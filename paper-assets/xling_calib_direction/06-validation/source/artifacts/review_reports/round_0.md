---
round: 0
review_mode: 
overall_score: borderline accept
timestamp: 2026-05-21T06:21:22.852138+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告 — Median Paper（更正版）

**论文**: Cross-Lingual Correctness Probe Transfer Reveals Architecture-Dependent Pareto Frontiers: Discovery, Negative Result, and Practical Recommendation
**Tier**: Dream Median
**目标 Venue**: Top ML venue (ACL-level)
**审稿模式**: 圆桌会议（2 Reviewers, 1 轮 + 交叉审阅）
**日期**: 2026-05-21
**备注**: 本报告替换先前误投递的版本——先前版本错误地将 worst-tier R1 审稿（2/5）归属为 median paper 的交叉修订。

---

## Panel Summary

| Reviewer | Focus | Initial | Post-discussion | Confidence |
|----------|-------|---------|-----------------|------------|
| R1 | Methods & Experiments | 4/5 (Weak Accept) | 4/5 (Weak Accept) | 4/5 |
| R2 | Novelty & Related Work | 3/5 (Findings) | 3/5 (Findings) | 4/5 |
| **Consensus** | | | **3.5/5 (Borderline Accept / Findings)** | |

**Overall Assessment**: Borderline Accept — 推荐 Findings track 接收。论文在统计方法论、内部一致性和学术诚实度上显著优于同 agenda 的 best-tier 版本。控制任务发现（37-42% artifact rate）具有 field-level 价值。CaCLR negative result 的实验设计充分（β sweep 3 OOM, component ablation）。主要不足在于零可视化、引用偏少、Gemma 4 数据不对等、以及 "only viable path" 对 linear projection 的 overclaim。

---

## 1. Summary

本文系统地将跨语言 correctness probe transfer 从 pilot（7-8B 模型）扩展至 3 个大规模架构（Qwen3-235B MoE, Llama 4 Scout MoE, Gemma 4 31B Dense）× 20 语言 × 5 迁移条件。三段叙事结构：(1) Discovery——architecture-dependent Pareto frontier（Qwen3 全负 ρ, Llama4 4/20 正, Gemma4 最强负）；(2) Negative result——CaCLR distributional matching 方法有害（β sweep 3 OOM, d=0.07, p=0.38），pilot 的 CKA-transfer 正相关被确认为 Simpson's Paradox；(3) Practical recommendation——linear projection 在特定条件下可行，~50 pairs 达 90% improvement。最有价值的方法论贡献是将 Hewitt & Liang selectivity controls 引入跨语言 probing，发现 37-42% 中低资源 probing 结果为 capacity artifacts。

---

## 2. Strengths

- **S1 [Consensus]**: **控制任务方法论是论文锚点**——Hewitt & Liang (2019) selectivity 首次系统应用于跨语言 probing。LOW tier 42% artifact rate, HIGH tier 18%。selectivity-AUROC 相关 ρ=0.68 (p<0.001)。对整个跨语言 probing 社区有方法论警示意义。

- **S2 [Consensus]**: **统计方法论 above-average**——Bonferroni correction、bootstrap 95% CIs、paired permutation tests、Cohen's d 贯穿全文。这是 probing 文献中的上游标准。

- **S3 [Consensus]**: **诚实的负面结果 framing**——Abstract 开门见山 "predominantly negative"，每个 claim 有 qualifier（"suggestive", "qualitative"）。Claims 校准到 evidence 水平，无 overclaim。

- **S4 [Consensus]**: **Simpson's Paradox falsification**——5-language pilot CKA-transfer 正相关在 20 languages 下崩溃（partial ρ=+0.14, p=0.22）。教科书级 ecological fallacy 案例。

- **S5 [R1]**: **CaCLR negative result 实验充分**——β sweep 3 OOM (0.001→1.0), monotonic degradation, component ablation（每项净负），两种架构一致。不留"未调参"空间。

- **S6 [R1]**: **CKA 自我纠正**——pooled r=0.52 做 partial correlation controlling depth 后降为 r=0.18 (p=0.11)，主动降级为 suggestive。

- **S7 [R1]**: **Llama 4 Scout 的 4/20 语言 ρ>0** 是 genuinely new observation——不是 "deeper=worse" 的简单重复，而是发现某些语言在 MoE 架构上 deeper layers transfer better。

- **S8 [Consensus]**: **内部一致性完美**——Abstract 数字与正文完全吻合，无任何自相矛盾。13/13 实验计划全部覆盖。

---

## 3. Weaknesses

### 3.1 Moderate Issues（影响评分但不阻止接收）

**W1. MMD 仅在 1-D probe logits 上测试——negative result scope 受限** [Consensus]

§3.2 承认 "design limitation: only match marginal distributions of scalar outputs"。但 §6 的推论隐含更广的 claim。未测试 activation-space MMD 或 optimal transport。严格来说，论文仅关闭 "1-D probe output MMD matching" 而非 "distributional matching for cross-lingual probe transfer" 的全部。

