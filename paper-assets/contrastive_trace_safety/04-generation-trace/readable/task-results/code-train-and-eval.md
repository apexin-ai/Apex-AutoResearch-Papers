# code train and eval

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_train_and_eval_20260516T191922_result.json`
- **Structured JSON:** [`ec937a85e590bbba917c.json`](../../sessions/ec/ec937a85e590bbba917c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 评估结果汇总

### 训练日志

两个 probe 均训练完成，无代码修改。

| Probe | Final Loss | Final Train Acc |
|-------|-----------|-----------------|
| Static MLP | 0.0007 | 100.0% |
| Temporal | 0.0248 | 99.14% |

### 评估结果对比 (43 test traces)

| 指标 | Static Probe | Temporal Probe |
|------|-------------|----------------|
| Step accuracy | 0.7777 ± 0.2072 | 0.7573 ± 0.2469 |
| Detection rate | 39.53% | 34.88% |
| Lead time (mean) | **-8.9 steps** | -10.7 steps |
| Lead time (median) | -3.0 steps | -3.0 steps |
| Earliest detection (mean step) | 31.7 | 32.6 |
| Crossing rate | 53.49% | 46.51% |
| Crossing lead time (mean) | +0.7 steps | -1.1 steps |
| Crossing lead time (median) | -1.0 steps | -1.0 steps |

### Pass/Fail 判断

**关键指标**：temporal probe lead time - static probe lead time = (-10.7) - (-8.9) = **-1.8 steps**

要求：temporal lead time - static lead time ≥ 3 → **FAIL**

Temporal probe 不仅没有比 static probe 提早检测，反而更晚了 1.8 步。两个 probe 的 lead time 都是负值（检测发生在 commitment point 之后），说明两者都在检测"已发生"的 commitment 而非提前预警。

### 关键观察

1. **两个 probe 都太晚了**：平均 lead time 都是负数，说明检测发生在 commitment point 之后
2. **Static probe 反而优于 temporal**：accuracy 更高 (0.778 vs 0.757)、detection rate 更高 (39.5% vs 34.9%)、crossing rate 更高 (53.5% vs 46.5%)
3. **训练过拟合**：训练 accuracy 接近 100% 但测试 accuracy 仅 ~77%，temporal probe 尤其严重（20480 维输入更容易过拟合）
4. **无代码修改**：pipeline 运行无 bug

---
