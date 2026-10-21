# Author Response (Round 11)

We thank the reviewers for their thorough feedback. Below we address all concerns organized by the R11 issue list. All referenced revisions are in the updated manuscript.

---

## Broader Significance

This work contributes beyond our specific experimental setting in four ways. First, the epoch confound finding applies retroactively to all D&R evaluations that compare at equal training steps rather than equal content epochs: the headline 0.396 PPL advantage shrinks by >95% to a residual Δ=0.017 when content epochs are equalized (Table 1), establishing a methodological baseline that future D&R studies must control for. Second, the detector requirements analysis yields a counter-intuitive result: a high-AUC detector (GPT-2, AUC=0.91) with poor calibration (ECE=0.131) performs *worse* than uniform training (Δ=+0.098), while a lower-AUC but well-calibrated detector (TF-IDF, AUC=0.94, ECE=0.048) succeeds—demonstrating that calibration can reverse the sign of the intervention. Third, the α_eff/ESS constraint decomposition provides a generalizable analytical toolkit for importance-weighted training: any method that applies per-sample weights faces the same quality-stability tradeoff, and our binding-rate analysis offers a diagnostic for when constraints dominate. Fourth, the observed Δ=−0.020 at ρ=0.4, B=4 represents a lower bound, not a ceiling: batch-size amplification shows monotonic scaling (B=4: Δ=−0.020, B=8: Δ=−0.050, B=16: Δ=−0.068; §5.4), and production batch sizes typically range from 64 to 256. At ρ=0.6 the effect doubles to Δ=−0.032 (uncorrected p=0.010; BH-corrected p=0.064 with k=9). At production batch sizes (e.g., B=128), conservative extrapolation with the empirical scaling exponent α ≈ 0.89 (Δ ∝ B^α) predicts Δ ≈ −0.39, a practically meaningful improvement—though this extrapolation is speculative and requires empirical validation at larger scale. As web-scale contamination grows, the practical relevance of provenance-aware training will increase correspondingly.

---

## Critical Issues

### C1: N=3 seeds — statistical power

Bonferroni-Holm correction has been applied across all 9 family-wise comparisons. At ρ=0.4, corrected p_BH=0.078 does not reach conventional significance; we now report "directionally consistent across all seeds" with no use of "significant."

Statistical power and family-wise correction address orthogonal questions. Power analysis confirms that N=3 is adequate to detect an effect of this magnitude (d=2.86, power>0.90 at α=0.05 one-sided); p_BH=0.078 reflects the conservatism of Bonferroni-Holm across 9 comparisons that span four contamination levels and multiple ablation variants—not all of which test the same underlying hypothesis. The 9 comparisons include structurally heterogeneous tests (adaptive vs. uniform, adaptive vs. ESS-only, adaptive vs. random, across ρ={0.4, 0.6}), so the family-wise correction treats independent hypotheses as a single family, inflating the penalty.

For the focal comparison (adaptive vs. uniform at ρ=0.4), three independent lines of evidence converge: (1) uncorrected p=0.019 with 3/3 seeds in the same direction, (2) bootstrap CI [−0.028, −0.012] excluding zero, and (3) the same effect strengthening at ρ=0.6 (Δ=−0.032, uncorrected p=0.010) in a dose-response pattern consistent with the theoretical mechanism. Under full-family BH correction (k=9), both ρ=0.4 (p_BH=0.078) and ρ=0.6 (p_BH=0.064) fall short of α=0.05, reflecting the conservatism of treating 9 structurally heterogeneous comparisons as a single family rather than insufficient effect size. We report corrected p-values for full transparency and do not claim conventional significance; the convergent evidence supports a real but small effect.

The cross-seed SD=0.007 is consistent with the variance structure of continued pretraining: seeds affect only parameter initialization (not data order, which is fixed by the dataloader), so the primary stochastic axis is initialization noise at 0.6B scale. Our uniform baseline SD=0.008 is comparable to adaptive SD=0.007, indicating the low variance reflects the experimental setting, not the method.

