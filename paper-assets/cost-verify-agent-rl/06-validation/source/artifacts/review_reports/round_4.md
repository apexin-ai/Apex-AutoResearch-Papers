---
round: 4
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-24T01:59:08.133816+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Sign Misattribution in Step-Independent Agent RL

**Venue**: EMNLP 2026 (ACL Rolling Review)
**Round**: 4 (Fresh Review)
**Reviewers**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 完整性 + 写作格式)

---

## Summary

本文诊断了多轮 Agent RL 中 step-independent windowing 训练范式的信用分配病理，将其分解为两个机制：策略信息损失（M1，截断上下文导致恒定性能天花板）和优势符号错误归因（M2，梯度方向反映 episode 结局而非局部动作质量）。通过 2×2 factorial 实验分离两个机制、闭式理论界（Proposition 2）量化错误梯度比例、11-seed 系统评估验证 episode-level GRPO 修复效果。论文写作质量高、诊断框架清晰，但在实验完整性（Cell C 缺失、单一主环境）、理论-实验衔接、和修复方案实用价值（36% 种子泛化率）方面存在显著不足。

---

## Strengths

**S1. 重要且及时的问题识别。** [R1-S1, R2 同意] Step-independent windowing 是 RAGEN 等主流框架的默认配置，被广泛无批判地采用。论文首次系统诊断了这一默认选择为何会导致训练崩溃。Appendix A.3 对"为何社区默认采用 step-independent"的六点分析尤其有洞察力。

**S2. 清晰的双机制分解框架与 factorial 设计。** [R1-S2, R2-S1] 将信用分配失败拆解为 M1（constant ceiling，推理层）和 M2（cumulative degradation，训练层）两个正交维度，并通过 2×2 factorial 设计分离验证（A→B 隔离 M2，B→D 隔离 M1），在 agent RL 文献中具有方法论示范价值。

**S3. 直接符号测量提供可操作的诊断指标。** [R1-S3, R2-S2] Section 4.4 引入的三层验证（sign-episode correlation 100%、credit agreement 52%、P(correct|update) ≤19.1%）具有可复用性，可应用于评估其他 credit assignment 方法。Proposition 2 的闭式上界直观且可验证。

**S4. 诚实、系统的 11-seed 评估。** [R1-S4, R2-S3] 完整报告了 73% 避免崩溃但仅 36% 实现显著 OOD 泛化。Table 2 分类明确（Collapsed/Stagnant/Generalized），附 Wilson 95% CI 和 Fisher exact p 值。Appendix F 的 step-5 统一评估降低了 checkpoint 选择偏差。这种透明度在当前 agent RL 文献中罕见。

**S5. 适当的贡献定位。** [R2-S4, R1 同意] 明确定位为"诊断"而非算法创新，Contributions 仅两项，与实际工作匹配，避免了 overclaim。

**S6. 写作质量与同期工作覆盖。** [R1-S5, R2-S6] 论文结构紧凑、论证精确，核心 claim 均有明确引用支撑。Related Work 覆盖了 10+ 同期工作（IRC, MC-GRPO, GAGPO, SWEET-RL, HCAPO, GiGPO, Turn-PPO 等），区分清晰。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W-Critical-1. Cell C 缺失使 factorial 设计不完整，削弱 M2 的独立验证。** [R1-W1 Critical; R2 交叉回应完全同意，承认自己初审遗漏]
- 2×2 factorial 中 Cell C（full context + step-level advantage，仅激活 M2）因 NaN 不稳定缺失（6 组超参均失败，Appendix D）。M2 效果仅能通过 A→B 差异间接推断。
- Discussion 中承认 Cell C 的 NaN 暗示非加性交互——这直接削弱了 factorial 分解的"正交可分"假设，而 factorial 设计是全文方法论核心。
- **两位 Reviewer 共识**：Discussion 中的讨论不足以替代实际的 Cell C 实验。若确实无法实现，应在正文明确降级 factorial claim 的强度。

