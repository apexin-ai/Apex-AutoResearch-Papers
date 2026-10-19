# KernelBench Dual Harness Runner Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Run real dual-Harness evolution and frozen-Harness cross-testing on pinned KernelBench instances using the Responses API for both Builder and Solver and the official remote GPU evaluator.

**Architecture:** A small experiment module creates the same initial executable Task Harness for every instance, archives each generated kernel, projects only public correctness/speed feedback into the Builder, and preserves private scorer logs. The CLI has separate `evolve` and `cross-test` paths; `cross-test` loads an explicit Harness SHA and never constructs or calls a Builder.

**Tech Stack:** Python 3.11+, OpenAI Responses API, existing `DualHarnessRuntime`, `KernelBenchSolutionCodec`, `SolutionArchive`, `SSHKernelBenchAdapter`, pytest.

---

### Task 1: Add the real KernelBench experiment boundary

**Files:**
- Create: `optimization_lab/harness_builder/kernelbench_dual_experiment.py`
- Test: `tests/test_kernelbench_dual_experiment.py`

- [ ] **Step 1: Write failing tests** proving that invalid model output receives public score `0` without a GPU call, valid output is archived and mapped from official evaluator fields, environment failures stop the run, and the initial Harness has an executable draft/check/final/emit flow.
- [ ] **Step 2: Run** `pytest -q tests/test_kernelbench_dual_experiment.py` and verify failure is caused by the missing module.
- [ ] **Step 3: Implement** `initial_kernelbench_harness()`, `KernelBenchPublicEvaluator`, `evolve_instance()`, and `cross_test_frozen_harness()` using the existing typed Harness and solution archive APIs.
- [ ] **Step 4: Run the focused tests** and verify they pass.

### Task 2: Add a production CLI and pinned H200 task protocols

**Files:**
- Create: `scripts/run_kernelbench_dual_experiment.py`
- Create: `optimization_lab/protocols/kernelbench_h200_cumsum_exclusive.json`
- Create: `optimization_lab/protocols/kernelbench_h200_matmul_sigmoid_sum.json`
- Test: `tests/test_kernelbench_dual_experiment_cli.py`

- [ ] **Step 1: Write failing CLI tests** for argument validation, environment-only credentials, separate per-instance workspaces, exact `gpt-5.6-sol/high` configuration, and a `cross-test` path that does not create a Builder.
- [ ] **Step 2: Run** `pytest -q tests/test_kernelbench_dual_experiment_cli.py` and verify the missing CLI behavior fails.
- [ ] **Step 3: Implement** `evolve` and `cross-test` subcommands. Construct `OpenAI(api_key=[REDACTED], base_url=LLM_BASE_URL)` without printing credentials; use `openai_responses` for both layers; require pinned source hashes and an execution-contract hash.
- [ ] **Step 4: Run the focused CLI tests** and verify they pass.

### Task 3: Verify and launch the two P0 lineages

**Files:**
- Modify only the files above plus the existing four `reasoning_effort=high` changes.
- Generate runtime artifacts under an untracked `results/` directory on the experiment EC2.

- [ ] **Step 1: Run** the dual-Harness, generator, codec, and SSH adapter contract tests, then the full test suite.
- [ ] **Step 2: Sync** the tested tree to the CPU experiment EC2, configure its SSH hop to H200 without committing either private key, and run evaluator preflight for both pinned tasks.
- [ ] **Step 3: Launch** two independent eight-round `evolve` processes on different H200 GPUs with Builder and Solver both `gpt-5.6-sol`, effort `high`, and no cross-instance Memory.
- [ ] **Step 4: Verify** each process has a live PID and a first durable model/evaluator record; report exact artifact and log paths. Do not describe fixture output or environment checks as experimental results.
