# Genuine ISR Crosscheck: β=0.1 Stratified Analysis (r5)

**Date**: 2026-05-14 (r5 — adds premise-count-matched analysis; corrects 2.5× headline)
**Scope**: ISR β=0.1 (plan002) 3-seed × Random β=0.1 (plan018) 2-seed × Exec-only baseline

> **Normalization**: H7/H1/Genuine classifications use `strip()` + whitespace-collapse (matching `h7_corrected_results.txt` and `scripts/classify_h7.py`). All four reasonable normalizations (strip, strip+collapse, strip+lower, strip+lower+nospace) yield **identical** H1=56/79 for Random s42 — the previously reported "58/79 (73.4%)" Worker number could not be reproduced with any of these normalizations; the file `h7_corrected_results.txt` reports 56/79 and is authoritative.

> **r5 critical revision**: The 2.5× ISR-vs-Random genuine-ISR ratio in r4 is **largely a premise-count distribution artifact** (Section 5b). When matched on premise count (≥3 premises, the only overlapping range), the ratio collapses to **1.06×**.

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
| H1 (strict, normalize=strip+collapse) | **56/79 (70.9%)** | **71/89 (79.8%)** |
| Hacking mode | **H1 conclusion embedding** | **H1 conclusion embedding** |

†Registry conclusion="negative" refers to comparison result (ISR > Random), not model quality.

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
| **Genuine** (no conclusion duplication) | **26** | **32.1%** | **0.601** | No surface H7/H1; premise count strongly skewed low (see §5b) |
| Total | 81 | 100% | 0.337 | — |

### s43 — Severe H7 Collapse

| Category | Est. Count | % of proved | Mean ISR | Notes |
|----------|------------|-------------|----------|-------|
| H7 | ~59 | 96.7% | ~0.506 | Nearly all proofs are P→P |
| H1 | 0 | 0% | — | All single-premise |
| **Genuine** | **~2** | **3.3%** | **N/A** | Sample too small |
| Total | 61 | 100% | 0.506 | — |

### s44 — Severe H7 Collapse

| Category | Est. Count | % of proved | Mean ISR | Notes |
|----------|------------|-------------|----------|-------|
| H7 | ~77 | 86.5% | ~0.88 (isr=1 in 65) | Single-premise P→P |
| H1 | 0 | 0% | — | All single-premise |
| **Genuine** | **~12** | **13.5%** | **Unknown** | Per-sample data unavailable (model deleted) |
| Total | 89 | 100% | 0.803 | — |

s43 and s44 eval JSONs no longer on disk (checkpoints cleared); only summary fields remain.

---

## 3. Random β=0.1 Stratification

Conclusion embedding (H1) is a **generic GRPO training strategy**, present regardless of reward type. Both random seeds show ~71–80% H1 rates.

| Seed | n_proved | H7 | H1 (strict) | Genuine | Genuine mean ISR | Genuine ISR std | H1 mean ISR |
|------|----------|-----|-------------|---------|------------------|-----------------|-------------|
| s42 | 79 | 0 (0.0%) | **56 (70.9%)** | 23 (29.1%) | **0.243** | 0.169 | 0.085 |
| s44 | 89 | 0 (0.0%) | **71 (79.8%)** | 18 (20.2%) | **0.166** | 0.335 | 0.045 |

**Observation**: Random reward induces the **same conclusion-embedding hack** as ISR reward, but with multi-premise wrappers (H1 form) instead of single-premise (H7 form). Random never produces H7=1.0 tautologies because there is no ISR signal rewarding single-premise compression; the model defaults to "stuff conclusion into a multi-premise list."

**Mechanistic read**: H1 is a **GRPO-universal strategy** — embedding the conclusion in the premise set guarantees executability (Prover9 trivially derives P from {…, P, …}) and thus collects the execution reward. The hack does not require ISR signal.

**H1 count cross-check (Task 2)**: Worker's earlier 58/79 (73.4%) number is not reproducible from the eval JSON under any of the four common normalizations:

| Normalization | Random s42 H1 |
|---------------|---------------|
| `strip()` only | 56/79 (70.9%) |
| `strip() + collapse whitespace` (h7_corrected_results.txt method) | **56/79 (70.9%)** |
| `strip().lower()` | 56/79 (70.9%) |
| `strip().lower().replace(' ','')` (Worker hypothesized method) | 56/79 (70.9%) |
| `re.sub(r'[^a-zA-Z0-9]','', s).lower()` (alnum-only loose match) | 61/79 (77.2%) |

The 56 figure is canonical and matches `h7_corrected_results.txt`. The 58 number likely came from a different source (possibly a stale intermediate run or counting `H7+H1+borderline-substring`). **Adopt 56/79 (70.9%) and Genuine=23 going forward.**

