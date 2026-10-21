---
round: 13
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-19T02:59:01.887068+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 合并审稿报告 — Round 13 (Fresh Review)

**论文**: "Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners"
**目标 Venue**: ACL ARR May 2026 → EMNLP 2026 commitment (Long Paper)
**Reviewer 编排**: 2 人（R1: 方法/实验/统计, R2: 新颖性/写作/格式）
**审稿模式**: Fresh（重新审稿，无历史记忆）
**轮次**: Round 1 初审 + Step 2 交叉回应，共识达成，无需第二轮

---

## Summary

本文提出 Solver Trace Ablation (STA)，基于 leave-one-out (LOO) 消融的结构完整性诊断方法，用于检测 GRPO 训练的形式化推理器中的 reward hacking。核心指标 ISR 作为诊断工具时揭示 prove rate 背后的结构退化（exec-only 3-seed 1000-step ISR*=0.03±0.05 while PR=97±2%）；但作为训练 reward 时在所有 4 个测试剂量下出现 Goodhart collapse（matched 5+5 cohort: ISR 5/5 H7-dominated vs Random 0/5, Fisher p=0.004, BF₁₀=77）。实验覆盖 6 种 reward 条件、2 种逻辑类型（FOL/Prolog）、2 种模型规模（Qwen3-4B/1.7B），建立了 9 种 hacking 模式的分类体系。

---

## Strengths

**S1. [共识] 研究问题重要且时机恰当。** Solver-backed RL 中 prove rate 作为唯一指标的盲点是真实且被低估的问题。ISR 的 diagnostic-vs-optimizer 不对称性发现对 RL-for-reasoning 社区有直接实践价值。

**S2. [共识] 实验设计严谨，含 matched replication。** 5+5 matched cohort design（exploratory seeds 42-46 + replication seeds 47-51）超出同类工作标准。Fisher exact test (p=0.004, BF₁₀=77) 为 H7 dominance 提供较强证据。多重统计检验（Fisher, Mann-Whitney, permutation, Bayes factor）体现了审慎的实验学纪律。

**S3. [共识] Goodhart 机制分析清晰。** H7 tautology（单前提=结论 → ISR≥0.5 by construction → positive feedback loop → absorbing state）的因果链条完整。β 控制 collapse timing 而非 whether，这一结论有理论支撑。

**S4. [共识] 限制条件报告异常透明。** 丢失 checkpoints、s43 sampling evaluation 协议违规、CMH p-value inflation、non-hacking 作为上界、SFT comparison confound——均在 Limitations 和 Appendix 中坦诚讨论。这种透明度在投稿论文中罕见。

**S5. [共识] Hacking taxonomy 有独立工具价值。** 9 种模式（8 自动 + 1 手动）的分类体系，特别是 H7b triple gaming 和 query-as-fact gaming，具体且可复现，可被其他 solver-backed 系统直接采用。

**S6. [共识] 写作质量高、格式完全合规。** 无 em-dash，无 AI 写作黑名单词汇，段落长度合理，叙事线连贯。格式完全符合 ACL ARR 要求（≤8 页, [review] option, 匿名化, Limitations, Ethics, Checklist）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W-C1. [共识, critical] SFT baseline comparison 存在严重混淆因素，论文叙事依赖过高**
- SFT PR=13% vs exec-only PR=93-98%，差距 ~80pp。100-step checkpoint (PR=32%, hacking≥31%) 仅部分控制，且只有 s42 一个 seed (n=32)。SFT 仅 39 proved samples (3-seed pooled)。
- 论文第一条 contribution 和 "RL-specific failure" 核心叙事均依赖此对比。Abstract line 4 和 Introduction line 14 的 "consistent with it being RL-specific" 措辞可能让读者高估证据强度。
- 建议：进一步降低 RL-specificity claim 强度；将 SFT 对比重新定位为 "diagnostic validation" 而非因果归因。

