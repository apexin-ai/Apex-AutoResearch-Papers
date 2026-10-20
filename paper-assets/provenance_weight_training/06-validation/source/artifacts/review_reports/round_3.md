---
round: 3
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-19T06:07:52.890679+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Review)

**论文**: Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining
**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验+统计; R2: 新颖性+叙事+Related Work+格式）
**审稿轮次**: Round 1 独立初审 → 交叉分享 → 收敛（1 轮收敛，关键问题全部达成共识）

---

## Summary

本文提出 Minimum Intervention Reweighting (MIR)，在 detect-and-reweight 框架 w(x)=(1-q(x))^b 下，通过 per-batch 双约束优化（α_eff(b) ≥ τ 质量下限 + ESS(b) ≥ n_min 稳定性上限）自动选择最小 b，消除 grid search。在 Qwen3-0.6B 续训（132M FineWeb tokens, 40% 合成污染）上，adaptive b* 与 grid-best 竞争（gap 0.031 PPL, 95% CI [-0.039, 0.101]），将搜索从 9 次训练降至 1 次。论文还发现 D&R 的优势完全来自多 epoch 暴露（epoch-matched Δ=0.006），以及判别式检测器（而非生成式）是 reweighting 有效性的必要条件。

---

## Strengths

**S1. D&R Epoch Confound 发现（独立社区价值）** [共识]
Table 2 的 epoch-matched 实验干净地分离了 data exposure 和 filtering quality：D&R 全长 17.290 vs. epoch-matched 17.657（Δ=0.367 完全来自多 epoch），3-seed 验证。这是一个有纠偏价值的 corrective finding，无论方法本身是否被接受。

**S2. Detector Type 发现（实践指导意义）** [共识]
GPT-2 PPL (AUC=0.91) 反而使 adaptive 退化 (+0.10)，证明 AUC 不等于 reweighting effectiveness。discriminative vs. generative 的区分对实践有指导意义，这个发现可能比方法本身更有影响力。

**S3. 诚实透明的 Limitations** [共识]
论文对自身局限的讨论异常坦诚：ρ=0.2 失败、downstream mixed、1.7B 无优势、CI 包含退化。Conclusion 明确承认 "the method's primary value lies in the 0.6B continued pretraining regime tested here"。在该领域少见。

**S4. 框架设计优雅** [共识]
将 b 选择形式化为双约束优化，两个约束具有自然的对立单调性（Proposition 1 & 2），比 grid search 更有原则性。

**S5. 写作和格式** [共识]
写作干净，无 em-dash/en-dash AI 痕迹，无过度分段，技术术语使用精准。格式完全合规（ACL review 模板, double-blind, 行号开启, Limitations section, Responsible NLP Research Checklist 认真填写）。

**S6. 可复现性高** [共识]
算法、超参、训练配置、detector 细节（Appendix J）描述充分。R1/R2 均给出 Reproducibility 4/5。

---

## Weaknesses

### Critical（影响接收决定）

**C1. 新颖性不足以支撑 Main Conference** [R1 AGREE, R2 raised; 共识]
论文使用与 Drayson et al. (2025) 完全相同的公式 w=(1-q)^b。全部方法创新在于 b 的选择方式：
- (i) per-batch vs fixed b：工程层面改进
- (ii) loss reweighting vs SIR resampling：实现选择差异
- (iii) lightweight detector suffices：实验发现而非方法贡献
- α_eff 约束是 Wang et al. (2026) 收敛理论的直接操作化；ESS 约束是 importance sampling 标准做法 (Kish 1965)
- "Minimum intervention" 本质是在两个单调函数上取 infimum，属标准约束优化

论文最有价值的贡献（D&R epoch confound, detector type finding）是**分析性发现**而非方法贡献，但当前 framing 将方法置于核心（Contribution 1）。两位 Reviewer 一致建议重新定位：以 analytical study 为主、method 为辅。

**C2. 效应量极小，下游任务不支持 PPL 改善的实际意义** [R1 raised, R2 AGREE; 共识]
- ρ=0.4: Δ = -0.043 PPL (0.24% relative)，在续训已吸收 5.2 PPL 的残差区间内
- ρ=0.6: Δ = -0.028 (减弱)
- 1.7B: Δ = -0.01 (negligible)
- Downstream: 5 个 benchmark 中 4 个为负（ARC-C -0.005, ARC-E -0.007, HellaSwag -0.005, WinoGrande -0.008），sign-test p≈0.19
- PPL 改善可能仅反映 distribution matching（训练数据更接近 human-only 评估集），而非真正的模型质量提升
- Abstract/Introduction framing 给出比实际证据更强的印象

