---
round: 11
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-20T06:53:51.171860+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — recursive_gen_depth_est (Round 14, Fresh)

**论文**: "How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints"
**目标 Venue**: EMNLP 2026 (ACL Rolling Review May cycle)
**投稿类别**: Long Paper (ARR)
**审稿团队**: Reviewer 1（方法严谨性）+ Reviewer 2（新颖性与完整性）
**审稿模式**: Fresh（重新审稿）
**日期**: 2026-05-20

---

## Summary

本文将递归生成深度估计形式化为序数分类任务，构建了涵盖 3 个模型家族（Pythia-1.4B, OLMo-1B, GPT-2 XL）× 3 种解码策略 × 4 个深度的 180K 样本 benchmark。基于 19 个统计特征的 Random Forest 分类器在 in-distribution 设定下达到 59–82% 四类准确率（d1-d3 balanced: 58.9–81.5%），并提出 Effective Discriminable Depth (EDD) 指标量化相邻深度的可判别性。论文系统分析了跨模型（66.4%, d1-d3: 55.4%）、跨策略（59.1%, d1-d3: 45.9%）和跨规模（7-14B）的泛化性能，发现 perplexity tail 特征族（p90_ppl, kurtosis_ppl）和 surprisal variance 在所有 9 个实验单元中占主导地位。

---

## Strengths

**S1. 任务定义新颖且有价值** [R1, R2 一致]
将递归生成深度估计从 binary human/machine detection 推进到 ordinal depth classification，是 model collapse 文献中被忽视的逆问题。经搜索确认无先前工作显式处理此问题。问题定义清晰（Definition 1），具有理论意义和实际价值。

**S2. Benchmark 设计系统** [R1, R2 一致]
180K 样本覆盖 3×3×4 完整网格，控制变量严格（固定 LoRA 配置、固定 reference model、固定 seed text）。Domain bias analysis（Appendix B.8）包括 bug 修复的透明披露，体现了实验诚信。15 页附录含 23 个子实验，透明度很高。

**S3. Perplexity tail insight 有理论连接** [R1, R2 一致]
将 model collapse 理论（tail distribution collapse）与检测特征（perplexity tail statistics）连接。三种 importance measures（Gini, SHAP, permutation）高度一致（Kendall's W=0.90, p<0.005），perplexity tail 在 9/9 cells 中占主导地位。§3.5 的 theoretical grounding 虽非完整证明但方向正确。

**S4. EDD 指标有概念贡献** [R1]
将聚合准确率分解为逐深度边界的可判别性，提供了比单一准确率更有信息量的评估框架。EDD 上界与 contraction factor 的关系（§3.5）提供了有用的理论框架。

**S5. Limitations 异常全面** [R1, R2 一致]
整页讨论 10+ 个 limitations，包括 d0 inflation、FPR、self-reference confound、cross-strategy constraint 等。多数问题是作者自己识别并讨论的，态度坦诚。这在 submission 中较为少见。

**S6. 相关工作覆盖全面** [R2]
68 篇引用涵盖 model collapse 理论、AI text detection、data provenance、ordinal classification、decoding strategies 五个领域。引用完整性检查：0 orphan / 0 missing bib entries，57/68 online verified。

**S7. Strategy-dependent trajectory 发现** [R2]
不同解码策略产生质量不同的退化轨迹是有价值的 empirical insight，对理解 model collapse 的机制有帮助。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. [Critical] 14B "signal persists" claim 与自定义 EDD 指标矛盾** [R1-N3, R2-N1, 交叉一致 AGREE]

14B 实验（Qwen2.5-14B）EDD=0（所有三种解码策略下无相邻深度对 AUC 超过 0.70 阈值），4-class 准确率仅 50.8%（2× chance）。但 §5.4 和 §6 声称 "signal persists at 14B"——这与论文自己的 EDD 定义直接矛盾。实验同时改变 5 个变量（model family, tokenizer, training data, reference model, model scale），Appendix B.14 §Confounds 承认 "infeasible to attribute the observed accuracy gap to any single factor"，但 headline claim 忽略了这一限定。

R1 补充关键观察：d0v1 AUC 在 14B 上降至 0.561-0.643（vs 1-1.5B >0.99）。d0/d1 boundary 是整个框架中最容易的判别（human vs first-gen），这个 boundary 的崩塌暗示 14B 的信号可能根本是不同性质的，而非同一信号的 scale-dependent attenuation。

