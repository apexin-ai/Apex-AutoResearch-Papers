---
round: 9
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-19T07:25:23.662429+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 9 (Fresh Review)

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Ontology Constraints
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: Fresh（重新审稿，无上轮记忆）
**Reviewer 编排**: 2 人（R1: 方法/实验/可复现性; R2: 新颖性/写作/相关工作/格式）
**轮次**: 1 轮收敛（交叉回应后无重大分歧）

---

## Summary

本文提出 OntoCoDec，将 IE ontology schema 编译为两层可组合的 token-level 解码约束：grammar layer (XGrammar) 保证 JSON 结构合法性，semantic layer 通过有状态实体注册表执行 per-triple domain/range 类型约束。在 SciERC、DocRED（RE）和 WikiEvents（EE）上评估，覆盖 4 个模型（Qwen3-8B/Llama-3.1-8B/Mistral-7B/Qwen2.5-72B）、zero-shot 和 LoRA fine-tuning 两种 regime。核心结果：fine-tuning 下 DR ≤ 0.20%、R-F1 ±0.6pp；zero-shot 下 DR 降低 42-99%，但引入 CF 副作用（zero-shot 下 9-21%），total violation burden 仅降约 30%。

---

## Strengths

**S1. 问题定义清晰，violation taxonomy 系统化。** [R1, R2 共识] §2 对 IE ontology 的形式化定义和四类 violation（DR/RV/ET/CF）的分类干净有用。Constraint tightness 作为预测 violation 难度的指标有独立分析价值。

**S2. 两层组合架构设计合理，enabling dependency 洞察有价值。** [R1] Table 1 ablation 清楚展示 semantic-only 仅降低 24% DR，grammar+semantic 组合降低 94%。Sequential masking 对 non-rectangular type signatures 的必要性分析严谨（独立检查会多放 33-37% spurious pairs）。

**S3. 实验覆盖面广。** [R1, R2 共识] 3 数据集 × 4 模型 × 2 regime × 3 解码策略 × prompt 变体 × 文档长度分层 + full FT + scalability benchmark。附录覆盖大部分可预见审稿质疑。

**S4. Fine-tuning composability 有部署实际价值。** [R1, R2 共识] LoRA+S1 在 4 个 model×dataset 设置下 DR ≤ 0.20%、R-F1 ±0.6pp。Beam search 进一步消除所有四类 violation（SciERC, calibrated models）。

**S5. 跨 tokenizer 通用设计。** [R2] Continuation masking 在三个 tokenizer family 上验证，工程通用性好。

**S6. 工程开销低。** [R1] +2-13% inference overhead、sub-second compilation、constant overhead up to 1,000 relations 使方法实际可部署。

**S7. 诚实讨论局限。** [R1, R2 共识] CF trade-off 分析（fallback ablation, Spearman ρ=-0.77, Pareto 分析）和 Mistral boundary condition 的处理在同类论文中较为坦诚。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1 [critical, R1+R2 共识] CF trade-off 与 "near-lossless composability" claim 不一致，headline number 具误导性。**
- Abstract "near-lossless composability" 仅以 DR 和 R-F1 衡量，忽略 CF 从 0.08%→9.90%（SciERC ZS）乃至 12.02%（Llama DocRED）、21.1%（Qwen WikiEvents）
- SciERC total violation burden (DR+CF) 从 15.45% 降至 10.83%，降幅仅 ~30%，与 "94% DR reduction" 的 headline 形成强烈反差
- Appendix B CF fallback ablation 证实 CF↔DR 为结构性 trade-off（消除 CF → DR +13.85pp），非可修复 bug
- Fine-tuning 将 CF 降至 ≤1.18%，此时 "near-lossless" 勉强成立，但 Abstract 未区分两种 regime
- **建议**：(1) 限定 "near-lossless" 仅 fine-tuned regime；(2) Abstract 报告 total violation burden (DR+CF)；(3) 明确 ZS 下 CF 严重，方法实际价值主要在 FT 组合场景

