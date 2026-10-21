# code scale validation 3b setup and run

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scale_validation_3b_setup_and_run_20260522T042422_result.json`
- **Structured JSON:** [`b9aebb4513a698eddf80.json`](../../sessions/b9/b9aebb4513a698eddf80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Code modifications complete, model download in progress. Summary:

**Done:**
- `src/config/model_paths.py` — Added Qwen2.5-3B-Instruct and Qwen2.5-72B-Instruct mappings (path: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-3B-Instruct`)
- `src/inference/vllm_runner.py` — Added `tensor_parallel_size` parameter; skips `CUDA_VISIBLE_DEVICES` restriction when TP > 1
- `src/design/generate_design.py` — Added `exp003_scale` config (2 models × bf16 × 2 temps × 6 prompts × 6 seeds × 4 orderings = 576 conditions)
- `src/inference/run_experiment.py` — Added `--tensor-parallel` CLI argument
- Generated `design_matrix_exp003_3b.csv` (288 conditions for 3B only)
- Created `scripts/run_exp003_3b.sh` run script

**In progress:**
- Qwen2.5-3B-Instruct downloading via ModelScope (~600KB/s, ~2h for 5.75GB)
- Cron monitoring every 8 minutes — will auto-start inference in tmux once download completes

Expected output: `results/exp003_scale_3b_mmlu.jsonl` with 288 × 200 = 57,600 records.

---
