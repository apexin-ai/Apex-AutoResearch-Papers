# Narrative Audit: 13 Negative Experiments vs 7 Successes — Framing Check

> Date: 2026-05-16
> Paper framing: **B — Diagnostic paper (CIVO identification + SGS as informative negative)**
> Core story: trained dt_embedding + multi-rate data → CIVO → stochastic collapse

---

## 1. Experiment Role Classification

### 1.1 Successful Experiments (7)

| Exp ID | Role in Story | What It Establishes |
|--------|--------------|---------------------|
| exp_001 (baseline) | Reference anchor | Healthy v/e dynamics at dt=1; calibration standard for NVE |
| exp_008a (unexposed emb) | Causal control for F3 | Trained embedding without multi-rate exposure does NOT trigger CIVO → multi-rate data is a necessary co-factor |
| exp_008e_v3_s1 | Partial mitigation / F6 setup | dt=1 imagination CAN prevent CIVO in some seeds → but only partial (setup for s2 failure) |
| exp_008f (no dt_emb) | **Core causal ablation** for F2 | Removing dt_embedding eliminates CIVO entirely (NVE ≤1.02x) → dt_emb is causally necessary |
| exp_009a (baseline s2) | Seed fragility control | Baseline stable at seed 2 → 008e_v3_s2 collapse is config-caused, not seed-caused |
| RSSM fidelity analysis | Mechanism evidence | 2.78x reward gap quantifies the asymmetric fidelity that enables critic exploitation |
| exp_008e_v3 (original s0) | Same as s1 above | Additional seed confirming dt=1 imag health |

### 1.2 Negative Experiments — Narrative Roles

| # | Exp ID | Conclusion | Narrative Role | Alternative Hypothesis Excluded | Currently in Paper? |
|---|--------|-----------|----------------|-------------------------------|-------------------|
| 1 | exp_005 (learned gate) | negative | F1: Universal failure | "Learned gating could adaptively avoid bad dt" — NO, gate collapses too | ✅ results.tex F1 |
| 2 | exp_006 (fixed dt=2) | negative | F1 + F4: Quantifies dt magnitude effect | "Gate learning mechanism is the problem" — NO, fixed dt also fails | ✅ results.tex F1, F4 |
| 3 | exp_007 (fixed dt=4) | negative | F1 + F4: Monotonic degradation | "dt=2 is a special case" — NO, dt=4 is worse (monotonic) | ✅ results.tex F1, F4 |
| 4 | exp_008c (unexposed, H=8) | negative | F3/F5: Horizon effect | "H=15 compounding error causes failure in 008a" — PARTIALLY (008c worse than 008a) | ✅ results.tex F3 (brief) |
| 5 | exp_008d (trained emb, sub ON) | negative | **F2: Core CIVO demonstration** | N/A — this IS the disease, not exclusion | ✅ results.tex F2 (primary) |
| 6 | exp_008e_v3_s2 | negative | **F6: Pathway B discovery** | "dt=1 imagination is a complete fix" — NO, non-CIVO pathway exists | ✅ results.tex F6 |
| 7 | exp_009b (008d s2) | negative (transient) | F2: Stochastic outcomes | "CIVO always causes full collapse" — NO, self-correction possible | ✅ results.tex F2 (Table 3) |
| 8 | exp_009c (008f s2) | negative (declining) | F5: Cross-seed variance control | "008f is always healthy" — NO, variance exists but NVE stays <1.5x → NOT CIVO | ✅ results.tex F5 (brief) |
| 9 | exp_009e (008d s1 extended) | negative (oscillatory) | F2: Third outcome mode | "Post-CIVO is binary (collapse or not)" — NO, oscillatory regime exists | ✅ results.tex F2 (Table 3) |
| 10 | exp_015b (frozen dt_emb) | negative (grad starvation) | F3: Trainability is necessary | "dt_emb presence (not training) causes CIVO" — NO, frozen emb never triggers CIVO | ✅ results.tex F3 |
| 11 | **exp_016e (SGS/reward detach)** | negative (no-op) | **Gradient decomposition finding** | "Reward head gradient drives dt_emb → stop it to fix CIVO" — NO, reward gradient = 0 by architecture | ❌ **NOT IN RESULTS/ANALYSIS** |
| 12 | exp_016a-d (SGS retries) | failed (technical) | Implementation iterations | N/A — technical failures leading to 016e | ❌ Not needed in paper |
| 13 | exp_017 (subsample OFF + trained) | killed (duplicate) | Cancelled — identical to 008a | N/A — design error, 008a already covers this cell | ❌ Correctly excluded |

### 1.3 Pending/Queued Experiments (not in current narrative)

| Exp ID | Intended Role | Status |
|--------|--------------|--------|
| exp_018 (Full-SGS) | Test obs-decoder gradient pathway | QUEUED — would validate gradient decomposition |
| exp_010a (Cheetah baseline) | Cross-environment generalization | RUNNING |
| exp_019a/b (PickCube) | Cross-task generalization | QUEUED |

