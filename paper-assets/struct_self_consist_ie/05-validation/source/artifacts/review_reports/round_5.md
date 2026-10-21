---
round: 5
overall_score: borderline
timestamp: 2026-05-15T08:08:03.142382+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 5

**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
**Venue**: EMNLP 2026 Findings (via ARR May 2026 cycle)
**Deadline**: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计 + 统计有效性; R2: 新颖性 + framing + related work + 写作质量）
**轮次**: Round 1（独立审稿 → 交叉分享 → 收敛，1 轮完成）

---

## Summary

论文系统比较了 5 种置信度信号（structural: entity voting, Soft Jaccard; surface: exact match, Fleiss' κ; model-internal: log-probability）在生成式 IE（NER + RE）中用于 quality estimation 和 sample selection 的能力。核心发现是 "correlation-selection gap"——信号能预测哪些实例模型处理可靠（ρ 最高 0.38, AUROC 最高 0.75），但无法在 N 个候选中选出最佳输出（p>0.39）。附带发现：信号排名随 task difficulty 变化（easy task EM 领先, hard task structural signals 领先），以及 WNUT-17 上的 capability boundary（conditional ρ 趋近零）。

---

## Strengths

1. **统计分析严谨性在 ACL 投稿中属上乘**。Bootstrap CI (B=10,000)、TOST 等价检验（多级 δ）、sign test、Cohen's d、multi-seed stability (σ≤0.025)、conditional filtering、diversity stratification——远超同类 empirical papers。[两位 Reviewer 一致肯定]

2. **Negative result 有实际价值**。Log-probability 作为唯一 per-sample signal 也无法有效 select（p=0.39, 13-18 pp oracle headroom），且原因可追溯到 constrained decoding 下的 score compression（60% instance 内 range <0.05, Appendix F）。这对 test-time scaling 文献是重要补充。[R1 Soundness 3, R2 Soundness 3.5]

3. **Problem formulation 清晰**。Per-sample vs instance-level 信号的分类框架简洁有力；quality estimation vs sample selection 的解耦是概念上的贡献。[两位 Reviewer 一致]

4. **实验设计公平**。两模型相同 LoRA 配置（Appendix E Table 8），三数据集覆盖 difficulty gradient（CoNLL easy → SciERC hard → WNUT-17 boundary），训练细节、prompt template 完整（Reproducibility 4/5）。[两位 Reviewer 一致]

5. **引用完整**。58 条引用，核心相关工作（Nédellec et al. 2026, Wang et al. 2023, Kuhn et al. 2023, Eikema & Aziz 2022, Xiong et al. 2024）均已覆盖。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[CONSENSUS] W-C1: Constrained decoding 作为核心混淆变量未被隔离，claim scope 与 evidence 不匹配**
- 来源: R1-N1 + R1-N2 + R2-N1 (constrained decoding 部分)
- 两位 Reviewer 独立提出，交叉分享后完全共识
- 核心问题: 所有实验均使用 constrained decoding (vLLM + XGrammar)。论文无法区分 correlation-selection gap 是 structured IE 的固有属性还是 constrained decoding 的 artifact。论文自身的 Appendix F 提供了反面证据：在 logprob non-tied subset (n=210, 40%) 中，logprob selection 显著优于 greedy (+2.9 pp, p=0.01, within-instance ρ 从 0.08 升到 0.39)——暗示 gap 主因是 constrained decoding 造成的 score compression，而非 IE 本身的固有性质
- 当前论文的 title、abstract、conclusion 将 gap 呈现为 structured IE 的通用属性，未限定 constrained decoding setting
- 修改建议: (a) Title/Abstract/Conclusion 限定 claim scope 为 constrained decoding setting; (b) 提升 Appendix F non-tied analysis 至主文 Discussion; (c) 明确承认 non-tied evidence 对 claim 普适性的影响; (d) 如条件允许添加 free-form decoding 消融更佳（但非强制）

