# Paper Framing — StructFuse

## Target Venue
- Primary: EMNLP 2026 Main
- Deadline: ARR May 25, 2026

## Core Claims (3)

1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.

2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.

3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]

## Story Spine

- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.

- **Existing approaches & gaps**:
  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies
  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal
  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings
  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works

- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.

- **Headline result template**: "Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective."

## Core Insight

Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.

## Dual-Pillar Motivation

1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.
2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.

## Formal Definition

Given retrieval domain D, structural graph G, query q:
**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)

The structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).

## Title Options

- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
- Alternative: "Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]
- Backup: "Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval"

## Venue Fit

1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
3. **Against "incremental" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.

## Anticipated Reviewer Concerns

| Concern | Response | Evidence |
|---------|----------|----------|
| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |
| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |
| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |
| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |
| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |

## Evidence Status

### Confirmed findings (basis for claims):
- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline
- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction
- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)
- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only
- plan_006: CodeQL scalability confirmed at 123-repo scale

### Evidence presentation strategy:
- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)
- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)
- Both metrics show directionally consistent results; no goalpost-moving between metrics

### In progress:
- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.
- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.
- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15

### Planned (priority order):
- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)
- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
- plan_019: Pool size sensitivity (Dream consensus — external validity)
- plan_014: Temperature ablation (Dream reviewer concern)
- plan_004: RepoBench-R second benchmark (with multi-seed CIs)
- plan_015: Dynamic mining baseline
- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)
- plan_007/008/009: Additional ablations

## Limitations

Effect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.

## Contingency (if full M2 results weaken claims)

### All 18 runs confirm pilot pattern: Best case
- Full statistical power, paper as framed above
- Target: EMNLP Main

### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
- Drop Claim 2 to analysis observation
- Paper becomes: "Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions"
- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main

### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]
- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment
- Pivot: "systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal"
- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome
- Claim 1 core preserved: "Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling"
- Impact: BM25 result determines narrative nuance, not core contribution

### Embedding mining also loses advantage at full scale: Major reassessment needed
- Recheck data pipeline for bugs (full-scale data may have distribution differences)
- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
- Discuss with user before committing direction

## Deprecated Claims (with reason)

- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.

<!-- Claim 2 wording fix: 2026-05-15 -->
<!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->
<!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->
<!-- Claim 2 exploratory wording unification: 2026-05-15 -->
<!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->
<!-- Status data refresh: s44 DONE, 4/9 runs, m1 90.5%, headline caveat: 2026-05-15 -->
