---
round: 8
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-18T15:27:19.897869+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 8

**论文**: Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary
**Venue**: EMNLP 2026 (ARR May 2026)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性 + 实验有效性；R2: 新颖性 + 完整性 + 写作质量）
**轮次**: Round 1 独立审稿 + 交叉分享，1 轮收敛

---

## Summary

本文首次定义并系统测量递归合成文本的 generational discrimination boundary K*（相邻代际可区分的最大深度）。使用 15 维统计特征和 OBD-LightGBM 分类器，在 9 个模型配置（5 架构族，1B-14B）、3 个源域、4 种解码策略下测量 K*。核心发现：web text K*=2（8/9 配置），arXiv K*=3，Wikipedia K*=1，呈现域依赖的有界饱和模式。Cross-model transfer 保留 80-92% 精度。Downstream filtering 验证 K*=2 正确预测 binary filtering 为 web text 最优策略。

---

## Strengths

**S1** [两位共识] 研究问题定义精准新颖。K* 将 model collapse 从 population-level 现象转化为 per-text 可测量的 discrimination boundary，填补了 binary detection 与 model collapse 理论之间的空白。据两位 Reviewer 所知，无 prior work 显式定义和测量 adjacent-generation discrimination boundary。

**S2** [两位共识] 实验设计系统全面。9 配置 × 3 域 × 4 解码策略 × 10+ ablation studies，覆盖 model scale、architecture family、generation mode、scorer choice、feature subset、segment length 等维度。统计严谨性超过领域大部分工作（bootstrap CI、permutation test、Holm-Bonferroni、ANOVA、GroupKFold）。

**S3** [两位共识] 边界案例处理诚实透明。Mistral K*=1、Qwen-cont marginal、LLaMA borderline、Wikipedia scorer confound、OLMo arXiv capacity failure 均被主动报告和讨论。Limitations 异常全面（8 条 + 扩展限制）。

**S4** [两位共识] Domain ordering 发现有理论价值。arXiv(3) > C4(2) > Wikipedia(1) 的一致 ordering 在全 θ 范围 [0.55, 0.70] 保持不变，跨 6 个模型和 4 个架构族验证。

**S5** [R1] 从 K* 测量到 binary filtering 预测到 downstream validation 的逻辑链条完整。

**S6** [R2] 写作质量良好，正文控制在 8 页内，无破折号违规（符合用户自定义规则），引用覆盖合格（37 条 bib 全部被引用）。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [critical, 两位共识, R1-N1 = R2-N2] **θ=0.60 阈值 post-hoc 选择，缺乏独立验证**

θ=0.60 被描述为 "data-driven operational threshold, chosen at the empirical discontinuity in the AUC distribution"（Section 3.1），但该 discontinuity 正是 1v2 AUC cluster (0.61-0.70) 与 2v3 cluster (0.55-0.59) 之间的间隔。阈值选在分开这两个 cluster 的位置后用于定义 K*=2，构成循环论证风险。K*=2 的稳定窗口仅 5pp（θ∈[0.575, 0.625]）；θ=0.55 使两个 Qwen 配置升至 K*=3，θ=0.625 使 OLMo 降至 K*=1。Permutation test (p<0.002) 和 sensitivity analysis 提供部分支持，但不能替代独立验证。

**建议**：(1) held-out domain 或 model family 独立验证 θ；(2) 将 θ 作为参数报告 K*(θ) 范围而非固定单一值；(3) 明确承认 θ 是 post-hoc 选择。R2 补充：domain ordering 在全 θ 范围保持不变，说明相对结构比绝对值更稳健，可作为辩护。

**MF-2** [critical, 两位共识, R2-N1, R1 AGREE] **prompt-chain 与现实 retrain-chain 的差距削弱核心 practical claim**

所有主实验使用 prompt-chain，但现实 web contamination 涉及 retrain-chain（或混合）。Appendix 中 retrain-chain K*≥4（Pythia-1.4B LoRA），远超 prompt-chain K*=2。这意味着：(a) "binary filtering 即可" 的 practical prescription 可能在 retrain-chain 下失效（graduated filtering 可能有效）；(b) one-wash laundering 仅适用于 prompt-chain。Introduction 声称 prompt-chain "isolates generation-level information loss from training dynamics"，学术上合理，但 Contribution (c) 和 Conclusion 的 practical framing 未充分限定 prompt-chain 前提。retrain-chain 实验仅 1 个模型，覆盖不足。

**建议**：(1) Section 5 和 Conclusion 正文中显著标注 prompt-chain 限定；(2) 将 retrain-chain 对比提升至正文（至少一段）；(3) 理想情况增加混合场景实验或更多 retrain-chain 模型。

**MF-3** [critical, 两位共识, R1-N3, R2 AGREE] **"Domain as sole dominant factor" 过度声称**

