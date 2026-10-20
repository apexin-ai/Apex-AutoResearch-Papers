---
round: 13
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T15:19:31.414910+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 13 审稿报告

**论文**: Characterizing the Detectability Landscape of Iterative Model Collapse
**Venue**: EMNLP 2026 (via ARR)
**审稿模式**: Fresh（重新审稿）
**Reviewer 配置**: 2 人（R1: 方法严谨性 + 统计可靠性；R2: 新颖性 + 完整性 + 参考文献）
**交叉回应**: R1→R2: 8 AGREE / 4 REBUT；R2→R1: 14 AGREE / 3 REBUT
**收敛状态**: 1 轮收敛，核心关切高度重叠

---

## Summary

本文研究迭代模型坍缩（iterative model collapse）的可检测性问题，在 Pythia-410M + WikiText-103 上对 13 个污染比例进行全网格实验，使用 permutation Granger causality（PermG）等 5 种统计方法构建检测景观（phase diagram）。主要发现包括：(1) 方法选择极大影响结论——5 种方法在相同数据上产生 3%–92% 的 null-control FPR；(2) 检测边界呈现 blind/onset/detection 三个 regime 加一个未解释异常；(3) entropy Granger-precedes diversity collapse ≥1 generation（14/15 实验）；(4) 跨架构评估（仅 α=1.0）在 5 个模型族 11/15 条件下支持前向检测。论文附录极为详尽，包含 specification curve、Shapley 分解、非平稳性鲁棒性等分析。

---

## Strengths

**S1 [共识]. 方法敏感性发现具有社区警示价值。** 5 种方法在相同数据上产生 3%→92% 的 FPR 跨度（§3.3, Table 1），这一发现对 model collapse 检测研究具有直接实用意义，提醒研究者方法选择是影响结论的首要因素。两位 Reviewer 独立将其列为首要优点。

**S2 [共识]. 问题定义有价值。** "何时可检测到"比"是否发生"更有实用意义，将检测问题转化为关于检测功效（statistical power）随参数变化的系统性研究。R2 补充：本质上是统计检验功效分析在新领域的应用，概念新颖性不应高估。

**S3 [共识]. Cascade ordering 一致性稳健。** 14/15 实验中 entropy Granger-precedes diversity collapse 的级联序一致性（§4.3, Appendix W），为 canary 概念提供了实证基础。R2 保留意见：连续统计量先于离散统计量响应在信息论层面可能较直观。

**S4 [共识]. Propositions 4-5 增加形式严谨性。** Appendix X 的形式化推导为 cascade ordering 提供了理论支撑。R1 认为非 trivial（mode amplification 下的特定机制），R2 认为核心假设（Assumption 3）较强。

**S5 [共识]. 附录详尽程度罕见。** Specification curve（Appendix E）、Shapley 分解（Appendix P）、非平稳性鲁棒性（Appendix O）等分析展现了超出一般投稿水平的实证严谨性。

**S6 [共识]. 诚实披露局限。** PermG FPR 膨胀、α=0.60 异常、GPT-2 失败等均在正文明确提及。

---

## Weaknesses

### Critical

**W1 [共识, 复发 R3-R13]. PermG FPR 膨胀——null-control 样本量根本不足。**
PermG 的 null-control FPR CI 为 [1.2%, 30.4%]，跨越两个数量级——FPR 可能是 1%（可接受）或 30%（完全不可用）。根源是 null-control 仅 36 pairs（6 seeds × 6-pair basis）。该问题从 Round 3 至今跨越 10 轮审稿未能根本解决。R2 进一步指出：替代方案 DiffXCorr 是 bidirectional 的，无法替代 PermG 在 phase diagram 中的方向性角色；正确替代应保持方向性约束下改进置换分布估计（增大置换次数至 50000 或 bootstrap）。**需要更多 null-control 实验，统计方法无法弥补样本量不足。**
[跟踪: F3-J4]

