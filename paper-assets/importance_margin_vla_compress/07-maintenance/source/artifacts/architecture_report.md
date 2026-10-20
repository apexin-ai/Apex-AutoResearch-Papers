# SmolVLA Architecture & ACIS Integration Report

## 1. SmolVLA Architecture Overview

### 1.1 Visual Encoder

**Encoder**: SigLIP vision transformer (`smolvlm_vision`)

| Parameter | Value |
|-----------|-------|
| hidden_size | 768 |
| image_size | 512 |
| patch_size | 16 |
| num_attention_heads | 12 |
| Patches per image | (512/16)² = **1024** |

**Raw output shape**: `(B, 1024, 768)`

**Pixel Shuffle + Projection** (`SmolVLMConnector`):
- `scale_factor = 4` → sequence reduction 16x: 1024 → **64 tokens**
- Channel increase 16x: 768 → 768×16 = 12288
- `SmolVLMSimpleMLP`: `nn.Linear(12288, 960, bias=False)`

**Final visual token shape per image**: `(B, 64, 960)`

```python
# transformers/models/smolvlm/modeling_smolvlm.py
class SmolVLMSimpleMLP(nn.Module):
    def __init__(self, config):
        input_size = config.vision_config.hidden_size * (config.scale_factor**2)  # 12288
        output_size = config.text_config.hidden_size  # 960
        self.proj = nn.Linear(input_size, output_size, bias=False)

class SmolVLMConnector(nn.Module):
    def __init__(self, config):
        self.scale_factor = config.scale_factor  # 4
        self.modality_projection = SmolVLMSimpleMLP(config)

    def pixel_shuffle(self, x, scale_factor=2):
        bsz, seq, embed_dim = x.size()
        height = width = int(seq**0.5)  # 32
        # Rearrange spatial → channels, reducing seq by scale_factor²
        ...
        return x  # (B, 64, 12288)

    def forward(self, image_hidden_states):
        image_hidden_states = self.pixel_shuffle(image_hidden_states, self.scale_factor)
        image_hidden_states = self.modality_projection(image_hidden_states)
        return image_hidden_states  # (B, 64, 960)
```

**Multi-camera input**: Multiple camera views supported. Each image wrapped with special tokens (`fake_image_token`, `global_image_token`). LIBERO uses 2 cameras (agentview + wrist).

```python
# SmolVLMWithExpertModel
def embed_image(self, image: torch.Tensor):
    image_hidden_states = self.get_vlm_model().vision_model(
        pixel_values=image.to(dtype=self.get_vlm_model().vision_model.dtype),
        patch_attention_mask=None,
    ).last_hidden_state                                    # (B, 1024, 768)
    image_hidden_states = self.get_vlm_model().connector(image_hidden_states)
    return image_hidden_states                             # (B, 64, 960)
```

### 1.2 Language Model / Backbone

**LLM**: SmolLM2 (Llama-architecture variant, `VLlama3ForCausalLM`)

| Parameter | Value |
|-----------|-------|
| hidden_size | **960** |
| num_hidden_layers | 32 (full); SmolVLA uses **16** (`num_vlm_layers`) |
| num_attention_heads | 15 |
| num_key_value_heads | 5 (GQA) |
| head_dim | 64 |
| intermediate_size | 2560 |
| max_position_embeddings | 8192 |
| rope_theta | 100000 |

**Input embedding dimension**: **960**

**Prefix construction** (in `embed_prefix()`):
```
[img_start_tokens] + [64 visual tokens] + [img_end_token]   × num_cameras
+ [language tokens]  (tokenizer_max_length=48)
+ [state token]      (nn.Linear(32, 960) from proprioceptive state)
```

All embeddings scaled by `√960` before concatenation. Attention: bidirectional for image+language tokens, causal for state token.

### 1.3 Action Head (Expert)

**Architecture**: Flow-Matching Transformer with interleaved cross-attention and self-attention.

**Class**: `SmolVLMWithExpertModel.lm_expert` — separate Llama-architecture transformer

| Parameter | Value |
|-----------|-------|
| expert_hidden_size | int(960 × 0.75) = **720** |
| intermediate_size | **1792** |
| num_expert_layers | **16** (same as num_vlm_layers) |
| self_attn_every_n_layers | 2 |

**Layer interleaving pattern**:
- Even layers (0, 2, 4, ...): **self-attention** (prefix + suffix tokens concatenated)
- Odd layers (1, 3, 5, ...): **cross-attention** (expert Q attends to VLM K,V)

