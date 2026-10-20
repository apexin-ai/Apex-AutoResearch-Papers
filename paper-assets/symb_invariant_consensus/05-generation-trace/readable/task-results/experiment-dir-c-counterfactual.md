# experiment dir c counterfactual

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-c-counterfactual_20260520T152704_result.json`
- **Structured JSON:** [`602748e870dfe9fb3b75.json`](../../sessions/60/602748e870dfe9fb3b75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。

**Direction C Pilot — 20 题 (exp033 Mistral-7B)**

| 策略 | Accuracy | vs Full |
|------|----------|---------|
| **full** (SICA baseline) | 13/20 = 65.0% | — |
| **signal** (仅 conclusion-referencing) | 13/20 = 65.0% | net 0 |
| **premise** (去掉 conclusion-referencing) | **14/20 = 70.0%** | **net +1** |
| **rules_only** (去掉 fact 类型) | 12/20 = 60.0% | net -1 |
| SC | 13/20 = 65.0% | — |

**关键发现：**

1. **premise 策略是唯一有正向信号的**：保留 40.2% 的 constraints（去掉了引用 conclusion 的），accuracy +5pp (65%→70%)。在 folio_8 上修正了 full SICA 的错误，没有引入新错误。

2. **signal 策略（纯 counterfactual）中性**：保留 59.8% 的 constraints，精度持平。在 folio_14 上翻对了一题，但 folio_17 翻错了一题，net=0。

3. **rules_only 策略负面**：过于激进（只保留 35.6%），丢掉了 folio_10 和 folio_17。

4. **folio_8 是 premise 策略的一个干净 gain**：去掉 conclusion-referencing constraints 后，SICA 从 False→Unknown（正确答案），说明那些引用 conclusion 的 constraints 确实引入了偏差。

20 题样本偏小，但 **premise-only 方向有微弱正信号**，值得扩到全 204 题验证。

---
