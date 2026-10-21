# fix cuda visible devices scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cuda_visible_devices_scripts_20260516T110327_result.json`
- **Structured JSON:** [`3f2657991008a1681184.json`](../../sessions/3f/3f2657991008a1681184.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

**已添加 `export CUDA_VISIBLE_DEVICES=N`：**
| 脚本 | GPU |
|------|-----|
| `run_threshold_q03_seed42.sh` | 3 |
| `run_threshold_q07_seed42.sh` | 0 |
| `run_threshold_q07_resume.sh` | 0 |

**已有 CUDA_VISIBLE_DEVICES（无需修改）：**
| 脚本 | GPU |
|------|-----|
| `run_batch_adaptive_tau_rho04_seed42.sh` | 2 |
| `run_eval_seed42.sh` | (已有) |
| `run_random_reweight_seed42.sh` | (已有) |
| `run_rho02_uniform_seed42.sh` | (已有) |

**已添加 TODO 注释（GPU 未固定）：**
- `run_batch_adaptive_tau_rho06_seed42.sh`
- `run_hybrid_rho04_seed42.sh`
- `run_bs8_auto_nmin_seed42.sh`
- `run_rho02_adaptive_tau09_seed42.sh`

---
