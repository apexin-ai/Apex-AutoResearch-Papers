# SFT eval vs RAGEN GRPO rollout 推理差异诊断

**日期**: 2026-05-15
**背景**: exp021 SFT 模型在 eval_sft_fast 中 action_is_valid=87.5%，在 RAGEN GRPO step 0 val（训练前）中降至 68.75%。

## 1. 对比表

| 维度 | SFT eval (eval_exp021.py) | RAGEN GRPO val (exp023) | 差异 |
|------|---------------------------|--------------------------|------|
| **Sampling: temperature** | 0.4 | 0.4 | 无 |
| **Sampling: top_p** | **0.95** | **1.0** | ⚠️ 不同 |
| **Sampling: top_k** | -1 (all) | -1 (all) | 无 |
| **Sampling: max_tokens** | **256** | **1024** | ⚠️ 不同 |
| **Sampling: repetition_penalty** | 1.0 | 1.0 | 无 |
| **Sampling: stop tokens** | 显式 `["<\|im_end\|>", "<\|endoftext\|>"]` | 依赖模型 EOS [151645, 151643] | 低：实际等价 |
| **System prompt: 格式指令** | `"present it within <answer>...</answer> tags"` | `"Do NOT wrap the action in any tags"` | ⚠️⚠️ 严重矛盾 |
| **System prompt: 示例** | 无示例 | 有示例（bare action） | ⚠️ 不同 |
| **User content 格式** | 裸 obs: `{obs}\n\nAdmissible actions: [...]` | 结构化: `Turn N:\nState:\n{state}\nYou have {X} actions left. Always output: <think>...</think><answer>...</answer>` | ⚠️⚠️ 严重不同 |
| **Turn 间反馈** | 无 | `Reward:\n{value}\n` | ⚠️ 不同 |
| **Generation prefix** | `<\|im_start\|>assistant\n`（标准） | `<\|im_start\|>assistant\n<think>`（强制 think 前缀） | 低 |
| **Max prompt length** | 30,000 tokens | ~4,096-7,168 tokens | ⚠️ 不同 |
| **模型路径** | `/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/final` | `/root/autodl-tmp/checkpoints/qwen3_exp021_ragen_sft_v4`（symlink → 同一目录） | 无 |
| **Tokenizer / chat_template** | 同一 tokenizer, `apply_chat_template` | 同一 tokenizer, `apply_chat_template` | 无 |

## 2. 差异清单

### 差异 1: System Prompt 格式指令互相矛盾 [严重]

**SFT eval**:
```
Your reasoning with self-guidance MUST be enclosed within <think> </think> tags.
Then choose an admissible action and present it within <answer>...</answer> tags.
```

**RAGEN (AlfworldSG env_instruction)**:
```
Your reasoning MUST be enclosed within <think> </think> tags.
After the closing </think> tag, output EXACTLY ONE admissible action command directly.
The action must be a precise ALFWorld command from the admissible actions list.
Do NOT wrap the action in any tags.
```

**且 RAGEN 内部自相矛盾**：system prompt 说 "Do NOT wrap the action in any tags"，但每轮 user content 中的 FORMAT_PROMPT 说 `Always output: <think> [Your thoughts] </think> <answer> [your answer] </answer>`。模型收到两个相互矛盾的指令。

**来源**:
- SFT eval: `scripts/eval_exp021.py` 行 15-28 硬编码 SYSTEM_PROMPT
- RAGEN: `RAGEN/config/envs.yaml` 中 `AlfworldSG.env_instruction`
- FORMAT_PROMPT: `RAGEN/ragen/llm_agent/ctx_manager.py` `_build_format_prompt()` 方法

### 差异 2: User Content 格式完全不同 [严重]

**SFT eval** 每轮 user message:
```
-= Welcome to TextWorld, ALFRED! =- ...
Admissible actions: [go to desk 1, pick up pen 2, ...]
```

**RAGEN** 每轮 user message:
```
Turn 3:
State:
-= Welcome to TextWorld, ALFRED! =- ...
Admissible actions: [go to desk 1, pick up pen 2, ...]
You have 27 actions left. Always output: <think> [Your thoughts] </think> <answer> [your answer] </answer>. Max response length: 512 words (tokens).
```

SFT 模型在训练时见过的是裸格式，没见过 `Turn N:`、`You have X actions left`、FORMAT_PROMPT 等附加信息。这些 OOD（out-of-distribution）内容会影响模型的输出分布。

此外，RAGEN 在 turn 之间插入 `Reward:\n{value}\n` 作为 user message，SFT eval 没有这个。

### 差异 3: top_p=0.95 vs 1.0 [中等]

