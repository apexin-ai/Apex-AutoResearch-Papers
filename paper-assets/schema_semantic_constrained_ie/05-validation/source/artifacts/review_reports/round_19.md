---
round: 19
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-22T13:56:52.745758+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# Round 19 审稿报告 — OntoCoDec: Type-Constrained IE via Compiled Schema Constraints
**Venue**: EMNLP 2026 (ARR Long Paper) | **Deadline**: 2026-05-25 | **审稿日期**: 2026-05-22

---

## Summary

OntoCoDec 提出两层约束解码框架，将 IE 本体编译为 token 级解码约束：grammar layer（CFG via XGrammar）保证 JSON 结构和词汇合法性，semantic layer（prefix-decidable with state）通过动态实体注册表在运行时执行 domain/range 类型约束。Proposition 1 证明无界实体集下 IE 类型约束不是 context-free。在 SciERC、DocRED、WikiEvents 三个数据集上，跨 3 个 8B 模型（Qwen3-8B、Llama-3.1-8B、Mistral-7B）和 1 个 70B 模型验证，LoRA + greedy S1 实现 DR ≤ 0.09%（fine-tuned），R-F1 43-46%。

---

## Strengths

**S1. 理论基础扎实。** Proposition 1（§3, Appendix O）正确证明 IE domain/range 约束非 context-free，Remark 诚实区分理论不可能性与工程不可行性。三层约束分类体系（context-free / prefix-decidable / non-local）为后续研究提供了有用的概念框架。[R1-S1, R2-S1, R2-S3 共识]

**S2. 实验矩阵极为全面。** 3 数据集 × 3-4 模型 × zero-shot/fine-tuned × 多种解码策略。五路消融（Table 1）清晰隔离各组件贡献；fine-tuning composability（Table 2）验证实用部署配置；cross-model validation（Table 3）验证泛化性。[R1-S2, R2-S2 共识]

**S3. 可重复性堪称典范。** 24 页附录包含完整超参（Appendix G）、cross-seed 方差（Table 26, 3 seeds）、prompt 模板（Table 5）、scalability profiling（Table 35）、4 case studies。[R1-S3 强调, R2-S2 认同]

**S4. Grammar-first fallback 分析是亮点。** Table 6 因果追溯精确定位 fallback 触发位置；Table 7 CF-priority 对比展示设计决策代价。对工程选择的系统化分析增强论文的科学性。[R1-S6, R2-S4 共识]

**S5. 诚实报告局限。** 70B 和 WikiEvents FT 明确标注 "preliminary"；dual-factor n=3 限制显式承认；CF↔DR tradeoff 透明讨论。[R1-S4]

**S6. GCD 等价性验证。** vLLM guided_json 实验（Table 16-17）独立验证 grammar layer ≈ GCD（所有指标 Δ<0.5pp），增强论文可信度。[R2-S5]

---

## Weaknesses

### Must-Fix（无）

### Should-Fix

**W1. Semantic layer 增量新颖性需更坦诚讨论。** [R2-W1, R1 Excitement 3.5/5]
Grammar layer 是标准 GCD（论文自己验证了等价性）。Semantic layer 的核心思想——维护运行时 entity registry 来执行 domain/range type checking——是合理但非突破性的工程扩展。PICARD（Scholak et al., 2021）已展示 stateful constrained decoding 思路。论文 §1 写 "systematic engineering contribution with theoretical grounding"，但 Discussion 段仅一句话（§7），未充分讨论增量创新与系统贡献的关系。
**建议**：§7 增加 1-2 段讨论 semantic layer 相对于 PICARD 式 stateful decoding 的独特技术点（entity registry random-access vs. beam pruning、forward masking vs. post-generation filtering、multi-relation output vs. single SQL query）。

**W2. CF 违规作为未解决核心问题在叙事中被弱化。** [R2-W3, R1 认同]
Fine-tuned CF 仍有 0.46-1.18%（Table 2），CF↔DR 是 fundamental tradeoff（Table 7: 消除 CF fallback → DR +13.85pp）。但 Abstract 写 "CF ≤ 1.4%"，Intro 贡献列表未提 CF 局限，§7 仅一句。CF 在下游 KG 构建中是严重问题（同一实体类型不一致）。
**建议**：Abstract CF 表述改为 "with residual CF 0.5-1.2% under fine-tuning (attributable to per-relation independence; §4)"；§7 明确标记 global entity-level type consensus 为最重要 future work。

**W3. WikiEvents 微调 n=20 统计效力不足。** [R1-W1, R2-Q4 共识，连续 8 轮提出]
§5.4 从 20 个测试文档得出 EE 微调兼容性结论。Bootstrap 95% CI ±3-5pp，F1 差异在 CI 范围内。无 power analysis。
**建议**：提供 power analysis（n=20 能检测多大的 effect size？），或将 fine-tuning composability claims 严格限制在 zero-shot (n=246) 范围内。

