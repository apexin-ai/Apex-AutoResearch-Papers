# diagnose s3 ext exit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_s3_ext_exit_20260519T212252_result.json`
- **Structured JSON:** [`9b858a864268ed28b662.json`](../../sessions/9b/9b858a864268ed28b662.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**exp_001_baseline_s3_extended — SUCCESS**

| 指标 | 值 |
|------|------|
| 最终 step | 520,000 (目标 505K) |
| 最终 eval_return@510K | 947.68 |
| 峰值 eval_return@460K | 967.25 |
| 后半段(250K-510K)均值 | ~930 |

**Eval profile 要点**：
- 0-100K：快速爬升至 ~870
- 100K-200K：稳定在 900-925 区间
- 200K-510K：在 845-967 范围波动，均值约 930，确认收敛到 920+ 水平

Registry 已更新为 DONE/success，cron 监控已删除。完整 eval_profile（52 个 checkpoint）已写入 metrics。

---
