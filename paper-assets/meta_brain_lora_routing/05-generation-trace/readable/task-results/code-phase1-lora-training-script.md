# code phase1 lora training script

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase1-lora-training-script_20260515T160319_result.json`
- **Structured JSON:** [`5a52f92681c9d979f947.json`](../../sessions/5a/5a52f92681c9d979f947.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 1 dry-run validation complete. All checks pass:

| Check | Result |
|-------|--------|
| Model load (PI0Pytorch from safetensors) | 3.5B params loaded on cuda:0 |
| LoRA injection — module targeting | **72 PaliGemma LM attn modules** (18 layers × 4 projections) |
| LoRA injection — param count | **3,686,400 trainable** (0.11% of total) |
| Forward + backward passes | 5 steps completed, loss 10.5 → 2.7 |
| Checkpoint save | `adapter_config.json` + `adapter_model.safetensors` (14.7MB) + `metadata.json` + `optimizer.pt` |
| Best model save | Saved to `checkpoints/phase1/visual/best/` |

The `adapter_config.json` confirms the regex targets only PaliGemma LM layers:
```
"target_modules": "paligemma_with_expert\.paligemma\.model\.language_model\.layers\.\d+\.self_attn\.(q|k|v|o)_proj"
```

**Artifacts delivered:**
- `artifacts/phase1/configs.py` — LoRAConfig (r=16, α=32), TrainConfig, perturbation taxonomy
- `artifacts/phase1/train_lora_expert.py` — full training script with model loading, PEFT LoRA injection (regex-based targeting), synthetic dry-run data, flow-matching loss, early stopping, W&B logging, checkpoint management

**Note:** The server (`/root/meta_brain_lora_routing/phase1/train_lora_expert.py`) now has a different version from another worker that integrates `data_loader.py` and `VisualAugmentation`. Both versions use the same correct `PALIGEMMA_ATTN_REGEX` for LoRA targeting.

---
