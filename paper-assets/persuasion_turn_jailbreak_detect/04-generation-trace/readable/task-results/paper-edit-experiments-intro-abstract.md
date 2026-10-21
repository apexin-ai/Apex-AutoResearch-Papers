# paper edit experiments intro abstract

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper-edit_experiments-intro-abstract_20260521T214615_result.json`
- **Structured JSON:** [`90dbc5cf217264a17971.json`](../../sessions/90/90dbc5cf217264a17971.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Protected areas confirmed intact.

**Edit 5 subsection review** (required by instructions):

| Section | First sentence | Qualifier needed? |
|---|---|---|
| 4.1 Cross-Attack Generalization (L56) | "Vanilla encoders collapse under cross-attack transfer" | No — Setup (L11) establishes synthetic context |
| 4.2 Decomposing the Detection Mechanism (L104) | "A clear evidence hierarchy emerges across seven variants" | No — refers to Table 2, within Setup's synthetic scope |
| 4.3 Summary (L139) | Now reads "on our synthetic multi-turn benchmark" | **Edited** ✓ |
| 4.4 Cross-Encoder Validation (L174) | "To test whether the evidence hierarchy depends on encoder choice" | No — describes experimental procedure |
| 4.5 Mixed-LLM Training (L188) | "All preceding experiments use single-source (Qwen3-8B) data" | No — already names the LLM source |
| 4.6 Human Data Validation (L196) | "Since both training and OOD evaluation data are Qwen3-8B-generated" | No — explicitly notes synthetic origin |
| 4.7 Perturbation Analysis (L227) | "Under adversarial paraphrasing (BERTScore 0.92)" | No — within synthetic benchmark context |
| 4.8 Strategy Trajectory Analysis (L233) | "The 9-class taxonomy provides interpretable characterization" | No — describes taxonomy properties |

No additional qualifiers added beyond Edit 5.

---

**Results summary:**

| Edit | Target | Status |
|---|---|---|
| 1 (Fix 10) | abstract.tex L4: `turn-level` added before `safety classifier` | ✅ |
| 2 (Fix 7) | introduction.tex L28: `indicate...provides` → `are consistent with...providing` | ✅ |
| 3 (Fix 9) | experiments.tex L6: OOD definition appended to Terminology | ✅ |
| 4 (Fix 3) | experiments.tex L81: Table 2 caption — OOD upper bound note added | ✅ |
| 5 (Fix 8) | experiments.tex L139: Summary — `on our synthetic multi-turn benchmark` inserted | ✅ |
| 6 (Fix 11) | experiments.tex L91: `Mean pooling` → `9-class + mean pool` | ✅ |

Protected areas: L27 (3-seed mean) ✓, L29 (Unless otherwise noted) ✓, L112 (TOST) ✓, intro L11 (systematically vary) ✓ — all intact.

---
