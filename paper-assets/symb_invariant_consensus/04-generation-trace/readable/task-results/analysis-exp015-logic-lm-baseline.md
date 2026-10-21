# analysis exp015 logic lm baseline

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp015-logic-lm-baseline_20260517T113121_result.json`
- **Structured JSON:** [`05ef7d0938d9dd9f44f2.json`](../../sessions/05/05ef7d0938d9dd9f44f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

```
============================================================
LOGIC-LM BASELINE (n=204, FOLIO)
============================================================
SICA:          60.8% (124/204)
Logic-LM vote: 62.7% (128/204)
SC:            63.2% (129/204)
============================================================
McNemar SICA vs Logic-LM:  p=0.4240
McNemar Logic-LM vs SC:    p=1.0000
McNemar SICA vs SC:        p=0.2668
============================================================
Logic-LM stats:
  Fallback to SC: 0/204 problems
  Total verified traces: 2109
  Total failed traces: 219
  Verification rate: 90.6%
  Elapsed: 2.3s
```

关键发现：
- **Logic-LM ≈ SC**（p=1.0），单 trace 自洽验证几乎不提供额外判别力
- 90.6% 的 traces 通过自洽检查，因为单条 trace 的约束很少自相矛盾
- 矛盾主要发生在**跨 trace** 之间，这正是 SICA 的 MaxSAT 聚合所捕获的
- Soft weighting（weight_fail=0.5）也只把 Logic-LM 提到和 SC 持平

数据说明：使用 exp020（FOLIO 204 题），因为只有 exp020 保存了 `raw_constraints` 含 `source_traces` 映射，能做真正的 per-trace Z3 验证。exp-001 的 `raw_constraints` 字段为空。

结果已保存到 `/root/symb_invariant_consensus/results/exp015_logic_lm/exp015_results.json`。

---
