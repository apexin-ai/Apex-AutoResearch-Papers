---
round: 19
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-18T23:44:40.567097+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 19 (Fresh) 审稿报告 — gen-depth-fingerprint

**论文**: "Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains"
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026 cycle
**Deadline**: 2026-05-25 (AoE)
**Reviewer 配置**: R1（方法严谨性+实验设计）+ R2（新颖性+完整性+写作质量）
**审稿模式**: Fresh（独立初审，无上轮记忆）

---

## Summary

论文提出 generation depth classification 任务，将文本分类为 gen-0/gen-1/gen-2+（三分类而非传统二分类），并在 8 个 base model（5 个家族，0.6B-8B）构建的 37K 文本数据集上识别出 differential depth response (DDR) 三分结构：3 个 drifting features（entropy_mean, TTR, hapax_ratio, Cohen's d > 0.75）、1 个 intermediate（entropy_std, d=0.55）、3 个 near-stationary（entropy_max, tail_decay, entropy_min, d < 0.10）。7 特征 XGBoost 分类器在 LOGO 评估下 binary F1=0.694。论文明确定位为 empirical study，限制于 base model，instruction tuning 下信号显著退化。

---

## Strengths

1. **任务定义新颖且有价值** [R1-S1, R2-S4]：从 binary detection 扩展到 ordinal depth classification 是自然且有意义的推进，贡献定位清晰（"empirical rather than methodological"），避免了 overclaim。

2. **实验设计系统且控制变量意识强** [R1-S2, R2-S1]：论文最大的亮点。gen-0 seed sharing 处理、independent-seed control（F1 差距仅 1.4pp）、length-matched subsampling（长度仅贡献约 6%）、seed-level demeaning、perturbation robustness——每个潜在 confound 都有对应 control experiment。

3. **统计严谨性远超领域平均** [R1-S3, R2-S2]：DDR 三分有六个独立度量的交叉验证（ρ、Cohen's d、KS test、Levene test、TOST、CV shift），per-generator TOST 排除 pooling artifact。Bootstrap 95% CIs、McNemar tests、Bonferroni correction 规范使用。

4. **科学诚实度高** [R1-S5, R2-S3]：所有重要 limitation 均在正文讨论——base model scope、instruction tuning 退化、temperature sensitivity、negative downstream result。不过度宣传。

5. **引用体系完整** [R1-S6, R2-S6]：67 篇引用覆盖 detection、model collapse、stylometry、data provenance、ordinal classification 等子领域，含 2025-2026 年最新 concurrent work，与 Broken Telephone/Markovian Chains 的比较公正准确。

6. **写作质量良好** [R2-S7]：几乎无 AI 写作痕迹（无 em-dash、无 -ing 分词堆砌），文本流畅度高于平均投稿。格式合规：正文 ≤8 页、行号、匿名化、ACL review mode 均正确。

7. **消融分析全面** [R1-S4]：Feature ablation（group-level + LOFO + 排列重要性）、classifier sensitivity（6 种替代方法）、temperature sensitivity（4 generators × 3 temps）、prompt-type sensitivity（3 种 prompt + LOPTO）覆盖主要维度。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1 [critical] DDR 三分结构缺乏先验理论基础，存在 post-hoc 和循环论证风险** [R1-N1+N2, R2-N1, 共识]

两个交织的问题：

(a) **阈值 post-hoc 风险**：Cohen's d > 0.75 / d < 0.10 和 Spearman |ρ| > 0.60 / |ρ| < 0.10 的切分点无先验理论或经验基础。Robustness check（±0.10 不改变 grouping）仅证明稳定性，不证明三分是数据中的自然结构而非人为施加的分类。无证据表明"三分"优于"两分"或"连续谱"。

(b) **特征选择透明度不足**：论文未说明 (i) 是否存在更大初始候选特征集，(ii) 特征选择在 DDR 分析前还是后最终确定，(iii) 是否有被排除的特征因不符合三分结构而丢弃。entropy_min（LOFO ΔF1=+0.01pp）被保留的理由（"completes four-number NLL summary"）像为维持 3/1/3 对称性的 post-hoc rationalization。§3.3 L32-36 承认特征选择服务于 DDR 叙事（"so that the DDR tri-partition remains transparent"），加剧了循环论证嫌疑。

