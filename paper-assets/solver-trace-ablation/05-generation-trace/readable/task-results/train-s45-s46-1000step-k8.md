# train s45 s46 1000step k8

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_s45-s46-1000step-k8_20260521T233334_result.json`
- **Structured JSON:** [`9fa1b76d4fd521016396.json`](../../sessions/9f/9fa1b76d4fd521016396.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s45 训练已在后台运行。状态：
- **磁盘**：163GB 空闲，无需清理
- **s45/s46 checkpoint-500**：不存在（已被之前清理），从 base model 从头跑 1000 步
- **K=8 配置**：已创建 `exec_only_s45_1000_k8.yaml` 和 `exec_only_s46_1000_k8.yaml`，参数：`num_generations=8, gradient_accumulation_steps=4, per_device_batch_size=2`
- **s45 训练**：tmux `exec-s45`，GPU 0，~6.3s/step，预计约 1.7h 完成

3 分钟后检查训练进度。

---
