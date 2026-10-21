# harvest grpo cka only 25 wandb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_grpo_cka_only_25_wandb_20260521T195612_result.json`
- **Structured JSON:** [`1d88bc4fc3ff253948cc.json`](../../sessions/1d/1d88bc4fc3ff253948cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

有 7/10 步完整数据（40/50/60 因 SSH 输出截断缺失）。结合 wandb-summary，可以完成分析。

从已有数据和 ROADMAP 交叉验证，整理完整结果：

## grpo_cka_only_25 Training Metrics (run mirgxi5b)

### Training Curve (7/10 steps, steps 40-60 truncated in SSH output)

| Step | Reward | Reward_std | frac_zero_std | Loss | KL | Entropy | Completion_len | Grad_norm |
|------|--------|-----------|---------------|------|------|---------|----------------|-----------|
| 10 | 0.2537 | 0.3988 | 0.275 | 0.0174 | 0.00154 | 0.1031 | 281.1 | 3.766 |
| 20 | 0.2050 | 0.3295 | 0.500 | 0.0485 | 0.00182 | 0.0950 | 283.4 | 3.438 |
| 30 | 0.1956 | 0.3528 | 0.225 | 0.0604 | 0.00178 | 0.0959 | 296.8 | 2.797 |
| 40-60 | — | — | — | — | — | — | — | — |
| 70 | 0.2838 | 0.4300 | 0.175 | 0.0041 | 0.00155 | 0.0869 | 307.3 | 1.875 |
| 80 | **0.3175** | 0.4474 | **0.125** | 0.1654 | 0.00171 | 0.0847 | 302.5 | 2.406 |
| 90 | 0.2413 | 0.3726 | 0.300 | 0.0741 | 0.00161 | 0.0836 | 287.0 | 2.578 |
| 100 | 0.2875 | 0.4330 | 0.275 | 0.1117 | 0.00180 | 0.0952 | 273.3 | 3.312 |

### Key Indicators

```json
{
  "run_id": "mirgxi5b",
  "run_name": "grpo_sft_cka_only_25",
  "config": {
    "sparsity": "25%",
    "pruning_method": "cka_only",
    "max_steps": 100,
    "lr": 1e-6,
    "beta": 0.01,
    "temperature": 0.4,
    "seed": 42,
    "loss_type": "dapo",
    "num_generations": 4,
    "gradient_accumulation_steps": 8,
    "max_completion_length": 512
  },
  "summary": {
    "final_reward": 0.2875,
    "peak_reward": 0.3175,
    "peak_step": 80,
    "final_frac_zero_std": 0.275,
    "best_frac_zero_std": 0.125,
    "final_loss": 0.1117,
    "final_kl": 0.00180,
    "final_entropy": 0.0952,
    "runtime_seconds": 1267,
    "gsm8k_accuracy": 0.5959,
    "math500_accuracy": 0.184
  },
  "trajectory_pattern": "active_learning",
  "trajectory_notes": "Dip at step 20-30 (frac_zero=0.50→0.225), recovery to peak at step 80 (reward=0.318, frac_zero=0.125), oscillation 80-100. NOT collapse, NOT stagnation."
}
```

### Comparison with Known Results

| Method | Sparsity | Final Reward | Peak Reward | GSM8K | Pattern |
|--------|----------|-------------|-------------|-------|---------|
| **CKA-only** | **25%** | **0.288** | **0.318** | **59.59%** | **Active learning** |
| Standard | 25% | ~0.05 | — | 51.86% | Reward stagnation |
| RASP | 25% | — | — | 53.15% | — |
| CKA-only | 20% | 0.344 | 0.354 | 64.39% | Active learning |

### Analysis

1. **Active learning confirmed**: CKA-only 25% shows the same active-learning pattern as CKA-only 20% — dip-then-recover, NOT collapse. Peak reward 0.318 at step 80, final 0.288.

2. **CKA-only >> Standard at 25%**: +7.73pp GSM8K advantage (59.59% vs 51.86%). This is the **largest gap** across all sparsity levels tested, confirming CKA-only advantage increases with sparsity.

3. **Reward vs Standard**: CKA-only final reward ~0.288 vs Standard ~0.05 stagnation — qualitatively different training dynamics.

4. **Degradation from 20%→25%**: Reward drops from 0.344→0.288, GSM8K from 64.39%→59.59% (−4.8pp). Graceful degradation, not cliff.

5. **frac_zero_std**: Transient spike at step 20 (0.50) recovers quickly — not a persistent collapse signal.

6. **W&B issue**: Run uploaded to wrong project (`huggingface`), needs `wandb sync --project recovery_aware_struct_prune` to fix.

7. **Missing steps 40-60**: SSH output truncated. If needed, can SSH to server to read full `trainer_state.json`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "run_id": "mirgxi5b",
    "run_name": "grpo_sft_cka_only_25",
    "config": {
      "sparsity": "25%",
      "pruning_method": "cka_only",
      "max_steps": 100,
      "lr": 1e-06,
      "beta": 0.01,
      "temperature": 0.4,
      "seed": 42,
      "loss_type": "dapo",
      "num_generations": 4,
      "gradient_accumulation_steps": 8,
      "max_completion_length": 512
    },
    "summary": {
      "final_reward": 0.2875,
      "peak_reward": 0.3175,
      "peak_step": 80,
      "final_frac_zero_std": 0.275,
      "best_frac_zero_std": 0.125,
      "final_loss": 0.1117,
      "final_kl": 0.0018,
      "final_entropy": 0.0952,
      "runtime_seconds": 1267,
      "gsm8k_accuracy": 0.5959,
      "math500_accuracy": 0.184
    },
    "trajectory_pattern": "active_learning",
    "trajectory_notes": "Dip at step 20-30 (frac_zero=0.50→0.225), recovery to peak at step 80 (reward=0.318, frac_zero=0.125), oscillation 80-100. NOT collapse, NOT stagnation."
  }
}
```

</details>

---
