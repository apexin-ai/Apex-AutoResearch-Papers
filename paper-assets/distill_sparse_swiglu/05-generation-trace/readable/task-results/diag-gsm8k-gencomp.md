# diag gsm8k gencomp

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gsm8k_gencomp_20260516T003501_result.json`
- **Structured JSON:** [`01dd1046de58502dbcd5.json`](../../sessions/01/01dd1046de58502dbcd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

KL sparse 50% 模型在 GSM8K 上的退化是**推理能力根本性丧失**，不是格式问题：

| 维度 | Dense | Sparse 50% |
|------|-------|------------|
| 推理连贯性 | 多步推理，逻辑清晰 | 1-3 句后进入无限重复循环 |
| 正确答案 | 多数正确 | 0/10 |
| 重复退化 | 无 | 10/10 全部出现 |
| 拼写质量 | 正常 | 退化（crabs→crbs, skein→skeen）|

**典型退化模式**：sparse 模型能生成与问题相关的开头（如 "First, we need to know..."），但随即进入同一句话的无限重复（如 "We can then use the formula to find the total number of crbs." 重复 15+ 次）。Sample 7 中甚至正确算出 9×2=18，但无法继续推理加 3。

Registry 已更新（notes + conclusion=negative），artifact 已注册。

---