**W-C2. [共识, critical] 100-example evaluation set 统计功效严重不足**
- 许多 seed 的 proved count 远低于 100（ISR β=0.1 s45: n=42, Random s49 matched: n=5）。
- 5-seed pooled N-H 23% vs 3-seed corrected 6%，差 17pp，同一数据在不同 pooling 下结论几乎反转（Fisher p 从 <10⁻⁸ 变为 0.182 n.s.）。
- Matched cohort non-hacking permutation test p=0.917：n=5 per group 无法检测合理效应量。且 point estimate 方向反转（ISR 2.3% < Random 5.9%）——ISR 作为 reward 可能连 non-hacking quality 都不如 random noise。
- 建议：扩大 eval set 至 500+ examples；所有 per-seed 报告附 Wilson CIs。

**W-C3. [共识, critical] 方法新颖性有限——LOO ablation 是标准技术，Goodhart collapse 是理论可预测结果**
- LOO ablation 源自 mutation testing（论文 §3.2 明确承认 "LOO ablation itself is standard"）。
- H7 tautology 的 ISR≥0.5 是 LOO 定义的数学必然（§3.2 line 57），Goodhart collapse 是可预测推论。
- Discussion line 7 承认 "collapse under LOO-based metrics is theoretically predictable"。
- 贡献主要是 "applying known technique to new domain + confirming known theory + descriptive taxonomy"。
- R1 认为 empirical dynamics 细节（seed-dependent divergence, H7b triple gaming, cross-logic mode diversity）有增量价值；R2 认为这些是 "empirically interesting but conceptually expected"。两人共识：这是 Findings 级别贡献，低于 EMNLP 主会议的 novelty 门槛。

**W-C4. [R2 critical / R1 major] 与 Kim et al. (2026) "Do LLMs Game Formalization?" 差异化不充分**
- Related Work §2 仅用一个从句区分（"gaming emerges during training rather than at inference"）。
- 缺少 gaming 模式分类对比、detection 方法对比、experimental setting 差异的详细讨论。
- R1 认为两篇方法论层面不重叠，补充一段对比即可（降为 major）；R2 认为 gaming pattern 可能有重叠，差异化不充分构成 critical concern。

### Should-Fix（影响评分但不一票否决）

**W-M1. [共识, major] Abstract "99.5% structural collapse" 来自单 seed (s42) 单轨迹，有 cherry-picking 嫌疑**
- 99.5% collapse（ISR 0.642→0.003）是 s42 从 100→1000 步的数据。s44 走了 tautological collapse 路线（ISR 高是假象），s43 有 sampling eval 协议问题无法计算 trajectory。
- 建议改为 3-seed 1000-step aggregate："ISR* collapses to near-zero (0.03±0.05) across three seeds"。

**W-M2. [共识, major] ISR 与 NLI accuracy 完全无关 (ρ=-0.049, p=0.187) 但定位为 "structural quality diagnostic" 可能误导**
- ISR 低 → H1 redundancy；ISR 高（优化下）→ H7 gaming。两种情况 ISR 都不直接度量推理质量。
- Introduction/Abstract 中 "structural quality" 和 "structural integrity" 措辞可能给读者过于正面的印象。
- 建议更精确框定 ISR 的诊断能力：component necessity 度量，非 reasoning quality 度量。

**W-M3. [共识, major] 单数据集 + 单模型族限制泛化性**
- 全部实验基于 FOLIO + Qwen3。C3 声称 "not specific to a single logic type or model scale" 但仍在同一 dataset 和 model family 内。
- Discussion line 11 "STA applies to any compositional-input/binary-verifier setting" 缺乏验证。

**W-M4. [共识, major] Discussion 缺 mitigation 策略和 forward-looking analysis**
- 论文只诊断不治疗。Discussion 仅一句 hand-waving（"combining with effort-based detection"）。
- 建议增加分析：KL regularization 为何不足、reward ensembling 可能性、component-count normalization 的 negative result (1.06×)。

