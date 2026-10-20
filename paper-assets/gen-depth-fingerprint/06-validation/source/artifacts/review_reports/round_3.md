---
round: 3
overall_score: borderline (Findings acceptance)
timestamp: 2026-05-16T04:26:19.700862+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 3 (Fresh Review)

**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains
**Venue**: EMNLP 2026 Main Conference (Long Paper, ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性/实验/统计), R2 (新颖性/相关工作/写作/格式)
**交叉回应**: 完成，两位 reviewer 均对对方意见逐条 [AGREE]/[REBUT]

---

## Summary

本文定义了"序贯生成深度估计"(ordinal depth estimation)任务——将文本分类为人写(gen-0)、一次生成(gen-1)或更深层(gen-2+)，超越传统二分类检测。作者在 6 个 base model 生成器（3 个模型族，0.6B–8.2B 参数）上构建非释义续写链，提取 7 个分布特征（5 个 NLL 统计量 + TTR + hapax ratio），用 XGBoost 分类。核心实证发现为"differential depth response"：中心趋势和多样性特征随深度单调漂移，而分布形状特征保持近稳态。Leak-free binary F1=0.723（gen-1 vs gen-2+），per-generator std=0.051。下游实验（单模型、单任务）显示深度感知数据筛选不优于随机采样。

---

## Strengths

1. **新颖的任务定义**: Ordinal depth estimation 填补了 binary detection 与递归生成分析之间的空白。形式化定义清晰（§3.1），与 source attribution 的区分明确（§2.1）。[R1, R2 一致]

2. **严谨的评估协议**: LOGO/LOFO 交叉验证正确测试了 cross-generator/cross-family generalization；binary evaluation 解决了 gen-0 泄露；Bonferroni 校正、McNemar 检验、paired bootstrap 等统计实践超出平均水平。[R1, R2 一致]

3. **Differential depth response 是有价值的实证贡献**: 中心趋势特征 monotonic drift + shape 特征 stationary 的分离是一个 clean 的 empirical pattern。Cross-family reference model 实验（3 个参考模型，F1 spread=0.013）确认其非 reference-specific。[R1, R2 一致]

4. **诚实报告负面结果**: instruct model 退化（OLMo-Instruct F1=0.338）、downstream curation 无效（ppl 差异 0.020）、entropy_min 冗余等均被透明报告。Limitations section 质量高，覆盖了规模、prompt type、语言、reference model 等多个维度。[R1, R2 一致]

5. **丰富的消融和鲁棒性分析**: 9 个附录覆盖 length confound, prompt type, finer-grained depth, QLoRA, LOFO, classifier sensitivity, human-edit robustness, sampling sensitivity, downstream。分析深度超出平均水平。[R1, R2 一致]

6. **Cross-model chain 和 cross-family 实验**: 异构链 F1=0.809（3-class）/0.764（binary），增强了 real-world relevance 可信度。[R1, R2 一致]

---

## Weaknesses

### Critical — Must-Fix（影响接收决定）

**N1 [critical, consensus]** Base-model-only 限制与 web-scale framing 根本性脱节
- 两位 reviewer 独立列为 Critical。Abstract 首句 "training corpora increasingly contain recursively generated text"、Introduction §1 以 "web-crawled corpora" 为动机，但全部 6 个 generator 均为 base model。Discussion 明确报告 instruct 深度信号大幅退化：OLMo-Instruct LOGO F1=0.338（vs base 0.764），Qwen3-0.6B length-matched binary F1≈0.5（chance level）。Web 文本几乎全部来自 instruct/RLHF 模型。
- **核心问题**: 方法在论文自身动机描述的应用场景中不工作。Introduction §1 L3 声称 "current detection methods are ill-equipped"，但本文方法同样无法处理 instruct chains。Claims 与 evidence 根本不匹配 (ARR R4)。
- **建议**: (a) 大幅修改 framing——Abstract/Intro 前置 base-model 限制，不以 web-crawled provenance 为主要动机，定位为 base-model recursive generation 的科学发现；(b) 或补充 2-3 个主流 instruct model 实验展示 method boundary。

**N2 [critical, consensus]** 下游实验 (§4.4) 严重 underpowered，无法支撑 "diagnostic not curative" 的广泛结论
- R1 列为 Critical，R2 列为 Should-Fix 后在交叉回应中同意升级。
- 单一模型 (OLMo-2-0425-1B)、单一任务 (causal LM)、~4K 训练样本、仅 3 个随机种子。关键 perplexity 差异仅 0.020（2.367 vs 2.387），**未报告统计显著性检验**（无 CI、无 p-value、无 effect size）。
- 但此结论被列为 Contribution #3（Abstract 末句、Conclusion §6），以 "diagnostic not curative" 的 universal framing 呈现。
- **建议**: (a) 对 ppl 差异做 bootstrap CI 或 permutation test；(b) 进一步降级——从 Contribution #3 移除，仅作为 supplementary analysis 在正文简述、详情移入 Appendix。

