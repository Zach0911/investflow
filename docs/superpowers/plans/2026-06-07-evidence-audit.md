# Evidence Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Build an evidence-first audit command that checks whether a report includes data sources, timestamps, contrarian review, invalidation conditions, and review triggers.

**Architecture:** Add `investflow audit <file>` next to `validate`. `validate` checks report structure; `audit` checks evidence and decision hygiene.

**Tech Stack:** Python standard library CLI, Markdown text scanning, unittest.

---

### Task 1: Implement Audit Rules

**Files:**
- Modify: `scripts/investflow`
- Test: `tests/test_cli.py`

- [x] **Step 1: Add `audit_report_text(text)`**

Rules:
- require one of `数据来源`, `来源`, `source`
- require one of `时间戳`, `截至`, `as of`, `as_of`
- require `反方最强质疑`
- require one of `失效条件`, `invalidation`
- require one of `复盘条件`, `复盘触发`, `review trigger`
- require one of `仓位`, `position`

- [x] **Step 2: Add `investflow audit <file>`**

JSON output must include `ok`, `file`, `missing`, and `warnings`.

- [x] **Step 3: Add tests**

One test must pass for `examples/full-thesis-report-example.zh-CN.md`; one test must fail for a report missing source and timestamp.

### Task 2: Document and Validate

**Files:**
- Modify: `docs/cli.zh-CN.md`
- Modify: `docs/cli.md`
- Modify: `docs/scenarios.zh-CN.md`

- [x] **Step 1: Add CLI examples**

Document `./scripts/investflow audit work/thesis.md`.

- [x] **Step 2: Run verification**

Run: `./scripts/validate.sh`

Expected: all tests pass.
