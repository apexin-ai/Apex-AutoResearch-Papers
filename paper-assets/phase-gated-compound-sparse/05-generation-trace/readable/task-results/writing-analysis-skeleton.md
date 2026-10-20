# writing analysis skeleton

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_analysis-skeleton_20260514T054050_result.json`
- **Structured JSON:** [`16d911f311d09a01809f.json`](../../sessions/16/16d911f311d09a01809f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Section written and registered. The file is at both `docs/paper/analysis.tex` (via `write_paper_section`) and `artifacts/_project/paper/analysis.tex`.

**Structure delivered:**
- **Opening paragraph**: poses the question (why phase-modulated for importance but not random?), introduces entropy-discrimination collapse
- **§6.1 Attention Redistribution**: defines attention entropy $\mathcal{H}$, argues pruning increases $\mathcal{H}$ asymmetrically across phases due to differential head redundancy; `\placeholder{}` for empirical entropy measurements
- **§6.2 Discrimination Collapse**: links entropy increase → uniform importance scores → noise-sensitive eviction → degeneracy to biased random; `\placeholder{}` for Gini/concentration metrics; explains crossover via the mechanism; notes random's immunity
- **§6.3 Implications**: architecture generality (H₂O/SnapKV/PyramidKV all affected), testable prediction (attention-independent metrics should be immune), reframing compound severity as strategy-phase interaction

**Framing constraints respected**: consistently frames as "emergent phase-strategy interaction," explicitly states the severity inversion is "not a failure of the importance metric in isolation" (line 32). Uses "we hypothesize" / "we propose" for unverified claims. Two `\placeholder{}` blocks mark where empirical data (C4) should go.

---
