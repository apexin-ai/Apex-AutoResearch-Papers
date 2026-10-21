# fix script compliance

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_script-compliance_20260516T150856_result.json`
- **Structured JSON:** [`51c7289389520b4e97e7.json`](../../sessions/51/51c7289389520b4e97e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两台服务器 10 个脚本全部验证通过。汇总：

## 修复结果

| 脚本 | 修改项 | 验证 |
|------|--------|------|
| **run_rho02_adaptive_tau09_seed42.sh** | `WANDB_MODE=offline` → `disabled`; `output_dir` → `/root/autodl-tmp/output/models/rho02_adaptive_tau09_seed42/` | ✅ WANDB_MODE=disabled, 无 wandb 参数, output_dir 指向数据盘 |
| **run_batch_adaptive_tau_rho06_seed42.sh** | 添加 `export WANDB_MODE=disabled`; 删除 `--use_wandb` / `--wandb_project` / `--wandb_run_name`; `output_dir` → `/root/autodl-tmp/output/models/batch_adaptive_tau_rho06_seed42/` | ✅ |
| **run_bs8_auto_nmin_seed42.sh** | inline `WANDB_MODE=disabled` → `export` 形式; 添加 `HF_HOME`; `output_dir` → `/root/autodl-tmp/output/models/bs8_auto_nmin_seed42/` | ✅ |
| **run_batchsize16.sh** | 删除 `--use_wandb` / `--wandb_project` / `--wandb_run_name`; `output_dir` → `/root/autodl-tmp/output/models/batchsize16_nmin8_seed42/` | ✅ |
| **run_grid_b0_2_seed42.sh** | 添加 `export WANDB_MODE=disabled`; 添加 `set -e` / `HF_HOME`; `output_dir` → `/root/autodl-tmp/output/models/grid_b0_2_seed42/`; 添加 `--eval_data_path` + `--eval_steps 500` | ✅ |

两台服务器（westd-47453 / westd-41312）均已同步修复。所有脚本满足 4 项硬约束：WANDB_MODE=disabled、无 wandb 参数、output_dir 在数据盘、grid_b0_2 有 eval 配置。

---
