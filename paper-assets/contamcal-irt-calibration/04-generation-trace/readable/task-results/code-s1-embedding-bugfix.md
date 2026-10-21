# code s1 embedding bugfix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_s1_embedding_bugfix_20260517T032324_result.json`
- **Structured JSON:** [`bb1b9c9ab9ee32819d15.json`](../../sessions/bb/bb1b9c9ab9ee32819d15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Fix verified. Here's the summary:

## Bug Report

**File**: `/root/contamcal-irt-calibration/exp002/signals/s1_embedding.py:54`

**Root cause**: When `adapter_path=None` (merged/full-fine-tune models like Llama), the original code unconditionally defaulted `dosage="000"` without checking if the dosage could be inferred from `model_path`. This caused merged checkpoint paths like `.../Llama-3.2-3B_d025_s42/merged` to compare against `sft_dosage_000.jsonl` instead of the correct `sft_dosage_025.jsonl`.

**Impact**: Cross-family Llama signals computed from merged models would all use d000 training data reference, making all dosage levels appear identical in s1 — corrupting the IRT signal differentiation.

**Fix** (lines 54-64):
```python
if adapter_path:
    dosage = infer_dosage_from_path(adapter_path) or "000"
else:
    # No adapter: infer dosage from model_path (handles merged checkpoints)
    from pathlib import Path
    dosage = None
    if model_path:
        dosage = infer_dosage_from_path(model_path)
        if not dosage:
            dosage = infer_dosage_from_path(str(Path(model_path).parent))
    dosage = dosage or "000"
```

**Verified**: 8 scenarios pass (Qwen+adapter, Llama merged d025/d100/d000, Llama raw base, Qwen Instruct, Llama adapter cases).

---
