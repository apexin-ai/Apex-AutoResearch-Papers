# fix rho02 tau09 cuda env

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_rho02_tau09_cuda_env_20260516T130101_result.json`
- **Structured JSON:** [`5c40bcc524534452e5b7.json`](../../sessions/5c/5c40bcc524534452e5b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器全部 37 个脚本已通过验证。汇总：

### 修复结果

**`run_rho02_adaptive_tau09_seed42.sh`（目标脚本）：**
- westd-47453: `export CUDA_VISIBLE_DEVICES=1` → `export CUDA_VISIBLE_DEVICES=-1`
- westd-41312: `# TODO: set CUDA_VISIBLE_DEVICES=N before running` → `export CUDA_VISIBLE_DEVICES=-1`

**TODO 注释替换为 `export CUDA_VISIBLE_DEVICES=-1`：**
- westd-47453: `run_batch_adaptive_tau_rho06_seed42.sh`, `run_bs8_auto_nmin_seed42.sh`, `run_hybrid_rho04_seed42.sh`（3 个）
- westd-41312: `run_rho02_adaptive_tau09_seed42.sh`, `run_batch_adaptive_tau_rho06_seed42.sh`, `run_bs8_auto_nmin_seed42.sh`（3 个）

**缺失脚本添加 `export CUDA_VISIBLE_DEVICES=-1`：**
- westd-47453: 26 个脚本（插入在 `set -e` 后或 shebang 后）
- westd-41312: 23 个脚本

**7 个无 `set -e` 的旧脚本**（`run_grid_b0_*`, `run_tau_*_nmin2`）单独在 shebang 后插入，两台服务器均已修复。

**最终状态：两台服务器全部 37 个 `run_*.sh` 脚本都有 `export CUDA_VISIBLE_DEVICES` 设置，无 TODO 注释残留。**

---
