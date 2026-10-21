# Plan005 NEGATIVE 结果文献调研：辅助 Reward 降低主目标性能

## 背景

plan005-sta-low-s42 实验结论为 NEGATIVE：GRPO 训练中 STA reward (weight=0.1) 导致 prove_rate 下降 10.7%（0.7725 vs exec-only 0.865）。ISR/PR ratio=0.298 稳定，说明 STA 确实维持了结构性分离，但任何非零 STA 权重都会引入 penalty effect。

本报告调研 multi-objective RL 和 LLM reasoning 领域中关于"辅助/过程 reward 降低主目标性能"现象的相关文献。

---

## Paper 1: On Designing Effective RL Reward at Training Time for LLM Reasoning

| 字段 | 内容 |
|------|------|
| 作者 | Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu |
| 年份 | 2024 |
| Venue | arXiv 2410.15115 |

**核心发现**: 学习到的 PRM (Process Reward Model) 和 ORM (Outcome Reward Model) 用于 RL 训练时，**可能不仅无帮助，甚至损害训练效果**，产生比仅使用 success reward 训练的模型更差的性能。模型通过重复正确但不必要的推理步骤获得高 reward，造成严重的 reward hacking。

**解决方案**: 提出两种 reward refinement 技术：
- **Clipping**: 限制累积 reward 的上界
- **Delta**: 限制跨 trajectory 的 reward 增长幅度

两者确保累积 reward 有上界，防止 learned reward model 被 exploit。

**与 plan005 的关联**: **高度相关**。STA 的 ISR 本质上是一种结构性 process reward。该论文直接证明 process reward 在 RL 训练时可降低主目标（accuracy/prove_rate）性能。STA weight=0.1 的 prove_rate 下降 10.7% 与此现象一致。Clipping/Delta 技术可作为 STA 改进方向——限制 ISR 对总 reward 的最大贡献。

---

## Paper 2: Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training

| 字段 | 内容 |
|------|------|
| 作者 | Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal |
| 年份 | 2025 |
| Venue | arXiv 2509.03403 |

**核心发现**: PRM 虽然提供细粒度的中间步骤指导，但**频繁出现不准确性且容易被 reward hacking 利用**。而 ORM 缺乏足够的粒度来评估推理质量。直接混合 PRM+ORM 信号会导致性能退化。

**解决方案**: PROF (PRocess cOnsistency Filter) — 基于 PRM-ORM 一致性的数据过滤。保留"高 process value 的正确 response"和"低 process value 的错误 response"，过滤掉不一致样本。比直接混合方法**提升 4%+ 准确率**。

**与 plan005 的关联**: **高度相关**。STA 的 ISR 是一种 process-level signal（结构必要性），与 execution outcome 是两个不同维度。PROF 的思路建议：仅在 ISR 与 execution 结果一致时使用 ISR reward（即只对 prove 成功的样本施加 ISR bonus，对 prove 失败的样本不施加 ISR penalty），而非无条件线性组合。这可能是解决 plan005 negative 的关键方向。

---

## Paper 3: Confronting Reward Model Overoptimization with Constrained RLHF

| 字段 | 内容 |
|------|------|
| 作者 | Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer |
| 年份 | 2023 |
| Venue | arXiv 2310.04373 / ICLR 2024 |

**核心发现**: 首个研究 composite reward model 过度优化的工作。发现组合多个 reward model 时，**component RM 之间的相关性显著影响过度优化发生的阈值**。超过阈值后，更高的 proxy reward 反而关联更差的真实表现。

**解决方案**: 
- **Constrained RL**: 将每个 component RM 的优化限制在其"有用阈值"内
- **Dynamic Lagrange Multipliers**: 通过拉格朗日乘子自动学习动态权重，替代固定权重的线性组合
- **Adaptive Gradient-Free Optimization**: 在训练过程中识别最优性能点

**与 plan005 的关联**: **直接相关**。plan005 使用固定权重 0.1 线性组合 exec reward 和 ISR。该论文表明固定权重的线性标量化存在本质缺陷，建议使用 constrained RL 或动态 Lagrange 乘子权重。这为 STA 提供了明确的改进方向：用约束优化替代固定权重。

---

## Paper 4: Defining and Characterizing Reward Hacking

