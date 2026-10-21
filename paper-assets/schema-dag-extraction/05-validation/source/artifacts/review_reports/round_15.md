---
round: 15
overall_score: 3.0
timestamp: 2026-05-18T05:41:58.461285+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 15 审稿报告：schema-dag-extraction

**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**Venue**: EMNLP 2026 via ARR May 2026 cycle
**审稿编排**: 2 名 Reviewer（R1: 方法严谨性+实验设计+统计论证；R2: 新颖性+完整性+写作质量+格式合规）
**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT） → 收敛判断 → 汇总报告

---

## Summary

本文对 training-free LLM 信息抽取中 schema 复杂度如何预测性能下降进行了系统性实证研究。作者将性能下降分解为两个维度——count-related recall decline 和 confusability-related type substitution——并通过 BCS-controlled quasi-experiments 在 FewRel、DocRED、Few-NERD、MAVEN 四个数据集上验证。论文还报告了 schema decomposition (SDGD) 的负面结果及其机制诊断。实验设计精细、统计方法严谨（TOST、bootstrap CI、permutation tests），负面结果诊断深度出色，Limitations 极为坦诚。但核心 confusability metric (SCS/BCS) 与 LLM-PEE 形式相同、practical effect size 小（typical 2.2pp）、强结果集中在 RE 任务，novelty 和 practical significance 不足以支撑主会议接收。

---

## Strengths

**S1. 实验设计精细且系统化** [共识]
Count curves + BCS-controlled 的双范式设计有效隔离 count 和 confusability。Within-pool analysis（80-relation pool → 16-relation subsets）控制 pool composition confound（permutation p=0.60）。BCS-controlled 跨 FewRel 和 DocRED 的一致性提供了 replication 证据。

**S2. 统计方法论高于 venue 平均水平** [共识]
TOST equivalence testing（而非仅靠 NHST non-significance）、percentile bootstrap CI (B=10,000)、cluster bootstrap for pairwise correlations、variance decomposition、permutation tests。TOST sensitivity analysis across margins 和 logit-scale sensitivity check 体现审慎态度。在 EMNLP submissions 中不常见。

**S3. 负面结果报告诚实且诊断深刻** [共识]
SDGD failure 不仅报告失败，还精确诊断 merge amplification（NER precision 0.563→0.210）和 routing failure（constrained decoding 导致 73.4% instances 在 3-5 sub-schemas 同时获正预测）。Few-shot 反而扩大 confusability gap (+4.3pp) 也是有价值的负面发现。

**S4. Centrality confound 发现有方法论价值** [共识]
MAVEN 上 BCS-F1 正相关的发现、centrality confound 的诊断、partial correlation 控制后效应消失（p>0.2），以及 "mean BCS 只适用于 cross-domain schemas" 的结论，对后续使用 embedding-based metrics 的研究有方法论指导意义。

**S5. Cross-model validation 覆盖面广** [共识]
Qwen3-32B → Llama-8B → Llama-70B → Gemini Flash (API)，覆盖 open-weight 和 proprietary，8B-70B+ scales。Dimension 1 在所有模型上复制。

**S6. Limitations 模范级别** [共识]
8 条 limitation + multiple comparisons 讨论，覆盖 model coverage、effect size、factorial interaction、decomposition scope、evaluation metric、format specificity、causal mechanism、data contamination。远超 venue 平均水平。

