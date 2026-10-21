---
round: 10
overall_score: borderline
timestamp: 2026-05-17T07:46:59.626672+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 10 审稿报告 — schema-dag-extraction

**Target Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**Reviewers**: R1 (方法严谨性 + 统计推断), R2 (新颖性 + 写作 + 格式)
**Submission date**: 2026-05-17

---

## Summary

本文对 training-free LLM 信息抽取中的 schema-induced degradation 进行了系统性实证研究，通过 stratified experimental design 将 type count 和 type confusability 两个因素隔离分析。在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）上进行了 count curves 和 BCS-controlled 实验，发现 count 效应主导（~20× larger than confusability in typical batches），confusability 的 typical-batch gap 仅 2.2pp。同时报告了 schema decomposition 的全面失败（NER merge amplification + RE routing failure）。

---

## Strengths

1. **实验设计卓越**：两个互补 paradigm（count curves 固定 confusability 随机化、BCS-controlled 固定 count 变化 confusability）的 factorial 思想在 NLP empirical work 中罕见，远超同类论文的 evaluation rigor。[R1, R2 共识]

2. **Confound reasoning 典范级**：centrality confound (MAVEN)、type frequency (NER batch-level)、pool composition (within-pool analysis)、split-origin (contamination) 每个 confound 都有 dedicated analysis 和 appropriate statistical control。[R1]

3. **负面结果的诚实诊断**：SDGD failure + routing failure 的 mechanistic diagnosis（merge amplification: precision 0.56→0.21; constrained decoding 消除 confidence signal）为后续研究提供了精确的 negative knowledge。[R1, R2 共识]

4. **统计方法多元适当**：bootstrap CI (pair/batch level)、permutation tests、TOST equivalence、variance decomposition、cluster bootstrap——方法选择与数据结构匹配。[R1, R2 共识]

5. **效应量的诚实报告**：不 inflate extreme-batch 31.2pp gap，honest 报告 typical 2.2pp effect——学术透明度在 NLP 论文中罕见。[R1, R2 共识]

6. **跨条件 robustness 全面**：4 datasets × 2 models × 4+ prompt variants × within/cross-pool comparison。[R1, R2 共识]

---

## Weaknesses

### Critical (Must-Fix)

**C1. 因果语言超出证据边界** [R1 N3 + R2 AGREE with qualification]
- Title "shape" 暗示因果；正文 "driven"、"channels"、"bounded interaction" 暗示 mechanistic independence
- Limitations item 7 自己承认 "correlational evidence...does not establish interventional causality"
- R2 补充：BCS-controlled 是 quasi-experimental design（deliberate manipulation），非纯观察；但 Title/正文 framing 仍过强
- **修改要求**：'driven' → 'predicted by'/'associated with'；'channels' → 'dimensions'/'components'；Introduction 明确 predictive framework

**C2. 聚合推理链叙事误导** [R1 N1 + R2 AGREE with nuance]
- §4.3 从 pairwise r²=1.3-1.7% → conditional R²=7% → batch R²=22% 的推理暗示因果中介
- Unconditional simulation 仅产出 R²=0.044，与观测 0.218 有 5× gap
- **两人共识**：batch R²=0.218 有独立实证支撑（direct OLS on 100 batches），但叙事链条让读者误以为 pairwise 信号"解释了"batch-level 效应
- **修改要求**：明确区分 "observational finding (R²=0.218)" 与 "post-hoc explanatory model (simulation)"；删除暗示中介因果的措辞

**C3. TOST margin justification 不足** [R1 N2; R2 REBUT on "三测两败" but AGREE on margin anchoring]
- ±3pp margin 的理由（"130% amplification"）是 arbitrary judgment call，缺乏 external standard
- **分歧**：R1 认为 "三个 test 两个失败" 构成 evidence pattern against bounded interaction；R2 反驳认为 primary test (n=69) passed，2×2 factorial 是 underpowered sensitivity check ≠ failure
- **共识**：margin 需要更透明的 external anchoring；Contribution #1 措辞应限定为 "RE shows bounded interaction" 而非暗示 general principle
- **修改要求**：Appendix C 加入 Lakens (2017) SESOI framework；明确 2×2 factorial 的 sensitivity check 定位；弱化 generality claim

