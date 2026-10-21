# code exp 008 signal survival

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_008_signal_survival_20260514T151607_result.json`
- **Structured JSON:** [`1211afabafbf711250a8.json`](../../sessions/12/1211afabafbf711250a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run passes end-to-end. All outputs generated successfully:

```
Signal                       Base          SFT-clean         SFT-contam         RL-aligned
------------------------------------------------------------------------------------------
Embedding      0.994 [0.984,1.000] 0.895 [0.788,0.977] 0.506 [0.280,0.748] 0.234 [0.091,0.408]
Min-K%++       0.977 [0.945,0.996] 0.881 [0.795,0.969] 0.597 [0.386,0.816] 0.254 [0.118,0.378]
ConStat                       N/A                N/A                N/A                N/A
Self-Critique  0.984 [0.956,1.000] 0.782 [0.602,0.927] 0.527 [0.307,0.744] 0.344 [0.091,0.603]
```

Mock data shows the expected pattern: signal AUC degrades from Base→RL-aligned (delta ~0.6-0.76). Reports saved (`survival_report.json`, `auc_summary.json`) and all PDF plots generated (heatmaps per benchmark + aggregate + trajectory).

Pipeline is validated. Next steps when ready:
- `--exp002-only --skip-compute` to run on real exp-002 signal data (d000/d005)
- Full pipeline with `--gpu 0` to compute signals on base + Instruct models

---
