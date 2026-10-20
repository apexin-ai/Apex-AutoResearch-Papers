> **⛔ DEPRECATED — DO NOT USE** (Director 指令 2026-05-16)
> 本文件含 NVE/ve_ratio 混淆错误（6.59x 是 raw ve_ratio，不是 NVE）。
> 权威审计文档：`artifacts/_project/report/framing_b_reaudit.md`（使用正确的 NVE=10.42x）。

# ~~Framing B Re-audit: Section-by-Section Diff Checklist~~ [DEPRECATED]

**Date**: 2026-05-16
**Drivers**: D059 (Framing B approved), D061 (016e reward SGS = no-op)
**Scope**: Integrate SGS informative negative + gradient decomposition finding into paper. No file edits — checklist only.

---

## Key New Facts to Integrate

| Fact | Source | Numbers |
|------|--------|---------|
| 016e reward_dt_emb_detach is architectural no-op | D061, gradient verification (commit 5fc8e49) | reward grad to dt_emb.weight = 0.000 |
| dt_emb gradient decomposition | D061 | obs decoders 93% (1.505), KL dynamics 7% (0.119), reward 0% (0.000) |
| 016e collapsed like 008d | 016e registry | peak eval 326.7@75K → 31.7@95K, NVE=6.59x@95K |
| 016e vs 008d difference = random variation | D061 | onset timing/peak height differ but both collapse; SGS intervention was null |
| Full-SGS (018) removes 93% gradient | D060 | planned experiment, queued |

---

## 1. Abstract

**Current state**: Mentions CIVO, NVE diagnostic (7/8, AUROC=0.933), dual pathways, MPC contrast. No mention of SGS or gradient decomposition.

**Changes needed**:

