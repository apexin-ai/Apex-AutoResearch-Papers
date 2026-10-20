# Narrative Frameworks: Success Line & Failure Line

## 成功线：exp_005 return ≥ 80% baseline

**Core claim: Variable-rate imagination works, and the debugging trail is the evidence.**

三次连续实现 bug（exp_002→004）就是工程 bug——但每次修复恰好隔离并消除了一个独立的 failure mode，使 debugging 过程在事后提供了 ablation 级别的证据。Three implementation bugs that, upon systematic resolution, revealed three necessary conditions for variable-rate imagination：

1. **Gate-curriculum–data synchronization**（exp_002 教训）：gate_scale=0 的 warmup 阶段，subsample 必须同步禁用，否则训练分布与 gate 状态脱节，world model 学到的 dynamics 在 gate 激活后立即失效。
2. **Imagination dt bounded by curriculum**（exp_003 教训）：imagination rollout 中的 dt 必须 clamp 到当前 curriculum 允许的 effective_max_dt 范围内，且 λ-return 的 dt 索引必须与 transition 对齐（off-by-2 导致 value 估计系统性偏移）。
3. **Target–logits dimensional consistency**（exp_004 教训）：gate target distribution 的支撑集必须与 logits masking 的维度严格一致——用 gate_max_dt 计算 target 却用 effective_max_dt masking logits 会产生 silent probability leak。

论文角度不是单纯的 "we propose event-gated RSSM"，而是 **"a systematic analysis of what makes variable-rate imagination viable"**。最终的 effective_max_dt 单一来源架构（`WorldModel._update_gate_schedule()`）是这三个条件的工程结论。exp_003 已验证 gate 行为健康（entropy=1.655, H_eff=2.667× nominal, Δt autocorr=0.652），exp_005 补上最后一块拼图——return 恢复证明修复是充分的。Progressive debugging as evidence 这个叙事让 contribution 从 "one new module" 升级为 "a recipe validated on locomotion tasks for variable-rate model-based RL"。

**⚠ 单任务 caveat**：当前所有证据来自 Walker Walk（dense reward, high-frequency control, 60Hz action space）。Generality 需要至少一个额外环境（如 Cheetah Run 或 sparse-reward 任务）验证。在论文中只能写 "a recipe validated on locomotion"，不能写 "a general recipe"——即使 gate 行为指标健康，也可能是 Walker Walk 的任务结构恰好容忍 gate overhead，而非方法本身的 general property。

---

## Gray Zone 线：exp_005 return ratio 在 70–79%（接近但未过 80% 阈值）

**Core claim: Variable-rate imagination has real but manageable overhead; the framework and analysis are the contribution, not the SOTA.**

如果 exp_005 return 接近 baseline 但始终差一截（70–79% ratio），存在三种同等合理的解读，论文需要诚实呈现而非选择性叙事：

1. **Gate overhead 真实存在但可控**：hard Gumbel gate 引入的离散化噪声和 dt 选择开销在 Walker Walk 这类 high-frequency 任务上是净负担，但在更长 horizon 任务（需要跳过冗余 transition 的场景）中可能回本。当前结果说明 overhead 是 real cost，不是 free lunch。

2. **训练不够充分**：500K 步可能不足以让 gate 充分学习 optimal skipping policy——baseline DreamerV3 在 ~300K 步才收敛，而 gate 增加了额外的探索维度（何时跳、跳多远），搜索空间更大，可能需要更长训练才能收敛到 competitive return。

3. **超参未优化**：gate_max_dt=8、curriculum schedule（100K→250K→400K）、gate entropy bonus 等均为初始值，未经过系统性 grid search。有可能 gate 本身是 sound 的，但当前 hyperparameter 配置对 Walker Walk 不是最优。

**论文写法**：报告为 "promising but not yet matching baseline"，核心 contribution 侧重 framework（event-gated RSSM 架构 + effective_max_dt 单一来源设计）和 analysis（三个必要条件的系统性发现），而非 absolute performance。Future work 强调两个方向：(a) scalability to longer-horizon tasks where gate overhead is amortized, (b) hyperparameter sensitivity study (gate_max_dt, curriculum pacing, entropy bonus)。这种定位比硬凹 SOTA 更 defensible，也为后续工作留足空间。

---

## 失败线：exp_005 return 仍显著低于 baseline

**Core claim: Hard event gating is a dead end for high-frequency control; the systematic elimination itself is the contribution.**

如果三个已知 bug 全部修复、gate 行为指标全部健康（entropy、H_eff、autocorr 均 PASS），return 仍然上不去，那问题就不在实现层面，而在机制层面——hard Gumbel gate 对 variable-rate imagination 施加了过强的离散化约束。这是一个有价值的负向结果：我们用三轮 bug 修复系统性排除了实现因素，将 failure 归因锁定到 architectural choice。

可能的根因与后续方向：

- **Hard gate → soft attention mixture**：Gumbel-Softmax 在低温时近似 argmax，imagination trajectory 在 dt 选择上缺乏梯度信号。改为 soft weighted mixture of multi-scale transitions 可能保留 variable-rate 的好处同时避免离散化的训练不稳定。
- **自由度过高 → binary skip (K=2)**：当前 gate 支持 K 种 dt 选择，搜索空间随 K 指数增长。限制为 skip/no-skip 二元决策大幅降低探索难度，且与 neuroscience 中的 event segmentation 文献更对齐。
- **任务适配性**：Walker Walk 是 dense-reward、high-frequency control 任务，每一步都携带有效信息，variable-rate 的 "跳过无聊时段" 优势无法体现。需要在 sparse-reward / long-horizon 任务（如 Crafter, Memory Maze）上验证 gate 是否在正确的任务类型上才有收益。

叙事策略：论文转型为 **"When does temporal abstraction help in model-based RL? A negative result and three necessary conditions"**，用 exp_002–005 的完整修复链作为 evidence，论证 hard gating 在 dense-control 任务上的局限性，为后续 soft-gate 或 task-conditional 方案指明方向。
