# ops kill stale downloads

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_stale_downloads_20260518T220525_result.json`
- **Structured JSON:** [`aa2101171e7d2cc2f8b6.json`](../../sessions/aa/aa2101171e7d2cc2f8b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**汇报：**

- **下载进程：无。** westd-29022 上没有任何模型下载进程（deepseek/huggingface/snapshot 等）。可能已经自行结束或被之前 kill 过了。
- **当前运行的进程**都是本项目的 `eval_math500.py` 评估任务（3 个，分别在 cuda:1/2/3 上），属正常工作负载。
- **HuggingFace 缓存：308MB**，内容仅为评估数据集（MATH-500、gsm8k、humaneval），没有未完成的模型下载文件，无需清理。

---
