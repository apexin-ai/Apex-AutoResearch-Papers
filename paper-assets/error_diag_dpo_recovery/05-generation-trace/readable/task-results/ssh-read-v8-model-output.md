# ssh read v8 model output

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_read-v8-model-output_20260513T073436_result.json`
- **Structured JSON:** [`59e7a9502a6d570a63a8.json`](../../sessions/59/59e7a9502a6d570a63a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 1. v8 assistant 消息内容

第一条轨迹（task_id=0, pick_clean_then_place, reward=False, steps=40）：

```
assistant[3]: 'Thought: The task is to put a clean potato in the microwave. I need to find a potato first...\nAction: go to fridge 1'
assistant[5]: 'Thought: I've reached the fridge. To find a potato...\nAction: open fridge 1'
...
assistant[17]: 'Thought: The microwave is open, but there's an apple inside...I will proceed with placing the potato in...\nAction: put potato 1 in/on microwave 1'
```

- 是否以 `&lt;think>` 开头：**否** — 格式正确，全部是 `Thought:` + `Action:`
- 是否有 `&lt;/think>`：**否**
- 是否有 `Thought:`/`Action:` 格式：**是**，每条都正确
- 模型是否重复同样的 action：**否**

**关键发现**：msg[18] 环境注入了一个**全新任务**（"clean some soapbar and put it in toilet"），模型在完成 potato 任务后被切换到新任务。40 步耗尽，整体 reward=False。

## 2. enable_thinking 支持

tokenizer 参数列表：`['conversation', 'tools', 'documents', 'chat_template', 'add_generation_prompt', 'continue_final_message', 'tokenize', 'padding', 'truncation', 'max_length', 'return_tensors', 'return_dict', 'return_assistant_tokens_mask', 'tokenizer_kwargs', 'kwargs']`

enable_thinking 支持：**否** — 代码第 245 行 `enable_thinking=False` 会触发 TypeError，被 except 捕获后 fallback 到无该参数的调用。**无害但无效。**

## 3. generate 参数

| 参数 | 值 |
|------|-----|
| temperature | 0.5（CLI default，代码 default 0.7） |
| top_p | 0.9 |
| max_new_tokens | 256 |
| do_sample | True（temperature > 0） |
| pad_token_id | tokenizer.pad_token_id or eos_token_id |
| repetition_penalty | 未设置 |

## 4. v7 vs v8 对比

| 指标 | v7 | v8 |
|------|-----|-----|
| success/total | 7/138 (5.1%) | 1/25 (4.0%) |
| avg steps | 38.6 | 38.6 |
| max steps | 40 | 40 |

v7 第一条轨迹和 v8 **完全一致**（同 task_id=0，同任务，同消息内容）。两版本行为基本相同。

## 根因判断

**不是 thinking mode 泄露问题。** 模型输出格式完全正确。

真正的问题是**多任务串行 + 步数不够**：
- 模型 ~18 步完成第一个任务（potato→microwave），环境立刻注入第二个任务（soapbar→toilet）
- 40 步上限不够完成两个任务，导致 reward=False
- 几乎所有轨迹都跑满 40 步（avg=38.6），说明步数上限是瓶颈

---
