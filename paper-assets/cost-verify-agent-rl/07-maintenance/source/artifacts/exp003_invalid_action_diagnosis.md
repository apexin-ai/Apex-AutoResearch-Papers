# exp003 Invalid Action 根因诊断报告

## 概要

exp003（ALFWorld GRPO，Qwen3-1.7B base）step 0/1 后 95.3% action 被判 invalid，根因是 **Qwen3-1.7B base 模型不生成 `<answer>` 标签**，导致 RAGEN 的 action 解析正则全部失败。

---

## 1. Invalid Action 原始样本

### 测试条件
- 模型：`/root/cost-verify-agent-rl/models/Qwen3-1.7B`（base，非 instruct）
- 温度：1.0，max_tokens=2048，32 个样本
- Prompt：RAGEN 标准 AlfworldSG 格式（system + user + `<|im_start|>assistant\n<think>`）

### Invalid 样本（32/32 全部 invalid）

**样本 1**（典型模式 — `</think>` 后重复格式指令）：
```
<think>
Okay, let's see. The task is to put a clean cloth on the countertop. Right now, I'm at 
the middle of a room and can see several objects around me. The available actions include 
going to different locations like the bathtub basin, countertop, drawers, garbage can, etc.

First, I need to figure out where the clean cloth is. Since the task is to place it on the 
countertop, the cloth must be somewhere nearby. The initial observation includes a countertop 
1, so maybe I should check if there's a cloth already there.

[Assessment: neutral] - I'm at the starting position and need to locate a clean cloth. The 
task hasn't been started yet.
[Reasoning: I need to find a cloth first by exploring nearby locations.]
[Suggestion: go to countertop 1 to check if there's a cloth there.]
</think>

</think>Your reasoning with self-guidance. [positive] - I'm progressing toward the task by 
moving to the countertop 1 to check if a cloth is already there. The goal is to place a 
clean cloth...
```

**样本 2**（`</think>` 后输出 `<tool_call>`）：
```
<think>
...thinking content...
[Assessment: positive] - I am ready to proceed by checking the surroundings.
[Reasoning: I need to find a clean cloth first.]
[Suggestion: go to countertop 1]
</think>

<tool_call>Your reasoning with self-guidance.assessment: positive - I'm ready to locate a 
clean cloth by checking nearby drawers...
```

**样本 3**（`</think>` 后继续生成自然语言）：
```
<think>
...thinking content...
</think>

</think>Your reasoning with self-guidance. Assessment: positive - I am ready to proceed by 
checking the surroundings for a clean cloth. Reasoning: The task requires placing a clean 
cloth on...
```

### Valid 样本

**32/32 样本中没有任何一个产生 `<answer>` 标签。** 0% 格式合规率。

训练日志中 step 0（val before train）`action_is_valid=0.00125`，意味着在更大的样本量下约有 0.1% 的 action 碰巧匹配了 admissible actions。

---

## 2. Invalid 原因分类

| 原因分类 | 占比 | 说明 |
|---------|------|------|
| **`</think>` 后无 `<answer>` 标签** | **100%** (32/32) | 模型产生 `</think>` 但之后不输出 `<answer>...</answer>`，而是重复格式指令或继续生成自然语言 |
| 缺少 `</think>` | 0% | 2048 tokens 足够让模型产生 `</think>`（1024 tokens 不够时为 100%） |
| `<answer>` 内容不匹配 | N/A | 因为 `<answer>` 标签从未出现，无法评估 |

### 解析失败机制

RAGEN 的 `_parse_response` 使用正则：
```python
pattern = r'<think>(.*?)</think>\s*<answer>(.*?)</answer>'
```

模型输出被预置 `<think>` 前缀后为：
```
<think>...long thinking...\n</think>\n\n</think>Your reasoning...
```

正则匹配到第一个 `</think>` 后寻找 `\s*<answer>`，但实际内容是 `\n\n</think>Your reasoning...`（无 `<answer>`），匹配失败 → `actions = []` → `valid_actions = []` → `manager_invalid_action = True`。

---

## 3. Tokenizer 分析结果

```
<think>  → token_id=151667 (单 token, added_token, 非 special_token)
</think> → token_id=151668 (单 token, added_token, 非 special_token)
<answer>  → token_ids=[27, 9217, 29] (3 tokens, 普通 token 序列)
</answer> → token_ids=[522, 9217, 29] (3 tokens, 普通 token 序列)
```

- `<think>`/`</think>` 是 Qwen3 tokenizer 的 **added_token**（ID 151667/151668），但 **不在 `all_special_tokens` 中**
- `skip_special_tokens=True` **不会剥离** `<think>`/`</think>`（已实验验证）
- `<answer>`/`</answer>` 不是任何特殊 token，由 3 个普通 token 组成

**结论：Tokenizer 不是问题。`<think>`/`</think>` 不会被意外剥离。**

---

## 4. Prompt Template 兼容性分析

### Qwen3 原生 thinking 格式

Qwen3 chat_template 内置了 thinking 模式支持：
```jinja2
{%- if add_generation_prompt %}
    {{- '<|im_start|>assistant\n' }}
    {%- if enable_thinking is defined and enable_thinking is false %}
        {{- '<think>\n\n</think>\n\n' }}  {# 禁用 thinking 时插入空 think 块 #}
    {%- endif %}
{%- endif %}
```

Qwen3 原生 assistant 输出格式：
```
<|im_start|>assistant
<think>
reasoning content
</think>

actual answer text here (无 <answer> 标签!)
<|im_end|>
```

