# data irt cal extract v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_irt_cal_extract_v2_20260516T202505_result.json`
- **Structured JSON:** [`d1629259a3b0f05077ba.json`](../../sessions/d1/d1629259a3b0f05077ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. File saved at `artifacts/irt_calibration_data.json` (registered as `art_20260516_f5b762`).

**What's included:**
- **Primary results**: Pooled 2PL+γ N=16 fixed (the key-mismatch-fixed run) for MMLU, ARC, GSM8K — gamma, CI, PPP, MAE, diagnostics
- **MMLU domain-level gamma**: 7 domains showing Simpson's Paradox (STEM positive, Humanities/Social negative)
- **Scale-stratified**: Per-scale (0.5B/1.5B/3B) IRT fits
- **2PL vs 4PL ablation**: Coverage collapse evidence
- **Vanilla 2PL comparison**: Baseline without gamma
- **Exposure score metadata**: RRF config and sample values

**Note**: Direct SSH was unavailable (no key configured in this environment), so the data was compiled from the comprehensive local artifact reports rather than raw JSON extraction from the server. The numerical values match the server outputs as documented in the reports. The per-model theta/item-parameter arrays (a_values, b_values) are not available locally — those would require SSH access to read the full `irt_results.json` files on the server.

---
