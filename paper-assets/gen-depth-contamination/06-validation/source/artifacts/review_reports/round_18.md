---
round: 18
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-20T10:49:40.205182+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Generational Depth Estimation of Recursive Synthetic Text

**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**Reviewer 编排**: 2 名 Reviewer（R1 方法严谨性+实验设计, R2 新颖性+完整性+写作质量）
**轮次**: Round 1（一轮收敛，交叉回应完成）

---

## Summary

本文提出 generational depth estimation 问题：给定一段文本，估计其经过了多少轮递归合成生成。作者定义了 discrimination boundary K*（使用 OBD-LightGBM 分类器在 bootstrap 95% CI lower > θ=0.60 条件下能可靠区分的最大深度），在 prompt-chain 设置下，对 10 个模型配置（6 个架构家族，1B-14B）、4 个域（C4, Wikipedia, arXiv, Code）进行了系统实证研究。核心发现：web text K*=2（7/9 continuation-mode 配置，4/6 架构家族），domain ordering arXiv > C4 ≥ Code > Wikipedia 跨 θ 稳定，DeBERTa 在高复杂度域可突破 OBD ceiling（two-tier ceiling）。论文还测试了 cross-model transfer 和 K*-aware data filtering。

---

## Strengths

1. **问题定义新颖且及时** [R1-S1, R2-S1, 共识]：K*（递归合成文本可辨别深度边界）是一个之前未被形式化的概念，填补了 binary detection 和 model collapse 之间的空白。

2. **实验覆盖面极广** [R1-S2, R2-S2, 共识]：10 个模型配置、6 个架构家族、4 个域、4 种解码策略、cross-scorer 验证、DeBERTa upper bound、neural probe、feature ablation、多种统计检验。在同类经验型 NLP 论文中属于高水准。

3. **统计方法严谨** [R1-S5, R2-S3, 共识]：所有 boundary comparison 配有 bootstrap 95% CIs + permutation p-values；LOFO 交叉验证 θ；PELT changepoint 作为 θ-free 验证；F1@0.50 独立确认。

4. **Limitations 异常详尽坦诚** [R1-S3, R2-S4, 共识]：9 条 numbered limitations 覆盖 scope、protocol、threshold、marginal boundary、feature set、segment length、curation、family balance、transfer coverage。远超一般论文标准。

5. **Domain ordering invariance** [R1-S4, R2-S6, 共识]：arXiv > C4 ≥ Code > Wikipedia 排序跨 θ、跨模型、跨 scorer 稳定，比绝对 K* 值更 robust，提供了对 domain structural complexity 的有效排序。

6. **Two-tier ceiling 发现** [R2-S5]：OBD 与 DeBERTa 在 low-complexity domain（C4, Code）上 K* 一致，high-complexity domain（Wikipedia, arXiv）上 DeBERTa K* 高 1 级，揭示 domain complexity 与 classifier expressiveness 的交互。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W-MF1** [critical, 共识] **Prompt-chain scope 与 Introduction framing 严重错位**
- Introduction line 6（"when models train on the outputs of earlier models"）明确指向 retrain-chain，但所有主实验为 prompt-chain。Appendix C.1 retrain-chain K*=7，与正文 K*=2 差 5 个 generation。Discussion 仅一句提及。
- 论文以 "web-scale contamination" 为 motivation，但 web-scale 污染涉及 retrain-chain、混合管道、跨模型交叉生成，prompt-chain 仅是最简单的场景。
- **要求**：Discussion 增加专门段落对比 prompt-chain 与 retrain-chain；或将 retrain-chain 结果提升到正文；Introduction 更精确地限定研究范围。
- [R1-N1 + R2-N3, 交叉共识]

**W-MF2** [critical, 共识] **K*=2 核心发现的脆弱性被摘要和标题低估**
- 7/9 continuation-mode 配置 K*=2（78%），但以 unique families 计仅 4/6（67%），Gemma-2-2B 和 Mistral-7B 均为 K*=1。
- 多个 K*=2 配置处于 borderline：Qwen-cont CI lower 仅超 θ 0.002，cross-scorer 降至 K*=1；LLaMA-3.1-8B CI lower 距 θ 0.3pp。
- 7B 跨模型迁移在 boundary 层面 fragile：4/6 off-diagonal 1v2 pairs below θ。
- Abstract 的 "7/9 configurations" 表述给人 robust 的印象，但实际 borderline 程度高。
- **要求**：Abstract 同时报告 per-family 结果（"4/6 families"）；明确提及 borderline cases；Contribution (c) 平衡 transfer 的优势与 boundary fragility。
- [R2-N2, R1 AGREE（同意脆弱性但认为统计证据仍支持 K*=2 作为 majority finding）]

