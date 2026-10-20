# research scrambled data investigation

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scrambled-data-investigation_20260518T075257_result.json`
- **Structured JSON:** [`0ff235ff80b874b113d7.json`](../../sessions/0f/0ff235ff80b874b113d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。报告已写入 `artifacts/scrambled_data_investigation.md`。

## 核心结论

**根因：`final_v2` 的 benign 数据（v4c-casual）存在结构性 shortcut。**

| 属性 | v4c benign (final_v2) | topic-anchored benign (plan_002) | jailbreak (crescendo) |
|------|----------------------|----------------------------------|----------------------|
| 对话结构 | **user-only** | user+assistant | user+assistant |
| 有 assistant 轮次 | **0/161** | 175/175 | 175/175 |
| 平均 user 轮数 | **6.5** | 8.1 | 8.3 |
| 平均 user 字符量 | **1086** | 2013 | 1992 |

v4c benign 是纯 user 独白（无 assistant 回复、轮数少、文本短），与 jailbreak 的多轮对话结构差异巨大。GRU 学到的是「短/少轮 = benign」的 shortcut，而非真实 intent 信号。IID 测试 F1=1.0（同分布有效），但遇到结构匹配 jailbreak 的 topic-anchored benign 就全部预测为 benign（F1=0.333）。

**三次实验的真实关系：**
- 原始 plan_003_v2 和 fix 版本都用了 plan_002_splits 数据（topic-anchored benign），DD OOD F1 = 0.98~0.99，结果一致
- retrain 版本误用了 final_v2 数据（v4c benign），0.333 是数据 bug 而非 scrambled control 本身的问题

**对论文：** 使用 plan_003_scrambled_fix 的结果（DD OOD F1=0.990）即可。Scrambled 作为有效 control 成立。

---
