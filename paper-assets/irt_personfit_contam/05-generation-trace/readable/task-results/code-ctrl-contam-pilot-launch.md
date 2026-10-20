# code ctrl contam pilot launch

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ctrl-contam-pilot-launch_20260520T153005_result.json`
- **Structured JSON:** [`0bfbfd287cc829a61f00.json`](../../sessions/0b/0bfbfd287cc829a61f00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All steps complete:

1. **Model download**: Qwen2.5-7B-Instruct downloaded via ModelScope (4 safetensors, ~14.6GB)
2. **Verification**: Model path resolves, tokenizer loads (vocab=151643)
3. **train.py fix**: Updated for TRL 1.4.0 API — `TrainingArguments` → `SFTConfig`, `max_seq_length` → `max_length`
4. **Dry-run**: 2 steps passed (loss=1.943, 9.6 samples/sec)
5. **4 training jobs submitted** via `submit_training_job`:
   - `exp-ctrl-contam-pilot-clean-s1` → GPU 0 (5000 samples, seed=42)
   - `exp-ctrl-contam-pilot-clean-s2` → GPU 1 (5000 samples, seed=123)
   - `exp-ctrl-contam-pilot-contam-15` → GPU 2 (7106 samples, seed=42)
   - `exp-ctrl-contam-pilot-contam-50` → GPU 3 (12021 samples, seed=42)
6. **Registry**: `exp-ctrl-contam-pilot` updated to RUNNING with full spec metadata

Estimated training time: clean conditions ~939 steps × ~1.1s/step ≈ 17 min; contam_50 ~2260 steps ≈ 42 min.

---
