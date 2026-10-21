---
dream_id: dream_20260526T023936
tier: median
overall_score: reject
timestamp: 2026-05-26T03:32:59.705861+00:00
---

# Dream Review Report — "Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion"

**Dream ID:** 20260526T023936  
**Venue:** CoRL 2026  
**Review Mode:** Full (2 Reviewers + Roundtable)  
**Venue Calibration:** CoRL 2024 acceptance rate ~39%, 1–4 scoring scale. Review dimensions: Originality, Quality, Clarity, Significance, Relevance to robot learning.

---

## I. Reviewer R1 — Methods & Experiments

### Summary
The paper identifies systematic contamination in VLA collision avoidance evaluation: standard CAR conflates genuine obstacle avoidance with action collapse (frozen robots scored as collision-free). The authors propose dfCAR as a corrective metric, demonstrate that EE-only SDF refinement structurally fails even with ground-truth geometry, and show that LoRA fine-tuning on collision-free demonstrations produces genuine collision avoidance (+26pp CAR) while SDF auxiliary loss adds nothing at standard λ and marginal benefit at extreme λ.

### Strengths
- **The fake safety observation is genuine and practically important.** The 6-order-of-magnitude gap in EE displacement between frozen and active episodes (sub-micrometer vs. 200+ mm) makes dfCAR threshold completely insensitive across δ∈[2mm, 200mm]. This bimodal structure is convincing evidence that action collapse is a qualitatively distinct failure mode.
- **Oracle experiment design is methodologically sound.** Testing three oracle variants (adaptive-alpha, fixed-alpha, feature-space SDF) with ground-truth geometry cleanly separates representation quality from EE-only structural limitation. Consistent negative results across all three variants is strong evidence.
- **Honest reporting of the negative result.** The LoRA-only attribution experiment overturns the paper's original hypothesis. The 3-seed × 2-lambda comparison showing LoRA-only CAR=52.8% vs. SDF λ=0.005 CAR=50.5% (p=0.24) with identical per-task patterns is a clean null result.
- **dfCAR is simple, well-defined, and immediately adoptable.** Threshold invariance across 4 orders of magnitude requires no calibration.
- **Multiple converging evidence lines.** Fake safety demonstrated across Pi0 and Pi0.5; EE-only limitation shown through 3 oracle variants; SDF redundancy tested across 4 lambda values.

### Weaknesses
- **Narrow benchmark scope undermines generalizability.** All primary experiments use a single SafeLIBERO suite (object_pudding, 4 tasks) with one robot embodiment. The spatial_bowl results critically lack the LoRA-only control (plan_015 never completed). The claim "SDF is redundant across scenes" rests on a single scene.
- **Only two model families tested (Pi0, Pi0.5), both from the same architecture lineage.** No OpenVLA, RT-2, or other architecture tested. The central claim that fake safety is a general VLA problem requires broader evidence.
- **Statistical power is marginal throughout.** 3 seeds × 200 episodes per condition. The one-sided p=0.24 for LoRA vs. SDF λ=0.005 cannot reject the null, but the power to detect a meaningful 5pp effect is also low at n=3. λ=0.1 tested with only 2 seeds. Phase 2 uses 2 seeds. For a paper whose central claim is a null result, the burden of proof is higher than demonstrated. A formal equivalence test (TOST) is needed.
- **TSR collapse (73%→6%) not adequately analyzed.** The paper attributes this to "conservative behavior" but does not distinguish from catastrophic forgetting. Since both LoRA-only and LoRA+SDF show identical collapse, this is the most practically consequential result but receives insufficient analysis.
- **Phase 2 results are preliminary.** 2 seeds, mean CAR=59.5%, p=0.12 vs. LoRA-only. Neither conclusion (real effect vs. noise) is supported at this sample size.
- **No real-robot validation or sim-to-real discussion.** The dfCAR threshold of 0.1mm is calibrated for MuJoCo where actuator noise is effectively zero. Real-world sensor noise could require recalibration.

