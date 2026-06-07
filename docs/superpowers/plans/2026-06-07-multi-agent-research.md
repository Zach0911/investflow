# Multi-Agent Research Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Build a multi-agent research scenario that assigns data, company, valuation, risk, and arbiter roles without allowing any role to execute trades.

**Architecture:** Add a multi-agent workflow template exposed by `investflow new multi-agent`.

**Tech Stack:** Python standard library CLI, Markdown templates, shell/Python tests.

---

### Task 1: Add Multi-Agent Template

**Files:**
- Create: `templates/multi-agent-research.md`
- Modify: `scripts/investflow`
- Test: `tests/test_cli.py`

- [x] **Step 1: Create the template**

The template must include `多 Agent 投研分工`, `Data Agent`, `Company Agent`, `Valuation Agent`, `Risk Agent`, `Arbiter Agent`, `交接规则`.

- [x] **Step 2: Register `multi-agent` in `TEMPLATE_MAP`**

Map `multi-agent` to `multi-agent-research.md`.

- [x] **Step 3: Verify generation**

Run: `./scripts/investflow new multi-agent`

Expected: stdout contains `## 多 Agent 投研分工`.

### Task 2: Document and Validate

**Files:**
- Modify: `docs/scenarios.zh-CN.md`
- Modify: `tests/e2e_investflow.py`
- Modify: `tests/validate-investflow-project.sh`

- [x] **Step 1: Add scenario index entry**

The index must describe multi-agent handoff and final arbiter boundaries.

- [x] **Step 2: Run verification**

Run: `./scripts/validate.sh`

Expected: all tests pass.
