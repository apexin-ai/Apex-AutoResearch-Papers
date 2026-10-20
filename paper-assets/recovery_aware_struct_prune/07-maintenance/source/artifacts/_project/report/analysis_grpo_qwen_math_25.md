# GRPO Qwen2.5-Math-7B 25% Sparsity Analysis

**Date**: 2026-05-16
**Experiments**: grpo_rasp_25_qwen_math, grpo_standard_25_qwen_math
**Server**: westd-11672 (cuda:2, cuda:3)
**W&B**: 3vjjzi13 (RASP), 16vqw4e6 (Standard)

## 1. Training Metrics (10-step resolution)

### RASP 25% (grpo_rasp_25_qwen_math)

| Step | reward | frac_0std | comp_len | kl | loss | entropy |
|------|--------|-----------|----------|------|------|---------|
| 10 | 0.112 | 0.575 | 772.7 | 0.002 | 0.006 | 0.117 |
| 20 | 0.203 | 0.250 | 811.9 | 0.002 | 0.045 | 0.109 |
| 30 | 0.125 | 0.550 | 801.0 | 0.026 | 0.004 | 0.107 |
| 40 | 0.184 | 0.375 | 784.4 | 0.002 | 0.076 | 0.098 |
| 50 | 0.177 | 0.300 | 763.3 | 0.045 | 0.035 | 0.099 |
| 60 | 0.183 | 0.350 | 743.1 | **725** | **49.7** | 0.107 |
| 70 | 0.199 | 0.375 | 750.7 | 0.002 | 0.027 | 0.112 |
| 80 | 0.225 | 0.400 | 758.3 | 0.002 | 0.079 | 0.104 |
| 90 | 0.111 | 0.375 | 753.2 | 0.002 | 0.055 | 0.115 |
| 100 | 0.206 | 0.350 | 811.9 | 0.004 | 0.068 | 0.090 |

**Pattern**: Stable training. Reward flat ~0.11-0.23. One transient KL spike at step 60 (725), immediately recovers. frac_zero_std 0.575→0.35 (improving). No collapse.

### Standard 25% (grpo_standard_25_qwen_math)

| Step | reward | frac_0std | comp_len | kl | loss | entropy |
|------|--------|-----------|----------|------|------|---------|
| 10 | 0.201 | 0.375 | 510.5 | 0.005 | 0.090 | 0.240 |
| 20 | 0.163 | 0.400 | 531.6 | **56** | **2.6** | 0.230 |
| 30 | 0.106 | 0.425 | 594.6 | 0.005 | 0.061 | 0.243 |
| 40 | 0.211 | 0.300 | 515.7 | **7.9e15** | **3.7e14** | 0.248 |
| 50 | 0.159 | 0.325 | 515.1 | 0.006 | 0.069 | 0.244 |
| 60 | 0.208 | 0.350 | 460.0 | 0.005 | 0.101 | 0.255 |
| 70 | 0.190 | 0.375 | 544.4 | 0.005 | 0.074 | 0.236 |
| 80 | 0.209 | 0.275 | 533.8 | **4.1e6** | **2.2e5** | 0.262 |
| 90 | 0.174 | 0.225 | 576.7 | 0.026 | 0.121 | 0.245 |
| 100 | 0.182 | 0.325 | 527.0 | 0.298 | 0.165 | 0.238 |

**Pattern**: Recurrent catastrophic KL explosions (steps 20, 40, 80). Each time self-recovers within 10 steps. Despite KL reaching 7.9e15, reward stays stable ~0.11-0.21 and frac_zero_std actually improves (0.375→0.225→0.325). No reward collapse.

## 2. Comparison with 20% Qwen Math GRPO (v3 runs)

### RASP 20% (grpo_rasp_qwen_math_v3)

| Step | reward | frac_0std | comp_len | kl | loss | entropy |
|------|--------|-----------|----------|------|------|---------|
| 10 | 0.049 | 0.650 | 1015 | 0.064 | 0.000 | 0.077 |
| 50 | 0.069 | 0.675 | 1013 | 0.010 | 0.009 | 0.071 |
| 100 | 0.061 | 0.675 | 1006 | 0.009 | -0.002 | 0.078 |

**20% RASP**: Permanent collapse. reward 0.05-0.10, frac_zero_std 0.55-0.70, comp_len maxed ~1003-1024, entropy very low 0.07.

### Standard 20% (grpo_standard_qwen_math_v3)

