# fix d134 analysis prefixes

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_d134-analysis-prefixes_20260518T134949_result.json`
- **Structured JSON:** [`112084b48d75b4609359.json`](../../sessions/11/112084b48d75b4609359.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Script works. Results:

**Discovery:** 6 runs found (4 ISR, 2 RANDOM)
| Source | Condition | Seed |
|---|---|---|
| `d134_4b_isr_b01_s47/classify.json` | ISR | 47 |
| `d134_4b_isr_b01_s48/classify.json` | ISR | 48 |
| `d134_4b_isr_b01_s49/classify.json` | ISR | 49 |
| `plan002_..._s42_1000_taxonomy_unified.json` | ISR | 42 |
| `plan018_additive_random_b01_s44_r2/taxonomy.json` | RANDOM | 44 |
| `plan018_random_s42_taxonomy_verification.json` | RANDOM | 42 |

**Condition stats:**
- ISR (n=4): H7 rate 91.8±7.7%, Genuine 1.3±1.3%
- RANDOM (n=2): H7 rate 0.0±0.0%, Genuine 11.0±6.0%

**Statistical tests all run:**
- Fisher H7 domination: p=0.067
- Mann-Whitney H7: U=8.0, p=0.050
- Permutation genuine: p=1.000 (RANDOM genuine > ISR, as expected)

Both local and remote copies are updated. Note that `d134_4b_isr_b01_s50` was skipped (no classify.json, only train.log) and `plan002_additive_b01_s45_1000` was skipped (no classify.json or taxonomy.json in that directory).

---
