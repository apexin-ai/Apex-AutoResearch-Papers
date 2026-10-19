# Exp010 GRPO Reward Analysis: Success 从 4.7% 降至 0% 的根因

## 1. Reward Function 结构

### 1.1 三层 Reward 组成

```
┌─────────────────────────────────────────────────────┐
│              最终 GRPO Score (per trajectory)         │
│                                                     │
│   score = env_reward + Σ(format_penalty)            │
│                                                     │
│   ┌──────────────────┐  ┌─────────────────────────┐ │
│   │  Environment Reward │  │   Format Penalty        │ │
│   │  (AlfWorld env.py)  │  │  (es_manager.py:236)    │ │
│   │                     │  │                         │ │
│   │  success → +10.0    │  │  每个 turn 中 LLM 生成  │ │
│   │  failure →   0.0    │  │  无法解析的 action 时:   │ │
│   │                     │  │  penalty_delta = -0.1   │ │
│   │  纯稀疏奖励:        │  │                         │ │
│   │  只在任务完成时      │  │  累积到 rollout_cache   │ │
│   │  给出正奖励         │  │  ["penalty"] 中         │ │
│   └──────────────────┘  └─────────────────────────┘ │
│                                                     │
│   Normalization: identity (不做任何归一化)            │
│   GRPO advantage: (score - group_mean) / group_std  │
│   group_size = 8                                    │
└─────────────────────────────────────────────────────┘
```

### 1.2 关键参数

| 参数 | 值 | 来源 |
|------|-----|------|
| env success reward | 10.0 | `AlfredEnvConfig.score` |
| env failure reward | 0.0 | `env.py: config.score * float(won)` |
| format_penalty | -0.1 | `es_manager.format_penalty` |
| reward_normalization | identity | `agent_proxy.reward_normalization.method` |
| GRPO grouping | state (同一问题) | `reward_normalization.grouping` |
| group_size | 8 | `es_manager.train.group_size` |
| norm_adv_by_std | True | `algorithm.norm_adv_by_std_in_grpo` |
| max_turn | 30 | `agent_proxy.max_turn` |
| KL loss | enabled, coef=0.01 | `actor.use_kl_loss, kl_loss_coef` |

### 1.3 Format Penalty 的触发条件

`es_manager.py:234-236`:
```python
if len(valid_actions) != len(env_input['actions']) or not valid_actions:
    penalty_delta = self.sys_config.es_manager.format_penalty  # -0.1
```

当 LLM 生成的 action 中存在**任何**无法映射到环境合法 action 的部分时，该 turn 扣 -0.1。
- 最大 penalty：-0.1 × 30 turns = -3.0
- 观测到的最小 score：-2.9（Step 1），说明有轨迹几乎每个 turn 都有格式错误

### 1.4 Score 传递路径

`ctx_manager.py:288-292`:
```python
acc_scores = score_tensor[:, -1]  # 环境给的累积 reward
penalty = torch.tensor([env_output.get("penalty", 0) ...])
normalized_acc_scores = acc_scores + penalty  # 加上格式 penalty
# identity normalization → 不做任何变换
```

然后 GRPO 在每个 group 内计算 advantage：`(score_i - group_mean) / group_std`

---

## 2. Step 1–10 训练指标趋势

| Step | success | pass@8 | action_valid | score_mean | score_max | score_min | adv_mean | adv_max | adv_min |
|------|---------|--------|--------------|------------|-----------|-----------|----------|---------|---------|
| 1 | **4.69%** | **37.5%** | 58.8% | 0.022 | **10.0** | -2.90 | -0.083 | 2.472 | -2.471 |
| 2 | 0.00% | 0.0% | 65.7% | -0.284 | **0.0** | -2.20 | -0.069 | 1.113 | -2.432 |
| 3 | 0.00% | 0.0% | 60.6% | -0.436 | **0.0** | -2.80 | -0.047 | 1.023 | -2.301 |
| 4 | 1.56% | 12.5% | 65.2% | -0.123 | 9.5 | -1.40 | -0.088 | 2.467 | -2.291 |
| 5 | 1.56% | 12.5% | 68.7% | -0.205 | 9.5 | -2.70 | -0.055 | 2.471 | -2.331 |
| 6 | 3.12% | 12.5% | 66.9% | 0.030 | 10.0 | -2.40 | -0.020 | 1.663 | -2.457 |
| 7 | 1.56% | 12.5% | 64.8% | -0.223 | 10.0 | -2.90 | -0.006 | 2.459 | -2.365 |
| 8 | **0.00%** | **0.0%** | 69.9% | -0.331 | **0.0** | -1.30 | -0.038 | 1.225 | -2.174 |
| 9 | **0.00%** | **0.0%** | 67.2% | -0.300 | **0.0** | -1.80 | -0.002 | 1.410 | -2.102 |
| 10 | **0.00%** | **0.0%** | 68.3% | -0.288 | **0.0** | -1.10 | -0.012 | 1.643 | -1.984 |

