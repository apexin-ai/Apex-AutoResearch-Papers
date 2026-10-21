# code exp 058 ddr causality

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_058_ddr_causality_20260520T070624_result.json`
- **Structured JSON:** [`577a43bd79841846a48b.json`](../../sessions/57/577a43bd79841846a48b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the summary:

---

**Script deployed and validated on bjb2-18868 (cuda:1)**

| Item | Status |
|------|--------|
| Script | `/root/gen-depth-fingerprint/scripts/ddr_causal_analysis.py` — 444 lines, 3 modules implemented |
| Data | `/root/gen-depth-fingerprint/data/features_8gen.csv` — 37,058 rows, 8 generators, depths 0-4 |
| Dependencies | xgboost 3.2.0, sklearn 1.8.0, statsmodels, scipy — all installed |
| Dry-run permutation | passed (75 rows, 8 folds, no errors/warnings) |
| Dry-run granger | passed (59 panel obs, F-test + Fisher's method working) |

**Execution commands** (full run, waiting for approval):

```bash
# Permutation importance (~15 min, CPU-only, n_repeats=50)
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/gen-depth-fingerprint
nohup python scripts/ddr_causal_analysis.py --module permutation --n-repeats 50 \
  --output results/ddr_causal_permutation.json > /tmp/ddr_perm.log 2>&1 &

# Granger causality (~2 min, CPU-only)
nohup python scripts/ddr_causal_analysis.py --module granger \
  --output results/ddr_causal_granger.json > /tmp/ddr_granger.log 2>&1 &

# Feature intervention (~45 min, CPU-only, n_repeats=30, trains 8×7×30=1680 XGB models)
nohup python scripts/ddr_causal_analysis.py --module intervention --n-repeats 30 \
  --output results/ddr_causal_intervention.json > /tmp/ddr_intervention.log 2>&1 &
```

**Estimated time**: Granger ~2min, Permutation ~15min, Intervention ~45min. All CPU-bound (no GPU needed). Can run all 3 in parallel.

---