**修改要求**：(1) §5.4 标题加强 caveat（如 "Inconclusive Cross-Scale Observations"）；(2) §6 用 "above-chance accuracy is observed but cannot be attributed to depth signal due to multiple confounds" 替换 "persists"；(3) Abstract 明确声明 14B EDD=0 及其意义。

**C2. [Critical] Headline metrics 被 d0 召回率（>97%）系统性膨胀** [R1-N1, R2 AGREE]

d0（human-written）召回率 >97%（Table 2），four-class accuracy 被系统性拉高。定量分析：d0 贡献约 24.25%（0.25×97%）到总 accuracy，最低 cell 的 d1-d3 实际准确率仅约 49%（vs headline ~61%）。Cross-model transfer 66.4% 中 d0 贡献巨大，d1-d3 balanced accuracy 仅 55.4%（1.66× chance）。Pythia holdout d2 recall 仅 26.8%（Table 5）。Abstract 和 Introduction 始终以 four-class accuracy 为主指标，d1-d3 balanced accuracy 虽有报告但处于括号或脚注位置。

R2 补充：d0 是任务的合法类别——问题在于 emphasis 而非 metric 定义。应双指标并列而非以 d1-d3 为唯一主指标。

**修改要求**：Abstract 和所有 headline 处双指标并列报告（4-class accuracy + d1-d3 balanced accuracy），使读者自行判断实用性。

**C3. [Critical] 与 Binoculars 11-feature RF 无显著差异（78.4% vs 78.1%, p>0.05），Table 4 呈现不透明** [R1-N2, R2 AGREE]

Table 4 仅列出 Binoculars 的较弱配置（threshold 69.8%, RF 1-feat 63.7%），78.1% 的完整 11-feature RF 配置仅在 §5.1 正文中一句话提及（"matches our pipeline within 0.3 pp"）。这种呈现方式——在 table 中放弱版本、在文本中轻描淡写强版本——降低了论文的透明度。

Merged 30-feature 达到 82.6%（+4.2pp）表明两个管线信号互补——但互补性本身暗示 19-feature pipeline 未完全覆盖 Binoculars 信号。R2 指出论文管线仅需单一 reference model（vs Binoculars 的 observer-performer pair），这种部署优势应被明确论证。

**修改要求**：(1) Table 4 加入 Binoculars 11-feat RF 行并标注 p-value；(2) 正文明确论证相对优势（单一 reference model、无需 observer-performer pair、特征可解释性）；(3) 将 merged 82.6% 作为推荐配置而非附录内容。

**C4. [Critical] 主文超出 8 页限制** [视觉审查]

视觉审查发现 Section 6 (Discussion and Conclusion) 从 page 8 底部延伸至 page 9 上半部（约 0.3-0.5 页溢出）。Limitations 在 page 9 中部开始。EMNLP 2026 规定 long paper 正文严格限制 8 页（Limitations 和 Ethics 不计入页数），Discussion/Conclusion 属正文，这是格式违规。注：R2 格式检查误判为合规。

**修改要求**：压缩正文约 0.3-0.5 页以符合 8-page limit。

---

### Should-Fix（影响评分但不一票否决）

**W1. Full-replacement 假设限制生态效度** [R2: critical, R1 REBUT → Director 裁定: Should-Fix]

所有实验使用 full-replacement 递归链。Real-world contamination 是 accumulation（partial mixing）。Gerstgrasser et al. (2024) 已证明 accumulation 可避免 collapse。Curation PoC（Appendix B.22）结果 inconclusive（p>0.4）。

R1 反驳（Director 采纳）：full-replacement 是 controlled study 的必要起点——消除 mixing ratio 连续混淆变量，使 depth 成为唯一自变量。论文定位为 upper bound 合理。Prompted generation（69.5%, -13.8pp）和 mixed-depth corpus 提供了 partial relaxation。作为 Findings 论文在 controlled setting 下建立 feasibility 已足够。完整 accumulation 实验是重要的 future work，但其缺失不否定当前贡献。

**修改建议**：Discussion 中加深 accumulation 场景分析。

**W2. 算法贡献有限** [R2: critical, R1 AGREE with nuance → Director 裁定: Should-Fix]

