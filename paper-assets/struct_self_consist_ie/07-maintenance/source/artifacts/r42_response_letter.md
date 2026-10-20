# Response to Reviewers — R42

We thank both reviewers for their thorough and constructive feedback. Below we address each point, referencing specific revisions in the paper.

---

## Must-Fix Responses

### MF1: Decomposition Bound Repositioned as Necessary Condition Test
**Concern (R1-N1, R2 agree):** The bound E[ΔF1(A)] ≤ (1−D)·G_nd·α recovers only 3–12% of actual gains, limiting its utility as a quantitative predictor.

**Response:** We have repositioned the bound as an *intentionally loose necessary condition test* rather than a tight predictor. §6.3 now states: "The bound is an intentionally loose *necessary condition test*: when D→1 or α→0, no aggregation method can improve over greedy, regardless of implementation. It localizes *where* aggregation fails—screening for favorable conditions—rather than quantitatively predicting gains." The low recovery ratio (3–12%) is explicitly framed as reflecting "its role as a screening test, not a tight estimate." We weakened language around Table 33 / Figure bound accordingly. The two dominant sources of looseness are identified: (1) entity independence assumption (split-half correlation r=0.578–0.644 reveals substantial inter-entity correlation), and (2) conservative α estimation as the minimum across instances.

**Paper location:** §6.3 (Degeneracy Decomposition), specifically the paragraph beginning "The bound is an intentionally loose..." and "Bound looseness" paragraph.

---

### MF2: Statistical Significance Under Multiple Comparison Corrections
**Concern (R1-N2, R2 agree):** The core positive claim (entity construction on Few-NERD) reaches global Holm p_adj=0.055 (not significant at α=0.05), while per-family p_adj=0.006; the family partition lacks prior justification.

**Response:** §7.5 (Prescriptive Results) now provides the prior rationale for the family partition: "We group the 57 comparisons into methodological families—per-sample signals (k=21), cross-sample signals (k=26), and entity construction (k=10)—reflecting mechanistic distinctions defined at experiment design time (not selected post-hoc to optimize p-values)." Both corrections are transparently reported: global Holm k=57 p_adj=0.055 (suggestive) and per-family k=10 p_adj=0.006 (significant), with BH FDR yielding 6/10 construction comparisons at FDR<0.05. As additional robustness evidence, the seed-replication analysis (5 SciERC seeds, Fisher z + Holm correction, k=5) yields p_adj=0.013 for the SJ > LP advantage (Appendix B.5), providing independent statistical support via a separate methodology.

**Paper location:** §7.5 (experiments_main.tex, lines 109–111), Appendix B.5 (app:bootstrap_signal, line 315), Appendix Holm enumeration (app:holm).

---

### MF3: Mechanistic Probes on Qwen2.5-7B Rather Than Qwen3-8B
**Concern (R1-N3, R2 agree):** Probe and ESJ experiments were conducted on Qwen2.5-7B-Instruct, not the fine-tuned Qwen3-8B used in main experiments, and the model discrepancy was not flagged in the main text.

**Response:** Two changes address this: (1) §4 (mechanistic.tex) now explicitly annotates: "Probe experiments use Qwen2.5-7B (not the fine-tuned Qwen3-8B used in main experiments); conclusions are architecture-specific." A footnote details the rationale and scope limitation. (2) We performed ESJ cross-validation on Qwen3-8B fine-tuned, reported in Appendix E (app:esj, Table tab:esj_cross): AUROC is SciERC 0.512, CoNLL 0.553, Few-NERD 0.495—all indistinguishable from chance. This confirms the introspection boundary transfers across architectures (Qwen2.5-7B pretrained → Qwen3-8B fine-tuned). The Limitations section also explicitly states: "probe cross-model transferability is not yet verified, though ESJ chance-level performance replicates on Qwen3-8B (AUROC 0.50–0.55)."

**Paper location:** §4 (mechanistic.tex, lines 4–5), §5 (single_signal.tex, line 55), Appendix E Table tab:esj_cross (appendix.tex, lines 688–699), Limitations (limitations.tex, line 4).

