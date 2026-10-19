# Paper Framing — StructFuse

## Target Venue
- Primary: EMNLP 2026 Main
- Deadline: ARR May 25, 2026

## Core Claims (3)

1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported "harm" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).

2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.

3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).

## Story Spine

- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.

- **Existing approaches & gaps**:
  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies
  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal
  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance
  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works

- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.

- **Headline result template**: "True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis."

## Core Insight

The effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.

## Dual-Pillar Motivation

1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.
2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.

## Formal Definition

Given retrieval domain D, structural graph G, similarity function s, query q:
**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)

The structural graph is externally fixed and does not update with the encoder (drift-immune).

## Title Options

- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
- Alternative: "StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval"
- Backup: "Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally"

## Venue Fit

1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
3. **Against "incremental" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.

## Anticipated Reviewer Concerns

| Concern | Response | Evidence |
|---------|----------|----------|
| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |
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
- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact
- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
- plan_006: CodeQL scalability confirmed at 123-repo scale

### In progress:
- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)
- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)
- m1_reextract_v2: expanded extraction for higher coverage

### Planned (priority order):
- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
- plan_014: Temperature ablation (Dream reviewer concern)
- plan_004: RepoBench-R second benchmark
- plan_015: Dynamic mining baseline
- plan_007/008/009: Additional ablations

## Contingency (if full M2 results weaken claims)

### All 18 runs confirm pilot pattern: Best case
- Full statistical power, paper as framed above
- Target: EMNLP Main

### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
- Drop Claim 2 to analysis observation
- Paper becomes: "True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main

### Embedding mining also loses advantage at full scale: Major reassessment needed
- Recheck data pipeline for bugs (full-scale data may have distribution differences)
- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
- Discuss with user before committing direction

## Deprecated Claims (with reason)

- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
