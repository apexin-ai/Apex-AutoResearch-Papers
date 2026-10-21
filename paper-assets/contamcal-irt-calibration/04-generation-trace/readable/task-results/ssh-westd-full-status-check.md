# ssh westd full status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-full-status-check_20260519T122407_result.json`
- **Structured JSON:** [`2eebd4abd0a7e7abb475.json`](../../sessions/2e/2eebd4abd0a7e7abb475.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Status Report — westd-29999 (2026-05-19 20:24 CST)

### GPU Utilization

| GPU | Status | Mem | Process |
|-----|--------|-----|---------|
| **0** | **BUSY** 94% | 16.7/97.9 GB | OLMo-2 **d005** eval (PID 168549) |
| **1** | **BUSY** 90% | 16.7/97.9 GB | OLMo-2 **d025** eval (PID 167370), nearly done → will then run d050 |
| **2** | **IDLE** 0% | 0/97.9 GB | d100 already completed |
| **3** | **BUSY** 92% | 16.7/97.9 GB | OLMo-2 **d050** eval (PID 169634), ~8% MMLU |

### Tmux Sessions

- `olmo2_gpu2` — orchestrating monitor + eval scripts across pts/0-3
- `olmo2_monitor` script running on pts/1, polling every 120s

### eval_results_v2 Completion Matrix

All 5 dosages (d000/d005/d025/d050/d100), benchmarks: MMLU + ARC Challenge.

| Model | d000 | d005 | d025 | d050 | d100 |
|-------|------|------|------|------|------|
| **Qwen-7B** | done | done | done | done | done |
| **Qwen-14B** | done | done | done | done | done |
| **Phi-4** | done | done | done | done | done |
| **Gemma-2** | done | done | done | done | done |
| **OLMo-2** | done | **running** (GPU0) | done (just finished) | **running** (GPU3) | done |

**OLMo-2 is the only family with incomplete evals.** Two dosages remaining: **d005** and **d050**, both actively running. At ~20 items/sec on MMLU (14042 items) + ARC, each should finish in roughly 15-25 minutes.

### Conflict Warning

**GPU1 and GPU3 scripts are duplicates** — both `olmo2_eval_gpu1.sh` and `olmo2_eval_gpu3.sh` run `d025 → d050` sequentially to the **same output dirs**. GPU3 already finished d025 and is now on d050. GPU1 is still finishing d025 and will then also start d050, creating a race condition on `eval_results_v2/olmo2_d050/`. You may want to kill PID 167370 (GPU1) after it finishes d025 to avoid the conflict, since GPU3 is already handling d050.

---
