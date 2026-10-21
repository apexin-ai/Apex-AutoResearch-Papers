# exp steering qwen L18 122 collect

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_steering-qwen-L18-122-collect_20260523T103910_result.json`
- **Structured JSON:** [`5ff5f9ff7418e0b5bbe5.json`](../../sessions/5f/5ff5f9ff7418e0b5bbe5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Qwen L18 (Layer 18)

**状态: 完成** (PID 568435 已退出)

**Probe accuracy: 73.81%**

Baseline 分布: contextual=35, both=20, neither=21, parametric=8 (共 84 conflict samples)

| Alpha | Steering flips | Control flips | Fisher p |
|-------|---------------|---------------|----------|
| +5.0  | 3/84 (3.6%)   | 1/84 (1.2%)   | 0.6205   |
| +10.0 | 3/84 (3.6%)   | 1/84 (1.2%)   | 0.6205   |
| +20.0 | 3/84 (3.6%)   | 2/84 (2.4%)   | 1.0000   |

**注意：只跑了正方向 alpha（+5/+10/+20），没有负方向（-5/-10/-20）。** 且所有 flips 均无方向性（p→c: 0, c→p: 0）。

**Bonferroni 显著: 无** — 所有 p 值远大于任何合理阈值。

**结论：L18 steering 完全无效。** 即使 alpha 从 5 增大到 20，flip 数量恒定为 3，且无方向性变化。Steered distribution 在三个 alpha 下完全相同（both=20, parametric=10, neither=19, contextual=35），说明模型输出几乎未被扰动。

```
JSON 路径: /root/clkc_mech_interp/data/qwen3/steering_results_L18_last.json
Log 路径: /root/clkc_mech_interp/logs/steering_qwen_L18.log
```

---