**W-Major-1. Table 1 报告标准不一致，跨条件对比失去可比性。** [R1-W2 Major; R2 AGREE]
- Cell A 报告 best seed (2 seeds)，Cell B 报告 best checkpoint at step 5 (2 seeds)，Cell D 报告 mean of 2 seeds，Dense reward 和 REINFORCE++ 仅 1 seed。三种标准混用使跨 cell 数值对比失去严谨性。
- Caption 中已标注不同标准（Round 3 修复），但根本问题是数据本身应统一报告标准，而非标注不同标准。

**W-Major-2. 理论分析（binary reward）与实验设置（ternary reward）的 gap 缺乏形式化桥接。** [R1-W3 Major; R2-W4 AGREE]
- Proposition 1/2 在 binary reward ($R \in \{0, r_+\}$) 下推导，全部实验使用含 $r_- = -0.1$ penalty 的 ternary reward。理论预测 ≤19.1% vs. 实测 52%，gap 仅有定性桥接（"penalty introduces variance"），缺乏 ternary reward 下的形式化上界。
- Appendix A.2 的解释定性正确（penalty 打破 sign-episode 完美相关），但论文以理论为核心卖点，定量不匹配需要更严谨的处理。

**W-Major-3. 单一主实验环境限制诊断的普遍性声称。** [R2-W1/N1 Major→Critical; R1 同意方向但降级为 Minor-Major]
- 完整 factorial + 11-seed 评估仅在 ALFWorld 完成。ScienceWorld 仅验证 Cell A 崩溃（Section 4.6），未报告 Cell D（fix 的跨环境验证缺失）。8B 为 single-seed。
- **分歧记录**：R1 认为理论论证不依赖环境（仅依赖 windowing 结构），severity 应降级；R2 认为 "fundamental pathology" 的 claim 需多环境支撑。
- **共识方向**：实验覆盖不足是事实。至少需补充 ScienceWorld Cell D 的 single-seed 结果。

**W-Major-4. 36% 种子成功率无原因分析，诊断→修复叙事断裂。** [R2-W2/N2 Major→Critical; R1 完全同意方向但保持 Major]
- Episode-level GRPO 仅 36% 种子泛化，实践者平均需 ~3 次训练才获一次成功。论文完全没有提供成功/失败种子差异的分析线索或早期检测指标。
- Appendix E 的 response length 分析显示 collapsed seeds 有 length inflation，但这是果（collapse 导致 length inflation）而非因。
- **分歧记录**：R2 认为应为 Critical；R1 认为属诊断论文的自然边界（Major）。

### Should-Fix（影响评分但不一票否决）

**W-Warning-1. 缺乏与同期方法的直接实验对比。** [R1-W6 Warning; R2-W3 Major; R1 交叉回应部分反驳]
- HCAPO (91.4%), GiGPO (90.2%) 等仅在 Discussion 通过引用间接对比，无直接实验。论文以"7B vs. 1.7B 不可比"为由回避。
- **分歧记录**：R1 认为 factorial 分解是独特方法论贡献，severity 应为 Minor-Major；R2 认为增量贡献不清晰。
- **共识**：诊断论文不要求 SOTA，但应更具体展示 M1/M2 框架对选择不同修复方法（HCAPO vs. Turn-PPO vs. GiGPO）的实践指导价值。

**W-Warning-2. REINFORCE++ 仅训练 15 步，不构成公平对比。** [R1-W5 Warning; R2 AGREE]
- REINFORCE++ 在 15 步内匹配 SFT baseline 无提升，论文承认可能不足以收敛，但仍列入 Table 1 和 Figure 6a 作为对比，且无 OOD 评估。

**W-Warning-3. Eq. 6 中 magnitude ratio ($|\hat{A}_{correct}|/|\hat{A}_{wrong}| \approx 1.32$) 仅基于单个训练快照测量。** [R1-W7 Warning; R2 AGREE]
- Cumulative divergence 论证依赖 correct/wrong-sign 梯度幅度可比假设。仅一个快照不足。需至少补充 3-5 个训练阶段 × 2-3 seeds 的测量。

