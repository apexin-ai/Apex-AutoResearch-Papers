# code bench mistral prep

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bench_mistral_prep_20260516T050300_result.json`
- **Structured JSON:** [`0c6cafe03a0d55a3d7de.json`](../../sessions/0c/0c6cafe03a0d55a3d7de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

预验证完成。9/10 项通过，1 项等待中：

**全部就绪**：checkpoint (145MB)、base model (3 shards)、架构兼容（Mistral 用相同 gate_proj/up_proj 接口）、benchmark_eval.py 参数齐全、few-shot 硬编码正确、lm-eval 已装。

**唯一阻塞**：cuda:1 被 bce_isocompute_v3_s42 占用。

**需确认一点**：Registry 中已有的 PENDING 条目用的是 `--sparsity_mode per_token`，但本次任务要求 `teal_global + global_topk`。提交前需决定用哪种模式。推荐命令已写入 artifact `bench_mistral_kl50_ready.md`。

---
