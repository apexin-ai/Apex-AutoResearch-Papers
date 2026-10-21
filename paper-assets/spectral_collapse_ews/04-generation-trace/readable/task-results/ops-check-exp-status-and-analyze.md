# ops check exp status and analyze

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_exp_status_and_analyze_20260520T204203_result.json`
- **Structured JSON:** [`435251a4c876d2b9fabe.json`](../../sessions/43/435251a4c876d2b9fabe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Report Summary

### Experiment Status
- **exp_012** (r=0.3, seed43): Gen 10 generation phase, 8320/35000 (~24%). Est. 3-5 hours remaining.
- **exp_013** (r=0, seed44): Gen 5 training, step 2500. 5 full gens remaining. Est. 15-20+ hours.
- **GPU**: Both GPUs active (74% / 100% util, ~25GB each)

### Key Findings (exp_012 Gen 0-9 complete)

**Cross-seed r=0.3 SLV**: seed43 closely tracks seed42 (max deviation ~11.6 at Gen 8). Mean trajectory: 2366.68 → 2495.37 at Gen 9.

**α Sensitivity — r_crit ∈ (0.25, 0.3] confirmed on cross-seed mean:**

| | r=0 (2-seed) | r=0.25 (1-seed) | r=0.3 (2-seed) |
|--|--|--|--|
| α=0.3 | ❌ t=4 | ❌ t=2 | ✅ |
| α=0.5 | ❌ t=3 | ❌ t=2 | ✅ |
| α=0.7 | ❌ t=3 | ❌ t=2 | ✅ |

**Table 3 interim (Gen 9, 2-seed)**: SLV=2495.37±1.94, eff_rank=516.18±0.27, PPL=12.96±0.00

**Flag**: D-4 has high cross-seed variance — seed43 D-4=0.1833 vs seed42 D-4=0.3732 at Gen 9. Seed43's diversity collapses much faster despite near-identical SLV. Worth discussing.

Full report: `artifacts/exp_012_013_status_report.md`

---
