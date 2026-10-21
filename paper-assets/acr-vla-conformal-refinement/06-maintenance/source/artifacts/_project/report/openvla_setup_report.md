# OpenVLA Setup Report — bjb1-18228

## Model Info

| Item | Value |
|------|-------|
| Model | `openvla/openvla-7b-libero-spatial` (fine-tuned on LIBERO-Spatial) |
| Base | OpenVLA 7B = Llama 2 7B + DINOv2 + SigLIP (fused dual-backbone) |
| Size | 15 GB on disk (4 safetensors shards), ~15.1 GB VRAM (bf16) |
| Local path | `/root/autodl-tmp/models/openvla-libero-spatial/` |
| Action space | 256-bin discrete tokenization → 7D continuous (q01/q99 unnormalization) |
| Action dim | 7 (3 translation + 3 rotation + 1 gripper), single-step (chunk_size=1) |
| Hidden dim | 4096 (Llama 2), vs 960 in SmolVLA |
| Image input | 224x224 (processor handles resize), vs 512x512 in SmolVLA |
| unnorm_key | `libero_spatial` (auto-detected from norm_stats) |

## Environment

| Item | Value |
|------|-------|
| Server | bjb1-18228 (AutoDL) |
| GPU | 4x NVIDIA A800 (only GPU 0 used, single-GPU inference) |
| Python | 3.12 (`/root/miniconda3/bin/python`) |
| transformers | 5.8.0 (model was trained on 4.40.1; patched for compat) |
| torch | 2.7.0+cu126 |
| CUDA | 12.6 |

## Compatibility Patches Applied

OpenVLA's custom model code (`modeling_prismatic.py`, `processing_prismatic.py`) was written for transformers 4.40.1. Four patches were needed for transformers 5.8.0:

1. **Auto class rename**: `AutoModelForVision2Seq` → `AutoModelForImageTextToText` in config.json auto_map and wrapper code
2. **Remote repo prefix removal**: Stripped `openvla/openvla-7b--` prefix from auto_map entries in config.json, preprocessor_config.json, tokenizer_config.json so modules load from local directory instead of fetching from HuggingFace
3. **Import path changes in `processing_prismatic.py`**: `PaddingStrategy` moved from `transformers.tokenization_utils` to `transformers.utils`; `PreTokenizedInput/TextInput/TruncationStrategy` moved to `transformers.tokenization_utils_base`
4. **Model init compat in `modeling_prismatic.py`**:
   - `_supports_sdpa` property: added `hasattr(self, "language_model")` guard (accessed during `__init__` before `language_model` is set)
   - `tie_weights()`: added `**kwargs` to accept new `recompute_mapping` argument
   - Relaxed strict timm and transformers version checks

## Inference Performance

| Metric | Value |
|--------|-------|
| Model load time | ~16.8s |
| Single action (cold) | ~809 ms |
| Single action (warm, in rollout) | ~180 ms/step |
| K=3 samples (cold) | ~643 ms total |
| VRAM usage | 15.1 GB allocated, 15.2 GB reserved |

## Code Files Created

| File | Description |
|------|-------------|
| `src/openvla_wrapper.py` | OpenVLA wrapper with same interface as SmolVLAWrapper. Key method: `get_obs_features_and_samples()` returns `(obs_features: (1, 4096), samples: (1, K, 1, 7))` |
| `src/openvla_eval.py` | Standalone LIBERO eval script for OpenVLA (does not import/modify SmolVLA code) |
| `src/test_openvla_load.py` | Quick sanity test: loads model, generates action, tests K samples |

## Pipeline Validation

Single-episode test completed successfully:
- Benchmark: LIBERO-Spatial, Task 0, 1 rollout
- Result: 0/1 success (expected for single rollout; pipeline validation only)
- 300 steps executed at 180ms/step average
- Output: `logs/openvla_single_test.json`

Run command: `TRANSFORMERS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/openvla_eval.py --benchmark spatial --model_path /root/autodl-tmp/models/openvla-libero-spatial --n_rollouts 20`

## Key Differences from SmolVLA (CRM Integration Notes)

| Aspect | SmolVLA | OpenVLA |
|--------|---------|---------|
| Hidden dim (obs_features) | 960 | 4096 |
| Chunk size | 50 (H_eff=5) | 1 |
| Action generation | Flow-matching (continuous) | 256-bin discrete tokens |
| K samples | Single forward, sample flow | K independent forward passes |
| samples shape | (1, K, 50, 7) | (1, K, 1, 7) |

**CRM adaptation required**: CRM's `input_dim` depends on `obs_dim` (960 for SmolVLA). For OpenVLA (4096), either:
1. Train a separate CRM with `obs_dim=4096`
2. Add a projection layer 4096→960 before CRM
3. Use `obs_features=zeros` and rely only on `action_dim + uncertainty_dim`

**CGS adaptation required**: CGS expects `chunk_size` samples. With OpenVLA's chunk_size=1, the per-DOF std and conformal radius will be computed over 1-step actions only (vs 5-step chunks in SmolVLA). `H_EFF` should be set to 1 for OpenVLA.

## Risks

1. **transformers version fragility**: Patches are manual edits to model code files. If model files are re-downloaded, patches must be reapplied.
2. **Single-GPU only**: 15.1 GB VRAM leaves ~65 GB free on A800. Sufficient for concurrent CRM training.
3. **Inference speed**: 180ms/step is ~3x slower than SmolVLA. For 20 rollouts x 10 tasks x 300 steps, full eval takes ~3 hours.
4. **No eye-in-hand image**: OpenVLA uses only agentview (single image input), while SmolVLA uses both agentview and eye-in-hand. The wrapper's `get_obs_features_and_samples()` ignores `eye_in_hand_rgb`.
