# ssh post restart training status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_post-restart-training-status_20260513T061633_result.json`
- **Structured JSON:** [`85c75293d97cdfe8e789.json`](../../sessions/85/85c75293d97cdfe8e789.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部收集，汇总如下：

---

## CLS v4 (home-1x5090, sonny@)

| 项目 | 状态 |
|------|------|
| **进程** | PID 2885139 存活，运行 8h21m（注：CMD 列截断显示 `bash -c rm -rf /home/sonny/...`，但训练正常推进，应为启动脚本截断显示） |
| **进度** | step 2600 / 6633 (**39.2%**)，当前正在跑 eval（476/4668 eval steps） |
| **最新 train_loss** | 0.2056 (step 2600) |
| **best_metric** | **0.0701** @ checkpoint-200 |
| **best_checkpoint** | `checkpoints_repo_cls_home/checkpoint-200` |
| **GPU** | 96% 利用率，19465 / 32607 MiB |

**Eval loss 历史：**

| step | eval_loss |
|------|-----------|
| 200 | **0.0701** ← best |
| 400 | 0.2500 |
| 600 | 0.1317 |
| 800 | 0.1462 |
| *(1000-1800)* | *(日志截断，数据在 checkpoint)* |
| 2000 | 0.2492 |
| 2200 | 0.3620 |
| 2400 | 0.1504 |
| 2600 | 0.2466 |

**ETA 估算：** checkpoint-2400→2600 耗时 ~36 min（含 13 min eval），剩余 ~4033 steps + ~20 次 eval → **约 11-12 小时**

---

## CWM v10 (seetacloud-westd-4x5090, root@)

| 项目 | 状态 |
|------|------|
| **进程** | PID 105205 存活，运行 6h37m，`python3 -u train_repo_cwm.p...` |
| **进度** | step 1767 / 6633 (**26.6%**)，实时训练中 ~8.0 s/it |
| **最新 train_loss** | 0.0792 (step 1750) |
| **best_metric** | **0.2975** @ checkpoint-400 |
| **best_checkpoint** | `checkpoints_repo_cwm_v9/checkpoint-400` |
| **GPU** | PID 105205 使用 21058 MiB |

**Eval loss 历史：**

| step | eval_loss |
|------|-----------|
| 100 | 0.4337 |
| 200 | 0.3236 |
| 300 | 0.3228 |
| 400 | **0.2975** ← best |
| 500 | 0.3294 |
| 600 | 0.3435 |
| *(700-1000)* | *(日志截断)* |
| 1100 | 0.3637 |
| 1200 | 0.3500 |
| 1300 | 0.3712 |
| 1400 | 0.3694 |
| 1500 | 0.3732 |
| 1600 | 0.3717 |
| 1700 | 0.3699 |

**ETA 估算：** 剩余 ~4866 steps × 8 s/it + ~49 次 eval × 12.2 min → **约 21 小时**

---

## 关键观察

1. **两个训练都在正常运行**，服务器重启后进程均存活。
2. **CLS eval_loss 震荡严重**（0.07 → 0.36），best 停在极早期 step 200，后续未刷新 best — 可能存在过拟合或 eval 指标选择问题。
3. **CWM eval_loss 自 step 400 起持续上升并平台化在 0.35-0.37**，train_loss 已降到 0.08，典型的过拟合信号。best 同样卡在早期 step 400。
4. 两个实验的 **best checkpoint 都在训练极早期**，当前训练继续跑下去可能不会产生更好的 checkpoint。

---
