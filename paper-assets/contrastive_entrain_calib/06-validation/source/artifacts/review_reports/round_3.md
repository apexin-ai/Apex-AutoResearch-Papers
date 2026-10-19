---
round: 3
review_mode: fresh
overall_score: 2.5
timestamp: 2026-05-22T12:56:26.624737+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# Round 3 审稿报告

**论文**: *Discriminability Without Utility: Why Sycophancy Directions Fail as Scalar RL Rewards*
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验有效性；R2: 新颖性 + framing 完整性）
**轮次**: 1 轮初审 + 1 轮交叉回应（关键问题达成共识，无需第二轮）

---

## Summary

论文提取了 contrastive sycophancy direction (d_syc)，在 Qwen3-8B (AUROC 0.827) 和 Llama-3-8B (AUROC 0.779) 上验证了其 discriminability，然后测试了三种将 d_syc 转化为 GRPO reward 的方法（cosine projection 4 变体、binary probe、continuous probe）以及 R3-only GRPO ablation 和 ACT baseline。所有 GRPO formulations 在 Qwen3-8B 上均失败。论文提出"discriminability ≠ reward utility"的概念框架解释失败原因。

---

## Strengths

**S1** [共识] 研究问题重要且及时——representation engineering → RL reward 是社区自然关注的方向，系统验证其失败模式有明确价值。

**S2** [共识] Probe reward trap (C2) 是独立有价值的新颖发现——behavioral death 先于 distributional collapse 的 1,300-step 时序分析（Figure 2, Table 3）提供了 RLHF 失败模式的有用 characterization，对 practitioners 有直接实践警示。

**S3** [共识] 跨模型验证增强可信度——Qwen3-8B 和 Llama-3-8B 两个架构上 d_syc 的一致结果（Table 1）排除了 model-specific artifact 的解释。

**S4** [共识] 与 Papadatos & Freedman (2024) 的对比分析精到——同一 probe 在 inference-time (Best-of-N) 成功但 training-time (GRPO reward) 失败，精准定位了"inside vs outside optimization loop"的关键区分（§7）。这是论文最有洞察力的分析之一。

**S5** [共识] d_syc 方向本身验证扎实——5-fold CV、evidence strength 分层、per-layer AUROC 分析、recalibration 机制和 probe ablation 显示了系统性 methodology。

**S6** [共识] 失败诊断链（gate saturation → gradient vanishing → mode collapse → behavioral death → stubbornness trap）对 practitioners 有参考价值，Stubbornness taxonomy (Appendix B) 的三种 failure mode 提供了有价值的定性补充。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, 共识] **GRPO group_size=2 严重偏离标准实践，构成致命替代解释**
- Table 5 (Appendix A) 显示 group_size=2，而标准 GRPO（Shao et al., 2024）使用 64，后续文献下限为 8-16。group_size=2 退化为噪声极高的 pairwise 对比，advantage 估计方差极大。
- 无法区分两种解释：(a) d_syc reward 信号本质不可用；(b) d_syc 信号微弱但可用，group_size=2 的 GRPO 无法提取有效梯度。解释 (b) 未被排除。
- R1 首提，R2 交叉回应中强烈同意并补充：这也可能是 probe reward trap (ToF→0 at step 500) 的直接原因——不是 probe 的 structural failure，而是 group_size=2 导致的 optimization instability。
- **建议**: 补充 group_size ∈ {8, 16} 消融实验。

**MF2** [critical, 共识] **max_completion_length=256 导致 80-84% truncation，可能是 reward failure 的直接原因**
- 3-turn 对话 256 tokens 远不足以生成完整响应。reward 在 truncated output 上计算，cosine/probe 可能不反映完整响应的 sycophantic 倾向。
- R2 补充：truncation 还导致 RL 训练中 reward 的 non-stationarity 远超正常水平，与 Figure 3 的 stochastic oscillation 可能有因果关系。
- 论文的"shared across conditions"辩护只保证公式间相对比较有效，不支持 d_syc 本质失败的绝对声明。
- **建议**: 至少一个 config 测试 max_completion_length=512/1024。

