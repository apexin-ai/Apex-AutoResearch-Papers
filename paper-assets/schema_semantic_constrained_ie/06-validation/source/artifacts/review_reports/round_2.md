---
round: 2
overall_score: weak reject
timestamp: 2026-05-15T08:41:16.454299+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — OntoCoDec: Type-Valid Information Extraction via Compiled Ontology Constraints

**目标 Venue**: EMNLP 2026 (ARR May 2026)
**审稿轮次**: Round 1（初审）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计，R2: 新颖性+Related Work+写作）
**交叉回应共识度**: R1 对 R2 意见 13/14 AGREE；R2 对 R1 意见 10/14 AGREE + 3 AGREE with nuance

---

## Summary

本文提出 OntoCoDec，一个两层约束解码框架：grammar 层（XGrammar CFG）保证 JSON 结构和词汇合法性，semantic 层通过有状态 entity registry + 动态 logit masking 强制 domain/range 约束。在 SciERC (7 relations) 和 DocRED (96 relations) 上用 Qwen3-8B 和 Llama-3.1-8B 零样本验证，DR 违规减少 45–99%，R-F1 中性或显著提升。论文还提出 constraint tightness 概念和 tightness×RV 双因子机制解释跨数据集和跨模型差异。

---

## Strengths

**S1. 首次系统量化 LLM-based IE 的本体约束违反。** [R1/R2 共识] 四类违规分类（DR/RV/ET/CF）清晰，Phase 0 分析揭示违规普遍性（SciERC 15.37%, DocRED 18.46%），诊断性贡献本身有价值。

**S2. Constraint tightness 假说有实质洞察力。** [R1/R2 共识] tightness×baseline RV 双因子机制定量解释 SciERC vs DocRED 差异及 Qwen vs Llama 非对称表现（同一 ontology τ̄=0.842 上 Qwen 10.21% vs Llama 2.55% 残余 DR），超越单纯经验报告。R1 认为双因子交互的定量化超越简单直觉。

**S3. 两层架构的 enabling dependency 验证清晰。** [R1/R2 共识] 五路消融展示 semantic-only DR 仅降 24%，grammar 层添加后跃升至 94%——"prerequisite structure" 论证令人信服。

**S4. 统计方法论扎实。** [R1/R2 共识] Bootstrap 95% CI + p-values (10,000 iterations)，跨模型复制，non-significant 结果诚实报告。

**S5. Related Work 全面且定位精确。** [R1/R2 共识] §6 + Appendix A 覆盖六大范式，与 code gen type-constrained decoding 对比细致，主动引用负面结果（CRANE/Schall/Tam）并论证 IE 特殊性。

**S6. 诚实的负面结果报告。** [R1/R2 共识] CF trade-off、post-hoc F1 优势、Llama SciERC 微降等不利结果均被主动报告。

**S7. Grammar layer "揭露"隐藏违规的发现有洞察力。** [R2] DocRED grammar-only DR 从 18.46% 升至 26.17%（Table 3），OOV 关系被纠正后暴露潜在类型不兼容。

---

## Weaknesses

### Must-Fix（4 项，均为两位 Reviewer 共识）

**W1. CF violation 爆炸性恶化是方法设计缺陷，非简单 trade-off。** [R1 W1 = R2 W2, 共识]
- SciERC: 0.08% → 9.90%；Llama DocRED: 0.17% → 12.02%（高于某些 baseline DR 率）
- 根因：当 D[h] ∉ dom(r) 时，semantic layer 放弃注册类型、强制选择 dom(r) 中的类型，主动制造 CF violation
- Entity registry 已追踪类型——可在 D[h] ∉ dom(r) 时保留注册类型并放弃 DR 约束（registry-consistent fallback），但此替代方案未被探索甚至未被讨论
- §7 将 CF 定性为 "qualitatively different" 可能被视为淡化问题；下游 KG 构建需要全局实体类型一致性
- Llama DocRED 的 DR↓23.52pp vs CF↑11.85pp，综合改善仅 ~11.67pp
- **要求**：增加 registry-consistent fallback 消融；提供 DR↓ vs CF↑ 综合指标；在 Limitations 中更突出 CF 为主要局限

**W2. §2 与 §3 的本体形式化存在根本性不一致。** [R2 W1 = R1 W6, 共识]
- §2 定义 σ: R → P(E × E)（pair-based），§3 改用 dom, range: R → 2^E（independent）——两者在一般情况下不等价
- 若 σ(r) = {(Person, Person), (Org, Org)}，independent check 会错误放行 (Person, Org)
- 评估用 pair-based 定义（§5.1），但执行用 independent dom/range——评估/执行错位
- Tightness 公式基于 pair 计数 |σ(r)|/|E|² 但实际执行比 pair-based 更宽松
- **要求**：明确 SciERC/DocRED 约束是否 rectangular（σ(r) = dom(r) × range(r)）；统一全文符号；如非 rectangular 则量化 over-permissiveness