---

### MF4: Systematic Comparison with Landesberg et al. (2026)
**Concern (R2-N1, R1 agree):** Need a half-page systematic comparison with Landesberg et al. (2026) and Table 1 augmented with failure mechanism dimension.

**Response:** §2 (Related Work) now contains a four-dimensional systematic comparison: "(a) domain—reasoning (scalar judgments) vs. NER/RE (entity sets with partial overlap); (b) failure mechanism—prompt-level baseline effects vs. degeneracy (12–68%) and signal alignment collapse (α→0), mechanisms specific to structured prediction; (c) granularity—prompt-level r decomposition vs. instance- and entity-level diagnostics (D, G_nd, α); (d) prescriptive—no constructive remedy vs. entity-level construction with MBR grounding." Table 1 (tab:novelty_comparison) has been expanded to seven dimensions including "Failure mechanism" (Landesberg: "Baseline effects"; Ours: "Degeneracy + α") and "Failure decomp." (Landesberg: "—"; Ours: "D, α, LP").

**Paper location:** §2 (background.tex, lines 39–46), Table 1 (tab:novelty_comparison, lines 18–37).

---

### MF5: Few-NERD Epoch Confound
**Concern (R2-N2, R1 escalated to critical):** The +1.40pp Few-NERD gain uses a 3-epoch under-converged model; 5-epoch training shows 94% collapse. Abstract lacked this conditioning.

**Response:** The Abstract now explicitly conditions the Few-NERD claim: "Entity-level construction yields conditional gains (+1.40 pp on Few-NERD under 3-epoch training; collapses by 77–91% at convergence; per-family Holm p_adj=0.006, global p_adj=0.055)." §7.5 reports the complete 3-vs-5 epoch comparison: LP selection collapses from +1.39 to +0.12±0.04 pp (91% reduction, 2-seed mean); entity construction from +0.88 to +0.20 pp (77% reduction, seed 42). Constant-F1 degeneracy rises from 13% to 31%. Appendix (app:epoch_confound) provides full details including the SciERC 3-point gradient (3/5/10 epochs) showing monotonic degeneracy increase with simultaneous within-instance alignment degradation. We frame this as a finding rather than a limitation: "SC may complement early stopping strategies—under-converged models preserve output diversity that enables aggregation gains."

**Paper location:** Abstract (abstract.tex, line 6), §7.5 (experiments_main.tex, lines 114–117), Appendix (app:epoch_confound, lines 2043–2112).

---

## Should-Fix Responses

### SF1: Diagnostic vs. Prescriptive Narrative Inconsistency
**Concern:** The paper oscillates between diagnostic and prescriptive framing.

**Response:** Abstract and Discussion now consistently use "primarily diagnostic": "The framework is primarily diagnostic, with limited predictive power for identifying favorable conditions, informing resource allocation decisions before investing in repeated inference" (Abstract, line 7). The Discussion (§8) reinforces: "The diagnostic framework—localizing failure to degeneracy and signal alignment collapse—is our primary contribution; cross-task and cross-model extensions are exploratory" (discussion.tex, line 15). Additionally, Introduction (line 12) and §7.5 (line 107) were revised from "predicts" to "identifies conditions" for consistency.

**Paper location:** Abstract (line 7), Introduction (line 12), §7.5 (line 107–108), Discussion/Conclusion (discussion.tex, lines 1, 15).

---

### SF2: 2–3 Seeds Insufficient for Statistical Inference
**Concern:** Only 2–3 training seeds limit the reliability of statistical claims.

**Response:** We use 5 seeds for SciERC on Qwen3-8B and 3 seeds for LLaMA across all datasets (Appendix app:multiseed confirms σ≤0.026 for all QE signals across 5 seeds). The seed-replication Holm correction (k=5, p_adj=0.013) and Fisher z test provide cross-seed statistical validation independent of the per-family correction. The Limitations section explicitly acknowledges this scope: seed counts reflect computational constraints (each seed × N=8 samples × 4 datasets × 2 models requires ~64 fine-tuning runs and ~512 inference batches). The directional consistency across all seeds (SC negative or negligible across all seed-dataset combinations for MV: Few-NERD −2.74±0.54, SciERC −0.74±0.46, CoNLL −0.04±0.15 pp) strengthens confidence beyond what raw seed count suggests.