核心方法是标准 RF（200 trees, 5-fold CV）+ 19 个标准统计特征。论文诚实定位为 "task formalization and systematic empirical characterization"。R1 指出 passage-level distributional aggregation（p90_ppl, var_surprisal, kurtosis_ppl）区别于 token-level 方法（GLTR, DetectGPT），是非 trivial 的特征工程选择。更关键的是，RF 大幅优于 neural 方法（Appendix B.7: PLM [CLS] representations yield negative R² for var_surprisal and p90_ppl）——"perplexity tail statistics are not linearly accessible in pretrained representation space" 可成为有价值的 insight，但未在主文充分展开。

**修改建议**：深入分析 RF vs neural 的 representational gap（将 Appendix B.7 核心结论提升到主文）；加强 EDD formalization 使其成为更有理论深度的贡献。

**W3. Self-reference 混淆使 3×3 atlas 内部不可比** [R1-W1, R2 AGREE]

Pythia-1.4B 同时作为 reference model 和 generator，self-reference 优势 4-11pp（Appendix B.11: self 78.6% vs cross-OLMo 74.5% vs cross-GPT2 67.3%）。Table 2 中 Pythia 的 78.7% 可能在 cross-reference 下降至 ~68-75%，与 OLMo 和 GPT-2 XL 的表观优势关系可能反转。Atlas 分析（§4）中所有 cross-cell 比较（如 "GPT-2 XL achieves highest accuracy"）基于不公平基础。

**修改建议**：Table 2 增加 cross-reference accuracy 列，或在 §4.1 axis effect 分析中明确声明 Pythia 行可比性受限。

**W4. Cross-strategy d1-d3 仅 45.9%（1.38× chance），实用性存疑** [R1-W2, R2-W4, 交叉一致]

d1/d2 boundary inversion（AUC<0.5）意味着某些策略下系统会系统性地反转深度判断——比随机猜测更危险。Two-stage pipeline 回收 11.5pp，但未报告 strategy classifier 本身的准确率。如果 strategy identification 不可靠，two-stage 方案的实际增益会打折扣。

**修改建议**：(1) 报告 strategy classifier 独立准确率；(2) Discussion 中明确 "decoding strategy must be known or identifiable" 为部署前提条件。

**W5. Cross-seed replication 不充分（3/9 cells）** [R1-W4, R2 AGREE]

仅 nucleus 策略 3 cells 有 2-seed replication（Appendix B.24）。OLMo seed=42 78.94% → seed=43 82.11%（+3.17pp, CI 不重叠）。Temperature 和 top-k 完全未复制。对于以系统性 benchmark 为核心贡献的论文，9/9 cells 均应有 cross-seed replication。

**修改建议**：所有 9 cells 提供 cross-seed replication。

**W6. Discussion 过于单薄** [R2-W2, R1 AGREE]

§6 约 1 页，混合讨论和结论。核心分析——multi-channel depth encoding（Appendix B.26）、RF vs neural divergence（Appendix B.9/B.7）、Binoculars signal decomposition（Appendix B.17）、cross-scale behavior（Appendix B.14）——全在 Appendix。主体 Discussion 深度不足，审稿人主要阅读 8 页正文，关键洞察在 Appendix 中容易被忽略。

**修改建议**：将 Appendix B.7（feature overlap analysis）和 B.17（Binoculars signal decomposition）核心结论提升到主文。

**W7. Curation PoC inconclusive 但语气偏乐观** [R1-W7, R2-W5, 交叉一致]

RF-filtered vs unfiltered p=0.407——主假设不成立。RF-vs-random 的 3 个 pairwise comparisons 在 Bonferroni 校正后仅 1/3 存活（rf_strict vs random_strict p=0.002 < α=0.017，另两个不通过）。§6 Discussion 仍称 "practical signal for data curation"，语气偏乐观。

**修改建议**：(1) Appendix B.10 标题改为 "Curation PoC (Inconclusive)"；(2) §6 中降低对 curation 应用的信心级别。

---

### Minor

**M1. EDD T=0.70 阈值需引用文献** [R1-W5, R2 partial REBUT]
R2 指出 AUC=0.70 对应 ROC "adequate discrimination" 的常用经验阈值（Hosmer & Lemeshow 分类标准），非凭空选择。但论文未显式引用。建议 §3.4 增加一句引用 ROC 解释标准文献。

