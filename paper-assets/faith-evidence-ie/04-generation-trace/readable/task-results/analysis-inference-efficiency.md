# analysis inference efficiency

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_inference-efficiency_20260523T224854_result.json`
- **Structured JSON:** [`25c1a9562244f2d1b488.json`](../../sessions/25/25c1a9562244f2d1b488.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/efficiency_comparison.md` 并注册。

核心发现：

1. **Evidence tax 与模型规模反相关**：1.7B no-evidence 反而慢 13.6%（生成 1.75× 更多 predictions），4B 增加 16.8%，8B 基本持平，14B 增加 16–24%。小模型缺少 evidence 结构约束后输出更冗长。

2. **推理时间亚线性缩放**：1.7B→8B (4.7× 参数) 仅增加 1.63× 推理时间 (batch=4)。

3. **RSFT 比 SFT 慢 15–47%**（with-evidence），因 RSFT 生成更结构化的输出。

4. **batch_size 影响显著**：batch=16 比 batch=1 快 4–6×，不同 eval 间的 batch_size 差异是主要混淆因素，报告中已按 matched-setting 分组标注。

---
