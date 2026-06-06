# InvestFlow

[English](README.md) | [中文](README.zh-CN.md)

InvestFlow 是一个面向投资 Agent 的开源 skills framework 与研究方法论。

它的目标不是让 AI 更快回答“能不能买”，而是让 AI 在给出投资研究结论之前，先澄清问题、确认数据基础、构建 thesis、进行反方风险审查，并输出可复盘的研究记录。

InvestFlow 不构成投资建议，不执行交易，不管理账户，不承诺收益，也不能替代持牌金融顾问。

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

## 项目结构

```text
investflow/
├── README.md
├── README.zh-CN.md
├── DISCLAIMER.md
├── .codex-plugin/
├── AGENTS.md
├── CONTRIBUTING.md
├── docs/
├── examples/
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

## 快速开始

1. 选择与任务匹配的 skill。
2. 阅读对应的 `SKILL.md`。
3. 在输出投资分析前，先询问必要的边界问题。
4. 使用 `templates/` 中的模板整理最终输出。
5. 如果判断依赖当前市场数据，需要注明数据来源和时间。

示例 prompt：

```text
使用 InvestFlow 分析我是否应该继续持有这个 ETF。
```

如果用户没有提供标的、周期、仓位和风险承受能力，Agent 应先补问，而不是直接给出投资判断。

## 安装到 Codex

将项目内置 skills 安装到 Codex 本地 skill 目录：

```bash
./scripts/install-codex-skills.sh
```

默认安装到 `~/.codex/skills`。如需指定目标目录，可以使用 `CODEX_SKILLS_DIR`：

```bash
CODEX_SKILLS_DIR=/path/to/skills ./scripts/install-codex-skills.sh
```

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

## 许可证

正式发布前需要确认开源许可证。
