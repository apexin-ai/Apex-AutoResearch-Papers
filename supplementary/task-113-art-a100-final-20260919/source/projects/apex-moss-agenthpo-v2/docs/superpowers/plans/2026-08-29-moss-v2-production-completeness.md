# Moss V2 Production Harness Completeness Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring the refreshed `main` branch to a production-consistent Moss V2 path where formal and cross-test runs use the same fixed public tools, Agent Harness proposals are gated before commit, and audit identities remain replayable.

**Architecture:** The controller builds one benchmark-scoped `ExperimentOneToolPack` per lineage root and passes both its registry and workspace to formal and cross-test execution. Builder probing reuses runtime validation for Agent declarations. Solver prompts distinguish Agent action envelopes from final benchmark candidate contracts, while audit scopes use the same node identity as trace events.

**Tech Stack:** Python 3.11+, pytest, dataclasses, JSONL durable evidence, existing `DualHarnessRuntime`, `ExperimentOneToolPack`, EdgeBench/ALE-Bench adapters.

---

### Task 1: Audit current production wiring

**Files:**
- Inspect `optimization_lab/harness_builder/experiment_one_production.py`
- Inspect `optimization_lab/harness_builder/dual_runtime.py`
- Inspect `optimization_lab/harness_builder/dual_harness.py`

- [ ] Confirm current `main` and preserve dirty user files.
- [ ] Trace formal and cross-test call sites and record exact missing arguments.
- [ ] Run focused tests before changes to establish baseline.

### Task 2: Wire the public tool pack into formal and cross-test execution

**Files:**
- Modify `optimization_lab/harness_builder/experiment_one_production.py`
- Test: `tests/test_experiment_one_production.py`
- Test: `tests/test_experiment_one_cross.py` (or nearest existing cross-test module)

- [ ] Build one `ExperimentOneToolPack` under each lineage/cell tool workspace.
- [ ] Pass `registry`, `workspace`, and operation scope to every `DualHarnessRuntime.run_round`/cross executor call.
- [ ] Keep evaluator outside the registry and preserve operation ids.
- [ ] Add an Agent-mode production smoke test proving a tool action reaches the fixed registry.

### Task 3: Strengthen pre-commit Harness gates

**Files:**
- Modify `optimization_lab/harness_builder/experiment_one_production.py`
- Modify `optimization_lab/harness_builder/builder_harness.py` only if shared validation is required
- Test: `tests/test_experiment_one_production.py`
- Test: `tests/test_builder_harness.py`

- [ ] Validate Agent model node, declared tools, max turns/tool calls, workflow ids, and required registry/workspace before commit.
- [ ] Reject evaluator ids and unregistered tools at probe time.
- [ ] Add negative tests for each rejected condition and one accepted Agent proposal.

### Task 4: Correct Agent prompt and audit identity

**Files:**
- Modify `optimization_lab/harness_builder/dual_harness.py`
- Test: `tests/test_agent_runtime.py`
- Test: `tests/test_dual_runtime.py`

- [ ] State that the benchmark contract applies only to `emit.candidate`; intermediate Agent action JSON is separate.
- [ ] Generate Agent operation scope from the actual trace node id, so scope and event node agree.
- [ ] Assert durable audit evidence keeps prior calls when a later call fails.

### Task 5: Verify and publish

**Files:**
- No additional source files unless tests expose a defect.

- [ ] Run focused regression suites and full regression if focused suites pass.
- [ ] Run `git diff --check`.
- [ ] Fetch/rebase against latest `origin/main` without touching user dirty files.
- [ ] Commit only Moss V2 source/tests/docs changes and push `apexin-ai/apex-moss:main`.
- [ ] Confirm local `HEAD` equals `origin/main` and report test counts plus any remaining blocker.
