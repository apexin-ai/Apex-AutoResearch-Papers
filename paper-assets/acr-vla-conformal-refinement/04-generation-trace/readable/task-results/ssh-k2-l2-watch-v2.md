# ssh k2 l2 watch v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_k2-l2-watch-v2_20260519T223624_result.json`
- **Structured JSON:** [`ca30d6330ce5f8205bb8.json`](../../sessions/ca/ca30d6330ce5f8205bb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 在第 1 次尝试就找到了。结果如下：

## K=2 L2 校准结果

### 实验配置
- Benchmark: object, 5 episodes, seed=42
- 采集步数: 14,512
- ODE steps: 10

### Spearman 相关性

| 指标对 | Spearman ρ | p-value | Go/No-Go |
|--------|-----------|---------|----------|
| K2_L2 vs FMVD | **0.0925** | 6.03e-29 | **No-Go** (ρ < 0.3) |
| K2_L2 vs K10_variance | **0.9979** | 0.0 | **Go** (ρ >> 0.3) |
| K10_variance vs FMVD (baseline) | **0.0825** | 2.33e-23 | **No-Go** (ρ < 0.3) |

### 统计摘要

| 指标 | Mean | Std | P25 | P50 | P75 | P90 |
|------|------|-----|-----|-----|-----|-----|
| FMVD | 0.0549 | 0.0403 | 0.0277 | 0.0467 | 0.0709 | 0.0938 |
| K10 variance | 0.0049 | 0.0056 | — | — | — | — |
| K2 L2 | 0.0807 | 0.0361 | 0.0550 | 0.0749 | 0.0987 | 0.1265 |

### Go/No-Go 判断

**K2 L2 作为 K10 variance 的廉价替代：Go** — ρ=0.9979，近乎完美相关，K2 L2 可以完美替代 K10 variance 作为不确定性代理。

**K2 L2 作为 FMVD 的预测器：No-Go** — ρ=0.0925，远低于 0.3 阈值。但这与 K10 variance vs FMVD 的 ρ=0.0825 一致，说明问题不在 K2 近似，而在于 ODE variance 类指标本身与 FMVD 的相关性就很弱。

---
