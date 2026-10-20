# code tau sweep script

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tau_sweep_script_20260515T093913_result.json`
- **Structured JSON:** [`58f334c98e142bc44b30.json`](../../sessions/58/58f334c98e142bc44b30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个脚本已创建并验证通过。

| 脚本 | `--tau` | `--output_dir` |
|------|---------|-----------------|
| `training/run_tau_0.5_seed42.sh` | 0.5 | `output/models/tau_0.5_seed42` |
| `training/run_tau_0.6_seed42.sh` | 0.6 | `output/models/tau_0.6_seed42` |
| `training/run_tau_0.7_seed42.sh` | 0.7 | `output/models/tau_0.7_seed42` |
| `training/run_tau_0.9_seed42.sh` | 0.9 | `output/models/tau_0.9_seed42` |
| `training/run_tau_0.95_seed42.sh` | 0.95 | `output/models/tau_0.95_seed42` |

所有脚本已 `chmod +x`，可直接提交运行。第一优先级 `run_tau_0.6_seed42.sh` 已就绪。

---
