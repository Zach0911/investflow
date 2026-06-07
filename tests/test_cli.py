#!/usr/bin/env python3
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "investflow"


class InvestFlowCliTest(unittest.TestCase):
    def run_cli(self, *args, env=None, check=True):
        merged_env = os.environ.copy()
        if env:
            merged_env.update(env)
        result = subprocess.run(
            [str(CLI), *args],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=merged_env,
        )
        if check and result.returncode != 0:
            self.fail(
                f"command failed: {args}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
            )
        return result

    def test_help_lists_core_commands(self):
        result = self.run_cli("--help")
        self.assertIn("doctor", result.stdout)
        self.assertIn("quickstart", result.stdout)
        self.assertIn("list", result.stdout)
        self.assertIn("new", result.stdout)
        self.assertIn("validate", result.stdout)
        self.assertIn("install", result.stdout)

    def test_json_doctor_reports_project_inventory(self):
        result = self.run_cli("--json", "doctor")
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["skills"], 8)
        self.assertGreaterEqual(payload["templates"], 4)
        self.assertGreaterEqual(payload["examples"], 7)
        self.assertTrue(payload["plugin_manifest"])
        self.assertTrue(payload["codex_installer"])

    def test_list_skills_outputs_known_skill(self):
        result = self.run_cli("list", "skills")
        self.assertIn("investment-briefing", result.stdout)
        self.assertIn("risk-review", result.stdout)

    def test_json_list_templates_outputs_paths(self):
        result = self.run_cli("--json", "list", "templates")
        payload = json.loads(result.stdout)
        self.assertIn("templates/thesis-report.md", payload["items"])
        self.assertIn("templates/risk-review.md", payload["items"])

    def test_quickstart_creates_markdown_and_html_demo(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "quickstart"
            result = self.run_cli("quickstart", "--output-dir", str(output_dir))
            self.assertIn("InvestFlow quickstart created", result.stdout)
            markdown = output_dir / "thesis.md"
            html_report = output_dir / "thesis.html"
            self.assertTrue(markdown.exists())
            self.assertTrue(html_report.exists())
            self.assertIn("## 投资判断", markdown.read_text(encoding="utf-8"))
            self.assertIn("<!doctype html>", html_report.read_text(encoding="utf-8"))

            second = self.run_cli("quickstart", "--output-dir", str(output_dir), check=False)
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("Refusing to overwrite", second.stderr)

    def test_json_quickstart_reports_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "quickstart"
            result = self.run_cli("--json", "quickstart", "--output-dir", str(output_dir))
            payload = json.loads(result.stdout)
            self.assertTrue(payload["ok"])
            self.assertEqual(payload["missing"], [])
            self.assertEqual(payload["violations"], [])
            self.assertTrue(Path(payload["markdown"]).exists())
            self.assertTrue(Path(payload["html"]).exists())

    def test_new_thesis_writes_report_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "thesis.md"
            result = self.run_cli("new", "thesis", "--output", str(output))
            self.assertIn(str(output), result.stdout)
            text = output.read_text(encoding="utf-8")
            self.assertIn("## 投资判断", text)
            self.assertIn("## 反方最强质疑", text)

            second = self.run_cli("new", "thesis", "--output", str(output), check=False)
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("already exists", second.stderr)

            forced = self.run_cli("new", "thesis", "--output", str(output), "--force")
            self.assertIn(str(output), forced.stdout)

    def test_new_brief_stdout(self):
        result = self.run_cli("new", "brief")
        self.assertIn("## 投资问题", result.stdout)
        self.assertIn("## 数据基础", result.stdout)

    def test_validate_good_report_passes_json(self):
        template = ROOT / "templates" / "thesis-report.md"
        result = self.run_cli("--json", "validate", str(template))
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["missing"], [])
        self.assertEqual(payload["violations"], [])

    def test_validate_missing_sections_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "bad.md"
            report.write_text("## 投资判断\n\n谨慎观察\n", encoding="utf-8")
            result = self.run_cli("--json", "validate", str(report), check=False)
            self.assertNotEqual(result.returncode, 0)
            payload = json.loads(result.stdout)
            self.assertFalse(payload["ok"])
            self.assertIn("## 反方最强质疑", payload["missing"])

    def test_validate_standalone_buy_sell_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "unsafe.md"
            report.write_text(
                "\n".join(
                    [
                        "## 投资判断",
                        "买入",
                        "## 关键依据",
                        "- x",
                        "## 反方最强质疑",
                        "- x",
                        "## 主要风险",
                        "- x",
                        "## 仓位与风控",
                        "- x",
                        "## 最终结论",
                        "- x",
                    ]
                ),
                encoding="utf-8",
            )
            result = self.run_cli("--json", "validate", str(report), check=False)
            self.assertNotEqual(result.returncode, 0)
            payload = json.loads(result.stdout)
            self.assertIn("standalone buy/sell conclusion", payload["violations"])

    def test_install_codex_uses_target_env(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = self.run_cli(
                "install",
                "codex",
                env={"CODEX_SKILLS_DIR": tmp},
            )
            self.assertIn("Installed 8 InvestFlow skills", result.stdout)
            self.assertTrue((Path(tmp) / "investment-briefing" / "SKILL.md").exists())
            self.assertTrue((Path(tmp) / "risk-review" / "agents" / "openai.yaml").exists())


if __name__ == "__main__":
    unittest.main()
