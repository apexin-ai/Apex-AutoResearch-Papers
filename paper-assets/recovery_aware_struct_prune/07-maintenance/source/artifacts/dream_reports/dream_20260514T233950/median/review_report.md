---
dream_id: dream_20260514T233950
tier: median
overall_score: 3 - Weak Reject
timestamp: 2026-05-15T00:27:21.403867+00:00
---


# Reviewer 1 (R1) — Methods & Experiments Focus

## 1. Summary

This paper presents a systematic empirical study of structured pruning on DeepSeek-R1-Distill-Qwen-7B, comparing four pruning strategies (Standard Taylor, magnitude-only, CKA-aware RASP, and learned-gate GRASPrune) across three sparsity levels with SFT and SFT+GRPO recovery. The central finding is that even 20% structured sparsity causes catastrophic reasoning collapse (83.2% → 7.6–26.8% GSM8K), and that CKA functional overlap — while a reliable metric (split-half ρ=0.92) — does not predict per-structure recoverability (β=0.08, p=0.12). The best recovered model (GRASPrune + SFT+GRPO) reaches only 47.7% of baseline, contradicting Self-Healing's 95% recovery claim for unstructured pruning at similar compression.

## 2. Strengths

- **Comprehensive experimental design.** 14 planned experiments covering the full pipeline (prune → eval → SFT → GRPO → eval) with multiple pruning methods, sparsity levels, recovery paradigms, and cross-benchmark evaluation. This is thorough for an empirical study.

- **Rigorous statistical methodology.** The paper employs McNemar's test for pairwise comparisons, mixed-effects regression with layer as random effect (appropriate given ICC=0.73), 95% CIs on all accuracy estimates (N=1319 full test set), and 2x2 ANOVA for interaction effects. The split-half reliability analysis for CKA (ρ=0.92) is a welcome methodological sanity check rarely seen in pruning papers.

- **Honest negative results.** The paper reports that CKA overlap does NOT predict per-structure recoverability (β=0.08, p=0.12, marginal R²=0.04), which directly undermines a core claim from the framing. Reporting this null finding rather than p-hacking or omitting it is commendable. The GRPO-adds-only-5pp finding (with no interaction, p=0.54) is similarly honest.

- **Multi-seed robustness.** Table 2 reports three seeds for RASP (22.4%, 15.8%, 28.1%; mean 22.1±6.2), acknowledging substantial variance. This is better than single-seed reporting, though the variance is concerning (see Weaknesses).

- **Well-motivated two-stage recovery.** The SFT warmup → GRPO pipeline is well-justified by the diagnosis that pruned models fail to generate EOS tokens under sampling, making direct GRPO impossible. The EOS rate tracking (Appendix C) provides mechanistic evidence.

- **Cross-benchmark analysis (Table 9).** Showing 76.8% MMLU retention vs 30% MATH-500 retention reveals that structured pruning selectively destroys reasoning chains while preserving factual recall — a genuinely informative finding with practical implications.

## 3. Weaknesses

- **The central hypothesis is falsified by the paper's own data.** The paper was framed around the "Redundancy Paradox" — that CKA functional overlap predicts RLVR recoverability. Table 5 shows this is not the case (β=0.08, p=0.12). The paper's title asks "When Does Structured Pruning Kill Reasoning?" but the actual answer — "almost immediately, at 20% sparsity, regardless of method" — is an observational finding, not a methodological contribution. The pivot from "RASP enables recovery" to "structured pruning is harder than expected" weakens the contribution from a methods paper to a negative-result empirical note.

- **Extremely high multi-seed variance undermines reliability.** RASP at seed 42 yields 22.4%, seed 123 yields 15.8%, seed 7 yields 28.1% — a range of 12.3pp with only 3 seeds. The standard deviation (6.2pp) is nearly as large as the gap between RASP and magnitude-only pruning (22.4 vs 18.3 = 4.1pp). This means most pairwise method comparisons in Table 1 are not robust to seed variation. Only the gap between RASP/GRASPrune and Standard/Random appears robust.

