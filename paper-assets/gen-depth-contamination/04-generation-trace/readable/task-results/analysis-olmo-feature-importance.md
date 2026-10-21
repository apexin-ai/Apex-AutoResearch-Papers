# analysis olmo feature importance

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_olmo_feature_importance_20260521T152802_result.json`
- **Structured JSON:** [`9f06711db2dc8828176e.json`](../../sessions/9f/9f06711db2dc8828176e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**OLMo-1B C4 Rerun 确认 K\*=1**：
- 0v1 AUC=0.985，由 Δ¹ Surprisal σ 主导（ΔAUC=0.160）
- 1v2 AUC=0.508，所有 15 个 feature 的 importance 都在噪声范围内（最高仅 0.007±0.004），6 个为负值
- 1v2 total positive importance = 0.029，是 K\*=2 模型的 1/4 到 1/7

**关键发现**：
1. K\*=2 模型（LLaMA/Pythia/Qwen/Gemma）在 1v2 上依赖 **Surprisal σ**（0.056-0.065）和 **Freq. Entropy**（0.017-0.056）。OLMo 在这两个 feature 上的 1v2 importance 本质为零。
2. **Gemma-2-2B 不是 K\*=1**：其 1v2 AUC=0.601，feature importance pattern 与 K\*=2 模型一致，应重新归类为 borderline K\*=2。
3. OLMo 是测试模型中**唯一真正的 K\*=1**，生成质量在 depth 1 即达到 floor，所有统计 fingerprint 一步到位不再变化。

**输出文件**：
- 服务器：`results/olmo_feature_importance/` 下 importance_results.json、gemma_importance_results.json、olmo_rerun_feature_importance.pdf、cross_model_feature_comparison.pdf
- 本地：`artifacts/olmo_feature_importance_analysis.md`（完整分析报告）

---
