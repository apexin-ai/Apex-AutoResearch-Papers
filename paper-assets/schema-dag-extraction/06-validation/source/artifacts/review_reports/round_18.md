---
round: 18
overall_score: 3.0
timestamp: 2026-05-18T09:32:27.078887+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 18 审稿报告

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**目标 Venue**: EMNLP 2026 (ARR May 25 cycle) — Findings
**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量)
**流程**: Round 1 独立审稿 → 交叉分享 + 逐条回应 → 收敛汇总 (1 轮即收敛)

---

## Summary

本文研究 training-free LLM 信息抽取中 schema 复杂度如何预测性能退化，将退化分解为两个维度：type count (Dimension 1) 和 type confusability (Dimension 2)。通过 SCS/BCS 指标量化 confusability，在 FewRel、DocRED、Few-NERD、MAVEN 四个数据集上进行控制实验。核心发现：count 导致 recall 单调下降（主效应），confusability 导致 type substitution（RE 中 BCS 解释 22-53% batch 间 accuracy 方差），但 NER 无 batch 级信号。Schema decomposition (SDGD) 因 merge amplification (NER) 和 routing failure (RE) 而失败。

这是一篇方法论严谨的实证分析论文，统计分析水准在 NLP 领域属于高水平，但核心新颖性有限（SCS 指标与 LLM-PEE 形式相同），且最强发现的适用范围（RE + closed-set classification format）远窄于标题和 abstract 的暗示。

---

## Strengths

**S1. 实验设计的方法论贡献显著。** BCS-controlled 实验（固定 type count 仅变动 confusability）在 IE 领域尚属首次，within-pool analysis 控制 pool composition confound，cross-model validation 覆盖 4 个模型含 proprietary (Gemini 2.5 Flash)。[R1, R2 共识]

**S2. 统计方法论在 NLP 中属高水准。** TOST 等价性检验评估维度分离性、permutation test 比较跨 pool 斜率、bootstrap CI (B=10,000)、variance decomposition 区分 batch 与 seed 方差、partial correlation 控制 centrality confound。TOST sensitivity analysis (Appendix Table 5) 在多个 margin 上报告而非仅挑最有利的。[R1 highlight; R2 Soundness 4/5]

**S3. Negative results 诚实透明且有独立诊断价值。** SDGD 失败的诊断（NER: merge amplification 导致 precision collapse 0.563→0.210; RE: routing failure 因 constrained decoding 迫使 confident predictions, 73.4% instances 收到 3-5 个 sub-schema 的 positive predictions）。Oracle routing 实验 (Table 3: 0.802 vs 0.504) 清晰定位瓶颈在 routing 而非 partitioning。[R1, R2 共识]

**S4. Limitations 极其全面诚实。** 10 条 limitations 预先回应了几乎所有潜在批评（单种子、logit-scale TOST inconclusive、causal mechanism、unconstrained decoding 缺失、data contamination 等），远超多数论文的 Limitations 质量。[R1, R2 共识]

**S5. Centrality confound 处理出色。** MAVEN 的 positive raw correlation 异常 → 诊断 embedding collapse → partial correlation 控制 log frequency + degree centrality → 正相关消失。方法论案例价值独立于论文主线。[R1 highlight]

**S6. 跨模型验证覆盖面广。** Dimension 1 在 Qwen3-32B、LLaMA-8B/70B、Gemini 2.5 Flash 上均得到验证，RE count curve 斜率近乎一致 (70B: -30.7pp vs 32B: -30.1pp)。[R1, R2 共识]

---

## Weaknesses

### Must-Fix (3 项, 影响接收决定)

**N1 [critical, R1+R2 共识] BCS batch-level 效应仅限 RE closed-set classification format，但 title/abstract 暗示跨任务普适性。**
- NER: batch-level r≈0, n=450 (§4.4)
- ED (MAVEN): positive correlation（方向相反），控制 confounders 后消失 (§4.5)
- RE: BCS R²=22-53% 仅在 constrained decoding + closed-set classification 下验证
- 关键精确化 [R2 提出, R1 交叉同意]: NER 也使用 constrained decoding (JSON schema with enum types)，但 BCS 在 NER 上无信号。因此 boundary condition 不是 "constrained decoding" 而是 "closed-set single-label classification format"（RE 的错误必然是 intra-batch type substitution；NER 的错误分散在 boundary errors、missed entities、spurious entities 等多模式）。论文 Discussion §6 已有类似分析但术语 "constrained decoding" 不精确。
- **行动**: Title 可保持但 Abstract 必须加 scope qualifier；Discussion/Conclusion 精确区分 constrained decoding vs closed-set classification format；Contribution 3 加 evaluation format qualification。

