# code exp 016 semi real better cm

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-016-semi-real-better-cm_20260521T132011_result.json`
- **Structured JSON:** [`a726d4ef2cbe29c8218a.json`](../../sessions/a7/a726d4ef2cbe29c8218a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs verified:
- CSV: 9601 lines (9600 data + 1 header) = 100 × 3 × 4 × 2 × 4 = 9600 rows
- Analysis MD written

## Results Summary

**Model selected**: gpt-3.5-turbo (worst-subgroup FNR=0.211). Higher FPR (0.14–0.39) than GPT-4.1 (0.05–0.19) but much lower FNR (0.15–0.21 vs 0.22–0.53).

**Key findings — despite lower FNR, results are worse than exp-015**:

| n_expert | Method | exp-016 RMSE | exp-015 RMSE | exp-016 Cov | exp-015 Cov |
|---|---|---|---|---|---|
| 100 | naive | 0.1274 | 0.1230 | 0.784 | 0.879 |
| 100 | global_corrected | 0.2652 | 0.2631 | 0.893 | 0.885 |
| 100 | hb_ec_hte | **0.9295** | **0.7842** | 0.769 | 0.744 |
| 500 | global_corrected | 0.1991 | 0.1963 | 0.939 | 0.922 |
| 500 | hb_ec_hte | **0.3222** | **0.2599** | 0.894 | 0.890 |

- **HB EC-HTE is consistently worse than global_corrected** at all n_expert levels (same pattern as exp-015)
- **Naive coverage drops** to 0.784 (from 0.879 in exp-015), because higher FPR creates more misclassification bias in the z=1 stratum despite lower FNR
- **Global corrected outperforms HB** because the higher FPR variation across subgroups (0.14–0.39) makes subgroup-level CM estimation harder with limited expert data — the HB sampler struggles more with this asymmetry
- **Bright spot for HB**: at n_expert=500, S0/z=1, HB actually beats global (|bias| 0.19 vs 0.25) — the one case where subgroup-specific correction helps

The experiment confirms that lower FNR alone doesn't help; the higher FPR variance across subgroups makes the correction problem harder overall.

---
