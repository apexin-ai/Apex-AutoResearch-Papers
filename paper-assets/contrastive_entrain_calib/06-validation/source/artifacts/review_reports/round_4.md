---
round: 4
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-22T14:16:38.051493+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 4 审稿报告：Discriminability Without Utility: Why Sycophancy Directions Fail as GRPO Rewards

**目标 Venue**: EMNLP 2026 via ARR May 2026
**审稿模式**: Fresh（重新审稿）
**Reviewer 配置**: 2 人（R1: 方法严谨性 + 实验设计；R2: 新颖性 + 完整性 + 写作质量）
**收敛轮次**: 1 轮（交叉分享后无重大未解决分歧）

---

## Summary

论文提取了一个 contrastive sycophancy direction (d_syc)，在 Qwen3-8B 上达到 AUROC 0.827，在 Llama-3-8B 上达到 0.779，然后测试了三种将 d_syc 转化为训练信号的方法（两种 GRPO reward variant + 一种 SFT-based probe penalty），以及一个纯行为奖励的 GRPO 消融（R₃-only）。所有 d_syc-based 和 GRPO 方法均失败，仅 ACT（dense per-token SFT）成功。论文提出"discriminability ≠ reward utility"的概念框架，认为 d_syc 编码了信念是否改变但未编码信念是否应该改变。

---

## Strengths

**S1.** 研究问题重要且及时——representation engineering 越来越多地被用于 reward design，本文对"discriminability 自动转化为 reward utility"这一隐含假设提出了有价值的质疑。[R1, R2 共识]

**S2.** 系统性 failure mode 分析——6 种配置（F1a-F1d cosine, F2 binary probe, F3 continuous probe）形成诊断链，每种解决前一种的 failure mode 但暴露更深层问题。这是负面结果论文应有的严谨性。[R1, R2 共识]

**S3.** Probe reward trap (C2) 是有原创性和实践价值的发现——behavioral death (ToF=0 at step 500) 先于 distributional collapse (entropy drop at step ~1840) 1,300 步的观察表明 entropy-based early stopping 不足以检测此类 reward hacking。关键：此发现在 SFT 设定下取得，独立于 GRPO 超参数 confound。[R1, R2 共识]

**S4.** Cross-model validation 增强了 d_syc 方向本身质量的可信度——Qwen3-8B (AUROC 0.827) 和 Llama-3-8B (AUROC 0.779) 上的一致 evidence-strength gradient 确认方向是可复现的。[R1, R2 共识]

**S5.** Limitations 诚实全面——论文坦承了 group_size=2、truncation、2 seeds、incomplete ACT seed 2、无人类 IAA 等所有主要局限。[R1, R2 共识]

**S6.** 写作清晰，结构逻辑通顺，从 direction extraction → reward formulation → failure catalog → mechanistic analysis 的叙事线索完整。格式合规（8 页正文，匿名，ACL style）。[R2 确认，R1 无异议]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [critical] GRPO group_size=2 构成致命 confound，C1 的因果归因不成立** [R1-N1, R2-N1; 双方 AGREE]
- Group size=2 远低于典型范围 8-64 (Shao et al., 2024)，导致 advantage estimation 极度噪声化。
- 关键证据：R₃-only GRPO（完全不使用 d_syc 的纯行为奖励）同样基本失败（仅 4/27 checkpoints 超过 vanilla，SyconScore 0.143 vs vanilla 0.134）。这强烈暗示问题出在 GRPO 在 group_size=2 下的不稳定性，而非 d_syc 的根本缺陷。
- 标题声称 "Why Sycophancy Directions Fail as GRPO Rewards"，但如果 group_size=8/16 后 d_syc 能成功，该结论完全翻转。
- **C2 (probe trap) 不受此 confound 影响**（SFT 设定），但 C1 的所有 GRPO 失败（F1a-F1d, F3, R₃-only）都可能被此 confound 解释。
- 建议：至少在一个 formulation 上测试 group_size=8/16；或将 C1 降级为条件性结论。

