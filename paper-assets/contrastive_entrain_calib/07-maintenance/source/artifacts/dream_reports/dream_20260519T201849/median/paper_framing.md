# Paper Framing — contrastive_entrain_calib

## Target Venue
- Primary: **EMNLP 2026** via ARR May 2026 cycle
- ARR Submission Deadline: **May 25, 2026** (6 days from May 19)
- Commitment Deadline: **August 2, 2026**
- ⚠️ May cycle 新政策：提交时必须声明目标会议为 EMNLP，绑定不可更改
- Fallback: ARR August 2026 cycle (DDL ~Aug 15) → EACL 2027 / ACL 2027
- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)

## Core Claims (3 条, 可证伪)

1. **Directional discriminability + training stability**: The policy model's activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision (AUROC 0.82), with signal emerging at mid-layers (L16-19). During GRPO training, d_syc remains stable (cosine ≈ 0.96 at step 500), and linear separability is preserved (AUROC 0.80 at step 500). Periodic recalibration (every 500 steps) is included as a safety mechanism.
   - *Evidence needed*: AUROC on style-controlled data, layer progression, direction stability curve, AUROC at each checkpoint
   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence
   - *New finding (D025 corrects D024)*: Initial stability measurement reported cosine=0.28 (74° drift) but this was a measurement artifact from referencing a stale directions.pt file (different dataset). Actual drift: cosine ≈ 0.96. Direction is stable during training.
   - *New finding (D019)*: Per-layer cosine AUROC ≥ 0.77 at step 500, deep layers L32/33 improved +0.025/+0.033. Full training curve (exp-006) pending.
   - *New finding (D025→D029)*: **Cosine R1 structural failure** — cosine(h, d_syc) gap between valid/invalid is ~0.098 (7-layer mean), far too small for GRPO reward. Four experiments confirmed this is structural, not tunable: exp-002 (tanh gate), exp-002v2 (raw cosine), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence samples get R1=-0.305 i.e. ALL negative). d_syc conflates legitimate revision with sycophantic capitulation at the continuous projection level. Binarization via probe resolves this (exp-008v3 R1 mean +0.72).

2. **DC-GRPO effectiveness via binarized direction reward (D029 pivot)**: Direction information (d_syc) is effective as GRPO reward ONLY when binarized through a probe classifier. Continuous cosine projection fails structurally — the paper presents a complete discovery→failure→understanding→solution arc.
   - *Evidence needed*: SYCONScore (harmonic mean of ToF + NoF) on D027 unified eval, compared to R3-only (exp-003) and ACT baselines (exp-004)
   - *Pass criterion*: exp-008v3 SYCONScore > 0.301 (ACT bar from exp-004 ckpt-8000)
   - *Narrative arc (D029)*:
     - **Discovery**: d_syc linearly separates sycophancy (AUROC 0.82, Claim 1) — direction information EXISTS
     - **Failure**: 4 cosine R1 attempts all fail — exp-002 (tanh gate), exp-002v2 (raw cosine, R1≈0), exp002v2-recalib (mode collapse, entropy 0.069), exp-002v3 (5x scale, strong evidence R1=-0.305 all negative)
     - **Understanding**: Per-strength analysis reveals structural cause — d_syc conflates legitimate revision with sycophantic capitulation at the continuous projection level. High-evidence samples (where model SHOULD revise) project most negatively onto d_syc
     - **Solution**: Binary probe resolves ambiguity — binarization via logistic regression on d_syc features maps continuous geometry to {sycophantic, genuine} decision. exp-008v3 R1 mean +0.72 (step 2140), consistently positive, upward trend
   - *Key insight*: Direction information exists (AUROC 0.82) but requires binarization to become effective GRPO reward. The gap between discriminability and reward utility is the paper's core finding.
   - *Fallback (D029)*: If exp-008v3 SYCONScore ≤ 0.301, paper downgrades to "direction signal characterization" (analysis paper targeting Findings, score 3.0-3.5)

3. **Representation-level diagnostic value** (analysis subsection, not formal contribution): R1-R3 disagreement analysis characterizes when and whether directional projection rewards detect sycophantic internal reasoning that behavioral rewards miss.
   - *Evidence needed*: R1-R3 disagreement frequency analysis, qualitative examples if > 5%
   - *Framing*: Empirical characterization of representation-level signal utility, reported honestly regardless of effect size. Not listed as a top-level contribution bullet.

## Story Spine

**Problem**: LLMs face a "double-bind" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes "the user is right, I should revise" from "the user is pressuring me, I should resist."

**Existing approaches & gaps**: Behavioral GRPO decomposition ("Pressure, What Pressure?") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.

**Our framing**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. Latent-GRPO (Zhang et al., 2026) uses spherical projection + robust centroids for reasoning correctness, but does not target behavioral attributes like sycophancy. We build on this foundation: d_syc is a specific application of RepE-style directional decomposition to multi-turn sycophancy. Our key finding is that d_syc successfully discriminates sycophancy (AUROC 0.82), but continuous geometric projections (cosine similarity) fail as GRPO rewards — the signal conflates legitimate revision with sycophantic capitulation. Binarization through a probe classifier trained on d_syc features resolves this: R1 = probe(h; d_syc) ∈ {0,1}, providing a clean, high-signal reward. The novelty is not the direction extraction itself, but the systematic investigation of HOW directional information should enter GRPO training — revealing that discriminability ≠ reward utility, and that binarization is necessary. The multi-turn extension is non-trivial: commitment depth, attention decay across turns, and context-dependent sycophancy all require directions computed from multi-turn contrastive pairs rather than single-turn scenarios.

