---
round: 9
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T11:06:00.286793+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Mapping the Detectability Landscape of Iterative Model Collapse

**Round 10 (Fresh Review) | Venue: EMNLP 2026 (ARR) | 2026-05-24**

---

## Summary

本文研究 iterative model collapse 的可检测性，使用 permutation Granger causality (PermG) 测试 token entropy 是否在时序上领先于 diversity decline。作者在 Pythia-410M 上跨 13 个 contamination level 和多种观测窗口长度 T 绘制了 "detectability landscape"，识别出四个 regime（blind zone、sharp onset、non-monotonic dip、reliable detection），并发现 5 种统计方法在相同数据上的 null-control FPR 差异巨大（3%–92%）。跨架构验证覆盖 3 个 model family（论文声称 5 个），intervention proof-of-concept 展示 64% 的 perplexity 降低。

---

## Strengths

**S1. 方法灵敏度发现（3%–92% FPR）具有实际警示价值。** 5 种统计方法在完全相同的数据上产生 3% 到 92% 的 null-control FPR（Section 4.1, Table 1）——不是细微差异，而是从 "全面检测" 到 "完全 null" 的翻转。这一发现对 model collapse 监控文献具有直接实践意义：任何不报告 method sensitivity 的 collapse 检测研究结论都是不完整的。**（R1-R2 共识）**

**S2. 系统性实验设计与高实验量。** 1415 个实验覆盖 13 个 α 水平 × 多种 T 值 × 多 seed，Phase diagram（Figure 1）提供直观可视化框架。Specification curve analysis（Appendix E，1160 个 specification）和 Shapley value 分解（Appendix P）展示了 thoroughness。**（R1-R2 共识）**

**S3. 透明报告局限。** Discussion（Section 6, p.8）明确 scope Granger "precedence" 而非 causation，承认 ">7B untested"，Limitations section 坦诚报告 GPT-2 medium 的 50% FPR。Intellectual honesty 值得肯定。**（R1-R2 共识）**

**S4. 写作清晰，格式合规。** Abstract 约 173 words（符合 200 word 限制），正文 8 页，ACL 模板，匿名格式正确，AI 披露存在。**（R1-R2 共识）**

---

## Weaknesses — Must-Fix（影响接收决定）

### MF-1. Propositions 1-2 理论贡献过度包装 [R1 PARTIAL, R2 critical → 共识]

**问题**：Proposition 1 声称 "entropy responds before diversity" under mode amplification，但这几乎是 metric 定义的必然结果：entropy 是对任意概率重分配敏感的连续指标，而 diversity metrics（distinct-n, effective support）是阈值型指标，只有当 token 概率被压低到阈值以下时才会变化。Assumption 4（mode amplification）本质上预设了结论。Proposition 2 (diversity lag ≥ 1) 同理。论文将这些作为 "formal motivation"（贡献 2）与实证发现并列呈现，给读者印象存在非平凡理论结果。

**共识**：Propositions 1-2 作为 design rationale formalization 有组织价值（使 violation conditions 可检验，如 SmolLM3-3B），不应删除，但 **framing 需从 "theoretical contribution" 降级为 "formal design rationale"**，且不应在 contribution list 中与实证发现并列为同等权重。

**跨轮次记录**：与 F5-N1、F5-W1 同源。R9 已做部分修复（"formalized observation"），但 R10 fresh review 仍认为定位不充分。

### MF-2. Proposition 3 power-law detection boundary 统计支撑不足 [R1 critical, R2 AGREE]

**问题**：5 个 T 值拟合 2 参数 (A, γ)，仅有 3 个自由度。γ CI [0.24, 0.78] 跨越 3 倍范围——boundary 可能是浅 power-law 也可能是陡 power-law，预测精度极有限。R²=0.969 在 5 个点上不具强说服力（少量点容易过拟合）。虽然论文标记为 "empirical"，但 "Proposition" 的形式化呈现仍给读者造成理论结果的印象。

**共识**：应从 "Proposition 3" 降级为 empirical observation，不使用 Proposition 编号。

**跨轮次记录**：与 F2-W4b、F2-W6 同源。R9 已降级为 "empirical scaling observation" 并诚实报告 β CI，但仍保留 Proposition 编号——修复不彻底。

