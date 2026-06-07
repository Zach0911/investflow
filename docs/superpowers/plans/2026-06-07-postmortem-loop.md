# Postmortem Loop Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Build a postmortem-loop scenario that connects original thesis, actual outcome, error attribution, and next action rules.

**Architecture:** Add a postmortem-loop template exposed through `investflow new postmortem-loop`, complementing the existing postmortem skill.

**Tech Stack:** Python standard library CLI, Markdown templates, shell/Python tests.

---

### Task 1: Add Postmortem Loop Template

**Files:**
- Create: `templates/postmortem-loop.md`
- Modify: `scripts/investflow`
- Test: `tests/test_cli.py`

- [x] **Step 1: Create the template**

The template must include `投资复盘闭环`, `原始 Thesis`, `实际结果`, `错误归因`, `下次行动规则`.

- [x] **Step 2: Register `postmortem-loop` in `TEMPLATE_MAP`**

Map `postmortem-loop` to `postmortem-loop.md`.

- [x] **Step 3: Verify generation**

Run: `./scripts/investflow new postmortem-loop`

Expected: stdout contains `## 投资复盘闭环`.

### Task 2: Document and Validate

**Files:**
- Modify: `docs/scenarios.zh-CN.md`
- Modify: `tests/e2e_investflow.py`
- Modify: `tests/validate-investflow-project.sh`

- [x] **Step 1: Add postmortem-loop scenario to docs**

Docs must explain that the loop compares the original thesis against actual results.

- [x] **Step 2: Run verification**

Run: `./scripts/validate.sh`

Expected: all tests pass.