**W-Warning-4. 52.07% credit agreement 的统计显著性报告有误导性。** [R1-W4 Warning; R2 AGREE]
- $n=3000$ 下 +2.07pp 的 binomial test 得 $p=0.025$，统计显著但 effect size 极小。论文将此作为 "near-random" 证据（正确），但 $p=0.025$ 可能误导读者以为这是有意义的正偏离。未讨论 action validity 作为 locally correct 代理的局限性对数字的影响。

**W-Warning-5. ScienceWorld 验证不完整——仅验证 failure 未验证 fix。** [R1-W8 Warning; R2 AGREE]
- 声称 "pathology extends beyond our primary setting"，但 ScienceWorld 只报告 Cell A 崩溃，未报告 Cell D 结果。需补充至少一个 seed 的 Cell D ScienceWorld 结果。

**W-Warning-6. h-sweep threshold claim 仍基于 single seed。** [R1 隐含; R2-Q2]
- Window size sweep 发现 h=10 和 h=20 之间的 threshold，但仅基于 seed 1。考虑到 11-seed 评估显示的巨大方差，single-seed 的 threshold claim 缺乏统计支撑。

### Minor Issues

**M1.** Definition 1 中 "Equivalently" 声明（oracle advantage ↔ counterfactual replacement）未形式化证明。多步交互中窗口间行为相互依赖，counterfactual 定义不显然等价。 [R1-M1]

**M2.** Discussion Section 6 声称三条件触发 sign misattribution，但仅在 GRPO 框架内验证。需明确区分理论覆盖范围 vs 实验验证范围。 [R2-W5; R1 AGREE]

**M3.** Section 4.5 中 seed 分类标准（>50% from peak + below baseline for ≥3 consecutive steps）未讨论阈值敏感性。 [R1-M3]

**M4.** AI 使用声明中 "summarizing related papers to inform related-work section" 措辞可调整为 "identifying potentially relevant papers to inform our literature review"。 [R2-W6; R1 部分同意]

---

## Reviewer Consensus [AGREE]

1. **Cell C 缺失是论文最大的方法论缺陷**——两位 Reviewer 均认为这削弱了 factorial 分解的核心假设（正交可加性），Discussion 中的讨论不足以替代。
2. **Table 1 报告标准不一致**需要统一——标注不同标准不等于解决了不一致问题。
3. **理论-实验 gap（19.1% vs 52%）** 需要更严谨的桥接——定性正确但在理论导向论文中不够。
4. **REINFORCE++ 对比不公平**——15 步不足以得出结论。
5. **Eq. 6 单点测量不足**——需多阶段多种子补充。
6. **ScienceWorld 验证不完整**——需补充 Cell D 结果。
7. **诚实的种子报告是重要优点**——在当前 agent RL 文献中罕见。
8. **贡献定位适当**——诊断而非算法创新，避免了 overclaim。
9. **格式完全合规**——8 页正文、Limitations 在正文、double-blind、ACL template。

---

## Reviewer Divergence [REBUT]

1. **Overall 评分**：R1 给 3.5（Borderline Conference），R2 给 3.0（Findings）。R1 更看重诊断框架的方法论贡献；R2 更看重实验环境多样性和修复方案实用性。R2 认为 R1 偏高 0.5 分。
2. **单一环境 severity**：R1 认为 Minor-Major（理论不依赖环境）；R2 认为 Major→Critical（实验覆盖不足）。
3. **36% 种子成功率 severity**：R1 认为 Major（诊断论文自然边界）；R2 认为 Critical（诊断→修复叙事断裂）。
4. **增量贡献 vs 同期工作**：R1 反驳 R2——factorial 分解是独特方法论贡献，R2 低估了这一点。R2 坚持 IRC/MC-GRPO 等已覆盖类似问题。

---

## Questions（需要作者澄清）

