# analysis qwen15b full trace tail1024 seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen15b_full_trace_tail1024_seed42_20260518T014349_result.json`
- **Structured JSON:** [`4bd0c063b34c8656e901.json`](../../sessions/4b/4bd0c063b34c8656e901.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，registry 已更新为 DONE/success。

**结果摘要**:
- **Accuracy: 96.6%** (95% CI: 95.5%-97.6%)，fail F1=0.94，pass F1=0.98
- **Hypothesis 被证伪**: tail-1024 (96.6%) > tail-512 (95.6%)，Qwen-1.5B 不存在 non-monotonicity
- 1.5B 在 tail-1024 与 7B (~96.5%) 和 DeepSeek (96.47%) 表现持平
- tail-512 → tail-1024 提升 +1.0pp，tail-1024 → tail-2048 持平 (~96.6%)，说明 tail-1024 已接近饱和

---
