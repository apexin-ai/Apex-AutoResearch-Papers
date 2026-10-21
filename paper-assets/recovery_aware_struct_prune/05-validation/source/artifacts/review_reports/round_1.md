---
round: 1
review_mode: fresh
overall_score: 2.5 - Borderline Findings
timestamp: 2026-05-20T05:37:14.562807+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Recovery-Aware Structured Pruning for Reasoning Language Models

**目标 Venue**: EMNLP 2026 Main (via ARR)
**审稿配置**: 2 Reviewers × 1 Round + Cross-sharing
**报告日期**: 2026-05-20

---

## Summary

本文在 DeepSeek-R1-Distill-Qwen-7B 上以 20% 结构化 sparsity 对比四种剪枝标准（CKA-only、Random、Standard/importance-only、RASP/composite）在相同 GRPO 训练下的恢复表现，发现 "recovery capacity gradient"：CKA-only >> Random >> Standard > RASP。核心论点是保留表征多样性（通过 intra-layer CKA 冗余度衡量）比保留梯度重要性更有利于 RL 恢复。附加实验包括 1.5B 跨规模验证、300 步扩展训练、四基准 OOD 评估、α 消融和 CKA 稳定性分析。

---

## Strengths

1. **重要且被忽视的研究问题**：剪枝标准如何影响下游 RL 恢复是一个有实际价值的问题，此前无人系统研究。两位 Reviewer 一致认可。
2. **控制实验框架设计原则正确**：共享结构分析 → 不同评分准则 → 相同恢复流程，Algorithm 1 清晰可复现。
3. **丰富的训练动态诊断**：reward trajectory、f₀（zero-variance batch fraction）、gradient norm、KL divergence 提供了多维度恢复动态视图，超越了传统的单指标评估。
4. **定性发现有价值**：不同剪枝标准导致定性不同的 GRPO 动态（active learning / stagnation / collapse）是有趣的观察。
5. **CKA scoring 高度稳定**（Spearman ρ ≥ 0.964, Table 9），增强了该指标的实用性。
6. **格式完全合规**：ACL review 模板、8 页正文、匿名合规、Limitations section 齐全。

---

## Weaknesses

### Must-Fix（6 项，两位 Reviewer 共识）

**[W-C1] Post-SFT 准确率混淆变量未控制** [R1-N1, R2 AGREE]
CKA-only post-SFT 准确率 63.91%，Standard 59.29%，RASP 61.49%——CKA-only 比 Standard 高 4.6pp。替代假设：更高起始准确率 → 更多正确 completion → 更多 reward 信号 → 更好 GRPO 学习。论文将此作为 "SFT recovery gradient" 讨论（Section 4.4），但未作为混淆变量控制。R2 补充：RASP post-SFT 61.49% > Standard 59.29% 但 RASP collapse 更严重，说明非唯一因素，但这不免除控制此变量的义务。**不控制起始准确率，核心因果声明（diversity → recovery）无法成立。**
→ 建议：添加实验均衡 post-SFT 准确率后重跑 GRPO，或做 partial correlation analysis。

**[W-C2] Table 2 混用控制实验与 "separately optimized runs"** [R1-N2, R2 AGREE]
Table 2 caption 明确写 "GRPO accuracy is evaluated on best-performing checkpoints from separately optimized runs; training dynamics in Table 1 use the controlled v5 configuration"。Standard 在 step 300 评估、CKA-only 在 step 100、RASP 在 step 5——不同方法有不同训练预算和停止点。"separately optimized runs" 的超参配置未定义。论文在 Section 4.2-4.3 交替引用 Table 1 和 Table 2 但从未解释两者的配置差异。R2 交叉回应中认为此问题比初始评估更严重——**动摇了论文核心数字的可信度**。
→ 建议：补充控制实验（Table 1 同一 run）的 step-100 准确率；定义 "separately optimized runs" 配置。

**[W-C3] `reward_desert_patience` 参数不一致** [R1-N3, R2 AGREE]
CKA-only/Random patience=50, Standard/RASP patience=200。论文声称 "GRPO configuration is held constant across all four pruned models"（Section 3.5, experiments.tex L27），但此参数实际不同。Figure 2 caption 提到 Random "timed out at step 97; 9 steps shown"——可能受 patience=50 触发早停。R2 补充：对 collapse 方法设更高 patience 允许它们在零 reward 下训练更久，可能**加剧** collapse 使对比不公平。**违反了论文反复强调的 "identical configuration" 核心前提。**
→ 建议：所有方法使用相同 patience 重跑，或证明差异无影响。

