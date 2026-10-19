# research ragen alfworld code

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ragen-alfworld-code_20260513T191636_result.json`
- **Structured JSON:** [`79e8a4408d43d2e11c70.json`](../../sessions/79/79e8a4408d43d2e11c70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 调研结果

### 1. RAGEN 官方 ALFWorld Config vs 我们的差异

**RAGEN 没有官方 ALFWorld training config。** 只有环境定义（`envs.yaml` 中的 `Alfworld`/`AlfworldOOD`/`AlfworldSG`），无对应的训练 yaml。所有 `_alfworld_*.yaml` 都是我们写的。

与 base.yaml 默认值对比：

| 参数 | base.yaml 默认 | exp001 | 影响 |
|------|---------------|--------|------|
| **model_path** | `Qwen/Qwen2.5-3B-Instruct` | `Qwen3-1.7B` (base) | **致命问题** |
| train group_size | 16 | 4 | 样本太少 |
| train env_groups | 8 | 4 | 样本太少 |
| max_model_len | 3600 | 4096→16384 (已修) | 已修复 |
| adv_estimator | gae (PPO) | grpo | 不同算法 |
| max_turn | 5 | 10 | ALFWorld 需要多步 |
| max_actions_per_turn | 2 | 1 | OK |

### 2. Reward Function 详细说明

**三层结构：**

- **环境层（env.py）**：纯 0/1 sparse reward → `reward = 10.0 * float(won)`。只有任务完成才给 +10，中间无任何 partial reward。
- **Format penalty（es_manager.py）**：每个 turn 如果 action 解析失败（`_parse_response` 匹配不到 `&lt;think>...&lt;/think>&lt;answer>...&lt;/answer>` 格式），`penalty += -0.1`。10 个 turn 全失败 = -1.0。
- **最终 reward**：`env_reward + accumulated_penalty`。exp_001 中模型完全不输出正确格式 → 每个 episode reward ≈ 0 + (-1.0) = -1.0。

**为什么 advantage = 0：** GRPO 在 group 内归一化 `(R - mean) / std`。group_size=4，4 个 rollout 都得 -1.0 → std = 0 → advantage = 0 → 无梯度。

### 3. SFT/Warm-start 机制

**不存在。** RAGEN 框架无内置 SFT/warm-start。verl 子模块有 SFT trainer 但 RAGEN 训练流程不使用。整个方案依赖模型零样本能力。

### 4. Instruct vs Base 模型

**RAGEN 所有官方配置使用 Instruct 模型**（`Qwen2.5-3B-Instruct`）。框架假定模型已具备：
- 遵循 `&lt;think>...&lt;/think>&lt;answer>...&lt;/answer>` 格式
- 理解 system prompt 中的任务指令
- 从 admissible actions 列表中选择有效 action

**Qwen3-1.7B 是 base 模型**，不理解 chat 格式，不遵循指令，输出随机文本。

### 5. max_model_len 修复

两个配置文件已修改为 16384：
- `_alfworld_exp001.yaml`: 4096 → 16384
- `_alfworld_exp001b.yaml`: 8192 → 16384

### 6. Bootstrap 问题根因分析与修复建议

**根因链路：**
1. Base 模型不遵循指令 → 不输出 `&lt;think>/&lt;answer>` 格式
2. `_parse_response` 返回空 actions → format_penalty 累积
3. 无有效 action 到达环境 → env reward 恒为 0
4. 每个 episode 总 reward ≈ -1.0，group 内全部相同
5. GRPO 归一化 std=0 → advantage=0 → 零梯度

**修复方案（优先级排序）：**

1. **P0: 换 Instruct 模型**。下载 `Qwen3-1.7B-Instruct` 或 `Qwen2.5-3B-Instruct`。这是唯一能立即解决零梯度问题的方案。
2. **P1: 增大 group_size**。从 4 增到 16（匹配 base.yaml 默认值）。更大的 group 增加出现 reward 方差的概率。
3. **P2: 如果坚持用 base 模型**——需要 SFT warm-start：用少量 `&lt;think>reasoning&lt;/think>&lt;answer>valid_action&lt;/answer>` 样本微调，让模型学会格式。但这偏离了 RAGEN 的设计假设。

---
