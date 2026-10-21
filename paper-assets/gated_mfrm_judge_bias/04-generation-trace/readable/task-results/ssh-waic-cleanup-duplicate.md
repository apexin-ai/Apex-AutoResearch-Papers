# ssh waic cleanup duplicate

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_waic_cleanup_duplicate_20260523T004920_result.json`
- **Structured JSON:** [`63b64b7408432902aac5.json`](../../sessions/63/63b64b7408432902aac5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。汇报：

**清理结果**
- PID 244822 (`compute_waic_loo.py`) — 已 kill
- PID 249604 (`waic_loo_comparison.py`) — 正常运行，GPU 0 独占（669MiB, 69% util）

**当前进度**
- G-MFRM 的 WAIC/LOO 已完成（ELPD_WAIC=-2272.26, Pareto-k 全部 good）
- 正在 fitting 标准 MFRM（无 contamination）：chain 进度 891/8000，~1.18 s/it
- 剩余 ~7109 iterations × 1.18s ≈ **2h 20min**（kill 掉竞争进程后 GPU 独占，实际可能更快）

**ETA**: MFRM fitting + WAIC/LOO 计算，预计 **~2.5-3 小时**完成（约今天 11:00-11:30 服务器时间）。

---
