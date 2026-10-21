# ops fig mi heatmap

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fig-mi-heatmap_20260525T144449_result.json`
- **Structured JSON:** [`b4b5ae79fe85ba48e9e5.json`](../../sessions/b4/b4b5ae79fe85ba48e9e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已生成 `fig_mi_heatmap.pdf` 和 `.png`。

视觉检查确认：
- 矩阵对称，对角线用 ×标记（self MI）
- 模型名按 MMLU accuracy 降序排列，标签可读（7pt, 45° 旋转）
- 两个 benchmark pattern 差异明显：MMLU 中 API 前沿模型间形成高 MI 块（Gem-Flash/GPT-5.5/Gem-Pro 三角），开源弱模型（Llama-8B, Q72B）MI 极低；ARC-Challenge 整体 MI 更高，但 Haiku 和 Q72B 显著低于其他模型
- 共享 colorbar，标注 "Mutual Information (bits)"，range 0–0.75
- YlOrRd colormap，300 DPI，白底

---
