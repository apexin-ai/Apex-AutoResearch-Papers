# analysis qwen c4 entropy

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen_c4_entropy_20260514T090913_result.json`
- **Structured JSON:** [`a235a4e1b7182bcfd0ad.json`](../../sessions/a2/a235a4e1b7182bcfd0ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE / negative。

**总结**：qwen_c4_entropy 实验 30/30 完成。Cross-model 验证结论为 **negative**——random pruning 增加 entropy 的效应跨模型一致，但 importance pruning 的 entropy collapse 在 Qwen 上不稳健（s025 方向反转，s030 接近零），不支持该效应具有强跨模型普适性的 claim。Gini/CV 方向一致但幅度差异显著。

---
