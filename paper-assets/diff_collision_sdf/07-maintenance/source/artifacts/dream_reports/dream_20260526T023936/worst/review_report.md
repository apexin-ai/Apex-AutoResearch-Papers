---
dream_id: dream_20260526T023936
tier: worst
overall_score: 5/10 Marginal Reject
timestamp: 2026-05-26T03:42:03.366291+00:00
---


# Dream Review Report: Rethinking VLA Safety Evaluation

**Dream ID:** 20260526T023936
**Venue:** CoRL 2026 (rating scale 1-10, acceptance rate ~40%)
**Review Mode:** Full (2 Reviewers + Roundtable)

---

## Reviewer Assignments
- **R1:** Methods and Experiments (Soundness, Statistical Rigor, Experimental Coverage)
- **R2:** Novelty and Related Work (Originality, Positioning, Contribution Scope)

---

## R1 Review: Methods and Experiments

### Summary
The paper diagnoses systematic contamination of CAR by action collapse ("fake safety"), proposes dfCAR, and conducts ablations decomposing collision avoidance into implicit demonstration signals vs. explicit SDF geometric supervision across 6000+ episodes. The central experimental finding is that LoRA fine-tuning alone accounts for the dominant avoidance signal (+29pp CAR), with SDF adding nothing at low lambda but +15.5pp at lambda=0.1 (p<0.02). A two-phase curriculum partially resolves the safety-capability tradeoff (CAR=66%, TSR=40%).

### Strengths
- **Well-designed fake safety diagnosis.** The 800-episode A1 evaluation with per-episode displacement analysis provides compelling evidence. The dual evidence chain (99.4% obstacle displacement <0.1mm AND TSR=0%) is methodologically sound. The bimodal displacement gap spanning 3+ orders of magnitude makes the finding robust.
- **dfCAR threshold robustness is thorough.** Invariance across δ∈[2mm, 100mm] cleanly separates fake from real safety and eliminates the threshold sensitivity objection.
- **3v3 seed design for SDF attribution (Table 4) is the correct structure.** Matched seed counts with separate SEs and per-lambda p-values follows good practice.
- **Honest reporting of negative results.** The paper does not hide inconvenient findings (cross-scene inconsistency, OpenVLA blocking, high LoRA variance).
- **Large cumulative experimental effort.** 6000+ episodes, multiple lambda values, cross-scene validation, two-phase ablation.

### Weaknesses
- **3v3 comparison is critically underpowered for a null-result claim (Table 4).** With n=3 seeds, effective df for Welch t-test is ~2-4. LoRA SD=6.5pp (SE=3.7pp) → 95% CI on LoRA-SDF difference at λ=0.005 spans roughly [-8pp, +10pp]. Cannot distinguish "SDF adds 0pp" from "SDF adds 5pp." No formal equivalence test (TOST) with pre-specified margin. Treating absence-of-significance as evidence-of-absence is a classic statistical error.
- **Lambda=0.1 result (+15.5pp, p<0.02) based on only 2 seeds.** With 2-3 effective df, p<0.02 has fragile coverage. A single additional seed could push p above 0.05. The 10x jump from λ=0.01 to λ=0.1 with no intermediate values (0.03, 0.05, 0.07) leaves the dose-response curve severely under-sampled.
- **Two-phase training uses only 2 seeds.** CAR=66% (SE~2pp), TSR=40% (SE~2pp). 95% CI on TSR spans ~[36%, 44%]. Only one Phase 1 duration (10K) and one lambda (0.005) tested — no ablation over Phase 1 hyperparameters.
- **Cross-scene results (Table 7) are inconsistent and single-seeded.** SDF effect: +0.8pp (ns) on object_pudding vs. +9pp (marginal) on spatial_bowl. With n=1 per condition for spatial_bowl, cannot distinguish genuine scene effects from seed noise.
- **dfCAR introduces potential selection bias.** Excluding low-displacement episodes conditions on a post-treatment variable. If SDF training changes the displacement distribution, dfCAR could create or mask treatment effects. Not discussed.
- **EE-only SDF circularity.** The paper demonstrates EE-only SDF is structurally deficient, then tests SDF redundancy using only EE-only SDF. Cannot distinguish "geometric supervision is fundamentally redundant" from "this particular formulation is too limited to help at low doses."
- **OpenVLA blocked.** Only projected values reported. Weakens generalization claim to 2 model families from the same Pi0 lineage.
- **Statistical methodology unreported.** No specification of which test was used, degrees of freedom, or confidence intervals — only p-values.

### Questions for Authors
1. What specific test produced the p-values in Tables 4-5? Report test statistic, df, and 95% CIs. Have you considered TOST equivalence testing?
2. Have you tested intermediate lambda values (0.03, 0.05, 0.07)? Is the jump at λ=0.1 a smooth transition or phase change?
3. How do you reconcile "SDF adds nothing at low lambda" with "SDF adds 15.5pp at high lambda" — is SDF redundant or under-dosed?
4. The TSR collapse (73%→5%) is identical across LoRA-only and all SDF variants. Is this catastrophic forgetting from fine-tuning on filtered demos? Have you tried standard mitigations (EWC, replay, lower LR)?
5. Does dfCAR filtering change the proportion of episodes differently across conditions?

