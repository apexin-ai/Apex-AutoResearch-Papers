# ssh b1 conll eval

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_b1-conll-eval_20260520T122939_result.json`
- **Structured JSON:** [`d242c46ca7fecc656570.json`](../../sessions/d2/d242c46ca7fecc656570.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Merge 完成。但 **GPU 2 当前非空闲** — 正在运行 `bc5cdr_inference.py`（LLaMA-8B zero-shot, PID 210509, 启动于 20:19）。

两个选项：
1. **Kill bc5cdr_inference** 释放 GPU 2，立即开始 CoNLL SCD eval（bc5cdr 推理可以后续重跑）
2. **等待** bc5cdr 完成（估计还需 20-30 分钟）

是否 kill PID 210509 以释放 GPU 2？

---
