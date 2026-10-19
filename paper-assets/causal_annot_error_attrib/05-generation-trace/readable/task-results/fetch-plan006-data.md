# fetch plan006 data

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fetch_plan006_data_20260520T232516_result.json`
- **Structured JSON:** [`c584a2cea8ddfab4cc91.json`](../../sessions/c5/c584a2cea8ddfab4cc91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Here's a summary of what was extracted:

**Files on remote server** (`/home/sonny/causal_annot_error_attrib/artifacts/plan006/`):
- `asv_empirical_results.json` — 121,851 bytes (complete, fetched via `ssh_fetch_file`)
- `f1_vs_bias.png` — 174,444 bytes
- `asv_heatmap.png` — 73,701 bytes  
- `plan006_humaid_run.log` — 2,905 bytes

**Data extracted** (saved to `artifacts/plan006_empirical_data.txt`, 178KB, 6026 lines):
- 9 confusion matrices (llama4/qwen3/deepseek × zero-shot/few-shot-3/few-shot-5, K=10 HumAID)
- 63 bias records across 7 topologies
- 189 ASV values (32 magnitude non-null, 2 significance non-null, 0 sign-flip)
- 63 F1-vs-bias records
- 63 Type I/II error records (31/63 ASV-unsafe)
- Inter-model error correlation (9 prompt×dataset pairs)
- Complete raw JSON embedded

**Artifact registered**: `art_20260520_505323`

---