### Missing Experiments
- Intermediate lambda values (0.03, 0.05, 0.07) to characterize dose-response
- Third seed for lambda=0.1 and Phase 2 conditions
- spatial_bowl LoRA-only control (plan_015)
- OpenVLA evaluation (even zero-shot)
- Phase 2 ablation over Phase 1 duration and lambda
- Real robot validation or discussion of dfCAR in noisy settings
- Application of dfCAR to published safety methods (AEGIS, SafeVLA)

### R1 Scores
- Soundness: 2/4
- Significance: 2/4
- Clarity: 3/4
- Overall: **4/10**
- Confidence: 4/5

---

## R2 Review: Novelty and Related Work

### Summary
The paper identifies CAR contamination by action collapse, proposes dfCAR as a corrective, and demonstrates through ablation that collision avoidance arises primarily from implicit demonstration signals rather than explicit SDF supervision. The novelty rests on the empirical documentation of metric contamination and the decomposition of avoidance sources, rather than on methodological innovation.

### Strengths
- **Fake safety observation is well-documented and impactful.** The 91.5% CAR / 0% TSR / 99.4% frozen finding is striking. Even if action collapse is conceptually unsurprising, demonstrating its magnitude of metric contamination is a genuine contribution.
- **dfCAR threshold robustness is convincing.** The bimodal gap rendering dfCAR invariant across [2, 100]mm eliminates the threshold sensitivity objection. Simple, principled, and immediately usable.
- **4-point lambda dose-response is well-designed.** The flat curve for λ≤0.01 with jump at λ=0.1 provides structured evidence of a threshold effect.
- **Honest limitation disclosure.** Appropriate for a diagnostic paper. The paper acknowledges scope restrictions and distinguishes discovery from validated method.
- **Per-task breakdown provides mechanistic insight** beyond aggregate numbers.

### Weaknesses
- **Action collapse is not novel; documenting its metric contamination is.** Action collapse / mode collapse is extensively documented in RL, generative modeling, and imitation learning. The contribution narrows to "CAR does not account for action collapse" — useful but closer to a benchmark/metrics paper than a conceptual advance. Title "Rethinking VLA Safety Evaluation" overstates this.
- **Bibliography is critically deficient with fabricated entries.** Multiple placeholder references with "{Authors}" as author field. The project's own literature map identifies 25+ real papers not cited. At CoRL, fabricated bibliography entries risk desk rejection.
- **dfCAR is conceptually simple** — displacement thresholding + CAR. The bimodal gap that makes it robust is a property of this specific benchmark/model, not guaranteed for all VLA evaluations. Paper does not discuss partial-collapse scenarios.
- **SDF redundancy has limited generalization scope.** EE-only SDF on Pi0.5 with LoRA on SafeLIBERO. The paper's own analysis identifies the structural limitation. Framing "implicit demonstration signals, not explicit geometric supervision" as a general conclusion overgeneralizes from EE-only SDF to all geometric supervision.
- **"Decomposition framework" is overstated.** This is a two-condition ablation (LoRA vs. LoRA+SDF), not a framework. A genuine decomposition would systematically disentangle data distribution, model capacity, training procedure, and geometric signal.
- **Only 2 model families from the same Pi0 lineage.** The blocked OpenVLA experiment is a significant gap for a paper claiming to rethink VLA safety evaluation writ large.
- **TSR collapse (73%→6%) not adequately analyzed.** Does not distinguish learned conservatism (safety-relevant) from catastrophic forgetting (fine-tuning artifact).

### Missing Related Work
- Safe RL foundations: CPO (Achiam et al., ICML 2017), Lagrangian constrained MDPs
- Action/mode collapse: Diffusion Policy (Chi et al., RSS 2023), Dong et al. (2025) loss collapse
- Other geometric representations: C-space distance fields (Li et al., RSS 2024), full-body SDF
- VLA foundations: RT-2, OpenVLA, Octo, LIBERO (proper citations needed)
- Runtime safety: RAIL, TamedPUMA, APEX
- Spatial/3D-aware VLAs: Spatial Forcing (ICLR 2026), QDepth-VLA
- Metric validity: Goodhart's law literature, benchmark saturation

### R2 Scores
- Originality: 2/4
- Significance: 2/4
- Clarity: 3/4
- Overall: **5/10**
- Confidence: 4/5

---

## Roundtable Synthesis

### Step 2: Cross-Sharing Summary
Both reviewers independently identified the same core strengths (fake safety diagnosis, dfCAR robustness) and weaknesses (statistical underpowering, narrow scope, EE-only SDF circularity, incomplete experiments). The convergence is strong.

### Step 3: Agreements and Disagreements

