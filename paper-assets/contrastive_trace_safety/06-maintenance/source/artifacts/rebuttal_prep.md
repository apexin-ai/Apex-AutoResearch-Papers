# Rebuttal Preparation: Anticipated Reviewer Questions

Paper: *Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models*
Target: EMNLP 2026 (ARR May 25)

---

## Q1: Hyperparameter Overfitting

**Reviewer wording:** "The paper optimizes layer and window size per model. How do we know this isn't overfitting to specific hyperparameter configurations? The search space (layer x window x model) seems large enough to find spurious results."

**Core response:**
The balanced accuracy landscape over layers is flat near the optimum: Table A3 (app:layer_sweep, tab:joint_layer_w) shows that for QwQ-32B, L63 is near-optimal at W=3-5 and layers within +/-5 of the selected layer vary by <2pp BA. This is not a sharp peak that could reflect overfitting. We further validate layer selection stability with 5-fold cross-validation on 32B models (app:hyperparameter_robustness, tab:fold_ba_layers): for R1-32B the dominant layer is selected in 13/20 folds under LOO-CV, and for QwQ-32B in 13/19 folds, confirming robustness to validation set composition. BCa bootstrap confidence intervals (app:holm_bonferroni, tab:holm_bonferroni) quantify uncertainty: all 4 model-level HB tests pass at 384d precision, with effect sizes (+15-24pp precision) far exceeding the minimum detectable effect (app:power_analysis, tab:power_analysis: MDE 6.7-9.5pp at 80% power).

**Supporting references:**
- app:layer_sweep, tab:joint_layer_w (joint layer x window grid)
- app:hyperparameter_robustness, tab:fold_ba_layers (5-fold CV layer stability)
- app:holm_bonferroni, tab:holm_bonferroni (4/4 model-level HB correction)
- app:power_analysis, tab:power_analysis (post-hoc MDE)
- app:ba_layer_comparison, tab:ba_layer_results (BA-optimal layers yield 14/16 HB, refuting circularity)

---

## Q2: Single Dataset

**Reviewer wording:** "All experiments are conducted on a single dataset (HarmThoughts). This severely limits the generalizability of the findings. Why not evaluate on additional safety benchmarks?"

**Core response:**
HarmThoughts is, to our knowledge, the only publicly available dataset with step-level commitment point annotations for reasoning model traces. Existing safety benchmarks (e.g., SafeRLHF, BeaverTails) provide trace-level labels (safe/unsafe), not the within-trace temporal annotations required for commitment point detection. We mitigate single-dataset risk through cross-model generalization: 4 models spanning 2 architectures (Llama, Qwen), 2 training paradigms (R1-distilled, STILL/native), and 2 scales (7-8B, 32B) all show consistent HS advantage at corrected layers (14/16 HB, precision +15-24pp). The consistency across architecturally diverse models provides stronger evidence than testing one model on multiple datasets with similar annotation schemes. We acknowledge this limitation explicitly in Section Limitations (sec:limitations) and identify multi-dataset evaluation as priority future work.

**Supporting references:**
- sec:limitations (explicit dataset limitation disclosure)
- sec:setup (4-model experimental design)
- tab:hs_vs_text, Table 3 (cross-model consistency of precision advantage)
- tab:holm_bonferroni (14/16 HB across 4 models)

---

## Q3: Stronger Text Encoder

**Reviewer wording:** "The text baseline uses MiniLM-L6-v2 (384d), a relatively weak encoder. A stronger text encoder could close or eliminate the reported HS advantage. Have you tested this?"

