# ops fix submit scripts 015B 017

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-submit-scripts-015B-017_20260515T102246_result.json`
- **Structured JSON:** [`a6a0d5a8d197d6966995.json`](../../sessions/a6/a6a0d5a8d197d6966995.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 1. submit_plan017.sh diff

```diff
-  --device cuda:0 \
+  --device cuda:1 \
```

其他参数未变（`--gate_subsample_max_dt 1` 保留）。

### 2. submit_plan015b.sh 完整内容

```bash
#!/bin/bash
# plan_015B: frozen dt_emb + subsample ON + dt=2 imagination + H=8
# 2x2 ablation: isolate training vs existence of dt_emb
# cuda:1, after 009e completes

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6
export MUJOCO_GL=osmesa
export PYOPENGL_PLATFORM=osmesa

cd /root/autodl-tmp/event-gated-adaptive-horizon

python -u dreamer.py --configs defaults dmc_proprio \
  --task dmc_walker_walk \
  --logdir logdir/exp_015b_frozen_dt_emb \
  --steps 105000 --seed 1 --compile False --device cuda:1 \
  --gate_enabled True --gate_fixed_dt 2 \
  --gate_subsample_max_dt 2 \
  --imag_horizon 8 \
  --dt_emb_freeze True
```

### 3. 关键参数对比

| 参数 | plan_015B | plan_017 |
|------|-----------|----------|
| device | cuda:1 | cuda:1 |
| gate_subsample_max_dt | 2 (ON) | 1 (OFF) |
| dt_emb_freeze | True (frozen) | 未设 (trained) |
| imag_horizon | 8 | 15 |
| seed | 1 | 1 |
| steps | 105000 | 105000 |

全部符合预期。

---