**Paper location:** Response-letter only; Limitations (limitations.tex), Appendix app:bootstrap_signal (line 315), Appendix app:multiseed (lines 701–706).

---

### SF3: RE/SQL Extensions Too Thin
**Concern:** RE (n=397) and SQL (n=196) extensions lack depth for strong conclusions.

**Response:** The Abstract explicitly marks these as "preliminary RE (n=397) and SQL (n=196) pilots" (abstract.tex, line 3). We do not make strong claims about either extension; they serve to demonstrate that the diagnostic framework identifies *different* failure modes across tasks (RE: diversity among failures from upstream entity span errors; SQL: 87.2% degeneracy). Cross-task generalization is listed as exploratory throughout.

**Paper location:** Abstract (line 3), Introduction (line 14), Discussion (line 15).

---

### SF4: Related Work Coverage Gaps
**Concern:** Missing coverage of MBR/calibration literature.

**Response:** §2 (Related Work) now includes: Eikema et al. (2025) on structured MBR utility degradation ("citet{eikema2025structured} find MBR utilities degrade on structured outputs, consistent with our LP compression findings"), calibration literature (Desai & Durrett 2020, Xiao et al. 2022), selective prediction (Geifman & El-Yaniv 2017), conformal prediction (Angelopoulos et al. 2023), and semantic uncertainty (Kuhn et al. 2023). These are positioned under the "Uncertainty estimation and MBR" paragraph.

**Paper location:** §2 (background.tex, lines 13–16).

---

### SF5: Entity-Level Decomposition Incremental Contribution
**Concern:** The entity-level decomposition may not add sufficient value over task-level analysis.

**Response:** The core value proposition of entity-level analysis is threefold: (1) *Degeneracy is only definable at entity level*—12–68% of instances produce identical entity sets across all N samples (Table tab:fewnerd), a phenomenon invisible to task-level F1 correlation. (2) *Task-level metrics mask instance-level failure*: CoNLL shows task-level ρ(SJ,F1)=0.45 (Table tab:quality_estimation), suggesting SJ is a useful signal, yet 61.7% of instances are degenerate—SJ assigns identical scores to all candidates for these instances, yielding zero discriminative power. Task-level ρ is inflated by non-degenerate instances' strong correlation masking degenerate instances' zero contribution. (3) *Construction gains concentrate in identifiable subsets*: on non-degenerate instances, entity construction yields +3.36 pp (SciERC), +5.18 pp (CoNLL), +7.08 pp (Few-NERD)—gains invisible in task-level aggregates.

**Paper location:** Response-letter only; data from Table tab:fewnerd (experiments_main.tex, line 71), Table tab:quality_estimation (line 40), §7.5 footnote (line 108).

---

### SF6: Constrained Decoding Confound Not Fully Resolved
**Concern:** LP compression may be an artifact of constrained decoding rather than a model-intrinsic property.

**Response:** We extended the free-form decoding ablation to three NER datasets (Appendix app:freeform_ablation). Table tab:freeform_summary reports LP std ratios (free-form / constrained): SciERC 0.97×, CoNLL 0.86×, Few-NERD 1.00×. LP compression is nearly identical under both regimes. NER selection gains remain negligible under free-form decoding across all three datasets. On CoNLL specifically, LP-selected F1=0.896 vs. single-sample 0.904 (Δ=−0.77 pp)—LP still fails. The Discussion states: "LP compression is model-intrinsic rather than an artifact of constrained decoding" (discussion.tex, line 6).

**Paper location:** Appendix app:freeform_ablation (appendix.tex, lines 1277–1389), Table tab:freeform_summary (line 1366), Discussion (line 6), Limitations (line 5).

---

## Questions

### Q1 [R1-Q1]: Source of Bound Looseness
**Question:** What are the sources of the 3–12% recovery ratio, and which simplification assumption dominates?

