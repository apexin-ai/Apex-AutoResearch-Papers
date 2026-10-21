---
round: 21
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-20T15:05:40.723930+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告（修正版）— Generational Depth Estimation of Recursive Synthetic Text

**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + related work + 写作)
**轮次**: Round 1 (fresh review), 1 轮收敛
**修正说明**: 本报告基于完整的交叉回应（[AGREE]/[REBUT]）修正了初版报告中的部分严重性分级。R1 对 R2-N2 和 R2-N3 的 [REBUT] 将两项从 Must-Fix 降级为 Should-Fix。

---

## Summary

本文提出 K*_empirical（discrimination boundary），衡量递归合成文本代际深度在统计特征层面的可区分上限。使用 15 维 generator-independent 统计特征 + OBD-LightGBM 分类器，在 10 个模型配置（6 个架构族, 1B-14B）× 4 个文本域上系统测量 K*。核心发现：域排序 arXiv (K*=3) > C4 (K*=2) = Code (K*=2) > Wikipedia (K*=1) 跨模型/阈值稳定；DeBERTa fine-tuned classifier 在结构化域上扩展 K*（"two-tier ceiling"）；跨模型特征迁移在 aggregate level 保留 80-92% accuracy 但边界级 K* 分配脆弱。

---

## Strengths

1. **问题定义新颖且实用** [R1+R2 共识]：K* 作为 discrimination boundary 填补了 binary detection 和 model collapse 之间的空白。"到底能分辨到第几代" 对 data curation 有直接指导意义。

2. **实验覆盖面广、鲁棒性验证充分** [R1+R2 共识]：10 configurations × 6 families × 4 domains × 5 depths × 5000 seeds。Bootstrap 95% CI 贯穿全文，18 页附录含 LOFO validation、power analysis、changepoint analysis、McNemar test、feature ablation。R1 评价："近期审过的最全面的实验设计之一。"

3. **θ-invariant 域排序** [R1+R2 共识]：arXiv > C4 = Code > Wikipedia 不依赖阈值选择或模型配置。Feature ordering 分析（surprisal dominance）提供结构性解释。R2 补充：此 claim 与 θ=0.60 的具体数值无关，是更鲁棒的核心发现。

4. **诚实的局限性讨论** [R1]：主动报告 boundary fragility、marginal cases、scale limitations、Wikipedia scorer confound。Limitations 涵盖 9 个方面。

5. **Generator-independent 设计** [R2]：15D 特征集不依赖特定生成器，术语全文一致使用 "generator-independent"（非误导性的 "model-free"）。

---

## Weaknesses

### Must-Fix（4 项，R1+R2 共识）

**[MF-1] DPI→adjacent-pair AUC 的理论推理链存在逻辑缺口** [R1-N1, R2 AGREE]
- Section 3.1: DPI 约束**累积**互信息 I(X;Y_k) 的单调递减，但 K* 定义基于**相邻对** AUC_{k-1,k}。从 cumulative decay 到 adjacent-pair convergence 需要 Markov chain mixing rate 的额外论证，论文未提供。
- R2 补充：K* 定义本身是经验性的，DPI 更多是 motivation 而非 proof。实验数据中所有 10 配置 AUC 确实单调递减，changepoint 分析 35/37 一致（94.6%）。缺口**不影响实验结论有效性**，但削弱 Section 3.1 的理论严谨性。
- **建议**：(1) 将 DPI 定位为 "motivating heuristic" 而非形式推导；(2) 补充 "Empirically, adjacent-pair AUC decreases monotonically across all configurations, consistent with DPI prediction but not formally guaranteed"；(3) 引用 Levin & Peres (2017) Markov chain mixing time 理论作为补充桥梁。

**[MF-2] 多个 K*=2 判定基于极薄统计余量** [R1-N2, R2 AGREE]
- LLaMA-3.1-8B (C4): CI lower = 0.603, 余量 0.003
- Qwen-cont (cross-scorer): CI lower = 0.602, 余量 0.002（cross-family 下降为 K*=1）
- 0.002-0.003 余量落在 bootstrap 估计噪声范围内。R2 补充：Appendix D.12 power analysis 是 aggregate level，未针对 boundary pair (1v2) 单独报告 power。40 次 θ 比较未做多重比较校正，α=0.05 下约 2 次 false positive 预期。分层报告后 "7/9" 可能缩减为 "5-6/9 confidently achieve K*=2"。
- **建议**：(1) 分层报告 "confident K*=2" vs "marginal K*=2"；(2) 所有配置报告确切 CI lower 和余量；(3) 附录报告 BH-corrected 结果；(4) 为 boundary pair 单独报告 statistical power。

