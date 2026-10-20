# analysis cohens d qwen

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cohens-d-qwen_20260514T080316_result.json`
- **Structured JSON:** [`4dd546d012fa558feb02.json`](../../sessions/4d/4dd546d012fa558feb02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。Cross-model 对比：

```
Sparsity   DeepSeek d                    Qwen d                       DeepSeek    Qwen
s015       0.4416 [0.3548, 0.7836]       0.2811 [-0.0063, 0.5967]     small       small
s020       0.5195 [0.4319, 0.9011]       0.5494 [0.2263, 1.0204]      medium      medium
s025       0.6831 [0.5576, 0.8634]       0.8894 [0.6906, 1.1981]      medium      large
s030       0.8031 [0.6659, 1.0191]       1.0220 [0.8639, 1.3275]      large       large
```

两个模型趋势一致：sparsity 增大 → Cohen's d 单调递增（phase 间 II 差异增大）。Qwen 在 s015 效应更弱（CI 跨零），但在 s025/s030 效应反而更强于 DeepSeek（0.89 vs 0.68, 1.02 vs 0.80）。Qwen 跳过了 4 个 problem（vs DeepSeek 1 个），因为有更多 problem 缺少 high 或 low phase 数据。

---
