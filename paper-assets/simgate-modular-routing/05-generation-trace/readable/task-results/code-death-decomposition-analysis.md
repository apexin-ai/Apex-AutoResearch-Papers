# code death decomposition analysis

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_death-decomposition-analysis_20260513T204749_result.json`
- **Structured JSON:** [`cabe843bbf20791403de.json`](../../sessions/ca/cabe843bbf20791403de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功。关键结果：

- **191 episodes, 24 tasks**
- Aggregate Δ(D-I) = +36.9, 去除 death 后 Δ_nd = +0.3
- **Death avoidance fraction = 99%** — 几乎全部 gap 来自 death avoidance
- Correlation r=0.986, p<0.0001 — death rate diff 与 Δ 高度相关
- Internal death rate 47%, Det death rate 11%
- 标签分布: det-preferred 77, internal-preferred 1, no-preference 113
- Signal source: death_asymmetry 36.1%, both_dead 11.0%, score_comparison 4.7%, tied_alive 48.2%

JSON 报告和 paper table 数据已保存。脚本功能完整，输出格式正确。

---
