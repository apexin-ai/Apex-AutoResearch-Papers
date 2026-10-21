---
dream_id: dream_20260525T223036
tier: worst
overall_score: 5/10 — marginally below acceptance
timestamp: 2026-05-25T23:26:26.708246+00:00
---

# Dream Review Report — CoRL 2026 Full Review

**Paper:** "Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion"
**Venue:** CoRL 2026
**Review Mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-25

---

## Roundtable Cross-Sharing Summary

### Agreements
- Both reviewers converge on **5/10** (marginally below acceptance threshold) independently.
- Both recognize the **fake safety identification** as the paper's strongest contribution — the 99.6% FSR for Pi0 is a striking, clearly presented result.
- Both flag the **2-seed LoRA-only baseline** as a critical statistical weakness: the central attribution claim (SDF adds nothing beyond LoRA capacity) rests on a +2.5pp delta with no confidence intervals or formal hypothesis test.
- Both find **displacement-filtered CAR** useful but technically straightforward — low novelty as a method contribution once the problem is identified.
- Both agree the **Phase 2 irreversibility claim** is underpowered (single seed, single checkpoint).
- Both note the paper's **narrow scope** (SafeLIBERO only, two scenes, related model families).

### Disagreements
- **Significance:** R1 rates 3/4 (good — useful diagnostic for the community), R2 rates 2/4 (fair — observation is unsurprising to safe RL practitioners). **Resolved toward R2's position** — the insight that inaction inflates safety metrics is well-known in constrained optimization; the VLA-specific demonstration is useful but not paradigm-shifting. Consensus: 2/4.
- **FSR metric redundancy:** R1 flags FSR as mathematically redundant (derivable from raw CAR + filtered CAR). R2 does not raise this. **Consensus: R1 is correct** — FSR adds no independent information, and listing it as a separate contribution overclaims.
- **Cross-model comparison fairness:** R1 critiques Table 1 for comparing finetuned Pi0 vs zero-shot Pi0.5/OpenVLA. R2 notes this but focuses more on scope. **Consensus: R1's concern is valid** — the taxonomy is descriptive rather than controlled. The paper should acknowledge that Pi0's action collapse is caused by SDF training, not inherent to the architecture.

### Complementary Insights
- R1 provides detailed experimental gap analysis (missing third LoRA seed, spatial_bowl LoRA-only control, threshold sensitivity). R2 provides broader positioning critique (missing related work, novelty limitations, specification gaming literature). Together they identify both micro-level and macro-level deficiencies.

---

## Consensus Assessment

### Paper Summary
The paper demonstrates that collision avoidance rate (CAR), the standard safety metric for VLA manipulation policies, is systematically unreliable. Through 6000+ episodes across three model families (Pi0, Pi0.5, OpenVLA) on SafeLIBERO, the authors identify three failure modes that inflate CAR without genuine avoidance: action collapse, geometric path safety, and random incompetence. They propose displacement-filtered CAR as a corrective metric and report a negative finding that SDF auxiliary training is neither necessary (LoRA finetuning alone achieves equivalent CAR) nor sufficient (causes irreversible task damage) for improving VLA collision avoidance.

### Strengths (Consensus)

1. **Striking quantitative demonstration of metric failure (both reviewers).** The 99.6% fake safety rate for Pi0 (A1) — a model with 91.5% CAR but 0% TSR and 18mm average EE displacement — is a compelling, clearly presented central result that should concern the VLA safety evaluation community.

2. **Clean mechanistic decomposition (R1 primary).** The three failure modes (action collapse, geometric path safety, random incompetence) provide practitioners with actionable diagnostic categories, even if the taxonomy is descriptive rather than formally principled.

3. **Practical metric with low adoption barrier (both reviewers).** Displacement-filtered CAR requires only end-effector position logging — no new hardware or model changes. This makes adoption realistic.

4. **Large-scale empirical effort (R1 primary).** 6000+ episodes, iterative debugging of measurement scripts, and multi-model evaluation demonstrate thorough empirical work.

5. **Honest negative results framing (R1 primary).** The paper does not oversell SDF. The finding that LoRA-only matches SDF in total CAR while maintaining higher TSR is presented transparently. The Phase 2 irreversibility finding is a genuine cautionary result.