- **Single model, single architecture.** All experiments use DeepSeek-R1-Distill-Qwen-7B. The paper acknowledges this but the limitation is severe: distilled models are known to be more pruning-sensitive (the paper's own memory.md documents this). Results may not generalize to base models, larger models, or non-Qwen architectures. The comparison with Self-Healing (95% recovery) is confounded by the fact that Self-Healing uses unstructured pruning on potentially different models.

- **Recovery results are modest and the claimed "best" method (GRASPrune) is an external baseline.** Table 3 shows GRASPrune achieves the highest recovery ratio (0.477), beating the paper's proposed RASP (0.406). The paper's own method is not the best performer. The 39.7% best recovered accuracy (vs 83.2% baseline) represents a 52% accuracy loss — this is not a practically useful compression result.

- **Per-layer 40% capacity floor is a strong constraint that confounds comparisons.** The paper introduced a minimum of 40% capacity per layer after discovering that unconstrained pruning destroys early layers (Section 8.1 of memory). This floor dramatically restricts the pruning space and may artificially reduce differences between methods — if most layers are constrained to keep ≥40%, the scoring function matters less.

- **F(h) definition inconsistency.** The paper summary states F(h) = max_{h' in same layer} CKA(X_h, X_{h'}), but the code (`cka_overlap.py` line 195) computes F(h) as the mean CKA similarity: `(matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)`. The max vs mean distinction materially affects the scoring — max captures the "best substitute" while mean captures "general redundancy." The paper should clarify which was actually used and justify the choice.

- **MLP grouping is arbitrary.** The code groups MLP channels into n_groups = n_heads = 28 groups of group_size = 18944//28 = 676 channels each. This grouping has no functional justification — it's chosen for implementation convenience to match the attention head count. Different groupings could yield different CKA overlap patterns and different pruning outcomes.

## 4. Questions to Authors

1. Given that CKA overlap does NOT predict per-structure recoverability (Table 5, p=0.12), what is the mechanistic explanation for why RASP still outperforms Standard pruning? Is the benefit purely from the per-layer capacity floor rather than the CKA term itself?

2. Table 4 shows CKA contributes only 2-4pp marginal improvement (RASP 22.4 vs Gradient-only 20.1). Given the multi-seed variance of ±6.2pp (Table 2), is this CKA contribution statistically significant? Please provide a direct significance test.

3. The paper claims GRPO adds "only ~5pp" but Table 7 shows the pruning main effect is significant (p=0.003) while recovery is also significant (p=0.008). With no interaction (p=0.54), doesn't this actually support that GRPO helps uniformly regardless of pruning method — undermining the claim that recovery-aware pruning is needed?

4. Why does Standard Taylor pruning (7.6%) perform WORSE than Random pruning (4.2%) in some comparisons? If standard importance scoring actively hurts, this suggests the Taylor importance scores are inversely correlated with reasoning-critical structures. Have you verified the importance computation is correct?

5. The split-half CKA reliability is ρ=0.92, but the multi-seed RASP accuracy variance is ±6.2pp. How do you reconcile high CKA reliability with high downstream variance? Is the instability coming from the pruning execution (greedy selection near score boundaries) rather than the CKA scores themselves?

6. Self-Healing reports 95% recovery at 25% compression with unstructured pruning. Your best result at 20% structured sparsity is 47.7% recovery. To what extent is this gap attributable to (a) structured vs unstructured, (b) distilled vs base model, (c) different recovery protocols, (d) different evaluation? Have you run any unstructured pruning baselines on the same model for calibration?

7. What is the actual parameter reduction achieved? The paper reports "20% sparsity" but with per-layer 40% capacity floors, the effective parameter reduction may be substantially less than 20%. Please report actual parameter count before and after pruning.

## 5. Missing Experiments or Controls

- **Unstructured pruning baseline on the same model.** Without this, the comparison to Self-Healing (95% recovery) is confounded by too many variables. Even a single unstructured pruning + GRPO recovery datapoint at 20% would calibrate expectations.

- **Ablation of the per-layer 40% floor.** The floor was introduced to fix a bug (early layers collapsing to 14.3%). But it's now a major design choice. What happens with a 20% or 30% floor? Does RASP's advantage over Standard change?

- **RASP α sensitivity.** The paper uses α=1.0 throughout. The RASP score S(h) = I(h) × (1-F(h))^α — different α values weight the CKA term differently. An α sweep (0.5, 1.0, 2.0) with at least 2-3 seeds each would determine whether the CKA contribution is robust.

