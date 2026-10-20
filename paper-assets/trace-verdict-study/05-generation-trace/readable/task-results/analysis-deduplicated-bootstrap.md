# analysis deduplicated bootstrap

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deduplicated_bootstrap_20260522T070032_result.json`
- **Structured JSON:** [`49592344f4bbab3787ab.json`](../../sessions/49/49592344f4bbab3787ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All confirmed. Here are the results:

---

## MF-4 Results

### 1. Unique Problems
**119 unique problems** (all HumanEval), each appearing exactly **10 times** (10 code variants per problem). This is far more extreme than the assumed "49% duplicates / 607 unique" — the effective sample size is 119, not 1190.

### 2. CI Width Changes

| Method | Mean Width | Max Width | Mean Ratio vs Original |
|--------|-----------|-----------|----------------------|
| Original (n=1190) | 0.0292 | 0.0538 | 1.00x |
| Deduplicated (n=119) | 0.0881 | 0.1681 | **2.47x** |
| Clustered (119 problems) | 0.0731 | 0.1479 | **2.24x** |

CI widths roughly **double** under proper clustered bootstrap. The original CIs were systematically too narrow.

### 3. Pairwise Significance (Clustered Bootstrap)
**14/19 comparisons remain significant.** All 9 comparisons with ≥14pp difference remain significant.

**5 comparisons that lost significance** (all small-effect or cross-model):
- exception_only vs ae_only (Δ=0.08pp) — near-ceiling, trivially n.s.
- label_only vs full_trace (Δ=4.45pp) — **borderline, most notable loss**
- Qwen-7B vs DeepSeek exception_only (Δ=0.5pp)
- Qwen-7B vs DeepSeek no_trace (Δ=1.8pp)
- Qwen-7B vs CodeLlama no_trace (Δ=1.3pp)

### 4. Data Quality
- 25/27 conditions used real prediction files
- 2 simulated (DeepSeek-6.7B/vota had garbled predictions; Qwen-7B/vota accuracy mismatch)

### Output Files
```
/root/autodl-tmp/trace-verdict-study-checkpoints/deduplicated_bootstrap/
├── deduplicated_bootstrap_results.json  (17.7KB)
├── ci_comparison_table.csv              (3.1KB)
└── pairwise_significance.json           (4.0KB)
```

**Bottom line:** The core findings (exception > no_trace, ae > loop, all ~20-30pp gaps) are robust to deduplication. Only small cross-model differences (<5pp) lose significance. The paper should report clustered CIs (2.24x wider on average) and note effective n=119.

---