**W2 [共识, 复发 R2-R13]. 实验范围与 framing 严重不匹配。**
"Detectability Landscape" 标题暗示广泛覆盖，实际 landscape 仅在 Pythia-410M + WikiText-103 上绘制。跨架构验证仅在 α=1.0——最极端（最容易检测）条件——下进行，且 4/15 条件失败。Phase diagram 核心贡献区 α∈[0.45, 0.75] 完全没有跨架构数据。"Five families (345M–6.9B)" 给读者广泛可推广印象，但实际深度实验局限于单一架构。两位 Reviewer 独立得出相同质疑（R1-W2/W6, R2-W3/Q1），R2 建议标题修改为含 "on Pythia-410M"。
[跟踪: F2-W2b, F2-W10, R10-MF5]

**W3 [共识, 复发 R2-R13]. 幂律拟合无信息量。**
γ 的 95% CI [0.64, 2.08] 跨越定性不同的缩放行为（亚线性 vs. 超线性），使幂律模型无法提供有区分度的预测。β 参数 MLE=0.66 vs CV=0.24（CI [0.24, 0.78]）进一步证实拟合不稳定。R13 论文修改（Abstract 删除 MAE=0.037，改为 "consistent with power-law scaling"）方向正确，但 Figure 1 虚线边界仍可能被读者解读为定量预测模型。
[跟踪: F2-W4b, R11-N1]

### Major

**W4 [共识]. α=0.60 异常排除对拟合结果影响根本性。**
仅 4 个边界 α 值中排除 1 个（α=0.60），对幂律拟合结果可能是决定性的。3 seeds 中 1 个异常即可产生非单调表象。R1 建议增加 α=0.55/0.65 实验——直接可行且必要。R2 进一步指出 α=0.60 异常可能与 SmolLM1.3B 跨架构非单调行为有关联。
[跟踪: F2-W1, R13-W2]

**W5 [共识, 复发 R2-R13]. Intervention 证据薄弱。**
Abstract "substantially reduces peak perplexity" 基于 N=2 seeds、α=1.0 单一条件、post-hoc 选择的 15% 阈值。两位 Reviewer 共识应降级为 "preliminary proof-of-concept"。R2 补充 Appendix H CUSUM comparison 显示 simple threshold 同效，削弱了 Granger 框架的实用优势。建议从主要贡献剥离。
[跟踪: F2-W7]

**W6 [共识, 复发 R5-R13]. 方法论新颖性有限。**
核心方法（permutation Granger causality、BH-FDR 校正、specification curve）均为计量经济学/统计学已有技术的直接迁移。R1 rebut：本文定位是 empirical systems paper 非方法论创新。R2 同意但指出本质是统计检验功效分析（power analysis）在新领域的应用。交叉后共识：novelty 来自 method-sensitivity finding 和 phase-diagram framing，非技术方法本身。**这是不可改变的天花板**——不影响 Findings 接收但排除 Main Conference 考虑。
[跟踪: F5-N1]

**W7 [R1 主张, R2 部分同意]. MMCT K≥3 共识 K 值缺乏理论依据。**
κ=0.185 表明方法间几乎无 agreement。MMCT FPR (16.7%) > PermG standalone (11.1%)。R2 部分 rebut：论文使用 FPR-inverse weighting 非简单投票，MMCT 仅作鲁棒性检查。但 R2 同意 K 选择缺乏理论最优性证明。共识：应提供不同 K 值下 MMCT FPR/TPR 曲线。
[跟踪: R13-W1]

**W8 [共识]. 检测边界区 seed 数量不足。**
α≈0.45–0.60 是论文最重要的贡献区域，但每个 α 值仅 3 seeds。α=0.10 仅单 seed。边界区应增加至 ≥5 seeds。每 cell 仅 8 pairs 的 binomial CI [0.25, 0.92] 极宽。
[跟踪: R11-W2, R10-SF7]

**W9 [共识]. Design Principles 作为独立贡献 oversells。**
Propositions 4-5 的核心假设（Assumption 3: mode amplification）较强，结论接近"连续指标比离散指标对微小偏移更敏感"。R1 rebut：specific ordering derivation 非 trivial。交叉后共识：内容非 trivial 但 "formal design rationale" 作为 Contribution 2 的 framing 需降级为 "empirically validated ordering principle"。
[跟踪: R12-N1, F5-W1]

### Minor/Warning

**W10 [共识]. Abstract "substantially" 超出证据强度。**
N=2, α=1.0, post-hoc 阈值条件下不应使用 "substantially reduces peak perplexity"。
[跟踪: R13-W4]