Section 4.5 段落标题使用 "Domain as the sole dominant factor"，但：(a) ANOVA Generator η²_p = 0.885 是大效应量，远非可忽略；(b) 仅 3 个 domain 无法支持排他性结论，domain 之间存在大量混杂变量；(c) Mistral C4 K*=1 说明 model identity 确实影响 K*。R2 补充：正文已使用 "the primary determinant"（L142），标题与正文不一致。

**建议**：将标题改为 "Domain as the primary factor"，与正文措辞对齐；增加更多 domain 或明确 3-domain 的比较性结论限制。

### Should-Fix（影响评分但不一票否决）

**SF-1** [warning, 分歧→降级, R1-N2 critical, R2 REBUT→should-fix] **DPI 论证到有限 K* 的跳跃缺乏严密性**

DPI 保证 I(X; Y_k) 单调递减，但 pairwise AUC_{k-1,k} 是不同的量。从 "information degrades monotonically" 到 "finite K*" 需要 G_δ contraction rate 有下界等额外假设。R1 列为 critical。R2 反驳：论文使用 "motivates"（非 "proves"），K*_theory 仅出现两次作为 motivation，核心贡献是 K*_empirical，应降级为 should-fix。

**最终共识**：should-fix。补充 "under mild regularity conditions" 限定即可。

**SF-2** [warning, 两位共识] **Qwen 家族 5/9 配置导致聚合统计偏向**

"8/9 configurations yield K*=2" 中 5 个来自 Qwen 家族（scale/base-instruct/mode 变体）。应报告为 "4/5 architecture families yield K*=2"，避免将 Qwen 内部变体与跨家族变体混为一谈。

**SF-3** [warning, 两位共识] **下游 filtering 实验生态效度有限**

100% synthetic 极端设定，仅 MMLU + HellaSwag 两个 task，绝对改善 ~0.8pp。Dose-response（10-50% contamination）显示合成数据在这些比例下是 net-beneficial 的，filtering 必要性本身存疑。Pythia replication 的 MMLU baseline 仅 0.2568（near-chance），strategy ordering 可靠性需质疑。

**建议**：将 filtering 贡献重新框定为 consistency check / proof of concept 而非独立实际效益证明。

**SF-4** [warning, 两位共识] **Cross-model transfer matrix 仅覆盖 4/9 配置**

Table S1 仅含 Qwen-rw/Pythia/OLMo/Qwen-cont，"80-92% retention" claim（Introduction contribution (c)）缺少 LLaMA/Mistral/Qwen-7B/14B 数据。Cross-scorer feature ranking (ρ>0.90) 部分支持 feature transferability，但 classifier-level transfer retention 仍缺 5 个配置。

**建议**：补充 Qwen-7B 和 LLaMA-8B 的 transfer 数据；或限定 retention claim 适用范围。

**SF-5** [warning, 两位共识] **Cross-scorer 不稳定性未被充分反映**

Qwen-cont cross-family scoring K*: 2→1（Table S13）。"largely robust to scorer choice" 措辞与此例外不完全匹配。C4 域 5/7 条件保持 agreement，confound 影响是局部的非系统性失效，但正文应更显著讨论。

**SF-6** [warning, 两位共识] **"One-wash laundering" 在 Abstract 中表述有歧义**

Abstract "A single generation pass suffices to render general web text indistinguishable from deeper synthetic content" 可误读为 human text 经一次生成后即不可区分（与 0v1 AUC ≥ 0.92 矛盾）。实际含义是 gen-1 → gen-2 后不可区分。

**建议**：改为 "A single additional generation pass suffices to render first-generation synthetic web text indistinguishable from deeper synthetic content"。

**SF-7** [warning, 部分共识] **arXiv K*=3 cross-scorer CI 仅 2/4 generators confirmed**

Table arxiv_crossscorer_ci 显示 strict CI-confirmed 仅 Qwen-1.5B（CI lower=0.617）和 LLaMA-8B（CI lower=0.605）；Mistral-7B 和 Qwen-7B CI 跨越 θ。Contribution (b) 的 "five-model cross-validated" 措辞在 cross-scorer 条件下需标注此限制。（注：R1 反驳 n=2,200 不足的论据，认为 power curve 针对不同 boundary pair 不可直接套用。）

---

## Reviewer Consensus

以下问题两位 Reviewer 达成 [AGREE] 共识：
- θ=0.60 post-hoc 选择是最核心的需要 address 的问题
- prompt-chain 的 practical claim 需限定
- "sole dominant factor" 应降级为 "primary"
- Qwen 5/9 聚合偏向需要 family-level 报告
- Filtering 实验应框定为 proof of concept
- Transfer matrix 不完整，retention claim 需限定
- Cross-scorer 不稳定性需更显著讨论
- One-wash 隐喻需精确化