**[MF-3] Qwen 家族 5/10 配置，"7/9" framing 具有误导性** [R1-N3, R2 AGREE]
- 9 个 continuation 配置中 Qwen 占 4 个（44%）。按独立架构家族：4/6 达 K*=2（Gemma, Mistral 为 K*=1）。同一家族内不同配置的 K* 高度相关，不应视为独立证据。
- R2 补充：Gemma-2-2B 和 Mistral-7B 的 K*=1 对应 instruction mode / 特定解码策略，K*=2 可能部分是 continuation mode artifact 而非 architecture-general 发现。论文应更明确讨论 generation mode 对 K* 的影响。
- **建议**：所有关键 claim 以 "4/6 architecture families" 为 primary framing；讨论 generation mode 对 K* 的系统性影响。

**[MF-4] Abstract 对迁移结果选择性报告** [R2-N1, R1 AGREE]
- Abstract "80-92% accuracy retention" 是 aggregate over all depth pairs（含 trivial 的 0v1），省略了 boundary-level fragility（7B 4/6 off-diagonal 1v2 pairs < θ）。R1 确认：Appendix D.19 的 96-100% mean pairwise AUC retention 被 0v1 高 AUC (>0.89) 拉高，单看 1v2 boundary pairs retention 显著更低。
- **建议**：Abstract 中补充 boundary-level fragility caveat，或改用更保守的 framing 明确区分 aggregate 和 boundary-level transfer。

### Should-Fix（10 项）

**[SF-1] 遗漏 Wang et al. (ACL 2025) attractor cycles 相关工作** [R2 critical→R1 REBUT→降级为 Should-Fix]
- Wang et al. "Unveiling Attractor Cycles in LLMs" (ACL 2025) 研究连续改写收敛到 2-period attractor cycles。R2 认为与 K* 直接相关且属同年同会议遗漏。
- R1 反驳：论文已引用同类工作（Geng et al. 2026, Mohamed et al. 2025），K* 与 attractor cycle 的对应关系非直接（统计判别边界 ≠ 确定性动力学收敛）。遗漏一篇相关但非直接基础性的引用不应为 Must-Fix。
- **共识**：补入 Related Work 并简要讨论 K* 与 attractor dynamics 的潜在联系，但降为 Should-Fix。

**[SF-2] "One-wash laundering" framing 需明确起点** [R2 critical→R1 AGREE with nuance→降级为 Should-Fix]
- K*=2 意味着 1v2 仍可区分，"one-wash" 暗示一次生成即可洗白。R1 同意核心观察正确，但认为在 model collapse 语境下起点 depth-1 是合理默认，属 wording 问题非方法论错误。
- **共识**：修改措辞明确起点是 depth-1 而非 depth-0。

**[SF-3] LOFO θ=0.60 验证存在数据层面依赖** [R1-W2, R2 AGREE with nuance]
- LOFO 所有 folds 使用同一 C4 数据集。Wikipedia 仅 1/6 匹配（17%）。
- R2 补充 nuance：应区分两个 claims——θ=0.60 是 C4-calibrated 的（跨域泛化有限），但域排序是 θ-invariant 的（Figure 3，成立且不依赖 θ 取值）。
- **建议**：补充 leave-one-domain-out validation；明确区分 θ 的 domain-specific calibration 与 θ-invariant ordering。

**[SF-4] Filtering 效果量在现实污染比例下极小** [R1-W3, R2 AGREE]
- 10% 污染下 MMLU 改善 ~0.2pp。R2 补充：Section 5 "consistency check" 定位部分缓解，但 abstract Contribution (c) 过度强调。
- **建议**：正文报告低污染比例效果量；abstract 降低 filtering 贡献权重或明确 "validation" 定位。

**[SF-5] Scale trend 外推仅基于 3 个数据点** [R1-W4, R2 AGREE]
- 1.5B/7B/14B（14B 仅 Qwen）三点无法支撑 scaling law claim。
- **建议**：严格限于 "K*=2 在 1.5B-14B 稳定"，删除外推语言。

