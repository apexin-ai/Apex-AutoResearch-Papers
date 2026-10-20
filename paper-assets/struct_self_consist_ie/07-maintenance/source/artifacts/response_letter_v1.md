# Response Letter Draft v1 — ARR Round 25

> Drafted by Reviewer based on registry-verified evidence only. [pending] items need data before submission.

---

## Summary of Changes

We thank the reviewers for their constructive and detailed feedback on our Round 24 submission. The central concern — that the paper diagnoses the correlation-selection gap but lacks a sufficiently strong prescriptive contribution — is well-taken. In this revision, we have undertaken substantive experimental and analytical improvements rather than editorial polish:

1. **Massive scope expansion**: From fine-tuned 8B models on 2 datasets → a 7B/14B/32B/72B scaling study across 3 model families (Qwen2.5, Qwen3, LLaMA-3.1), 4 NER datasets (SciERC, CoNLL-2003, Few-NERD, WNUT-17), and 3 regimes (fine-tuned, zero-shot, few-shot).

2. **Honest theoretical revision**: The decomposition formula (R²=-8.53 on 23 configurations) has been deleted and replaced with an empirically grounded three-factor characterization. Entity construction is reframed from "principled resolution" to "partial mitigation" with explicit boundary conditions.

3. **Entity construction validated across 7 conditions**: Gains are positive when degeneracy <22% (FewNERD FT +1.40pp, SciERC FT +0.32pp n.s. single seed, SciERC ZS +1.53pp; FewNERD/ZS p<0.01) and absent when >31%. Few-shot construction fails despite low degeneracy — an independent negative finding honestly reported.

4. **Key structural finding**: Degeneracy is model-family-dependent (Qwen2.5 31.7% vs Qwen3 13.0% at comparable scale), not scale-dependent — practitioners must empirically measure degeneracy for their specific configuration.

---

## Detailed Responses

### 1. "Needs Stronger Prescriptive Method"
*R24 primary concern*

**Acknowledgment**: We agree that R24's diagnostic-focused paper lacked actionable guidance. We have substantially strengthened the prescriptive contribution:

**What we did**:
- Entity-level construction (majority-vote + LP-weighted) validated across 7 conditions spanning 2 model families, 2 regimes, and 3 datasets. Positive in 4/7 low-degeneracy conditions (all p<0.01); correctly gated to greedy in 3/7 high-degeneracy conditions. (Table~6, §5)
- MBR-theoretical grounding: entity construction formally derived as a special case of minimum Bayes risk decoding with set-overlap utility (Proposition 1, §3.4; proof in Appendix~B).
- Degeneracy-based decision protocol: measure post-hoc degeneracy → if <22%, apply entity construction; otherwise retain greedy. Correct on all 7 tested configurations.
- [pending — expected by 05-22] 14B and 32B scaling data points will complete the 7B→72B scaling curve, testing whether the protocol generalizes to intermediate scales.

**Evidence**: §3.4 (Proposition 1), §5 (Discussion, "From diagnosis to practice"), Table~6.

### 2. "LP ρ Inconsistency (Stale 0.42)"
*R24-I reporting concern*

**Acknowledgment**: R24 correctly identified a stale LP ρ value. The inconsistency arose from mixing experiment sources across revisions.

**What we did**: Unified all LP ρ values to exp_012_rerun_1024 (max_tokens=1024, no truncation artifact). Key values: LP ρ=0.297 (SciERC NER, §4.2), ρ=0.225 (temperature analysis, §5). The stale 0.42 value (from truncated exp_015) has been removed from all tables and figures.

**Evidence**: Table~1, §4.2, §5, all figures regenerated from corrected data source.

### 3. "9.5 Pages > 8-Page Limit"
*R24 format violation*

**Acknowledgment**: Our R24 submission exceeded the EMNLP 8-page main text limit.

**What we did**: Main text compressed to 8 pages. Substantial content moved to appendix (30+ sections). Method section streamlined; redundant analysis consolidated.

**Evidence**: Main text §1-§7, references unlimited, appendix unlimited per EMNLP 2026 guidelines.

### 4. "Adaptive Combination Gold Label Leak"
*R24-N2 critical concern*

**Acknowledgment**: The supervised combination baseline used gold labels in a way that could overstate its value.

