# code e1d grpo 1p5b pipeline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e1d_grpo_1p5b_pipeline_20260518T123722_result.json`
- **Structured JSON:** [`d6432131a87e037da891.json`](../../sessions/d6/d6432131a87e037da891.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 SFT 目录都没有 optimizer states 可清理。

**磁盘严重不足**：5.8GB free，需要约 9GB（3 x 3GB）来跑 3 个 1.5B GRPO。必须先清理空间。

可安全删除的候选：
1. **grpo_cka_only_20/model.safetensors (12GB)** — checkpoint-100 里已有相同模型权重，顶层的是冗余副本
2. **grpo_rasp_25 (11GB)** — 已完成的 7B GRPO，如果不再需要

不能删：grpo_cka_only_20/checkpoint-100（E2 需要）

**建议**：删除 grpo_cka_only_20 顶层的 model.safetensors 即可释放 12GB，足够跑完全部 3 个 1.5B GRPO。是否执行？

另外 cuda:0 正在跑 gsm8k eval（~100 samples），需等它完成后才能启动 GRPO。

---
