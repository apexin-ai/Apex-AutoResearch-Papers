---
round: 17
overall_score: 3.0 (Findings)
timestamp: 2026-05-18T08:39:11.883494+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 17

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)
**投稿类别**: Findings
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+写作+完整性）
**审稿模式**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮收敛）

---

## Summary

本文研究 training-free LLM 信息抽取中 schema 复杂度如何影响性能，将 schema 复杂度分解为类型数量（count, Dimension 1）和类型间语义混淆度（confusability, Dimension 2），提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 量化后者。在 Few-NERD (NER)、FewRel (RE)、DocRED (doc-RE)、MAVEN (ED) 上进行 count curve 和 BCS-controlled 两类实验，发现：count-related recall decline 是主导因素（-34 至 -49pp）；BCS 可预测 RE batch-level accuracy variance（R²=0.22-0.53）但对 NER 无效（r≈0, n=450）；Schema 分解因 merge amplification (NER) 和 routing failure (RE) 而失败。Cross-model 验证覆盖 Qwen3-32B、Llama-3.1-8B/70B、Gemini 2.5 Flash。

---

## Strengths

**S1. 实验控制设计出色** [R1/R2 共识]
BCS-controlled 实验通过固定 count 变化 BCS，在 FewRel balanced design 下消除 type frequency confound。within-pool analysis（80-relation pool 采样 16-relation subsets）进一步控制 pool composition confound，permutation test (p=0.60) 证实 slope 一致性。这种层层递进的控制设计在 NLP 实证研究中罕见。

**S2. 统计方法论成熟** [R1/R2 共识]
TOST 等价检验、bootstrap CI (B=10,000/1,000)、permutation test、cluster bootstrap、variance decomposition、Fisher z CI 等方法组合使用，达到行为科学严格标准。TOST sensitivity analysis 提供不同 margin 完整结果，统计报告透明度在 NLP 论文中属上游。

**S3. 负面结果报告诚实且有诊断价值** [R1/R2 共识]
SDGD 分解失败不仅报告结果，还提供 merge amplification 和 routing failure 的机制诊断。NER batch-level null (r≈0, n=450) 坦诚报告而非隐藏。MAVEN centrality confound 的发现和处理（partial correlation 控制 log frequency + degree centrality）展示科学严谨性。

**S4. Cross-model 验证覆盖面广** [R1/R2 共识]
从 8B (Llama-3.1-8B) 到 32B (Qwen3) 到 70B (Llama-3.1-70B-FP8) 到 proprietary (Gemini 2.5 Flash)，Dimension 1 在所有模型上复现（RE count 8→80: -30.7pp on 70B vs -30.1pp on 32B）。

**S5. Robustness checks 全面** [R1 主导, R2 认可]
Cross-prompt validation (4 prompt variants)、cross-seed variance decomposition、BCS aggregation sensitivity (mean vs max)、SCS embedding ablation (name-only vs name+def)。每一项增强核心发现可信度。

**S6. Limitations 极其详尽** [R1/R2 共识]
9 条 + multiple comparisons 讨论，覆盖几乎所有可预见 concern，包括 data contamination 多层防线分析。在 NLP 论文中属最诚实的 limitations 之一。

**S7. AI 写作痕迹极少** [R2 主导, R1 认可]
全文无 em-dash 解释性用法、无禁忌词（notably/leverage/delve 未出现）、仅附录有 3 处轻微 -ing 短语。写作质量在同类论文中处于上游。

---

## Weaknesses

### Must-Fix (Critical)

**N1. Scope overclaim: Title/Abstract 暗示跨任务通用性，但 BCS batch-level 预测力仅限 RE** [R1/R2 完全共识]
- Title "Information Extraction" 涵盖 NER/RE/ED，但 BCS 在 batch-level 对 NER 无预测力 (r≈0, n=450, §5.3-5.4)，MAVEN 有 centrality confound (§5.5)，仅在 RE (FewRel R²=0.22, DocRED R²=0.53) 有效。
- Abstract 确实提到 "but not NER"，但关键限定出现在中间位置，Title 仍暗示通用性。
- Pairwise SCS 在三个任务上均显著（Few-NERD r=0.112, MAVEN r=0.129, FewRel r=0.187; Table 2），这是真正跨任务的发现。问题在于从 pairwise 到 batch-level 的 aggregation 仅在 RE 成功。
- **建议**: Title 加限定词；或改叙事为 "pairwise confusability predicts type confusion across tasks; batch-level prediction is task-dependent"；Abstract 第一段即声明 scope boundary。

