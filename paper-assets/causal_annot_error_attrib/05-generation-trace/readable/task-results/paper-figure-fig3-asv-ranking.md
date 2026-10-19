# paper figure fig3 asv ranking

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig3_asv_ranking_20260520T154842_result.json`
- **Structured JSON:** [`9420950b0227c79ded58.json`](../../sessions/94/9420950b0227c79ded58.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已生成并注册 (`art_20260520_8051a6`)。

**输出文件**:
- PDF: `figures/paper/fig3_asv_ranking.pdf` (45K, 矢量)
- PNG: `figures/paper/fig3_asv_ranking.png` (253K, 300 DPI)
- 脚本: `figures/paper/gen_fig3.py`

**设计要点**:
- 三面板 forest plot：Magnitude ASV（范围条）| Significance Power（棒棒糖图）| 右侧数值列（含 sign-flip 标记）
- 7 个拓扑按综合脆弱性排序，Exposure 斜体标注为仅 sign-flip 拓扑
- 浅橙色 fragile zone 背景带（magnitude < 0.3, power < 50%）
- M-bias 用绿色箭头 + ∞ 标记免疫状态
- 排序不一致一目了然：Front-door 在 magnitude 最脆弱但 significance power 100%；Collider 反之

---
