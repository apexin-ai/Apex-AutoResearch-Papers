---
round: 1
overall_score: weak accept
timestamp: 2026-05-15T10:58:01.571361+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告 — Round 1

**论文**: "How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints"
**目标 Venue**: EMNLP 2026 Main Conference (ARR May cycle, deadline 2026-05-25)
**审稿团队**: Reviewer 1（方法严谨性 + 实验完整性）, Reviewer 2（新颖性 + 写作质量 + 相关工作 + 格式合规）
**审稿轮次**: Round 1（1 轮收敛，所有 critical 问题达成共识）

---

## Summary

本文提出 recursive generation depth estimation 作为新任务（ordinal classification），构建了覆盖 3 model families × 3 decoding strategies × 4 depths 的 180K 样本 benchmark，使用 19 个统计特征 + Random Forest 达到 70-85% 四分类准确率（chance=25%）。论文引入 Depth Degradation Atlas 系统性刻画递归生成下文本统计特性的演变，定义 Effective Discriminable Depth (EDD) 量化相邻深度可区分的边界。跨模型迁移 66.4%、跨策略迁移 59.1%。发现 temperature sampling 导致 d1/d2 AUC 反转，以及 DCOL end-to-end 方法的 negative result。

---

## Strengths

**S1** [共识] 问题定义 genuinely novel。Recursive generation depth estimation 是真正未被填补的空白——现有工作仅做 binary detection 或假设 depth 已知。Task formalization（ordinal classification）合理清晰，EDD metric 有独立学术价值。

**S2** [共识] 实验设计系统性强。3×3×4 的 Atlas 结构提供了多维度 controlled comparison，180K 样本量充足。比 "单模型单策略" 的实验设计强得多。

**S3** [共识] Feature universality 是有价值的科学发现。p90_ppl 在 9/9 cells top-2、cross-cell Spearman ρ=0.868，即使理论上可预期（Shumailov/Dohmatob 已预测 tail erosion），实证验证仍有价值。

**S4** [共识] Temperature-induced d1/d2 AUC inversion 是实质性 insight，对跨策略部署有直接指导价值。

**S5** [共识] EDD threshold sensitivity analysis（Table 3）和 granularity ablation 展示负责任的实验报告态度。Limitations section 坦诚透明。

---

## Weaknesses（按严重程度排序）

### Must-Fix（影响接收决定）

**N1** [critical, 共识] **EDD 公式存在系统性 off-by-one 错误**
Eq. 1 定义 EDD_T = max{d* : AUC(d*, d*+1) ≥ T}，d* ∈ {0,...,K-1}。以 Pythia nucleus d0-d5 T=0.75 为例：AUC(3,4)=0.784≥0.75 → d*=3，但全文（Abstract, Section 4.3, Table 3, Conclusion）报告 EDD=4。Table 3 所有行验证均差 1。这是论文四项贡献之一的核心 metric，公式与报告值不一致直接损害技术可信度。
→ 修正 Eq.1 为 EDD_T = max{d*+1 : AUC(d*,d*+1) ≥ T}，或全文数值下调 1。

**N2** [critical, 共识] **DCOL negative result 证据严重不足**
仅测试 1 个架构（RoBERTa-large）、1 个方法框架（DCOL）、6 个配置（5 个因 embedding collapse/OOM/NaN 失败），超参未报告。未测试任何简单 end-to-end baseline（如 RoBERTa-base finetune 4-class）。CLOC (CVPR 2025) 在 bib 中却未测试或引用。从 1 个方法的 1 次成功 run 外推到 "end-to-end models struggle to extract depth info" 属于 overclaim。
→ 补充 2-3 个简单 end-to-end baselines，报告完整超参，弱化结论为 preliminary evidence。

**N3** [critical, 共识] **主实验缺乏不确定性量化**
Table 1（9 cell accuracy）和 Table 2（baseline comparison）无 std/CI。5-fold CV 完全可以报告 fold-level std（成本为零）。RF 78.2% vs DivEye 78.2% 差异 0.0pp、RF vs MLP 差异数 pp，无 significance test 无法判断是否显著。Figure 2 有 bootstrap CI 说明作者知道如何做——但未应用到主表格。
→ Table 1/2 报告 mean±std；对关键比较做 paired t-test 或 bootstrap。

**N4** [critical, 共识] **Mohamed et al. (ACL 2025) "LLM as a Broken Telephone" 高度相关但未讨论**
该论文研究 LLM 迭代生成中的信息失真，概念上与 recursive depth estimation 直接相关。引用已存在于 references.bib (key: mohamed2025_broken_telephone) 但正文从未引用——orphan entry 暴露了 related work 覆盖不完整。
→ 在 Related Work "Adjacent Tasks" 中讨论，区分信息失真量化 vs 递归深度估计。

### Should-Fix（影响评分但不一票否决）

**W1** [warning, 共识] Feature importance (Gini) 受 correlated features 影响——19 features 中 perplexity percentiles 和 surprisal statistics 存在强数学相关，Gini importance 会在相关特征间分散权重，p90_ppl/var_surprisal 的 "universality" claim 可能不可靠。建议提供 correlation matrix + permutation importance。

