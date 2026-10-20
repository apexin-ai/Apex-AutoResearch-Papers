# 4B Duplication + Truncation + Capacity Valley Analysis

## 1. Duplication Rate Table (All Models)

| Model | Condition | Raw preds | Unique preds | Dup rate | Docs w/dups |
|-------|-----------|-----------|-------------|----------|-------------|
| Qwen3-1.7B | With-Evidence | 17,184 | 11,500 | 33.1% | 399 |
| Qwen3-1.7B | No-Evidence | 26,157 | 10,332 | 60.5% | 579 |
| **Qwen3-4B** | **With-Evidence** | **16,880** | **11,626** | **31.1%** | N/A* |
| **Qwen3-4B** | **No-Evidence** | **21,181** | **12,025** | **43.2%** | **345** |
| Qwen3-8B | With-Evidence | 17,401 | 12,322 | 29.2% | 308 |
| Qwen3-8B | No-Evidence | 19,948 | 13,382 | 32.9% | 284 |
| LLaMA-3.1-8B | With-Evidence | 15,325 | 12,375 | 19.2% | 226 |
| LLaMA-3.1-8B | No-Evidence | 18,466 | 13,358 | 27.7% | 240 |

*4B with-evidence: No predictions.json, dup rate computed from metrics (n_predictions vs pred_count). Docs w/dups unavailable.

### Duplication Rate Pattern (with-evidence → no-evidence increase)
- 1.7B: 33.1% → 60.5% (+27.4pp) — massive degeneration without evidence
- 4B: 31.1% → 43.2% (+12.1pp) — moderate increase
- 8B: 29.2% → 32.9% (+3.7pp) — minimal increase
- LLaMA-8B: 19.2% → 27.7% (+8.5pp) — moderate

## 2. Truncation Crossover

### Qwen3-1.7B (per-doc)
| Category | Count | Evi F1 | NoEvi F1 | Delta |
|----------|-------|--------|----------|-------|
| Both truncated | 272 | 0.3072 | 0.2368 | -7.04pp |
| Only evi truncated | 42 | 0.3909 | 0.4833 | +9.24pp |
| Only noevi truncated | 229 | 0.5370 | 0.3431 | -19.40pp |
| Neither truncated | 442 | 0.6319 | 0.5704 | -6.16pp |

### Qwen3-4B (aggregate only, no per-doc crossover)
- With-evi truncated: 288/985 (29.2%)
- No-evi truncated: 307/985 (31.2%)

### Qwen3-8B (per-doc)
| Category | Count | Evi F1 | NoEvi F1 | Delta |
|----------|-------|--------|----------|-------|
| Both truncated | 168 | 0.3308 | 0.2987 | -3.21pp |
| Only evi truncated | 145 | 0.4013 | 0.5248 | +12.35pp |
| Only noevi truncated | 57 | 0.5310 | 0.3577 | -17.33pp |
| Neither truncated | 615 | 0.6147 | 0.6116 | -0.31pp |

### LLaMA-3.1-8B (per-doc)
| Category | Count | Evi F1 | NoEvi F1 | Delta |
|----------|-------|--------|----------|-------|
| Both truncated | 88 | 0.3602 | 0.3615 | +0.13pp |
| Only evi truncated | 109 | 0.4025 | 0.5448 | +14.23pp |
| Only noevi truncated | 94 | 0.5130 | 0.3643 | -14.87pp |
| Neither truncated | 694 | 0.6134 | 0.6161 | +0.27pp |

## 3. Document Complexity Interaction (Truncation by Gold Triple Bin)

### 4B No-Evidence
| Bin | Docs | Truncated | Rate |
|-----|------|-----------|------|
| 0-5 | 154 | 15 | 9.7% |
| 6-10 | 323 | 52 | 16.1% |
| 11-20 | 370 | 154 | 41.6% |
| 21+ | 138 | 86 | 62.3% |

### Full Cross-Model Comparison

**With-Evidence Truncation Rate by Complexity Bin:**
| Bin | 1.7B | 4B | 8B | LLaMA-8B |
|-----|------|-----|-----|----------|
| 0-5 | 8.4% | 29.2%* | 5.2% | 5.2% |
| 6-10 | 16.4% | — | 17.0% | 8.7% |
| 11-20 | 39.7% | — | 39.5% | 24.3% |
| 21+ | 73.2% | — | 75.4% | 51.4% |

*4B with-evidence: only aggregate available (288/985 = 29.2%)

**No-Evidence Truncation Rate by Complexity Bin:**
| Bin | 1.7B | 4B | 8B | LLaMA-8B |
|-----|------|-----|-----|----------|
| 0-5 | 13.0% | 9.7% | 5.2% | 3.2% |
| 6-10 | 38.1% | 16.1% | 9.9% | 12.7% |
| 11-20 | 66.2% | 41.6% | 28.1% | 20.5% |
| 21+ | 81.9% | 62.3% | 58.7% | 43.5% |

## 4. Capacity Valley Verification

### 4B Summary
- With-evidence Ign-F1: 0.3974
- No-evidence Ign-F1: 0.4721
- **Evidence Tax: +7.47pp** (highest among all models)
- Recall gain (no-evi): +8.89pp
- Dup rate: 31.1% (with-evi) → 43.2% (no-evi)

### Cross-Model Evidence Tax
| Model | WE dup% | NE dup% | Tax (pp) | WE trunc | NE trunc |
|-------|---------|---------|----------|----------|----------|
| Qwen3-1.7B | 33.1% | 60.5% | -8.04 | 314/985 | 501/985 |
| **Qwen3-4B** | **31.1%** | **43.2%** | **+7.47** | **288/985** | **307/985** |
| Qwen3-8B | 29.2% | 32.9% | +0.28 | 313/985 | 225/985 |
| LLaMA-3.1-8B | 19.2% | 27.7% | +0.68 | 197/985 | 182/985 |

### Capacity Valley Narrative
- **1.7B (below valley)**: Evidence acts as regularizer. Without it, model degenerates (60.5% dup, 501 truncated). Tax is negative because evidence constrains degeneration.
- **4B (IN the valley)**: Evidence is pure overhead. Low dup (31.1%), moderate truncation, but highest tax (+7.47pp). Model has enough capacity to avoid degeneration without evidence, but not enough to handle evidence efficiently.
- **8B+ (above valley)**: Near-zero tax. Enough capacity for both tasks.

## 5. Config Check: 1.7B base_model Field

CONFIRMED: Both 1.7B eval configs have incorrect base_model field:
- `qwen3_1_7b_sft_eval`: base_model = `/root/autodl-tmp/models/Qwen3-4B` (WRONG, should be Qwen3-1.7B)
- `qwen3_1_7b_no_evidence_eval_v3`: base_model = `/root/autodl-tmp/models/Qwen3-4B` (WRONG)
- model_path is correct: `/root/autodl-tmp/models/Qwen/Qwen3-1.7B`
- This is a metadata error only. The actual model loaded is Qwen3-1.7B (via model_path).

## Missing Data
- 4B with-evidence predictions.json not saved (older eval code version). Need to re-run eval with --save_predictions to get per-doc crossover analysis.
- Until then, only aggregate stats available for 4B with-evidence condition.
