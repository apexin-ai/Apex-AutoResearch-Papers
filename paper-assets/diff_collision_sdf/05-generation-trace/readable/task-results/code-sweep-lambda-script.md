# code sweep lambda script

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sweep_lambda_script_20260520T120751_result.json`
- **Structured JSON:** [`fcc104e36353c45faf6f.json`](../../sessions/fc/fcc104e36353c45faf6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。脚本 `/root/colliforce-vla/scripts/sweep_lambda.sh` 已创建并通过 `--help` 验证。

功能：串行遍历 `--lambdas` 列表，每个值调用 `train_a3_hook.py` 并传入 `--lambda_refine`、`--exp_name a3_lambda{VALUE}_{scene}_s{seed}`，日志 tee 到 `outputs/{exp_name}/train.log`。

---
