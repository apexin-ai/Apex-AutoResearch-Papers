# check plan003 status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_plan003_status_20260515T093329_result.json`
- **Structured JSON:** [`1e7345b8fabab5042cfb.json`](../../sessions/1e/1e7345b8fabab5042cfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. vota_exception_only_seed42_v2 — **已完成**

- **PID 79633**: 已退出（进程不存在）
- **GPU**: 无活跃进程
- **Checkpoint**: `/exception_only/final/` 已生成，含 adapter 模型 + eval 结果
- **eval_results.json**:
  - **Accuracy: 99.83%** (n=1190)
  - Majority baseline: 71.51%, Lift: +28.32%
  - Pass: precision=1.0, recall=0.998, F1=0.999
  - Fail: precision=0.994, recall=1.0, F1=0.997

### 2. vota_loop_only_seed42 — **训练中**

- **PID 82362**: 存活，已运行 1h35m43s
- **GPU**: PID 82372 占用 cuda:0，显存 33306 MiB
- **训练进度**: step **344/444** (77%)，约 ~16s/it，预计还需 ~26 分钟
- **Checkpoint**: 已有 `checkpoint-148` 和 `checkpoint-296`，尚无 `final/`
- **Eval**: 训练未完成，eval 尚未开始

---
