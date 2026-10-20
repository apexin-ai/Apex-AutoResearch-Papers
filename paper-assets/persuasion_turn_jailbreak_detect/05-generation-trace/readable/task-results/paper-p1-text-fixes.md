# paper p1 text fixes

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_p1-text-fixes_20260523T115055_result.json`
- **Structured JSON:** [`5ca065759e69e67b7186.json`](../../sessions/5c/5ca065759e69e67b7186.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes verified. Summary of edits:

**experiments.tex:**
- **MF2**: Added dual-OOD rows (no adapt: .855/.842, +10-shot: .994/.981) to Table 2 before `\bottomrule`; added caption note about dual-OOD evaluation
- **MF3**: L184 "the advantage narrows..." → "ActorAttack detection degrades to chance level (9-class F1=0.504±0.107, indistinguishable from majority baseline ~0.5 at n=3)"
- **MF5**: L65 bootstrap CIs → seed-level primary with exploratory bootstrap secondary
- **MF6**: L115 "3--23×" → "descriptively 3--23×"
- **SF4**: L112 "primary mechanism" → "primary observed factor"
- **SF4**: L178 "is driven by DAPT" → "appears primarily associated with DAPT"

**introduction.tex:**
- **SF4**: L9 "requires domain adaptation, not a better classifier" → "at base model scale benefits substantially from domain adaptation"
- **SF4**: L26 "is necessary" → "appears necessary"

**conclusion.tex (Discussion only):**
- **SF4**: L8 "is necessary" → "appears necessary"
- **MF6**: L11 "3--23×" → "descriptively 3--23×"
- **SF4**: Added alternative interpretation paragraph (overfitting/representation collapse vs. beneficial feature selection) at end of "Cross-condition transfer and boundaries." paragraph

---
