# code attention steering gen mode upgrade

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_attention_steering_gen_mode_upgrade_20260520T095913_result.json`
- **Structured JSON:** [`c86a80fe5b385b43114f.json`](../../sessions/c8/c86a80fe5b385b43114f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**修改摘要：**

**文件：** `/root/turn_residual_gating/src/eval_attention_steering.py`

**新增函数：**
- `load_gen_data_from_file(path, max_convs=None)` — 从外部 JSON 加载对话，返回 `(sys_prompt, user_questions)` 元组列表。无 system message 时回退到 "You are a helpful assistant."

**新增参数：**
- `--data-file PATH` — 外部对话 JSON（gen 模式使用，覆盖 hardcoded prompts）
- `--max-convs N` — 限制从 data-file 读取的最大对话数（默认全部）

**修改点：**
1. `n_convs` 计算逻辑 — 提供 `--data-file` 时从文件确定对话数，否则保持原有 hardcoded 5 个
2. gen loop — `gen_data is not None` 时从外部数据取 `sys_prompt`/`user_qs`，否则走原有 `SYSTEM_PROMPTS[i]`/`CONVERSATIONS_DATA[i]`
3. 输出 metadata `conversations_source` — 记录实际数据来源

**向后兼容：** 不提供 `--data-file` 时行为完全不变。tf 模式逻辑未触碰。

**数据格式确认：** eval_200.json 是标准 ChatML 格式（200 个对话，avg 3.1 user turns，无 system message），兼容良好。

**内存估算：** 200 convs × avg 3 turns × ~100 tokens/turn 生成 ≈ 每个 β 值约 1h GPU 时间（greedy decoding），VRAM 与现有 5-conv 相同（逐条处理，无 batch）。

---
