# CRM Correction 退化现象：文献调研

> **背景**：ACR-VLA 的 CRM correction 在 LIBERO spatial eval 中反而降低了 performance（23.3% vs baseline 30%），而简单的 sample selection（SampleConsensus, 42.9%）显著更好。本文档调研相关文献，分析退化原因并提出补救方向。

---

## 1. Conformal Prediction + Correction 退化现象

### 1.1 Calibration-Efficiency Paradox

| 论文 | 年份 | Venue | 核心发现 |
|------|------|-------|----------|
| **Does Confidence Calibration Improve Conformal Prediction?** (Xi et al.) | 2024 | arXiv | 标准 temperature scaling calibration 反而导致 adaptive CP 的 prediction set 更大——直接的效率退化。高置信度预测有利于效率，但 cross-entropy 优化的 rescaling 参数与高效集合生成目标冲突。 |
| **On Temperature Scaling and Conformal Prediction of Deep Classifiers** (Dabah & Tirer) | 2024 | ICML 2025 | Temperature scaling 改善了 class-conditional coverage，但负面影响 prediction set size。温度升高使 softmax 更平滑，APS conformal set 单调增长。**校准精度和预测实用性之间存在根本性张力。** |
| **Adaptive Coverage Policies in Conformal Prediction** (Gauthier et al.) | 2025 | arXiv | 固定覆盖水平的 CP 产生无信息量的预测——过于保守的集合或空集。CP 对所有测试点使用常数修正，忽略个体不确定性，可能使 prediction interval 无法反映模型的实际 uncertainty。 |

### 1.2 Distribution Shift 下的 CP 失效

| 论文 | 年份 | Venue | 核心发现 |
|------|------|-------|----------|
| **Conformal Prediction Under Distribution Shift: A COVID-19 Natural Experiment** | 2026 | arXiv | 8 个供应链任务上，distribution shift 导致 CP coverage 从 86.7% 灾难性降至 0%。单特征依赖与覆盖崩溃强相关（ρ=0.714, p=0.047）。季度重训练可恢复部分覆盖，但对已鲁棒任务无益。 |
| **Beyond Overconfidence: Foundation Models Redefine Calibration in DNNs** | 2025 | arXiv | Post-hoc calibration 在 in-distribution 有效，但在 distribution shift 增大时**逐渐变得适得其反**。现代 foundation model 表现为 underconfidence 而非 overconfidence，颠覆了经典假设。 |

**与 ACR-VLA 的关联**：CRM 在 LIBERO spatial 上的退化很可能源于训练分布与评估分布的 mismatch。CP 的 exchangeability 假设被违反时，conformal-guided correction 不仅失去保障，还可能系统性地将 action 推向错误方向。

---

## 2. 过度修正 (Over-Correction) 现象

### 2.1 Self-Correction 退化

| 论文 | 年份 | Venue | 核心发现 |
|------|------|-------|----------|
| **Large Language Models Cannot Self-Correct Reasoning Yet** (Huang et al.) | 2024 | ICLR 2024 | 无外部反馈的 intrinsic self-correction 不仅不改善，反而**降低**推理性能。GPT-3.5-Turbo 在 CommonSenseQA 上 self-correction 后性能下降近一半。模型频繁将正确答案翻转为错误答案。 |
| **Understanding the Dark Side of LLMs' Intrinsic Self-Correction** (Qingjie et al.) | 2024 | ACL 2025 | 两种失败模式：(1) 简单任务上的 answer wavering 和 prompt bias；(2) 复杂任务上的认知偏差（overthinking、cognitive overload、perfectionism bias）。 |
| **When Can LLMs Actually Correct Their Own Mistakes?** (Kamoi et al.) | 2024 | TACL | 综述发现：没有先前工作能证明仅用 prompted LLM feedback 的 self-correction 是成功的。Self-correction 仅在有**可靠外部反馈**或**大规模 fine-tuning** 时有效。 |

### 2.2 Correction Magnitude 与 Cascading Error

