---
round: 9
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-22T06:07:25.418244+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 9 审稿报告（Fresh Review）

**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
**Venue**: EMNLP 2026 via ARR May | Long Paper | Deadline 2026-05-25
**Reviewers**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 格式合规）
**审稿模式**: Fresh（无前轮记忆）

---

## Summary

本文利用 Wang et al. (2025) 的 controlled model zoo（3 种 hybrid linear recurrent architectures × 5 attention ratios × 2 scales = 30 configurations），在 10 个 benchmark 上系统分析 per-example predictive multiplicity。核心发现：(1) per-example ambiguity α 随 task type 变化（0.14–0.30），与 attention dose 无关；(2) 仅 LAMBADA 显示 aggregate convergence 的 suggestive evidence（Bonferroni-adjusted p = .100）；(3) 在 LAMBADA 上，aggregate σ 随 attention 递减但 per-example Jaccard 在首个 attention level 即饱和（decoupling 现象）。

---

## Strengths

1. **问题选择及时且实践相关**：随着 hybrid recurrent architectures 日益普及，理解 per-example 行为差异对模型选型和 deployment 至关重要。[R1 S1, R2 S1]

2. **实验设计利用 controlled model zoo 有效隔离变量**：共享 training data、tokenizer、hyperparameters，仅变化 architecture 和 attention ratio。[R1 S2, R2 S2]

3. **统计方法选择总体恰当**：exact permutation test（n=5）、BCa bootstrap、Bonferroni correction、非参数检验的组合使用体现统计意识。[R1 S3, R2 S3]

4. **分析全面性和透明度突出**：18 个附录覆盖 sensitivity analysis、robustness checks、cross-scale comparison、attention weight analysis 等，读者可独立验证 claims。[R1 S2, R2 S4]

5. **对自身局限性的坦诚度高于平均水平**：明确承认 bootstrap CIs 是 heuristic、convergence 是 suggestive、单次训练无法 disentangle architecture vs seed。[R1 S4, R2 S6]