**W2** [warning, 共识] Wikipedia seed text 引入 domain bias——d0 recall >99% 可能部分反映文体特征。3-class accuracy (d1-d3) 70.8-82.0% 提供部分缓解，但建议用非 Wikipedia domain 做 pilot validation。

**W3** [warning, 共识] LoRA 参数 (r=16, α=32, lr=2e-4) 缺乏选择依据和 sensitivity analysis——参数直接决定 depth signal 强度，结论可能是 hyperparameter-specific。

**W4** [warning, 共识] Zero-shot LLM baseline (DeepSeek V3.2) 仅 200 samples, ±6.8pp CI——统计可信度不足以支撑与 20K sample 方法的直接比较。

**W5** [warning, 共识] 5-fold CV 未说明是否按 passage lineage 分组——同一 seed text 的跨 depth descendants 若未在同一 fold，存在数据泄漏风险导致 accuracy 乐观偏估。作者必须 clarify。

**W6** [warning, 共识] Cross-strategy transfer (Table 4) 未报告 per-class recall——考虑到 temperature d1/d2 inversion，per-class 信息尤为关键。Cross-model transfer (Table 3) 有 per-class recall，此处缺失不一致。

**W7** [warning, 共识] Temperature inversion 仅在 τ=0.9 验证——缺乏 multi-τ ablation 支撑因果解释。如不做 ablation，应弱化为 observational finding。

**W8** [warning, 共识] Limitations section 位置不当——当前嵌套在 Discussion (Section 6.2)，ACL 模板要求独立 unnumbered section 在 Conclusion 之后。

**W9** [warning, 共识] 4 个 orphan bib entries (cloc2025, dohmatob2024_demystified, dohmatob2024_strong_collapse, mohamed2025_broken_telephone)——应整合到正文或清理。

**W10** [warning, 共识] 术语不一致 var_surprisal vs var_surp——Abstract/Introduction 与 Section 4.2 使用不同缩写。

### Minor（不影响接收）

- M1: var_surprisal 与 perplexity variance 的数学关系未明确说明
- M2: RF 200/500 trees 无 convergence analysis
- M3: DCOL "v6" 暗示 v1-v5 但未报告配置
- M4: Appendix 过薄（仅 11 行 top-k 描述，无图表）
- M5: 全文未提及代码/数据/模型开放计划，影响 reproducibility 评分
- M6: DivEye venue 可能有误（R2 称 ICLR 撤回至 TMLR，R1 无法验证，存分歧，需作者核实）
- M7: 多个 bib entry 标题可能不完整（R2 指出，R1 未复现，存分歧，需作者核实）
- M8: Abstract "70-85%" 实为 69.6-85.4%，严格来说不够精确
- M9: Figure 3 caption 提到 Appendix 有 top-k 图表但实际仅文字描述

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：

| 问题 | R1 | R2 | 共识 |
|------|----|----|------|
| EDD off-by-one | N1 (发现者) | 验证确认 | ✓ Critical |
| DCOL 证据不足 | N3 | N1 | ✓ Critical，独立发现 |
| 不确定性量化缺失 | N2 | 同意 (建议分级) | ✓ Critical |
| Mohamed et al. 遗漏 | 同意 | N2 (发现者) | ✓ Critical |
| Feature correlation | W1 (发现者) | 同意并补充 | ✓ Warning |
| Domain bias | W2 (发现者) | 同意 | ✓ Warning |
| LoRA justification | W3 (发现者) | 同意 | ✓ Warning |
| LLM baseline 样本量 | W4 (发现者) | 同意 | ✓ Warning |
| Passage lineage 泄漏 | W5 (发现者) | 同意 | ✓ Warning |
| Cross-strategy recall | W6 (发现者) | 同意 | ✓ Warning |
| var_surp 术语不一致 | 同意 | W2 (发现者) | ✓ Warning |
| Multi-τ ablation | 同意 | W3 (发现者) | ✓ Warning |
| Limitations 位置 | 同意 | W4 (发现者) | ✓ Warning |
| Orphan bib entries | 同意 | W6 (发现者) | ✓ Warning |
| 问题定义新颖 | S1 | S1 | ✓ 核心优势 |
| 实验系统性强 | S2 | S2 | ✓ 核心优势 |
| Temperature inversion 有价值 | S3 | 同意 | ✓ 核心优势 |
| Main/Findings borderline | 3/5 | 3.0/5 | ✓ 评分一致 |

## Reviewer Divergence

| 问题 | R1 | R2 | 备注 |
|------|----|----|------|
| DivEye venue 是否有误 | REBUT（无法验证） | W1（称 ICLR→TMLR） | Minor，需作者核实 |
| Bib 标题是否被截短 | REBUT（未复现） | W5（指出 3 个条目） | Minor，需作者核实 |

**分歧仅存在于 2 个 minor bibliographic 问题，所有 critical 和 warning 问题均无分歧。**

---

## Questions for Authors

**Q1** [两位 Reviewer 共同关注] Eq. 1 的 EDD 公式与全文报告值存在系统性 +1 偏差——请确认是公式需修正还是报告值需修正。

