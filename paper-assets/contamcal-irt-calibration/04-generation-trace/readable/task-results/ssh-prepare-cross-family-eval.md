# ssh prepare cross family eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prepare-cross-family-eval_20260519T052405_result.json`
- **Structured JSON:** [`def6974a2565d46bc670.json`](../../sessions/de/def6974a2565d46bc670.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Script verified. Here's the summary:

## Verification Results

**Server**: westd-29999 confirmed (4× NVIDIA RTX PRO 6000 Blackwell, 97887 MiB each)

**All 8 checkpoints verified** (adapter_model.safetensors present, lora_alpha=32):

| Family | Dosage | .done | Status |
|--------|--------|-------|--------|
| gemma-2-9b | d000 | No | Adapter exists, usable |
| gemma-2-9b | d005 | Yes | Ready |
| gemma-2-9b | d025 | Yes | Ready |
| gemma-2-9b | d050 | Yes | Ready |
| phi-4 | d000 | Yes | Ready |
| phi-4 | d005 | Yes | Ready |
| phi-4 | d025 | Yes | Ready |
| OLMo-2-7B | d000 | Yes | Ready |

**No existing eval results** for any cross-family model.

## Script

**Path**: `/root/contamcal-irt-calibration/exp001/run_eval_cross_family_batch.sh`

**Usage**: `bash run_eval_cross_family_batch.sh &lt;GPU_ID>` (defaults to GPU 0)

Key design notes:
- Corrected CLI args vs task description: uses `--model-path` (not `--model-name`), `--benchmarks mmlu arc_challenge` (not `--benchmark`), `--output-dir` (not `--output-path`). No `--shots` flag needed (hardcoded in evaluate.py).
- Runs both MMLU + ARC in a single invocation per checkpoint (model loaded once, not twice).
- Skips if adapter missing or `.done` already exists (safe to re-run).
- Explicit `CUDA_VISIBLE_DEVICES=$GPU` per C004.
- Output: `/root/autodl-tmp/exp001/eval_results_cross_family/&lt;family>_&lt;dosage>_s42/`
- 8 checkpoints = 8 sequential eval runs.

---
