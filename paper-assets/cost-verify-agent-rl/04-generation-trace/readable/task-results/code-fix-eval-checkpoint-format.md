# code fix eval checkpoint format

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_eval_checkpoint_format_20260515T185336_result.json`
- **Structured JSON:** [`c8f09eec15da80503311.json`](../../sessions/c8/c8f09eec15da80503311.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结改了什么：

**修复的三个格式不匹配问题：**

1. **System prompt 前缀** — 添加 `"You're a helpful assistant. "` 前缀（`_build_system_content` 格式）。原来直接用 env_instruction 作为 system prompt，现在 `SYSTEM_PROMPT = "You're a helpful assistant. " + ENV_INSTRUCTION`。

2. **User message 格式** — 从多轮对话（raw obs 作 user message）改为单轮 step_independent 格式，完全复刻 `AlfWorldMemory.build_user_content()`：
   - `Your task is to: {task}.`
   - `Prior to this step, you have already taken N step(s).`
   - 最近 5 步的紧凑历史 `[Observation N: '...', Action N: '...']`
   - 当前 observation（清理掉 welcome message、格式指令等 boilerplate）
   - 当前 admissible actions
   - 格式指令 + actions_left + length_prompt

3. **Answer 标签对齐** — 用户消息中的格式指令改为 `"Output your reasoning in &lt;think>...&lt;/think> tags, then output exactly one admissible action command directly after &lt;/think>. Do not use &lt;answer> tags."` —— 与 AlfWorldMemory 一致。`parse_action` 保留对 `&lt;answer>` 和裸文本两种格式的解析（兼容模型可能输出的任一格式）。

**辅助改动：**
- 新增 `clean_observation`、`extract_task`、`extract_admissible_actions`、`extract_action_from_response`、`build_user_content` 函数（均从 AlfWorldMemory 复刻）
- `run_episode` 从多轮 messages 追加改为每步重建单轮 `[system, user]` 消息
- `max_tokens` 从 256 改为 1024（匹配 GRPO config 的 `response_length: 1024`）
- 备份存在于 `eval_checkpoint.py.bak`

---