**Q2** [两位 Reviewer 共同关注] 5-fold CV 的 split 策略是否考虑了 passage lineage？如果同一 seed text 的 d0/d1/d2/d3 passages 不在同一 fold，accuracy 可能因内容相似性被高估。

**Q3** [两位 Reviewer 共同关注] DCOL 6 个配置的具体超参是什么？为何选择 DCOL 而非 CLOC (Pitawela et al., CVPR 2025)？是否尝试过直接 finetune RoBERTa-base 做 4-class classification？

**Q4** [R1] 能否提供 19 特征的 correlation matrix？Feature universality 是否可能因 reference model (GPT-2 base) 的选择而产生 artifact？

**Q5** [R2] 为什么 ppl-regression baseline (mean perplexity) 表现为 chance level (25.1%)？所有 features 都 monotonically decrease with depth，mean perplexity 也应有 monotonic trend，为何单特征分类接近 random？

**Q6** [R2] Mohamed et al. (ACL 2025) "LLM as a Broken Telephone" 在 bib 中但未被讨论，为什么？

**Q7** [两位 Reviewer] 是否计划公开代码、数据和训练好的分类器？

---

## Missing References

- **Mohamed et al. (ACL 2025)** "LLM as a Broken Telephone: Iterative Generation Distorts Information" — bib 中存在但未引用，高度相关
- **Dohmatob et al. (ICLR 2024)** "Strong Model Collapse" — bib 中存在但未引用，进一步 formalize collapse dynamics
- **Dohmatob et al. (NeurIPS 2024)** "Model Collapse Demystified" — bib 中存在但未引用
- **CLOC (Pitawela et al., CVPR 2025)** — bib 中存在但未引用，ordinal contrastive learning 方法，与 DCOL 直接相关

---

## Overall Assessment

**评分: 3/5 — Weak Accept (Findings track)**
**置信度: 4/5**

两位 Reviewer 评分完全一致（R1: 3/5, R2: 3.0/5），均推荐 Findings track acceptance。

**核心判断**：论文提出了一个 genuinely novel 且有实际价值的问题（recursive generation depth estimation），实验设计系统性强（180K 样本、9 configurations），发现了有价值的 empirical regularities（feature universality, strategy-dependent trajectories, EDD boundary）。但存在 4 个 critical 问题需要修复：(1) EDD 公式 off-by-one 错误损害核心 metric 可信度；(2) DCOL negative result 证据严重不足（论文最薄弱的贡献点，两位 Reviewer 独立一致）；(3) 主实验无不确定性量化；(4) 高度相关的 ACL 2025 工作未讨论。

**升级路径**：若 N1-N4 均修复（特别是补充简单 end-to-end baselines 和统计显著性），论文有望从 Findings 升级至 Main conference level。问题定义的新颖性和 Atlas 的系统性分析是其最强卖点，方法贡献的轻量化（RF + handcrafted features）是主要限制。

---

## Detailed Comments（逐节）

### Abstract
- 数字准确（70-85% 对应 69.6-85.4%，可接受的四舍五入）
- "universal depth markers" 稍显 strong（仅 3 个 1-1.5B 模型验证）
- EDD₀.₇₅=4 存在 off-by-one 问题（N1）

### Introduction (Section 1)
- Motivation 清晰，从 model collapse 引出 depth estimation 需求
- 贡献列表 4 项：前 3 项扎实，第 4 项（DCOL negative result）证据不足（N2）
- 写作质量好，逻辑流畅

### Related Work (Section 2)
- Model collapse 和 AI text detection 覆盖全面
- 遗漏 Mohamed et al. (ACL 2025)（N4）
- 4 个 orphan bib entries 需清理（W9）

### Task Formulation (Section 3)
- 问题定义严密，ordinal classification formalization 合理
- EDD 定义 (Eq.1) 有 off-by-one 错误（N1）
- Feature design 有理论依据但未量化 feature 间相关性（W1）
- Reference model 选择的 circularity 在 Discussion 有讨论，可接受

### Depth Degradation Atlas (Section 4)
- 9-cell 实验覆盖系统性强
- Table 1 无 std/CI（N3）
- Feature universality 发现有价值但需 robustness check（W1）
- EDD sensitivity analysis 好但数值因 off-by-one 全部偏移
- Strategy trajectory 分析深入，three-tier taxonomy 有见地

### Generalization (Section 5)
- Cross-model/strategy transfer 实验设计合理
- Table 2 baseline 比较无 significance test（N3）
- Cross-strategy table 缺 per-class recall（W6）
- DCOL section 是全文最薄弱环节（N2）
- LLM baseline 样本量不足（W4）

### Discussion (Section 6)
- Implications 讨论合理
- Limitations 坦诚但位置不当（W8）
- 未讨论 cross-strategy deployment 的具体约束（应加入 per-strategy d1v2 AUC 数据）

### Conclusion (Section 7)
- 准确总结全文，无 overclaim（除 EDD 数值）
- Future work 方向合理

### Appendix
- 过薄，仅 11 行文字描述 top-k trajectories
- 建议补充：DCOL 配置详情、confusion matrices (9 cells)、correlation matrix、per-class distributions
