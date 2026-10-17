---
round: 7
overall_score: borderline
timestamp: 2026-05-16T15:27:22.241357+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# Round 7 审稿报告 — schema-dag-extraction

**论文**: "Does Type Confusability Shape Schema-Induced Degradation in Training-Free LLM Information Extraction?"
**目标 Venue**: EMNLP 2026 Main Conference (ARR May 25, 2026)
**Reviewer 编排**: 本轮使用 2 人 (R1: 方法严谨性/实验设计/统计; R2: 新颖性/framing/related work/完整性)。R3 席位本轮未分配——按 EMNLP Main 标准 2 人审稿已覆盖方法+新颖性两个维度，历史轮次 R3 的审查侧重（格式/ethics/细节）已由 R1/R2 在本轮分担。
**外部审稿**: 已请求，截至报告提交时未返回

---

## Summary

本文通过分层控制实验设计，在零样本 LLM 信息抽取中将 schema 规模（count）与类型间语义混淆度（confusability）解耦，提出 Schema Confusability Score (SCS) 作为量化指标，在 NER/RE/ED 四个数据集上验证了"两通道退化"假说——count 驱动 recall 下降（Channel 1），confusability 驱动 type substitution（Channel 2）。实验设计严谨、统计报告透明，但核心效应在实际场景中偏小（typical batch 仅 2.2pp 差异），"两通道可分离"的核心 claim 仅在 RE 上有 TOST 支持（NER factorial p=0.50 不支持），且论文的 framing 偏向放大极端结果。

---

## Strengths

- **S1 [共识]**: 实验设计精心——BCS-controlled experiments 有效隔离 count/confusability，within-pool analysis 控制 pool composition confound，permutation test 验证跨池 slope 一致性（p=0.60）。这是 zero-shot IE 领域罕见的准因果推断尝试。
- **S2 [共识]**: 统计透明度在 NLP 论文中少见——主动报告 r²=1.3-1.7% 的微小效应，§4.3 明确区分 extreme-batch（31.2pp）与 typical-batch（2.2pp），Limitations 逐条列出 7 项已知缺陷。
- **S3 [共识]**: 负面结果的诚实报告——SDGD 在 NER 上的全面失败（F1: 0.445→0.251）及 merge amplification 的深入诊断对社区有实际指导价值。Oracle routing ceiling analysis 巧妙证明了性能天花板存在但实际不可达。
- **S4 [共识]**: MAVEN centrality confound 的识别和处理（partial correlation 控制 log frequency + degree centrality）展示了对 embedding space 结构的成熟理解。
- **S5 [共识]**: Pair-to-batch amplification 的 Monte Carlo 模拟（Appendix F）提供了从 pair-level r²=7% 到 batch-level R²=22% 的定量解释。
- **S6 [共识]**: 跨模型（Qwen3-32B + Llama-3.1-8B）、跨 prompt（v1/v2）、跨任务（NER/RE/ED）、跨粒度（sentence/document-level RE）的多维验证增强结论鲁棒性。

---

## Weaknesses

### Critical

**W1. "Empirically separable channels" 的核心 claim 在 NER 上缺乏统计支撑 [R1-W1 + R2-W4, 共识]**
三项 factorial/equivalence 检验中两项失败：FewRel TOST p=0.003（支持），Few-NERD factorial p=0.50（不支持），Few-NERD 2×2 TOST p=0.56（不支持）。§4.4 自己承认 NER 中 channels "coupled"，但 Abstract/Introduction 仍以 "empirically separable" 为全局 framing。R2 补充：NER 中 boundary ambiguity 和 type ambiguity 本质上不可分离，所以 separability 在 span-level tasks 上可能概念上就不成立。
→ **必须修改**: Abstract/Intro 将 "empirically separable" 限定为 RE-specific，NER 改为 "two channels identified, separability not confirmed"。

**W2. Framing 过度强调 extreme-batch 31.2pp，弱化 typical-batch 2.2pp [R1-W6 + R2-W2, 共识]**
Abstract 首个数据点为 quartile gap −5.3pp，Introduction finding (1) 以 "up to 31.2pp" 结尾。但 typical scenario 下效应仅 2.2pp（CI: [0.4, 4.0]），CI 下界仅 0.4pp。R1 补充：count effect 达 35+pp 而 confusability 仅 2.2pp——confusability 作为 "shaping factor" 的重要性需 contextualize。论文 §4.3 的 honest qualification 来得太晚。
→ **必须修改**: Abstract 以 typical 2.2pp 和 quartile 5.3pp 为主锚，extreme 31.2pp 降为 "upper bound under adversarial construction"；讨论 2.2pp 是否超过 practitioner noise tolerance。