### Questions for Authors
1. Can you provide a formal equivalence test (TOST) for the SDF redundancy claim? What minimum detectable effect size at 80% power with n=3?
2. Do you have any evidence, even indirect, that the +22pp CAR gain over baseline in spatial_bowl is attributable to LoRA rather than SDF? Without this, cross-scene generalization of Claim 4 is unsupported.
3. Is the 73%→6% TSR drop consistent with standard catastrophic forgetting curves (monotonic decay with training steps)? Did you analyze per-task TSR as a function of training steps?
4. Have you applied dfCAR to published results from other VLA safety papers? Even a discussion of what published systems would look like under dfCAR would strengthen the contribution.
5. Why only object_pudding Level I? SafeLIBERO includes multiple difficulty levels and scene types.

### Scores (R1)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Overall | **2 (Reject)** | Core observation valuable but experimental scope too narrow for claim generality. Missing controls, marginal statistical power for null result, incomplete draft. |
| Soundness | 2 | Fake safety diagnosis and oracle experiments are sound. SDF redundancy null result lacks adequate power (n=3, no equivalence testing). Phase 2 preliminary (n=2). Missing spatial_bowl control. |
| Significance | 3 | If fake safety generalizes beyond Pi0/SafeLIBERO (plausible but unverified), it has immediate practical impact. dfCAR is adoption-ready. SDF redundancy finding could redirect community effort. |
| Clarity | 2 | Written sections are clear and well-structured, but paper has incomplete elements (placeholders, missing figures, outdated sections contradicting current claims). |
| Confidence | 4 (Expert) | Familiar with VLA architectures, SDF collision methods, SafeLIBERO, and relevant statistical methodology. |

---

## II. Reviewer R2 — Novelty & Related Work

### Summary
The paper identifies metric contamination in VLA safety evaluation (action collapse inflating CAR), proposes dfCAR to correct it, demonstrates EE-only SDF structural failure, and shows LoRA fine-tuning alone drives collision avoidance while SDF is redundant. All conditions suffer catastrophic task performance collapse.

### Strengths
- **The fake safety finding is well-documented and useful.** The demonstration that action collapse *systematically contaminates the primary evaluation metric* is a genuine contribution, even if action collapse itself is individually known.
- **Oracle SDF experiments are well-designed.** Testing three distinct oracle variants with ground-truth geometry eliminates prediction-error explanations and isolates the fundamental EE-only scope limitation.
- **The writing is direct and technically precise in diagnostic sections.** The introduction opens effectively and the paper generally avoids overclaiming.
- **The negative SDF redundancy finding is scientifically valuable.** Showing the avoidance signal comes from demonstration imitation rather than geometric supervision challenges a natural assumption.
- **dfCAR threshold invariance is elegant.** The six-order-of-magnitude displacement gap eliminates threshold tuning entirely.

### Weaknesses
- **Related work is severely underdeveloped.** Only 5 references in the submitted draft. Critical omissions include:
  - SafeVLA (Zhang et al., NeurIPS 2025): most direct competitor, uses constrained MDP for VLA safety. Do their reported CAR numbers suffer from the same contamination?
  - Configuration-space distance fields (Li et al., RSS 2024): directly addresses the EE-only SDF limitation by working in C-space.
  - RAIL (Jung et al., ICRA 2025), TamedPUMA (Bakker et al., L4DC 2025): runtime safety filtering methods providing contrasting approaches.
  - The paper needs a systematic taxonomy: post-hoc correction vs. constrained optimization vs. inference-time guidance vs. training-time supervision.
- **Novelty of dfCAR is limited.** Filtering a safety metric by displacement to exclude degenerate episodes is straightforward. For a CoRL main track paper, the methodological contribution needs to be either technically deeper or empirically broader. Currently it is neither.
- **Generalizability is a critical unaddressed weakness.** All evidence comes from SafeLIBERO with Pi0/Pi0.5. No experiments on OpenVLA, RT-2, Octo, or any non-Pi0-family model. For an evaluation methodology paper, the methodology should be validated across the models it claims to evaluate.
- **SDF redundancy claim is underpowered.** p=0.24 and p=0.48 do not support the *absence* of an effect — they merely fail to reject the null. A formal equivalence test (TOST) with pre-specified equivalence margin is needed. The paper states SDF contributes "0 additional percentage points" but confidence intervals likely include meaningful effects in both directions.
- **Capability-safety anti-correlation (Section 4.4) is trivially obvious.** Models that move more collide more. This should be a motivating paragraph, not a standalone claim.
- **Missing spatial_bowl LoRA-only control undermines cross-scene claims.**