**Method (D029 pivot)**: R1 = probe(h; d_syc) ∈ {0,1}, where probe is a logistic regression classifier trained on hidden-state projections onto d_syc. Binary output provides clean reward signal (exp-008v3 R1 mean +0.72). Combined reward: R = w1·R1 + w3·R3 (R2 disabled). Cosine R1 = cos(h, d_syc) was tested extensively and fails structurally (see "Cosine R1 failure chain" below) — this negative result is a key finding, not a footnote. No adaptive gating, no per-sample weighting. Gate was tested and found unnecessary (Appendix-level note only).

**Online recalibration**: d_syc is recalibrated every 500 training steps as a safety mechanism. Empirically, direction drift is modest (cosine ≈ 0.96 at step 500), but recalibration ensures the reward signal tracks any longer-term geometry changes. Cost is negligible (one forward pass over calibration data per 500 steps).

**Cosine R1 failure chain (D029 — key negative result)**: Continuous cosine R1 fails structurally, not due to scaling. Evidence chain:
1. **exp-002** (tanh gate): gate collapsed, R1 contribution zero → removed gate (D021)
2. **exp-002v2** (raw cosine, weight=0.25): R1 ≈ 0 throughout training, functionally equivalent to R3-only
3. **exp002v2-recalib** (raw cosine + recalibration): mode collapse (entropy 0.069, mean_length 62 tokens) — not clean evidence
4. **exp-002v3** (5x scaled cosine, weight=0.4): Per-strength analysis reveals structural cause — strong evidence samples (where model SHOULD revise) get R1=-0.305 (ALL negative). d_syc projection cannot distinguish "model correctly revises belief" from "model sycophantically capitulates" because both involve moving TOWARD the user's position in activation space. Scaling amplifies this flaw rather than fixing it.

**Root cause**: Cosine similarity measures angular alignment with d_syc direction. But sycophantic capitulation and genuine revision BOTH involve belief change toward the user's claim — they differ in WHETHER the change is warranted, not in the DIRECTION of the change. A linear direction captures the direction of change, not its warrant. Binarization via probe adds a decision boundary that the continuous projection lacks.

**Binarization insight**: Binary probe trained on d_syc features resolves the conflation by learning a nonlinear decision boundary between warranted and unwarranted belief change. exp-008v3 R1 mean +0.72 at step 2140 (consistently positive, upward trend) vs exp-002v2 R1 ≈ 0. The probe doesn't just threshold — it learns which combinations of layer projections indicate sycophancy vs genuine revision.

**Headline result template**: "On SYCON Bench, DC-GRPO with binarized direction reward (probe R1) achieves SYCONScore X (vs R3-only Y and ACT Z), demonstrating that representation-level direction information requires binarization to serve as effective GRPO reward — continuous cosine projection fails despite the same direction achieving AUROC 0.82 in discrimination."

## Venue Fit Risks

- **EMNLP fit**: Strong. Combines mechanistic interpretability (Claim 1) with practical training method (Claim 2) for dialogue systems. EMNLP values empirically rigorous NLP work with clear practical impact. The sycophancy-revision double-bind is directly relevant to EMNLP's alignment and safety track.
- **Reviewer concern 1 (novelty)**: "This is just RepE/CRAFT applied to sycophancy." Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is the systematic investigation of how direction information should enter GRPO rewards — discovering that discriminability ≠ reward utility; (b) the cosine R1 failure chain (4 experiments) and binarization insight are the core contribution, not direction extraction; (c) multi-turn calibration with evidence-strength stratification is a standalone contribution; (d) neither CRAFT nor RepE has investigated the discriminability–reward gap.
- **Reviewer concern 6 (RC-AUC custom metric)**: "Strongest results on self-invented metric." Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.
- **Reviewer concern 2 (signal strength)**: "AUROC ~0.82 on style-controlled data is moderate." Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) D019 confirms AUROC ≥ 0.77 persists across ALL 7 layers even after 500+ LoRA training steps, with deep layers actually improving (+0.025-0.033); (e) direction remains stable during training (cosine sim ≥ 0.82 with initial direction).
- **Reviewer concern 3 (scale)**: "Only Qwen3-8B." Counter: Budget constraint (200 H100-hr). If time/budget allows, add one more model family (e.g., Llama-3-8B). Cross-model direction transfer analysis partially addresses this.
- **Reviewer concern 4 (R2 degeneration)**: "d_gen = -d_syc in binary design." Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.
- **Reviewer concern 5 (practical utility)**: "Do models actually exhibit masked sycophancy at meaningful rates?" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.

## Anticipated Reviewer Concerns & Experimental Responses

| Concern | Experiment | Priority |
|---------|-----------|----------|
| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |
| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |
| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |
| Probe doesn't need d_syc (random features work) | Random-direction probe ablation: probe trained on random directions vs d_syc features | P1 |
| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |
| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |
| Single model, doesn't generalize | Cross-model direction transfer analysis (if budget allows) | P2 |
| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |
| Why not continuous probe output (probability) instead of binary? | Continuous probe probability vs binary probe reward comparison | P1 |
| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |
| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |
| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |
| Cosine R1 failure is just bad tuning, not structural | 4-experiment failure chain + per-strength analysis showing structural conflation | P0 (evidence complete) |
| Direction drifts during training | exp-006 stability curve: cosine sim + AUROC at 5 checkpoints | P0 |
| Why cosine not dot product? | Appendix: dot product saturation analysis + R1 distribution comparison | P2 (less critical post-D029, cosine R1 is negative evidence not method) |