**W-MF3** [critical, 共识] **模型规模外推趋势威胁核心结论的时效性**
- LightGBM 1v2 AUC: 0.626 (1.5B) → 0.621 (14B) → 0.618 (32B)，DeBERTa: 0.705 → 0.678 → 0.694。
- 单调下降趋势暗示 70B+ 模型上 K* 可能降为 1。当前最 impactful 的 LLM（GPT-4 class, 70B+）恰好在论文未覆盖的规模范围。
- Discussion 仅一句 "70B+ extrapolation warrants investigation"。
- **要求**：对 AUC-vs-scale 做定量分析（如 log-linear 拟合）；讨论 K*=1 的 crossover point；Abstract/Conclusion 明确限定 "≤32B"。
- [R1-N2, R2 AGREE]

**W-MF4** [critical, 共识] **Filtering 实验效果量过小，contribution (c) 与实际证据不匹配**
- Binary filtering MMLU 改善仅 0.76pp，HellaSwag 无显著差异（Table 6）。
- 仅 2 个架构验证（Qwen-1.5B, Pythia-1.4B）。
- arXiv K*=3 时 graduated filtering 同样失败，论文自己承认 "K* measures discriminability but overestimates filtering utility"。
- Introduction contribution (c) 仍以 "correctly predicts binary > graduated" 表述，仅对 C4 成立，不具一般性。
- **要求**：降级 filtering 为"一个域上的初步观察"而非 contribution；或大幅增强 filtering 实验；对齐 Introduction (c) 与 Section 5 的实际结论。
- [R1-N3 + R2-W2, 交叉共识]

### Should-Fix（影响评分）

**W-SF1** [warning, 共识] **Qwen 家族过度代表（5/10 configs），aggregate statistics 偏向**
- "7/9 configurations yield K*=2" 中 4 个来自 Qwen。以 family 计为 4/6 (67%)。Qwen 内部一致性不令人惊讶（共享 tokenizer + 训练数据分布）。
- **要求**：所有 aggregate claim 优先使用 per-family 统计。
- [R1-W1 = R2-W4]

**W-SF2** [warning, 共识] **Table 1 / 配置数量不一致**
- Section 3.3: "nine configurations, five families"；Section 4: "ten configurations, six families"。Gemma-2-2B 在 Table 5 出现但 Table 1 缺席。
- **要求**：统一数字，确保 Gemma 在所有相关表格中一致处理。
- [R1-M1 = R2-W1]

**W-SF3** [warning, 共识] **Discussion 过于简短（2 段 ~200 词）**
- 缺少：(a) 为什么 K*=2（信息论解释）；(b) domain ordering 深层原因；(c) 对 model collapse 社区的 implications；(d) 规模趋势分析；(e) prompt-chain vs retrain-chain 对比。
- **要求**：扩展 Discussion 至至少 4-5 段。
- [R2-W5, R1 AGREE]

**W-SF4** [warning, 共识] **θ=0.60 仍为 post-hoc 选择**
- 尽管有 LOFO、changepoint、permutation test 验证，K* 在 5pp window 内稳定但绝对值对 θ 敏感。
- Domain ordering invariance 是比 K*=2 更 robust 的 claim。
- **要求**：考虑提升 domain ordering invariance 为主发现。
- [R1-W2, R2 AGREE]

**W-SF5** [warning, 共识] **Scorer 模型规模未做消融**
- 所有 15D 特征由 ≤1.5B scorer 计算。Cross-scorer 仅在 ≤1.5B 之间交叉。未测试 7B scorer 对 K* 的影响。
- **要求**：至少用一个 7B scorer 计算特征并报告 K*，或在 Limitations 中讨论 scorer 规模影响。
- [R1-W4, R2 AGREE（不升级为 critical）]

---

## Reviewer Consensus

