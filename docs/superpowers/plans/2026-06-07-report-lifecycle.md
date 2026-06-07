# Report Lifecycle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Build a report-lifecycle scenario that tracks whether an investment report is draft, validated, reviewed, archived, or waiting for postmortem.

**Architecture:** Add a lifecycle template and keep lifecycle status as Markdown metadata/checklist instead of introducing a database.

**Tech Stack:** Python standard library CLI, Markdown templates.

---

### Task 1: Add Lifecycle Template

**Files:**
- Create: `templates/report-lifecycle.md`
- Modify: `scripts/investflow`
- Test: `tests/test_cli.py`

- [x] **Step 1: Create the template**

The template must include `报告生命周期`, `当前状态`, `状态流转`, `复盘触发`, `归档信息`.

- [x] **Step 2: Register `lifecycle` in `TEMPLATE_MAP`**

Map `lifecycle` to `report-lifecycle.md`.

- [x] **Step 3: Verify generation**

Run: `./scripts/investflow new lifecycle`

Expected: stdout contains `## 报告生命周期`.

### Task 2: Document and Validate

**Files:**
- Modify: `docs/scenarios.zh-CN.md`
- Modify: `tests/validate-investflow-project.sh`

- [x] **Step 1: Add lifecycle scenario to docs**

Docs must list the statuses `草稿`, `已校验`, `已审查`, `已归档`, `待复盘`.

- [x] **Step 2: Run verification**

Run: `./scripts/validate.sh`

Expected: all tests pass.
