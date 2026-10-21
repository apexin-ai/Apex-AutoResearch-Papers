---
round: 39
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T13:51:45.448728+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 39 审稿报告 — struct_self_consist_ie

**论文**: "When Does Test-Time Scaling Fail? A Diagnostic Framework for Named Entity Recognition"
**Venue**: EMNLP 2026 (via ACL Rolling Review, long paper)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作）
**轮次**: Round 1（1 轮初审 + 交叉回应，达成收敛）

---

## Summary

本文研究 test-time compute scaling（self-consistency / best-of-N）在 NER 任务上何时成功、何时失败。在 4 个英文 NER 数据集、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）上，作者发现了 correlation-selection gap：质量估计信号（AUROC 达 0.82）能预测输出质量，但 instance-level selection 几乎无法带来增益（MV gain <1pp）。论文提出诊断框架，以 degeneracy（多样本坍缩）和 signal alignment collapse（LP 压缩）作为联合诊断条件，并探索了 entity-level construction 作为缓解策略（+1.40pp on Few-NERD，global Holm p=0.055）。RE 和 SQL 作为 exploratory pilot 扩展。

---

## Strengths

**S1. 研究问题重要且切入点好。** [R1, R2 共识] Correlation-selection gap 的识别——quality estimation 有效但 selection 失败——对依赖 self-consistency 的 LLM pipeline 有直接实践指导意义。

**S2. 实证工作极为详尽。** [R1, R2 共识] 45 页论文（含 36 页附录），覆盖 4 个 NER 数据集、2 个模型家族、9 类方法、多种 N 值（8-64）和温度（0.7-1.0），附录包含 temperature/seed robustness、calibration analysis、per-entity-type analysis 等。实验设计的 thoroughness 在分析型论文中属上乘。

**S3. 负面结果诚实报告。** [R1, R2 共识] 69% N-transitions 出现 inverse scaling、cross-dataset transfer negative、5-epoch 训练消除 LP gains（91% collapse）。论文反复强调 "diagnostic rather than predictive"，没有过度宣称。

**S4. 理论连接有深度。** [R1, R2 共识] MBR decoding 连接（Proposition 2）、degeneracy decomposition 的概念性分解（虽 bound 过松）为理解 SC 失败提供了有用的分析框架。

**S5. Robustness 检查全面。** [R1] Temperature sensitivity、seed stability、sample size effects、FK independence test、bootstrap significance、permutation tests 均有覆盖。

**S6. 实用指导明确。** [R1, R2 共识] §9 "When not to scale"：degeneracy < 20% 时考虑 LP selection，ρ > 0.70 时选 LP；N=8 pilot = 12.5% of N=64 full scaling cost。

---

## Weaknesses

### Must-Fix（4 项共识 + 1 项争议严重性）

**W1. [critical] [R1+R2 共识] 正文超过 8 页限制。** §9 Discussion 起始于 PDF 第 9 页，主文约 8.6 页，超出 EMNLP 2026 strict 8-page limit 约 0.6 页。格式违规存在 desk reject 风险。需压缩 §8 Related Work（约 30-40%）或将部分 §9 内容移至 Appendix。

**W2. [critical] [R1+R2 共识] Proposition 1 bound (1−D)·G_nd·α 仅 capture 3-12% actual gains。** 尽管 Round 38 后已添加 "illustrative directional analysis" 定位和 looseness 讨论（split-half r=0.578-0.644, conservative α），但以 formal proposition 形式呈现于主文 §6.3 仍给人以定量诊断工具的错误印象。两位 Reviewer 共识：定性分解有价值（三因子可独立干预），但应降级呈现——formal proof 移至 Appendix，主文保留分解直觉。

**W3. [critical] [R1+R2 共识] 3-epoch vs 5-epoch confound 严重威胁 Few-NERD 核心正面结果。** Few-NERD 是论文最核心的正面结果来源（唯一 Holm p_adj < 0.05 的 LP selection, +1.39pp），但 5-epoch 训练使 LP gains collapse 91%（+1.39 → +0.12±0.04pp）。Entity construction +1.40pp 同样基于 3-epoch 模型，5-epoch entity construction 结果未报告。论文 §8 已有 paragraph 讨论但 visibility 不足。两位 Reviewer 共识：(a) 5-epoch entity construction 结果必须报告；(b) Few-NERD 5-epoch 纳入主文 Table 作 paired comparison；(c) ScIERC 补 epoch ablation 确认一般性。

