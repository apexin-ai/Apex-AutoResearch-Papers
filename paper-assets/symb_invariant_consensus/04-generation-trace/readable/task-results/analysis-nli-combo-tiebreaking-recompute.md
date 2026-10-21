# analysis nli combo tiebreaking recompute

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nli-combo-tiebreaking-recompute_20260522T151117_result.json`
- **Structured JSON:** [`a8ae1c8fe8734d38bd16.json`](../../sessions/a8/a8ae1c8fe8734d38bd16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Recompute Results

### exp-092 LLaMA-3.1-8B × PW-600
SC baseline: **70.00%** (420/600)

| Weight | Old Combo | New Combo | Old Δ | New Δ | Old p | New p |
|--------|-----------|-----------|-------|-------|-------|-------|
| w=1 | 72.83% | **73.33%** | +2.83 | **+3.33** | 0.0001 | 0.0012 |
| w=3 | 74.17% | **73.33%** | +4.17 | **+3.33** | 0.0035 | 0.0519 |
| w=5 | 71.67% | **72.00%** | +1.67 | **+2.00** | 0.4335 | 0.3846 |

Best new weight: **w=1** (+3.33pp, p=0.0012, significant)

Note: w=3 dropped from 74.17% to 73.33% (lost significance, p=0.0519 borderline). w=1 is now the best and only significant weight.

### exp-091 Qwen2.5-14B × PW-600
SC baseline: **73.50%** (441/600)

| Weight | Old Combo | New Combo | Old Δ | New Δ | Old p | New p |
|--------|-----------|-----------|-------|-------|-------|-------|
| w=1 | 74.17% | **74.17%** | +0.67 | **+0.67** | 0.3438 | 0.3438 |
| w=3 | 74.33% | **74.67%** | +0.83 | **+1.17** | 0.4049 | 0.2295 |
| w=5 | 75.33% | **75.17%** | +1.83 | **+1.67** | 0.1439 | 0.1934 |

Best new weight: **w=5** (+1.67pp, p=0.1934, not significant)

Note: w=1 unchanged (no ties at that weight). w=3 improved slightly (+0.34pp). w=5 dropped slightly (-0.16pp). None reach significance.

Results saved to `artifacts/nli_recompute_exp091_exp092.json` on westd-16639 and registered as `art_20260522_c8ec0c`.

---