**S7. 写作质量高、格式合规** [R2]
无 AI 写作痕迹（无 em-dash、无 -ing 短语结尾、无过度分段），术语首次出现均有定义，正文恰好 8 页，Limitations section 存在，Checklist 完整，匿名化正确。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. [critical] [共识] Logit-scale TOST inconclusive (p=0.209) 削弱 "bounded association" 核心 claim**
- 位置：§4.4 Multi-Dimensional Degradation, Appendix F
- Linear-scale TOST p=0.003 at ±3pp，但 logit-scale interaction 0.111 logit units (p=0.047, marginally significant)，logit-scale TOST p=0.209 (inconclusive)。Accuracy 接近 50%（high-BCS ≈ 51%）时 linear scale 系统性压缩 interaction effects。选择 linear scale 作为 "primary test" 是 convenience choice，不是 methodological necessity，构成分析自由度。
- 论文的 back-transformation argument (2.78pp at floor p=0.51, within ±3pp) 提供 partial mitigation。Inconclusive ≠ rejected，但 claim 必须降级。
- **要求**: 正文（非仅 Appendix）报告 logit-scale 结果；claim 改为 "consistent with bounded association under the primary linear specification; inconclusive on logit scale"；报告 TOST n=69 at ±3pp 的 post-hoc power。

**W2. [critical] [共识] NER/ED batch-level 结果实质为 null，"three tasks, four datasets" generality claim 虚高**
- 位置：§4.3, §4.5, §4.6, Title, Abstract
- NER batch-level BCS-F1: r≈0, n=450。MAVEN per-type BCS-F1: centrality confound 完全解释 (p>0.2 after control)。NER pairwise SCS: r=0.112, r²=1.3%。
- Dimension 1 (count decline) 跨任务成立（NER 0.72→~0.27, RE monotonic）。Dimension 2 (confusability) 仅 RE batch-level 成立。标题 "Training-Free LLM Information Extraction"（无限定词）暗示跨任务通用性。
- Contribution 3 将此称为 "task asymmetry" 是诚实的，但 R2 正确指出这实质上是 NER/ED 的 null result。MAVEN 仅贡献 1 行 pairwise 数据 + centrality confound 分析，不支撑 "event detection" 和 "four datasets" claim。
- **要求**: 标题或 Abstract 加入 confusability 效应的 RE-specificity 限定；"four datasets" → "three primary datasets with supplementary MAVEN analysis"；或在 Abstract 中平衡呈现 null results。

**W3. [critical→warning] [基本共识，severity 分歧] DocRED R²=0.53 (n=35) CI 极宽 [0.27, 0.73]，"22-53%" 上界在叙事中权重过高**
- 位置：Abstract, §1 Contribution 2, §4.3, §5 Discussion
- R1 列为 critical，R2 认为 lower severity（DocRED 是 replication dataset，primary R²=0.218 from FewRel n=100 更可靠）。Adjusted R²=0.511，shrinkage 仅 0.014，slope 高度显著 (p<0.001)。CI 宽因 n 小，非 effect 不稳定。
- **要求**: "22-53%" 表述后加注 CI 和样本量：如 "22% [FewRel, n=100] to 53% [DocRED, n=35; 95% CI: 27-73%]"。降低 53% 在 summary framing 中的权重。

### Should-Fix（影响评分但不一票否决）

**W4. [major] [共识] Formal power analysis 缺失**
- TOST n=69 at ±3pp 的 power 未报告。NER null (n=450, r≈0) 的 minimum detectable effect size 未报告。Power 不足会直接影响 linear-scale equivalence conclusion (p=0.003) 的可信度和 NER null claim 的解读。
- **要求**: 报告 TOST post-hoc power；NER null 的 minimum detectable r at 80% power。

**W5. [major] [共识] Single-seed (seed=42) 实验，typical effect 2.2pp 与 seed variance 2.7pp 可比**
- BCS-controlled experiments、DocRED、MAVEN、cross-model validation 均为单 seed。Count curves 有 3 seeds。Seed SD=2.7pp at count 16（Appendix K）与 typical BCS gap 2.2pp 量级可比，意味着某些 seed 下 effect 可能不显著。Bootstrap CI 只捕获 batch composition variance，不含 seed variance。
- **要求**: 核心 BCS-controlled RE 实验增加 multi-seed replication；或在 Limitations 中明确说明影响。

**W6. [major] [共识] Dimension 2 跨模型验证不充分**
- BCS-controlled 完整验证仅 Qwen3-32B 和 Llama-8B。Llama-70B 仅 count=16 一个数据点（$\Delta=+10.9$pp, CI excludes zero）。Gemini 无 Dim2 数据。Abstract/Conclusion "patterns replicate across model scales and architecture families" 暗示全面验证。
- **要求**: Abstract/Conclusion 区分 Dim1 和 Dim2 的验证范围。

