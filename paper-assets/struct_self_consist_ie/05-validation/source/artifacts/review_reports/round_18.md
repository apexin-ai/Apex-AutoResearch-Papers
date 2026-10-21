---
round: 18
overall_score: weak reject
timestamp: 2026-05-18T01:47:52.256672+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 18 审稿报告 — struct_self_consist_ie

**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction
**目标**: EMNLP 2026 Main Conference Long Paper (ARR May 2026)
**截止**: 2026-05-25
**Reviewers**: 2 人 (R1: 方法严谨性/统计分析; R2: 新颖性/写作/完整性)

---

## Summary

本文研究五种 confidence signals 在 LLM-based NER 中的质量估计（QE）与样本选择（selection）表现。核心发现：所有信号都能可靠估计实例质量（ρ 最高 0.42, AUROC 0.82），但无法将 QE 优势转化为 best-of-N 选择增益（13pp oracle headroom 未被利用）。论文诊断出三层失败机制，识别 LP 选择成功的两个必要条件（低 degeneracy + 充足 alignment），在 Few-NERD 上验证正面发现（+1.36pp, p<0.001）。

---

## Strengths

1. **QE 与 selection 的系统性分离**。填补文献中混淆这两个任务的空白，对 test-time compute scaling 社区有方法论价值。[强共识]

2. **实验设计全面且统计严谨**。四数据集 difficulty gradient，两模型族，4B ablation，温度/N/LoRA-rank/epoch 多维消融。Bootstrap CI, TOST, Bonferroni, Fisher combined p, permutation tests 远超同类工作。[强共识]

3. **Two-condition 分析框架优雅**。Degeneracy + alignment 的解耦分析有洞察力，Few-NERD (n=32,565) 提供高统计功效验证（>99% power, CI [+1.18, +1.53]）。[强共识]

4. **诚实报告负面结果**。不过度宣传 LP 效用，清晰界定成功/失败条件。[强共识]

5. **写作质量显著提升**。Em-dash 清零，Discussion 从 14 个子话题压缩至 7 个，术语定义到位，格式完全合规。[强共识]

---

## Weaknesses

### Must-Fix (blocking for Main Conference)

**W1 [Critical] SciERC selection test 统计效力不足，negative result 被 over-stated。** [强共识: R1-W1 + R2 AGREE]
- n=529, 2 seeds, ~55% power for 1pp effect. p=0.29 无法区分 "no effect" vs "underpowered"
- N-scaling (+0.42→+0.91pp at N=8→32) suggests small but real effect
- 三路梯度中间点（18%→weak）依赖此 null 为 genuine
- **Action**: 报告 MDE at 80% power; reframe "fails"→"insufficient evidence below ~1.5pp"; Abstract/Intro 先呈现 Few-NERD positive

**W2 [Critical] Cross-dataset degeneracy gradient: n=3 因果推断过强 + entity-type non-independence。** [强共识: R1-W2/W3 + R2 AGREE]
- 3 dataset-level 数据点 trivially monotonic; datasets confounded on ≥5 dimensions
- Entity-type ρ=-0.881 (p=0.004) 违反 independence (shared model/tokenizer/temp); effective df<6; p 可能高估 5-10x
- **Action**: "establishes"→"is consistent with"; entity-type p 加 non-independence caveat; foreground T-ablation as controlled evidence; cross-dataset 降级为 exploratory

**W3 [Critical] Three-layer gap 中 Layer 1 是 definitional, 接近 tautological。** [强共识: R1 AGREE + R2-W2]
- "Instance-level signals cannot rank by construction" 是定义推论非实验发现
- 与 empirical Layers 2-3 并列计数夸大分析深度
- **Action**: Reframe as methodological premise; Contributions 改为 two empirical mechanisms

**W4 [Critical] 纯诊断性论文缺乏 positive contribution，venue-fit 风险。** [强共识: R2-W1 + R1 AGREE]
- 核心结论 = "现有信号不 work"; supervised verifier baseline (5 scalar features) 是 straw-man
- LP +1.36pp modest; actionable takeaway 有限
- **Action**: Reframe Few-NERD LP as primary practical finding; 提供 practitioners' decision rule; 考虑 lightweight learned verifier

### Should-Fix (important for acceptance)

**W5 [Warning] Few-NERD 3-epoch training confound。** [分歧: R1 Major, R2 部分反驳]
- 3 epochs = early stopping (标准实践); 5-epoch control shows LP still works (+0.62pp)
- 但主文未披露 3-epoch fact; performance-regime confound (greedy F1 0.748 vs 0.777)
- **Action**: Section 4.1 明确披露; foreground 5-epoch still positive

**W6 [Warning] LoRA rank=8 ablation conflates capacity and degeneracy。** [强共识: R1-W5 + R2 AGREE]
- rank=8 同时改变 model capacity; lower ρ≈0.24 可能 = insufficient capacity
- T=1.2 ablation 更 clean (same model, degeneracy 12.5%, ρ=0.225)
- **Action**: T=1.2 为 primary evidence; LoRA-rank 承认 capacity confound

**W7 [Warning] Supervised verifier 结论过度泛化。** [强共识: R1-W6 + R2 AGREE]
- "Bottleneck lies in what signals encode" 仅对 5 个 features 成立
- Hidden states / entity embeddings 有完全不同 capacity
- **Action**: Scope to "these five unsupervised signals"