Cross-attention K,V project from VLM dim (320 = 5×64) to expert dim:
```python
self.lm_expert.layers[layer_idx].self_attn.k_proj = nn.Linear(320, ..., bias=False)
self.lm_expert.layers[layer_idx].self_attn.v_proj = nn.Linear(320, ..., bias=False)
```

**Action embedding** (in `embed_suffix()`):
```python
self.action_in_proj  = nn.Linear(32, 720)    # noisy actions → expert dim
self.action_out_proj = nn.Linear(720, 32)    # expert output → action dim
self.action_time_mlp_in  = nn.Linear(1440, 720)  # concat(action_emb, time_emb) → expert dim
self.action_time_mlp_out = nn.Linear(720, 720)

# Forward:
action_emb = self.action_in_proj(noisy_actions)            # (B, 50, 720)
time_emb = sinusoidal(timestep, dim=720)                   # (B, 1, 720) → expand to (B, 50, 720)
action_time_emb = cat([action_emb, time_emb], dim=2)       # (B, 50, 1440)
action_time_emb = silu(self.action_time_mlp_in(action_time_emb))  # (B, 50, 720)
action_time_emb = self.action_time_mlp_out(action_time_emb)       # (B, 50, 720)
```

**Output**: Continuous, `chunk_size=50` steps, `max_action_dim=32` (padded; LIBERO actual: 7D = 6D EEF delta + 1D gripper).

## 2. Forward Pass Data Flow

### 2.1 Training (`VLAFlowMatching.forward`)

```
Input: images, lang_tokens, state, actions

1. Sample noise ~ N(0,1),  shape (B, 50, 32)
2. Sample time ~ Beta(1.5, 1.0) * 0.999 + 0.001
3. x_t = time * noise + (1 - time) * actions        # noisy interpolation
4. u_t = noise - actions                             # target velocity field

5. embed_prefix(images, lang_tokens, state):
   a. vision_model(images) → (B, 1024, 768)         # SigLIP
   b. connector(·) → (B, 64, 960)                   # pixel shuffle + projection
   c. Concat: [img_special + 64_vis + img_end] × cameras + lang_emb + state_emb
   → prefix_embs: (B, prefix_len, 960)

6. embed_suffix(x_t, time):
   a. action_in_proj(x_t) → (B, 50, 720)
   b. sinusoidal time embedding → (B, 50, 720)
   c. MLP(cat(action, time)) → (B, 50, 720)
   → suffix_embs: (B, 50, 720)

7. Construct 2D attention mask + position_ids

8. vlm_with_expert.forward([prefix_embs, suffix_embs]):
   For each layer i in 0..15:
     if i % 2 == 0:  # self-attention
       concat(prefix, suffix) → joint self-attention → split back
     else:            # cross-attention
       VLM processes prefix → KV
       Expert Q attends to VLM KV
   → (prefix_out, suffix_out)

9. suffix_out = suffix_out[:, -50:]                  # last chunk_size tokens
10. v_t = action_out_proj(suffix_out)                # (B, 50, 32)
11. loss = F.mse_loss(u_t, v_t, reduction="none")    # masked by actions_is_pad
```

### 2.2 Inference (`VLAFlowMatching.sample_actions`)

```
1. Encode prefix once → cache KV
2. x_t = noise ~ N(0,1)
3. For step in range(num_steps=10):
     time = 1.0 - step/10
     v_t = denoise_step(x_t, time, cached_KV)
     x_t = x_t + (-1/10) * v_t       # Euler integration
4. Return x_t as predicted actions
```

KV-caching: prefix encoded once, denoising steps only process suffix with cross-attention to cached prefix KV.

## 3. Key Classes and File Paths

### LeRobot repo (`huggingface/lerobot`)

| Class | File |
|-------|------|
| `SmolVLAPolicy` | `lerobot/policies/smolvla/modeling_smolvla.py` |
| `SmolVLAConfig` | `lerobot/policies/smolvla/configuration_smolvla.py` |
| `VLAFlowMatching` | `lerobot/policies/smolvla/modeling_smolvla.py` |
| `SmolVLMWithExpertModel` | `lerobot/policies/smolvla/smolvlm_with_expert.py` |

### Transformers repo (`huggingface/transformers`)

| Class | File |
|-------|------|
| `SmolVLMForConditionalGeneration` | `transformers/models/smolvlm/modeling_smolvlm.py` |
| `SmolVLMConnector` | `transformers/models/smolvlm/modeling_smolvlm.py` |
| `SmolVLMSimpleMLP` | `transformers/models/smolvlm/modeling_smolvlm.py` |
| `SmolVLMVisionTransformer` (SigLIP) | `transformers/models/smolvlm/modeling_smolvlm.py` |