**MF2 [critical, R1+R2 共识] Constraint table 来源于训练数据共现，非形式本体，与标题/framing 不符。**
- 标题 "Compiled Ontology Constraints" 但 SciERC/DocRED 约束表从训练集共现统计提取
- 33% 残留 DR 源于 "schema coverage gaps"（Appendix B residual analysis）
- Constraint table 覆盖率（training type pairs vs test type pairs）未报告
- 仅 WikiEvents 使用真正形式本体（KAIROS），但结果 "preliminary"（20 docs）
- **建议**：(1) 标题或 Introduction 区分 "formal ontology"（WikiEvents）vs "empirical type-pair constraints"（SciERC/DocRED）；(2) 报告覆盖率；(3) 分析 constraint table completeness 对效果的敏感性

**MF3 [critical, R1+R2 共识] WikiEvents EE 评估过于初步但在 Abstract/Contributions 中权重过高。**
- 仅 20-document test set（数据集约束非设计选择），trigger F1 -5.4pp，bootstrap CI 极宽
- 论文自称 "preliminary" 但 Abstract 和 Contribution 3 将 EE 与 RE 并列呈现，无充分 hedging
- **建议**：Abstract/Contribution 中为 EE 结果增加 "preliminary" 限定，降低 EE 在 contribution list 中的权重

### Should-Fix（影响评分但不一票否决）

**SF1 [warning, R1 主导, R2 部分同意] 缺少关键 baseline 实验对比。**
- GCD 通过 grammar-only 行隐式对比但未显式标注
- GoLLIE、EnriCo 缺少 fine-tuned 场景对比（或需明确说明不可比原因）
- Post-hoc filtering 在 5/6 zero-shot settings 下 F1 更高（Appendix B Table 11），但此关键数据仅在附录
- **建议**：grammar-only 行标注为 GCD-equivalent；main text 纳入 post-hoc 对比数据

**SF2 [warning, R1+R2 共识] 多个关键实验样本量不足，统计可信度存疑。**
- Dual-factor: n=4, p≈0.058, 但主文构建围绕此 pattern 的叙事
- DocRED sampling: 114/998 docs
- WikiEvents FT: 20 docs（数据集限制）
- Beam DocRED: 50 docs, Clopper-Pearson 95% CI upper bound 5.8%
- **建议**：dual-factor 增加 "descriptive"/"tentative" 限定；小样本实验标注 CI 和 hedging

**SF3 [warning, R1 主导, R2 部分同意] Zero-shot 叙事占比过高（~60% of §5），FT composability 应为主角。**
- ZS R-F1 仅 2-8%，实用价值有限；violation rate 变化可能由 prediction distribution 偏移驱动
- FT composability 有部署价值但篇幅不足
- **建议**：重新平衡叙事，FT composability 为 primary，ZS 为 stress-test

**SF4 [warning, R1+R2 共识] Mistral "boundary condition" 定义不充分。**
- ET>5% 排除准则为 post-hoc，无理论依据
- Mistral 排除在 dual-factor 但纳入 cross-model claims (42-99% range)，存在一致性问题
- **建议**：将 entity typing quality 列为方法前提假设，讨论部署前检查方法

**SF5 [warning, R1+R2 共识] Introduction 以 KG/pipeline violation propagation 为动机，但无任何下游评估。**
- CF 对下游影响完全未评估
- **建议**：pilot downstream evaluation 或调整动机为 intrinsic type correctness

**SF6 [warning, R1+R2 共识] §6 Related Work 过于压缩（12 行，1 段）。**
- **建议**：扩展为 2-3 段，分覆盖 grammar-constrained decoding、schema-aware IE、post-hoc validation

**SF7 [warning, R1+R2 共识] Abstract 数据密度过高（~15 数字, 7 缩写 in 201 词）。**
- **建议**：减至 ~4 关键数字，移除 beam/WikiEvents 细节

**SF8 [warning, R1+R2 共识] Contribution 3 信息过载（5+ 独立 claim 压在一条）。**
- **建议**：拆分为 RE/EE composability + robustness/generalization

**SF9 [warning, R1+R2 共识] §7 Discussion and Conclusion 过短（~80 words）。**
- **建议**：增加 findings 综合解读、CF 前瞻、适用范围总结

---

## Reviewer Consensus

以下问题两位 Reviewer 独立评估后在交叉回应中达成共识 [AGREE]：

