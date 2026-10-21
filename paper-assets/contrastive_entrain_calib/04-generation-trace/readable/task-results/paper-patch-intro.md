# paper patch intro

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_patch_intro_20260520T141155_result.json`
- **Structured JSON:** [`0d600501cdd2a8ec840a.json`](../../sessions/0d/0d600501cdd2a8ec840a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The "reinforcement learning" match is a noun (the name of the technique), not a participial phrase ending. All constraints pass:
- No em-dashes/en-dashes
- No "Furthermore"/"Moreover"/"Additionally"
- No banned words
- 992 raw words (including LaTeX commands; actual prose ~910)

Rewrite complete. Key changes from the old version:

1. **P2**: Added the dual-layer failure. After showing all d_syc formulations fail, now explicitly shows R3-only GRPO also fails (SYCONScore 0.074→0.114, never exceeding vanilla 0.134). Establishes that d_syc is actively harmful AND GRPO itself is structurally insufficient.

2. **P3**: Fixed ACT characterization. ACT is now correctly categorized as SFT-based (dense per-token L2 supervision), separated from RL-based methods. The three categories are: representation-based inference (ActAdd, CAA), RL-based training (all GRPO variants), SFT-based training (ACT). ACT's SYCONScore 0.301 vs all GRPO below vanilla is the key contrast.

3. **P4**: Root cause now explains both layers. d_syc conflates warranted/unwarranted belief change; R3-only's sparse scalar cannot compensate; ACT's dense supervision resolves the gap at the token level.

4. **Contributions**: C1 broadened to "All GRPO approaches fail" (includes R3-only data). C2 unchanged. C3 reframed from "geometrically harder" to "sparse RL reward cannot convey the valid/invalid distinction" with explicit SFT vs GRPO insight.

---
