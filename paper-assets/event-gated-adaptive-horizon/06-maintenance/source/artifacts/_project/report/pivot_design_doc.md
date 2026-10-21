# Pivot 设计文档：DreamerV3 时间抽象替代方案

## 问题陈述

当前项目尝试在 DreamerV3 的 RSSM imagination rollout 中引入 variable-rate stepping（dt>1）。实现方式是：(1) RSSM.img_step 接收 dt embedding 拼接到输入；(2) EventGate 用 Gumbel-Softmax 选择 dt∈{1,...,K}；(3) lambda_return_variable_dt 用 γ^dt 做折扣修正。

**所有 dt>1 实验均失败**——eval_return 崩塌。根本原因：RSSM 的 GRU cell 是逐步递归结构，将 dt embedding 拼入输入只是告诉网络"你应该跳多远"，但 GRU 隐状态 deter 仍然只做一次递归更新。网络无法仅凭一个 embedding 学会模拟多步状态演化——这本质上要求单次前向传播完成多步 dynamics 的压缩，与 RSSM 的归纳偏置矛盾。

## 方案 A：Context-Change Gated Imagination（THICK 风格）

### 核心思路

不改变 imagination 的 dt（始终 dt=1），而是在 imagination trajectory 上引入**上下文变化检测**。参考 THICK（Gumbsch et al., ICLR 2024），低层 RSSM 正常 dt=1 rollout，但将 latent state 分为"快变部分"（stoch）和"慢变上下文"（context），上下文仅在事件边界更新。高层模型只预测上下文变化点之间的转移，实现跨时间尺度的 value estimation。

具体适配：
- 保留现有 EventGate 架构，但输出改为**二值 boundary signal**（"此步是否为事件边界"），而非 dt 值
- Imagination 仍 dt=1 逐步 rollout（不改 RSSM.img_step）
- 在 boundary 处做额外的 long-horizon value bootstrap：用高层 critic 估计从此 boundary 到下一 boundary 的 value
- Lambda-return 计算中，在 boundary 处混入高层 value 估计，加速 credit assignment

### 集成点

| 文件 | 改动 |
|------|------|
| `networks.py` EventGate | 输出从 K-way categorical 改为 binary（boundary / no-boundary），简化门控 |
| `networks.py` RSSM | **不改**。img_step 保持 dt=1，去掉 dt_embedding |
| `models.py` ImagBehavior | 添加高层 critic head；_imagine 中记录 boundary mask；_compute_target 中在 boundary 处插入高层 value |
| `tools.py` | 新增 `lambda_return_hierarchical()`，在 boundary 处用高层 value 做 bootstrap |

### 工程量：~5-7 天

### 优缺点
- **优**：不改 RSSM dynamics，避开 dt>1 的根本问题；与 THICK 有明确的对标 baseline 可引用；EventGate 代码可大量复用
- **缺**：新颖性下降（更接近 THICK 的变体）；高层 critic 增加训练复杂度；需要仔细调 boundary 频率

## 方案 B：Actor-Level Action Repeat（TempoRL 风格）

### 核心思路

Imagination 保持 dt=1，但 actor 输出额外的一维**repeat duration** r∈{1,...,K}，表示"当前动作重复执行 r 步"。在 imagination rollout 中，当 actor 选择 r>1 时，连续 r 步使用相同 action 做 dt=1 的 RSSM img_step。

### 集成点

| 文件 | 改动 |
|------|------|
| `networks.py` RSSM | **不改**。去掉 dt_embedding，img_step 回归原版 |
| `networks.py` EventGate | 改为 RepeatHead：输入 feat，输出 repeat duration 的 categorical 分布 |
| `models.py` ImagBehavior._imagine | step_fn 中：如果 remaining_repeat>0，复用上一动作；否则采样新动作 + repeat duration |
| `models.py` _compute_target | 回归标准 lambda_return |
| `tools.py` | 可删除 subsample_variable_dt 和 lambda_return_variable_dt |

### 工程量：~3-4 天

### 优缺点
- **优**：最小改动量；RSSM 完全不碰，风险最低；实现简单可快速验证；tools.py 大量简化
- **缺**：action repeat 是 open-loop 的时间抽象；学术新颖性最低；论文 story 从 "event-gated adaptive horizon" 变成 "learned action repeat"

## 推荐

**方案 B（Action Repeat）**，理由：
1. **时间约束**：CoRL DDL 2026-05-29，剩余 15 天。方案 B 实现 3-4 天，留 10+ 天。方案 A 需 5-7 天。
2. **风险**：方案 B 不改 RSSM，回归验证过的 dt=1 dynamics，几乎不可能再出崩塌。
3. **Story 兼容**：action repeat 仍可用 EventGate 的 boundary detection 叙事——"event-gated action persistence"。

## 关键参考文献

1. Gumbsch et al., "Learning Hierarchical World Models with Adaptive Temporal Abstractions" (THICK), ICLR 2024
2. Hafner et al., "Deep Hierarchical Planning from Pixels" (Director), NeurIPS 2022
3. Sutton et al., "Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in RL", AIJ 1999
4. Biedenkapp et al., "TempoRL: Learning When to Act", ICML 2021
5. Yu et al., "TAAC: Temporally Abstract Actor-Critic for Continuous Control", NeurIPS 2021
6. Saxena et al., "Clockwork Variational Autoencoders", NeurIPS 2021
7. Hafner et al., "Mastering Diverse Domains through World Models" (DreamerV3), 2023
8. Khetarpal et al., "Exploring the Limits of Hierarchical World Models in RL", Scientific Reports 2024