1. **CF trade-off 是论文最大的方法论问题**（R1-W2 = R2-N1）
2. **WikiEvents preliminary 与 contribution 权重不匹配**（R1-W4 part = R2-N2）
3. **Dual-factor 统计不足**（R1-W4 = R2-W4）
4. **Constraint table framing 与 "ontology" 标题不符**（R1-W1, R2 交叉 AGREE）
5. **Related Work 压缩**（R2-W1, R1 AGREE）
6. **Abstract 数据密度过高**（R2-W2, R1 AGREE）
7. **Conclusion 过短**（R2-W6, R1 AGREE）
8. **Overall 评分 3.0 (Findings)**：双方一致

---

## Reviewer Divergence

交叉回应中有 3 处分歧，均已解决或降级：

1. **R2-N3 Responsible NLP Checklist 缺失**：R1 [REBUT]，认为 checklist 在 OpenReview 系统单独提交而非嵌入 PDF。降为 administrative reminder，不列入 Must-Fix。
2. **R2-W5 DocRED grammar-only DR 增加解释不充分**：R1 [REBUT]，论文解释技术正确（evaluable triples 分母变化），但应补充绝对数量。降为 Minor presentation issue。
3. **R1-M4 源码残留内部路径注释**：R2 [REBUT]，LaTeX 注释在 PDF 中不可见，camera-ready 清理即可。降为 camera-ready housekeeping。

---

## Questions（需要作者澄清）

**Q1.** [R1+R2] Constraint table 对 test set 的覆盖率（observed/possible type pairs）？Unseen-but-valid type pairs 是否被错误计为 DR violation？

**Q2.** [R1+R2] CF↔DR Pareto 前沿是否意味着 per-slot greedy enforcement 框架内无法同时降低两者？（R1 交叉回应指出 beam search 可绕过此 trade-off）

**Q3.** [R1] Post-hoc filtering 在 5/6 ZS settings 下 F1 更高、FT 下基本持平。OntoCoDec 相对 post-hoc 的实际优势在哪？是否存在 reject rate 使 post-hoc 不可用的 real-world scenario？

**Q4.** [R1] Beam search (k=4) 在 FT SciERC 消除所有 violation。1.54× latency overhead 在离线 batch IE 中可接受——为何不设为默认推荐？

**Q5.** [R2] Qwen LoRA DR=0% vs Llama LoRA DR=0.09%：在如此低的绝对数量下（~0-2 triples out of ~2000）差异是否统计显著？"DR=0%" 作为 headline 是否过强？

**Q6.** [R1] Sequential masking 的固定字段顺序是否限制 prompt template 灵活性？如需改变生成顺序，约束如何处理？

**Q7.** [R2] Beam search + LoRA 消除所有 violation 的结论在 DocRED 上是否成立？（论文仅报告 SciERC FT beam 结果）

---

## Missing References

两位 Reviewer 独立识别的遗漏引用（按共识度排序）：

1. **InstructUIE** (Wang et al., 2023) — [R1+R2 共识]
2. **DeepStruct** (Wang et al., 2022) — [R1+R2 共识]
3. **UniversalNER** (Zhou et al., 2024) — [R2]
4. **USM** (Lou et al., 2023) — [R1]
5. **Wadhwa et al. (2023)** "Revisiting Relation Extraction in the era of LLMs" — [R2]
6. **BioREx** (Luo et al., 2022) — [R2, lower priority, no biomedical domain in eval]

---

## External Review (Stanford Agentic Reviewer)

**状态**：未配置。项目 config 中 `external_review.paperreview_ai.enabled` 未设置。

---

## Overall Assessment

**Overall: 3.0 (Findings)**
**Confidence: 4/5**（两位 Reviewer 均 4/5，高度一致）

**评分标准 (EMNLP 2026 ARR)**：3 = Findings（可被 Findings 接收）

### 评分理由

**积极面**：问题定义清晰且有实际意义（S1）；两层可组合约束架构在 constrained decoding for IE 中有新意（S2）；实验覆盖面在同类论文中属上乘（S3）；fine-tuning composability 有真实部署价值——DR ≤ 0.20%, R-F1 ±0.6pp（S4）；跨 tokenizer 通用且开销低（S5, S6）；局限讨论诚实（S7）。

