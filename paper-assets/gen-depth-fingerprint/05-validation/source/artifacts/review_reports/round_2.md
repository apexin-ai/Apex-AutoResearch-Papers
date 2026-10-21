---
round: 2
overall_score: borderline
timestamp: 2026-05-15T13:31:11.982420+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

## 审稿报告 — Round 2（Fresh Review）

**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains
**Venue**: EMNLP 2026 ARR Main Conference (Long Paper)
**审稿日期**: 2026-05-15
**Reviewer**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 完整性 + 写作质量）

---

## Summary

本文定义了 ordinal depth estimation 任务——将文本分类为 gen-0（人写）/ gen-1（首次生成）/ gen-2+（更深层递归），超越二分类检测。作者在 6 个生成器（3 个模型族，0.6B–8.2B）上构建非改写 continuation 链，发现 "differential depth response"：中心趋势和多样性特征随深度单调漂移，分布形状特征保持近稳态。7 特征集在 LOGO 评估中达 macro-F1=0.789。同时报告负面发现：depth-aware 数据筛选不优于随机采样。

---

## Strengths

**S1. 任务定义有价值且有动机** [R1, R2 一致]
从二分类到有序多分类的扩展是自然且有意义的。LOGO/LOFO 评估设计确保测试深度信号而非生成器指纹。Source attribution vs depth estimation 的区分清晰（§2.1）。

**S2. 实验方法论全面** [R1, R2 一致]
统计检验（McNemar, paired bootstrap）、多层消融（feature ablation, LOFO, LOGO, LOFO-family, cross-reference-model, classifier sensitivity）、三种长度混淆控制、cross-prompt-type 实验——消融设计的广度在同类论文中少见。

**S3. 诚实报告不利结果** [R1, R2 一致]
Downstream negative finding（§4.4）和 multi-detector ensemble 优于 proposed method（§4.3）均坦率报告，有助社区避免无效的工程投入。

**S4. Related work 系统且区分准确** [R1, R2 一致]
对 detection、model collapse、iterative generation、data quality 的梳理系统。与 concurrent work（Broken Telephone, Markovian Chains）的区分明确。

**S5. 写作整体清晰，结构合理** [R1, R2 一致]

**S6. Reproducibility 良好** [R2]
超参完整报告，承诺代码/数据发布，评估协议描述清晰。

---

## Weaknesses

### Critical（影响接收决定）

**C1. Bootstrap CI 被系统性误用为跨生成器一致性指标** [R1 raised, R2 strongly agrees]
- 论文核心 claim 之一：ensemble "CI width < 1pp" vs baselines "18–26pp" 作为跨生成器一致性证据，出现在 Abstract、§1、§4.3、§5、§6 至少 6 处。
- **问题**：Bootstrap CI 衡量 pooled F1 的采样精度，不等于跨生成器一致性。Table 1 明确显示 per-generator F1 从 0.683（Qwen3-8B）到 0.856（Pythia-1B），跨度 17.3pp——与 "tight cross-generator consistency" 直接矛盾。Baseline CIs 混合了采样噪声和 generator-dependent 方差，与 ensemble CI 不可比。
- **影响**：读者被误导以为 ensemble 在每个 generator 上都稳定在 ~0.79 附近。
- **修改方向**：以 per-generator F1 的 std（~0.058）和 range（17.3pp）作为一致性度量；abstract/intro/conclusion 替换 CI width 表述；§4.3 明确 bootstrap CI 衡量的是什么。

**C2. Gen-0 数据泄露风险** [R1 raised, R2 agrees]
- §3.2 未说明 Wikipedia seeds 是否跨 generator 共享。若共享，LOGO 中 gen-0 在训练集和测试集完全相同——直接数据泄露。
- Confusion matrix gen-0 准确率 99.4%，远超 gen-1（75.0%）和 gen-2+（73.7%），与泄露假说一致。
- 即使独立采样，gen-0 全部来自 Wikipedia 同一语料，分布高度一致，分类器可能学到 "Wikipedia style = gen-0" 而非真正的深度信号。
- **修改方向**：明确 seed 采样策略；如共享，重新计算排除 gen-0 后的 F1（或 gen-1 vs gen-2+ 二分类 F1）。

