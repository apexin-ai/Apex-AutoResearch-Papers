# analysis phase2 hellaswag 2temp fix

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_hellaswag_2temp_fix_20260521T230301_result.json`
- **Structured JSON:** [`559562ad80a2a2474254.json`](../../sessions/55/559562ad80a2a2474254.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All other benchmarks are clean. The bug was isolated to the 8-model HellaSwag analysis (JSONL float `0.7000000000000001` + binary blob float `0.7` → 3 phantom temp levels).

---

## Results Summary

### Temperature Diagnosis

| Model | T=0.0 | T=0.3 | T=0.7 | Total |
|-------|-------|-------|-------|-------|
| Llama-3.1-8B | 28,800 | 0 | 28,800 | 57,600 |
| Qwen3-8B | 28,800 | 0 | 28,800 | 57,600 |
| Mistral-7B-v0.3 | 28,800 | 0 | 28,800 | 57,600 |
| Gemma-2-9B | 28,800 | 0 | 28,800 | 57,600 |
| DeepSeek-7B | 28,800 | 0 | 28,800 | 57,600 |
| InternLM2.5-7B | 28,800 | 0 | 28,800 | 57,600 |
| OLMo-2-7B | 28,800 | 0 | 28,800 | 57,600 |
| Yi-1.5-9B | 28,800 | 0 | 28,800 | 57,600 |

**No T=0.3 contamination in raw data.** Root cause: `pd.read_json` parses JSON `0.7` as `np.float64(0.7000000000000001)`. After `.astype(str)`, this became `"0.7000000000000001"` ≠ `"0.7"` (from OLMo/Yi binary), creating a phantom 3rd temperature with zero-filled tensor cells → massive artificial temperature variance.

### Variance Decomposition: 3-temp (broken) vs 2-temp (fixed)

| Component | 3-temp % | 2-temp % | Change |
|-----------|----------|----------|--------|
| **item_id** | **8.91%** | **34.27%** | +25.4pp |
| model:item_id | 10.84% | 36.00% | +25.2pp |
| model:temperature | 36.44% | 0.04% | -36.4pp (artifact) |
| temperature | 20.80% | 0.02% | -20.8pp (artifact) |
| residual | 17.81% | 21.41% | +3.6pp |
| model | 0.00% | 5.35% | +5.4pp |
| prompt_template:item_id | 0.63% | 2.14% | +1.5pp |
| ordering:item_id | 0.00% | 0.00% | ✓ confirmed zero |

### G_item

| Metric | 3-temp (broken) | 2-temp (fixed) |
|--------|-----------------|----------------|
| G_item | 0.7510 | **0.8716** |
| 95% CI | [0.719, 0.780] | **[0.843, 0.897]** |
| σ²(τ) | 0.0270 | 0.0705 |
| σ²(δ) | 0.0090 | 0.0104 |

### Fix applied
- Script: `scripts/hellaswag_2temp_gstudy_v2.py` — adds `df["temperature"] = df["temperature"].round(1)` before `.astype(str)`
- Output: `results/exp004_8model_analysis/per_benchmark_gstudy_hellaswag_2temp.json`
- N = 460,800 (8 × 2 × 6 × 6 × 4 × 200) ✓
- Bootstrap: 500 iterations
- ordering:item_id = 0% across all 8 models ✓

---
