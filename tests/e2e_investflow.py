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
    require(
        f"skills/{name}/agents/openai.yaml",
        rf'default_prompt: "Use \${re.escape(name)}',
        r"allow_implicit_invocation: true",
    )
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
    if plugin.get("mcpServers") != "./.mcp.json":
        fail("plugin must expose ./.mcp.json")
    if "apps" in plugin:
        fail("plugin must not claim apps before those files exist")

    require("README.md", r"skills framework", r"not investment advice", r"Use Cases", r"Review a losing position", r"portfolio concentration", r"\./scripts/investflow doctor", r"\./scripts/investflow quickstart", r"\./scripts/investflow scenario list", r"\./scripts/investflow audit", r"\./scripts/investflow data list", r"docs/cli\.md", r"docs/scenarios\.zh-CN\.md", r"full thesis report", r"MCP and Data Connectors", r"Phase 2 CLI Requirements", r"Decision Labels", r"Phase 2: CLI", r"Phase 3: MCP")
    require("README.md", r"README\.zh-CN\.md")
    require("README.md", r"docs/installation\.md", r"run the installer again")
    require("README.zh-CN.md", r"InvestFlow 是一个面向投资 Agent", r"不构成投资建议", r"核心 Skills", r"使用场景", r"复盘亏损持仓", r"组合集中度", r"\./scripts/investflow doctor", r"\./scripts/investflow quickstart", r"\./scripts/investflow scenario list", r"\./scripts/investflow audit", r"\./scripts/investflow data list", r"docs/cli\.zh-CN\.md", r"docs/scenarios\.zh-CN\.md", r"完整 thesis 报告", r"MCP 和只读数据连接器", r"第二阶段 CLI 需求设计文档", r"决策标签", r"README\.md")
    require("README.zh-CN.md", r"docs/installation\.zh-CN\.md", r"重新运行安装脚本")
    require("docs/installation.md", r"git clone https://github.com/Zach0911/investflow.git", r"The installer copies files", r"does not delete unrelated skills")
    require("docs/installation.zh-CN.md", r"安装脚本采用复制方式", r"不会删除", r"验证项目", r"使用 CLI")
    require("docs/phase-2-cli-requirements.zh-CN.md", r"investflow doctor", r"investflow quickstart", r"investflow scenario", r"investflow validate", r"investflow audit", r"验收标准")
    require("docs/cli.md", r"Three-Minute Quick Start", r"Common Commands", r"JSON Output", r"Scenario Discovery")
    require("docs/cli.zh-CN.md", r"三分钟跑通", r"常用命令", r"JSON 输出", r"场景发现")
    require("docs/scenarios.zh-CN.md", r"投资研究任务书", r"证据优先审计", r"多 Agent 分工研究", r"投资复盘闭环")
    require("docs/platform-adapters.md", r"Current Support", r"Codex", r"MCP Client", r"Generic Agent")
    require("packs/community/README.md", r"Contribution Flow", r"investflow pack validate")
    require("docs/phase-3-mcp-data-requirements.zh-CN.md", r"investflow data read", r"scripts/investflow-mcp", r"验收标准")
    require("docs/phase-4-report-community-requirements.zh-CN.md", r"investflow render", r"pack validate", r"验收标准")
    require(".mcp.json", r"investflow", r"scripts/investflow-mcp")
    require("DISCLAIMER.md", r"not investment advice", r"does not execute trades", r"Users are responsible")
    require("AGENTS.md", r"Do not provide standalone buy or sell conclusions", r"Verify current data", r"Every actionable investment output must include")
    require("LICENSE", r"MIT License", r"Copyright \(c\) 2026 Zach0911")
    require(".github/workflows/validate.yml", r"\./scripts/validate\.sh", r"actions/checkout@v4", r"Codex plugin manifest passed")
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
        "templates/research-design.md": ["投资研究任务书", "待确认边界", "下一步路由"],
        "templates/research-plan.md": ["投研执行计划", "执行步骤", "验证关口"],
        "templates/thesis-report.md": ["投资判断", "反方最强质疑", "仓位与风控", "最终结论"],
        "templates/decision-gate.md": ["结论前检查", "禁止输出", "最终结论条件"],
        "templates/multi-agent-research.md": ["多 Agent 投研分工", "Data Agent", "Arbiter Agent"],
        "templates/data-linked-brief.md": ["数据到报告联动", "数据源清单", "写入报告位置"],
        "templates/report-lifecycle.md": ["报告生命周期", "当前状态", "复盘触发"],
        "templates/community-pack-proposal.md": ["社区 Skill Pack 提案", "边界声明", "验收标准"],
        "templates/platform-adapter-checklist.md": ["平台适配清单", "Codex", "MCP Client"],
        "templates/risk-review.md": ["原始观点", "反方最强质疑", "行为偏差"],
        "templates/postmortem.md": ["原始决策", "实际结果", "错误来源", "下次改进"],
        "templates/postmortem-loop.md": ["投资复盘闭环", "原始 Thesis", "下次行动规则"],
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
        "examples/losing-position-review-example.md": ["亏了 25%", "补仓", "反方最强质疑"],
        "examples/company-to-thesis-example.md": ["Company Research to Thesis", "核心 Thesis", "失效条件"],
        "examples/etf-long-term-review-example.md": ["ETF Long-Term Review", "持仓集中度", "复盘条件"],
        "examples/investment-postmortem-example.md": ["Investment Postmortem", "错误来源", "下次行动规则"],
        "examples/full-thesis-report-example.zh-CN.md": ["完整 Thesis 报告示例", "投资判断", "反方最强质疑", "仓位与风控", "数据来源", "失效条件"],
        "tests/skill-boundary-cases.md": ["Case 1", "Case 2", "Case 3", "Expected behavior"],
        "tests/e2e-scenarios.md": ["Vague stock question", "Actionable decision", "Past decision review"],
    }
    for path, terms in scenarios.items():
        text = read(path)
        for term in terms:
            if term not in text:
                fail(f"{path} missing scenario term: {term}")

    plans = [
        "docs/superpowers/plans/2026-06-07-research-design.md",
        "docs/superpowers/plans/2026-06-07-research-plan.md",
        "docs/superpowers/plans/2026-06-07-evidence-audit.md",
        "docs/superpowers/plans/2026-06-07-decision-gate.md",
        "docs/superpowers/plans/2026-06-07-multi-agent-research.md",
        "docs/superpowers/plans/2026-06-07-data-linked-report.md",
        "docs/superpowers/plans/2026-06-07-report-lifecycle.md",
        "docs/superpowers/plans/2026-06-07-community-pack-contribution.md",
        "docs/superpowers/plans/2026-06-07-platform-adapters.md",
        "docs/superpowers/plans/2026-06-07-postmortem-loop.md",
    ]
    for path in plans:
        require(path, r"Implementation Plan", r"\*\*Goal:\*\*", r"\*\*Architecture:\*\*", r"Run: `\./scripts/validate\.sh`")

    print(f"E2E InvestFlow scenarios passed: {ROOT}")


if __name__ == "__main__":
    main()
