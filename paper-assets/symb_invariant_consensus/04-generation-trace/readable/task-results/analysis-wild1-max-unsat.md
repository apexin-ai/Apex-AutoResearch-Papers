# analysis wild1 max unsat

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wild1-max-unsat_20260520T072215_result.json`
- **Structured JSON:** [`4a2b1076509565305c40.json`](../../sessions/4a/4a2b1076509565305c40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

```
Method                        Acc      N   Δ vs SC   Δ vs MAXSAT
──────────────────────────────────────────────────────────────────
SC (majority vote)           54.4%   111     ---         ---
MAX-SAT (current SICA)       55.9%   114   +1.5pp       ---
MIN-UNSAT-raw                49.5%   101   -4.9pp      -6.4pp
MIN-UNSAT-weighted           49.0%   100   -5.4pp      -6.9pp
MAX-SAT-discrim-only         55.9%   114   +1.5pp      +0.0pp

Trivially satisfied: 371/7767 (4.8%)
```

**MIN-UNSAT 假设被否定。** 核心原因：MAX-SAT solver 每个问题平均只排除 1.3 条约束（80/204 题排除数为 0）。信号太弱——65/204 题所有候选答案 MIN-UNSAT 得分相同（退化为 SC），剩余有差异的情况中也倾向于选错。

去除 trivially satisfied 约束也无效——实际只有 4.8%（非假设的 43%），对分数排序零影响。

注意：re-run MAX-SAT（55.9%）低于原始 SICA（59.3%），因 z3 dedup 顺序敏感性导致 15/204 题约束集略有差异。各方法间的相对比较在同一约束集上，是公平的。

服务器结果：`/root/symb_invariant_consensus/results/wild1_max_unsat/results.json`
本地 artifact：已注册为 `art_20260520_7451a6`

---
