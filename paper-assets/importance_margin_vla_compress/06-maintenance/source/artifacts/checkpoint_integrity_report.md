=== CHECKPOINT INTEGRITY REPORT ===
Path: /root/autodl-tmp/importance_margin_vla_compress/checkpoints/libero_lora_50k/checkpoint.pt
File size: 924,851,886 bytes (924 MB)
Step: 50000
Embedded config: libero_baseline.yaml (LoRA rank=32, alpha=16)

## [Step 1] LoRA Weight Check: PASS

- Total state_dict keys: 574 (all PEFT-pattern `model.base_model.model.*`)
- LoRA params: 74 (37 pairs of lora_A + lora_B)
- Non-zero check: **PASS** — all params have nonzero elements
- Key alignment with model: **0 missing keys, 0 unexpected keys**

Sample weights:
| Key | Shape | Mean | Std | NonZero |
|-----|-------|------|-----|---------|
| action_in_proj.lora_A | (32, 32) | -0.000613 | 0.139574 | 1024/1024 |
| action_in_proj.lora_B | (720, 32) | -0.000224 | 0.031929 | 23040/23040 |
| lm_expert.layers.0.q_proj.lora_A | (32, 720) | -0.000237 | 0.032187 | 23040/23040 |
| lm_expert.layers.0.q_proj.lora_B | (960, 32) | -0.000076 | 0.024800 | 30720/30720 |

## [Step 2] MD5 Comparison: PASS (MATCH)

| Location | Path | MD5 |
|----------|------|-----|
| westd-27271 | checkpoints/libero_lora_50k/checkpoint.pt | 445418230f9642acc1932d7a3098cab3 |
| cqa1-33015 | checkpoints/libero_baseline/step_050000/checkpoint.pt | 445418230f9642acc1932d7a3098cab3 |

No SCP/transfer corruption.

## [Step 3] Inference Check: PASS (REASONABLE)

10 forward passes with random observations, using exact eval code path (`predict_actions` via `sample_actions`):

| Trial | First Action (7D) | Chunk Mean | Chunk Std |
|-------|-------------------|------------|-----------|
| 0 | [-0.23, 0.35, -0.19, -0.24, 0.02, 0.02, 0.88] | -0.125 | 0.341 |
| 1 | [0.10, 0.23, -0.01, -0.34, -0.06, 0.01, 0.87] | -0.055 | 0.317 |
| 2 | [-0.05, 0.17, -0.18, -0.30, -0.01, 0.01, 0.90] | -0.086 | 0.314 |
| ... | ... | ... | ... |
| 9 | [0.07, 0.24, -0.05, -0.36, -0.02, 0.02, 0.90] | -0.143 | 0.354 |

- Action chunk shape: (50, 7) ✓
- Global range: [-1.026, 1.000] — within expected bounds ✓
- Mean abs value: 0.224 — non-degenerate ✓
- Any NaN: **False** ✓
- All zeros: **False** ✓
- All same: **False** — model responds to different inputs ✓
- Cross-trial std per dim: [0.15, 0.08, 0.20, 0.06, 0.05, 0.05, 0.55]

## ⚠️ CRITICAL FINDING: Config/Checkpoint Key Mismatch Risk

Full FT and LoRA checkpoints have **ZERO overlapping keys**:
- Full FT keys: `model.action_in_proj.weight` (500 keys, no PEFT wrapper)
- LoRA keys: `model.base_model.model.action_in_proj.base_layer.weight` (574 keys, PEFT-wrapped)
- **Overlap: 0 keys**

The eval script uses `strict=False`, which **silently ignores all mismatched keys**. If:
- Full FT checkpoint is evaluated with LoRA config → 0 keys loaded → pretrained model + random LoRA = ~0% SR
- LoRA checkpoint is evaluated with Full FT config → 0 keys loaded → pretrained model = ~0% SR

The saved eval result file (`eval_results/libero_libero_object.json`) shows:
- checkpoint: `checkpoints/libero_full_ft_50k/checkpoint.pt` (Full FT!)
- config: `configs/libero_baseline.yaml` (LoRA rank=32!)
- result: SR = 0/1 (0%)

**This IS a config-checkpoint mismatch.** However, this file appears to be from the Full FT eval, not the LoRA eval.

=== VERDICT ===
☑ **CONFIRMED: No loading/transfer bug** — weights are correct, MD5 matches, inference is reasonable.
☐ LOADING BUG (weights zero/corrupted/md5 mismatch) — ruled out.

**If LoRA was evaluated with the correct config (`libero_baseline.yaml`):**
→ LoRA genuinely 0% SR at 50K. The model produces non-degenerate actions but the policy is simply not good enough.

**If LoRA was evaluated with the wrong config (e.g., `libero_full_ft.yaml` with rank=0):**
→ 0% SR is a config bug, not a training failure. Re-evaluate with the correct config.

**Recommendation:** Re-run the LoRA eval with explicit logging of load_state_dict result:
```bash
python eval_success_rate_libero.py \
    --checkpoint checkpoints/libero_lora_50k/checkpoint.pt \
    --config configs/libero_baseline.yaml \
    --suite libero_object --num_episodes 10 --task_ids 0
```
And add a check: if `load_state_dict(strict=False)` returns any missing/unexpected keys, log a **WARNING**.