---

## 2. Narrative Coherence Assessment

### 2.1 Current Story Arc (as written in tex files)

```
F1: All dt>1 configs fail
  → "Why?" motivates factorial
F2: Trained dt_emb = causal factor (008d vs 008f)
  → NVE ≥ 1.5x diagnostic, 7/8 accuracy
  → Stochastic outcomes (3 post-CIVO modes)
F3: Unexposed/frozen embedding = safe
  → Dual necessary condition: trained + multi-rate exposure
F4: Degradation ∝ dt magnitude
F5: Horizon/subsample secondary
F6: dt=1 imagination ≠ complete fix
  → Pathway B (non-CIVO, entropy-increasing)
  → Trained dt_emb creates multiple vulnerability channels
```

**Verdict:** The arc from F1→F6 is logically coherent and well-structured as a causal diagnostic. The analysis section correctly synthesizes the mechanism (RSSM fidelity → critic exploitation → actor feedback loop) and contrasts with TAWM (MPC immunity).

### 2.2 Missing Narrative Links

#### GAP 1 (P0): 016e / Gradient Decomposition — NOT IN PAPER

**What's missing:** The gradient decomposition finding (obs decoders 93%, KL 7%, reward 0%) and 016e's no-op result are the **strongest evidence for understanding WHY the causal mechanism works** — but they appear NOWHERE in results.tex or analysis.tex.

**Impact on story:**
- Without this, the paper shows dt_emb causes CIVO but doesn't explain *through which gradient pathway*
- The conclusion mentions "gradient stopping" as future work — but 016e already shows reward-only SGS is a no-op!
- This creates an internal contradiction: the factorial table (methodology.tex line 55-56) lists 016e and 018, but results never discuss them

**Narrative role of 016e:** It should be **Finding 7** — "The reward pathway is an architectural null: gradient decomposition reveals that 93% of dt_emb gradients flow through observation decoders, making reward-only stop-gradient (016e) a no-op. This redirects future intervention to the obs decoder pathway (018)."

**Alternative hypothesis excluded:** "Reward head gradient to dt_emb is the CIVO driver, so blocking it (SGS) should prevent CIVO."

#### GAP 2 (P1): Conclusion's "gradient stopping" suggestion conflicts with 016e

**Current conclusion.tex line 20:** "regularization of the dt-embedding (e.g., gradient stopping or spectral normalization) could potentially preserve the temporal signal while preventing co-adaptation with the reward head"

**Problem:** This implies SGS is untested future work. But 016e already tested reward-only SGS and proved it's a no-op. The conclusion should:
1. State that reward-pathway SGS is empirically confirmed as a no-op (016e)
2. Redirect to full-SGS (018, obs decoder pathway) as the correct gradient-level intervention
3. Frame 018 (queued) as the open question, not generic "gradient stopping"

#### GAP 3 (P1): 015b's gradient starvation mechanism underdeveloped

**Current treatment:** F3 mentions 015b's "gradient starvation (actor loss → 0)" in one sentence. The analysis section doesn't discuss WHY frozen embedding causes gradient starvation or what this tells us about the role of dt_emb gradients in the broader training loop.

**Narrative opportunity:** 015b's gradient starvation + 016e's no-op together paint a picture: dt_emb gradients are overwhelmingly from obs decoders. Freezing dt_emb removes ALL these gradients (starvation). Detaching only reward gradients removes 0% (no-op). This triangulation is currently invisible in the paper.

#### GAP 4 (P2): 009c's narrative role is vague

**Current:** F5 mentions 009c briefly as cross-seed variance. But 009c (008f seed 2, NVE=1.14x, eval declining to 148) is important because it shows that removing dt_emb doesn't guarantee good performance — it just eliminates CIVO specifically. The paper could be clearer that 008f/009c's low performance has a different cause (degraded reward prediction quality: 0.7469 MAE) than 008d's collapse.

---

## 3. Alternative Hypotheses — Coverage Check

| Alternative Hypothesis | Excluded By | In Paper? | Clarity |
|----------------------|-------------|-----------|---------|
| "Learned gating mechanism is the problem" | 006 (fixed dt=2 also fails) | ✅ F1 | Clear |
| "Only large dt fails (dt=2 might be fine)" | 006 fails at dt=2 | ✅ F1, F4 | Clear |
| "dt_emb architecture alone causes CIVO" | 008a (trained but unexposed = healthy) | ✅ F3 | Clear |
| "Multi-rate data alone causes CIVO" | 008f (no emb + sub ON = healthy) | ✅ F2 | Clear |
| "dt_emb presence (not trainability) is sufficient" | 015b (frozen = no CIVO) | ✅ F3 | Clear |
| "CIVO always leads to full collapse" | 009b (transient, self-corrects) | ✅ F2 | Clear |
| "dt=1 imagination fully prevents collapse" | 008e_v3_s2 (collapses anyway) | ✅ F6 | Clear |
| "008e_v3_s2 collapse is seed fragility" | 009a (baseline s2 stable) | ✅ F6 | Clear |
| "Reward head gradient drives dt_emb training → block it to fix CIVO" | 016e (no-op, reward grad = 0) | ❌ **NOT IN PAPER** | **MISSING** |
| "dt-conditioning is inherently broken (not architecture-specific)" | TAWM contrast (succeeds in MPC) | ✅ Analysis §5.3 | Clear |
| "Compounding error alone explains failure" | 008c vs 008a (horizon matters, but 008a still works at H=15) | ✅ F3/F5 | Moderate |
| "All dt_emb configurations have same failure mode" | 008e_v3_s2 Pathway B ≠ 008d Pathway A | ✅ F6 | Clear |

