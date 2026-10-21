# code phase2 eval fixed conversations

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2_eval_fixed_conversations_20260518T065200_result.json`
- **Structured JSON:** [`79257d2b37a718f93a35.json`](../../sessions/79/79257d2b37a718f93a35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

1. **`generate_standard_conversations.py`** (新建) - 用 vanilla Qwen2.5-7B-Instruct 生成 5 组 10-turn 标准对话，`do_sample=False` 确保可复现
2. **`eval_phase2_gar.py`** (修改) - 添加 `--conversations-path` 参数，提供时加载固定对话（`conversations_source: "fixed"`），未提供时保持原有生成逻辑（`"generated"`）。normalized GAR 和 gate loading 逻辑未动
3. **`compare_phase2.py`** (修改) - 加载结果后检查 `conversations_source` 一致性，不一致时打印警告；summary JSON 中增加 `conversations_source` 字段
4. **`standard_conversations.json`** 已生成 - 5 个对话，每个 10 轮，35KB

---
