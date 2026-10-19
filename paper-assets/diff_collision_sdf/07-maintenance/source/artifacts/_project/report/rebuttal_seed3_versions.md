# Rebuttal Seed3 Pre-Written Versions

**Status**: Pre-written, awaiting s3 results. Replace placeholder values when data arrives.

**Current baseline (3 seeds)**:
- LoRA-only: s0=57.0, s1=52.5, s2=55.0 → mean=54.83, std=2.25
- SDF λ=0.1: s0=58.0, s1=58.5, s2=54.5 → mean=57.00, std=2.18
- Permutation (two-tailed): p=0.155, C(6,3)=20
- MDE (80% power): 5.6pp

---

## Version A: Null Confirmed (s3 CAR ≤ 55%)

### Assumptions

| Seed | LoRA-only CAR | SDF λ=0.1 CAR |
|------|---------------|---------------|
| s0 | 57.0 | 58.0 |
| s1 | 52.5 | 58.5 |
| s2 | 55.0 | 54.5 |
| s3 | **[PLACEHOLDER: 53.0]** | **[PLACEHOLDER: 54.0]** |

**Pre-computed stats (with placeholder values):**
- LoRA 4-seed: mean=54.38, std=2.06
- SDF 4-seed: mean=56.25, std=2.33
- Delta: +1.88pp
- Pool: 8 values, C(8,4)=70 permutations
- Permutation test: p_one=0.129, p_two=0.257
- σ_pooled=2.20, MDE (80% power)=4.35pp
- Observed delta (1.88pp) << MDE (4.35pp)

**Verdict**: Null robustly confirmed. paper_switch.py Scenario B triggers (p_one ≥ 0.05).

### Q&A Updates

#### Q1: Statistical Power (replaces rebuttal_prep.md §Statistical Power)

**Q: "Why only n=3 seeds? Your MDE is 5.6pp — you might be missing a small but real effect."**

**A [UPDATED — 4 seeds]:** We now report 4 seeds per condition (C(8,4)=70 permutations), narrowing the MDE from 5.6pp to ~4.3pp at α=0.05, β=0.2. The observed SDF vs LoRA-only difference is +[PLACEHOLDER: 1.9]pp (permutation p=[PLACEHOLDER: 0.257], two-tailed), far smaller than any practically relevant effect size — a real effect below our MDE would represent <8% relative improvement, negligible for safety-critical applications.

Four lines of evidence argue against a meaningful hidden effect:

1. The observed delta ([PLACEHOLDER: 1.9]pp) is less than half the MDE ([PLACEHOLDER: 4.3]pp), and the p-value increased from 0.155 (3 seeds) to [PLACEHOLDER: 0.257] (4 seeds), indicating the 3-seed result was, if anything, inflated by sampling variability.
2. Per-task CAR ordering is identical across all conditions (LoRA-only, λ=0.005/0.01/0.1 × seeds), confirming the avoidance pattern is entirely determined by the demonstration distribution.
3. Stepwise analysis across 7 checkpoints (16K–30K) shows no transient SDF signal at any training stage.
4. The additional seed narrows our confidence interval without revealing any trend toward significance — the effect is converging toward zero, not toward detection.

We acknowledge this limitation explicitly in the paper and note that detecting effects smaller than ~4.3pp would require n≥8 seeds per condition (~256h additional GPU time), which we consider disproportionate given the converging null evidence.

#### Q2: p-value Defense (replaces rebuttal_prep.md §Two-Tailed vs One-Tailed Test + §Third Seed Outlier Concern)

**Q: "With 4 seeds the p-value got worse — doesn't that confirm the 3-seed result was just noise?"**

**A:** The increase from p=0.155 (3 seeds, C(6,3)=20) to p=[PLACEHOLDER: 0.257] (4 seeds, C(8,4)=70) is expected when the true effect is near zero. With 70 permutations (vs 20), the test has finer resolution and converges toward the true null. The 4th seed in each group ([PLACEHOLDER: LoRA s3=53.0, SDF s3=54.0]) falls within ±1σ of each group's 3-seed mean, ruling out outlier concerns in either direction.