**N2. TOST ±3pp margin > typical main effect 2.2pp，"bounded association" claim 被削弱** [R1/R2 完全共识]
- Typical-batch confusability gap 为 2.2pp (§5.3)。TOST 使用 ±3pp margin 超过主效应本身。±1pp 下 inconclusive (p=0.278)，无法排除 interaction 达主效应 ~50% 的可能。logit-scale TOST 同样 inconclusive (p=0.209)。
- 主文 "bounded association" 措辞暗示 interaction 可忽略，但 ±1pp 证据不支持此强度。
- **建议**: 主文 §5.4 报告 ±1pp/±2pp/±3pp 三个 margin 结果；措辞改为 "point estimate (0.47pp) is small, but equivalence not confirmed below 2pp"；logit-scale 结果移至主文或至少提及。

**N3. Constrained decoding (enum constraint) 可能是 BCS-accuracy 关系成立的必要条件** [R1/R2 共识，R2 qualified]
- RE 使用 enum constraint，closed-set classification 下所有 non-none errors 必然是 intra-batch type substitution，结构性保证 BCS-error rate 关联。NER（无 enum constraint）的 batch-level null (r≈0) 与此一致：errors 散布到 missed entities、boundary errors、hallucinated types，稀释 BCS 信号。
- §7 Discussion 承认 "upper bounds" 但不够显著。这不仅是 upper bound 问题——constrained decoding 可能是 BCS 预测力的必要条件。
- R2 指出 unconstrained decoding ablation 技术上困难（输出格式不可控），建议 relaxed constrained decoding 中间态作为折中。
- **建议**: 主文显式将 constrained decoding 列为 boundary condition；考虑 relaxed decoding ablation；讨论 NER null 是否可用 error channeling hypothesis 统一解释。

### Should-Fix (Warning)

**W1. SCS 缺乏与简单 baseline metrics 对比** [R1/R2 完全共识]
- SCS 使用 embedding cosine similarity。Limitations 承认 "whether simpler measures achieve comparable predictive power remains open"——这不应是 open question，应在论文中回答。
- Appendix L 仅比较 SCS 两个变体 (name-only vs name+def)，未与 string edit distance、WordNet path distance、same-parent indicator 对比。
- **建议**: 增加 Table 对比 SCS 与至少 2 个 qualitatively different baselines 的 pairwise confusion prediction r 值。

**W2. SCS/BCS 指标新颖性定位** [R1/R2 分歧，降级为 warning]
- R2 认为 SCS/BCS 与 LLM-PEE metric 形式相同，novelty 不足为 critical 问题。
- R1 反驳：LLM-PEE 用 similarity 做工程（schema partitioning），本文做科学（controlled measurement），是合法区分。
- 共识：Contribution 2 措辞应更明确与 LLM-PEE 区分，避免暗示 metric novelty。
- **建议**: Contribution 2 改为 "Using the embedding-similarity criterion from LLM-PEE, we show..." 或类似措辞明确 borrowed metric。

**W3. Practical implications 薄弱** [R1/R2 部分分歧，R2 列为 critical，R1 qualified agree]
- NER 建议 "减少候选类型数" trivially known；RE "pre-screen 上四分位 SCS" 收益 3-5pp 在部署中边际效用有限。Schema decomposition 被证明失败。
- R1 引用 ARR guidelines H5/H6：不应要求 SOTA 或惩罚 negative results；诊断研究有独立价值。
- **建议**: Discussion 增加具体 practitioner guidance——BCS 阈值建议、type pool 设计原则、task-type-dependent decision flowchart。

**W4. Abstract 信息密度过高** [R1/R2 完全共识]
- ~195 words 含 8+ 数值，BCS 未展开全称（仅 "batch-level aggregation (BCS)"），嵌套括号增加认知负担。
- **建议**: 减少到 3-4 个关键数字，展开 BCS 全称，先说 takeaway 再给支撑。

**W5. DocRED R²=0.53 基于 n=35, CI 宽** [R1/R2 完全共识]
- Fisher z CI: [0.27, 0.73]，跨度 0.46。主文 "BCS explains 22-53%" 中的 53% 使用点估计，uncertainty 很大。
- **建议**: 引用 DocRED R² 时附带 CI 或注明 sample size limitation。

**W6. 16-relation BCS-controlled 仅 single extreme batch** [R1/R2 完全共识]
- n=1 extreme batch per BCS level，无 bootstrap CI。Table 已注释但数据仍被引用为 evidence。
- **建议**: 提及 16-rel 结果时注明 "based on a single extreme batch; no CI available"。

**W7. Pair-to-batch aggregation simulation post-hoc** [R1/R2 完全共识]
- Monte Carlo simulation 参数来自同一数据 (ρ=0.35, R²=0.074)。Appendix 声明 "not evidence base" 但 §7 引用时措辞偏强。
- **建议**: §7 加注 "simulation uses parameters from the same data; serves as consistency check, not independent evidence"。

