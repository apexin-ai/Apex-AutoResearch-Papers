# diag gpu23 cwm eval check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu23-cwm-eval-check_20260519T035009_result.json`
- **Structured JSON:** [`4bb76183cf10cdc4260b.json`](../../sessions/4b/4bb76183cf10cdc4260b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结论：两个进程均正常运行，未卡住。**

| | GPU 2 (PID 734440) | GPU 3 (PID 668680) |
|---|---|---|
| 实验 | D131-cwm-s42-epoch3-seq2048 | deepseek-cwm-repo-s123 |
| 已运行 | ~14h | ~34h |
| 进度 | 4576/9784 (46.7%) | 9632/9784 (98.4%) |
| running_acc | 65.7% | — (无 eval.log) |
| 速率 | ~13s/sample | ~12.7s/sample |
| GPU util | 53% | 50% |
| 最后输出 | 11:50:41 (刚刚) | 11:50 (刚刚) |
| **预估剩余** | **~18.8h** | **~32min** |

GPU 3 即将完成。GPU 2 还需大约 19 小时，预计明天早上 ~6:30 结束。两个进程的 output 文件持续写入，step 计数器稳定递增，GPU 利用率正常，无卡住迹象。

---
