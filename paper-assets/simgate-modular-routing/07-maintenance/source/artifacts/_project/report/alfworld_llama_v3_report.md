# ALFWorld Llama v3 Restart Report

**Date**: 2026-05-20 16:54 UTC
**Server**: westb-13313 (RTX 5090 × 2)
**tmux session**: `alfworld_v3`

## Changes Made

- Added `enable_prefix_caching=False` to `src/alfworld_counterfactual.py` line 165 (vLLM LLM() constructor)
- `src/llm_agent.py` already had this parameter — no change needed

## Launch Command

```bash
CUDA_VISIBLE_DEVICES=0 python src/alfworld_counterfactual.py \
  --model_path /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct \
  --output results/alfworld_llama_counterfactual/episodes.jsonl \
  --gpu_id 0 --n_tasks 0
```

## Verification (3 min post-launch)

| Check | Result |
|-------|--------|
| GPU 0 memory | 24401 MiB / 32607 MiB |
| Process | python PID 761143 |
| EngineCore died | **No** |
| Model loaded | Llama-3.1-8B-Instruct, bf16, 14.99 GiB |
| enable_prefix_caching | False (confirmed in vLLM log) |
| Existing episodes | 68 (preserved) |
| Total games | 135 (67 remaining) |
| First new game | #69 pick_clean_then_place (SoapBar → Toilet) |
| GPU 1 | Not touched (Gemma running) |

## Notes

- `--output` expects a file path, not directory (fixed from initial `--output_dir` error)
- `--n_tasks 0` processes all 135 available games (default was 10)
- Script auto-resumes: skips 68 completed episodes, continues from #69