### Questions for Authors
1. Have you tested dfCAR on any non-Pi0-family VLA? Even zero-shot evaluation of OpenVLA with displacement logging would substantially strengthen generalizability.
2. Can you provide formal equivalence tests (TOST) for the SDF redundancy claim?
3. How do you distinguish "genuine collision avoidance" from "the model learned conservative/hesitant behavior"? The EE displacement ~0.48m shows the robot moves, but does it move *around* obstacles or just less aggressively overall? Per-trajectory visualization or nearest-obstacle-distance analysis during active episodes would help.
4. Why does LoRA-only improve CAR by +26pp over baseline? If collision-free demo filtering biases the learned behavior toward conservative trajectories, this is data curation, not genuine safety learning. This mechanism should be discussed.
5. The title "98% of Collision Avoidance is an Illusion" — this is demonstrated only on Pi0/Pi0.5 on SafeLIBERO. Does the claim extend to other pipelines?

### Scores (R2)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Overall | **2 (Reject)** | Core finding useful but insufficiently novel for main conference. dfCAR is technically trivial. Experimental scope too narrow for claim breadth. Paper visibly incomplete. |
| Novelty | 2 | Fake safety observation is a useful diagnostic rather than a methodological advance. dfCAR is a simple threshold filter. SDF redundancy finding is interesting but underpowered. |
| Significance | 3 | If fake safety generalizes, meaningful impact on VLA safety evaluation. Recommendation to report both CAR and dfCAR is practical and easy to adopt. |
| Clarity | 2 | Diagnostic sections well-written. Paper incomplete with placeholder values, missing figures, inconsistent framing between sections. |
| Confidence | 3 | Familiar with VLA evaluation, SDF collision avoidance, and SafeLIBERO. Main uncertainty: whether fake safety is as prevalent as claimed beyond Pi0+SafeLIBERO. |

---

## III. Roundtable Discussion

### Step 2: Cross-Sharing

**R1 after reading R2:**
- Agrees related work is severely underdeveloped; 5 references is inadequate for CoRL
- Concurs the capability-safety anti-correlation is trivially obvious and should not be a standalone claim
- Acknowledges dfCAR novelty is technically simple; maintains the empirical bimodal-structure demonstration is non-trivial
- Agrees "98%" title may overstate given single-benchmark evidence

**R2 after reading R1:**
- Agrees TSR collapse is inadequately analyzed — the most practically consequential result
- Acknowledges the Pi0.5 baseline safe-episode displacement question is a real clarity issue
- Both reviewers independently flagged the need for equivalence testing (TOST) — strong convergence
- Concurs Phase 2 with n=2 is too preliminary for any conclusion

### Step 3: Convergence

**Full agreement (both reviewers):**
1. **Overall score: 2 (Reject)** — independent convergence
2. **Significance: 3** — underlying message important IF evidence strengthened
3. Fake safety finding is genuine and practically useful
4. dfCAR threshold invariance property is elegant
5. Experimental scope too narrow: one benchmark, one model family, n=3
6. Statistical treatment of null result (SDF redundancy) inadequate — needs equivalence testing
7. Paper materially incomplete (placeholders, missing figures)
8. Missing spatial_bowl LoRA-only control is a significant gap
9. Paper should be resubmitted after completing experiments and expanding scope

**Remaining divergence:**
- R1 gives dfCAR more credit as a methodological contribution; R2 considers it technically trivial
- R2 is more critical of related work gaps (identifies specific missing citations); R1 focuses more on experimental gaps
- On path to acceptance: R1 sees a viable path (complete controls + equivalence testing + one more model family); R2 additionally requires substantially expanded related work and questions whether dfCAR alone merits main-conference contribution

---

## IV. Consolidated Assessment

### Overall Score: **2 / 4 (Reject)**