**M2. LoRA sensitivity analysis 缺失** [R1-W3, R2 REBUT]
R2 反驳：LoRA 是 benchmark 构建工具而非核心方法，sensitivity analysis 属于 benchmark robustness 问题。Director 裁定 Minor——在 Limitations 中更明确声明此局限即可。

**M3. Perturbation-based baselines 适配不充分** [R1-W6, R2 AGREE]
DetectGPT（28.8%）和 Min-K% Prob（33.2%）从 binary 改造为 ordinal，低性能可能反映适配方法局限。Min-K% augmented feature set +0.48pp 且排名 #3 说明确实携带互补信号。建议 Table 4 注明 "adapted from binary detection"，增加 binary d0-vs-d1+ sanity check。

**M4. Bib entries 年份/作者 mismatch** [R1, R2 独立发现]
- he2021_deberta_v3: bib=2023, actual=2021
- alemohammad2024_mad: first author mismatch
- guo2024_biscope: first author mismatch
- gerstgrasser2024_accumulate, briesch2024selfconsuming: 应从 misc 更新为 inproceedings（已被会议接收）

**M5. Surface-text ablation 低估简单 baselines** [R1]
Mean perplexity（25.1%, chance level）被用作 "surface-text ablation" 代表，但 p90_ppl 单特征达 58.3%。更公平的 ablation 应使用 best single feature。

**M6. Abstract 信息过载** [R2-W1, R1 REBUT]
R1 反驳：ACL/EMNLP 惯例允许具体数字，问题在于 which numbers are highlighted 而非数量。Director 裁定与 C2（d0 inflation）合并处理——修正 emphasis 即可。

**M7. "Depth Degradation Atlas" 命名** [R2-W3, R1 partial REBUT]
R1 认为 3×3 grid + feature trajectory + EDD decay + importance heatmap 符合 atlas 使用惯例。建议折中：保留 "atlas" 但首次使用时加注 scope（"a 3×3 atlas at the 1-1.5B scale"）。

**M8. Figure 可读性** [视觉审查, R2-M4]
Figure 1 heatmap 灰度打印下区分度有限（axis labels 约正文 60%）；Figure 2/4 仅靠颜色区分线条，无 line style 差异，灰度/色盲不友好；Figure 3 confusion matrix 字号偏小。

**M9. 前 3 页无 display item + 缺少方法 pipeline 概念图** [视觉审查]
pp.1-3 连续纯文本无视觉锚点。Statistical fingerprint → RF → EDD 的多阶段框架无图示，增加审稿人认知负担。建议在 page 2 前引入方法概览图。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 通过交叉回应达成一致：

| # | 问题 | 严重度 | 共识内容 |
|---|------|--------|----------|
| 1 | 14B "signal persists" overclaiming (C1) | Critical | EDD=0 与 "persists" 矛盾；5 重混淆无法归因 → 必须修正措辞 |
| 2 | d0 inflation (C2) | Critical | 双指标并列报告；d0 是合法类别但不应膨胀印象 |
| 3 | Binoculars parity (C3) | Critical | Table 4 应包含 11-feat RF；方法优势需通过其他维度论证 |
| 4 | Cross-strategy 实用性 (W4) | Warning | d1-d3 45.9% + boundary inversion → 需报告 strategy classifier 准确率 |
| 5 | Cross-seed 不充分 (W5) | Warning | 3/9 cells + CI 不重叠 → 9/9 均需覆盖 |
| 6 | Discussion 单薄 (W6) | Warning | 核心洞察在 Appendix → 提升到主文 |
| 7 | Curation PoC inconclusive (W7) | Warning | p>0.4 主假设不成立 → 降调 |
| 8 | 评分一致 | — | Overall 3.0 (Findings) |

---

## Reviewer Divergence [REBUT]

