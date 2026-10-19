# Moss Experiment 1B Cross-Benchmark Stress Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a preregistered, auditable six-direction frozen-Harness transfer test between EdgeBench and ALE-Bench without changing Experiment 1A or enabling Builder adaptation.

**Architecture:** Reuse Experiment 1A freeze receipts, `H0BaselineReceipt` records, candidate codecs, evaluator adapters, and audited Solver calls. Add a separate manifest and runner that rebind a frozen source Harness to a fresh target workspace, execute exactly one Solver call and one official evaluation, and report validity and target-local comparisons against native Harness and `H0`.

**Tech Stack:** Python 3.12, pytest, OpenAI Responses API, EdgeBench/SForge, ALE-Bench, JSON receipts, SHA-256 content addressing.

---

### Task CB1: Cross-Benchmark Manifest and Frozen Transfer Runner

**Files:**
- Create: `optimization_lab/harness_builder/experiment_one_cross_benchmark.py`
- Test: `tests/test_experiment_one_cross_benchmark.py`

- [ ] **Step 1: Write failing manifest tests** that require the static production manifest to contain exactly the six ordered pair templates and allowed seeds `S1`/`S2`/`S3`, reject duplicate or mismatched-position templates, and reject any prebound freeze receipt SHA, full Harness SHA, or H0 receipt locator. Add runtime binding tests proving the controller can materialize exactly six concrete entries for one eligible seed, each with the six-field source locator (`benchmark`, `position`, `instance`, `seed`, `freeze_receipt_sha`, `full_harness_sha`), target binding, and `H0BaselineReceipt` locator.
- [ ] **Step 2: Run** `py -3.12 -m pytest -q tests/test_experiment_one_cross_benchmark.py` and verify failure because the module does not exist.
- [ ] **Step 3: Implement immutable types** for the six-template static manifest and each seed-specific six-entry runtime binding receipt/manifest. Runtime entries bind pair identity, the six-field source locator, target binding reference, shared seed ID, `H0BaselineReceipt` reference, and contract digest. Canonical serialization must use sorted-key compact JSON and SHA-256.
- [ ] **Step 4: Write failing execution tests** proving each pair creates a fresh target root, passes no target history or source candidate text, performs one audited Solver call and one evaluator call, never constructs a Builder, and records explicit `valid_scored`, `candidate_invalid`, `harness_incompatible`, `evaluator_failed`, or `audit_failed` status. Add H0 tests proving no Builder construction or call, `upper_model_configuration_hash` is the configured-but-uncalled formal Builder Harness model, `lower_model_configuration_hash` is the formal Task Harness/Solver model, and both resolve to `gpt-5.6-sol`/`high`. Their canonical payload covers only provider, API family/transport, model, reasoning effort, max output tokens, sampling parameters, and tool permission policy, and excludes prompt, Harness content, operation ID, and task binding. Require equal hashes and Builder/Solver/evaluator calls of `0`/`1`/`1`, not two Solver calls.
- [ ] **Step 5: Implement the runner** using injected candidate codec and evaluator interfaces. Reject any target root that already contains a lineage, candidate, Memory, score, or model-call ledger. Reject any unavailable frozen Harness component before the Solver call.
- [ ] **Step 6: Add recovery tests and implementation** so a completed receipt replays without new calls, a started operation without a terminal receipt becomes abandoned and consumes the pair budget, and no operation ID is reissued automatically.
- [ ] **Step 7: Run** `py -3.12 -m pytest -q tests/test_experiment_one_cross_benchmark.py tests/test_experiment_one.py tests/test_experiment_one_audit.py` and require all tests to pass.
- [ ] **Step 8: Commit** `optimization_lab/harness_builder/experiment_one_cross_benchmark.py` and `tests/test_experiment_one_cross_benchmark.py` with message `feat: add preregistered cross-benchmark Harness stress test`.

### Task CB2: Production Manifest and CLI Commands

