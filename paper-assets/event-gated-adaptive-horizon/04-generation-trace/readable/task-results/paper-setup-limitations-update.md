# paper setup limitations update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_setup-limitations-update_20260516T045238_result.json`
- **Structured JSON:** [`bd6470b4147f67f17573.json`](../../sessions/bd/bd6470b4147f67f17573.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Only hit is in `related_work.md` (Lu et al. delusional bias reference — that's a citation to prior work, not our terminology). Both edited files are clean.

**Summary of changes:**

**experimental_setup.md** (2 edits):
- Table 1: added 018 (Full-SGS) row with `$^\ddagger$` footnote marking it as pending at submission
- §4.4 Classification accuracy: added `nve_sensitivity_table` reference to supplementary material sentence

**limitations.md** (2 edits):
- "Limited seed count": added 7/8 overall accuracy and AUROC=0.933 alongside retained 4/4 threshold separation; identified 008e_v3_s2 FP as non-CIVO
- "NVE threshold": fixed CI attribution — [47.3%, 99.7%] now correctly attributed to 7/8 (not 4/4); added supplementary 8/8 CI [68.8%, 100%] at 1.7x threshold

All other DIFF items (E2–E5, seed updates, mitigation removal, baseline normalization) were already applied in the current files.

---