### MF-3. PermG FPR = 11.1% 超出 nominal 5%，且 architecture-dependent [R1 critical, R2 AGREE]

**问题**：
- PermG FPR = 11.1%，CI 上界达 30.4%，超出 nominal 5% 水平
- GPT-2 medium 上 PermG FPR 达 50%（Discussion p.8, Appendix Z.2），说明 FPR 是 architecture-dependent 的——与 "methodology transfers" claim 直接矛盾
- BH-FDR 的 PRDS (positive regression dependency on a subset) 假设未验证。Permutation test p-values 因共享训练数据可能存在正依赖
- "Lowest among directional methods" 的表述实际价值有限——可能只是 "least bad"

**共识**：这是最核心的方法论问题。如果 FPR 是 architecture-dependent 的，论文的核心 claim 需要重新限定适用范围。

**跨轮次记录**：与 F3-J4 同源（贯穿 R3-R10 共 7 轮）。R9 解决了 CI 报告一致性，但 FPR 偏高本身和跨架构不稳定性未解决。

### MF-4. 跨架构验证不足 + 标题 overpromise [R1 critical, R2 critical → 双方共识]

**问题**：
- 完整的 (α, T) grid 仅在 Pythia-410M 上映射。跨架构验证（Table 2）仅在 α=1.0（最极端、最容易检测的 regime）进行，未验证 landscape 中最有诊断价值的 moderate contamination regime
- 4/15 条件失败（26.7%），包括 SmolLM3-3B entropy 0/4 **直接违反 Proposition 1 前提**——说明 Assumption 4 适用范围比预期更窄，质疑理论框架的 generality
- GPT-2 medium PermG FPR = 50% vs Pythia-410M 11%——methodology 并不可靠 "transfer"
- 标题 "Mapping the Detectability Landscape" 使用定冠词 "the"，暗示全面覆盖。实际交付是 "detection boundary characterization on Pythia-410M"

**共识**：标题改为 "Toward Mapping..." 或明确 scope 为 Pythia-410M；或在至少一个非 Pythia 架构上做完整 (α,T) grid。

**跨轮次记录**：与 F2-W2b、F2-W10 同源。R9 framing 已调整为 "detection boundary characterization"，但标题未改——修复不彻底。

### MF-5. "Five families (1435M–6.9B)" 数字自洽性错误 [R2 critical, R1 AGREE]

**问题**：
- Abstract 声称 "cross-architecture validation on five families (1435M–6.9B)"
- Table 2 中可辨识的独立架构 family 仅有 3 个（Pythia, GPT-2, SmolLM3）。同一架构不同 scale（如 Pythia-410M 和 Pythia-1.4B）按学术惯例属同一 family
- 参数范围 "1435M–6.9B" 中，GPT-2 medium 仅 437M、Pythia-410M 仅 410M，均显著低于声称的 1435M 下界
- 数字自洽性是 soundness 的基本要求

**共识**：明确列出 "five families" 的定义，修正参数范围以包含实际最小模型。

---

## Weaknesses — Should-Fix（影响评分但不一票否决）

### SF-1. Intervention 实验 underpowered [R1-R2 共识]

Section 5.6 仅展示 α=1.0（最极端设置）的单一 proof-of-concept，n=2 canary metrics，单次触发事件，CI 29–64%。Abstract 将 "triggered cessation reduces peak perplexity by 64%" 作为最后一个 claim，呈现方式可能误导读者以为 intervention 经过充分验证。

**建议**：在 abstract 中加 "proof-of-concept" 限定词，或从 abstract 中移除降级为 supplementary finding。

### SF-2. Data accumulation vs. replacement 未讨论 [R2 raised, R1 partial AGREE]

所有实验使用 replacement paradigm。Gerstgrasser et al. (2024) 已证明 accumulation 可缓解 collapse。真实 web-scale training pipeline 更接近 accumulation。Discussion 应至少定性讨论 accumulation 对 landscape 的预期影响（如 boundary shift、non-monotonic dip 行为）。

R1 注意：replacement 是 model collapse 文献的标准实验范式，不应因此降低评分，但 Discussion 中需增加讨论。

### SF-3. 单一解码策略需定性讨论 [R1 raised, R2 partial AGREE]

