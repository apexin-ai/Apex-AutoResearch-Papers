# fix kill restart kl30 multiseed

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill_restart_kl30_multiseed_20260517T102635_result.json`
- **Structured JSON:** [`6ad6134b13148ef7ec3e.json`](../../sessions/6a/6ad6134b13148ef7ec3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果汇总：**
- 错误进程（PID 22730/22732, lambda_max=1000）已 kill
- 错误 checkpoint `kl_30pct_s123` 已删除
- 新训练已启动（PID 23613→子进程 23615），配置 `lambda_max=5000`，日志确认 `cap=5000.0`
- cuda:0（PID 22260, 50% multiseed）未受影响
- 日志路径：`/root/distill_sparse_swiglu/logs/multiseed_kl30_fixed.log`

---