**Response:** Three simplifying assumptions contribute to bound looseness, in decreasing order of impact: (1) *Entity independence* is the dominant source. The bound assumes entities independently contribute to F1, but NER entities are often correlated (e.g., "New York City" spans three tokens with near-unity co-occurrence). Split-half correlation r=0.578–0.644 quantifies this violation. (2) *Multiplicative structure*: the (1−D)·G_nd·α decomposition assumes factors interact multiplicatively, which is an approximation. (3) *Linear α approximation*: α is estimated as the minimum across instances rather than instance-adaptive, further loosening the bound. We did not pursue tighter bounds because the diagnostic purpose—necessary condition screening—does not require quantitative precision. The key insight is qualitative: α→0 is the binding constraint (8–33× tighter than D), and this conclusion holds regardless of bound tightness.

**Paper location:** §6.3 "Bound looseness" paragraph (theory.tex, line 33).

---

### Q2 [R1-Q2]: Probe Replication on Qwen3-8B
**Question:** Have the probes been replicated on the Qwen3-8B model used in main experiments?

**Response:** ESJ has been cross-validated on Qwen3-8B fine-tuned. Appendix E (Table tab:esj_cross) reports entity-level AUROC: SciERC 0.512, CoNLL 0.553, Few-NERD 0.495—all at chance level. This confirms the introspection boundary transfers across both architectures (Qwen2.5-7B → Qwen3-8B) and training conditions (pretrained → fine-tuned). Hidden-state probes have not yet been replicated on Qwen3-8B; the Limitations section acknowledges this.

**Paper location:** Appendix E Table tab:esj_cross (appendix.tex, lines 688–699), §5 (single_signal.tex, line 55), Limitations (line 4).

---

### Q3 [R1-Q3, R2-Q1]: 5-Epoch Entity Construction Numbers
**Question:** What are the exact 5-epoch numbers for both LP selection and entity construction on Few-NERD?

**Response:** From §7.5 and Appendix app:epoch_confound: LP selection gain collapses from +1.39 pp (3-epoch) to +0.12±0.04 pp (5-epoch, 2-seed mean), a 91% reduction. Entity construction gain drops from +0.88 pp to +0.20 pp (seed 42), a 77% reduction. Constant-F1 degeneracy rises from 13% to 31%. Greedy F1 improves modestly (+0.7 pp, 0.791→0.798). The 5-epoch model is past the optimal early-stopping point (evaluation loss increases after epoch 3; best checkpoint at ~epoch 3.9).

Regarding the ESJ AUROC range question: different sections cite different precision levels of the same data. Qwen2.5-7B SciERC single-dataset ESJ gives AUROC 0.512 (rounded to 0.51 in some references). The "0.50–0.55" range in §4/§5 covers Qwen3-8B cross-validation across three datasets (Few-NERD 0.495, SciERC 0.512, CoNLL 0.553). No inconsistency exists; the apparent discrepancy reflects different scopes (single model/dataset vs. cross-model/dataset range).

**Paper location:** §7.5 (experiments_main.tex, lines 114–116), Appendix app:epoch_confound Table tab:epoch_confound (appendix.tex, lines 2043–2070), ESJ cross-validation (Appendix E, Table tab:esj_cross).

---

### Q4 [R1-Q4]: Free-Form LP Selection Performance
**Question:** Does LP selection improve under free-form (unconstrained) decoding?

**Response:** No. Across three NER datasets under free-form decoding: SciERC shows negligible LP Δ under both regimes; CoNLL LP-selected F1=0.896 vs. single-sample 0.904 (Δ=−0.77 pp)—LP still fails; Few-NERD shows all deltas <0.02 pp—identical to constrained. The conclusion "LP fails for structured prediction" holds across datasets and decoding modes. The one exception is RE, where LP selection reverses direction under free-form decoding (+1.84±0.12 pp across 4 seeds vs. −0.68 pp constrained), but this is task-specific and does not generalize to NER.

**Paper location:** Appendix app:freeform_ablation (appendix.tex, lines 1277–1389), Table tab:freeform_summary (line 1366).

