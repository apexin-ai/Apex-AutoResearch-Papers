# Genuine ISR Crosscheck: β=0.1 Stratified Analysis (r3)

**Date**: 2026-05-14 (r3 — Reviewer correction: Random has conclusion duplication)
**Scope**: ISR β=0.1 (plan002) 3-seed × Random β=0.1 (plan018) 2-seed × Exec-only baseline

> **r3 correction note**: Earlier revisions (r1/r2) erroneously claimed "Random shows no conclusion duplication." This was wrong on the data. Both random seeds show very high H1 rates (random s42 H1=70.9%–73.4%, random s44 H1=83.1%). Conclusion embedding is a **generic GRPO training strategy**, present regardless of reward type. This document now corrects the comparison and reports apple-to-apple genuine-only ISR.

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
| Hacking mode | partial (H7+H1) | conclusion_dup (severe H7) | conclusion_dup (severe H7) |
| proved_single_premise_ratio | 0.185 | 1.00 | 1.00 |

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
| H1 (multi-premise, conclusion in premises) | **70.9% (56/79)**‡ | **83.1% (74/89)** |
| Hacking mode | **H1 conclusion embedding** | **H1 conclusion embedding** |

†Registry conclusion="negative" refers to comparison result (ISR > Random), not model quality.
‡h7_corrected_results.txt strict-normalize count (56/79). Author's re-classification with looser normalization yields 58/79 (73.4%). Difference is 2 borderline samples; narrative unchanged.

### Exec-only Baseline (plan001-s42-r2)

| Metric | s42 |
|--------|-----|
| PR | 0.93 |
| Mean ISR | 0.123 |
| Proved-only ISR | 0.132 |
| n_proved | 93 |

---

## 2. Hacking-Mode Stratification (ISR β=0.1)

### s42 — Full H7/H1/Genuine Breakdown

| Category | Count | % of proved | Mean ISR | Description |
|----------|-------|-------------|----------|-------------|
| H7 (single premise=conclusion) | 13 | 16.0% | 0.660 | Trivial tautology P→P |
| H1 (multi-premise, conclusion embedded) | 42 | 51.9% | 0.225 | Conclusion among real premises |
| **Genuine** (no conclusion duplication) | **26** | **32.1%** | **0.601** | Clean structural reasoning |
| Total | 81 | 100% | 0.337 | — |

ISR β=0.1 s42 mixes three regimes; aggregate ISR (0.337) is a weighted blend.

### s43 — Severe H7 Collapse

| Category | Est. Count | % of proved | Mean ISR | Notes |
|----------|------------|-------------|----------|-------|
| H7 | ~59 | 96.7% | ~0.506 | Nearly all proofs are P→P |
| H1 | 0 | 0% | — | All single-premise |
| **Genuine** | **~2** | **3.3%** | **N/A** | Sample too small |
| Total | 61 | 100% | 0.506 | — |

97% trivial-tautology collapse; genuine ISR is statistically meaningless at n=2.

### s44 — Severe H7 Collapse

| Category | Est. Count | % of proved | Mean ISR | Notes |
|----------|------------|-------------|----------|-------|
| H7 | ~77 | 86.5% | ~0.88 (isr=1 in 65) | Single-premise P→P |
| H1 | 0 | 0% | — | All single-premise |
| **Genuine** | **~12** | **13.5%** | **Unknown** | Per-sample data unavailable (model deleted) |
| Total | 89 | 100% | 0.803 | — |

s43 and s44 eval JSONs no longer on disk (checkpoints cleared); only summary fields remain.

---

## 3. Random β=0.1 Stratification (CORRECTED)

**Random control is NOT clean.** Both random seeds exhibit massive H1 conclusion embedding:

| Seed | n_proved | H7 | H1 | Genuine | Genuine mean ISR | Genuine ISR std | H1 mean ISR |
|------|----------|-----|-----|---------|------------------|-----------------|-------------|
| s42 | 79 | 0 (0.0%) | 58 (73.4%)† | 21 (26.6%) | **0.252** | 0.179 | 0.088 |
| s44 | 89 | 0 (0.0%) | 74 (83.1%) | 15 (16.9%) | **0.199** | 0.370 | 0.043 |

