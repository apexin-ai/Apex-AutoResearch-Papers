# debug kirr diagnosis

**turn hier kv compress** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_kirr_diagnosis_20260513T105706_result.json`
- **Structured JSON:** [`3818162f50e1af6c748d.json`](../../sessions/38/3818162f50e1af6c748d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full diagnostic output. Here's my analysis:

---

## Diagnosis: TurnKV KIRR < Uniform EA — Root Cause

### Not a Bug — It's a Methodological Problem

The code correctly implements the design. The issue is in the **multiplicative modulation mechanism itself**.

### Primary Root Cause: Multiplicative Budget Suppression

The formula `modulated_score = ea_score × B_final` systematically starves non-SYSTEM_PROMPT segments. The data across all 3 traces shows a consistent pattern:

**Budget vs Token Share (layer 16):**

| Trace | SYSTEM_PROMPT Tokens | SYSTEM_PROMPT Budget Share | Effective Multiplier |
|-------|---------------------|---------------------------|---------------------|
| 001   | 31.1%               | 44.2%                     | 0.94               |
| 002   | 38.8%               | 52.7%                     | 0.98               |
| 003   | 33.1%               | 51.3%                     | 1.00               |

SYSTEM_PROMPT takes 44-53% of the retention budget despite being only 31-39% of tokens.

**Modulation ratios show the damage to non-system segments:**

| Segment Type         | mod/ea ratio (typical) | Effect                        |
|---------------------|------------------------|-------------------------------|
| SYSTEM_PROMPT       | 0.94 – 1.00           | Scores barely touched         |
| USER_MESSAGE        | 0.65 – 0.88           | Mild suppression              |
| TOOL_RESULT (old)   | **0.40 – 0.57**       | **40-60% of score destroyed** |
| ASSISTANT_MESSAGE   | **0.37 – 0.61**       | **40-63% of score destroyed** |
| THINKING_TRACE      | **0.30 – 0.37**       | **63-70% of score destroyed** |

### How This Kills KIRR

**Retention shift (all-layers avg, Trace 001):**
- SYSTEM_PROMPT: EA 26.5% → TKV 40.7% **(+14.2pp)**
- TOOL_RESULT t=0 (169 tokens): EA 11.8% → TKV 4.7% **(-7.1pp)**
- TOOL_RESULT t=1 (73 tokens): EA 21.9% → TKV 2.7% **(-19.2pp)**

**Planted info that TurnKV kills:**
- `$1,091.58` in TOOL_RESULT: EA retains 17% of tokens → TKV retains **0%** (Δ=−17%)
- `$351.46` in TOOL_RESULT: both 0% (even EA fails here)
- TOOL_RESULT planted info in Trace 003 (`0.9474`, `3.96`): both EA and TKV at 0%

TurnKV helps SYSTEM_PROMPT planted info (+0 to +22%) but **destroys TOOL_RESULT planted info**. Since 40-60% of planted info lives outside SYSTEM_PROMPT, the net KIRR drops.

### EASS Modulation Amplifies the Problem

The z-scored EASS reinforces the structural bias instead of correcting it:
- SYSTEM_PROMPT tends to have higher mean EA scores → positive z → B_final ≥ B_prior
- TOOL_RESULT/ASSISTANT tend to have lower mean EA scores → negative z → **B_final ≪ B_prior**

Example from Trace 001: TOOL_RESULT t=0 has B_prior=0.80 but B_final=**0.3965** (EASS pulled it down 50%).

### Trace 002 Edge Case: max_turn=0

All segments at turn 0 → no recency differentiation. THINKING_TRACE gets Bp=0.40, Bf=0.30 → retention crashes from EA 32.4% to TKV **5.4%** (−27pp).

### Structural Issues Summary

1. **Multiplicative modulation is zero-sum in the wrong direction**: B_prior < 1.0 suppresses scores; SYSTEM_PROMPT (B_prior=1.0) is the only segment that doesn't lose. All other segments compete at a 20-60% disadvantage.

2. **"Budget" doesn't mean "budget"**: B_final=0.4 doesn't mean "keep 40% of this segment." It means "multiply all scores by 0.4," making them lose in the global top-k competition against segments with higher budgets.

3. **No minimum retention guarantee**: A segment can be nearly fully evicted if its B_final is low enough relative to others.

4. **Z-scoring with N=10-15 segments is unstable**: One outlier segment shifts all z-scores.

### Recommendations

1. **Normalize budgets to mean 1.0** — `B_final / mean(B_final)` redistributes instead of suppresses
2. **Or use additive modulation** — `ea_score + offset(budget)` preserves cross-segment ranking
3. **Raise TOOL_RESULT B_prior** — 0.8 is too low under multiplicative modulation; should be 0.95+
4. **Add per-segment minimum retention floor** — guarantee each segment keeps at least k% of tokens

---
