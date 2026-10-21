# Director coordination — Part 5 of 6

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/c6/c6f03cee0ffebd7a6573.json)

## Round 121

### Tool call

_source line 1256 · 2026-05-24T15:19:31.396752+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 13 审稿报告\n\n**论文**: Characterizing the Detectability Landscape of Iterative Model Collapse\n**Venue**: EMNLP 2026 (via ARR)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 配置**: 2 人（R1: 方法严谨性 + 统计可靠性；R2: 新颖性 + 完整性 + 参考文献）\n**交叉回应**: R1→R2: 8 AGREE / 4 REBUT；R2→R1: 14 AGREE / 3 REBUT\n**收敛状态**: 1 轮收敛，核心关切高度重叠\n\n---\n\n## Summary\n\n本文研究迭代模型坍缩（iterative model collapse）的可检测性问题，在 Pythia-410M + WikiText-103 上对 13 个污染比例进行全网格实验，使用 permutation Granger causality（PermG）等 5 种统计方法构建检测景观（phase diagram）。主要发现包括：(1) 方法选择极大影响结论——5 种方法在相同数据上产生 3%–92% 的 null-control FPR；(2) 检测边界呈现 blind/onset/detection 三个 regime 加一个未解释异常；(3) entropy Granger-precedes diversity collapse ≥1 generation（14/15 实验）；(4) 跨架构评估（仅 α=1.0）在 5 个模型族 11/15 条件下支持前向检测。论文附录极为详尽，包含 specification curve、Shapley 分解、非平稳性鲁棒性等分析。\n\n---\n\n## Strengths\n\n**S1 [共识]. 方法敏感性发现具有社区警示价值。** 5 种方法在相同数据上产生 3%→92% 的 FPR 跨度（§3.3, Table 1），这一发现对 model collapse 检测研究具有直接实用意义，提醒研究者方法选择是影响结论的首要因素。两位 Reviewer 独立将其列为首要优点。\n\n**S2 [共识]. 问题定义有价值。** \"何时可检测到\"比\"是否发生\"更有实用意义，将检测问题转化为关于检测功效（statistical power）随参数变化的系统性研究。R2 补充：本质上是统计检验功效分析在新领域的应用，概念新颖性不应高估。\n\n**S3 [共识]. Cascade ordering 一致性稳健。** 14/15 实验中 entropy Granger-precedes diversity collapse 的级联序一致性（§4.3, Appendix W），为 canary 概念提供了实证基础。R2 保留意见：连续统计量先于离散统计量响应在信息论层面可能较直观。\n\n**S4 [共识]. Propositions 4-5 增加形式严谨性。** Appendix X 的形式化推导为 cascade ordering 提供了理论支撑。R1 认为非 trivial（mode amplification 下的特定机制），R2 认为核心假设（Assumption 3）较强。\n\n**S5 [共识]. 附录详尽程度罕见。** Specification curve（Appendix E）、Shapley 分解（Appendix P）、非平稳性鲁棒性（Appendix O）等分析展现了超出一般投稿水平的实证严谨性。\n\n**S6 [共识]. 诚实披露局限。** PermG FPR 膨胀、α=0.60 异常、GPT-2 失败等均在正文明确提及。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**W1 [共识, 复发 R3-R13]. PermG FPR 膨胀——null-control 样本量根本不足。**\nPermG 的 null-control FPR CI 为 [1.2%, 30.4%]，跨越两个数量级——FPR 可能是 1%（可接受）或 30%（完全不可用）。根源是 null-control 仅 36 pairs（6 seeds × 6-pair basis）。该问题从 Round 3 至今跨越 10 轮审稿未能根本解决。R2 进一步指出：替代方案 DiffXCorr 是 bidirectional 的，无法替代 PermG 在 phase diagram 中的方向性角色；正确替代应保持方向性约束下改进置换分布估计（增大置换次数至 50000 或 bootstrap）。**需要更多 null-control 实验，统计方法无法弥补样本量不足。**\n[跟踪: F3-J4]\n\n**W2 [共识, 复发 R2-R13]. 实验范围与 framing 严重不匹配。**\n\"Detectability Landscape\" 标题暗示广泛覆盖，实际 landscape 仅在 Pythia-410M + WikiText-103 上绘制。跨架构验证仅在 α=1.0——最极端（最容易检测）条件——下进行，且 4/15 条件失败。Phase diagram 核心贡献区 α∈[0.45, 0.75] 完全没有跨架构数据。\"Five families (345M–6.9B)\" 给读者广泛可推广印象，但实际深度实验局限于单一架构。两位 Reviewer 独立得出相同质疑（R1-W2/W6, R2-W3/Q1），R2 建议标题修改为含 \"on Pythia-410M\"。\n[跟踪: F2-W2b, F2-W10, R10-MF5]\n\n**W3 [共识, 复发 R2-R13]. 幂律拟合无信息量。**\nγ 的 95% CI [0.64, 2.08] 跨越定性不同的缩放行为（亚线性 vs. 超线性），使幂律模型无法提供有区分度的预测。β 参数 MLE=0.66 vs CV=0.24（CI [0.24, 0.78]）进一步证实拟合不稳定。R13 论文修改（Abstract 删除 MAE=0.037，改为 \"consistent with power-law scaling\"）方向正确，但 Figure 1 虚线边界仍可能被读者解读为定量预测模型。\n[跟踪: F2-W4b, R11-N1]\n\n### Major\n\n**W4 [共识]. α=0.60 异常排除对拟合结果影响根本性。**\n仅 4 个边界 α 值中排除 1 个（α=0.60），对幂律拟合结果可能是决定性的。3 seeds 中 1 个异常即可产生非单调表象。R1 建议增加 α=0.55/0.65 实验——直接可行且必要。R2 进一步指出 α=0.60 异常可能与 SmolLM1.3B 跨架构非单调行为有关联。\n[跟踪: F2-W1, R13-W2]\n\n**W5 [共识, 复发 R2-R13]. Intervention 证据薄弱。**\nAbstract \"substantially reduces peak perplexity\" 基于 N=2 seeds、α=1.0 单一条件、post-hoc 选择的 15% 阈值。两位 Reviewer 共识应降级为 \"preliminary proof-of-concept\"。R2 补充 Appendix H CUSUM comparison 显示 simple threshold 同效，削弱了 Granger 框架的实用优势。建议从主要贡献剥离。\n[跟踪: F2-W7]\n\n**W6 [共识, 复发 R5-R13]. 方法论新颖性有限。**\n核心方法（permutation Granger causality、BH-FDR 校正、specification curve）均为计量经济学/统计学已有技术的直接迁移。R1 rebut：本文定位是 empirical systems paper 非方法论创新。R2 同意但指出本质是统计检验功效分析（power analysis）在新领域的应用。交叉后共识：novelty 来自 method-sensitivity finding 和 phase-diagram framing，非技术方法本身。**这是不可改变的天花板**——不影响 Findings 接收但排除 Main Conference 考虑。\n[跟踪: F5-N1]\n\n**W7 [R1 主张, R2 部分同意]. MMCT K≥3 共识 K 值缺乏理论依据。**\nκ=0.185 表明方法间几乎无 agreement。MMCT FPR (16.7%) > PermG standalone (11.1%)。R2 部分 rebut：论文使用 FPR-inverse weighting 非简单投票，MMCT 仅作鲁棒性检查。但 R2 同意 K 选择缺乏理论最优性证明。共识：应提供不同 K 值下 MMCT FPR/TPR 曲线。\n[跟踪: R13-W1]\n\n**W8 [共识]. 检测边界区 seed 数量不足。**\nα≈0.45–0.60 是论文最重要的贡献区域，但每个 α 值仅 3 seeds。α=0.10 仅单 seed。边界区应增加至 ≥5 seeds。每 cell 仅 8 pairs 的 binomial CI [0.25, 0.92] 极宽。\n[跟踪: R11-W2, R10-SF7]\n\n**W9 [共识]. Design Principles 作为独立贡献 oversells。**\nPropositions 4-5 的核心假设（Assumption 3: mode amplification）较强，结论接近\"连续指标比离散指标对微小偏移更敏感\"。R1 rebut：specific ordering derivation 非 trivial。交叉后共识：内容非 trivial 但 \"formal design rationale\" 作为 Contribution 2 的 framing 需降级为 \"empirically validated ordering principle\"。\n[跟踪: R12-N1, F5-W1]\n\n### Minor/Warning\n\n**W10 [共识]. Abstract \"substantially\" 超出证据强度。**\nN=2, α=1.0, post-hoc 阈值条件下不应使用 \"substantially reduces peak perplexity\"。\n[跟踪: R13-W4]\n\n**W11 [共识]. 偏相关分析（控制 generation number）缺失。**\nGranger precedence 可能被 generation number 混淆。控制 generation 的偏相关是标准混淆因素检验，应在附录报告。\n[跟踪: R13-W5]\n\n**W12 [R2]. Granger causality 标准局限性未讨论。**\n论文引用 Shojaie & Fox (2022) 但未讨论其 §4 的标准局限性（observational equivalence, Lucas critique）。在 intervention 场景下 Lucas critique 的相关性值得讨论。\n[跟踪: R13-REF3]\n\n**W13 [持续]. 写作信息密度过高。**\n§5.2–5.4 数字密度过高，关键 findings 被淹没。视觉审查印证：pages 5-6 连续纯文本无 display item，Figures 3-5 堆积在 page 7。\n[跟踪: R12-W1, R11-VIS2]\n\n---\n\n## Questions\n\n**Q1.** MMCT FPR > PermG standalone 的根本原因是否为高 FPR 方法（NaiveXCor 91.7%）在 null 条件下的投票共现？Appendix R 独立性分析是否充分验证？\n\n**Q2.** 用 DiffXCorr 重绘 Figure 1 的 phase diagram 语义如何（检测\"关联存在\" vs. \"entropy precedes diversity\"）？方向性对相变结构的影响是否显著？\n\n**Q3.** α=0.60 异常在 3 seeds 中是否一致出现？若仅 1 seed 异常，是否足以判断为系统性而非随机波动？\n\n**Q4.** 纳入 T=5,15,20,25 数据是否可收窄 γ 的 CI？需注意短序列（T=5）检测功效极低可能引入新噪声。\n\n**Q5.** 跨架构验证为何不在 α=0.50（更有意义的中间条件）进行？两位 Reviewer 独立提出此质疑。\n\n---\n\n## Missing References\n\n**R2 识别, R1 未发现（R1 称\"未发现关键缺失引用\"——R2 明确反驳）：**\n\n1. **Dakos et al. (2008, 2012)** — 早期预警信号领域核心实证方法论。论文任务（从时间序列检测系统退化早期信号）与该领域高度吻合，且已引用同领域 Scheffer et al. 却遗漏最重要方法论文。[severity: warning]\n\n2. **Lenton et al. (2008)** — 气候 tipping elements 奠基工作。论文使用 tipping point 类比但未引用。[severity: minor]\n\n3. **Guo et al. (2025, arXiv:2502.15654)** — \"Machine-generated text detection prevents language model collapse\"——与 canary detection 主题直接相关。[需验证是否已在 bib 中——曾在 R4 标记为 resolved (F2-REF1)]\n\n**此外，R2 指出论文未讨论 Granger causality 标准局限性**，而其引用的 Shojaie & Fox (2022) §4 恰好覆盖了 observational equivalence 和 Lucas critique。\n\n**历史遗留 open 引用问题**（未在 R13 复发但仍 open）：Adams & MacKay (2007)、Papana et al. (2013)、Montgomery SPC 等。\n\n---\n\n## External Review\n\n**状态**: 未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 完成（3 warning / 9 info）\n\n**Warnings:**\n1. **Pages 5-6**: 连续两页纯文本（§4.1 至 §4.4），无 figure/table/equation 穿插。Figures 3-5 全部堆积在 page 7，每图尺寸偏小。建议前移至少一个 figure 改善视觉节奏。[复发 R11-R13]\n2. **Page 7**: 三个 figure 集中，axis label 约 6-7pt，低于正文字号 70% 可读性阈值。打印后可能难以辨认。[复发 R8-R13]\n3. **Pages 1-2**: 前两页无任何 display item，Figure 1 直到第 3 页。缺少视觉锚点建立第一印象。\n\n**Info（选要）:**\n- 主文 8 页 6 figures / 0 tables。所有定量结果表格在 appendix——实证论文应在主文有至少一个核心结果 summary table。\n- Figure 2 框内 FPR 数字偏小，打印可能模糊。\n- 参考文献格式统一，无 [?] 未解析引用。\n- Appendix 表格使用 booktabs 风格但加粗最优值标注不统一。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Reviewer 1**: 3.0 (Findings)\n**Reviewer 2**: 3.0 (Findings)\n**Director 裁定**: 3.0 (Findings)\n\n**评分理由：**\n\n本文的核心优势在于方法敏感性发现（3%→92% FPR）和系统性实验设计，这对 model collapse 研究社区具有警示价值。Cascade ordering 的 14/15 一致性和详尽的附录分析体现了超出平均水平的实证严谨性。\n\n然而，三个结构性问题阻碍了 Main Conference 接收：\n\n1. **统计可靠性硬伤**（W1, W3, W8）：PermG FPR CI [1.2%, 30.4%] 使核心方法的可靠性存疑；幂律拟合 γ CI [0.64, 2.08] 使定量模型无区分度；边界区 3 seeds / 8 pairs 导致 CI 极宽。这些问题从 R3 至今跨越 10 轮未能根本解决——根源是样本量不足，需要更多实验而非更精妙的统计方法。\n\n2. **Scope-framing 不匹配**（W2）：标题承诺 \"detectability landscape\" 但实际覆盖仅 Pythia-410M + WikiText-103。跨架构验证仅在最极端条件（α=1.0）进行且 4/15 失败，core contribution zone (α∈[0.45, 0.75]) 完全无跨架构数据。\n\n3. **方法论新颖性天花板**（W6）：核心技术为成熟计量经济学工具的直接迁移。创新体现在问题 framing 和实证发现，而非方法本身。\n\n**Findings 定位合理**：方法敏感性发现和 cascade ordering 的实证贡献足够支撑 Findings 接收；但统计基础的不确定性和实验范围的局限性使得 main conference 的说服力不足。\n\n**与前轮对比（Director 观察）**：R13 论文在 R11-R12 反馈基础上做了显著改进——Abstract 降级幂律 claim、cross-arch 重新定位为 exploratory、GPT-2 FPR 进入正文。但核心问题（null-control 样本量、跨架构覆盖）属于实验规模限制，非写作修改可解决。\n\n---\n\n## Detailed Comments\n\n### 高优先级修改建议（影响 Findings 接收概率）\n\n1. **增加 null-control seeds**：将 null-control 从 6 seeds 增至 ≥12，使 FPR CI 从 [1.2%, 30.4%] 收窄到可判断区间。这是成本最低、收益最高的改进。\n\n2. **α=0.55/0.65 补充实验**：确认 α=0.60 异常是系统性还是随机波动。仅需 2 个额外 α 值 × 3 seeds = 6 个训练 run。\n\n3. **Abstract \"substantially\" 降级**：将 intervention 描述改为 \"proof-of-concept demonstration (N=2, α=1.0)\"，删除 \"substantially\"。\n\n4. **偏相关分析**：在附录报告控制 generation number 后的 Granger precedence，排除混淆。\n\n### 中优先级（改善论文质量）\n\n5. **Figure 1 caption 明确标注**：虚线边界为粗略经验趋势，非定量预测模型。\n\n6. **MMCT K 值敏感性**：补充 K=2,3,4,5 下 FPR/TPR 对比表（可在附录）。\n\n7. **主文加入核心结果 summary table**：将 FPR 对比或 cascade ordering 结果的关键子集移入主文。\n\n8. **视觉节奏调整**：至少将一个 figure 从 page 7 前移至 page 5-6 区域。\n\n### 低优先级（建议但不影响接收）\n\n9. 补充 Dakos et al. (2008, 2012) 和 Lenton et al. (2008) 引用。\n10. 在 §3 或 Discussion 讨论 Granger causality 标准局限性。\n11. Design Principles 贡献降级为 \"empirically validated ordering principle\"。\n\n### Reviewer 分歧记录\n\n| 议题 | R1 | R2 | Director 裁定 |\n|------|----|----|--------------|\n| 方法论新颖性 | empirical systems paper, novelty 合理 | power analysis 迁移, novelty 有限 | novelty 天花板存在但不阻碍 Findings |\n| Design Principle 贡献 | mode amplification 下非 trivial | 核心假设强，接近\"连续>离散\" | framing 需降级，内容可保留 |\n| MMCT 共识框架 | 缺乏理论支撑 | FPR-inverse weighting 合理但 K 缺乏证明 | MMCT 可保留但需 K 值敏感性分析 |\n| Full replacement 限制 | 限制生态效度 | α=0.10-1.0 覆盖混合比例 | 训练范式（从头训练 vs 增量微调）是真正限制 |\n| Missing references | 无关键缺失 | 3 组遗漏引用 | R2 更准确——Dakos et al. 确实应引 |\n| AI 写作影响 (Q7) | 需关注 | 缺乏可操作性 | 同意 R2——通过内容本身判断 |\n",
  "project": "distrib_canary_collapse",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 13 审稿报告\n\n**论文**: Characterizing the Detectability Landscape of Iterative Model Collapse\n**Venue**: EMNLP 2026 (via ARR)\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 配置**: 2 人（R1: 方法严谨性 + 统计可靠性；R2: 新颖性 + 完整性 + 参考文献）\n**交叉回应**: R1→R2: 8 AGREE / 4 REBUT；R2→R1: 14 AGREE / 3 REBUT\n**收敛状态**: 1 轮收敛，核心关切高度重叠\n\n---\n\n## Summary\n\n本文研究迭代模型坍缩（iterative model collapse）的可检测性问题，在 Pythia-410M + WikiText-103 上对 13 个污染比例进行全网格实验，使用 permutation Granger causality（PermG）等 5 种统计方法构建检测景观（phase diagram）。主要发现包括：(1) 方法选择极大影响结论——5 种方法在相同数据上产生 3%–92% 的 null-control FPR；(2) 检测边界呈现 blind/onset/detection 三个 regime 加一个未解释异常；(3) entropy Granger-precedes diversity collapse ≥1 generation（14/15 实验）；(4) 跨架构评估（仅 α=1.0）在 5 个模型族 11/15 条件下支持前向检测。论文附录极为详尽，包含 specification curve、Shapley 分解、非平稳性鲁棒性等分析。\n\n---\n\n## Strengths\n\n**S1 [共识]. 方法敏感性发现具有社区警示价值。** 5 种方法在相同数据上产生 3%→92% 的 FPR 跨度（§3.3, Table 1），这一发现对 model collapse 检测研究具有直接实用意义，提醒研究者方法选择是影响结论的首要因素。两位 Reviewer 独立将其列为首要优点。\n\n**S2 [共识]. 问题定义有价值。** \"何时可检测到\"比\"是否发生\"更有实用意义，将检测问题转化为关于检测功效（statistical power）随参数变化的系统性研究。R2 补充：本质上是统计检验功效分析在新领域的应用，概念新颖性不应高估。\n\n**S3 [共识]. Cascade ordering 一致性稳健。** 14/15 实验中 entropy Granger-precedes diversity collapse 的级联序一致性（§4.3, Appendix W），为 canary 概念提供了实证基础。R2 保留意见：连续统计量先于离散统计量响应在信息论层面可能较直观。\n\n**S4 [共识]. Propositions 4-5 增加形式严谨性。** Appendix X 的形式化推导为 cascade ordering 提供了理论支撑。R1 认为非 trivial（mode amplification 下的特定机制），R2 认为核心假设（Assumption 3）较强。\n\n**S5 [共识]. 附录详尽程度罕见。** Specification curve（Appendix E）、Shapley 分解（Appendix P）、非平稳性鲁棒性（Appendix O）等分析展现了超出一般投稿水平的实证严谨性。\n\n**S6 [共识]. 诚实披露局限。** PermG FPR 膨胀、α=0.60 异常、GPT-2 失败等均在正文明确提及。\n\n---\n\n## Weaknesses\n\n### Critical\n\n**W1 [共识, 复发 R3-R13]. PermG FPR 膨胀——null-control 样本量根本不足。**\nPermG 的 null-control FPR CI 为 [1.2%, 30.4%]，跨越两个数量级——FPR 可能是 1%（可接受）或 30%（完全不可用）。根源是 null-control 仅 36 pairs（6 seeds × 6-pair basis）。该问题从 Round 3 至今跨越 10 轮审稿未能根本解决。R2 进一步指出：替代方案 DiffXCorr 是 bidirectional 的，无法替代 PermG 在 phase diagram 中的方向性角色；正确替代应保持方向性约束下改进置换分布估计（增大置换次数至 50000 或 bootstrap）。**需要更多 null-control 实验，统计方法无法弥补样本量不足。**\n[跟踪: F3-J4]\n\n**W2 [共识, 复发 R2-R13]. 实验范围与 framing 严重不匹配。**\n\"Detectability Landscape\" 标题暗示广泛覆盖，实际 landscape 仅在 Pythia-410M + WikiText-103 上绘制。跨架构验证仅在 α=1.0——最极端（最容易检测）条件——下进行，且 4/15 条件失败。Phase diagram 核心贡献区 α∈[0.45, 0.75] 完全没有跨架构数据。\"Five families (345M–6.9B)\" 给读者广泛可推广印象，但实际深度实验局限于单一架构。两位 Reviewer 独立得出相同质疑（R1-W2/W6, R2-W3/Q1），R2 建议标题修改为含 \"on Pythia-410M\"。\n[跟踪: F2-W2b, F2-W10, R10-MF5]\n\n**W3 [共识, 复发 R2-R13]. 幂律拟合无信息量。**\nγ 的 95% CI [0.64, 2.08] 跨越定性不同的缩放行为（亚线性 vs. 超线性），使幂律模型无法提供有区分度的预测。β 参数 MLE=0.66 vs CV=0.24（CI [0.24, 0.78]）进一步证实拟合不稳定。R13 论文修改（Abstract 删除 MAE=0.037，改为 \"consistent with power-law scaling\"）方向正确，但 Figure 1 虚线边界仍可能被读者解读为定量预测模型。\n[跟踪: F2-W4b, R11-N1]\n\n### Major\n\n**W4 [共识]. α=0.60 异常排除对拟合结果影响根本性。**\n仅 4 个边界 α 值中排除 1 个（α=0.60），对幂律拟合结果可能是决定性的。3 seeds 中 1 个异常即可产生非单调表象。R1 建议增加 α=0.55/0.65 实验——直接可行且必要。R2 进一步指出 α=0.60 异常可能与 SmolLM1.3B 跨架构非单调行为有关联。\n[跟踪: F2-W1, R13-W2]\n\n**W5 [共识, 复发 R2-R13]. Intervention 证据薄弱。**\nAbstract \"substantially reduces peak perplexity\" 基于 N=2 seeds、α=1.0 单一条件、post-hoc 选择的 15% 阈值。两位 Reviewer 共识应降级为 \"preliminary proof-of-concept\"。R2 补充 Appendix H CUSUM comparison 显示 simple threshold 同效，削弱了 Granger 框架的实用优势。建议从主要贡献剥离。\n[跟踪: F2-W7]\n\n**W6 [共识, 复发 R5-R13]. 方法论新颖性有限。**\n核心方法（permutation Granger causality、BH-FDR 校正、specification curve）均为计量经济学/统计学已有技术的直接迁移。R1 rebut：本文定位是 empirical systems paper 非方法论创新。R2 同意但指出本质是统计检验功效分析（power analysis）在新领域的应用。交叉后共识：novelty 来自 method-sensitivity finding 和 phase-diagram framing，非技术方法本身。**这是不可改变的天花板**——不影响 Findings 接收但排除 Main Conference 考虑。\n[跟踪: F5-N1]\n\n**W7 [R1 主张, R2 部分同意]. MMCT K≥3 共识 K 值缺乏理论依据。**\nκ=0.185 表明方法间几乎无 agreement。MMCT FPR (16.7%) > PermG standalone (11.1%)。R2 部分 rebut：论文使用 FPR-inverse weighting 非简单投票，MMCT 仅作鲁棒性检查。但 R2 同意 K 选择缺乏理论最优性证明。共识：应提供不同 K 值下 MMCT FPR/TPR 曲线。\n[跟踪: R13-W1]\n\n**W8 [共识]. 检测边界区 seed 数量不足。**\nα≈0.45–0.60 是论文最重要的贡献区域，但每个 α 值仅 3 seeds。α=0.10 仅单 seed。边界区应增加至 ≥5 seeds。每 cell 仅 8 pairs 的 binomial CI [0.25, 0.92] 极宽。\n[跟踪: R11-W2, R10-SF7]\n\n**W9 [共识]. Design Principles 作为独立贡献 oversells。**\nPropositions 4-5 的核心假设（Assumption 3: mode amplification）较强，结论接近\"连续指标比离散指标对微小偏移更敏感\"。R1 rebut：specific ordering derivation 非 trivial。交叉后共识：内容非 trivial 但 \"formal design rationale\" 作为 Contribution 2 的 framing 需降级为 \"empirically validated ordering principle\"。\n[跟踪: R12-N1, F5-W1]\n\n### Minor/Warning\n\n**W10 [共识]. Abstract \"substantially\" 超出证据强度。**\nN=2, α=1.0, post-hoc 阈值条件下不应使用 \"substantially reduces peak perplexity\"。\n[跟踪: R13-W4]\n\n**W11 [共识]. 偏相关分析（控制 generation number）缺失。**\nGranger precedence 可能被 generation number 混淆。控制 generation 的偏相关是标准混淆因素检验，应在附录报告。\n[跟踪: R13-W5]\n\n**W12 [R2]. Granger causality 标准局限性未讨论。**\n论文引用 Shojaie & Fox (2022) 但未讨论其 §4 的标准局限性（observational equivalence, Lucas critique）。在 intervention 场景下 Lucas critique 的相关性值得讨论。\n[跟踪: R13-REF3]\n\n**W13 [持续]. 写作信息密度过高。**\n§5.2–5.4 数字密度过高，关键 findings 被淹没。视觉审查印证：pages 5-6 连续纯文本无 display item，Figures 3-5 堆积在 page 7。\n[跟踪: R12-W1, R11-VIS2]\n\n---\n\n## Questions\n\n**Q1.** MMCT FPR > PermG standalone 的根本原因是否为高 FPR 方法（NaiveXCor 91.7%）在 null 条件下的投票共现？Appendix R 独立性分析是否充分验证？\n\n**Q2.** 用 DiffXCorr 重绘 Figure 1 的 phase diagram 语义如何（检测\"关联存在\" vs. \"entropy precedes diversity\"）？方向性对相变结构的影响是否显著？\n\n**Q3.** α=0.60 异常在 3 seeds 中是否一致出现？若仅 1 seed 异常，是否足以判断为系统性而非随机波动？\n\n**Q4.** 纳入 T=5,15,20,25 数据是否可收窄 γ 的 CI？需注意短序列（T=5）检测功效极低可能引入新噪声。\n\n**Q5.** 跨架构验证为何不在 α=0.50（更有意义的中间条件）进行？两位 Reviewer 独立提出此质疑。\n\n---\n\n## Missing References\n\n**R2 识别, R1 未发现（R1 称\"未发现关键缺失引用\"——R2 明确反驳）：**\n\n1. **Dakos et al. (2008, 2012)** — 早期预警信号领域核心实证方法论。论文任务（从时间序列检测系统退化早期信号）与该领域高度吻合，且已引用同领域 Scheffer et al. 却遗漏最重要方法论文。[severity: warning]\n\n2. **Lenton et al. (2008)** — 气候 tipping elements 奠基工作。论文使用 tipping point 类比但未引用。[severity: minor]\n\n3. **Guo et al. (2025, arXiv:2502.15654)** — \"Machine-generated text detection prevents language model collapse\"——与 canary detection 主题直接相关。[需验证是否已在 bib 中——曾在 R4 标记为 resolved (F2-REF1)]\n\n**此外，R2 指出论文未讨论 Granger causality 标准局限性**，而其引用的 Shojaie & Fox (2022) §4 恰好覆盖了 observational equivalence 和 Lucas critique。\n\n**历史遗留 open 引用问题**（未在 R13 复发但仍 open）：Adams & MacKay (2007)、Papana et al. (2013)、Montgomery SPC 等。\n\n---\n\n## External Review\n\n**状态**: 未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 完成（3 warning / 9 info）\n\n**Warnings:**\n1. **Pages 5-6**: 连续两页纯文本（§4.1 至 §4.4），无 figure/table/equation 穿插。Figures 3-5 全部堆积在 page 7，每图尺寸偏小。建议前移至少一个 figure 改善视觉节奏。[复发 R11-R13]\n2. **Page 7**: 三个 figure 集中，axis label 约 6-7pt，低于正文字号 70% 可读性阈值。打印后可能难以辨认。[复发 R8-R13]\n3. **Pages 1-2**: 前两页无任何 display item，Figure 1 直到第 3 页。缺少视觉锚点建立第一印象。\n\n**Info（选要）:**\n- 主文 8 页 6 figures / 0 tables。所有定量结果表格在 appendix——实证论文应在主文有至少一个核心结果 summary table。\n- Figure 2 框内 FPR 数字偏小，打印可能模糊。\n- 参考文献格式统一，无 [?] 未解析引用。\n- Appendix 表格使用 booktabs 风格但加粗最优值标注不统一。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**Reviewer 1**: 3.0 (Findings)\n**Reviewer 2**: 3.0 (Findings)\n**Director 裁定**: 3.0 (Findings)\n\n**评分理由：**\n\n本文的核心优势在于方法敏感性发现（3%→92% FPR）和系统性实验设计，这对 model collapse 研究社区具有警示价值。Cascade ordering 的 14/15 一致性和详尽的附录分析体现了超出平均水平的实证严谨性。\n\n然而，三个结构性问题阻碍了 Main Conference 接收：\n\n1. **统计可靠性硬伤**（W1, W3, W8）：PermG FPR CI [1.2%, 30.4%] 使核心方法的可靠性存疑；幂律拟合 γ CI [0.64, 2.08] 使定量模型无区分度；边界区 3 seeds / 8 pairs 导致 CI 极宽。这些问题从 R3 至今跨越 10 轮未能根本解决——根源是样本量不足，需要更多实验而非更精妙的统计方法。\n\n2. **Scope-framing 不匹配**（W2）：标题承诺 \"detectability landscape\" 但实际覆盖仅 Pythia-410M + WikiText-103。跨架构验证仅在最极端条件（α=1.0）进行且 4/15 失败，core contribution zone (α∈[0.45, 0.75]) 完全无跨架构数据。\n\n3. **方法论新颖性天花板**（W6）：核心技术为成熟计量经济学工具的直接迁移。创新体现在问题 framing 和实证发现，而非方法本身。\n\n**Findings 定位合理**：方法敏感性发现和 cascade ordering 的实证贡献足够支撑 Findings 接收；但统计基础的不确定性和实验范围的局限性使得 main conference 的说服力不足。\n\n**与前轮对比（Director 观察）**：R13 论文在 R11-R12 反馈基础上做了显著改进——Abstract 降级幂律 claim、cross-arch 重新定位为 exploratory、GPT-2 FPR 进入正文。但核心问题（null-control 样本量、跨架构覆盖）属于实验规模限制，非写作修改可解决。\n\n---\n\n## Detailed Comments\n\n### 高优先级修改建议（影响 Findings 接收概率）\n\n1. **增加 null-control seeds**：将 null-control 从 6 seeds 增至 ≥12，使 FPR CI 从 [1.2%, 30.4%] 收窄到可判断区间。这是成本最低、收益最高的改进。\n\n2. **α=0.55/0.65 补充实验**：确认 α=0.60 异常是系统性还是随机波动。仅需 2 个额外 α 值 × 3 seeds = 6 个训练 run。\n\n3. **Abstract \"substantially\" 降级**：将 intervention 描述改为 \"proof-of-concept demonstration (N=2, α=1.0)\"，删除 \"substantially\"。\n\n4. **偏相关分析**：在附录报告控制 generation number 后的 Granger precedence，排除混淆。\n\n### 中优先级（改善论文质量）\n\n5. **Figure 1 caption 明确标注**：虚线边界为粗略经验趋势，非定量预测模型。\n\n6. **MMCT K 值敏感性**：补充 K=2,3,4,5 下 FPR/TPR 对比表（可在附录）。\n\n7. **主文加入核心结果 summary table**：将 FPR 对比或 cascade ordering 结果的关键子集移入主文。\n\n8. **视觉节奏调整**：至少将一个 figure 从 page 7 前移至 page 5-6 区域。\n\n### 低优先级（建议但不影响接收）\n\n9. 补充 Dakos et al. (2008, 2012) 和 Lenton et al. (2008) 引用。\n10. 在 §3 或 Discussion 讨论 Granger causality 标准局限性。\n11. Design Principles 贡献降级为 \"empirically validated ordering principle\"。\n\n### Reviewer 分歧记录\n\n| 议题 | R1 | R2 | Director 裁定 |\n|------|----|----|--------------|\n| 方法论新颖性 | empirical systems paper, novelty 合理 | power analysis 迁移, novelty 有限 | novelty 天花板存在但不阻碍 Findings |\n| Design Principle 贡献 | mode amplification 下非 trivial | 核心假设强，接近\"连续>离散\" | framing 需降级，内容可保留 |\n| MMCT 共识框架 | 缺乏理论支撑 | FPR-inverse weighting 合理但 K 缺乏证明 | MMCT 可保留但需 K 值敏感性分析 |\n| Full replacement 限制 | 限制生态效度 | α=0.10-1.0 覆盖混合比例 | 训练范式（从头训练 vs 增量微调）是真正限制 |\n| Missing references | 无关键缺失 | 3 组遗漏引用 | R2 更准确——Dakos et al. 确实应引 |\n| AI 写作影响 (Q7) | 需关注 | 缺乏可操作性 | 同意 R2——通过内容本身判断 |\n",
    "project": "distrib_canary_collapse",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
  }
}
```

</details>

---


### Tool result

_source line 1257 · 2026-05-24T15:19:35.467439+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_150c7ce908e05d7932315e0288cf5bfb:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4070
}
```

</details>

---


### Assistant

_source line 1258 · 2026-05-24T15:19:47.941822+00:00_

Round 13 审稿报告已投递。

**最终评分：3.0 (Findings)**，两位 Reviewer 独立一致。

核心结论：
- **最强贡献**：方法敏感性发现（3%→92% FPR）和 cascade ordering 一致性
- **三个结构性限制阻碍 Main Conference**：(1) null-control 样本量根本不足导致 FPR CI 跨两个数量级——跨 10 轮未解决；(2) landscape 仅 Pythia-410M 但标题暗示广泛覆盖；(3) 方法论新颖性天花板
- **最高 ROI 改进**：增加 null-control seeds 至 ≥12（成本低，直接收窄 FPR CI）

Issue Tracker 已同步更新，新增 9 个 R13 issues，历史 issues 状态已刷新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 122

## Round 122

46 recorded events


### User

_source line 1259 · 2026-05-24T22:49:23.267365+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distrib_canary_collapse
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 2026-06-15
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1260 · 2026-05-24T22:49:28.806320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1261 · 2026-05-24T22:49:28.907600+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1262 · 2026-05-24T22:49:38.330198+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-24T22:49:38.380818+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-24T22:49:42.532048+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1265 · 2026-05-24T22:49:43.556747+00:00_

{"result":"# 项目 distrib_canary_collapse 概况\n\n## 实验状态 (215 个)\n\n- **gen_wiki_gpt2m_a100_s42_v3**: DONE (success) — \n- **mvp_v4_rep44**: DONE (success) — \n- **plan_006_s42**: DONE (failed) — \n- **plan_006_s42_resume**: DONE (killed) — \n- **gen_wiki_gpt2m_a100_s42_v2**: DONE (killed) — \n- **method_ablation_phase2**: DONE (success) — \n- **alpha_sweep_a025_s42_v3**: DONE (success) — \n- **method_ablation_phase1**: DONE (success) — \n- **plan_009_bootstrap_ty**: DONE (success) — \n- **mvp_v3_rep43**: DONE (failed) — \n- **mvp_v3_rep42**: DONE (failed) — \n- **mvp_v2_rep43**: DONE (killed) — \n- **mvp_v2_rep42**: DONE (killed) — \n- **mvp_rep43**: DONE (killed) — \n- **mvp_rep42**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| null_fpr_s51_fp32 | Null experiment (α=0.00) for FPR estimation: no synthetic data contamination, all detection methods should show p>0.05, contributing to narrower FPR CI with 15 seeds | — | — | — |\n\n## 待处理\n- 14b_t10_a060_s43（准备中）\n- 14b_t10_a075_s43（准备中）\n- 14b_t10_a050_s43（准备中）\n- t15_a050_s42_fp32（准备中）\n- qwen35_dryrun_launch（准备中）\n\n## 近期结论\n- **null_t15_s42_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n- **null_t15_s43_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n- **null_gpt2m_s43_fp32** (success): Cross-architecture FPR verification: GPT-2-medium null (α=0.00) should show 0% PermG detection rate, confirming method is not architecture-specific\n\n## 趋势\n成功 153 / 负向 4 / 失败 22 / 共 209\n累计 GPU: 8.4h\nrobust_pairs_K3: 0 →（近 3 次 success）\ntotal_pairs: 6 →（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-19828: 空闲 cuda
…[truncated 1799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1024
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-24T22:49:43.557145+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1267 · 2026-05-24T22:49:43.557382+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1268 · 2026-05-24T22:49:44.109880+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1269 · 2026-05-24T22:49:44.110334+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1270 · 2026-05-24T22:49:45.667192+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1271 · 2026-05-24T22:49:45.718248+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{graphicx}
13	\usepackage{booktabs}
14	\usepackage{subcaption}
15	\usepackage{dblfloatfix}
16	\usepackage{placeins}
17	\usepackage{algorithm}
18	\usepackage{algpseudocode}
19	\usepackage{amsthm}
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{proposition}[theorem]{Proposition}
22	\newtheorem{designprinciple}[theorem]{Design Principle}
23	\theoremstyle{definition}
24	\newtheorem{assumption}[theorem]{Assumption}
25	
26	\title{Characterizing the Detectability Landscape of Iterative Model Collapse}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	\input{introduction}
35	\input{related_work}
36	\input{method}
37	\input{experiments}
38	\input{discussion}
39	\input{conclusion}
40	\input{limitations}
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1272 · 2026-05-24T22:49:52.196041+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR"
  }
}
```

</details>

---


### Tool call

_source line 1273 · 2026-05-24T22:49:54.255563+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1274 · 2026-05-24T22:49:55.009537+00:00_

1	issues:
2	# ============================================================
3	# Round 1-11 历史 resolved — 保留跨轮次记录
4	# ============================================================
5	- id: "R1-N1"
6	  summary: "Ground-truth pairs 定义存在循环论证"
7	  category: method
8	  severity: critical
9	  status: resolved
10	  first_raised_round: 1
11	  last_seen_round: 1
12	  resolution: "Effect-size GT 重定义完成。"
13	  resolution_round: 1
14	
15	- id: "R1-N2"
16	  summary: "FPR=0% 标定仅基于单 seed"
17	  category: method
18	  severity: critical
19	  status: resolved
20	  first_raised_round: 1
21	  last_seen_round: 1
22	  resolution: "α=0.0 三 seed FPR 验证完成。"
23	  resolution_round: 1
24	
25	- id: "R1-N3"
26	  summary: "α=0.50 和 α=0.75 仅 1 seed"
27	  category: experiment
28	  severity: critical
29	  status: resolved
30	  first_raised_round: 1
31	  last_seen_round: 1
32	  resolution: "Multi-seed 补充完成。"
33	  resolution_round: 1
34	
35	- id: "R2-N1"
36	  summary: "核心方法论为计量经济学已有知识的直接迁移，新颖性有限"
37	  category: framing
38	  severity: critical
39	  status: resolved
40	  first_raised_round: 1
41	  last_seen_round: 2
42	  resolution: "Round 1 三层定位 reframe 完成。"
43	  resolution_round: 1
44	
45	- id: "R2-N2"
46	  summary: "α=0.75 multi-seed 实验未完成 + Appendix A 缺失"
47	  category: experiment
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 1
51	  last_seen_round: 1
52	  resolution: "完成。"
53	  resolution_round: 1
54	
55	- id: "R2-N3"
56	  summary: "实验规模过窄"
57	  category: experiment
58	  severity: critical
59	  status: resolved
60	  first_raised_round: 1
61	  last_seen_round: 1
62	  resolution: "跨架构验证已扩展至 15 model-seed 组合。"
63	  resolution_round: 1
64	
65	- id: "R1-W1"
66	  summary: "Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致"
67	  category: writing
68	  severity: warning
69	  status: resolved
70	  first_raised_round: 1
71	  last_seen_round: 2
72	  resolution: "核心修复完成。"
73	  resolution_round: 1
74	
75	- id: "R1-W2"
76	  summary: "PermG 缺少 power analysis"
77	  category: metho
…[truncated 31581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 1275 · 2026-05-24T22:49:55.009897+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1276 · 2026-05-24T22:49:55.160691+00:00_

1	\begin{abstract}
2	When language models train iteratively on their own output, the resulting distributional collapse is difficult to detect: the time series are short, the signal grows sub-linearly with contamination, and---as we demonstrate---the choice of statistical method can shift conclusions from universal detection to complete null.
3	We apply five lead-lag detection methods to identical iterative-training data and find that null-control false-positive rates span 7\% to 94\%, exposing method sensitivity as a primary obstacle to reliable collapse monitoring.
4	Permutation Granger causality, the lowest false-positive method, reveals a structured detectability landscape: detection jumps from absent to reliable within a narrow contamination interval, organized by a power-law boundary across three confirmed regimes.
5	Cross-architecture evaluation across five model families supports forward detection in the majority of conditions.
6	Token entropy Granger-precedes diversity collapse by at least one generation, providing a canary signal whose triggered cessation reduces peak perplexity in a proof-of-concept demonstration.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 1277 · 2026-05-24T22:49:55.161147+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1278 · 2026-05-24T22:49:55.261895+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\citep{shumailov2024curse,alemohammad2024mad}.
5	This process can be triggered by vanishingly small synthetic fractions~\citep{dohmatob2025strong}: lexical diversity narrows, calibration deteriorates, and each generation inherits the biases of its predecessors.
6	As machine-generated text grows prevalent on the web, such feedback loops pose a growing risk to production pipelines, and by the time standard quality metrics register degradation, the distribution may have already shifted irreversibly.
7	
8	This threat motivates a fundamental question: \emph{can we reliably detect the onset of model collapse?}
9	The answer is less clear than it might appear.
10	Iterative training produces short, noisy time series (often fewer than 15 points) where detection power drops sharply~\citep{boettiger2012limits}, and model collapse is a first-order transition~\citep{truong2026phase}, structurally ruling out the critical-slowing-down early-warning signals that ecologists rely on~\citep{scheffer2009early} (\S\ref{sec:related_work}).
11	More fundamentally, no prior work has systematically compared detection methods on this problem; as we show, the choice of statistical test alone can shift conclusions from universal detection to complete null on identical data.
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{figures/fig_phase_diagram.pdf}
16	\caption{Phase diagram (Pythia-410M, fp32, PermG). FDR-significant canary$\to$diversity pairs across $\alpha$ and $T$; dashed curve: fitted $\alpha_c(T) \propto T^{-\gamma}$; $\diamond$: non-monotonic anomaly; $\star$: dissolution at $T{=}25$.}
17	\label{fig:phase_diagram}
18	\end{figure}
19	
20	We systematically map this landscape on Pythia-410M~\citep{biderman2023pythia} across 13 contamination levels w
…[truncated 2463 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1279 · 2026-05-24T22:50:00.473127+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"}]

Based on the search results, here are the key submission guidelines and information for EMNLP 2026 via ARR:

## Paper Types and Scope

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## Important Deadlines

The ARR submission deadline for long and short papers is May 25, 2026, with a reviewer registration deadline for all authors on May 27, 2026. Author response and author-reviewer discussion will occur July 7-13, 2026, with meta reviews released July 30, 2026, and the 
…[truncated 772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 8277
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-24T22:50:12.401754+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1281 · 2026-05-24T22:50:12.452502+00:00_

1	\FloatBarrier
2	\section{Related Work}
3	\label{sec:related_work}
4	
5	\subsection{Model Collapse: Theory and Empirical Evidence}
6	\label{sec:rw_collapse}
7	
8	Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}; \citet{schaeffer2025position} systematize eight distinct notions of collapse---our operationalization aligns with their \emph{distributional shift} family (definitions~D4--D6).
9	Theoretical analyses sharpen these results: \citet{dohmatob2024tale} recast collapse as changed scaling-law exponents, \citet{dohmatob2025strong} proved collapse at vanishingly small synthetic fractions, and \citet{truong2026phase} prove entropy collapse is a first-order transition, structurally ruling out critical-slowing-down early-warning signals~\citep{scheffer2009early,scheffer2012anticipating}.
10	Critical mixture ratios separating qualitative outcomes have independent precedent: \citet{kazdan2025collapse} map collapse conditions, \citet{gu2024cmr} establish scaling laws for critical ratios, and \citet{gu2025datamixing} show data mixing induces phase transitions in knowledge acquisition.
11	
12	\subsection{Detection of Synthetic Data Contamination}
13	\label{sec:rw_detection}
14	
15	Monitoring metrics proposed for collapse include expected calibration error (ECE)~\citep{du2025scales}, surplexity~\citep{gambetta2024surplexity}, and machine-generated text detection~\citep{drayson2025detection}; \citet{shi2025closer} independently validate entropy as a collapse diagnostic in diffusion models.
16	\citet{boettiger2012limits} establish fundamental power limits for early-warning detection in short time series ($T{<}25$), directly relevant to iterative training where observation windows are typically $T{=}5$--$20$.
17	However, these works evaluate single metrics in isolation without cross-validating against alternative statistical tests.
18	We differ by applying five detection methods to identical data, mapping detectability acro
…[truncated 1571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1282 · 2026-05-24T22:50:12.754066+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1283 · 2026-05-24T22:50:12.754573+00:00_

1	\FloatBarrier
2	\section{Method}
3	\label{sec:method}
4	
5	\subsection{Cascade Ordering}
6	\label{sec:cascade}
7	
8	If distributional collapse follows a predictable ordering across metrics, the earliest-responding metric can serve as a canary signal.
9	We formalize known metric properties---entropy as a continuous indicator of mode concentration, diversity as a threshold indicator of lexical coverage---under mode amplification~\citep{shumailov2024curse,dohmatob2024tale} (derivations in Appendix~\ref{app:cascade_theory}).
10	
11	\begin{designprinciple}[Entropy responds before diversity]\label{thm:entropy_leads}
12	Under mode amplification: \textup{(a)} entropy can decrease while the $\epsilon$-effective support $S_\epsilon(p) {=} |\{i: p_i > \epsilon\}|$ (hence distinct-$n$) is unchanged; \textup{(b)} if distinct-$n$ decreases, entropy has already decreased.
13	\end{designprinciple}
14	
15	The asymmetry arises because entropy responds to any mass redistribution (first-order), while diversity changes only when a token probability crosses the generation threshold~$\epsilon$; the margin $\gamma = \min_{i: p_i > \epsilon}(p_i - \epsilon)$ quantifies how much shift diversity absorbs silently.
16	
17	\begin{designprinciple}[Diversity lag $\geq 1$ generation]\label{prop:div_lag}
18	If the per-generation perturbation satisfies $\alpha\|\mathcal{T}(p_t) - p_t\|_\infty < \gamma(p_t, \epsilon)$ through entropy onset $t_H$, then diversity onset $t_D \geq t_H + 1$.
19	\end{designprinciple}
20	
21	ECE co-moves with entropy at zero lag ($\Delta\mathrm{ECE} \approx \Delta C > 0$ whenever $\Delta\bar{H} < 0$; Appendix~\ref{app:cascade_theory}).
22	The predicted cascade $\{H, \mathrm{ECE}\} \to \mathrm{Distinct}$-$n$ holds in 14/15 experiments at $\alpha \geq 0.30$: entropy and ECE onset at generation~1, distinct-$n$ at generation~2 ($t_H{=}t_{\mathrm{ECE}}{=}1$, $t_D{=}2$ uniformly; \S\ref{sec:regime}; Appendix~\ref{app:moment_cascade}).
23	The assumption requires monotonic entropy
…[truncated 6212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1284 · 2026-05-24T22:50:13.056028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1285 · 2026-05-24T22:50:13.056725+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study iterative training collapse using Pythia-410M~\citep{biderman2023pythia} as the primary architecture.
8	Training data is drawn from WikiText-103~\citep{merity2017pointer} following the replace paradigm of~\citet{shumailov2024curse}: each generation fine-tunes on a mixture of $\alpha$ synthetic and $(1{-}\alpha)$ real data, generates 5{,}000 replacement samples, and fully replaces the synthetic pool (hyperparameters in Appendix~\ref{app:training_details}).
9	We run $T{=}10$ generations across 13 contamination levels ($\alpha \in \{0.00, \ldots, 1.00\}$) with multi-seed replication, yielding ${\sim}1{,}500$ statistical tests after BH-FDR correction~\citep{benjamini1995controlling}.
10	We track two \emph{canary metrics} (token entropy and ECE) and three \emph{downstream metrics}: distinct-1, distinct-2~\citep{li2016diversity}, and perplexity (distinct-3: Appendix~\ref{app:distinct3}).
11	PermG uses 5{,}000 permutations on first-differenced series~\citep{shojaie2022granger} with maximum lag~5.
12	
13	
14	\subsection{Sharp Detection Onset}
15	\label{sec:regime}
16	
17	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ even at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$.
18	Despite this ubiquitous degradation, Granger detectability is sharply regime-dependent.
19	PermG finds 0/8 canary$\to$downstream pairs FDR-significant from $\alpha{=}0.00$ through $\alpha{=}0.45$, then jumps to 6/8 (Clopper--Pearson 95\% CI $[0.25, 0.92]$) at $\alpha{=}0.50$, uniformly across all 3~fp32 seeds.
20	
21	\begin{figure}[t]
22	\centering
23	\includegraphics[width=\columnwidth]{figures/metric_trajectory.pdf}
24	\caption{Metric trajectories at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead 
…[truncated 10467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1286 · 2026-05-24T22:50:13.308002+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1287 · 2026-05-24T22:50:13.358882+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Scope and failure modes.}
4	Our Granger-precedence claim is scoped to temporal predictive improvement~\citep{granger1969investigating,shojaie2022granger}: bivariate tests cannot exclude confounders, and the FPR CI ($[2.1\%, 17.9\%]$) means Type~I error may be non-negligible.
5	Four of fifteen cross-architecture conditions do not confirm forward detection (\S\ref{sec:generalization}), each isolating a distinct PermG assumption violation: precision sensitivity (GPT-2 bf16), seed dependence (Pythia-1.4B), and entropy decoupling (SmolLM3-3B).
6	These patterns require architecture-specific null calibration before deployment (Appendix~\ref{app:extended_discussion}).
7	
8	\paragraph{Granger causality limitations.}
9	Our observation sequences ($T{=}10$--$25$) are far shorter than econometric standards ($T{\geq}100$); permutation testing avoids asymptotic assumptions but cannot recover power lost to short samples~\citep{shojaie2022granger}.
10	Bivariate tests are susceptible to omitted variable bias; first-differencing removes shared linear trends but nonlinear confounds remain possible.
11	PermG tests linear precedence only; transfer entropy (Appendix~\ref{app:transfer_entropy}) yields 0/192 significant pairs, consistent with either absent nonlinear structure or insufficient short-$T$ power.
12	Partial correlation controlling for generation number provides additional evidence: contemporaneous associations weaken after trend removal ($\bar{|r|}$: $0.590{\to}0.381$ at $\alpha{=}0.50$), while lagged correlations \emph{strengthen} ($0.759{\to}0.841$), with 35/36 pairs retaining significance (Appendix~\ref{app:partial_corr}).
13	This pattern---weakening contemporaneous but strengthening lagged structure---is consistent with genuine temporal precedence rather than shared-trend artifacts.
14	
15	\paragraph{Method complementarity.}
16	Shapley value decomposition over all $2^5{=}32$ method coalitions (Appendix~\ref{app:sha
…[truncated 957 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-24T22:50:13.560188+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1289 · 2026-05-24T22:50:13.560605+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Lead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.
5	Method choice alone inflates null-control FPR from 7.4\% to 94.4\%, and first-differencing exposes canary$\to$perplexity associations as entirely spurious, establishing that single-method analyses cannot reliably distinguish temporal precedence from artifacts.
6	
7	Our five-method comparison identifies permutation Granger causality as the recommended detector: it combines the lowest FPR (7.4\%, 9~seeds) with a steep dose-response onset from 0/8 at $\alpha{\leq}0.45$ to 6/8 at $\alpha{=}0.50$ (sigmoid $k{=}15.7$).
8	Token entropy exhibits robust one-generation-ahead precedence over diversity collapse (24/24 forward, 0/24 reverse at $\alpha{=}1.0$), replicated across GPT-2-medium and OPT-1.3B, with cross-architecture validation confirming forward detection (${\geq}6/8$) in 11/15 conditions spanning five families (345M--6.9B).
9	The blind zone below $\alpha_c$ constrains practical deployment to settings with sufficient contamination; evaluation at ${>}$7B parameters remains open.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1290 · 2026-05-24T22:50:13.761558+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1291 · 2026-05-24T22:50:13.762010+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Scope and generalizability.}
5	Our landscape characterization uses Pythia-410M as the primary architecture; the phase diagram is Pythia-family-only, frontier-scale behavior (${>}$7B) is untested, and cross-architecture evaluation is limited to $\alpha{=}1.0$.
6	All experiments use full replacement with a single decoding strategy (temperature~$1.0$, top-$k{=}50$); data accumulation~\citep{dey2024breaking} or lower temperatures would shift the landscape.
7	
8	\paragraph{Statistical power.}
9	PermG's empirical FPR is 7.4\% (CI $[2.1\%, 17.9\%]$) and $K{\geq}3$ consensus yields 11.1\% (6/54); per-condition detection rates carry wide binomial CIs (e.g., $[0.25, 0.92]$ for 6/8), so the phase diagram represents a coarse topology rather than precise probability estimates.
10	
11	\paragraph{Causal interpretation.}
12	Permutation Granger testing establishes temporal precedence, not causation; our short-sequence regime ($T{\leq}25$) limits statistical power relative to econometric standards ($T{\geq}100$), and nonlinear alternatives to the linear PermG test yield no significant results in our setting (see \S\ref{sec:discussion}).
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1292 · 2026-05-24T22:50:13.912906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1293 · 2026-05-24T22:50:14.266016+00:00_

1	\appendix
2	
3	\section{Training Details and Metric Drift}
4	\label{app:training_details}
5	\label{app:drift}
6	
7	\paragraph{Hyperparameters.}
8	Each generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).
9	Generation uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.
10	Canary metrics: token entropy $H(p_\theta | \text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.
11	Additional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.
12	
13	\paragraph{Metric drift.}
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
19	\label{tab:drift_summary}
20	\resizebox{\columnwidth}{!}{%
21	\begin{tabular}{lccccc}
22	\toprule
23	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
24	\midrule
25	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
26	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
27	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
28	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
29	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}
…[truncated 37527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-24T22:50:32.677410+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1295 · 2026-05-24T22:50:33.682577+00:00_

{"result":"# 项目 distrib_canary_collapse 概况\n\n## 实验状态 (215 个)\n\n- **gen_wiki_gpt2m_a100_s42_v3**: DONE (success) — \n- **mvp_v4_rep44**: DONE (success) — \n- **plan_006_s42**: DONE (failed) — \n- **plan_006_s42_resume**: DONE (killed) — \n- **gen_wiki_gpt2m_a100_s42_v2**: DONE (killed) — \n- **method_ablation_phase2**: DONE (success) — \n- **alpha_sweep_a025_s42_v3**: DONE (success) — \n- **method_ablation_phase1**: DONE (success) — \n- **plan_009_bootstrap_ty**: DONE (success) — \n- **mvp_v3_rep43**: DONE (failed) — \n- **mvp_v3_rep42**: DONE (failed) — \n- **mvp_v2_rep43**: DONE (killed) — \n- **mvp_v2_rep42**: DONE (killed) — \n- **mvp_rep43**: DONE (killed) — \n- **mvp_rep42**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-24\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| null_fpr_s51_fp32 | Null experiment (α=0.00) for FPR estimation: no synthetic data contamination, all detection methods should show p>0.05, contributing to narrower FPR CI with 15 seeds | — | — | — |\n\n## 待处理\n- 14b_t10_a060_s43（准备中）\n- 14b_t10_a075_s43（准备中）\n- 14b_t10_a050_s43（准备中）\n- t15_a050_s42_fp32（准备中）\n- qwen35_dryrun_launch（准备中）\n\n## 近期结论\n- **null_t15_s42_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n- **null_t15_s43_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n- **null_gpt2m_s43_fp32** (success): Cross-architecture FPR verification: GPT-2-medium null (α=0.00) should show 0% PermG detection rate, confirming method is not architecture-specific\n\n## 趋势\n成功 153 / 负向 4 / 失败 22 / 共 209\n累计 GPU: 8.4h\nrobust_pairs_K3: 0 →（近 3 次 success）\ntotal_pairs: 6 →（近 3 次 success）\n\n## 下一步\n（无活跃 idea，请通过 ideas.md 添加）\n\n## 资源状态\nwestd-19828: 空闲 cuda
…[truncated 1799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 1296 · 2026-05-24T22:50:34.687080+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distrib_canary_collapse",
  "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
  }
}
```

</details>

---


### Tool call

_source line 1297 · 2026-05-24T22:50:34.787854+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1298 · 2026-05-24T22:50:38.557440+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3870
}
```

</details>

---


### Tool result

_source line 1299 · 2026-05-24T22:50:38.557842+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3769
}
```

</details>

---


### Tool call

_source line 1300 · 2026-05-24T22:51:32.412666+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **目标会议**：EMNLP 2026（via ACL Rolling Review）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**：ACL（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n- **附录规则**：允许，审稿人不强制审查附录\n\n### 论文文件\n- LaTeX 源码：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_14/submitted.pdf`\n\n### 你的审查侧重\n\n**核心方向：方法严谨性与实验有效性**。重点审查以下方面：\n\n1. **统计方法论**：\n   - PermG（permutation Granger causality）的技术正确性——5000 次置换是否足够？first-differencing 作为前处理是否恰当？BH-FDR 在此场景下的适用性？\n   - MMCT（Multi-Method Consensus Test）的 FPR-inverse weighting 方案是否合理？K≥3 阈值选择是否有理论依据？\n   - 五种方法的比较公平性——是否存在偏向某一方法的设计选择？\n\n2. **FPR 标定**：\n   - 9 seeds × 6 pairs = 54 null-control pairs 是否足够支撑 FPR 估计？CI [2.1%, 17.9%] 的宽度是否影响核心结论？\n   - GPT-2 null FPR 50% 对跨架构声明的影响\n   - 论文声称 PermG FPR 7.4% 但这超出 nominal 5%——是否充分讨论？\n\n3. **检测边界模型**：\n   - 幂律拟合 α_c(T) ∝ T^{-γ}，γ ∈ [0.64, 2.08]——CI 跨越亚线性/超线性分界，模型是否有区分度？\n   - β MLE vs CV 分歧——拟合是否稳定？\n   - α=0.60 非单调异常排除后，仅 3-4 个有效 α 值支撑边界拟合——是否充分？\n\n4. **功效分析**：\n   - 每条件仅 3 seeds，每 α 值 8 pairs——binomial CI 极宽（如 6/8 → [0.25, 0.92]）\n   - 这些宽 CI 对 phase diagram 的定量解读意味着什么？\n\n5. **实验设计**：\n   - 跨架构验证仅在 α=1.0（最极端条件）——phase diagram 核心区 α∈[0.45,0.75] 完全无跨架构数据\n   - Intervention 实验：N=2 seeds, α=1.0, post-hoc 15% threshold——证据强度如何？\n   - 单一解码策略（temperature 1.0, top-k 50）的外部效度\n\n6. **Granger 因果性局限**：\n   - 偏相关分析（控制 generation number）是否充分？\n   - Bivariate 限制——论文是否充分讨论？\n   - Short T (≤25) 下 Granger 检验的可靠性\n\n请按 ARR 标准格式输出审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\nWeaknesses 按严重程度分级：\n- **[Must-Fix]**：不解决则不能接收\n- **[Should-Fix]**：应该修改但非致命\n- **[Minor]**：可选修改"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1（方法严谨性 + 实验有效性）\n\n### Venue 信息\n- **目标会议**：EMNLP 2026（via ACL Rolling Review）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**：ACL（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n- **附录规则**：允许，审稿人不强制审查附录\n\n### 论文文件\n- LaTeX 源码：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_14/submitted.pdf`\n\n### 你的审查侧重\n\n**核心方向：方法严谨性与实验有效性**。重点审查以下方面：\n\n1. **统计方法论**：\n   - PermG（permutation Granger causality）的技术正确性——5000 次置换是否足够？first-differencing 作为前处理是否恰当？BH-FDR 在此场景下的适用性？\n   - MMCT（Multi-Method Consensus Test）的 FPR-inverse weighting 方案是否合理？K≥3 阈值选择是否有理论依据？\n   - 五种方法的比较公平性——是否存在偏向某一方法的设计选择？\n\n2. **FPR 标定**：\n   - 9 seeds × 6 pairs = 54 null-control pairs 是否足够支撑 FPR 估计？CI [2.1%, 17.9%] 的宽度是否影响核心结论？\n   - GPT-2 null FPR 50% 对跨架构声明的影响\n   - 论文声称 PermG FPR 7.4% 但这超出 nominal 5%——是否充分讨论？\n\n3. **检测边界模型**：\n   - 幂律拟合 α_c(T) ∝ T^{-γ}，γ ∈ [0.64, 2.08]——CI 跨越亚线性/超线性分界，模型是否有区分度？\n   - β MLE vs CV 分歧——拟合是否稳定？\n   - α=0.60 非单调异常排除后，仅 3-4 个有效 α 值支撑边界拟合——是否充分？\n\n4. **功效分析**：\n   - 每条件仅 3 seeds，每 α 值 8 pairs——binomial CI 极宽（如 6/8 → [0.25, 0.92]）\n   - 这些宽 CI 对 phase diagram 的定量解读意味着什么？\n\n5. **实验设计**：\n   - 跨架构验证仅在 α=1.0（最极端条件）——phase diagram 核心区 α∈[0.45,0.75] 完全无跨架构数据\n   - Intervention 实验：N=2 seeds, α=1.0, post-hoc 15% threshold——证据强度如何？\n   - 单一解码策略（temperature 1.0, top-k 50）的外部效度\n\n6. **Granger 因果性局限**：\n   - 偏相关分析（控制 generation number）是否充分？\n   - Bivariate 限制——论文是否充分讨论？\n   - Short T (≤25) 下 Granger 检验的可靠性\n\n请按 ARR 标准格式输出审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含评分和置信度）。\n\nWeaknesses 按严重程度分级：\n- **[Must-Fix]**：不解决则不能接收\n- **[Should-Fix]**：应该修改但非致命\n- **[Minor]**：可选修改"
  }
}
```

</details>

---


### Tool result

_source line 1301 · 2026-05-24T22:51:56.870728+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24458
}
```

</details>

---


### Tool call

_source line 1302 · 2026-05-24T22:51:57.876137+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标会议**：EMNLP 2026（via ACL Rolling Review）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**：ACL（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n- **附录规则**：允许，审稿人不强制审查附录\n- **EMNLP 评分标准**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n### 论文文件\n- LaTeX 源码：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_14/submitted.pdf`\n\n### 你的审查侧重\n\n**核心方向：新颖性、完整性、写作质量与格式合规**。重点审查以下方面：\n\n1. **新颖性评估**：\n   - 核心方法（Granger causality, specification curve analysis）是计量经济学标准技术——在 NLP/ML 领域的移植是否构成足够的 novelty？\n   - \"method sensitivity\" 作为 primary finding——这是否是一个有意义的 empirical contribution？\n   - Design Principles（cascade ordering）——数学深度是否与 contribution 声明匹配？\n\n2. **贡献声明 vs 证据强度**：\n   - 标题 \"Characterizing the Detectability Landscape\" vs 实际覆盖范围（主要是 Pythia-410M + WikiText-103）\n   - Abstract 中的具体声明逐条检查——每条声明是否有充分的数据支撑？\n   - \"Cross-architecture evaluation across five model families\" vs 实际仅在 α=1.0 进行\n   - Intervention \"substantially reduces peak perplexity\"——证据强度是否支持 \"substantially\"？\n   - \"five families (345M-6.9B)\" 给读者的印象 vs 实际实验规模\n\n3. **Related Work 覆盖**：\n   - 是否有遗漏的关键 related work？特别关注：\n     - 早期预警信号文献（Dakos et al. 2008/2012, Lenton et al. 2008）\n     - Granger causality 标准局限性讨论（observational equivalence, Lucas critique）\n     - 近期 model collapse 检测方法\n   - 与已有工作的区分是否清晰？Table 在 appendix 中的 comparison table 是否公平？\n\n4. **写作质量**：\n   - 信息密度是否过高？关键 findings 是否被数字洪流淹没？\n   - 技术术语使用是否一致？（如 Granger \"precedence\" vs \"causality\"）\n   - β 符号是否重用（统计功率 vs 幂律指数）？\n   - Abstract 是否 ≤200 words（EMNLP 硬约束）？\n   - 叙事流畅性——读者是否能跟上论证逻辑？\n\n5. **格式合规**：\n   - 正文是否 ≤8 页？\n   - 主文中是否有至少一个核心结果 summary table？（关注 table 分布）\n   - Figure/Table 分布是否合理？（有无连续纯文本页面？）\n   - Limitations section 是否存在且位置正确（正文内，非 appendix）？\n   - AI Writing Disclosure 是否存在？\n   - ACL 模板使用是否正确？\n\n6. **引用完整性**：\n   - bib 条目是否有明显错误（作者不匹配、标题不匹配）？\n   - 引用格式是否统一？\n   - 是否有 bib 中存在但正文未引用的条目？\n\n请按 ARR 标准格式输出审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含 EMNLP 评分和置信度）。\n\nWeaknesses 按严重程度分级：\n- **[Must-Fix]**：不解决则不能接收\n- **[Should-Fix]**：应该修改但非致命\n- **[Minor]**：可选修改"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2（新颖性 + 完整性 + 写作质量）\n\n### Venue 信息\n- **目标会议**：EMNLP 2026（via ACL Rolling Review）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations 不计入页数\n- **模板**：ACL（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n- **附录规则**：允许，审稿人不强制审查附录\n- **EMNLP 评分标准**：5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle\n\n### 论文文件\n- LaTeX 源码：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex`\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_14/submitted.pdf`\n\n### 你的审查侧重\n\n**核心方向：新颖性、完整性、写作质量与格式合规**。重点审查以下方面：\n\n1. **新颖性评估**：\n   - 核心方法（Granger causality, specification curve analysis）是计量经济学标准技术——在 NLP/ML 领域的移植是否构成足够的 novelty？\n   - \"method sensitivity\" 作为 primary finding——这是否是一个有意义的 empirical contribution？\n   - Design Principles（cascade ordering）——数学深度是否与 contribution 声明匹配？\n\n2. **贡献声明 vs 证据强度**：\n   - 标题 \"Characterizing the Detectability Landscape\" vs 实际覆盖范围（主要是 Pythia-410M + WikiText-103）\n   - Abstract 中的具体声明逐条检查——每条声明是否有充分的数据支撑？\n   - \"Cross-architecture evaluation across five model families\" vs 实际仅在 α=1.0 进行\n   - Intervention \"substantially reduces peak perplexity\"——证据强度是否支持 \"substantially\"？\n   - \"five families (345M-6.9B)\" 给读者的印象 vs 实际实验规模\n\n3. **Related Work 覆盖**：\n   - 是否有遗漏的关键 related work？特别关注：\n     - 早期预警信号文献（Dakos et al. 2008/2012, Lenton et al. 2008）\n     - Granger causality 标准局限性讨论（observational equivalence, Lucas critique）\n     - 近期 model collapse 检测方法\n   - 与已有工作的区分是否清晰？Table 在 appendix 中的 comparison table 是否公平？\n\n4. **写作质量**：\n   - 信息密度是否过高？关键 findings 是否被数字洪流淹没？\n   - 技术术语使用是否一致？（如 Granger \"precedence\" vs \"causality\"）\n   - β 符号是否重用（统计功率 vs 幂律指数）？\n   - Abstract 是否 ≤200 words（EMNLP 硬约束）？\n   - 叙事流畅性——读者是否能跟上论证逻辑？\n\n5. **格式合规**：\n   - 正文是否 ≤8 页？\n   - 主文中是否有至少一个核心结果 summary table？（关注 table 分布）\n   - Figure/Table 分布是否合理？（有无连续纯文本页面？）\n   - Limitations section 是否存在且位置正确（正文内，非 appendix）？\n   - AI Writing Disclosure 是否存在？\n   - ACL 模板使用是否正确？\n\n6. **引用完整性**：\n   - bib 条目是否有明显错误（作者不匹配、标题不匹配）？\n   - 引用格式是否统一？\n   - 是否有 bib 中存在但正文未引用的条目？\n\n请按 ARR 标准格式输出审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References → Overall Assessment（含 EMNLP 评分和置信度）。\n\nWeaknesses 按严重程度分级：\n- **[Must-Fix]**：不解决则不能接收\n- **[Should-Fix]**：应该修改但非致命\n- **[Minor]**：可选修改"
  }
}
```

</details>

---


### Tool result

_source line 1303 · 2026-05-24T22:51:59.237321+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1361
}
```

</details>

---


### Assistant

_source line 1304 · 2026-05-24T22:52:05.363071+00:00_

两位 Reviewer 已启动，视觉审查已并行派发。等待审稿结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 123

## Round 123

2 recorded events


### User

_source line 1305 · 2026-05-24T22:58:07.819595+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：Characterizing the Detectability Landscape of Iterative Model Collapse

## Summary

本文研究迭代训练语言模型中分布坍缩（model collapse）何时可被统计检测到。作者提出以 canary metrics（token entropy、ECE）作为早期指标，应用五种时间序列检测方法（NaiveXCorr、DiffXCorr、Threshold Onset、PermG、Toda-Yamamoto），并设计 Multi-Method Consensus Test（MMCT）来刻画"检测边界"——在 contamination fraction α 与观测窗口 T 的二维空间中。核心发现：检测在 α≈0.45 以下完全缺失，在约 2 个百分点的窄区间内从 0/8 跳至 6/8 显著对，呈现尖锐相变。幂律模型 α_c(T) ∝ T^{−γ} 刻画该边界。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 2.5/5 | 核心定量声明（精确边界位置、跨架构普适性、幂律函数形式）的统计支撑不足：样本量过小导致置信区间极宽，FPR 标定不够精确，跨架构验证仅限于最极端条件 |
| **Excitement** | 3.5/5 | 研究问题新颖且及时——从"collapse 是否发生"转向"collapse 何时可检测"是有意义的范式转换；cascade ordering 框架和 phase diagram 概念有启发性 |
| **Overall Assessment** | 3/5 (Findings) | 框架思路有价值，但实验规模不足以支撑多个核心声明的精度要求。适合 Findings 但需要显著加强实验才能进入主会议 |
| **Confidence** | 4/5 | 仔细检查了统计方法论和实验设计的技术细节 |
| **Reproducibility** | 3/5 | 方法描述较完整（Algorithm 1、附录有伪代码），但未提供代码/数据；超参数选择的依据不够透明 |

---

## Must-Fix 问题（影响接收决定）

### N1 [critical] 统计功效严重不足，定量声明缺乏可信支撑

- **具体位置**：Section 4.1（实验设置）、Section 4.2-4.4（所有定量结论）、Table 2、Figure 3
- **问题**：
  - 每个条件仅 **3 seeds**，每个 α 值仅 **8 pairs**。对于二值检测结果（显著/不显著），binomial CI 极宽：6/8 → 95% CI [0.25, 0.92]，意味着真实检测率可能低至 25%。
  - Phase diagram（Figure 3）被呈现为精确的检测边界面，但每个网格点背后仅有 3-8 个观测值，CI 几乎覆盖整个 [0,1] 区间。论文称"sharp onset"（Section 4.2），但数据无法区分 sharp transition 和 gradual transition——两者在如此小的样本下产生的观测模式不可区分。
  - Table 2 中 MMCT K≥3 的 TPR 在 α=0.50 为 85.4%、α=0.75 为 72.9%——但这些数字的 CI 因样本量小而极宽，定量解读无意义。
- **为什么影响接收**：论文的核心贡献是定量刻画检测边界，但当前样本量不支持任何精确的定量声明。phase diagram 更接近 coarse qualitative sketch 而非精确 landscape。
- **建议修改方向**：(1) 增加 seeds 至少至 10-15 per condition 以获得有意义的 CI；(2) 或大幅降低定量声明的精度——将 phase diagram 明确标注为定性趋势图，避免使用"sharp"、precise boundary 等暗示高精度的措辞；(3) 在正文（非仅 limitations）讨论 CI 宽度对结论的实质影响。

### N2 [critical] 跨架构验证仅在 α=1.0（最极端条件），核心区域无数据

- **具体位置**：Section 4.5（Cross-Architecture Validation）、Table 17（Appendix Z.1）、Abstract
- **问题**：
  - 跨架构验证**仅在 α=1.0**（100% 合成数据替换）进行，这是最极端的条件。Phase diagram 的核心贡献在于 α∈[0.45, 0.75] 的过渡区域，但该区域**完全没有**跨架构数据。
  - Abstract 声称"Cross-architecture evaluation across five model families supports forward detection in the majority of conditions"——casual reader 会理解为跨架构验证覆盖多个 α 值，但实际仅有一个 α 值。这构成 overclaim。
  - 更严重的是，GPT-2 medium 的 null FPR 高达 **50%**（6/12，2 seeds；Appendix Z.2），意味着在 GPT-2 上任何检测结果都可能是 false positive。论文在 Section 5 提到这一点但轻描淡写（"require architecture-specific null calibration"），实际上这直接否定了 GPT-2 上检测的有效性。
- **为什么影响接收**：跨架构泛化是论文的重要卖点之一，但证据仅限于最极端条件且部分架构的 null calibration 失败。这使得 phase diagram 实质上是 Pythia-410M 特定的结果。
- **建议修改方向**：(1) 至少在 α=0.50 和 α=0.75 补充 2-3 个架构的实验；(2) 将 abstract 中的 cross-architecture claim 限定为"at full replacement (α=1.0)"；(3) 明确承认 GPT-2 null FPR 50% 意味着该架构上的检测不可信，而非仅说"需要 architecture-specific calibration"。

### N3 [critical] PermG FPR 超出 nominal 5% 且 CI 极宽，FPR 标定不充分

- **具体位置**：Section 3.3（Method Sensitivity Analysis）、Section 4.1、Table 13（Appendix R）、Limitations
- **问题**：
  - PermG 的经验 FPR 为 **4/54 = 7.4%**，已超出 nominal 5%。95% CI **[2.1%, 17.9%]** 意味着真实 FPR 可能接近 18%，远超可接受水平。
  - 54 个 null-control pairs（9 seeds × 6 pairs）用于 FPR 估计。按 binomial 计算，要将 FPR 的 95% CI 宽度控制在 ±5% 以内，至少需要约 400 个 null pairs。当前 54 pairs 的 CI 宽度约 ±8%，估计精度极低。
  - MMCT K≥3 的 FPR 为 **11.1%**（Table 2），超出 nominal 5% 的两倍多。论文将 K=3 描述为"balances FPR control"，但 11.1% 的 FPR 在统计检验标准下是不可接受的。
  - Limitations 提到 CI [2.1%, 17.9%] 但仅说"phase diagram represents a coarse topology rather than precise probability estimates"——这个表述不够准确，问题不仅是精度，而是 FPR 可能本身就超标。
- **为什么影响接收**：如果真实 FPR 接近 18%，Figure 3 phase diagram 中的许多"检测成功"可能是 false positive，检测边界的位置将大幅右移。整个定量框架的可信度依赖于 FPR 的可靠控制。
- **建议修改方向**：(1) 大幅增加 null-control seeds（至少 20+ seeds）以获得更精确的 FPR 估计；(2) 在正文中明确报告 PermG FPR 超出 nominal 5% 的事实及其对结论的影响；(3) 考虑采用更保守的 α level（如 0.025）来补偿 FPR inflation。

### N4 [critical] 幂律边界模型缺乏区分度——仅 3-4 个有效数据点，γ CI 跨越不同标度域

- **具体位置**：Section 3.4（Detection Boundary）、Equation (1)-(2)、Section 4.4（Detection Boundary Left-Shift）
- **问题**：
  - 幂律拟合 α_c(T) = A · T^{−γ} 的 γ 的 95% CI 为 **[0.64, 2.08]**（Section 3.4）。γ<1 对应亚线性衰减（边界缓慢移动），γ>1 对应超线性衰减（边界快速移动），γ=1 对应线性。CI 完全跨越三种 qualitatively different 行为，该模型对边界的功能形式**没有区分度**。
  - 排除 α=0.60 的非单调异常后（Section 4.3 提到该点的 non-monotonic dip），仅剩 **3-4 个有效 α 值**支撑拟合。用 3-4 个点拟合 2 参数幂律（A 和 γ），自由度极低（1-2），任何函数形式都能拟合。
  - Section 4.4 称"Profile likelihood yields γ ∈ [0.64, 2.08]"，但 profile likelihood 在如此少的数据点上也不能提供有意义的推断。
  - β MLE vs CV 分歧（Appendix S 提到 sigmoid transition shape）进一步表明拟合不稳定。
- **为什么影响接收**：Equation (1) 和 phase diagram 的幂律边界是论文的标志性结果之一。如果该模型无法区分不同的 scaling behavior，其理论价值大幅降低。
- **建议修改方向**：(1) 增加更多 T 值（当前仅 T=10,15,25？）和 α 值的实验以增加拟合数据点；(2) 对比不同函数形式（线性、对数、指数）的拟合质量，说明幂律不是唯一合理选择；(3) 如果数据不足以区分函数形式，降级为定性声明（"detection improves with longer T"），不再强调特定的幂律公式。

---

## Should-Fix 问题（影响评分但不一票否决）

### W1 [warning] Intervention 实验证据极弱——N=2, α=1.0, post-hoc threshold

- **具体位置**：Section 4.6（Canary-Based Intervention）、Figure 9
- **问题**：
  - 仅 **N=2 seeds**，仅 **α=1.0**（最极端条件），15% threshold 是 **post-hoc** 选择。
  - 论文称"reduces peak perplexity by 64%"，但 N=2 完全不支持任何统计推断。这是 anecdotal evidence，不是 proof of concept。
  - 论文称 threshold 在 [10%, 22%] 范围内 robust，但该 robustness band 也是从同样的 2 seeds 得出的。
- **建议**：(1) 至少增加至 5+ seeds；(2) 探索 α<1.0 的 intervention 效果；(3) 使用 pre-registered threshold 或 cross-validated threshold；(4) 或将该部分大幅缩减，明确标注为 "preliminary illustration" 而非 "proof of concept"。

### W2 [warning] MMCT 的 FPR-inverse weighting 依赖于噪声极大的经验 FPR 估计

- **具体位置**：Algorithm 1（Section 3.3）、Appendix Q（Weight Robustness Ablation）
- **问题**：
  - FPR-inverse weighting 使用 w_k = 1/max(FPR_k, 0.01) 计算权重，其中 FPR_k 来自仅 54 个 null pairs 的经验估计。
  - NaiveXCorr FPR=94.4% → weight≈1.06；PermG FPR=7.4% → weight≈13.5。但 PermG 的 FPR 95% CI 为 [2.1%, 17.9%]，如果真实 FPR=2.1%，权重将变为 47.6；如果真实 FPR=17.9%，权重将变为 5.6。权重的 uncertainty propagation 完全未讨论。
  - Appendix Q 的 ablation（equal, cap-5, cap-10, FPR-inverse cap-100）显示结果对 weighting 方案 somewhat robust，但仍未解决权重本身的 estimation uncertainty。
- **建议**：讨论权重估计的 bootstrap CI，或展示在 FPR 估计的 CI 边界处 MMCT 结论的稳定性。

### W3 [warning] Granger 因果性的根本局限讨论不充分

- **具体位置**：Section 3.2（Design Considerations）、Section 5（Discussion）、Appendix F（Transfer Entropy）
- **问题**：
  - Appendix F 报告 transfer entropy 检验在 **0/192 pairs** 中显著。论文解释为"consistent with either absent nonlinear structure or insufficient short-T power"。但另一种解释是：PermG 检测到的"temporal precedence"本身可能主要由 shared monotonic trend（generation number）驱动，而非 genuine causal structure。
  - 论文在 Section 5 报告了 partial correlation controlling for generation number 的结果：|r|=0.509→0.381 at α=0.50（lagged correlations 从 0.739→0.841 at α=0.50 增强）。但这些数字方向相反——trend removal 削弱了 contemporaneous association 但增强了 lagged correlation？这需要更清楚的解释。
  - Bivariate Granger 不能排除 confounders。论文承认这点（"bivariate tests cannot exclude confounders"，Section 3.2），但未讨论具体哪些 confounders 可能影响结论（如 learning rate schedule effects, tokenizer artifacts 等）。
  - Short T (≤25) 下 Granger 检验的 power 很低（Appendix N 讨论了这一点），first-differencing 进一步将有效样本量减至 T-1≤24。
- **建议**：(1) 更清楚地讨论 generation-number trend 作为 confounder 的可能性；(2) 解释 partial correlation 结果中 contemporaneous vs lagged 方向相反的原因；(3) 考虑 multivariate Granger 或 conditional independence testing。

### W4 [warning] 单一解码策略限制外部效度

- **具体位置**：Section 4.1（Experimental Setup）、Limitations
- **问题**：
  - 所有实验使用 **temperature 1.0, top-k 50** 的单一解码策略。
  - Limitations 提到"lower temperatures would shift the landscape"，但未提供任何证据或定性分析。
  - Temperature 和 top-k/top-p 的选择直接影响生成文本的多样性，进而影响 canary metrics（token entropy, distinct-n）的分布。Phase diagram 的位置可能在不同解码策略下大幅移动。
  - 实际应用中，不同场景使用不同的解码策略，这严重限制了结论的 practical applicability。
- **建议**：至少补充 1-2 个不同温度（如 0.7, 1.5）的实验点，验证 phase transition 的存在性在解码策略变化下是否 robust。

### W5 [warning] Table 2 显示 MMCT 对 K 阈值极度敏感

- **具体位置**：Table 2（Section 4.5 area on page 8）
- **问题**：
  - K=2: FPR 38.9%（不可接受）
  - K=3: FPR 11.1%（仍超标，但有一定检测力）
  - K=4: FPR 0%，TPR 也降至 ≤25%（几乎无检测力）
  - K=5: 全部为 0%
  - 方法**仅在 K=3 这一个阈值**上勉强可用，且 FPR 仍超出 nominal。这意味着 MMCT 不是 robust method，而是在特定阈值下的 fragile operating point。
  - K≥3 的理论依据不充分——论文未提供为什么 majority vote 是最优选择的分析。
- **建议**：(1) 讨论 K=3 的理论依据（如 voting theory, redundancy arguments）；(2) 报告 K 的连续版本（如 weighted consensus score 的 ROC 曲线），避免硬阈值；(3) 承认 MMCT 的操作区间极窄。

---

## 小问题（不影响接收）

- **M1**: BH-FDR 的 PRDS（positive regression dependency on a subset）假设未讨论。由于不同 pairs 共享相同的 seeds 和生成过程，test statistics 之间可能存在相关性，BH-FDR 的 validity 需要论证（Section 3.3）。
- **M2**: Equation (2) 中 γ = 1/(2ℓ) 的推导依赖于 sub-linear signal model S(α) = cα^ℓ (ℓ<1)。但 ℓ 的取值范围和 empirical 验证未在正文中呈现（仅在 Appendix X？）。
- **M3**: Figure 2 的 y 轴 label "Significant pairs (%)" 和 bar heights 难以精确读取（bar 顶部数字较小），建议增大字体或改用 table 呈现精确数值。
- **M4**: Abstract 第一句"When language models train iteratively on their own output, the resulting distributional collapse is difficult to detect"——这个 framing 预设了 collapse 总是存在的，但在低 α 值下可能根本不发生 meaningful collapse，此时"difficult to detect"与"nothing to detect"无法区分。
- **M5**: Limitations 提到"frontier-scale behavior (>7B) is untested"——考虑到 Pythia-410M 是一个相对小的模型，这一局限的影响可能比论文暗示的更大。

---

## 主要优势

- **S1**: 研究问题的切入角度新颖——从"model collapse exists"到"when is it detectable"是有价值的范式转换，具有实际意义（监控/预防部署中的退化）。
- **S2**: Multi-method framework 和 consensus mechanism 的设计思路合理——单一方法的 FPR 问题通过多方法共识来缓解，虽然执行上有问题但思路正确。
- **S3**: Cascade ordering 的理论框架（Design Principles 1-2）和 formal derivations（Appendix X）提供了有用的理论基础，entropy→diversity→perplexity 的排序有直觉和理论支撑。
- **S4**: 附录的 robustness checks 广泛（permutation count stability、spec curve analysis、weight ablation 等），显示作者对方法论问题有认识。
- **S5**: Null-control calibration 的设计（相同 pipeline、identical data、仅 seed 不同）是合理的实验对照思路。
- **S6**: Spec curve analysis（Appendix E, Figure 6, Table 6）across 1,160 specifications 是方法论上的加分项，增强了 blind→onset 跳跃的 robustness。

---

## Questions for Authors

1. 如果将 null-control seeds 增加到 20+，PermG 的 FPR 估计会如何变化？作者是否有 pilot data 可以预估？
2. 排除 α=0.60 non-monotonic anomaly 的理由是什么？如果保留该点，幂律拟合的结果如何变化？该异常是否在不同 seeds 之间一致出现？
3. Appendix F 的 partial correlation 结果中，trend removal 削弱 contemporaneous association 但增强 lagged correlation——作者能否解释这一看似矛盾的模式？
4. 在 GPT-2 null FPR 50% 的情况下，Table 17 中 GPT-2 的检测结果是否有任何统计意义？
5. 为什么 intervention 实验限于 N=2 seeds？这是计算资源限制还是设计选择？

---

## Missing References

- Dohmatob et al. (2024) "Model collapse demystified" — 提供了 collapse 的 scaling law 分析，论文引用了但未与本文的幂律边界做对比。
- Shumailov et al. (2024) 的更新版本可能包含更多关于检测/缓解的讨论。
- 建议引用 specification curve analysis 的原始方法论文献（Simonsohn et al., 2020 已引用，确认）。

---

## Overall Assessment

**Overall**: 3/5 — Findings

**一句话总结**：研究问题有价值、框架设计有思路，但统计功效严重不足——3 seeds/condition、54 null pairs、仅 α=1.0 的跨架构验证——使得核心定量声明（精确检测边界、幂律 scaling、跨架构泛化）的可信度远低于论文所暗示的水平。

框架本身（cascade ordering + multi-method consensus + phase diagram 概念）对 model collapse 监控的实践有启发意义，值得发表。但当前的实验规模将论文从"rigorous characterization"降级为"preliminary exploration with an interesting framework"。如果作者能增加样本量并缩窄关键声明的范围，这篇论文有进入主会议的潜力。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1306 · 2026-05-24T22:58:22.096342+00:00_

Reviewer 1 报告已收到。评分 3/5（Findings）。4 个 Must-Fix（统计功效不足、跨架构仅 α=1.0、FPR 超标、幂律模型无区分度）+ 5 个 Should-Fix。等待 Reviewer 2 报告后进入交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 124

## Round 124

2 recorded events


### User

_source line 1307 · 2026-05-24T22:58:24.563347+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**审稿完成摘要**：

- **Overall: 3/5 (Findings)**
- 识别了 **4 个 Must-Fix 问题**：(1) 统计功效严重不足（3 seeds/condition, binomial CI 极宽）；(2) 跨架构验证仅限 α=1.0 且 GPT-2 null FPR 50%；(3) PermG FPR 7.4% 超出 nominal 5%，CI [2.1%, 17.9%] 极宽；(4) 幂律边界仅 3-4 个有效数据点，γ CI 跨越不同标度域无区分度
- 识别了 **5 个 Should-Fix 问题**：intervention 实验 N=2、MMCT 权重 uncertainty、Granger 因果局限、单一解码策略、K 阈值敏感性
- **优势**：研究问题切入角度新颖，multi-method 框架思路正确，附录 robustness checks 广泛

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1308 · 2026-05-24T22:58:29.082805+00:00_

收到 Reviewer 1 的报告。等待 Reviewer 2 完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 125

## Round 125

6 recorded events


### User

_source line 1309 · 2026-05-24T23:03:02.151646+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿报告

### Paper Summary

本文研究迭代模型坍缩（iterative model collapse）的可检测性问题。作者将五种 lead-lag 统计检测方法（naive cross-correlation, differenced cross-correlation, threshold onset, permutation Granger causality, Toda-Yamamoto）应用于相同的迭代训练数据，发现方法选择本身就能使 null-control FPR 从 7% 变到 94%（κ=0.185）。以 PermG（FPR 最低的方法）为主检测器，作者绘制了一张 phase diagram：检测在 α≤0.45 完全缺失，在 α≈0.50 突然跳至 6/8，跨越一个 power-law 边界组织的三个区域。在 α=1.0 下对五个模型家族（345M–6.9B）进行跨架构验证，11/15 条件确认正向检测。Token entropy 以至少一代的提前量 Granger-precede diversity collapse（24/24 forward, 0/24 reverse），并通过 proof-of-concept intervention 将峰值 perplexity 降低 64%。

---

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法选择合理（置换检验避免短序列渐近假设、BH-FDR 校正、null-control 校准），但实验范围主要限于 Pythia-410M + WikiText-103，α=0.60 异常未得到解释性解决，Design Principles 有已知反例 |
| Excitement | 2.5/5 | 方法敏感性发现（FPR 7%→94%）有实际价值，但核心方法全部借自计量经济学/统计学（Granger causality 1969, specification curve 2020），blind zone（α<0.50）限制实际部署场景 |
| Reproducibility | 4/5 | 实验设置详尽（Appendix A），统计细节充分（5,000 permutations, BH-FDR q=0.05, 9 seeds），附录覆盖 24 个鲁棒性分析，AI 使用透明声明 |
| Overall Assessment | 3.0/5 | Findings 水平。扎实的实证工作，方法敏感性发现对社区有价值，但 scope 过窄（单架构 phase diagram）、novelty 有限（方法论迁移而非创新），不足以支撑 Conference 接收 |
| Confidence | 4/5 | 熟悉 Granger 因果检验、specification curve 方法论和 model collapse 文献 |

---

### 主要优势

**S1. 方法敏感性发现具有方法论意义（§3.3, Figure 2）**
五种方法在完全相同的数据上产生 FPR 从 7% 到 94% 的结果——这不仅对 model collapse 领域重要，对任何使用统计检测方法的 NLP 实证工作都有警示意义。Specification curve analysis（1,160 configurations, Figure 6）有力地强化了这一发现。

**S2. 诚实的失败报告**
论文透明报告了四个跨架构失败条件（GPT-2 bf16 精度敏感性、GPT-2 s43 双向混淆、Pythia-1.4B seed 依赖、SmolLM3-3B entropy 解耦），α=0.60 非单调异常，以及 Design Principle 1 的反例。这种知识诚实性在实证论文中值得肯定。

**S3. 统计方法论严谨（§3.2–3.3）**
针对短时序（T=10–25）的特殊挑战，选择置换检验而非渐近方法；first-differencing 分析成功分离了虚假的 canary→perplexity 关联和真实的 canary→diversity 关联（24/24→24/24 vs F≈0, p=0.99），这是一个令人信服的方法论验证。

**S4. 因果声明的审慎范围界定**
论文始终区分 "Granger precedence"（temporal predictive improvement）和 mechanistic causation，在 §3.2、§5、Limitations 中多次重申。这是对 Granger 方法的正确理解和使用。

**S5. 问题的时效性和实际相关性**
随着 AI 生成内容在 web 上的增长，model collapse 检测是一个日益重要的问题。系统性比较检测方法的工作在该领域尚属空白。

---

### Must-Fix 问题（影响接收决定）

**N1** [critical] **标题和核心声明的 scope 与实际证据不匹配**
- 具体位置：Title, Abstract, §1 contributions, §6 Conclusion
- 问题：标题 "Characterizing the Detectability Landscape of Iterative Model Collapse" 暗示了对检测性的全面刻画，但 detectability landscape（phase diagram）实质上仅在 **一个架构**（Pythia-410M）、**一个数据集**（WikiText-103）、**一个时间长度**（T=10）上绘制。Cross-architecture validation（§4.5）仅在 α=1.0（全合成替换，即最容易检测的场景）进行。Phase diagram 最有趣的区域——blind→onset 转换（α≈0.50 附近）——在其他架构上完全没有数据。
- 对照 ARR R2 准则："a few QA benchmarks ≠ 'reasoning'" — 类比地，单架构 phase diagram ≠ "the detectability landscape"。
- 为什么影响接收：这是论文最核心的 contribution claim（Contribution 2），如果 scope 与 claim 不匹配，整篇论文的 framing 就不成立。
- 建议修改方向：（a）缩窄标题以反映实际范围（如 "Detection Method Sensitivity and Phase Transitions in Iterative Model Collapse"）；或（b）在至少一个额外架构上验证 α≈0.50 边界（即使只是 GPT-2-medium 的 3-4 个 α 值）。

**N2** [critical] **"Five families (345M–6.9B)" 给读者造成误导性的广度印象**
- 具体位置：Abstract 第5句, §1 Contribution 3 之后的段落, §4.5 首段, §6 Conclusion 第3句
- 问题：Abstract 说 "Cross-architecture evaluation across five model families supports forward detection in the majority of conditions." 这句话技术上正确，但给人的印象是整个 detectability landscape 在五个家族上都得到了验证。实际上：
  - 只有 α=1.0（最大污染）一个点在五个家族上验证
  - 11/15 的"多数条件"意味着 27% 失败率——这在统计检测中并不小
  - "345M–6.9B" 范围暗示了 scale robustness，但 detection boundary α_c≈0.50、cascade ordering、α=0.60 anomaly 在 6.9B scale 上是否成立完全未知
  - Pythia-1.4B 的 scale consistency 描述（§4.5 "Scale consistency" 段）仅是定性观察
- 为什么影响接收：误导性 framing 会导致读者对结果的 generalizability 产生错误预期，这在实证论文中是严重问题。
- 建议修改方向：在 Abstract 和 Conclusion 中明确加上 "at α=1.0 (full replacement)"；在 Contribution 列表中不将 cross-architecture 等同于 landscape characterization。

---

### Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **α=0.60 非单调异常破坏了 phase diagram 的叙事连贯性**
- 具体位置：§4.3 第3段, §5 "The α=0.60 non-monotonic anomaly" 段
- 问题：论文的核心 narrative 是三区域 phase diagram（blind/onset/detection）。但在 α=0.60，所有方向性方法都失败（PermG 0/8, threshold 0/8, Toda-Yamamoto 1/8），只有双向 DiffXCorr 保持检测（6/8）。这意味着 "detection" 区域正中间有一个洞。
- 解释 "temporal lag compression defeats directional separation" 是 post-hoc 的：为什么偏偏在 α=0.60 lag 压缩，而非 α=0.50 或 α=0.75？
- 异常在 T=25 消解，但若框架在主要设置（T=10）下存在系统性 gap，实际可用性存疑。
- 建议：将 phase diagram 明确描述为四区域（blind/onset/sync-dip/detection）而非将 sync-dip 作为异常处理；或提供对 lag compression 在 α=0.60 发生的机制解释。

**W2** [warning] **Blind zone（α<0.50）限制了框架的实际适用性**
- 具体位置：§4.2 "Blind zone" 段, Limitations §1
- 问题：在 α=0.25，distinct-1 已下降 40.3%（§4.2），但 Granger 检测完全无信号。实际场景中最危险的恰恰是低至中等污染的渐进累积。Detection boundary α_c≈0.50 意味着需要 ≥50% 合成数据才能检测，这对大多数实际部署场景过高。
- Limitations 中有提及但 Discussion 未充分讨论实际部署含义。
- 建议：在 Discussion 中增加一段关于 practical deployment implications 的讨论，明确哪些场景下该框架有效、哪些无效。

**W3** [warning] **Design Principles 1–2 的形式化呈现与证据强度不匹配**
- 具体位置：§3.1, Appendix X (derivations)
- 问题：Design Principle 1 和 2 使用定理编号和形式化 statement 风格，但：
  - DP1 有已知反例（SmolLM3-3B entropy decoupling, §4.5）
  - 推导依赖 Assumption 3（mode amplification），该假设未在实验中独立验证
  - "Design Principle" 的命名暗示这些是可靠的工程指导，但实际上它们是有条件的经验性观察
- 建议：将其重新定义为 "Empirical Observation" 或 "Heuristic"，或在陈述中加入明确的适用条件（"under mode amplification, as verified for Pythia-family models"）。

**W4** [warning] **Intervention 评估过于有限**
- 具体位置：§4.6
- 问题：Canary-based intervention 仅在 α=1.0（最有利条件）、Pythia-410M 和 Pythia-1.4B 上评估。15% entropy threshold 需要 generation 0 的 entropy baseline，这在实际场景中可能不可用。未与更简单的替代方案（如固定周期数据刷新、直接监控 perplexity）比较。
- 论文称其为 "proof of concept"，这是合理的 framing，但 Conclusion 中的表述提升了其地位。
- 建议：在 Conclusion 中对 intervention 结果的措辞加上 "proof-of-concept" 限定语。

**W5** [warning] **Granger causality 的局限性讨论不够充分**
- 具体位置：§5 "Granger causality limitations" 段
- 问题：Discussion 提到了短 T、bivariate confounders 和非线性局限。但以下重要局限缺失：
  - **Observational equivalence**：多个不同的因果结构可以产生相同的 Granger causality 模式——这对 "canary" 声明有根本性影响
  - **Time aggregation bias**：per-generation 的采样间隔是任意的（为什么是每代一个点？），不同的时间聚合可能改变 lead-lag 检测结果
  - T=10 在计量经济学标准下的意义：§5 提到 "T≥100" 是标准，但对 T=10 只有 10% 的推荐序列长度这一事实未给予足够强调
- 建议：增加一段关于 observational equivalence 和 time aggregation 的简要讨论。

---

### 小问题（不影响接收）

**M1** 第 2 页是纯文本页面（Introduction 续 + Related Work），无任何图表。对于信息密度很高的论文，建议考虑视觉元素的均匀分布。

**M2** bib 条目格式不一致：部分条目使用作者首字母缩写（如 du2025scales: "Du, Y. and Wu, G."），而其他条目使用完整姓名。应统一。

**M3** Abstract 中 "Granger-precedes" 是一个新造复合词，对不熟悉 Granger causality 的读者可能造成困惑。建议改写为更易读的表述（如 "Token entropy temporally precedes diversity collapse by at least one generation (Granger significance)"）。

**M4** 附录非常庞大（~7 页，A–Z 共 24 个 section），主文有时依赖附录来支撑核心声明（如 Shapley 分析在 Appendix P，cascade 验证在 Appendix W）。最关键的附录结果建议在主文中给出简要摘要。

---

### Questions to Authors

**Q1.** Cross-architecture evaluation 为什么限于 α=1.0？即使只在 α=0.50（临界边界）增加 2-3 个架构的验证，都能大幅增强 generalizability 声明。这是否因为计算成本限制？如果是，请估算单个架构的完整 phase diagram 的计算成本。

**Q2.** α=0.60 anomaly：是否存在可以预测 temporal lag compression 何时会击败方向性检测的先验指标？如果没有，实际部署者如何处理这个失败模式？

**Q3.** PermG FPR 7.4% [2.1%, 17.9%] 高于名义 5% 水平。是否考虑过更严格的 permutation threshold 或更多 permutations 来降低 FPR？

**Q4.** WikiText-103 是相对同质的数据集。结果对训练语料的选择有多敏感？更多样化的语料（如 C4 或 The Pile）是否会移动 detection boundary？

**Q5.** Conclusion 提到 "evaluation at >7B parameters remains open"。五个家族中 Pythia-6.9B 的结果是否提供了关于 scale 趋势的初步信号？

---

### Missing References

1. **Dakos et al. (2012)** "Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data" — PLoS ONE. 方法论上直接相关：讨论短时序中 early warning 检测方法，是本文核心挑战的源头文献之一。已在 bib 中但未被引用。

2. **Bell et al. (2022)** "Modeling the Machine Learning Multiverse" — NeurIPS. 与 specification curve / multiverse analysis 框架直接相关。已在 bib 中但未被引用。

3. **Gu et al. (2026, SIGMA)** "Scalable Spectral Insights for LLM Model Collapse" — 最近的基于谱方法的 model collapse 检测方案，应在 Related Work §2.2 中作为替代方法论讨论。已在 bib 中但未被引用。

4. **Dakos et al. (2008)** "Slowing Down as an Early Warning Signal for Abrupt Climate Change" — PNAS. Critical-slowing-down early warning 的奠基性实证工作。论文引用了 Scheffer et al. 2009 的理论框架，但缺少 Dakos 2008 的实证基础。已在 bib 中但未被引用。

（以上四篇均已在 bib 文件中有条目，但在正文中未被 cite，属于 bib 清理 + related work 覆盖的双重问题。）

---

### 格式合规检查

| 检查项 | 状态 | 说明 |
|--------|------|------|
| Abstract ≤200 words | ✅ | 约 147 words |
| 正文 ≤8 页 | ✅ | Sections 1–6 在第 8 页内完成 |
| Limitations section 存在且在正文内 | ✅ | \section*{Limitations} 位于 Conclusion 之后、References 之前 |
| Limitations 不在 Appendix | ✅ | 正文第 8 页 |
| ACL 模板使用 | ✅ | \usepackage[review]{acl} |
| 匿名性 | ✅ | \author{Anonymous} |
| AI Writing Disclosure | ✅ | 第 16 页 "Use of AI Assistants" 节，声明使用 Claude |
| β 符号重用 | ✅ 无问题 | β 仅用于 sub-linear signal exponent（Eq. 2），未用于统计功率 |
| 主文包含核心结果 summary table | ✅ | Table 1（detection outcomes）, Table 2（consensus threshold） |
| Figure/Table 分布 | 基本合理 | 仅第 2 页无视觉元素 |

---

### 总体评分

**Overall: 3.0 — Findings**

**一句话总结**：扎实但范围过窄的实证研究——方法敏感性发现（FPR 7%→94%）有方法论价值，但 "detectability landscape" 实质上仅覆盖 Pythia-410M + WikiText-103 的单一 phase diagram，cross-architecture 验证仅在 α=1.0（最容易的检测场景），标题和声明的广度与实际证据之间存在显著 gap。核心方法均为计量经济学标准工具的领域迁移，novelty 有限。适合 Findings 接收，需在 rebuttal 中解决 scope-claim mismatch。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1310 · 2026-05-24T23:03:36.970608+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**N1 [critical] 统计功效严重不足，定量声明缺乏可信支撑**\n- 每个条件仅 3 seeds，每个 α 值仅 8 pairs。binomial CI 极宽：6/8 → [0.25, 0.92]\n- Phase diagram 每个网格点仅 3-8 个观测值\n- 论文称\"sharp onset\"但数据无法区分 sharp 和 gradual transition\n- 建议增加 seeds 至 10-15 per condition\n\n**N2 [critical] 跨架构验证仅在 α=1.0，核心区域无数据**\n- Phase diagram 核心区 α∈[0.45,0.75] 完全无跨架构数据\n- Abstract \"Cross-architecture evaluation across five model families\" 构成 overclaim\n- GPT-2 null FPR 50% 直接否定该架构上检测的有效性\n\n**N3 [critical] PermG FPR 超出 nominal 5% 且 CI 极宽**\n- 4/54 = 7.4%，超出 nominal 5%\n- CI [2.1%, 17.9%] 意味真实 FPR 可能接近 18%\n- MMCT K≥3 FPR 11.1% 超出 nominal 两倍\n- 建议增加 null seeds 至 20+\n\n**N4 [critical] 幂律边界仅 3-4 个有效数据点，γ CI 无区分度**\n- γ ∈ [0.64, 2.08] 跨越亚线性/超线性分界\n- 排除 α=0.60 后仅 3-4 个有效 α 值支撑拟合\n- 任何函数形式都能拟合 3-4 个点\n\n### Reviewer 1 的 Should-Fix 问题\n\n**W1** Intervention 实验 N=2, α=1.0, post-hoc threshold，证据极弱\n**W2** MMCT FPR-inverse weighting 依赖噪声极大的经验 FPR 估计，权重 uncertainty 未讨论\n**W3** Granger 因果局限讨论不充分（transfer entropy 0/192、partial correlation 方向矛盾、bivariate confounders）\n**W4** 单一解码策略（temp=1.0, top-k=50）限制外部效度\n**W5** Table 2 显示 MMCT 对 K 阈值极度敏感，仅 K=3 勉强可用\n\n### Reviewer 1 的 Minor Issues\n\n**M1** BH-FDR PRDS 假设未讨论\n**M2** Eq.(2) 中 γ=1/(2β) 的 β 验证未在正文呈现\n**M3** Figure 2 y轴标签难读\n**M4** Abstract 首句预设 collapse 总是存在\n**M5** Limitations 对 >7B 局限的影响可能更大\n\n### Reviewer 1 评分：Overall 3/5 (Findings)\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 问题逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**N1 [critical] 统计功效严重不足，定量声明缺乏可信支撑**\n- 每个条件仅 3 seeds，每个 α 值仅 8 pairs。binomial CI 极宽：6/8 → [0.25, 0.92]\n- Phase diagram 每个网格点仅 3-8 个观测值\n- 论文称\"sharp onset\"但数据无法区分 sharp 和 gradual transition\n- 建议增加 seeds 至 10-15 per condition\n\n**N2 [critical] 跨架构验证仅在 α=1.0，核心区域无数据**\n- Phase diagram 核心区 α∈[0.45,0.75] 完全无跨架构数据\n- Abstract \"Cross-architecture evaluation across five model families\" 构成 overclaim\n- GPT-2 null FPR 50% 直接否定该架构上检测的有效性\n\n**N3 [critical] PermG FPR 超出 nominal 5% 且 CI 极宽**\n- 4/54 = 7.4%，超出 nominal 5%\n- CI [2.1%, 17.9%] 意味真实 FPR 可能接近 18%\n- MMCT K≥3 FPR 11.1% 超出 nominal 两倍\n- 建议增加 null seeds 至 20+\n\n**N4 [critical] 幂律边界仅 3-4 个有效数据点，γ CI 无区分度**\n- γ ∈ [0.64, 2.08] 跨越亚线性/超线性分界\n- 排除 α=0.60 后仅 3-4 个有效 α 值支撑拟合\n- 任何函数形式都能拟合 3-4 个点\n\n### Reviewer 1 的 Should-Fix 问题\n\n**W1** Intervention 实验 N=2, α=1.0, post-hoc threshold，证据极弱\n**W2** MMCT FPR-inverse weighting 依赖噪声极大的经验 FPR 估计，权重 uncertainty 未讨论\n**W3** Granger 因果局限讨论不充分（transfer entropy 0/192、partial correlation 方向矛盾、bivariate confounders）\n**W4** 单一解码策略（temp=1.0, top-k=50）限制外部效度\n**W5** Table 2 显示 MMCT 对 K 阈值极度敏感，仅 K=3 勉强可用\n\n### Reviewer 1 的 Minor Issues\n\n**M1** BH-FDR PRDS 假设未讨论\n**M2** Eq.(2) 中 γ=1/(2β) 的 β 验证未在正文呈现\n**M3** Figure 2 y轴标签难读\n**M4** Abstract 首句预设 collapse 总是存在\n**M5** Limitations 对 >7B 局限的影响可能更大\n\n### Reviewer 1 评分：Overall 3/5 (Findings)\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 问题逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1311 · 2026-05-24T23:03:57.071675+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 20101
}
```

</details>

---


### Tool call

_source line 1312 · 2026-05-24T23:03:58.176755+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**N1 [critical] 标题和核心声明的 scope 与实际证据不匹配**\n- \"Detectability Landscape\" 实质仅在 Pythia-410M + WikiText-103 + T=10 上绘制\n- Cross-architecture validation 仅在 α=1.0（最容易检测的场景）\n- Phase diagram 最有趣的区域（α≈0.50 附近）在其他架构上完全无数据\n- 建议缩窄标题或补充跨架构边界验证\n\n**N2 [critical] \"Five families (345M-6.9B)\" 给读者造成误导性广度印象**\n- Abstract \"supports forward detection in the majority of conditions\" 技术正确但误导\n- 11/15 = 27% 失败率在统计检测中并不小\n- \"345M-6.9B\" 暗示 scale robustness 但核心发现在 >1.4B 上完全未验证\n- 建议明确加上 \"at α=1.0 (full replacement)\"\n\n### Reviewer 2 的 Should-Fix 问题\n\n**W1** α=0.60 非单调异常破坏 phase diagram 叙事连贯性，\"temporal lag compression\" 解释是 post-hoc\n**W2** Blind zone（α<0.50）限制框架的实际适用性，α=0.25 时 distinct-1 已下降 40% 但检测无信号\n**W3** Design Principles 1-2 形式化呈现与证据强度不匹配（有反例、假设未验证、命名暗示可靠性）\n**W4** Intervention 评估过于有限（仅 α=1.0，未与更简单替代方案比较）\n**W5** Granger causality 局限讨论不够充分（observational equivalence、time aggregation bias、T=10 仅为推荐长度 10%）\n\n### Reviewer 2 的 Minor Issues\n\n**M1** 第 2 页纯文本无图表\n**M2** bib 条目格式不一致\n**M3** Abstract \"Granger-precedes\" 对非专业读者可能困惑\n**M4** 附录庞大（24 sections），核心结果应在主文简要摘要\n\n### Reviewer 2 的 Missing References\n\n- Dakos et al. (2012) — bib 中存在但正文未引用\n- Bell et al. (2022) — bib 中存在但正文未引用\n- Gu et al. (2026, SIGMA) — bib 中存在但正文未引用\n- Dakos et al. (2008) — bib 中存在但正文未引用\n\n### Reviewer 2 格式合规检查\n\n全部通过（Abstract ≤200w, 正文 ≤8页, Limitations 正确位置, ACL 模板, 匿名, AI disclosure）\n\n### Reviewer 2 评分：Overall 3/5 (Findings)\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 问题逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**N1 [critical] 标题和核心声明的 scope 与实际证据不匹配**\n- \"Detectability Landscape\" 实质仅在 Pythia-410M + WikiText-103 + T=10 上绘制\n- Cross-architecture validation 仅在 α=1.0（最容易检测的场景）\n- Phase diagram 最有趣的区域（α≈0.50 附近）在其他架构上完全无数据\n- 建议缩窄标题或补充跨架构边界验证\n\n**N2 [critical] \"Five families (345M-6.9B)\" 给读者造成误导性广度印象**\n- Abstract \"supports forward detection in the majority of conditions\" 技术正确但误导\n- 11/15 = 27% 失败率在统计检测中并不小\n- \"345M-6.9B\" 暗示 scale robustness 但核心发现在 >1.4B 上完全未验证\n- 建议明确加上 \"at α=1.0 (full replacement)\"\n\n### Reviewer 2 的 Should-Fix 问题\n\n**W1** α=0.60 非单调异常破坏 phase diagram 叙事连贯性，\"temporal lag compression\" 解释是 post-hoc\n**W2** Blind zone（α<0.50）限制框架的实际适用性，α=0.25 时 distinct-1 已下降 40% 但检测无信号\n**W3** Design Principles 1-2 形式化呈现与证据强度不匹配（有反例、假设未验证、命名暗示可靠性）\n**W4** Intervention 评估过于有限（仅 α=1.0，未与更简单替代方案比较）\n**W5** Granger causality 局限讨论不够充分（observational equivalence、time aggregation bias、T=10 仅为推荐长度 10%）\n\n### Reviewer 2 的 Minor Issues\n\n**M1** 第 2 页纯文本无图表\n**M2** bib 条目格式不一致\n**M3** Abstract \"Granger-precedes\" 对非专业读者可能困惑\n**M4** 附录庞大（24 sections），核心结果应在主文简要摘要\n\n### Reviewer 2 的 Missing References\n\n- Dakos et al. (2012) — bib 中存在但正文未引用\n- Bell et al. (2022) — bib 中存在但正文未引用\n- Gu et al. (2026, SIGMA) — bib 中存在但正文未引用\n- Dakos et al. (2008) — bib 中存在但正文未引用\n\n### Reviewer 2 格式合规检查\n\n全部通过（Abstract ≤200w, 正文 ≤8页, Limitations 正确位置, ACL 模板, 匿名, AI disclosure）\n\n### Reviewer 2 评分：Overall 3/5 (Findings)\n\n---\n\n请对以上每个 Must-Fix 和 Should-Fix 问题逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 1313 · 2026-05-24T23:03:59.510686+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1333
}
```

</details>

---


### Assistant

_source line 1314 · 2026-05-24T23:04:01.996550+00:00_

交叉分享已发送给两位 Reviewer，等待回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 126

## Round 126

2 recorded events


### User

_source line 1315 · 2026-05-24T23:04:04.540444+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成。核心评估：

- **Overall: 3.0 (Findings)**
- **关键问题**：标题/声明的 scope 与实际证据不匹配（N1/N2）——phase diagram 仅覆盖 Pythia-410M + WikiText-103，cross-architecture 仅在 α=1.0 验证
- **主要优势**：方法敏感性发现（FPR 7%→94%）有实际方法论价值，统计方法论严谨，失败案例报告诚实
- **格式合规**：全部通过（abstract 147 words，正文 8 页，Limitations 位置正确，AI disclosure 存在）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1316 · 2026-05-24T23:04:08.667872+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 127

## Round 127

6 recorded events


### User

_source line 1317 · 2026-05-24T23:05:39.676507+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 交叉回应 Reviewer 2 审稿意见

---

## Must-Fix 问题

### [AGREE] R2-N1: 标题和核心声明的 scope 与实际证据不匹配

完全同意。这与我的 N2 高度一致。论文标题 "Characterizing the Detectability Landscape" 暗示了系统性的多条件覆盖，但实际 phase diagram 仅基于 Pythia-410M + WikiText-103。跨架构验证仅在 α=1.0——这是最极端、最容易检测的条件，对 phase diagram 核心过渡区域（α∈[0.45, 0.75]）的泛化性提供零证据。

补充我自己的发现：Table 17（Appendix Z.1）中 GPT-2 medium 的 null FPR 高达 50%（Appendix Z.2），意味着即使在 α=1.0 上，GPT-2 的检测结果也不具统计意义。这进一步削弱了"five families"的跨架构叙事。

R2 建议"缩窄标题或补充跨架构边界验证"是合理的最低修改要求。

---

### [AGREE] R2-N2: "Five families (345M-6.9B)" 给读者造成误导性广度印象

完全同意。Abstract 中 "Cross-architecture evaluation across five model families supports forward detection in the majority of conditions" 确实是 technically correct but misleading。一个不熟悉细节的读者（包括 AC）会自然理解为多 α 值、多架构的系统验证。

R2 指出的 11/15 = 27% 失败率是一个我未充分强调的好角度。在统计检测领域，近三分之一的条件检测失败本身就值得警惕，论文却将其框架为"majority of conditions"的成功。

R2 建议在 abstract 中明确加上 "at α=1.0 (full replacement)" 是必要修改，我完全支持。此外，"345M-6.9B" 的范围描述也需要注明核心定量结果（phase diagram, detection boundary）仅基于 410M。

---

## Should-Fix 问题

### [AGREE] R2-W1: α=0.60 非单调异常与 post-hoc 解释

同意。我在 Questions #2 中也问了这个问题。Section 4.3 提到 α=0.60 的 non-monotonic dip（"the α=0.60 non-monotonic dip"），论文用 "temporal lag compression" 解释并将其排除后仅用 3-4 个 α 值拟合幂律边界（我的 N4）。

R2 正确指出这一解释是 post-hoc 的——没有独立证据支持 "lag compression" 假说，它只是对异常值的便利解释。如果该异常在多 seeds 之间一致出现，它可能反映了真实的非单调物理过程而非噪声，排除它会引入 selection bias。论文需要：(1) 报告该异常在不同 seeds 间的一致性；(2) 展示保留该点后拟合结果的变化。

---

### [AGREE] R2-W2: Blind zone 限制框架实际适用性

同意，且这个角度我的审稿未充分覆盖。R2 指出 α=0.25 时 distinct-1 已下降约 40%（参见 Table 4, Appendix B: distinct-1 drift at α=0.25 为 -58.3±10.9%），但所有五种检测方法均无信号。这意味着：

**在框架能检测到 collapse 时，下游质量已经严重退化。** 如果检测只在 α≈0.50 以上才有效，而 α=0.25 已经造成显著的 diversity 损失，那么该框架的 early warning 价值大打折扣——它更像是一个 confirmation tool（确认已经发生的退化）而非 prevention tool（在退化变严重前发出警告）。

论文在 Discussion/Limitations 中未充分讨论这一 fundamental limitation。建议增加对 blind zone 的实际影响的 honest assessment。

---

### [REBUT] R2-W3: Design Principles 1-2 形式化呈现与证据强度不匹配

部分不同意。R2 认为 Design Principles 的 formal 呈现暗示了过高的可靠性，但我认为这需要区分两个层面：

1. **理论推导层面（Appendix X）**：Design Principle 1（entropy 先于 diversity 响应）和 Design Principle 2（diversity 是阈值指示器）有 formal derivations，基于 mode amplification 假设（Assumption 3）。推导逻辑自洽，前提假设也合理（有限词汇上的概率重分布）。称之为 "Design Principles" 而非 "Theorems" 本身已经是较谦逊的表述。

2. **经验验证层面**：Table 16（Appendix W）确认了 cascade ordering 在 representative conditions 下成立。Section 4.3 的 dose-response 分析也支持 entropy→onset 先于 diversity→onset 的时序。

然而，R2 提到的反例（first-differencing 消除 canary→perplexity association, F=0, p≈0.99; Section 3.3）确实值得重视。此外，Appendix F 的 transfer entropy 0/192 significant pairs 对 Design Principle 1 构成挑战——如果 canary 真的"precedes" downstream metrics，非线性因果检验应该能捕捉到某些信号。

**结论**：Design Principles 作为 theoretical framework 的形式化程度是合理的，但论文应更明确讨论已知反例和局限，而非在正文中仅呈现支持性证据。我建议降级为 "partially agree"——R2 的担忧有道理但表述过于绝对。

---

### [AGREE] R2-W4: Intervention 评估过于有限

完全同意。这与我的 W1 一致。N=2 seeds, α=1.0 only, post-hoc 15% threshold。R2 额外指出的"未与更简单替代方案比较"也是有效批评——例如，简单的 perplexity 阈值（不依赖 canary metrics）是否也能达到类似效果？如果一个 naive baseline 就能完成同样的 intervention，canary-based approach 的增量价值就不明确了。

论文 Section 4.6 将此部分称为 "Proof of Concept"，但即使对 PoC 而言，N=2 + single α + no baseline comparison 也太薄弱了。

---

### [AGREE] R2-W5: Granger causality 局限讨论不够充分

同意，且 R2 的补充角度有价值。我的 W3 主要从 confounders 和 transfer entropy null 结果角度讨论，R2 增加了两个重要点：

1. **Observational equivalence**：Granger precedence 不等于 causation，但论文中多处措辞（如 Section 5 "Granger-precedence claim", abstract "Granger-precedes"）给读者留下了因果性的印象。Section 3.2 虽有 disclaimer（"not mechanistic causation"），但这种 caveat 容易被忽略。

2. **T=10 仅为推荐长度 10%**：这是我未注意到的好观察。Granger 检验在短序列上 power 极低。Appendix N 的 power simulation 显示 T=10 时 FPR under FDR correction 已经 inflated。论文选择 T=10 作为 primary 设置但在如此短的序列上做 Granger 检验，本身就是方法论上的 tension。

R2 提到的 "time aggregation bias" 也值得重视——generation 间隔不是自然时间单位，不同 generation 之间的训练数据量和质量变化可能引入系统性偏差。

---

## Minor Issues

### [AGREE] R2-M1: 第 2 页纯文本无图表
同意这是排版优化点。Related Work 和 Method 开头集中在第 2 页，视觉密度低。不影响接收但改善后阅读体验更好。

### [AGREE] R2-M2: bib 条目格式不一致
未做详细检查，但 bib 格式一致性是基本要求，同意应修复。

### [AGREE] R2-M3: Abstract "Granger-precedes" 对非专业读者可能困惑
同意。Abstract 应对更广泛受众可读。建议改为更直白的表述如 "canary metrics show statistically significant temporal precedence over downstream metrics"。

### [REBUT] R2-M4: 附录庞大（24 sections）应在主文简要摘要
部分不同意。附录的广泛 robustness checks 是本文的优势之一（我的 S4）。ARR 审稿人不强制阅读附录，但附录的存在为有疑问的审稿人提供了验证渠道。我认为当前主文对附录的引用方式（如 "see Appendix D" 式的简短引用）是合适的。不过，R2 的观点在一点上有效：某些附录结果如果对核心论证很重要（如 Appendix R 的 FPR 分析），应在主文中更充分摘要而非仅以括号引用带过。

---

## Missing References

### [AGREE] R2 关于 bib 中未引用条目的发现
同意。bib 文件中存在但正文未引用的条目（Dakos et al. 2012, Bell et al. 2022, Gu et al. 2026, Dakos et al. 2008）应该要么在正文中引用（如果相关），要么从 bib 中移除以保持一致性。未引用的 bib 条目是常见的编辑遗漏，容易修复。

---

## 两位 Reviewer 的共识总结

R1（我）和 R2 在以下核心问题上完全一致：
1. **跨架构验证不足**（仅 α=1.0）且 abstract claim 过度（R1-N2 ≈ R2-N1 + R2-N2）
2. **Intervention 实验过弱**（N=2, α=1.0, post-hoc threshold）（R1-W1 ≈ R2-W4）
3. **Granger causality 局限讨论不充分**（R1-W3 ≈ R2-W5）
4. **Overall 3/5 Findings** — 框架有价值但实验规模不足

R1 独有的重点关切：**统计功效**（3 seeds/condition 的 CI 宽度问题）和 **FPR 标定**（7.4% > 5%, CI 极宽）。
R2 独有的重点关切：**blind zone 实际影响**（α<0.50 已严重退化但检测无信号）和 **scope overclaim**（标题暗示的广度与实际证据不匹配）。

两者互补，共同指向同一结论：论文提出了有价值的框架但定量声明超出了当前证据的支撑范围。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1318 · 2026-05-24T23:06:41.800593+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1319 · 2026-05-24T23:06:41.851366+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-24T23:07:12.320916+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 1 的审稿要点\n\n请逐条回应以下 Reviewer 1 的发现，标注 [AGREE] 或 [REBUT]（附理由）。\n\n---\n\n### R1 的 Must-Fix 问题\n\n**R1-N2: 跨架构验证仅在 α=1.0，scope overclaim**\n- 标题 \"Characterizing the Detectability Landscape\" 暗示系统性多条件覆盖，但 phase diagram 仅基于 Pythia-410M + WikiText-103\n- 跨架构验证仅 α=1.0（最极端条件），对核心过渡区域 α∈[0.45, 0.75] 提供零泛化证据\n- Table 17 中 GPT-2 medium null FPR 高达 50%（Appendix Z.2），α=1.0 上 GPT-2 结果不具统计意义\n- \"Five families\" 叙事被严重削弱\n\n**R1-N4: 幂律边界拟合仅 3-4 个 α 值**\n- 排除 α=0.60 异常后，phase boundary 的幂律拟合仅基于 3-4 个数据点\n- 数据点数量不足以可靠拟合幂律关系\n\n### R1 的 Should-Fix 问题\n\n**R1-W1: Intervention 实验过弱**\n- N=2 seeds, α=1.0 only, post-hoc 15% threshold\n- 即使作为 Proof of Concept 也太薄弱\n\n**R1-W2: 统计功效不足**\n- 3 seeds/condition 导致 CI 极宽\n- 无法可靠区分真实效应和噪声\n\n**R1-W3: Granger causality 局限**\n- Transfer entropy 0/192 significant pairs（Appendix F）\n- First-differencing 消除 canary→perplexity 关联（F=0, p≈0.99, Section 3.3）\n- 潜在 confounders（训练动态）未排除\n\n**R1-FPR: FPR 标定问题**\n- 观察到的 FPR 7.4% > 名义 5%\n- CI 极宽，统计可靠性存疑\n\n### R1 的 Strengths 要点\n- S4: 附录的广泛 robustness checks 是优势\n- 框架本身（canary metrics 用于检测 model collapse）有价值\n\n### R1 的 Overall\n- 评分 3/5（Findings）\n- 框架有价值但定量声明超出证据支撑\n\n---\n\n请对以上每个要点给出 [AGREE] 或 [REBUT] 回应。特别关注：\n1. R1-N4 的幂律拟合数据点不足问题——你是否在审稿中也注意到？\n2. R1-W2 的 3 seeds 统计功效问题——你如何评估其严重性？\n3. R1-FPR 的 FPR 标定问题——这是否影响你对核心结果可靠性的判断？",
  "reviewer_id": "2",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 1 的审稿要点\n\n请逐条回应以下 Reviewer 1 的发现，标注 [AGREE] 或 [REBUT]（附理由）。\n\n---\n\n### R1 的 Must-Fix 问题\n\n**R1-N2: 跨架构验证仅在 α=1.0，scope overclaim**\n- 标题 \"Characterizing the Detectability Landscape\" 暗示系统性多条件覆盖，但 phase diagram 仅基于 Pythia-410M + WikiText-103\n- 跨架构验证仅 α=1.0（最极端条件），对核心过渡区域 α∈[0.45, 0.75] 提供零泛化证据\n- Table 17 中 GPT-2 medium null FPR 高达 50%（Appendix Z.2），α=1.0 上 GPT-2 结果不具统计意义\n- \"Five families\" 叙事被严重削弱\n\n**R1-N4: 幂律边界拟合仅 3-4 个 α 值**\n- 排除 α=0.60 异常后，phase boundary 的幂律拟合仅基于 3-4 个数据点\n- 数据点数量不足以可靠拟合幂律关系\n\n### R1 的 Should-Fix 问题\n\n**R1-W1: Intervention 实验过弱**\n- N=2 seeds, α=1.0 only, post-hoc 15% threshold\n- 即使作为 Proof of Concept 也太薄弱\n\n**R1-W2: 统计功效不足**\n- 3 seeds/condition 导致 CI 极宽\n- 无法可靠区分真实效应和噪声\n\n**R1-W3: Granger causality 局限**\n- Transfer entropy 0/192 significant pairs（Appendix F）\n- First-differencing 消除 canary→perplexity 关联（F=0, p≈0.99, Section 3.3）\n- 潜在 confounders（训练动态）未排除\n\n**R1-FPR: FPR 标定问题**\n- 观察到的 FPR 7.4% > 名义 5%\n- CI 极宽，统计可靠性存疑\n\n### R1 的 Strengths 要点\n- S4: 附录的广泛 robustness checks 是优势\n- 框架本身（canary metrics 用于检测 model collapse）有价值\n\n### R1 的 Overall\n- 评分 3/5（Findings）\n- 框架有价值但定量声明超出证据支撑\n\n---\n\n请对以上每个要点给出 [AGREE] 或 [REBUT] 回应。特别关注：\n1. R1-N4 的幂律拟合数据点不足问题——你是否在审稿中也注意到？\n2. R1-W2 的 3 seeds 统计功效问题——你如何评估其严重性？\n3. R1-FPR 的 FPR 标定问题——这是否影响你对核心结果可靠性的判断？",
    "reviewer_id": "2",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 1321 · 2026-05-24T23:07:16.193481+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3872
}
```

</details>

---


### Assistant

_source line 1322 · 2026-05-24T23:07:28.239904+00:00_

已将 Reviewer 1 的审稿要点转发给 Reviewer 2，等待其交叉回应。

当前交叉分享状态：
- **Reviewer 1 → R2 回应**：✅ 已收到（4/4 Must-Fix AGREE，Should-Fix 仅 W3、M4 部分 REBUT）
- **Reviewer 2 → R1 回应**：⏳ 等待中

R1 的交叉回应要点记录：
- 与 R2 在核心问题上高度共识：跨架构验证不足、abstract overclaim、intervention 过弱、Granger 局限
- R1 补充了 R2 未充分覆盖的角度：GPT-2 medium null FPR 50% 进一步削弱跨架构叙事
- R1 对 R2 的 blind zone 观点（α<0.50 检测失败但质量已退化）表示认同且认为自己审稿中未充分强调
- 两个部分 REBUT：Design Principles 形式化程度合理（但需讨论反例）；附录庞大是优势而非缺陷（但关键结果应在主文更充分摘要）

收到 Reviewer 2 的交叉回应后将评估收敛并合成最终报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 128

## Round 128

14 recorded events


### User

_source line 1323 · 2026-05-24T23:07:29.225573+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的 7 个 Must-Fix/Should-Fix 问题：5 个 [AGREE]、2 个 [REBUT]（W3 Design Principles 和 M4 附录规模）。两位 Reviewer 在跨架构验证不足、intervention 过弱、Granger 局限、Overall 3/5 Findings 上完全一致。

---

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条评估

---

### Must-Fix 问题

**[AGREE] R1-N1: 统计功效不足，定量声明缺乏可信支撑**

同意核心论点。3 seeds per condition、8 pairs per α 的确太少，binomial CI [0.25, 0.92]（6/8）使得 phase diagram 每个网格点的定量可信度很低。

但需要补充一个缓解因素：论文并非仅靠裸比例作声明。§4.2 的 sigmoid regression 拟合（k=15.7, R²=0.969）和 Fisher exact test（p=3.45×10⁻¹¹）为 "sharp onset" 提供了超越 raw binomial 的统计支撑。Specification curve analysis（1,160 configurations, Figure 6, Appendix E）也跨越了 methods/pairs/seeds 的组合来验证 blind→onset jump 的鲁棒性。

因此我的立场是：**sample size 确实是 weakness**，但 "数据无法区分 sharp 和 gradual transition" 的说法过于绝对——sigmoid Hill coefficient k=15.7 表明 80% 的转换发生在 Δα≈0.05 内（§4.3），这不是 3-4 个点能伪造的 gradient。

**严重程度判定：Should-Fix 而非 Must-Fix。** 增加 seeds 当然更好，但现有的多方法交叉验证提供了部分弥补。

---

**[AGREE] R1-N2: 跨架构验证仅在 α=1.0**

完全同意。这与我自己的 N1、N2 一致。Cross-architecture validation 仅在 α=1.0（全合成替换）是论文最大的 scope-claim mismatch。

补充我的发现：即使在 α=1.0 这个最有利场景，也有 4/15（27%）条件失败。其中 GPT-2 null FPR 达 50%（Appendix R, §4.5），直接意味着 PermG 在该架构上无法可靠使用——这不是边缘 failure，而是根本性的。论文在 §4.5 "Failure mode taxonomy" 中报告了这些 failure，但 Abstract 和 Conclusion 的措辞 "supports forward detection in the majority of conditions" 未充分传达这些 qualification。

**严重程度判定：同意 Must-Fix。**

---

**[REBUT] R1-N3: PermG FPR 超出 nominal 5% — 严重程度应降级**

R1 的事实陈述是准确的：4/54 = 7.4%，CI [2.1%, 17.9%]。但我认为这不构成 Must-Fix，理由如下：

1. **论文的 contribution 不是声称 PermG 控制在 5%**，而是展示 PermG 是五种方法中 FPR 最低的（7.4% vs NaiveXCorr 94.4%）。方法敏感性比较框架（§3.3）本身就承认没有完美的检测器。

2. **置换检验的 FPR 受有限 null samples 约束**。54 null pairs 的 granularity 决定了 FPR 估计的精度。论文在 §3.3 提到 "7/9 seeds yield 0 FP"（Appendix R），说明多数 seeds 的 FPR 实际为 0%，4 个 false positives 集中在少数 seeds。

3. **MMCT K≥3 的 11.1% FPR** 确实偏高，但 Table 2 完整呈现了 K=2 到 K=5 的 trade-off，读者可自行选择操作点。

4. **Limitations §2 明确承认此问题**："PermG's empirical FPR is 7.4% (CI [2.1%, 17.9%]) and K≥3 consensus yields 11.1% (6/54)"。

**严重程度判定：Should-Fix 而非 Must-Fix。** 增加 null seeds 可以收窄 CI，但现有结果已在论文内得到合理 qualification。

---

**[AGREE] R1-N4: 幂律边界数据点过少，γ CI 无区分度**

同意。γ ∈ [0.64, 2.08] 跨越了 3× 的范围，确实不具有参数辨识力。论文自己也承认 "the qualitative conclusion—detection improves with longer observation—is robust to the specific γ value"（§3.4），这等于默认 γ 的精确值无法确定。

但我注意到论文的措辞已经相当谨慎：§3.4 说 "consistent with power-law scaling"（consistent with，而非 "demonstrates"），并且在 §4.4 中提供了定性验证（α=0.45 从 T≤10 的 0/8 跨越到 T=15 的 6/8）。问题不在于论文过度声称了 power-law 的精确性，而在于用 Eq. (1)-(2) 的形式化呈现给读者一种虚假的精确感。

**严重程度判定：同意 Should-Fix（但非 Must-Fix）。** 论文的定性结论（detection improves with T）有充分支撑；建议将 Eq. (2) 降级为 "empirical scaling hypothesis" 而非给出一个看起来精确的公式。

---

### Should-Fix 问题

**[AGREE] R1-W1: Intervention 证据极弱**

同意，与我的 W4 一致。N=2 architectures, α=1.0 only, threshold 从同一数据确定。论文称 "proof of concept" 是合理的自我限定，但 Conclusion 中 "providing a canary signal whose triggered cessation reduces peak perplexity" 的措辞未保留 proof-of-concept 的限定语。

---

**[PARTIALLY AGREE] R1-W2: MMCT weighting noise**

同意权重估计噪声未讨论是一个缺陷。但需要指出论文有部分回应：Appendix Q（MMCT Weight Robustness Ablation）测试了四种加权方案（equal, cap-5, cap-10, FPR-inverse cap-100），结论是 PermG 在所有方案下均排名第一（PermG best combined Shapley −0.152），说明结果对加权选择有一定鲁棒性。

因此问题的实质是：robustness ablation 的存在降低了这个 weakness 的严重性，但确实应该在主文中提及而非仅放在附录。

---

**[PARTIALLY REBUT] R1-W3: Granger 局限讨论 — partial correlation 方向矛盾的说法需要纠正**

同意 Granger 局限讨论不够充分（与我的 W5 一致），但 R1 提到的 "partial correlation 方向矛盾" 需要澄清。

§5 "Granger causality limitations" 段报告的 partial correlation 结果实际上 **支持** 论文的 Granger precedence claim：
- 去趋势后，同期关联减弱（|r̄|: 0.590→0.381 at α=0.50）
- 去趋势后，滞后关联 **增强**（0.759→0.841）
- 35/36 pairs 保持显著性（Appendix V.1）

这个模式——"同期减弱而滞后增强"——正是 genuine temporal precedence 区别于 shared-trend artifact 的标志。所以 partial correlation 的结果不是 "方向矛盾"，而是对 Granger 发现的补充验证。

**但我同意 R1 的其他两点**：transfer entropy 0/192 确实值得更多讨论（是 nonlinear structure 缺失还是 short-T power 不足？论文在 §5 承认无法区分），bivariate confounders 的讨论确实不够。我在自己的审稿中也提到了 observational equivalence 和 time aggregation bias 的缺失。

---

**[AGREE] R1-W4: 单一解码策略限制外部效度**

同意。temp=1.0, top-k=50 是单一配置。不同解码策略（nucleus sampling, 不同温度, beam search）可能改变合成数据的分布特征，进而影响 detection boundary。Limitations 中有提及但 Discussion 未充分展开。

---

**[AGREE] R1-W5: MMCT 对 K 阈值极度敏感**

同意。Table 2 清楚显示仅 K=3 在 FPR-TPR 之间取得勉强平衡：
- K≥2: FPR 38.9%（不可接受）
- K≥3: FPR 11.1%, TPR 75%（勉强可用）
- K≥4: FPR 0%, TPR 25%（power 不足）
- K=5: FPR 0%, TPR 0%（完全无用）

这意味着 MMCT 的实际工作点只有一个。论文对此是透明的，但应在 Discussion 中讨论这对实际部署的影响——使用者需要先在 null-control 数据上校准 K，这限制了方法的即用性。

---

### Minor Issues

**[PARTIALLY AGREE] R1-M1: BH-FDR PRDS 假设**
§3.3 PermG 段确实提到了 PRDS："BH-FDR remains valid under positive regression dependence on a subset (PRDS) (Benjamini and Yekutieli, 2001)"。但未验证 PRDS 是否在该数据上成立。Minor concern。

**[AGREE] R1-M2: β 验证未在正文呈现**
Eq. (2) 中 S(α) = c·α^β 的 β 值未在主文中报告。仅在 Appendix X 有拟合。

**[AGREE] R1-M3: Figure 2 y 轴标签**
从 PDF 视觉检查，Figure 2 的 y 轴文字确实较小。

**[REBUT] R1-M4: Abstract 首句预设 collapse**
R1 说首句 "When language models train iteratively on their own output, the resulting distributional collapse is difficult to detect" 预设了 collapse 总是存在。但在 iterative training 文献中，collapse 在全替换条件下确实普遍发生（Shumailov et al. 2024, Dohmatob et al. 2025 strong collapse）。这是被领域接受的前提，而非未经验证的假设。论文在 §4.2 也用数据支撑了这一点：即使 α=0.00（纯真实数据 fine-tuning），distinct-1 也下降了 14.1%。Abstract 的措辞是合理的背景设定。

**[AGREE] R1-M5: >7B 局限影响可能更大**
同意。Frontier models（>7B）可能有不同的 collapse dynamics。Limitations 中的提及过于简短。

---

### 总体评估

R1 和我的评分一致：**Overall 3.0 (Findings)**。

在 Must-Fix 问题上，我和 R1 的核心判断一致：**cross-architecture scope 是最大问题**（R1-N2 = 我的 N1+N2）。我们的分歧主要在严重程度判定上：

| R1 判定 | 我的判定 | 问题 |
|---------|---------|------|
| Must-Fix | Should-Fix | N1 统计功效（有多方法交叉验证缓解） |
| Must-Fix | Must-Fix | N2 跨架构 scope（完全同意） |
| Must-Fix | Should-Fix | N3 FPR 控制（论文透明承认，是 comparative finding 而非 absolute claim） |
| Must-Fix | Should-Fix | N4 幂律拟合（定性结论有支撑，问题在于呈现方式） |

R1 的审稿整体严谨，事实引用准确，多数批评有据。唯一需要纠正的是 W3 中关于 partial correlation "方向矛盾" 的说法——§5 的 partial correlation 结果实际上支持而非反驳论文的 Granger precedence claim。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。核心判断：与 R1 在最终评分（3.0 Findings）上一致，在 cross-architecture scope 问题上完全同意（Must-Fix），但在统计功效（N1）、FPR 控制（N3）和幂律拟合（N4）的严重程度上有分歧——我认为这三项是 Should-Fix 而非 Must-Fix，因为论文有部分缓解证据（specification curve 交叉验证、透明的 CI 报告、定性结论的稳健性）。对 R1-W3 partial correlation 的"方向矛盾"说法提出了纠正：§5 的 partial correlation 结果实际支持论文的 Granger precedence claim。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1324 · 2026-05-24T23:07:57.151799+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1325 · 2026-05-24T23:07:57.152357+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-24T23:08:00.416606+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1327 · 2026-05-24T23:08:00.868804+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1328 · 2026-05-24T23:08:00.869131+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1329 · 2026-05-24T23:08:01.923171+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-24T22:50:38.305431+00:00\", \"completed_at\": \"2026-05-24T22:53:48.458020+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 3\", \"message\": \"Figure 2 (Method sensitivity bar chart): legend 文字偏小（约 6pt），5 种方法的标签在 150dpi 渲染下已接近可读性边界；建议增大 legend fontsize 或移入 caption\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"Figure 4 (Metric trajectories): 4 个子图纵向堆叠，每个子图的 axis labels 和 tick labels 非常小（估计 <7pt），审稿人需要放大才能阅读具体数值\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"Page 5 整体有 3 个 display items（Fig 4 + Fig 5 + Table 1），视觉密度较高，与 page 2 的纯文本形成较大节奏反差\"}, {\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"Figure 6 (Specification curve): 下半部分 specification indicator panel 的标签文字极小且密集排列，x 轴标签辨识度低\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"整页纯文本（Related Work），无任何 display item 穿插。虽然 Related Work 性质上不需要图表，但如果能将部分内容精简，可改善整体视觉节奏\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 5 (Cascade onset): 图幅较小，曲线细节（dashed fitted boundary vs solid curve）在小尺寸下区分度有限\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 8 (Cross-architecture): faded bars（non-confirming conditions）对比度较低，灰度打印时可能与背景难以区分\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 9 (Intervention): 双面板 (a)(b) 布局清晰，但 y 轴标签 \\\"Token entropy\\\" 和 \\\"Perplexity\\\" 字号偏小\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Table 2: booktabs 风格正确，数值精度一致（1 位小数），最优值未见加粗标注——建议对 best FPR-TPR trade-off 行加粗\"}, {\"severity\": \"info\", \"dimension\": \"page 12\", \"message\": \"Figure 10 (Appendix, Pythia-1.4B phase diagram): 热力图色阶与 Figure 1 一致，颜色语义连贯\"}, {\"severity\": \"info\", \"dimension\": \"pages 10-16\", \"message\": \"Appendix 表格（Tables 3-17）均使用 booktabs 风格，格式统一，数值精度一致\"}], \"counts\": {\"critical\": 0, \"warning\": 4, \"i
…[truncated 48 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 1330 · 2026-05-24T23:08:01.923624+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-24T23:08:02.225604+00:00_

1	issues:
2	# ============================================================
3	# Round 1-11 历史 resolved — 保留跨轮次记录
4	# ============================================================
5	- id: "R1-N1"
6	  summary: "Ground-truth pairs 定义存在循环论证"
7	  category: method
8	  severity: critical
9	  status: resolved
10	  first_raised_round: 1
11	  last_seen_round: 1
12	  resolution: "Effect-size GT 重定义完成。"
13	  resolution_round: 1
14	
15	- id: "R1-N2"
16	  summary: "FPR=0% 标定仅基于单 seed"
17	  category: method
18	  severity: critical
19	  status: resolved
20	  first_raised_round: 1
21	  last_seen_round: 1
22	  resolution: "α=0.0 三 seed FPR 验证完成。"
23	  resolution_round: 1
24	
25	- id: "R1-N3"
26	  summary: "α=0.50 和 α=0.75 仅 1 seed"
27	  category: experiment
28	  severity: critical
29	  status: resolved
30	  first_raised_round: 1
31	  last_seen_round: 1
32	  resolution: "Multi-seed 补充完成。"
33	  resolution_round: 1
34	
35	- id: "R2-N1"
36	  summary: "核心方法论为计量经济学已有知识的直接迁移，新颖性有限"
37	  category: framing
38	  severity: critical
39	  status: resolved
40	  first_raised_round: 1
41	  last_seen_round: 2
42	  resolution: "Round 1 三层定位 reframe 完成。"
43	  resolution_round: 1
44	
45	- id: "R2-N2"
46	  summary: "α=0.75 multi-seed 实验未完成 + Appendix A 缺失"
47	  category: experiment
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 1
51	  last_seen_round: 1
52	  resolution: "完成。"
53	  resolution_round: 1
54	
55	- id: "R2-N3"
56	  summary: "实验规模过窄"
57	  category: experiment
58	  severity: critical
59	  status: resolved
60	  first_raised_round: 1
61	  last_seen_round: 1
62	  resolution: "跨架构验证已扩展至 15 model-seed 组合。"
63	  resolution_round: 1
64	
65	- id: "R1-W1"
66	  summary: "Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致"
67	  category: writing
68	  severity: warning
69	  status: resolved
70	  first_raised_round: 1
71	  last_seen_round: 2
72	  resolution: "核心修复完成。"
73	  resolution_round: 1
74	
75	- id: "R1-W2"
76	  summary: "PermG 缺少 power analysis"
77	  category: metho
…[truncated 31581 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1332 · 2026-05-24T23:12:35.780504+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distrib_canary_collapse",
  "issues_yaml": "issues:\n# ============================================================\n# Round 1-11 历史 resolved — 保留跨轮次记录\n# ============================================================\n- id: \"R1-N1\"\n  summary: \"Ground-truth pairs 定义存在循环论证\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Effect-size GT 重定义完成。\"\n  resolution_round: 1\n\n- id: \"R1-N2\"\n  summary: \"FPR=0% 标定仅基于单 seed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"α=0.0 三 seed FPR 验证完成。\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"α=0.50 和 α=0.75 仅 1 seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Multi-seed 补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"核心方法论为计量经济学已有知识的直接迁移，新颖性有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Round 1 三层定位 reframe 完成。\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"α=0.75 multi-seed 实验未完成 + Appendix A 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"实验规模过窄\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"跨架构验证已扩展至 15 model-seed 组合。\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"核心修复完成。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"PermG 缺少 power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix N power analysis 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"75% spurious-signal rate headline 依赖 underpowered T-Y\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"α=0.75 单 seed borderline 结果不应出现在 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"Toda-Yamamoto 纳入理由表述不充分\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W6\"\n  summary: \"可重复性信息不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"超参补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-W3\"\n  summary: \"Token entropy canary 仅在 α=1.0 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"缺少独立 Limitations section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W5\"\n  summary: \"缺少 AI Writing Disclosure\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"缺少 canary→perplexity 为何 spurious 的深入解释\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF1\"\n  summary: \"遗漏 Granger & Newbold (1974)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF2\"\n  summary: \"遗漏 Hataya et al. (2023) 和 Seddik et al. (2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W1-old\"\n  summary: \"Citation key chen2025scales 与实际作者不匹配\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"F2-W3\"\n  summary: \"Section 3 承诺的三项附录内容缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"附录内容补充完成。\"\n  resolution_round: 3\n\n- id: \"F2-W8\"\n  summary: \"格式不合规：未使用 ACL 模板\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"ACL 模板迁移完成。\"\n  resolution_round: 2\n\n- id: \"F2-REF1\"\n  summary: \"遗漏 arXiv:2502.15654\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF1\"\n  summary: \"遗漏 arXiv:2602.10531\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF2\"\n  summary: \"遗漏 arXiv:2505.19046\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF3\"\n  summary: \"遗漏 arXiv:2510.16657\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF5\"\n  summary: \"Appendix H CUSUM 未引用 Page (1954)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F4-REF1\"\n  summary: \"遗漏 Truong & Truong (2026)\"\n  category: reference\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"引用已添加并在 §1/§2 讨论。\"\n  resolution_round: 6\n\n- id: \"F4-REF3\"\n  summary: \"遗漏 Benjamini & Yekutieli (2001)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§4 现引用 benjamini2001control。\"\n  resolution_round: 5\n\n- id: \"F2-REF3\"\n  summary: \"Dakos et al. (2012) + Schreiber (2000) + Phipson & Smyth (2010) 在 bib 中但正文未引用\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"引用补充完成。\"\n  resolution_round: 4\n\n- id: \"F6-W2\"\n  summary: \"页数可能超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"R8 PDF 审查确认主体 8 页合规。\"\n  resolution_round: 8\n\n- id: \"F2-W6b\"\n  summary: \"'Methodological pitfalls' 有 straw-man 倾向\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  resolution: \"全文已改为 'design considerations'。R8 fresh review 未再提及。\"\n  resolution_round: 8\n\n- id: \"F5-N2\"\n  summary: \"T=10 统计效力不足(power≈37%), sharp onset 可能是 power artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Power simulation 重写通过。Steepness comparison 写入正文。Dense α 证据额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 5\n  last_seen_round: 9\n\n- id: \"F2-W5\"\n  summary: \"Token entropy → distinct-n 机械耦合 confound 未排除\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Metric structure 分析完成。讨论已添加。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 9\n\n- id: \"F2-W2\"\n  summary: \"Specification curve analysis 定位不精确\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Appendix E 已改称 'systematic robustness analysis'。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F8-C2\"\n  summary: \"Discussion §6 过于简短(~100词)\"\n  category: writing\n  severity: major\n  status: resolved\n  resolution: \"Discussion 扩展至 20 行。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C3\"\n  summary: \"与 Schaeffer et al. (2025) '8 种 collapse 定义' 的关系讨论不充分\"\n  category: framing\n  severity: major\n  status: resolved\n  resolution: \"Schaeffer taxonomy 映射已添加到 related_work.tex。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C1\"\n  summary: \"Du & Tanaka-Ishii (2026) 引用三重错误\"\n  category: reference\n  severity: critical\n  status: resolved\n  resolution: \"§2 已修正。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R9-C1\"\n  summary: \"FPR CI method.tex 内部矛盾\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"FPR=10% MMCT sensitivity analysis 完成。\"\n  resolution_round: 9\n  first_raised_round: 9\n  last_seen_round: 9\n\n- id: \"F8-N1\"\n  summary: \"BH-FDR 在强正回归依赖下适用性讨论不充分\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"PRDS 假设适用性讨论已添加。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 10\n\n- id: \"F8-REF1\"\n  summary: \"遗漏引用：online/continual learning 下 model collapse 检测\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"related_work.tex 已添加 scope 区分。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F2-W11\"\n  summary: \"α_c SE=0.006 低估真实 seed 不确定性\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"被 F2-W4b/F2-W6 的统计基础问题覆盖。\"\n  resolution_round: 11\n  first_raised_round: 2\n  last_seen_round: 10\n\n- id: \"F8-N2\"\n  summary: \"未讨论为何选择经典 permutation Granger 而非 neural Granger causality\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"§4 已添加 T≤25 理由。§2 引用 neural Granger 文献。\"\n  resolution_round: 11\n  first_raised_round: 8\n  last_seen_round: 11\n\n- id: \"R9-REF2\"\n  summary: \"遗漏引用：Steegen et al. (2016) multiverse analysis\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 steegen2016increasing。\"\n  resolution_round: 11\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-REF2\"\n  summary: \"遗漏引用：Mitchell et al. (2023) DetectGPT\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 mitchell2023detectgpt。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-REF4\"\n  summary: \"遗漏引用：Padmakumar et al. (2024)\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 padmakumar2024writing。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n# ============================================================\n# 活跃 issues — Round 14 更新\n# ============================================================\n\n- id: \"F3-J4\"\n  summary: \"PermG FPR 超出 nominal 5%，architecture-dependent\"\n  category: method\n  severity: critical\n  status: in_progress\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 3\n  last_seen_round: 14\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 MF-1。6轮 mild hedging 失败。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方共识 critical。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方共识 critical。null-control 36 pairs 使 FPR 估计本质上不精确。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 列为 Must-Fix（7.4% > 5%, CI [2.1%, 17.9%]），R2 降级为 Should-Fix（论文透明承认，comparative finding 而非 absolute claim，7/9 seeds FPR=0%）。GPT-2 null FPR 50% 在两位 Reviewer 均提及。交叉后分歧保留。\"\n  action_items:\n    - round: 13\n      action: \"增加 null-control seeds 至 ≥12 使 FPR 估计 CI 收窄；或在正文报告保守版边界\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W4b\"\n  summary: \"幂律边界 α_c(T) 拟合基础薄弱\"\n  category: framing\n  severity: critical\n  status: in_progress\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"γ CI [0.64, 2.08] 使幂律模型无区分度预测。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 列为 Must-Fix（3-4 点拟合幂律不可靠），R2 降级为 Should-Fix（定性结论'detection improves with T'有支撑，问题在于 Eq.(2) 的虚假精确感）。交叉后 R2 建议将 Eq.(2) 降级为 'empirical scaling hypothesis'。\"\n  action_items:\n    - round: 14\n      action: \"Eq.(2) 降级为 empirical scaling hypothesis；Figure 1 caption 标注虚线为粗略经验趋势\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W2b\"\n  summary: \"'Detectability landscape' framing 承诺超过交付\"\n  category: framing\n  severity: critical\n  status: in_progress\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 最高共识 Must-Fix。Phase diagram 仅 Pythia-410M + WikiText-103。跨架构仅 α=1.0（4/15 失败）。Abstract 'five families (345M-6.9B)' + 'supports forward detection in the majority of conditions' 给读者系统性多条件验证的误导印象。11/15 = 27% 失败率在统计检测领域值得警惕。R1 建议缩窄标题或补充边界验证。R2 建议 abstract 明确 'at α=1.0 (full replacement)'。\"\n  action_items:\n    - round: 14\n      action: \"Abstract 加 'at α=1.0' 限定；标题考虑加限定语；确保 phase diagram scope 不被误解为跨架构\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W10\"\n  summary: \"Cross-architecture 'coupling preserved' 条件 post-hoc\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 与 F2-W2b 继续合并。GPT-2 medium null FPR 50% 意味着该架构结果不具统计意义。\"\n\n- id: \"R11-N1\"\n  summary: \"统计功率 β=0.66 CI [0.24,0.78] 使检测边界定量解读不可靠\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 列为 Must-Fix（3 seeds/condition，binomial CI [0.25,0.92] 使 phase diagram 每个网格点不可信）。R2 降级为 Should-Fix，理由：sigmoid regression k=15.7/R²=0.969 和 spec curve 1160 configs 提供超越 raw binomial 的统计支撑。交叉后分歧保留但 R2 同意 sample size 是 weakness。\"\n\n- id: \"F2-W7\"\n  summary: \"Intervention 实验薄弱\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方完全一致。N=2 seeds, α=1.0 only, post-hoc 15% threshold。即使作为 PoC 也太薄弱。R2 补充：未与更简单替代方案（如 perplexity threshold）比较，canary-based approach 增量价值不明确。Conclusion 'substantially reduces peak perplexity' 未保留 PoC 限定。\"\n  action_items:\n    - round: 14\n      action: \"降级为 preliminary PoC；Abstract/Conclusion 删除 'substantially'；考虑与 naive baseline 比较\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R12-N1\"\n  summary: \"Design Principle 'formal design rationale' 作为独立贡献 oversells\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R2 认为 formal 呈现暗示过高可靠性。R1 partial rebut：mode amplification 下推导自洽，'Design Principles' 而非 'Theorems' 已较谦逊。但 R1 同意应更明确讨论已知反例（transfer entropy 0/192, first-differencing F=0）。共识：内容非 trivial 但应在正文讨论局限性。\"\n  action_items:\n    - round: 14\n      action: \"正文增加 Design Principles 已知反例和局限性讨论\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-W1\"\n  summary: \"'3%-92%' FPR 范围含失效方法 NaiveXCorr\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: []\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方同意方法敏感性是最强贡献。需在正文区分合理方法与失效方法。\"\n\n- id: \"R11-W2\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 与 R11-N1 交叉。6/8 的 CI [0.25, 0.92] 使 phase diagram 每格的可信度低。\"\n\n- id: \"R10-VIS1\"\n  summary: \"Table 1 / Figure 6 浮动超出 8 页主文边界\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2, visual_check]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [visual_check]\n    - round: 14\n      reviewers: [visual_check]\n      note: \"R14 视觉审查确认主文 0 个 table。实证论文主文应有至少一个核心结果 summary table。\"\n  action_items:\n    - round: 14\n      action: \"在主文中恢复或新增一个核心结果 summary table\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R12-W1\"\n  summary: \"写作信息密度过高，关键 findings 淹没在数字洪流中\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: []\n    - round: 14\n      reviewers: []\n      note: \"R14 未单独提及但视觉审查侧面印证：page 5 有 3 个 display items 视觉密度高。\"\n\n- id: \"R11-FMT1\"\n  summary: \"Abstract 脚注不标准\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n\n- id: \"R11-SYM1\"\n  summary: \"β 符号重用：统计功率 vs 幂律指数\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n\n- id: \"F5-N1\"\n  summary: \"核心方法是计量经济学标准技术的直接移植\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方确认：novelty 来自 method-sensitivity finding 和 phase-diagram framing，非技术方法本身。不可改变的天花板。\"\n\n- id: \"F5-W1\"\n  summary: \"Design Principles 数学深度有限\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n    - round: 5\n      reviewers: [2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 认为 mode amplification 下推导自洽且'Design Principles'表述谦逊。R2 同意 Propositions 4-5 增加严谨性但核心 Assumption 3 较强。反例（transfer entropy 0/192, first-differencing F=0）需讨论。\"\n\n- id: \"F2-W1\"\n  summary: \"α=0.60 sync dip：mechanism unexplained\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方同意 'temporal lag compression' 解释是 post-hoc，无独立证据。若该异常在多 seeds 间一致，排除它引入 selection bias。论文需：(1) 报告异常在不同 seeds 间一致性；(2) 展示保留该点后拟合变化。\"\n  action_items:\n    - round: 14\n      action: \"报告 α=0.60 异常的 cross-seed 一致性；展示含/排该点的拟合对比\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W6\"\n  summary: \"Detection boundary 验证不足\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 与 F2-W4b 合并。排除 α=0.60 后仅 3-4 个 α 值可用于边界拟合。\"\n\n- id: \"R10-MF5\"\n  summary: \"'Five families (345M-6.9B)' 数字自洽性\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R2 指出 11/15 = 27% 失败率。Abstract 'five families (345M-6.9B)' + 'majority of conditions' 对不了解细节的读者（含 AC）构成误导。需注明核心定量结果仅基于 410M。\"\n\n- id: \"R10-SF2\"\n  summary: \"Data accumulation vs replacement paradigm 未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: []\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 Limitations 已覆盖但可进一步展开。\"\n\n- id: \"R10-SF3\"\n  summary: \"单一解码策略需定性讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方同意 temp=1.0 top-k=50 单一配置限制外部效度。Discussion 未充分展开。\"\n\n- id: \"R10-SF4\"\n  summary: \"方法敏感性 '3%-92%' framing\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF5\"\n  summary: \"Bivariate confounding\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1/R2 均提及。训练动态作为共同驱动因素未排除。偏相关分析（控制 generation number）缺失。\"\n\n- id: \"R10-SF6\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF7\"\n  summary: \"3-4 seeds replication power 有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 维持 Must-Fix。R2 降级为 Should-Fix（sigmoid + spec curve 部分弥补）。\"\n\n- id: \"R11-VIS2\"\n  summary: \"Pages 5-6 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n    - round: 12\n      reviewers: [visual_check]\n    - round: 13\n      reviewers: [visual_check]\n    - round: 14\n      reviewers: [visual_check]\n      note: \"R14 视觉审查：page 5 有 3 个 display items（Fig 4 + Fig 5 + Table 1），与 page 2 纯文本反差大。\"\n\n- id: \"F8-W2\"\n  summary: \"Figure 子图内文字偏小\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n    - round: 12\n      reviewers: [visual_check]\n    - round: 13\n      reviewers: [visual_check]\n    - round: 14\n      reviewers: [1, 2, visual_check]\n      note: \"R14 R1 M3 确认 Figure 2 y 轴标签偏小。视觉审查确认 Figures 2/4/6 多处 axis/legend 文字 <7pt。\"\n\n- id: \"R10-REF3\"\n  summary: \"遗漏引用：Runge et al. (2019) PCMCI\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R9-m5\"\n  summary: \"Granger 'precedence' vs 'causality' 术语不一致\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R2 指出 §5 多处 'Granger-precedence claim' 给读者因果性印象。§3.2 disclaimer 容易被忽略。R1 同意 Abstract 'Granger-precedes' 对非专业读者困惑。\"\n\n- id: \"R9-REF1\"\n  summary: \"遗漏引用：Gerstgrasser et al. (2024) data accumulation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-m1\"\n  summary: \"Figure 3 y 轴标签含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m2\"\n  summary: \"Table 2 'x/8' 列含义未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m3\"\n  summary: \"§5.1 前向引用缺上下文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-REF5\"\n  summary: \"遗漏引用：Montgomery SPC\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"F4-REF5\"\n  summary: \"bib first author mismatch: dey2024breaking\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 4\n  last_seen_round: 11\n\n- id: \"F2-W9b\"\n  summary: \"孤立 bib entries\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 同意：Dakos et al. 2012, Bell et al. 2022, Gu et al. 2026, Dakos et al. 2008 在 bib 中但正文未引用。应引用或移除。\"\n\n- id: \"F6-C2\"\n  summary: \"buffa2026entropy 引用标题不匹配\"\n  category: reference\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n\n- id: \"F8-N3\"\n  summary: \"Appendix 关键验证内容应纳入正文\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 认为某些重要附录结果（如 Appendix R FPR 分析）应在主文更充分摘要。R2 部分同意但认为附录广度本身是优势。\"\n\n- id: \"F8-N4\"\n  summary: \"predict-then-verify post-hoc adjustment 嫌疑\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R12-REF1\"\n  summary: \"遗漏引用：Adams & MacKay (2007) Bayesian online changepoint detection\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-REF2\"\n  summary: \"遗漏引用：Papana et al. (2013) / Siggiridou & Kugiumtzis (2016) permutation Granger validation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W2\"\n  summary: \"Eq.1 sigmoid 上界 0.70 选择理由未说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W3\"\n  summary: \"α 采样间隔不均匀（0.10→0.25 跳跃）理由未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W4\"\n  summary: \"Schaeffer et al. 8 种 collapse 定义中本文使用哪种未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R13-W1\"\n  summary: \"MMCT K≥3 共识框架 K 选择缺乏理论最优性证明\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R2 补充 Table 2 数据：K≥2 FPR 38.9%，K≥3 FPR 11.1%/TPR 75%，K≥4 FPR 0%/TPR 25%，K=5 TPR 0%。MMCT 实际工作点仅一个（K=3），部署需先校准 K。\"\n  action_items:\n    - round: 13\n      action: \"补充 K=2,3,4,5 下 MMCT FPR/TPR 对比；或将 MMCT 降级为纯附录内容\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R13-W2\"\n  summary: \"α=0.60 异常排除对幂律拟合的根本性影响\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方同意 post-hoc exclusion 是 selection bias 风险。需报告 cross-seed 一致性和含/排该点的拟合对比。\"\n\n- id: \"R13-W3\"\n  summary: \"跨架构验证仅在 α=1.0 最极端条件进行\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 最高共识 Must-Fix。与 F2-W2b 合并。\"\n\n- id: \"R13-W4\"\n  summary: \"Abstract 'substantially reduces peak perplexity' 超出证据强度\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方完全一致。与 F2-W7 合并。\"\n\n- id: \"R13-W5\"\n  summary: \"偏相关分析（控制 generation number）缺失\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 继续确认。\"\n\n- id: \"R13-REF1\"\n  summary: \"遗漏引用：Dakos et al. (2008, 2012) 早期预警信号核心实证方法论\"\n  category: reference\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 同意 bib 中存在但正文未引用的条目应处理。\"\n\n- id: \"R13-REF2\"\n  summary: \"遗漏引用：Lenton et al. (2008) 气候 tipping elements\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n\n- id: \"R13-REF3\"\n  summary: \"Granger causality 标准局限性（observational equivalence, Lucas critique）未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 补充 observational equivalence 和 time aggregation bias。R2 指出 T=10 仅为推荐长度 10%，短序列 Granger 检验 power 极低。\"\n\n- id: \"R13-VIS1\"\n  summary: \"主文 8 页 0 个 table，所有定量结果表格在 appendix\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [visual_check]\n    - round: 14\n      reviewers: [visual_check]\n      note: \"R14 视觉审查再次确认。Table 2 实际在 page 8（视觉审查确认 booktabs 风格正确），但 MMCT 结果表不属于核心 detection 结果。\"\n\n- id: \"R13-VIS2\"\n  summary: \"前两页无任何 display item，Figure 1 直到第 3 页\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [visual_check]\n    - round: 14\n      reviewers: [visual_check]\n      note: \"R14 视觉审查确认 page 2 整页纯文本。\"\n\n# ============================================================\n# 新 issues — Round 14\n# ============================================================\n\n- id: \"R14-N1\"\n  summary: \"Blind zone：α<0.50 已严重退化但所有检测方法均无信号\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [2]\n      note: \"R2 独有发现。α=0.25 时 distinct-1 已下降约 40%（-58.3±10.9%）但所有五种检测方法均无信号。框架更像 confirmation tool 而非 early warning/prevention tool。Discussion/Limitations 未充分讨论这一根本限制。R1 交叉后完全同意。\"\n  action_items:\n    - round: 14\n      action: \"Discussion/Limitations 增加 blind zone 实际影响的 honest assessment\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R14-W1\"\n  summary: \"MMCT 权重估计噪声未讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 提出。R2 partially agree：Appendix Q 的 weight robustness ablation 提供部分缓解（PermG 在所有方案下排名第一），但应在主文提及。\"\n\n- id: \"R14-W2\"\n  summary: \"Granger 检验在 T=10 短序列上 power 极低\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现：T=10 仅为推荐长度（T≈100）的 10%。Appendix N power simulation 显示 T=10 时 FPR under FDR correction 已 inflated。选择 T=10 作 primary 设置但在此长度上做 Granger 检验存在方法论 tension。与 R13-REF3 交叉。\"\n\n- id: \"R14-M1\"\n  summary: \"bib 格式不一致\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [2]\n      note: \"R2 提出。未详细检查但基本格式要求。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "issues_yaml": "issues:\n# ============================================================\n# Round 1-11 历史 resolved — 保留跨轮次记录\n# ============================================================\n- id: \"R1-N1\"\n  summary: \"Ground-truth pairs 定义存在循环论证\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Effect-size GT 重定义完成。\"\n  resolution_round: 1\n\n- id: \"R1-N2\"\n  summary: \"FPR=0% 标定仅基于单 seed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"α=0.0 三 seed FPR 验证完成。\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"α=0.50 和 α=0.75 仅 1 seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Multi-seed 补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"核心方法论为计量经济学已有知识的直接迁移，新颖性有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Round 1 三层定位 reframe 完成。\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"α=0.75 multi-seed 实验未完成 + Appendix A 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"实验规模过窄\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"跨架构验证已扩展至 15 model-seed 组合。\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"核心修复完成。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"PermG 缺少 power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix N power analysis 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"75% spurious-signal rate headline 依赖 underpowered T-Y\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"α=0.75 单 seed borderline 结果不应出现在 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"Toda-Yamamoto 纳入理由表述不充分\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W6\"\n  summary: \"可重复性信息不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"超参补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-W3\"\n  summary: \"Token entropy canary 仅在 α=1.0 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"缺少独立 Limitations section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W5\"\n  summary: \"缺少 AI Writing Disclosure\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"缺少 canary→perplexity 为何 spurious 的深入解释\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF1\"\n  summary: \"遗漏 Granger & Newbold (1974)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF2\"\n  summary: \"遗漏 Hataya et al. (2023) 和 Seddik et al. (2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W1-old\"\n  summary: \"Citation key chen2025scales 与实际作者不匹配\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"F2-W3\"\n  summary: \"Section 3 承诺的三项附录内容缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"附录内容补充完成。\"\n  resolution_round: 3\n\n- id: \"F2-W8\"\n  summary: \"格式不合规：未使用 ACL 模板\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"ACL 模板迁移完成。\"\n  resolution_round: 2\n\n- id: \"F2-REF1\"\n  summary: \"遗漏 arXiv:2502.15654\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF1\"\n  summary: \"遗漏 arXiv:2602.10531\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF2\"\n  summary: \"遗漏 arXiv:2505.19046\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF3\"\n  summary: \"遗漏 arXiv:2510.16657\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF5\"\n  summary: \"Appendix H CUSUM 未引用 Page (1954)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F4-REF1\"\n  summary: \"遗漏 Truong & Truong (2026)\"\n  category: reference\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"引用已添加并在 §1/§2 讨论。\"\n  resolution_round: 6\n\n- id: \"F4-REF3\"\n  summary: \"遗漏 Benjamini & Yekutieli (2001)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§4 现引用 benjamini2001control。\"\n  resolution_round: 5\n\n- id: \"F2-REF3\"\n  summary: \"Dakos et al. (2012) + Schreiber (2000) + Phipson & Smyth (2010) 在 bib 中但正文未引用\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"引用补充完成。\"\n  resolution_round: 4\n\n- id: \"F6-W2\"\n  summary: \"页数可能超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"R8 PDF 审查确认主体 8 页合规。\"\n  resolution_round: 8\n\n- id: \"F2-W6b\"\n  summary: \"'Methodological pitfalls' 有 straw-man 倾向\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  resolution: \"全文已改为 'design considerations'。R8 fresh review 未再提及。\"\n  resolution_round: 8\n\n- id: \"F5-N2\"\n  summary: \"T=10 统计效力不足(power≈37%), sharp onset 可能是 power artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Power simulation 重写通过。Steepness comparison 写入正文。Dense α 证据额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 5\n  last_seen_round: 9\n\n- id: \"F2-W5\"\n  summary: \"Token entropy → distinct-n 机械耦合 confound 未排除\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Metric structure 分析完成。讨论已添加。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 9\n\n- id: \"F2-W2\"\n  summary: \"Specification curve analysis 定位不精确\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Appendix E 已改称 'systematic robustness analysis'。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F8-C2\"\n  summary: \"Discussion §6 过于简短(~100词)\"\n  category: writing\n  severity: major\n  status: resolved\n  resolution: \"Discussion 扩展至 20 行。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C3\"\n  summary: \"与 Schaeffer et al. (2025) '8 种 collapse 定义' 的关系讨论不充分\"\n  category: framing\n  severity: major\n  status: resolved\n  resolution: \"Schaeffer taxonomy 映射已添加到 related_work.tex。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C1\"\n  summary: \"Du & Tanaka-Ishii (2026) 引用三重错误\"\n  category: reference\n  severity: critical\n  status: resolved\n  resolution: \"§2 已修正。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R9-C1\"\n  summary: \"FPR CI method.tex 内部矛盾\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"FPR=10% MMCT sensitivity analysis 完成。\"\n  resolution_round: 9\n  first_raised_round: 9\n  last_seen_round: 9\n\n- id: \"F8-N1\"\n  summary: \"BH-FDR 在强正回归依赖下适用性讨论不充分\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"PRDS 假设适用性讨论已添加。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 10\n\n- id: \"F8-REF1\"\n  summary: \"遗漏引用：online/continual learning 下 model collapse 检测\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"related_work.tex 已添加 scope 区分。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F2-W11\"\n  summary: \"α_c SE=0.006 低估真实 seed 不确定性\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"被 F2-W4b/F2-W6 的统计基础问题覆盖。\"\n  resolution_round: 11\n  first_raised_round: 2\n  last_seen_round: 10\n\n- id: \"F8-N2\"\n  summary: \"未讨论为何选择经典 permutation Granger 而非 neural Granger causality\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"§4 已添加 T≤25 理由。§2 引用 neural Granger 文献。\"\n  resolution_round: 11\n  first_raised_round: 8\n  last_seen_round: 11\n\n- id: \"R9-REF2\"\n  summary: \"遗漏引用：Steegen et al. (2016) multiverse analysis\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 steegen2016increasing。\"\n  resolution_round: 11\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-REF2\"\n  summary: \"遗漏引用：Mitchell et al. (2023) DetectGPT\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 mitchell2023detectgpt。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-REF4\"\n  summary: \"遗漏引用：Padmakumar et al. (2024)\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 padmakumar2024writing。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n# ============================================================\n# 活跃 issues — Round 14 更新\n# ============================================================\n\n- id: \"F3-J4\"\n  summary: \"PermG FPR 超出 nominal 5%，architecture-dependent\"\n  category: method\n  severity: critical\n  status: in_progress\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 3\n  last_seen_round: 14\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 MF-1。6轮 mild hedging 失败。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 双方共识 critical。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 双方共识 critical。null-control 36 pairs 使 FPR 估计本质上不精确。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 列为 Must-Fix（7.4% > 5%, CI [2.1%, 17.9%]），R2 降级为 Should-Fix（论文透明承认，comparative finding 而非 absolute claim，7/9 seeds FPR=0%）。GPT-2 null FPR 50% 在两位 Reviewer 均提及。交叉后分歧保留。\"\n  action_items:\n    - round: 13\n      action: \"增加 null-control seeds 至 ≥12 使 FPR 估计 CI 收窄；或在正文报告保守版边界\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W4b\"\n  summary: \"幂律边界 α_c(T) 拟合基础薄弱\"\n  category: framing\n  severity: critical\n  status: in_progress\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n      note: \"γ CI [0.64, 2.08] 使幂律模型无区分度预测。\"\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 列为 Must-Fix（3-4 点拟合幂律不可靠），R2 降级为 Should-Fix（定性结论'detection improves with T'有支撑，问题在于 Eq.(2) 的虚假精确感）。交叉后 R2 建议将 Eq.(2) 降级为 'empirical scaling hypothesis'。\"\n  action_items:\n    - round: 14\n      action: \"Eq.(2) 降级为 empirical scaling hypothesis；Figure 1 caption 标注虚线为粗略经验趋势\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W2b\"\n  summary: \"'Detectability landscape' framing 承诺超过交付\"\n  category: framing\n  severity: critical\n  status: in_progress\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 最高共识 Must-Fix。Phase diagram 仅 Pythia-410M + WikiText-103。跨架构仅 α=1.0（4/15 失败）。Abstract 'five families (345M-6.9B)' + 'supports forward detection in the majority of conditions' 给读者系统性多条件验证的误导印象。11/15 = 27% 失败率在统计检测领域值得警惕。R1 建议缩窄标题或补充边界验证。R2 建议 abstract 明确 'at α=1.0 (full replacement)'。\"\n  action_items:\n    - round: 14\n      action: \"Abstract 加 'at α=1.0' 限定；标题考虑加限定语；确保 phase diagram scope 不被误解为跨架构\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W10\"\n  summary: \"Cross-architecture 'coupling preserved' 条件 post-hoc\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 与 F2-W2b 继续合并。GPT-2 medium null FPR 50% 意味着该架构结果不具统计意义。\"\n\n- id: \"R11-N1\"\n  summary: \"统计功率 β=0.66 CI [0.24,0.78] 使检测边界定量解读不可靠\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 列为 Must-Fix（3 seeds/condition，binomial CI [0.25,0.92] 使 phase diagram 每个网格点不可信）。R2 降级为 Should-Fix，理由：sigmoid regression k=15.7/R²=0.969 和 spec curve 1160 configs 提供超越 raw binomial 的统计支撑。交叉后分歧保留但 R2 同意 sample size 是 weakness。\"\n\n- id: \"F2-W7\"\n  summary: \"Intervention 实验薄弱\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 2\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方完全一致。N=2 seeds, α=1.0 only, post-hoc 15% threshold。即使作为 PoC 也太薄弱。R2 补充：未与更简单替代方案（如 perplexity threshold）比较，canary-based approach 增量价值不明确。Conclusion 'substantially reduces peak perplexity' 未保留 PoC 限定。\"\n  action_items:\n    - round: 14\n      action: \"降级为 preliminary PoC；Abstract/Conclusion 删除 'substantially'；考虑与 naive baseline 比较\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R12-N1\"\n  summary: \"Design Principle 'formal design rationale' 作为独立贡献 oversells\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R2 认为 formal 呈现暗示过高可靠性。R1 partial rebut：mode amplification 下推导自洽，'Design Principles' 而非 'Theorems' 已较谦逊。但 R1 同意应更明确讨论已知反例（transfer entropy 0/192, first-differencing F=0）。共识：内容非 trivial 但应在正文讨论局限性。\"\n  action_items:\n    - round: 14\n      action: \"正文增加 Design Principles 已知反例和局限性讨论\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R11-W1\"\n  summary: \"'3%-92%' FPR 范围含失效方法 NaiveXCorr\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: []\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方同意方法敏感性是最强贡献。需在正文区分合理方法与失效方法。\"\n\n- id: \"R11-W2\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 与 R11-N1 交叉。6/8 的 CI [0.25, 0.92] 使 phase diagram 每格的可信度低。\"\n\n- id: \"R10-VIS1\"\n  summary: \"Table 1 / Figure 6 浮动超出 8 页主文边界\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2, visual_check]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [visual_check]\n    - round: 14\n      reviewers: [visual_check]\n      note: \"R14 视觉审查确认主文 0 个 table。实证论文主文应有至少一个核心结果 summary table。\"\n  action_items:\n    - round: 14\n      action: \"在主文中恢复或新增一个核心结果 summary table\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R12-W1\"\n  summary: \"写作信息密度过高，关键 findings 淹没在数字洪流中\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: []\n    - round: 14\n      reviewers: []\n      note: \"R14 未单独提及但视觉审查侧面印证：page 5 有 3 个 display items 视觉密度高。\"\n\n- id: \"R11-FMT1\"\n  summary: \"Abstract 脚注不标准\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n\n- id: \"R11-SYM1\"\n  summary: \"β 符号重用：统计功率 vs 幂律指数\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n\n- id: \"F5-N1\"\n  summary: \"核心方法是计量经济学标准技术的直接移植\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n    - round: 5\n      reviewers: [1, 2]\n    - round: 6\n      reviewers: [1, 2]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 9\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方确认：novelty 来自 method-sensitivity finding 和 phase-diagram framing，非技术方法本身。不可改变的天花板。\"\n\n- id: \"F5-W1\"\n  summary: \"Design Principles 数学深度有限\"\n  category: framing\n  severity: major\n  status: open\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n    - round: 5\n      reviewers: [2]\n    - round: 6\n      reviewers: [1]\n    - round: 8\n      reviewers: [1, 2]\n    - round: 10\n      reviewers: [1, 2]\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 认为 mode amplification 下推导自洽且'Design Principles'表述谦逊。R2 同意 Propositions 4-5 增加严谨性但核心 Assumption 3 较强。反例（transfer entropy 0/192, first-differencing F=0）需讨论。\"\n\n- id: \"F2-W1\"\n  summary: \"α=0.60 sync dip：mechanism unexplained\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方同意 'temporal lag compression' 解释是 post-hoc，无独立证据。若该异常在多 seeds 间一致，排除它引入 selection bias。论文需：(1) 报告异常在不同 seeds 间一致性；(2) 展示保留该点后拟合变化。\"\n  action_items:\n    - round: 14\n      action: \"报告 α=0.60 异常的 cross-seed 一致性；展示含/排该点的拟合对比\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"F2-W6\"\n  summary: \"Detection boundary 验证不足\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 与 F2-W4b 合并。排除 α=0.60 后仅 3-4 个 α 值可用于边界拟合。\"\n\n- id: \"R10-MF5\"\n  summary: \"'Five families (345M-6.9B)' 数字自洽性\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R2 指出 11/15 = 27% 失败率。Abstract 'five families (345M-6.9B)' + 'majority of conditions' 对不了解细节的读者（含 AC）构成误导。需注明核心定量结果仅基于 410M。\"\n\n- id: \"R10-SF2\"\n  summary: \"Data accumulation vs replacement paradigm 未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 12\n      reviewers: []\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 Limitations 已覆盖但可进一步展开。\"\n\n- id: \"R10-SF3\"\n  summary: \"单一解码策略需定性讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方同意 temp=1.0 top-k=50 单一配置限制外部效度。Discussion 未充分展开。\"\n\n- id: \"R10-SF4\"\n  summary: \"方法敏感性 '3%-92%' framing\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF5\"\n  summary: \"Bivariate confounding\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1/R2 均提及。训练动态作为共同驱动因素未排除。偏相关分析（控制 generation number）缺失。\"\n\n- id: \"R10-SF6\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF7\"\n  summary: \"3-4 seeds replication power 有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 维持 Must-Fix。R2 降级为 Should-Fix（sigmoid + spec curve 部分弥补）。\"\n\n- id: \"R11-VIS2\"\n  summary: \"Pages 5-6 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n    - round: 12\n      reviewers: [visual_check]\n    - round: 13\n      reviewers: [visual_check]\n    - round: 14\n      reviewers: [visual_check]\n      note: \"R14 视觉审查：page 5 有 3 个 display items（Fig 4 + Fig 5 + Table 1），与 page 2 纯文本反差大。\"\n\n- id: \"F8-W2\"\n  summary: \"Figure 子图内文字偏小\"\n  category: format\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 14\n  mentions:\n    - round: 11\n      reviewers: [visual_check]\n    - round: 12\n      reviewers: [visual_check]\n    - round: 13\n      reviewers: [visual_check]\n    - round: 14\n      reviewers: [1, 2, visual_check]\n      note: \"R14 R1 M3 确认 Figure 2 y 轴标签偏小。视觉审查确认 Figures 2/4/6 多处 axis/legend 文字 <7pt。\"\n\n- id: \"R10-REF3\"\n  summary: \"遗漏引用：Runge et al. (2019) PCMCI\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R9-m5\"\n  summary: \"Granger 'precedence' vs 'causality' 术语不一致\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R2 指出 §5 多处 'Granger-precedence claim' 给读者因果性印象。§3.2 disclaimer 容易被忽略。R1 同意 Abstract 'Granger-precedes' 对非专业读者困惑。\"\n\n- id: \"R9-REF1\"\n  summary: \"遗漏引用：Gerstgrasser et al. (2024) data accumulation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-m1\"\n  summary: \"Figure 3 y 轴标签含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m2\"\n  summary: \"Table 2 'x/8' 列含义未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m3\"\n  summary: \"§5.1 前向引用缺上下文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-REF5\"\n  summary: \"遗漏引用：Montgomery SPC\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"F4-REF5\"\n  summary: \"bib first author mismatch: dey2024breaking\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 4\n  last_seen_round: 11\n\n- id: \"F2-W9b\"\n  summary: \"孤立 bib entries\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 2\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 同意：Dakos et al. 2012, Bell et al. 2022, Gu et al. 2026, Dakos et al. 2008 在 bib 中但正文未引用。应引用或移除。\"\n\n- id: \"F6-C2\"\n  summary: \"buffa2026entropy 引用标题不匹配\"\n  category: reference\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n\n- id: \"F8-N3\"\n  summary: \"Appendix 关键验证内容应纳入正文\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 认为某些重要附录结果（如 Appendix R FPR 分析）应在主文更充分摘要。R2 部分同意但认为附录广度本身是优势。\"\n\n- id: \"F8-N4\"\n  summary: \"predict-then-verify post-hoc adjustment 嫌疑\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R12-REF1\"\n  summary: \"遗漏引用：Adams & MacKay (2007) Bayesian online changepoint detection\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-REF2\"\n  summary: \"遗漏引用：Papana et al. (2013) / Siggiridou & Kugiumtzis (2016) permutation Granger validation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W2\"\n  summary: \"Eq.1 sigmoid 上界 0.70 选择理由未说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W3\"\n  summary: \"α 采样间隔不均匀（0.10→0.25 跳跃）理由未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W4\"\n  summary: \"Schaeffer et al. 8 种 collapse 定义中本文使用哪种未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R13-W1\"\n  summary: \"MMCT K≥3 共识框架 K 选择缺乏理论最优性证明\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R2 补充 Table 2 数据：K≥2 FPR 38.9%，K≥3 FPR 11.1%/TPR 75%，K≥4 FPR 0%/TPR 25%，K=5 TPR 0%。MMCT 实际工作点仅一个（K=3），部署需先校准 K。\"\n  action_items:\n    - round: 13\n      action: \"补充 K=2,3,4,5 下 MMCT FPR/TPR 对比；或将 MMCT 降级为纯附录内容\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R13-W2\"\n  summary: \"α=0.60 异常排除对幂律拟合的根本性影响\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方同意 post-hoc exclusion 是 selection bias 风险。需报告 cross-seed 一致性和含/排该点的拟合对比。\"\n\n- id: \"R13-W3\"\n  summary: \"跨架构验证仅在 α=1.0 最极端条件进行\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 最高共识 Must-Fix。与 F2-W2b 合并。\"\n\n- id: \"R13-W4\"\n  summary: \"Abstract 'substantially reduces peak perplexity' 超出证据强度\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方完全一致。与 F2-W7 合并。\"\n\n- id: \"R13-W5\"\n  summary: \"偏相关分析（控制 generation number）缺失\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 继续确认。\"\n\n- id: \"R13-REF1\"\n  summary: \"遗漏引用：Dakos et al. (2008, 2012) 早期预警信号核心实证方法论\"\n  category: reference\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 同意 bib 中存在但正文未引用的条目应处理。\"\n\n- id: \"R13-REF2\"\n  summary: \"遗漏引用：Lenton et al. (2008) 气候 tipping elements\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n\n- id: \"R13-REF3\"\n  summary: \"Granger causality 标准局限性（observational equivalence, Lucas critique）未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [2]\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 补充 observational equivalence 和 time aggregation bias。R2 指出 T=10 仅为推荐长度 10%，短序列 Granger 检验 power 极低。\"\n\n- id: \"R13-VIS1\"\n  summary: \"主文 8 页 0 个 table，所有定量结果表格在 appendix\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [visual_check]\n    - round: 14\n      reviewers: [visual_check]\n      note: \"R14 视觉审查再次确认。Table 2 实际在 page 8（视觉审查确认 booktabs 风格正确），但 MMCT 结果表不属于核心 detection 结果。\"\n\n- id: \"R13-VIS2\"\n  summary: \"前两页无任何 display item，Figure 1 直到第 3 页\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n    - round: 13\n      reviewers: [visual_check]\n    - round: 14\n      reviewers: [visual_check]\n      note: \"R14 视觉审查确认 page 2 整页纯文本。\"\n\n# ============================================================\n# 新 issues — Round 14\n# ============================================================\n\n- id: \"R14-N1\"\n  summary: \"Blind zone：α<0.50 已严重退化但所有检测方法均无信号\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [2]\n      note: \"R2 独有发现。α=0.25 时 distinct-1 已下降约 40%（-58.3±10.9%）但所有五种检测方法均无信号。框架更像 confirmation tool 而非 early warning/prevention tool。Discussion/Limitations 未充分讨论这一根本限制。R1 交叉后完全同意。\"\n  action_items:\n    - round: 14\n      action: \"Discussion/Limitations 增加 blind zone 实际影响的 honest assessment\"\n      assigned_to: paper_agent\n      status: open\n\n- id: \"R14-W1\"\n  summary: \"MMCT 权重估计噪声未讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 提出。R2 partially agree：Appendix Q 的 weight robustness ablation 提供部分缓解（PermG 在所有方案下排名第一），但应在主文提及。\"\n\n- id: \"R14-W2\"\n  summary: \"Granger 检验在 T=10 短序列上 power 极低\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R2 发现：T=10 仅为推荐长度（T≈100）的 10%。Appendix N power simulation 显示 T=10 时 FPR under FDR correction 已 inflated。选择 T=10 作 primary 设置但在此长度上做 Granger 检验存在方法论 tension。与 R13-REF3 交叉。\"\n\n- id: \"R14-M1\"\n  summary: \"bib 格式不一致\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [2]\n      note: \"R2 提出。未详细检查但基本格式要求。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1333 · 2026-05-24T23:12:35.984137+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml\", \"bytes\": 31791}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 203
}
```

</details>

---


### Tool call

_source line 1334 · 2026-05-24T23:15:20.194641+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 14 审稿报告\n\n**Venue**: EMNLP 2026 (via ARR)\n**论文**: Characterizing the Detectability Landscape of LLM-Generated Text in Iterative Training\n**Reviewers**: R1（方法严谨性 + 统计基础）, R2（新颖性 + 完整性 + scope 校准）\n**轮次**: Round 14（fresh review，无上轮记忆）\n**交叉回应**: 双向完成。R1 对 R2 共 7 项回应（5 AGREE, 2 REBUT）；R2 对 R1 共 12 项回应（7 AGREE, 3 PARTIALLY AGREE, 2 REBUT）。\n\n---\n\n## Summary\n\n本文提出基于 canary metrics（token entropy, distinct-n）的统计检测框架，用于在迭代训练中检测 LLM 输出分布退化（model collapse）。核心贡献包括：(1) 方法敏感性比较（五种检测方法的 FPR 从 3% 到 92%）；(2) 基于 Pythia-410M + WikiText-103 的 detection phase diagram；(3) Design Principles（entropy 先于 diversity 响应）的形式化推导；(4) Granger precedence 分析；(5) 概念验证级 intervention 实验。\n\n论文在方法敏感性发现和 phase diagram 概念上有价值，但 **定量声明系统性地超出证据支撑范围**：phase diagram 仅基于单一架构/数据集，跨架构验证仅在最极端条件（α=1.0）进行且仍有 27% 失败率，统计功效不足（3 seeds/condition），intervention 实验仅为 N=2 的概念验证。\n\n---\n\n## Strengths\n\n**S1: 方法敏感性发现（最强贡献）**\n五种检测方法的 FPR 从 3% 到 92% 的发现——展示了统计方法选择对 model collapse 检测结论的决定性影响——是论文最有价值的贡献。这一发现具有直接的实践指导意义，且在 specification curve analysis（1,160 configurations, Figure 6）中得到了系统验证。两位 Reviewer 一致认可。\n\n**S2: 问题定位准确**\n将 model collapse 检测框架化为统计检测问题（需要控制 FPR 的假设检验），而非简单的指标监控，是合理且有价值的学术贡献。\n\n**S3: 附录广度**\n24 个 appendix sections 提供了广泛的 robustness checks（不同 lag orders, FDR 方法, 权重方案, null-control 验证等），为有疑问的审稿人提供了充分的验证渠道。\n\n**S4: 透明报告**\n论文在 §4.5 failure mode taxonomy 中报告了失败条件，在 §5 讨论了 Granger causality 的局限性。这种透明性值得肯定。\n\n**S5: Dose-response 分析**\n§4.3 的 dose-response 分析清楚展示了检测能力随 α 和 T 的变化，sigmoid 拟合（k=15.7, R²=0.969）为 sharp onset 提供了定量支撑。\n\n---\n\n## Weaknesses\n\n### Must-Fix（两位 Reviewer 共识）\n\n**MF-1: 跨架构验证仅在 α=1.0，scope overclaim 严重** [F2-W2b, R13-W3, R10-MF5]\n*（Round 2 首次提出，连续 13 轮未解决）*\n\n这是论文最严重的问题。Phase diagram（Figure 1）——论文的核心定量贡献——仅基于 Pythia-410M + WikiText-103 单一配置。跨架构验证（five families, 345M-6.9B）仅在 α=1.0（100% 合成数据替换）进行。\n\n**α=1.0 是最极端、最容易检测的条件。** 它对 phase diagram 核心过渡区域（α∈[0.45, 0.75]）的泛化性提供零证据。即使在此最有利条件下，4/15 = 27% 的 model-seed 组合检测失败。其中 GPT-2 medium 的 null FPR 高达 50%（Appendix Z.2），意味着该架构上的检测结果不具统计意义。\n\nAbstract 中 \"Cross-architecture evaluation across five model families (345M–6.9B) supports forward detection in the majority of conditions\" 是 technically correct 但 misleading。一个不熟悉细节的读者（包括 AC）会自然理解为多 α 值、多架构的系统验证。\"majority of conditions\" 掩盖了近三分之一的失败率。\n\n**要求**：(1) Abstract 明确标注 \"at α=1.0 (full replacement)\"；(2) 标题考虑加限定语或缩窄 scope；(3) 正文注明核心定量结果（phase diagram, detection boundary）仅基于 Pythia-410M。\n\n---\n\n### Should-Fix\n\n**SF-1: 统计功效不足（3 seeds/condition）** [R11-N1, R11-W2, R10-SF7]\n*（R1 列为 Must-Fix，R2 降级为 Should-Fix——交叉后分歧保留）*\n\n每个 (α, T) condition 仅 3 seeds（8 pairs）。6/8 的 binomial CI 为 [0.25, 0.92]，跨越了从\"偶然\"到\"几乎确定\"的全范围。Phase diagram 每个网格点的定量可信度很低。\n\nR2 指出的缓解因素值得注意：sigmoid regression（k=15.7, R²=0.969）和 specification curve（1,160 configurations）提供了超越 raw binomial 的统计支撑。因此定性结论（存在 sharp onset）有一定基础，但定量边界位置不可靠。\n\n**要求**：在主文中报告每格 CI 宽度，并讨论其对 boundary 精度的影响。理想情况下增加边界区域 seeds 至 ≥5。\n\n**SF-2: FPR 标定偏高且 CI 极宽** [F3-J4]\n*（Round 3 首次提出，连续 12 轮未解决。R1 列为 Must-Fix，R2 降级为 Should-Fix）*\n\nPermG FPR = 7.4%（4/54），CI [2.1%, 17.9%]。MMCT K≥3 的 FPR = 11.1%（6/54）。两者均超出 nominal 5%。GPT-2 null FPR 50% 是架构级失效。\n\nR2 指出的缓解因素：论文的贡献不是声称 PermG 控制在 5%，而是展示它是五种方法中 FPR 最低的（7.4% vs NaiveXCorr 94.4%）。Limitations §2 已明确承认此问题。但 null-control 仅 54 pairs 使得 FPR 估计本质上不精确。\n\n**要求**：增加 null-control seeds 收窄 CI，或在正文中更突出报告 CI 宽度。\n\n**SF-3: 幂律边界拟合数据点不足** [F2-W4b, R13-W2]\n*（Round 2 首次提出，连续 13 轮未解决）*\n\n排除 α=0.60 异常后，幂律边界 α_c(T) = c·T^(-γ) 的拟合仅基于 3-4 个 α 值。γ 的 CI [0.64, 2.08] 跨越了亚线性到超线性的定性分界，不具参数辨识力。论文自己承认 \"the qualitative conclusion is robust to the specific γ value\"，等于默认 γ 的精确值无法确定。\n\nR2 建议将 Eq.(2) 降级为 \"empirical scaling hypothesis\" 而非给出一个看起来精确的公式。Figure 1 中的虚线边界应标注为\"粗略经验趋势\"。\n\n此外，α=0.60 的排除缺乏独立验证。\"Temporal lag compression\" 解释是 post-hoc 的。论文需：(1) 报告该异常在不同 seeds 间的一致性；(2) 展示保留该点后拟合结果的变化。\n\n**要求**：Eq.(2) 降级为 empirical scaling hypothesis；报告 α=0.60 cross-seed 一致性和含/排该点的拟合对比。\n\n**SF-4: Intervention 实验过弱** [F2-W7, R13-W4]\n*（Round 2 首次提出，连续 13 轮未解决）*\n\nN=2 seeds, α=1.0 only, post-hoc 15% threshold（从同一数据确定）。即使作为 Proof of Concept 也太薄弱。两位 Reviewer 完全一致。\n\nR2 补充了一个重要批评：未与更简单替代方案（如 perplexity threshold 或 CUSUM）比较。如果 naive baseline 就能达到类似效果，canary-based approach 的增量价值不明确。\n\nConclusion 中 \"substantially reduces peak perplexity\" 未保留 PoC 限定语。\n\n**要求**：Abstract/Conclusion 将 \"substantially\" 降级为 \"preliminary proof-of-concept\"；考虑添加 naive baseline 比较。\n\n**SF-5: Granger causality 局限讨论不充分** [R10-SF5, R13-W5, R13-REF3]\n\n两位 Reviewer 从不同角度指出同一问题：\n\n(a) **Transfer entropy 0/192 significant pairs**（Appendix F）：如果 canary 真的 \"precedes\" downstream metrics，非线性因果检验应能捕捉到某些信号。论文在 §5 承认无法区分是 nonlinear structure 缺失还是短序列 power 不足，但讨论过于简短。\n\n(b) **T=10 仅为推荐长度 10%**：Granger 检验在短序列上 power 极低。Appendix N 显示 T=10 时 FPR under FDR correction 已 inflated。\n\n(c) **Observational equivalence**：Granger precedence ≠ causation，但 §5 \"Granger-precedence claim\" 等措辞给读者因果性印象。\n\n(d) **Bivariate confounders**：训练动态作为共同驱动因素未排除。偏相关分析（控制 generation number）缺失。\n\nR2 对 R1 关于 \"partial correlation 方向矛盾\" 的纠正是准确的：§5 的 partial correlation 结果（同期减弱、滞后增强）实际上支持论文的 Granger precedence claim。但其他三个维度的局限仍需更充分讨论。\n\n**要求**：Discussion 扩展 Granger 局限讨论；补充 partial correlation（控制 generation number）分析到附录。\n\n**SF-6: Blind zone 限制框架实际适用性** [R14-N1, 新发现]\n\nR2 独有发现，R1 交叉后完全同意。α=0.25 时 distinct-1 已下降约 40%（-58.3±10.9%），但所有五种检测方法均无信号。这意味着：**在框架能检测到 collapse 时（α≈0.50+），下游质量已经严重退化。** 框架更像 confirmation tool（确认已发生的退化）而非 prevention tool（在退化变严重前发出警告）。\n\nDiscussion/Limitations 未充分讨论这一根本限制。\n\n**要求**：Limitations 增加对 blind zone 实际影响的 honest assessment。\n\n**SF-7: Design Principles 形式化呈现与已知反例的讨论缺失** [R12-N1, F5-W1]\n\nDesign Principle 1（entropy 先于 diversity 响应）和 Design Principle 2（diversity 是阈值指示器）在 mode amplification 假设下的推导逻辑自洽。但存在已知反例：transfer entropy 0/192 significant pairs 和 first-differencing 消除 canary→perplexity 关联（F=0, p≈0.99）。\n\nR1 认为 \"Design Principles\" 而非 \"Theorems\" 已是较谦逊表述；R2 认为 formal 呈现仍暗示过高可靠性。交叉后共识：内容非 trivial 但正文应更明确讨论已知反例和局限性。\n\n**要求**：正文增加 Design Principles 已知反例和局限性讨论。\n\n**SF-8: MMCT K 阈值极度敏感** [R13-W1]\n\nTable 2 数据：K≥2 FPR 38.9%（不可接受）；K≥3 FPR 11.1%, TPR 75%（勉强可用）；K≥4 FPR 0%, TPR 25%（power 不足）；K=5 FPR 0%, TPR 0%（完全无用）。MMCT 实际工作点仅一个。使用者需先在 null-control 数据上校准 K，限制即用性。\n\n**要求**：Discussion 讨论 K 校准对实际部署的影响。\n\n---\n\n### Minor Issues\n\n- **M1**: Figure 2 y 轴标签偏小，Figures 4/6 axis/legend 文字 <7pt（视觉审查 + R1 确认）\n- **M2**: bib 格式不一致（R2）\n- **M3**: Abstract \"Granger-precedes\" 对非专业读者可能困惑，建议改为更直白表述\n- **M4**: Granger \"precedence\" vs \"causality\" 术语在全文中仍有不一致\n- **M5**: β 符号重用（统计功率 vs 幂律指数），增加阅读混淆\n- **M6**: bib 中存在但正文未引用的条目（Dakos et al. 2012, Bell et al. 2022, Gu et al. 2026, Dakos et al. 2008），应引用或移除\n- **M7**: >7B 模型局限在 Limitations 中提及过于简短\n- **M8**: 单一解码策略（temp=1.0, top-k=50）限制外部效度，Discussion 未充分展开\n\n---\n\n## Questions\n\n1. α=0.60 non-monotonic dip 在 3 个 seeds 之间是否一致出现？如果仅出现在部分 seeds，排除它的理由更充分；如果一致出现，它可能反映真实的非单调物理过程。\n2. 保留 α=0.60 数据点后幂律拟合的 γ 和 R² 变化多大？\n3. 简单的 perplexity threshold（不依赖 canary metrics）是否也能达到与 intervention 实验类似的效果？\n4. 如果在 α=0.50（而非 1.0）上进行跨架构验证，预期有多少 model families 能通过？\n5. PRDS 假设在该数据上是否经验验证过？\n\n---\n\n## Missing References\n\n以下引用在两位 Reviewer 的交叉回应中被提及：\n- Dakos et al. (2008, 2012) — 早期预警信号核心实证方法论（bib 中存在但正文未引用）\n- Runge et al. (2019) PCMCI — 多变量因果推断\n- Adams & MacKay (2007) — Bayesian online changepoint detection\n- Papana et al. (2013) / Siggiridou & Kugiumtzis (2016) — permutation Granger validation\n- Gerstgrasser et al. (2024) — data accumulation paradigm\n- Lenton et al. (2008) — tipping elements（论文使用 tipping point 类比但未引此奠基工作）\n\n---\n\n## External Review\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（2026-05-24T22:50:38 → 22:53:48）\n\n### Warnings (4)\n1. **Page 3** — Figure 2 legend 文字约 6pt，150dpi 下接近可读性边界\n2. **Page 5** — Figure 4 四个子图 axis/tick labels 非常小（<7pt）\n3. **Page 5** — 3 个 display items（Fig 4 + Fig 5 + Table 1）视觉密度高，与 page 2 纯文本反差大\n4. **Page 6** — Figure 6 下半部分 specification indicator panel 标签极小且密集\n\n### Info (7)\n- Page 2 整页纯文本无 display item\n- Figure 5 小尺寸下 dashed/solid curve 区分度有限\n- Figure 8 faded bars 灰度打印时对比度低\n- Figure 9 y 轴标签字号偏小\n- Table 2 最优值未加粗标注\n- Appendix Figure 10 色阶与 Figure 1 一致（正面）\n- Appendix 表格格式统一（正面）\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings**\n\n两位 Reviewer 独立给出相同评分，交叉回应后维持不变。\n\n**评分理由**：\n\n论文提出了有价值的框架——将 model collapse 检测框架化为需要控制 FPR 的统计检测问题，方法敏感性发现（FPR 3%→92%）具有实践指导意义，phase diagram 概念为该领域提供了有用的组织框架。\n\n但定量声明系统性超出证据支撑：\n- Phase diagram 仅基于 Pythia-410M + WikiText-103，跨架构验证仅在最极端条件 α=1.0 进行\n- Abstract/标题暗示的广度与实际证据严重不匹配\n- 统计功效不足（3 seeds, 8 pairs/cell）使 boundary 精度不可靠\n- Intervention 仅为 N=2 概念验证却使用 \"substantially\" 等强修饰语\n- Blind zone（α<0.50 已退化但无检测信号）限制框架的 early warning 价值\n\n**不可改变的天花板**：核心方法为计量经济学标准技术的移植（Granger, permutation test, BH-FDR），技术新颖性有限。两位 Reviewer 一致认为 novelty 来自 method-sensitivity finding 和 phase-diagram framing，而非方法本身。这是结构性限制。\n\n**Findings 而非 Conference 的关键差距**：如果跨架构验证扩展到 α∈[0.50, 0.75] 的过渡区域，且 intervention 有更充分的比较实验，评分可升至 3.5。当前版本的 scope claim 与证据之间的 gap 是阻止 Conference 接收的主要障碍。\n\n**与前轮比较（基于 issue tracker）**：MF-1（scope overclaim）、SF-2（FPR 标定）、SF-3（幂律拟合）、SF-4（intervention）均从 Round 2-3 首次提出，历经 12-13 轮仍未根本解决。论文在每轮进行了措辞调整（hedging），但核心实验规模未变。这些不是 writing 问题，而是 evidence 问题——无法仅通过文字修改解决。\n\n---\n\n## Detailed Comments\n\n### 两位 Reviewer 的分歧与裁定\n\n| 问题 | R1 判定 | R2 判定 | Director 裁定 |\n|------|---------|---------|---------------|\n| 统计功效 (N1) | Must-Fix | Should-Fix（sigmoid+spec curve 缓解） | Should-Fix — R2 的缓解证据有效 |\n| FPR 标定 (N3) | Must-Fix | Should-Fix（comparative 而非 absolute claim） | Should-Fix — 论文定位合理 |\n| 幂律拟合 (N4) | Must-Fix | Should-Fix（定性结论稳健） | Should-Fix — 但 Eq.(2) 需降级 |\n| Partial correlation | 方向矛盾 | 支持 Granger claim | R2 正确 — 同期减弱+滞后增强是 genuine temporal precedence 的标志 |\n| Design Principles | 形式化合理 | 过度 formal | 中间立场 — 需讨论反例 |\n| Appendix 规模 | 优势 | 应在主文摘要 | R1 正确 — 附录广度是优势，但关键结果需在主文充分摘要 |\n\n### 优先修改建议（按影响力排序）\n\n1. **Abstract/标题 scope 校准** — 最高优先级。明确核心结果基于 Pythia-410M，跨架构验证限于 α=1.0。\n2. **Intervention 降级** — 删除 \"substantially\"，明确 preliminary PoC 定位。\n3. **Blind zone 讨论** — Limitations 增加 α<0.50 检测盲区的 honest assessment。\n4. **Eq.(2) 降级** — 改为 empirical scaling hypothesis。\n5. **Granger 局限扩展** — 补充 partial correlation（控制 generation）、讨论 T=10 power 限制。\n6. **Design Principles 反例** — 正文讨论 transfer entropy null 和 first-differencing null。\n7. **Figure 字号** — Figures 2/4/6 axis labels 增大至 ≥8pt。\n8. **bib 清理** — 未引用条目处理，格式统一。",
  "project": "distrib_canary_collapse",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 14 审稿报告\n\n**Venue**: EMNLP 2026 (via ARR)\n**论文**: Characterizing the Detectability Landscape of LLM-Generated Text in Iterative Training\n**Reviewers**: R1（方法严谨性 + 统计基础）, R2（新颖性 + 完整性 + scope 校准）\n**轮次**: Round 14（fresh review，无上轮记忆）\n**交叉回应**: 双向完成。R1 对 R2 共 7 项回应（5 AGREE, 2 REBUT）；R2 对 R1 共 12 项回应（7 AGREE, 3 PARTIALLY AGREE, 2 REBUT）。\n\n---\n\n## Summary\n\n本文提出基于 canary metrics（token entropy, distinct-n）的统计检测框架，用于在迭代训练中检测 LLM 输出分布退化（model collapse）。核心贡献包括：(1) 方法敏感性比较（五种检测方法的 FPR 从 3% 到 92%）；(2) 基于 Pythia-410M + WikiText-103 的 detection phase diagram；(3) Design Principles（entropy 先于 diversity 响应）的形式化推导；(4) Granger precedence 分析；(5) 概念验证级 intervention 实验。\n\n论文在方法敏感性发现和 phase diagram 概念上有价值，但 **定量声明系统性地超出证据支撑范围**：phase diagram 仅基于单一架构/数据集，跨架构验证仅在最极端条件（α=1.0）进行且仍有 27% 失败率，统计功效不足（3 seeds/condition），intervention 实验仅为 N=2 的概念验证。\n\n---\n\n## Strengths\n\n**S1: 方法敏感性发现（最强贡献）**\n五种检测方法的 FPR 从 3% 到 92% 的发现——展示了统计方法选择对 model collapse 检测结论的决定性影响——是论文最有价值的贡献。这一发现具有直接的实践指导意义，且在 specification curve analysis（1,160 configurations, Figure 6）中得到了系统验证。两位 Reviewer 一致认可。\n\n**S2: 问题定位准确**\n将 model collapse 检测框架化为统计检测问题（需要控制 FPR 的假设检验），而非简单的指标监控，是合理且有价值的学术贡献。\n\n**S3: 附录广度**\n24 个 appendix sections 提供了广泛的 robustness checks（不同 lag orders, FDR 方法, 权重方案, null-control 验证等），为有疑问的审稿人提供了充分的验证渠道。\n\n**S4: 透明报告**\n论文在 §4.5 failure mode taxonomy 中报告了失败条件，在 §5 讨论了 Granger causality 的局限性。这种透明性值得肯定。\n\n**S5: Dose-response 分析**\n§4.3 的 dose-response 分析清楚展示了检测能力随 α 和 T 的变化，sigmoid 拟合（k=15.7, R²=0.969）为 sharp onset 提供了定量支撑。\n\n---\n\n## Weaknesses\n\n### Must-Fix（两位 Reviewer 共识）\n\n**MF-1: 跨架构验证仅在 α=1.0，scope overclaim 严重** [F2-W2b, R13-W3, R10-MF5]\n*（Round 2 首次提出，连续 13 轮未解决）*\n\n这是论文最严重的问题。Phase diagram（Figure 1）——论文的核心定量贡献——仅基于 Pythia-410M + WikiText-103 单一配置。跨架构验证（five families, 345M-6.9B）仅在 α=1.0（100% 合成数据替换）进行。\n\n**α=1.0 是最极端、最容易检测的条件。** 它对 phase diagram 核心过渡区域（α∈[0.45, 0.75]）的泛化性提供零证据。即使在此最有利条件下，4/15 = 27% 的 model-seed 组合检测失败。其中 GPT-2 medium 的 null FPR 高达 50%（Appendix Z.2），意味着该架构上的检测结果不具统计意义。\n\nAbstract 中 \"Cross-architecture evaluation across five model families (345M–6.9B) supports forward detection in the majority of conditions\" 是 technically correct 但 misleading。一个不熟悉细节的读者（包括 AC）会自然理解为多 α 值、多架构的系统验证。\"majority of conditions\" 掩盖了近三分之一的失败率。\n\n**要求**：(1) Abstract 明确标注 \"at α=1.0 (full replacement)\"；(2) 标题考虑加限定语或缩窄 scope；(3) 正文注明核心定量结果（phase diagram, detection boundary）仅基于 Pythia-410M。\n\n---\n\n### Should-Fix\n\n**SF-1: 统计功效不足（3 seeds/condition）** [R11-N1, R11-W2, R10-SF7]\n*（R1 列为 Must-Fix，R2 降级为 Should-Fix——交叉后分歧保留）*\n\n每个 (α, T) condition 仅 3 seeds（8 pairs）。6/8 的 binomial CI 为 [0.25, 0.92]，跨越了从\"偶然\"到\"几乎确定\"的全范围。Phase diagram 每个网格点的定量可信度很低。\n\nR2 指出的缓解因素值得注意：sigmoid regression（k=15.7, R²=0.969）和 specification curve（1,160 configurations）提供了超越 raw binomial 的统计支撑。因此定性结论（存在 sharp onset）有一定基础，但定量边界位置不可靠。\n\n**要求**：在主文中报告每格 CI 宽度，并讨论其对 boundary 精度的影响。理想情况下增加边界区域 seeds 至 ≥5。\n\n**SF-2: FPR 标定偏高且 CI 极宽** [F3-J4]\n*（Round 3 首次提出，连续 12 轮未解决。R1 列为 Must-Fix，R2 降级为 Should-Fix）*\n\nPermG FPR = 7.4%（4/54），CI [2.1%, 17.9%]。MMCT K≥3 的 FPR = 11.1%（6/54）。两者均超出 nominal 5%。GPT-2 null FPR 50% 是架构级失效。\n\nR2 指出的缓解因素：论文的贡献不是声称 PermG 控制在 5%，而是展示它是五种方法中 FPR 最低的（7.4% vs NaiveXCorr 94.4%）。Limitations §2 已明确承认此问题。但 null-control 仅 54 pairs 使得 FPR 估计本质上不精确。\n\n**要求**：增加 null-control seeds 收窄 CI，或在正文中更突出报告 CI 宽度。\n\n**SF-3: 幂律边界拟合数据点不足** [F2-W4b, R13-W2]\n*（Round 2 首次提出，连续 13 轮未解决）*\n\n排除 α=0.60 异常后，幂律边界 α_c(T) = c·T^(-γ) 的拟合仅基于 3-4 个 α 值。γ 的 CI [0.64, 2.08] 跨越了亚线性到超线性的定性分界，不具参数辨识力。论文自己承认 \"the qualitative conclusion is robust to the specific γ value\"，等于默认 γ 的精确值无法确定。\n\nR2 建议将 Eq.(2) 降级为 \"empirical scaling hypothesis\" 而非给出一个看起来精确的公式。Figure 1 中的虚线边界应标注为\"粗略经验趋势\"。\n\n此外，α=0.60 的排除缺乏独立验证。\"Temporal lag compression\" 解释是 post-hoc 的。论文需：(1) 报告该异常在不同 seeds 间的一致性；(2) 展示保留该点后拟合结果的变化。\n\n**要求**：Eq.(2) 降级为 empirical scaling hypothesis；报告 α=0.60 cross-seed 一致性和含/排该点的拟合对比。\n\n**SF-4: Intervention 实验过弱** [F2-W7, R13-W4]\n*（Round 2 首次提出，连续 13 轮未解决）*\n\nN=2 seeds, α=1.0 only, post-hoc 15% threshold（从同一数据确定）。即使作为 Proof of Concept 也太薄弱。两位 Reviewer 完全一致。\n\nR2 补充了一个重要批评：未与更简单替代方案（如 perplexity threshold 或 CUSUM）比较。如果 naive baseline 就能达到类似效果，canary-based approach 的增量价值不明确。\n\nConclusion 中 \"substantially reduces peak perplexity\" 未保留 PoC 限定语。\n\n**要求**：Abstract/Conclusion 将 \"substantially\" 降级为 \"preliminary proof-of-concept\"；考虑添加 naive baseline 比较。\n\n**SF-5: Granger causality 局限讨论不充分** [R10-SF5, R13-W5, R13-REF3]\n\n两位 Reviewer 从不同角度指出同一问题：\n\n(a) **Transfer entropy 0/192 significant pairs**（Appendix F）：如果 canary 真的 \"precedes\" downstream metrics，非线性因果检验应能捕捉到某些信号。论文在 §5 承认无法区分是 nonlinear structure 缺失还是短序列 power 不足，但讨论过于简短。\n\n(b) **T=10 仅为推荐长度 10%**：Granger 检验在短序列上 power 极低。Appendix N 显示 T=10 时 FPR under FDR correction 已 inflated。\n\n(c) **Observational equivalence**：Granger precedence ≠ causation，但 §5 \"Granger-precedence claim\" 等措辞给读者因果性印象。\n\n(d) **Bivariate confounders**：训练动态作为共同驱动因素未排除。偏相关分析（控制 generation number）缺失。\n\nR2 对 R1 关于 \"partial correlation 方向矛盾\" 的纠正是准确的：§5 的 partial correlation 结果（同期减弱、滞后增强）实际上支持论文的 Granger precedence claim。但其他三个维度的局限仍需更充分讨论。\n\n**要求**：Discussion 扩展 Granger 局限讨论；补充 partial correlation（控制 generation number）分析到附录。\n\n**SF-6: Blind zone 限制框架实际适用性** [R14-N1, 新发现]\n\nR2 独有发现，R1 交叉后完全同意。α=0.25 时 distinct-1 已下降约 40%（-58.3±10.9%），但所有五种检测方法均无信号。这意味着：**在框架能检测到 collapse 时（α≈0.50+），下游质量已经严重退化。** 框架更像 confirmation tool（确认已发生的退化）而非 prevention tool（在退化变严重前发出警告）。\n\nDiscussion/Limitations 未充分讨论这一根本限制。\n\n**要求**：Limitations 增加对 blind zone 实际影响的 honest assessment。\n\n**SF-7: Design Principles 形式化呈现与已知反例的讨论缺失** [R12-N1, F5-W1]\n\nDesign Principle 1（entropy 先于 diversity 响应）和 Design Principle 2（diversity 是阈值指示器）在 mode amplification 假设下的推导逻辑自洽。但存在已知反例：transfer entropy 0/192 significant pairs 和 first-differencing 消除 canary→perplexity 关联（F=0, p≈0.99）。\n\nR1 认为 \"Design Principles\" 而非 \"Theorems\" 已是较谦逊表述；R2 认为 formal 呈现仍暗示过高可靠性。交叉后共识：内容非 trivial 但正文应更明确讨论已知反例和局限性。\n\n**要求**：正文增加 Design Principles 已知反例和局限性讨论。\n\n**SF-8: MMCT K 阈值极度敏感** [R13-W1]\n\nTable 2 数据：K≥2 FPR 38.9%（不可接受）；K≥3 FPR 11.1%, TPR 75%（勉强可用）；K≥4 FPR 0%, TPR 25%（power 不足）；K=5 FPR 0%, TPR 0%（完全无用）。MMCT 实际工作点仅一个。使用者需先在 null-control 数据上校准 K，限制即用性。\n\n**要求**：Discussion 讨论 K 校准对实际部署的影响。\n\n---\n\n### Minor Issues\n\n- **M1**: Figure 2 y 轴标签偏小，Figures 4/6 axis/legend 文字 <7pt（视觉审查 + R1 确认）\n- **M2**: bib 格式不一致（R2）\n- **M3**: Abstract \"Granger-precedes\" 对非专业读者可能困惑，建议改为更直白表述\n- **M4**: Granger \"precedence\" vs \"causality\" 术语在全文中仍有不一致\n- **M5**: β 符号重用（统计功率 vs 幂律指数），增加阅读混淆\n- **M6**: bib 中存在但正文未引用的条目（Dakos et al. 2012, Bell et al. 2022, Gu et al. 2026, Dakos et al. 2008），应引用或移除\n- **M7**: >7B 模型局限在 Limitations 中提及过于简短\n- **M8**: 单一解码策略（temp=1.0, top-k=50）限制外部效度，Discussion 未充分展开\n\n---\n\n## Questions\n\n1. α=0.60 non-monotonic dip 在 3 个 seeds 之间是否一致出现？如果仅出现在部分 seeds，排除它的理由更充分；如果一致出现，它可能反映真实的非单调物理过程。\n2. 保留 α=0.60 数据点后幂律拟合的 γ 和 R² 变化多大？\n3. 简单的 perplexity threshold（不依赖 canary metrics）是否也能达到与 intervention 实验类似的效果？\n4. 如果在 α=0.50（而非 1.0）上进行跨架构验证，预期有多少 model families 能通过？\n5. PRDS 假设在该数据上是否经验验证过？\n\n---\n\n## Missing References\n\n以下引用在两位 Reviewer 的交叉回应中被提及：\n- Dakos et al. (2008, 2012) — 早期预警信号核心实证方法论（bib 中存在但正文未引用）\n- Runge et al. (2019) PCMCI — 多变量因果推断\n- Adams & MacKay (2007) — Bayesian online changepoint detection\n- Papana et al. (2013) / Siggiridou & Kugiumtzis (2016) — permutation Granger validation\n- Gerstgrasser et al. (2024) — data accumulation paradigm\n- Lenton et al. (2008) — tipping elements（论文使用 tipping point 类比但未引此奠基工作）\n\n---\n\n## External Review\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**: 已完成（2026-05-24T22:50:38 → 22:53:48）\n\n### Warnings (4)\n1. **Page 3** — Figure 2 legend 文字约 6pt，150dpi 下接近可读性边界\n2. **Page 5** — Figure 4 四个子图 axis/tick labels 非常小（<7pt）\n3. **Page 5** — 3 个 display items（Fig 4 + Fig 5 + Table 1）视觉密度高，与 page 2 纯文本反差大\n4. **Page 6** — Figure 6 下半部分 specification indicator panel 标签极小且密集\n\n### Info (7)\n- Page 2 整页纯文本无 display item\n- Figure 5 小尺寸下 dashed/solid curve 区分度有限\n- Figure 8 faded bars 灰度打印时对比度低\n- Figure 9 y 轴标签字号偏小\n- Table 2 最优值未加粗标注\n- Appendix Figure 10 色阶与 Figure 1 一致（正面）\n- Appendix 表格格式统一（正面）\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 — Findings**\n\n两位 Reviewer 独立给出相同评分，交叉回应后维持不变。\n\n**评分理由**：\n\n论文提出了有价值的框架——将 model collapse 检测框架化为需要控制 FPR 的统计检测问题，方法敏感性发现（FPR 3%→92%）具有实践指导意义，phase diagram 概念为该领域提供了有用的组织框架。\n\n但定量声明系统性超出证据支撑：\n- Phase diagram 仅基于 Pythia-410M + WikiText-103，跨架构验证仅在最极端条件 α=1.0 进行\n- Abstract/标题暗示的广度与实际证据严重不匹配\n- 统计功效不足（3 seeds, 8 pairs/cell）使 boundary 精度不可靠\n- Intervention 仅为 N=2 概念验证却使用 \"substantially\" 等强修饰语\n- Blind zone（α<0.50 已退化但无检测信号）限制框架的 early warning 价值\n\n**不可改变的天花板**：核心方法为计量经济学标准技术的移植（Granger, permutation test, BH-FDR），技术新颖性有限。两位 Reviewer 一致认为 novelty 来自 method-sensitivity finding 和 phase-diagram framing，而非方法本身。这是结构性限制。\n\n**Findings 而非 Conference 的关键差距**：如果跨架构验证扩展到 α∈[0.50, 0.75] 的过渡区域，且 intervention 有更充分的比较实验，评分可升至 3.5。当前版本的 scope claim 与证据之间的 gap 是阻止 Conference 接收的主要障碍。\n\n**与前轮比较（基于 issue tracker）**：MF-1（scope overclaim）、SF-2（FPR 标定）、SF-3（幂律拟合）、SF-4（intervention）均从 Round 2-3 首次提出，历经 12-13 轮仍未根本解决。论文在每轮进行了措辞调整（hedging），但核心实验规模未变。这些不是 writing 问题，而是 evidence 问题——无法仅通过文字修改解决。\n\n---\n\n## Detailed Comments\n\n### 两位 Reviewer 的分歧与裁定\n\n| 问题 | R1 判定 | R2 判定 | Director 裁定 |\n|------|---------|---------|---------------|\n| 统计功效 (N1) | Must-Fix | Should-Fix（sigmoid+spec curve 缓解） | Should-Fix — R2 的缓解证据有效 |\n| FPR 标定 (N3) | Must-Fix | Should-Fix（comparative 而非 absolute claim） | Should-Fix — 论文定位合理 |\n| 幂律拟合 (N4) | Must-Fix | Should-Fix（定性结论稳健） | Should-Fix — 但 Eq.(2) 需降级 |\n| Partial correlation | 方向矛盾 | 支持 Granger claim | R2 正确 — 同期减弱+滞后增强是 genuine temporal precedence 的标志 |\n| Design Principles | 形式化合理 | 过度 formal | 中间立场 — 需讨论反例 |\n| Appendix 规模 | 优势 | 应在主文摘要 | R1 正确 — 附录广度是优势，但关键结果需在主文充分摘要 |\n\n### 优先修改建议（按影响力排序）\n\n1. **Abstract/标题 scope 校准** — 最高优先级。明确核心结果基于 Pythia-410M，跨架构验证限于 α=1.0。\n2. **Intervention 降级** — 删除 \"substantially\"，明确 preliminary PoC 定位。\n3. **Blind zone 讨论** — Limitations 增加 α<0.50 检测盲区的 honest assessment。\n4. **Eq.(2) 降级** — 改为 empirical scaling hypothesis。\n5. **Granger 局限扩展** — 补充 partial correlation（控制 generation）、讨论 T=10 power 限制。\n6. **Design Principles 反例** — 正文讨论 transfer entropy null 和 first-differencing null。\n7. **Figure 字号** — Figures 2/4/6 axis labels 增大至 ≥8pt。\n8. **bib 清理** — 未引用条目处理，格式统一。",
    "project": "distrib_canary_collapse",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
  }
}
```

</details>

---


### Tool result

_source line 1335 · 2026-05-24T23:15:24.341097+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_150c7ce908e05d7932315e0288cf5bfb:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4146
}
```

</details>

---


### Assistant

_source line 1336 · 2026-05-24T23:15:33.803819+00:00_

Round 14 审稿报告已投递。

**评分：3.0（Findings）** — 两位 Reviewer 独立一致。

核心发现：
- **最高共识 Must-Fix**：跨架构验证仅 α=1.0，scope overclaim（Round 2 首提，13 轮未根本解决）
- **8 项 Should-Fix**：统计功效不足、FPR CI 极宽、幂律拟合数据点不足、intervention 过弱、Granger 局限、blind zone（新发现）、Design Principles 反例缺失、MMCT K 敏感性
- **Findings 而非 Conference 的关键差距**：scope claim 与证据的 gap 是结构性问题，需要补充实验而非仅修改文字

Issue tracker 已同步更新至 Round 14，新增 3 个 issue（R14-N1 blind zone、R14-W1 MMCT 权重噪声、R14-W2 T=10 短序列 power）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 129

## Round 129

2 recorded events


### User

_source line 1337 · 2026-05-24T23:15:33.809711+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 对 Reviewer 1 要点的逐条评估（第二轮）

注：部分要点与上一轮交叉回应重叠，此处聚焦 Director 指定的三个重点问题，对其余要点简要确认。

---

### Must-Fix 问题

**[AGREE] R1-N2: 跨架构验证仅在 α=1.0，scope overclaim**

完全同意，与我自己的 N1+N2 一致。这是论文最核心的问题。

补充一点 R1 提到的 GPT-2 null FPR 50%（Appendix Z.2）：这个数字意味着 PermG 在 GPT-2 上的 α=1.0 检测结果在统计上无法与随机猜测区分。§4.5 的 failure mode taxonomy 把这归为 "precision sensitivity"（bf16）和 "bidirectional confounding"（s43），但这些 failure modes 恰恰说明 PermG 的有效性高度依赖架构——而论文标题暗示的是 architecture-general 的 landscape characterization。

---

**[AGREE，但降级为 Should-Fix] R1-N4: 幂律拟合仅 3-4 个数据点**

**Director Q1: 我是否也注意到此问题？** 是的，但我在自己的审稿中未单列为独立 weakness——我将其归入了对 Detection Boundary（§3.4）呈现方式的总体评估中。

R1 的事实观察是正确的：排除 α=0.60 异常后，支撑幂律拟合的有效 α 值仅有 α∈{0.50, 0.75, 1.0}（加上 α=0.45 在 T≥15 时的跨越），共 3-4 个点。γ ∈ [0.64, 2.08] 的 CI 跨越 3× 范围，确实不具参数辨识力。

但我认为这是 **Should-Fix 而非 Must-Fix**，理由：
1. 论文自身措辞已经很谨慎——§3.4 说 "consistent with power-law scaling"，§4.4 说 "the qualitative conclusion—detection improves with longer observation—is robust to the specific γ value"
2. 论文的核心 contribution 不依赖 γ 的精确值——phase diagram 的三区域结构和 sharp onset 是独立于幂律参数的经验发现
3. Eq. (1)-(2) 的形式化呈现确实给人虚假的精确感，但修复方式是调整呈现（降级为 scaling hypothesis）而非否定结论

**建议**：将 Eq. (2) 标注为 "empirical scaling hypothesis" 而非推导结果；在主文中报告 γ 的 CI 宽度并明确声明 "current data cannot distinguish sub-linear from super-linear scaling"。

---

### Should-Fix 问题

**[AGREE] R1-W1: Intervention 过弱**

同意，与我的 W4 一致。即使 proof-of-concept 也应满足最低证据标准：N=2 seeds 在同一架构族（Pythia-410M 和 1.4B 属同一家族），α=1.0 是最有利条件，15% threshold 从数据本身确定。不构成 Must-Fix 是因为论文的 framing 确实是 "proof of concept"。

---

**[PARTIALLY AGREE] R1-W2: 3 seeds 统计功效不足**

**Director Q2: 如何评估严重性？**

R1 的核心论点（3 seeds → CI 宽 → 定量声明不可靠）在原始统计意义上是正确的。6/8 的 Clopper-Pearson CI [0.25, 0.92] 确实非常宽。

但我认为需要区分两个层次：

**(a) 单点估计层面** — R1 是对的。任何单个 (α, seed) 条件的检测率估计都不可靠。Phase diagram 的每个网格点确实缺乏统计功效。

**(b) 多条件一致性层面** — 论文有缓解证据。关键的 blind→onset 转换在 3/3 fp32 seeds 上一致出现（0/8→6/8 at α=0.50, §4.2），Fisher exact p=3.45×10⁻¹¹。Specification curve 跨 1,160 configurations 显示 blind→onset jump 的鲁棒性（Figure 6, Appendix E）。α=0.45 在 T≥15 跨越检测边界的模式在 dual-seed 上重现（§4.4）。

**我的判定：Should-Fix**。增加 seeds 会收窄 CI 并增强可信度，但现有的多方法、多条件交叉一致性为定性结论（存在 sharp onset）提供了合理支撑。论文应避免报告看似精确的数字（如 α_c=0.483±0.006）而应强调定性模式。

---

**[PARTIALLY REBUT] R1-W3: Granger causality 局限**

同意 Granger 局限讨论不够充分（与我的 W5 一致），但需要纠正 R1 对具体证据的解读：

1. **Transfer entropy 0/192**（Appendix F）：R1 将此视为 Granger 发现的反证。但论文在 §5 已讨论：这与 "absent nonlinear structure" 或 "insufficient short-T power" 均一致。短序列（T=10-25）下非参数方法（如 transfer entropy 需要 kernel density estimation）的 power 远低于参数方法，0/192 更可能反映功效不足而非非线性结构不存在。

2. **First-differencing 消除 canary→perplexity**（F≈0, p=0.99）：R1 将此列为局限，但论文在 §4.2 将其作为 **正面发现** 呈现——first-differencing 成功分离了虚假关联（canary→perplexity 是 shared trend artifact）和真实关联（canary→diversity 24/24→24/24 存活）。这实际上是方法论严谨性的证据。

3. **潜在 confounders**：同意。训练动态（learning rate schedule, optimization trajectory）作为共同驱动因素未被排除。论文在 §5 和 Limitations §3 承认了 bivariate 局限但未深入讨论 specific confounders。

**我的判定：核心的 Granger 局限确实应更充分讨论（尤其是 observational equivalence 和 confounders），但 R1 对 first-differencing 和 transfer entropy 结果的解读需要修正。**

---

**[AGREE] R1-FPR: FPR 标定问题**

**Director Q3: 是否影响对核心结果可靠性的判断？**

FPR 7.4% > 5%（nominal）且 CI [2.1%, 17.9%] 确实偏宽。对核心结果的影响需分情境讨论：

**(a) 对 method comparison（Contribution 1）的影响：低。** 方法敏感性的核心发现是 5 种方法的 FPR 从 7% 到 94%——PermG 是否恰好控制在 5% 还是 7.4% 不影响 "方法选择极大影响结论" 这一主发现。

**(b) 对 phase diagram（Contribution 2）的影响：中等。** 如果真实 FPR 接近 CI 上界 17.9%，那么 α=0.50 的 6/8 检测率（75%）中可能有 ~1.4 个是 false positives。这不会消除 0/8→6/8 的定性跳跃，但会弱化定量声明。

**(c) 对 cascade ordering（Contribution 3）的影响：低。** 24/24 forward vs 0/24 reverse 的极端不对称性不太可能被 FPR bias 解释。

**总结：FPR 问题影响定量精度但不推翻定性结论。是 Should-Fix 而非 Must-Fix。**

---

### Strengths 确认

**[AGREE] R1-S4: 附录 robustness checks 是优势**

完全同意。24 个附录 section（A-Z）覆盖了置换检验鲁棒性（D）、specification curve（E）、change-point detection（G）、Shapley decomposition（P）、weight ablation（Q）等。这种系统性自我审查在 EMNLP 实证论文中不常见。

**[AGREE] R1: 框架本身有价值**

同意。将 canary metrics + multi-method comparison 应用于 model collapse detection 的框架思路有实际价值，即使当前证据范围有限。

---

### 综合评估

与 R1 评分一致：**3.0 (Findings)**。

两位 Reviewer 的核心共识：
1. **Cross-architecture scope 是最大问题**（R1-N2 = 我的 N1+N2）— 一致判定 Must-Fix
2. **方法敏感性发现有价值** — 一致认可
3. **定量声明超出证据支撑** — 一致判定需要修改

主要分歧在 severity grading：我倾向于将 R1 的部分 Must-Fix（N4 幂律拟合、FPR 标定）降级为 Should-Fix，因为论文的核心 contribution 不依赖这些定量细节的精确性，而是在于揭示方法敏感性问题和定性的 phase structure。

---

[Reviewer 2 审稿结果]:
交叉回应已提交。两轮交叉评审的核心立场一致：与 R1 在 cross-architecture scope（Must-Fix）和最终评分（3.0 Findings）上完全对齐，分歧集中在幂律拟合和 FPR 标定的严重程度判定上——我认为这些是 Should-Fix 因为论文的定性结论不依赖精确参数值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1338 · 2026-05-24T23:15:43.237778+00:00_

收到 R2 的第二轮交叉回应。两轮交叉已完全收敛——双方在评分（3.0 Findings）和最大问题（cross-architecture scope Must-Fix）上完全对齐，剩余分歧仅为 severity grading（Must-Fix vs Should-Fix），不涉及问题存在性的分歧。

报告已在上一步提交。本轮无需额外操作——R2 的第二轮交叉回应进一步确认了报告中的裁定方向（Director 已将 R1 的 N1/N3/N4 从 Must-Fix 降级为 Should-Fix，与 R2 立场一致）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 130

## Round 130

72 recorded events


### User

_source line 1339 · 2026-05-25T07:12:07.596220+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distrib_canary_collapse
- 论文路径: projects/distrib_canary_collapse/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper
- 截止日期: 未提供，请自行调研
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1340 · 2026-05-25T07:12:13.638613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-25T07:12:13.689582+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1342 · 2026-05-25T07:12:22.491543+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,read_project_file,WebSearch",
  "max_results": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,read_project_file,WebSearch",
    "max_results": "12"
  }
}
```

</details>

---


### Tool result

_source line 1343 · 2026-05-25T07:12:22.491902+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1344 · 2026-05-25T07:12:37.159890+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,get_visual_check_status,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1345 · 2026-05-25T07:12:37.160366+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1346 · 2026-05-25T07:12:45.850008+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,update_review_issues,submit_review_report_to_research_director",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,director_post_to_reviewer,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,update_review_issues,submit_review_report_to_research_director",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1347 · 2026-05-25T07:12:45.900937+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1348 · 2026-05-25T07:12:51.081867+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1349 · 2026-05-25T07:12:51.082215+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1350 · 2026-05-25T07:12:56.710545+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool call

_source line 1351 · 2026-05-25T07:12:57.157134+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline ARR"
  }
}
```

</details>

---


### Tool result

_source line 1352 · 2026-05-25T07:12:59.015430+00:00_

{"result":"# 项目 distrib_canary_collapse 概况\n\n## 实验状态 (218 个)\n\n- **gen_wiki_gpt2m_a100_s42_v3**: DONE (success) — \n- **mvp_v4_rep44**: DONE (success) — \n- **plan_006_s42**: DONE (failed) — \n- **plan_006_s42_resume**: DONE (killed) — \n- **gen_wiki_gpt2m_a100_s42_v2**: DONE (killed) — \n- **method_ablation_phase2**: DONE (success) — \n- **alpha_sweep_a025_s42_v3**: DONE (success) — \n- **method_ablation_phase1**: DONE (success) — \n- **plan_009_bootstrap_ty**: DONE (success) — \n- **mvp_v3_rep43**: DONE (failed) — \n- **mvp_v3_rep42**: DONE (failed) — \n- **mvp_v2_rep43**: DONE (killed) — \n- **mvp_v2_rep42**: DONE (killed) — \n- **mvp_rep43**: DONE (killed) — \n- **mvp_rep42**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-25\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| c2_opt13b_a050_s42_fp32 | OPT-1.3B at α=0.50 should show PermG forward detection onset similar to Pythia-410M (6/8 at α=0.50), validating that the phase diagram structure generalizes beyond the Pythia family to the transition region | — | — | — |\n\n## 待处理\n- c2_opt13b_a050_s43_fp32_v2（准备中，spec 已填充，cuda:0 only）\n- C1: c1_interv_gpt2m_pred_s42 / c1_interv_gpt2m_react_s42 / c1_interv_opt13b_pred_s42 / c1_interv_opt13b_react_s42（命令就绪，待 C2 完成后注册）\n\n## 近期结论\n- **c2_opt13b_a050_s43_fp32** (failed): OPT-1.3B at α=0.50 seed 43 replication: cross-seed consistency of PermG forward detection in the transition region on a non-Pythia architecture\n- **null_fpr_s51_fp32** (success): Null experiment (α=0.00) for FPR estimation: no synthetic data contamination, all detection methods should show p>0.05, contributing to narrower FPR CI with 15 seeds\n- **null_t15_s42_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n\n## 趋势\n成功 154 / 负向 4 / 失败 23 / 共 211\n累计 GPU: 8.4h\n\n## 下一步\n（无活跃 idea，请通过 ideas
…[truncated 1793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2304
}
```

</details>

---


### Tool call

_source line 1353 · 2026-05-25T07:12:59.467955+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-25T07:12:59.468442+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1355 · 2026-05-25T07:12:59.569205+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{graphicx}
13	\usepackage{booktabs}
14	\usepackage{subcaption}
15	\usepackage{dblfloatfix}
16	\usepackage{placeins}
17	\usepackage{algorithm}
18	\usepackage{algpseudocode}
19	\usepackage{amsthm}
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{proposition}[theorem]{Proposition}
22	\newtheorem{designprinciple}[theorem]{Design Principle}
23	\theoremstyle{definition}
24	\newtheorem{assumption}[theorem]{Assumption}
25	
26	\title{Characterizing the Detectability Landscape of Iterative Model Collapse}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	\input{introduction}
35	\input{related_work}
36	\input{method}
37	\input{experiments}
38	\input{discussion}
39	\input{conclusion}
40	\input{limitations}
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1356 · 2026-05-25T07:13:04.186797+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here are the key findings about EMNLP 2026 call for papers and submission deadlines:

## ARR Submission Deadline

The ARR (ACL Rolling Review) submissio
…[truncated 1205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 7029
}
```

</details>

---


### Tool result

_source line 1357 · 2026-05-25T07:13:04.187323+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 4718
}
```

</details>

---


### Tool call

_source line 1358 · 2026-05-25T07:13:13.051928+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 author guidelines page limit format template double-blind site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 author guidelines page limit format template double-blind site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 1359 · 2026-05-25T07:13:15.413166+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1360 · 2026-05-25T07:13:15.868519+00:00_

-rw-r--r-- 1 ubuntu ubuntu 1252044 May 25 07:08 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 455
}
```

</details>

---


### Tool call

_source line 1361 · 2026-05-25T07:13:16.375284+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 1362 · 2026-05-25T07:13:16.878130+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1363 · 2026-05-25T07:13:16.878631+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/ 2>/dev/null",
  "description": "Check existing review reports"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_reports/ 2>/dev/null",
    "description": "Check existing review reports"
  }
}
```

</details>

---


### Tool result

_source line 1364 · 2026-05-25T07:13:16.981675+00:00_

round_1.md
round_10.md
round_11.md
round_12.md
round_13.md
round_14.md
round_2.md
round_3.md
round_4.md
round_5.md
round_6.md
round_7.md
round_8.md
round_9.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 103
}
```

</details>

---


### Tool result

_source line 1365 · 2026-05-25T07:13:19.244917+00:00_

Web search results for query: "EMNLP 2026 author guidelines page limit format template double-blind site:2026.emnlp.org"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"},{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"Registration Information for EMNLP 2025 - EMNLP 2026","url":"https://2026.emnlp.org/registration/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"EMNLP 2026 Blog - EMNLP 2026","url":"https://2026.emnlp.org/blog/"},{"title":"EMNLP 2026 AI Reviewing Experiment - EMNLP 2026","url":"https://2026.emnlp.org/ai-reviewing-experiment/"}]

Based on the search results, I found some information about EMNLP 2026 author guidelines, though the main conference papers follow the ARR submission requirements rather than having their own specific format page. Here's what I found:

## For Industry Track Papers:

Industry track papers have a maximum of 6 pages. Industry Track submissions must neither include the authors' names nor their affiliations, following double-blind review requirements. Authors are required to discuss the limitations of their work in a dedicated section titled "Limitations" at the end of the paper before references, which will not count toward the page limit.

## For Tutorial Proposals:

Tutorial proposals should not exceed 4 pages of content (plus one page for tutor biographies and unlimited pages for references) and should use the ACL pa
…[truncated 813 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 6192
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-25T07:13:40.567469+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit long paper short paper format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit long paper short paper format requirements"
  }
}
```

</details>

---


### Tool call

_source line 1367 · 2026-05-25T07:13:40.567930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 1368 · 2026-05-25T07:13:40.568183+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1369 · 2026-05-25T07:13:40.618687+00:00_

1	\begin{abstract}
2	When language models train iteratively on their own output, the resulting distributional collapse is difficult to detect: the time series are short, the signal grows sub-linearly with contamination, and---as we demonstrate---the choice of statistical method can shift conclusions from universal detection to complete null.
3	We apply five lead-lag detection methods to identical iterative-training data and find that null-control false-positive rates span 7\% to 94\%, exposing method sensitivity as a primary obstacle to reliable collapse monitoring.
4	Permutation Granger causality, the lowest false-positive method, reveals a structured detectability landscape: detection jumps from absent to reliable within a narrow contamination interval, organized by a power-law boundary across three confirmed regimes.
5	Cross-architecture evaluation at $\alpha{=}1.0$ (full synthetic replacement) across five model families (345M--6.9B) supports forward detection in 11/15 conditions, with four non-confirming cases isolating distinct failure modes.
6	Token entropy temporally precedes diversity collapse by at least one generation (Granger precedence), providing a canary signal whose triggered cessation reduces peak perplexity in a proof-of-concept demonstration.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1370 · 2026-05-25T07:13:40.619168+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\citep{shumailov2024curse,alemohammad2024mad}.
5	This process can be triggered by vanishingly small synthetic fractions~\citep{dohmatob2025strong}: lexical diversity narrows, calibration deteriorates, and each generation inherits the biases of its predecessors.
6	As machine-generated text grows prevalent on the web, such feedback loops pose a growing risk to production pipelines, and by the time standard quality metrics register degradation, the distribution may have already shifted irreversibly.
7	
8	This threat motivates a fundamental question: \emph{can we reliably detect the onset of model collapse?}
9	The answer is less clear than it might appear.
10	Iterative training produces short, noisy time series (often fewer than 15 points) where detection power drops sharply~\citep{boettiger2012limits}, and model collapse is a first-order transition~\citep{truong2026phase}, structurally ruling out the critical-slowing-down early-warning signals that ecologists rely on~\citep{scheffer2009early} (\S\ref{sec:related_work}).
11	More fundamentally, no prior work has systematically compared detection methods on this problem; as we show, the choice of statistical test alone can shift conclusions from universal detection to complete null on identical data.
12	
13	We systematically map this landscape on Pythia-410M~\citep{biderman2023pythia} across 13 contamination levels with multi-seed replication (Figure~\ref{fig:phase_diagram}).
14	Our most consequential finding concerns method sensitivity: five statistical methods applied to identical data yield null-control FPR spanning 7\% to 94\% ($\kappa{=}0.185$; Figure~\ref{fig:method_comparison}), demonstrating that single-method analyses cannot reliably distinguish real signals from artifacts.
15	Permutation Granger causal
…[truncated 2432 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1371 · 2026-05-25T07:13:46.550168+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit long paper short paper format requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"acl2026/formatting.md at master · Lilaizhen/acl2026","url":"https://github.com/Lilaizhen/acl2026/blob/master/formatting.md"},{"title":"Instructions for *ACL Proceedings","url":"https://arxiv.org/html/2506.06751v2"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the ACL Rolling Review 2026 submission guidelines, here are the key details regarding page limits and format requirements:

## Page Limits

**Long Papers:** Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references.

**Short Papers:** Review versions of short papers may have up to four (4) pages of conten
…[truncated 908 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 5982
}
```

</details>

---


### Tool call

_source line 1372 · 2026-05-25T07:13:54.937402+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1373 · 2026-05-25T07:13:55.893036+00:00_

1	\FloatBarrier
2	\section{Related Work}
3	\label{sec:related_work}
4	
5	\subsection{Model Collapse: Theory and Empirical Evidence}
6	\label{sec:rw_collapse}
7	
8	Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}; \citet{schaeffer2025position} systematize eight distinct notions of collapse---our operationalization aligns with their \emph{distributional shift} family (definitions~D4--D6).
9	Theoretical analyses sharpen these results: \citet{dohmatob2024tale} recast collapse as changed scaling-law exponents, \citet{dohmatob2025strong} proved collapse at vanishingly small synthetic fractions, and \citet{truong2026phase} prove entropy collapse is a first-order transition, structurally ruling out critical-slowing-down early-warning signals~\citep{scheffer2009early,scheffer2012anticipating}.
10	Critical mixture ratios separating qualitative outcomes have independent precedent: \citet{kazdan2025collapse} map collapse conditions, \citet{gu2024cmr} establish scaling laws for critical ratios, and \citet{gu2025datamixing} show data mixing induces phase transitions in knowledge acquisition.
11	
12	\subsection{Detection of Synthetic Data Contamination}
13	\label{sec:rw_detection}
14	
15	Monitoring metrics proposed for collapse include expected calibration error (ECE)~\citep{du2025scales}, surplexity~\citep{gambetta2024surplexity}, and machine-generated text detection~\citep{drayson2025detection}; \citet{shi2025closer} independently validate entropy as a collapse diagnostic in diffusion models.
16	\citet{boettiger2012limits} establish fundamental power limits for early-warning detection in short time series ($T{<}25$), directly relevant to iterative training where observation windows are typically $T{=}5$--$20$.
17	However, these works evaluate single metrics in isolation without cross-validating against alternative statistical tests.
18	We differ by applying five detection methods to identical data, mapping detectability acro
…[truncated 1571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 1374 · 2026-05-25T07:13:55.893590+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1375 · 2026-05-25T07:13:55.994450+00:00_

1	\FloatBarrier
2	\section{Method}
3	\label{sec:method}
4	
5	\subsection{Cascade Ordering}
6	\label{sec:cascade}
7	
8	If distributional collapse follows a predictable ordering across metrics, the earliest-responding metric can serve as a canary signal.
9	We formalize known metric properties---entropy as a continuous indicator of mode concentration, diversity as a threshold indicator of lexical coverage---under mode amplification~\citep{shumailov2024curse,dohmatob2024tale} (derivations in Appendix~\ref{app:cascade_theory}).
10	
11	\begin{designprinciple}[Entropy responds before diversity]\label{thm:entropy_leads}
12	Under mode amplification: \textup{(a)} entropy can decrease while the $\epsilon$-effective support $S_\epsilon(p) {=} |\{i: p_i > \epsilon\}|$ (hence distinct-$n$) is unchanged; \textup{(b)} if distinct-$n$ decreases, entropy has already decreased.
13	\end{designprinciple}
14	
15	The asymmetry arises because entropy responds to any mass redistribution (first-order), while diversity changes only when a token probability crosses the generation threshold~$\epsilon$; the margin $\gamma = \min_{i: p_i > \epsilon}(p_i - \epsilon)$ quantifies how much shift diversity absorbs silently.
16	
17	\begin{designprinciple}[Diversity lag $\geq 1$ generation]\label{prop:div_lag}
18	If the per-generation perturbation satisfies $\alpha\|\mathcal{T}(p_t) - p_t\|_\infty < \gamma(p_t, \epsilon)$ through entropy onset $t_H$, then diversity onset $t_D \geq t_H + 1$.
19	\end{designprinciple}
20	
21	ECE co-moves with entropy at zero lag ($\Delta\mathrm{ECE} \approx \Delta C > 0$ whenever $\Delta\bar{H} < 0$; Appendix~\ref{app:cascade_theory}), yielding a three-stage cascade $\{H, \mathrm{ECE}\} \to \mathrm{Distinct}$-$n$.
22	This ordering holds in 14/15 experiments at $\alpha \geq 0.30$, with entropy and ECE consistently reaching onset at generation~1 and distinct-$n$ following at generation~2 ($t_H{=}t_{\mathrm{ECE}}{=}1$, $t_D{=}2$; \S\ref{sec:regime}; Appendix~\ref{app:moment_c
…[truncated 7067 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1376 · 2026-05-25T07:13:55.994833+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1377 · 2026-05-25T07:13:56.045569+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study iterative training collapse using Pythia-410M~\citep{biderman2023pythia} as the primary architecture.
8	Training data is drawn from WikiText-103~\citep{merity2017pointer} following the replace paradigm of~\citet{shumailov2024curse}: each generation fine-tunes on a mixture of $\alpha$ synthetic and $(1{-}\alpha)$ real data, generates 5{,}000 replacement samples, and fully replaces the synthetic pool (hyperparameters in Appendix~\ref{app:training_details}).
9	We run $T{=}10$ generations across 13 contamination levels ($\alpha \in \{0.00, \ldots, 1.00\}$) with multi-seed replication, yielding ${\sim}1{,}500$ statistical tests after BH-FDR correction~\citep{benjamini1995controlling}.
10	We track two \emph{canary metrics} (token entropy and ECE) and three \emph{downstream metrics}: distinct-1, distinct-2~\citep{li2016diversity}, and perplexity (distinct-3: Appendix~\ref{app:distinct3}).
11	PermG uses 5{,}000 permutations on first-differenced series~\citep{shojaie2022granger} with maximum lag~5.
12	
13	
14	\subsection{Sharp Detection Onset}
15	\label{sec:regime}
16	
17	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ even at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$.
18	Despite this ubiquitous degradation, Granger detectability is sharply regime-dependent.
19	PermG finds 0/8 canary$\to$downstream pairs FDR-significant from $\alpha{=}0.00$ through $\alpha{=}0.45$, then jumps to 6/8 (Clopper--Pearson 95\% CI $[0.25, 0.92]$) at $\alpha{=}0.50$, uniformly across all 3~fp32 seeds.
20	
21	\begin{figure}[t]
22	\centering
23	\includegraphics[width=\columnwidth]{figures/metric_trajectory.pdf}
24	\caption{Metric trajectories at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead 
…[truncated 10804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1378 · 2026-05-25T07:14:00.566354+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1379 · 2026-05-25T07:14:01.018782+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	Our Granger-precedence claim is scoped to temporal predictive improvement~\citep{granger1969investigating,shojaie2022granger}: bivariate tests cannot exclude confounders, and the FPR CI ($[1.8\%, 16.2\%]$) means Type~I error may be non-negligible.
4	Four of fifteen cross-architecture conditions do not confirm forward detection (\S\ref{sec:generalization}), each isolating a distinct PermG assumption violation---precision sensitivity (GPT-2 bf16), seed dependence (Pythia-1.4B), and entropy decoupling (SmolLM3-3B)---requiring architecture-specific null calibration before deployment (Appendix~\ref{app:extended_discussion}).
5	More broadly, our observation sequences ($T{=}10$--$25$) are far shorter than econometric standards ($T{\geq}100$); permutation testing avoids asymptotic assumptions but cannot recover power lost to short samples~\citep{shojaie2022granger}.
6	Bivariate tests are susceptible to omitted variable bias---first-differencing removes shared linear trends but nonlinear confounds remain possible---and PermG tests linear precedence only; transfer entropy (Appendix~\ref{app:transfer_entropy}) yields 0/192 significant pairs.
7	Partial correlation provides supporting evidence: after controlling for generation number, contemporaneous associations weaken ($\bar{|r|}$: $0.590{\to}0.381$) while lagged correlations strengthen ($0.759{\to}0.841$), consistent with genuine temporal precedence rather than shared-trend artifacts (Appendix~\ref{app:partial_corr}).
8	
9	Despite these individual limitations, the five methods exhibit complementary strengths.
10	Shapley value decomposition over all $2^5{=}32$ coalitions (Appendix~\ref{app:shapley}) shows DiffXCorr achieving the best combined Shapley contribution ($-0.299$) by detecting bidirectional coupling that directional methods miss, while PermG ranks best among directional methods ($-0.141$).
11	This complementarity explains why consensus voting outperforms any single me
…[truncated 648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1380 · 2026-05-25T07:14:01.019466+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1381 · 2026-05-25T07:14:01.523243+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Lead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.
5	Method choice alone inflates null-control FPR from 6.7\% to 94.4\%, establishing that single-method analyses cannot reliably distinguish temporal precedence from artifacts.
6	Our five-method comparison identifies PermG as the recommended detector, combining the lowest FPR (6.7\%, 10~seeds) with a steep onset from 0/8 at $\alpha{\leq}0.45$ to 6/8 at $\alpha{=}0.50$.
7	Token entropy exhibits robust one-generation-ahead precedence over diversity collapse (24/24 forward, 0/24 reverse at $\alpha{=}1.0$; ${\geq}6/8$ in 11/15 cross-architecture conditions).
8	The blind zone below $\alpha_c$ constrains practical deployment to settings with sufficient contamination; evaluation at ${>}$7B parameters remains open.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1382 · 2026-05-25T07:14:01.573938+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-25T07:14:01.624692+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Scope and generalizability.}
5	Our landscape characterization uses Pythia-410M as the primary architecture; the phase diagram is Pythia-family-only, frontier-scale behavior (${>}$7B) is untested, and cross-architecture evaluation is limited to $\alpha{=}1.0$.
6	All experiments use full replacement with a single decoding strategy (temperature~$1.0$, top-$k{=}50$); data accumulation~\citep{dey2024breaking} or lower temperatures would shift the landscape.
7	More fundamentally, the blind zone below $\alpha_c$ means that substantial quality degradation (e.g., ${\sim}40\%$ distinct-1 decline at $\alpha{=}0.25$) occurs before any statistical method signals detection.
8	The framework is therefore better characterized as a confirmation tool for ongoing collapse than an early-warning system.
9	
10	\paragraph{Statistical power.}
11	PermG's empirical FPR is 6.7\% (CI $[1.8\%, 16.2\%]$) and $K{\geq}3$ consensus yields 10.0\% (6/60); per-condition detection rates carry wide binomial CIs (e.g., $[0.25, 0.92]$ for 6/8), so the phase diagram represents a coarse topology rather than precise probability estimates.
12	
13	\paragraph{Causal interpretation.}
14	Permutation Granger testing establishes temporal precedence, not causation; our short-sequence regime ($T{\leq}25$) limits statistical power relative to econometric standards ($T{\geq}100$), and nonlinear alternatives to the linear PermG test yield no significant results in our setting (see \S\ref{sec:discussion}).
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1384 · 2026-05-25T07:14:06.339936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1385 · 2026-05-25T07:14:06.791753+00:00_

1	\appendix
2	
3	\section{Training Details and Metric Drift}
4	\label{app:training_details}
5	\label{app:drift}
6	
7	\paragraph{Hyperparameters.}
8	Each generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).
9	Generation uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.
10	Canary metrics: token entropy $H(p_\theta | \text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.
11	Additional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.
12	
13	\paragraph{Architecture-specific training.}
14	Table~\ref{tab:arch_hyperparams} reports training hyperparameters for each architecture in the cross-architecture evaluation (\S\ref{sec:generalization}).
15	All models use the same generation parameters (temperature~$1.0$, top-$k{=}50$, max length 512) to control for decoding-strategy confounds.
16	Batch sizes are adjusted for GPU memory constraints; learning rates follow the respective model families' recommended fine-tuning ranges.
17	
18	\begin{table}[h]
19	\centering
20	\small
21	\caption{Per-architecture training hyperparameters.}
22	\label{tab:arch_hyperparams}
23	\begin{tabular}{lcccl}
24	\toprule
25	Model & Batch & LR & Steps & Precision \\
26	\midrule
27	Pythia-410M & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
28	Pythia-1.4B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
29	Pythia-6.9B & 2 & $2{\times}10^{-5}$ & 5{,}000 & bf16 \\
30	GPT-2-medium & 32 & $5{\times}10^{-5}$ & 5{,}000 & fp32/bf16 \\
31	OPT-1.3B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
32	Qwen3.5-0.8B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
33	SmolLM3-3B & 4 & $2{\times}10^{-5}$ & 5{,}000 & fp32 \\
34	\bottomrule
35	\end{tabular}
36	\end{table}
37	
38	\paragraph{Metric computation details.}
39	Token entropy is computed as $H(p_\the
…[truncated 1149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1386 · 2026-05-25T07:14:06.894090+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-25T07:14:07.596673+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf (1.2MB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 702
}
```

</details>

---


### Tool call

_source line 1388 · 2026-05-25T07:14:16.694132+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf",
  "pages": "10-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf",
    "pages": "10-20"
  }
}
```

</details>

---


### Tool result

_source line 1389 · 2026-05-25T07:14:17.549957+00:00_

PDF pages extracted: 11 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf (1.2MB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 1390 · 2026-05-25T07:14:17.562590+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1391 · 2026-05-25T07:14:17.613299+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1392 · 2026-05-25T07:14:57.278398+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1393 · 2026-05-25T07:14:59.772715+00:00_

{"result":"# 项目 distrib_canary_collapse 概况\n\n## 实验状态 (218 个)\n\n- **gen_wiki_gpt2m_a100_s42_v3**: DONE (success) — \n- **mvp_v4_rep44**: DONE (success) — \n- **plan_006_s42**: DONE (failed) — \n- **plan_006_s42_resume**: DONE (killed) — \n- **gen_wiki_gpt2m_a100_s42_v2**: DONE (killed) — \n- **method_ablation_phase2**: DONE (success) — \n- **alpha_sweep_a025_s42_v3**: DONE (success) — \n- **method_ablation_phase1**: DONE (success) — \n- **plan_009_bootstrap_ty**: DONE (success) — \n- **mvp_v3_rep43**: DONE (failed) — \n- **mvp_v3_rep42**: DONE (failed) — \n- **mvp_v2_rep43**: DONE (killed) — \n- **mvp_v2_rep42**: DONE (killed) — \n- **mvp_rep43**: DONE (killed) — \n- **mvp_rep42**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-25\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| c2_opt13b_a050_s42_fp32 | OPT-1.3B at α=0.50 should show PermG forward detection onset similar to Pythia-410M (6/8 at α=0.50), validating that the phase diagram structure generalizes beyond the Pythia family to the transition region | — | — | — |\n\n## 待处理\n- c2_opt13b_a050_s43_fp32_v2（准备中，spec 已填充，cuda:0 only）\n- C1: c1_interv_gpt2m_pred_s42 / c1_interv_gpt2m_react_s42 / c1_interv_opt13b_pred_s42 / c1_interv_opt13b_react_s42（命令就绪，待 C2 完成后注册）\n\n## 近期结论\n- **c2_opt13b_a050_s43_fp32** (failed): OPT-1.3B at α=0.50 seed 43 replication: cross-seed consistency of PermG forward detection in the transition region on a non-Pythia architecture\n- **null_fpr_s51_fp32** (success): Null experiment (α=0.00) for FPR estimation: no synthetic data contamination, all detection methods should show p>0.05, contributing to narrower FPR CI with 15 seeds\n- **null_t15_s42_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n\n## 趋势\n成功 154 / 负向 4 / 失败 23 / 共 211\n累计 GPU: 8.4h\n\n## 下一步\n（无活跃 idea，请通过 ideas
…[truncated 1793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 2494
}
```

</details>

---


### Tool call

_source line 1394 · 2026-05-25T07:14:59.874443+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -c /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf | awk '{print $1}' && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -c /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf | awk '{print $1}' && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdfinfo', '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf'], capture_output=True, text=True)\nprint(result.stdout)\n\" 2>/dev/null || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1395 · 2026-05-25T07:15:00.093082+00:00_

1252044
Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        pdfTeX-1.40.28
CreationDate:    Mon May 25 07:08:16 2026 UTC
ModDate:         Mon May 25 07:08:16 2026 UTC
Custom Metadata: yes
Metadata Stream: no
Tagged:          no
UserProperties:  no
Suspects:        no
Form:            none
JavaScript:      no
Pages:           37
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       1252044 bytes
Optimized:       no
PDF version:     1.7

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 218
}
```

</details>

---


### Tool call

_source line 1396 · 2026-05-25T07:15:10.328459+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_CONFIG_FOUND\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\" || echo \"NO_CONFIG_FOUND\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1397 · 2026-05-25T07:15:10.379237+00:00_

NO_CONFIG_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-25T07:15:13.950809+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 1399 · 2026-05-25T07:15:14.102828+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1400 · 2026-05-25T07:15:26.569748+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4 -maxdepth 3 -name \"*.yaml\" -path \"*/distrib_canary*\" 2>/dev/null | head -10",
  "description": "Find project YAML files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4 -maxdepth 3 -name \"*.yaml\" -path \"*/distrib_canary*\" 2>/dev/null | head -10",
    "description": "Find project YAML files"
  }
}
```

</details>

---


### Tool result

_source line 1401 · 2026-05-25T07:15:26.670678+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/config/projects/distrib_canary_collapse.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1402 · 2026-05-25T07:15:30.641850+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/config/projects/distrib_canary_collapse.yaml 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Check external review config in project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"external_review\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/config/projects/distrib_canary_collapse.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Check external review config in project config"
  }
}
```

</details>

---


### Tool result

_source line 1403 · 2026-05-25T07:15:30.793072+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1404 · 2026-05-25T07:15:53.422382+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distrib_canary_collapse",
  "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
  }
}
```

</details>

---


### Tool result

_source line 1405 · 2026-05-25T07:16:15.077947+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21655
}
```

</details>

---


### Tool call

_source line 1406 · 2026-05-25T07:16:15.128660+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你负责审查本文的**方法严谨性和实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（via ARR）\n- **Deadline**: 2026-05-25\n- **类别**: Long Paper（正文 8 页 + 无限参考文献）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind（作者标为 \"Anonymous ACL submission\"）\n- **Limitations**: 必须有，最多 1 页，不计入页数限制\n- **附录**: 允许，不计入页数\n\n## 论文信息\n- **标题**: Characterizing the Detectability Landscape of Iterative Model Collapse\n- **论文路径**: `projects/distrib_canary_collapse/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf`（37 页：正文 8 页 + 参考文献 + 附录约 27 页）\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **统计方法的正确性**：\n   - PermG 的 FPR 估计（6.7%, CI [1.8%, 16.2%]）是否基于足够的 null-control 样本？10 seeds × 6 pairs = 60 pairs 是否足够？\n   - BH-FDR 校正在 8 pairs 的小族群中是否适当？\n   - MMCT 共识投票的 FPR-inverse weighting 设计是否有统计学依据？\n   - 检测边界 α_c(T) = A·T^{-γ} 用 3-4 个数据点拟合 3 个自由参数是否过拟合？\n\n2. **实验设计的充分性**：\n   - 主要 phase diagram 仅基于 Pythia-410M，泛化性如何？\n   - 跨架构评估仅在 α=1.0，是否足以支持 claim？\n   - 每个条件 3-4 seeds 的 replication 是否足够？\n   - T=10 generations 作为主要实验窗口是否合理？\n\n3. **因果推断的局限性**：\n   - Granger precedence vs. causation 的区分是否充分？\n   - 双变量检验无法排除混淆因素——论文是否充分承认这一点？\n   - First-differencing 消除 canary→perplexity 但保留 canary→diversity——这是否被过度解读？\n\n4. **Intervention 实验**：\n   - 仅在 α=1.0 的 proof-of-concept 是否足以支持实际部署的含义？\n   - 15% 阈值的选择是否充分验证？\n   - 与 naive PPL threshold 的比较是否公平？\n\n5. **可重现性**：\n   - 超参数和实验设置是否足够详细？\n   - 代码/数据是否提供（或承诺提供）？\n\n请按 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Missing References、Overall Assessment（用 EMNLP 2026 ARR 评分标准 1-5 分）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你负责审查本文的**方法严谨性和实验设计**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（via ARR）\n- **Deadline**: 2026-05-25\n- **类别**: Long Paper（正文 8 页 + 无限参考文献）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind（作者标为 \"Anonymous ACL submission\"）\n- **Limitations**: 必须有，最多 1 页，不计入页数限制\n- **附录**: 允许，不计入页数\n\n## 论文信息\n- **标题**: Characterizing the Detectability Landscape of Iterative Model Collapse\n- **论文路径**: `projects/distrib_canary_collapse/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf`（37 页：正文 8 页 + 参考文献 + 附录约 27 页）\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **统计方法的正确性**：\n   - PermG 的 FPR 估计（6.7%, CI [1.8%, 16.2%]）是否基于足够的 null-control 样本？10 seeds × 6 pairs = 60 pairs 是否足够？\n   - BH-FDR 校正在 8 pairs 的小族群中是否适当？\n   - MMCT 共识投票的 FPR-inverse weighting 设计是否有统计学依据？\n   - 检测边界 α_c(T) = A·T^{-γ} 用 3-4 个数据点拟合 3 个自由参数是否过拟合？\n\n2. **实验设计的充分性**：\n   - 主要 phase diagram 仅基于 Pythia-410M，泛化性如何？\n   - 跨架构评估仅在 α=1.0，是否足以支持 claim？\n   - 每个条件 3-4 seeds 的 replication 是否足够？\n   - T=10 generations 作为主要实验窗口是否合理？\n\n3. **因果推断的局限性**：\n   - Granger precedence vs. causation 的区分是否充分？\n   - 双变量检验无法排除混淆因素——论文是否充分承认这一点？\n   - First-differencing 消除 canary→perplexity 但保留 canary→diversity——这是否被过度解读？\n\n4. **Intervention 实验**：\n   - 仅在 α=1.0 的 proof-of-concept 是否足以支持实际部署的含义？\n   - 15% 阈值的选择是否充分验证？\n   - 与 naive PPL threshold 的比较是否公平？\n\n5. **可重现性**：\n   - 超参数和实验设置是否足够详细？\n   - 代码/数据是否提供（或承诺提供）？\n\n请按 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Missing References、Overall Assessment（用 EMNLP 2026 ARR 评分标准 1-5 分）。"
  }
}
```

</details>

---


### Tool result

_source line 1407 · 2026-05-25T07:16:32.146859+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17018
}
```

</details>

---


### Tool call

_source line 1408 · 2026-05-25T07:16:32.349328+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你负责审查本文的**新颖性、完整性和写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（via ARR）\n- **Deadline**: 2026-05-25\n- **类别**: Long Paper（正文 8 页 + 无限参考文献）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind（作者标为 \"Anonymous ACL submission\"）\n- **Limitations**: 必须有，最多 1 页，不计入页数限制\n- **附录**: 允许，不计入页数\n- **Abstract**: 不超过 200 words\n\n## 论文信息\n- **标题**: Characterizing the Detectability Landscape of Iterative Model Collapse\n- **论文路径**: `projects/distrib_canary_collapse/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf`（37 页：正文 8 页 + 参考文献 + 附录约 27 页）\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性（Novelty）**：\n   - 相对于 Shumailov et al. (2024), Dohmatob et al. (2024/2025), Truong & Truong (2026) 等已有工作，本文的核心贡献是否有足够的新颖性？\n   - \"method sensitivity as a primary finding\" 是否构成足够的研究贡献？将多种统计方法应用于同一数据是否只是工程性的比较？\n   - \"detectability landscape\" 的概念是否真正新颖，还是 dose-response 分析的换名？\n   - MMCT 共识投票框架是否有足够的方法论贡献？\n\n2. **Related Work 覆盖度**：\n   - 是否遗漏了重要的相关工作？特别关注：\n     - 模型坍缩检测方面的最新工作\n     - 因果推断/Granger causality 在 ML 中的应用\n     - 规格曲线分析/多分析师研究\n     - 时间序列中的 early-warning signals\n   - 与现有工作的定位是否清晰准确？\n\n3. **论文结构和叙事**：\n   - 论文的 framing 是否恰当？\"detectability landscape\" 是否是一个有意义的概念框架？\n   - 从 method sensitivity → phase diagram → cross-architecture → intervention 的叙事弧线是否连贯？\n   - Contributions 的列举是否与正文内容匹配？\n   - Discussion 和 Limitations 是否充分覆盖了主要局限？\n\n4. **写作质量**：\n   - 是否存在 AI 生成痕迹（过度使用 \"we demonstrate\"、\"remarkably\"、\"notably\" 等模式化用语）？\n   - 数学符号是否一致？\n   - 图表是否清晰、信息密度是否合理？\n   - 是否存在冗余或自我重复？\n\n5. **格式合规**：\n   - 正文是否严格控制在 8 页内？\n   - Abstract 是否在 200 words 以内？\n   - Limitations section 是否存在且内容适当？\n   - 附录是否包含了不应该放在附录中的核心内容（审稿人可能不会阅读附录）？\n   - 是否有 anonymity violation？\n\n请按 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Missing References、Overall Assessment（用 EMNLP 2026 ARR 评分标准 1-5 分）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你负责审查本文的**新颖性、完整性和写作质量**。\n\n## Venue 信息\n- **目标**: EMNLP 2026（via ARR）\n- **Deadline**: 2026-05-25\n- **类别**: Long Paper（正文 8 页 + 无限参考文献）\n- **模板**: ACL style（`\\usepackage[review]{acl}`）\n- **匿名**: Double-blind（作者标为 \"Anonymous ACL submission\"）\n- **Limitations**: 必须有，最多 1 页，不计入页数限制\n- **附录**: 允许，不计入页数\n- **Abstract**: 不超过 200 words\n\n## 论文信息\n- **标题**: Characterizing the Detectability Landscape of Iterative Model Collapse\n- **论文路径**: `projects/distrib_canary_collapse/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_15/submitted.pdf`（37 页：正文 8 页 + 参考文献 + 附录约 27 页）\n\n## 你的审查侧重\n\n请重点评估以下方面：\n\n1. **新颖性（Novelty）**：\n   - 相对于 Shumailov et al. (2024), Dohmatob et al. (2024/2025), Truong & Truong (2026) 等已有工作，本文的核心贡献是否有足够的新颖性？\n   - \"method sensitivity as a primary finding\" 是否构成足够的研究贡献？将多种统计方法应用于同一数据是否只是工程性的比较？\n   - \"detectability landscape\" 的概念是否真正新颖，还是 dose-response 分析的换名？\n   - MMCT 共识投票框架是否有足够的方法论贡献？\n\n2. **Related Work 覆盖度**：\n   - 是否遗漏了重要的相关工作？特别关注：\n     - 模型坍缩检测方面的最新工作\n     - 因果推断/Granger causality 在 ML 中的应用\n     - 规格曲线分析/多分析师研究\n     - 时间序列中的 early-warning signals\n   - 与现有工作的定位是否清晰准确？\n\n3. **论文结构和叙事**：\n   - 论文的 framing 是否恰当？\"detectability landscape\" 是否是一个有意义的概念框架？\n   - 从 method sensitivity → phase diagram → cross-architecture → intervention 的叙事弧线是否连贯？\n   - Contributions 的列举是否与正文内容匹配？\n   - Discussion 和 Limitations 是否充分覆盖了主要局限？\n\n4. **写作质量**：\n   - 是否存在 AI 生成痕迹（过度使用 \"we demonstrate\"、\"remarkably\"、\"notably\" 等模式化用语）？\n   - 数学符号是否一致？\n   - 图表是否清晰、信息密度是否合理？\n   - 是否存在冗余或自我重复？\n\n5. **格式合规**：\n   - 正文是否严格控制在 8 页内？\n   - Abstract 是否在 200 words 以内？\n   - Limitations section 是否存在且内容适当？\n   - 附录是否包含了不应该放在附录中的核心内容（审稿人可能不会阅读附录）？\n   - 是否有 anonymity violation？\n\n请按 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses、Questions、Missing References、Overall Assessment（用 EMNLP 2026 ARR 评分标准 1-5 分）。"
  }
}
```

</details>

---


### Tool result

_source line 1409 · 2026-05-25T07:16:33.993483+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1644
}
```

</details>

---


### Assistant

_source line 1410 · 2026-05-25T07:16:48.866621+00:00_

Round 1 已启动：

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | ✅ 已派发 | 方法严谨性 + 实验设计 |
| Reviewer 2 | ✅ 已派发 | 新颖性 + 完整性 + 写作质量 |
| 视觉审查 Agent | ✅ 已派发 | PDF 排版质量（非评分项） |
| 外部审稿 | ❌ 未启用 | — |

等待两位 Reviewer 返回独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 131

## Round 131

2 recorded events


### User

_source line 1411 · 2026-05-25T07:23:21.875200+00:00_

[Reviewer 2 审稿意见]:
## 总体评分
**Overall**: 3.0（Findings — 可被 Findings 接收）
**一句话总结**: 一项系统性的实证比较研究，展示了模型坍缩检测对统计方法选择的敏感性，但核心贡献（"detectability landscape"、MMCT）的新颖性不足以支撑主会议接收。

---

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论总体严谨（置换检验、BH-FDR 校正、null control），但 landscape 的泛化性仅基于 Pythia-410M，跨架构仅在 α=1.0 一个极端条件下验证 |
| Excitement | 2.5/5 | 主题相关且实用，但核心发现（不同统计检验给出不同结论）对统计学背景的读者而言并不意外；"landscape" framing 夸大了实际贡献 |
| Reproducibility | 4/5 | 实验细节充分（Appendix A/G），使用公开数据集 WikiText-103，承诺开源代码，种子和超参数记录完整 |
| Confidence | 4/5 | 熟悉 model collapse 文献、时间序列因果检验和 specification curve 方法论 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] "Detectability landscape" 的新颖性不足——本质上是标准的 dose-response 参数扫描
- 具体位置：Section 4.3, Figure 7, 以及 abstract 和 introduction 中对 "landscape" 的定位
- 问题：论文将 "detectability landscape" 作为核心概念贡献（Contribution 2），但实际操作是：在 α（污染比例）× T（观测窗口）的二维参数空间上扫描 PermG 检测率，拟合 sigmoid 边界，划分三个 regime（blind/onset/detection）。这是标准的 dose-response 分析——低剂量检测不到、高剂量检测得到、中间有过渡带——用 "phase diagram" 和 "landscape" 等物理学术语包装，但并未揭示超越参数扫描的结构性洞见。三个 regime 的划分本身取决于 PermG 的阈值行为（BH-FDR 校正后的二元判定），而非现象本身的内在结构。
- 为什么影响接收：这是论文标题和核心 framing 所依赖的概念。如果 "landscape" 仅是 dose-response 曲线的改名，则论文的概念贡献大幅缩水。
- 建议修改方向：(1) 明确承认与 dose-response 分析的关系，解释为什么 "landscape" 提供了超越标准 dose-response 的额外洞见；(2) 或者将重心从 "landscape mapping" 转移到更有实质的发现上（例如过渡带的锐度、power-law boundary 的普遍性），但需要跨架构的 landscape 数据来支撑。

**N2** [critical] 跨架构泛化仅在 α=1.0 条件下验证，landscape 的可迁移性未得到证实
- 具体位置：Section 4.5, Figure 8, Appendix Z.1 (Table 37)
- 问题：论文声称刻画了 "detectability landscape"，但详细的 landscape 分析（不同 α × T 组合下的检测率）仅在 Pythia-410M 上完成。跨架构评估仅在 α=1.0（100% 合成数据替换）这一极端条件下进行。4/15 条件不支持检测（GPT-2 medium, OPT-1.3B 部分配置, SmolLM3-3B），这些 non-confirming cases 反而暗示 landscape 可能是架构依赖的——不同架构可能有不同的 blind zone 边界、不同的过渡锐度、甚至不同的 regime 结构。但论文未在其他架构上展示 landscape 是否保持。
- 为什么影响接收：论文标题暗示对 "iterative model collapse" 的普遍性刻画，但实际上是对单一架构的详细分析加上其他架构在极端条件下的验证。这与 claim 的广度不匹配。
- 建议修改方向：(1) 至少对 Pythia-1.4B 或 GPT-2 在多个 α 水平上复现 landscape（即使只有 3-4 个 α 点）；(2) 或者在标题和 framing 中明确 landscape 是在 Pythia-410M 上刻画的，并将跨架构结果定位为初步验证。

**N3** [critical] Method sensitivity 作为 "primary finding"（Contribution 1）的新颖性有限
- 具体位置：Section 3.3, Figure 2, Contribution 1（page 2）
- 问题：论文将 "method sensitivity" 定位为首要贡献——五种统计方法对同一数据给出 6.7% 到 94.4% 的检测率。但这个发现的实质是：不同统计检验具有不同的功效（power）和第一类错误率（Type I error），而未经恰当多重比较校正的方法（如 NaiveXCorr）自然会产生高 FPR。NaiveXCorr 在所有水平（包括 null control）上都检出 7-8/8 对（Figure 2, Appendix K），这不是 "method sensitivity"，而是 NaiveXCorr 没有恰当控制 false positives。对统计学背景的审稿人来说，不同功效的检验给出不同结论并不意外。
- 为什么影响接收：将一个统计学常识（不同检验有不同 FPR/power trade-off）包装为 "primary finding" 会削弱论文的可信度，尤其是当一个 "94% detection" 的方法实际上是一个未校正的检验时。
- 建议修改方向：(1) 将 method sensitivity 重新定位为动机（motivation）而非发现（finding），即 "因为方法选择对结论影响巨大，因此需要系统比较"；(2) 更深入分析 sensitivity 的来源——是 power 差异、assumptions 差异、还是 null 校准差异？Section 3.3 和 Appendix D 的 specification curve 已经有这些分析的雏形，但主文的 framing 没有利用。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] MMCT 的方法论贡献薄弱
- 具体位置：Algorithm 1 (Section 3.3, page 4), Appendix H
- 问题：MMCT 本质上是一个 FPR 逆权重的多数投票——计算每个方法的 FPR，取逆作为权重，加权投票。这是一个非常标准的 ensemble 技术，算法本身不构成显著的方法论贡献。更关键的是，Appendix P 的 Shapley 分析显示 PermG 的边际贡献远超其他方法（combined Shapley = -0.041），这意味着 MMCT 的主要价值来自 PermG 本身，而非共识机制。如果单独使用 PermG 就能获得最低 FPR（6.7%），MMCT 的实际增量价值需要更充分的论证。
- 建议：在 Table 2 中直接对比 PermG-only vs. MMCT 在更多条件下的 FPR/TPR trade-off，或者更坦诚地将 MMCT 定位为实践性的稳健性工具而非方法论贡献。

**W2** [warning] 缺少关键参考文献：Silberzahn et al. (2018)
- 具体位置：Section 2.2（Related Work），Section 3.3
- 问题：论文的核心方法论——将多种分析方法应用于同一数据、展示结论如何随方法选择变化——直接对应 Silberzahn et al. (2018) "Many Analysts, One Data Set" 的研究范式。论文引用了 Coretta et al. (2023) 和 Simonsohn et al. (2020)，但遗漏了这一领域的奠基性工作。此外，Silberzahn 等人的关键发现——分析者的专业程度无法解释结论差异——与本文的 method sensitivity 发现高度相关。
- 建议：补充引用并在 Related Work 中讨论本文方法与 many-analysts 范式的关系。

**W3** [warning] Intervention（Section 4.6）过于初步但占据过多正文篇幅
- 具体位置：Section 4.6, Figure 9
- 问题：canary-based intervention 仅在一个条件下测试（Pythia-410M, α=1.0, 4 seeds），且干预策略是简单的阈值触发停训。64% perplexity reduction 的 claim（Figure 9b）来自这唯一的实验条件。在 8 页主文中，这占了约 0.5 页（Section 4.6 + Figure 9），对于如此初步的 proof-of-concept 来说比例偏大。
- 建议：(1) 压缩 intervention 到 1 段 + 1 figure，把省下的空间用于加强 landscape 的跨架构验证；(2) 或者在更多 α 水平上测试 intervention 以增强说服力。

**W4** [warning] Entropy 作为 canary metric 的因果解释不足
- 具体位置：Section 4.1（canary metrics 选择），Discussion (page 7-8)
- 问题：论文声称 token entropy 在时间上先于 diversity collapse（Granger precedence），因此可作为 canary signal。但 Appendix J 的 extended discussion 自己承认 "entropy as a measurement artifact" 的可能性——entropy 可能反映的是测量敏感度而非真正的时间先行性。这是一个关键的方法论顾虑，却被放在审稿人可能不会阅读的 appendix 中。主文的 Discussion 未充分讨论这一问题。
- 建议：将 Appendix J 中关于 entropy artifact 的讨论核心内容移入主文 Discussion 或 Limitations。

**W5** [warning] 核心内容过度依赖附录
- 具体位置：多处引用 Appendix（"derivations in Appendix X1", "see Appendix G", "Appendix I/Table 9" 等）
- 问题：Design Principle 的推导（Appendix X）、完整方法细节（Appendix G/15 页）、与已有工作的方法论比较表（Appendix I/Table 9）、extended discussion（Appendix J）都在附录中。主文的论述在多个关键环节依赖附录来补充论证。按 ARR 政策，审稿人不被要求阅读附录——这意味着仅凭主文，部分核心 claim 的论证链是不完整的。
- 建议：将 Table 9（方法论比较）的简化版和 Design Principle 推导的关键步骤移入主文。如果页面紧张，可以压缩 intervention 部分和部分图表。

---

## 小问题（不影响接收）

- **α 符号多义**：α 同时用于污染比例（contamination fraction）和 BH-FDR 的显著性水平（q=0.05），虽然在上下文中可区分，但偶尔造成困惑（如 Section 4.1 page 5 "Sub-threshold p-values at α=0.15"中的 α 指污染比例，但容易与统计显著性混淆）。建议对显著性水平统一使用 q 或其他符号。

- **图表密度偏高**：8 页正文包含 9 个 figure + 2 个 table + 1 个 algorithm。Figure 1 的 heatmap 标签在两栏格式下偏小；Figure 5 的 cascade timeline 压缩严重；Figure 6 的 specification curve 信息量大但文字偏小。

- **"canary metric" 术语动机不足**：虽然 "canary in the coal mine" 的隐喻可理解，但论文在 Section 3.2 首次引入时未解释为什么选用这个特定术语而非更标准的 "leading indicator" 或 "early-warning signal"。

- **写作质量总体可接受**，无明显 AI 生成痕迹。叙事连贯，从 method sensitivity → phase diagram → cross-architecture → intervention 的弧线清晰。个别句子略显冗长（如 abstract 第一句有 3 个并列从句）。

- **格式合规**：正文 8 页 ✓；Abstract 约 163 words ✓（< 200）；Limitations 存在且内容适当 ✓；双盲匿名 ✓（"Anonymous ACL submission"）；AI 使用声明存在（page 37）✓。

---

## 主要优势

1. **实验方法论严谨**：5,000 次置换检验、BH-FDR 多重比较校正、null control（α=0 条件）、多种子重复（10 seeds for Pythia-410M）——这是高标准的实验设计。

2. **Specification curve 分析的创造性引入**：从心理学/社会科学引入 specification curve 到 ML 检测问题中（Section 4.2, Figure 6, Appendix D），这是一个有价值的方法论迁移，1,160 个 specifications 的全面扫描有效展示了分析选择的影响。

3. **实用的方法推荐**：论文清晰地为实践者提供了可操作的建议——使用 PermG 作为首选检测方法（最低 FPR），这基于充分的经验证据（Table 2, Appendix P/Q/R）。

4. **附录的详尽程度值得肯定**：27 页附录覆盖了 robustness analysis、power analysis、ablation、理论推导等，展示了大量的补充工作。

5. **写作清晰度**：尽管信息密度高，论文的整体叙事弧线连贯，Design Principle 1 和 2 提供了简洁的理论动机。

---

## 缺失参考文献

1. **Silberzahn, R. et al. (2018)**. "Many Analysts, One Data Set: Making Transparent How Variations in Analytic Choices Affect Results." *Advances in Methods and Practices in Psychological Science*, 1(3), 337-356. — 这是 many-analysts 范式的奠基论文，与本文的 method sensitivity 分析直接相关。

2. **Mitchell et al. (2023)**. "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvatures." — 论文讨论 synthetic data detection 但未覆盖 per-sample detection 方法，应至少讨论分布层面检测与样本层面检测的关系和区别。

3. **Gretton et al. (2012)**. "A Kernel Two-Sample Test." — 论文使用 Granger-type temporal tests 检测分布漂移，但未讨论为什么选择时间序列检验而非标准的两样本检验（如 MMD）。应在 Related Work 或 Method 中说明选择依据。

---

## Questions for Authors

1. 如果在 Pythia-1.4B 或 GPT-2 上进行完整的 α × T landscape 扫描，你们是否预期 blind zone 的边界和过渡锐度会保持一致？如果不一致，"landscape" 作为一个统一概念框架的价值是什么？

2. NaiveXCorr 在 null control（α=0）下检出 7-8/8 对（Figure 2, page 3），这意味着它的 FPR 接近 100%。你们是否考虑过将其排除在方法比较之外，而非将其高 FPR 作为 "method sensitivity" 的证据？包含一个明显 uncalibrated 的方法来放大 sensitivity 幅度（7% vs 94%）是否有方法论上的合理性？

3. Appendix J 讨论了 entropy 可能是 "measurement artifact" 而非真正的 temporal precursor。这个担忧是否动摇了论文的核心 claim（Granger precedence as canary signal）？如果 entropy 的时间先行性仅反映其对微小分布变化的更高敏感度，那 canary signal 的因果叙事是否成立？

4. MMCT 的 Shapley 分析（Appendix P）显示 PermG 的 combined contribution 为 -0.041（即降低 FPR+FNR），远超其他方法。在什么场景下，MMCT 比单独使用 PermG 有实质性优势？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1412 · 2026-05-25T07:23:48.359184+00:00_

Reviewer 2 审稿意见已收到（Overall: 3.0 / Findings）。等待 Reviewer 1 完成独立初审后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 132

## Round 132

6 recorded events


### User

_source line 1413 · 2026-05-25T07:23:49.660648+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.5/5 (Borderline Conference)
**一句话总结**: 方法论框架扎实、问题选取及时，但核心 phase diagram 仅基于单一架构（Pythia-410M，3 seeds），跨架构验证仅在 α=1.0——这一最容易检测的极端场景——限制了泛化性 claim 的说服力。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 统计方法整体得当（PermG、BH-FDR、specification curve），但存在关键样本量不足问题：60 null pairs 的 FPR CI 宽达 [1.8%, 16.2%]，3 seeds 不足以可靠估计 seed variance，power-law boundary 3 参数拟合 3-4 个数据点实质为插值 |
| Excitement | 3.5/5 | Model collapse 检测是及时且重要的问题；multi-method comparison 框架和"方法选择本身是最大变异源（κ=0.185）"的发现有实际意义；但单架构限制降低了兴奋度 |
| Reproducibility | 3/5 | 超参数描述充分（Appendix A），实验设置透明；但代码/数据 "upon acceptance" 才释放，审稿期间无法验证；合成数据不释放 |
| Reviewer Confidence | 4/5 | 熟悉 Granger causality、permutation tests、FDR correction、specification curve 等统计方法，仔细阅读了全部 37 页 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Power-law detection boundary α_c(T) = A·T^{-γ} 的拟合严重欠定（3 free parameters, 3-4 data points）

- 具体位置：Section 3.4 (page 5), Appendix S (page 27), Appendix X (page 31-32)
- 问题：论文用 3 个自由参数（A, γ, 以及 sub-linear signal model 的 ρ）拟合仅 3-4 个数据点（T=5, 10, 15, 20 在 α 轴上的 detection onset）。这实质上是插值而非回归——剩余自由度为 0-1。γ 的 95% CI 为 [0.01, 2.10]，论文自己承认"无法区分 sub-linear 和 super-linear decay"（page 5）。但 phase diagram（Figure 1, Figure 3）和 main text 的叙事（"power-law boundary across three confirmed regimes"）仍以此为核心贡献展示。
- 为什么影响接收：Phase diagram 是论文第二个核心 claim（Contribution 2）。如果 boundary 的函数形式不可靠，phase diagram 的定量解读（blind zone 在 α<0.45，detection zone 在 0.45-0.60）也不可靠。三个 regime 的划分可能是对 noise 的过度解读。
- 建议修改方向：(1) 降低对 power-law 函数形式的 claim 强度——将其定位为"描述性拟合"（descriptive fit）而非"confirmed boundary"；(2) 使用更简单的 2 参数模型（如线性或 log-linear）并报告 AIC/BIC 比较；(3) 或增加数据点（T=3, 7, 12, 18 等中间值），使拟合有足够自由度。Appendix S (page 27) 的 sigmoid 拟合结果（SE of k = 327.6, 大于 estimate k=279.3）进一步表明数据不足以约束任何非线性函数形式。

**N2** [critical] 核心 phase diagram 仅基于 Pythia-410M（3 seeds），泛化性证据不足

- 具体位置：Section 4.1 (page 4), Section 4.5 (page 6-7), Table 1 (page 6), Figure 8 (page 7)
- 问题：论文标题是 "Characterizing the Detectability **Landscape**"，暗示普适性。但 phase diagram（Figure 1, 3）完全基于 Pythia-410M 单一模型。跨架构验证（Section 4.5, Table 1）仅在 α=1.0——全量合成替换，collapse 最严重、检测最容易的场景。在 detection boundary 附近（α≈0.45-0.60）——也就是论文发现最有趣的区域——没有任何跨架构数据。
- 四个 non-confirming 条件（GPT-2 medium s43, OPT-1.3B, Pythia-1.4B s43, SmolLM3-3B）的 failure mode 分析（Table 10, page 17）表明架构差异确实导致检测行为不同（如 SmolLM3-3B 的 entropy decoupling 违反 cascade ordering assumption）。这恰恰说明 phase diagram 不应假设架构无关。
- 为什么影响接收：没有跨架构的 intermediate-α 数据，读者无法判断 three-regime structure 是 Pythia-410M 的特异性质还是普适现象。对于一篇定位为 "landscape characterization" 的论文，这是核心泛化性缺陷。
- 建议修改方向：(1) 至少在一个额外架构（如 GPT-2 medium 或 Pythia-1.4B）上运行 α∈{0.25, 0.50, 0.75} 的实验，验证 phase boundary 位置；(2) 或显著降低泛化性 claim——将标题/abstract 中的 "landscape" 限定为 "Pythia-410M landscape"，并将跨架构结果明确定位为初步探索。

**N3** [critical] PermG 的 FPR 置信区间 [1.8%, 16.2%] 过宽，无法确认其 FPR 在可接受范围内

- 具体位置：Section 3.3 (page 4), Table 2 (page 8), Appendix R (page 25-26)
- 问题：PermG 的 null-control FPR = 4/60 = 6.7%，95% Clopper-Pearson CI [1.8%, 16.2%]。CI 上界 16.2% 远超 conventional 5% significance level 的 3 倍。论文将 PermG 推荐为 "the recommended detector"（Section 6, page 8），但数据无法排除其真实 FPR 高达 16%。
- 60 null pairs（10 seeds × 6 canary→downstream pairs）是不够的。标准的 permutation test 校准通常需要数百到数千个 null 样本。Appendix R 的 bootstrapping 分析（Figure 18, page 26）显示 PermG 的 FPR bootstrap 分布集中在 0-10%，但 95th percentile 仍可达 ~15%。
- 为什么影响接收：如果 PermG 的真实 FPR 接近 16%，那么论文的核心 claim——"PermG achieves the lowest FPR"——虽然在 point estimate 上成立，但实际表现可能与 DiffXCorr（14.8%）无统计显著差异。这动摇了 method comparison 和 MMCT 设计的基础。
- 建议修改方向：(1) 增加 null-control seeds（至少 20-30 seeds）以将 FPR CI 收窄到可解读范围；(2) 在当前数据下，不应将 PermG 绝对地推荐为 "the recommended detector"，而应表述为 "the method with the lowest *observed* FPR, though the confidence interval does not exclude FPR above 10%"。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 3 seeds 的 replication 不足以估计 seed-level variance

- 具体位置：Section 4.1 (page 4), Appendix B (page 12), Appendix L (page 21)
- 问题：Phase diagram 使用 3 seeds（42, 43, 44），intervention 使用 4 seeds。以 3 seeds 估计 variance 本身就是高度不确定的——3 个样本的标准差估计服从 2 自由度的 χ² 分布，CI 极宽。Appendix L (page 21) 报告 cross-seed consistency，但 Figure 10 的 stability 分析本身也只有 4 seeds，对 PermG K≥3 only 呈现 0/8 或 6/8 的 binary 行为，无法精细刻画 detection probability。
- 建议：增加 seeds 到 10+，或至少在 main text 中明确讨论 3-seed 限制对 detection rate 估计的不确定性（目前 Table 1 报告 "6/8" 但不附 binomial CI）。

**W2** [warning] MMCT 的 FPR-inverse weighting 缺乏理论依据

- 具体位置：Algorithm 1 (page 4), Appendix H (page 16), Appendix Q (page 25)
- 问题：MMCT 用 w_k = 1/max(FPR_k, ε) 对各方法加权。这是 ad-hoc 设计——论文未给出为什么 FPR 的倒数是最优权重的理论分析。Appendix Q (Table 18) 的 robustness check 显示 4 种 weighting scheme 下 PermG 的排名不变——但这可能只是因为 PermG 的 FPR 远低于 NaiveXCorr（6.7% vs 94.4%），任何合理的 weighting 都会得到相同结果。在方法 FPR 更接近时（如两个 FPR 都在 5-15%），weighting 的效果可能不同。
- 此外，FPR 估计来自同一个 null dataset（60 pairs），用于同时 (a) 估计 FPR 和 (b) 构造权重——虽然权重应用于 test data 而非 null data，但 FPR 估计的噪声会传播到权重中。
- 建议：增加 weighting 的理论 justification（如从 Bayesian model averaging 或 Neyman-Pearson 最优化角度），或使用 cross-validated FPR 估计。

**W3** [warning] Intervention 实验仅在 α=1.0 的 proof-of-concept，实用性论断过强

- 具体位置：Section 4.6 (page 7), Figure 9 (page 7), Appendix T (page 28)
- 问题：论文声称 "predictive cessation reduces peak perplexity by 64%"（abstract 和 Section 4.6），但这仅在 α=1.0——模型完全在合成数据上训练——的极端场景下验证。在更现实的部分污染场景（α=0.25-0.75），intervention 的效果未知。而论文的 Discussion (page 7-8) 和 Section 6 (page 8) 暗示了 deployment implications（"practical deployment"），这可能误导读者认为该方法已准备好用于实际部署。
- 此外，Appendix M (page 21) 的 CUSUM comparison 显示在 α=1.0 时，简单的 PPL threshold 也能在同一 generation 触发警报，canary-based 方法相对优势不明显。
- 建议：(1) 明确限定 intervention 的 claim 为 "α=1.0 proof-of-concept"，避免在 discussion 中暗示部署适用性；(2) 最好增加至少 α=0.50 的 intervention 实验；(3) 在 CUSUM comparison 中诚实说明在高 α 下两种方法差异不大。

**W4** [warning] Entropy 的 "leading" 行为可能是测量分辨率差异而非真实因果前序

- 具体位置：Section 5 (page 7-8), Appendix J (page 17), Appendix V (page 29)
- 问题：论文的 Design Principle 1 声称 "entropy responds before diversity under mode amplification"。但 Appendix J (page 17) 自己提出了 measurement artifact concern："entropy is a continuous quantity computed from the full probability distribution, while distinct-n is a discrete count computed from a finite sample." Entropy 对分布的微小变化更敏感，distinct-n 需要观测到足够多 token 才能反映变化。这意味着 entropy "先于" diversity 可能仅仅是因为连续测量比离散计数的 resolution 更高，而非存在真正的 temporal cascade。
- 论文尝试用 first-differencing 和 Fisher Z-transform（Appendix V, Table 25）来 address 这个问题，但这些分析本身依赖于同样的 measurement scale 差异。
- 建议：讨论中需要更明确地承认 measurement sensitivity explanation 无法被排除，并考虑使用 entropy 和 diversity 在可比尺度上的归一化版本进行 robustness check。

---

## 小问题（不影响接收）

- **P1**: Table 2 (page 8) 中 K≥4 和 K≥5 列全为 0%，实际上没有提供额外信息。考虑移除或合并。
- **P2**: Figure 1 (page 2) 的热力图颜色区分度在低 detection rate 区域（0/8 vs 0/8）不足，建议用不同 marker 标注 non-monotonic anomaly。
- **P3**: Section 3.1 中 Design Principle 1 和 2 的 formal statement 使用了 set notation（S_ε(p)={t:...}）但这些集合在后文实验中并未被 operationalize——实验直接使用了 threshold crossing，与 formal definition 有 gap。
- **P4**: Appendix G (page 15) 中 PermG 的 direction checking 描述应更早引入（Section 3.3 或 Algorithm 附近），因为 forward-only vs bidirectional 是理解 PermG FPR 的关键。
- **P5**: 论文使用 Claude (Anthropic) 作为 AI assistant（page 37），但未具体说明 AI 在哪些分析步骤中参与、输出是否经过人工验证——ARR 的 responsible NLP 要求可能需要更详细的 disclosure。

---

## 主要优势

1. **问题选取精准且及时**: Model collapse 检测是一个被大量理论/实证工作忽视的实际需求点。论文将问题从 "collapse exists" 推进到 "how do we *detect* it and *when* can we detect it"，这是一个有意义的研究方向转变。
2. **Multi-method comparison 是核心贡献**: "方法选择本身是最大变异源（κ=0.185，即 method choice 对 detection rate 的影响超过 contamination level 或 seed）"这一发现（Section 3.3, Figure 2）是 genuinely surprising 且对从业者有直接指导意义的。
3. **统计分析深度**: Specification curve analysis（1,160 specifications，Appendix D），Shapley value decomposition（Appendix P），partial correlation controlling for generation（Appendix V），AR(1) coefficient analysis（Appendix O）——这些远超一般 NLP empirical 论文的统计方法深度。
4. **诚实的 limitation 讨论**: 论文明确承认 Granger ≠ causation、FPR CI 宽、short-series regime、single-architecture 限制，没有过度 claim。这种 intellectual honesty 值得肯定。
5. **Appendix 的完整性**: 27 页附录覆盖了几乎所有可预见的 reviewer concern——robustness to T_min、weight scheme、observation window、cross-seed consistency、CUSUM comparison、power analysis 等。

---

## Questions to Authors

Q1: 能否提供至少一个额外架构（如 GPT-2 medium）在 α∈{0.25, 0.50, 0.75} 下的 phase diagram 数据？这是验证 three-regime structure 泛化性的最直接方式。如果计算资源不允许完整实验，即使只有 T=10、2 seeds 也比没有强。

Q2: MMCT 的 K≥3 consensus threshold 是如何选择的？论文在 Table 2 和 Figure 12 探讨了 K=2,3,4,5，但选择 K≥3 作为 default 的依据是什么？是否有基于 null-control data 的 optimal K 选择程序？

Q3: 对于 PermG FPR 的 4/60 false positives——这 4 个 false positive 来自哪些 seed 和 pair 组合？它们是否集中在特定 seed 或特定 canary→downstream pair（如 entropy→PPL）？如果集中分布，可能暗示 systematic bias 而非 random error。Appendix R.1 (page 26, Table 22) 提到 seed 45 和 s50 贡献了全部 4 个 false positives——这是否暗示 PermG 的 FPR 是 seed-dependent 的？

Q4: First-differencing 消除了 canary→perplexity 关联但保留了 canary→diversity——论文将此解读为 "temporal structure is channel-specific rather than global"（page 3）。但另一种解读是 first-differencing 对连续型变量（entropy）和离散型变量（distinct-n）的 power 不同——您如何排除这种可能？

Q5: Intervention 实验中，predictive cessation 在 generation 1 触发——这意味着模型只训练了 1 generation 就停止。在实际部署中，这是否意味着 canary-based 方法过于敏感，会在 collapse 尚未发生时就触发 alarm（given the blind zone below α≈0.45）？

---

## Missing References

- Dohmatob et al. (2024, 2025) 已引用。
- Shumailov et al. (2024) 已引用。
- 建议增加：Alemohammad et al. (2024) "Self-Consuming Generative Models with Shingled Losses" 如果有后续工作涉及检测方法。
- 建议增加：近期关于 data provenance 和 synthetic data watermarking 的工作（如 Kirchenbauer et al., 2023 "A Watermark for Large Language Models"），作为 alternative detection paradigm 的 related work。论文当前 related work（Section 2.2）仅讨论 statistical detection 方法，缺少 watermarking-based 检测这一重要替代路线。

---

[Reviewer 2 审稿结果]:
审稿完成。总结：

- **Overall: 3.0（Findings）**——一项系统性的实证比较研究，实验方法论严谨，但核心新颖性不足以支撑主会议。
- **3 个 Must-Fix**：(1) "detectability landscape" 本质是标准 dose-response 参数扫描的改名；(2) 跨架构泛化仅在 α=1.0 极端条件下验证，landscape 可迁移性未证实；(3) method sensitivity 作为 "primary finding" 实质是统计学常识。
- **5 个 Should-Fix**：MMCT 贡献薄弱、缺 Silberzahn et al. (2018) 关键引用、intervention 过于初步、entropy canary 的因果解释不足、核心内容过度依赖附录。
- **主要优势**：实验设计严谨（置换检验+FDR 校正+null control）、specification curve 引入有创意、方法推荐实用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1414 · 2026-05-25T07:24:39.637228+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，请标注 [AGREE] 或 [REBUT]，并说明理由。如果是 [REBUT]，请引用论文具体 Section/Table/Figure 提供证据。\n\n---\n\n## Reviewer 2 审稿意见（Overall: 3.0, Findings）\n\n### Must-Fix 问题\n\n**N1** [critical] \"Detectability landscape\" 的新颖性不足——本质上是标准的 dose-response 参数扫描\n- 论文将 \"detectability landscape\" 作为核心概念贡献（Contribution 2），但实际操作是在 α × T 的二维参数空间上扫描 PermG 检测率，拟合 sigmoid 边界，划分三个 regime（blind/onset/detection）。这是标准的 dose-response 分析，用 \"phase diagram\" 和 \"landscape\" 等物理学术语包装，但并未揭示超越参数扫描的结构性洞见。三个 regime 的划分本身取决于 PermG 的阈值行为（BH-FDR 校正后的二元判定），而非现象本身的内在结构。\n\n**N2** [critical] 跨架构泛化仅在 α=1.0 条件下验证，landscape 的可迁移性未得到证实\n- 详细的 landscape 分析仅在 Pythia-410M 上完成。跨架构评估仅在 α=1.0 极端条件下进行。4/15 条件不支持检测，暗示 landscape 可能是架构依赖的。论文标题暗示对 \"iterative model collapse\" 的普遍性刻画，但实际上是单一架构的详细分析。\n\n**N3** [critical] Method sensitivity 作为 \"primary finding\"（Contribution 1）的新颖性有限\n- 不同统计检验具有不同的功效和 Type I error rate，这对统计学背景读者并不意外。NaiveXCorr 在所有水平上检出 7-8/8 对，这不是 \"method sensitivity\"，而是 NaiveXCorr 没有恰当控制 false positives。将统计学常识包装为 \"primary finding\" 削弱论文可信度。\n\n### Should-Fix 问题\n\n**W1** MMCT 的方法论贡献薄弱——本质上是 FPR 逆权重的多数投票，标准 ensemble 技术。Shapley 分析显示 PermG 的边际贡献远超其他方法。\n\n**W2** 缺少 Silberzahn et al. (2018) \"Many Analysts, One Data Set\" 这一 many-analysts 范式的奠基性工作。\n\n**W3** Intervention（Section 4.6）仅在 α=1.0 条件下测试，过于初步但占据过多正文篇幅。\n\n**W4** Entropy 作为 canary metric 的因果解释不足——Appendix J 的 measurement artifact concern 应在主文讨论。\n\n**W5** 核心内容过度依赖附录——Design Principle 推导、方法论比较表、extended discussion 都在附录中。\n\n### 缺失参考文献\n1. Silberzahn et al. (2018) \"Many Analysts, One Data Set\"\n2. Mitchell et al. (2023) DetectGPT\n3. Gretton et al. (2012) MMD kernel two-sample test\n\n### Questions\n1. 如果在其他架构上做完整 landscape 扫描，blind zone 边界和过渡锐度是否一致？\n2. 是否考虑排除 NaiveXCorr 而非将其高 FPR 作为 method sensitivity 的证据？\n3. Entropy artifact concern 是否动摇核心 claim？\n4. MMCT 在什么场景下比单独使用 PermG 有优势？"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，请标注 [AGREE] 或 [REBUT]，并说明理由。如果是 [REBUT]，请引用论文具体 Section/Table/Figure 提供证据。\n\n---\n\n## Reviewer 2 审稿意见（Overall: 3.0, Findings）\n\n### Must-Fix 问题\n\n**N1** [critical] \"Detectability landscape\" 的新颖性不足——本质上是标准的 dose-response 参数扫描\n- 论文将 \"detectability landscape\" 作为核心概念贡献（Contribution 2），但实际操作是在 α × T 的二维参数空间上扫描 PermG 检测率，拟合 sigmoid 边界，划分三个 regime（blind/onset/detection）。这是标准的 dose-response 分析，用 \"phase diagram\" 和 \"landscape\" 等物理学术语包装，但并未揭示超越参数扫描的结构性洞见。三个 regime 的划分本身取决于 PermG 的阈值行为（BH-FDR 校正后的二元判定），而非现象本身的内在结构。\n\n**N2** [critical] 跨架构泛化仅在 α=1.0 条件下验证，landscape 的可迁移性未得到证实\n- 详细的 landscape 分析仅在 Pythia-410M 上完成。跨架构评估仅在 α=1.0 极端条件下进行。4/15 条件不支持检测，暗示 landscape 可能是架构依赖的。论文标题暗示对 \"iterative model collapse\" 的普遍性刻画，但实际上是单一架构的详细分析。\n\n**N3** [critical] Method sensitivity 作为 \"primary finding\"（Contribution 1）的新颖性有限\n- 不同统计检验具有不同的功效和 Type I error rate，这对统计学背景读者并不意外。NaiveXCorr 在所有水平上检出 7-8/8 对，这不是 \"method sensitivity\"，而是 NaiveXCorr 没有恰当控制 false positives。将统计学常识包装为 \"primary finding\" 削弱论文可信度。\n\n### Should-Fix 问题\n\n**W1** MMCT 的方法论贡献薄弱——本质上是 FPR 逆权重的多数投票，标准 ensemble 技术。Shapley 分析显示 PermG 的边际贡献远超其他方法。\n\n**W2** 缺少 Silberzahn et al. (2018) \"Many Analysts, One Data Set\" 这一 many-analysts 范式的奠基性工作。\n\n**W3** Intervention（Section 4.6）仅在 α=1.0 条件下测试，过于初步但占据过多正文篇幅。\n\n**W4** Entropy 作为 canary metric 的因果解释不足——Appendix J 的 measurement artifact concern 应在主文讨论。\n\n**W5** 核心内容过度依赖附录——Design Principle 推导、方法论比较表、extended discussion 都在附录中。\n\n### 缺失参考文献\n1. Silberzahn et al. (2018) \"Many Analysts, One Data Set\"\n2. Mitchell et al. (2023) DetectGPT\n3. Gretton et al. (2012) MMD kernel two-sample test\n\n### Questions\n1. 如果在其他架构上做完整 landscape 扫描，blind zone 边界和过渡锐度是否一致？\n2. 是否考虑排除 NaiveXCorr 而非将其高 FPR 作为 method sensitivity 的证据？\n3. Entropy artifact concern 是否动摇核心 claim？\n4. MMCT 在什么场景下比单独使用 PermG 有优势？"
  }
}
```

</details>

---


### Tool result

_source line 1415 · 2026-05-25T07:25:04.598568+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 24961
}
```

</details>

---


### Tool call

_source line 1416 · 2026-05-25T07:25:04.850341+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，请标注 [AGREE] 或 [REBUT]，并说明理由。如果是 [REBUT]，请引用论文具体 Section/Table/Figure 提供证据。\n\n---\n\n## Reviewer 1 审稿意见（Overall: 3.5, Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] Power-law detection boundary α_c(T) = A·T^{-γ} 的拟合严重欠定（3 free parameters, 3-4 data points）\n- 实质上是插值而非回归——剩余自由度为 0-1。γ 的 95% CI 为 [0.01, 2.10]。但 phase diagram 和 main text 的叙事仍以此为核心贡献展示。如果 boundary 的函数形式不可靠，phase diagram 的定量解读也不可靠。\n\n**N2** [critical] 核心 phase diagram 仅基于 Pythia-410M（3 seeds），泛化性证据不足\n- 标题暗示普适性，但 phase diagram 完全基于 Pythia-410M。跨架构验证仅在 α=1.0——collapse 最严重、检测最容易的场景。4 个 non-confirming 条件（Table 10）表明架构差异确实导致检测行为不同。\n\n**N3** [critical] PermG 的 FPR 置信区间 [1.8%, 16.2%] 过宽，无法确认其 FPR 在可接受范围内\n- 60 null pairs 不够。CI 上界 16.2% 远超 5% 的 3 倍。数据无法排除 PermG 真实 FPR 高达 16%，可能与 DiffXCorr（14.8%）无统计显著差异。\n\n### Should-Fix 问题\n\n**W1** 3 seeds 的 replication 不足以估计 seed-level variance（3 个样本的标准差估计服从 2 自由度的 χ² 分布，CI 极宽）。\n\n**W2** MMCT 的 FPR-inverse weighting 缺乏理论依据——w_k = 1/max(FPR_k, ε) 是 ad-hoc 设计，未给出理论最优性分析。FPR 估计来自同一 null dataset，噪声传播到权重中。\n\n**W3** Intervention 仅在 α=1.0 验证，但 Discussion 暗示了 deployment implications，可能误导读者。CUSUM comparison（Appendix M）显示在高 α 下两种方法差异不大。\n\n**W4** Entropy 的 \"leading\" 行为可能是测量分辨率差异（continuous vs discrete）而非真实因果前序。\n\n### 小问题\n- P1: Table 2 中 K≥4/5 列全为 0%，无额外信息\n- P2: Figure 1 低 detection rate 区域颜色区分度不足\n- P3: Design Principle 的 formal statement 与实验 operationalization 有 gap\n- P4: PermG direction checking 应更早引入\n- P5: AI assistant disclosure 不够详细\n\n### Questions\nQ1: 能否提供一个额外架构在 α∈{0.25, 0.50, 0.75} 下的 phase diagram？\nQ2: MMCT K≥3 的选择依据是什么？\nQ3: 4 个 false positives 来自哪些 seed/pair？是否 seed-dependent？\nQ4: First-differencing 对连续型和离散型变量的 power 差异如何排除？\nQ5: Canary-based 方法是否过于敏感，在 collapse 未发生时就触发 alarm？\n\n### 缺失参考文献\n- Kirchenbauer et al. (2023) 关于 LLM watermarking 的 alternative detection paradigm"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Must-Fix 和 Should-Fix 问题，请标注 [AGREE] 或 [REBUT]，并说明理由。如果是 [REBUT]，请引用论文具体 Section/Table/Figure 提供证据。\n\n---\n\n## Reviewer 1 审稿意见（Overall: 3.5, Borderline Conference）\n\n### Must-Fix 问题\n\n**N1** [critical] Power-law detection boundary α_c(T) = A·T^{-γ} 的拟合严重欠定（3 free parameters, 3-4 data points）\n- 实质上是插值而非回归——剩余自由度为 0-1。γ 的 95% CI 为 [0.01, 2.10]。但 phase diagram 和 main text 的叙事仍以此为核心贡献展示。如果 boundary 的函数形式不可靠，phase diagram 的定量解读也不可靠。\n\n**N2** [critical] 核心 phase diagram 仅基于 Pythia-410M（3 seeds），泛化性证据不足\n- 标题暗示普适性，但 phase diagram 完全基于 Pythia-410M。跨架构验证仅在 α=1.0——collapse 最严重、检测最容易的场景。4 个 non-confirming 条件（Table 10）表明架构差异确实导致检测行为不同。\n\n**N3** [critical] PermG 的 FPR 置信区间 [1.8%, 16.2%] 过宽，无法确认其 FPR 在可接受范围内\n- 60 null pairs 不够。CI 上界 16.2% 远超 5% 的 3 倍。数据无法排除 PermG 真实 FPR 高达 16%，可能与 DiffXCorr（14.8%）无统计显著差异。\n\n### Should-Fix 问题\n\n**W1** 3 seeds 的 replication 不足以估计 seed-level variance（3 个样本的标准差估计服从 2 自由度的 χ² 分布，CI 极宽）。\n\n**W2** MMCT 的 FPR-inverse weighting 缺乏理论依据——w_k = 1/max(FPR_k, ε) 是 ad-hoc 设计，未给出理论最优性分析。FPR 估计来自同一 null dataset，噪声传播到权重中。\n\n**W3** Intervention 仅在 α=1.0 验证，但 Discussion 暗示了 deployment implications，可能误导读者。CUSUM comparison（Appendix M）显示在高 α 下两种方法差异不大。\n\n**W4** Entropy 的 \"leading\" 行为可能是测量分辨率差异（continuous vs discrete）而非真实因果前序。\n\n### 小问题\n- P1: Table 2 中 K≥4/5 列全为 0%，无额外信息\n- P2: Figure 1 低 detection rate 区域颜色区分度不足\n- P3: Design Principle 的 formal statement 与实验 operationalization 有 gap\n- P4: PermG direction checking 应更早引入\n- P5: AI assistant disclosure 不够详细\n\n### Questions\nQ1: 能否提供一个额外架构在 α∈{0.25, 0.50, 0.75} 下的 phase diagram？\nQ2: MMCT K≥3 的选择依据是什么？\nQ3: 4 个 false positives 来自哪些 seed/pair？是否 seed-dependent？\nQ4: First-differencing 对连续型和离散型变量的 power 差异如何排除？\nQ5: Canary-based 方法是否过于敏感，在 collapse 未发生时就触发 alarm？\n\n### 缺失参考文献\n- Kirchenbauer et al. (2023) 关于 LLM watermarking 的 alternative detection paradigm"
  }
}
```

</details>

---


### Tool result

_source line 1417 · 2026-05-25T07:25:06.611469+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1761
}
```

</details>

---


### Assistant

_source line 1418 · 2026-05-25T07:25:11.510777+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 133

## Round 133

2 recorded events


### User

_source line 1419 · 2026-05-25T07:25:14.268848+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

总结：我给出 **Overall 3.5/5（Borderline Conference）**。论文方法论框架扎实（multi-method comparison、specification curve、Shapley decomposition），"方法选择本身是最大变异源"的发现有实际价值。但存在三个 critical 问题：

1. **Power-law boundary 过拟合**——3 参数拟合 3-4 个数据点，γ 的 CI 跨越 sub-linear 到 super-linear，函数形式不可约束
2. **单架构 phase diagram + α=1.0-only 跨架构验证**——"landscape" 的 claim 缺乏足够的泛化证据
3. **PermG FPR CI [1.8%, 16.2%]**——60 null pairs 不足以确认 FPR 在可接受范围内，"recommended detector" 的论断过强

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1420 · 2026-05-25T07:25:20.691070+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 134

## Round 134

2 recorded events


### User

_source line 1421 · 2026-05-25T07:26:27.464933+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R2-N1: "Detectability landscape" 本质上是标准 dose-response 参数扫描**

R2 认为 phase diagram 仅是 α × T 的二维参数扫描加 sigmoid 拟合。我部分反对：

1. **论文的核心发现不是 phase diagram 本身，而是 multi-method comparison**。Section 3.3 和 Figure 2 的 specification curve analysis（1,160 specifications）揭示的 κ=0.185 inter-method agreement 是定量的、特定于 model collapse 检测的发现，不能简化为"标准 dose-response"。标准 dose-response 不涉及多方法比较。

2. **Non-monotonic detection dip 是超越简单 dose-response 的结构**。Figure 3 (page 5) 和 Table 6 (page 5) 显示在 α=0.60 存在 non-monotonic detection anomaly——这不是 sigmoid 可以拟合的行为，论文专门在 Section 4.2 和 Appendix K 分析了其成因（entropy-diversity temporal decoupling）。纯参数扫描不会发现这种异常。

3. **但 R2 关于 regime 划分取决于 PermG 阈值行为的观点有道理**。论文 Table 2 (page 8) 的 K≥2 和 K≥3 列确实显示 regime 边界随共识阈值移动。这说明 three-regime structure 部分是分析选择的产物。

**总结**：R2 对"landscape"这个术语的 inflation concern 有道理，但将全部贡献简化为标准 dose-response 忽视了 multi-method comparison 和 non-monotonic anomaly 的发现。建议作者在修订中将"landscape"定位为"multi-method detection sensitivity profile"，降低物理学类比的 claim 强度。

---

**[AGREE] R2-N2: 跨架构泛化仅在 α=1.0**

完全同意。这与我的 N2 一致。Section 4.5 (Table 1, page 6) 的跨架构验证仅在 α=1.0（全量合成替换），而论文最有趣的发现——detection boundary 附近的 phase transition——没有任何跨架构验证。4/15 non-confirming 条件（Table 10, page 17）中 SmolLM3-3B 的 entropy decoupling 和 GPT-2 medium 的 calibration dependency 表明 landscape 确实是架构依赖的。

论文标题 "Characterizing the Detectability Landscape of Iterative Model Collapse" 暗示普适性，但实际上是 "Characterizing the Detectability Landscape of Pythia-410M under Iterative Model Collapse"。

---

**[REBUT] R2-N3: Method sensitivity 作为 primary finding 缺乏新颖性**

R2 认为"不同统计检验具有不同 power 和 Type I error"是统计学常识，不构成发现。我反对：

1. **定量幅度是新信息**。虽然统计学家知道不同检验有不同性质，但 FPR 从 6.7%（PermG）到 94.4%（NaiveXCorr）——跨越 14 倍——在同一数据集上，这个幅度是 domain-specific 的实证发现，不是先验可预测的。没有理论告诉我们 naive cross-correlation 在 model collapse 时序数据上的 FPR 会接近 100%。

2. **R2 对 NaiveXCorr 的解读不完整**。R2 说"NaiveXCorr 没有恰当控制 false positives"——但这恰恰是论文的 point。Section 3.3 (page 4) 明确解释 NaiveXCorr 检出 7-8/8 对的原因是"shared trend confounding"（共同趋势混淆），这是 model collapse 时序数据的特有陷阱（短序列、强趋势）。论文的贡献在于：(a) 识别这个 domain-specific 陷阱，(b) 量化其影响，(c) 提供替代方案（first-differencing, PermG）。

3. **对从业者有实际指导意义**。Model collapse 检测是新兴问题，大多数 practitioner 会首先尝试简单的 cross-correlation。论文的 warning（"naive cross-correlation will detect everywhere, including null"）是有实际价值的。

4. **但 R2 的表述 concern 有道理**——将此包装为"primary finding"（Contribution 1）确实拔高了。建议作者将其定位为"important methodological warning"而非"primary finding"。

---

### Should-Fix 问题

**[AGREE] R2-W1: MMCT 方法论贡献薄弱**

同意。Algorithm 1 (page 4) 的 MMCT 确实是 FPR-inverse weighted majority voting，在 ensemble learning 文献中是基本技术。Appendix P (page 24) 的 Shapley 分析显示 PermG 的 combined Shapley = −0.041（最接近零，即 FPR-FNR 最平衡），而 NaiveXCorr = +0.069（FPR 贡献最大）。这实际上说明 MMCT 的最大价值是**排除高 FPR 方法**（通过低权重），而非**组合互补方法**。如果 PermG 单独就是最优选择（Table 2 已显示），MMCT 的增量价值有限。

论文应降低对 MMCT 的方法论 claim（不要在 Contribution 列表中突出），或提供 MMCT 确实优于单独 PermG 的场景（目前没有这样的证据）。

---

**[AGREE] R2-W2: 缺少 Silberzahn et al. (2018)**

同意。Silberzahn et al. (2018) "Many Analysts, One Data Set" 是 multi-analyst/multi-method 范式的奠基性工作。论文的 core finding（method choice as primary variability source）直接回应了 Silberzahn 框架。Section 2 或 Section 3.3 应引用并讨论。

---

**[AGREE] R2-W3: Intervention 过于初步但占据过多篇幅**

同意，与我的 W3 一致。Section 4.6 (page 7) 的 intervention 仅在 α=1.0 验证，但在 8 页正文中占约 0.5 页——对于一个 proof-of-concept 来说偏多。Appendix M (page 21) 的 CUSUM comparison 还显示在 α=1.0 下简单 PPL threshold 效果相当。建议正文压缩到 1-2 段，将细节移入附录。

---

**[AGREE] R2-W4: Entropy measurement artifact 应在主文讨论**

同意，与我的 W4 一致。Appendix J (page 17) 讨论了 entropy 作为连续测量 vs. distinct-n 作为离散计数的 resolution 差异可能导致 apparent temporal precedence。这是对 Design Principle 1（entropy precedes diversity）的根本性替代解释，应在 Section 5 的 Discussion 中明确讨论，而非藏在附录里。

---

**[REBUT] R2-W5: 核心内容过度依赖附录**

部分反对。在 8 页正文限制下，论文需要在正文中覆盖：(a) 5 个检测方法，(b) phase diagram，(c) 跨架构验证，(d) intervention，(e) discussion + limitations。将 Design Principle 推导、方法论比较表、extended discussion 放入附录是**页面约束下的合理选择**，而非结构缺陷。

但我同意 R2 的 implicit concern：正文应该更 self-contained。目前 Section 3.1 的 Design Principle 提到 "see Appendix G for derivation" 但没有给出任何直觉解释——读者必须翻到附录才能理解为什么 entropy 被选为 canary metric。建议正文增加 1-2 句 intuitive justification。

---

### 缺失参考文献

**[AGREE]** Silberzahn et al. (2018) — 应引用，如上。

**[REBUT]** Mitchell et al. (2023) DetectGPT — DetectGPT 检测的是**单个文本是否由 AI 生成**（per-text classification），而本文检测的是**训练数据分布是否被 AI 生成文本污染**（distributional detection on time series）。问题设定完全不同。Section 2.2 的 related work 已通过 "our distributional framework differs from per-text classifiers" 划清了边界。引用 DetectGPT 可以增加完整性，但不是必须的。

**[REBUT]** Gretton et al. (2012) MMD — 论文使用的是 Granger causality 和 permutation tests，不涉及 kernel two-sample testing。MMD 在 model collapse 检测中的适用性不明确（MMD 需要两个样本集的分布比较，而论文处理的是时间序列上的 lead-lag 关系）。除非 R2 能说明 MMD 在本文设定中的具体适用性，这不是 missing reference。

---

### Questions 回应

**Q1**（跨架构 landscape 边界一致性）: 与我的 N2 和 Q1 一致——这是本文最大的 open question。如果在 GPT-2 medium 上做 α∈{0.25, 0.50, 0.75} 的扫描发现 phase boundary 不在 0.45 而在 0.30 或 0.60，论文的定量 claim 就需要重写。

**Q2**（排除 NaiveXCorr）: 这是个好建议。如果排除 NaiveXCorr，κ 值可能显著提高，method sensitivity 的 claim 就会弱化。论文应报告排除 NaiveXCorr 后的 κ 值以回应此质疑。

**Q3**（Entropy artifact 是否动摇 core claim）: 不完全动摇。即使 entropy 的 "leading" 行为部分来自 measurement resolution，canary→detection 的 pipeline 仍然有效——entropy 仍然是最早可用的信号，不论其"先于"diversity 的原因是因果还是测量。但 Design Principle 1 的因果叙事确实需要弱化。

**Q4**（MMCT vs. 单独 PermG）: 基于 Table 2 和 Appendix P 的证据，我认为 MMCT 在 PermG 已可用的情况下增量价值有限。MMCT 的理论优势是当单一方法不可靠时提供 robustness——但论文的数据恰恰显示 PermG 是最可靠的，MMCT 主要起到验证 PermG 结论的作用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1422 · 2026-05-25T07:27:24.194461+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 对 Reviewer 1 审稿意见的逐条回应后进行收敛判断。

**Reviewer 1 交叉回应要点速记：**

| R2 问题 | R1 立场 | 关键理由 |
|---------|---------|---------|
| R2-N1: Phase diagram = 标准 dose-response | **REBUT（部分）** | multi-method comparison + non-monotonic dip 超越简单参数扫描，但"landscape"术语确实 inflated |
| R2-N2: 跨架构仅 α=1.0 | **AGREE** | 与 R1 自己的 N2 一致，标题暗示普适性但实质仅 Pythia-410M |
| R2-N3: Method sensitivity 非新发现 | **REBUT** | FPR 14 倍差异是 domain-specific 实证发现，但同意不应作为 "primary finding" |
| R2-W1: MMCT 贡献薄弱 | **AGREE** | PermG 单独已最优，MMCT 增量价值有限 |
| R2-W2: 缺 Silberzahn (2018) | **AGREE** | 直接相关 |
| R2-W3: Intervention 过多篇幅 | **AGREE** | 与 R1-W3 一致 |
| R2-W4: Entropy artifact 应入主文 | **AGREE** | 与 R1-W4 一致 |
| R2-W5: 过度依赖附录 | **REBUT（部分）** | 8页限制下合理，但正文应更 self-contained |

**共识度较高**：7/8 个问题达成共识或部分共识。主要分歧仅在 N1（phase diagram 定位）和 N3（method sensitivity 新颖性）的程度判断上，但 R1 也承认了 R2 concern 的合理性。

Reviewer 2 的交叉回应到达后即可进行收敛判断。预计可在本轮收敛。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 135

## Round 135

2 recorded events


### User

_source line 1423 · 2026-05-25T07:27:27.230724+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **R2-N1**（landscape = dose-response）: [REBUT] — multi-method comparison 和 non-monotonic anomaly 超越了标准参数扫描，但"landscape"术语确实有 inflation
- **R2-N2**（跨架构仅 α=1.0）: [AGREE] — 与我的 N2 完全一致
- **R2-N3**（method sensitivity 不新颖）: [REBUT] — 14 倍 FPR 差异的定量幅度是 domain-specific 实证发现，但"primary finding"的定位确实偏高
- **R2-W1~W4**: 基本 [AGREE]，与我自己的审稿意见方向一致
- **R2-W5**（过度依赖附录）: [REBUT] — 8 页限制下合理，但正文应更 self-contained
- **缺失参考文献**: 同意 Silberzahn，反对 DetectGPT 和 MMD 的必要性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1424 · 2026-05-25T07:28:29.704523+00:00_

Reviewer 1 交叉回应已收录。8 个议题中 5 个 AGREE、3 个 partial REBUT（均承认对方部分合理），共识度高。

等待 Reviewer 2 对 Reviewer 1 审稿意见的交叉回应，两者到齐后进入报告合成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 136

## Round 136

16 recorded events


### User

_source line 1425 · 2026-05-25T07:28:29.711646+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的交叉回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Power-law boundary 拟合严重欠定**

同意。这是一个严重的定量可信度问题。从 Section 4.3（page 5）可以看到，sigmoid regression 的 95% CI 为 [0.25, 0.82]，而 Limitations（page 8）自己承认 γ 的 CI 为 [0.01, 2.10]——跨越两个数量级，本质上对 power-law 的函数形式没有约束力。3 个自由参数拟合 3-4 个数据点确实是插值而非回归。

补充发现：论文在 Appendix Y（Power Simulation）中尝试通过模拟来验证 boundary shape，但模拟本身依赖于同样的参数化形式，属于循环论证。如果作者能在至少 6-8 个 α 水平上重复实验以增加数据点，这个拟合才有统计意义。

**[AGREE] R1-N2: Phase diagram 仅基于 Pythia-410M，泛化性不足**

完全同意。这与我自己的 N2 观点一致。我补充一点：Table 10（Appendix J, page 17）显示的 4 个 non-confirming 条件中，GPT-2 Medium 和 SmolLM3-3B 的 failure modes 分别是 "precision"（仅检测正向信号）和 "decoupling"（entropy 非单调性），这些质性差异暗示不同架构可能需要不同的 landscape 参数化——single universal boundary 假设可能不成立。

**[AGREE] R1-N3: PermG FPR 置信区间过宽**

同意。60 null pairs 下 4/60 = 6.7% 的 exact binomial 95% CI 确实约为 [1.8%, 16.2%]。R1 正确指出 CI 上界 16.2% 与 DiffXCorr 的 14.8% 实测 FPR 重叠，使得 PermG 相对于 DiffXCorr 的 FPR 优势在统计上不显著。

不过我想补充一个 nuance：即使绝对 FPR 的 CI 很宽，论文的 comparative ranking（Figure 2, page 3）在方向上仍然是信息性的——PermG 的点估计 6.7% 是五种方法中最低的，NaiveXCorr 的 94.4% 显然在不同量级。问题不在于 ranking 方向，而在于论文将 "6.7%" 作为一个精确数字来使用（如 Conclusion "combining the lowest FPR 6.7%"），这给了读者一个比数据实际支持的更精确的印象。建议作者在正文中明确报告 CI，而非仅在附录中提及。

---

### Should-Fix 问题

**[AGREE] R1-W1: 3 seeds 不足以估计 seed-level variance**

同意。需要注意的是，论文在不同分析中使用了不同的 seed 数量——phase diagram 用 3 seeds（Figure 3 caption），null control 用 10 seeds/60 pairs（Section 4.1），cross-architecture 用 4 seeds。3 seeds 的标准差估计确实服从 2 自由度的 χ² 分布，CI 极宽。Appendix L（Cross-Seed Consistency, page 21）尝试用跨 seed 分析来解决这一问题，但分析本身也只有 3-4 seeds，无法从根本上改善估计精度。

**[AGREE] R1-W2: MMCT FPR-inverse weighting 缺乏理论依据**

同意，与我的 W1 一致。w_k = 1/max(FPR_k, ε) 是一个直觉合理但缺乏理论最优性保证的 ad-hoc 设计。Appendix Q（MMCT Weight Robustness Ablation）显示结果对权重方案不太敏感，这在一定程度上缓解了担忧——但 "对 ad-hoc 选择不敏感" 并不等同于 "有理论依据"。更根本的问题是，Appendix P 的 Shapley 分析（page 24, Figure 16-17）显示 PermG 的 coalition contribution 在所有组合中最稳定，这实际上质疑了 MMCT 相对于单独使用 PermG 的增量价值。

**[AGREE] R1-W3: Intervention 仅在 α=1.0 验证但暗示了部署含义**

同意，与我的 W3 一致。论文 Discussion（page 7-8）提到 "canary-based intervention" 的 deployment implications（如 "deployment recommendations" 列表），但实验证据仅来自一个极端条件。Appendix T（Intervention Threshold Sensitivity, page 28）确实做了阈值敏感性分析，但仍限于 α=1.0。Appendix F（CUSUM comparison, page 16）显示在高 α 下 CUSUM 与 canary 方法差异不大——这进一步削弱了 canary-based intervention 的独特价值主张。

**[AGREE] R1-W4: Entropy "leading" 可能是测量分辨率差异**

完全同意，这也是我自己的 W4。Appendix J（page 17）明确讨论了这一 concern："entropy is a continuous quantity computed from the full probability distribution, while distinct-n is a discrete count... Entropy can therefore respond to arbitrarily small distributional shifts that leave the token-level generation unchanged." 这段文字实际上承认了 R1 的担忧，但被放在审稿人可能不会阅读的 appendix 中。补充：Appendix V（Partial Correlation Analysis, page 30）试图用偏相关来排除 confound，但如果 confound 本身就是测量分辨率差异，偏相关无法解决这个问题——需要的是对 entropy 进行 discretization 后重新测试 Granger precedence 是否依然成立（论文未做此验证）。

---

### 小问题

**[AGREE] R1-P1**: Table 2 中 K≥4 和 K≥5 列全为 0%，确实无额外信息。可以删除或合并为脚注 "at K≥4, all metrics drop to 0%"。

**[AGREE] R1-P2**: Figure 1（phase diagram heatmap）在低 detection rate 区域颜色区分度确实不足。我在自己的审稿中也注意到这一问题。

**[AGREE] R1-P3**: Design Principle 1 和 2（Section 3.1, page 3）的 formal statement 使用信息论语言（"entropy responds before diversity"），但 operationalization 跳转到具体 metrics（distinct-3, ECE, PPL）时缺少中间推导步骤。Appendix X 有推导但主文中的 gap 影响可读性。

**[AGREE] R1-P4**: PermG direction checking（forward-only vs. bidirectional）是方法论的一个关键细节，Section 3.3 的 method description 对此介绍不足。Appendix G（page 15）提供了详细描述（"Direction checking: For each significant pair, we additionally test the reverse direction"），但这应该在主文中更早引入。

**[REBUT] R1-P5: AI assistant disclosure 不够详细**

不同意。Page 37 的 "Use of AI Assistants" section 明确列出了 Claude (Anthropic) 的三种使用类别：(1) Code — drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring; (2) Writing — drafting and revising paper sections, polishing prose, and reformatting LaTeX; (3) Literature — summarizing related papers to inform related-work section。这已经覆盖了主要使用场景，且格式清晰。ARR 的 AI 使用披露要求是 "disclose the use of AI assistants"，并无 "逐 prompt 记录" 的要求。现有披露在合规性和详细度上都是充分的。

---

### 缺失参考文献

**[AGREE] Kirchenbauer et al. (2023) — watermarking as alternative detection paradigm**

同意应该引用，但需注意方法论层面的本质区别：Kirchenbauer 的 watermarking 是一种 **proactive** 方法（在生成时注入信号），而本文的 distributional detection 是 **reactive** 方法（在事后分析分布漂移）。两者解决的是不同的问题设定——watermarking 需要对生成模型有控制权，而本文方法适用于无法控制上游模型的场景。论文应在 Related Work 中简要讨论这一区分，而非视二者为直接竞争方法。

---

### 综合评估

R1 的三个 Must-Fix 问题我全部同意，且认为这些问题与我自己审稿中识别的核心 concerns 高度一致：

| R1 问题 | R2 对应问题 | 核心共识 |
|---------|-----------|---------|
| R1-N1 (boundary fitting) | R2-N1 (landscape = dose-response) | landscape 的定量基础不足 |
| R1-N2 (single architecture) | R2-N2 (cross-arch at α=1.0 only) | 泛化性 claim 超出证据 |
| R1-N3 (PermG FPR CI) | R2-W1 (MMCT value over PermG) | 统计校准的精度不足以支撑强结论 |

R1 给出 3.5（Borderline Conference），我给出 3.0（Findings）。差异主要在于我对 "detectability landscape" 新颖性的评估更严格——我认为 landscape 本质上是 dose-response analysis 的 rebranding（我的 N1），R1 更多关注 landscape 的 quantitative reliability（R1-N1）。两个角度互补，但我认为即使修复了 fitting 问题，landscape 的概念新颖性仍然有限。

---

[Reviewer 2 审稿结果]:
交叉回应已完成。要点总结：

- R1 的 3 个 Must-Fix 全部 **AGREE**（boundary 拟合欠定、单架构 landscape、PermG FPR CI 过宽）
- 4 个 Should-Fix 全部 **AGREE**（seed 不足、MMCT ad-hoc、intervention 过于初步、entropy artifact）
- 小问题 P1-P4 **AGREE**，唯一 **REBUT** 的是 P5（AI disclosure 已足够详细，page 37 明确列出了三种使用类别）
- 两位 Reviewer 的核心共识：landscape 的定量基础和泛化性 claim 超出了现有证据的支撑范围

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1426 · 2026-05-25T07:28:52.585204+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 1427 · 2026-05-25T07:28:52.635905+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1428 · 2026-05-25T07:28:55.750491+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1429 · 2026-05-25T07:28:56.253486+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1430 · 2026-05-25T07:28:56.253809+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1431 · 2026-05-25T07:28:57.609675+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T07:15:57.344800+00:00\", \"completed_at\": \"2026-05-25T07:20:56.472846+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 2\", \"message\": \"Figure 1 phase diagram heatmap 单元格内数字标注（如 \\\"6/8\\\"、\\\"5/8\\\"）字号偏小，打印后可能难以辨认；色彩映射使用红-橙-黄-绿渐变，红绿色盲（deuteranopia）用户可能难以区分低检测区和高检测区——虽有数字标注作为冗余编码，仍建议换用 viridis 或 Okabe-Ito 友好色板\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"单页承载 3 个 display items（Figure 3 + Figure 4 + Table 1），Figure 4 的两个子面板 (a)(b) 非常小，轴标签和图例文字约为正文字号的 50-60%，低于 70% 可读性阈值\"}, {\"severity\": \"warning\", \"dimension\": \"page 6\", \"message\": \"单页承载 3 个 figures（Figure 5 + Figure 6 + Figure 7），虽各自传达不同 message，但视觉压缩严重，Figure 7 尤其紧凑\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"Figure 8 横向条形图 y 轴模型名称（如 \\\"Pythia-1.4B 48 s42\\\"）字号偏小，模型-seed 组合标签密集排列\"}, {\"severity\": \"warning\", \"dimension\": \"page 20\", \"message\": \"Figure 14（5 个子面板纵向堆叠）占页面约 75%，底部约 25% 空白；5 个独立条形图格式相似，可考虑合并为 grouped bar chart 或 heatmap 以节省空间\"}, {\"severity\": \"warning\", \"dimension\": \"page 24\", \"message\": \"Figures 16-17 之后底部约 30% 空白\"}, {\"severity\": \"warning\", \"dimension\": \"page 37\", \"message\": \"最后一页仅有 ~6 行文字（AI Assistants 声明尾部），底部约 85% 空白\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点。对于实证主导的论文，在第 1 页放置核心结果缩略图或 framework 概览图可帮助审稿人在 Abstract 阶段建立直觉——非硬性要求，但可提升第一印象\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 caption 较长但自包含，可独立理解——这是好的。建议在 caption 末尾补充阅读指引（如 \\\"darker = higher detection rate\\\"）进一步降低认知负担\"}, {\"severity\": \"info\", \"dimension\": \"pages 5-7\", \"message\": \"正文 display item 总数 12 个（9 fig + 2 tab + 1 algo），略高于实证论文 8 页典型的 5-8 个。每个 item 确实传达独立 message，但审稿人可能感到信息过载。如需压缩，Figure 3（detection rate surface）和 Figure 7（dose-response）在信息上有一定重叠，可考虑合并或将其一移至 appendix\"}, {\"severity\": \"info\", \"dimension\": \"pages 13-15\", 
…[truncated 784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 1432 · 2026-05-25T07:28:57.610218+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1433 · 2026-05-25T07:28:58.615548+00:00_

1	issues:
2	# ============================================================
3	# Round 1-11 历史 resolved — 保留跨轮次记录
4	# ============================================================
5	- id: "R1-N1"
6	  summary: "Ground-truth pairs 定义存在循环论证"
7	  category: method
8	  severity: critical
9	  status: resolved
10	  first_raised_round: 1
11	  last_seen_round: 1
12	  resolution: "Effect-size GT 重定义完成。"
13	  resolution_round: 1
14	
15	- id: "R1-N2"
16	  summary: "FPR=0% 标定仅基于单 seed"
17	  category: method
18	  severity: critical
19	  status: resolved
20	  first_raised_round: 1
21	  last_seen_round: 1
22	  resolution: "α=0.0 三 seed FPR 验证完成。"
23	  resolution_round: 1
24	
25	- id: "R1-N3"
26	  summary: "α=0.50 和 α=0.75 仅 1 seed"
27	  category: experiment
28	  severity: critical
29	  status: resolved
30	  first_raised_round: 1
31	  last_seen_round: 1
32	  resolution: "Multi-seed 补充完成。"
33	  resolution_round: 1
34	
35	- id: "R2-N1"
36	  summary: "核心方法论为计量经济学已有知识的直接迁移，新颖性有限"
37	  category: framing
38	  severity: critical
39	  status: resolved
40	  first_raised_round: 1
41	  last_seen_round: 2
42	  resolution: "Round 1 三层定位 reframe 完成。"
43	  resolution_round: 1
44	
45	- id: "R2-N2"
46	  summary: "α=0.75 multi-seed 实验未完成 + Appendix A 缺失"
47	  category: experiment
48	  severity: critical
49	  status: resolved
50	  first_raised_round: 1
51	  last_seen_round: 1
52	  resolution: "完成。"
53	  resolution_round: 1
54	
55	- id: "R2-N3"
56	  summary: "实验规模过窄"
57	  category: experiment
58	  severity: critical
59	  status: resolved
60	  first_raised_round: 1
61	  last_seen_round: 1
62	  resolution: "跨架构验证已扩展至 15 model-seed 组合。"
63	  resolution_round: 1
64	
65	- id: "R1-W1"
66	  summary: "Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致"
67	  category: writing
68	  severity: warning
69	  status: resolved
70	  first_raised_round: 1
71	  last_seen_round: 2
72	  resolution: "核心修复完成。"
73	  resolution_round: 1
74	
75	- id: "R1-W2"
76	  summary: "PermG 缺少 power analysis"
77	  category: metho
…[truncated 26498 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 1434 · 2026-05-25T07:28:58.616105+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1435 · 2026-05-25T07:28:58.667118+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1436 · 2026-05-25T07:37:10.117904+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "distrib_canary_collapse",
  "issues_yaml": "issues:\n# ============================================================\n# Round 1-11 历史 resolved — 保留跨轮次记录\n# ============================================================\n- id: \"R1-N1\"\n  summary: \"Ground-truth pairs 定义存在循环论证\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Effect-size GT 重定义完成。\"\n  resolution_round: 1\n\n- id: \"R1-N2\"\n  summary: \"FPR=0% 标定仅基于单 seed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"α=0.0 三 seed FPR 验证完成。\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"α=0.50 和 α=0.75 仅 1 seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Multi-seed 补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"核心方法论为计量经济学已有知识的直接迁移，新颖性有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Round 1 三层定位 reframe 完成。\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"α=0.75 multi-seed 实验未完成 + Appendix A 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"实验规模过窄\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"跨架构验证已扩展至 15 model-seed 组合。\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"核心修复完成。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"PermG 缺少 power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix N power analysis 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"75% spurious-signal rate headline 依赖 underpowered T-Y\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"α=0.75 单 seed borderline 结果不应出现在 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"Toda-Yamamoto 纳入理由表述不充分\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W6\"\n  summary: \"可重复性信息不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"超参补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-W3\"\n  summary: \"Token entropy canary 仅在 α=1.0 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"缺少独立 Limitations section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W5\"\n  summary: \"缺少 AI Writing Disclosure\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"缺少 canary→perplexity 为何 spurious 的深入解释\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF1\"\n  summary: \"遗漏 Granger & Newbold (1974)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF2\"\n  summary: \"遗漏 Hataya et al. (2023) 和 Seddik et al. (2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W1-old\"\n  summary: \"Citation key chen2025scales 与实际作者不匹配\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"F2-W3\"\n  summary: \"Section 3 承诺的三项附录内容缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"附录内容补充完成。\"\n  resolution_round: 3\n\n- id: \"F2-W8\"\n  summary: \"格式不合规：未使用 ACL 模板\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"ACL 模板迁移完成。\"\n  resolution_round: 2\n\n- id: \"F2-REF1\"\n  summary: \"遗漏 arXiv:2502.15654\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF1\"\n  summary: \"遗漏 arXiv:2602.10531\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF2\"\n  summary: \"遗漏 arXiv:2505.19046\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF3\"\n  summary: \"遗漏 arXiv:2510.16657\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF5\"\n  summary: \"Appendix H CUSUM 未引用 Page (1954)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F4-REF1\"\n  summary: \"遗漏 Truong & Truong (2026)\"\n  category: reference\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"引用已添加并在 §1/§2 讨论。\"\n  resolution_round: 6\n\n- id: \"F4-REF3\"\n  summary: \"遗漏 Benjamini & Yekutieli (2001)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§4 现引用 benjamini2001control。\"\n  resolution_round: 5\n\n- id: \"F2-REF3\"\n  summary: \"Dakos et al. (2012) + Schreiber (2000) + Phipson & Smyth (2010) 在 bib 中但正文未引用\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"引用补充完成。\"\n  resolution_round: 4\n\n- id: \"F6-W2\"\n  summary: \"页数可能超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"R8 PDF 审查确认主体 8 页合规。\"\n  resolution_round: 8\n\n- id: \"F2-W6b\"\n  summary: \"'Methodological pitfalls' 有 straw-man 倾向\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  resolution: \"全文已改为 'design considerations'。R8 fresh review 未再提及。\"\n  resolution_round: 8\n\n- id: \"F5-N2\"\n  summary: \"T=10 统计效力不足(power≈37%), sharp onset 可能是 power artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Power simulation 重写通过。Steepness comparison 写入正文。Dense α 证据额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 5\n  last_seen_round: 9\n\n- id: \"F2-W5\"\n  summary: \"Token entropy → distinct-n 机械耦合 confound 未排除\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Metric structure 分析完成。讨论已添加。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 9\n\n- id: \"F2-W2\"\n  summary: \"Specification curve analysis 定位不精确\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Appendix E 已改称 'systematic robustness analysis'。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F8-C2\"\n  summary: \"Discussion §6 过于简短(~100词)\"\n  category: writing\n  severity: major\n  status: resolved\n  resolution: \"Discussion 扩展至 20 行。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C3\"\n  summary: \"与 Schaeffer et al. (2025) '8 种 collapse 定义' 的关系讨论不充分\"\n  category: framing\n  severity: major\n  status: resolved\n  resolution: \"Schaeffer taxonomy 映射已添加到 related_work.tex。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C1\"\n  summary: \"Du & Tanaka-Ishii (2026) 引用三重错误\"\n  category: reference\n  severity: critical\n  status: resolved\n  resolution: \"§2 已修正。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R9-C1\"\n  summary: \"FPR CI method.tex 内部矛盾\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"FPR=10% MMCT sensitivity analysis 完成。\"\n  resolution_round: 9\n  first_raised_round: 9\n  last_seen_round: 9\n\n- id: \"F8-N1\"\n  summary: \"BH-FDR 在强正回归依赖下适用性讨论不充分\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"PRDS 假设适用性讨论已添加。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 10\n\n- id: \"F8-REF1\"\n  summary: \"遗漏引用：online/continual learning 下 model collapse 检测\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"related_work.tex 已添加 scope 区分。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F2-W11\"\n  summary: \"α_c SE=0.006 低估真实 seed 不确定性\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"被 F2-W4b/F2-W6 的统计基础问题覆盖。\"\n  resolution_round: 11\n  first_raised_round: 2\n  last_seen_round: 10\n\n- id: \"F8-N2\"\n  summary: \"未讨论为何选择经典 permutation Granger 而非 neural Granger causality\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"§4 已添加 T≤25 理由。§2 引用 neural Granger 文献。\"\n  resolution_round: 11\n  first_raised_round: 8\n  last_seen_round: 11\n\n- id: \"R9-REF2\"\n  summary: \"遗漏引用：Steegen et al. (2016) multiverse analysis\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 steegen2016increasing。\"\n  resolution_round: 11\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-REF2\"\n  summary: \"遗漏引用：Mitchell et al. (2023) DetectGPT\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 mitchell2023detectgpt。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-REF4\"\n  summary: \"遗漏引用：Padmakumar et al. (2024)\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 padmakumar2024writing。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n# ============================================================\n# 活跃 issues — Round 15 更新\n# ============================================================\n\n- id: \"F3-J4\"\n  summary: \"PermG FPR 超出 nominal 5%，architecture-dependent\"\n  category: method\n  severity: critical\n  status: in_progress\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 3\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 Must-Fix, R2 Should-Fix。GPT-2 null FPR 50%。CI [2.1%, 17.9%]。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-N3 Must-Fix。60 null pairs 下 4/60=6.7% CI [1.8%, 16.2%]，与 DiffXCorr 14.8% 重叠。R2 AGREE，补充：点估计 ranking 方向仍有信息价值，但论文不应将 6.7% 作为精确数字使用。\"\n  action_items:\n    - round: 14\n      action: \"C3: 增加 null seeds s52-s54 收窄 CI；写作已明确 comparative 定位\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"F2-W4b\"\n  summary: \"幂律边界 α_c(T) 拟合基础薄弱\"\n  category: framing\n  severity: critical\n  status: in_progress\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 Eq.(2) 降级为 empirical parametrization。B1 α=0.60 cross-seed 分析完成。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-N1 Must-Fix。3 自由参数拟合 3-4 数据点=插值非回归。γ CI [0.01,2.10] 跨两个数量级。Appendix Y power simulation 循环论证。R2 完全同意，建议 ≥6-8 个 α 水平。\"\n  action_items:\n    - round: 14\n      action: \"A2: Eq.(2)→empirical parametrization + Fig 1 fitted boundary [完成]; B1: α=0.60 v3/v4 + 含/排拟合对比 [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"F2-W2b\"\n  summary: \"'Detectability landscape' framing 承诺超过交付\"\n  category: framing\n  severity: critical\n  status: in_progress\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 最高共识 Must-Fix。A1 写作修复完成（Abstract 加 at α=1.0）。C2 OPT α=0.50 实验待执行。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 最高共识。R2-N1 认为 landscape=dose-response rebranding；R1 REBUT（multi-method + non-monotonic 超越 dose-response）但同意术语 inflation。R1-N2/R2-N2 双方 AGREE 跨架构仅 α=1.0 是最严重泛化缺陷。\"\n  action_items:\n    - round: 14\n      action: \"A1: Abstract scope 校准 [完成]; §4.5 标题加 at α=1.0 [完成]; C2: OPT-1.3B α=0.50 实验 [待GPU]\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"F2-W10\"\n  summary: \"Cross-architecture 'coupling preserved' 条件 post-hoc\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"与 F2-W2b 继续合并。GPT-2 null FPR 50%。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 与 F2-W2b 合并讨论。4/15 non-confirming 条件（SmolLM3-3B entropy decoupling, GPT-2 Medium calibration dependency）暗示 landscape 是 architecture-dependent。\"\n\n- id: \"R11-N1\"\n  summary: \"统计功率 β=0.66 CI [0.24,0.78] 使检测边界定量解读不可靠\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix, R2 Should-Fix。Limitations 已明确 coarse topology 定位。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 通过 R1-N1 boundary fitting 间接再次提及。3 seeds 的 variance 估计不足（R1-W1, R2 AGREE）加剧了此问题。\"\n  action_items:\n    - round: 14\n      action: \"Limitations 已更新 per-cell CI 宽度讨论。边界区域增加 seeds 需 GPU。\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"F2-W7\"\n  summary: \"Intervention 实验薄弱\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方一致。A3 降级措辞已验证。B3 naive baseline 分析完成。C1 N=5 实验待 GPU。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-W3/R2-W3 双方 AGREE。仅 α=1.0 验证但占正文 ~0.5 页偏多。CUSUM comparison 显示在高 α 下差异不大，削弱独特价值。Discussion 的 deployment recommendations 超出证据支撑。建议压缩到 1-2 段。\"\n  action_items:\n    - round: 14\n      action: \"A3: PoC 措辞验证 [完成]; B3: PPL threshold baseline [完成]; C1: N=5 intervention [待GPU]\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R12-N1\"\n  summary: \"Design Principle 'formal design rationale' 作为独立贡献 oversells\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"A6: SmolLM3-3B 3/8 + first-diff F=0 反例已写入 method.tex。待 Reviewer 验证。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-P3/R2 AGREE：Design Principle 1&2 formal statement 使用信息论语言但 operationalization 跳到具体 metrics 缺中间推导。正文仅引 Appendix 无直觉解释。\"\n\n- id: \"R14-N1\"\n  summary: \"Blind zone：α<0.50 已严重退化但所有检测方法均无信号\"\n  category: method\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [2]\n      note: \"A4: Limitations 已加 honest assessment（confirmation tool 定位）。待 Reviewer PASS。\"\n    - round: 15\n      reviewers: []\n      note: \"R15 未显式提及，可能已修复。待 Research Director 确认。\"\n  action_items:\n    - round: 14\n      action: \"A4: Limitations blind zone honest assessment [完成，待 Reviewer PASS]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R11-W1\"\n  summary: \"'3%-92%' FPR 范围含失效方法 NaiveXCorr\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R2-N3 间接涉及。R1 REBUT 认为 14x FPR 差异有 domain-specific 实证价值，但同意 'primary finding' 定位偏高。R2 的 Q2 建议排除 NaiveXCorr 后重算 κ。\"\n\n- id: \"R11-W2\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 通过 R1-N3（PermG FPR CI）间接涉及。每 cell 8 pairs 的精度不足是统计校准问题的底层原因。\"\n\n- id: \"R10-VIS1\"\n  summary: \"Table 1 / Figure 6 浮动超出 8 页主文边界\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 视觉审查：Pages 5-6 单页 3 个 display items，视觉压缩严重。Limitations 页面合规（page 8 确认）。\"\n\n- id: \"R12-W1\"\n  summary: \"写作信息密度过高，关键 findings 淹没在数字洪流中\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 未显式提及。视觉审查发现 pages 5-7 共 12 个 display items 略高于 8 页典型的 5-8 个。\"\n\n- id: \"R11-FMT1\"\n  summary: \"Abstract 脚注不标准\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n\n- id: \"R11-SYM1\"\n  summary: \"β 符号重用：统计功率 vs 幂律指数\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A10: β→π_det 替换\"\n      assigned_to: agent\n      status: done\n\n- id: \"F5-N1\"\n  summary: \"核心方法是计量经济学标准技术的直接移植\"\n  category: framing\n  severity: major\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 15\n  resolution: \"结构性天花板，novelty 来自 method-sensitivity finding 和 phase-diagram framing。\"\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"R15 R2-N3 从新角度重提：method sensitivity 作为 primary finding 缺乏新颖性。R1 REBUT 认为 14x FPR 差异是 domain-specific 实证发现。分歧在程度非方向。\"\n\n- id: \"F5-W1\"\n  summary: \"Design Principles 数学深度有限\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"A6 反例讨论已添加。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-P3 指出 formal statement→operationalization 缺中间推导。与 R12-N1 合并处理。\"\n\n- id: \"F2-W1\"\n  summary: \"α=0.60 sync dip：mechanism unexplained\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1]\n      note: \"R15 R1 在 REBUT R2-N1 时引用 non-monotonic detection dip（Figure 3, Table 6）作为超越 dose-response 的证据。α=0.60 anomaly 被视为正面发现而非问题。\"\n  action_items:\n    - round: 14\n      action: \"B1: cross-seed 一致性 (2/2 seeds 均 0/8) + 含/排拟合对比已写入 Appendix [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"F2-W6\"\n  summary: \"Detection boundary 验证不足\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-N1 boundary fitting 欠定问题的直接后果。需要更多 α 水平数据点。\"\n\n- id: \"R10-MF5\"\n  summary: \"'Five families (345M-6.9B)' 数字自洽性\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 未显式提及。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 14\n      action: \"A1: Abstract 加 'at α=1.0' + '11/15 conditions' + '四个 non-confirming cases' [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R10-SF2\"\n  summary: \"Data accumulation vs replacement paradigm 未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n\n- id: \"R10-SF3\"\n  summary: \"单一解码策略需定性讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n\n- id: \"R10-SF5\"\n  summary: \"Bivariate confounding\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A5: Granger 局限扩展讨论（partial correlation 已在 §5）[已有]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R10-SF6\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF7\"\n  summary: \"3-4 seeds replication power 有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-W1 Should-Fix。3 seeds 标准差估计服从 2 自由度 χ²，CI 极宽。Appendix L 跨 seed 分析也仅 3-4 seeds。R2 完全同意。\"\n\n- id: \"R11-VIS2\"\n  summary: \"Pages 5-6 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n\n- id: \"F8-W2\"\n  summary: \"Figure 子图内文字偏小\"\n  category: format\n  severity: minor\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 视觉审查再次发现：Page 5 Figure 4 轴标签约正文字号 50-60%（低于 70% 阈值），Page 7 Figure 8 y 轴标签偏小。\"\n  action_items:\n    - round: 14\n      action: \"A8: Figures 2/4/6 labels 放大至 ≥8pt [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R9-m5\"\n  summary: \"Granger 'precedence' vs 'causality' 术语不一致\"\n  category: writing\n  severity: minor\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A10: 全文统一为 Granger precedence [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"F2-W9b\"\n  summary: \"孤立 bib entries\"\n  category: writing\n  severity: minor\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A9: 移除 14 个未引用条目 [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"F6-C2\"\n  summary: \"buffa2026entropy 引用标题不匹配\"\n  category: reference\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n\n- id: \"R13-W1\"\n  summary: \"MMCT K≥3 共识框架 K 选择缺乏理论最优性证明\"\n  category: method\n  severity: major\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-W2/R2-W1 双方 AGREE。MMCT 是 FPR-inverse weighted majority voting（基本技术）。Shapley 分析显示 PermG 已最优。MMCT 增量价值有限。w_k=1/max(FPR_k,ε) ad-hoc 无理论保证。Table 2 K≥4/K≥5 全 0% 无额外信息。\"\n  action_items:\n    - round: 14\n      action: \"A7: Discussion 加 K calibration 讨论 [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R13-W2\"\n  summary: \"α=0.60 异常排除对幂律拟合的根本性影响\"\n  category: method\n  severity: major\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1]\n      note: \"R15 R1 在 REBUT R2-N1 时将 α=0.60 non-monotonic anomaly 视为超越 dose-response 的结构性发现。与 F2-W4b boundary fitting 问题关联。\"\n  action_items:\n    - round: 14\n      action: \"B1: cross-seed 一致性 + 含/排拟合对比 [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R13-W3\"\n  summary: \"跨架构验证仅在 α=1.0 最极端条件进行\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 最高共识 Must-Fix。R1-N2/R2-N2 双方 AGREE。论文标题暗示普适性但实际是 Pythia-410M landscape。4/15 non-confirming 条件显示 architecture-dependent。\"\n  action_items:\n    - round: 14\n      action: \"C2: OPT-1.3B α=0.50 实验 [待GPU]\"\n      assigned_to: agent\n      status: open\n\n- id: \"R13-W4\"\n  summary: \"Abstract 'substantially reduces peak perplexity' 超出证据强度\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A3: 已确认 Abstract/Conclusion 无 'substantially' [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R13-W5\"\n  summary: \"偏相关分析（控制 generation number）缺失\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A5: §5 已有 partial correlation 35/36 讨论 [已有]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R13-REF1\"\n  summary: \"遗漏引用：Dakos et al. (2008, 2012) 早期预警信号核心实证方法论\"\n  category: reference\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A9: bib 清理中已移除未引用条目（含 dakos2008, dakos2012）\"\n      assigned_to: agent\n      status: done\n\n- id: \"R13-REF3\"\n  summary: \"Granger causality 标准局限性（observational equivalence, Lucas critique）未讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A5: Granger 局限扩展已在 §5 [已有]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R14-W1\"\n  summary: \"MMCT 权重估计噪声未讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-W2/R2-W1 的 MMCT 弱贡献共识间接涉及。\"\n\n- id: \"R14-W2\"\n  summary: \"Granger 检验在 T=10 短序列上 power 极低\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n\n- id: \"R14-M1\"\n  summary: \"bib 格式不一致\"\n  category: writing\n  severity: minor\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A9: bib 清理和格式统一 [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R10-SF4\"\n  summary: \"方法敏感性 '3%-92%' framing\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-REF3\"\n  summary: \"遗漏引用：Runge et al. (2019) PCMCI\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R9-REF1\"\n  summary: \"遗漏引用：Gerstgrasser et al. (2024) data accumulation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-m1\"\n  summary: \"Figure 3 y 轴标签含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m2\"\n  summary: \"Table 2 'x/8' 列含义未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m3\"\n  summary: \"§5.1 前向引用缺上下文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-REF5\"\n  summary: \"遗漏引用：Montgomery SPC\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"F4-REF5\"\n  summary: \"bib first author mismatch: dey2024breaking\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 4\n  last_seen_round: 11\n\n- id: \"F8-N3\"\n  summary: \"Appendix 关键验证内容应纳入正文\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R2-W5 认为正文不 self-contained。R1 partial REBUT（8 页限制下合理）但同意需增加直觉解释。R1-W4/R2-W4 特别指出 Appendix J entropy artifact 应提升到 §5 Discussion。\"\n\n- id: \"F8-N4\"\n  summary: \"predict-then-verify post-hoc adjustment 嫌疑\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R12-REF1\"\n  summary: \"遗漏引用：Adams & MacKay (2007) Bayesian online changepoint detection\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-REF2\"\n  summary: \"遗漏引用：Papana et al. (2013) / Siggiridou & Kugiumtzis (2016)\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W2\"\n  summary: \"Eq.1 sigmoid 上界 0.70 选择理由未说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W3\"\n  summary: \"α 采样间隔不均匀（0.10→0.25 跳跃）理由未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W4\"\n  summary: \"Schaeffer et al. 8 种 collapse 定义中本文使用哪种未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R13-REF2\"\n  summary: \"遗漏引用：Lenton et al. (2008) 气候 tipping elements\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n\n- id: \"R13-VIS1\"\n  summary: \"主文 8 页 0 个 table，所有定量结果表格在 appendix\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n\n- id: \"R13-VIS2\"\n  summary: \"前两页无任何 display item，Figure 1 直到第 3 页\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n\n# ============================================================\n# Round 15 新增 issues\n# ============================================================\n\n- id: \"R15-REF1\"\n  summary: \"遗漏引用：Silberzahn et al. (2018) Many Analysts, One Data Set\"\n  category: reference\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"论文 method sensitivity finding 直接回应 Silberzahn 的 multi-analyst/multi-method 框架。双方 AGREE 应在 §2 或 §3.3 引用。\"\n\n- id: \"R15-REF2\"\n  summary: \"遗漏引用：Kirchenbauer et al. (2023) watermarking as alternative paradigm\"\n  category: reference\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"Watermarking (proactive) vs distributional detection (reactive) 的方法论区分应在 Related Work 简要讨论。R2 AGREE。R1 未强调。\"\n\n- id: \"R15-W1\"\n  summary: \"Entropy artifact（测量分辨率差异）应从 Appendix J 提升到 §5 Discussion\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W4/R2-W4 双方 AGREE。Appendix J 承认 entropy 是连续量、distinct-n 是离散计数——对 Design Principle 1 的根本性替代解释。R2 补充：需对 entropy 做 discretization 后重新测试 Granger precedence。此前 F2-W5 曾在 R9 标记 resolved，但 R15 从新角度（主文可见性 + discretization 验证）重新提出。\"\n\n- id: \"R15-W2\"\n  summary: \"排除 NaiveXCorr 后 κ 值应报告，以校准 method sensitivity claim\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"R2 Q2：如果排除 NaiveXCorr（94.4% FPR 的失效方法），κ 可能显著提高，method sensitivity claim 需要重新校准。与 R11-W1 关联。\"\n\n- id: \"R15-W3\"\n  summary: \"Method sensitivity 定位应从 'primary finding' 降为 'methodological warning'\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-N3 认为统计学常识不构成 finding。R1 REBUT（14x FPR 差异是 domain-specific 实证发现）但同意 Contribution 1 定位偏高。共识：降为 methodological warning，Contribution 列表重新排序。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "issues_yaml": "issues:\n# ============================================================\n# Round 1-11 历史 resolved — 保留跨轮次记录\n# ============================================================\n- id: \"R1-N1\"\n  summary: \"Ground-truth pairs 定义存在循环论证\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Effect-size GT 重定义完成。\"\n  resolution_round: 1\n\n- id: \"R1-N2\"\n  summary: \"FPR=0% 标定仅基于单 seed\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"α=0.0 三 seed FPR 验证完成。\"\n  resolution_round: 1\n\n- id: \"R1-N3\"\n  summary: \"α=0.50 和 α=0.75 仅 1 seed\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"Multi-seed 补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-N1\"\n  summary: \"核心方法论为计量经济学已有知识的直接迁移，新颖性有限\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Round 1 三层定位 reframe 完成。\"\n  resolution_round: 1\n\n- id: \"R2-N2\"\n  summary: \"α=0.75 multi-seed 实验未完成 + Appendix A 缺失\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-N3\"\n  summary: \"实验规模过窄\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"跨架构验证已扩展至 15 model-seed 组合。\"\n  resolution_round: 1\n\n- id: \"R1-W1\"\n  summary: \"Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"核心修复完成。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"PermG 缺少 power analysis\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 2\n  resolution: \"Appendix N power analysis 完成。\"\n  resolution_round: 1\n\n- id: \"R1-W3\"\n  summary: \"75% spurious-signal rate headline 依赖 underpowered T-Y\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W4\"\n  summary: \"α=0.75 单 seed borderline 结果不应出现在 abstract\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W5\"\n  summary: \"Toda-Yamamoto 纳入理由表述不充分\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R1-W6\"\n  summary: \"可重复性信息不足\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"超参补充完成。\"\n  resolution_round: 1\n\n- id: \"R2-W3\"\n  summary: \"Token entropy canary 仅在 α=1.0 验证\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W4\"\n  summary: \"缺少独立 Limitations section\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W5\"\n  summary: \"缺少 AI Writing Disclosure\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W6\"\n  summary: \"缺少 canary→perplexity 为何 spurious 的深入解释\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF1\"\n  summary: \"遗漏 Granger & Newbold (1974)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-REF2\"\n  summary: \"遗漏 Hataya et al. (2023) 和 Seddik et al. (2024)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"R2-W1-old\"\n  summary: \"Citation key chen2025scales 与实际作者不匹配\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"完成。\"\n  resolution_round: 1\n\n- id: \"F2-W3\"\n  summary: \"Section 3 承诺的三项附录内容缺失\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"附录内容补充完成。\"\n  resolution_round: 3\n\n- id: \"F2-W8\"\n  summary: \"格式不合规：未使用 ACL 模板\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"ACL 模板迁移完成。\"\n  resolution_round: 2\n\n- id: \"F2-REF1\"\n  summary: \"遗漏 arXiv:2502.15654\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 2\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF1\"\n  summary: \"遗漏 arXiv:2602.10531\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF2\"\n  summary: \"遗漏 arXiv:2505.19046\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF3\"\n  summary: \"遗漏 arXiv:2510.16657\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F3-REF5\"\n  summary: \"Appendix H CUSUM 未引用 Page (1954)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 3\n  resolution: \"引用已添加。\"\n  resolution_round: 4\n\n- id: \"F4-REF1\"\n  summary: \"遗漏 Truong & Truong (2026)\"\n  category: reference\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 6\n  resolution: \"引用已添加并在 §1/§2 讨论。\"\n  resolution_round: 6\n\n- id: \"F4-REF3\"\n  summary: \"遗漏 Benjamini & Yekutieli (2001)\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"§4 现引用 benjamini2001control。\"\n  resolution_round: 5\n\n- id: \"F2-REF3\"\n  summary: \"Dakos et al. (2012) + Schreiber (2000) + Phipson & Smyth (2010) 在 bib 中但正文未引用\"\n  category: reference\n  severity: minor\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"引用补充完成。\"\n  resolution_round: 4\n\n- id: \"F6-W2\"\n  summary: \"页数可能超限\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 8\n  resolution: \"R8 PDF 审查确认主体 8 页合规。\"\n  resolution_round: 8\n\n- id: \"F2-W6b\"\n  summary: \"'Methodological pitfalls' 有 straw-man 倾向\"\n  category: framing\n  severity: major\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 8\n  resolution: \"全文已改为 'design considerations'。R8 fresh review 未再提及。\"\n  resolution_round: 8\n\n- id: \"F5-N2\"\n  summary: \"T=10 统计效力不足(power≈37%), sharp onset 可能是 power artifact\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"Power simulation 重写通过。Steepness comparison 写入正文。Dense α 证据额外支撑。\"\n  resolution_round: 9\n  first_raised_round: 5\n  last_seen_round: 9\n\n- id: \"F2-W5\"\n  summary: \"Token entropy → distinct-n 机械耦合 confound 未排除\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Metric structure 分析完成。讨论已添加。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 9\n\n- id: \"F2-W2\"\n  summary: \"Specification curve analysis 定位不精确\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"Appendix E 已改称 'systematic robustness analysis'。\"\n  resolution_round: 9\n  first_raised_round: 2\n  last_seen_round: 8\n\n- id: \"F8-C2\"\n  summary: \"Discussion §6 过于简短(~100词)\"\n  category: writing\n  severity: major\n  status: resolved\n  resolution: \"Discussion 扩展至 20 行。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C3\"\n  summary: \"与 Schaeffer et al. (2025) '8 种 collapse 定义' 的关系讨论不充分\"\n  category: framing\n  severity: major\n  status: resolved\n  resolution: \"Schaeffer taxonomy 映射已添加到 related_work.tex。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F8-C1\"\n  summary: \"Du & Tanaka-Ishii (2026) 引用三重错误\"\n  category: reference\n  severity: critical\n  status: resolved\n  resolution: \"§2 已修正。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R9-C1\"\n  summary: \"FPR CI method.tex 内部矛盾\"\n  category: method\n  severity: critical\n  status: resolved\n  resolution: \"FPR=10% MMCT sensitivity analysis 完成。\"\n  resolution_round: 9\n  first_raised_round: 9\n  last_seen_round: 9\n\n- id: \"F8-N1\"\n  summary: \"BH-FDR 在强正回归依赖下适用性讨论不充分\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"PRDS 假设适用性讨论已添加。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 10\n\n- id: \"F8-REF1\"\n  summary: \"遗漏引用：online/continual learning 下 model collapse 检测\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"related_work.tex 已添加 scope 区分。\"\n  resolution_round: 9\n  first_raised_round: 8\n  last_seen_round: 9\n\n- id: \"F2-W11\"\n  summary: \"α_c SE=0.006 低估真实 seed 不确定性\"\n  category: method\n  severity: major\n  status: resolved\n  resolution: \"被 F2-W4b/F2-W6 的统计基础问题覆盖。\"\n  resolution_round: 11\n  first_raised_round: 2\n  last_seen_round: 10\n\n- id: \"F8-N2\"\n  summary: \"未讨论为何选择经典 permutation Granger 而非 neural Granger causality\"\n  category: method\n  severity: minor\n  status: resolved\n  resolution: \"§4 已添加 T≤25 理由。§2 引用 neural Granger 文献。\"\n  resolution_round: 11\n  first_raised_round: 8\n  last_seen_round: 11\n\n- id: \"R9-REF2\"\n  summary: \"遗漏引用：Steegen et al. (2016) multiverse analysis\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 steegen2016increasing。\"\n  resolution_round: 11\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-REF2\"\n  summary: \"遗漏引用：Mitchell et al. (2023) DetectGPT\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 mitchell2023detectgpt。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-REF4\"\n  summary: \"遗漏引用：Padmakumar et al. (2024)\"\n  category: reference\n  severity: minor\n  status: resolved\n  resolution: \"论文 §2 已引用 padmakumar2024writing。\"\n  resolution_round: 11\n  first_raised_round: 10\n  last_seen_round: 11\n\n# ============================================================\n# 活跃 issues — Round 15 更新\n# ============================================================\n\n- id: \"F3-J4\"\n  summary: \"PermG FPR 超出 nominal 5%，architecture-dependent\"\n  category: method\n  severity: critical\n  status: in_progress\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 3\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 R1 Must-Fix, R2 Should-Fix。GPT-2 null FPR 50%。CI [2.1%, 17.9%]。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-N3 Must-Fix。60 null pairs 下 4/60=6.7% CI [1.8%, 16.2%]，与 DiffXCorr 14.8% 重叠。R2 AGREE，补充：点估计 ranking 方向仍有信息价值，但论文不应将 6.7% 作为精确数字使用。\"\n  action_items:\n    - round: 14\n      action: \"C3: 增加 null seeds s52-s54 收窄 CI；写作已明确 comparative 定位\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"F2-W4b\"\n  summary: \"幂律边界 α_c(T) 拟合基础薄弱\"\n  category: framing\n  severity: critical\n  status: in_progress\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 Eq.(2) 降级为 empirical parametrization。B1 α=0.60 cross-seed 分析完成。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-N1 Must-Fix。3 自由参数拟合 3-4 数据点=插值非回归。γ CI [0.01,2.10] 跨两个数量级。Appendix Y power simulation 循环论证。R2 完全同意，建议 ≥6-8 个 α 水平。\"\n  action_items:\n    - round: 14\n      action: \"A2: Eq.(2)→empirical parametrization + Fig 1 fitted boundary [完成]; B1: α=0.60 v3/v4 + 含/排拟合对比 [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"F2-W2b\"\n  summary: \"'Detectability landscape' framing 承诺超过交付\"\n  category: framing\n  severity: critical\n  status: in_progress\n  resolution: \"\"\n  resolution_round: null\n  first_raised_round: 2\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 最高共识 Must-Fix。A1 写作修复完成（Abstract 加 at α=1.0）。C2 OPT α=0.50 实验待执行。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 最高共识。R2-N1 认为 landscape=dose-response rebranding；R1 REBUT（multi-method + non-monotonic 超越 dose-response）但同意术语 inflation。R1-N2/R2-N2 双方 AGREE 跨架构仅 α=1.0 是最严重泛化缺陷。\"\n  action_items:\n    - round: 14\n      action: \"A1: Abstract scope 校准 [完成]; §4.5 标题加 at α=1.0 [完成]; C2: OPT-1.3B α=0.50 实验 [待GPU]\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"F2-W10\"\n  summary: \"Cross-architecture 'coupling preserved' 条件 post-hoc\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"与 F2-W2b 继续合并。GPT-2 null FPR 50%。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 与 F2-W2b 合并讨论。4/15 non-confirming 条件（SmolLM3-3B entropy decoupling, GPT-2 Medium calibration dependency）暗示 landscape 是 architecture-dependent。\"\n\n- id: \"R11-N1\"\n  summary: \"统计功率 β=0.66 CI [0.24,0.78] 使检测边界定量解读不可靠\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R1 Must-Fix, R2 Should-Fix。Limitations 已明确 coarse topology 定位。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 通过 R1-N1 boundary fitting 间接再次提及。3 seeds 的 variance 估计不足（R1-W1, R2 AGREE）加剧了此问题。\"\n  action_items:\n    - round: 14\n      action: \"Limitations 已更新 per-cell CI 宽度讨论。边界区域增加 seeds 需 GPU。\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"F2-W7\"\n  summary: \"Intervention 实验薄弱\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"R14 双方一致。A3 降级措辞已验证。B3 naive baseline 分析完成。C1 N=5 实验待 GPU。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-W3/R2-W3 双方 AGREE。仅 α=1.0 验证但占正文 ~0.5 页偏多。CUSUM comparison 显示在高 α 下差异不大，削弱独特价值。Discussion 的 deployment recommendations 超出证据支撑。建议压缩到 1-2 段。\"\n  action_items:\n    - round: 14\n      action: \"A3: PoC 措辞验证 [完成]; B3: PPL threshold baseline [完成]; C1: N=5 intervention [待GPU]\"\n      assigned_to: agent\n      status: in_progress\n\n- id: \"R12-N1\"\n  summary: \"Design Principle 'formal design rationale' 作为独立贡献 oversells\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"A6: SmolLM3-3B 3/8 + first-diff F=0 反例已写入 method.tex。待 Reviewer 验证。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-P3/R2 AGREE：Design Principle 1&2 formal statement 使用信息论语言但 operationalization 跳到具体 metrics 缺中间推导。正文仅引 Appendix 无直觉解释。\"\n\n- id: \"R14-N1\"\n  summary: \"Blind zone：α<0.50 已严重退化但所有检测方法均无信号\"\n  category: method\n  severity: major\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n    - round: 14\n      reviewers: [2]\n      note: \"A4: Limitations 已加 honest assessment（confirmation tool 定位）。待 Reviewer PASS。\"\n    - round: 15\n      reviewers: []\n      note: \"R15 未显式提及，可能已修复。待 Research Director 确认。\"\n  action_items:\n    - round: 14\n      action: \"A4: Limitations blind zone honest assessment [完成，待 Reviewer PASS]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R11-W1\"\n  summary: \"'3%-92%' FPR 范围含失效方法 NaiveXCorr\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R2-N3 间接涉及。R1 REBUT 认为 14x FPR 差异有 domain-specific 实证价值，但同意 'primary finding' 定位偏高。R2 的 Q2 建议排除 NaiveXCorr 后重算 κ。\"\n\n- id: \"R11-W2\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 通过 R1-N3（PermG FPR CI）间接涉及。每 cell 8 pairs 的精度不足是统计校准问题的底层原因。\"\n\n- id: \"R10-VIS1\"\n  summary: \"Table 1 / Figure 6 浮动超出 8 页主文边界\"\n  category: format\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 视觉审查：Pages 5-6 单页 3 个 display items，视觉压缩严重。Limitations 页面合规（page 8 确认）。\"\n\n- id: \"R12-W1\"\n  summary: \"写作信息密度过高，关键 findings 淹没在数字洪流中\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 未显式提及。视觉审查发现 pages 5-7 共 12 个 display items 略高于 8 页典型的 5-8 个。\"\n\n- id: \"R11-FMT1\"\n  summary: \"Abstract 脚注不标准\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 11\n  last_seen_round: 11\n\n- id: \"R11-SYM1\"\n  summary: \"β 符号重用：统计功率 vs 幂律指数\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A10: β→π_det 替换\"\n      assigned_to: agent\n      status: done\n\n- id: \"F5-N1\"\n  summary: \"核心方法是计量经济学标准技术的直接移植\"\n  category: framing\n  severity: major\n  status: wont_fix\n  first_raised_round: 5\n  last_seen_round: 15\n  resolution: \"结构性天花板，novelty 来自 method-sensitivity finding 和 phase-diagram framing。\"\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"R15 R2-N3 从新角度重提：method sensitivity 作为 primary finding 缺乏新颖性。R1 REBUT 认为 14x FPR 差异是 domain-specific 实证发现。分歧在程度非方向。\"\n\n- id: \"F5-W1\"\n  summary: \"Design Principles 数学深度有限\"\n  category: framing\n  severity: major\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 15\n  mentions:\n    - round: 14\n      reviewers: [1, 2]\n      note: \"A6 反例讨论已添加。\"\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-P3 指出 formal statement→operationalization 缺中间推导。与 R12-N1 合并处理。\"\n\n- id: \"F2-W1\"\n  summary: \"α=0.60 sync dip：mechanism unexplained\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1]\n      note: \"R15 R1 在 REBUT R2-N1 时引用 non-monotonic detection dip（Figure 3, Table 6）作为超越 dose-response 的证据。α=0.60 anomaly 被视为正面发现而非问题。\"\n  action_items:\n    - round: 14\n      action: \"B1: cross-seed 一致性 (2/2 seeds 均 0/8) + 含/排拟合对比已写入 Appendix [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"F2-W6\"\n  summary: \"Detection boundary 验证不足\"\n  category: experiment\n  severity: major\n  status: open\n  first_raised_round: 2\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-N1 boundary fitting 欠定问题的直接后果。需要更多 α 水平数据点。\"\n\n- id: \"R10-MF5\"\n  summary: \"'Five families (345M-6.9B)' 数字自洽性\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 未显式提及。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 14\n      action: \"A1: Abstract 加 'at α=1.0' + '11/15 conditions' + '四个 non-confirming cases' [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R10-SF2\"\n  summary: \"Data accumulation vs replacement paradigm 未讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n\n- id: \"R10-SF3\"\n  summary: \"单一解码策略需定性讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 14\n\n- id: \"R10-SF5\"\n  summary: \"Bivariate confounding\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A5: Granger 局限扩展讨论（partial correlation 已在 §5）[已有]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R10-SF6\"\n  summary: \"每 cell 仅 8 pairs 的 binomial CI 极宽\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-SF7\"\n  summary: \"3-4 seeds replication power 有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-W1 Should-Fix。3 seeds 标准差估计服从 2 自由度 χ²，CI 极宽。Appendix L 跨 seed 分析也仅 3-4 seeds。R2 完全同意。\"\n\n- id: \"R11-VIS2\"\n  summary: \"Pages 5-6 连续纯文本无 display item\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 14\n\n- id: \"F8-W2\"\n  summary: \"Figure 子图内文字偏小\"\n  category: format\n  severity: minor\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: []\n      note: \"R15 视觉审查再次发现：Page 5 Figure 4 轴标签约正文字号 50-60%（低于 70% 阈值），Page 7 Figure 8 y 轴标签偏小。\"\n  action_items:\n    - round: 14\n      action: \"A8: Figures 2/4/6 labels 放大至 ≥8pt [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R9-m5\"\n  summary: \"Granger 'precedence' vs 'causality' 术语不一致\"\n  category: writing\n  severity: minor\n  status: in_progress\n  first_raised_round: 9\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A10: 全文统一为 Granger precedence [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"F2-W9b\"\n  summary: \"孤立 bib entries\"\n  category: writing\n  severity: minor\n  status: in_progress\n  first_raised_round: 2\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A9: 移除 14 个未引用条目 [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"F6-C2\"\n  summary: \"buffa2026entropy 引用标题不匹配\"\n  category: reference\n  severity: critical\n  status: open\n  first_raised_round: 6\n  last_seen_round: 8\n\n- id: \"R13-W1\"\n  summary: \"MMCT K≥3 共识框架 K 选择缺乏理论最优性证明\"\n  category: method\n  severity: major\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-W2/R2-W1 双方 AGREE。MMCT 是 FPR-inverse weighted majority voting（基本技术）。Shapley 分析显示 PermG 已最优。MMCT 增量价值有限。w_k=1/max(FPR_k,ε) ad-hoc 无理论保证。Table 2 K≥4/K≥5 全 0% 无额外信息。\"\n  action_items:\n    - round: 14\n      action: \"A7: Discussion 加 K calibration 讨论 [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R13-W2\"\n  summary: \"α=0.60 异常排除对幂律拟合的根本性影响\"\n  category: method\n  severity: major\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1]\n      note: \"R15 R1 在 REBUT R2-N1 时将 α=0.60 non-monotonic anomaly 视为超越 dose-response 的结构性发现。与 F2-W4b boundary fitting 问题关联。\"\n  action_items:\n    - round: 14\n      action: \"B1: cross-seed 一致性 + 含/排拟合对比 [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R13-W3\"\n  summary: \"跨架构验证仅在 α=1.0 最极端条件进行\"\n  category: experiment\n  severity: major\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 最高共识 Must-Fix。R1-N2/R2-N2 双方 AGREE。论文标题暗示普适性但实际是 Pythia-410M landscape。4/15 non-confirming 条件显示 architecture-dependent。\"\n  action_items:\n    - round: 14\n      action: \"C2: OPT-1.3B α=0.50 实验 [待GPU]\"\n      assigned_to: agent\n      status: open\n\n- id: \"R13-W4\"\n  summary: \"Abstract 'substantially reduces peak perplexity' 超出证据强度\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A3: 已确认 Abstract/Conclusion 无 'substantially' [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R13-W5\"\n  summary: \"偏相关分析（控制 generation number）缺失\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A5: §5 已有 partial correlation 35/36 讨论 [已有]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R13-REF1\"\n  summary: \"遗漏引用：Dakos et al. (2008, 2012) 早期预警信号核心实证方法论\"\n  category: reference\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A9: bib 清理中已移除未引用条目（含 dakos2008, dakos2012）\"\n      assigned_to: agent\n      status: done\n\n- id: \"R13-REF3\"\n  summary: \"Granger causality 标准局限性（observational equivalence, Lucas critique）未讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A5: Granger 局限扩展已在 §5 [已有]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R14-W1\"\n  summary: \"MMCT 权重估计噪声未讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R1-W2/R2-W1 的 MMCT 弱贡献共识间接涉及。\"\n\n- id: \"R14-W2\"\n  summary: \"Granger 检验在 T=10 短序列上 power 极低\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n\n- id: \"R14-M1\"\n  summary: \"bib 格式不一致\"\n  category: writing\n  severity: minor\n  status: in_progress\n  first_raised_round: 14\n  last_seen_round: 14\n  action_items:\n    - round: 14\n      action: \"A9: bib 清理和格式统一 [完成]\"\n      assigned_to: agent\n      status: done\n\n- id: \"R10-SF4\"\n  summary: \"方法敏感性 '3%-92%' framing\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R10-REF3\"\n  summary: \"遗漏引用：Runge et al. (2019) PCMCI\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 11\n\n- id: \"R9-REF1\"\n  summary: \"遗漏引用：Gerstgrasser et al. (2024) data accumulation\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 9\n  last_seen_round: 11\n\n- id: \"R10-m1\"\n  summary: \"Figure 3 y 轴标签含义不直观\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m2\"\n  summary: \"Table 2 'x/8' 列含义未定义\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-m3\"\n  summary: \"§5.1 前向引用缺上下文\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"R10-REF5\"\n  summary: \"遗漏引用：Montgomery SPC\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 10\n  last_seen_round: 10\n\n- id: \"F4-REF5\"\n  summary: \"bib first author mismatch: dey2024breaking\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 4\n  last_seen_round: 11\n\n- id: \"F8-N3\"\n  summary: \"Appendix 关键验证内容应纳入正文\"\n  category: writing\n  severity: minor\n  status: open\n  first_raised_round: 8\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R15 R2-W5 认为正文不 self-contained。R1 partial REBUT（8 页限制下合理）但同意需增加直觉解释。R1-W4/R2-W4 特别指出 Appendix J entropy artifact 应提升到 §5 Discussion。\"\n\n- id: \"F8-N4\"\n  summary: \"predict-then-verify post-hoc adjustment 嫌疑\"\n  category: method\n  severity: major\n  status: open\n  first_raised_round: 8\n  last_seen_round: 8\n\n- id: \"R12-REF1\"\n  summary: \"遗漏引用：Adams & MacKay (2007) Bayesian online changepoint detection\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-REF2\"\n  summary: \"遗漏引用：Papana et al. (2013) / Siggiridou & Kugiumtzis (2016)\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W2\"\n  summary: \"Eq.1 sigmoid 上界 0.70 选择理由未说明\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W3\"\n  summary: \"α 采样间隔不均匀（0.10→0.25 跳跃）理由未解释\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R12-W4\"\n  summary: \"Schaeffer et al. 8 种 collapse 定义中本文使用哪种未明确\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 12\n\n- id: \"R13-REF2\"\n  summary: \"遗漏引用：Lenton et al. (2008) 气候 tipping elements\"\n  category: reference\n  severity: minor\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n\n- id: \"R13-VIS1\"\n  summary: \"主文 8 页 0 个 table，所有定量结果表格在 appendix\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n\n- id: \"R13-VIS2\"\n  summary: \"前两页无任何 display item，Figure 1 直到第 3 页\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n\n# ============================================================\n# Round 15 新增 issues\n# ============================================================\n\n- id: \"R15-REF1\"\n  summary: \"遗漏引用：Silberzahn et al. (2018) Many Analysts, One Data Set\"\n  category: reference\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"论文 method sensitivity finding 直接回应 Silberzahn 的 multi-analyst/multi-method 框架。双方 AGREE 应在 §2 或 §3.3 引用。\"\n\n- id: \"R15-REF2\"\n  summary: \"遗漏引用：Kirchenbauer et al. (2023) watermarking as alternative paradigm\"\n  category: reference\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"Watermarking (proactive) vs distributional detection (reactive) 的方法论区分应在 Related Work 简要讨论。R2 AGREE。R1 未强调。\"\n\n- id: \"R15-W1\"\n  summary: \"Entropy artifact（测量分辨率差异）应从 Appendix J 提升到 §5 Discussion\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R1-W4/R2-W4 双方 AGREE。Appendix J 承认 entropy 是连续量、distinct-n 是离散计数——对 Design Principle 1 的根本性替代解释。R2 补充：需对 entropy 做 discretization 后重新测试 Granger precedence。此前 F2-W5 曾在 R9 标记 resolved，但 R15 从新角度（主文可见性 + discretization 验证）重新提出。\"\n\n- id: \"R15-W2\"\n  summary: \"排除 NaiveXCorr 后 κ 值应报告，以校准 method sensitivity claim\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [2]\n      note: \"R2 Q2：如果排除 NaiveXCorr（94.4% FPR 的失效方法），κ 可能显著提高，method sensitivity claim 需要重新校准。与 R11-W1 关联。\"\n\n- id: \"R15-W3\"\n  summary: \"Method sensitivity 定位应从 'primary finding' 降为 'methodological warning'\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 15\n  last_seen_round: 15\n  mentions:\n    - round: 15\n      reviewers: [1, 2]\n      note: \"R2-N3 认为统计学常识不构成 finding。R1 REBUT（14x FPR 差异是 domain-specific 实证发现）但同意 Contribution 1 定位偏高。共识：降为 methodological warning，Contribution 列表重新排序。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 1437 · 2026-05-25T07:37:10.270746+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml\", \"bytes\": 30121}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1438 · 2026-05-25T07:39:37.302849+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 15 审稿报告 — Distrib Canary Collapse\n\n## Summary\n\n本文研究 iterative model collapse 场景下多种统计检测方法的灵敏度差异，以合成数据替换比例 α 和训练代数 T 为二维参数，构建 \"detectability landscape\"。核心发现包括：(1) 不同检测方法的 FPR 跨越 14 倍（6.7%–94.4%），方法选择是检测结论变异的首要来源；(2) α≈0.45 附近存在 detection boundary 的 phase transition；(3) α=0.60 存在 non-monotonic detection anomaly。论文提出 MMCT（Multi-Method Consensus Testing）框架进行方法融合，并在 α=1.0 条件下进行了 5 个模型家族的跨架构验证。\n\n## Strengths\n\n**S1. 系统性的多方法比较框架。** 论文在同一数据集上对 5 种检测方法进行系统比较（Section 3.3, Figure 2），1,160 个 specification 的 robustness analysis 揭示了 κ=0.185 的低 inter-method agreement。这种\"同一数据、多种方法、量化一致性\"的实证设计在 model collapse 文献中尚属首次，为该领域的方法论规范化提供了参考。\n\n**S2. Non-monotonic detection anomaly 的识别与分析。** α=0.60 处的 detection dip（Figure 3, Table 6）超越了简单的 dose-response 单调关系，Section 4.2 和 Appendix K 对其成因（entropy-diversity temporal decoupling）的分析展示了超出参数扫描的结构性发现。\n\n**S3. 方法论警示的实用价值。** NaiveXCorr 的 FPR 高达 94.4%（检出 7-8/8 null pairs）源于 shared trend confounding（Section 3.3），这一 domain-specific 陷阱对从业者有直接的指导意义——大多数 practitioner 会首先尝试简单 cross-correlation，论文提供了明确的反面教材和替代方案（first-differencing, PermG）。\n\n**S4. 实验规模和透明度。** 涵盖 5 个模型家族（345M–6.9B），15 个 model-seed 组合，Appendix 提供了详尽的消融分析（Shapley contribution, weight robustness, power simulation, CUSUM comparison 等），AI 使用披露清晰（page 37，三种使用类别）。\n\n**S5. 写作质量和格式合规。** 论文格式符合 ACL 模板，booktabs 表格规范，LaTeX 无编译错误，Limitations section 覆盖 3 个要点（Scope, Statistical power, Causal interpretation），符合 EMNLP 2026 要求。\n\n## Weaknesses — Must-Fix\n\n**MF1. [共识] 跨架构泛化仅在 α=1.0，landscape 泛化性不足。**\nSection 4.5 (Table 1, page 6) 的跨架构验证仅在 α=1.0（全量合成替换）条件下进行，而论文最核心的发现——detection boundary 附近的 phase transition（α≈0.45）——没有任何跨架构验证。4/15 non-confirming 条件（Table 10, page 17）中 SmolLM3-3B 的 entropy decoupling 和 GPT-2 Medium 的 calibration dependency 暗示 landscape 是 architecture-dependent 的。论文标题 \"Characterizing the Detectability Landscape\" 暗示普适性，但实际上是 Pythia-410M 的 landscape。[R1-N2, R2-N2: 双方 AGREE]\n\n**MF2. [共识] Power-law boundary 拟合严重欠定。**\nSection 4.3 的 sigmoid regression 95% CI 为 [0.25, 0.82]，Limitations 自承 γ 的 CI 为 [0.01, 2.10]——跨越两个数量级。3 个自由参数拟合 3-4 个数据点是插值而非回归，对 power-law 的函数形式没有约束力。Appendix Y 的 power simulation 依赖同样的参数化形式，构成循环论证。需要至少 6-8 个 α 水平的数据点才有统计意义。[R1-N1, R2 AGREE]\n\n**MF3. [共识] PermG FPR 6.7% 置信区间过宽，削弱核心结论。**\n60 null pairs 下 4/60 = 6.7% 的 exact binomial 95% CI 约为 [1.8%, 16.2%]。CI 上界 16.2% 与 DiffXCorr 的 14.8% 实测 FPR 重叠，使 PermG 相对于 DiffXCorr 的 FPR 优势在统计上不显著。Conclusion 中 \"combining the lowest FPR 6.7%\" 给出了比数据实际支持的更精确的印象。应在正文中明确报告 CI。[R1-N3, R2 AGREE with nuance——R2 补充点估计 ranking 方向仍有信息价值，但不应作为精确数字使用]\n\n**MF4. [分歧] \"Detectability landscape\" 概念新颖性。**\nR2 认为 phase diagram 本质上是标准 dose-response 参数扫描加 sigmoid 拟合，\"landscape\" 是术语通胀。R1 部分反驳：multi-method comparison（1,160 specifications, κ=0.185）和 non-monotonic anomaly（α=0.60）超越了标准 dose-response，但同意 \"landscape\" 术语确实有 inflation，建议改为 \"multi-method detection sensitivity profile\"。\n→ 共识方向：landscape 的概念框架需要降低 claim 强度，但 multi-method comparison 和 non-monotonic finding 是有实质内容的。[R1 REBUT with concessions, R2-N1]\n\n**MF5. [分歧] Method sensitivity 作为 \"primary finding\" 的定位。**\nR2 认为\"不同统计检验具有不同 power 和 Type I error\"是统计学常识，不构成发现。R1 反驳：14 倍 FPR 差异（6.7%→94.4%）是 domain-specific 实证发现，且 NaiveXCorr 的 shared trend confounding 是 model collapse 时序数据的特有陷阱。但 R1 也同意将此定位为 \"primary finding\"（Contribution 1）确实偏高，建议降为 \"important methodological warning\"。\n→ 共识方向：FPR 差异幅度有信息价值，但 Contribution 列表应重新排序。[R1 REBUT with concessions, R2-N3]\n\n## Weaknesses — Should-Fix\n\n**SF1. [共识] 3 seeds 不足以估计 seed-level variance。**\nPhase diagram 用 3 seeds（Figure 3 caption），3 seeds 的标准差估计服从 2 自由度的 χ² 分布，CI 极宽。Appendix L 的跨 seed 分析也仅 3-4 seeds，无法从根本上改善估计精度。[R1-W1, R2 AGREE]\n\n**SF2. [共识] MMCT 方法论贡献薄弱，增量价值有限。**\nAlgorithm 1 (page 4) 的 FPR-inverse weighted majority voting 在 ensemble learning 文献中是基本技术。Appendix P Shapley 分析显示 PermG 的 combined Shapley 最接近零（FPR-FNR 最平衡），MMCT 的主要价值是排除高 FPR 方法而非组合互补方法。Table 2 已显示 PermG 单独是最优选择时，MMCT 增量价值有限。w_k = 1/max(FPR_k, ε) 是直觉合理但缺乏理论最优性保证的 ad-hoc 设计。[R1-W2, R2-W1: 双方 AGREE]\n\n**SF3. [共识] Intervention 仅在 α=1.0 验证但占据过多正文篇幅。**\nSection 4.6 (page 7) 的 intervention 仅在 α=1.0 验证，但占正文约 0.5 页。Appendix F (CUSUM comparison) 显示在高 α 下 CUSUM 与 canary 方法差异不大，削弱了 canary-based intervention 的独特价值主张。Discussion 的 \"deployment recommendations\" 超出了单一极端条件的证据支撑。建议正文压缩到 1-2 段，细节移入附录。[R1-W3, R2-W3: 双方 AGREE]\n\n**SF4. [共识] Entropy \"leading\" 可能是测量分辨率差异的 artifact。**\nAppendix J (page 17) 自己承认 entropy 是连续量而 distinct-n 是离散计数，entropy 可以响应任意小的分布变化。这是对 Design Principle 1（entropy precedes diversity）的根本性替代解释，但被放在 appendix 而非 Section 5 Discussion 中。需要：(a) 在 Discussion 中明确讨论此 concern，(b) 对 entropy 进行 discretization 后重新测试 Granger precedence 是否依然成立（论文未做此验证）。[R1-W4, R2-W4: 双方 AGREE]\n\n**SF5. [共识] 缺少 Silberzahn et al. (2018) \"Many Analysts, One Data Set\"。**\n论文的 core finding（method choice as primary variability source）直接回应了 Silberzahn 框架。Section 2 或 Section 3.3 应引用并讨论。[R2-W2, R1 AGREE]\n\n**SF6. [部分共识] 核心内容过度依赖附录。**\nR2 认为 Design Principle 推导、方法论比较表等放入附录导致正文不 self-contained。R1 反驳：8 页限制下这是合理选择，但同意正文应增加 1-2 句 intuitive justification（如 Section 3.1 的 Design Principle 缺少直觉解释）。[R1 partial REBUT, R2-W5]\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| 跨架构仅 α=1.0 | N2 | N2 | **AGREE** — 最高共识 Must-Fix |\n| Boundary fitting 欠定 | N1 | AGREE | **AGREE** — 3 参数拟合 3-4 点 = 插值 |\n| PermG FPR CI 过宽 | N3 | AGREE | **AGREE** — CI 上界与 DiffXCorr 重叠 |\n| 3 seeds 不足 | W1 | AGREE | **AGREE** |\n| MMCT 增量价值有限 | W2 | W1 | **AGREE** |\n| Intervention 过于初步 | W3 | W3 | **AGREE** |\n| Entropy artifact 应在主文讨论 | W4 | W4 | **AGREE** |\n| 缺失 Silberzahn (2018) | — | W2 | **AGREE** |\n| Table 2 K≥4/K≥5 列冗余 | P1 | AGREE | **AGREE** |\n| Figure 1 低值区颜色区分度差 | P2 | AGREE | **AGREE** |\n| Design Principle 正文缺中间推导 | P3 | AGREE | **AGREE** |\n| PermG direction checking 正文不足 | P4 | AGREE | **AGREE** |\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | 分歧性质 |\n|------|---------|---------|----------|\n| Landscape = dose-response? | REBUT — multi-method + non-monotonic 超越 dose-response，但同意术语 inflation | N1 — 本质是参数扫描 rebranding | 程度分歧：方向一致（需降低 claim），程度不同 |\n| Method sensitivity 新颖性 | REBUT — 14x FPR 差异是 domain-specific 发现 | N3 — 统计学常识 | 程度分歧：R1 认为有实证价值但 framing 偏高 |\n| 附录依赖 | partial REBUT — 页面约束下合理 | W5 — 正文不 self-contained | 程度分歧：R1 主张结构合理但需增加直觉解释 |\n| AI disclosure 详细度 | P5 — 不够详细 | REBUT — page 37 已充分 | 事实分歧：R2 指出 page 37 已列出三种使用类别 |\n\n## Questions\n\n**Q1.** 如果在 GPT-2 Medium 或 SmolLM3-3B 上做 α∈{0.25, 0.50, 0.75} 的完整扫描，phase boundary 位置是否与 Pythia-410M 的 α≈0.45 一致？如果不一致，论文的定量 claim 需要如何重写？\n\n**Q2.** 排除 NaiveXCorr 后，specification curve 的 κ 值是多少？如果显著提高，method sensitivity 的 claim 是否需要重新校准？\n\n**Q3.** 对 entropy 进行 discretization（如 binning 到与 distinct-n 相同的分辨率）后重新运行 Granger precedence test，Design Principle 1 是否仍然成立？\n\n**Q4.** 能否提供 MMCT 确实优于单独使用 PermG 的具体场景？如果没有这样的场景，MMCT 的方法论 claim 是否应该降级？\n\n## Missing References\n\n1. **Silberzahn et al. (2018)** \"Many Analysts, One Data Set: Making Transparent How Variations in Analytic Choices Affect Results\" — 多方法/多分析者范式的奠基性工作，论文的 method sensitivity finding 直接回应此框架。[R1 AGREE, R2 AGREE] **应引用。**\n\n2. **Kirchenbauer et al. (2023)** \"A Watermark for Large Language Models\" — watermarking 作为 proactive detection 的替代范式，与本文的 reactive distributional detection 形成方法论区分。Related Work 应简要讨论两者的差异。[R2 AGREE] **应引用。**\n\n3. DetectGPT (Mitchell et al., 2023) — R1 指出问题设定完全不同（per-text classification vs. distributional detection on time series），论文已在 Section 2.2 划清边界。**非必须。**\n\n4. MMD / Gretton et al. (2012) — R1 指出 MMD 在本文 time-series lead-lag 设定中的适用性不明确。**非必须。**\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求外部审稿。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成。0 critical / 7 warnings / 9 info。\n\n**Warnings:**\n1. **Page 2**: Figure 1 phase diagram 单元格数字标注字号偏小；红-橙-黄-绿渐变对红绿色盲不友好，建议 viridis/Okabe-Ito 色板\n2. **Page 5**: 单页 3 个 display items（Figure 3 + Figure 4 + Table 1），Figure 4 子面板轴标签约正文字号 50-60%，低于 70% 可读性阈值\n3. **Page 6**: 单页 3 个 figures（Figure 5-7），视觉压缩严重\n4. **Page 7**: Figure 8 条形图 y 轴模型名称字号偏小\n5. **Page 20**: Figure 14 占 75% 页面，底部 25% 空白\n6. **Page 24**: Figures 16-17 后底部 30% 空白\n7. **Page 37**: 最后一页仅 ~6 行文字，底部 85% 空白\n\n**Info highlights:**\n- 首页无视觉锚点（建议非必须）\n- 正文 12 个 display items 略高于 8 页典型 5-8 个；Figure 3 与 Figure 7 信息重叠可考虑合并\n- Limitations 覆盖 3 点，篇幅适中，符合 EMNLP 2026\n- 表格 booktabs 规范，公式正确，无 margin 溢出，References 统一\n\n## Overall Assessment\n\n**评分：3.0 (Findings)**\n\n**置信度：High**\n\nR1 给出 3.5（Borderline Conference），R2 给出 3.0（Findings）。差异来自对 \"detectability landscape\" 概念新颖性的评估——R2 认为即使修复拟合和泛化问题，landscape 的概念新颖性仍有限（本质是 dose-response rebranding），R1 认为 multi-method comparison 增加了超越 dose-response 的价值。\n\n综合评估采用 3.0，理由：\n\n1. **泛化性缺陷是根本性的。** 跨架构验证仅在 α=1.0（双方最高共识 Must-Fix），标题承诺的 \"landscape characterization\" 实际仅基于 Pythia-410M。需要额外实验而非仅修改写作。\n\n2. **统计精度不足以支撑定量 claim。** Boundary fitting 欠定（3 参数 / 3-4 点）、PermG FPR CI 过宽（[1.8%, 16.2%]）、3 seeds 的 variance 估计——共同使得定量结论（\"α_c ≈ 0.45\"、\"FPR = 6.7%\"）的 precision 远低于呈现方式所暗示的。\n\n3. **MMCT 方法论贡献薄弱。** 在 PermG 已是最优单方法的情况下，MMCT 的增量价值缺乏证据支持，且缺乏理论最优性保证。\n\n4. **实证发现有真正价值。** 14 倍 FPR 差异的定量化、NaiveXCorr 的 shared trend confounding 警示、α=0.60 non-monotonic anomaly——这些是 genuine contributions，适合 Findings 收录。\n\n**ARR 评分对照：Overall Assessment = 3 (Findings)** — 可被 Findings 接收，但需显著修改 framing 和补充跨架构实验后才能考虑主会议。\n\n## Detailed Comments\n\n### Section 1 — Introduction\n- \"Characterizing the Detectability Landscape\" 标题暗示普适性，与实际仅基于 Pythia-410M 的证据不匹配\n- Contribution 列表应重新排序：method sensitivity 从 Contribution 1 降为 methodological warning，landscape characterization 需加 scope qualifier\n\n### Section 2 — Related Work\n- 缺少 Silberzahn et al. (2018) 和 Kirchenbauer et al. (2023) 的讨论\n- 与 Schaeffer et al. (2025) \"8 种 collapse 定义\" 的映射应更明确\n\n### Section 3 — Method\n- Design Principle 1 和 2 的 formal statement 使用信息论语言但 operationalization 跳转到具体 metrics 时缺少中间推导（仅引用 Appendix，主文无直觉解释）\n- MMCT Algorithm 1 的 FPR-inverse weighting 缺乏理论依据，Appendix Q \"对 ad-hoc 选择不敏感\" ≠ \"有理论依据\"\n- PermG direction checking 描述不足（Appendix G 有详细描述，但 Section 3.3 缺关键细节）\n\n### Section 4 — Experiments\n- Phase diagram boundary fitting：需要更多数据点（建议 ≥6 个 α 水平），当前 CI 过宽\n- Cross-architecture：Table 1 仅 α=1.0，需要至少 α∈{0.50, 0.75} 的验证\n- Intervention：正文篇幅应压缩，证据仅支持 proof-of-concept 定位\n- Table 2 的 K≥4 和 K≥5 列全为 0%，可删除或合并为脚注\n- α=0.60 non-monotonic anomaly 是有价值的发现，建议给予更多正文空间\n\n### Section 5 — Discussion\n- Entropy artifact（测量分辨率 vs. 因果 precedence）应从 Appendix J 提升到 Discussion\n- Design Principle 1 的因果叙事需要弱化，或提供 discretized entropy 的验证\n\n### Section 6 — Conclusion\n- \"combining the lowest FPR 6.7%\" 应改为包含 CI 的表述\n- Cross-architecture generalization claim 需加 \"at α=1.0\" qualifier\n\n### Limitations\n- 当前 3 个点的覆盖适当，建议增加对 MMCT 增量价值有限的 honest assessment\n\n### Appendix\n- 内容全面，但部分关键验证（entropy artifact, PermG FPR CI）应在正文中有显式引用和简要讨论\n- Figure 子图内文字偏小问题（Page 5 Figure 4, Page 7 Figure 8）仍存在",
  "project": "distrib_canary_collapse",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 15 审稿报告 — Distrib Canary Collapse\n\n## Summary\n\n本文研究 iterative model collapse 场景下多种统计检测方法的灵敏度差异，以合成数据替换比例 α 和训练代数 T 为二维参数，构建 \"detectability landscape\"。核心发现包括：(1) 不同检测方法的 FPR 跨越 14 倍（6.7%–94.4%），方法选择是检测结论变异的首要来源；(2) α≈0.45 附近存在 detection boundary 的 phase transition；(3) α=0.60 存在 non-monotonic detection anomaly。论文提出 MMCT（Multi-Method Consensus Testing）框架进行方法融合，并在 α=1.0 条件下进行了 5 个模型家族的跨架构验证。\n\n## Strengths\n\n**S1. 系统性的多方法比较框架。** 论文在同一数据集上对 5 种检测方法进行系统比较（Section 3.3, Figure 2），1,160 个 specification 的 robustness analysis 揭示了 κ=0.185 的低 inter-method agreement。这种\"同一数据、多种方法、量化一致性\"的实证设计在 model collapse 文献中尚属首次，为该领域的方法论规范化提供了参考。\n\n**S2. Non-monotonic detection anomaly 的识别与分析。** α=0.60 处的 detection dip（Figure 3, Table 6）超越了简单的 dose-response 单调关系，Section 4.2 和 Appendix K 对其成因（entropy-diversity temporal decoupling）的分析展示了超出参数扫描的结构性发现。\n\n**S3. 方法论警示的实用价值。** NaiveXCorr 的 FPR 高达 94.4%（检出 7-8/8 null pairs）源于 shared trend confounding（Section 3.3），这一 domain-specific 陷阱对从业者有直接的指导意义——大多数 practitioner 会首先尝试简单 cross-correlation，论文提供了明确的反面教材和替代方案（first-differencing, PermG）。\n\n**S4. 实验规模和透明度。** 涵盖 5 个模型家族（345M–6.9B），15 个 model-seed 组合，Appendix 提供了详尽的消融分析（Shapley contribution, weight robustness, power simulation, CUSUM comparison 等），AI 使用披露清晰（page 37，三种使用类别）。\n\n**S5. 写作质量和格式合规。** 论文格式符合 ACL 模板，booktabs 表格规范，LaTeX 无编译错误，Limitations section 覆盖 3 个要点（Scope, Statistical power, Causal interpretation），符合 EMNLP 2026 要求。\n\n## Weaknesses — Must-Fix\n\n**MF1. [共识] 跨架构泛化仅在 α=1.0，landscape 泛化性不足。**\nSection 4.5 (Table 1, page 6) 的跨架构验证仅在 α=1.0（全量合成替换）条件下进行，而论文最核心的发现——detection boundary 附近的 phase transition（α≈0.45）——没有任何跨架构验证。4/15 non-confirming 条件（Table 10, page 17）中 SmolLM3-3B 的 entropy decoupling 和 GPT-2 Medium 的 calibration dependency 暗示 landscape 是 architecture-dependent 的。论文标题 \"Characterizing the Detectability Landscape\" 暗示普适性，但实际上是 Pythia-410M 的 landscape。[R1-N2, R2-N2: 双方 AGREE]\n\n**MF2. [共识] Power-law boundary 拟合严重欠定。**\nSection 4.3 的 sigmoid regression 95% CI 为 [0.25, 0.82]，Limitations 自承 γ 的 CI 为 [0.01, 2.10]——跨越两个数量级。3 个自由参数拟合 3-4 个数据点是插值而非回归，对 power-law 的函数形式没有约束力。Appendix Y 的 power simulation 依赖同样的参数化形式，构成循环论证。需要至少 6-8 个 α 水平的数据点才有统计意义。[R1-N1, R2 AGREE]\n\n**MF3. [共识] PermG FPR 6.7% 置信区间过宽，削弱核心结论。**\n60 null pairs 下 4/60 = 6.7% 的 exact binomial 95% CI 约为 [1.8%, 16.2%]。CI 上界 16.2% 与 DiffXCorr 的 14.8% 实测 FPR 重叠，使 PermG 相对于 DiffXCorr 的 FPR 优势在统计上不显著。Conclusion 中 \"combining the lowest FPR 6.7%\" 给出了比数据实际支持的更精确的印象。应在正文中明确报告 CI。[R1-N3, R2 AGREE with nuance——R2 补充点估计 ranking 方向仍有信息价值，但不应作为精确数字使用]\n\n**MF4. [分歧] \"Detectability landscape\" 概念新颖性。**\nR2 认为 phase diagram 本质上是标准 dose-response 参数扫描加 sigmoid 拟合，\"landscape\" 是术语通胀。R1 部分反驳：multi-method comparison（1,160 specifications, κ=0.185）和 non-monotonic anomaly（α=0.60）超越了标准 dose-response，但同意 \"landscape\" 术语确实有 inflation，建议改为 \"multi-method detection sensitivity profile\"。\n→ 共识方向：landscape 的概念框架需要降低 claim 强度，但 multi-method comparison 和 non-monotonic finding 是有实质内容的。[R1 REBUT with concessions, R2-N1]\n\n**MF5. [分歧] Method sensitivity 作为 \"primary finding\" 的定位。**\nR2 认为\"不同统计检验具有不同 power 和 Type I error\"是统计学常识，不构成发现。R1 反驳：14 倍 FPR 差异（6.7%→94.4%）是 domain-specific 实证发现，且 NaiveXCorr 的 shared trend confounding 是 model collapse 时序数据的特有陷阱。但 R1 也同意将此定位为 \"primary finding\"（Contribution 1）确实偏高，建议降为 \"important methodological warning\"。\n→ 共识方向：FPR 差异幅度有信息价值，但 Contribution 列表应重新排序。[R1 REBUT with concessions, R2-N3]\n\n## Weaknesses — Should-Fix\n\n**SF1. [共识] 3 seeds 不足以估计 seed-level variance。**\nPhase diagram 用 3 seeds（Figure 3 caption），3 seeds 的标准差估计服从 2 自由度的 χ² 分布，CI 极宽。Appendix L 的跨 seed 分析也仅 3-4 seeds，无法从根本上改善估计精度。[R1-W1, R2 AGREE]\n\n**SF2. [共识] MMCT 方法论贡献薄弱，增量价值有限。**\nAlgorithm 1 (page 4) 的 FPR-inverse weighted majority voting 在 ensemble learning 文献中是基本技术。Appendix P Shapley 分析显示 PermG 的 combined Shapley 最接近零（FPR-FNR 最平衡），MMCT 的主要价值是排除高 FPR 方法而非组合互补方法。Table 2 已显示 PermG 单独是最优选择时，MMCT 增量价值有限。w_k = 1/max(FPR_k, ε) 是直觉合理但缺乏理论最优性保证的 ad-hoc 设计。[R1-W2, R2-W1: 双方 AGREE]\n\n**SF3. [共识] Intervention 仅在 α=1.0 验证但占据过多正文篇幅。**\nSection 4.6 (page 7) 的 intervention 仅在 α=1.0 验证，但占正文约 0.5 页。Appendix F (CUSUM comparison) 显示在高 α 下 CUSUM 与 canary 方法差异不大，削弱了 canary-based intervention 的独特价值主张。Discussion 的 \"deployment recommendations\" 超出了单一极端条件的证据支撑。建议正文压缩到 1-2 段，细节移入附录。[R1-W3, R2-W3: 双方 AGREE]\n\n**SF4. [共识] Entropy \"leading\" 可能是测量分辨率差异的 artifact。**\nAppendix J (page 17) 自己承认 entropy 是连续量而 distinct-n 是离散计数，entropy 可以响应任意小的分布变化。这是对 Design Principle 1（entropy precedes diversity）的根本性替代解释，但被放在 appendix 而非 Section 5 Discussion 中。需要：(a) 在 Discussion 中明确讨论此 concern，(b) 对 entropy 进行 discretization 后重新测试 Granger precedence 是否依然成立（论文未做此验证）。[R1-W4, R2-W4: 双方 AGREE]\n\n**SF5. [共识] 缺少 Silberzahn et al. (2018) \"Many Analysts, One Data Set\"。**\n论文的 core finding（method choice as primary variability source）直接回应了 Silberzahn 框架。Section 2 或 Section 3.3 应引用并讨论。[R2-W2, R1 AGREE]\n\n**SF6. [部分共识] 核心内容过度依赖附录。**\nR2 认为 Design Principle 推导、方法论比较表等放入附录导致正文不 self-contained。R1 反驳：8 页限制下这是合理选择，但同意正文应增加 1-2 句 intuitive justification（如 Section 3.1 的 Design Principle 缺少直觉解释）。[R1 partial REBUT, R2-W5]\n\n## Reviewer Consensus\n\n| 问题 | R1 | R2 | 共识 |\n|------|----|----|------|\n| 跨架构仅 α=1.0 | N2 | N2 | **AGREE** — 最高共识 Must-Fix |\n| Boundary fitting 欠定 | N1 | AGREE | **AGREE** — 3 参数拟合 3-4 点 = 插值 |\n| PermG FPR CI 过宽 | N3 | AGREE | **AGREE** — CI 上界与 DiffXCorr 重叠 |\n| 3 seeds 不足 | W1 | AGREE | **AGREE** |\n| MMCT 增量价值有限 | W2 | W1 | **AGREE** |\n| Intervention 过于初步 | W3 | W3 | **AGREE** |\n| Entropy artifact 应在主文讨论 | W4 | W4 | **AGREE** |\n| 缺失 Silberzahn (2018) | — | W2 | **AGREE** |\n| Table 2 K≥4/K≥5 列冗余 | P1 | AGREE | **AGREE** |\n| Figure 1 低值区颜色区分度差 | P2 | AGREE | **AGREE** |\n| Design Principle 正文缺中间推导 | P3 | AGREE | **AGREE** |\n| PermG direction checking 正文不足 | P4 | AGREE | **AGREE** |\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | 分歧性质 |\n|------|---------|---------|----------|\n| Landscape = dose-response? | REBUT — multi-method + non-monotonic 超越 dose-response，但同意术语 inflation | N1 — 本质是参数扫描 rebranding | 程度分歧：方向一致（需降低 claim），程度不同 |\n| Method sensitivity 新颖性 | REBUT — 14x FPR 差异是 domain-specific 发现 | N3 — 统计学常识 | 程度分歧：R1 认为有实证价值但 framing 偏高 |\n| 附录依赖 | partial REBUT — 页面约束下合理 | W5 — 正文不 self-contained | 程度分歧：R1 主张结构合理但需增加直觉解释 |\n| AI disclosure 详细度 | P5 — 不够详细 | REBUT — page 37 已充分 | 事实分歧：R2 指出 page 37 已列出三种使用类别 |\n\n## Questions\n\n**Q1.** 如果在 GPT-2 Medium 或 SmolLM3-3B 上做 α∈{0.25, 0.50, 0.75} 的完整扫描，phase boundary 位置是否与 Pythia-410M 的 α≈0.45 一致？如果不一致，论文的定量 claim 需要如何重写？\n\n**Q2.** 排除 NaiveXCorr 后，specification curve 的 κ 值是多少？如果显著提高，method sensitivity 的 claim 是否需要重新校准？\n\n**Q3.** 对 entropy 进行 discretization（如 binning 到与 distinct-n 相同的分辨率）后重新运行 Granger precedence test，Design Principle 1 是否仍然成立？\n\n**Q4.** 能否提供 MMCT 确实优于单独使用 PermG 的具体场景？如果没有这样的场景，MMCT 的方法论 claim 是否应该降级？\n\n## Missing References\n\n1. **Silberzahn et al. (2018)** \"Many Analysts, One Data Set: Making Transparent How Variations in Analytic Choices Affect Results\" — 多方法/多分析者范式的奠基性工作，论文的 method sensitivity finding 直接回应此框架。[R1 AGREE, R2 AGREE] **应引用。**\n\n2. **Kirchenbauer et al. (2023)** \"A Watermark for Large Language Models\" — watermarking 作为 proactive detection 的替代范式，与本文的 reactive distributional detection 形成方法论区分。Related Work 应简要讨论两者的差异。[R2 AGREE] **应引用。**\n\n3. DetectGPT (Mitchell et al., 2023) — R1 指出问题设定完全不同（per-text classification vs. distributional detection on time series），论文已在 Section 2.2 划清边界。**非必须。**\n\n4. MMD / Gretton et al. (2012) — R1 指出 MMD 在本文 time-series lead-lag 设定中的适用性不明确。**非必须。**\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求外部审稿。\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成。0 critical / 7 warnings / 9 info。\n\n**Warnings:**\n1. **Page 2**: Figure 1 phase diagram 单元格数字标注字号偏小；红-橙-黄-绿渐变对红绿色盲不友好，建议 viridis/Okabe-Ito 色板\n2. **Page 5**: 单页 3 个 display items（Figure 3 + Figure 4 + Table 1），Figure 4 子面板轴标签约正文字号 50-60%，低于 70% 可读性阈值\n3. **Page 6**: 单页 3 个 figures（Figure 5-7），视觉压缩严重\n4. **Page 7**: Figure 8 条形图 y 轴模型名称字号偏小\n5. **Page 20**: Figure 14 占 75% 页面，底部 25% 空白\n6. **Page 24**: Figures 16-17 后底部 30% 空白\n7. **Page 37**: 最后一页仅 ~6 行文字，底部 85% 空白\n\n**Info highlights:**\n- 首页无视觉锚点（建议非必须）\n- 正文 12 个 display items 略高于 8 页典型 5-8 个；Figure 3 与 Figure 7 信息重叠可考虑合并\n- Limitations 覆盖 3 点，篇幅适中，符合 EMNLP 2026\n- 表格 booktabs 规范，公式正确，无 margin 溢出，References 统一\n\n## Overall Assessment\n\n**评分：3.0 (Findings)**\n\n**置信度：High**\n\nR1 给出 3.5（Borderline Conference），R2 给出 3.0（Findings）。差异来自对 \"detectability landscape\" 概念新颖性的评估——R2 认为即使修复拟合和泛化问题，landscape 的概念新颖性仍有限（本质是 dose-response rebranding），R1 认为 multi-method comparison 增加了超越 dose-response 的价值。\n\n综合评估采用 3.0，理由：\n\n1. **泛化性缺陷是根本性的。** 跨架构验证仅在 α=1.0（双方最高共识 Must-Fix），标题承诺的 \"landscape characterization\" 实际仅基于 Pythia-410M。需要额外实验而非仅修改写作。\n\n2. **统计精度不足以支撑定量 claim。** Boundary fitting 欠定（3 参数 / 3-4 点）、PermG FPR CI 过宽（[1.8%, 16.2%]）、3 seeds 的 variance 估计——共同使得定量结论（\"α_c ≈ 0.45\"、\"FPR = 6.7%\"）的 precision 远低于呈现方式所暗示的。\n\n3. **MMCT 方法论贡献薄弱。** 在 PermG 已是最优单方法的情况下，MMCT 的增量价值缺乏证据支持，且缺乏理论最优性保证。\n\n4. **实证发现有真正价值。** 14 倍 FPR 差异的定量化、NaiveXCorr 的 shared trend confounding 警示、α=0.60 non-monotonic anomaly——这些是 genuine contributions，适合 Findings 收录。\n\n**ARR 评分对照：Overall Assessment = 3 (Findings)** — 可被 Findings 接收，但需显著修改 framing 和补充跨架构实验后才能考虑主会议。\n\n## Detailed Comments\n\n### Section 1 — Introduction\n- \"Characterizing the Detectability Landscape\" 标题暗示普适性，与实际仅基于 Pythia-410M 的证据不匹配\n- Contribution 列表应重新排序：method sensitivity 从 Contribution 1 降为 methodological warning，landscape characterization 需加 scope qualifier\n\n### Section 2 — Related Work\n- 缺少 Silberzahn et al. (2018) 和 Kirchenbauer et al. (2023) 的讨论\n- 与 Schaeffer et al. (2025) \"8 种 collapse 定义\" 的映射应更明确\n\n### Section 3 — Method\n- Design Principle 1 和 2 的 formal statement 使用信息论语言但 operationalization 跳转到具体 metrics 时缺少中间推导（仅引用 Appendix，主文无直觉解释）\n- MMCT Algorithm 1 的 FPR-inverse weighting 缺乏理论依据，Appendix Q \"对 ad-hoc 选择不敏感\" ≠ \"有理论依据\"\n- PermG direction checking 描述不足（Appendix G 有详细描述，但 Section 3.3 缺关键细节）\n\n### Section 4 — Experiments\n- Phase diagram boundary fitting：需要更多数据点（建议 ≥6 个 α 水平），当前 CI 过宽\n- Cross-architecture：Table 1 仅 α=1.0，需要至少 α∈{0.50, 0.75} 的验证\n- Intervention：正文篇幅应压缩，证据仅支持 proof-of-concept 定位\n- Table 2 的 K≥4 和 K≥5 列全为 0%，可删除或合并为脚注\n- α=0.60 non-monotonic anomaly 是有价值的发现，建议给予更多正文空间\n\n### Section 5 — Discussion\n- Entropy artifact（测量分辨率 vs. 因果 precedence）应从 Appendix J 提升到 Discussion\n- Design Principle 1 的因果叙事需要弱化，或提供 discretized entropy 的验证\n\n### Section 6 — Conclusion\n- \"combining the lowest FPR 6.7%\" 应改为包含 CI 的表述\n- Cross-architecture generalization claim 需加 \"at α=1.0\" qualifier\n\n### Limitations\n- 当前 3 个点的覆盖适当，建议增加对 MMCT 增量价值有限的 honest assessment\n\n### Appendix\n- 内容全面，但部分关键验证（entropy artifact, PermG FPR CI）应在正文中有显式引用和简要讨论\n- Figure 子图内文字偏小问题（Page 5 Figure 4, Page 7 Figure 8）仍存在",
    "project": "distrib_canary_collapse",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
  }
}
```

</details>

---


### Tool result

_source line 1439 · 2026-05-25T07:39:42.189856+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_150c7ce908e05d7932315e0288cf5bfb:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4887
}
```

</details>

---


### Assistant

_source line 1440 · 2026-05-25T07:39:52.016383+00:00_

Round 15 审稿完成。

**报告已投递至 Research Director。** 核心结论：

- **评分：3.0 (Findings)**，R1 给 3.5 / R2 给 3.0，综合取 3.0
- **5 个 Must-Fix**（前 3 个双方共识，后 2 个有程度分歧但方向一致）：跨架构泛化仅 α=1.0、boundary fitting 欠定、PermG FPR CI 过宽、landscape 术语通胀、method sensitivity 定位偏高
- **6 个 Should-Fix**：3 seeds 不足、MMCT 贡献薄弱、intervention 初步、entropy artifact 应入主文、缺 Silberzahn 引用、附录依赖
- **Issue Tracker 已同步**：更新 18 个活跃 issue 的 R15 mentions，新增 3 个 issue（R15-REF1/REF2/W1/W2/W3）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 137

## Round 137

74 recorded events


### User

_source line 1441 · 2026-05-25T08:16:26.340939+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: distrib_canary_collapse
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 截止日期: 2026-06-15
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1442 · 2026-05-25T08:16:34.937991+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1443 · 2026-05-25T08:16:35.039908+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1444 · 2026-05-25T08:16:43.184617+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1445 · 2026-05-25T08:16:43.235309+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1446 · 2026-05-25T08:16:52.691455+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1447 · 2026-05-25T08:16:52.691957+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1448 · 2026-05-25T08:16:58.797483+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool call

_source line 1449 · 2026-05-25T08:17:00.305989+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex",
    "limit": "80"
  }
}
```

</details>

---


### Tool result

_source line 1450 · 2026-05-25T08:17:00.740291+00:00_

{"result":"# 项目 distrib_canary_collapse 概况\n\n## 实验状态 (218 个)\n\n- **gen_wiki_gpt2m_a100_s42_v3**: DONE (success) — \n- **mvp_v4_rep44**: DONE (success) — \n- **plan_006_s42**: DONE (failed) — \n- **plan_006_s42_resume**: DONE (killed) — \n- **gen_wiki_gpt2m_a100_s42_v2**: DONE (killed) — \n- **method_ablation_phase2**: DONE (success) — \n- **alpha_sweep_a025_s42_v3**: DONE (success) — \n- **method_ablation_phase1**: DONE (success) — \n- **plan_009_bootstrap_ty**: DONE (success) — \n- **mvp_v3_rep43**: DONE (failed) — \n- **mvp_v3_rep42**: DONE (failed) — \n- **mvp_v2_rep43**: DONE (killed) — \n- **mvp_v2_rep42**: DONE (killed) — \n- **mvp_rep43**: DONE (killed) — \n- **mvp_rep42**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-25\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| c2_opt13b_a050_s42_fp32 | OPT-1.3B at α=0.50 should show PermG forward detection onset similar to Pythia-410M (6/8 at α=0.50), validating that the phase diagram structure generalizes beyond the Pythia family to the transition region | — | — | — |\n\n## 待处理\n- c2_opt13b_a050_s43_fp32_v2（准备中，spec 已填充，cuda:0 only）\n- C1: c1_interv_gpt2m_pred_s42 / c1_interv_gpt2m_react_s42 / c1_interv_opt13b_pred_s42 / c1_interv_opt13b_react_s42（命令就绪，待 C2 完成后注册）\n\n## 近期结论\n- **c2_opt13b_a050_s43_fp32** (failed): OPT-1.3B at α=0.50 seed 43 replication: cross-seed consistency of PermG forward detection in the transition region on a non-Pythia architecture\n- **null_fpr_s51_fp32** (success): Null experiment (α=0.00) for FPR estimation: no synthetic data contamination, all detection methods should show p>0.05, contributing to narrower FPR CI with 15 seeds\n- **null_t15_s42_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n\n## 趋势\n成功 154 / 负向 4 / 失败 23 / 共 211\n累计 GPU: 8.4h\n\n## 下一步\n（无活跃 idea，请通过 ideas
…[truncated 1793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1942
}
```

</details>

---


### Tool result

_source line 1451 · 2026-05-25T08:17:00.740767+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{graphicx}
13	\usepackage{booktabs}
14	\usepackage{subcaption}
15	\usepackage{dblfloatfix}
16	\usepackage{placeins}
17	\usepackage{algorithm}
18	\usepackage{algpseudocode}
19	\usepackage{amsthm}
20	\newtheorem{theorem}{Theorem}
21	\newtheorem{proposition}[theorem]{Proposition}
22	\newtheorem{designprinciple}[theorem]{Design Principle}
23	\theoremstyle{definition}
24	\newtheorem{assumption}[theorem]{Assumption}
25	
26	\title{Characterizing the Detectability Landscape of Iterative Model Collapse}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	\input{introduction}
35	\input{related_work}
36	\input{method}
37	\input{experiments}
38	\input{discussion}
39	\input{conclusion}
40	\input{limitations}
41	\bibliography{references}
42	
43	\input{appendix}
44	
45	\end{document}
46	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 434
}
```

</details>

---


### Tool call

_source line 1452 · 2026-05-25T08:17:00.741033+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1453 · 2026-05-25T08:17:00.741245+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1454 · 2026-05-25T08:17:02.000025+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"NO_PDF\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1455 · 2026-05-25T08:17:02.355962+00:00_

-rw-r--r-- 1 ubuntu ubuntu 1255680 May 25 08:14 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 355
}
```

</details>

---


### Tool call

_source line 1456 · 2026-05-25T08:17:10.551129+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR",
  "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR",
    "allowed_domains": "['aclweb.org', '2026.emnlp.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 1457 · 2026-05-25T08:17:10.853899+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1458 · 2026-05-25T08:17:11.361602+00:00_

1	\begin{abstract}
2	When language models train iteratively on their own output, the resulting distributional collapse is difficult to detect: the time series are short, the signal grows sub-linearly with contamination, and---as we demonstrate---the choice of statistical method alone can shift conclusions from universal detection to complete null.
3	We identify a sharp detection phase transition in iterative model collapse: Granger-based testing finds zero significant canary$\to$downstream pairs through 45\% synthetic contamination, then jumps to reliable detection within a two-percentage-point interval at $\alpha_c \approx 0.50$, defining three confirmed regimes (blind, onset, detection).
4	This transition emerges from a five-method comparison where null-control false-positive rates span 7\% to 94\%; permutation Granger causality, the lowest-FPR method (6.7\%, CI $[1.8\%, 16.2\%]$), serves as the primary detector.
5	Cross-architecture evaluation at full synthetic replacement ($\alpha{=}1.0$) across five model families (345M--6.9B) supports forward detection in 11/15 conditions.
6	Token entropy temporally precedes diversity collapse by at least one generation, enabling a proof-of-concept intervention that reduces peak perplexity by 64\%.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 1459 · 2026-05-25T08:17:11.463126+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "distrib_canary_collapse",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1460 · 2026-05-25T08:17:20.439923+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026 related to ARR:

## Main Conference Paper Submissions

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. Papers may contribute negative findings, survey an area, announce the creation of a new resource, argue a position, report novel linguistic insights derived using existing computational techniques, and reproduce (or fail to reproduce) previous results.

## ARR 2026 May Submission Policy

Given that the ARR 2026 May cycle is aligned with two conferences (EMNLP and AACL), authors must explicitly declare which conference they intend to commit to at submission time. This choice wil
…[truncated 715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 9888
}
```

</details>

---


### Tool result

_source line 1461 · 2026-05-25T08:17:20.490634+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'distrib_canary_collapse'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 9027
}
```

</details>

---


### Tool call

_source line 1462 · 2026-05-25T08:17:25.621099+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline page limit format requirements long paper short paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline page limit format requirements long paper short paper"
  }
}
```

</details>

---


### Tool call

_source line 1463 · 2026-05-25T08:17:25.973098+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1464 · 2026-05-25T08:17:26.073906+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1465 · 2026-05-25T08:17:30.864773+00:00_

Web search results for query: "EMNLP 2026 submission deadline page limit format requirements long paper short paper"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"}]

Based on the search results, here is the information about EMNLP 2026 submission requirements:

## Submission Deadline
The ARR submission deadline for both long and short papers is May 25, 2026.

## Page Limits
The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Additionally, final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## Format Requirements
EMNLP uses the standard ACL st
…[truncated 558 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebSearch",
  "elapsed_ms": 5243
}
```

</details>

---


### Tool call

_source line 1466 · 2026-05-25T08:17:37.758660+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract all submission requirements: page limits (long/short), format/template, anonymity rules, appendix rules, citation format, deadline dates, and any special rules. Be thorough and exact."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract all submission requirements: page limits (long/short), format/template, anonymity rules, appendix rules, citation format, deadline dates, and any special rules. Be thorough and exact."
  }
}
```

</details>

---


### Tool call

_source line 1467 · 2026-05-25T08:17:38.010232+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1468 · 2026-05-25T08:17:43.838454+00:00_

# EMNLP 2026 Submission Requirements

## Page Limits
- **Long Papers:** 8 pages
- **Short Papers:** 4 pages
- **Final versions:** +1 additional page (9 pages for long, 5 pages for short)

## Format & Templates
Submissions must follow "all of the ARR submission requirements," including specific templates available through the ARR platform. Exact formatting specifications are referenced in the linked ARR guidelines.

## Anonymity Rules
The reviewing process maintains double-blind review standards. "Reviewers will not see authors, nor will authors see reviewers and reviews on ARR will not be made publicly visible." Authors may choose to make anonymized submitted articles publicly visible through ARR. "There is no anonymity period requirement" per ACL and ARR policies.

## Appendices & Supplementary Materials
"Optional Supplementary Materials (Appendices, Software and Data)" are permitted per ARR guidelines, though specific limits aren't detailed in this document.

## Citation Format
The document references adherence to ARR's "Citation and Comparison" policy but doesn't specify a particular citation style.

## Deadline Dates
- ARR submission: May 25, 2026
- Reviewer registration: May 27, 2026
- Author response period: July 7-13, 2026
- Meta-review release: July 30, 2026
- EMNLP commitment: August 2, 2026
- Acceptance notification: August 20, 2026
- Camera-ready due: September 20, 2026

All deadlines are "11:59PM UTC-12:00 ('anywhere on Earth')."

## Special Rules
- No dual submissions allowed
- Author lists cannot be modified during commitment (order changes permitted)
- Authors must register for mandatory reviewing duties
- Papers must include a limitations section
- AI writing assistance is permitted; entirely AI-generated papers are not

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "WebFetch",
  "elapsed_ms": 6079
}
```

</details>

---


### Tool result

_source line 1469 · 2026-05-25T08:17:44.692721+00:00_

{"result":"# 项目 distrib_canary_collapse 概况\n\n## 实验状态 (218 个)\n\n- **gen_wiki_gpt2m_a100_s42_v3**: DONE (success) — \n- **mvp_v4_rep44**: DONE (success) — \n- **plan_006_s42**: DONE (failed) — \n- **plan_006_s42_resume**: DONE (killed) — \n- **gen_wiki_gpt2m_a100_s42_v2**: DONE (killed) — \n- **method_ablation_phase2**: DONE (success) — \n- **alpha_sweep_a025_s42_v3**: DONE (success) — \n- **method_ablation_phase1**: DONE (success) — \n- **plan_009_bootstrap_ty**: DONE (success) — \n- **mvp_v3_rep43**: DONE (failed) — \n- **mvp_v3_rep42**: DONE (failed) — \n- **mvp_v2_rep43**: DONE (killed) — \n- **mvp_v2_rep42**: DONE (killed) — \n- **mvp_rep43**: DONE (killed) — \n- **mvp_rep42**: DONE (killed) — \n\n## 最新报告\n# Handover — 2026-05-25\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| c2_opt13b_a050_s42_fp32 | OPT-1.3B at α=0.50 should show PermG forward detection onset similar to Pythia-410M (6/8 at α=0.50), validating that the phase diagram structure generalizes beyond the Pythia family to the transition region | — | — | — |\n\n## 待处理\n- c2_opt13b_a050_s43_fp32_v2（准备中，spec 已填充，cuda:0 only）\n- C1: c1_interv_gpt2m_pred_s42 / c1_interv_gpt2m_react_s42 / c1_interv_opt13b_pred_s42 / c1_interv_opt13b_react_s42（命令就绪，待 C2 完成后注册）\n\n## 近期结论\n- **c2_opt13b_a050_s43_fp32** (failed): OPT-1.3B at α=0.50 seed 43 replication: cross-seed consistency of PermG forward detection in the transition region on a non-Pythia architecture\n- **null_fpr_s51_fp32** (success): Null experiment (α=0.00) for FPR estimation: no synthetic data contamination, all detection methods should show p>0.05, contributing to narrower FPR CI with 15 seeds\n- **null_t15_s42_fp32** (success): FPR verification at T=15: null condition (α=0.00) should show 0% PermG detection rate with longer observation window, confirming FPR control generalizes across T\n\n## 趋势\n成功 154 / 负向 4 / 失败 23 / 共 211\n累计 GPU: 8.4h\n\n## 下一步\n（无活跃 idea，请通过 ideas
…[truncated 1793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 6682
}
```

</details>

---


### Tool call

_source line 1470 · 2026-05-25T08:17:52.643930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1471 · 2026-05-25T08:17:53.607627+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\citep{shumailov2024curse,alemohammad2024mad}.
5	This process can be triggered by vanishingly small synthetic fractions~\citep{dohmatob2025strong}: lexical diversity narrows, calibration deteriorates, and each generation inherits the biases of its predecessors.
6	As machine-generated text grows prevalent on the web, such feedback loops pose a growing risk to production pipelines, and by the time standard quality metrics register degradation, the distribution may have already shifted irreversibly.
7	
8	This threat motivates a fundamental question: \emph{can we reliably detect the onset of model collapse?}
9	The answer is less clear than it might appear.
10	Iterative training produces short, noisy time series (often fewer than 15 points) where detection power drops sharply~\citep{boettiger2012limits}, and model collapse is a first-order transition~\citep{truong2026phase}, structurally ruling out the critical-slowing-down early-warning signals that ecologists rely on~\citep{scheffer2009early} (\S\ref{sec:related_work}).
11	More fundamentally, no prior work has systematically compared detection methods on this problem; as we show, the choice of statistical test alone can shift conclusions from universal detection to complete null on identical data.
12	
13	We systematically map this \emph{detectability landscape}---how detection outcomes vary across contamination levels ($\alpha$), observation windows ($T$), and statistical methods---on Pythia-410M~\citep{biderman2023pythia} across 13 contamination levels with multi-seed replication (Figure~\ref{fig:phase_diagram}).
14	Our central finding is a sharp detection phase transition: Permutation Granger causality (PermG) finds 0/8 significant canary$\to$downstream pairs through $\alpha{=}0.45$, then jumps to 6/8 withi
…[truncated 2788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 963
}
```

</details>

---


### Tool call

_source line 1472 · 2026-05-25T08:17:53.607998+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1473 · 2026-05-25T08:17:54.211167+00:00_

1	\FloatBarrier
2	\section{Related Work}
3	\label{sec:related_work}
4	
5	\subsection{Model Collapse: Theory and Empirical Evidence}
6	\label{sec:rw_collapse}
7	
8	Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}; \citet{schaeffer2025position} systematize eight distinct notions of collapse---our operationalization aligns with their \emph{distributional shift} family (definitions~D4--D6).
9	Theoretical analyses sharpen these results: \citet{dohmatob2024tale} recast collapse as changed scaling-law exponents, \citet{dohmatob2025strong} proved collapse at vanishingly small synthetic fractions, and \citet{truong2026phase} prove entropy collapse is a first-order transition, structurally ruling out critical-slowing-down early-warning signals~\citep{scheffer2009early,scheffer2012anticipating}.
10	Critical mixture ratios separating qualitative outcomes have independent precedent: \citet{kazdan2025collapse} map collapse conditions, \citet{gu2024cmr} establish scaling laws for critical ratios, and \citet{gu2025datamixing} show data mixing induces phase transitions in knowledge acquisition.
11	
12	\subsection{Detection of Synthetic Data Contamination}
13	\label{sec:rw_detection}
14	
15	Monitoring metrics proposed for collapse include expected calibration error (ECE)~\citep{du2025scales}, surplexity~\citep{gambetta2024surplexity}, and machine-generated text detection~\citep{drayson2025detection}; \citet{shi2025closer} independently validate entropy as a collapse diagnostic in diffusion models.
16	A complementary line of work pursues \emph{proactive} contamination prevention via watermarking~\citep{kirchenbauer2023watermark}; our distributional detection framework is \emph{reactive}---it identifies collapse from observed metric trajectories without requiring control over the generation process.
17	\citet{boettiger2012limits} establish fundamental power limits for early-warning detection in short time series ($T{<}25$), directl
…[truncated 2184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 1474 · 2026-05-25T08:17:54.211691+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1475 · 2026-05-25T08:17:54.563772+00:00_

1	\FloatBarrier
2	\section{Method}
3	\label{sec:method}
4	
5	\subsection{Cascade Ordering}
6	\label{sec:cascade}
7	
8	If distributional collapse follows a predictable ordering across metrics, the earliest-responding metric can serve as a canary signal.
9	We formalize known metric properties---entropy as a continuous indicator of mode concentration, diversity as a threshold indicator of lexical coverage---under mode amplification~\citep{shumailov2024curse,dohmatob2024tale} (derivations in Appendix~\ref{app:cascade_theory}).
10	
11	\begin{designprinciple}[Entropy responds before diversity]\label{thm:entropy_leads}
12	Under mode amplification: \textup{(a)} entropy can decrease while the $\epsilon$-effective support $S_\epsilon(p) {=} |\{i: p_i > \epsilon\}|$ (hence distinct-$n$) is unchanged; \textup{(b)} if distinct-$n$ decreases, entropy has already decreased.
13	\end{designprinciple}
14	
15	Intuitively, entropy responds to any redistribution of probability mass (a continuous change), whereas diversity metrics like distinct-$n$ only change when tokens are pushed entirely below the generation threshold (a discrete event).
16	This measurement asymmetry ensures entropy shifts before diversity under gradual mode amplification.
17	The margin $\gamma = \min_{i: p_i > \epsilon}(p_i - \epsilon)$ quantifies how much shift diversity absorbs silently.
18	
19	\begin{designprinciple}[Diversity lag $\geq 1$ generation]\label{prop:div_lag}
20	If the per-generation perturbation satisfies $\alpha\|\mathcal{T}(p_t) - p_t\|_\infty < \gamma(p_t, \epsilon)$ through entropy onset $t_H$, then diversity onset $t_D \geq t_H + 1$.
21	\end{designprinciple}
22	
23	ECE co-moves with entropy at zero lag ($\Delta\mathrm{ECE} \approx \Delta C > 0$ whenever $\Delta\bar{H} < 0$; Appendix~\ref{app:cascade_theory}), yielding a three-stage cascade $\{H, \mathrm{ECE}\} \to \mathrm{Distinct}$-$n$.
24	This ordering holds in 14/15 experiments at $\alpha \geq 0.30$, with entropy and ECE consistently reaching
…[truncated 7251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 1476 · 2026-05-25T08:17:54.564243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1477 · 2026-05-25T08:17:55.066658+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study iterative training collapse using Pythia-410M~\citep{biderman2023pythia} as the primary architecture.
8	Training data is drawn from WikiText-103~\citep{merity2017pointer} following the replace paradigm of~\citet{shumailov2024curse}: each generation fine-tunes on a mixture of $\alpha$ synthetic and $(1{-}\alpha)$ real data, generates 5{,}000 replacement samples, and fully replaces the synthetic pool (hyperparameters in Appendix~\ref{app:training_details}).
9	We run $T{=}10$ generations across 13 contamination levels ($\alpha \in \{0.00, \ldots, 1.00\}$) with multi-seed replication, yielding ${\sim}1{,}500$ statistical tests after BH-FDR correction~\citep{benjamini1995controlling}.
10	We track two \emph{canary metrics} (token entropy and ECE) and three \emph{downstream metrics}: distinct-1, distinct-2~\citep{li2016diversity}, and perplexity (distinct-3: Appendix~\ref{app:distinct3}).
11	PermG uses 5{,}000 permutations on first-differenced series~\citep{shojaie2022granger} with maximum lag~5.
12	
13	
14	\subsection{Sharp Detection Onset}
15	\label{sec:regime}
16	
17	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ even at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$.
18	Despite this ubiquitous degradation, Granger detectability is sharply regime-dependent.
19	PermG finds 0/8 canary$\to$downstream pairs FDR-significant from $\alpha{=}0.00$ through $\alpha{=}0.45$, then jumps to 6/8 (Clopper--Pearson 95\% CI $[0.25, 0.92]$) at $\alpha{=}0.50$, uniformly across all 3~fp32 seeds.
20	
21	\begin{figure}[t]
22	\centering
23	\includegraphics[width=\columnwidth]{figures/metric_trajectory.pdf}
24	\caption{Metric trajectories at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead 
…[truncated 10212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1478 · 2026-05-25T08:17:55.067196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1479 · 2026-05-25T08:17:55.569618+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	Our Granger-precedence claim is scoped to temporal predictive improvement~\citep{granger1969investigating,shojaie2022granger}: bivariate tests cannot exclude confounders, and the FPR CI ($[1.8\%, 16.2\%]$) means Type~I error may be non-negligible.
4	Four of fifteen cross-architecture conditions do not confirm forward detection (\S\ref{sec:generalization}), each isolating a distinct PermG assumption violation---precision sensitivity (GPT-2 bf16), seed dependence (Pythia-1.4B), and entropy decoupling (SmolLM3-3B)---requiring architecture-specific null calibration before deployment (Appendix~\ref{app:extended_discussion}).
5	More broadly, our observation sequences ($T{=}10$--$25$) are far shorter than econometric standards ($T{\geq}100$); permutation testing avoids asymptotic assumptions but cannot recover power lost to short samples~\citep{shojaie2022granger}.
6	Bivariate tests are susceptible to omitted variable bias---first-differencing removes shared linear trends but nonlinear confounds remain possible---and PermG tests linear precedence only; transfer entropy (Appendix~\ref{app:transfer_entropy}) yields 0/192 significant pairs.
7	Partial correlation provides supporting evidence: after controlling for generation number, contemporaneous associations weaken ($\bar{|r|}$: $0.590{\to}0.381$) while lagged correlations strengthen ($0.759{\to}0.841$), consistent with genuine temporal precedence rather than shared-trend artifacts (Appendix~\ref{app:partial_corr}).
8	
9	Despite these individual limitations, the five methods exhibit complementary strengths.
10	Shapley value decomposition over all $2^5{=}32$ coalitions (Appendix~\ref{app:shapley}) shows DiffXCorr achieving the best combined Shapley contribution ($-0.299$) by detecting bidirectional coupling that directional methods miss, while PermG ranks best among directional methods ($-0.141$).
11	This complementarity explains why consensus voting outperforms any single me
…[truncated 1602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1480 · 2026-05-25T08:17:55.570024+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1481 · 2026-05-25T08:17:56.021848+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Iterative training collapse exhibits a sharp detection phase transition: PermG detection jumps from 0/8 to 6/8 significant pairs within 2~percentage points of $\alpha_c \approx 0.50$, organizing three regimes (blind, onset, detection) that characterize when statistical monitoring can and cannot succeed.
5	The detection boundary shifts leftward with longer observation ($\alpha_c(T) \propto T^{-\gamma}$), and systematic method comparison reveals that single-method analyses are unreliable: null-control FPR spans 6.7\% (PermG; 95\% CI $[1.8\%, 16.2\%]$, 10~seeds) to 94.4\%.
6	Token entropy exhibits robust one-generation-ahead precedence over diversity collapse (24/24 forward, 0/24 reverse at $\alpha{=}1.0$; ${\geq}6/8$ in 11/15 cross-architecture conditions at $\alpha{=}1.0$).
7	The blind zone below $\alpha_c$ constrains practical deployment to settings with sufficient contamination; evaluation at ${>}$7B parameters remains open.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 1482 · 2026-05-25T08:17:56.022407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1483 · 2026-05-25T08:17:56.976190+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Scope and generalizability.}
5	Our landscape characterization uses Pythia-410M as the primary architecture; the phase diagram is Pythia-family-only, frontier-scale behavior (${>}$7B) is untested, and cross-architecture evaluation is limited to $\alpha{=}1.0$.
6	All experiments use full replacement with a single decoding strategy (temperature~$1.0$, top-$k{=}50$); data accumulation~\citep{dey2024breaking} or lower temperatures would shift the landscape.
7	More fundamentally, the blind zone below $\alpha_c$ means that substantial quality degradation (e.g., ${\sim}40\%$ distinct-1 decline at $\alpha{=}0.25$) occurs before any statistical method signals detection.
8	The framework is therefore better characterized as a confirmation tool for ongoing collapse than an early-warning system.
9	
10	\paragraph{Statistical power.}
11	PermG's empirical FPR is 6.7\% (CI $[1.8\%, 16.2\%]$) and $K{\geq}3$ consensus yields 10.0\% (6/60); per-condition detection rates carry wide binomial CIs (e.g., $[0.25, 0.92]$ for 6/8), so the phase diagram represents a coarse topology rather than precise probability estimates.
12	The 3-seed phase diagram limits variance estimation (2 degrees of freedom); the detection boundary CI should be interpreted with this constraint.
13	MMCT provides marginal improvement over standalone PermG in the current experimental setting; its primary value is as an analytical framework for comparing methods rather than a deployment-ready ensemble.
14	
15	\paragraph{Causal interpretation.}
16	Permutation Granger testing establishes temporal precedence, not causation; our short-sequence regime ($T{\leq}25$) limits statistical power relative to econometric standards ($T{\geq}100$), and nonlinear alternatives to the linear PermG test yield no significant results in our setting (see \S\ref{sec:discussion}).
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 1484 · 2026-05-25T08:17:57.227545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1485 · 2026-05-25T08:17:57.482412+00:00_

File content (43508 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 254
}
```

</details>

---


### Tool call

_source line 1486 · 2026-05-25T08:17:57.533052+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null || echo \"NO_ISSUES_FILE\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1487 · 2026-05-25T08:17:58.336852+00:00_

&lt;persisted-output>
Output too large (38.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-review-director-741faaa0/15434102-6a9f-4dbc-9e4f-0e014bffe0f2/tool-results/bmoxaliur.txt

Preview (first 2KB):
issues:
# ============================================================
# Round 1-11 历史 resolved — 保留跨轮次记录
# ============================================================
- id: "R1-N1"
  summary: "Ground-truth pairs 定义存在循环论证"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Effect-size GT 重定义完成。"
  resolution_round: 1

- id: "R1-N2"
  summary: "FPR=0% 标定仅基于单 seed"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "α=0.0 三 seed FPR 验证完成。"
  resolution_round: 1

- id: "R1-N3"
  summary: "α=0.50 和 α=0.75 仅 1 seed"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Multi-seed 补充完成。"
  resolution_round: 1

- id: "R2-N1"
  summary: "核心方法论为计量经济学已有知识的直接迁移，新颖性有限"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Round 1 三层定位 reframe 完成。"
  resolution_round: 1

- id: "R2-N2"
  summary: "α=0.75 multi-seed 实验未完成 + Appendix A 缺失"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "完成。"
  resolution_round: 1

- id: "R2-N3"
  summary: "实验规模过窄"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "跨架构验证已扩展至 15 model-seed 组合。"
  resolution_round: 1

- id: "R1-W1"
  summary: "Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "核心修复完
…[truncated 287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 1488 · 2026-05-25T08:17:58.337380+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/config.yaml 2>/dev/null | head -100",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/agent/config.yaml 2>/dev/null | head -100",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1489 · 2026-05-25T08:17:58.438098+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1490 · 2026-05-25T08:18:09.408793+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"config.yaml\" -o -name \"config.yml\" -o -name \"project.yaml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 1491 · 2026-05-25T08:18:09.710590+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1492 · 2026-05-25T08:18:09.861450+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1493 · 2026-05-25T08:18:09.912292+00:00_

1	\appendix
2	
3	\section{Training Details and Metric Drift}
4	\label{app:training_details}
5	\label{app:drift}
6	
7	\paragraph{Hyperparameters.}
8	Each generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).
9	Generation uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.
10	Canary metrics: token entropy $H(p_\theta | \text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.
11	Additional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.
12	
13	\paragraph{Architecture-specific training.}
14	Table~\ref{tab:arch_hyperparams} reports training hyperparameters for each architecture in the cross-architecture evaluation (\S\ref{sec:generalization}).
15	All models use the same generation parameters (temperature~$1.0$, top-$k{=}50$, max length 512) to control for decoding-strategy confounds.
16	Batch sizes are adjusted for GPU memory constraints; learning rates follow the respective model families' recommended fine-tuning ranges.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Per-architecture training hyperparameters.}
22	\label{tab:arch_hyperparams}
23	\begin{tabular}{lcccl}
24	\toprule
25	Model & Batch & LR & Steps & Precision \\
26	\midrule
27	Pythia-410M & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
28	Pythia-1.4B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
29	Pythia-6.9B & 2 & $2{\times}10^{-5}$ & 5{,}000 & bf16 \\
30	GPT-2-medium & 32 & $5{\times}10^{-5}$ & 5{,}000 & fp32/bf16 \\
31	OPT-1.3B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
32	Qwen3.5-0.8B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
33	SmolLM3-3B & 4 & $2{\times}10^{-5}$ & 5{,}000 & fp32 \\
34	\bottomrule
35	\end{tabular}
36	\end{table}
37	
38	\paragraph{Metric computation details.}
39	Token entropy is computed as $H(p_\the
…[truncated 6129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1494 · 2026-05-25T08:18:17.414888+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4 -maxdepth 3 -name \"*.yaml\" -path \"*/distrib_canary_collapse/*\" 2>/dev/null | head -10",
  "description": "Find project yaml config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4 -maxdepth 3 -name \"*.yaml\" -path \"*/distrib_canary_collapse/*\" 2>/dev/null | head -10",
    "description": "Find project yaml config files"
  }
}
```

</details>

---


### Tool result

_source line 1495 · 2026-05-25T08:18:17.867153+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/decisions.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/experiment_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1496 · 2026-05-25T08:18:18.370134+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1497 · 2026-05-25T08:18:18.822476+00:00_

1	% ============================================================
2	% GAME THEORY / ATTRIBUTION
3	% ============================================================
4	
5	@incollection{shapley1953value,
6	  title     = {A Value for $n$-Person Games},
7	  author    = {Shapley, Lloyd S.},
8	  booktitle = {Contributions to the Theory of Games II},
9	  editor    = {Kuhn, Harold W. and Tucker, Albert W.},
10	  pages     = {307--317},
11	  year      = {1953},
12	  publisher = {Princeton University Press},
13	}
14	
15	% ============================================================
16	% CORE MODEL COLLAPSE
17	% ============================================================
18	
19	@article{shumailov2024curse,
20	  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},
21	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},
22	  journal   = {Nature},
23	  year      = {2024},
24	  url       = {https://arxiv.org/abs/2305.17493},
25	}
26	
27	@inproceedings{alemohammad2024mad,
28	  title     = {Self-Consuming Generative Models Go {MAD}},
29	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},
30	  booktitle = {International Conference on Learning Representations},
31	  year      = {2024},
32	  url       = {https://arxiv.org/abs/2307.01850},
33	}
34	
35	@inproceedings{dohmatob2024tale,
36	  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},
37	  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},
38	  booktitle = {International Conference on Machine Learning},
39	  year      = {2024},
40	  url       = {https://arxiv.org/abs/2402.07043},
41	}
42	
43	@inproceedings{dohmatob2025strong,
44	  title     = {Strong Model Collapse},
45	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
46	  bo
…[truncated 2246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1498 · 2026-05-25T08:18:18.974443+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/*.tex",
  "description": "Count lines in each tex file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/*.tex",
    "description": "Count lines in each tex file"
  }
}
```

</details>

---


### Tool result

_source line 1499 · 2026-05-25T08:18:19.025137+00:00_

     7 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex
  1692 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex
    38 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex
     7 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex
    17 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex
    35 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion_reframe.tex
    12 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex
   149 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex
   131 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex
    45 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/intro_reframe.tex
    38 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex
    16 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex
    45 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex
   103 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex
    61 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex
    29 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex
    22 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work_reframe.tex
    21 /home/ubuntu/.agent-ml-research-i
…[truncated 82 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1500 · 2026-05-25T08:18:26.210460+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/constraints.yaml 2>/dev/null || echo \"NOT_FOUND\"",
  "description": "Check external review config in constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/constraints.yaml 2>/dev/null || echo \"NOT_FOUND\"",
    "description": "Check external review config in constraints.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1501 · 2026-05-25T08:18:26.713685+00:00_

NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 1502 · 2026-05-25T08:18:26.764531+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf"
  }
}
```

</details>

---


### Tool result

_source line 1503 · 2026-05-25T08:18:26.816481+00:00_

This PDF has 36 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1504 · 2026-05-25T08:18:32.386663+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf",
  "pages": "1-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf",
    "pages": "1-10"
  }
}
```

</details>

---


### Tool call

_source line 1505 · 2026-05-25T08:18:32.991491+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf",
  "pages": "11-20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf",
    "pages": "11-20"
  }
}
```

</details>

---


### Tool result

_source line 1506 · 2026-05-25T08:18:33.292696+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf (1.2MB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool result

_source line 1507 · 2026-05-25T08:18:33.925788+00:00_

PDF pages extracted: 10 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf (1.2MB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 934
}
```

</details>

---


### Tool call

_source line 1508 · 2026-05-25T08:19:22.212990+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "distrib_canary_collapse",
  "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
  }
}
```

</details>

---


### Tool result

_source line 1509 · 2026-05-25T08:19:46.317753+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 24104
}
```

</details>

---


### Tool call

_source line 1510 · 2026-05-25T08:19:46.470414+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题：Characterizing the Detectability Landscape of Iterative Model Collapse\n- 目标 venue：EMNLP 2026（通过 ARR 提交）\n- 截止日期：2026-05-25\n- 格式：ACL 模板，长文 8 页正文限制，double-blind\n- 论文路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex`\n- PDF 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 统计方法论\n- PermG（Permutation Granger causality）的实现是否正确？5,000 permutations + BH-FDR 校正是否足够？\n- 短时间序列（T=10–25）下 Granger 检验的统计功效是否被充分讨论？\n- FPR 标定：6.7% CI [1.8%, 16.2%] 基于 10 seeds/60 pairs——样本量是否足以支撑主要结论？\n- MMCT（Algorithm 1）的 FPR-inverse weighting 设计是否合理？权重方案是否有理论支撑？\n- First-differencing 消除 canary→perplexity 但保留 canary→diversity——这是否真正排除了 spurious regression？\n\n### 2. 实验设计\n- Phase diagram 基于 3 seeds（2 自由度）——方差估计是否可靠？\n- α=0.60 non-monotonic anomaly 的解释（temporal lag compression）是否有直接证据支持？\n- Cross-architecture evaluation 仅在 α=1.0 做——phase diagram 在其他架构上是否通用？\n- Intervention 实验（64% perplexity reduction）仅在 α=1.0 做——在 blind zone 附近（α≈0.50）效果如何？\n- WikiText-103 作为唯一训练数据集——domain 泛化性如何？\n\n### 3. 定量声明的可靠性\n- 检查所有定量声明是否有充分的置信区间\n- 6/8 detection rate 的 Clopper-Pearson CI [0.25, 0.92] 非常宽——是否足以支撑 \"sharp transition\" 的说法？\n- Table 2 中 K≥3 consensus FPR=10.0%——是否显著高于 5% nominal level？\n\n### 4. 格式合规\n- 正文是否在 8 页以内？\n- Limitations section 是否符合 EMNLP 要求？\n- 匿名性是否保持（无 deanonymizing 信息）？\n\n请按以下格式输出：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/major/minor）\n4. Questions（需要作者回答的问题）\n5. Missing References（遗漏的重要相关工作）\n6. Overall Assessment（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验有效性**。\n\n## 论文信息\n- 标题：Characterizing the Detectability Landscape of Iterative Model Collapse\n- 目标 venue：EMNLP 2026（通过 ARR 提交）\n- 截止日期：2026-05-25\n- 格式：ACL 模板，长文 8 页正文限制，double-blind\n- 论文路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex`\n- PDF 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 统计方法论\n- PermG（Permutation Granger causality）的实现是否正确？5,000 permutations + BH-FDR 校正是否足够？\n- 短时间序列（T=10–25）下 Granger 检验的统计功效是否被充分讨论？\n- FPR 标定：6.7% CI [1.8%, 16.2%] 基于 10 seeds/60 pairs——样本量是否足以支撑主要结论？\n- MMCT（Algorithm 1）的 FPR-inverse weighting 设计是否合理？权重方案是否有理论支撑？\n- First-differencing 消除 canary→perplexity 但保留 canary→diversity——这是否真正排除了 spurious regression？\n\n### 2. 实验设计\n- Phase diagram 基于 3 seeds（2 自由度）——方差估计是否可靠？\n- α=0.60 non-monotonic anomaly 的解释（temporal lag compression）是否有直接证据支持？\n- Cross-architecture evaluation 仅在 α=1.0 做——phase diagram 在其他架构上是否通用？\n- Intervention 实验（64% perplexity reduction）仅在 α=1.0 做——在 blind zone 附近（α≈0.50）效果如何？\n- WikiText-103 作为唯一训练数据集——domain 泛化性如何？\n\n### 3. 定量声明的可靠性\n- 检查所有定量声明是否有充分的置信区间\n- 6/8 detection rate 的 Clopper-Pearson CI [0.25, 0.92] 非常宽——是否足以支撑 \"sharp transition\" 的说法？\n- Table 2 中 K≥3 consensus FPR=10.0%——是否显著高于 5% nominal level？\n\n### 4. 格式合规\n- 正文是否在 8 页以内？\n- Limitations section 是否符合 EMNLP 要求？\n- 匿名性是否保持（无 deanonymizing 信息）？\n\n请按以下格式输出：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/major/minor）\n4. Questions（需要作者回答的问题）\n5. Missing References（遗漏的重要相关工作）\n6. Overall Assessment（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
  }
}
```

</details>

---


### Tool result

_source line 1511 · 2026-05-25T08:20:05.948271+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19477
}
```

</details>

---


### Tool call

_source line 1512 · 2026-05-25T08:20:06.067626+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题：Characterizing the Detectability Landscape of Iterative Model Collapse\n- 目标 venue：EMNLP 2026（通过 ARR 提交）\n- 截止日期：2026-05-25\n- 格式：ACL 模板，长文 8 页正文限制，double-blind\n- 论文路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex`\n- PDF 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献评估\n- 核心方法（Granger causality + permutation testing）是计量经济学的既有工具——迁移到 model collapse 检测的新颖性有多大？\n- \"Detection phase transition\" 是真正的新发现还是统计功效的自然结果？（功效随 signal strength 增加而增加是预期的）\n- MMCT 是否只是对 specification curve analysis 的简单应用？\n- 与 Shumailov et al. (2024), Dohmatob et al. (2025), Truong & Truong (2026) 相比，本文的增量贡献是什么？\n- Design Principles 1-2 是否足够 novel——entropy 先于 discrete metrics 响应是否 trivially true？\n\n### 2. Related Work 覆盖\n- 是否遗漏了重要的 model collapse 检测相关工作？\n- 是否遗漏了 Granger causality 在 NLP/ML 领域的应用？\n- 2025-2026 年的最新工作是否被充分覆盖？特别注意搜索以下方向的最新文献：\n  - Model collapse detection and monitoring\n  - Synthetic data contamination detection\n  - Distribution shift detection in LLMs\n  - 用 web_search 搜索 2025-2026 年可能遗漏的相关工作\n\n### 3. 写作质量\n- 叙事结构是否清晰？reader 能否在 first pass 理解主要贡献？\n- 术语一致性：Granger causality vs. Granger precedence vs. temporal predictive improvement——是否混淆？\n- \"Design Principle\" 这个标签是否恰当？（它们更像 propositions 或 observations）\n- Abstract 是否准确反映论文内容？是否有 overclaiming？\n- 主文与 appendix 的分配是否合理？（26 页 appendix 是否有核心内容被遗漏在正文之外？）\n\n### 4. 论文完整性\n- 实验是否足以支撑所有 claims？\n- 是否有 claim 缺少实验支持？\n- 负面结果（4/15 non-confirming conditions）的讨论是否充分？\n- Intervention 实验是否只是 proof-of-concept 而被 overclaimed？\n\n### 5. 格式合规\n- 正文是否在 8 页以内？\n- Abstract 是否在 200 词以内？\n- 匿名性检查\n\n请按以下格式输出：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/major/minor）\n4. Questions（需要作者回答的问题）\n5. Missing References（遗漏的重要相关工作，请务必用 web_search 搜索验证）\n6. Overall Assessment（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。\n\n## 论文信息\n- 标题：Characterizing the Detectability Landscape of Iterative Model Collapse\n- 目标 venue：EMNLP 2026（通过 ARR 提交）\n- 截止日期：2026-05-25\n- 格式：ACL 模板，长文 8 页正文限制，double-blind\n- 论文路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex`\n- PDF 路径：`/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_round_16/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性与贡献评估\n- 核心方法（Granger causality + permutation testing）是计量经济学的既有工具——迁移到 model collapse 检测的新颖性有多大？\n- \"Detection phase transition\" 是真正的新发现还是统计功效的自然结果？（功效随 signal strength 增加而增加是预期的）\n- MMCT 是否只是对 specification curve analysis 的简单应用？\n- 与 Shumailov et al. (2024), Dohmatob et al. (2025), Truong & Truong (2026) 相比，本文的增量贡献是什么？\n- Design Principles 1-2 是否足够 novel——entropy 先于 discrete metrics 响应是否 trivially true？\n\n### 2. Related Work 覆盖\n- 是否遗漏了重要的 model collapse 检测相关工作？\n- 是否遗漏了 Granger causality 在 NLP/ML 领域的应用？\n- 2025-2026 年的最新工作是否被充分覆盖？特别注意搜索以下方向的最新文献：\n  - Model collapse detection and monitoring\n  - Synthetic data contamination detection\n  - Distribution shift detection in LLMs\n  - 用 web_search 搜索 2025-2026 年可能遗漏的相关工作\n\n### 3. 写作质量\n- 叙事结构是否清晰？reader 能否在 first pass 理解主要贡献？\n- 术语一致性：Granger causality vs. Granger precedence vs. temporal predictive improvement——是否混淆？\n- \"Design Principle\" 这个标签是否恰当？（它们更像 propositions 或 observations）\n- Abstract 是否准确反映论文内容？是否有 overclaiming？\n- 主文与 appendix 的分配是否合理？（26 页 appendix 是否有核心内容被遗漏在正文之外？）\n\n### 4. 论文完整性\n- 实验是否足以支撑所有 claims？\n- 是否有 claim 缺少实验支持？\n- 负面结果（4/15 non-confirming conditions）的讨论是否充分？\n- Intervention 实验是否只是 proof-of-concept 而被 overclaimed？\n\n### 5. 格式合规\n- 正文是否在 8 页以内？\n- Abstract 是否在 200 词以内？\n- 匿名性检查\n\n请按以下格式输出：\n1. Summary（2-3 句）\n2. Strengths（逐条）\n3. Weaknesses（逐条，标注 severity: critical/major/minor）\n4. Questions（需要作者回答的问题）\n5. Missing References（遗漏的重要相关工作，请务必用 web_search 搜索验证）\n6. Overall Assessment（评分 + 置信度）\n\n评分标准（EMNLP 2026 ARR）：5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit"
  }
}
```

</details>

---


### Tool result

_source line 1513 · 2026-05-25T08:20:07.755068+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1687
}
```

</details>

---


### Assistant

_source line 1514 · 2026-05-25T08:20:22.664703+00:00_

Round 1 已启动：

| 角色 | 状态 | 侧重 |
|------|------|------|
| Reviewer 1 | ✅ 已派发 | 方法严谨性 + 实验有效性 |
| Reviewer 2 | ✅ 已派发 | 新颖性 + 完整性 + 写作质量 |
| 视觉审查 | ✅ 已派发 | PDF 排版质量（非评分项） |
| 外部审稿 | ⏭ 跳过 | 项目未配置 paperreview.ai |

等待两位 Reviewer 完成独立初审。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 138

## Round 138

2 recorded events


### User

_source line 1515 · 2026-05-25T08:28:51.547372+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告

### 论文信息
- **标题**: Characterizing the Detectability Landscape of Iterative Model Collapse
- **Venue**: EMNLP 2026 (via ARR)
- **审查侧重**: 新颖性 + 完整性 + 写作质量 + Related Work 覆盖 + 格式合规

---

## 1. Summary

本文系统地研究了迭代训练 model collapse 的**可检测性**问题。核心方法是将 Granger causality（置换检验版本 PermG）应用于 canary metrics（token entropy, ECE）和 downstream metrics（distinct-n, perplexity）之间的时序领先-滞后关系检测。主要发现包括：(1) 在 α_c ≈ 0.50 处存在一个陡峭的检测相变——PermG 从 0/8 显著对跳到 6/8；(2) 五种统计方法在相同数据上 FPR 从 6.7% 到 94.4%，说明单方法分析不可靠；(3) entropy 在 diversity 之前至少一代响应 collapse。实验以 Pythia-410M 为主，在 5 个模型家族（345M–6.9B）上做了 α=1.0 的 cross-architecture 验证。

---

## 2. Strengths

**S1. 方法敏感性的实证发现具有重要警示意义。** 五种 lead-lag 检测方法在相同数据上产生 FPR 从 6.7% 到 94.4% 的巨大差异（κ=0.185），这个发现本身就是对该领域的重要贡献。它表明 model collapse 检测文献中，使用单一统计方法的研究结论可能不可靠。这个 finding 比 phase transition 本身更有价值。

**S2. 实验设计严谨，统计控制充分。** 论文在多个层面做了适当的统计控制：null-control (α=0.0) 基线、BH-FDR 多重检验校正、置换检验避免参数假设、多 seed 复制。Specification curve analysis 跨 1,160 个配置验证了结果的稳健性（Figure 6; Appendix D）。这种严谨程度在 model collapse 检测文献中少见。

**S3. 对 limitations 和 non-confirming cases 的讨论坦诚且详尽。** 论文明确讨论了 4/15 non-confirming cross-architecture conditions，每个都被归因到具体的 PermG assumption violation（precision sensitivity, bidirectional confounding, seed dependence, entropy decoupling）。Limitations section 坦承 blind zone 意味着该框架更适合作为"确认工具"而非"预警系统"（Section Limitations, "confirmation tool for ongoing collapse than an early-warning system"）。这种自我认识是积极的。

**S4. Appendix 内容充实，支撑主文 claims。** 26 页的 appendix 包含了完整的理论推导（Appendix X: Cascade Ordering Theory），Shapley 分解（Appendix P），partial correlation 分析（Appendix V），cross-architecture 细节（Appendix Z），power simulation（Appendix Y）等。核心 claims 都有 appendix 中的详细支撑。

**S5. 检测边界的参数化建模有参考价值。** α_c(T) = A·T^{-γ} 的参数化（Eq. 1-2）虽然拟合精度有限（γ 的 95% CI [0.64, 2.08] 很宽），但提供了一个定量框架来思考"需要多长观测窗口才能检测给定水平的 contamination"，对 practitioners 有实用指导意义。

---

## 3. Weaknesses

**W1 [major] "检测相变"的新颖性存疑——可能只是统计功效的自然行为。**
- 具体位置：Section 4.2 (Sharp Detection Onset), Section 4.3 (Dose-Response)
- 问题：任何统计检验在信号强度跨过检测阈值时都会从不显著跳到显著，这是统计功效（power）的基本性质。论文声称 sigmoid Hill coefficient k=15.7 比 smooth-signal predictions 陡峭 3-4x（Section 3.4, "3–4× steeper than smooth-signal predictions"），但这个比较的 baseline 是论文自己构建的 power simulation（Appendix Y），而非已有文献中标准的 phase transition 判据。论文未排除实验设计本身（full replacement, 离散的 α 取值, 短时间序列 T=10）对 transition steepness 的贡献。
- 为什么影响接收：这是论文的**核心 claim**（Contribution 1）。如果 phase transition 只是 power curve 在有限样本下的自然表现，那么 Contribution 1 的新颖性大幅降低。
- 建议修改方向：(a) 与标准 power analysis 文献中的 detection threshold behavior 做更严格的比较；(b) 讨论 transition steepness 可能来自实验 discretization 而非物理现象的可能性；(c) 考虑重新定位为"empirical characterization of detection limits"而非"phase transition discovery"。

**W2 [major] 核心方法论的新颖性有限——Granger causality + 置换检验是成熟工具的直接应用。**
- 具体位置：Section 3.2 (Design Considerations), Section 3.3 (Method Sensitivity Analysis)
- 问题：Permutation Granger causality 是计量经济学的标准工具（Granger 1969; Shojaie & Fox 2022），first-differencing 去趋势也是标准做法（Granger & Newbold 1974），BH-FDR 校正是通用的多重检验方法。MMCT（Algorithm 1）本质上是一个 FPR-inverse weighted voting scheme，算法本身的技术贡献有限。论文的贡献更多在于"将这些工具应用到 model collapse 检测场景"，而非方法论创新。
- 为什么影响接收：对于主会议论文，期望有更高的方法论新颖性。
- 建议修改方向：将论文重新定位为**实证研究**（empirical study），强调实验发现（方法敏感性、检测景观映射）而非方法论贡献。如果保持方法论定位，需要更清楚地阐述为什么标准工具在此场景下的应用是 non-trivial 的（例如，短时序列 T<25 下 Granger 检验的 finite-sample 表现是否有理论上的新挑战）。

**W3 [major] Blind zone 根本性地限制了框架的实用价值。**
- 具体位置：Section 4.2, Limitations
- 问题：在 α < 0.50 时，distinct-1 已下降 ~40%（Section 4.2, "at α=0.10, distinct-1 has already dropped by 39.6%"），但 Granger 检测完全失效（0/8）。论文在 Limitations 中将框架定位为"confirmation tool"而非"early-warning system"，但 abstract 和 introduction 的叙事仍然暗示这是一个有实用价值的检测框架（"can we reliably detect the onset of model collapse?"）。这造成了 framing 与实际能力之间的张力。
- 为什么影响接收：如果该框架只能在 contamination 已经很高（>50%）时才能检测，其实际部署场景非常有限——现实世界中，practitioners 不太可能在 50% 以上的 synthetic contamination 下才开始关注。
- 建议修改方向：(a) 在 abstract 和 introduction 中更明确地 scope practical claims；(b) 讨论在什么现实场景下 α > 0.50 是可能的；(c) 明确讨论该框架与更简单的 threshold-based monitoring 相比的优势场景。

**W4 [major] Cross-architecture 验证仅在 α=1.0 下进行，限制了 generalizability claims。**
- 具体位置：Section 4.5, Figure 8
- 问题：Phase diagram（Figure 1）是 Pythia-410M-specific 的。Cross-architecture 评估（Section 4.5）仅在 α=1.0（full synthetic replacement）下进行——这是最有利的条件。论文不知道 α_c ≈ 0.50 的 phase transition 是否在其他架构上存在。事实上，GPT-2 和 Pythia-1.4B 的 non-confirming conditions 暗示 phase diagram 可能是 architecture-specific 的。
- 为什么影响接收：论文的 Contribution 1-2（phase transition 和 detectability landscape）的 generalizability 未被充分验证。
- 建议修改方向：至少在 1-2 个其他架构上跑完整的 α grid，验证 phase diagram 结构是否保持。如果资源不允许，应在 claims 中更明确地限定为 "Pythia-410M-specific findings"。

**W5 [major] Design Principles 1-2 的新颖性和标签存疑。**
- 具体位置：Section 3.1
- 问题：Design Principle 1 说 "entropy responds before diversity"——直觉上这几乎是 trivially true：entropy 是连续量，对概率分布任何微小变化都响应；distinct-n 是离散量（token 计数），只在 token 概率跌破阈值时才变化。这个 measurement resolution asymmetry 论文自己在 Discussion（Section 5）中也承认了（"whether entropy's 'leading' behavior partly reflects measurement-resolution asymmetry"）。将此包装为 "Design Principle" 在修辞上有过度包装之嫌——它们更适合被称为 Proposition 或 Observation。
- 为什么影响接收：不至于单独否决，但削弱了 Contribution 4 的说服力。
- 建议修改方向：(a) 将 "Design Principle" 重命名为 "Proposition" 或 "Observation"；(b) 更深入地讨论 measurement resolution asymmetry 是否是 entropy leading 的主要原因而非 genuine temporal precedence。

**W6 [minor] 正文可能略超 8 页限制。**
- 具体位置：Section 6 (Conclusion) 溢出到第 9 页
- 问题：从 PDF 渲染结果看，Conclusion (Section 6) 从第 8 页底部开始，但约 8-10 行文本延续到了第 9 页（Limitations 之前）。根据 EMNLP 2026 规则，正文（不含 Limitations 和 References）限 8 页。
- 建议修改方向：压缩 Discussion 或 Conclusion 几句话即可解决。

**W7 [minor] Intervention 实验（Section 4.6）仅在 α=1.0 下进行，但叙事中被提升为重要贡献。**
- 具体位置：Section 4.6, Abstract
- 问题：Predictive cessation 仅在最有利条件（α=1.0）下测试，且只是 proof-of-concept。但 abstract 将 "reduces peak perplexity by 64%" 作为最后的 highlight，Contribution 4 也以此为核心。在 blind zone（α < 0.50）中 entropy 信号不可检测，意味着该 intervention 策略在最需要它的场景下无法工作。
- 建议修改方向：在 abstract 和贡献列表中降低 intervention 的prominence，明确标注为 "proof-of-concept under favorable conditions"。

**W8 [minor] 术语使用不完全一致。**
- 具体位置：全文
- 问题：论文在 "Granger causality"、"Granger precedence"、"temporal predictive improvement" 三个术语之间切换。虽然论文在 Section 3.2 和 Discussion 中都做了 scoping（"not mechanistic causation"），但 Section 1 introduction 中仍使用 "Permutation Granger causality" 作为方法名，而 Discussion 中则用 "Granger-precedence claim"。建议统一使用 "Granger precedence" 或 "temporal precedence testing"，避免读者将其与 causal claims 混淆。

---

## 4. Questions for Authors

**Q1.** Phase transition steepness (k=15.7) 的 3-4x 比较是和什么 baseline 比的？能否提供标准 power analysis 下的 expected transition steepness 作为对照？如何排除 steepness 来自 α grid 的离散化（13 个取值点）而非真实的物理现象？

**Q2.** 在 blind zone (α < 0.50) 中，distinct-1 已下降 ~40% 但 Granger 检测完全失效。能否讨论：是否存在更灵敏的 canary metric（例如某种 spectral 或 information-theoretic measure）可以降低 α_c？论文引用了 SIGMA (Gu et al. 2026) 的 spectral approach 但未纳入方法比较。

**Q3.** MMCT 在当前实验设置下相比 standalone PermG 的边际改进有多大？Limitations 中承认 "MMCT provides marginal improvement over standalone PermG"——如果 MMCT 不比单用 PermG 好很多，那么 Algorithm 1 的贡献是否应降级为 analytical framework 而非 practical tool？

**Q4.** α=0.60 的 non-monotonic anomaly 在所有 seed 上都复现（Section 4.3, "consistent across seeds 0/8 for both tested seeds"），论文将其归因于 temporal lag compression。能否提供更直接的证据支持这一解释？例如，在 α=0.60 下 entropy 和 distinct-n 的 lag 是否确实更短？

**Q5.** 论文的 intervention 策略（entropy 降 15% 时停止 synthetic training）需要知道 generation-0 的 entropy baseline。在实际部署中（未知初始状态），这个 threshold 如何设定？

**Q6.** Table 2 中 K≥3 consensus 在 α=0.75 的 TPR 为 37.5%，低于 α=0.50 的 66.7%——这是不是意味着 consensus voting 在 detection zone 中反而不如 onset 区域可靠？能否解释这个 non-monotonicity？

---

## 5. Missing References

通过 web search 验证，以下几项工作可能与本文高度相关但未被引用：

**MR1. Carvalhais et al. (EMNLP 2025)** "Recursive Training Loops in LLMs: How Training Data Properties Modulate Distribution Shift in Generated Data" (arXiv:2504.03814)
- 这篇 EMNLP 2025 论文直接研究了 recursive training 中 data properties 如何调节 distribution shift，发现 lexical diversity 放大 shift 而 semantic diversity 缓解 shift。与本文的 entropy/diversity canary 高度相关，应在 Section 2.1 讨论。

**MR2. Buffa & Del Corro (2026)** "Entropy Sentinel: Continuous LLM Accuracy Monitoring from Decoding Entropy Traces in STEM" (arXiv:2601.09001)
- 这篇 2026 年 1 月的工作同样使用 output entropy 来持续监控 LLM 性能，使用 lightweight classifier 预测 instance correctness。虽然场景不完全相同（monitoring vs. collapse detection），但方法论上有直接关联——都基于 entropy 作为 canary signal。应至少在 Related Work Section 2.2 中提及。

**MR3.** 可能遗漏的 Granger causality 在 NLP/ML 中的应用：
- **LLM-GC (WSDM 2026)**: "LLM-GC: Advancing Granger Causal Discovery from Time Series with Multimodal Language Modeling"——将 LLMs 与 Granger causality 结合用于 causal discovery，是该交叉领域的最新工作。虽然技术路线不同，但在 Section 2.3 中提及可增强 related work 的完整性。

**MR4.** "Rate of Model Collapse in Recursive Training" (arXiv:2412.17646, 2024) ——给出了 recursive training 下 model collapse rate 的理论分析，可能与本文的 detection boundary 参数化互补。

**现有引用覆盖评价**：论文对 model collapse 核心文献（Shumailov 2024, Dohmatob 2024/2025, Kazdan 2025, Schaeffer 2025）和 Granger causality 方法论（Granger 1969, Shojaie & Fox 2022, Tank et al. 2021）的引用是充分的。遗漏主要集中在 2025-2026 年的最新 detection/monitoring 工作。

---

## 6. Overall Assessment

### 官方维度打分（ACL ARR Review Form, Feb 2025+）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验设计严谨，统计控制充分（null control, FDR, 置换检验）；但 FPR CI [1.8%, 16.2%] 意味着实际 FPR 可能显著高于 nominal 5%；3-seed 设计限制了方差估计（2 自由度）；phase transition claim 未充分排除 power curve 的 trivial 解释 |
| **Excitement** | 2.5/5 | 方法敏感性发现（6.7%–94.4% FPR spread）有警示价值，但核心方法是成熟工具的直接应用；phase transition framing 有 overclaiming 嫌疑；blind zone 严重限制实用性；以 2026 标准衡量，Pythia-410M 实验的 practical relevance 有限 |
| **Reproducibility** | 4/5 | 详细的实验设置描述（Appendix A），代码和数据承诺 release（Section 35, "generation scripts are included in the code release"），统计方法完整描述，但部分 cross-architecture 实验的 hyperparameter 细节分散在 appendix 多处 |

### Overall Assessment

**Overall**: **3.0 — Findings**

**一句话总结**: 这是一篇方法论严谨的实证研究，核心发现（方法敏感性、检测景观映射）对 model collapse 检测领域有参考价值，但方法论新颖性有限（成熟工具的应用），phase transition 的 framing 有 overclaiming 嫌疑，且 blind zone 根本性地限制了框架的实际部署价值，整体贡献更适合 Findings 而非主会议。

**置信度**: 4/5 — 对 Granger causality 方法论和 model collapse 文献有较好的了解；对统计检验和多重比较方法比较熟悉；仔细阅读了全部 36 页（含 appendix）。

---

### 关键判断依据

1. **定位 Findings 而非 Conference 的主要原因**：Contribution 1（phase transition）可能只是 statistical power 的自然行为；Contribution 2（detectability landscape）是有价值的 empirical mapping 但方法论贡献有限；Contribution 3（MMCT）是简单的 weighted voting，在当前设置下比 standalone PermG 改进不大；Contribution 4（intervention）是 proof-of-concept，仅在 α=1.0 下验证。

2. **可能提升至 3.5 (Borderline Conference) 的条件**：(a) 在至少 1 个其他架构上验证完整 phase diagram；(b) 重新定位 framing，将核心贡献明确为"方法敏感性的系统性发现"而非"phase transition discovery"；(c) 解决 page limit 问题。

3. **不建议降至 2.5 的原因**：实验质量高、统计控制严格、self-awareness 良好——这些特质使论文即使在 novelty 有限的情况下仍有发表价值。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1516 · 2026-05-25T08:29:06.847377+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 139

## Round 139

2 recorded events


### User

_source line 1517 · 2026-05-25T08:29:21.758755+00:00_

[Reviewer 2 审稿结果]:
审稿完成。已向 Review Director 提交完整审稿报告，核心结论：

- **Overall: 3.0 (Findings)**
- **Soundness 3.5/5, Excitement 2.5/5, Reproducibility 4/5**

主要问题：
1. **Phase transition framing overclaiming** — 可能只是统计功效的自然行为，非真正的物理相变
2. **方法论新颖性有限** — Granger causality + 置换检验是成熟工具的直接应用，MMCT 是简单的 weighted voting
3. **Blind zone (α<0.50) 根本性限制实用性** — distinct-1 已降 40% 但完全不可检测
4. **Cross-architecture 验证仅在 α=1.0** — phase diagram 的 generalizability 未验证
5. **Design Principles 更像 Propositions** — entropy 先于 diversity 响应可能只是 measurement resolution asymmetry
6. **正文略超 8 页** — Conclusion 溢出约 8-10 行到第 9 页

主要优势：方法敏感性发现（FPR 6.7%–94.4%）有重要警示价值，实验设计严谨，limitations 讨论坦诚。建议 4 项可能遗漏的文献（Carvalhais EMNLP 2025, Entropy Sentinel 2026, LLM-GC WSDM 2026, Rate of Model Collapse 2024）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1518 · 2026-05-25T08:29:30.710650+00:00_

Reviewer 2 审稿报告已收到（Overall: 3.0 Findings）。等待 Reviewer 1 的报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 140

## Round 140

6 recorded events


### User

_source line 1519 · 2026-05-25T08:29:35.510457+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 审稿报告：Characterizing the Detectability Landscape of Iterative Model Collapse

**审查侧重**：方法严谨性 + 实验有效性

---

## 1. Summary

本文系统比较五种时间序列统计方法，检测分布型 canary 指标（token entropy, distinct-n）对下游质量指标（perplexity）的因果先导关系，以此刻画迭代 model collapse 的可检测性。核心发现是一个尖锐的检测相变：Permutation Granger causality (PermG) 的检测率在 contamination fraction α_c ≈ 0.50 的 2 个百分点区间内从 0/8 跳至 6/8。论文在多个 contamination 水平、观测窗口和五个模型族上映射了这一检测景观，并提出 MMCT（Multi-Method Consensus Test）作为组合诊断框架。

---

## 2. Strengths

- **S1: 定义清晰且实际意义强的研究问题。** Model collapse 是日益重要的问题，理解"何时可检测"对部署监控有直接实践价值。

- **S2: 严格的多方法对比。** 对比 5 种方法（NaiveXCor、DiffXCor、Threshold onset、PermG、Toda-Yamamoto）并做 null-control FPR 校准，揭示方法选择对结论有戏剧性影响（FPR 从 6.7% 到 94.4%）。这本身就是一个有意义的发现（Section 3.3, Figure 2）。

- **S3: 相变识别。** α_c ≈ 0.50 的尖锐 0/8→6/8 跳变是新颖的发现，Figure 1 的三区域划分（blind/onset/detection）给出了可操作的实践指导。

- **S4: Cascade ordering 结果。** Entropy 领先 diversity collapse（24/24 forward, 0/24 reverse at α=1.0），first-differencing 消除 canary→perplexity 但保留 canary→diversity（Section 5），提供了机制层面的洞察。

- **S5: 极为详尽的附录（27 页）。** 覆盖 robustness analysis（Appendix D）、cross-architecture validation（Appendix Z）、Shapley decomposition（Appendix P）、specification curve（Appendix D, Figure 6）、partial correlations（Appendix V）、AR(1) analysis（Appendix E）等，展现了严肃的科学态度。

- **S6: Intervention proof-of-concept。** Canary-triggered intervention 实现 64% perplexity 降低（Section 4.6, Figure 9），将检测框架落地为实际干预能力。

- **S7: 可复现性。** 详细超参（Appendix A）、明确随机种子、接收后代码发布承诺。

---

## 3. Weaknesses

### **W1 [critical] Phase diagram 仅基于 3 seeds（2 自由度），方差估计不可靠**

- **具体位置**：Section 4.1, Figure 1, Figure 3
- **问题**：Phase diagram 是论文的核心图表（Figure 1），但仅用 3 seeds 构建。2 个自由度下，区域边界的 variance 估计极不可靠。虽然 Appendix K 对 FPR 分析使用了 10 seeds（60 pairs），但决定 regime 边界的 α×T 网格仅用 3 seeds。
- **为什么影响接收**：检测边界 α_c ≈ 0.50 和三区域分类可能随 seed 增加而显著偏移。论文的核心 claim 建立在统计不稳定的基础上。
- **建议**：至少使用 10 seeds 重新构建 phase diagram，或在主文中提供 α_c 的 bootstrap 置信区间。

### **W2 [critical] 6/8 检测率的置信区间 [0.25, 0.92] 过宽，不足以支撑 "sharp transition" 的表述**

- **具体位置**：Abstract, Section 1, Section 3.4, Section 6
- **问题**：论文多处使用 "sharp detection phase transition" 来描述 0/8→6/8 的跳变。但 6/8 的 Clopper-Pearson 95% CI 为 [0.25, 0.92]，即真实检测概率可能低至 25%。此外，Appendix S 的 sigmoid 拟合报告 steepness k = 478 ± 473（SE ≈ k），即 sharpness 参数有 ~100% 的相对不确定性。"Sharp" 的措辞超出了统计证据所能支撑的范围。
- **为什么影响接收**：核心 claim 的置信度不足。如果 reviewer 质疑 "sharp"，整篇论文的叙事框架动摇。
- **建议**：(1) 增加 seed 数量以缩窄 CI；(2) 或将措辞改为 "apparent transition" 并在主文中显式报告不确定性。

### **W3 [major] Cross-architecture validation 仅在 α=1.0（最易检测条件）进行**

- **具体位置**：Section 4.5, Figure 8, Table 37 (Appendix Z)
- **问题**：五个模型族的评估仅在 full replacement（α=1.0）进行。这是最容易检测的条件。论文的核心发现——α_c ≈ 0.50 的相变——在 GPT-2、Qwen、SmolLM 上未经验证。仅 Pythia-1.4B 有附录中的 phase diagram 复现（Figure 13），且显示 α_c ≈ 0.50 一致，但其他三个架构完全缺失。
- **为什么影响接收**：Phase diagram 可能是 Pythia-410M 特有的。如果不同架构有不同的相变点，论文的泛化性 claim（Section 4.5 标题 "Cross-Architecture Evaluation"）名不副实。
- **建议**：至少在 GPT-2-medium 上补做 α ∈ {0.25, 0.50, 0.75} 的检测实验，验证相变结构的一致性。

### **W4 [major] 单一数据集（WikiText-103），domain 泛化性证据极弱**

- **具体位置**：Section 4.1 (实验设置), Limitations (p9)
- **问题**：所有主实验使用 WikiText-103。Domain 泛化性仅有 Appendix J 中一句话提及："Pythia-1.4B on C4 yields 8/8 PermG forward detection"。不同 domain 的词汇分布、主题多样性、序列长度特征可能实质性地影响检测景观。对于声称映射 "detectability landscape" 的论文，单一 domain 是显著短板。
- **建议**：在 C4 或 OpenWebText 上复现核心实验（至少 phase diagram），或显式缩窄 claim 范围。

### **W5 [major] MMCT 设计问题：K≥3 null-control FPR = 10%，NaiveXCor 的 94.4% FPR 污染共识**

- **具体位置**：Algorithm 1, Table 2, Section 3.3
- **问题**：
  (a) K≥3 consensus 在 null 条件下 FPR = 10.0%（Table 2），是名义 5% 水平的两倍。
  (b) NaiveXCor 的 94.4% FPR 意味着它在几乎所有条件下都会 "报警"，实际不提供有用的判别信息。但在 K 计数中它贡献 1 分，使得 K≥3 实际只需要剩余 4 种方法中的 2 种同意。
  (c) FPR-inverse weighting（Algorithm 1）给 NaiveXCor 权重 w ≈ 1.06（vs. PermG 的 w ≈ 14.9），但加权 W 和计数 K 传递矛盾信号。
  (d) Empirical null calibration 仅基于 60 null pairs（10 seeds × 6 pairs），null 分布估计粗糙。
- **建议**：排除 FPR > 50% 的方法（NaiveXCor），或提供排除后的 MMCT 结果作为 robustness check。

### **W6 [moderate] Intervention 实验仅在 α=1.0，未验证实际最有价值的中等污染场景**

- **具体位置**：Section 4.6, Figure 9
- **问题**：α=1.0 是最严重的 collapse 条件，此时不需要精细检测即可观察到退化。Detection framework 的实际价值在 blind zone 边界附近（α ≈ 0.45–0.55），但该区域的干预效果未知。
- **建议**：补充 α ∈ {0.50, 0.60} 的 intervention 实验。

### **W7 [moderate] α=0.60 non-monotonic anomaly 的解释缺乏直接证据**

- **具体位置**：Section 3.4, Appendix I/J
- **问题**："Temporal lag compression" 解释合理但间接。证据来自 AR(1) 系数和 cross-T 分析，但没有直接测量 entropy-diversity lag 结构随 α 的变化（如实证 cross-correlation function）。Appendix J 讨论了三种替代解释但未能决定性区分。
- **建议**：在 Appendix 中增加实证 cross-correlation function 图（entropy vs. diversity at lag 0, 1, 2 across α levels），直接展示 lag 压缩。

### **W8 [minor] 格式问题：主文（Sections 1–6 Conclusion）似乎延伸到第 9 页**

- **具体位置**：PDF pages 8–9
- **问题**：Conclusion 文本从第 8 页延续到第 9 页（Limitations 标题之前有约 15–20 行结论文本）。EMNLP 2026 规定正文 ≤ 8 页（Limitations 不计入）。如果确认，需要压缩。

### **W9 [minor] Abstract 可能超过 200 词**

- **具体位置**：Page 1 Abstract
- **问题**：Abstract 跨两栏，文本密度高，目测接近或略超 200 词限制。建议作者精确验证。

---

## 4. Questions for Authors

**Q1.** α_c ≈ 0.50 边界对 seed 数量有多敏感？如果在完整 α×T 网格上使用 10 seeds 而非 3 seeds，边界估计是否会变化？能否提供 α_c 的 bootstrap 置信区间？

**Q2.** 对于 K≥3 consensus（Table 2），*校准后* 的 MMCT（使用加权 W 统计量和 empirical null，而非原始计数 K≥3）的实际 FPR 是多少？论文报告了 K-threshold FPR 但未清晰区分这与完整 MMCT 程序的 FPR。

**Q3.** First-differencing 消除 canary→perplexity 但保留 canary→diversity（Section 5）。为什么 first-differencing 会消除一个因果关系但不消除另一个？两个指标都响应同一底层分布偏移。论文解释是 perplexity 为 "channel-specific rather than global"——能否更严格地定义这一区别？

**Q4.** 在 α=0.60，non-monotonic anomaly 被解释为 "temporal lag compression"。能否提供直接证据——例如实证 cross-correlation function 显示 entropy-diversity lag 在 α=0.60 相比 α=0.50 和 α=0.75 有所减小？

**Q5.** Intervention 在 generation 1 基于 canary signal 触发。实践中监控系统不知道 α 的值。如何确定触发阈值？是否有一个跨 α 水平有效的校准阈值？

**Q6.** 是否考虑过在分布特征根本不同的 domain（如代码、对话、科学文本）上评估？WikiText-103 的百科式文本可能有特定的分布特征有利于你们的检测方法。

---

## 5. Missing References

- **Rabanser et al. (2019)**, "Failing Loudly: An Empirical Study of Methods for Detecting Dataset Shift" — 本文本质上是检测分布偏移，但未连接到更广泛的 dataset shift detection 文献。

- **Hataya et al. (2023)**, "Will Large-scale Generative Models Corrupt Future Datasets?" — 早期迭代合成数据训练工作，早于多个被引参考文献。

---

## 6. Overall Assessment

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 方法论框架合理（PermG + BH-FDR + first-differencing），但核心 claims 建立在有限样本上（3 seeds phase diagram, 6/8 with CI [0.25,0.92]），MMCT null FPR 偏高 |
| **Excitement** | 3.0/5 | 研究问题及时且实用，相变发现新颖，但单一 dataset + 单一架构（主实验）限制了影响力 |
| **Reproducibility** | 4.0/5 | 详细超参（Appendix A）、明确种子、代码承诺；扣分因 3-seed phase diagram 难以精确复现边界 |
| **Confidence** | 4/5 | 仔细阅读全文（36 页），熟悉时间序列因果检验和 model collapse 文献 |

**Overall**: **3.0 — Findings**

**一句话总结**: 论文提出了一个有创意的多方法框架来刻画 model collapse 的可检测性景观，识别出新颖的相变现象，但核心 claims 的证据基础（3 seeds、宽 CI、单一 dataset、仅 α=1.0 的跨架构验证）对于 "sharp transition" 和 "landscape" 的表述而言过薄，适合 Findings 接收但需补强以达到主会议水准。

**升至 Conference (3.5–4.0) 的路径**：(1) Phase diagram 增至 ≥10 seeds 并报告 α_c 的 CI；(2) 至少一个非 Pythia 架构的 intermediate-α 验证；(3) 第二 domain 的核心实验复现；(4) 修正 "sharp transition" 措辞以匹配统计证据强度。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1520 · 2026-05-25T08:30:34.562486+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Weakness，请标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。对 Strengths 和 Questions 也可选择性回应。\n\n---\n\n# Reviewer 1 审稿报告\n\n## 2. Strengths\n\n- **S1: 定义清晰且实际意义强的研究问题。** Model collapse 是日益重要的问题，理解\"何时可检测\"对部署监控有直接实践价值。\n\n- **S2: 严格的多方法对比。** 对比 5 种方法（NaiveXCor、DiffXCor、Threshold onset、PermG、Toda-Yamamoto）并做 null-control FPR 校准，揭示方法选择对结论有戏剧性影响（FPR 从 6.7% 到 94.4%）。这本身就是一个有意义的发现（Section 3.3, Figure 2）。\n\n- **S3: 相变识别。** α_c ≈ 0.50 的尖锐 0/8→6/8 跳变是新颖的发现，Figure 1 的三区域划分（blind/onset/detection）给出了可操作的实践指导。\n\n- **S4: Cascade ordering 结果。** Entropy 领先 diversity collapse（24/24 forward, 0/24 reverse at α=1.0），first-differencing 消除 canary→perplexity 但保留 canary→diversity（Section 5），提供了机制层面的洞察。\n\n- **S5: 极为详尽的附录（27 页）。** 覆盖 robustness analysis（Appendix D）、cross-architecture validation（Appendix Z）、Shapley decomposition（Appendix P）、specification curve（Appendix D, Figure 6）、partial correlations（Appendix V）、AR(1) analysis（Appendix E）等，展现了严肃的科学态度。\n\n- **S6: Intervention proof-of-concept。** Canary-triggered intervention 实现 64% perplexity 降低（Section 4.6, Figure 9），将检测框架落地为实际干预能力。\n\n- **S7: 可复现性。** 详细超参（Appendix A）、明确随机种子、接收后代码发布承诺。\n\n## 3. Weaknesses\n\n### **W1 [critical] Phase diagram 仅基于 3 seeds（2 自由度），方差估计不可靠**\n- Phase diagram 是论文的核心图表（Figure 1），但仅用 3 seeds 构建。2 个自由度下，区域边界的 variance 估计极不可靠。虽然 Appendix K 对 FPR 分析使用了 10 seeds（60 pairs），但决定 regime 边界的 α×T 网格仅用 3 seeds。\n- 检测边界 α_c ≈ 0.50 和三区域分类可能随 seed 增加而显著偏移。论文的核心 claim 建立在统计不稳定的基础上。\n\n### **W2 [critical] 6/8 检测率的置信区间 [0.25, 0.92] 过宽，不足以支撑 \"sharp transition\" 的表述**\n- 论文多处使用 \"sharp detection phase transition\" 来描述 0/8→6/8 的跳变。但 6/8 的 Clopper-Pearson 95% CI 为 [0.25, 0.92]，即真实检测概率可能低至 25%。此外，Appendix S 的 sigmoid 拟合报告 steepness k = 478 ± 473（SE ≈ k），即 sharpness 参数有 ~100% 的相对不确定性。\"Sharp\" 的措辞超出了统计证据所能支撑的范围。\n\n### **W3 [major] Cross-architecture validation 仅在 α=1.0（最易检测条件）进行**\n- 五个模型族的评估仅在 full replacement（α=1.0）进行。这是最容易检测的条件。论文的核心发现——α_c ≈ 0.50 的相变——在 GPT-2、Qwen、SmolLM 上未经验证。仅 Pythia-1.4B 有附录中的 phase diagram 复现（Figure 13），且显示 α_c ≈ 0.50 一致，但其他三个架构完全缺失。\n\n### **W4 [major] 单一数据集（WikiText-103），domain 泛化性证据极弱**\n- 所有主实验使用 WikiText-103。Domain 泛化性仅有 Appendix J 中一句话提及：\"Pythia-1.4B on C4 yields 8/8 PermG forward detection\"。\n\n### **W5 [major] MMCT 设计问题：K≥3 null-control FPR = 10%，NaiveXCor 的 94.4% FPR 污染共识**\n- K≥3 consensus 在 null 条件下 FPR = 10.0%（Table 2），是名义 5% 水平的两倍。\n- NaiveXCor 的 94.4% FPR 意味着它在几乎所有条件下都会 \"报警\"。\n- Empirical null calibration 仅基于 60 null pairs（10 seeds × 6 pairs），null 分布估计粗糙。\n\n### **W6 [moderate] Intervention 实验仅在 α=1.0，未验证实际最有价值的中等污染场景**\n\n### **W7 [moderate] α=0.60 non-monotonic anomaly 的解释缺乏直接证据**\n- \"Temporal lag compression\" 解释合理但间接。没有直接测量 entropy-diversity lag 结构随 α 的变化。\n\n### **W8 [minor] 格式问题：主文（Sections 1–6 Conclusion）似乎延伸到第 9 页**\n\n### **W9 [minor] Abstract 可能超过 200 词**\n\n## 4. Questions\nQ1-Q6（详见上方完整报告）\n\n## 5. Missing References\n- Rabanser et al. (2019), \"Failing Loudly\"\n- Hataya et al. (2023), \"Will Large-scale Generative Models Corrupt Future Datasets?\"\n\n## 6. Overall Assessment\n**Overall: 3.0 — Findings**"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应。对每个 Weakness，请标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。对 Strengths 和 Questions 也可选择性回应。\n\n---\n\n# Reviewer 1 审稿报告\n\n## 2. Strengths\n\n- **S1: 定义清晰且实际意义强的研究问题。** Model collapse 是日益重要的问题，理解\"何时可检测\"对部署监控有直接实践价值。\n\n- **S2: 严格的多方法对比。** 对比 5 种方法（NaiveXCor、DiffXCor、Threshold onset、PermG、Toda-Yamamoto）并做 null-control FPR 校准，揭示方法选择对结论有戏剧性影响（FPR 从 6.7% 到 94.4%）。这本身就是一个有意义的发现（Section 3.3, Figure 2）。\n\n- **S3: 相变识别。** α_c ≈ 0.50 的尖锐 0/8→6/8 跳变是新颖的发现，Figure 1 的三区域划分（blind/onset/detection）给出了可操作的实践指导。\n\n- **S4: Cascade ordering 结果。** Entropy 领先 diversity collapse（24/24 forward, 0/24 reverse at α=1.0），first-differencing 消除 canary→perplexity 但保留 canary→diversity（Section 5），提供了机制层面的洞察。\n\n- **S5: 极为详尽的附录（27 页）。** 覆盖 robustness analysis（Appendix D）、cross-architecture validation（Appendix Z）、Shapley decomposition（Appendix P）、specification curve（Appendix D, Figure 6）、partial correlations（Appendix V）、AR(1) analysis（Appendix E）等，展现了严肃的科学态度。\n\n- **S6: Intervention proof-of-concept。** Canary-triggered intervention 实现 64% perplexity 降低（Section 4.6, Figure 9），将检测框架落地为实际干预能力。\n\n- **S7: 可复现性。** 详细超参（Appendix A）、明确随机种子、接收后代码发布承诺。\n\n## 3. Weaknesses\n\n### **W1 [critical] Phase diagram 仅基于 3 seeds（2 自由度），方差估计不可靠**\n- Phase diagram 是论文的核心图表（Figure 1），但仅用 3 seeds 构建。2 个自由度下，区域边界的 variance 估计极不可靠。虽然 Appendix K 对 FPR 分析使用了 10 seeds（60 pairs），但决定 regime 边界的 α×T 网格仅用 3 seeds。\n- 检测边界 α_c ≈ 0.50 和三区域分类可能随 seed 增加而显著偏移。论文的核心 claim 建立在统计不稳定的基础上。\n\n### **W2 [critical] 6/8 检测率的置信区间 [0.25, 0.92] 过宽，不足以支撑 \"sharp transition\" 的表述**\n- 论文多处使用 \"sharp detection phase transition\" 来描述 0/8→6/8 的跳变。但 6/8 的 Clopper-Pearson 95% CI 为 [0.25, 0.92]，即真实检测概率可能低至 25%。此外，Appendix S 的 sigmoid 拟合报告 steepness k = 478 ± 473（SE ≈ k），即 sharpness 参数有 ~100% 的相对不确定性。\"Sharp\" 的措辞超出了统计证据所能支撑的范围。\n\n### **W3 [major] Cross-architecture validation 仅在 α=1.0（最易检测条件）进行**\n- 五个模型族的评估仅在 full replacement（α=1.0）进行。这是最容易检测的条件。论文的核心发现——α_c ≈ 0.50 的相变——在 GPT-2、Qwen、SmolLM 上未经验证。仅 Pythia-1.4B 有附录中的 phase diagram 复现（Figure 13），且显示 α_c ≈ 0.50 一致，但其他三个架构完全缺失。\n\n### **W4 [major] 单一数据集（WikiText-103），domain 泛化性证据极弱**\n- 所有主实验使用 WikiText-103。Domain 泛化性仅有 Appendix J 中一句话提及：\"Pythia-1.4B on C4 yields 8/8 PermG forward detection\"。\n\n### **W5 [major] MMCT 设计问题：K≥3 null-control FPR = 10%，NaiveXCor 的 94.4% FPR 污染共识**\n- K≥3 consensus 在 null 条件下 FPR = 10.0%（Table 2），是名义 5% 水平的两倍。\n- NaiveXCor 的 94.4% FPR 意味着它在几乎所有条件下都会 \"报警\"。\n- Empirical null calibration 仅基于 60 null pairs（10 seeds × 6 pairs），null 分布估计粗糙。\n\n### **W6 [moderate] Intervention 实验仅在 α=1.0，未验证实际最有价值的中等污染场景**\n\n### **W7 [moderate] α=0.60 non-monotonic anomaly 的解释缺乏直接证据**\n- \"Temporal lag compression\" 解释合理但间接。没有直接测量 entropy-diversity lag 结构随 α 的变化。\n\n### **W8 [minor] 格式问题：主文（Sections 1–6 Conclusion）似乎延伸到第 9 页**\n\n### **W9 [minor] Abstract 可能超过 200 词**\n\n## 4. Questions\nQ1-Q6（详见上方完整报告）\n\n## 5. Missing References\n- Rabanser et al. (2019), \"Failing Loudly\"\n- Hataya et al. (2023), \"Will Large-scale Generative Models Corrupt Future Datasets?\"\n\n## 6. Overall Assessment\n**Overall: 3.0 — Findings**"
  }
}
```

</details>

---


### Tool result

_source line 1521 · 2026-05-25T08:31:07.828048+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33265
}
```

</details>

---


### Tool call

_source line 1522 · 2026-05-25T08:31:08.082548+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Weakness，请标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。对 Strengths 和 Questions 也可选择性回应。\n\n---\n\n# Reviewer 2 审稿报告\n\n## 2. Strengths\n\n**S1. 方法敏感性的实证发现具有重要警示意义。** 五种 lead-lag 检测方法在相同数据上产生 FPR 从 6.7% 到 94.4% 的巨大差异（κ=0.185），这个发现本身就是对该领域的重要贡献。它表明 model collapse 检测文献中，使用单一统计方法的研究结论可能不可靠。这个 finding 比 phase transition 本身更有价值。\n\n**S2. 实验设计严谨，统计控制充分。**\n\n**S3. 对 limitations 和 non-confirming cases 的讨论坦诚且详尽。**\n\n**S4. Appendix 内容充实，支撑主文 claims。** 26 页的 appendix 包含了完整的理论推导、Shapley 分解、partial correlation 分析等。\n\n**S5. 检测边界的参数化建模有参考价值。** α_c(T) = A·T^{-γ} 虽然拟合精度有限（γ 的 95% CI [0.64, 2.08] 很宽），但提供了定量框架。\n\n## 3. Weaknesses\n\n### **W1 [major] \"检测相变\"的新颖性存疑——可能只是统计功效的自然行为。**\n- 任何统计检验在信号强度跨过检测阈值时都会从不显著跳到显著，这是统计功效（power）的基本性质。论文声称 sigmoid Hill coefficient k=15.7 比 smooth-signal predictions 陡峭 3-4x，但比较 baseline 是论文自己构建的 power simulation。论文未排除实验设计本身（full replacement, 离散 α 取值, T=10）对 transition steepness 的贡献。\n- 如果 phase transition 只是 power curve 在有限样本下的自然表现，那么 Contribution 1 的新颖性大幅降低。\n\n### **W2 [major] 核心方法论的新颖性有限——Granger causality + 置换检验是成熟工具的直接应用。**\n- PermG 是计量经济学的标准工具，first-differencing 去趋势也是标准做法，BH-FDR 校正是通用方法。MMCT 本质上是一个 FPR-inverse weighted voting scheme，算法本身技术贡献有限。论文贡献更多在于\"将这些工具应用到 model collapse 检测场景\"。\n\n### **W3 [major] Blind zone 根本性地限制了框架的实用价值。**\n- α < 0.50 时，distinct-1 已下降 ~40%，但 Granger 检测完全失效（0/8）。论文在 Limitations 定位为 \"confirmation tool\"，但 abstract 和 introduction 叙事暗示有实用的检测框架。\n- 如果框架只能在 contamination >50% 时才能检测，实际部署场景非常有限。\n\n### **W4 [major] Cross-architecture 验证仅在 α=1.0 下进行，限制了 generalizability claims。**\n\n### **W5 [major] Design Principles 1-2 的新颖性和标签存疑。**\n- Design Principle 1 说 \"entropy responds before diversity\"——这几乎是 trivially true：entropy 是连续量，distinct-n 是离散量。论文自己在 Discussion 中也承认了 measurement resolution asymmetry。\"Design Principle\" 标签有过度包装之嫌。\n\n### **W6 [minor] 正文可能略超 8 页限制。**\n\n### **W7 [minor] Intervention 实验仅在 α=1.0 下进行，但叙事中被提升为重要贡献。**\n\n### **W8 [minor] 术语使用不完全一致。** \"Granger causality\"、\"Granger precedence\"、\"temporal predictive improvement\" 三个术语交替使用。\n\n## 4. Questions\nQ1-Q6（详见上方完整报告）\n\n## 5. Missing References\n- Carvalhais et al. (EMNLP 2025) \"Recursive Training Loops in LLMs\"\n- Buffa & Del Corro (2026) \"Entropy Sentinel\"\n- LLM-GC (WSDM 2026) Granger causal discovery\n- \"Rate of Model Collapse in Recursive Training\" (arXiv:2412.17646, 2024)\n\n## 6. Overall Assessment\n**Overall: 3.0 — Findings**"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应。对每个 Weakness，请标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。对 Strengths 和 Questions 也可选择性回应。\n\n---\n\n# Reviewer 2 审稿报告\n\n## 2. Strengths\n\n**S1. 方法敏感性的实证发现具有重要警示意义。** 五种 lead-lag 检测方法在相同数据上产生 FPR 从 6.7% 到 94.4% 的巨大差异（κ=0.185），这个发现本身就是对该领域的重要贡献。它表明 model collapse 检测文献中，使用单一统计方法的研究结论可能不可靠。这个 finding 比 phase transition 本身更有价值。\n\n**S2. 实验设计严谨，统计控制充分。**\n\n**S3. 对 limitations 和 non-confirming cases 的讨论坦诚且详尽。**\n\n**S4. Appendix 内容充实，支撑主文 claims。** 26 页的 appendix 包含了完整的理论推导、Shapley 分解、partial correlation 分析等。\n\n**S5. 检测边界的参数化建模有参考价值。** α_c(T) = A·T^{-γ} 虽然拟合精度有限（γ 的 95% CI [0.64, 2.08] 很宽），但提供了定量框架。\n\n## 3. Weaknesses\n\n### **W1 [major] \"检测相变\"的新颖性存疑——可能只是统计功效的自然行为。**\n- 任何统计检验在信号强度跨过检测阈值时都会从不显著跳到显著，这是统计功效（power）的基本性质。论文声称 sigmoid Hill coefficient k=15.7 比 smooth-signal predictions 陡峭 3-4x，但比较 baseline 是论文自己构建的 power simulation。论文未排除实验设计本身（full replacement, 离散 α 取值, T=10）对 transition steepness 的贡献。\n- 如果 phase transition 只是 power curve 在有限样本下的自然表现，那么 Contribution 1 的新颖性大幅降低。\n\n### **W2 [major] 核心方法论的新颖性有限——Granger causality + 置换检验是成熟工具的直接应用。**\n- PermG 是计量经济学的标准工具，first-differencing 去趋势也是标准做法，BH-FDR 校正是通用方法。MMCT 本质上是一个 FPR-inverse weighted voting scheme，算法本身技术贡献有限。论文贡献更多在于\"将这些工具应用到 model collapse 检测场景\"。\n\n### **W3 [major] Blind zone 根本性地限制了框架的实用价值。**\n- α < 0.50 时，distinct-1 已下降 ~40%，但 Granger 检测完全失效（0/8）。论文在 Limitations 定位为 \"confirmation tool\"，但 abstract 和 introduction 叙事暗示有实用的检测框架。\n- 如果框架只能在 contamination >50% 时才能检测，实际部署场景非常有限。\n\n### **W4 [major] Cross-architecture 验证仅在 α=1.0 下进行，限制了 generalizability claims。**\n\n### **W5 [major] Design Principles 1-2 的新颖性和标签存疑。**\n- Design Principle 1 说 \"entropy responds before diversity\"——这几乎是 trivially true：entropy 是连续量，distinct-n 是离散量。论文自己在 Discussion 中也承认了 measurement resolution asymmetry。\"Design Principle\" 标签有过度包装之嫌。\n\n### **W6 [minor] 正文可能略超 8 页限制。**\n\n### **W7 [minor] Intervention 实验仅在 α=1.0 下进行，但叙事中被提升为重要贡献。**\n\n### **W8 [minor] 术语使用不完全一致。** \"Granger causality\"、\"Granger precedence\"、\"temporal predictive improvement\" 三个术语交替使用。\n\n## 4. Questions\nQ1-Q6（详见上方完整报告）\n\n## 5. Missing References\n- Carvalhais et al. (EMNLP 2025) \"Recursive Training Loops in LLMs\"\n- Buffa & Del Corro (2026) \"Entropy Sentinel\"\n- LLM-GC (WSDM 2026) Granger causal discovery\n- \"Rate of Model Collapse in Recursive Training\" (arXiv:2412.17646, 2024)\n\n## 6. Overall Assessment\n**Overall: 3.0 — Findings**"
  }
}
```

</details>

---


### Tool result

_source line 1523 · 2026-05-25T08:31:11.690162+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3607
}
```

</details>

---


### Assistant

_source line 1524 · 2026-05-25T08:31:16.304730+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 141

## Round 141

2 recorded events


### User

_source line 1525 · 2026-05-25T08:31:19.156274+00:00_

[Reviewer 1 审稿结果]:
审稿完成。核心评判：

- **Overall: 3.0 (Findings)**，Soundness 3.5，Excitement 3.0
- **2 个 critical 问题**：Phase diagram 仅 3 seeds（方差不可靠）；6/8 detection rate 的 CI [0.25, 0.92] 过宽，不支撑 "sharp transition" 措辞
- **3 个 major 问题**：Cross-architecture 仅在 α=1.0 验证；单一 dataset（WikiText-103）；MMCT 的 K≥3 null FPR=10%（NaiveXCor 94.4% FPR 污染共识）
- **升级路径**：增加 seeds、补做 intermediate-α 跨架构实验、第二 domain 复现、修正 claim 强度

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1526 · 2026-05-25T08:31:26.401182+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 142

## Round 142

2 recorded events


### User

_source line 1527 · 2026-05-25T08:32:59.961714+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Strengths 回应

**S1-S7**: 整体同意 R1 对优势的评价。补充两点：

- 关于 **S3（相变识别）**：R1 将其列为 Strength，但我在自己的审稿中将其列为主要 weakness（W1）。我的理由是 0/8→6/8 的跳变可能只是 statistical power 在有限样本下的自然行为，而非真正的物理相变。R1 在 W2 中也对 "sharp" 的表述提出质疑，两者有张力——建议 R1 考虑是否应将 S3 降级或加限定条件。

- 关于 **S6（Intervention）**：R1 将其列为 Strength，但也在 W6 中指出仅在 α=1.0 验证。我同意这两面评价——作为 proof-of-concept 有展示价值，但不应被提升为核心贡献。

---

### Weaknesses 逐条回应

**[AGREE] R1-W1: Phase diagram 仅基于 3 seeds**
- 同意这是 critical issue。我在自己的审稿中也指出了相同问题（R2-Soundness 评分理由："3-seed 设计限制了方差估计，2 自由度"）。
- 补充：论文 Limitations 中也承认了这一点（"The 3-seed phase diagram limits variance estimation (2 degrees of freedom); the detection boundary CI should be interpreted with this constraint"），但 Limitations 中的 self-acknowledgment 不能替代实际增加 seeds 来解决问题。
- **与我的评估一致**：这是导致我给 Soundness 3.5/5 而非 4/5 的原因之一。

**[AGREE with nuance] R1-W2: 6/8 CI [0.25, 0.92] 过宽，"sharp" overclaimed**
- 同意单个条件下 6/8 的 CI 很宽（[0.25, 0.92]）。
- 但需补充上下文：论文的 "sharp transition" claim 不仅基于单个条件的 6/8，还依赖三条补充证据：(1) **cross-seed consistency**——3 个 fp32 seeds 都独立产生 0/8→6/8 跳变（Section 4.2）；(2) **specification curve**——1,160 个配置中 blind→onset 跳变一致（Figure 6, Appendix D）；(3) **Fisher exact test** p = 3.45×10⁻¹¹（Section 4.2）。
- 关于 R1 引用的 Appendix S sigmoid 拟合 k=478±473（SE≈k）：如果 R1 引用准确，这与主文 Section 4.3 的 k=15.7 存在显著数值差异。两者可能来自不同的参数化或拟合目标，但论文应在正文中解释这一差异。**这一点我的原始审稿未覆盖，感谢 R1 发现。**
- **总结**：同意 "sharp" 的措辞应被弱化（例如改为 "steep" 或 "abrupt"），但不认为单条件 CI 宽度足以否定 transition 本身的存在。

**[AGREE] R1-W3: Cross-architecture validation 仅在 α=1.0**
- 完全同意。这与我的 R2-W4 一致。补充：Pythia-1.4B 在 Appendix 中有部分 phase diagram 复现（论文提到 "Pythia-1.4B qualitatively reproduces the 410M phase-diagram structure"，Section 4.5），但其他三个架构（GPT-2, Qwen, SmolLM3）完全缺失。
- 这是我建议论文 "可能提升至 3.5 Borderline Conference 的条件" 之一：至少在 1 个其他架构上验证完整 phase diagram。

**[AGREE] R1-W4: 单一数据集 WikiText-103**
- 同意。我的原始审稿对此关注不够。论文仅在 Appendix 中提及 C4 上 Pythia-1.4B 的 8/8 PermG detection（一句话），这远不足以支撑 domain generalizability。
- 不过，model collapse 文献中的大多数工作也使用单一数据集（Shumailov et al. 2024 用 WikiText，Dohmatob et al. 2025 用合成分布），所以这个问题是领域性的，不完全是本文特有的缺陷。

**[AGREE with nuance] R1-W5: MMCT K≥3 FPR=10% 和 NaiveXCor 污染**
- 部分同意。需要区分两个不同的方案：
  - **MMCT proper**（Algorithm 1）：使用 FPR-inverse weighting，NaiveXCor 权重仅 1.06（vs. PermG 14.9），因此 NaiveXCor 对加权共识的影响被大幅压制。
  - **K≥3 majority voting**：equal-weight，此时 NaiveXCor（几乎必 reject）确实"污染"了共识，导致 FPR=10%。
- R1 的批评对 K≥3 scheme 完全成立，但对 weighted MMCT 的批评需要弱化。论文的问题在于 Table 2 报告的是 K≥3 scheme 的结果，而 Algorithm 1 描述的是 weighted scheme——两者的混淆是写作问题。
- 关于 60 null pairs 不够的问题，同意——bootstrap CI（Appendix Figure 19）在这个样本量下可能不够稳定。

**[AGREE] R1-W6: Intervention 仅在 α=1.0**
- 与我的 R2-W7 一致。

**[AGREE] R1-W7: α=0.60 anomaly 解释缺直接证据**
- 与我的 R2-Q4 一致。论文提供了间接解释（temporal lag compression + T=25 时恢复与 √T power scaling 一致），但没有直接测量 entropy-diversity lag 随 α 的变化曲线。一个简单的附加分析——绘制 cross-correlation peak lag vs. α 的图——就能大幅加强这个解释。

**[REBUT] R1-W8: 主文延伸到第 9 页**
- 我在 R2-W6 中也提到了这个问题（标为 minor），但需要注意：从 PDF 渲染看，Section 6 (Conclusion) 约 8-10 行文本溢出到第 9 页。这是一个格式问题但**不是 critical**——压缩 Discussion 或 Conclusion 几句话即可解决。R1 也将此标为 minor，分级合理。

**[REBUT] R1-W9: Abstract 可能超过 200 词**
- 我仔细计算了 abstract 词数，约 **158-160 词**（即使将 hyphenated compounds 如 "proof-of-concept" 算作 3 个词，也在 170-180 词范围内）。Abstract 符合 EMNLP 2026 的 200 词限制。R1 应提供具体的词数计算来支持此 claim。

---

### Missing References 回应

**Rabanser et al. (2019), "Failing Loudly"**
- 部分同意。这篇论文关于 distribution shift detection 的 general framework，与本文的 detection methodology 有间接关联。但它处理的是通用的 distribution shift（不是 iterative model collapse），且方法（MMD, classifier-based tests）与本文的 time-series approach 不同。可以在 Related Work Section 2.3 中简要提及，但不是关键遗漏。

**Hataya et al. (2023), "Will Large-scale Generative Models Corrupt Future Datasets?"**
- 同意应该引用。这篇工作直接讨论了 generative models 对未来训练数据的污染，与本文的 synthetic contamination 场景高度相关。

**补充我在 R2 中建议的遗漏引用**：
- Carvalhais et al. (EMNLP 2025), "Recursive Training Loops in LLMs" — 直接研究 recursive training 中 data properties 对 distribution shift 的调节
- Buffa & Del Corro (2026), "Entropy Sentinel" — 同样使用 entropy 做持续 LLM 监控

---

### Overall Assessment 回应

R1 给出 **3.0 Findings**，与我的评分一致。

**共识点**：
1. 方法论新颖性有限（成熟工具的应用）
2. Cross-architecture 验证不足
3. Blind zone 限制实用性
4. 实验设计严谨，统计控制充分
5. 方法敏感性发现本身有价值

**分歧点**：
- R1 将 "phase transition" 同时列为 Strength（S3）和通过 W2 质疑其 claim——建议统一立场。我认为 transition 的存在是可信的（基于 cross-seed consistency 和 specification curve），但 "sharp" 的表述应被弱化。
- R1 对 Abstract 词数的 W9 似乎基于错误判断。

**综合建议**：两位 Reviewer 一致认为 3.0 Findings 是合适的评级。论文需要：(1) 扩大 seed 数量或降低 claims 的确定性语气；(2) 至少在 1 个非 Pythia 架构上跑完整 α grid；(3) 将 framing 从 "phase transition discovery" 重新定位为 "empirical characterization of detection limits"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1528 · 2026-05-25T08:33:16.940758+00:00_

收到 Reviewer 2 的交叉回应。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 143

## Round 143

2 recorded events


### User

_source line 1529 · 2026-05-25T08:33:19.599546+00:00_

[Reviewer 2 审稿结果]:
对 Reviewer 1 的 9 条 Weakness 逐条回应已提交。总结：

- **6 条 AGREE**（W1 seeds 不足, W3 cross-arch 仅 α=1.0, W4 单数据集, W6 intervention 限制, W7 anomaly 证据不足, W8 格式）
- **1 条 AGREE with nuance**（W2 sharp transition overclaimed——但 cross-seed 和 spec-curve 提供了部分支撑；W5 MMCT FPR——需区分 weighted MMCT 和 K≥3 scheme）
- **1 条 REBUT**（W9 abstract 词数——实际约 158-160 词，在 200 词限制内）

两位 Reviewer 一致评级 **3.0 Findings**，核心共识是方法论新颖性有限、cross-architecture 验证不足、blind zone 限制实用性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1530 · 2026-05-25T08:33:24.893246+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director"
}
```

</details>

---


## Round 144

## Round 144

50 recorded events


### User

_source line 1531 · 2026-05-25T08:33:58.719366+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 对 Reviewer 2 意见的逐条回应

---

## Strengths 回应

**R2-S1**（方法敏感性发现）: [AGREE] 同意 R2 的判断。FPR 从 6.7% 到 94.4%（κ=0.185）这个发现确实可能比 phase transition 本身更有社区价值。我在自己的审稿中也将此列为 S2 核心优势。这个结果直接表明 model collapse 检测文献中使用单一方法的研究应被谨慎对待。

**R2-S5**（参数化建模）: [AGREE] σ_c(T) = A·T^{-γ} 的框架有参考价值，但 γ 的 95% CI [0.64, 2.08] 确实很宽（我在 W2 中也提到了类似的宽 CI 问题）。

---

## Weaknesses 逐条回应

### [AGREE with nuance] R2-W1: "检测相变"可能只是统计功效的自然行为

R2 的核心论点成立：任何统计检验在信号跨越检测阈值时都会从不显著跳到显著。这是 power curve 的基本性质。

**我同意的部分：**
- 论文声称 sigmoid steepness k=15.7 比 smooth-signal predictions 陡峭 3-4x（Appendix S, page 26），但比较 baseline 是论文自己构建的 VAR(1) power simulation。这有一定循环论证的嫌疑。
- 实际数据中，α 的取值分辨率在关键区域为 5 个百分点（α=0.45 → 0/8, α=0.50 → 6/8）。论文声称的 "2 percentage-point interval" 来自 sigmoid 模型插值，而非直接观测。实际观测到的跳变区间是 [0.45, 0.50]，即 5 pp。
- Appendix S 报告的 sigmoid 拟合 steepness k = 478 ± 473（SE ≈ k），100% 相对不确定性。这严重削弱了 "sharp" 的量化声明。

**我持保留的部分：**
- 论文确实提供了 *一些* 超越标准 power 行为的证据：VAR(1) simulation 的 onset steepness ratio k_obs/k_sim = 2.6–4.2（Appendix S）。如果这些 simulation 参数化合理，transition 比 power curve 预期更陡是有实质内容的。
- Phase transition 的*定位*（α_c ≈ 0.50）和*三区域划分*即使陡度证据不完美，作为 empirical characterization 仍有价值。

**结论：** 同意 R2 的判断——如果 "phase transition" 只是有限样本下 power curve 的自然表现，Contribution 1 的新颖性确实大幅降低。论文需要更强的证据（如独立的 power simulation benchmark，或更密的 α 网格）来区分 genuine transition 和 power artifact。

---

### [AGREE] R2-W2: 核心方法论的新颖性有限

R2 正确指出 PermG、first-differencing、BH-FDR 都是成熟的标准工具，MMCT 本质是 FPR-inverse weighted voting。

**补充观点：** 这是一篇 *empirical contribution* 论文而非 *methodological contribution* 论文。对 EMNLP 而言，将成熟工具系统性地应用到新场景并产生有意义的发现是被接受的贡献形式。但 R2 的判断是准确的——方法论新颖性有限，论文的价值主要在 empirical characterization。这也是我给 Excitement 3.0/5 的原因之一。

---

### [AGREE with nuance] R2-W3: Blind zone 限制框架实用价值

**同意核心判断：** α < 0.50 时 distinct-1 已下降 ~40% 但检测完全失效（0/8），这确实严重限制了框架作为 *early warning system* 的价值。论文的 abstract 和 introduction 叙事（"can we reliably detect the onset of model collapse?"）暗示实用检测能力，但 blind zone 的存在意味着检测只在 contamination 已经很严重时才有效。

**我的保留：** 尽管如此，*刻画* blind zone 本身是有价值的——它告诉 practitioners "不要依赖这些方法做早期检测"。论文在 Limitations (p9) 中承认将框架定位为 "confirmation tool rather than early-warning system"，但这个定位应该在 abstract/introduction 中就明确，而不是在 Limitations 才出现。

---

### [AGREE] R2-W4: Cross-architecture 仅在 α=1.0

完全同意。这与我在 Round 1 审稿中的 W3 一致。仅在最易检测条件下验证，无法支撑 generalizability claim。Section 4.5 标题 "Cross-Architecture Evaluation" 在仅 α=1.0 的条件下有误导性。

---

### [AGREE with nuance] R2-W5: Design Principles 1-2 标签过度包装

**同意 "Design Principle" 标签不当：** R2 正确指出 entropy（连续量）比 distinct-n（离散量）先响应在一定程度上是 trivially expected。论文自己在 Discussion (Section 5) 承认了 "measurement resolution asymmetry"——entropy 对任何 probability mass 重新分配都连续变化，而 distinct-n 仅在 token 跨越出现/消失阈值时变化。

**我的保留：**
- Design Principle 1 的 *量化* 刻画仍有价值——不仅是 "entropy 先响应"，而是 "先 ≥ 1 generation 且在所有条件下一致"（24/24 forward, 0/24 reverse at α=1.0）。这个一致性不是 trivially 可预测的。
- Design Principle 2（σ_c(T) 的 √T scaling）确实提供了实用的部署指导。
- 但 R2 的建议合理——将 "Design Principle" 改为 "Empirical Finding" 或 "Design Guideline" 更为贴切。

---

### [AGREE] R2-W6: 正文可能略超 8 页

同意。这与我的 W8 一致。从 PDF 观察，Conclusion 文本延伸到第 9 页（Limitations 标题之前），违反 EMNLP 8 页正文限制。

---

### [AGREE] R2-W7: Intervention 仅 α=1.0

同意。这与我的 W6 一致。α=1.0 是最严重的 collapse 条件，不需要精细检测就能观察到退化。在 blind zone 边界附近（α ≈ 0.50）测试 intervention 才能展示框架的实际价值。

---

### [REBUT] R2-W8: 术语使用不一致

R2 指出 "Granger causality"、"Granger precedence"、"temporal predictive improvement" 交替使用。

**这看起来是有意的术语精确化，而非不一致。** 证据：
- Section 5 (p8) 明确写道："Our Granger-precedence claim is scoped to temporal predictive improvement (Granger, 1969; Shojaie and Fox, 2022), bivariate tests cannot exclude confounders..."
- 论文刻意避免使用 "Granger causality" 来描述自己的 claims，改用 "Granger precedence" 以避免过度的因果推断表述。"Temporal predictive improvement" 是其操作化定义。
- 这种区分在计量经济学文献中是标准做法（Granger himself 后来对 "causality" 一词表示遗憾）。

**不过：** 论文确实可以在首次出现时明确定义三个术语的关系："We use 'Granger precedence' (≡ temporal predictive improvement) to distinguish from the stronger 'Granger causality' claim..." 这会消除歧义。

---

## Missing References 回应

R2 建议的四篇参考文献：
- **Carvalhais et al. (EMNLP 2025)** "Recursive Training Loops in LLMs"
- **Buffa & Del Corro (2026)** "Entropy Sentinel"
- **LLM-GC (WSDM 2026)** Granger causal discovery
- **"Rate of Model Collapse in Recursive Training"** (arXiv:2412.17646, 2024)

**注意：** 我无法独立验证这些引用的真实性（特别是 2026 年的文献）。建议 Director 核实这些是否为真实发表的论文。如果真实存在，特别是 LLM-GC（Granger causal discovery in LLMs）和 arXiv:2412.17646 与本文直接相关，应被引用。

---

## 总结

| R2 问题 | 我的判断 | 与我 Round 1 的关系 |
|---------|---------|-------------------|
| W1 (phase transition = power?) | AGREE with nuance | 补充了我的 W2（宽 CI） |
| W2 (方法新颖性有限) | AGREE | 新观点，有效 |
| W3 (blind zone 限制实用性) | AGREE with nuance | 新观点，有效 |
| W4 (cross-arch α=1.0 only) | AGREE | = 我的 W3 |
| W5 (Design Principles 过度包装) | AGREE with nuance | 新观点，部分有效 |
| W6 (页数超限) | AGREE | = 我的 W8 |
| W7 (intervention α=1.0 only) | AGREE | = 我的 W6 |
| W8 (术语不一致) | REBUT | 论文的术语区分是有意为之 |

**R2 审稿总体评价：** R2 的审稿质量高，视角与我互补——我侧重统计严谨性的技术细节（CI 宽度、seed 数量、FPR 校准），R2 更关注 novelty 和 framing 层面的问题。W1（phase transition vs. power curve）和 W3（blind zone 的实用价值限制）是 R2 独有的重要观点，应被纳入最终评审意见。

**我维持 Overall 3.0 (Findings) 的评分。** R2 的意见强化了这个判断——论文的 empirical characterization 有价值，但 novelty 和 evidence 不足以支撑 Conference 接收。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1532 · 2026-05-25T08:34:19.680967+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1533 · 2026-05-25T08:34:20.135473+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T08:19:26.401488+00:00\", \"completed_at\": \"2026-05-25T08:23:38.324646+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 36\", \"message\": \"最后一页仅左栏顶部 3 个 bullet point（约 6 行），页面 ~85% 为空白。建议将此内容合并到前一页，或扩充 appendix 末尾内容填充空间\"}, {\"severity\": \"warning\", \"dimension\": \"page 9\", \"message\": \"主文 Conclusion 段延伸到第 9 页左栏约 15-20 行后才出现 Limitations。EMNLP 2026 正文限 8 页（limitations/references 不计入），当前主文约 8.2 页，存在超页风险。建议压缩 Discussion/Conclusion 或调整 float 位置将正文控制在 8 页内\"}, {\"severity\": \"warning\", \"dimension\": \"page 14\", \"message\": \"Appendix 页面几乎全为连续密集文本（Table 7 仅在页首，其余为跨双栏纯文字），无 figure/equation 视觉间断。审稿人扫读 appendix 时可能跳过此页。建议在 specification decomposition 或 alternative FDR thresholds 讨论处插入小型汇总图或公式\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 4 panel (b) 的 y 轴标签和 legend 字号偏小（接近正文 70% 下限），高分辨率打印可读但屏幕阅读稍吃力\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 5（cascade onset timeline）中各 method 的彩色小方块较小，灰度打印时可能难以区分不同 method。建议增加 marker shape 或文字标签辅助\"}, {\"severity\": \"info\", \"dimension\": \"page 25\", \"message\": \"Appendix 页面密度极高（Figure 18 + Figure 19 + Table 20 + Table 21 + Table 22），每个图表都偏小。虽然内容完整但阅读体验紧凑\"}, {\"severity\": \"info\", \"dimension\": \"pages 21, 30\", \"message\": \"Appendix 中的数学推导页（PermG power analysis、Cascade Ordering Theory derivations）为连续纯文本+公式，无视觉间断。理论推导例外，但若能在 Proposition/Proof 之间插入示意图会提升可读性\"}], \"counts\": {\"critical\": 1, \"warning\": 2, \"info\": 4}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 454
}
```

</details>

---


### Tool call

_source line 1534 · 2026-05-25T08:34:20.136385+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---


### Tool result

_source line 1535 · 2026-05-25T08:34:21.541868+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 1536 · 2026-05-25T08:34:21.593453+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null | head -200",
  "description": "Read current review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null | head -200",
    "description": "Read current review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1537 · 2026-05-25T08:34:21.796080+00:00_

issues:
# ============================================================
# Round 1-11 历史 resolved — 保留跨轮次记录
# ============================================================
- id: "R1-N1"
  summary: "Ground-truth pairs 定义存在循环论证"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Effect-size GT 重定义完成。"
  resolution_round: 1

- id: "R1-N2"
  summary: "FPR=0% 标定仅基于单 seed"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "α=0.0 三 seed FPR 验证完成。"
  resolution_round: 1

- id: "R1-N3"
  summary: "α=0.50 和 α=0.75 仅 1 seed"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Multi-seed 补充完成。"
  resolution_round: 1

- id: "R2-N1"
  summary: "核心方法论为计量经济学已有知识的直接迁移，新颖性有限"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Round 1 三层定位 reframe 完成。"
  resolution_round: 1

- id: "R2-N2"
  summary: "α=0.75 multi-seed 实验未完成 + Appendix A 缺失"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "完成。"
  resolution_round: 1

- id: "R2-N3"
  summary: "实验规模过窄"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "跨架构验证已扩展至 15 model-seed 组合。"
  resolution_round: 1

- id: "R1-W1"
  summary: "Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "核心修复完成。"
  resolution_round: 1

- id: "R1-W2"
  summary: "PermG 缺少 power analysis"
  category: method
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Appendix N power analysis 完成。"
  resolution_round: 1

- id: "R1-W3"
  summary: "75% spurious-signal rate headline 依赖 unde
…[truncated 2349 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 1538 · 2026-05-25T08:34:29.460075+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null | tail -n +200",
  "description": "Read remaining review issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null | tail -n +200",
    "description": "Read remaining review issues"
  }
}
```

</details>

---


### Tool result

_source line 1539 · 2026-05-25T08:34:29.561632+00:00_

&lt;persisted-output>
Output too large (33.7KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-review-director-741faaa0/15434102-6a9f-4dbc-9e4f-0e014bffe0f2/tool-results/bfjzd62w9.txt

Preview (first 2KB):
  first_raised_round: 2
  last_seen_round: 2
  resolution: "附录内容补充完成。"
  resolution_round: 3

- id: "F2-W8"
  summary: "格式不合规：未使用 ACL 模板"
  category: format
  severity: critical
  status: resolved
  first_raised_round: 2
  last_seen_round: 2
  resolution: "ACL 模板迁移完成。"
  resolution_round: 2

- id: "F2-REF1"
  summary: "遗漏 arXiv:2502.15654"
  category: reference
  severity: minor
  status: resolved
  first_raised_round: 2
  last_seen_round: 2
  resolution: "引用已添加。"
  resolution_round: 4

- id: "F3-REF1"
  summary: "遗漏 arXiv:2602.10531"
  category: reference
  severity: minor
  status: resolved
  first_raised_round: 3
  last_seen_round: 3
  resolution: "引用已添加。"
  resolution_round: 4

- id: "F3-REF2"
  summary: "遗漏 arXiv:2505.19046"
  category: reference
  severity: minor
  status: resolved
  first_raised_round: 3
  last_seen_round: 3
  resolution: "引用已添加。"
  resolution_round: 4

- id: "F3-REF3"
  summary: "遗漏 arXiv:2510.16657"
  category: reference
  severity: minor
  status: resolved
  first_raised_round: 3
  last_seen_round: 3
  resolution: "引用已添加。"
  resolution_round: 4

- id: "F3-REF5"
  summary: "Appendix H CUSUM 未引用 Page (1954)"
  category: reference
  severity: minor
  status: resolved
  first_raised_round: 3
  last_seen_round: 3
  resolution: "引用已添加。"
  resolution_round: 4

- id: "F4-REF1"
  summary: "遗漏 Truong & Truong (2026)"
  category: reference
  severity: critical
  status: resolved
  first_raised_round: 4
  last_seen_round: 6
  resolution: "引用已添加并在 §1/§2 讨论。"
  resolution_round: 6

- id: "F4-REF3"
  summary: "遗漏 Benjamini & Yekutieli (2001)"
  category: reference
  severity: minor
  status: resolved
  first_raised_round: 4
  last_seen_round: 
…[truncated 328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1540 · 2026-05-25T08:34:34.838422+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"status: open\\|status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null",
  "description": "Count open/in_progress issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"status: open\\|status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null",
    "description": "Count open/in_progress issues"
  }
}
```

</details>

---


### Tool result

_source line 1541 · 2026-05-25T08:34:35.801801+00:00_

75

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 963
}
```

</details>

---


### Tool call

_source line 1542 · 2026-05-25T08:34:35.853444+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -B2 \"status: open\\|status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null",
  "description": "Show open/in_progress issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -B2 \"status: open\\|status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null",
    "description": "Show open/in_progress issues"
  }
}
```

</details>

---


### Tool result

_source line 1543 · 2026-05-25T08:34:35.954413+00:00_

  category: method
  severity: critical
  status: in_progress
--
      action: "C3: 增加 null seeds s52-s54 收窄 CI；写作已明确 comparative 定位"
      assigned_to: agent
      status: in_progress
--
  category: framing
  severity: critical
  status: in_progress
--
  category: framing
  severity: critical
  status: in_progress
--
      action: "A1: Abstract scope 校准 [完成]; §4.5 标题加 at α=1.0 [完成]; C2: OPT-1.3B α=0.50 实验 [待GPU]"
      assigned_to: agent
      status: in_progress
--
  category: method
  severity: critical
  status: in_progress
--
  category: method
  severity: critical
  status: in_progress
--
      action: "Limitations 已更新 per-cell CI 宽度讨论。边界区域增加 seeds 需 GPU。"
      assigned_to: agent
      status: in_progress
--
  category: experiment
  severity: major
  status: in_progress
--
      action: "A3: PoC 措辞验证 [完成]; B3: PPL threshold baseline [完成]; C1: N=5 intervention [待GPU]"
      assigned_to: agent
      status: in_progress
--
  category: framing
  severity: warning
  status: in_progress
--
  category: method
  severity: major
  status: in_progress
--
  category: writing
  severity: warning
  status: open
--
  category: experiment
  severity: warning
  status: open
--
  category: format
  severity: critical
  status: in_progress
--
  category: writing
  severity: warning
  status: in_progress
--
  category: format
  severity: info
  status: open
--
  category: writing
  severity: info
  status: in_progress
--
  category: framing
  severity: major
  status: in_progress
--
  category: method
  severity: warning
  status: in_progress
--
  category: experiment
  severity: major
  status: open
--
  category: writing
  severity: critical
  status: in_progress
--
  category: writing
  severity: warning
  status: open
--
  category: experiment
  severity: warning
  status: open
--
  category: method
  severity: warning
  status: in_progress
--
  category: experiment
  severity: warning
  status: open
--
  category: experiment
  severity: warning
  status: open
--
  category
…[truncated 2930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1544 · 2026-05-25T08:35:02.238947+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"^- id:\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml | tail -5",
  "description": "Check last issue IDs in tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"^- id:\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml | tail -5",
    "description": "Check last issue IDs in tracker"
  }
}
```

</details>

---


### Tool result

_source line 1545 · 2026-05-25T08:35:02.391666+00:00_

1296:- id: "R15-SF1"
1309:- id: "R15-SF2"
1322:- id: "R15-SF3"
1335:- id: "R15-SF4"
1348:- id: "R15-1.4B-rev"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1546 · 2026-05-25T08:35:05.777566+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml",
  "description": "Read full review issues YAML",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml",
    "description": "Read full review issues YAML",
    "timeout": "30000"
  }
}
```

</details>

---


### Tool result

_source line 1547 · 2026-05-25T08:35:05.879331+00:00_

&lt;persisted-output>
Output too large (38.4KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse--claude-sessions-review-director-741faaa0/15434102-6a9f-4dbc-9e4f-0e014bffe0f2/tool-results/bt90d0x2i.txt

Preview (first 2KB):
issues:
# ============================================================
# Round 1-11 历史 resolved — 保留跨轮次记录
# ============================================================
- id: "R1-N1"
  summary: "Ground-truth pairs 定义存在循环论证"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Effect-size GT 重定义完成。"
  resolution_round: 1

- id: "R1-N2"
  summary: "FPR=0% 标定仅基于单 seed"
  category: method
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "α=0.0 三 seed FPR 验证完成。"
  resolution_round: 1

- id: "R1-N3"
  summary: "α=0.50 和 α=0.75 仅 1 seed"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "Multi-seed 补充完成。"
  resolution_round: 1

- id: "R2-N1"
  summary: "核心方法论为计量经济学已有知识的直接迁移，新颖性有限"
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "Round 1 三层定位 reframe 完成。"
  resolution_round: 1

- id: "R2-N2"
  summary: "α=0.75 multi-seed 实验未完成 + Appendix A 缺失"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "完成。"
  resolution_round: 1

- id: "R2-N3"
  summary: "实验规模过窄"
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: "跨架构验证已扩展至 15 model-seed 组合。"
  resolution_round: 1

- id: "R1-W1"
  summary: "Abstract 'Granger-causes' vs Discussion 'Granger-precedes' 措辞不一致"
  category: writing
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 2
  resolution: "核心修复完
…[truncated 287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1548 · 2026-05-25T08:35:21.619507+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"status: open\\|status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null | grep \"id:\\|summary:\\|status:\" | head -60",
  "description": "List open/in_progress issue IDs and summaries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"status: open\\|status: in_progress\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml 2>/dev/null | grep \"id:\\|summary:\\|status:\" | head -60",
    "description": "List open/in_progress issue IDs and summaries"
  }
}
```

</details>

---


### Tool result

_source line 1549 · 2026-05-25T08:35:21.720361+00:00_

  status: in_progress
      status: in_progress
- id: "F2-W4b"
  summary: "幂律边界 α_c(T) 拟合基础薄弱"
  status: in_progress
  status: in_progress
      status: in_progress
- id: "F2-W10"
  summary: "Cross-architecture 'coupling preserved' 条件 post-hoc"
  status: in_progress
  status: in_progress
      status: in_progress
- id: "F2-W7"
  summary: "Intervention 实验薄弱"
  status: in_progress
      status: in_progress
- id: "R12-N1"
  summary: "Design Principle 'formal design rationale' 作为独立贡献 oversells"
  status: in_progress
  status: in_progress
  status: open
  status: open
  status: in_progress
  status: in_progress
  status: open
- id: "R11-SYM1"
  summary: "β 符号重用：统计功率 vs 幂律指数"
  status: in_progress
  status: in_progress
  status: in_progress
  status: open
  status: in_progress
  status: open
- id: "R10-SF3"
  summary: "单一解码策略需定性讨论"
  status: open
- id: "R10-SF5"
  summary: "Bivariate confounding"
  status: in_progress
  status: open
- id: "R10-SF7"
  summary: "3-4 seeds replication power 有限"
  status: open
  status: open
- id: "F8-W2"
  summary: "Figure 子图内文字偏小"
  status: in_progress
  status: in_progress
  status: in_progress
  status: open
- id: "R13-W1"
  summary: "MMCT K≥3 共识框架 K 选择缺乏理论最优性证明"
  status: in_progress
  status: in_progress
  status: in_progress
      status: open
- id: "R13-W4"
  summary: "Abstract 'substantially reduces peak perplexity' 超出证据强度"
  status: in_progress
  status: in_progress

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1550 · 2026-05-25T08:35:36.144157+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml",
  "limit": "2000",
  "offset": "1340"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/review_issues.yaml",
    "limit": "2000",
    "offset": "1340"
  }
}
```

</details>

---


### Tool result

_source line 1551 · 2026-05-25T08:35:36.245304+00:00_

1340	  first_raised_round: 15
1341	  last_seen_round: 15
1342	  action_items:
1343	    - round: 15
1344	      action: "对 entropy 做 binning 后重跑 Granger test（~2h CPU 分析）"
1345	      assigned_to: main_agent
1346	      status: pending
1347	
1348	- id: "R15-1.4B-rev"
1349	  summary: "1.4B s43 bidirectional confounding 未在论文讨论"
1350	  category: writing
1351	  severity: warning
1352	  status: open
1353	  first_raised_round: 15
1354	  last_seen_round: 15
1355	  mentions:
1356	    - round: 15
1357	      reviewers: [reviewer]
1358	      note: "s43 在 α=0.60 reverse=6/8、α=0.75 reverse=5/8。§4.4 需加 disclosure。"
1359	  action_items:
1360	    - round: 15
1361	      action: "§4.4 加一句 1.4B seed-specific bidirectional confounding disclosure"
1362	      assigned_to: paper_agent
1363	      status: pending
1364	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1552 · 2026-05-25T08:38:40.353669+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 16 综合审稿报告\n\n**论文**: Characterizing the Detectability Landscape of Iterative Model Collapse\n**Venue**: EMNLP 2026 (ARR)\n**Reviewer**: R1（方法严谨性+实验有效性）、R2（新颖性+完整性+写作质量）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文系统研究迭代 model collapse 的可检测性，将 5 种时间序列统计方法（含 Permutation Granger causality）应用于 canary metrics（token entropy, ECE）与 downstream metrics（distinct-n, perplexity）的时序领先-滞后关系检测。核心发现是 PermG 在 α_c ≈ 0.50 处从 0/8 跳到 6/8 显著对，定义了三个检测区域（blind/onset/detection）。五种方法的 null-control FPR 从 6.7% 到 94.4%（κ=0.185），表明单方法分析不可靠。Cross-architecture 在 α=1.0 下支持 11/15 conditions 的 forward detection。\n\n---\n\n## Strengths\n\n**S1. [共识] 方法敏感性发现是论文最有价值的贡献。** 五种方法在相同数据上 FPR 从 6.7% 到 94.4%（κ=0.185），直接表明 model collapse 检测文献中单方法研究的结论可能不可靠。R2 认为此发现比 phase transition 本身更有价值，R1 同意。\n\n**S2. [共识] 实验设计严谨，统计控制充分。** Null-control (α=0.0) 基线、BH-FDR 多重检验校正、置换检验避免参数假设、multi-seed 复制、1,160 配置的 specification curve。这种严谨程度在 model collapse 检测文献中少见。\n\n**S3. [共识] 对 limitations 和 non-confirming cases 的讨论坦诚。** 4/15 cross-architecture non-confirming conditions 各有具体归因（precision sensitivity, bidirectional confounding, seed dependence, entropy decoupling）。Limitations 明确将框架定位为 \"confirmation tool rather than early-warning system\"。\n\n**S4. [共识] Appendix 充实（26 页），核心 claims 有详细支撑。** 涵盖理论推导、Shapley 分解、partial correlation、cross-architecture 细节、power simulation 等。\n\n**S5. [R1] Cascade ordering 结果有机制洞察。** Entropy 领先 diversity（24/24 forward, 0/24 reverse at α=1.0），first-differencing 消除 canary→perplexity 但保留 canary→diversity，证据干净。\n\n**S6. [R1] 可复现性高。** 详细超参（Appendix A）、明确种子、代码发布承诺。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical, 共识] Phase diagram 仅基于 3 seeds（2 自由度），方差估计不可靠。**\n- R1 提出（W1 critical），R2 完全同意。\n- Phase diagram（Figure 1）是论文核心图表，但仅 3 seeds 构建。检测边界 α_c ≈ 0.50 和三区域分类可能随 seed 增加而显著偏移。FPR 分析使用了 10 seeds（60 pairs），但 regime 边界的 α×T 网格仅 3 seeds。\n- 论文在 Limitations 中承认了这一点，但 self-acknowledgment 不能替代实际增加 seeds。\n\n**W2 [critical, 共识] \"Sharp transition\" 措辞超出统计证据强度。**\n- R1 提出（W2 critical），R2 提出（W1 major），交叉后双方同意需弱化措辞。\n- 6/8 检测率的 Clopper-Pearson 95% CI 为 [0.25, 0.92]，即真实检测概率可能低至 25%。Appendix S 的 sigmoid 拟合 steepness k=478±473（SE≈k），~100% 相对不确定性。\n- R2 补充：cross-seed consistency（3 seeds 独立产生 0/8→6/8）和 Fisher exact test（p=3.45×10⁻¹¹）提供了 transition 存在的部分支撑，但 \"sharp\" 仍超出证据强度。\n- **共识建议**：将 \"sharp detection phase transition\" 改为 \"steep/abrupt transition\" 或 \"apparent transition\"，在主文显式报告不确定性。\n\n**W3 [critical, R2→R1 同意] Phase transition 可能只是统计功效的自然行为，非真正的物理相变。**\n- R2 提出（W1 major），R1 在交叉中 AGREE with nuance。\n- 任何统计检验在信号强度跨过检测阈值时都会从不显著跳到显著——这是 power curve 的基本性质。k=15.7 比 smooth-signal predictions 陡峭 3-4x 的比较 baseline 是论文自己构建的 VAR(1) power simulation，有循环论证嫌疑。\n- R1 保留意见：VAR(1) simulation 的 onset steepness ratio k_obs/k_sim = 2.6-4.2 如果参数化合理，transition 比预期更陡有实质内容。但实际 α 网格分辨率为 5pp（0.45→0.50），\"2 percentage-point interval\" 来自 sigmoid 插值而非直接观测。\n- **共识建议**：重新定位核心贡献为 \"empirical characterization of detection limits\" 而非 \"phase transition discovery\"。\n\n**W4 [critical, 共识] 正文超出 8 页限制。**\n- R1（W8 minor）和 R2（W6 minor）均指出，视觉审查确认。Conclusion 延伸到第 9 页约 15-20 行（Limitations 标题之前）。EMNLP 2026 正文限 8 页。\n- 虽然修复简单（压缩 Discussion/Conclusion 几句话），但提交时必须解决。\n\n### Should-Fix（显著影响论文质量）\n\n**W5 [major, 共识] Cross-architecture 验证仅在 α=1.0（最易检测条件）。**\n- R1（W3 major）和 R2（W4 major）独立提出并在交叉中互相确认。\n- Phase diagram（Figure 1）是 Pythia-410M-specific。α_c ≈ 0.50 的相变在 GPT-2、Qwen、SmolLM 上未验证。仅 Pythia-1.4B 有 Appendix 中的部分 phase diagram 复现。Section 4.5 标题 \"Cross-Architecture Evaluation\" 在仅 α=1.0 条件下有误导性。\n- **共识建议**：至少在 1 个非 Pythia 架构上补做 intermediate-α 验证。\n\n**W6 [major, 共识] 方法论新颖性有限——成熟工具的直接应用。**\n- R2 提出（W2 major），R1 在交叉中 AGREE。\n- PermG、first-differencing、BH-FDR 均为标准工具。MMCT（Algorithm 1）本质是 FPR-inverse weighted voting，技术贡献有限。\n- R1 补充：作为 empirical contribution 论文是被接受的贡献形式，但方法论新颖性确实有限。\n- **共识建议**：将论文明确定位为 empirical study，强调实验发现而非方法论贡献。\n\n**W7 [major, 共识] Blind zone（α < 0.50）根本性限制框架实用价值。**\n- R2 提出（W3 major），R1 AGREE with nuance。\n- α=0.10 时 distinct-1 已下降 39.6%，但 Granger 检测完全失效（0/8）。Abstract/Introduction 叙事暗示实用检测能力，但 blind zone 意味着检测只在 contamination 已很严重时才有效。\n- R1 补充：刻画 blind zone 本身有价值——告诉 practitioners \"不要依赖这些方法做早期检测\"。但此定位应在 abstract/introduction 明确，不应延迟到 Limitations。\n\n**W8 [major, R1] 单一数据集（WikiText-103），domain 泛化性证据极弱。**\n- R1 提出（W4 major），R2 在交叉中 AGREE。\n- Domain 泛化性仅有 Appendix 一句话：\"Pythia-1.4B on C4 yields 8/8 PermG forward detection\"。\n- R2 补充：model collapse 文献大多使用单一数据集，这是领域性问题，非本文特有缺陷。\n\n**W9 [major, R1] MMCT K≥3 null-control FPR=10%，NaiveXCor（94.4% FPR）污染共识。**\n- R1 提出（W5 major），R2 AGREE with nuance。\n- K≥3 consensus FPR=10%（名义 5% 的两倍）。NaiveXCor 几乎必 reject，在 K 计数中恒贡献 1 分。\n- R2 澄清：需区分 weighted MMCT（NaiveXCor 权重仅 1.06 vs. PermG 14.9，影响被压制）和 K≥3 majority voting（equal-weight，NaiveXCor 确实污染）。Table 2 报告的是 K≥3 结果，Algorithm 1 描述的是 weighted scheme——两者混淆是写作问题。\n- **共识建议**：排除 FPR>50% 方法作为 robustness check，或在正文中解释 K≥3 和 weighted MMCT 的区别。\n\n**W10 [major, R2→R1 部分同意] Design Principles 1-2 标签过度包装。**\n- R2 提出（W5 major），R1 AGREE with nuance。\n- Entropy（连续量）比 distinct-n（离散量）先响应在一定程度上是 trivially expected。论文 Discussion 中也承认了 measurement resolution asymmetry。\n- R1 保留：量化刻画（24/24 forward, 0/24 reverse）的一致性不是 trivially 可预测的。\n- **共识建议**：将 \"Design Principle\" 改为 \"Empirical Finding\" 或 \"Proposition\"。\n\n### Nice-to-Fix\n\n**W11 [moderate, 共识] Intervention 实验仅在 α=1.0。**\n- R1（W6）和 R2（W7）独立提出。α=1.0 是最严重 collapse 条件，不需要精细检测即可观察退化。在 blind zone 边界（α≈0.50）测试才能展示实际价值。\n\n**W12 [moderate, R1] α=0.60 non-monotonic anomaly 解释缺直接证据。**\n- R1（W7）提出，R2 AGREE。\"Temporal lag compression\" 解释合理但间接。建议绘制 cross-correlation peak lag vs. α 图直接展示。\n\n**W13 [minor, R2→R1 REBUT] 术语使用（Granger causality / precedence / temporal predictive improvement）。**\n- R2 提出（W8 minor），R1 REBUT——认为是有意的术语精确化而非不一致。论文刻意避免 \"Granger causality\" 描述自己的 claims。\n- **分歧记录**：R1 认为这是术语精确化（标准计量经济学做法），建议首次出现时明确定义三者关系即可。R2 建议统一使用一个术语。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识（[AGREE]）：\n\n1. **Phase diagram 需要更多 seeds**（W1）——3 seeds 不足以稳定估计边界\n2. **\"Sharp transition\" 措辞需弱化**（W2）——CI 过宽，steepness 不确定性 ~100%\n3. **Cross-architecture 验证不足**（W5）——仅 α=1.0 不足以支撑 generalizability\n4. **方法论新颖性有限**（W6）——empirical contribution 而非 methodological contribution\n5. **Blind zone 限制实用性**（W7）——framing 应在 abstract/intro 明确\n6. **正文超页**（W4）——Conclusion 溢出约 15-20 行到第 9 页\n7. **Intervention 仅 α=1.0**（W11）——proof-of-concept scope 应明确\n8. **方法敏感性发现是最有价值的贡献**（S1）——6.7%→94.4% FPR spread\n9. **实验设计严谨**（S2）——统计控制在该领域属优秀水平\n\n## Reviewer Divergence\n\n仅一处实质分歧：\n\n| 问题 | R1 | R2 | 决议 |\n|------|----|----|------|\n| 术语一致性（W13） | REBUT：有意的精确化 | minor weakness | 非关键问题，记录分歧 |\n\n此外 R1-W9（Abstract 超 200 词）被 R2 REBUT（实际约 158-160 词），R1 未提供词数计算支持，采纳 R2 判断——Abstract 符合限制。\n\n---\n\n## Questions for Authors\n\n**Q1. [共识, critical]** α_c ≈ 0.50 边界对 seed 数量有多敏感？如果使用 10 seeds 构建 phase diagram，边界估计是否变化？能否提供 α_c 的 bootstrap 置信区间？\n\n**Q2. [共识, critical]** Phase transition steepness k=15.7 的 3-4x 比较 baseline 是什么？如何排除 steepness 来自 α grid 离散化（13 取值点，关键区域 5pp 分辨率）而非真实的物理现象？Appendix S 的 k=478±473 与主文 k=15.7 的数值差异如何解释？\n\n**Q3. [R2]** MMCT 相比 standalone PermG 的边际改进有多大？Limitations 承认 \"marginal improvement\"——Algorithm 1 的贡献是否应降级为 analytical framework？\n\n**Q4. [共识]** α=0.60 的 entropy-diversity lag 是否确实比 α=0.50 和 α=0.75 更短？能否提供直接的 cross-correlation 证据？\n\n**Q5. [共识]** Intervention 的 15% entropy threshold 在实际部署中（未知初始状态）如何设定？跨 α 水平是否有一个通用的校准阈值？\n\n**Q6. [R1]** First-differencing 消除 canary→perplexity 但保留 canary→diversity——两个指标都响应同一底层分布偏移，为什么 first-differencing 区分了二者？\"channel-specific rather than global\" 能否更严格定义？\n\n**Q7. [R2]** Table 2 中 K≥3 consensus 在 α=0.75 的 TPR 为 37.5%，低于 α=0.50 的 66.7%——consensus voting 在 detection zone 反而不如 onset 区域可靠？\n\n---\n\n## Missing References\n\n两位 Reviewer 共建议 6 篇可能遗漏的文献：\n\n| 文献 | 提出者 | 相关性 | 引用紧迫度 |\n|------|--------|--------|-----------|\n| Hataya et al. (2023) \"Will Large-scale Generative Models Corrupt Future Datasets?\" | R1 | 早期迭代合成训练 | 应引用 |\n| Rabanser et al. (2019) \"Failing Loudly\" | R1 | 通用 distribution shift detection | 可选引用 |\n| Carvalhais et al. (EMNLP 2025) \"Recursive Training Loops in LLMs\" (arXiv:2504.03814) | R2 | Recursive training + distribution shift | 应引用（需验证真实性） |\n| Buffa & Del Corro (2026) \"Entropy Sentinel\" (arXiv:2601.09001) | R2 | Entropy 做 LLM 监控 | 应引用（需验证真实性） |\n| LLM-GC (WSDM 2026) | R2 | Granger + LLMs | 可选引用（需验证真实性） |\n| Rate of Model Collapse (arXiv:2412.17646, 2024) | R2 | Collapse rate 理论分析 | 可选引用（需验证真实性） |\n\n**R1 注意**：R2 建议的 2025-2026 年文献真实性未经独立验证，建议 Research Director 核实后再决定是否引用。\n\n现有引用覆盖评价：对 model collapse 核心文献（Shumailov 2024, Dohmatob 2024/2025, Kazdan 2025, Schaeffer 2025）和 Granger causality 方法论（Granger 1969, Shojaie & Fox 2022）的引用充分。遗漏主要集中在 2025-2026 年最新 detection/monitoring 工作。\n\n---\n\n## External Review\n\n**状态：未请求。** 项目配置中未启用外部审稿（paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成**（耗时 ~4 分钟）\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| **critical** | Page 36 | 最后一页仅左栏顶部 ~6 行，~85% 空白。建议合并或扩充 |\n| **warning** | Page 9 | 主文 Conclusion 延伸到第 9 页约 15-20 行。正文约 8.2 页，超页风险（与 W4 一致） |\n| **warning** | Page 14 | Appendix 页面几乎全为密集文本，无 figure/equation 视觉间断 |\n| **info** | Page 5 | Figure 4(b) 的 y 轴标签和 legend 字号偏小 |\n| **info** | Page 6 | Figure 5 彩色方块较小，灰度打印时难区分 |\n| **info** | Page 25 | Appendix 页面密度极高（多图表挤压） |\n| **info** | Pages 21, 30 | 数学推导页纯文本+公式，无视觉间断 |\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.0/5 | 2.5/5 | 2.75/5 |\n| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |\n\n### Overall: 3.0 — Findings\n\n两位 Reviewer 独立且一致地评估为 **3.0 Findings**。\n\n**核心判断依据：**\n\n1. **贡献定位问题**：论文最强的贡献是方法敏感性的实证发现（FPR 6.7%→94.4%），但论文将 \"phase transition discovery\" 作为第一贡献——这一 claim 的证据基础（3 seeds, CI [0.25, 0.92], steepness 不确定性 ~100%）不足以支撑 Conference 级别的 novelty。\n2. **方法论新颖性**：核心方法（PermG + first-differencing + BH-FDR）是成熟工具的应用，MMCT 是简单的 weighted voting。作为 empirical study 有价值，但方法论贡献有限。\n3. **Generalizability 缺口**：Phase diagram 是 Pythia-410M + WikiText-103 specific。Cross-architecture 仅 α=1.0。单一数据集。\n4. **Blind zone 的 framing 张力**：框架在 α < 0.50 时完全失效，但叙事暗示实用检测能力。\n\n**升至 3.5 Borderline Conference 的条件（两位 Reviewer 共识）：**\n1. Phase diagram 增至 ≥10 seeds 并报告 α_c 的 bootstrap CI\n2. 至少在 1 个非 Pythia 架构上验证 intermediate-α phase diagram 结构\n3. 第二 domain（如 C4）的核心实验复现\n4. 将 framing 从 \"phase transition discovery\" 重新定位为 \"empirical characterization of detection limits\"\n5. 修正 \"sharp transition\" 措辞以匹配统计证据强度\n6. 解决正文超页问题\n\n**不建议降至 2.5 的原因：** 实验质量高、统计控制严格、self-awareness 良好、方法敏感性发现对社区有实际警示价值。\n\n### Confidence: 4/5\n两位 Reviewer 均仔细阅读全部 36 页（含 26 页 appendix），熟悉时间序列因果检验和 model collapse 文献。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 约 158-160 词，符合 200 词限制（R2 验证，R1-W9 不成立）\n- \"sharp detection phase transition\" 需弱化为 \"steep\" 或 \"abrupt\"\n- \"reduces peak perplexity by 64%\" 需标注 \"proof-of-concept under α=1.0\"\n\n### Section 1 (Introduction)\n- \"can we reliably detect the onset of model collapse?\" 的叙事与 blind zone（α<0.50）存在张力——应更早地 scope practical claims\n- Contribution 1 应重新定位：从 \"identify a sharp detection phase transition\" 到 \"empirically characterize detection limits\"\n- Contribution 4 的 intervention 应降低 prominence，明确为 proof-of-concept\n\n### Section 2 (Related Work)\n- 覆盖充分，遗漏集中在 2025-2026 最新工作（见 Missing References）\n- 与 distribution shift detection 更广文献的连接不足（Rabanser et al. 2019 等）\n\n### Section 3 (Method)\n- Design Principle 1-2 标签应改为 Proposition/Empirical Finding\n- MMCT（Algorithm 1）与 Table 2 的 K≥3 scheme 关系需在正文中澄清\n- 建议排除 NaiveXCor（FPR 94.4%）的 robustness check\n\n### Section 4 (Experiments)\n- Phase diagram（Figure 1）需更多 seeds 或显式报告 boundary uncertainty\n- α=0.60 anomaly 需直接 cross-correlation 证据\n- Cross-architecture（Section 4.5）标题应改为 \"Cross-Architecture Evaluation at α=1.0\"\n- Intervention（Section 4.6）需在中等 contamination（α≈0.50）验证\n\n### Section 5 (Discussion)\n- 写作质量良好，对 limitations 的讨论坦诚\n- \"measurement resolution asymmetry\" 的讨论与 Design Principle 标签的张力应解决\n\n### Section 6 (Conclusion)\n- 需压缩以解决超页问题\n\n### Limitations\n- 内容充分，覆盖 scope/power/causality 三个方面\n- \"confirmation tool rather than early-warning system\" 的定位应前移到 abstract/introduction\n\n### Appendix\n- 内容极为充实（26 页），支撑主文 claims\n- 部分页面密度过高（视觉审查 Page 14, 25）\n- 最后一页（Page 36）85% 空白，建议合并",
  "project": "distrib_canary_collapse",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_21bf8254f3677799a62db5ed920cc0b3:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 16 综合审稿报告\n\n**论文**: Characterizing the Detectability Landscape of Iterative Model Collapse\n**Venue**: EMNLP 2026 (ARR)\n**Reviewer**: R1（方法严谨性+实验有效性）、R2（新颖性+完整性+写作质量）\n**审稿模式**: Fresh（重新审稿）\n\n---\n\n## Summary\n\n本文系统研究迭代 model collapse 的可检测性，将 5 种时间序列统计方法（含 Permutation Granger causality）应用于 canary metrics（token entropy, ECE）与 downstream metrics（distinct-n, perplexity）的时序领先-滞后关系检测。核心发现是 PermG 在 α_c ≈ 0.50 处从 0/8 跳到 6/8 显著对，定义了三个检测区域（blind/onset/detection）。五种方法的 null-control FPR 从 6.7% 到 94.4%（κ=0.185），表明单方法分析不可靠。Cross-architecture 在 α=1.0 下支持 11/15 conditions 的 forward detection。\n\n---\n\n## Strengths\n\n**S1. [共识] 方法敏感性发现是论文最有价值的贡献。** 五种方法在相同数据上 FPR 从 6.7% 到 94.4%（κ=0.185），直接表明 model collapse 检测文献中单方法研究的结论可能不可靠。R2 认为此发现比 phase transition 本身更有价值，R1 同意。\n\n**S2. [共识] 实验设计严谨，统计控制充分。** Null-control (α=0.0) 基线、BH-FDR 多重检验校正、置换检验避免参数假设、multi-seed 复制、1,160 配置的 specification curve。这种严谨程度在 model collapse 检测文献中少见。\n\n**S3. [共识] 对 limitations 和 non-confirming cases 的讨论坦诚。** 4/15 cross-architecture non-confirming conditions 各有具体归因（precision sensitivity, bidirectional confounding, seed dependence, entropy decoupling）。Limitations 明确将框架定位为 \"confirmation tool rather than early-warning system\"。\n\n**S4. [共识] Appendix 充实（26 页），核心 claims 有详细支撑。** 涵盖理论推导、Shapley 分解、partial correlation、cross-architecture 细节、power simulation 等。\n\n**S5. [R1] Cascade ordering 结果有机制洞察。** Entropy 领先 diversity（24/24 forward, 0/24 reverse at α=1.0），first-differencing 消除 canary→perplexity 但保留 canary→diversity，证据干净。\n\n**S6. [R1] 可复现性高。** 详细超参（Appendix A）、明确种子、代码发布承诺。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical, 共识] Phase diagram 仅基于 3 seeds（2 自由度），方差估计不可靠。**\n- R1 提出（W1 critical），R2 完全同意。\n- Phase diagram（Figure 1）是论文核心图表，但仅 3 seeds 构建。检测边界 α_c ≈ 0.50 和三区域分类可能随 seed 增加而显著偏移。FPR 分析使用了 10 seeds（60 pairs），但 regime 边界的 α×T 网格仅 3 seeds。\n- 论文在 Limitations 中承认了这一点，但 self-acknowledgment 不能替代实际增加 seeds。\n\n**W2 [critical, 共识] \"Sharp transition\" 措辞超出统计证据强度。**\n- R1 提出（W2 critical），R2 提出（W1 major），交叉后双方同意需弱化措辞。\n- 6/8 检测率的 Clopper-Pearson 95% CI 为 [0.25, 0.92]，即真实检测概率可能低至 25%。Appendix S 的 sigmoid 拟合 steepness k=478±473（SE≈k），~100% 相对不确定性。\n- R2 补充：cross-seed consistency（3 seeds 独立产生 0/8→6/8）和 Fisher exact test（p=3.45×10⁻¹¹）提供了 transition 存在的部分支撑，但 \"sharp\" 仍超出证据强度。\n- **共识建议**：将 \"sharp detection phase transition\" 改为 \"steep/abrupt transition\" 或 \"apparent transition\"，在主文显式报告不确定性。\n\n**W3 [critical, R2→R1 同意] Phase transition 可能只是统计功效的自然行为，非真正的物理相变。**\n- R2 提出（W1 major），R1 在交叉中 AGREE with nuance。\n- 任何统计检验在信号强度跨过检测阈值时都会从不显著跳到显著——这是 power curve 的基本性质。k=15.7 比 smooth-signal predictions 陡峭 3-4x 的比较 baseline 是论文自己构建的 VAR(1) power simulation，有循环论证嫌疑。\n- R1 保留意见：VAR(1) simulation 的 onset steepness ratio k_obs/k_sim = 2.6-4.2 如果参数化合理，transition 比预期更陡有实质内容。但实际 α 网格分辨率为 5pp（0.45→0.50），\"2 percentage-point interval\" 来自 sigmoid 插值而非直接观测。\n- **共识建议**：重新定位核心贡献为 \"empirical characterization of detection limits\" 而非 \"phase transition discovery\"。\n\n**W4 [critical, 共识] 正文超出 8 页限制。**\n- R1（W8 minor）和 R2（W6 minor）均指出，视觉审查确认。Conclusion 延伸到第 9 页约 15-20 行（Limitations 标题之前）。EMNLP 2026 正文限 8 页。\n- 虽然修复简单（压缩 Discussion/Conclusion 几句话），但提交时必须解决。\n\n### Should-Fix（显著影响论文质量）\n\n**W5 [major, 共识] Cross-architecture 验证仅在 α=1.0（最易检测条件）。**\n- R1（W3 major）和 R2（W4 major）独立提出并在交叉中互相确认。\n- Phase diagram（Figure 1）是 Pythia-410M-specific。α_c ≈ 0.50 的相变在 GPT-2、Qwen、SmolLM 上未验证。仅 Pythia-1.4B 有 Appendix 中的部分 phase diagram 复现。Section 4.5 标题 \"Cross-Architecture Evaluation\" 在仅 α=1.0 条件下有误导性。\n- **共识建议**：至少在 1 个非 Pythia 架构上补做 intermediate-α 验证。\n\n**W6 [major, 共识] 方法论新颖性有限——成熟工具的直接应用。**\n- R2 提出（W2 major），R1 在交叉中 AGREE。\n- PermG、first-differencing、BH-FDR 均为标准工具。MMCT（Algorithm 1）本质是 FPR-inverse weighted voting，技术贡献有限。\n- R1 补充：作为 empirical contribution 论文是被接受的贡献形式，但方法论新颖性确实有限。\n- **共识建议**：将论文明确定位为 empirical study，强调实验发现而非方法论贡献。\n\n**W7 [major, 共识] Blind zone（α < 0.50）根本性限制框架实用价值。**\n- R2 提出（W3 major），R1 AGREE with nuance。\n- α=0.10 时 distinct-1 已下降 39.6%，但 Granger 检测完全失效（0/8）。Abstract/Introduction 叙事暗示实用检测能力，但 blind zone 意味着检测只在 contamination 已很严重时才有效。\n- R1 补充：刻画 blind zone 本身有价值——告诉 practitioners \"不要依赖这些方法做早期检测\"。但此定位应在 abstract/introduction 明确，不应延迟到 Limitations。\n\n**W8 [major, R1] 单一数据集（WikiText-103），domain 泛化性证据极弱。**\n- R1 提出（W4 major），R2 在交叉中 AGREE。\n- Domain 泛化性仅有 Appendix 一句话：\"Pythia-1.4B on C4 yields 8/8 PermG forward detection\"。\n- R2 补充：model collapse 文献大多使用单一数据集，这是领域性问题，非本文特有缺陷。\n\n**W9 [major, R1] MMCT K≥3 null-control FPR=10%，NaiveXCor（94.4% FPR）污染共识。**\n- R1 提出（W5 major），R2 AGREE with nuance。\n- K≥3 consensus FPR=10%（名义 5% 的两倍）。NaiveXCor 几乎必 reject，在 K 计数中恒贡献 1 分。\n- R2 澄清：需区分 weighted MMCT（NaiveXCor 权重仅 1.06 vs. PermG 14.9，影响被压制）和 K≥3 majority voting（equal-weight，NaiveXCor 确实污染）。Table 2 报告的是 K≥3 结果，Algorithm 1 描述的是 weighted scheme——两者混淆是写作问题。\n- **共识建议**：排除 FPR>50% 方法作为 robustness check，或在正文中解释 K≥3 和 weighted MMCT 的区别。\n\n**W10 [major, R2→R1 部分同意] Design Principles 1-2 标签过度包装。**\n- R2 提出（W5 major），R1 AGREE with nuance。\n- Entropy（连续量）比 distinct-n（离散量）先响应在一定程度上是 trivially expected。论文 Discussion 中也承认了 measurement resolution asymmetry。\n- R1 保留：量化刻画（24/24 forward, 0/24 reverse）的一致性不是 trivially 可预测的。\n- **共识建议**：将 \"Design Principle\" 改为 \"Empirical Finding\" 或 \"Proposition\"。\n\n### Nice-to-Fix\n\n**W11 [moderate, 共识] Intervention 实验仅在 α=1.0。**\n- R1（W6）和 R2（W7）独立提出。α=1.0 是最严重 collapse 条件，不需要精细检测即可观察退化。在 blind zone 边界（α≈0.50）测试才能展示实际价值。\n\n**W12 [moderate, R1] α=0.60 non-monotonic anomaly 解释缺直接证据。**\n- R1（W7）提出，R2 AGREE。\"Temporal lag compression\" 解释合理但间接。建议绘制 cross-correlation peak lag vs. α 图直接展示。\n\n**W13 [minor, R2→R1 REBUT] 术语使用（Granger causality / precedence / temporal predictive improvement）。**\n- R2 提出（W8 minor），R1 REBUT——认为是有意的术语精确化而非不一致。论文刻意避免 \"Granger causality\" 描述自己的 claims。\n- **分歧记录**：R1 认为这是术语精确化（标准计量经济学做法），建议首次出现时明确定义三者关系即可。R2 建议统一使用一个术语。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成共识（[AGREE]）：\n\n1. **Phase diagram 需要更多 seeds**（W1）——3 seeds 不足以稳定估计边界\n2. **\"Sharp transition\" 措辞需弱化**（W2）——CI 过宽，steepness 不确定性 ~100%\n3. **Cross-architecture 验证不足**（W5）——仅 α=1.0 不足以支撑 generalizability\n4. **方法论新颖性有限**（W6）——empirical contribution 而非 methodological contribution\n5. **Blind zone 限制实用性**（W7）——framing 应在 abstract/intro 明确\n6. **正文超页**（W4）——Conclusion 溢出约 15-20 行到第 9 页\n7. **Intervention 仅 α=1.0**（W11）——proof-of-concept scope 应明确\n8. **方法敏感性发现是最有价值的贡献**（S1）——6.7%→94.4% FPR spread\n9. **实验设计严谨**（S2）——统计控制在该领域属优秀水平\n\n## Reviewer Divergence\n\n仅一处实质分歧：\n\n| 问题 | R1 | R2 | 决议 |\n|------|----|----|------|\n| 术语一致性（W13） | REBUT：有意的精确化 | minor weakness | 非关键问题，记录分歧 |\n\n此外 R1-W9（Abstract 超 200 词）被 R2 REBUT（实际约 158-160 词），R1 未提供词数计算支持，采纳 R2 判断——Abstract 符合限制。\n\n---\n\n## Questions for Authors\n\n**Q1. [共识, critical]** α_c ≈ 0.50 边界对 seed 数量有多敏感？如果使用 10 seeds 构建 phase diagram，边界估计是否变化？能否提供 α_c 的 bootstrap 置信区间？\n\n**Q2. [共识, critical]** Phase transition steepness k=15.7 的 3-4x 比较 baseline 是什么？如何排除 steepness 来自 α grid 离散化（13 取值点，关键区域 5pp 分辨率）而非真实的物理现象？Appendix S 的 k=478±473 与主文 k=15.7 的数值差异如何解释？\n\n**Q3. [R2]** MMCT 相比 standalone PermG 的边际改进有多大？Limitations 承认 \"marginal improvement\"——Algorithm 1 的贡献是否应降级为 analytical framework？\n\n**Q4. [共识]** α=0.60 的 entropy-diversity lag 是否确实比 α=0.50 和 α=0.75 更短？能否提供直接的 cross-correlation 证据？\n\n**Q5. [共识]** Intervention 的 15% entropy threshold 在实际部署中（未知初始状态）如何设定？跨 α 水平是否有一个通用的校准阈值？\n\n**Q6. [R1]** First-differencing 消除 canary→perplexity 但保留 canary→diversity——两个指标都响应同一底层分布偏移，为什么 first-differencing 区分了二者？\"channel-specific rather than global\" 能否更严格定义？\n\n**Q7. [R2]** Table 2 中 K≥3 consensus 在 α=0.75 的 TPR 为 37.5%，低于 α=0.50 的 66.7%——consensus voting 在 detection zone 反而不如 onset 区域可靠？\n\n---\n\n## Missing References\n\n两位 Reviewer 共建议 6 篇可能遗漏的文献：\n\n| 文献 | 提出者 | 相关性 | 引用紧迫度 |\n|------|--------|--------|-----------|\n| Hataya et al. (2023) \"Will Large-scale Generative Models Corrupt Future Datasets?\" | R1 | 早期迭代合成训练 | 应引用 |\n| Rabanser et al. (2019) \"Failing Loudly\" | R1 | 通用 distribution shift detection | 可选引用 |\n| Carvalhais et al. (EMNLP 2025) \"Recursive Training Loops in LLMs\" (arXiv:2504.03814) | R2 | Recursive training + distribution shift | 应引用（需验证真实性） |\n| Buffa & Del Corro (2026) \"Entropy Sentinel\" (arXiv:2601.09001) | R2 | Entropy 做 LLM 监控 | 应引用（需验证真实性） |\n| LLM-GC (WSDM 2026) | R2 | Granger + LLMs | 可选引用（需验证真实性） |\n| Rate of Model Collapse (arXiv:2412.17646, 2024) | R2 | Collapse rate 理论分析 | 可选引用（需验证真实性） |\n\n**R1 注意**：R2 建议的 2025-2026 年文献真实性未经独立验证，建议 Research Director 核实后再决定是否引用。\n\n现有引用覆盖评价：对 model collapse 核心文献（Shumailov 2024, Dohmatob 2024/2025, Kazdan 2025, Schaeffer 2025）和 Granger causality 方法论（Granger 1969, Shojaie & Fox 2022）的引用充分。遗漏主要集中在 2025-2026 年最新 detection/monitoring 工作。\n\n---\n\n## External Review\n\n**状态：未请求。** 项目配置中未启用外部审稿（paperreview.ai）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态：已完成**（耗时 ~4 分钟）\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| **critical** | Page 36 | 最后一页仅左栏顶部 ~6 行，~85% 空白。建议合并或扩充 |\n| **warning** | Page 9 | 主文 Conclusion 延伸到第 9 页约 15-20 行。正文约 8.2 页，超页风险（与 W4 一致） |\n| **warning** | Page 14 | Appendix 页面几乎全为密集文本，无 figure/equation 视觉间断 |\n| **info** | Page 5 | Figure 4(b) 的 y 轴标签和 legend 字号偏小 |\n| **info** | Page 6 | Figure 5 彩色方块较小，灰度打印时难区分 |\n| **info** | Page 25 | Appendix 页面密度极高（多图表挤压） |\n| **info** | Pages 21, 30 | 数学推导页纯文本+公式，无视觉间断 |\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |\n| Excitement | 3.0/5 | 2.5/5 | 2.75/5 |\n| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |\n\n### Overall: 3.0 — Findings\n\n两位 Reviewer 独立且一致地评估为 **3.0 Findings**。\n\n**核心判断依据：**\n\n1. **贡献定位问题**：论文最强的贡献是方法敏感性的实证发现（FPR 6.7%→94.4%），但论文将 \"phase transition discovery\" 作为第一贡献——这一 claim 的证据基础（3 seeds, CI [0.25, 0.92], steepness 不确定性 ~100%）不足以支撑 Conference 级别的 novelty。\n2. **方法论新颖性**：核心方法（PermG + first-differencing + BH-FDR）是成熟工具的应用，MMCT 是简单的 weighted voting。作为 empirical study 有价值，但方法论贡献有限。\n3. **Generalizability 缺口**：Phase diagram 是 Pythia-410M + WikiText-103 specific。Cross-architecture 仅 α=1.0。单一数据集。\n4. **Blind zone 的 framing 张力**：框架在 α < 0.50 时完全失效，但叙事暗示实用检测能力。\n\n**升至 3.5 Borderline Conference 的条件（两位 Reviewer 共识）：**\n1. Phase diagram 增至 ≥10 seeds 并报告 α_c 的 bootstrap CI\n2. 至少在 1 个非 Pythia 架构上验证 intermediate-α phase diagram 结构\n3. 第二 domain（如 C4）的核心实验复现\n4. 将 framing 从 \"phase transition discovery\" 重新定位为 \"empirical characterization of detection limits\"\n5. 修正 \"sharp transition\" 措辞以匹配统计证据强度\n6. 解决正文超页问题\n\n**不建议降至 2.5 的原因：** 实验质量高、统计控制严格、self-awareness 良好、方法敏感性发现对社区有实际警示价值。\n\n### Confidence: 4/5\n两位 Reviewer 均仔细阅读全部 36 页（含 26 页 appendix），熟悉时间序列因果检验和 model collapse 文献。\n\n---\n\n## Detailed Comments（逐节）\n\n### Abstract\n- 约 158-160 词，符合 200 词限制（R2 验证，R1-W9 不成立）\n- \"sharp detection phase transition\" 需弱化为 \"steep\" 或 \"abrupt\"\n- \"reduces peak perplexity by 64%\" 需标注 \"proof-of-concept under α=1.0\"\n\n### Section 1 (Introduction)\n- \"can we reliably detect the onset of model collapse?\" 的叙事与 blind zone（α<0.50）存在张力——应更早地 scope practical claims\n- Contribution 1 应重新定位：从 \"identify a sharp detection phase transition\" 到 \"empirically characterize detection limits\"\n- Contribution 4 的 intervention 应降低 prominence，明确为 proof-of-concept\n\n### Section 2 (Related Work)\n- 覆盖充分，遗漏集中在 2025-2026 最新工作（见 Missing References）\n- 与 distribution shift detection 更广文献的连接不足（Rabanser et al. 2019 等）\n\n### Section 3 (Method)\n- Design Principle 1-2 标签应改为 Proposition/Empirical Finding\n- MMCT（Algorithm 1）与 Table 2 的 K≥3 scheme 关系需在正文中澄清\n- 建议排除 NaiveXCor（FPR 94.4%）的 robustness check\n\n### Section 4 (Experiments)\n- Phase diagram（Figure 1）需更多 seeds 或显式报告 boundary uncertainty\n- α=0.60 anomaly 需直接 cross-correlation 证据\n- Cross-architecture（Section 4.5）标题应改为 \"Cross-Architecture Evaluation at α=1.0\"\n- Intervention（Section 4.6）需在中等 contamination（α≈0.50）验证\n\n### Section 5 (Discussion)\n- 写作质量良好，对 limitations 的讨论坦诚\n- \"measurement resolution asymmetry\" 的讨论与 Design Principle 标签的张力应解决\n\n### Section 6 (Conclusion)\n- 需压缩以解决超页问题\n\n### Limitations\n- 内容充分，覆盖 scope/power/causality 三个方面\n- \"confirmation tool rather than early-warning system\" 的定位应前移到 abstract/introduction\n\n### Appendix\n- 内容极为充实（26 页），支撑主文 claims\n- 部分页面密度过高（视觉审查 Page 14, 25）\n- 最后一页（Page 36）85% 空白，建议合并",
    "project": "distrib_canary_collapse",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "review_chat_id": "oc_21bf8254f3677799a62db5ed920cc0b3"
  }
}
```

</details>

---
