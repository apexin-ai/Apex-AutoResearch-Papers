# analysis eval pi05 random k085 object seed42 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_random_k085_object_seed42_postfix_20260524T043149_result.json`
- **Structured JSON:** [`0618166ff3c7c3af0be8.json`](../../sessions/06/0618166ff3c7c3af0be8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

## 结果

**Post-fix SR = 5.6%** (28/500) vs Pre-fix SR = 5.0%

Per-task breakdown:

| Task | SR |
|------|-----|
| T0 alphabet soup | 6% |
| T1 cream cheese | 2% |
| T2 salad dressing | 2% |
| T3 bbq sauce | 2% |
| T4 ketchup | 12% |
| T5 tomato sauce | 8% |
| T6 butter | 4% |
| T7 milk | 8% |
| T8 chocolate pudding | 4% |
| T9 orange juice | 8% |

## 结论：**success** — Disruption peak 是真实现象

Post-fix 5.6% 与 pre-fix 5.0% 基本一致（差异在统计噪声范围内），确认 k=0.85 处的 disruption peak 不是 CPU RNG bug 的 artifact，而是 random pruning 的真实行为特征。

完整 post-fix Object Random 曲线：k=0.5=68.2%, k=0.7=74.0%, **k=0.85=5.6%**, k=0.9=9.0%, k=0.95=74.0%。disruption peak 集中在 k=0.85–0.9 区间。

---