**阻止 Conference 推荐的因素**：
1. **Framing integrity** (MF1+MF2)：论文的两个核心术语——"near-lossless" 和 "ontology"——与实际结果/实现不匹配。CF 副作用使 ZS 下 total violation 仅降 30%（非 headline 暗示的 94%）；constraint table 来自训练数据共现而非形式本体。这不是写作问题，而是 claim 与 evidence 的结构性 gap。
2. **CF 无解决路径** (MF1)：CF↔DR 是结构性 trade-off（ablation 证实），且论文未提出可行的解决方向（majority voting 实验为 negative, Appendix）。方法在 ZS 下的实际收益有限。
3. **关键 baseline 缺失** (SF1)：无法判断 OntoCoDec 相对 GoLLIE/EnriCo/GCD 的真实增量。Post-hoc filtering 在多数 ZS settings 下 F1 更高的事实仅在附录呈现。

**Findings 推荐理由**：尽管存在上述问题，论文的技术贡献（两层组合约束、violation taxonomy、enabling dependency 分析）和实验深度（覆盖面、ablation、failure mode 分析）对 IE 社区有参考价值。Fine-tuning composability 结果有实用意义。CF trade-off 的诚实讨论本身也是有价值的 negative finding。Findings 是合适的推荐。

---

## Detailed Comments（逐节，合并两位 Reviewer 意见）

### §1 Introduction
- 叙事结构清晰：violation 问题 → 现有不足 → OntoCoDec → contributions [R1]
- Contribution 3 过密，应拆分 [R1+R2]
- "training-free" framing 与实际需 FT 控制 CF 有张力 [R1]
- 每条 Contribution 有对应 section 支撑 [R2]

### §2 Background
- 清晰简洁，形式化定义和 violation taxonomy 有独立价值 [R1]
- Constraint tightness 在 §4 重复定义，浪费空间 [R2]

### §3 Method
- 技术描述充分：entity registry、position detection、continuation masking [R1]
- 缺少 failure mode 分析：position detection failure 如何 gracefully degrade？[R1]
- Logit -∞ numerical stability 未讨论 [R1]

### §4 Constraint Composition
- Non-rectangularity 分析说服力强（0/7 SciERC, 23/96 DocRED 是 rectangular）[R1]
- Constraint tightness 分母 $|\mathcal{E}|^2$ 假设 type pair 等概率，实际分布不均 [R1]
- Dual-factor pattern 统计不足（n=4, p≈0.058）但叙事权重过高 [R1+R2]

### §5 Experiments
- §5.1 SciERC ablation 是论文最扎实部分 [R1]
- §5.2 DocRED grammar-only DR 增加需补充绝对数量 [R1+R2 交叉共识]
- §5.3 Cross-model: Mistral 差距极大，"boundary condition" 标签不充分 [R1+R2]
- §5.4 WikiEvents: CF 15-21% ZS 下实际不可用 [R1]
- §5.5 Runtime: 数据充分，overhead 合理 [R1]
- 整体叙事 ZS 过重，FT 应为主角 [R1+R2]

### §6 Related Work
- 主文仅 1 段 12 行，严重压缩 [R1+R2]
- 需扩展为 2-3 段，增加与 GCD/GoLLIE 的显式定位 [R1+R2]
- InstructUIE, DeepStruct, UniversalNER, USM 缺失 [R1+R2]

### §7 Discussion and Conclusion
- 过短（~80 words），缺综合解读、CF 前瞻、适用范围 [R1+R2]

### Limitations
- 内容详尽诚实，覆盖 CF scope、evaluation coverage、engineering considerations [R1]
- 已有 3 个 \paragraph 子节，结构合理
- WikiEvents 20-doc 是数据集约束已说明，但 need larger EE benchmark 的责任不免除 [R1]

### Ethics Statement
- 存在且覆盖数据、subjects、code release [R2]

### Appendix
- 覆盖面优秀（12 个附录）[R1]
- Case studies（Appendix K）特别有用 [R1]
- 附录间存在部分信息重复（CF-DR trade-off 多处讨论）[R1]

### Format
- ✅ ACL review 模板正确
- ✅ 匿名化完整
- ✅ 主体 8 页
- ✅ Limitations + Ethics 存在
- ⚠️ Bib: 8 orphan entries, 1 duplicate key, 3 unverified citations [R2]
- ⚠️ Responsible NLP Research Checklist: 论文 PDF 中未见（通常 OpenReview 系统单独提交）[R2 raised, R1 降级为 admin reminder]