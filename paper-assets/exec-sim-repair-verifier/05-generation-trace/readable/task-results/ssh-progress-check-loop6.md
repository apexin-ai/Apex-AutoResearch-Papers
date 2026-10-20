# ssh progress check loop6

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_progress-check-loop6_20260513T012651_result.json`
- **Structured JSON:** [`a103b56510b4ace4eac6.json`](../../sessions/a1/a103b56510b4ace4eac6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均正常运行，registry 已更新。

| | CLS v4 (home-1x5090) | CWM v10 (seetacloud-4x5090) |
|---|---|---|
| PID | 2885139 ✓ (elapsed 3:32) | 105205 ✓ (elapsed 1:48, RSS 5.1GB) |
| Step | 1200/6633 (18.1%) | 601/6633 (9.1%) |
| train_loss | 0.5212 | 1.7617 |
| eval_loss | 0.2410 (step 1000) | 0.3435 (step 600) |
| 速度 | ~7s/it | ~8s/it |
| 当前状态 | 正在跑 eval@1200 (1505/4668) | 刚完成 eval@600，继续训练 |
| Checkpoints | — | 400, 500, 600 (最新 09:26 CST) |
| ETA | ~17:00 UTC 5/13 | ~19:30 UTC 5/13 |

CLS eval_loss 趋势平稳（step200=0.070 仍是 best）。CWM loss 从 6.71→1.91→1.76 持续下降，eval_loss 从上次的 0.3294 微升至 0.3435（可能波动）。

---