### Training

| Item | Detail |
|------|--------|
| Entry point | `lerobot/scripts/lerobot_train.py` → `train(cfg: TrainPipelineConfig)` |
| CLI | `lerobot-train` |
| Loss | MSE: `F.mse_loss(u_t, v_t)` where u_t = noise - actions |
| Time sampling | Beta(α=1.5, β=1.0) scaled to [0.001, 1.0] |
| Optimizer | AdamW, lr=1e-4, betas=(0.9, 0.95), weight_decay=1e-10 |
| Scheduler | Cosine decay, warmup=1000, decay_steps=30000, decay_lr=2.5e-6 |
| Grad clip | 10.0 |

## 4. LoRA Configuration

Default targets (`_get_default_peft_targets`):
```python
target_modules = r"(model\.vlm_with_expert\.lm_expert\..*\.(q|v)_proj|model\.(state_proj|action_in_proj|action_out_proj|action_time_mlp_in|action_time_mlp_out))"
```

Targets:
- All **Q and V projections** in the expert transformer
- **state_proj**, **action_in_proj**, **action_out_proj**, **action_time_mlp_in**, **action_time_mlp_out**

Default training mode: `train_expert_only=True`, `freeze_vision_encoder=True`, `train_state_proj=True`. VLM backbone frozen.

## 5. LIBERO Dataset

**HuggingFace repo**: `HuggingFaceVLA/libero`

| Field | Shape / Type |
|-------|-------------|
| `observation.state` | 8D (EEF pos 3D + axis-angle 3D + gripper qpos 2D) |
| `observation.images.image` | agentview camera, HWC uint8 |
| `observation.images.image2` | wrist camera, HWC uint8 |
| actions | 7D (6D EEF delta + 1D gripper), padded to 32D internally |
| action range | Box(-1, 1, shape=(7,)) |

**Data format**: LeRobotDataset v3.0 — chunked Parquet (tabular) + MP4 (video frames).

**Loading**: `make_dataset(cfg)` creates `LeRobotDataset` from Hub repo_id.

**Training command**:
```bash
lerobot-train \
  --policy.type=smolvla \
  --policy.load_vlm_weights=true \
  --dataset.repo_id=HuggingFaceVLA/libero \
  --env.type=libero \
  --env.task=libero_10 \
  --steps=100000 \
  --batch_size=4
```

## 6. ACIS Insertion Point Analysis

### 6.1 Existing Compression

SmolVLA already has:
- **Pixel shuffle**: 1024 → 64 tokens (16x spatial reduction)
- **VLM layer skipping**: uses 16 of 32 layers

No dynamic token pruning exists in the codebase.

### 6.2 ACIS Cross-Attention Module: `s_i = CrossAttn(a_query, v_i)`

#### Where to get `v_i` (visual tokens)

**Option A — Post-connector (recommended)**:
- Location: output of `SmolVLMConnector.forward()` in `embed_image()`
- Shape: `(B, 64, 960)` per camera
- Advantage: already in LLM embedding space (dim=960), semantically rich after SigLIP + projection
- These are the tokens that enter the prefix embeddings

**Option B — Post-VLM-encoding**:
- Location: after VLM prefix forward pass (the cached KV states)
- Shape: `(B, prefix_len, num_kv_heads, head_dim)` per layer
- Advantage: contextualized by language tokens via self-attention
- Disadvantage: entangled with non-visual tokens, need to extract visual positions

**Recommendation: Option A** — cleaner, shape is known, tokens are identifiable.

#### Where to get `a_query` (action conditioning)

**Option A — From `embed_suffix()` output (recommended)**:
- Location: after `action_time_mlp_out` in `embed_suffix()`
- Shape: `(B, chunk_size, 720)` — need projection to match v_i dim
- Contains action + time information, semantically represents "what action is being predicted"
- Available before the expert transformer processes it

**Option B — From expert intermediate layer**:
- Location: output of an early expert layer (e.g., layer 2 or 4)
- Shape: `(B, chunk_size, 720)`
- Advantage: richer representation after some self/cross-attention
- Disadvantage: creates a circular dependency (expert output depends on prefix, but ACIS modifies prefix based on expert)

