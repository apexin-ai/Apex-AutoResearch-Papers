# code write evaluate mvp

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_write_evaluate_mvp_20260514T142325_result.json`
- **Structured JSON:** [`1508e6fef5182eae4768.json`](../../sessions/15/1508e6fef5182eae4768.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本部署完成，试跑结果：

```
=== MVP Gate Evaluation ===
Input: results/mvp_v4_full.json
Total samples: 80

--- All Samples ---
                        Value   Threshold  Status
C1 disagree_rate        30.0%      >=10%   PASS
C2 diagnostic_rate      87.5%      >=40%   PASS
C3 error_types              5        >=2   PASS
C4 targeted_delta     +22.6pp       >5pp   PASS
C5 localization         45.8%      >=60%   FAIL

MVP Gate: 4/5 PASS -> FAIL

--- Excl. Unknown-GT ---
Excluded: 29 samples (36.2%), Remaining: 51
C1 29.4% PASS | C2 86.7% PASS | C3 4 PASS | C4 +10.0pp PASS | C5 46.7% FAIL

MVP Gate: 4/5 PASS -> FAIL
```

C1-C4 全部通过，唯一未过的是 **C5 localization** (45.8% < 60%)。

---