所有实验使用 temperature 1.0 / top-k=50。Limitations 仅用半句话提及。应讨论 lower temperature（entropy profile 更尖锐→可能加速 collapse→可能左移 detection boundary）和 nucleus sampling（概率质量截断→可能改变 diversity metric 阈值行为）的预期影响方向。不需要新实验，但需更充分的 qualitative discussion。

---

## Minor Issues（不影响接收）

| # | 问题 | 来源 | 建议 |
|---|------|------|------|
| m1 | bf16/fp32 精度敏感性（α=0.60 bf16 0/8 vs fp32 6/8） | R1→R2 共识降级 | Limitations 加一句 |
| m2 | MMCT 投票阈值 K≥3 缺 formal justification | R1→R2 共识降级 | Appendix 补 K sensitivity |
| m3 | 缺 Steegen et al. (2016) multiverse analysis 引用 | R2 raised, R1 AGREE | Related Work 或 Appendix E 补充 |
| m4 | Granger "causality" vs "precedence" 区分不够突出 | R2 raised, R1 PARTIAL | Section 3/4 开头增 1-2 句 |
| m5 | "1435M" 精度与 "410M/1.4B" 风格不一致 | R2 | 统一为 "1.4B" |
| m6 | Abstract "confirms" 过强（73% 成功率） | R2 | 改 "partially supports" |
| m7 | Figure 1 缺 colorblind-friendly 方案 | R2 | 增加纹理/图案辅助区分 |
| m8 | Figure 3 legend/tick label 字号偏小（约正文 60-65%） | R2 + visual check | 检查是否 ≥8pt |
| m9 | 缺 Hataya et al. (2023) ICCV 引用 | R2 | 补充 image generation 视角 |

---

## Questions for Authors

1. **"Five families" 明细**：请明确列出 5 个 family 及其对应的模型名称和参数量。Table 2 中可辨识的独立架构族仅有 3 个（Pythia, GPT-2, SmolLM3）。
2. **GPT-2 medium FPR**：GPT-2 medium 的 PermG FPR 高达 50%（vs. Pythia-410M 的 11%），这是否意味着 FPR 是 architecture-dependent 的？如果是，这对 "methodology transfers" 的 claim 有何影响？
3. **Accumulation paradigm**：在 data accumulation 设定下，你们预期 landscape 的哪些结构特征会保留、哪些会改变？是否有初步实验？
4. **Non-monotonic dip mechanism**：α=0.60 处的 non-monotonic dip（"syn-dip mechanism at α=0.60 remains open"，Limitations p.8）是否有后续分析或假说？

---

## Missing References

1. **Steegen, S., Tuerlinckx, F., Gelman, A., & Vanpaemel, W. (2016).** Increasing transparency through a multiverse analysis. *Perspectives on Psychological Science, 11*(5), 702-712. — multiverse analysis 方法论奠基论文，与 Appendix E specification curve 直接相关。
2. **Hataya, R., Bao, H., & Arai, H. (2023).** Will large-scale generative models corrupt future datasets? *ICCV 2023.* — 早期 model collapse 研究，补充 image generation 领域视角。

---

## External Review

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 12 info）。

**Warnings:**
- 前 2 页为纯文本（Abstract + Introduction + Related Work），无任何 display item（figure/table/display equation）。Figure 1 直到 page 3 才出现，第一印象锚定较晚。建议考虑在 Introduction 中提前引用或内嵌示意图。
- 最后一页（p.28）仅使用约 1/5 页面（AI Assistants 短段落），约 4/5 为空白。

**Info highlights:**
- Figure 2 和 Figure 3 堆叠在 page 7，Figure 3 三个 subplot 在单栏宽度内排列，axis label 和 legend 字号偏小（约正文 60-65%），接近可读性下限。
- Page 8 非常密集（Table 2 + Figure 4 + Discussion + Limitations），Figure 4 与上方文字间距略紧。
- 其余排版（Table 1/2 booktabs、Algorithm 1、参考文献格式、匿名格式）均规范。

---

## Overall Assessment

| 维度 | Reviewer 1 | Reviewer 2 | 共识 |
|------|-----------|-----------|------|
| **Overall** | **3.5** (Borderline Conference) | **3.0** (Findings) | **3.0** (Findings) |
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3.5/5 | 2.5/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |

