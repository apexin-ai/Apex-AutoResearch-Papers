# Relax Production Harness Probe Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Permit multi-model-call Task Harness evolution while retaining general structural and public-tool safety gates.

**Architecture:** Keep `TaskHarnessSpec` as the structural validator. Narrow `production_harness_probe` to topology-neutral production requirements: at least one model call and only allowlisted tools.

**Tech Stack:** Python 3.12, dataclasses, pytest.

---

### Task 1: Add the multi-call regression test

**Files:**
- Modify: `tests/test_experiment_one_production.py`

- [ ] Rename the probe test so it describes general model/tool requirements rather than a single-model topology.
- [ ] Change the existing two-model Harness expectation from rejected to accepted.
- [ ] Add an emit-only Harness assertion proving that a Harness with no solver model call remains rejected.
- [ ] Run `py -m pytest tests/test_experiment_one_production.py::test_frozen_h0_conversion_and_production_probe_enforce_model_and_tool_requirements -q` and confirm it fails because the two-model Harness is still rejected by production code.

### Task 2: Remove the topology-specific production restriction

**Files:**
- Modify: `optimization_lab/harness_builder/experiment_one_production.py`

- [ ] Replace `model_call count == 1` with `any model_call exists`.
- [ ] Keep the public tool allowlist check.
- [ ] Rely on `TaskHarnessSpec` for the single-final-emit and structural invariants.
- [ ] Run the focused probe test and confirm it passes.

### Task 3: Verify and document the behavior

**Files:**
- Modify: `CLAUDE.md`
- Modify: `TEST.md`
- Modify: `PROGRESS.md`

- [ ] Record that experiment-one Builder proposals may contain multiple model calls and are no longer rejected solely for their topology.
- [ ] Document the focused regression command and preserved rejection cases.
- [ ] Run `py -m pytest tests/test_experiment_one_production.py -q`.
- [ ] Run `py -m pytest -q`.
- [ ] Commit the verified change and push it to `origin/main` after rebasing on the latest main.
