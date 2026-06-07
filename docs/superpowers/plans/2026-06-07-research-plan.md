# Research Plan Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Build a research-plan scenario that converts a confirmed research task into a step-by-step investment research execution plan.

**Architecture:** Add a dedicated plan template exposed through `investflow new plan`, with explicit gates for data, thesis, valuation, risk, and conclusion.

**Tech Stack:** Python standard library CLI, Markdown templates, shell/Python tests.

---

### Task 1: Add Research Plan Template

**Files:**
- Create: `templates/research-plan.md`
- Modify: `scripts/investflow`
- Test: `tests/test_cli.py`

- [x] **Step 1: Create the template**

The template must include `投研执行计划`, `研究范围`, `执行步骤`, `验证关口`, `交付物`.

- [x] **Step 2: Register `plan` in `TEMPLATE_MAP`**

Map `plan` to `research-plan.md`.

- [x] **Step 3: Verify generation**

Run: `./scripts/investflow new plan`

Expected: stdout contains `## 投研执行计划` and `## 验证关口`.

### Task 2: Document and Validate

**Files:**
- Modify: `docs/scenarios.zh-CN.md`
- Modify: `tests/e2e_investflow.py`
- Modify: `tests/validate-investflow-project.sh`

- [x] **Step 1: Add scenario documentation**

The scenario index must explain that this is the investment equivalent of a coding implementation plan.

- [x] **Step 2: Add project checks**

Validation must require `templates/research-plan.md` and the `投研执行计划` heading.

- [x] **Step 3: Run verification**

Run: `./scripts/validate.sh`

Expected: all tests pass.