6. **Decoupling 发现是最有说服力的贡献**：aggregate σ 下降 + Jaccard 饱和在低水平，且不依赖 GDN inclusion（§4.4），有 permutation test 支撑（p < .0001）。[R1 S5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1 [Critical]: 架构效应 vs 种子效应无法区分——单次训练 confound** [R1-N1 + R2-N1, 交叉 AGREE]
- 每个配置仅一次训练。论文核心 claim 是 "不同架构影响不同 example 子集"（low Jaccard），但无法排除 seed variation 的贡献。
- 论文引用的 3× Jaccard gap（cross-arch ≈ 0.095 vs within-arch ≈ 0.33）作为 proxy evidence 不充分：within-architecture 比较改变的是 attention ratio 而非 seed，两端变量不同，gap 不可直接解读为 "architecture > seed"。
- Appendix K permutation test（p < .0001）的 baseline 是对 example identity 的 random permutation，非 seed variation baseline。
- **两位 Reviewer 独立提出并在交叉中完全一致**：blocking issue。
- **建议**：(a) 从 McCoy et al. (2020) / Sellam et al. (2022) / Fehlauer et al. (2025) 已发表数据提取 seed-level Jaccard 或 per-example disagreement rate 作为 calibration 参考；(b) 或补充 1-2 配置的 multi-seed 训练（哪怕只有 h3-1 at 1.3B）；(c) 若均不可行，正文（非仅 Limitations）显著弱化因果表述，从 "architecture-driven multiplicity" 调整为 "multiplicity observed across architectures under fixed zoo conditions"。

**MF2 [Critical]: LAMBADA convergence 统计脆弱且依赖 GDN inclusion** [R1-N2 + R2-N2 部分, 交叉 AGREE]
- Bonferroni-adjusted p = .100（未达 α = .05）
- 排除 confounded GDN（16-head vs 32-head confound）后，ρ 从 -1.0 降至 -0.7，p = .233——完全不显著
- 10 个 benchmark 中仅此一个显示 monotonic convergence pattern
- Conclusion 和 Abstract 的表述力度仍强于证据支持——"suggestive evidence" 可能仍过强，应定位为 "exploratory observation"
- **建议**：(a) Abstract/Introduction 中明确标注 convergence 依赖 GDN inclusion 并报告 excluding-GDN ρ 和 p；(b) 降低表述力度；(c) 将 LAMBADA 特殊性（唯一 open-ended retrieval task）作为 mechanistic hypothesis 深入讨论。

### Should-Fix（影响评分但不一票否决）

**SF1 [Major]: Confirmatory/exploratory benchmark split 缺乏 pre-registration** [R1-W1, R2 AGREE]
- 论文承认 "no external timestamp exists"。选择哪些 benchmark 进入 confirmatory set 可能已受数据影响。
- 对全部 10 个 benchmark 做 Bonferroni，LAMBADA adj-p = 0.17（更不显著）。
- **建议**：报告 10-benchmark Bonferroni 作 sensitivity check；考虑 BH (FDR) 作 alternative。

**SF2 [Major]: 缺少与 seed-driven multiplicity 的 quantitative comparison** [R2-W2, R1 AGREE strongly]
- 论文在 Related Work 引用了 McCoy (2020)、Fehlauer (2025)、Sellam (2022) 但仅做 qualitative 讨论。
- 读者无法判断 architecture-driven α = 0.14–0.30 相比 seed-driven per-example disagreement 有多大。
- **建议**：至少从已发表文献提取 seed-driven 数值进行 contextual comparison（无需额外训练）。

**SF3 [Major]: Binary decomposition 信息损失** [R1-W4, R2 AGREE with nuance]
- Helped/hurt/unchanged 丢弃 confidence margin 的连续信息。
- Appendix I normalized ES < 0.10；near-zero Cohen's d 可能反映 binary 分辨力不足而非真实 effect 小。
- R2 补充：binary 是 Jaccard 分析的自然选择，但 continuous confidence shift 作为补充分析有价值。
- **建议**：报告基于 continuous confidence margins 的 cross-architecture similarity（如 Pearson/Spearman on per-example Δprobability），与 Jaccard 结果对比。

**SF4 [Major]: 新颖性定位需更 honest 的 framing** [R2-W1, R1 AGREE]
- α、Jaccard、helped/hurt decomposition 均为现有工具的直接应用。McCoy et al. (2020) 已在 seed-driven 设置下做了类似 per-example divergence 分析。
- 许多发现在 predictive multiplicity 文献框架下先验上不令人意外。
- 真正 non-trivial 的 decoupling 发现恰恰是统计上最脆弱的。
- **建议**：更诚实地定位核心贡献为 "首次对 hybrid recurrent architectures 进行系统的 per-example 分析" 这一 empirical contribution，突出真正 unexpected 的发现。

**SF5 [Minor-Major]: Decoupling "saturation" 缺乏形式化定义** [R1-W5, R2 AGREE]
- "Saturates at first attention level" 无 plateau detection test / change-point analysis。
- 可能只是 floor effect（J ≈ 0.095 已接近 random baseline，无下降空间）。
- **建议**：补充各 attention level 间 Jaccard 的 pairwise comparison 和 trend test；讨论 floor effect alternative。

**SF6 [Major]: Bootstrap CI 覆盖率问题** [R1-W3, R2 AGREE]
- n=3 architectures 的 BCa bootstrap 最多 27 唯一 resamples，coverage 远低于名义 95%。
- §4.1 引用 "BCa 95% CI [-1.0, -0.7]" 未附 heuristic caveat。
- **建议**：每次引用 CI 时附 "heuristic" 标注，或在 Table 1 脚注统一说明。

### Minor Issues

1. **Abstract 信息密度过高**（α 从 0.14 逐项列到 0.30）——建议高层概括如 "varies 2× across tasks" [R2 m1, R1 AGREE]
2. **Appendix F.2 attention entropy null result 应在主文更显著讨论**——GDN ΔH = -0.0009, HGRN2 +0.0020，说明 attention mechanism 对 per-example effects 解释力有限 [R2 m5, R1 AGREE]
3. **Table 1 LAMBADA Cohen's d = 2.41 异常高**——需讨论是否因 σ 特别小导致 d 膨胀 [R1-M1]
4. **§3.4 "correct" 定义应明确**——argmax-based binary，对 LAMBADA open-ended task 尤其重要 [R1-M2]
5. **Appendix R α estimation stability 应在主文引用** [R1-M3]
6. **部分 arXiv 引用如已有正式 venue 版本应更新** [R2 m4]
7. **Practical guidance 不足**——Conclusion 提到 "concrete protocol" 但内容有限；不过在 seed confound 解决前，过早给实践指导可能误导 [R2-W4, R1 AGREE as Minor]

---

## Reviewer Consensus [AGREE]

1. **Overall 3.0 (Findings)**——两位独立评分完全一致
2. **Seed confound 是 #1 blocking issue**——独立提出 + 交叉完全 AGREE
3. **LAMBADA convergence 统计脆弱**——共识应降为 exploratory observation
4. **Decoupling 是最强贡献**——不依赖 GDN、有 permutation test 支撑
5. **分析全面性和 limitation 坦诚度优于平均**——18 附录、统计方法选择恰当
6. **Binary decomposition 有信息损失**——需连续 measure 补充
7. **Bootstrap CI 需更谨慎表述**——heuristic qualifier 应统一附加
8. **新颖性有限但 empirical contribution 有价值**——Findings track 合适
9. **缺少与 seed-driven multiplicity 的 quantitative comparison**——阻碍读者评估实际 effect size

## Reviewer Divergence [REBUT]

1. **Format confound (R1-W2)**：R1 认为 α 差异可能由评估格式（open-ended vs 2-choice vs 4-choice）而非 task type 驱动，标为 Major。R2 REBUT 并提供数据反驳：ARC-Easy（4-choice）α=0.21 介于 LAMBADA 和 PIQA 之间，不按 choice 数排列；BoolQ 和 PIQA 同为 2-choice 但 pattern 完全不同。R2 论证 task type 是更可能的 driver。**Director 判断**：R2 的反驳有数据支持，format 不是 α 的主要 driver，但补充 format × task type 交叉分析仍有增量价值。此项降为 Minor 建议。

2. **PM 概念适用性 (R2-W3)**：R2 认为跨架构比较称为 "predictive multiplicity" 可能引起概念混淆，标为 Minor-Major。R1 REBUT：Marx (2020) 原始定义未限定 same hypothesis class；model zoo 中模型共享 training data 是 canonical PM setting。**Director 判断**：R1 反驳成立，非实质性问题，可加一句脚注 clarify。

3. **Decoupling generalizability severity**：R2 标为 Critical（仅 LAMBADA），R1 标为 Major（论文已在 Conclusion 中限定 "On LAMBADA"）。**Director 判断**：论文确实已做 scope limiting，但作为论文核心发现之一仅基于单一 benchmark 仍是显著弱点，定为 **Major**。

---

## Questions for Authors

1. 能否获取 Wang et al. (2025) model zoo 中任一配置的额外 seed 训练结果，以计算 within-architecture cross-seed Jaccard？[R1-Q1]
2. 排除 GDN 后 convergence 不显著（p = .233），论文对 convergence 的结论应如何修订？[R1-Q3]
3. LAMBADA 改为 perplexity-based ranking（而非 exact match）后 convergence pattern 是否持续？[R1-Q2]
4. 不同 prompt templates 是否会改变 per-example multiplicity 的 pattern？[R1-Q5]
5. 论文标题和框架使用 "predictive multiplicity"，但 α metric 仅在 4 个 benchmark 上报告（主文）+ 2 个（附录）。对其余 4 个 benchmark 是否有 α 数据？如果有，为何不报告？[Director Q]

---

## Missing References

以下引用由两位 Reviewer 建议，需核实真实性后再行添加：

- **Lindström et al. (2024)** "What Makes Two Language Models Think Alike?" — 跨架构 per-layer representation similarity [R2, R1 NEUTRAL 未验证]
- **Sellam et al. (2022)** — 已引用但应更深入讨论其 multi-seed 实验设计对本文的启示 [R1+R2 共识]
- **Pleiss et al. (2020)** "Identifying Mislabeled Data" — per-example training dynamics 方法论 context [R2]

⚠️ 以下引用来自 Reviewer 推荐，真实性未独立验证：
- "Reconciling Predictive Multiplicity in Practice" (FAccT 2025) [R2]
- "Hybrid Architectures for Language Models" (arXiv:2510.04800, 2025) [R2]
- Jiang et al. (2024) fine-tuning per-example behavior [R1]
- Bai et al. (2024) per-example reasoning behavior [R1]

---

## External Review (Stanford Agentic Reviewer)

**状态：pending**（已请求，等待用户提交结果）

外部审稿请求已于 2026-05-22T05:50 发送，8 小时后自动提醒。截至报告提交时尚未返回。内部审稿不受影响。外部结果到达后将作为补充信息单独转发。

---

## Visual Layout Check（非评分项）

**状态：done** | 0 critical, 4 warning, 2 info

| Severity | 位置 | 发现 |
|----------|------|------|
| ⚠️ warning | pp.3-5 | 连续 3 页纯文本（Related Work → Method → Experiments 开头），无 display item 穿插，节奏单调。建议 Method 中加架构示意图 |
| ⚠️ warning | pp.1-8 | 正文 8 页仅 4 个 display items（2 figure + 2 table），对实证论文偏低。建议提升附录关键结果为正文 figure |
| ⚠️ warning | p.2 | Figure 1 子面板 axis label/legend/tick 字号偏小（≤6pt），缩小打印后难以辨认 |
| ⚠️ warning | p.6 | Figure 2 多面板内文字非常小，信息密度高但可读性受限 |
| ℹ️ info | pp.10-18 | 附录 ~9 页含 ~23 张表但零 figure，视觉极为单调 |
| ℹ️ info | p.8 | Limitations 段落简洁（3 points），长度适中 ✓ |

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

**EMNLP 2026 ARR 评分映射**: 3 = Findings（可被 Findings 接收）

**维度汇总**:
| 维度 | R1 | R2 | 加权 |
|------|----|----|------|
| Soundness | 3.0 | 3.0 | 3.0 |
| Excitement | 3.0 | 2.5 | 2.75 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Confidence | 4/5 | 4/5 | 4/5 |

**一句话**：扎实的 empirical study，将 predictive multiplicity 系统引入 hybrid recurrent architecture 研究。分析全面、limitations 诚实，Decoupling 发现有启发性。但单次训练 confound 使核心 causal claim 无法确立，LAMBADA convergence 统计脆弱且依赖 confounded data point，新颖性限于现有方法应用于新 domain。当前状态适合 Findings。

**提升至 3.5 (Borderline Conference) 的路径**:
1. 提供 seed-level Jaccard calibration（从已发表文献提取或补充 multi-seed 训练）——解决 MF1
2. 将 LAMBADA convergence 降级为 exploratory observation 并在 Abstract/Intro 标注 GDN dependency——解决 MF2
3. 添加 continuous confidence margin cross-architecture similarity 作为 binary decomposition 的补充——解决 SF3
4. 从 seed-driven 文献提取可比数值进行 quantitative calibration——解决 SF2

---

## Detailed Comments

### §1 Introduction
- Contribution 1 的表述 "Unlike seed-driven disagreement within a single architecture (McCoy et al., 2020; D'Amour et al., 2022), this multiplicity is not addressable by seed averaging" 需要弱化——在无 multi-seed 对照的情况下，不能断言 architecture effect 独立于 seed effect（MF1）
- "the first systematic per-example analysis" 在 hybrid recurrent 领域是准确的，但应避免暗示方法论创新（SF4）

### §3 Method
- §3.1 Model Zoo：应在此处（而非仅 Limitations）讨论单次训练的局限性
- §3.5 Statistical Methods：bootstrap CI caveat ("heuristic indicators") 的表述很好，但后续引用时需一致性附加（SF6）
- Confirmatory/exploratory split（Appendix A）：应在 §3.5 中提及 pre-registration 的缺失（SF1）

### §4 Experiments
- §4.1：LAMBADA convergence 的 "suggestive evidence" 在排除 GDN 后不成立（ρ=-0.7, p=.233）。§4.4 的 GDN 敏感性分析已覆盖这一点，但应在 §4.1 本身就 flag（MF2）
- §4.2：binary decomposition limitation 讨论充分（Cohen's d cross-validation），但 near-zero normalized ES 的解释存在歧义（binary 粗糙 vs 真实 effect 小）（SF3）
- §4.3：decoupling 是最有价值的发现。"saturation at first attention level" 需 formal support（SF5）。Jaccard floor effect 的讨论（normalized ES 5-7% of achievable range）是有效的反驳，但需补充 trend test

### §5 Conclusion
- Practical protocol 段落存在但内容有限。在 seed confound 解决前，practical recommendations 的前提不完全成立
- Majority vote POC 的负面结果（-0.2pp LAMBADA, -1.1pp ARC-Easy）与 "per-example analysis tools may inform practitioners" 之间存在 tension——oracle gap (+7-14pp) 的存在缓解了这一 tension，但桥接不够清晰

### Limitations
- 三个 limitation points（Coverage, Methodological constraints, Pre-training only）覆盖合理，符合 EMNLP 要求
- 对 seed confound 的讨论充分但应进一步强化——当前表述 "we cannot fully disentangle" 偏弱，应明确这是论文最大的 validity threat

### Format
- 正文 ≤ 8 页 ✓
- Double-blind 匿名 ✓
- ACL style template ✓
- Figure/Table 字号需增大（视觉审查 warning）
- 正文 display item 数量偏低（4 个），建议增加