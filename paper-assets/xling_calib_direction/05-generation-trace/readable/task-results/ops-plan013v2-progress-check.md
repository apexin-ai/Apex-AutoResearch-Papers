# ops plan013v2 progress check

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan013v2_progress_check_20260521T135826_result.json`
- **Structured JSON:** [`be18df8c39e59186f6f8.json`](../../sessions/be/be18df8c39e59186f6f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full picture now. Here's the summary:

## PID 47972 Status
- **Alive**, running **13h 03m**, CPU 97.8%
- Command: `python -u -W ignore code/probing_controls_v2.py`
- Log: `/tmp/probing_v2.log`

## Progress: 4/8 layers complete

Layer order (string-sorted): `[0, 12, 16, 20, 24, 27, 4, 8]`

| Layer | CV AUROC | Perm AUROC | Perm Std | Selectivity | Time |
|-------|----------|------------|----------|-------------|------|
| 0 | 0.6304 | 0.5007 | 0.0049 | **+0.1297** | 3.5h |
| 12 | 0.6389 | 0.4977 | 0.0067 | **+0.1411** | 2.6h |
| 16 | 0.6801 | 0.5038 | 0.0084 | **+0.1764** | 2.1h |
| 20 | 0.7211 | 0.5006 | 0.0082 | **+0.2205** | 2.1h |

**Currently running**: Layer 24 (started ~2.7h ago, ~37293s of compute done before it)

**Remaining**: L24 (in progress), L27, L4, L8

## Key observations
- All permuted AUROCs are ~0.50 (chance level) — controls are working correctly
- Selectivity increases monotonically with depth: L0 (+0.13) → L20 (+0.22)
- L0 took longest (3.5h), mid-to-late layers average ~2.1-2.6h each

## Estimated completion
- L24 has been running ~2.7h, likely finishing soon (avg ~2.2h for recent layers, but L24 may have more signal → longer)
- Remaining 4 layers × ~2.3h avg = **~7-9 hours total remaining**
- Estimated completion: ~**May 22 morning (UTC+8)**

## Output path
Results will be written to: `/root/xling_calib_direction/results/probing_controls_v2.csv` (only created after all 8 layers finish)

---