**C3. 仅测试 base 模型，缺失 instruction-tuned/RLHF 模型** [R2 raised as Critical, R1 agrees — upgraded from Minor to Major]
- 全部 6 个生成器为 base/pretrained 模型。论文动机（§1 第 1 段 "LLM outputs accumulate on the web"）指向网络文本——绝大多数来自 instruction-tuned/chat 模型。
- Base 模型的 continuation 与 chat 模型的 instruction-following 在分布特征上有本质差异。如果 differential depth response 在 instruction-tuned 模型上不成立，核心发现将大幅缩水。
- **修改方向**：(1) 加入 2–3 个 instruction-tuned 模型验证；或 (2) 重新定位论文范围——明确限制于 base 模型 continuation chains 的科学分析。

**C4. Cross-scale gap 严重且与 web-scale 动机矛盾** [R2 raised, R1 agrees]
- Qwen3-8B (8.2B) 的 held-out F1=0.683，远低于 ≤2.8B 生成器的 0.764–0.856，下降约 10pp。
- 网络文本主要由 70B+ 模型生成。从 8.2B 已显著下降，外推到 frontier scale 前景不明。
- §4.1 "adding Qwen3-8B data improves +1.1pp" 未控制 data volume 混淆。
- 与 Introduction 的 web-crawled data curation 叙述存在根本矛盾。

---

### Major（应修复，影响评分）

**M1. Differential depth response 新颖性被过度声称** [R1 Major, R2 agrees]
- §1 称其为 "our central empirical finding"，但 mean shift + variance stationarity 是分布 location shift 的标准性质，OOD detection 文献已有记录（作者自己引用 Hendrycks & Gimpel 2017 并在 §5 承认）。
- 贡献在于在新 setting（non-paraphrastic inference chains）下的系统测量，但语言应调整为 "characterization" 或 "documentation"。

**M2. Downstream "diagnostic not curative" 结论过度泛化** [R1 Major, R2 Major]
- 1 模型（OLMo-2-1B）、1 任务（causal LM）、~4K 样本、3 seeds。PPL 差异仅 0.020（2.367 vs 2.387）。
- 虽已降级为 "complementary analysis"，但 abstract 和 conclusion 的措辞仍为普遍性判断（"depth fingerprinting is an effective diagnostic tool ... not a curative tool"）。
- 应限定为 "in our setting" 或增加更多 tasks/scales。

**M3. 评估协议不一致（5-gen vs 6-gen LOGO）** [R1 Major, R2 Major]
- Table 1: 6-gen LOGO；Table 3: 5-gen LOGO (baselines)；§4.3 multi-detector: 6-gen LOGO。三处使用不同协议，数字不可直接比较。
- 应统一为 6-gen LOGO，在同一表中报告所有方法。

**M4. Negative finding 削弱实用性，替代应用缺乏实验验证** [R2 Major, R1 agrees]
- Depth-aware curation 无效的结论严重削弱正面贡献。Discussion 中 "risk-stratified data curation" 纯属假设，无实验支持。
- 如果 depth 无下游用途，估计 depth 的动机减弱。应提供至少一个有用应用的实验证据。

**M5. Ordinal 任务用 multiclass 分类，未讨论 ordinal-specific 方法** [R1 Minor-Major, R2 agrees]
- 论文在 §3.1 定义为 ordinal classification，但使用标准 multiclass XGBoost。未讨论 ordinal regression 或 CORAL。
- Confusion matrix 中 gen-1↔gen-2+ 高误分类率可能正因未利用有序结构。

**M6. Baseline 超参不对称** [R1 Major, R2 partially rebuts]
- Ensemble: n_estimators=200, max_depth=6；Baselines: 100/3。性能差距可能部分反映分类器容量。
- R2 指出单特征输入用 max_depth=6 会过拟合，选择合理——但应提供实验证据（200/6 下 baseline F1）。

---

### Minor

**m1.** entropy_min 完全冗余（LOFO Δ=+0.01pp）但保留在 7-feature set 中。应改为 6-feature 或给出理由。[R1, R2 一致]

