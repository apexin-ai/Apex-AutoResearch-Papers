---
round: 2
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-20T13:07:30.140246+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 2 (Fresh Review)

**论文**: A Detection Phase Transition in Iterative Model Collapse
**Venue**: EMNLP 2026 Main Track (via ARR June 2026)
**截止日期**: 2026-06-15
**审稿日期**: 2026-05-20
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计 | R2: 新颖性+完整性+格式合规）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即收敛）

---

## Summary

本文发现迭代合成数据训练中 canary metric→downstream metric 的 Granger 因果可检测性在 per-generation mixing ratio α≈0.50 处呈现陡峭的 sigmoid 型跃迁（PermG 检测率从 0/8 跳至 6/8），并提出 Signal×Resolution (S×R) 框架和 Multi-Method Consensus Test (MMCT) 来解释和系统化这一现象。实验覆盖 6 个模型族（345M–6.9B）的 15 个模型-种子组合，87% 条件下确认检测。论文的方法论对比（五种统计方法在相同数据上产生 0%–75% 显著性率）对 model collapse 文献有实质性警示价值，但存在若干关键问题：内部数据矛盾、承诺的附录分析缺失、以及格式不合规。

---

## Strengths

**S1. 方法敏感性的系统暴露是核心价值。** [共识] Table 1 展示五种方法在相同数据上产生 0%–75% forward significance rate（κ=0.185），first-differencing 将 canary→perplexity 从显著变为完全不显著（F≈0, p=0.99）而保留 canary→diversity（24/24→24/24）。这一发现独立于 "phase transition" 叙事，对依赖单一方法的 model collapse 文献构成有力批判。

**S2. 诚实的 claim scoping。** [共识] 论文明确声明 Granger precedence ≠ causation，canary claim 仅限 diversity metrics（非 perplexity），MMCT 是 consensus protocol 非 novel method。这种自我约束在 ML 文献中值得肯定。

**S3. 充分的实验覆盖和 robustness checks。** [共识] 13 个 α 水平、最多 4 seeds、6 架构家族、2 数据域，加上 permutation count stability、FDR threshold sensitivity、observation window sensitivity 等检验。Cross-architecture 验证（15 组合，13 确认）提供了广泛的泛化证据。

**S4. Null-control 校准设计专业。** [共识] α=0.0 作为 FPR 校准（0/24, 3 seeds），α=1.0 作为 FNR 校准（0% FNR），是实验设计的亮点。

**S5. 实用价值。** [共识] Canary-based predictive cessation 提前一代触发，降低 58% 峰值 perplexity。四层检测分类提供从 α≥0.10 到 α≥0.50 的分级诊断。

**S6. 非单调 dose-response 是最有趣的发现。** [共识] α≈0.60 synchronous dip 非直觉，temporal resolution 压缩的解释合理——但此发现的实验支撑不足（见 W1）。

---

## Weaknesses

### Must-Fix（CRITICAL）

**W1. α=0.60 同步凹陷：内部矛盾 + 证据不足。** [R1 首发, R2 AGREE]
Section 4.1 列 α=0.60 为 "single-seed probing point"；Limitations 确认 "single seed; bf16"；但 Section 4.3 声称 "dual-seed confirmed"——三处不可能同时为真。四 regime 结构（blind/onset/synchronous dip/detection）中，synchronous dip 是区分本文四 regime 与简单三 regime 的关键，但仅有 single-seed bf16 一个数据点支撑。如果 dip 是精度伪影或 seed 偶然，S×R 框架的 R→0 解释将失去实验锚点。

**W2. Specification curve analysis (1,160 specs) 声称但缺失。** [R1 首发, R2 AGREE]
Section 4.2 最后一句声称此分析存在，但正文+附录（~15 页）中无任何图表、数据或描述。对以 "analytical robustness" 为核心定位的论文，unsubstantiated claim 严重损害可信度。

**W3. 更多 promised appendix content 缺失。** [R1 首发, R2 AGREE]
Section 3 承诺 "per-method dose-response profiles, Shapley value analysis, and the full MMCT algorithm appear in the Appendix"——三项均不存在。MMCT 是论文的 Contribution 3，但读者无法获得完整定义（权重公式有，但 weighted score → formal p-value 的流程、empirical null distribution 构建均不完整）。直接影响可复现性。

