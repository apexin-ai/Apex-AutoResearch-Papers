# Narrative Frameworks: Success Line & Failure Line

## 成功线：exp_005 return ≥ 80% baseline

**Core claim: Variable-rate imagination works, and the bugs are the story.**

三次连续失败（exp_002→004）不是工程事故，而是一组天然的 ablation experiments——每次修复精确移除一个 failure mode，揭示 variable-rate imagination 在 model-based RL 中成立的三个必要条件：

1. **Gate-curriculum–data synchronization**（exp_002 教训）：gate_scale=0 的 warmup 阶段，subsample 必须同步禁用，否则训练分布与 gate 状态脱节，world model 学到的 dynamics 在 gate 激活后立即失效。
2. **Imagination dt bounded by curriculum**（exp_003 教训）：imagination rollout 中的 dt 必须 clamp 到当前 curriculum 允许的 effective_max_dt 范围内，且 λ-return 的 dt 索引必须与 transition 对齐（off-by-2 导致 value 估计系统性偏移）。
3. **Target–logits dimensional consistency**（exp_004 教训）：gate target distribution 的支撑集必须与 logits masking 的维度严格一致——用 gate_max_dt 计算 target 却用 effective_max_dt masking logits 会产生 silent probability leak。

论文角度不是单纯的 "we propose event-gated RSSM"，而是 **"a systematic analysis of what makes variable-rate imagination viable"**。最终的 effective_max_dt 单一来源架构（`WorldModel._update_gate_schedule()`）是这三个条件的工程结论。exp_003 已验证 gate 行为健康（entropy=1.655, H_eff=2.667× nominal, Δt autocorr=0.652），exp_005 补上最后一块拼图——return 恢复证明修复是充分的。Progressive debugging as ablation 这个叙事让 contribution 从 "one new module" 升级为 "a recipe for variable-rate model-based RL"。

---

## 失败线：exp_005 return 仍显著低于 baseline

**Core claim: Hard event gating is a dead end for high-frequency control; the systematic elimination itself is the contribution.**

如果三个已知 bug 全部修复、gate 行为指标全部健康（entropy、H_eff、autocorr 均 PASS），return 仍然上不去，那问题就不在实现层面，而在机制层面——hard Gumbel gate 对 variable-rate imagination 施加了过强的离散化约束。这是一个有价值的负向结果：我们用三轮 bug 修复系统性排除了实现因素，将 failure 归因锁定到 architectural choice。

可能的根因与后续方向：

- **Hard gate → soft attention mixture**：Gumbel-Softmax 在低温时近似 argmax，imagination trajectory 在 dt 选择上缺乏梯度信号。改为 soft weighted mixture of multi-scale transitions 可能保留 variable-rate 的好处同时避免离散化的训练不稳定。
- **自由度过高 → binary skip (K=2)**：当前 gate 支持 K 种 dt 选择，搜索空间随 K 指数增长。限制为 skip/no-skip 二元决策大幅降低探索难度，且与 neuroscience 中的 event segmentation 文献更对齐。
- **任务适配性**：Walker Walk 是 dense-reward、high-frequency control 任务，每一步都携带有效信息，variable-rate 的 "跳过无聊时段" 优势无法体现。需要在 sparse-reward / long-horizon 任务（如 Crafter, Memory Maze）上验证 gate 是否在正确的任务类型上才有收益。

叙事策略：论文转型为 **"When does temporal abstraction help in model-based RL? A negative result and three necessary conditions"**，用 exp_002–005 的完整修复链作为 evidence，论证 hard gating 在 dense-control 任务上的局限性，为后续 soft-gate 或 task-conditional 方案指明方向。
