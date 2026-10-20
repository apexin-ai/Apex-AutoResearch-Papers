# analysis bayesian rope

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bayesian-rope_20260522T170114_result.json`
- **Structured JSON:** [`84be6d1ac80d650b2a56.json`](../../sessions/84/84be6d1ac80d650b2a56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果摘要：**

| 对比 | P(ROPE) | 95% HDI | 结论 |
|------|---------|---------|------|
| CLS–CWM (per-test) | **0.975** | [+0.10, +2.00] pp | 等价性成立 |
| CLS–TRAJ (per-test) | **0.542** | [+0.35, +3.52] pp | 不确定 |
| CLS–TRAJ (variant) | **0.970** | [−2.00, +1.03] pp | 等价性成立 |

与 TOST 完全一致：CLS–CWM 等价性在两种范式下都确认（TOST p=0.007, P(ROPE)=0.975）；CLS–TRAJ per-test 水平两种方法都不确定（TOST Holm 修正后 p=0.075, P(ROPE)=0.542），variant 水平等价性成立。

**产出：**
- 服务器脚本：`/home/sonny/exec-sim-repair-verifier/bayesian_rope.py`
- 服务器结果 JSON：`artifacts/bayesian_rope_results.json`
- 本地报告：`artifacts/bayesian_rope_report.md`（含论文可用段落和 Kruschke 2013/2018 引用）

---
