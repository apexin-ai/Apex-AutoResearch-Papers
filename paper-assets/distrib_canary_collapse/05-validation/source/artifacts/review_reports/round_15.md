---
round: 15
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T07:39:37.318886+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 15 审稿报告 — Distrib Canary Collapse

## Summary

本文研究 iterative model collapse 场景下多种统计检测方法的灵敏度差异，以合成数据替换比例 α 和训练代数 T 为二维参数，构建 "detectability landscape"。核心发现包括：(1) 不同检测方法的 FPR 跨越 14 倍（6.7%–94.4%），方法选择是检测结论变异的首要来源；(2) α≈0.45 附近存在 detection boundary 的 phase transition；(3) α=0.60 存在 non-monotonic detection anomaly。论文提出 MMCT（Multi-Method Consensus Testing）框架进行方法融合，并在 α=1.0 条件下进行了 5 个模型家族的跨架构验证。

## Strengths

**S1. 系统性的多方法比较框架。** 论文在同一数据集上对 5 种检测方法进行系统比较（Section 3.3, Figure 2），1,160 个 specification 的 robustness analysis 揭示了 κ=0.185 的低 inter-method agreement。这种"同一数据、多种方法、量化一致性"的实证设计在 model collapse 文献中尚属首次，为该领域的方法论规范化提供了参考。

**S2. Non-monotonic detection anomaly 的识别与分析。** α=0.60 处的 detection dip（Figure 3, Table 6）超越了简单的 dose-response 单调关系，Section 4.2 和 Appendix K 对其成因（entropy-diversity temporal decoupling）的分析展示了超出参数扫描的结构性发现。

**S3. 方法论警示的实用价值。** NaiveXCorr 的 FPR 高达 94.4%（检出 7-8/8 null pairs）源于 shared trend confounding（Section 3.3），这一 domain-specific 陷阱对从业者有直接的指导意义——大多数 practitioner 会首先尝试简单 cross-correlation，论文提供了明确的反面教材和替代方案（first-differencing, PermG）。

**S4. 实验规模和透明度。** 涵盖 5 个模型家族（345M–6.9B），15 个 model-seed 组合，Appendix 提供了详尽的消融分析（Shapley contribution, weight robustness, power simulation, CUSUM comparison 等），AI 使用披露清晰（page 37，三种使用类别）。

**S5. 写作质量和格式合规。** 论文格式符合 ACL 模板，booktabs 表格规范，LaTeX 无编译错误，Limitations section 覆盖 3 个要点（Scope, Statistical power, Causal interpretation），符合 EMNLP 2026 要求。

## Weaknesses — Must-Fix

**MF1. [共识] 跨架构泛化仅在 α=1.0，landscape 泛化性不足。**
Section 4.5 (Table 1, page 6) 的跨架构验证仅在 α=1.0（全量合成替换）条件下进行，而论文最核心的发现——detection boundary 附近的 phase transition（α≈0.45）——没有任何跨架构验证。4/15 non-confirming 条件（Table 10, page 17）中 SmolLM3-3B 的 entropy decoupling 和 GPT-2 Medium 的 calibration dependency 暗示 landscape 是 architecture-dependent 的。论文标题 "Characterizing the Detectability Landscape" 暗示普适性，但实际上是 Pythia-410M 的 landscape。[R1-N2, R2-N2: 双方 AGREE]

**MF2. [共识] Power-law boundary 拟合严重欠定。**
Section 4.3 的 sigmoid regression 95% CI 为 [0.25, 0.82]，Limitations 自承 γ 的 CI 为 [0.01, 2.10]——跨越两个数量级。3 个自由参数拟合 3-4 个数据点是插值而非回归，对 power-law 的函数形式没有约束力。Appendix Y 的 power simulation 依赖同样的参数化形式，构成循环论证。需要至少 6-8 个 α 水平的数据点才有统计意义。[R1-N1, R2 AGREE]

**MF3. [共识] PermG FPR 6.7% 置信区间过宽，削弱核心结论。**
60 null pairs 下 4/60 = 6.7% 的 exact binomial 95% CI 约为 [1.8%, 16.2%]。CI 上界 16.2% 与 DiffXCorr 的 14.8% 实测 FPR 重叠，使 PermG 相对于 DiffXCorr 的 FPR 优势在统计上不显著。Conclusion 中 "combining the lowest FPR 6.7%" 给出了比数据实际支持的更精确的印象。应在正文中明确报告 CI。[R1-N3, R2 AGREE with nuance——R2 补充点估计 ranking 方向仍有信息价值，但不应作为精确数字使用]

