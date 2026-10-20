# data wildchat real benign

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_wildchat-real-benign_20260517T232114_result.json`
- **Structured JSON:** [`300a585df4d2e836e490.json`](../../sessions/30/300a585df4d2e836e490.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了（末尾的 PyGILState 错误是无害的 cleanup 警告）。

**关键结果：TF-IDF F1 = 0.9980 — WildChat benign 对 Crescendo jailbreak 仍然几乎完美可分。**

但值得注意的是，top features 已经不再是明显的 artifact，而是 stop words 级别的分布差异（"like", "what if", "just", "how" → jailbreak; "the", "is", "as", "and" → benign）。这说明区分不再是由于 LLM 生成痕迹，而是 Crescendo 对话本身有独特的语用模式（大量使用口语化探测性表达 "what if", "like", "just"）。

统计摘要：

| 指标 | 值 |
|------|-----|
| WildChat 扫描量 | 63,563 |
| 过滤后候选 | 2,000 |
| 采样量 | 250 |
| 过滤原因：< 4 user turns | 48,112 (75.7%) |
| 过滤原因：非英语 | 9,199 (14.5%) |
| 过滤原因：长度/jailbreak/ascii | 4,252 (6.7%) |
| 平均 user turns | 6.8 |
| Min/Max user turns | 4 / 28 |
| 平均 user turn 词数 | 93.0 |
| **TF-IDF Macro F1** | **0.9980** |

**Top TF-IDF features 分析：**
- Jailbreak 侧：`like`, `what if`, `just`, `how`, `what`, `if`, `it`, `ve`, `really`, `you` — 口语化、试探性表达
- Benign 侧：`the`, `is`, `as`, `and`, `an`, `will`, `of`, `write`, `which`, `in` — 正式/指令性表达

虽然 F1 仍然很高，但 confound 性质已从 LLM-artifact（之前 TF-IDF=1.0 with topic keywords）变为 **pragmatic register difference**（Crescendo 的社交工程式口语 vs WildChat 的任务导向正式表达）。这个 confound 可能在 BERT 层面可以被模型学到有意义的信号，因为这些 pragmatic cues 本身就是说服策略的特征。

---
