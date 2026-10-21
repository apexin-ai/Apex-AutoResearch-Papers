---
round: 1
overall_score: strong reject
timestamp: 2026-05-15T12:43:17.705786+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 审稿报告 — Round 1

**论文**: "Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**目标 Venue**: CoRL 2026 Main Conference
**审稿日期**: 2026-05-15
**Reviewer 编排**: 3 人（R1: 方法严谨性 & 实验设计 | R2: 新颖性 & 贡献度 & Venue Fit | R3: 格式合规 & 写作质量）
**轮次**: Round 1 初审 + 交叉分享（1 轮收敛）

---

## Summary

本文通过 factorial ablation 分析 DreamerV3 中 variable-rate imagination 的失败原因。在 Walker Walk (DMC) 上测试 9 组配置（2-3 seeds each），识别出 trained dt-embedding 导致 RSSM reward head 产生 2.78× 跨时间尺度预测偏差，critic 通过 imagination bootstrapping 将其内化为系统性高估——称为 conditioning-induced value overestimation (CIVO)。论文进一步发现同一 trigger 产生三种随机下游结果（full collapse / self-correction / oscillatory degradation），且限制 imagination 到 dt=1 不能完全防止崩溃（存在 non-CIVO Pathway B）。与 TAWM (MPC-based) 的对比将 feedback architecture 定位为关键结构差异。

---

## Strengths

1. **清晰的问题定义和切入点**：将 "为什么 dt-conditioning 在 MPC 中成功但在 imagination-based AC 中失败" 作为核心问题，切入角度明确且有实际意义（3/3 reviewer 认可）
2. **结构化的 factorial 设计**：trained vs untrained vs removed embedding 的三向对比是方法论亮点，核心对照 008d vs 008f 在控制变量上是干净的（R3 在交叉回应中澄清）
3. **CIVO 机制描述细致**：四阶段反馈回路描述清晰，三种 post-CIVO 结果的刻画有信息量
4. **Multiple pathways 发现 (F6)**：Pathway A (value-driven) 和 Pathway B (eval-driven) 的识别是 genuine discovery，表明问题比单一 value overestimation 更深层（3/3 认可为论文最有价值的 insight）
5. **写作质量高**：F1-F6 因果链式叙述清晰，Figure/Table 信息密度高，术语定义到位（Clarity 获三位 reviewer 最高分 4/5 或 7/10）
6. **诚实的 Limitations**：承认单环境和单架构局限，F6 的 partial falsification 展示良好科学态度

---

## Weaknesses（按严重性排序）

### Critical（影响接收决定）

**W-C1. CoRL Venue Fit 严重不足 [3/3 reviewer 共识，最强共识]**
全文仅在 DMC Walker Walk（proprioceptive observations）上做实验，无任何 robotics benchmark（RoboSuite/ManiSkill/IsaacGym）、无 real-robot 实验、无 robotics application 讨论。Introduction 直接从 TAWM 的 RL 结果出发，完全没有 robotics motivation。CoRL CFP 明确要求 "Submissions should focus on a core robotics problem"——当前论文不满足这一硬约束，存在 desk reject 风险。

**W-C2. 统计检验力严重不足 [3/3 reviewer 共识]**
核心因果声明 "trained dt-embedding is the causal factor" 依赖 n=2 per group 的 factorial 比较。"4/4 separating power" 在随机零假设下 P=1/16≈6.25%，未达 p<0.05 且未做多重比较修正。论文引用 Agarwal et al. (2021) 辩护 per-seed reporting，但该文的核心论点恰恰是需要更多 seeds + IQM 等稳健统计量。语言中频繁使用 "causal factor"、"triggers"、"necessary and sufficient" 等因果措辞，与 n=2 的证据强度严重不匹配。

**W-C3. 单环境（Walker Walk）局限使因果声明不可泛化 [3/3 reviewer 共识]**
Walker Walk 是 DMC 中最简单的 locomotion 任务之一（24-dim obs, 6-dim action, dense reward）。CIVO 的 2.78× reward gap 可能高度依赖：(a) 低维动力学的高 RSSM fidelity（baseline reward MAE 仅 0.0102）；(b) dense reward 下 critic 获得频繁真实信号；(c) proprioceptive observations 无 representation bottleneck。在 sparse reward、高维视觉、contact-rich dynamics 环境下，CIVO 可能表现完全不同或不出现。Section 6.6 的 "structural incompatibility" 声明在没有多环境验证下是过度泛化。