### RAGEN 期望格式
```
<think>reasoning</think><answer>action text</answer>
```

### 不兼容点

| 方面 | Qwen3 原生格式 | RAGEN 期望格式 | 冲突 |
|-----|--------------|--------------|------|
| 思考标签 | `<think>...\n</think>\n\n` | `<think>...</think>` | 格式细微差异 |
| **答案标签** | **无标签，直接文本** | **`<answer>...</answer>`** | **核心冲突！** |
| 换行 | `</think>` 后有 `\n\n` | `</think>` 后紧跟 `<answer>` | 正则可兼容（`\s*`） |

### RAGEN 的 prompt 构建
- `apply_chat_template(messages, add_generation_prompt=True)` → `...<|im_start|>assistant\n`
- RAGEN 没有传 `enable_thinking` 参数
- 手动追加 `<think>` → `...<|im_start|>assistant\n<think>`

**RAGEN 没有利用 Qwen3 的 `enable_thinking` 参数。** 但即使传了也不影响根因，因为 Qwen3 base 模型在 thinking 模式下就是不输出 `<answer>` 标签。

---

## 5. vLLM 生成配置

```yaml
# exp003 配置
rollout:
  response_length: 1024   # max_tokens per turn
  temperature: 1.0
  gpu_memory_utilization: 0.4
  max_model_len: 8192
  enforce_eager: True
```

- **无显式 stop tokens**：SamplingParams 中只有 `max_tokens`, `temperature`, `top_p`, `top_k`
- **EOS token**：`<|im_end|>` (151645)，vLLM 默认会在 EOS 处停止
- **`</think>` 不是 stop token**：模型输出 `</think>` 后不会停止，继续生成到 EOS 或 max_tokens

潜在问题：如果模型在 1024 tokens 内没有产生 `<|im_end|>`，将用完所有 token budget。这导致 response 很长但没有有效 action。

---

## 6. 根因结论

### 主因：Qwen3-1.7B base 模型不生成 `<answer>` 标签

Qwen3 系列模型（包括 base 和 instruct）的 thinking 模式设计为：
- `<think>reasoning</think>` + **直接输出答案文本**（无标签包裹）
- `<answer>` 不在 Qwen3 的预训练数据/对齐数据中

RAGEN 框架要求 `<think>...</think><answer>...</answer>` 格式，这与 Qwen3 的原生格式不兼容。

### 完整因果链

```
Qwen3-1.7B base 不理解 <answer> 标签
  → 模型输出 </think> 后不产生 <answer>，而是继续生成自然语言
    → RAGEN regex <think>(.*?)</think>\s*<answer>(.*?)</answer> 匹配失败
      → actions = [] (空列表)
        → no_manager_action = True
          → manager_invalid_action = 95.3%
            → 几乎所有 turn 的 reward = format_penalty = -0.1
              → pg_loss ≈ 0 (无有效梯度信号)
```

### 对比验证

exp004 配置使用 `Qwen3-1.7B-Instruct`（已确认），说明已识别到 base 模型的问题。Instruct 模型有可能通过 instruction following 产生 `<answer>` 标签，但仍然不是 Qwen3 的原生输出格式。

---

## 7. 修复建议

### 方案 A：修改 `_parse_response` 适配 Qwen3 原生格式（推荐）

```python
def _parse_response(self, response: str) -> List:
    # 先尝试 RAGEN 标准格式
    pattern = r'<think>(.*?)</think>\s*<answer>(.*?)</answer>'
    match = re.search(pattern, response, re.DOTALL)
    if match:
        # 标准格式解析
        ...
    else:
        # Qwen3 兼容：<think>...</think> 后面的文本即为 action
        pattern_qwen3 = r'<think>(.*?)</think>\s*(.*?)$'
        match = re.search(pattern_qwen3, response, re.DOTALL)
        if match:
            think_content = match.group(1)
            action_content = match.group(2).strip()
            actions = [action.strip() for action in action_content.split(self.action_sep) if action.strip()]
            ...
```

**优点**：不改模型，兼容 Qwen3 原生格式  
**缺点**：`</think>` 后的文本可能很长且不是一个有效的 action 字符串，需要额外截断逻辑

### 方案 B：使用 Instruct 模型

使用 `Qwen3-1.7B-Instruct`，其 instruction following 能力更强，更可能按照 `<answer>` 格式输出。但 Qwen3-Instruct 的原生格式仍然不含 `<answer>` 标签，需要验证效果。

### 方案 C：将 `<answer>` 替换为 Qwen3 原生分隔

修改 RAGEN 的 action 提取逻辑，使用 `</think>` 后的第一行文本作为 action：
- Prompt 中不再要求 `<answer>` 标签，改为 "After your reasoning, output exactly one admissible action on a new line"
- `_parse_response` 改为：取 `</think>` 后第一个非空行作为 action

### 方案 D（激进）：SFT warmup

在 GRPO 训练前，先用少量示例对 base 模型做 SFT warmup，教会它输出 `<think>...</think><answer>...</answer>` 格式。这是多数 agent RL 论文的标准做法。

### 建议优先级
1. **D（SFT warmup）**：最可靠，base model 需要先学会格式
2. **A（修改解析器）**：最小改动，短期验证
3. **B（Instruct 模型）**：exp004 已在验证
4. **C（改 prompt）**：需要同步修改 prompt + 解析器，改动面大
