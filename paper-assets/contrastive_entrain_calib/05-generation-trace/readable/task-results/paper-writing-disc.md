# paper writing disc

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_disc_20260520T144740_result.json`
- **Structured JSON:** [`0806ac69179ab7eb84aa.json`](../../sessions/08/0806ac69179ab7eb84aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Discussion section written to `docs/paper/sections/discussion.tex`. ~680 words across 4 paragraphs:

1. **Unified root cause** — cosine too punitive, probe too permissive; both are dual symptoms of $d_{\text{syc}}$ conflating target and complement. Cross-model (Llama-3-8B AUROC 0.779) confirms generalizability of the gap.
2. **GRPO stubbornness** — Table 2 comparing all 6 methods. R3-only GRPO trajectory (0.074→0.114 over 5000 steps) stays below vanilla 0.134. ActAdd also included.
3. **Why SFT succeeds** — ACT non-monotonic trajectory (dip at ckpt-4000, recovery at ckpt-6000/8000). Dense per-token loss breaks stubbornness equilibria that sparse reward reinforces. 16x efficiency over GRPO.
4. **Future directions** — condition-aware rewards, hybrid SFT+RL, process reward models, generalization beyond sycophancy.

---
