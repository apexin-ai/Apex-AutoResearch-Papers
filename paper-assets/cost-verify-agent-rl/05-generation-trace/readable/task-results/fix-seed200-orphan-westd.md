# fix seed200 orphan westd

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_seed200_orphan_westd_20260522T184832_result.json`
- **Structured JSON:** [`ac9a073c2429127395d8.json`](../../sessions/ac/ac9a073c2429127395d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### seed200 — 已清理

| 项目 | 详情 |
|------|------|
| **训练进度** | step 2/5 (40%)，最后日志 ~02:31，此后无新输出 |
| **训练指标** | step 1: success=17.97%, pass@8=68.75% / step 2: success=15.63%, pass@8=68.75% |
| **Checkpoint** | **无**，目录 `/root/autodl-tmp/checkpoints/exp029-seed200/` 不存在 |
| **已 kill 进程** | 63675 (bash launcher), 64789 (raylet), 66207 (TaskRunner), 66567/66568 (WorkerDict GPU 2,3), 69739 (wandb-core), 64851 (RuntimeEnvAgent), 64313/69371 (resource trackers) |
| **GPU 2,3** | 已释放，0 MiB / 0% 利用率 |

### seed100 — 正常运行

| 项目 | 详情 |
|------|------|
| **主进程** | PID **72007** (`python train.py --config-name _alfworld_exp029_seed100_episode`)，PPID=1 |
| **进程树** | 72007 → raylet 73132 → TaskRunner 78400 + WorkerDict 78937 (GPU 0) / 78938 (GPU 1) |
| **当前阶段** | step 1 训练中，GPU 进程显示 `ref_compute_ref_log_prob`（ref 对数概率计算，update_actor 之前） |
| **已完成步数** | 0（step 0 初始 eval 已完成，step 1 尚未完成） |
| **GPU 0,1** | 100% 利用率，各 ~47GB 显存 |
| **Checkpoint** | 目录尚未创建 |
| **wandb** | run `zsrodv2f` — exp029-seed100-episode-level |

### 磁盘

```
/dev/md0   250G  111G  140G  45%  /root/autodl-tmp
```

---
