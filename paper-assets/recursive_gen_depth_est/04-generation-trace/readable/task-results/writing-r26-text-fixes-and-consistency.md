# writing r26 text fixes and consistency

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_r26-text-fixes-and-consistency_20260515T232957_result.json`
- **Structured JSON:** [`a335af575f76e448a085.json`](../../sessions/a3/a335af575f76e448a085.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Summary:

### Priority 1 — Already fixed (no changes needed)
1. **Forward selection count** (atlas.tex:58): Already `p90_ppl 6/9, var_surprisal 3/9` ✓
2. **SHAP-permutation ρ** (generalization.tex:119): Already `0.830`, no `0.839` anywhere ✓
3. **"other categories"** (atlas.tex:56): Already `${\leq}$47\%` ✓

### Priority 2 — Changes made

**4. Abstract/atlas var_surprisal 8/9 consistency:**
- `atlas.tex:47` — Changed `7/9 (8/9 under SHAP)` → `8/9 under SHAP (7/9 under Gini)` — now SHAP-primary, matching abstract (8/9) and discussion (8/9 under SHAP)
- `atlas.tex:67` (Table 3 caption) — Same change

**5. "Feature Universality" stale references:**
- Only in `main.aux` (auto-generated LaTeX auxiliary file), no .tex source references. Will resolve on next compile. No fix needed.

**6. SHAP ρ cross-file consistency:**
- `generalization.tex:119` — Changed SHAP–Gini from `0.931` → `0.93` to match `section_appendix.tex:18` (`0.93`)
- SHAP–permutation: `0.830` in generalization.tex, `0.83` in appendix — consistent (precision difference only)
- Gini–permutation: `0.76` only in appendix — no conflict
- All three pairs now consistent across both files: SHAP-Gini 0.93, SHAP-permutation 0.830/0.83, Gini-permutation 0.76 ✓

---