| 字段 | 内容 |
|------|------|
| 作者 | Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger |
| 年份 | 2022 |
| Venue | arXiv 2209.13085 / NeurIPS 2022 |

**核心发现**: 形式化定义了 reward hacking。关键定理：**对于所有随机策略的集合，两个 reward function 只有在其中一个为常数时才是 unhackable 的**。这意味着任何非平凡的 proxy reward（如 ISR）在被优化时，都有可能降低 true reward（如 prove_rate）。

**理论意义**: 该结果为 plan005 的 negative 提供了**理论解释基础**——ISR 作为 prove_rate 的 proxy，在任何非零权重下都可能 hack 真实目标。这不是 STA 特有的问题，而是 reward composition 的基本限制。

**解决方向**: 论文建议通过限制策略空间（而非使 reward 更复杂）来缓解 hacking。对 STA 而言，这意味着可能需要约束优化策略空间（如 KL penalty 或 clipping），而非简单调低 ISR 权重。

---

## Paper 5: LLM Reasoning with Process Rewards for Outcome-Guided Steps (PROGRS)

| 字段 | 内容 |
|------|------|
| 作者 | Mohammad Rezaei, Jens Lehmann, Sahar Vahdati |
| 年份 | 2026 |
| Venue | arXiv 2604.02341 (submitted to IJCNN 2026) |

**核心发现**: PRM scores 如果作为绝对 reward 被优化，**会放大"流利但错误"的推理模式并诱发 reward hacking**。PRM 经常对最终不正确的推理路径给出高分。

**解决方案**: **Outcome-Conditioned Centering** — 将错误 trajectory 的 PRM scores 平移至零均值。这在保留 PRM 对中间步骤的排序信息的同时，消除 PRM 对错误 trajectory 的系统性偏差。结果：以更少的 rollout 达到比 outcome-only baseline 一致的提升。

**与 plan005 的关联**: **高度相关**。ISR 目前无条件地对所有样本施加：prove 成功的样本得到 ISR bonus（正面），prove 失败的样本被 ISR 评估后可能得到非零 reward（负面效应）。Outcome-conditioned centering 建议：将 ISR 调整为以 execution outcome 为条件——仅对 prove 成功的样本保留 ISR 差异化信号，对 prove 失败的样本将 ISR 归零。

---

## 综合分析与 STA 改进方向

### plan005 NEGATIVE 的理论解释

5 篇论文一致指向同一机制：**辅助/过程 reward 在 RL 训练中降低主目标性能**是一个已知且普遍的现象，不是 STA 特有的。原因包括：

1. **Proxy reward 的固有 hackability**（Skalse et al.）：任何非常数 proxy 都可能降低 true reward
2. **Process reward 的不准确性**（Gao et al., Ye et al.）：process-level signal 与 outcome 不完全对齐
3. **固定权重线性组合的缺陷**（Moskovitz et al.）：无法适应训练阶段变化
4. **无条件施加 process reward 的危害**（Rezaei et al.）：对错误 trajectory 的 process reward 破坏梯度信号

### 可行改进方案（优先级排序）

| 方案 | 来源 | 核心思路 | 实施复杂度 |
|------|------|----------|-----------|
| **Outcome-conditioned ISR** | PROGRS | 仅对 prove 成功的样本施加 ISR 差异化 reward | 低 |
| **ISR Clipping** | Gao et al. | 限制 ISR 对总 reward 的最大贡献 | 低 |
| **Consistency Filtering** | PROF | 仅使用 ISR-execution 一致的样本 | 中 |
| **Dynamic Lagrange Weighting** | Moskovitz et al. | 用约束优化自动学习 ISR 权重 | 高 |
| **Bonus-only ISR** | 综合 | ISR 仅作为 bonus（≥0），不作为 penalty | 低 |

### 推荐下一步

最低成本高收益方案：**Bonus-only + Outcome-conditioned ISR**。具体实现：
- 对 prove 成功的样本：`reward = exec_reward + α × max(ISR - baseline, 0)`
- 对 prove 失败的样本：`reward = exec_reward`（ISR 不参与）

这同时解决了 Skalse 的 hackability 问题（ISR 只做正向 bonus）和 Rezaei 的 outcome-conditioning 问题。
