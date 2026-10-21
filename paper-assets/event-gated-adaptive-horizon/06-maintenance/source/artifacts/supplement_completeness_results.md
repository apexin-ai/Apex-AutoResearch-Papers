# Supplement 完整性检查报告

检查日期：2026-05-24

## 1. 正文→Appendix 引用映射

| 引用来源（文件:行号） | 引用目标 | appendix 中是否存在 | 内容状态 |
|---|---|---|---|
| introduction.tex:6 | `Table~\ref{tab:nve_loeo}` | ✅ appendix.tex:289 | 长（完整 LOEO 表格） |
| methodology.tex:32 | `Table~\ref{tab:factorial_design}` in `Appendix~\ref{sec:appendix_factorial}` | ✅ appendix.tex:345, 310 | 长（完整 factorial 设计表） |
| methodology.tex:38 | `Appendix~Table~\ref{tab:nve_loeo}` | ✅ appendix.tex:289 | 长 |
| methodology.tex:42 | `Appendix~\ref{sec:sgs_gradient_analysis}` | ✅ appendix.tex:516 | 长（含梯度分解结果） |
| methodology.tex:57 | `Appendix~\ref{sec:hyperparameters}` | ✅ appendix.tex:738 | 中（~54行，完整超参表） |
| results.tex:8 | `Table~\ref{tab:complete_results}` | ✅ appendix.tex:11 | 长（43个实验配置完整表） |
| results.tex:82 | `Appendix~\ref{sec:seed_divergence}` | ✅ appendix.tex:593 | 长（seed 分析+failure taxonomy） |
| results.tex:88 | `Appendix~\ref{sec:appendix_factorial}` | ✅ appendix.tex:310 | 长 |
| results.tex:91 | `Table~\ref{tab:three_way_emb}`, `Figure~\ref{fig:dt_amplification}`, `Appendix~\ref{sec:appendix_factorial}` | ✅ appendix.tex:320, 435, 310 | 长 |
| results.tex:104 | `Figure~\ref{fig:multiple_pathways}` in `Appendix~\ref{sec:pathways}` | ✅ appendix.tex:674, 666 | 中 |
| results.tex:106 | `Appendix~\ref{sec:sgs_gradient_analysis}` | ✅ appendix.tex:516 | 长 |
| results.tex:109 | `Appendix~\ref{sec:seed_divergence}` | ✅ appendix.tex:593 | 长 |
| results.tex:157 | `Appendix~\ref{sec:tcn_cross_env}` | ✅ appendix.tex:683 | 长（完整 TCN 跨环境表） |
| results.tex:167 | `Appendix~\ref{sec:dual_critic_appendix}` | ✅ appendix.tex:872 | 中（~50行） |
| results.tex:170 | `Appendix~\ref{sec:dual_critic_appendix}` | ✅ appendix.tex:872 | 中 |
| results.tex:179 | `Appendix~\ref{sec:detector_appendix}` | ✅ appendix.tex:792 | 中（~80行，含算法+验证） |
| analysis.tex:5 | `Table~\ref{tab:rssm_fidelity}`, `Appendix~\ref{sec:mpc_immune}` | ✅ appendix.tex:467, 656 | 长 / 短 |
| analysis.tex:8 | `Table~\ref{tab:nve_loeo}`, `Appendix~\ref{sec:appendix_analysis}` | ✅ appendix.tex:289, 450 | 长 |
| analysis.tex:11 | `Appendix~\ref{sec:extended_training}` | ✅ appendix.tex:651 | 短（~4行） |
| analysis.tex:14 | `Table~\ref{tab:cross_domain}` | ✅ appendix.tex:103 | 长（跨环境验证表） |

## 2. Appendix 内部引用

Appendix 共 35 个 `\ref{}` 引用，全部有对应 `\label{}`：