**C4. SCS Contribution #2 framing 暗示 metric novelty** [R2 N1 + R1 AGREE with nuance]
- 论文已承认 SCS 与 LLM-PEE 形式相同，但 Abstract/Contribution #2 措辞让读者误以为 metric 本身是贡献
- 真正增量是 controlled experimental evidence proving predictive relationship
- **修改要求**：Contribution #2 → "First controlled validation that embedding similarity predicts type confusion in zero-shot IE"；Abstract 明确 "empirical validation under controlled conditions"

### Warning (Should-Fix)

**W1. `\enlargethispage*{9\baselineskip}` 页面操纵** [R2 W3 + R1 强 AGREE]
- 实质多出 ~1/4 页空间，可能被视为 format violation
- **修改要求**：删除此命令，压缩 §5 或移部分到 appendix

**W2. Negative results 缺乏 constructive resolution** [R2 N3 + R1 AGREE partially]
- ~1.5 页报告失败但只有一句 future direction
- **修改要求**：§5 末尾或 Discussion 扩展 2-3 个具体方向（two-stage pipeline, retrieval-based routing, calibrated confidence estimation）

**W3. Abstract 数字密度过高** [R2 W1 + R1 AGREE]
- TOST p-value 和 ±3pp margin 不应出现在 abstract
- **修改要求**：保留 2-3 核心数字，TOST → "bounded interaction"

**W4. Contribution list 含未铺垫概念且过长** [R2 W2 + R1 AGREE]
- TOST、merge amplification 在 Introduction 首次出现但到后面才解释
- **修改要求**：每条 1-2 行，技术细节移至对应 section

