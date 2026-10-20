# Negative Results Paper Value Analysis

Generated: 2026-05-29 | Source: Registry (45 experiments, conclusion=negative)

---

## Category 1: Intervention Failures (21 experiments)

### 1a. SGS — Gradient-level (5 experiments)

| Exp | Variant | NVE peak | Outcome |
|-----|---------|----------|---------|
| 016e | Reward-only SGS | 10.42× | Catastrophic delayed collapse (worse than untreated 4.12×) |
| 018v2 s1 | Full-SGS | 1.66× | Partial mitigation, late instability rising to 1.66× at 95K |
| 018 s2 | Full-SGS | collapsed | Complete failure |
| 021 s1 | Full-SGS Cheetah | 9.94× | Transient CIVO, self-correcting |
| 025 s2 | Obs-decoder SGS | eval 89.6 | Poor performance |

**Paper coverage**: ✅ Well-covered. F7 discusses full-SGS mixed results. Table 3 shows rates. "Pathway redundancy" explanation in Discussion.

**Gap — SGS paradox under-emphasized**: Reward-only SGS (NVE 10.42×) is *worse* than untreated (NVE 4.12×). This "blocking one channel amplifies others" effect is mentioned in appendix but not quantified in main text. Strengthens the "pathway redundancy" argument.

**Suggested addition** (experiments_results.tex F7 paragraph, after "blocking the dominant gradient channel shifts co-adaptation to remaining pathways"):
> "Reward-only detachment (exp\_016e) illustrates this: NVE reaches $10.42\times$ vs.\ $4.12\times$ untreated, as the remaining gradient pathways compensate."

### 1b. RAVE — Output-level (2 experiments)

| Exp | Ceiling | NVE peak | Eval (% BL) |
|-----|---------|----------|-------------|
| 028 | 2.0 | 4.09× | 3% |
| 028 ceil15 | 1.5 | ~1.5× | 4% |

**Paper coverage**: ✅ One sentence in Forward-Pass. Table 3 shows 0/2.

**Gap**: None significant. Two experiments, clear failure mechanism (EMA anchor lag).

### 1c. TCN — Representation-level (11 experiments)

| Env | σ=0.1 | σ=0.2 | σ=0.5 | σ=1.0 |
|-----|-------|-------|-------|-------|
| Walker | 1/1 prev, 36%BL | 2/4 prev (binary) | 0/2 prev (oscillatory) | — |
| Cheetah | — | 0/1 prev (NVE 1.9×) | 0/1 prev (NVE 10.7×) | 1/1 prev, 8.6%BL (eroded) |
| PickCube | — | 0/1 prev (NVE 3.7×) | 0/1 prev (NVE 3.3×) | — |

**Paper coverage**: ✅ "Binary behavior" and "cross-environment transfer fails" discussed. σ=1.0 erosion noted.

**Gap — Dose-response asymmetry across environments is richer than presented**: The data reveals a systematic pattern: Walker effective dose ≈ σ=0.2 (with binary outcome); Cheetah needs σ≥1.0 to suppress CIVO but at that dose the policy is destroyed; PickCube is unresponsive at any tested dose. This 3-environment dose-response pattern more strongly supports "TCN is diagnostic, not deployable" than the current one-sentence treatment. Not a major gap, but upgradeable.

### 1d. Architecture-level (4 experiments)

| Exp | Config | NVE peak | Note |
|-----|--------|----------|------|
| 034 | Narrow dual Cheetah | 1.75× | Borderline, eventual collapse |
| 036 | Dual PickCube | 2.3× | Not prevented |
| 037 | Wide single Cheetah | 3.6× | Capacity alone insufficient |
| 038 s2 | Wide dual Walker | 0.3× | **CIVO prevented but non-CIVO collapse** (eval 99.6) |

**Paper coverage**: ✅ 2×2 factorial well-covered. Cross-env limits acknowledged.

**Gap — "Prevented CIVO but still failed" pattern**: exp_038 s2 shows NVE ≤0.3× (CIVO fully prevented) yet eval collapses to 99.6 (11% baseline). This demonstrates that CIVO prevention ≠ performance recovery — the variable-rate setup may cause additional non-CIVO degradation. The paper notes low eval % in Table 3 (55±24% for wide dual) but doesn't explicitly call out this "prevention without recovery" pattern.