**Option C — Learnable query (simplest)**:
- `a_query = nn.Parameter(torch.randn(1, num_queries, 960))`
- No dependency on actual actions during forward pass
- Trained end-to-end to predict importance

**Recommendation: Option A** for training (action-conditioned), **Option C** as simpler baseline.

#### Insertion Point in Code

```python
# In SmolVLMWithExpertModel or VLAFlowMatching

# STEP 1: Get visual tokens (before prefix assembly)
vis_tokens = self.embed_image(images)          # (B, 64, 960) per camera
# → all cameras: (B, num_cameras * 64, 960)

# STEP 2: Get action query
suffix_embs = self.embed_suffix(x_t, time)     # (B, 50, 720)
a_query = self.acis_query_proj(suffix_embs)     # (B, 50, 960) or pool to (B, 1, 960)

# STEP 3: ACIS cross-attention
# s_i = CrossAttn(a_query, v_i)
importance_scores = self.acis_module(
    query=a_query,                              # (B, Q, 960)
    key=vis_tokens,                             # (B, N_vis, 960)
    value=vis_tokens                            # (B, N_vis, 960)
)                                               # → (B, N_vis) scores

# STEP 4: Soft top-k selection
soft_mask = differentiable_topk(importance_scores, k=k)  # (B, N_vis)

# STEP 5: Apply mask to visual tokens
vis_tokens_pruned = vis_tokens * soft_mask.unsqueeze(-1)  # soft weighting
# OR: select top-k indices for hard pruning

# STEP 6: Continue with prefix assembly using pruned tokens
prefix_embs = self.embed_prefix_with_pruned_vis(vis_tokens_pruned, lang, state)
```

#### Specific Code Modifications

**File**: `lerobot/policies/smolvla/smolvlm_with_expert.py`

1. Add ACIS module to `SmolVLMWithExpertModel.__init__()`:
```python
self.acis_query_proj = nn.Linear(720, 960)  # expert dim → VLM dim
self.acis_cross_attn = nn.MultiheadAttention(
    embed_dim=960, num_heads=8, kdim=960, vdim=960, batch_first=True
)
self.acis_score_head = nn.Linear(960, 1)  # output per-token score
```

2. Modify forward flow in `VLAFlowMatching.forward()` (in `modeling_smolvla.py`):
   - After `embed_image()` and `embed_suffix()`, compute ACIS scores
   - Apply soft top-k mask
   - Rebuild prefix with masked visual tokens

3. Add ACIS modules to LoRA target regex:
```python
target_modules = r"(...|model\.acis_.*)"
```

### 6.3 Forward Pass Modification Summary

```
Original:  images → SigLIP → connector → embed_prefix → VLM+Expert → loss
Modified:  images → SigLIP → connector → [ACIS scoring → soft top-k] → embed_prefix → VLM+Expert → loss + IMM_loss
                                              ↑
                                     action query from embed_suffix()
```

### 6.4 IMM Loss Integration

The IMM loss adds to the existing flow matching MSE loss:

```python
# Original loss
loss_fm = F.mse_loss(u_t, v_t, reduction="none")  # flow matching

# IMM auxiliary losses (computed from ACIS scores)
loss_margin = margin_loss(importance_scores, kept_mask, pruned_mask, margin=δ)
loss_calibration = calibration_loss(importance_scores, reconstruction_error)

# Total
loss = loss_fm + λ_margin * loss_margin + λ_cal * loss_calibration
```

## 7. Differentiable Soft Top-K: Method Comparison

### 7.1 Methods Surveyed

#### Sigmoid + Implicit Differentiation (Thomas Ahle)

Binary-search for shift `t` such that `Σ σ(x_i + t) = k`, return `σ(x_i + t)`. Backward via implicit differentiation: `J = diag(v) - vv^T/‖v‖₁`.

