---
round: 25
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T07:33:49.212376+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 25 审稿报告 — gen-depth-contamination

**Venue**: EMNLP 2026 (ARR May 2026)
**审稿模式**: Fresh（初审）
**Reviewer 配置**: 2 人（R1: 方法严谨性+实验验证; R2: 新颖性+完整性+Related Work）
**轮次**: 1 轮（Round 1 后交叉分享达成共识，无需下一轮）

---

## Summary

本文提出"生成深度估计"（generational depth estimation）问题，使用 15 维统计特征 + OBD-LightGBM 分类器测量递归合成文本的可区分代际边界 K*_empirical。在 10 个模型配置（6 家族, 1B–8B）、3 个域、4 种解码策略上实验表明：web 文本 K*_empirical∈{1,2}（6/10 配置为 2），arXiv K*_empirical=3。核心发现为"一次洗白"效应：一次生成后文本即与更深层合成内容不可区分。下游验证表明 binary filtering 最优，与 K*=2 的预测一致。

---

## Strengths

**S1** [R1+R2 共识] **问题定义新颖且有实际动机**：generational depth estimation 是此前未被正式定义的问题，K*_empirical 填补了 binary detection 和 model collapse 文献之间的概念空白。"一次洗白"效应对数据 curation 社区有直接参考价值。

**S2** [R1+R2 共识] **实验设计严谨**：5-fold GroupKFold（按 seed document 分组）防止数据泄漏；self-BLEU 的 fold-internal 计算消除信息泄漏风险；bootstrap CI + permutation test + ANOVA 三重统计验证；10,000 次 permutation test 提供充分的 null distribution 估计。

**S3** [R1+R2 共识] **实验覆盖度极高**：10 个模型配置 × 4 种解码策略 × 3 个域 + 大量消融（segment length, seed robustness, dose-response, decoding strategy, LLM zero-shot comparison, neural probe, cross-scorer, cross-model transfer）。附录 21 个表格 + 5 个图。

**S4** [R1] **Cross-model transfer 实用性**：15D 统计特征实现 80–100% 跨模型准确率保留（Pythia↔OLMo 90–92%），feature ranking 跨 scorer 高度一致（ρ>0.90），增强了方法的实际部署前景。

**S5** [R1+R2 共识] **Limitations 极其彻底**：7 条具体限制覆盖了规模、协议、阈值、边界脆弱性、特征集依赖、segment length、curation 适用性。诚实程度超出同类工作。

**S6** [R1] **统计实践规范**：effect size（Cohen's h）、bootstrap CI、permutation p-value、ANOVA 交互效应分析齐备，是 NLP 实证研究的良好示范。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1** [R1-N2 + R2-N2, 双方最强共识] **θ=0.60 阈值敏感性高，K*_empirical 作为可操作量稳健性不足**
- θ∈[0.55, 0.70] 范围内 K* 从 3 变化到 1。Qwen-cont 1v2 CI 下界仅超 θ 0.002。
- Cohen's h=0.20 → θ=0.60 的映射假设 null AUC=0.50，但 permutation test 95th percentile null <0.55，实际 null 高于理论预期。
- 核心问题：K*_empirical=2 这一关键结论在 θ 微调时不稳定，论文未提供 θ-free 的表述方式。
- **要求**：(a) 报告 θ-free 指标（AUC gap 及其 CI），提供完整灵敏度曲线；(b) 在 Discussion 中明确鼓励读者根据应用场景选择 θ；(c) 第三条证据（distributional discontinuity）标为 post-hoc confirmatory。

**C2** [R1-N2 + R2-W3, 共识] **模型规模覆盖仅 ≤8B，核心结论 K*≈2 的泛化性未验证**
- 全部 10 配置为 1B–8B。当前主流模型（Llama-70B, GPT-4 等）远超此范围。
- 已有内部证据（0v1 JSD 从 ≤1.5B 的 0.15–0.27 降至 8B 的 0.077；Pythia 1.4B→6.9B K* 从 2→1）暗示规模增大可能降低 K*。
- Abstract 和 Conclusion 中 K*≈2 被呈现为通用结论，但实际适用范围仅 ≤8B。
- **要求**：Abstract/Conclusion 显式限定 "1B–8B" 适用范围。如可能，补充 ≥1 个 >30B 模型实验。

