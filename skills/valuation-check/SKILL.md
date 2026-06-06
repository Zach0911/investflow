---
name: valuation-check
description: Use when checking whether an asset's price, valuation, yield, premium, discount, or scenario assumptions are reasonable.
---

# Valuation Check

## Overview

Check whether the price paid is reasonable relative to assumptions. Valuation is a range, not a certainty.

## Required Inputs

- Instrument and market
- Current price or valuation source time
- Relevant metrics for the asset class
- Peer group or historical range if used
- Horizon and thesis assumptions

## Asset-Specific Checks

| Asset | Checks |
|---|---|
| Stock | PE, PB, PS, EV/EBITDA, margins, growth, cash flow, dilution |
| ETF / Fund | Holdings, index exposure, fees, tracking error, premium / discount |
| Bond | Yield, duration, credit quality, issuer risk |
| Crypto | Liquidity, protocol risk, drawdown, custody and regulatory risk |

## Workflow

1. State data timestamp.
2. Pick valuation methods appropriate to the asset.
3. Compare against history, peers, or scenario assumptions.
4. Build optimistic, base, and adverse scenarios.
5. Identify sensitivity to growth, margins, rates, and multiples.
6. State whether valuation risk is low, moderate, high, or unknown.

## Output Format

```markdown
## 估值检查

## 数据时间

## 使用方法

## 情景分析

## 敏感因素

## 估值风险

## 不能判断的原因
```

## Common Mistakes

- Using stale multiples.
- Treating target price as certainty.
- Comparing companies with different growth, margin, or risk profiles.