**W8 [Warning] Abstract 信息密度仍过高。** [部分分歧: R2-W3, R1 部分反驳]
- ~170 words, 8+ 定量值; R1 认为部分数值 IS contribution
- 共识: 保留 4-5 核心数字, 移除中间机制数字

**W9 [Warning] 模型规模 4B-8B 覆盖有限。** [共识: R2-W4 + R1 AGREE]
- 8B degeneracy > 4B, 70B+ 可能更严重; LP alignment 方向不确定
- **Action**: Limitations 增加 scale extrapolation discussion

**W10 [Warning] Instance degeneracy 定义操作性模糊。** [强共识: R1-W7 + R2 AGREE]
- Prose "identical outputs" vs operation "identical F1"; Table diversity (11%) ≠ Table degeneracy (17.8%)
- **Action**: 首次使用时明确 "identical F1" 非 "identical outputs"

---

## Reviewer Consensus [AGREE]

1. Overall 3.0/5 (Findings-level) — 两位 Reviewer 独立达成相同评分
2. 纯诊断性质 + straw-man verifier 限制了 Main Conference 竞争力
3. 统计 claims 需系统性 softening (establishes→consistent with; fails→insufficient evidence)
4. QE/selection 分离的方法论贡献 + Few-NERD 验证是真实有价值的
5. 写作质量和实验设计执行层面达到高标准
6. LoRA-rank confound: T=1.2 应为 primary evidence

## Reviewer Divergence [REBUT]

1. **Abstract 数字密度** (轻微): R2 认为过多 (8+ 数字); R1 认为诊断论文需要数值但同意中间机制数字可移除. 共识: 减至 4-5 个.
2. **Few-NERD epoch confound severity** (中度): R1 视为 Major (performance-regime confound, matched-degeneracy 比较缺失); R2 视为 well-designed control showing the mechanism works (LP still +0.62pp at 5 epochs). 共识: 需主文披露, 但 severity ≤ warning.

---

## Questions for Authors

1. SciERC within-instance ρ(LP,F1)=0.248 vs Few-NERD ρ≈0.5 差异是否由 entity boundary clarity 解释？有无 SciERC per-type alignment 数据？
2. SciERC per-type ρ(degeneracy, LP Δ)=0.14 (p=0.79) 与 cross-dataset 和 within-Few-NERD 的 strong negative correlation 如何 reconcile？
3. Supervised verifier 在 Few-NERD (32K instances) 上训练是否结果不同？
4. Entity-token LP 方差 4× 但选择更差: if higher variance doesn't help, is compression truly the bottleneck, or is it representation-level determinism?

---

## Missing References

- Vijayakumar et al. (2018) "Diverse Beam Search" — 直接关联 degeneracy/diversity
- Shi et al. (2022) MBR for code generation — structured output MBR
- Eisenstein et al. (2023) reward model ensembles — signal limitation
- 4 个 orphan bib entries 需清理: bhattacharyya2026beyond, malinin2021uncertainty, ren2023selfevaluation, zhang2025conformal

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置外部审稿）。

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0 | 3.5 | 3.25 |
| Excitement | 3.5 | 2.5 | 3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Confidence | 4/5 | 4/5 | 4/5 |

**Overall: 3.0/5 — Findings-level (weak reject for Main Conference)**

**置信度**: 4/5 (高)

**一句话**: 方法论严谨的诊断性论文，成功揭示 QE/selection disconnect，但纯诊断性质（无 remedy）、统计 claims 过强（n=3 因果、underpowered null = "fail"、non-independence）、以及 Layer 1 tautological 限制其达到 Main Conference 门槛。适合 Findings track。

**升级路径** (非建议，仅记录 Reviewer 共识):
- 统计 claims 系统性 softening
- Reframe three-layer → methodological premise + two empirical mechanisms
- 补充至少一个 non-trivial positive contribution (learned verifier 或 LP practitioners' rule 的正式化)
- Few-NERD LP +1.36pp reframe 为 primary finding 而非仅诊断证据

---

## Detailed Comments

### Abstract
- 保留 4-5 核心数字 (headroom, +1.36pp, degeneracy range, ρ threshold)
- 移除: ρ up to 0.38, +0.52pp N-scaling, MBR utility ρ=0.52
- "identical outputs" → "identical F1 scores"

### Introduction
- Contribution 2 "three-layer" → methodological premise + two empirical layers
- "establishes" → "is consistent with"
- 先 Few-NERD positive, 再 SciERC inconclusive

### Method
- Instance degeneracy 操作性定义首次出现时明确

### Experiments
- Section 4.1: 明确 Few-NERD = 3 epochs (early stopping)
- Table 3 caption 加粗 "(full-set evaluation)"
- Table 2 EM/VC 无 p 值原因说明

### Discussion
- T=1.2 ablation 作为 alignment condition 的 primary evidence
- LoRA-rank: 承认 capacity confound
- Supervised verifier: scope to "these five features"
- Figure 2: 15% threshold 来源说明

### Limitations
- Scale extrapolation: 70B+ degeneracy 可能更高但 alignment 未知
- SciERC MDE at 80% power

### References
- 清理 4 个 orphan entries
- 补充 diverse decoding / structured MBR 文献