**W-C4. NVE 阈值 1.5× 为 post-hoc 选择 [3/3 reviewer 共识]**
1.5× 阈值未说明选择依据（pre-registered vs data-driven）。数据显示 [1.2, 2.0] 范围内任何阈值均可达到类似分类效果，强烈暗示 post-hoc 选择。"88.9% accuracy" 是在训练集上的准确率，无 held-out 验证、cross-validation 或 sensitivity analysis。将 post-hoc 指标阈值包装为 "separating power" 可能误导后续研究者。

**W-C5. 未使用 CoRL 2026 官方 PMLR 模板 [2/3 reviewer 列为 critical]**
论文使用 `\documentclass[10pt,letterpaper,twocolumn]{article}` + 自定义 geometry（0.75in margins），完全不符合 CoRL 2026 要求的 PMLR 模板（`\usepackage[final]{corl_2026}`）。这构成 desk reject 的独立理由。换模板后正文极可能超过 8 页限制。

### Warning（影响评分但不一票否决）

**W-W1. 纯诊断负面结果缺乏 actionable solution [2/3 reviewer 共识，1/3 partial disagreement]**
论文 Section 6.6 提出三个 future directions（hierarchical abstraction、embedding regularization、transformer extension），全部 "leave to future work"。Gradient stopping 作为 mitigation 仅需一行代码改动却未测试。R3 部分反驳：论文有 NVE 框架、CIVO 机制分析、MPC vs imagination 架构对比等诊断贡献，类似 Henderson et al. (2018) 的模式。但三位 reviewer 均同意：对 CoRL 这个偏重实际 solution 的 venue，纯诊断贡献度偏低。

**W-W2. 与 TAWM 的对比缺乏实证 [3/3 reviewer 共识]**
Section 6.3 关于 MPC 免疫性的解释完全基于 architectural reasoning，未实际运行 TAWM/TD-MPC2 验证。TD-MPC2 与 DreamerV3 的多重差异（连续 vs 离散 latent、training objective 等）可能 confound 对比。

**W-W3. 105K vs 505K 训练步数不对等 [3/3 reviewer 共识]**
Baseline 运行 505K 展示完整收敛，treatment 仅 105K。Self-correcting seed 009b（eval 267.9@105K = baseline 的 29%）可能只是 slower collapse 而非真正的 self-correction。Oscillatory seed 009e 的长期命运未知。

**W-W4. Pathway B 解释不充分 [2/3 AGREE, 1/3 partial REBUT]**
008e_v3 seed 2 的 non-CIVO collapse 仅有 1 个 seed 的证据。论文用 baseline seed 2 (009a) 的稳定性排除 seed fragility（R2 认为此 control 有一定价值），但未排除 subsampling data augmentation 等引入的普通 training instability。Pathway B 的特征（entropy increase, eval-driven）与已知 plasticity loss / capacity collapse 的区分不够清晰。

**W-W5. RSSM fidelity 仅报告 MAE，未验证 overprediction 方向性 [3/3 AGREE]**
Table 4 的 reward MAE 不区分 over- vs under-prediction。CIVO 机制假设 reward head "systematically overpredicts rewards at dt=2"，但 MAE=0.1579 可能是双向误差。需 signed error 验证方向性。

**W-W6. CIVO 与已知 value overestimation 的区分不够清晰 [R2 提出，R1/R3 partial REBUT]**
R2 认为 CIVO 可能只是 compounding model error 的实例化。R1 和 R3 均 partial REBUT：trained vs untrained embedding 对比（008a/008c nve<0.6× vs 008d nve=4.12×）提供了超越 generic compounding error 的机制特异性——如果仅是 compounding error，untrained embedding + dt=2 也应出现 overestimation。但论文应更系统地阐述这一区分。

