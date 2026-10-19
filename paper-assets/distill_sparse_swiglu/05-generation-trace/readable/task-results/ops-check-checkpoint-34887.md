# ops check checkpoint 34887

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_checkpoint_34887_20260519T175245_result.json`
- **Structured JSON:** [`3652a4d14c691696d6e4.json`](../../sessions/36/3652a4d14c691696d6e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**Checkpoint**: 存在于 34887，路径 `/root/distill_sparse_swiglu/checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt`，大小 **~223MB** (234,191,583 bytes)。无需 scp。

**34887:1 GPU 状态**: TEAL v3 (PID 115174) **仍在运行**。
- 命令: `benchmark_eval.py --baseline_mode teal_vanilla --allocation uniform --sparsity_target 0.275 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k --exp_id qwen14b_teal275_uniform_eval_v3`
- GPU 1: 61665MiB / 97887MiB，利用率 75%，温度 52°C

**34887:0**: 也在使用中 (PID 126081)，39993MiB / 97887MiB，利用率 100%，温度 75°C。

---
