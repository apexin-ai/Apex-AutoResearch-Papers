# fix gpu collision kill diagnose fix

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gpu_collision_kill_diagnose_fix_20260522T060352_result.json`
- **Structured JSON:** [`4c2fbd1393d45b6cb982.json`](../../sessions/4c/4c2fbd1393d45b6cb982.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 张 GPU 分配全部正确。

```
== Step 1: Kill ==
PID 11979: killed
PID 12421: already_dead
tmux sessions: pipeline_alpha0p5_20 cleaned, pipeline_alpha2p0_20 not found

== Step 2: MATH-500 eval health ==
PID 2234: alive ✅
GPU 0 status: 17532MiB, 98% util

== Step 3: Root cause ==
Files with CUDA_VISIBLE_DEVICES override:
- sft_recovery.py line 19-22: early `--gpu` parsing sets `os.environ["CUDA_VISIBLE_DEVICES"] = sys.argv[_i + 1]` before torch import
- train_grpo_v5.py: clean (args.gpu only used in log message)
- eval_gsm8k.py: clean
- eval_math500.py: clean
- prune.py: clean

== Step 4: Fix applied ==
- sft_recovery.py: removed lines 19-23 (early CUDA_VISIBLE_DEVICES override block)
  唯一的越界源头。pipeline 传 `--gpu 0` 导致覆盖外部 CUDA_VISIBLE_DEVICES=3/2 → 0

== Step 5: Restart ==
α=0.5 PID: 14672 (child of 13852) on GPU 3
α=2.0 PID: 15120 (child of 14133) on GPU 2

== Step 6: Verification ==
GPU 0: PID 2234 (MATH-500 eval) 17532MiB ✅
GPU 1: PID 5241 (eval) 16040MiB ✅
GPU 2: PID 15120 (α=2.0 SFT) 9278MiB ✅
GPU 3: PID 14672 (α=0.5 SFT) 12464MiB ✅

== eval_gsm8k_sft_alpha4_20_v5 ==
Status: DONE (accuracy=61.94%, 817/1319, EOS rate=98.1%)
```

---
