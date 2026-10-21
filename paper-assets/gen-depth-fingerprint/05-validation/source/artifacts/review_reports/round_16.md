---
round: 16
overall_score: 3.0 (Findings)
timestamp: 2026-05-18T09:25:15.048361+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 17 (Fresh Review)

**论文**: "Depth Fingerprinting: Detecting Recursive Generation Depth in Base LLM Text Chains"
**目标 Venue**: EMNLP 2026 (via ACL Rolling Review, May cycle)
**截止日期**: 2026-05-25 (AoE)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+写作质量+格式合规+相关工作）

---

## Summary

本文提出 generation depth classification 任务，将传统 binary（human vs. AI）检测扩展为三类分类（gen-0/gen-1/gen-2+），并发现 differential depth response (DDR)：递归生成中，central-tendency 特征（entropy mean, TTR, hapax ratio）随深度单调漂移，而 shape 特征（entropy max, tail decay）保持近似静态。基于 7 个特征 + XGBoost 分类器，在 8 个 base model generator (0.6B-8B) 的 LOGO 评估下达到 leak-free binary F1=0.694。实验设计全面，包含 seed sharing 控制、cross-model chains、temperature/prompt-type sensitivity 分析等。

---

## Strengths

1. **新颖的任务定义**: 从 binary detection 扩展到 ordinal depth classification 是概念上有意义的贡献，与 model collapse 和 data provenance 文献有清晰连接。[R1, R2 AGREE]

2. **系统化的 confound 控制**: Seed demeaning + independent-seed 实验排除 topic fingerprint（§4.1）、length-matched subsampling 排除长度混淆（Appendix B）、cross-domain/temperature/prompt-type robustness 分析。这种系统性在 AI-text detection 文献中较为少见。[R1, R2 AGREE]

3. **DDR 分解的分析价值**: 将特征分为 drifting 和 stationary 两类，提供了理解递归生成统计特性的有用分析框架。Cohen's d、Spearman ρ、Levene test、CV shift 多维度验证。[R1, R2 AGREE]

4. **诚实的局限性报告**: Instruction tuning 信号崩溃、模型规模限制、温度敏感性等负面结果均如实报告，未掩盖核心弱点。[R1]

5. **写作质量良好**: AI 写作痕迹极少（0 em-dash, 0 黑名单词汇）。引用完整（59 篇，0 orphan，0 missing）。[R2]

6. **计算效率优势**: 单个 410M 参考模型 + 7 特征 + XGBoost = 9.7 ms/text，相比 multi-detector ensemble (22.8 ms) 成本优势显著。[R1]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, CONSENSUS] **正文页数超限（~8.12 页 vs. 8 页限制）**
- PDF 编译核实：Conclusion 结束于 Page 9 约 12%，Limitations 从此处开始。主体内容（Sections 1-6）约 8.12 页。
- ARR CFP: "Submissions that exceed the length requirements will be desk rejected."
- 两位 Reviewer 均 AGREE 这是 desk reject 风险。
- **Action**: 压缩 Discussion (当前约 1.5 栏) 和 Results 中部分冗余分析，确保 Conclusion 在 Page 8 内结束。

**MF2** [critical, CONSENSUS] **DDR 二分框架内部不一致**
- entropy_std (d=0.55, |ρ|=0.16) 和 entropy_min (pooled |ρ|=0.40) 不符合 drifting/stationary 二分框架。7 个特征中 28.6% 需要"qualification"（§4.2 原文承认）。
- 两位 Reviewer 均 AGREE：建议改为三分法（drifting/intermediate/stationary），这比强行塞入二分框架更诚实，且 intermediate 类本身是有趣的发现。
- **Action**: 修改 DDR 叙事为三分类；Abstract/Intro/Results 同步更新。

**MF3** [critical, CONSENSUS] **Instruction tuning 信号崩溃 + 论文 framing 脱节**
- OLMo-2-1B-Instruct LOGO F1=0.338 vs. base 0.763（Limitations, Page 9）。
- Introduction 以"LLM text re-enters the web"为动机，暗示实际检测应用；但方法仅适用于 base model 输出，在当前 LLM 生态中极为少见。
- 两位 Reviewer 均 AGREE：动机与适用范围严重脱节。
- **Action**: 重新 frame 论文贡献为分析性/科学性发现（understanding distributional drift under recursive generation），弱化 practical detection/curation claims。

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, DIVERGENT] **与并发工作（Broken Telephone, Markovian Chains）增量贡献区分不充分**
- R2 升为 Must-Fix：DDR 的 drifting features 与 Broken Telephone 的信息失真高度重叠；DDR 可能只是 Markovian Chains 理论预测的实证验证。
- R1 REBUT：DDR 提供特征层面的操作化分解 + LOGO 跨生成器分类 + 全面 confound 控制，这些是 task-oriented 贡献。但同意 Related Work positioning 论证不够清晰。
- **共识方向**: novelty 存在但 positioning 不足。§2.2 和 Introduction 需明确列出 unique contributions。

