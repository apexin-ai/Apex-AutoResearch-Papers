# ops westd urgent disk cleanup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_urgent_disk_cleanup_20260522T163005_result.json`
- **Structured JSON:** [`47108fb69b61d0051774.json`](../../sessions/47/47108fb69b61d0051774.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

seed200 训练成功启动。

---

## 汇总

### 磁盘清理

| 操作 | 释放空间 |
|------|---------|
| intervention-c-hard-cap (FSDP) | **41G** |
| exp029-seed6 (FSDP) | **25G** |
| exp029-seed8 (FSDP) | **21G** |
| exp029_new_seed_2048 (FSDP) | **25G** |
| cost-verify-agent-rl/backups/exp029-seed2-bjb1 | **21G** |
| exp029-seed4 (FSDP) | **3.8G** |
| wandb + ray_tmp + tmp + eval_results + /tmp/ray* | **~1G** |

| | 磁盘 |
|--|------|
| **清理前** | 240G/250G (96%), 11G 可用 |
| **清理后** | 105G/250G (42%), **146G 可用** |

### seed200 重启

- **PID**: 999987 (nohup), TaskRunner pid=7472
- **GPU**: cuda:2, cuda:3 (4731 MiB 已加载)
- **W&B run**: `exp029-seed200-episode-level` (ID: z7e85fie)
- **日志**: `/root/autodl-tmp/logs/seed200_episode_grpo.log`
- **配置**: seed=200, 5 steps, GRPO episode-level, val_before_train=True
- 当前状态：环境初始化完成 (494/494)，即将进入 val_before_train

---
