---
round: 7
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-28T02:17:15.181579+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 7 (Fresh)

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**目标 Venue**: CoRL 2026 (10th Conference on Robot Learning)
**截止日期**: 2026-05-28 UTC 12:00
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法/实验/数据透明度; R2: 新颖性/venue fit/格式/完整性）

---

## Summary

本文识别了 DreamerV3 中引入变速率时间抽象（variable-rate temporal conditioning）时出现的一种失败模式——conditioning-induced value overestimation (CIVO)。通过 43 个实验配置 × 4-5 seeds 的 factorial 分析，论文确定 trained dt-embedding + multi-rate data exposure 是 CIVO 的 jointly sufficient 预测因子（NVE ≥ 2.0× 阈值，AUROC=1.000，n=36）。四级干预层级（gradient → output → representation → architecture）测试表明无干预能可靠消除 CIVO。论文还提出了 NVE 在线检测器（TPR=5/5, FPR=2/9）。

论文实验规模大、数据透明度极高（35 页 Appendix，per-seed 结果，code correction 完整记录），但存在两个独立的 desk-reject 级别问题（正文超页 ~2.5 页 + CoRL venue fit 不足），以及多个方法论层面的关切。

---

## Strengths

1. **实验规模与系统性设计**: 43 个实验配置，208 个独立训练 run，factorial design 系统隔离 dt-embedding/subsample/horizon/step-size 四因素。四级干预层级从 gradient 到 architecture 逐层诊断，方法论严谨。

2. **数据透明度标杆级别**: 完整 per-seed 结果（Table 3, 37-38 页）、code correction 历史（Appendix I, Table 32）、版本控制记录。Appendix 共 31 页，几乎每个声明都有 backing data。这种透明度在 MBRL 论文中极为罕见。[R1 R2 共识]

3. **NVE 诊断指标有实用价值**: NVE 定义简洁（仅需 critic value 和 eval return），AUROC=1.000（n=36），LOEO/LOCO 交叉验证完整。Online CIVO Detector（Algorithm 1）可直接部署，不增加额外计算开销。

4. **诚实的负面结论**: 坦承四种干预均无法在所有环境中完全消除 CIVO，未过度声称 solution。这种科学诚实比包装不可靠的 fix 更有价值。[R1 R2 共识]

5. **写作质量高**: 论文组织清晰，Figure 1 的 CIVO 双路径机制图高效传达核心思想，findings F1-F7 的递进叙事逻辑连贯。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W-MF1** [critical] **正文严重超页: ~10.5 页 vs CoRL 8 页限制** [R2-N1, Director 独立确认]
- 正文内容（Section 1 至 Broader Impact Statement 结束）约 10.5 页，超限约 2.5 页
- CoRL 2026 Instruction for Authors 明确限 8 页正文 + 无限引用，超页可直接触发 desk rejection
- Discussion（~1.5 页）大量重复 Section 4 的 findings；Experimental Setup（3.3-3.8 共 8 个子节，~1.5 页纯文本）细节可移至 Appendix
- **Desk reject 风险: 极高**

**W-MF2** [critical] **Venue Fit 严重不足: 核心贡献是通用 RL 诊断，非 robotics-specific** [R1-W3, R2-N2; R2 给 Relevance 1/5]
- CoRL 2026 CFP 明确要求 "Submissions must focus on a core robotics problem"，鼓励 real-robot experiments 或 convincing sim-to-real evidence
- CIVO 的成因（dt-conditioning + imagination value overestimation）在任何使用 DreamerV3 temporal abstraction 的领域均会出现，非机器人特有
- 所有实验在 DMC locomotion（Walker Walk, Cheetah Run）+ ManiSkill manipulation 上进行，无真实机器人实验、无 sim-to-real 验证、无高维视觉控制
- Practitioner guidelines（冻结 dt-embedding、NVE 监控）适用于任何 DreamerV3 场景，无 robotics 特异性
- **本文曾在 Round 1-3 以 CoRL 为目标，Round 4 因 venue fit 问题切换至 ICML，现再次切回 CoRL——原始问题未解决**
- **Desk reject 风险: 高**

