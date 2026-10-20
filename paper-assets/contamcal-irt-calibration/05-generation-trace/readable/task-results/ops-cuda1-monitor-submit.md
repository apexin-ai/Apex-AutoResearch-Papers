# ops cuda1 monitor submit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda1-monitor-submit_20260514T091417_result.json`
- **Structured JSON:** [`3f78364872d225cf47a9.json`](../../sessions/3f/3f78364872d225cf47a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**cuda:1 状态：占用，进程疑似卡死**

- PID 318424 仍存活，状态 `Tl`（stopped），GPU 1 占用 8129 MiB，利用率 0%
- 日志最后写入 16:53:19，已 **20+ 分钟无更新**
- HumanEval 卡在 **31% (51/164)**，很可能某个生成的代码执行陷入死循环

**已完成的 metrics（0.5B raw）：**

| Benchmark | Score |
|-----------|-------|
| MMLU | 0.2302 (3233/14042) |
| GSM8K | 0.1592 (210/1319) |
| ARC-Challenge | 0.2261 (265/1172) |
| HumanEval | 卡住，未完成 |

**建议：** 进程大概率需要 kill 释放 cuda:1。HumanEval 的 code execution 经常因生成代码死循环而 hang。如需保留 HumanEval 结果，可以 kill 后单独重跑 HumanEval（加 timeout per sample）。是否 kill PID 318424？

---
