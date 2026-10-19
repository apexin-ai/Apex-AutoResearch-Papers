# research advbench data check

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_advbench_data_check_20260522T092720_result.json`
- **Structured JSON:** [`c1a1d29a72e2c141876e.json`](../../sessions/c1/c1a1d29a72e2c141876e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full status report:

## 1. AdvBench prompts
**Not present.** `/root/autodl-tmp/contrastive_trace_safety/data/` directory does not exist. No `advbench/` directory or prompt files anywhere.

## 2. R1-8B AdvBench reasoning traces
**No AdvBench-specific traces found.** `find` for `*advbench*` returned empty across both `data/` and `artifacts/`.

## 3. Existing hidden states (HarmThoughts, not AdvBench)
- `artifacts/hidden_states_r1_8b_full/` — **209 .pt files, 1.9 GB total**
- These are from the **HarmThoughts** dataset (`ishitakakkar-10/HarmThoughts`), not AdvBench
- Each .pt file is a per-trace hidden state extraction (all 25 layers, L0–L24, dim=4096)
- Also present: `artifacts/ensemble_cv_results.json` (5-fold CV results), `artifacts/random_cp_control/`

## 4. Disk space
| Filesystem | Size | Used | Avail | Use% |
|---|---|---|---|---|
| `/dev/md0` | 250G | 18G | **233G free** | 7% |

Plenty of space for AdvBench experiments.

## 5. Model availability
**R1-8B is cached in two locations:**
- `/root/autodl-tmp/models/r1_8b/deepseek-ai/DeepSeek-R1-Distill-Llama-8B/` (15 GB)
- `/root/autodl-tmp/.hf_cache/hub/models--deepseek-ai--DeepSeek-R1-Distill-Llama-8B/` (HF cache)

No need to re-download.

## 6. Existing scripts
Server-side scripts in `/root/autodl-tmp/contrastive_trace_safety/scripts/`:
- `extract_hs_r1_8b.py` — HarmThoughts hidden state extraction (reference for AdvBench script)
- `n7_ensemble_loocv.py` — ensemble CV validation
- `random_cp_control_r1_8b.py` — random changepoint control
- `run_r1_8b_pipeline.sh` — pipeline runner

**No AdvBench-specific scripts** exist yet. No `src/` directory.

## 7. GPU
| GPU | VRAM | Used |
|---|---|---|
| **NVIDIA RTX PRO 6000 Blackwell Server Edition** | **97,887 MiB (~96 GB)** | 0 MiB |

GPU is idle and has massive VRAM — can easily hold the 8B model (~16GB in fp16) with room for long-context inference.

## Summary
**What's available:** R1-8B model weights (cached), 96GB GPU (idle), 233GB free disk, existing HarmThoughts extraction script as template.

**What's missing:** AdvBench prompts, AdvBench reasoning traces, AdvBench hidden states, AdvBench extraction script. Everything AdvBench-related needs to be created from scratch.

---
