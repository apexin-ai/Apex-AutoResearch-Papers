---
round: 8
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-22T05:36:50.065185+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 8 审稿报告（修正版）

> **修正说明**：本报告替代首次提交版本。R1 在交叉回应中发现 R2 存在三处事实性错误——Fehlauer et al. (2025)、Watson-Daniels et al. (2023)、Hsu & Calmon (2022) 三篇论文实际上均已在 §2 Related Work 中被引用（经验证属实）。首次报告中的 MF4（遗漏 Fehlauer）和 SF4（补充 Watson-Daniels/Hsu）已撤回。Missing References 部分已更正为"无遗漏"。其余评估不变。

**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
**Venue**: EMNLP 2026 (ARR May 2026 cycle, Long Paper)
**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）
**交叉分享**: 完成（R1→R2, R2→R1）。R2 对 R1 的回应：12/14 [AGREE]，2 [REBUT]。R1 对 R2 的回应：9/14 [AGREE]（含 nuance），3 [REBUT]（W4/N2 Fehlauer 已引用, W5 Abstract 密度是写作偏好, W7/SF-W3 Watson-Daniels+Hsu 已引用），2 部分同意。
**审稿轮次**: 1 轮收敛（无需 Round 2）

---

## Summary

本文利用 Wang et al. (2025) 的 controlled model zoo（3 hybrid linear recurrent 架构 × 5 attention ratios × 2 scales = 30 配置），在 10 个 benchmark 上分析 attention 对跨架构 per-example 行为的影响。核心发现：(1) per-example predictive multiplicity 随 task 类型变化（α = 0.14–0.30），Jaccard 始终低于 0.10；(2) aggregate convergence 仅在 LAMBADA 上有初步证据（Bonferroni-adjusted p = .100）；(3) aggregate convergence 与 per-example divergence 存在 decoupling。论文定位为经验性分析，将已有 multiplicity 框架应用于 hybrid recurrent 架构。

## Strengths

1. **控制变量实验设计**：统一 training data / tokenizer / hyperparameters 的 model zoo，仅变化 architecture 和 attention ratio，是隔离 architectural effects 的 gold standard approach（§3.1）
2. **诚实的统计报告**：convergence claims 全部标注 "suggestive"/"preliminary"，Bootstrap CI 明确为 "heuristic indicators"，formal inference 基于 exact permutation test（§3.5, §4.1）
3. **核心发现扎实**：per-example multiplicity（α = 0.14–0.30, Jaccard ≤ 0.10）由描述性统计直接支持，不依赖争议性假设检验（§4.2, Table 2）
4. **多层次证据结构**：从 aggregate metrics（σ, ρ）→ per-example decomposition → cross-architecture Jaccard → confidence margin mechanism（Cohen's d），分析层次递进（§4.1–4.3）
5. **Normalized effect size 分析**：排除了 Jaccard floor effect 的替代解释——observed J ≈ 0.10 vs. J_max = 0.78–0.92，仅 5–7% achievable range（§4.2, Appendix K）
6. **Ensemble POC 增加实用性**：majority vote vs. oracle analysis 量化了 multiplicity 的 structural cost（§5）
7. **极其详尽的敏感性分析**：Appendix 覆盖 GDN 排除、cross-scale、bootstrap CI 细节、normalized ES、subsample 稳定性等，远超同类论文常规水平
8. **Related Work 覆盖全面**：Fehlauer et al. (2025)、Watson-Daniels et al. (2023)、Hsu & Calmon (2022)、Swayamdipta et al. (2020)、Cooper et al. (2024)、Black et al. (2022) 等 multiplicity/underspecification 领域关键文献均已引用
9. **Reproducibility 良好**：基于公开 model zoo，方法描述详细，统计程序清楚

## Weaknesses

### Must-Fix（影响接收决定）

**MF1 [Critical, R1-N1+R2-N1 共识]: Bonferroni 显著性在当前设计下结构性不可达，但论文将 convergence 和 decoupling 列为核心 contributions**

n = 5 attention ratios 的 exact permutation test 中，两尾最小可达 p = 2/120 = 0.0167。经 6 个 confirmatory benchmarks Bonferroni 校正后，adjusted p = 0.100——**无论观测到多极端的结果，当前设计永远无法达到常规显著性**。这不是 power 不足（可通过增大样本改善），而是设计的结构性天花板。

Contribution 2（task-specific convergence）和 Contribution 3（decoupling formalization）均建立在此不可达的显著性之上。论文用大量篇幅（§4.1, §4.3, §4.4, Appendix B–D）展开一个自身方法论无法在常规阈值下支持的发现，contribution 列表的权重分配与证据强度不匹配。

建议（R1 方案，R2 同意）：将 Contribution 2 & 3 降级为 secondary observations（保留概念区分）或合并为单一 suggestive finding，将论文叙事重心完全转移到 per-example multiplicity（Contribution 1）。

