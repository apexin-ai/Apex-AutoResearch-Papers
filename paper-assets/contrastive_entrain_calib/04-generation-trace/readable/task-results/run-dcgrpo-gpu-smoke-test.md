# run dcgrpo gpu smoke test

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_dcgrpo_gpu_smoke_test_20260518T123458_result.json`
- **Structured JSON:** [`d9580a7c4c20a3c081b5.json`](../../sessions/d9/d9580a7c4c20a3c081b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

本地文件已同步修复。

**总结**: 3 项测试全部 PASSED。唯一需要修复的 bug 是 `directions.pt`（Float32）与模型 hidden states（BFloat16）的 dtype 不匹配，已在本地和远程同步修复。R1/R2 的分布显示 4 对中有 2 对 contrastive 方向正确（R2=0.5），2 对反转（R2≈-0.5），符合小样本冒烟测试的预期波动。

---
