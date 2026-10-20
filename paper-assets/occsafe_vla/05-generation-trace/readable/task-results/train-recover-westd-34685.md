# train recover westd 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_recover-westd-34685_20260522T073429_result.json`
- **Structured JSON:** [`cf43fdb7fceaef4311a6.json`](../../sessions/cf/cf43fdb7fceaef4311a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务已由其他 Worker 提前完成。汇报如下：

---

## 汇报

### 1. 补充清理情况

**无需额外清理。** 紧急清理 Worker 已删除所有需要清理的内容：

| 目标 | 状态 |
|------|------|
| occ_s1_fresh 中间 checkpoint | 已清理，仅剩 47500_chkpt + 50000_chkpt（30G） |
| depth_s0 所有 checkpoint | **全部被删**（包括 12500_chkpt），目录只剩 dataset_statistics.json（4K） |
| depth_s1 所有 checkpoint | **全部被删**（同上） |
| cutoff_s1 目录 | 已清理，仅剩 dataset_statistics.json（4K） |

**关键问题**：depth_s0/s1 的 12500_chkpt 也被紧急清理误删了，无法从 12500 resume，只能从头重跑。

### 2. 最终磁盘状态

```
/dev/md127  350G  66G used  285G available  19%
```

### 3. 4 个实验状态（全部正在运行）

| 实验 | GPU | PID (tmux) | PID (python) | 当前 step | 启动方式 | master_port |
|------|-----|-----------|-------------|-----------|---------|------------|
| cutoff_s0 | cuda:0 | 125522 | 125602 | ~3306 | 从头跑（14:32 启动） | 默认 |
| depth_s0 | cuda:1 | 131535 | 131615 | ~128 | **从头重跑**（15:33 启动） | 29501 |
| depth_s1 | cuda:2 | 131682 | 131829 | ~128 | **从头重跑**（15:33 启动） | 29502 |
| cutoff_s1 | cuda:3 | 131898 | 132048 | ~126 | **从头重跑**（15:33 启动） | 29503 |

- 所有 4 个 GPU 均分配 62GB 显存
- 速度 ~1.08 it/s
- save_freq：cutoff_s0 = 2500，其余 3 个 = 10000
- WANDB_MODE=disabled（3 个重跑的实验）
- tmux session 和 registry 条目均已存在

### 4. cutoff_s0 当前 step

**step ~3306/50005**（6.6%），启动于 14:32，已跑约 1 小时。

---