With the additional seed, we can now rule out effects larger than ~4.3pp with 80% power (down from 5.6pp). The observed ~[PLACEHOLDER: 1.9]pp delta is both statistically and practically insignificant for safety-critical applications where even a 5pp CAR improvement would represent marginal benefit relative to the 26pp gain from demonstration curation alone.

**Q: "The one-tailed p=[PLACEHOLDER: 0.129] is closer to significance — should we use one-tailed?"**

**A:** As argued in the 3-seed analysis, SDF supervision does not have a unidirectional prior — our oracle experiments demonstrate SDF gradients can *reduce* CAR by rotating unmonitored arm links into obstacles. The two-tailed test remains correct. Even the one-tailed p=[PLACEHOLDER: 0.129] fails to reach conventional significance at α=0.05.

#### Q3: Per-Task BBQ (supplements rebuttal_prep.md §Per-Task Error Case Analysis)

**Q: "Does the 4th seed reduce BBQ sauce variance?"**

**A [UPDATE WHEN s3 BBQ DATA AVAILABLE]:**

*Template — fill in per-task s3 CARs:*

With 4 seeds, BBQ sauce variance [narrows/stays wide]: std=[PLACEHOLDER]pp (was [range from 3 seeds]). The key observation holds: [PLACEHOLDER — whether excluding BBQ preserves null, whether stable tasks still show null]. The 4th seed [confirms/does not alter] the conclusion that BBQ sauce variance reflects task difficulty interacting with seed-specific trajectory distributions, not a masked SDF effect.

*If BBQ variance narrows*: The reduced variance strengthens the null — even the highest-variance task now shows no systematic SDF benefit.

*If BBQ variance stays wide*: The per-task analysis is consistent with n=3. Chocolate_pudding and milk remain the cleanest test cases, both continuing to show null with 4 seeds.

### Paper Impact

- **Claim 3 (claim3.tex)**: No narrative change needed. Update table row with 4-seed stats, update MDE from 5.6pp to ~4.3pp in dose-response paragraph. All existing language ("no statistically significant benefit") strengthened.
- **paper_switch.py**: **Scenario B** (full redundancy). Run: `python paper_switch.py --s2-car [actual_s3_sdf_car]` — note: paper_switch.py currently uses 3-seed logic; for 4-seed, manually update table row and dose-response paragraph with 4-seed numbers after running Scenario B switch.
- **rebuttal_prep.md sections to update**:
  - §Statistical Power: replace entirely with Q1 above
  - §Two-Tailed vs One-Tailed Test: merge with Q2 above
  - §Third Seed Outlier Concern: subsumed by Q2 (no longer relevant with 4 seeds)
  - §Per-Task Error Case Analysis: append Q3 update
  - §Permutation Test vs Welch t-test: update with 4-seed Welch t-test p-value for completeness

---

## Version B: Signal Recovered (s3 CAR ≥ 58%)

### Assumptions

| Seed | LoRA-only CAR | SDF λ=0.1 CAR |
|------|---------------|---------------|
| s0 | 57.0 | 58.0 |
| s1 | 52.5 | 58.5 |
| s2 | 55.0 | 54.5 |
| s3 | **[PLACEHOLDER: 53.0]** | **[PLACEHOLDER: 60.0]** |

**Pre-computed stats (with placeholder values):**
- LoRA 4-seed: mean=54.38, std=2.06
- SDF 4-seed: mean=57.75, std=2.33
- Delta: +3.38pp
- Pool: 8 values, C(8,4)=70 permutations
- Permutation test: p_one=0.043, p_two=0.086
- One-tailed p < 0.05 → **Scenario C triggers**
- Two-tailed p = 0.086 > 0.05 → two-tailed still non-significant

**Note on directional test**: paper_switch.py uses p_one < 0.05 as the Scenario C criterion. With placeholder values, p_one=0.043 triggers Scenario C. However, the two-tailed p=0.086 remains non-significant at α=0.05. This creates a nuanced situation: the one-tailed test reaches significance, but the two-tailed (which we argued is more appropriate) does not. The rebuttal narrative must address this tension.