**MF2 [Critical, R1-N2+R2-W3 共识]: Decoupling 形式化（Equation 1）存在技术问题**

三个子问题：
1. **Condition (i) 的 brittleness**：要求精确值 ρ = −1.0——n=5 离散排名中任何微小扰动即失败。未讨论 "近似 decoupling" 阈值，限制了该定义对未来研究的可用性。
2. **Condition (ii) 缺乏区分力**：n = 3 的 bootstrap CI 必然很宽（论文自述 heuristic）。如果 Jaccard 呈单调递增趋势（即不存在 decoupling），宽 CI 是否也导致 condition (ii) 被满足？论文未论证。如果 condition (ii) 在任何趋势下都成立，它就是 vacuously true。
3. **唯一拟合案例**：Equation 1 精确拟合 LAMBADA——唯一满足条件的 benchmark。无泛化案例，难以判断是有用抽象还是 post-hoc 描述。

R2 建议保留定性描述、弱化形式化。R1 建议报告 CI 宽度并论证区分力。

**MF3 [Critical, R1-N1 发现, R2 AGREE]: Limitations 中 p 值事实性错误**

Limitations 称 "the minimum achievable two-tailed p-value is approximately 0.008"——这是事实性错误。1/120 ≈ 0.008 是**单尾**最小值；两尾最小值为 2/120 ≈ 0.017。Table 1 中 LAMBADA p = .017 是正确的，说明实际计算无误，但文字表述需修正。

### Should-Fix（影响评分但不一票否决）

**SF1 [Major, R1-W1+R2-W1 共识]: 单次训练运行的 confound 仍未充分讨论**

所有 30 个配置均为单次训练。R1 指出一个此前未明确的精确问题：within-arch Jaccard ≈ 0.33 不是 seed baseline——它包含 attention ratio variation 的效应（within-arch 比较改变了模型结构）。真正的 seed baseline（相同架构 + 相同 ratio + 不同 seed）在数据中不存在。3× gap 的归因精度无法确定。

建议：Limitations 中更明确说明 within-arch Jaccard 不等于 seed baseline；Abstract 增加 single-run caveat。

**SF2 [Major, R1-W2+R2-W2 共识]: LAMBADA convergence 依赖于 GDN**

移除 GDN（存在 16-head confound）后，ρ 从 −1.0 降至 −0.7（p = .233）——convergence 完全不显著。§4.4 的 "partially dependent on GDN" 低估了实际情况。Decoupling 的 condition (i) 依赖 convergence，因此 decoupling 也连带失效。建议措辞改为 "dependent on GDN inclusion"。

**SF3 [Warning, R2-W6+R1 部分 AGREE]: Ensemble POC 负面结果与 practical protocol 的 tension**

Majority vote 不如最佳单模型（LAMBADA −0.2pp, ARC-Easy −1.1pp），但论文随后建议 per-example audit 指导 deployment。R1 补充：三条建议是**诊断性**的（不是 ensemble 方法），majority vote 失败恰恰 motivate per-example-aware selection。但 confidence-margin screening 作为建议被提出却未验证预测准确性。需更明确讨论 negative ensemble result 与 positive diagnosis 之间的关系。

### Minor（不影响接收）

**M1 [R2-W5, R1 部分 REBUT]**: Abstract 统计量密度。R2 建议删减，R1 认为具体数字是 empirical paper 的 contribution 本身——未达成共识。如果要减少密度，建议仅移除 79%（σ reduction percentage），保留其余数字。
**M2 [R1-W3, R2 AGREE]**: Binary decomposition 在多选题 benchmarks 上信息损失更大——Cohen's d 仅覆盖 LAMBADA，多选题 effect size 更弱（Appendix O）。已有 continuous analysis 在 Appendix，但主文未充分引用。
**M3 [R1-W4, R2 AGREE]**: "rescue"/"disruption" 是因果性语言但分析为 observational comparison。建议加一句 clarification。
**M4 [Visual check]**: 连续 3 页（pp.3–5）无 display item，Table 1 到 p.6 才出现。建议将 Table 1 或 summary figure 提前。
**M5 [Visual check]**: 主文 display item 总数偏低（4 个）。建议提升 1–2 个关键 appendix 表格至主文。

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成完全共识：

1. **Contribution 1 是最有力的发现**：per-example multiplicity 的 task-dependent variation（α = 0.14–0.30, Jaccard ≤ 0.10）由描述性统计直接支持，不依赖争议性假设检验
2. **Contribution 2 & 3 的统计基础不够 robust**：Bonferroni 显著性结构性不可达，收敛依赖 GDN，decoupling 形式化可能缺乏区分力——应降级或合并
3. **Overall 3.0（Findings）**：适合 Findings 发表，不足以支撑主会议
4. **单次训练运行是根本性限制**：within-arch Jaccard 不是纯 seed baseline
5. **Limitations 中 0.008 是事实性错误**：应修正为 0.017
6. **论文写作诚实透明**：对统计局限的标注是负责任的学术态度
7. **Related Work 覆盖全面**：R1 交叉验证确认 R2 指出的三篇"遗漏"文献实际均已被引用

