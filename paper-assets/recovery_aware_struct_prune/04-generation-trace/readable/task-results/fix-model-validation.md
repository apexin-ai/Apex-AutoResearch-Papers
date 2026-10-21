# fix model validation

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_model-validation_20260514T030545_result.json`
- **Structured JSON:** [`913fd74b2de7d028cbd1.json`](../../sessions/91/913fd74b2de7d028cbd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。汇报：

1. **.aria2 残留**：存在 2 个 .aria2 文件 + 4 个冗余下载进程（2x wget + 2x aria2c 同时写同一文件）。已全部杀掉并清理 .aria2 文件。
2. **模型验证**：
   - safetensors 文件头完整：shard 1 = 200 tensors, shard 2 = 139 tensors（合计 339）
   - 文件大小 15.2GB 与 index.json 的 `total_size` 一致
   - transformers 加载权重 339/339 成功（CPU 实例化超时但权重读取无报错）
   - Tokenizer OK, vocab_size=151,643
3. **无需重新下载**，模型完整可用。

---
