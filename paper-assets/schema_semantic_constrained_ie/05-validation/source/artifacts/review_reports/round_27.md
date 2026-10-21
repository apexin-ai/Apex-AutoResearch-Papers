---
round: 27
review_mode: fresh
overall_score: 3.5 — Borderline Conference
timestamp: 2026-05-25T22:02:34.961694+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 27 审稿报告 — OntoCoDec: Compiled Schema Constraints for Structured IE

**Venue**: EMNLP 2026 (ARR)  
**审稿模式**: Fresh（重新审稿）  
**Reviewer 编排**: 2 人（R1 方法严谨性+实验设计 / R2 新颖性+framing+完整性）  
**轮次**: 1 轮初审 + 交叉分享 → 收敛

---

## Summary

论文提出 OntoCoDec，一个两层约束解码框架（Grammar layer via XGrammar + Semantic layer via dynamic logit masking），将 IE schema 约束编译为 token-level masks，在生成时 enforce domain/range type constraints。Proposition 1 通过 pumping lemma 证明 domain/range 约束超出 CFG 表达能力，为两层设计提供原则性动机。在 SciERC（7 relations）和 DocRED（96 relations）上验证，zero-shot DR 违规减少 94%+，fine-tuning 后 DR→0%，F1 中性或微升。附带 WikiEvents 事件抽取初步验证和 70B 规模实验。

---

## Strengths

**S1. 形式化分析扎实**  
Proposition 1 通过 pumping lemma 严谨证明 domain/range 约束超出 context-free 表达能力。Appendix O 覆盖 position-based 和 name-based 两种情况。此前未有 IE type constraint 非 context-free 的形式化证明，为两层架构提供不可替代的理论动机。[R1 AGREE, R2 AGREE]

**S2. 实验深度罕见**  
39 页、49 个表格、8 张图。五路消融（Table 1）、跨模型验证（3 model families × 3 datasets）、微调 composability（Table 2）、beam search 分析、fallback causal tracing（Table 4）、CF-DR trade-off 分析（Table 5）、prompt sensitivity（Table 34）、document length 分析、量化鲁棒性（Appendix R）、nucleus sampling 鲁棒性、order invariance（Appendix N）、lucky violation 分析（Table 39）、ontology scalability（Table 40）。[R1 highlight, R2 highlight]

**S3. 统计方法规范**  
Bonferroni 校正 bootstrap CIs（10,000 iterations，document-level resampling）、Cohen's d 效应量、跨种子确定性验证（Table 29）、200-doc 子集功效分析。在 NLP 论文中显著高于平均水平。[R1 5/5 Reproducibility, R2 5/5 Reproducibility]

**S4. Non-additive layer interaction**  
Grammar-only 3% DR reduction + Semantic-only 24% → Combined 94%。这一超加性效应的定量刻画（含 fallback causal tracing）是有洞察力的实证发现，展示 grammar 层作为 semantic 层 enabling prerequisite 的机制。[R1 acknowledge, R2 acknowledge]

**S5. 诚实的 limitation 分析**  
CF-DR trade-off、residual error breakdown、fallback 机制量化、lucky violation 分析均透明展示系统真实边界。[R1 highlight]

**S6. 实用部署考量**  
无需 constraint-specific training，可组合任何有 logits 接口的 autoregressive LM。三级部署方案（greedy S1 / beam k=2 / beam k=4），runtime overhead 2-3%。[R1 highlight, R2 acknowledge]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. "Ontology-Compiled" framing 与 RE 实验约束来源不一致** [R27-N1]  
- Abstract 承诺 "compiles constraints automatically from IE ontologies"，系统名 "OntoCoDec = Ontology-Compiled Decoding"
- 但 SciERC/DocRED 的约束实际从训练数据共现统计提取（§5 lines 419-423），非形式化本体编译
- 仅 WikiEvents 使用了真正的 KAIROS ontology
- Appendix C 显示 33% residual DR 来自 schema coverage gaps——频率统计遗漏的长尾 valid type pairs
- 这不仅是表述问题：理论框架（Proposition 1）基于"给定完备 ontology"假设，但 RE 实验使用不完备的统计近似
- **Reviewer 共识**: R2 升级为 must-fix（方法论诚信），R1 认同问题存在但降级为 should-fix。Director 裁决 must-fix。
- **建议**: (1) Abstract "from IE ontologies" → "from IE schema specifications or training-set statistics"；(2) §3 或 §5 明确讨论两条路径（完备 ontology vs 经验性统计）的 completeness 差异；(3) 说明 "Onto" 指 ontology-style constraints 而非要求完备本体输入