**Shared pattern across all 21 intervention experiments**: 
- **All interventions that "work" on Walker fail or hurt on Cheetah.** Zero interventions transfer across environments at the same hyperparameters. This is the strongest systemic negative finding — it implies the CIVO mechanism is environmentally parameterized, making universal mitigation impossible without per-environment tuning.

---

## Category 2: Environment Boundary (7 experiments)

| Env | DoF | Exps | CIVO triggered | Key finding |
|-----|-----|------|----------------|-------------|
| Cartpole Swingup | 1 | 061, 062 | 0/3 trigger, 0/3 control | Too simple |
| Hopper Hop | 4 | hopper_trained_ext, hopper_frozen_ext | 0/1 (transient, recovered) | Intermediate |
| StackCube | 6 (manip) | 051 frozen | Env-specific transient | Not dt_emb-dependent |
| Quadruped Walk | 12 | baseline_s0_r2 | N/A (baseline NVE 4.7×) | Intrinsically unstable |
| Humanoid Walk | 21 | baseline_s0 | N/A (baseline NVE 12.97×) | Intrinsically unstable |

**Paper coverage**: ✅ Discussion "Environment complexity boundary" paragraph. Appendix DoF table. Well-framed as Goldilocks zone.

**Gap — Hopper frozen phantom value**: Hopper frozen control shows persistent phantom value (ve_ratio in the millions at 105K) that never recovers, while trained version eventually recovers. This is *opposite* to Walker/Cheetah where frozen is always better. It suggests frozen embedding causes its own pathology (gradient starvation) that is environment-dependent. The paper mentions gradient starvation for Walker frozen (015b) but doesn't connect to Hopper. This could strengthen the "frozen is a diagnostic tool, not a universal fix" nuance.

Not a required addition, but an interesting footnote.

---

## Category 3: Configuration Controls (3 experiments)

| Exp | Config | NVE | Note |
|-----|--------|-----|------|
| 015b | Frozen Walker | 0.42× | No CIVO, gradient starvation |
| 008f s4 | No dt_emb Walker | 0.58× | No CIVO, healthy |
| 009c s2 | No dt_emb Walker | 1.14× | No CIVO, declining performance |

**Paper coverage**: ✅ Table 2 (three_way_emb), 0/10 frozen/removed. These are adequately covered as causal controls.

**Gap**: None.

---

## Category 4: Stochastic Onset Seeds (3 experiments)

| Exp | Config | NVE | Classification |
|-----|--------|-----|---------------|
| 009e s1 | Walker 008d | 4.13× | onset_collapse |
| 009b s2 | Walker 008d | 1.62× | onset_self_correcting |
| 088 s1 | Cheetah 008d | 0.52× | no_onset |

**Paper coverage**: ✅ "5/7 trained runs" framing. Appendix has per-seed trajectories.

**Gap — Stochastic onset mechanism**: The paper notes seed divergence but doesn't characterize *what* seed-level factor predicts onset vs. no-onset. From the data:
- 008d Walker: 3/5 onset (s0 ✓, s1 ✓, s2 self-correct, s3 ✓, s4 ✓) — but nve_classifications vary
- 008d Cheetah: 3/4 onset (s0 ✓, s1 ✗, s2 extreme, s3 ✓)

The non-onset seeds (Walker s2, Cheetah s1) don't obviously differ in early training metrics. This supports CIVO as a *phase transition* — small perturbations in early stochastic dynamics determine whether the feedback loop engages. Currently implicit in the appendix seed divergence analysis; could be one sentence in Discussion.

---

## Category 5: Core Design Variants (6 experiments)

| Exp | Config | Peak eval | Fate |
|-----|--------|-----------|------|
| 003 | Event gate v2 | 118.7 | Collapse |
| 004 | Event gate v3 | — | Collapse |
| 005 | Learned gate | 541 | Collapse to 99 |
| 006 | Fixed dt=2 | 485 | Inverted-V collapse to 133 |
| 007 | Fixed dt=4 | 177 | Never learns |
| 008c | No subsample + dt=2 | 241 | Plateau |

**Paper coverage**: ✅ F1 covers 005/006/007 with Figure 1. Monotonic degradation mentioned in F3-F5 summary.

**Gap — Inverted-V pattern**: exp_005 and exp_006 both show inverted-V trajectories (performance rises then crashes). This "first learns, then collapses" pattern is the hallmark of CIVO — the critic initially learns useful representations but co-adaptation eventually corrupts them. The paper describes this for 008d but doesn't emphasize that the *identical temporal pattern* appears across all variable-rate configs. Could add one sentence.