- **Impl**: [gist, 20 lines](https://gist.github.com/thomasahle/4c1e85e5842d01b007a8d10f5fed3a18), zero deps
- **Gradient**: Exact Jacobian, deterministic, zero variance
- **Complexity**: O(n × B) forward (B≈64 binary search steps), O(n) backward
- **Constraint**: Σp_i = k **exactly** satisfied
- **Issues**: Binary search not maximally GPU-efficient; elements near threshold get soft (ambiguous) values

#### DFTopK (arXiv Oct 2025)

Sigmoid on scores shifted by midpoint of k-th and (k+1)-th largest: `σ((x - (x[k]+x[k+1])/2) / τ)`.

- **Impl**: [github.com/zhangzhen97/DFTOPK](https://github.com/zhangzhen97/DFTOPK)
- **Gradient**: Deterministic, localized uncertainty at boundary
- **Complexity**: O(n) average (Introselect)
- **Constraint**: Σp_i ≈ k (approximate)
- **Issues**: τ requires tuning

#### LapSum (ICML 2025)

Differentiable top-k via CDF of sum of Laplace distributions. Threshold `b` found such that `Σ Lap_α(b - r_i) = w`.

- **Impl**: [github.com/gmum/LapSum](https://github.com/gmum/LapSum), `pip install lapsum`
- **Gradient**: Exact, deterministic, zero variance
- **Complexity**: O(n log n), O(n) backward
- **Constraint**: Exact
- **Issues**: α hyperparameter; requires library

#### Gumbel Top-k (Subset Sampling)

Iterative Gumbel-perturbed softmax k times with masking. Used in **LightVLA**.

- **Impl**: ~20 lines; UvA DL Notebooks `SubsetOperator`
- **Gradient**: Stochastic (Gumbel noise), reparameterizable, STE for hard mode
- **Complexity**: O(n × k) — k sequential softmax ops
- **Constraint**: Exact k elements (hard mode)
- **Issues**: k=150 means 150 sequential ops; variance from noise

#### SOFT (Optimal Transport, NeurIPS 2020)

Top-k as Entropic OT via Sinkhorn iterations.

- **Impl**: ~120 lines gist, no pip package
- **Gradient**: Biased (controlled by ε)
- **Complexity**: O(n × k × T), T=50-200 Sinkhorn iterations
- **Constraint**: Exact (doubly stochastic)
- **Issues**: NaN instability for small ε; slow

#### NeuralSort / SoftSort

Full n×n permutation matrix relaxation. O(n²) time and memory.

- **Issues**: Produces full permutation matrix — overkill for top-k; n=500 → 250K entries

#### Temperature Sigmoid (baseline)

`σ(α · (s_i - kth_percentile) / τ)` with τ annealing.

- **Impl**: 5 lines, zero deps
- **Gradient**: Biased; no gradient through `kthvalue`
- **Complexity**: O(n log n) or O(n) with `torch.kthvalue`
- **Issues**: Σp_i ≠ k; gradient vanishing at low τ

### 7.2 Comparison Table

| Method | Complexity | Gradient | Exact Σ=k | Variance | Code | VLA Proven |
|--------|-----------|----------|-----------|----------|------|------------|
| **Sigmoid+ImplDiff** | O(n) | Exact | **Yes** | Zero | 20 lines | No |
| **DFTopK** | O(n) | Deterministic | Approx | Zero | ~50 lines | No |
| **LapSum** | O(n log n) | Exact | **Yes** | Zero | Library | No |
| **Gumbel Top-k** | O(n·k) | STE | Yes (hard) | High | 20 lines | **Yes** |
| **SOFT (OT)** | O(n·k·T) | Biased | Yes | Zero | 120 lines | No |
| **NeuralSort** | O(n²) | Biased | N/A | Zero | Library | No |
| **SoftSort** | O(n²) | Biased | N/A | Zero | 3 lines | No |
| **Temp Sigmoid** | O(n) | Biased | No | Zero | 5 lines | Indirect |

### 7.3 Recommendation

**Primary: Sigmoid + Implicit Differentiation**

- 20 lines of PyTorch, zero dependencies, passes `torch.autograd.gradcheck`
- Exact Jacobian, zero variance — critical for stable LoRA fine-tuning
- Exactly satisfies Σp_i = k
- O(n) backward; forward binary search negligible vs VLA forward pass
- Soft probabilities usable as token weights; binarize with STE at inference

```python
# Reference implementation (Thomas Ahle)
# https://gist.github.com/thomasahle/4c1e85e5842d01b007a8d10f5fed3a18

class TopK(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x, k):
        # Binary search for threshold t such that sum(sigmoid(x + t)) = k
        lo, hi = -1000.0, 1000.0
        for _ in range(64):
            mid = (lo + hi) / 2
            if torch.sigmoid(x + mid).sum(-1).item() < k:
                lo = mid
            else:
                hi = mid
        t = (lo + hi) / 2
        p = torch.sigmoid(x + t)
        ctx.save_for_backward(p)
        return p

    @staticmethod
    def backward(ctx, grad_output):
        p, = ctx.saved_tensors
        v = p * (1 - p)  # sigmoid derivative
        # Implicit differentiation of constraint sum(p) = k
        grad = v * (grad_output - (v * grad_output).sum(-1, keepdim=True) / v.sum(-1, keepdim=True))
        return grad, None
```

**Secondary: DFTopK** — for citation in paper (published method), O(n) complexity, similar sigmoid approach but uses `torch.kthvalue`.

**Fallback: Gumbel Top-k** — if stochastic gradients prove beneficial for exploration during LoRA training. Proven in LightVLA.

### 7.4 Key Related Work

- **LightVLA** (arXiv:2509.12594): Gumbel-softmax VLA token pruning, LoRA rank 32, 59% FLOP reduction, 2.9% task success improvement
- **AutoSelect** (arXiv:2603.07135): Soft top-k + variance-preserving noise gating for LLaVA, 0.69ms overhead, 96.5% accuracy retention at 88.9% pruning
- **DiffRate** (ICCV 2023): Differentiable compression rate for ViT ([github.com/OpenGVLab/DiffRate](https://github.com/OpenGVLab/DiffRate))

## 8. Token Compression Integration: FastV-Style Pruning

### 8.1 How It Maps to SmolVLA

FastV prunes visual tokens at an intermediate LLM layer based on attention from text tokens. In SmolVLA:

**Option 1 — Prune before VLM+Expert forward (ACIS approach)**:
- After `embed_image()` returns `(B, 64, 960)`, score with ACIS, mask/select, then build prefix
- Pros: clean, modular, no VLM modification
- Cons: scores computed without LLM context

**Option 2 — Prune in VLM KV cache (inference optimization)**:
- After prefix encoding, prune KV entries for low-importance visual tokens
- Modify `past_key_values[layer]["key_states"]` and `["value_states"]`
- Shape: `(B, prefix_len, num_kv_heads, head_dim)` → remove rows for pruned visual positions
- Pros: reduces computation in all subsequent denoising steps
- Cons: requires tracking visual token positions within prefix

**Option 3 — Mid-layer pruning (FastV-faithful)**:
- In `SmolVLMWithExpertModel.forward()`, after layer N, compute attention scores from state/language tokens to visual tokens, prune, continue
- Requires modifying the layer-by-layer loop

**Recommendation**: Option 1 (ACIS before prefix) for training. At inference, additionally apply Option 2 (KV cache pruning) for efficiency.

### 8.2 Visual Token Position Tracking

Prefix layout for LIBERO (2 cameras):
```
[img_start(2)] [vis_0..63(64)] [img_end(1)]  → camera 1: tokens 0..66
[img_start(2)] [vis_0..63(64)] [img_end(1)]  → camera 2: tokens 67..133
[lang_tokens(48)]                              → tokens 134..181
[state_token(1)]                               → token 182
```

Visual token indices: `[2:66]` and `[69:133]` (64 tokens each, offset by special tokens).

## 9. Summary: ACIS Integration Blueprint

```
┌─────────┐     ┌──────────┐     ┌───────────────┐
│  Images  │────→│  SigLIP  │────→│  Connector    │──→ vis_tokens (B, 64×C, 960)
└─────────┘     └──────────┘     │  (PixelShuffle│
                                  │   + MLP)      │
                                  └───────────────┘
                                          │
                                          ▼
┌─────────────┐                 ┌─────────────────┐
│ embed_suffix │──a_query──────→│  ACIS Module    │
│ (noisy act + │  (B,Q,960)     │  CrossAttn +    │──→ importance_scores (B, N_vis)
│  time emb)   │                │  Score Head     │
└─────────────┘                 └─────────────────┘
                                          │
                                          ▼
                                ┌─────────────────┐
                                │  Soft Top-K     │──→ soft_mask (B, N_vis)
                                │  (Sigmoid+Impl) │
                                └─────────────────┘
                                          │
                                          ▼
                                ┌─────────────────┐
                                │  Apply Mask     │──→ pruned_vis (B, K, 960)
                                └─────────────────┘
                                          │
                                          ▼
                                ┌─────────────────┐
                                │  embed_prefix   │──→ prefix_embs (B, prefix_len', 960)
                                │  (+ lang + state│
                                └─────────────────┘
                                          │
                                          ▼
                                ┌─────────────────┐
                                │  VLM + Expert   │──→ v_t (B, 50, 32)
                                │  (16 layers)    │
                                └─────────────────┘
                                          │
                                          ▼
                                ┌─────────────────┐
                                │  Loss:          │
                                │  MSE(u_t, v_t)  │
                                │  + λ·L_margin   │
                                │  + λ·L_calibr   │
                                └─────────────────┘
```