**W11 [共识]. 偏相关分析（控制 generation number）缺失。**
Granger precedence 可能被 generation number 混淆。控制 generation 的偏相关是标准混淆因素检验，应在附录报告。
[跟踪: R13-W5]

**W12 [R2]. Granger causality 标准局限性未讨论。**
论文引用 Shojaie & Fox (2022) 但未讨论其 §4 的标准局限性（observational equivalence, Lucas critique）。在 intervention 场景下 Lucas critique 的相关性值得讨论。
[跟踪: R13-REF3]

**W13 [持续]. 写作信息密度过高。**
§5.2–5.4 数字密度过高，关键 findings 被淹没。视觉审查印证：pages 5-6 连续纯文本无 display item，Figures 3-5 堆积在 page 7。
[跟踪: R12-W1, R11-VIS2]

---

## Questions

**Q1.** MMCT FPR > PermG standalone 的根本原因是否为高 FPR 方法（NaiveXCor 91.7%）在 null 条件下的投票共现？Appendix R 独立性分析是否充分验证？

**Q2.** 用 DiffXCorr 重绘 Figure 1 的 phase diagram 语义如何（检测"关联存在" vs. "entropy precedes diversity"）？方向性对相变结构的影响是否显著？

**Q3.** α=0.60 异常在 3 seeds 中是否一致出现？若仅 1 seed 异常，是否足以判断为系统性而非随机波动？

**Q4.** 纳入 T=5,15,20,25 数据是否可收窄 γ 的 CI？需注意短序列（T=5）检测功效极低可能引入新噪声。

**Q5.** 跨架构验证为何不在 α=0.50（更有意义的中间条件）进行？两位 Reviewer 独立提出此质疑。

---

## Missing References

**R2 识别, R1 未发现（R1 称"未发现关键缺失引用"——R2 明确反驳）：**

1. **Dakos et al. (2008, 2012)** — 早期预警信号领域核心实证方法论。论文任务（从时间序列检测系统退化早期信号）与该领域高度吻合，且已引用同领域 Scheffer et al. 却遗漏最重要方法论文。[severity: warning]

2. **Lenton et al. (2008)** — 气候 tipping elements 奠基工作。论文使用 tipping point 类比但未引用。[severity: minor]

3. **Guo et al. (2025, arXiv:2502.15654)** — "Machine-generated text detection prevents language model collapse"——与 canary detection 主题直接相关。[需验证是否已在 bib 中——曾在 R4 标记为 resolved (F2-REF1)]

**此外，R2 指出论文未讨论 Granger causality 标准局限性**，而其引用的 Shojaie & Fox (2022) §4 恰好覆盖了 observational equivalence 和 Lucas critique。

**历史遗留 open 引用问题**（未在 R13 复发但仍 open）：Adams & MacKay (2007)、Papana et al. (2013)、Montgomery SPC 等。

---

## External Review

**状态**: 未请求。

---

## Visual Layout Check（非评分项）

**状态**: 完成（3 warning / 9 info）

**Warnings:**
1. **Pages 5-6**: 连续两页纯文本（§4.1 至 §4.4），无 figure/table/equation 穿插。Figures 3-5 全部堆积在 page 7，每图尺寸偏小。建议前移至少一个 figure 改善视觉节奏。[复发 R11-R13]
2. **Page 7**: 三个 figure 集中，axis label 约 6-7pt，低于正文字号 70% 可读性阈值。打印后可能难以辨认。[复发 R8-R13]
3. **Pages 1-2**: 前两页无任何 display item，Figure 1 直到第 3 页。缺少视觉锚点建立第一印象。

**Info（选要）:**
- 主文 8 页 6 figures / 0 tables。所有定量结果表格在 appendix——实证论文应在主文有至少一个核心结果 summary table。
- Figure 2 框内 FPR 数字偏小，打印可能模糊。
- 参考文献格式统一，无 [?] 未解析引用。
- Appendix 表格使用 booktabs 风格但加粗最优值标注不统一。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Reviewer 1**: 3.0 (Findings)
**Reviewer 2**: 3.0 (Findings)
**Director 裁定**: 3.0 (Findings)

**评分理由：**

