---
dream_id: dream_20260525T223036
tier: median
overall_score: weak reject
timestamp: 2026-05-25T23:17:56.601711+00:00
---

# Dream Review Report: "Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion"

**Dream ID:** 20260525T223036  
**Target Venue:** CoRL 2026 (~30-35% acceptance rate)  
**Review Mode:** Full (2 Reviewers + Roundtable)

---

## Roundtable Process Summary

- **R1 (Methods & Experiments):** Evaluated methodological soundness, experimental rigor, reproducibility, and result presentation.
- **R2 (Novelty & Related Work):** Evaluated originality, significance, related work completeness, and positioning.
- **Step 1 (Independent):** Both reviewers completed blind independent reviews.
- **Step 2 (Cross-sharing):** Reviews exchanged; key divergences identified.
- **Step 3 (Convergence):** Director reconciled reviewer assessments against the actual submitted PDF. Both reviewers incorrectly reported extensive placeholder values in tables — the submitted PDF contains complete numerical results in all 9 tables. Director corrected this factual error while retaining valid analytical points.
- **Step 4 (Synthesis):** This consolidated report.

---

## Paper Summary

The paper argues that Collision Avoidance Rate (CAR) — the standard safety metric for VLA models — is systematically contaminated by "fake safety." Through evaluation of 6000+ episodes across three model families (Pi0, Pi0.5, OpenVLA), the authors show that 70–99.6% of nominally "safe" episodes reflect action collapse or geometric coincidence rather than intentional avoidance. They propose displacement-filtered CAR (dfCAR, Eq. 1) as a corrective metric, use SDF auxiliary loss as a diagnostic probe to demonstrate real avoidance is achievable (+25pp CAR) but at extreme task cost (TSR: 73%→7%), and characterize the safety-capability landscape through a 4-point λ curve and phase-2 ablation.

---

## Consolidated Strengths

1. **Important and timely problem identification.** The "fake safety" phenomenon — where action-collapsed or minimally-moving policies trivially achieve high CAR — is a real confound affecting VLA safety evaluation. Quantifying this across three model families (Pi0 at 99.6% fake safe, OpenVLA at ~70%, Pi0.5 at 98.2% of safe episodes) provides useful empirical documentation that the community needs to see. [R1, R2 agree]

2. **Comprehensive experimental design.** The paper covers substantial ground: (a) cross-model fake safety analysis (Table 1), (b) LoRA vs. SDF attribution decomposition (Tables 3-4), (c) 4-point lambda dose-response curve (Tables 5-6), (d) phase-2 ablation for supervision persistence (Table 7), (e) cross-scene generalization (Tables 8-9). All tables contain actual numerical values. The experimental structure is logical and builds a coherent narrative. [R1]

3. **Phase-2 ablation is a well-designed experiment.** Testing whether safety encoding persists after removing SDF supervision (TSR recovers to 42%, CAR regresses to 32%) provides a genuine insight: safety requires continuous geometric supervision, ruling out a naive "safety imprinting" curriculum. [R1, R2 agree]

4. **Honest self-positioning.** The paper explicitly positions SDF as a "diagnostic probe, not solution" and acknowledges the extreme tradeoff. The limitations section is forthcoming about narrow empirical scope. This calibrated framing builds credibility. [R2]

5. **Lambda curve reveals structural insight.** The abrupt TSR collapse at λ=0.005 (from 36.5% to 7%) followed by CAR saturation (~52-58%) suggests a fundamental tension in how diffusion-based VLA action heads handle competing objectives. The marginal analysis (Table 6) showing 0.49 CAR/TSR-pp-lost at the first step vs. 0.91 at higher λ is informative. [R1]

6. **Cross-scene analysis identifies structural EE-only limitation.** The dramatic attenuation of SDF benefit on spatial_bowl (+5pp vs. +25pp on object_pudding) due to arm-body collision dominance provides a clear mechanistic explanation and motivates full-kinematic SDF as future work. [R1, R2 agree]

---

## Consolidated Weaknesses

### Major

**W1. Limited novelty of the core observation.** [R2, R1 partially agrees]  
"A robot that doesn't move can't collide" is conceptually straightforward. The paper's value lies in the quantification, but any researcher observing TSR=0% alongside CAR=91.5% would immediately question the CAR number. The paper does not demonstrate concrete downstream harm — no published work is cited that drew incorrect conclusions from contaminated CAR. Without evidence of actual misleading claims in the literature, the urgency of the problem remains somewhat hypothetical. Severity: **Major for novelty assessment.**

