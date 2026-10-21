# ops exp029 seed2 envgroups fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp029-seed2-envgroups-fix_20260518T093818_result.json`
- **Structured JSON:** [`cbca82cae39da939ddb0.json`](../../sessions/cb/cbca82cae39da939ddb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

"Evaluating with 140 games" — 已经进入 val_before_train 阶段了。这需要跑 32 个 val episodes（每个最多 50 turns），每 turn 需要 vLLM 生成。这可能需要 10-20 分钟。

OOM 发生在 training 的 backward pass，不是在 val 阶段。所以需要等 val 完成 + 第一个 training step 的 rollout + backward pass。整体可能需要 20-30 分钟。

当前状态总结已经足够汇报了。让我先给出中间汇报，然后继续监控。

---

## 汇报（中间状态）

### 1. env_groups 语义分析

**结论：env_groups 只控制数据生成并行度，不影响 GRPO advantage 计算。**

- `env_groups` = 环境分组数（不同 task/seed），决定每步生成多少个独立环境实例
- `group_size` = 每个 group 内的样本数，用于 GRPO advantage 归一化的分母
- GRPO advantage 按 `index`（=group_id）分组计算 mean/std，分母是 `group_size`（保持 8 不变）
- `train_batch_size = env_groups × group_size`：从 128→64
- Assertion 验证：`8 × 8 = 64 >= ppo_mini_batch_size(8)` ✓

### 2. 修改内容
- `es_manager.train.env_groups`: 16 → **8**
- `es_manager.train.env_configs.n_groups`: [16] → **[8]**
- 其余参数不变（group_size=8, ppo_mini_batch_size=8, gradient_checkpointing=true, optimizer_offload=true, seed.train=43）

### 3. 当前状态
- **PID**: 24047
- **GPU 显存**: 0: 4715 MiB, 1: 4715 MiB（初始化阶段）
- **阶段**: val_before_train（正在跑 140 games 的 eval_in_distribution）
- **进程存活**: ✓
- **W&B run ID**: 尚未生成（val 完成后才会初始化 W&B run）

### 4. OOM 判定
OOM 发生在 training backward pass，需要等 val 完成 + 第一个 training step 完成。预计 20-30 分钟。需要后续检查确认。

要我继续监控到 backward pass 完成吗？

---
