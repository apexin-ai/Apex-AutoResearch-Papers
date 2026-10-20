# Re-Repair Phase 0 Results

## Setup
- **Date**: 2026-05-16
- **Server**: westd-48478 (RTX 5090, cuda:2)
- **Model**: Qwen3-8B (base, /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B)
- **Instances**: 10 (T_f2p ≥ 2, partial-failure mutations only)
- **Samples**: K=3 per (instance, condition)
- **Conditions**: control, cls-diag (simulated 84% acc), oracle-diag, random-diag
- **Evaluation**: Sequence similarity to gold patch (no Docker)
- **Runtime**: ~22 minutes total

## Results

### Best-of-K Mean Similarity

| Condition | Mean Sim | Best-of-K Mean | Δ vs Control | Win Rate |
|-----------|----------|---------------|-------------|----------|
| control | 0.815 | 0.820 | — | — |
| cls-diag | 0.775 | 0.818 | -0.002 | 3/10 |
| oracle-diag | 0.773 | 0.809 | -0.011 | 3/10 |
| random-diag | 0.719 | 0.719 | -0.101 | 2/10 |

### Per-Instance Breakdown (Best-of-K)

| Instance | control | cls-diag | oracle | random |
|----------|---------|----------|--------|--------|
| django__django-11848 | 0.779 | 0.780 | 0.780 | 0.780 |
| django__django-12406 | 0.713 | 0.713 | 0.626 | 0.713 |
| django__django-13344 | 0.729 | 0.742 | 0.742 | 0.742 |
| django__django-14315 | 0.938 | 0.938 | 0.938 | 0.938 |
| django__django-14631 | 0.700 | 0.700 | 0.700 | 0.700 |
| psf__requests-6028 | 0.999 | 0.959 | 0.959 | 0.959 |
| pytest-dev__pytest-5787 | 0.468 | 0.468 | 0.468 | 0.468 |
| pytest-dev__pytest-7490 | 0.999 | 0.999 | 0.999 | 0.999 |
| sphinx-doc__sphinx-11445 | 0.999 | 0.999 | 0.999 | 0.885 |
| sympy__sympy-14248 | 0.879 | 0.882 | 0.880 | 0.009 |

### Output Quality
- Valid diff (starts with `diff`): control=100%, cls=97%, oracle=100%, random=90%
- All conditions produce parseable diffs >90% of the time

## Analysis

### Key Findings

1. **Diagnostic info does NOT help** on average: control has the highest best-of-K mean (0.820). All diagnostic conditions score equal or lower.

2. **Random diagnostic is clearly harmful** (-0.101 delta): noisy test names actively confuse the model, especially catastrophically on sympy (0.009 vs 0.879).

3. **Oracle ≈ CLS ≈ Control** for most instances: the deltas are negligible (-0.002 to -0.011). Diagnostic info is neither helping nor hurting significantly.

4. **Ceiling effect on 5/10 instances**: several instances already achieve >0.93 similarity without any diagnostic, leaving no room for improvement.

### Root Causes

1. **Mutations too easy**: operator_swap/off_by_one/boundary_removal mutations create mechanically small differences. An 8B model can reverse these from patch structure alone without needing test diagnostic info.

2. **Base model limitations**: Qwen3-8B (base, not instruct) may not follow diagnostic instructions effectively. The diagnostic section may read as noise rather than actionable info.

3. **Text similarity ≠ functional correctness**: A patch that fixes different tests than the gold might still be functionally correct but score low on similarity. Conversely, near-identical patches might still fail.

4. **Prompt length competition**: Diagnostic sections (even truncated) add context that may displace useful patch/problem information from the effective attention window.

## Go/No-Go Assessment

**Result: INCONCLUSIVE (lean proceed with modifications)**

- The hypothesis is NOT refuted — the weak signal could be due to task design (too-easy mutations) and model choice (base vs instruct)
- random-diag < control confirms the model IS reading the diagnostic section
- The real test requires: (a) harder incorrect patches, (b) instruct model, (c) Docker verification

## Recommendations for Phase 1

1. **Use agent predictions** (not mutations) as incorrect patches — structurally different from gold, harder to fix
2. **Use instruct model** (Qwen3-8B-Instruct, or Claude/GPT-4 API for stronger signal)
3. **Docker execution** for evaluation (the actual resolve rate metric)
4. **Reduce diagnostic verbosity** — only show failing tests (skip the long pass list)
5. **Increase K** to 5-10 for better best-of-K estimation

## Artifacts

- Remote results: `/root/autodl-tmp/eval_results/re_repair_phase0/`
  - `phase0_dataset.jsonl` — 10 selected instances
  - `phase0_repairs.jsonl` — 120 generated repairs
  - `phase0_summary.json` — aggregate metrics
- Script: `/home/sonny/exec-sim-repair-verifier/re_repair_phase0.py`
