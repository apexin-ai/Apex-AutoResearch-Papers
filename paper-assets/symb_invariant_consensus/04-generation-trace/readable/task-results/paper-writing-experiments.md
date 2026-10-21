# paper writing experiments

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260517T170226_result.json`
- **Structured JSON:** [`de7d4ad4c7afb7013563.json`](../../sessions/de/de7d4ad4c7afb7013563.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass. No em-dashes in running text, no blacklisted words, no trailing -ing participial phrases.

The experiments section is written to `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/docs/paper/experiments.tex` with:

- **5 subsections**: Setup, Main Results (Table 1), Oracle Control, Capability Trap Diagnostics (Table 2 + 2 commented-out figures), Constraint Ablation (Table 3)
- **Narrative arc**: null result across 8 conditions (N>1,300) → oracle proves mechanism works (+8.82pp, p=6.15e-5) → diagnostics identify two failure modes (low C0, non-discriminative constraints) → ablation confirms MAX-SAT degenerates to counting (802/804 agreement with SC)
- All numbers from registry data, n=60 conditions use "suggestive/underpowered" language, 2-decimal accuracy, booktabs tables, self-contained captions

---
