# code plan 011 rule based

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-011-rule-based_20260514T004303_result.json`
- **Structured JSON:** [`950990be0ec68cbec918.json`](../../sessions/95/950990be0ec68cbec918.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都运行正常。结果完美验证了 D014 的预测：

**v3 keywords 结果**：
- 匹配率仅 **2.8%**（接近 v2 的 4.9%）
- Episode routing accuracy **1.5%**（1/66）——几乎所有 episode 都被路由到 internal
- KeywordRouter 模拟分数 = **-53.7** ≈ always-internal（-53.7），vs always-det（-7.7）
- **关键词路由器完全退化为 always-internal**，因为 match_rate 几乎不会超过 0.5 threshold

已创建/更新的文件：
- `src/rule_based_keywords_v3.json` — D014 v3 关键词（12 个科学动词，排除通用交互词）
- `src/rule_based_accuracy.py` — 增加 step-level P/R/F1、`--threshold`/`--strategy` 参数、v3 默认
- `src/rule_based_inference.py` — 新建，score simulation + baseline 对比

---