**MF3** [critical, 共识] **标题和 claims 范围显著超出实验证据**
- 标题"Sycophancy Directions Fail as Scalar RL Rewards"暗示对所有 scalar RL rewards 的普遍结论，但仅测试 GRPO。PPO、RLOO、REINFORCE、DPO 均未测试。
- §8 自己承认"whether they exhibit similar failures remains an open question"，与标题的普遍性声明直接矛盾。
- C1 用了"Every tested GRPO formulation"的限定，比标题更谨慎——标题与正文 contributions 之间存在 scope 不一致。
- **建议**: 标题改为"…as GRPO Rewards"或"…as Scalar Per-Completion Rewards: Evidence from GRPO"；或补充 PPO/REINFORCE 实验。

**MF4** [critical, 共识] **C3 将 confounded observation 包装为 contribution**
- C3 声称"sparse RL reward failed to convey the valid/invalid distinction"，核心证据来自 ACT 成功而 GRPO 失败。但 ACT 与 GRPO 至少在 5 个维度上不同：训练范式（SFT vs RL）、监督粒度（per-token vs per-completion）、labeled pairs 使用、loss function（L2 vs reward maximization）、LoRA capacity (~1.75× 参数差异）。
- §6 承认"this gap is an observational finding, not a controlled comparison"，但 C3 仍以 contribution 形式呈现——存在逻辑矛盾。
- R1 最初列为 Should-Fix，交叉回应后同意 R2 的 critical 级别判断。
- **建议**: C3 降格为 observation/hypothesis，明确列出所有 confounding factors，移除因果语言。

**MF5** [critical, 共识] **仅 2 random seeds，负面结论证据标准不足**
- RL 训练高方差，2 seeds 无法提供有意义方差估计。"4/26 checkpoints exceed vanilla"的可靠性完全依赖 2 seeds 的代表性。
- R2 补充：SYCONSCORE 的 harmonic mean 当 ToF 或 NoF 为 0 时自动归零，因此 Table 4 中全部为零可能是指标设计的 artifact（对零值极端敏感）而非 truly consistent failure。ToF/NoF 原始值的 variance 未报告。
- 负面结论证据标准应高于正面结论——如果存在 5% 概率某 seed 成功，结论即被推翻。
- **建议**: 增加到 3-5 seeds 并报告 mean ± std。

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, 共识] **Wu & Tang (2026) "geometric separability"论点缺乏定量支撑**
- §6 定性论证 d_syc 不够 separable，但未量化。d_syc AUROC 已达 0.827，"separability 不足"并非不证自明。
- 需要定量分析：如 d_syc 在 online 分布下 valid vs sycophantic 的 cosine 分布重叠度，与 Wu & Tang 场景对比。

**SF2** [warning, 共识] **"Discriminability ≠ Reward Utility"泛化声明超出证据**
- 该原则仅在 sycophancy + GRPO + 两个 8B 模型上验证。§8 泛化到其他 behavioral attributes 是 speculative。
- 建议表述改为"our results suggest"/"we hypothesize"。

**SF3** [warning, 共识] **SMART (Beigi et al., 2025) 讨论过于简略**
- SMART 的 per-step process reward 是 per-completion（GRPO）和 per-token（ACT）之间的中间监督密度，与论文核心发现直接相关。
- 如 SMART 部分成功，为"密度是关键因素"提供证据；如也失败，加强"问题在 d_syc 本身"的论点。无论如何应深入讨论。

**SF4** [warning, 共识] **Reward 设计空间探索偏窄**
- w₁ 仅测试 0.25/0.40，间距仅 0.15。w₁=0.25 时 d_syc 仅贡献 ~8.3% reward 方差。
- Multi-layer aggregation 未探索——Figure 1 显示不同层有不同信号，仅用 best single layer 可能丢失信息。
- R2 部分反驳：概念论证（d_syc 不携带 valid/invalid 信息→MLP 也无法改善）有逻辑支撑，但 w₁ 范围和 multi-layer 批评仍有效。

