# check 5seed pid status

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_5seed-pid-status_20260515T135100_result.json`
- **Structured JSON:** [`4deb09be3a99cbce7c5d.json`](../../sessions/4d/4deb09be3a99cbce7c5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Batch 1 训练状态总结

### PID 状态：4/4 全部存活

| PID | 任务 | GPU | 运行时间 |
|-----|------|-----|---------|
| 154589 | vanilla-seed1 | cuda:0 | 11m04s |
| 154666 | vanilla-seed7 | cuda:1 | 11m03s |
| 154937 | taxei-seed1 | cuda:2 | 11m00s |
| 155145 | taxei-seed7 | cuda:3 | 10m57s |

### GPU 使用情况：全部繁忙

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 18659/32607 MiB | 82% |
| 1 | 18659/32607 MiB | 85% |
| 2 | 19537/32607 MiB | 64% |
| 3 | 19537/32607 MiB | 94% |

### 训练进度

| 任务 | 进度 | 最新 loss | token_acc | 速度 | 预计剩余 |
|------|------|----------|-----------|------|---------|
| vanilla-seed1 | 302/1635 (18%) | 0.567 @step150 | 0.817 | ~2.15s/it | ~49min |
| vanilla-seed7 | 299/1635 (18%) | 0.571 @step150 | 0.816 | ~2.05s/it | ~46min |
| taxei-seed1 | 333/3387 (10%) | 0.565 @step305 | 0.819 | ~2.02s/it | ~1h40m |
| taxei-seed7 | 328/3387 (10%) | 0.563 @step305 | 0.819 | ~1.90s/it | ~1h40m |

### 关键信息
- **无 checkpoint 产生**：save_strategy=epoch，vanilla 首个 checkpoint 在 step 545，taxei 在 step 1129，都还没到
- **loss 正常下降**，4 个任务的 loss 和 token_acc 走势一致
- vanilla 两组预计 ~50min 后完成，taxei 两组预计 ~1h40m 后完成

---