**[CONSENSUS with nuance] W-C2: Correlation-selection gap 的 tautological 成分削弱核心贡献新颖性**
- 来源: R2-N1 (tautological) + R1 交叉回应
- R2 认为 gap 被 "两头夹击"（4/5 instance-level failure = tautological; logprob failure = artifact），整体 contribution 空心化
- R1 部分 rebut：consensus-proximity/MBR failure 是 non-trivial empirical finding（MBR 在 MT 成功但 IE 失败并非 a priori obvious）；论文已有两层论证结构（Discussion §5）
- **共识**: Gap 不完全 tautological，但 Contribution 2 应以 logprob score compression + MBR/consensus-proximity empirical failure 为重心，而非 "5 signals all fail" 的统一叙事。Abstract 和 Introduction 需 reframe
- 修改建议: (a) Reframe C2 聚焦 logprob 和 MBR failure; (b) 弱化 "5 signals all fail" 叙事; (c) Introduction 加强非显然性论证

### Should-Fix（影响评分但不一票否决）

**[CONSENSUS] W-S1: RE "preliminary" 标注与实际使用不一致**
- 来源: R1-W1 + R2-W2
- Abstract 标注 "(SciERC, preliminary)"，但 Table 1/2, Figure 2-3, Discussion 大量使用 RE 结果无限定词。Contribution #3 将 RE 结论嵌入通用表述
- 修改建议: 全文一致标注 RE 为 single-benchmark preliminary; Contribution #3 加限定; Future work 列出 RE 多数据集验证

**[CONSENSUS] W-S2: Abstract 信息密度过高**
- 来源: R2-W1, R1 交叉 AGREE
- 9 行含 5 signal/3 family/4 metric/3 dataset/2 model + gap 概念 + technical arguments
- 修改建议: 聚焦 1-2 个核心 claim，具体数字移入 Introduction

**[CONSENSUS] W-S3: "First multi-family comparison" claim 过度依赖 scope 限定**
- 来源: R2-W4, R1 交叉 AGREE
- 通过堆叠修饰词确保 "first" 成立属于 scope engineering
- 修改建议: 改为描述性表述，避免 "first" claim

**[CONSENSUS] W-S4: "Cross-architecture" 用词过度**
- 来源: R1-W3, R2 交叉 AGREE
- 两模型均为 8B decoder-only transformer (GQA, RoPE, SwiGLU)
- 修改建议: 改为 "across two model families at 8B scale"

**[CONSENSUS] W-S5: 术语不一致**
- 来源: R3-W7 (Round 3 遗留, 仍未解决)
- Table 1 "Voting Conf." vs Table 4/7 "VC" vs 正文 "entity voting"
- 修改建议: 全文统一（建议全部用 VC）

**[CONSENSUS, low severity] W-S6: FK independence justification 不够严格**
- 来源: R1-W2, R2 交叉 AGREE with nuance (severity 偏低)
- Excess agreement (-0.4% to -4.0%) 未注明 configuration, 未引用 FK 非独立 rater 行为文献
- 修改建议: 补充 configuration 信息 + 引用; FK 非核心 contribution, 可接受 minimal fix

**[CONSENSUS, low severity] W-S7: TOST δ 选择缺乏外部锚点**
- 来源: R1-W4, R2 交叉 AGREE with nuance
- 多水平 δ 已构成 sensitivity analysis, 但需引用 IAA 数据
- 修改建议: 引用 1-2 篇 IE benchmark IAA 文献

**[R1 only] W-S8: Qwen3-8B thinking token 训练不一致**
- 来源: R1-W5, R2 交叉 AGREE
- SciERC 未禁用 enable_thinking, CoNLL/WNUT 显式禁用
- 修改建议: Limitations 讨论此不一致性

