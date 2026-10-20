# ops c2 qw cron check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c2_qw_cron_check_20260514T191909_result.json`
- **Structured JSON:** [`d45b0d38fbfd3a070604.json`](../../sessions/d4/d45b0d38fbfd3a070604.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Cron 误判，实验正常运行。**

## 状态汇总

**Qwen n500 进度：**

| 条件 | 状态 |
|------|------|
| imp_s015 | **完成** (500/500, profiling_results.json 已生成) |
| rand_s015 | **完成** (500/500, profiling_results.json 已生成) |
| imp_s020 | **运行中** (40/500, GPU2, PID 159269) |
| rand_s020 | **运行中** (20/500, GPU3, PID 159794) |
| s025/s030 | 未开始 |

**DeepSeek n500 同时在跑：**
- ds_imp_s020: GPU0, PID 156554
- ds_rand_s020: GPU1, PID 154305

**GPU 利用率：** 4 卡全满（77-96%，各用 ~24GB）。

s015 已完成并自动切到 s020，脚本正按预期顺序执行。无需干预。

---