**W4. [critical] [R2 critical, R1 部分同意] Entity construction p=0.055 (global Holm k=57) 统计显著性不足 + family partition 未 pre-register。** R2 视为 critical（唯一改进策略 borderline significance）；R1 认为 family-wise (k=21) p_adj=0.021 显著，建议定位为 "family-wise significant, global borderline"。两人共识：需在 §7.5 讨论 family partition rationale，明确 pre-registration 缺失，Abstract 降调表述。

**W5. [disputed severity: R1 Must-Fix / R2 Should-Fix] Probe 使用 Qwen2.5-7B 而非主实验 Qwen3-8B，introspection boundary 论证链存在 architecture gap。** R1 认为 §3 probe 是 introspection boundary 论证的关键支撑，architecture mismatch 削弱核心论证链。R2 认为 probe 是 supporting evidence（机制解释）而非 load-bearing evidence，核心发现 §4-§7 不依赖 probe。分歧未解决。建议：在 Qwen3-8B 上补 probe 验证（至少一个数据集），或更显著标注 architecture mismatch 及其影响。

### Should-Fix（9 项）

**W6. [warning] [R2 critical, R1 REBUT] 新颖性相对 Landesberg (2026)/Yao (2026)/Yun (2025) 并发工作偏弱。** R2 认为 correlation-selection gap 与 Landesberg 重叠、degeneracy 与 Yun diversity collapse 概念相似、instance-level 延伸可能 incremental，更适合 Findings。R1 反驳：instance-level gap 是 qualitatively different phenomenon，entity construction 在 prior work 未出现，structured prediction 的 entity-level diagnostic 是 novel contribution。**分歧未解决**。建议：更明确论证 NER-specific findings 的不可替代性——(a) 为什么 Landesberg reasoning 结论不能推导到 structured IE；(b) 强调 LP compression 和 entity construction 是 NER-specific 独有发现。

**W7. [warning] [R1+R2 共识] Cross-model ensemble 仅 Few-NERD 一个数据集验证。** §5.1 Qwen+LLaMA 混合（4+4 samples, +0.42pp），但未在 SciERC/CoNLL 上验证。

**W8. [warning] [R1+R2 共识] RE (n=397) / SQL (n=196) pilot 覆盖太薄。** Abstract "exploratory extensions" 仍可能过强；SQL 在主文提及但无 table/figure。

**W9. [warning] [R1 提出, R2 同意] LightGBM trained verifier cross-dataset transfer failure 未做 feature-level root cause analysis。** §5.2 归因 "dataset-specific feature mappings" 但未分析具体 features。

**W10. [warning] [R1+R2 共识] 69% inverse scaling 与 conditional gains framing 仍有张力。** Abstract/§1 应更 upfront 说明 scaling fails in majority of configurations。R1 不升级至 Must-Fix（标题 + §6.2/Limitations 已报告）。

**W11. [warning] [R2 提出, R1 同意] 正文数字密度过高。** §4/§6/§7 单段内 6+ 统计量，narrative thread 难以跟踪。建议将更多数字移入 Table/Appendix。

**W12. [warning] [R1+R2 共识] Token-level uncertainty / entity-level calibration / self-evaluation Related Work 覆盖不足。** 缺失引用：Vazhentsev et al. (2022)、Kuleshov et al. (2022)、Kadavath et al. (2022)。另外 Smith & Eisner (2006) MBR for structured prediction 可加强理论连接。

**W13. [warning] [R2 提出, R1 同意] Degeneracy 术语歧义。** 跨学科含义不同，首次使用缺乏术语选择说明。

**W14. [warning] [R2 提出, R1 部分反驳] Related Work 密度过高。** §8 约 1 页覆盖 6 个子主题，每个方向讨论偏表面。R1 认为 §8 位置在 EMNLP 实证论文中常见，不构成问题。

---

## Reviewer Consensus [AGREE]

