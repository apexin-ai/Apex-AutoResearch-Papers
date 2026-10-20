# ops diagnose eval d025v3 batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-eval-d025v3-batch_20260516T034759_result.json`
- **Structured JSON:** [`3f092039e763ce8a9871.json`](../../sessions/3f/3f092039e763ce8a9871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，conclusion 保持 `killed`，notes 记录了详细完成状态。

**总结：**
| 部分 | 状态 | 详情 |
|------|------|------|
| aligned | 完成 | mmlu=0.624, gsm8k=0.682, arc=0.823，.done 标记存在 |
| para_aligned | 未完成 | mmlu paraphrased 已跑完但未落盘，GSM8K paraphrased 18% 时被 kill，arc paraphrased 未开始 |

需要重跑 para_aligned eval。aligned 结果可直接使用。

---
