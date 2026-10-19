# eval exp004 batch1 and ckpt4000 check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp004-batch1-and-ckpt4000-check_20260520T141446_result.json`
- **Structured JSON:** [`97d2b6300254a932b7bb.json`](../../sessions/97/97d2b6300254a932b7bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四卡全部占用，全部正常启动。

### 汇总

**Part A: exp-003 ckpt-4000 rerun**
- 状态：**运行中**，GPU 0（16.8 GB, 42% util）
- tmux session: `exp-003-eval-ckpt4000`（22:14 启动）
- 模型已加载，正在 eval 362 对数据，预计 ~30 min 内完成
- ckpt 路径: `/root/contrastive_entrain_calib/checkpoints/exp003/checkpoint-4000`

**Part B: exp-004 补充 eval Batch 1** — 3 个 job 全部启动成功

| GPU | Checkpoint | tmux session | PID |
|-----|-----------|-------------|-----|
| 1 | ckpt-1000 | `exp-004-eval-ckpt1000` | 591967 |
| 2 | ckpt-4000 | `exp-004-eval-ckpt4000` | 592042 |
| 3 | ckpt-6000 | `exp-004-eval-ckpt6000` | 592184 |

**GPU 占用确认：**
- GPU 0: 16844 MiB (exp-003 ckpt-4000 eval)
- GPU 1: 17024 MiB (exp-004 ckpt-1000 eval)
- GPU 2: 16152 MiB (exp-004 ckpt-4000 eval)
- GPU 3: 14944 MiB (exp-004 ckpt-6000 eval)

Batch 1 完成后还剩 10 个 checkpoint 待 eval：1500, 2500, 3000, 3500, 4500, 5000, 5500, 6500, 7000, 7500。

---