**W-W7. Factorial design 部分对比存在混淆 [R1 提出，R3 partial REBUT]**
008d vs 008a/008c 的比较同时改变了 embedding、subsampling、horizon 三个因素。R3 澄清：核心对照 008d vs 008f 是干净的（仅 embedding 不同），混淆仅存在于 secondary comparisons。但论文未清晰区分 primary vs secondary comparisons，容易导致误读。

**W-W8. Related Work 遗漏 + Bibliography 冗余 [3/3 reviewer 共识]**
Becker-Ehmck et al. (2023)、Park et al. (2021)、Wang & Beltrame (2024)、Colas et al. (2018) 均在 .bib 中但未在正文引用，且与论文主题高度相关。77 条 bib entries 中 48 条 orphan，多个占位符 author 字段（splates2025 等）。

---

## Reviewer Consensus

| 问题 | R1 | R2 | R3 | 共识度 |
|------|----|----|-----|--------|
| CoRL venue fit 不足 | N3 critical | N1 critical | N2 critical | **3/3 一致** |
| 统计检验力不足 | N1 critical | 交叉 AGREE | 交叉 AGREE | **3/3 一致** |
| 单环境不可泛化 | N4 critical | N2 critical | 交叉 AGREE | **3/3 一致** |
| NVE 阈值 post-hoc | N2 critical | W2 warning | 交叉 AGREE | **3/3 一致** |
| 模板不合规 | W5 warning | 小问题 | N1 critical | 3/3 提及 |
| 缺乏 actionable solution | 交叉 nuance | N3 critical | 交叉 partial REBUT | 2/3 |

---

## Reviewer Divergence

**1. Factorial design 混淆变量（R1-W1）**
- R1/R2: AGREE——缺少干净的 trained vs untrained 对比
- R3: REBUT——核心对照 008d vs 008f 是干净的（仅 embedding 不同），混淆仅在 secondary comparisons
- **Director 判断**：R3 的 REBUT 有理据（Table 1 确认 008d/008f 仅 embedding 不同），但论文确实缺少 untrained+SubON+H=8 的配置来完成完整 factorial grid

**2. CIVO 新颖性（R2-W3）**
- R2: CIVO 可能只是 compounding model error 的实例化
- R1/R3: partial REBUT——trained vs untrained 对比提供了机制特异性，untrained embedding 不触发 overestimation 说明不是 generic compounding error
- **Director 判断**：R1/R3 的 REBUT 在技术上合理——CIVO 的 specific trigger（learned co-adaptation between embedding and reward head）超越了 generic compounding error 的解释。但这一区分在论文中应更显式地阐述

**3. Pathway B 解释（R1-W3）**
- R1/R3: Pathway B 可能是普通 training instability
- R2: partial REBUT——baseline seed 2 (009a) 的稳定性提供了部分因果证据
- **Director 判断**：baseline control 有一定说服力，但仅 1 个 seed 的证据确实不足以做 "qualitatively distinct pathway" 的强声明

---

## Questions for Authors

1. 是否在其他 DMC 任务上做过任何初步验证？即使不完整的数据也能大幅增强 CIVO 发现的可信度。
2. Gradient stopping（阻止 dt-embedding 梯度流向 reward head）作为 mitigation 只需一行代码——为什么未测试？
3. Table 4 的 reward MAE 能否补充 signed error（mean error），验证 dt=2 是否为系统性正向偏差？
4. TAWM 原文中 Walker Walk 的具体数据是什么？能否直接引用来支撑 MPC vs imagination 的对比论点？
5. NVE 阈值 1.5× 在 1.3× 或 2.0× 下的分类结果如何变化？是否做过 sensitivity analysis？
6. 008e_v3 seed 2 (Pathway B) 的 actor action distribution 在崩溃前后是否有分析？这对区分 exploration-driven degradation 和 representation corruption 很关键。

---

## Missing References

以下工作存在于 .bib 中但未在正文引用，且与论文主题高度相关：
- **Becker-Ehmck et al. (2023)** "Multi-timestep models for Model-based RL" — 直接研究 multi-timestep world model 在 MBRL 中的效果
- **Park et al. (2021)** "Time Discretization-Invariant Safe Action Repetition" — time-discretization 对 RL 的影响
- **Wang & Beltrame (2024)** "Reinforcement Learning with Elastic Time Steps" — elastic time steps in RL
- **Colas et al. (2018)** — seed 数量对 deep RL 结论可靠性的影响，与 N1 直接相关

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目中未找到 `external_review.paperreview_ai.enabled: true`）。

