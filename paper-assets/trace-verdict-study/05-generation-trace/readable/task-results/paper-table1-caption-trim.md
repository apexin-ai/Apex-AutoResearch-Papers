# paper table1 caption trim

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table1_caption_trim_20260519T154054_result.json`
- **Structured JSON:** [`d5cbac30b9d60ee3fe51.json`](../../sessions/d5/d5cbac30b9d60ee3fe51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SSH 连接不可用（Permission denied）。修改已在本地完成，需要你手动同步到服务器或检查 SSH 配置。

**修改总结：**

- **Caption**：从 ~120 词精简到 ~40 词（约 3 行），保留核心信息（模型范围、样本量、multi-seed 说明、Appendix 指引）
- **Table notes**：所有 per-seed 细节（DeepSeek outlier、VOTA/ae_only/loop_only 各 seed 值、Qwen-1.5B 确认）移到表格下方的 `\footnotesize` 注释块
- **label/引用**：`\label{tab:cross_model}` 和 `$^\dag$` 标记均保持不变
- **无信息丢失**：原 caption 中所有数据点都保留在 tablenote 中

---
