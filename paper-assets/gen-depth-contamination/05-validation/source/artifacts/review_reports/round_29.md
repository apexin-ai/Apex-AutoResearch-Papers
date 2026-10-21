---
round: 29
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T12:54:26.644399+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 29 审稿报告 — Generational Depth Estimation of Recursive Synthetic Text

**Venue**: EMNLP 2026 (ARR May 2026) | **Reviewers**: R1 + R2 | **模式**: Fresh (重新审稿) | **轮次**: 1 轮 + 交叉分享

---

## Summary

论文提出 generational depth estimation 问题：给定一段文本，估计它经历了多少轮递归合成生成。核心度量 K*_empirical 定义为统计特征可区分的最大相邻代际深度。在 10 个模型配置（6 架构族，1B-8B）、4 个文本域、4 种解码策略下，K*_empirical ≤ 2（web text），arXiv 达到 K*_empirical=3。论文将此现象命名为 "one-wash laundering"，并用下游 filtering 实验作为 consistency check。

---

## Strengths

1. **问题提出有真正新颖性** [R1 AGREE, R2 AGREE]：从 binary detection 扩展到 ordinal depth estimation 是自然但未被形式化的研究方向。K*_empirical（Eq. 1）作为 discrimination boundary 的操作化定义有概念清晰度，在先前文献中没有对应概念。

2. **统计方法严谨全面** [R1 AGREE, R2 AGREE]：10,000-iteration permutation tests + bootstrap 95% CIs + Bonferroni correction for 10 comparisons 的组合使用正确。θ 敏感性分析（Figure 3）、跨种子鲁棒性（Table 26）、5K/10K cross-sample validation（Table 28）体现了高标准的实验方法论。

3. **实验覆盖面广** [R1 AGREE, R2 AGREE]：6 架构族 × 4 域 × 4 解码策略 × cross-model transfer × neural probe × DeBERTa upper bound × downstream evaluation。附录 29 张表格展示全面的 sensitivity analysis。

4. **K*_empirical ≤ 2 作为负结论有实际意义** [R1 AGREE, R2 AGREE]：告诉社区 depth estimation 的天花板在哪里，为 data curation 设计提供实证基础。

5. **Cross-model transfer（continuation mode）** [R1 AGREE, R2 AGREE]：80-92% accuracy retention + scorer-invariant feature rankings (ρ > 0.90) 支持跨 generator 部署可行性。

6. **Section 5 consistency check 设计** [R1 AGREE, R2 AGREE]：measurement → prediction → validation 的完整科学链条。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [critical, R1+R2 共识] **下游过滤实验在现实污染比例下各策略趋同，实用性 overclaim**
- Table 5 + Appendix B.8 (Table 25)：≤50% 污染率下所有 6 种 filtering 策略差异不显著（p > 0.12）；10% 污染下 no-filter MMLU (0.6009) 与 base model (0.6018) 差异仅 0.09pp。
- Abstract 第 6 句 "K*_empirical correctly predicts that binary filtering outperforms graduated alternatives" 仅在 100% 合成极端设定下成立。
- Section 5 的 consistency check 在现实场景下 vacuous——所有方法等价（包括不 filter）。
- **要求**：Abstract/Conclusion filtering 声明加 "at high contamination ratios" 限定；正文充分引用 dose-response 数据；讨论低污染率趋同原因；或重新定位为 fundamental measurement 而非 actionable curation guidance。

**MF-2** [critical, R1+R2 共识] **"Generator-agnostic" 声明范围过大——仅限 continuation mode**
- Abstract "80-92% cross-model transfer" 仅在 continuation-mode 模型间验证。Section 4.2 明确报告 rewrite mode 迁移仅 61-63%。
- Rewrite mode 是现实常见的生成方式（paraphrasing, rewriting），排除在 "generator-agnostic" 之外会误导读者。
- **要求**：Abstract/Conclusion 中限定为 "within continuation-mode models"；或补充 rewrite-mode 跨模型迁移实验。

**MF-3** [critical, R1 发起, R2 同意] **K*_empirical 在样本量变化时不稳定**
- Table 28：LLaMA-8B 从 5K 的 K*=2 降至 10K 的 K*=1（OOF AUC = 0.5880）；Gemma-2-2B 反向漂移（K*=1→2, AUC = 0.6099）。
- "6/10 yield K*_empirical=2" 对采样敏感。但 "K*_empirical ≤ 2" 上界在所有样本量下成立。
- **要求**：(a) 对全部 10 configs 统一 10K 报告或论证 5K 充分；(b) 对 K*_empirical 本身做 bootstrap 量化离散估计不确定性；(c) 正文讨论 Table 28 key findings。

