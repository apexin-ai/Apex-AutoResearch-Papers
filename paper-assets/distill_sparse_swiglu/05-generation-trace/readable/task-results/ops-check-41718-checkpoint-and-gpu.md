# ops check 41718 checkpoint and gpu

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-41718-checkpoint-and-gpu_20260518T175921_result.json`
- **Structured JSON:** [`e15e4c9939c84c5d58dd.json`](../../sessions/e1/e15e4c9939c84c5d58dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| 项目 | 状态 |
|------|------|
| **mvp_kl_norm_v2_s123 checkpoint** | **Y** — `/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s123/predictor_kl_normalized.pt`，145 MB |
| **cuda:0 空闲** | **Y** — 0% 利用率，0 MiB 显存占用 |
| **cuda:1 空闲** | **Y** — 0% 利用率，0 MiB 显存占用 |
| **25% checkpoint (kl_sparsity25_s42)** | **Y** — 存在，`predictor_kl_normalized.pt` 145 MB |
| **40% checkpoint (kl_sparsity40_s42)** | **N** — 不存在 |

**完整 checkpoint 目录列表（14个）：**
- `bce_30pct_s42`
- `c1_ablation_bce_kl_targets_s123`
- `c1_ablation_bce_kl_targets_s42`
- `kl_comp_30pct_s123`
- `kl_comp_30pct_s42`
- `kl_comp_30pct_s456`
- `kl_comp_50pct_s42`
- `kl_sparsity25_s123`
- `kl_sparsity25_s42`
- `kl_sparsity30_s123`
- `kl_sparsity30_s42_v3`
- `kl_sparsity30_s456`
- `mvp_kl_norm_v2_s123`
- `mvp_kl_norm_v2_s42`

两块 RTX PRO 6000 Blackwell (98 GB each) 完全空闲，随时可用。

---
