# diagnose calibrate crm correction signal

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_calibrate-crm-correction-signal_20260520T052305_result.json`
- **Structured JSON:** [`81804928fffd8de5d9af.json`](../../sessions/81/81804928fffd8de5d9af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**日志完整**：JSON 包含全部 10 episodes（episode 0-9），27626 steps，correlations 和 go/no-go 判定均已计算并写入。

**退出原因：正常完成**。脚本末尾是 `calibrate(args)` → `sys.exit(0)`，正常退出码 0。

**根因：脚本没有任何 W&B/sentinel 代码**。`calibrate_crm_signal.py` 只写 JSON 结果文件后直接 `sys.exit(0)`，从未初始化 wandb、从未写 sentinel 文件。cron 检测 W&B sentinel 必然判定为 failed。

**是否需要修复**：是。如果希望 cron 正确识别此类纯离线分析脚本的完成状态，需要二选一：
1. 在脚本末尾加 sentinel 文件写入（如 `touch logs/.sentinel_crm_calibration_done`）
2. cron 侧增加对 JSON 输出文件存在性的检查作为备选完成信号

---
