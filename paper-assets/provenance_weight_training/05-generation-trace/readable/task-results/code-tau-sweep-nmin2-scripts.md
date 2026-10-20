# code tau sweep nmin2 scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_tau_sweep_nmin2_scripts_20260516T012332_result.json`
- **Structured JSON:** [`6123eb149dcf61b7523b.json`](../../sessions/61/6123eb149dcf61b7523b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 结果汇总

| 脚本 | τ | 路径 |
|------|---|------|
| `run_tau_05_nmin2.sh` | 0.5 | `/root/provenance_weight_training/scripts/run_tau_05_nmin2.sh` |
| `run_tau_06_nmin2.sh` | 0.6 | `/root/provenance_weight_training/scripts/run_tau_06_nmin2.sh` |
| `run_tau_07_nmin2.sh` | 0.7 | `/root/provenance_weight_training/scripts/run_tau_07_nmin2.sh` |
| `run_tau_09_nmin2.sh` | 0.9 | `/root/provenance_weight_training/scripts/run_tau_09_nmin2.sh` |
| `run_tau_095_nmin2.sh` | 0.95 | `/root/provenance_weight_training/scripts/run_tau_095_nmin2.sh` |

**验证结果：**
- `--n_min 2` 在 5 个脚本中均确认存在
- `data/scored_data.jsonl` 存在
- `models/Qwen/Qwen3-0.6B` 存在
- `--n_min` 参数被 `pretrain_weighted.py` 识别（默认值为 batch_size//2，显式设为 2 覆盖）
- 所有脚本已 `chmod +x`

---
