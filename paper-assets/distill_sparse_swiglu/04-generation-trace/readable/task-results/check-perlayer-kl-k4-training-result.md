# check perlayer kl k4 training result

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_perlayer_kl_k4_training_result_20260522T113013_result.json`
- **Structured JSON:** [`bf6431abd1b27c057390.json`](../../sessions/bf/bf6431abd1b27c057390.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**perlayer_kl_k4_s42 训练成功完成。** Registry 已更新为 DONE/success，无活跃 cron 需要删除。

**最终 metrics：**
| 指标 | 值 |
|------|-----|
| avg_kl | 0.0447 |
| final_kl (step 2700) | 0.0547 |
| final_sparsity | 28.2% |
| final_loss | 0.0913 |
| constraint_loss | 0.0366 |
| total_steps | 2700/2700 |
| wall_time | 5015s (~83.6 min) |

**Checkpoint：** `/root/distill_sparse_swiglu/checkpoints/perlayer_kl_k4_s42/predictor_perlayer_kl_k4.pt` (152MB)

值得注意：Layer 20 的 final_lambda 仅 0.01（几乎没有 sparsity 压力），而大多数层 lambda 达到了上限 5000。这说明 Layer 20 的 sparsity 本身就容易满足约束，或者其 KL 特别敏感导致 lambda 被反复下调。

---