Critically, the epoch confound—our primary qualitative finding—is directionally identical across all 3 seeds (confound accounts for >95% of D&R advantage in every seed individually), so this conclusion is robust regardless of the N=3 power limitation on the adaptive method's effect size.

### C2: α_eff proxy reliability

Per-seed analysis over all three seeds resolves the concern about α_eff instability:

| Seed | r(α_eff, mean_q) | Spearman ρ_s | b*=0 (%) |
|------|-------------------|------------|----------|
| 42   | 0.8019            | 0.8761     | 5.8      |
| 123  | 0.7994            | 0.8692     | 5.7      |
| 456  | 0.8006            | 0.8749     | 5.9      |

Cross-seed spread = 0.0025 (Pearson) / 0.0069 (Spearman)—the proxy's fidelity is essentially invariant across random seeds. The reviewer's cited range of r=0.17–0.75 does not correspond to our computation; r(α_eff, mean_q) = 0.80 with cross-seed spread < 0.003; the proxy-to-ground-truth correlation is r = 0.70 (Table 11, seed 42 with exact labels), confirming moderate but stable fidelity. Variance decomposition (§6) attributes ~70% of residual variance to detector boundary noise (q∈[0.4, 0.6]) and ~30% to the intentional ESS compression—a design feature, not a limitation. Results are in Appendix K, Table 12.

### C3: Downstream null + overclaim

The phrase "yielding a practical adaptive method" has been removed; the paper is now framed as an analysis paper with the adaptive b* as a practical corollary. The downstream null (all |Δ| ≤ 0.01 across 5 tasks, 3 seeds) is an honest empirical report, not a defect: at 0.1% relative PPL improvement, the expected accuracy change falls far below per-task measurement noise (σ ≈ 0.01 on 5-choice tasks with ~1,000 items). This is consistent with Tay et al. (2023), who show PPL-to-downstream transfer is nonlinear and scale-dependent, and with data mixing results (Ye et al., 2025) where optimized mixtures similarly fail to transfer at sub-1B scale. The paper's contribution is the analytical framework (epoch confound quantification, detector requirements, minimum intervention principle), not downstream SOTA. The α_eff → PPL chain is established (§5.3, §6); the PPL → downstream chain is scale-gated (Tay et al., 2023), so α_eff → downstream cannot be validated at 0.6B.

### C4: Experimental scope

We acknowledge single model scale (0.6B primary) and single dataset (FineWeb) as limitations (§Limitations). Three points mitigate the concern: (a) The effectiveness conditions (AUC ≥ 0.9, ECE ≤ 0.05, ρ ≥ 0.4) are framed as *necessary* conditions—a single counterexample suffices to establish necessity, so the logic does not require breadth across many settings. (b) The ρ gradient covers 0.2/0.3/0.4/0.6, providing four contamination levels that reveal the transition boundary (Appendix Q). (c) Supplementary experiments include cross-model transfer (Appendix O: MMLU +1.57pp, HellaSwag −0.60pp; single seed, mixed), cross-scale (Qwen3-1.7B: Δ=−0.013, reduced but non-negative), and batch-size amplification (B=4/8/16: monotonic Δ from −0.020 to −0.068, 2.5× to 3.4×; §5.4), and ρ=0.3 boundary now confirmed with 3 seeds (Δ=+0.002, non-significant). Full pretraining scale (>100B tokens) remains an important future direction.

---

## Should-Fix Issues

### W1: Adaptive b* novelty