| 论文 | 年份 | Venue | 核心发现 |
|------|------|-------|----------|
| **Error-Bounded Correction of Noisy Labels** (Zheng et al.) | 2020 | ICML 2020 | 首次从理论上证明：**无界修正是危险的**。没有形式化的 error bound，修正幅度可能超出数据所能支持的范围，导致性能退化。AdaCorr 算法基于理论保证约束修正幅度。 |
| **ReCAPA: Hierarchical Predictive Correction** | 2026 | arXiv | 中间步骤的 mis-specification 通过后续步骤传播和累积成 cascading failure。提出 Error Propagation Rate (EPR) 量化错误复合，Propagation Attenuation Coefficient (PAC) 测量错误耗散。 |
| **Two Sides of Miscalibration** (Ao et al.) | 2023 | UAI 2023 | 校准技术经常**过度校准**模型——在修复 over-confidence 的同时恶化 under-confidence。修正不是均匀有益的，修复一种 miscalibration 会创造或放大另一种。 |
| **Rethinking Calibration of DNNs: Do Not Be Afraid of Overconfidence** (Wang et al.) | 2021 | NeurIPS 2021 | 反直觉发现：训练中抑制 overconfidence 的正则化使模型**更难被 post-hoc 方法校准**——aggressive pre-correction 适得其反。 |

**与 ACR-VLA 的关联**：CRM 作为 learned correction model，其修正幅度没有被显式 bound。在 uncertainty estimation 不准确的条件下（distribution shift），CRM 可能产出过大或方向错误的修正，且这些错误在 action sequence 的时间维度上 cascade。

---

## 3. Sample Selection vs Learned Correction

### 3.1 Learned Correction 的优势场景

| 论文 | 年份 | Venue | 核心发现 |
|------|------|-------|----------|
| **Residual Policy Learning** (Silver et al.) | 2018 | arXiv | 在固定 base policy 上学习 residual action。Residual correction 在 long-horizon sparse-reward 操作任务上大幅改善不完美控制器，可隐式修正模型误差和部分可观测性——这是 sample selection 无法提供的。 |
| **TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction** (Jiang et al.) | 2024 | CoRL 2024 | 从人类遥操作干预中训练 residual correction policy。Base sim policy + learned residual 在接触密集装配任务上达到 77% 成功率 vs 最佳 baseline 18%。**Learned correction 在桥接系统性 domain gap 时远优于 selection。** |
| **PLD: Self-Improving VLA Models via Residual RL** (Xiao et al.) | 2025 | ICLR 2026 | 混合方法：Stage 1 用 residual RL 修正 frozen VLA 的失败，Stage 2 用 distribution-aware filtering 收集修正数据，Stage 3 蒸馏回 base VLA。LIBERO 上达到 99% 成功率。 |

### 3.2 Sample Selection 的优势场景

| 论文 | 年份 | Venue | 核心发现 |
|------|------|-------|----------|
| **RAFT: Reward rAnked FineTuning** (Dong et al.) | 2023 | arXiv | Best-of-N selection + SFT 范式：生成 N 个样本，按 reward 排序，用 top-ranked 微调。优于 PPO-based RLHF，且 perplexity 退化更小。**迭代 best-of-N selection 是 RL-based correction 的稳定、可扩展替代方案。** |
| **Two-Steps Diffusion Policy (GDP)** | 2025 | NeurIPS 2025 | 在去噪过程中引入 population-based sample selection：生成候选群体，计算 OoD fitness score，选择最佳一半并复制继续去噪。仅 2 次神经网络前向传播，在 14 个任务上比标准 diffusion policy 提升最高 20%。 |
| **SCOPE-Gen: Conformal Generative Modeling with Sequential Greedy Filtering** | 2024 | ICLR 2025 | 提出用 sequential conformal prediction 过滤生成模型样本。生成初始 i.i.d. 样本集，通过 greedy filter 迭代剪枝，保持 conformal admissibility 保证。提供了 multi-sample filtering 的原则性统计框架。 |

### 3.3 关键对比

| 维度 | Sample Selection | Learned Correction |
|------|-----------------|-------------------|
| **系统性 bias** | 无法修复（只能从现有样本中选） | 可以修复系统性偏差 |
| **训练需求** | 推理时即可，无需额外训练 | 需要额外训练数据和模型 |
| **稳定性** | 更稳定，不会引入新错误 | 可能引入 harmful correction |
| **Distribution shift 鲁棒性** | 较好（依赖 base model 多样性） | 较差（correction model 也受 shift 影响） |
| **适用场景** | Base model 已有好样本但概率不高 | Base model 有系统性偏差需修正 |

**与 ACR-VLA 的关联**：SampleConsensus (42.9%) >> CRM (23.3%) 说明 LIBERO spatial 可能属于"base model 已有好样本"的场景——VLA 生成的 N 个样本中有接近正确的，CRM 的修正反而破坏了它们。

