# analysis exp 001 sft 0pct 3B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_0pct_3B_20260513T232449_result.json`
- **Structured JSON:** [`eeb23c7ba4f282ee6dc8.json`](../../sessions/ee/eeb23c7ba4f282ee6dc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已全部更新完成，status=DONE, conclusion=success。

三个模型 clean baseline 对比：

| 模型 | Final Loss | Mean Loss | Token Acc | 训练时间 |
|------|-----------|-----------|-----------|---------|
| 0.5B | 1.4894 | 1.5388 | 0.682 | 52.9 min |
| 1.5B | 1.2039 | 1.2599 | 0.711 | 101.5 min |
| **3B** | **1.0736** | **1.1306** | **0.734** | **214.7 min** |

符合预期：模型越大，loss 越低、accuracy 越高，训练时间大致线性增长。

---
