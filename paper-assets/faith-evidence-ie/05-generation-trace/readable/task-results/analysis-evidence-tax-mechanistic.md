# analysis evidence tax mechanistic

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_evidence_tax_mechanistic_20260518T131147_result.json`
- **Structured JSON:** [`b5972ec7eeff23e36f07.json`](../../sessions/b5/b5972ec7eeff23e36f07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已注册为 artifact `art_20260518_cc2048`，关键发现已写入 memory.md。

核心发现：

1. **Duplication regularization 是主要机制**：1.7B 无 evidence 时生成 60.5% 重复三元组（unique 仅 10,343），evidence 将重复率降至 33.0% 且 unique 数反而更多（11,511）。8B 模型的重复率差距仅 3-8pp。

2. **Truncation asymmetry 是次要机制**：1.7B 无 evidence 截断率 50.9% vs 有 evidence 31.9%；8B 反转，evidence 截断率更高。229 篇文档仅在 no-evidence 条件下截断，evidence F1 高出 20.7pp。

3. **Fair comparison 证明 scaffold 效应**：排除截断后，evidence 仍帮助 1.7B 4.9pp，而 8B Qwen 差异恰好为 0.0pp。这证明 8B 的 tax 完全由截断开销解释，而 1.7B 有真实的推理质量提升。

4. **4B 处于 "capacity valley"**：输出够干净不需要正则化，但容量不足以同时生成 evidence + RE。

建议的 4 张图表方案已列在报告末尾，可后续派 Worker 画图。

---
