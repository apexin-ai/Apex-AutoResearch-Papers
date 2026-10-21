---
round: 38
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-22T13:00:50.996806+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 38

**论文**: When Does Test-Time Scaling Fail? Boundary Conditions for Named Entity Recognition
**Venue**: EMNLP 2026 Long Paper (ARR May cycle)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计；R2: 新颖性+完整性+写作）
**圆桌轮次**: 1 轮（Round 1 后交叉分享，关键问题已收敛）

---

## Summary

本文研究 test-time compute scaling（self-consistency / best-of-N）在 NER 上的失败条件。在 4 个 NER 数据集（SciERC、CoNLL-2003、Few-NERD、WNUT-17）上使用 Qwen3-8B 和 LLaMA-3.1-8B 进行实验，发现质量估计信号能预测输出质量（AUROC 最高 0.82），但 instance-level selection gain <1pp（即使 N=64），定义为 "correlation-selection gap"。提出 diagnostic framework 识别两个 co-occurring 失败条件：high output degeneracy（12–68%）和 signal alignment collapse（α→0）。Exploratory entity-level construction 在 Few-NERD 上获得 +1.40pp 提升（per-family Holm p=0.006; global Holm p=0.055）。扩展到 RE 和 SQL parsing 作为 exploratory pilot。

---

## Strengths

**S1. 研究问题的 timeliness 和重要性。** TTS 在 reasoning 上的成功已被广泛验证，但在结构化输出任务上的 failure mode 缺乏系统研究。论文填补了真实的知识 gap。[R1 Excitement 4/5, R2 Excitement 3/5]

**S2. 实验体量与统计严谨性出色。** 44 页论文（含 35 页 Appendix），4 NER 数据集 × 2 模型族 × 多种信号/选择策略全排列。统计方法覆盖 bootstrap 95% CI、Holm-Bonferroni 全局校正（k=57 全部 57 个检验枚举于 Table 12）、TOST 等价性检验、permutation test、split-half reliability。这在 NLP 实证研究中属上乘水准。[R1, R2 共识]

**S3. Correlation-selection gap 是 genuine 且 well-documented 的新发现。** AUROC up to 0.82 但 selection gain <1pp 的 disconnect 在 4 个 NER 数据集 + 2 个模型上一致复现（Table 1, Table 3, Table 4），非 cherry-picked 结果。[R1, R2 共识]

**S4. Negative results 的诚实报告。** Cross-dataset transfer 为负（§5.2）、entity construction 在 CoNLL 无增益、Holm 全局校正后 p=0.055、69% inverse scaling 等均如实报告。这种透明度值得肯定。[R1, R2 共识]

**S5. MBR 理论连接有深度。** Appendix 将 entity construction 形式化为 MBR decoding 特例（Proposition 2），balanced set-overlap utility 下最优解刻画为理论发现提供了 formal grounding。[R2 highlighted]

**S6. 多层次分析框架。** 从 population-level (QE → AUROC) → instance-level (ranking → selection) → entity-level (construction) 三个粒度递进分析，Discover → Diagnose → Explore bypasses 叙事结构有效。[R2 highlighted]

---

## Weaknesses

### Must-Fix（4 项，两位 Reviewer 均达成共识）

**MF1. [CRITICAL] Title "Boundary Conditions" 与实际交付 "diagnostic correlations" 之间存在 claim-evidence mismatch。** [R1 AGREE, R2 AGREE]

"Boundary conditions" 在数学和科学中暗示 necessary/sufficient conditions。论文自身在 §6.3 和 §9 中反复使用 "diagnostic rather than predictive" 限定 framework 性质，与标题矛盾。Corollary 1 给出的 degeneracy threshold 精度极低（bound 仅 capture 3–12% actual gains），进一步削弱 "boundary" 的含义。

→ **建议**：改为 "Failure Modes" (R1 建议) 或 "Diagnostic Conditions" (R2 建议)。两位 Reviewer 对替代措辞有分歧但对核心判断完全一致。

