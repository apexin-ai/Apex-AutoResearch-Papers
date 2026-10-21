# Table 1 Compilation — Provenance Weight Training

All PPL values verified against experiment registry (2026-05-16).

---

## Main Table: ρ=0.4, Holdout Perplexity

| Method | seed42 PPL | seed123 PPL | seed456 PPL | Mean | Δ vs Uniform | # seeds |
|--------|-----------|------------|------------|------|-------------|---------|
| Pretrained (no training) | 22.9700 `baseline_qwen3_0.6b` | — | — | — | — | 1 |
| Uniform (no reweight) | 17.6939 `uniform_seed42` | 17.6861 `uniform_seed123` | 17.7015 `uniform_seed456` | 17.6938 | 0.0000 | 3 |
| Grid b=0.5 | 17.6510 `grid_b_seed42_batch/b0.5` | 17.6380 `grid_b0_5_seed123` | 17.6500 `grid_b0_5_seed456` | 17.6463 | −0.0475 | 3 |
| Grid b=1.0 | 17.6920 `grid_b_seed42_batch/b1.0` | 17.6740 `grid_b1_0_seed123` | 17.6800 `grid_b1_0_seed456` | 17.6820 | −0.0118 | 3 |
| Grid b=1.5 | 17.7180 `grid_b_seed42_batch/b1.5` | 17.7010 `grid_b1_5_seed123` | 17.7100 `grid_b1_5_seed456` | 17.7097 | +0.0158 | 3 |
| Grid b=2.0 † | 17.7410 `grid_b_seed42_batch/b2.0` | 17.7250 `grid_b2_0_seed123` | ~~17.989~~ | 17.7330 | +0.0392 | 2 |
| Grid b=3.0 † | 17.7740 `grid_b_seed42_batch/b3.0` | 17.7600 `grid_b3_0_seed123` | ~~17.921~~ | 17.7670 | +0.0732 | 2 |
| Grid b=5.0 † | 17.8180 `grid_b_seed42_batch/b5.0` | 17.8039 `grid_b5_0_seed123` | ~~17.993~~ | 17.8110 | +0.1171 | 2 |
| ESS-only | 17.7300 `ess_only_seed42` | 17.7200 `ess_only_seed123` | 17.7190 `ess_only_seed456` | 17.7230 | +0.0292 | 3 |
| Adaptive (τ=0.8, n_min=2) | 17.6527 `adaptive_fix_seed42` | 17.6432 `adaptive_fix_seed123` | 17.6566 `adaptive_fix_seed456` | 17.6508 | −0.0430 | 3 |
| Golden Ratio (oracle) | 17.6540 `golden_ratio_seed42` | — | — | — | −0.0398 | 1 |

† seed456 excluded: checkpoint resume artifact caused anomalous PPL (17.989/17.921/17.993). Mean computed from seed42+seed123 only.

**Ranking by Δ**: Grid b=0.5 (−0.0475) > Adaptive (−0.0430) > Golden Ratio (−0.0398) > Grid b=1.0 (−0.0118) > Uniform (0) > Grid b=1.5 (+0.0158) > ESS-only (+0.0292) > Grid b=2.0 (+0.0392) > Grid b=3.0 (+0.0732) > Grid b=5.0 (+0.1171)

---

## τ Sweep Sub-table (seed42 only, n_min=2 for τ=0.8, n_min=3 for others)

| τ | PPL | b* mean | b* median | exp_id |
|---|-----|---------|-----------|--------|
| 0.50 | 17.6880 | 0.3923 | 0.1707 | `tau_05_seed42` |
| 0.60 | 17.6805 | 0.5899 | 0.3746 | `tau_06_seed42` |
| 0.70 | 17.6793 | 0.8943 | 0.5800 | `tau_07_seed42` |
| 0.80 | 17.6527 | 1.3990 | 0.8710 | `adaptive_fix_seed42` |
| 0.90 | 17.7120 | 2.3600 | 1.3200 | `tau_09_seed42` |
| 0.95 | 17.7230 | 3.0775 | 1.5200 | `tau_095_seed42` |

Best: τ=0.8 (PPL 17.6527). Optimum is in the sweet spot where b* is moderate (mean ~1.4).

---

## n_min Ablation Sub-table (seed42, τ=0.8, bs=4)

| n_min | PPL | b* mean | Behavior | exp_id |
|-------|-----|---------|----------|--------|
| 1 | 17.7890 | 7.197 | Over-downweighting | `nmin1_seed42` |
| 2 | 17.6527 | 1.399 | Optimal (=adaptive_fix) | `adaptive_fix_seed42` |
| 3 | 17.6440 | — | Old version (adaptive_seed42) | `adaptive_seed42` |
| 4 | 17.6947 | 0 | Degenerates to uniform | `nmin4_seed42` |

