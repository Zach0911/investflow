# Community Pack Contribution Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Build a community contribution scenario that helps users propose a new investment skill pack without bypassing InvestFlow safety boundaries.

**Architecture:** Add a pack proposal template and document the existing `pack list` / `pack validate` flow.

**Tech Stack:** Python standard library CLI, Markdown templates, JSON pack manifests.

---

### Task 1: Add Pack Proposal Template

**Files:**
- Create: `templates/community-pack-proposal.md`
- Modify: `scripts/investflow`
- Test: `tests/test_cli.py`

- [x] **Step 1: Create the template**

The template must include `社区 Skill Pack 提案`, `适用场景`, `包含 Skills`, `边界声明`, `验收标准`.

- [x] **Step 2: Register `pack-proposal` in `TEMPLATE_MAP`**

Map `pack-proposal` to `community-pack-proposal.md`.

- [x] **Step 3: Verify generation**

Run: `./scripts/investflow new pack-proposal`

Expected: stdout contains `## 社区 Skill Pack 提案`.

### Task 2: Document and Validate

**Files:**
- Modify: `packs/community/README.md`
- Modify: `docs/scenarios.zh-CN.md`
- Modify: `tests/e2e_investflow.py`

- [x] **Step 1: Document contribution flow**

Docs must mention `investflow pack validate <path>`.

- [x] **Step 2: Run verification**

Run: `./scripts/validate.sh`

Expected: all tests pass.
