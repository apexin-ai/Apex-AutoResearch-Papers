# check westd full status v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-full-status-v2_20260514T110516_result.json`
- **Structured JSON:** [`4d24483b3a2c82460c42.json`](../../sessions/4d/4d24483b3a2c82460c42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇总

### GPU 占用

| GPU | 进程 | PID | 显存 | GPU利用率 |
|-----|------|-----|------|----------|
| cuda:0 | CWM seed123 eval (4B, ckpt-500) | 195531 | 12988/32607 MiB | 87% |
| cuda:1 | CWM v12 eval (4B, ckpt-500) | 195668 | 12988/32607 MiB | 88% |
| cuda:2 | CWM 8B 训练 (seed42) | 210573 | 31534/32607 MiB | 97% |
| cuda:3 | CLS 8B 训练 (seed123) | 210657 | 23596/32607 MiB | 61% |

### CWM Eval 进度

**无法直接获取进度** — 两个 eval 进程的 stdout 输出到 pipe（非文件），输出目录 `repo_cwm_seed123_conda_eval/` 和 `repo_cwm_v12_conda_eval/` 均为空。进程启动于 09:03，已运行 **~10 小时**。GPU 利用率 87-88% 说明仍在正常推理（非挂起），但 10 小时无输出文件有些异常（可能是脚本在最后才写文件，或者 batch_size=8 + max_new_tokens=1024 的生成确实很慢）。

### 8B CWM 训练 (GPU 2)

- **当前 step**: 800/6633 (12%)，正在做 step 800 的 eval（eval 进度 83%，7784/9335）
- **速率**: ~12s/step
- **最新 loss**: 1.4913 (epoch 0.36)
- **eval_loss**: 0.3174 (step 800)
- **ETA**: 纯训练剩余 ~19h，加上 eval 开销 → 预计还需 **24-30h**
- **Checkpoints**: 300, 400, 500, 600, 700

### 8B CLS seed123 训练 (GPU 3)

- **当前 step**: ~1562/6633 (23%)
- **速率**: ~8.2s/step
- **最新 loss**: 0.8878 (step 1550, epoch 0.70)
- **eval_loss 趋势**: 0.086→0.103→0.109→0.093→**0.415**→0.306→0.165（step 1000 有 spike，之后恢复下降）
- **ETA**: 纯训练剩余 ~11.5h + eval 开销 → 预计还需 **~17h**
- **Checkpoints**: 200, 400, 600, 800, 1000, 1200, 1400

### Checkpoint 备份

| 备份目录 | 已备份 checkpoints |
|---------|-------------------|
| checkpoints_backup_cls_8b_seed123 | 200, 800, 1000, 1200, 1400 (5个) |
| checkpoints_backup_cwm_8b | 300, 400, 500, 600, 700 (5个) |

`backup.log` 为空。`tmux ls` 无法通过 read_only 执行，无法确认 auto-backup session 状态。

### 磁盘

```
/root/autodl-tmp: 131G/250G used, 120G available (53%)
```

### 注意事项

1. **CWM eval 10h 无输出** — 建议确认进程是否正常。可以 `ssh_execute` 里 `tmux ls` 看 eval session 输出，或检查 eval 脚本是否在最后才写文件。
2. **CLS 8B eval_loss step 1000 spike** (0.093→0.415) — 已在后续恢复到 0.165，但需关注是否再次出现。

---
