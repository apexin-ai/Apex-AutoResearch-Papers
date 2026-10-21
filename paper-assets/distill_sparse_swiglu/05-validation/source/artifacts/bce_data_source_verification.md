# BCE Data Source Verification (Tables 2 & 4)

## 1. Table 2: "BCE + comp.*" PPL = 28.13±0.20

### Source Experiments

| Seed | Registry exp_id | Metric Key | PPL |
|------|-----------------|------------|-----|
| s42 | `bce_isocompute_v3_s42_eval` | `wikitext2_ppl` | 27.9696 |
| s123 | `bce_isocompute_v3_s123_eval` | `wikitext2_ppl` | 28.0627 |
| s456 | `bce_isocompute_v3_s456_eval` | `teal_sparse_ppl` | 28.3503 |

Training config: pure BCE loss, 2700 steps (iso-compute), NO compensation network.

### Computation

- Mean = (27.9696 + 28.0627 + 28.3503) / 3 = **28.1275 → 28.13** ✅
- Std = sqrt(Σ(x-μ)²/2) = sqrt(0.03943) = **0.1985 → 0.20** ✅

### Downstream Metrics

| Metric | s42 | s123 | s456 | Mean | Paper | Std | Paper | Match |
|--------|-----|------|------|------|-------|-----|-------|-------|
| ARC-c | 27.65 | 26.96 | 28.07 | 27.56 | 27.6 | 0.56 | 0.6 | ✅ |
| WG | 51.62 | 51.30 | 52.41 | 51.78 | 51.8 | 0.57 | 0.6 | ✅ |
| MMLU | 26.14 | 26.55 | 25.67 | 26.12 | 26.1 | 0.44 | 0.5 | ⚠️ |
| GSM8K | 1.9 | 2.2 | 2.2 | 2.10 | 2.1 | 0.17 | 0.2 | ✅ |

**MMLU std note**: actual = 0.44, rounds to 0.4; paper reports 0.5 (conservative rounding, minor).

### Footnote Concern

Paper footnote `$^\ast$` reads: "BCE 50%: DejaVu/FastForward pipeline with compensation (67.2M params)."

This is **misleading**. The actual data comes from `bce_isocompute_v3` experiments which have **no compensation network**. The "comp." in "BCE + comp.*" refers to **computational budget matching** (iso-compute, 2700 steps ≈ 2.71x KL budget), NOT the compensation network. The actual compensation experiment (`bce_comp_staged_s42`) yields PPL 25.44 (reported in Table 4).

### Metric Name Inconsistency

s42/s123 use metric key `wikitext2_ppl`; s456 uses `teal_sparse_ppl`. Both represent WikiText-2 PPL under TEAL 50% global allocation. This is a registry naming inconsistency (not a data issue).

---

## 2. Table 4: "BCE + Compensation (hard mask)" PPL = 25.44

### Source Experiment

| Field | Value |
|-------|-------|
| Registry exp_id | `bce_comp_staged_s42` |
| Metric key | `predictor_hard_mask_ppl` |
| PPL | **25.44** ✅ |

Additional metrics from same experiment:
- `predictor_hard_mask_ppl_no_comp` = 27.96 (consistent with Table 4 "BCE (no compensation)" = 27.97 from `eval_bce_v3_s42`)
- `teal_sparse_ppl` = 44.54 (TEAL allocation, not used in table)

### Eval Protocol

The PPL 25.44 uses **predictor hard masks** (per-neuron binary predictions applied directly), NOT TEAL global allocation. This is correctly indicated by "(hard mask)" in the row label. Other rows in Table 4 (KL variants) use TEAL global allocation. The table caption says "unified benchmark protocol" which refers to WikiText-2 seq_len=2048, not the allocation method.

The 0.01 discrepancy between `predictor_hard_mask_ppl_no_comp` (27.96) and the separate `eval_bce_v3_s42` `teal_sparse_ppl` (27.97) is within floating-point rounding.

---

## 3. Conclusion

| Check | Status | Notes |
|-------|--------|-------|
| Table 2 PPL 28.13±0.20 | ✅ Verified | Source: `bce_isocompute_v3_{s42,s123,s456}_eval` |
| Table 2 downstream | ✅ Verified | MMLU std rounding 0.44→0.5 is minor |
| Table 4 PPL 25.44 | ✅ Verified | Source: `bce_comp_staged_s42` `predictor_hard_mask_ppl` |
| Table 4 eval protocol | ✅ Correctly labeled | "(hard mask)" annotation present |

### Issues to Address

1. **Table 2 footnote** (priority: medium): Footnote says "with compensation (67.2M params)" but data is from no-compensation iso-compute experiments. Should clarify that "comp." = computational budget matching, not compensation network.
2. **MMLU std rounding** (priority: low): 0.44 reported as 0.5. Conservative but technically rounds to 0.4.
3. **Registry metric naming** (priority: low): `wikitext2_ppl` vs `teal_sparse_ppl` across seeds for same evaluation.
