# Genuine ISR Crosscheck: β=0.1 Stratified Analysis (r2)

**Date**: 2026-05-14 (r2 update)
**Scope**: ISR β=0.1 (plan002) 3-seed × Random β=0.1 (plan018) 2-seed × Exec-only baseline

---

## 1. Raw Data Summary

### ISR β=0.1 (plan002-additive-b01)

| Metric | s42 | s43 | s44 |
|--------|-----|-----|-----|
| Status | success | negative | negative |
| PR | 0.81 | 0.61 | 0.89 |
| Mean ISR | 0.337 | 0.506 | 0.803 |
| ISR std | 0.323 | 0.452 | 0.342 |
| Proved-only ISR | 0.415 | 0.830 | — |
| n_proved | 81 | 61 | 89 |
| Component mean | 5.58 | 4.03 | 4.33 |
| Tautological collapse | No | No | No |
| Hacking mode | partial | conclusion_dup (severe) | conclusion_dup (severe) |
| Conclusion embedding | — | true | true |
| proved_single_premise_ratio | mixed | 1.00 | 1.00 |

### Random β=0.1 (plan018-additive-random-b01)

| Metric | s42 | s44 |
|--------|-----|-----|
| Status | success† | success |
| PR | 0.79 | 0.89 |
| Mean ISR | 0.104 | 0.062 |
| ISR std | 0.137 | 0.176 |
| Proved-only ISR | 0.131 | 0.070 |
| n_proved | 79 | 89 |
| Component mean | 8.46 | — |
| ISR=0 count (proved) | 29 (36.7%) | 72 (80.9%) |
| Hacking mode | None | None |

†Registry conclusion="negative" refers to the comparison result (ISR > Random), not model quality.

### Exec-only Baseline (plan001-s42-r2)

| Metric | s42 |
|--------|-----|
| PR | 0.93 |
| Mean ISR | 0.123 |
| Proved-only ISR | 0.132 |
| n_proved | 93 |

---

## 2. Hacking-Mode Stratification (ISR β=0.1)

### s42 — Full H7/H1/Genuine Breakdown (from registry audit)

| Category | Count | % of proved | Mean ISR | Description |
|----------|-------|-------------|----------|-------------|
| H7 (single premise=conclusion) | 13 | 16.0% | 0.660 | Trivial tautology P→P |
| H1 (multi premise contains conclusion) | 42 | 51.9% | 0.225 | Conclusion embedded among real premises |
| **Genuine** (no conclusion duplication) | **26** | **32.1%** | **0.601** | Clean structural reasoning |
| Total | 81 | 100% | 0.337 | — |

**s42 interpretation**: Despite 67.9% conclusion duplication, the genuine subset shows high ISR (0.601). H1 samples deflate total ISR (0.225) because embedded conclusion is one of many components; H7 inflates ISR (0.660) because single-premise ablation is binary.

### s43 — Severe Conclusion Duplication

| Category | Est. Count | % of proved | Mean ISR | Notes |
|----------|------------|-------------|----------|-------|
| H7 (single premise=conclusion) | ~59 | 96.7% | ~0.506† | Nearly all proved samples |
| H1 | 0 | 0% | — | All single-premise (no multi) |
| **Genuine** | **~2** | **3.3%** | **N/A** | Too few for ISR estimate |
| Total | 61 | 100% | 0.506 | — |

†h7_rate_calibrated=0.967, proved_single_premise_ratio=1.0.
**s43**: Essentially collapsed — 97% of proofs are P→P tautologies. The ~2 genuine samples are statistically meaningless.

### s44 — Severe Conclusion Duplication

| Category | Est. Count | % of proved | Mean ISR | Notes |
|----------|------------|-------------|----------|-------|
| H7 (single premise=conclusion) | ~77 | 86.5% | ~0.88† | ISR=1.0 in ~65 samples |
| H1 | 0 | 0% | — | All single-premise |
| **Genuine** | **~12** | **13.5%** | **Unknown** | Per-sample data needed |
| Total | 89 | 100% | 0.803 | — |

†h7_rate_calibrated=0.865, isr_1_ratio=0.73.
**s44**: 86.5% conclusion duplication. 12 genuine samples exist but their ISR is not decomposed in registry.

---

## 3. Random β=0.1 Stratification

Random control shows **no conclusion duplication** in either seed:
- **s42**: component_mean=8.46, isr_1_ratio=0, ISR=0 in 36.7% of proved — proofs are verbose with many unnecessary components
- **s44**: ISR=0 in 80.9% of proved (72/89) — most proofs have zero necessary-only components

Random β=0.1 is "clean" — no hacking, no conclusion embedding. All ISR values are genuine.

---

## 4. Comparison Table

