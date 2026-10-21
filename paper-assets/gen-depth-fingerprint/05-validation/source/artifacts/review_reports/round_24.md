---
round: 24
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T04:22:19.568512+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 24 审稿报告 — gen-depth-fingerprint

**论文**: Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains
**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计推断；R2: 新颖性+完整性+写作质量+格式合规）
**轮次**: Round 1 + 交叉分享（1 轮收敛）
**外部审稿**: 未配置

---

## Summary

本文提出 generation depth classification 任务——将文本分类为 gen-0（人类）/ gen-1（首次生成）/ gen-2+（递归生成），取代传统二分类检测。通过 7 个手工特征（5 个参考模型 NLL 统计量 + 2 个表面词汇多样性特征）和 XGBoost 分类器，在 8 个 base model generator（Pythia/OLMo/Qwen/Llama/Mistral，0.6B–8B）上实现 LOGO binary F1=0.694。核心发现是 differential depth response (DDR)：特征分为 drifting（entropy mean, TTR, hapax ratio）、intermediate（entropy std）和 near-stationary（entropy max, tail decay, entropy min）三组，与递归生成下 NLL location shift / shape stability 的解释一致。论文诚实地将贡献定位为 "empirical rather than methodological"。

---

## Strengths

**S1. 新颖且有实际意义的任务定义。** [R1,R2 共识] 从 binary real-vs-synthetic 推进到 ordinal depth classification 是有意义的方向扩展，与 model collapse 和数据溯源有清晰关联。这是一个之前未被正式定义的研究问题。

**S2. 评估协议严谨且透明。** [R1,R2 共识] LOGO + LOFO 双重评估，配套 independent-seed、length matching、cross-domain、cross-temperature、prompt type sensitivity 等多项控制实验。覆盖度在 EMNLP 投稿中属上乘。

**S3. 诚实的学术态度。** [R1,R2 共识] 论文主动标注 gen-0 seed sharing 问题、下游 n=3 局限、QLoRA 天花板与手工特征的 tradeoff。Limitations section 详尽（34 行，8+ 项局限）。

**S4. 可解释的方法设计。** [R1,R2 共识] 7 个手工特征完全透明可分析，DDR 框架为理解递归生成下文本属性的演化提供了有用的概念结构。

**S5. 附录覆盖全面。** [R1,R2 共识] 20+ 页附录涵盖 16 个实验板块，覆盖了几乎所有可预见的审稿问题。

**S6. 与 concurrent work 定位清晰。** [R2] 对 Broken Telephone 和 Markovian Chains 的区分有说服力，三个独立工作收敛于 ~3 class ceiling 的讨论增强了可信度。

---

## Weaknesses

### Critical

**N1. Base model 限制严重削弱论文 significance。** [R2 Critical, R1 Major]
- OLMo-2-1B-Instruct LOGO F1 从 0.763 暴跌至 0.338；Llama 3-class F1 从 0.742 降至 0.544
- 现实 web text 几乎全部由 instruct/RLHF 模型生成，base model 直接生成的文本在实际场景中极为罕见
- 论文将此框架为设计选择（"We restrict to base models, since instruction-tuning introduces confounds"），但实质是核心限制
- R1 认为对于 foundational study 此范围界定合理，R2 认为这严重削弱 impact
- **Director 判定**: Major-Critical。论文标题已含 "Base LLM"，scope 透明；但缺少 concrete deployment scenario 论证 base-model study 的独立实际价值

**N2. DDR tri-partition 阈值缺乏 principled 依据。** [R1 Critical, R2 同意降为 Major]
- Cohen's d 阈值 0.75 介于惯例 medium (0.5) 和 large (0.8) 之间，未说明选择理由
- 敏感性分析仅覆盖 near-stationary boundary，未检验 drifting boundary
- 若阈值降至 0.5，entropy_std (d=0.55) 将从 intermediate 重分类为 drifting，改变 DDR 叙事
- R2 指出 data-driven clustering (silhouette=0.632) 和 9.5× gap 提供了独立验证
- **Director 判定**: Major。data-driven 验证降低了风险，但阈值选择仍需 justification

