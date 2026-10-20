# fix eval script paths

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval-script-paths_20260516T164937_result.json`
- **Structured JSON:** [`a4f3245fa935d81287fc.json`](../../sessions/a4/a4f3245fa935d81287fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

| 脚本 | 服务器 | 修正前路径 | 修正后路径 | 状态 |
|------|--------|-----------|-----------|------|
| `eval_hybrid_rho04_seed42.sh` | westd-41312 | `output/models/hybrid_rho04_seed42/final` (相对) | — | **无需修正** (通过 symlink 正确解析到数据盘) |
| `eval_hybrid_rho06_seed42.sh` | westd-41312 | `output/models/hybrid_rho06_seed42/final` (相对) | — | **无需修正** (同上；`final/` 将在训练完成时创建) |
| `run_batchsize16.sh` | westd-41312 | `/root/autodl-tmp/output/models/batchsize16_nmin8_seed42/` | `output/models/batchsize16_nmin8_seed42` | **已修正** |
| `run_grid_b0_2_seed42.sh` | westd-41312 | `/root/autodl-tmp/output/models/grid_b0_2_seed42/` | `output/models/grid_b0_2_seed42` | **已修正** |
| `run_threshold_q07_seed42.sh` | westd-47453 | `output/models/threshold_q07_seed42` (相对) | — | **无需修正** (路径正确 + 自带 inline eval: `--eval_steps 500`) |

**关键发现：**
- 两台服务器 `/root/provenance_weight_training/output` 均为 symlink → `/root/autodl-tmp/provenance_weight_training/output`，相对路径通过 symlink 正确指向数据盘
- hybrid eval 脚本路径正确，训练尚未完成（当前 checkpoint-2500），`final/` 目录将在训练结束时由 `pretrain_weighted.py` 自动保存
- threshold_q07 训练自带 `--eval_data_path` + `--eval_steps 500`，无需额外 post-hoc eval

---
