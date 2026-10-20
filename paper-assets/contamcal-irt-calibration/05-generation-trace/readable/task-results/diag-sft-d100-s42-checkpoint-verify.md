# diag sft d100 s42 checkpoint verify

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_sft_d100_s42_checkpoint_verify_20260516T015846_result.json`
- **Structured JSON:** [`1350de748b732eb4985a.json`](../../sessions/13/1350de748b732eb4985a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

### exp_001_sft_3B_d100_s42_a32_v3 → **DONE (success)**
- Checkpoint: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter/`
- `lora_alpha=32`, `adapter_model.safetensors` = 114 MB
- Train loss: 1.18, token accuracy: 0.72, 4159 steps, ~4.9h

### exp_002_signals_05B_s123_batch → **DONE (failed)**
- 脚本 `run_05B_s123_signals.sh` 不存在，EXIT_CODE=127，从未实际运行
- GPU 1 当前空闲，无 PID

---