---

## Overall Assessment

**评分: Strong Reject (4/10)**
**置信度: High (4/5)**

三位 Reviewer 评分完全一致（4/4/4），在以下核心问题上形成强共识：

1. **CoRL venue fit**（3/3 critical）：论文不满足 CoRL 对 robot learning 的 scope 要求，存在 desk reject 风险
2. **统计基础**（3/3 一致）：2-3 seeds 无法支撑因果声明，NVE 阈值 post-hoc
3. **单环境泛化性**（3/3 一致）：Walker Walk 一个环境的诊断无法支撑 "structural incompatibility" 级别的结论
4. **格式合规**（3/3 提及）：未使用 PMLR 模板，独立的 desk reject 理由

论文的 factorial 设计思路和 CIVO 机制描述有价值，但在当前形态下存在多个根本性缺陷。

**建议**：
1. **Venue 选择**：论文更适合 ICML/NeurIPS/ICLR 的 RL track 或 RLC，而非 CoRL。如坚持投 CoRL，需大幅增加 robotics motivation 和 robot-relevant 实验。
2. **实验扩展**：至少增加 2-3 个不同复杂度的环境（如 Cheetah Run, Humanoid Walk, 或 manipulation task），每配置 5+ seeds。
3. **方法论修正**：(a) 将因果语言弱化为 "strongly associated" 或 "candidate mechanism"；(b) 对 NVE 阈值做 sensitivity analysis 或跨环境验证；(c) 补充 reward signed error 验证 CIVO 方向性假设。
4. **增加 actionable 贡献**：实现并测试至少一种 mitigation（如 gradient stopping dt-embedding 对 reward head 的梯度）。
5. **格式修正**：切换到目标 venue 官方模板，清理 bibliography。

---

## Detailed Comments（逐节）

### Abstract
- 过长且过于技术化（~180 词含大量具体数字）
- 缺乏 robotics motivation（对 CoRL 是硬伤）
- "88.9% accuracy" 放在 abstract 有误导性（post-hoc in-sample accuracy）

### Introduction (Section 1)
- 问题定义清晰，从 TAWM 的 MPC 成功切入有效
- 但完全没有 robotics framing——需要首段建立 temporal abstraction 对 robot learning 的重要性
- "causal factor" 措辞过强

### Related Work (Section 2)
- 覆盖面合理但有遗漏（Becker-Ehmck 2023, Park 2021, Wang 2024, Colas 2018 在 bib 中未引用）
- DreamerV4 讨论移至 Analysis 而非 Related Work 是合理选择
- CIVO 与已知 value overestimation 的区分需更清晰阐述

### Methodology (Section 3)
- Factorial design 结构良好，Table 1 信息清晰
- 核心对照 008d vs 008f 干净（R3 交叉确认），但 secondary comparisons 有混淆
- "2--3 seeds" 应直接讨论统计效力局限而非仅在 Limitations 中提及
- NVE 阈值选取过程需透明化

### Results (Section 5)
- F1-F6 的因果链组织出色
- Table 2 和 per-seed trajectory 报告方式专业
- 但 exp_006/007/005 的 NVE 标注为 "---" 未解释原因
- "self-correction" 的标签对 009b（eval 267.9 = baseline 29%）可能过于乐观

### Analysis & Discussion (Section 6)
- CIVO 四阶段机制描述（6.1）清晰有说服力
- Seed divergence 讨论（6.2）引用 Lyle et al. 的 capacity loss 假说有价值
- MPC immune 分析（6.3）合理但缺乏实证
- dt-Embedding Dilemma（6.4）包装过度——在单环境 + 低 seeds 下，"dilemma" 可能只是 artifact
- Multiple Pathways（6.5）是论文最有价值的 section，但 Pathway B 仅 1 seed 证据

### Conclusion (Section 7)
- Limitations paragraph 内容实质到位，但形式上应提升为独立 section/subsection
- Future directions 过于 speculative，缺乏初步验证
- Baseline seed 0 "in progress" 不应出现在提交版本中
