# code fix kstar theta ci data

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_kstar_theta_ci_data_20260515T130830_result.json`
- **Structured JSON:** [`a6065cbe3fa06292bc27.json`](../../sessions/a6/a6065cbe3fa06292bc27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果符合预期。

---

### 旧 ci_half vs 新 ci_half 对比

| Model | Pair | 旧 ci_half | 新 ci_half (exp-007) | 变化 |
|---|---|---|---|---|
| **Qwen-rewrite** | 0v1 | 0.003 | 0.00095 | ↓ 3.2× |
| | 1v2 | 0.025 | 0.0091 | ↓ 2.7× |
| | 2v3 | 0.020 | 0.0098 | ↓ 2.0× |
| | 3v4 | 0.015 | 0.0109 | ↓ 1.4× |
| | 4v5 | 0.012 | 0.0105 | ↓ 1.1× |
| **Pythia** | 0v1 | 0.004 | 0.0011 | ↓ 3.6× |
| | 1v2 | 0.028 | 0.0088 | ↓ 3.2× |
| | 2v3 | 0.022 | 0.01055 | ↓ 2.1× |
| | 3v4 | 0.014 | 0.01095 | ↓ 1.3× |
| | 4v5 | 0.011 | 0.0114 | ↑ 1.04× |
| **OLMo** | 0v1 | 0.002 | 0.00055 | ↓ 3.6× |
| | 1v2 | 0.030 | 0.0101 | ↓ 3.0× |
| | 2v3 | 0.024 | 0.00985 | ↓ 2.4× |
| | 3v4 | 0.013 | 0.01135 | ↓ 1.1× |
| | 4v5 | 0.010 | 0.0109 | ↑ 1.09× |
| **Qwen-cont** | 0v1 | 0.002 | 0.00075 | ↓ 2.7× |
| | 1v2 | 0.029 | 0.0099 | ↓ 2.9× |
| | 2v3 | 0.023 | 0.01005 | ↓ 2.3× |
| | 3v4 | 0.016 | 0.01 | ↓ 1.6× |
| | 4v5 | 0.012 | 0.011 | ↓ 1.1× |

旧 CI 整体偏大 1.1–3.6 倍，尤其 1v2 pair 偏大最严重（~3×）。

### θ=0.60 时 K* 结果

| Model | K*(0.60) |
|---|---|
| Qwen-rewrite | **2** |
| Pythia | **2** |
| OLMo | **2** |
| Qwen-cont | **2** |

**4/4 unanimous K\*=2**，验证通过。所有模型 1v2 的 ci_lower > 0.60（例如 Qwen-cont 最低：0.6112 - 0.0099 = 0.6013 > 0.60），而 2v3 的 ci_lower < 0.60。

Unanimous K\*=2 区间：θ ∈ [0.580, 0.600]；K\* ∈ {2,3} 区间：θ ∈ [0.535, 0.600]。

---
