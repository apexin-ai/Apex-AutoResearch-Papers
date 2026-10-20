# Response to Reviewers — R43

We thank both reviewers for their rigorous and constructive feedback. The central critique—that claims are stronger than evidence—is well-taken. We have performed a **systematic claim downgrade** throughout the paper: causal→correlational, prescriptive→exploratory, four-stage→three-stage contributions, and power-aware negative claims. Below we address each point with specific revisions.

---

## Must-Fix Responses

### MF1: Statistical Power — Negative Claims Need Power Qualification [R43-N1]
**Concern (R1 Must-Fix, R2 AGREE):** 2–3 seeds yield bootstrap CIs crossing zero (LP Δ 95% CI [−0.41, +2.54]). Cannot distinguish true null from insufficient power.

**Response:** Three changes address this:
1. **Limitations** now explicitly states: "Our negative selection claims are bounded by statistical power: with 2–3 seeds and MDE ≈1.5 pp, we cannot distinguish true null effects from small positive effects below detection threshold" (limitations.tex, line 6).
2. **§4** reports all selection gains with CI language: "LP achieves +0.2 pp (p=0.29), below MDE (≈1.5 pp at n=529, 2–3 seeds)" (single_signal.tex, line 39).
3. Throughout the paper, absolute negative claims ("fails", "no gain") are replaced with power-qualified language ("yields no detectable gains", "CI crosses zero").

**Paper location:** limitations.tex line 6, single_signal.tex lines 39–40, abstract.tex line 4.

---

### MF2: Bound Demoted from Independent Contribution [R43-N2]
**Concern (R1 Must-Fix, R2 AGREE):** §1 lists bound as one of four contributions, but §6.3 admits it's "intentionally loose." Framing inconsistency.

**Response:** The contribution structure is restructured from four stages to three:
1. **Discover** [§4]: QE signals achieve AUROC up to 0.82; instance-level decomposition reveals why correlation does not yield selection gains.
2. **Diagnose** [§4, §5, §6]: Diagnostic cascade—degeneracy, LP compression, signal alignment—quantifies failure mechanisms. The necessary condition bound (§6.3) is positioned *within* Diagnose as supporting analysis, not an independent contribution. Hidden-state probes reveal the introspection boundary (moved to Appendix reference).
3. **Construct (exploratory)** [§7.5]: Entity-level construction yields conditional gains under favorable diagnostic conditions.

The bound is no longer elevated as an independent contribution. §6.3 retains "intentionally loose necessary condition test" framing, now consistent with its role as a supporting diagnostic tool within the Diagnose stage.

**Paper location:** introduction.tex lines 23–31, §6.3 (theory.tex lines 27–29).

---

### MF3: Causal Language → Correlational/Observational [R43-N3]
**Concern (R1 Must-Fix, R2 strongly AGREE):** 11+ instances of causal language despite self-described observational design. §4 title implies causation.

**Response:** Systematic replacement across the paper (11 changes):
- **Abstract:** "jointly determine" → "are jointly associated with"
- **§1:** "jointly prevent selection" → "co-occur with selection failure"; added observational disclaimer: "our analysis is observational and all reported associations are correlational, not causal" (introduction.tex line 10)
- **§4 title:** "Where Single-Signal Selection Fails" → "Single-Signal Selection Results"
- **§4 body:** "effectively eliminating" → "leaving insufficient"
- **§6:** "localizes" → "identifies"
- **§8:** "localizing failure" → "identifying conditions associated with failure"; "eliminates...prevents" → "reduces...limits"
- **Discussion:** "prescriptive" → "preliminary check", "may warrant exploratory entity construction"

The paper now consistently uses correlational language throughout. The Few-NERD 3-vs-5 epoch comparison is explicitly framed as an observed association with a confound caveat, not a controlled experiment.

**Paper location:** abstract.tex line 5, introduction.tex line 10, single_signal.tex line 1 (title) and line 6, theory.tex, discussion.tex lines 8–9.

---

### MF4: Prescriptive → Exploratory [R43-N4]
**Concern (R2 Must-Fix, R1 AGREE):** Global Holm p_adj=0.055 is not significant. Per-family p_adj=0.006 relies on unregistered partition. Abstract places per-family before global, guiding attention to the more favorable number.

**Response:** Three changes:
1. **Contribution label:** "Prescriptive" → "Construct (exploratory)" in §1 (introduction.tex line 29).
2. **§7.5:** Opening paragraph and entity construction header now explicitly read "Entity-level construction (exploratory)" (experiments_main.tex line 104). Language changed from prescriptive recommendations to exploratory observations.
3. **Abstract p-value order swapped:** Now reads "global Holm p_adj=0.055, suggestive; per-family p_adj=0.006, post-hoc family partition" — global first, with explicit post-hoc annotation (abstract.tex line 6).

The paper no longer claims entity construction as a reliable prescriptive method. It is positioned as an exploratory finding under specific conditions, with transparent statistical caveats.

**Paper location:** abstract.tex line 6, introduction.tex line 29, experiments_main.tex lines 104, 109–110, discussion.tex line 9.

---

### MF5 (Divergent → Resolved): Title "Why" → "When" [R43-N5]
**Concern (R2 Must-Fix, R1 REBUT):** "Why SC Fails" is absolute; paper shows conditional success.

**Response:** Title changed to: **"When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap"** (main.tex line 28). "When" captures both the diagnostic (under what conditions does scaling fail?) and the conditional nature of findings (it sometimes succeeds).

---

## Should-Fix Responses

### SF1: Table 1 Dimension Overlap [R43-N6]
**Concern:** "Failure decomp." and "Diagnostics" overlap; Prescriptive row lacks p-value caveat.

