# code rule based accuracy analysis

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rule-based-accuracy-analysis_20260513T204923_result.json`
- **Structured JSON:** [`504e67d42064d5321913.json`](../../sessions/50/504e67d42064d5321913.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。结果：

- **Overall accuracy: 97.4%** (75/77 scorable episodes)，但这是因为 `connect`/`disconnect` 关键词匹配了几乎所有 action（3662 次命中），导致 keyword router 几乎总是预测 `det-preferred`
- **Avg keyword match rate: 85.8%** — 严重偏高
- **Precision for det-preferred 仅 40.8%** — 184/189 episodes 被预测为 det-preferred，其中 108 个实际是 no-preference
- 数据集中只有 1 个 `internal-preferred` episode（find-non-living-thing），keyword router 也把它分错了
- Top keyword: `connect`(3662), `activate`(238), `freeze`(36), `mix`(2)

核心发现：`connect`/`disconnect` 是 ScienceWorld 中几乎每步都用的通用动作，把它们作为 "route to simulator" 关键词导致 keyword router 退化为 "always det-preferred" baseline，基本无区分能力。

脚本已写入 `src/rule_based_accuracy.py`，报告已生成到 `results/rule_based_accuracy_test.json`。

---
