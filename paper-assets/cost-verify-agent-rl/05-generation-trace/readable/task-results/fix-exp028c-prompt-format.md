# fix exp028c prompt format

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp028c_prompt_format_20260516T032327_result.json`
- **Structured JSON:** [`8cfa5df475c66a6c9dac.json`](../../sessions/8c/8cfa5df475c66a6c9dac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。总结：

**修改了 2 个文件，4 处代码：**

1. **`RAGEN/config/envs.yaml`** — AlfworldSG、AlfworldSG_Dense、AlfworldSG_SuccessGated 三个变体的 env_instruction：示例和指令从 bare action 改为 `&lt;answer>` tag 格式
2. **`RAGEN/ragen/llm_agent/memory/alfworld_memory.py`** — build_user_content 不再硬编码 "Do not use \&lt;answer\> tags"，改用传入的 format_prompt 参数

现在 system prompt、user content、_build_format_prompt、_parse_response 四处全部统一为 `&lt;think>...&lt;/think>&lt;answer>...&lt;/answer>` 格式。

**当前训练不受影响**，PID 824675 启动时已将旧配置加载到内存，需重启才能使用新格式。

---
