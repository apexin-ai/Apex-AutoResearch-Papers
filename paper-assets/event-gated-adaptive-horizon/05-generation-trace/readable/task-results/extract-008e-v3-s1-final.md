# extract 008e v3 s1 final

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_008e_v3_s1_final_20260514T223306_result.json`
- **Structured JSON:** [`acfdade48bf29767ae8d.json`](../../sessions/ac/acfdade48bf29767ae8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the compiled result:

```
=== 008e_v3_s1 FINAL RESULTS ===
STATUS: STILL_RUNNING (PID 898127, elapsed 3h44m, target 105000 steps)
CURRENT_STEP: ~92000 (last train log)
LAST_EVAL_STEP: 85000
CHECKPOINT: latest.pt (221MB), no checkpoint.ckpt

CONFIG: --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15 --seed 1

EVAL_TRAJECTORY:
  step=5000:  eval_return=31.00   value_mean=0.00     ve_ratio=0.0001  reward_loss=3.3450  model_loss=20.7378  actor_entropy=8.1598
  step=15000: eval_return=131.17  value_mean=4.00     ve_ratio=0.0305  reward_loss=0.6736  model_loss=7.4676   actor_entropy=2.2060
  step=25000: eval_return=155.69  value_mean=26.19    ve_ratio=0.1683  reward_loss=0.5944  model_loss=5.3057   actor_entropy=0.0658
  step=35000: eval_return=276.47  value_mean=62.76    ve_ratio=0.2270  reward_loss=0.6115  model_loss=5.0288   actor_entropy=-1.2322
  step=45000: eval_return=382.22  value_mean=110.67   ve_ratio=0.2896  reward_loss=0.6182  model_loss=4.9644   actor_entropy=-1.9930
  step=55000: eval_return=486.84  value_mean=170.09   ve_ratio=0.3494  reward_loss=0.6228  model_loss=4.9633   actor_entropy=-3.2020
  step=65000: eval_return=580.67  value_mean=235.05   ve_ratio=0.4048  reward_loss=0.6203  model_loss=4.9721   actor_entropy=-4.8221
  step=75000: eval_return=574.09  value_mean=300.51   ve_ratio=0.5235  reward_loss=0.6112  model_loss=4.9152   actor_entropy=-5.1072
  step=85000: eval_return=657.31  value_mean=351.33   ve_ratio=0.5345  reward_loss=0.6019  model_loss=4.8267   actor_entropy=-5.1767

LATEST_EVAL_RETURN: 657.31
LATEST_VALUE_MEAN: 351.33
LATEST_VE_RATIO: 0.5345

GATE METRICS: gate_dt_mean=1.0 at all checkpoints (gate_fixed_dt=1, no adaptive gating active)

=== NVE TRAJECTORY ===
exp_001_baseline NOT FOUND at specified path.
No exp_001* directories exist in logdir/.
Cannot compute NVE against baseline.

=== 009a STATUS ===
STATUS: STILL_RUNNING (PID 142508, elapsed 13h01m)
CURRENT_STEP: 336000 / 500000 (67.2%)
LAST_EVAL: step=335000, eval_return=919.23

009a EVAL TRAJECTORY (selected):
  step=85000:  618.73
  step=105000: 836.51
  step=215000: 956.04 (peak)
  step=285000: 960.20 (best)
  step=335000: 919.23 (latest)
PROCESS: ALIVE
```

**Key observations:**
- 008e 还在跑（~92k/105k），预计 ~1h 内完成
- 009a 作为 baseline（seed 2, 无 gate），67% 进度，eval_return 已稳定在 920-960 区间
- 008e 在 85k 步的 eval_return=657 远低于 009a 同步数下的 618（009a 85k=618.73，008e 85k=657.31，008e 略高）
- 008e 的 ve_ratio 持续上升（0.53），说明 value function 在追赶但仍有差距
- gate_dt 全程固定为 1（因为 gate_fixed_dt=1），没有真正的 adaptive horizon

---
