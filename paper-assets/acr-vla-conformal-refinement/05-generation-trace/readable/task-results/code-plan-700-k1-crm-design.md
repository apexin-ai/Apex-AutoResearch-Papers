# code plan 700 k1 crm design

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_700-k1-crm-design_20260517T132148_result.json`
- **Structured JSON:** [`941ca7ecc8afa53adc78.json`](../../sessions/94/941ca7ecc8afa53adc78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 产出

### 代码文件 (服务器 bjb2-28827)
1. **`/root/acr-vla-conformal-refinement/src/crm_k1_model.py`** - 3 个核心类：
   - `MultiScaleFeatureExtractor`: 通过 forward hooks 从 VLM text_model layers [3,7,11,15] 提取中间特征，验证与 obs_features cosine_sim=1.0
   - `MultiScaleCRM`: 323,102 参数。共享 bottleneck(960->192) + FiLM 调制 + action-conditioned attention + GELU/LayerNorm MLP。支持 multi-scale 和 single-obs fallback
   - `CRMMultiLoss`: L2 + direction cosine + triplet improvement + magnitude regularization

2. **`/root/acr-vla-conformal-refinement/src/train_crm_k1.py`** - 完整训练 pipeline：
   - `--precompute`: K=1 采样 + multi-scale hook 提取，缓存到磁盘
   - `--reuse_k10_cache`: 复用现有 K=10 cache (fallback mode)
   - `--loss_mode multi|mse`: multi-loss vs MSE-only ablation
   - batch_size=512, AdamW+CosineAnnealing, synthetic augmentation

### 设计文档
- Artifact `k1_crm_design.md` 已注册，包含架构图、维度分析、loss 公式、参数对比、训练命令

### 验证结果
- 模型实例化、multi-scale/fallback forward、norm clipping、loss 计算、梯度流全部通过
- Hook 提取在真实 SmolVLA encode_prefix 上验证成功

---
