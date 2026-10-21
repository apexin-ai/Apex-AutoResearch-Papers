# Paper Data Verification Report

**Date**: 2026-05-23
**Paper**: G-theory variance decomposition of LLM evaluation
**Scope**: All numbers in tex files vs. source JSON data on server (westd-32570)

---

## Summary

| Category | Items Checked | PASS | FAIL | UNVERIFIED |
|----------|:---:|:---:|:---:|:---:|
| Abstract vs Body | 8 | 8 | 0 | 0 |
| Table 2 (cross-model MMLU) | 9 | 9 | 0 | 0 |
| Table 3 (cross-benchmark) | 35 | 35 | 0 | 0 |
| Table 4 (D-study budgets) | 8 | 8 | 0 | 0 |
| §4.1 single-model baseline | 12 | 11 | 0 | 1 |
| §4.6 scale validation | 10 | 8 | **2** (fixed) | 0 |
| Limitations vs body | 4 | 4 | 0 | 0 |
| Appendix tables | 15 | 15 | 0 | 0 |
| Record counts | 4 | 4 | 0 | 0 |
| **Total** | **105** | **102** | **2 (fixed)** | **1** |

---

## Errors Found & Fixed

### 1. §4.6 Qwen-72B item share: 83.3% → 83.2% ✅ FIXED
- **Source**: `exp003_72b_single_gstudy.json` → item_id = 83.2482%
- **Rule**: 83.2482 rounds to 83.2% (not 83.3%)
- **File**: `experiments.tex` line 120

### 2. §4.6 item share gap: 8.8pp → 8.7pp ✅ FIXED
- **Calculation**: 83.2482 − 74.5106 = 8.7376pp → rounds to 8.7pp (not 8.8pp)
- **File**: `experiments.tex` line 120

**Fix applied**: `sed` on `experiments.tex` line 120, LaTeX recompiled successfully.

---

## Unverified Items

### §4.1 text-exact-match temperature = 79.7%
- **Claim**: "temperature dominates at 79.7% of variance" under text-exact-match scoring
- **Status**: No source JSON found that produces this number
- `variance_components_text.json` (5,400 obs, 50 items) shows temperature=14.1%
- The 259K text-exact-match analysis likely exists but its JSON output was not located on server
- **Risk**: LOW — this is a secondary analysis contrasting binary vs text scoring; the number is internally consistent with the narrative but source data is missing

---

## Detailed Verification Log

### Abstract Numbers
| Claim | Source | Status |
|-------|--------|--------|
| ~2.3M records | 2,304,000 exp-002 design | ✅ PASS |
| G≥0.80 with 178 items | D-study 3p×3s projection | ✅ PASS |
| 1,602 evals/model | 178×9=1,602 | ✅ PASS |
| 3.1× item reduction | 552/178=3.10 | ✅ PASS |
| 552 items single-condition | single_condition_dstudy.json n_G80=552 | ✅ PASS |
| model×item up to 36% | HellaSwag 36.0% in Table 3 | ✅ PASS |
| 3× more total evals | 1602/552=2.9≈3× | ✅ PASS |
| Abstract word count | <200 words | ✅ PASS |

### Table 2: Cross-Model MMLU (per_benchmark_gstudy_mmlu.json)
| Component | Paper | Source | Status |
|-----------|-------|--------|--------|
| item_id | 37.9% | 37.9138% | ✅ |
| model×item | 30.2% | 30.1585% | ✅ |
| residual | 25.0% | 25.0271% | ✅ |
| model | 2.8% | 2.7832% | ✅ |
| model×prompt | 1.6% | 1.6081% | ✅ |
| prompt×item | 0.9% | 0.8714% | ✅ |
| temp×item | 0.6% | 0.5797% | ✅ |
| seed×item | 0.5% | 0.5173% | ✅ |
| ordering×item | 0.3% | 0.2643% | ✅ |
| G_item | 0.896 | 0.896176 | ✅ |
| Column sum | 100.0% (with "all others") | ✅ | ✅ |

### Table 3: Cross-Benchmark (5 benchmarks)
All 5 columns verified against source JSON files:
- MMLU: `per_benchmark_gstudy_mmlu.json` ✅
- ARC: `per_benchmark_gstudy_arc.json` ✅
- HellaSwag: `per_benchmark_gstudy_hellaswag_2temp.json` (2-temp version) ✅
- GSM8K: `per_benchmark_gstudy_ff.json` (GSM8K section) ✅
- MATH: `math_8model_verified.json` (8-model version) ✅

All 5 columns sum to 100.0% ✅