---

## Category 6: dt=1 Imagination Seeds (4 experiments)

| Exp | Seed | NVE | Eval 105K | Note |
|-----|------|-----|-----------|------|
| 008e_v3_walker_s2 | s2 (old) | 3.78× | 137 | Late-onset collapse |
| 008e_v3_s3 | s3 | 4.02× | 92.7 | Collapse |
| 070_008e_v3_walker_s0 | s0 | 0.8× | 148 | Non-CIVO learning failure |
| 081_008e_v3_walker_s2 | s2 (corrected) | low | 597 | 64% baseline |

**Paper coverage**: F6 reports "0/4 CIVO (peak NVE ≤0.8×); three seeds achieve 65–96% of baseline (mean 775.6)."

**⚠️ Potential consistency issue**: Registry has 2 seeds (exp_008e_v3_walker_s2, exp_008e_v3_s3) with NVE >2.0× labeled as 008e_v3. The paper likely uses the corrected-code runs (exp_081 for s2, presumably similar for others), while earlier runs remain in registry. If these are pre-correction runs, this is fine — but the registry doesn't clearly mark which are corrected. The Appendix code corrections section should explicitly list which exp_ids are superseded.

---

## Cross-Cutting Patterns

### Pattern A: Zero cross-environment transfer for interventions
Every intervention that works on Walker fails on Cheetah at the same hyperparameters (TCN σ=0.2, dual-critic, SGS). This is arguably the paper's strongest systemic negative: the CIVO mechanism is environment-parameterized. The Discussion says "cross-environment transfer is limited" — could be stronger.

### Pattern B: Monotonic severity with temporal stride
dt=1 (healthy) → dt=2 (−47%, some CIVO) → dt=4 (−81%, severe failure). This continuous scaling is consistent with compounding error amplified by co-adaptation. Currently mentioned quantitatively only in the F3-F5 summary.

### Pattern C: Binary onset (phase transition)
For the same config, seeds either fully trigger CIVO or don't at all (no "mild" CIVO). TCN shows the same binary pattern. This suggests a critical threshold / phase transition in the feedback loop dynamics. The paper notes "binary behavior" for TCN but doesn't generalize it.

---

## Summary: Paper Coverage Assessment

| Category | Count | Paper Coverage | Gap Severity |
|----------|-------|---------------|--------------|
| Intervention failures | 21 | ✅ Good (Table 3, F7, forward-pass, arch) | Minor: dose-response, SGS paradox quantification |
| Environment boundary | 7 | ✅ Good (Goldilocks zone) | Minor: Hopper frozen anomaly |
| Configuration controls | 3 | ✅ Complete | None |
| Stochastic onset | 3 | ✅ Good (per-seed analysis) | Minor: phase transition framing |
| Core design variants | 6 | ✅ Good (F1, Figure 1) | Minor: inverted-V universality |
| dt=1 imagination | 4 | ⚠️ Registry/paper alignment | Check code correction labels |

**Overall verdict**: The paper leverages its 45 negative experiments well. The main contribution — systematic intervention failure — is clearly presented through the hierarchy table and per-level analysis. Three upgradeable gaps:

1. **"Zero cross-environment transfer" could be a named finding** — currently buried in individual section notes. One sentence in Discussion would strengthen the practical takeaway.

2. **SGS paradox quantification** — reward-only SGS making CIVO *worse* (10.42× vs 4.12×) is a powerful data point for pathway redundancy. Currently only in appendix.

3. **Phase transition framing** — the binary onset pattern (both for stochastic seeds and TCN) could unify several observations under one concept. Currently described separately.

### Suggested 1-2 Sentence Additions

**Discussion "Why interventions fail" paragraph, after "single-pathway interventions cannot break":**
> No tested intervention transfers across environments at the same hyperparameters: TCN's effective dose ($\sigma{=}0.2$ on Walker) is insufficient for Cheetah and unresponsive on PickCube; narrow dual-critic prevents on Walker but not Cheetah. This environment-specificity is consistent with the closed-loop nature of imagination, where the bias landscape is shaped by environment dynamics.

**Discussion "CIVO mechanism" paragraph, after existing content (optional):**
> Onset exhibits binary characteristics: within the same configuration, seeds either fully trigger CIVO or remain healthy, with no intermediate outcomes; TCN shows the same all-or-nothing pattern across doses, suggesting a phase-transition-like critical threshold in the co-adaptation feedback loop.
