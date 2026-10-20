---
round: 14
review_mode: fresh
overall_score: 3.5 — Borderline Conference
timestamp: 2026-05-20T20:07:42.010438+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 14 审稿报告：OntoCoDec

**论文**: OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewers**: R1（方法严谨性 + 实验评估）、R2（新颖性 + 完整性 + 写作 + Related Work）
**审稿模式**: Fresh（重新审稿）

---

## Summary

OntoCoDec 提出将 IE ontology 编译为两层 token-level 解码约束：grammar layer（context-free，基于 XGrammar）保证 JSON 结构有效性和词汇准入；semantic layer（prefix-decidable with state）通过动态 entity registry 实现 domain/range type 约束，含 grammar-first fallback。核心理论贡献为三级 decidability taxonomy 和 Proposition 1（证明 domain/range 约束不是 context-free 的）。在 SciERC（551 docs）、DocRED（998 docs）、WikiEvents（246 docs）上跨 3 个 7-8B 模型评估，LoRA + greedy S1 实现 DR ≤ 0.09%、R-F1 ±0.6 pp；beam (k=4) 在 SciERC 上消除全部违规（1.54× latency）。

---

## Strengths

**S1. Decidability taxonomy 提供扎实的形式化框架。** 三级分类（context-free / prefix-decidable with state / non-local）清晰界定了不同约束类别的计算复杂度。Proposition 1 的 pumping lemma 证明正确且直接支撑两层架构的必要性。[R1, R2 共识]

**S2. 消融设计严谨，enabling dependency 论证清晰。** SciERC 五路消融和 DocRED 四路消融有效证明了各层的独立贡献：grammar-only 仅减 24% DR，semantic-only 无法保证词汇合规，二者组合才实现 94-100% DR reduction。层间双向依赖在此前文献中未被识别，是本文亮点。[R1, R2 共识]

**S3. 统计检验规范。** Bootstrap 10,000 paired significance tests 覆盖关键对比，p 值均有报告，展现负责任的统计实践。[R1]

**S4. 跨模型一致性好。** 3 models × 3 tokenizer families 的交叉验证显示约束效果在不同 tokenizer 间一致，支持 tokenizer-agnostic 声称。[R1, R2 共识]

**S5. 工程贡献实用。** 运行时开销低（+2-13%），自动从任意 IE ontology 编译约束，continuation masking tokenizer-agnostic，grammar-first fallback 保证结构完整性。[R1, R2 共识]

**S6. 复现性强。** Appendix G 提供完整超参数、prompt templates、硬件配置、随机种子。[R1, R2 共识]

**S7. 写作质量良好。** 结构清晰，术语一致（compile/interpret 分层），Figure 1 信息密度高。[R1, R2 共识]

---

## Weaknesses

### Must-Fix（全部 Reviewer 共识）

**MF1. [critical] 缺少最直接竞争方法的实验对比。** [R1-W1, R2 AGREE]
BoostCD（Sakota et al., 2025）是唯一明确将 constrained decoding 应用于 IE 的同期工作，GCD（Geng et al., 2023）是 grammar-constrained decoding for structured NLP 的直接前驱。论文在 §6 引用了这些工作但实验中未做头对头对比。当前 baselines（unconstrained vs grammar-only vs full）仅为内部消融，不能证明相对于现有 constrained decoding 方法的优势。**此问题已连续 3 轮（R12-R14）提出，仍未解决。**

**MF2. [critical] Grammar-first fallback 触发率 36.6%，type enforcement 核心声称被削弱。** [R1-W2 critical, R2 AGREE with nuance → major]
SciERC 上 36.64% 的 type-bearing positions 触发 grammar-first fallback（Table 7），意味着超过 1/3 的关键位置上 semantic layer 的 type constraints 被完全放弃。论文称"best-effort pair-based enforcement"，但正文未充分讨论这一退化的幅度和影响。**更关键的是：fine-tuned 设置下的 fallback 率未报告**——这是验证"fine-tuning 缓解 fallback"论点的关键缺失数据。R2 认为可降为 major（fine-tuning 后应改善），但因论文未提供数据支持，Director 取 critical。

### Should-Fix（全部 Reviewer 共识）

**SF1. WikiEvents 20-doc test set 统计功效极低。** [R1-W3 major, R2 AGREE]
20 文档 / 56 event types / 30 argument roles——平均每个 event type 不到 0.4 个测试文档。论文自称"preliminary"但 Contribution 列表中仍声称 EE 扩展。需报告完整置信区间和 per-document variance，或将 EE 定位为 proof-of-concept。