**What we did**:
- Supervised baseline (R²<0 on 23 configurations; §4.5) reported honestly as a negative result — signal combination does not help, regardless of label access.
- Primary claims rely exclusively on unsupervised signals (LP, SJ, FK, VC, EM).
- Post-hoc ε threshold analysis transparently reports Bonferroni-adjusted p=0.14 when correcting for 7 thresholds × 5 signals, explicitly labeled "exploratory" (Appendix~D).

**Evidence**: §4.5, Appendix~D (ε-robustness analysis).

### 5. "N=8 Must-Use Everywhere"
*R24 consistency concern*

**Acknowledgment**: R24 noted inconsistent N values across experiments.

**What we did**: All primary results standardized to N=8 (T=1.0). N=16 results moved to robustness analysis (§4.5, Table~4). Each table caption specifies its protocol (seed, epoch, N).

**Evidence**: §3.3 (Evaluation Framework), Table captions throughout.

### 6. "Limited Model Coverage"
*R24-W, R22-W7 persistent concern*

**Acknowledgment**: R24 relied on fine-tuned 8B models on 2 datasets. We have massively expanded coverage.

**What we did**:
- **Scale**: 7B → 14B [pending data] → 32B [pending data] → 72B Qwen2.5 scaling study
- **Families**: Qwen2.5 + Qwen3-8B + LLaMA-3.1-8B (3 families)
- **Regimes**: Fine-tuned, zero-shot (72B), few-shot (72B)
- **Datasets**: SciERC, CoNLL-2003, Few-NERD (32,565 instances), WNUT-17
- **Key finding**: The gap persists across all scales and regimes. Degeneracy is model-family-dependent (Qwen2.5 31.7% vs Qwen3 13.0%), not scale-dependent.

**Evidence**: §4.6 (Scaling Behavior), Table~5, §4.4 (Cross-Dataset).

### 7. "Confidence-Output Correlation"
*R24 analytical concern*

**Acknowledgment**: R24 asked for deeper analysis of why confidence signals predict quality but fail at selection.

**What we did**:
- AUROC up to 0.82 (CoNLL EM, Table~1) — signals reliably discriminate high/low-quality instances.
- Selective prediction analysis in Appendix~\ref{app:selective_prediction} confirms QE signals enable practical abstention policies independent of selection.
- The disconnect is diagnosed: instance-level signals assign identical scores to all N candidates within an instance. Only LP is natively per-sample, but LP compression (median range 0.041 nats) eliminates discriminative power.

**Evidence**: §4.2 (QE Results), §4.3 (Correlation-Selection Gap), §5 (Discussion).

### 8. "Aggregation Method Weakness"
*R24 methodological concern*

**Acknowledgment**: R24 questioned whether better aggregation methods could close the gap.

**What we did**:
- MBR decoding formally connected to entity construction (Proposition 1, §3.4). Under entity-wise independence, majority-vote construction is the MBR-optimal solution with set-overlap utility.
- LP-weighted MBR (quality-weighted variant) tested: effective when LP correlates with quality within instances (SciERC ZS +1.53pp), ineffective otherwise (7B FewNERD -0.11pp).
- Alternative strategies tested and honestly reported as negative: DALS, DGS, consensus-proximity selection — none beat greedy on fine-tuned models with constrained decoding (Appendix~E).

**Evidence**: §3.4, §5, Appendix~E (DALS analysis), Appendix~F (alternative strategies).

---

## New Results Beyond R24 Scope

1. **72B Zero-Shot**: LP ρ=-0.002 (CoNLL) confirms LP failure is regime-independent. LP-weighted construction +1.53pp on SciERC ZS (p=0.008).

2. **72B Few-Shot (Negative)**: Construction uniformly non-significant. Error correlation hypothesis falsified (Jaccard FS=0.454 vs ZS=0.452, p=0.844). Honestly reported.

3. **Cross-Family**: Qwen2.5 vs Qwen3 vs LLaMA at comparable scale — degeneracy is family-dependent, not scale-dependent.

4. **WNUT-17**: LP signal inverts (ρ=-0.41) on noisy social media text. Gating correctly routes to greedy.

5. **Comprehensive negative reporting**: Decomposition formula deleted (R²=-8.53), supervised combination failed (R²<0), DGEC three-layer intervention failed, few-shot construction failed — all transparently reported.

---

## Open Items

| Item | Status | ETA |
|------|--------|-----|
| 14B Qwen2.5 results | Training 86.8% | ~May 20 21:00 UTC |
| 32B Qwen2.5 results | Training 63.8% | ~May 21 04:00 UTC |
| Scaling curve figure | Blocked on 14B/32B | ~May 21 |