**W3. Post-hoc filtering 在 F1 上优于 OntoCoDec。** [R1 W2, R2 agree with nuance]
- Appendix B: Post-hoc SciERC R-F1=8.63 vs OntoCoDec 8.36；DocRED 9.61 vs 8.23
- F1 综合了 P/R，post-hoc 整体更优
- 论文声称 "preventing violations rather than discarding" 避免 compute 浪费，但无 runtime 数据支撑
- Post-hoc 还保留了 ET=2.47%，而 OntoCoDec ET=0%——但这不改变 F1 劣势
- **要求**：报告 wall-clock time 对比；展示 recall trade-off curve；讨论 OntoCoDec + post-hoc 组合方案

**W4. DocRED baseline 数据表间不一致。** [R1 W3, R2 交叉确认]
- Table 1（§5.1 violation landscape）: DR=18.7%, RV=28.9%, ET=7.5%
- Table 3（§5.2 DocRED ablation）: DR=18.46%, RV=29.66%, ET=2.48%
- ET 差 3 倍（7.5% vs 2.48%），RV 也不同（28.9% vs 29.66%）
- exp_id 不同（phase0 vs phase2）暗示不同实验配置，但论文未作任何解释
- Abstract 与 §5.1 的 DR 数据也不一致（18.46% vs 18.70%）
- **要求**：统一数据或明确解释差异来源

### Should-Fix（5 项）

**W5. 仅零样本评估，无法验证可组合性声明。** [R2 W3 ≈ R1 W4/W8, 共识]
- R-F1 ≈ 8% 距 SOTA ~50% 差距巨大
- 论文声称与 GoLLIE 等 fine-tuned 方法可组合，但无任何实验验证
- "F1 as control variable" 论证部分合理但存在循环论证风险
- **建议**：至少在一个设置上用 fine-tuned 模型验证

**W6. 完全缺失 latency/throughput 分析。** [R1 W5, R2 同意]
- Decoding-time 方法的 runtime overhead 是核心实用性指标
- **建议**：报告 tokens/sec 和 wall-clock time

**W7. 标题 "Type-Valid" 误导。** [R1 W7, R2 同意]
- DocRED 残余 DR=10.21% + CF=12.02%，远非 "valid"
- **建议**：改为 "Type-Constrained" 或类似更准确措辞

**W8. 新颖性声明过宽。** [R2 W4, R1 同意]
- §1 Contribution #2 "the first to extend grammar-constrained decoding with semantic ontology constraints" 可被误解为领域无关首创
- Code gen 已有成熟先例（Synchromesh 2022, PICARD 2021, MGD 2023, PLDI 2025）
- §6 讨论实际很到位但 §1 表述需缩窄
- **建议**：改为 "the first to automatically compile IE ontology domain/range constraints into token-level semantic masks"

**W9. Single-token type assumption 限制可扩展性。** [R2 W5 = R1 W12, 共识]
- §3.3.2 将每个 τ ∈ E 映射到 first subword token，仅验证 6 types + Qwen tokenizer
- Llama tokenizer 验证未报告
- 更大本体可能不满足 first-token 唯一性
- **建议**：验证 Llama；讨论 multi-token masking 可行性

### Minor（5 项）

**W10.** Prompt 模板未提供，影响 reproducibility。[R1 W10, R2 同意]
**W11.** DocRED 使用 dev set 未说明理由。[R1 W11, R2 同意]
**W12.** S1 vs S2 缺计算成本归一化。[R1 W9, R2 同意]
**W13.** Abstract 首句 "produce" 过于绝对（建议 "can produce"）；§3.3.2 "6 types each" 指代不清。[R2 W8, R1 同意]
**W14.** Bib 中 rastogi2020sgd 为 orphan entry。[R1 W14, R2 partially agree]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识 [AGREE]：

1. **CF 恶化是方法设计缺陷**（W1）——registry-consistent fallback 是可行替代方案但未被探索
2. **§2/§3 形式化不一致**（W2）——pair-based vs independent 定义不等价，评估/执行错位
3. **Post-hoc filtering F1 优于 OntoCoDec**（W3）——需 runtime 对比支撑论点
4. **Table 数据不一致**（W4）——ET 差 3 倍，无解释
5. **缺 latency 分析**（W6）
6. **缺 fine-tuned 实验**（W5）
7. **新颖性声明过宽**（W8）
8. **Single-token assumption**（W9）

## Reviewer Divergence

仅有两处轻微分歧，已在交叉回应中解决：

1. **R2-W7 (Tightness 直觉性)**：R1 [REBUT]——双因子交互的定量化（Spearman ρ=0.069 等）有超越简单直觉的贡献。R2 接受此论点但维持 "systematic empirical observation" 定性。→ 不影响评分。

