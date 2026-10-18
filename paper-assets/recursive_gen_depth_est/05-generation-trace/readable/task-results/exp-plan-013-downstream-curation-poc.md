# exp plan 013 downstream curation poc

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan_013_downstream_curation_poc_20260515T213758_result.json`
- **Structured JSON:** [`b3dd679f0688fea63d6c.json`](../../sessions/b3/b3dd679f0688fea63d6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full 40-run finetune job is running. Summary:

**Dry run result:** unfiltered/seed_42 → PPL=15.74, train_loss=1.655, 419s

**Full job status:**
- PID: **364466** on gpu-6000pro-2 (cuda:1)
- Log: `/tmp/finetune_full.log`
- Run 1 skipped (reusing dry run), Run 2 (unfiltered/seed_123) training at ~3.9 it/s
- ETA: **~3.5-4 hours** (39 remaining runs × ~5-6 min each)
- Registry: `downstream_curation_poc_001` → RUNNING

**After completion**, run:
```bash
# Analyze phase (statistical comparison)
python src/curation_poc.py --phase analyze

# Check results
cat results/curation_poc/summary.json
```

Monitor progress with:
```bash
# Check which runs are done
grep -E "PPL=|SKIP|/40\]" /tmp/finetune_full.log
# Check if still running
ps -p 364466 -o pid=
```

---