**C3. "Competitive with grid-best" 的 framing 与统计证据不一致** [R1 raised, R2 AGREE; 共识]
- 95% CI [-0.039, 0.101] 包含 0.101 PPL 的降级（upper bound 是 effect size 的 2.3x）
- Abstract 将 gap (0.031) 与 cross-seed variance (±0.033) 做比较，但这是两个不同统计量（paired variability vs. marginal variability）
- N=3 下 CI 过宽是 power 不足的结果，不是等价性的证明
- §5.1 的 "we refrain from claiming statistical indistinguishability" 是正确的审慎态度，但 Abstract 和 Conclusion 的措辞与此矛盾

**C4. 1.7B "transfers without degradation" claim 缺乏统计支撑** [R1 raised, R2 AGREE; 共识]
- 2 seeds adaptive (13.25, 13.27) vs. 1 seed uniform (13.26)
- Δ = -0.01 在任何标准下都无法区分 noise 和 signal
- §5.2 的 "confirming" 用词过强
- 效应量从 0.6B 到 1.7B 缩小 4x，equally consistent with "no effect at this scale"

**C5. 自污染实验设计严重限制泛化性** [R2 raised as critical, R1 AGREE; 共识]
- Self-contamination (generator=trainee) 是最容易检测的场景，不是论文声称的 "challenging detection scenario"
- TF-IDF+LR 在此场景下达到 AUC=0.94 恰好证明了检测的容易性
- 真实 web 污染的关键挑战（多源异构、非均匀混合）在 uniform random mixing 设计中完全缺失
- Limitations section **没有**将 self-contamination 作为独立限制讨论
- Cross-model 结果 (Appendix H) 单 seed、mixed results、缺少 PPL（"checkpoints not retained"）

### Warning（影响评分但不一票否决）

**W1. B=4 下 α_eff 仅 5 个离散值，与 "连续优化" 叙事不一致** [R1: critical N4; R2: should-fix W6; 严重程度分歧]
- B=4 时 α_eff ∈ {0, 0.25, 0.5, 0.75, 1.0}，bisection 在阶梯函数上运行
- Pearson r≈0.70（51% 方差未解释），MAE=0.114
- R2 反驳严重程度：bisection 仍正确（效率非正确性问题）；B=8/16 验证 PPL <0.01 差异
- 共识：substance 成立，但方法描述与实际操作之间存在失配，需在§3.3 承认

**W2. "Robust defaults" 声明验证不足** [共识]
- τ sweep 基于 seed 42, ρ=0.4 单次实验
- ρ=0.6 时 optimal τ shift 到 0.7（Figure 3）
- "empirically robust defaults that transfer without per-model tuning" 仅在 1 个模型、2 个 ρ 值上验证
- 建议弱化为 "default values that perform well in the tested configurations"

**W3. Grid search 在 ρ=0.6 为单 seed** [共识]
- Table 5: Grid b=0.3 at ρ=0.6 仅 seed 42 (17.634)
- Adaptive 3-seed mean 17.736 vs Grid 单 seed，gap 0.102 不具可比性
- §5.2 "gap widens from 0.013 to 0.106" 叙述不可靠

**W4. "D&R" 缩写在 Abstract/Introduction 中未定义** [共识]
- Abstract line 9, Introduction contribution #2 直接使用，全称首次出现在 §4

**W5. 下游评估不充分** [共识]
- 5 benchmarks, single seed, 4/5 negative Δ
- 放在 Appendix 而非正文，且 caption 称 "preserves downstream performance"（over-positive interpretation）
- 建议纳入正文并诚实讨论 PPL-downstream 脱节

**W6. p<0.01 (N=3) 需要附带 caveats** [共识]
- 2 df, t 分布尾部极厚，正态性假设不可验证
- 建议报告 exact paired differences，注明 sample size 限制

**W7. 缺少近期重要相关工作** [R2 raised, R1 AGREE with caveat]
- R2 识别 3 篇未引用论文：Kang et al. (EMNLP 2025), Zhang et al. (2025 ForTIFAI), Yi et al. (2025)
- R1 无法独立验证存在性但原则同意应覆盖
- 当前 41 条引用偏少

**W8. Scale mismatch: Introduction 框架 web-scale 但实验 132M tokens** [共识]
- Introduction 以 "Web corpora increasingly contain machine-generated text" 开头
- 实验规模与 web-scale 差 4 个数量级
- 建议 Introduction 明确限定为 "continued pretraining on moderate-scale corpora"