### 关键趋势

1. **action_is_valid 持续上升**: 58.8% → 68.3%（模型在学生成合法 action）
2. **success 持续下降**: 4.69% → 0%（模型完全失去了完成任务的能力）
3. **score_max 在 step 8 后 = 0**: 没有任何轨迹成功，所有 reward 都是负的
4. **score_min 在收窄**: -2.9 → -1.1（格式错误减少，penalty 总量减少）
5. **advantage range 在收窄**: max 从 2.47 降到 1.64，min 从 -2.47 升到 -1.98

---

## 3. 成功 vs 失败轨迹的 Reward 差距分析

### 3.1 有成功轨迹的 Group（Step 1 为例）

Step 1: success=4.69% → 3/64 轨迹成功 → 约 3/8 group 有成功

**含成功轨迹的 Group 内部**（示例）:
```
成功轨迹 score: 10.0 - (3 × 0.1) = 9.7
失败轨迹 score: 0.0 - (5 × 0.1) = -0.5 (平均)

group_mean ≈ (9.7 + 7×(-0.5))/8 ≈ 0.77
group_std ≈ 3.5

成功轨迹 advantage: (9.7 - 0.77) / 3.5 ≈ +2.55  ✓ 强正信号
失败轨迹 advantage: (-0.5 - 0.77) / 3.5 ≈ -0.36  ✓ 弱负信号
```

### 3.2 无成功轨迹的 Group（占 5/8 = 62.5%）

```
所有轨迹 score ∈ [-2.9, 0.0]（纯 format penalty）

Traj 1: 0 + (-0.1 × 8) = -0.8   (8个 turn 格式错误)
Traj 2: 0 + (-0.1 × 3) = -0.3   (3个 turn 格式错误)
Traj 3: 0 + (-0.1 × 1) = -0.1   (1个 turn 格式错误)
...

group_mean ≈ -0.45
group_std ≈ 0.23

Traj 1 advantage: (-0.8 - (-0.45)) / 0.23 = -1.52  ← "多格式错误=差"
Traj 3 advantage: (-0.1 - (-0.45)) / 0.23 = +1.52  ← "少格式错误=好"
```

### 3.3 梯度贡献对比

| 信号来源 | Group 数量 | 梯度方向 |
|----------|-----------|----------|
| 有成功的 Group | ~3/8 (37.5%) | "完成任务 → 好" |
| 无成功的 Group | ~5/8 (62.5%) | **"减少格式错误 → 好"** |

**无成功 group 提供的梯度**是有成功 group 的 **1.67 倍**。但两者的目标方向完全不同。

---

## 4. 结论：Reward 问题的根因

### 根因：Format Penalty 在零成功 Group 中主导了 GRPO 的 Advantage 信号

GRPO 的 advantage 计算在每个 group（8 条轨迹，同一问题）内进行归一化。当一个 group 中没有任何轨迹成功时：

1. **环境 reward 全为 0**：所有轨迹的 env_reward = 0
2. **score 完全由 format_penalty 决定**：score = 0 + Σ(format_penalty)
3. **GRPO advantage 只区分格式合规程度**：格式错误少的轨迹获得正 advantage

这导致了一个**恶性循环**：

