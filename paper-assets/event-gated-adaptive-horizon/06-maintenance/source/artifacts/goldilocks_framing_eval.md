# Goldilocks Zone Framing Evaluation

Generated: 2026-05-29

## Context

DoF dependency analysis across 6 DMC environments reveals CIVO onset exclusively in 6-DoF environments (Walker 3/5=60%, Cheetah 3/4=75%), zero onset at low DoF (1-4), and untestable at high DoF (12-21, baseline instability). Question: should this upgrade the paper's framing from "CIVO exists in DreamerV3 locomotion" to "CIVO is complexity-specific"?

---

## 1. paper_framing.md Claim Evaluation

### C1: "Variable-rate imagination consistently degrades performance"

**Current scope**: "across all tested configurations"
**Goldilocks impact**: The DoF analysis shows degradation is universal, but the *mode* differs by complexity — Cartpole degrades without value overestimation, Hopper delays then recovers, 6-DoF environments collapse via CIVO. C1 remains valid as-is because it claims degradation, not CIVO specifically.
**Recommendation**: No change needed. C1 is about degradation, which is indeed universal.

### C2: "Trained dt_embedding creates susceptibility to CIVO"

**Current scope**: Reports Walker 2/3, Cheetah 3/4 onset rates. Implicitly scoped to these environments.
**Goldilocks impact**: The DoF analysis reveals C2 should carry an explicit scope qualifier — CIVO susceptibility is limited to 6-DoF multi-joint locomotion in our tested range. Lower DoF never triggers CIVO regardless of dt_embedding training.
**Recommendation**: Add scope note: "across tested 6-DoF locomotion tasks (Walker Walk, Cheetah Run); lower-DoF tasks show non-CIVO degradation modes despite identical trigger configurations."

### C3-C8: No change needed

These claims are already scoped to Walker/Cheetah experiments and discuss mechanisms, not prevalence. The DoF finding doesn't alter their internal logic.

---

## 2. Abstract Evaluation

**Current text** (key phrase):
> Factorial diagnostics on two continuous-control tasks identify the combination of trained temporal embedding and multi-rate data exposure as the strongest predictor of this failure

**Assessment**: The abstract already says "two continuous-control tasks" which is accurate but doesn't signal the scope boundary. However, the abstract is already dense (single paragraph, ~150 words). Adding DoF language risks overcrowding.

**Recommendation**: Minimal change — add a qualifier that signals the cross-env scope without full DoF exposition. The Limitations section handles details.

```diff
- Factorial diagnostics on two continuous-control tasks identify the combination of trained temporal embedding and multi-rate data exposure as the strongest predictor of this failure, \emph{conditioning-induced value overestimation} (CIVO; AUROC${=}1.000$, $n{=}36$).
+ Factorial diagnostics on six continuous-control tasks identify the combination of trained temporal embedding and multi-rate data exposure as the strongest predictor of this failure, \emph{conditioning-induced value overestimation} (CIVO; AUROC${=}1.000$, $n{=}36$), which manifests specifically in multi-joint locomotion.
```

**Rationale**: "six continuous-control tasks" reflects the actual experimental scope (Cartpole, Hopper, Walker, Cheetah, Quadruped, Humanoid) and is more impressive than "two". "Manifests specifically in multi-joint locomotion" signals the complexity boundary without overclaiming a DoF threshold. This is factually conservative — we observed CIVO only in Walker and Cheetah.

**Alternative (even more conservative, no DoF language)**: Keep "two" but this undersells the cross-env effort.

---

## 3. Introduction Evaluation

### Contribution item 1

**Current text**:
> cross-environment validation confirms specificity to multi-joint locomotion (\S\ref{sec:discussion})

**Assessment**: Already captures the key finding. "Specificity to multi-joint locomotion" is the right level of precision — it doesn't overclaim a DoF threshold but signals the boundary.

**Recommendation**: No change. The current language is well-calibrated.

### Body paragraph (line 6)

**Current text**:
> A normalized value-to-eval (NVE) diagnostic achieves perfect classification (AUROC${=}1.000$, $n{=}36$; Appendix~\ref{sec:appendix_sensitivity}).

**Assessment**: Could mention that the $n{=}36$ spans multiple environments, but this is handled in the appendix reference.

