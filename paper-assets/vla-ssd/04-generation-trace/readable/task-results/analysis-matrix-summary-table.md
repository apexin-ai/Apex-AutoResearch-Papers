# analysis matrix summary table

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_matrix_summary_table_20260522T000858_result.json`
- **Structured JSON:** [`2934e651d8adf7745ee3.json`](../../sessions/29/2934e651d8adf7745ee3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

表格已写入 `artifacts/matrix_summary_table.md` 并注册。

关键发现：

**缺失数据**：OpenVLA Goal 和 Spatial 不存在标准化 pipeline 目录（`libero_goal_trained/` 等均不存在，只有旧格式 `trained_libero_goal/goal_classification/`）。NORA Spatial untrained 缺 CF 文件。

**跨架构一致 pattern**：
- **R² 坍缩是训练引起的**：trained Δ 显著大于 untrained（所有架构一致）。NORA 最极端（Goal Δ=0.691，exit R²=-0.004），TracVLA 中等（Δ=0.138–0.294），OpenVLA Long 几乎无坍缩（Δ=0.004）
- **CF 敏感性**：trained 模型中 "empty" 在 5/6 setting 中排第一；untrained 中 "empty" 全部排第一，且 cosine distance 量级远小于 trained 的 Cohen's d
- **L1 注意力**：TracVLA untrained 全部 32/32 instruction-dominant（Phi-3 预训练已带有指令偏置），fine-tuning 反而轻微降低

**异常点**：NORA Goal trained CF exit 层 cosine distance 全部饱和为 1.0；OpenVLA Long untrained 使用了 Cohen's d 而非 cosine distance 方法。

---
