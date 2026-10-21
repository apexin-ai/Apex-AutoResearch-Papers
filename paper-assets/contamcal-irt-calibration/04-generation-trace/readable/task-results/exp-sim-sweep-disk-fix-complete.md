# exp sim sweep disk fix complete

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_sim-sweep-disk-fix-complete_20260515T082940_result.json`
- **Structured JSON:** [`bf30c7286a2b465c9837.json`](../../sessions/bf/bf30c7286a2b465c9837.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Summary of what was done:**

1. **Disk diagnosis**: Root partition at 64% (11G free), no longer full. Original failures were from CmdStan temp files filling root `/tmp/`.

2. **TMPDIR fix**: Created `/root/autodl-tmp/tmp_sim/` and launched sweep with `TMPDIR=/root/autodl-tmp/tmp_sim`. Verified temp files now go to data disk.

3. **N=8 added**: Modified SUBSET config in `run_sweep.py` to include `n_models=8` alongside `[20, 50, 100]`.

4. **Sweep launched**: `python run_sweep.py subset --resume --chains-parallel 1 --parallel 4` (PID 528380). With `--resume`, it skips 7 already-complete conditions and processes 9 remaining ones:
   - 4 new N=8 conditions (D039)
   - 3 AUC=0.65 conditions (all failed from disk quota)
   - auc0.55_n100 (2 seeds remaining)
   - auc0.9_n100 (8 seeds remaining)

5. **Log**: `/root/autodl-tmp/sweep_resume.log`

Estimated completion: ~10-11 hours from now (bottleneck is `auc0.65_n100` at ~9.3hr serial). You can monitor with:
```
grep "DONE" /root/autodl-tmp/sweep_resume.log
grep -c '"success": true' /root/contamcal-irt-calibration/exp004_sim_sweep/results/&lt;condition>.json
```

---