**W5. BCS "generalizes across tasks" (Contribution #3) 过强** [R1 W3 + R2 W5 共识]
- Batch-level BCS 仅在 RE (FewRel + DocRED) 直接支持；NER/ED 需 confound adjustment
- **修改要求**：加 qualifier 限定 cross-domain RE tasks

**W6. Em-dash 19 处偏高** [R2 W4 + R1 同意]
- AI 写作痕迹，建议替换至少 2/3

**W7. Supplementary placeholder 未完成** [R1 + R2 强共识]
- Appendix L, M 有 "[Placeholder: ... to be added.]"
- **修改要求**：投稿前必须填充或删除

---

## Reviewer Consensus [AGREE]

1. **实验设计是论文最强贡献**——stratified factorial design 在 NLP empirical work 中具有示范价值
2. **因果语言需全面软化**——quasi-experimental ≠ causal；"predict" 替代 "drive"
3. **聚合推理链需重组**——observed R²=0.218 是 primary evidence，simulation 是 post-hoc explanation
4. **SCS framing 需修正**——贡献是 controlled validation，不是 metric discovery
5. **格式硬伤必须修复**——\enlargethispage hack + placeholder sections
6. **BCS batch-level 适用性受限**——仅 RE cross-domain schemas 直接适用

## Reviewer Divergence [REBUT]

1. **Practical significance of 2.2pp**
   - R1：证明 widely-assumed factor 实际 effect 小 = valuable counter-narrative；Cohen (1988) 标准下 "small but real"
   - R2：2.2pp practically marginal，削弱论文 motivation；practitioners 应关注 count reduction
   - **Director 判断**：这是 paper positioning 分歧而非方法缺陷。两种 framing 都有道理。

2. **TOST "三测两败" 的定性**
   - R1：三个独立 test 中两个失败 = evidence pattern 不支撑 "bounded interaction"
   - R2：Primary test (n=69, 5 count levels) passed；2×2 factorial 是 known-underpowered sensitivity check ≠ independent failure
   - **Director 判断**：R2 的层级解读更合理——non-significance in underpowered test ≠ evidence against。但 margin justification 的 external anchoring 仍需加强。

3. **Main vs Findings 定位**
   - R1：3.5/5（borderline Main，如果修正 N1-N3 可升）
   - R2：3.0/5（Findings，核心障碍：metric 非新 + effect 小 + 无 mitigation）

---

## Questions for Authors

1. 如果删除 conditional R²=7% 的中介推理，直接以 observed batch R²=0.218 为 claim，如何解释"为什么 mean-BCS（包含 89% 不产生 confusion 的 pairs）仍有预测力"？
2. v2 prompt 下 NER full count curve 是否也呈现 U-shape？如果是，U-shape 不是 prompt artifact；如果否，则 mechanistic explanation 需修正。
3. FewRel 64 train types vs 16 val types 的 BCS distribution 是否有 systematic difference？如果有，within-pool analysis 是否受此影响？

---

## Missing References

- NuNER (Bogdanov et al., 2024): zero-shot NER via instruction tuning [R2 提出, R1 同意]
- Self-Improving LLM IE (Zhang et al., 2024): iterative improvement [R2 提出]
- LLMaAA (Zhang et al., 2024): LLM-as-annotator schema scaling [R2 提出]
- Structured prediction/CRF label confusion 视角 [R2 提出, R1 认为可选]

---

## External Review (Stanford Agentic Reviewer)

项目配置 `external_review.paperreview_ai.enabled: false`。未请求外部审稿。

---

## Overall Assessment

**Score: Borderline (weak accept / borderline)**
**Confidence: High (4/5)**

这是一篇实验设计极为严谨的 empirical study，在 NLP IE 领域提供了罕见的 controlled factorial evidence 和诚实的 negative result diagnosis。核心贡献不在于 metric novelty（SCS = LLM-PEE），而在于 controlled validation framework 和 "count dominates confusability by ~20×" 的 counter-narrative finding。

**阻碍 Main acceptance 的主要因素**：
1. 因果语言的 over-claim（可修复）
2. TOST margin 的 external anchoring 不足（可修复）
3. BCS generalization claim 过强（可修复）
4. Typical effect size 仅 2.2pp 的 practical relevance 论证（positioning issue）
5. 格式硬伤（\enlargethispage, placeholders）（必须修复但 trivial）

**如果 C1-C4 和 W1-W7 被充分修正**，论文的 experimental rigor + negative result value + counter-narrative finding 组合足以支撑 EMNLP Main borderline acceptance。当前状态介于 Main borderline 和 Findings 之间。

---

## Detailed Comments

### Abstract
- 删除 TOST 具体参数，保留 "bounded interaction in RE"
- 保留 2.2pp (typical)、-49pp (count)、22-53% (batch R²) 三个核心数字

### Introduction
- Contribution #1: 弱化 "bounded interaction" 为 RE-specific finding
- Contribution #2: "First controlled validation" not "Pairwise embedding similarity predicts"
- Contribution #3: 加 cross-domain RE qualifier
- 全部 contribution 每条 ≤ 2 行

### §4.3 Practical Magnitude
- 开头以 observed R²=0.218 (direct OLS) 为 primary claim
- Conditional R²=7% 和 simulation 明确标注为 "post-hoc explanatory model, not evidence chain"
- "为什么 mean-BCS 有预测力" 给出不依赖条件化的解释（high mean-BCS batches contain more active pairs）

### §4.4 Multi-Channel Degradation
- "channels" → "dimensions" / "components"
- "driven" → "predicted by" / "associated with"
- TOST discussion: 加 Lakens (2017) SESOI framework reference

### §5 SDGD
- 删除 \enlargethispage*{9\baselineskip}
- 压缩 routing strategy details（移部分到 appendix）
- 末尾扩展 future directions（2-3 sentences: two-stage coarse→fine, retrieval routing, calibrated generation）

### Discussion
- U-shape explanation 标注为 "hypothesis"
- Boundary conditions 加 "BCS batch-level applicability limited to cross-domain RE"

### Writing
- 替换至少 12/19 处 em-dash
- 填充 Appendix L/M 或删除 placeholder

### Format
- 确认正文 ≤ 8 页（删除 \enlargethispage 后重新编译验证）
- §3.4 补充 GPU 型号统一