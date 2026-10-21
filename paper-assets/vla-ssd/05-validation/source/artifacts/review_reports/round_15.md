---
round: 15
review_mode: fresh
overall_score: weak reject
timestamp: 2026-05-22T13:58:06.559768+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# Round 15 审稿报告

**论文**: "Three Architectures, One Routing Pattern: How VLA Fine-Tuning Reshapes Instruction Flow"
**Venue**: CoRL 2026 | **Deadline**: 2026-05-29
**Reviewers**: R1（方法/统计）、R2（新颖性/贡献）、R3（Scope/格式/写作）
**模式**: Fresh review（无上轮记忆）

---

## Summary

本文对三种 VLA 架构（OpenVLA/Llama-2-7B, TracVLA/Phi-3-mini, NORA/Qwen2.5-VL-3B）在四个 LIBERO task suite 上进行跨架构表征分析，比较 trained 和 untrained checkpoints。主要发现：(1) R² exit collapse（action-probe 精度从中间层到出口层的下降）在所有 VLM→VLA 转换中一致出现（6/6 cells, sign test p=0.016）；(2) 所有 trained VLA 展示 counterfactual instruction sensitivity（Cohen's d ≥ 0.45）；(3) L1 instruction-dominant attention 来自 base model pretraining 而非 VLA fine-tuning。论文将 VLA instruction routing 分解为 training-induced 和 inherited 两类效应。

---

## Strengths

**S1** [三位共识] 研究问题新颖且有价值——首次系统跨 VLA 架构比较 fine-tuning 对内部表征路由的影响，3×4 矩阵化实验设计在 VLA interpretability 文献中无先例。

**S2** [三位共识] 附录极其详尽（26 页、30+ 辅助分析），包括 probe sensitivity（5 seeds）、threshold stability（30%-70%）、random-subset ablation（30 seeds）、等价检验、多重比较校正（48/65 通过 Bonferroni）。统计分析深度远超同类 interpretability 论文。

**S3** [三位共识] Limitations section 诚实完整：明确列出 N=2 VLM→VLA 限制、LIBERO-only、单 checkpoint、仅限 causal-decoder VLAs、NORA 缺 2/4 checkpoints。

**S4** [R1+R2] Training-induced vs inherited effects 的分解框架有洞察力——区分了 OXE 预训练遗留和 LIBERO fine-tuning 引入的效应，是有用的概念贡献。

**S5** [R2+R3] 多方法交叉验证（linear probes、RSA、CKA、attention analysis、counterfactual perturbation），结论不依赖单一指标。

**S6** [R3] NLP fine-tuning control（Llama-2-7b-chat, ΔR²≈0）提供了 VLA-specificity 的初步证据。

---

## Weaknesses

### Must-Fix（6 项，三位 Reviewer 达成共识）

**W-MF1** [critical, R1-N1 + R2-N1 + R3 AGREE] **标题 "One Routing Pattern" overclaim + sign test N=6 统计基础脆弱**

标题声称跨三种架构发现"一个路由模式"，但实际仅 N=2 独立 VLM→VLA 转换（TracVLA, NORA）。OpenVLA 因 OXE 预训练是 confounded data point（VLA→VLA 而非 VLM→VLA）。支撑 convergence 的唯一正式统计检验是 sign test（6/6 cells, p=0.016），但：(a) N=6 时 p=0.016 是最小可达 p 值，一个 cell 不符即失败（p=0.109），无统计余量；(b) 6 个 cell 非独立——同架构共享权重，同 suite 共享环境——有效独立 N 可能降至 2-3；(c) NORA 缺 Object/Long 两个 suite。核心 convergence claim 的统计基础无法支撑标题和 Abstract 的强度。

**W-MF2** [critical, R1-N2 + R2 AGREE + R3 AGREE] **N=63,228 伪重复导致 CI 系统性偏窄**

63,228 "观测"存在至少三层嵌套依赖：(a) 同 trajectory 内 timestep 高度时序相关；(b) 同模型不同层共享输入；(c) 同任务不同 demo 共享视觉/动作分布。有效独立单元数远低于报告值（可能仅 10 个 cells）。标准 bootstrap 不做 cluster correction 会系统性低估 uncertainty。Table 2 中精确到小数点后三位的 ΔR² 值（如 0.016, 0.038）可能给人误导性的置信感。

**W-MF3** [critical, R1-N3 + R2 AGREE + R3 AGREE] **Trained/Untrained 不对称性混淆跨架构可比性**

