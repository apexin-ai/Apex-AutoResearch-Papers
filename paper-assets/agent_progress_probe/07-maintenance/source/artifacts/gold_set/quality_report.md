# Gold Set Quality Report — annotation_unknown_2026-05-15.csv

**Date**: 2026-05-15
**Annotator**: unknown (1 of 3 planned annotators)
**Total rows**: 199

## Source Distribution

| Source | Count | % |
|--------|-------|------|
| swe-agent | 136 | 68.3% |
| openhands | 63 | 31.7% |

## Confidence Distribution

| Confidence | Count | % |
|------------|-------|------|
| 0 | 4 | 2.0% |
| 1 | 115 | 57.8% |
| 2 | 67 | 33.7% |
| 3 | 13 | 6.5% |

## Label Distribution

| Label | Count | % |
|-------|-------|------|
| progress | 132 | 66.3% |
| stagnation | 67 | 33.7% |

## Source x Label Cross-tabulation

| Source | Progress | Stagnation | Progress % |
|--------|----------|------------|------------|
| swe-agent | 70 | 66 | 51.5% |
| openhands | 62 | 1 | 98.4% |

**Flag**: OpenHands windows are almost universally labeled progress (62/63). This is a significant source imbalance — the annotator found only 1 stagnation case among 63 openhands windows. This could reflect genuine agent behavior differences or annotator bias.

## Confidence x Label Cross-tabulation

| Confidence | Progress | Stagnation | Total |
|------------|----------|------------|-------|
| 0 | 1 | 3 | 4 |
| 1 | 82 | 33 | 115 |
| 2 | 41 | 26 | 67 |
| 3 | 8 | 5 | 13 |

## Data Quality Checks

- **Duplicate (trajectory_id, window_idx) pairs**: 0
- **Missing values**: None detected
- **Annotator column**: All "unknown"
- **Label vocabulary**: {progress, stagnation} — as expected
- **Confidence range**: [0, 3] — as expected

## Statistical Power Notes

- N=199 is sufficient for overall metrics but limits stratified analysis
- conf≥2 subset: 80 windows (only 31 stagnation) — moderate power
- conf=3 subset: 13 windows — too small for reliable stratified metrics
- openhands stagnation: only 1 case — per-source analysis unreliable for openhands minority class
