# analysis lambda sparsity curves

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lambda-sparsity-curves_20260516T193855_result.json`
- **Structured JSON:** [`e49dc07792633380bc73.json`](../../sessions/e4/e49dc07792633380bc73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

提取完成。

**服务器产出**: `/root/distill_sparse_swiglu/artifacts/lambda_sparsity_curves.json` (42KB, 4 个 run 的完整曲线数据)

**摘要**:

| Run | Target | Lambda 终值 | Sparsity 终值 | 收敛 step | KL 终值 |
|-----|--------|------------|--------------|----------|---------|
| 30% | 0.3 | 5000 (cap) | 0.285 | ~110 | 0.165 |
| 40% | 0.4 | 625 | 0.398 | ~1 | 0.262 |
| 50% | 0.5 | 8 | 0.504 | ~80 | 0.641 |
| 70% | 0.7 | 1000 (cap) | 0.688 | ~40 | 0.609 |

**关键发现**:
- Lambda 大小反映目标难度：50% 最容易（lambda=8，gate 初始值已接近），30% 最难（lambda=5000 饱和）
- 所有 target 在 ~100 步内收敛到 ±0.03 范围
- Tau 退火（1.0→0.1）导致后期 loss 轻微回升——mask 更 binary，KL 增大

**限制**：50% run 只有 200 步（quicktest），`mvp_kl_norm_v2_s42` 的 wandb 数据不在当前服务器上。本地摘要见 `artifacts/lambda_sparsity_curves_summary.md`。

---
