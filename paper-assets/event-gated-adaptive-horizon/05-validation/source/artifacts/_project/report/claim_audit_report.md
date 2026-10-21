# Claim Language Audit Report

**Purpose:** Ensure all claims align with the empirical evidence: trained dt_emb is a necessary (not sufficient) condition for CIVO; triggering requires subsample ON + dt>1 imagination; collapse probability is environment-dependent.

---

## Findings

### [CRITICAL] results.md line 159 — Factually incorrect necessity claim

**Original:**
> Subsampling and imagination horizon modulate performance levels but are neither necessary nor sufficient for CIVO.

**Problem:** Subsample ON IS necessary for CIVO (exp_008a: trained dt_emb + subsample OFF → no CIVO). Saying it's "neither necessary" contradicts the paper's own factorial data.

**Suggested fix:**
> Subsampling is a necessary co-factor for CIVO but not independently sufficient; imagination horizon modulates performance level without independently triggering overestimation.

---

### [HIGH] method_framingB_reaudit_v2.md line 111 — Overly absolute "not harmful"

**Original:**
> The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\Delta t > 1$ predictions during imagination.

**Problem:** The paper's own IRD finding (exp_008e_v3_s2) shows that the trained embedding CAN cause collapse even at dt=1 imagination through a non-CIVO pathway. "Not harmful" is an unqualified absolute.

**Suggested fix:**
> The trained embedding does not trigger CIVO when imagination is restricted to $\Delta t{=}1$; the pathological overestimation arises specifically when the actor-critic exploits the embedding's $\Delta t > 1$ predictions during imagination.

---

### [HIGH] method_framingB_reaudit_v2.md line 124 — "The necessary condition" implies sole sufficiency

**Original:**
> Trained dt\_embedding is the necessary condition for sustained CIVO (NVE $>$ 1.5$\times$ across consecutive checkpoints).

**Problem:** Using "the necessary condition" (definite article, singular) implies it's the only required factor. Multi-rate data exposure is also required (exp_008a proves this).

**Suggested fix:**
> A trained dt\_embedding is necessary for sustained CIVO (NVE $>$ 1.5$\times$ across consecutive checkpoints), though not independently sufficient---multi-rate training data exposure is jointly required.

---

### [HIGH] method_framingB_reaudit_v2.md line 187 — Repeated "not harmful" absolute

**Original:**
> The trained embedding itself is not harmful; the problem arises only when the actor-critic exploits $\Delta t > 1$ predictions during imagination.

**Problem:** Same as line 111. Contradicted by IRD pathway.

**Suggested fix:**
> The trained embedding does not trigger CIVO when imagination is restricted to $\Delta t{=}1$; the pathological overestimation arises only when the actor-critic exploits $\Delta t > 1$ predictions during imagination.

---

### [MEDIUM] results.md line 196 — "definitively rules out"

**Original:**
> our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result that definitively rules out reward-pathway interventions.

**Problem:** "Definitively" overstates certainty. The measurement is at one checkpoint (95K) in one configuration. While the architectural argument is strong, "definitively" implies mathematical proof.

**Suggested fix:**
> our finding that the reward gradient is not merely small but numerically zero for the temporal embedding is a stronger result, ruling out reward-pathway interventions for this architecture.

---

### [MEDIUM] 018_prewrite_two_versions.md line 53 — "The complete causal mechanism"

**Original (Version A):**
> The complete causal mechanism is: observation decoder gradients train $e_{\Delta t}$...

**Problem:** "Complete" implies no unknown factors. With only 2 seeds on 2 envs, the mechanism may have additional factors not yet observed.

**Suggested fix:**
> The identified causal mechanism is: observation decoder gradients train $e_{\Delta t}$...

---

### [LOW] method_90ca4b.md line 109 — "not harmful" (same pattern)

**Original:**
> The trained embedding itself is not harmful; the problem arises when the actor-critic *exploits* the embedding's $\Delta t > 1$ predictions during imagination.

**Problem:** Same absolute claim as in framingB. This is an older draft version so lower priority.

**Suggested fix:** Same as framingB line 111.

---

### [LOW] results.md line 73 — "reliably induces" in single-env context

**Original:**
> The trained embedding reliably induces pathological value overestimation, though whether this overestimation progresses to catastrophic collapse is stochastic.

**Problem:** "Reliably" based on 2/2 seeds in one environment. The subsequent clause about stochastic collapse is correct, and the NVE evidence supports high trigger probability. Borderline acceptable.

**Suggested fix (optional):**
> The trained embedding triggers pathological value overestimation in all tested seeds (2/2), though whether this overestimation progresses to catastrophic collapse is stochastic.

---

## Summary

| Severity | Count | Files affected |
|----------|-------|----------------|
| CRITICAL | 1 | results.md |
| HIGH | 3 | method_framingB_reaudit_v2.md |
| MEDIUM | 2 | results.md, 018_prewrite_two_versions.md |
| LOW | 2 | method_90ca4b.md, results.md |

**Total: 8 overly strong claims found.**

Key patterns:
1. **Incorrect "neither necessary nor sufficient"** — subsample IS necessary per factorial data (1 instance)
2. **Unqualified "not harmful" absolutes** — contradicted by the paper's own IRD finding (3 instances)
3. **"Definitively"/"complete" certainty language** — overstates evidence from limited seeds/envs (2 instances)
4. **"The necessary condition" (sole)** — implies independent sufficiency (1 instance)

All CRITICAL and HIGH findings are directly edited in results.md and method_framingB_reaudit_v2.md.
