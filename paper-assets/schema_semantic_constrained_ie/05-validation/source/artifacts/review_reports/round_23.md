---
round: 23
review_mode: fresh
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-23T08:40:20.132537+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 23 审稿报告 — OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)  
**类别**: Long Paper  
**审稿模式**: Fresh（无上轮记忆）  
**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）  
**交叉分享**: 完成（R1↔R2 逐条回应）  
**轮次**: 1 轮收敛（核心问题达成共识，无需 Round 2）

---

## Summary

本文提出 OntoCoDec，将 IE 本体编译为两层可组合 token 级解码约束：grammar layer（基于 XGrammar 的 CFG，强制 JSON 结构和词汇成员关系）和 semantic layer（有状态 logits 处理器，通过动态 entity registry 强制 domain/range 类型约束）。论文在 SciERC、DocRED、WikiEvents 上评估了 Qwen3-8B、Llama-3.1-8B、Mistral-7B 及 Llama-3.1-70B (AWQ INT4)，提供了五路消融、bootstrap CI + Cohen's d、beam search 兼容性验证等极其详尽的实验分析。LoRA 微调 + greedy S1 近乎消除 domain/range 违规（DR<0.1%），beam search (k=4) 消除所有违规类型（1.54× 延迟）。

---

## Strengths

**S1: 评估深度在 IE 领域极为罕见。** 39 页附录覆盖五路消融（Table 1）、bootstrap CI + Cohen's d（Appendix C）、fallback 因果追踪（Table 6-7）、cross-field 违规分解（Table 9）、document 长度分箱分析（Appendix H）、prompt 敏感性（Appendix I）、TCR post-hoc resolution（Appendix M）、beam search 兼容性（Appendix F）、8B FP16 vs INT4 消融（Appendix P）。统计报告采用 document-level bootstrap resampling（10,000 iterations），报告 MDE，诚实承认 n=6 不足以进行相关性统计推断。[R1-S3/S4, R2-S1 共识]

**S2: 方法形式化严密。** Proposition 1 的 pumping lemma 论证结构正确，完整证明（Appendix O）严格。约束可判定性三级分类（context-free → prefix-decidable with state → non-local）概念清晰，精准界定了 CFG 的能力边界。Grammar-first fallback（§4, eq.2）在 soundness 和 availability 之间取得了合理平衡。[R1-S1/S2, R2 acknowledges]

**S3: 诚实透明的呈现方式。** 论文明确承认 DR enforcement 引入 CF 违规、zero-shot 质量低、WikiEvents 结果是 preliminary 的。Limitations 部分极为详细，覆盖约束范围、评估覆盖度、工程局限。[R2-S2]

**S4: 实用的系统设计 + Tokenizer 无关的跨模型泛化。** 延迟开销适度（greedy +10%，beam 1.54×），编译速度快（<0.5s），可扩展性测试显示 200 实体类型/1000 关系时保持恒定 2-3% 开销。Continuation masking 在三种 tokenizer 族（byte-level BPE: Qwen/Llama, SentencePiece: Mistral）上验证有效。[R1-S6, R2-S3/S5]

**S5: Enabling dependency 是有价值的经验发现。** Grammar alone 84% DR at 8B vs semantic-only 24%（Table 1），但 70B 时 grammar alone 接近 semantic layer 的水平（§5.3）。Scale-dependent 特性对约束解码系统设计有指导价值。[R1-S5]

---

## Weaknesses

### Must Fix（阻碍接收）

**MF1 [Critical]: CF 违规占残余违规 64%，与标题 "Type-Constrained IE" 形成 gap，正文讨论严重不足。**
Table 9（Appendix）显示 S1 配置下 SciERC 245 个残余违规中 CF=155（63.9%），集中在 GENERIC↔OtherScientificTerm（34.7%）和 GENERIC↔Material（12.3%）。系统消除了 DR violations 但引入了 CF violations 作为新的 dominant 问题。正文 §4 仅一句 "Level 3 is addressed by beam search or post-hoc resolution" 带过，64% 这个关键数字仅在附录出现。Greedy 部署层成为不完整方案，用户必须在"容忍 CF"和"支付 beam 延迟"之间选择——这个 trade-off 在 Abstract/Introduction 中被低估。
**两位 Reviewer 共识**（R1-W1 Critical + R2-W2 Major）。分歧仅在标题是否需要修改（R1 建议改为 "Domain/Range-Constrained"；R2 建议界定 "type-constrained" 范围即可）。
→ 建议：(1) §5.1 或 §4 量化 CF 占残余违规比例；(2) 讨论 CF 从架构上为何难以在单 pass 解码中解决；(3) Abstract/Introduction 诚实呈现 greedy vs beam 的 trade-off。

