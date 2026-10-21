---
round: 22
review_mode: fresh
overall_score: 3.0 Findings
timestamp: 2026-05-25T21:37:56.257086+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告 — Round 22（Fresh Review）

**论文**: Aggregate Equivalence ≠ Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models
**目标 Venue**: EMNLP 2026 (via ARR)
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计；R2: 新颖性 + 相关工作完整性 + 格式合规）
**审稿模式**: Fresh（无上轮记忆）

---

## Summary

本文研究 hybrid linear recurrent models（Mamba、Mamba-2、GDN 等）中 aggregate-level 等价掩盖 per-example 行为分歧的现象。利用 Wang et al. (2025) 受控 model zoo 在 4 个 benchmark 上进行系统性 per-example 分析，发现：(1) 不同架构在整体准确率相近时，per-example 正确/错误集合存在显著结构化差异；(2) per-example overlap 在 attention ratio 约 4% 处趋于稳定；(3) confidence margin 可以中等精度（AUC 0.70-0.74）预测受影响样本。附带 confidence-based routing case study。

---

## Strengths

1. **受控实验设计精良**：Wang et al. (2025) model zoo 实现了 training recipe 严格对齐的单变量控制（仅改变架构 backbone），这在 multiplicity 文献中罕见。
2. **统计方法透明诚实**：permutation tests + Bonferroni 校正 + normalized effect sizes，每一处统计不足都有坦诚 caveat（Section 3.5）。
3. **附录深度**：14-22 页附录提供全面 robustness checks（GDN exclusion、continuous-threshold Jaccard、5-architecture validation 等），极大增强可信度。
4. **Reproducibility**：inference-only 实验（~5 GPU-hours），代码和数据匿名公开。
5. **5-architecture validation**：40 个 permutation tests 全部显著（p ≤ .002），per-example divergence 的核心发现在跨架构层面稳健。
6. **研究问题重要且及时**：hybrid recurrent models 正在被广泛部署，揭示 aggregate metrics 掩盖的 per-example 差异具有实际价值。
7. **格式完全合规**：8 页主文、匿名化、Limitations 位置正确、Abstract ≤ 200 words。

---

## Weaknesses

### Critical（影响接收决定）

**W1** [R1-C1 + R2-W2, 共识 Critical] **Spearman n=5 统计功效不足，核心发现呈现与 caveat 矛盾**
- n=5 attention ratios 的 Spearman 相关统计功效近乎为零。LAMBADA 校正后 p=.167 不显著，但仍作为核心发现呈现。Bonferroni α/10=.005 在 n=5 下理论上不可达（最小 p=.017）。
- Section 3.5 标注 "suggestive" 的 caveat 与 Section 4.2 标题和 Conclusion 中更确定性的表述之间存在张力（尽管 R21 已改为 "appears to stabilize"，但根本问题不变）。
- **跨 22 轮持续 Critical**（对应 R5-W2 + R16-N1）。

**W2** [R1-C2 + R2-W1, 共识 Critical→Structural] **单 seed 训练无法分离架构效应与随机种子效应**
- 每个架构仅有 1 次训练运行，观察到的 per-example 差异可能部分或完全由 seed variation 驱动。
- Pythia 70M 9-seed 校准存在三重 mismatch（scale/family/accuracy），无法可靠推广到 hybrid 1.3B 模型。
- **结构性限制**，无法在现有数据上修复。R22 确认为 wont_fix 但必须在 Limitations 中充分讨论。

**W3** [R2-N2 + R1 交叉 PARTIALLY AGREE] **核心贡献偏描述性，方法论增量有限**
- 三个 contributions 可归结为：在新模型族上复现已知 predictive multiplicity + 观察到 Jaccard 趋平（n=5 无法统计确认）+ moderate AUC predictor。方法论均为已有工具（Jaccard, α, permutation tests）。
- R1 指出 empirical context novelty（within-family controlled comparison）有别于 McCoy et al. (2020) 的 across-family 比较，足以支撑 Findings 但不够 Conference。
- **共识：Major。Findings 标准下可接受。**

### Major（影响评分但不一票否决）

**W4** [R2-N1 + R1 交叉 AGREE→Major] **Discussion and Conclusion 过于单薄**
- Section 5 仅约 120 词。以 "deployment reliability" 为卖点的论文未讨论：从业者模型选择流程变化、benchmark 设计含义、fine-tuning 后 multiplicity 持续性、与 ecological fallacy 的理论联系。
- R1 认为是 presentation 问题而非 soundness 问题，降为 Major。

**W5** [R2-N3 + R1 交叉 AGREE→Major] **相关工作缺失重要引用**
- 缺失 4 篇高度相关工作：
  - Swayamdipta et al. (2020) Dataset Cartography — per-example analysis 方法论前驱，confidence/variability 分解与本文 helped/hurt 概念高度类似
  - Black et al. (2022) Model Multiplicity survey — multiplicity 综述
  - Fehlauer et al. (2025) Convergence and Divergence under Different Random Seeds — 直接关联 seed confound
  - Ganesh et al. (2025) Systematizing Multiplicity — multiplicity 最新框架
