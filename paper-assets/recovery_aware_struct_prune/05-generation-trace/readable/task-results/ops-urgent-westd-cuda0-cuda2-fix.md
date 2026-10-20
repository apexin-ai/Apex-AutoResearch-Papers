# ops urgent westd cuda0 cuda2 fix

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_westd_cuda0_cuda2_fix_20260517T184051_result.json`
- **Structured JSON:** [`101b92490e8df0b814df.json`](../../sessions/10/101b92490e8df0b814df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full diagnosis:

---

## westd-11672 GPU Status

| GPU | Status | Details |
|-----|--------|---------|
| **cuda:0** | **IDLE** | 0MiB, 0% — **blocker: `sft_cka_only_20` model does not exist on westd** |
| cuda:1 | Running | PID 14556, 34560MiB, 99% util |
| **cuda:2** | **Running (NOT idle)** | PIDs 43911+44270, 23150MiB, 93% — `eval_postprune_rasp_30` submitted at 02:21, 25/200 samples (~4.6h ETA) |
| cuda:3 | Running | PID 31706, 31527MiB, 99% util |

## cuda:0 Blocker

`sft_cka_only_20` (12GB) only exists on **westb-23072**, not westd. Transfer is blocked:
- No direct SSH between servers (auth fails)
- No shared filesystem (autodl-fs/NAS absent)
- Docker network isolation blocks HTTP transfer
- westd disk nearly full (13GB free for 12GB model — barely fits even if transfer worked)

**Options:**
1. Wait for westb GRPO to finish (~7h), run eval there
2. Manually transfer the model (outside automated tools)
3. Use cuda:0 for a different eval with a model already on westd

## westb-23072 GRPO Progress

| Experiment | Step | Elapsed | ETA |
|-----------|------|---------|-----|
| grpo_cka_only_20 | **36/100** | ~4h06m | ~7h12m |
| grpo_random_20 | **44/100** | ~5h18m | ~6h55m |

## HumanEval Results (completed)

| Model | pass@1 | Correct/Total | Median Response Length |
|-------|--------|---------------|----------------------|
| sft_standard_20 | **11.6%** | 19/164 | 2048 (capped) |
| grpo_standard_20 | **10.4%** | 17/164 | 2048 (capped) |

Both models are generating reasoning text instead of code, hitting the 2048 token cap. HumanEval scores are very low — likely need `--max_new_tokens` raised or a code-specific prompt template.

## Summary

- cuda:2 was NOT idle — already running eval_postprune_rasp_30
- cuda:0 is truly idle because `sft_cka_only_20` was never copied to westd. No automated transfer path exists between these servers.
- Need your decision on how to handle cuda:0.

---