| 问题 | R1 立场 | R2 立场 | Director 裁定 |
|------|---------|---------|---------------|
| Full-replacement 生态效度 | Should-Fix（controlled study 合理起点，upper bound 定位有效） | Critical（限制应用前景，需 accumulation 实验） | **Should-Fix** — controlled study 起点选择合理；Findings 论文建立 feasibility 已足够 |
| Abstract 信息量 | Fine（ACL 惯例允许数字） | Warning（信息过载） | **Minor** — 与 C2 合并处理 |
| LoRA sensitivity | Should-Fix（不同 rank 可能改变 shift 特征） | Nice-to-have（LoRA 是 benchmark 工具非方法） | **Minor** — Limitations 中声明即可 |
| EDD T=0.70 | Should-Fix（循环论证） | 有 ROC 经验标准支撑 | **Minor** — 需引用文献但非循环论证 |
| Atlas 命名 | 符合使用惯例（3×3 + full analysis） | 过度包装 | **Minor** — 加注 scope 即可 |
| AI 写作痕迹 | 标准学术英语，不应标记 | 可被注意到 | **不列入** — R1 反驳有效；Ethics Statement 已透明披露 |

---

## Questions（需作者澄清）

1. **Strategy classifier 准确率**：Two-stage pipeline（§5.3）中 strategy identification 模块的独立准确率是多少？如不可靠，two-stage 方案的实际增益如何？
2. **14B Pythia-referenced pipeline**：是否有使用 Pythia-1.4B（而非 self-reference）作为 14B 实验 reference model 的消融结果？这可隔离 reference model 混淆。
3. **Binoculars 部署成本**：论文管线（单一 Pythia-1.4B, 1.4B params）vs Binoculars（observer-performer pair）的实际推理时间/成本对比？
4. **d0 FPR calibration**：C4 FPR 4.7-22.4%，阈值 P(d0)≥0.15 降至 2.8%——这个阈值是在 held-out data 上选择的吗？
5. **14B feature hierarchy shift**：14B top-k 下 TTR/hapax 替代 p90_ppl/var_surprisal（Appendix B.14）——这是否暗示 14B 的 depth signal 来源不同（lexical diversity vs distributional tail）？

---

## Missing References

以下为两位 Reviewer 建议（非 must-cite，但可加强文献覆盖）：

1. **SeqXGPT**（sentence-level AI text attribution）— 与 passage-level depth estimation 形成方法论对比 [R1]
2. **PAN 2026 Shared Task**（Generative Plagiarism Detection / Voight-Kampff）— 2026 直接相关的 shared task [R2]
3. **TROVE / GenProve**（fine-grained text provenance, NAACL 2025/2026）— §2 Data Provenance 子节相关 [R2]
4. **"Collapse or Thrive? Perils and Promises of Synthetic Data in the Era of Generative AI"** (arXiv:2410.16713, 2024) — model collapse 综述补充 [R2]
5. **"Rate of Model Collapse in Recursive Training"** (arXiv:2412.17646, 2024) — collapse 速率理论，与 EDD contraction factor 分析（§3.5）相关 [R2]

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求（项目未启用外部审稿 `external_review.paperreview_ai.enabled = false`）

---

## Visual Layout Check（非评分项）

**状态**: done（2026-05-20 06:26–06:30 UTC）

| 严重度 | 位置 | 发现 |
|--------|------|------|
| **Critical** | p.8-9 | 主文（§1-6）超出 8 页限制：§6 从 p.8 底部延伸至 p.9 上半部（约 0.3-0.5 页溢出）。Limitations 在 p.9 中部开始。需压缩正文。 |
| Warning | pp.1-3 | 连续 3 页纯文本，无 display item（figure/table/equation），缺乏视觉锚点。建议在 p.2 前引入方法概览图。 |
| Warning | global | 全文缺少方法 pipeline 概念图。Statistical fingerprint → RF → EDD 的多阶段框架无图示。 |
| Warning | p.8 | Figure 3（confusion matrices）单元格数字字号偏小，打印或低分辨率下难以辨认。 |
| Info | p.6 | Figure 1 heatmap Y/X 轴标签约正文 60%，灰度打印区分度有限。建议加大字号或在 cell 内标注数值。 |
| Info | p.7 | Figure 2 legend 字号偏小；三条线仅靠颜色区分，未使用 line style。灰度/色盲不友好。 |
| Info | p.14 | Figure 4（appendix, feature trajectories）同样仅靠颜色区分。 |
| Info | pp.4-8 | 所有表格使用 booktabs 风格，排版规范，符合顶会标准。✓ |
| Info | pp.10-12 | References 格式统一，无未解析引用。✓ |

---

## Overall Assessment

### Overall Score: 3.0 — Findings（可被 Findings 接收）

