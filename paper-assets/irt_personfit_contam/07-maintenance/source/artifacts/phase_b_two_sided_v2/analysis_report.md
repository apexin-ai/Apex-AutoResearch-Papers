# Two-sided Detection v2 — Analysis Report

## Method
- **θ estimation**: Benchmark-specific MLE (not global PSN-IRT θ)
- **Null distribution**: Parametric bootstrap (N=1000) per cell
- **Multiple testing**: Benjamini-Hochberg FDR at α=0.05

## Key Results

### Flagging rate: 57/60 (95.0%)

v1 flagged 56/60 (93.3%) using global θ + |lz*|>1.96 threshold.
v2 flags 57/60 (95.0%) after correcting θ estimation and using empirical null with BH-FDR.

The flagged rate remains high (95.0%) even after correcting θ estimation. This means the v1 over-flagging was NOT primarily due to global θ bias — the 4PL IRT model genuinely does not fit LLM response patterns at the item level.

The lz* values are extreme (|lz*| >> 2 for most cells), and even 1000 bootstrap replicates under the 4PL model cannot reproduce such deviations. This is strong evidence that LLM responses violate 4PL assumptions:
  - Local independence: LLMs have correlated item responses (knowledge clusters)
  - Unidimensionality: even within a single benchmark, LLM abilities are multi-faceted
  - Monotonicity: LLMs may exhibit non-monotonic response patterns on certain items

### Gemini-1.5 on MMLU
- Accuracy: 100% (θ_bench = 4.0, boundary value)
- lz*: 31.815
- Empirical p-value: 0.0
- Flagged (BH): True

Gemini-1.5 achieves 100% on MMLU, pushing θ_bench to the boundary (4.0). At boundary θ, lz* may be unreliable because the MLE is constrained — the Fisher information correction in lz* assumes an interior optimum. The bootstrap null appropriately handles this: bootstrap replicates can also hit the boundary, so the empirical p-value remains valid even when the asymptotic N(0,1) approximation breaks down.

### Calibration gap: global θ vs benchmark-specific θ

| Benchmark | Mean gap (θ_bench − θ_global) | Std | Min | Max |
|-----------|-------------------------------|-----|-----|-----|
| arc_c | +0.430 | 1.259 | -2.106 | +2.541 |
| gsm8k | +0.227 | 1.004 | -1.136 | +2.860 |
| hellaswag | +0.405 | 1.054 | -1.150 | +2.571 |
| humaneval | +0.230 | 1.294 | -2.106 | +3.043 |
| mmlu | +0.361 | 0.911 | -0.350 | +3.223 |

The gap between global and benchmark-specific θ varies substantially across benchmarks, confirming that a single global θ misrepresents model ability on individual benchmarks. However, the high flagging rate persists even with benchmark-specific θ, meaning the calibration gap is a secondary issue — the primary issue is 4PL model misfit.

### Per-benchmark detail

**arc_c** (n_items=295)
  - 360GPT2-Pro: θ_global=1.459, θ_bench=4.000, acc=0.963, lz*=2.898, p_emp=0.0080, p_adj=0.0092 **FLAGGED**
  - DeepSeek-V3: θ_global=3.772, θ_bench=2.460, acc=0.925, lz*=3.022, p_emp=0.0020, p_adj=0.0026 **FLAGGED**
  - Doubao-pro: θ_global=1.140, θ_bench=1.098, acc=0.885, lz*=2.324, p_emp=0.0250, p_adj=0.0268 **FLAGGED**
  - Gemini-1.5: θ_global=0.777, θ_bench=1.261, acc=0.898, lz*=2.050, p_emp=0.0460, p_adj=0.0484 **FLAGGED**
  - Gemma-2B-it: θ_global=-3.378, θ_bench=-2.374, acc=0.451, lz*=6.214, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Hunyuan-Turbo: θ_global=1.732, θ_bench=4.000, acc=0.966, lz*=3.569, p_emp=0.0010, p_adj=0.0014 **FLAGGED**
  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-0.878, acc=0.702, lz*=5.597, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Moonshot-v1: θ_global=0.926, θ_bench=1.621, acc=0.915, lz*=2.746, p_emp=0.0070, p_adj=0.0082 **FLAGGED**
  - Qwen-Plus: θ_global=0.957, θ_bench=2.121, acc=0.925, lz*=2.851, p_emp=0.0070, p_adj=0.0082 **FLAGGED**
  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=0.155, acc=0.844, lz*=3.434, p_emp=0.0010, p_adj=0.0014 **FLAGGED**
  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-4.000, acc=0.237, lz*=2.979, p_emp=0.0020, p_adj=0.0026 **FLAGGED**
  - Yi-Lightning: θ_global=0.772, θ_bench=0.466, acc=0.841, lz*=1.664, p_emp=0.0950, p_adj=0.0983

