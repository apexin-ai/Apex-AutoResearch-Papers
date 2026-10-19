# diagnose eval vs ragen diff

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-vs-ragen-diff_20260514T222025_result.json`
- **Structured JSON:** [`eec9f35eac6a070a0732.json`](../../sessions/ee/eec9f35eac6a070a0732.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the code needed for a complete analysis. Here's the comprehensive comparison:

---

## 1. System Prompt 对比

### eval_sft_fast.py
```python
SYSTEM_PROMPT = (
    "You're a helpful assistant. You are an expert agent in the ALFRED Embodied Environment.\n"
    "Complete household tasks by navigating and interacting with objects.\n\n"
    "Before each action, you MUST first produce a self-guidance assessment:\n"
    "[Assessment: positive/neutral/negative] - evaluate your current progress.\n"
    "[Reasoning: one sentence analyzing what has been accomplished and what remains.]\n"
    "[Suggestion: the best next action from admissible actions.]\n\n"
    "Your reasoning with self-guidance MUST be enclosed within &lt;think> &lt;/think> tags.\n"
    "Then choose an admissible action and present it within &lt;answer>...&lt;/answer> tags."
)
```

### SFT 训练 (sft_train_v2.py)
训练数据中 messages 数组自带 system prompt，模板为标准 ChatML (`SIMPLE_CHATML`)。模型学到的输出格式是 `&lt;think>...&lt;/think>&lt;answer>action&lt;/answer>`。

### RAGEN (AlfworldSG config → `_build_system_content`)
```
"You're a helpful assistant. You are an expert agent in the ALFRED Embodied Environment.
Complete household tasks by navigating and interacting with objects.

Before each action, you MUST first produce a self-guidance assessment in your reasoning:
[Assessment: positive/neutral/negative] - evaluate your current progress toward the task goal.
[Reasoning: one sentence analyzing what has been accomplished and what remains.]
[Suggestion: the best next action from admissible actions.]

Your reasoning MUST be enclosed within &lt;think> &lt;/think> tags.
After the closing &lt;/think> tag, output EXACTLY ONE admissible action command directly.
The action must be a precise ALFWorld command from the admissible actions list
(e.g. go to desk 1, pick up pen 2, open drawer 1).
Do NOT wrap the action in any tags. Do NOT output natural language descriptions
or anything after the action.

Example: &lt;think>[Assessment: neutral] I need to find a pen. The desk is a likely
location. [Suggestion: go to desk 1]&lt;/think>go to desk 1"
```

**关键差异**: eval_sft_fast.py 说 "present it within `&lt;answer>...&lt;/answer>` tags"，RAGEN 说 "Do NOT wrap the action in any tags" 且示例是 `&lt;/think>go to desk 1`（无 `&lt;answer>` 标签）。

---

## 2. User Message / Observation 格式对比

### eval_sft_fast.py
直接把 env 返回的原始 observation 作为 user message，多轮对话结构：
```
system: [system prompt]
user: "-= Welcome to TextWorld, ALFRED! =-\nYou are in the middle of a room...\n\nAdmissible actions: [go to desk 1, go to shelf 1, ...]"
assistant: "&lt;think>...&lt;/think>&lt;answer>go to desk 1&lt;/answer>"
user: "On the desk 1, you see a lamp 1...\n\nAdmissible actions: [...]"
assistant: "..."
```

### RAGEN (`_build_infer_multi_turn_messages` + `_build_turn_state_content`)
`context_window_mode: full` 下，每个 turn 的 user content 是：
```python
content = f"\nTurn {turn_number}:\n"
content += (
    f"State:\n{turn['state']}\n{warning}"
    f"You have {turn['actions_left']} actions left. Always output: "
    f"&lt;think> [Your thoughts] &lt;/think> &lt;answer> [your answer] &lt;/answer> "
    f"with no extra text. Strictly follow this format. "
    f"Max response length: 512 words (tokens).\n"
)
```

而且每个 assistant 回复之后，还插入一个 **Reward 消息**：
```python
if "reward" in content:
    messages.append({"role": "user", "content": f"Reward:\n{content['reward']}\n"})
