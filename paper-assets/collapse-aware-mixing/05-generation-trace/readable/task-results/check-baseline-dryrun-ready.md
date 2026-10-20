# check baseline dryrun ready

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_baseline_dryrun_ready_20260513T202351_result.json`
- **Structured JSON:** [`9e35fc4f5ffd42c63955.json`](../../sessions/9e/9e35fc4f5ffd42c63955.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== BASELINE DRY-RUN ===
Scripts: 6/6 exist
Import: OK
Argparse: OK

Per-script params:
| Script              | w_init | w_min | w_max | Kp | Ki | output_dir                          |
|---------------------|--------|-------|-------|----|----|-------------------------------------|
| launch_baseline_w0  | 0.0    | 0.0   | 0.0   | 0  | 0  | /root/autodl-tmp/output_p0/baseline_w0  |
| launch_baseline_w01 | 0.1    | 0.1   | 0.1   | 0  | 0  | /root/autodl-tmp/output_p0/baseline_w01 |
| launch_baseline_w03 | 0.3    | 0.3   | 0.3   | 0  | 0  | /root/autodl-tmp/output_p0/baseline_w03 |
| launch_baseline_w05 | 0.5    | 0.5   | 0.5   | 0  | 0  | /root/autodl-tmp/output_p0/baseline_w05 |
| launch_baseline_w07 | 0.7    | 0.7   | 0.7   | 0  | 0  | /root/autodl-tmp/output_p0/baseline_w07 |
| launch_baseline_w1  | 1.0    | 1.0   | 1.0   | 0  | 0  | /root/autodl-tmp/output_p0/baseline_w1  |

Common params: model=pythia-1b, lr=2e-6, 3 gens × 20M tokens, ckpt every 5M, seed=42, --no_wandb
All scripts: Kp=0, Ki=0, w_init=w_min=w_max ✓

GPU status: 1× NVIDIA RTX PRO 6000 Blackwell (96GB), 3 MiB used, 0% util — idle, no training running
Issues: None — all scripts ready to launch
```

---
