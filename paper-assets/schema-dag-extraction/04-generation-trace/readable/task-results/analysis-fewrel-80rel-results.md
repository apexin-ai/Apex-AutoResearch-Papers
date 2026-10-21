# analysis fewrel 80rel results

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fewrel-80rel-results_20260515T133830_result.json`
- **Structured JSON:** [`95e04d36cc915ff61594.json`](../../sessions/95/95e04d36cc915ff61594.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据提取完成。

## FewRel 80-rel 实验结果

### 文件状态
所有文件完整，但时间戳为 21:05-21:17 UTC（新 run PID 269256 的产出，原始结果已被覆盖）。新 run 也完整完成了 exp1 + exp2，结果可用。

### Exp1: Count Curve

| count | accuracy | n_batches | mean_BCS |
|-------|----------|-----------|----------|
| 1     | 0.8573   | 80        | 0.0000   |
| 4     | 0.8667   | 5         | 0.6335   |
| 8     | 0.8021   | 5         | 0.7175   |
| 16    | 0.6958   | 5         | 0.7950   |
| 32    | 0.6578   | 5         | 0.8893   |
| 64    | 0.5424   | 5         | 0.9434   |
| 80    | 0.5042   | 5         | 0.9706   |

### Exp2: BCS-Controlled

| count | low_BCS acc | low_BCS | high_BCS acc | high_BCS | random acc | delta |
|-------|-------------|---------|--------------|----------|------------|-------|
| 8     | 0.8229      | 0.4715  | 0.5104       | 0.9706   | 0.8025     | **+31.2pp** |
| 16    | 0.8281      | 0.5705  | 0.5156       | 0.9706   | 0.7169     | **+31.2pp** |

### 与 16-rel 对比

| 指标 | 16-rel | 80-rel | 分析 |
|------|--------|--------|------|
| count_1 acc | 0.904 | 0.857 | 80-rel baseline 更低（更多 relation → 更难） |
| count_4 acc | 0.932 | 0.867 | |
| count_8 acc | 0.867 | 0.802 | |
| count_16 acc | 0.778 | 0.696 | |
| degradation (1→max) | 0.904→0.778 (-12.6pp) | 0.857→0.504 (-35.3pp) | **80-rel degradation 远强于 16-rel** |
| BCS Δ (exp2) | -9.1pp | -31.2pp | **BCS effect 在 80-rel 下放大 3.4x** |

关键发现：
- 80-rel 的 count curve 展现出从 0.857 到 0.504 的持续下降，degradation 幅度 (35.3pp) 远大于 16-rel (12.6pp)
- BCS effect 从 16-rel 的 -9.1pp 暴增到 -31.2pp，说明 schema 复杂度对模型性能的影响随 relation 数量增加而显著放大
- 符合预期：更多 relations → 更大的 confusion space → 更强的 degradation + BCS effect

---
