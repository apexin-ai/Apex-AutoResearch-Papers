# code plan 003b gae config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_003b_gae_config_20260517T073519_result.json`
- **Structured JSON:** [`6e3d56fc934c17604ff9.json`](../../sessions/6e/6e3d56fc934c17604ff9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出报告

### 1. exp029 base config

路径：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_episode_level.yaml`

关键参数：
- `adv_estimator: grpo`，`gamma: 0.95`，full context window mode
- `model_path: /root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`
- 2 GPU，`gpu_memory_utilization: 0.35`，`max_model_len: 20480`
- `total_training_steps: 100`，`ppo_mini_batch_size: 16`

### 2. GAE baseline config

路径：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_gae_baseline.yaml`

关键 diff vs exp029：
| 参数 | exp029 | GAE baseline |
|------|--------|--------------|
| `algorithm.adv_estimator` | grpo | **gae** |
| `algorithm.gamma` | 0.95 | **1.0** |
| `algorithm.lam` | (无) | **0.95** |
| `critic` | 无 | **enabled (auto), model=SFT ckpt, lr=1e-5** |
| `rollout.gpu_memory_utilization` | 0.35 | **0.30** (为 critic 留显存) |
| `trainer.total_training_steps` | 100 | **15** |

### 3. REINFORCE++ baseline config

路径：`/root/cost-verify-agent-rl/RAGEN/config/_alfworld_reinforce_pp_baseline.yaml`

关键 diff vs exp029：
| 参数 | exp029 | REINFORCE++ |
|------|--------|-------------|
| `algorithm.adv_estimator` | grpo | **reinforce_plus_plus_baseline** |
| `algorithm.gamma` | 0.95 | **1.0** |
| `algorithm.lam` | (无) | **1.0** |
| `trainer.total_training_steps` | 100 | **15** |

无 critic，其余与 exp029 一致。

### 4. 验证结果

- YAML 语法：两个文件均通过 `yaml.safe_load` 验证
- Hydra 解析：两个文件均通过 `hydra.compose` 验证，关键字段值正确
- Checkpoint 路径：`/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4` 存在

### 5. 注意事项

- **GAE 显存压力**：critic 与 actor 共用 2×GPU，已将 rollout `gpu_memory_utilization` 降至 0.30。如果 OOM，可进一步降低或开启 `critic.model.enable_gradient_checkpointing: True`（dp_critic.yaml 默认已开启）。
- **`need_critic` 自动判定**：verl 中 `adv_estimator=gae` 会自动启用 critic（无需显式设 `critic.enable: True`）。
- **REINFORCE++ 枚举值**：使用 `reinforce_plus_plus_baseline`（带 running mean baseline），而非 `reinforce_plus_plus`（后者是无 baseline 的原始版本）。

---