**N2 [critical, R1+R2 共识] "Two separable dimensions" 的 claim 在 logit-scale 上 inconclusive。**
- TOST: ±3pp 显著 (p=0.003), ±1pp inconclusive (p=0.278)
- Logit-scale TOST: inconclusive (p=0.209); logit-scale interaction marginally significant (p=0.047)
- 交互效应 90% CI [−1.0, 2.0]pp，上界 2.0pp 接近主效应 2.2pp 的 91%
- Introduction "Degradation operates along two dimensions" 与 Results "bounded association" 存在措辞不一致
- **行动**: Introduction 改为更审慎表述如 "largely additive with bounded interaction"；全文统一措辞；logit-scale 结果在正文提及而非仅 appendix。

**N3 [critical, R2 提出, R1 partially agree] Novelty claim 需更诚实定位。**
- SCS/BCS 与 LLM-PEE 的 embedding similarity 形式完全相同（论文 §2 自己承认）
- "Two-dimensional degradation" 框架是对已知现象（count-dependent degradation [Li et al. 2023]、embedding similarity partitioning [LLM-PEE 2025]）的系统化命名
- **分歧**: R2 认为框架是 "confirmation not discovery" (Excitement 2.5/5)；R1 rebut 认为 experimental methodology (BCS-controlled design + TOST + within-pool analysis) 构成实质贡献，从 engineering tool 到 analytical instrument 的转变不 trivial
- **共识**: Contribution 2 措辞 "we repurpose it as a predictive metric" 暗示指标层面创新，需修改
- **行动**: Contribution 2 改为 "Building on the embedding-similarity criterion used for schema partitioning in prior work, we design controlled experiments that quantify its predictive relationship with extraction degradation..."

### Should-Fix (8 项, 影响评分但不一票否决)

**W1 [warning, R1+R2 共识] Abstract 信息过载。** 217 词塞入过多技术细节，读如 Results 压缩版而非 compelling story。核心问题是叙事结构：应先给 high-level takeaway 再选择性展开。R2 升为 critical，R1 同意但降为 should-fix（理由：多任务论文天然需要 nuance）。

**W2 [warning, R1+R2 共识] Pairwise effect size (r²=1.3-1.7%) 解释过于乐观。** Cohen (1988) behavioral research 标准套用到 LLM 系统的 type-pair confusion 需额外论证。注：R1 将 pair-to-batch aggregation 定性为 "依赖 simulation"，R2 正确指出这是误读——batch R²=22% 是 §4.3 中 100 个 random batches 的直接 OLS 回归结果，simulation (Appendix F) 仅为 illustrative model（论文首句明确声明）。

**W3 [warning, R1+R2 共识] Typical-batch 效应量 (2.2pp, CI [0.4, 4.0]) 实际意义有限。** 加上 SDGD 失败、confusability-aware grouping 无显著优势 (+1.4pp, p≈0.19)、few-shot 无法缩小 gap (+4.3pp widening)，实际可操作的 practical implications 薄弱。

**W4 [warning, R2 提出, R1 partially agree] 不同数据集使用不同 embedding。** Few-NERD 用 Qwen3（extraction model 自身），其他用 MiniLM。损害 SCS 作为 "lightweight pre-hoc proxy" 的通用性。Cross-check 显示 MiniLM 在 Few-NERD 上 r=0.172 > Qwen3 r=0.138，说明 overfitting 不成立但加剧不一致性。

**W5 [warning, R1 提出, R2 agree] Dimension 2 在 proprietary model 上未验证。** Gemini 2.5 Flash 仅验证了 Dimension 1；Dimension 2 (BCS-controlled) 在开源模型 (Qwen3-32B, LLaMA-8B/70B) 上验证。跨模型证据不对称。

**W6 [warning, R1 提出, R2 agree] NER U-shape rebound 的 "dual-task burden" 假说缺乏直接实验证据。** U-shape 在 LLaMA-70B 上复现排除模型特异性，但机制仍属推测。

