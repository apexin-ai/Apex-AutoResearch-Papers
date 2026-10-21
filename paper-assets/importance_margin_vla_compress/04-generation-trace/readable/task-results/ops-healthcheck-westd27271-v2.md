# ops healthcheck westd27271 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_healthcheck-westd27271-v2_20260524T093523_result.json`
- **Structured JSON:** [`3dae9244310b0302e3eb.json`](../../sessions/3d/3dae9244310b0302e3eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 健康检查报告 — westd-27271

### GPU 状态总览

| GPU | PID | 实验ID | Suite | Status | 运行时间 | 显存 | GPU-Util |
|-----|-----|--------|-------|--------|----------|------|----------|
| 0 | 676491 | eval_openvla_attn_k05_object_seed42_v2 | libero_object | **RUNNING** (Task 5/10) | 2h47m | 15.9/97.9 GB | 68% |
| 1 | 675522 | eval_openvla_attn_k05_goal_seed42 | libero_goal | **RUNNING** (Task 7/10) | 2h49m | 15.9/97.9 GB | 67% |

### 当前运行进度

**GPU 0 — Object suite (v2 重跑)**
- Tasks 1-4 完成，全部 0% SR（与之前 v1 结果一致）
- Task 5/10 进行中
- 预估剩余 ~3h（按 1.5 eps/min）

**GPU 1 — Goal suite**
- Tasks 1-6 完成：14%, 56%, 70%, 10%, 62%, 66%
- Task 7/10 进行中（ep 20/50, 当前 9/20）
- 预估剩余 ~1.5h

### 已完成结果文件（本地已存储）

| 文件 | Mode | Suite | SR | Episodes | 时间戳 |
|------|------|-------|----|----------|--------|
| `openvla_attention_prune_k05_object_seed42.json` | attention_prune k=0.5 | libero_object | **0.0%** | 500 | 13:45 (v1, 旧) |
| `openvla_l2norm_prune_k05_goal_seed42.json` | l2norm_prune k=0.5 | libero_goal | **43.4%** | 500 | 12:25 |
| `openvla_random_prune_k05_goal_seed42.json` | random_prune k=0.5 | libero_goal | **52.2%** | 500 | 12:56 |
| `openvla_baseline_10_seed42.json` | baseline (no prune) | libero_10 | **52.8%** | 500 | 07:43 |

### 未注册进程

**无未注册任务。** 除了两个已注册实验进程外，只有系统级 tensorboard (PID 904) 和 jupyter-lab (PID 907)。无 tmux session。

Director 报告的"未注册任务"可能是之前 v1 的 object 评估（13:45 完成写入 JSON，之后 14:48 启动了 v2 重跑）——那次运行已结束并被 v2 替代。

### 关键发现

- Attention pruning k=0.5 在 Object suite 上完全失效（0.0%），v2 重跑中也延续相同趋势
- Goal suite: attention (当前运行中) vs l2norm (43.4%) vs random (52.2%) — random 意外优于 l2norm

---
