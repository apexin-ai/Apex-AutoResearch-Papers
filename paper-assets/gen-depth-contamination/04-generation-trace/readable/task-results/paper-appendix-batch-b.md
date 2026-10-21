# paper appendix batch b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix-batch-b_20260514T071112_result.json`
- **Structured JSON:** [`03c3de901d20e6515df2.json`](../../sessions/03/03c3de901d20e6515df2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。追加了 `\section{Supplementary Details}` 包含 5 个表格（Tables S4--S8）：

- **S4** — 数据集统计（每 depth 5000 samples，depth-0 平均 147.8 tokens，depth 1-5 约 207 tokens）
- **S5** — 15 维特征完整描述，按 Surprisal (9) / Lexical diversity (3) / Frequency tail (3) 分组，含公式和值域
- **S6** — LightGBM 超参数（n_estimators=200, lr=0.05, max_depth=6, num_leaves=31, 5-fold GroupKFold）
- **S7** — Neural probe 架构（1536→512→256→6 MLP, Adam lr=1e-3, Dropout 0.1, patience=5）
- **S8** — 4 模型 × 5 depth pairs 的 bootstrap CI 详细数据，标注了 OLMo 两个不显著的 p 值

所有数值均来自服务器代码和 registry 实际数据。

---
