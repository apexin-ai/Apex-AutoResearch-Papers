# ops diagnose permuted score exit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_permuted_score_exit_20260524T203730_result.json`
- **Structured JSON:** [`642c2f5533dfaf4b3eca.json`](../../sessions/64/642c2f5533dfaf4b3eca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被之前的 hook 自动清理）。

---

**诊断结果: 训练成功完成**

| 项目 | 值 |
|------|-----|
| 状态 | success (6103/6103 steps) |
| train_loss | 8.033 |
| 训练时长 | ~3h 45m (13540s) |
| throughput | 7.21 samples/s, 0.45 steps/s |
| final checkpoint | `.../permuted_score_control_seed42/final` (1.19GB model.safetensors) |
| eval | 未执行（无 eval_results 文件） |

**备注**: `~/runs/` 日志中 step 500 的 `ENOSPC` 崩溃是第一次运行的残留记录（retry_count=2 确认了重跑）。重启后成功跑完全部 6103 steps 并保存了 final model。

Registry 已更新为 `conclusion=success`，metrics 已记录。

---