**W2. dfCAR is a trivially simple metric contribution.** [R2, R1 agrees]  
The proposed metric (Eq. 1) is a one-line displacement filter. While correct and useful, this is the kind of practical fix that would normally appear as a paragraph in a methods section, not as a primary contribution. A stronger metric contribution might involve: continuous safety scores weighted by proximity, behavioral decomposition of CAR into intentional/incidental categories, or statistical tests distinguishing genuine avoidance from coincidental safety.

**W3. Severely sparse related work — only 5 references.** [R2 primary, R1 agrees]  
Five references is far below the standard for any top venue. Critical missing categories include:
- Safe RL foundations (CPO, constrained MDPs)
- Alternative robot safety metrics (minimum clearance, time-to-collision, near-miss frequency)
- Spatial-aware VLA methods (SpatialVLA, 3D-CAVLA, GeoAware-VLA, DepthVLA)
- Configuration-space SDFs for full-body collision (Li et al., RSS 2024)
- Other VLA architectures (RT-2, Octo) for scope contextualization
- Action collapse / mode collapse in diffusion policies (Dong et al., 2025)
- Test-time safety methods (RAIL, TamedPUMA)
- Safe manipulation surveys (Zhang et al., 2025)

This is the paper's most glaring presentation deficit.

**W4. No deployable solution offered.** [R2 primary]  
The paper identifies a metric problem (dfCAR fix is trivial) and shows that SDF produces real avoidance but at impractical tradeoff (TSR: 73%→7%). For CoRL, reviewers will ask: "What should practitioners do?" The answer — "report dfCAR alongside CAR" — is underwhelming. The phase-2 ablation rules out naive curriculum learning. Without at least a promising direction toward resolving the tradeoff, the paper's practical impact is limited.

### Moderate

**W5. Cross-model comparison is uneven.** [R1, R2]  
The three model families are tested under very different conditions: Pi0 is LoRA+SDF fine-tuned (TSR=0%), Pi0.5 is a baseline (TSR=73%), OpenVLA is zero-shot (TSR~8%). These are not comparable experimental conditions. The fake safety in Pi0 (TSR=0%) is trivially expected. The OpenVLA results use approximate values (~) throughout. A cleaner comparison would test all models under the same condition (e.g., all zero-shot, or all fine-tuned).

**W6. Statistical concerns.** [R1]  
- λ=0.1 uses only 1 seed (Table 5) while λ=0.005 and 0.01 use 3-seed averages. This asymmetry weakens the lambda curve's reliability at the high-λ endpoint.
- No confidence intervals or error bars reported for any metric. Given the binary nature of CAR/TSR, Clopper-Pearson intervals would be straightforward and informative.
- LoRA-only baseline uses 2 seeds while SDF conditions use 3. Consistency would strengthen attribution claims.

**W7. SDF loss formulation underspecified.** [R1]  
Eq. 2 states L = L_action + λ·L_SDF but never specifies the exact form of L_SDF. What is the clamping threshold? Is there an Eikonal regularizer? How are query points sampled during training (along predicted trajectories or from the voxel grid)? For a methods-oriented paper, this omission is notable.

**W8. Title and framing sensationalized.** [R2]  
"Rethinking VLA Safety Evaluation" and "98% of Collision Avoidance is an Illusion" overstate the scope. The paper examines one metric (CAR) on one benchmark (SafeLIBERO) with 2 scenes. The 98% figure primarily comes from a model with TSR=0%, where fake safety is expected by construction. A more calibrated title would improve credibility with reviewers.

### Minor

**W9. Formatting issues.** On page 3, Tables 1 and 3 overlap significantly — column headers from Table 3 intrude into Table 1's data rows, creating garbled text. This is a clear formatting/layout bug that harms readability of the paper's central results.

**W10. Cross-scene analysis limited to 2 scenes.** [R1, R2]  
object_pudding (EE-obstacle dominant) and spatial_bowl (arm-body dominant) represent two points on a spectrum. Additional scenes would strengthen the generalization of the EE-only limitation finding.

**W11. Computational details absent.** [R1]  
No GPU type, training wall-clock time, or total compute budget reported. This limits reproducibility assessment.

---

## Questions for Authors

1. Can you cite any published work that drew an incorrect safety conclusion due to CAR contamination? This would concretely demonstrate the downstream harm of fake safety.

2. Why not propose a continuous safety metric (e.g., weighted by minimum obstacle distance or EE displacement magnitude) instead of the binary dfCAR filter? This would be a more substantial metric contribution.

3. What is the exact form of L_SDF? Please provide the full loss equation including clamping, Eikonal regularization, and query point sampling strategy.

4. For the phase-2 ablation, CAR regresses to 32% — slightly below LoRA-only (38%). Is this 6pp gap statistically significant, or within noise? If significant, it would suggest SDF training actually damages the incidental safety patterns learned by LoRA.

