# infra westd 34685 cleanup and status

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-34685-cleanup-and-status_20260521T150106_result.json`
- **Structured JSON:** [`7d8ee50e1184a6c3a2b4.json`](../../sessions/7d/7d8ee50e1184a6c3a2b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全了。以下是结构化报告：

---

## westd-34685 服务器状态报告

### GPU 状态

| GPU | Utilization | Memory Used | Memory Total | 状态 |
|-----|------------|-------------|--------------|------|
| 0 | 99% | 62,203 MiB | 97,887 MiB | **occ_s1_fresh 训练中** |
| 1 | 2% | 16,778 MiB | 97,887 MiB | **occ_s0 50r eval 运行中** |
| 2 | 0% | 16,778 MiB | 97,887 MiB | **occ_s2 50r eval 运行中** |
| 3 | 0% | 1 MiB | 97,887 MiB | **空闲，已恢复正常**（之前报告物理卡死，现在 0% util / 1 MiB，正常空闲状态） |

### 运行中的进程

| PID | GPU | 任务 | 进度 |
|-----|-----|------|------|
| 487053 | cuda:0 | occ_s1_fresh finetune (seed=43, max_steps=50005) | **step 711/50005 (1.4%)**，~1.09 it/s，ETA ~12.5h |
| 482355 | cuda:1 | occ_s0 47500 chkpt 50r eval | **Task 3, rollout 32/50 (约 30% 总进度)** |
| 491669 | cuda:2 | occ_s2 47500 chkpt 50r eval | **Task 2, rollout 11/50 (约 22% 总进度)** |

### occ_s1_fresh 训练详情
- 刚启动不久，step 700 时 loss: `occ_loss=0.0239, action_loss=0.2656`
- checkpoint 目录 `/root/autodl-tmp/checkpoints/occ_s1_fresh/` 已创建，含 `dataset_statistics.json`，尚未保存 checkpoint（首次保存在 step 2500）

### tmux 清理
- `occ_s1_fresh` session 已清理（kill-session 执行成功）
- 当前无任何 tmux session 残留
- 训练和 eval 进程均以 nohup/后台方式运行，不依赖 tmux

### 磁盘
| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| /root/autodl-tmp | 350G | 172G | 179G | 49% |

### 已有的 eval 结果文件（eval_results 目录）
- `occ_s0_final.json` — 20r eval, TSR=0.915, CAR=0.800
- `occ_s0_50000.json` — 20r eval for 50000 chkpt
- `occ_s2_final.json` / `occ_s2_50000.json` — 20r evals
- `vanilla_s0_50r.json` / `vanilla_s1_50r.json` — vanilla baseline 50r 已完成

### 异常
- **无异常。** cuda:3 已恢复正常（不再卡死），所有进程稳定运行。

---