**W-MF3** [critical] **因果机制声明超出观测证据强度** [R1-N2, R2-W1; 共识]
- Figure 1 提出四步反馈环机制，但实验证据是 observational ablation——证明了必要条件，非直接因果证明
- Step 3→4（value overestimation → exploitative policy）无直接 policy behavior 分析
- Step 4→1（biased data → further embedding bias）完全是推断
- 与 Janner et al. 讨论的 compounding model error 概念上高度相似，缺乏形式化理论区分
- Section 5 称 CIVO 是 "structural vulnerability, not regularization deficiency" 但无形式化证明

**W-MF4** [critical] **AUROC=1.000 on n=36 缺乏不确定性量化** [R1-N1]
- 未报告 bootstrap confidence interval；n=36 上单个误分类使 AUROC 降至 ~0.97
- LOEO 仅涵盖 3 个环境，每个 fold 留出集极小
- n=36 中 CIVO-positive vs non-CIVO 的类别比例（9:27）未在主文明确报告
- "Perfect classification" 声明在如此小样本上可能是假象

**W-MF5** [critical] **统计效力不足以支撑部分关键声明** [R1-N3]
- 4-5 seeds 的 IQM（中间 2-3 值均值）每配置效果估计噪声极大
- 多处 seed-level 叙述性声明（"seed 3 shows early collapse"）不构成统计证据
- Table 2 干预效果比较基于极小样本（如 "2/4 Walker seeds = 50%"），置信区间极宽
- 缺乏 effect size confidence intervals 和 formal statistical tests

**W-MF6** [critical] **纯诊断 + 负面结论在 CoRL 的 significance 偏低** [R2-N3, R1 部分同意]
- 核心结论是 "no tested intervention reliably eliminates CIVO"
- "冻结 dt-embedding" 等于放弃 temporal abstraction 的全部价值——不是真正的解决方案
- CoRL 社区高度重视 practical impact；negative result papers 在 robotics venues 接受门槛极高

### Should-Fix（影响评分但不一票否决）

**W-SF1** [warning] NVE 阈值 2.0× 选取存在潜在循环性 [R1-W1]
- 阈值从同一数据集选出并在同一组环境上 cross-validate，不构成 external validation
- 在新颖环境类别上的有效性完全未知

**W-SF2** [warning] Factorial design 未完全分离 embedding 架构与训练信号 [R1-W2]
- "trained dt-embedding" 同时引入架构变化和训练信号变化
- Frozen embedding 的初始化策略可能影响结论

**W-SF3** [warning] Table 1 脚注 f ("corrected-code rerun") 影响范围需汇总 [R1-W4, 延续 N-R6-1/N-R6-3]
- 代码修正影响了多少配置的 CIVO 分类标签？修正前后 AUROC 是否变化？
- Appendix I 有 code correction 历史但缺汇总统计

**W-SF4** [warning] "pathway redundancy" 声明缺乏统计检验 [R1-W5]
- Table 2 prevention rates 基于极小样本，无 Fisher exact test 或 bootstrap comparison

**W-SF5** [warning] 诊断协议通用性未经验证——仅 DreamerV3 [R2-W3]
- "Transferable diagnostic protocol" 声明但仅在一个算法上验证

### Minor

- Figure 3 seed 曲线颜色区分度不足，灰度打印下难以辨别 [R1-M2]
- Table 1 信息密度极高（43 配置），需 summary statistics 帮助读者把握全局 [R1-M3, R2-M2]
- Section 3.5-3.6 干预方法描述可更紧凑 [R1-M4]
- Figure 1 流程图内文字偏小（约正文 60-65%），打印时可能难以辨认 [R2-M1, Visual Check]
- Contribution list 中 "preliminary diagnostics" 与 "failure mode identification" 分类不够正交 [R2-M3]
- NVE 数学定义应在正文给出完整公式形式 [R1-M1]

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成共识：

1. **环境多样性不足**: 仅 Walker Walk + Cheetah Run 两个 DMC locomotion 环境，缺少 contact-rich manipulation、navigation、high-dimensional observation、real-robot 验证。对 CoRL 的 robotics relevance 构成显著减分。[R1 5/10 relevance, R2 1/5 relevance]

