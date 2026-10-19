# SmolVLA Wrapper ↔ lerobot Pipeline Alignment Analysis

**Date**: 2026-05-14  
**Server**: bjb2-40593 (RTX 4090 D, 24GB)  
**Model**: smolvla_libero (LIBERO fine-tuned SmolVLA)

## lerobot Inference Pipeline (from checkpoint config)

### Preprocessor (6 steps)
Source: `policy_preprocessor.json`

| Step | Class | Function |
|------|-------|----------|
| 0 | RenameProcessorStep | Rename obs keys to lerobot format |
| 1 | ToBatchProcessorStep | Add batch dim |
| 2 | SmolVLANewLineProcessor | **Append `\n` to task string** |
| 3 | SmolVLATokenizerProcessorStep | Tokenize (max_length=48, padding=max_length) |
| 4 | DeviceProcessorStep | Move to CUDA |
| 5 | NormalizerProcessorStep | MEAN_STD normalize state (IDENTITY for images) |

### Postprocessor (2 steps)
Source: `policy_postprocessor.json`

| Step | Class | Function |
|------|-------|----------|
| 0 | UnnormalizerProcessorStep | MEAN_STD unnormalize action |
| 1 | DeviceProcessorStep | Move to CPU |

### LiberoProcessorStep (env-level)
Source: `lerobot/processor/env_processor.py`

- Images: `torch.flip(img, dims=[2, 3])` — flip H and W axes
- State: quat→axisangle, concat `[eef_pos(3), axisangle(3), gripper_qpos(2)]` → 8D

## Wrapper Alignment Verification

| Step | lerobot | Wrapper | Match |
|------|---------|---------|-------|
| Image flip H+W | `torch.flip(img, dims=[2,3])` | `img.flip(dims=[-2,-1])` | ✅ |
| Image resize | `resize_with_pad(img, 512, 512)` | Same function imported | ✅ |
| Image normalize | `img * 2.0 - 1.0` (inside VLM) | `img * 2.0 - 1.0` (explicit) | ✅ |
| Task string `\n` | SmolVLANewLineProcessor | `task_text = f"{task_name}\n"` | ✅ (FIXED) |
| Tokenizer | max_length=48, pad=max_length | Same config from model | ✅ |
| State dim | 8D (eef+axisangle+gripper) | 8D from evaluate.py | ✅ |
| State normalize | MEAN_STD: `(x-mean)/(std+eps)` | Same formula, eps=1e-8 | ✅ |
| State pad | Pad to max_state_dim=32 | `torch.zeros(1, 32)` | ✅ |
| Action unnormalize | `x * (std+eps) + mean` | `x * std + mean` | ⚠️ (eps difference, negligible) |
| Flow matching | 10 denoising steps, dt=-0.1 | Same | ✅ |
| KV cache | Standard lerobot pattern | Reused for K samples | ✅ |

## Fix Applied

**Root cause**: The wrapper was missing Step 2 (SmolVLANewLineProcessor) — appending `\n` to the task description string before tokenization. This caused the tokenized input to differ from training time by 1 token (token ID 198 = `\n`), shifting all downstream attention patterns.

**Fix**: Added `\n` append in both `preprocess_obs()` (line 130) and `preprocess_obs_batch()` (line 166).

```python
# Before (wrong)
tokens = self.tokenizer(task_name, ...)

# After (correct)
task_text = task_name if task_name.endswith("\n") else f"{task_name}\n"
tokens = self.tokenizer(task_text, ...)
```

## Normalization Stats (from checkpoint safetensors)

### State (8D) — MEAN_STD
- Mean: `observation.state.mean` from `policy_preprocessor_step_5_normalizer_processor.safetensors`
- Std: `observation.state.std` from same file

### Action (7D) — MEAN_STD  
- Mean: `action.mean` from `policy_postprocessor_step_0_unnormalizer_processor.safetensors`
- Std: `action.std` from same file

### Images — IDENTITY (no normalization at preprocessor level)
- [0,1] → [-1,1] conversion happens inside `prepare_images()` in the VLM

## Key Model Config
```json
{
  "chunk_size": 50,
  "max_state_dim": 32,
  "max_action_dim": 32,
  "resize_imgs_with_padding": [512, 512],
  "num_steps": 10,
  "tokenizer_max_length": 48,
  "empty_cameras": 0
}
```