## Reviewer Divergence

分歧均为非根本性：

1. **Contribution 2 & 3 的处理方式**：R1 建议保留概念区分但降级为 secondary observations；R2 建议直接合并为一个 contribution。效果等价，具体形式由作者决定。
2. **Abstract 统计量密度** [R2-W5 vs R1-REBUT]：R2 认为数字过多，R1 认为具体数字恰恰是 empirical contribution 本身。写作偏好问题。
3. **Normalized ES 5–7% 的解读** [R1-Q5 vs R2-REBUT]：R1 认为低比例可能说明 per-example divergence 实际规模小；R2 认为低 ES 支持 non-overlap claim（接近 chance level = 近乎不重叠）。两种解读均合理，论文应更明确区分 divergence 的覆盖面（α）vs 独特性（Jaccard/ES）。
4. **Oracle-selected ensemble** [R1-Q4 vs R2-REBUT]：R1 建议基于 α/Jaccard 的 oracle selection，R2 认为在 deployment 时不可用——论文的 confidence-based routing 建议更现实。

## Questions

1. Limitations 称两尾最小 p ≈ 0.008，但 Table 1 LAMBADA p = .017——请确认是否为笔误？（R1-Q1, R2 AGREE）
2. Equation 1 condition (ii) 的 bootstrap CI 在各 attention ratio 下宽度是多少？如果 Jaccard 呈单调递增（non-decoupled scenario），宽 CI 是否仍满足 overlap 条件？请论证 discriminative power。（R1-Q2, R2 AGREE）
3. Appendix F 用 attention weight cosine similarity（0.995）论证分歧源于 recurrent layers。但 aggregate weight similarity 不保证特定 example 上 attention 行为相同。是否可在 divergent examples 上计算 attention output similarity？（R1-Q3, R2 AGREE）
4. ρ_α = −0.1（LAMBADA）意味着 multiplicity magnitude 与 attention dose 几乎无关，如何与 convergence（aggregate σ 递减）调和？R1 解释：α 和 σ 测量不同量——同比例 example 被影响但架构间 aggregate 趋于一致（per-example 分歧在 aggregate 层面相互抵消），这正是 decoupling 的操作定义。建议在正文中更明确阐述。（R2-Q3, R1 回应）
5. 三个架构的 recurrent backbone 差异是否在 per-example effect 中表现出可解释的 pattern？§4.2 的 confidence margin 分析是否可按架构分解？（R2-Q4, R1 认为超出当前工具范围但合理 future direction）
6. 是否考虑过用 option probability margin 来获得 continuous per-example divergence measure？（R2-Q2, R1 AGREE）

## Missing References

**无遗漏。** R2 初审指出 Fehlauer et al. (2025)、Watson-Daniels et al. (2023)、Hsu & Calmon (2022) 三篇遗漏，但 R1 交叉验证确认三篇均已在 §2 Related Work 中被引用（§2 line: "the four-phase convergence pattern of autoregressive LMs \citep{fehlauer2025convergence}"；"extensions address probabilistic classification \citep{watson2023predictive}, Rashomon capacity \citep{hsu2022rashomon}"）。前轮补充的 Swayamdipta et al. (2020)、Fu et al. (2023)、Cooper et al. (2024)、Black et al. (2022) 也均已存在。

## External Review

外部审稿未配置（项目配置中无 `external_review.paperreview_ai.enabled`）。

## Visual Layout Check（非评分项）

状态：**已完成**（0 critical, 1 warning, 8 info）

主要发现：
- **[Warning]** Pages 3–5 连续 3 页无 display item（Related Work → Method → Results §4.1 开头）。第一个结果表 Table 1 到 page 6 才出现。建议将 Table 1 或 summary figure 提前至 page 4–5。
- **[Info]** 主文 display item 总数偏低（4 个），大量定量证据推入 appendix。建议提升 1–2 个关键 appendix 表格至主文。
- **[Info]** Figure 2 内部文字字号偏小，接近可读性下限。
- **[Info]** Table 1 脚注标记（†, ‡）密集。
- **[Info]** Figure 1 双面板颜色方案良好（线型+颜色双编码），低 attention ratio 区域线条重叠略密。
- **[Info]** 参考文献格式统一，无 [?] 未解析引用。

## Overall Assessment

