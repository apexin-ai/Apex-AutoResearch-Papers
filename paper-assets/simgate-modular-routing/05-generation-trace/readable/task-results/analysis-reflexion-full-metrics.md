# analysis reflexion full metrics

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reflexion-full-metrics_20260517T163356_result.json`
- **Structured JSON:** [`be49d3dcea09b63551f4.json`](../../sessions/be/be49d3dcea09b63551f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是完整结果：

## Reflexion Baseline 详细 Metrics

### Per-Task 汇总表

| Task | N | Death Rate | Success Rate | Mean (all) | Mean (alive) | T1 Death | T2 Death | T3 Death | Rescued |
|------|---|-----------|-------------|-----------|-------------|---------|---------|---------|---------|
| chemistry-mix | 20 | 30.0% | 20.0% | -26.8 | 4.6 | 50.0% | 44.4% | 33.3% | 5 |
| find-animal | 20 | 35.0% | 25.0% | -28.8 | 9.5 | 50.0% | 47.1% | 46.7% | 3 |
| find-non-living-thing | 20 | 0.0% | 65.0% | 30.8 | 30.8 | 0.0% | 0.0% | 0.0% | 0 |
| freeze | 20 | 50.0% | 10.0% | -49.2 | 1.5 | 50.0% | 52.6% | 52.6% | 1 |
| grow-fruit | 20 | 30.0% | 25.0% | -28.6 | 1.9 | 45.0% | 20.0% | 40.0% | 4 |
| identify-life-stages-1 | 20 | 30.0% | 5.0% | -28.8 | 1.8 | 30.0% | 31.6% | 31.6% | 0 |
| identify-life-stages-2 | 20 | 25.0% | 5.0% | -24.2 | 1.1 | 25.0% | 26.3% | 26.3% | 0 |
| inclined-plane-determine-angle | 20 | 30.0% | 10.0% | -24.5 | 7.9 | 55.0% | 45.0% | 31.6% | 5 |
| lifespan-longest-lived | 20 | 30.0% | 10.0% | -26.2 | 5.4 | 55.0% | 35.0% | 33.3% | 5 |
| lifespan-longest-lived-then-shortest | 20 | 35.0% | 5.0% | -33.4 | 2.5 | 50.0% | 40.0% | 36.8% | 3 |
| measure-melting-point-unknown | 20 | 50.0% | 10.0% | -49.3 | 1.4 | 50.0% | 50.0% | 55.6% | 1 |
| **OVERALL** | **220** | **31.4%** | **17.3%** | **-26.3** | **7.4** | **41.8%** | **37.6%** | **37.1%** | **27** |

### Per-Part 汇总
- Part 1 (6 tasks, 120 eps): death=29.2%, success=25.0%
- Part 2 (5 tasks, 100 eps): death=34.0%, success=8.0%

### Trial 转换分析

| 转换 | Fix (死→活) | Break (活→死) | 净收益 |
|------|------------|--------------|--------|
| T1→T2 | 24 | 5 | +19 |
| T2→T3 | 16 | 12 | +4 |
| **总计** | **40** | **17** | **+23** |

### Reflexion 效果评估

关键数据：
- **T1 death rate = 41.8%** (几乎等于 7B baseline 42.9%，说明单次表现相当)
- 经过 reflexion 后最终 death rate 降至 **31.4%** (减少 11.5pp vs 7B baseline)
- 194 个需要 reflexion 的 episodes 中：
  - 仅 **14.9% (29/194)** 最终得分改善
  - **83.0% (161/194)** 得分不变
  - 仅 **6.2% (12/194)** 最终成功
- 27/92 T1 死亡的 episodes 被"救回"(29.3%)

### 核心发现

1. **Reflexion 对 death 的修复有限**：T1→T2 death rate 仅从 41.8% 降到 37.6%，T3 进一步降到 37.1%。减少幅度远小于预期。

2. **Reflexion 会引入新死亡**：17 个本来存活的 episode 在后续 trial 中反而死亡（尤其 T2→T3 有 12 个 break）。

3. **Task 差异巨大**：`find-non-living-thing` 完全无死亡(0%)，而 `freeze` 和 `measure-melting-point` 高达 50%。

4. **成功率极低**：除 `find-non-living-thing`(65%)外，多数 task 成功率 ≤25%，Part2 tasks 平均仅 8%。

5. **vs 7B baseline**：Reflexion 的优势主要来自多次尝试的机会(3 trials)，而非 reflection 本身带来的策略改进。T1 表现(41.8% death)与 7B 单次 baseline(42.9%)基本持平。

---
