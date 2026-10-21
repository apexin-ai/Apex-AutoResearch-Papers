# ssh fix scripts and verify 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_scripts_and_verify_30476_20260517T102753_result.json`
- **Structured JSON:** [`5995e3bb402ce273aa1f.json`](../../sessions/59/5995e3bb402ce273aa1f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary:

| Script | output_dir | eval_steps | WANDB_MODE | CUDA_VISIBLE_DEVICES |
|--------|-----------|-----------|-----------|---------------------|
| `run_bs8_auto_nmin_seed42.sh` | `/dev/shm/output/models/bs8_auto_nmin_seed42/` | CLEAN | disabled | comment only |
| `run_batch_adaptive_tau_rho06_seed42.sh` | `/dev/shm/output/models/batch_adaptive_tau_rho06_seed42/` | CLEAN | disabled | comment only |
| `run_rho02_adaptive_tau09_seed42.sh` | `/dev/shm/output/models/rho02_adaptive_tau09_seed42/` | CLEAN | disabled | comment only |

All 3 scripts updated. Also removed `eval_steps` and `eval_data_path` lines that violated M003 constraints. `/dev/shm/output/models` directory created.

---
