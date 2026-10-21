---
round: 16
overall_score: 3.0
timestamp: 2026-05-18T07:20:12.078317+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 16 (Fresh Review)

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**目标 venue**: EMNLP 2026 via ARR May 2026
**截止日期**: 2026-05-25
**Reviewer 编排**: 2 人 (R1: 方法严谨性+统计分析; R2: 新颖性+写作+格式)
**审稿模式**: Fresh review (Round 16), 1 轮独立审稿 + 1 轮交叉回应

---

## Summary

本文研究 training-free LLM 信息抽取中 schema 复杂度对性能的影响，将退化分解为两个维度：type count（数量导致 recall 下降）和 type confusability（语义相似度导致 type substitution）。提出 SCS/BCS 指标量化 confusability，在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）、3 个任务（NER, RE, ED）、4 个模型上进行控制实验。核心发现：count 是主导退化因素（最高 -49pp）；confusability 在 RE batch 级有预测力（R²=0.22-0.53），但典型场景效应仅 2.2pp，且在 NER batch 级无信号；schema decomposition（SDGD）因 merge amplification 和 routing failure 失败。

---

## Strengths

**S1. 实验设计精良**。BCS-controlled 实验通过固定 count 变化 BCS 隔离 confusability 效应，within-pool 分析控制 pool composition confound（permutation p=0.60），FewRel 平衡设计排除 type frequency 混杂。设计远超同领域平均水平。[R1 S1, R2 S1, 交叉共识]

**S2. 跨模型验证充分**。Dimension 1 在 4 个模型上复现（8B-70B + Gemini Flash），包含一个 proprietary model。Dimension 2 在 Qwen3-32B, Llama-8B, Llama-70B 上验证。[R1 S3, R2 S2]

**S3. 负面结果报告有深度**。SDGD 失败不是简单的"不 work"：merge amplification 的机制诊断（precision 0.563→0.210）、oracle routing headroom 量化（+29.8pp）、routing failure 归因（constrained decoding 下 confidence 不可比）均有独立分析价值。[R1 S2, R2 S3, 交叉共识]

**S4. 统计方法学全面**。TOST 等价性检验、bootstrap CIs（B=10,000）、cluster bootstrap、Jonckheere-Terpstra 趋势检验、permutation tests、partial correlation、cross-seed variance decomposition——方法选择恰当，透明度高。[R1 S4, R2 S1]

**S5. Limitations section 堪称范例**。10 条 limitation + multiple comparisons 讨论，每条有量化支撑（logit-scale power analysis、MDE 计算等），自我批判深度在 NLP 论文中罕见。[R1 S5, R2 S4]

