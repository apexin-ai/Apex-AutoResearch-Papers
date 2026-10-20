# GRPO Qwen2.5-Math-7B v3 Analysis: Standard vs RASP 20%

**Date**: 2026-05-16
**Experiments**: grpo_standard_qwen_math_v3 (5n2snh48) / grpo_rasp_qwen_math_v3 (yyg9ty4u)
**Server**: westd-11672, 100 steps, save_steps=100
**Config**: beta=0.04, temp=0.4, lr=5e-7, loss_type=dapo, repetition_penalty=1.15

---

## 1. Key Metrics Time Series

### Standard 20% (5n2snh48)

| Step | reward | frac_zero_std | entropy | grad_norm | kl | clipped_ratio |
|------|--------|---------------|---------|-----------|------|---------------|
| 10 | 0.063 | 0.750 | 0.200 | 10.5 | 0.051 | 0.881 |
| 20 | 0.044 | 0.850 | 0.193 | 1.87 | 0.005 | 0.888 |
| 30 | 0.031 | **0.900** | 0.198 | 0.19 | 0.006 | 0.863 |
| 40 | 0.039 | 0.875 | 0.178 | 0.29 | 0.010 | — |
| 50 | 0.033 | 0.825 | 0.192 | 0.22 | 0.006 | — |
| 60 | 0.033 | 0.825 | 0.191 | **172** | 0.029 | — |
| 70 | 0.045 | 0.825 | 0.190 | 0.26 | 0.006 | — |
| 80 | **0.069** | **0.750** | 0.171 | **130** | 0.011 | 0.831 |
| 90 | 0.038 | 0.825 | 0.189 | 0.15 | 0.006 | 0.856 |
| 100 | 0.044 | 0.850 | 0.175 | 0.40 | 0.005 | 0.856 |

**Summary**: reward range [0.031, 0.069], frac_zero_std range [0.75, 0.90], entropy ~0.18

### RASP 20% (yyg9ty4u)

| Step | reward | frac_zero_std | entropy | grad_norm | kl | clipped_ratio | mean_len |
|------|--------|---------------|---------|-----------|------|---------------|----------|
| 10 | 0.049 | 0.650 | **0.077** | 0.73 | 0.064 | 0.988 | 1015 |
| 20 | 0.083 | 0.625 | 0.066 | 1.91 | 0.221 | 0.994 | 1020 |
| 30 | 0.059 | **0.550** | 0.077 | 6.91 | 0.008 | 0.994 | 1019 |
| 40 | **0.102** | 0.575 | 0.073 | 1.87 | 0.007 | 0.975 | 1003 |
| 50 | 0.069 | 0.675 | 0.071 | 2.92 | 0.010 | 0.988 | 1013 |
| 60 | 0.071 | 0.575 | 0.072 | 3.27 | 0.005 | 0.969 | 1003 |
| 70 | 0.091 | 0.575 | 0.073 | 4.81 | 0.014 | 0.975 | 1003 |
| 80 | 0.056 | 0.700 | 0.079 | 14.9 | 0.016 | **1.000** | **1024** |
| 90 | 0.048 | 0.575 | 0.069 | 5.72 | 0.007 | 0.975 | 1003 |
| 100 | 0.061 | 0.675 | 0.078 | 1.62 | 0.009 | 0.975 | 1006 |

**Summary**: reward range [0.048, 0.102], frac_zero_std range [0.55, 0.70], entropy ~0.073, clipped_ratio ~0.98

---

## 2. Collapse Analysis

### Standard 20%: Persistent Reward-Homogeneity Collapse

- **frac_zero_std** stays in [0.75, 0.90] throughout — 75-90% of batches have zero reward variance (all samples same reward)
- Peak collapse at step 30 (frac_zero_std=0.90), partial improvement to 0.75 at step 80, then returns to 0.85
- Reward low but non-zero (0.031-0.069), never crashes to zero
- Entropy remains healthy (~0.18): the model generates diverse text, but it's all equally wrong (or right)
- Two grad_norm spikes (step 60: 172, step 80: 130) suggest intermittent large updates but no sustained improvement
- **Pattern**: persistent reward-signal starvation, NOT the transient dip+recovery seen in Llama Standard

### RASP 20%: Entropy Collapse + Length Pathology (NOT reward collapse)

- **Entropy** at 0.066-0.079 — 2.5x lower than Standard's 0.18. Model generates highly repetitive outputs.
- **clipped_ratio** 0.97-1.00: nearly all completions hit max length (1024 tokens). Model cannot terminate properly.
- **frac_zero_std** at 0.55-0.70 — paradoxically LOWER than Standard. More batches have reward variance.
- Reward at 0.048-0.102 — comparable to or higher than Standard. Model still solves some problems.
- No reward crash, no frac_zero_std spike — fundamentally different from Llama RASP.
- **Pattern**: diversity/termination collapse, not reward collapse. RASP damage manifests as mode collapse in output space rather than inability to solve problems.

