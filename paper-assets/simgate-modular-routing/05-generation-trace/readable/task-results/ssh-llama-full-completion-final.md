# ssh llama full completion final

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_llama-full-completion-final_20260519T103716_result.json`
- **Structured JSON:** [`221861c421b9922a0b30.json`](../../sessions/22/221861c421b9922a0b30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D118 完成确认：11/11 tasks, 220 episodes ✓

### Per-task 结果

| Task | Eps | IntDR | DetDR | Both | Det>Int | Int>Det | Tie | AvgI | AvgD |
|---|---|---|---|---|---|---|---|---|---|
| chemistry-mix | 20 | 45% | 20% | 4 | 5 | 0 | 15 | -43.2 | -17.1 |
| find-animal | 20 | 40% | 25% | 3 | 6 | 2 | 12 | -39.2 | -23.0 |
| find-non-living-thing | 20 | 0% | 0% | 0 | 10 | 0 | 10 | 22.0 | 41.2 |
| freeze | 20 | 45% | 0% | 0 | 9 | 0 | 11 | -44.8 | 0.8 |
| grow-fruit | 20 | 45% | 5% | 1 | 8 | 0 | 12 | -43.7 | -3.7 |
| identify-life-stages-1 | 20 | 55% | 10% | 2 | 9 | 0 | 11 | -55.0 | -7.5 |
| identify-life-stages-2 | 20 | 45% | 5% | 1 | 8 | 0 | 12 | -43.4 | -3.4 |
| inclined-plane-determine-angle | 20 | 45% | 20% | 4 | 6 | 0 | 14 | -44.0 | -14.5 |
| lifespan-longest-lived | 20 | 35% | 5% | 0 | 7 | 1 | 12 | -30.0 | 2.5 |
| lifespan-longest-lived-then-... | 20 | 50% | 20% | 4 | 6 | 0 | 14 | -48.4 | -15.1 |
| measure-melting-point-unknown | 20 | 50% | 15% | 3 | 9 | 0 | 11 | -49.3 | -14.2 |

### Aggregate Metrics

| Metric | Llama | Qwen |
|---|---|---|
| Internal DR | **41.4%** (91/220) | 42.9% |
| Deterministic DR | **11.4%** (25/220) | 16.3% |
| Delta DR | **30.0pp** | 26.6pp |
| DAF | **88.2%** | 78.9% |
| Delta_full | 33.17 | - |
| Delta_nd | 3.90 | - |
| Labels | det=83, int=3, tie=134 | - |
| Both dead | 22 | - |

### vs Qwen 对比

Direction: **CONSISTENT**. Llama 结果与 Qwen 方向完全一致，且效应更强：
- DetDR 更低（11.4% vs 16.3%），说明 deterministic routing 在 Llama 上存活性更好
- DAF 更高（88.2% vs 78.9%），说明 death avoidance 对总分差异的贡献更大
- Det 压倒性胜出（83 vs 3），几乎没有 internal routing 优于 deterministic 的 case

跨模型验证强有力地支持核心 claim。

### Registry JSON

```json
{
  "total_episodes": 220,
  "tasks": 11,
  "internal_death_rate": 0.4136,
  "det_death_rate": 0.1136,
  "delta_dr_pp": 30.0,
  "both_dead": 22,
  "det_preferred": 83,
  "int_preferred": 3,
  "no_preference": 134,
  "delta_full": 33.17,
  "delta_nd": 3.9,
  "daf": 88.2,
  "per_task": { ... }  // 完整 per-task 数据见上表
}
```

---