- R1 确认全部 4 篇高度相关，但认为 revision 可修复，降为 Major。

**W6** [R1-C3] **n=3 架构下 cross-architecture 统计推断基础薄弱**
- 仅 3 个架构族（Transformer、Mamba/Mamba-2、GDN），bootstrap CI 在 n=3 下覆盖率远低于名义值。Section 3.5 已标 "heuristic" 但 Table 2 呈现方式暗示更强可靠性。

**W7** [R1-M1] **GDN h3-1 的 16-head confound**
- GDN 模型使用 14 个注意力头（vs Transformer/Hawk 12 heads），构成混淆变量。排除 GDN 后 LAMBADA ρ=-0.7 (p=.233) 不显著，MMLU ρ 反转。Per-example 核心发现不受影响，但 convergence 叙事高度敏感。

**W8** [R1-M3 + R2-W3] **Routing case study 证据单薄，定位过高**
- LAMBADA +5.3pp，但 PIQA -0.6pp (p=.006) 显著为负。仅 2/4 benchmark 正向效果。
- 缺少 baseline（majority-vote ensemble、average-logits ensemble、oracle routing 上界）。
- Abstract/Conclusion 仍暗示更广泛实用性。

**W9** [R1-M5] **缺少 fine-tuning 实验**
- 论文以 deployment 为卖点但全部实验基于 pre-trained model。Fine-tuning 后 per-example multiplicity 是否持续完全未验证。

**W10** [R1-M2] **Binarization 信息损失**
- 将连续预测概率二值化为 correct/incorrect 损失信息。Appendix O continuous-threshold Jaccard 部分缓解，但正文未充分讨论。

**W11** [R1-M4] **AUC 0.70-0.74 实用性未讨论**
- Moderate AUC 在实际部署中是否足够有用需要讨论。"Reliable" 用词应修正为 "moderate"。

### Minor

**W12** [R2 小问题] Table 3 列标签 J̄_u 中 "u" 代表 "hurt" 不直观，建议改为 J̄_hurt。
**W13** [R2 小问题] Task taxonomy 为 informal/non-pre-registered，后续 cross-category 比较说服力受限。
**W14** [R2 小问题] LaTeX aggressive spacing hacks（\textfloatsep=4pt 等），虽不违规但影响阅读体验。

---

## Reviewer Consensus

| 问题 | R1 | R2 | 交叉结果 |
|------|----|----|----------|
| Spearman n=5 功效不足 | C1 (Critical) | W2 (Should-Fix) | R1 [AGREE] R2 → 共识 Critical |
| 单 seed confound | C2 (Critical) | W1 (Should-Fix) | R1 [AGREE] R2 → 共识 Critical/Structural |
| Contributions 增量有限 | — | N2 (Critical) | R1 [PARTIALLY AGREE] → 共识 Major |
| Discussion 单薄 | — | N1 (Critical) | R1 [AGREE] 但降 Major |
| 缺失关键引用 | — | N3 (Critical) | R1 [AGREE] 但降 Major |
| n=3 统计推断薄弱 | C3 (Critical) | — | R1 独有 |
| Routing 价值有限 | M3 (Major) | W3 (Should-Fix) | R1 [AGREE] R2 → 共识 Major |
| GDN head confound | M1 (Major) | — | R1 独有 |
| Fine-tuning 缺失 | M5 (Major) | 含在 N1 | 共识方向一致 |
| Overall Score | 3.0 Findings | 3.0 Findings | **3.0 Findings** |
| Confidence | 4/5 | 4/5 | — |

---

## Reviewer Divergence

**严重程度分级分歧**：R1 将统计功效（n=5 Spearman）和 seed confound 列为 Critical，R2 列为 Should-Fix。反之，R2 将 Discussion 单薄和 novelty 不足列为 Critical，R1 降为 Major。但双方在总体评价（3.0 Findings）上完全一致，分歧仅在于哪些问题更致命，而非论文整体水平。

---

## Questions（需要作者澄清）

1. Pythia 70M 校准显示 within-seed J 与 cross-architecture J 存在 2.7-4.3× gap。这个 gap 是否在更大 scale（如 410M+）上仍然成立？410M 校准失败的原因是什么？
2. 排除 GDN 后 LAMBADA ρ=-0.7 (p=.233) 不显著，MMLU ρ 反转——这对 Contribution 2（saturation claim）意味着什么？
3. Confidence-based routing 在 PIQA 上显著为负 (-0.6pp, p=.006)——作者如何解释这一结果？是否暗示 routing 策略需要 task-specific 调整？
4. 论文提到 "left to future work" 的 average-logits ensemble baseline——为什么不在本文中提供这一最自然的对比？
5. Per-example multiplicity 在 fine-tuning 后是否持续？作者有任何初步证据或理论预期吗？

---

## Missing References

以下高度相关工作未被引用（均已在 bib 中但未在正文中引用，或完全缺失）：

