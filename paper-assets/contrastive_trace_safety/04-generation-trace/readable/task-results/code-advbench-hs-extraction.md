# code advbench hs extraction

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_advbench_hs_extraction_20260519T193710_result.json`
- **Structured JSON:** [`b4cf7de23de5c5f99533.json`](../../sessions/b4/b4cf7de23de5c5f99533.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both scripts verified. Summary:

**`src/advbench/extract_hidden_states.py`**
- Extracts L0-L24 (25 of 33 layers) from R1-8B
- Output: `artifacts/hidden_states_all25/{trace_id}.pt` — dict with `hidden_states: [T, 25, 4096]` fp16 + metadata
- Dry-run confirmed: `[57, 25, 4096]`, `[38, 25, 4096]`
- Supports `--dry-run`, `--start/--end`, `--batch-size`

**`src/advbench/extract_text_embeddings.py`**
- Uses all-MiniLM-L6-v2 (384d)
- Output: `artifacts/r1_8b_text_emb_all.pkl` — dict `trace_id → ndarray(T, 384)` float32
- Format matches existing `r1_8b_text_emb.pkl`
- Dry-run confirmed: `(57, 384)`, `(38, 384)`

324 traces total. Full extraction commands:
```bash
cd /root/autodl-tmp/contrastive_trace_safety
source /etc/network_turbo
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# HS extraction (~1-2 min per trace with GPU)
python -m src.advbench.extract_hidden_states

# Text embeddings (~30s total)
python -m src.advbench.extract_text_embeddings
```

---
