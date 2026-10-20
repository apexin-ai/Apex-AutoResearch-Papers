# code exp 020 prep

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_020_prep_20260523T043542_result.json`
- **Structured JSON:** [`a71fff5e7c8933eb0484.json`](../../sessions/a7/a71fff5e7c8933eb0484.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_020 code prep complete. Summary:

**Files created on server** (`/root/spectral_collapse_ews/`):
- `run_gpt2m_phase1.py` — GPT-2-medium runner (reuses `src.pipeline`, no existing code modified)
- `prepare_data_gpt2m.py` — re-tokenizes Pile with GPT-2 tokenizer
- `dry_run_gpt2m.py` — CPU dry-run test
- `scripts/launch_gpt2medium_r0_seed42.sh` — launch script

**Dry-run**: all tests passed on CPU. Model loads (354.8M params, hidden=1024, 24 layers), forward+backward works, embedding extraction + SVD spectral metrics work, text generation works.

**Key findings**:
- No pipeline code changes needed — `src/*.py` is fully model-agnostic
- Data needs re-tokenization (different BPE vocabulary)
- GPU memory: ~5.9 GB (vs 72-78 GB free)
- Estimated wall time: ~2h/gen, ~20-22h total (10 gens)
- Running experiments (exp_018/019) verified unaffected

**Launch command**:
```bash
nohup bash /root/spectral_collapse_ews/scripts/launch_gpt2medium_r0_seed42.sh &lt;GPU_ID> \
  > /root/spectral_collapse_ews/logs/exp_020_gpt2m_r0_s42.log 2>&1 &
```

---