**MF2. [critical] 标题和 framing 过度泛化，与证据范围不匹配** [R1-W2, R2-N2; 双方 AGREE]
- 标题 "Discriminability Without Utility" 暗示一般性原则，但证据仅来自：一种行为属性（sycophancy）、一种 RL 算法（GRPO, group_size=2）、一种主要模型（Qwen3-8B）。
- Wu & Tang (2026) 在论文自身引用中展示 representation-level directions 在 GRPO reward hacking detection 中以 100% accuracy 成功——直接与标题的一般性声明矛盾。
- §6 标题 "Discriminability ≠ Reward Utility" 作为一般性原则呈现，但论文仅提供 single case study 的描述性证据。"Why ... Fail" 暗示因果解释，实际上是 observational/post-hoc 分析。
- 建议：(1) 标题进一步限定（如加 "A Case Study"）；(2) Abstract 中明确实验范围限制；(3) §6 标题改为条件性表述。

**MF3. [critical] 80-84% truncation rate 可能系统性扭曲奖励信号** [R1-N2; R2 AGREE with nuance]
- d_syc 从完整 3-turn 对话中提取，但 GRPO 训练中 rollout 在 256 token 处截断（80-84% truncation）。
- 论文声称 "response-level decisions typically manifest within the first 100-200 tokens" 但无任何实证支持。
- Cosine gap 仅 0.098（§4），truncation 引入的噪声可能完全淹没信号。论文将 gap 过窄归因于 d_syc 的 "semantic limitation"，但同样可能是 truncation 导致。
- R2 补充：truncation confound 主要影响 C1（GRPO failures），对 C2（probe trap at step 500, 模型尚未大幅偏离初始分布）影响较小。
- 建议：提供 truncation vs non-truncation 的 AUROC/cosine gap 对比。

**MF4. [critical] 仅 2 random seeds 不足以支撑负面结论** [R1-N3, R2-W3; 双方 AGREE]
- 负面结论需要比正面结论更高的统计门槛——读者需要排除 "实验做得不够好" 这一竞争假说。
- 两个 seed 之间差异不小：crash onset 差 ~2,500 步（seed 1 at checkpoint 6000 vs seed 2 at checkpoint 4000），在 8,000 步训练中占 31%。
- 2 seeds 无法区分 "d_syc 本质上不能工作" 和 "这两个特定 seed 恰好失败"。
- 建议：增加到至少 5 seeds，报告 mean ± std。

**MF5. [critical] 缺乏标准 RM-based GRPO 对照基线** [R2-N3; R1 AGREE]
- 缺少关键对照：标准 reward model（如 trained classifier 或 LLM-as-judge）的 GRPO 在同一 sycophancy calibration task 上的表现。
- 无此对照，无法区分三种竞争假说：(a) d_syc 本质上不适合做 reward；(b) GRPO group_size=2 下任何 reward 都不工作；(c) sycophancy calibration 本身不适合 scalar per-completion RL。
- R₃-only GRPO 的失败（NLI behavioral reward）部分扮演了此角色，但其同样失败恰恰暗示问题在 (b) 而非 (a)——这实际上削弱而非支持论文论点。
- 建议：添加一个 LLM-judge-based GRPO baseline。

### Should-Fix（影响评分但不一票否决）

**SF1. [warning] ACT vs GRPO 对比被 5+ 维度差异严重 confound** [R1-W1; R2 AGREE]
- ACT 与 GRPO 至少在 5 个维度上不同：supervision granularity, loss family, training data format, optimization dynamics, LoRA capacity (~1.75x 参数量)。
- 论文标记为 "observational" 但 Table 4 将 ACT 与 GRPO variants 并列展示，暗示可比性。
- 建议：Table 4 中为 ACT 行加 separator 或 "reference only, not directly comparable" 标注。

