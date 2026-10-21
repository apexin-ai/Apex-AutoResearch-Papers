# code llama2 base control setup

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama2_base_control_setup_20260517T045040_result.json`
- **Structured JSON:** [`e3b7320c2450f9dca65e.json`](../../sessions/e3/e3b7320c2450f9dca65e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

OK, I'll stop polling now. The download is clearly progressing at a steady ~290 MB/min. Here's the full status report:

---

## Summary

### Completed:
1. **Weight mapping confirmed** — OpenVLA's LLM keys are `language_model.{llama2_key}`. Direct 1:1 mapping with `language_model.` prefix.

2. **Vocab mismatch handled** — OpenVLA has 32064 tokens (32000 + 64 action bins). For `embed_tokens` and `lm_head`: first 32000 rows from Llama-2 base, extra 64 rows kept from trained OpenVLA.

3. **Scripts written**:
   - **`/root/vla-ssd/scripts/create_llama2_base_openvla.py`** — Standalone checkpoint creation. Loads both models' state dicts, injects Llama-2 base weights into `language_model.*`, saves sharded safetensors.
   - **`/root/vla-ssd/scripts/cross_instruction_extract_dense.py`** — Modified to accept `--condition llama2base` (loads Llama-2 base at runtime, same as existing `untrained` pattern).

4. **Server ready** — 2x RTX PRO 6000 (98GB), PyTorch 2.10, CUDA, safetensors 0.7.0.

### In progress:
- **Llama-2-7B downloading** from `NousResearch/Llama-2-7b-hf` via hf-mirror.com (Meta gated model → used community copy). ~3.2GB / ~13.5GB done. **ETA: ~35 min** (PID 768142).
- Saved to: `/root/autodl-tmp/hf_cache/models--NousResearch--Llama-2-7b-hf/`

### After download completes, run:
```bash
# Find the snapshot path
SNAP=$(ls /root/autodl-tmp/hf_cache/models--NousResearch--Llama-2-7b-hf/snapshots/)
# Create checkpoint
/root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/create_llama2_base_openvla.py \
  --openvla_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b \
  --llama2_path /root/autodl-tmp/hf_cache/models--NousResearch--Llama-2-7b-hf/snapshots/$SNAP \
  --output_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-llama2base
```

Or skip the checkpoint and run the probe directly:
```bash
/root/miniconda3/bin/python3.12 /root/vla-ssd/scripts/cross_instruction_extract_dense.py \
  --condition llama2base --dry-run
```

### No blockers — just waiting on download.

---
