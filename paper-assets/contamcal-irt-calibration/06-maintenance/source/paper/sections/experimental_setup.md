## 4 Experimental Setup

### 4.1 Controlled SFT Injection

We construct a controlled contamination testbed using the Qwen2.5 model family at three scales: 0.5B, 1.5B, and 3B parameters. For each scale, we fine-tune with LoRA ($\alpha = 32$) on a general-purpose SFT corpus into which we inject benchmark items at four dosage levels: d000 (0%, clean control), d005 (5%), d025 (25%), and d100 (100%). Benchmark items are formatted as instruction-response pairs and mixed into the training corpus at the specified proportions. All injected items pass a quality-control filter that removes ambiguous or malformed entries.

We train each configuration with two random seeds (s42 and s123), yielding $J = 24$ models across 3 scales $\times$ 4 dosages $\times$ 2 seeds. This within-family design isolates contamination dosage as the primary experimental variable while controlling for architecture, tokenizer, and pretraining data.

Qwen2.5-0.5B exhibits severe position bias under logprob-based multiple-choice evaluation (d000 A-rate = 46%, d100 A-rate = 98%). We exclude 0.5B MMLU and ARC data from all IRT analyses. The 0.5B GSM8K results (free-form generation, unaffected by position bias) remain included. This exclusion is discussed further in Section 6.

### 4.2 Cross-Family Analysis

To test whether contamination patterns are family-specific, we fine-tune Llama-3.2-3B under the same protocol (d000, d005, d025, d100) with a single seed, yielding $J = 4$ additional models. This analysis is **exploratory**: the single-seed design provides limited statistical power. We report post-hoc power calculations using Qwen $J = 24$ effect sizes as reference (e.g., MMLU Math $\gamma = 0.97$).

Llama-3.2-3B at d100 on MMLU exhibits catastrophic format collapse: all outputs default to option "A" (accuracy = 0.34). This configuration is excluded from IRT fitting. ARC and GSM8K at d100 behave normally. The effective Llama MMLU dosage range is d000 to d025.

### 4.3 Benchmarks, Domains, and Evaluation

We evaluate on three benchmarks that span distinct cognitive demands and response formats.

**MMLU** (Hendrycks et al., 2021): 14,042 multiple-choice items across 57 subjects. We group these subjects into 8 cognitive domains by functional similarity: Math, Science, CS & Engineering, Medical, Humanities, Social Sciences, Business & Law, and Other. This domain stratification is central to our analysis, as it reveals within-benchmark heterogeneity that aggregate scoring obscures (Section 5.1).

**ARC-Challenge** (Clark et al., 2018): 1,172 multiple-choice science reasoning items.

**GSM8K** (Cobbe et al., 2021): 1,319 open-ended mathematical problem-solving items. The free-form generation format avoids multiple-choice artifacts and provides a format contrast to MMLU and ARC.

We assess performance with six metrics. For *calibration quality*: mean absolute error (MAE) between calibrated and ground-truth clean accuracy, and Kendall $\tau$ for rank preservation across models. For *uncertainty quality*: 95% credible interval coverage. For *model diagnostics*: posterior predictive $p$-value (PPP $\in [0.1, 0.9]$ indicates acceptable fit), $\gamma$ significance (whether the 95% CI excludes zero), and $\hat{R}$ convergence ($< 1.01$).

### 4.4 Baselines

We compare against seven baselines. **B0-Raw** reports original benchmark accuracy with no adjustment. **B1-Remove&Rescore** drops items flagged as contaminated and rescores on the remainder. **B2-Single2PL+$\gamma$** fits a single aggregate $\gamma$ without domain stratification, testing whether per-domain modeling is necessary. **B3-Vanilla4PL** fits standard 4PL IRT with no contamination parameter ($\gamma = 0$), isolating the calibration contribution of IRT ability estimation from the contamination covariate. **B4-LinearRegression** regresses score residuals on exposure scores, testing whether the full IRT machinery is necessary. **B5-Emperor** applies representative mitigation strategies (item rephrasing and option shuffling) from the Emperor's New Clothes study (ICML 2025), which demonstrated that all 20 tested mitigation methods fail to restore clean performance. **B6-DCR** uses the Data Contamination Report adjusted accuracy (Oren et al., 2024), the only prior method that produces decontaminated score estimates.
