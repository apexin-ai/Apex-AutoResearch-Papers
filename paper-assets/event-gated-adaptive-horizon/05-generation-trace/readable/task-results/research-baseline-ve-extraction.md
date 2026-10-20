# research baseline ve extraction

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_baseline_ve_extraction_20260514T053023_result.json`
- **Structured JSON:** [`8408b497d7919450d850.json`](../../sessions/84/8408b497d7919450d850.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整数据如下：

## Baseline (exp_001) v/e Ratio Trajectory

| Step | value_mean | eval_return | v/e ratio |
|-----:|-----------:|------------:|----------:|
| 5K | 0.00 | 31.77 | 0.0% |
| 15K | 5.36 | 206.61 | 2.6% |
| 25K | 34.48 | 395.27 | 8.7% |
| 35K | 93.71 | 388.47 | 24.1% |
| 45K | 170.07 | 513.77 | 33.1% |
| 55K | 252.50 | 625.73 | 40.4% |
| 65K | 346.69 | 615.86 | 56.3% |
| 75K | 428.98 | 596.28 | 71.9% |
| 85K | 500.22 | 713.93 | 70.1% |
| 95K | 550.52 | 871.06 | 63.2% |
| 105K | 601.06 | 915.67 | 65.6% |
| 115K | 627.88 | 919.81 | 68.3% |
| 125K | 632.32 | 921.37 | 68.6% |
| 135K+ | ~663-666 | ~900-970 | **68.5%-72.8%** |

### 关键发现

1. **Baseline 稳态 v/e ratio 约 69-72%**，从 ~135K 步开始稳定在这个范围。

2. **008a 的 37% 是严重的悲观偏差。** Baseline 在同等训练阶段的 v/e ratio 是 ~70%，008a 的 37% 不到 baseline 的一半。"pessimistic bias" 这个术语完全成立。

3. **v/e ratio 的演化轨迹：**
   - 0-55K：快速上升（0% → 40%），value 在追赶 return
   - 55K-135K：继续上升（40% → 70%），value 逐渐逼近
   - 135K+：稳定在 **69-72%** 区间，轻微波动

4. **Baseline 的 v/e 从未在 35-40% 停留过**——那只是过渡阶段（45K-55K 步），之后持续上升到 70%。所以 008a 长期停在 37% 是异常的，不是正常水平。

---