## Reviewer Divergence

**DPI 论证严重性**：R1 列为 critical（缺 sketch-level 推导），R2 REBUT 降为 should-fix（论文用 "motivates" 而非 "proves"，核心贡献不依赖此理论论证）。最终采纳 R2 论证，记录为 should-fix。

**arXiv n=2,200 充足性**：R2 认为不足（< power curve 推荐 n≥2,500），R1 REBUT（power curve 针对不同 boundary pair，直接套用不恰当）。共识：sample size 本身不构成问题，但 cross-scorer CI 仅 2/4 confirmed 是真实限制。

**"First empirical measurement" 措辞**：R2 建议改为 "First systematic empirical characterization"，R1 REBUT（K* 是本文定义的概念，"first measurement" 在定义上准确）。最终：无需修改。

---

## Questions

1. 是否可以在 held-out model family（如仅用 Pythia+OLMo 的 AUC gap）上独立验证 θ=0.60，再应用于 Qwen/LLaMA/Mistral 检验？
2. retrain-chain 实验能否扩展到 Qwen-1.5B 或 OLMo-1B，验证 K*≥4 的跨模型一致性？
3. 若将 θ 作为连续参数报告 K*(θ) curve（已有 Figure 3），是否可以将该 curve 作为核心结果取代固定 K*=2 claim？
4. Pythia filtering replication 中 MMLU baseline 0.2568 接近随机，该实验的 strategy ordering 是否在统计上可靠？

---

## Missing References

1. **Cao et al. (2020)** — CORAL: deep ordinal regression with consistent rank ordering（OBD 的 neural alternative，completeness 需引用）
2. **Ke et al. (2017)** — LightGBM 原始论文（核心分类器未引用原始文献）
3. **DivEye (Basani & Chen, 2026)** — 已引用但 Related Work 未详细讨论与 15D 特征集的重叠（surprisal moments, diversity metrics 高度相关）
4. **多步 paraphrasing 检测文献** — 与 prompt-chain rewrite mode 直接相关
5. **Oren et al. (2024)** — contamination detection framework

---

## External Review (Stanford Agentic Reviewer)

项目未配置外部审稿（external_review.paperreview_ai.enabled 未启用），本轮无外部审稿结果。

---

## Overall Assessment

**评分：3.5 (Borderline Conference)**

**置信度：4/5**（两位 Reviewer 独立给出相同评分，交叉分享后共识度高）

**理由**：

论文提出了一个新颖且定义清晰的研究问题（K* discrimination boundary），实验覆盖面广（9 配置、3 域、4 解码策略）、统计方法严谨、边界案例处理诚实。Domain ordering 的发现有理论价值，cross-model transfer 和 downstream filtering 形成完整的验证链条。

但三个 critical 问题限制了当前版本的可信度：(1) θ=0.60 的 post-hoc 选择缺乏独立验证，headline claim K*=2 的稳健性直接受制于此；(2) prompt-chain 设定与现实 retrain-chain 的巨大差距（K*=2 vs ≥4）削弱了 practical prescription 的推广性；(3) "sole dominant factor" 与 ANOVA 证据和 Mistral 反例不一致。若这三个问题被充分 address（特别是 θ 的独立验证和 prompt-chain 限定），论文有潜力达到 Conference (4.0) 水平。

方法组件均为现有技术（LightGBM、手工特征、OBD），方法创新有限；下游 filtering 效果 modest（~0.8pp），实际影响力受限。但问题定义本身的新颖性和实验的系统性部分弥补了方法创新不足。

---

## Detailed Comments

### Section 1 (Introduction)
- L10 长列表句式难解析，建议拆分
- Contribution (c) "80-92% accuracy retention" 应标注仅基于 4 个模型

### Section 3 (Method)
- Eq. 1 用 point-estimate AUC 定义 K* 但实际用 CI lower bound 判断，定义与实践不一致
- "motivates a finite K*_theory" 处补充 "under mild regularity conditions"
- θ=0.60 段落明确标注 post-hoc 选择

### Section 4 (Experiments)
- Section 4.5 标题 "sole dominant" → "primary"
- Table S2 footnote: Nuc p=0.9 的 2v3 CI upper=0.601 marginally above θ，Discussion 应提及
- Neural probe 补充 n per depth level
- "largely robust to scorer choice" 措辞需修改

### Section 5 (Filtering)
- 正文中显著标注 prompt-chain 限定
- 框定为 consistency check / proof of concept

### Section 6 (Discussion)
- retrain-chain 对比建议提升至正文
- "Domain as sole dominant factor" 相关段落措辞对齐

### Abstract
- AUC 首次出现展开全称
- θ=0.60 简要说明含义
- One-wash 表述精确化

### Writing
- -ing participial trailing phrases ~15 处建议改写
- 补充 LightGBM 和 CORAL 引用