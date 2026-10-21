---
round: 14
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-24T23:15:20.225317+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 14 审稿报告

**Venue**: EMNLP 2026 (via ARR)
**论文**: Characterizing the Detectability Landscape of LLM-Generated Text in Iterative Training
**Reviewers**: R1（方法严谨性 + 统计基础）, R2（新颖性 + 完整性 + scope 校准）
**轮次**: Round 14（fresh review，无上轮记忆）
**交叉回应**: 双向完成。R1 对 R2 共 7 项回应（5 AGREE, 2 REBUT）；R2 对 R1 共 12 项回应（7 AGREE, 3 PARTIALLY AGREE, 2 REBUT）。

---

## Summary

本文提出基于 canary metrics（token entropy, distinct-n）的统计检测框架，用于在迭代训练中检测 LLM 输出分布退化（model collapse）。核心贡献包括：(1) 方法敏感性比较（五种检测方法的 FPR 从 3% 到 92%）；(2) 基于 Pythia-410M + WikiText-103 的 detection phase diagram；(3) Design Principles（entropy 先于 diversity 响应）的形式化推导；(4) Granger precedence 分析；(5) 概念验证级 intervention 实验。

论文在方法敏感性发现和 phase diagram 概念上有价值，但 **定量声明系统性地超出证据支撑范围**：phase diagram 仅基于单一架构/数据集，跨架构验证仅在最极端条件（α=1.0）进行且仍有 27% 失败率，统计功效不足（3 seeds/condition），intervention 实验仅为 N=2 的概念验证。

---

## Strengths

**S1: 方法敏感性发现（最强贡献）**
五种检测方法的 FPR 从 3% 到 92% 的发现——展示了统计方法选择对 model collapse 检测结论的决定性影响——是论文最有价值的贡献。这一发现具有直接的实践指导意义，且在 specification curve analysis（1,160 configurations, Figure 6）中得到了系统验证。两位 Reviewer 一致认可。

**S2: 问题定位准确**
将 model collapse 检测框架化为统计检测问题（需要控制 FPR 的假设检验），而非简单的指标监控，是合理且有价值的学术贡献。

**S3: 附录广度**
24 个 appendix sections 提供了广泛的 robustness checks（不同 lag orders, FDR 方法, 权重方案, null-control 验证等），为有疑问的审稿人提供了充分的验证渠道。

**S4: 透明报告**
论文在 §4.5 failure mode taxonomy 中报告了失败条件，在 §5 讨论了 Granger causality 的局限性。这种透明性值得肯定。

**S5: Dose-response 分析**
§4.3 的 dose-response 分析清楚展示了检测能力随 α 和 T 的变化，sigmoid 拟合（k=15.7, R²=0.969）为 sharp onset 提供了定量支撑。

---

## Weaknesses

### Must-Fix（两位 Reviewer 共识）

**MF-1: 跨架构验证仅在 α=1.0，scope overclaim 严重** [F2-W2b, R13-W3, R10-MF5]
*（Round 2 首次提出，连续 13 轮未解决）*

这是论文最严重的问题。Phase diagram（Figure 1）——论文的核心定量贡献——仅基于 Pythia-410M + WikiText-103 单一配置。跨架构验证（five families, 345M-6.9B）仅在 α=1.0（100% 合成数据替换）进行。

**α=1.0 是最极端、最容易检测的条件。** 它对 phase diagram 核心过渡区域（α∈[0.45, 0.75]）的泛化性提供零证据。即使在此最有利条件下，4/15 = 27% 的 model-seed 组合检测失败。其中 GPT-2 medium 的 null FPR 高达 50%（Appendix Z.2），意味着该架构上的检测结果不具统计意义。

Abstract 中 "Cross-architecture evaluation across five model families (345M–6.9B) supports forward detection in the majority of conditions" 是 technically correct 但 misleading。一个不熟悉细节的读者（包括 AC）会自然理解为多 α 值、多架构的系统验证。"majority of conditions" 掩盖了近三分之一的失败率。

**要求**：(1) Abstract 明确标注 "at α=1.0 (full replacement)"；(2) 标题考虑加限定语或缩窄 scope；(3) 正文注明核心定量结果（phase diagram, detection boundary）仅基于 Pythia-410M。

---

### Should-Fix

**SF-1: 统计功效不足（3 seeds/condition）** [R11-N1, R11-W2, R10-SF7]
*（R1 列为 Must-Fix，R2 降级为 Should-Fix——交叉后分歧保留）*

