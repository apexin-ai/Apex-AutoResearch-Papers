# diag eval obs only object norm01 seed71

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-obs-only-object-norm01-seed71_20260521T031530_result.json`
- **Structured JSON:** [`d3b691f64cfcee8269f5.json`](../../sessions/d3/d3b691f64cfcee8269f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：实验正常完成，Cron 回调是误报。**

验证结果：
- **日志**：完整跑完 10 个 task × 10 rollouts = 100 rollouts，末尾输出 `Overall success rate (crm_obs_only): 16.0% (16/100)` 和 `Results saved to logs/norm01_seed71.json`
- **JSON 输出**：`/root/acr-vla-conformal-refinement/logs/norm01_seed71.json` 存在（1490 bytes），内容完整，10 个 task 各 10 rollouts，`overall_success_rate: 0.16`，与日志一致
- **进程**：PID 922504 已退出（正常结束）

Cron 报 "exited without valid W&B metrics" 是因为这个 eval 脚本不向 W&B 上报指标，只写本地 JSON——Cron 的 W&B 检测逻辑不适用于纯 eval 任务。

---
