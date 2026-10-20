# analysis exp001b gstudy

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp001b_gstudy_20260521T083847_result.json`
- **Structured JSON:** [`9e609ede5f19a233a930.json`](../../sessions/9e/9e609ede5f19a233a930.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `results/analysis/exp001b_resampling_gstudy.json`。

## 汇总

| Metric | exp-001 (6 facets) | Sample 1 | Sample 2 | Sample 3 | Mean±Std | CV% |
|--------|-------------------|----------|----------|----------|----------|-----|
| item_id% | 61.08 | 75.88 | 75.38 | 72.18 | 74.48±2.01 | **2.7%** |
| prompt×item% | 4.58 | 4.42 | 4.35 | 5.38 | 4.71±0.58 | 12.2% |
| seed×item% | 4.72 | 5.41 | 4.87 | 5.32 | 5.20±0.29 | **5.5%** |
| temp×item% | 1.83 | 1.43 | 1.44 | 1.66 | 1.51±0.13 | **8.7%** |
| order×item% | 0.59 | 0.49 | 1.18 | 1.17 | 0.95±0.39 | 41.5% |
| residual% | 21.59 | 12.20 | 12.65 | 14.11 | 12.98±1.00 | **7.7%** |
| G_item | 0.6108 | 0.7588 | 0.7538 | 0.7218 | 0.745±0.020 | **2.7%** |
| min_items(G≥0.80) | — | 255 | 262 | 309 | — | — |

## 关键发现

**核心指标稳定（支持 hypothesis）：**
- **item_id%**: CV=2.7%，三组均在 72-76% 范围，远低于 10% 阈值
- **G_item**: CV=2.7%，0.72-0.76 范围稳定
- seed×item、temp×item、residual 的 CV 均 <10%

**两个小组分不稳定（但绝对值很小）：**
- **prompt×item%**: CV=12.2%，略超 10% 阈值，但绝对偏差仅 ~1%
- **ordering×item%**: CV=41.5%，但该组分本身 <1.2%，绝对波动仅 0.7 个百分点

**与 baseline 的差异：** exp001b item_id% 均值 74.5% vs baseline 61.1%，差异 +13.4pp。这是因为 baseline 有 6 facets（含 precision），precision 及 precision:item_id 共占 ~5.4% 方差；移除 precision 后这些方差被重新分配，item_id 比例相应升高。residual 从 21.6% 降至 13.0% 也反映了 precision 相关高阶交互被吸收到 residual 的减少。

**结论：** G-theory 方差分解结构在不同 item 样本间高度稳定。item_id 主导性（>70%）是 robust 的，不依赖特定 item 抽样。

---