**W7. [major] [R2 raised, R1 partially agrees] SCS/BCS 与 LLM-PEE 形式相同，Abstract "operationalize" 措辞暗示独立新颖性**
- SCS = pairwise cosine similarity of type name embeddings，论文 §2 自承与 LLM-PEE 相同。BCS = mean aggregation。Novelty 完全在 experimental framework 和 findings。但 Abstract/Contribution 措辞给读者 metric 本身是贡献的印象。
- R1 认为是 presentation issue（§2 self-qualification 已充分），R2 认为是 structural novelty deficit（capping the paper at Findings）。
- **要求**: Abstract "operationalize confusability via SCS" → 更中性措辞（如 "quantify confusability using pairwise embedding similarity"）；Contribution 2 明确声明 metric 与 LLM-PEE 相同，贡献在于 controlled framework。

**W8. [major] [共识] Practical effect size 小 (2.2pp typical gap, r²=1.3%)，Abstract 叙事重心偏向极端条件数字**
- Typical-batch BCS gap 2.2pp (CI [0.4, 4.0])，quartile gap 3.9-5.3pp。Abstract 领衔 -49pp (Dimension 1, DocRED full-schema) 和 "22-53%" R²。虽 Abstract 已区分 Dim1/Dim2 并报告 2.2pp，但叙事重心在戏剧性数字。Introduction findings summary 反复强调 extreme-batch gap，practical magnitude 放在 §4.3 的一个 paragraph。
- R1 认为 Abstract 的事实区分正确（partial rebut），但同意叙事重心偏移。R2 认为 cherry-picking。
- **要求**: Abstract 更突出 typical-batch magnitude；Introduction findings 平衡 extreme vs typical。

### Minor

**W9.** [info] Aggregation simulation (Appendix J) 声称 "not evidence base" 但正文 §4.3/§5 引用 ~3× amplification 作论证——定位矛盾。
**W10.** [info] ρ=0.35 inter-pair SCS correlation 未报告 CI，aggregation simulation 缺 sensitivity analysis。
**W11.** [info] Table 2 缺 FewRel pairwise r=0.187。
**W12.** [info] NER U-shaped recovery 解释 ("type-filtering overhead elimination") 缺实验证据。
**W13.** [info] Orphan bib entries: bogdanov2024nuner, xie2024selfimproving, zhang2023llmaaa, cheng2023batch, levy-2024-same-task。
**W14.** [info] Gemini count 64 仅 13/25 batches，partial data 可信度打折。

---

## Reviewer Consensus

以下为两位 Reviewer 达成共识的关键问题：

1. **[AGREE] Logit-scale TOST inconclusive**: bounded association claim 需限定为 "under linear specification; inconclusive on logit"。R1 列为 critical N1，R2 列为 major W2，交叉后 R2 AGREE。
2. **[AGREE] NER/ED generality overclaim**: confusability strong story 限于 RE。R2 列为 critical N3，R1 交叉 "substantially agree"。Dim1 跨任务成立，Dim2 batch-level 仅 RE。
3. **[AGREE] Single-seed limitation**: typical 2.2pp 与 seed SD 2.7pp 可比。R1 W3 + R2 W3，交叉共识。
4. **[AGREE] Power analysis 缺失**: TOST 和 NER null 均需 power 报告。R1 W1，R2 交叉 AGREE。
5. **[AGREE] DocRED R² CI 宽**: 需在正文报告 CI，降低 53% 在 framing 中权重。R1 N2，R2 交叉 AGREE with nuance。
6. **[AGREE] Dim2 跨模型验证不充分**: Abstract/Conclusion 需区分两个 dimension 的验证范围。R1 W4，R2 交叉 AGREE with nuance。
7. **[AGREE] MAVEN 参与度极低**: "four datasets" → "three primary + supplementary"。R2 W1，R1 交叉 AGREE。
8. **[AGREE] Orphan bib entries**: 5 个未引用条目需清理。R2 W6，R1 交叉 AGREE。

