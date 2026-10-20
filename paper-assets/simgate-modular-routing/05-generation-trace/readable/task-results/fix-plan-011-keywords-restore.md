# fix plan 011 keywords restore

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan-011-keywords-restore_20260514T043107_result.json`
- **Structured JSON:** [`d36742ce01f2df313ff4.json`](../../sessions/d3/d36742ce01f2df313ff4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

---

### 文件状态

| 文件 | 状态 | 内容 |
|------|------|------|
| `src/rule_based_keywords.json` | **已恢复为 v1** | 20 keywords（含 connect/disconnect/turn on 等泛用词） |
| `src/rule_based_keywords_v2.json` | **新建** | 17 keywords（去掉 combine 等，加入 ignite/combust/evaporate/condense/oxidize） |
| `src/rule_based_keywords_v3.json` | **新建** | 9 keywords（精简为物理/化学动词） |
| `results/rule_based_accuracy_v3.json` | **新建** | v3 分析完整结果 |

### v3 关键指标

- **Episodes**: 225（11 tasks）
- **Avg keyword match rate**: 6.1%（v1 是 86.1%，v3 大幅去除了 connect 等高频噪声词）
- **Episode accuracy**（excl no-preference）: **23.3%**（20/86 scorable）
- **Step accuracy**: 13.2%
- **Top keyword hits**: activate (296), freeze (93)
- **Per-task accuracy range**: 0%（chemistry-mix, find-animal, grow-fruit）~ 35%（find-non-living-thing）

### 异常标注

`lifespan-longest-lived/episodes.jsonl` 原始文件 844,689 行（8.3GB），远超正常 20 episodes，属损坏文件残留。已截断为前 20 episodes 用于分析，原始文件保留为 `episodes_full_844k.jsonl.bak`。

---
