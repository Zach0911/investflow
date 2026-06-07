# InvestFlow

[English](README.md) | [中文](README.zh-CN.md)

[![Validate](https://github.com/Zach0911/investflow/actions/workflows/validate.yml/badge.svg)](https://github.com/Zach0911/investflow/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-early%20MVP-blue.svg)](#项目状态)

InvestFlow 是一个面向投资 Agent 的开源 skills framework 与研究方法论。

它的目标不是让 AI 更快回答“能不能买”，而是让 AI 在给出投资研究结论之前，先澄清问题、确认数据基础、构建 thesis、进行反方风险审查，并输出可复盘的研究记录。

InvestFlow 不构成投资建议，不执行交易，不管理账户，不承诺收益，也不能替代持牌金融顾问。

## 项目状态

当前版本是 early MVP，已经具备可运行的本地工具链：

| 模块 | 状态 |
|---|---|
| 核心 skills | 8 个，覆盖澄清、公司研究、thesis、估值、风险、决策压测和复盘 |
| 报告模板 | 13 个，覆盖基础投研报告和 10 个对标 Superpowers 的工作流场景 |
| 示例 | 8 个，包括完整 thesis 示例、亏损持仓、ETF、组合和复盘 |
| CLI | 可生成、校验、审计、渲染报告，并列出场景和资源 |
| MCP | 本地只读基础版，可列出数据源、读取示例数据、渲染报告 |
| 社区包 | 1 个示例包，支持 manifest 校验 |

当前优先级是打磨 Agent 工作流基础设施，而不是接入交易、荐股或实时行情。

版本记录见：[CHANGELOG.md](CHANGELOG.md)。

## 适合谁

- 个人投资者：把 AI 投研从随口问答变成结构化研究记录。
- AI Agent 开发者：把投资研究流程封装成可复用 skill、CLI 和 MCP 工具。
- 投研内容创作者：用统一模板生成可审查、可复盘的研究稿。
- 开源贡献者：贡献新的投资研究 skill pack、模板、示例和边界测试。

## 不适合什么

- 不适合作为荐股工具。
- 不适合作为自动交易系统。
- 不适合作为实时行情或财务数据终端。
- 不替代持牌投顾、税务、法律或会计建议。

## 为什么需要它

越来越多个人投资者开始用 AI 研究股票、ETF、基金、行业和投资组合。主要风险不是 AI 说得太少，而是 AI 在信息不足时说得太满。

InvestFlow 为投资 Agent 提供一套更严格的工作方式：

- 在给出可行动判断前，先确认标的、周期、仓位和风险承受能力。
- 区分事实、假设、thesis、估值、风险和缺失信息。
- 在结论前强制加入最强反方观点。
- 为每个可行动判断附加失效条件和复盘触发条件。
- 将输出沉淀为可复用的投资研究记录。

## 核心 Skills

| Skill | 用途 |
|---|---|
| `using-investflow` | 负责投资任务路由，并执行项目级边界规则。 |
| `investment-briefing` | 在分析前澄清投资问题。 |
| `company-research` | 结构化分析商业模式、财务质量、行业位置和治理风险。 |
| `thesis-builder` | 将研究内容转化为可验证的投资 thesis。 |
| `valuation-check` | 检查价格、估值和关键假设是否匹配。 |
| `risk-review` | 从风险优先和反方视角审查投资观点。 |
| `dialectic-investment-decision` | 对买入、持有、加仓、减仓、回避、对冲或比较决策进行压测。 |
| `postmortem` | 对已有投资结果进行复盘。 |

## 使用场景

InvestFlow 适合用于需要 AI Agent 先完成研究流程、再输出判断的投资研究场景。

| 场景 | 典型问题 | 建议流程 |
|---|---|---|
| 澄清模糊股票问题 | “这个股票还能买吗？” | `investment-briefing` -> `company-research` -> `risk-review` |
| 研究一家公司 | “帮我看看这家公司的业务质量。” | `company-research` -> `thesis-builder` |
| 构建投资 thesis | “这个公司真正可投资的逻辑是什么？” | `company-research` -> `thesis-builder` -> `risk-review` |
| 检查估值风险 | “这个 ETF / 股票现在贵不贵？” | `valuation-check` -> `risk-review` |
| 复盘亏损持仓 | “我已经亏了 25%，要不要补仓？” | `investment-briefing` -> `risk-review` -> `dialectic-investment-decision` |
| 审查组合集中度 | “我科技股仓位太高，要不要降一点？” | `risk-review` -> `dialectic-investment-decision` |
| 比较两个资产 | “哪个更适合我的长期计划？” | `investment-briefing` -> `valuation-check` -> `risk-review` |
| 复盘历史决策 | “这次投资错误本来能避免吗？” | `postmortem` |

这些流程是研究工作流，不是交易指令。如果判断依赖当前行情、估值、财报、新闻或政策信息，Agent 应先核验数据来源和时间。

### 10 个工作流场景

对标 Superpowers 后，InvestFlow 也提供面向投资 Agent 的工作流脚手架：

| 场景 | CLI 入口 |
|---|---|
| 投资研究任务书 | `./scripts/investflow new design` |
| 投研执行计划 | `./scripts/investflow new plan` |
| 证据优先审计 | `./scripts/investflow audit report.md` |
| 结论前强制反方审查 | `./scripts/investflow new decision-gate` |
| 多 Agent 分工研究 | `./scripts/investflow new multi-agent` |
| 数据到报告联动 | `./scripts/investflow new data-brief` |
| 报告生命周期 | `./scripts/investflow new lifecycle` |
| 社区 skill pack 贡献 | `./scripts/investflow new pack-proposal` |
| 多平台适配 | `./scripts/investflow new platform-adapter` |
| 投资复盘闭环 | `./scripts/investflow new postmortem-loop` |

完整说明见：[使用场景总览](docs/scenarios.zh-CN.md)。

## 项目结构

```text
investflow/
├── README.md
├── README.zh-CN.md
├── DISCLAIMER.md
├── .mcp.json
├── .codex-plugin/
├── AGENTS.md
├── CONTRIBUTING.md
├── data/
├── docs/
├── examples/
├── packs/
├── scripts/
├── skills/
│   ├── using-investflow/
│   ├── investment-briefing/
│   ├── company-research/
│   ├── thesis-builder/
│   ├── valuation-check/
│   ├── risk-review/
│   ├── dialectic-investment-decision/
│   └── postmortem/
├── templates/
└── tests/
```

更多完整示例见 [`examples/`](examples/)，包括完整 thesis 报告、亏损持仓复盘、ETF 长期持有审查、公司研究到 thesis、投资复盘等。

## 快速开始

先在本地跑通一次完整链路：

```bash
git clone https://github.com/Zach0911/investflow.git
cd investflow
./scripts/investflow quickstart
```

该命令会生成：

```text
work/quickstart/thesis.md
work/quickstart/thesis.html
```

然后可以继续校验和渲染：

```bash
./scripts/investflow validate work/quickstart/thesis.md
./scripts/investflow render work/quickstart/thesis.md --output work/quickstart/thesis.html
```

如果你想直接看一份更完整的报告示例，可以阅读：

```text
examples/full-thesis-report-example.zh-CN.md
```

Agent 使用 InvestFlow 时，推荐流程是：

1. 选择与任务匹配的 skill。
2. 阅读对应的 `SKILL.md`。
3. 在输出投资分析前，先询问必要的边界问题。
4. 使用 `templates/` 中的模板整理最终输出。
5. 使用 CLI 校验报告结构。
6. 如果判断依赖当前市场数据，需要注明数据来源和时间。

示例 prompt：

```text
使用 InvestFlow 分析我是否应该继续持有这个 ETF。
```

如果用户没有提供标的、周期、仓位和风险承受能力，Agent 应先补问，而不是直接给出投资判断。

## CLI

InvestFlow 提供一个轻量本地 CLI，用于报告搭建和结构校验：

```bash
./scripts/investflow --help
./scripts/investflow doctor
./scripts/investflow quickstart
./scripts/investflow scenario list
./scripts/investflow list skills
./scripts/investflow new thesis --output work/thesis.md
./scripts/investflow validate work/thesis.md
./scripts/investflow audit work/thesis.md
./scripts/investflow data list
./scripts/investflow data read sample-market-snapshot
./scripts/investflow render work/thesis.md --output work/thesis.html
./scripts/investflow pack list
./scripts/investflow install codex
```

CLI 不获取行情数据，不生成投资建议，也不执行交易。它只处理本地 skills、templates、examples 和 Markdown 报告。

完整 CLI 用法见：[CLI 使用指南](docs/cli.zh-CN.md)。
10 个对标 Superpowers 的优化场景见：[使用场景总览](docs/scenarios.zh-CN.md)。
命令契约和验收标准见：[第二阶段 CLI 需求设计文档](docs/phase-2-cli-requirements.zh-CN.md)。
只读数据、MCP、报告生成和社区包边界见：[第三阶段 MCP 与只读数据连接器需求设计文档](docs/phase-3-mcp-data-requirements.zh-CN.md) 与 [第四阶段报告生成与社区技能包需求设计文档](docs/phase-4-report-community-requirements.zh-CN.md)。

## MCP 和只读数据连接器

InvestFlow 已包含本地 MCP server manifest：

```text
.mcp.json
```

MCP server 提供只读工具：列出注册数据源、读取注册示例数据、渲染本地 Markdown 报告。它不会连接券商账户，不获取实时行情，也不执行交易。

## 安装到 Codex

将项目内置 skills 安装到 Codex 本地 skill 目录：

```bash
./scripts/install-codex-skills.sh
```

默认安装到 `~/.codex/skills`。如需指定目标目录，可以使用 `CODEX_SKILLS_DIR`：

```bash
CODEX_SKILLS_DIR=/path/to/skills ./scripts/install-codex-skills.sh
```

安装脚本采用复制方式，不是软链接。修改 `skills/` 源码后，需要重新运行安装脚本，Codex 才会使用最新版本。

更多克隆、更新和验证说明见：[安装说明](docs/installation.zh-CN.md)。

## 决策标签

InvestFlow 避免输出单独的“买入”或“卖出”结论。请使用有边界的标签：

- `信息不足`
- `不建议参与`
- `谨慎观察`
- `低仓位试错`
- `分批参与`
- `持有但设退出条件`
- `减仓控制风险`

每个可行动标签都必须包含前提假设、仓位建议、失效条件和退出 / 复盘条件。

## 路线图

- 第一阶段：skills framework、模板、示例和边界测试。
- 第二阶段：用于报告脚手架和校验的 CLI。
- 第三阶段：MCP 与只读数据连接器。
- 第四阶段：报告生成和社区 skill packs。

## 贡献

欢迎贡献：

- 新的投资研究 skill。
- 新的报告模板或完整示例。
- 社区 skill pack。
- 更严格的边界测试。
- 平台适配文档。

贡献前请阅读：[CONTRIBUTING.md](CONTRIBUTING.md) 和 [合规边界](docs/compliance-boundaries.md)。

## 许可证

MIT License.
