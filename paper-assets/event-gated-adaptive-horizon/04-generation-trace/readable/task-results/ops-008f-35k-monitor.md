# ops 008f 35k monitor

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_008f_35k_monitor_20260514T061802_result.json`
- **Structured JSON:** [`c004ced95d36f2ccc3b2.json`](../../sessions/c0/c004ced95d36f2ccc3b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
008f:
- current_step: 35000 (eval marker written, eval 正在执行中)
- eval@5K:  return=30.49,  value=0.0012,  v/e≈0%
- eval@15K: return=182.03, value=2.99,    v/e=1.64%
- eval@25K: return=196.78, value=17.51,   v/e=8.90%, normalized=1.02x (baseline 8.7%)
- eval@35K: 未产出——step marker 已写但 eval episodes 仍在运行，预估 5-10 分钟内完成
- process_alive: yes (PID 127766, 859% CPU)
- 注意: gate_dt_mean=2.0 恒定, gate_dt_2_frac=1.0 (固定 dt=2, 无变化)

008e_v3:
- current_step: ≥45000 (训练继续至 105K)
- eval@5K:  return=31.00,  value=0.0017
- eval@15K: return=131.17, value=4.00
- eval@25K: return=155.69, value=26.19,   v/e=16.83%, normalized=1.93x (baseline 8.7%)
- eval@35K: return=276.47, value=62.76,   v/e=22.70%, normalized=0.94x (baseline 24.1%)
- eval@45K: return=382.22, value=110.67,  v/e=28.96%, normalized=0.87x (baseline 33.1%)
- process_alive: yes (PID 126115, 907% CPU)
- 注意: gate_dt_mean=1.0 恒定, gate_dt_1_frac=1.0 (固定 dt=1, 无变化)
```

关键发现：008e_v3 的 normalized v/e 随训练推进从 1.93x 降到 0.87x——early steps value 高估严重，但后期趋于正常甚至低于 baseline。008f 的 @25K normalized v/e 几乎与 baseline 持平 (1.02x)，@35K 数据再等几分钟即可。

---
