# Moss Experiment One: EdgeBench and ALE-Bench Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and run a real, auditable two-layer Moss experiment that evolves instance-specific Task Harnesses on EdgeBench and ALE-Bench and performs frozen no-evolution cross-tests.

**Architecture:** Reuse `TaskHarnessRuntime`, `BuilderHarness`, and `HarnessWorkspace`; add a benchmark-neutral experiment-one controller, strict candidate codecs, and two official evaluator adapters. Keep target contracts and hidden evaluator data outside the evolving Harness, expose only allowlisted public feedback, and use an explicit frozen-Harness path that never constructs a Builder.

**Tech Stack:** Python 3.12, pytest, OpenAI Responses API, Docker, SForge 1.0.0, ALE-Bench 1.6.1, AWS c6i.32xlarge.

---

### Task 1: Public Builder View and Audited Model Calls

**Files:**
- Modify: `optimization_lab/harness_builder/builder_harness.py`
- Create: `optimization_lab/harness_builder/experiment_one_audit.py`
- Test: `tests/test_experiment_one_audit.py`

- [ ] **Step 1: Write failing tests** proving an experiment Builder receives score, feedback, Harness hashes, and node kinds but not raw candidate text or raw model event payloads; prove every Builder/Solver response writes model, provider, effort, token usage, prompt hash, response hash, operation ID, and timestamp to append-only JSONL.
- [ ] **Step 2: Run** `python -m pytest -q tests/test_experiment_one_audit.py` and verify failure because the projector and audit wrapper do not exist.
- [ ] **Step 3: Implement** an optional `inspection_transform` on `BuilderHarness` and an `AuditedGenerator` wrapper. The default remains identity for existing callers; experiment one must pass the redacting transform explicitly.
- [ ] **Step 4: Run** the focused tests and existing dual-Harness tests; require all green.
- [ ] **Step 5: Commit** with `git commit -m "feat: add auditable public Builder view"`.

### Task 2: Candidate Codecs and Immutable Archives

**Files:**
- Create: `optimization_lab/harness_builder/official_solutions.py`
- Test: `tests/test_official_solutions.py`

- [ ] **Step 1: Write failing tests** for an EdgeBench JSON file bundle and an ALE-Bench single fenced source file. Reject absolute paths, `..`, duplicate paths, symlinks, oversized output, missing required submit paths, extra prose, and unsupported language labels.
- [ ] **Step 2: Run** `python -m pytest -q tests/test_official_solutions.py` and verify missing-codec failures.
- [ ] **Step 3: Implement** `EdgeBenchBundleCodec`, `ALEBenchCodeCodec`, and content-addressed storage. Normalize line endings, canonicalize JSON, calculate structural summaries without embedding answer text, and materialize Edge archives only below a new per-attempt directory.
- [ ] **Step 4: Run** focused tests and require all green.
- [ ] **Step 5: Commit** with `git commit -m "feat: add EdgeBench and ALE-Bench candidate codecs"`.

### Task 3: Official Evaluator Adapters

**Files:**
- Create: `optimization_lab/harness_builder/adapters/edgebench_official.py`
- Create: `optimization_lab/harness_builder/adapters/alebench_official.py`
- Test: `tests/test_edgebench_official_adapter.py`
- Test: `tests/test_alebench_official_adapter.py`

- [ ] **Step 1: Write failing tests** around real subprocess/session boundaries. Edge tests require argv lists with pinned task/log roots and parse only SForge JSON. ALE tests require `public_eval` during evolution and reject `private_eval` until a freeze receipt is supplied.
- [ ] **Step 2: Run** both focused test modules and confirm expected missing-adapter failures.
- [ ] **Step 3: Implement** controller-owned private evidence files and strict public projections. Public feedback uses allowlisted status/reason/aggregate score fields; private stdout, stderr, cases, seeds, paths, rank maps, and hidden outputs never enter `EvaluationResult.public`.
- [ ] **Step 4: Add fail-closed identity checks** for source commit, dataset revision, task ID, Docker image digest, timeout, score direction, and evaluator command.
- [ ] **Step 5: Run** focused tests and existing adapter tests; require all green.
- [ ] **Step 6: Commit** with `git commit -m "feat: connect official EdgeBench and ALE-Bench evaluators"`.

### Task 4: Experiment-One Evolution, Freeze, and Cross Matrix

**Files:**
- Create: `optimization_lab/harness_builder/experiment_one.py`
- Test: `tests/test_experiment_one.py`

- [ ] **Step 1: Write failing tests** proving A/B/C start from byte-identical H0 in separate workspaces, each lineage runs eight rounds, best Harness selection uses score/earliest-round/SHA ordering, a valid `FreezeReceipt` cannot be issued without a valid numeric official score, and every 3x3 cross-test cell calls the Task Harness exactly once without constructing or calling a Builder. Add `H0BaselineReceipt` tests proving no Builder is constructed or called, `upper_model_configuration_hash` represents the configured-but-uncalled formal Builder Harness model, `lower_model_configuration_hash` represents the formal Task Harness/Solver model, both resolve to `gpt-5.6-sol`/`high`, the hashes are equal, and the call ledger is Builder `0`/Solver `1` rather than two Solver calls.
- [ ] **Step 2: Add red tests** proving target IDs, submission paths, raw prior answers, and target history are absent from a transferred Harness; target binding is supplied separately at execution time.
- [ ] **Step 3: Run** `python -m pytest -q tests/test_experiment_one.py` and verify the controller is missing.
- [ ] **Step 4: Implement** frozen `ExperimentOneManifest`, `LineageRunner`, `FreezeReceipt`, `CrossTestReceipt`, `H0BaselineReceipt`, and `CrossMatrixRunner`. Bind every receipt to contract, source, task, Harness ancestry, candidate, evaluator, audit ledger, model, transport, and effort hashes. Each target/seed `H0BaselineReceipt` requires a fresh root, no Builder construction or call, and `upper_model_configuration_hash == lower_model_configuration_hash` for `gpt-5.6-sol`/`high`, where the canonical payload contains only provider, API family/transport, model, reasoning effort, max output tokens, sampling parameters, and tool permission policy, excluding prompt, Harness content, operation ID, and task binding. It records Builder/Solver/official-evaluator call counts of `0`/`1`/`1`.
- [ ] **Step 5: Implement deterministic recovery**: completed operations replay, started-without-result becomes terminally abandoned and consumes budget, and no operation ID is automatically reissued.
- [ ] **Step 6: Run** focused tests plus all dual-Harness tests; require all green.
- [ ] **Step 7: Commit** with `git commit -m "feat: orchestrate Harness specialization experiment"`.

