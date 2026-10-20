# code exp64 levene test

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp64_levene_test_20260522T231046_result.json`
- **Structured JSON:** [`77b7b5368190f599b20d.json`](../../sessions/77/77b7b5368190f599b20d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### DD OOD (Deceptive Delight)

| | mean | std | var |
|---|---|---|---|
| 9-class | 0.9968 | 0.0056 | 0.0000310 |
| Vanilla | 0.3123 | 0.0323 | 0.0010411 |

- **Levene's W = 1.946, p = 0.236** — 不显著
- 描述性方差比：Vanilla 方差是 9-class 的 **33.6×**

### AA (ActorAttack)

| | mean | std | var |
|---|---|---|---|
| 9-class | 0.9719 | 0.0320 | 0.001023 |
| Vanilla | 0.2575 | 0.0000 | 0.000000 |

- **Levene's W = 1.000, p = 0.374** — 不显著
- Vanilla 三个 seed F1 完全相同（0.2575），方差为 0，Levene test 退化

### 统计功效说明

n=3 per group → df₁=1, df₂=4。这个样本量下 Levene's test 的 power 极低（远低于 0.80 的常规阈值），即使 DD 的方差比达到 33.6 倍也未达显著性。结果**仅供参考，不具推断效力**。

### 结论

两个 OOD 条件下 Levene's test 均不显著（p > 0.05），但这主要是 n=3 的 power 不足所致，而非方差真正相等的证据。描述性数据显示 DD 上 Vanilla 方差远大于 9-class，AA 上 Vanilla 方差为 0（退化情况）。论文中 variance claim 保持 descriptive 处理是合理的。

---