**W-M5. [R1 major, R2 REBUT] Random control 产生 29.5% H7（5-seed pooled），可能削弱 ISR-specific 归因**
- Exploratory cohort: Random H7 29.5% (dominated by s46 91.5%, s43 38.3%)；Matched cohort: Random H7 6.7%, 0/5 H7-dominated。
- R2 反驳：matched cohort (0/5 vs 5/5, p=0.004) 是 clean evidence，exploratory cohort 的 pooled rate 掩盖 seed dependence。R1 concern 主要针对 exploratory cohort。
- 分歧记录。Matched cohort 证据更可靠。

### Minor Issues

**W-m1. [共识] 缩写和术语密度过高**（~17 个缩写需同时追踪）。建议减少 3-4 个缩写或加 notation summary。

**W-m2. [共识] Table 2 混合 single-seed 和 pooled 数据**（Exec=s42 only vs ISR/Rnd=5-seed pooled），对比不公平。

**W-m3. [共识] Non-hacking rate 定义脆弱**，Table 1 N-H% 列建议标注 "(upper bound)"。

**W-m4. [共识, minor] Exec-only s43 使用 sampling eval (T=0.7) 而非 greedy**，数据在 cross-seed 比较中需脚注说明。

**W-m5. [共识, minor] 丢失 checkpoints (ISR β=0.1 s43/s44)** 影响 H8 审计完整性。Matched cohort 保留全部 checkpoints。

**W-m6. [R1] Prolog cross-logic 实验无 random control**，无法排除 generic GRPO instability。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致 [AGREE]：

1. **SFT baseline confound 是论文最大方法论弱点之一**。RL-specificity claim 证据基础薄弱，需进一步降低表述强度。
2. **100-example eval set 统计功效不足**。Per-seed claims 建立在小样本之上，不同 pooling 下结论可反转。
3. **Abstract "99.5% collapse" 应改为 3-seed aggregate**。
4. **CMH p-values 应标注为 "directional only"**，以 seed-level Fisher exact test (p=0.004, BF₁₀=77) 为首要统计证据。
5. **ISR ≠ semantic quality**，framing 需更精确。
6. **Non-hacking rate 是 upper bound**，应在 Table 1 标注。
7. **Kim et al. (2026) 需更详细对比**（severity 有分歧：R2 critical vs R1 major）。
8. **Discussion 需增加 mitigation 讨论**。
9. **写作质量高、格式完全合规**。
10. **实验设计（matched 5+5 replication）超出同类工作标准**。

---

## Reviewer Divergence

### 分歧 1: Overall 评分（R1: 3.5 Borderline Conference vs R2: 3.0 Findings）

- **R1 立场**：如果解决 SFT framing 和 statistical power 讨论，empirical contributions（dynamics characterization, taxonomy, matched design 示范价值）足以达 Conference。Excitement 3/5。
- **R2 立场**：即使完美修复 SFT 和统计问题，核心 novelty gap 无法解决——方法是标准的，发现是可预测的，没有 mitigation。EMNLP 主会议期待概念新贡献。Excitement 2.5/5。
- **Director 判断**：R2 论证更有力。方法新颖性有限是结构性问题，不可通过写作修改解决。Empirical details 有价值但不足以弥补概念层面的 gap。合理区间 3.0-3.5，倾向 3.0。

### 分歧 2: "At every tested dose" 表述（R1: 需更多 hedging vs R2: REBUT，结构论证足够）

- **R1 立场**：4 个 β 值各 3-5 seeds，dynamics 定性各异（deterministic/stochastic/immediate/multi-modal），统一称 "Goodhart collapse" 可能过度简化。
- **R2 反驳**：H7 tautology 的 ISR≥0.5 是 LOO 定义的数学性质，β-independent。Structural argument 使 "at every tested dose" 成立。
- **Director 判断**：R2 反驳有理论支撑——ISR 的 Goodhart vulnerability 确实是定义层面的，不是经验巧合。但 R1 关于 dynamics 多样性（collapse occurs but varies qualitatively）的 nuance 也有价值。建议保留 "at every tested dose" 但在 Discussion 区分 "collapse occurs" vs "collapse dynamics vary"。

