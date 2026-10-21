# infra full check westd 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_full-check-westd-10894_20260521T164807_result.json`
- **Structured JSON:** [`565ec9b43b9f2af43121.json`](../../sessions/56/565ec9b43b9f2af43121.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Ablation 状态汇报

**所有 4 个实验均为 RUNNING，约 39% 进度，远未完成。**

| 实验 | GPU | 当前 Step | 进度 | 速度 | 已有 Checkpoint | ETA (完成) |
|------|-----|-----------|------|------|----------------|-----------|
| ablation_occ_detach_s0 | GPU 0 | 19421/50005 | 39% | ~1.08 it/s | 10000_chkpt | ~7.9h |
| ablation_random_occ_s0 | GPU 1 | 19827/50005 | 40% | ~1.08 it/s | 10000_chkpt | ~7.8h |
| ablation_occ_detach_s1 | GPU 2 | 19459/50005 | 39% | ~1.08 it/s | 10000_chkpt | ~7.9h |
| ablation_random_occ_s1 | GPU 3 | 19437/50005 | 39% | ~1.08 it/s | 10000_chkpt | ~7.9h |

**关键信息：**

- **20000_chkpt** 即将保存（各实验距 step 20000 还有 3-9 分钟）
- **50000_chkpt 预计完成时间**：距现在约 **7.8-7.9 小时**（~May 23 凌晨 UTC+8）
- **GPU**：4 卡全占满（80-99% utilization，~62GB 显存），无空闲 GPU 可用于 eval
- **磁盘**：/root/autodl-tmp 111GB/250GB (45%)，空间充足
- **tmux sessions**：4 个 ablation session + 3 个 vanilla session 均存活

原 ETA (00:30-00:45 UTC May 22) 明显偏乐观，实际训练速度 ~1.08 it/s，50005 步总耗时约 12.9 小时。

---
