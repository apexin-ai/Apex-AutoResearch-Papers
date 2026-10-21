# exp temp curve t05 t09

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_temp-curve-t05-t09_20260517T221118_result.json`
- **Structured JSON:** [`ee8f7290a62cac3f116e.json`](../../sessions/ee/ee8f7290a62cac3f116e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Status summary:**

1. **`generate_chain.py` modified** — added `--temperature` and `--top-p` CLI args (verified with dry-run)

2. **Generation running** in tmux `temp_curve` on autodl-5090:
   - Job 1: Pythia-2.8B t=0.5 (~2.6h, started)
   - Job 2: Pythia-2.8B t=0.9 (~2.6h, queued after job 1)
   - Job 3: Qwen3-1.7B t=0.9 (~2.6h, queued after job 2)

3. **Eval script ready** (`eval_temp_curve_logo.py`) — partial results from existing data:

| Model | Temp | Binary F1 | 95% CI |
|-------|------|-----------|--------|
| qwen3-1.7b | 0.5 | 0.7506 | [0.7348, 0.7656] |
| qwen3-1.7b | 0.7 | 0.7505 | [0.7345, 0.7664] |
| qwen3-1.7b | 1.0 | 0.3670 | [0.3525, 0.3813] |
| pythia-2.8b | 0.7 | 0.7395 | [0.7254, 0.7548] |

4. **Registry**: exp_049 and exp_050 both set to RUNNING

5. **Missing from task scope**: Pythia-2.8B t=1.0 data doesn't exist. Once the current 3 jobs complete, I can add it as a 4th run if you want the full 4-point curve for both models.

I'll check back in 1 hour for progress.

---
