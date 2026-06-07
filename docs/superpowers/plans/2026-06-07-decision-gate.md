# Decision Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Build a decision-gate scenario that prevents final conclusions before contrarian review and boundary checks.

**Architecture:** Add a decision-gate template and expose it through `investflow new decision-gate`.

**Tech Stack:** Python standard library CLI, Markdown templates, shell/Python tests.

---

### Task 1: Add Decision Gate Template

**Files:**
- Create: `templates/decision-gate.md`
- Modify: `scripts/investflow`
- Test: `tests/test_cli.py`

- [x] **Step 1: Create the template**

The template must include `结论前检查`, `反方最强质疑`, `禁止输出`, `允许输出`, `最终结论条件`.

- [x] **Step 2: Register `decision-gate` in `TEMPLATE_MAP`**

Map `decision-gate` to `decision-gate.md`.

- [x] **Step 3: Verify generation**

Run: `./scripts/investflow new decision-gate`

Expected: stdout contains `## 结论前检查`.

### Task 2: Strengthen Validation Coverage

**Files:**
- Modify: `tests/validate-investflow-project.sh`
- Modify: `tests/e2e_investflow.py`

- [x] **Step 1: Require decision-gate template in project validation**

Validation must fail if `templates/decision-gate.md` is missing.

- [x] **Step 2: Run verification**

Run: `./scripts/validate.sh`

Expected: all tests pass.
