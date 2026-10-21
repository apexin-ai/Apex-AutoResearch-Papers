# analysis full trace data consistency

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_full_trace_data_consistency_20260519T090924_result.json`
- **Structured JSON:** [`fad7d52b1338539faf43.json`](../../sessions/fa/fad7d52b1338539faf43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完全一致。结论如下：

## 结果

### 1. seed42 (full_trace_label_only_seed42)
- **数据路径**: `/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl`（脚本默认 `--data_dir`，日志未覆盖）
- **样本数**: Train: 4720, Eval: 1190 (total 5910)
- **Accuracy**: 86.22%

### 2. N5 seed123/456
- **seed123 数据路径**: `/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl`（registry spec.data_path 明确记录）
- **seed123 样本数**: Train: 4720, Eval: 1190 (total 5910), Accuracy: 87.06%
- **seed456 数据路径**: `/root/autodl-tmp/trace-verdict-study-data/full_trace_{train,test}.jsonl`（同上）
- **seed456 样本数**: Train: 4720, Eval: 1190 (total 5910), Accuracy: 85.90%

### 3. 一致性判定: **完全一致**

三个 seed 使用相同数据文件（`/root/autodl-tmp/trace-verdict-study-data/full_trace_train.jsonl` 4720行 + `full_trace_test.jsonl` 1190行），相同 condition (`full_trace`)，相同 `--label_only_loss` flag，相同模型 (`Qwen2.5-Coder-7B-Instruct`)，相同 code commit (`e404237`)。唯一差异是 seed 和 output_dir。

数据文件 MD5: train `62a3fa164d20135ff2a609d1cf336139`, test `4a751d6ae89c504234203e02be97629f`。

---