2. **R1-W13 (Grammar-only DR 增加应进 abstract)**：R2 [REBUT]——Abstract 应聚焦 full system 结果，grammar-only DR 增加是 DocRED 特有现象。→ 不影响评分。

---

## Questions（需要作者澄清）

**Q1. [Critical]** SciERC/DocRED 的约束结构是否 rectangular（σ(r) = dom(r) × range(r)）？如不是，independent enforcement 的 over-permissiveness 有多大？[R1/R2 共识最关键问题]

**Q2.** 残余 DR 中，grammar-first fallback 导致 vs dom/range 独立性导致的比例？

**Q3.** 当 D[h] ∉ dom(r) 时，为什么 override 注册类型而非保留注册类型并放弃 DR 约束？

**Q4.** Table 1 vs Table 3 DocRED baseline 数据不一致的原因？

**Q5.** OntoCoDec vs post-hoc filtering 的 wall-clock time？

**Q6.** Entity type 首 subword 唯一性是否对 Llama tokenizer 验证？

**Q7.** CF 冲突的 245 个实体中，60 个归因于 Generic↔OST 歧义，其余 185 个的分布？

**Q8.** OntoCoDec 因约束重定向概率质量而引入的 false positives 有多少？

---

## Missing References

两位 Reviewer 均认为 Related Work 覆盖已相当全面。建议性补充（非严重遗漏）：
- SuRE (Kim et al., ACL 2024) — schema-based structured generation for RE
- Constrained beam search for KGC (KG-BERT + type constraints)

---

## External Review (Stanford Agentic Reviewer)

外部审稿未启用。

---

## Overall Assessment

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 2.5/5 | 3.0/5 → 2.5-3.0（交叉后下调） | **2.5/5** |
| Excitement | 2.5/5 | 3.0/5 | **2.75/5** |
| Overall | 2.5/5 | 3.0/5 | **2.75/5** |
| Reproducibility | 2/5 | 4/5 → 3/5（交叉后下调） | **2.5/5** |
| Confidence | 4/5 | 4/5 | **4/5** |

**总评：Weak Reject**

论文方向正确，tightness 分析和 enabling dependency 验证有真实的方法论贡献，实验设计系统且统计方法论扎实。但存在四个 Must-Fix 问题：

1. CF violation 爆炸（0.08%→9.90%/12.02%）是未解决的方法缺陷，非简单 trade-off
2. §2/§3 形式化不一致（pair vs independent），评估/执行错位
3. Post-hoc filtering F1 优于提出方法，缺 runtime 对比
4. DocRED baseline 表间数据不一致（ET 差 3 倍），无解释

这些问题中，W1 和 W2 涉及方法论层面（需要额外实验和形式化修正），W3 和 W4 涉及论证完整性（需补充数据和解释）。当前版本的证据不足以支撑论文的核心声明。

**修改建议优先级**：
1. [最高] W1 CF fallback 消融 + W2 形式化统一 → 修复方法论缺陷
2. [高] W4 表间数据统一 + W3 runtime 对比 → 修复论证完整性
3. [中] W5 fine-tuned 实验 + W6 latency 分析 → 增强说服力
4. [低] W7-W14 写作和格式修正

修复 W1-W4 后可达 Findings 水准；追加 W5-W6 可增强主会议竞争力。

---

## Detailed Comments（逐节）

### Abstract
- "produce systematic ontology constraint violations" → "can produce"（R2 W8）
- DR 数据引用需与正文统一（18.46% vs 18.70%）

### §1 Introduction
- Contribution #2 新颖性声明需缩窄（R2 W4）

### §2 Background
- σ: R → P(E × E) 定义需与 §3 统一（R2 W1）
- Tightness 定义需与 §4 公式统一符号

### §3 Method
- §3.5.3 fallback 策略需讨论 registry-consistent 替代方案（R1 W1）
- §3.3.2 "DocRED (6 types each)" 指代不清（R2 W8）
- §3.3.2 single-token assumption 需讨论 scalability（R2 W5）

### §4 Constraint Composition
- Tightness 公式符号需与 §2 统一

### §5 Experiments
- Table 1 vs Table 3 数据不一致需解决（R1 W3）
- DocRED 用 dev set 需说明理由（R1 W11）
- 缺 runtime/latency 数据（R1 W5）
- S1 vs S2 缺计算成本归一化（R1 W9）

### §6 Related Work
- 覆盖全面，仅建议性补充（SuRE 等）

### §7 Discussion and Conclusion
- CF 讨论需加强，不应仅定性为 "qualitatively different"
- Post-hoc filtering 对比需补充 runtime

### Limitations
- 需更突出 CF 为主要局限
- 需提及 single-token assumption

### Appendix
- Post-hoc filtering 对比需补充 runtime 和 recall curve
- 建议增加 prompt 模板