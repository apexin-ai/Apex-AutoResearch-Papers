# analysis alpha sweep a000 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a000_s43_20260516T184610_result.json`
- **Structured JSON:** [`937a92afa63201bcd6f5.json`](../../sessions/93/937a92afa63201bcd6f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE/success。

## 结果摘要

**alpha_sweep_a000_s43 (null baseline, α=0.00, seed=43)**

### Drift (gen0→gen10)
| Metric | Drift% | 与 s42 一致性 |
|--------|--------|--------------|
| token_entropy | -4.4% | s42=-5.1% ✓ |
| ece | +37.2% | s42=+51.7% ✓ (方向一致,ECE noisy) |
| perplexity | -20.3% | s42=-21.7% ✓ |
| distinct_1 | -13.9% | s42=-13.8% ✓ |
| distinct_2 | -9.8% | s42=-9.8% ✓ |
| distinct_3 | -4.8% | s42=-4.5% ✓ |

### 5-Method 因果分析
- **Permutation Granger (FDR)**: 0/8 significant
- **TY Granger**: 1/8 (token_entropy→distinct_1, p=0.036, 但 df_resid=1 不可靠 — 符合 C003 约束)
- **Robust consensus (≥3/5)**: **0/8**
- **FPR 控制**: 正常

**结论: SUCCESS** — 框架在 null 条件下无 false positive，cross-seed 一致性高。

---