**Overall Score: 3.0 — Findings**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3/5 | 3/5 |
| Excitement | 2.5/5 | 2.5/5 | 2.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**总体判断**：论文的核心贡献——记录 hybrid linear recurrent 架构中 task-dependent 的 per-example predictive multiplicity（α = 0.14–0.30, Jaccard ≤ 0.10）——是扎实的经验性发现，由描述性统计直接支持，适合 **EMNLP 2026 Findings** 发表。

论文两个更具辨识度的 contributions（LAMBADA convergence 和 decoupling formalization）存在根本性的统计功效限制：Bonferroni 显著性在 n = 5 设计下结构性不可达，convergence 依赖于有 confound 的 GDN，decoupling 的 CI-overlap condition 可能缺乏区分力。单次训练 run 的设计进一步限制了因果归因。Limitations 中存在一个 p 值事实性错误（0.008 → 0.017）需修正。

论文对自身局限的诚实标注、极其详尽的附录（18 页）、全面的 Related Work 覆盖值得肯定——在经验性分析论文中达到了较高的工艺水准。但数据能支撑的结论与作为 contribution 呈现的内容之间仍存在 gap，不足以支撑 Conference 接收。

**接收建议**：Findings，需完成以下修改：
1. **[Must-Fix]** 修正 Limitations 中 p 值错误（0.008 → 0.017）
2. **[Must-Fix]** 降级/合并 Contribution 2 & 3 为 secondary observations
3. **[Must-Fix]** 论证 Equation 1 condition (ii) 的区分力，或弱化形式化
4. **[Should-Fix]** Limitations 中明确 within-arch Jaccard 0.33 不是 seed baseline；Abstract 加 single-run caveat
5. **[Should-Fix]** §4.4 将 "partially dependent on GDN" 改为 "dependent on GDN inclusion"
6. **[Should-Fix]** Conclusion 中更明确讨论 ensemble POC negative result 与 practical protocol 的关系

## Detailed Comments

### §1 Introduction
- Contribution 1 表述清晰，是最有力的贡献
- Contribution 2 & 3 应降级或合并。R1 建议保留概念区分但标注为 secondary；R2 建议直接合并。具体形式由作者决定。
- "not addressable by seed averaging" 已修改为 hedged 形式（"though we cannot fully disentangle the two"）——恰当。但 Abstract 中仍缺 single-run caveat。
- Figure 1 是有效的 hero figure，decoupling 的视觉展示直观

### §2 Related Work
- 覆盖全面：Fehlauer et al. (2025)、Watson-Daniels et al. (2023)、Hsu & Calmon (2022)、Swayamdipta et al. (2020)、Cooper et al. (2024)、Black et al. (2022) 等关键文献均已引用
- Swayamdipta 的 differentiation（training dynamics vs. deployment-time analysis）已存在

### §3 Method
- §3.1 Model Zoo 描述清晰完整
- §3.4 Per-Example Decomposition 的 binary limitation 已有 Cohen's d 交叉验证（LAMBADA d = 0.73–0.92），多选题 benchmarks 的 continuous analysis 在 Appendix
- §3.5 Bootstrap CI 的 heuristic caveat 恰当

### §4 Experiments
- §4.1 Task-Specific Convergence：LAMBADA convergence 标注为 "suggestive"——但作为 numbered contribution 的呈现仍暗示更强。Table 1 GDN 脚注 (‡) 存在。
- §4.2 Per-Example Divergence：核心分析扎实。"rescue"/"disruption" 措辞建议加 clarification。
- §4.3 Decoupling：定性观察有价值，但 Equation 1 存在三重技术问题（brittleness, discriminative power, single-case fit）。
- §4.4 Robustness："partially dependent on GDN" 应改为 "dependent on GDN inclusion"，并明确 decoupling 同样依赖 GDN。

### §5 Conclusion
- Practical protocol 三条建议合理但需连接 ensemble POC 负面结果
- Ensemble 分析（majority vote + oracle）是有价值的补充，量化了 structural cost

### Limitations
- 三段覆盖 Coverage / Methodological constraints / Pre-training only，结构合理
- **必须修正**："minimum achievable two-tailed p-value is approximately 0.008" → 0.017
- 建议在 Methodological constraints 中更明确说明 within-arch Jaccard 0.33 不是 seed baseline

### Appendix
- 极其详尽（18 页），远超同类论文。Cross-scale comparison、GDN sensitivity、normalized ES、subsample stability 等全面
- 建议将 1–2 个关键表格（如 cross-scale comparison Table 12）提升至主文以增加 evidence 密度

### 审稿过程说明
- R2 在初审中将 Fehlauer et al. (2025) 列为 Critical Must-Fix（遗漏引用），并将 Watson-Daniels et al. (2023) 和 Hsu & Calmon (2022) 列为 Should-Fix。R1 在交叉回应中验证论文原文，确认三篇均已在 §2 中被引用。本修正版报告已撤回这些不实指控。这一事件不影响 R2 其余方法论评估的有效性。