### Should Fix（显著影响评分）

**SF1 [Major]: 算法创新有限，主要是系统集成贡献。**
Proposition 1 结论对了解 PDA 局限性的研究者来说不意外。XGrammar + stateful logits processor 的组合是自然的设计选择。κ 在 n=3 下 p=0.138 统计不显著。论文自我定位为 "systematic engineering contribution" 是诚实的，但在 EMNLP 审稿中 novelty 仍是重要维度。
**R2-W1 (Major)，R1 交叉 AGREE 但 nuance**：enabling dependency 和三级分类有独立价值，定位为 "strong engineering contribution with useful empirical insights" 在 EMNLP 可接受，但应降低理论贡献措辞强度。
→ 建议：降低 Proposition 1 和 κ 的呈现强度，突出 enabling dependency 的实证价值和系统可复用性。

**SF2 [Major]: GoLLIE 对比不公平 + 缺少与训练基方法的系统性对比。**
Appendix Q 比较 GoLLIE-7B zero-shot（R-F1=0.0, 5 predictions）vs OntoCoDec LoRA fine-tuned——evaluation setup 不匹配。§6 主文引用该结果可能误导读者。论文定位 training-based 和 decoding-time 方法为互补，但现有对比反而是 misleading 的。
**R1-W5 (Major) + R2-W4 (Minor) 共识**。R2 REBUT 指出互补定位使直接对比 methodologically difficult，但同意需说明原因。
→ 建议：(1) §6 修正 GoLLIE 引用措辞，明确标注 setup 差异；(2) 解释为何与 ADELIE/GoLLIE 的公平对比不可行（不同 schema format、不同 evaluation protocol）。

**SF3 [Major]: WikiEvents n=20 结论呈现过度自信。**
MDE=±5.0pp（Table 31），n=20 下 fine-tuning composability 结论几乎无法可靠。Introduction contribution list "validates event extraction applicability" 过度推销。
**R1-W3 (Major) + R2-W5 (Minor) 共识**。
→ 建议：(1) §5.4 大幅缩减，标题改为 "Preliminary Event Extraction Pilot"；(2) Table 4 caption 注明 "n=20, MDE=5.0pp, results are directional only"；(3) Introduction 贡献列表降低 WikiEvents 措辞。

**SF4 [Major]: 70B 实验全在 AWQ INT4 上，Abstract 未标注。**
Abstract "with 70B-class validation" 让读者以为 70B 验证是 solid 的。DocRED E-F1 drop -7.07（INT4: 84.87 vs FP16: 91.94）源于 parse failure。量化限制 caveat 出现在 §5.3 最后一段，过晚。
**R1-W4 (Major)，R2 AGREE 但降低严重性**（8B 消融已确认 INT4 不影响 DR）。
→ 建议：(1) Abstract 标注 "70B (AWQ INT4)"；(2) §5.3 开头说明量化限制。

**SF5 [Major]: Zero-shot 实验占主文 ~3 页但 R-F1 仅 4-8%，篇幅分配失衡。**
Fine-tuning composability（Table 2）仅获约 1 页篇幅，是真正有实用价值的结果。
**分歧点**：R2-W3 认为 zero-shot 缺乏实用价值应大幅压缩；R1 REBUT 认为 zero-shot 作为 diagnostic probe 有独立科学价值（消融隔离约束效果、latent violation surfacing 仅在 ZS 下可观察）。**Director 判定**：两者均有道理。保留 zero-shot 的 diagnostic 定位和 Table 1 消融，但压缩篇幅（~1 段+1 表），释放空间给 fine-tuning per-relation 分析。

### Nice to Have（不影响接收决策）

**NF1 [Minor]: Proposition 1 unbounded vs bounded 论证之间逻辑跳跃。**
Remark（§3）已区分理论不可能性和工程不可行性，但作为 Remark 不够 prominent。R1 评为 Major，R2 REBUT 评为 Minor。**Director 判定**：Minor——提升 Remark 为正式段落即可。

**NF2 [Minor]: "Empirical enabling dependency" 重复 ≥6 次。**
建议保留 3 次（Abstract、§3 定义、§5.1 引用），释放 ~0.3 页空间。[R2-W7, R1 AGREE]

**NF3 [Minor]: Fallback 频率模型依赖性（Qwen 0 vs Llama 5882）未在正文讨论。**
影响框架通用性声称。[R1-W6, R2 AGREE]

