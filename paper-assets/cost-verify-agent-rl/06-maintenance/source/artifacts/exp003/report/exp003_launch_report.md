# exp_003 Launch Report

## Prompt Truncation
- Location: `ragen/llm_agent/ctx_manager.py`, `_apply_max_length()` (line 461-537)
- Called in all 3 code paths: limited_multi_turn (L1081), full (L1179), infer (L1272)
- Logic: tokenizer-accurate counting, preserves system prompt, removes oldest complete turns first
- No new code needed — already implemented

## Config
- max_prompt_length: 4096
- response_length: 1024
- max_model_len: 8192
- model: Qwen3-1.7B
- 128 trajectories/step (16 env_groups × 8 group_size)
- max_turn: 50, GRPO, 2 GPUs

## Dry-run Results
- Ran 1+ hour stable
- 83GB/96GB VRAM, 93% GPU utilization
- No OOM, no crashes
- Truncation effective: 50 turns would produce ~66K tokens without it

## Training Submission
- Server: bjb1-17606
- GPUs: cuda:0, cuda:1
- tmux session: exp003
- Log: ~/runs/cost-verify-agent-rl/exp003.log
- 100 steps, timeout 72h
- Estimated: ~50-60 hours