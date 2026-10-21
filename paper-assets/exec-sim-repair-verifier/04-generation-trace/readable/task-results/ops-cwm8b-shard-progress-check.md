# ops cwm8b shard progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm8b-shard-progress-check_20260516T042956_result.json`
- **Structured JSON:** [`d02c11c7303e6c7e7ac6.json`](../../sessions/d0/d02c11c7303e6c7e7ac6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| Shard | Completed | % | PID | ETA (CST) |
|-------|-----------|---|-----|-----------|
| **v3** | 7208/9784 | 73.7% | alive | ~18:20 |
| **shard3** | 952/1480 | 64.3% | alive | ~13:32 |
| **shard2** | 1592/2104 | 75.7% | alive | ~13:29 |
| **shard4** | 688/684 | 100% | done | ✅ |

关键发现：
- **v3 跑的是全量测试集**（无 `--start_idx`/`--end_idx`），输出在 `cwm_8b_ckpt400_test/`，用 cuda:0。已到 index 7207，远超原计划的 6200。
- **shard2/shard3 约 1 小时内完成**。完成后 idx 0-9783 全覆盖可用——v3 前 6200 行 + shard3 (6200-7680) + shard2 (7680-9784) 拼接即可，无需等 v3 跑完全量。
- 报告已写到 `artifacts/cwm8b_shard_progress.md`。

---
