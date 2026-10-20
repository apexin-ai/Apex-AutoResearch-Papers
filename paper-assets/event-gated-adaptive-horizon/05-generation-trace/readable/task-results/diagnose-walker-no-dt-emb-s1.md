# diagnose walker no dt emb s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_walker_no_dt_emb_s1_20260529T005126_result.json`
- **Structured JSON:** [`69e985c79e233ce63563.json`](../../sessions/69/69e985c79e233ce63563.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已有完整 registry 记录，状态已是 DONE/success。

**exp_walker_no_dt_emb_s1 结果摘要：**

| 指标 | 值 |
|------|-----|
| 状态 | DONE (success) |
| 最终 step | 105K (继续跑到 112K) |
| eval_return@105K | **468.83** |
| civo/ve_ratio | 0.23 (远低于 2.0 阈值) |
| civo/alert | 0 (无 CIVO 触发) |
| gate_dt_mean | 2.0 (100% 选择 dt=2) |
| gate_empirical_entropy | 0.0 |
| EXIT_CODE | 0 |
| 完成时间 | 2026-05-27 14:21 |

结论：hypothesis 确认——移除 dt_embedding 后 CIVO 未触发，但 gate 完全退化为常量 dt=2（零熵），自适应 horizon 机制无实际作用。Registry 已有正确记录，无需额外更新。

---
