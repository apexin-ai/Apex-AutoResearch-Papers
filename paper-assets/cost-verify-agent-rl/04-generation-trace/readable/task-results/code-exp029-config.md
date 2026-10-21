# code exp029 config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp029_config_20260516T083041_result.json`
- **Structured JSON:** [`6dd1bdeb1343ca3e6ab6.json`](../../sessions/6d/6dd1bdeb1343ca3e6ab6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出：

- **配置文件**: `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_episode_level.yaml`
- **启动脚本**: `/root/cost-verify-agent-rl/scripts/run_exp029_episode_level.sh`
- **Diff 报告**: `/root/cost-verify-agent-rl/artifacts/exp029_episode_level/intermediate/config_diff.md`

验证结果: `OK: full 140 32 0.92 16384` — 所有关键参数正确。

注意：配置实际路径在 `RAGEN/config/` 而非任务描述中的 `configs/`，启动脚本入口点已对齐 exp028c（`cd RAGEN && python train.py --config-name ...`）。训练未启动。

---
