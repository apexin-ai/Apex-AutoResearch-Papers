# compute round3 bootstrap figure

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_round3-bootstrap-figure_20260516T044618_result.json`
- **Structured JSON:** [`7ee585f545b23d894ca9.json`](../../sessions/7e/7ee585f545b23d894ca9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 tasks complete. Results summary:

### Task 1: N2a — Downstream Bootstrap CI
- **size_matched vs all**: mean Δppl = +0.032, bootstrap 95% CI [0.0316, 0.0326], Cohen's d = 67.3 (large, but n=3)
- Permutation p = 0.25 (floor for n=3 paired test when all diffs agree in sign — 2^3 = 8 possible permutations, minimum two-tailed p = 2/8)
- Paired t-test p = 0.0001 (parametric, more sensitive at n=3)
- All curated variants have higher (worse) perplexity than `all`
- Output: `/root/gen-depth-fingerprint/results/n2a_bootstrap_ci.json`

### Task 2: Per-Generator Binary F1
Extracted from existing LOGO results (7-feature ensemble):
| Generator | Binary F1 | 95% CI |
|-----------|-----------|--------|
| Pythia-1B | 0.795 | [0.780, 0.809] |
| Qwen3-0.6B | 0.756 | [0.742, 0.772] |
| Qwen3-1.7B | 0.748 | [0.732, 0.762] |
| Pythia-2.8B | 0.723 | [0.709, 0.739] |
| OLMo-2-1B | 0.677 | [0.660, 0.692] |
| Qwen3-8B | 0.641 | [0.625, 0.657] |
- Output: `/root/gen-depth-fingerprint/results/per_gen_binary_f1.json`

### Task 3: Strip Plot
- Spearman ρ(feature, depth) per generator — strong negative for entropy_mean, TTR, hapax_ratio across all generators; near-zero for entropy_max and tail_decay
- Output: `/root/gen-depth-fingerprint/figures/fig1_differential_response_strip.{pdf,png}`

### Task 4: Dataset Statistics
- 27,529 total samples across 6 generators × 5 depths
- ~995 samples per generator at depth 0, gradual attrition to ~755–878 at depth 4
- Text length ~1000–1130 chars (mean), with std ~170–365
- Output: `/root/gen-depth-fingerprint/results/dataset_stats_table.tex` + `dataset_stats.json`

---
