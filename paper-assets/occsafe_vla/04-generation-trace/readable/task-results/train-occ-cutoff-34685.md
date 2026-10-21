# train occ cutoff 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_occ-cutoff-34685_20260522T062941_result.json`
- **Structured JSON:** [`07de384a7436a935c1b5.json`](../../sessions/07/07de384a7436a935c1b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已正常运行。汇报：

## 结果

**代码改动**：无。`occ_loss_cutoff_step` 参数和 cutoff 逻辑已存在于 `finetune.py:94,1164-1166`。

**实验状态**：

| 实验 | GPU | PID | tmux | seed | 速度 | ETA |
|------|-----|-----|------|------|------|-----|
| cutoff_s0 | cuda:0 | 125522 | cutoff_s0 | 42 | ~1.07 it/s | ~13h (May 23 ~04:00 UTC) |
| cutoff_s1 | cuda:3 | 125672 | cutoff_s1 | 43 | ~1.05 it/s | ~13h (May 23 ~04:00 UTC) |

**初始 metrics**：
- cutoff_s0: step=0, occ_loss=0.1080, action_loss=0.6523
- cutoff_s1: step=0, occ_loss=0.1656, action_loss=0.5391

**GPU 占用**：4 卡全部活跃（cuda:0/3 cutoff，cuda:1/2 depth），各 ~62GB VRAM。

**磁盘**：/root/autodl-tmp 62GB 可用。save_freq=2500 × 50K steps = 20 checkpoints/run，LoRA checkpoints 较小，空间充足。

**Cron 监控**：cutoff_s0 和 cutoff_s1 均已注册，120s 轮询。

**关键参数**：`occ_loss_cutoff_step=35000`，前 35K 步 OCC loss 正常衰减，35K 后 occ_weight 归零。

---