**S6. 引用完整**。63 篇引用全部验证通过，0 orphan/missing，覆盖直接相关方法、baseline、benchmark、理论基础和统计方法。[R2 S5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [CRITICAL] — Scope 过宽：title/abstract 暗示跨任务泛化，但 BCS batch-level 预测力仅限 RE constrained classification。** [R1 N1 + R2 W6, 交叉完全共识]

BCS 解释 RE 22-53% cross-batch accuracy variance（FewRel R²=0.218, DocRED R²=0.525），但：NER batch-level r≈0 (n=450, §4.4)；MAVEN 因 centrality confound 需剔除 (§4.5)；Dimension 2 跨模型验证仅限 open-weight 模型。三个 task 中仅 RE（且是 constrained enum classification）给出强 batch-level signal。标题 "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?" 暗示通用结论，与实际发现不匹配。

**N2 [CRITICAL] — TOST ±3pp margin > typical main effect (2.2pp)，"bounded association" claim 被削弱。** [R1 N2 critical + R2 交叉 AGREE]

±3pp margin 意味着 >130% amplification of main effect 仍被判 "equivalent"。±2pp 下仅 marginally equivalent (p=0.047)；±1pp inconclusive (p=0.278)。Logit-scale TOST inconclusive (p=0.209)，论文以 "insufficient power" 解释，但将其降为 sensitivity check 不够充分——当 accuracy 接近 50% 时 linear scale 压缩效应，logit scale 更适合 bounded data。"bounded association" 是论文核心叙事支柱（Introduction finding (1)），margin 选择使 claim 变得 trivially satisfiable。

R2 补充：论文 Appendix C 的三重 anchoring 和 sensitivity table 比表面呈现更完整（交互点估计仅 0.47pp, 90% CI [-1.0, 2.0]pp），但主文叙事不够反映 logit-scale 不确定性。

**N3 [CRITICAL] — 效应量报告 framing 偏误。** [R2 W1 critical + R1 W4 major]

论文在显著位置（Abstract、Figure 1b、§4.3 标题）反复强调 extreme-batch gaps（-31.2pp, -25.5pp），而 typical-batch effect（2.2pp, quartile gap 3.9-5.3pp）被放在 §4.3 的一个 paragraph 中。Extreme batches 是人为构造的最大对比条件，不代表实际部署场景。

R1 补充：但需区分 pairwise r²=1.3% 和 batch-level R²=0.22-0.53——后者是实质性的，R2 的批评过度集中于 pairwise r² 而忽视了 batch-level evidence。

### Should-Fix（影响评分但不一票否决）

**W1 [MAJOR] — SCS 缺乏与简单 baseline metrics 的对比。** [R1 W1 + R2 交叉 AGREE]

未与 string overlap、WordNet distance、same-parent category binary variable 等简单 proxy 比较。Few-NERD 有明确的 8 大类层级结构，如果 same-parent membership 就能解释类似比例的 confusion variance，SCS 的增量价值有限。论文在 Appendix G 仅做了 SCS 内部变体比较（name vs name+definition），不是 qualitatively different baselines 的对比。

**W2 [MAJOR] — "First controlled study" claim 需弱化。** [R2 W2 critical, R1 REBUT → 分歧但共识弱化措辞]

SCS 与 LLM-PEE 的 partitioning criterion 形式相同（论文自认）。R1 认为 engineering (LLM-PEE) vs controlled analysis (本文) 的区分合法；R2 认为当 finding 效应量 modest 且 metric 相同时 "first" 显得 overclaimed。双方同意措辞应弱化为 "the first study that systematically disentangles..." 或类似表述。

**W3 [MAJOR] — 论文定位模糊，缺乏 actionable insights。** [R2 W3 + R1 交叉 AGREE]

作为纯 empirical analysis paper（无新方法/模型/数据集），Discussion §practical implications 仅两句话。Finding 1 confirmatory, Finding 2 效应小且 NER 无效, Finding 3 属 robustness check, Finding 4 negative result。未提供 schema design decision framework（BCS 阈值、type pool 设计原则）。

R1 部分反驳：Finding 2 的量化本身有价值——"similar types are confusable" 是直觉，但效应量、pair-to-batch 传导机制、task asymmetry 不是领域知识能预测的。

**W4 [MAJOR] — Abstract 过度压缩。** [R2 W4 + R1 交叉 AGREE]

~180 words 含 SCS、BCS、SDGD 三个缩写（BCS 和 SDGD 未在 Abstract 内定义）和 8+ 数值。嵌套括号注释（"confusability operates at the pair level...only in RE"）在 Abstract 中不合适。

**W5 [MAJOR] — Introduction findings 段统计量过密。** [R2 W5 + R1 交叉 AGREE]

§1 findings (1)-(4) 含 TOST p=0.003, R²=0.22-0.53, CI [0.27, 0.73], +1.4pp p≈0.19 等。这些属于 Results，不属于 Introduction。

**W6 [MAJOR] — Constrained decoding 可能人为放大 BCS 的 RE 效应。** [R1 Q2 + R2 Q1, 交叉完全共识]

Constrained decoding 将所有 non-none errors 强制导向 intra-batch substitution，BCS 的预测对象本身被实验设计放大。Discussion §task-dependent effects 有 "upper bounds" caveat 但不够显著。是论文 generalizability 最大 threat。未在 unconstrained decoding 条件下验证。

### Minor（不影响接收）

**W7** [MINOR] Few-shot "confusability gap widens" 结论过强——仅 3 data points，5-shot 降回可能是 prompt length artifact。[R1 W5 + R2 交叉 AGREE]

**W8** [MINOR] NER U-shape "dual-task burden" 解释是 post-hoc 推测，缺直接验证。[R1 W6 + R2 交叉 AGREE]

**W9** [MINOR] "Notably" (results.tex:49) 是 AI 写作标志词。[R2 W8 + R1 交叉 AGREE]

**W10** [MINOR] Contribution 3 将 NER null result 包装为 "discovery"，但实质是 limitation；且 task asymmetry 可能由 evaluation format 驱动而非 task 本身。[R2 W9 + R1 交叉 AGREE]

**W11** [MINOR] 16-relation BCS-controlled 条件仅 single extreme batch, 无 CI。核心证据不依赖此，但应标注 pilot。[R1 W2 + R2 交叉 AGREE]

---

## Reviewer Consensus [AGREE]

1. **Scope 过宽**：BCS batch-level prediction 仅 RE 有效，title/abstract 的泛化暗示不匹配。[R1 N1 + R2 W6, 双向 AGREE]
2. **TOST margin 问题**：±3pp > 2.2pp main effect；logit-scale inconclusive 应更受重视。[R1 N2, R2 AGREE with nuance]
3. **效应量 framing**：extreme-batch gaps 前置、typical 2.2pp 后置构成 framing 偏误。[R2 W1, R1 部分 AGREE (batch R²≠pairwise r²)]
4. **SCS baseline 缺失**：缺与 string/ontological baselines 对比。[R1 W1 + R2 AGREE]
5. **Abstract/Intro 过密**：数字和统计量堆砌。[R2 W4+W5, R1 AGREE]
6. **Practical implications 不足**：Discussion 缺 actionable guidance。[R2 W3, R1 AGREE]
7. **Constrained decoding confound**：RE 效应可能被 format 放大。[R1 Q2 + R2 Q1, 双向 AGREE]
8. **Few-shot widening 过强**：仅 3 points，prompt length confound。[R1 W5 + R2 AGREE]
9. **NER U-shape 缺验证**：post-hoc hypothesis。[R1 W6 + R2 AGREE]
10. **"Notably" AI marker**：trivial fix。[R2 W8 + R1 AGREE]

## Reviewer Divergence [REBUT areas]

1. **"First controlled study" claim**：R1 REBUT R2 W2——engineering (LLM-PEE) vs controlled analysis (本文) 是合法区分。R2 坚持 metric 相同时 "first" overclaimed。**共识**：措辞弱化，但区分本身成立。

2. **FewRel 数据污染**：R1 W3 (major concern)；R2 交叉 REBUT——论文多层防线（反事实方向、单调退化、slope 一致性、split-origin covariate、DocRED 复制）充分。**共识**：论证合理但永远无法完全排除；当前水平在同类论文中已属充分。

3. **Batch-level R² vs Pairwise r²**：R2 聚焦 pairwise r²=1.3% 批评 novelty 不足；R1 指出 batch-level R²=0.22-0.53 是实质性的。**共识**：论文应更清晰区分两个层级，以 batch-level R² 为主证据。

4. **评分**：R1 = 3.5 (Borderline Conference)，R2 = 3.0 (Findings)。分歧在 Excitement（R1: 3.0 vs R2: 2.5）和对负面结果独立价值的评估。R1 认为方法学质量和 negative results 诊断深度值得 higher credit；R2 认为 confirmatory findings + modest effect size 限制了 impact。

---

## Questions（需要作者澄清）

1. **Constrained decoding confound**: 如果 RE 使用开放式生成（类似 NER），BCS 是否仍有 batch-level predictive power？这决定了 Dimension 2 是 "task-general" 还是 "format-specific"。[R1 Q2 + R2 Q1, 双方最关注的问题]

2. **Extreme batch 构造方法**: 通过 exhaustive enumeration、optimization search 还是 heuristic？如果是 optimization-based，是否可能在 type difficulty 上也不平衡？[R1 Q1, R2 AGREE]

3. **Few-NERD centrality control**: 论文对 MAVEN 做了完整的 partial correlation 分析（Appendix E），但 Few-NERD 未报告相同的 multi-confounder partial analysis（仅报告 ρ=-0.293, p=0.02）。[R1 Q3, R2 REBUT 部分]

4. **NER U-shape 为什么 RE 没有类似 rebound**: RE 在 count 80 时是否也存在 "full schema = no filtering" 效应？[R2 Q3, R1 AGREE]

5. **Intervention 方案**: 除 label renaming 外，是否考虑过 adding disambiguating definitions、type reordering、hierarchical two-stage classification？至少一个 successful intervention 会大幅增强 practical contribution。[R1 Q4, R2 AGREE]

---

## Missing References

以下引用经交叉讨论后建议补充：

1. **Tam et al. (2024) "Let Me Speak Freely?"** — constrained decoding 对 LLM error distribution 的影响。[R1 提出, R2 AGREE: 高度相关]
2. **Yin et al. (2019) "Benchmarking Zero-shot Text Classification"** — label embedding similarity 在 zero-shot 中的应用，SCS 的直接前身。[R1 提出, R2 AGREE]
3. **Fei et al. (NAACL 2024) "Quantifying and Mitigating Label Bias in LLMs"** — label bias 作为潜在 confound。[R2 提出, R1 AGREE: supplementary]
4. **Zhao et al. (2025) "Label-Guided In-Context Learning for NER"** — 与 few-shot findings 相关。[R2 提出, R1 AGREE: optional]

---

## External Review (Stanford Agentic Reviewer)

未启用（项目配置 `external_review.paperreview_ai.enabled: false`）。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**评分区间**: R1 = 3.5 (Borderline Conference)，R2 = 3.0 (Findings)。综合评估取 3.0-3.5 range 的保守端。

**核心理由**:

（+）实验方法学在 LLM IE 分析论文中属上乘，BCS-controlled + within-pool + cross-model + cross-prompt 的验证框架可作为方法论模板。

（+）SDGD 负面结果的诊断深度（merge amplification mechanism, oracle routing headroom）对 decompose-then-merge paradigm 有广泛 cautionary value。

（+）Limitations section 的深度和统计透明度是 gold standard。

（-）核心 Dimension 2 的 batch-level 预测力仅限 RE constrained classification，NER 和 ED 均为 null/confounded，论文标题和 abstract 的泛化暗示不匹配——这是最严重的问题。

（-）Typical-batch 效应量仅 2.2pp（CI [0.4, 4.0]），在工程实践中几乎不可操作；pairwise r²=1.3% 过小；"bounded association" 的 TOST 证据在 logit scale 上 inconclusive。

（-）SCS 与 LLM-PEE 的 metric 形式相同，缺乏与简单 baseline 的对比，作为 named contribution 的增量价值未充分证明。

（-）纯分析论文缺乏 actionable insights——SDGD 失败后无 mitigation solution，Discussion practical implications 极薄。

**置信度**: 4/5

**提升路径**（可达 3.5 Borderline Conference）:
1. 解决 scope（title/abstract RE-specificity 限定 + constrained decoding caveat 显著化）
2. 加入 SCS vs simple baseline 对比
3. Discussion 增加 actionable schema design guidelines
4. TOST margin 讨论与 logit-scale 结果并列呈现
5. Abstract/Introduction 信息密度降低，typical effect 前置

---

## Detailed Comments（逐节）

### Abstract
~180 words，长度合规。四个必答问题均覆盖。但信息密度过高：BCS 和 SDGD 未定义；8+ 数值堆砌；嵌套括号注释不合适。应首先说清 takeaway（"confusability is a real but minor factor; count dominates"），减少至 2-3 个关键数字，删除括号注释。

### Introduction
叙事结构完整（background → gap → this study → findings → contributions），开头切入具体问题避免了泛泛介绍。但 findings (1)-(4) 统计量过密（TOST p-value, R² 精确值），应改为定性描述。Contribution list 四条均有 section reference，合规。Contribution 3 将 NER null 包装为 "discovery" 需 reframe。

### Related Work
结构清晰，五段覆盖主要方向。与 LLM-PEE 的差异化清晰（analysis vs engineering）。"SCS novelty" 段诚实承认形式共享但强调 framework 贡献。建议补充 label bias 文献线。

### Experimental Setup
数据集描述完整，Table 1 自包含。SCS/BCS 定义清晰。两个实验范式设计合理。SCS validation paragraph 有效。MiniLM vs Qwen3 选择有理有据。

### Results
§4.1 Count curves：结果清晰，cross-seed validation 和 trend analysis 充分。
§4.2 Pairwise：r² 极小，论文诚实但辩护（Cohen 1988 类比）NLP 语境下不足。
§4.3 BCS-controlled：核心实验设计严谨。within-pool 分析是亮点。但 typical magnitude (2.2pp) 出现位置太靠后，应前置。
§4.4 Multi-dimensional：Error taxonomy 有价值。TOST "bounded association" 是论文最脆弱的 claim——logit-scale 不确定性需更显著呈现。
§4.5 Centrality confound：分析到位，是重要的 self-correction。

### SDGD Negative Results (§5)
论文最有价值的 section。Merge amplification 诊断清晰，oracle routing headroom 量化有力，future directions 具体。

### Discussion
偏短。Task-dependent effects 和 mechanism explanation 到位。Practical implications 极薄（仅两句话）——对 analysis paper 而言不够。Conclusion 与 Discussion 合并，略显仓促。

### Limitations
堪称范例。特别赞赏 logit-scale TOST 不确定性的坦诚讨论（item 3）、data contamination 的多层防线（item 9）、NER metric 局限性（item 6）。

### Checklist
认真填写，每项有 section reference 或合理 N/A justification。AI assistant usage 已声明。

### 格式合规
- `\usepackage[review]{acl}` ✓
- `\author{Anonymous}` ✓
- anonymous.4open.science 链接 ✓
- Limitations section 存在 ✓
- Responsible NLP checklist 存在且认真填写 ✓
- 无 em-dash（一处 "Notably" 标志词待删除）
- 页数：未编译确认，内容量接近 8 页上限