**SF2. [warning] Wu & Tang (2026) 的 geometric separability 论证缺乏定量验证** [R2-W1; R1 AGREE]
- §6 将 "geometric separability" 作为核心解释机制（为什么 Wu & Tang 成功而本文失败），但未提供任何定量指标。
- AUROC 0.827 已显示不错的可分性——为什么这不够？需要量化比较（如 cluster separation, inter/intra-class variance, cosine 分布重叠度）。
- 建议：定量比较 d_syc 与 Wu & Tang direction 的 geometric properties，或承认对比的不完整性。

**SF3. [warning] ACT seed 2 仅 4/16 checkpoints 完成评估** [R1-W4; R2 AGREE]
- 25% 评估完成度不构成可靠证据，且可能存在 selection bias。
- 论文多次引用 "seed 2: 4/4 ongoing" 作为 ACT 成功的支撑。
- 建议：完成全部评估后投稿；或将 seed 2 行标记为 preliminary data，不纳入正式结论。

**SF4. [warning] Cross-seed rank correlation ρ≈0.33 统计报告不充分** [R1-W5; R2 AGREE]
- 未报告 N（参与排序的 checkpoint 数量）、window 划分方式、p-value 和 CI。
- 如果 N<10，ρ=1.0 和 ρ=0.33 都无统计意义。
- 建议：报告 exact N、p-value、CI；如果 N 过小承认统计功效不足。

**SF5. [warning] R₃-only GRPO 在 Table 4 中缺少 ToF 和 NoF 分项数据** [R1-W6; R2 AGREE]
- §6 声称 R₃-only 表现出 "same stubbornness pattern (high NoF, near-zero ToF)" 但 Table 4 中 ToF/NoF 列为空（"--"）。
- 声称 pattern 相似但不提供数据不充分。
- 建议：填充 R₃-only GRPO 的 ToF 和 NoF 值。

