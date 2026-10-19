# code prepare gsweep configs

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_gsweep_configs_20260518T001214_result.json`
- **Structured JSON:** [`442acd66e52dd4ffc82b.json`](../../sessions/44/442acd66e52dd4ffc82b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个配置文件全部已存在，Hydra 加载验证通过。

**配置汇总：**

| 配置文件 | gamma | h | experiment_name | 路径 |
|---|---|---|---|---|
| `_alfworld_gamma_sweep_g080_h5.yaml` | 0.8 | 5 | gsweep-g080-h5 | `/root/cost-verify-agent-rl/RAGEN/config/` |
| `_alfworld_gamma_sweep_g095_h5.yaml` | 0.95 | 5 | gsweep-g095-h5 | `/root/cost-verify-agent-rl/RAGEN/config/` |
| `_alfworld_gamma_sweep_g100_h5.yaml` | 1.0 | 5 | gsweep-g100-h5 | `/root/cost-verify-agent-rl/RAGEN/config/` |

**关键参数（所有配置一致）：**
- `algorithm.gamma` — 字段名确认为 `gamma`
- `algorithm.high_level_gamma` = 0.95（所有配置统一）
- `step_independent_history_length` = 5
- `total_training_steps` = 15
- `CUDA_VISIBLE_DEVICES` = "2,3"
- `val.env_groups` = 32（满足 C003 ≥16 episodes 约束）
- checkpoint 输出到 `/root/autodl-tmp/checkpoints/gsweep-g{080,095,100}-h5/`

**注意：** 配置目录是 `config/` 而非任务描述中的 `configs/`。Hydra 有 `_self_` 缺失警告，但不影响运行（与模板 g050 一致）。g050 实验完成后可直接启动 g080。

---
