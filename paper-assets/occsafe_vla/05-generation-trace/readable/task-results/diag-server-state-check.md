# diag server state check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_server_state_check_20260520T092535_result.json`
- **Structured JSON:** [`afd2755a0c196dd8ae9b.json`](../../sessions/af/afd2755a0c196dd8ae9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**三个实验全部在正常训练中，registry 状态滞后。**

### 训练进程状态

| 实验 | PID | GPU | VRAM | 启动时间 | 当前 Step | 速度 | tmux session |
|------|-----|-----|------|----------|-----------|------|-------------|
| vanilla_s0 | 100203 | GPU 0 | 63.0 GB | 17:22 | **178**/50005 | ~1.02s/it | vanilla_s0 (pts/0) |
| vanilla_s1 | 97847 | GPU 1 | 62.2 GB | 17:20 | **277**/50005 | ~1.06s/it | vanilla_s0 (pts/1) |
| vanilla_s2 | 98174 | GPU 2 | 62.2 GB | 17:20 | **274**/50005 | ~1.04s/it | vanilla_s0 (pts/2) |

GPU 利用率：GPU 0 35%, GPU 1 42%, GPU 2 99%, GPU 3 空闲。

### extract_occupancy.py 进程

10 个进程在跑（task_id 0-9），全部在 CPU 上运行，每个占 ~2.4 GB RAM，每个在 GPU 0 上占 557 MiB VRAM（总计 ~5.6 GB）。从 15:23 起运行至今。

### 磁盘

`/root/autodl-tmp`: 37G / 250G used, **214G 可用 (15%)**，充足。

### 结论

三个实验**确实在训练**，自动重试成功。s1/s2 于 17:20 启动，s0 晚 2 分钟于 17:22 启动，目前 s1/s2 已跑约 275 步，s0 约 178 步。按当前速度 (~1.05s/step)，50005 步预计总耗时约 **14.5 小时**，大约在明天 08:00 左右完成。Registry 的 DONE(failed) 状态需要更新。

---
