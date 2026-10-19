# analysis steering 107

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_steering_107_20260522T105154_result.json`
- **Structured JSON:** [`fc21f642d4c935e92bf1.json`](../../sessions/fc/fc21f642d4c935e92bf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## steering_107 分析完成 — 结论：**NEGATIVE**

### 核心数据

**Baseline** (n=136): contextual 41 | both 35 | parametric 32 | neither 28

| alpha | steering flip rate | random flip rate | Fisher p | p→c / c→p |
|------:|-------------------:|-----------------:|---------:|----------:|
| -20 | **14.7%** | 16.9% | 0.740 | 0 / 2 |
| -10 | 10.3% | 9.6% | 1.000 | 0 / 1 |
| -5 | 4.4% | 3.7% | 1.000 | 1 / 0 |
| -2 | 3.7% | 2.9% | 1.000 | 1 / 0 |
| -1 | 4.4% | 2.9% | 0.749 | 2 / 0 |
| +1 | 0.7% | 0.7% | 1.000 | 0 / 0 |
| +2 | 2.2% | 1.5% | 1.000 | 0 / 0 |
| +5 | 3.7% | 4.4% | 1.000 | 0 / 0 |
| +10 | 7.4% | 6.6% | 1.000 | 0 / 0 |
| +20 | 12.5% | **17.6%** | 0.309 | 1 / 0 |

### 判断

**假设证伪。** 三条核心证据：

1. **最高 steering flip rate 14.7%（α=-20），未达 ≥15% 阈值**，且对应 random 更高（16.9%）
2. **所有 alpha 的 Fisher p > 0.3**，steering 与 random 方向无统计差异
3. **方向性 flips (p→c + c→p) 总计仅 9 次**——观测到的 "flips" 几乎都是进出 both/neither 的噪声，而非 parametric↔contextual 定向转换

Flip 率随 |alpha| 单调递增且 steering/random 对称，说明 flips 由扰动幅度驱动，与方向无关。

### 对论文的影响

- 探针的判别精度（77.6%）作为**相关性发现**仍成立
- **不能声称因果性**——这是一个 clean negative result
- 可作为 "correlation ≠ causation" 的讨论点：线性探针高精度 ≠ mechanistic understanding

### 建议下一步

1. **Activation patching / causal tracing** — 定位真正的因果节点，不假设 probe direction = causal direction
2. **DAS (Distributed Alignment Search)** — 非线性/多层干预方向
3. **多层联合 steering** — 因果机制可能跨层分布
4. **非线性探针对比** — MLP probe 看因果方向是否在非线性子空间

Registry 已更新：status=DONE, conclusion=negative, metrics 已写入。Artifact 已注册。

---