### Should-Fix（影响评分但不一票否决）

**SF-1** [warning, R1+R2 共识] **θ=0.60 阈值的理论根基和敏感性**
- Cohen's h = 0.20 作为 justification 存在概念问题（AUC 是 rank-based 指标，不等同于比例检验中的比例）。Figure 3 显示 K*_empirical 在 θ ∈ [0.55, 0.70] 从 3 变到 1。
- 建议在 Section 4.1 首次报告 K*=2 时就附带 θ 敏感性说明，避免读者到第 6 页才看到 Figure 3。

**SF-2** [warning, R2 发起, R1 部分同意] **Related Work 遗漏 text watermarking**
- Section 2 和 Section 6 未讨论 watermarking（Kirchenbauer et al., 2023; SynthID）作为 provenance tracking 替代方案。
- R1 认为应降级（范式不同，不影响核心论证）。两人共识：值得在 Section 2 或 6 中用 1-2 句话定位 watermarking 作为互补方案。

**SF-3** [warning, R2 发起+升级, R1 同意] **"One-wash laundering" 命名与 K*=2 存在逻辑矛盾**
- K*_empirical=2 意味着 0v1 和 1v2 都可区分（AUC > θ），需要**两次**生成才使文本与更深层内容不可区分。"One-wash" 命名暗示一次生成即可消除信号，与数据矛盾。
- Discussion 写 "A single generation pass renders text indistinguishable from multiply recycled content"——但 K*=2 恰恰说明 single pass 产生的 depth-1 仍可与 depth-2 区分。
- 建议：重命名（如 "rapid saturation effect"）或明确限定 "one wash" 的语义（binary detection perspective vs depth estimation perspective）。

**SF-4** [warning, R1+R2 共识] **Qwen 过度代表（4/10 配置）**
- "6/10 yield K*=2" 中 Qwen 贡献 4/6。按 family 去重后比例可能降至约 50%（3/6 或 4/6，取决于边界配置）。4 个 Qwen 配置共享 tokenizer 和 pretraining data，不具备独立性。
- 建议同时报告 per-family 去重统计。

**SF-5** [warning, R2 发起, R1 部分反驳] **方法论贡献定位**
- 15 个统计特征 + OBD LightGBM 为现有工具直接应用。R1 反驳论文 contribution list 措辞已为 empirical finding（"Measuring..."），未声称方法创新。
- 分歧缩小：论文自我定位基本合理，但可更明确。

**SF-6** [warning, R2] **未报告计算开销**
- 特征提取和分类器推理的 per-document 时间未报告。对 data curation pipeline 部署有实际意义。

---

## Reviewer Consensus [AGREE]

1. **实用性 overclaim**：dose-response 在 ≤50% 污染下趋同，Abstract/Conclusion 需限定 → 两人 critical
2. **"Generator-agnostic" 限定**：需明确限定 continuation mode → 两人一致
3. **θ 敏感性**：K*_empirical 点值依赖单一操作点，需区间报告 → 两人 Should-Fix
4. **Qwen 过度代表**：per-family 去重分析必要 → 两人一致
5. **K*_empirical 样本敏感性**：部分配置处于 θ 边际带，"6/10" 数字不稳健 → 两人一致（程度有差异）
6. **格式全部合规**：Abstract ≤200 words (147)、正文 8 页、Limitations 正确、匿名合规、无破折号违规

## Reviewer Divergence [REBUT]

1. **Watermarking 缺失严重度**：R2 标 critical（Related Work 不完整），R1 反驳为 Should-Fix（范式不同、不影响核心论证）。**裁定**：采纳 R1 论据，定为 Should-Fix。Watermarking 是 proactive embedding，本文是 post-hoc detection，用 1-2 句话定位即可。
2. **"One-wash laundering" vs model collapse**：R2 认为是已知现象的重述，R1 反驳 prompt-chain(K*=2) vs retrain-chain(K*=7) 有定量巨大差异。**裁定**：R1 的区分有道理，但 R2 关于命名精确性（"one-wash" vs K*=2 矛盾）的论点成立。两者的增量贡献需更精确界定。
3. **13B+/RLHF 模型缺失**：R1 标 Should-Fix，R2 反驳 Limitations 已恰当处理。**裁定**：已在 Limitations 中承认，Discussion 有规模效应讨论（JSD 趋势），不额外降分。

---

## Questions（需作者澄清）