**Q1.** [R1-Q1] Cell C 的 NaN 不稳定是否在所有 6 组超参中表现一致（均为 KL divergence 爆炸）？是否尝试过 gradient clipping per window position？

**Q2.** [R1-Q2] Cell B OOD 5.97% < SFT 6.72%——M1 是否导致 OOD 性能退化（而非仅施加 ceiling）？如果是，M1 的表述需要修正。

**Q3.** [R1-Q4, R2 交叉回应强调] HCAPO 在 h=2 达 91.4% (7B)，与 M1 诊断是否矛盾？是否说明对足够大的模型 M1 ceiling 已足够高？论文需在 rebuttal 中显式分析 HCAPO 如何改变了三条件中的哪一条。

**Q4.** [R2-Q1] 36% 种子成功率下，是否可以从早期训练信号（如 step 1 后的梯度统计、loss landscape 特征）预测最终泛化能力？

**Q5.** [R2-Q3] Episode-level GRPO 的 wall-clock 计算成本对比 step-independent 如何？这影响实践者采用意愿。

**Q6.** [R1-Q5] Evaluation variance analysis 仅测试了一个 Stagnant seed（seed200 step 5）。Generalized seeds 的评估方差是否相同？

---

## Missing References

1. **DAPO** (Yu et al., 2025) — GRPO 变体，涉及 clip-higher 和 dynamic sampling，与 advantage normalization 分析相关 [R2 提出, R1 AGREE]
2. **VAPO** (Liu et al., 2025) — value-based credit assignment，与 group normalization 符号错误诊断形成对比 [R2 提出, R1 AGREE]
3. **PRIME / Process Reward Models** — step-level supervision 的替代范式，与 episode-level GRPO 正交的解决思路 [R2 提出, R1 AGREE]
4. **Ahmadian et al. (2024)** "Back to Basics: Revisiting REINFORCE Style Optimization" — 与 REINFORCE++ 对比相关 [R1 提出]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~3 分钟）。结果：0 critical, 1 warning, 14 info。

**Warning:**
- Page 1-2 无任何 display item（figure/table），审稿人需翻到第 3 页才看到首个视觉锚点 Figure 1。建议将概念图或核心结果表提前到第 1-2 页。

**Info (正面):**
- Figure 1 概念图设计清晰，颜色区分度好，caption 自包含
- 全文颜色语义一致：橙色=Cell A, 蓝色=Cell B, 绿色=Cell D，色盲友好
- 所有 Table 使用 booktabs 风格，格式规范
- 公式渲染正确，无 LaTeX 错误残留，无 margin 溢出
- 主文 8 页符合限制，Limitations 在正文内，匿名格式正确

---

## Overall Assessment

### 综合评分

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |
| Excitement | 3.0/5 | 2.5/5 | **2.5/5** |
| Reproducibility | 3.5/5 | 4.0/5 | **3.5/5** |
| **Overall** | **3.5** | **3.0** | **3.0** |

### Overall: 3.0 (Findings)

**综合置信度: 4/5**

**评分理由：**

论文对 step-independent agent RL 训练中的信用分配病理提供了一个结构清晰、理论支撑的诊断框架。双机制分解（M1 + M2）和 factorial 实验设计是有方法论贡献的，直接符号测量指标具有可复用性，11-seed 的透明报告在当前文献中罕见。

但以下因素将论文定位在 Findings 而非主会议：

1. **实验完整性不足**：Cell C 缺失使 factorial 设计——论文的核心方法论——不完整；Table 1 报告标准混用削弱了跨条件对比的严谨性；理论与实验的定量 gap 缺乏形式化桥接。
2. **修复方案实用价值有限**：Episode-level GRPO 仅 36% 种子泛化且无原因分析，实践者缺乏可操作的指导。
3. **泛化证据不足**：主实验仅在单一环境（ALFWorld）完成；ScienceWorld 仅验证 failure 未验证 fix；8B 为 single-seed。
4. **与同期工作重叠**：IRC、MC-GRPO、GAGPO 等已独立发现类似问题，论文的增量知识贡献（factorial 分解 + 形式化）虽然独特，但 excitement 受限。