**W4. 主表缺少外部约束解码 baseline。** [R1-W3]
Tables 1-4 仅对比无约束和自身消融变体。GCD/vLLM 验证数据在 Appendix（Table 16-17），但主文读者不一定会翻到附录。
**建议**：Table 1 增加 GCD-equivalent 行（vLLM guided_json 数据），让读者在主表中直接看到与最直接 prior work 的对比。

**W5. 遗漏 2026 年初高相关 constrained decoding 工作。** [R2-W4]
- DCCD（Reddy et al., arXiv:2603.03305, March 2026）—— draft-conditioned constrained decoding，分析约束解码 quality degradation，与 grammar-first fallback 互补
- "Thinking Before Constraining"（Nguyen et al., arXiv:2601.07525, January 2026）—— free-reasoning + structured-generation 混合，与 S2 two-pass 有设计哲学相似性
**建议**：§6 Constrained decoding 段落末尾增加 2-3 句讨论。

**W6. Enabling dependency 验证存在混淆变量。** [R1-W4]
Table 1 Semantic-only 行同时移除了 JSON 结构保证和词汇约束，无法区分 enabling dependency（grammar 是 semantic 的前提）和语义层独立缺陷。理想控制：提供 JSON 结构但不提供词汇 enum 约束 + semantic layer。
**建议**：补充说明 semantic-only 配置的确切 scope，或在 Appendix 增加此消融实验。

**W7. Dual-factor 分析 (n=6) 被过度引用。** [R1-W2, 与 R16-W1 相关]
Figure 2 对 6 点拟合 R²=0.886，虽已降级为 "descriptive correlate"（p=0.138 显式标注），但后续多处引用（Pareto frontier 等）。
**建议**：进一步降格为 exploratory observation，限制引用范围在 §4 内。

### Minor

**M1.** 效应量报告不完整——Table 2 有 p-value 无标准化效应量，Table 1 无 CI。[R1-W5]
**M2.** Proposition 1 主文可更精确标注 "unbounded" 限定条件。[R1-W7, R2-W2]
**M3.** 信息密度极高，§3.3 单段引入过多概念。建议增加 SciERC triple 的 running example。[R2-W5]
**M4.** Abstract 部分数值精度过高（"DR ≤ 0.09%"），跨配置 range 下可能误导。[R2-W7]
**M5.** 70B AWQ INT4 量化对 logit 分布的影响未隔离（Limitations 已有 disclaimer）。[R1-W6, 连续 6 轮]

---

## Reviewer Consensus

以下为两位 Reviewer 达成共识的关键判断：

1. **[AGREE] Proposition 1 证明正确且有价值**，但其实践影响力不应被过度包装——PDA 不能做 cross-reference checking 是已知限制，形式化到 IE 场景有贡献但非深刻理论突破。
2. **[AGREE] 实验覆盖度和可重复性是论文最大亮点**，24 页附录、cross-seed、多数据集/模型设计均为高标准。
3. **[AGREE] CF 问题是当前框架的核心未解决局限**，叙事中应给予更多权重。
4. **[AGREE] WikiEvents n=20 统计效力不足**，fine-tuning composability claims 需要降级或补充 power analysis。
5. **[AGREE] 论文定位为 engineering contribution with theoretical grounding 是准确的**，但 §7 Discussion 对此讨论不足。
6. **[AGREE] 评分 3.5/5 (Borderline Conference)**——补充 W1-W5 可提升至 Conference 水平。

## Reviewer Divergence

无重大分歧。两位 Reviewer 在评分和主要判断上一致。
- R1 更关注统计方法论（effect sizes、power analysis、confounding variables）
- R2 更关注学术定位（novelty ceiling、missing references、narrative balance）
- 两个视角互补，结论一致。

---

## Questions

**Q1.** [R2] Proposition 1 使用 position-based indexing，系统使用 name-based referencing。在 name-based 且 entity names 唯一有界长度下，CFG 能否编码 name→type 映射来执行约束？

**Q2.** [R1] Semantic-only 配置是否完全移除了 JSON 结构保证？这影响 enabling dependency 证据强度。

**Q3.** [R1] Grammar-first fallback 在 Llama 上 100% 触发但 Qwen 零触发——根本原因是什么？

**Q4.** [R1] TCR（Post-hoc type consistency, Appendix L）为何不作为标准 pipeline？似乎是 CF 的完整解决方案。

**Q5.** [R1] Constraint compilation 0.45s (XLarge) 是否验证到更大本体（如 Wikidata 规模 5000+ entity types）？

**Q6.** [R2] CF fallback rate（0.46%）和 first-token fallback rate（19.93%）的差异如何解释？

**Q7.** [R2] §5.2 cross-dataset validation 的确切 setup——SciERC schema 用于 DocRED？

---

## Missing References

