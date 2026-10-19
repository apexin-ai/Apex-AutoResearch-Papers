# Adaptive KL 实现可行性评估

## 1. 当前 KL 实现分析

### verl 框架中的两套 KL 机制

verl 存在 **两套独立的 KL 惩罚机制**，当前项目只用了其中一套：

| 机制 | 配置位置 | 当前状态 | 是否支持 adaptive |
|------|---------|---------|------------------|
| **Reward-level KL** (`use_kl_in_reward`) | `algorithm.kl_ctrl` | **未启用** (`use_kl_in_reward: False`) | **已支持** — `AdaptiveKLController` 已实现 |
| **Loss-level KL** (`use_kl_loss`) | `actor_rollout_ref.actor.kl_loss_coef` | **启用中** (exp026: 0.01, exp027: 0.005) | **不支持** — 静态 float |

### 关键代码路径

**Reward-level KL（已有 adaptive 支持）：**
- 控制器定义：`RAGEN/verl/verl/trainer/ppo/core_algos.py:150-170`
  ```python
  class AdaptiveKLController:
      def __init__(self, init_kl_coef, target_kl, horizon):
          self.value = init_kl_coef
          self.target = target_kl
          self.horizon = horizon

      def update(self, current_kl, n_steps):
          proportional_error = np.clip(current_kl / target - 1, -0.2, 0.2)
          mult = 1 + proportional_error * n_steps / self.horizon
          self.value *= mult
  ```
- 配置：`RAGEN/verl/verl/trainer/config/algorithm.py:24-39` — `KLControlConfig(type="adaptive", target_kl=0.1, ...)`
- 工厂函数：`core_algos.py:196-207` — `get_kl_controller()` 根据 type 返回 Fixed 或 Adaptive
- agent_trainer 初始化：`RAGEN/ragen/trainer/agent_trainer.py:342` — `self.kl_ctrl_in_reward = core_algos.get_kl_controller(...)`
- agent_trainer 使用：`agent_trainer.py:836-840, 1412-1414` — 调用 `apply_kl_penalty(batch, kl_ctrl=self.kl_ctrl_in_reward, ...)`
- apply_kl_penalty 函数：`verl/trainer/ppo/ray_trainer.py:165-201` — 计算 KL、应用惩罚、调用 `kl_ctrl.update()`

**Loss-level KL（当前使用，静态 coef）：**
- 配置：`RAGEN/verl/verl/workers/config/actor.py:109-112` — `kl_loss_coef: float = 0.001`
- 使用：`RAGEN/ragen/workers/actor/dp_actor.py:360-365, 453-461`
  ```python
  kld = kl_penalty(logprob=log_prob, ref_logprob=ref_log_prob, kl_penalty=self.config.kl_loss_type)
  kl_loss = agg_loss(loss_mat=kld, loss_mask=response_mask, loss_agg_mode=self.config.loss_agg_mode)
  policy_loss = policy_loss + kl_loss * self.config.kl_loss_coef  # ← 静态值
  ```

### 两套机制的区别

- **Reward-level KL**：将 KL 惩罚加到 reward 信号中，影响 GRPO 的 advantage 计算。这是 InstructGPT/PPO 的标准做法。
- **Loss-level KL**：作为 policy loss 的独立正则项，不影响 advantage。这是更直接的约束方式。

对 GRPO 而言，两者都是有效的正则化手段。Reward-level 通过改变 advantage 间接影响梯度方向，Loss-level 直接在梯度中加入 KL 项。

## 2. 需要修改的文件

### 方案 A：切换到 Reward-level KL（推荐）— 纯配置修改

| 文件 | 修改内容 | 行数估算 |
|------|---------|---------|
| 实验 YAML 配置 | 设 `algorithm.use_kl_in_reward: True`, `kl_ctrl.type: adaptive`, `kl_ctrl.target_kl: 0.1`；设 `actor.use_kl_loss: False` | ~8 行 |

**零代码修改。** `AdaptiveKLController` 已完整实现，agent_trainer 已正确初始化和调用。

配置示例：
```yaml
actor_rollout_ref:
  actor:
    use_ref: True          # 保持 ref model（KL 计算需要）
    use_kl_loss: False     # 关闭静态 loss-level KL

algorithm:
  use_kl_in_reward: True   # 启用 reward-level KL
  kl_penalty: kl           # KL 估计方式
  kl_ctrl:
    type: adaptive         # 使用自适应控制器
    kl_coef: 0.005         # 初始 coef（exp027 的值）
    target_kl: 0.1         # 目标 KL（可调 0.1-0.15）
    horizon: 10000         # 控制器平滑系数
```

### 方案 B：让 Loss-level KL 支持 adaptive — 需改代码

| 文件 | 修改内容 | 行数估算 |
|------|---------|---------|
| `verl/workers/config/actor.py` | 新增 `kl_loss_adaptive: bool`, `kl_loss_target_kl: float`, `kl_loss_horizon: int` | +3 行 |
| `ragen/workers/actor/dp_actor.py` | `__init__` 中初始化 KL 控制器；替换 `self.config.kl_loss_coef` 为 `self.kl_ctrl.value`；每个 micro-batch 后调 `controller.update()` | +15 行，改 ~8 行 |
| 实验 YAML 配置 | 新增 adaptive 参数 | ~4 行 |

总改动 ~30 行。

## 3. 现成实现参考

