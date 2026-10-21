# analysis advbench layer bias results

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_advbench_layer_bias_results_20260522T095045_result.json`
- **Structured JSON:** [`6006aa71c6d2f3376d44.json`](../../sessions/60/6006aa71c6d2f3376d44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

本地脚本已同步修复。

**状态总结：**

实验 `advbench_layer_bias_r1_8b` 第一次运行失败，根因有两个：

1. **`apply_chat_template` 返回类型变更** — transformers 5.9.0 返回 `BatchEncoding` 而非 `Tensor`，导致 `AttributeError`（空错误消息，所有 520 样本立即失败）
2. **tokenizer decode 损坏** — transformers 5.9.0 + tokenizers 0.22.2 组合导致 byte-level BPE 字符未被还原（`Ġ`→空格, `Ċ`→换行全部丢失）

**已修复：**
- 修改 `generate_trace` 兼容 `BatchEncoding` 和 `Tensor` 两种返回类型
- 降级 transformers 到 4.46.3（tokenizers 0.20.3），tokenizer 恢复正常

**实验已重新启动：** PID 51252，第一条 trace 成功（20 steps, 18.7s），ETA ~162 分钟。需要约 2.7 小时后再取回结果。

---