**SF2** [warning, DIVERGENT] **DDR vs model collapse 因果区分不足**
- R2 升为 Must-Fix：DDR 是否只是 model collapse 在 inference-time 的微观表现？
- R1 REBUT 降级 Should-Fix：training-time vs inference-time 概念区别清晰；但同意 Discussion 需扩展论证。
- **共识方向**: Discussion 增加 1-2 段系统性分析。

**SF3** [warning, CONSENSUS] **Baseline 比较方法论不够公平**
- 将 binary detection 方法的分数 repurposed 为 ordinal depth predictors，与专门设计的 7 特征比较不是 apples-to-apples。
- §4.3 的 "contextualize" framing 部分缓解，但 Table 2 的并排呈现暗示竞争性对比。
- **Action**: §4.3 开头明确声明比较意图。

**SF4** [warning, CONSENSUS] **Abstract 数据密度过高**
- ~200 词内 8+ 个具体数值，削弱叙事力。
- **Action**: 精简至 3-4 个关键数字。

**SF5** [warning, CONSENSUS] **Feature selection 缺少系统化方法论**
- 未讨论为什么选这 7 个特征而非 NLL skewness/kurtosis、句法复杂度、repetition metrics 等。LOFO 是事后验证。
- **Action**: §3.3 补充特征空间探索说明。

**SF6** [warning, DIVERGENT] **模型规模覆盖不足（0.6B-8B）**
- R1 升为 Must-Fix（Table 1 显示下降趋势）。R2 部分 REBUT：Pythia 族内规模增大 F1 略升，趋势非单调，更可能是架构差异而非规模衰减。
- **共识**: 缺少 >8B 数据点是 gap。Limitations 应明确声明规模边界。

**SF7** [warning, CONSENSUS] **Introduction 缺少"why depth matters"的中间论证**
- 从 binary detection 到 depth classification 的跳跃缺少动机论证。
- **Action**: 补充 depth 的信息价值说明。

### Nice-to-Have

1. DDR 阈值（|ρ|=0.10, d=0.10）在正文中引用 Cohen's benchmarks + 概括 Appendix L 的 equivalence test 结果 [R1 提出, R2 部分 REBUT: Appendix L 已有 Lakens 2017]
2. 术语统一："generation depth" vs "recursive generation depth"；Introduction 明确定义 "fingerprinting" 含义 [R1, R2]
3. Table 1 中 "---" 改为 "—" 或 "N/A" [R2]
4. Bib entry author 格式统一（self_consuming_mad, qwen3, llama3）[R1, R2]
5. Stylometry 引用补充 2015 后综述 + Tang et al. 2024 CACM detection survey [R1, R2]
6. Responsible NLP Checklist 确认包含在提交材料中 [R2]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全共识 [AGREE]：

| # | 问题 | 严重性 |
|---|------|--------|
| MF1 | 正文超 8 页限制 | critical |
| MF2 | DDR 二分框架不一致 | critical |
| MF3 | Instruct 信号崩溃 + framing 脱节 | critical |
| SF3 | Baseline 比较不公平 | warning |
| SF4 | Abstract 数据密度 | warning |
| SF5 | Feature selection 方法论 | warning |
| SF7 | Introduction 动机不足 | warning |

## Reviewer Divergence

| # | 问题 | R1 | R2 | 分歧实质 |
|---|------|-----|-----|----------|
| SF1 | 并发工作增量 | Should-Fix (writing issue) | Must-Fix (novelty concern) | R1 认为 DDR 特征分解 + LOGO 是增量贡献，R2 认为增量不充分 |
| SF2 | DDR vs model collapse | Should-Fix | Must-Fix | R1 认为概念区别清晰，R2 认为因果关系需论证 |
| SF6 | 模型规模 >8B | Must-Fix (下降趋势) | Warning (趋势非单调) | 数据解读不同：R1 看整体趋势，R2 看族内趋势 |

---

## Questions for Authors