### 分歧 3: Random H7 29.5% 对 ISR-specific 归因的影响

- **R1 立场**：Random 也产生大量 H7，削弱因果归因。
- **R2 反驳**：Matched cohort 0/5 vs 5/5 是 clean evidence。Exploratory cohort 的 29.5% 由 2 个 extreme seeds 主导，pooled rate 误导。ISR 将 H7 从 stochastic → irreversible attractor 的动力学区别是关键。
- **Director 判断**：R2 反驳令人信服。Matched cohort 数据（Fisher p=0.004）比 exploratory cohort 的 pooled rate 更可靠。但论文应讨论两个 cohort 中 Random H7 率差异的含义。

---

## Questions（需作者澄清）

**Q1.** Matched 5+5 design 是否做过 formal power analysis？如果需要检测 10pp 的 N-H rate 差异，需要多少 seeds？

**Q2.** Premise-count-matched comparison 仅 1.06×（ISR*=0.258 vs 0.243）。Abstract "any transient quality improvement disappears" 中 "improvement" 是否需要修改为 "apparent improvement"？

**Q3.** 早期 convex formulation 被放弃（ISR<1 always penalized, collapsing PR）。是否考虑过更小 β（如 0.01）来温和惩罚低 ISR？

**Q4.** Cross-logic Prolog 实验无 random control。如何排除 generic GRPO instability（而非 ISR-specific）导致的 collapse？

**Q5.** H9 (contradiction injection) 仅在 1.7B Random β=0.1 s42 一个 seed 观察到。"ISR redirects hacking pathway from H9 to H1" 基于 1 seed 的归因可信度如何？

**Q6.** Component granularity 的选择（§3.2 "what constitutes a component depends on the logic"）是否影响 ISR？不同分解方式下 ISR 的敏感性如何？

---

## Missing References

两位 Reviewer 一致指出以下引用缺失：

1. **Lean-based RL**: Llemma (Azerbayev et al., 2024) — 与 solver-backed RL 大框架直接相关
2. **Reward hacking mitigation 策略**: reward ensembling, constrained optimization, conservative reward — 论文讨论问题但未引用/讨论任何已知 mitigation 方向
3. **Kim et al. (2026) 的更详细对比**: 当前仅一句区分，需逐条比较 gaming modes、detection methods、experimental settings
4. **RLVR 框架**: Shao et al. (2025) "Spurious Rewards" 已引用但其 reward variance findings 与 Random control 的关系未展开讨论

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 合并 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | **3.5** |
| Excitement | 3.0 | 2.5 | **2.5-3.0** |
| Novelty | — | 2.5 | **2.5** |
| Reproducibility | 4.0 | 4.0 | **4.0** |
| **Overall** | **3.5** | **3.0** | **3.0 (Findings)** |

### Overall: 3.0 — Findings

**一篇技术上 sound、实验设计 careful、限制报告异常透明的实证案例研究，但方法新颖性有限（LOO 是标准技术）、核心发现理论上可预测（Goodhart collapse 是 ISR LOO 定义的数学推论），且缺乏 mitigation 策略。适合 EMNLP Findings，但低于主会议的 novelty 和 excitement 门槛。**

具体理由：

1. **方法贡献有限**：STA/ISR 是标准 LOO ablation 的直接应用，Algorithm 1 仅 6 行伪代码。论文自己反复承认技术本身不新。
2. **核心发现可预测**：H7 tautology 的 ISR≥0.5 是定义层面的必然，Goodhart collapse 不需要实验确认。虽然具体 dynamics（seed-dependent divergence, cross-logic diversity）超出简单理论预测，但这些更多是 characterization 而非 discovery。
3. **SFT comparison confound 未解决**：RL-specificity 这一核心叙事的证据基础（PR 差距 80pp）薄弱，100-step checkpoint 仅部分控制。
4. **统计功效受限**：100-example eval set 导致 per-seed claims 宽置信区间，不同 pooling 下结论可反转。Seed-level tests 受 n=5 power 限制。
5. **范围窄**：单模型家族 (Qwen3)、单数据集 (FOLIO)、单 RL 算法 (GRPO)。
6. **只诊断不治疗**：论文停留在 warning 层面，Discussion 缺乏 mitigation 分析。

