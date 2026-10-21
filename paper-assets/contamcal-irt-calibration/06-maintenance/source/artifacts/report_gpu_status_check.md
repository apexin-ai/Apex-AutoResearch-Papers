# GPU Status Check 2026-05-16 (00:04 UTC)

## Summary
**All 6 GPUs ACTIVE** — all original PIDs alive and running. System reporting "idle" for cuda:0/2/4/5 was incorrect.

| GPU | Status | PID | Experiment | Runtime | Memory | GPU-Util | Notes |
|-----|--------|-----|-----------|---------|--------|----------|-------|
| cuda:0 | **Running** | 804570 | Llama-3.2-3B d005 SFT | 32min | 16252/24564 MiB | 86% | Output: `checkpoints/Llama-3.2-3B_d005_s42/lora_adapter` (in progress) |
| cuda:1 | **Running** | 807025 | Llama-3.2-3B d000 eval v3 (aligned) | 30min | 6913/24564 MiB | 80% | Benchmarks: gsm8k, arc_challenge, humaneval. Output so far: `eval_results/Llama-3.2-3B_d000_s42_aligned/mmlu_results.json` |
| cuda:2 | **Running** | 797754 | Qwen2.5-0.5B-Instruct eval | 1h22min | 1511/24564 MiB | 0% (idle burst) | Benchmarks: mmlu, gsm8k, humaneval. Output so far: `eval_results/Qwen2.5-0.5B-Instruct/{gsm8k,mmlu}_results.json` |
| cuda:3 | **Running** | 801766 | Llama-3.2-3B d025 SFT | 56min | 17853/24564 MiB | 100% | Output: `checkpoints/Llama-3.2-3B_d025_s42/lora_adapter` (in progress) |
| cuda:4 | **Running** | 810809 | 1.5B-Instruct MMLU signals | 15min | 3951/24564 MiB | 45% | Computing all signals for MMLU. Partial output: `signals/Qwen2.5-1.5B-Instruct/` (embedding+minkpp+selfcritique done for arc/gsm8k, mmlu chunked in progress) |
| cuda:5 | **Running** | 804791 | Llama-3.2-3B d100 SFT | 32min | 20585/24564 MiB | 84% | Output: `checkpoints/Llama-3.2-3B_d100_s42/lora_adapter` (in progress) |

## Output Paths
- SFT checkpoints: `/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d{005,025,100}_s42/`
- Llama d000 eval: `/root/autodl-tmp/exp001/eval_results/Llama-3.2-3B_d000_s42_aligned/`
- 0.5B eval: `/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct/`
- 1.5B signals: `/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/`

## Notes
- cuda:2 shows 0% GPU-util but process is alive (1h22m runtime) — likely in CPU-bound eval phase (e.g., HumanEval code execution) or between benchmark transitions
- All 3 Llama SFT jobs (d005/d025/d100) only have `lora_adapter/` dir — no `merged/` yet, meaning training is still in LoRA phase before merge step
- System误报 cuda:0/2/4/5 idle 可能是 resource_usage 工具的 PID/tmux 不匹配问题 (参见 C002)
