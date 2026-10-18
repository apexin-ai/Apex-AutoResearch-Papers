# code remaining 48h scripts

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_remaining_48h_scripts_20260516T024849_result.json`
- **Structured JSON:** [`c7d9a896953e3562f053.json`](../../sessions/c7/c7d9a896953e3562f053.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 scripts pass syntax validation. Summary:

**Long context 8K evals (3 scripts):**
| Script | Model | Profile source | Attention patch |
|---|---|---|---|
| `run_qwen_longcontext_8k.py` | Qwen2.5-7B | `hires_profiles.json` (2/4/8-bit) | standard `patch_attention` |
| `run_phi3_longcontext_8k.py` | Phi-3-medium-14B | `artifacts/phi3_medium_profiles_hires.json` (2-bit, synthesize 4/8) | standard `patch_attention` |
| `run_internlm2_longcontext_8k.py` | InternLM2-7B | `artifacts/internlm2_profiles_hires.json` (2-bit, synthesize 4/8) | inline `patch_attention_internlm2` (fused wqkv) |

**3-seed downstream CI (3 scripts):**
| Script | Model | Profile pattern | Attention patch |
|---|---|---|---|
| `run_yi_3seed_downstream_ci.py` | Yi-1.5-9B | `yi15_multi_seed_profiles_s{0,1,2}.json` | standard `patch_attention` |
| `run_mistral_3seed_downstream_ci.py` | Mistral-7B-v0.3 | `mistral_multi_seed_profiles_s{0,1,2}.json` | standard `patch_attention` |
| `run_gemma2_3seed_downstream_ci.py` | Gemma-2-9B | `gemma2_multi_seed_profiles_s{0,1,2}.json` | `patch_attention_gemma2` (from `run_gemma2_full_pipeline`) |

**Skipped:** `run_codellama_hires_profiling.py` — already exists.

All scripts support `--gpu`, output JSON to `artifacts/`, and have docstrings describing inputs/outputs. The 3-seed downstream scripts expect pre-generated per-seed profile files (same pattern as the existing Qwen 3-seed CI).

---
