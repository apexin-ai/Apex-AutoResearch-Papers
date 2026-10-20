# infra post restart status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_post-restart-status_20260518T125845_result.json`
- **Structured JSON:** [`11acffe234a04f5cfb7e.json`](../../sessions/11/11acffe234a04f5cfb7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 任务 | 进度 | running_acc | 利用率 | 显存 |
|-----|------|------|-------------|--------|------|
| 0 | CLS v5 retrain | **3633/6315** (57%) | eval_loss=0.0886 (epoch 1 刚完成) | 99% | 24861 MiB |
| 1 | CWM s42 epoch 3 eval | **5963/9784** (61%) | 56.4% | 50% | 17699 MiB |
| 2 | CWM s42 epoch 2 eval (D124) | **2798/9784** (29%) | 66.9% | 57% | 17851 MiB |
| 3 | CWM s123 eval | **5562/9784** (57%) | 61.3% | 49% | 17699 MiB |

四张卡全在跑，GPU 0 的 CLS v5 训练刚过 epoch 1 eval checkpoint（eval_loss 0.0886），正在继续 epoch 2。三个 CWM eval 任务正常推进中。

---
