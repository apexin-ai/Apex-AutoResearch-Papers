# code 48h remaining scripts

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_48h_remaining_scripts_20260516T025323_result.json`
- **Structured JSON:** [`d5839bd1c58f099c6992.json`](../../sessions/d5/d5839bd1c58f099c6992.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 7 scripts pass syntax validation. Summary:

**Already existed (verified correct):**
- `run_phi3_longcontext_8k.py` — Phi-3-medium-14B, 2-bit-only profiles + synthesis, `trust_remote_code=False`
- `run_internlm2_longcontext_8k.py` — InternLM2-7B, custom `patch_attention_internlm2`, fused wqkv handling
- `run_yi_3seed_downstream_ci.py` — Yi-1.5-9B, k=8, standard `patch_attention`
- `run_mistral_3seed_downstream_ci.py` — Mistral-7B-v0.3, k=8, standard `patch_attention`
- `run_gemma2_3seed_downstream_ci.py` — Gemma-2-9B, k=8, uses `patch_attention_gemma2` (softcapping + sliding window)

**Newly created:**
- `run_qwen7b_longcontext_8k.py` — Qwen2.5-7B, loads multi-bit `hires_profiles.json` directly, k=8
- `run_codellama_longcontext_8k.py` — CodeLlama-7B (MHA, 1024 heads), 2-bit-only profiles + synthesis, standard `patch_attention`

---