**W4. 格式不合规——面临 desk rejection。** [R1+R2 共识]
使用 `\documentclass[article]` + `\usepackage[numbers]{natbib}` + 自定义 geometry，非 ACL 官方模板。引用显示为 [1] 而非 (Author, Year)。ARR desk rejection checklist 第一项即模板合规。

### Should-Fix（MAJOR）

**W5. "Phase transition" framing oversells power curve crossing。** [R2 首发 CRITICAL, R1 REBUT 降为 MAJOR]
论文自身承认 "the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal"。Power = Φ(effect_size × √n / σ) 是教科书级 power analysis。R1 辩护：实证量化（sigmoid k≥200, Δα≈0.02）和方法敏感性暴露在 model collapse 领域有独立价值。**Director 判定 MAJOR**：术语需降级（"detection onset/threshold"），但实证贡献不可否认。

**W6. T=20 预测未验证 + 大部分不可证伪。** [R1+R2 共识]
三个 "testable predictions" 无实验数据（"under empirical verification"）。α=0.45 和 α=0.50 的 bootstrap CI 均为 [0,7]，几乎任何结果都 "consistent"。唯一有约束力的预测：α≥0.75 predicted 7/8 [6,8]，below 6/8 would falsify。声称 falsifiable 却不提供 falsification attempt 削弱 S×R 作为 predictive theory 的定位。

**W7. S×R 框架是标准 power analysis 的重新包装。** [R2 首发, R1 partial REBUT]
Power = Φ(S·R·√T/σ) 即 z-test power formula。R(α) 非单调性有定性机制论证（relaxation time matching），但 R(α) 无独立于 PermG 检测率的可操作化定义，非第一性原理推导。建议定位为 "interpretive decomposition" 而非 "theory/framework"。

**W8. PermG formal power analysis 缺失。** [R1 首发, R2 AGREE with nuance]
T=11 差分后 10 点、lag-1 仅 ~9 有效观测。5,000 permutation 验证采样稳定性而非检验功效。Empirical null-control 校准提供部分辩护，但不等于 formal power analysis across α spectrum。

**W9. Token entropy → distinct-n 机械耦合 confound 未讨论。** [R1 首发, R2 partial AGREE]
Entropy 下降→生成分布集中→n-gram 多样性机械降低。R2 辩护：纯机械耦合是同步的，不应产生 one-generation lag（Figure 1），且 first-differencing 存活提供部分排除。但论文应显式讨论此 confound。

**W10. 与 Gu et al. (2024, 2025) 关系分析不充分。** [R2 首发, R1 AGREE]
CMR scaling law 的 critical ratio 和 data mixing phase transitions 与本文 α_c≈0.50 可能描述同一现象——仅有 "invites connection" 一句 forward-looking 声明，无定量对比。

**W11. Introduction "four deficiencies" 存在 straw-man 倾向。** [R2 首发, R1 partial REBUT]
对描述性 collapse 研究不公平，但对做了 temporal precedence claims 的先行工作（Du 2025/2026, Gambetta 2024）合理。建议收窄适用范围。

**W12. Intervention 实验薄弱。** [R1+R2 共识]
15% entropy threshold 无理论依据、无 sensitivity analysis。仅 2 模型（410M, 1.4B）。Bootstrap CI [29%, 64%] 极宽。未测试 partial contamination (α<1.0)。

### Minor

**W13.** "Causal detection" 措辞残留，与 Granger ≠ causation 声明不一致
**W14.** 87% headline 掩盖两类不同性质的架构依赖失败
**W15.** α_c CI [0.43, 0.56] 跨越 blind/onset regime 边界
**W16.** 非均匀 seed 覆盖 + α=0.45 seed 数量不一致（Section 4.1 vs Appendix）
**W17.** Abstract ≥20 个数值，信息密度过高
**W18.** 22 个 orphan bib entries (44% orphan ratio)

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全一致：

1. **格式必须修复**，否则面临 desk rejection（W4）
2. **α=0.60 内部矛盾**必须澄清——dual-seed 还是 single-seed？（W1）
3. **所有 promised appendix content 必须补齐**——specification curve、Shapley、MMCT algorithm、dose-response profiles（W2, W3）
4. **T=20 需要数据或降级声明**（W6）
5. **方法敏感性暴露是论文的核心价值**，独立于 phase transition framing（S1）
6. **Intervention 实验需要加强或降低 claim 强度**（W12）
7. **机械耦合 confound 必须在 Discussion 中讨论**，即使 one-generation lag 部分排除纯机械解释（W9）
8. **Overall 3.0 (Findings)**——当前状态适合 Findings，修复后有 3.5–4.0 潜力

