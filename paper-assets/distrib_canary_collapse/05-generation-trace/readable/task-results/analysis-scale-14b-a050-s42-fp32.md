# analysis scale 14b a050 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scale_14b_a050_s42_fp32_20260520T162250_result.json`
- **Structured JSON:** [`20d5cce2c5be138183b1.json`](../../sessions/20/20d5cce2c5be138183b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。Registry 已更新为 DONE (negative)。

**结果摘要**:

| 方法 | 结果 |
|------|------|
| PermG fwd (FDR) | **0/8** |
| PermG rev (FDR) | 0/8 (控制组正常) |
| Diff XCorr (FDR+方向) | 3/8 |
| Naive XCorr (方向) | 3/8 |
| Threshold 3sigma | 2/8 |
| TY Granger | 0/8 (obs不足) |
| **K≥3** | **0/8** |
| **K≥4** | **0/8** |

**结论: NEGATIVE.** 1.4B 在 α=0.50 无法检测到 lead-lag 因果信号（0/8 pairs 达到 K≥3 共识），而 410M 在相同 α=0.50 下 PermG=6/8。**Onset boundary 随 model scale 上移**——更大的模型需要更高的 contamination ratio 才能产生可检测的 canary lead-lag 模式。

模型坍塌本身很明显（perplexity +79%, distinct_1 -31%），但因果时序结构在此 contamination 水平下对 1.4B 规模模型太弱，无法统计检测。

---
