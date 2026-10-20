# fix random reweight resubmit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_random_reweight_resubmit_20260516T092825_result.json`
- **Structured JSON:** [`6c85dd81b761cc9e3085.json`](../../sessions/6c/6c85dd81b761cc9e3085.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

- **根因**：脚本有 `WANDB_MODE=offline` 但同时传了 `--use_wandb`（`store_true`），Python 代码中会执行 `report_to.append("wandb")` 触发 wandb 初始化，仍需 API key
- **修复**：从脚本中移除了 `--use_wandb`、`--wandb_project`、`--wandb_run_name` 三个参数
- **状态**：训练已重新启动，PID 318752，cuda:2 占用 46.5GB，已在 step 6/6103 正常推进（~2.2s/it，预计 ~3.7h 完成）
- **Registry**：已更新为 RUNNING，retry_count=3

---