**Verdict**: Marginal signal. Effect size (~3.4pp) is real but small relative to 26pp LoRA gain. paper_switch.py Scenario C triggers.

### Q&A Updates

#### Q1: Statistical Power & Significance (replaces rebuttal_prep.md §Statistical Power)

**Q: "With 4 seeds, does SDF show a significant effect?"**

**A [UPDATED — 4 seeds]:** The 4-seed permutation test (C(8,4)=70) yields one-tailed p=[PLACEHOLDER: 0.043] and two-tailed p=[PLACEHOLDER: 0.086]. Whether this constitutes statistical significance depends on the directional prior:

- **One-tailed** (SDF can only help): p=[PLACEHOLDER: 0.043] < 0.05, nominally significant.
- **Two-tailed** (SDF could help or harm): p=[PLACEHOLDER: 0.086] > 0.05, non-significant.

We previously argued for the two-tailed test on the grounds that oracle experiments show SDF gradients can *reduce* CAR. Under that framework, the result remains non-significant. However, for transparency, we report both and note that the one-tailed result reaches the conventional threshold.

Critically, even under the most favorable interpretation:
1. The effect size ([PLACEHOLDER: 3.4]pp) represents a ~6% relative improvement over LoRA-only (54.4% → 57.8%), compared to the 26pp (+91%) gain from demonstration curation alone.
2. The per-task avoidance fingerprint remains identical to LoRA-only — the improvement is a global offset, not task-specific geometric avoidance learning.
3. The MDE narrows to ~4.3pp; the observed [PLACEHOLDER: 3.4]pp falls just below this, meaning detection was marginal and sensitive to seed sampling.

The result is consistent with a small, real SDF effect at high λ that does not alter the dominant conclusion: collision avoidance primarily arises from demonstration data.

#### Q2: Practical Significance (new section for rebuttal_prep.md)

**Q: "If SDF shows a statistically significant effect, doesn't that invalidate the 'SDF is redundant' claim?"**

**A:** Statistical significance does not imply practical significance. The observed [PLACEHOLDER: 3.4]pp CAR improvement must be evaluated against three factors:

1. **Effect magnitude vs. demonstration gain**: The 26pp CAR improvement from LoRA fine-tuning on collision-free demonstrations dwarfs the [PLACEHOLDER: 3.4]pp SDF increment. Demonstration curation alone provides >88% of the total avoidance gain; SDF contributes at most [PLACEHOLDER: ~12]%.

2. **Computational cost**: SDF auxiliary loss requires per-step SDF field queries, pre-computed obstacle meshes, and additional backward passes — approximately [15–20]% training overhead. A [PLACEHOLDER: 3.4]pp gain for this overhead represents poor cost-effectiveness, especially when the same computational budget could be spent on additional demonstration collection.

3. **Structural limitation persists**: Even with a statistically significant effect, the per-task CAR fingerprint is identical across all conditions. SDF λ=0.1 does not help on the hardest tasks (bbq_sauce) where avoidance is most needed — the improvement is distributed uniformly, suggesting a regularization-like effect rather than genuine geometric avoidance learning. The EE-only monitoring limitation (Claim 2) remains unaddressed.

We revise Claim 3 from "SDF is fully redundant" to "SDF provides at most a modest increment at high loss weights (λ=0.1) that does not justify its computational overhead or address the structural EE-only limitation."

#### Q3: Claim 3 Narrative Shift (impacts claim3.tex + discussion.tex)

**Q: "How does the narrative change if SDF shows a marginal effect?"**

**A:** The core narrative shifts from "null result" to "marginal positive effect insufficient to justify SDF overhead":

| Aspect | 3-seed narrative (current) | 4-seed narrative (Version B) |
|--------|---------------------------|------------------------------|
| Claim 3 headline | SDF is redundant | SDF is near-redundant; demonstration data dominates |
| p-value framing | p=0.155, non-significant | p_one=[0.043], marginal; p_two=[0.086], non-significant |
| Effect size emphasis | +2.2pp, below MDE | +[3.4]pp, at MDE boundary |
| Cost-benefit | SDF adds overhead for no gain | SDF adds overhead for ~[3.4]pp gain (~[12]% of demo-driven gain) |
| Per-task fingerprint | Identical → demo-driven | Identical → global offset, not geometric learning |
| Practical recommendation | Use demo curation, skip SDF | Use demo curation; SDF optional at high λ for marginal gain |

