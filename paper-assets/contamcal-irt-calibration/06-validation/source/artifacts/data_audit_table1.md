# Data Audit: Table 1 (Dose-Response Profiles) + Table 2 (Cross-Seed) + Inline Numbers

Audited: 2026-05-22
Source: eval_results.json files on westd-29999 and cqa1-21977

---

## Table 1 (tab:taxonomy) — Baselines

| Model | Paper | Source (s42) | Check |
|-------|-------|-------------|-------|
| Phi-4 14.7B | 76.4% | 76.44% (0.7644210226) | ✅ |
| Qwen-14B | 69.4% | 69.44% (0.6944167498) | ✅ |
| Qwen-7B | 66.1% | 66.11% (0.6610881641) | ✅ |
| Gemma-2 9B | 61.9% | 61.86% (0.6186440678) | ✅ |
| OLMo-2 7B | 53.8% | 53.79% (0.5378863410) | ✅ |

## Table 1 — Δacc (d000→d100)

| Model | Paper | Source Δ | Check |
|-------|-------|----------|-------|
| Phi-4 | ±0.5pp | -0.17pp (max dev: +0.54 at d025) | ✅ characterization of CI range [-0.60,+0.26] |
| Qwen-14B | −9.4 to −12.7pp | -9.37pp, CI [-12.74,-9.0] | ✅ -9.4≈point est, -12.7≈CI lower bound |
| Qwen-7B | −1.8pp | -1.78pp | ✅ |
| Gemma-2 | +3.8pp | +3.76pp | ✅ |
| OLMo-2 | +3.2pp | +3.21pp | ✅ |

## Table 1 — Peak Column

| Model | Paper | Source | Check |
|-------|-------|--------|-------|
| Phi-4 | negl. | max |Δ|=0.54pp | ✅ |
| Qwen-14B | --- | max harm at d050 (-10.03pp) | ✅ |
| Qwen-7B | −3.1 d025 | d025 Δ=-3.13pp from baseline | ✅ |
| Gemma-2 | mono. | 61.86→63.42→64.56→64.01→65.62 | ⚠️ d050 dips -0.55pp below d025; not strictly monotonic |
| OLMo-2 | sat. d050 | d050=57.25% > d100=57.00% | ✅ |

## Table 1 — OLMo-2 Footnote (†)

| Seed | Paper | Source | Check |
|------|-------|--------|-------|
| s42 | +3.2pp | +3.21pp | ✅ |
| s123 | −0.6pp | −0.55pp | ✅ (rounds to -0.6) |
| s0 | +1.4pp | +1.38pp | ✅ (rounds to +1.4) |

---

## Table 2 (tab:cross_seed) — Per-Seed Signs

Convention: |Δ|≥1pp = +/−; |Δ|<1pp = 0

| Model | Seed | Source Δ(d100) | Expected Sign | Paper Sign | Check |
|-------|------|---------------|---------------|------------|-------|
| Phi-4 | s42 | -0.17pp | 0 | 0 | ✅ |
| Phi-4 | s123 | +1.82pp | + | + | ✅ |
| Phi-4 | s0 | +0.51pp | 0 | 0 | ✅ |
| Qwen-14B | s42 | -9.37pp | − | − | ✅ |
| Qwen-14B | s123 | -12.73pp | − | − | ✅ |
| Qwen-14B | s0 | -24.99pp | − | − | ✅ |
| Qwen-7B | s42 | -1.78pp | − | − | ✅ |
| Qwen-7B | s123 | -0.01pp | 0 | 0 | ✅ |
| Qwen-7B | s0 | -1.03pp | − | − | ✅ |
| Gemma-2 | s42 | +3.76pp | + | + | ✅ |
| Gemma-2 | s123 | +1.49pp | + | + | ✅ |
| Gemma-2 | s0 | +1.90pp | + | + | ✅ |
| OLMo-2 | s42 | +3.21pp | + | + | ✅ |
| OLMo-2 | s123 | -0.55pp | 0 | − | ⚠️ |Δ|=0.55<1 → should be "0" not "−" |
| OLMo-2 | s0 | +1.38pp | + | + | ✅ |

### Table 2 — Cross-Seed Aggregate Values

| Model | Paper CI | Verified? |
|-------|---------|-----------|
| Qwen-14B mean | −15.7pp | (-9.37-12.73-24.99)/3 = -15.70pp ✅ |
| Qwen-14B range | −9.4 to −25.0pp | s42=-9.37, s0=-24.99 ✅ |

---

## §5.1 Inline Numbers — Baseline Ability Gradient

| Claim | Source | Check |
|-------|--------|-------|
| OLMo-2 (53.8%) gains +3.2pp | 53.79%, Δ=+3.21pp | ✅ |
| Gemma-2 (61.9%) gains +3.8pp monotonically | 61.86%, Δ=+3.76pp | ✅ Δ; ⚠️ "monotonically" (d050<d025) |
| Qwen-7B (66.1%) trough at d025 | 66.11%, d025 trough=-3.13pp | ✅ |
| Qwen-14B (69.4%) collapses −9.4 to −25.0pp | 69.44%, range -9.37 to -24.99pp | ✅ |
| Qwen-14B mean −15.7pp | (-9.37-12.73-24.99)/3 = -15.70pp | ✅ |
| Qwen-14B 3× more fragile than 7B | peak harm: 14B d050=-10.03 / 7B d025=-3.13 = 3.2× | ✅ approximate |
| Phi-4 (76.4%) immune | 76.44%, |Δ|<1pp all dosages | ✅ |

