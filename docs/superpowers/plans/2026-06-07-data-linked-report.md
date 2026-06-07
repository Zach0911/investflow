# Data-Linked Report Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Build a data-linked report scenario that helps agents connect read-only data source metadata to the report's data basis section.

**Architecture:** Add a data-brief template and keep data access read-only through existing `investflow data` commands.

**Tech Stack:** Python standard library CLI, JSON fixtures, Markdown templates.

---

### Task 1: Add Data Brief Template

**Files:**
- Create: `templates/data-linked-brief.md`
- Modify: `scripts/investflow`
- Test: `tests/test_cli.py`

- [x] **Step 1: Create the template**

The template must include `数据到报告联动`, `数据源清单`, `读取结果摘要`, `写入报告位置`, `缺失数据`.

- [x] **Step 2: Register `data-brief` in `TEMPLATE_MAP`**

Map `data-brief` to `data-linked-brief.md`.

- [x] **Step 3: Verify generation and data command**

Run: `./scripts/investflow new data-brief`

Expected: stdout contains `## 数据到报告联动`.

Run: `./scripts/investflow data list`

Expected: output contains `sample-market-snapshot`.

### Task 2: Document and Validate

**Files:**
- Modify: `docs/scenarios.zh-CN.md`
- Modify: `docs/cli.zh-CN.md`
- Modify: `tests/e2e_investflow.py`

- [x] **Step 1: Document how to combine `data read` and report templates**

The docs must show `investflow data read sample-company-profile`.

- [x] **Step 2: Run verification**

Run: `./scripts/validate.sh`

Expected: all tests pass.
