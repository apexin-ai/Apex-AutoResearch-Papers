# diagnose prune k05 spatial v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_prune_k05_spatial_v2_20260519T131812_result.json`
- **Structured JSON:** [`75f481b2505cefb418f0.json`](../../sessions/75/75f481b2505cefb418f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**进程状态：正常完成退出（非崩溃）。** Cron 检测到的"进程消失"是因为实验跑完了。

**结果：**
- Overall SR: **0.00%** (0/500)，Wilson 95% CI: [0.00%, 0.76%]
- 10 个 task 全部 0/50，与预期一致（k=0.5 random pruning 移除一半视觉 token 导致完全失效）
- 结果 JSON 已完整保存：`smolvla_random_prune_k05_spatial.json`

**无需重启。** Registry 已更新为 DONE/success，metrics 已写入。cuda:2 现已空闲可用。

---
