# deploy exp 045 treatment extension

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_exp_045_treatment_extension_20260522T094126_result.json`
- **Structured JSON:** [`aa1097967d30a9ea282a.json`](../../sessions/aa/aa1097967d30a9ea282a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇报：

**exp_045_treatment_extension_008d_s3**
- **PID**: 70945（GPU 0，3359 MiB）
- **tmux 会话**: `exp045`
- **恢复确认**: 从 step 112,000 恢复，目标 300,000 steps
- **启动命令**: `python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3`
- **日志**: `logdir/exp_045_treatment_extension_008d_s3/train.log`

注意：任务指定的 `--dt_emb trained` 和 `--subsample_imagination True` 并非实际参数名。实际使用 `--gate_fixed_dt 2 --gate_subsample_max_dt 2`（与源实验 008d_civo_trigger_s2.sh 脚本一致）。

---
