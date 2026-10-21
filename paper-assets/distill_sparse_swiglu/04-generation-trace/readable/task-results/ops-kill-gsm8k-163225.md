# ops kill gsm8k 163225

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_gsm8k_163225_20260519T175040_result.json`
- **Structured JSON:** [`8a767c0fdd60c9415a5b.json`](../../sessions/8a/8a767c0fdd60c9415a5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 项目 | 状态 |
|------|------|
| **163225 (孤儿进程)** | 已确认杀死，ps 返回空 |
| **GPU 1 显存** | 未完全释放 — 仍占用 32181MiB/97887MiB，被 PID 164335 (python) 占用 |
| **164330 (qwen14b_dense_4task_v2)** | 存活，正在运行 benchmark_eval.py（dense baseline，tasks=wikitext2,arc_challenge,winogrande,mmlu），子进程 PID 164335 在 GPU 1 上 |

GPU 1 上 32GB 显存是 164330 的子进程 164335 在用（qwen14b_dense_4task_v2 评估任务），不是孤儿进程残留。163225 占用的 63GB 显存已释放。GPU 0 上 PID 162205 占用 37GB，利用率 100%，在正常运行。

---
