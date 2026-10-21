# data scienceworld consolidate

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_scienceworld-consolidate_20260514T132243_result.json`
- **Structured JSON:** [`1d8b1c696e49f0bccd95.json`](../../sessions/1d/1d8b1c696e49f0bccd95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。ScienceWorld counterfactual 数据已转换为统一格式：

- **输出**: `data/scienceworld-counterfactual/episodes.jsonl` (245 条)
- **摘要**: `data/scienceworld-counterfactual/summary.json`
- **转换脚本**: `src/consolidate_scienceworld.py`

验证结果全部匹配预期：
| 指标 | 值 |
|------|-----|
| Episodes | 245 |
| Tasks | 11 |
| det-preferred | 86 |
| internal-preferred | 9 |
| no-preference | 150 |
| only_int_dies | 70 |
| only_det_dies | 5 |
| both_die | 35 |
| neither_die | 135 |

两种原始数据格式（完整版含 observation/llm_output 和精简版仅含核心字段）均已处理，缺失 observation 的 step 填充为空字符串。

---