**C3** [R2-N1 + R1 同意, 共识] **Qwen 过度代表使 "6/10" 统计量误导**
- 6/10 K*=2 配置中 4 个来自 Qwen。按 family 统计：仅 2/6 家族 unanimously K*=2（Qwen 4/4, LLaMA 1/1），3/6 unanimously K*=1（OLMo, Mistral, Gemma）。
- Abstract "6/10 configurations" 技术正确但给读者过于乐观的印象。
- R1 补充：即使 K*=1 的配置也确认 boundary 极浅（≤2），one-wash 定性结论在所有配置成立。
- **要求**：(a) Section 4.1 添加 family-level 汇总表；(b) Abstract 同时报告 per-config 和 per-family 统计。

**C4** [R1-N1 + R2 同意] **DPI→AUC 推理链仅为启发式，K*_empirical 作为 lower bound 的理论地位不清**
- 论文以 DPI（MI 单调递减）motivate 期望 AUC 单调递减，但坦承 "AUC and mutual information are not formally equivalent"。K*_empirical 是 K*_theory 的 "lower bound" 仅为断言。
- R2 认为可降级为 Should-Fix（论文已诚实承认），R1 坚持 Must-Fix（这是全文理论框架根基）。
- **Director 判定**：Must-Fix（修改难度低但影响核心叙事完整性）。
- **要求**：明确区分 K*_empirical 为操作性定义 vs K*_theory 下界两个 claim；对 lower bound claim 要么给出形式证明要么降级为 conjecture。

### Should-Fix（影响评分但不一票否决）

**W1** [R2-N3, R1 部分反驳→降级] **Prompt-chain 生态有效性需限定**
- Retrain-chain K*≥4（Appendix D.7），"one-wash laundering" 可能是 prompt-chain 特有现象。
- R1 辩护：prompt-chain 是 web-scale contamination 主流路径（API 调用→发布→收录），retrain-chain 在实际 web contamination 中罕见。论文选择合理，但表述缺乏限定。
- **要求**：Abstract/Conclusion 添加 "under prompt-chain generation" 限定语。

**W2** [R1-W1 + R2 同意] **Cross-scorer 降级暴露部署局限**
- Qwen-cont cross-scoring AUC=0.5923(Pythia)/0.5858(OLMo) 均 <θ，K*=2→1。
- 实际部署中 generator 身份未知，cross-scoring 才是工作条件。K*=2→1 意味着退化为 binary detection。
- **要求**：Section 4.2 更突出讨论此限制；探讨 scorer-ensemble 策略。

**W3** [R1-W2 + R2 同意] **Filtering 效果量小且 dose-response 未在正文讨论**
- +0.74pp MMLU, +0.03pp HellaSwag（100% 合成极端条件下）。
- Appendix D.8：≤30% contamination 下所有策略差异消失（p>0.8）。
- 论文已定位为 consistency check，但正文未引用 dose-response，读者可能高估实际价值。
- **要求**：Section 5 或 Discussion 引用 dose-response 分析，承认现实污染比例下边际增益可忽略。

**W4** [R2-W1 + R1 同意] **Filtering 仅在单一 generator 验证**
- 仅 Qwen-1.5B continuation。K*=1 配置下 binary filtering 是否退化为普通 binary detection 未讨论。
- **要求**：Limitations 声明，Section 5 讨论 K*=1 场景。

**W5** [R2-W2, R1 反驳] **K*=2 相对 binary detection 的增量贡献讨论不足**（Reviewer 分歧）
- R2：结论 "binary is sufficient" 使增量贡献不明确。
- R1 反驳：K* 提供解释性价值（为什么 binary 有效）、域差异化（C4 vs arXiv）、策略指导（binary vs graduated），是度量框架而非仅实用策略。
- **Director 判定**：保留为 Should-Fix。Discussion 应更明确阐述 K*_empirical 的认识论贡献。

### Minor

