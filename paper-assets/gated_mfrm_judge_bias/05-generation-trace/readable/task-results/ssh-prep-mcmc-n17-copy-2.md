# ssh prep mcmc n17

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_prep-mcmc-n17_20260524T173612_result.json`
- **Structured JSON:** [`034f618726a9b63d91f5.json`](../../sessions/03/034f618726a9b63d91f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run completed successfully. All 4 methods ran, model compiled, data loaded correctly. Convergence "failed" as expected with only 10 warmup/10 samples — that's normal for a dry-run.

Key results:

**Data summary:**
- N=18 target models (17 original + qwen3-8b probe), I=355 items, J=6 judges
- 26,154 observations after filtering mistral-large-2 (43 obs removed)
- Judge coverage: llama-3.3-70b 79%, qwen2.5-72b 78.5%, qwen3-235b 81.5%, claude-sonnet 68.5%, deepseek 54.8%, gemini 47.1%

**Dry-run timing (1 chain, 10+10):**
- raw_average: 0s, mfrm_only: 11s (mostly JAX compilation), sequential: 5s, joint_gmfrm: 7s
- Total: 24s

**Full run time estimate:**
- The 2000x extrapolation (from 20→40000 effective samples) is very rough. More realistic estimate: JAX compilation dominates the dry-run (~10s), so actual scaling is lower.
- Based on prior exp003 runs with similar N/I/J dimensions, expect **2-4 hours** for the full 4-method run (6000 warmup + 4000 samples × 4 chains, sequential chain method).

**Arena τ correlation (dry-run, unreliable with 10 samples):**
- raw_average: τ=0.712, ρ=0.879
- mfrm_only: τ=0.471, ρ=0.641
- sequential: τ=0.471, ρ=0.644
- joint_gmfrm: τ=0.706, ρ=0.868

The τ values will change substantially with proper MCMC samples; the dry-run just validates the pipeline runs end-to-end.

**Script ready at:** `/root/gated_mfrm_judge_bias/run_mcmc_n17_exp020.py`

**To launch full run:**
```bash
CUDA_VISIBLE_DEVICES=0 nohup python run_mcmc_n17_exp020.py \
  --output-dir /root/gated_mfrm_judge_bias/exp003/output_n17_exp020 \
  > /root/gated_mfrm_judge_bias/logs/exp020_mcmc.log 2>&1 &
```

---
