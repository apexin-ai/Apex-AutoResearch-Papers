---
round: 23
review_mode: 
overall_score: borderline
timestamp: 2026-05-19T06:26:58.953659+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 24

**论文**: "Strong Predictors, Weak Selectors: Diagnosing and Resolving Self-Consistency for Named Entity Recognition"
**Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review May cycle)
**Deadline**: 2026-05-25 (AoE)
**Reviewer**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 叙事 + 写作)
**圆桌轮次**: 1 轮（关键问题达成共识，无重大未解决矛盾）

---

## Summary

本文系统评估了 5 种置信度信号在 NER 任务上的质量估计 (QE) 和样本选择效果，使用 fine-tuned 4B-8B 模型在 4 个 NER benchmark 上进行实验。核心发现：所有信号可靠估计实例质量（ρ up to 0.45, AUROC up to 0.82），但 instance-level selection 失败——论文诊断出 instance degeneracy 和 LP compression 两个瓶颈，并提出 entity-level construction 作为部分缓解（+1.40pp Few-NERD, +1.02pp SciERC）。

---

## Strengths

**S1. 统计严谨性在 NLP 论文中属上乘水平。** [共识] 贯穿 paired bootstrap tests, MDE 分析 (SciERC n=529 → MDE≈1.5pp), TOST 等价性检验, Bonferroni/BH 校正, 以及 multi-seed stability 报告。Post-hoc 分析（ε=0.05 → p_adj=0.14）主动标注为 exploratory。

**S2. QE vs Selection 的概念区分是有效贡献。** [共识] Instance-level vs per-sample signal 分类法清晰且对 structured prediction 领域有指导意义。

**S3. 实验覆盖异常全面。** [共识] 5 信号 × 4 NER 数据集（难度梯度：WNUT→SciERC→Few-NERD→CoNLL）× 2 模型家族 × 4B scale ablation × 温度/epoch/N/LoRA-rank 消融 × supervised 组合 × hidden state probes × DeBERTa verifier × verbalized confidence × free-form decoding × calibration baseline × OOD 分析。附录约 1571 行。

**S4. 诚实的负结果呈现。** [共识] 坦率承认 supervised combinations、hidden state probes、DeBERTa verifier 均无法关闭 selection gap。清楚区分 exploratory 与 confirmatory findings。

**S5. 写作质量良好，无 AI 写作痕迹。** [共识] 无 em-dash/en-dash 滥用，无黑名单词汇，术语定义完整，段落长度合理。

**S6. 混淆变量控制充分。** [共识] Thinking token confound (Appendix J: 3-part analysis), epoch confound (Appendix S), SJ normalizer (Table 6: |Δρ|<0.01), FK independence (permutation test), length-LP correlation (正向，排除 length penalty confound) 均有对应分析。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1. [Critical] 分解公式 E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) 验证严重不足。** [R1 critical + R2 agree]
- g(·) 被 "assumed monotonically increasing" 但无理论推导，无函数形式
- 仅用 3 个 macro-level 数据点（SciERC, Few-NERD, CoNLL）验证 "consistency"——任何单调函数都能拟合 3 个点
- Figure 3 中 23 个 configurations 的数据完全可做 predicted vs actual 的回归验证，但论文未做
- **修改方向**: (a) 在 23 configurations 上做回归验证并报告 predicted-actual correlation；或 (b) 删除 "consistent with the observed data" 验证措辞，明确标注为 "descriptive heuristic / illustration"

**W2. [Critical] Gating protocol 循环性 + 验证不足。** [R1 critical + R2 agree]
- Within-instance ρ(LP, F1) 需 gold labels 才能计算，仅为回顾性诊断而非前瞻性预测器
- Dev probe: 仅 50 held-out instances，bootstrap SE 未报告
- Threshold 0.3 来源未说明，敏感性分析缺失
- 仅 3 dataset 验证，inter-dataset margins 大（SciERC 0.167, CoNLL 0.065, Few-NERD 0.516），不清楚 margins 窄时是否可靠
- Gating 在 LP selection 与 construction 间选择但无 "greedy fallback" option——CoNLL construction 有害 (-0.39pp) 时 gating 仍可能路由到 construction
- **修改方向**: 报告 bootstrap CI、讨论 threshold 敏感性、增加 greedy fallback、明确 gating 为 preliminary protocol

### Should-Fix（影响评分但不一票否决）