**W9. "Minimum intervention" 缺乏最优性证明** [R1 raised, R2 partially rebuts]
- 选择 b*=b_τ (minimum) 而非中间值是设计直觉
- R2 反驳：ESS-only ablation (maximum) 已显示退化，minimum > maximum 已建立
- 但 (b_τ+b_ESS)/2 等中间策略未测试
- 共识：应标注为 "empirically motivated strategy"，不暗示最优性

---

## Reviewer Consensus

以下问题两位 Reviewer **完全一致**（[AGREE]）：

1. 效应量过小（0.043 PPL, 0.24%），下游 4/5 为负，PPL 改善可能是 distribution matching artifact
2. 1.7B claim 统计不支撑（2 seeds vs 1 seed, Δ=-0.01）
3. "Competitive" framing 与 CI [-0.039, 0.101] 矛盾
4. 新颖性不足以支撑 Main Conference（同一公式，不同 b 选择）
5. 自污染设计限制泛化性，Limitations 未充分讨论
6. "Robust defaults" 验证不足
7. Grid ρ=0.6 单 seed 比较不可靠
8. 下游评估不充分
9. D&R 缩写未定义
10. p<0.01 (N=3) 需要 caveats
11. 分析性发现（epoch confound, detector type）比方法本身更有价值

---

## Reviewer Divergence

| 问题 | R1 | R2 | 分析 |
|------|----|----|------|
| B=4 离散化严重程度 | Critical (N4) | Should-Fix (W6) | R2 认为正确性不受影响，B=8/16 已验证。Director 判断：Should-Fix 更合理，离散化不影响算法正确性 |
| Epoch-matched LR confound | Should-Fix (W3) | REBUT（方向有利） | R2 认为 schedule 差异的方向对论文结论有利而非不利。Director 判断：R2 分析合理，但应在论文中简要讨论 |
| Minimum intervention 最优性 | Should-Fix (W6) | REBUT（ablation 已足够） | R2 认为 min > max 已通过 ESS-only ablation 建立。Director 判断：中间策略未测试是 completeness gap，但不构成 soundness 问题 |
| Overall 评分 | 2.5/5 (Borderline Findings) | 3.0/5 (Findings) | R1 对效应量权重更大。Director 综合判断见下 |

---

## Questions（需要作者澄清）

1. 如果 PPL 改善仅反映 distribution matching（训练数据更接近 human-only 评估集），方法的核心 value proposition 是什么？
2. 在 B=4 的阶梯函数上，per-batch adaptation 的实际机制是什么？是 α_eff 的精确值驱动了 b* 的选择，还是其他因素（如 batch-level contamination composition 的变异性）？
3. 论文 Conclusion 承认 "primary value lies in the 0.6B continued pretraining regime"——如果方法不 scale，它的 target audience 是谁？
4. Midpoint 策略 b* = (b_τ + b_ESS)/2 是否测试过？如果 minimum 是唯一测试的 feasible region 内策略，"minimum intervention" 的 claim 缺乏对照
5. Self-contamination 设计下 AUC=0.94 是否代表了真实 web 污染场景下的检测器性能？如果真实场景 AUC 显著更低，α_eff proxy 的可靠性如何？

---

## Missing References（R2 识别，R1 原则同意）

| 论文 | 为什么相关 |
|------|-----------|
| Kang et al. (EMNLP 2025) "Demystifying Synthetic Data in LLM Pre-training" | 大规模 synthetic data mixing 研究（>1000 LLMs），直接相关 |
| Zhang et al. (2025) "ForTIFAI" (arXiv:2509.08972) | 不依赖检测器的 model collapse prevention（Truncated CE loss），替代方案 |
| Yi et al. (2025) "Escaping Model Collapse via Synthetic Data Verification" (arXiv:2510.16657) | Verifier-guided retraining 理论分析，与 α_eff 动机相关 |

注：R1 无法独立验证这些论文的存在性，建议 Research Director 核实后决定是否引用。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。项目配置中无 `external_review.paperreview_ai.enabled` 字段。

---

## Overall Assessment

**Overall Score: Weak Reject (for Main Conference) / Borderline Accept (for Findings)**

**评分依据:**
- R1: 2.5/5 (Borderline Findings)
- R2: 3.0/5 (Findings)
- Director 综合: **Weak Reject for Main Conference, potential Findings-level accept**

**核心判断:**

论文技术执行干净、写作诚实，但存在两个根本性问题：

