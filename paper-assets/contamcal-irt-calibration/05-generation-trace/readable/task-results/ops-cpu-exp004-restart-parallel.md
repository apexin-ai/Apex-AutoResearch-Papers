# ops cpu exp004 restart parallel

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cpu_exp004_restart_parallel_20260514T211825_result.json`
- **Structured JSON:** [`293d28fa9abd96cc5640.json`](../../sessions/29/293d28fa9abd96cc5640.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**改动摘要:**
- `run_sweep.py` 新增 `--parallel N`（并行 conditions 数）和 `--chains-parallel N`（每 fit 并行 chains 数）参数
- 用 `ProcessPoolExecutor` 实现 condition 级并行，保留 checkpoint/resume
- 已启动: `PID=599560`, `--parallel 2 --chains-parallel 2`
- 53/120 runs 已完成自动跳过，正在并行跑 auc0.8_n100 (剩4) 和 auc0.9_n20 (剩10)

**限制**: 本机仅 2 核 7.6GB RAM，`--parallel 2` 配合 `--chains-parallel 2` 已是合理上限。实际加速约 1.3-1.5x（非 2x，因 CPU 竞争）。如需更快需迁移到多核机器。

---
