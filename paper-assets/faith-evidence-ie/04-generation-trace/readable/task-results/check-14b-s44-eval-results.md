# check 14b s44 eval results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_14b_s44_eval_results_20260525T111824_result.json`
- **Structured JSON:** [`c201e9051b232bfe5570.json`](../../sessions/c2/c201e9051b232bfe5570.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 均在运行中，尚无结果输出。

| 任务 | GPU | 进度 | 启动时间 | 预计剩余 |
|------|-----|------|---------|---------|
| **d158_14b_rsft_s44_eval** (dev with-evi) | cuda:0 | 389/985 (39%) | 17:02 | ~4h |
| **d158_14b_rsft_s44_dev_no_evi** (dev no-evi) | cuda:2 | 92/985 (9%) | 18:53 | ~2.5h |
| **d158_14b_rsft_s44_test_no_evi** (test no-evi) | cuda:3 | 7/32 batches (22%) | 18:53 | ~1.5h |

结果目录目前都是空的（推理完成后才会写出 metrics）。test_no_evi 的 32 个 batch 每个约 3.5 min，预计最先完成（~20:20 左右）。dev no-evi 和 dev with-evi 各约 985 个文档逐个推理，速度较慢。

---
