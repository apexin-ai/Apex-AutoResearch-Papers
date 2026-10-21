# analyze eval pi05 random k05 goal seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k05_goal_seed42_v2_20260524T025508_result.json`
- **Structured JSON:** [`b41adc8db0bac841266f.json`](../../sessions/b4/b41adc8db0bac841266f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果

| 指标 | 值 |
|------|-----|
| **Overall SR** | **73.6%** (368/500) |
| 耗时 | 109.7 min |
| 错误 | 无 (EXIT_CODE=0) |

**Per-task SR**: T0=78%, T1=44%, T2=86%, T3=76%, T4=92%, T5=70%, T6=62%, T7=100%, T8=86%, T9=42%

**Conclusion: success** — 符合单调递减预期：k=0.3 (50.6%) < **k=0.5 (73.6%)** < k=0.7 (78.2%)。与 pre-fix v1 (74.4%) 接近，CPU RNG 修复对 random pruning 影响很小（-0.8pp）。

---