**N3. 下游效用实验 n=3 seeds 严重 underpowered。** [R1 Critical, R2 初标 Minor 后同意升级]
- n=3 时 TOST power 极低，论文自承 Cohen's d "unreliable"
- Discussion §5 L17 仍做定性结论（"depth composition does not determine training utility"），该声明无法由 n=3 支撑
- 虽已从 contribution list 移除，但 Discussion 中的结论措辞需降格为 "preliminary evidence"

### Major

**W1. 三个 drifting 特征本质是同一 latent factor。** [R1,R2 强烈共识]
- entropy mean、TTR、hapax ratio 相关性 r=0.81-0.97，PCA 92.3% by PC1
- DDR 3/1/3 在独立信息维度上更接近 1/1/3
- 论文自承 permutation importance 差异反映 feature masking 而非独立信号
- "7-feature ensemble" / "three drifting features" 的表述可能误导读者关于独立信息维度数量

**W2. DDR 作为 EMNLP 核心贡献偏薄。** [R1,R2 共识]
- 核心发现是 "some features are more sensitive to recursive generation than others" 的系统化表述
- 自承 "post-hoc and empirical"，无理论解释，缺乏 predictive power
- 作为 Findings 贡献合适，不够 main conference
- 需要更严谨的 mechanistic explanation 或形式化分析来增强深度

**W3. Contribution #3 (parameter dependence) 本质是 negative result。** [R1,R2 共识]
- 将 "方法在某些条件下失效"（instruction tuning, t=0.9）列为贡献逻辑不自洽
- R1 指出温度 boundary condition 有操作价值
- 建议 reframe 为 Discussion 中的 "boundary conditions"

**W4. Independent-seed 控制覆盖率不足。** [R1,R2 共识]
- 仅 2/8 generators (Pythia-2.8B, OLMo-2-1B)，覆盖 2/5 家族
- F1 差距可忽略 (0.680 vs 0.694)，但 Qwen/Llama/Mistral 未验证

### Minor

**M1. LOGO 同家族泄漏未在 Table 1 体现。** [R1 Major, R2 降级] LOFO 0.686 vs LOGO 0.694，差 0.8pp。建议 Table 1 增加 LOFO 行。

**M2. Abstract 数字过多。** [R1,R2 共识] 7+ 个具体数值，建议精简至 2-3 个。

**M3. Related Work 缺少 ordinal classification in NLP 讨论。** [R1,R2 共识] 论文将 task 框架为 ordinal classification 但 Related Work 无对应子章节。

**M4. Pooled Cohen's d 异方差问题仅在附录讨论。** [R1,R2 共识] 正文需添加 caveat。

**M5. 未探索 n-gram/句法特征，缺少相关引用。** [R1,R2 共识]

---

## Reviewer Consensus [AGREE]

1. **Overall 3.0 (Findings)**: 两位 Reviewer 独立给出相同评分
2. **任务定义新颖 + 实验严谨 → 达到 Findings 门槛**
3. **DDR 贡献偏 empirical + base-model 限制 + 性能偏低 → 不够 Conference**
4. **Contribution #3 定位不当**: 需 reframe
5. **三个 drifting 特征高度冗余**: 3/1/3 叙事需调整
6. **下游 n=3 underpowered**: 结论措辞需降格
7. **附录覆盖和学术诚实度为论文最突出优点**

## Reviewer Divergence [REBUT]

1. **Base model 限制严重程度**: R2=Critical（实际场景失效）vs R1=Major（foundational study 合理范围）。Director 判定 Major-Critical：scope 透明但需补充 deployment scenario 论证。

2. **F1=0.694 是否偏低**: R2=Major（QLoRA 0.905 说明远非最优）vs R1=REBUT（指标不可比：8-gen binary LOGO vs 6-gen 3-class QLoRA；LOGO 是极严格评估；QLoRA 高 F1 恰恰支持 depth signal 存在）。Director 判定：R1 论据更有力——R2 的对比存在指标和评估集不匹配问题。F1=0.694 在 LOGO 下对 foundational study 可接受。

3. **R1-W2 参考模型 confound**: R1 声称 cross-reference F1 降至 ~0.613。R2 核查发现 R1 数据引用错误（0.613 来自 Appendix H perturbation experiment，非 cross-reference；实际 spread=0.013）。**R1 未在交叉回应中反驳此点。Director 判定：R1-W2 dismissed**，参考模型 confound 不构成实质问题。

