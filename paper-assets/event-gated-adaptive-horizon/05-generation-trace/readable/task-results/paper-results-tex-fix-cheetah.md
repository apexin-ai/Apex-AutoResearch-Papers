# paper results tex fix cheetah

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_results_tex_fix_cheetah_20260525T155535_result.json`
- **Structured JSON:** [`981a0fbb0c04f45ad395.json`](../../sessions/98/981a0fbb0c04f45ad395.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`results.md` already has correct numbers (10/10, 8 Walker, 2 Cheetah, 0/8 controls, p<0.0001). Consistent with the LaTeX edits.

Here's a summary of all changes made:

### Diffs by file

**`docs/paper/sections/results.tex`** — 4 edits:
| Location | Before | After | Registry source |
|---|---|---|---|
| Line 84 | `all seven tested seeds ($n{=}7$)...6/7 sustained...1/7 self-correcting` | `all ten tested runs ($n{=}10$)...6/10 sustained...three self-correct...one onset without sustained collapse` | 8 Walker + 2 Cheetah (010b, 078) |
| Line 31 | Only 010b row | Added exp\_078 row: eval 119.5@105K, NVE 4.10×, Self-correcting | exp\_078 registry: nve\_peak=4.10, eval\_return\_final=119.5 |
| Line 99 | `0/5 controls`, `p < 0.001` | `0/8 controls`, `p < 0.0001` | Agent context |
| Line 134 | `Untreated & 7 & 0/7 & 0\%` | `Untreated & 10 & 0/10 & 0\%` | 10 total trigger runs |

**`docs/paper/sections/introduction.tex`** — 1 edit:
| Location | Before | After |
|---|---|---|
| Line 11 | `7/7 multi-joint locomotion seeds` | `10/10 multi-joint locomotion runs` |

**`docs/paper/sections/analysis.tex`** — 4 edits:
| Location | Before | After |
|---|---|---|
| Line 14 | `7/7 trained locomotion` | `10/10 trained multi-joint locomotion runs` |
| Line 32 | Walker `\cmark~(5/5)` | `\cmark~(8/8)` |
| Line 37 | Cheetah `$26.3 \pm 36.0$`, `$70.64\times$` | `$85.6 \pm 33.9$`, `$8.27\times$` |
| Line 48 | `7/7 seeds`, `0/6 seeds` | `10/10 runs`, `0/8 runs` |

**`docs/paper/sections/appendix.tex`** — 4 edits:
| Location | Before | After |
|---|---|---|
| Line 732 caption | `all seven CIVO-positive seeds` | `all ten CIVO-positive runs` |
| Line 747 | (table ended at 010b\_s0) | Added exp\_078 row with footnote |
| Line 754 | `All seven...6/7 seeds...one self-correction...NVE $8.27$--$108.52\times$` | `All ten...6/10 runs...Three self-correct...Cheetah seed~1 NVE $8.27\times$` |
| Line 372 | `0/5 controls...p < 0.001` | `0/8 controls...p < 0.0001` |

D151 compliance: self-correcting is mentioned in exactly 2 sentences across the main results text (results.tex line 84), with no claim upgrade.

---