**gsm8k** (n_items=1319)
  - 360GPT2-Pro: θ_global=1.459, θ_bench=2.184, acc=0.901, lz*=7.216, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - DeepSeek-V3: θ_global=3.772, θ_bench=4.000, acc=0.951, lz*=7.894, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Doubao-pro: θ_global=1.140, θ_bench=4.000, acc=0.914, lz*=2.650, p_emp=0.0120, p_adj=0.0131 **FLAGGED**
  - Gemini-1.5: θ_global=0.777, θ_bench=0.386, acc=0.779, lz*=-7.773, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Gemma-2B-it: θ_global=-3.378, θ_bench=-4.000, acc=0.132, lz*=10.019, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Hunyuan-Turbo: θ_global=1.732, θ_bench=0.780, acc=0.814, lz*=6.749, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-1.364, acc=0.423, lz*=11.658, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Moonshot-v1: θ_global=0.926, θ_bench=1.250, acc=0.861, lz*=7.799, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Qwen-Plus: θ_global=0.957, θ_bench=1.708, acc=0.882, lz*=7.174, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=0.115, acc=0.739, lz*=10.821, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-3.030, acc=0.175, lz*=8.630, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Yi-Lightning: θ_global=0.772, θ_bench=1.471, acc=0.875, lz*=6.030, p_emp=0.0000, p_adj=0.0000 **FLAGGED**

**hellaswag** (n_items=10042)
  - 360GPT2-Pro: θ_global=1.459, θ_bench=2.734, acc=0.913, lz*=16.040, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - DeepSeek-V3: θ_global=3.772, θ_bench=2.622, acc=0.905, lz*=14.808, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Doubao-pro: θ_global=1.140, θ_bench=1.074, acc=0.861, lz*=17.739, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Gemini-1.5: θ_global=0.777, θ_bench=1.144, acc=0.874, lz*=-15.303, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Gemma-2B-it: θ_global=-3.378, θ_bench=-3.613, acc=0.291, lz*=23.931, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Hunyuan-Turbo: θ_global=1.732, θ_bench=4.000, acc=0.952, lz*=20.420, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-1.362, acc=0.530, lz*=31.855, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Moonshot-v1: θ_global=0.926, θ_bench=3.497, acc=0.930, lz*=13.234, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Qwen-Plus: θ_global=0.957, θ_bench=0.382, acc=0.794, lz*=8.241, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=0.007, acc=0.766, lz*=18.862, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-1.679, acc=0.476, lz*=28.378, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Yi-Lightning: θ_global=0.772, θ_bench=0.829, acc=0.848, lz*=18.010, p_emp=0.0000, p_adj=0.0000 **FLAGGED**