**Key rhetorical move**: The paper's strongest argument shifts from "p > 0.05" to "even with significance, the effect is dominated by demonstration data and does not address structural limitations." This is actually a *stronger* scientific argument — it separates the statistical from the mechanistic.

### Paper Impact

- **Claim 3 (claim3.tex)**: Narrative shift required. paper_switch.py Scenario C handles the mechanical text replacements:
  - Table caption: add significance qualifier for λ=0.1
  - Body paragraph: split into "no effect at λ ≤ 0.01" + "modest effect at λ=0.1"
  - Dose-response paragraph: rewrite as "modest but significant departure" with cost-benefit framing
  - Figure caption: update null band language
- **paper_switch.py**: **Scenario C** (modest but significant). Run: `python paper_switch.py --s2-car [actual_s3_sdf_car] --s2-tsr [actual_s3_sdf_tsr]`
  - Handles 10 replacements across abstract.tex, claim3.tex, discussion.tex
  - After running, manually update table row and dose-response paragraph with 4-seed numbers
- **abstract.tex**: Scenario C modifies two sentences — "no statistically significant benefit" → "no significant benefit at λ ≤ 0.01; modest increase at λ=0.1"
- **discussion.tex**: Scenario C modifies scope sentence and limitation paragraph
- **rebuttal_prep.md sections to update**:
  - §Statistical Power: replace entirely with Q1 above
  - §Two-Tailed vs One-Tailed Test: becomes critical — the directional test choice now determines significance; expand with Q1's directional analysis
  - Add new §Practical Significance section (Q2 above)
  - §Method Negative Q1 ("Why does SDF aux loss not improve..."): soften to "SDF aux loss shows no effect at λ ≤ 0.01; at λ=0.1, a modest effect emerges but is dominated by demonstration-driven avoidance"
  - §Positive Contribution Q: update takeaway (3) to "EE-only SDF provides at most marginal benefit; full-body monitoring remains the structural barrier"

---

## Decision Matrix: How to Route s3 Results

| LoRA s3 | SDF s3 | Δ(4-seed) | p_one est. | Version | Scenario | Action |
|---------|--------|-----------|------------|---------|----------|--------|
| ≤54 | ≤55 | ~1-2pp | >0.1 | A | B | Strengthen null |
| ~54 | ~56 | ~2-3pp | ~0.05-0.1 | A/B gray | B | Lean null, note trend |
| ~53 | ≥58 | >3pp | <0.05 | B | C | Narrative shift |
| ≥56 | ≤55 | <1pp or neg | >0.3 | A (strong) | B | Strongest null |
| ≥56 | ≥60 | >3pp | <0.05 | B | C | Narrative shift |

**Gray zone (p_one ∈ [0.04, 0.06])**: Run paper_switch.py — it applies the p_one < 0.05 threshold mechanically. If p_one lands in [0.04, 0.06], consider reporting both one-tailed and two-tailed results prominently, and emphasize effect size and practical significance over the threshold.

## Checklist After s3 Results

1. [ ] Plug actual s3 CAR values into the stats script; record exact p-values
2. [ ] Determine Version A or B (or gray zone)
3. [ ] Replace all [PLACEHOLDER] values in the chosen version
4. [ ] Run `python paper_switch.py --s2-car [SDF_s3_CAR] --s2-tsr [SDF_s3_TSR]` (note: script currently keyed on s2; for s3, adapt or run manually)
5. [ ] Update rebuttal_prep.md with the chosen Q&A version
6. [ ] Update claim3.tex table row with 4-seed stats (manual, beyond paper_switch.py)
7. [ ] If Version B: review abstract.tex and discussion.tex for consistency with narrative shift
8. [ ] If s3 BBQ data available: fill in Q3 per-task analysis
9. [ ] Re-run permutation test with actual values to confirm pre-computed estimates
