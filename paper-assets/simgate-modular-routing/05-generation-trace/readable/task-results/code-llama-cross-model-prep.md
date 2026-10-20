# code llama cross model prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-cross-model-prep_20260519T014029_result.json`
- **Structured JSON:** [`7ccde32c1c546f6c7393.json`](../../sessions/7c/7ccde32c1c546f6c7393.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The user has already launched the D118 experiment with their own scripts. Here's the current status:

**Experiment D118 — Llama-3.1-8B-Instruct full ScienceWorld replication**

**Status: Running successfully on both GPUs**

| GPU | Current Task | Episodes | Output Dir |
|-----|-------------|----------|------------|
| 0 | chemistry-mix (1/6 tasks) | 20 | results/llama_cross_model_full |
| 1 | identify-life-stages-2 (1/5 tasks) | 20 | results/llama_cross_model_full |

**Verified working:**
- vLLM V1 (0.18.1) loads Llama-3.1-8B correctly (14.99 GiB, CUDA graphs)
- Internal episodes complete (~48s each)
- Deterministic episodes with fork_and_lookahead complete (~170s each)
- No EngineCore crashes in the user's foreground processes

**Episode timing (from Episode 0):**
- Internal: 48s + Deterministic: ~170s = ~218s per episode pair (~3.6 min)
- Per task (20 episodes): ~72 min
- GPU 0 (6 tasks): ~7.2 hours
- GPU 1 (5 tasks): ~6.0 hours

**My dry-run crash** was caused by GPU memory conflict — the user started their processes on GPU 0 while my nohup dry-run was still occupying it, killing the EngineCore subprocess.

The experiment will likely finish in ~7-8 hours from start (10:23 CST → ~17:30-18:30 CST).

---