### verl 框架自带（最直接）
- `AdaptiveKLController` 完整实现在 `verl/trainer/ppo/core_algos.py:150-170`
- 算法来自 Ziegler et al. 2019 (https://arxiv.org/pdf/1909.08593.pdf)
- 比任务描述中的 "×2/÷2" 方案更平滑 — 使用 proportional control + clipping

### TRL 库
- TRL GRPOTrainer 的 `beta` 参数默认为 0.0（不使用 KL）
- TRL 有 [issue #4532](https://github.com/huggingface/trl/issues/4532) 请求 GRPO 的 adaptive KL（2025-11 提出，尚未实现）
- TRL PPOTrainer 有 `AdaptiveKLController`，实现与 verl 相同

### OpenRLHF
- 有 `AdaptiveKLController`，基于 InstructGPT (Ouyang et al., 2022)
- 实现逻辑与 verl 一致

### DAPO
- DAPO (2025) 方案更激进：直接设 β=0 去掉 KL，靠 clip ratio 和 dynamic sampling 稳定训练
- TRL 已默认采用此做法
- **但 DAPO 针对可验证奖励的推理任务设计，不一定适用于 agent 场景**

### 结论
**RAGEN 中 verl 已有的 `AdaptiveKLController` 就是最佳参考，无需引入外部实现。**

## 4. 实现方案

### 推荐方案：方案 A（Reward-level adaptive KL）

**插入点**：无需插入代码。已有完整链路：
```
config.yaml
  → agent_trainer.__init__() 创建 AdaptiveKLController
    → agent_trainer.fit() 每步调用 apply_kl_penalty()
      → apply_kl_penalty() 内部：
        1. 计算 KL: kld = kl_penalty(old_log_probs, ref_log_prob)
        2. 加到 reward: reward += kl_ctrl.value * kld
        3. 更新控制器: kl_ctrl.update(current_kl, n_steps)
        4. 返回 metrics: {"actor/reward_kl_penalty": kl, "actor/reward_kl_penalty_coeff": coef}
```

**Adaptive 控制器行为**：
- 当 actual_kl > target_kl → proportional_error > 0 → coef 增大 → 加强惩罚
- 当 actual_kl < target_kl → proportional_error < 0 → coef 减小 → 放松惩罚
- `horizon` 控制调整速度（越大越平滑）
- `np.clip(error, -0.2, 0.2)` 防止单步跳变过大

**与 exp026/exp027 的对比**：
- exp026 (kl_coef=0.01): KL 崩塌到 0.0025 → adaptive 会自动降低 coef
- exp027 (kl_coef=0.005): KL 暴涨到 0.413 → adaptive 会自动增大 coef

## 5. 风险

### 与 GRPO 的兼容性
- **低风险。** Reward-level KL 修改 reward 后进入 GRPO 的 group normalization。KL 惩罚被视为 reward 的一部分，advantage 计算逻辑不变。
- verl 的 PPO/GRPO 训练中 reward-level KL + adaptive controller 是标准配置（见 `verl/examples/`, `recipe/`），已被大量用户验证。

### 与 entropy bonus 的平衡
- **中等风险。** 当前 `entropy_coeff=0.001`。KL 惩罚（约束策略不要偏离 ref model）和 entropy bonus（鼓励探索）方向可能冲突。
- 建议：首次实验保持 `entropy_coeff=0.001` 不变，观察 entropy 指标。如果 entropy 被 KL 惩罚压制，可适当提高 entropy_coeff。

### Reward-level vs Loss-level 的行为差异
- **中等风险。** 从 loss-level KL 切换到 reward-level KL 改变了 KL 信号影响梯度的方式：
  - Loss-level: KL 梯度直接加到 policy gradient
  - Reward-level: KL 通过 advantage 间接影响 policy gradient
- GRPO 的 group normalization 会对 reward-level KL 做归一化，可能削弱 KL 惩罚效果
- **缓解**：如果 reward-level KL 效果不理想，可改用方案 B（~30 行代码改动让 loss-level KL 支持 adaptive）

### 实现错误风险
- **极低风险（方案 A）。** 零代码修改，全部复用已有实现。
- 方案 B 有中等实现风险：需要在 actor worker 中维护控制器状态，处理多 micro-batch 的 KL 聚合。

### 测试策略
1. 先跑 1 个短实验（~30 steps）验证 adaptive KL 正常工作
2. 检查 wandb 中 `actor/reward_kl_penalty_coeff` 是否动态变化
3. 检查 KL 是否被控制在 target 附近
4. 如果表现符合预期，跑完整训练

## 6. 工时预估

### 方案 A（推荐）
- **实现：<1 小时**（纯配置修改 + 验证）
- **验证实验：2-4 小时**（跑 30 步确认 adaptive 生效）
- **完整训练：1 天**（需跑完整实验确认效果）
- **总计：Worker 小时级（<4h 实现 + 验证），含完整训练约 1.5 天**

### 方案 B（备选）
- **实现：2-3 小时**（~30 行代码改动 + 单元测试）
- **验证 + 完整训练：同方案 A**
- **总计：半天级（4-6h），含完整训练约 2 天**

## 7. 结论

**改动量极小。** verl 框架已内置 `AdaptiveKLController`，且 RAGEN 的 agent_trainer 已完整接入 reward-level KL 的 adaptive 链路。推荐方案 A（纯配置修改），零代码改动即可启用 adaptive KL。

**有现成实现。** verl 自带的实现来自 Ziegler et al. 2019，是 PPO adaptive KL 的标准方案，已被 verl 生态广泛使用。

**建议参数**：`target_kl=0.1`, `kl_coef=0.005`（初始），`horizon=10000`。这组参数对应 exp026/exp027 的 KL 范围（0.0025-0.413），target 0.1 在中间偏低位置，适合起步观察。