**MF2. [CRITICAL] Degeneracy decomposition bound $(1-D) \cdot G_{\text{nd}} \cdot \alpha$ 仅 capture 3–12% actual gains，削弱 framework 的定量诊断价值。** [R1 raised, R2 AGREE]

Bound off by an order of magnitude（Figure 10）。Abstract 声称 "guides practitioners on what to measure" 但一个 10× loose 的 bound 无法提供 quantitative guidance。R2 补充：looseness 主要源于 entity independence 假设（split-half r=0.578–0.644 显示 entity 间有 correlation structure）。

→ **建议**：(a) 正文显式讨论 looseness 来源（entity independence 假设 vs α 保守性），量化各因素贡献；(b) 将 bound 定位为 "illustrative upper bound" 而非 "diagnostic tool"；(c) 降低 Abstract/§9 的实践指导 claim。

**MF3. [CRITICAL] Entity construction 69% inverse scaling (40/58 transitions)，"bypass" framing 严重过度。** [R1 raised, R2 AGREE]

§6.2 报告 "Increasing N decreases construction F1 in 40 of 58 transitions"。LP-weighted construction 仅 Few-NERD 上 consistently positive (+1.40pp)，SciERC non-significant (+0.32pp)，CoNLL negative (−0.39pp)。Abstract/§1/§5/§9 多处 "partially bypasses the bottleneck" 与 69% failure 率直接矛盾。论文同时报告两个相互矛盾的 narrative——§5 将 entity construction 作为 bypass solution，§6.2 则报告 69% inverse scaling——读者需自行拼凑。

→ **建议**：将 entity construction 明确定位为 "conditional bypass: works only under low-degeneracy + LP-F1 alignment"；Abstract/Introduction 调低 claim；主文直面 inverse scaling 矛盾。

**MF4. [CRITICAL] 核心 positive result (Few-NERD LP selection) 在 global Holm-Bonferroni (k=57) 下 p_adj=0.055，跨越显著性边界。** [R1 raised, R2 AGREE; 跨轮复发——R34 首次提出]

Per-family Holm (k=10): p_adj=0.006 → significant；Global Holm (k=57): p_adj=0.055 → non-significant。§7.5 先报告显著后报告不显著的呈现顺序有 framing bias（R2 指出）。Per-family 划分 "independent mechanisms" 论证不充分——三者共享 sampling pipeline 和 instance population，且未 pre-registered（R1 指出）。Few-NERD 是唯一 LP selection 产生实质性正面 gain 的数据集。

→ **建议**：(a) 以 global correction 为主要报告，per-family 作为 sensitivity analysis；(b) Abstract 附 global p-value caveat；(c) 明确承认 per-family 划分未 pre-registered。

### Should-Fix（10 项）

**SF1. [WARNING] §3 Hidden-state probe 使用 Qwen2.5-7B 而非主实验 Qwen3-8B。** [R1, R2 共识; 跨轮复发——R36 首次提出]

Qwen3 架构（thinking mode、不同 attention）与 Qwen2.5 有显著差异。Probe AUROC 0.63–0.88 能否迁移到 Qwen3-8B 未验证。§9 将 probe 结论作为 general finding 使用是 over-reaching。建议至少在 Qwen3-8B 上做 1 组 key probe 或更显著地限定结论 scope。

**SF2. [WARNING] Few-NERD "positive contrast" 受 3-epoch under-training confound 影响。** [R1 raised, R2 AGREE with nuance; 跨轮复发]

5-epoch model degeneracy 从 ~13% 升至 31%，LP gain 从 +1.39 消失至 +0.12±0.04pp。Few-NERD 在全文被反复用作 positive anchor，但此 anchor 是 confounded 的。§7.5 仅两行讨论，不够 prominent。论文的 defense ("sensitivity reinforces diagnostic value") 逻辑上自洽，但应更突出讨论 ecological validity。

