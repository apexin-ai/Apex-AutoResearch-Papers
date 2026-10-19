# analysis kl sparsity30 s42 v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kl_sparsity30_s42_v2_20260515T211324_result.json`
- **Structured JSON:** [`e43f47769e6d3175d40d.json`](../../sessions/e4/e43f47769e6d3175d40d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE. Here's the analysis summary:

## kl_sparsity30_s42_v2 — NEGATIVE

**核心问题：sparsity 仍然卡在 0.281，与 v1 完全相同，v2 修复无效。**

### 关键指标
| 指标 | 值 |
|------|-----|
| model_level_sparsity | **0.281** (目标 0.3) |
| final_loss | 0.1465 |
| kl_normalized | 0.1465 |
| lambda_sparse | 1000 (hit cap) |
| training_steps | 1000/1000 |
| wall_clock | ~44 min (0.74 GPU-hr) |

### Sparsity 收敛轨迹
- Step 1: 0.406 → Step 130: 0.289 → Step 300: 0.301 (短暂接近目标) → Step 360+: 锁定在 0.281

### 根因分析
Lambda multiplier 在 step 220 就已经 hit cap=1000，之后再无调节能力。Sparsity 从 0.301 滑落到 0.281 时，lambda 已经没有上升空间来施加更强的约束。**lambda_max=1000 这个上限本身就是瓶颈**——两次实验（v1、v2）都卡在同一个 sparsity 值，说明这不是随机波动而是结构性限制。

### 缺失
- **无 PPL 评估**：训练脚本不包含 eval 步骤，没有 true_dense_ppl / predictor_hard_mask_ppl / teal_sparse_ppl
- **W&B 离线**：run 未同步到云端，无法通过 API 查询

### Plan_008 影响
30% sparsity 数据点连续两次失败（v1 killed, v2 negative），需要：
1. 提高 lambda_max（如 5000 或 10000），或
2. 改用更激进的 lambda 增长策略（如指数增长而非 2x），或
3. 检查 sparsity=0.281 是否是模型结构的某种离散边界（如某层全部 on/off 导致 sparsity 量化）

---
