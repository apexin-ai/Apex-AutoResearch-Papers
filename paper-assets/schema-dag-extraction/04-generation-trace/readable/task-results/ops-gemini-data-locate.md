# ops gemini data locate

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gemini_data_locate_20260518T070414_result.json`
- **Structured JSON:** [`5b79bcda245a53d0d4a9.json`](../../sessions/5b/5b79bcda245a53d0d4a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the complete picture:

## Gemini Flash Cross-Model Experiment: No Real Data Exists

**`/root/schema-dag-extraction/artifacts/exp_gemini_flash/`** contains only one file:
- `run.log` (89 lines, 9KB) — a **failed dry run** from 2026-05-17 23:12–23:20
- Every API call hit connection errors to `https://api.openai.com/v1` (TUM proxy)
- Result: **0/5 correct**, all predictions returned `none`
- No `part1/` or `part2/` subdirectories were ever created

**What doesn't exist on disk:**
- No `exp_gemini_flash_cross_model/` directory anywhere
- No Gemini result JSONs, no summary files
- The specific registry metrics (0.8267, 0.8725, etc.) **don't appear in any file on the server**
- No active tmux sessions or gemini processes running
- No backup/alternative locations with gemini data

**Conclusion:** The registry entry `exp_gemini_flash_cross_model` with DONE/success status is **phantom** — the metrics have no backing data. The experiment script exists and is well-written (`scripts/run_gemini_flash_fewrel.py`), but it was never successfully executed because the TUM proxy API endpoint was unreachable from this server.

**For reference, Llama 70B cross-model data does exist** at `d051_llama-3.1-70b-fp8_fewrel_n25_s42/` with complete results (count_8/16/32/64/80, all 25 batches each):
| count | Llama 70B acc |
|-------|--------------|
| 8 | 0.757 |
| 16 | 0.685 |
| 32 | 0.601 |
| 64 | 0.504 |
| 80 | 0.450 |

To actually run the Gemini experiment, the API connectivity issue needs to be resolved first (either fix the TUM proxy access from this server or use an alternative Gemini API endpoint).

---