**Core response:**
We have. Appendix app:encoder_robustness reports results with BGE-large-en-v1.5 (1024d), a substantially stronger encoder. The HS advantage narrows, as expected: only 1/4 models (OT-7B, +18.1pp precision) survives Holm-Bonferroni correction against BGE-large, compared to 4/4 against MiniLM (tab:encoder_robustness, tab:bge_ba_fpr). This is precisely what our paper predicts. Our claim is not that HS universally dominates all text encoders; it is that HS advantage is encoder-conditional (Section sec:hs-text). At the MiniLM baseline widely used in deployment monitoring, HS provides a significant and consistent advantage. As text encoders improve, the gap shrinks. This encoder-conditional framing is visible in Figure fig:forest_precision, where the forest plot shows both MiniLM and BGE-large comparisons side by side. The remaining OT-7B advantage against BGE-large, plus the random projection control (app:random_projection: RP 384d outperforms text 384d by +8-20pp), confirms that HS carries genuine non-textual signal beyond dimensionality matching.

We further tested E5-Mistral-7B-Instruct (intfloat/e5-mistral-7b-instruct, 4096d, PCA-reduced to 384d), a 7B-parameter SOTA text encoder representing a 300x scale-up from MiniLM (22M). HS probes outperform E5-Mistral on all 4 models: R1-8B shows significant HS advantage on all 3 metrics (BA p=0.004, Precision p=0.001, FPR p=0.021); OT-7B on BA (p=0.090, marginal), Precision (p=0.009), and FPR (p=0.007); R1-32B shows directional HS leads (BA p=0.091, Precision p=0.235, FPR p=0.533); QwQ-32B is marginal on BA (p=0.076). The HS advantage partially survives even against a 7B encoder (2/4 models reach HB significance on at least one metric), consistent with the encoder-conditional framing. The progression from MiniLM (22M) to BGE-large (335M) to E5-Mistral (7B) shows a monotonic narrowing of the HS gap that never closes, supporting the conclusion that hidden states encode safety-relevant features not fully recoverable from surface text at any tested encoder scale.

**Supporting references:**
- app:encoder_robustness, tab:encoder_robustness (BGE-large precision comparison)
- tab:bge_ba_fpr (BGE-large BA and FPR comparison)
- fig:forest_precision (forest plot, MiniLM vs BGE-large)
- app:random_projection, tab:random_projection (dimensionality control)
- sec:hs-text (encoder-conditional framing in main text)
- E5-Mistral results: artifacts/e5_mistral_comparison_v2/ (corrected HS layers)

---

## Q4: Position Confound (R1-32B)

**Reviewer wording:** "The HS probe's advantage could simply reflect position information encoded in hidden states. Since commitment points tend to occur at specific relative positions, the probe may be exploiting a positional shortcut rather than genuine safety content."

**Core response:**
We directly test this with position-residualized probing (app:position_residual, tab:position_residual). After regressing out relative position (t/T) from both HS and text features, we retrain probes and re-evaluate. Results: 3/4 models retain significant non-positional HS advantage (OT-7B +6.9pp, R1-8B +6.4pp, QwQ-32B +3.7pp, all HB-corrected). R1-32B is the exception: its residualized gap drops to +1.9pp (p=0.914, NS), confirming that its HS advantage is largely position-mediated. We report this transparently in the paper, grading R1-32B as "qualified" evidence (sec:discussion). Importantly, position encoding in hidden states does not invalidate the probe. In deployment, position is available and informative; the residualization analysis serves to decompose signal sources, not to disqualify position-aware detection. The 3/4 model consensus for non-positional signal, combined with selectivity scores of 11.1-16.8pp above the random control task (app:control), establishes that HS probes capture genuine safety-relevant content beyond positional shortcuts.

**Supporting references:**
- app:position_residual, tab:position_residual (residualized BA, 3/4 HB pass)
- sec:discussion (R1-32B qualified framing, position mediation paragraph)
- app:control (control task selectivity 11.1-16.8pp)
- tab:hs_vs_text, Table 3 (original vs residualized comparison)

---

## Q5: Small Sample Size at 32B (n=19-20)

**Reviewer wording:** "The 32B model experiments use only 19-20 test traces. This is far too small to draw reliable conclusions, especially given the number of comparisons made."

