# paper writing abstract

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_abstract_20260524T193730_result.json`
- **Structured JSON:** [`b1c43c1b89cf96ac6667.json`](../../sessions/b1/b1c43c1b89cf96ac6667.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Abstract v2 written to `artifacts/drafts/abstract_v2.tex` (211 words). Structure:

- **Problem** (2 sentences): VLA collision avoidance methods report high CAR, but metrics are contaminated by action collapse
- **Evidence** (2 sentences): 91.5% CAR with 99.6% fake safe; cross-method validation (82% CAR / 99.4% fake on baseline)
- **Corrective metric**: displacement-filtered CAR (CAR_f)
- **Claim 2**: TSR-CAR anti-correlation
- **Claim 3**: EE-only SDF oracle fails (arm links sweep through obstacles)
- **Claim 4** (1 sentence): training-time SDF on capable VLA yields genuine avoidance with 0% frozen-action rate
- **Takeaway** (1 sentence): displacement filtering is necessary for meaningful evaluation

All abbreviations expanded on first use (VLA, CAR, SDF, TSR, CAR_f). No em-dashes, no -ing sentence endings. Key numbers limited to 91.5%/99.6% core pair plus 82%/99.4% cross-validation.

---