**SF2. κ̄ 的 predictive value 基于仅 2 个数据点。** [R1-W5 major, R2 AGREE]
κ̄ 仅在 SciERC (0.333) 和 DocRED (0.842) 上计算。Appendix D 的 Spearman ρ=-0.77 with n=6 统计功效极低。应将 κ̄ 明确定位为仅描述性指标，移除推断统计声称。

**SF3. DocRED beam search 仅 50-doc 子集。** [R1-W6 major, R2 AGREE]
Beam search 是处理 Level 3 non-local constraints 的主要策略，在 DocRED 上仅用 50/998 docs 评估代表性不足。

**SF4. 泛化性声称超出验证范围。** [R2-W2 major, R1 AGREE]
仅 3 个英语数据集、7-8B 模型（70B preliminary）。Abstract 和 §1 声称"compiles constraints automatically from any IE ontology"和"applicable to any autoregressive LM"超出验证范围。无生物医学、工业级或大规模本体评估。

**SF5. 新颖性适中。** [R2-W1 major, R1 AGREE with nuance]
Grammar layer = XGrammar 应用于 IE JSON schema；semantic layer = 带状态查找表；decidability taxonomy = 已知形式语言理论的 IE 重述。R1 认为 Proposition 1 的特定场景证明和 enabling dependency 的实验发现有超越简单组合的贡献，但整体 novelty 在 composition + formalization 层面而非组件创新。此为 reviewer 判断，非可修复 issue。

### Minor

**M1. Proposition 1 position-indexing 简化的 transfer argument。** [R1-W4 major → R2 REBUT → 降为 minor]
R2 指出 Appendix O 已讨论 position vs name referencing 的 gap。但 R1-Q3 更尖锐：有限实体集 + canonical IDs 下约束退化为 regular language，Proposition 1 不成立。论文应更明确讨论适用边界。

**M2. 70B 评估过于 preliminary。** [R1-W7, R2 AGREE]
仅 INT4 量化推理，无 LoRA fine-tuning、beam search 或消融变体。

**M3. Entity registry 顺序依赖未量化。** [R1-W8, R2 AGREE]
S1 下 entity-before-relation ordering 的保持率未报告。

**M4. Related Work 压缩过度。** [R2-W4, R1 AGREE]
正文 §6 仅约 0.6 页，关键定位论述被推至 Appendix B。8 页限制下可理解但削弱正文叙事。

**M5. 孤立 bib 条目。** [R2-W6, R1 AGREE]
chen2024agentre、fan2024fsn 为 orphan entries；formattax2026、regino2025kgcurator 无法通过 OpenAlex 验证。

---

## Reviewer Consensus [AGREE]

1. **缺少 baseline 是最大缺陷**：BoostCD/GCD 实验对比是影响接收决定的核心问题。
2. **评估范围偏窄**：3 个英语数据集、7-8B 模型不足以支撑泛化声称。
3. **WikiEvents 统计功效不足**：20-doc test set 无法支撑可靠评估。
4. **κ̄ 仅描述性**：2 个数据点不足以建立 predictive relationship。
5. **消融设计严谨**：enabling dependency 论证是本文亮点。
6. **工程质量高**：运行时开销低、tokenizer-agnostic、自动编译。
7. **写作质量良好**：结构清晰、术语一致、统计规范。
8. **TANL 应被引用**。

---

## Reviewer Divergence [REBUT]

1. **Fallback 36.6% 严重度** [R1=critical, R2=major]：R2 认为 fine-tuning 后应降低。Director 取 critical（论文未提供 fine-tuned fallback 数据）。
2. **F1 实际影响** [R1 REBUT R2-W3]：R1 认为 violation elimination 本身即 KG 构建场景的实际价值，F1 不变是"无损执行"的证据而非缺陷。Director 判定 R1 论点更有说服力——violation elimination 对 KG 质量的保障不需要通过 F1 提升来证明。**不列入 weakness。** 但建议论文补充下游应用场景讨论。
3. **Excitement** [R1=3.5, R2=3.0]：R1 更看重 decidability taxonomy 的概念迁移价值；R2 侧重组件级 novelty。合理价值判断差异。

---

## Questions for Authors

Q1. BoostCD 为何未作为 experimental baseline？如果不可直接比较，请提供详细论证和 best-effort adaptation。
Q2. Grammar-first fallback 在 fine-tuned 设置下的触发率是多少？fallback root causes 分布（tokenizer collision vs schema ambiguity vs model preference）？
Q3. 有限实体集 + canonical entity IDs 下，Proposition 1 是否仍成立？约束是否退化为 regular language？
Q4. 更 aggressive 的约束策略（backtrack/resample）能否同时降低 DR 和 CF？
Q5. "Well-calibrated" 能否被显式定义和量化？
Q6. WikiEvents 20-doc test set 上各指标的 document-level variance 和置信区间？
Q7. OntoCoDec 在显著更大规模本体上的 IE 性能如何？