**M1** [R1+R2] 正文缺少 Mistral-7B、Gemma-2-2B 数据覆盖——Section 4.1 应添加 1-2 句概述全部 10 配置结果。
**M2** [R2+R1 同意] 遗漏 Suresh et al. (2024) "Rate of Model Collapse"——Related Work 应补充。
**M3** [R2+R1 同意] Abstract "Cohen's h≈0.20" 缺乏上下文——替换为直观表述，技术细节移至 Section 3.1。
**M4** [R1] Figure 1 中 K* Estimation 步骤箭头指向不清——应标注为语料库层面估计。
**M5** [R2+R1 同意] Table 2 应视觉高亮 K* boundary 行。
**M6** [R2+R1 同意] self-BLEU deployment 替代方案应更突出说明。
**M7** [R1] Eq.1 后应明确声明 AUC 单调递减为经验观察而非理论保证。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识：

| 问题 | R1 | R2 | 状态 |
|------|----|----|------|
| θ=0.60 敏感性 | W3→升级 Must-Fix | N2 (Must-Fix) | [AGREE] 最强共识 |
| 模型规模 ≤8B | N2 (Must-Fix) | W3 (Should-Fix) | [AGREE] |
| Qwen 过度代表 | 同意 R2-N1 | N1 (Must-Fix) | [AGREE] 表述需改 |
| Cross-scorer 降级 | W1 (Should-Fix) | 同意 R1-W1 | [AGREE] |
| Filtering 效果量小 | W2 (Should-Fix) | 同意 | [AGREE] |
| Filtering 单配置 | 同意 R2-W1 | W1 (Should-Fix) | [AGREE] |
| DPI→AUC 理论缺口 | N1 (Must-Fix) | 同意降为 Should-Fix | [AGREE] 严重性有差异 |

---

## Reviewer Divergence

| 问题 | R1 立场 | R2 立场 | Director 判定 |
|------|---------|---------|---------------|
| Prompt-chain 生态有效性 | [REBUT] 降级 Should-Fix：prompt-chain 是 web contamination 主流路径 | Must-Fix：retrain-chain K*≥4 说明设定特有 | Should-Fix（R1 论证更有说服力，但同意需限定表述） |
| K*=2 vs binary detection 贡献 | [REBUT] K* 是度量框架，提供解释性+域差异化价值 | Should-Fix：增量贡献不清 | Should-Fix（分歧记录，双方各有理据） |
| Rewrite vs continuation 分析 | W4 (Should-Fix)：需更深入分析 | [REBUT] 现有分析在 8 页限制下足够 | Minor（R2 论点合理） |
| Pythia EOS truncation | M4：34-36% truncation 可能引入长度混淆 | [REBUT] Appendix Table 12 已充分讨论 | Dropped（已有覆盖） |

---

## Questions（需要作者澄清）

**Q1** [R1] 更强分类器（fine-tuned transformer encoder）是否会增加 K*_empirical？Neural probe K*=3（Qwen）是否意味着 K*_theory>2，从而削弱"一次洗白"叙事的绝对性？

**Q2** [R1] θ=0.60 映射假设 null AUC=0.50，但 permutation null 95th percentile <0.55。能否用 permutation null 直接校准 θ？

**Q3** [R1] Qwen-cont 1v2 AUC=0.611 的 fold 间方差是多少？是否有 fold 中 AUC<θ？

**Q4** [R1+R2] K*=1 模型（OLMo-1B）生成的污染数据下，binary filtering 是否仍有效？此时 K*-aware 的价值是否消失？

**Q5** [R1] arXiv 域 n=2,200 是 per-model 还是两个家族共享？每个深度级别的样本量？

**Q6** [R2] Cross-model retrain-chain（如 Qwen→Pythia→OLMo）下 K* 预期是什么？

**Q7** [R2] Appendix D.8 显示 ≤30% contamination 下策略差异消失——现实中 K*-aware filtering 是否实际无用？

---

## Missing References

| 引用 | 来源 | 重要性 | 共识 |
|------|------|--------|------|
| Suresh et al. (2024) "Rate of Model Collapse in Recursive Training" | R2 | Should-Cite | R1 同意 |
| Gehrmann et al. (2019) "GLTR" | R1 | Nice-to-Cite | R2 认为已被后续工作覆盖 |
| Tang et al. (2024) "The Science of Detecting LLM-Generated Text" | R1 | Nice-to-Cite | R2 需核实真实性 |
| Borji (2024) "A Note on Shumailov et al." | R2 | Nice-to-Cite | R1 认为相关性有限 |
| Dugan et al. (ACL 2024) "RAID" benchmark | R2 | Nice-to-Cite | R1 同意但非必须 |

---

