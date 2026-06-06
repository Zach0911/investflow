---
name: dialectic-investment-decision
description: Use when a user asks to decide, compare, buy, hold, add, reduce, avoid, hedge, or pressure-test an investment action.
---

# Dialectic Investment Decision

## Overview

Use pro, con, and arbiter roles to pressure-test an investment action. The final answer must be bounded and conditional.

## Required Boundary Check

Before analysis, confirm:

- Instrument: ticker / name / market / asset class
- Decision: buy, hold, add, reduce, avoid, hedge, or compare
- Horizon
- Existing position and portfolio concentration
- Capital at risk and max acceptable loss
- Current data source and timestamp

If these are missing, ask for them or output `信息不足`.

## Current Data Rule

If price, valuation, filings, policy, earnings, rates, flows, or news matter, verify current sources before the contest. If they cannot be checked, provide framework-only analysis.

## Contest Roles

- Pro: argue the strongest feasible thesis, upside path, catalyst, and risk/reward.
- Con: attack assumptions, valuation, liquidity, drawdown, macro, governance, event, and behavioral risk.
- Arbiter: choose a bounded decision label and define conditions.

## Output Format

```markdown
## 投资判断

信息不足 / 不建议参与 / 谨慎观察 / 低仓位试错 / 分批参与 / 持有但设退出条件 / 减仓控制风险

## 关键依据

## 反方最强质疑

## 主要风险

## 仓位与风控

- 仓位：
- 失效条件：
- 退出 / 复盘条件：

## 最终结论
```

## Safety Rules

- Do not promise returns.
- Do not claim certainty.
- Do not output standalone buy or sell commands.
- Do not output `买入` or `卖出` as a standalone conclusion.
- Always attach premise, sizing, invalidation, and review conditions to actionable views.

## Common Mistakes

- Running a debate without current data when current data matters.
- Ending with "both sides are reasonable" instead of a bounded label.
- Ignoring user concentration or liquidity needs.