---

## 4. Comparison Table (Genuine-Only, Surface Filtering Only)

| Condition | Seed | PR | Aggregate ISR | Genuine n | **Genuine ISR** | H7 % | H1 % | Hacking mode |
|-----------|------|------|--------------|-----------|-----------------|-------|------|--------------|
| ISR β=0.1 | s42 | 0.81 | 0.337 | 26 | **0.601** | 16.0% | 51.9% | mixed H7+H1 |
| ISR β=0.1 | s43 | 0.61 | 0.506 | ~2 | N/A | 96.7% | 0% | severe H7 |
| ISR β=0.1 | s44 | 0.89 | 0.803 | ~12 | Unknown | 86.5% | 0% | severe H7 |
| Random β=0.1 | s42 | 0.79 | 0.104 | 23 | **0.243** | 0.0% | 70.9% | H1 only |
| Random β=0.1 | s44 | 0.89 | 0.062 | 18 | **0.166** | 0.0% | 79.8% | H1 only |
| Exec-only | s42 | 0.93 | 0.123 | —§ | 0.123§ | — | — | redundant coding |

§Exec-only ISR has different semantics (C006: low ISR = redundant coding from repeated ground facts, not absence of reasoning).

> **Read this table with §5b in mind.** The 0.601 vs 0.243 "Genuine" gap is dominated by short-proof samples (n_premises ≤ 2) that only appear on the ISR side. After matching on premise count, the gap evaporates.

---

## 5. Genuine-Only Comparison

### 5a. Surface-level (premise-count-unmatched)

- ISR β=0.1 s42 Genuine ISR = **0.601** (n=26, std=0.337)
- Random β=0.1 s42 Genuine ISR = **0.243** (n=23, std=0.169)
- Δ = 0.358, naive ratio = **2.47×**

This is the number reported in r4 as "2.5×". It is **not premise-count-matched**.

### 5b. Premise-Count-Matched (r5 — CRITICAL)

Reviewer concern: ISR genuine 26 samples are concentrated at very low premise count, where ISR is mechanically high (LOO removes 1 of 1–2 premises → ISR ≥ 0.5 by construction). Random genuine 23 samples are all ≥ 3 premises.

**Premise-count distribution of Genuine samples:**

| n_premises bucket | ISR s42 Genuine | Random s42 Genuine |
|-------------------|------------------|---------------------|
| 1 | 2 (7.7%) | 0 |
| 2 | 13 (50.0%) | 0 |
| 3 | 2 (7.7%) | 4 (17.4%) |
| 4 | 0 | 0 |
| 5+ | 9 (34.6%) | 19 (82.6%) |
| **Total** | **26** | **23** |
| ≤ 2 premises | **15 (57.7%)** | **0 (0.0%)** |
| ≥ 3 premises | **11 (42.3%)** | **23 (100%)** |

**Bucket-wise Genuine mean ISR:**

| Bucket | ISR n | ISR mean ISR | Rnd n | Rnd mean ISR | Δ |
|--------|-------|--------------|-------|--------------|---|
| 1 | 2 | 0.5000 | 0 | — | — |
| 2 | 13 | **0.9077** | 0 | — | — |
| 3 | 2 | 0.2500 | 4 | **0.4375** | **−0.1875** (Random higher) |
| 4 | 0 | — | 0 | — | — |
| 5+ | 9 | 0.2595 | 19 | 0.2026 | +0.0569 |

**Matched-range comparison (n_premises ≥ 3, the only overlapping range):**

- ISR β=0.1 s42 Genuine (≥3 prems) = **0.2578** (n=11)
- Random β=0.1 s42 Genuine (≥3 prems) = **0.2434** (n=23)
- Δ = 0.0144, ratio = **1.06×**

**Within-bucket findings:**
- **n=3 bucket**: Random (0.4375) > ISR (0.2500). The direction *inverts* in the smallest overlapping bucket.
- **n=5+ bucket**: ISR (0.2595) ≈ Random (0.2026). Tiny absolute gap (Δ=0.057); not robust given Random std=high.
- **n≤2 bucket**: ISR has 15/26 samples here; Random has 0. ISR's mean here is 0.86 because LOO of 1-2 premises mechanically gives ISR ≥ 0.5.

**Reinterpretation of the 2.5× headline:**

The 0.601 (ISR) vs 0.243 (Random) gap arises almost entirely from the fact that 57.7 % of ISR's Genuine sample lies in a premise-count bucket where Random has zero samples — and where ISR is mechanically inflated by short-proof arithmetic (LOO of 1–2 premises forces ISR ≥ 0.5).

