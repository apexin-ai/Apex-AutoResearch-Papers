# analysis gpt2 detector auc

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt2-detector-auc_20260518T192753_result.json`
- **Structured JSON:** [`e0c985e9450cf8194432.json`](../../sessions/e0/e0c985e9450cf8194432.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`pretrain_weighted.py` reads `q_score` from the data (line 79: `item.get("q_score", 0.0)`). The GPT-2 scored data file already has a `q_score` column, so it's directly compatible.

## Results

| Metric | Value |
|--------|-------|
| **GPT-2 PPL Detector AUC** | **0.9130** |
| GPT-2 NLL AUC | 0.9130 |
| q_score AUC | 0.9130 |
| Total samples | 371,499 |
| Contaminated (depth=1) | 206,610 |
| Clean (depth=0) | 164,889 |

**Key findings:**

1. **AUC = 0.9130** — GPT-2 PPL is a strong contamination detector. Lower PPL = more likely generated (contaminated mean PPL=5.23, clean mean PPL=13.75).

2. **Column names in GPT-2 scored file:** `text`, `depth`, `source_model`, `prompt_tokens`, `generated_tokens`, `decoding`, `q_score`, `gpt2_ppl`, `gpt2_nll`

3. **`q_score` is derived from `gpt2_ppl`** — all three scores yield identical AUC (0.9130), confirming `q_score` in this file is a monotone transform of the GPT-2 PPL score (higher q_score = lower PPL = more contaminated).

4. **Compatible with `pretrain_weighted.py`** — the file has a `q_score` column and `pretrain_weighted.py` reads `item.get("q_score", 0.0)` at line 79. No `--score_column` parameter needed; the file works directly.

5. **Different from original detector's q_score** — the original `scored_data.jsonl` has different `q_score` values (e.g., first record: original=0.968 vs GPT-2=0.754), meaning they use different scoring methods but the same column name.

---
