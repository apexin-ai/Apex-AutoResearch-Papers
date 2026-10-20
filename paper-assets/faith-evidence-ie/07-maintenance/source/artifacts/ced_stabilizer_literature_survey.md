# CED-as-Training-Stabilizer 文献调研摘要

## 最接近的已有工作

**GDPO**（NVIDIA, ICML 2026）是最直接的先行工作。它发现将 GRPO 直接应用于多 reward 组合时，归一化会把不同 reward 组合 collapse 为相同 advantage 值，导致训练信号分辨率丧失甚至收敛失败。GDPO 的解法是对每个 reward 独立归一化再聚合。这与我们的发现高度一致：CED reward 自然引入了独立的 evidence quality 维度，天然避免了 advantage collapse，而 extraction-only 和 flat-NLI 只有单维 reward，正好落入 GDPO 所刻画的失败模式。

**DRA-GRPO**（2025）从另一角度切入：GRPO 的标量 reward 无法区分语义多样但得分相同的输出。DRA 用子模互信息加权 reward 来注入多样性。CED 的对比结构本身就天然携带多样性信号，无需后处理。

**Dr. GRPO**（COLM 2025）的分析最直接解释了我们的 frac_zero_std 现象：reward_std→0 时 GRPO advantage 归一化产生 difficulty bias（全对/全错组被过度加权或梯度消失）。CED 维持了 reward_std>0，从 Dr. GRPO 的视角看就是避免了这一 bias。理论论文 [arXiv 2601.23135] 进一步证明了 reward_std 越大 GRPO 收敛越好。

对比 reward 方面，Shen & Zhang（2024）验证了 contrastive reward 在 PPO 中减少 variance、提升鲁棒性，EMNLP 2024 的工作验证了对比训练 reward model 带来更稳定 RL 训练。但这些都在通用 RLHF 场景，未涉及 GRPO 或 task-specific evidence discrimination。

## 我们的新颖性

1. **首次在 IE 任务中用实验证据表明 reward 结构（而非 algorithm trick）决定 GRPO 训练稳定性**。DAPO/Dr.GRPO/GVPO/REINFORCE++ 都从优化算法层面解决 mode collapse，而 CED 展示了 reward design 本身就能解决这一问题。
2. **对比 evidence discrimination 作为 RL stabilizer 是全新的**。已有 contrastive reward 工作要么在通用 RLHF 中（Shen 2024），要么在图像生成中（DiverseGRPO），没有在 IE/DocRE 中用 evidence quality 的对比判别作为 stabilizing signal。
3. **三种 reward type 的 controlled ablation 提供了干净的因果证据**，这在已有文献中罕见——大多数工作只对比新方法 vs. baseline，没有在完全相同配置下系统比较不同 reward structure 的稳定性。

## 论文定位建议

**角度 1：Multi-dimensional Reward as Implicit Diversity Regularizer**。将 CED 定位为一种 reward design 层面的 diversity mechanism，与 GDPO/DRA-GRPO 形成"从不同层面解决同一问题"的叙事。引用 GDPO 的 advantage collapse 理论作为解释框架。

**角度 2：Reward Variance Maintenance for Gradient Health**。利用 [arXiv 2601.23135] 的理论（reward_std 与收敛速率正相关）和 Dr. GRPO 的 difficulty bias 分析，将 CED 的稳定性归因于 evidence quality 维持了 per-group reward variance，防止了 GRPO 的梯度消失。

**角度 3：Task-Specific Contrastive Signal as a Free Stabilizer**。强调 CED 的对比结构不是专门为 training stability 设计的（它的原始目的是提升 evidence faithfulness），但意外地作为 training stabilizer 起作用。这个"free lunch"叙事与 DRA-GRPO/DAPO 的"需要额外 trick"形成鲜明对比，是最有叙事张力的角度。
