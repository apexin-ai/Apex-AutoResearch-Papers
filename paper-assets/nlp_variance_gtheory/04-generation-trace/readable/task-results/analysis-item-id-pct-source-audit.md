# analysis item id pct source audit

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_item_id_pct_source_audit_20260521T205635_result.json`
- **Structured JSON:** [`f8213b799d0eabd04cab.json`](../../sessions/f8/f8213b799d0eabd04cab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have the complete picture. Here's the audit.

---

## Audit Results: item_id% Number Tracing

### Method Discrepancy Found

Two different methods are mixed across analysis files:
- **SS proportion** (Type III SS / SS_total) — used by `gstudy_full.py`, `exp001b_gstudy.py`
- **Henderson I** (EMS-based variance component estimates) — used by corrected scripts that regenerated `llama_single_model_gstudy.json` and `exp001b_resampling_gstudy.json`

The paper claims "Henderson Method I" (experiments.tex:9) but most reported numbers come from SS proportion.

---

### 1. **54.85%** — `results/analysis/llama_single_model_gstudy.json`

| Field | Value |
|---|---|
| Source file | `llama_single_model_gstudy.json` → `correct.components_pct.item_id = 54.8479` |
| Method | **Henderson I** (corrected script, regenerated file) |
| Facets | 6-facet: precision, temperature, prompt_template, seed, ordering, item_id |
| Data | exp001_llama full (239,200 records, 1,196 conditions, 200 items, all 3 precisions) |
| G_item | 0.9184 (Henderson I G coefficient) |

**This file was regenerated with Henderson I after the ICC bug fix.** The original output from `gstudy_full.py` (SS proportion) gave 61.1%.

---

### 2. **61.1%** — Original SS-proportion analysis (overwritten)

| Field | Value |
|---|---|
| Original source | `gstudy_full.py` output (SS-proportion method, now overwritten) |
| Preserved in | Registry note: "item_id%=61.1%", `bernoulli_adjustment.json` → `mmlu_exp001b_baseline.item_id_pct_raw = 61.08` |
| Method | **SS proportion** (SS_item_id / SS_total), NOT Henderson I |
| Data | Same exp001_llama data |
| Original G_item | 0.6108 (ICC = item_id% / 100 — the bug) |

The registry note said "Variance percentages (item_id%=61.1%) are correct — only G_item affected." This was **incorrect**: the file was later regenerated with Henderson I, changing percentages to 54.85%.

**The paper currently uses 61.1% (experiments.tex:11) alongside G = 0.918 (experiments.tex:13). These are from different methods** — SS proportion and Henderson I respectively. Internally consistent pairs:
- Henderson I: item_id = **54.85%**, G = **0.918**
- SS proportion: item_id = 61.1%, G = 0.611

---

### 3. **74.48%** — Registry mean of SS-proportion resampling values

| Field | Value |
|---|---|
| Source | Registry `exp001b_resampling.metrics.item_id_pct_mean = 74.48` |
| Computation | Mean of SS-proportion per-sample values: (75.88 + 75.38 + 72.18) / 3 |
| Method | **SS proportion** (from `bernoulli_adjustment.json`, which read OLD exp001b file) |
| Current Henderson I mean | **71.59%** (from current `exp001b_resampling_gstudy.json`) |

---

### 4. **75.9 / 75.4 / 72.2%** — Paper's resampling numbers (experiments.tex:142)

| Field | Value |
|---|---|
| Source | `bernoulli_adjustment.json` → `resampling_samples` (75.88, 75.38, 72.18 rounded) |
| Method | **SS proportion** — read from OLD exp001b_resampling_gstudy.json before Henderson I correction |
| Current Henderson I values | **73.18, 72.57, 69.00** (from current `exp001b_resampling_gstudy.json`) |
| G_item in paper | "CV = 0.5%" matches Henderson I G values (0.9637, 0.9620, 0.9548) |

**The paper mixes SS-proportion percentages (75.9/75.4/72.2) with Henderson I G values (CV = 0.5%).** The SS-proportion G values would be 0.759/0.754/0.722 with CV ≈ 2.7%.

---

### 5. Cross-model numbers (42.1%, 33.6%) — CORRECT

| Field | Value |
|---|---|
| Source | `dataset_a4_gstudy.json` → `variance_components_ems` |
| Method | **Henderson I** with 200-resample bootstrap CIs |
| Data | 4 models × BF16 × 345,600 records |
| G_item | 0.820 [0.782, 0.861] |

These are properly Henderson I and match the paper exactly. No issues.

---

### Summary Table

| Number | In Paper? | Source File | Method | Henderson I Equivalent |
|---|---|---|---|---|
| 54.85% | No | `llama_single_model_gstudy.json` | Henderson I | ← this IS Henderson I |
| 61.1% | Yes (§4.1) | Original gstudy_full.py (overwritten) | SS proportion | **54.85%** |
| 74.48% | No (registry) | bernoulli_adjustment.json mean | SS proportion | **71.59%** |
| 75.9/75.4/72.2% | Yes (§4.6) | bernoulli_adjustment.json | SS proportion | **73.18/72.57/69.00%** |
| 42.1% | Yes (§4.2) | dataset_a4_gstudy.json | Henderson I | ← already correct |

---

### Recommendation

The paper should use Henderson I numbers consistently throughout:

1. **§4.1 Single-model baseline**: Change 61.1% → **54.85%**. Update interaction percentages to match Henderson I (precision×item 6.1%, seed×item 5.4%, prompt×item 5.3%, temp×item 2.6%). G = 0.918 is already correct.

2. **§4.6 Robustness resampling**: Change 75.9/75.4/72.2% → **73.2/72.6/69.0%** (CV = 2.6%). G_item CV = 0.4% (unchanged). The "higher item share relative to the 6-facet baseline (61.1%)" should reference 54.85%.

3. **§4.2 cross-model**: Already Henderson I. The drop from single-model to cross-model becomes **54.85% → 42.1%** (−12.7pp) instead of 61.1% → 42.1% (−19.0pp). Still a meaningful drop.

4. **Registry**: Update `exp001b_resampling.metrics.item_id_pct_mean` from 74.48 → 71.59.

5. **Stale files**: `exp001_llama_bf16only_5facet.json` still uses ICC (G_item = 0.74). `bernoulli_adjustment.json` contains SS-proportion values. Both need regeneration or flagging.

---
