# analysis rankme extraction

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rankme_extraction_20260523T042329_result.json`
- **Structured JSON:** [`da8f6ae71b9aebab4707.json`](../../sessions/da/da8f6ae71b9aebab4707.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Written to `artifacts/plan_018/rankme_trajectory_analysis.md`.

**Core finding: r_eff shows a 2-type phase diagram, not the 3-type SLV structure.**

- **r=0** — peak at Gen 2 (496), then monotonic decline to 438. Matches SLV Type I (collapse).
- **r=0.2** — monotonic increase 418→509. **No dip.** Does NOT match SLV Type II — indistinguishable from Type III.
- **r=0.25/0.3/0.5** — monotonic increase, differing only in rate (higher r → faster expansion).

The Type II/III boundary that SLV captures (transient dip at r=0.2) is invisible to r_eff. This reinforces SLV's superiority as an early warning signal — it detects transient spectral stress that RankMe misses entirely. r_eff only distinguishes "collapse" from "no collapse."

---
