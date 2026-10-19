# SmolVLA Architecture Notes (Verified from lerobot source)

## Module Hierarchy

```
SmolVLAPolicy                               (PreTrainedPolicy)
├── model: VLAFlowMatching                   (nn.Module)
│   ├── vlm_with_expert: SmolVLMWithExpertModel
│   │   ├── vlm: SmolVLMForConditionalGeneration
│   │   │   └── model
│   │   │       ├── vision_model             SigLIP vision encoder
│   │   │       ├── connector                PixelShuffle + Linear projection
│   │   │       └── text_model               SmolLM2 language model
│   │   │           ├── get_input_embeddings()
│   │   │           └── layers[0..N-1]       Transformer layers
│   │   ├── lm_expert                        Action expert (smaller LM)
│   │   │   └── layers[0..M-1]
│   │   └── processor                        AutoProcessor (tokenizer etc.)
│   ├── state_proj: Linear(max_state_dim → hidden_size)
│   ├── action_in_proj: Linear(max_action_dim → expert_hidden_size)
│   ├── action_out_proj: Linear(expert_hidden_size → max_action_dim)
│   ├── action_time_mlp_in: Linear(expert_hidden*2 → expert_hidden)
│   └── action_time_mlp_out: Linear(expert_hidden → expert_hidden)
```

## Key Dimensions (SmolVLM2-500M-Video-Instruct)

- `text_config.hidden_size` = 960 (VLM hidden dim, connector output dim)
- `expert_hidden_size` = 720 (960 * expert_width_multiplier=0.75)
- `num_vlm_layers` = 16 (config default, may be reduced from base model's 32)
- `num_expert_layers` = -1 (default → same as num_vlm_layers = 16)
- `max_state_dim` = 32, `max_action_dim` = 32
- `chunk_size` = 50, `n_action_steps` = 50
- Image resize: 512×512 with padding (resize_with_pad function)

## Forward Data Flow

### Training: SmolVLAPolicy.forward(batch)

1. `prepare_images(batch)` → images list, img_masks
2. `prepare_state(batch)` → state tensor (padded to max_state_dim=32)
3. `prepare_action(batch)` → actions tensor (padded to max_action_dim=32)
4. `self.model.forward(images, img_masks, lang_tokens, lang_masks, state, actions)`
   → calls VLAFlowMatching.forward()

### VLAFlowMatching.forward()

1. Flow matching setup:
   - `noise = sample_noise(actions.shape)`
   - `time = sample_time(B)`
   - `x_t = time * noise + (1-time) * actions`
   - `u_t = noise - actions` (target velocity)

2. `embed_prefix(images, img_masks, lang_tokens, lang_masks, state)`:
   - For each camera image:
     - Optional: embed image start special tokens
     - **`vlm_with_expert.embed_image(img)`** ← ACIB hook point
       - `vision_model(pixel_values)` → `.last_hidden_state`
       - `connector(hidden_states)` → visual tokens (B, N, 960)
     - Scale: `img_emb * sqrt(dim)`
     - Optional: embed image end special tokens
   - Embed language tokens: `embed_language_tokens(lang_tokens) * sqrt(dim)`
   - Project state: `state_proj(state)` → (B, 1, 960)
   - Concatenate all → prefix_embs (B, L_prefix, 960)

3. `embed_suffix(x_t, time)`:
   - `action_in_proj(x_t)` → (B, chunk_size, expert_hidden)
   - Time embedding via sinusoidal + MLP
   - → suffix_embs (B, chunk_size, expert_hidden)

4. `vlm_with_expert.forward(inputs_embeds=[prefix_embs, suffix_embs])`:
   - Interleaved VLM + expert layers
   - VLM processes prefix, expert processes suffix
   - Cross-attention: expert attends to VLM KV cache
   - → (prefix_out, suffix_out)

5. `action_out_proj(suffix_out[:, -chunk_size:])` → v_t (B, chunk, max_action_dim)
6. `F.mse_loss(u_t, v_t, reduction="none")` → losses

### SmolVLAPolicy.forward() return

- `reduction="mean"` (default): `(loss: scalar, loss_dict: dict)`
- `reduction="none"`: `(per_sample_loss: (B,), loss_dict: dict)`

## embed_image() — ACIB Hook Target

```python
# In SmolVLMWithExpertModel:
def embed_image(self, image):
    hidden = self.vlm.model.vision_model(
        pixel_values=image.to(dtype=self.vlm.model.vision_model.dtype)
    ).last_hidden_state
    hidden = self.vlm.model.connector(hidden)   # ← HOOK HERE
    return hidden
```

The connector output shape: `(B, N_visual_tokens, 960)`.
N_visual_tokens depends on SigLIP patch count after pixel shuffle reduction.

## num_expert_layers Semantics

From SmolVLMWithExpertModel.__init__:
- `num_expert_layers > 0`: Expert has exactly that many layers. VLM layers must be divisible by it. Expert layers are interleaved: every `num_vlm_layers // num_expert_layers` VLM layers share one expert layer.
- `num_expert_layers = -1` or `0`: Expert has same number of layers as VLM (1:1 mapping).

`get_model_layers()` maps expert layers to VLM layers:
- `multiple_of = num_vlm_layers // num_expert_layers`
- VLM layer i gets expert layer `i // multiple_of` (or None if not aligned)

## Attention Mode

Default: `cross_attn` with `self_attn_every_n_layers=2`
- Even layers (0, 2, 4...): self-attention (prefix + suffix concatenated)
- Odd layers (1, 3, 5...): cross-attention (expert queries attend to VLM KV)
- `fill_kv_cache` phase: always self-attention (builds KV cache for prefix)

## Image Processing

- `resize_with_pad(img, 512, 512, pad_value=-1)`: aspect-ratio-preserving resize, pad top-left
- No separate crop or center-crop — just resize + pad

## ACIB Integration Points

1. **Hook**: `register_forward_hook` on `base_policy.model.vlm_with_expert.vlm.model.connector`
2. **Conditioning**: MVP uses `connector_output.mean(dim=1)` as self-conditioning
3. **Freeze**: `vlm_with_expert.vlm` (entire VLM) frozen; `lm_expert` optionally trainable
4. **Vision pipeline for perturbation**: `vlm_with_expert.embed_image(perturbed_img)` (bypasses hook via flag)
