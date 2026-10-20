# eval ablation b e2e correct

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ablation-b-e2e-correct_20260514T091045_result.json`
- **Structured JSON:** [`344cee45ec1b2a042207.json`](../../sessions/34/344cee45ec1b2a042207.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

---

## 结果汇总

**实验**: `plan-003-e2e-ablation-b-correct`  
**Checkpoint**: `checkpoints/plan-004-implicit/final_adapter` (ablation-b, internal_recall=51.52%)  
**结论**: **NEGATIVE** — trained-router 未超过 always-det baseline

### 核心指标

| 指标 | trained-router | always-det | oracle |
|------|---------------|------------|--------|
| continuous_score | **-10.70** [-15.25, -6.38] | -9.47 | -6.58 |
| success_rate | 0.237 | — | — |
| death_rate | 0.176 | — | — |
| sim_ratio | 0.970 | — | — |
| delta vs always-det | **-1.23** | — | — |

### 关键问题

1. **sim_ratio=97%** — router 几乎把所有 episode 都路由到 deterministic，等于一个略差的 always-det
2. **fallback=70.6%** — 245 episodes 中只有 68 个有 step data，173 个直接 fallback 到 deterministic
3. **唯一正分 task**: find-non-living-thing (+28.68, 62.5% success, 0% death)
4. **高 death rate tasks**: freeze (30%), find-animal (25%), inclined-plane (25%), measure-melting-point (25%)

---
