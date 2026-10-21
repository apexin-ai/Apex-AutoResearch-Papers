# code prep rho02 adaptive tau09

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_rho02_adaptive_tau09_20260516T125401_result.json`
- **Structured JSON:** [`023a67c73efb652cbd45.json`](../../sessions/02/023a67c73efb652cbd45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪。总结：

- **脚本**：`/root/provenance_weight_training/scripts/run_rho02_adaptive_tau09_seed42.sh` (chmod +x)
- **数据**：`data/scored_data_rho02.jsonl` (626MB，确认存在)
- **修复**：相比原版移除了 `--use_wandb`/`--wandb_project`/`--wandb_run_name`，添加了 `export CUDA_VISIBLE_DEVICES=1`（第一行），日志输出到 `~/runs/provenance_weight_training/rho02_adaptive_tau09_seed42.log`
- **关键参数**：adaptive, tau=0.9, n_min=2, batch_size=4, seed=42, rho=0.2
- **启动方式**：rho02_uniform_seed42 完成后直接 `nohup bash scripts/run_rho02_adaptive_tau09_seed42.sh &`

---