---

## Missing References

1. **TANL** (Paolini et al., 2021, ICLR): "Structured Prediction as Translation between Augmented Natural Languages" — 生成式结构化预测的基础性工作。[R2 raised, R1 AGREE]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置，本轮未请求。

---

## Visual Layout Check（非评分项）

状态：**已完成**（耗时 ~4 分钟）

发现（3 warnings, 5 info）：
- **[warning]** 前 2 页纯文本无 display item，Figure 1 直到第 3 页才出现。
- **[warning]** 正文 8 页仅 1 个 figure + 5 个 table，视觉 table-heavy。建议增加 1 个结果可视化图。
- **[warning]** 第 8 页整页纯文本（Related Work + Conclusion），与前面 table 密集区形成节奏断裂。
- **[info]** Figure 1 内部分标注文字字号偏小，接近 8pt 可读下限。
- **[info]** Table 25 使用纯红/绿色标注，色盲不友好。
- **[info]** Appendix B 连续 5 页纯文本。
- **[info]** 第 6-7 页各含 2 个 table，信息密度高但无冗余。
- **[info]** Figure 4（附录）轴标签偏小，灰度打印区分度有限。

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | **3.5** |
| Excitement | 3.5 | 3.0 | **3.0** |
| Reproducibility | 4.0 | 4.0 | **4.0** |
| Overall | 3.5 | 3.5 | **3.5** |
| Confidence | 4 | 4 | **4** |

### Overall: 3.5 — Borderline Conference

两位 Reviewer 独立评估后完全一致：3.5 Borderline Conference。交叉回应后共识进一步加强。

**核心判断**：OntoCoDec 是一篇技术上扎实、工程质量高的工作。Decidability taxonomy 和 enabling dependency 是有价值的概念贡献，消融设计严谨，跨模型验证充分。但两个关键问题阻碍接收至 Conference 水平：
1. **缺少 BoostCD/GCD 等最直接竞争方法的实验对比**（连续 3 轮提出），无法证明相对优势；
2. **Grammar-first fallback 36.6% 触发率**未在正文诚实讨论，且 fine-tuned fallback 率未报告，削弱了"type-constrained"的核心声称。

评估范围（3 个英语数据集、7-8B 模型）相对泛化性声称偏窄；WikiEvents 20-doc 评估和 κ̄ 的 2 数据点进一步削弱证据说服力。新颖性在 principled composition 层面，而非组件创新。

若能补充 BoostCD/GCD 对比实验、报告 fine-tuned fallback 率、并限定泛化性声称，本文有望达到 Conference 水平（4.0）。当前版本推荐 **Borderline Conference（3.5）**，有较好的 Findings 接收前景。

---

## Detailed Comments

### §1 Introduction
- "applicable to any autoregressive LM" → 限定为 "autoregressive LMs with logits access; validated on 7-70B"
- "compiles constraints automatically from any IE ontology" → 限定为已验证的 ontology 规模
- Contribution 列表中 EE 扩展应从 "systematic evaluation" 降级为 "preliminary demonstration"

### §3 Method
- Proposition 1 适用边界（有限实体集 + canonical IDs 退化）应更明确讨论
- "Best-effort pair-based enforcement" 首次出现时给出完整 inline definition

### §4 Constraint Composition
- Grammar-first fallback 的 36.6% 触发率应在此 section 正文中讨论，而非仅在 Appendix Table 7
- κ̄ 的 Appendix D 推断统计（Spearman ρ with n=6）应移除或限定
- Fine-tuned 设置下的 fallback 率是关键缺失数据

### §5 Experiments
- 需添加 BoostCD 和/或 GCD 实验对比（must-fix）
- WikiEvents fine-tuning 结论加 "preliminary" 限定，报告置信区间
- DocRED beam search 应在完整 998-doc 集上至少报告一个模型的结果
- 70B 评估可保留但应精简以节省空间给 baseline 对比

### §6 Related Work
- 添加 TANL (Paolini et al., 2021) 引用
- 正文定位论述偏简，关键区分（preventive vs corrective, forward-only vs backtracking）应留在正文

### Bibliography
- 清理 orphan entries（chen2024agentre, fan2024fsn）
- 确认 formattax2026 和 regino2025kgcurator 的 arXiv ID

### Visual（非评分项）
- 考虑增加 1 个结果可视化图改善正文视觉节奏
- Table 25 补充非颜色视觉标记（色盲友好）