**Consensus Points:**
1. Fake safety / dfCAR is the paper's strongest and most actionable contribution.
2. The SDF attribution claim is critically underpowered (n=3 seeds, no equivalence test, high LoRA variance SD=6.5pp).
3. The lambda=0.1 result (+15.5pp) contradicts the "SDF redundancy" headline — SDF works when dosed sufficiently, undermining the paper's framing.
4. Scope is too narrow for the claim generality: 2 model families (same lineage), 1 main scene, OpenVLA blocked, spatial_bowl single-seeded and inconsistent.
5. Two-phase results are promising but preliminary (2 seeds, no hyperparameter ablation).
6. Bibliography is critically deficient with fabricated/placeholder entries.
7. The paper is well-written and honestly self-critical about limitations.

**Divergence:**
- R1 (4/10) weighs statistical rigor failures more heavily; R2 (5/10) gives more credit for practical value of the fake safety observation.
- R1 uniquely raises dfCAR selection bias (conditioning on post-treatment variable); R2 uniquely raises partial-collapse generality concern.
- Both concerns are valid and complementary rather than conflicting.

### Step 4: Consolidated Assessment

**Overall Score: 4.5/10 → 5/10 (Marginal Reject)**

**Justification:**

The paper identifies a genuine and practically important problem — standard CAR is systematically inflated by action collapse in low-capability VLA models. The proposed dfCAR metric is simple, principled, and remarkably robust to threshold choice. These contributions alone have value for the VLA safety evaluation community.

However, the paper suffers from several issues that place it below the CoRL acceptance threshold (~40% acceptance):

1. **Statistical rigor is insufficient for the central claims.** The SDF attribution analysis (the paper's most ambitious claim) uses n=3 seeds with high variance (SD=6.5pp), no equivalence testing, unreported test methodology, and no confidence intervals. The lambda=0.1 result uses only 2 seeds. These sample sizes cannot support the conclusions drawn.

2. **The SDF redundancy framing is internally contradicted.** The paper's own lambda=0.1 result shows SDF provides +15.5pp CAR when sufficiently weighted. This means SDF is not redundant — it is under-dosed at low lambda. The paper attempts to reconcile this but the framing remains confused between "SDF is redundant" and "SDF has a dose-dependent effect."

3. **Scope is too narrow for the claim generality.** "Rethinking VLA Safety Evaluation" requires evidence beyond 1 benchmark, 2 scenes, and 2 model families from the same architectural lineage. The OpenVLA gap is particularly damaging.

4. **Bibliography is critically incomplete.** Placeholder/fabricated citations would risk desk rejection at a top venue.

5. **The "decomposition framework" label overstates what is fundamentally a two-condition ablation** (LoRA vs. LoRA+SDF).

**What would raise the score to accept (6-7):**
- 5+ seeds for LoRA and SDF conditions with proper equivalence testing
- Intermediate lambda values (0.03, 0.05, 0.07) to characterize the dose-response
- At least one non-Pi0 model family (OpenVLA or RT-2)
- Complete bibliography with real citations
- Reframe from "SDF redundancy" to "dose-dependent decomposition" — which is the actual finding
- Scope claims to match evidence: "on SafeLIBERO with Pi0 family" not "VLA safety evaluation" broadly

**Experiment Coverage Assessment (vs. review_context.yaml):**
- plan_001 (A1 re-eval): ✅ Covered (Table 1)
- plan_002 (OpenVLA): ❌ BLOCKED — only projected values
- plan_003 (LoRA 2-seed eval): ✅ Covered (Table 3, s0/s1)
- plan_004 (LoRA training): ✅ Covered
- plan_005 (Phase 2 training): ✅ Covered
- plan_006 (Phase 2 eval): ✅ Covered (Table 6)
- plan_007 (spatial_bowl training): ✅ Covered
- plan_008 (spatial_bowl eval): ✅ Covered (Table 7)
- plan_009 (Lambda=0.1 training): ✅ Covered
- plan_010 (Lambda=0.1 eval): ✅ Covered (Table 5)
- plan_011 (A1 re-eval decision): ✅ Covered
- plan_012 (Phase 2 additional seed): ✅ Covered (Table 6, seed 0)
- plan_013 (LoRA seed2): ✅ Covered (Table 3, s2) — low CAR=44% drives variance
- plan_014 (dfCAR threshold sensitivity): ✅ Covered (Table 2)
- plan_015 (spatial_bowl LoRA control): ⚠️ Partially covered (Table 7 reports CAR=36% but only 1 seed)

**Key coverage gaps:** OpenVLA blocked, spatial_bowl underpowered, no intermediate lambda values, no Phase 2 hyperparameter ablation.

---

## Final Scores Summary

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness/Originality | 2/4 | 2/4 | 2/4 |
| Significance | 2/4 | 2/4 | 2/4 |
| Clarity | 3/4 | 3/4 | 3/4 |
| Overall | 4/10 | 5/10 | **5/10 (Marginal Reject)** |
| Confidence | 4/5 | 4/5 | 4/5 |

**Recommendation: Reject (with encouragement to resubmit after addressing statistical rigor, scope, and bibliography issues)**


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