R2 补充：事前 MMD on probe outputs 并非 obviously 会失败——这是 Ben-David et al. domain adaptation 理论的自然实现。论文的 framing 有 caveat（§3.2, §6），逻辑自洽，但 scope 限制降低了对 community 的警示广度。

**W2. Gemma 4 31B 数据严重不对等** [Consensus]

仅 Table 14 的 3 行摘要（Appendix），无 per-language breakdown、β sweep、control task analysis。"Architecture-dependent" claim 实质仅基于 Qwen3 和 Llama4 两个 MoE 架构。Gemma4 是唯一 Dense 架构——缺其完整数据使 MoE vs Dense 对比无法完成。

**W3. "Only viable path" overclaim——few-shot 100 实际优于 linear projection** [Consensus: R1 raised key evidence, R2 endorsed]

Table 21 显示：
- Linear Proj 200: AUROC .610, Sig. impr. 11/20
- Few-shot 100: AUROC .623, Sig. impr. 13/20

Few-shot 100 在 AUROC 和 significant improvement count 上均优于 Linear Proj 200。论文声称 linear projection 是 "the only viable transfer method"（§1, §5.6），但这仅在 "zero-correctness-label" 条件下成立。当前措辞对读者有误导——应改为 "the only viable label-free transfer method"。

此外，Table 15 的 effect-reversal zone [0.48-0.68] 覆盖 16/20 语言。§6 的 conditional recommendation 仅适用 ~4/20 语言，practical guidance 近乎空洞。

**W4. Difficulty decomposition 否定太快** [Consensus]

§5.4 一段话否定。IRT R²=0.40/0.31——difficulty probe 只捕获 31-40% variance，projecting out 的是噪声方向。Random-direction control 产生同量级效果（Δ=-0.005 vs -0.003, p=0.42）与 "poor difficulty probe" 和 "no decomposition" 两种解释均一致。论文未分析：(a) 更复杂的 difficulty model 是否改变结论，(b) scale 效应，(c) 量化效应对 difficulty signal 的影响。

### 3.2 Minor Issues

**W5. 23 张表格、0 张图** [Consensus]

核心负面结论极适合可视化：Pareto scatter plot、CaCLR β sweep 折线图、Simpson's Paradox 分组 scatter、selectivity heatmap、linear projection learning curve。表格密集增加审稿负担。

**W6. 引用偏少（~15-17 篇）** [Consensus]

虽比 best-tier 版本（8 篇）改善，仍低于顶会标准（30-50 篇）。缺 IRT 基础文献（Lord 1980, Baker 2001）、Belinkov (2022) probing survey、Guo et al. (2017) temperature scaling、Conneau et al. (2020)、Pires et al. (2019)。R2 报告 References section 不醒目——R1 确认 section 存在（p.10 下半部分）但排版需改善。

**W7. Pilot work 区分不充分** [Consensus]

未说明 pilot（Qwen2.5-7B, Llama-3.1-8B）是已发表还是未发表。影响 §5.3 Simpson's Paradox 分析的可验证性。

**W8. "First systematic study" overclaim** [Consensus]

鉴于 Civelli et al. 和 Xiao et al. 先行工作。建议改为 "first study to apply probing control tasks to cross-lingual calibration transfer"——更准确反映真正新贡献。

**W9. CaCLR 失败减少论文正面贡献数量** [R2]

论文实质贡献为 (1) 控制任务方法论 (2) systematic negative result (3) practical guidance。R1 认为 well-executed negative result 有独立出版价值；R2 认为对 main conference excitement 不足。共识：Findings track 可接受。

---

## 4. Reviewer Consensus [AGREE]

1. **控制任务发现是最强贡献**（37-42% artifact rate，field-level 价值）
2. **统计方法论扎实**，内部一致性完美
3. **CaCLR negative result 实验设计充分**但 scope 受 1-D MMD 限制
4. **零可视化**是严重表述问题
5. **引用偏少**但比 best-tier 版本改善
6. **"Only viable path" overclaim**——few-shot 100 实际优于 linear projection（Table 21 关键证据）
7. **Difficulty decomposition 否定太快**——IRT R² 过低可能导致 false null
8. **Findings track 接收合适**

---

## 5. Reviewer Divergence

**5.1 评分差距的根本原因**

- **R1 (4/5 Weak Accept)**: 更重视方法论执行质量。认为 0 Major issues + thorough negative result + honest framing + above-average statistics = Findings-level contribution。"Well-executed negative result 有独立出版价值。"
- **R2 (3/5 Borderline)**: 更重视正面贡献强度。认为 control task finding 是唯一 field-level 贡献，negative result scope 受限（1-D MMD），Gemma 4 不对等削弱三架构 claim。"统计执行是必要条件而非充分条件。"

**Director 判断**: 两位 Reviewer 的分歧是价值取向差异（执行质量 vs 贡献数量），而非事实分歧。双方均认可 Findings track 适合。综合评分 3.5/5——偏向 Findings track 接收，不足 main conference。

**5.2 CaCLR negative result 的独立价值**

