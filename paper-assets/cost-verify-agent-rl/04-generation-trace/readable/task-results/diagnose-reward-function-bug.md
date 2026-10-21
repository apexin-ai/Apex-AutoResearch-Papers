# diagnose reward function bug

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_reward-function-bug_20260514T145624_result.json`
- **Structured JSON:** [`fa67cc20ae5417dd4557.json`](../../sessions/fa/fa67cc20ae5417dd4557.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have a complete picture. Let me write the final diagnosis.

## Diagnosis: exp016 Reward=0 Bug

### Root Cause

**有两个独立的问题**，混在一起产生了误导：

---

### 问题 1（主因）：`raw_reward` 日志指标恒为 0 — 环境 bug

**文件**: `RAGEN/ragen/env/alfworld/env.py:201` + `RAGEN/ragen/llm_agent/es_manager.py:191`

**机制**:
- `es_manager._execute_actions()` 第 191 行从 `info.get('raw_reward', 0.0)` 读取 raw_reward
- 但 `env.py` 的 `step()` 返回的 `info` dict 不包含 `raw_reward` 字段：
  ```python
  info = {
      "action_is_effective": True,
      "action_is_valid": action_is_available,
      "success": won
  }
  ```
- 因此 `raw_acc_reward` 恒为 0.0
- 传播到 `get_rollout_states()` 中：
  - `custom_metric['raw_reward']` = 全 0 列表
  - `env_metric['episodic_return']` = 0
  - `env_metric['raw_reward']` = 0
- **WandB 中 `train/AlfworldSG/raw_reward` 和 `episodic_return` 恒为 0**

**注意**：这只是日志/指标 bug。实际训练用的 reward 来自 `history['reward']`（即 `env.step()` 返回的 `acc_reward`），不走 `info['raw_reward']` 路径。当 `won=True` 时，`reward = config.score * float(won) = 10.0`，这个值通过 `history → _build_samples_full → score_tensor → rm_scores → DummyRewardManager → token_level_rewards` 正确传递到 GRPO。

---

### 问题 2：`advantages/returns` 为 0 — GRPO 设计特性 + 训练 success=0%

**GRPO 的 advantage 归一化**（`core_algos.py:73`）确保每个 group 内 advantage 均值为 0。所以 `critic/advantages/mean` 在 WandB 中永远接近 0 — 这是设计行为，不是 bug。

但如果**训练过程中没有任何 episode 成功**（success=0%），则所有 group 的所有 reward 都是 0，因此 advantage 也全为 0。

**为什么 val 有 4.7% success 但训练可能是 0%**:
- val 用 `temperature=0.4`（较确定性），train 用 `temperature=1.0`（随机性很高）
- AlfWorld 需要 30+ 步串联正确 action，temperature=1.0 下几乎不可能
- exp016 只有 64 个训练 episode（4 groups × 16），在 sparse reward 设定下极易全部失败

---

### 对比分析：为什么 exp013f 正常

| 方面 | exp013f (正常) | exp016 (reward=0) |
|------|---------------|-------------------|
| Reward 类型 | Dense: `valid_action_bonus=0.15` | Sparse: `valid_action_bonus=0` |
| 每步 reward | 每个 valid action +0.15 | 只有最终成功 +10.0 |
| Tag | `AlfworldSG_Dense` | `AlfworldSG` |
| reward_mean | 2.6 → 4.39 | 0 → 0 |

exp013f 用 dense reward shaping，每个 valid action 都给 +0.15 bonus。即使没有最终成功，模型也能获得 policy gradient 信号。exp016 用纯 sparse reward，只有完成全部任务才有 reward=10，否则为 0。

---

### 修复方案

**修复 1**（日志 bug）：在 `env.py` 的 `step()` 中将实际 reward 加入 info dict

文件：`RAGEN/ragen/env/alfworld/env.py`，`step()` 方法中 info dict 定义处（约第 219 行）

```python
# 当前代码
info = {
    "action_is_effective": True,
    "action_is_valid": action_is_available,
    "success": won
}

# 修复为
info = {
    "action_is_effective": True,
    "action_is_valid": action_is_available,
    "success": won,
    "raw_reward": reward  # 添加这行，让 es_manager 能正确记录 raw_reward
}
```

**修复 2**（training reward=0）：这不是代码 bug，是实验设计问题。选项：
- **A**: 对 exp016 也启用 dense reward — 把 tag 从 `AlfworldSG` 换成 `AlfworldSG_Dense`（或在 exp016 yaml 的 `env_config` 中加 `valid_action_bonus: 0.15`）
- **B**: 降低训练 temperature（如 0.6），增加 success 概率
- **C**: 增大 `env_groups`/`group_size`，增加训练样本量提高 success 几率

---

### 验证脚本结果

验证脚本已运行：`/root/cost-verify-agent-rl/scripts/debug_reward.py`。确认：
- `AlfredEnvConfig.score = 10.0`（默认值正确）
- `AlfworldSG` tag 不覆盖 `score`
- `env.step()` info dict 缺少 `raw_reward` 字段
- resume checkpoint `/root/autodl-tmp/checkpoints/exp015/global_step_5` 存在
- 训练 64 envs，4.7% success ≈ 3 个成功（但这可能是 val 的数字）

---
