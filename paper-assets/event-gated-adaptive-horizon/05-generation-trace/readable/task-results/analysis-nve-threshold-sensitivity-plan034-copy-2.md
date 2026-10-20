# analysis nve threshold sensitivity plan034

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve_threshold_sensitivity_plan034_20260525T035039_result.json`
- **Structured JSON:** [`de8603fece15b0dff8d8.json`](../../sessions/de/de8603fece15b0dff8d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果汇总：

**数据集**: 26 个实验（7 CIVO-positive, 19 CIVO-negative），覆盖 Walker/Cheetah/Cartpole 三个环境。

**Threshold Sensitivity**:

| Threshold | TP | FP | TN | FN | Precision | Recall | F1 | Accuracy |
|-----------|----|----|----|----|-----------|--------|------|----------|
| 1.3× | 7 | 4 | 15 | 0 | 0.636 | 1.000 | 0.778 | 0.846 |
| **1.5×** | **7** | **2** | **17** | **0** | **0.778** | **1.000** | **0.875** | **0.923** |
| 1.7× | 5 | 2 | 17 | 2 | 0.714 | 0.714 | 0.714 | 0.846 |
| 2.0× | 5 | 0 | 19 | 2 | 1.000 | 0.714 | 0.833 | 0.923 |

**AUROC = 0.970**

**关键发现**:
- 1.5× 是最优阈值（max F1 = 0.875），完美 recall（7/7 positive 全部检出）
- 1.5× 处 2 个 FP：frozen Walker s1 (NVE=1.71) 和 s2 (NVE=1.88)，均为 transient spikes
- 2.0× 达到 precision=1.0 但漏检 Walker s2 (NVE=1.62) 和 s3 (NVE=1.53)
- 1.3× recall 完美但 FP 增至 4 个（加入 008f_s4 和 Cheetah frozen）
- 阈值选择在 1.3×–2.0× 范围内鲁棒，AUROC 不依赖单一阈值

已注册 artifact：JSON 数据 (`art_20260525_20aa79`) + LaTeX 表格 (`art_20260525_58c709`)。

---
