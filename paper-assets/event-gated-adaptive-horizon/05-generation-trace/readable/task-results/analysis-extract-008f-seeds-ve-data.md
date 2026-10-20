# analysis extract 008f seeds ve data

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_extract-008f-seeds-ve-data_20260517T040146_result.json`
- **Structured JSON:** [`0af6486ec7760a87c6b3.json`](../../sessions/0a/0af6486ec7760a87c6b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果写入 `artifacts/analysis/negative_cases_ve_data.json`。

**摘要：**

| 实验 | Seed | Steps | Max V/E | 状态 |
|------|------|-------|---------|------|
| exp_008f_s3_no_dt_embed_walker | 3 | 105K | 0.538 | success |
| exp_009c_008f_walker_s2 | 2 | 105K | 0.750 | negative/healthy |
| exp_009h_008f_walker_s0 | 0 | 5K | N/A | failed (无数据) |

**关键观察：**
- 008f_s3: V/E 全程 < 0.54，非常稳定，适合做 negative case
- 009c: V/E 在后期升至 0.75（eval_return 下降但 value_mean 仍涨），但这是正常的 value overestimation 而非 catastrophic divergence
- 009h: 实验在 step 5000 就失败了，metrics.jsonl 只有 5 行初始化记录，无可用数据，已标注 `data_unavailable: true`

---
