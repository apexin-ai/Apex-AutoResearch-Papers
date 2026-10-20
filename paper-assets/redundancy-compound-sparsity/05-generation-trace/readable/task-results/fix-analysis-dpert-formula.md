# fix analysis dpert formula

**When Does KV Redundancy Predict MLP Sparsity? Architecture Dependence of Cross-Axis Signals in Reasoning Inference** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_analysis-dpert-formula_20260512T030856_result.json`
- **Structured JSON:** [`3697a0b866d045542fc1.json`](../../sessions/36/3697a0b866d045542fc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改内容：

- `extract_per_layer_dpert` 函数：`(n_mean - r_mean) / r_mean * 100` → `(n_mean - r_mean) / (n_mean + 1e-10) * 100`
- 分母从 redundant mean 改为 novel mean，同时用 `1e-10` 防除零
- 所有图表（6 个 PDF + 6 个 PNG）和 `llama_vs_deepseek_summary.md` 已重新生成

---