**[W-C4] 单种子设计，seed 消融不完整** [R1-N4, R2 AGREE]
主实验仅 seed 42；Appendix H 仅对 CKA-only 做了 seed 123 对比（Δ=0.15pp）。Standard、RASP、Random 的 seed 敏感性完全未知。R2 强调：真正需要 seed 消融的是 collapse 方法——collapse 行为本身可能是 seed-dependent 的。**如果换一个种子 Standard 不 collapse，"recovery capacity gradient" 叙事就瓦解。** N=1 的实验无法支撑 "qualitatively distinct training dynamics" 的结论。
→ 建议：至少 3 seeds 重复实验，报告均值 ± std。

**[W-C5] 标题与结论严重错位** [R2-N1, R1 AGREE]
标题 "Recovery-Aware Structured Pruning" 暗示论文提出了一个 recovery-aware 的剪枝方法。然而 RASP（Recovery-Aware Structural Pruning）是实验中表现**最差**的方法（peak reward 0.061, full collapse），而论文实际推荐的 CKA-only 完全不使用 gradient importance。读者对标题的期望与论文实际结论完全相反。**影响论文的叙事诚信性。**
→ 建议：标题应反映实际发现，如 "Representational Diversity Matters More Than Importance for Post-Pruning RL Recovery"。

**[W-C6] 实验规模不足以支撑一般性声明** [R2-N2, R1 AGREE]
仅 1 模型（DeepSeek-R1-7B）× 1 sparsity（20%）× 1 RL 算法（GRPO）× 1 数据集（GSM8K）。30% sparsity 全 collapse（Table 3）；1.5B cross-scale 准确率极低缺乏说服力。Abstract 称 "gradient importance scoring is actively harmful for post-pruning RL alignment"、Section 5 称 "substantially shapes"——从单一配置得出普遍性声明不满足 ARR Soundness 标准。
→ 建议：至少增加 1 个不同架构 + 1 个额外 sparsity level，或大幅弱化 claims 加限定词。

### Should-Fix（8 项）

**[W-S1] 相关→因果跳跃** [R1-W1, R2 AGREE]
Section 5 声明 "The mechanism is preserved representational diversity"。Figure 4 显示 CKA-only 与 dense 模型 CKA 差异最大（μ=0.62），但这是相关性。R2 补充：低 CKA similarity 可能是 active learning 的**结果**而非**原因**。
→ 建议改为 "a plausible mechanism is"，讨论替代解释。

**[W-S2] "actively harmful" overclaiming** [R1-W2 + R2-W5, mutual AGREE]
"Gradient importance scoring is actively harmful" 暗示比不剪枝更差——论文未提供此比较。结合 W-C1 confound，可能仅因起始准确率低。
→ 弱化为 "underperforms CKA-based scoring in our controlled setting"。

**[W-S3] MATH-500 含 TBD 条目** [R1-W3, R2 AGREE, 视觉审查 critical]
Table 7 有多个 TBD（CKA-only GRPO Truncated%、Standard SFT/GRPO Truncated%）。提交论文中出现未完成数据不可接受。
→ 完成评估或删除表格。

**[W-S4] 主结果缺乏统计检验** [R1-W5, R2 AGREE]
Fisher test 仅在 N=100 子集；N=1,319 完整结果无 CI。CKA-only +0.46pp 是否显著？
→ 添加 bootstrap CI 或 McNemar's test。

**[W-S5] 缺乏与 Self-Healing 的性能差距讨论** [R2-N3, R1 REBUT→降级]
Self-Healing (Ji et al., 2025) 在 25% 压缩下达到 95%+ 准确率，本文最佳 64.37%。R1 认为实验条件不可直比（不同模型/方法/恢复设置），降为 Should-Fix。但论文仅一句话提及且未解释巨大差距。
→ 在 Related Work 或 Discussion 中讨论条件差异和性能差距来源。

**[W-S6] Orphan 引用 + CKA 可靠性未讨论** [R2-W1/W2, R1 AGREE]
8 个 bib 条目未引用（rac2025, ssgr2025, doingmore2026, opsd2026, davari2023cka 等），多篇高度相关。特别是 Davari et al. (2023) 讨论 CKA 可靠性——论文核心依赖 CKA 但未提及已知局限。
→ 引用讨论相关 entries，特别是 CKA 可靠性。

