# ops prepare scienceworld v4c config

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare_scienceworld_v4c_config_20260522T042323_result.json`
- **Structured JSON:** [`9cabd0693aae678d993a.json`](../../sessions/9c/9cabd0693aae678d993a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

### 1. v4c config 已创建 ✓

### 2. 关键参数验证

| 参数 | 值 | 备注 |
|------|-----|------|
| env_groups (train, L94) | **1** | ✓ 从 8 改为 1 |
| group_size (train, L95) | **16** | 不变 |
| env_groups (eval, L100) | 32 | 未改（eval 部分） |
| experiment_name | `scienceworld-cell-c-v4c` | ✓ |
| local_log_dir | `/root/autodl-tmp/checkpoints/scienceworld-cell-c-v4c/` | ✓ |

总 rollouts per step: 1 × 16 = **16**（v4 为 8 × 16 = 128）。

### 3. v4b 当前状态

- **进程 386364**: 运行中，状态 `Ss+`，已运行 **14 分 18 秒**
- **日志**: TaskRunner 正在处理 `find-non-living-thing` 任务，输出 non-numeric metric 跳过警告（正常）
- **GPU**: cuda:0 = 4715 MiB, cuda:1 = 4717 MiB（v4b 正在使用）

---