(c) **补充问题**：TTR 和 hapax_ratio 高度冗余（r=0.97），effective dimensionality ≈5，DDR 实际可能是 2/1/3 而非 3/1/3，削弱对称性。intermediate 组仅 entropy_std 一个成员。tail_decay 仅 4/8 generator 通过 TOST 等价性检验，near-stationary 标签跨 generator 不稳健。

**建议**：(a) 提供 gap statistics / silhouette analysis / clustering evidence 证明三分自然 emerge；(b) 在 held-out 数据集上预注册阈值验证 replicability；(c) 明确报告完整特征选择时间线和候选集；(d) 或将 DDR 降级为 descriptive framework，降低 novelty claim 强度。

**MF2 [critical] Base-model-only scope 从根本上限制实际影响力** [R1-N3, R2-N2, 共识]

所有 8 个 generator 均为 base models。Instruction tuning 下：
- OLMo-2-1B-Instruct LOGO F1: 0.763 → 0.338（接近随机）
- entropy_mean ρ: -0.6 → +0.48（方向反转）
- 6/7 特征方向反转——DDR 在 instruct 下不是"减弱版"而是**质性不同的现象**

实际部署的 LLM 文本几乎全部来自 instruction-tuned models。加上 downstream utility 实验为明确负面结果（depth-aware curation 不优于 random subsampling：PPL 2.387 vs 2.367，TOST 确认等价），论文面临双重困境：方法在实际场景（instruct）中不可用，即使可用也无实际用途（depth 不改善训练质量）。

**建议**：(a) 提供 2-3 个 instruct model 的系统性实验，分析 DDR 为何失效，探索 instruct 下的替代 depth signal；(b) 将论文明确定位为面向 pretraining data pipeline 的科学发现，在 Introduction 中收窄 scope；(c) 或重定位为 scientific contribution（理解递归生成本质），彻底弱化 data governance/provenance 动机。

**MF3 [critical] DDR 的新颖性为描述性而非解释性，贡献深度不足** [R2-N1, R1-N1 partial, 共识]

DDR 本质上是将 7 个特征按 depth correlation 分为三组——这是统计分类而非有理论支撑的发现。NLL mean 下降和 TTR/hapax 下降的方向在 model collapse 文献中已有文档（R1 纠正：inference-time DDR 与 training-time model collapse 机制确有区别——可逆 vs 不可逆、shape stable vs degradation——但这一区分虽有价值，analytical contribution 仍然有限）。§5 仅用一句话 gesture at "softmax architecture and fixed sampling parameters" 作为理论解释，缺乏严格论证。

论文自述 "our contributions are empirical rather than methodological"，定位诚实但也准确指出了核心弱点：作为 empirical study 缺理论深度，作为 method paper 缺实用性，identity 模糊。

**建议**：(a) 提供 DDR 的理论解释——为什么 location drift 而 shape stable？需要严格论证而非 gesture；(b) 或将 QLoRA 结果（3-class F1: 0.789→0.905, +11.6pp）提升到正文作为第三个贡献，增加论文厚度。

### Should-Fix（影响评分但不一票否决）

**SF1 [warning] Downstream utility 负面结果削弱 Introduction 的 practical motivation** [R2-W1, R1-N3 partial, 共识]
- Introduction 以 data provenance 和 training pipeline 质量为动机，但 Appendix L 明确否定"depth classification 对 data curation 有价值"的隐含承诺。负面结果被埋在附录中，正文仅一句话提及。建议在 Discussion 中显著讨论，并调整 Introduction 动机方向。

**SF2 [warning] Table 1 vs Table 2 binary F1 不一致（0.694 vs 0.705），评估协议差异解释不清** [R1-W1, R2-W2, 共识]
- 同方法两表相差 1.1pp。pooled vs macro-averaged LOGO F1 的区别对 reproduce 关键但未在 §3.4 正式定义。建议统一标注。

**SF3 [warning] Temperature sensitivity 限定不够醒目** [R1-W3, R2-W3, 部分共识]
- t=0.9 导致 9.3-26.0pp 损失，且温度敏感性是 model-dependent 的（parameter × model family 交互效应）。Abstract 中 "under standard decoding (t≤0.7)" 已存在但不够醒目。R1 认为论文措辞已足够审慎，R2 认为暗示 DDR 是 intrinsic property。建议在 Discussion 中明确区分 DDR 作为 phenomenon (parameter-dependent) 和 property (intrinsic)。