**SF5** [warning, 共识] **181 contrastive pairs 质量控制不足**
- GPT-4.1 生成 + automated style validation，无人工验证/IAA。Evidence strength 三级标注为单一标注者。
- 需至少对一个 subset 人工验证并报告 agreement rate。

**SF6** [warning, 共识] **SYCONSCORE harmonic mean 选择未 justify，可能掩盖部分改善**
- harmonic mean 当 ToF=0 时自动归零，可能 mask 部分 ToF 改善。论文应 justify 选择（引用 F-score 类比）并补报 ToF/NoF 独立数值和 confidence interval。
- 补报 arithmetic mean 作为 sensitivity analysis。

### Minor Issues

- §6 cross-seed rank correlation "ρ≈0.33 (n.s.)" 统计描述可能有误——2 个 seed 的 Spearman rank correlation 只能取 +1/-1，需明确计算方式（R2 交叉回应识别）
- Table 2 "mode collapse"/"gate saturation" 缺操作性定义
- Figure 1 y 轴标签未在 caption 中解释
- §6 "semantic gap" 是核心概念但未形式化——可考虑简单形式化
- Appendix B stubbornness taxonomy 仅 100 条、无 inter-rater reliability
- Abstract 信息密度极高（~250 words）——R1 认为在 *ACL 可接受范围，R2 建议精简（轻微分歧，recorded）

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上完全一致 [AGREE]：

1. **GRPO group_size=2 + 80-84% truncation 构成致命 confounds** (MF1+MF2)：无法区分"d_syc 本质失败"和"GRPO 优化配置不足"两种解释。这是本轮审稿识别到的**最核心问题**。
2. **标题/claims overclaiming** (MF3)：仅测试 GRPO 但标题声称 Scalar RL Rewards。
3. **C3 confound → contribution 的逻辑矛盾** (MF4)：§6 承认无法归因但 C3 仍用因果语言。
4. **2 seeds 不足以支撑负面结论** (MF5)：证据标准应高于正面结论。
5. **Probe reward trap (C2) 是最有独立价值的发现**：但其 failure 归因可能受 MF1/MF2 影响。
6. **Papadatos & Freedman 对比分析是论文最有洞察力的部分**。

---

## Reviewer Divergence

仅一项轻微分歧（已在交叉回应中解决）：

- **R1-N4 (Reward 设计空间探索) 的 severity**：R1 列为 critical，R2 部分 [REBUT]——论文的概念性分析（d_syc 不携带 valid/invalid 信息→更复杂变换也无效）部分缓解了 MLP/non-linear 变体的必要性，但 w₁ 搜索范围和 multi-layer aggregation 批评有效。R2 建议降为 Should-Fix。→ 最终采纳 R2 判断，列为 SF4。

---

## Questions

1. group_size=2 的选择理由是什么？是否有预实验表明更大 group_size 在此 setting 下计算不可行？
2. 是否有对 truncated vs non-truncated samples 的 reward 分布分析？
3. §6 的 cross-seed rank correlation "ρ≈0.33" 具体是如何计算的？（2 data points 无法产生此值）
4. ACT 和 GRPO 的 LoRA 配置差异（4 vs 7 modules, ~1.75× 参数）是否经过消融验证？
5. 是否考虑过将 d_syc 用于 DPO preference ranking 而非 scalar GRPO reward？

---

## Missing References

- 论文已涵盖主要相关工作（Papadatos & Freedman, Wu & Tang, SMART, CRAFT, Latent-GRPO）。
- 建议深化 SMART 讨论（SF3）和 Wu & Tang 定量对比（SF1）。
- DPO/KTO 在 sycophancy mitigation 中的应用可考虑在 §7 或 §8 简要讨论。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2 warnings, 4 info）：

**Warnings:**
- 前 3 页无 figure/table，审稿人翻到 page 4 才看到首个视觉锚点——建议 page 2 前插入概念总览图或核心结果 teaser figure
- Appendix B 仅占页面约 25%，剩余 75% 空白——建议与 Appendix A 合并或扩充内容