6. **Well-written and clearly structured (both reviewers).** The paper is logically organized, claims are clearly stated, and the reader can follow the argument from metric critique to experimental evidence to negative finding.

### Weaknesses (Consensus)

1. **[Critical] Statistical insufficiency for the central attribution claim.** The LoRA-only vs SDF comparison (CAR 50.0% vs 52.5%, delta +2.5pp) uses 2 seeds for LoRA-only vs 3 for SDF, with no confidence intervals, no formal hypothesis test, and no per-seed breakdown reported. The 95% CI on the LoRA-only estimate likely spans ±5-7pp given binomial variance + between-seed variance. The paper cannot claim "statistically indistinguishable" without rigorous statistical support. This is the single most important weakness.

2. **[Critical] No threshold sensitivity analysis.** The δ=5mm threshold for displacement filtering is stated without justification. No sensitivity analysis showing how filtered CAR, FSR, or the LoRA-vs-SDF comparison changes across threshold values (e.g., 2mm, 5mm, 10mm, 20mm). If the EE displacement distribution is bimodal, the threshold may not matter, but this must be demonstrated.

3. **[Major] Limited novelty of core observation.** That collision-absence metrics reward inaction is conceptually straightforward and has precedent in the safe RL / constrained optimization literature (Goodhart's law, specification gaming). The VLA-specific demonstration adds value but is not a paradigm shift. The displacement-filtered CAR fix is technically trivial once the problem is identified.

4. **[Major] Related work is severely underdeveloped.** Only 3 references in the main paper. Critical missing citations include: specification gaming literature (Krakovna et al., 2020; Amodei et al., 2016), reward hacking (Skalse et al., 2022), catastrophic forgetting / multi-task interference (relevant to SDF damage), LoRA/PEFT for robotics, activity-conditioned safety evaluation in safe RL, and VLA safety benchmarks beyond SafeLIBERO.

5. **[Major] Phase 2 irreversibility claim is underpowered.** Based on a single seed from a single checkpoint (seed2, λ=0.005, 10K steps). Different seeds, checkpoints, hyperparameters (higher LR, longer training), or LoRA ranks might yield different recovery trajectories. The claim "SDF training is a one-way door" is overstrong for the evidence.

6. **[Major] Cross-model comparison is not controlled.** Table 1 compares a finetuned model (Pi0+LoRA+SDF) against zero-shot models (Pi0.5, OpenVLA) — these are fundamentally different experimental conditions. Pi0's action collapse is caused by SDF training, not inherent to the Pi0 architecture. The "three failure modes" are observed in three different setups, not three controlled comparisons.

7. **[Major] Narrow scope.** Single benchmark (SafeLIBERO), two scenes (one dominant — object_pudding), and Pi0/Pi0.5 from the same model family. OpenVLA evaluation is noisy (15% NaN episodes) and ambiguous (FSR=42%). Generalizability claims require additional benchmarks or model families.

8. **[Minor] FSR metric is redundant.** FSR = 1 − (filtered_CAR × filtered_denominator) / (raw_CAR × total_episodes). It contains no information beyond filtered CAR and raw CAR jointly. Listing it as a separate contribution is overclaiming.

9. **[Minor] Missing LoRA-only control on spatial_bowl.** Without this, the +9pp on spatial_bowl cannot be attributed to SDF vs LoRA finetuning.

10. **[Minor] OpenVLA NaN episode handling unclear.** 15% of episodes terminated early due to NaN actions. Whether these are counted as "safe" in CAR affects the FSR=42% figure. Should report both including and excluding.

### Required Revisions (for potential acceptance)

1. **Run a third LoRA-only seed** and report per-seed CAR values with confidence intervals. Perform a formal statistical test (e.g., two-sample proportion test or permutation test) for the LoRA-only vs SDF comparison.

2. **Add threshold sensitivity analysis.** Plot filtered CAR and FSR as a function of δ across all conditions (Pi0, Pi0.5 baseline, LoRA-only, LoRA+SDF). Demonstrate robustness to threshold choice.

3. **Expand related work substantially.** Add at least 8-10 references covering specification gaming, reward hacking, catastrophic forgetting, LoRA for robotics, and safe RL evaluation methodology. Position the contribution relative to existing metric validity work.

4. **Strengthen Phase 2 with at least one additional seed or checkpoint.** Alternatively, temper the "irreversible" language to "not recoverable under the tested conditions."

5. **Clarify cross-model comparison.** Acknowledge that Table 1 compares different experimental conditions. Reframe as "failure modes observed across diverse conditions" rather than "cross-model comparison."

6. **Run LoRA-only on spatial_bowl** to complete the attribution analysis.

7. **Report OpenVLA CAR with and without NaN-terminated episodes.**

### Questions for Authors

1. What are the per-seed CAR values for the 2 LoRA-only seeds? If one yields 45% and the other 55%, between-seed variance alone could account for the SDF delta.

2. What is the distribution of EE displacements for safe episodes in Pi0.5 baseline? Is it bimodal (confirming the 5mm threshold sits in a gap)?

3. Has any prior safe RL work noted that low-action policies trivially satisfy collision-rate metrics? How does your observation differ beyond VLA-specific context?

4. Why not propose a more informative metric — e.g., conditioning on task-relevant progress or comparing to a reference trajectory?

5. Were NaN-terminated OpenVLA episodes counted as safe or excluded from CAR calculation?

6. What LoRA rank and alpha values are used? Are they identical for LoRA-only and LoRA+SDF conditions?

7. What fraction of Pi0.5 total episodes (not just safe subset) show action collapse (EE displacement < 5mm)?

8. Could Phase 2 recovery improve with higher learning rate, longer training (e.g., 40K additional steps), or higher LoRA rank?

### Missing Related Work

**Specification gaming / Metric validity:**
- Krakovna et al. (2020), "Specification gaming: the flip side of AI ingenuity"
- Amodei et al. (2016), "Concrete Problems in AI Safety"
- Skalse et al. (2022), "Defining and Characterizing Reward Hacking"
- Pan et al. (2022), "The Effects of Reward Misspecification"

**Safe RL evaluation:**
- Dulac-Arnold et al. (2021), "Challenges of Real-World RL"
- Thomas et al. (2019), "Preventing undesirable behavior of intelligent machines"
- Activity-conditioned safety in constrained MDPs (CPO, TRPO-Lagrangian)

**Catastrophic forgetting (for SDF damage finding):**
- French (1999), "Catastrophic forgetting in connectionist networks"
- Hessel et al. (2019), "Multi-Task Deep RL with PopArt"

**LoRA/PEFT for robotics:**
- Hu et al. (2022), "LoRA: Low-Rank Adaptation"
- Embodiment-specific adaptation (RT-2, Octo fine-tuning)

**VLA safety beyond SafeLIBERO:**
- RoboCasa, BEHAVIOR-1K, or other manipulation benchmarks with safety considerations

---

## Final Scores

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness/Quality | 2/4 | —  | 2/4 |
| Originality | — | 2/4 | 2/4 |
| Clarity | 3/4 | 3/4 | 3/4 |
| Significance | 3/4 | 2/4 | 2/4 |
| Overall | 5/10 | 5/10 | **5/10** |
| Confidence | 4/5 | 4/5 | 4/5 |

---

## Meta-Review

Both reviewers independently converge on **5/10 — marginally below the acceptance threshold**. The paper identifies a real, quantitatively demonstrated evaluation validity problem (99.6% fake safety in Pi0) that the VLA safety community should be aware of. However, three factors prevent acceptance: (1) the central attribution claim (SDF adds nothing beyond LoRA) lacks statistical rigor due to a 2-seed baseline with no confidence intervals; (2) the core observation (inaction inflates safety metrics) has limited novelty for the broader robotics/ML community, and the proposed fix (displacement filtering) is technically trivial once stated; (3) the narrow scope (one benchmark, two scenes, closely related model families) limits generalizability. The paper has a clear path to acceptance: a third LoRA seed with formal statistics, threshold sensitivity analysis, expanded related work positioning against specification gaming literature, and ideally evaluation on one additional benchmark would address all major concerns. The Phase 2 irreversibility finding is genuinely interesting but needs strengthening beyond a single seed. Recommend **revision and resubmission** with the above additions.

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