OpenVLA "untrained" 是 OXE 预训练 VLA（970K episodes），TracVLA/NORA "untrained" 是纯 VLM——这是质的不同。将三者混入同一 sign test 和"跨架构一致性"叙事中逻辑不自洽。论文虽在 Table 2 脚注和 Section 3.1 中标注了不对称性，但标题"Three Architectures"暗示三者地位平等。

**W-MF4** [critical, R3-N2 + R2 AGREE] **正文超过 CoRL 8 页限制**

Conclusion 最后 1-2 行溢出到第 9 页（References 之前）。CoRL 2026 严格限制正文 8 页（Limitations 计入）。页数超限是硬性格式违规，存在 desk rejection 风险。

**W-MF5** [critical, R3-N3 + R2 AGREE] **模板间距违规**

main.tex 包含 7 条 `\setlength` 命令修改浮动体间距、caption 间距和公式间距。CoRL 2026 要求 "Text density, fonts, spacing, and margins must match template exactly"。间距压缩后仍超页，说明内容根本性超出限制。

**W-MF6** [critical, R2-N3 + R3 AGREE(中等)] **与并发工作新颖性区分不足，Fang et al. 2026 未引用**

至少三篇高度相关并发工作未充分讨论：(a) Swann et al. (2026) 6 models × 4 benchmarks × 394K rollouts，规模远大；(b) Buurmeijer et al. (2026) 增加 intervention；(c) Fang et al. (2026) 在 LIBERO 上研究 VLA counterfactual instruction following（与本文 Section 3.3 / 4.3 方法论高度重叠但未引用）。Related Work 对 differentiation 不足。

### Should-Fix（10 项）

**W-SF1** [warning, R3-N1, R2 降级] **CoRL scope fit 偏弱**：纯 representational analysis，无物理机器人实验、无 closed-loop 评估。Discussion 中 actionable implications（early exit, layer pruning）全为推测。R2 认为非 desk-reject 级别但需 behavioral validation 桥接。R3 维持 must-fix 判定。报告将其列为 should-fix，但标注为高优先级。

**W-SF2** [warning, R1-W1 + R2 AGREE + R3 AGREE] **MLP probe 容量过大（105 万参数），linear probe 结果应提升至主文**。Appendix A.13 的 linear probe 结论一致且更有利于论文 claim（trained-untrained gap 更大），但主文完全未提及。

**W-SF3** [warning, R1-W2 + R2-W4 + R3 AGREE] **单一 checkpoint 无法支撑动态性语言**。标题 "Reshapes"、Abstract "emerges" 暗示训练过程中的动态变化，但仅分析 final checkpoint。建议改用 "is observed in" 等静态描述。

**W-SF4** [warning, R2-W2 + R3 AGREE] **论文定位模糊——confirmatory vs discovery**。Introduction 用 discovery 语言（"We identify"），Discussion 用 confirmatory 语言（"confirms"），不一致。建议统一为 confirmatory framing。

**W-SF5** [warning, R2-W3 + R3 AGREE] **Cohen's d ≥ 0.45 标注为 "substantial" 但仅为 medium effect**。实际 range 0.45-1.97，应报告分布而非用最小值加 "substantial" 标签。

**W-SF6** [warning, R1-W3 + R2 AGREE] **TOST 等价边界 δ=0.30 过宽且缺乏 justification**。在 R² 的 0-1 尺度上，δ=0.30 意味着接受 30% 绝对差异的"等价性"。应报告多个 δ 下的结果。

**W-SF7** [warning, R1-W6 + R2 AGREE + R3 AGREE] **Table 2 中 Cohen's d 与 cosine distance 并列暗示可比性**。两个 metric 量纲不同，不可直接比较，但 Table 2 将其放在同一列。应拆分或用格式明确区分。

**W-SF8** [warning, R1-W5 + R2-W1 + R3 AGREE] **Appendix "Cross-Benchmark Validation" 名不副实**：LIBERO 4 suite 共享模拟器/embodiment/action space，应改为 "Cross-Suite Validation within LIBERO"。

**W-SF9** [warning, R3-W2 + R3-W4 + R2 AGREE] **Abstract 信息过载 + Introduction 重复**。Abstract ~220 词含大量定量结果，对首次阅读者难以消化。Introduction 与 Abstract 内容 80% 重叠。

**W-SF10** [warning, R3-W1 + R2 AGREE] **对 CoRL 受众可读性门槛偏高**。RSA、CKA、probing classifier 等术语对机器人研究者未提供直觉解释。

---