```

多轮对话实际结构：
```
system: [system prompt with "Do NOT wrap the action in any tags"]
user: "\nTurn 1:\nState:\n{obs}\nYou have 30 actions left. Always output: &lt;think>...&lt;/think> &lt;answer>...&lt;/answer>..."
assistant: "..."
user: "Reward:\n0.0\n\nTurn 2:\nState:\n{obs2}\nYou have 29 actions left..."
...
```

**关键差异**:
1. RAGEN 给 observation 加了 "Turn N:" / "State:" / "You have X actions left" / 格式指令的包装
2. RAGEN 在轮次之间插入 "Reward:\n0.0\n" 消息 — SFT 模型从未见过这种模式
3. RAGEN 内部有**自相矛盾**: system prompt 说 "Do NOT wrap the action in any tags"，但 turn-level format prompt 说 "Always output: `&lt;think>...&lt;/think> &lt;answer>...&lt;/answer>`"

---

## 3. Action 解析对比

### eval_sft_fast.py (`parse_action`)
```python
def parse_action(response: str):
    has_think = bool(re.search(r"&lt;think>.*?&lt;/think>", response, re.DOTALL))
    # 主路径: &lt;think>...&lt;/think>\s*&lt;answer>(.*?)&lt;/answer>
    m = re.search(r"&lt;think>.*?&lt;/think>\s*&lt;answer>(.*?)&lt;/answer>", response, re.DOTALL)
    if m:
        return m.group(1).strip(), has_think, True
    # 回退: &lt;/think> 之后的裸文本
    m = re.search(r"&lt;/think>\s*(.*)", response, re.DOTALL)
    if m:
        action = m.group(1).strip().split("\n")[0].strip()
        ...
```

### RAGEN (`get_env_inputs` → `_parse_response`)
```python
# 关键: 先给模型输出加 &lt;think> 前缀
responses = ["&lt;think>" + response for response in responses]

# _parse_response:
pattern = r'&lt;think>(.*?)&lt;/think>\s*&lt;answer>(.*?)&lt;/answer>'
match = re.search(pattern, response, re.DOTALL)
if not match:
    # 回退: Qwen3 native format
    fallback_match = re.search(r'&lt;think>(.*?)&lt;/think>\s*(.*)', response, re.DOTALL)
    if fallback_match:
        action_content = next((line.strip() for line in remaining.split('\n') if line.strip()), '')
        for special_token in self.special_token_list:  # 包含 "&lt;answer>", "&lt;/answer>"
            action_content = action_content.replace(special_token, '').strip()
```

**解析逻辑本身大体等价**——两者都支持 `&lt;answer>` 标签和裸文本回退。RAGEN 额外在 `special_token_list` 中包含了 `&lt;answer>`/`&lt;/answer>`，能在回退路径中清理掉这些标签。

---

## 4. 其他差异

| 维度 | eval_sft_fast.py | RAGEN val_before_train |
|------|-----------------|----------------------|
| temperature | **0.1** (近贪心) | **0.4** (较高随机性) |
| max_tokens | 512 | 1024 |
| do_sample | True (但 temp=0.1 接近确定性) | True |
| tokenizer chat_template | 从 checkpoint 加载 (SIMPLE_CHATML) | 从 checkpoint 加载 (SIMPLE_CHATML) |
| env | 直接使用 `AlfredTXTEnv` | 通过 `es_manager` 使用相同的 `AlfredTXTEnv` |
| seed | `episode_idx` | config 中 `seed.val: 123` |
| val episodes | 参数指定 (e.g. 75) | `es_manager.val.env_groups * group_size = 4` |

---

## 最可能的根因（按影响排序）

### 根因 #1: Prompt 格式严重偏移（最主要）

SFT 模型学到的 pattern：
```
system: ...present it within &lt;answer>...&lt;/answer> tags
user: {raw_observation_from_env}
assistant: &lt;think>...&lt;/think>&lt;answer>go to desk 1&lt;/answer>
```

RAGEN 喂给模型的 pattern：
```
system: ...Do NOT wrap the action in any tags...Example: &lt;/think>go to desk 1
user: "\nTurn 1:\nState:\n{obs}\nYou have 30 actions left. Always output: &lt;think>...&lt;/think>&lt;answer>...&lt;/answer>..."
```

模型同时收到三个矛盾指令：
1. SFT 训练数据教它用 `&lt;answer>` 标签
2. System prompt 说 "Do NOT wrap the action in any tags"
3. Turn-level prompt 又说 "Always output: `&lt;think>...&lt;answer>...&lt;/answer>`"

这种矛盾 + observation 的结构化包装（Turn N, State, Reward 消息），远离了 SFT 训练分布，导致模型输出严重退化。

### 根因 #2: Reward 消息污染上下文

RAGEN 在每个 assistant 回复后插入 `"Reward:\n0.0\n"` 作为 user 消息。SFT 模型从未在训练中见过这种 pattern。随着对话进行，这些陌生的 reward 消息累积，进一步破坏模型的上下文理解。

### 根因 #3: Temperature 差异

Temperature 0.4 vs 0.1。在模型已经因 prompt mismatch 而不确定的情况下，更高的 temperature 放大了格式崩塌的概率。单独影响有限，但叠加根因 #1 会雪上加霜。

### 验证建议

最快的验证方式：修改 RAGEN 的 AlfworldSG `env_instruction` 使其与 eval_sft_fast.py 的 SYSTEM_PROMPT 完全一致（使用 `&lt;answer>` 标签指令），并将 val temperature 降到 0.1，跑一次 val_before_train 看 action_is_valid 是否恢复。

---
