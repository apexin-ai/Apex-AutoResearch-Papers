# check c2 n500 progress

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_c2_n500_progress_20260515T014220_result.json`
- **Structured JSON:** [`41068fc82a61cdcdbe20.json`](../../sessions/41/41068fc82a61cdcdbe20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## C2 n=500 进度汇总

**s015 ✅ | s020 ✅ | s025 运行中 | s030 待启动**

### 当前 s025 进度

| 任务 | 进度 | 速率 | s025 完成 ETA | s030 完成 ETA |
|------|------|------|-------------|-------------|
| ds_imp (GPU0) | **325**/500 | 1.9/min | ~11:17 | ~15:37 |
| ds_rand (GPU1) | **371**/500 | 1.9/min | ~10:53 | ~15:13 |
| qw_imp (GPU2) | **483**/500 | 2.5/min | ~09:52 | ~13:12 |
| qw_rand (GPU3) | **465**/500 | 2.5/min | ~09:59 | ~13:19 |

Qwen 两条线 s025 约 10 分钟内完成，随后进入 s030。DeepSeek 较慢，全部跑完预计 **~15:37**。

系统状态正常：磁盘充裕（34%），GPU 76-78% 利用率，4 进程全部存活，无异常。

---
