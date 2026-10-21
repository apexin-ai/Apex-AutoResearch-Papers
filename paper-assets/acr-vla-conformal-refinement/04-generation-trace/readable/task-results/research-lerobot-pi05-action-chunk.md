# research lerobot pi05 action chunk

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lerobot-pi05-action-chunk_20260521T050352_result.json`
- **Structured JSON:** [`4672b7e3ba033ecf4669.json`](../../sessions/46/4672b7e3ba033ecf4669.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是完整报告。

---

## 官方 action chunk 执行策略

### lerobot π0/π0.5 `select_action` 实现

```python
# src/lerobot/policies/pi0/modeling_pi0.py

def reset(self):
    self._action_queue = deque(maxlen=self.config.n_action_steps)

@torch.no_grad()
def select_action(self, batch):
    if len(self._action_queue) == 0:
        actions = self.predict_action_chunk(batch)[:, :self.config.n_action_steps]
        self._action_queue.extend(actions.transpose(0, 1))
    return self._action_queue.popleft()
```

### 配置参数 (π0.5 LIBERO finetuned)

| 参数 | 值 | 含义 |
|------|-----|------|
| `chunk_size` | **50** | 模型预测 50 步 action |
| `n_action_steps` | **50** | 从 chunk 中取 50 步放入 queue |
| `num_inference_steps` | 10 | flow matching 去噪步数 |

### 执行方式：**全 chunk 开环执行**

- Step 0: queue 空 → 运行一次推理，预测 50 个 action，全部入队，返回 action[0]
- Step 1-49: **不运行推理**，直接 `popleft()` 返回 action[1]...action[49]
- Step 50: queue 空 → 重新推理，产生新一批 50 个 action
- **每 50 个 env step 才调用一次模型**

eval loop 每步都获取新 observation，但只在 queue 为空时使用它：
```python
# src/lerobot/scripts/lerobot_eval.py
while not np.all(done) and step < max_steps:
    action = policy.select_action(observation)  # 内部有 queue
    observation, reward, ... = env.step(action.cpu().numpy())
    step += 1
```

---

## 对比我们的 Wrapper

### 我们的 SmolVLA eval pipeline (adaptive_k_design.md)

```
每个 step:
  obs → encode_prefix() → KV cache
     → generate_k_samples(K) → (B, K, 50, 7)
     → 取 [:H_EFF] = 前 5 步用于 scoring/CRM
     → 返回单个 7D action → env.step()
```

| 维度 | 官方 lerobot | 我们的 wrapper |
|------|-------------|---------------|
| 推理频率 | 每 50 步一次 | **每步一次** (50x 更多) |
| chunk 利用率 | 50/50 = 100% | 1/50 = 2% (仅 action[0]) |
| 时间连贯性 | 50 步开环，轨迹连贯 | 无连贯性，每步独立预测 |
| observation 利用率 | 每 50 步更新一次 | 每步更新（更 reactive） |

### 是否可能导致 0% SR

**可能是重要因素之一，但不太可能是唯一根因。**

**支持论据：**
1. π0.5 训练时 `n_action_steps=50`，模型学的是"预测完整 50 步轨迹"。action[0] 可能只是运动的起始加速度，不是完整动作语义
2. 每步重新从噪声开始去噪，相邻步的 action[0] 之间无连贯保证 → 机器人可能"抖动"或反复启动相同运动
3. 对需要多步协调的动作（抓取 = 伸手 → 预开夹爪 → 闭合），只执行 action[0] 可能永远无法完成完整运动序列

**反对论据：**
1. Receding horizon (每步取 action[0]) 是标准 MPC 策略，ACT policy 用 `n_action_steps < chunk_size` 正常工作
2. SmolVLA 用同样的 wrapper 策略（每步重新预测）能达到 ~11% SR，不是 0%
3. 0% SR 更可能源于预处理差异（图像变换、状态维度、归一化统计量不匹配）

---

## 建议修复方案

### 方案 1: 实现 action queue（推荐先试）

```python
from collections import deque

class Pi05Wrapper:
    def __init__(self, policy, n_action_steps=50):
        self.policy = policy
        self.n_action_steps = n_action_steps
        self._action_queue = deque(maxlen=n_action_steps)
    
    def reset(self):
        self._action_queue.clear()
    
    def get_action(self, obs_batch):
        if len(self._action_queue) == 0:
            chunk = self.policy.predict_action_chunk(obs_batch)  # (1, 50, 7)
            actions = chunk[0, :self.n_action_steps]  # (50, 7)
            self._action_queue.extend(actions)
        return self._action_queue.popleft().cpu().numpy()
```

### 方案 2: 排查预处理 （更可能是 0% 的根因）

重点检查:
- 图像 transform 是否与 lerobot preprocessor 一致（flip H+W、resize_with_pad、[-1,1] 归一化）
- state 维度：π0.5 LIBERO 用 8D state（eef_pos + axisangle + gripper_qpos），是否正确传入
- action 归一化统计量（mean/std）是否从正确的 checkpoint 加载
- `n_obs_steps=1`：是否只传了一帧 observation

### 方案 3: 直接用 lerobot 官方 eval（对照基线）

```bash
lerobot-eval \
    --policy.path=lerobot/pi05_libero_finetuned \
    --env.type=libero \
    --eval.batch_size=10 \
    --eval.n_episodes=10
```

先跑一次官方 eval 确认 π0.5 本身能达到预期 SR，再回来排查 wrapper 差异。

---

**结论**：官方 lerobot π0.5 执行 **全部 50 步 action chunk 开环执行**（n_action_steps=50），而非仅取首步。这与我们的 wrapper 策略（每步重新预测取 action[0]）有本质差异。建议先用方案 3 跑官方 eval 确认 baseline SR，如果官方 eval 能正常工作而我们的不行，再逐步对齐 action queue（方案 1）和预处理（方案 2）。

Sources:
- [lerobot eval script](https://github.com/huggingface/lerobot/blob/main/src/lerobot/scripts/lerobot_eval.py)
- [pi0 modeling](https://github.com/huggingface/lerobot/blob/main/src/lerobot/policies/pi0/modeling_pi0.py)
- [pi0.5 config on HuggingFace](https://huggingface.co/lerobot/pi05_libero_finetuned)
- [RTC documentation](https://huggingface.co/docs/lerobot/rtc)
- [Bring Your Own Policies](https://huggingface.co/docs/lerobot/bring_your_own_policies)
- [Issue #3226: OpenPI vs LeRobot pi0.5 settings](https://github.com/huggingface/lerobot/issues/3226)
- [Issue #2375: Reproducing pi0.5 on LIBERO](https://github.com/huggingface/lerobot/issues/2375)

---
