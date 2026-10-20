# analysis alpha sweep a045 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha_sweep_a045_s42_fp32_20260519T224707_result.json`
- **Structured JSON:** [`8be24059c7d6dde6a28d.json`](../../sessions/8b/8be24059c7d6dde6a28d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

**结果**: α=0.45 PermG fwd (FDR) = **0/8**，onset boundary 从 [0.40, 0.50] 缩窄至 **[0.45, 0.50]**。

关键数据：
| 指标 | 值 |
|------|-----|
| PermG fwd/rev | 0/8, 0/8 |
| K≥3 consensus | 3/8 |
| K≥4 consensus | 0/8 |
| naive_xcorr (fwd) | 7/8 |
| diff_xcorr (fwd) | 3/8 |
| threshold_onset | 8/8 |
| TY granger | 1/8 (ece→mauve, df_resid=1 不可靠) |
| Δ entropy | −18.7% |
| Δ d1/d2/d3 | −35.4% / −47.9% / −47.8% |

值得注意：4/8 pairs 的 PermG raw p < 0.07（FDR 后 > 0.09），说明 α=0.45 处于 onset 近侧但未跨过阈值。K≥3 从邻近 α 的 6/8 降到 3/8，可能与 α=0.45 下 entropy 的剧烈 gen0→gen1 跌落（−22.9%）然后回升的非单调轨迹有关。

报告已写入 artifacts，registry 已更新为 DONE/success。

---
