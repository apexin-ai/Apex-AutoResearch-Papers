# analysis crm train v3 obs only

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_crm-train-v3-obs-only_20260514T182913_result.json`
- **Structured JSON:** [`6e4d53fcf2f4d3b2b3ab.json`](../../sessions/6e/6e4d53fcf2f4d3b2b3ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报：crm-train-v3-obs-only

### Conclusion: **NEGATIVE**

| 指标 | 值 |
|------|-----|
| best_val_loss | **1.193424** |
| best_epoch | 50（仍在下降，未收敛） |
| final_train_loss | 1.885808 |
| baseline MSE（delta=0） | 1.001596 |
| checkpoint | `/root/autodl-tmp/checkpoints/crm_v3/obs_only/crm_best.pt` |
| log | `~/runs/acr-vla-conformal-refinement/crm-train-v3-obs-only.log` |
| W&B | 无 |

### 与 v2 对比

| | v2 obs_only | v3 obs_only | 倍数 |
|--|-------------|-------------|------|
| val_loss | 0.018 | 1.193 | **66x 退化** |

### 根因分析

训练过程本身正常（50 epochs 完整跑完），但发现了比归一化更根本的问题：

1. **VLA 输出与 expert 动作 scale 严重不匹配**：expert_flat 范围 [-0.94, 0.94]，但 base_action（K 个 VLA 样本的 argmin）范围 [-4.25, 5.77]
2. **max_correction_norm 过小**：平均需要 L2=5.34 的校正，但 delta 被裁剪到 L2≤1.42，模型无法弥补 base_action 和 expert 之间的差距
3. **val_loss=1.19 > baseline_MSE=1.00**：模型的校正反而让预测更差（delta 不足以到达目标，反而引入噪声）
4. **v2 的 0.018 与 v3 的 1.19 差距太大**——说明 v2 可能使用了不同的缓存数据（k_samples scale 不同）或不同的目标表示

**归一化修复（D018）本身逻辑正确**，但暴露了更深层的问题：当前缓存中的 VLA 预测与 expert 动作在 scale 上不一致，残差校正架构在此条件下无法工作。

---