†Author re-classification. h7_corrected_results.txt reports 56/79 (70.9%); difference attributable to whitespace/parenthesis normalization on 2 borderline cases.

**Observation**: Random reward induces the **same conclusion-embedding hack** as ISR reward, but with multi-premise wrappers (H1 form) instead of single-premise (H7 form). Random never produces H7=1.0 tautologies because there is no ISR signal rewarding single-premise compression; the model defaults to "stuff conclusion into a multi-premise list."

**Mechanistic read**: H1 is a **GRPO-universal strategy** — embedding the conclusion in the premise set guarantees executability (Prover9 trivially derives P from {…, P, …}) and thus collects the execution reward. The hack does not require ISR signal.

---

## 4. Comparison Table (Genuine-Only, Apple-to-Apple)

| Condition | Seed | PR | Aggregate ISR | Genuine n | **Genuine ISR** | H7 % | H1 % | Hacking mode |
|-----------|------|------|--------------|-----------|-----------------|-------|------|--------------|
| ISR β=0.1 | s42 | 0.81 | 0.337 | 26 | **0.601** | 16.0% | 51.9% | mixed H7+H1 |
| ISR β=0.1 | s43 | 0.61 | 0.506 | ~2 | N/A | 96.7% | 0% | severe H7 |
| ISR β=0.1 | s44 | 0.89 | 0.803 | ~12 | Unknown | 86.5% | 0% | severe H7 |
| Random β=0.1 | s42 | 0.79 | 0.104 | 21 | **0.252** | 0.0% | 73.4% | H1 only |
| Random β=0.1 | s44 | 0.89 | 0.062 | 15 | **0.199** | 0.0% | 83.1% | H1 only |
| Exec-only | s42 | 0.93 | 0.123 | —§ | 0.123§ | — | — | redundant coding |

§Exec-only ISR has different semantics (C006: low ISR = redundant coding from repeated ground facts, not absence of reasoning).

---

## 5. Genuine-Only Comparison (apple-to-apple)

### Genuine ISR: ISR β=0.1 vs Random β=0.1

**Single seed (s42 within-seed comparison, only seed where both methods provide reliable n):**
- ISR β=0.1 s42 Genuine ISR = **0.601** (n=26)
- Random β=0.1 s42 Genuine ISR = **0.252** (n=21)
- Δ = 0.349, ratio = **2.4×**

**Random cross-seed (genuine baseline reliability check):**
- Random s42 Genuine ISR = 0.252 (n=21, std=0.179)
- Random s44 Genuine ISR = 0.199 (n=15, std=0.370)
- Random Genuine mean ≈ 0.23, broadly consistent across random seeds

### Revised 5.8× claim

Earlier the doc reported "5.8× difference" between ISR s42 Genuine ISR (0.601) and Random s42 aggregate ISR (0.104). That comparison was **not apple-to-apple** — it compared a hacking-filtered ISR to an unfiltered (H1-contaminated) ISR.

**Corrected apple-to-apple ratio**: 0.601 / 0.252 = **2.4×**, not 5.8×.

The smaller ratio reflects that ~73% of "random ISR" was H1-contaminated and depressed by H1 mean ISR (0.088). Filtering to genuine-only raises random's effective ISR by ~2.4× (0.104 → 0.252) and shrinks the ISR vs Random gap accordingly.

### Cross-seed statistics (still 1 seed for ISR genuine)

- ISR β=0.1 genuine ISR available for s42 only (n=26)
- s43 has n≈2 genuine (unusable)
- s44 has n≈12 genuine but per-sample data is gone (model dir deleted/eval JSON missing)
- 3-seed mean±std for ISR genuine cannot be computed honestly

---

## 6. Core Narrative Update

### What's true (data-supported)

