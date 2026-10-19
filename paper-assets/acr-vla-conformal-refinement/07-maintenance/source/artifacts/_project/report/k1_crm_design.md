# K=1 Multi-Scale CRM (MSCRM) Architecture Design

## Motivation

K=10 CRM 的核心价值是 uncertainty-based selection (obs_only SR=17.5% vs argmin 12.3%)。K=1 场景下只有一个 action sample，无法做 selection，必须直接改善 correction quality。

关键洞察：当前 CRM 只用 VLM 最终层的 mean-pooled features (960D)。不同 VLM 层编码不同层次的信息：
- 浅层 (Layer 3): 视觉-空间布局，gripper-object 位置关系
- 中层 (Layer 7): 物体身份，交互 affordance
- 深中层 (Layer 11): 任务进度，高层推理
- 深层 (Layer 15): 最终任务表征 (= 当前 obs_features)

## SmolVLA Encoder 结构

```
Vision Model: SmolVLMVisionTransformer
  - 12 layers, hidden_size=768, image 512x512, patch 16x16

Connector: SmolVLMSimpleMLP
  - Linear(12288, 960)  # 16 vision tokens * 768D -> 960D

Text Model (VLM backbone): LlamaModel
  - 16 layers (LlamaDecoderLayer), hidden_size=960
  - Each layer: self_attn (Q:960->960, K:960->320, V:960->320, O:960->960)
  - MLP: gate 960->2560, up 960->2560, down 2560->960

LM Expert: LlamaModel
  - 16 layers, hidden_size=720
  - During encode_prefix, expert stream is None -> VLM 独立处理
```

## Architecture

```
SmolVLA Text Model Layers [3, 7, 11, 15]
     |         |         |         |
     v         v         v         v
  (B,960)  (B,960)  (B,960)  (B,960)    <- hook-based extraction + mean pooling
     |         |         |         |
     +----+----+----+----+
          |
     Per-layer normalization (obs_mean[i], obs_std[i])
          |
     Shared Linear(960, 192)                          <- bottleneck projection
          |
     FiLM: scale[i] * x + shift[i]                   <- layer-specific modulation
          |
     Stack -> (B, 4, 192)
          |
     Action-conditioned attention:
       query = Linear(30, 192)(action_norm)           <- action as query
       attn = softmax(query . features / sqrt(192))
       fused = weighted_sum(features)  -> (B, 192)
          |
     Concat(action_norm, fused) -> (B, 222)
          |
     MLP: Linear(222, 256) -> GELU -> LayerNorm(256)
          -> Linear(256, 256) -> GELU
          -> Linear(256, 30)                          <- zero-init for residual
          |
     eps-clipping: ||delta||_2 <= max_correction_norm
          |
     refined = base_action + delta -> (B, 30)
```

### Fallback Mode
当 multi-scale features 不可用时 (e.g., 复用 K=10 cache)，接受单个 (B, 960) obs_features:
- 跳过 attention fusion，直接 project + FiLM(last layer) -> fused
- 架构参数完全相同，推理路径简化

## Multi-Scale Feature Extraction

通过 forward hooks 在 SmolVLAWrapper.encode_prefix 期间提取中间层特征，不修改任何现有代码。

**关键发现**: encode_prefix 时 inputs_embeds[1] (expert stream) = None，VLM text model 独立处理。hooks 在 SmolVLMWithExpertModel.forward 内部的 layer.input_layernorm 调用时触发。

```python
# Hook 策略:
# Layer N (N < 15): hook on layers[N+1].input_layernorm INPUT -> captures layer N output
# Layer 15: hook on text_model.norm OUTPUT -> captures post-norm final (= obs_features)

extractor = MultiScaleFeatureExtractor(text_model, [3, 7, 11, 15])
with extractor.capture():
    obs_feat, kv, pad_masks = wrapper.encode_prefix(...)
    ms_feats = extractor.get_features(pad_masks)  # list of 4 x (B, 960)
```

**验证结果**: Layer 15 提取结果与 obs_features cosine similarity = 1.000000

## Loss Functions

### 1. L2 Residual Loss (primary, weight=1.0)
```
L_l2 = MSE(refined, expert)
```

### 2. Direction-Aware Cosine Loss (weight=0.1)
```
delta_pred = refined - base_action
delta_true = expert - base_action
L_dir = (1 - cosine_similarity(delta_pred, delta_true)).mean()
```
仅在 ||delta_true|| > 0.01 的样本上计算，避免零向量 cosine 不稳定。

### 3. Triplet Improvement Loss (weight=0.05)
```
L_tri = max(0, margin + ||refined - expert|| - ||vla_action - expert||).mean()
```
margin=0.01。确保 correction 后 action 离 expert 更近。

### 4. Correction Magnitude Regularization (weight=0.01)
```
L_mag = ||delta_pred||^2.mean()
```
防止过度纠正，配合 eps-bound clipping。

### Total
```
L = L_l2 + 0.1 * L_dir + 0.05 * L_tri + 0.01 * L_mag
```

## Parameter Count

| Module           | Parameters |
|-----------------|-----------|
| layer_proj      | 184,512   |
| FiLM (scale+shift) | 1,536  |
| action_query_proj | 5,952   |
| MLP             | 131,102   |
| **Total**       | **323,102** |

vs. 旧 CRM: ~327K params (obs_only mode: 990*256+256*256+256*30)

## 与旧 CRM 对比

| Feature | Old CRM (K=10) | New MSCRM (K=1) |
|---------|---------------|-----------------|
| Input | action(30D) + obs(960D) | action(30D) + 4x obs(960D) |
| Feature fusion | Concat | Action-conditioned attention |
| Activation | ReLU | GELU + LayerNorm |
| Loss | MSE only | MSE + direction + triplet + magnitude |
| Normalization | Global input_mean/std | Per-layer obs_mean/obs_std |
| Params | ~327K | ~323K |
| Use case | Select best from K=10 | Directly correct K=1 |

## Code Files

| File | Path | Description |
|------|------|-------------|
| crm_k1_model.py | `/root/acr-vla-conformal-refinement/src/crm_k1_model.py` | MultiScaleCRM, MultiScaleFeatureExtractor, CRMMultiLoss |
| train_crm_k1.py | `/root/acr-vla-conformal-refinement/src/train_crm_k1.py` | Precompute + training pipeline |

## Training Commands

```bash
# Phase 1: Precompute K=1 features with multi-scale extraction
python train_crm_k1.py --precompute --benchmark object

# Phase 2: Train with multi-loss
python train_crm_k1.py --benchmark object --epochs 50 --batch_size 512

# Quick test with existing K=10 cache (fallback mode)
python train_crm_k1.py --benchmark object --epochs 50 --reuse_k10_cache

# MSE-only ablation
python train_crm_k1.py --benchmark object --epochs 50 --loss_mode mse
```

## Design Decisions

1. **Shared bottleneck vs separate projections**: 4 separate 960->192 projections = 738K params (over budget). Shared projection + FiLM achieves layer-specific representation with 186K params.

2. **Action-conditioned attention vs concat**: Concat of 4x192=768D requires wider MLP. Attention dynamically selects relevant scale based on the current action, more parameter-efficient.

3. **GELU + LayerNorm vs ReLU**: GELU provides smoother gradients for the multi-loss landscape. LayerNorm stabilizes training with the heterogeneous multi-scale inputs (layers 3-11 have mean~-8.5, std~160 vs layer 15 mean~0, std~0.9).

4. **Zero-init last layer**: Standard residual learning trick. At init, CRM outputs base_action unchanged. Gradients initially only flow to last layer but propagate to all layers after first step.
