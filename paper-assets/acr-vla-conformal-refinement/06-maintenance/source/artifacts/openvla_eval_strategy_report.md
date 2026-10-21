# OpenVLA 7B LIBERO Evaluation: Fix Report

**Date**: 2026-05-18
**Server**: bjb1-18228 (4x RTX 4090)
**Status**: Dry-run successful, ready for full evaluation

## 1. Problem

Our project wrapper (`src/openvla_wrapper.py`) uses transformers 5.8's `AutoModelForImageTextToText`, which triggers `DynamicCache` in the model's internal `generate()` call. OpenVLA's custom Prismatic model code is incompatible with this cache format, resulting in 0% success rate on all LIBERO benchmarks.

## 2. Strategy Chosen

Use the **official OpenVLA repo's eval code** with the correct dependency versions (transformers 4.40.1), instead of patching transformers 5.8 compatibility into the model code.

## 3. Environment Setup

**Conda env**: `/root/autodl-tmp/conda_envs/openvla` (Python 3.10)

Key packages:
- `transformers==4.40.1` (uses `AutoModelForVision2Seq`, not `AutoModelForImageTextToText`)
- `torch==2.2.0+cu121`
- `timm==0.9.16`
- `libero==0.1.1` (from PyPI)
- `flash-attn`: compiling in background; eager attention fallback used for dry-run

**Model weights** (local):
- `/root/autodl-tmp/models/openvla-libero-spatial`
- `/root/autodl-tmp/models/openvla-libero-object`

**Eval code**: `/root/autodl-tmp/openvla/` (cloned via gitclone.com mirror)

**LIBERO assets**: Downloaded from `jadechoghari/libero-assets` via hf-mirror.com to `/root/.cache/libero/assets/`, symlinked from the libero package's assets directory.

## 4. Bugs Found and Fixed

### Bug 1: `attention_mask` / `input_ids` length mismatch in `predict_action()`

**Root cause**: `predict_action()` appends token ID 29871 (empty space token) to `input_ids` to match training format, but does NOT extend the `attention_mask` passed via `**kwargs`. With flash_attention_2, this is harmless because flash attention doesn't use the explicit 4D causal mask. With eager attention, LlamaAttention constructs a causal mask from the attention_mask, and the 1-element length mismatch causes:

```
RuntimeError: The size of tensor a (277) must match the size of tensor b (276) at non-singleton dimension 3
```

at `modeling_llama.py:375: attn_weights = attn_weights + causal_mask`.

**Fix**: In `predict_action()`, extend `attention_mask` when appending the extra token:

```python
if not torch.all(input_ids[:, -1] == 29871):
    input_ids = torch.cat(
        (input_ids, torch.unsqueeze(torch.Tensor([29871]).long(), dim=0).to(input_ids.device)), dim=1
    )
    if 'attention_mask' in kwargs and kwargs['attention_mask'] is not None:
        kwargs['attention_mask'] = torch.cat(
            [kwargs['attention_mask'], torch.ones((1, 1), dtype=kwargs['attention_mask'].dtype, device=kwargs['attention_mask'].device)], dim=1
        )
```

**Files modified**:
- `/root/.cache/huggingface/modules/transformers_modules/openvla-libero-spatial/modeling_prismatic.py` (HF cached copy, loaded at runtime)
- `/root/autodl-tmp/models/openvla-libero-spatial/modeling_prismatic.py`
- `/root/autodl-tmp/models/openvla-libero-object/modeling_prismatic.py`
- `/root/.cache/huggingface/modules/transformers_modules/openvla_hyphen_libero_hyphen_object/e6c2690bae843207/modeling_prismatic.py`

### Bug 2: `AutoModelForVision2Seq` not in `auto_map`

**Root cause**: The model's `config.json` only had `AutoModelForImageTextToText` in `auto_map` (transformers 5.x name). transformers 4.40.1 uses `AutoModelForVision2Seq`.

**Fix**: Added `"AutoModelForVision2Seq": "modeling_prismatic.OpenVLAForActionPrediction"` to `auto_map` in both model config.json files.

### Bug 3 (informational): DynamicCache patches were irrelevant

