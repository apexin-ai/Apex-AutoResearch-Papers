# code full trace tail 512

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full_trace_tail_512_20260517T045624_result.json`
- **Structured JSON:** [`b2f3ee31d4d2a7863a54.json`](../../sessions/b2/b2f3ee31d4d2a7863a54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**cuda:0 状态**: 49GB dead memory（无进程），新训练进程已启动会回收。

**数据生成**:
- `full_trace_tail_512_train.jsonl`: 4720 条 (10.6MB)
- `full_trace_tail_512_test.jsonl`: 1190 条 (2.6MB)
- trace 上限 512 tokens，保留尾部（含 `[...trace truncated...]` 标记）

**训练提交**:
- PID: 330357
- GPU: cuda:0
- 444 steps，已开始训练
- 训练完成后自动执行 eval

---
