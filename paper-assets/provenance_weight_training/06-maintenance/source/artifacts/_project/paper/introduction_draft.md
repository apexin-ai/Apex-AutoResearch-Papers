# Introduction

Web corpora increasingly contain machine-generated text.
Recent estimates place the synthetic fraction at 20--60% of crawled data \citep{cheng_2025_contamination_survey}, and this share grows as language models are deployed for content production at scale.
Training on such contaminated data has concrete consequences: \citet{shumailov_2024_model_collapse} show that recursive training on model outputs leads to irreversible quality degradation---*model collapse*---and \citet{dohmatob_2025_strong_collapse} prove under scaling-law regimes that even a vanishingly small synthetic fraction suffices to trigger this failure mode, ruling out data scaling as a remedy.
A central difficulty is that the contamination proportion in any given corpus is unknown: synthetic text enters through diverse, uncoordinated channels with no centralized provenance record.
The prevalence, severity, and opacity of synthetic contamination make contamination-aware pretraining a practical necessity.

A natural response is *detect-and-reweight*: train a classifier to estimate each sample's synthetic probability $q(x)$, then suppress likely-synthetic samples via the weighting function $w(x) = (1 - q(x))^b$.
\citet{drayson_2025_detection_collapse} demonstrate this approach for model collapse prevention and show that the exponent $b$ critically determines outcomes---their optimal values range from $b=10$ for models at $\leq$360M parameters to $b=1$ at 1.7B, and misspecification degrades results substantially.
Selecting $b$ therefore requires per-model validation-set grid search, with computational cost scaling linearly in the number of candidates (six training runs in a typical sweep).
Other approaches assume even stronger supervision: \citet{he_2025_golden_ratio} derive theoretically optimal weights from convergence analysis but require the exact contamination ratio $\rho$, which is precisely what is unavailable in practice.
Hard detection-and-removal strategies \citep{feng_2025_beyond_collapse} discard borderline samples entirely, sacrificing the smooth reweighting that continuous $q$-scores enable.

Given per-sample detector scores $q(x)$, how should one choose $b$ without a validation set or known contamination proportion?
We formulate this as a dual-constraint optimization over each training batch: find the smallest $b$ that ensures the weighted effective real proportion $\alpha_{\mathrm{eff}}(b)$ reaches a quality threshold $\tau$, while keeping Kish's effective sample size $\mathrm{ESS}(b)$ above a stability floor $n_{\min}$.
The quality constraint has theoretical grounding: convergence rate under contaminated training improves with the effective real-data fraction \citep{wang_2026_survive_contamination}, motivating a lower bound on $\alpha_{\mathrm{eff}}$.
The stability constraint prevents extreme weight concentration that degrades gradient quality.
These two requirements exhibit a natural opposition.
$\alpha_{\mathrm{eff}}(b)$ increases monotonically in $b$ (Proposition 1), yielding a lower bound $b_\tau$---the minimum exponent needed to achieve the target quality.
$\mathrm{ESS}(b)$ decreases monotonically, yielding an upper bound $b_{\mathrm{ESS}}$---the maximum exponent before gradient stability degrades.
The adaptive exponent $b^* = b_\tau$ when the feasible region $[b_\tau, b_{\mathrm{ESS}}]$ is non-empty, embodying a *minimum intervention principle*: apply the least downweighting sufficient to meet the quality target, preserving as much effective training data as possible.
When the constraints conflict ($b_\tau > b_{\mathrm{ESS}}$), the stability ceiling takes precedence.

This minimum-intervention semantics distinguishes the method from the alternative of maximizing $b$ subject only to ESS stability.
Among batches that require reweighting, the dual-constraint solver selects $b^*$ via the $\alpha_{\mathrm{eff}}$ bound in 40% of cases, with mean $b^*=1.67$; the ESS-only variant would choose $b=4.15$ in these same batches, 2.5$\times$ more aggressive.
The remaining 49.9% of batches have sufficient real-data content to skip reweighting entirely ($b^*=0$).
The per-batch $b^*$ distribution (median 0.87, mean 1.40) adapts continuously to each batch's contamination composition without any held-out signal.

On Qwen3-0.6B continued pretraining with 40% synthetic contamination (132M+ tokens from FineWeb), adaptive reweighting achieves mean held-out perplexity of 17.651 across three seeds, matching the grid-searched optimum ($b=0.5$, mean 17.646) within seed-to-seed variance (Section 5).
The grid sweep requires six complete training runs to identify this optimum; the adaptive method requires one.
The ESS-only variant (maximum intervention) yields mean PPL 17.723---worse than the uniform baseline (17.694)---confirming that maximum intervention degrades training while minimum intervention improves it.
A lightweight TF-IDF + Logistic Regression detector (AUC = 0.939, calibrated ECE = 0.048) suffices throughout, suggesting that score calibration matters more than raw classification accuracy for provenance-based reweighting.

Our contributions are as follows:

1. A dual-constraint framework for adaptive exponent selection: $b^* = \inf\{b \geq 0 : \alpha_{\mathrm{eff}}(b) \geq \tau\}$ subject to $\mathrm{ESS}(b) \geq n_{\min}$, computed per-batch from detector scores with minimum-intervention semantics (Section 3).
2. Empirical evidence that adaptive $b^*$ matches grid-searched best within seed variance at zero validation cost, and that minimum intervention (dual constraint) outperforms maximum intervention (ESS-only) across three seeds (Section 5).
3. A demonstration that a lightweight TF-IDF + LR detector with calibrated $q$-scores supports effective reweighting, achieving results comparable to stronger neural detectors (Section 5).
