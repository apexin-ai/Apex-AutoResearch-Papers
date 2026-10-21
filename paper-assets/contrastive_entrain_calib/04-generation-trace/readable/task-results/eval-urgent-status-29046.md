# eval urgent status 29046

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_urgent-status-29046_20260522T161836_result.json`
- **Structured JSON:** [`cc1dd8a762aa63120f23.json`](../../sessions/cc/cc1dd8a762aa63120f23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-29046 ===
GPU0: 93331/97887 MiB [100%]  多进程共占
GPU1: 40222/97887 MiB [100%]  exp-004 resume

exp-003-gs8 (r3only): 运行中 step 21/8000, ~65s/step, ETA ~146h
  PID 516696: run_exp003_gs8_r3only.py (cuda:0, 38188 MiB)
  PID 519538: run_exp003_gs8_r3only.py (cuda:0, 38186 MiB) ← 第2个进程，可能是子进程
  ⚠ 每步都有 WARNING: "d_syc not loaded; returning R3-only rewards"

exp-004-s2-v2 (act resume): 运行中 step 4150/8000, ~9.2s/step, elapsed 5.5h
  PID 494017: run_exp004s2_act_resume.py --resume-from-checkpoint checkpoint-2000 --device cuda:0 (23270 MiB)
  注意：命令行写的 cuda:0，但 GPU1 有 40GB 显存占用，实际可能跑在 cuda:1

其他进程 (eval，跑在 GPU1):
  PID 517336: eval_unified_preset.py exp003-s2-ckpt7500 (16938 MiB)
  PID 517417: eval_unified_preset.py exp003-s2-ckpt8000 (16938 MiB)
```

---
