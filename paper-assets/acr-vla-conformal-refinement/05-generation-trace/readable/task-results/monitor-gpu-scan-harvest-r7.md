# monitor gpu scan harvest r7

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_gpu-scan-harvest-r7_20260524T192151_result.json`
- **Structured JSON:** [`9ad1ef9ee67068116f8f.json`](../../sessions/9a/9ad1ef9ee67068116f8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

扫描完成，报告已注册为 `gpu_scan_r7` (art_20260524_9dfa78)。

**关键发现**:

1. **17 张 GPU 空闲**（cqa1-32758 全部 6 张、bjb1-32546 有 5 张、bjb2-28827 有 4 张、bjb1-18228 有 2 张）
2. **bjb2-40593 K=5 spatial 仍在运行**，约完成 7/10 tasks，部分难题 0/20
3. **CRM 训练 epoch 25/50**，val_loss=0.004854 持续下降，预计 8-10h 完成
4. **eval-a1-baseline-object-s42 未运行**（确认 A1 已放弃）
5. **⚠️ eval-pi05-vla-only-spatial-s42-v2 因 OOM 全部失败 (0/200)**，需重跑
6. **⚠️ Long horizon adaptive CRM 仅 56.5%，低于 VLA-only 58.5%**，trigger_rate 仅 3.8%，CRM 几乎不触发

---