**W3. 非显著结果 +1.4pp (p≈0.19) 的 contribution framing [R2-W3, R1 部分同意]**
Contribution #4 正文实际写 "no statistically significant improvement"（R1 指出这是负面证据），但 Abstract 措辞 "directional +1.4pp gain" 可被误读为正面 claim。Graph coloring 方案在 15 random seeds 中仅排第 13——比大多数随机方案更差，这一 damning detail 仅在 Table caption 中。
→ **必须修改**: Abstract 改为 "no significant improvement (+1.4pp, p≈0.19, n.s.)"；正文讨论 graph coloring 排 13/15 的含义。

**W4. 核心 novelty 有限 — two-channel decomposition 近似 trivial [R2-W1 critical, R1 部分 REBUT]**
"count↓recall + similarity↑confusion" 作为概念分解是常识性直觉。LLM-PEE (2025) 已用同样 metric。R1 部分反驳：controlled methodology 有 RCT-like 价值，nuanced findings（NER coupling, 2.2pp typical, merge amplification）非 trivial。但 R1 也承认 "not enough for main conference"。
**两人共识**: Findings-level 贡献，非 main conference level novelty。

**W5. Pairwise r²=1.3-1.7% 实际意义 + conditioning bias [R1-W3, R2 AGREE]**
Conditioning on non-zero confusion pairs 将 r² 从 1.3% → 7%，引入选择偏差。Monte Carlo 用 7% 输出 R²=0.219 匹配观测 0.218——有效但论文未明确区分 conditional vs unconditional。缺乏对 alternative confusability metrics 的讨论。
→ **必须修改**: 明确标注 7% 为 conditional effect size；讨论 alternative proxies；引用 Cohen (1988) / Lakens (2013)。

---

### Warning

**W6. Count curve 每 level 仅 5 batches，方差未报告 [R1-W2 → R2 REBUT 降为 warning]**
Monotonic pattern 跨 4 数据集复现，cross-model r=0.725 支持 stability。但 Figure 1a 缺少 error bars。
→ 补充 Figure 1a error bars 和 batch 间 SD。

**W7. 不同 dataset 使用不同 embedding (Qwen3 vs MiniLM) [R1-W4, R2 AGREE]**
Few-NERD 用 extraction model 自身 hidden states → 循环论证风险；跨数据集 r 值不可比。
→ 解释 Few-NERD 选 Qwen3 的理由；补充 MiniLM 对比。

**W8. FewRel data contamination 未充分排除 [R1-W5 + R2-W7, 共识]**
Defense (−8.8pp, p=0.06) borderline n.s.。Contamination 可能 non-uniform。
→ 细化 contamination 分析到 BCS 条件。

**W9. Cross-model claim 省略 NER Channel 2 失败 [R2-W5, R1 AGREE]**
Conclusion "replicate across model families" 后仅列 RE 数据。
→ Conclusion 明确限定。

**W10. Prompt length vs count confound [R1-Q5 + R2, 新发现]**
Per-type recall 0.586 > single-pass 0.368 暗示 count-degradation 可能是 prompt-length-driven。
→ 讨论 prompt length 作为 Channel 1 的潜在 mechanism。

**W11. TOST margin ±3pp 无 justification [R1-Q6, R2 AGREE]**
Typical difference 仅 2.2pp，±3pp margin 宽松。Analyst degrees of freedom。
→ 提供 justification + sensitivity analysis。

**W12. Related Work 缺口 [R2-M1/M3, R1 部分 AGREE]**
未引用 "From Haystack to Needle" (2025)、传统 ML label confusion 文献。

---

### Info

- **W13**: Abstract 数字密度过高 [R2-W8 → R1 REBUT 降为 info]
- **W14**: p-value 格式不一致 (Appendix 无前导零)

---

## Reviewer Consensus

1. "Empirically separable" claim 必须限定为 RE-specific [AGREE]
2. Extreme-batch 31.2pp 不应作为 headline [AGREE]
3. +1.4pp (p≈0.19) 不应 frame 为正面结果 [AGREE]
4. FewRel contamination defense 不够 conclusive [AGREE]
5. 不同 embedding 跨数据集不可比 [AGREE]
6. Count curve 应补充方差信息 [AGREE]
7. Cross-model claim 应限定 NER Channel 2 [AGREE]
8. 核心 novelty 为 Findings-level [AGREE]

## Reviewer Divergence

