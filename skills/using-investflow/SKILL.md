---
name: using-investflow
description: Use when an investment research, portfolio review, valuation, risk review, or AI investment-agent task should follow InvestFlow boundaries.
---

# Using InvestFlow

## Overview

InvestFlow routes investment tasks to the right skill and enforces research, data, and safety boundaries.

## When to Use

Use when the user asks about stocks, ETFs, funds, portfolios, valuation, thesis, risk, postmortem, or investment-agent workflow design.

Do not use for tax, legal, accounting, or trade execution tasks.

## Core Boundary

Before actionable analysis, confirm:

- Instrument: ticker / name / market / asset class
- Decision: buy, hold, add, reduce, avoid, hedge, compare, or review
- Horizon: short, medium, long term, or unknown
- Position: none, light, heavy, portfolio percentage
- Risk: max acceptable loss or drawdown
- Data basis: latest price, valuation, filings, news, macro or sector context, and source time

If these are missing, ask first or label the result `信息不足`.

## Skill Routing

| User task | Skill |
|---|---|
| Vague investment question | `investment-briefing` |
| Business or company analysis | `company-research` |
| Build an investment thesis | `thesis-builder` |
| Check valuation | `valuation-check` |
| Challenge a view | `risk-review` |
| Decide buy / hold / reduce / avoid | `dialectic-investment-decision` |
| Review past decision | `postmortem` |

## Output Labels

Use bounded labels:

- `信息不足`
- `不建议参与`
- `谨慎观察`
- `低仓位试错`
- `分批参与`
- `持有但设退出条件`
- `减仓控制风险`

Do not output standalone `买入` or `卖出`.

## Current Data Rule

If the decision depends on current price, valuation, filings, earnings, rates, policy, news, fund holdings, flows, or market regime, verify current data and state the source time.

If data cannot be verified, provide framework-only analysis and say exactly which data is missing.

## Common Mistakes

- Answering "can I buy?" before clarifying horizon and position.
- Treating a strong story as a thesis without invalidation conditions.
- Using old valuation data without marking the timestamp.
- Omitting the strongest opposing argument.