- R1: 有独立价值（well-executed systematic null = informative closure）
- R2: 有价值但 scope 有限（仅关闭 1-D MMD 这一条路）；事前非 obvious 但也非 surprising
- 共识: Moderate novelty，对 Findings track 足够

---

## 6. Questions for Authors

1. CaCLR 的 L_cons 使用 MMD 在 1-D probe logits 上。是否考虑过 activation-space MMD 或 optimal transport？如果 Zhao et al. 理论排除所有 marginal matching，需在 §6 更明确论证。
2. Gemma 4 31B 的完整 per-language breakdown 和 transfer comparison 是否可用？
3. IRT difficulty probe R²=0.31-0.40——是否尝试过 2-PL IRT 或 neural IRT？
4. Table 21 中 few-shot 100 (AUROC .623, 13/20 sig.) 优于 linear proj 200 (.610, 11/20 sig.)——为什么论文仍称 linear proj 是 "only viable path"？
5. Table 1 的完整 24 层 × 20 语言数据可否放入 supplementary？
6. Pilot studies 是已发表还是未发表前期工作？
7. Control task selectivity 阈值 < 0.05 的选择依据？改为 0.10/0.03 时 42% 如何变化？
8. §5.1 Gemma4 "moderately clear frontier" vs Summary "does not generalize" 是否矛盾？
9. 代码和 probing 数据是否有公开计划？

---

## 7. Missing References

1. Conneau et al. (2020) — XLM-R
2. Pires et al. (2019) — Multilingual BERT analysis
3. Belinkov (2022) — Probing survey
4. Lord (1980) / Baker (2001) — IRT foundational
5. Guo et al. (2017) — Temperature scaling
6. Keleg & Magdy (2023) — Multilingual calibration
7. Ganin et al. (2016) / Long et al. (2015) — Domain adaptation
8. Fedus et al. (2022) — MoE analysis

---

## 8. External Review

**状态: pending**

---

## 9. Visual Layout Check

**状态: not_started**（PDF 路径未配置）

---

## 10. Overall Assessment

**评分: 3.5/5 — Borderline Accept (推荐 Findings track)**

**置信度: 4/5**

**核心判断**: 这是一篇学术品质显著优于同 agenda best-tier 版本的论文。控制任务发现（37-42% artifact rate）是真正的 field-level 贡献。CaCLR negative result 的实验设计充分（β sweep 3 OOM, component ablation, 两架构一致）。统计方法论在 probing 文献中属于上游。内部一致性完美。

不足以升至 main conference 的原因：
1. 负面结果 scope 受限（仅 1-D MMD），无法断言 "distributional matching 全部失败"
2. Gemma 4 数据不对等使三架构 claim 不完整
3. "Only viable path" overclaim——few-shot 100 实际上更好
4. 零可视化和引用偏少影响 presentation

**修改建议优先级**:
1. [重要] 添加 2-3 个核心 figure（selectivity heatmap, Simpson's Paradox scatter, Pareto comparison）
2. [重要] 补充 Gemma 4 完整数据
3. [重要] 修正 "only viable path" → "only viable label-free method"，坦诚讨论 few-shot 100 的优势
4. [建议] 扩展引用至 30+ 篇
5. [建议] 补充 activation-space MMD 实验（即使失败也扩大 scope）
6. [建议] Decomposition §5.4 补充失败原因分析

**与 Best-tier 对比**:

| 维度 | Best (2.5/5 Weak Reject) | Median (3.5/5 Borderline Accept) |
|------|--------------------------|----------------------------------|
| 内部一致性 | 差（72%/81%/25% 矛盾） | 完美 |
| 统计严谨性 | 差（无 CI/检验） | 好（Bonferroni/CIs/Cohen's d） |
| 学术诚信 | 差（疑似 fabricated refs） | 好（诚实负面结果） |
| 引用 | 8 篇（严重不足） | ~15 篇（偏少但有结构） |
| 控制任务 | 无 | 42% artifact（field-level） |
| 核心缺陷 | 可信度危机 | Scope 限制 + 数据不对等 |
| 可修复性 | 低 | 高 |
| 推荐 | Reject → Revise | Findings track 接收 |

---

## 11. Detailed Comments

### §1-2
- "First systematic study" → "first study applying probing control tasks to cross-lingual calibration"
- Related Work 覆盖 5-6 子方向，结构合理，但缺核心引用

### §3
- §3.2 MMD scope caveat 好，但 §6 推论过广
- "Two regularization terms" 应为 three（公式有 3 项额外 loss）

### §5
- §5.1 Llama4 的 4/20 正 ρ 是 genuinely new finding
- §5.3 Simpson's Paradox 分析方法论值得肯定
- §5.4 Decomposition 否定太快——IRT R²=0.31 是 probe quality 问题
- §5.5 Control task 是论文锚点
- §5.6 Linear projection recommendation 需坦诚讨论 reversal zone + few-shot 对比

### Appendix
- Table 14 Gemma4 需大幅扩充
- References section 存在但不醒目（R2 漏看），排版需改善