2. **数据透明度优秀**: 35 页 Appendix、per-seed 结果、code correction 历史——在 MBRL 论文中标杆级别。

3. **因果声明过强**: Figure 1 的 feedback loop 机制超出了 observational ablation 能支撑的证据强度。需弱化为 "proposed/hypothesized mechanism"。

4. **诚实负面结论有价值但 significance 受限**: 坦承无有效缓解方案是科学诚实的体现，但在 CoRL 语境下 practical impact 不足。

5. **统计效力有限**: 4-5 seeds 在 RL 实验中是合理的（per Agarwal et al. 2021），但论文的定量声明精度超出了统计效力能支撑的范围。

---

## Reviewer Divergence [REBUT]

以下问题两位 Reviewer 存在显著分歧：

1. **页数违规严重性**: R2 认为 desk-reject 级别（10.5 vs 8 页），R1 未单独标记页数问题。**Director 判断**: 客观超页 ~2.5 页，确实构成 desk-reject 风险。R2 评估准确。

2. **Venue fit 致命程度**: R2 给 Relevance 1/5（desk-reject），R1 给 5/10（弱但非致命）。**Director 判断**: CoRL CFP 明确要求 robotics focus，本文曾因同一问题在 Round 4 切换至 ICML。R2 的评估更贴合 CoRL 的 scope 要求。

3. **整体评分**: R1=6/10 vs R2=3/10。差距主要来自格式合规和 venue fit 的权重分配。R1 更侧重 methodological quality（确实较高），R2 更侧重 venue appropriateness（确实不足）。

---

## Questions（需作者在 rebuttal 中回答）

1. 为什么从 ICML 切回 CoRL？ICML 语境下多个先前 reviewer 认为论文的 diagnostic/negative-result 贡献模式合理，切回 CoRL 重新引入了 Round 1-3 已识别的 venue fit 风险。

2. n=36 中 CIVO-positive 和 non-CIVO 的精确数量是多少？类别比例如何影响 AUROC 的可靠性？（从 Appendix B.4 推断为 9:27，但主文未明确报告。）

3. 代码修正（Appendix I）总共影响了多少个配置的 CIVO 分类标签？修正前的 AUROC 是多少？

4. Figure 1 四步反馈环中，Step 3→4 和 Step 4→1 的直接实验证据是什么？如果没有，是否应标注为 hypothesized？

5. 论文声称 "transferable diagnostic protocol"（Section 5），但仅在 DreamerV3 上验证。是否有计划在 TD-MPC2 或其他 imagination-based 架构上测试？

6. 如何将正文从 ~10.5 页压缩至 8 页？哪些内容可以移至 Appendix 而不损失核心论证？

---

## Missing References

R2 标记以下可能缺失的引用：
- **FiGAR** (Sharma, Lakshminarayanan, Ravindran, 2017): Fine Grained Action Repetition for Deep RL — 与 variable-rate control 直接相关
- **DAC** (Zhang & Whiteson, 2019): Double Actor-Critic Architecture for Learning Options — options 学习中与 value estimation 相关
- **SPiRL/SPIRAL** (Pertsch et al., 2020): Skill-prior RL with temporal abstraction — CoRL 接受的 robotics temporal abstraction 工作范例
- Robotics-specific temporal abstraction 部署工作——补充这些可强化 robotics relevance

注意：论文引用了 [12] Sharma et al. 2017，需确认是否已涵盖 FiGAR。

---

## External Review (Stanford Agentic Reviewer)

未启用。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~4.5 分钟）。发现 1 critical + 3 warning + 11 info：

**Critical**:
- **Page 36**: 近乎空白页（仅顶部 5 行文字，~10% 填充）。Appendix I 段落结束后直接分页，下一页才是 Table 3。应重排以消除空页。

**Warning**:
- **Pages 3-4**: 连续 2 页纯文本（Experimental Setup §3.1-3.8），无任何 display item，视觉疲劳风险。
- **Pages 9-10**: 连续 2 页纯文本（Discussion §5），无图/表/公式打断。
- **Page 45**: 末页内容约 55%，有较大空白。