### Task 5: Production CLI and Frozen Manifests

**Files:**
- Create: `scripts/run_moss_experiment_one.py`
- Create: `optimization_lab/harness_builder/manifests/experiment_one_edgebench.json`
- Create: `optimization_lab/harness_builder/manifests/experiment_one_alebench.json`
- Test: `tests/test_experiment_one_cli.py`
- Modify: `README.md`
- Modify: `TEST.md`
- Modify: `CLAUDE.md`

- [ ] **Step 1: Write failing CLI tests** for `preflight`, `canary`, `evolve`, `freeze`, `cross-test`, `report`, and `resume`. All mutating/model/evaluator commands require `--execute`; default invocation is read-only.
- [ ] **Step 2: Run** `python -m pytest -q tests/test_experiment_one_cli.py` and verify the entry point is missing.
- [ ] **Step 3: Implement** the CLI with exact model assertions (`gpt-5.6-sol`, `high`, Responses API), per-suite/instance/seed roots, fixed eight-round caps, separate canary/formal roots, and machine-readable progress/status output.
- [ ] **Step 4: Add manifests** pinned to EdgeBench A/B/C as `apple_incremental_game`/`molecular_self_assembly`/`treant_forest` and ALE-Bench A/B/C as `ahc024`/`ahc026`/`ahc011`, plus official source/data revisions, resource envelopes, and the shared seed IDs `S1`/`S2`/`S3`. The CLI must reject any formal manifest that changes a position mapping, seed ID, or the exactly-three-distinct-targets contract.
- [ ] **Step 5: Update documentation** with exact commands, artifact layout, information boundary, recovery behavior, and the distinction between eight-round mechanism evidence and leaderboard-comparable full-budget results.
- [ ] **Step 6: Run** CLI tests and full repository tests; require all green.
- [ ] **Step 7: Commit** with `git commit -m "feat: add experiment-one production CLI"`.

### Task 6: EC2 Preflight and Real Canaries

**Files:**
- Create at runtime: `/home/ubuntu/Projects/moss-exp1-official/contracts/`
- Create at runtime: `/home/ubuntu/Projects/moss-exp1-official/canary/`

- [ ] **Step 1: Install official dependencies** in separate pinned virtual environments and record `pip freeze`, Python identity, Docker version, host CPU/memory/disk, and source commits.
- [ ] **Step 2: Fetch official task revisions** and pull only the two frozen Edge images; build ALE judge images for the frozen judge version. Record immutable image digests.
- [ ] **Step 3: Run no-model positive and negative evaluator canaries** for both benchmarks. Verify invalid artifacts receive terminal failure/floor score and known-valid artifacts receive valid numeric scores.
- [ ] **Step 4: Run one real Builder+Solver route canary per benchmark** with `gpt-5.6-sol` and `high`. Store the complete model audit and evaluator receipts outside formal roots.
- [ ] **Step 5: Independently audit canary evidence** and do not start formal calls until model identity, score projection, hidden-data boundary, and replay behavior all pass.

### Task 7: Formal Run, Analysis, and Delivery

**Files:**
- Create at runtime: `/home/ubuntu/Projects/moss-exp1-official/formal/`
- Create: `docs/reports/2026-08-26-moss-experiment-one-results.md`
- Modify: `PROGRESS.md`

- [ ] **Step 1: Launch six isolated lineages**: Edge A/B/C and ALE A/B/C. Run both benchmarks and all three lineages per benchmark concurrently when CPU/memory and API gates remain within the manifests; never share workspace, candidate, score history, Memory, or Builder state.
- [ ] **Step 2: Freeze best Harnesses** after all eight rounds and verify complete ancestry, operation journals, and a valid numeric official score before issuing each valid `FreezeReceipt`.
- [ ] **Step 3: For `S1`, run the nine no-evolution cells per benchmark in fresh roots and create one `H0BaselineReceipt` per target from its own fresh root; if all nine cells are valid, repeat the complete three-lineage evolution, formal 3x3 matrix, and H0 baselines for `S2` and `S3`. Every H0 receipt proves equal upper Builder/lower Task Harness model configuration hashes for `gpt-5.6-sol`/`high`, while its call ledger remains Builder `0`, Solver `1`, and official evaluator `1`.
- [ ] **Step 4: Generate native-score tables and paired specialization statistics** without pooling incomparable scores across benchmarks. Mark one-way, invalid, or contract-confounded results explicitly.
- [ ] **Step 5: Run a final evidence audit** proving every reported cell maps to a real evaluator receipt and no canary/fixture/setup event entered the formal table.
- [ ] **Step 6: Commit code and report, rebase against the authorized remote, push to `apexin-ai/apex-moss`, and record the pushed commit. If GitHub authorization still returns 403, preserve the local commit and report that external blocker without weakening experimental evidence.
