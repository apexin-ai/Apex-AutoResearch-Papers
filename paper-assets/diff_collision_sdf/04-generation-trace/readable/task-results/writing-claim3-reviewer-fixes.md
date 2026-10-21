# writing claim3 reviewer fixes

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_claim3_reviewer_fixes_20260527T082858_result.json`
- **Structured JSON:** [`0934b40abf50d4864c43.json`](../../sessions/09/0934b40abf50d4864c43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Verified:

- **28.5%** only remains in `archive/analysis_claim1.tex` (old archive, not active paper) — all active files cleaned.
- **"single seed"** now appears in claim3.tex (footnote), discussion.tex, and appendix.tex.
- **"null distribution"** now appears in claim3.tex line 35 (the z-score fix).

## Summary of changes

| File | Issue | Change |
|---|---|---|
| `abstract.tex` L7 | Pi0.5 CAR inconsistency | 28.5% → 26.8% |
| `claim1.tex` L19 | Table CAR_f mismatch | CAR_f 28.5 → 26.8 |
| `claim1.tex` L3 | Text/table mismatch | "57 safe episodes...28.5%" → "every safe episode exceeds 200mm...26.8% ± 1.6" |
| `claim3.tex` L35 | z-score reference wrong | "against the curve mean" → "against the null distribution; Appendix" |
| `claim3.tex` L27 | Phase 2 single seed | Added `\footnote{Single seed (s2)...}` after 57.5% |
| `appendix.tex` L119 | Phase 2 single seed | Added "(single seed, s2)" after 57.5% |
| `discussion.tex` L8 | Phase 2 single seed | Added "single seed" parenthetical after 57.5% |

**Provenance**: 26.8% ± 1.6 = mean of `eval_pi05_safelibero_object_v11` (28.0%), `_s1` (25.0%), `_s2` (27.5%). z = (60.5 − 54.5)/2.15 = 2.79 against null (5 seeds pooled from LoRA-only + λ=0.005, mean=54.5, σ=2.15). Phase 2 ablation from `eval_phase2_lambda0_s2` (seed 2 only).

---
