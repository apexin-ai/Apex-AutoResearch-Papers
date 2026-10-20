---
round: 26
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-23T12:56:09.113530+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 26 审稿报告（Fresh Review）
## OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints

**Venue**: EMNLP 2026 (ARR May cycle) | **Deadline**: 2026-05-25 | **Reviewers**: 2 | **Rounds**: 1（交叉分享后共识充分，无需第二轮）

---

## Summary

论文提出 OntoCoDec，一个将 IE 本体约束编译为 token-level 解码约束的框架。核心观察是 domain/range 类型约束超越 context-free 表达能力（Proposition 1），因此采用两层架构：grammar 层（基于 XGrammar）保证 JSON 结构和词汇合法性，semantic 层通过运行时 entity registry 和 dynamic logit masking 执行类型约束。在 SciERC（551 docs）、DocRED（998 docs）和 WikiEvents（n=20 pilot）上评估，涵盖 3 个 8B 级模型和 1 个 70B 模型（Llama-3.1-70B AWQ INT4），zero-shot 和 LoRA fine-tuning 两种设置。

---

## Strengths

**S1. 系统性的约束编译框架。** 将 IE 本体约束编译为可组合的解码层的想法在 IE 领域是新颖的。两层架构的设计有理论支撑（Proposition 1），将 context-free 可处理的约束与需要运行时状态的约束清晰分离。框架 model-agnostic，与 fine-tuning 正交可组合。[R1-S1, R2-S6]

**S2. 极其充分的实验和统计方法。** 40 页论文含 48+ 表格、5-way ablation、4-way fine-tuning ablation、beam search 兼容性、prompt sensitivity、文档长度分析等。统计方法规范：Bootstrap CIs（10,000 iterations）、Bonferroni correction（α_adj=0.0125）、Cohen's d effect sizes、统计 power analysis。可复现性文档详尽（Appendix G）。这一评估覆盖面在同类工作中罕见。[R1-S2/S3/S5, R2-S2]

**S3. DR→CF trade-off 的量化分析有真正洞察。** 论文诚实地识别并量化了 per-triple enforcement 引入 cross-field 不一致的代价，提供了 CF source breakdown（hallucinated entities 58.1%, true cascade errors 7.3%）和 beam search 消除路径。[R1-S4, R2-S3]

**S4. Limitations section 诚实全面。** 三段式结构（Constraint scope, Evaluation coverage, Engineering considerations）系统性地列出了方法的边界条件，达到了顶会审稿人期望的坦诚程度。[R1-S4, R2-S4]

