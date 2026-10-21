# 阴性实验 Framing 审计

## exp-007b (killed): PPCI 表 HB backfill

- **论文中是否讨论**：不需要（内部决策，非阴性结果）
- **PPCI composition 讨论完整性**：充分
- **位置**：`method.tex:55-61`（PPCI composition 段落）、`appendix.tex:507-555`（Appendix PPCI 完整实验）
- **具体情况**：论文在 method.tex 中清楚说明 EC-HTE 和 PPCI 的互补性（"Neither is redundant with the other"），并给出了 4-DGP 正交设计的完整结果（Table PPCI）。DGP-A（仅 covariate error）下 PPCI 无增益，DGP-B（仅 outcome error）下 EC-HTE 贡献可忽略——这些就是 exp-007b 放弃 HB backfill 的理由的间接体现。
- **建议**：无需补充

---

## exp-015 (negative): GPT-4.1 real CM 上 EC-HTE 失败

- **论文中是否讨论**：是，详细
- **讨论位置**：
  - `appendix.tex:751-828`（§Semi-Real CM Validation，完整 section）
  - `appendix.tex:806-811`（root cause 分析：S0 FNR=0.526）
  - `appendix.tex:818-821`（diagnostic rule，明确引用 exp-015）
  - `experiments.tex:82`（operating conditions 汇总，FNR<0.50 条件）
  - `limitations.tex:1`（FPR/FNR<0.5 条件）
  - `experiments.tex:79`（hate speech 实测 underperformance）
- **充分性**：**充分**
  - Root cause 完整：S0 FNR=0.526 → CM 行近均匀 → inversion 放大噪声（appendix.tex:807）
  - P(Z=1)=0.18 的 class imbalance 影响在 appendix.tex:756 和 814 中明确提及
  - 三个 applicability conditions 在 appendix.tex:815 归纳，并上升到 experiments.tex:82 的 operating conditions
  - 提供了 applicability frontier 图（Figure applicability_frontier.pdf）
  - 明确指出 exp-015 同时违反 κ 和 effective n 两个条件（appendix.tex:820）
  - 提到 subgroup-average metrics 可能 mask cell-level heterogeneity（appendix.tex:821）
- **建议**：无需补充

---

## exp-016 (negative): GPT-3.5-Turbo real CM 上 EC-HTE 失败

- **论文中是否讨论**：是
- **讨论位置**：
  - `appendix.tex:813-814`（第二个 semi-real 实验，明确 GPT-3.5-Turbo）
  - `appendix.tex:820`（diagnostic 正确预测 exp-016 失败）
  - `appendix.tex:946`（Civil Comments multi-LLM 表中 GPT-3.5-turbo FPR 数据）
- **充分性**：**充分**
  - Root cause 明确：high FPR variance (worst-subgroup FPR=0.39) + class imbalance P(Z=1)=0.18（appendix.tex:814）
  - 与 exp-015 root cause 的一致性被明确指出（"yields similar results"）
  - Diagnostic rule 在 appendix.tex:820 验证了对 exp-016 的 100% 预测准确率
- **建议**：无需补充

---

## exp-028 (negative): 非对称 diagnostic AUC ≈ 对称版

- **论文中是否讨论**：是
- **讨论位置**：
  - `theory.tex:56-67`（Remark 2，核心理论结果）
  - `theory.tex:64-65`（关键推导：column-stochastic M → |B_s[0,1]|=|B_s[1,1]|，非对称退化为对称）
  - `appendix.tex:168-177`（asymmetric extension 讨论，AUC 0.86→0.66）
  - `appendix.tex:443-466`（完整 asymmetric 实验 section）
- **充分性**：**充分**
  - 退化机制在 theory.tex:65 清楚解释："because column-stochastic M forces |B_s[0,1]|=|B_s[1,1]|; practitioners may use the simpler symmetric formula without loss"
  - 这是 positive framing：论文将"非对称退化为对称"呈现为一个便利的理论结果（practitioners 可以用更简单的公式），而非实验失败
  - AUC 降低（0.86→0.66）在 appendix.tex:176 中有报告
- **具体问题**：无。这个实验的 framing 是诚实的——退化结论本身是有用的理论洞见。
- **建议**：无需补充

---

## exp-030 (negative): K=8 HB RMSE >> Global

