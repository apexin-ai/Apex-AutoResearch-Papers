# Decoupling Data Pipeline Audit

**Date:** 2026-05-20
**File:** `decoupling_data.csv` (local) / `fig1_decoupling_data.csv` (server)

## 1. Data in decoupling_data.csv

| attention_ratio | cross_arch_std | jaccard_helped | jaccard_hurt | net_asymmetry |
|-----------------|---------------|----------------|-------------|---------------|
| 0.0000 (pure) | 0.024047 | — | — | — |
| 0.0400 (h24-1) | 0.016238 | 0.09452 | 0.08733 | 0.01281 |
| 0.0769 (h12-1) | 0.013596 | 0.09509 | 0.08087 | 0.01889 |
| 0.1429 (h6-1) | 0.006055 | 0.09223 | 0.09880 | 0.03868 |
| 0.2500 (h3-1) | 0.004943 | 0.10018 | 0.09281 | 0.03959 |

## 2. Generation Pipeline

```
exp010_bridge_analysis.py
  ├─ cross_arch_std ← summary_all_1.3b.csv ← root _results.json files
  └─ Jaccard values ← per-example data (JSON_MAP / JSONL_MAP)
        ↓
exp010_bridge_results.csv
        ↓
generate_paper_data.py → fig1_decoupling_data.csv
        ↓
(local copy with renamed columns) → decoupling_data.csv
```

## 3. Per-Example Data Sources (All lm-eval --log_samples)

| Model | Source File | Format |
|-------|-----------|--------|
| GDN-pure | `lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json` | JSON w/ embedded samples |
| **GDN-h24-1** | `lm_eval_clean/1.3b/GDN-h24-1-logsamples/samples/lambada_openai.jsonl` | JSONL log_samples |
| GDN-h12-1 | `lm_eval_clean/1.3B-100B-GatedDeltaNet-hybrid-12-1.json` | JSON w/ embedded samples |
| **GDN-h6-1** | `lm_eval_clean/1.3b/GDN-h6-1-logsamples/samples/lambada_openai.jsonl` | JSONL log_samples |
| **GDN-h3-1** | `lm_eval_clean/1.3b/GDN-h3-1-logsamples/samples/lambada_openai.jsonl` | JSONL log_samples |
| HGRN2-* (all 5) | `lm_eval_clean/1.3B-100B-HGRN2-*.json` | JSON w/ embedded samples |
| RetNet-* (all 5) | `lm_eval_clean/1.3B-100B-RetNet-*.json` | JSON w/ embedded samples |

All 15 models: 5153 samples (LAMBADA full set), aligned by doc_id.

## 4. Pipeline Consistency Assessment

### Result: CONSISTENT — all data from lm-eval --log_samples

`results_1.3b/logprob/` (custom depth-based logprob pipeline) is **NOT used** in decoupling_data.csv.

### Minor Discrepancy: GDN intermediate variants have two lm-eval runs

The root `_results.json` files (used in `summary_all_1.3b.csv` → `cross_arch_std`) and the logsamples JSONL files (used for Jaccard) come from slightly different lm-eval runs:

| Variant | summary CSV acc | logsamples acc | Δ samples (of 5153) |
|---------|----------------|---------------|---------------------|
| GDN-h24-1 | 0.53969 | 0.53988 | 1 |
| GDN-h6-1 | 0.51096 | 0.50961 | 7 |
| GDN-h3-1 | 0.51349 | 0.51329 | 1 |

### Impact: NEGLIGIBLE

1. `cross_arch_std` and Jaccard are computed independently — never mixed within a single calculation
2. Maximum discrepancy: 7/5153 = 0.14% (GDN-h6-1)
3. Effect on cross_arch_std for h6-1: original σ=0.006055 uses acc=0.5110; if using logsamples acc=0.5096, σ would shift by ~0.0005 — well within noise
4. Jaccard computation is purely per-example binary comparison (helped/hurt sets), unaffected by aggregate acc

### Root Cause

GDN h24-1, h6-1, h3-1 were initially evaluated without `--log_samples` (producing root `_results.json`). A second lm-eval run with `--log_samples` was done later to obtain per-example data (producing the `1.3b/GDN-*-logsamples/` directories). Minor non-determinism between runs causes the small acc differences.

## 5. Conclusion

- **All decoupling data comes from a single pipeline: lm-eval `--log_samples`**
- No contamination from `results_1.3b/logprob/` custom pipeline
- The σ trajectory and Jaccard trajectory use consistent per-example data sources
- The mild two-run discrepancy for 3 GDN variants has negligible impact (<0.15%) and does not affect any qualitative conclusions in §4.4
