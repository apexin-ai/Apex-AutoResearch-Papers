# BernoulliST Value Pessimism 设计方案

> 背景：BernoulliST gate + dt_embedding 训练 → RSSM 精确预测 dt=2 转移 → imagination return 虚高 → value 过估 → advantage 枯竭 → 崩塌。需要在 value estimation 层面引入悲观偏置。

## 方案 A: Pessimistic Value Estimation (Twin Critic + Penalty)

**改动点**：
- `models.py` / `ImagBehavior.__init__`：新增 `self.value2`（与 `self.value` 同构的第二个 MLP），对应 `_slow_value2`、`_value_opt2`
- `models.py` / `_compute_target`：将 `value = self.value(imag_feat).mode()` 替换为 `v1 = self.value(imag_feat).mode(); v2 = self.value2(imag_feat).mode(); value = torch.min(v1, v2) - beta * torch.abs(v1 - v2)`
- `models.py` / `_train`：critic loss 段同时训练 value 和 value2（各自独立对 target 回归），两个 slow_target 各自 EMA 更新

**新增超参**：
- `pessimism_beta`: float = 0.5（penalty 强度，0 退化为 clipped double Q）
- `twin_critic`: bool = True（总开关，false 时完全退回单 critic）

**兼容性**：不改 BernoulliSTGate、RSSM、dt_embedding。`twin_critic=False` 时行为与现有代码完全一致。critic 配置复用 `config.critic` 字典。

**预期效果**：value 被系统性低估，抑制 dt=2 imagination 产生的虚高 return。β=0.5 时 penalty 约为 critic 分歧的一半，足够抵消过估但不至于过度保守导致 exploration 停滞。

**风险**：参数量翻倍（+1个 critic MLP ~0.5M params）；β 过大时 actor 因 value 过低而停止学习；两个 critic 需要同步收敛，否则 |v1-v2| 噪声大。

---

## 方案 B: Imagination Reward Discount

**改动点**：
- `models.py` / `_compute_target`：在 `reward` 传入 `lambda_return_variable_dt` 之前，对 imagination step t > K 的 reward 乘以衰减因子 `pessimism_factor^(t-K)`

```python
# 在 _compute_target 的 gate_enabled 分支，reward[1:] 之前
if pessimism_start > 0 and pessimism_factor < 1.0:
    H = reward.shape[0]
    step_idx = torch.arange(H, device=reward.device).unsqueeze(-1).unsqueeze(-1)
    decay = torch.where(step_idx > pessimism_start,
                        pessimism_factor ** (step_idx - pessimism_start),
                        torch.ones_like(step_idx, dtype=torch.float32))
    reward = reward * decay
```

**新增超参**：
- `imag_pessimism_start`: int = 5（前 K 步 reward 不衰减）
- `imag_pessimism_factor`: float = 0.95（每步衰减率，step 15 时累计衰减 0.95^10 ≈ 0.60）

**兼容性**：仅修改 `_compute_target` 内 reward 预处理，不触碰 critic/actor/gate/RSSM。`pessimism_factor=1.0` 时完全退回原逻辑。与 `bernoulli_physical_horizon` 正交（两者可叠加）。

**预期效果**：远期 imagination 的 reward 被显式压低，value target 自然下降。K=5 保护近期准确预测不受干扰，仅压制 dt=2 跳步累积后的远端 return 膨胀。

**风险**：引入了 non-stationary reward（reward scale 随 imagination depth 变化），可能干扰 RewardEMA 归一化；pessimism_factor 太小会让 actor 完全忽略远期奖励，退化为 myopic policy；与 physical horizon mask 叠加后可能过度惩罚。

---

## 方案 C: Partial dt_embedding Freeze (Built-in Pessimism)

**改动点**：
- `networks.py` / `RSSM.__init__`：`_dt_embedding` 创建后，用更大 std 重新初始化 index 1（dt=2）：`nn.init.normal_(self._dt_embedding.weight[1:], std=1.0)`，并注册 backward hook 将 index 1 的梯度置零

```python
# RSSM.__init__ 中，_dt_embedding 初始化后追加：
if freeze_dt2_embedding:
    nn.init.normal_(self._dt_embedding.weight.data[1:], std=1.0)
    self._dt_embedding.weight.register_hook(
        lambda grad: grad * torch.tensor([1.0, 0.0], device=grad.device).unsqueeze(-1)
    )
```

- `models.py` / 无需改动（dt_embedding 的冻结在 RSSM 内部完成）

**新增超参**：
- `freeze_dt2_embedding`: bool = True（总开关）
- `dt2_init_std`: float = 1.0（dt=2 embedding 的随机初始化标准差，越大越悲观）

**兼容性**：仅改 RSSM 初始化，不影响 BernoulliSTGate、ImagBehavior、_compute_target。`freeze_dt2_embedding=False` 时退回原逻辑。gate 仍正常选择 dt∈{1,2}，只是 dt=2 对应的 RSSM 转移因 embedding 未训练而不精确 → 产生更大预测误差 → 天然的 value 低估。

**预期效果**：dt=2 的 RSSM 转移带有内置噪声（因 embedding 随机且不训练），imagination 从 dt=2 步展开时预测质量下降 → value 自然偏低。gate 在"精确 dt=1"和"模糊 dt=2"之间权衡，形成隐式悲观。不需要额外 critic 或 reward 修改。

**风险**：dt=2 的转移质量被永久牺牲——如果 dt=2 跳步是正确策略，agent 永远无法充分利用它；`dt2_init_std` 控制悲观程度但缺乏理论指导选择值；梯度 hook 在 `torch.compile` 下可能不兼容（需测试）。

---

## 方案对比表

| 维度 | A: Twin Critic + Penalty | B: Reward Discount | C: Partial Freeze |
|------|-------------------------|--------------------|--------------------|
| **实现复杂度** | 中（加 critic + optimizer + loss） | 低（仅改 reward 预处理） | 低（加 init + hook） |
| **新增超参** | 2（beta, twin_critic） | 2（start, factor） | 2（freeze, init_std） |
| **代码兼容性** | 好（开关关闭 = 原代码） | 好（factor=1.0 = 原代码） | 好（freeze=False = 原代码） |
| **理论依据** | 强（TD3/SAC/CQL 成熟范式） | 中（启发式，无理论最优衰减率） | 弱（新颖但无先例） |
| **新颖性** | 低（标准 pessimism） | 低（简单工程 trick） | 高（dt-embedding 作为内置悲观源） |
| **论文贡献** | 低（reviewer 会认为是 standard practice） | 低（不构成方法论贡献） | 高（可作为 "information-asymmetric gate" story） |
| **参数开销** | 高（+1 critic MLP ~0.5M） | 零 | 零 |
| **风险** | β 调参敏感；双 critic 收敛慢 | EMA 干扰；myopic policy | dt=2 永久受损；compile 兼容性 |
| **推荐优先级** | **首选实现** | 备选 / 消融对照 | 实验性探索 |