每个 (α, T) condition 仅 3 seeds（8 pairs）。6/8 的 binomial CI 为 [0.25, 0.92]，跨越了从"偶然"到"几乎确定"的全范围。Phase diagram 每个网格点的定量可信度很低。

R2 指出的缓解因素值得注意：sigmoid regression（k=15.7, R²=0.969）和 specification curve（1,160 configurations）提供了超越 raw binomial 的统计支撑。因此定性结论（存在 sharp onset）有一定基础，但定量边界位置不可靠。

**要求**：在主文中报告每格 CI 宽度，并讨论其对 boundary 精度的影响。理想情况下增加边界区域 seeds 至 ≥5。

**SF-2: FPR 标定偏高且 CI 极宽** [F3-J4]
*（Round 3 首次提出，连续 12 轮未解决。R1 列为 Must-Fix，R2 降级为 Should-Fix）*

PermG FPR = 7.4%（4/54），CI [2.1%, 17.9%]。MMCT K≥3 的 FPR = 11.1%（6/54）。两者均超出 nominal 5%。GPT-2 null FPR 50% 是架构级失效。

R2 指出的缓解因素：论文的贡献不是声称 PermG 控制在 5%，而是展示它是五种方法中 FPR 最低的（7.4% vs NaiveXCorr 94.4%）。Limitations §2 已明确承认此问题。但 null-control 仅 54 pairs 使得 FPR 估计本质上不精确。

**要求**：增加 null-control seeds 收窄 CI，或在正文中更突出报告 CI 宽度。

**SF-3: 幂律边界拟合数据点不足** [F2-W4b, R13-W2]
*（Round 2 首次提出，连续 13 轮未解决）*

排除 α=0.60 异常后，幂律边界 α_c(T) = c·T^(-γ) 的拟合仅基于 3-4 个 α 值。γ 的 CI [0.64, 2.08] 跨越了亚线性到超线性的定性分界，不具参数辨识力。论文自己承认 "the qualitative conclusion is robust to the specific γ value"，等于默认 γ 的精确值无法确定。

R2 建议将 Eq.(2) 降级为 "empirical scaling hypothesis" 而非给出一个看起来精确的公式。Figure 1 中的虚线边界应标注为"粗略经验趋势"。

此外，α=0.60 的排除缺乏独立验证。"Temporal lag compression" 解释是 post-hoc 的。论文需：(1) 报告该异常在不同 seeds 间的一致性；(2) 展示保留该点后拟合结果的变化。

**要求**：Eq.(2) 降级为 empirical scaling hypothesis；报告 α=0.60 cross-seed 一致性和含/排该点的拟合对比。

**SF-4: Intervention 实验过弱** [F2-W7, R13-W4]
*（Round 2 首次提出，连续 13 轮未解决）*

N=2 seeds, α=1.0 only, post-hoc 15% threshold（从同一数据确定）。即使作为 Proof of Concept 也太薄弱。两位 Reviewer 完全一致。

R2 补充了一个重要批评：未与更简单替代方案（如 perplexity threshold 或 CUSUM）比较。如果 naive baseline 就能达到类似效果，canary-based approach 的增量价值不明确。

Conclusion 中 "substantially reduces peak perplexity" 未保留 PoC 限定语。

**要求**：Abstract/Conclusion 将 "substantially" 降级为 "preliminary proof-of-concept"；考虑添加 naive baseline 比较。

**SF-5: Granger causality 局限讨论不充分** [R10-SF5, R13-W5, R13-REF3]

两位 Reviewer 从不同角度指出同一问题：

(a) **Transfer entropy 0/192 significant pairs**（Appendix F）：如果 canary 真的 "precedes" downstream metrics，非线性因果检验应能捕捉到某些信号。论文在 §5 承认无法区分是 nonlinear structure 缺失还是短序列 power 不足，但讨论过于简短。

(b) **T=10 仅为推荐长度 10%**：Granger 检验在短序列上 power 极低。Appendix N 显示 T=10 时 FPR under FDR correction 已 inflated。

(c) **Observational equivalence**：Granger precedence ≠ causation，但 §5 "Granger-precedence claim" 等措辞给读者因果性印象。

(d) **Bivariate confounders**：训练动态作为共同驱动因素未排除。偏相关分析（控制 generation number）缺失。

R2 对 R1 关于 "partial correlation 方向矛盾" 的纠正是准确的：§5 的 partial correlation 结果（同期减弱、滞后增强）实际上支持论文的 Granger precedence claim。但其他三个维度的局限仍需更充分讨论。

