# paper p0 2 5 statistics phase2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_p0-2-5-statistics-phase2_20260528T053501_result.json`
- **Structured JSON:** [`1eabcfba67a40019c964.json`](../../sessions/1e/1eabcfba67a40019c964.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits applied, all paper_switch.py templates verified. Here's the summary:

---

## Changes Made

### claim3.tex (lines 34–41 added)

| Line | Change |
|------|--------|
| 34–35 | **NEW** `\paragraph{Robustness to null construction.}` — Reports Null A (LoRA-only, p_two=0.300) and Null B (p_two=0.131), both non-significant |
| 37–38 | **NEW** `\paragraph{Statistical power.}` — MDE ≈ 5.0 pp at 80% power; observed effect ~2.3 pp is underpowered |
| 40–41 | **NEW** `\paragraph{Evaluation-seed consistency.}` — References Appendix J (+1.5/+2.5/+5.5 pp, σ=0.9 vs 2.0), concludes with cautious "cannot be resolved at current sample size" |

### appendix.tex

| Line | Change |
|------|--------|
| 180–181 | **NEW** `\paragraph{Alternative null construction (Null~A).}` — Exact p-values for λ=0.1 (p_two=0.300) and λ=0.01 (p_two=0.400) under Null A; also λ=0.01 under Null B (p_two=0.262) |
| 183 | **MODIFIED** Phase 2 ablation: 57.5% → 58.0%, "steps 5K–30K" → "steps 5K–18K", added "at the 18K checkpoint (13K steps of Phase~2 training)" + footnote about disk constraints |

---

## Managed Blocks Requiring Your Attention (flagged, not modified)

These contain absolute wording ("redundant", "no measurable benefit", etc.) or the 57.5% value, but are managed by paper_switch.py:

1. **claim3.tex L7** (caption): "SDF adds no measurable CAR beyond LoRA-only across the full tested range"
2. **claim3.tex L26** (body): "Adding SDF supervision produces no measurable benefit across the full tested range" + "confirming that SDF gradients produce no lasting behavioral effect" + **"CAR\,=\,57.5\%"** (Phase 2, needs → 58.0%)
3. **claim3.tex L32** (dose-response): "SDF supervision is redundant with the demonstration signal across the full tested range"
4. **claim3.tex L46** (fig caption): "confirming full redundancy of EE-only SDF supervision"

All four need updating in `paper_switch.py`'s `old` and `new` templates (both Scenario B and C) to:
- Replace absolute wording with cautious phrasing
- Change `57.5\%` → `58.0\%` with the 18K checkpoint note

---
