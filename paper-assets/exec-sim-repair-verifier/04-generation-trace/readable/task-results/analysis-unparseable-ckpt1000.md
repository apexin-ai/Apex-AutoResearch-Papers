# analysis unparseable ckpt1000

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_unparseable-ckpt1000_20260515T165712_result.json`
- **Structured JSON:** [`01f170eee3319ce3b05e.json`](../../sessions/01/01f170eee3319ce3b05e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the complete picture:

## Unparseable Data — What Exists

**No val eval with unparseable tracking exists for ckpt-1000 (or any checkpoint 200-1600).** The previous val sweep only recorded accuracy, not unparseable counts (`n_cls_unparseable: None` in `compile_val_sweep.py`).

Available unparseable data from other eval runs:

| Checkpoint | Split | seq_len | n_instances | unparseable | rate |
|-----------|-------|---------|-------------|-------------|------|
| ckpt-200 (different ckpt path¹) | test | 2048 | 9784 | 136 | 1.4% |
| ckpt-800 (s42) | test | 8192 | 9784 | 0 | 0.0% |
| ckpt-1400 (s42) | test | 8192 | 9784 | 0 | 0.0% |
| ckpt-1800 (s42) | val | 2048 | 9335 | 1883 | 20.2% |

¹ `checkpoints_repo_cls_8b` not `checkpoints_repo_cls_8b_s42_resume`

## Key Confound

The ckpt-1800 eval used **seq_length=2048**, while ckpt-800/1400 used **seq_length=8192**. The 20.2% unparseable could be caused by truncation at seq=2048, not overfitting.

## Extended Val Sweep Status

`run_extended_val_sweep.sh` was launched to re-evaluate at seq=8192 with unparseable tracking, but **crashed at 560/9335 on ckpt-1800** (log stopped ~43 minutes ago at 22:16). No results were saved. The ckpt-1800 val prediction files that previously existed have also been deleted.

## What's Needed

To get the comparison you want, we need to either:
1. Re-run the extended sweep (fix whatever crashed it) to get all checkpoints at seq=8192 with unparseable tracking
2. Or at minimum: run `eval_repo_cls.py` on ckpt-1000 and ckpt-1800 with **identical settings** (same split, same seq_length)

Want me to investigate the crash and re-launch the sweep, or just run ckpt-1000 specifically?

---
