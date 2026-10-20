---
round: 39
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-22T00:58:46.812273+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 39 (Fresh Review)

**论文**: Depth Fingerprinting: Classifying Recursive Generation Depth in Base-Model LLM Text
**Venue**: EMNLP 2026 via ARR May 2026
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: �����性+完整性+写作质量）
**交叉验证**: 完成，1 轮即收敛

---

## Summary

论文提出 Differential Depth Response (DDR) 概念，表征 base-model LLM 递归生成文本中 NLL 位置统计量单调漂移而分布形状特征近乎不变的不对称现象。基于 8 个生成器（5 族, 0.6B-8B）在 nucleus sampling 下的系统实验，论文验证了 DDR 分解并开发了 7-feature XGBoost 分类器，在 leave-one-generator-out 评估中达到 binary F1=0.694（gen-1 vs. gen-2+, 有效分辨率 3 类）。

---

## Strengths

1. **问题新颖**: Depth classification 首次被形式化为独立任务（beyond binary AI text detection），DDR 分解是有实质贡献的 empirical finding。
2. **实验设计严谨**: 8-gen LOGO cross-validation 消除 generator leakage；Bonferroni-corrected bootstrap CI；Cohen's d effect size 报告；涵盖 22 页附录的全面消融（特征/生成器/解码/温度/prompt/跨域/文本扰动/种子控制）。
3. **Baseline comparison 公平**: 与 Avg-LogProb、FastDetectGPT、Binoculars、LD-Score 统一框架（XGBoost + LOGO）对比。
4. **透明度高**: Appendix K 诚实报告 instruction-tuned 阴性结果；Appendix M 坦诚呈现 downstream null result；Limitations 章节覆盖主要约束。
5. **DDR 概念可视化有效**: Figure 1 (strip plot) 和 Figure 2 (μ,d space) 清晰传达 drifting vs. stationary 分离。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[MF-1] DDR 缺乏形式化定义与理论基础** [R1-N1, R2 AGREE]
- DDR 全文无数学定义。"d>0.50=drifting, d<0.15=stationary" 是 post-hoc 分类，缺乏独立预测力。Section 5 的解释（"nucleus sampling preserves conditional distribution form"）是 hand-waving 而非推导。
- 影响：作为 empirical study 的核心概念贡献，DDR 的泛化性（新模型/新解码策略）无法从理论预测，只能事后验证。
- 修改方向：(a) 提供 KL/Wasserstein 形式化定义；(b) 或从 autoregressive stationary distribution 收敛理论给出 theoretical motivation。

**[MF-2] Reference model (Pythia-410M) 混淆变量未消融** [R1-N2, R2 AGREE]
- 全部 7 特征基于 Pythia-410M NLL。Table 2 显示 Pythia 系列生成器 F1 最高 (0.724)，跨族最低 (Mistral 0.633)。family proximity（共享 tokenizer + 预训练语料）可能贡献了部分 depth signal。
- 影响：DDR 可能部分是 reference-model calibration artifact 而非 depth intrinsic property，直接削弱 "cross-generator" claim。
- 修改方向：用 ≥1 个非 Pythia reference model 重复 8-gen LOGO 核心实验。

**[MF-3] 正文溢出 8 页限制** [R1-N3, R2 AGREE]
- Section 6 Conclusion 延续到 p.9 顶部。EMNLP 2026 严格 8 页正文（Limitations/Ethics 除外）。
- 影响：格式违规，desk reject 风险。
- 修改方向：压缩 Discussion/Conclusion；Figure 3 可移至附录。

### Should-Fix（影响评分）

**[SF-1] 3-class 深度分辨率与标题 "fingerprinting" 的 framing gap** [R2-N1, R1 agree with nuance]
- 实际系统仅支持 gen-0/gen-1/gen-2+ 三类；5-class F1=0.50 (Appendix D)。"Depth Fingerprinting" 暗示更精细的分辨能力。R1 认为这是 framing 问题而非方法论缺陷。
- 修改：Abstract 补充 "effective resolution: three depth classes"；Section 3.1 明确合并理由。

