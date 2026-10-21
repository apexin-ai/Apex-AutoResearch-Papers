# code plan 005 analysis prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-005-analysis-prep_20260514T073128_result.json`
- **Structured JSON:** [`a9939b98b94a07de2460.json`](../../sessions/a9/a9939b98b94a07de2460.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已完成，报告已输出到 `results/plan_005_analysis/`。

核心发现：

| 指标 | 值 |
|------|-----|
| oracle 选 det-preferred | 31.4% (61/194) |
| oracle 选 internal-preferred | 3.6% (7/194) |
| no-preference | 65.0% (126/194) |
| **internal 单独死亡 → 100% det-preferred** | 47 episodes |
| **det 单独死亡 → 100% internal-preferred** | 4 episodes |
| 非死亡 episode 中有 preference 的 | 仅 15% |
| 有 preference 的 episode 中 score gap ≥ 100 | 75% |
| trained-router vs oracle agreement | 96.4%（7 个 disagreement 全是 router 选了 det 但 oracle 选 internal） |

结论与项目假设一致：routing signal 绝大部分来自 death avoidance（51/68 有偏好的 episode 是 death_asymmetry 驱动），非死亡 episode 的 score 差异很小。`lifespan-longest-lived` 是 det-preferred 率最高的 task (56%)。

---
