# check exp 077 078 progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_077_078_progress_20260525T124934_result.json`
- **Structured JSON:** [`42b379f49ebc3269028d.json`](../../sessions/42/42b379f49ebc3269028d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
exp_077_cheetah_baseline_s0: step 60000/105000 (57.1%)
  latest eval: eval_return 441.0 @ step 55000
  train_return ~310 (recent avg @ 60k)

exp_078_cheetah_008d_s0: step 52000/105000 (49.5%)
  latest eval: eval_return 148.9 @ step 45000
  train_return ~69 (recent avg @ 52k)
  gate_dt_mean 2.0, gate_dt_2_frac 1.0 (gate 锁在 dt=2, 未分化)
```

exp_078 的 return 明显低于 baseline，且 gate 完全退化到固定 dt=2（entropy=0, 无分化）。

---
