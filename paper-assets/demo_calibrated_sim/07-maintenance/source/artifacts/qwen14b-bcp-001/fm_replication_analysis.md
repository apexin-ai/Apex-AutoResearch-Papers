# FM Replication Analysis: qwen14b-bcp-001

**Model**: Qwen2.5-14B-Instruct FP16 (TP=2)  
**Experiment**: qwen14b-bcp-001, 4 runs × 6 variants × 20 scenarios  
**Date**: 2026-05-13

---

## Per-Variant Data (All 4 Runs)

### Task Completion Rate

| Variant | Run 1 | Run 2 | Run 3 | Run 4 | Mean |
|---------|-------|-------|-------|-------|------|
| uncalibrated_baseline | 0.737 | 0.550 | 0.579 | 0.600 | **0.616** |
| aave_target | 0.700 | 0.474 | 0.632 | 0.600 | **0.601** |
| indian_english_target | 0.650 | 0.600 | 0.842 | 0.650 | **0.686** |
| overcorrected | 0.750 | 0.500 | 0.600 | 0.650 | **0.625** |
| single_dim_question | 0.500 | 0.700 | 0.600 | 0.600 | **0.600** |
| single_dim_politeness | 0.600 | 0.800 | 0.474 | 0.750 | **0.656** |

### Mean Politeness Rate

| Variant | Run 1 | Run 2 | Run 3 | Run 4 | Mean |
|---------|-------|-------|-------|-------|------|
| uncalibrated_baseline | 0.470 | 0.588 | 0.497 | 0.536 | **0.523** |
| aave_target | 0.393 | 0.454 | 0.493 | 0.455 | **0.449** |
| indian_english_target | 0.462 | 0.442 | 0.427 | 0.444 | **0.444** |
| overcorrected | 0.453 | 0.419 | 0.466 | 0.467 | **0.451** |
| single_dim_question | 0.449 | 0.499 | 0.463 | 0.512 | **0.481** |
| single_dim_politeness | 0.489 | 0.438 | 0.456 | 0.403 | **0.447** |

### Mean Question Rate

| Variant | Run 1 | Run 2 | Run 3 | Run 4 | Mean |
|---------|-------|-------|-------|-------|------|
| uncalibrated_baseline | 0.037 | 0.035 | 0.054 | 0.041 | **0.042** |
| aave_target | 0.044 | 0.015 | 0.044 | 0.008 | **0.028** |
| indian_english_target | 0.038 | 0.023 | 0.027 | 0.018 | **0.027** |
| overcorrected | 0.015 | 0.028 | 0.010 | 0.011 | **0.016** |
| single_dim_question | 0.048 | 0.017 | 0.034 | 0.005 | **0.026** |
| single_dim_politeness | 0.018 | 0.023 | 0.016 | 0.021 | **0.020** |

### Gate Results

| Run | H1 | H2 | H3 |
|-----|----|----|-----|
| run_1 | PASS | FAIL | PASS |
| run_2 | PASS | PASS | PASS |
| run_3 | PASS | FAIL | PASS |
| run_4 | PASS | FAIL | PASS |
| **Aggregate** | **4/4** | **1/4** | **4/4** |

---

## FM1: Global Behavior Suppression

**Definition**: BCP variant completion significantly lower than baseline (retention < 80%).

| Variant | Mean Completion | Baseline (0.616) | Retention | FM1? |
|---------|----------------|-------------------|-----------|------|
| aave_target | 0.601 | 0.616 | **97.6%** | NO |
| indian_english_target | 0.686 | 0.616 | **111.2%** | NO |
| overcorrected | 0.625 | 0.616 | **101.4%** | NO |

**判断: FM1 未复现。** 所有 BCP variant 的 completion 保持率 > 97%，没有行为抑制。14B 模型在接到 BCP prompt 后仍然正常完成任务。

---

## FM2: Cross-Dimension Interference

**Definition**: Calibrating one dimension causes unintended degradation of another dimension.

### single_dim_question → politeness impact

| Metric | Baseline | single_dim_question | Change |
|--------|----------|-------------------|--------|
| Politeness | 0.523 | 0.481 | **-8.0%** (-4.2 pp) |

### single_dim_politeness → question_rate impact

| Metric | Baseline | single_dim_politeness | Change |
|--------|----------|---------------------|--------|
| Question Rate | 0.042 | 0.020 | **-52.8%** (-2.2 pp) |

**判断: FM2 部分复现（弱）。**
- question→politeness 方向：politeness 下降 8%（4.2 pp），效应较弱。
- politeness→question 方向：question_rate 相对下降 53%，但基线本身仅 4.2%，绝对下降仅 2.2 pp，可能在噪声范围内。
- 两个方向均存在跨维度干扰，但绝对幅度远小于 7B。

---

## FM3: Overcorrection Rebound

**Definition**: overcorrected variant 的 politeness 高于 baseline（模型被 overcorrection prompt "激发"出更高的 politeness）。

| Metric | Baseline | Overcorrected | Change |
|--------|----------|---------------|--------|
| Politeness | 0.523 | 0.451 | **-13.6%** (-7.1 pp) |

**判断: FM3 未复现。** overcorrected variant 的 politeness 低于 baseline（-7.1 pp），方向与 FM3 预测相反。14B 模型不会因 overcorrection prompt 产生反弹效应，反而略微降低 politeness。

---

## 与 7B 对比

| Failure Mode | 7B (mvp-004) | 14B (qwen14b-bcp-001) | 模式一致? |
|-------------|-------------|----------------------|----------|
| **FM1: Global Behavior Suppression** | 严重复现：AAVE 10%, Indian 15% vs baseline 36.8%（retention ~27-41%） | 未复现：所有 variant retention > 97% | **否** |
| **FM2: Cross-Dimension Interference** | 显著复现 | 弱复现：-8.0% politeness, -2.2pp question rate | **部分** |
| **FM3: Overcorrection Rebound** | 复现：overcorrected politeness > baseline | 未复现：overcorrected politeness < baseline (-7.1pp) | **否** |
| **H2 (Calibration Accuracy)** | FAIL | FAIL (3/4 runs) | **是** |
| **Mean Completion** | ~25% | ~61.6% | 14B >> 7B |

---

## 关键发现

14B 模型的 BCP 校准失败机制与 7B **根本不同**：

1. **7B 失败模式：灾难性崩溃。** BCP prompt 导致模型"冻结"——无法完成任务（completion 暴跌至 10-15%）、跨维度严重干扰、overcorrection 反弹。模型被 BCP prompt 严重干扰。

2. **14B 失败模式：选择性忽略。** 模型正常完成任务（completion ~62%），但 BCP prompt 几乎没有改变行为指标。所有 variant 的 politeness 和 question_rate 都接近 baseline。模型不是被 BCP "破坏"了，而是**无视**了 BCP 校准指令。

3. **共同点**：两种 scale 都 H2 FAIL——BCP 都未能成功校准目标行为维度。但失败原因不同：7B 是"过度响应导致崩溃"，14B 是"不够响应导致无效"。

4. **论文启示**：这揭示了一个 scale-dependent failure mode transition。BCP 作为校准方法在两个 scale 上都失败，但机制相反——这是一个重要的 finding，说明 BCP 的问题不仅仅是"prompt 设计不好"，而是方法论层面的缺陷。