**W3. [Warning] Entity construction 新颖性有限 + "Resolving" framing 过强。** [R2 critical → R1 agree on substance, disagree on severity]
- 本质是 Florian et al. (2003) entity voting 从 multi-model ensemble 迁移到 single-model stochastic sampling + LP weighting
- LP weighting vs uniform 增量仅 0.28pp (SciERC) 和 0.66pp (Few-NERD)
- 实际恢复 oracle headroom 仅 8-11%（SciERC 1.02/13.0≈8%, Few-NERD 1.40/12.4≈11%）
- Title "Resolving" 和 Contribution 3 "principled resolution" 暗示问题已有效解决
- **R1 rebuttal**: 作为诊断的自然推论可接受，不应作为主要贡献；建议降级 narrative
- **修改方向**: Title "Resolving" → "Addressing"/"Mitigating"；Contribution 3 降级为 "diagnostic-motivated mitigation"；正文加 oracle recovery percentage

**W4. [Warning] Correlation-selection gap 概念：by-construction vs empirical 边界模糊。** [R2 critical → R1 partial rebut]
- 4/5 信号的 selection 失败是信号定义的直接结果（by construction），非 empirical discovery
- **R1 有效 rebuttal**: MBR consensus-proximity 确实给不同 sample 赋不同分数，其失败是 empirical finding；LP 失败和 degeneracy/compression 的机制识别不是同义反复
- **Director 判断**: R1 的分析更有说服力——umbrella term 模糊了 by-construction 与 empirical 边界，但不等于整个概念无价值。降级为 warning
- **修改方向**: 正文更清晰区分 definitional limitation（1 段 setup）与 empirical findings（LP failure, degeneracy-compression disentanglement 作为核心）

**W5. [Warning] SciERC selection 结果 underpowered (n=529, MDE≈1.5pp, σ=0.48pp)。** [共识]
- SciERC LP selection 3-seed mean +0.04±0.48pp，方向 seed-dependent
- 论文说 "Few-NERD provides the definitive test" 但 SciERC 仍是 primary test bed
- **修改方向**: 正文明确标注 SciERC selection 为 "underpowered to detect effects below 1.5pp"

**W6. [Warning] "Tuning-free" threshold 声明不准确。** [共识]
- θ=2/N 是观察所有数据集 sweep 后选择的 "works reasonably well" 值，非先验推导
- **修改方向**: 改为 "default heuristic threshold"

**W7. [Warning] Related Work 缺少与 Taubenfeld (CISC) / Kang (Self-Certainty) 的技术差异对比。** [共识]
- 两者在 RW 仅一句带过 ("reward-free selectors")，未讨论为何不适用于 structured prediction
- Self-Certainty 在 Limitations 列为未测试的 per-sample signal，但 RW 未解释为何不测
- **修改方向**: RW 增加 2-3 句技术差异对比

**W8. [Warning] English-only + NER-heavy 泛化局限未在 Limitations 中讨论语言覆盖。** [共识]

**W9. [Warning] Appendix D "as a reviewer correctly noted" 暗示审稿历史，应删除。** [R1 raises, R2 agrees is minor]

### Minor Issues

- **M1**: Table 2 中 EM/VC 的 p 值标 "---" 应报告具体值
- **M2**: F1 metric 术语不统一 (macro F1 / per-instance macro-F1)
- **M3**: 8 个 orphan bib entries 待清理（Li et al. 2025, Muennighoff et al. 2025 等在 bib 但未 cite）
- **M4**: SJ 分母 max(|g_i|,|g_j|)=0 的边界情况未讨论
- **M5**: Abstract "ρ up to 0.45" 取自 CoNLL EM（最易数据集），SciERC 最高仅 0.379，易给读者过于乐观印象

---

## Reviewer Consensus [AGREE]

1. **实验覆盖和统计透明度是论文最大优势**——在 NLP empirical studies 中属顶尖水平
2. **分解公式验证不足是核心方法论弱点**——3 data points, no regression on 23 configs
3. **Gating protocol 需要更充分验证**——循环性、bootstrap CI、threshold 敏感性
4. **Entity construction 新颖性有限**——直接迁移 + 小增量，narrative 需降调
5. **"Resolving" framing 过强**——实际仅恢复 8-11% oracle headroom
6. **负结果对领域有价值**——系统排除了多种 selection 方法的有效性
7. **写作质量良好**——无 AI 痕迹，统计声明诚实

## Reviewer Divergence [REBUT]

1. **Correlation-selection gap 新颖性**: R2 认为整体 critical（by construction），R1 成功 rebut 指出 MBR conversion 失败和 LP regime 分析是真实 empirical contributions。**Director 采纳 R1 立场：降级为 warning，但需 narrative 重组。**

2. **Scope 限制严重程度**: R2 认为 critical（fine-tuned + constrained decoding specific），R1 rebut 指出 scope 声明清晰且 NER free-form 数据显示 constrained decoding 非根本原因（Table 13 Panel B）。**Director 采纳 R1 立场：scope 声明已足够，fine-tuned + constrained 是主流 deployment paradigm。降级为 existing warning (W8 语言覆盖 + 已有 Limitations 覆盖)。**

3. **Thinking token confound 严重程度**: R1 列为 warning，R2 rebut 认为 3-part analysis 有说服力。**Director 采纳 R2 立场：non-issue，已在 Appendix 充分处理。**