---

## Reviewer Divergence

1. **SCS novelty severity**: R2 认为 SCS/BCS 无独立新颖性是 structural problem，将论文 ceiling 限制在 Findings（即使 soundness 全修也不升 Conference）。R1 认为是 presentation issue（§2 self-qualification 已充分，修改 Abstract 措辞即可）。**Review Director 评估**: R2 的批评有道理——metric 形式等同于 prior work 是客观事实，但论文的核心贡献在 experimental framework 和 findings 而非 metric 本身，positioning 调整可以部分缓解。这更接近 R1 的判断（presentation issue），但对 novelty-sensitive 的 reviewer 确实构成 acceptance barrier。

2. **Abstract framing / cherry-picking**: R2 认为 Abstract 以 -49pp 领衔构成 cherry-picking。R1 反驳：Abstract 已明确区分 Dim1(-49pp)/Dim2(2.2pp) 且用 "dominates" 连接。**Review Director 评估**: 事实层面 R1 正确（Abstract 确实区分了），但 R2 的阅读体验反馈有效——审稿人快速扫描时 -49pp 的数字冲击力遮盖结构化区分。叙事调整而非事实纠正。

3. **TOST margin Cohen's d=0.5**: R1 认为用 d=0.5 (medium) 定义 equivalence margin 逻辑不通（medium ≠ negligible）。R2 反驳：TOST SESOI 不要求 "negligible"，论文的 130% amplification argument 是主要 justification，Cohen's d 仅辅助参照。**Review Director 评估**: R2 的 TOST 方法论理解更准确。SESOI = smallest effect of practical significance，不等于 negligible。但 d=0.5 的类比确实容易误导，建议弱化或删除。

4. **Overall score**: R1 给 3.5 (Borderline Conference)，R2 给 3.0 (Findings)。核心分歧在 novelty 权重和负面结果的价值评估。R1 认为 task asymmetry、centrality confound、SDGD 诊断有独立的分析价值 (Excitement 3.0)。R2 认为这些不改变 novelty deficit (Excitement 2.5)。

---

## Questions for Authors

Q1. TOST 在 n=69 下对 ±3pp margin 的 statistical power 是多少？如果 power < 0.8，linear-scale equivalence conclusion 的可信度如何？

Q2. Aggregation simulation (Appendix J) 中 ρ=0.35 的 CI 是多少？如果 ρ=0.20，simulated batch R² 大约是多少？

Q3. 是否尝试过在 NER 上使用 type-only matching（忽略 boundary）来检测 batch-level confusability signal？

Q4. 论文多处出现 "schema-associated degradation" 和 "schema-induced degradation"——请确认全文是否已统一为 correlational 措辞。

Q5. SCS 与 LLM-PEE 的 partitioning criterion 形式相同，论文的 incremental contribution 如何 beyond controlled experimentation？是否有 evidence 表明 SCS/BCS 在 schema design guidance 方面有 practical utility（超出分析意义）？

---

## Missing References

**R1 提出**: Funder & Ozer (2019) effect size critique; Wellek (2010) TOST 教材; Schuirmann (1987) TOST 原始论文; constrained decoding 对 calibration 影响的文献。
**R2 提出**: DLiSC (arXiv:2505.14992, Dual-LoRA with Incremental Schema Caching); SPT (arXiv:2506.01276, Schema as Parameterized Tools)。
**共同建议**: structured prediction calibration 文献。

---

## External Review (Stanford Agentic Reviewer)

未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**评分**: 3.0 (Findings)

**EMNLP 2026 评分标准对照**:
- 5 = Consider for Award (前 2.5%)
- 4 = Conference (可被主会议接收)
- 3.5 = Borderline Conference
- 3 = Findings (可被 Findings 接收)
- 2.5 = Borderline Findings

