# code cuda2 grpo protect

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cuda2-grpo-protect_20260521T073552_result.json`
- **Structured JSON:** [`389bf80613f2a10e1ca4.json`](../../sessions/38/389bf80613f2a10e1ca4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GRPO STATUS: DEAD (PID 93846) → already restarted as PID 97791 (running 1h22m)
GRPO STEP: 11/14042 (most time spent loading model)
GRPO PARAMS: per_device_batch=2, grad_accum=4, lr=5e-6 ✓, num_generations=8 ✓
GRPO HEALTH: no loss/grad_norm/clip_ratio in log yet (only progress bar through step 11)

CUDA:2 CLEANUP: killed PID 97296 (train.py clean_s7). cuda:2 now GRPO-only.

GPU STATUS:
cuda:0: PID 92119 (eval_lz.py clean_s4) + PID 96262 (eval_lz.py clean_s4) — 17212MiB
cuda:1: PID 96745 (train.py clean_s6) — 23111MiB
cuda:2: PID 97791 (train_grpo.py) — GRPO only ✓
cuda:3: PID 94961 (eval_lz.py clean_s5) — 8639MiB
```

**Note:** The "128" parameter — actual effective batch per step is `2 * 4 = 8` prompts (or `2 * 4 * 8 = 64` completions). Neither matches 128. If 128 was intended, `gradient_accumulation_steps` or `per_device_train_batch_size` may need adjustment. The GRPO (PID 97791) is currently running and progressing normally; the s7 conflict has been eliminated.

---