**SF4 [warning] Cross-domain 实验使用不同解码参数（t=1.0 vs t=0.7）** [R1-W4, R2 AGREE, 共识]
- 引入 confound，结果不可与主实验直接比较。Main experiment t=0.9 崩溃但 cross-domain t=1.0 表现良好（F1>0.73），存在内在矛盾。建议在 t=0.7 下重复或明确标注不可比性。

**SF5 [warning] Paraphrastic chain F1=0.671 在正文引用但附录无完整支撑** [R2-W4, R1 AGREE, 共识]
- §4.2 L88 报告数字但 Appendix C 不含 paraphrastic chains 的方法和结果。建议补充或删除引用。

**SF6 [warning] "Entropy" 术语指代 per-token NLL，与 Shannon entropy 混淆** [R1-W6, R2-W5, 共识]
- 全文 feature 命名和讨论使用 "entropy" 但实际是 NLL。对统计分析为核心的论文，术语精确性重要。建议改用 NLL 命名或更突出标注区分。

**SF7 [warning] Generator subset 不一致（5/6/8-gen），缺集中说明** [R1-M2, R2-W2, 共识]
- LOGO 用 8-gen，cross-model 用 5-gen，QLoRA 用 6-gen。缺集中说明三种子集的原因和可比性。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下核心问题上完全一致（独立给出后交叉确认）：

| # | 议题 | R1 | R2 | 交叉结果 |
|---|------|----|----|----------|
| 1 | DDR 三分缺理论基础 / post-hoc 风险 | N1 | N1 | 双向 AGREE |
| 2 | 特征选择不透明 / 循环论证 | N2 | AGREE 补充 | R2 补充证据 |
| 3 | Base-model-only 限制影响力 | N3 | N2 | 双向 AGREE |
| 4 | Downstream negative result 与动机矛盾 | N3(b) | W1 | 双向 AGREE |
| 5 | Table 1/2 metrics 不一致 | W1 | W2 | 双向 AGREE |
| 6 | TTR/hapax 冗余膨胀 DDR | W2 | AGREE 补充 | R2 补充证据 |
| 7 | Temperature 限制需更醒目标注 | W3 | W3 | AGREE（程度有差异）|
| 8 | Cross-domain 参数 confound | W4 | AGREE | R2 补充矛盾分析 |
| 9 | Entropy 术语混用 | W6 | W5 | 双向 AGREE |
| 10 | Paraphrastic chain 缺支撑 | AGREE | W4 | R1 确认 |
| 11 | Generator subset 不一致 | M2 | W2 | 双向 AGREE |
| 12 | 论文 identity 模糊（empirical vs method） | AGREE | Framing 评估 | R1 确认 |

---

## Reviewer Divergence [REBUT]

**分歧 1：贡献数量是否 Must-Fix**
- R2-N3 认为仅 2 条贡献对 8+16 页论文不足，建议将 QLoRA 提升为第三贡献或改投 short paper
- R1 REBUT：(a) 正文仅 6 页非 8 页；(b) QLoRA 有方法论限制（within-model affinity 风险、仅 6-gen 评估）；(c) 贡献数量非评判标准，深度和可靠性才是。真正问题是 DDR 论证不够严谨和应用价值有限
- **Director 判断**：R1 的反驳有理，此问题降级为 Should-Fix 建议而非 Must-Fix

**分歧 2：DDR 是 parameter-dependent 还是 intrinsic**
- R2-W3 认为温度敏感性暗示 DDR 是参数依赖现象而非内在属性
- R1 REBUT：论文已用 "under fixed sampling parameters" 限定，t=0.7 是标准解码温度，温度敏感性是边界条件非否定 DDR
- **Director 判断**：R1 正确指出论文措辞已较审慎，但 R2 的关切（DDR 是 parameter × model family 交互效应）有数据支持。两者都有道理——论文应更明确区分 phenomenon vs property。

**分歧 3：TOST 阈值选择**
- R1-W5 认为 ε=|d|<0.20 缺 application-specific 论证
- R2 partial REBUT：ε=0.20 是 Cohen (1988)/Lakens (2017) 惯例值，方法论可接受
- 但两位均同意 tail_decay 仅 4/8 generator 通过是实质问题
- **Director 判断**：阈值本身可辩护，tail_decay 不一致性是 DDR partition 的局部缺陷