**W7 [warning, R1 提出, R2 agree] Confusability-aware grouping 无显著优势。** Oracle routing 下 graph coloring 仅比 random +1.4pp (p≈0.19, n.s.)。与 BCS R²=22-53% 的预测力形成张力——如果 BCS 解释如此多方差，为什么 BCS-aware grouping 不改善？可能解释：graph coloring 降低 mean BCS 但未充分降低 max BCS。

**W8 [warning, R2 提出, R1 agree] 页数可能超限。** Conclusion 出现在第 9 页，Long paper 限 8 页正文。需编译后精确验证。

---

## Reviewer Consensus

以下问题两位 Reviewer 在交叉分享后达成共识 [AGREE]：

1. **BCS 适用范围** [N1]: Batch-level 预测力仅限 RE closed-set classification，NER 和 MAVEN 上无效或被 confound。标题/abstract 需 narrower scope。
2. **TOST margin** [N2]: "Separable dimensions" 过强，应改为 "largely additive with bounded interaction"。
3. **Typical-batch 效应量** [W3]: 2.2pp 的实际意义有限，practical implications 需更坦诚。
4. **Dimension 2 跨模型 gap** [W5]: 未在 proprietary model 上验证。
5. **U-shape 机制** [W6]: 缺乏直接实验证据。
6. **BCS-aware grouping 无优势** [W7]: 削弱 BCS 实践价值。
7. **Missing references** [m3]: Chen et al. (2026) 和 Wei et al. (2023) 应引用。

## Reviewer Divergence

1. **R1-N1 严重性 [pair-to-batch aggregation]**: R1 定为 critical（aggregation 依赖 simulation），R2 rebut 指出 batch R²=22% 是直接回归测量值非 simulation 推导（论文 Appendix F 首句明确声明）。R2 的论据更准确——N1 应从 critical 降为 warning（已反映在 W2 中）。
2. **Novelty 评估** [N3]: R2 认为框架是 "confirmation not discovery"；R1 认为 experimental methodology (BCS-controlled + TOST + within-pool) 构成实质贡献。共识：指标不新，methodology 有贡献，Contribution 2 措辞需修改。
3. **Contribution 3 framing** [R2-W3 vs R1 rebut]: R2 认为 NER null result 不应 framed 为 contribution；R1 rebut 认为 task asymmetry 本身有信息量（对 NER practitioners 的指导意义、error channeling hypothesis 的推动）。此分歧未解决，记录在案。
4. **Overall score**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)。差异主要在 Excitement (R1: 3.0 vs R2: 2.5) 和对 methodology contribution 价值的判断。

---

## Questions (需作者澄清)

**Q1 [R1+R2 共识, 优先级最高]**: 为什么不对 RE 进行 unconstrained decoding ablation？这是验证 "error channeling hypothesis" 最直接的实验，比添加新模型更容易实现。如果 BCS-accuracy association 在 unconstrained decoding 下消失，论文的 batch-level 发现需被限定为 constrained-decoding-specific。

**Q2 [R2 提出]**: 真正的 boundary condition 是 constrained decoding 还是 closed-set single-label classification format？请精确区分——NER 也用了 constrained decoding 但 BCS 无信号。

**Q3 [R1 提出]**: Few-NERD 使用 extraction model 自身的 embedding (Qwen3) 计算 SCS，如果 SCS 旨在作为 "lightweight pre-hoc proxy"，embedding 选择不应依赖对任务特性的先验知识。这是否构成 overfitting-to-the-metric 的风险？

**Q4 [R2 提出]**: Few-shot 实验中 prompt length 是否被控制？5-shot 下 low-BCS accuracy 下降 (0.754→0.715) 是否因 lost-in-middle effect 而非 confusability？

**Q5 [R1 提出]**: Confusability-aware grouping (graph coloring) 相对 random 无显著优势 (+1.4pp, p≈0.19)，但 BCS 解释 22% variance。如何解释这一矛盾？

---

## Missing References

1. **Chen et al. (2026)**, "Understanding LLM Performance Degradation in Multi-Instance Processing" (arXiv:2603.22608) — 与 Dimension 1 (count-related decline) 直接相关 [R2 提出, R1 同意]
2. **Wei et al. (2023)**, "Zero-Shot Information Extraction via Chatting with ChatGPT" — LLM zero-shot IE 的直接前驱工作 [R1 提出, R2 同意]
3. **Schall & de Melo (2025)** 已引用但讨论不足 — constrained decoding 对 model distribution 的扭曲机制对解释 RE vs NER BCS asymmetry 有帮助 [R2 提出]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**评分理由**:

*Soundness (3.75/5)*: 实验设计和统计方法论在 NLP 领域属高水准（BCS-controlled experiments、TOST equivalence、within-pool analysis、partial correlation、variance decomposition）。扣分点：pairwise r²=1.3-1.7% 效应量小；logit-scale TOST inconclusive 削弱 "separable dimensions" claim；BCS batch-level 效应仅限 RE。

*Excitement (2.5/5)*: 研究问题有价值（首次通过 controlled stratification 隔离 count vs confusability），negative results 有诊断意义。但 SCS/BCS 指标与 LLM-PEE 形式相同，"两维度"框架是对已知现象的系统化命名而非新发现。Typical-batch 效应量有限 (2.2pp)，无可行 mitigation 方案（SDGD 失败、few-shot 无效），实践指导薄弱。核心发现适用范围 (RE + closed-set classification) 窄于 framing 暗示。

*Reproducibility (4/5)*: 实验细节充分（decoding parameters、seed、batch 构造、prompt templates 完整公开）。Anonymous review materials 链接已提供。代码承诺 acceptance 后释放。单 GPU 推理 (~72 GPU-hours)。扣分：单种子评估。

**置信度**: 4/5。两位 Reviewer 均仔细阅读全文及所有 appendix，熟悉 IE、statistical methodology、LLM prompting 相关文献。交叉分享后关键问题达成共识。

**一句话总结**: 方法论严谨的实证分析论文，统计分析水准高，negative results 有诊断价值，但核心新颖性有限（SCS 与 LLM-PEE 形式相同），BCS batch-level 预测力仅限 RE closed-set classification format，typical-batch 效应量 (2.2pp) 和实践影响力有限。达到 Findings 水平。

**如需上调至 3.5 (Borderline Conference)**，需：(a) Abstract 重写为 story-driven 而非 data-dump；(b) 精确化 boundary condition 为 closed-set classification format 而非 constrained decoding；(c) 统一 "bounded interaction" 措辞；(d) 补充 unconstrained RE decoding ablation。

---

## Detailed Comments (逐节)

### Abstract
- 217 词信息过密，试图覆盖所有发现。应聚焦 1-2 个最强发现 + clear "so what"。
- "identifying confusability as a schema-structural constraint" 含 -ing 分词结尾 (AI 写作标志)。

### Introduction
- "Degradation operates along two dimensions" 暗示强分离性，与 §4.4 的 "bounded association" 不一致。
- Contribution 2 "we repurpose it as a predictive metric" 暗示指标创新，需改为 methodology contribution。
- Contribution 3 (task asymmetry) framing 存在分歧：R2 认为是 limitation 包装为 contribution，R1 rebut 认为有独立信息量。

### Related Work
- §2 "SCS novelty" 段已诚实承认与 LLM-PEE 的关系，但 Introduction 的 contribution 列表未充分反映这一诚实度。
- 缺 Chen et al. (2026) 和 Wei et al. (2023)。引用数量 (~46) 对覆盖 NER/RE/ED + schema complexity + constrained decoding 多个子领域偏少。

### Experimental Setup
- 不同数据集使用不同 embedding 损害 SCS 通用性。建议统一 MiniLM 为 primary。
- Table 1 BCS Range 列跨数据集不可比（不同 embeddings），caption 未说明。

### Results
- §4.3 Practical magnitude: typical-batch 2.2pp 与 extreme-batch 31.2pp 的对比需更显著。
- §4.4 TOST: logit-scale 结果应在正文提及（目前仅 appendix）。

### SDGD (§5)
- BCS-aware grouping 无显著优势 (+1.4pp) 与 BCS R²=22-53% 的张力需要解释。

### Discussion
- "constrained decoding" 术语不精确，应改为 "closed-set classification format"。
- Practical implications 用 extreme-batch 结果 frame，对 typical-batch 2.2pp 讨论不足。

### Format
- 正文可能超 8 页限制。需编译验证并压缩。
- Checklist A4 AI 辅助声明过于笼统。