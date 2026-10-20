---
round: 3
review_mode: continue
overall_score: weak reject
timestamp: 2026-05-24T07:19:49.260508+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 3

**论文**: "Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**目标 Venue**: CoRL 2026 Main Conference
**审稿日期**: 2026-05-24
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验充分性 | R2: Venue Fit + 贡献度 + 写作质量）
**轮次**: Round 3 继续审稿（修订评估）+ 交叉分享（1 轮收敛）
**上轮评分**: Round 1 Strong Reject (4/10)

---

## Summary

论文在 Round 1 (Strong Reject) 后进行了大幅修改：从 1 环境扩展到 5 环境（Walker Walk, Cheetah Run, PickCube-v1, StackCube-v1, PegInsertionSide-v1），关键配置 seeds 增至 4，引入 LOEO 交叉验证（AUROC=0.981），因果语言全面弱化为 "strongest predictor"，新增四级干预层级分析和在线 CIVO 检测器，切换至 CoRL 2026 PMLR 模板，添加 robotics framing 和 ManiSkill 实验。论文现在识别 CIVO 为 locomotion-specific（6/6 locomotion seeds 触发，0/5 manipulation configurations 触发），并提供了 discriminative validity（frozen-embedding 控制正确区分 CIVO 与环境特异性 transient）。

---

## Strengths

1. **Factorial design 系统且严谨**（2/2 reviewer 共识）：43 配置 × 4 seeds × 5 环境的设计空间覆盖广泛；primary/secondary comparison 标注清晰；2×2 factorial grid 完整
2. **LOEO 交叉验证显著增强统计可信度**：AUROC=0.953 (in-sample, n=29), 0.981 (LOEO, 3 folds) 在 RL 诊断类工作中是扎实的统计功效水平
3. **四级干预层级分析**（gradient/output/representation/architecture）：提供了系统性的 negative result，对社区有长期参考价值。Gradient magnitude ≠ causal importance 的发现（reward head 38-49% 但 SGS 无效）是有洞见的
4. **ManiSkill non-CIVO 结果增加 discriminative validity**：NVE 诊断能正确区分 dt-embedding-dependent CIVO 与环境特异性 transient（frozen controls 匹配 trained spikes），展示了方法论的特异性
5. **Dual-critic convergence (ρ > 0.999)**：关于 imagination-based training 中 Double Q pessimism 失效的 structural insight 有价值
6. **Limitations section 诚实全面**：主动承认 4-seed 局限、architecture 局限、locomotion-specificity，ManiSkill non-CIVO 如实报告
7. **Signed error 分析**：dt=2 underprediction (SE=-0.599) 排除 observation-level reward overprediction，将 CIVO 定位为 imagination-level prior drift，与 compounding error 清晰区分

---

## Weaknesses（按严重性排序）

### Critical（影响接收决定）

**W-C1. CoRL Venue Fit 仍有结构性 gap [R2 判定 STILL_OPEN，R1 部分同意]**
论文做了显著改进（ManiSkill 实验、robotics framing），但核心矛盾未解决：
- **ManiSkill 结果反向证明 CIVO 与 manipulation 无关**：所有 3 个 ManiSkill 环境均未出现 dt-embedding-dependent CIVO（Section 4.3: "CIVO is locomotion-specific in DreamerV3"），frozen controls 表现相当甚至更高。论文的核心发现恰恰在 robotics-relevant manipulation 任务中不成立。
- **Robotics framing 仍是 "bookend" 式的**：robotics motivation 集中在 Introduction 前两句和 Discussion 一个段落，方法和结果部分（Section 3-4，约 4 页）完全是通用 RL 分析。
- **CoRL CFP 要求 "focus on core robotics problems"**：CIVO 是一个通用 RL/world-model 问题，并非 robotics-specific。论文自己承认 "does not test...real-robot deployments"（conclusion.tex:7）。
- **Desk reject 风险已降低但未消除**：ManiSkill 实验使论文不至于完全没有 robot-relevant 实验，但严格的 AC 可能认为 negative ManiSkill 结果 + DMC-based 核心实验不满足 scope。