**要求**：Discussion 扩展 Granger 局限讨论；补充 partial correlation（控制 generation number）分析到附录。

**SF-6: Blind zone 限制框架实际适用性** [R14-N1, 新发现]

R2 独有发现，R1 交叉后完全同意。α=0.25 时 distinct-1 已下降约 40%（-58.3±10.9%），但所有五种检测方法均无信号。这意味着：**在框架能检测到 collapse 时（α≈0.50+），下游质量已经严重退化。** 框架更像 confirmation tool（确认已发生的退化）而非 prevention tool（在退化变严重前发出警告）。

Discussion/Limitations 未充分讨论这一根本限制。

**要求**：Limitations 增加对 blind zone 实际影响的 honest assessment。

**SF-7: Design Principles 形式化呈现与已知反例的讨论缺失** [R12-N1, F5-W1]

Design Principle 1（entropy 先于 diversity 响应）和 Design Principle 2（diversity 是阈值指示器）在 mode amplification 假设下的推导逻辑自洽。但存在已知反例：transfer entropy 0/192 significant pairs 和 first-differencing 消除 canary→perplexity 关联（F=0, p≈0.99）。

R1 认为 "Design Principles" 而非 "Theorems" 已是较谦逊表述；R2 认为 formal 呈现仍暗示过高可靠性。交叉后共识：内容非 trivial 但正文应更明确讨论已知反例和局限性。

**要求**：正文增加 Design Principles 已知反例和局限性讨论。

**SF-8: MMCT K 阈值极度敏感** [R13-W1]

Table 2 数据：K≥2 FPR 38.9%（不可接受）；K≥3 FPR 11.1%, TPR 75%（勉强可用）；K≥4 FPR 0%, TPR 25%（power 不足）；K=5 FPR 0%, TPR 0%（完全无用）。MMCT 实际工作点仅一个。使用者需先在 null-control 数据上校准 K，限制即用性。

**要求**：Discussion 讨论 K 校准对实际部署的影响。

---

### Minor Issues

- **M1**: Figure 2 y 轴标签偏小，Figures 4/6 axis/legend 文字 <7pt（视觉审查 + R1 确认）
- **M2**: bib 格式不一致（R2）
- **M3**: Abstract "Granger-precedes" 对非专业读者可能困惑，建议改为更直白表述
- **M4**: Granger "precedence" vs "causality" 术语在全文中仍有不一致
- **M5**: β 符号重用（统计功率 vs 幂律指数），增加阅读混淆
- **M6**: bib 中存在但正文未引用的条目（Dakos et al. 2012, Bell et al. 2022, Gu et al. 2026, Dakos et al. 2008），应引用或移除
- **M7**: >7B 模型局限在 Limitations 中提及过于简短
- **M8**: 单一解码策略（temp=1.0, top-k=50）限制外部效度，Discussion 未充分展开

---

## Questions

1. α=0.60 non-monotonic dip 在 3 个 seeds 之间是否一致出现？如果仅出现在部分 seeds，排除它的理由更充分；如果一致出现，它可能反映真实的非单调物理过程。
2. 保留 α=0.60 数据点后幂律拟合的 γ 和 R² 变化多大？
3. 简单的 perplexity threshold（不依赖 canary metrics）是否也能达到与 intervention 实验类似的效果？
4. 如果在 α=0.50（而非 1.0）上进行跨架构验证，预期有多少 model families 能通过？
5. PRDS 假设在该数据上是否经验验证过？

---

## Missing References

以下引用在两位 Reviewer 的交叉回应中被提及：
- Dakos et al. (2008, 2012) — 早期预警信号核心实证方法论（bib 中存在但正文未引用）
- Runge et al. (2019) PCMCI — 多变量因果推断
- Adams & MacKay (2007) — Bayesian online changepoint detection
- Papana et al. (2013) / Siggiridou & Kugiumtzis (2016) — permutation Granger validation
- Gerstgrasser et al. (2024) — data accumulation paradigm
- Lenton et al. (2008) — tipping elements（论文使用 tipping point 类比但未引此奠基工作）

---

## External Review

未请求。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（2026-05-24T22:50:38 → 22:53:48）

