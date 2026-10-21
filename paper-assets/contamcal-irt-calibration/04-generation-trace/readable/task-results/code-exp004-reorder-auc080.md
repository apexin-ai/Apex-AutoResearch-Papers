# code exp004 reorder auc080

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp004_reorder_auc080_20260514T042939_result.json`
- **Structured JSON:** [`c4202f37878f6e2ef37e.json`](../../sessions/c4/c4202f37878f6e2ef37e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Stan chains 3-4 已运行约 19 分钟，状态为 R（运行中）。

---

**总结：**

1. **已完成修改**：`run_sweep.py` 的 SUBSET AUC 顺序从 `[0.55, 0.65, 0.80, 0.90]` 改为 `[0.80, 0.90, 0.55, 0.65]`

2. **自动重启监控已部署**（PID 362586）：每 5 秒检查 auc0.55_n100 的 seed 数。当 seed 6 保存后（当前 Stan chains 完成），自动 kill 旧进程并重启 sweep。不会 kill 正在运行的 Stan。

3. **AUC=0.80 现有结果**：仅 1 个 seed（N=50, seed 0），CI95 宽度 16.2pp，是 AUC=0.55 同 N 的 1.86 倍。gamma_sd=0.0408 vs AUC=0.55 的 ~0.016。确实系统性偏宽，但需要更多 seed 确认方差。

4. **预计时间线**：Stan chains 预计再跑 20-70 分钟完成 → 自动重启 → AUC=0.80 的 N=20 fit 较快（~7-11min/seed）→ 首批 AUC=0.80 结果约 1-2 小时内可用。

可以用 `cat /tmp/restart_sweep_monitor.log` 和 `cat /tmp/sweep_restart.log` 监控进度。

---