---

## 4. Multi-Sample Action Aggregation 策略

### 4.1 现有方法

| 策略 | 代表工作 | 机制 | 优缺点 |
|------|---------|------|--------|
| **Argmin (SampleConsensus)** | ACR-VLA | 选 uncertainty 最低的样本 | 简单稳定；浪费其他样本信息 |
| **Temporal Ensemble** | ACT (Zhao et al., RSS 2023) | 重叠 action chunk 用 exponential weighting 组合 | 平滑 jitter 无 bias；仅跨时间步非跨样本 |
| **Population-based Selection** | GDP (NeurIPS 2025) | 去噪过程中生成群体，按 OoD fitness 选最优半数 | 在生成过程中即进行筛选，高效；需定义 fitness |
| **Flow Matching + Voting** | π0 / π0.5 (Physical Intelligence) | Flow matching 生成 action chunk，投票过滤噪声预测 | 高频控制；投票在 task-planning 层面 |
| **Residual RL + Distillation** | PLD (ICLR 2026) | RL 修正 + distribution-aware filtering + SFT 蒸馏 | 性能最优（LIBERO 99%）；流程复杂 |
| **One-step Newton Correction** | Rollout Then Optimize (2025) | 对 learned policy 的 rollout 施加单步 Riccati 修正 | 理论保证二次收敛；需可微模型 |
| **Conformal Filtering** | SCOPE-Gen (ICLR 2025) | Sequential conformal prediction 迭代剪枝 | 有统计保证；计算成本随样本数增长 |
| **Weighted Average by Confidence** | — | 按 confidence score 加权平均 | 简单；**破坏多模态结构**（已知失败模式） |
| **Truncated Mean** | — | 去掉极端值后取均值 | 对 outlier 鲁棒；仍可能 mode averaging |
| **Median** | — | 取各维度中位数 | 最鲁棒的 aggregation；同样 mode averaging 问题 |

### 4.2 关键发现

- **简单平均/加权平均在多模态 action distribution 下必然失败**：Diffusion Policy 的核心设计哲学就是避免 mode averaging，因此 weighted average 和 truncated mean 等方法在 VLA 场景下不适合
- **Temporal ensemble 是实践中最广泛采用的方法**：ACT 的 exponential-weighted temporal ensemble 被广泛使用
- **Population-based selection (GDP) 是最有前景的新范式**：在生成过程中即做筛选，兼顾效率和质量

---

## 5. ACR-VLA CRM 退化的可能解释

基于文献分析，CRM correction 退化的最可能原因（按可能性排序）：

### 5.1 Distribution Shift 导致 CP 保证失效
- CRM 的 conformal prediction 基于 exchangeability 假设
- LIBERO spatial 的 eval 分布与 CRM 训练分布存在 mismatch
- 文献 [Dabah & Tirer, ICML 2025; COVID-19 study, 2026] 一致表明：distribution shift 下 CP 的覆盖率可以从 ~87% 灾难性降至 0%
- **失效的 CP 给出错误的 uncertainty signal → CRM 向错误方向修正**

### 5.2 Correction Magnitude 无界
- CRM 的修正幅度没有显式约束
- 文献 [Zheng et al., ICML 2020] 理论证明无界修正必然在某些条件下导致退化
- **即使修正方向正确，过大的修正幅度也会 overshoot**

### 5.3 Cascading Error 在 Action Sequence 上累积
- CRM 修正的微小错误在 action chunk 的时间维度上传播
- 文献 [ReCAPA, 2026] 显示中间步骤的 mis-specification 会 cascade 到后续所有步骤
- **单步过度修正 → 整条轨迹偏离 → 任务失败**

### 5.4 Base Model 已有好样本但 CRM 破坏了它们
- SampleConsensus 42.9% >> Baseline 30% 说明 VLA 生成的多样本中确实存在好样本
- CRM 对所有样本施加修正（包括已经好的样本），反而将好样本推离最优
- 类似 [Ao et al., UAI 2023] 的"修复 over-confidence 时恶化 under-confidence"现象

### 5.5 Self-Correction 的内在局限
- 文献 [Huang et al., ICLR 2024; Kamoi et al., TACL] 一致发现：无可靠外部反馈的 self-correction 通常降低性能
- CRM 依赖自身的 uncertainty estimation 做修正，缺乏外部 ground truth signal

---

## 6. 建议的补救方向

### 6.1 短期修正（不改架构）

