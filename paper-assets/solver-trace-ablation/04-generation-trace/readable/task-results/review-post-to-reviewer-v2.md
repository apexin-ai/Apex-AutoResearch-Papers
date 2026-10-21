# review post to reviewer v2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_post-to-reviewer-v2_20260515T050523_result.json`
- **Structured JSON:** [`eb5e43522e9fe3ed4721.json`](../../sessions/eb/eb5e43522e9fe3ed4721.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Consistency Check Report

### CRITICAL (1)

**Conclusion `conclusion.tex:5` — stale Random β=0.3 number**

> "at $\beta{=}0.3$, PR collapses (18\% vs.\ 48\% random)"

- "18%" = ISR β=0.3 seed-42 (correct per-seed value)
- "48%" = Random β=0.3 seed-42 only — this was the old single-seed number

After the 3-seed update, Random β=0.3 **mean = 54±35%** (Table 1, `experiments.tex:60`). The conclusion still uses the old seed-42-only value (48%) without qualification. Meanwhile `experiments.tex:85` correctly reports the 3-seed mean: "PR=54±35%, spanning 23--92%".

Additionally, comparing single cherry-picked seeds is misleading: ISR 3-seed mean PR (66%) is actually *higher* than Random (54%). The "collapse" framing only holds for s42 specifically, while s44 shows the opposite (ISR 95% vs Random 23%).

**Fix needed:** Update to use 3-seed means, e.g., "at $\beta{=}0.3$, cross-seed instability is extreme (PR $66{\pm}42\%$, Random $54{\pm}35\%$)".

---

### WARNING (1)

**Experiments `experiments.tex:85` — "≤1% non-hacking across all 3 seeds"**

Random β=0.3 per-seed N-H (`appendix.tex:432-434`): s42=0%, s43=**2.2%**, s44=0%. The phrase "≤1% non-hacking across all 3 seeds" implies each seed is ≤1%, but s43 is 2.2%. The **mean** (~0.7%) rounds to ≤1%, so if "across all 3 seeds" means "on average," it's fine. If it means "each seed individually," it's inaccurate.

**Suggested fix:** Change to "${\leq}1\%$ mean non-hacking" or "${\leq}3\%$ non-hacking per seed".

---

### INFO (2)

1. **`appendix.tex:314-315` — tab:fol-detailed only shows β=0.3 seed-42** for both ISR and Random conditions. Seeds 43/44 are in the separate `tab:beta03-detailed`. This is by design but could confuse readers expecting all β=0.3 data in one place.

2. **Abstract vs Table 1 rounding: H7 64.5% vs 65%** — Abstract uses the exact fraction (149/231 = 64.5%, `abstract.tex:7`), Table 1 rounds to 65% (`experiments.tex:56`). Consistent intent, just different precision. No action needed.

---

### Verified Consistent

- Abstract ISR β=0.3 PR 66±42% ✓ matches Table 1
- Abstract/Introduction 99.5% collapse (0.642→0.003) ✓
- Abstract/Introduction/Conclusion 1.06× ✓
- Abstract/Introduction/Conclusion 64.5% vs 0% H7 ✓
- Abstract/Introduction ρ=−0.049 ✓
- SFT 92.9% non-hacking ✓ everywhere
- All `\ref{}`/`\label{}` pairs matched — 0 dangling references
- ISR β=0.3 per-seed numbers in §4.3 match appendix tab:beta03-detailed ✓
- Random β=0.3 Table 1 aggregates match per-seed data ✓

**Summary: 1 CRITICAL, 1 WARNING, 2 INFO.** The critical issue is a stale "48% random" in the conclusion that should reflect the updated 3-seed mean of 54%.

---
