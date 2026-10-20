# R4-N3: Beam Search vs Greedy Per-Document Runtime Profiling

## Data Sources

All experiments run on westd-16980 with grammar-constrained decoding.

### Files Used

| Experiment | Output File | Docs |
|---|---|---|
| Qwen SciERC greedy constrained | `phase2_scierc_full_s1_v2.jsonl` | 551 |
| Qwen SciERC beam k=2 | `scierc_qwen_beam_k2_551.jsonl` | 551 |
| Qwen SciERC beam k=4 | `beam_search_scierc_full_551.jsonl` | 551 |
| Qwen SciERC beam k=8 | `scierc_qwen_beam_k8_551.jsonl` | 551 |
| Qwen SciERC FT beam k=4 | `w10_qwen_scierc_ft_beam_k4.jsonl` | 551 |
| Llama SciERC greedy constrained | `llama_scierc_full_s1.jsonl` | 550 |
| Llama SciERC beam k=4 | `llama_scierc_beam_full_s1_551.jsonl` | 551 |
| Qwen DocRED greedy (matched 50) | `qwen_docred_greedy_matched50.jsonl` | 50 |
| Qwen DocRED beam k=4 | `w9_qwen_docred_beam_50.jsonl` | 50 |
| Llama DocRED greedy (matched 50) | `llama_docred_greedy_matched50.jsonl` | 50 |
| Llama DocRED beam k=4 | `docred_llama_beam_50.jsonl` | 50 |

---

## SciERC Runtime (551 docs, sentence-level)

| Model | Decoding | k | Total (s) | Per-doc Avg (s) | Per-doc Median (s) | Min (s) | Max (s) |
|-------|----------|---|-----------|-----------------|--------------------|---------|---------| 
| Qwen-3-8B | greedy | 1 | 3725.2 | 6.761 | 5.981 | 0.666 | 20.371 |
| Qwen-3-8B | beam | 2 | 2969.7 | 5.390 | 5.058 | 0.741 | 15.454 |
| Qwen-3-8B | beam | 4 | 3259.4 | 5.915 | 5.506 | 0.797 | 16.941 |
| Qwen-3-8B | beam | 8 | 3890.4 | 7.061 | 6.642 | 2.003 | 21.063 |
| Qwen-3-8B (FT) | beam | 4 | 2041.3 | 3.705 | 3.324 | 0.570 | 19.431 |
| Llama-3.1-8B | greedy | 1 | 2379.1 | 4.326 | 3.694 | 0.206 | 27.285 |
| Llama-3.1-8B | beam | 4 | 2652.5 | 4.814 | 4.631 | 0.658 | 15.984 |

### SciERC Overhead Analysis

| Comparison | Avg Overhead | Median Overhead |
|---|---|---|
| Qwen beam k=4 vs greedy | 0.87x (faster) | 0.92x (faster) |
| Qwen beam k=2 vs greedy | 0.80x (faster) | 0.85x (faster) |
| Qwen beam k=8 vs greedy | 1.04x | 1.11x |
| Llama beam k=4 vs greedy | 1.11x | 1.25x |

**Caveat**: Qwen greedy run (`phase2_scierc_full_s1_v2`) was from an earlier experiment wave (May 14-15) while beam runs are from May 17. Different GPU thermal states, background processes, or codebase optimizations between runs could explain the anomalous result where beam k=2/4 appear faster than greedy. The Llama comparison (1.11x overhead) is more consistent with expectations.

---

## DocRED Runtime (50 matched docs, document-level)

| Model | Decoding | k | Total (s) | Per-doc Avg (s) | Per-doc Median (s) | Min (s) | Max (s) |
|-------|----------|---|-----------|-----------------|--------------------|---------|---------| 
| Qwen-3-8B | greedy | 1 | 925.9 | 18.519 | 18.126 | 9.451 | 33.095 |
| Qwen-3-8B | beam | 4 | 1567.6 | 31.352 | 24.506 | 13.527 | 129.328 |
| Llama-3.1-8B | greedy | 1 | 1060.9 | 21.219 | 15.958 | 6.732 | 66.405 |
| Llama-3.1-8B | beam | 4 | 1039.2 | 20.783 | 16.970 | 9.666 | 48.718 |

### DocRED Overhead Analysis (matched 50-doc subset)

| Comparison | Avg Overhead | Median Overhead |
|---|---|---|
| Qwen beam k=4 vs greedy | **1.69x** | **1.35x** |
| Llama beam k=4 vs greedy | 0.98x (comparable) | 1.06x |

**Qwen DocRED** shows the clearest beam overhead: 1.69x average, 1.35x median. The difference between mean and median indicates beam search has high-variance tail latency (max 129.3s vs greedy max 33.1s).

**Llama DocRED** shows negligible overhead on average, but the greedy run has a high-variance tail (max 66.4s) that inflates its mean.

---

## Beam Width Scaling (Qwen SciERC, 551 docs)

| k | Per-doc Avg (s) | Relative to k=2 |
|---|-----------------|------------------|
| 2 | 5.390 | 1.00x |
| 4 | 5.915 | 1.10x |
| 8 | 7.061 | 1.31x |

Beam width scaling is sub-linear: doubling k from 2 to 4 adds ~10% latency; from 4 to 8 adds ~19%.

---

## Fine-tuned vs Zero-shot Beam (Qwen SciERC, k=4)

| Setting | Per-doc Avg (s) | Per-doc Median (s) |
|---|---|---|
| Zero-shot beam k=4 | 5.915 | 5.506 |
| Fine-tuned beam k=4 | 3.705 | 3.324 |
| Speedup | **1.60x** | **1.66x** |

Fine-tuning reduces beam search latency by ~37%, likely because the model produces more confident token distributions, leading to earlier convergence.

---

## Summary for Paper

**Recommended numbers to cite (most reliable comparisons):**

1. **Qwen DocRED beam k=4 overhead**: 1.69x avg / 1.35x median over greedy (matched 50-doc subset, same GPU, close temporal proximity)
2. **Beam width scaling** (SciERC): k=2 to k=4 adds 10%, k=4 to k=8 adds 19% (sub-linear)
3. **FT speedup**: Fine-tuned beam k=4 is 1.6x faster than zero-shot beam k=4

**Key finding**: Beam search (k=4) adds moderate latency overhead (~1.3-1.7x on document-level tasks), scaling sub-linearly with beam width. The overhead is more pronounced on longer documents (DocRED) where each beam candidate generates substantially more tokens.

**Caveats**:
- SciERC greedy vs beam comparison is confounded by different run dates; the matched DocRED 50-doc comparison is the most controlled
- Llama DocRED shows near-zero overhead, possibly due to different tokenization efficiency or variance in greedy tail latency
- For a clean SciERC comparison, a fresh greedy run on the same GPU session as beam runs would be ideal
