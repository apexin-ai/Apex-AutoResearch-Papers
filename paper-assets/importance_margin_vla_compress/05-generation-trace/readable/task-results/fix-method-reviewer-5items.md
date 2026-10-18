# fix method reviewer 5items

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_method_reviewer_5items_20260528T180655_result.json`
- **Structured JSON:** [`fc961db7f630572c0f0b.json`](../../sessions/fc/fc961db7f630572c0f0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All remaining hits are either in non-compiled files (analysis.tex, results_v2.tex, results.tex) or are descriptive prose without Δ notation. Compiled files are now consistent.

---

**Summary of all changes:**

### Fix 1: Δ direction unified to L2 − Random (4 files)
- **method.tex:95** — `Δ(Random − L2) decreases monotonically` → `Δ(L2 − Random) increases monotonically`
- **experiments.tex:91** — `Δ(R−L2) = +36.0, +27.2` → `Δ(L2−R) = −36.0, −27.2`
- **appendix.tex:823-837** — Table header + caption + all 5 Δ values flipped (R−L2 → L2−R)
- **appendix.tex:760** — Inline Δ values flipped, "random-over-L2 advantage grows as CV decreases" → "L2-over-random advantage grows as CV increases"

### Fix 2: k=0.75 added + 0.85 de-duplicated
- **method.tex:72** — Base set: `{0.30, 0.50, 0.70, 0.85, 0.90, 0.95}` → `{0.30, 0.50, 0.70, 0.75, 0.85, 0.90, 0.95}`
- **method.tex:72** — Refined set: `{0.80, 0.85, 0.925}` → `{0.80, 0.925}` (0.85 already in base)
- **experiments.tex:9** — Same k set updated to include 0.75

### Fix 3: π0.5 cameras corrected
- **method.tex:9** — `768 tokens from three cameras` → `768 tokens from three image slots (two active cameras in LIBERO`
- Verified via [HuggingFace config](https://huggingface.co/lerobot/pi05_libero_base): model has 2 image inputs + 1 empty slot = 3 image processing slots = 768 tokens

### Fix 4: VTR section expanded
- **method.tex:103-109** — Added architecture paragraph (2-layer cross-attention, 12 heads, dropout 0.1), training paragraph (end-to-end joint optimization), and `Appendix~\ref{app:smart_compress_details}` pointer

### Fix 5: SmolVLA params unified to 450M
- **appendix.tex:599** — `451.5M` → `450M`
- **appendix.tex:859** — `451.5M` → `450M`
- **background.tex:12** — `451.5M` → `450M`
- 450M is the dominant convention in all active compiled files (method, experiments, introduction, appendix table)

---
