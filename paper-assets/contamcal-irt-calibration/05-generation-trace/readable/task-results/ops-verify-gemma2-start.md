# ops verify gemma2 start

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-gemma2-start_20260518T181120_result.json`
- **Structured JSON:** [`f06e0c16d958c5c5a4a1.json`](../../sessions/f0/f06e0c16d958c5c5a4a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**启动失败。**

汇总：

| 检查项 | 结果 |
|---|---|
| tmux session `exp_001_sft_gemma2_9b_d000_s42` | **不存在**（仅有 `exp_001_sft_7b_d050_s123` 和 `exp_001_sft_7b_d100_s123`） |
| Gemma-2 相关进程 | **无**（pgrep 无匹配） |
| cuda:1 | **空闲**（0MiB, 0% util） |
| 日志 | **`ABORT: active process on target dir`**，退出码 1 |

**失败原因**：启动脚本检测到目标 output 目录已有活跃进程，触发了防冲突保护，自动中止。需要检查是哪个进程占用了该 output dir（可能是之前残留的进程），清理后重新提交。

---
