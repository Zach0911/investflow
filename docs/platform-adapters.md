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

## Current Support

| Platform | Status | Entry |
|---|---|---|
| Codex | Supported now | `./scripts/investflow install codex` |
| MCP Client | Local experimental support | `.mcp.json` and `scripts/investflow-mcp` |
| Generic Agent | Manual adaptation | Read `skills/*/SKILL.md` and call the CLI |
| Claude-style agents | Not packaged yet | Manual skill copy only |
| Gemini-style agents | Not packaged yet | Manual instruction adaptation only |
| Cursor / OpenCode-style tools | Not packaged yet | Use CLI and Markdown docs manually |

## Adapter Checklist

Generate a checklist:

```bash
./scripts/investflow new platform-adapter --output work/platform-adapter.md
```

An adapter must confirm:

- How skills are discovered.
- Whether local CLI execution is available.
- Whether MCP stdio is supported.
- Where generated Markdown / HTML reports can be written.
- How the platform preserves InvestFlow boundaries.

## Non-Goals

- Do not claim a native platform integration before it is tested.
- Do not duplicate `SKILL.md` instructions across platform folders.
- Do not add trading, brokerage write access, or account operations.
