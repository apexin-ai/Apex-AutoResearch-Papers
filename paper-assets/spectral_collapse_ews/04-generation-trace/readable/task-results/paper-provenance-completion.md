# paper provenance completion

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_provenance-completion_20260519T171040_result.json`
- **Structured JSON:** [`425947c10cb1ffb8fc1d.json`](../../sessions/42/425947c10cb1ffb8fc1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass. Summary:

**Coverage: 15/25 → 25/27** (2 new claims added, 10 previously unmapped claims filled)

**Fixes (3):**
- C030, C046, C067: exp_005 (killed) → exp_006 (controller never triggered) + exp_007 (r=0.2 Δ_t=0.0019<τ) + exp_009 (r=0.25 Δ_t=0.00028<τ) + decisions D019/D020/D023

**New claims (2):**
- C070: r_crit ∈ (0.25, 0.3] — evidence: exp_009 (Type II EMA violation) + exp_008 (Type III EMA satisfied), decisions D029/D031
- C071: Three trajectory types — evidence: exp_001 (Type I) + exp_007/exp_009 (Type II) + exp_004/exp_008 (Type III), decisions D028/D029

**Newly mapped existing claims (8):**
- C006/C010: controller rule/params → exp_006
- C015: conditions budget → exp_001/exp_004/exp_006 + D026
- C040: +exp_006 for closed-loop axis
- C047/C049/C052/C056: limitations → relevant experiments
- C061: proportional controller → exp_006 + D020

**Remaining tier3 (2):** C001, C003 — pure math definitions, no experimental evidence needed.

---
