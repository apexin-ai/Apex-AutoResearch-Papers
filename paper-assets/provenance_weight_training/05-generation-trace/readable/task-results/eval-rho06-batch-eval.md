# eval rho06 batch eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_rho06_batch_eval_20260518T102556_result.json`
- **Structured JSON:** [`eec0d1310498a64dbc22.json`](../../sessions/ee/eec0d1310498a64dbc22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval Results (ρ=0.6, Qwen3-0.6B, 5000 docs, 4,077,068 tokens)

| Experiment | Loss | PPL | Tokens | Time |
|---|---|---|---|---|
| `contamination_60_seed123` (ESS-only, seed123) | 2.8754 | **17.732** | 4,077,068 | 195s |
| `contamination_60_uniform_seed123` (Uniform, seed123) | 2.8766 | **17.754** | 4,077,068 | 168s |
| `contamination_60_random_seed42` (Random, seed42) | 2.8810 | **17.832** | 4,077,068 | 168s |
| `contamination_60_grid_b0_3_seed42` (Grid b0.3/Adaptive, seed42) | 2.8698 | **17.634** | 4,077,068 | 168s |

### Comparison with expected seed42 results

| Method | seed42 expected | This eval | Match? |
|---|---|---|---|
| ESS-only | 17.770 | 17.732 (seed123) | seed123 vs seed42, lower |
| Uniform | 17.763 | 17.754 (seed123) | seed123 vs seed42, close |
| Random | 17.832 | 17.832 (seed42) | **exact match** |
| Adaptive | 17.736 | 17.634 (grid b0.3 seed42) | significantly lower |

### Issues noted

1. **Experiment names don't match task description.** The server has `contamination_60_seed123` (not `ess_only_seed123`), `contamination_60_uniform_seed123`, and seed42 variants for random/grid. The requested `ess_only_seed456`, `random_seed123`, `random_seed456` don't exist on this server.

2. **Qwen3-1.7B download failed** - server has no internet access (Network unreachable). No proxy/mirror configured.

3. **3 GPUs are running active training** (detect_remove_q05_seed123, detect_remove_q05_seed456, detect_remove_q09_seed42), not "all 4 free" as stated.

Results saved to `/root/autodl-tmp/output/eval_results_contamination_60_all.json`.

---
