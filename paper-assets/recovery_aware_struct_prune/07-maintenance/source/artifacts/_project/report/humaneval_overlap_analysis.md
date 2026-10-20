# HumanEval Overlap Analysis

## Summary
| Model | Passed | Total | Pass@1 |
|-------|--------|-------|--------|
| GRPO_Standard | 18 | 164 | 11.0% |
| GRPO_RASP | 18 | 164 | 11.0% |
| SFT_CKA | 33 | 164 | 20.1% |
| GRPO_CKA | 33 | 164 | 20.1% |

## A. Pairwise Overlap Matrix

| A vs B | Both Pass | A-only | B-only | Both Fail |
|--------|-----------|--------|--------|-----------|
| Std vs RASP | 5 | 13 | 13 | 133 |
| Std vs SFT-CKA | 9 | 9 | 24 | 122 |
| Std vs GRPO-CKA | 8 | 10 | 25 | 121 |
| RASP vs SFT-CKA | 8 | 10 | 25 | 121 |
| RASP vs GRPO-CKA | 5 | 13 | 28 | 118 |
| SFT-CKA vs GRPO-CKA | 17 | 16 | 16 | 115 |

## Key Finding 1: GRPO Standard vs RASP Overlap

- Both passed: **5/18**
- Jaccard similarity: 16.1%
- Standard-only (13): HumanEval/133, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/35, HumanEval/45, HumanEval/49, HumanEval/51, HumanEval/53, HumanEval/60, HumanEval/90, HumanEval/97
- RASP-only (13): HumanEval/102, HumanEval/12, HumanEval/151, HumanEval/154, HumanEval/29, HumanEval/3, HumanEval/34, HumanEval/47, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82, HumanEval/92

**Conclusion**: Moderate overlap (5/18). RASP and Standard pruning preserve partially different code capabilities.

## Key Finding 2: CKA-only Superset Analysis

- CKA-only union (SFT CKA ∪ GRPO CKA): **49** unique tasks
- Standard ∪ RASP union: **31** unique tasks
- Overlap (both groups pass): **18**
- CKA superset of Standard/RASP? **No** (covers 18/31 of Standard/RASP tasks)

- Standard/RASP-only tasks (13): HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82
- CKA-exclusive tasks (31): HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/112, HumanEval/115, HumanEval/123, HumanEval/139, HumanEval/155, HumanEval/159, HumanEval/17, HumanEval/2, HumanEval/21, HumanEval/22, HumanEval/27, HumanEval/30, HumanEval/4, HumanEval/40, HumanEval/42, HumanEval/44, HumanEval/5, HumanEval/52, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/7, HumanEval/72, HumanEval/8, HumanEval/85, HumanEval/88, HumanEval/9, HumanEval/96

## Key Finding 3: SFT CKA -> GRPO CKA Transition

- Both passed: **17**
- SFT-only (GRPO lost, 16): HumanEval/102, HumanEval/104, HumanEval/106, HumanEval/111, HumanEval/123, HumanEval/155, HumanEval/157, HumanEval/31, HumanEval/45, HumanEval/47, HumanEval/5, HumanEval/60, HumanEval/85, HumanEval/9, HumanEval/92, HumanEval/96
- GRPO-only (GRPO gained, 16): HumanEval/112, HumanEval/12, HumanEval/133, HumanEval/139, HumanEval/151, HumanEval/17, HumanEval/4, HumanEval/42, HumanEval/44, HumanEval/55, HumanEval/63, HumanEval/68, HumanEval/72, HumanEval/88, HumanEval/90, HumanEval/97
- Net effect: 33 - 33 = **+0** (GRPO lost 16, gained 16)

## B. CKA-only Exclusive Tasks (Detailed)

Tasks passed by CKA-only models (SFT or GRPO) but failed by both GRPO Standard and GRPO RASP:

| # | Task ID | SFT CKA | GRPO CKA |
|---|---------|---------|----------|
| 1 | HumanEval/104 | Pass | Fail |
| 2 | HumanEval/106 | Pass | Fail |
| 3 | HumanEval/111 | Pass | Fail |
| 4 | HumanEval/112 | Fail | Pass |
| 5 | HumanEval/115 | Pass | Pass |
| 6 | HumanEval/123 | Pass | Fail |
| 7 | HumanEval/139 | Fail | Pass |
| 8 | HumanEval/155 | Pass | Fail |
| 9 | HumanEval/159 | Pass | Pass |
| 10 | HumanEval/17 | Fail | Pass |
| 11 | HumanEval/2 | Pass | Pass |
| 12 | HumanEval/21 | Pass | Pass |
| 13 | HumanEval/22 | Pass | Pass |
| 14 | HumanEval/27 | Pass | Pass |
| 15 | HumanEval/30 | Pass | Pass |
| 16 | HumanEval/4 | Fail | Pass |
| 17 | HumanEval/40 | Pass | Pass |
| 18 | HumanEval/42 | Fail | Pass |
| 19 | HumanEval/44 | Fail | Pass |
| 20 | HumanEval/5 | Pass | Fail |
| 21 | HumanEval/52 | Pass | Pass |
| 22 | HumanEval/55 | Fail | Pass |
| 23 | HumanEval/63 | Fail | Pass |
| 24 | HumanEval/68 | Fail | Pass |
| 25 | HumanEval/7 | Pass | Pass |
| 26 | HumanEval/72 | Fail | Pass |
| 27 | HumanEval/8 | Pass | Pass |
| 28 | HumanEval/85 | Pass | Fail |
| 29 | HumanEval/88 | Fail | Pass |
| 30 | HumanEval/9 | Pass | Fail |
| 31 | HumanEval/96 | Pass | Fail |

## Interpretation

GRPO Standard and GRPO RASP share only 5/31 tasks (16% Jaccard). The two pruning strategies preserve meaningfully different code capabilities after GRPO recovery.

CKA-only covers 18/31 Standard/RASP tasks and adds 31 exclusive tasks, but loses 13 tasks (HumanEval/13, HumanEval/135, HumanEval/136, HumanEval/138, HumanEval/144, HumanEval/154, HumanEval/29, HumanEval/34, HumanEval/35, HumanEval/69, HumanEval/73, HumanEval/74, HumanEval/82). The capability profiles partially diverge.

SFT->GRPO CKA maintains the same pass count (33) but with 16 task swaps: GRPO loses 16 SFT tasks and gains 16 new ones. This suggests GRPO redistributes capability rather than expanding it.