1. 如果对所有 10 configs 统一使用 10K 样本，"6/10 yield K*=2" 是否需修正为其他数字？
2. 是否有更敏感的下游评测指标（如 perplexity, generation diversity）能区分不同 filtering 策略在 ≤50% 污染下的效果？
3. 是否测试过 rewrite-mode → continuation-mode 的跨模式迁移？如果没有，主要困难是什么？
4. DeBERTa 在 arXiv 上 K*=4（Table 29），这是否暗示 15D 特征 substantially underestimates K*_theory？

---

## Missing References

1. **Kirchenbauer et al., 2023**. "A Watermark for Large Language Models." ICML. — provenance tracking 替代方案 [R1+R2 共识]
2. **SynthID / C2PA content credentials** — 工业界 provenance 方案 [R2]
3. 建议检查 2025-2026 年 multi-class AI text detection 工作（需具体引用）[R2，R1 要求具体化]

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时 2m50s）。0 critical, 4 warning, 14 info。

主要发现：
- **Page 5** [warning]：整页纯文本（Sections 4.2-4.4），夹在 page 4（Table 1 + Figure 2）和 page 6（Figure 3, 4 + Table 3, 4）之间，引用多个 table/figure 但无法就近看到
- **Page 8** [warning]：整页纯文本（Discussion 续 + Conclusion），pages 7-8 视觉密度偏低。Conclusion 前若有 summary figure/table 可改善节奏
- **Page 14** [warning]：6 个小表格密集排列，部分字号接近可读性下限
- **Page 18** [warning]：末页仅占 ~35%，~65% 空白。可重分配 page 14 内容
- Figure 1 pipeline 图清晰可读，Figure 2 line plot 带 CI bands 专业，整体排版符合 ACL 规范

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

**置信度: 4/5**（两位 Reviewer 均仔细阅读全文及全部附录，熟悉相关领域）

**评审意见**：

论文提出了一个真正新颖的研究问题（generational depth estimation），K*_empirical 的形式化定义和系统性实验矩阵展现了高质量的经验研究。统计方法严谨，在同类 empirical study 中属于高标准。

主要问题集中在三个方面：(1) 实用性 overclaim——dose-response 证据表明 K*-aware filtering 在现实污染率（≤50%）下无显著优势，但论文叙事暗示广泛的实际应用价值；(2) "generator-agnostic" 声明仅对 continuation mode 成立，需明确限定；(3) K*_empirical 的点值对阈值和样本量均敏感，核心数字 "6/10" 不够稳健。

如果三个 Must-Fix 问题（filtering 声明限定、generator-agnostic 限定、样本稳定性讨论）能在修改中妥善处理，论文作为 empirical measurement 的定位足以支撑 Findings 接收。达到主会议水平需要更强的实用性证据或更深入的理论洞见。

---

## Detailed Comments（逐节）

### Abstract
- 约 147 words，符合限制
- 第 5 句 "Generator-agnostic" 需加 "under continuation mode"
- 第 6 句 filtering 声明需加 "at high contamination ratios"

### Section 1 (Introduction)
- Contribution (a)(b)(c) 定位为 empirical finding，基本合理
- 建议在 contribution list 后立即提及 θ 敏感性，设置正确预期

### Section 2 (Related Work)
- 覆盖 model collapse / binary detection / data curation / ordinal classification 四个方向
- 遗漏 watermarking 作为 provenance tracking 替代方案（1-2 句定位即可）

### Section 3 (Method)
- K*_empirical 定义（Eq. 1）形式化清晰
- θ=0.60 的 Cohen's h 映射需更严格论证（AUC ≠ proportion）
- 15D 特征描述完整（Table 14），OBD-LightGBM 超参数明确（Table 15）

### Section 4 (Experiments)
- 覆盖面广：10 configs × 4 domains × 4 decoding × cross-transfer × neural probe
- "6/10 yield K*=2" 需加 per-family 去重统计和样本敏感性讨论
- Cross-model transfer 需明确限定 continuation mode

### Section 5 (Filtering)
- 100% synthetic setting 过极端；需更充分引用 dose-response 结果
- 建议重新定位为 "consistency check under extreme contamination"

### Section 6 (Discussion)
- "One-wash laundering" 命名与 K*=2 存在逻辑矛盾——K*=2 意味着需两次生成
- Retrain-chain 段落信息密度过高，建议拆分
- 建议明确区分 one-wash laundering (discriminability loss) vs model collapse (quality loss)

### Section 7 (Conclusion)
- 简洁但需修改 filtering 和 generator-agnostic 声明

### Limitations
- 覆盖 scope/features/threshold/domain 四点，诚实全面
- 已承认 ≤8B 和无 RLHF/DPO 模型的局限

### Appendix
- 29 张表格，全面的 sensitivity analysis
- Table 28 (5K vs 10K) 的 key findings 建议提升至正文
