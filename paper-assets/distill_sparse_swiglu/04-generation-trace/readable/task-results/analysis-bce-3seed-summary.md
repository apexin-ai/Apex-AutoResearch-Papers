# analysis bce 3seed summary

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bce_3seed_summary_20260515T140445_result.json`
- **Structured JSON:** [`1460810be7edbefc59dc.json`](../../sessions/14/1460810be7edbefc59dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析文件已生成并注册 (`art_20260515_adad23`)。

核心结论：
- **BCE 训练高度稳定**：loss CV=0.08%，training sparsity 三个 seed 完全相同 (0.551)，model-level sparsity 均为 0.498
- **评估 PPL**：dense 28.16±0.21，sparse 43.86±1.18，增幅 55.7%±3.9%
- **逐层稀疏性**：32 层 max std=0.003，浅层 ~46%、深层 ~58-66%，与 TEAL 一致
- **s456 PPL 增幅偏低 (51.2% vs ~58%)**：sparse PPL 较低 (42.54 vs ~44.5)，来自 predictor 权重的随机差异，非系统性偏差
- **KL 对比**：稀疏性坍塌到 0%，sparse PPL=455.93，确认 BCE 是当前唯一可行路径

两个 LaTeX 表格可直接粘贴到论文中。

---