**SF3. [WARNING] 与并发工作 arxiv 2603.12520 (correlation-selection gap in BoN reasoning) 的新颖性区分缺失。** [R2 raised; R1 REBUT——认为结构化输出 degeneracy 机制根本不同; 分歧未完全收敛]

R1 的 rebut 有合理性——NER degeneracy 是 entity-set level collapse，与 reasoning BoN 的评分区分度问题机制不同。但该并发工作仍应被引用并讨论，以明确本文在 structured prediction 维度上的独特贡献。

**SF4. [WARNING] 模型 scale 覆盖不足以支撑 cross-scale generalization claim。** [R1 raised, R2 partial REBUT; 跨轮复发]

主实验 Qwen3-8B + LLaMA-3.1-8B 均为 8B 级别。72B 仅 SciERC 零样本，GPT-5.5 仅 200 instances pilot。R2 认为 "two families" 满足 "multiple families" 但 scale diversity 不足。建议 Limitations 更明确标注 scale 限制。

**SF5. [WARNING] RE (n=397) / SQL (n=196) 证据强度与 abstract/intro 呈现权重不匹配。** [R1, R2 共识; 跨轮复发]

Abstract 将 RE/SQL 与 NER 并列给人等权重印象。SQL pilot n=196 单数据集。建议进一步降格为 "preliminary pilot"。

**SF6. [WARNING] Constrained decoding ablation 仅 2 数据集 (CoNLL + SciERC)，覆盖不足。** [R1, R2 共识]

Constrained decoding 直接影响 output distribution 和 degeneracy 核心机制。Table 33 仅覆盖 SciERC + RE。Few-NERD free-form ablation 缺失。建议补充或讨论代表性。

**SF7. [WARNING] Abstract 数字密度过高。** [R1, R2 共识; 跨轮复发]

Abstract 塞入 AUROC 0.82、<1pp、N=64、12–68%、+1.40pp 等大量数字。建议精简至 3-4 个最关键数字。

**SF8. [WARNING] 术语不一致：degeneracy / output convergence / convergence 交替使用。** [R1, R2 共识; 跨轮复发]

§2 定义 "degeneracy" 后仍有混用，且与 "training convergence" 歧义。建议全文统一。

**SF9. [WARNING] 与 Yao et al. (2026) 的增量新颖性区分在主文中不够 prominent。** [R2 raised, R1 partial AGREE; 跨轮复发]

§1 三层区分存在但对非专家读者不够清晰。Table 66 differentiation matrix 在 Appendix，主文 §8 visibility 不足。

**SF10. [WARNING] Diagnostic framework 实用价值缺乏 cost-benefit analysis。** [R2 raised, R1 REBUT; 分歧存在]

R2 认为需先采样才能诊断，构成循环。R1 反驳：pilot-based 分阶段决策（N=8 诊断 → decide → scale/abort）不构成循环。两方都有道理——建议 §7.5 添加简要 cost analysis（N=8 pilot 成本 vs N=64 全量 scaling 成本）即可化解。

---

## Reviewer Consensus [AGREE]

1. **Title overclaims** — "Boundary Conditions" 暗示 formal necessary/sufficient conditions，但论文交付 diagnostic correlations
2. **统计显著性敏感** — 核心 positive result 在 global correction 下 borderline non-significant (p=0.055)
3. **Entity construction "bypass" 过度 framing** — 69% inverse scaling 与 "partially bypasses" narrative 矛盾
4. **Bound looseness** — $(1-D) \cdot G_{\text{nd}} \cdot \alpha$ 仅 capture 3–12% actual gains
5. **Probe 模型不匹配** — Qwen2.5-7B probe 结论不能无条件迁移至 Qwen3-8B
6. **RE/SQL 证据薄弱** — n=397/n=196 不足以支撑 abstract 级别呈现
7. **Abstract 数字过密 + 术语不一致** — 写作质量可改善

## Reviewer Divergence [REBUT]