**W8. Introduction findings 段统计量过密** [延续 R16]
- Findings (1)-(4) 含 TOST p=0.003, R²=0.22-0.53, +1.4pp p≈0.19 等精确值，属 Results 内容。
- **建议**: Introduction 改为定性描述。

---

## Reviewer Consensus

以下关键问题两位 Reviewer 达成共识：

1. **[AGREE] Scope overclaim**: BCS batch-level 仅限 RE，Title/Abstract 应限定（R1-N2 = R2-N1）
2. **[AGREE] TOST margin**: ±3pp > 2.2pp main effect，"bounded association" 措辞偏强（R1-N1, R2-W6→AGREE）
3. **[AGREE] Constrained decoding**: enum constraint 可能是 BCS-accuracy 关系的必要条件（R1-N3, R2-Q1→AGREE with nuance）
4. **[AGREE] SCS baseline 对比缺失**: 需与 string overlap / WordNet 等对比（R1-W1, R2→AGREE）
5. **[AGREE] Abstract 过度压缩**: 数字堆砌 + 缩写未定义（R2-W1, R1→AGREE）
6. **[AGREE] DocRED R² CI 宽**: n=35, CI [0.27, 0.73]（R1-W3, R2→AGREE）
7. **[AGREE] Few-shot 因果语言偏强**: prompt length confound 未排除（R1-W6, R2→AGREE with nuance）
8. **[AGREE] Effect size framing 已修复**: typical-batch 2.2pp 现在适当前置（R16-N3→resolved）
9. **[AGREE] Data contamination 已充分论证**: split-origin covariate + held-out validation + DocRED replication（R16-m5→resolved）

---

## Reviewer Divergence

以下问题两位 Reviewer 存在分歧：

1. **SCS/BCS 指标新颖性** [R2: critical, R1: REBUT]
   - R2：与 LLM-PEE metric 形式完全相同，novelty 完全依赖实验设计
   - R1：工程用途 (partitioning) vs 科学用途 (controlled measurement) 是合法区分；论文已在 §3 "SCS novelty" 段承认
   - **Director 判断**: R1 的区分有道理，但 Contribution 2 措辞确需调整。降级为 warning。

2. **Practical implications 严重性** [R2: critical, R1: qualified agree]
   - R2：empirical analysis paper 不提供 actionable insights 其价值受质疑
   - R1：诊断研究不应被 ARR H5/H6 惩罚；SDGD 失败诊断有方法论价值
   - **Director 判断**: 两人均认为 practical advice 薄弱是事实，分歧在严重性。列为 warning。

3. **"First controlled study" claim** [R2: warning overclaim, R1: REBUT 认为准确]
   - R2：LLM-PEE 也有 similarity-based 分组比较
   - R1：LLM-PEE 同时改变 count 和 BCS，未 isolate；本文 BCS-controlled 实验是真正 controlled isolation
   - **Director 判断**: R1 论点更有力。"First controlled study isolating count from confusability via stratified design" 是准确 claim，但建议加 "via stratified experimental design" 限定。

---

## Questions to Authors

1. RE 是否有移除/放松 constrained decoding 的 ablation？如果 BCS-accuracy 关系在 unconstrained/relaxed generation 下消失，核心 claim 是否需重新 scope？[R1-Q3, R2-Q1 共识]
2. Typical-batch gap 2.2pp (CI [0.4, 4.0]) 在实际部署中是否 meaningful？CI 下限 0.4pp 几乎为零。论文是否区分了 statistical significance 与 practical significance？[R1-Q1, R2-Q2 共识]
3. SCS 是否优于 string edit distance、WordNet path distance、same-parent indicator？[R1-W1, R2→AGREE]
4. NER batch-level null 是否可能由 exact-match metric confound 导致？relaxed matching 下 BCS-F1 是否可能恢复？[R1-Q2]
5. 对于 same-domain schemas（如 biomedical ontology），MAVEN centrality confound 是否意味着 BCS 完全不可用？[R1-Q5, R2-Q5]
6. SCS embedding 选择依赖先验知识（Few-NERD 用 Qwen3，其余用 MiniLM），这是否削弱 pre-hoc proxy 的实用性？[R2-Q4, R1→partial agree]

---

## Missing References

两位 Reviewer 共同建议补充：
- **Card et al. (2020)** "With Little Power Comes Great Responsibility" — NLP 中 effect size 和 power 分析方法论 [R1 提出, R2 AGREE]
- **Fei et al. (2024)** — event extraction 评测 [R2 提出, 延续 R16-m6]
- **Gillick et al. (2014)** "Context-Dependent Fine-Grained Entity Type Tagging" — supervised setting 中的 count-dependent degradation [R2 提出]
- Constrained vs. free-form decoding 对 IE 的实证比较文献 [R1 提出]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 2.5 | 2.5-3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| **Overall** | **3.5** | **3.0** | **3.0** |
| Confidence | 4 | 4 | 4 |

