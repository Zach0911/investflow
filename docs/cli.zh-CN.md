# InvestFlow CLI 使用指南

InvestFlow CLI 用于本地报告搭建、结构校验、HTML 渲染、示例数据读取和 Codex skills 同步。

它不联网获取行情，不连接券商账户，不执行交易，也不生成投资建议。

## 1. 三分钟跑通

在项目根目录执行：

```bash
./scripts/investflow quickstart
```

默认会生成：

```text
work/quickstart/thesis.md
work/quickstart/thesis.html
```

如果目录里已经存在同名文件，CLI 会拒绝覆盖。确认要重建时使用：

```bash
./scripts/investflow quickstart --force
```

指定输出目录：

```bash
./scripts/investflow quickstart --output-dir work/demo
```

## 2. 常用命令

| 命令 | 用途 |
|---|---|
| `./scripts/investflow doctor` | 检查项目结构、skills、templates、MCP 和社区包是否齐全。 |
| `./scripts/investflow scenario list` | 查看 10 个对标 Superpowers 的优化场景。 |
| `./scripts/investflow scenario show evidence-audit` | 查看单个场景的命令和计划文档。 |
| `./scripts/investflow list skills` | 查看内置 skills。 |
| `./scripts/investflow list templates` | 查看可用报告模板。 |
| `./scripts/investflow list examples` | 查看示例报告。 |
| `./scripts/investflow new thesis --output work/thesis.md` | 生成 thesis 报告骨架。 |
| `./scripts/investflow validate work/thesis.md` | 校验报告是否包含必要章节和边界。 |
| `./scripts/investflow audit work/thesis.md` | 审计报告是否包含数据来源、时间戳、反方观点、失效条件和复盘条件。 |
| `./scripts/investflow render work/thesis.md --output work/thesis.html` | 将 Markdown 报告渲染为 HTML。 |
| `./scripts/investflow data list` | 查看注册的只读数据源。 |
| `./scripts/investflow data read sample-market-snapshot` | 读取示例数据源。 |
| `./scripts/investflow pack list` | 查看社区 skill packs。 |
| `./scripts/investflow install codex` | 将内置 skills 同步到 Codex。 |

## 3. 推荐工作流

### 3.1 生成报告

```bash
./scripts/investflow new thesis --output work/my-thesis.md
```

其他可用模板：

```bash
./scripts/investflow new design --output work/research-design.md
./scripts/investflow new plan --output work/research-plan.md
./scripts/investflow new brief --output work/research-brief.md
./scripts/investflow new risk-review --output work/risk-review.md
./scripts/investflow new decision-gate --output work/decision-gate.md
./scripts/investflow new multi-agent --output work/multi-agent.md
./scripts/investflow new data-brief --output work/data-brief.md
./scripts/investflow new lifecycle --output work/lifecycle.md
./scripts/investflow new pack-proposal --output work/pack-proposal.md
./scripts/investflow new platform-adapter --output work/platform-adapter.md
./scripts/investflow new postmortem --output work/postmortem.md
./scripts/investflow new postmortem-loop --output work/postmortem-loop.md
```

### 3.2 填写报告

建议先明确：

- 标的：股票、ETF、基金、行业或组合。
- 决策：研究、持有、减仓、复盘、比较等。
- 周期：短期、中期、长期。
- 仓位：已有仓位或计划仓位。
- 风险承受能力：最大可接受回撤、流动性要求、集中度限制。
- 数据基础：数据来源、时间戳、缺失信息。

### 3.3 校验报告

```bash
./scripts/investflow validate work/my-thesis.md
```

校验重点：

- 是否包含 `投资判断`、`关键依据`、`反方最强质疑`、`主要风险`、`仓位与风控`、`最终结论`。
- 是否避免单独使用 `买入` / `卖出` 作为标题式结论。

### 3.4 审计证据质量

```bash
./scripts/investflow audit work/my-thesis.md
```

审计重点：

- 是否有数据来源。
- 是否有数据时间戳或截至日期。
- 是否有反方最强质疑。
- 是否有失效条件。
- 是否有复盘条件。
- 是否有仓位边界。

### 3.5 渲染报告

```bash
./scripts/investflow render work/my-thesis.md --output work/my-thesis.html
```

如果报告尚未通过校验，但仍需预览 HTML：

```bash
./scripts/investflow render work/my-thesis.md --output work/my-thesis.html --force
```

## 4. JSON 输出

适合被其他 Agent、脚本或 MCP 工具调用：

```bash
./scripts/investflow --json doctor
./scripts/investflow --json quickstart --output-dir work/demo
./scripts/investflow --json validate work/my-thesis.md
./scripts/investflow --json audit work/my-thesis.md
./scripts/investflow --json scenario list
./scripts/investflow --json list skills
```

## 5. 场景发现

查看全部场景：

```bash
./scripts/investflow scenario list
```

查看单个场景：

```bash
./scripts/investflow scenario show research-design
```

## 6. 查看完整示例

可以先阅读完整示例报告：

```text
examples/full-thesis-report-example.zh-CN.md
```

该示例使用虚构标的，只用于展示 InvestFlow 报告结构，不构成投资建议。
