# analysis dstudy progressive

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dstudy_progressive_20260521T091708_result.json`
- **Structured JSON:** [`dff1b50560f6669fd1d9.json`](../../sessions/df/dff1b50560f6669fd1d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果写入 `results/analysis/dstudy_progressive_validation.json`。

**收敛性结论：converged**

| 指标 | 50 items (CV) | 100 items (CV) | 150 items (CV) | 200 items | 150→200 变化 |
|------|-------------|--------------|--------------|-----------|-------------|
| item_id_pct | 62.46% (3.04%) | 61.61% (1.21%) | 61.99% (0.65%) | 61.08% | 1.47% |
| G_item | 0.625 (3.04%) | 0.616 (1.21%) | 0.620 (0.65%) | 0.611 | 1.47% |
| min_items_G80 | 483 (7.87%) | 499 (3.16%) | 491 (1.74%) | 510 | 3.87% |

所有三项指标 150→200 变化均 <10%，CV 随 subset size 增大单调下降。D-study 投影使用 n_base=200 的公共基准，确保不同 subset sizes 间的 min_items_G80 可比。方差分量估计从 ~100 items 起已高度稳定。

---