1. **Novelty 程度**: R2 near-trivial (critical) vs R1 methodological value (partial rebut)。两人均认为不够 main conference。
2. **SCS metric**: R2 增量贡献存疑 (warning) vs R1 非 claimed novelty (rebut)。
3. **Abstract 数字密度**: R2 影响可读性 (warning) vs R1 精确性是优点 (rebut → info)。
4. **Count curve 5 batches**: R1 critical vs R2 rebut to warning。

---

## Questions for Authors

1. Typical-batch 2.2pp 是否超过下游应用 noise tolerance？
2. 为什么不纳入 entity frequency、prompt position 等 multivariate model？
3. Count curve recall 下降是否部分由 prompt length 而非 type count 驱动？
4. TOST margin ±3pp 的选择依据？sensitivity analysis？
5. Few-NERD 为什么选 Qwen3 而非 MiniLM？
6. Aggregation simulation ρ=0.35 的来源和 sensitivity？
7. Extreme batch 中具体 types 是否有 domain confound？

---

## Missing References

**必须引用**:
- "From Haystack to Needle" (2025) — label space reduction [共识]
- Cohen (1988) / Lakens (2013) — small effect size 方法论 [共识]
- 传统 ML label confusion 文献 [共识]

**建议引用**:
- Rothman (1990) / Perneger (1998) — multiple testing [R1]
- Many-shot ICL (NeurIPS 2024) [分歧]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：已请求，截至报告提交时**未返回**。状态: pending。

---

## Overall Assessment

**Overall Score**: **Borderline** (介于 weak reject 和 Findings accept 之间)

- R1: 3/5 (Findings acceptance)
- R2: 2.5/5 (Borderline reject → 条件性 3/5 if framing fixed)
- R3: 本轮未分配（历史席位；本轮审查维度已由 R1/R2 覆盖）

**置信度**: 4/5

**核心判断**: 实验设计严谨、统计报告透明的分析型论文。三个结构性问题制约 main conference 接收：(1) Novelty ceiling——核心发现概念上不令人惊讶，practical magnitude 仅 2.2pp；(2) Overclaiming——separability 仅 RE 上有 TOST 支持，framing 偏向极端结果；(3) Generality gap——clean results 主要来自 FewRel (closed-set classification)，NER 上 separability 不成立且 8B 无法复现 Channel 2。

**建议**: 修复 overclaiming 后适合作为 **EMNLP 2026 Findings** 接收。当前 framing 下不建议 main conference。

---

## Detailed Comments

### Abstract
- 12+ 数字/区间，建议精简至 3-4 核心数字
- "first study to formally isolate" 加 qualifier
- "two empirically separable channels" 限定为 RE
- "directional +1.4pp gain" → "no significant improvement"

### §1 Introduction
- Contribution #4: "directional gain" 可被误读；graph coloring 排 13/15 应在正文讨论
- Finding (1): extreme 31.2pp 在最显眼位置；confusability 2.2pp vs count 35+pp 的 relative importance 需 contextualize
- Channel 1/2 定义位置——当前 Introduction 已有，confirmed adequate

### §2 Related Work
- 缺 "From Haystack to Needle" (2025)
- 缺传统 ML label confusion 文献
- SGD/SGD-X 正文仅一句（Appendix H 补充不够）
- SCS novelty 段诚实但强化 novelty 有限印象

### §3 Experimental Setup
- FewRel contamination defense (p=0.06) 不 conclusive
- 单 seed + "variance not quantified"（greedy decoding 理论上 deterministic，实际影响极小）
- 不同 embedding 选择需更明确 justify
- Bootstrap B 差异 justified，non-issue

### §4 Results
- §4.3 Practical magnitude 段优秀但来得太晚
- §4.4 NER "coupled" vs Abstract "separable" 矛盾
- §4.5 Centrality confound 分析深入
- Pairwise "ρ=0.27-0.31 among non-zero pairs" 有选择偏差，建议移至 appendix

### §5 SDGD
- Merge amplification 诊断有力
- Graph coloring BCS margin 0.006——ceiling effect 应讨论
- 是否尝试 NMS / span-level voting 替代 merge？

### §6 Discussion
- Embedding similarity 假说缺 mechanistic evidence
- Schema design implications 在 typical 2.2pp 下 cost-benefit 存疑
- Cross-domain connections 应从 Appendix 提升到正文

### Conclusion
- 过短 (~100 words)
- "replicate across model families" 应限定
- "+1.4pp" 应标 n.s.

### Limitations
- 写得全面。Item 3 TOST p=0.50 需澄清是 interaction p 还是 TOST p
- Multiple comparisons 段应引用方法论文献

### Checklist
- B1 补 DocRED + Llama 引用