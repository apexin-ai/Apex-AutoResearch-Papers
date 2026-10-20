# analysis find nonliving sft labels

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_find-nonliving-sft-labels_20260513T190907_result.json`
- **Structured JSON:** [`f3360f0f049e89cc742e.json`](../../sessions/f3/f3360f0f049e89cc742e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### Episode-level label 分布

| Episode | I score | D score | Label |
|---------|---------|---------|-------|
| ep=0 var=0 | 50.0 | 58.0 | deterministic |
| ep=1 var=1 | 0.0 | 0.0 | tie |
| ep=2 var=2 | 8.0 | 8.0 | tie |
| ep=3 var=3 | 50.0 | 58.0 | deterministic |
| ep=4 var=4 | 50.0 | 0.0 | **internal** |

**汇总**: Det wins 2/5, Int wins 1/5, Ties 2/5

### Internal SFT 正样本

- Internal SFT steps: **30** (1 episode × 30 steps)
- Det SFT steps: **60** (2 episodes × 30 steps)
- Tie steps (排除): 60
- **Internal label ratio: 30/90 = 33.3%**

### Step-level 数据完整性

两种 mode 的 step 都包含 `observation` + `action`：
- `always_internal`: keys = `[step, action, modality, score_before, score_after, score_delta, observation, llm_output]`
- `always_deterministic`: keys = `[step, action, modality, score_before, score_after, score_delta, candidates, observation]`

数据格式完整可用，但 internal 正样本量很少——只有 1 个 episode (30 steps)，占比仅 33.3%。尽管 find-non-living-thing 是唯一 internal-preferred task，episode-level 看实际上 deterministic 赢的更多 (2 vs 1)，prescreening 的聚合指标 (I=+31.6) 可能是被 ep4 的大幅领先拉高的均值效应。

---