**[R2 only, R1 REBUT] W-S9: Soft Jaccard 方法论新颖性有限**
- 来源: R2-W3
- R1 rebut: application novelty 在 IE quality estimation 中是新的; Nédellec (2026) 承认其表面方法的局限
- 共识: SJ 有 application novelty 但不应过度宣传; "core structural signal" 可弱化为 "primary"

**[R2 only] W-S10: 与 Nédellec et al. (2026) 增量贡献论证不充分**
- 来源: R2-N2
- R1 rebut: WNUT-17 conditional collapse 和 logprob negative correlation 不是直觉可预测; difficulty-dependent crossover 是核心 claim
- 共识: Findings-worthy 但非 ground-breaking; 建议更诚实量化增量

### Minor（不影响接收）

- **M1** [CONSENSUS]: Semantic entropy 脚注（§4.2）——自述 "direct comparison not meaningful" 但给出具体数字，可能误导。建议缩短
- **M2** [R1]: `he2024uncertainty` bib entry 与引用上下文不匹配（sequential labeling 论文被描述为 LLM survey）
- **M3** [CONSENSUS]: Table 1 脚注格式（`\textsuperscript{†}` + `\footnotetext`）在 two-column 模板下可能渲染异常
- **M4** [R1]: Consensus-proximity = LOO-SJ 等价性声称缺少推导
- **M5** [CONSENSUS]: 部分 bib entries (`hobelsberger2025systematic`, `lightman2024verify`) 在 OpenAlex 未找到; `feng2025optimal` 和 `ye2025uncertainty` author name 可能有 variant
- **M6** [R2]: Ethics Statement 仅 2 句（格式合规但内容偏简）

---

## Reviewer Consensus

以下问题两位 Reviewer 在交叉分享后完全一致：

1. **Constrained decoding confound 是论文最大弱点** [AGREE]: 论文自身 Appendix F 数据（non-tied subset logprob selection +2.9pp, p=0.01）暗示 gap 主因是 score compression 而非 IE 固有属性。Title/Abstract/Conclusion 的 claim scope 需限定
2. **RE scope 不一致** [AGREE]: Abstract "preliminary" 与后续大量使用之间矛盾
3. **Abstract 过密** [AGREE]: 首次阅读难以把握核心 message
4. **"Cross-architecture" 过度** [AGREE]: 改为 "across two model families at 8B scale"
5. **"First" claim 应去掉** [AGREE]: scope engineering
6. **术语不一致** [AGREE]: 需全文统一
7. **统计分析质量高** [AGREE]: bootstrap CI、TOST、multi-seed 在 ACL 投稿中属上乘
8. **训练配置完整** [AGREE]: Reproducibility 4/5

---

## Reviewer Divergence

1. **Tautological 程度**:
   - R2: Gap 被两头夹击，整体 contribution 空心化 → Excitement 2.5
   - R1: Consensus-proximity/MBR failure 是 non-trivial → Excitement 3.5
   - **Resolution**: 共识认为 gap 不完全 tautological，但 C2 需 reframe 以 logprob+MBR failure 为重心

2. **与 Nédellec 增量**:
   - R2: 三个增量均偏弱
   - R1: Difficulty gradient 发现（WNUT-17 conditional collapse）不是直觉可预测
   - **Resolution**: Findings-worthy 但非 ground-breaking

3. **SJ 方法新颖性**:
   - R2: 标准技术组合
   - R1: Application novelty 在 IE context 中是新的
   - **Resolution**: 有 application novelty 但不应过度宣传

---

## Questions

1. Appendix F 的 non-tied subset 中 logprob selection 有效 (+2.9pp, p=0.01)。如果 constrained decoding 是 score compression 主因，free-form decoding 下 logprob 是否可能成为有效 selector？如何论证 gap 是 IE-inherent 而非 decoding-induced？
2. Consensus-proximity = LOO-SJ 的数学等价性缺少推导。能否补充？
3. FK excess agreement (-0.4% to -4.0%) 在哪个 configuration 测量？是否在所有配置一致？
4. WNUT-17 logprob 负相关 (ρ=-0.410) 的机制解释？