5. The lambda curve has only 4 points with the highest (λ=0.1) from a single seed. Have you considered finer-grained λ search in the 0 < λ < 0.005 range where the critical transition occurs?

6. For Pi0.5 baseline (TSR=73%, CAR=28%), how many total safe episodes exist across seeds? If the absolute count is small, the 98.2% fake safe rate estimate has high variance.

7. What is the actuator resolution of the simulated robot? Is the 0.1mm obstacle displacement threshold truly sub-actuator-resolution as implied?

---

## Experiment Coverage Assessment

Comparing against `review_context.yaml` planned experiments:

| Experiment | Status in Paper |
|---|---|
| A1 EE displacement re-eval (50ep) | ✅ Reported (Section 4.1, ~0.002m EE disp) |
| OpenVLA zero-shot (200ep) | ✅ Reported (Tables 1-2, approximate values) |
| LoRA baseline eval (2 seeds) | ✅ Reported (Tables 3-5, TSR=36.5%, CAR=38%) |
| Phase 2 λ=0 ablation | ✅ Reported (Table 7, TSR=42%, CAR=32%) |
| spatial_bowl eval | ✅ Reported (Tables 8-9, +5pp SDF effect) |
| Lambda=0.1 bracket | ✅ Reported (Table 5, 1 seed, TSR=1.5%, CAR=58%) |
| Plan_011 decision | Implicitly covered (50ep sufficient) |

**All planned experiments are present in the paper.** The experimental coverage is complete relative to the design document.

---

## Scores

### R1 (Methods & Experiments)
| Dimension | Score | Notes |
|---|---|---|
| Soundness | 2.5/4 | dfCAR and phase-2 design are sound; SDF loss underspecified; attribution analysis reasonable but confounded by uneven conditions |
| Empirical Rigor | 2.5/4 | All planned experiments present with actual data; λ=0.1 single seed and lack of error bars are concerns; 200ep evaluations adequate |
| Clarity (methods/tables) | 2/4 | Page 3 formatting issues; SDF loss not fully specified; tables otherwise clear |
| Overall | 5/10 | |
| Confidence | 4/5 | |

### R2 (Novelty & Related Work)
| Dimension | Score | Notes |
|---|---|---|
| Novelty | 2/4 | Core observation important to document but conceptually straightforward; dfCAR trivially simple; SDF probe adds moderate novelty |
| Significance | 2/4 | Problem matters but practical impact limited; no solution offered; diagnostic-only framing risky for CoRL |
| Related Work | 1/4 | 5 references is critically insufficient; major categories of relevant work entirely absent |
| Overall | 4/10 | |
| Confidence | 4/5 | |

### Consolidated Overall
| Dimension | Score |
|---|---|
| Soundness | 2.5/4 |
| Novelty | 2/4 |
| Significance | 2/4 |
| Empirical Completeness | 3/4 |
| Clarity & Presentation | 2/4 |
| Related Work | 1/4 |
| **Overall** | **4.5/10** |
| **Confidence** | **4/5** |

---

## Final Assessment

**Recommendation: Weak Reject (4.5/10)**

**Key reasoning:**

The paper identifies a real and important problem — that CAR is systematically contaminated by fake safety across VLA model families. The experimental design is comprehensive and all planned experiments are completed. The phase-2 ablation and lambda dose-response curve provide genuine insights about the safety-capability landscape.

However, the paper falls short of the CoRL acceptance bar for several reasons:

1. **Novelty gap:** The core observation that non-moving robots trivially achieve high CAR is close to self-evident. The metric fix (dfCAR) is a one-line filter. The SDF probe concept adds moderate novelty but doesn't resolve the tradeoff.

2. **No actionable solution:** The paper diagnoses a problem but offers no path forward beyond "use dfCAR" and "future work on adaptive λ / full-body SDF." For CoRL, diagnostic-only papers need exceptional insight to clear the bar — this paper's insights, while valid, are not sufficiently deep.

3. **Critically sparse related work:** 5 references is unacceptable. Major bodies of relevant work (safe RL, spatial-aware VLAs, C-space SDFs, alternative safety metrics) are entirely absent.

4. **Presentation issues:** Page 3 formatting errors, sensationalized title, missing computational details.

**To reach acceptance (estimated improvements needed):**
- Expand related work to 25-30 references minimum
- Propose a more sophisticated metric beyond binary dfCAR (continuous, multi-dimensional)
- Add at least preliminary results on mitigating the tradeoff (adaptive λ, curriculum, or partial-body SDF)
- Fix formatting, calibrate title
- Add confidence intervals to all metrics
- Strengthen cross-model comparison with matched experimental conditions


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