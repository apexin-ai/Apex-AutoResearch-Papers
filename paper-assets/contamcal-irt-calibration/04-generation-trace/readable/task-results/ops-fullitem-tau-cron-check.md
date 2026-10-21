# ops fullitem tau cron check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fullitem_tau_cron_check_20260517T154043_result.json`
- **Structured JSON:** [`b8fb01573f1992b1c145.json`](../../sessions/b8/b8fb01573f1992b1c145.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：实验失败（进程被 kill）。**

日志停在 MCMC 采样中途：
- chain 3/4 完成 100%（2000/2000）
- chain 1 仅到 80%（1600/2000）
- chain 2 仅到 75%（1500/2000）

之后日志无更多输出，无 JSON 输出文件，tmux session `vanilla_2pl_full` 已不存在，无相关进程运行。

进程在采样约 1h45m 时被终止（很可能是 SeetaCloud 容器重启导致）。数据规模为 20 models × 14,042 items，4 chains × 2000 iterations。

需要重新提交。

---