| Step | reward | frac_0std | comp_len | kl | loss | entropy |
|------|--------|-----------|----------|------|------|---------|
| 10 | 0.063 | 0.750 | 943 | 0.051 | 0.015 | 0.200 |
| 30 | 0.031 | 0.900 | 931 | 0.006 | -0.005 | 0.198 |
| 100 | 0.044 | 0.850 | 921 | 0.005 | -0.012 | 0.175 |

**20% Standard**: Severe permanent collapse. reward 0.03-0.07, frac_zero_std 0.75-0.90.

## 3. Cross-Sparsity Comparison (Same Model)

| Metric | RASP 20% | RASP 25% | Std 20% | Std 25% |
|--------|----------|----------|---------|---------|
| reward (final) | 0.061 | **0.206** | 0.044 | **0.182** |
| reward (peak) | 0.083 | **0.225** | 0.069 | **0.211** |
| frac_0std (final) | 0.675 | **0.350** | 0.850 | **0.325** |
| frac_0std (range) | 0.55-0.70 | **0.25-0.575** | 0.75-0.90 | **0.225-0.425** |
| comp_len (final) | 1006 | 812 | 921 | 527 |
| entropy (final) | 0.078 | **0.090** | 0.175 | **0.238** |
| KL spikes | none | 1 (step 60) | none | **3** (steps 20,40,80) |
| collapse_pattern | permanent | **none** | permanent | **KL explosions** |

**Key finding: 25% is BETTER than 20% across all collapse metrics.** This is the opposite of the expected sparsity gradient.

## 4. Cross-Model Comparison (DeepSeek vs Qwen Math)

| Pattern | DeepSeek 20% | Qwen Math 20% | Qwen Math 25% |
|---------|-------------|---------------|---------------|
| RASP collapse | permanent (frac→0.95) | permanent (frac 0.55-0.70) | **no collapse** (frac 0.25-0.575) |
| Standard collapse | transient dip + recovery | **permanent** (frac 0.75-0.90) | KL explosions, no reward collapse |
| RASP vs Standard | RASP worse | **Standard worse** | Standard more unstable |

**RASP vs Standard direction reverses between models**: On DeepSeek RASP collapses worse; on Qwen Math Standard collapses worse.

## 5. Conclusion

### Verdict: NEGATIVE (both experiments)

The sparsity gradient hypothesis (C3: more sparsity → worse collapse) is **contradicted**:

1. **25% < 20% in collapse severity** — reward is 3-4x higher, frac_zero_std is substantially lower at 25% than 20%. Higher sparsity paradoxically produces better GRPO outcomes on Qwen Math.

2. **RASP vs Standard direction inconsistent** — On DeepSeek, RASP collapses worse. On Qwen Math at 20%, Standard collapses worse. At 25%, neither shows classic collapse (Standard shows KL instability instead).

3. **New failure mode**: Standard 25% introduces catastrophic KL explosions (up to 7.9e15) that are qualitatively different from reward collapse. The model survives these through DAPO's clipping, but the optimization trajectory is severely disrupted.

### Why 25% might be better than 20%

Possible explanations (require further investigation):
- **SFT recovery quality**: The 25% SFT models may have converged to a better point for GRPO
- **Model capacity**: More aggressive pruning may force the model into a more constrained but more stable optimization landscape
- **Completion length**: 20% models generate maxed-out completions (~1024 tokens) suggesting degenerate repetitive behavior; 25% models generate shorter, more diverse completions

### Impact on Paper Claims

| Claim | Status after this experiment |
|-------|------------------------------|
| C1: RASP causes permanent GRPO collapse | **Model-dependent** — holds for DeepSeek and Qwen 20%, NOT for Qwen 25% |
| C2: Standard causes transient collapse | **Model-dependent** — on Qwen Math, Standard shows WORSE collapse at 20%, KL explosions at 25% |
| C3: Higher sparsity → worse collapse | **CONTRADICTED** — 25% Qwen Math is better than 20% |
| New: Collapse is model-specific | **Supported** — DeepSeek and Qwen show qualitatively different patterns |
| New: KL explosion as alternative failure mode | **Observed** — Standard 25% shows recurrent KL blowups not seen in other experiments |

### Recommended Next Steps

1. Run 25% GRPO on DeepSeek (grpo_rasp_25, already PREPARING) to test if sparsity gradient holds within-model
2. Investigate SFT checkpoint quality differences between 20% and 25% (eval scores, perplexity)
3. Consider whether 100 steps is sufficient — 25% models may simply be slower to manifest collapse

## 6. Checkpoints

- RASP 25%: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25_qwen_math/` (checkpoint-100)
- Standard 25%: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math/` (checkpoint-100)
