# data irt extraction

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_irt_extraction_20260516T202646_result.json`
- **Structured JSON:** [`e493d79e2cf9f8614ed1.json`](../../sessions/e4/e493d79e2cf9f8614ed1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

File successfully extracted and saved at:
`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/irt_calibration_data.json`

The worker compiled data from local artifact reports (direct SSH was unavailable from this environment). Contents:

- **Source**: `pooled_irt_2pl_gamma_n16_fixed` (N=16 fixed run)
- **3 benchmarks** (mmlu, arc_challenge, gsm8k) with gamma posteriors, CI, PPP, MAE
- **Earlier N=13/21 run** from `results_pooled_n20`
- **7 MMLU domains** with per-domain gamma (Simpson's Paradox: STEM positive, Humanities/Social negative)
- **Scale-stratified** results (0.5B, 1.5B, 3B per benchmark)
- **2PL vs 4PL ablation** (2PL resolves 4PL coverage collapse)
- **Exposure scores** metadata (RRF composite, 3 scales × 3 signals)
- **Stan config** (4 chains, 1000 warmup/samples, adapt_delta=0.95)

Note: The structure deviates slightly from the requested schema because the data was assembled from local reports rather than raw server JSON. The per-model `theta` and `item_params` arrays weren't available in the local artifacts — those would require direct SSH access to the server's raw IRT output files.

---
