# D130: 4B Content-Independent Backcheck

**Date**: 2026-05-18  
**Motivation**: d129 found 1.7B ISR-b01-s44 genuine inflated from 42.7% to 6.1% due to H9 conjunction aggregation with content-independent predicates. This audit checks whether 4B ISR b01 (5-seed) data has the same problem.

## Result: 4B genuine is NOT inflated

The 1.7B content_independent inflation pattern is absent in 4B. No revision needed.

## Per-Seed Data

### Official classify_h7.py taxonomy (from registry + eval_archive)

| Seed | PR | H7 | H1 | H8 | Genuine | Genuine% | CI_total |
|------|-----|-----|-----|-----|---------|----------|----------|
| s42 | 81 | 13 | 42 | 12 | 14 | 14% | 19 |
| s43 | 61 | 59 | 0 | 0 | 2 | 0% | 5 |
| s44 | 89 | 89 | 0 | 0 | 0 | 0% | N/A |
| s45 | 42 | 16 | 2 | 1 | 23 | 23% | 1 |
| s46 | 77 | 11 | 20 | 4 | 42 | 42% | 2 |

### Content-independent overlap with genuine (this audit)

| Seed | Genuine | CI in genuine | H9_conj in genuine | Strict genuine |
|------|---------|--------------|-------------------|----------------|
| s42 | 14 (official) | 0 | ~0 (H9_conj mostly = official H8) | ~14 |
| s45 | 23 | 0 | 1 | 23 |
| s46 | 42 | 0 | 2 | 42 |

**CI among genuine = 0 for all seeds.**

## Why 4B differs from 1.7B

| Dimension | 1.7B (d129 s44) | 4B (all seeds) |
|-----------|-----------------|----------------|
| Content-independent rate | 93.9% of proved | 1-19 of proved (seed-dependent) |
| CI in genuine | 30/35 (85.7%) | 0/79 (0%) |
| Predicate style | Single-letter (P, Q, R) | Content-dependent (Lawyer, Chef, Defender) |
| H9 conjunction in genuine | 30/35 | 1-2 per seed (s45/s46), caught by H8 for s42 |
| Strict genuine after audit | 5/82 (6.1%) | No change needed |

## Genuine sample quality (spot check)

Sampled 5 genuine proofs per seed. All use:
- Content-dependent predicate names derived from NL premises
- Multi-step reasoning chains (e.g., Centerback -> Defender -> Player -> not BasketballPlayer)
- 2-8 premises with ISR 0.125-1.0

Example (s45, folio_833, ISR=0.833):
```
P1: ∀x (Defender(x) → Player(x))
P2: ∀x (Player(x) → ¬BasketballPlayer(x))
P3: ∀x (Centerback(x) → Defender(x))
P4: ∀x (NBAPlayer(x) → BasketballPlayer(x))
P5: NBAPlayer(StephenCurry)
Conclusion: ¬Centerback(StephenCurry)
```
5/6 components necessary. Genuine 4-step chain reasoning.

## Conclusion

- **4B genuine figures are robust.** Content-independent inflation does not exist.
- **Pooled genuine mean (15.8%) needs no correction.**
- The 1.7B inflation was model-size specific: 1.7B models abstract to single-letter predicates and apply conjunction templates; 4B models retain content-dependent predicates and perform multi-step reasoning.
- s42's CI=19 is entirely in H7/H1/H8 categories (not genuine).

## Data sources
- s42: `/root/autodl-tmp/eval_backups/plan002_additive_b01_s42_eval_sta_results.json` + `h7_classification/plan002_additive_b01_s42_h8.json`
- s45: `/root/autodl-tmp/eval_archive/plan002_additive_b01_s45/{eval_results,h7_classification}.json`
- s46: `/root/autodl-tmp/eval_archive/plan002_additive_b01_s46/{eval_results,h7_classification}.json`
