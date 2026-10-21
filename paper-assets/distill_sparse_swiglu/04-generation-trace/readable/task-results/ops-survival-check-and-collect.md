# ops survival check and collect

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_survival-check-and-collect_20260518T162959_result.json`
- **Structured JSON:** [`39a4da0243511dd1dc1b.json`](../../sessions/39/39a4da0243511dd1dc1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

| 实验 | 服务器 | GPU | 状态 | 指标/进度 |
|------|--------|-----|------|-----------|
| c1_ablation_eval_uniform | westd-41718 | 0 | **运行中** | MMLU loglikelihood 14% (8545/58702)，~50 it/s，预计还需 ~20min 完成 MMLU + gsm8k |
| kl_sparsity25_s42 | westd-41718 | 1 | **完成** ✓ | loss=0.158, sparsity=0.230 (target 0.25), 1000/1000 steps, checkpoint saved |
| kl_sparsity35_s42 | westd-34887 | 0 | **运行中** | step 450/1000 (45%), loss~0.19, sparsity~0.34, 预计 ~20min 完成 |
| kl_sparsity45_s42 | westd-34887 | 1 | **运行中** | step 450/1000 (45%), loss~0.28, sparsity~0.43, 预计 ~20min 完成 |

**kl_sparsity25_s42 已更新 registry → DONE/success**，训练指标已录入。checkpoint 在 `checkpoints/kl_sparsity25_s42/predictor_kl_normalized.pt` (145MB)。

注意：kl_sparsity25_s42 实际 sparsity 收敛到 0.23（vs target 0.25），与 30% target 收敛到 ~0.27 的模式一致（均略低于 target）。需要后续跑 benchmark eval 获取 PPL 和 downstream 指标。

---
