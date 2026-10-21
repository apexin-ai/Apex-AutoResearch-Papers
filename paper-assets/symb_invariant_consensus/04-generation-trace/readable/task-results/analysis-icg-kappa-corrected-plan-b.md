# analysis icg kappa corrected plan b

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_icg-kappa-corrected-plan-b_20260520T015454_result.json`
- **Structured JSON:** [`80e30474126524235bc2.json`](../../sessions/80/80e30474126524235bc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| 指标 | 值 |
|---|---|
| **Fleiss' κ** | **0.4649** |
| **Eff-K** | **1.93** |
| n_raters | 10 |
| n_questions | 204 |
| Answer flip rate | 79.4% (162/204) |
| Non-trace votes | 85 (MAX-SAT 翻转了 trace 答案) |

与其他方法对比：
- **ICG (corrected)**: κ=0.46, Eff-K=1.93
- **ICG (bootstrap, 旧)**: κ=0.72 ← bootstrap overlap 膨胀
- **SC**: κ=0.44, Eff-K=2.02
- **Debate**: κ=0.15, Eff-K=4.44

ICG κ=0.46 与 SC κ=0.44 接近，方法论一致（per-independent-source rater）。85 个 non-trace votes 说明 MAX-SAT 评分不完全退化——约 4.2% 的 rater-question 对中，约束集的 MAX-SAT 结果翻转了原始 trace 答案（因 fallback mode 或约束冲突）。

---