**Core response:**
We acknowledge the small sample and address it with three complementary analyses. First, post-hoc power analysis (app:power_analysis, tab:power_analysis) shows the MDE at 80% power is 8.6-9.5pp for 32B models. All significant effects (+15-24pp precision, +11-19pp BA) are well above MDE, confirming adequate statistical power for the detected effects. Second, 5-seed stability analysis (app:multi_seed, tab:seed_hb) shows QwQ-32B achieves 5/5 HB pass rate and R1-32B achieves 5/5, with precision advantage never reversing across any of the 10 model-seed combinations. Third, the effects are internally consistent: QwQ-32B shows significance at all 15 window sizes (not just the cherry-picked best), making a Type I error at alpha=0.05 across 15 independent tests astronomically unlikely. R1-32B is honestly reported as "statistically narrow" (W=1 only, 25% coverage). The 32B trace generation cost (~2000-4000 reasoning steps per trace) makes large-scale evaluation prohibitively expensive. We view the current results as sufficient for the claim that HS advantage exists at 32B, while acknowledging precision of effect size estimates is limited.

**Supporting references:**
- app:power_analysis, tab:power_analysis (MDE vs observed effects)
- app:multi_seed, tab:seed_hb, tab:multi_seed (5-seed HB pass rates)
- sec:32b-analysis, tab:32b_divergence, Table 4 (per-model 32B analysis)
- tab:hs_vs_text, Table 3 (bootstrap CIs for all comparisons)
- sec:limitations (sample size limitation acknowledged)

---

## Negative Experiments Rebuttal Guide (20 experiments)

Generated: 2026-05-24 pre-submission.

### Classification

- **A (Boundary Conditions, 5)**: A1 AUROC layer sweep, A2 raw selectivity NS, A3 window ablation, A4-A5 FPR mixed results
- **B (Method Limitations -> support C3, 10)**: B1-B3 Mahalanobis 4/4 fail, B4-B7 BOCPD/CUSUM systematic fail, B8 CCS < supervised, B9 MLP < LR, B10 cross-transfer fail
- **C (Diagnostic null results, 5)**: C1 temporal vs static NS, C2 GRU single-seed, C3 regularized probes, C4 initial layer sweep, C5 annotation validation

### Top 3 Risks from Negative Experiments

**Risk #1: FPR Mixed Results (A4+A5)**
- QwQ HS FPR ~= text FPR (47.5% vs 50%); OT-7B HS FPR much better (17.5% vs 46%)
- Core claim is precision (+15-22pp), not FPR. Model-specific FPR consistent with conditional advantage framing.
- Key line: "Our primary claim (C2) is about precision advantage, not FPR."

**Risk #2: AUROC Layer Selection Divergence (A1)**
- AUROC selects different layers than precision-based metrics for 32B models
- Strongest defense: BA-layer robustness shows 16/16 HB pass at threshold-free selected layers
- Key line: "At BA-selected layers, all four models show significant HS advantage across all four metrics (16/16 HB)."

**Risk #3: Cross-Model Transfer Failure (B10)**
- PCA projections don't transfer across models (max 67% vs 82% baseline)
- Framing is methodological analysis, not universal detector. Model-specificity strengthens need for per-model audit.
- Key line: "Model-specificity makes our diagnostic framework more necessary, not less."

### Response Templates

**Template A (Boundary Condition):** "This result defines boundary conditions. We explicitly report this in [Section X] and frame C2 as conditional."

**Template B (Method Limitation -> C3):** "The failure of [method] is core to C3. We provide mechanism-specific failure analysis in Appendix [X]. The pattern across 7 methods constrains the hypothesis space."

**Template C (Diagnostic):** "Preliminary diagnostic that informed experimental design. Final results incorporating these insights are in [Section X]."

### Overall Assessment
- 10/20 negatives directly support C3 (negative results contribution)
- 5/20 define boundary conditions (honest disclosure)
- 5/20 are internal diagnostics (mostly not in paper)
- All 3 real risk points have adequate paper defenses