---

## Reviewer Divergence [REBUT]

**1. Excitement (R1: 3.5 vs R2: 2.5)**
- R1 认为：在 model collapse 领域实证量化检测阈值（sigmoid k≥200）和方法敏感性（κ=0.185）有独立贡献价值，类比 Boettiger & Hastings (2012) 在生态学中的角色
- R2 认为：核心发现是教科书级 power analysis 的直接推论，MMCT 非新方法，S×R 非新理论，新颖性有限
- **Director 判定**：3.0。R1 的辩护有道理——实证发现在特定领域的首次系统量化有价值——但 R2 正确指出 framing 的 oversell 降低了 excitement。真正新颖的部分（非单调 dose-response、method sensitivity 暴露）未被充分突出

**2. Reproducibility (R1: 2.5 vs R2: 3.0, revised from 4.0)**
- R1 强调 MMCT 方法框架的可复现性（核心方法无完整定义）
- R2 强调实验 setup 的可复现性（超参数完整）
- **Director 判定**：2.5。方法定义的完整性比超参报告更根本——MMCT 是论文的 Contribution 3，但读者无法从论文中重建它

---

## Questions（需作者回答）

1. Section 4.3 声称 α=0.60 "dual-seed confirmed"。请澄清两个 seed 的精度和来源，或更正为 single-seed。
2. Specification curve analysis (1,160 specifications) 的完整结果在哪里？
3. Shapley value analysis、MMCT algorithm pseudocode、per-method dose-response profiles 为什么没有出现在声称的附录中？
4. 是否考虑过 token entropy 和 distinct-n 之间的机械耦合（entropy 降低→分布集中→diversity 机械下降）作为 24/24 完美保留的替代解释？
5. 15% entropy threshold 如何选定？是否有 sensitivity analysis？
6. α=0.45 实际有几个 seed？Section 4.1 说 single-seed probing point，Appendix 报告了 2 seeds。
7. α_c=0.476 与 Gu et al. (2024) CMR scaling law 预测的 critical ratio 的定量关系是什么？
8. α=0.00 下 distinct-1 已降 14.1%（纯 fine-tuning drift）。contamination 到底添加了什么额外信号使得 Granger precedence 出现？
9. C4 domain α=0.50 s42 PermG reverse 7/8——这对 directionality claim 意味着什么？
10. 为什么选择 replace-only 而非 accumulate protocol？

---

## Missing References

1. **arXiv:2502.15654** (2025) — Detection-based mitigation for model collapse，直接相关
2. **Schaeffer et al. (2025)** "Position: Model Collapse Does Not Mean What You Think" — 8 种 collapse 定义应在 Related Work 中与本文 claim scoping 对接（当前仅在 Limitations 简单引用）
3. **Dakos et al. (2012)** "Methods for Detecting Early Warnings" — bib 中有但未 cite，与本文 multi-method 比较高度相关
4. **Schreiber (2000)** "Measuring Information Transfer" — 附录使用 Transfer Entropy 但未在正文引用
5. **Ernst (2004) / Phipson & Smyth (2010)** — Permutation testing 功效和 p-value 处理的参考文献
6. **Marcinkevics & Vogt (2022)** — Neural Granger causality，bib 中有但未 cite
7. **Kazdan et al. (2025)** "Collapse or Thrive?" — bib 中有但未 cite，与 Schaeffer (2025) 互补

---

## External Review (Stanford Agentic Reviewer)

**状态：已跳过。** 外部审稿请求已发送但被用户跳过（skipped at 2026-05-20T12:45:54）。

---

## Visual Layout Check（非评分项）

**状态：已完成。** 3 warnings, 9 info items。

关键发现：
- ⚠️ **前 4 页纯文本无 figure/table**：审稿人在前 2 分钟内只看到密集双栏文字墙。建议将核心结果图（Figure 1 的相变曲线）前移到 page 2 或 Introduction 末尾
- ⚠️ **Figure 1 使用单栏宽度**：作为论文核心可视化，建议改用 figure*（全宽）增强视觉冲击力
- ⚠️ **主文 8 页仅 4 个 display items**：作为实证论文，密度偏低（通常 5-8 个），大量表格推到 appendix
- ℹ️ Figure 1 axis labels 偏小（接近可读性下限），建议 ≥9pt
- ℹ️ Figure 2 灰度打印下蓝/绿线可能难区分，建议辅以不同 line style
- ℹ️ Table 1/2 未对关键数值加粗标注
- ℹ️ 13 个 appendix tables，部分小表可合并
- ℹ️ References 格式统一，无 [?] 未解析引用