**W-C2. 贡献模式对 CoRL deployment-oriented 社区偏弱 [R2 判定 STILL_OPEN]**
论文从 "纯诊断" 升级为 "诊断 + partial mitigation + detection"，但：
- **核心结论仍是 negative**：Table 2 总结 "No level reliably eliminates CIVO across environments"
- **最有效 "solution" 是不使用该功能**：embedding removed = 100% prevention = 不做 temporal abstraction via dt-conditioning
- **Partial mitigations 效果有限**：frozen embedding 5/7 prevention 但 eval 仍差（015b: 22% baseline）；wide dual-critic 3/4 Walker 但 Cheetah 0/1
- **Practitioner guidelines 的核心建议**："不要用 trained dt-embedding" + "用 NVE 监控"——对需要 temporal abstraction 的应用帮助有限

### Warning（影响评分但不一票否决）

**W-W1. 105K vs 505K 训练步数不对等未显式讨论 [2/2 reviewer 共识 STILL_OPEN]**
论文在 105K 对治疗组和基线进行 matched-timestep 比较，但：
- 未在正文讨论为什么 105K 足够确认 collapse（尤其当 1/4 seeds self-correct 时）
- exp_045 延长到 300K 的数据未在正文呈现
- 如果 self-correction 在更长时间窗口更普遍，"all variable-rate configurations degrade" (F1) 可能过强

**W-W2. TAWM/MPC 对比仍无实证 [2/2 reviewer 共识 STILL_OPEN]**
Abstract 和 Conclusion 称 "feedback architecture as the structural factor"，但从未在 TD-MPC2/TAWM 上运行实验。这一核心论断只有 architectural reasoning 支撑。应弱化为 "hypothesized structural factor" 或增加至少一个 MPC baseline 实验。

**W-W3. Online CIVO Detector 评估样本量不足 [2/2 reviewer 共识，Round 3 新发现]**
n=14 runs 中仅 5 个正例。TPR=5/5 的 95% CI 下界 (Clopper-Pearson) 仅 47.8%。FPR=2/9 (22%) 在部署场景中误报率过高。论文将 detector 作为四项 contribution 之一，但样本量不足以支撑独立贡献地位。

**W-W4. Becker-Ehmck et al. (2023) 仍未引用 [R2 指出，PARTIALLY RESOLVED]**
三篇遗漏文献已引用（Park 2021, Wang 2024, Colas 2018），但 Becker-Ehmck et al. (2023) "Multi-timestep models for MBRL" 仍缺失，与论文主题直接相关。

### Minor

**W-M1. Abstract 统计数据过密**：~150 词包含 6+ 数字指标（14-19%, 26/29, AUROC=0.953, 2.78×, ρ>0.999, 100% sensitivity），建议精简至 2-3 个关键数字。

**W-M2. Dual-critic convergence 叙事过于简化 [2/2 reviewer 共识]**：ρ > 0.999 是 asymptotic 结果；与 wide dual-critic 3/4 prevention 成功存在张力；主文 "pessimism ineffective" 需 nuance——min operation 可能通过非 pessimism 机制发挥作用。

**W-M3. ManiSkill 和 Cheetah Run baseline eval 值缺失**：Table 1 中这些环境缺少 vanilla DreamerV3 baseline 参照值，读者无法判断相对性能。

**W-M4. Abstract 中 "isolate" 携带因果含义**，与全文 "strongest predictor" 措辞不一致。

---

## Reviewer Consensus

| 问题 | R1 | R2 | 共识度 |
|------|----|----|--------|
| R1-N1 统计检验力 | RESOLVED | RESOLVED | **2/2 一致** |
| R1-N4 单环境 | RESOLVED | RESOLVED | **2/2 一致** |
| R1-W1 Factorial 混淆 | RESOLVED | RESOLVED | **2/2 一致** |
| R1-W2 步数不对等 | STILL_OPEN | STILL_OPEN | **2/2 一致** |
| R1-W3 Pathway B | RESOLVED | RESOLVED | **2/2 一致** |
| R2-W1 TAWM 无实证 | STILL_OPEN | STILL_OPEN | **2/2 一致** |
| R1-W4 Signed error | RESOLVED | RESOLVED | **2/2 一致** |
| R2-W3 CIVO 区分 | — | RESOLVED | R2 独立确认 |
| R3-W2 Abstract | — | RESOLVED | R2 独立确认 |
| R2-W4 Bib | — | PARTIALLY | Becker-Ehmck 仍缺 |
| R1-N3 Venue fit | Relevance 4/5 | STILL_OPEN (5/10) | **分歧** |
| R2-N3 Actionable | — | STILL_OPEN (6/10) | R2 独立判定 |
| N-new-1 Detector 样本量 | WARNING | AGREE | **2/2 一致** |
| N-new-3 Dual-critic | MINOR | AGREE | **2/2 一致** |

