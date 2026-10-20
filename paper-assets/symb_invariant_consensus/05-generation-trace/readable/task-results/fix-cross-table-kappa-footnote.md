# fix cross table kappa footnote

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cross-table-kappa-footnote_20260524T074516_result.json`
- **Structured JSON:** [`1dbf30f32114d74a6868.json`](../../sessions/1d/1dbf30f32114d74a6868.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

L678 is in `tab:kappa_generalization` with K=10 — same situation as the diagnosis.tex table the user warned about. This is a K=10 result, not K=12, so correctly left unchanged.

L765 (0.447) is a cosine similarity value, unrelated to κ.

Compilation succeeded (29 pages, no errors).

---

**All modifications in appendix.tex:**

| Location | Old | New |
|---|---|---|
| L726 prose | `Mistral-7B ($\kappa = 0.44$)` | `Mistral-7B ($\kappa = 0.46$)` |
| L726 prose | `$\Delta\kappa = 0.03$` | `$\Delta\kappa = 0.05$` |
| L726 prose | `$\Delta\kappa$ up to 0.22` | `$\Delta\kappa$ up to 0.20` |
| L739 tab:cross_model_kappa | `0.44 & 2.02 & 56.86` | `0.46 & 1.98 & 55.88` |
| L703 tab:independence | `0.91 &` | `0.91$^{\dag}$ &` (Qwen3 think) |
| L707 tab:independence | `0.66 &` | `0.66$^{\dag}$ &` (Qwen2.5-7B) |
| L709 tab:independence | `0.53 &` | `0.53$^{\dag}$ &` (Mistral T=0.3) |
| L710 tab:independence | `0.52 &` | `0.52$^{\dag}$ &` (Mistral T=0.5) |
| L712 tab:independence | `0.48 &` | `0.48$^{\dag}$ &` (Mistral T=1.0) |
| L697 caption | (end) | added `$^{\dag}$\,$\kappa$ computed in an earlier pipeline run...` |

**Not changed** (correct):
- L678 `tab:kappa_generalization`: Mistral-7B SC κ=0.44 at K=10 — different experiment, left as-is
- diagnosis.tex — not touched per instructions

**Derived values also fixed**: Δκ 0.03→0.05 and Δκ 0.22→0.20 in the prose paragraph, since they were computed from the old 0.44 value.

Compilation passed, 29 pages, no errors.

---