### Headline Assessment
The paper identifies a real and practically important problem — fake safety from action collapse contaminates the primary VLA safety metric. The proposed correction (dfCAR) is simple, elegant in its threshold invariance, and immediately adoptable. The negative finding about SDF redundancy is scientifically valuable. However, the paper in its current form has critical gaps that prevent acceptance at CoRL 2026.

### Key Strengths (consensus)
1. **Fake safety identification is a genuine contribution.** The 6-order-of-magnitude bimodal displacement gap is a striking empirical finding. The community should know about this.
2. **Oracle SDF experiments are well-designed.** Three variants with ground-truth geometry cleanly isolate the structural EE-only limitation.
3. **Honest, well-hedged negative result.** The paper does not overclaim SDF redundancy — it provides appropriate statistical caveats.
4. **dfCAR requires no threshold tuning.** The invariance across [2mm, 200mm] makes it practically deployable.

### Critical Weaknesses (consensus)
1. **Narrow experimental scope.** One benchmark (SafeLIBERO), one model family (Pi0/Pi0.5), one scene for the core SDF comparison (object_pudding). For a paper claiming to identify a general evaluation problem, this is insufficient.
2. **Statistical power inadequate for the null claim.** n=3 seeds with one-sided Welch t-test cannot support "SDF adds nothing." Formal equivalence testing (TOST) with pre-specified margin is required. λ=0.1 and Phase 2 tested with only n=2 seeds.
3. **Related work severely underdeveloped.** 5 references is far below CoRL standards. Missing critical citations: SafeVLA, C-space distance fields, runtime safety filtering methods (RAIL, TamedPUMA, CAPE), diffusion policy collapse analysis.
4. **Missing spatial_bowl LoRA-only control.** Prevents cross-scene SDF attribution. The paper's own experiment plan (plan_015) was never completed.
5. **Paper incomplete.** Placeholder values in tables, missing figures, outdated sections contradicting current claims, inconsistent framing.
6. **TSR collapse (73%→6%) insufficiently analyzed.** The most practically consequential result receives superficial treatment. Is this catastrophic forgetting? Conservative behavior? The mechanism matters for the conclusion.

### Experiment Coverage vs. Design
The paper completed 8 of 9 planned experiments. The one missing experiment (spatial_bowl LoRA-only control, plan_015) is unfortunately the one needed for cross-scene generalization of the central SDF redundancy claim. The LoRA seed2 anomaly (CAR=48%, pulling the 3-seed mean to 52.8% with SD=4.2pp) weakened the statistical clarity of the originally "clean negative" narrative, forcing hedged language throughout.

### Recommendations for Revision
1. **Complete spatial_bowl LoRA-only control** (plan_015) — essential for cross-scene generalization
2. **Add at least one non-Pi0-family VLA** (OpenVLA or RT-2) — even zero-shot dfCAR analysis would help
3. **Perform formal equivalence testing (TOST)** with pre-specified equivalence margin for the SDF redundancy claim
4. **Expand related work** to 20+ references with systematic taxonomy of safety approaches
5. **Analyze TSR collapse mechanism** — learning curves, per-task temporal profiles, failure mode categorization
6. **Complete all tables and figures** — fill placeholders, add the displacement histogram and lambda-CAR curve
7. **Resolve narrative inconsistencies** — ensure all sections reflect the final "predominantly negative with boundary conditions" framing
8. **Downgrade capability-safety anti-correlation** from a standalone claim to a motivating observation

### Venue Fit
The paper addresses a relevant CoRL topic (VLA safety evaluation) and the negative finding about SDF redundancy is the type of result the community needs. However, the combination of narrow scope, insufficient statistical rigor for the central null claim, underdeveloped related work, and incomplete draft places it below the CoRL 2026 acceptance threshold (~39% acceptance rate). A thoroughly revised version addressing the above points could be competitive at CoRL 2027 or ICRA 2027.

### Score Summary
| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Overall | 2 | 2 | **2 (Reject)** |
| Soundness/Quality | 2 | — | 2 |
| Novelty | — | 2 | 2 |
| Significance | 3 | 3 | **3** |
| Clarity | 2 | 2 | **2** |
| Confidence | 4 | 3 | 3.5 |


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