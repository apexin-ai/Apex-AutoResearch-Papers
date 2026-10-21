# ssh retry determinism audit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_retry-determinism-audit_20260518T171907_result.json`
- **Structured JSON:** [`138805ead153decedf74.json`](../../sessions/13/138805ead153decedf74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Retry N=5 Determinism Audit (200 episodes)

```
Total episodes: 200 (180 full 5-trial, 20 early success)

全死: 76/200 (38.0%)
全活: 102/200 (51.0%)
混合: 22/200 (11.0%)
Rescue (death→alive): 20/200 (10.0%)
Regression (alive→death): 2/200 (1.0%)
```

### Per-Task Breakdown

| Task | Total | 全死 | 全活 | 混合 | Rescue | Regr |
|---|---|---|---|---|---|---|
| chemistry-mix | 20 | 9 | 9 | 2 | 2 | 0 |
| find-animal | 20 | 10 | 9 | 1 | 0 | 1 |
| freeze | 20 | 9 | 9 | 2 | 2 | 0 |
| grow-fruit | 20 | 6 | 10 | 4 | 3 | 1 |
| identify-life-stages-1 | 20 | 5 | 13 | 2 | 2 | 0 |
| identify-life-stages-2 | 20 | 5 | 15 | 0 | 0 | 0 |
| inclined-plane-determine-angle | 20 | 8 | 9 | 3 | 3 | 0 |
| lifespan-longest-lived | 20 | 8 | 10 | 2 | 2 | 0 |
| lifespan-longest-lived-then-shortest-lived | 20 | 6 | 9 | 5 | 5 | 0 |
| measure-melting-point-unknown-substance | 20 | 10 | 9 | 1 | 1 | 0 |

### Mixed Episode Details (22 episodes)

| Task | Episode | Death Pattern | Type |
|---|---|---|---|
| chemistry-mix | ep009 | 3/4 deaths [T,T,T,F] | RESCUE |
| chemistry-mix | ep012 | 4/5 deaths [T,T,F,T,T] | RESCUE |
| find-animal | ep016 | 2/5 deaths [F,T,F,F,T] | REGRESSION |
| freeze | ep012 | 4/5 deaths [T,T,T,F,T] | RESCUE |
| freeze | ep016 | 4/5 deaths [T,T,T,T,F] | RESCUE |
| grow-fruit | ep005 | 4/5 [T,T,T,F,T] | RESCUE |
| grow-fruit | ep012 | 4/5 [T,T,F,T,T] | RESCUE |
| grow-fruit | ep015 | 4/5 [F,T,T,T,T] | REGRESSION |
| grow-fruit | ep016 | 4/5 [T,T,T,F,T] | RESCUE |
| identify-life-stages-1 | ep003 | 1/2 [T,F] | RESCUE |
| identify-life-stages-1 | ep012 | 3/5 [T,T,F,T,F] | RESCUE |
| inclined-plane-determine-angle | ep005 | 3/4 [T,T,T,F] | RESCUE |
| inclined-plane-determine-angle | ep015 | 2/3 [T,T,F] | RESCUE |
| inclined-plane-determine-angle | ep016 | 4/5 [T,T,F,T,T] | RESCUE |
| lifespan-longest-lived-then-shortest-lived | ep003 | 1/2 [T,F] | RESCUE |
| lifespan-longest-lived-then-shortest-lived | ep012 | 2/5 [T,F,F,T,F] | RESCUE |
| lifespan-longest-lived-then-shortest-lived | ep015 | 4/5 [T,T,T,F,T] | RESCUE |
| lifespan-longest-lived-then-shortest-lived | ep016 | 4/5 [T,T,T,T,F] | RESCUE |
| lifespan-longest-lived-then-shortest-lived | ep017 | 4/5 [T,T,T,T,F] | RESCUE |
| lifespan-longest-lived | ep012 | 4/5 [T,T,T,F,T] | RESCUE |
| lifespan-longest-lived | ep017 | 1/2 [T,F] | RESCUE |
| measure-melting-point-unknown-substance | ep012 | 4/5 [T,T,F,T,T] | RESCUE |

### Retry-Control-Baseline N=3

无 N=3 control/retry 数据。`results/` 下只有 `retry_dose_response/retry_n5/`，其他 baseline 目录（`plan_003_eval_full_baseline`, `baseline_245eps`, `majority_vote_baseline`）是不同实验。

### 关键发现

**Retry 不是完全确定性行为。** 11% (22/200) 的 episode 存在 trial 间 outcome 不一致。

但模式高度非对称：
- **Rescue 占绝对主导**: 20/22 混合 episode 是 death→alive 转换（91%），仅 2 个是 regression
- **Rescue 集中在少数 trial**: 混合 episode 中大多数 trial 仍然是 death（典型模式 4/5 deaths），只有 1 个 trial 偶然存活
- **lifespan-longest-lived-then-shortest-lived** 混合率最高 (5/20 = 25%)，identify-life-stages-2 完全确定性 (0% mixed)

论文叙事不能升级为"完全确定性"。但可以说：**retry 行为高度一致（89% episode 完全一致），残余随机性主要表现为低概率 rescue（10%），几乎不存在 regression（1%）。**

---
