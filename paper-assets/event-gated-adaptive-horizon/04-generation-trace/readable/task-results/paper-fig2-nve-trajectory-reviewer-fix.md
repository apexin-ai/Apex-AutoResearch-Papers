# paper fig2 nve trajectory reviewer fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fig2_nve_trajectory_reviewer_fix_20260515T183811_result.json`
- **Structured JSON:** [`b2c58ae05782ad057feb.json`](../../sessions/b2/b2c58ae05782ad057feb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs generated. File sizes increased from 31K/337K to 33K/392K (PDF/PNG), consistent with the additions.

**Summary of changes:**

| Fix | What was done |
|-----|------|
| **Fix 1: 35K+ classification window** | `axvspan(25K-35K)` gray zone (alpha=0.22) + vertical dashed line at 35K + "Classification window →" annotation at top-right of the gray band |
| **Fix 2: 008e_v3_s2 actor loss** | Purple dashed line (#9B59B6, marker='P') in bottom panel with hardcoded data from metrics.jsonl. Label "008e_v3 s2 (IRD)". Sign flip annotation at 105K (+0.016) |
| **Fix 3: exp_006** | Omitted — y-axis would need 5.2+ which compresses the 0-2 cluster where most runs live. Caption suggestion printed: *"exp_006 (NVE=4.84x) omitted for clarity; see Appendix Table X."* |

**Other changes vs server version:**
- 008d/009e NVE data extended from 6 points (→75K) to 9 points (→105K)
- Baseline trimmed to ≤105K to match x-range
- Added linestyle differentiation in bottom panel
- Fixed x-axis ticks to uniform 0-110K range in bottom panel

**Output files:**
- `artifacts/fig2_nve_trajectory_d054.pdf` (33K)
- `artifacts/fig2_nve_trajectory_d054.png` (392K)
- `artifacts/figures/paper/fig2_nve_trajectory.{pdf,png}` (same)

---
