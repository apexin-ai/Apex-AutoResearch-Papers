# analysis steering 107

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_steering_107_20260522T082944_result.json`
- **Structured JSON:** [`ef4102bc1271dac27647.json`](../../sessions/ef/ef4102bc1271dac27647.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**steering_107: failed** — 脚本在第一个 steering 条件崩溃，无任何结果数据。

**崩溃根因**: `SteeringHook.__call__`（line 119）用 `h[:, -1, :]` 索引 hidden states，假设 3D tensor。但 `model.generate()` 使用 KV cache 时，decoder layer 输出的 hidden states 在某些步骤为 2D，触发 `IndexError: too many indices for tensor of dimension 2`。

**可用信息**:
- Baseline 完成：contextual=41, parametric=32, both=35, neither=28（136 samples）
- 探针 layer 28 accuracy: 77.57%
- 正交性验证通过

**修复**: hook 需加 `if h.dim() == 2` 分支处理 KV cache 场景。分析已写入 `artifacts/steering_107_analysis.md`。

---
