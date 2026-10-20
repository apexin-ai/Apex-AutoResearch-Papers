# ops c2 progress check 20260514

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c2_progress_check_20260514_20260514T214544_result.json`
- **Structured JSON:** [`1c76d0dcd8ff6b47d6d7.json`](../../sessions/1c/1c76d0dcd8ff6b47d6d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

快照已保存。总结：

**已完成：** s015 全部 4 个 condition × 2 模型 = 8 组，各 500/500 ✓

**正在运行 (s020)：**

| GPU | 实验 | 进度 | 速率 | s020 完成 ETA |
|-----|------|------|------|-------------|
| 0 | ds_imp | 375/500 (75%) | 1.90/min | ~06:54 UTC |
| 1 | ds_rand | 423/500 (85%) | 1.90/min | ~06:28 UTC |
| 2 | qw_imp | 419/500 (84%) | 2.54/min | ~06:20 UTC |
| 3 | qw_rand | 397/500 (79%) | 2.54/min | ~06:28 UTC |

**排队中：** s025、s030 各 8 组，s020 完成后自动接续

**全部完成 ETA：** ~15:40 UTC (23:40 CST)，瓶颈在 GPU0 (ds_imp，DeepSeek 比 Qwen 慢约 33%)

---
