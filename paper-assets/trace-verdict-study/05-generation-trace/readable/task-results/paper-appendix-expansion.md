# paper appendix expansion

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix-expansion_20260515T194033_result.json`
- **Structured JSON:** [`12afc5da961aead7e686.json`](../../sessions/12/12afc5da961aead7e686.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。appendix.tex 新增 4 个 section：

- **Section B (Training Details)**: 超参表格 + 各 condition 训练时长表格
- **Section C (VOTA Trace Examples)**: 1 个 fail（ZeroDivisionError）+ 1 个 pass（add）示例，用 `verbatim` 环境
- **Section D (Full Experimental Results)**: Qwen 跨 8 条件 × 3 种子完整表格 + DeepSeek 4 条件表格（含 label truncation bug 标注）
- **Section E (Irreducible Sample Analysis)**: 2 个 irreducible samples (ID 901, 905) 的 check\_dict\_case 分析，含 99.83% accuracy ceiling 推导

原有 Section A (Per-Class Performance Breakdown) 保持不变。

---