| 方向 | 具体做法 | 依据 |
|------|---------|------|
| **Correction magnitude clipping** | 限制 CRM 输出的 L2 norm 在 `[0, δ_max]` 内 | [Zheng et al., ICML 2020] 证明 error-bounded correction 的必要性 |
| **Confidence-gated correction** | 仅在 uncertainty > threshold 时施加修正，低 uncertainty 样本保持原样 | 避免对已经好的样本做 harmful correction |
| **Soft blending** | `a_final = α · a_corrected + (1-α) · a_original`，α 由 uncertainty 控制 | 介于 no correction 和 full correction 之间的连续谱 |
| **Correction rejection** | 如果修正后的 action 的 conformal score 比修正前更差，reject 此次修正 | 类似 Metropolis-Hastings 的 accept/reject |

### 6.2 中期改进（需要额外训练）

| 方向 | 具体做法 | 依据 |
|------|---------|------|
| **Population-based selection** | 借鉴 GDP，在 VLA 生成过程中即做 OoD-aware filtering | [GDP, NeurIPS 2025] 14 个任务上提升 20% |
| **Hybrid selection + correction** | 先 SampleConsensus 选 top-K，再对 top-K 做 bounded correction | 结合 selection 的稳定性和 correction 的精度 |
| **Domain-adaptive CP** | 用 LIBERO spatial 的少量数据 recalibrate conformal threshold | [COVID-19 study] 季度重训练恢复覆盖率 |
| **Residual RL correction** | 借鉴 PLD，用 residual RL 替代 learned CRM | [PLD, ICLR 2026] LIBERO 99% 成功率 |

### 6.3 长期方向

| 方向 | 具体做法 | 依据 |
|------|---------|------|
| **External feedback signal** | 引入 world model 或 reward model 作为 correction 的外部验证 | [SC-VLA, 2026] 用 auxiliary predictive heads 预测 task progress |
| **Adaptive correction regime** | 根据 task/distribution 自动选择 correction vs selection vs hybrid | 不同场景需要不同策略 |
| **Conformal + causal reasoning** | 结合因果推理避免 spurious correlation 导致的错误修正 | Distribution shift 的根本解法 |

---

## 参考文献

1. Xi et al., "Does Confidence Calibration Improve Conformal Prediction?" arXiv 2402.04344, 2024.
2. Dabah & Tirer, "On Temperature Scaling and Conformal Prediction of Deep Classifiers," ICML 2025. arXiv 2402.05806.
3. "Conformal Prediction Under Distribution Shift: A COVID-19 Natural Experiment," arXiv 2601.00908, 2026.
4. "Beyond Overconfidence: Foundation Models Redefine Calibration in DNNs," arXiv 2506.09593, 2025.
5. Gauthier et al., "Adaptive Coverage Policies in Conformal Prediction," arXiv 2510.04318, 2025.
6. Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet," ICLR 2024. arXiv 2310.01798.
7. Qingjie et al., "Understanding the Dark Side of LLMs' Intrinsic Self-Correction," ACL 2025. arXiv 2412.14959.
8. Kamoi et al., "When Can LLMs Actually Correct Their Own Mistakes?" TACL Vol. 12, 2024.
9. "ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures," arXiv 2604.21232, 2026.
10. Zheng et al., "Error-Bounded Correction of Noisy Labels," ICML 2020.
11. Ao et al., "Two Sides of Miscalibration," UAI 2023.
12. Wang et al., "Rethinking Calibration of DNNs: Do Not Be Afraid of Overconfidence," NeurIPS 2021.
13. Silver et al., "Residual Policy Learning," arXiv 1812.06298, 2018.
14. Jiang et al., "TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction," CoRL 2024.
15. Xiao et al., "PLD: Self-Improving VLA Models with Data Generation via Residual RL," ICLR 2026.
16. Dong et al., "RAFT: Reward rAnked FineTuning," arXiv 2304.06767, 2023.
17. Chi et al., "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion," RSS 2023.
18. Zhao et al., "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ACT)," RSS 2023.
19. "Two-Steps Diffusion Policy via Genetic Denoising (GDP)," NeurIPS 2025. arXiv 2510.21991.
20. "π0: A Vision-Language-Action Flow Model for General Robot Control," arXiv 2410.24164, 2024.
21. "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination," arXiv 2602.21633, 2026.
22. "SCOPE-Gen: Conformal Generative Modeling with Sequential Greedy Filtering," ICLR 2025. arXiv 2410.01660.
