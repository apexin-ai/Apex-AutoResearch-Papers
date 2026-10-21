# analysis cascade theory empirical validation

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cascade_theory_empirical_validation_20260520T185910_result.json`
- **Structured JSON:** [`c5b5a6a49b30be3bed47.json`](../../sessions/c5/c5b5a6a49b30be3bed47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Written both artifacts:
- `artifacts/theory/cascade_empirical_validation.md` — full report with 3 query tables and analysis
- `artifacts/theory/cascade_empirical_data.json` — structured data with all onset values

Key findings:

**Query 1 (α=1.0)**: Entropy still leads diversity (t_H=1, t_D=2). Condition (6) does not break even at maximal perturbation.

**Query 2 (C4)**: Domain-normalized analysis (M3) confirms cascade ordering holds on C4 (t_H=1, t_D=2). Raw comparison is confounded by WikiText→C4 domain shift.

**Query 3 (Low-α)**: This is the strongest result — at α≤0.25, entropy does NOT onset at all (gen1 deviation 0.004–0.011, far below threshold 0.121). Sharp phase transition at α~0.30 where gen1 deviation jumps 60× to 0.483. **Gen-1 artifact hypothesis refuted** by three independent tests: α-dependence, phase transition sharpness, and metric asymmetry (distinct-n never triggers at gen 1).

Invariant across all 17 WikiText experiments: t_D = 2 regardless of α, seed, or entropy onset status.

---