### Warnings (4)
1. **Page 3** — Figure 2 legend 文字约 6pt，150dpi 下接近可读性边界
2. **Page 5** — Figure 4 四个子图 axis/tick labels 非常小（<7pt）
3. **Page 5** — 3 个 display items（Fig 4 + Fig 5 + Table 1）视觉密度高，与 page 2 纯文本反差大
4. **Page 6** — Figure 6 下半部分 specification indicator panel 标签极小且密集

### Info (7)
- Page 2 整页纯文本无 display item
- Figure 5 小尺寸下 dashed/solid curve 区分度有限
- Figure 8 faded bars 灰度打印时对比度低
- Figure 9 y 轴标签字号偏小
- Table 2 最优值未加粗标注
- Appendix Figure 10 色阶与 Figure 1 一致（正面）
- Appendix 表格格式统一（正面）

---

## Overall Assessment

**评分: 3.0 — Findings**

两位 Reviewer 独立给出相同评分，交叉回应后维持不变。

**评分理由**：

论文提出了有价值的框架——将 model collapse 检测框架化为需要控制 FPR 的统计检测问题，方法敏感性发现（FPR 3%→92%）具有实践指导意义，phase diagram 概念为该领域提供了有用的组织框架。

但定量声明系统性超出证据支撑：
- Phase diagram 仅基于 Pythia-410M + WikiText-103，跨架构验证仅在最极端条件 α=1.0 进行
- Abstract/标题暗示的广度与实际证据严重不匹配
- 统计功效不足（3 seeds, 8 pairs/cell）使 boundary 精度不可靠
- Intervention 仅为 N=2 概念验证却使用 "substantially" 等强修饰语
- Blind zone（α<0.50 已退化但无检测信号）限制框架的 early warning 价值

**不可改变的天花板**：核心方法为计量经济学标准技术的移植（Granger, permutation test, BH-FDR），技术新颖性有限。两位 Reviewer 一致认为 novelty 来自 method-sensitivity finding 和 phase-diagram framing，而非方法本身。这是结构性限制。

**Findings 而非 Conference 的关键差距**：如果跨架构验证扩展到 α∈[0.50, 0.75] 的过渡区域，且 intervention 有更充分的比较实验，评分可升至 3.5。当前版本的 scope claim 与证据之间的 gap 是阻止 Conference 接收的主要障碍。

**与前轮比较（基于 issue tracker）**：MF-1（scope overclaim）、SF-2（FPR 标定）、SF-3（幂律拟合）、SF-4（intervention）均从 Round 2-3 首次提出，历经 12-13 轮仍未根本解决。论文在每轮进行了措辞调整（hedging），但核心实验规模未变。这些不是 writing 问题，而是 evidence 问题——无法仅通过文字修改解决。

---

## Detailed Comments

### 两位 Reviewer 的分歧与裁定

| 问题 | R1 判定 | R2 判定 | Director 裁定 |
|------|---------|---------|---------------|
| 统计功效 (N1) | Must-Fix | Should-Fix（sigmoid+spec curve 缓解） | Should-Fix — R2 的缓解证据有效 |
| FPR 标定 (N3) | Must-Fix | Should-Fix（comparative 而非 absolute claim） | Should-Fix — 论文定位合理 |
| 幂律拟合 (N4) | Must-Fix | Should-Fix（定性结论稳健） | Should-Fix — 但 Eq.(2) 需降级 |
| Partial correlation | 方向矛盾 | 支持 Granger claim | R2 正确 — 同期减弱+滞后增强是 genuine temporal precedence 的标志 |
| Design Principles | 形式化合理 | 过度 formal | 中间立场 — 需讨论反例 |
| Appendix 规模 | 优势 | 应在主文摘要 | R1 正确 — 附录广度是优势，但关键结果需在主文充分摘要 |

### 优先修改建议（按影响力排序）

1. **Abstract/标题 scope 校准** — 最高优先级。明确核心结果基于 Pythia-410M，跨架构验证限于 α=1.0。
2. **Intervention 降级** — 删除 "substantially"，明确 preliminary PoC 定位。
3. **Blind zone 讨论** — Limitations 增加 α<0.50 检测盲区的 honest assessment。
4. **Eq.(2) 降级** — 改为 empirical scaling hypothesis。
5. **Granger 局限扩展** — 补充 partial correlation（控制 generation）、讨论 T=10 power 限制。
6. **Design Principles 反例** — 正文讨论 transfer entropy null 和 first-differencing null。
7. **Figure 字号** — Figures 2/4/6 axis labels 增大至 ≥8pt。
8. **bib 清理** — 未引用条目处理，格式统一。