1. **实验规模和严谨性是论文主要优势**——4 个 NER 数据集、2 个模型家族、45 页含详尽 Appendix
2. **页数超限必须修复**——约 8.6 页，超出 0.6 页（R1 初审遗漏，交叉后追认）
3. **Proposition 1 bound 过松（3-12%）**——应降级呈现，formal proof 移至 Appendix
4. **Epoch confound 是对主要正面结果的严重威胁**——5-epoch entity construction 结果必须报告
5. **p=0.055 需要更透明讨论**——family partition rationale + pre-registration 缺失
6. **69% inverse scaling 是诚实但需更突出呈现的 negative finding**
7. **论文的实践价值（"When not to scale" 指导）有意义**
8. **Missing references**：Vazhentsev (2022), Kuleshov (2022), Kadavath (2022)
9. **Reproducibility 高**（Appendix 详尽，承诺 code/data release）

---

## Reviewer Divergence [REBUT]

**1. 总评分：R1 3.5 (Borderline Conference) vs R2 3.0 (Findings)**
- 核心驱动因素：**新颖性评估**
- R1 认为 instance-level diagnostic + entity construction 在 structured IE 中构成 novel contribution，不应降至 Findings
- R2 认为与 Landesberg (2026) correlation-selection gap、Yao (2026) task-level correlation、Yun (2025) diversity collapse 的重叠度过高，contribution 更接近 targeted analysis

**2. Probe architecture gap 严重性：R1 Must-Fix vs R2 Should-Fix**
- R1：introspection boundary 是框架重要组成，architecture mismatch 削弱核心论证链
- R2：§3 probe 是 supporting evidence 非 load-bearing evidence，核心发现 §4-§7 不依赖 probe

---

## Questions（合并去重，8 项）

**Q1.** [R1] Proposition 1 假设 entity independence，但 NER 中同一句子的 entities 有 structural correlation。CoNLL bound ratio 为负（Table 31: −0.42），是否说明 independence 假设严重违反？

**Q2.** [R1+R2] 在 converged models（5+ epochs）上，entity construction 仍能获正增益的条件是什么？论文是否有 5-epoch entity construction 数据？

**Q3.** [R2] Few-NERD vs SciERC/CoNLL 增益差异的主要驱动因素？是 entity type 粒度（66 vs 4 types）还是 dataset difficulty？

**Q4.** [R2] ESJ AUROC 0.512（chance level）是否受限于 binary yes/no prompt 设计？是否尝试过 confidence elicitation 或 chain-of-thought verification？

**Q5.** [R2] GPT-5.5 degeneracy 更高（50% on Few-NERD vs Qwen3-8B 13%）的原因？与 API 的 temperature 实现有关？

**Q6.** [R1] Cross-model ensemble 在高 degeneracy datasets（CoNLL 61.7%）上效果如何？

**Q7.** [R1] BH FDR 19/57 significant vs Holm borderline 的差异是否值得在主文更 prominently 讨论？

**Q8.** [R2] Instruction-tuned（非 fine-tuned）模型的 degeneracy 模式是否有本质不同？

---

## Missing References（合并）

1. **Token-level uncertainty**: Vazhentsev et al. (2022, "Uncertainty Estimation of Transformer Predictions for Misclassification Detection", ACL)
2. **Structured calibration**: Kuleshov et al. (2022)
3. **Self-evaluation reliability**: Kadavath et al. (2022, "Language Models (Mostly) Know What They Know")
4. **MBR for structured prediction**: Smith & Eisner (2006, "Minimum Risk Annealing"), Goel & Byrne (2000)
5. **Process reward models / SC failure**: Welleck et al. (2024), Lightman et al. (2024) — 已在 References 中但未在 §8 充分讨论

---

## External Review (Stanford Agentic Reviewer)

**状态**：未请求。项目未配置外部审稿。

---

## Visual Layout Check（非评分项）

**状态**：超时（Agent timed out after 300s）。无排版检查结果。用户可重新触发 `dispatch_visual_check`。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**Confidence: 4/5**

**总评**：

这是一篇方法论严谨、实验规模可观的分析型论文，成功识别并系统诊断了 self-consistency 在 NER 上的 correlation-selection gap。核心发现（quality estimation 有效但 selection 失败）对 NLP 社区有直接参考价值，诊断框架（degeneracy + LP compression 的联合诊断）提供了有用的分析 lens。

将论文定位在 Findings (3.0) 而非 Borderline Conference (3.5) 的理由：

