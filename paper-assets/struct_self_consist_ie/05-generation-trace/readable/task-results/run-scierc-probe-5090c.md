# run scierc probe 5090c

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_scierc_probe_5090c_20260521T022157_result.json`
- **Structured JSON:** [`6175b0b542b6aeb809d9.json`](../../sessions/61/6175b0b542b6aeb809d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron monitoring set up — checks FewNERD N=16 every 20 minutes and will auto-register results when it finishes.

**Status summary:**

| Task | Status | Result |
|------|--------|--------|
| SciERC Entity Probe (cuda:1) | ✅ DONE | AUROC = 0.977 ± 0.001 |
| CoNLL T=1.0 (cuda:3) | ✅ DONE | greedy_f1=0.908, ρ(SJ,F1)=0.425 |
| FewNERD N=16 (cuda:2) | 🔄 3.9% | ~2h remaining, cron monitoring active |
| 14B inference (cuda:0) | 🔄 running | not touched per instructions |

cuda:1 and cuda:3 are now free. All requested tasks are handled — waiting on FewNERD N=16 to finish.

---