**[SF-2] Downstream utility 阴性结果需在主文正面讨论** [R2-N3, R1 agree on factual basis]
- Appendix M: depth-aware curation 与 random curation 统计等价 (TOST p<0.001)。R1 指出 primary motivation 是 provenance transparency 而非 filtering，severity 有分歧（R2 critical, R1 warning）。
- 修改：Discussion 加段落报告 null result，将 motivation 明确定位为 provenance auditing。

**[SF-3] TOST n=3 underpowered + margin 论证不足** [R1-W1 + R2-W3, mutual AGREE]
- Per-generator TOST 仅 n=3 seeds，统计力不足。TOST ε=0.20 选择缺 power analysis。Bootstrap stability 不能弥补原始样本量不足。
- 修改：降低 TOST 在论证中的权重或增加 seeds；补充 margin 敏感性分析。

**[SF-4] gen-0 shared-seed 致 3-class F1 被 inflate** [R1-W2, R2 AGREE]
- LOGO 中 gen-0 文本在所有 generator 间共享（同文本→同特征值），构成 train-on-test。Binary F1（主指标）不受影响，但 3-class F1=0.762 中 gen-0 recall 被 inflate。
- 修改：补充 3-class independent-seed 结果或明确标注 inflation。

**[SF-5] Cross-domain 退化 (F1=0.52-0.65) 主文讨论不足** [R2-W1, R1 AGREE]
- 非 Wikipedia 域 3-class F1 显著下降但仅在附录报告。
- 修改：Section 5 或 Discussion 补充具体数值。

**[SF-6] 与 concurrent work 区分应更清晰** [R2-W4, R1 partially AGREE]
- Geng et al. (2026) / Mohamed et al. (2025) 对比在附录 Table 45 但主文未引用。
- 修改：主文 Related Work 增加显式区分维度。

**[SF-7] QLoRA vs XGBoost trade-off 应在主文讨论** [R1-W3, R2 corrects metric: 3-class gap = +1.6pp not +11.6pp]
- R2 纠正了 R1 的 metric confusion（binary 0.905 vs 3-class 0.789 不是同一 task）。公平对比 3-class: QLoRA 0.805 vs XGBoost 0.789，差距仅 +1.6pp。
- 修改：主文简述 accuracy-interpretability trade-off。

**[SF-8] Cohen's d 阈值 domain appropriateness** [R1-W4, R2 AGREE]
- 行为科学阈值在 NLP distributional statistics 中适用性未讨论。k-means 验证部分缓解。
- 修改：说明阈值仅作参考锚点，主要依据数据驱动聚类。

### Minor Issues (不影响接收)

- 术语不一致："generation depth" / "recursive depth" 交替使用
- Footnote 1 的 base-model 限定放脚注易被忽略
- Table 2 "3-cl F1" 列标题不够自解释
- DDR 缩写首次使用位置与正式定义位置不一致
- Figure 1/2 灰度打印可读性（建议增加 marker shape）
- Bonferroni "family" 定义和检验数量未明确

---

## Reviewer Consensus

以下问题两位 Reviewer 达成一致：
- [AGREE] DDR 需要形式化定义或理论支撑（MF-1）
- [AGREE] Reference model 消融是最大实验 gap（MF-2）
- [AGREE] 页面超限必须修复（MF-3）
- [AGREE] TOST n=3 underpowered（SF-3）
- [AGREE] gen-0 shared-seed inflation（SF-4）
- [AGREE] Cross-domain 退化应在主文讨论（SF-5）
- [AGREE] Cohen's d 阈值域适用性（SF-8）

## Reviewer Divergence

- **R2-N2 (base model 未标识)**: R1 直接 REBUT——标题已含 "Base-Model"，abstract 首句已标注。R2 的 specific factual claim 不成立。**采纳 R1 判断：scope 标注已充分。**
- **R2-N3 severity (downstream negative)**: R2 视为 critical，R1 降级为 warning（primary motivation 是 provenance transparency）。**采纳折中：归入 SF-2 而非 MF。**
- **R1-W3 (QLoRA gap)**: R2 纠正 R1 的 metric confusion（混淆 binary/3-class F1）。实际 3-class gap +1.6pp，非 +11.6pp。**采纳 R2 修正。**