**NF4 [Minor]: Continuation masking prefix collision 频率未量化。**
建议附录增加 prefix collision 频率分析。[R1-W7, R2 AGREE]

**NF5 [Minor]: Beam k=2 中间值缺失。**
k=1 → k=4 跳跃太大，k=2 可能以更低延迟消除大部分 violations。[R2-Q3, R1 AGREE]

**NF6 [Minor]: Entity registry first-seen type 行为主文解释不清。**
CF 主要来源于 first-seen 注册机制，§3.3 应更显式 formalize。Entity-first 生成顺序是架构约束，应在 Limitations 中明确。[R2-Q4, R1-Q4 共识]

**NF7 [Minor]: Limitations 可适度精简。**
R2 认为 ~1.5 页接近 "excessive"，R1 REBUT 认为内容 substantive。**Director 判定**：有 10-15% 压缩空间，将具体数字分解移至 appendix。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成 [AGREE]：
1. CF 违规是核心未解决缺陷，正文必须量化讨论 [R1-W1 + R2-W2]
2. WikiEvents n=20 统计效力不足，不应作为可靠结论 [R1-W3 + R2-W5]
3. GoLLIE 对比不公平，训练基方法对比缺失或 misleading [R1-W5 + R2-W4]
4. 70B INT4 披露不足 [R1-W4 + R2 AGREE]
5. Enabling dependency 重复过多 [R2-W7 + R1 AGREE]
6. Fallback 模型依赖性值得正文讨论 [R1-W6 + R2 AGREE]
7. Prefix collision 未量化 [R1-W7 + R2 AGREE]
8. Beam k=2 缺失 [R2-Q3 + R1 AGREE]
9. Entity registry first-seen 行为需更清晰解释 [R2-Q4 + R1-Q4]

---

## Reviewer Divergence

| Issue | R1 | R2 | Director 判定 |
|-------|----|----|--------------|
| CF → 改标题？ | 建议改为 "Domain/Range-Constrained" | 界定范围即可，不改标题 | 不强制改标题，但 Abstract/§1 必须界定 "type-constrained" 覆盖范围 |
| Proposition 1 gap | Major | Minor (Remark 已区分) | Minor：提升 Remark prominence |
| 训练基方法对比 | Major: 需补实验 | Minor: 互补定位合理 | Should Fix：至少解释为何直接对比不可行 |
| Zero-shot 篇幅 | 有 diagnostic 价值保留 | 缺乏实用价值应压缩 | 折中：保留 Table 1 + 1 段，释放空间给 FT |
| Limitations 长度 | Substantive，不需删 | 接近 excessive | 10-15% 精简空间 |

---

## Questions（需要作者澄清）

**Q1** [R1-Q1]: Grammar-first fallback 放弃类型约束，是否考虑过 backtracking 替代策略？Latency cost 估算？

**Q2** [R2-Q1]: 约束引入的 false negatives 对 recall 的影响——被约束阻断的合法三元组（从未生成的部分）是否被量化？0.49% downstream impact 仅衡量被后验移除的部分。

**Q3** [R2-Q2]: DocRED grammar-only 增加 DR（18.46%→26.17% "latent violation surfacing"）。Fine-tuning 后是否持续？Grammar layer 在复杂 schema 下是否可能 over-constrain？

**Q4** [R1-Q3]: Ontology scalability 测试最大到 1000 entity types。Real-world KG（Wikidata 10,000+ properties）下的编译时间和 runtime overhead 估算？

**Q5** [R1-Q5]: Cohen's d 从 pooled bootstrap SD 计算，与传统 Cohen's d（样本 SD）的区别及理由？

---

## Missing References

两位 Reviewer 均认为相关工作覆盖**充分**（R2-S4 明确肯定）。非关键性建议：
- PARSE (Suri et al., 2025): LLM-driven schema optimization，与 schema compilation 相关
- GenIE (Josifoski et al., 2022): 已引用但 §6 可更详细讨论其 constraint enforcement 机制
- TANL (Paolini et al., 2021): 已引用（R2 指出 R1 遗漏检查）

---

## External Review (Stanford Agentic Reviewer)

未请求（项目未配置 external_review）。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 完成（2026-05-23 08:20–08:24 UTC）

