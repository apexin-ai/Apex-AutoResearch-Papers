# ops rebuttal llama5 check

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rebuttal-llama5-check_20260524T035124_result.json`
- **Structured JSON:** [`4fbd323080f428a1ae1c.json`](../../sessions/4f/4fbd323080f428a1ae1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕，汇总结果：

## Llama 5% Contamination 结果

### 1. lz* 值

| 指标 | 值 |
|------|-----|
| **lz\* (free-θ)** | **-4.9540** |
| theta_MLE | -0.4089 |
| accuracy_overall | 0.6342 |
| lz\* (fixed-θ) | **不存在** — `theta_fixed_llama.json` 只有 clean/15%/50%，没有 5% |
| n_items | 14,042 |

### 2. Cohen's d（用 V2 clean baseline）

```
d = (-4.9540 - 0.2618) / 1.5416 = -5.2158 / 1.5416 = -3.3834
|d| = 3.38
```

### 3. Item selection seed

确认 seed=999，`prepare_data_5pct.py` 第 38 行 `rng_contam = random.Random(999)`。5% 是 15% 的子集（代码中有 assert 验证）。

### 4. 数据条数

- 训练数据：5,702 条（5,000 alpaca + 702 MMLU items）
- seen items: 702 个（`seen_items_5pct.json` 存在但 eval_lz.py 没读取它）

### 5. 异常问题

**lz\* = -4.954 for 5% 比 50% (-2.858) 更极端，违反直觉的 dose-response。** 但这可能是合理的：

- 5% 只污染 702 个 item，其中包含一些高难度 item
- 模型在这些 item 上异常答对，但整体能力 (θ=-0.41) 仍较低
- 这种 "低能力 + 少量难题答对" 的模式对 lz\* 来说恰恰是最 aberrant 的
- 50% 污染则更均匀地提升能力（θ=-0.15），response pattern 反而更像一个高能力考生

**但 eval_lz.py 有一个 bug**：它没有为 contam_5 加载 seen_items（只硬编码了 15/25/50%），导致 n_seen=0。这不影响 overall lz_star 的计算，但 seen/unseen 分拆分析缺失。

### 6. 需要做什么

- **不需要重新训练**，checkpoint 存在且正常
- **需要重新评估**：
  1. 更新 eval_lz.py 加入 contam_5 的 seen_items 路径
  2. 重新跑 theta_fixed 分析，加入 contam_5 条件
  3. 可以用现有 response_vector 直接重算，不需要重新推理

---