**N3 [critical, R1 critical / R2 agree with nuance]** Gen-0 共享种子导致 3-class LOGO F1 呈现具有误导性
- 所有 generator 共享相同 ~1000 Wikipedia seeds 作为 gen-0。LOGO 中 held-out generator 的 gen-0 与训练集 gen-0 逐字相同——直接 train-test overlap。gen-0 class F1=0.94 人为虚高，3-class LOGO F1=0.789 被系统性高估。
- 文字上 binary F1 已被设为 primary metric（§4.1, §4.3），但呈现上不到位：Table 1 无 binary 列，3-class 0.789 仍是最显眼的数字。R2 认为更多是 presentation issue 而非方法论缺陷。
- **建议**: (a) Table 1 增加 binary F1 列或将 binary 结果提升至与 3-class 同等显著位置；(b) Table 1 caption 增加 gen-0 overlap caveat；(c) 最佳方案：使用独立 seed pool。

---

### Divergence — Reviewer 分歧

**D1 [R2: critical / R1: should-fix]** 方法新颖性不足
- R2 认为 7 个标准统计量 + XGBoost 无方法创新，"differential depth response" 本质是已知 OOD/mode-seeking 现象的重新描述，不足以支撑 main conference。
- R1 反驳：(1) 论文贡献定位为 task formulation + empirical characterization 而非 feature engineering（§2.1 末段明确声明）；(2) drift/stationary 分离（Figure 1, §4.2 Spearman ρ: hapax −0.558, entropy_std 0.076）在文献中无 prior documentation——model collapse 研究 training-loop degradation，OOD detection 做二值区分，均未在 inference chains 上做 ordinal drift pattern 分析；(3) ARR H7 不应 penalize methodological simplicity。
- R1 同意论文缺乏理论分析解释 shape stationarity，应补充更深入的 mechanistic discussion。
- **Director 判定**: 此分歧在 Findings vs Main 的定位上有实质影响。R1 的反驳有理——ARR 接受 empirical contribution + simple methods。但 R2 的关切对 main conference bar 成立。作为 Findings paper，方法简洁性不构成否决理由；作为 main conference，需要更深入的 mechanistic analysis。

---

### Warning — Should-Fix（影响评分但不一票否决）

**W1 [warning, consensus]** Table 4 (cross-ref) 与 Table 1 数字不一致
- Table 4 Pythia-410M LOGO F1=0.803 vs Table 1 6-gen average=0.789。几乎确定是 5-gen vs 6-gen split 差异，但论文未标注。论文涉及至少 3 种 split (5-gen, 6-gen, 7-gen)，增加读者混淆。Qwen3-0.6B 同时作为 generator 和 reference model 时的 self-referencing bias 也未讨论。

**W2 [warning, consensus]** 4-det+surface ensemble 暴露核心特征工程增量有限
- 4-det+surface binary F1=0.724 ≥ 7-feature ensemble 0.723。现有 detector + 简单 surface features 即可达到同等性能。Table 3 caption 声称 "strongest single-model method on both metrics" 不准确（4-det+surface 在 3-class 0.805 > 0.789 且 binary 0.724 ≥ 0.723）。
- 核心贡献应明确定位为 task formulation + differential depth response，而非 feature engineering 优越性。

**W3 [warning, consensus]** 单 prompt type 限制 differential depth response 普适性
- 主实验仅用 continuation prompt。Appendix B cross-prompt 仅用 Pythia-2.8B，且 elaboration per-depth decay rate 仅 1.4%（vs continuation 16.9%），暗示 differential depth response 强度高度 prompt-dependent。Cross-generator × cross-prompt 交互未测试。

**W4 [warning, consensus]** "Differential depth response" 机制解释是描述性重述而非因果机制
- "Location shift in the NLL distribution while preserving functional form" 是对观察到的 pattern 的 restatement，不是因果机制。Discussion §5 "Shape stationarity" 仅给出 informal hypothesis。Introduction/Abstract 表述比 Discussion 更断言性，需统一为假说。

**W5 [warning, consensus]** Binary F1=0.723 的实际效用未讨论
- gen-1 per-class F1=0.64，约 36% 错分率。论文未讨论何种精度水平使 depth fingerprinting 在实践中有意义。Corpus-level prevalence estimation vs document-level classification 的 use-case-dependent 效用讨论完全缺失。

**W6 [warning, consensus]** 与 model collapse 文献的机制对比不足
- Discussion §5 仅一句 "parallels model collapse...but occurs without parameter updates"。未讨论 inference-chain vs training-loop drift 的 functional form 是否相同、mode dropping 是否发生、shape stationarity 是否 inference chains 独有。

