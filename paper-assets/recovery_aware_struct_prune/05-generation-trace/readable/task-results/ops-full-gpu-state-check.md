# ops full gpu state check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_gpu_state_check_20260519T105936_result.json`
- **Structured JSON:** [`192ebe59e0bd3fa5d7a3.json`](../../sessions/19/192ebe59e0bd3fa5d7a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU State Audit Summary

### westd-29022 (4× RTX PRO 6000)

| GPU | Experiment | PID | Status | Progress | Key Metric | VRAM | Util |
|-----|-----------|-----|--------|----------|------------|------|------|
| cuda:0 | eval_gsm8k_grpo_standard_20_fair_v2 | 83299 | Running | **766/1319 (58%)** | acc=59.47% @750 | 30GB | 94% |
| cuda:1 | eval_humaneval_sft_cka_only_20_2048_v2 | 78740 | Running | **161/164 (98%)** | pass@1=20.62% @160 | 18GB | 98% |
| cuda:2 | eval_humaneval_grpo_standard_20_fair_2048_v3 | 76392 | Running | **155/164 (95%)** | pass@1=11.43% @140 | 18GB | 91% |
| cuda:3 | eval_humaneval_sft_standard_20_2048_v3 | 86171 | Running | **64/164 (39%)** | pass@1=16.67% @60 | 17GB | 99% |

**ETAs (westd):**
- **sft_cka_only_20_2048_v2**: ~5 min (3 problems left, ~87s/it)
- **grpo_standard_20_fair_2048_v3**: ~16 min (9 problems left, ~107s/it)
- **gsm8k_grpo_standard_20_fair_v2**: ~1-2 hours (553 left, variable 2-5s/it with occasional long-gen outliers)
- **sft_standard_20_2048_v3**: ~2.5 hours (100 left, ~91s/it)

---

### westb-23072 (2× RTX PRO 6000)

| GPU | Experiment | PID | Status | Progress | VRAM | Util |
|-----|-----------|-----|--------|----------|------|------|
| cuda:0 | — | — | **IDLE** | — | 0MB | 0% |
| cuda:1 | grpo_cka_only_20_seed123 | 857962 | Running | **~step 63/100** | 68GB | 99% |

**Training pace**: ~6.9 min/step (consistent across all 10-step dumps). ETA for step 100: **~23:15 today**.

**Disk**: `/root/autodl-tmp` — 213G/250G (85%), **38G free**.

---

### Anomalies
- **None.** All 5 expected experiments are alive and progressing normally.
- GSM8K eval has occasional long-generation outliers (5-6 min pauses at items 722, 732) but resumes normally — likely hard problems triggering max token generation.
- Two HumanEval evals (cuda:1, cuda:2) will finish imminently. Their GPUs will be free within ~20 min.

---
