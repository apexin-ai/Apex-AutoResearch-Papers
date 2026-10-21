# code fix occ dataloader

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-occ-dataloader_20260520T080215_result.json`
- **Structured JSON:** [`d78d0ad90d34741491e0.json`](../../sessions/d7/d78d0ad90d34741491e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 tests passed:

| Test | Scenario | Result |
|------|----------|--------|
| 1 | traj_len=93 (matches demo_0), timestep=5 | nonzero=1016 (24.8%) |
| 2 | timestep=30, same demo | nonzero=960 |
| 3 | traj_len=88 → demo_2 selection | nonzero=1016 |
| 4 | Unknown task → zeros fallback | nonzero=0 |
| 5 | No `_traj_len` → positional fallback | nonzero=1016 |
| 6 | Bytes language instruction (TF format) | nonzero=1016 |

The `_load_occ_label` method correctly:
- Maps language instruction → task_name → occ file
- Selects demos by trajectory length matching
- Falls back gracefully for unknown tasks (zeros + warning)
- Handles both string and bytes language instructions
- Works with and without `_traj_len`

**Remaining**: Full verification with real pipeline data is blocked until the 10 `extract_occupancy.py` processes finish (all 10 HDF5 files locked; each task on ~demo 2 of 50). At the current rate with 10 parallel CPU-bound processes plus 3 training jobs, this will take many more hours. Once the pipeline finishes, switch `occ_data_dir` from `occ_data_test` to `occ_data` and re-run to confirm non-zero BEV with real data:

```bash
cd /root/occsafe_vla/openvla-oft && python /root/occsafe_vla/verify_occ_fix.py
```

---
