---
round: 11
review_mode: fresh
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-24T13:38:49.662798+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 11 (Fresh Review)

**论文**: "Characterizing the Detectability Landscape of Iterative Model Collapse"
**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)
**审稿模式**: Fresh (重新审稿)
**Reviewer**: 2 人（R1: 方法严谨性+统计验证+实验有效性; R2: 新颖性/贡献定位+完整性+写作质量+格式合规）

---

## Summary

本文系统研究迭代模型坍塌的可检测性边界：在给定合成数据污染比例 α 和观测窗口长度 T 的条件下，何时能统计显著地检测到分布退化。以 Pythia-410M 为主架构，在 13 个 α 水平 × 多个 T 值上构建检测相图，发现四个 regime（blind / onset / sync-dip / detection），拟合幂律检测边界 α_c(T) ∝ T^{−2.08}。跨 5 个模型族（345M–6.9B）在 α=1.0 下验证泛化性。证明 entropy Granger-precedes diversity by ≥1 generation（14/15 实验），并展示 canary-triggered intervention 的概念验证（64% peak perplexity reduction, N=2）。方法敏感性分析表明 5 种检测方法在相同数据上产生 FPR 从 3% 到 92% 的差异。

---

## Strengths

1. **新颖且重要的研究问题**：model collapse 的可检测性景观是该领域空白，将问题框架化为 (α, T) 二维相图具有很强的概念清晰度。

2. **方法论透明度异常出色**：论文对自身统计局限的坦诚程度（FPR CI、功率不足、8-pair CI 宽度、β CI 宽度）超过同类工作。Limitations section 直接引用 Clopper-Pearson CI 并承认"coarse topology rather than precise probability surface"。

3. **方法敏感性是最强贡献**：5 种方法在相同数据上产生截然不同的结论（从 universal detection 到 complete null），这一发现对 model collapse 文献中方法选择的随意性具有重要警示意义。

4. **异常详尽的鲁棒性验证**（21 页 appendix）：specification curve analysis（1,160 配置）、Shapley 值分解、功率分析、非平稳鲁棒性模拟、predict-then-verify 等，远超平均水平。

5. **First-differencing 作为诊断工具**：发现 first-differencing 消除 canary→perplexity 但保留 canary→diversity（24/24→24/24），精确 scope 了 Granger precedence claim，具有独立方法论价值。

6. **系统且严谨的实验控制**：BH-FDR 校正、5000 permutations、多种子复制、null-control calibration，在 NLP 实证工作中罕见。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [critical] PermG 的 FPR 膨胀削弱检测边界精度
- PermG null-control FPR = 11.1%（4/36），CI [1.2%, 30.4%]，超出 nominal 5%
- 在检测边界附近（α≈0.45-0.50），假阳性和真阳性难以区分
- 虽然 0/8→6/8 的跳跃幅度不能完全由 FPR 解释，但精确边界位置不可靠
- GPT-2-medium 上 FPR=50% 说明该问题是 architecture-dependent
- **共识**: 双方 AGREE，must-fix

**MF-2** [critical] "Detectability landscape" framing 与证据范围显著落差
- 完整 α×T grid 仅在 Pythia-410M 上映射
- 跨架构验证限于 α=1.0（最容易检测的极端场景）
- 无法回答：phase-diagram 的四 regime 结构是否适用于其他架构在中间 α 水平下的情况
- "Five families (345M–6.9B)" 实为 4 个独立族 + 1 Pythia variant；最大实测 3B，非 6.9B
- Abstract "cross-architecture validation confirms" 措辞过于乐观（27% 失败率=4/15 条件）
- **共识**: 双方 AGREE，framing gap 真实存在

**MF-3** [critical] 幂律边界 α_c(T) ∝ T^{−2.08} 拟合基础过于薄弱
- 5 个 T 值拟合 2 参数（A, β_signal），排除 sync-dip 后仅 4 有效点（2 自由度）
- LOO-CV MAE=0.037 在 4-5 个点上信息量极有限——任何合理单调函数均可达到
- sync-dip 排除是 post-hoc，ΔAIC=4.15 仅在包含 sync-dip 时支持 power-probit
- β_signal MLE CI [0.24, 0.78] 意味着 T 指数不确定性极大（可能从 −0.64 到 −2.08）
- **共识**: 双方 AGREE。R2 补充 mitigating factors（15/15 within CI, ΔAIC analysis）但同意应降级为"consistent with power law"

**MF-4** [critical] 统计功率 β=0.66 CI [0.24, 0.78] 使"不可检测"无法区分于"功率不足"
- 功率低至 0.24 时，α_c(T) 会被严重高估
- T^{−2.08} 指数可能反映检验功率随 T 衰减而非信号物理特性
- Appendix N 确认：T≤8 时功率不足 50%
- 正文对此限制的呈现不够显著（仅 Limitations 一句）
- **共识**: 双方 AGREE

### Should-Fix（影响评分但不一票否决）