1. 是否有任何 >8B base model 的实验数据（即使是 pilot）？
2. Instruction tuning 信号崩溃的根本原因：是消除了 depth-dependent NLL 结构，还是引入了更强的 prompt-dependent 变异？
3. entropy_std 为什么有高 Cohen's d (0.55) 但低 Spearman ρ (0.16)？是否存在非单调关系？
4. 如果将论文重新定位为 phenomenon paper，core contribution 是否应仅聚焦 DDR 发现而非 classification pipeline？
5. DDR 的 stationary component 在 model collapse 文献中是否有对应物？

---

## Missing References

1. **Tang et al., 2024** "The Science of Detecting LLM-Generated Text" (CACM) — detection 综合综述
2. **Neal et al., 2017** "Surveying Stylometry Techniques and Applications" — 补充 stylometry 近年综述
3. **Kirchenbauer et al., 2024** (ICLR) — watermarking depth-robustness（如与已引用 2023 ICML 版本不同）
4. Stylometry 方向仅引 Stamatatos (2009) 和 Koppel (2009)，缺 2015 后更新

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.0 | 3.0 |
| Excitement | 3.0 | 2.5 | 2.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.0 | 2.5 | 3.0 |

**评分理由**:

本文的核心贡献——generation depth classification 任务定义 + DDR 现象发现——对 AI-text detection 和 model collapse 社区有科学参考价值。实验设计全面，confound 控制系统化，统计方法论整体规范，写作质量良好。

阻止达到 Conference (4.0) 的主要因素：
1. **适用范围根本性受限**：仅 base models (0.6B-8B)，instruction tuning 下信号近乎崩溃（F1: 0.763→0.338），几乎无实际部署场景
2. **DDR 框架内部不一致**：28.6% 特征不符合二分框架，核心叙事需修正
3. **与并发工作的增量论证不足**：Broken Telephone 和 Markovian Chains 覆盖了相邻的研究空间，论文的 unique positioning 需更有力论证
4. **页数超限**：~8.12 页，存在 desk reject 风险

论文适合 Findings track：提供了有意义的实证发现和分析框架，尽管实际影响力受限。若能修复页数问题、将 DDR 改为三分类、重新 frame 为科学发现、加强与并发工作的区分论证，有潜力稳固在 Findings (3.0) 水平。

**Confidence: 4/5**（两位 Reviewer 均熟悉 AI-text detection、model collapse、统计分析方法）

---

## Detailed Comments (by Section)

### Abstract
- 数据密度过高（8+ 数字/200 词），建议精简至 binary F1 + cross-model F1 + Cohen's d 范围
- "shape features remain near-stationary" 需改为三分类表述

### Introduction (§1)
- 开头动机（"LLM text re-enters web"）与方法适用范围（仅 base models）脱节，需重新 frame
- 缺少"为什么 depth 比 binary 更重要"的中间论证
- Contribution 列表清晰，但应删除或弱化 practical implication 相关表述

### Related Work (§2)
- 与 Broken Telephone / Markovian Chains 的区分需扩展为完整段落，明确列出 3 个 unique contributions
- Stylometry 引用仅 2 篇经典综述（2009），需补充近年更新
- 引用密度整体合理（59 篇），0 orphan / 0 missing

### Method (§3)
- Feature selection 缺少系统化方法论说明（为什么这 7 个而非其他候选）
- "entropy_min" 首次出现时应明确定义
- 其他方面（task formulation, generation chain construction, evaluation protocol）清晰完整

### Results (§4)
- DDR 描述需从二分改为三分（drifting/intermediate/stationary）
- Table 1 的 3-class F1 caveat 已到位（dagger footnote），但 Abstract 和 §4.1 第一段仍突出 3-class 数字
- Baseline 比较 (§4.3) 需明确声明 contextualization 意图
- 统计方法整体规范（Bootstrap CI, Bonferroni, McNemar, Cohen's d）

### Discussion (§5)
- 需增加 DDR vs model collapse 的系统性区分段落
- 温度敏感性讨论可更突出（当前主要在 Appendix）
- 需压缩以解决页数超限

### Conclusion (§6)
- 需压缩以确保在 Page 8 内结束

### Limitations
- 内容充实且诚实，覆盖了核心弱点
- instruct model 结果如重新 frame 为科学发现，此处的讨论需相应调整

### Ethics Statement
- 覆盖充分（许可证、计算预算、软件版本）

### Appendix
- 15 个 appendix 数量偏多，建议合并相关分析（如 temperature sensitivity + cross-temp transfer）
- 关键结果（如 equivalence test, Appendix L）可在正文中一句话概括