- **论文中是否讨论**：是，详细
- **讨论位置**：
  - `appendix.tex:376-440`（完整 K=8 subsection，含 per-subgroup breakdown）
  - `appendix.tex:397`（HB RMSE=0.340 vs Global RMSE=0.168）
  - `appendix.tex:406`（明确指出 ~31 labels/subgroup 不足）
  - `experiments.tex:29`（主文提及 K=8 RMSE 增加，推荐 n_expert/K≥50）
  - `experiments.tex:82`（operating conditions：K≤4）
  - `limitations.tex:2`（K=8 boundary 明确讨论）
- **充分性**：**充分**
  - 主文 experiments.tex:29 直接承认 RMSE 增加
  - 主文 experiments.tex:82 将 K≤4 列为 operating condition
  - limitations.tex:2 明确 K=8 boundary："coverage remains nominal (≥95.6%) but RMSE exceeds global correction, establishing a scalability boundary"
  - Appendix 提供完整 per-subgroup 分析（Table k8_per_subgroup）
  - 解释了 RMSE degradation 集中在 high-π subgroups（appendix.tex:432）
- **建议**：无需补充

---

## exp-033 (negative): K=8 adaptive shrinkage 仍不够

- **论文中是否讨论**：是
- **讨论位置**：
  - `appendix.tex:436-440`（adaptive shrinkage 结果）
  - `appendix.tex:438`（RMSE 0.340→0.216，但仍超 Global 0.166）
  - `appendix.tex:439`（关键结论："the bottleneck is per-subgroup sample size (~31 expert labels) rather than the shrinkage method itself"）
  - `appendix.tex:440`（给出 n_expert≥500 的推荐）
- **充分性**：**充分**
  - Root cause 诊断精准：瓶颈是 per-subgroup sample size 而非 shrinkage 方法（appendix.tex:439）
  - 给出实际建议：n_expert≥500（~60 labels/subgroup）才能达到 RMSE parity（appendix.tex:440）
  - 与 exp-030 的讨论形成完整 narrative：K=8 是真实边界，adaptive shrinkage 只能缩小但无法消除差距
- **建议**：无需补充

---

## 总结

### 需要补充的地方

**无。** 所有 6 个阴性/killed 实验在论文中都有诚实且充分的讨论：

| 实验 | 主文提及 | Appendix 详细分析 | Limitations 提及 | Operating Conditions |
|------|---------|-------------------|------------------|---------------------|
| exp-007b | N/A（内部决策） | PPCI section | N/A | N/A |
| exp-015 | ✓ (experiments.tex:79,82) | ✓ (appendix.tex:751-828) | ✓ (limitations.tex:1) | ✓ (FNR<0.5) |
| exp-016 | ✓ (via operating conditions) | ✓ (appendix.tex:813-814) | ✓ (via exp-015) | ✓ (FPR<0.5) |
| exp-028 | ✓ (theory.tex:56-67) | ✓ (appendix.tex:443-466) | ✓ (limitations.tex:6) | N/A |
| exp-030 | ✓ (experiments.tex:29,82) | ✓ (appendix.tex:376-440) | ✓ (limitations.tex:2) | ✓ (K≤4) |
| exp-033 | via exp-030 | ✓ (appendix.tex:438-440) | via exp-030 | via exp-030 |

### 风险评估

**低风险。** Reviewer 可能追问的点及论文已有应对：

1. **"Why does EC-HTE fail on real LLMs?"** — 论文在 appendix.tex:815 归纳了三个 applicability conditions，在 experiments.tex:82 给出操作指南，在 Figure applicability_frontier 提供可视化决策工具。
2. **"K=8 is a limitation — does the method scale?"** — limitations.tex:2 直接承认 scalability boundary，appendix.tex:440 给出量化建议（n_expert≥500），framing 为 fixed-budget 下的 trade-off 而非方法缺陷。
3. **"Asymmetric diagnostic 没有提升？"** — theory.tex:65 将其 reframe 为理论便利性（practitioners 无需区分 symmetric/asymmetric），而非 negative result。
4. **"Why not test on more real data?"** — limitations.tex:12 诚实承认缺乏 ground-truth subgroup CATEs 的公共数据集，解释了使用 synthetic CATE injection 的原因。

唯一潜在弱点：exp-015/016 的失败在**主文**中的措辞比较间接（experiments.tex:79 说 "underperforms"，experiments.tex:82 列 operating conditions），完整 root cause 分析只在 Appendix。但这符合顶会惯例——主文给结论和条件，Appendix 给机制，不构成 framing 问题。