**[SF-6] DeBERTa "two-tier ceiling" 缺中间基线** [R1-W5 + R2-W2 共识]
- 15D hand-crafted vs 184M fine-tuned DeBERTa 的 capacity 差异巨大。缺少中间基线（frozen DeBERTa + linear probe、DistilBERT、更大特征集）来排除 trivial explanation。C4 gap=0 是有趣的（representation-independent boundary），但 Wiki/arXiv gap 可能仅反映 classifier capacity。
- **建议**：补充中间基线，或将表述从 "two-tier ceiling" 调整为 "feature-set-dependent gap"。

**[SF-7] 与 Geng et al. (2026) 的区分度不足** [R2-W1, R1 AGREE]
- Related Work 对 Geng et al. 仅一句。应明确区分：Geng et al. 关注输出**何时收敛**（convergence to attractor），本文关注分类器**何时失效**（discrimination boundary）。
- R1 补充：K* 可被视为 mixing time 的 feature-space proxy。

**[SF-8] 混合场景（prompt-chain + retrain-chain）未讨论** [R2-W3, R1 AGREE]
- Prompt-chain K*=2 vs retrain-chain K*=7，混合路径 K* 行为完全未知（可能 2-7）。
- **建议**：至少在 Limitations 中讨论混合场景的 ecological validity gap。

**[SF-9] Conclusion 过于简短** [R2-W4, R1 REBUT]
- R2 认为约 1/3 页过短，缺乏 broader implications。R1 反驳：长度在 *ACL 8-page papers 正常范围，关键讨论在 Section 4-5 和 Appendix D 已展开。
- **分歧记录**：R2 希望扩展，R1 认为不必要。如有空间，可考虑增加 1-2 段 broader implications。

**[SF-10] Abstract 信息密度过高** [R2-W5, R1 部分同意]
- K*_theory, K*_neural, K*_binary 三个变体在 Abstract 首次出现未解释区别。R1 认为 empirical NLP abstract 需要 specific results，属 minor。
- **建议**：可将部分细节（域排序具体 K* 值）移至 Introduction contribution list。

### Minor Issues（10 项）

- [m1] Retrain-chain CI 用 z=1.96（5 folds 应用 t 分布，低估宽度 ~42%）[R1]
- [m2] holtzman2020curious orphan bib entry [R1+R2]
- [m3] K* 符号系统缺统一 notation table [R2]
- [m4] Bootstrap resample 数不一致（1,000 vs 10,000），需说明标准 [R1]
- [m5] Appendix Table 9 交叉引用不一致 [R1]
- [m6] bib 条目 first_author mismatch（alemohammad2024, mehta2025, levy2008）[R1]
- [m7] Shahriar et al. (2025) "The Erosion of LLM Signatures" 建议引用 [R2]
- [m8] CodeSearchNet (2019) 代码风格可能不代表当前 LLM 代码生成场景 [R1]
- [m9] Figure 2 y 轴标签未说明 bootstrapped vs raw AUC [R2]
- [m10] Table 2 脚注极小，打印后可能难辨 [Visual Check]

---

## Reviewer Consensus（交叉回应后确认）

以下问题双方明确 [AGREE]：
- DPI 推理链有逻辑缺口，但不影响实验结论，需调整 framing [MF-1]
- 统计余量极薄，需分层报告 + 多重比较校正 [MF-2]
- Qwen 5/10 过度代表，"4/6 families" 为更诚实的 primary framing [MF-3]
- Abstract 选择性报告迁移结果，boundary-level 与 aggregate 需区分 [MF-4]
- DeBERTa two-tier ceiling 的 non-triviality 需中间基线或调整表述 [SF-6]
- Filtering 效果量小，abstract 权重需调低 [SF-4]
- Scale 外推仅 3 点，不可靠 [SF-5]
- 混合场景是重要遗漏 [SF-8]

## Reviewer Divergence（交叉回应后记录）

| 问题 | R1 立场 | R2 立场 | 最终处理 |
|------|---------|---------|----------|
| Wang et al. 遗漏严重性 | Should-Fix（已覆盖同类工作） | Must-Fix（同年同会议核心工作） | **Should-Fix**（R1 rebuttal 成立：非直接基础性引用） |
| "One-wash" framing 严重性 | Should-Fix（wording 问题） | Must-Fix（术语可能被误引） | **Should-Fix**（R1 rebuttal 成立：修改措辞即可） |
| Conclusion 长度 | 正常范围，不需修改 | 过短，需扩展 | **Should-Fix**（记录分歧，非强制） |
| Abstract 信息密度 | Minor（empirical abstract 正常） | Should-Fix（认知过载） | **Minor→Should-Fix 折中**（SF-10） |

