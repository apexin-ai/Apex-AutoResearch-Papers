# code exp028 config prep

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp028_config_prep_20260515T202818_result.json`
- **Structured JSON:** [`e7e77f121c9b7e7ffd59.json`](../../sessions/e7/e7e77f121c9b7e7ffd59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

配置解析验证通过。总结：

**已创建 4 个文件：**

| 文件 | 路径 |
|------|------|
| exp028a config | `RAGEN/config/_alfworld_exp028a_recipe_fix.yaml` |
| exp028b config | `RAGEN/config/_alfworld_exp028b_full_recipe.yaml` |
| exp028a script | `scripts/run_exp028a_recipe_fix.sh` |
| exp028b script | `scripts/run_exp028b_full_recipe.sh` |

**exp028a（最小变更）vs exp027 差异：**
- `model_path`: SFT v4 → `Qwen/Qwen2.5-1.5B-Instruct`（Instruct 冷启动）
- `format_penalty`: 0 → -0.1（解决全零 group 零梯度）

**exp028b（全 recipe 对齐）额外变更：**
- LR: 5e-7 → 1e-6
- KL coef: 0.005 → 0.01
- mini_batch: 32 → 256
- steps: 50 → 150
- history_length: 5 → 2
- prompt_length: 4096 → 2048
- response_length: 1024 → 512
- loss_agg_mode: seq-mean-token-mean → token-mean
- env_groups: 8×16 → 16×8（总 rollout 仍 128）

**注意事项：**
1. **Qwen2.5-1.5B-Instruct 不在服务器上**，启动前需先下载（建议用 ModelScope 或 `source /etc/network_turbo` 后 HF 下载）
2. `format_penalty` 在 `ctx_manager.py:291` 中 **GRPO normalization 之前** 加到 `acc_scores`，确认在 GRPO 模式下生效——全失败 group 中有 invalid action 的 episode 会被额外扣 0.1/step，产生非零方差，梯度不再为零

---
