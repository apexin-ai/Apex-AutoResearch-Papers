# ops rho02 adaptive diagnose

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rho02-adaptive-diagnose_20260516T225737_result.json`
- **Structured JSON:** [`a9941e3ad085b52e71c0.json`](../../sessions/a9/a9941e3ad085b52e71c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断与修复总结

| 项目 | 结果 |
|------|------|
| **进程状态** | PID 364149 已死 |
| **死因** | `CUDA_VISIBLE_DEVICES=-1` 禁用了所有 GPU，导致 `bf16` 训练立即报错 `ValueError: Your setup doesn't support bf16/gpu` |
| **训练进度** | 零（无 step_metrics，模型未开始训练） |
| **磁盘** | 充足（数据盘 40G 可用） |

**修复内容**：
1. 移除 `export CUDA_VISIBLE_DEVICES=-1`，改为注释（由 `submit_training_job` 在启动时设置）
2. `set -e` → `set -eo pipefail`，防止管道吞错误码

**修复后脚本路径**：`/root/provenance_weight_training/scripts/run_rho02_adaptive_tau09_seed42.sh`

**验证**：`bash -n` 语法检查通过，`WANDB_MODE=disabled`，`output_dir` 在数据盘 `/root/autodl-tmp/`。

可以用 `submit_training_job` 重新提交到 `cuda:1`。

---