**m2.** tail_decay 90th percentile 阈值无 justification。R2 认为是标准选择，但缺少 sensitivity analysis。[R1 raised, R2 agrees on adding justification]

**m3.** 6 次显著性检验未报告多重比较校正。R2 指出 all p<0.001 Bonferroni 后仍显著，不影响结论但应补报。[R1 raised, R2 agrees as reporting issue]

**m4.** 术语 "Depth Fingerprinting"（方法）vs "ordinal depth estimation"（任务）未明确定义区别。"Fingerprinting" 暗示唯一标识，与分类任务有语义偏差。[R2 raised as Major, R1 rebuts to Minor]

**m5.** Abstract ~200 词，包含过多数字细节（CI width, pp 值）。应精简至 ~150 词。[R2]

**m6.** Related Work 遗漏 Wu et al. (2025) "A Survey on LLM-Generated Text Detection"（Computational Linguistics, MIT Press）——当前最全面综述，应替代或补充 Jawahar et al. (2020)。也未讨论 trained classifier baselines（如 GPTZero）。[R2]

**m7.** Bib 条目年份可能有误：diveye (2026→2025?), strong_model_collapse (2025→2024?)；aaronson_watermark 作为 misc 类型缺可追溯信息。[R2]

**m8.** Introduction §1 line 42 "§5 discusses limitations" 不准确——Limitations 是独立未编号 section。[R2]

**m9.** Feature 变量名在正文用 code-style（entropy\_mean 等），建议用正式数学符号或自然语言。[R2]

---

## Reviewer Consensus [AGREE]

两位 Reviewer 独立给出 3.0/5（Findings），交叉回应后一致性极高：

| 问题 | R1 | R2 | 交叉后共识 |
|------|----|----|-----------|
| Bootstrap CI 误用 | Critical | Strongly agrees | **Critical** |
| Gen-0 数据泄露 | Critical | Agrees (补充 Wikipedia 分布问题) | **Critical** |
| 缺 instruction-tuned 模型 | Minor→Major | Critical | **Critical** |
| Cross-scale gap | Implicit | Critical | **Critical** |
| Differential depth response 过度声称 | Major | Agrees | **Major** |
| Downstream 规模不足 | Major | Major | **Major** |
| 评估协议混用 | Major | Major | **Major** |
| Negative finding 削弱实用性 | Agrees | Major | **Major** |
| 缺 ordinal-specific 方法 | Minor-Major | Agrees | **Major** |

## Reviewer Divergence [REBUT]

仅有程度上的微小分歧，不影响总体判断：

1. **R2-N2（方法新颖性 → Critical vs Major）**：R2 认为 Critical（不够 main conference），R1 rebuts 认为 task formulation + systematic LOGO 是实质贡献，降为 Major（overclaimed 但非无贡献）。**最终判断**：Major——方法新颖性确实不足，但 task formulation 有价值，问题更多在于 claim 强度而非贡献存在性。

2. **R2-W4（术语不一致 → Major vs Minor）**：R2 认为 Major，R1 rebuts（NLP 论文常见做法）。**最终判断**：Minor——添加明确定义即可。

3. **R1-W1（Baseline 超参不对称 → Major）**：R2 部分 rebuts（单特征 max_depth=6 会过拟合，100/3 是合理实践）。**最终判断**：Major——理由合理但应提供实验证据。

---

## Questions for Authors

1. Wikipedia seeds 是否跨 generator 共享？如共享，排除 gen-0 后的 gen-1 vs gen-2+ 二分类 F1 是多少？
2. 是否测试过 instruction-tuned 模型？如果没有，是否有理由认为 differential depth response 在 RLHF 模型上仍成立？
3. Per-generator F1 的 std 是多少？Baselines 的 per-generator F1 及 std 又是多少？（以直接比较跨生成器一致性）
4. Baselines 使用 n_estimators=200, max_depth=6 时 F1 变化如何？
5. 为何在 multi-detector ensemble (0.796/0.805) 优于 7-feature (0.789) 时仍以后者为 proposed method？
6. Cross-reference-model 实验中，Pythia-1B 作为最易分类 generator 是否受 same-family reference model (Pythia-410M) 影响？
7. Shape features 的近稳态性是否仅因固定 temperature=0.7 和 top-p=0.9？
8. "Adding Qwen3-8B data improves +1.1pp" 是否控制了 data volume？

