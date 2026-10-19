# data ssh fetch probe json

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_ssh_fetch_probe_json_20260522T132437_result.json`
- **Structured JSON:** [`8b3bf5b9e29a25787dd8.json`](../../sessions/8b/8b3bf5b9e29a25787dd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个文件已保存到本地：

- `data/llama31_probe_results.json` — 62KB, Llama-3.1, 32层, bootstrap n=100, 含 EN→EN 等方向的逐层 balanced_accuracy/f1
- `data/qwen3_probe_results.json` — 62KB, Qwen-3, 36层, bootstrap n=100, 同结构

JSON 格式有效，包含 `mode`, `n_bootstrap`, `num_layers`, `directions` 等字段，每个方向有 `balanced_accuracy_mean/std`, `f1_mean/std`, `peak_layers` 和逐层数据。

---
