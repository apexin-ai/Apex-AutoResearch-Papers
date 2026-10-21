# code batch64 config and submit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_batch64_config_and_submit_20260517T011243_result.json`
- **Structured JSON:** [`f0377f19cfac620c4d3e.json`](../../sessions/f0/f0377f19cfac620c4d3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练确认正常运行：

```
=== CONFIG ===
gradient_accumulation_steps: 16
effective_batch: 64
total_optimizer_steps: 100K
total_samples: 6.4M
trainable_params: 99,880,992 (~100M, 22.2%)

=== TRAINING STARTED ===
PID: 124908
GPU: 1 (2727 MiB, 37% util)
tmux session: fullft_batch64
log: logs/fullft_batch64.log

=== FIRST STEPS ===
step=0/100000   loss=1.5052  lr=1.00e-07  grad=11.21  sps=0.2
step=50/100000  loss=1.3758  lr=5.10e-06  grad=7.60   sps=0.3

=== ESTIMATE ===
~3.3 sec/optimizer_step → 100K steps ≈ 3.8 days
```

GPU 0/2/3 上的其他训练不受影响。Loss 正常下降，梯度累积生效。

---
