# code appendix curves stats heatmaps

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_appendix_curves_stats_heatmaps_20260524T152748_result.json`
- **Structured JSON:** [`37eac32b127f27bdb2d5.json`](../../sessions/37/37eac32b127f27bdb2d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项附录扩充素材全部完成：

| 项目 | 输出路径 | 状态 |
|------|---------|------|
| **Item 8** — 6-panel 训练曲线 | `figures/paper/fig_training_curves_6panel.pdf/.png` | 5 条件 + 图例面板，含 epoch 边界标记 |
| **Item 9** — 统计检验汇总表 | `artifacts/appendix_expansion/tab_statistical_tests.tex` | 12 行 Wilcoxon (β=0/3/5) + McNemar 指令保持检验 |
| **Item 10** — 4-panel steering per-turn GAR | `figures/paper/fig_steering_perturn_4panel.pdf/.png` | β=0/3/5/10 柱状图，含 PPL 标注和 β=0 参考线 |

关键发现：β=0 时 TG 显著优于 Base/LoRA/PCGrad（r=0.45–0.87）；β≥5 时各条件差异不再显著（p>.08）；β=10 虽 GAR≈0.98 但 PPL=505 崩溃。指令保持 McNemar 检验 p=.077（边际），但 point-biserial r=.200, p=.007（显著）。

---
