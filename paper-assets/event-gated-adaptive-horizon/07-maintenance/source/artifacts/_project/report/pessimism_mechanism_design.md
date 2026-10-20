# BernoulliST 悲观机制设计（D020）

## 问题：Delusional Critic 困境

训练 `dt_embedding` 使 RSSM 精确预测 dt>1 转移 → imagination 中 gate 选择 dt=2 跳步获得过高 return → critic 过估 → advantage 枯竭 → actor 崩塌。008a 实验（未训练 dt_embedding）的成功正源于随机 embedding 充当天然悲观偏置。核心矛盾：gate 学习需要 dt_embedding 梯度，但梯度导致过估。需要悲观机制在允许 gate 学习的同时抑制 value 膨胀。

## 方案 A：Pessimistic Value Estimation

**改动点**：`models.py` `ImagBehavior.__init__`（L436-447）增加 `self.value2`，与 `self.value` 同构的 MLP；`__init__`（L449）增加 `self._slow_value2`；`_value_opt`（L468）纳入 value2 参数。`_compute_target`（L671）将 `value = self.value(imag_feat).mode()` 改为 `v1, v2 = self.value(feat).mode(), self.value2(feat).mode(); value = torch.min(v1, v2) - β * torch.abs(v1 - v2)`。`_train`（L521-527）value_loss 中对 value2 做同样的 log_prob + slow_target 计算并相加。

**超参**：`pessimism_beta`=0.5（value penalty 系数），`twin_critic`=True（开关）。

**与现有代码交互**：不影响 world model 训练。slow_target 更新（`_update_slow_target` L768）需对 value2 做同样的 EMA 更新。checkpoint 序列化需包含 value2 + slow_value2。

**风险**：双 critic 使 value 参数量翻倍（约 +1.5M），训练速度下降 ~15%。β 过大导致过度悲观，actor 学不到有效策略。两个 critic 可能收敛到相同值，失去分歧信号。

**监控指标**：`value1_value2_gap`（两 critic 差异），`pessimistic_value_mean`（修正后 value 均值），`advantage_std`（应保持非零），`imag_return_mean`（不应单调上升）。

## 方案 B：Imagination Reward Discount

**改动点**：仅改 `models.py` `_compute_target`（L665-723）。在 L671 `value = self.value(imag_feat).mode()` 之后、L693 `lambda_return_variable_dt` 调用之前，对 `reward` 施加衰减：`decay = pessimism_factor ** torch.clamp(torch.arange(H, device=reward.device).unsqueeze(-1).unsqueeze(-1) - K, min=0); reward = reward * decay`。仅在 `gate_enabled and gate_type == 'bernoulli_st'` 时生效。

**超参**：`pessimism_factor`=0.95（每步衰减率），`pessimism_start_step` K=5（开始衰减的 imagination 步数）。

**与现有代码交互**：不改任何网络架构，不影响 world model 训练，不改 loss 函数。reward 衰减只影响 actor 的 lambda-return target 计算，与 `bernoulli_physical_horizon` 掩码正交可叠加。

**风险**：衰减是启发式的，没有理论保证。K 和 factor 对环境敏感——reward 稀疏的任务（如 Crafter）可能被过度惩罚。factor 太小则远步 imagination 完全无用，退化为短视策略。不解决 critic 本身过估的根因，只抑制过估 reward 向 target 传播。

**监控指标**：`raw_vs_discounted_return`（衰减前后 return 比值），`effective_horizon`（reward 衰减到 <0.5 的步数），`advantage_mean/std`。

## 方案 C：Partial dt_embedding Freeze

**改动点**：`networks.py` RSSM `__init__`（L57-58）中 `_dt_embedding = nn.Embedding(2, 32)` 保持不变。`models.py` `WorldModel._train`（L194）中，在 `self._model_opt(mean_model_loss, self.parameters())` 调用（L329）之前，注册 gradient hook：`self.dynamics._dt_embedding.weight.register_hook(lambda g: g * mask)`，其中 `mask = torch.tensor([[1.0]*32, [0.0]*32])` 冻结 index 1（dt=2）的梯度。或更简洁地：在每次 optimizer step 后执行 `self.dynamics._dt_embedding.weight.data[1] = self._init_dt2_embedding`（保存初始随机值）。BernoulliSTGate 不改动——gate 通过 ST gradient 学习在"精确 dt=1"和"天然悲观 dt=2"之间做选择。

**超参**：`freeze_dt2_embedding`=True（开关），无额外连续超参。

**与现有代码交互**：影响 world model 训练——RSSM 对 dt=2 转移的预测能力被刻意限制。Gate supervision loss（`compute_gate_targets` L19）不受影响，仍正常训练 gate MLP。需在 `WorldModel.__init__` 中保存 `self._init_dt2_embedding = self.dynamics._dt_embedding.weight.data[1].clone()`。

**风险**：dt=2 预测不准可能导致 decoder/reward head 在 dt=2 转移上产生异常梯度，间接干扰 RSSM 其他参数。冻结策略过于绝对——没有中间态，无法调节悲观程度。如果 gate 学会永远选 dt=1 来回避不准确的 dt=2 预测，则 gate 机制完全失效。

**监控指标**：`dt2_embedding_norm`（应保持恒定），`dt2_reconstruction_error`（应高于 dt1），`gate_skip_fraction`（dt=2 选择比例，应非零非满），`rssm_kl_by_dt`（分 dt 的 KL loss）。

## 对比总结

| 维度 | 方案 A：Twin Critic | 方案 B：Reward Discount | 方案 C：Partial Freeze |
|------|---------------------|------------------------|----------------------|
| 实现复杂度 | 高（新增 critic + optimizer + slow target） | 低（_compute_target 加 5 行） | 中（gradient hook + 状态保存） |
| 新颖性 | 低（TD3/CQL 已有先例） | 低（纯启发式） | 高（利用 embedding 冻结制造结构性悲观） |
| 超参敏感性 | 中（β 需调） | 高（factor 和 K 环境敏感） | 低（无连续超参） |
| 计算开销 | +15%（双 critic forward/backward） | ~0% | ~0% |
| 与现有代码兼容 | 好（不改 world model） | 最好（仅改 target 计算） | 中（改 world model 梯度流） |
| 解决根因 | 部分（抑制 value 但不治 RSSM 过估） | 否（只抑制 reward 传播） | 是（直接阻止 dt=2 预测变准确） |
| 失败模式 | 双 critic 坍缩到同值 | 远步 imagination 完全无效 | gate 退化为永远 dt=1 |

## 推荐

**首选方案 C**，原因：(1) 直接命中根因——RSSM dt=2 预测不会因训练变准确，保持 008a 的悲观偏置效果；(2) 零额外超参，消除调参负担；(3) 计算零开销；(4) 最具学术新颖性——"结构性悲观"是全新概念，可作为论文核心 contribution。主要风险（gate 退化为纯 dt=1）可通过 gate supervision loss 中的 entropy bonus 和 skip ratio 监控预防。

**备选方案 A** 作为安全后备——如果方案 C 的 gate 退化无法缓解，twin critic 是工程上最稳健的方案，有丰富文献支撑。

**方案 B 不推荐**作为独立方案，但可与 A 或 C 叠加使用作为额外保险。
