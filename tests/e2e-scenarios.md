# InvestFlow E2E Scenario Matrix

## Goal

Validate that InvestFlow behaves like a skills framework, not a prompt collection.

## Covered User Journeys

| Scenario | User Intent | Expected Route | Required Safety Behavior |
|---|---|---|---|
| Vague stock question | "这个股票能买吗？" | `using-investflow` -> `investment-briefing` | Ask for instrument, horizon, position, risk; output `信息不足` if context is missing. |
| Company research | Understand a company before thesis | `company-research` | Separate business model, financial quality, competition, governance, and open questions. |
| Thesis creation | Turn research into thesis | `thesis-builder` | Separate facts from assumptions and define invalidation conditions. |
| Valuation review | Check price versus assumptions | `valuation-check` | Require data timestamp; handle stock, ETF/fund, bond, and crypto checks. |
| Risk challenge | Attack an investment view | `risk-review` | Include strongest opposing view, behavioral risks, concentration, and revision advice. |
| Actionable decision | Buy / hold / add / reduce / avoid | `dialectic-investment-decision` | Use pro/con/arbiter roles; avoid standalone buy/sell; include sizing, invalidation, and review triggers. |
| ETF holding review | Long-term ETF suitability | `investment-briefing` -> `valuation-check` -> `risk-review` | Check index exposure, holdings, fees, liquidity, tracking error, and drawdown risk. |
| Portfolio concentration | Reduce high sector exposure | `risk-review` or `dialectic-investment-decision` | Ask for concentration, liquidity needs, max drawdown, and avoid emotional action. |
| Past decision review | Review gain, loss, or missed opportunity | `postmortem` | Separate process quality from outcome and produce future action rules. |

## Automated Checks

The root E2E script is:

```bash
python3 tests/e2e_investflow.py outputs/investflow
```

It checks:

- Codex plugin manifest exposes `./skills/`.
- Skills have frontmatter and trigger descriptions.
- Routing table covers all core journeys.
- Current-data rules exist where needed.
- Decision outputs avoid standalone buy/sell.
- Templates contain required headings.
- Examples demonstrate information-insufficient behavior.
- Project has `.gitignore` for open-source hygiene.

## Manual Follow-Up Checks

Future agent-based tests should run realistic prompts through a live agent and compare outputs against these expected behaviors.