---

## Missing References

- "Trust but Verify! A Survey on Verification Design for Test-time Scaling" (2025) — 与 Discussion 中 verifier 建议直接相关 [两位 Reviewer 一致]
- MBR 在非 MT 任务 (summarization, QA) 中的应用文献 — 增强 Discussion §5 MBR 对比分析 [两位 Reviewer 一致]
- 最新 uncertainty quantification survey (2025-2026) [R2 建议]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未启用外部审稿）。

---

## Overall Assessment

**评分: borderline (3.0/5)**
**置信度: 高 (4/5)**

| 维度 | R1 | R2 | 加权 |
|------|-----|-----|------|
| Soundness | 3.0 | 3.5 | 3.25 |
| Excitement | 3.5 | 2.5 | 3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.0 | 3.0 | 3.0 |

**总结判断**: 这是一篇执行质量较高的 empirical study——统计分析严谨、实验设计公平、训练细节完整。核心概念（quality estimation vs sample selection 解耦）对 test-time scaling 实践有指导价值。

**但存在两个结构性问题阻碍更高评分:**

1. **Claim scope 与 evidence 不匹配**: 论文将 correlation-selection gap 呈现为 structured IE 的通用属性，但所有实验均在 constrained decoding 下进行，且论文自身数据（Appendix F non-tied subset）暗示 gap 主因可能是 score compression artifact。Title/Abstract/Conclusion 需加限定词。

2. **核心贡献的 tautological 成分**: 4/5 信号的 selection failure 是定义的逻辑后果（instance-level signals 无法 rank per-sample），真正 non-trivial 的发现是 logprob 的 failure 和 consensus-proximity/MBR 在 IE 中的 failure。C2 需 reframe。

**Findings track 接收条件**: 如果作者能 (a) 在核心 claim 中限定 constrained decoding scope, (b) reframe C2 以 logprob + MBR failure 为中心, (c) 统一 RE preliminary 标注, (d) 精简 Abstract, 则论文适合 Findings track。当前版本需 moderate revision。

---

## Detailed Comments（按 Section）

### Abstract
- 信息密度过高，需拆分为 2-3 句核心 claim
- "(SciERC, preliminary)" 限定词需在后续分析中一致使用
- "for Information Extraction" 需加 "under constrained decoding" 限定

### §1 Introduction
- Contribution 2 需 reframe：将 "5 signals all fail" 叙事改为以 logprob compression + MBR failure 为中心
- Contribution 3 需加 RE single-benchmark 限定
- "first multi-family comparison" → 改为描述性表述
- MBR 在 MT 中成功 → IE 中失败的非显然性论证可以加强

### §2 Related Work
- 引用覆盖良好
- 补充: test-time verification survey, MBR 非 MT 应用
- `he2024uncertainty` 引用上下文需修正

### §3 Method
- SJ 形式化清晰完整
- FK independence justification 补 configuration 信息
- Consensus-proximity = LOO-SJ 等价性需推导
- "core structural signal" → "primary structural signal"

### §4 Experiments
- 统计分析严谨
- Table 1 脚注格式检查 PDF 渲染
- Semantic entropy 脚注缩短
- TOST δ 引用 IAA 数据
- WNUT-17 logprob negative correlation 需机制解释

### §5 Discussion
- "Two layers" 结构良好但需更明确分离定义性 vs 经验性 gap
- 提升 Appendix F non-tied analysis 至此处
- 承认 non-tied evidence 对 claim 普适性的影响

### §6 Conclusion
- 加 constrained decoding scope 限定
- RE 限定与 Abstract 对齐
- "across model families" → "across two model families at 8B scale"

### Limitations
- 全面诚实
- 补充 thinking token 训练不一致性讨论

### Appendix
- Training config (Table 8) 完整 ✓
- Prompt template 提供 ✓
- Appendix F logprob tie analysis 应提升至主文