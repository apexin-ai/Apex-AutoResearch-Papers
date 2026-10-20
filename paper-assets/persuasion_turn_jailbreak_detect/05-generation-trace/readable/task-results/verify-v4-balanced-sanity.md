# verify v4 balanced sanity

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_v4-balanced-sanity_20260517T160313_result.json`
- **Structured JSON:** [`d3cb7c3983e17b7f8c3b.json`](../../sessions/d3/d3cb7c3983e17b7f8c3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| Metric | Score | Target | Result |
|--------|-------|--------|--------|
| TF-IDF F1 | 0.924 ± 0.062 | ≤ 0.75 | **FAIL** |
| DeBERTa F1 | 0.789 ± 0.068 | 0.70–0.85 | **PASS** |

**OVERALL: FAIL — need iteration**

DeBERTa 语义层面通过 (0.789)，说明对话内容的语义区分度在合理范围。但 TF-IDF 严重超标 (0.924)，说明 iter2 benign 数据存在明显的词汇/风格 shortcut：

- **Benign 特征词泄露**: `detection`, `training`, `systems`, `model`, `drug`, `handle` — 这些是 topic-level shortcut，benign 对话在讨论技术/专业话题时用了大量领域术语
- **Jailbreak 特征词**: `just`, `hey`, `him`, `trying`, `ve`, `re` — 口语化、非正式语气

结论：v4b iter2 的 benign 数据话题分布与 crescendo jailbreak 差异过大，TF-IDF 能轻松区分。需要进一步迭代，让 benign 对话的话题/词汇分布更接近 jailbreak 的口语化风格。

---