**Info** (11 项，不逐列):
- Figure 1 流程图文字偏小（~正文 60-65%）
- Table 1 列间距偏紧
- Figure 2/3 同页略拥挤
- Figure 9 cosine similarity heatmap 在灰度打印下区分度降低
- 附录 Tables 4-28 密集排列但格式统一
- Algorithm 1 伪代码格式清晰
- 全文无 LaTeX 错误残留，无 [?] 未解析引用

---

## Overall Assessment

**评分: Weak Reject**
**置信度: 4/5**

本文是一篇实验设计严谨、数据透明度极高的 MBRL 诊断论文，成功识别了 CIVO 这一 failure mode 并提供了系统性的实验证据。然而，**投稿目标选择失误**是最根本的问题：

1. **两个独立的 desk-reject 条件**: 正文超页 ~2.5 页 + CoRL robotics relevance 不足。任一条件单独即可导致 desk rejection。

2. **历史重复**: 本文在 Round 1-3 以 CoRL 为目标时即因 venue fit 被三位 reviewer 一致标记为最强共识问题，Round 4 切换至 ICML 解决了该问题，Round 5-6 在 ICML 框架下评审趋向积极。**切回 CoRL 是一个战略性错误**——重新引入了已知的致命弱点，且超页问题叠加使局面更糟。

3. **方法论层面**: AUROC 缺乏 uncertainty quantification、因果声明过强、统计效力有限——这些问题可通过修改论文文本缓解（弱化措辞 + 报告 CI），不影响核心发现的有效性。

**建议**:
- **立即**: 放弃 CoRL 2026 投稿。在今天 deadline 前提交一篇有两个 desk-reject 条件的论文是浪费机会。
- **短期**: 将论文切回 ICML 2026（或 NeurIPS 2026）格式，压缩正文至 8 页，补充 AUROC bootstrap CI，弱化因果机制措辞。
- **中期**: 如果仍希望投 robotics venue，需补充 real-robot 实验或 sim-to-real 验证。

---

## Detailed Comments

### Section 1 (Introduction)
- Abstract 中 "increasingly deployed for robot control" 是 CoRL 的 framing hook，但后续所有实验均在 DMC 仿真中进行，缺乏 robotics deployment 的具体支撑。
- Contribution list 中 "preliminary diagnostic"（NVE detector）与 "failure mode identification" 概念重叠，分类可更正交。

### Section 2 (Related Work)
- 与 compounding model error (Janner et al., Lambert et al.) 的区分需要更锐利的形式化论证，而非仅靠经验观察。
- 缺少 robotics-specific temporal abstraction 工作的引用（FiGAR, SPiRL 等），削弱了 CoRL 的 positioning。

### Section 3 (Experimental Setup)
- 8 个子节（3.1-3.8）在约 1.5 页纯文本中展开，是超页的主要来源之一。建议仅保留 3.1-3.4 在正文（base architecture + factorial design + metrics），其余移至 Appendix。
- NVE 的数学定义分散在文字描述中，应给出完整公式。

### Section 4 (Results)
- F1-F7 的递进叙事逻辑清晰，但 seed-level 叙述（如 "seed 3 shows early collapse"）需标注为 anecdotal observation。
- Table 1 的 43 行信息密度极高但扫描性差，建议精简为 summary table。
- Table 2 prevention rates 基于极小样本，需补充 Fisher exact test。

### Section 5 (Discussion)
- ~1.5 页 Discussion 大量重复 Section 4 的 findings，是超页的另一主要来源。
- "Transferable diagnostic protocol" 声明需限定为 "within DreamerV3"。
- "CIVO is upstream of estimation error—a structural consequence of shared-feature imagination" 需更强的理论支撑。

### Section 6 (Conclusion + Limitations)
- Limitations section 诚实全面，覆盖了环境多样性、统计效力、架构泛化性。
- Broader Impact Statement 存在且合理，但 CoRL 2026 未要求此节——可作为压缩页数的候选。

### Appendix
- 31 页附录是论文的重要资产。Appendix I (Code Corrections) 的透明度值得赞赏但需补充汇总统计。
- Page 36 近乎空白页应修复。
- 建议将 Section 3.5-3.8 和 Discussion 的详细分析移入 Appendix 以解决超页问题。