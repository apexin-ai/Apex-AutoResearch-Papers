# paper figure fig1 overview

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig1_overview_20260519T192811_result.json`
- **Structured JSON:** [`3796ba2ae7f3b800b0cb.json`](../../sessions/37/3796ba2ae7f3b800b0cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 1 生成完成。

**输出文件**:
- PDF (vector): `figures/paper/fig1_overview.pdf` (48K)
- PNG (300 DPI): `figures/paper/fig1_overview.png` (189K, 1599×591px)

**三段式布局**:
- **左 — Observation**: 多轮对话栈 + GAR 衰减曲线 (↓70.8%) + 残差流持久性 (AUC=0.98)
- **中 — ThreadGate**: 残差连接上的 sigmoid gate 架构图 + 公式 $x_{l+1} = x_l + g_l \cdot f_l(x_l)$
- **右 — Result**: 训练成功 (GAR 0.48) vs 推理失败 (GAR 0.016, 30× gap) + 根因分析 → distribution shift

**注意**: 这是 full-width 图 (170mm)。最小字号 4.5pt 用于次要标注，主要内容 5.5pt+。若需缩到 column width 需要进一步精简内容或增大字号。生成脚本保存在 `figures/fig1_overview.py` 方便迭代。

---