## Reviewer Consensus

三位 Reviewer 独立达成以下共识（交叉分享后全部 AGREE）：

1. **OpenVLA 的 OXE pretraining confound 使"跨架构一致性"论据削弱**（R1-N3 = R2-N1 = R3 AGREE）
2. **Sign test N=6 统计力度不足，p=0.016 是最小可达值，独立性不成立**（R1-N1, R2/R3 AGREE）
3. **N=63K 伪重复未处理，CI 可能系统性乐观**（R1-N2, R2/R3 AGREE）
4. **标题 "One Routing Pattern" overclaim 超出 N=2 证据支撑范围**（R2-N1, R1/R3 AGREE）
5. **正文超页 + 间距违规是硬性格式问题**（R3-N2/N3, R2 AGREE）
6. **单 checkpoint + 动态语言矛盾**（R1-W2 + R2-W4 + R3 AGREE）
7. **Actionable implications 全为推测，缺乏任何验证**（R3-W5 + R2 AGREE）

---

## Reviewer Divergence

**仅一处实质性分歧**（已在交叉分享中部分收敛）：

| Issue | R2 | R3 | 共识 |
|---|---|---|---|
| CoRL scope fit 严重性 | Should-fix（CoRL 接受过分析性工作） | Must-fix（4/10 核心理由） | 高优先级 should-fix |

**一处事实性纠正**：
- R2-N2 判定 NLP control "缺失"。R3 指出 Section 5 存在 NLP control（Llama-2-7b-chat, ΔR²≈0.009），但方法细节严重不足。共识：control 存在但 presentation 不充分，需扩展为独立段落。

---

## Questions

**Q1** [R1-Q1] Sign test 的 6 个 cell 为何不包含全部 10 个 filled cells？是否因 metric 不可比？

**Q2** [R1-Q2] Bootstrap CI 是在什么层面 resampling 的？能否提供 task-level 或 demo-level clustered bootstrap 结果？

**Q3** [R1-Q6] 为何不用 mixed-effects model（random intercepts for architecture and task suite）处理嵌套数据？

**Q4** [R2-Q1] 对 Llama-2-7B 进行标准 NLP instruction tuning 是否也会出现 exit collapse？NLP control 的具体任务和设置是什么？

**Q5** [R2-Q4] Exit collapse 发现的 actionable guidance 是什么？知道它存在后，下一步是避免、利用还是仅观察？

**Q6** [R2-Q5] 相对于 Swann et al. (2026) 6×4×394K 的大规模研究，本文 3×4 矩阵的 incremental contribution 具体是什么？

**Q7** [R3-Q2] Paraphrased instruction 的 counterfactual sensitivity 是否说明模型依赖表面文本特征而非语义？这与 "encode task-relevant instruction information" 的 claim 是否矛盾？

**Q8** [R3-Q3] L1 instruction attention 是 inherited prior 而非 learned——这对 VLA 设计者的 actionable takeaway 是什么？

---

## Missing References

1. **Fang et al. (2026)** "When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs" (arXiv: 2602.17659) — 在 LIBERO 上研究 VLA counterfactual instruction following，引入 LIBERO-CF benchmark。与本文 Section 3.3/4.3 方法论高度重叠。**最重要的遗漏。**（R2-N3 提出，R3 AGREE）

2. 建议检查：**Circuit tracing / sparse autoencoder 在 VLM 上的应用**（如 arXiv 2602.20330），提供比 linear probes 更精细的 mechanistic insight。（R2 提出）

---

## External Review

**状态**：未请求（项目未配置 external_review.paperreview_ai）。

---

## Visual Layout Check

**状态**：✅ Done（2 warning, 0 critical, 10 info）

**Warnings**:
1. Pages 3-5 纯文本区域缺乏视觉锚点——Figure 1 (p2) 到 Figure 2 (p6) 间隔 3+ 页，审稿人在 Related Work→Method→Setup 段经历长段纯文本。建议在 page 3-4 区域增加概念图或方法示意图。
2. Figure 1 多面板极为密集（9+ 子图），打印尺寸下文字标签偏小（<8pt）。建议增大标签或减少 panel 数量。

**Info highlights**: 主体仅 4 个 display items（2 fig + 2 table），对 empirical analysis 论文偏少，大量关键证据全在 appendix。Table 2 和 Figure 2/3 格式规范、色盲友好。Appendix figures 质量良好。

---

## Overall Assessment

**评分**: Weak Reject (4.5/10)
**置信度**: High（三位 Reviewer 评分一致：5/5/4，交叉分享后共识程度高）