1. **并发工作 novelty** (R38-SF3) — R2 认为 arxiv 2603.12520 发现了本质相同的 correlation-selection gap；R1 REBUT 认为结构化输出的 degeneracy 机制（entity-set collapse）与 BoN reasoning（评分区分度）根本不同。**Director 判断**：R1 的 rebut 合理，但该工作仍应被引用讨论。降为 Should-Fix。
2. **Diagnostic circularity** (R38-SF10) — R2 认为需先采样才能诊断构成循环；R1 REBUT 认为 pilot-based 分阶段决策合理。**Director 判断**：R1 rebut 有效，但论文应添加 cost-benefit 数字以增强说服力。降为 Should-Fix。
3. **模型 scale 多样性** (R38-SF4) — R1 认为不足以支撑 "multiple families" claim；R2 partial REBUT 认为 two architecture families 已满足但 scale 不足。**Director 判断**：claim 范围应限定为 "7–14B open-weight"，scale generalization 在 Limitations 中明确标注。

---

## Questions for Authors

**Q1** (from R1): Degeneracy bound looseness 主要来自 entity independence 假设还是 α 保守估计？能否量化各因素贡献？

**Q2** (from R1): 如果 global Holm p=0.055 下 Few-NERD LP selection 不 significant，论文核心叙事如何调整？

**Q3** (from R1): Entity construction inverse scaling 69% 的情况下，practitioners 在什么具体条件下应使用 entity construction？degeneracy <20% 且 LP-F1 ρ >0.2 是充分条件吗？

**Q4** (from R1, R2): 是否尝试过 Qwen3-8B hidden states（去掉 thinking tokens）训练 probe？

**Q5** (from R1): Few-NERD 5-epoch degeneracy 升至 31% 后 LP gain 消失——LP selection 是否仅在模型 under-converged 时有效？

**Q6** (from R2): Title 为什么用 "Boundary Conditions" 而非 "Failure Modes" 或 "Diagnostic Conditions"？

**Q7** (from R2): arxiv 2603.12520 在 BoN 设置下发现了几乎相同的 correlation-selection gap 现象——如何界定本文的独立贡献？

---

## Missing References

**必须添加**:
1. "When LLM Judge Scores Look Good but Best-of-N Decisions Fail" (arxiv 2603.12520, March 2026) — 并发工作，correlation-selection gap in BoN reasoning [R2 raised, R1 认为应引用但机制不同]

**推荐添加**:
2. "Conformal Structured Prediction" (Angelopoulos et al., ICLR 2025) — 结构化输出 conformal prediction [R2]
3. "Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission" (He et al., NAACL Findings 2024) — token-level uncertainty for NER [R2]
4. "Conformal Prediction for Natural Language Processing: A Survey" (TACL 2024/2025) [R2]
5. "LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty" (WWW 2024) [R2]
6. Malinin and Gales (2021) "Uncertainty Estimation in Autoregressive Structured Prediction" [R1]

---

## External Review (Stanford Agentic Reviewer)

未启用。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时约 5 分钟）。0 critical / 0 warning / 8 info。

主要发现：
- 首页无 display item（Figure 1 在第 2 页顶部），ACL 格式下正常
- Page 7 视觉密度极高（单页 3 个 display items：Table 3 + Table 4 + Figure 4）
- Page 8（最后一页正文）纯文本，无 display item
- Table 2 部分缩写列字号偏小，快速扫描可读性一般
- Appendix 中 Table 12（57 行）和 Tables 13–22 字号接近可读性下限，appendix 标准可接受

无排版硬伤，不影响评分。

---

## Overall Assessment

**评分: 3.0 — Findings**
**置信度: 4/5**

**评分依据**:

两位 Reviewer 独立给出 3.5 (Borderline Conference)，但交叉分享后多个 Must-Fix 问题得到强化确认，综合考虑后下调至 3.0：

