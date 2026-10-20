# research smolvla setup

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_smolvla_setup_20260520T230045_result.json`
- **Structured JSON:** [`b7836ee82aeab779f0cb.json`](../../sessions/b7/b7836ee82aeab779f0cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All steps complete. Here's the full architecture report:

---

## SmolVLA Architecture Report

### 1. Model Type + Backbone
- **Model**: SmolVLA (lerobot `HuggingFaceVLA/smolvla_libero`)
- **VLM backbone**: SmolVLM2-500M-Instruct (`HuggingFaceTB/SmolVLM2-500M-Instruct`)
- **LLM**: SmolLM2 (Llama-style architecture)
- **Total SmolVLA params**: ~450M (VLM 507M + action expert ~100M, with weight sharing)

### 2. Layer Count
- **VLM text layers**: 32 (LIBERO config uses ALL 32, not 16 as in the paper's default)
- **SigLIP vision layers**: 12
- **Action expert layers**: 32 (paired 1:1 with VLM layers)

### 3. Hidden Size
- **VLM text hidden**: 960
- **VLM vision hidden**: 768
- **Action expert hidden**: 480 (0.5 × 960, LIBERO config)

### 4. Attention Heads
- **Text heads**: 15 total, 5 KV heads (GQA), head_dim=64
- **Vision heads**: 12
- **Expert**: q_proj [960, 480] — same head structure as VLM projected from expert hidden

### 5. Vision Encoder + Image Tokens
- **Type**: SigLIP (512×512 input, patch_size=16)
- **Raw patches**: (512/16)² = 1024
- **pixel_shuffle_factor**: 4 → 64 visual features
- **Input tokens**: 1088 image-related tokens (1024 patches + 64 formatting/row-col markers)
- **Total sequence**: 5 (system) + 1088 (image) + 21 (instruction) = ~1150

### 6. Action Tokenization
- **Continuous actions via flow matching** (NOT discrete bins like OpenVLA)
- `action_in_proj`: [480, 32] — projects action dim to expert hidden
- `action_out_proj`: [32, 480] — expert hidden to action predictions
- `chunk_size`: 50 actions per prediction
- `num_steps`: 10 denoising steps
- Action shape: [7] for LIBERO (7-DoF)

### 7. Token Layout
```
[<|im_start|>] [User:] [&lt;fake_token_around_image>] [&lt;row_1_col_1>] [1088 image tokens] [instruction ~21 tokens]
 pos 0-4 (sys)          pos 5-1128 (image region)                   pos 1129-1149 (text)
```

### 8. Causal Mask
- VLM backbone: standard causal attention
- Action expert: interleaved cross-attention (from VLM) + causal self-attention (self_attn_every_n_layers=2)

### 9. Dry-Run Results (1 task, 1 demo, 10 timesteps)

```
[last_preaction position]
  L0:  shape (10, 960), mean=-0.0010, std=0.1179
  L32: shape (10, 960), mean=-0.0495, std=1.7661

[image_mean position]
  L0:  mean=-0.1922, std=3.0528
  L32: mean=0.0222,  std=0.8629

Temporal variance:
  last_preaction L0:  0.000000 (identical — same instruction)
  last_preaction L32: 0.005407 (image-driven variation)
  image_mean L0:      0.005674 (different images)
  image_mean L32:     0.002103

Cosine sim (t=0 vs t=last):
  last_preaction L0:  1.0000 | L32: 0.9969
  image_mean L0:      0.9991 | L32: 0.9962
```

### 10. Key Differences vs OpenVLA

| Feature | OpenVLA | SmolVLA |
|---------|---------|---------|
| Backbone | Llama-2-7B | SmolLM2-500M |
| Total params | 7.6B | ~450M |
| Text layers | 32 | 32 |
| Hidden dim | 4096 | 960 |
| Vision encoder | SigLIP + DINOv2 (fused) | SigLIP only |
| Image tokens | 256 | ~1088 |
| Action method | Discrete 256-bin tokenization | Continuous flow matching |
| Action generation | Autoregressive (VLM generates action tokens) | Separate action expert (cross-attn from VLM) |
| VLM during training | Fine-tuned | **Frozen** (train_expert_only=True) |
| Feature size per timestep | 32 × 4096 = 131K | 32 × 960 = 30K (~4.3× smaller) |

### Critical Design Implication
**VLM is frozen** → VLM hidden states are identical whether the model is "trained" or not. The trained/untrained distinction only applies to the action expert. For counterfactual instruction analysis, we still get meaningful results because different instructions → different VLM hidden states → different action expert cross-attention → different actions.

### Installed Packages
- `transformers` upgraded: 4.48.3 → 5.9.0
- `num2words` installed (required by SmolVLMProcessor)

### Downloaded Checkpoints
- `/root/autodl-tmp/vla-ssd/checkpoints/smolvla_libero/` — SmolVLA LIBERO (1.22GB)
- `/root/autodl-tmp/vla-ssd/checkpoints/smolvlm2-500m/` — SmolVLM2-500M-Instruct (2.0GB)

---
