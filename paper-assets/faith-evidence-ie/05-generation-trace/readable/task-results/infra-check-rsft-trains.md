# infra check rsft trains

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_rsft_trains_20260516T002355_result.json`
- **Structured JSON:** [`3347cbf60db133c242af.json`](../../sessions/33/3347cbf60db133c242af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### rsft_ced_s43_train_r3 (PID 277310, cuda:1)
- **状态**: 运行中，已运行 3h08m
- **进度**: step 31/510 (epoch 1/3, ~6%)，约 5.5s/step
- **GPU 1**: PID 277315 占用 28,341 MiB / 32,607 MiB

### rsft_ced_s45_train_r3 (PID 277407, cuda:2)
- **状态**: 已失败，退出码 1
- **失败时间**: 2026-05-16T00:21:27Z（启动后很快崩溃）
- **原因**: CUDA OOM — 模型加载阶段 `cudaMemGetInfo` 报 out of memory
- **根因**: GPU 2 被 PID 276148 占用 31,639 MiB / 32,607 MiB，s45 无法分配显存

### 4 张 GPU 状态

| GPU | PID | 显存占用 | 说明 |
|-----|-----|---------|------|
| 0 | 270467 | 10,855 / 32,607 MiB | 其他任务 |
| 1 | 277315 | 28,341 / 32,607 MiB | **s43 训练中** |
| 2 | 276148 | 31,639 / 32,607 MiB | 其他任务（导致 s45 OOM） |
| 3 | 272169 | 10,859 / 32,607 MiB | 其他任务 |

**结论**: s43 正常训练中（进度较慢，510 步预计还需 ~44 min）。s45 因 GPU 2 被占满而 OOM 失败，需要等 GPU 2 空闲后重新提交，或改用其他空闲 GPU。

---
