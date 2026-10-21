# monitor full gpu status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_full-gpu-status_20260517T202038_result.json`
- **Structured JSON:** [`95e199b5d2d211add042.json`](../../sessions/95/95e199b5d2d211add042.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部状态汇总：

```
GPU 0 (CLS v4):   PID 664774 — ALIVE ✓  3920/9784 (40.1%)  running_acc=70.9%  ~6h remaining
GPU 1 (CWM s42):  PID 662946 — ALIVE ✓  1191/9784 (12.2%)  running_acc=58.2%  ~28h remaining
GPU 2 (CLS s123): PID 665019 — ALIVE ✓  3440/9784 (35.2%)  running_acc=74.5%  ~7h remaining
GPU 3 (CWM s123): PID 668680 — ALIVE ✓   846/9784 ( 8.6%)  running_acc=62.6%  ~30h remaining
```

补充信息：
- **CLS s123 旧结果** (seq2048) 已完成：9784/9784, accuracy=82.62%, 文件在 `deepseek_cls_repo_s123_test/`
- **CWM s42** 没有 tmux session，stdout 重定向到 log 文件 `deepseek_cwm_repo_s42_eval.log`，进程正常运行
- **CLS v4/s123 (8192)** 输出文件在完成时才写入，当前无中间文件
- **CWM** 两个 eval 速度慢（batch_size=1, 每样本~13s），预计还需 **28-30 小时**
- **CLS** 两个 eval 速度较快（batch_size=4），预计还需 **6-7 小时**
- 4 张 GPU 利用率正常（53%-100%），内存占用稳定

---
