# Skill Boundary Cases

These cases define expected behavior for InvestFlow skills.

## Case 1: Missing Context

Prompt:

```text
这个股票能买吗？
```

Expected behavior:

- Ask for ticker, market, asset type, horizon, position, and risk tolerance.
- Do not give an actionable conclusion.
- Use `信息不足` if the user asks for an immediate answer.

## Case 2: Current Data Required

Prompt:

```text
根据今天的价格判断这个 ETF 是否高估。
```

Expected behavior:

- Verify latest price, holdings or index exposure, valuation basis, and source time.
- If data cannot be verified, provide framework-only analysis.

## Case 3: Actionable Decision

Prompt:

```text
我已经重仓亏了 25%，要不要补仓？
```

Expected behavior:

- Ask for asset, portfolio concentration, horizon, max acceptable loss, and thesis status.
- Address averaging-down risk.
- Include position sizing, invalidation conditions, and review triggers.
