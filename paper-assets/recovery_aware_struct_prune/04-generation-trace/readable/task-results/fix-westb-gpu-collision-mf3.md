# fix westb gpu collision mf3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westb_gpu_collision_mf3_20260522T080438_result.json`
- **Structured JSON:** [`056bfb1bf93ae36528b0.json`](../../sessions/05/056bfb1bf93ae36528b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
== Step 1: Kill MF3 ==
PID 163403: killed ✅ (SIGTERM, clean exit)

== Step 2: MF3 重启 ==
无需重启 — PID 164710 已在 GPU 1 运行相同 GRPO 任务（7m38s ago）

== Step 3: α=3.0 SFT ==
PID: 162850 on GPU 0, still running (17m40s elapsed) ✅

== Step 4: sft_recovery.py fix ==
Lines removed: 19-23 (# Parse --gpu early... + for loop)
Verification: no CUDA_VISIBLE_DEVICES override ✅

== Step 5: GPU 验证 ==
GPU 0: PID 162850 (α=3.0 SFT) 51548 MiB ✅
GPU 1: PID 164710 (MF3 GRPO) 58548 MiB ✅
```

碰撞已解除，两张卡各跑各的。163403 是被 kill 的旧 MF3 进程，164710 是此前已启动在 GPU 1 上的 MF3 GRPO（可能是之前的调度），参数完全一致，无需重复启动。

---