4. **下游 n=3 严重程度**: R1=Critical vs R2=Minor。R1 在交叉回应中成功说服 R2 升级。Director 判定：论文已将 downstream 从 contribution list 移除，降为 Major-Critical——需修改 Discussion 措辞但不再影响核心评分。

---

## Questions for Authors

**Q1.** [R2, R1 同意] 请具体描述 base-model depth profiling 的实际部署场景。在什么现实应用中需要判断文本经历了多少代 base model 递归生成？

**Q2.** [R1] 若将 drifting 阈值从 0.75 降至 0.5，DDR 的三分叙事如何变化？请提供 drifting boundary 的完整敏感性分析。

**Q3.** [R2] QLoRA 端到端模型在 instruct model 上的表现如何？它是否能部分克服 base model 限制？

**Q4.** [R1] 三个 drifting 特征替换为其第一主成分后，分类性能是否变化？这能直接检验它们是否携带独立信息。

**Q5.** [R2] Cross-model chains F1=0.764 高于 LOGO 0.694——depth signal 在 generator 混合时反而更强？R1 指出评估协议差异（5-fold CV vs LOGO）可能解释部分 gap。

---

## Missing References

- **Ordinal classification in NLP**: 缺少 ordinal classification 在 NLP 任务中的应用文献（如 sentiment ordinal approaches） [R1,R2 共识]
- **N-gram based detection methods**: 论文特征集不含 n-gram 特征，需引用相关方法 contextualize 特征选择 [R1,R2 共识]
- **Distribution shift 文献**: DDR 本质是 distribution shift 现象，可引用经典框架（covariate shift, dataset shift）[R2, R1 部分同意]

---

## Overall Assessment

**Overall: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 4/5 | 3.5/5 |
| Excitement | 3.5/5 | 2.5/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Clarity | — | 4/5 | 4/5 |

**ARR 评分**: 3.0 = Findings（可被 Findings 接收）

**综合评价**: 论文定义了一个新颖且有意义的任务（generation depth classification），以高标准的实验设计和学术诚实度支撑了一个有趣的 empirical 发现（DDR tri-partition）。评估协议（LOGO/LOFO + 多项控制实验）和附录覆盖度远超平均水平。然而，三个核心问题制约了评分：(1) base-model-only 限制使得方法在实际场景（instruct models）中性能严重退化，significance 受限；(2) DDR 作为纯 empirical 贡献缺乏理论深度和 predictive power，三个 drifting 特征本质是同一 latent factor，3/1/3 叙事有误导性；(3) 部分声明的统计基础不够稳固（DDR 阈值选择、下游 n=3）。整体达到 Findings 水准——新颖任务定义 + 严谨实验 + 诚实报告构成 solid 但 non-exciting 的贡献。修复阈值敏感性分析、调整 drifting 特征叙事、补充 base-model deployment scenario 后有潜力升至 3.5 (Borderline Conference)。

---

## Detailed Comments（按章节）

### Abstract
- 数字过密（7+ 个具体数值），建议精简至 F1=0.694 和一个核心效应量描述
- "instruction tuning" 限制的提及方式得当

### Introduction
- Contribution #3 需 reframe：将 parameter dependence 从 "贡献" 改为 Discussion 中的 boundary conditions
- 叙事聚焦 model collapse / scientific characterization 方向正确

### Related Work
- 缺少 ordinal classification in NLP 子章节
- 与 concurrent works 的区分清晰有效
- 需补充 n-gram detection methods 和 distribution shift 文献

### Method
- 特征选择动机清晰，两组特征（reference-model + surface）的互补性论证充分
- 需在 §3.3 简要说明为何排除 n-gram/句法特征

### Results
- Table 1 建议增加 LOFO binary F1 行
- §4.2 DDR 部分需补充 drifting boundary 敏感性分析
- §4.2 需在正文添加 pooled Cohen's d 异方差 caveat
- 三个 drifting 特征的叙事需调整为 "single latent diversity/entropy factor"

### Discussion
- §5 L17 下游结论需降格为 "preliminary evidence suggests..."
- DDR 的 post-hoc / empirical 定位诚实但限制了贡献深度

### Limitations
- 详尽全面，是论文最佳章节之一
- 所有关键限制均已覆盖

### Format
- 正文 8 页，符合 ARR Long Paper 要求
- 模板 `\usepackage[review]{acl}` 正确
- 匿名化到位
- Figure 1 x 轴标签字体可能低于 7pt（需检查）