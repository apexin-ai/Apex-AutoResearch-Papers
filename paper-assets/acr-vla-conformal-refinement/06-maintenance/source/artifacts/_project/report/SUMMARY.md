# Rank-Deficient Covariance Analysis (plan_302)

- Suite: **LIBERO-object**, tasks=5, init/task=4, decision points N=20

- Action representation: H_eff=5 × pose_dim=6 = **30-D flattened**

- Ground truth: K_max=64 SmolVLA samples per decision point; K ∈ [6, 10, 16, 20, 32, 50] estimated via 32 bootstrap subsamples each


## 1. Numerical rank of the 30×30 sample covariance

| K | rank median | rank max | log10 cond# (median) | log10 cond# (p90) |
|---|-------------|----------|----------------------|-------------------|
| 6 | 5 | 5 | 19.32 | 20.21 |
| 10 | 9 | 9 | 19.03 | 19.90 |
| 16 | 15 | 15 | 18.66 | 19.50 |
| 20 | 19 | 19 | 18.51 | 19.37 |
| 32 | 30 | 30 | 5.65 | 6.63 |
| 50 | 30 | 30 | 4.17 | 4.65 |
| 64 | 30 | 30 | 3.95 | 4.38 |

- **K=10 → rank ≤ 9 < 30** ⇒ the 30D sample covariance is structurally rank-deficient. The 21 'missing' eigen-directions carry no information about the underlying VLA action distribution; any downstream feature that projects onto them is pure noise.

- The condition number explodes at low K because the smallest non-zero eigenvalue is dominated by sampling noise. Ledoit-Wolf shrinkage (used in CGS) regularizes the inverse but does **not** recover the missing rank — it merely smooths the diagonal.


## 2. Per-DOF std estimation error vs K

| K | mean \|rel err\| | median \|rel err\| | p90 \|rel err\| |
|---|------------------|---------------------|------------------|
| 6 | 0.258 | 0.223 | 0.524 |
| 10 | 0.187 | 0.158 | 0.387 |
| 16 | 0.138 | 0.116 | 0.286 |
| 20 | 0.118 | 0.099 | 0.244 |
| 32 | 0.079 | 0.067 | 0.162 |
| 50 | 0.041 | 0.034 | 0.082 |

- At **K=10**, per-DOF std estimates have ~19% mean absolute relative error compared to the K=64 ground truth, with a long tail (p90 = 39%). The empirical curve closely tracks the chi-distribution prediction of $\sigma/\sqrt{2(K-1)}\approx 0.24$ for K=10.


## 3. Which DOFs are hit hardest at K=10

| rank | horizon h | DOF d | mean \|rel err\| |
|------|-----------|-------|------------------|
| #1 (worst) | h4 | d4 | 0.241 |
| #2 (worst) | h3 | d4 | 0.228 |
| #3 (worst) | h5 | d4 | 0.216 |
| #4 (worst) | h5 | d5 | 0.213 |
| #5 (worst) | h2 | d4 | 0.201 |
| #1 (best)  | h3 | d2 | 0.162 |
| #2 (best)  | h2 | d2 | 0.167 |
| #3 (best)  | h4 | d1 | 0.168 |
| #4 (best)  | h3 | d3 | 0.168 |
| #5 (best)  | h5 | d1 | 0.169 |

- Rotational DOFs (typically d=4-6) are noisier than translational (d=1-3) because their underlying scale σ is smaller — the *relative* error grows even though the *absolute* error stays bounded.

- Later horizon steps (h=4,5) are also noisier: the flow-matching decoder accumulates uncertainty along the chunk, so later steps have more entropy and require more samples to estimate reliably.


## 4. Implications for `crm_perdof` vs `crm_obs_only`

- `crm_perdof` conditions on a 30-D per-DOF std vector (plus 5 conformal radii + 5 log volumes). At K=10 the first 30 channels have ~24% relative noise each and span a 9-D effective subspace of the 30-D embedding; the remaining 21 directions are **pure label noise** from the CRM's perspective.

- The CRM head therefore has to learn (a) which of the 30 inputs are signal vs. noise and (b) which of the 9 effective directions carries actionable uncertainty. With our LIBERO data budget this manifests as the *progressive collapse* observed during training: the model learns a near-degenerate response to the per-DOF channels and overfits to the scalar conformal radius.

- `crm_obs_only` removes this 40-D conformal feature entirely. The remaining VLM observation embedding (~960-D) is high-SNR (no K-sample variance) and the CRM head learns a cleaner correction function. This is precisely the gap we measured: obs_only outperforms perdof not because conformal information is useless, but because **at K=10 the per-DOF conformal estimate is too noisy to provide a positive learning signal**.

- Practical recipe: either (i) raise K to ≥50 to make per-DOF stds reliable, accepting 5x inference cost; or (ii) replace the 30-D channel with a **rank-aware** summary (e.g., log-volume + top-r principal directions of the 30×30 covariance, r ≤ K-1), which keeps the conditioning informative without forcing the CRM to learn through 21 noise dimensions.