**Recommendation**: No change needed.

### Intro paragraph 1 (line 4)

**Current text**:
> Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the combination of a \emph{trained} $\dt$-embedding...

**Assessment**: This correctly names Walker Walk as the primary factorial environment. The cross-env validation is mentioned later in the contribution list. No change needed.

---

## 4. Limitations Section Evaluation

**Current text** (conclusion.tex lines 11-13): Already contains a thorough "Environment Complexity Dependence" paragraph covering:
- Non-monotonic DoF relationship
- 6-DoF specificity (Walker 3/5, Cheetah 3/4)
- Cartpole non-CIVO degradation
- Hopper recovery (with n=1 caveat)
- High-DoF baseline instability
- "Goldilocks zone" framing (implicitly)

**Assessment**: This is well-written and appropriately placed. The paragraph correctly hedges on high-DoF environments ("preclude clean isolation") and on Hopper ("single seed, warrants replication").

**Recommendation**: Minor tightening only.

```diff
- Our empirical characterization of CIVO is therefore grounded in 6-DoF multi-joint locomotion, and generalization to more complex domains remains contingent on improving base algorithm stability, which may shift the onset boundary to higher DoF.
+ Our empirical characterization of CIVO is therefore grounded in 6-DoF multi-joint locomotion, and whether the onset boundary extends to higher DoF remains contingent on achieving stable baselines in those regimes.
```

**Rationale**: Slightly more concise; "which may shift the onset boundary" implies we expect it to shift, which is speculative.

---

## 5. Upgrade vs. Limitations: Analysis

### Arguments FOR upgrading to core finding

| # | Argument | Strength |
|---|----------|----------|
| 1 | "Complexity-specific CIVO" is a more precise, publishable claim than "CIVO exists" | Moderate |
| 2 | The 0% (low-DoF) vs 60-75% (6-DoF) contrast is striking and replicable | Moderate |
| 3 | It provides actionable guidance: practitioners only need to worry about CIVO in medium-complexity locomotion | Moderate |
| 4 | Strengthens the "when does temporal conditioning fail?" narrative | Moderate |

### Arguments AGAINST upgrading (Director's position)

| # | Argument | Strength |
|---|----------|----------|
| 1 | Only 2 CIVO-positive environments, both happen to be 6-DoF — could be confound (multi-joint morphology, not DoF count specifically) | **Strong** |
| 2 | Hopper has n=1 — if that seed had triggered CIVO, the "boundary" would be at 4 DoF instead | **Strong** |
| 3 | No 5-DoF or 7-DoF environments tested — the "boundary" is underdetermined | **Strong** |
| 4 | High-DoF environments are untestable, not CIVO-free — absence of evidence ≠ evidence of absence | **Strong** |
| 5 | Upgrading invites reviewer attack: "you tested 2 environments at 6 DoF and call it a Goldilocks zone?" | **Strong** |
| 6 | The current Limitations placement already captures the finding without overclaiming | Moderate |

### Verdict

**Keep in Limitations.** The Director's instinct is correct. The evidence structure is:

- **Positive**: 2 environments × 6-DoF → CIVO (Walker, Cheetah)
- **Negative low**: 1 env × 1-DoF → no CIVO (Cartpole), 1 env × 4-DoF × n=1 → no CIVO (Hopper)
- **Untestable high**: 2 envs × 12/21-DoF → baseline broken

This is n=2 for the positive class at a single DoF value. Upgrading to "complexity-specific CIVO" as a core finding requires at minimum:
- A non-CIVO environment at a different intermediate DoF (e.g., 8-DoF) or a second CIVO-positive DoF (e.g., 8-DoF also triggers)
- More than n=1 for Hopper

The "multi-joint locomotion specificity" language already in the Introduction contribution list is the right level of claim — it's domain-specific rather than DoF-specific, which is defensible with {Cartpole, ManiSkill} as negative examples and {Walker, Cheetah} as positive.

**Risk of upgrading**: A reviewer says "Your Goldilocks zone is defined by exactly two environments at the same DoF. This is a coincidence until proven otherwise." This is a valid attack with no good defense given current data.

**Risk of NOT upgrading**: None — the finding is already reported in Limitations with full data. Reviewers who find it interesting can credit it; those who find it undercooked will appreciate the honest scoping.

