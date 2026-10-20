# Paper Framing — min_necessary_circuit_css

> 最后更新: 2026-05-13 | 更新原因: D036 — IOI 正例死亡（size confound），0/6 PASS，Claim 4 降级

## Target Venue
EMNLP 2026 Findings (ARR deadline 2026-05-25)

## Title
Why Cross-Method Consensus Fails in Circuit Discovery

## Core Insight
Cross-method binary consensus in circuit discovery fails universally. Through systematic experiments on 4 tasks × 2 models (6 configurations), we find that CSS=1.0 never outperforms the best single method when circuit size is controlled. We identify three distinct failure modes: (1) ACDC's isinf binarization creates artificial sparsity that collapses consensus to a single method's output, (2) method correlation among gradient-based approaches reduces effective ensemble size (K=3 → K≈2), and (3) component-level scoring granularity on larger models (>100K edges) causes near-zero inter-method overlap. These findings provide actionable diagnostic guidelines for practitioners considering multi-method circuit validation.

## Narrative Arc
1. Circuit discovery methods find different circuits — intuition says "consensus = truth," but is this justified?
2. We test this intuition systematically with CSS (binary consensus) across K=3 methods on multiple tasks and models
3. CSS fails on all 6 task×model configurations — the only apparent success (IOI) is a size artifact (size-controlled experiment confirms)
4. We identify three mechanistic failure modes with distinct signatures
5. Universal negative result + failure mode taxonomy = actionable practitioner guidelines

## Core Claims

### Claim 1: ACDC isinf binarization pathology (METHODOLOGICAL — strongest)
- **Evidence**: CSS=1.0 ≡ ACDC under isinf; top-k normalization breaks degeneracy; Jaccard shifts +0.16 to +0.25 across tasks; size-controlled experiment shows CSS=1.0 CPR = ACDC top-16 CPR (identical at 0.0295)
- **Status**: Fully demonstrated on IOI + Arithmetic + SVA (3 tasks). Size-controlled result strengthens: consensus is literally ACDC's subset
- **Strength**: ★★★★★ — concrete, reproducible, actionable

### Claim 2: CSS fails universally across task×model configurations (EMPIRICAL)
- **Evidence**: 0/6 configurations show CSS=1.0 CPR advantage over best single method when size is controlled. IOI apparent advantage was size confound (7 vs 100 edges); size-controlled N=16 shows CSS=1.0 ≤ EAP-IG/EP. Arithmetic FAIL (J=0.70), Factual Recall FAIL (J=0.82, gradient-pair dominance), SVA inconclusive (Δ<0.01), Qwen×2 zero overlap
- **Three failure modes**: (a) ACDC isinf binarization pathology (Claim 1), (b) method correlation reduces effective K (gradient-pair dominance: EAP-IG×EP J=0.82 on Factual Recall), (c) component-level scoring granularity collapse (Claim 3)
- **Status**: All 6 configs evaluated. IOI size-controlled baseline completed
- **Strength**: ★★★★★ — clean universal negative with mechanistic explanation

### Claim 3: Component-level scoring causes scaling failure (MECHANISTIC)
- **Evidence**: On Qwen-0.5B (179K edges), both IFR and ACDC degenerate to node-level scoring; top-0.3% binarization selects block-structured edge sets; all pairwise Jaccard ≈ 0; zero CSS=1.0 edges
- **Status**: Demonstrated with two independent methods (IFR D028, ACDC D034)
- **Strength**: ★★★★ — root cause identified, not fixable by method substitution

### Claim 4: CIRCUS (within-method threshold diversity) fails completely (COMPARATIVE)
- **Evidence**: CIRCUS produces negative CPR on all tested tasks; cross-method consensus is necessary but not sufficient
- **Status**: D021 documented 3× failure
- **Strength**: ★★★ — negative ablation, depends on implementation correctness caveat

## Discussion Observations (not independent claims)

### Jaccard as diagnostic signal
- **Finding**: max Jaccard > 0.5 → CSS always fails (4/4 cases); max Jaccard < 0.35 → CSS also fails (1/1 case, IOI after size control)
- **Implication**: With 0/6 PASS, Jaccard can only predict "always fail" — no positive regime exists in our evaluation. Presented as observation with caveat that diagnostic value depends on existence of positive cases
- **Note**: Gradient-pair correlation (EAP-IG×EP) drives max Jaccard on 3/4 GPT-2 tasks — "method correlation reduces effective K" pattern

### Method correlation / gradient-pair dominance
- **Finding**: On Factual Recall, EAP-IG×EP J=0.82 — two gradient methods nearly identical, K=3 effectively K≈2, consensus dominated by correlated pair
- **Implication**: Discussed under Claim 2 failure modes as structural issue. Use terminology "method correlation reduces effective K" rather than "vote stuffing"

## Anticipated Reviewer Concerns

### R1: "This is just a negative result, what's the contribution?"
- **Response**: Three concrete contributions: (a) binarization pathology + fix, (b) scaling failure root cause (component-level scoring), (c) failure mode taxonomy with diagnostic guidelines. Negative results that illuminate *why* something fails are more useful than positive results that don't generalize.

### R2: "CSS is just the feature selection stability index (Nogueira & Brown 2016)"
- **Response**: Acknowledged explicitly in Related Work. Our contribution is not the mathematical framework but the systematic empirical characterization of when/why it fails in circuit discovery, plus domain-specific failure modes.

### R3: "IOI positive result could be size effect" — RESOLVED
- **Response**: Confirmed. Size-controlled baseline (N=16) shows CSS=1.0 CPR = ACDC top-16 CPR (zero: 0.0295, identical) and CSS=1.0 CPR(mean) < EAP-IG/EP. IOI advantage was entirely size confound. This strengthens the universal negative finding.

### R4: "Only GPT-2 Small + Qwen 0.5B, limited model coverage"
- **Response**: Two models at different scales (32K vs 179K edges) already reveal the scaling failure. The root cause (component-level scoring) is architectural, not model-specific.

### R5: "EAP-IG and EP are gradient-adjacent, K=3 is effectively K≈2"
- **Response**: This is part of our finding, not a limitation — method correlation is a structural failure mode we characterize. Even ACDC (greedy causal, different paradigm) doesn't help: under isinf, consensus collapses to ACDC alone.

### R6: "No confidence intervals on CPR differences"
- **Response**: Bootstrap CIs computed for SVA (p=0.099, not significant) and Factual Recall (p=0.000, significantly negative). IOI Bootstrap CI pending (~30 min). Size-controlled comparison already demonstrates no advantage independent of CI.

## Competitors
- **CIRCUS** (Parekh 2026): Within-method threshold diversity; our negative ablation
- **Mondorf et al.** (2510.06811): Cross-method score averaging; must acknowledge continuous averaging may outperform binary consensus
- **PIE** (2604.16889): Iterative pruning ensemble; single paradigm
- **Nogueira & Brown** (JMLR 2016): Feature selection stability; CSS is domain application, must cite
- **Kuncheva & Whitaker** (2003): Ensemble diversity theory; theoretical foundation for our failure mode analysis
