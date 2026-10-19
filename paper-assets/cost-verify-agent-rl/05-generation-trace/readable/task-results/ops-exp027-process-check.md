# ops exp027 process check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp027_process_check_20260515T143606_result.json`
- **Structured JSON:** [`2a9d5c1876a5b834ae7f.json`](../../sessions/2a/2a9d5c1876a5b834ae7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp027_stable_grpo 状态

| 项目 | 状态 |
|------|------|
| **PID 789764** | 存活，启动于 22:33（约 3 分钟前） |
| **tmux session** | `exp027_stable_grpo` 存在 |
| **GPU 占用** | GPU 0: 41598 MiB, GPU 1: 41390 MiB（两卡均在使用） |
| **W&B** | 已创建 run `exp027-alfworld-stable-grpo` (ID: y7jiibqk)，正在同步 |
| **训练主进程** | `python train.py --config-name _alfworld_exp027_stable_grpo` (PID 789790) |
| **Ray workers** | 2 个 `actor_rollout_generate_sequences` worker 在运行（CPU 75%+），多个 IDLE worker 就绪 |

**日志最后内容**：W&B 初始化完成，数据集 tokenize 完成（8810 条 + 494 条），训练即将开始第一个 step。当前处于 **正常启动阶段**，尚未产出训练 metrics。

---
