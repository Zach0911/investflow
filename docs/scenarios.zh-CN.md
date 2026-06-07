# InvestFlow 对标 Superpowers 的 10 个优化场景

本文档定义 InvestFlow 下一阶段的 10 个完整使用场景。每个场景都有对应计划文档、模板或 CLI 入口，目标是把 InvestFlow 从 skills 集合推进为投资 Agent 工作流基础设施。

## 场景总览

| 编号 | 场景 | 用户问题 | 可用入口 | 状态 |
|---|---|---|---|---|
| 1 | 投资研究任务书 | “帮我看看这个标的值不值得研究？” | `investflow new design` | 已完成基础版 |
| 2 | 投研执行计划 | “确认研究范围后，接下来怎么做？” | `investflow new plan` | 已完成基础版 |
| 3 | 证据优先审计 | “这份报告有没有证据、时间戳和反方观点？” | `investflow audit report.md` | 已完成基础版 |
| 4 | 结论前强制反方审查 | “输出结论前，先帮我找最大漏洞。” | `investflow new decision-gate` | 已完成基础版 |
| 5 | 多 Agent 分工研究 | “让不同 Agent 分别做数据、公司、估值、风险审查。” | `investflow new multi-agent` | 已完成基础版 |
| 6 | 数据到报告联动 | “把读取到的数据写进报告的数据基础部分。” | `investflow new data-brief` | 已完成基础版 |
| 7 | 报告生命周期 | “这份报告现在是草稿、已审查还是待复盘？” | `investflow new lifecycle` | 已完成基础版 |
| 8 | 社区 skill pack 贡献 | “我想贡献一个自己的投资方法包。” | `investflow new pack-proposal` | 已完成基础版 |
| 9 | 多平台适配 | “除了 Codex，其他 Agent 平台怎么使用？” | `investflow new platform-adapter` | 已完成基础版 |
| 10 | 投资复盘闭环 | “原 thesis 到结果之间发生了什么？” | `investflow new postmortem-loop` | 已完成基础版 |

## 设计原则

- 每个场景先生成结构化文档，再进入分析或实现。
- 当前所有能力保持只读，不接券商账户，不执行交易。
- 对当前价格、财报、新闻、政策和基金持仓的判断必须标注来源和时间。
- 没有反方审查，不输出最终结论。
- 没有失效条件、仓位边界和复盘条件，不输出可行动标签。

## 对应计划文档

| 场景 | 计划文档 |
|---|---|
| 投资研究任务书 | `docs/superpowers/plans/2026-06-07-research-design.md` |
| 投研执行计划 | `docs/superpowers/plans/2026-06-07-research-plan.md` |
| 证据优先审计 | `docs/superpowers/plans/2026-06-07-evidence-audit.md` |
| 结论前强制反方审查 | `docs/superpowers/plans/2026-06-07-decision-gate.md` |
| 多 Agent 分工研究 | `docs/superpowers/plans/2026-06-07-multi-agent-research.md` |
| 数据到报告联动 | `docs/superpowers/plans/2026-06-07-data-linked-report.md` |
| 报告生命周期 | `docs/superpowers/plans/2026-06-07-report-lifecycle.md` |
| 社区 skill pack 贡献 | `docs/superpowers/plans/2026-06-07-community-pack-contribution.md` |
| 多平台适配 | `docs/superpowers/plans/2026-06-07-platform-adapters.md` |
| 投资复盘闭环 | `docs/superpowers/plans/2026-06-07-postmortem-loop.md` |
