---
name: investment-briefing
description: Use when a user asks a broad or under-specified investment question and the agent needs to clarify scope before analysis.
---

# Investment Briefing

## Overview

Turn an ambiguous investment question into a research brief. Do not analyze the instrument until the brief has enough context.

## When to Use

Use for questions like:

- "这个股票能买吗？"
- "这个 ETF 适合长期持有吗？"
- "亏了 20%，要不要补仓？"
- "帮我看看这个标的。"

## Required Inputs

Ask for:

1. 标的：代码 / 名称 / 市场 / 资产类型
2. 周期：短线 / 中线 / 长线
3. 仓位：无仓 / 轻仓 / 重仓 / 占总资产比例
4. 风险：最大可接受亏损比例或金额

Also clarify the intended decision: buy, hold, add, reduce, avoid, hedge, compare, or review.

## Workflow

1. Restate the user's question as a research task.
2. Identify missing boundary information.
3. Ask only the missing questions.
4. If the user insists on an answer without context, output `信息不足`.
5. Once context is available, route to the next skill.

## Output Format

```markdown
## 研究任务

- 标的：
- 决策：
- 周期：
- 当前仓位：
- 最大可接受亏损：

## 缺失信息

-

## 下一步

建议进入：[skill name]
```

## Common Mistakes

- Giving a buy or sell view from the first user sentence.
- Asking for too many unrelated details.
- Treating a ticker as enough context.