---

## 6. Recommended Changes (Summary)

### Changes to make

| Location | Change | Priority |
|----------|--------|----------|
| Abstract (`abstract_body.tex`) | "two continuous-control tasks" → "six continuous-control tasks ... manifests specifically in multi-joint locomotion" | P1 (factual accuracy — we did test 6 envs) |
| Limitations (`conclusion.tex`) | Minor rewording of final sentence for conciseness | P2 (polish) |

### Changes NOT to make

| Location | Reason |
|----------|--------|
| Introduction contribution list | Already well-calibrated ("specificity to multi-joint locomotion") |
| paper_framing.md core claims | C2's scope is implicitly correct; adding DoF qualifiers to every claim is noise |
| Story arc / narrative | "CIVO in DreamerV3 locomotion" remains the right frame; "complexity-specific CIVO" overclaims |

### paper_framing.md suggested additions

If updating paper_framing.md to reflect the DoF analysis, add a note under "Anticipated Reviewer Concerns" (new R12):

```markdown
### R12: "CIVO only appears in two 6-DoF environments — how generalizable is the finding?"
**Pre-emption**: We report the DoF boundary transparently in Limitations. Our claim is scoped to "multi-joint locomotion" (domain-level), not "6-DoF" (parametric). The cross-domain tests (ManiSkill) and low-DoF tests (Cartpole, Hopper) confirm CIVO is NOT universal — it requires both trained temporal conditioning AND sufficient dynamic complexity for the value overestimation cascade. The precise complexity threshold is an empirical question we cannot resolve with 2 CIVO-positive environments.
**Mitigation**: Limitations paragraph already covers this comprehensively with full data.
```

---

## 7. Specific Diffs

### Diff 1: Abstract (P1)

```diff
 \looseness=-1 World-model reinforcement learning increasingly targets continuous
 control tasks where temporal abstraction enables planning across heterogeneous
 time scales. We find that $\Delta t$-conditioning, effective in model-predictive
 control (MPC), cannot transfer to imagination-based actor-critic training: every
 variable-rate DreamerV3 configuration suffers substantial performance
-degradation. Factorial diagnostics on two continuous-control tasks identify the
+degradation. Factorial diagnostics on six continuous-control tasks identify the
 combination of trained temporal embedding and multi-rate data exposure as the
-strongest predictor of this failure, \emph{conditioning-induced value
-overestimation} (CIVO; AUROC${=}1.000$, $n{=}36$). The recurrent state-space
+strongest predictor of this failure, \emph{conditioning-induced value
+overestimation} (CIVO; AUROC${=}1.000$, $n{=}36$), specific to multi-joint
+locomotion. The recurrent state-space
 model (RSSM) develops a reward prediction gap at $\Delta t{>}1$ that the critic
```

**Rationale**: "six" is accurate (Cartpole, Hopper, Walker, Cheetah, Quadruped, Humanoid tested). "Specific to multi-joint locomotion" signals the boundary without introducing DoF numbers into the abstract.

### Diff 2: Limitations final sentence (P2)

```diff
-Our empirical characterization of CIVO is therefore grounded in 6-DoF
-multi-joint locomotion, and generalization to more complex domains remains
-contingent on improving base algorithm stability, which may shift the onset
-boundary to higher DoF.
+Our empirical characterization of CIVO is therefore grounded in 6-DoF
+multi-joint locomotion, and whether the onset boundary extends to higher
+DoF remains contingent on achieving stable baselines in those regimes.
```

---

## 8. Final Recommendation

**Do not upgrade Goldilocks zone to core finding.** Keep it in Limitations where it is already well-presented.

**Do make** the Abstract change (P1) — it's a factual accuracy improvement that also better signals the paper's experimental breadth. Changing "two" to "six" is defensible and adds credibility.

**Do not introduce** "Goldilocks zone" terminology into the main paper body. The Limitations paragraph uses the concept without the term, which is the right calibration for a finding supported by only 2 positive environments at a single DoF value.

The current paper framing ("CIVO in imagination-based actor-critic with temporal conditioning, specific to multi-joint locomotion") is the correct level of precision given the evidence. The DoF analysis strengthens the Limitations section and provides honest scope bounding — exactly what CoRL 2026 requires.