1. **新颖性不足以支撑 Main Conference**。核心方法对 Drayson et al. (2025) 的增量有限——同一公式，不同的 b 选择策略。双约束框架虽优雅，但各组件（α_eff 约束、ESS 约束、bisection）均来自已有工具的组合。

2. **实验证据系统性地弱于 claims**。效应量极小（0.043 PPL, 0.24%），下游 4/5 为负，1.7B 无 measurable advantage，CI 包含 substantial degradation。论文在 Limitations 和 Conclusion 中审慎表述，但 Abstract 和 Introduction 的 framing 过度乐观。

**论文最有价值的部分是两个分析性发现**：(1) D&R 优势完全来自多 epoch 暴露（Table 2）；(2) 检测器 signal type 而非 AUC 决定 reweighting 有效性。这些发现有独立社区价值，但在当前 framing 中被方法论述遮盖。

**建议投稿路径:**
- **Findings track**: 重新 frame 为 analytical study（epoch confound + detector type 为主要贡献，method 为实用工具），补充下游评估和统计 caveats 后，Findings 级别可行
- **Main Conference**: 需要显著增强实验证据（更多 seeds、更大规模、下游转化、cross-generator 验证）或提出本质不同的方法创新

**置信度**: 4/5（两位 Reviewer 在关键问题上独立达成高度一致，增强了判断的可信度）

---

## Detailed Comments

### Abstract (sections/abstract.tex)
- "eliminating the need for exhaustive search (nine runs to one; 95% CI of gap [−0.039, 0.101], which includes possible degradation)" — 后半句削弱前半句的 claim，造成 Abstract 内部信息矛盾。建议选择一个一致的 framing [R1]
- "D&R's full-length advantage" — D&R 缩写未定义 [共识]
- 字数偏多（约 280 words），数据堆砌过多，建议精简到 ≤250 words [R3-W2 延续]

### Introduction (sections/introduction.tex)
- Line 1 "Web corpora increasingly contain machine-generated text" 开启 web-scale framing，但实验仅 132M tokens / 0.6B。建议明确 scope 为 continued pretraining [共识]
- Contribution list 将方法置于 #1，分析发现置于 #2 和 #3。建议颠倒优先级，以 analytical contributions 为主 [共识]
- "D&R's reported advantage" (contribution #2) — 缩写未定义 [共识]

### Method (sections/method.tex)
- §3.2 Proposition 1 proof sketch: "better-than-random discrimination" 条件对 Cov ≥ 0 是冗余的（given r_i = 1[q_i ≤ 0.5]，covariance non-negativity is by construction）[R3-W8 延续]
- §3.3 "we compute b* at the micro-batch level (B=4)" — 应明确承认 B=4 下 α_eff 仅 5 个离散值，bisection 退化为离散 lookup [R1-N4 / R2-W6]
- §3.4 "empirically robust defaults" — 验证不足，建议弱化表述 [共识]

### Experiments (sections/experiments.tex)
- "creates a challenging detection scenario" — 实际上 self-contamination 下 AUC=0.94 证明这不 challenging。建议移除或改述 [R1 交叉回应]

### Results (sections/results.tex)
- §5.1 "competitive with grid-best" 与后文 CI caveat 矛盾 [共识]
- §5.1 downstream 结果不在正文——4/5 negative 的 pattern 应在正文讨论 [R1-N1]
- §5.2 "confirming that the method transfers to larger scale without degradation" — 2 seeds 不足以 "confirm"，改为 "preliminary evidence suggests" [共识]
- §5.2 ρ=0.6 Grid 比较为单 seed，"gap widens" 叙述不可靠 [共识]

### Discussion (sections/discussion.tex)
- "the selected exponent is 4.9× lower than the ESS-only upper bound" — 有价值但本节整体仍偏薄
- 缺少 PPL-downstream divergence 的讨论 [R1-N1]

### Limitations (sections/limitations.tex)
- 缺少 self-contamination 设计作为独立限制的讨论 [共识]
- "Cross-model transfer" 段落讨论 Llama-3.2-3B 但这是 cross-generator transfer，不是 self-contamination 限制

### References (references.bib)
- wang2026survive (arXiv:2602.16065): 2026 年 2 月 arXiv，需验证存在性 [R2]
- 可能缺少 3 篇近期相关工作 [R2-W4]
- 总数 41 条偏少 [共识]

### Appendix (sections/appendix.tex)
- Detector details (Appendix J) 现在完整 [resolved]
- Cross-model table (Appendix H, Table 10) 存在但 single seed + no PPL [R3-M4]