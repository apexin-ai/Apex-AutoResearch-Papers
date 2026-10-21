# code plan 012 death decomposition prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-012-death-decomposition-prep_20260513T214834_result.json`
- **Structured JSON:** [`7518a1544b6739d546f8.json`](../../sessions/75/7518a1544b6739d546f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量分析完成，脚本运行正常。

## 汇总

**脚本状态**: `death_decomposition.py` (519行) 完整就绪，所有 6 项分析功能均已实现且验证通过。

**全量结果** (30 tasks, 219 episodes from prescreening + MVP):

| 指标 | 值 |
|------|-----|
| Δ_full | +37.9 |
| Δ_nd | +0.2 |
| death_fraction | 99% |
| r (death_rate_diff vs Δ) | 0.989, p<0.0001 |
| Δ_penalty_removed | +0.9 |
| Labels | det-preferred: 89, internal-preferred: 1, no-preference: 129 |
| Internal death rate | 49% |
| Det death rate | 12% |

**与 MVP 初步结果对比**：数据从 5 tasks → 30 tasks，核心结论不变——death avoidance 贡献 99% 的 routing signal，r 从 0.986 微升至 0.989。

**数据目录结构**：prescreening 和 mvp 格式一致，每个 task 子目录含 `episodes.jsonl` + `summary.json`，脚本能直接读取。

**一个小问题**：`aggregate_results()` 函数（~line 185-275）是死代码，`main()` 用的是 `aggregate_from_raw()`。无功能影响，可以清理但非必需。

---
