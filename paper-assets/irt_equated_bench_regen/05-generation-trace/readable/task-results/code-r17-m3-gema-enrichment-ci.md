# code r17 m3 gema enrichment ci

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r17_m3_gema_enrichment_ci_20260522T160033_result.json`
- **Structured JSON:** [`4df664c9a6c4f3fcd056.json`](../../sessions/4d/4df664c9a6c4f3fcd056.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three outputs produced. Summary of results:

**DIF-C × Gema MMLU-Redux Error Enrichment:**
- Universe: 5,069 items (vs task's expected ~4,802 — difference due to the original R14-SF5 having applied a li_label filter)
- Enrichment = **1.10×** (slightly above 1.0, not below)
- Bootstrap 95% CI: **[0.92, 1.27]** — includes 1.0
- Fisher exact: OR=1.156, p=0.235
- φ = 0.017

The CI comfortably spans 1.0, consistent with the Fisher p=0.235. DIF-C items are not significantly enriched among Gema-annotated error items. The point estimate differs from the R14-SF5 value (0.92×) because that analysis applied an additional `li_label` filter reducing the universe; the current analysis uses the natural DIF × Redux join.

Outputs:
- Script: `artifacts/r17_gema_enrichment_ci/gema_enrichment_ci.py`
- CSV (1000 bootstrap reps): `artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_results.csv`
- Report: `artifacts/r17_gema_enrichment_ci/gema_enrichment_ci_report.md`

---
