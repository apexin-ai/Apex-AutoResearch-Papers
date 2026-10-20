# code fig scatter v2 dense

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fig_scatter_v2_dense_20260518T213719_result.json`
- **Structured JSON:** [`d350dc08e6dd28c4959e.json`](../../sessions/d3/d350dc08e6dd28c4959e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Complete. Here are the results:

## 23 Data Points (all N=8, gold-filtered, unified entity F1)

| Condition | Degen% | LP Delta (pp) | Category |
|---|---|---|---|
| SciERC s42 | 17.8 | +0.61 | Qwen canonical |
| CoNLL s42 | 58.0 | -0.81 | Qwen canonical |
| FewNERD s42 | 14.4 | +1.32 | Qwen canonical |
| SciERC s123 | 17.2 | -0.21 | Multi-seed |
| SciERC s456 | 20.4 | -0.28 | Multi-seed |
| CoNLL s123 | 63.0 | -0.77 | Multi-seed |
| CoNLL s456 | 62.9 | -0.73 | Multi-seed |
| FewNERD s123 | 13.1 | +1.44 | Multi-seed |
| FewNERD s456 | 12.1 | +1.37 | Multi-seed |
| LLaMA SciERC s42/123/456 | 24.9-27.4 | -0.38 to +0.19 | LLaMA |
| LLaMA CoNLL s42/123/456 | 89.3-89.4 | +0.02 to +0.14 | LLaMA |
| 3-epoch | 6.4 | -1.18 | Epoch |
| 10-epoch | 47.8 | +0.99 | Epoch |
| rank=8 | 7.2 | -0.47 | Rank |
| T=0.5 / T=0.8 / T=1.2 | 41.4 / 23.8 / 14.9 | -0.23 / +0.03 / -0.61 | Temperature |
| 4B SciERC | 10.4 | -2.23 | Qwen3-4B |
| 4B CoNLL | 90.6 | +0.09 | Qwen3-4B |

## Statistics
- **Spearman rho = 0.052, p = 0.814** (not significant)
- No correlation between degeneracy rate and LP selection delta across all conditions
- The LP delta is confounded by dataset-specific factors: FewNERD consistently benefits from LP selection regardless of degen level, while CoNLL consistently does not

## Outputs
- `artifacts/fig_degeneracy_lp_scatter_v2.pdf` (300 dpi)
- `artifacts/fig_degeneracy_lp_scatter_v2.png` (150 dpi preview)
- `artifacts/scatter_v2_data.json` (all 23 data points)

---
