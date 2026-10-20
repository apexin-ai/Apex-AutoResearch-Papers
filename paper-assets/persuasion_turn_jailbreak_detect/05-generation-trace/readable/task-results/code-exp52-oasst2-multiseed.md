# code exp52 oasst2 multiseed

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp52_oasst2_multiseed_20260522T100929_result.json`
- **Structured JSON:** [`e13486f76c32c8faa203.json`](../../sessions/e1/e13486f76c32c8faa203.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp52 complete. Results:

| Seed | OASST2 FPR | IID F1 | DD F1 | AA F1 | FITD F1 |
|------|-----------|--------|-------|-------|---------|
| 42   | 1.50%     | 1.000  | 1.000 | 0.953 | 1.000   |
| 123  | **0.50%** | 1.000  | 1.000 | 0.917 | 1.000   |
| 456  | 1.00%     | 1.000  | 1.000 | 0.990 | 1.000   |
| **Mean±Std** | **1.0%±0.5%** | 1.000 | 1.000 | 0.953±0.037 | 1.000 |

Multi-seed confirms N=25 OASST2 adaptation is robust — FPR consistently in 0.5-1.5% range across all 3 seeds. IID F1 and most OOD F1 metrics are perfect. Only AA F1 shows minor seed variance (0.917-0.990). Registry updated to DONE/success.

---