**MF2. WikiEvents 证据不足以支撑"Structured IE"标题声称** [R27-N2]  
- 标题 "Information Extraction" 暗示对 IE 的广泛覆盖，abstract 将 EE 列为三个验证轴之一
- 但 WikiEvents ZS n=246、FT n=20。unconstrained baseline EV+RoV 违规 >85%，使约束有效性 trivially observable
- n=20 下 F1 影响无法可靠评估
- 注：R26-W2 已修复 §7 表述（"2 RE datasets + preliminary pilot"），但标题/abstract 仍过宽
- **Reviewer 共识**: R1 critical, R2 agree-with-nuance。Director 裁决 must-fix，但修改 framing 即可解决，无需扩大实验。
- **建议**: (1) 标题考虑限定为 "Relation Extraction" 或添加限定语；(2) Abstract 不将 EE 与 RE 并列为同等验证轴，明确为 "preliminary pilot"

### Should-Fix（影响评分但不一票否决）

**SF1. 缺乏与现有语义约束 IE 系统的直接对比** [R27-W1]  
- 仅与 grammar-only baselines（GCD/BoostedCD/vLLM guided_json）和自身消融对比
- 缺少与 EnriCo（ASP 约束）、SPIRES/OntoGPT（post-hoc validation）的 head-to-head
- Appendix S 以 "incompatible evaluation settings" 回避，但 post-hoc validation 可在相同 unconstrained 输出上运行
- Table 12 的 post-hoc filtering 实现过于简单（直接删除违规 triple），不代表 post-hoc 方法最优表现
- **Reviewer 分歧**: R1 critical, R2 降级 should-fix（跨领域复现非 trivial）。Director 裁决 should-fix (elevated)。
- **建议**: Appendix S 增加定性对比表（约束类型、运行时开销、是否需重训练、completeness guarantee），明确 post-hoc vs decoding-time trade-off

**SF2. Figure 3 线性拟合 n=4 统计效力不足** [R27-W2]  
- R²=0.886, p=0.058（不显著于 α=0.05），仅 4 个数据点
- 虽标注 "descriptive only"，但 Figure 3 在正文 §4 位置突出，给读者过强的因果暗示
- **Reviewer 共识**: 两位完全一致 [AGREE]
- **建议**: Caption 明确标注 n=4 和 p>0.05；或移至附录

**SF3. 70B 验证仅一个模型（Llama-3.1-70B AWQ INT4）** [R27-W3]  
- Scale-dependent interaction 是核心发现之一（Contribution 3），但 70B 仅单一模型+量化
- 8B 层面验证 3 个家族，70B 仅 1 个，scale 效应泛化性未经检验
- INT4 量化可能与 constrained decoding mask 机制有非平凡交互
- **Reviewer 共识**: 两位一致。属资源限制下的合理选择，需明确声明。
- **建议**: Limitations 明确声明；可选补充 Qwen-72B 或非量化验证

**SF4. 核心新颖性偏工程导向** [R27-W4]  
- Grammar layer = XGrammar 直接应用，Semantic layer = constrained beam search + type-based filtering 的自然延伸，组合方式（bitwise AND）为标准做法
- Proposition 1 的 pumping lemma 证明思路在 PL theory 中是标准技术
- **Reviewer 分歧**: R2 Excitement 2.5/5, R1 Excitement 3/5。R1 认为 non-additive interaction 和 Proposition 1 对 IE 领域有独立价值。
- **建议**: 贡献定位更明确为"系统贡献+实证发现"；强化 Proposition 1 在 IE 约束解码社区的意义论述

