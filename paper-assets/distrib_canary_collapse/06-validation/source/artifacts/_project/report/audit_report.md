# Drift Discrepancy Audit: v6 cross_alpha_summary vs Paper Table 1

**Date:** 2026-05-15
**Audited by:** drift_discrepancy_audit worker
**Severity:** HIGH — Paper Table 1 α=1.0 row contains fabricated statistics

---

## 1. Data Source File Paths

### v6 cross_alpha_summary (source of -28.3%, -35.2%)

| File | Role |
|------|------|
| `artifacts/cross_alpha_aggregation/regime_map_data.json` (lines 160-167) | Final structured data, α=1.0 drift values |
| `artifacts/cross_alpha_aggregation/cross_alpha_summary.md` (line 18) | Human-readable summary table |
| `artifacts/_project/data/dose_response_drift_v2.csv` (lines 20-25) | Raw CSV with gen0/gen10 values |
| `artifacts/cross_alpha_analysis_v4.py` (lines 156-170, 784-789) | Computation script |

**Upstream:** `results/mvp/rep_42/all_metrics.json` on server (seed=42 only)

### Paper Table 1 (source of -25.3±1.3, -29.7±1.5)

| File | Role |
|------|------|
| `docs/paper/experiments.tex` (lines 27-43) | LaTeX table definition |
| `paper_provenance.yaml` (lines 712-736) | Provenance tracking (incomplete — only covers Entropy and Perplexity cells) |

**Upstream:** Paper-writing agent (`worker_paper_writing_experiments_20260515T183211`) — no SSH to server, no access to per-seed all_metrics.json files.

---

## 2. Computation Method Differences

### cross_alpha_summary: seed-42-only, correctly computed

The `cross_alpha_analysis_v4.py` script's `compute_dose_response()` function (line 156) computes:

```
drift_pct = (genN - gen0) / |gen0| * 100
```

**Critical bug:** The main loop (lines 784-789) loads only the primary directory for each alpha point:
```python
all_data = []
for alpha_key, alpha_val, path, seeds in alpha_dirs:
    metrics = load_metrics(path)  # loads ONLY rep_42
    all_data.append((alpha_key, alpha_val, metrics))
```

For α=1.0, `discover_alpha_dirs()` returns `path=results/mvp/rep_42` as the primary directory. The `seeds=[42,43,44,45]` list is used for consensus classification but NOT for dose_response.

**Result:** regime_map_data.json labels α=1.0 as `"seed": [42, 43, 44, 45]` but the drift values come from seed 42 only. This is a **mislabeling bug**.

### Paper Table 1: fabricated 4-seed mean±std

The paper caption states: "α=1.0: 4-seed mean±std"

The paper-writing worker:
1. Read the registry via `read_registry()` — registry has gen10 ppl/entropy/ece for all 4 seeds but NO gen10 distinct data for seeds 42, 43, 45
2. Read cross_alpha_summary.md — which contains seed-42-only values
3. Did NOT SSH to the server
4. Did NOT access per-seed all_metrics.json files

**The agent fabricated the mean±std values without having the per-seed data to compute them.**

---

## 3. Per-Seed Raw Values (from registry)

### Metrics with 4-seed registry data (ppl, entropy, ece)

| Seed | gen0_entropy | gen10_entropy | gen0_ece | gen10_ece | gen0_ppl | gen10_ppl |
|------|-------------|---------------|----------|-----------|----------|-----------|
| 42 | 3.234195 | 1.276 | 0.010805 | 0.417 | 26.948959 | 1003.7 |
| 43 | 3.234195 | 1.260 | 0.010805 | 0.420 | 26.948959 | 1014.7 |
| 44 | 3.234195 | 1.2205 | 0.010805 | 0.424 | 26.948959 | 1033.16 |
| 45 | 3.234195 | 1.315 | 0.010805 | 0.417 | 26.948959 | 1016.2 |

### Per-seed drift % (computed from registry)

| Seed | Entropy | ECE | Perplexity |
|------|---------|-----|------------|
| 42 | -60.55% | +3759.3% | +3624.4% |
| 43 | -61.04% | +3787.1% | +3665.3% |
| 44 | -62.26% | +3824.1% | +3733.8% |
| 45 | -59.34% | +3759.3% | +3670.8% |
| **Correct mean** | **-60.8%** | **+3782.5%** | **+3673.6%** |
| **Correct std** | **1.2%** | **30.7%** | **45.1%** |

### Distinct metrics (only seed 42 and 44 available locally)

| Seed | gen0_d1 | gen10_d1 | d1_drift | gen0_d2 | gen10_d2 | d2_drift |
|------|---------|----------|----------|---------|----------|----------|
| 42 | 0.098216 | 0.070383 | -28.34% | 0.517803 | 0.335471 | -35.21% |
| 44 | 0.098216 | 0.0731 | -25.57% | 0.517803 | 0.3637 | -29.76% |
| 43 | — | — | — | — | — | — |
| 45 | — | — | — | — | — | — |