两位 Reviewer 在以下问题上完全一致（[AGREE]）：
1. **Prompt-chain 限制**需要在正文中充分讨论（R1-N1 = R2-N3）
2. **K*=2 脆弱性**被 Abstract 低估（R2-N2, R1 AGREE with nuances）
3. **模型规模外推**趋势需定量分析（R1-N2, R2 AGREE）
4. **Filtering 偏弱**，contribution (c) overclaimed（R1-N3 ≈ R2-W2）
5. **Qwen 过度代表**（R1-W1 = R2-W4）
6. **Table 1 / 配置数不一致**（R1-M1 = R2-W1）
7. **Discussion 过短**（R2-W5, R1 AGREE）
8. **θ post-hoc 但验证充分**，domain ordering 更 robust（R1-W2, R2 AGREE）
9. **Scorer 规模未消融**（R1-W4, R2 AGREE）
10. **Missing references**：Dohmatob, Seddik, RADAR, Tulchinskii（双方 AGREE）

---

## Reviewer Divergence

**方法论新颖性**（核心分歧，未解决）：
- **R2 立场**（N1 critical）：15D 手工特征 + LightGBM 均为现成工具，Section 3 仅 1.5 页，无独立方法贡献。EMNLP 主会议通常期待方法论贡献或显著实际应用价值。
- **R1 反驳**：本文定位为 empirical characterization study，贡献在于 findings（K* 概念、domain ordering、two-tier ceiling）而非 methods。K* 定义整合 CI + 单调约束 + operational threshold 并非 trivial。ACL/EMNLP 接收过大量 empirical characterization 论文。
- **Director 判断**：R2 的批评有合理性——纯 characterization study 需要 findings 足够 impactful 来弥补方法层面的空白。结合 prompt-chain 限制和 filtering 弱效果，本文的 practical impact 不足以仅凭 findings 达到 EMNLP 主会议标准。但 R1 关于 empirical characterization 的辩护也成立——不应以 methods paper 的标准苛求。此分歧记录在案，不构成独立 must-fix。

**次要分歧**（不影响总评）：
- Eq. 1 单调性假设（R1-W5 should-fix vs R2 REBUT 认为已充分处理）
- Abstract "contaminated" 用词（R1-M3 建议中性化 vs R2 REBUT 认为是标准术语）
- Abstract 信息密度（R2-W3 should-fix vs R1 REBUT 认为 empirical paper 需要）
- "Domain as primary factor" 措辞（R2-M4 建议改 correlate vs R1 REBUT 认为 within-model evidence 充分）

---

## Questions

1. 如果用 7B 级别的 scorer（如 Qwen2.5-7B）计算 15D surprisal 特征，K* 是否会改变？
2. Retrain-chain K*=7 在 mixed setting（部分 prompt-chain + 部分 retrain-chain）下会如何变化？
3. AUC 1v2 的 1.5B→32B 下降趋势是否可以 log-linear 拟合？预计在什么 scale 下 K* 降至 1？
4. 论文承认 "K* measures discriminability but overestimates filtering utility"——如果 K* 不能指导 filtering，其 practical value proposition 是什么？
5. Domain ordering（arXiv > C4 ≥ Code > Wikipedia）是否可以用更基础的文本统计量（如 vocabulary richness、sentence complexity）直接预测？

---

## Missing References

- **Dohmatob et al. (2024)** "Model Collapse Demystified" (arXiv 2402.07712) — DPI 论证相关。需验证是否独立于已引用的 dohmatob2024model 和 dohmatob2025strong。[R1 提出, R2 AGREE]
- **Seddik et al. (2024)** "How Bad is Training on Synthetic Data?" — retrain-chain 理论分析。[R1 提出, R2 AGREE]
- **RADAR** (Li et al., 2023) "Robust AI-Text Detection via Adversarial Learning" — adversarial training 方向 binary detector。[R2 提出, R1 AGREE]
- **Tulchinskii et al. (2024)** "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts" — intrinsic dimension 特征，替代特征空间可能性。[R2 提出, R1 AGREE]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 6 info）。

**Warning:**
1. **末页 (p.27)**：仅 ~35% 面积有内容（Tables 48-49），下方 ~50% 空白。可重排合并以消除尾页空洞。
2. **Page 5**：单页堆叠 3 个 display items（Table 2 + Figure 2 + Figure 3），图内 axis label 和 legend 字号接近可读下限。

**Info:**
- 首页无视觉锚点（纯文字），Figure 1 在 p.2 出现。建议加 teaser figure。
- Figure 4 heatmap 数字字号偏小（~6pt）。
- Qwen-cont 和 OLMo-1B 线条颜色较近，灰度打印可能混淆。建议辅以不同 marker shape。
- 附录表格极密集（p.19-20），字号小于正文。
- 8 页主文含 11 个 display items（5 fig + 6 table），密度偏高。
- Discussion + Conclusion 各约 1 段，较压缩（与 W-SF3 一致）。

