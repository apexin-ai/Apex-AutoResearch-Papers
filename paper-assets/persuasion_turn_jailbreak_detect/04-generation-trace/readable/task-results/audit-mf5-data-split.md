# audit mf5 data split

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_mf5-data-split_20260518T192403_result.json`
- **Structured JSON:** [`7c4902f3afae684479d4.json`](../../sessions/7c/7c4902f3afae684479d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete table:

---

| Dataset | Split | Jailbreak | Benign | Total | Benign Source | Turns |
|---------|-------|-----------|--------|-------|---------------|-------|
| Crescendo | Train | 175 | 175 | 350 | Synthetic (Qwen3-8B topic-anchored) | Multi (avg 16.3, range 10–24) |
| Crescendo | Val | 37 | 37 | 74 | Synthetic (Qwen3-8B topic-anchored) | Multi |
| Crescendo | Test (IID) | 38 | 38 | 76 | Synthetic (Qwen3-8B topic-anchored) | Multi (avg 16.6, range 10–24) |
| DD | OOD | 80 | 38 | 118 | plan_002 test split benign | Multi (avg 16.1, range 12–20) |
| FITD | OOD | 80 | 38 | 118 | plan_002 test split benign | Multi (avg 15.5, range 12–20) |
| ActorAttack | OOD | 80 | 38 | 118 | plan_002 test split benign | Multi (avg 10.3, range 6–16) |
| ToxicChat | Ext | 204 | 204 | 408 | ToxicChat dataset itself (LMSYS) | Single (1 user + 1 assistant) |
| verazuo | Ext | 666 | 213 | 879 | plan_002 benign first-turns (**LEAKED**) | Single (user query only) |

**关键发现：**

1. **OOD benign 来源统一**：DD、FITD、ActorAttack 三个 OOD 数据集的 38 个 benign 都来自 `plan_002_splits/test.jsonl` 的 benign 部分。这意味着 OOD 评估中 benign 与 IID test 的 benign 完全相同。代码确认：`plan_006_cross_attack_eval.py:160`、`exp6_actorattack_perturbation.py:172`、`exp7_tfidf_perprefix.py:77`。

2. **verazuo benign 泄漏确认**：213 个 benign 是 plan_002 benign 多轮对话的第一轮 user turn 提取（ID 格式 `plan002_bn_XXX`）。内容匹配检查显示 115 个独特的首轮内容全部能在 plan_002 的 train/test/val 中找到对应，其中大量来自 train split（102/115 前缀匹配 train）。总 plan_002 benign 250 个，verazuo 用了其中 213 个。

3. **ToxicChat 无泄漏**：jailbreak 和 benign 全部来自 ToxicChat 数据集本身（source: `toxicchat-human`），与训练数据无重叠。

---