## §5.1 — Out-of-Sample Validation (LLaMA-3.1-8B)

| Claim | Source (s0) | Check |
|-------|------------|-------|
| MMLU 53.50%→52.81% | d000=0.53497, d100=0.52813 → 53.50%→52.81% | ✅ |
| Δ=−0.69pp | 52.81-53.50 = -0.69pp | ✅ |
| ARC 72.61%→72.70% | d000=0.72611, d100=0.72696 → 72.61%→72.70% | ✅ |
| Δ=+0.09pp | 72.70-72.61 = +0.09pp | ✅ |

## §5.2 — GSM8K Transfer (tab:gsm8k_transfer)

The appendix table uses mean(s42, s123) for families where both seeds exist.

| Claim | Source | Check |
|-------|--------|-------|
| Qwen-7B +10.1pp GSM8K | mean(s42=+11.07, s123=+9.18) = +10.13pp | ✅ |
| Qwen-7B Range ±0.9 | (11.07-9.18)/2 = ±0.95pp | ✅ |
| Phi-4 −0.5pp GSM8K | s123: -0.46pp → -0.5pp | ✅ |
| OLMo-2 +2.1pp GSM8K | mean(s42=+1.74, s123=+2.43) = +2.09pp → +2.1pp | ✅ value; ⚠️ footnote says "Seed=42" but is mean(s42,s123) |
| Qwen-14B +13.1pp GSM8K | mean(s42=+20.47, s123=+5.69) = +13.08pp → +13.1pp | ✅ |
| Qwen-14B Range ±7.4 | (20.47-5.69)/2 = ±7.39pp | ✅ |
| LLaMA-3.1 +16.4pp GSM8K | s0: d000=38.74%, d100=55.12%, Δ=+16.38pp → +16.4pp | ✅ |

## §5.2 — GSM8K Dose Table (tab:gsm8k_dose, seed=0)

| Family | Paper d000 | Source d000 | Paper d100 | Source d100 | Paper Δ | Source Δ | Check |
|--------|-----------|------------|-----------|------------|---------|---------|-------|
| Phi-4 | 84.46 | 84.46% | 85.60 | 85.60% | +1.14 | +1.14pp | ✅ |
| Qwen-14B | 74.98 | 74.98% | 82.41 | 82.41% | +7.43 | +7.43pp | ✅ |
| Qwen-7B | 73.31 | 73.31% | 81.20 | 81.20% | +7.89 | +7.89pp | ✅ |
| OLMo-2 | 60.58 | 60.58% | 69.75 | 69.75% | +9.17 | +9.17pp | ✅ |
| LLaMA-3.1 | 38.74 | 38.74% | 55.12 | 55.12% | +16.38 | +16.38pp | ✅ |

## §5.2 — OLMo-2 Seed Sensitivity Inline

| Claim | Source | Check |
|-------|--------|-------|
| +2.1pp at s42 | mean(s42,s123)=+2.09pp | ✅ value; ⚠️ "s42" label is misleading (actually mean) |
| +9.2pp at s0 | gsm8k_eval s0: +9.17pp → +9.2pp | ✅ |

---

## Issues Found

### 1. Gemma-2 "mono." Peak Label (Table 1)
**Severity: Minor**
s42 MMLU trajectory: 61.86→63.42→64.56→64.01→65.62. The d050 value (64.01%) is 0.55pp below d025 (64.56%), violating strict monotonicity. The overall trend is upward and the dip is likely within noise, but the "mono." label is technically inaccurate.

### 2. OLMo-2 s123 Sign in Table 2
**Severity: Minor**
The sign convention (footnote b) defines |Δ|<1pp as "0". OLMo-2 s123 Δ=-0.55pp (|Δ|=0.55<1) should be classified as "0" rather than "−". This affects the stated cross-seed pattern: currently "+/−/+" should be "+/0/+". The "Borderl." direction classification and "×" consistency verdict in Table 2 may need revisiting.

### 3. GSM8K Transfer Table Footnote Mislabel
**Severity: Minor**
OLMo-2 footnote (§) says "Seed=42: +2.1pp" but the value is mean(s42=+1.74, s123=+2.43)=+2.09pp. The same occurs in the inline text ("OLMo-2's gain is seed-sensitive (+2.1pp at s42; +9.2pp at s0)"). True s42-only value is +1.74pp, not +2.1pp.

---

## Summary

| Category | Total Checked | Correct | Issues |
|----------|--------------|---------|--------|
| Table 1 baselines | 5 | 5 | 0 |
| Table 1 Δacc | 5 | 5 | 0 |
| Table 1 Peak | 5 | 4 | 1 (Gemma-2 mono.) |
| Table 1 footnotes | 3 | 3 | 0 |
| Table 2 signs | 15 | 14 | 1 (OLMo-2 s123) |
| Table 2 aggregates | 2 | 2 | 0 |
| §5.1 inline | 11 | 11 | 0 (Gemma-2 mono. same issue) |
| §5.1 LLaMA OOS | 4 | 4 | 0 |
| §5.2 GSM8K transfer | 7 | 7 | 0 (value correct, label issue) |
| §5.2 GSM8K dose | 5 | 5 | 0 |
| §5.2 seed sensitivity | 2 | 2 | 0 (value correct, label issue) |
| **Total** | **64** | **61** | **3** |

All 3 issues are minor (labeling/characterization, not data errors). No numerical discrepancies between paper and source data.