**综合判断依据**:

论文实验设计严谨（BCS-controlled stratification、within-pool control、TOST equivalence），统计报告规范，负面结果诚实有诊断价值，cross-model validation 充分（4 models）。这些优势使其成为一篇高质量的经验分析论文。

但三个结构性问题限制了评分：
1. **Scope 与证据不匹配**: 核心度量 BCS 的 batch-level 预测力仅限 RE constrained classification，Title 和 Abstract 暗示跨任务通用性。
2. **Constrained decoding 未被 disentangle**: enum constraint 可能是 BCS-accuracy 关系成立的必要条件，缺少 ablation 验证。如果确认为必要条件，论文 scope 进一步收窄至 "constrained-decoding RE" 场景。
3. **Practical impact 有限**: typical-batch gap 仅 2.2pp (CI [0.4, 4.0])，SCS/BCS 非新颖指标，schema decomposition 失败。actionable takeaways 薄弱。

**Overall 3.0 (Findings)** 反映：论文适合 Findings track——实验方法论有贡献，但 novelty + scope + practical impact 的组合不足以支撑主会议。

**升分路径 → 3.5-4.0 (Borderline Conference / Conference)**:
1. 提供 relaxed constrained decoding 的 RE ablation，证明 BCS 关系不依赖 enum constraint
2. 调整 TOST framing：主文报告三个 margin、弱化 "bounded association"
3. 提供 SCS vs simple baselines 对比数据
4. 增加具体 practical guidelines（BCS threshold、decision flowchart）
5. 调整 Title/Abstract scope

**降分风险 → 2.5 (Borderline Findings)**:
如果 unconstrained decoding 下 BCS-accuracy 关系消失，核心贡献降级为 "constrained decoding 下的 error channeling analysis"，scope 过窄。

---

## Detailed Comments

### Abstract (abstract.tex)
- 约 195 words, 信息密度过高, 8+ 数值
- BCS 未展开全称 "Batch Confusability Score"
- "To our knowledge, we present the first controlled study" 语法不自然（R1-m1）
- 建议: 减至 3-4 个关键数字, 先说 takeaway 再给数据支撑

### Introduction (introduction.tex)
- Findings (1)-(4) 含过多精确统计量 (TOST p=0.003, R²=0.22-0.53 等), 属 Results 内容
- Contribution 2 措辞容易被读为 metric novelty claim, 需与 LLM-PEE 显式区分
- Contribution 3 "task asymmetry" 未 qualify evaluation format confound

### Related Work (related_work.tex)
- 引用覆盖总体充分 (65 条, 无虚假引用)
- "SCS novelty" 段对与 LLM-PEE 的区分已到位，但可更明确
- 缺 Card et al. 2020 (power analysis), Fei et al. 2024, Gillick et al. 2014

### Experimental Setup (experimental_setup.tex)
- SCS 定义和实验设计描述清晰
- FewRel train+val 合并的 rationale 和 covariate 结果仅在 Appendix，主文应简要提及
- Embedding 选择 (MiniLM vs Qwen3) 的 ad hoc 性质需讨论

### Results (results.tex)
- Count curve 和 BCS-controlled 结果呈现清晰
- §5.3 Practical magnitude: typical-batch 2.2pp 已适当前置（R16-N3 已修复）
- §5.4: "bounded association" 措辞偏强, 需报告 ±1pp/±2pp TOST 并弱化
- §5.5 Centrality confound 分析是方法论亮点

### SDGD Section (sdgd_negative.tex)
- Merge amplification 诊断清晰有说服力
- Oracle routing vs practical routing 对比有信息量
- "Future directions" 三个方向偏泛，可展开为具体建议

### Discussion (discussion.tex)
- "Practical implications" 段过短 (2 句)，需扩展
- Constrained decoding caveat 仅以 "upper bounds" 一笔带过，需升级为显式 boundary condition
- Aggregation simulation 引用措辞需弱化

### Limitations (main.tex)
- 9 条 + multiple comparisons 讨论，极其详尽
- Item 3 (TOST + logit-scale) 过长，建议拆分
- 整体是论文的明显优势

### Checklist (checklist.tex)
- 认真填写, A4 诚实报告 AI assistant 使用
- B2 列出数据集 license
- 总体合格，无遗漏

### Format
- supplementary.tex 标题使用旧标题 "Schema-Induced Degradation"，需统一
- 附录 3 处 -ing 分词短语结尾 (lines 209, 219, 275)
- ACL template `\usepackage[review]{acl}` 正确; author Anonymous 正确