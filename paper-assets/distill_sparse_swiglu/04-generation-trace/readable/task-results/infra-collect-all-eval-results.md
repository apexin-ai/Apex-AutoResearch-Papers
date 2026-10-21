# infra collect all eval results

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_collect_all_eval_results_20260517T195809_result.json`
- **Structured JSON:** [`32cace41cd60a42373d7.json`](../../sessions/32/32cace41cd60a42373d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 experiments are still running. Here's the status:

## qwen14b_bce30_s42_eval
**Server:** westd-34887, cuda:0
**Status:** running — GSM8K 49% (641/1319), ETA ~2h47m
- Earlier tasks (wikitext2, arc_challenge, winogrande, mmlu) completed, but results.json only written after all tasks finish

## bce_isocompute_v3_s456
**Server:** westd-34887, cuda:1
**Status:** running — training 96% (2600/2700), ~2 min left to finish training
- Final loss: 0.6357, bce: 0.6347, sparsity: 0.510
- Training only; eval phase will follow (or needs separate launch)

## qwen14b_teal30
**Server:** westd-41718, cuda:1
**Status:** running — GSM8K 55% (729/1319), ETA ~2h50m
- Log at `/root/distill_sparse_swiglu/logs/qwen14b_teal30_eval.log`

## qwen14b_dense_baseline
**Server:** westd-41718, cuda:0
**Status:** running — GSM8K 16% (217/1319), ETA ~2h36m

---

**Re: launching bce_isocompute_v3_s123** — cuda:0 on westd-34887 is still occupied by qwen14b_bce30_s42_eval (~2h47m remaining). Cannot start yet.

**Note on bce_isocompute_v3_s456:** Training finishes in ~2 min. Does the command chain include auto-eval after training, or should I prepare a separate eval launch for when it completes?

---