---

## Reviewer Divergence

**1. CoRL Relevance（R1: 4/5 vs R2: 2.5/5）**
- R1：temporal abstraction 是 CoRL 核心话题，world-model RL 直接关联 robot control
- R2：CIVO 恰恰在 robotics-relevant manipulation 中不出现，核心发现是 locomotion-specific，CoRL 社区更关心 contact-rich manipulation
- **Director 判断**：R2 的论点更有说服力。ManiSkill negative results 是论文的 honest science，但客观上削弱了对 CoRL 的 relevance。CIVO 仅在 DMC locomotion 中复现，而 DMC locomotion 不是 CoRL 的核心关注点。综合评估 relevance 约 3/5。

**2. Significance（R1: 3/5 vs R2: 2/5）**
- R1：四级干预层级分析对社区有长期价值
- R2：negative result + no reliable fix 的贡献模式在 deployment-oriented 社区价值有限；核心 takeaway 是 "不要用"
- **Director 判断**：部分同意双方。四级干预分析的系统性是 genuine contribution，但论文的 actionable 输出确实有限。综合约 2.5/5。

**3. Originality（R1: 4/5 vs R2: 3/5）**
- R1：首个系统诊断 DreamerV3 变速想象失败的工作，CIVO 现象识别新颖
- R2：方法论（factorial ablation）是标准做法，negative result 的原创性 credit 存在争议
- **Director 判断**：CIVO 现象的识别和因果分离确实新颖（特别是 gradient magnitude ≠ causal importance 的发现），但方法论框架本身不新。综合约 3.5/5。

---

## Questions for Authors

1. 如果 treatment 训练延长到 300K-500K 步，self-correction 是否会更普遍？exp_045 的数据是否可以报告？
2. "Feedback architecture as the structural factor" 能否弱化为 "hypothesized structural factor"，或者是否有计划在 TD-MPC2 上验证？
3. CIVO 在 locomotion 出现但 manipulation 不出现的 reward density 假说（Discussion "a possible mediator is reward density"），是否有更直接的证据？
4. Online detector 的 FPR=22% 在实际部署中是否可接受？是否有降低误报率的方案？
5. Wide dual-critic 3/4 CIVO prevention 的成功机制是什么？如果 ρ > 0.999 使 pessimism 无效，min operation 通过什么机制起作用？

---

## Missing References

- **Becker-Ehmck et al. (2023)** "Multi-timestep models for Model-based RL" — 直接研究 multi-timestep world model，与论文主题高度相关，在 Round 1 已提出但仍未引用

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

视觉审查已完成（5 warnings, 0 critical, 12 info）。

**主要发现**：
1. **[warning] 前 4 页无 display item**：连续 4 页纯文本，第一个视觉锚点（Table 1 + Figure 1）直到第 5 页才出现。对诊断/实证型论文，审稿人第一印象不利。建议将架构图或核心发现概览图提前到第 1-2 页。
2. **[warning] 正文 display item 密度偏低**：8 页正文仅 4 个 display items（Table 1-2, Figure 1-2），实证型论文通常期望 5-8 个。
3. **[warning] CIVO mechanism diagram (Figure 6) 被放在 Appendix**：这是论文最重要的概念可视化，审稿人在正文中看不到方法的直觉图示。强烈建议移入正文。
4. **[warning] Appendix 页面空白**：Page 26 和 Page 33 有大面积空白。
5. **[info] 图表质量良好**：Figure 1/2 使用彩色线条和清晰标注；Table 1-2 使用 booktabs 风格；ROC 曲线标注 AUC 和阈值点。

---

## Overall Assessment

**评分: Weak Reject (5/10)**
**置信度: High (4/5)**

**与 Round 1 (Strong Reject, 4/10) 的变化**：论文在方法论和实验充分性方面取得了显著进步：

| 维度 | Round 1 | Round 3 | 变化 |
|------|---------|---------|------|
| 统计检验力 | Critical (2-3 seeds) | Resolved (4 seeds, LOEO) | ▲▲ |
| 环境覆盖 | Critical (1 env) | Resolved (5 envs) | ▲▲ |
| NVE 验证 | Critical (post-hoc) | Resolved (LOEO, AUROC=0.981) | ▲▲ |
| 模板合规 | Critical (desk reject) | Resolved (PMLR) | ▲▲ |
| Venue fit | Critical | Still open but improved | ▲ |
| Actionable 贡献 | Warning | Still open but improved | ▲ |
| CIVO 区分 | Warning | Resolved | ▲▲ |