**Info:**
- Table 3（probe trajectory）列数多，单栏排版可能偏小，建议 table* 全宽排版
- Table 4 ACT (seed 2) 标注"ongoing: 4/16 ckpts evaluated"——在正式投稿中给人 work-in-progress 印象
- 全文 3 个 figure 均为折线图，缺少概念性图示（framework overview）
- Figure 3 彩色折线区分度有限，建议辅以不同 line style 和 marker shape

---

## Overall Assessment

**Overall Score: 2.5 (Borderline Findings)**

**评分理由：**
论文提出了有价值的概念框架（discriminability ≠ reward utility），probe reward trap 的时序分析（C2）是新颖的实证发现，d_syc 方向的 cross-model 验证扎实。然而，作为一篇负面结果论文（negative result paper），其核心结论受到多个严重的未控制 confounds 削弱：

1. **GRPO group_size=2** 和 **80-84% response truncation** 构成致命替代解释——无法区分"d_syc reward 本质不可用"和"GRPO 优化配置不当"。
2. **标题和 C3 overclaiming**——仅测试 GRPO 但声称对 Scalar RL Rewards 的普遍结论；confounded ACT vs GRPO 对比被包装为 contribution。
3. **仅 2 seeds** 不足以支撑负面结论的证据标准。

论文有潜力达到 Findings 水准，但需要补充 **group_size 和 completion_length 的消融实验**以排除 optimizer 配置这一强替代解释，并需要**收窄 claims scope**使其与实验证据匹配。

**两位 Reviewer 均给出 2.5 分（Borderline Findings），交叉回应后完全一致。**

**置信度: 4/5**（两位 Reviewer 均熟悉 RL alignment、representation engineering 和 sycophancy 文献）

---

## Detailed Comments

### §1 Introduction
- C1 的"Every tested GRPO formulation"限定词比标题更谨慎——标题应与正文对齐
- C3 的因果语言与 §6 的 observational disclaimer 矛盾——统一措辞
- 数字密度高（AUROC, CV σ, checkpoint counts），建议简化引言中的重复数字

### §2 Experimental Framework
- group_size=2 和 max_completion_length=256 应在正文中 justify，而非仅在 Appendix 提及
- w₁ 选择描述为"diagnostic-driven iteration"但实质是仅 2 个值——需更诚实的措辞
- 181 pairs 的 GPT-4.1 生成流程已描述，但缺少内容正确性的人工验证

### §3 Direction Discriminability
- 最扎实的章节——5-fold CV、cross-model、evidence strength gradient 验证充分
- 建议补充 post-attention vs post-MLP residual stream 的明确说明

### §4 Cosine R1
- 失败诊断链逻辑清晰，但 failure mode 术语（gate saturation, mode collapse）需操作性定义
- Table 2 cosine gap "averages only 0.098"——是否受 group_size=2 的高方差采样影响？

### §5 Probe Reward Trap
- 最有价值的实证章节——但 behavioral death 的归因需排除 truncation artifact
- "entropy remained healthy"应给具体数值范围
- 如补充 group_size=8 实验后 trap 仍存在，则 C2 的独立价值大幅增强

### §6 Analysis
- "unified root cause"叙事依赖 ACT 对比——在 confounds 未解决前，这个归因不够稳固
- cross-seed rank correlation "ρ≈0.33" 统计描述需修正
- "semantic gap"概念有价值但未形式化

### §7 Related Work
- Papadatos & Freedman 对比是亮点
- SMART 讨论需扩展——作为中间监督密度案例与核心论点直接相关
- Wu & Tang 对比需定量支撑

### §8 Conclusion
- 泛化声明应降级为 hypothesis
- "discriminability ≠ utility"原则在单一 case study 基础上需更谨慎表述

### Limitations
- 覆盖了主要限制但措辞可更强——特别是 group_size=2 和 truncation 应显式列出
- "Other RL algorithms (PPO, DPO) may interact differently"应从 Limitations 提升到主文的 scope qualification