**humaneval** (n_items=164)
  - 360GPT2-Pro: θ_global=1.459, θ_bench=1.806, acc=0.860, lz*=1.504, p_emp=0.1320, p_adj=0.1342
  - DeepSeek-V3: θ_global=3.772, θ_bench=4.000, acc=0.915, lz*=2.348, p_emp=0.0120, p_adj=0.0131 **FLAGGED**
  - Doubao-pro: θ_global=1.140, θ_bench=0.554, acc=0.750, lz*=2.529, p_emp=0.0100, p_adj=0.0113 **FLAGGED**
  - Gemini-1.5: θ_global=0.777, θ_bench=-0.244, acc=0.543, lz*=-3.128, p_emp=0.0020, p_adj=0.0026 **FLAGGED**
  - Gemma-2B-it: θ_global=-3.378, θ_bench=-3.350, acc=0.183, lz*=3.823, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Hunyuan-Turbo: θ_global=1.732, θ_bench=4.000, acc=0.939, lz*=2.831, p_emp=0.0050, p_adj=0.0062 **FLAGGED**
  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-1.644, acc=0.341, lz*=4.231, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Moonshot-v1: θ_global=0.926, θ_bench=1.171, acc=0.823, lz*=3.808, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Qwen-Plus: θ_global=0.957, θ_bench=4.000, acc=0.927, lz*=2.813, p_emp=0.0060, p_adj=0.0073 **FLAGGED**
  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=0.134, acc=0.726, lz*=3.523, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-4.000, acc=0.140, lz*=3.063, p_emp=0.0020, p_adj=0.0026 **FLAGGED**
  - Yi-Lightning: θ_global=0.772, θ_bench=1.110, acc=0.823, lz*=1.354, p_emp=0.1810, p_adj=0.1810

**mmlu** (n_items=14042)
  - 360GPT2-Pro: θ_global=1.459, θ_bench=1.748, acc=0.831, lz*=19.789, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - DeepSeek-V3: θ_global=3.772, θ_bench=3.422, acc=0.867, lz*=18.236, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Doubao-pro: θ_global=1.140, θ_bench=1.410, acc=0.844, lz*=-21.333, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Gemini-1.5: θ_global=0.777, θ_bench=4.000, acc=1.000, lz*=31.815, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Gemma-2B-it: θ_global=-3.378, θ_bench=-3.077, acc=0.335, lz*=24.701, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Hunyuan-Turbo: θ_global=1.732, θ_bench=1.505, acc=0.821, lz*=16.565, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Mistral-7B-Instruct-v0.1: θ_global=-1.365, θ_bench=-1.168, acc=0.533, lz*=34.901, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Moonshot-v1: θ_global=0.926, θ_bench=0.873, acc=0.779, lz*=20.216, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Qwen-Plus: θ_global=0.957, θ_bench=1.399, acc=0.819, lz*=36.154, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Qwen2.5-3B-Instruct: θ_global=-0.125, θ_bench=-0.303, acc=0.653, lz*=26.193, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Vicuna-7B-v1.3: θ_global=-1.894, θ_bench=-2.109, acc=0.391, lz*=27.390, p_emp=0.0000, p_adj=0.0000 **FLAGGED**
  - Yi-Lightning: θ_global=0.772, θ_bench=1.401, acc=0.819, lz*=36.128, p_emp=0.0000, p_adj=0.0000 **FLAGGED**

## Methodological finding

Switching from global to benchmark-specific θ corrects the ability estimation bias but does NOT resolve the high flagging rate. This reveals a deeper issue: the 4PL IRT model is fundamentally inadequate for modeling LLM response patterns.

LLM responses violate core IRT assumptions even within homogeneous benchmarks. The massive lz* values (often 10-30+) indicate systematic, not marginal, misfit. This has implications for any IRT-based contamination detection method — the signal-to-noise ratio of person-fit statistics is dominated by model misfit, making it difficult to isolate genuine contamination signals.

The parametric bootstrap with benchmark-specific θ provides the most rigorous calibration available within the 4PL framework. The persistent flagging is therefore a property of the LLM-IRT interaction, not a statistical artifact.
