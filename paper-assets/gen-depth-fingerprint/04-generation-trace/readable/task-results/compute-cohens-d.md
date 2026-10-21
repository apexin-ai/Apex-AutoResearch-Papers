# compute cohens d

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_cohens-d_20260518T084239_result.json`
- **Structured JSON:** [`fc4bfb0b5274a5f1db79.json`](../../sessions/fc/fc4bfb0b5274a5f1db79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### 数据概况
- 总行数: 27,529 (6 个模型, depth 0-4)
- 排除 gen-0 后: 21,557 行 (gen-1: 5,918, gen-2+: 15,639)
- Class-balanced 后: 11,836 行 (每组 5,918)

### Pooled Cohen's d: gen-1 vs gen-2+ (class-balanced)

| Feature | Cohen's d | 95% CI | \|d\| | Category |
|---|---|---|---|---|
| entropy_mean | +1.1690 | [+1.1161, +1.2200] | 1.1690 | drifting |
| ttr | +0.8765 | [+0.8338, +0.9230] | 0.8765 | drifting |
| hapax_ratio | +0.7559 | [+0.7101, +0.7996] | 0.7559 | drifting |
| entropy_std | +0.5453 | [+0.5058, +0.5845] | 0.5453 | drifting |
| entropy_max | +0.0795 | [+0.0434, +0.1145] | 0.0795 | stationary |
| tail_decay | +0.0745 | [+0.0396, +0.1086] | 0.0745 | stationary |
| entropy_min | -0.0247 | [-0.0584, +0.0127] | 0.0247 | stationary |

4 个特征 drifting (\|d\| > 0.5): entropy_mean (大效应, d=1.17), ttr, hapax_ratio, entropy_std。3 个特征 stationary (\|d\| < 0.2): entropy_max, tail_decay, entropy_min。没有 intermediate 类 (0.2 < \|d\| < 0.5)。所有正 d 值表示 gen-1 均值高于 gen-2+，即这些特征随生成深度递减。

---
