# harvest llama sft s44 withevi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_llama-sft-s44-withevi-2048_20260521T035158_result.json`
- **Structured JSON:** [`872aef285e28a4e73b82.json`](../../sessions/87/872aef285e28a4e73b82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**成功。** Registry 已更新为 DONE，cron 已清除。

## 结果

| 指标 | @1024 | @2048 | Delta |
|------|-------|-------|-------|
| **Ign-F1** | 0.4802 | **0.4655** | **-1.47pp** |
| F1 | — | 0.4798 | — |
| Evi-F1 (DREEAM) | — | 0.3719 | — |
| Evi-F1 (TP) | — | 0.8393 | — |
| EDCR | — | 0.7122 | — |
| Format OK | — | 985/985 (100%) | — |
| Truncated | — | 177/985 | — |
| Predictions | — | 21,530 | — |

s44 with-evidence @2048 的 ign_f1 反而比 @1024 **低 1.47pp**（0.4655 vs 0.4802），与 s42 control 的趋势相反（s42 @2048 比 @1024 高 2.65pp）。s44 模型在更大生成预算下未能受益，truncated 数从 @1024 的水平降到 177/985 但没有转化为更好的 RE 性能。

---
