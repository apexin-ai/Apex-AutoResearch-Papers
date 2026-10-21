# diagnosis repeated failures

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_repeated_failures_20260517T214740_result.json`
- **Structured JSON:** [`6790ddbbdd8e3c4057b9.json`](../../sessions/67/6790ddbbdd8e3c4057b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/diagnosis_westd41312_failures.md`。

**核心发现：这些不是真正的训练失败。**

1. **ess_only_seed123_r2, ess_only_seed456_r2, random_reweight_seed456** — 当前正在 westd-41312 上正常运行（55%/63%/25%），但 registry 在启动 4 分钟后就误判为 failed，因为 `WANDB_MODE=disabled` 导致无 heartbeat 且 registry 无 server 字段

2. **原始实验的 SIGTERM** — GPU 调度系统主动杀进程（两个实验在同一秒被杀），不是 OOM/代码 bug。而且 registry 显示 ess_only_seed123/456 已在 westd-47453 上成功完成

3. **grid_b0_3_seed123_r2** — 从未在 westd-41312 上启动（无日志无进程），需要在 GPU 空出后调度

**立即行动**：不要重启任何实验，手动将 registry 状态改回 RUNNING。等 ess_only_seed456_r2 完成后（~1.3h），用空出的 GPU 跑 grid_b0_3_seed123_r2。

---