---

## Missing References

1. **Wu et al. (2025)** "A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions." *Computational Linguistics*, MIT Press — 当前最全面综述，应替代/补充 Jawahar et al. (2020)
2. **Tian et al. (2026)** "GPTZero: Robust Detection of LLM-Generated Texts." arXiv:2602.13042 — trained classifier baseline 应讨论
3. **Data contamination detection 文献** — 如 Dong et al. (2024) "Does Data Contamination Detection Work (Well) for LLMs?" — 与 data provenance 动机直接相关

---

## External Review (Stanford Agentic Reviewer)

项目未配置外部审稿（`external_review.paperreview_ai.enabled` 未设置），未请求。

---

## Overall Assessment

**评分**: Borderline (3.0/5) — 适合 Findings track，当前不达 Main Conference 标准
**置信度**: 4/5

**核心判断**：论文提出了一个有价值的任务定义（ordinal depth estimation），实验方法论的广度和严谨度值得肯定。但存在四个 Critical 级问题：

1. **统计论证可靠性**：Bootstrap CI 误用和潜在的 gen-0 数据泄露动摇了核心数字的可信度
2. **实验覆盖范围**：仅 base 模型 + ≤8.2B 规模，与 web-scale 动机不匹配
3. **Cross-scale 可行性**：8.2B 已出现 ~10pp 下降，frontier 模型前景不明
4. **实用价值空洞**：负面发现削弱动机，无替代应用的实验验证

**如果修改**：
- **升至 Weak Accept 的路径**：(a) 修正 CI 论述 + 澄清 gen-0 泄露；(b) 加入 2-3 个 instruction-tuned 模型；(c) 统一评估协议为 6-gen LOGO；(d) 提供至少一个有用应用场景的实验证据
- **升至 Accept 还需**：(e) 测试 70B+ 模型；(f) 深化 differential depth response 的理论分析

**Findings track 推荐理由**：任务定义 + 现象刻画的组合具有发表价值，但实验覆盖不足和统计论证问题使其不达 main conference 标准。

---

## Detailed Comments (by Section)

### Abstract
- 替换 "CI width < 1pp vs 18-26pp" 为 per-generator F1 range
- 精简至 ~150 词
- "confidence intervals spanning 0.41--0.82" 表述准确但在 abstract 中信息过载

### §1 Introduction
- Line 24-26: "tight cross-generator consistency (CI width < 1pp)" — 核心误导，必须修正
- Contribution 3 "complementary analysis" 定位合理，但 conclusion 仍有过度泛化倾向
- Line 42: "§5 discusses limitations" 不准确

### §2 Related Work
- Source attribution vs depth estimation 区分有力
- 缺 Wu et al. (2025) 综述和 trained classifier 讨论
- §2.4 data provenance 可扩展 data contamination detection 线

### §3 Method
- §3.1 task formulation 清晰
- §3.2 必须明确 seed 共享策略
- §3.3 feature selection rationale 段落合理，但 entropy_min 冗余应处理
- §3.4 应讨论 ordinal regression 替代方案

### §4 Results
- §4.1 Table 1 数据可靠（若 gen-0 泄露澄清后），但 CI width 表述必须修正
- §4.2 differential depth response 描述客观，但 "central empirical finding" 措辞应降温
- §4.3 评估协议混用需统一
- §4.4 negative finding 诚实，但 conclusion 中泛化过度

### §5 Discussion
- "Why are shape features stationary?" 标注为 speculative 是诚实的
- "Topic drift as mediator" 分析有说服力
- "Depth features vs multi-detector ensembles" 段落坦率
- 缺失：为什么 depth estimation 有用的正面论证

### Limitations & Ethics
- Limitations 诚实且全面
- 但 instruction-tuned 模型缺失应更显著地列入
- Ethics Statement 充分