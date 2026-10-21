---
dream_id: dream_20260525T223036
tier: best
overall_score: borderline (5-6/10)
timestamp: 2026-05-25T23:09:44.446279+00:00
---

# Dream Review Report: "Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion"

**Venue**: CoRL 2026 (acceptance rate ~36%, OpenReview 1-10 scale)
**Review mode**: Full (2 Reviewers + Roundtable)
**Dream ID**: 20260525T223036

---

## Step 1: Independent Reviews

### R1 Review: Methods & Experiments

**Summary**: The paper presents a large-scale empirical study (70+ experiments, 6000+ episodes) diagnosing systematic contamination of the CAR metric in VLA safety evaluation, proposes dfCAR as a corrective metric, and demonstrates SDF auxiliary training as both a diagnostic probe and partial solution via a two-phase strategy. The diagnostic contribution is strong and well-evidenced; the constructive contribution has meaningful statistical gaps.

**Strengths**:
- Diagnostic finding is compelling and well-quantified across 3 model families, 2 scenes, and 6000+ episodes
- LoRA attribution experiment (Table 4) is a clean ablation: LoRA-only CAR ≈ zero-shot baseline (27% vs 26.8%), confirming the full +25pp is from SDF
- 4-point λ curve (Table 6) provides dose-response evidence with clear diminishing returns pattern
- Two-phase result (TSR=48%, CAR=45%) occupies a previously unachievable region of the TSR-CAR plane
- Cross-scene validation (object_pudding + spatial_bowl) shows consistent SDF effect (+25-32pp CAR)
- Per-task analysis reveals non-obvious EE-only limitation (bbq_sauce -24pp), adding depth

**Weaknesses**:
- **Phase 2 single seed**: The paper's most important constructive result (TSR=48%, CAR=45%) rests on 1 seed. At minimum 2 additional seeds are needed to establish reliability
- **OpenVLA asymmetry**: Zero-shot evaluation confounds "fake safety is architecture-general" with "OOD models freeze." A frozen OOD model trivially has low displacement — this doesn't prove CAR contamination is architecture-general in the same way as Pi0's SDF-induced collapse. The paper should either fine-tune OpenVLA or explicitly scope the claim
- **EE-only paradox unresolved**: The paper establishes EE-only SDF has structural limitations (bbq_sauce -24pp, arm-body collisions) then uses EE-only SDF successfully for the two-phase strategy, without reconciling when/why it works vs. fails
- **dfCAR threshold justification is thin**: δ=0.1m is chosen as "minimum displacement needed to complete any SafeLIBERO task" but no sensitivity analysis is presented. What happens at δ=0.05m or δ=0.2m?
- **No evaluation of published safety methods**: Applying dfCAR to existing methods (AEGIS, SafeVLA) would transform the finding from self-diagnosis to field-wide impact
- **spatial_bowl single seed**: Cross-scene generalization claim rests on 1 seed for the second scene

**Questions for Authors**:
1. What is the variance of the Phase 2 result across different Phase 1 checkpoints or seeds?
2. Does the 0.1m threshold produce qualitatively different conclusions than 0.05m or 0.2m?
3. How does AEGIS (which reports high CAR with non-trivial TSR) fare under dfCAR?

**Scoring (R1)**:
- Quality: 6/10
- Clarity: 7/10
- Significance: 6/10
- Relevance: 8/10
- Overall: 6/10
- Confidence: 4/5

---

### R2 Review: Novelty & Related Work

**Summary**: The paper quantifies a systematic bias in CAR (fake safety from action collapse and geometric path safety) across three VLA families, proposes a displacement-filtered metric, and demonstrates SDF auxiliary training as a partial solution. The diagnostic finding is useful but conceptually straightforward once stated; the methodological contributions are incremental combinations of known techniques; and the paper is severely under-cited (5 references).

**Strengths**:
- Compelling empirical observation with immediate practical consequences for VLA safety evaluation
- Thorough experimental methodology for diagnostic claims (multiple independent validation signals)
- Two-phase training result is genuinely interesting — 81% safety retention after removing auxiliary loss is non-trivial
- Cross-architecture validation with OpenVLA adds breadth
- Per-task collision transfer analysis reveals non-obvious geometric limitations