---

## Questions for Authors

1. 7 个特征是否从更大候选集选出？初始集大小、淘汰标准、选择在 DDR 分析前/后？
2. DDR 三分能否通过无监督方法（clustering on depth-sensitivity metrics）自动 emerge？
3. Cross-model chains 的提升（0.764 vs 0.734 LOGO）来自 protocol difference 还是 generator mixing 本身？
4. Instruction-tuned models 的 "anti-DDR" 模式（ρ 反转）是否有独立分析价值？
5. 如何解释 main experiment t=0.9 崩溃但 cross-domain t=1.0 表现良好的矛盾？

---

## Missing References

两位 Reviewer 均确认引用体系基本完整（67 篇覆盖全面）。以下为非必须建议补充：
- Synthetic data contamination detection 工作（FineWeb/Dolma filtering 之外的专门文献）
- MTLD/HD-D 在 LLM detection 中的应用讨论
- Image domain 的 iterative generation parallel work（如 StableRep）

---

## External Review

未配置。

---

## Overall Assessment

**Overall Score: 3.0 / 5 — Findings（可被 Findings 接收）**

**ARR 维度评分（两位 Reviewer 共识）：**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5/5 |
| Excitement | 2.5 | 2.5 | 2.5/5 |
| Reproducibility | 4.0 | 4.0 | 4.0/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**一句话总结**：论文提出了有价值的任务定义（generation depth classification）和有趣的 empirical finding（DDR 三分结构），实验设计和统计实践远超该领域平均水平，但三个根本性问题限制了主会议接收：(1) DDR 核心贡献缺乏理论深度和先验验证，更像 descriptive taxonomy；(2) base-model-only scope 严重制约实际影响力；(3) downstream utility 的负面结果弱化了论文的 practical motivation。两位 Reviewer 独立给出 3.0 / 5（Findings），Confidence 4/5，核心问题高度一致。

**接收建议**：Findings 水平。论文的实验质量和科学诚实度值得认可，但贡献深度（描述性非解释性）和影响范围（仅 base model）不足以支撑主会议长论文。

---

## Detailed Comments（逐节）

### Abstract
- 四个必答问题（问题、重要性、方法、结果）均已覆盖
- "under standard decoding (t≤0.7)" 限定条件存在但不够醒目
- 最后一句声明 base-model scope，但两位 Reviewer 认为应更早/更醒目
- F1=0.694 无置信区间（Table 1 有 CI [.688, .700]）

### Introduction
- 动机从 dynamical system 切入，逻辑连贯
- "empirical rather than methodological" 定位清晰诚实
- 贡献列表仅 2 条，对长论文偏薄（R1 认为可接受，R2 认为不足）
- Data provenance/governance 动机与 downstream negative result 存在张力

### Related Work
- 与 Broken Telephone / Markovian Chains 的比较清晰准确
- DDR vs model collapse 区分有效（inference-time reversible vs training-time irreversible）
- 引用覆盖全面

### Method
- Task formulation 清晰
- 特征选择动机叙述存在与 DDR 的循环论证嫌疑
- entropy 术语需修正
- Generator subset 差异需集中说明

### Results
- LOGO 评估设计严谨
- Table 1/2 metrics 不一致需解决
- DDR 阈值论证需加强
- TTR/hapax 冗余需讨论

### Discussion
- Temperature sensitivity 和 instruct degradation 正确讨论
- 需更显著讨论 downstream negative result
- DDR vs model collapse 区分 adequate
- 需明确区分 DDR 作为 phenomenon vs property

### Appendix
- 20+ 节过多，建议合并到 10-12 个核心节
- QLoRA 结果（+11.6pp）值得在正文简要提及
- Paraphrastic chain 实验缺完整支撑
- Cross-domain 参数 confound 需标注
- p.24 有排版残留

### Format Compliance
- ✅ ACL template [review] mode
- ✅ 正文 ≤8 页
- ✅ 行号、匿名化
- ✅ Limitations section（详尽）
- ✅ Ethics statement
- ⚠️ Responsible NLP Checklist 未在论文中可见（可能在 OpenReview 单独提交）