- 自引用（appendix 内部）：`tab:complete_results`, `tab:nve_raw`, `tab:sensitivity_b1`, `tab:sensitivity_b2`, `tab:sensitivity_b2_full`, `fig:nve_roc`, `tab:baseline_seeds`, `tab:three_way_emb`, `tab:factorial_design`, `fig:factorial_grid`, `tab:causal_matrix`, `fig:dt_amplification`, `fig:multiple_pathways`, `tab:tcn_full`, `tab:hyperparams`, `tab:dual_critic_full`, `sec:appendix_sensitivity`, `sec:seed_divergence` 等
- 引用正文：`tab:main_results` (results.tex:13 ✅), `sec:metrics` (methodology.tex ✅), `sec:results` (results.tex ✅), `sec:f6` (results.tex:101 ✅), `sec:detector` (results.tex ✅)

**悬空引用：无**

## 3. Figure/Table 文件检查

`\graphicspath` 设为 `../artifacts/`，所有图片路径相对于 `artifacts/` 解析。

### Appendix 中引用的图片

| 文件路径 | 是否存在 |
|---|---|
| `figures/nve_roc_curve.pdf` | ✅ `artifacts/figures/nve_roc_curve.pdf` |
| `figures/paper/fig3_factorial_grid.pdf` | ✅ `artifacts/figures/paper/fig3_factorial_grid.pdf` |
| `figures/paper/fig5_dt_amplification.pdf` | ✅ `artifacts/figures/paper/fig5_dt_amplification.pdf` |
| `figures/paper/fig4_mechanism_diagram.pdf` | ✅ `artifacts/figures/paper/fig4_mechanism_diagram.pdf` |
| `figures/fig3_gradient_decomposition.pdf` | ✅ `artifacts/figures/fig3_gradient_decomposition.pdf` |
| `figures/fig2_civo_decomposition.pdf` | ✅ `artifacts/figures/fig2_civo_decomposition.pdf` |
| `figures/fig4_entropy_dynamics.pdf` | ✅ `artifacts/figures/fig4_entropy_dynamics.pdf` |
| `figures/paper/fig6_multiple_pathways.pdf` | ✅ `artifacts/figures/paper/fig6_multiple_pathways.pdf` |

### 正文中引用的图片

| 文件路径 | 是否存在 |
|---|---|
| `figures/paper/fig1_learning_curves.pdf` | ✅ `artifacts/figures/paper/fig1_learning_curves.pdf` |
| `figures/fig1_nve_trajectory.pdf` | ✅ `artifacts/figures/fig1_nve_trajectory.pdf` |

### figures/ 目录完整文件清单

**`artifacts/figures/`:**
actor_entropy_comparison.pdf, actor_entropy_comparison.png, fig1_nve_trajectory.pdf, fig2_civo_decomposition.pdf, fig3_gradient_decomposition.pdf, fig4_entropy_dynamics.pdf, nve_roc_curve.pdf, data/, paper/

**`artifacts/figures/paper/`:**
fig1_learning_curves.pdf, fig2_nve_trajectory.pdf, fig3_factorial_grid.pdf, fig4_mechanism_diagram.pdf, fig5_dt_amplification.pdf, fig6_collapse_pathways_d054.pdf, fig6_multiple_pathways.pdf, fig_style.py

## 4. Appendix Section 清单