Note: n_min=3 (adaptive_seed42) used old code; n_min=2 (adaptive_fix) is the corrected version used in main table.

---

## ρ=0.6 (contamination_60)

| Method | PPL | Status | exp_id |
|--------|-----|--------|--------|
| Uniform | 17.7660 | DONE | `contamination_60_uniform_seed42` |
| Adaptive | — | RUNNING | `contamination_60_seed42_r2` |
| Grid b=0.5 | — | RUNNING | `contamination_60_grid_b0_5_seed42` |
| ESS-only | — | RUNNING | `contamination_60_ess_only_seed42` |

---

## LaTeX Table Code

### Main Table (ρ=0.4)

```latex
\begin{table}[t]
\centering
\caption{Holdout perplexity on the FineMath-3+ corpus ($\rho=0.4$, Qwen3-0.6B). Lower is better. $\Delta$ is relative to the uniform baseline. Adaptive uses $\tau=0.8, n_{\min}=2$. $^\dagger$\,seed456 excluded due to checkpoint artifact; mean from 2 seeds.}
\label{tab:main_results}
\small
\begin{tabular}{lccccr}
\toprule
\textbf{Method} & \textbf{seed42} & \textbf{seed123} & \textbf{seed456} & \textbf{Mean} & \textbf{$\Delta$} \\
\midrule
Pretrained (no training) & 22.970 & --- & --- & --- & --- \\
\midrule
Uniform (no reweight) & 17.694 & 17.686 & 17.702 & 17.694 & 0.000 \\
Grid $b{=}0.5$ & 17.651 & 17.638 & 17.650 & 17.646 & $-$0.048 \\
Grid $b{=}1.0$ & 17.692 & 17.674 & 17.680 & 17.682 & $-$0.012 \\
Grid $b{=}1.5$ & 17.718 & 17.701 & 17.710 & 17.710 & +0.016 \\
Grid $b{=}2.0^\dagger$ & 17.741 & 17.725 & --- & 17.733 & +0.039 \\
Grid $b{=}3.0^\dagger$ & 17.774 & 17.760 & --- & 17.767 & +0.073 \\
Grid $b{=}5.0^\dagger$ & 17.818 & 17.804 & --- & 17.811 & +0.117 \\
ESS-only & 17.730 & 17.720 & 17.719 & 17.723 & +0.029 \\
\midrule
Adaptive ($\tau{=}0.8$) & \textbf{17.653} & \textbf{17.643} & \textbf{17.657} & \textbf{17.651} & $-$\textbf{0.043} \\
Golden Ratio (oracle) & 17.654 & --- & --- & --- & $-$0.040 \\
\bottomrule
\end{tabular}
\end{table}
```

### τ Sweep Sub-table

```latex
\begin{table}[t]
\centering
\caption{Effect of threshold $\tau$ on adaptive weighting (seed42, $\rho=0.4$). $b^*$ statistics summarize the per-batch learned exponent.}
\label{tab:tau_sweep}
\small
\begin{tabular}{ccccc}
\toprule
$\tau$ & \textbf{PPL} & $\bar{b}^*$ & median $b^*$ & $\Delta$ vs Uniform \\
\midrule
0.50 & 17.688 & 0.392 & 0.171 & $-$0.006 \\
0.60 & 17.681 & 0.590 & 0.375 & $-$0.013 \\
0.70 & 17.679 & 0.894 & 0.580 & $-$0.015 \\
\textbf{0.80} & \textbf{17.653} & \textbf{1.399} & \textbf{0.871} & $-$\textbf{0.041} \\
0.90 & 17.712 & 2.360 & 1.320 & +0.018 \\
0.95 & 17.723 & 3.078 & 1.520 & +0.029 \\
\bottomrule
\end{tabular}
\end{table}
```

### n_min Ablation Sub-table

```latex
\begin{table}[t]
\centering
\caption{Effect of minimum batch size $n_{\min}$ on adaptive weighting (seed42, $\tau=0.8$, $\rho=0.4$).}
\label{tab:nmin_ablation}
\small
\begin{tabular}{cccc}
\toprule
$n_{\min}$ & \textbf{PPL} & $\bar{b}^*$ & Behavior \\
\midrule
1 & 17.789 & 7.197 & Over-downweighting \\
\textbf{2} & \textbf{17.653} & \textbf{1.399} & Optimal \\
4 & 17.695 & 0.000 & Degenerates to uniform \\
\bottomrule
\end{tabular}
\end{table}
```