本文的核心优势在于方法敏感性发现（3%→92% FPR）和系统性实验设计，这对 model collapse 研究社区具有警示价值。Cascade ordering 的 14/15 一致性和详尽的附录分析体现了超出平均水平的实证严谨性。

然而，三个结构性问题阻碍了 Main Conference 接收：

1. **统计可靠性硬伤**（W1, W3, W8）：PermG FPR CI [1.2%, 30.4%] 使核心方法的可靠性存疑；幂律拟合 γ CI [0.64, 2.08] 使定量模型无区分度；边界区 3 seeds / 8 pairs 导致 CI 极宽。这些问题从 R3 至今跨越 10 轮未能根本解决——根源是样本量不足，需要更多实验而非更精妙的统计方法。

2. **Scope-framing 不匹配**（W2）：标题承诺 "detectability landscape" 但实际覆盖仅 Pythia-410M + WikiText-103。跨架构验证仅在最极端条件（α=1.0）进行且 4/15 失败，core contribution zone (α∈[0.45, 0.75]) 完全无跨架构数据。

3. **方法论新颖性天花板**（W6）：核心技术为成熟计量经济学工具的直接迁移。创新体现在问题 framing 和实证发现，而非方法本身。

**Findings 定位合理**：方法敏感性发现和 cascade ordering 的实证贡献足够支撑 Findings 接收；但统计基础的不确定性和实验范围的局限性使得 main conference 的说服力不足。

**与前轮对比（Director 观察）**：R13 论文在 R11-R12 反馈基础上做了显著改进——Abstract 降级幂律 claim、cross-arch 重新定位为 exploratory、GPT-2 FPR 进入正文。但核心问题（null-control 样本量、跨架构覆盖）属于实验规模限制，非写作修改可解决。

---

## Detailed Comments

### 高优先级修改建议（影响 Findings 接收概率）

1. **增加 null-control seeds**：将 null-control 从 6 seeds 增至 ≥12，使 FPR CI 从 [1.2%, 30.4%] 收窄到可判断区间。这是成本最低、收益最高的改进。

2. **α=0.55/0.65 补充实验**：确认 α=0.60 异常是系统性还是随机波动。仅需 2 个额外 α 值 × 3 seeds = 6 个训练 run。

3. **Abstract "substantially" 降级**：将 intervention 描述改为 "proof-of-concept demonstration (N=2, α=1.0)"，删除 "substantially"。

4. **偏相关分析**：在附录报告控制 generation number 后的 Granger precedence，排除混淆。

### 中优先级（改善论文质量）

5. **Figure 1 caption 明确标注**：虚线边界为粗略经验趋势，非定量预测模型。

6. **MMCT K 值敏感性**：补充 K=2,3,4,5 下 FPR/TPR 对比表（可在附录）。

7. **主文加入核心结果 summary table**：将 FPR 对比或 cascade ordering 结果的关键子集移入主文。

8. **视觉节奏调整**：至少将一个 figure 从 page 7 前移至 page 5-6 区域。

### 低优先级（建议但不影响接收）

9. 补充 Dakos et al. (2008, 2012) 和 Lenton et al. (2008) 引用。
10. 在 §3 或 Discussion 讨论 Granger causality 标准局限性。
11. Design Principles 贡献降级为 "empirically validated ordering principle"。

### Reviewer 分歧记录

| 议题 | R1 | R2 | Director 裁定 |
|------|----|----|--------------|
| 方法论新颖性 | empirical systems paper, novelty 合理 | power analysis 迁移, novelty 有限 | novelty 天花板存在但不阻碍 Findings |
| Design Principle 贡献 | mode amplification 下非 trivial | 核心假设强，接近"连续>离散" | framing 需降级，内容可保留 |
| MMCT 共识框架 | 缺乏理论支撑 | FPR-inverse weighting 合理但 K 缺乏证明 | MMCT 可保留但需 K 值敏感性分析 |
| Full replacement 限制 | 限制生态效度 | α=0.10-1.0 覆盖混合比例 | 训练范式（从头训练 vs 增量微调）是真正限制 |
| Missing references | 无关键缺失 | 3 组遗漏引用 | R2 更准确——Dakos et al. 确实应引 |
| AI 写作影响 (Q7) | 需关注 | 缺乏可操作性 | 同意 R2——通过内容本身判断 |