**改进路径（可在 rebuttal/camera-ready 中实现）：**
- 补充 ScienceWorld Cell D 单种子结果（验证 fix 跨环境）
- 统一 Table 1 报告标准
- 提供种子成功/失败的早期信号分析（即使是初步的）
- 在 Discussion 中加强 M1/M2 框架对选择修复方法的具体指导

若上述前两项在 rebuttal 中解决，论文可考虑升至 3.5（Borderline Conference）。

---

## Detailed Comments（逐 Section）

### Abstract (≈193 words, ≤200 ✓)
- 内容准确概括双机制诊断和主要发现。"17.2% mean OOD success versus 6.7% SFT baseline" 绝对数值偏低，建议同时强调相对提升（~2.6×）以避免"改进幅度不大"的第一印象。
- "fundamental credit assignment pathology" 用词与实验覆盖范围（单一环境）存在张力。

### Section 1 (Introduction)
- 开篇动机清晰，第一段即指出 step-independent 是 "unscrutinized implementation pattern"。
- 贡献列表精简为两项，与实际工作匹配，这是正面改进。
- Concurrent methods 定位合理（"validating that sign correctness is the critical factor"）。

### Section 2 (Method)
- POMDP 形式化清晰，GRPO advantage 公式正确。
- Step-independent windowing 描述精确，Eq. 2 正确归因 RAGEN。
- M1 ("constant ceiling") vs M2 ("cumulative degradation") 的对比是核心 insight。
- Episode-level training 正确定位为 GRPO 原始设计。
- Cell C 缺失首次提到，处理得当。

### Section 3 (Theoretical Analysis)
- Proposition 1-2 在 binary reward 下逻辑自洽。
- 19.1% 上界在 p=12.5%, K=8 处是有力结果。
- Reward saturation 分析有价值（~1/3 batch 零梯度）。
- **关键问题**：Eq. 6 的 comparable magnitude 假设基于单个快照。
- **关键问题**：Binary 理论 vs ternary 实验的 gap。

### Section 4 (Experiments)
- Setup 详细充分。
- **Table 1 报告标准不一致**是核心问题。
- Sign verification 的三层架构是方法论亮点。
- 11-seed 评估是全文最有价值部分之一；Fisher exact test 使用恰当；seed2 的 p=0.03 正确分类为 Stagnant。
- 8B 结果令人印象深刻但仅 single seed。ScienceWorld 不完整。

### Section 5 (Related Work)
- 覆盖较全。与 HCAPO/GiGPO 的定位（"diagnose why" vs. "propose fix"）合理。
- 缺失 DAPO、VAPO、PRIME。

### Section 6 (Discussion)
- "Non-additive mechanism interaction" 段落坦诚讨论了 Cell C 含义。
- "Seed-dependent OOD generalization" 仅描述现象，未提供假设或探索方向。
- "Practitioner guidance" 实用但可更具体。
- "Relationship to concurrent credit methods" 段落是有价值的外部验证论证。

### Section 7 (Conclusion)
- 简洁准确，scope 已缩窄至 "methods combining step-level windowing, sparse reward, and group-relative normalization"。

### Limitations
- 覆盖主要弱点（环境/规模有限、36% 泛化率、单次评估方差、长 episode 局限），约 4 个要点，长度适当。
- 合规。

### 格式合规
- ✅ `\usepackage[review]{acl}` 正确
- ✅ 正文 8 页（Sections 1-7 至 page 8）
- ✅ Limitations 在正文（page 9，`\section*{Limitations}`），非 appendix
- ✅ 仅一个 limitations section
- ✅ Abstract ≈193 words（≤200）
- ✅ Double-blind（`\author{Anonymous}`，无身份泄露）
- ✅ 参考文献格式一致（natbib/acl_natbib.bst）
- ✅ AI 使用声明（Appendix H）
