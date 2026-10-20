# analysis d102 t15 a075 s43

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d102_t15_a075_s43_20260522T071610_result.json`
- **Structured JSON:** [`d9a9878009b6f14f570f.json`](../../sessions/d9/d9a9878009b6f14f570f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果摘要

| 指标 | 值 |
|------|------|
| **PermG_fwd** | **6/8** |
| **Robust pairs (≥3/5)** | **6/8** |
| MAUVE pairs consensus | 1/5 (both token_entropy<mauve and ece<mauve) |

### 逐代 MAUVE
MAUVE 全程极低（0.028–0.034），无明显单调趋势，确认 MAUVE bottleneck。

### Consensus 细节
- 4/5: token_entropy→distinct_1, token_entropy→distinct_2, ece→distinct_1, ece→distinct_2
- 3/5: token_entropy→distinct_3, ece→distinct_3
- 1/5: token_entropy→mauve, ece→mauve（仅 diff_xcorr 显著）

### Cross-seed 对比
**s42=6/8, s43=6/8 — 完全一致。** α=0.75 远超 α_c(15)≈0.304，6/8 ceiling 在 T=15 下 seed-robust。Registry 已更新为 DONE(success)。

---