Earlier patches to `prepare_inputs_for_generation()` and `forward()` for DynamicCache handling were unnecessary for transformers 4.40.1 (which uses tuple-based KV cache). The HF-cached copy of the model code had the original (correct) logic. These patches in the model directory copies have been reverted.

## 5. Dry-Run Results

**Command**:
```bash
CUDA_VISIBLE_DEVICES=1 HF_ENDPOINT=https://hf-mirror.com TF_CPP_MIN_LOG_LEVEL=3 TOKENIZERS_PARALLELISM=false \
/root/autodl-tmp/conda_envs/openvla/bin/python experiments/robot/libero/run_libero_eval.py \
    --model_family openvla \
    --pretrained_checkpoint /root/autodl-tmp/models/openvla-libero-spatial \
    --task_suite_name libero_spatial \
    --center_crop True \
    --num_trials_per_task 1 \
    --seed 42
```

**Results** (10 tasks x 1 trial, COMPLETE):
| # | Task | Result |
|---|------|--------|
| 1 | bowl between plate and ramekin | Success |
| 2 | bowl next to ramekin | Success |
| 3 | bowl from table center | Fail |
| 4 | bowl on cookie box | Success |
| 5 | bowl in top drawer of cabinet | Success |
| 6 | bowl on ramekin | Fail |
| 7 | bowl next to cookie box | Fail |
| 8 | bowl on stove | Fail |
| 9 | bowl next to plate | Success |
| 10 | bowl on wooden cabinet | Success |

**Final: 6/10 (60%)** success rate. No tensor errors, no exceptions. With only 1 trial per task, variance is extremely high. The OpenVLA paper reports ~84% on libero_spatial with 50 trials per task, so this 60% single-trial result is consistent.

**Standalone predict_action test**:
```
Action: [0.089, 0.071, 0.137, -0.059, 0.062, 0.114, 0.0]
```
7D continuous actions (6 DoF + gripper), non-zero, non-random.

## 6. Full Evaluation Commands

For the full evaluation (10 tasks x 50 trials per benchmark), use a dedicated GPU:

### libero_spatial
```bash
cd /root/autodl-tmp/openvla
CUDA_VISIBLE_DEVICES=<GPU_ID> HF_ENDPOINT=https://hf-mirror.com TOKENIZERS_PARALLELISM=false \
/root/autodl-tmp/conda_envs/openvla/bin/python experiments/robot/libero/run_libero_eval.py \
    --model_family openvla \
    --pretrained_checkpoint /root/autodl-tmp/models/openvla-libero-spatial \
    --task_suite_name libero_spatial \
    --center_crop True \
    --num_trials_per_task 50 \
    --seed 42
```

### libero_object
```bash
cd /root/autodl-tmp/openvla
CUDA_VISIBLE_DEVICES=<GPU_ID> HF_ENDPOINT=https://hf-mirror.com TOKENIZERS_PARALLELISM=false \
/root/autodl-tmp/conda_envs/openvla/bin/python experiments/robot/libero/run_libero_eval.py \
    --model_family openvla \
    --pretrained_checkpoint /root/autodl-tmp/models/openvla-libero-object \
    --task_suite_name libero_object \
    --center_crop True \
    --num_trials_per_task 50 \
    --seed 42
```

**Estimated time**: Each benchmark takes ~2-3 hours on a single 4090 with eager attention. With flash-attn (once compiled), expect ~30-50% faster.

**GPU requirements**: ~15-19 GB VRAM. Can share a 24 GB GPU if the other process uses < 5 GB.

## 7. Notes

- **flash-attn**: Still compiling in background. Once available, the model will automatically use flash_attention_2 (the `importlib.util.find_spec("flash_attn")` check in `openvla_utils.py` handles this). Flash attention makes the attention_mask fix unnecessary for correctness but the fix should remain for robustness.
- **China network**: GitHub is blocked. Use `gitclone.com` for git clones and `hf-mirror.com` for HuggingFace (set `HF_ENDPOINT=https://hf-mirror.com`).
- **LIBERO assets**: Downloaded to `/root/.cache/libero/assets/` and symlinked from the libero package directory. No manual extraction needed.
- **GPU constraints**: cuda:0 and cuda:2 are reserved for K sweep. cuda:1 and cuda:3 are running crm_k1 evaluations. The dry-run shares cuda:1 (18.7/24.5 GB total).