**评分理由**:

本文提出了一个有价值的研究问题——VLA fine-tuning 是否跨架构产生一致的 instruction routing pattern——并进行了系统性实验。附录的深度和诚实的 Limitations 值得肯定。

然而，论文面临三层结构性问题：

1. **统计框架缺陷**（W-MF1/2/3）：核心 convergence claim 依赖 N=6 sign test（刚好踩线，独立性不成立），63K 观测的伪重复使 CI 不可靠，OpenVLA 的 OXE pretraining confound 混淆了跨架构比较。这些不是 minor corrections——它们触及论文核心推断逻辑。

2. **Claims 与 Evidence 不匹配**（W-MF1/6, W-SF1/3/4/5）：标题 "One Routing Pattern" 远超 N=2 证据；"substantial" counterfactual sensitivity 实为 medium effect；"emerges" 暗示动态过程但仅分析 final checkpoint；actionable implications 全为推测。

3. **格式硬伤**（W-MF4/5）：正文超 8 页 + 7 条间距违规，存在 desk rejection 风险。

**可修复性评估**：格式问题（W-MF4/5）可在提交前修复。统计框架（W-MF1/2/3）需要 block bootstrap/mixed-effects model 重新分析，工作量中等但不确定结论是否维持。标题/framing overclaim（W-MF1）可通过文字修改解决。NLP control 扩展（W-MF6 部分）和并发工作讨论可在 revision 中完成。但 CoRL scope fit（W-SF1）和 LIBERO-only 限制（R9-N1 wont_fix）是结构性局限，无法通过 revision 解决。

**建议修改路径**（按优先级）：
1. **紧急**：移除 setlength 覆盖，压缩正文至 ≤8 页
2. **高优先级**：修改标题和 Abstract 降低 claim 强度；使用 block bootstrap 替代 sign test；将 OpenVLA 独立分析
3. **中优先级**：扩展 NLP control 描述；引用 Fang et al. 2026；添加并发工作 differentiation 段落
4. **如可行**：至少验证一个 actionable implication（如 exit collapse → early exit inference）来桥接 scope fit

如果以上 Must-Fix 中的统计和 framing 问题得到解决，且增加一个 behavioral validation 实验，评分可上调至 Borderline/Weak Accept (5-6/10)。

---

## Detailed Comments

### Section-by-Section

**Abstract**: 信息过载（~220 词含大量数字）。"substantial counterfactual sensitivity (d ≥ 0.45)" 应改为 "moderate to large (d = 0.45-1.97)"。"consistently emerges" 应改为 "is observed in"。建议聚焦 2-3 个 high-level takeaway。

**Introduction**: 与 Abstract 内容 80% 重复。三条 contribution 表述与 Abstract 高度相似。建议精简，将篇幅让给 motivation（为什么机器人研究者应关心 instruction routing）。

**Related Work**: 引用覆盖 adequate（Aghajanyan 2021, Kumar 2022 已补充），但缺少 Fang et al. 2026。与 Swann 2026、Buurmeijer 2026 的 systematic differentiation 不足。建议增加 dedicated 对比段落。

**Method (Section 3)**: 对 CoRL 受众，RSA/CKA/probing 术语需 1-2 句直觉解释。L1 attention 50% 阈值的 sensitivity analysis（Table 19）应在主文提及。Counterfactual 分析的 metric incomparability 说明到位但可更突出。

**Experiments (Section 4)**: Table 2 是论文核心——需明确标注 metric 类型差异。Sign test p=0.016 应伴随 power/independence caveat。NLP control 仅 Discussion 一句话，应扩展为独立段落。Linear probe 结论（A.13）应提升至此处。

**Discussion (Section 5)**: 深度不足。"Three-tier gradient" 框架仅在 Appendix，应提升。Actionable implications 全为推测，措辞应弱化为 "hypotheses for future work"。"Orthogonal contribution" 措辞对 closed-loop validation 过于 dismissive。

**Conclusion (Section 7)**: 与 Discussion 重复。溢出到第 9 页。建议合并或精简至 3-4 句。

**Format**: 7 条 setlength 违规必须移除。Keywords 行需确认是否为 CoRL 2026 要求。GenAI disclosure 位置（References 后 Appendix 前）需确认合规。

**Appendix**: 极其详尽。Table 27 resizebox 导致字体过小，可拆分。"Cross-Benchmark Validation" 应改为 "Cross-Suite"。"Robust attractor" 措辞较主文更强，应一致化。