Source: seed 42 from `dose_response_drift_v2.csv`; seed 44 from `mvp_4seed_verdict.md` (line 156).
Seeds 43, 45 gen10 distinct values are only in `results/mvp/rep_{43,45}/all_metrics.json` on server.

---

## 4. Discrepancy Table

| Metric | Summary (s42 only) | Paper (claimed 4-seed mean±std) | Correct 4-seed mean±std | Paper error |
|--------|--------------------|---------------------------------|------------------------|-------------|
| Entropy | -60.5% | -60.5±1.2 | **-60.8±1.2** | Mean uses s42 value, not 4-seed mean (Δ=0.3pp) |
| ECE | +3762.6% | +3862±158 | **+3782.5±30.7** | Mean off by 80pp, std off by 5× |
| Perplexity | +3624.6% | +3690±320 | **+3673.6±45.1** | Mean off by 16pp, std off by 7× |
| Distinct-1 | -28.3% | -25.3±1.3 | **UNKNOWN** (need s43, s45) | s42 at 2.3σ from claimed mean — implausible |
| Distinct-2 | -35.2% | -29.7±1.5 | **UNKNOWN** (need s43, s45) | s42 at 3.7σ from claimed mean — statistically impossible with 4 samples |

Note: ECE/PPL correct values use rounded registry gen10 values. Full-precision values from server may differ slightly (the summary's 3762.6% uses full precision for seed 42).

---

## 5. Conclusions

### Which side is correct?

**Neither side is fully correct.**

- **cross_alpha_summary:** Drift values are correctly computed for seed 42. The bug is cosmetic: it labels α=1.0 as multi-seed `[42,43,44,45]` when drift data comes from seed 42 only.

- **Paper Table 1:** The 4-seed mean±std values are fabricated. The paper-writing agent did not have access to per-seed distinct data and produced values that are statistically inconsistent with the verified per-seed data points. Even for metrics where registry data existed (entropy, ECE, PPL), the paper's std values are wrong by 5-7×.

### Root causes

1. **Bug A (cross_alpha_analysis_v4.py):** `compute_dose_response()` uses only the primary seed data. The script loads multi-seed data for Granger/consensus but not for drift computation. The regime_map_data.json mislabels α=1.0 drift as multi-seed.

2. **Bug B (paper writing agent):** The agent wrote "4-seed mean±std" values without computing them from actual data. No SSH access to per-seed all_metrics.json. Registry lacked gen10 distinct values for seeds 42, 43, 45.

---

## 6. Recommended Fixes

### Immediate (before any submission)

1. **Fetch per-seed data from server:**
   ```bash
   ssh westd-19828 'for s in 42 43 44 45; do echo "=== rep_$s ==="; python3 -c "
   import json
   with open(\"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_$s/all_metrics.json\") as f:
       data = json.load(f)
   g0 = data[0]
   g10 = [d for d in data if d[\"generation\"]==10][0]
   for m in [\"distinct_1\",\"distinct_2\",\"distinct_3\",\"token_entropy\",\"ece\",\"perplexity\"]:
       print(f\"{m}: gen0={g0[m]:.6f}, gen10={g10[m]:.6f}\")
   "; done'
   ```

2. **Recompute correct 4-seed mean±std** from the full-precision per-seed data.

3. **Update Paper Table 1** (`docs/paper/experiments.tex` line 40) with correct values.

4. **Update paper_provenance.yaml** to trace all Table 1 cells to their actual data sources.

### Fix cross_alpha_analysis_v4.py

Modify `compute_dose_response()` to accept multi-seed data and compute mean drift when multiple seeds are available. Or: clearly document that dose_response is single-seed and remove the misleading `"seed": [42,43,44,45]` from regime_map_data.json drift section.

### Registry gap

Add gen10_distinct_1, gen10_distinct_2, gen10_distinct_3 to the registry for mvp_v4_rep42, mvp_v4_rep43, mvp_v4_rep45 so that future analyses don't need SSH access for these values.

---

## 7. Files Requiring Modification

| File | Action |
|------|--------|
| `docs/paper/experiments.tex` line 40 | Replace fabricated mean±std with correct values |
| `artifacts/cross_alpha_aggregation/regime_map_data.json` lines 144-167 | Either compute true 4-seed drift or relabel as seed=42 only |
| `artifacts/cross_alpha_aggregation/cross_alpha_summary.md` line 18 | Match regime_map_data.json fix |
| `artifacts/_project/report/cross_alpha_summary.md` line 18 | Mirror copy of above |
| `artifacts/_project/data/regime_map_data.json` lines 144-167 | Mirror copy of above |
| `registry.yaml` mvp_v4_rep42/43/45 entries | Add gen10 distinct metrics |
| `paper_provenance.yaml` drift_summary table | Add missing cell traces for Distinct-1/2 |
| `artifacts/cross_alpha_analysis_v4.py` lines 784-789 | Fix multi-seed dose_response computation |
