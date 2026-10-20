# code eval mvp script

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-mvp-script_20260513T032907_result.json`
- **Structured JSON:** [`e93d6ec67ef98e47f978.json`](../../sessions/e9/e93d6ec67ef98e47f978.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。结果：

```
Baseline step range: 0-44000
Event-gated step range: 0-36000

Criterion 1 (Return >= 80% baseline): FAIL
  Baseline: 491.70, Event-gated: 196.50, Ratio: 0.40

Criterion 2 (Gate entropy > 0.3 nats): FAIL
  Mean gate entropy: 0.0000 nats

Criterion 3 (H_eff > 1.2 × H_nominal): FAIL
  Mean Δt: 1.0000 (gate 完全选 dt=1)

Criterion 4 (Δt temporal structure): FAIL
  dt std: 0.0000, Autocorrelation: N/A

Overall: 0/4 PASS
```

训练仅 ~36K-44K / 500K 步（<10%），gate 尚未开始学习（gate_scale=0，所有 Δt=1，entropy=0）。这是预期行为——gate 通常需要更长训练才会开始分化。4 张图已保存到 `logdir/event_gated_s1/eval_plots/`。

脚本可随时重新运行以跟踪训练进展。

---
