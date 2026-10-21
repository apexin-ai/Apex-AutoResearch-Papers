# data cross dataset split

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_cross_dataset_split_20260522T035424_result.json`
- **Structured JSON:** [`116427012bc828583f14.json`](../../sessions/11/116427012bc828583f14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**数据分布**（exception_only 和 no_trace 一致）：
- HumanEval: 1,640 samples
- MBPP: 4,270 samples
- unknown: 0

**生成的 8 个文件**（`/root/autodl-tmp/trace-verdict-study-data/cross_dataset/`）：

| 文件 | 行数 |
|------|------|
| `cross_mbpp2he_exception_only_train.jsonl` (MBPP) | 4,270 |
| `cross_mbpp2he_exception_only_test.jsonl` (HumanEval) | 1,640 |
| `cross_he2mbpp_exception_only_train.jsonl` (HumanEval) | 1,640 |
| `cross_he2mbpp_exception_only_test.jsonl` (MBPP) | 4,270 |
| `cross_mbpp2he_no_trace_train.jsonl` (MBPP) | 4,270 |
| `cross_mbpp2he_no_trace_test.jsonl` (HumanEval) | 1,640 |
| `cross_he2mbpp_no_trace_train.jsonl` (HumanEval) | 1,640 |
| `cross_he2mbpp_no_trace_test.jsonl` (MBPP) | 4,270 |

**注意事项**：HumanEval 有 1,640 samples（>100 阈值），数据量足够。HE→MBPP 方向训练集较小（1,640），训练时可能需要关注过拟合。脚本在 `/root/trace-verdict-study/data/split_cross_dataset.py`。

---