**SF-1** [warning] 核心方法 novelty 有限：计量经济学标准技术直接移植
- PermG 源自 Granger (1969)，MMCT 是简单投票，Design Principles 依赖 Jensen 不等式
- R1 partial REBUT：pipeline integration (PermG + first-diff + BH-FDR + MMCT + Shapley + spec curve) 有方法论价值；empirical characterization 是合理贡献模式
- **分歧**: R2 认为 novelty 不足以支撑 main conference；R1 认为在 Findings-borderline Conference 范围合理

**SF-2** [warning] Intervention 实验证据力不足
- 仅 α=1.0, N=2 seeds, post-hoc threshold (15%)
- Abstract 中 "64% perplexity reduction" 在 N=2 下精确数字不可信
- **共识**: 双方同意 abstract 应用定性描述替代精确数字；proof-of-concept framing 可保留

**SF-3** [warning] 跨架构验证暴露系统性异质性
- SmolLM3 在 α=1.0 下仅 3/8（non-monotonic entropy violates Design Principle 1）
- GPT-2-medium null FPR=50%；Pythia-1.4B seed-dependent (2/8 vs 6/8)
- 三种失败覆盖不同规模和家族，说明非随机变异
- **共识**: 双方 AGREE，建议改为"partial validation with notable exceptions"

**SF-4** [warning] "3%–92%" FPR 范围含失效方法 NaiveXCorr
- 92% 来自 NaiveXCorr——本质上是未通过 null 验证的 failed baseline
- 合格方法范围实为 3%–39%，仍有意义但不如 92% 戏剧化
- **共识**: 双方 AGREE，abstract 应区分 validated methods vs all methods

**SF-5** [warning] 每 cell 仅 8 pairs → binomial CI 极宽
- 6/8 的 Clopper-Pearson 95% CI = [0.25, 0.92]
- Figure 1 的二值化色彩编码可能夸大相邻 cell 的统计区分度
- Limitations 已承认但视觉呈现未反映不确定性
- **共识**: 双方 AGREE

### Minor Issues

- β 符号重用：统计功率 vs 幂律指数，同一论文中易混淆（双方 AGREE）
- Table 1 / Figure 6 浮动到第 9 页，触及 8 页限制边界（双方 AGREE）
- Abstract 脚注不标准，可能影响索引系统（双方 AGREE）
- "Five families" 含 Padding-410M（Pythia variant），严格仅 4 独立族（双方 AGREE）

---

## Reviewer Consensus

以下问题双方达成完全共识 [AGREE]：

1. FPR 膨胀是核心定量声称的薄弱环节（MF-1）
2. 幂律拟合自由度不足，应降级为"consistent with"（MF-3）
3. 统计功率限制使 landscape 解读存在系统性偏差（MF-4）
4. Framing 与证据范围存在落差（MF-2）
5. 跨架构 27% 失败率需要更审慎的措辞（SF-3）
6. "3%–92%" 含 NaiveXCorr 夸大了 method sensitivity（SF-4）
7. 8 pairs/cell 的 CI 宽度应在视觉呈现中反映（SF-5）
8. Intervention 的 "64%" 不应以精确数字出现在 abstract（SF-2）
9. "Five families" 计数和 "345M–6.9B" 范围不准确（minor）
10. 页数边界问题需要调整 float placement（minor）

---

## Reviewer Divergence

1. **Novelty 评价** (SF-1)：
   - R2: PermG 直接移植，novelty 天花板限制主会议定位
   - R1: Empirical characterization + pipeline integration 是合理贡献模式，前提是定量结论稳健
   - 综合：novelty 有限是事实，但不是一票否决因素——关键取决于统计基础能否加固

2. **Granger precedence confounding 讨论充分性** (R1-W3)：
   - R1: 讨论不充分，measurement sensitivity 替代解释未充分排除
   - R2: §6 已讨论（"Entropy's greater sensitivity... means the temporal lead may partly reflect measurement sensitivity"）
   - 综合：论文已有讨论但不够显著；不构成 must-fix

---

## Questions

1. 如果 null-condition seeds 增加到 10-20 个，FPR 点估计预期收敛到什么水平？如果仍 >5%，检测边界声称是否需要根本性修改？

2. 能否为 T^{−2.08} 指数报告完整 bootstrap CI？如果覆盖 [−0.5, −2.5]，对 abstract 中的定量表述有何影响？

3. SmolLM3 在 α=1.0 下 0/8 检测——什么解释了完全污染下的检测失败？这是 PermG 的根本局限还是统计功效问题？

4. 能否为至少一个额外架构提供缩减版 α×T grid（如 5α × 3T），以验证 phase-diagram 结构的可迁移性？

5. Data accumulation 设置下 landscape 如何变化？这是否是一个比 full replacement 更现实的场景？

---

## Missing References

- **Runge et al. (2019)** "Detecting and quantifying causal associations in large nonlinear time series datasets." *Science Advances*. — 与本文核心设置（短非线性时间序列中的因果发现）直接相关，PCMCI 算法应在 §2 讨论并解释为何选择线性 PermG。（双方 AGREE）

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（3 warnings, 3 info）：

