# monitor exp029 gpu check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp029_gpu_check_20260516T192410_result.json`
- **Structured JSON:** [`34f3b179f444f56dba38.json`](../../sessions/34/34f3b179f444f56dba38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029_episode_level 状态报告

| 项目 | 状态 |
|------|------|
| **进程** | PID 896477 存活，运行 2h58m，状态 Ss+ |
| **GPU 0** | 36683/97887 MiB (37%), util 0% |
| **GPU 1** | 36679/97887 MiB (37%), util 0% |
| **GPU 占用进程** | PID 899940 (GPU0, 36674 MiB), PID 899941 (GPU1, 36670 MiB) — 均为本实验 worker，无抢占 |
| **W&B run** | `exp029-alfworld-episode-level` / `ugkd8ys1` |

**当前阶段**: 初始化完毕，正在进入第一轮 rollout。日志显示：
- 模型加载完成（checkpoint shards 100%）
- FSDP worker 已初始化（2 GPU）
- W&B 连接成功
- 训练数据集 tokenize 完成（8810/8810 + 494/494）
- **尚未出现 step/train metrics 或 val_before_train 输出**

GPU 利用率 0% + 显存已占 37% 表明模型已加载到显存，当前可能正在执行 val_before_train 的 environment rollout（CPU-bound ALFWorld 交互阶段，GPU 空闲是正常的）。日志文件仍在增长中（200KB, timestamp 更新中），进程树正常。

**结论**: 正常运行，处于首轮 evaluation/rollout 阶段，预计产出第一条 metrics 还需一段时间。

---