---

## Questions for Authors

1. 是否观察到任何配置下 AUC_{k,k+1} 出现非单调行为？如有，K* 定义如何处理？[R1]
2. 应用 Bonferroni/BH 校正（α=0.05/40）后 marginal cases 是否仍通过？[R1+R2]
3. Qwen-cont 在 cross-scorer 下 K* 从 2 降至 1，是否说明 same-family scorer artifact？[R1]
4. 更大 scorer (7B vs 1.5B) 是否会提高 K*？Appendix D.1 的 Qwen 内部对比是否可推广至 cross-family？[R2+R1]
5. K*=2 是否对应 Wang et al. (ACL 2025) 发现的 attractor cycle 进入深度？两者的理论联系是什么？[R2]
6. "80-92% accuracy retention" 的确切计算基础：aggregate over all depth pairs（含 0v1）还是仅 boundary-level 1v2？[R2, R1 确认为 aggregate]
7. 混合场景（prompt-chain + retrain-chain 交替）中 K* 如何定义和测量？[R2+R1]
8. 代码和种子文档集的公开计划？[R1]

---

## Missing References

1. **Wang et al. (ACL 2025)** — "Unveiling Attractor Cycles in LLMs" — attractor cycle 与 K* boundary 潜在联系 [R2, R1 同意补入但非 critical]
2. **Shahriar et al. (arXiv 2512.05311, 2025)** — "The Erosion of LLM Signatures" — iterative paraphrasing 检测下降，与 K*=2 互证 [R2]
3. **Levin & Peres (2017)** — "Markov Chains and Mixing Times" — adjacent-pair convergence 理论基础 [R1, R2 支持]

---

## External Review

**状态**: 未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: done（0 critical, 3 warnings, 22 info）

**Warnings**:
1. **Page 5 拥挤**：单页 3 个 display item（Table 2 + Figure 2 + Figure 3），Figure 2/3 被压缩至 ~1/4 栏高，轴标签/图例 ~7pt 接近可读性下限。建议将 Figure 3 移至下一页。
2. **Page 8 无视觉锚点**：Discussion + Conclusion + Limitations 为纯文本，正文最后页缺总结性视觉元素。
3. **Page 15 附录表格间距紧**：Table 12 跨 2/3 页后 Table 13 紧随，中间文字被挤压。

**Positive**: 正文恰好 8 页（符合 EMNLP 2026 限制）；booktabs 风格统一；无 LaTeX 错误/overfull hbox；颜色方案基本色盲友好；display item 密度 1.13/页合理。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Justification**:

论文提出了新颖且有实际意义的研究问题（递归合成文本的代际深度判别边界），实验覆盖面和鲁棒性验证达到顶会标准。域排序不变性（arXiv > C4 = Code > Wikipedia）是核心的干净发现，不依赖具体阈值。

阻碍 conference-level 接收的问题：

(1) **理论基础需修正**：DPI→adjacent-pair AUC 推理链有缺口（MF-1）。两位 Reviewer 一致认为不影响实验有效性，但需将 DPI 重新定位为 heuristic motivation。

(2) **核心 claim 的统计可靠性**：多个 K*=2 判定余量极薄（MF-2），Qwen 过度代表膨胀了 "7/9" framing（MF-3）。两位 Reviewer 一致认为真实 support 是 "3-4/6 families confidently achieve K*≥2"，需分层报告。

(3) **Framing 问题**：Abstract 选择性报告迁移结果（MF-4），掩盖 boundary-level fragility。

(4) **方法论增量有限**：15D hand-crafted features + LightGBM 均为标准工具。Novelty 主要在问题定义和 empirical findings，需更充分论证 empirical characterization study 的独立价值。

**修复路径**：MF-1（理论 framing 调整，不需新实验）+ MF-2（分层报告 + BH 校正）+ MF-3（"4/6 families" 为 primary framing）+ MF-4（Abstract 补充 boundary-level caveat）均可在 revision 中完成。修复后有潜力提升至 3.5 (Borderline Conference)。

**Reviewer Scores**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)
**Consensus Score**: 3.0 (Findings)
**Confidence**: 4/5