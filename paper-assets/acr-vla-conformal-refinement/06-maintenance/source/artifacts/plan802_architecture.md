# OpenVLA obs_only Residual Corrector: Architecture Design

## 1. Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Inference Pipeline                         │
│                                                              │
│  Image ──► OpenVLA ──► 7 discrete tokens ──► detokenize     │
│    │         │                                    │          │
│    │         │ (frozen)                    a_base (7D)       │
│    │         │                                    │          │
│    │    Vision Encoder                            │          │
│    │    (SigLIP+DINOv2)                           │          │
│    │         │                                    │          │
│    │    [256, 2176]                               │          │
│    │         │                                    │          │
│    │    Mean Pool                                  │          │
│    │         │                                    │          │
│    │      [2176]                                  │          │
│    │         │                                    │          │
│    │    Projection (2176 → 512)                   │          │
│    │         │                                    │          │
│    │      [512]                                   │          │
│    │         │                                    │          │
│    │         └──────────┐                         │          │
│    │                    ▼                         ▼          │
│    │              ┌──────────────┐                           │
│    │              │  Corrector   │                           │
│    │              │   (MLP)      │                           │
│    │              │              │                           │
│    │              │ Input: 519D  │ ◄── concat(obs_proj, a)  │
│    │              │ 512→256→256  │                           │
│    │              │ Output: 7D   │ ──► delta (ε-clipped)    │
│    │              └──────────────┘                           │
│    │                                              │          │
│    │                              a_final = a_base + delta   │
│    │                                              │          │
└─────────────────────────────────────────────────────────────┘
```

## 2. Feature Extraction

### Extraction Point: Pre-projector fused features

- **Source**: OpenVLA vision backbone output (before MLP projector to LLM space)
- **Raw shape**: `[batch, 256, 2176]` (256 patches, 1024 DINOv2 + 1152 SigLIP)
- **Pooling**: Spatial mean over 256 patches → `[batch, 2176]`
- **Projection**: Linear(2176, 512) with LayerNorm

**Why pre-projector, not post-projector (4096D)?**
- Pre-projector features are richer visual representations (DINOv2 spatial + SigLIP semantic)
- Post-projector features are optimized for language modeling, not action correction
- 2176D is more manageable than 4096D, and the projector discards visual information to fit LLM embedding space
- Empirically, DINOv2 features encode spatial/geometric information critical for manipulation

### Implementation

```python
class FeatureExtractor:
    """Extract and cache vision features from frozen OpenVLA."""
    
    def __init__(self, openvla_model):
        self.vision_backbone = openvla_model.vision_backbone
        self.vision_backbone.eval()
        for p in self.vision_backbone.parameters():
            p.requires_grad = False
    
    def extract(self, pixel_values):
        # pixel_values: [bsz, 6, 224, 224] (stacked for dual encoder)
        with torch.no_grad():
            feats = self.vision_backbone(pixel_values)  # [bsz, 256, 2176]
        return feats.mean(dim=1)  # [bsz, 2176]
```

## 3. Corrector Architecture

### MLP Design (~200K params)

```python
class ObsOnlyCorrectorOpenVLA(nn.Module):
    def __init__(self, obs_dim=2176, proj_dim=512, action_dim=7, 
                 hidden_dim=256, max_correction_norm=0.15):
        super().__init__()
        self.max_correction_norm = max_correction_norm
        
        # Observation projection
        self.obs_proj = nn.Sequential(
            nn.Linear(obs_dim, proj_dim),
            nn.LayerNorm(proj_dim),
            nn.GELU()
        )
        
        # Corrector MLP
        input_dim = proj_dim + action_dim  # 512 + 7 = 519
        self.mlp = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.GELU(),
            nn.LayerNorm(hidden_dim),
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, action_dim)
        )
        
        # Zero-init last layer for residual learning
        nn.init.zeros_(self.mlp[-1].weight)
        nn.init.zeros_(self.mlp[-1].bias)
    
    def forward(self, obs_features, base_action):
        """
        obs_features: [bsz, 2176] mean-pooled vision features
        base_action: [bsz, 7] de-tokenized OpenVLA action
        """
        obs_proj = self.obs_proj(obs_features)  # [bsz, 512]
        x = torch.cat([obs_proj, base_action], dim=-1)  # [bsz, 519]
        delta = self.mlp(x)  # [bsz, 7]
        
        # Epsilon-bounded norm clipping
        norm = delta.norm(dim=-1, keepdim=True).clamp(min=1e-8)
        delta = delta * (self.max_correction_norm / norm).clamp(max=1.0)
        
        return base_action + delta
