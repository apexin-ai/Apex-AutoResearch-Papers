# SFT Warmup 方案 — ALFWorld + RAGEN + Qwen3-1.7B

## 1. 问题定义

Qwen3-1.7B base 模型不会自发输出 `<think>...</think><answer>...</answer>` 格式。RAGEN 框架解析 action 时依赖该格式，导致 action 解析 100% 失败。

**解决方案**: SFT warmup → 教模型输出正确格式 → 再接 GRPO 训练。

---

## 2. 文献调研

### 2.1 RAGEN 论文

- 使用 **Qwen2.5-Instruct** 模型（已会遵循格式指令），未做 SFT warmup
- 格式: `<think> [reasoning] </think> <answer> [action] </answer>`（`enable_think: True`）或 `<answer> [action] </answer>`（`enable_think: False`）
- RAGEN 在 Sokoban 上 SFT baseline 达 74.6%，Frozen Lake 上 23%
- **RAGEN 代码中无 SFT 训练脚本**，仅有 RL（GRPO/PPO）训练流程

### 2.2 "Warm Up Before You Train" (EMNLP 2025)

- 两阶段: SFT warmup（domain-agnostic 逻辑推理数据）→ RLVR（50-100 条 target domain 数据）
- Warmup 数据: QwQ-32B 在 Knights & Knaves 逻辑题上生成长 CoT
- 结论: warmup 后模型收敛更快，泛化性更好
- **关键参数**: warmup SFT 不需要 rejection sampling，目标是习得推理行为模式

### 2.3 SkillRL (ICLR 2026)

- SFT → RL 两阶段 pipeline
- SFT 使用 **LLaMA-Factory** 框架
- Qwen2.5-7B-Instruct 在 ALFWorld 上超越 GPT-4o 41.9%
- 已开源 SFT 数据生成代码（`examples/sft_data_generation/`）

### 2.4 AgentGym-RL

- SFT + progressive horizon-scaling RL
- 支持 PPO、GRPO、RLOO、REINFORCE++ 等算法
- 渐进式增加 interaction turns

### 2.5 数据量参考

| 来源 | SFT 数据量 | Epochs | 备注 |
|------|-----------|--------|------|
| Warm Up Before You Train | warmup: ~1000 条 CoT; target: 50-100 条 | 1-3 | domain-agnostic warmup |
| SkillRL | 未明确，使用 LLaMA-Factory | 2-3 | 成功轨迹 |
| RAGEN SFT baseline | 未明确 | - | 用于 ablation 对比 |
| 通用实践 | 200-2000 条轨迹 | 2-3 | 格式教学 100 条即可见效 |

---

## 3. 可用公开数据集

