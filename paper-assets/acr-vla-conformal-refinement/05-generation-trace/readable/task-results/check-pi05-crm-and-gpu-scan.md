# check pi05 crm and gpu scan

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pi05-crm-and-gpu-scan_20260524T112917_result.json`
- **Structured JSON:** [`62d54ededede2f449b72.json`](../../sessions/62/62d54ededede2f449b72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## π0.5 CRM 训练

- 当前进度: **Epoch 2/50, batch 650/684**
- 运行时长: 52 min
- Epoch 1 结果: train_loss=0.014627, val_loss=0.008004 (best)
- Epoch 2 最新 loss: ~0.0126
- 速率: ~25.5 batches/min → ~26.8 min/epoch
- 剩余: 34 batches + 48 epochs ≈ **21.4 小时**
- 预估 ETA: **~2026-05-25 04:00 UTC**

## GPU 空闲扫描

| 服务器 | 总GPU | 空闲GPU | 空闲编号 |
|--------|-------|---------|----------|
| bjb1-18228 | 4 | 1 | cuda:2 |
| bjb1-32546 | 6 | 4 | cuda:0,1,2,3 |
| bjb2-28827 | 6 | 0 | — |
| bjb2-40593 | 1 | 0 | — |
| cqa1-32758 | 6 | 0 | — |

**空闲判定标准**: 显存 < 100 MiB 且利用率 0%

**备注**:
- bjb1-18228 cuda:0 跑 CRM 训练 (580 MiB)，cuda:1/3 被占用
- bjb1-32546 cuda:4,5 各占 ~1.9 GB（有轻量任务）
- bjb2-28827 全部 GPU 占用 1.9-4.7 GB
- cqa1-32758 全部 GPU 占用 2.0-4.9 GB
- bjb2-40593 占用 5.4 GB

**可调度资源: bjb1-32546 有 4 块空闲 4090 可用。**

---