- **Second model.** At minimum, Qwen2.5-7B (non-distilled) or LLaMA-3-8B would establish whether the catastrophic sensitivity to structured pruning is specific to distilled reasoning models or general.

- **Recovery with more compute.** The GRPO phase uses only 2000 steps. Self-Healing may use substantially more recovery compute. A compute-matched comparison or a scaling curve (recovery accuracy vs GRPO steps) would clarify whether the low recovery is fundamental or just under-trained.

- **Per-layer pruning distribution analysis.** The paper mentions that pruning sensitivity is "predominantly layer-level" (ICC=0.73) but doesn't analyze which layers are most affected or how RASP vs Standard distribute their pruning across layers. A layer-wise pruning heatmap would be informative.

- **Inference speedup measurement.** Structured pruning's practical value is inference acceleration. The paper reports no latency or throughput measurements. Without these, the practical relevance of 20% structured sparsity is unclear.

## 6. Minor Issues

- The Methods section lists 6 pruning strategies (Standard Taylor, RASP, Magnitude-only, Gradient-only, GRASPrune, Bonsai) but the abstract and title frame the paper around 4 methods. Clarify which are primary methods vs ablation variants.

- Table 2 (multi-seed) has only 3 seeds — the minimum for computing a standard deviation but insufficient for robust variance estimation. 5+ seeds would be more convincing.

- The CKA computation uses q_proj activations only for attention heads (line 96 of cka_overlap.py). This captures query representations but misses key/value head behavior. For GQA architectures where KV heads are shared, the CKA overlap between query heads may not reflect the actual functional redundancy at the attention output level. Consider using post-attention (o_proj output) representations instead.

- The paper's F(h) is computed on the unpruned model. After pruning, the remaining heads' functional roles may shift. A post-prune CKA analysis would reveal whether the overlap structure is preserved.

- The eval prompt format ("Solve...put your final answer in \boxed{}") differs from the training format ("Question:...Answer: Let me think step by step."). This mismatch could underestimate pruned model accuracy if the pruned model is more sensitive to prompt format.

- Table 8 (sparsity sensitivity) reports "collapse" at 30% for both methods but doesn't define what "collapse" means quantitatively. RASP at 30% still achieves 2.8% post-prune — is this considered collapse?

## 7. Overall Assessment

This paper tackles an important and timely question: how does structured pruning interact with reasoning ability in LLMs, and can recovery training restore what pruning removes? The experimental design is comprehensive and the statistical methodology is above average for the pruning literature. The finding that 20% structured sparsity causes catastrophic reasoning collapse in a distilled model — with best recovery reaching only 47.7% of baseline — is a valuable negative result that challenges optimistic claims from the unstructured pruning literature.

However, the paper suffers from a fundamental framing problem: its proposed method (RASP with CKA-aware scoring) is not the best performer (GRASPrune is), and the core hypothesis that CKA functional overlap predicts recoverability is falsified by the data (p=0.12). The paper has pivoted from a methods contribution to an empirical analysis, but the current framing still implies RASP is a methodological advance. The high multi-seed variance (±6.2pp) further undermines confidence in pairwise method comparisons. The single-model limitation is significant given that the chosen model (distilled) is acknowledged to be unusually pruning-sensitive. The paper would be strengthened by (a) reframing honestly as a negative-result / empirical analysis paper, (b) adding an unstructured pruning baseline for calibration, (c) testing on at least one non-distilled model, and (d) resolving the F(h) definition inconsistency between the paper and code.

## 8. Score

**3 — Weak Reject.** The empirical findings are interesting (structured pruning catastrophically degrades reasoning; recovery is limited) but the paper's proposed method underperforms an external baseline, the core hypothesis is falsified by its own data, single-model evaluation limits generalizability, and the high variance across seeds makes most method comparisons unreliable. A significant revision with additional models and honest reframing could elevate this to a publishable empirical study.

## 9. Confidence

**4 — High.** I have read the code implementation, verified the CKA computation and pruning logic, cross-referenced the experimental design against the actual project state, and am familiar with the relevant literature (Self-Healing, GRASPrune, FANG, RL Squeezes). The one area of lower confidence is the GRPO recovery dynamics, where I rely on the reported numbers without independent verification of the training logs.