- [ ] **ADD** one sentence after the dual-pathway finding: gradient decomposition reveals dt_emb receives 93% of its gradient from observation decoders and 0% from reward, making reward-pathway interventions architectural no-ops.
- [ ] **Reframe** "reward head develops 2.78× gap" — keep this (it's still true and drives CIVO), but the new gradient finding adds depth: the reward head exploits dt_emb for differentiation, but dt_emb is trained by obs decoders, not by reward. The exploitation is asymmetric.
- [ ] **Candidate sentence**: "A gradient decomposition of the temporal embedding reveals that 93\% of its training signal originates from observation decoders and 0\% from the reward head, rendering reward-pathway interventions architectural no-ops and identifying observation reconstruction as the primary driver of temporal co-adaptation."

**Constraint**: Abstract is already dense (1 paragraph). May need to compress existing text to fit. Consider dropping the "stochastic downstream outcomes" detail to make room — it's elaborated in intro and results.

---

## 2. Introduction

**Current state**: Three numbered findings: (1) stochastic outcomes, (2) dt=1 doesn't prevent collapse, (3) MPC contrast. No SGS mention.

**Changes needed**:

- [ ] **ADD finding (4)**: Gradient decomposition + SGS no-op as a fourth contribution. Suggested placement: after finding (3), before the closing sentence.
- [ ] **Candidate text**: "(4)~a gradient decomposition of the $\dt$-embedding reveals that 93\% of its training signal comes from observation decoders and 0\% from the reward head---an intervention that detaches reward gradients from the embedding (selective gradient stopping) is confirmed as an architectural no-op, shifting the causal target from reward co-adaptation to observation-driven representation learning."
- [ ] **UPDATE contribution framing**: The contribution list should now explicitly include the gradient decomposition as an independent finding, not just the CIVO diagnostic. This strengthens the "actionable insight for future method design" angle.

---

## 3. Methodology (§3)

### 3.1 Factorial Design Table (Table 1)

**Current state**: 9 configurations listed. No 016e.

**Changes needed**:

- [ ] **ADD row** for 016e in Table 1:
  ```
  016e | SGS (reward detach) | trn* | on | 8 | 2
  ```
  With footnote: `*trained but reward head gradients detached from dt-embedding (reward_dt_emb_detach=True)`
- [ ] **ADD row** for 018 (planned, if results available before submission):
  ```
  018 | Full-SGS (all detach) | trn† | on | 8 | 2
  ```
  With footnote: `†trained but all non-KL head gradients detached from dt-embedding`
- [ ] **Place** these rows in a new section separator "Gradient intervention" below the mitigation row (008e_v3).

### 3.2 New Subsection: Selective Gradient Stopping (SGS)

**Current state**: No description of SGS mechanism.

**Changes needed**:

- [ ] **ADD paragraph** in §3.2 (Variable-Rate Imagination Mechanism) or as new §3.3:
  - Define SGS: detaching specific gradient pathways from dt_emb during backprop
  - Describe 016e variant: `reward_dt_emb_detach=True` — stops reward loss gradient from flowing to dt_emb.weight
  - Describe Full-SGS (018): detaches ALL non-KL head gradients (obs decoders + reward + cont), retaining only KL dynamics → dt_emb
  - Motivation: test whether CIVO is gradient-driven (specific head training dt_emb to exploit) or representation-level (any training of dt_emb creates vulnerability)

### 3.3 Diagnostic Metrics — Gradient Decomposition

**Current state**: NVE, RSSM fidelity, actor loss sign, value std described. No gradient analysis.

**Changes needed**:

- [ ] **ADD paragraph** describing gradient decomposition methodology:
  - `torch.autograd.grad` per-head analysis of dt_emb.weight
  - Decomposition: compute gradient norm from each loss component independently
  - Report: fraction of total gradient norm attributed to each head

---

## 4. Results (§4)

### New Finding: F7 (or renumber existing)

**Current state**: F1–F6. No SGS finding.

**Changes needed**:

- [ ] **ADD §4.7**: "F7: Reward-Pathway Gradient Stopping Is an Architectural No-Op"

**Content for F7**:

```
Experiment 016e applies selective gradient stopping (SGS) to the reward
head, detaching reward-loss gradients from the dt-embedding. If CIVO
were driven by reward-head co-adaptation with the temporal embedding,
this intervention should prevent or delay collapse.

016e collapses: peak eval 326.7@75K → 31.7@95K, NVE = 6.59×@95K.
The trajectory is consistent with cross-seed variation from 008d
(peak 167@25K → 82.8@55K, NVE = 4.12×@55K) — both show accelerating
NVE followed by catastrophic eval decline. Differences in onset timing
and peak height fall within the range of cross-seed variation observed
in 008d's three seeds (Table 3).

A gradient decomposition (Table X) explains why: reward loss contributes
exactly 0% of the gradient to dt_emb.weight. The detach operation in
016e removes a gradient pathway that does not exist. 93% of dt_emb's
gradient comes from observation decoders (orientations, velocity,
height), with the remaining 7% from KL dynamics.

This finding has two implications:
(1) The intuition that CIVO is reward-driven is incorrect at the
    gradient level — dt_emb learns temporal structure primarily from
    observation reconstruction, not from reward prediction.
(2) The reward head's 2.78× prediction gap (Table 2) is a downstream
    consequence of dt_emb features learned for observation decoding,
    not the cause of dt_emb's temporal specialization.
```

- [ ] **ADD Table**: dt_emb Gradient Decomposition

| Source | Grad Norm | Fraction |
|--------|-----------|----------|
| Observation decoders | 1.505 | 93% |
| KL dynamics | 0.119 | 7% |
| Cont head | ~0 | <1% |
| Reward head | 0.000 | 0% |
| **Total** | **1.624** | **100%** |

- [ ] **ADD 016e to main results table** (Table 1 in results):
  ```
  016e | SGS (reward detach) | trn* | ON | 8 | 31.7 @95K | 6.59× | Collapsed (no-op)
  ```

### Existing F2 — Minor Update

**Current state**: "the trained dt-embedding enables the RSSM reward head to develop a 2.78× prediction gap"

- [ ] **ADD clarification** after F2's RSSM fidelity paragraph: "§4.7 shows this reward gap is a downstream effect of dt_emb features learned via observation reconstruction, not the gradient-level cause of dt_emb's temporal specialization."
- [ ] This is a forward reference only — F2's data and claim remain valid.

### Existing F6 Paragraph Summary — Minor Update

**Current state**: "F1–F5 establish trained dt-embedding as the causal factor... F6 shows..."

- [ ] **EXTEND** summary to include F7: "F7 confirms that reward-pathway intervention is an architectural no-op: 93% of the temporal embedding's gradient originates from observation decoders, not reward prediction."

---

## 5. Analysis & Discussion (§5)

### §5.1 The CIVO Mechanism

**Current state**: Four-stage feedback loop. Emphasis on reward head co-adaptation.

**Changes needed**:

- [ ] **ADD paragraph** after the four-stage description: "Gradient decomposition reveals an unexpected asymmetry in this mechanism. While Stage 1 depends on the reward head's dt-differentiated predictions (2.78× gap), the dt-embedding itself is trained almost entirely by observation decoders (93% gradient fraction) and receives zero gradient from the reward head. The reward head's temporal differentiation is therefore a free-rider effect: it exploits features that dt_emb learned for observation reconstruction, not features that reward gradients shaped. This decoupling means that interventions targeting reward→dt_emb gradients (selective gradient stopping) are architectural no-ops — the gradient pathway being 'stopped' carries no signal."
- [ ] **UPDATE** the analogy with delusional bias: add that unlike delusional bias where the policy constraint is the direct cause, CIVO's gradient pathway is indirect — the observation decoders shape dt_emb, and the reward head piggybacks.

### §5.4 Multiple Vulnerability Pathways

**Current state**: Pathway A (CIVO) vs Pathway B (non-CIVO). No gradient-level analysis.

**Changes needed**:

- [ ] **ADD**: 016e as evidence that Pathway A is not reward-gradient-driven. The gradient decomposition suggests that Pathway A operates through representation-level effects (dt_emb features learned from obs decoders enable reward differentiation) rather than through direct reward-gradient co-adaptation.

### §5.5 The dt-Embedding Dilemma

**Current state**: "removing dt-embedding eliminates CIVO but 13× cost to reward prediction"

**Changes needed**:

- [ ] **ADD third horn**: SGS (reward detach) is a no-op, so the design space is not {remove embedding, keep embedding} but {remove embedding, keep + mitigate}. The gradient decomposition shows the mitigation target is obs decoder→dt_emb, not reward→dt_emb.

### §5.6 Implications for Temporal Abstraction

**Current state**: "Regularization of the dt-embedding (e.g., gradient stopping or spectral normalization) could preserve the temporal signal while preventing co-adaptation; we leave empirical evaluation to future work."

**Changes needed**:

- [ ] **REPLACE** "gradient stopping" with specificity: ~~"gradient stopping"~~ → "gradient stopping on observation-decoder pathways (Full-SGS), which removes 93% of the embedding's training signal". Note: reward gradient stopping is confirmed no-op. Full-SGS (018) is the pending test.
- [ ] **ADD**: If 018 results available before submission, integrate: Full-SGS collapses → CIVO is representation-level (even 7% KL gradient suffices); Full-SGS stable → obs decoders are the gradient-level root cause.
- [ ] **UPDATE**: The recommendation for hierarchical approaches (THICK, Hieros) is strengthened by the gradient finding — the problem is not just the reward head but the entire multi-head observation reconstruction system training the temporal embedding.

---

## 6. Conclusion (§6)

### Enumerated Findings

**Current state**: 5 findings listed.

**Changes needed**:

- [ ] **ADD finding 6**: "A gradient decomposition of the temporal embedding reveals that 93\% of its training signal originates from observation decoders and 0\% from reward prediction, rendering reward-pathway interventions architectural no-ops (exp\_016e confirms). The reward head's $2.78\times$ prediction gap is a downstream effect of observation-learned features, not the gradient-level cause of temporal co-adaptation."

### Future Directions

**Current state**: Three avenues: (1) hierarchical, (2) gradient stopping / spectral norm, (3) transformer world models.

**Changes needed**:

- [ ] **UPDATE avenue (2)**: ~~"gradient stopping"~~ → "Full-SGS (detaching observation-decoder gradients from the temporal embedding) is the next critical test: it removes 93% of the embedding's training signal and will distinguish gradient-driven from representation-level CIVO." Reward gradient stopping is ruled out.
- [ ] **Strengthen avenue (1)**: Hierarchical approaches avoid the root cause (multi-head obs reconstruction training a shared temporal embedding) rather than patching a downstream symptom.

---

## 7. Related Work (§2)

**Current state**: Not fully audited here. Check for:

- [ ] **Verify** no claim that "gradient stopping on reward head" is a viable mitigation — D061 rules this out.
- [ ] **ADD** if missing: citation context for gradient-based analysis of learned embeddings in MBRL. The gradient decomposition methodology (per-head attribution of embedding gradients) may be novel in this context.

---

## 8. Figures

- [ ] **ADD Figure**: 016e learning curve overlaid with 008d seeds — showing 016e falls within the 008d seed distribution (no-op visual evidence).
- [ ] **ADD Figure or Table**: Gradient decomposition bar chart (obs decoders 93%, KL 7%, reward 0%).
- [ ] **UPDATE** Fig 2 (NVE trajectory): add 016e trace (should overlap with 008d band).

---

## 9. Cross-Cutting Constraints

- [ ] **Numbers must trace to registry**: 016e peak eval 326.7@75K, collapse 31.7@95K, NVE 6.59×@95K (from 016e diagnosis report)
- [ ] **Do NOT use "SGS delays collapse"** — D061 withdrew this interpretation. 016e vs 008d timing difference = random variation.
- [ ] **Do NOT use "SGS partially effective"** — D057/D058 interpretation retracted.
- [ ] **AUROC=0.933** is from d054 corrected analysis (008e_v3_s2 relabeled as non-CIVO). Must cite this version.
- [ ] **016e NVE**: 016e report says 6.59×@95K. paper_framing.md says 10.42x@95K — **reconcile before writing**. The 016e diagnosis report (artifacts/016e/report/) shows 6.59× at 95K. Use 6.59× unless later checkpoint data available.

---

## Priority Order for Edits

1. **§4 Results — F7** (new finding, highest impact)
2. **§3 Methodology — factorial table + SGS description** (needed for F7 to make sense)
3. **§5.1 CIVO Mechanism — gradient asymmetry paragraph** (reframes the mechanism)
4. **§5.6 Implications — correct "gradient stopping"** (prevents reviewer catching stale claim)
5. **§6 Conclusion — add finding 6 + update future directions**
6. **§1 Introduction — add contribution (4)**
7. **Abstract — compress + add gradient finding**
8. **Figures — 016e overlay + gradient bar chart**
