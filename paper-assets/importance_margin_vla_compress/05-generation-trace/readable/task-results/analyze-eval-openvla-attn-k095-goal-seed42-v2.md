# analyze eval openvla attn k095 goal seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_attn_k095_goal_seed42_v2_20260527T092855_result.json`
- **Structured JSON:** [`c7f25fc2e537902cea7f.json`](../../sessions/c7/c7f25fc2e537902cea7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

**结果汇总：**

| 指标 | 值 |
|------|-----|
| **Overall SR** | **75.6%** (378/500) |
| 之前记录 (ROADMAP) | 76.8% |
| 差值 | -1.2pp |

Per-task breakdown:

| Task | SR |
|------|-----|
| T1 open middle drawer | 72% |
| T2 put bowl on stove | 94% |
| T3 put wine bottle on cabinet | 86% |
| T4 open drawer put bowl | 44% |
| T5 put bowl on cabinet | 94% |
| T6 push plate to stove | 74% |
| T7 put cream cheese in bowl | 74% |
| T8 turn on stove | 94% |
| T9 put bowl on plate | 74% |
| T10 put wine bottle on rack | 50% |

v2 的 75.6% 与之前的 76.8% 差 1.2pp，在正常方差范围内。Attn k=0.95 Goal 数据点已补全。

---