## External Review

**状态**: 未请求（项目配置未启用 paperreview.ai）

---

## Visual Layout Check（非评分项）

**状态**: 已完成（0 critical, 8 warning, 19 info）

主要发现：
- **页面 1-2 纯文本**（warning）：连续 2 页无 display item。建议将 Figure 1 前移至第 2 页。
- **页面 3-6 视觉节奏优秀**（info）：Figure 1→Table 1+Figure 2+Figure 3→Table 2+Figure 4+Table 3→Table 4+Table 5，display items 密集穿插。
- **主正文密度**（info）：8 页含 4 figures + 5 tables = 9 个 display items（~1.1/页），符合实证论文预期。
- **Appendix 空白**（warning×6）：Table 10-13、Table 21-22、Table 26 附近存在显著空白，页面利用率 15%-50%。建议合并小表。
- **格式合规**（info）：ACL 匿名模板正确，无 LaTeX 残留/margin 溢出/未解析引用，References 格式统一。
- **Figure 质量**（info）：Figure 1 pipeline 清晰，Figure 2 AUC 衰减曲线带 CI shaded band，Figure 4 heatmap 数值标注清晰。

---

## Overall Assessment

**评分: 3.5 / 5（Borderline Conference）**

**对应 EMNLP 2026 ARR 标准**: 3.5 = Borderline Conference（介于可被主会议接收与 Findings 之间）

**R1**: 3.5 | **R2**: 3.5 | **Director 综合**: 3.5

**置信度**: 4/5

### 判定理由

**支持 Conference (4.0) 的因素**：
- 问题定义新颖，K*_empirical 是一个有清晰动机的新概念
- 实验设计严谨，统计实践规范，附录极其充分
- "One-wash laundering" 是一个可记忆、可操作的发现
- Cross-model transfer 增强了方法实用性

**拉低至 3.5 的因素**：
- θ=0.60 敏感性使核心结论 K*=2 的稳健性存疑（最关键）
- 模型规模 ≤8B，核心发现的泛化性未验证
- Qwen 4/10 过度代表，per-family 统计显著弱于 per-config
- DPI→AUC 理论桥接仅为启发式
- 下游 filtering 效果量小，现实污染比例下近乎无用
- Cross-scorer 降级使 K*=2 在部署条件下不稳健

**修改路径建议（不构成审稿意见，仅供参考）**：
如果作者能 (a) 提供 θ-free 表述和灵敏度曲线，(b) 限定 K*≈2 适用范围（1B–8B, prompt-chain），(c) 添加 per-family 统计，(d) 明确 K*_empirical 的 lower bound 理论条件——则有望达到 4.0 (Conference) 水准。这些修改均不涉及新实验，属于 framing/presentation 层面的改进。

---

## Detailed Comments

### Section 1 (Introduction)
- "6/10 configurations" 应同时报告 per-family 统计（2/6 unanimously K*=2）
- "one-wash laundering effect" 首次出现时应限定为 prompt-chain 场景
- Retrain-chain K*≥4 的对比应在 Introduction 末尾提及，而非仅在 Discussion

### Section 3 (Method)
- Eq. 1 后应明确声明 AUC 单调递减为经验观察
- θ=0.60 的第三条证据（distributional discontinuity）应标为 "post-hoc confirmatory"
- "lower bound on K*_theory" claim 需形式化或降级

### Section 4 (Experiments)
- 4.1: 添加 family-level 汇总表，正文覆盖全部 10 配置
- 4.2: Cross-scorer 降级的部署影响需更突出讨论
- Table 2: 高亮 boundary 行

### Section 5 (Filtering)
- 正文引用 dose-response 分析（Appendix D.8）
- 承认 ≤30% contamination 下策略差异消失
- 讨论 K*=1 场景下 filtering 是否退化

### Section 6 (Discussion)
- K*_empirical 作为度量框架（vs 仅作为 binary detection 副产品）的价值需更明确阐述
- Prompt-chain vs retrain-chain 的适用范围需更清晰界定

### Section 7 (Conclusion)
- 显式限定 "1B–8B" 和 "prompt-chain" 适用范围
- 补充 per-family 统计

### Abstract
- "Cohen's h≈0.20" 替换为直观表述
- 同时报告 per-config 和 per-family 统计
- 添加 prompt-chain 限定语