**[W-S7] 引用年份不一致** [R2-W4, R1 AGREE]
lachance2024cka（实际 2022 硕士论文）、klabunde_similarity_survey_2025（实际 2023）。
→ 修正年份。

**[W-S8] 跨规模验证薄弱** [R1-W4, R2 AGREE]
仅 1.5B GSM8K 一个基准；Random 缺失；Section 5 "structural advantage is not scale-dependent" 证据仅一个额外数据点。
→ 弱化为 "preliminary evidence suggests the ordering may hold across scales"。

### Minor（4 项）

- **[W-M1]** "Reward-accuracy decoupling" 可能仅反映 100 步 GRPO 对 accuracy 影响本身就小，非根本性解耦。[R1-M1]
- **[W-M2]** Abstract 中 "self-recovery from mid-training perturbations" 仅来自单次事件（step 90, 单种子单 run），放在 abstract 过度宣传。[R1-M2]
- **[W-M3]** "Recovery capacity" 贯穿全文作为核心概念但未给出形式化定义（peak reward? mean reward? accuracy delta?）。[R1-M3]
- **[W-M4]** Table 5 与 Table 1 的 reward 值不一致（Standard 0.054 vs 0.081/0.050），未说明 Table 5 报告的是哪个 step。[R1-M4]

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上完全一致（[AGREE]）：
1. **实验控制缺陷**：post-SFT 准确率混淆(W-C1)、Table 2 混用配置(W-C2)、patience 不一致(W-C3)、单种子(W-C4)——这四个问题共同动摇了 "controlled comparison" 的核心前提
2. **Claims 过强**：标题暗示错误方法(W-C5)、一般性声明缺乏支撑(W-C6)、"actively harmful" 无充分证据(W-S2)
3. **引用问题**：orphan entries(W-S6)、CKA 可靠性未讨论(W-S6)、年份错误(W-S7)
4. **数据不完整**：MATH-500 TBD(W-S3)

## Reviewer Divergence

| 问题 | R2 评级 | R1 评级 | 最终判定 | 理由 |
|------|---------|---------|----------|------|
| Self-Healing 对比 | Critical (N3) | Should-Fix | **Should-Fix** | R1 REBUT：实验条件不可直比（不同模型/pruning/recovery），但应讨论差距来源 |
| 技术贡献深度 | Critical (N4) | Not independent | **注意事项** | R1 REBUT：EMNLP 有 empirical study 先例；深度不足是实验控制问题的下游后果 |
| OOD 结果价值 | Padding (W3) | 有补充价值 | **Should-Fix (TBD)** | R1 partial REBUT：MATH-500 保留 ranking (6.4pp gap)，但 TBD 条目削弱说服力 |

---

## Questions for Authors

1. Random baseline 的 post-SFT 准确率是多少？（缺失数据，对评估 W-C1 至关重要）
2. 若通过增加 SFT epoch 将 Standard/RASP post-SFT 准确率提升到与 CKA-only 接近，recovery gradient 是否依然存在？
3. `reward_desert_patience` 差异是设计选择还是疏忽？能否以统一值重跑？
4. Table 2 中 "separately optimized runs" 的 GRPO 配置与控制实验是否完全一致？"v5 configuration" 具体指什么？
5. 在 30% sparsity（Table 3）下 CKA-only 崩溃到 0% 而 Standard 保留 4%——这是否削弱 "表征多样性保护恢复能力" 的论点？
6. Davari et al. (2023) 对 CKA 可靠性的批评是否影响本文的 intra-layer CKA 使用？
7. intra-layer CKA vs inter-layer CKA 是否做过消融？MPruner 的 inter-layer 方法在本文设置下效果如何？

---

## Missing References

1. **Davari et al. (2023, ICLR)** — "Reliability of CKA as a Similarity Measure in Deep Learning" — 已在 bib 未引用，作为论文核心指标 CKA 的可靠性研究**必须**讨论
2. **RAC (Lucas et al., 2025, NeurIPS)** — "Reasoning Models Can be Accurately Pruned Via CoT Reconstruction" — 已在 bib 未引用
3. **SSGR (Xiang et al., 2025)** — "Think Before You Prune: Selective Self-Generated Calibration" — 已在 bib 未引用
4. **OPSD (Kim & Lee, 2026)** — "OPSD Compresses What RLVR Teaches" — 已在 bib 未引用，直接相关 post-RL 压缩
5. **Doing More With Less (Monjur et al., 2026)** — 已在 bib 未引用
6. **A Free Lunch in LLM Compression** (arXiv 2510.14444) — 剪枝后 retraining，R2 建议补充

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求**（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态：已完成** (2026-05-20T05:21 → 05:23, 约 2 分钟)