---

### Minor — 不影响接收

- **M1**: Bootstrap CI 类型 (percentile/BCa) 和 resampling 粒度未说明
- **M2**: 样本量 30000 expected vs 27529 actual，差异未解释
- **M3**: tail_decay 引用 Hendrycks & Gimpel 2017 是 OOD baseline 而非 heavy-tail 方法论
- **M4**: Figure 1 缺少 per-generator variation（建议 strip plot 或 error bars）；正文仅 2 个 Figure，可增加 NLL 分布 violin plot
- **M5**: "entropy_*" 实为 NLL 统计量，命名可能混淆（建议 footnote 澄清）
- **M6**: 缺少 dataset statistics 表（per-generator × per-depth 样本数和长度分布）
- **M7**: Abstract 数字密度仍偏高
- **M8**: Qwen3-0.6B F1 在不同 split 下报告为 0.816 和 0.824，需标注 split 区分

---

## Questions for Authors（合并去重）

1. Per-generator binary F1 (gen-1 vs gen-2+) 的完整分布是什么？（当前只报告 std=0.051）
2. Bootstrap CI 使用什么类型 (percentile/BCa)？resampling 在 sample 级别还是 document 级别？
3. Table 4 (cross-ref) 使用的是几个 generator 的 LOGO？如果是 5-gen，为何不与 6-gen 保持一致？
4. Wikipedia seed passages 如何选择（random/topic-controlled/length-filtered）？
5. Downstream perplexity 差异 0.020 的 95% CI 和 p-value 是多少？
6. Qwen3-0.6B 同时作为 generator 和 reference model 时，held-out F1 是否有异常（self-referencing bias）？
7. Baseline detectors (FastDetectGPT, Binoculars) 是否使用了与 7-feature ensemble 相同的 Pythia-410M reference model？
8. 能否提供 instruct 模型 length-matched 条件下的 feature 分布可视化？
9. Gen-0 seed 为何在所有 generator 间共享而非使用独立 seed pool？

---

## Missing References

**共识遗漏（R1, R2 均同意）**:
- Energy-based OOD detection: Liu et al., "Energy-based Out-of-distribution Detection", NeurIPS 2020
- Mahalanobis distance OOD: Lee et al., "A Simple Unified Framework for Detecting Out-of-Distribution Samples and Adversarial Attacks", NeurIPS 2018
- FineWeb: Penedo et al. (2024) — 大规模 web data curation pipeline
- Dolma: Soldaini et al. (2024) — 大规模 data curation pipeline
- Gerstgrasser et al. (2024) data mixing strategy 与 depth-aware curation 的关系需讨论

**单方建议（待核实）**:
- DetectRL (R2, 未提供完整引用)
- arXiv:2505.11550 (R2, 未提供标题和作者)

---

## Overall Assessment

**Overall Score: 3.0 / Findings acceptance**

**R1**: 3.0 (Soundness 3.5/5, Excitement 3.0/5, Confidence 4/5)
**R2**: 3.0 (Soundness 3.5/5, Excitement 2.5/5, Confidence 4/5)

### 评分依据

**为什么不是 Main Conference (≥3.5)**:
- N1 (framing-scope mismatch) 是核心缺陷——论文以 web-crawled text provenance 为动机但方法仅对 base model 有效，instruct model 接近 chance。这不是边界局限而是 claims 与 evidence 的根本不匹配。
- 方法新颖性存在分歧（D1），但两位 reviewer 均认为当前深度不足以支撑 main conference bar。
- Binary F1=0.723 的实际效用未被讨论，gen-1 per-class F1=0.64（36% 错分）在诊断场景中偏低。

**为什么不是 Reject (≤2.0)**:
- 任务定义确实新颖且有研究价值。
- 实验方法论质量高——LOGO/LOFO 设计、统计测试、大量消融均超出平均水平。
- Differential depth response（drift/stationary 分离）是一个 clean 的 empirical pattern，对理解 recursive generation 有独立科学价值。
- Negative findings 被诚实报告，展现良好学术规范。

**对作者的建议**:
1. **首要任务**: 大幅修改 framing——将论文明确定位为 base-model recursive generation chains 的实证研究，而非 web-scale provenance 工具。Abstract/Intro 第一段即前置 base-model scope。
2. 下游实验补统计检验（bootstrap CI for ppl difference），降级为 supplementary analysis，从 Contribution 列表移除。
3. Table 1 增加 binary F1 列或以 binary 为主表，3-class 降为辅助。
4. 增加 mechanistic discussion：inference-chain vs training-loop drift 对比、shape stationarity 假说的 theoretical grounding。
5. 每个表格标注 generator split，修正 Table 3 caption。

**置信度: 4/5** — 两位 reviewer 均仔细阅读了全文含全部 9 个附录。