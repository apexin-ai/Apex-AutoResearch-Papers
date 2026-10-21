# ssh cuda3 qwen or exp009

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cuda3_qwen_or_exp009_20260522T215849_result.json`
- **Structured JSON:** [`745c2ac6fe73cc039d31.json`](../../sessions/74/745c2ac6fe73cc039d31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full status:

## Qwen2.5-7B Responses
- **COMPLETE**: 500 lines, 1.67MB on autodl-8gpu ✓

## Qwen2.5-7B Judge Evaluation
- **NOT configured**: `qwen2.5-7b` is not in `target_models` of any judge config (llama/mistral/qwen). All three configs only judge: gpt-3.5-turbo-0125, gpt-4-0314, gpt-4-0613, gpt-4o, gpt-4o-mini, llama-3.3-70b, qwen2.5-72b, gemma-2-9b, qwen3-8b.
- Need to add `qwen2.5-7b` to target_models and re-run collection on **rtx6000-4x** (where vLLM judge servers are running).

## exp-009 (rtx6000-4x)
- **Part A**: COMPLETE (401 lines = 4 rhos × 50 seeds × 2 methods)
- **Part B**: 24/50 seeds done (1201 lines), still running (PID 112925)
- **CPU-bound** (NumPyro MCMC with `XLA_FLAGS=--xla_force_host_platform_device_count=4`). cuda:3 won't help.

## Judge Collection on rtx6000-4x
| Judge | Progress | ETA |
|-------|----------|-----|
| Llama-3.3-70B | 1980/8311 | ~21h |
| Mistral-Large-2 | 5460/8742 | ~5h |
| Qwen2.5-72B | 915 lines, collect.py **not running** | — |

All 4 rtx6000 GPUs fully loaded (75-91GB VRAM) with vLLM servers.

## cuda:3 on autodl-8gpu
**No useful GPU task available:**
- exp-009 is CPU-only
- No large judge models on autodl (only small models: Llama-3.1-8B, Mistral-7B, Qwen2.5-7B, Gemma-2-9B)

## Director Decisions Needed
1. **Add qwen2.5-7b to judge configs on rtx6000?** The vLLM servers are already there; just need to update configs and restart/supplement the collect.py runs.
2. **Restart Qwen2.5-72B judge collection on rtx6000?** It stopped at 915 items. The vLLM server at port 8002 is running.
3. **Run exp-009 Part B on autodl CPU** to supplement rtx6000? Would need seed coordination (copy cn_recovery.csv from rtx6000 to avoid duplicating seeds 0-23).
4. Or: **download a large judge model** (e.g. Qwen2.5-72B-AWQ) to autodl and run judge eval on cuda:3?

---