**MF4. [分歧] "Detectability landscape" 概念新颖性。**
R2 认为 phase diagram 本质上是标准 dose-response 参数扫描加 sigmoid 拟合，"landscape" 是术语通胀。R1 部分反驳：multi-method comparison（1,160 specifications, κ=0.185）和 non-monotonic anomaly（α=0.60）超越了标准 dose-response，但同意 "landscape" 术语确实有 inflation，建议改为 "multi-method detection sensitivity profile"。
→ 共识方向：landscape 的概念框架需要降低 claim 强度，但 multi-method comparison 和 non-monotonic finding 是有实质内容的。[R1 REBUT with concessions, R2-N1]

**MF5. [分歧] Method sensitivity 作为 "primary finding" 的定位。**
R2 认为"不同统计检验具有不同 power 和 Type I error"是统计学常识，不构成发现。R1 反驳：14 倍 FPR 差异（6.7%→94.4%）是 domain-specific 实证发现，且 NaiveXCorr 的 shared trend confounding 是 model collapse 时序数据的特有陷阱。但 R1 也同意将此定位为 "primary finding"（Contribution 1）确实偏高，建议降为 "important methodological warning"。
→ 共识方向：FPR 差异幅度有信息价值，但 Contribution 列表应重新排序。[R1 REBUT with concessions, R2-N3]

## Weaknesses — Should-Fix

**SF1. [共识] 3 seeds 不足以估计 seed-level variance。**
Phase diagram 用 3 seeds（Figure 3 caption），3 seeds 的标准差估计服从 2 自由度的 χ² 分布，CI 极宽。Appendix L 的跨 seed 分析也仅 3-4 seeds，无法从根本上改善估计精度。[R1-W1, R2 AGREE]

**SF2. [共识] MMCT 方法论贡献薄弱，增量价值有限。**
Algorithm 1 (page 4) 的 FPR-inverse weighted majority voting 在 ensemble learning 文献中是基本技术。Appendix P Shapley 分析显示 PermG 的 combined Shapley 最接近零（FPR-FNR 最平衡），MMCT 的主要价值是排除高 FPR 方法而非组合互补方法。Table 2 已显示 PermG 单独是最优选择时，MMCT 增量价值有限。w_k = 1/max(FPR_k, ε) 是直觉合理但缺乏理论最优性保证的 ad-hoc 设计。[R1-W2, R2-W1: 双方 AGREE]

**SF3. [共识] Intervention 仅在 α=1.0 验证但占据过多正文篇幅。**
Section 4.6 (page 7) 的 intervention 仅在 α=1.0 验证，但占正文约 0.5 页。Appendix F (CUSUM comparison) 显示在高 α 下 CUSUM 与 canary 方法差异不大，削弱了 canary-based intervention 的独特价值主张。Discussion 的 "deployment recommendations" 超出了单一极端条件的证据支撑。建议正文压缩到 1-2 段，细节移入附录。[R1-W3, R2-W3: 双方 AGREE]

**SF4. [共识] Entropy "leading" 可能是测量分辨率差异的 artifact。**
Appendix J (page 17) 自己承认 entropy 是连续量而 distinct-n 是离散计数，entropy 可以响应任意小的分布变化。这是对 Design Principle 1（entropy precedes diversity）的根本性替代解释，但被放在 appendix 而非 Section 5 Discussion 中。需要：(a) 在 Discussion 中明确讨论此 concern，(b) 对 entropy 进行 discretization 后重新测试 Granger precedence 是否依然成立（论文未做此验证）。[R1-W4, R2-W4: 双方 AGREE]

**SF5. [共识] 缺少 Silberzahn et al. (2018) "Many Analysts, One Data Set"。**
论文的 core finding（method choice as primary variability source）直接回应了 Silberzahn 框架。Section 2 或 Section 3.3 应引用并讨论。[R2-W2, R1 AGREE]

**SF6. [部分共识] 核心内容过度依赖附录。**
R2 认为 Design Principle 推导、方法论比较表等放入附录导致正文不 self-contained。R1 反驳：8 页限制下这是合理选择，但同意正文应增加 1-2 句 intuitive justification（如 Section 3.1 的 Design Principle 缺少直觉解释）。[R1 partial REBUT, R2-W5]

## Reviewer Consensus

