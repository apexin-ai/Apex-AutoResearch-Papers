# code plan 011 rule based baseline

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-011-rule-based-baseline_20260514T041427_result.json`
- **Structured JSON:** [`efbcdbfdc4fdf5880441.json`](../../sessions/ef/efbcdbfdc4fdf5880441.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本和 CSV 输出均正常。

**结果摘要：**

| 指标 | 值 |
|------|-----|
| 总 episodes | 254,889 |
| 可评分 (排除 tie) | 107,312 |
| Keyword match rate | 42.1% |
| Overall accuracy | 50.0% |

v3 关键词 match rate 42.1%（被 `lifespan-longest-lived` 的 254k episodes 主导），accuracy 50.0% — 本质等于随机，符合预期的"关键词 heuristic 结构性失效"结论。

**产出文件：**
- 本地脚本：`src/analysis/rule_based_routing.py`
- 本地关键词：`src/rule_based_keywords.json`（v3，9 个词）
- 服务器 dry-run CSV：`/tmp/rule_based_comparison.csv`

---
