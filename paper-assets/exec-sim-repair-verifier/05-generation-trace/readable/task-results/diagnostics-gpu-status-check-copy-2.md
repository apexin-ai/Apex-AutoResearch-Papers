# diagnostics gpu status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostics_gpu-status-check_20260517T224126_result.json`
- **Structured JSON:** [`fa290ec1d4eb4e6d2942.json`](../../sessions/fa/fa290ec1d4eb4e6d2942.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入。总结：

**4x5090 全部满载，4 个 eval 任务正常运行：**

| GPU | 任务 | 进度 | 准确率 | 预计完成 |
|-----|------|------|--------|----------|
| 0 | CLS v4 (seq8192) | 65% | 71.1% | 今天 ~10:30 |
| 1 | CWM s42 (test) | 19% | 57.7% | 明天 ~09:00 |
| 2 | CLS s123 (seq8192) | 57% | 74.9% | 今天 ~11:10 |
| 3 | CWM s123 (test) | 16% | 62.1% | 明天 ~10:00 |

**home-1x5090 完全空闲**，GPU 无负载。有一个 `eval_re_repair.py` 进程从 5/16 开始挂着，疑似已完成但未退出。

关键发现：CLS s123 (74.9%) 显著优于 CLS v4 (71.1%)；CWM 两个 eval 因逐条生成，还需约 26-27 小时才能跑完。

---
