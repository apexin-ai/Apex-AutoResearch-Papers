# ops threshold q07 recovery

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_threshold-q07-recovery_20260516T185326_result.json`
- **Structured JSON:** [`b9e2c2f0460c03940e55.json`](../../sessions/b9/b9e2c2f0460c03940e55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本语法验证通过。

---

## 恢复总结

| 项目 | 状态 |
|------|------|
| wandb/ 目录 | 已不存在（无需删除） |
| step_metrics | 卡在 step 5999，最后修改 02:21:45（20+ 分钟无更新） |
| PID 324550 | 已 kill |
| checkpoint-5500 | 存在于 `/root/autodl-tmp/provenance_weight_training/output/models/threshold_q07_seed42/checkpoint-5500/` |

**恢复脚本**：`/root/provenance_weight_training/scripts/run_threshold_q07_resume_r2.sh`

关键变更（vs 原脚本）：
- `--resume_from_checkpoint` → `checkpoint-5500`（原为 checkpoint-2000）
- `WANDB_MODE=disabled`（原为 offline）
- `--use_wandb` 和 wandb 相关参数已移除
- `CUDA_VISIBLE_DEVICES=-1`（submit_training_job 会替换）

从 step 5500 恢复到 6104，剩余 604 steps，预计 10-20 分钟完成。需要 submit_training_job 提交。

---
