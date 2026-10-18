# ops check llama sweep status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_llama_sweep_status_20260515T163523_result.json`
- **Structured JSON:** [`04bb94f9f96dbc6bd097.json`](../../sessions/04/04bb94f9f96dbc6bd097.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**总结**：Llama compounding sweep 已成功完成，不是快速失败——ANALYZING 状态只是 registry 没及时更新。GPU 0 已空闲。关键发现：Llama-3.1-8B 在 budget=0.25 下，k≤8 时 PPL 退化极小（+0.13），k=16 开始可感知（+0.35），k≥64 急剧恶化。

---