```

### Key Design Choices

| Choice | Value | Rationale |
|--------|-------|-----------|
| Projection dim | 512 | Balance between expressiveness and overfitting (training set ~10-20K samples) |
| Hidden dim | 256 | Matches SmolVLA CRM, proven sufficient |
| max_correction_norm | 0.15 | OpenVLA actions are single-step 7D (not 30D chunk), corrections should be small |
| Zero-init last layer | Yes | Start as identity (no correction), learn deviations gradually |
| LayerNorm | After projection | Stabilize features from frozen encoder across different scenes |

### Parameter Count
- obs_proj: 2176×512 + 512 + 512 = ~1.1M
- MLP: 519×256 + 256×256 + 256×7 = ~200K
- **Total: ~1.3M** (lightweight, fast to train)

## 4. Training Pipeline

### Phase 1: Data Collection (Day 1-2)

**Goal**: Collect (observation, OpenVLA_action, expert_action) tuples on LIBERO-Object.

```
For each LIBERO-Object demo (10 tasks × ~50 demos × ~150 steps):
    1. Load observation image from demo
    2. Forward through frozen OpenVLA → get predicted action (7D)
    3. Record expert action from demo
    4. Extract vision features [256, 2176] → mean pool → [2176]
    5. Save to disk: {obs_features, vla_action, expert_action}
```

**Estimated dataset size**:
- 10 tasks × 50 demos × 150 steps = ~75,000 samples
- Storage per sample: 2176×4 + 7×4 + 7×4 ≈ 8.7 KB
- Total: ~650 MB (fits in RAM)

**OpenVLA inference speed**: ~0.5s per sample on single 4090 (autoregressive 7 tokens)
- Total collection time: 75,000 × 0.5s = ~10.4 hours on 1 GPU
- With 4 GPUs parallel: ~2.6 hours

### Phase 2: Training (Day 2-3)

**Loss function**:
```python
L = MSE(corrector(obs_feat, vla_action), expert_action)
```

**Training config**:
- Optimizer: AdamW, lr=5e-4, weight_decay=1e-4
- Schedule: Cosine decay with 5% warmup
- Batch size: 256 (fits easily on single GPU)
- Epochs: 100 (small model, fast convergence)
- Val split: 10% (per-task stratified)
- Augmentation: Gaussian noise on base_action (σ=0.02, 50% probability)

**Training time estimate**: 
- 75K samples, batch 256 → ~293 steps/epoch
- 100 epochs × 293 steps × ~5ms/step ≈ 2.5 minutes total
- Model is tiny, training is negligible. Data collection dominates.

### Phase 3: Evaluation (Day 3-5)

**Closed-loop evaluation on LIBERO-Object**:
- 10 tasks × 50 evaluation episodes
- Metrics: per-task success rate, average success rate
- Compare: OpenVLA baseline vs OpenVLA + corrector
- Ablations: correction norm budget (ε = 0.05, 0.10, 0.15, 0.20)

## 5. Action Space Details

### OpenVLA Action De-tokenization

```python
def detokenize_action(tokens, action_stats):
    """Convert 7 discrete tokens (0-255) to continuous actions."""
    # tokens: [7], each in {0, ..., 255}
    # Map bin index to normalized value in [-1, 1]
    continuous = (tokens.float() / 255.0) * 2.0 - 1.0
    # Denormalize using dataset statistics (per-dim min/max from training)
    actions = continuous * (action_stats['max'] - action_stats['min']) / 2.0 \
              + (action_stats['max'] + action_stats['min']) / 2.0
    return actions  # [7] continuous
