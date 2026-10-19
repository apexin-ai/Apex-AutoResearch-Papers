# fix exp028c val episodes

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp028c_val_episodes_20260516T032314_result.json`
- **Structured JSON:** [`b0c6e4a564085cc41902.json`](../../sessions/b0/b0c6e4a564085cc41902.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。

**修改**：`RAGEN/config/_alfworld_exp028c_selfguide_recipe.yaml` 中 val 的 `env_groups: 16 → 140`，`n_groups: [16] → [140]`。总 val episodes 从 16 提升到 140，对齐 Self-Guide 论文（valid_seen 共 234 games，140 在范围内）。

**对当前训练无影响**——Hydra 在 `train.py` 启动时一次性把配置加载到 OmegaConf 内存对象，运行中不重读 YAML。PID 824675 继续以原 16 episodes 评估。下次重启实验自动生效。

---
