# infra verify gpu0 and gpu2 status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-gpu0-and-gpu2-status_20260518T030333_result.json`
- **Structured JSON:** [`ba987f8d6c454bde1500.json`](../../sessions/ba/ba987f8d6c454bde1500.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部状态汇总：

| GPU | 利用率 | 显存 | 任务 | PID | 状态 |
|-----|--------|------|------|-----|------|
| 0 | 99% | 23449/32607 MiB | **CLS v5 retrain** (train_unified.py, seed 42) | 698038 | 正在训练，36/6315 steps (~9.5s/it，预计约16.5h) |
| 1 | 50% | 17519/32607 MiB | **CWM s42 eval** (best checkpoint, test split) | 662946 | 运行中 |
| 2 | 90% | 24565/32607 MiB | **CLS s123 eval** (tmux session 存活) | 665019 | 仍在运行 |
| 3 | 50% | 17519/32607 MiB | **CWM s123 eval** (checkpoint-8844, test split) | 668680 | 运行中 |

关键确认：
- **GPU 0 CLS v5**：进程存活，tmux session `deepseek-cls-repo-v5` 存在，PID 698033/698038 正常运行，当前 36/6315 steps。
- **GPU 1**：CWM s42 eval（**best checkpoint**，即 epoch 3），不是 epoch 2。
- **GPU 2**：CLS s123 eval 仍在运行，GPU 未空闲，暂不启动 CWM s42 epoch 2 eval。
- **GPU 3**：CWM s123 eval（checkpoint-8844）运行中。

所有 4 张卡都在满载工作，无需手动干预。GPU 2 空闲后再启动 CWM s42 epoch 2 eval。

---
