# analysis r14 a8 oracle gap

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_a8_oracle_gap_20260518T184954_result.json`
- **Structured JSON:** [`5c797e8181ac8be0e105.json`](../../sessions/5c/5c797e8181ac8be0e105.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Oracle Gap (K=5 consecutive trigger, early detection before CP), test set 60/20/20 seed=42:

```
Model     Oracle Gap   Count    Mean Lead Time
R1-8B     76.7%        33/43    31.0 steps
OT-7B     93.6%        44/47    50.0 steps
R1-32B    50.0%        10/20    32.4 steps
QwQ-32B   84.2%        16/19    24.4 steps
```

OT-7B 最高 (93.6%)，因为其 trace 更长、CP 前有更多 non-safety 标注；R1-32B 最低 (50.0%)，test set 只有 20 条且 median CP=15 较早，CP 前 non-safety 窗口不足。

关于 R1-8B 参考值：task 提到 85.5%，实际 test set 为 76.7%。85.5% 对应 val set (85.4%)，可能来自早期分析。4 个模型均使用相同代码路径 (`analyze_oracle` from `oracle_upper_bound.py`)，结果可直接对比。

结果已存入 `artifacts/r14_a8_oracle_gap/oracle_gap_all_models.json` 并注册。

---
