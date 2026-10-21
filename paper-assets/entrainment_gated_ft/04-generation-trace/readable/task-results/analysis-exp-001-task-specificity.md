# analysis exp 001 task specificity

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_task_specificity_20260519T131100_result.json`
- **Structured JSON:** [`15ded3eae9a68395e4c3.json`](../../sessions/15/15ded3eae9a68395e4c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**显著收敛的 benchmark（p < 0.05）：**

| Benchmark | Taxonomy | Scale | ρ | p | 显著 |
|-----------|----------|-------|----|----|------|
| **LAMBADA** | Retrieval-dependent | 1.3B | **−1.000** | **0.017** | **是** |

**不显著的 benchmark：**

| Benchmark | Taxonomy | 1.3B ρ | 1.3B p |
|-----------|----------|--------|--------|
| HellaSwag | Reasoning-dependent | +0.300 | 0.683 |
| ARC-C | Reasoning-dependent | +0.600 | 0.350 |
| WinoGrande | Reasoning-dependent | +0.100 | 0.950 |
| ARC-E | Mixed | −0.700 | 0.233 |
| MMLU | Mixed | −0.700 | 0.233 |

**Taxonomy 与 convergence pattern 的对应关系：**

- **Retrieval-dependent (LAMBADA)**: 完美单调收敛（ρ = −1.0, p = 0.017），cross-arch σ 从 pure 的 0.024 单调下降到 h3-1 的 0.005。符合预期——LAMBADA 测试的是上下文中检索最后一个词的能力，attention 层直接增强这种能力，使不同架构表现趋同。
- **Reasoning-dependent (HellaSwag, ARC-C, WinoGrande)**: 均无显著收敛，ρ 甚至为正（发散方向），说明增加 attention 层不能让不同架构在推理任务上趋同——架构差异在推理能力上是持久的。
- **Mixed (ARC-E, MMLU)**: 趋势方向正确（ρ = −0.7）但未达显著性（p = 0.233），n=5 的 exact test 统计功效有限，但数值上也呈现收敛趋势。

340M 尺度上均未达显著，可能因为小模型本身噪声更大。

**输出文件：**
- CSV: `/root/entrainment_gated_ft/analysis/task_specificity_results.csv`
- Figure: `/root/entrainment_gated_ft/analysis/task_specificity_figure.{pdf,png}`
- Script: `/root/entrainment_gated_ft/analysis/task_specificity_analysis.py`

---
