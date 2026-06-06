#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: str) -> str:
    file_path = ROOT / path
    if not file_path.exists():
        fail(f"missing file: {path}")
    return file_path.read_text(encoding="utf-8")


def require(path: str, *patterns: str) -> str:
    text = read(path)
    for pattern in patterns:
        if not re.search(pattern, text, re.MULTILINE):
            fail(f"{path} missing pattern: {pattern}")
    return text


def skill(name: str) -> str:
    return require(
        f"skills/{name}/SKILL.md",
        r"^---$",
        rf"^name: {re.escape(name)}$",
        r"^description: Use when ",
        r"## .*",
    )


def assert_route(router: str, user_need: str, expected_skill: str) -> None:
    if user_need not in router or expected_skill not in router:
        fail(f"using-investflow route missing: {user_need} -> {expected_skill}")


def main() -> None:
    if not ROOT.exists():
        fail(f"missing project root: {ROOT}")

    plugin = json.loads(read(".codex-plugin/plugin.json"))
    if plugin["name"] != "investflow":
        fail("plugin name must be investflow")
    if plugin.get("skills") != "./skills/":
        fail("plugin must expose ./skills/")
    if "mcpServers" in plugin or "apps" in plugin:
        fail("plugin must not claim MCP/apps before those files exist")

    require("README.md", r"skills framework", r"not investment advice", r"Decision Labels", r"Phase 2: CLI", r"Phase 3: MCP")
    require("DISCLAIMER.md", r"not investment advice", r"does not execute trades", r"Users are responsible")
    require("AGENTS.md", r"Do not provide standalone buy or sell conclusions", r"Verify current data", r"Every actionable investment output must include")
    require("LICENSE", r"License to be selected before public release")
    require(".gitignore", r"\.DS_Store")

    using = skill("using-investflow")
    for user_need, expected_skill in [
        ("Vague investment question", "investment-briefing"),
        ("Business or company analysis", "company-research"),
        ("Build an investment thesis", "thesis-builder"),
        ("Check valuation", "valuation-check"),
        ("Challenge a view", "risk-review"),
        ("Decide buy / hold / reduce / avoid", "dialectic-investment-decision"),
        ("Review past decision", "postmortem"),
    ]:
        assert_route(using, user_need, expected_skill)

    for boundary in ["Instrument", "Decision", "Horizon", "Position", "Risk", "Data basis"]:
        if boundary not in using:
            fail(f"using-investflow missing boundary: {boundary}")

    checks = {
        "investment-briefing": ["标的", "周期", "仓位", "风险", "信息不足"],
        "company-research": ["business model", "financial quality", "competitive position", "governance", "Current Data Rule"],
        "thesis-builder": ["facts from assumptions", "catalysts", "失效条件", "risk-review"],
        "valuation-check": ["Stock", "ETF / Fund", "Bond", "Crypto", "data timestamp", "情景分析"],
        "risk-review": ["反方", "behavioral risks", "FOMO", "averaging down", "concentration", "修正建议"],
        "dialectic-investment-decision": ["Pro", "Con", "Arbiter", "Current Data Rule", "Do not output standalone buy or sell commands", "Do not output `买入` or `卖出`", "仓位", "失效条件", "复盘条件"],
        "postmortem": ["decision process", "outcome", "Original thesis", "错误来源", "下次行动规则"],
    }

    for skill_name, terms in checks.items():
        text = skill(skill_name)
        for term in terms:
            if term not in text:
                fail(f"{skill_name} missing: {term}")

    templates = {
        "templates/research-brief.md": ["投资问题", "数据基础", "缺失信息"],
        "templates/thesis-report.md": ["投资判断", "反方最强质疑", "仓位与风控", "最终结论"],
        "templates/risk-review.md": ["原始观点", "反方最强质疑", "行为偏差"],
        "templates/postmortem.md": ["原始决策", "实际结果", "错误来源", "下次改进"],
    }
    for path, headings in templates.items():
        text = read(path)
        for heading in headings:
            if heading not in text:
                fail(f"{path} missing heading: {heading}")

    scenarios = {
        "examples/stock-research-example.md": ["信息不足", "标的", "周期", "仓位", "风险"],
        "examples/etf-research-example.md": ["信息不足", "跟踪指数", "费率", "流动性"],
        "examples/portfolio-review-example.md": ["信息不足", "科技股占比", "最大可接受组合回撤"],
        "tests/skill-boundary-cases.md": ["Case 1", "Case 2", "Case 3", "Expected behavior"],
        "tests/e2e-scenarios.md": ["Vague stock question", "Actionable decision", "Past decision review"],
    }
    for path, terms in scenarios.items():
        text = read(path)
        for term in terms:
            if term not in text:
                fail(f"{path} missing scenario term: {term}")

    print(f"E2E InvestFlow scenarios passed: {ROOT}")


if __name__ == "__main__":
    main()
