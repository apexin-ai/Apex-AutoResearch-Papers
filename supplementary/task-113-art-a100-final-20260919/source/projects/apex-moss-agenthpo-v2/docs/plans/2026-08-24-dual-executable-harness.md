# Dual Executable Harness Implementation Plan

> Status: implemented on `main`; retained as the historical implementation checklist.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Add a versioned executable Task Harness and a multi-step Builder Harness while preserving the existing configuration runtime as a regression baseline.

**Architecture:** The Task Harness is a typed JSON artifact whose nodes execute model calls and allowlisted tools, producing a candidate plus an append-only trace. The Builder Harness is a fixed Python control loop that reads the current artifact and trace, asks a model for a typed replacement proposal, validates it, runs an optional probe, and commits or rolls back the next artifact. Artifacts, traces, and completed-round receipts are content-addressed and safe to replay.

**Tech Stack:** Python 3.11+, dataclasses, JSON, pathlib, pytest, existing `CandidateGenerator`/`GenerationResult` interfaces.

---

### Task 1: Add typed executable Task Harness artifacts

**Files:**
- Create: `optimization_lab/harness_builder/dual_harness.py`
- Test: `tests/test_dual_harness.py`

- [x] **Step 1: Write failing tests** for strict artifact parsing, stable hashing, allowlisted model/tool nodes, and rejection of unknown node types or unsafe tool names.
- [x] **Step 2: Run the focused tests** and verify they fail because the new module does not exist.
- [x] **Step 3: Implement** `TaskHarnessSpec`, `TaskHarnessNode`, `TaskHarnessArtifact`, `HarnessTraceEvent`, `TaskHarnessRun`, and `TaskHarnessRuntime`.
- [x] **Step 4: Run the focused tests** and verify all pass.

### Task 2: Add persistent Builder workspace and version lineage

**Files:**
- Modify: `optimization_lab/harness_builder/dual_harness.py`
- Test: `tests/test_dual_harness.py`

- [x] **Step 1: Add failing tests** for storing immutable artifact versions, loading the current version, recording traces, diffing versions, and rollback without overwriting content.
- [x] **Step 2: Run the focused tests** and verify the new tests fail.
- [x] **Step 3: Implement** `HarnessWorkspace` with safe paths, immutable content-addressed JSON records, parent hashes, integrity-checked run bindings, and current-version binding.
- [x] **Step 4: Run the focused tests** and verify all pass.

### Task 3: Add the multi-step Builder Harness loop

**Files:**
- Create: `optimization_lab/harness_builder/builder_harness.py`
- Test: `tests/test_builder_harness.py`

- [x] **Step 1: Write failing tests** for inspect → propose → validate → probe → commit, invalid proposal rollback, probe failure rollback, and trace visibility.
- [x] **Step 2: Run the focused tests** and verify they fail for the missing Builder Harness.
- [x] **Step 3: Implement** `HarnessChangeProposal`, strict JSON parsing, `BuilderHarness.inspect`, `BuilderHarness.propose`, and `BuilderHarness.evolve_once`.
- [x] **Step 4: Run the focused tests** and verify all pass.

### Task 4: Connect both layers in a resumable round pipeline

**Files:**
- Create: `optimization_lab/harness_builder/dual_runtime.py`
- Modify: `optimization_lab/harness_builder/__init__.py`
- Test: `tests/test_dual_runtime.py`

- [x] **Step 1: Write failing tests** for one round of lower execution followed by Builder evolution, including score/feedback entering the next Builder prompt and no evaluator-private data entering the trace.
- [x] **Step 2: Run the focused tests** and verify they fail.
- [x] **Step 3: Implement** `DualHarnessRuntime` with explicit model names for Builder and Solver, a typed public/private evaluator boundary, append-only round receipts, and replay-safe current artifact loading.
- [x] **Step 4: Run focused tests and the existing harness-builder runtime tests** and verify all pass.

### Task 5: Add model transport configuration and offline fixture

**Files:**
- Create: `optimization_lab/harness_builder/dual_config.py`
- Create: `scripts/run_dual_harness_fixture.py`
- Test: `tests/test_dual_config.py`
- Modify: `README.md`

- [x] **Step 1: Write failing tests** for default same-model configuration, explicit separate Builder/Solver models, and rejection of blank model names.
- [x] **Step 2: Run the focused tests** and verify they fail.
- [x] **Step 3: Implement** configuration without embedding API keys; keep the existing Codex CLI transport as an optional adapter and use fake generators in the fixture.
- [x] **Step 4: Run the fixture and tests**, then document required credentials, API calls, and server resources.

### Task 6: Verify, commit, and push a reviewable branch

**Files:**
- Modify: only files created or changed above.

- [x] **Step 1: Run the full test suite** with `pytest -q`.
- [x] **Step 2: Inspect `git diff` and ensure no credentials, benchmark answers, or generated artifacts are tracked.**
- [x] **Step 3: Commit** with message `feat: add dual executable harness runtime`.
- [x] **Step 4: Push** branch `codex/dual-executable-harness` to `origin` and report the remote branch URL.