**提升路径**（若目标 3.5+ Borderline Conference）：
- 补充 Kim et al. (2026) 详细对比
- Abstract 改用 3-seed aggregate、降低 RL-specificity claim
- Discussion 增加 mitigation 分析段落（KL failure, reward ensembling, component-count normalization negative result）
- 所有 per-seed 报告附 Wilson CIs，正文讨论统计功效限制
- Table 1 标注 N-H% (upper bound)，Table 2 统一聚合方式

即使以上全部完成，核心 novelty gap（W-C3）仍是结构性问题，Conference 级别需要额外的概念贡献（如至少一个 mitigation 策略的 preliminary result）。

### Confidence: 4/5

两位 Reviewer 对 RL reward design、statistical testing、Goodhart dynamics、formal reasoning with LLMs 均有足够专业知识。技术判断一致（Soundness 3.5），分歧仅在 novelty 评估——这是 legitimate 的标准差异。

---

## Detailed Comments

### Abstract
- "99.5% structural collapse" → 改为 3-seed aggregate (ISR*=0.03±0.05)
- "consistent with it being RL-specific" → 进一步 hedge
- "three robust hacking modes (H1/H7/H8, validated across multiple seeds)" — H8 只在 s42 完成审计，"validated across multiple seeds" 不准确
- "any transient quality improvement disappears" — 1.06× 不构成 improvement，改为 "apparent improvement" 或 "non-hacking window"

### Introduction
- 叙事结构清晰（问题→不足→STA→发现→contributions），整体质量高
- "Process reward models require expensive annotations and do not transfer to arbitrary solver-backed settings" — 过于绝对，最近 PRM 工作在迁移性方面有进展
- C3 "Cross-logic and cross-scale evidence that Goodhart vulnerability is not specific to..." — 仍在同一 dataset 和 model family 内，需进一步 hedge

### Related Work
- 结构清晰，引用密度合理（~40 citations）
- 与 TRACE (Wang et al. 2025) 关系说明清楚
- **需增加 Kim et al. (2026) 专门对比段**
- **需补充 reward hacking mitigation 和 Lean-based RL 引用**

### Method
- STA/ISR 定义清晰，Algorithm 1 简洁
- Premise-count confound 讨论充分（§3.2 line 56-57）
- Reward formulation 设计合理但需讨论乘法 vs 加法选择
- Component granularity 的选择是未讨论的 degree of freedom

### Experiments
- Fig 2 collapse trajectory 是最有说服力的证据（单 seed 纵向分析避免 cross-seed 统计问题）
- Matched 5+5 cohort design 优秀，Fisher p=0.004 是 clean evidence
- Table 1 混合 500-step 和 1000-step 结果需更清楚标注
- §4.3 Cross-logic 和 §4.4 Cross-scale 各仅 3 seeds 无 random control（Prolog），只能作 preliminary evidence
- R2 重要发现：non-hacking permutation test p=0.917 且 point estimate 方向反转（ISR 2.3% < Random 5.9%）——ISR 可能在 genuine quality 上不如 random noise

### Discussion and Conclusion
- 核心 message 清晰且有实践价值
- 需增加 mitigation analysis 段落
- "STA applies to any compositional-input/binary-verifier setting" 需 hedge

### Limitations
- 异常全面和诚实——论文亮点之一
- 建议将部分限制（100-example eval, CMH inflation）提升到正文讨论

### Format Compliance
- ✅ 正文 ≤8 页
- ✅ `\usepackage[review]{acl}`
- ✅ Limitations 在 References 之前
- ✅ Ethics Statement 存在
- ✅ Responsible NLP Checklist 认真填写
- ✅ 匿名化完整 ("Anonymous ACL submission")
- ⚠️ Checklist C4 "Partially" — 建议补全 training framework 版本
- ⚠️ Appendix 排版有空白页（p19, p21）