# W5: LP ρ Cross-Table Audit

## Background

SciERC LP ρ was reported as 0.205 (mean_LP definition). Decision D132 proposed switching to max_LP, which would change the value to 0.215. This audit checks whether all LP ρ occurrences in the paper are consistent.

## Method

Searched all `.tex` files in `docs/paper/sections/` for patterns: `.205`, `.215`, `0.205`, `0.215`.

## Findings

**0.215 occurrences: 0** (not present anywhere in the paper)

**0.205 occurrences: 11 locations, all consistent with mean_LP definition**

### experiments.tex

| Line | Context | Value | Consistent? |
|------|---------|-------|-------------|
| 40 | Table 1 (tab:quality_estimation): LP row, SciERC ρ | .205 | Yes |
| 48 | Text: "over LP ($0.205$)" | 0.205 | Yes |
| 109 | Table tab:fewnerd: SciERC LP ρ column | .205 | Yes |

### appendix.tex

| Line | Context | Value | Consistent? |
|------|---------|-------|-------------|
| 49 | Table tab:robustness: LP T=1.0 NER ρ | 0.205 | Yes |
| 77 | Text: temperature comparison "vs. $0.205$ at $T{=}1.0$" | 0.205 | Yes |
| 78 | Text: signal hierarchy "$0.360{>}0.267{>}0.205$" | 0.205 | Yes |
| 284 | Table (bootstrap CI): LP row, ρ value | +0.205 | Yes |
| 853 | Table: LP N=8 column | 0.205 | Yes |
| 1052 | Table tab:t_degeneracy or epoch table: LP ρ column | 0.205 | Yes |
| 1143 | Table: ρ row comparing LP across configs | 0.205 | Yes |
| 1159 | Text: "VerbConf achieves higher ρ than LP (SciERC: 0.297 vs. 0.205)" | 0.205 | Yes |

## Assessment

All 11 occurrences use the value **0.205** (mean_LP definition). The paper is internally consistent.

**D132 decision (mean_LP → max_LP, 0.205 → 0.215) was NOT applied.** Two possibilities:

1. **D132 was superseded or deferred**: The paper kept mean_LP throughout. This is the current state.
2. **If D132 should be applied**: All 11 locations need updating from 0.205 to 0.215, plus downstream values that depend on LP ρ (e.g., the bootstrap CI for LP, Δρ gaps like the +0.155 gap in line 48).

### Related values that would change if switching to max_LP (0.215):
- Line 48: Δρ gap between VC and LP would change from +0.155 to +0.145 (if VC stays .379)
- Table tab:fewnerd: LP ρ column for SciERC
- Temperature comparison text: Δ from T=0.7 would need recalculation
- Bootstrap CI bounds for LP

## Recommendation

The paper is consistent as-is (mean_LP = 0.205 everywhere). If D132 must be applied, update all 11 locations plus recalculate Δρ values. Verify with the actual max_LP computation before mass replacement.
