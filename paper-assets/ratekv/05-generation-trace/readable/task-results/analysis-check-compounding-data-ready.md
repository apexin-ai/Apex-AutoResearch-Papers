# analysis check compounding data ready

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_compounding_data_ready_20260516T023620_result.json`
- **Structured JSON:** [`9567af09bad03a199bad.json`](../../sessions/95/9567af09bad03a199bad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full assessment:

---

## 1. llama_compounding_sweep — FULLY INTEGRATED

| Item | Status |
|------|--------|
| **Registry** | DONE, success (registry.yaml:3497) |
| **Metrics** | k=0→8.09, k=8→8.23, k=64→11.99, k=128→40.21, k=256→1519.19 |
| **Checkpoint** | `/root/ratekv/artifacts/llama_compounding_sweep_results.json` (server) |
| **Local artifact** | `artifacts/llama_compounding_sweep/data/llama_compounding_sweep_summary.txt` |
| **Paper figure** | Hardcoded in `generate_compounding_curves.py:38-39`, rendered as `fig_compounding_curves.pdf` |
| **Paper text** | `experiments.tex:103` — numbers match exactly |
| **Action needed** | None |

## 2. mistral_compounding_sweep — FULLY INTEGRATED (with stale JSON)

| Item | Status |
|------|--------|
| **Registry** | DONE, success. V1 (registry.yaml:3528) + V2 bf16_2bitonly (registry.yaml:3701) |
| **Paper uses V2 data** | k256=45.28 (V2) not k256=7.59 (V1) |
| **Figure script** | `generate_compounding_curves.py:48` uses V2 values (45.28) — correct |
| **Paper text** | `experiments.tex:105` — "reaches only 45.28 at k=256 (6.4×)" — matches V2 |
| **Stale file** | `compounding_curves_data.json` contains V1 data (k256=7.59) — NOT used by figure script, but misleading if someone reads it directly |
| **Action needed** | Optional: update `compounding_curves_data.json` to V2 values for consistency |

## 3. llama_3seed_downstream_ci — INTEGRATED, minor paper update possible

| Item | Status |
|------|--------|
| **Registry** | DONE, success (registry.yaml:4039) |
| **Metrics** | ARC-C: -0.8, HS: 0.0, PIQA: -0.1, WG: +0.5, Avg: -0.1 |
| **Key finding** | Single profile → deterministic allocation → **all 3 seeds identical (std=0)** |
| **Checkpoint** | `/root/ratekv/artifacts/llama_3seed_downstream_ci_results.json` (server) |
| **Table 4** | `experiments.tex:123` — "Llama-3.1-8B: -0.8, +0.0, -0.1, +0.5, -0.1" — **values match** |
| **No ±σ shown** | Correct, since std=0. But table caption only mentions Qwen 3-seed; doesn't note Llama also ran 3 seeds |

### Issues to address

1. **`conclusion.tex:21`** says "no confidence intervals are reported for the current single-seed results" — **outdated**. Qwen has 3-seed CI, Llama 3-seed confirms std=0. Should update to something like: "Qwen downstream is reported with 3-seed CI; Llama 3-seed yields identical results (single-profile determinism); Yi, Mistral, and Gemma-2 remain single-seed."

2. **Table caption** (`experiments.tex:115`) says "Qwen values are mean over 3 calibration seeds (±1σ)" — could add: "Llama 3-seed results are identical (single-profile determinism) and reported without error bars."

3. **`compounding_curves_data.json`** has stale V1 Mistral data — not blocking (figure bypasses it) but a housekeeping inconsistency.

### Summary

All three experiments' data are **already integrated** into the paper figures and tables with correct values. No new figures need to be generated. The only actionable items are minor text updates to `conclusion.tex` (limitation statement) and optionally the table caption to reflect the Llama 3-seed determinism finding.

---
