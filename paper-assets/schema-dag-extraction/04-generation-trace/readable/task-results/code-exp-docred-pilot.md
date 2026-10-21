# code exp docred pilot

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_docred_pilot_20260516T040940_result.json`
- **Structured JSON:** [`df9d54783cc23cbc943d.json`](../../sessions/df/df9d54783cc23cbc943d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pilot complete. Here's the summary:

---

## DocRED Confusability Pilot — Complete

**Experiment**: `exp_docred_confusability` | **Status**: DONE (success)

### Results (Count Curve)

| Count | Mean Accuracy | Batches | BCS Range |
|-------|-------------|---------|-----------|
| 4 | **75.0%** | 100%, 55%, 70% | 0.58–0.86 |
| 16 | **56.7%** | 51.3%, 64.9%, 53.8% | 0.77–0.84 |
| 64 | **42.6%** | 44.0%, 39.1%, 44.6% | 0.92–0.99 |

### Key Findings
- Clear monotone count→accuracy degradation on DocRED (96 relation types)
- Pattern matches FewRel (80 types): more candidate types = lower accuracy
- Within count_4, BCS correlates with accuracy (BCS=0.58 → 100% vs BCS=0.86 → 55%)
- All accuracies well above random baseline (1/count), pipeline works correctly
- Total runtime: ~80s (1240 inferences), model: Qwen3-32B-FP8

### Artifacts on Server (`cqa1-38874:/root/schema-dag-extraction/artifacts/exp_docred_confusability/`)
- `scs_matrix.npy` — 96×96 SCS matrix
- `scs_matrix.pt` — PyTorch format with type_names/type_to_idx
- `pilot_results.json` — structured results
- `predictions.json` — full per-sample predictions (1240 entries)
- `eval_results.json` — per-batch evaluation

### Code
- `src/run_docred.py` — full pipeline (data loading, SCS, batch construction, vLLM inference, evaluation)
- Data: `data/docred/{dev.json, train_annotated.json, rel_info.json}`

---
