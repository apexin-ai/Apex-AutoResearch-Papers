# ops fix checkpoint rotation 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_checkpoint_rotation_34685_20260524T041644_result.json`
- **Structured JSON:** [`fee37999e9bb2b15a280.json`](../../sessions/fe/fee37999e9bb2b15a280.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

### 磁盘变化
| | Used | Avail | Use% |
|---|---|---|---|
| 修复前 | 289G | 62G | 83% |
| 修复后 | 259G | 92G | 74% |

### 删除的 checkpoint（共 30GB）
- `cutoff_45k_s0/...10000_chkpt` — 15GB
- `cutoff_15k_s0/...10000_chkpt` — 15GB

### Rotation 脚本
- **不是 cron**，是 while-true + sleep 300 的后台循环（PID 694641）
- 旧脚本（PID 151027，监控 `cutoff_s0/s1 depth_s0/s1`）已停止
- 新脚本覆盖 5 个活跃实验：`cutoff_45k_s0`、`cutoff_15k_s0`、`cutoff_25k_s1`、`reverse_cutoff_s1`、`vanilla_retrain_s0`
- 保留最新 2 个 checkpoint，有进程保护（不会删除正在被训练加载的 checkpoint）
- 日志写入 `/root/rotation.log`

### 旧实验 checkpoint（未删除，仅报告）
- `cutoff_25k_s0`: 3 个 checkpoint (45GB) — 30000/40000/50000
- `reverse_cutoff_s0`: 3 个 checkpoint (45GB) — 30000/40000/50000
- `full_occ_retrain_s0`/`vanilla_retrain_s0`/`ablation_occ_detach_s2`/`ablation_random_occ_s2`: 各 1 个 50000 checkpoint (共 60GB)

如果旧实验 `cutoff_25k_s0` 和 `reverse_cutoff_s0` 的中间 checkpoint (30000/40000) 不再需要，删除可再释放 60GB。

---
