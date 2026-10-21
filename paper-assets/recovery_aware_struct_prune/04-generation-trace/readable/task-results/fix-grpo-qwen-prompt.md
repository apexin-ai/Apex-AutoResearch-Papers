# fix grpo qwen prompt

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_grpo_qwen_prompt_20260522T064053_result.json`
- **Structured JSON:** [`be5e73859b838ed0667c.json`](../../sessions/be/be5e73859b838ed0667c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整 `prepare_dataset` 也通过验证。

```
== Fix 1: Chat template ==
修改位置: line 168-176 (prepare_dataset 内 format_prompt)
修改内容: 新增 is_qwen 检测（line 168），format_prompt 中对 Qwen 模型用 tokenizer.apply_chat_template 包装 prompt，非 Qwen 保持原逻辑

== Fix 2: System prompt ==
修改位置: line 172-175
修改内容: Qwen 分支的 messages 中注入 system prompt "Please reason step by step, and put your final answer within \boxed{}."

== 验证 ==
Dry-run: PASS
Sample prompt: <|im_start|>system\nPlease reason step by step, and put your final answer within \\boxed{}.<|im_end|>\n<|im_start|>user\nMimi picked up 2 dozen seashells...
Contains chat template: yes
Contains system prompt: yes

== 文件同步 ==
本地: 已修改
westb: 已修改
一致性: 确认
```

---
