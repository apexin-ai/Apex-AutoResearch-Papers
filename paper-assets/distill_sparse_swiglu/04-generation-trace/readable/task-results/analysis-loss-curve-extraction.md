# analysis loss curve extraction

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_loss-curve-extraction_20260516T191352_result.json`
- **Structured JSON:** [`f9ada21695231403d37e.json`](../../sessions/f9/f9ada21695231403d37e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。

## 摘要

**已提取 8 个 runs 的训练曲线数据：**

| Run | 数据点 | Final Loss | Final Sparsity |
|-----|--------|-----------|----------------|
| kl_lagrangian_s42/s123/s456 | 101 each | kl_raw ≈ 0.30 | ~0.487 |
| bce_vanilla_s42/s123/s456 | 10 each | bce ≈ 0.638 | ~0.551 |
| bce_isocompute_v2_s42 | 10 | bce = 0.659 | 0.502 |
| bce_comp_staged_s42 | 101 | bce = 0.638 | 0.551 |

**KL vs BCE 对比关键发现：**

- **KL** 将蒸馏 loss 从 1.18 降至 0.30（降幅 74%），sparsity 稳定在 ~0.49（接近目标 0.50）
- **BCE** 仅从 0.663 降至 0.638（降幅 3.7%），停滞在 random baseline (ln2≈0.693) 附近
- BCE saturation 原因：预测值接近 0.5 时 BCE 梯度消失，predictor 无法学到决定性的 activation pattern
- Lagrangian λ 在前 10 步爆升至 cap=1000 后稳定，tau 线性退火 0.999→0.100
- BCE isocompute（Gumbel-sigmoid）更差：sparsity 停在 0.502，几乎没学到东西

**文件位置：**
- 服务器完整数据：`/root/distill_sparse_swiglu/artifacts/training_curves_data.json` (53KB)
- 本地摘要：`artifacts/training_curves_data.json`
- Artifact ID: `art_20260516_d4520a`

---