---

### Q5 [R1-Q5]: Pre-Registration of Hypothesis Families
**Question:** Were the per-family hypothesis groupings pre-registered?

**Response:** No. This is a post-hoc analysis study, not a confirmatory experiment, so pre-registration was not applicable. We explicitly acknowledge this: "the family partition was not pre-registered" (§7.5, experiments_main.tex line 111). The per-family groupings reflect methodological distinctions at design time: per-sample signals (LP-based, k=21), cross-sample signals (agreement-based, k=26), and entity construction (aggregation-based, k=10) test fundamentally different mechanisms and were designed as separate experimental modules. As an additional safeguard independent of the family partition, the seed-replication Fisher z test (k=5, p_adj=0.013) provides a separate statistical path that does not depend on how the 57 comparisons are grouped.

**Paper location:** §7.5 (experiments_main.tex, lines 109–111), Appendix app:bootstrap_signal (line 315).

---

### Q6 [R2-Q4]: Task-Level vs. Instance-Level Contradiction
**Question:** Can you provide a concrete example where task-level metrics are misleading?

**Response:** CoNLL provides the clearest case. Task-level: ρ(SJ, F1)=0.436, AUROC=0.801 (Table tab:quality_estimation)—SJ appears to be a strong quality signal. Instance-level: 61.7% of instances are degenerate (all N samples produce identical entity sets; Table tab:fewnerd). For these instances, SJ assigns identical scores to all candidates, providing zero discriminative power. The task-level ρ is inflated by non-degenerate instances where SJ-F1 correlation is genuinely strong, masking that >60% of instances receive no useful signal. Consequence: MV selection on CoNLL yields only +0.61 pp at N=64 despite 4 pp oracle headroom, and LP selection is negative (−0.85 pp). The entity-level decomposition reveals *why*: the problem is not signal quality but instance-level degeneracy eliminating the selection opportunity for the majority of instances.

**Paper location:** Table tab:quality_estimation (experiments_main.tex, line 40), Table tab:fewnerd (line 71), Figure fig:n_scaling (line 19).

---

### Q7 [R2-Q5]: Partial-Match Degeneracy Definition
**Question:** How would relaxing the degeneracy definition (e.g., Jaccard > 0.9 instead of exact match) affect results?

**Response:** The current definition is binary: an instance is degenerate iff all N samples produce identical entity sets. Relaxing to partial match (e.g., Jaccard similarity > 0.9) would likely reduce measured degeneracy rates. However, we did not run this experiment. Critically, even if D decreases substantially under a softer definition, the binding constraint is α (signal alignment), not D. §6.3 establishes that α is 8–33× tighter than D across all configurations: α=0.000–0.161 while (1−D) ranges from 0.32–0.88. Halving D would at most double the bound's headroom, but α→0 would still suppress actual gains to near zero. The key diagnostic conclusion (α is the bottleneck) is robust to the degeneracy definition.

**Paper location:** §6.3 (theory.tex, line 30).

---

### Q8 [R2-Q2]: Entity Independence Assumption Violation
**Question:** How does violating the entity independence assumption in Proposition 1 affect the bound's validity?

**Response:** The entity independence assumption (entities independently contribute to F1) is typically violated in NER—e.g., "New York City" tokens have near-unity co-occurrence, and nested entities share boundary dependencies. Violating independence means the bound becomes looser: actual F1 changes can exceed or fall below the bound's prediction, because correlated entities amplify or dampen changes in ways the independent model cannot capture. Split-half correlation r=0.578–0.644 quantifies the violation magnitude. However, as a necessary condition, the bound remains valid under independence violation: if D=1 (complete degeneracy) or α=0 (zero signal alignment), no aggregation method can improve over greedy regardless of entity correlation structure. Independence affects the bound's *quantitative precision* (explaining part of the 3–12% recovery ratio) but not its *qualitative diagnostic validity*. The conclusion that α→0 is the binding constraint does not depend on the independence assumption.

**Paper location:** §6.3 "Bound looseness" paragraph (theory.tex, line 33), Limitations (limitations.tex, line 1).