---

## 3. Cross-Model Comparison with Llama-3.2-3B

| Metric | Llama Standard 20% | Qwen Standard 20% | Llama RASP 20% | Qwen RASP 20% |
|--------|--------------------|--------------------|----------------|----------------|
| Collapse type | Transient dip→recovery | Persistent high frac_zero_std | Permanent reward collapse | Entropy/length collapse |
| frac_zero_std | Dip ~0.6→recovery | 0.75-0.90 persistent | →0.95 (permanent) | 0.55-0.70 (moderate) |
| Reward | Dip step60→recovery step90 | 0.03-0.07 flat | →0.039 (stuck) | 0.05-0.10 (functional) |
| Entropy | — | ~0.18 (healthy) | — | ~0.07 (collapsed) |
| Clipped ratio | — | ~0.86 | — | ~0.98 (near-max) |
| Collapse onset | Step ~60 | Step 1 | Step ~10 | Step 1 (entropy) |
| Recovery | Yes (step ~90) | No | No | No |

### Key Differences

1. **Llama showed reward collapse; Qwen shows signal-quality collapse.** Llama RASP couldn't solve any problems (reward→0). Qwen RASP still solves problems but generates pathologically repetitive, non-terminating outputs.

2. **Standard pattern inverted.** Llama Standard showed a clean transient dip+recovery. Qwen Standard is stuck in high frac_zero_std from step 1 with no clear recovery arc.

3. **Damage signature differs by model capacity.** Qwen2.5-Math-7B (7B, math-specialized) has enough capacity to maintain base problem-solving under RASP damage, but the damage manifests in output diversity instead. Llama-3.2-3B (3B, general) lacks this buffer.

---

## 4. Comparison with Qwen 25% Sparsity

| | Standard 20% | Standard 25% | RASP 20% | RASP 25% |
|---|---|---|---|---|
| reward | 0.03-0.07 | 0.10-0.21 | 0.05-0.10 | 0.11-0.23 |
| frac_zero_std | 0.75-0.90 | 0.23-0.43 | 0.55-0.70 | 0.25-0.58 |
| entropy | ~0.18 | ~0.24 | ~0.07 | ~0.10 |
| clipped_ratio | ~0.86 | ~0.34 | ~0.98 | ~0.67 |
| KL stability | Stable | Catastrophic spikes | Stable | Mostly stable |

**Paradox**: 25% sparsity performs BETTER than 20% in reward and frac_zero_std. This is counterintuitive and suggests the 20% pruning pattern cuts more critical structures than 25% for this model. Likely a model-specific pruning sensitivity profile rather than a monotonic sparsity-collapse relationship.

---

## 5. Conclusions

### C2 Cross-Model Validation: **PARTIAL FAILURE**

- **Standard collapse gradient**: NOT replicated. Llama showed transient dip+recovery; Qwen shows persistent high frac_zero_std without recovery. Pattern qualitatively different.
- **RASP permanent collapse**: Partially replicated but mechanism differs. Qwen RASP shows permanent entropy/length collapse but NOT reward collapse. The model fails differently.

### What IS Validated

- RASP and Standard produce **distinct** collapse signatures in GRPO — this holds across models. The damage type (RASP vs Standard pruning) does affect GRPO dynamics differently.
- Both models show that pruned models struggle with GRPO compared to expected full-model behavior. The general phenomenon of pruning-induced GRPO fragility is cross-model consistent.

### What Is NOT Validated

- The specific Llama collapse signatures (reward crash, frac_zero_std→0.95 for RASP; transient dip+recovery for Standard) are NOT reproduced in Qwen.
- The collapse mechanism appears model-dependent, potentially correlated with base model capability (math-specialized 7B vs general 3B).

### Recommendation

- The paper should frame the finding as "pruning-method-dependent GRPO fragility" rather than claiming specific collapse signatures generalize across models.
- The Qwen RASP entropy collapse is a distinct finding worth reporting: RASP damage in stronger models manifests as mode collapse rather than reward collapse.
- Consider the 20% vs 25% paradox — may need model-specific pruning sensitivity analysis.

---

## 6. Artifact Metadata

- **Standard checkpoint**: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math/`
- **RASP checkpoint**: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math/`
- **Standard log**: `~/runs/recovery_aware_struct_prune/grpo_standard_qwen_math_v3.log`
- **RASP log**: `~/runs/recovery_aware_struct_prune/grpo_rasp_qwen_math_v3.log`
- **W&B**: [Standard](https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/5n2snh48) | [RASP](https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/yyg9ty4u)