1. **格式违规**：正文约 8.6 页，超出 EMNLP 2026 strict 8-page limit。这是提交前必须解决的硬约束。
2. **核心正面结果脆弱**：唯一的改进策略（entity construction +1.40pp）在 global Holm 校正后仅 borderline significant (p=0.055)，且依赖 under-converged model（3-epoch，5-epoch collapse 91%）。从诊断到处方的桥梁在当前版本不够坚固。
3. **并发工作重叠**（R2 critical, R1 rebuts）：Landesberg et al. (2026) 独立发现 correlation-selection gap，Yao et al. (2026) 已有 task-level correlation。本文增量贡献主要在 NER-specific 细粒度诊断——这是有价值的但更接近 targeted analysis 而非 broad contribution。
4. **理论贡献有限**：Proposition 1 bound 仅 capture 3-12% actual gains，定量诊断价值不足。

**但论文有明确的上升空间**（若 revision 修复关键问题）：
- 压缩至 8 页 → 消除 desk reject 风险
- 报告 5-epoch entity construction 结果 + ScIERC epoch ablation → 确认或排除 epoch confound
- 更清晰论证 NER-specific findings 的不可替代性 → 回应新颖性 concern
- 上述修复后，论文有潜力达到 **3.5 (Borderline Conference)**

**R1 与 R2 评分差异说明**：R1 (3.5) 更重视方法严谨性和实验深度，认为 instance-level diagnostic 构成 novel contribution；R2 (3.0) 更重视新颖性和统计支持力度，认为与并发工作重叠度过高。综合权衡后取 3.0，因为格式违规、borderline significance 和 epoch confound 三个问题在当前版本中共同将论文定位在 Findings 级别。

---

## Detailed Comments

### §1 Introduction
- 数字密度偏高（6+ 统计量在两段内）。建议保留关键数字（AUROC 0.82, <1pp gap, +1.40pp conditional, 69% inverse scaling），其余移至 Table/Appendix。
- "exploratory extensions to RE and SQL pilots" 已降调，但考虑标注 sample sizes (n=397, n=196)。

### §2 Diagnostic Framework
- Signal taxonomy (Structural / Surface / Model) 清晰，但 "Family" 列标题在 Table 3 中不够直观，建议换为更具描述性的标题。
- "Degeneracy" 首次定义时缺乏术语选择说明。建议简短解释为什么选择此术语。

### §3 How Self-Verification Fails
- Architecture mismatch (Qwen2.5-7B vs Qwen3-8B) 需更显著标注。当前 footnote caveat 不够 visible。
- ESJ binary yes/no prompt 可能过于简化，建议讨论 alternative self-verification prompt designs。

### §4 Where Single-Signal Selection Fails
- 核心 section，correlation-selection gap 的诊断清晰。
- 数字密度问题集中在此（单段 6+ 统计量）。

### §5 Adaptive Methods
- Table 2 (method summary) 是有价值的综合对比。
- Cross-model ensemble 仅 Few-NERD，需补充或降调 claim。
- LightGBM transfer failure 的 feature-level analysis 缺失。

### §6 Threshold Regime Analysis
- Proposition 1 formal proof 建议移至 Appendix，主文保留分解直觉。
- Inverse scaling 69% 的发现重要，但在 Abstract/§1 中的 visibility 不足。
- Degeneracy decomposition 的概念价值（三因子可独立干预）应保留。

### §7 Experiments
- 实验设计全面，但 Few-NERD 3-epoch 结果的 prominence 与 5-epoch collapse 的 visibility 不对称。
- 建议 Table 中并列 3-epoch 和 5-epoch 结果。
- §7.5 entity construction：global p=0.055 需更透明讨论 family partition rationale。

### §8 Related Work
- 密度过高（1 页 6 子主题）。若需压缩至 8 页，此 section 是首选压缩目标。
- 缺失 token-level uncertainty / calibration / self-evaluation 文献。
- 与 Yao et al. (2026) 的 3-dimension differentiation 已改善但在正文仍可加强。

### §9 Discussion and Conclusion
- "When not to scale" 实践指导有价值。
- "Open questions" 部分可移至 Appendix 以节省页面。
- Cost-benefit analysis（N=8 pilot = 12.5% of N=64）是有益补充。

### Limitations
- 覆盖合理（模型家族局限、frontier 不适用、非因果框架）。
- 可补充：single prompt template limitation。

### Ethics Statement
- 合规。使用公开数据集和开源/API 模型，无新 human annotation。
- CoNLL-2003 Reuters corpus 的 NIST agreement 已提及。

### Appendix
- 极为详尽（36 页），实验细节和补充分析全面。
- Appendix ab (epoch confound) 的核心数据应部分上移至主文。