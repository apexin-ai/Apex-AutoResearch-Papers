# check eval progress round3

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-progress-round3_20260522T104758_result.json`
- **Structured JSON:** [`449fa99819b37ed0a987.json`](../../sessions/44/449fa99819b37ed0a987.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 任务 | 进度 | Running Acc | ETA |
|-----|------|------|-------------|-----|
| 0 | Qwen CWM s123 | 9436/9784 (**96.4%**) | 67.5% (6365/9436) | ~30 min |
| 1 | DS CWM s123 1epoch | 6592/9784 (**67.4%**) | 75.6% (4986/6592) | ~4.1h |
| 2 | DS CWM s123 e3 | 9012/9784 (**92.1%**) | 57.3% (5160/9012) | ~1.0h |
| 3 | Qwen CWM s456 | 8652/9784 (**88.4%**) | 66.9% (5785/8652) | ~1.7h |

4 个进程全部存活（100% CPU）。注意：

- **DS 1epoch (75.6%)** acc 显著高于 **DS e3 (57.3%)**，e3 checkpoint 可能 overfit
- GPU 1 的 1epoch eval 用的是 checkpoint-4209，GPU 2 的 e3 eval 用的是 checkpoint-12627
- Qwen s123 最快完成，预计 ~30 分钟内跑完

---