---

## Overall Assessment

**Overall: 3.0 — Findings（可被 Findings 接收）**

| 维度 | R1 | R2 | Director |
|------|-----|-----|----------|
| Soundness | 3.0 | 3.5 | **3.0** |
| Excitement | 3.5 | 2.5 | **3.0** |
| Reproducibility | 2.5 | 3.0 | **2.5** |
| Confidence | 4/5 | 4/5 | — |

**理由：**

论文的核心价值在于方法敏感性的系统暴露（S1）和 null-control 校准设计（S4），这些对 model collapse 文献有独立贡献。检测阈值的实证发现（sigmoid k≥200, Δα≈0.02, Fisher exact p=3.45×10⁻¹¹）在该领域是新的。

但论文自身的方法论标准与实际执行之间存在显著 gap——一篇以"暴露方法论缺陷"为卖点的论文出现了：(a) 支撑核心 framing 的数据点存在内部矛盾（α=0.60 W1）；(b) 正文声称的多项分析在附录中不存在（W2, W3）；(c) 核心方法论框架（MMCT）无法从论文中完整重建。这些问题的严重性在于它们恰好出现在论文声称最 rigorous 的维度上。

格式不合规（W4）是独立的 blocking issue——当前模板无法通过 ARR desk check。

**升级路径（3.0→3.5–4.0）：**
1. ⬆️ **修复 α=0.60 矛盾** + 补 fp32 multi-seed（四 regime 是否成立的关键）
2. ⬆️ **补齐所有 promised appendix content**（specification curve, Shapley, MMCT algorithm, dose-response profiles）
3. ⬆️ **迁移 ACL 模板** + author-year citations
4. ⬆️ **完成至少一个 T=20 验证点**（t20_a075 已在运行中）
5. ↗️ 将 "phase transition" 降级为 "detection onset/threshold"
6. ↗️ Discussion 增加机械耦合 confound 讨论
7. ↗️ 与 Gu et al. CMR 做定量对比
8. ↗️ Intervention threshold sensitivity analysis

项 1-4 如全部完成，论文有 Borderline Conference (3.5) 到 Conference (4.0) 的潜力。核心 insight 足够 strong，当前的 gap 是 addressable 的。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度过高（≥20 个数值），建议精简至 3-5 个关键数字
- "causal detection" 措辞与后文 "Granger precedence ≠ causation" 不一致

### Introduction
- "Four deficiencies" 对描述性 collapse 研究不公平，建议收窄到做了 temporal precedence claims 的工作
- 贡献列表清晰，但 Contribution 2 (S×R theory) 的定位过高

### Method (Section 3)
- MMCT 权重公式有但完整流程不完整
- "appear in the Appendix" 引用的三项内容均缺失
- S×R 框架定位应从 "theory" 降为 "interpretive framework"

### Experiments (Section 4)
- 核心发现（检测阈值 0/8→6/8）统计支撑充分（Fisher exact + sigmoid fit + sub-threshold gradient）
- α=0.60 "dual-seed confirmed" 与 Section 4.1/Limitations 直接矛盾
- α=0.45 seed 数量描述不一致
- Specification curve analysis 声称但缺失
- Cross-architecture 87% headline 应区分两类失败模式
- Intervention 15% threshold 无理论依据

### Discussion
- Granger precedence ≠ causation 的声明到位
- 缺少机械耦合 confound 讨论
- 与 Gu et al. CMR 的连接仅有一句 forward-looking 声明
- α=0.00 fine-tuning drift 产生 14.1% diversity decline 但不产生 Granger precedence 的机制未解释

### Limitations
- 内容充实且诚实
- 与 Section 4.1 和 4.3 关于 α=0.60 的描述存在内部矛盾

### Format
- 未使用 ACL 官方模板（desk rejection 风险）
- Numbered citations 而非 author-year
- 自定义 margins
- Limitations 和 Ethics statement 位置和内容合规
- 匿名性合规