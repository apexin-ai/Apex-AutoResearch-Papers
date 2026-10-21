# gpu gemma zh activations 102

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_gemma-zh-activations-102_20260522T102224_result.json`
- **Structured JSON:** [`4a81a834bc2073f616ec.json`](../../sessions/4a/4a81a834bc2073f616ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ZH activations 收集完成。

**结果汇总**：
- 输出文件：`data/gemma2/zh_activations.pt`（~456 MB，时间戳 18:27）
- shape：`[1590, 42, 3584]` bfloat16（1590 samples × 42 layers × 3584 hidden dim）
- labels：1590 个，split_sizes = train 1274 + test 316
- Registry 已更新（gemma_full_pipeline_102）

下一步可以进行 ZH probe 训练和 cross-lingual bootstrap 分析。

---