---

## Questions (需要作者澄清)

1. 换用非 Pythia reference model (如 OLMo-1B, GPT-2-small) 后，DDR partition 和分类性能如何变化？
2. Shape features 的 near-stationarity 能否从 autoregressive generation 的 mixing property 推导？
3. 3-class independent-seed LOGO 的 F1 是多少？gen-0 shared-seed inflation 量化值？
4. Instruction-tuned model 的 depth signal 衰减——是 NLL landscape 改变还是 reference model calibration 变差？
5. Figure 3 (p.8) 的 DDR partition 可视化是否必须在正文？移至附录能否解决页面超限？

---

## Missing References

- R2 建议添加 arXiv:2511.17602 ("Beyond Surface-Level Similarity: Hierarchical Contamination Detection")——需验证 relevance 后酌情添加。
- R1 未发现明显遗漏。整体引用覆盖良好（66 条，0 orphan）。

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿（项目 config 中无 `external_review.paperreview_ai.enabled`），本轮跳过。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 于 2026-05-22 00:40 启动，300s 后超时未完成。无有效 findings 返回。
- 状态：**timeout**
- 建议：用户可手动重新触发视觉审查。历史轮次（Round 34-38）持续标记 "前 3-4 页无 display item" 的问题（R34-V1），本轮无法验证是否已修复。

---

## Overall Assessment

**评分: 3.0 — Findings（可被 Findings 接收）**

**置信度: 4/5**（两位 Reviewer 仔细阅读全文及附录，领域熟悉度高）

**评分依据**:
- R1: 3.5 (Borderline Conference), R2: 3.0 (Findings)
- 综合判断取 **3.0**，理由：
  1. MF-2（reference model 消融）是实质性实验 gap，修复需要新实验，不是 writing fix
  2. MF-1（DDR 形式化）在 empirical paper 中权重较低但仍限制了理论贡献
  3. MF-3（页面超限）虽易修复但当前版本确实违规
  4. Base-model-only scope（SF, 结构性限制）+ downstream null result 共同削弱实际影响力
  5. 若 MF-2 消融结果积极（DDR 在非 Pythia reference 下仍成立）+ MF-1 有 minimal 形式化 + 页面修复，可上调至 3.5

**修改优先级**:
1. 🔴 **立即**: 压缩正文至 8 页（MF-3，30 分钟内可完成）
2. 🔴 **高优先**: 非 Pythia reference model 消融实验（MF-2，需跑实验）
3. 🟡 **中优先**: DDR 形式化定义或理论 motivation（MF-1）；主文讨论 cross-domain 退化和 downstream null result（SF-2, SF-5）
4. 🟢 **低优先**: 3-class framing 调整（SF-1）；Figure 可读性（SF-8/minor）

---

## Detailed Comments（逐节）

**Title**: "Base-Model" qualifier 已在标题中，但 "Fingerprinting" 暗示精细分辨率需注意 framing。
**Abstract**: 信息密度高，scope 标注清晰。建议补充 "three depth classes" 的分辨率限定。
**Section 1 (Intro)**: Contribution 列表清晰，proof-of-concept 定位到位。
**Section 2 (Related Work)**: 覆盖全面，但与 Geng/Mohamed 的 explicit 区分可更系统。
**Section 3 (Method)**: LOGO 评估协议设计严谨；特征选择 rationale 可更充分。
**Section 4 (Results)**: 核心结果呈现清晰；建议 4.2 降低 TOST 权重或标注 preliminary。
**Section 5 (Discussion)**: 需压缩以解决页面问题；应补充 cross-domain 和 downstream negative 讨论。
**Section 6 (Conclusion)**: 溢出到 p.9，必须修复。
**Limitations**: 诚实全面，覆盖主要约束。
**Appendix**: 详尽程度在同类工作中突出，但关键负面结果（Appendix J, K, M）应在主文有 summary。