**S5. Constraint tightness κ 有诊断价值。** 提供了可量化的 schema 约束强度指标，用于解释不同 schema 下的违规模式差异。[R2-S5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [Critical, 共识] DR→CF trade-off 的 Abstract/正文 framing 严重不平衡。**
Zero-shot greedy S1 下：DR 15.37%→0.17%（↓99%），但 CF 0.08%→9.85%（↑123×）。总违规率从 ~16.7% 降至 ~10.1%，净降幅仅约 40%——远低于 "DR reduction to near-zero" 给读者的印象。Abstract 将 DR reduction 置于叙事主位，CF 被降格为从句且引用 fine-tuned 数字（≤1.4%）而非 zero-shot（up to 12%）。论文认为 DR/CF 严重程度不同（DR 不可恢复 vs CF 可 post-hoc 修复），这有合理性，但当前叙事仍然不够平衡。
- **要求**：Abstract + §5 中并列报告 DR reduction 和 CF increase 的 net effect（total violation change）；§7 扩展 deployment recommendations（明确哪些配置适合哪些场景）

### Should-Fix（影响评分但不一票否决）

**SF1. [Major, 共识] WikiEvents n=20 不足以支撑 task generalization claim。**
MDE=2.0pp, 95% CI ±3.9pp，统计效力严重不足。Abstract 将其与 SciERC（551 docs）和 DocRED（998 docs）并列，给读者造成三个数据集同等证据的印象。
- **要求**：从 Abstract 主 claim 中移除 WikiEvents 或明确标注 preliminary；§5.2 正文最多保留 1 句 feasibility mention

**SF2. [Major, 共识] 70B scale-dependent findings 混淆 scale/family/quantization 三个变量。**
Scale-dependent interaction（8B: 24% vs 70B: 84% independent DR reduction）仅基于 Llama-3.1-70B AWQ INT4 vs 三个 8B 模型。Vocabulary calibration hypothesis（§7）仅有间接推断。8B 量化消融（Appendix R）部分控制了量化效应但缺少 70B FP16 对比。
- **要求**：Contribution 3 改为 'preliminary single-family scale probe'；§7 中 vocabulary calibration hypothesis 标注为 speculative

**SF3. [Major, 共识] Proposition 1 形式化构造（position-based）与实际系统（name-based）之间存在 gap。**
Pumping lemma 证明使用 position-indexed entity references，但实际系统使用 name-based references。Case 1 论证在 name-based scheme 下不直接成立。R2 论证 non-CF 结论通过 cross-serial dependency 论证仍然成立，但当前证明的直接适用性未经论证。
- **要求**：Appendix O 补充讨论 position-based proof 对 name-based scheme 的适用性

**SF4. [Major→Warning, Director 裁定] 绝对 F1 低 (R-F1 40-46%) 且缺失监督 baseline 上下文参照。**
R2 认为 Critical（缺少 PL-Marker 60%+ R-F1 对比使读者无法评估实用价值），R1 REBUT（OntoCoDec 定位为约束框架非 IE 系统，与 span-based 方法不可比）。**Director 裁定**：R1 的定位论证成立——约束框架与 IE 系统的对比方法论不合理。但读者确实需要绝对 F1 的领域参照。降级为 Warning。
- **要求**：§5 Setup 添加 1-2 句说明 LLM-based generative RE 的典型 F1 范围和监督方法 SOTA 水平作为上下文

**SF5. [Major→Warning, Director 裁定] GoLLIE 实验对比被推迟到 future work。**
R2 认为 Critical（最直接竞争者回避对比削弱 novelty），R1 REBUT（方法论差异大、已多处讨论 GoLLIE、complementary work）。**Director 裁定**：GoLLIE 对比的方法论复杂性合理（不同 training paradigm + schema encoding + model families），但"future work"定位感觉回避。降级为 Warning。
- **要求**：引用 GoLLIE 已发表 F1 数字进行 approximate comparison；删除或限定 Appendix S 中不公平的直接对比表

**SF6. [Major, 共识] Contribution 1 声称 '3 model families under both settings' 但 Mistral 仅有 zero-shot。**
Table 2 只有 Qwen + Llama 的 fine-tuning 结果，Mistral-7B 仅 zero-shot。
- **要求**：修改 Contribution 1 措辞或补充 Mistral fine-tuning

### Minor（不影响接收）

**M1. [Info] Abstract F1 范围可能不准确。** "F1 40-46%" 需核实是否与 Table 2 全部数据一致。[R2-W3, R1 AGREE]

**M2. [Info] CF increase 缺少统计检验。** DR reduction 有完整 bootstrap + Bonferroni，CF increase 无 CI/p-value。作为主要 trade-off 应同等对待。[R1-W5, R2 AGREE]

**M3. [Info] LoRA 超参跨数据集迁移。** 超参在 SciERC 调优后直接迁移 DocRED，§5 中未提醒读者此 caveat（仅在 Limitations 提及）。[R1-W8, R2 AGREE]

**M4. [Info] 正文视觉密度不足。** 8 页正文仅 3 个 display items（Figure 1 + Table 1 + Table 2），Related Work + Discussion 连续纯文本。建议从 Appendix 提升 1-2 个关键表/图。[Visual Check]

**M5. [Info] 缩写密度过高。** DR, CF, RV, ET, S1, S2 等在 §5 密集出现，首次阅读体验差。[R2-W8]

**M6. [Info] Proposition 1 新颖性争议。** R2 认为 cross-field binding 超越 CFG 在 PL 理论中是公知常识；R1 认为 NLP 语境中的应用形式化有价值。建议 §3 acknowledge PL 理论中的已知性。[分歧记录]

---

## Reviewer Consensus

以下为两位 Reviewer 达成共识的关键问题：

1. **[AGREE] DR→CF trade-off framing 不平衡**——Abstract 叙事不对称，zero-shot 下净收益远低于 DR 单项数字暗示
2. **[AGREE] WikiEvents n=20 不足以支撑 generalization claim**——应降级或扩展
3. **[AGREE] 70B 仅单一模型族**——混淆 scale/family/quantization，应限定 claim
4. **[AGREE] Proposition 1 证明有 gap**——结论不失效但需补充讨论
5. **[AGREE] Contribution 1 Mistral 覆盖 overclaim**——措辞应修正
6. **[AGREE] CF 缺少统计检验**——与 DR reduction 不对等

---

## Reviewer Divergence

1. **监督 baseline 对比的必要性**：R2 [Critical] 认为缺少监督 baseline 使方法价值不清；R1 [REBUT] 认为约束框架与 IE 系统的对比方法论不合理。Director 采纳 R1 定位论证，降级为 Warning。
2. **GoLLIE 对比的严重程度**：R2 [Critical] 认为回避最直接竞争者；R1 [REBUT] 认为方法论差异大。Director 降级为 Warning，要求 approximate comparison。
3. **Proposition 1 新颖性**：R2 认为有限（PL 公知）；R1 认为语境新颖。如实记录。
4. **Overall Score**：R1 给 3.5 (Borderline Conference)；R2 给 3.0 (Findings)。分歧源于 novelty 评估和监督 baseline/GoLLIE 对比的重要性判断。

---

## Questions（需要作者澄清）

**Q1.** Zero-shot greedy S1 下总违规率从 ~16.7% 降至 ~10.1%（净降 ~40%）。在什么部署场景下，将 DR 转换为 CF 是净正向改善？论文应提供明确的 deployment recommendations。

**Q2.** Proposition 1 的 pumping lemma 证明使用 position-based entity references。如果实际系统使用 name-based references，pumping lemma Case 1 论证是否仍成立？请解释或补充 name-based variant。

**Q3.** Scale-dependent interaction 的 vocabulary calibration hypothesis——有没有直接证据（如 token-level probability distribution 对比），还是仅从 fallback frequency gap 间接推断？

**Q4.** Qwen-8B 触发 0 次 grammar-first fallback vs Llama-8B 触发 5,882 次（100× 差异，Table 10）。这是否暗示 fallback 行为高度依赖 model-specific tokenizer alignment？如果是，框架的 model-agnostic claim 是否需要限定？

**Q5.** Beam search k=4 消除所有 CF violations（Table 24），但 R-F1 从 greedy S1 的 43.77 降至 43.60（SciERC）。这一 tradeoff 在 DocRED 上如何表现？precision/recall 的具体变化？

**Q6.** Fine-tuned 设置下 CF≤1.4% 的违规是否集中在特定高频 relation type？κ 与 per-relation F1 的关系能否为"何时使用约束解码"提供实践指导？

---

## Missing References

- **监督 IE baseline 数字**：PL-Marker, DyGIE++ 等在 SciERC/DocRED 上的已发表 F1 数字应作为上下文参照引用（presentation 需要，非实验对比）[R1 AGREE, R2-W1]
- **Guidance (Microsoft, 2023)**：主要 constrained decoding 库之一，应在 §6 提及 [R1, R2 AGREE]
- **DeepStruct (Wang et al., 2022)**：structured prediction as seq2seq，与 OntoCoDec 范式相关 [R1, R2 弱 AGREE]
- **CRANE (Banerjee et al., 2025)**：已引用但 §6 讨论不够充分（仅 §7 提及），考虑到方法相关性应在 Related Work 更多篇幅 [R2, R1 REBUT——当前讨论篇幅可接受]

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。**

---

## Visual Layout Check（非评分项）

**状态：已完成** (2026-05-23 12:34-12:38 UTC)

| 严重程度 | 数量 |
|----------|------|
| Critical | 1 |
| Warning | 4 |
| Info | 13 |

**关键发现：**
- **[Critical]** 最后一页（p40）仅约 1/5 内容，4/5 为空白，影响专业感
- **[Warning]** 前两页纯文本无 display item，审稿人缺乏视觉锚点
- **[Warning]** 正文 8 页仅 3 个 display items（Figure 1 + Table 1 + Table 2），对实证为主的论文偏少
- **[Warning]** Related Work + Discussion（p7-8）连续纯文本无穿插
- **[Warning]** Appendix B（Extended Related Work, p14-17）连续 4 页纯文本
- **[Info]** 所有表格统一 booktabs 风格，格式专业；公式渲染正确；Limitations 排版符合 EMNLP 要求；无 margin 溢出；无 undefined reference

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Soundness: 3.5/5** — 方法论合理，统计严谨（bootstrap + Bonferroni + effect sizes）。但 Proposition 1 有 position-based/name-based 形式化 gap，CF trade-off framing 不够平衡，scale-dependent claims 证据基础过窄。

**Excitement: 3/5** — 将 IE 本体约束编译为解码掩码的想法新颖实用，但核心架构（XGrammar + stateful type checker）是已有技术的自然组合而非概念性突破。Per-triple 架构限制（无法处理 cross-field consistency without beam search）降低了实际影响力。

**Reproducibility: 5/5** — 28 页附录含完整超参数、硬件配置、随机种子、prompt 模板。统计 power analysis 和 200-doc subset 的充分性论证质量极高。

**Confidence: 4/5**

### 评分理由

论文的核心价值在于**执行质量和评估全面性**而非概念新颖性。两层约束编译框架设计合理、实验覆盖面远超平均水平、统计方法规范、局限性讨论诚实——这些是 Findings 级工作的标志。

降分的主要原因：
1. **DR→CF trade-off 的叙事不平衡**是最严重的问题——zero-shot 下净总违规仅降约 40%，与 headline claim "DR reduction to near-zero" 的印象差距过大
2. **核心新颖性有限**——entity registry + dynamic masking 概念上非 surprising，Proposition 1 是对 PL 理论已知结论的 IE 应用
3. **实验覆盖有明确缺口**——WikiEvents n=20、70B 单一模型族、Mistral 仅 zero-shot、GoLLIE 无实验对比

R1 给出 3.5 (Borderline Conference) 主要基于框架的新颖性和实验充分性；R2 给出 3.0 (Findings) 主要基于有限的概念新颖性和缺失的关键对比。Director 综合裁定 3.0——论文的主要贡献是工程实践和实证分析，Findings track 是其恰当定位。

---

## Detailed Comments

### Abstract
- 约 186-190 words，在 200 word 限制内
- F1 范围 "40-46%" 需核实一致性
- CF 的叙事权重应与 DR 更对称
- "with scale- and schema-dependent layer interaction" 语法不完整

### §1 Introduction
- 叙事结构清晰（problem → limitation → solution → contributions）
- Contribution 1 对 Mistral fine-tuning 覆盖的声称需修正
- "eliminates all violation types at 8B at 1.39× latency" 需限定为 beam k=4 + LoRA

### §2 Background
- 问题形式化清楚，ontology 定义精确
- 正确识别了 grammar-constrained decoding 的局限性

### §3 Method
- 两层架构描述清晰，decidability taxonomy 有组织价值
- Proposition 1 的 position-based/name-based gap 需补充讨论
- Entity registry 的 first-seen semantics 有合理动机，但替代策略（majority voting, deferred assignment）缺乏讨论
- DFA state explosion 的工程论证（6^17 states）比 Proposition 1 本身更有实用价值

### §4 Constraint Composition
- M_final = M_grammar ∧ M_semantic 的组合公式简洁
- Grammar-First Fallback 是合理的工程决策
- κ 概念有诊断价值但 n=3 的统计分析应保持描述性定位

### §5 Experiments
- 五路消融设计合理，fine-tuning composability 是亮点
- DocRED 使用 dev set 的 caveat 应更早、更显著地提及
- CF increase 应得到与 DR reduction 同等的统计处理
- WikiEvents §5.2 仅 1 句交叉引用 Appendix，处理得当

### §6 Related Work
- 三轴组织（constrained decoding / schema-aware IE / constraint enforcement）清晰有效
- GoLLIE 定位（training-time vs runtime enforcement）准确但缺实验支撑
- 篇幅适中但 Appendix B 过长（4 页纯文本）

### §7 Discussion and Conclusion
- Scale-dependent interaction 讨论有价值但 causal explanation 过于 speculative
- DR↔CF trade-off 讨论诚实但篇幅不足，缺 deployment recommendations
- Per-triple vs global enforcement 的讨论恰当指出了未来方向

### Limitations
- 三段式结构全面诚实
- 覆盖了 CF 的本质限制、评估范围、工程约束
- Schema evolution caveat 已存在但可更显著

### Ethics Statement
- 简洁适当

### 格式合规
| 检查项 | 结果 |
|--------|------|
| ACL 模板 | ✓ `\usepackage[review]{acl}` |
| Double-blind | ✓ "Anonymous ACL submission" |
| 正文 ≤ 8 页 | ✓ |
| Limitations 位置 | ✓ |
| Abstract ≤ 200 words | ✓ (~190) |
| Ethics Statement | ✓ |
| References 格式 | ✓ |

---

## Action Items 优先级排序

| 优先级 | ID | Action | 严重程度 |
|--------|----|--------|----------|
| 1 | MF1 | Abstract + §5 并列报告 DR/CF net effect + §7 deployment recommendations | Critical |
| 2 | SF1 | WikiEvents 从 Abstract 降级 + §5.2 最多 1 句 | Major |
| 3 | SF3 | Appendix O 补充 name-based scheme 讨论 | Major |
| 4 | SF6 | Contribution 1 修正 Mistral 覆盖声称 | Major |
| 5 | SF2 | Contribution 3 改 'preliminary probe' + vocabulary calibration 标 speculative | Major |
| 6 | SF4 | §5 Setup 添加 LLM-based RE F1 上下文参照 | Warning |
| 7 | SF5 | GoLLIE approximate comparison + 限定 Appendix S | Warning |
| 8 | M1-M6 | Abstract F1 范围、CF 统计检验、LoRA caveat、视觉密度、缩写、PL acknowledge | Info |