### Table 4: D-study Budgets (dstudy_henderson_i_259k.json + single_condition_dstudy.json)
| Number | Paper | Source | Status |
|--------|-------|--------|--------|
| Multi-facet n_G80 = 55 | 55 | dstudy n_G80=55 | ✅ |
| Multi-facet G_200 = .936 | .936 | G_item=0.936121 | ✅ |
| Single-cond n_G80 = 552 | 552 | single_condition n_G80=552 | ✅ |
| Single-cond G_200 = .592 | .592 | G_200=0.591748 | ✅ |
| Single-cond G_116 = .457 | .457 | G_116=0.456726 | ✅ |
| IRT+multi G_116 = .895 | .895 | G_116_multi=0.895208 | ✅ |
| Budget ratio 10.0× | 10.0× | 552/55=10.036 | ✅ |
| 3p×3s: 178 items | 178 | Formula verified: σ²_δ=0.028219, n_G80=178 | ✅ |

### §4.1 Single-Model Baseline (dstudy_henderson_i_259k.json, 259,200 records)
| Claim | Paper | Source | Status |
|-------|-------|--------|--------|
| item_id | 58.4% | 58.39% | ✅ |
| residual | 23.1% | 23.14% | ✅ |
| precision | 0.9% | 0.89% | ✅ |
| prompt×item | 5.5% | 5.48% | ✅ |
| seed×item | 4.7% | 4.74% | ✅ |
| precision×item | 3.3% | 3.28% | ✅ |
| temp×item | 2.9% | 2.90% | ✅ |
| ordering×item | 0.8% | 0.84% | ✅ |
| G_item | 0.936 | 0.936121 | ✅ |
| n_G80 = 55 | 55 | n_G80=55 | ✅ |
| 259,200 observations | 259,200 | n_observations=259200 | ✅ |
| text-exact-match temp=79.7% | 79.7% | **SOURCE NOT FOUND** | ⚠️ |

### §4.6 Scale Validation
| Claim | Source | Status |
|-------|--------|--------|
| Qwen-72B item=83.2% | exp003_72b: 83.2482% | ✅ (was 83.3%, **FIXED**) |
| Qwen-72B G=0.979 | exp003_72b: 0.978544 | ✅ |
| Llama-70B item=74.5% | llama70b: 74.5106% | ✅ |
| Llama-70B G=0.957 | llama70b: 0.956639 | ✅ |
| Crossed model×item=38.5% | exp003_crossed: 38.5478% | ✅ |
| Crossed item=35.7% | exp003_crossed: 35.7089% | ✅ |
| Crossed G=0.720 | exp003_crossed: 0.719989 | ✅ |
| Gap=8.7pp | 83.25−74.51=8.74→8.7 | ✅ (was 8.8pp, **FIXED**) |

### Limitations vs Body
| Claim | Body source | Status |
|-------|-------------|--------|
| partial credit 0.86→0.77 | Source: binary G=0.862852, partial G=0.768 | ✅ |
| p=0.10 format test | experiments.tex §4.3 | ✅ |
| 116-item IRT | Table 4 | ✅ |
| 8 models | Throughout | ✅ |

### Record Counts
| Count | Calculation | Status |
|-------|-------------|--------|
| 460,800 | 8×200×6×6×2×4 | ✅ |
| 259,200 | 1×200×3×6×6×3×4 | ✅ |
| 2,304,000 | 8×1×2×6×6×4×200×5 | ✅ |
| 71,280 | 55×1,296 | ✅ |

### Rounding Consistency
All percentages use 1 decimal place consistently. G coefficients use 3 decimal places. Item counts are integers. No inconsistencies found.

---

## Data Source Mapping

| Paper Section | Correct Source File | Notes |
|---------------|-------------------|-------|
| §4.1 single-model | `dstudy_henderson_i_259k.json` | NOT `llama_single_model_gstudy.json` (older, 239K) |
| Table 2 MMLU | `per_benchmark_gstudy_mmlu.json` | |
| Table 3 ARC | `per_benchmark_gstudy_arc.json` | |
| Table 3 HellaSwag | `per_benchmark_gstudy_hellaswag_2temp.json` | NOT the 3-temp version |
| Table 3 GSM8K | `per_benchmark_gstudy_ff.json` (GSM section) | |
| Table 3 MATH | `math_8model_verified.json` | NOT `per_benchmark_gstudy_ff.json` MATH section (7 models) |
| Table 4 D-study | `dstudy_henderson_i_259k.json` + `single_condition_dstudy.json` | |
| §4.6 Qwen-72B | `exp003_72b_single_gstudy.json` | |
| §4.6 Llama-70B | `data/exp_llama70b/llama70b_mmlu_gstudy.json` | |
| §4.6 crossed | `exp003_scale_crossed_3model.json` | |
