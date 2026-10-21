# code exp013b dense reward

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp013b-dense-reward_20260514T080513_result.json`
- **Structured JSON:** [`a742f093dc15c1852e2a.json`](../../sessions/a7/a742f093dc15c1852e2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 已释放。以下是完整产出汇总。

---

## 产出

### 1. 代码改动说明

**3 个文件，5 行新增/修改：**

| 文件 | 行号 | 改动 |
|------|------|------|
| `RAGEN/ragen/env/alfworld/config.py:15` | 新增 | `valid_action_bonus: float = 0.0` — AlfredEnvConfig dataclass 加字段，默认 0（不影响已有实验） |
| `RAGEN/ragen/env/alfworld/env.py:196-197` | 新增 | `if action_is_available and self.config.valid_action_bonus > 0: reward += self.config.valid_action_bonus` — step() 中，有效动作加 bonus |
| `RAGEN/config/envs.yaml:399-422` | 新增 | `AlfworldSG_Dense` tag — 复制 AlfworldSG，env_config 加 `valid_action_bonus: 0.5` |
| `RAGEN/config/_alfworld_exp013b_dense_reward.yaml` | 新文件 | 基于 exp012，改 experiment_name / log_dir / tags → AlfworldSG_Dense |

**逻辑**：env.py 的 step() 中，在原有 `reward = score * won` 之后，如果 action 是 admissible action（`action_is_available=True`）且 config 中 `valid_action_bonus > 0`，则 reward 追加 0.5。reward 通过 es_manager 的 `_execute_actions → acc_reward += reward` 正常累积到 GRPO 的 reward signal 中。

### 2. 配置 diff（exp012 vs exp013b）

```diff
- experiment_name: exp012-alfworld-reward-fix
+ experiment_name: exp013b-alfworld-dense-reward
- local_log_dir: "/root/autodl-tmp/checkpoints/exp012_grpo/"
+ local_log_dir: "/root/autodl-tmp/checkpoints/exp013b_grpo/"
- default_local_dir: "/root/autodl-tmp/checkpoints/exp012_grpo/"
+ default_local_dir: "/root/autodl-tmp/checkpoints/exp013b_grpo/"
- tags: ["AlfworldSG"]          # train & val
+ tags: ["AlfworldSG_Dense"]    # valid_action_bonus=0.5
```

其余参数不变：lr=1e-6, kl_loss_coef=0.01, group_size=16, format_penalty=0, resume from step 5。

### 3. Dry-run 结果

- 配置解析 ✓（Hydra 无报错）
- AlfworldSG_Dense tag 识别 ✓
- 模型加载 ✓（Qwen3ForCausalLM 1.72B, checkpoint step 5）
- 环境初始化 ✓（3553 train games, 494 eval games）
- 无 Error/Exception/Traceback

### 4. Pre-flight C002

| 检查项 | 结果 |
|--------|------|
| 入口点 train.py | ✓ |
| Checkpoint exp008_grpo/global_step_5 | ✓ |
| 根分区空闲 | 23G / 25% 使用 ✓ |
| GPU | 0 MiB / 0% ✓ |
| 残留进程 | 无 ✓ |

### 5. 启动命令

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export TMPDIR=/root/autodl-tmp/tmp/ && mkdir -p $TMPDIR && \
export ALFWORLD_DATA=/root/autodl-tmp/alfworld && \
export CUDA_VISIBLE_DEVICES=0,1 && \
cd /root/cost-verify-agent-rl/RAGEN && \
nohup python train.py --config-name _alfworld_exp013b_dense_reward > /root/autodl-tmp/checkpoints/exp013b_grpo/train.log 2>&1 &
```

---
