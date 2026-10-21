# ssh 72b death rate analysis

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_72b-death-rate-analysis_20260517T213329_result.json`
- **Structured JSON:** [`7730e350681dce03eec5.json`](../../sessions/77/7730e350681dce03eec5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已写入 `artifacts/72b_death_rate_analysis.md`。

**核心数据**：

| 指标 | 值 |
|------|-----|
| 72B Aggregate Death Rate | **33.3%** (72/216) |
| 95% CI (bootstrap) | **[26.9%, 40.3%]** |
| vs 7B (42.9%) | **-9.6pp** |
| vs deterministic (16.3%) | **+17.0pp** |

**数据完整性**：10/11 tasks 已有 ≥20 episodes。measure-melting-point 目前只有 16 eps，缺 4。

**Per-task 极端值**：chemistry-mix 最高 (50%)，find-non-living-thing 为 0%。

**结论**：72B scaling 将 death rate 从 42.9% 降到 33.3%，有改善但远未解决问题，95% CI 完全在 deterministic baseline (16.3%) 之上。

---