**Files:**
- Create: `optimization_lab/harness_builder/manifests/experiment_one_cross_benchmark.json`
- Modify: `scripts/run_moss_experiment_one.py`
- Modify: `tests/test_experiment_one_cli.py`

- [ ] **Step 1: Write failing CLI tests** for read-only `cross-benchmark-status` and mutating `cross-benchmark-run --execute`. For a shared seed ID, the command must reject execution until both benchmarks have completed all three Experiment 1A eight-round lineages, valid numeric-score freezes, and formal 3x3 matrices for that same seed.
- [ ] **Step 2: Add the production JSON with exactly six immutable pair templates**: EdgeBench A/B/C=`apple_incremental_game`/`molecular_self_assembly`/`treant_forest`, ALE-Bench A/B/C=`ahc024`/`ahc026`/`ahc011`, and allowed seeds `S1`/`S2`/`S3`. It must not contain concrete freeze receipt SHAs, full Harness SHAs, or H0 receipt locators and must not expand to eighteen static entries.
- [ ] **Step 3: Implement CLI loading, validation, and runtime materialization** that rejects missing, reordered, duplicated, same-benchmark, mismatched-position, or unpinned templates. Only after one seed passes the full Experiment 1A gate, materialize a separate six-entry runtime binding receipt/manifest containing each concrete six-field source locator, target binding, and H0 receipt locator. Default invocation must not create directories or call models/evaluators.
- [ ] **Step 4: Implement execution dispatch** so each pair receives a distinct root and operation-ID namespace. Allow pair-level concurrency only after CPU/API gates pass and never share candidate, Memory, history, audit ledger, or target workspace.
- [ ] **Step 5: Run** `py -3.12 -m pytest -q tests/test_experiment_one_cli.py tests/test_experiment_one_cross_benchmark.py` and require all tests to pass.
- [ ] **Step 6: Commit** the manifest, CLI, and tests with message `feat: expose experiment-one cross-benchmark stress CLI`.

### Task CB3: Canary, Formal Run, and Report

**Files:**
- Modify: `docs/reports/2026-08-26-moss-experiment-one-results.md`
- Modify: `PROGRESS.md`

- [ ] **Step 1: Run no-model negative canaries** for one pair in each direction. Confirm unavailable Harness components and target-invalid candidates produce explicit non-numeric categories rather than a fabricated floor score.
- [ ] **Step 2: Run one real-model canary per direction** outside formal roots with `gpt-5.6-sol`, reasoning effort `high`, exactly one Solver call, no Builder ledger, and one official evaluator call.
- [ ] **Step 3: After both benchmarks complete all three Experiment 1A eight-round lineages, valid freezes, and formal 3x3 matrices for `S1`, materialize its six-entry runtime binding and execute all six preregistered formal pairs in new roots; verify one valid `H0BaselineReceipt` per target/seed.** Do not drop or replace invalid or unexpectedly strong transfers.
- [ ] **Step 4: If Experiment 1A proceeds to the remaining replicas, apply the same gate independently to `S2` and `S3`, materialize one separate six-entry runtime binding for each eligible seed, then execute their six pairs** using matching six-field source locators, target references, and H0 baseline receipts.
- [ ] **Step 5: Generate target-local tables** with native, transferred, and `H0` scores; validity category; native-minus-transfer; transfer-minus-H0; and per-seed direction. Never average raw EdgeBench and ALE-Bench scores together.
- [ ] **Step 6: Audit every reported row** against the six-field source locator, valid numeric-score freeze, target binding, `H0BaselineReceipt`, model-call, codec, evaluator, candidate, fresh-root, and no-Builder receipts. Exclude canary/setup roots from formal tables.
- [ ] **Step 7: Update the report and progress file** with separate Experiment 1A and 1B conclusions. Use only “cross-benchmark compatibility/mismatch” language for Experiment 1B.
- [ ] **Step 8: Commit** the audited report updates with message `docs: report cross-benchmark Harness stress results`.