---

## Questions for Authors

Q1. 分解公式能否在 23 configurations (Fig 3) 上做回归验证？Predicted vs actual gain 的 R² 或 Spearman ρ 是多少？

Q2. Gating protocol 的 50 dev instances 是随机采样还是 stratified？Bootstrap 95% CI 是什么？Threshold 从 0.3 移到 0.2 或 0.4，routing 是否改变？

Q3. Entity construction 的 precision-recall trade-off 数据？Construction 是 recall-driven，precision 变化如何？

Q4. Degeneracy rises with capability (8B>4B) 是否因 convergence 差异？有无 matched-convergence scale 对比（如 8B 3-epoch vs 4B 5-epoch）？

Q5. Cross-instance LP ρ (0.220 on Few-NERD) vs within-instance ρ (0.667) 的关系需要更明确解释——为何 cross-instance ρ 不能预测 selection 而 within-instance ρ 可以？

---

## Missing References

- **LLM-Blender** (Jiang et al. 2023): output fusion pipeline 直接相关 [R1 agree, R2 agree]
- **Taubenfeld/Kang 技术差异对比**: 非 missing citation 但 RW 对比不足 [共识]
- **8 orphan bib entries**: 应 cite 或删除 [共识]

---

## External Review

外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**Score: Borderline (3.25/5)**
- R1: 3.5/5 (Borderline accept, 倾向 Findings)
- R2: 3.0/5 (Borderline)
- Director 综合: 3.25/5

**置信度: 4/5**（两位 Reviewer 均熟悉相关领域，交叉后在关键问题上达成共识）

**判断依据**:

论文的**核心优势**在于实验覆盖和统计严谨性——这在 NLP 论文中极为罕见，值得肯定。QE vs selection 的概念区分、degeneracy/compression 的机制诊断、以及诚实的负结果对领域有真实价值。

论文的**核心弱点**在于：(1) 分析框架的数学基础（分解公式 3 点验证、gating 循环性）不够扎实；(2) positive contribution 增量过小（entity construction ~1pp, 恢复 ~10% oracle headroom）且基于已知技术迁移；(3) "Resolving" framing 与实际增益不匹配。

**建议**:
- **Main Conference 接收面临挑战**: 核心新颖性（entity construction）增量不足以支撑 Main Conference 标准。如果能在分解公式上做 23-config 回归验证证明其 predictive power，或增加非 fine-tuned 设置的实验，竞争力会显著提升。
- **Findings 接收可期**: 论文作为 systematic empirical study 有充分价值——诊断框架、全面的负结果、以及统计最佳实践均值得发表。
- **修改优先级**: W1 (分解公式) > W2 (gating) > W3 (construction framing) > W4 (gap narrative) > W5-W9 (presentation)

---

## Detailed Comments (逐 Section)

### Abstract
- 信息密集但准确。"ρ up to 0.45" 取自 CoNLL EM，SciERC 最高仅 0.379——建议加注 dataset context。缺少 oracle recovery percentage，读者无法判断 construction 增益的实际意义。

### Introduction
- 叙事结构清晰：self-consistency → NER structural difference → QE/selection 区分 → gap 诊断 → construction。
- MBR 差异化定位 (L16) 有效。
- Contribution 3 "principled resolution" 需降调。

### Related Work
- 覆盖 4 个主题块，引用密度合理（70 citations）。
- 缺少 Taubenfeld (CISC) / Kang (Self-Certainty) 的技术差异对比——需解释为何不适用于 structured prediction。

### Method (Section 3)
- 5 个信号数学定义严谨。SJ normalizer robustness (Table 6) 和 FK independence (permutation test) 是好的实践。
- SJ 分母 E_∪=∅ 边界情况未讨论。
- Instance-level vs per-sample 区分清晰且重要。

### Experiments (Section 4)
- 数据集选择策略性强（难度梯度 + 各有实验角色）。
- QE 结果可信（structural > LP 在 SciERC 上显著，bootstrap CI 不含 0）。
- Selection 结果：SciERC 无显著差异是可靠 negative result。Few-NERD LP +1.39pp (p<0.001, CI [+1.18, +1.53]) 是最强 positive result。
- 分解公式验证不足（见 W1）。

### Discussion (Section 5)
- 压缩严重但信息密度高。Non-tied subset analysis 的 exploratory 标注正确。
- Entity construction 作为 "resolution" 的 narrative 需降调。

### Conclusion
- 准确，未超出实证支持范围。Practitioner guidance 有价值。

### Limitations
- 异常全面。缺少语言覆盖讨论。

### 格式
- 正文 ≤8 页，`\usepackage[review]{acl}`, `\author{Anonymous}`，double-blind 合规。
- Figure/Table 紧凑高效。
- Responsible NLP Checklist 认真填写。