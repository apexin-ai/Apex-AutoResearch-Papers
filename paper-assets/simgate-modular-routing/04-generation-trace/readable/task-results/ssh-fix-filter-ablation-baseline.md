# ssh fix filter ablation baseline

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-filter-ablation-baseline_20260518T235241_result.json`
- **Structured JSON:** [`adc801b332dbeba2ee92.json`](../../sessions/ad/adc801b332dbeba2ee92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。`baseline_comparison` 现在为：

```json
{
  "baseline_death_rate": 0.48,
  "baseline_daf": 0.904,
  "baseline_episodes": 200,
  "baseline_source": "retry_dose_response_n1",
  "delta_vs_baseline": -0.19
}
```

- `baseline_death_rate`: 0.429 → **0.48**
- `baseline_episodes`: 245 → **200**
- 新增 `baseline_source`: `"retry_dose_response_n1"`
- 新增 `delta_vs_baseline`: **-0.19** (filter DR 0.29 - baseline 0.48 = -19pp)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "baseline_death_rate": 0.48,
    "baseline_daf": 0.904,
    "baseline_episodes": 200,
    "baseline_source": "retry_dose_response_n1",
    "delta_vs_baseline": -0.19
  }
}
```

</details>

---