**Findings (3 warnings, 19 info)**:
- ⚠️ Page 4-5：连续两页纯文本（Method §3.1-3.4 + §4），缺少 illustrative figure
- ⚠️ Page 8-9：连续两页纯文本（§6 + §7 + Limitations），Limitations 占满整页，内容偏多
- ⚠️ Page 39：最后一页 Appendix Q 后有 ~40% 空白
- ℹ️ 主文 8 页含 1 figure + 4 tables = 5 个 display items（密度 0.625/页，偏低端但可接受）
- ℹ️ Appendix 极其丰富（27 页，~45+ tables + 4 figures），主文/附录比约 1:3
- ℹ️ 全文无 margin 溢出、LaTeX 渲染错误、公式乱码，排版专业
- ℹ️ Table 36 色盲友好设计（shape markers + color）
- ℹ️ References 3.5 页，格式统一，无未解析引用

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

**置信度**: 4/5（两位 Reviewer 均为该领域活跃研究者，逐节验证了技术细节）

**评分理由**:

论文的工程执行和评估深度是显著优势——39 页附录、bootstrap CI + Cohen's d + MDE 报告、五路消融、三种 tokenizer 族跨模型验证，统计规范性显著优于 IE 领域平均水平。系统设计实用（+10% 延迟、<0.5s 编译、tokenizer 无关），enabling dependency 是有价值的经验发现。

阻碍 Conference (4.0) 评分的核心问题：

1. **CF gap 是根本性的**：系统将 DR violations 转化为 CF violations，后者占残余违规的 64%。"Type-Constrained IE" 标题与实际能力之间存在 gap。仅 beam search 完全解决，greedy 部署层不完整。
2. **Novelty ceiling**：核心贡献是 XGrammar + stateful logits processor 的系统集成。Proposition 1 结论对形式语言理论研究者来说不意外。在 EMNLP 审稿中 novelty 是重要维度。
3. **评估完整性存在盲区**：WikiEvents n=20 统计效力不足但结论呈现过度自信；70B 全在 INT4 上但 Abstract 未标注；GoLLIE 对比不公平。

**如果作者在 revision 中**：
(a) 在正文显著讨论 CF gap 并在 Abstract/§1 界定 "type-constrained" 范围；
(b) 修正 WikiEvents/70B 的结论 scope；
(c) 修正 GoLLIE 对比或解释为何公平对比不可行；
(d) 压缩 zero-shot 篇幅，扩展 fine-tuning 分析——
评分可提升至 **4.0 (Conference)**。当前状态介于 Conference 和 Findings 之间。

---

## Detailed Comments

### Abstract
- 信息密度高但准确。CF 分层报告（FT ≤1.4%, ZS up to 12%）较前版本有改善
- 建议标注 "70B (AWQ INT4)"
- "empirical enabling dependency" 术语可能对非专业读者不够直觉

### §1 Introduction
- Motivation 论证链完整（违规率 → 现有方法不足 → OntoCoDec）
- Contribution list 过长（两个条目各含 4-5 个子句），建议拆分为更短要点
- WikiEvents 贡献措辞需降级

### §3 Method
- 三级可判定性分类是有用的 conceptual framework
- Proposition 1 proof sketch 应更清楚标注为 informal argument
- Semantic layer 设计（§3.3）解释清晰，running example 有助理解
- Remark（有限集合）需提升 prominence

### §4 Constraint Composition
- Grammar-first fallback 有充分工程动机
- κ 在 n=3 下应明确标注 "descriptive only, not statistically significant"
- Non-rectangularity 分析可考虑移至 appendix

### §5 Experiments
- Table 1 五路消融是论文最强部分
- Zero-shot 篇幅过大，fine-tuning composability 篇幅不足
- §5.3 的 "beam (k=1) eliminates all violations" 中 k=1 就是 greedy，不算 beam search
- §5.4 WikiEvents 需标注 preliminary
- Fallback 频率模型依赖性应在正文提及

### §6 Related Work
- 覆盖充分（R2-S4 明确肯定）
- GoLLIE 引用需修正措辞

### §7 Discussion and Conclusion
- 简短恰当。Future direction（global entity-level type consensus）直接针对 CF

### Limitations
- 内容 substantive 但可精简 10-15%
- 应量化 CF gap 的 64% 数字
- Entity-first 生成顺序作为架构约束应明确说明

### Format Compliance
- ✅ 正文 8 页
- ✅ 匿名："Anonymous ACL submission"
- ✅ `\usepackage[review]{acl}`
- ✅ Limitations 在正文中
- ✅ Ethics Statement 存在
- ✅ 引用格式正确（natbib）
- ✅ 无 TODO/TBD/placeholder
- ✅ 无匿名违规