**SF6. [warning] SyconScore harmonic mean 的选择 justification 不足** [R1 minor #2]
- Harmonic mean 当 ToF=0 时自动归零，可能掩盖 NoF 维度的改善。
- §2.5 仅一句话提及 F₁ score 类比，未充分论证。
- 建议：扩展 justification，解释惩罚单侧极端的意图。

---

## Reviewer Consensus

以下问题两位 Reviewer 在交叉分享中达成完全共识：

| 问题 | 状态 |
|------|------|
| Group size=2 致命 confound (MF1) | [AGREE] 双方一致，R1 补充 R₃-only 也失败的证据 |
| 标题/framing 过度泛化 (MF2) | [AGREE] 双方一致 |
| 80-84% truncation confound (MF3) | [AGREE] R2 补充对 C2 影响较小的 nuance |
| 2 seeds 不足 (MF4) | [AGREE] 双方一致 |
| 缺少 RM baseline (MF5) | [AGREE] R1 补充三种竞争假说分析 |
| ACT vs GRPO confound (SF1) | [AGREE] 双方一致 |
| Wu & Tang 定量验证缺失 (SF2) | [AGREE] 双方一致 |
| ACT seed 2 incomplete (SF3) | [AGREE] 双方一致 |
| Cross-seed correlation stats (SF4) | [AGREE] 双方一致 |
| R₃-only 缺分项数据 (SF5) | [AGREE] 双方一致 |

## Reviewer Divergence

以下问题存在分歧但不影响整体判断：

| 问题 | R1 | R2 | 结论 |
|------|-----|-----|------|
| DPO/KTO 实验 | REBUT: 超出合理 scope | W4: 应至少测试一种 | 不纳入 Should-Fix；论文已在 §6 列为 open question |
| PRM 讨论 | REBUT: 概念已覆盖 | W5: 应扩展 | 不纳入 Should-Fix；§6 Future directions 已涵盖 per-step reward 概念 |
| Evidence strength IAA | W3: Should-Fix | REBUT: 降级为 minor | 保留为 Should-Fix 但降低优先级；evidence gradient 非核心 claim |
| CRAFT/Latent-GRPO 讨论深度 | REBUT: §6 有实质讨论 | W2: 过于简略 | 不纳入 Should-Fix；§6 geometric separability 框架已涵盖 |

---

## Questions

1. R₃-only GRPO 也基本失败（4/27 checkpoints > vanilla）——作者如何解释"即使不使用 d_syc 的标准行为奖励在相同 GRPO 配置下也不工作"这一事实？这是否暗示问题在 GRPO 配置而非 d_syc？
2. "Response-level decisions typically manifest within the first 100-200 tokens"（Appendix A）的依据是什么？是否有 token-level 分析支持？
3. Stubbornness taxonomy (Appendix B) 中 sycophantic stubbornness (24%) + deliberation traps (29%) = 53%，evidence-graded hedging 的百分比是多少？三种类别是否互斥？
4. Abstract 和 Table 4 footnote 显示 "4 of 26" checkpoints，Introduction 和 §6 显示 "4 of 27"——正确数字是多少？
5. Cross-seed rank correlation ρ≈0.33 是在多少个 checkpoint pairs (N) 上计算的？划分 "early" 和 "late" 窗口的标准是什么？

---

## Missing References

以下参考文献可能与论文主题相关，建议考虑：
- Perez et al. (2022) "Discovering Language Model Behaviors with Model-Written Evaluations" — 早期 sycophancy 量化方法，与本文 evaluation framework 有关
- Rafailov et al. (2023) DPO — 已引用但讨论不足，作为 GRPO 之外的 preference-based 替代方案应更深入讨论

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 external_review）。

---

## Visual Layout Check（非评分项）

视觉审查状态：**done**（耗时 ~3.5 分钟）

| 严重级别 | 数量 |
|----------|------|
| Critical | 0 |
| Warning | 2 |
| Info | 8 |

**Warnings:**
1. **Page 1-3 连续纯文本无 display item** — 审稿人前 3 页只看到密集文字，无法快速锚定核心贡献。建议在 page 2-3 插入概念图或将 Figure 1 前移。
2. **Page 11 底部约 45% 空白** — Appendix B 内容较少，可考虑合并或调整 float 位置。

**Info highlights:**
- Table 4 (page 6) 中 ACT seed 2 "ongoing; 4/16 ckpts ev..." 字样对审稿人观感不佳
- Figure 3 建议确认灰度打印时两条 seed 线可区分（加不同 marker shape）
- 公式渲染正确，无 LaTeX 残留错误，无未解析引用

---

## Overall Assessment

**评分：3.0 / 5 — Findings（可被 Findings 接收）**

**置信度：4/5（两位 Reviewer 均表示高置信度）**

### 评分理由

**核心判断**：论文的研究问题重要、实验设计系统、probe reward trap (C2) 有原创价值。但五个 critical 问题共同构成了对论文核心论点的严重质疑：

1. **GRPO group_size=2 confound**（MF1）+ **R₃-only 也失败**（MF5 的证据）共同暗示问题可能在 GRPO 配置而非 d_syc。这是最致命的问题——如果 group_size=8 后 d_syc 能成功，论文核心 thesis 完全翻转。
2. **标题/framing overclaim**（MF2）在 Wu & Tang (2026) 的成功案例面前尤为突出。
3. **Truncation**（MF3）和 **2 seeds**（MF4）进一步削弱因果推断的可靠性。
4. **缺少标准 RM baseline**（MF5）使三种竞争假说无法区分。

**C2 (probe reward trap) 是论文最稳健的贡献**，因为它在 SFT 设定下独立于所有 GRPO 超参数 confound。如果论文以 C2 为核心贡献重新 frame，C1 降级为条件性观察，论文的可接收性会显著提高。

**当前状态适合 Findings**——有价值的负面发现和实践警示（特别是 C2 的 entropy monitoring 盲区），但实验范围和因果推断不足以支撑 Conference 级别的结论。

### 提升到 Conference (4.0) 的路径

1. **[必须]** 在 group_size=8/16 下复现至少一个 formulation——确认失败是否 robust
2. **[必须]** 增加到 ≥5 seeds 并报告 mean ± std
3. **[强烈建议]** 添加标准 RM baseline，区分 d_syc 缺陷 vs GRPO 配置缺陷
4. **[强烈建议]** 提供 truncation vs non-truncation 的 cosine gap 分析
5. **[建议]** 标题进一步限定；完成 ACT seed 2 评估

---

## Detailed Comments

### §1 Introduction
- 第二段 "only 4 of 27 checkpoints" 与 Abstract "4 of 26" 不一致——需统一。
- Contributions 从 3 个精简到 2 个（C1, C2）是正确的决定，但 C1 表述 "Every tested GRPO formulation fails" 在 group_size=2 的条件下过于绝对。建议改为 "Under our GRPO configuration (group size=2), every tested formulation fails"。

### §2 Experimental Framework
- §2.5: GRPO group size=2 的 disclosure 诚实但应更突出——当前仅在一个括号中提及，建议提升为独立句。
- §2.5: SyconScore harmonic mean 的 justification 仅一句话，应扩展（引用 F₁ 类比，解释 ToF=0 时归零的意图）。
- Table 5 footnote d "Below typical 8-16; not tuned" 应更正为 "Below typical 8-64" (Shao et al., 2024 原文)。

### §3 Direction Discriminability
- 分析扎实，cross-model validation 是加分项。Bootstrap CI 的使用正确。
- Evidence-strength gradient 分析有趣但依赖 GPT-4.1 单一标注者（无 IAA）——在当前论文中不影响核心结论，但建议在 Limitations 中更显式承认。

### §4 Cosine R₁: Structural Failure
- 诊断链结构清晰（F1a→F1b→F1c→F1d 每步解决一个问题暴露一个更深问题）。
- Cosine gap 0.098 的归因——"semantic limitation" vs truncation artifact——在未做 non-truncation 对比前无法区分。

### §5 The Probe Reward Trap
- 本文最稳健的贡献。1,300-step lag 的观察有实践价值。
- 独立于 GRPO 超参数（SFT 设定），不受 group_size confound 影响。
- Stubbornness taxonomy (Appendix B) 百分比不完整——24% + 29% = 53%，剩余类别未报告。

### §6 Analysis: Discriminability ≠ Reward Utility
- §6 标题作为一般性原则呈现过于强势，建议改为条件性表述。
- R₃-only GRPO 分析：Table 4 中 ToF/NoF 为空但文字声称 "same stubbornness pattern"——数据缺失。
- Cross-seed rank correlation ρ≈0.33 统计报告不充分（缺 N, p-value, CI）。
- ACT comparison 标记为 "observational" 是好的，但 Table 4 并列呈现暗示可比性——建议加 separator。

### §7 Related Work
- Papadatos & Freedman (2024) 的讨论是论文优势——inference-time vs training-time 对比精到。
- CRAFT/Latent-GRPO 讨论可适度扩展，但非必须。
- SMART per-step reward 在 §6 Future directions 中已概念性涵盖，但可考虑加 PRM 术语提升可检索性。

### §8 Conclusion
- "Our results suggest" 的措辞较 cautious，是好的。
- 但标题和 §6 标题与 §8 的谨慎措辞不一致——应统一。

### Limitations
- 诚实覆盖了 group_size=2、truncation、2 seeds、ACT seed 2 incomplete 等主要问题。
- Group size disclosure 应更突出其对 C1 因果推断的影响。

### Appendix
- Table 5 超参数详尽，可复现性好。
- Stubbornness taxonomy 百分比需补完。