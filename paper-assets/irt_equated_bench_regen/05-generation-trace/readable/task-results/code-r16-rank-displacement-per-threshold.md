# code r16 rank displacement per threshold

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r16_rank_displacement_per_threshold_20260523T110807_result.json`
- **Structured JSON:** [`86d8f7331fdfb37aeb46.json`](../../sessions/86/86d8f7331fdfb37aeb46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs generated. Key findings:

- **All z-scores >> 2** across every threshold — DIF-flagged items cause significantly more ranking instability than random removal of the same count.
- Threshold 1.0 flags 49% of items (too aggressive), z ≈ 4. Thresholds 1.5–2.5 flag 10–31% with z-scores 13–19, showing the effect is robust and not driven by sheer removal volume.
- Max displacement reaches ~800–1000 ranks (out of 5227 models) — some models shift dramatically.
- Flip rates are 2–3× the random baseline at every threshold.

Output files in `artifacts/r16_threshold_calibration/`:
- `rank_displacement_by_threshold.csv` — full metrics table
- `rank_displacement_report.md` — formatted report
- `rank_displacement.py` — analysis script

---