---

## Overall Assessment

**评分：3.0 / 5（Findings）**

**置信度：4 / 5**

**Reviewer 评分**：R1 = 3.5（Borderline Conference），R2 = 3.0（Findings）

**综合评分理由**：

本文提出了一个 genuinely novel 的研究问题（generational depth estimation），并以极其全面的实验设计和严谨的统计方法进行了系统研究。Domain ordering invariance 和 two-tier ceiling 是有独立价值的发现。Limitations 的坦诚程度在同类论文中罕见。

然而，多个结构性问题阻碍了主会议接收：

1. **Scope 限制**：论文以 web-scale contamination 为动机但仅研究 prompt-chain，而 retrain-chain K*=7 说明两者差异根本性。Introduction framing 与实验 scope 存在错位。

2. **核心发现脆弱**：K*=2 在多个配置上为 borderline（CI margin ≤ 0.3pp），cross-scorer/cross-model transfer 在 boundary 层面 fragile。以 family 计仅 4/6 (67%) 支持 K*=2。规模外推趋势暗示 K*→1 at 70B+。

3. **实际应用价值有限**：Filtering 改善 less than 1pp，arXiv 反证 K*→filtering 因果链不成立。论文自我承认 "overestimates filtering utility"。

4. **方法论层面**无独立贡献（15D 手工特征 + LightGBM），需要 findings 或 practical impact 来补偿——但两者力度均不够强。

综合评估：论文的问题新颖性和实验严谨性足以支撑 **Findings 接收**，但 scope 限制、核心发现的 borderline 性质和有限的实际影响阻碍了主会议接收。

**建议修改方向**（不构成指导，仅记录审稿共识）：
1. 在正文中充分讨论 prompt-chain vs retrain-chain，消除 framing 错位
2. 以 per-family 统计取代 per-config 统计作为主要 claim
3. 降级 filtering 为观察而非 contribution
4. 扩展 Discussion 讨论规模趋势和理论 implications
5. 对 AUC-vs-scale 趋势做定量分析
6. 统一 Table 1 / 配置数量

---

## Detailed Comments

### Section 1 (Introduction)
- Line 6 "when models train on the outputs of earlier models" 指向 retrain-chain 但实验为 prompt-chain，需修改 framing [W-MF1]
- Contribution (c) "correctly predicts binary > graduated" 仅对 C4 成立，arXiv 反证 [W-MF4]
- "7/9 continuation-mode configurations" 应同时报告 "4/6 families" [W-SF1]

### Section 3 (Method)
- Eq. 1 的 ∀j≤k 约束依赖经验单调性，非理论保证。论文已 acknowledge 但可更明确 [R1-W5 vs R2 REBUT]
- θ=0.60 post-hoc 选择已多重验证，但应提升 domain ordering invariance 为主发现 [W-SF4]
- K* 符号体系（K*_theory, K*, K*_neural, K*_binary）需在首次出现时统一说明 [Minor]

### Section 3.3 / Table 1
- 配置数不一致（9 vs 10），Gemma-2-2B 缺席 Table 1 但在 Table 5 出现 [W-SF2]

### Section 4 (Experiments)
- Table 4 AUC 下降趋势需在 Discussion 中做定量分析 [W-MF3]
- Cross-model transfer: Contribution (c) "80-92% accuracy retention" 过于乐观，4/6 boundary pairs below θ [W-MF2]

### Section 5 (Filtering)
- 效果量 less than 1pp 不足以支撑 contribution claim [W-MF4]
- Introduction contribution (c) 与 Section 5 结论不一致 [W-MF4]

### Section 6 (Discussion)
- 仅 2 段 ~200 词，对 empirical characterization study 而言过短 [W-SF3]
- 缺少：K*=2 信息论解释、domain ordering 深层原因、model collapse implications、规模趋势分析、prompt-chain vs retrain-chain 对比 [W-SF3, W-MF1]

### Section 7 (Conclusion)
- 仅 4 行，缺 synthesis 和 future directions [Minor]

### Limitations
- 高质量，9 条覆盖全面。无需修改。

### 格式合规
- 页数：正文 8 页 ✓
- 模板：\usepackage[review]{acl} ✓
- 匿名：Anonymous ✓
- 破折号：正文行文中未发现 em-dash ✓（符合用户规则）
- AI 写作痕迹：未发现 ✓
- 引用：52 条 bib entries，0 orphan，0 missing，无虚假引用 ✓（3 条 first_author mismatch 为元数据格式差异）