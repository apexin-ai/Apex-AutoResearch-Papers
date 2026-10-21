# analysis step tie rate 245eps

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_step-tie-rate-245eps_20260514T122336_result.json`
- **Structured JSON:** [`22f9db537ac68d02eb12.json`](../../sessions/22/22f9db537ac68d02eb12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**Step-level tie rate (245 eps / 11 tasks): 97.39% (5935/6094)**

| 指标 | 值 |
|---|---|
| Total steps | 6094 |
| Tie steps | 5935 |
| **Tie rate** | **97.39%** |
| Both-zero ties | 5920 (99.7% of ties) |
| Det preferred | 133 steps |
| Int preferred | 26 steps |

Per-task range: 96.07% (measure-melting-point) ~ 97.99% (lifespan-longest-lived-then-shortest-lived)

**vs 旧 MVP 对比：** 97.39% vs 98.2%，差 0.78pp < 1% 阈值。差异来源：(1) 方法论不同——旧数据用 oracle routing（同状态对比），新数据用独立轨迹；(2) 11 tasks 覆盖更多 task type 包括更复杂场景。

论文引用建议更新为 **97.4% (5935/6094 steps, 245 episodes, 11 tasks)**。

Registry entry `plan-012-step-tie-rate` 已注册，status=DONE，含完整 per-task metrics。

---
