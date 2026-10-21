# analyze eval obs only object norm01 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-obs-only-object-norm01-seed44_20260516T194412_result.json`
- **Structured JSON:** [`39964ac2fa8a10702db6.json`](../../sessions/39/39964ac2fa8a10702db6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已完成，registry 已更新为 DONE。

## 结果汇总

| 实验 | Overall SR | vs argmin (13%) | 结论 |
|------|-----------|-----------------|------|
| **obs_only norm=0.1 seed44** | **16%** (16/100) | +3pp | **success** |
| **perdof norm=0.1 seed44** | **8%** (8/100) | -5pp | **negative** |

### obs_only norm=0.1 seed44 — 跨 seed 汇总
- seed42: 19%, seed44: 16% → norm=0.1 均正向
- 与 norm=0.2 seed44 (16%) 持平，说明 norm=0.1 vs 0.2 在该 seed 上无差异

### perdof seed44 — 跨 seed 汇总
- seed42: 11%, seed43: 12%, seed44: 8% → 三个 seed 均低于 argmin baseline，且 seed44 最差
- perdof 方案在 object benchmark 上一致性地 negative

---