```
Step 1: 5% success, 59% valid
    → 37.5% group 有成功信号, 62.5% group 只有 format 信号
    → 模型同时学 "完成任务" 和 "减少格式错误"
    → format 信号更强，主导梯度

Step 2-3: success 降到 0%
    → 100% group 只有 format 信号
    → 模型完全转向学 "减少格式错误"
    → 失去探索性行为（尝试可能失败但有潜力的动作）

Step 4-7: success 偶尔回升（随机涨落）
    → 但大部分梯度仍来自 format 信号
    → 模型继续收敛到 "生成合法但无效的动作"

Step 8-10: success = 0, valid = 68%
    → 模型已完全学会 "生成格式合法的动作"
    → 但完全丧失了 "完成任务" 的能力
    → score range 收窄到 [-1.1, 0]
    → advantage 信号变弱，训练趋于停滞
```

### 辅助因素

1. **Success rate 太低（4.7%）+ Group size 太小（8）**: 期望每个 group 有 0.38 个成功轨迹。大部分 group 完全没有正奖励信号。
2. **Reward normalization = identity**: 不同 group 的 score scale 差异极大（有成功的 group score ∈ [-3, 10]，没成功的 ∈ [-3, 0]），但没有做跨 group 归一化。
3. **纯稀疏奖励**: AlfWorld 只有终态奖励，没有过程奖励。模型无法从"接近成功"的轨迹中获得正向信号。
4. **KL loss 可能抑制探索**: `kl_loss_coef=0.01` 加上 `use_ref=True`，KL 惩罚可能阻止模型尝试偏离 SFT 策略的新行为。

---

## 5. 建议方案

### 方案 A: 修改 Reward 结构（推荐，最根本的修复）

**A1. 添加进度奖励 (Progress Reward)**

AlfWorld 的 `info["won"]` 是终态信号，但环境内部有 score 信息。可以添加基于任务进度的中间奖励：
- 拿起正确物品: +2.0
- 到达正确房间: +1.0  
- 打开正确容器: +1.0

在 `env.py` 中利用 AlfWorld 的 `infos["score"]` 字段（0-1 连续值），替换 won-based reward：

```python
# 现在: reward = self.config.score * float(won)  # 10.0 or 0.0
# 改为: reward = self.config.score * infos["score"][0]  # 0.0 to 10.0 连续
```

**A2. 大幅降低 Format Penalty**

```yaml
es_manager:
  format_penalty: -0.01  # 从 -0.1 降到 -0.01，或直接设为 0
```

理由：format_penalty 在零成功 group 中是唯一的 gradient 来源。降低它能让 advantage 信号更均匀（减少 format penalty 对梯度的主导），同时模型仍可通过 KL loss 保持 SFT 学到的格式。

### 方案 B: 调整 GRPO 参数

**B1. 增大 Group Size**

```yaml
es_manager:
  train:
    group_size: 16  # 或 32
```

Group size 16 时，4.7% success rate 期望每组有 0.75 个成功，约 53% 的 group 至少有 1 个成功（vs 当前 8 时的 32%）。

**B2. 关闭 advantage std 归一化**

```yaml
algorithm:
  norm_adv_by_std_in_grpo: False  # Dr. GRPO 模式
```

使 advantage = (R - mean)，不除以 std。这样零成功 group 的 advantage 绝对值更小（因为 score 范围小），减少其梯度贡献。

### 方案 C: 从 Step 5 Checkpoint 恢复

`/root/autodl-tmp/checkpoints/exp008_grpo/global_step_5/` 有 checkpoint。Step 5 时 success=1.56%, pass@8=12.5%，模型尚未完全崩溃。

可以从 step 5 恢复，应用方案 A 的 reward 修改后继续训练。

### 方案优先级

1. **方案 A1 + A2**（必做）: 修改 reward 函数，添加进度奖励 + 降低 format penalty
2. **方案 B1**（强烈建议）: 增大 group_size 到 16+
3. **方案 C**（可选）: 从 step 5 checkpoint 恢复而非从头开始
4. **方案 B2**（可选）: 关闭 std 归一化

### 不建议做的事

- ❌ 从 step 10 继续训练：模型已完全丧失任务完成能力，需要重新开始或从较早 checkpoint 恢复
- ❌ 仅增大 group_size 而不改 reward：即使 group_size=32，5% success rate 仍然意味着每组只有 1.6 个成功，format penalty 仍会主导多数 group 的梯度
- ❌ 仅调高 success reward（如 100.0）：不解决根本问题——零成功 group 内仍然没有正信号