**SF5. CF violations 主文讨论不足** [R27-W5]  
- 附录有 5+ 页详细分析（Tables 4/5/7/8, Appendix C/M），但主文 Limitations 仅一句
- **Reviewer 分歧**: R2 raised, R1 rebutted（附录充分）。Director 判断：增加主文 forward pointer。
- **建议**: §3.3 或 Limitations 增加 1-2 句 CF failure mode 讨论 + forward pointer

**SF6. Entity registry first-seen 语义的系统性偏差** [R27-W6]  
- Table 8: 58.1% CF violations 来自 hallucinated entity，first-seen lock 传播错误类型
- Fine-tuning 后 cascade errors 完全消除（0/22），但 zero-shot 下是系统性问题
- Appendix C 有详细分析但主文不足
- **建议**: §3.3 增加 failure mode 风险说明

**SF7. S2 70B R-F1 退化分析分散** [R27-W7]  
- S2 70B R-F1 36.28 vs S1 44.53（-8.25pp），原因分析分散在 §4、§5.1、Appendix F
- Appendix F 数据已回答是 over-constraining 而非 entity extraction 退化，但读者需跨多处才能拼凑
- **Reviewer 分歧**: R1 raised, R2 rebutted（分析存在但分散）。
- **建议**: §5.1 增加 1-2 句直接归因总结

### Minor（不影响接收）

**M1.** 评估覆盖范围有限——缺乏非英语语言、超大规模 schema（>1000 relations）、小模型（<8B）评估 [R27-M1]  
**M2.** 200-doc DocRED 子集的 relation type coverage 代表性未讨论 [R27-M2]  
**M3.** Beam search wall-clock latency scaling 未报告（Table 40 仅覆盖 greedy） [R27-M3]  
**M4.** κ(r) 公式中 |E|² 应写为 |E × E| 避免符号混淆 [R2]  
**M5.** S1/S2 命名不直观，建议改为 "joint" / "pipeline" [R2]  
**M6.** Figure 5 x 轴 relation 标签角度使部分名称难辨认 [R2]  
**M7.** Figure 2 "Additive prediction (27%)" 虚线对比度不足 [R1]  
**M8.** 正文缩写密度高（DR, CF, RV, ET, OOV, BPE），建议表格标题展开关键缩写 [R2]

---

## Reviewer Consensus（两位 AGREE）

1. **Figure 3 统计效力不足**（n=4, p=0.058）——正文位置过突出
2. **70B 验证范围有限**——单一模型+量化，scale 结论泛化性受限
3. **约束来源 framing 需修正**——从训练数据提取 ≠ 从形式化 ontology 编译
4. **WikiEvents 证据不足以支撑标题级别 claim**
5. **新颖性偏工程导向**——系统贡献而非算法创新
6. **实验深度和统计规范性极高**（Reproducibility 均 5/5）
7. **Proposition 1 证明正确**，为两层设计提供原则性动机

## Reviewer Divergence（存在 REBUT）

| Issue | R1 | R2 | Director 裁决 |
|-------|----|----|--------------|
| Ontology framing 严重性 | should-fix | **must-fix** | must-fix |
| Head-to-head baselines | **critical** | should-fix | should-fix (elevated) |
| CF 讨论是否充分 | 充分（附录 5+ 页） | 不充分（主文不够） | 增加 forward pointer |
| S2 70B 分析 | 分析不足 | 分析存在但分散 | 集中归因 |
| Excitement | 3/5 | 2.5/5 | — |

---

## Questions to Authors

1. **RE 约束忠实性**: 从训练数据提取的 type constraints 与"真正的"ontology constraints 的一致性如何量化？是否有 ground truth 对比？
2. **First-seen 替代方案**: 是否考虑过 soft/probabilistic entity registry（如 weighted type distribution masking）？
3. **CF 下游影响**: DR→CF 转换被描述为 "severity downgrade"——是否有定量的下游任务评估支持？
4. **大规模 schema**: Wikidata-scale（~10K+ relations）下编译和运行时表现？Entity registry 查询复杂度是否成为瓶颈？
5. **Post-hoc comparison**: 是否可在相同 unconstrained 输出上运行 SPIRES 的 validate-then-correct 流程作为对比？

