# analysis 72b vs 7b item correlation

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_72b_vs_7b_item_correlation_20260522T203114_result.json`
- **Structured JSON:** [`8153c4ba1c98ddf34935.json`](../../sessions/81/8153c4ba1c98ddf34935.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总：**

| Pair | Pearson *r* | Spearman *ρ* | n |
|------|------------|-------------|---|
| 7B vs 72B | 0.428 (p=2.58e-10) | 0.571 (p=1.06e-18) | 200 |
| 3B vs 72B | 0.450 (p=2.35e-11) | 0.509 (p=1.49e-14) | 200 |

Item difficulty ordering 在 model scale 之间呈中等正相关（Spearman ρ ≈ 0.51–0.57），高度显著。散点图显示明显的 ceiling effect——72B 在大量 item 上达到 100% accuracy，压缩了分布范围，这解释了 Pearson r 偏低（受限范围衰减）。Spearman rank correlation 更高，说明 difficulty ranking 比 raw accuracy 更稳定。

**输出文件：**
- JSON: `artifacts/exp004/data/scale_item_difficulty_correlation.json`
- PDF/PNG: `artifacts/figures/scale_item_difficulty_scatter.{pdf,png}`

---
