# analysis long conv data check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_long_conv_data_check_20260524T081500_result.json`
- **Structured JSON:** [`215b00a78813233dafef.json`](../../sessions/21/215b00a78813233dafef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Turn 分布总览

| 数据集 | 条数 | Turn范围 | 均值 | >10 turns | >8 turns |
|--------|------|----------|------|-----------|----------|
| eval_200.json | 200 | 2-7 | 3.1 | 0 | 0 |
| ultrachat_eval_heldout.json | 50 | 5-7 | 5.5 | 0 | 0 |
| ultrachat_eval_sample.json | 50 | 5-7 | 5.8 | 0 | 0 |
| ultrachat_eval_20.json | 20 | 5-7 | 5.8 | 0 | 0 |
| ultrachat_8k (训练集) | 8000 | 5-7 | 5.6 | 0 | 0 |
| standard_conversations.json | 5 | 10 | 10.0 | 0 | 5 |

### 结论

**现有数据中 0 条对话超过 10 turns。** UltraChat 200k 本身经过过滤，上限就是 7 turns。`standard_conversations.json` 有 5 条 10-turn 对话，但数量远不够。

**plan_030 无法用现有数据执行。** 需要从外部获取长对话数据。

### 建议数据源

1. **LMSYS-Chat-1M** (`lmsys/lmsys-chat-1m`) — 真实用户多轮对话，大量 >10 turns 样本，最适合 plan_030 "exposure bias gap worsens with conversation length" 的验证目标
2. **WildChat** (`allenai/WildChat-1M`) — 真实 ChatGPT 对话，turn 数分布广
3. **ShareGPT** — 社区分享的对话，长对话比例高
4. **合成拼接** — 将现有 UltraChat 对话 concatenate 成长对话（但可能引入不自然的 topic shift，不推荐作为首选）

下一步需要决定用哪个数据源，然后筛选 >10 turns 的对话做 eval subset。

---
