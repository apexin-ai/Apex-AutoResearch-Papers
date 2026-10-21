# analysis mae qwk adjacent

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mae_qwk_adjacent_20260518T142858_result.json`
- **Structured JSON:** [`daae3e06b0a431df881e.json`](../../sessions/da/daae3e06b0a431df881e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部计算完成。结果已保存到 `results/reviewer_metrics/mae_qwk_analysis.json`。

## 结果汇总

### Within-distribution (9 cells, RF 5-fold CV OOF)

| Cell | MAE | QWK | QWK(d1-d3) |
|------|-----|-----|------------|
| pythia_nucleus | 0.2346 | 0.8903 | 0.7304 |
| pythia_temp09 | 0.2581 | 0.8774 | 0.6995 |
| pythia_topk50 | 0.3589 | 0.8193 | 0.5669 |
| gpt2xl_nucleus | 0.1684 | 0.9233 | 0.8196 |
| gpt2xl_temp09 | 0.1447 | 0.9398 | 0.8521 |
| gpt2xl_topk50 | 0.2554 | 0.8850 | 0.7221 |
| olmo_nucleus | 0.2293 | 0.8941 | 0.7545 |
| olmo_temp09 | 0.1833 | 0.9228 | 0.8082 |
| olmo_topk50 | 0.2752 | 0.8744 | 0.6961 |
| **Mean** | **0.2342** | **0.8918** | **0.7388** |

**|Δ| 分布** (180K samples pooled): |0|=78.42%, |1|=19.80%, |2|=1.70%, |3|=0.07%
**Adjacent accuracy** (|Δ|≤1): **98.23%**

### Cross-model LOO Transfer

| Holdout | MAE | QWK | QWK(d1-d3) |
|---------|-----|-----|------------|
| Pythia | 0.4538 | 0.7793 | 0.4331 |
| OLMo | 0.3438 | 0.8332 | 0.5980 |
| GPT-2 XL | 0.3701 | 0.8043 | 0.5538 |
| **Mean** | **0.3892** | **0.8056** | **0.5283** |

**|Δ| 分布** (180K samples): |0|=66.40%, |1|=28.42%, |2|=5.03%, |3|=0.15%
**Adjacent accuracy**: **94.82%**

### 要点

- Within-distribution QWK 0.89 表明 ordinal agreement 很强，98.2% 预测在 ±1 depth 内
- Cross-model transfer QWK 从 0.89 降至 0.81（降幅 ~9%），MAE 从 0.23 升至 0.39
- d1-d3 QWK 在 transfer 设定下降幅更大（0.74→0.53），说明 d0 的高准确率撑起了整体指标
- Part B (从已有CM) 与 Part C (重新跑RF) 数值几乎完全一致，验证了计算正确性

---
