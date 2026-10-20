# Seed Label Correction: results.tex Diff Summary

**Reason:** Registry confirms exp\_008d uses `seed=1` (per `experimental_setup.md`: "All primary conditions use seed 1"). All "s0"/"Seed 0" labels for 008d (and derived runs 008f, 009e) were incorrect and have been corrected to "s1"/"Seed 1".

## Changes

| # | Location | Line | Before | After |
|---|----------|------|--------|-------|
| 1 | Table 1 (008d row) | 27 | `Factorial (s0)` | `Factorial (s1)` |
| 2 | Table 1 (008f row) | 32 | `No dt\_emb (s0)` | `No dt\_emb (s1)` |
| 3 | Post-CIVO paragraph | 91 | `two independent seeds (s0, s2)` | `two independent seeds (s1, s2)` |
| 4 | Post-CIVO table caption | 99 | `Seeds 0 and 2 are independent` | `Seeds 1 and 2 are independent runs; 009e extends seed~1 (008d) from 55K to 105K` |
| 5 | Post-CIVO table body | 107 | `s0 (008d)` | `s1 (008d)` |
| 6 | Post-CIVO table body | 109 | `s1 (009e)` | `s1 ext (009e)` |
| 7 | Text paragraph | 114 | `Seed 0 (008d):` | `Seed 1 (008d):` |
| 8 | Text paragraph | 118 | `Seed 1 (009e):` | `Seed 1 extended (009e):` |

## Verification

- Grep for `s0`, `seed 0`, `Seed 0` in results.tex: **0 matches** (no residual references).
- All 8 affected locations updated consistently.
- No other sections reference 008d/008f/009e seed labels, so no further changes needed.

## Sign-off Status

Pending Reviewer sign-off.
