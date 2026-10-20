# 72B Backbone Death Rate — Canonical Audit (2026-05-17)

## Data Source Rules

- **Canonical source**: westb-13313 (used when ≥20 episodes available)
- **Supplement source**: westb-14838 (only for tasks missing/incomplete on 13313)
- Each task: exactly 20 episodes (ep 0-19)
- Death criterion: `internal_final == -100.0`

## Fixes Applied

- **P0**: Removed duplicate ep15 in `measure-melting-point-unknown-substance` on 14838 (supplement line deleted, first-write-wins preserved). File now has exactly 20 lines.

## Per-Task Death Rate Table

| Task | Source | Deaths | Total | DR |
|------|--------|--------|-------|----|
| chemistry-mix | 13313 | 10 | 20 | 50.0% |
| find-animal | 13313 | 8 | 20 | 40.0% |
| find-non-living-thing | 13313 | 0 | 20 | 0.0% |
| freeze | 13313 | 9 | 20 | 45.0% |
| grow-fruit | 13313 | 8 | 20 | 40.0% |
| identify-life-stages-1 | 13313 | 8 | 20 | 40.0% |
| identify-life-stages-2 | 13313 | 6 | 20 | 30.0% |
| inclined-plane-determine-angle | 13313 | 6 | 20 | 30.0% |
| lifespan-longest-lived | 14838 (first 20 of 27) | 5 | 20 | 25.0% |
| lifespan-longest-lived-then-shortest-lived | 14838 | 4 | 20 | 20.0% |
| measure-melting-point-unknown-substance | 14838 (post-fix) | 5 | 20 | 25.0% |

## Aggregate Results

| Metric | Deaths | Total | Rate | 95% CI (bootstrap 1000x) |
|--------|--------|-------|------|---------------------------|
| All-task | 69 | 220 | 31.4% | [25.5%, 37.3%] |
| Death-prone (excl find-non-living-thing) | 69 | 200 | 34.5% | [28.0%, 41.0%] |

## Comparison with 7B

| Metric | 7B | 72B | Δ |
|--------|-----|-----|---|
| All-task DR | 42.9% | 31.4% | -11.5pp |
| Death-prone DR | ~47.0% | 34.5% | -12.5pp |

## Validation

- Reviewer's expected death-prone aggregate: **69/200 = 34.5%** ✓ (exact match)
- 13313 not used for 3 tasks: lifespan-longest-lived (only 15 eps), lifespan-longest-lived-then-shortest-lived (absent), measure-melting-point-unknown-substance (absent)
- 14838 tasks with excess lines truncated: lifespan-longest-lived (27→20, first 20 used)
- identify-life-stages-2 (40 lines on 14838) and inclined-plane (40 lines on 14838) NOT used — 13313 has complete 20-episode data for both