**Weaknesses**:
- **Limited novelty**: The "fake safety" observation is conceptually straightforward once stated — a metric that counts non-events is trivially satisfied by inaction. Action collapse is well-documented. The contribution is quantification on a specific benchmark, not discovery of a new phenomenon
- **dfCAR is a minimal methodological contribution**: Adding a displacement threshold is the obvious fix. No formal connection to measurement theory, construct validity, or threshold selection theory
- **SDF auxiliary loss is an incremental combination**: SDF-based collision costs are standard in motion planning (CHOMP, DiffCo, RAMP). Applying SDF as auxiliary VLA training loss via LoRA is a straightforward adaptation without new formulations
- **Two-phase strategy not positioned relative to curriculum learning**: Pre-training with auxiliary objective then removing it is well-known (scheduled auxiliary losses, progressive training). The paper does not cite or discuss this extensive prior work, making the contribution appear more novel than it is
- **Only 5 references**: Grossly insufficient for any top venue. Missing entire literatures:
  - Safe RL / constrained RL (CPO, Lagrangian CMDPs, safety critics)
  - Curriculum learning (Bengio et al. 2009, scheduled auxiliary losses)
  - SDF in robotics beyond CHOMP (DiffCo, C-space distance fields)
  - Metric gaming / Goodhart's Law in ML evaluation
  - Other manipulation benchmarks with safety metrics
  - Full-body collision detection in learning-based manipulation
- **Safety-performance tradeoff under-analyzed**: Even the best result (TSR 48%) is a 26pp degradation. No mechanistic analysis of *why* SDF loss degrades task performance so severely
- **Narrow scope**: Only SafeLIBERO (2 scenes from 1 benchmark). Claims about "VLA safety evaluation" are broader than the evidence

**Questions for Authors**:
1. Does the original SafeLIBERO/AEGIS paper already discuss or account for action collapse when reporting CAR?
2. What happens with Phase 1 durations other than 10K (e.g., 2K, 5K)? Is there a principled stopping criterion?
3. At λ=0.1, fake safe rate rises to 8% — is this SDF-induced action collapse? If so, there's a non-monotonic genuine-safety vs λ relationship that deserves analysis
4. SafeLIBERO has 32 scenarios. Why only 2? Selection bias?
5. Has oracle SDF refinement been tested on Pi0.5 (which actually moves) rather than only on collapsed Pi0?

**Scoring (R2)**:
- Originality: 5/10
- Clarity: 7/10
- Significance: 6/10
- Relevance: 8/10
- Overall: 5/10
- Confidence: 4/5

---

## Step 2: Cross-Sharing — Key Agreements and Divergences

### Agreements (both reviewers)
1. **Diagnostic contribution is the paper's primary strength** — the fake safety finding is well-evidenced and practically important
2. **Phase 2 single seed is a serious concern** — the most important constructive claim lacks statistical backing
3. **OpenVLA zero-shot is problematic** — confounds OOD failure with metric-general bias
4. **High relevance to CoRL** (both score 8/10) — VLA safety is timely, the problem directly affects evaluation practices
5. **Paper is well-written** (both score clarity 7/10) — logical narrative arc, clear experimental methodology
6. **EE-only limitation is acknowledged but unresolved** — the paper identifies the problem without fully reconciling it with the SDF success claims

