# monitor training progress check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-check_20260514T142507_result.json`
- **Structured JSON:** [`a1276d7ada951f19d04d.json`](../../sessions/a1/a1276d7ada951f19d04d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

| | exp_009a (baseline) | exp_009b (008d treatment) |
|---|---|---|
| **Step** | 116K / 500K (23.2%) | 5K / 105K (4.8%) |
| **eval_return** | 804.8 @ 115K | 39.3 @ 5K |
| **value_mean** | 574.9 | 0.0013 |
| **value/eval ratio** | 71.4% | ~0% (正常，太早期) |
| **fps** | 7.77 | ~7.5 (估算) |
| **ETA** | ~13.7h | ~3.7h |
| **GPU** | cuda:0, 16%, 4165MiB | cuda:1, 0%, 2751MiB |
| **状态** | 健康，eval_return 稳步上升 | 刚启动，gate 全锁 dt=2 |

009a 训练曲线正常，eval_return 从 41→805 稳步爬升。009b 刚跑 7 分钟，尚无法判断 delusional critic collapse 风险——需要等到 ~30K-50K steps 时观察 value_eval_ratio 是否异常膨胀。

---
