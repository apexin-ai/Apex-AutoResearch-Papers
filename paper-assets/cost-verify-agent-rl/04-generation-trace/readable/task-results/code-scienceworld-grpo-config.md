# code scienceworld grpo config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scienceworld_grpo_config_20260519T201551_result.json`
- **Structured JSON:** [`750b73b10e6bd77a6e7c.json`](../../sessions/75/750b73b10e6bd77a6e7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 config 均通过 Hydra 解析验证（`_self_` 警告是已有 ALFWorld configs 同样存在的 Hydra 1.x 兼容性提示，不影响运行）。

---

## 产出报告

### 1. 文件路径
- Cell A: `/root/cost-verify-agent-rl/RAGEN/config/_scienceworld_cell_a.yaml`
- Cell C: `/root/cost-verify-agent-rl/RAGEN/config/_scienceworld_cell_c.yaml`

### 2. 与 ALFWorld 模板的 diff 摘要

基于 1.7B ALFWorld 模板（exp026 = Cell A, exp029 = Cell C），改动：

| 参数 | ALFWorld 1.7B | ScienceWorld |
|------|-------------|--------------|
| model_path | `qwen3_exp021_ragen_sft_v4` | `scienceworld_sft/global_step_448/huggingface` |
| CUDA_VISIBLE_DEVICES | `"0,1"` (2 GPU) | `"0,1,2,3"` (4 GPU) |
| n_gpus_per_node | 2 | 4 |
| env tags | `["AlfworldSG"]` | `["ScienceWorldBoil"]` |
| step_independent_history_length (Cell A) | 5 → **2** | 2（对齐 8B canonical Cell A 定义） |
| loss_agg_mode (Cell A) | `seq-mean-token-mean` → **`token-mean`** | token-mean（对齐 8B canonical） |
| ppo_mini_batch_size (Cell A) | 32 → **16** | 16（4 GPU 下更合理） |
| checkpoint 路径 | `exp026/` / `exp029/` | `scienceworld-cell-a/` / `scienceworld-cell-c/` |

其余超参（lr=1e-6, gamma=0.95, KL coef=0.01, clip ratio, entropy_coeff 等）保持一致。

### 3. Dry-run 结果
- Cell A: **通过** — model_path、env_tags、context_window_mode 全部正确解析
- Cell C: **通过** — ppo_max_token_len_per_gpu=65536 正确加载

### 4. ScienceWorld reward 机制
- **Continuous reward**，非 binary。公式：`reward = (episode_score / 100) * 10.0`，范围 0.0~10.0
- **Sparse**：仅在 episode 结束时发放（`done=True`），中间步骤 reward=0
- 对 Cell A（step-level advantage）：所有中间步 reward=0，只有最后一步有非零 reward。step-level credit assignment 几乎无法工作——这正是实验预期的失败模式
- 对 Cell C（episode-level advantage）：整个 episode 的 reward 作为一个 scalar 参与 GRPO 优势估计，与 continuous reward 兼容
- GRPO 的 `norm_adv_by_std_in_grpo: True` 会对 advantage 做 group 内标准化，continuous reward 的方差信号比 binary 更丰富

### 5. max_turn = 50 的理由
- envs.yaml 中 `ScienceWorldBoil` 设置 `max_actions_per_traj: 50`，与 ALFWorld 一致
- 环境内部 `max_steps: 100`，但 agent 每 turn 执行 1 action（`max_actions_per_turn: 1`），50 turns = 50 env steps
- Boil 任务典型长度 20~40 步，50 turns 留有余量
- 如后续发现截断率过高，可提升至 70~80

---
