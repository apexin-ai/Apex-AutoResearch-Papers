# code llama70b crossbench

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama70b_crossbench_20260524T081820_result.json`
- **Structured JSON:** [`198881b3c215171c697d.json`](../../sessions/19/198881b3c215171c697d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Results

| Benchmark | Axis | n (consistent) | BT% | BT CI | BT p | Likert d | Likert p (Wilcoxon) | GEE Style OR | GEE Orig OR | Blindspot |
|-----------|------|----------------|-----|-------|------|----------|---------------------|--------------|-------------|-----------|
| AlpacaEval | formality | 47 | 95.7% | [89.4%, 100%] | <0.0001 | 0.211 | 0.0124 | degenerate | degenerate | **No** |
| AlpacaEval | verbosity | 66 | 97.0% | [92.4%, 100%] | <0.0001 | 0.297 | 0.0002 | 0.54 (NS) | 0.54 (NS) | **No** |
| MT-Bench | formality | 36 | 91.7% | [80.6%, 100%] | <0.0001 | 0.234 | 0.0029 | 32.68 (NS) | 0.89 (NS) | **No** |
| MT-Bench | verbosity | — | — | — | — | — | — | — | — | **MISSING DATA** |

### Comparison with LLMBar Llama-70B
| Benchmark | Axis | BT% | Likert | Blindspot |
|-----------|------|-----|--------|-----------|
| LLMBar | formality | 69.5% | NS | **YES** |
| LLMBar | verbosity | 73.5% | NS | **YES** |
| AlpacaEval | formality | 95.7% | p=0.012 | No |
| AlpacaEval | verbosity | 97.0% | p=0.0002 | No |
| MT-Bench | formality | 91.7% | p=0.003 | No |

### Key findings
- **No blindspots on AlpacaEval/MT-Bench** — Llama-70B's Likert scores pick up the style preference (small but significant Cohen's d = 0.21–0.30), unlike LLMBar where Likert was NS.
- **Pairwise bias is much stronger** on these benchmarks (91–97% vs 69–73% on LLMBar), with near-ceiling consistency among position-consistent pairs.
- **Conclusion: negative** — the LLMBar blindspot pattern does not replicate on AlpacaEval/MT-Bench. The style bias is amplified (higher BT%), but so is Likert detection, eliminating the dissociation that defines a blindspot.
- GEE is degenerate or NS across groups due to near-perfect separation in pairwise results.

---
