#!/usr/bin/env python3
import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "investflow"
MCP = ROOT / "scripts" / "investflow-mcp"


def mcp_message(payload):
    body = json.dumps(payload).encode("utf-8")
    return b"Content-Length: " + str(len(body)).encode() + b"\r\n\r\n" + body


def parse_mcp_response(raw):
    marker = b"\r\n\r\n"
    _, body = raw.split(marker, 1)
    return json.loads(body.decode("utf-8"))


class Phase3Phase4Test(unittest.TestCase):
    def run_cli(self, *args, check=True):
        result = subprocess.run(
            [str(CLI), *args],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if check and result.returncode != 0:
            self.fail(f"command failed: {args}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}")
        return result

    def test_data_list_and_read_registered_source(self):
        listed = self.run_cli("--json", "data", "list")
        list_payload = json.loads(listed.stdout)
        self.assertIn("sample-market-snapshot", [item["id"] for item in list_payload["sources"]])

        shown = self.run_cli("--json", "data", "show", "sample-market-snapshot")
        show_payload = json.loads(shown.stdout)
        self.assertEqual(show_payload["id"], "sample-market-snapshot")
        self.assertTrue(show_payload["read_only"])
        self.assertTrue(show_payload["sample"])

        read = self.run_cli("--json", "data", "read", "sample-market-snapshot")
        read_payload = json.loads(read.stdout)
        self.assertEqual(read_payload["source"]["id"], "sample-market-snapshot")
        self.assertTrue(read_payload["sample"])
        self.assertIn("data", read_payload)

    def test_data_read_rejects_unknown_source(self):
        result = self.run_cli("--json", "data", "read", "../secret", check=False)
        self.assertNotEqual(result.returncode, 0)
        payload = json.loads(result.stdout)
        self.assertFalse(payload["ok"])
        self.assertIn("unknown data source", payload["error"])

    def test_mcp_manifest_and_tools_list(self):
        manifest = json.loads((ROOT / ".mcp.json").read_text(encoding="utf-8"))
        self.assertIn("investflow", manifest["mcpServers"])

        request = mcp_message({"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}})
        result = subprocess.run(
            [str(MCP)],
            cwd=ROOT,
            input=request,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        response = parse_mcp_response(result.stdout)
        tool_names = [tool["name"] for tool in response["result"]["tools"]]
        self.assertIn("investflow_list_data_sources", tool_names)
        self.assertIn("investflow_read_data_source", tool_names)
        self.assertIn("investflow_render_report", tool_names)

    def test_mcp_can_call_list_data_sources(self):
        request = mcp_message(
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {"name": "investflow_list_data_sources", "arguments": {}},
            }
        )
        result = subprocess.run(
            [str(MCP)],
            cwd=ROOT,
            input=request,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        response = parse_mcp_response(result.stdout)
        text = response["result"]["content"][0]["text"]
        payload = json.loads(text)
        self.assertIn("sample-market-snapshot", [item["id"] for item in payload["sources"]])

    def test_render_valid_report_to_html(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "report.html"
            result = self.run_cli("render", "templates/thesis-report.md", "--output", str(output))
            self.assertIn(str(output), result.stdout)
            html = output.read_text(encoding="utf-8")
            self.assertIn("<html", html)
            self.assertIn("InvestFlow", html)
            self.assertIn("not investment advice", html)
            self.assertIn("反方最强质疑", html)

    def test_render_rejects_invalid_report_unless_forced(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.md"
            output = Path(tmp) / "bad.html"
            bad.write_text("## 投资判断\n\n信息不足\n", encoding="utf-8")
            result = self.run_cli("render", str(bad), "--output", str(output), check=False)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(output.exists())

            forced = self.run_cli("render", str(bad), "--output", str(output), "--force")
            self.assertEqual(forced.returncode, 0)
            self.assertIn("not investment advice", output.read_text(encoding="utf-8"))

    def test_pack_list_and_validate(self):
        listed = self.run_cli("--json", "pack", "list")
        payload = json.loads(listed.stdout)
        self.assertIn("long-term-investing", [item["name"] for item in payload["packs"]])

        validated = self.run_cli("--json", "pack", "validate", "packs/community/long-term-investing")
        validation = json.loads(validated.stdout)
        self.assertTrue(validation["ok"])
        self.assertEqual(validation["name"], "long-term-investing")


if __name__ == "__main__":
    unittest.main()