1. **Conclusion embedding (H1) is GRPO-universal**, not ISR-induced.
   - Random s42 H1=70.9–73.4%, Random s44 H1=83.1%, ISR s42 H1=51.9%.
   - GRPO reward shaping favors embedding the goal in the premise list because it trivially passes the executability gate.

2. **ISR reward shifts the embedding mode, not the embedding rate.**
   - Random: 0% H7, ~73-83% H1 → multi-premise wrappers with conclusion inside.
   - ISR β=0.1: 16% H7, 52% H1 (s42); 87-97% H7 (s43/s44) → single-premise P→P collapse.
   - ISR's per-premise indispensability signal rewards compressing the premise list to a single line containing the conclusion (maximizes ISR=1.0 trivially).

3. **Even after filtering hacks, ISR β=0.1 produces higher genuine ISR than random** in the one seed where comparison is possible (s42: 0.601 vs 0.252, 2.4×).
   - This is a within-seed observation, not a cross-seed claim.
   - n=1 ISR seed for genuine ISR estimate; n=2 random seeds (broadly stable at ~0.20-0.25).

### What was wrong before

| Earlier claim | Reality |
|---------------|---------|
| "Random control shows no conclusion duplication" | Random s42 H1=70.9%, s44 H1=83.1% — equally high embedding rate |
| "5.8× ISR vs Random ratio (0.601 / 0.104)" | Not apple-to-apple; mixed genuine vs hacked. Correct ratio is 2.4× (0.601 / 0.252). |
| "Random ISR is genuine" | False; ~73-83% of random "ISR" comes from H1-hacked proofs with very low ISR (mean 0.04-0.09). |

### Paper-ready framing

- "Conclusion embedding (placing the target conclusion into the premise list) is a generic GRPO strategy that emerges under both ISR and random rewards. The specific form differs: ISR reward promotes single-premise tautological collapse (H7), random reward promotes multi-premise embedding (H1), but the underlying mechanism — exploiting the executability gate — is shared."
- "Comparing apple-to-apple genuine-only ISR within seed 42, ISR β=0.1 produces 2.4× the genuine ISR of random (0.601 vs 0.252). This effect is observed in 1 of 3 ISR seeds; the other 2 seeds collapse into H7 hacking before the genuine signal can stabilize."

---

## 7. Recommended Next Steps

1. **Retire all "Random has no hacking" claims** in the paper. Random has H1 hacking at ~70-83% rates.
2. **Use 2.4× as the headline genuine-vs-genuine effect**, not 5.8×.
3. **Frame the contribution as mode-specific hacking**: ISR → H7 tautology; Random → H1 embedding. Both stem from the executability gate.
4. **Do NOT report 3-seed genuine mean±std** for ISR; n=1 reliable seed.
5. If a stronger genuine claim is needed for camera-ready, re-train ISR β=0.1 s44 from scratch with eval JSON retention, and run the same H7/H1/Genuine classification.

---

## Data Provenance

All metrics from project registry (eval_sta.py unified evaluation, per C004).

- plan002-additive-b01-s42: H7/H1/Genuine breakdown computed from `/root/autodl-tmp/outputs/plan002_additive_b01_s42/eval_sta_results.json` via per-sample normalize(premises)/normalize(conclusion) comparison (2026-05-14)
- plan002-additive-b01-s43, s44: eval JSONs unavailable on disk; H7 rate from registry's h7_rate_calibrated field, genuine count estimated as (1 − h7_rate) × n_proved
- plan018-additive-random-b01-s42: H7/H1/Genuine from `/root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json`
- plan018-additive-random-b01-s44: H7/H1/Genuine from `/root/autodl-tmp/outputs/plan018_additive_random_b01_s44/eval_results/eval_sta_results.json`
- Classification script: `/tmp/classify_genuine.py` on westd-39279 (normalized string compare on premises vs conclusion; H7 = single-premise & match, H1 = multi-premise & at least one premise matches, Genuine = no premise matches conclusion after normalization)
- plan001-exec-only-s42-r2: eval_sta.py full STA evaluation
