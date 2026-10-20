# ssh merge scored shards

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_merge-scored-shards_20260515T052217_result.json`
- **Structured JSON:** [`04640a26e7efa48c85c7.json`](../../sessions/04/04640a26e7efa48c85c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 指标 | 值 |
|------|-----|
| **总输入 generations** | 21,952 |
| **筛选后样本数** | 2,719 (去重后 **2,718**) |
| **选择率** | 12.4% |
| **Unique docs** | 2,691 |
| **去重删除** | 1 条 |
| **Mean F1 reward** | 0.6157 |
| **Mean CED score** | 0.6683 |
| **F1 范围** | [0.1026, 1.0000] |
| **f1 < 0.1 样本** | 0 (f1 threshold 生效) |
| **截断比例** | 8.88% (1,950 条) |
| **f1 过滤丢弃** | 1,310 generations / 25 docs |
| **缺失 input/output** | 0 / 0 |

输出文件：`/root/autodl-tmp/rsft_filtered/rsft_train.jsonl` (2,718 samples)，汇总报告 `rsft_combined_report.json` 已写入同目录。

---
