# ssh post restart status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_post-restart-status-check_20260513T091614_result.json`
- **Structured JSON:** [`00d5849dfa017dc064da.json`](../../sessions/00/00d5849dfa017dc064da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇报

### 1. Home — CLS v5 (PID 2947259)
| 项目 | 状态 |
|------|------|
| 进程 | **ALIVE** — 运行 1h35m，实际训练子进程 PID 2947263 CPU 100% |
| 进度 | **step 589 / 6633**（~9%），刚完成 step 400 checkpoint 保存和 eval |
| GPU | 98% 利用率，19467 MiB / 32607 MiB |
| 最新 loss | step 550: **0.7077**（从 step 50 的 99.12 → step 500 的 0.808 → 0.708，稳步下降） |
| eval_loss | step 400 eval: **0.0761** |
| 速度 | ~6-7 s/it，预计剩余 ~11.5h |

### 2. Seetacloud — CWM v11 (PID 130026)
| 项目 | 状态 |
|------|------|
| 进程 | **ALIVE** — 运行 56m27s，CPU 0%（父进程正常，GPU 在干活） |
| 进度 | **step 8550 / 9335**（~92%），进度条显示 23:43 elapsed |
| GPU | GPU 2: 98% 利用率，29806 MiB / 32607 MiB；其余 3 卡空闲 |
| 最新 loss | step 100: **19.93**（step 50: 29.94 → step 100: 19.93）— 日志只记录到 step 100，后续 loss 未打印，但进度条仍在正常推进 |
| 速度 | ~5-6 it/s，预计剩余 ~2.5 min |

**结论**：两个训练都在正常运行。CWM v11 即将完成（~2-3 分钟内结束），CLS v5 还需约 11 小时。

---
