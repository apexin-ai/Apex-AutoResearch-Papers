# Paper Framing — min_necessary_circuit_css

> 最后更新: 2026-05-13 | 更新原因: D034 后 reframe 为分析论文（Route A）

## Target Venue
EMNLP 2026 Findings (ARR deadline 2026-05-25)

## Core Insight
Cross-method binary consensus in circuit discovery fails more often than it succeeds. Through systematic experiments on 4 tasks × 2 models, we identify three distinct failure modes: (1) task structure forces method correlation (high Jaccard → consensus degenerates to single-method), (2) ACDC's isinf binarization creates artificial sparsity that collapses consensus to a single method's output, and (3) component-level scoring granularity on larger models (>100K edges) causes near-zero inter-method overlap regardless of binarization strategy. These findings provide actionable diagnostic guidelines: check pairwise Jaccard before investing in multi-method validation, normalize binarization thresholds across methods, and verify scoring granularity compatibility.

## Narrative Arc
1. Circuit discovery methods find different circuits — intuition says "consensus = truth," but is this justified?
2. We test this intuition systematically with CSS (binary consensus) across K=3 methods on multiple tasks and models
3. CSS succeeds in only 1 of 5+ configurations (IOI on GPT-2) — consensus mostly fails
4. We identify three mechanistic failure modes with distinct signatures
5. Negative results + failure mode taxonomy = actionable practitioner guidelines

## Core Claims

### Claim 1: ACDC isinf binarization pathology (METHODOLOGICAL — strongest)
- **Evidence**: CSS=1.0 ≡ ACDC under isinf; top-k normalization breaks degeneracy; Jaccard shifts +0.16 to +0.25 across tasks
- **Status**: Fully demonstrated on IOI + Arithmetic + SVA (3 tasks)
- **Strength**: ★★★★★ — concrete, reproducible, actionable

### Claim 2: CSS fails on majority of task×model configurations (EMPIRICAL)
- **Evidence**: 1/5+ configurations show CSS=1.0 CPR advantage; failures include task-dependent (Arithmetic, SVA) and model-scaling (Qwen×2)
- **Status**: IOI PASS, Arithmetic FAIL, SVA inconclusive (D033), Qwen IFR FAIL, Qwen ACDC FAIL, Factual Recall pending
- **Strength**: ★★★★ — honest negative finding with systematic coverage

### Claim 3: Component-level scoring causes scaling failure (MECHANISTIC)
- **Evidence**: On Qwen-0.5B (179K edges), both IFR and ACDC degenerate to node-level scoring; top-0.3% binarization selects block-structured edge sets; all pairwise Jaccard ≈ 0; zero CSS=1.0 edges
- **Status**: Demonstrated with two independent methods (IFR D028, ACDC D034)
- **Strength**: ★★★★ — root cause identified, not fixable by method substitution

### Claim 4: Jaccard as necessary-condition diagnostic (PRACTICAL)
- **Evidence**: max Jaccard > 0.5 → CSS never helps (3/3 cases); max Jaccard < 0.35 → CSS helps (1/1 case, IOI); gap zone 0.35-0.50 inconclusive
- **Status**: Directionally supported but n too small for statistical significance. Framed as "motivated conjecture + practical heuristic," NOT as proven correlation
- **Strength**: ★★★ — honest about limitations, still useful as guideline

### Claim 5: CIRCUS (within-method threshold diversity) fails completely (COMPARATIVE)
- **Evidence**: CIRCUS produces negative CPR on all tested tasks; cross-method consensus is necessary but not sufficient
- **Status**: D021 documented 3× failure
- **Strength**: ★★★ — negative ablation, depends on implementation correctness caveat

## Anticipated Reviewer Concerns

### R1: "This is just a negative result, what's the contribution?"
- **Response**: Three concrete contributions: (a) binarization pathology + fix, (b) scaling failure root cause (component-level scoring), (c) diagnostic guidelines. Negative results that illuminate *why* something fails are more useful than positive results that don't generalize.

### R2: "CSS is just the feature selection stability index (Nogueira & Brown 2016)"
- **Response**: Acknowledged explicitly in Related Work. Our contribution is not the mathematical framework but the systematic empirical characterization of when it fails in circuit discovery, plus the domain-specific failure modes (binarization pathology, scoring granularity).

### R3: "IOI positive result could be size effect"
- **Response**: Size-controlled baseline analysis (pending) directly addresses this. If confirmed as artifact, strengthens the negative finding narrative.

### R4: "Only GPT-2 Small + Qwen 0.5B, limited model coverage"
- **Response**: Two models at different scales (32K vs 179K edges) already reveal the scaling failure. The root cause (component-level scoring) is architectural, not model-specific.

### R5: "EAP-IG and EP are gradient-adjacent, K=3 is effectively K≈2"
- **Response**: This is part of our finding, not a limitation — even theoretically diverse methods (IFR, ACDC) fail to provide independent evidence at scale. Method correlation is structural, not accidental.

### R6: "No confidence intervals on CPR differences"
- **Response**: Must add bootstrap CIs. IOI advantage of +0.08 needs statistical validation.

## Competitors
- **CIRCUS** (Parekh 2026): Within-method threshold diversity; our negative ablation
- **Mondorf et al.** (2510.06811): Cross-method score averaging; must acknowledge continuous averaging may outperform binary consensus
- **PIE** (2604.16889): Iterative pruning ensemble; single paradigm
- **Nogueira & Brown** (JMLR 2016): Feature selection stability; CSS is domain application, must cite
- **Kuncheva & Whitaker** (2003): Ensemble diversity theory; theoretical foundation for our failure mode analysis
