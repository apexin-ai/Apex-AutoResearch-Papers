# sft_qwen14b_s0_sweep Analysis

**Date**: 2026-05-21
**Server**: westd-29999, GPU: cuda:3
**Model**: Qwen2.5-14B, seed=0
**Config**: lora_r=16, lora_alpha=32, lr=5e-5, batch=1, grad_accum=16

## Training Status

| Dosage | Status | Train Loss | Token Acc | Steps | Runtime |
|--------|--------|-----------|-----------|-------|---------|
| d000 | ✅ Complete | 0.9095 | 0.7842 | 3125 | 11130s |
| d005 | ✅ Complete | 0.9134 | 0.7703 | 3177 | 11350s |
| d025 | ✅ Complete | 0.9261 | 0.7705 | 3384 | 11680s |
| d050 | ❌ **CRASHED** | — | — | 1902/3642 (52%) | ~6600s |
| d100 | ✅ Complete | 0.9695 | 0.7640 | 4159 | 13560s |

## d050 Crash Details

- **Error**: `RuntimeError: Pin memory thread exited unexpectedly`
- **Location**: trainer.py → dataloader → pin_memory_thread
- **Progress**: 52% (step 1902/3642, epoch ~0.52)
- **Note**: Script reported exit_code=0 despite crash. Same d050 empty adapter bug pattern as previous runs.
- **Impact**: No adapter produced.

## MMLU Eval Results

| Dosage | MMLU Accuracy | Correct/Total | Δ from d000 |
|--------|--------------|---------------|-------------|
| d000 | 68.84% | 9666/14042 | — |
| d005 | 68.86% | 9670/14042 | +0.02pp |
| d025 | 65.05% | 9135/14042 | -3.79pp |
| d050 | — | — | — |
| d100 | 43.85% | 6157/14042 | -24.99pp |

## Adapter File Check

| Dosage | Path | Size |
|--------|------|------|
| d000 | `checkpoints/Qwen2.5-14B_d000_s0/lora_adapter/` | 263MB |
| d005 | `checkpoints/Qwen2.5-14B_d005_s0/lora_adapter/` | 263MB |
| d025 | `checkpoints/Qwen2.5-14B_d025_s0/lora_adapter/` | 263MB |
| d050 | `checkpoints/Qwen2.5-14B_d050_s0/lora_adapter/` | **EMPTY** |
| d100 | `checkpoints/Qwen2.5-14B_d100_s0/lora_adapter/` | 263MB |

All adapters verified: lora_alpha=32 ✓

## Dose-Response Pattern

MMLU collapse at d100 is **-24.99pp** — much more severe than s42 (-9.37pp). Monotonic degradation d000→d025→d100 consistent with contamination-induced overfitting. Training loss increases with dosage (0.9095 → 0.9695).

## Conclusion

**Partial success.** 4/5 dosages complete. d050 requires retraining (Pin memory thread crash). Action: retrain d050_s0 only.