```

### Correction Application

```
a_final = detokenize(OpenVLA_tokens) + clip(delta, ||delta||_2 <= epsilon)
```

The correction is applied in continuous action space AFTER de-tokenization. This is clean: the corrector never touches the discrete token space.

## 6. Comparison with SmolVLA CRM

| Aspect | SmolVLA CRM (obs_only) | OpenVLA Corrector |
|--------|----------------------|-------------------|
| obs_features dim | 960 (mean-pooled VLM hidden states) | 2176 (mean-pooled dual vision encoder) |
| Action input dim | 30 (5 steps × 6 DoF, chunked) | 7 (single step, 6 DoF + gripper) |
| Output dim | 30 | 7 |
| Multi-sample (K) | K=10 flow-matching samples | K=1 (single greedy decode) |
| Max correction norm | 0.5-1.42 (30D chunk) | 0.15 (7D single step) |
| Feature source | VLM text_model hidden states (language-grounded) | Vision backbone (spatial-geometric) |
| Parameters | ~327K | ~1.3M |
| Training samples | ~27K | ~75K |

### Conformal Guarantees: What Is Lost

1. **Multi-sample uncertainty estimation**: OpenVLA greedy decode = K=1, no empirical distribution over actions. Cannot compute CGS features (per-DOF std, conformal radii, log-volumes).

2. **Conformal prediction sets**: Without K samples, cannot construct nonconformity scores or calibrated prediction regions. No coverage guarantee P(Y ∈ C_α) ≥ 1-α.

3. **Online ACI adaptation**: Without per-step coverage signals, cannot run α_{t+1} = α_t + γ(α - err_t).

4. **What IS preserved**:
   - Residual correction bounded by ε (safety constraint)
   - obs_only architecture (which was empirically best anyway)
   - Zero-init residual learning

5. **Potential recovery path** (future work, not for CoRL deadline):
   - Use temperature>0 token sampling to generate K action samples from OpenVLA
   - Each sample: independent autoregressive decode with top-k/nucleus sampling
   - Cost: K× inference time (expensive: K=10 means 5s per step)
   - Alternative: Train a separate lightweight uncertainty head on vision features

## 7. Implementation Plan (5-7 Day Timeline)

| Day | Task | Output |
|-----|------|--------|
| 1 | Set up OpenVLA inference on server, verify action prediction on LIBERO-Object | Working inference script |
| 1-2 | Data collection: run OpenVLA on all LIBERO-Object demos, extract features | ~75K cached samples |
| 2-3 | Implement and train corrector MLP | Trained model checkpoint |
| 3-4 | Closed-loop evaluation: OpenVLA baseline | Baseline success rates |
| 4-5 | Closed-loop evaluation: OpenVLA + corrector | Corrector success rates |
| 5-6 | Ablations (ε values, projection dim, with/without action conditioning) | Ablation results |
| 6-7 | Buffer for debugging, additional experiments | Final numbers |

## 8. Risk Assessment

### High Risk
- **OpenVLA baseline too weak on LIBERO-Object**: If OpenVLA success rate is <5%, residual correction may not help (garbage in, garbage out). Mitigation: check baseline first (Day 3), pivot to fine-tuned OpenVLA if needed.
- **Feature extraction overhead**: Loading full 8B OpenVLA model just for vision features is memory-heavy (~16GB). Mitigation: extract and cache features offline in Phase 1.

### Medium Risk  
- **Action normalization mismatch**: OpenVLA's 256-bin discretization may use different normalization than LIBERO-Object expert actions. Mitigation: verify action statistics match before training.
- **Single-step vs chunked**: SmolVLA's CRM corrected 5-step chunks (temporal smoothing). Single-step correction may be noisier. Mitigation: ε-clipping provides hard safety bound.

### Low Risk
- **Model too small**: 1.3M params for 75K samples is well-sized (not overparameterized). Could increase if needed.
- **Training instability**: Zero-init + small corrections + LayerNorm makes training stable by construction.

## 9. Compute Requirements

| Resource | Requirement |
|----------|-------------|
| Data collection (Phase 1) | 4×4090, ~3 hours (OpenVLA inference parallelized) |
| Training (Phase 2) | 1×4090, <5 minutes |
| Evaluation (Phase 3) | 4×4090, ~6 hours (500 episodes × ~45s each) |
| Peak GPU memory | ~20GB (OpenVLA model for feature extraction) |
| Disk | ~1GB (cached features + checkpoints) |

## 10. Summary

This design is a minimal viable corrector: extract frozen visual features from OpenVLA's dual vision encoder, project to compact space, predict bounded residual corrections via lightweight MLP. The key tradeoff vs SmolVLA CRM is losing conformal guarantees (no multi-sample uncertainty) in exchange for architectural simplicity and compatibility with OpenVLA's autoregressive token-based action space. The obs_only approach was empirically the strongest variant in SmolVLA experiments, so this is not merely a fallback but builds on the best-performing design.