| Section 标题 | Label | 内容长度 |
|---|---|---|
| **A. Complete Experimental Results** | `sec:complete_results` | 长 (~116行，含43配置完整表) |
| **B. NVE Threshold Sensitivity Analysis** | `sec:appendix_sensitivity` | 长 (~190行) |
| ├ B.1 Per-Experiment NVE Values | — | 中 (~28行) |
| ├ B.2 Multi-Threshold Classification Performance | — | 长 (~68行) |
| ├ B.3 Threshold Recommendation | — | 短 (~12行) |
| ├ B.4 Expanded ROC Analysis | `sec:roc_analysis` | 短 (~16行) |
| ├ B.5 NVE Normalization Robustness | `sec:nve_robustness` | 中 (~30行) |
| └ B.6 Leave-One-Environment-Out Cross-Validation | `sec:nve_loeo` | 中 (~30行) |
| **C. Factorial Ablation Details** | `sec:appendix_factorial` | 长 (~140行) |
| ├ C.1 F3: Unexposed Temporal Embedding Suppresses Value Drift | `sec:f3` | 中 (~50行) |
| ├ C.2 F4: Degradation Scales Monotonically with dt | `sec:f4` | 短 (~12行) |
| └ C.3 F5: Imagination Horizon and Subsampling Are Secondary | `sec:f5` | 短 (~9行) |
| **D. Full Analysis & Discussion** | `sec:appendix_analysis` | 长 (~288行) |
| ├ D.1 The CIVO Mechanism | `sec:civo_mechanism` | 长 (~60行) |
| ├ D.2 SGS and Gradient Decomposition | `sec:sgs_gradient_analysis` | 长 (~62行) |
| │ ├ D.2.1 Gradient Decomposition Results | `sec:gradient_decomposition` | 中 (~38行) |
| │ ├ D.2.2 Implications for CIVO Mechanism | `sec:sgs_implications` | 中 (~20行) |
| │ ├ D.2.3 Entropy Dynamics Across Configurations | `sec:entropy_dynamics` | 短 (~9行) |
| │ └ D.2.4 Exp_016e Reinterpreted as Stochastic Variation | `sec:016e_reinterp` | 短 (~5行) |
| ├ D.3 Post-CIVO Outcomes: Why Seeds Diverge | `sec:seed_divergence` | 长 (~59行) |
| │ └ D.3.1 Failure and Degradation Mode Taxonomy | — | 中 (~26行) |
| ├ D.4 Extended Training Dynamics | `sec:extended_training` | 短 (~4行) |
| ├ D.5 Why MPC Is Immune | `sec:mpc_immune` | 短 (~5行) |
| ├ D.6 The dt-Embedding Dilemma | `sec:embedding_dilemma` | 短 (~5行) |
| ├ D.7 Multiple Vulnerability Pathways | `sec:pathways` | 中 (~12行) |
| ├ D.8 Implications for Temporal Abstraction | `sec:implications` | 短 (~5行) |
| └ D.9 Cross-Environment TCN Evaluation | `sec:tcn_cross_env` | 长 (~54行，含完整 TCN 表) |
| **E. DreamerV3 Hyperparameters** | `sec:hyperparameters` | 中 (~54行，含超参表) |
| **F. Online CIVO Detector Details** | `sec:detector_appendix` | 中 (~80行) |
| ├ F.1 Algorithm Specification | — | 中 (~29行，含算法伪代码) |
| ├ F.2 Validation Results | — | 中 (~38行) |
| ├ F.3 Cross-Simulator Specificity (PickCube) | — | 短 (~4行) |
| └ F.4 Detector Limitations | — | 短 (~4行) |
| **G. Dual-Critic Mechanism Ablation** | `sec:dual_critic_appendix` | 中 (~50行) |
| ├ G.1 2×2 Factorial Design | — | 中 (~33行，含结果表) |
| ├ G.2 Critic Convergence (v1 ≈ v2) | — | 短 (~6行) |
| └ G.3 Recovery vs. Prevention Mechanism | — | 中 (~8行) |

## 总结

- ✅ 通过项: **4/4**
  - 正文→Appendix 引用：20 处引用，全部在 appendix 中有对应 label 且内容非空
  - Appendix 内部引用：35 个 `\ref{}`，0 个悬空引用
  - 图片文件：10 个 `\includegraphics`（8 appendix + 2 正文），全部存在于 artifacts/ 目录
  - Appendix 结构：7 个主 section + 25 个 subsection，内容完整
- ⚠️ 需修复: **0**
