# code standard conversations gen

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_standard_conversations_gen_20260519T011352_result.json`
- **Structured JSON:** [`0f526d1b1707b43860bc.json`](../../sessions/0f/0f526d1b1707b43860bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已就绪，无需重新生成。

**结果汇报：**

| 对话 | System Prompt | Turn 数 | 约 words | 截断 |
|------|--------------|---------|---------|------|
| 0 | Science tutor | 10 | 845 | 否 |
| 1 | Code reviewer | 10 | 837 | 否 |
| 2 | Creative writing coach | 10 | 841 | 否 |
| 3 | Math problem solver | 10 | 817 | 否 |
| 4 | Debate coach | 10 | 833 | 否 |

- **5 组对话，每组 10 轮 assistant turn，均无截断**
- **总计 ~4173 words**
- 文件路径：`/root/turn_residual_gating/data/standard_conversations.json`
- 脚本已部署：`/root/turn_residual_gating/src/generate_standard_conversations.py`（新版添加了 `conversation_id` 字段，如需重新生成可用）

旧文件结构缺少 `conversation_id` 字段，但 `system_prompt` / `messages` / `num_turns` 齐全，后续 eval 使用 `--conversations-path` 指向该文件即可公平对比三种模型。

---