### Divergences
1. **Novelty assessment**: R1 is more neutral (doesn't heavily penalize novelty); R2 argues the observation is "conceptually straightforward once stated" and penalizes more strongly (Originality 5/10)
2. **dfCAR as contribution**: R1 considers it well-motivated; R2 considers it a minimal/obvious fix
3. **Related work severity**: R1 doesn't heavily flag the 5-reference issue; R2 considers it a critical failure (missing safe RL, curriculum learning, SDF in robotics, metric gaming literatures)
4. **Overall score**: R1 gives 6/10 (borderline accept); R2 gives 5/10 (marginally below)

---

## Step 3: Convergence — Reconciliation

After cross-examining both positions:

1. **On novelty**: R2's critique is well-founded. The core insight (inaction-based metrics are trivially satisfied) is indeed conceptually simple. However, R1 correctly notes that the *quantification* across 3 model families with 6000+ episodes transforms a theoretical concern into actionable evidence. **Consensus**: The novelty is moderate — "known issue, now rigorously quantified" rather than "new discovery." This is legitimate but below the bar for a strong accept at a 36% acceptance rate venue.

2. **On related work**: R2's concern is decisive. Five references for a CoRL submission is untenable. The missing connections to safe RL, curriculum learning, and SDF motion planning literature are not cosmetic — they affect how readers assess the contribution's positioning and novelty. **Consensus**: This is a major weakness that must be addressed.

3. **On Phase 2 single seed**: Both reviewers agree. This is the paper's most important constructive claim and it cannot rest on n=1. **Consensus**: Critical weakness.

4. **On OpenVLA**: Both reviewers flag this. A zero-shot OOD model freezing is expected behavior, not evidence of a metric-general bias. **Consensus**: The claim should be scoped as "fake safety occurs across models" (empirically true) rather than "CAR is systematically contaminated across architectures" (which requires same-distribution evaluation).

5. **On overall score**: Averaging R1 (6) and R2 (5) gives 5.5. Given the severity of the related work gap and the single-seed Phase 2, we converge at **5.5/10 → rounded to 6/10 (marginally above threshold)**, contingent on the diagnostic contribution's practical value outweighing the novelty and completeness concerns.

---

## Step 4: Consolidated Assessment

### Final Scores (CoRL 1-10 scale)

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Originality | — | 5 | **5** |
| Quality | 6 | — | **6** |
| Clarity | 7 | 7 | **7** |
| Significance | 6 | 6 | **6** |
| Relevance | 8 | 8 | **8** |
| **Overall** | **6** | **5** | **5-6** |
| Confidence | 4/5 | 4/5 | **4/5** |

### Overall Recommendation: **Borderline (5-6/10)**

The paper would be a weak/borderline submission at CoRL 2026 in its current form.

### What Works
- The fake safety finding is **important and well-quantified**. If the VLA safety community adopts dfCAR, evaluation practices will meaningfully improve. The 98-99.6% fake safety rate across 3 model families is a striking and actionable finding.
- The experimental scale (70+ experiments, 6000+ episodes) is thorough for the diagnostic claims.
- The two-phase training result is the most novel element and could anchor a stronger paper if replicated.

### What Needs Work (ranked by priority)

**Critical (must fix)**:
1. **Related work**: Expand from 5 to 25+ references. Must cover: safe RL/constrained RL, curriculum learning/progressive training, SDF in motion planning (beyond CHOMP), metric gaming/Goodhart's Law in ML, other VLA safety methods, full-body collision detection
2. **Phase 2 multi-seed**: Replicate across ≥3 seeds. The TSR=48%/CAR=45% claim is load-bearing for the "partial solution" framing
3. **OpenVLA scoping**: Either fine-tune OpenVLA (preferred) or explicitly scope the claim to "fake safety is observed across architectures" without implying it's the same phenomenon

**Major (strongly recommended)**:
4. **dfCAR threshold sensitivity**: Show results at δ ∈ {0.05, 0.1, 0.15, 0.2}m to demonstrate robustness
5. **Apply dfCAR to published methods**: Evaluate AEGIS or SafeVLA under dfCAR — this would dramatically increase impact
6. **spatial_bowl multi-seed**: At least 2 seeds for cross-scene claim
7. **Two-phase mechanism analysis**: Why does safety "stick" after removing SDF loss? Probing LoRA weight structure (e.g., weight similarity, gradient alignment) would strengthen the contribution

**Minor**:
8. **Novelty framing**: Position honestly as "rigorous quantification of a suspected problem + preliminary solution direction" rather than implying the observation itself is novel
9. **Curriculum learning connection**: Explicitly discuss relationship to scheduled auxiliary losses and progressive training
10. **λ=0.1 analysis**: The rising fake safe rate at high λ suggests SDF-induced conservatism approaching collapse — worth analyzing

### Acceptance Probability Estimate
- **Current form**: 25-35% (below average acceptance probability at a 36% venue)
- **With critical fixes (1-3)**: 45-55%
- **With critical + major fixes (1-7)**: 60-70%

### Key Insight for Authors
The paper's core tension is that the **diagnostic contribution is strong but not novel enough to carry the paper alone**, while the **constructive contribution (SDF + two-phase) is novel enough but not statistically mature**. The path to acceptance requires either (a) strengthening the diagnostic impact by applying dfCAR to published methods (transforming it from self-diagnosis to field audit), or (b) maturing the constructive contribution with multi-seed replication and mechanistic analysis, or ideally both.

---

## Experiment Coverage Assessment

Comparing paper content against `review_context.yaml` planned experiments:

| Experiment | In Paper? | Quality |
|-----------|-----------|---------|
| A1 EE Displacement Re-eval (50ep) | ✅ Table 1 | Good — cross-validates with 800ep obstacle disp |
| OpenVLA Zero-shot (200ep) | ✅ Tables 2-3 | Adequate but zero-shot limits generalization claim |
| LoRA Baseline (2 seeds) | ✅ Table 4 | Good — clean attribution control |
| Phase 2 λ=0 Training | ✅ Table 7 | Training described, loss trajectory discussed |
| Phase 2 λ=0 Eval (200ep) | ✅ Tables 7-8 | **Single seed — critical gap** |
| spatial_bowl A1 Eval (200ep) | ✅ Tables 9-10 | **Single seed — weakness** |
| Lambda=0.1 Training + Eval | ✅ Table 6 | Adequate — completes 4-point curve |

All planned experiments are covered in the paper. The coverage is complete but the seed counts for Phase 2 and spatial_bowl are insufficient for the claims made.

---

## 引用验证结果

**统计**: 40 篇文献 / 29 处引用 / 在线验证 40/40 篇

### 问题 (24)

- ⚠️ `liu2023libero` — 元数据不匹配: first_author: bib=liu vs api=feng
- ❌ `karwowski2024goodhart` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.29 below threshold 0.82
- ⚠️ `geoaware2025` — 元数据不匹配: first_author: bib=abouzeid vs api=ali
- ❌ `stemvla2026` — 在线验证未找到匹配（疑似虚假引用）: no results from any source
- ❌ `evo02025` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.31 below threshold 0.82
- ⚠️ `vasilopoulos2023ramp` — 在 .bib 中但正文未引用
- ⚠️ `chen2026cssdfnet` — 在 .bib 中但正文未引用
- ⚠️ `jacquet2025neuralnmpc` — 在 .bib 中但正文未引用
- ⚠️ `chen2025samp` — 在 .bib 中但正文未引用
- ⚠️ `ruan2025profrobot` — 在 .bib 中但正文未引用
- ⚠️ `depthvla2025` — 在 .bib 中但正文未引用
- ⚠️ `li2025qdepth` — 在 .bib 中但正文未引用
- ⚠️ `li2025spatialforcing` — 在 .bib 中但正文未引用
- ⚠️ `3dcavla2025` — 在 .bib 中但正文未引用
- ⚠️ `geoaware2025` — 在 .bib 中但正文未引用
- ⚠️ `spatialvla2025` — 在 .bib 中但正文未引用
- ⚠️ `gstvla2026` — 在 .bib 中但正文未引用
- ⚠️ `stemvla2026` — 在 .bib 中但正文未引用
- ⚠️ `stvla2026` — 在 .bib 中但正文未引用
- ⚠️ `evo02025` — 在 .bib 中但正文未引用
- ⚠️ `savla2026` — 在 .bib 中但正文未引用
- ⚠️ `augvla3d2026` — 在 .bib 中但正文未引用
- ⚠️ `evodepth2026` — 在 .bib 中但正文未引用
- ⚠️ `chen2026dfmvla` — 在 .bib 中但正文未引用

### ✅ 通过 (35)