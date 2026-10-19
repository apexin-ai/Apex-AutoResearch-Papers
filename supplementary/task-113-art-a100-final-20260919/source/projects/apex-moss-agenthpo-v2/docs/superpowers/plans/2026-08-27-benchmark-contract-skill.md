# Benchmark Contract Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make every benchmark-specific output contract an explicit, hashable skill that is injected into each compiled Solver Harness and verified by the existing deterministic parser.

**Architecture:** Extend the existing public capability-card mechanism with EdgeBench and ALE-Bench cards. The compiler will place a compact contract-skill payload and final-output checklist in every solver prompt; receipts will include its hash through the prompt hash. The post-generation codec remains authoritative and no semantic answer repair is introduced.

**Tech Stack:** Python, dataclasses, pytest, existing Harness compiler and solution codecs.

---

### Task 1: Add regression tests for benchmark contract skills

**Files:**
- Modify: `tests/test_official_solutions.py`
- Modify: `tests/test_harness_builder_runtime.py`

- [ ] **Step 1: Write failing tests** for EdgeBench/ALE-Bench capability cards and for their presence in the compiled solver prompt, including the exact response-boundary rule and a stable skill hash.
- [ ] **Step 2: Run the focused tests** and confirm they fail because the two codecs have no capability cards and the prompt has no explicit skill block.

### Task 2: Define public contract skills for EdgeBench and ALE-Bench

**Files:**
- Modify: `optimization_lab/harness_builder/contract_compatibility.py`
- Modify: `optimization_lab/harness_builder/official_solutions.py`

- [ ] **Step 1: Add `edgebench_capability()` and `alebench_capability()` cards** describing the public response boundary, literal template, safe normalizations, forbidden transformations, and failure stages.
- [ ] **Step 2: Attach the cards to `EdgeBenchBundleCodec` and `ALEBenchCodeCodec`.
- [ ] **Step 3: Extend exports and run focused tests.

### Task 3: Inject a contract-skill block into every compiled Solver Harness

**Files:**
- Modify: `optimization_lab/harness_builder/operators.py`

- [ ] **Step 1: Add a helper that serializes the bound artifact contract into a clearly delimited solver-facing skill block.
- [ ] **Step 2: Include the skill block before task data and append a short final-output checklist.
- [ ] **Step 3: Keep the payload public-only and deterministic; do not add hidden evaluator data or answer-repair logic.
- [ ] **Step 4: Run runtime and compile-receipt tests.

### Task 4: Verify and publish

**Files:**
- No additional production files.

- [ ] **Step 1: Run the full relevant pytest suite.
- [ ] **Step 2: Inspect the diff and verify no experiment-setting changes.
- [ ] **Step 3: Create a commit and push it to `apexin-ai/apex-moss` `main` after confirming the remote and branch.

