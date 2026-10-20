# ALFWorld Llama Restart v2 Report

**Date**: 2026-05-20 16:37 UTC
**Server**: westb-13313
**GPU**: cuda:0 (RTX 5090, 32GB)

## Status: RUNNING

## What happened
- Original run crashed at 68/135 episodes
- GPU 0 had stale python process (PID 709893, 26.8 GiB) — killed
- Script had no resume support (deletes output file on start)

## Changes made
1. **Backed up existing data**: `episodes.jsonl` → `episodes_68.jsonl.bak` (68 episodes preserved)
2. **Added resume logic** to `src/alfworld_counterfactual.py`:
   - Reads completed `task_id`s from existing output file
   - Skips already-completed episodes
   - Appends new results (no file deletion)
3. **Lowered `gpu_memory_utilization`**: 0.85 → 0.75 (vLLM v1 multiprocess engine was failing with OOM on startup)
4. **Added `enforce_eager=True`**: avoids CUDA graph memory overhead

## Launch details
- tmux session: `alfworld-v2`
- Log: `logs/alfworld_llama_v2.log`
- Output: `results/alfworld_llama_counterfactual/episodes.jsonl`
- Command: `CUDA_VISIBLE_DEVICES=0 python src/alfworld_counterfactual.py --model_path /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --output results/alfworld_llama_counterfactual/episodes.jsonl --n_tasks 0 --gpu_id 0 --seed 42`

## Verification
- Resume confirmed: "Resuming: 68 episodes already completed", 68 SKIPs logged
- vLLM loaded successfully on GPU 0 (24.4 GiB, 96% utilization)
- Inference active (~90 toks/s output)
- GPU 1 untouched (0 MiB)
- Remaining: 67 episodes to process
