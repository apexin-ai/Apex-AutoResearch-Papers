# GPU Cleanup + Dual Experiment Restart Report

**Date**: 2026-05-20 15:01 UTC  
**Server**: westb-13313 (2x RTX 5090 32GB)

## Step 1: GPU Cleanup

- Killed orphan vLLM processes (PIDs 532172, 532006 → respawned as 534791, 534804 → respawned again)
- Root cause: tmux sessions managing Python→vLLM process trees kept respawning
- Fix: `tmux kill-server` + kill entire process tree
- **Result**: Both GPUs at 0 MiB

## Step 2: Code Fix — System Role Compatibility

**File**: `src/llm_agent.py` → `sanitize_messages_for_template()`

- **Before**: String matching (`'System role not supported' in chat_template`) — fragile, misses Gemma's error format
- **After**: Try-except approach — tries `apply_chat_template()`, catches system role errors, merges system content into first user message
- Also added `tensor_parallel_size` parameter to `LLMAgent.__init__` for compatibility with remote `episode_level_collection.py` (793-line version)
- `alfworld_counterfactual.py` imports the same function, no changes needed

## Step 2.5: Dry-run Verification

- Model: Gemma-2-9B-IT on GPU 1
- Task: ScienceWorld "boil", 1 episode, 10 max steps
- **Result**: PASSED — no system role errors, episode completed (internal=0.0, det=0.0, label=no-preference)

### Bug Found During First Restart Attempt

- `CUDA_VISIBLE_DEVICES=1` in shell + `--gpu_id 0` caused code to override env var (`os.environ["CUDA_VISIBLE_DEVICES"] = "0"`)
- Gemma loaded on GPU 0 instead of GPU 1, conflicting with Llama
- **Fix**: Remove `CUDA_VISIBLE_DEVICES` from shell command, use `--gpu_id 1` directly

## Step 3: Dual Experiment Restart

### 3A: GPU 0 — Llama ALFWorld Counterfactual
- **Command**: `python src/alfworld_counterfactual.py --model_path /root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct --output results/alfworld_llama_counterfactual/episodes.jsonl --n_tasks 0 --gpu_id 0 --seed 42`
- **tmux session**: `alfworld`
- **GPU memory**: 28017 MiB / 32607 MiB

### 3B: GPU 1 — Gemma ScienceWorld Counterfactual
- **Command**: `python src/episode_level_collection.py --model_path /root/autodl-tmp/models/gemma-2-9b-it/AI-ModelScope/gemma-2-9b-it --task_types "boil,melt,freeze,change-the-state-of-matter-of" --episodes 20 --output_dir results/gemma_scienceworld_counterfactual --gpu_id 1 --seed 42`
- **tmux session**: `gemma`
- **GPU memory**: 27681 MiB / 32607 MiB

## Step 4: Verification

| Check | Status |
|-------|--------|
| GPU 0 has Llama vLLM (PID 547473) | OK |
| GPU 1 has Gemma vLLM (PID 547990) | OK |
| `alfworld` tmux session alive | OK |
| `gemma` tmux session alive | OK |
| No cross-GPU contamination | OK |

## Step 5: Registry

- `alfworld-llama-counterfactual` → RUNNING
- `gemma-scienceworld-counterfactual` → RUNNING
