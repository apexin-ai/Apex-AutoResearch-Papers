# ops cleanup 25068 exp085b exp084

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-25068-exp085b-exp084_20260520T001051_result.json`
- **Structured JSON:** [`0c640c19d28998406b86.json`](../../sessions/0c/0c640c19d28998406b86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**任务 1: PID 295425 — 已 kill。** exp-085b dryrun 进程 (`run_contrastive.py`) 已终止，不再竞争 vLLM API。

**任务 2: exp-084 真实状态：**
- **PID 295377 仍然存活**，运行时间 01:34:20（约1.5小时），正在执行 `run_debate.py`
- **进度：82/200**，有 summary 数据（debate_accuracy=0.2561, sc_accuracy=0.4878）
- **GPU 1 利用率 96%，显存 90677 MiB** — 正在高负载计算
- **结论：exp-084 仍在正常推进中，registry 标记 DONE/failed 是错误的，需要修正。**

---
