# analysis vota data consistency check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_vota_data_consistency_check_20260519T090848_result.json`
- **Structured JSON:** [`9fb561510c90bee0d191.json`](../../sessions/9f/9fb561510c90bee0d191.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### Q1: N5 实验实际使用了多少训练样本？

**Train: 4720, Eval: 1190** — seed123 和 seed456 日志都明确打印了这个数字。

### Q2: N5 使用的训练数据与 seed42_v5 是否相同？

**相同。** 证据：

| 检查项 | 结果 |
|--------|------|
| `train_sft.py` 默认 `--data_dir` | `/root/autodl-tmp/trace-verdict-study-data/` |
| seed123/456 日志中 `data_dir` 覆盖 | **无** — grep 未找到任何 `--data_dir` 参数覆盖 |
| `/root/trace-verdict-study/data/` 中 vota 数据文件 | **不存在** — 该目录只有 `.py` 脚本，无 `.jsonl` |
| 三个 seed 的 Train/Eval 行数 | 全部 `Train: 4720, Eval: 1190` |
| 数据文件 md5 | `vota_train.jsonl`: `873d58ae...`, `vota_test.jsonl`: `54dd7e91...` |

三个 seed 都走默认 `--data_dir`，读的是同一份 `/root/autodl-tmp/trace-verdict-study-data/vota_train.jsonl`（4720 行）和 `vota_test.jsonl`（1190 行）。不存在"新路径"的 vota 数据文件，所以不可能读到不同数据。

### Q3: data_count=1190 是什么？

**1190 是 eval/test set 大小**（`vota_test.jsonl` 的行数），不是训练集大小。训练集是 4720 样本。

**结论：3-seed 对比有效，数据完全一致。**

---
