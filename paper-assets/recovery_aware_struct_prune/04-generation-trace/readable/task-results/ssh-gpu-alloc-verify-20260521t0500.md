# ssh gpu alloc verify 20260521T0500

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_alloc_verify_20260521T0500_20260521T044542_result.json`
- **Structured JSON:** [`43a49c41e5c9b62da7e6.json`](../../sessions/43/43a49c41e5c9b62da7e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

| # | 任务 | 结果 |
|---|------|------|
| 1 | eval_gsm8k_grpo_cka_only_25_v2 | 原进程 320735 **路径错误**（缺 `/checkpoint-100`）→ 已 kill → 重启 **PID=321540**，model_path 已修正为 `.../grpo_cka_only_25/checkpoint-100`，cuda:2 |
| 2 | eval_gsm8k_grpo_random_20 | **PID=321338**，cuda:0 |
| 3 | RASP seed456 模型完整性 | **加载失败** — `RuntimeError: ignore_mismatched_sizes=False`，checkpoint 权重与模型结构 size mismatch。未启动 eval |

---
