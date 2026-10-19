# ssh deploy v9 3gpu

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy-v9-3gpu_20260513T075451_result.json`
- **Structured JSON:** [`c0ef39a5414367722c16.json`](../../sessions/c0/c0ef39a5414367722c16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No episode boundary detection triggered in dry-run (0 occurrences) — which is expected since the successful task 1 completed via `reward=True` from `info["won"]`, not via boundary detection. The boundary detection is a fallback for when ALFWorld auto-resets.

## D031 Report

### Step 1: Code Sync -- PASS
| File | Status |
|------|--------|
| `artifacts/collect_trajectories_icl.py` | FILE1_OK |
| `src/build_dpo_pairs.py` | FILE2_OK |
| `src/etadn_discount.py` | FILE3_OK |
| `src/train_dpo.py` | FILE4_OK |
| `src/dmpo_loss.py` | FILE5_OK |

Verification greps all passed:
- `episode boundary` at line 336
- `max_new_tokens: int = 2048` at line 240
- `gamma_planning: float = 1.0` at line 33
- `gamma_min/gamma_max` continuous mode confirmed

### Step 2: Dry-run -- PASS (1/2 = 50%)
| Task | Type | Reward | Steps | Time |
|------|------|--------|-------|------|
| 0 | pick_clean_then_place | False | 40 | 158.6s |
| 1 | pick_clean_then_place | **True** | 35 | 118.0s |

- `&lt;think>` leakage: **0** (clean)
- Episode boundary detection: code present, not triggered (normal path used)

### Step 3: v9 Full Collection -- ALREADY RUNNING
v9 was already launched by a previous session on 3 GPUs:

| GPU | CUDA_VISIBLE_DEVICES | part_idx | Status | Progress |
|-----|---------------------|----------|--------|----------|
| 0 | 0 | 0 | Running (PID 884787) | 12/1107, sr=8/12 (66.7%) |
| 1 | 1 | 1 | Running (PID 885185) | 13/1107, sr=9/13 (69.2%) |
| 4 | 4 | 2 | Running (PID 885703) | 9/1107, sr=7/9 (77.8%) |

All 3 jobs running with `--part_num 3`, each processing 1107 tasks. No additional submission needed — v9 is in progress.

---