### 推荐处置：3.0 (Findings)

5 个 Must-Fix 中：
- **MF-1**（理论定位）和 **MF-5**（数字自洽性）可通过 framing/文字调整解决
- **MF-2**（Prop3 统计支撑）可通过降级为 empirical observation 解决
- **MF-4**（跨架构/标题）需要 scope 缩窄或补充实验
- **MF-3**（FPR architecture-dependence）是最核心的方法论问题——如果 PermG 的 FPR 是 architecture-dependent 的，论文的核心 claim 需要重新限定适用范围

### 评分分歧说明

R1（3.5）和 R2（3.0）的分歧主要在 Excitement 维度：R1 认为 detectability landscape 框架本身是对领域的原创组织贡献（framework paper 视角），R2 认为核心方法论无创新、是标准计量经济学工具的领域搬运（novel technique 视角）。这反映了对 "framework/characterization paper" vs "novel technique paper" 的评审标准差异。

取共识 **3.0 (Findings)**，理由：5 个 Must-Fix 数量偏多，且 MF-3（FPR architecture-dependence）和 MF-4（landscape generalizability）共同削弱了论文最核心的 contribution——如果 landscape 是 architecture-dependent 且方法 FPR 不可控，框架本身的价值也会打折。

### 评分上调路径

如果作者充分解决以下问题，评分可上调至 **3.5–4.0**：
1. MF-1: 将 Propositions 1-2 重新定位为 design rationale（文字调整）
2. MF-2: 将 Proposition 3 降级为 empirical observation，去掉 Proposition 编号（文字调整）
3. MF-3: 扩大 null-control 样本 + 讨论 architecture-dependent FPR 的 implications（可能需要少量补充实验）
4. MF-4: 缩窄标题 scope 或在至少一个非 Pythia 架构上做完整 (α,T) grid（需要补充实验或标题调整）
5. MF-5: 修正 "five families" 定义和参数范围（文字调整）

---

## Detailed Comments

### Reviewer 1 最终立场（Overall 3.5）

**Must-Fix (3)**:
1. Proposition 3 power-law: 5T 拟合 2 参数，γ CI [0.24, 0.78] 极宽，统计支撑不足
2. PermG FPR = 11.1% (CI→30.4%)，超出 nominal 5%，PRDS 假设未验证
3. 跨架构 26.7% 失败率，SmolLM3-3B 0/4 entropy 违反 Proposition 1

**Should-Fix (2, 经交叉调整)**:
1. Intervention underpowered（与 R2 共识）
2. 单一解码策略需 qualitative discussion（与 R2 共识保留）

**Minor (2, 经交叉降级)**:
- bf16/fp32 precision → Limitations 提及
- MMCT K threshold → Appendix sensitivity

**撤回**: TY 膨胀 FPR 叙事（接受 R2 rebut）

### Reviewer 2 最终立场（Overall 3.0）

**Must-Fix (3)**:
1. Propositions 1-2 近乎同义反复，需降级为 design rationale formalization
2. Landscape 主体基于单一架构，标题 overpromise
3. "Five families (1435M–6.9B)" 数字自洽性错误

**Should-Fix (2, 经交叉调整)**:
1. Intervention abstract framing 过于单薄
2. Accumulation vs replacement 需 Discussion 讨论

**Minor (4)**:
- Granger terminology 区分不够突出
- "1435M" 表述风格不一致
- "confirms" 用词过强
- 缺 Steegen et al. (2016) 和 Hataya et al. (2023) 引用

---

## 格式合规检查

| 检查项 | 结果 |
|--------|------|
| 正文 ≤ 8 页 | ✓ (正文到 p.8，References 从 p.9) |
| Abstract ≤ 200 words | ✓ (约 173 words) |
| Limitations section 在正文内 | ✓ (p.8, References 之前) |
| Limitations 仅一个 | ✓ |
| Double-blind 匿名 | ✓ ("Anonymous ACL submission") |
| ACL 模板 | ✓ |
| 引用格式 (natbib) | ✓ |
| AI Assistant 披露 | ✓ (p.28) |

---

*报告由 Review Director 基于 Reviewer 1 和 Reviewer 2 的独立审稿及交叉回应合成。*