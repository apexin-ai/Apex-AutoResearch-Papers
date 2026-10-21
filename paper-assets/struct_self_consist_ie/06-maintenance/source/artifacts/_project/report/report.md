# VC Quartile Stratification Analysis (D105)

**Core question:** Does LP selection recover effectiveness on high-VC (high voting confidence) instances?

**Data:** Qwen-2.5 8B, N=8 samples, `_rerun_1024` experiments. Gold-empty instances excluded.

## Results

### SciERC NER (n=529)

| Quartile | n | VC range | Mean VC | Greedy | LP sel | LP delta | SJ sel | FK sel | EM sel | Oracle | Headroom |
|----------|---|----------|---------|--------|--------|----------|--------|--------|--------|--------|----------|
| Q1 | 132 | 0.13-0.38 | 0.296 | 0.556 | 0.572 | **+0.016** | 0.562 | 0.559 | 0.531 | 0.725 | 0.169 |
| Q2 | 132 | 0.38-0.63 | 0.512 | 0.648 | 0.642 | -0.006 | 0.629 | 0.631 | 0.625 | 0.792 | 0.144 |
| Q3 | 132 | 0.63-0.75 | 0.677 | 0.586 | 0.606 | **+0.020** | 0.604 | 0.605 | 0.605 | 0.754 | 0.168 |
| Q4 | 133 | 0.75-1.00 | 0.921 | 0.784 | 0.780 | -0.004 | 0.784 | 0.784 | 0.784 | 0.832 | 0.048 |
| **Overall** | 529 | — | — | 0.644 | 0.650 | +0.006 | 0.645 | 0.645 | 0.636 | 0.776 | 0.132 |

### SciERC RE (n=397)

| Quartile | n | VC range | Mean VC | Greedy | LP sel | LP delta | SJ sel | FK sel | EM sel | Oracle | Headroom |
|----------|---|----------|---------|--------|--------|----------|--------|--------|--------|--------|----------|
| Q1 | 99 | 0.13-0.38 | 0.232 | 0.310 | 0.275 | -0.036 | 0.301 | 0.313 | 0.249 | 0.521 | 0.211 |
| Q2 | 99 | 0.38-0.50 | 0.439 | 0.393 | 0.373 | -0.021 | 0.355 | 0.348 | 0.324 | 0.591 | 0.197 |
| Q3 | 99 | 0.50-0.75 | 0.616 | 0.476 | 0.454 | -0.022 | 0.438 | 0.429 | 0.406 | 0.646 | 0.171 |
| Q4 | 100 | 0.75-1.00 | 0.894 | 0.437 | 0.477 | **+0.040** | 0.448 | 0.448 | 0.448 | 0.582 | 0.145 |
| **Overall** | 397 | — | — | 0.404 | 0.395 | -0.009 | 0.386 | 0.387 | 0.372 | 0.585 | 0.181 |

### CoNLL NER (n=2756)

| Quartile | n | VC range | Mean VC | Greedy | LP sel | LP delta | SJ sel | FK sel | EM sel | Oracle | Headroom |
|----------|---|----------|---------|--------|--------|----------|--------|--------|--------|--------|----------|
| Q1 | 689 | 0.13-0.75 | 0.550 | 0.774 | 0.737 | -0.037 | 0.738 | 0.739 | 0.733 | 0.903 | 0.130 |
| Q2 | 689 | 0.75-1.00 | 0.899 | 0.918 | 0.913 | -0.005 | 0.919 | 0.918 | 0.918 | 0.950 | 0.032 |
| Q3 | 689 | 1.00 | 1.000 | 0.964 | 0.964 | -0.000 | 0.964 | 0.963 | 0.964 | 0.965 | 0.001 |
| Q4 | 689 | 1.00 | 1.000 | 0.975 | 0.975 | 0.000 | 0.975 | 0.975 | 0.975 | 0.975 | 0.000 |
| **Overall** | 2756 | — | — | 0.908 | 0.897 | -0.010 | 0.899 | 0.899 | 0.898 | 0.948 | 0.040 |

**Note:** CoNLL Q3/Q4 are degenerate (VC=1.0, all 8 samples identical) — 50% of CoNLL instances have perfect agreement, leaving no room for selection.

## Key Findings

### 1. LP selection does NOT robustly recover in high-VC instances

- **SciERC NER Q4 (VC=0.92):** LP delta = -0.004 (slightly negative). No recovery.
- **SciERC RE Q4 (VC=0.89):** LP delta = **+0.040** (positive). This is the only clear recovery signal, and it's the strongest delta across all quartile x dataset combinations.
- **CoNLL NER:** High VC means trivial selection (all samples identical). LP delta converges to 0 as VC -> 1.0.

### 2. LP delta is non-monotonic across VC quartiles

For SciERC NER, the pattern is +0.016, -0.006, +0.020, -0.004 (Q1->Q4). There is no monotonic relationship between VC and LP effectiveness.

### 3. Oracle headroom shrinks with higher VC

This is the most consistent finding:
- SciERC NER: headroom drops from 0.169 (Q1) to 0.048 (Q4)
- SciERC RE: headroom drops from 0.211 (Q1) to 0.145 (Q4)
- CoNLL NER: headroom drops from 0.130 (Q1) to 0.000 (Q4)

When samples agree more, there's less room for *any* selection signal to improve. But even in Q4, RE retains substantial headroom (0.145), where LP captures ~28% of it.

### 4. All signals underperform greedy in most quartiles

Across all datasets, the dominant pattern is that selection signals (LP, SJ, FK, EM) tend to hurt or match greedy performance. The exception is SciERC RE Q4 (LP) and some scattered small positive deltas in lower quartiles.

### 5. SciERC RE Q4 is the exception

LP in RE Q4 achieves +0.040 delta, substantially outperforming all other signals (SJ/FK/EM at +0.011). This suggests LP carries genuine ranking information for RE when samples are highly consistent — possibly because RE's logprob variance reflects structural correctness more directly than NER's.

## Conclusion

**VC stratification does not solve the LP compression problem for NER.** The LP delta remains near-zero or negative in high-VC NER instances across both datasets. For **RE only**, there is evidence of LP recovery in Q4 (+0.040), but this is insufficient to change the overall negative delta. The core finding stands: logprob-based selection is not an effective sample ranker for structured IE, even when restricted to high-agreement subsets.
