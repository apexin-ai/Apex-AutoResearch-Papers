# paper 008e v3 s1 nve fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_008e-v3-s1-nve-fix_20260517T131402_result.json`
- **Structured JSON:** [`eabf73fd448f44bc1d0d.json`](../../sessions/ea/eabf73fd448f44bc1d0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No residual `0.80` anywhere in `docs/paper/`.

**Summary of changes in `docs/paper/sections/results.tex`:**

1. **Line 39** (Table 1, 008e\_v3 s1 row): `0.80$\times$` → `0.94$\times$`
2. **Line 109** (F6 paragraph, inline text): `$\nve = 0.80\times$` → `$\nve = 0.94\times$`

**Verification:**
- No `0.80` remains in any `.tex` file under `docs/paper/`
- Appendix Table 4 already had `0.94` for 008e\_v3\_s1 — now consistent with Table 1

---
