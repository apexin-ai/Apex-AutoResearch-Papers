# fix hsweep val size and h10 config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_hsweep-val-size-and-h10-config_20260517T164925_result.json`
- **Structured JSON:** [`5a823bc19c1d63ed60be.json`](../../sessions/5a/5a823bc19c1d63ed60be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### P0: seed2 val set 大小
- **config 已正确**：`val: env_groups: 32, group_size: 1` = 32 val tasks，与 seed1/论文一致
- **无需修改**

### P1: h=10 config + auto_next 链

**h=10 config**: 已存在 `_alfworld_hsweep_h10.yaml`，参数正确：
- `step_independent_history_length: 10`
- γ=0.95, 15 steps, GRPO step_independent
- val: 32 tasks (env_groups: 32, group_size: 1)

**auto_next 链已修改**：
- 旧序列：`2:2 → 5:1 → 10:1 → ...`
- 新序列：`2:2 → 10:1 → 5:1 → 20:1 → full:1 → 2:3 → ...`
- 机制：`launch_hsweep.sh` 训练结束后自动调用 `auto_next_hsweep.sh 2 2`，脚本查序列取下一个 entry `10:1`

### Seed2 当前进度
- **Step 1/15 完成**，正在跑 step 2 的 rollout
- 每 step 约 53 分钟
- 启动时间：2026-05-17 22:29
- 预计剩余：~12 小时

---