1. **核心 negative finding 有价值但 framing 系统性过度**：correlation-selection gap 本身是 genuine 且 well-documented 的发现（S3），但论文在 title（"Boundary Conditions"）、theoretical contribution（bound 仅 capture 3-12%）、prescriptive contribution（entity construction 69% inverse scaling）三个维度上均存在 claim-evidence mismatch。这不是单点问题，而是全文 framing 与实际证据强度之间的系统性 gap。

2. **唯一的 positive contrast 统计上脆弱且 confounded**：Few-NERD LP selection 是论文叙事的核心 anchor，但 (a) 在 global correction 下 borderline non-significant (p=0.055)，(b) 受 3-epoch under-training confound 影响（5-epoch 下 LP gain 消失），(c) entity construction 的 Few-NERD gain 也在多数 N-scaling 配置上 inverse scaling。

3. **跨轮复发问题未彻底解决**：multiple testing sensitivity（首次 R34）、probe 模型不匹配（首次 R36）、Yao et al. 区分（首次 R35）、abstract 密度（首次 R37）等问题在本轮再次被独立发现。

**Conference vs Findings 判断**：论文的实验 thoroughness（S2）和问题重要性（S1）使其具备 Findings 水平。但 4 个 Must-Fix 问题（title overclaim、bound looseness、bypass over-framing、statistical sensitivity）均涉及 contribution narrative 的根基，在这些问题解决之前，论文的 contribution 定位不够清晰——读者难以判断应该 take away 什么。如果 re-framing 为 "comprehensive negative result + conditional positive finding" 并调低 prescriptive claims，论文可达 Conference 水平。当前版本定为 Findings。

---

## Detailed Comments

### §1 Introduction
- "correlation-selection gap" 的定义清晰有效，但 "partially bypasses the bottleneck" (+1.40pp) 需要附 global Holm p=0.055 caveat
- 三阶段 (Discover → Diagnose → Explore bypasses) 结构好，但第三阶段的 delivery 不足以支撑 "bypass" 的含义

### §2 Diagnostic Framework
- Per-sample vs instance-level signal 的区分（§2.1）是重要的方法论贡献
- Instance degeneracy 的定义（§2.3）清晰，但后续使用中术语不一致

### §3 How Self-Verification Fails
- ESJ/MRSC/LSC 的 negative results 有诊断价值
- **核心问题**：全部基于 Qwen2.5-7B，§9 将其作为 general conclusion 使用是 over-reaching
- Introspection boundary 概念有趣，但 LODO transfer drops (0.56–0.67) 已削弱其通用性

### §4 Where Single-Signal Selection Fails
- Table 3 的 correlation-selection gap 呈现清晰有效
- "Definitional vs empirical" 两层分解是论文的亮点

### §5 Adaptive Methods
- Table 2 的 9 类方法汇总有参考价值
- Cross-model self-consistency (+0.42pp) 是唯一 unconditional positive result，值得更多讨论

### §6 Threshold Regime Analysis
- MBR 连接（§6.1）理论上优雅
- **核心问题**：§6.2 inverse scaling 69% 与 §5 的 bypass narrative 矛盾
- §6.3 bound looseness 需要正文级别的讨论

### §7 Experiments
- 实验设计 thorough，4 数据集覆盖 difficulty gradient
- Few-NERD epoch confound 需更 prominent 讨论
- Robustness analysis (§7.4) 展示了 signal ranking 的稳定性，是 strength

### §8 Related Work
- 与 Yao et al. 和 Yun et al. 的区分存在但 visibility 不足
- 缺少 arxiv 2603.12520 的讨论
- Conformal prediction 覆盖不够（仅引用 gentle introduction，未讨论 structured prediction 最新进展）

### §9 Discussion/Conclusion
- "Diagnostic rather than predictive" 定位合适，但与 title "Boundary Conditions" 矛盾
- Practical implications 段落缺 cost-benefit analysis
- 作为论文的 conclusion，对 open questions 和 generalizability 的讨论可以更深入