1. **Reddy, A., et al. 2026.** Draft-Conditioned Constrained Decoding for Structured Generation in LLMs. arXiv:2603.03305. — 分析 constrained decoding quality degradation，提出 draft-then-constrain 方法。
2. **Nguyen, N.T.H., et al. 2026.** Thinking Before Constraining: A Unified Decoding Framework for Large Language Models. arXiv:2601.07525. — free-reasoning + structured-generation 混合解码。
3. **（可选）Schema Key Wording.** arXiv:2604.14862, April 2026. — JSON schema key 命名作为约束解码隐式指令通道。发表时间较近。

---

## External Review (Stanford Agentic Reviewer)

**状态：已跳过。** 外部审稿请求发送后被跳过（skipped_at: 2026-05-22T13:43:32）。本报告不包含外部审稿结果。

---

## Visual Layout Check（非评分项）

**状态：已完成。** 4 warnings / 14 info / 0 critical。

**Warnings：**
1. **Page 1-2**：连续 2 页纯文本（Abstract + Intro + Background），Figure 1 直到 page 3 才出现。建议将架构图或 teaser 前移至 page 2。
2. **Page 8-9**：Related Work + Limitations 连续 2 页纯文本。可考虑 Related Work 中嵌入方法对比 taxonomy 表。
3. **Page 13-17**：Appendix B Extended Related Work 连续 5 页纯文本，无 display item。
4. **Page 30**：Table 31 使用红/绿标注，对色盲读者不友好。建议改为 red/blue 或添加 ✗/✓ 形状标记。

**Info 摘要：**
- 主文 8 页内 5 个 display items（1 figure + 4 tables），密度偏低端（通常 5-8 个）
- Figure 1 组件标注文字偏小（约正文 60%）
- Tables 排版规范（booktabs、加粗、对齐一致）
- 无 margin 溢出、公式渲染错误或 section heading 孤悬
- ACL anonymous submission 格式正确

---

## Overall Assessment

| 维度 | 分数 | 理由 |
|------|------|------|
| **Soundness** | 3.5/5 | Proposition 1 正确，消融设计干净。但 WikiEvents FT n=20 和 dual-factor n=6 统计效力不足；enabling dependency 消融存在混淆变量。 |
| **Excitement** | 3/5 | IE 本体自动编译为 token 约束有实用价值，三层分类体系有概念贡献。但 semantic layer 是对已知 stateful CD 的工程扩展，核心思路可预见。 |
| **Reproducibility** | 4/5 | 超参/种子/硬件/prompt 详细，附录信息量大，代码承诺开源。 |
| **Overall** | **3.5/5 (Borderline Conference)** | 执行质量高的系统论文，理论动机清晰、实验覆盖全面、附录详尽。距 Conference (4.0) 的差距在于：(a) semantic layer 增量新颖性讨论不足；(b) CF 作为核心局限在叙事中被弱化；(c) WikiEvents n=20 统计效力问题连续 8 轮未解决；(d) 主表缺外部 baseline。修复 W1-W5 后有望达到 Conference 水平。 |
| **Confidence** | 4/5 | 两位 Reviewer 分别精读全文（含 24 页附录），独立检索最新文献，交叉验证后评分一致。 |

**一句话判断**：一篇实验全面、理论有支撑、执行精度高的系统性工作，但 semantic layer 的概念增量和 CF 问题的坦诚度是从 Borderline 到 Conference 的关键差距。

---

## Detailed Comments

### §1 Introduction
- "systematic engineering contribution with theoretical grounding" 定位准确但需 §7 展开讨论
- 贡献列表第 1 点 "formalize a well-known intuition" 措辞得当，但 Proposition 1 的定位应更精确（形式化已知直觉 vs. 新理论发现）

### §3 Method
- Proposition 1 证明正确；Remark（finite entity sets）诚实且必要
- 建议在 Remark 后增加："The practical contribution is the precise characterization motivating our two-layer design, not the impossibility result per se."
- Semantic layer §3.3 信息密度过高——建议增加 running example

### §4 Constraint Composition
- Grammar-first fallback 设计有理有据（Table 6 causal tracing 是亮点）
- κ̄ 分析已降级为 descriptive（p=0.138 标注），但后续引用仍偏多

### §5 Experiments
- Table 1 消融干净但缺 GCD baseline 行
- Table 2 composability 是论文最有说服力的结果——DR ≤ 0.09% at R-F1 43-46%
- WikiEvents FT（Table 4 下半）n=20 效力不足——连续 8 轮 unresolved
- vLLM guided_json 验证（§5 末段）增强了论文的可信度

### §6 Related Work
- 遗漏 DCCD (2603.03305) 和 Thinking Before Constraining (2601.07525)
- 与 PICARD 的技术区别讨论不充分（当前仅一句）

### §7 Discussion
- 过于简短（仅 1 句话）——需要展开讨论 novelty positioning 和 CF as open problem

### Limitations
- 覆盖充分（constraint scope、evaluation coverage、engineering considerations）
- AWQ INT4 disclaimer 已存在但无实证量化

### Format
- 正文 ≤ 8 页 ✓
- ACL anonymous submission 格式 ✓（页眉 "Anonymous ACL submission"）
- Limitations 和 Ethics 独立 section ✓
- 无匿名性泄露 ✓