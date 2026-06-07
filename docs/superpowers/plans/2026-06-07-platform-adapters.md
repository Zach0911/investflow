# Platform Adapters Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Build a platform-adapter scenario that explains how InvestFlow can be installed or adapted across Codex, Claude-style agents, Gemini-style agents, and generic MCP clients.

**Architecture:** Add a platform adapter checklist template and expand platform documentation without claiming unsupported native integrations.

**Tech Stack:** Markdown docs, Python standard library CLI.

---

### Task 1: Add Platform Adapter Template

**Files:**
- Create: `templates/platform-adapter-checklist.md`
- Modify: `scripts/investflow`
- Test: `tests/test_cli.py`

- [x] **Step 1: Create the template**

The template must include `平台适配清单`, `Codex`, `MCP Client`, `Generic Agent`, `待确认能力`, `不支持能力`.

- [x] **Step 2: Register `platform-adapter` in `TEMPLATE_MAP`**

Map `platform-adapter` to `platform-adapter-checklist.md`.

- [x] **Step 3: Verify generation**

Run: `./scripts/investflow new platform-adapter`

Expected: stdout contains `## 平台适配清单`.

### Task 2: Document and Validate

**Files:**
- Modify: `docs/platform-adapters.md`
- Modify: `docs/scenarios.zh-CN.md`
- Modify: `tests/validate-investflow-project.sh`

- [x] **Step 1: Document supported and aspirational adapters**

Docs must state Codex is supported now, MCP clients are local/experimental, and other platforms require manual adaptation.

- [x] **Step 2: Run verification**

Run: `./scripts/validate.sh`

Expected: all tests pass.