SFT eval 用 top_p=0.95 做 nucleus sampling，裁剪掉最低 5% 概率的 token，使输出更集中。

RAGEN val 用 top_p=1.0（无裁剪），从完整分布采样，增加了采到低概率（可能无效）action 的概率。

**来源**:
- SFT eval: `scripts/eval_exp021.py` 行 `SamplingParams(temperature=0.4, top_p=0.95, ...)`
- RAGEN: `verl/verl/workers/config/rollout.py` `SamplingConfig.top_p` 默认值 1.0，exp023 未覆写 `val_kwargs.top_p`

### 差异 4: max_tokens=256 vs 1024 [低-中等]

SFT eval 限制每次生成 256 tokens，RAGEN 允许 1024。实际上 ALFWorld 每轮响应通常 < 200 tokens，但 1024 的上限意味着模型偶尔可能生成冗长、重复的输出（尤其在 top_p=1.0 下），浪费 token 或产生解析错误。

### 差异 5: Max Prompt Length [低]

SFT eval 允许 30,000 tokens 的 prompt（几乎不截断）。RAGEN 的有效 prompt 限制为 max_model_len(8192) - response_length(1024) = 7,168 tokens，且 agent_proxy.max_prompt_length=4096。

对于长 episode（>10 步），RAGEN 会截断历史，丢失早期上下文。SFT eval 保留更多历史。

### 差异 6: 强制 `<think>` 前缀 [低]

SFT eval 让模型自行决定是否输出 `<think>`。RAGEN 在 prompt 末尾强制添加 `<think>` 前缀。由于 SFT 模型已被训练始终输出 `<think>`，这个差异影响很小。

## 3. 影响分析

| 差异 | 影响程度 | 机制 |
|------|----------|------|
| System prompt 矛盾 | **高** | 模型看到"不要用 tag"和"用 `<answer>` tag"两个矛盾指令，有时输出 bare action（不被 parser 捕获）或格式混乱 |
| User content OOD | **高** | 模型从未在 SFT 中见过 `Turn N:`、FORMAT_PROMPT 等模板，输入分布偏移直接降低输出质量 |
| top_p 1.0 vs 0.95 | **中** | 从完整分布采样增加无效 action 概率，尤其在模型不确定时 |
| max_tokens 1024 | **低-中** | 偶尔导致过长输出，但多数情况不影响 |
| Max prompt length | **低** | 仅在长 episode 中有影响，且 val 只有 16 episodes |
| 强制 `<think>` | **低** | 模型已习惯输出 `<think>` |

**综合判断**：action_is_valid 从 87.5% 降至 68.75% 最可能的原因是 **system prompt 矛盾** + **user content OOD** 的叠加效应。top_p 差异是次要因素。

## 4. 修复方案（给后续实验用，不改 exp023c）

### 方案 A：对齐 RAGEN 的 prompt 到 SFT 训练格式（推荐）

1. **修改 `envs.yaml` 中 AlfworldSG 的 `env_instruction`**：
   - 将 "Do NOT wrap the action in any tags" 改为 "present it within `<answer>...</answer>` tags"
   - 或者直接使用与 SFT eval 相同的 SYSTEM_PROMPT 文本
   
2. **修改 ctx_manager 的 user content 构建**（或创建新的 env config）：
   - 去掉 `Turn N:` 前缀
   - 去掉 `You have X actions left. Always output: ... Max response length: ...` 后缀
   - 只保留裸 observation（与 SFT 训练数据一致）
   - 或者：在 SFT 训练数据中就包含这些 RAGEN 格式

3. **在 exp023 config 中设置 `val_kwargs.top_p: 0.95`**

### 方案 B：对齐 SFT 训练数据到 RAGEN 格式

如果不想改 RAGEN 的 prompt 结构，在 SFT 数据准备阶段就使用 RAGEN 的完整 prompt 格式（包括 Turn N、FORMAT_PROMPT、reward feedback 等）。这需要重新生成 SFT 数据和重新训练。

### 方案 C：最小改动（快速修复）

只修改 sampling 参数，不改 prompt：
1. `val_kwargs.top_p: 0.95`
2. 可选：`response_length: 256`（val 时）

这不解决根本问题（prompt 格式不匹配），但可以部分缩小差距。

### 建议优先级

1. **立即**：下个实验在 YAML 中加 `val_kwargs.top_p: 0.95`
2. **短期**：统一 system prompt 的 `<answer>` tag 指令（AlfworldSG env_instruction 改为与 SFT 训练一致的格式）
3. **中期**：评估是否需要让 ctx_manager 的 user content 也与 SFT 训练格式一致，或反过来在 SFT 数据中使用 RAGEN 格式