**Response:** Table 1 reduced from 7 to 6 dimensions. "Failure decomp." and "Diagnostics" merged into a single "Diagnostic framework" row. "Prescriptive" row now reads "Conditional (p_adj=0.055)" to transparently signal statistical status.

**Paper location:** background.tex Table 1 (lines 24–34).

---

### SF2: Epoch Confound Baseline Difference [R43-W1]
**Concern:** 3-epoch model has lower greedy baseline; construction gains may partly reflect greater headroom.

**Response:** §7.5 now includes: "(note: 3-epoch greedy F1 0.748 vs 5-epoch 0.798; part of the larger Δ may reflect greater headroom under a weaker baseline)" (experiments_main.tex line 116). This explicitly flags the confound for readers.

---

### SF3: RE/SQL Abstract Reduction [R43-W2]
**Concern:** RE (n=397) and SQL (n=196) are too thin for "cross-task exploration."

**Response:** Abstract now reads "preliminary cross-task pilots (RE, SQL)" (abstract.tex line 3), further deemphasizing these extensions. Introduction frames them as "exploratory extensions" (line 14). No strong claims are made.

---

### SF4: Number Density [R43-W3]
**Concern:** Abstract has ~15 numerical values; §7 has 2–3 per sentence.

**Response:** Abstract numerical count reduced. Key numbers retained: AUROC 0.82, <1 pp selection gain, +1.40 pp entity construction, p-values (0.055, 0.006), 77–91% convergence collapse. Peripheral numbers (dataset counts, model sizes, seed counts) moved to Introduction or omitted from Abstract.

---

### SF5: Model Diversity [R43-W5]
**Concern:** Only Qwen + LLaMA; frontier degeneracy profiles differ substantially (5.5–74%).

**Response:** Limitations already states: "Frontier models exhibit markedly different degeneracy profiles (5.5–74%), suggesting findings from fine-tuned open-weight models may not fully generalize to proprietary systems" (limitations.tex line 1). This is an inherent scope limitation; we do not overclaim generalization.

---

### SF6: Practitioner Workflow [R43-W6]
**Concern:** §7.5 lacks concrete practitioner guidance.

**Response:** §7.5 now includes: "Practitioners can compute D and α on a pilot sample (N=8) to assess scaling viability before committing to repeated inference" (experiments_main.tex line 111). This provides actionable guidance: compute diagnostics cheaply before investing in full N-scaling.

---

### SF7: Missing References [R43-W8]
**Concern:** Malinin & Gales (2021) and Reflexion not discussed.

**Response:** Both added to §2 (Related Work):
- Malinin & Gales (2021) cited under "Uncertainty estimation and MBR" paragraph (background.tex line 16).
- Shinn et al. (2023, Reflexion) cited under "Test-time scaling and self-consistency" paragraph (background.tex line 5), with connection to our ESJ/MRSC negative results.

---

## Questions

### Q1: Bound Optimality
**Q:** Is the 3–12% recovery ratio optimal for this framework?

**A:** No. The bound is intentionally loose because diagnostic utility (screening) does not require quantitative precision. Two sources dominate looseness: (1) entity independence assumption (split-half r=0.395–0.578 reveals inter-entity correlation); (2) conservative α estimation as the instance minimum. Pursuing tighter bounds would require relaxing the independence assumption (entity-correlation-aware F1 decomposition), which we leave to future work. The key qualitative insight—α is 8–33× tighter than D—is robust regardless of bound tightness.

**Paper location:** §6.3 "Bound looseness" paragraph (theory.tex line 33).

---

### Q2: Free-Form RE Reversal
**Q:** LP selection reverses direction under free-form RE decoding. Is the gap decoding-strategy-dependent?

**A:** For NER, no: free-form ablation on SciERC, CoNLL, and Few-NERD shows LP std ratios of 0.97×, 0.86×, 1.00× respectively—LP compression is model-intrinsic. For RE, the reversal (+1.84±0.12 pp free-form vs −0.68 pp constrained) suggests the gap may be partially decoding-strategy-dependent in tasks where constrained decoding introduces format artifacts. This is task-specific and does not generalize to NER. Limitations notes the single-prompt-template scope.

**Paper location:** Appendix app:freeform_ablation, limitations.tex line 3.

---

### Q3: θ Selection Dependence
**Q:** θ∈[0.15, 0.35] across datasets—does this undermine pre-deployment diagnostics?

**A:** The θ sweep (Appendix app:theta_sweep) shows stable performance within this range; θ=2/N is a simple default that does not require held-out tuning. The practitioner diagnostic (compute D, α at N=8) assesses *whether* scaling is viable, not the optimal θ. If diagnostics indicate favorable conditions, θ=2/N is a reasonable starting point; grid search over θ would be a secondary optimization.

**Paper location:** experiments_main.tex line 105, Appendix app:theta_sweep.

---

### Q4: Degeneracy × Inverse Scaling Stratification
**Q:** Do high/low degeneracy subgroups show significantly different inverse scaling rates?

**A:** **Yes, strongly.** Post-hoc analysis across 4 datasets × N-transitions: degenerate instances show 1.3% inverse scaling rate vs non-degenerate instances 11.1% (OR=0.109, p<1e-300, Fisher's exact test). This is expected: degenerate instances produce identical entity sets across all N, so F1 is constant—they cannot exhibit inverse scaling by construction. Non-degenerate instances bear the full burden of threshold-sensitivity-driven inverse scaling. This directly supports the diagnostic framework: degeneracy partitioning identifies qualitatively different scaling regimes.

**Paper location:** Appendix app:degen_inverse (Table tab:degen_inverse), within §N-Scaling Detailed Analysis.
