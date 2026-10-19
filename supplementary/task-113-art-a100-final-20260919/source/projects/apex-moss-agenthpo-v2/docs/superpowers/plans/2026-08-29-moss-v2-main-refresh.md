# Moss V2 Main Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended; or superpowers:executing-plans) to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring the latest `origin/main` to a complete, auditable Moss V2 Experiment 1 implementation without changing historical V1 artifacts or frozen experimental semantics.

**Architecture:** Keep Builder Harness and Task Harness as separate content-addressed artifacts. The Builder sees only the current instance's public Harness history by default; cross-task memory remains opt-in for B-online. Solver tools are mediated by the public ToolRegistry, while evaluator execution stays outside the Agent loop. V2 manifests are additive and explicitly selected by the CLI.

**Tech Stack:** Python 3, dataclasses, JSON manifests, pytest, git worktrees.

---

### Task 1: Freeze the V2 manifest contract

**Files:**
- Create: `optimization_lab/harness_builder/manifests/experiment_one_edgebench_v2.json`
- Create: `optimization_lab/harness_builder/manifests/experiment_one_alebench_v2.json`
- Modify: `scripts/run_moss_experiment_one.py`
- Test: `tests/test_experiment_one_cli.py`

- [ ] Add additive V2 manifest entries copied from the current frozen V1 payload, changing only explicitly declared Task Harness schema/entry metadata.
- [ ] Extend CLI manifest selection with an explicit `--harness-version v1|v2` switch; default remains V1 for replay compatibility, while `--harness-version v2` selects the new files.
- [ ] Validate that V2 manifests cannot silently load as V1 and that their manifest hash is included in every report.
- [ ] Add tests for default V1 selection, explicit V2 selection, and rejection of a schema-mismatched manifest.

### Task 2: Route static public tools through the registry

**Files:**
- Modify: `optimization_lab/harness_builder/dual_harness.py`
- Modify: `optimization_lab/harness_builder/experiment_one_production.py`
- Test: `tests/test_dual_harness.py`
- Test: `tests/test_experiment_one_production.py`

- [ ] Add a registry-backed adapter for legacy static `tool_call` nodes that binds the node's tool name to the same allow/deny policy used by Agent actions.
- [ ] Preserve V1 behavior for non-production callers, but make production V2 reject direct unregistered tool mappings and emit a durable tool receipt for every static call.
- [ ] Add tests proving an allowed public tool succeeds, a forbidden evaluator tool fails closed, and a missing registry entry never executes.

### Task 3: Make cross-test Solver failures fail closed

**Files:**
- Modify: `optimization_lab/harness_builder/experiment_one.py`
- Modify: `optimization_lab/harness_builder/dual_runtime.py`
- Test: `tests/test_experiment_one.py`
- Test: `tests/test_dual_runtime.py`

- [ ] On Solver API, format, or Harness execution failure, write only the immutable error audit with the original exception class/message and operation scope.
- [ ] Do not create score or `cross_solver.json` artifacts for failed cells; expose `status=error` or `status=invalid` to `CrossMatrixRunner` instead of converting the failure to zero.
- [ ] Add replay/idempotency tests for successful and failed cells and verify no automatic retry is introduced.

### Task 4: Synchronize project documentation

**Files:**
- Modify: `README.md`
- Modify: `TEST.md`
- Modify: `CLAUDE.md`
- Modify: `PROGRESS.md`

- [ ] Document the explicit V2 CLI switch, public-tool receipts, and the no-score-on-error rule.
- [ ] Keep historical V1 commands and frozen results unchanged and clearly labeled as replay-compatible.
- [ ] Record the final commit id and any environment limitation encountered while running tests.

### Task 5: Verify and publish

**Files:**
- No source changes unless verification finds a defect.

- [ ] Run the focused V2 regression suite and `git diff --check`.
- [ ] Run any available broader suite; report missing local dependencies separately from code failures.
- [ ] Rebase the feature branch onto the latest `origin/main`, merge fast-forward into local `main`, and push `apexin-ai/apex-moss:main`.
- [ ] Verify local `HEAD` equals `origin/main` and preserve unrelated user files/stash entries.