| 严重度 | 数量 | 关键发现 |
|--------|------|----------|
| Critical | 1 | Table 7 (MATH-500) 含 TBD 条目——提交论文中出现未完成数据严重损害可信度 |
| Warning | 3 | (1) Pages 3-5 连续纯文本无 figure/table，审稿人注意力易流失；(2) Figure 5 三个 subfigure 字号极小(≤6pt)，打印后难以辨认；(3) 末页(p12) 约 1/3 空白 |
| Info | 10 | 首页无视觉锚点(Figure 1 在 p2 可接受)；Figure 1 纯文字流程图吸引力有限；Figure 2 颜色在灰度打印下可能难辨别（建议加 line style）；Figure 3 y 轴标签偏小(~7pt)；Table 3 信息量少可合并至正文；Figure 4 热力图子图较小需检查打印可读性 |

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 2.5 | 2.5 (交叉后倾向 2.0) | **2.0** |
| Excitement | 3.0 | 2.5 | **2.75** |
| Reproducibility | 3.5 | 3.0 | **3.25** |
| **Overall** | **2.5** | **2.5** | **2.5 (Borderline Findings)** |
| Confidence | 4 | 4 | **4** |

### 总评

**2.5 / 5 — Borderline Findings**

研究问题重要且被忽视（剪枝标准对 RL 恢复的影响），控制实验框架设计原则正确，定性发现（不同剪枝标准产生定性不同的 GRPO 动态）有价值。

但论文存在 **6 个 critical 问题**，其中 4 个直接动摇了 "controlled comparison" 的核心前提：(1) post-SFT 准确率作为未控制混淆变量使因果声明不成立；(2) Table 2 混用控制与非控制实验的结果使关键数字可信度存疑；(3) patience 参数不一致违反 "identical configuration" 声明；(4) 单种子设计使所有定量结论的可靠性不足。另外 2 个 critical 问题影响论文的整体定位：(5) 标题暗示 RASP 是所提方法但 RASP 实际表现最差；(6) 单一实验配置无法支撑广泛的一般性声明。

**修补路径**：若解决 W-C1（控制起始准确率实验）、W-C3（统一 patience）、W-C4（3+ seeds）、W-C5（改标题）、W-C6（弱化 claims 或增加实验），论文有潜力达到 3.0-3.5（Findings 水平）。当前状态下距离 Main Conference 接收标准（4.0）有显著差距。

---

## Detailed Comments（逐节）

### Abstract
- "self-recovery from mid-training perturbations" 仅来自单次事件（step 90），放在 abstract 过度宣传 [W-M2]
- "gradient importance scoring is actively harmful" 过强 [W-S2]

### Introduction
- Figure 1 作为首个 display item，传达实验框架但为纯文字流程图，视觉吸引力有限
- "the pruning criterion substantially shapes recovery capacity" 在单一配置下过度泛化 [W-C6]

### Method (Section 3)
- 框架设计清晰，Algorithm 1 可复现
- "recovery capacity" 未形式化定义 [W-M3]
- Section 3.5 声称 "GRPO configuration is held constant" 但 patience 实际不同 [W-C3]

### Experiments (Section 4)
- Table 1: 结果展示清晰，但单种子无法评估方差 [W-C4]
- Table 2: 混用配置严重问题 [W-C2]；缺乏统计检验 [W-S4]
- Section 4.4: SFT gradient 应作为 confound 讨论而非 feature [W-C1]
- Random post-SFT 准确率缺失——对评估 W-C1 至关重要
- Table 5 reward 值与 Table 1 不一致 [W-M4]

### Extended Analysis (Section 4.5)
- Figure 4 CKA heatmap: 相关性不等于因果 [W-S1]
- Cross-scale: 仅 1.5B GSM8K，Random 缺失 [W-S8]

### Conclusion (Section 5)
- 因果语言过强（"The mechanism is..."） [W-S1]
- 未讨论 CKA 可靠性局限 [W-S6]

### References
- 8 个 orphan entries [W-S6]
- 2 处年份错误 [W-S7]

### Appendix
- MATH-500 TBD 条目 [W-S3]
- Figure 5 字号过小(≤6pt) [视觉审查]
- Seed 消融仅覆盖 CKA-only [W-C4]