| 问题 | R1 | R2 | 共识 |
|------|----|----|------|
| 跨架构仅 α=1.0 | N2 | N2 | **AGREE** — 最高共识 Must-Fix |
| Boundary fitting 欠定 | N1 | AGREE | **AGREE** — 3 参数拟合 3-4 点 = 插值 |
| PermG FPR CI 过宽 | N3 | AGREE | **AGREE** — CI 上界与 DiffXCorr 重叠 |
| 3 seeds 不足 | W1 | AGREE | **AGREE** |
| MMCT 增量价值有限 | W2 | W1 | **AGREE** |
| Intervention 过于初步 | W3 | W3 | **AGREE** |
| Entropy artifact 应在主文讨论 | W4 | W4 | **AGREE** |
| 缺失 Silberzahn (2018) | — | W2 | **AGREE** |
| Table 2 K≥4/K≥5 列冗余 | P1 | AGREE | **AGREE** |
| Figure 1 低值区颜色区分度差 | P2 | AGREE | **AGREE** |
| Design Principle 正文缺中间推导 | P3 | AGREE | **AGREE** |
| PermG direction checking 正文不足 | P4 | AGREE | **AGREE** |

## Reviewer Divergence

| 问题 | R1 立场 | R2 立场 | 分歧性质 |
|------|---------|---------|----------|
| Landscape = dose-response? | REBUT — multi-method + non-monotonic 超越 dose-response，但同意术语 inflation | N1 — 本质是参数扫描 rebranding | 程度分歧：方向一致（需降低 claim），程度不同 |
| Method sensitivity 新颖性 | REBUT — 14x FPR 差异是 domain-specific 发现 | N3 — 统计学常识 | 程度分歧：R1 认为有实证价值但 framing 偏高 |
| 附录依赖 | partial REBUT — 页面约束下合理 | W5 — 正文不 self-contained | 程度分歧：R1 主张结构合理但需增加直觉解释 |
| AI disclosure 详细度 | P5 — 不够详细 | REBUT — page 37 已充分 | 事实分歧：R2 指出 page 37 已列出三种使用类别 |

## Questions

**Q1.** 如果在 GPT-2 Medium 或 SmolLM3-3B 上做 α∈{0.25, 0.50, 0.75} 的完整扫描，phase boundary 位置是否与 Pythia-410M 的 α≈0.45 一致？如果不一致，论文的定量 claim 需要如何重写？

**Q2.** 排除 NaiveXCorr 后，specification curve 的 κ 值是多少？如果显著提高，method sensitivity 的 claim 是否需要重新校准？

**Q3.** 对 entropy 进行 discretization（如 binning 到与 distinct-n 相同的分辨率）后重新运行 Granger precedence test，Design Principle 1 是否仍然成立？

**Q4.** 能否提供 MMCT 确实优于单独使用 PermG 的具体场景？如果没有这样的场景，MMCT 的方法论 claim 是否应该降级？

## Missing References

1. **Silberzahn et al. (2018)** "Many Analysts, One Data Set: Making Transparent How Variations in Analytic Choices Affect Results" — 多方法/多分析者范式的奠基性工作，论文的 method sensitivity finding 直接回应此框架。[R1 AGREE, R2 AGREE] **应引用。**

2. **Kirchenbauer et al. (2023)** "A Watermark for Large Language Models" — watermarking 作为 proactive detection 的替代范式，与本文的 reactive distributional detection 形成方法论区分。Related Work 应简要讨论两者的差异。[R2 AGREE] **应引用。**

3. DetectGPT (Mitchell et al., 2023) — R1 指出问题设定完全不同（per-text classification vs. distributional detection on time series），论文已在 Section 2.2 划清边界。**非必须。**

4. MMD / Gretton et al. (2012) — R1 指出 MMD 在本文 time-series lead-lag 设定中的适用性不明确。**非必须。**

## External Review (Stanford Agentic Reviewer)

未请求外部审稿。

## Visual Layout Check（非评分项）

视觉审查已完成。0 critical / 7 warnings / 9 info。

**Warnings:**
1. **Page 2**: Figure 1 phase diagram 单元格数字标注字号偏小；红-橙-黄-绿渐变对红绿色盲不友好，建议 viridis/Okabe-Ito 色板
2. **Page 5**: 单页 3 个 display items（Figure 3 + Figure 4 + Table 1），Figure 4 子面板轴标签约正文字号 50-60%，低于 70% 可读性阈值
3. **Page 6**: 单页 3 个 figures（Figure 5-7），视觉压缩严重
4. **Page 7**: Figure 8 条形图 y 轴模型名称字号偏小
5. **Page 20**: Figure 14 占 75% 页面，底部 25% 空白
6. **Page 24**: Figures 16-17 后底部 30% 空白
7. **Page 37**: 最后一页仅 ~6 行文字，底部 85% 空白

