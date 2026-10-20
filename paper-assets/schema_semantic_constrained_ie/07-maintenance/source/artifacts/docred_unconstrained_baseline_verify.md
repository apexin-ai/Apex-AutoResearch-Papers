# DocRED Unconstrained Eval Baseline — Verification Report

Date: 2026-05-16

## 1. Data Source Verification

| Item | Qwen | Llama |
|------|------|-------|
| Output file | `outputs/w5_qwen_docred_lora_unconstrained_eval.jsonl` | `outputs/w5_llama_docred_lora_unconstrained_eval.jsonl` |
| Lines (wc -l) | 998 | 998 |
| Parse failures (grep `parsed_output": null`) | 71 | 23 |
| Compute script | `scripts/compute_metrics_qwen_unconstrained.py` | `scripts/compute_metrics.py` |

Both files contain 998 per-sample JSONL records (no summary line). Metrics were computed by separate scripts and registered to the experiment registry.

## 2. Registry Metrics (Complete)

### Qwen (w5_qwen_docred_lora_unconstrained_eval)

| Metric | All Samples | Excl Fail |
|--------|-------------|-----------|
| ET% | 0.00 | 0.00 |
| RV% | 0.27 | 0.27 |
| DR% | 0.76 | 0.76 |
| CF% | 0.12 | 0.12 |
| E-F1 | 82.15 | 85.72 |
| E-P | 85.44 | 85.44 |
| E-R | 79.11 | 86.00 |
| R-F1 | 40.86 | 42.20 |
| R-P | 36.41 | 36.41 |
| R-R | 46.56 | 50.17 |
| parse_fail_rate | 7.11% | — |
| total_samples | 998 | 927 |
| total_entities_pred | 18091 | — |
| total_relations_pred | 15870 | — |

### Llama (w5_llama_docred_lora_unconstrained_eval)

| Metric | All Samples | Excl Fail |
|--------|-------------|-----------|
| ET% | 0.00 | **not computed** |
| RV% | 0.15 | **not computed** |
| DR% | 0.49 | **not computed** |
| CF% | **not computed** | **not computed** |
| E-F1 | 83.93 | **not computed** |
| E-P | 84.93 | **not computed** |
| E-R | 82.96 | **not computed** |
| R-F1 | 43.72 | **not computed** |
| R-P | 38.59 | **not computed** |
| R-R | 50.41 | **not computed** |
| parse_fail_rate | 2.30% | — |
| total_samples | 998 | 975 |
| total_entities_pred | 19106 | — |
| total_relations_pred | 16171 | — |

## 3. Consistency Check: File vs Registry

### Parse failure verification (file → registry)

| Model | File grep count | Registry parse_fail_rate | Expected (count/998×100) | Match? |
|-------|----------------|--------------------------|--------------------------|--------|
| Qwen | 71 | 7.11% | 7.114% → 7.11% | **YES** |
| Llama | 23 | 2.30% | 2.305% → 2.30% | **YES** |

### Key numbers cited in task

| Model | Cited DR% | Registry DR% | Match? | Cited R-F1 | Registry R-F1 | Match? |
|-------|-----------|--------------|--------|------------|---------------|--------|
| Qwen | 0.76% | 0.76 | **YES** | 40.86% | 40.86 | **YES** |
| Llama | 0.49% | 0.49 | **YES** | 43.72% | 43.72 | **YES** |

**Conclusion: All cited baseline numbers are consistent with registry records, and registry records are consistent with the raw output files (verified via parse failure counts and file line counts).**

## 4. Script Methodology Differences (Important)

| Aspect | Qwen script | Llama script |
|--------|-------------|--------------|
| Entity type normalization | YES (PERSON→PER, ORGANIZATION→ORG, etc.) | NO (raw string match) |
| CF% computation | YES | NO |
| Excl-fail metrics | YES | NO |
| F1 rounding | `round(x, 2)` | `.2f` format |

**Impact**: 
- Qwen ET% = 0 partly because normalization maps "PERSON"→"PER" etc. Llama ET% = 0 means the model natively outputs the correct short-form types.
- Llama is missing CF% and excl_fail metrics. These should be computed for a fair comparison in the paper.

## 5. Parse Failure Analysis

| Model | Parse Failures | Rate | Severity |
|-------|---------------|------|----------|
| Qwen | 71/998 | 7.11% | **High** — material impact on all-samples F1 |
| Llama | 23/998 | 2.30% | Moderate — lower but still notable |

The Qwen parse failure rate (7.11%) is **3x higher** than Llama (2.30%). This inflates the gap between all-samples and excl_fail metrics for Qwen:
- Qwen E-F1: 82.15 → 85.72 (+3.57 pp when excluding failures)
- Qwen R-F1: 40.86 → 42.20 (+1.34 pp when excluding failures)

## 6. Paper Recommendations

### Which version to use?

| Scenario | Recommendation |
|----------|---------------|
| Main table (Table 1 / Table 2) | **All-samples** — more conservative, standard practice |
| Supplementary / discussion | Report **excl_fail** alongside all-samples, plus parse_fail_rate |
| Constrained vs unconstrained comparison | Use **same version** for both; all-samples is safer |

### Missing data to compute before paper

1. **Llama CF%** — the `compute_metrics.py` script doesn't compute cross-field consistency violations. Need to add CF counting (same logic as Qwen script) or run the Qwen script adapted for Llama.
2. **Llama excl_fail metrics** — needed for fair apples-to-apples comparison in supplementary.
3. Both models show very low violation rates (DR < 1%), which is the expected unconstrained baseline — constrained decoding should reduce these further.
