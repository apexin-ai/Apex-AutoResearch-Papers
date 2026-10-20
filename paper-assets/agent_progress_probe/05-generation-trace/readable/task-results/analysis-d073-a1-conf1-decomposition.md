# analysis d073 a1 conf1 decomposition

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d073-a1-conf1-decomposition_20260516T022720_result.json`
- **Structured JSON:** [`fe666077c9de56333951.json`](../../sessions/fe/fe666077c9de56333951.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass. Output saved to `artifacts/d073/conf1_error_decomposition.json`.

Key findings on conf=1 (N=172 SWE windows with gold):

| Cell | Count | % |
|---|---|---|
| Both correct | 125 | 72.7% |
| GB correct, MV wrong | 15 | 8.7% |
| GB wrong, MV correct | 2 | 1.2% |
| Both wrong | 30 | 17.4% |

**GB net advantage: +13 windows** (corrects 15 MV errors, introduces only 2 new ones). The advantage is concentrated in **stagnation** detection (12 of 15 GB corrections are stagnation windows where MV called progress). This confirms GB learns structural patterns that LF majority voting misses, particularly for identifying stagnation in LF-disagreement cases.

---