**One critical hypothesis is NOT excluded in the paper text:** the reward-pathway hypothesis (016e). This is the single biggest narrative gap.

---

## 4. Narrative Weak Points — Prioritized

### Critical (blocks Framing B coherence)

1. **016e results absent from paper** — The gradient decomposition is a defining contribution of Framing B. Without it, the paper identifies WHAT causes CIVO (trained dt_emb + multi-rate data) but cannot explain THROUGH WHICH PATHWAY dt_emb's training drives the problem. The causal story stops one level short.

2. **Conclusion contradicts known results** — Suggesting "gradient stopping" as future work when 016e already proves reward-only SGS is a no-op is internally inconsistent. A reviewer would immediately ask "did you try it?"

### Important (strengthens narrative)

3. **015b + 016e triangulation not synthesized** — These two experiments together prove: (a) dt_emb gradients are overwhelmingly from obs decoders, (b) removing all gradients (freeze) → starvation, (c) removing reward-only gradients → no-op. This triangulation is powerful but invisible.

4. **No explicit "failed mitigation" subsection** — Framing B positions negative results as diagnostic evidence, but the paper currently lacks a section that frames 016e's failure as informative (analogous to how F6 frames 008e_v3_s2's failure).

### Minor (polish)

5. **methodology.tex lists 016e and 018 in factorial table but results never discuss them** — creates expectation violation for readers.

6. **009c's distinct failure mode (low absolute reward prediction) vs 008d's CIVO** — could be more explicit about why NVE < 1.5x + low eval ≠ CIVO.

---

## 5. Recommendations

### R1: Add F7 (Gradient Decomposition) to results.tex

Content:
- 016e result: collapse at 95K (NVE=10.42x), indistinguishable from 008d stochastic variation
- Gradient analysis: obs decoders 93% (1.505), KL 7% (0.119), reward 0% (0.000)
- Interpretation: reward-only SGS is architectural no-op
- Implication: obs decoder pathway is the actual gradient channel for dt_emb training

### R2: Add gradient decomposition discussion to analysis.tex

After §5.4 "The dt-Embedding Dilemma":
- New subsection: "Gradient Anatomy of the Temporal Embedding"
- Explain WHY obs decoders dominate: dt_emb conditions RSSM state → state predicts observations → obs reconstruction loss backpropagates through dt_emb
- Explain WHY reward = 0: reward head is small relative to obs heads; or reward prediction is too easy
- Connect to 015b: freezing removes obs decoder gradients → gradient starvation
- Frame 018 (full-SGS) as the principled next test

### R3: Update conclusion.tex

Replace "gradient stopping or spectral normalization" with:
- "Reward-pathway stop-gradient is empirically confirmed as a no-op (016e); gradient decomposition shows that observation decoders provide 93% of dt_emb's training signal. Full stop-gradient (018, detaching all non-KL gradients) targets the correct pathway and is pending evaluation."

### R4: Synthesize 015b + 016e as complementary gradient evidence

In F3 or the new F7, explicitly state:
- 015b (freeze all → starvation, NVE safe) + 016e (block reward only → no-op, NVE pathological) = the gradient source is obs decoders, not reward
- This convergent evidence from two independent experiments strengthens the conclusion

---

## 6. Summary Assessment

| Dimension | Score | Notes |
|-----------|-------|-------|
| Causal chain coherence (F1→F6) | 9/10 | Excellent logical flow from discovery to diagnosis |
| Alternative hypothesis coverage | 8/10 | One critical hypothesis (reward pathway) not excluded in paper |
| Negative results framing | 7/10 | Most negatives well-framed as diagnostic evidence; 016e completely missing |
| Internal consistency | 6/10 | Conclusion contradicts available evidence; factorial table promises results not delivered |
| Story completeness for Framing B | 7/10 | Missing the gradient decomposition that defines Framing B's unique contribution |

**Bottom line:** The paper's F1-F6 structure is strong and the narrative is coherent — each negative result clearly serves a diagnostic purpose. The single critical gap is the **absence of 016e and gradient decomposition** from the written paper. This is not a minor omission — Framing B's reaudit document identifies it as the defining P0 contribution that distinguishes this paper from a generic "we tried X and it failed" story. Adding F7 (gradient decomposition) and R2-R4 would close the narrative loop and make the diagnostic argument complete.