| 严重度 | 位置 | 发现 |
|--------|------|------|
| ⚠️ warning | pp.6-7 | 实验章节连续 2 页纯文本无 display item，结果与图表分离 |
| ⚠️ warning | p.8 | Figures 3/4/5 三图堆叠同页，每图仅 1/3 页高，图内文字偏小（正文 60-65%） |
| ⚠️ warning | p.9 | Table 1 和 Figure 6 浮动超出 8 页主文边界 |
| ℹ️ info | pp.1-2 | 前 2 页纯文本，Figure 1 在 p.3 出现（合格但非最优） |
| ℹ️ info | p.8 | Tick labels/legend 字号约 60-65%，在可读性边界 |
| ℹ️ info | p.30 | Appendix 最后页 ~35% 空白（不影响评价） |

建议：将至少 1 个 figure 上移至 pp.6-7 改善视觉节奏；调整 float 将 Table 1/Figure 6 拉回 p.8 内。

---

## Overall Assessment

**评分**: 3.5 (Borderline Conference)
**置信度**: 4/5（双方 Reviewer 均熟悉统计方法和 model collapse 文献）

**评分理由**:

论文提出了一个新颖且重要的研究问题（model collapse 的可检测性景观），实验设计严谨（specification curve 1,160 配置、5,000 permutations、multi-seed 复制），方法论透明度出色（对自身局限性的坦诚程度超过同类工作）。方法敏感性发现（同一数据上 5 种方法得出截然不同结论）是最强贡献。

然而，核心定量声称的统计基础存在多处脆弱性：FPR 膨胀（11.1%, CI 上界 30%）使精确边界不可靠；幂律拟合自由度极低（4-5 点拟合 2 参数）；统计功率 CI [0.24, 0.78] 无法区分"不可检测"与"功率不足"。"Detectability landscape" 的宏大 framing 与实际证据范围（单模型完整 grid + 极端条件下的跨架构抽样验证）之间存在落差。跨架构验证暴露 27% 的系统性失败率。

**推荐路径**:
- 如果定量结论的统计基础能显著加固（更多 null seeds 收窄 FPR CI、更多 T 值增加拟合自由度）+ framing 调整为更准确反映单模型范围 → Conference (4.0)
- 当前状态下，方法敏感性 + first-differencing 诊断的实证贡献已达 Findings 水平 → 3.0-3.5
- Novelty 不是决定性障碍（empirical characterization 是合理贡献模式），关键是统计可信度

---

## Detailed Comments

### Abstract
- "345M–6.9B"：实测最大 3B（SmolLM3），6.9B 仅 Pythia-6.9B 一个条件且为 bf16。建议修正为实际范围。
- "five families"：Padding-410M 是 Pythia variant，严格 4 族。建议 "four families plus one architectural variant"。
- "null-control false positive rates from 3% to 92%"：92% 来自 NaiveXCorr（failed baseline）。建议区分或注明。
- "reduces peak perplexity by 64%"：N=2, post-hoc threshold, α=1.0 only。建议替换为定性描述。
- 脚注 1 在 abstract 中不标准，建议移至 §1。

### §3 Cascade Ordering (Design Principles)
- Design Principles 1-2 数学深度有限（Jensen 不等式级别），不构成独立理论贡献。
- 但作为实验设计 motivation 和 canary metric 选择的形式化依据，其角色是合理的。
- 建议：明确定位为"theoretically motivated, empirically validated design principles"而非"theoretical contribution"。

### §4 Method
- PermG FPR=11.1% CI [1.2%, 30.4%] 是全文最关键的统计弱点。建议正文中更显著地讨论其对边界精度的影响。
- β 符号同时用于统计功率和幂律指数，建议区分。
- 幂律拟合应降级为"empirical observation consistent with power-law scaling"而非确认幂律。

### §5 Experiments
- §5.1 sharp onset（0/8→6/8）：统计上显著（Fisher exact p=3.45×10^{-11}），但 CI 宽度意味着相邻 cell 差异不一定显著。建议在正文中注明 6/8 的 CI。
- §5.5 Cross-architecture：4/15 失败率需更审慎措辞。建议表述为 "PermG forward detection reaches ≥6/8 in 11/15 conditions, with four non-confirming conditions isolating distinct failure modes"（论文已有类似表述但 abstract 未反映）。
- §5.6 Intervention：proof-of-concept framing 恰当，但应从 abstract 移除精确数字。

### §6 Discussion
- 已讨论 measurement sensitivity 替代解释（"Entropy's greater sensitivity..."），这是积极的。
- 缺少对 data accumulation paradigm 的讨论——所有实验用 full replacement，Gerstgrasser et al. (2024) 表明 accumulation 可 mitigate collapse，应讨论 landscape 在 accumulation 下的预期变化。
- 单一解码策略：Limitations 已承认，建议补充一句关于结构性改变（非仅平移）的可能性。

### Format
- Table 1 / Figure 6 浮动到 p.9：需调整 float placement 确保 8 页合规。
- pp.6-7 纯文本缺 display item：建议至少 1 figure 上移改善视觉节奏。
- Figure 3-5 tick labels 偏小（~60-65% 正文字号）：建议在布局调整后适当放大。