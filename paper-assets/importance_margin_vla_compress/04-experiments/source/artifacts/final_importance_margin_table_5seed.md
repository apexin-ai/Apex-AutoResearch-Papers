# π0.5 LIBERO-Long Importance Margin Profile — Multi-Seed Data Table

> Generated: 2026-05-28 ~12:00 UTC
> All values: strict evaluation, success rate (%)
> Error bars: sample std (ddof=1) per D301

## ⚠️ Data Completeness Warning

| Seeds | Cells | Notes |
|-------|-------|-------|
| 5-seed | 3/18 | L2norm k=0.95, L2norm k=0.75, Attn k=0.95 |
| 4-seed | 7/18 | |
| 3-seed | 7/18 | Most s44/s45 values not in registry/decisions |
| 2-seed | 1/18 | L2norm k=0.7 (s46 still RUNNING) |

**Root cause:** s44 (18/18 done) and s45 (18/18 done) per ROADMAP, but individual SR values not registered — exist only in server result JSON files. **Action needed:** harvest s44/s45 values from server eval_results/ directories before final paper figures.

**RUNNING s46 experiments:** L2norm k=0.7 (w41), Random k=0.5 (w41). Random k=0.95 s46 just completed (~11:40 UTC) but value not yet harvested.

---

## Table 1: Mean ± Std Summary

| k | L2norm | Random | Attention | Importance Margin |
|------|---------|---------|-----------|-------------------|
| 0.95 | **86.8 ± 0.8** (5s) | 61.3 ± 0.8 (4s) | 77.3 ± 1.2 (5s) | **+25.5 pp** |
| 0.90 | **80.5 ± 0.5** (4s) | 33.6 ± 1.4 (4s) | 64.1 ± 1.3 (3s) | **+46.9 pp** ⭐peak |
| 0.85 | **78.3 ± 0.6** (3s) | 45.4 ± 1.3 (4s) | 50.9 ± 1.3 (3s) | **+32.9 pp** |
| 0.75 | **70.6 ± 2.7** (5s) | 62.6 ± 1.7 (4s) | 50.8 ± 1.1 (3s) | **+8.0 pp** |
| 0.70 | 64.3 ± 1.6 (2s) | 65.3 ± 0.8 (3s) | 52.8 ± 1.1 (4s) | **−1.0 pp** 🔄crossover |
| 0.50 | 51.5 ± 2.0 (3s) | 50.5 ± 0.8 (3s) | 49.4 ± 1.8 (4s) | **+1.1 pp** ≈0 |

---

## Table 2: Per-Seed Detail

### L2norm

| k | s42 | s43 | s44 | s45 | s46 | mean ± std | n |
|------|------|------|------|------|------|------------|---|
| 0.95 | 86.2 | 85.8 | 86.8 | 87.8 | 87.2 | 86.8 ± 0.8 | 5 |
| 0.90 | 80.0 | 81.2 | 80.4 | — | 80.6 | 80.5 ± 0.5 | 4 |
| 0.85 | 77.6 | 78.6 | — | — | 78.6 | 78.3 ± 0.6 | 3 |
| 0.75 | 70.8 | 73.2 | 67.4 | 68.4 | 73.2 | 70.6 ± 2.7 | 5 |
| 0.70 | 63.2 | 65.4 | — | — | ⏳RUN | 64.3 ± 1.6 | 2 |
| 0.50 | 49.2 | 52.8 | — | — | 52.6 | 51.5 ± 2.0 | 3 |

### Random

| k | s42 | s43 | s44 | s45 | s46 | mean ± std | n |
|------|------|------|------|------|------|------------|---|
| 0.95 | 60.6 | 60.8 | 61.2 | 62.4 | ⏳done | 61.3 ± 0.8 | 4 |
| 0.90 | 34.2 | 35.0 | 31.8 | — | 33.4 | 33.6 ± 1.4 | 4 |
| 0.85 | 45.2 | 47.2 | 44.2 | — | 44.8 | 45.4 ± 1.3 | 4 |
| 0.75 | 63.0 | 60.6 | 64.6 | — | 62.2 | 62.6 ± 1.7 | 4 |
| 0.70 | 66.0 | 64.4 | — | — | 65.6 | 65.3 ± 0.8 | 3 |
| 0.50 | 49.8 | 51.4 | 50.2 | — | ⏳RUN | 50.5 ± 0.8 | 3 |

### Attention

| k | s42 | s43 | s44 | s45 | s46 | mean ± std | n |
|------|------|------|------|------|------|------------|---|
| 0.95 | 78.4 | 77.2 | 77.8 | 77.8 | 75.2 | 77.3 ± 1.2 | 5 |
| 0.90 | 64.0 | 62.8 | — | — | 65.4 | 64.1 ± 1.3 | 3 |
| 0.85 | 50.0 | 52.4 | — | — | 50.4 | 50.9 ± 1.3 | 3 |
| 0.75 | 49.8 | 52.0 | — | — | 50.6 | 50.8 ± 1.1 | 3 |
| 0.70 | 53.6 | 53.8 | 52.2 | — | 51.4 | 52.8 ± 1.1 | 4 |
| 0.50 | 52.0 | 48.8 | 48.8 | — | 48.0 | 49.4 ± 1.8 | 4 |

---

## Data Integrity Checklist

| # | Item | Status | Value Used |
|---|------|--------|------------|
| 1 | Attn k=0.75 s43: use cqa1 value | ✅ | 52.0% (w27=49.0% discarded — w27 lacks attention scoring) |
| 2 | Attn k=0.75 s42: verify source | ✅ | 49.8% from D278 (w41 canonical — w41 supports attention) |
| 3 | Random k=0.9 s43: use v2 | ✅ | 35.0% (D292/D273, old 32.4% discarded) |
| 4 | OV Attn k=0.75: use v3 | N/A | π0.5 table only |
| 5 | Random k=0.85 s43: per-task mixing | ✅ | Overall SR=47.2% reliable; per-task from server log needed |
| 6 | Metrics scale unified | ✅ | All values 0-100% scale |
| 7 | Attn k=0.95 s42: D268 correction | ✅ | 78.4% (D268 v2, supersedes old 77.0% — zero-masking bug fixed) |

## Data Sources

- **Registry (DONE):** primary for s42/s43 experiments
- **Decisions.yaml (D250–D301):** s42/s43 strict corrections, s44 3-seed summaries
- **ROADMAP s46 table:** all s46 values marked ✅
- **Report.md conclusions:** Random k=0.95 s42-s45 aggregation, L2norm k=0.7 s42-s45 aggregation
- **NOT captured:** most s44/s45 individual values (experiments ran but not tracked)

## Key Narrative Numbers

- **Peak Importance Margin:** +46.9 pp at k=0.9 (L2norm 80.5% vs Random 33.6%)
- **Crossover point:** ~k=0.7 where margin flips to −1.0 pp (Random > L2norm)
- **Convergence:** k=0.5 margin ≈ +1.1 pp ≈ 0 (both methods ~50%)
- **Attn cliff:** 77.3% (k=0.95) → 64.1% (k=0.9) → 50.9% (k=0.85), then plateau ~50%
