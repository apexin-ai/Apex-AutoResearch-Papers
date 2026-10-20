# Appendix Cleanup Scan Report

## 1. Placeholder/Tentative Wording

| Line | Current Text | Issue | Suggested Fix |
|------|-------------|-------|---------------|
| 67 | `\footnote{These majority-voting values were computed from an unverified checkpoint and may differ slightly from the val-best checkpoint results.}` | "unverified checkpoint" + "may differ" — pre-submission hedge that signals unfinished verification | Either verify against val-best checkpoint and update numbers, or remove footnote if difference is negligible |
| 110 | `\cwm{} 4B per-mutation overall accuracy unavailable except gold` | "unavailable" — missing data acknowledged in table caption | Compute the missing values or explicitly state why they cannot be computed (e.g., "not reported due to …") |
| 463 | `Repo-level \cls{}--\traj{} comparison is tentative due to configuration and granularity differences.` | "tentative" — acceptable as scientific qualifier but weakens the claim | Consider replacing with "should be interpreted with caution" or similar phrasing that doesn't sound like the analysis is incomplete |

**Note:** `\tbd{}` appears in **experiments.tex** Table 2 (lines 120–121, CWM columns for Qwen3-8B and DeepSeek-6.7B) but **not** in appendix.tex. The appendix implicitly depends on these missing values (e.g., paragraph (g) references CWM repo-level results).

## 2. Inconsistencies with Main Text

| Item | Main Text Value | Appendix Value | Line | Fix |
|------|----------------|----------------|------|-----|
| Parseable-only accuracy range | **38–43%** (experiments.tex:174, appendix ¶(g):322) | **42–53%** (¶(c):304) | 304 | Inconsistent range. ¶(g) and main text agree on 38–43%. ¶(c) uses 42–53% — if this is the cross-seed range for 4B specifically (seed 42 ≈ 42.88%, seed 123 ≈ 53%?), state the scope explicitly. Otherwise correct to match. |
| CLS–CWM gap under relaxed matching | Standard gap = 25.59pp (experiments.tex:135, 4B s42) | "divergence widens from 26pp to 28pp" (¶(c):304) | 304 | 25.59pp rounds to ~26pp — OK. But "28pp": CLS 83.63% − CWM-relaxed 56.98% = 26.65pp, not 28pp. The 28pp might use seed 123 (83.63 − 55.91 = 27.72 ≈ 28pp), but CLS 83.63% is seed 42 only. Verify computation and clarify which seed(s) the "26→28" refers to. |
| Unparseable rate (8B) | **73.8%** (experiments.tex:160) | **74%** (threats ¶:449) | 449 | Minor rounding: 73.8% vs 74%. Standardize to one value (73.8% preferred as more precise). |
| 19–26pp gap | 19–26pp (experiments.tex:135, conclusion:4) | 19–26pp (threats:457) | — | ✅ Consistent |
| z = −23.7 | experiments.tex:164 | appendix:432 | — | ✅ Consistent |
| Oracle 90.63% | introduction:17, experiments.tex:178 | appendix:292, 298 | — | ✅ Consistent |
| 217× throughput | experiments.tex:176, conclusion:4 | appendix:332 | — | ✅ Consistent |
| ~370 GPU-hours | (main text via git history) | appendix:251 | — | ✅ Consistent |
| TOST p = 0.007 | experiments.tex:98, conclusion:4 | appendix:358, 463 | — | ✅ Consistent |

## 3. Redundancy / Pruning Opportunities

| Section | Lines | Issue | Recommendation |
|---------|-------|-------|----------------|
| ¶(g) Failed interventions | 317–326 | Summarizes four interventions, each already detailed in dedicated sections: rank ablation (§B:44–64), majority voting (§B:66–67), relaxed matching (¶(c):303–304), model scaling (main text §4.4) | Useful as synthesis. **Keep**, but shorten each bullet to 1 line with cross-refs instead of repeating numbers. Currently ~10 lines of near-duplicate data. |
| ¶(h) Per-mutation scaling | 328–329 | Recapitulates Table 8 (§D) and Table 12 (§F) findings narratively | **Keep** as narrative synthesis. No action needed — adds interpretive value over raw tables. |
| Threats §J (full) | 442–457 | Overlaps with main text §5.5 (experiments.tex:180–183). The final paragraph (line 457) repeats "19–26pp exceeds any single assessed confound" verbatim from the main text summary. | Expected: appendix is the full version, main text is the summary. **No pruning needed**, but consider removing the final summary paragraph (lines 457–end) since it's identical to the main text version — readers who reach the appendix have already read it. |
| Oracle §A (lines 36–39) sensitivity paragraph | 38–39 | Speculative paragraph about repo-level ICC yielding "even larger gap" — no quantitative analysis provided, just a qualitative extrapolation | Either compute the repo-level oracle advantage or delete. Currently a soft claim without evidence. |

## Summary

**Critical (fix before submission):**
1. **Line 67**: "unverified checkpoint" footnote on majority-voting numbers — either verify or remove. This is the only item that signals incomplete work to a reviewer.
2. **Line 304**: Parseable-only accuracy "42–53%" contradicts "38–43%" used in ¶(g) and main text. Verify the correct range and make all three locations consistent.
3. **Line 304**: "26pp to 28pp" gap claim — arithmetic doesn't cleanly match (standard gap = 25.59pp, relaxed = 26.65pp for seed 42). Verify computation.

**Minor (nice to fix):**
4. **Line 449**: Standardize unparseable rate to 73.8% (not 74%).
5. **Line 110**: "unavailable" in Table 8 caption — consider rewording to explain *why*.
6. **Lines 317–326**: ¶(g) bullets can be compressed to cross-refs (~5 lines saved).
7. **Line 463**: "tentative" is acceptable hedging but could be reworded.

**No action needed:** All major numerical claims (19–26pp, z = −23.7, oracle 90.63%/95.83%, 217×, ~370 GPU-hours, TOST p = 0.007) are consistent between appendix and main text.
