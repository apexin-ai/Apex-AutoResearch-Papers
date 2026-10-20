# analysis exp b complexity bin

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-b-complexity-bin_20260519T030027_result.json`
- **Structured JSON:** [`9b1facc3ddd52546f007.json`](../../sessions/9b/9b1facc3ddd52546f007.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs saved. Here's the summary:

## Results

**Bin Distribution** (48 variants, 9784 tests total):

| Bin | #Variants | #Tests |
|-----|-----------|--------|
| 23-70 | 12 | 538 |
| 71-150 | 14 | 1,282 |
| 151-250 | 15 | 2,999 |
| 251+ | 7 | 4,965 |

**Variant-Level Accuracy by Bin (best CLS vs best CWM):**

| Bin | CLS (Qwen3-8B s123) | CLS (DS v5 ckpt-2105) | CWM (Qwen3-8B s42) | CLS-CWM Gap |
|-----|-----|-----|-----|-----|
| 23-70 | 10/12 = 83.3% | 11/12 = 91.7% | 8/12 = 66.7% | +16.7pp |
| 71-150 | 9/14 = 64.3% | 10/14 = 71.4% | 6/14 = 42.9% | +21.4pp |
| 151-250 | 14/15 = 93.3% | 12/15 = 80.0% | 8/15 = 53.3% | +40.0pp |
| 251+ | 6/7 = 85.7% | 6/7 = 85.7% | 3/7 = 42.9% | +42.9pp |
| **Overall** | **39/48 = 81.2%** | **39/48 = 81.2%** | **25/48 = 52.1%** | **+29.2pp** |

**Key Finding:** The CLS-CWM gap **widens dramatically with complexity**: +16.7pp for simple variants (23-70 tests) to +42.9pp for complex variants (251+ tests). CLS maintains 85%+ variant-level accuracy across all complexity tiers, while CWM degrades to near-random (42.9%) for high-test-count variants.

**TRAJ Status:** Per-variant predictions not saved in eval files. Only aggregate results available (DeepSeek TRAJ s42: 81.25%, Qwen3-8B: 70.83%). Per-bin TRAJ breakdown requires GPU re-inference.

**Outputs:**
- `artifacts/complexity_bin_analysis.json` (structured results)
- `artifacts/complexity_bin_analysis.pdf` / `.png` (bar chart)

---