**EMNLP 2026 评分标准**：3 = Findings, 3.5 = Borderline Conference, 4 = Conference

**维度汇总**：

| 维度 | R1 | R2 | 均值 |
|------|----|----|------|
| Soundness | 3.0/5 | 3.5/5 | 3.25/5 |
| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |
| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |
| Overall | 3.0/5 | 3.0/5 | 3.0/5 |

**Confidence**: 4/5（两位 Reviewer 均仔细阅读全文 + 15 页附录，核验统计检验和引用）

### 核心限制（阻止从 Findings 上升到 Conference）

1. **算法贡献缺失**：标准 RF + 已有统计特征，无方法论创新 → Excitement 低（均值 3.0）
2. **Scale 受限**：14B EDD=0（50.8%, 2× chance），在实际关心的模型规模（≥14B）上实用性未验证
3. **Cross-transfer 实用性不足**：cross-strategy d1-d3 仅 45.9%（1.38× chance），需已知策略信息
4. **与 Binoculars 无显著差异**：78.4% vs 78.1% (p>0.05)，方法附加价值需重新论证
5. **格式违规**：主文超出 8 页限制

### 升级路径（如修复以下问题，可考虑 3.5 Borderline Conference）

- 修正 14B overclaiming、d0 inflation 报告、Binoculars Table 4 透明度
- 修复页数超限
- 深化 RF vs neural 的 representational gap 分析（从 Appendix 提升到主文）
- 增加 accumulation 场景的至少一组 pilot 实验
- 完成 9/9 cells cross-seed replication

---

## Detailed Comments（逐节）

### Abstract
- 以 4-class accuracy 为主导叙事，d1-d3 balanced accuracy 未并列 → **C2**
- "scale-dependent in magnitude" 对 14B EDD=0 不够审慎 → **C1**
- 数字偏多但 ACL 惯例可接受 → **M6**

### §1 Introduction
- 问题定义清晰，gap 识别准确 → **S1**
- "empirical contribution" 定位诚实
- 未提及 Binoculars 已达 78.1% 的上下文 → **C3**

### §2 Related Work
- 覆盖全面（model collapse, detection, provenance, ordinal, decoding）→ **S6**
- 建议补充 SeqXGPT, PAN 2026, TROVE/GenProve → Missing References

### §3 Method
- Benchmark 构建系统（180K, 3×3×4 grid）→ **S2**
- Self-reference 混淆（Pythia 同时为 generator 和 reference）未在本节充分讨论 → **W3**
- EDD Definition 1 的 contiguous prefix 要求在 non-monotonic 场景下过于保守 → **M1**
- Feature design 19 个特征有据，perplexity tail 理论连接良好 → **S3**

### §4 Depth Degradation Atlas
- Feature analysis 深入一致（Kendall's W=0.90）→ **S3**
- Atlas 内部比较受 self-reference 影响：所有 cross-cell 比较（如 "GPT-2 XL achieves highest accuracy"）基于不公平基础 → **W3**
- Strategy-dependent trajectory 是有价值的发现 → **S7**
- EDD threshold sensitivity analysis 存在但缺乏文献引用 → **M1**

### §5 Generalization and Robustness
- Cross-model 66.4%（d1-d3: 55.4%）实验设计合理 → 但 d2 worst case 26.8% 应更突出
- Cross-strategy 45.9%（d1-d3）+ boundary inversion 讨论不足 → **W4**
- §5.4 14B "signal persists" overclaiming → **C1**
- Binoculars comparison Table 4 呈现不透明 → **C3**
- RF vs neural 差距（78.4% vs 53.1%）的分析在 Appendix 而非主文 → **W2**

### §6 Discussion and Conclusion
- 过于单薄（约 1 页），核心洞察在 Appendix → **W6**
- Curation 语气偏乐观（p>0.4 的主比较） → **W7**
- 超出 8 页限制 → **C4**

### Limitations
- 异常全面和诚实 → **S5**
- Full-replacement scope 声明合理 → **W1** 裁定依据

### Appendix
- 丰富（15 页，23 子实验）→ **S2**
- B.7（RF vs neural）、B.17（Binoculars decomposition）应提升到主文 → **W2, W6**
- B.22（Curation PoC）应标记为 Inconclusive → **W7**
- B.24（cross-seed）仅 3/9 cells → **W5**