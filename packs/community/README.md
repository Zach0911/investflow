# Community Skill Packs

Community skill packs extend InvestFlow for specific research styles while preserving project boundaries.

Rules:

- Do not include trading execution.
- Do not promise returns.
- Do not bypass risk review.
- Include `not_investment_advice` in every pack boundary manifest.

## Contribution Flow

1. Draft a pack proposal:

```bash
./scripts/investflow new pack-proposal --output work/pack-proposal.md
```

2. Create a pack folder under `packs/community/<pack-name>`.
3. Add `pack.json` with name, display name, description, version, author, license, skills, and boundaries.
4. Include `not_investment_advice` in boundaries.
5. Do not include `trade_execution`, `brokerage_write`, or `place_order`.
6. Validate the pack:

```bash
./scripts/investflow pack validate packs/community/<pack-name>
```

Community packs are research workflow extensions. They are not investment products, signal services, or trade execution modules.
