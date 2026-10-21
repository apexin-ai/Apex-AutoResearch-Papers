# diagnose 8b cell c episode v9

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_8b_cell_c_episode_v9_20260519T181748_result.json`
- **Structured JSON:** [`d6bd04ffacd055314023.json`](../../sessions/d6/d6bd04ffacd055314023.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

```json
{
  "root_cause": "train.py:241 的 strategy 判断只匹配 'fsdp'，v9 config 设置了 actor.strategy='fsdp2'，命中 else 分支触发 line 245 的 raise NotImplementedError",
  "error_type": "infrastructure",
  "config_diff": "v9 新增: actor.strategy=fsdp2, actor.fsdp_config.strategy=fsdp2, actor.fsdp_config.offload_policy=True, actor.fsdp_config.param_offload=False, model.enable_activation_offload=true, ppo_mini_batch_size 2→4, rollout.gpu_memory_utilization 0.22→0.25; 缺失: critic.strategy 未设为 fsdp2（默认 fsdp）",
  "fix_steps": [
    "1. train.py:241 — 将 `== 'fsdp'` 改为 `in ('fsdp', 'fsdp2')`，与 verl 上游 main_ppo_split.py:130 的模式一致",
    "2. train.py:242 — 将 `assert config.actor_rollout_ref.actor.strategy == config.critic.strategy` 改为 `assert config.critic.strategy in ('fsdp', 'fsdp2')`，允许 actor/critic 使用不同 FSDP 版本",
    "3. _alfworld_8b_cell_c_v9.yaml — 添加 `critic: strategy: fsdp2`，否则 critic 默认 fsdp 与 actor 的 fsdp2 不匹配（assertion 会失败）"
  ],
  "can_auto_fix": true,
  "fix_complexity": "简单配置修改+train.py 两行代码改动"
}
```

**详细分析**：

- `train.py:241` 的分支逻辑：
  ```python
  if config.actor_rollout_ref.actor.strategy == 'fsdp':    # 只匹配 'fsdp'
      ...
  else:
      raise NotImplementedError                             # 'fsdp2' 落到这里
  ```

- RAGEN 的 worker 层已经支持 fsdp2：
  - `ragen/workers/fsdp_workers.py:338` — CriticWorker 有 `elif config.strategy == "fsdp2":` 分支
  - `ragen/workers/fsdp_workers.py:43-44` — 已导入 `apply_fsdp2`, `fsdp2_load_full_state_dict`
  - `verl/workers/fsdp_workers.py:509-535` — ActorRolloutRefWorker 完整支持 fsdp2 + CPUOffloadPolicy

- 问题仅在 **入口调度层**（train.py），底层实现已就绪，只是入口的 if 条件没有跟上 verl 上游的 `in {'fsdp', 'fsdp2'}` 写法。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "train.py:241 的 strategy 判断只匹配 'fsdp'，v9 config 设置了 actor.strategy='fsdp2'，命中 else 分支触发 line 245 的 raise NotImplementedError",
    "error_type": "infrastructure",
    "config_diff": "v9 新增: actor.strategy=fsdp2, actor.fsdp_config.strategy=fsdp2, actor.fsdp_config.offload_policy=True, actor.fsdp_config.param_offload=False, model.enable_activation_offload=true, ppo_mini_batch_size 2→4, rollout.gpu_memory_utilization 0.22→0.25; 缺失: critic.strategy 未设为 fsdp2（默认 fsdp）",
    "fix_steps": [
      "1. train.py:241 — 将 `== 'fsdp'` 改为 `in ('fsdp', 'fsdp2')`，与 verl 上游 main_ppo_split.py:130 的模式一致",
      "2. train.py:242 — 将 `assert config.actor_rollout_ref.actor.strategy == config.critic.strategy` 改为 `assert config.critic.strategy in ('fsdp', 'fsdp2')`，允许 actor/critic 使用不同 FSDP 版本",
      "3. _alfworld_8b_cell_c_v9.yaml — 添加 `critic: strategy: fsdp2`，否则 critic 默认 fsdp 与 actor 的 fsdp2 不匹配（assertion 会失败）"
    ],
    "can_auto_fix": true,
    "fix_complexity": "简单配置修改+train.py 两行代码改动"
  }
}
```

</details>

---
