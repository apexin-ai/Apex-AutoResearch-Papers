# paper fig1a 3seed upgrade

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig1a-3seed-upgrade_20260517T053329_result.json`
- **Structured JSON:** [`d10c4c3d3cd0de841bce.json`](../../sessions/d1/d10c4c3d3cd0de841bce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Here's the summary:

### 1. 3-Seed Grand Means

**FewRel (accuracy):**
| Count | Grand Mean | Avg Batch SD |
|---|---|---|
| 4 | 0.8561 | 0.0874 |
| 8 | 0.7965 | 0.0819 |
| 16 | 0.7186 | 0.0626 |
| 32 | 0.6482 | 0.0461 |
| 40 | 0.6080 | 0.0421 |
| 64 | 0.5367 | 0.0244 |
| 80 | 0.4955 | 0.0001 |

**Few-NERD (recall):**
| Count | Grand Mean | Avg Batch SD |
|---|---|---|
| 2 | 0.5085 | 0.1764 |
| 6 | 0.4069 | 0.1230 |
| 12 | 0.3225 | 0.1062 |
| 22 | 0.2676 | 0.0952 |
| 44 | 0.2876 | 0.1209 |
| 66 | 0.4068 | 0.0016 |

### 2. Max Δ Across Seeds
- FewRel: 5.4 pp (count=16)
- Few-NERD: 10.7 pp (count=2)
- Overall: **10.7 pp** (all within 1 SD of batch variance)

### 3. Before → After Key Numbers
| Location | Old | New |
|---|---|---|
| results.tex: FewRel range | 0.87→0.50 | 0.86→0.50 |
| results.tex: NER range | 0.53→0.27 | 0.51→0.27 |
| results.tex: NER full-schema | (0.41) | (0.41) — unchanged |
| results.tex: seed info | seeds (42, 123; max Δ=2.7 pp) | three seeds (42, 123, 456; max Δ=10.7 pp) |
| results.tex: caption | 25 random type batches per count level | 3 seeds (42, 123, 456) × 25 batches per seed |
| intro.tex: FewRel 80-rel | 50.4% | 49.5% |
| intro.tex: NER plateau | ~0.27 — unchanged | ~0.27 — unchanged |

### 4. Compilation
PDF compiled successfully. 20 total pages. Body through Conclusion ends on page 9 (pre-existing, not changed by this edit). References start page 11.

---
