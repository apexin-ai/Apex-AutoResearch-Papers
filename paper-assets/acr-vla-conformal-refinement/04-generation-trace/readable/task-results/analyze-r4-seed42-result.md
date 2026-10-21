# analyze r4 seed42 result

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_r4-seed42-result_20260522T112512_result.json`
- **Structured JSON:** [`7907ba491e06f840151a.json`](../../sessions/79/7907ba491e06f840151a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

## 结果汇总

| 指标 | r3 (n_action_steps=50) | r4 (n_action_steps=10) |
|------|----------------------|----------------------|
| **Overall** | **81.5%** ± 0.5% | **100.0%** (200/200) |
| 每个 task | 有失败 | 全部 20/20 |

**+18.5pp**。所有 10 个 Object task 均完美通过。

核心原因：`n_action_steps=10` 让 PI0.5 每 10 步重新规划一次（r3 是 50 步），更高频的 re-planning 在 Object 这类简单任务上彻底消除了累积误差。Object benchmark 已达天花板 100%，conformal refinement 在此 benchmark 上无提升空间，需在更难的 benchmark（Spatial/Goal）上验证价值。

---
