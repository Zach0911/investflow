# Platform Adapters

InvestFlow starts with Codex-compatible skill folders:

```text
skills/<skill-name>/SKILL.md
```

The initial plugin manifest is:

```text
.codex-plugin/plugin.json
```

Future adapters can add platform-specific metadata without changing the core skill content:

- `.claude-plugin/`
- `.cursor-plugin/`
- `.opencode/`
- `GEMINI.md`
- MCP server manifests

Adapter rule: platform files should reference the same `skills/` source of truth instead of duplicating skill instructions.
