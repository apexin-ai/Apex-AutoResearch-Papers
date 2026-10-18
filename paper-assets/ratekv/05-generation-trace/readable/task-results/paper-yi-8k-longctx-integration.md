# paper yi 8k longctx integration

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_yi_8k_longctx_integration_20260516T064812_result.json`
- **Structured JSON:** [`ba3ecb40e5e1b7f2f794.json`](../../sessions/ba/ba3ecb40e5e1b7f2f794.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改内容：

- 加入 Yi-1.5-9B 8K 数据（uniform 1.05×, MCKP 1.06×）
- 将 non-Spread 模型的总结改为 "no benefit or slight degradation"（替代之前对两个模型的 "negligible difference" / "indistinguishable"）
- 修复原文 "All three non-spread models (Llama spike, Mistral flat)" 只列了两个的问题，现在三个模型（Llama/Mistral/Yi）均明确列出
- 最后一句加入 Yi
- 数字与表格一致，无 "≈ uniform" 残留

---
