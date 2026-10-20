# Paper Data Consistency Audit (2026-05-19)

Pre-submission check for EMNLP 2026. Compares paper (`docs/paper/`) against code artifacts and recent experimental updates.

---

## Algorithm 1 Consistency

**Comparison: `profile_classifier.py` vs artifacts `algorithm1_pseudocode.tex` vs paper `method.tex` Algorithm 1**

| Check | Status | Detail |
|-------|--------|--------|
| Δ = a100 − a0 | ✅ | All three sources match |
| m* = min(a5, a25, a50) | ✅ | All three sources match |
| v* = max\|ai − a0\| (volatility check) | ✅ | All three sources match |
| Branch 1: \|Δ\| ≤ τ → Immune (v* ≤ τ) | ✅ | Match |
| Branch 1: \|Δ\| ≤ τ, v* > τ, V-dip → ? | ❌ | **Code returns `V-recovery-full`; artifacts pseudocode returns `V-recovery-full`; paper Algorithm 1 returns `V-recovery`** |
| Branch 1: \|Δ\| ≤ τ, v* > τ, no V-dip → Immune | ✅ | Match |
| Branch 2: Δ < −τ, Δ ≤ −σ → U-collapse | ✅ | Match |
| Branch 2: Δ < −τ, V-dip → V-recovery | ✅ | Match |
| Branch 2: Δ < −τ, no V-dip → U-collapse | ✅ | Match |
| Branch 3: Δ > τ, saturation check | ✅ | g1, g2, ℓ logic identical across all three |
| Branch 3: saturating → Benefit-sat | ✅ | Match |
| Branch 3: not saturating → Benefit | ✅ | Match |
| Default thresholds (τ=1, σ=5, ρ=0.3, λ=0.5) | ✅ | Match |
| Output pattern set | ❌ | **Code/artifacts: 6 patterns (includes `V-recovery-full`). Paper Ensure line (method.tex:68): 5 patterns (no `V-recovery-full`)** |

### Verdict

The paper intentionally merges `V-recovery-full` into `V-recovery`, treating full vs partial recovery as subtypes rather than separate labels. The prose (method.tex:59) describes the distinction: "recovery extent varies by seed (partial at seed=42, full at seed=123)". This is a defensible editorial choice, but creates a mismatch with the implementation.

**Action needed**: Either (a) update the paper Ensure line to include `V-recovery-full` as a 6th pattern, or (b) document explicitly that the paper merges the two subtypes. If keeping 5 patterns in the paper, the code's `V-recovery-full` label should be mentioned in a footnote or appendix to avoid reproducibility confusion.

---

## Sensitivity Description

**Expected state**: v2 sweep with 180 combinations (per task description). **Actual state**: All references say 30 combinations.

| Location | Current Text | Status |
|----------|-------------|--------|
| method.tex:59 | "a 30-combination grid sweep confirms 5/5 families are stable" | ❌ Not updated |
| results.tex:11 (Table 1 caption) | "150/150 model-combination pairs across 30 (τ,σ) combinations" | ❌ Not updated |
| results.tex:27 | "stable across 30 (τ,σ) threshold combinations" | ❌ Not updated |
| appendix.tex:154 | "a grid sweep over 30 (τ, σ) combinations: τ ∈ {0.5, 0.75, 1.0, 1.25, 1.5, 2.0} pp × σ ∈ {3, 4, 5, 6, 7} pp" | ❌ Not updated |
| appendix.tex:158 (Table 7 caption) | "Profile classification stability across 30 (τ, σ) threshold combinations" | ❌ Not updated |
| appendix.tex:164–169 (Table 7 data) | Each model shows "30/30" | ❌ Not updated |

### Verdict

**All 6 locations still reference the v1 30-combination sweep.** None have been updated to reflect the v2 180-combination sweep. The parameter grid description (appendix.tex:154) and all stability counts need updating.

---

## V-recovery Dual-Seed

**Expected**: Paper reflects D165 dual-seed confirmation (s42 partial Δacc=−1.82pp, s123 full Δacc=0.00pp). No stale hedge language.

| Location | Current Text | Status |
|----------|-------------|--------|
| method.tex:59 | "recovery extent varies by seed (partial at seed=42, full at seed=123)" | ✅ Correct |
| results.tex:29–30 | "Qwen-7B (66.1%) shows V-shaped harm-then-recovery under both seeds (trough at d025 for seed=42, d005 for seed=123; recovery extent varies from partial to full)" | ✅ Correct |
| results.tex Table 1 | Qwen-7B Δacc = −1.8pp | ✅ Consistent with s42 −1.82pp (rounded) |
| limitations.tex:9 | **Paragraph heading: "Single seed."** but body says "confirmed across two seeds (s42, s123)" | ⚠️ **Stale heading** |
| limitations.tex:10 | "V-recovery is qualitatively stable: both seeds exhibit a mid-dosage trough followed by recovery, though recovery extent varies (partial at s42, full at s123)" | ✅ Content is correct |
| limitations.tex:10 | "Triple-seed validation with error bars is in progress." | ⚠️ Check if still accurate or if this has been completed |
| abstract.tex:1 | "V-type recovery (−3pp then partial rebound)" | ⚠️ **Only describes s42 partial case; does not mention s123 full recovery** |
| conclusion.tex | No V-recovery detail mentioned | ✅ N/A (no claim made) |
| introduction.tex | No V-recovery detail mentioned | ✅ N/A |

### Verdict

Core method/results sections correctly reflect dual-seed confirmation. Three issues remain:

1. **limitations.tex:9** — Paragraph heading "Single seed." is stale. Should be renamed (e.g., "Seed coverage." or "Two-seed validation.") since the content already describes dual-seed confirmation.
2. **abstract.tex:1** — "V-type recovery (−3pp then partial rebound)" only describes s42. Consider adding "to full rebound" or similar to acknowledge the s123 result.
3. **limitations.tex:10** — "Triple-seed validation with error bars is in progress" — verify if this is still the current status or needs updating.

---

## Summary of Required Changes

| Priority | Item | Files |
|----------|------|-------|
| **P0** | Update sensitivity sweep from 30 → 180 combinations (6 locations) | method.tex, results.tex, appendix.tex |
| **P1** | Fix stale "Single seed." heading in limitations | limitations.tex:9 |
| **P1** | Decide on V-recovery-full: align paper ↔ code (either add 6th pattern to paper or document the merge) | method.tex:68, method.tex:76 |
| **P2** | Abstract only mentions partial rebound for V-recovery | abstract.tex:1 |
| **P2** | Verify "Triple-seed validation in progress" claim | limitations.tex:10 |
