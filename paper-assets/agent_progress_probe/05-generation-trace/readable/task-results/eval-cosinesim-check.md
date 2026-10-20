# eval cosinesim check

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cosinesim-check_20260514T154822_result.json`
- **Structured JSON:** [`bd63b0e597f7a82d8b76.json`](../../sessions/bd/bd63b0e597f7a82d8b76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已足够，不需要再找 0.3129 来源了。分析脚本已运行完毕，结果如下：

---

## CosineSim Baseline 排查结果

### 实现方式
CosineSim baseline 计算窗口内**相邻 step embedding 之间的 cosine similarity 平均值**。假设 stagnation 窗口相邻 step 更相似（重复动作），progress 窗口相邻 step 差异更大。`fit()` 在 val set 上搜索最优 threshold（-1.0 到 1.01，步长 0.01）+ invert flag。

### 分数分布

| Split | Class | N | Mean | Std |
|-------|-------|---|------|-----|
| Test | Progress | 1339 | 0.6133 | 0.0892 |
| Test | Stagnation | 485 | 0.6923 | 0.1317 |
| Test | Overall | 1824 | 0.6343 | 0.1080 |

**关键发现：方向符合直觉但分离度很低。** Stagnation 确实有更高的 cosine sim（重复步骤更相似），但 mean 差仅 0.079，Cohen's d = 0.70（中等效应量），两类分布严重重叠。

### Threshold 搜索结果

| 评估方式 | Threshold | Invert | Macro-F1 |
|----------|-----------|--------|----------|
| Val-tuned (用于实际预测) | 0.61 | True | **0.5606** (test) |
| Oracle best on test | 0.70 | True | 0.7439 |

Val-tuned threshold 在 test 上达到 0.5606，不是 0.3129。

### 0.3129 是否合理？

**0.3129 大概率来自非 invert 方向或 threshold 不匹配的情况。** 从 threshold-F1 曲线看：
- 非 invert 模式下 threshold=0.60 → macro_f1=0.3768
- threshold=0.65 → macro_f1=0.2864

如果 val/test 分布漂移导致 val 上选的 threshold 不带 invert（或 threshold 值不同），0.31 附近的 F1 完全可能出现。

但当前代码实现的 `fit()` 是搜索了 invert 的，val 上最优是 invert=True + threshold=0.61，test 上给 0.5606。**所以如果代码正确执行，0.3129 不应该出现。** 可能的来源：
1. 早期版本代码没搜索 invert（只搜 threshold），导致用了错误方向
2. 评估时用了不同的 split 或没做 conf≥2 过滤

### 结论
- CosineSim baseline 的 **实际合理表现是 test macro_f1 ≈ 0.56**（val-tuned）
- 0.3129 可能来自早期未搜索 invert 的实现版本
- 即使优化后 0.56 也远低于 probe，因为两类 cosine sim 分布重叠严重（Cohen's d=0.70），单一标量特征无法有效分离

---
