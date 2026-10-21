# diagnose multiseed mistral pw

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_multiseed-mistral-pw_20260522T232552_result.json`
- **Structured JSON:** [`1d735bbab55ac9e49490.json`](../../sessions/1d/1d735bbab55ac9e49490.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**exp-multi-seed-mistral-pw 诊断结果：**

| Seed | SC (%) | SICA (%) | Δ (pp) |
|------|--------|----------|--------|
| 42   | 40.00  | 36.67    | -3.33  |
| 123  | 40.83  | 37.50    | -3.33  |
| 456  | 39.83  | 38.67    | -1.17  |
| 789  | 38.83  | 37.17    | -1.67  |
| **Mean±SD** | **39.87±0.82** | **37.50±0.85** | **-2.38±1.12** |

- 4/4 seeds 600/600 完整，4/4 seeds Δ≤0
- Registry → DONE(success)，metrics 已更新含 mean/sd
- Cron `exp-multi-seed-mistral-pw` 已删除

---
