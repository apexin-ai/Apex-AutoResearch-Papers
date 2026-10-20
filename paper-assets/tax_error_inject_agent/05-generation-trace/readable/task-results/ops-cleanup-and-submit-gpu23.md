# ops cleanup and submit gpu23

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-and-submit-gpu23_20260515T205645_result.json`
- **Structured JSON:** [`814f53099a6b16760e09.json`](../../sessions/81/814f53099a6b16760e09.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 结果

**无需清理和重新提交。** 两个实验实际上已成功启动并在运行中：

| 实验 | GPU | PID | 运行时间 | 状态 |
|------|-----|-----|---------|------|
| v4-taxei-fixed-inject10-s1-eval-r2 | cuda:2 | 196323 | ~3m | eval/recovery.py 运行中 |
| v4-random-fixed-inject10-s7 | cuda:3 | 196760 | ~3m | swift sft 训练中 |

"duplicate session" 错误是因为之前的提交已经成功创建了 tmux session，再次提交时检测到同名 session 所以报错。4 张 GPU 全部在用，registry spec 已补充完毕。

---
