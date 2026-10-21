# paper writing probe trap

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_probe_trap_20260520T075146_result.json`
- **Structured JSON:** [`020c47e8223ee4c95dd5.json`](../../sessions/02/020c47e8223ee4c95dd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Written to `docs/paper/sections/probe_trap.tex`. The section (~660 words) follows the specified narrative arc:

1. **Differentiable probe** (exp-008): gamed in ~30 steps, inverted to ToF=0.978/NoF=0.006
2. **Binary probe mechanism** (exp-008v3): stubbornness trap where never flipping collects reward
3. **Behavioral-before-distributional collapse**: ToF=0 at step 500, entropy healthy at 0.70, 1,300-step diagnostic lag; entropy monitoring cannot detect the failure
4. **Dilemma**: differentiable = gaming, non-differentiable = rigidity trap; both stem from d_syc not encoding warrant

All custom commands (`\dsyc`, `\rone`, `\rthree`, `\tof`, `\nof`, `\sycon`), figure reference (`fig:probe_trap`), and citation keys used. No em-dashes, no -ing phrase endings.

---
