# ops post restart status check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post-restart-status-check_20260518T162647_result.json`
- **Structured JSON:** [`8284095fd949b1e3d4dd.json`](../../sessions/82/8284095fd949b1e3d4dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. All 4 experiments confirmed alive and set to RUNNING.

| 实验 | 服务器 | GPU | 状态 | 指标/进度 |
|------|--------|-----|------|-----------|
| c1_ablation_eval_uniform | westd-41718 | 0 | 运行中 | MMLU loglikelihood 321/58702 (~0.5%), 还在评估中 |
| kl_sparsity25_s42 | westd-41718 | 1 | 运行中 | Step 950/1000, loss=0.236, sparsity=0.227, 即将完成 |
| kl_sparsity35_s42 | westd-34887 | 0 | 运行中 | Step 360/1000, loss=0.227, sparsity=0.355 |
| kl_sparsity45_s42 | westd-34887 | 1 | 运行中 | Step 360/1000, loss=0.305, sparsity=0.449 |

要点：
- **kl_sparsity25_s42** 在 step 950/1000，约 5-10 分钟内完成
- **c1_ablation_eval_uniform** 正在跑 MMLU（58702 个 loglikelihood requests），GPU 0 显存占用 44.8 GiB 但 util 0%（可能在 CPU tokenization 阶段），预计还需较长时间
- **westd-34887** 两个训练都在 step 360/1000（~36%），预计还需 ~25 分钟

---