**Info highlights:**
- 首页无视觉锚点（建议非必须）
- 正文 12 个 display items 略高于 8 页典型 5-8 个；Figure 3 与 Figure 7 信息重叠可考虑合并
- Limitations 覆盖 3 点，篇幅适中，符合 EMNLP 2026
- 表格 booktabs 规范，公式正确，无 margin 溢出，References 统一

## Overall Assessment

**评分：3.0 (Findings)**

**置信度：High**

R1 给出 3.5（Borderline Conference），R2 给出 3.0（Findings）。差异来自对 "detectability landscape" 概念新颖性的评估——R2 认为即使修复拟合和泛化问题，landscape 的概念新颖性仍有限（本质是 dose-response rebranding），R1 认为 multi-method comparison 增加了超越 dose-response 的价值。

综合评估采用 3.0，理由：

1. **泛化性缺陷是根本性的。** 跨架构验证仅在 α=1.0（双方最高共识 Must-Fix），标题承诺的 "landscape characterization" 实际仅基于 Pythia-410M。需要额外实验而非仅修改写作。

2. **统计精度不足以支撑定量 claim。** Boundary fitting 欠定（3 参数 / 3-4 点）、PermG FPR CI 过宽（[1.8%, 16.2%]）、3 seeds 的 variance 估计——共同使得定量结论（"α_c ≈ 0.45"、"FPR = 6.7%"）的 precision 远低于呈现方式所暗示的。

3. **MMCT 方法论贡献薄弱。** 在 PermG 已是最优单方法的情况下，MMCT 的增量价值缺乏证据支持，且缺乏理论最优性保证。

4. **实证发现有真正价值。** 14 倍 FPR 差异的定量化、NaiveXCorr 的 shared trend confounding 警示、α=0.60 non-monotonic anomaly——这些是 genuine contributions，适合 Findings 收录。

**ARR 评分对照：Overall Assessment = 3 (Findings)** — 可被 Findings 接收，但需显著修改 framing 和补充跨架构实验后才能考虑主会议。

## Detailed Comments

### Section 1 — Introduction
- "Characterizing the Detectability Landscape" 标题暗示普适性，与实际仅基于 Pythia-410M 的证据不匹配
- Contribution 列表应重新排序：method sensitivity 从 Contribution 1 降为 methodological warning，landscape characterization 需加 scope qualifier

### Section 2 — Related Work
- 缺少 Silberzahn et al. (2018) 和 Kirchenbauer et al. (2023) 的讨论
- 与 Schaeffer et al. (2025) "8 种 collapse 定义" 的映射应更明确

### Section 3 — Method
- Design Principle 1 和 2 的 formal statement 使用信息论语言但 operationalization 跳转到具体 metrics 时缺少中间推导（仅引用 Appendix，主文无直觉解释）
- MMCT Algorithm 1 的 FPR-inverse weighting 缺乏理论依据，Appendix Q "对 ad-hoc 选择不敏感" ≠ "有理论依据"
- PermG direction checking 描述不足（Appendix G 有详细描述，但 Section 3.3 缺关键细节）

### Section 4 — Experiments
- Phase diagram boundary fitting：需要更多数据点（建议 ≥6 个 α 水平），当前 CI 过宽
- Cross-architecture：Table 1 仅 α=1.0，需要至少 α∈{0.50, 0.75} 的验证
- Intervention：正文篇幅应压缩，证据仅支持 proof-of-concept 定位
- Table 2 的 K≥4 和 K≥5 列全为 0%，可删除或合并为脚注
- α=0.60 non-monotonic anomaly 是有价值的发现，建议给予更多正文空间

### Section 5 — Discussion
- Entropy artifact（测量分辨率 vs. 因果 precedence）应从 Appendix J 提升到 Discussion
- Design Principle 1 的因果叙事需要弱化，或提供 discretized entropy 的验证

### Section 6 — Conclusion
- "combining the lowest FPR 6.7%" 应改为包含 CI 的表述
- Cross-architecture generalization claim 需加 "at α=1.0" qualifier

### Limitations
- 当前 3 个点的覆盖适当，建议增加对 MMCT 增量价值有限的 honest assessment

### Appendix
- 内容全面，但部分关键验证（entropy artifact, PermG FPR CI）应在正文中有显式引用和简要讨论
- Figure 子图内文字偏小问题（Page 5 Figure 4, Page 7 Figure 8）仍存在