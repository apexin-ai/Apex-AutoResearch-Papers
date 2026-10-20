# fetch bootstrap ohfix results

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fetch_bootstrap-ohfix-results_20260515T093958_result.json`
- **Structured JSON:** [`c81e181d7c5e5c4383ca.json`](../../sessions/c8/c81e181d7c5e5c4383ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**已拉取文件**：`artifacts/gold_set/bootstrap_ci_ohfix.json`

**OH 判断逻辑确认**（第374行）：
```python
is_oh = "__openhands__" in w.get("trajectory_id", "")
```
Worker 用的是 `trajectory_id` 字段中是否包含 `__openhands__` 来判断 OpenHands 轨迹，而非文件路径。

**关键结果摘要**：
| 对比 | n | ΔF1 | 95% CI | p | sig |
|------|---|-----|--------|---|-----|
| GB vs MV | 195 | +0.046 | [0.006, 0.088] | 0.012 | **yes** |
| GB vs GRU Probe | 132 | +0.050 | [−0.016, 0.120] | 0.070 | no |
| RF vs GB | 195 | −0.013 | [−0.037, 0.009] | 0.136 | no |
| TWV Probe vs GB | 132 | −0.016 | [−0.067, 0.031] | 0.254 | no |
| TWV Probe vs GRU | 132 | +0.034 | [−0.029, 0.099] | 0.150 | no |

唯一显著的仍是 GB vs MV（p=0.012）。

---
