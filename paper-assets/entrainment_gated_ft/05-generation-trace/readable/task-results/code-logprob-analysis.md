# code logprob analysis

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_logprob_analysis_20260518T205632_result.json`
- **Structured JSON:** [`9bcb3dfff167ece8396e.json`](../../sessions/9b/9bcb3dfff167ece8396e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是核心发现：

## 结果摘要

### 整体准确率
| 模型 | Acc |
|------|-----|
| GDN-pure | 54.30% |
| GDN-h12-1 | 53.37% |
| HGRN2-pure | 48.42% |
| HGRN2-h3-1 | 51.39% |

### Attention 效果（核心发现）

**GDN (pure → h12-1, 12层attention)**: attention 整体轻微有害
- Helped: 464 (9.0%), Hurt: 512 (9.9%), **净效果: -48 样本**
- 被帮助的样本 logprob 平均提升 +1.38; 被伤害的样本平均下降 -1.45

**HGRN2 (pure → h3-1, 3层attention)**: attention 明显有益
- Helped: 548 (10.6%), Hurt: 395 (7.7%), **净效果: +153 样本**
- 被帮助的样本 logprob 平均提升 +1.22; 被伤害的样本平均下降 -0.93

### 跨模型对比
- Attention 帮助/伤害的样本在两个模型间**重叠很低** (Jaccard: helped=0.118, hurt=0.089)
- 两模型的 logprob delta 相关性较弱, 说明 attention 对不同架构的影响路径不同
- GDN attention 伤害的 512 样本中, 仅 74 个 HGRN2 也被伤害

### 长度分析
- 中等长度(30-50词): GDN attention 有害(-29), HGRN2 有益(+31)
- 长文本(50-100词): GDN 有害(-21), HGRN2 明显有益(+123)
- 超长文本(100+): 样本太少(34个), 趋势不稳定

### 数据缺口
**GDN hybrid-3-1 (`_results.json`) 缺少 per-example 数据**。当前用 h12-1 替代，但 12层 vs 3层 attention 不可直接对比。如需严格对比，需用 `--log_samples` 重跑 GDN h3-1 评测 (~3min)。

### 输出文件
- `/root/entrainment_gated_ft/analysis/lambada_per_example.csv` — 全量逐样本数据
- `/root/entrainment_gated_ft/analysis/lambada_attention_analysis.png` — 4面板分析图
- `/root/entrainment_gated_ft/analysis/lambada_crossmodel_scatter.png` — 跨模型 logprob scatter
- `/root/entrainment_gated_ft/analysis/logprob_analysis.py` — 分析脚本
- `/root/entrainment_gated_ft/analysis/logprob_plots.py` — 绘图脚本

---