1. **Swayamdipta et al. (2020)** "Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics" — per-example analysis 方法论前驱，confidence/variability 分类与本文概念高度类似。**必须引用。**
2. **Black et al. (2022)** "Model Multiplicity: Opportunities, Concerns, and Solutions" — multiplicity 综述。论文以 multiplicity 为核心概念却未引用该综述。
3. **Fehlauer et al. (2025)** "Convergence and Divergence of Language Models under Different Random Seeds" — 直接关联 seed confound 问题，可提供 seed variation 基线。
4. **Ganesh et al. (2025)** "Systemizing Multiplicity" — multiplicity 最新系统化框架。
5. **Geifman & El-Yaniv (2017/2019)** selective prediction — routing 策略的方法论前驱。
6. **Caruana et al. (2004)** ensemble selection — routing/selection 的经典框架。

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。**

---

## Visual Layout Check（非评分项）

**状态：已完成** (2026-05-25 21:16-21:20 UTC)

| 严重程度 | 位置 | 发现 |
|----------|------|------|
| ⚠️ Warning | Page 7 | 页面过度拥挤：1 figure + 2 tables 共 3 个 display items。Figure 6 散点图尺寸过小，打印时难以辨认。建议放大或将 Table 3/4 之一移至相邻页。 |
| ⚠️ Warning | Page 5 | Figure 3 红绿色系对红绿色盲读者区分度不足。建议改用 Okabe-Ito 色板或辅以 hatch pattern。 |
| ⚠️ Warning | Page 6 | Figure 5(b) 同样存在红绿色盲可辨识性问题。 |
| ⚠️ Warning | Page 22 | 末页仅 ~15% 内容填充，85% 空白。 |
| ℹ️ Info | Page 1 | Figure 1 在 page 2 顶部紧接出现，符合最佳实践。 |
| ℹ️ Info | Page 4 | Figure 2 内部文字较小，缩小打印时可能难以辨读。 |
| ℹ️ Info | Page 8 | Figure 7 热力图数值字号偏小（~6-7pt）。 |
| ℹ️ Info | Pages 11-21 | Appendix 全为表格+文字，无 figure，视觉单调。 |
| ℹ️ Info | Page 7 | Table 4 bold 标注正确，booktabs 风格规范。 |
| ℹ️ Info | Pages 9-10 | 参考文献格式统一，无未解析引用。 |

**小结**：0 critical, 4 warnings, 6 info。主要关注色盲可辨识性（2 处）和 Page 7 拥挤。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**
**Confidence: 4/5**
**Soundness: 3.5/5** | **Excitement: 2.5/5** | **Reproducibility: 4/5**

本文是一篇实验设计严谨、统计分析透明的经验性研究。受控 model zoo 的单变量设计和 5-architecture validation 是实质性优点。然而，核心贡献偏描述性（在新模型族上复现已知 multiplicity 现象），方法论无新增工具。两个关键统计问题（n=5 Spearman 功效不足、单 seed 无法分离架构/种子效应）构成结构性限制，无法通过修订完全解决。Discussion 过于单薄，routing case study 证据不足但定位过高。

**适合 Findings track**：核心 per-example divergence 发现稳健（40 个 permutation tests 全部显著），对 hybrid model 部署有参考价值，但 evidence strength 和 intellectual depth 不足以支撑主会议。

---

## Detailed Comments

### Section 1 (Introduction)
- Contributions 列表三点均为描述性发现，应强化 "first controlled within-family comparison" 的独特实验设计价值。
- 当前版本是否已将 "saturates" 改为 "appears to stabilize" 需确认。

### Section 2 (Related Work)
- 缺失 4 篇高度相关引用（见 Missing References）。
- Dataset Cartography 的 confidence/variability 分解与本文 helped/hurt 概念的对比讨论完全缺失。
- Selective prediction 和 ensemble selection 文献未引用，削弱 routing 贡献的 positioning。

### Section 3 (Methodology)
- §3.5 的 "heuristic" caveat 与后续章节确定性表述之间的张力是核心 presentation 问题。
- Permutation test 的 "conservative" 论证需要修正——不条件化 item difficulty 可能使检验 anti-conservative。

### Section 4 (Results)
- §4.2 saturation claim：hedging 已改善（"appears to stabilize"），但 n=5 根本问题不变。
- GDN exclusion 后多个 benchmark 的 ρ 不显著或反转，需在正文中更显著位置讨论。
- Routing：需要 ensemble baseline 和更诚实的 Abstract/Conclusion 定位。

### Section 5 (Discussion & Conclusion)
- 从 ~120 词扩展至至少 0.5 页。
- 应涵盖：ecological fallacy 理论联系、从业者实践建议、fine-tuning 后 multiplicity 假设、benchmark 设计含义。

### Limitations
- 当前 3 点覆盖合理。
- 建议补充 greedy decoding 对生成任务的潜在影响（一句即可）。

### Format
- 全部合规：8 页、匿名化、正确模板、Limitations 位置正确。
- 色盲可辨识性问题（Figure 3, 5b）应在 camera-ready 前修正。

### 引用真实性
- 3 个 2026 arXiv 引用已验证真实。
- 2 个引用（Basu 2026, Haghighat et al. 2026 AAAI）未独立验证。