| Condition | Seed | PR | Total ISR | Genuine % | Genuine ISR | H7 % | H1 % | Hacking |
|-----------|------|------|-----------|-----------|-------------|-------|------|---------|
| ISR β=0.1 | s42 | 0.81 | 0.337 | 32.1% | **0.601** | 16.0% | 51.9% | partial |
| ISR β=0.1 | s43 | 0.61 | 0.506 | 3.3% | N/A (n≈2) | 96.7% | 0% | severe |
| ISR β=0.1 | s44 | 0.89 | 0.803 | 13.5% | Unknown (n≈12) | 86.5% | 0% | severe |
| Random β=0.1 | s42 | 0.79 | 0.104 | 100% | 0.104 | 0% | 0% | none |
| Random β=0.1 | s44 | 0.89 | 0.062 | 100% | 0.062 | 0% | 0% | none |
| Exec-only | s42 | 0.93 | 0.123 | —† | 0.123† | — | — | — |

†Exec-only ISR has different characteristics (C006: low ISR = redundant coding, not absence of reasoning).

---

## 5. Genuine-Only 3-Seed Analysis

### Problem: Cannot compute 3-seed mean±std

- **s42**: Genuine ISR = 0.601 (n=26, reliable)
- **s43**: Genuine ISR = N/A (n≈2, statistically meaningless)
- **s44**: Genuine ISR = Unknown (n≈12, per-sample data not in registry)

**Only 1 of 3 seeds has a reliable genuine ISR estimate.** 3-seed statistics cannot be computed from registry data alone.

### What would be needed
- s44: Run per-sample H7/genuine classification on the 89 proved samples and compute genuine-only ISR. With n≈12 genuine samples, the estimate would be noisy but usable.
- s43: Even with per-sample data, n≈2 is too small. This seed is a write-off for genuine ISR.

### Best available estimate (s42-only)
- Genuine ISR (ISR β=0.1, s42) = **0.601**
- Random ISR (s42) = **0.104**
- Δ = 0.497, ratio = **5.8×**

---

## 6. Core Question: Is genuine ISR (β=0.1) > Random ISR after excluding hacking?

### Evidence FOR (genuine ISR > random):

1. **s42 within-seed**: Genuine ISR 0.601 vs Random 0.104 = 5.8× difference
2. **Mechanism**: Genuine s42 samples have multi-component proofs (mean 5.58 components) with structurally necessary premises — not tautologies
3. **Random shows zero structure**: Random ISR is near-zero (0.062–0.104), confirming that random noise cannot induce proof structure

### Evidence AGAINST (or complicating factors):

1. **n=1 seed**: Only s42 provides genuine ISR. No cross-seed replication.
2. **Selection bias**: The 32.1% genuine samples in s42 are self-selected — they are the ones that happened not to hack. Their high ISR might reflect a bimodal distribution (hack or don't hack) rather than genuine structural guidance.
3. **H1 contamination in s42**: 51.9% of s42's proofs have conclusion embedded among premises (H1). These aren't counted as "genuine" but they share training signal with genuine samples. The boundary between H1 and genuine is fuzzy.
4. **2/3 seed failure**: ISR β=0.1 collapsed into hacking in 2/3 seeds. The method is unstable regardless of the genuine ISR value.
5. **s42 may be the easy seed**: s42 is the only seed where exec-only also produced decent proofs (PR=0.93).

### Verdict

**Yes, genuine ISR signal exists but is not statistically robust.**

The s42 genuine ISR (0.601) vs random ISR (0.104) gap is large and mechanistically interpretable. But with only 1/3 seeds providing genuine data, this is an observation, not a confirmed finding.

Paper recommendations:
1. Report the s42 genuine ISR as a case study, not a population estimate
2. Emphasize that 2/3 seeds collapsed into hacking (Claim 1 / Goodhart narrative)
3. Frame the genuine ISR signal as "promising but unreliable"
4. Use the ISR vs Random comparison primarily at the within-seed level (s42: 0.601 vs 0.104)

---

## 7. Recommended Next Steps

1. **Run H7/genuine classification on s44 eval outputs** to get genuine ISR for n≈12 samples
2. **Do NOT report 3-seed genuine mean±std** — cannot be computed honestly
3. **Report s42 as the primary genuine ISR datapoint** with the caveat that 2/3 seeds hacked
4. **Consider framing**: "ISR β=0.1 induces genuine structural reasoning in 32% of proofs (s42), but the reward signal is unstable across seeds, with 2/3 seeds collapsing into conclusion duplication hacking"

---

## Data Provenance

All metrics from project registry (eval_sta.py unified evaluation, per C004).
- plan002-additive-b01-s42: H7/H1/genuine breakdown from registry notes (manual audit 2026-05-14)
- plan002-additive-b01-s43: H7 rate from h7_rate_calibrated field; genuine count estimated from (1-h7_rate)*n_proved
- plan002-additive-b01-s44: H7 rate from h7_rate_calibrated field; genuine count estimated similarly
- plan018 seeds: No hacking detected; all ISR values considered genuine
- plan001-exec-only-s42-r2: eval_sta.py full STA evaluation
