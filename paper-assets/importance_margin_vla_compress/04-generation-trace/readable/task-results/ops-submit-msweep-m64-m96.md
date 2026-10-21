# ops submit msweep m64 m96

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit-msweep-m64-m96_20260520T033510_result.json`
- **Structured JSON:** [`32cbc7dbbd43a1553ea1.json`](../../sessions/32/32cbc7dbbd43a1553ea1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments are successfully launched and verified. Here's the summary:

**westd-41074 GPU allocation:**
| GPU | Experiment | PID | Status |
|-----|-----------|-----|--------|
| cuda:0 | M=128 VTC-only | 26118 | Training (ongoing) |
| cuda:2 | M=96 `train_openvla_sc_m96_seed42` | 68539 | Computing action stats (~10 min), then training starts |
| cuda:3 | M=64 `train_openvla_sc_m64_seed42` | 68852 | Computing action stats (~10 min), then training starts |

**What was done:**
1. **Diagnosed previous failure**: The earlier M=64/M=96 runs were NOT config/path failures — they were SIGTERM'd (killed) and restarted as ad-hoc processes writing to `/tmp/`. Those ad-hoc runs had wrong output_dir naming (no `_seed42` suffix).
2. **Fixed**: Killed ad-hoc processes, updated config output_dirs to `checkpoints/openvla_sc_m{96,64}_seed42`, relaunched with proper nohup + persistent log files.
3. **Note**: The script doesn't accept `--output_dir` / `--seed` as CLI args — those must be set in the YAML config.
4. **Registry**: Both updated to RUNNING with full provenance spec.
5. **Logs**: `logs/train_openvla_sc_m96_seed42.log` and `logs/train_openvla_sc_m64_seed42.log` — no errors, model/dataset loaded correctly.

Training steps should appear in logs ~10 min after launch (after action stats computation). Previous runs at these M values showed healthy loss curves (M=64 loss ~3.4, M=96 loss ~4.0 at step 400).

---