A weighted decomposition makes this concrete:
- ISR genuine mean = 0.577 × 0.86 (≤2 bucket) + 0.423 × 0.258 (≥3 bucket) = 0.496 + 0.109 = **0.605**
- ~82 % of the gap to Random (0.243) is attributable to the ≤2-premise mass that has no Random counterpart.

**Conclusion: The "2.5× genuine ISR advantage" is principally a premise-length confound, not a reasoning-quality signal.** At matched premise count, ISR and Random produce statistically indistinguishable genuine ISRs (0.258 vs 0.243, ratio 1.06×).

### 5c. Cross-seed reliability

- ISR β=0.1 genuine ISR is only computable for s42 (s43/s44 collapsed to H7, no usable Genuine eval JSON).
- Random β=0.1 genuine ISR: s42=0.243 (n=23), s44=0.166 (n=18); consistent direction.
- 3-seed mean±std for ISR genuine **cannot be computed honestly**.

---

## 6. Core Narrative (revised)

### What's true (data-supported)

1. **Conclusion embedding (H1) is GRPO-universal**, not ISR-induced.
   - Random s42 H1=70.9%, Random s44 H1=79.8%, ISR s42 H1=51.9%.
   - GRPO reward shaping favors embedding the goal in the premise list because it trivially passes the executability gate.

2. **ISR reward shifts the embedding mode, not the embedding rate.**
   - Random: 0% H7, ~71–80% H1 → multi-premise wrappers with conclusion inside.
   - ISR β=0.1: 16% H7, 52% H1 (s42); 87–97% H7 (s43/s44) → single-premise P→P collapse.
   - ISR's per-premise indispensability signal rewards compressing the premise list to a single line containing the conclusion (maximizes ISR=1.0 trivially).

3. **Surface-filtered (Genuine-only) ISR β=0.1 looks 2.5× higher than Random, but this gap is premise-count confounded.**
   - At matched premise count (≥3 premises), ISR and Random produce nearly identical genuine ISR (1.06×).
   - The apparent advantage is driven by ISR's tendency to also emit short (1–2 premise) proofs that don't trip H7 but still arithmetically yield ISR ≥ 0.5.

### Paper-ready framing

- **DO** report mode-specific hacking: ISR → H7 tautology (s43/s44 severely; s42 moderately); Random → H1 embedding.
- **DO** report H1 as a GRPO-universal strategy emerging from the executability gate.
- **DO NOT** claim "ISR produces 2.5× higher genuine ISR than Random." After premise-count matching the effect is ≈1×.
- If a headline genuine-ISR comparison is needed, report the **matched** comparison (1.06× at ≥3 premises) and either bucket-wise tables or weighted matching.

---

## 7. Recommended Next Steps

1. **Retract the 2.5× headline.** Replace with "premise-count-matched genuine ISR is statistically indistinguishable between ISR and Random rewards (1.06× at n_premises ≥ 3)."
2. **Frame the contribution as mode-specific hacking** (still robust): ISR → H7; Random → H1; both driven by the executability gate.
3. **If a positive ISR claim is needed**, look at a non-ISR-derived signal (e.g., proof-length correctness, downstream NLI transfer from plan014), not at ISR itself, since matched ISR shows no advantage.
4. To recover a genuine ISR claim, regenerate ISR β=0.1 with seeds that avoid both H7 and short-proof concentration — likely requires a regularizer that penalizes proof shortness or rewards multi-premise grounding.

---

## Data Provenance

All metrics from eval_sta.py unified evaluation (per C004), classified with strip+collapse-whitespace normalization (matches `scripts/classify_h7.py` and `h7_corrected_results.txt`).

- plan002-additive-b01-s42: `/root/autodl-tmp/outputs/plan002_additive_b01_s42/eval_sta_results.json` — H7=13, H1=42, Genuine=26
- plan002-additive-b01-s43, s44: eval JSONs unavailable on disk; H7 rate from registry's h7_rate_calibrated field, genuine count estimated as (1 − h7_rate) × n_proved
- plan018-additive-random-b01-s42: `/root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json` — H7=0, H1=56, Genuine=23 (matches `h7_corrected_results.txt`)
- plan018-additive-random-b01-s44: `/root/autodl-tmp/outputs/plan018_additive_random_b01_s44/eval_results/eval_sta_results.json` — H7=0, H1=71, Genuine=18 (not in h7_corrected_results.txt; fresh strict classification)
- **Premise-count-matched analysis**: `/tmp/premise_match_analysis.py` on westd-39279 (per-sample iteration over both eval JSONs, bucketing on `len(details.premises)`)
- plan001-exec-only-s42-r2: eval_sta.py full STA evaluation