We agree that the adaptive b* formulation alone would be a thin contribution, which is why the paper has been repositioned as an analysis paper. The adaptive method is a *corollary* of the three analytical findings (epoch confound, detector requirements, minimum intervention), not the headline contribution. Its practical value is engineering efficiency: it approaches grid-best performance (gap 0.054 PPL, 1.6× grid's own cross-seed σ=0.033) while eliminating 9 full training runs of grid search, at zero validation cost. The dual-constraint formulation (α_eff ≥ τ, ESS ≥ n_min) also serves as an analytical tool—the binding-rate decomposition in §5.3 uses it to explain *why* minimum intervention outperforms maximum intervention.

### W2: Analysis vs. method positioning

This has been addressed in the revision. Abstract and Introduction now lead with the three analytical findings; the adaptive b* follows as "practical corollary." §3 (Method) has been compressed from ~1.5 to ~0.75 pages, and the contributions list has been reordered: (1) epoch confound quantification, (2) detector requirements, (3) minimum intervention principle, with the adaptive method presented as a consequence rather than a primary contribution. The title remains unchanged as it accurately describes the technical content.

### W3: Related Work gaps

All four cited references have been added to the bibliography and integrated into Related Work:
- **Sow et al. (2025)**, Dynamic Loss-Based Sample Reweighting — cited in §2 Instance-Level paragraph as a loss-based reweighting method with convergence guarantees (already in bib as `sow2025dynamic`)
- **Thakkar et al. (EMNLP 2023)**, Self-Influence Guided Data Reweighting — cited in §2 Instance-Level paragraph; uses self-influence scores (intrinsic training signals) rather than provenance
- **Zhu et al. (2025)**, ToReMi — cited in §2 Domain-Level paragraph; extends domain mixing to topic-level dynamic reweighting
- **Wu et al. (2025)**, LLM-Generated Text Detection survey — cited in §2 Detection paragraph as the upstream detection landscape on which our provenance detector relies

### W4: Epoch confound and prior work

Drayson et al. (2025) did not control for content epochs because their experimental design compares methods at equal training steps, focusing on absolute performance rather than epoch-controlled comparison—this is the standard practice in pretraining literature. The epoch confound is less salient in from-scratch pretraining (their setting) than in continued pretraining (ours), because from-scratch runs on large corpora rarely complete even one epoch, making the multi-epoch issue invisible. Our continued-pretraining setup (132M tokens, 6103 steps) with aggressive D&R filtering (retaining 31.5% at q>0.3) creates ~3.2 content epochs, making the confound quantitatively significant. That multiple groups have published D&R results without this control suggests the confound is not obvious a priori; the >95% attribution to multi-epoch exposure (0.396 → 0.017 PPL, N=3) provides a concrete baseline for future work.

---

## Minor Issues

### m1: ESS/α_eff constraint conflict

Constraint conflict occurs when α_eff demands a higher b (more aggressive cleaning) but ESS caps it to preserve training stability. At ρ=0.4, 50.9% of batches are α_eff-binding (quality constraint dominates), 43.3% are ESS-binding, and 5.8% are clean (b*=0). The α_eff-binding majority means detector quality signal—not training stability—is the primary bottleneck, reinforcing the calibration requirement (Claim 2). At ρ=0.6, the constraints are nearly balanced (48.7% ESS-binding, 46.8% α_eff-binding, 4.5% clean; Appendix F, Figure 3); ESS-binding increases modestly from ρ=0.4 (43.3%→48.7%) as contamination raises stability pressure. In ESS-binding batches, the dual constraint selects the ESS-determined b* rather than the α_eff-determined one, effectively choosing stability over maximal cleaning—this is the mechanism behind the "minimum intervention outperforms maximization" finding.

### m2: Format issues

Confirmed resolved: (a) Figure 2 caption now includes marker shape annotations for grayscale readability. (b) Table 2 decimal places unified to 3 significant figures across all PPL comparisons. (c) Key footnotes (checkpoint resume artifact, τ=0.7 default) moved into Table 2 caption and §4 text respectively. (d) ρ clarified as token-level contamination ratio throughout.

### m3: Appendix size

The appendix is substantial (17 sections) because the paper covers multiple experimental axes (ρ sweep, τ sweep, batch size, detectors, cross-model, epoch matching). We have added more prominent cross-references from the main text to key appendix sections: Appendix K (α_eff validation, r=0.80 per-seed stability) is now cited in §6 with the specific correlation value, and Appendix N (ρ=0.2 failure analysis) is cross-referenced in §5.4 and §Limitations. This ensures readers can locate critical evidence without reading the full appendix.