| 数据集 | 来源 | 特点 |
|--------|------|------|
| [u-10bei/sft_alfworld_trajectory_dataset](https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset) (v1-v5) | HuggingFace | 模板合成，无需 LLM/环境交互，支持 6 种任务，ReAct 格式，messages 字段 |
| [yijunyang/alfworld-sft-dataset](https://huggingface.co/datasets/yijunyang/alfworld-sft-dataset) | HuggingFace | ALFWorld SFT 数据 |
| [zai-org/AgentInstruct (alfworld split)](https://huggingface.co/datasets/zai-org/AgentInstruct) | HuggingFace | Agent 指令数据含 ALFWorld |

**推荐**: 优先尝试 `u-10bei/sft_alfworld_trajectory_dataset`，已是 chat format（messages 字段），最接近 RAGEN 需要的格式。

---

## 4. RAGEN 格式要求

### 4.1 对话格式

RAGEN 使用标准 chat format（Qwen chat template）：

```
[system] You're a helpful assistant. {env_instruction}
[user] {observation + admissible actions}
[assistant] <think>reasoning</think><answer>action</answer>
[user] {next observation + admissible actions}
[assistant] <think>reasoning</think><answer>action</answer>
...
```

### 4.2 AlfworldSG 的 env_instruction

```
You are an expert agent in the ALFRED Embodied Environment.
Complete household tasks by navigating and interacting with objects.

Before each action, you MUST first produce a self-guidance assessment:
[Assessment: positive/neutral/negative] - evaluate your current progress.
[Reasoning: one sentence analyzing what has been accomplished and what remains.]
[Suggestion: the best next action from admissible actions.]

Your reasoning with self-guidance MUST be enclosed within <think> </think> tags.
Then choose an admissible action and present it within <answer>...</answer> tags.
```

### 4.3 SFT 数据样例

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You're a helpful assistant. You are an expert agent in the ALFRED Embodied Environment. Complete household tasks by navigating and interacting with objects.\n\nBefore each action, you MUST first produce a self-guidance assessment in your reasoning:\n[Assessment: positive/neutral/negative] - evaluate your current progress toward the task goal.\n[Reasoning: one sentence analyzing what has been accomplished and what remains.]\n[Suggestion: the best next action from admissible actions.]\n\nYour reasoning with self-guidance MUST be enclosed within <think> </think> tags.\nThen choose an admissible action and present it within <answer>...</answer> tags.\nMax response length: 512 words (tokens)."
    },
    {
      "role": "user",
      "content": "You are in the middle of a room. Looking quickly around you, you see a cabinet 6, a cabinet 5, ...\nYour task is to: put some spraybottle on toilet.\n\nAdmissible actions: [go to cabinet 1, go to cabinet 2, ...]"
    },
    {
      "role": "assistant",
      "content": "<think>[Assessment: neutral] [Reasoning: I just started, need to find a spraybottle first. Cabinets and shelves are likely locations.] [Suggestion: go to cabinet 1]</think><answer>go to cabinet 1</answer>"
    },
    {
      "role": "user",
      "content": "You arrive at cabinet 1. The cabinet 1 is closed.\n\nAdmissible actions: [open cabinet 1, go to cabinet 2, ...]"
    },
    {
      "role": "assistant",
      "content": "<think>[Assessment: neutral] [Reasoning: Found cabinet 1 but it's closed. Need to open it to check for spraybottle.] [Suggestion: open cabinet 1]</think><answer>open cabinet 1</answer>"
    }
  ]
}
```

---

## 5. 数据生成方案

### 方案 A: 使用公开数据集 + 格式转换（推荐，快速启动）

1. 下载 `u-10bei/sft_alfworld_trajectory_dataset`
2. 将其 messages 格式转换为 RAGEN 的 `<think>...</think><answer>...</answer>` 格式
3. 替换 system prompt 为 AlfworldSG 的 env_instruction
4. 确保 action 在 admissible actions 列表中

**优点**: 零成本，立即可用
**缺点**: 轨迹质量可能不如强模型生成；self-guidance 格式需要后处理添加

### 方案 B: 强模型 rollout 生成（高质量）

1. 用 Qwen3-30B-A3B（或 Qwen3-32B）在 ALFWorld 环境中做 rollout
2. 使用 RAGEN 的 eval 脚本（`agent_proxy.py`）+ 强模型做 inference
3. 收集成功轨迹（reward > 0 的 episode）
4. 转换为 SFT 格式

**预估**:
- 目标: 200-500 条成功轨迹
- 强模型 ALFWorld 成功率约 40-60%（需要 ~500-1000 次 rollout）
- 每条轨迹约 10-30 turns，token 消耗约 2000-5000 tokens/轨迹
- 总 token 消耗: ~2-5M tokens
- 如果用本地 Qwen3-30B-A3B（服务器上跑）: 免费，耗时约 2-4 小时
- 如果用 API: 约 $2-10

**优点**: 数据质量高，格式完全匹配
**缺点**: 需要部署强模型或用 API

### 方案 C: 混合方案（推荐）

1. **Phase 1**: 用公开数据集做格式教学（~100 条），训练 1 epoch
   - 目标: 让模型学会输出 `<think>...</think><answer>...</answer>` 格式
2. **Phase 2**: 用 Phase 1 模型或强模型做 rollout，收集成功轨迹（~200 条）
3. **Phase 3**: 合并数据做最终 SFT（2-3 epochs）

---

## 6. SFT 训练方案

### 6.1 工具选择

RAGEN 本身不含 SFT 训练功能。推荐使用:

| 工具 | 优点 | 缺点 |
|------|------|------|
| **ms-swift** | Qwen 官方推荐，支持 LoRA/全量，中文文档好 | 配置较复杂 |
| **LLaMA-Factory** | SkillRL 使用，简单易用 | - |
| **TRL SFTTrainer** | 轻量，和 RAGEN 的 verl 生态兼容 | 功能较少 |
| **直接用 transformers** | 最灵活 | 需手写训练循环 |

**推荐**: TRL SFTTrainer 或 ms-swift

### 6.2 训练参数

```yaml
model: /root/cost-verify-agent-rl/models/Qwen3-1.7B
method: full  # 1.7B 足够小，可以全量微调
lr: 2e-5
epochs: 2-3
batch_size: 4
gradient_accumulation: 4
max_seq_length: 4096  # ALFWorld 轨迹较长
warmup_ratio: 0.1
weight_decay: 0.01
bf16: true
# 如果用 LoRA:
lora_rank: 64
lora_alpha: 128
lora_target: all-linear
```

### 6.3 GPU 需求

- Qwen3-1.7B 全量 SFT: ~12GB VRAM（bf16）
- 2× RTX PRO 6000 96GB 绰绰有余，单卡即可
- 训练时间: 200-500 条数据，2-3 epochs，约 10-30 分钟

---

## 7. 执行计划

| 步骤 | 内容 | 耗时 |
|------|------|------|
| 1 | 下载 u-10bei 数据集，检查格式 | 10 min |
| 2 | 编写格式转换脚本（→ RAGEN format） | 30 min |
| 3 | 安装 SFT 训练框架（TRL/ms-swift） | 15 min |
| 4 | SFT 训练 Qwen3-1.7B | 20-30 min |
| 5 | 验证: 用 SFT 模型跑 RAGEN eval，检查格式输出 | 15 min |
| 6 | （可选）用 SFT 模型接入 GRPO 训练 | - |

**总预估时间**: 1.5-2 小时

---

## 8. RAGEN 代码中 SFT 相关功能盘点

| 功能 | 存在? | 说明 |
|------|-------|------|
| SFT 训练脚本 | ❌ | 无。需外部工具 |
| SFT 数据生成脚本 | ❌ | 无。需自行编写 |
| 数据格式转换 | ✅ | `scripts/convert_to_jsonl.py` 可将 rollout 结果转 JSONL |
| Eval/Rollout 脚本 | ✅ | `ragen/llm_agent/agent_proxy.py` 可用于强模型 rollout |
| Chat template 支持 | ✅ | `ctx_manager.py` 中的 `_build_system_content` 等函数 |
| Format prompt 定义 | ✅ | `ctx_manager.py` 中 `_build_format_prompt`，定义 think/answer 格式 |
| ALFWorld 环境 | ✅ | `ragen/env/alfworld/` 完整可用 |

---

## Sources

- [RAGEN GitHub](https://github.com/mll-lab-nu/RAGEN)
- [RAGEN Paper](https://arxiv.org/abs/2504.20073)
- [Warm Up Before You Train (EMNLP 2025)](https://arxiv.org/abs/2505.13718)
- [SkillRL (ICLR 2026)](https://github.com/aiming-lab/SkillRL)
- [AgentGym-RL](https://arxiv.org/abs/2509.08755)
- [u-10bei/sft_alfworld_trajectory_dataset](https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset)
- [yijunyang/alfworld-sft-dataset](https://huggingface.co/datasets/yijunyang/alfworld-sft-dataset)
- [AgentTrek (ICLR 2025 Spotlight)](https://github.com/xlang-ai/AgentTrek)
