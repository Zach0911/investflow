# Research Design Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Build a research-design scenario that turns a vague investment question into a structured research task brief.

**Architecture:** Add a Markdown template exposed through `investflow new design`, document the scenario, and verify the template is discoverable. The feature remains local and does not fetch market data.

**Tech Stack:** Python standard library CLI, Markdown templates, shell/Python tests.

---

### Task 1: Add Research Design Template

**Files:**
- Create: `templates/research-design.md`
- Modify: `scripts/investflow`
- Test: `tests/test_cli.py`

- [x] **Step 1: Create the template with required headings**

The template must include `投资研究任务书`, `原始问题`, `待确认边界`, `必需数据`, `下一步路由`.

- [x] **Step 2: Register `design` in `TEMPLATE_MAP`**

Map `design` to `research-design.md`.

- [x] **Step 3: Test CLI generation**

Run: `./scripts/investflow new design`

Expected: stdout contains `## 投资研究任务书` and `## 下一步路由`.

### Task 2: Document and Validate

**Files:**
- Modify: `docs/scenarios.zh-CN.md`
- Modify: `tests/e2e_investflow.py`
- Modify: `tests/validate-investflow-project.sh`

- [x] **Step 1: Link the scenario from the scenario index**

The index must list `investflow new design`.

- [x] **Step 2: Add validation checks**

Project validation must require `templates/research-design.md` and the `投资研究任务书` heading.

- [x] **Step 3: Run verification**

Run: `./scripts/validate.sh`

Expected: all validation and CLI tests pass.
