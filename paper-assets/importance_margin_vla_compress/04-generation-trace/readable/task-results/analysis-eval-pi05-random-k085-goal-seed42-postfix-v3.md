# analysis eval pi05 random k085 goal seed42 postfix v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_random_k085_goal_seed42_postfix_v3_20260525T095349_result.json`
- **Structured JSON:** [`96279f3476ab220a4c63.json`](../../sessions/96/96279f3476ab220a4c63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (success)。

## 结果报告

### Overall
**SR = 53.0% (265/500)** | Δ baseline = **-43.4pp** (vs 96.4%) | 耗时 139.3 min

### Per-task Breakdown

| Task | Description | SR | Successes |
|------|------------|-----|-----------|
| T0 | open the middle drawer of the cabinet | 84% | 42/50 |
| T1 | put the bowl on the stove | 2% | 1/50 |
| T2 | put the wine bottle on top of the cabinet | 18% | 9/50 |
| T3 | open the top drawer and put the bowl in | 34% | 17/50 |
| T4 | put the bowl on top of the cabinet | 54% | 27/50 |
| T5 | push the plate to the front of the stove | 76% | 38/50 |
| T6 | put the cream cheese in the bowl | 82% | 41/50 |
| T7 | turn on the stove | 88% | 44/50 |
| T8 | put the bowl on the plate | 84% | 42/50 |
| T9 | put the wine bottle on the rack | 8% | 4/50 |

### 历史一致性对比

| Run | SR | Successes |
|-----|-----|-----------|
| random k=0.85 Goal postfix (original) | 52.8% | 264/500 |
| random k=0.85 Goal v3 (non-postfix) | 52.4% | 262/500 |
| random k=0.85 Goal v4 | 52.4% | 262/500 |
| random k=0.85 Goal seed43 postfix | 53.4% | 267/500 |
| **本次 (v3 postfix)** | **53.0%** | **265/500** |

### Conclusion: **SUCCESS**

本次 53.0% 落在历史 5 次运行的 [52.4%, 53.4%] 区间内，方差极小 (σ ≈ 0.4pp)，确认 random k=0.85 Goal 性能稳定在 ~52-53%。无异常或错误，进程正常退出 (EXIT_CODE=0)。

---
