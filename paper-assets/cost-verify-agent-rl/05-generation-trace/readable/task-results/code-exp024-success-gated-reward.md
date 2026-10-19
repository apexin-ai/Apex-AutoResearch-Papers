# code exp024 success gated reward

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp024-success-gated-reward_20260515T051557_result.json`
- **Structured JSON:** [`3394fe30b412305d4b5c.json`](../../sessions/33/3394fe30b412305d4b5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

### 1. Reward function 代码确认
**已存在**，无需新增。`env.py` 的 `step()` 方法中已有完整的 success-gated 逻辑：
```python
if self.config.success_gated_bonus:
    if done and won:
        reward += self.valid_action_count * self.config.valid_action_bonus
```
失败 episode reward = 0，成功 episode reward = 10.0 + valid_action_count × 0.15。

### 2. Config 参数确认
- `valid_action_bonus = 0.15` ✓（通过 `AlfworldSG_SuccessGated` tag 在 envs.yaml 中设定）
- `success_gated_bonus = True` ✓
- `score = 10.0` ✓
- `kl_loss_coef = 0.5`, `lr = 5e-7`, `30 steps`, serial mode, val `env_groups=16` — 全部与 exp023 一致

### 3. exp024 启动状态
- **tmux session**: `exp024`
- **PID**: 455719 (train.py), TaskRunner 458971, WorkerDict 459173/459174
- **GPU**: 双卡均在加载模型 checkpoint（7.9 GB/卡，持续增长中）
- **状态**: 正常初始化中，safetensors 加载中，预计几分钟后进入 val_before_train

---
