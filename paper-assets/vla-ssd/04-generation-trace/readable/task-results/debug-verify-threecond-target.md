# debug verify threecond target

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_verify_threecond_target_20260518T074346_result.json`
- **Structured JSON:** [`6fdd97e7f553c8f4a69d.json`](../../sessions/6f/6fdd97e7f553c8f4a69d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论：

### 1. Target variable 是什么
**7-dim action** (next action a_{t+1})。`threecond_multiseed_probe.py` line 39: `out_dim=7`，line 68 从 `fa[f"data/demo_{idx}/actions"]` 加载 action，line 90-91 用 `feat[:T-1]` 预测 `act[1:T]`。

### 2. 与原实验 target 是否一致
**一致。** 两个脚本完全相同：
- 同一个 HDF5 action source
- 同一个 probe 架构 `Linear(4096,256)->ReLU->Linear(256,7)`
- 同一个 target: next-step 7-dim action
- 同样的超参 (50ep, patience=5, lr=1e-3, hidden=256, batch=256)
- 同样的 feature: `image_mean` aggregation

### 3. R² 差异的真实原因
**Train/val split 方法不同：**
- `fulllayer_action_probe.py` line 86-91: **顺序切分**，按 demo 原始顺序取前 80% 训练、后 20% 验证，无 shuffle
- `threecond_multiseed_probe.py` line 82: **shuffle 切分**，`rng.shuffle(indices)` 用 seed 打乱 demo 顺序后再 80/20 切

这意味着即使 seed=42，两个脚本的 val set 组成完全不同。原实验的顺序切分恰好得到了一个"较容易"的 val set，导致 R² 偏高。

### 4. seed=42 trained L8 R² 值
- **threecond (shuffled split)**: seed=42 → **0.5254**，3-seed mean = 0.5456 ± 0.0146
- **fulllayer (sequential split)**: seed=42 → **0.6553**

差值 0.13 完全由 train/val split 方法差异解释，不是 target variable 问题。

---