**Round 1 的 4 个 critical issues 中 3 个已 resolved**（统计检验力、单环境、模板），第 4 个（venue fit）有改善但结构性矛盾未解。

**核心矛盾**（影响从 Weak Reject 上升到 Borderline 的障碍）：
1. **Venue fit**：论文的核心发现（CIVO）仅在 DMC locomotion 中成立，在 robotics-relevant manipulation 中不出现。CoRL 要求 "focus on core robotics problems"，当前论文更适合 ICML/NeurIPS 的 RL/world-model track。
2. **贡献模式**：diagnostic negative result + partial mitigation + detection 的组合在 ML theory venue 可以接受，但对 CoRL 的 deployment-oriented 社区偏弱。Practitioner 的最佳策略仍然是 "不要用 trained dt-embedding"。

**如果提交到 ICML/NeurIPS**：方法论评分会提升至 Borderline Accept (6/10)——factorial design 严谨、LOEO 验证有力、四级干预分析有系统性贡献、CIVO 与 compounding error 的区分清晰。Venue fit 和 actionable 贡献的约束消失。

**综合维度评分**（Director 综合两位 Reviewer）：

| 维度 | 评分 | 理由 |
|------|------|------|
| Originality | 3.5/5 | CIVO 现象新颖，gradient ≠ causal importance 有洞见，方法论框架标准 |
| Quality | 3/5 | Factorial design 严谨，LOEO 有力，但 CIVO 仅 2/5 环境复现，部分配置样本量小 |
| Clarity | 4/5 | 结构清晰，F1-F7 叙事好，33 页 appendix 详尽 |
| Significance | 2.5/5 | 四级干预有系统贡献，但 locomotion-specific + no reliable fix 限制 impact |
| Relevance | 3/5 | Temporal abstraction 与 CoRL 相关，但核心发现在 manipulation 不成立 |
| Limitations | 4/5 | 诚实全面 |

---

## Detailed Comments（逐节）

### Abstract
- 约 150 词，长度合理。Robotics motivation 到位（首句）。
- 统计数据过密（6+ 数字指标），建议精简至 2-3 个关键数字
- "isolate" 一词与全文 "strongest predictor" 不一致

### Introduction (Section 1)
- Robotics framing 明显改善（DayDreamer, TD-MPC2 引用，temporal abstraction 的 robotics 需求）
- Contribution 列表 4 项与正文一致
- 最后一段 robotics relevance 论述合理但稍显牵强

### Related Work (Section 2)
- CIVO vs compounding error 区分清晰（控制实验 + signed error）
- Park 2021, Wang 2024, Colas 2018 已引用
- Becker-Ehmck 2023 仍缺

### Experimental Setup (Section 3)
- Factorial design 展示专业，四因素清晰
- Primary vs secondary comparison 标注到位
- SGS, TCN, RAVE, Dual-critic 方法描述完整
- 缺少对 105K vs 505K 步数选择的 rationale 讨论

### Results (Section 4)
- F1-F7 因果链叙事清晰
- Table 1 信息密度高，灰色标记 CIVO-positive 有效
- ManiSkill negative results 诚实呈现
- 缺少 Cheetah/ManiSkill baseline eval 参照值
- Online detector 评估样本量不足（n=14, 5 正例）
- Dual-critic ρ > 0.999 结论需 nuance

### Discussion (Section 5)
- CIVO mechanism 段落简洁准确
- Practitioner guidelines 可操作（NVE ≥ 1.5×, embedding freezing）
- "Implications for robot learning" 提供了 reward density 假说
- "structural factor" 措辞过强（无 MPC 实验验证）

### Conclusion (Section 6)
- Limitations paragraph 诚实（4 seeds, architecture, real-robot）
- 措辞恰当，未过度泛化

### Appendix
- 33 页，极其详尽（完整 42 配置结果、NVE sensitivity、LOEO、gradient decomposition、entropy dynamics、dual-critic analysis）
- Figure 6 (CIVO mechanism diagram) 应移入正文
- 部分页面空白可优化