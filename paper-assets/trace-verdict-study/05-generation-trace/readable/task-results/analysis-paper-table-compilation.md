# analysis paper table compilation

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_table_compilation_20260516T191118_result.json`
- **Structured JSON:** [`3e7832aea12635504943.json`](../../sessions/3e/3e7832aea12635504943.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出写入 `artifacts/table1_data.md` 并注册为 `art_20260516_217dd5`。

内容包括：
- **CSV 原始数据** — 28 行实验记录（4 模型 × 7 条件）
- **聚合表** — mean±std 格式，可直接对照论文
- **LaTeX tabular** — Table 1 主表 + nomarker ablation 表，可直接复制
- **Cross-scale 分析**：
  - no_trace: 67.31%→75.13%→76.50%，scale 递增但收益递减
  - exception_only: Qwen/CodeLlama 全部 99.83%，DeepSeek 99.33%（seed123 有一次训练不稳定=91.09%）
  - VOTA: Qwen/CodeLlama ≥98.57%，DeepSeek 仅 84.45%（family-dependent）

注意事项：`exception_only_nomarker_seed456` 仍在运行，表中标 \* 。

---
