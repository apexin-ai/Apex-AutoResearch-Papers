# fix a060 s43 metrics backfill

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_a060_s43_metrics_backfill_20260519T185811_result.json`
- **Structured JSON:** [`9325a99053e8da6e4da7.json`](../../sessions/93/9325a99053e8da6e4da7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验 metrics 均已回填成功：

**alpha_sweep_a060_s43_fp32** — PermG FDR 0/8 (fwd+rev), K≥4=3/8, K≥3=7/8, threshold_onset=8/8, naive_xcorr=7/8, diff_xcorr=6/8, TY=4/8, 含全部 drift_pct + gen0/gen9 绝对值 + D108 non-monotonicity note。

**interv_react_s43_fp32** — trigger_gen=2, d1 drop=-15.83%, gen2_ppl=158.22, recovery_ppl=21.98 (gen3), recovery_complete_by_gen=3, 含 gen0/gen9/gen10 绝对值 + intervention config + recovery note。

---
