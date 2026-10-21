# ops check westd eval results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_westd_eval_results_20260517T090042_result.json`
- **Structured JSON:** [`6d06b4beb10b0f65834f.json`](../../sessions/6d/6d06b4beb10b0f65834f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. eval_random_prune_k05 (已完成)

| Task | Description | SR |
|------|------------|-----|
| 0 | alphabet soup → basket | 0/50 (0%) |
| 1 | cream cheese → basket | 0/50 (0%) |
| 2 | salad dressing → basket | 0/50 (0%) |
| 3 | bbq sauce → basket | 0/50 (0%) |
| 4 | ketchup → basket | 0/50 (0%) |
| 5 | tomato sauce → basket | 0/50 (0%) |
| 6 | butter → basket | 0/50 (0%) |
| 7 | milk → basket | 0/50 (0%) |
| 8 | chocolate pudding → basket | 0/50 (0%) |
| 9 | orange juice → basket | 0/50 (0%) |

**Overall SR: 0/500 (0.0%)**。随机剪枝 50% token 后模型完全丧失能力。

### 2. eval_stage1only_k09 (已完成)

| Task | Description | SR |
|------|------------|-----|
| 0–9 | (同上 10 个 object tasks) | 全部 0/50 (0%) |

**Overall SR: 0/500 (0.0%)**。仅用 stage1 checkpoint + ACIS prune k=0.9（保留 90% token）也完全失败。

### 3. eval_true_removal_k05 (运行中)

- 当前进度：**Task 4, Ep 40/50**（已完成 task 0-3，正在跑 task 4）
- 已完成 4 个 task 的 SR 均为 0%
- 进度约 **44%**（~240/500 episodes 完成）
- 按每 task ~4 分钟估算，剩余 6 个 task 约 **24 分钟**完成

### 4. GPU 状态

| GPU | 型号 | 显存占用 | GPU-Util | 温度 |
|-----|------|---------|----------|------|
| 0 | RTX PRO 6000 Blackwell | 2248/97887 MiB | 1% | 35°C |
| 1 | RTX PRO 6000 Blackwell | 3047/97887 MiB | 0% | 35°C |

一个 python 进程 (PID 261666) 占用双卡，就是 true_removal eval。GPU 利用率低是因为 eval 主要是 CPU-bound 的 sim 环境交互。

### 小结

三个 pruning baseline 实验（random prune k=0.5, stage1only k=0.9, true removal k=0.5）在 libero_object 上 SR 全部为 **0%**。这说明不经过 stage2 fine-tuning，无论是随机剪枝还是 importance-based 剪枝，直接在推理时 prune token 都会导致模型彻底崩溃。

---
