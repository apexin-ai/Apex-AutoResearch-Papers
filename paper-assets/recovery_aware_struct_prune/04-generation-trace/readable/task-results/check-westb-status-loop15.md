# check westb status loop15

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westb_status_loop15_20260516T200506_result.json`
- **Structured JSON:** [`07073d24d0bba4f33eb4.json`](../../sessions/07/07073d24d0bba4f33eb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 服务器状态汇报

### 1. GPU 使用

| GPU | 型号 | 显存占用 | GPU利用率 | 状态 |
|-----|------|---------|----------|------|
| cuda:0 | RTX PRO 6000 Blackwell | 28.9/97.9 GB | 94% | **占用** — eval_grpo_rasp_25 |
| cuda:1 | RTX PRO 6000 Blackwell | 71.7/97.9 GB | 100% | **占用** — grpo_rasp_rlvr_20 训练 |

**两张 GPU 均满载，无空闲。**

### 2. 活跃实验

| 实验 | PID | GPU | 进度 | 状态 |
|------|-----|-----|------|------|
| **grpo_rasp_rlvr_20** | 635524 | cuda:1 | 13/100 steps (13%), ~1h28m已跑 | **运行中**，约还需 9h48m |
| **eval_grpo_rasp_25** | 639423 | cuda:0 | 46/1319 samples (3%), ~18min已跑 | **运行中**，tmux session `eval_grpo_rasp_25` |

### 3. grpo_standard_20_v8 / grpo_rasp_20_v8 状态

- PID 534667, 532861: **已死亡**（不在进程列表中）
- 日志文件: `~/runs/` 下**不存在** v8 日志，`/root/autodl-tmp/` 下也无 v8 相关文件
- **grpo_stage2_standard_20_v8/**: 存在，有 `checkpoint-50`（May 16 05:42）和 `completions/`（May 16 09:07）
- **grpo_stage2_rasp_20_v8/**: **不存在**

结论：v8 实验进程已死，standard_20_v8 保存了 1 个 checkpoint，rasp_20_v8 无产出。

### 4. tmux sessions

- `eval_grpo_rasp_25` — 1 个 session（May 17 03:45 创建）

### 5. 磁盘空间

| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| /root/autodl-tmp/ | 250G | 223G | 28G | **89%** |

数据盘还剩 28G，较紧张。

---