---

## Missing References

Related work 覆盖极为全面（主文 2 页 + 附录 4+ 页），未发现重大遗漏。供参考：
- Josifoski et al. (2023) "Language Model Decoding as Direct Metrics Optimization" — 约束解码与度量优化的关系
- 若能与 SPIRES/OntoGPT 做定性对比，应正式引用 Caufield et al. (2024)

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求。本轮未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 已完成（2026-05-25 21:16 → 21:20, ~4 分钟）

| 严重性 | 位置 | 发现 |
|--------|------|------|
| ⚠️ warning | Page 1-2 | 连续 2 页纯文本无 display item，首个视觉锚点（Figure 1）到 page 3 才出现。实证贡献为主的论文建议在 page 1-2 加 teaser figure |
| ℹ️ info | Page 7 | Figure 5 x 轴 relation type 标签旋转后字号偏小（约正文 60-70%） |
| ℹ️ info | Page 5 | Figure 2/3 红绿色组合对 deuteranopia 色盲有风险，建议改用 blue+orange |
| ℹ️ info | Page 12-16 | Appendix B+C 连续 5 页纯文本，附录可接受但密度极高 |
| ℹ️ info | Page 39 | 末页内容约 80%，AI 辅助声明列表简短，整体可接受 |

---

## Overall Assessment

**评分**: 3.5 — Borderline Conference  
**置信度**: 4/5（两位 Reviewer 均熟悉约束解码和结构化 IE 领域）

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 4/5 | 4/5 | 4/5 |
| Excitement | 3/5 | 2.5/5 | 2.75/5 |
| Reproducibility | 5/5 | 5/5 | 5/5 |
| Overall | 3.5 | 3.5 | **3.5** |

**综合判断**:

论文执行质量达到主会议水准——形式化分析正确、实验深度罕见、统计方法规范、附录极其详尽。两个 Must-Fix 问题（ontology framing 偏差 + WikiEvents 泛化 overclaim）均可通过 framing 调整解决，不需要新实验。

主要隐忧是**新颖性**：核心技术是已有组件的工程整合（XGrammar + logit masking + bitwise AND），non-additive interaction 和 Proposition 1 提供了一定的学术增量，但不足以构成强 novelty。Excitement 综合 2.75/5 在 ARR 中偏低。

**定位建议**: 修复两个 Must-Fix 后，论文更适合 Findings 接收（Overall 3.0-3.5 区间）。若要冲主会议（4.0），需要：(1) 至少一个 head-to-head baseline 对比显示显著优势；(2) 更强的 novelty 论证（如 non-additive interaction 的理论解释而非仅实证观察）。

---

## Detailed Comments

### §1 Introduction
- "three distinct IE tasks" (line 075-076) 过宽——实际仅深入验证 RE，EE 为 pilot
- Contribution list 准确反映了系统+实证贡献定位

### §3 Method
- Proposition 1 证明正确，position-based + name-based 两种情况均有覆盖
- §3.3 Entity registry 的 first-seen 语义缺少 failure mode 警告
- S1/S2 命名不直观

### §4 Constraint Tightness Analysis
- Figure 3 线性拟合应弱化展示（n=4, p>0.05）
- κ(r) 公式 |E|² 符号可优化

### §5 Experiments
- 消融设计严谨（五路），统计方法规范
- §5 应更明确标注 SciERC/DocRED 约束来源（训练数据 vs 本体）
- §5.1 70B 讨论应集中归因 S2 退化原因
- §5.3 WikiEvents 内部 hedging 到位（"preliminary pilot"），但标题/abstract 不匹配

### §6 Related Work
- 覆盖极为全面
- 缺少与 post-hoc validation 系统的系统性对比论述

### §7 Conclusion
- R26-W2 修复后表述已改善（"2 RE datasets + preliminary pilot"）
- 仍需与标题/abstract 对齐

### Appendix
- 质量极高，覆盖了几乎所有可能的 reviewer 疑问
- Appendix S (Related Methods Comparison) 应强化为定性对比表