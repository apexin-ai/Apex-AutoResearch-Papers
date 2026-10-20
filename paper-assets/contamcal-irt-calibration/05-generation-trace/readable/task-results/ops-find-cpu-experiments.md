# ops find cpu experiments

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_find_cpu_experiments_20260514T205253_result.json`
- **Structured JSON:** [`7cdd4c73f1f398ad7ccd.json`](../../sessions/7c/7cdd4c73f1f398ad7ccd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### exp-004 (sim_sweep)
- **脚本位置**: `artifacts/simulation_sweep/run_sweep.py`（用 `artifacts/mvp_simulation/.venv` 的 Python）
- **日志**: `/tmp/exp004_sweep_restart.log`
- **PID 559605**: **存活**，已运行 2h45m58s（是 bash wrapper，实际 python 子进程在 nohup 下）
- **进度**: 48/120 runs 完成

### exp-005 (noise_prop)
- **脚本位置**: `artifacts/exp005_noise_propagation/run_noise_propagation_v3.py`
- **日志**: `artifacts/exp005_noise_propagation/exp005_v3.log`
- **输出目录**: `artifacts/exp005_noise_propagation/output_v3/`
- **PID 559666**: **存活**，已运行 2h45m56s（bash wrapper）
- **进度**: 14/25 fits 完成

**两个实验都在本地机器运行，不在远程服务器 cqa1-21977 上。** Bash wrapper 进程存活，实际 Python 子进程通过 nohup 在后台执行。

---
