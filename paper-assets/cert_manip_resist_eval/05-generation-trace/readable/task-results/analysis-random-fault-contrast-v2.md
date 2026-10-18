# analysis random fault contrast v2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_random-fault-contrast-v2_20260523T182424_result.json`
- **Structured JSON:** [`0ed0834ad32336a582fe.json`](../../sessions/0e/0ed0834ad32336a582fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

**Scripts found:**
- `run_k5_rf_contrast.py` — RF side V2 (clean accuracy), but loaded adaptive R² from V1 `k5_aggregation_analysis.json`
- `run_k5_aggregation_analysis.py` — **V1 (fixed to V2)**: had `.get("winner","tie")` at 4 locations
- `run_rf_keff_correction.py` (K=3) — already V2, self-contained
- `run_plan001_step5_random_fault.py` — V2 imports (local V1 functions dead code), never run

**Fix applied:** `run_k5_aggregation_analysis.py` — added `_is_valid_score` filtering. Reran both aggregation and RF contrast scripts.

**V1 → V2 changes:**
| Metric | V1 | V2 | Delta |
|--------|----|----|-------|
| RF mean R² | 0.7047 | 0.7047 | 0 (unchanged) |
| Adaptive mean R² | 0.2562 | 0.2751 | +0.019 |
| RF-Adaptive gap | +0.4485 | +0.4296 | -0.019 |

RF R² unchanged (clean accuracy based, not affected by V1 bug). Adaptive R² shifted slightly upward. Gap narrowed marginally but remains massive (0.43). Contrast significance fully preserved.

Output written to `docs/paper/data/random_fault_contrast_corrected.json`.

---