**R1**: 3.5 (Borderline Conference) — Soundness 3.5, Excitement 3.0
**R2**: 3.0 (Findings) — Soundness 3.5, Excitement 2.5
**Director 综合**: 3.0 (Findings)

**综合评分理由**:

Soundness 维度两位 Reviewer 一致给 3.5，这反映了论文在实验设计和统计方法论上的高水准。Logit-scale TOST inconclusive 是最大的方法论弱点，但它影响的是一个 supporting claim（bounded association），不动摇两个维度各自的主效应。

Excitement/Novelty 是关键分歧和决定性因素。论文面临三个结构性约束：
1. **Metric 新颖性为零**: SCS/BCS 与 LLM-PEE 形式相同，这是客观事实。贡献完全在 experimental framework 和 findings。对 novelty 敏感的 reviewer 会将此视为 hard constraint。
2. **Practical effect size 小**: Typical-batch confusability gap 2.2pp (CI [0.4, 4.0]) 低于多数部署场景的显著性阈值。极端 batch 的 25-31pp gap 来自刻意构造，不代表自然条件。这限制了从业者的 actionable takeaway。
3. **跨任务通用性有限**: Confusability 的 batch-level 强效应仅限于 RE classification format；NER 和 ED 实质上是 null results。"Three tasks, four datasets" 的 generality framing 虚高。

论文的正面价值——精细的实验设计、诚实的负面结果报告、centrality confound 的方法论贡献、task asymmetry 的诊断性发现——使其成为一篇高质量的分析性 Findings 论文。但上述三个结构性约束共同决定了它难以达到主会议的 novelty 和 impact bar。

**置信度**: 4/5（两位 Reviewer 均仔细审阅全文及 Appendix，统计方法论和 NLP IE 文献覆盖充分）

---

## Detailed Comments

### Abstract
- "operationalize confusability via the Schema Confusability Score (SCS)" → 需降低 metric novelty 暗示
- "up to −49pp" 为 Dimension 1 DocRED，叙事与 confusability 的关联可能误导快速阅读者
- 2.2pp typical gap 需更突出呈现
- "BCS explains 22-53%" 需附 CI

### Introduction
- Finding (1) 仍为 56 词复合句，可拆为 2-3 句
- Findings 与 Contributions 的映射不完全一一对应
- "first controlled study" 需 qualify（基本现象已有 Li et al. 2023, LLM-PEE 报告）

### §2 Related Work
- SCS novelty paragraph positioning 合理，但与 Abstract/Contribution 的 metric-centric 措辞不一致
- 缺 DLiSC, SPT 引用；缺 TOST 原始文献 (Schuirmann 1987)

### §3 Experimental Setup
- §3.2 "We define" → 需与 §2 "SCS shares its formal definition with LLM-PEE" 统一
- FewRel balanced design 是 BCS analysis 的关键优势，值得更强调
- DocRED/MAVEN 5 batches vs FewRel/Few-NERD 25 batches 的不对称需解释

### §4 Results
- §4.4: "bounded association" claim 需加限定 "under linear specification"；logit-scale 结果需提升到正文
- §4.3 practical magnitude paragraph 是论文最重要的 honest framing，应考虑前置
- §4.6 centrality confound 分析出色

### §5 SDGD
- Merge amplification 诊断清晰
- 缺 k vs false positive 率的定量关系
- Routing failure 缺代表性 error cases

### §6 Discussion
- "no confusability amplification at scale" 需加 "under linear-scale specification" 限定
- 残余因果语言（"schema-induced"）需替换为 "schema-associated"

### Conclusion
- 偏短，future work 方向可扩展
- "consistent across tested model families" 比 "fundamental property" 更准确

### Limitations
- 模范级别，8 条 + multiple comparisons 讨论
- 坦诚度远超 venue 平均

### Checklist
- 完整，A4 声明 AI 使用合理

### Format
- ✅ 正文 8 页, ACL template, review mode, anonymous
- ⚠️ 5 个 orphan bib entries 需清理
