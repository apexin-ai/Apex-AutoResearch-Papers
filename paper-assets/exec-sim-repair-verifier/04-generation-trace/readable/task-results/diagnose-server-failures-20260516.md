# diagnose server failures 20260516

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_server-failures-20260516_20260516T002555_result.json`
- **Structured JSON:** [`b01618cd940f0fea9c0e.json`](../../sessions/b0/b01618cd940f0fea9c0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。核心发现：

**CLS ablation** — 误报，实际已成功完成。Accuracy 83.04%，F1 macro 76.80%，结果完整。

**CWM 8B v5 训练** — 进程在 step 6198/6633 被系统杀死，无错误日志。最新 checkpoint 是 6100，剩余 533 steps（约 1.8 小时）。推测根因：训练做 checkpoint-6100 eval 时与同 GPU 上的 ckpt-400 eval 争抢显存触发 OOM。

**CWM ckpt-400 eval** — EXIT_CODE=137 确认 SIGKILL。已完成 5280/9784 样本（54%），部分结果 5280 行完整可用。

4 块 RTX 5090 当前全部空闲，可立即恢复训练。建议先单独跑完 CWM v5 训练（从 ckpt-6100 resume），完成后再跑 eval，避免 GPU 资源冲突。

报告已写入 `artifacts/diag_server_failures_20260516.md`。

---
