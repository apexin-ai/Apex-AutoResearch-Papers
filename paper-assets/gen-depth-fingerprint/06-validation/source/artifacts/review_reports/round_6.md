---
round: 6
overall_score: borderline
timestamp: 2026-05-17T11:23:52.593639+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 7（Fresh Review）

**论文**: Depth Fingerprinting: Ordinal Generation Depth Estimation in Non-Paraphrastic LLM Text Chains
**目标 venue**: EMNLP 2026 ARR (May cycle), Long Paper
**审稿日期**: 2026-05-17
**Reviewer 编排**: 2 人（R1 方法严谨性+实验设计, R2 新颖性+完整性+写作质量）
**外部审稿**: 已跳过（用户未提交至 paperreview.ai）

---

## Summary

本文定义 ordinal generation depth estimation 任务，将 LLM 生成文本检测从 binary (human vs. machine) 扩展到 3-class (gen-0 / gen-1 / gen-2+)。使用 5 个模型族的 8 个 base 模型 (0.6B-8B) 构建非释义式续写链，提取 7 个已知指标（5 个 NLL 统计量 + TTR + hapax ratio），发现 differential depth response (DDR)：中心趋势特征随深度单调漂移，分布形状特征保持近稳态。XGBoost 集成在 LOGO 评估下达到 3-class F1=0.762, binary F1=0.694。附带 negative finding：depth-aware data curation 不优于 random subsampling。

---

## Strengths

**S1. 新颖且有意义的 task formulation。** Ordinal depth estimation 填补了 binary detection 和 source attribution 之间的空白。3-class schema 有理论支撑（5-class collapse 在 Appendix D 验证）。[R1, R2 共识]

**S2. 全面的泛化性评估。** LOGO (8 generators) + LOFO (5 families) + cross-model chains + cross-domain (Appendix J) + cross-prompt-type (Appendix C) + sampling ablation (Appendix H) 构成完整的泛化性证据链。[R1, R2 共识]

**S3. 严格的 confound 控制框架。** Length confound 通过三种互补分析系统排除 (Δ=-0.046, 约 6% discriminative performance)。Random subsample control 排除了 sample-size effect。[R1, R2 共识]

**S4. 附录质量高。** 12 个附录覆盖数据集统计、长度控制、prompt 泛化、细粒度分类、QLoRA upper bound、LOFO、混淆矩阵、分类器敏感性、文本扰动、跨域泛化、错误分析、下游效用。与正文衔接良好。[R1, R2 共识]

**S5. 诚实的 scope 限定。** Limitations section 坦承 instruction-tuned 退化 (F1→0.338)、高温采样退化 (-6pp at t=1.0)、>8B 未测试。[R1]

**S6. 统计报告规范。** Percentile bootstrap CI, McNemar test, Bonferroni correction, 使用恰当。可复现性高 (4/5)。[R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. [critical] Table 4 baseline 比较超参不公平** [R1 提出, R2 AGREE]

7-feature ensemble 使用 n_estimators=200, max_depth=6，所有 baselines 使用 100/3。论文称 "to avoid overfitting" 但未提供验证证据。2× trees + 2× depth 给予 proposed method 结构性容量优势。更关键的是，4-det+surface ensemble (binary F1=0.707) 在低容量设置下已超过 7-feature ensemble (0.701)，若统一超参 proposed method 可能更劣。

- **修复要求**: 对所有方法做 grid search 或统一超参重跑 Table 4；如坚持 split hyperparams 需附 validation curve 证明 baselines 在 200/6 下确实过拟合。
- **Issue**: R1-W1 (recurrence, status: open)

**N2. [critical] Downstream 实验统计功效严重不足，negative claim 过强** [R1 提出, R2 AGREE]

3 seeds 的 paired permutation test, p=0.25 (minimum achievable p=0.125)。"Depth composition per se does not determine training utility" 是 negative claim，需要 equivalence testing 或充足统计功效才能成立。当前设计无法区分"无效果"和"效果存在但检测不到"。此外，intro.tex 仍将此列为第 3 条 Contribution，与此前 Round 5 "降级为 additional finding" 的 resolution 矛盾。

- **修复要求**: (a) 从 Contributions 列表移除或弱化为 "preliminary evidence"；(b) 增加到 10+ seeds 并做 TOST equivalence test。
- **Issue**: R1-W5 (recurrence, status: open)

### Should-Fix（影响评分但不一票否决）

**W1. [warning] gen-0 sharing 导致 3-class LOGO F1 含义模糊** [R1 提出, R2 AGREE]

所有 generators 共享 gen-0 seeds，LOGO 中 held-out generator 的 gen-0 测试样本在训练集中以相同文本出现。Confusion matrix 显示 gen-0 几乎完美分类，人为拉高 macro F1。Abstract headline (3-class F1=0.762) 受此 inflation。

- **修复要求**: Abstract 中突出 binary F1 (0.694) 作为 primary metric；正文讨论 gen-0 overlap 影响。
- **Issue**: R7-W1

**W2. [warning] DDR 机制解释缺乏形式化，与自身实验证据矛盾** [R1 提出, R2 AGREE 并补充]

Section 5 称 "softmax architecture and fixed sampling parameters constrain distributional shape regardless of input"，但 Appendix H 的 sampling analysis 显示 t=1.0 时 shape features 变得更重要——stationarity 是温度依赖的，而非架构固有性质。entropy_std 处于 drift/stationary 中间地带 (|ρ|=0.17) 也与 binary categorization 矛盾。

- **修复要求**: 弱化为 empirical pattern (在特定温度范围内观测到)，删除 "regardless of input"；讨论 entropy_std 中间状态的含义。
- **Issue**: R7-W2

**W3. [warning] 4-det+surface ensemble 实际优于 proposed method，efficiency justify 未量化** [R1 提出, R2 AGREE]

Table 4 中 4-det+surface (3-class 0.792, binary 0.707) 均高于 7-feature ensemble (0.776, 0.701)，且 baselines 用较低容量超参。论文用 "single-reference approach" 暗示计算效率优势但未给出 inference time、FLOP 或内存占用对比。与 N1 叠加后问题更严重。

- **修复要求**: 报告 inference cost 量化对比；或重新定位 contribution 为 "interpretable features revealing DDR mechanism" 而非 "best performing method"。
- **Issue**: R7-W3

**W4. [warning] Instruction-tuned 模型 depth signal 严重退化，但 framing 仍暗示 practical applicability** [R2 提出, R1 AGREE 但认为可通过 repositioning 解决]

Limitations 报告 instruction-tuned OLMo F1 降至 0.338。Introduction 的 practical motivation ("LLM outputs increasingly enter pretraining corpora") 暗示 real-world 应用，但实验证据仅覆盖 base models。现实中绝大多数 LLM 生成文本来自 instruction-tuned 模型。

- **修复要求**: (a) 弱化 practical framing，明确限定为 base model phenomenon study；或 (b) 增加 2-3 个 instruction-tuned 模型实验并分析 failure mode。
- **Issue**: R7-W5

**W5. [warning] gen-1/gen-2+ 边界混淆率高但正文讨论不足** [R2 提出, R1 AGREE]

Binary F1=0.694 意味着约 30% error rate。Appendix G 显示 gen-2→gen-1 误判率 36.5%。正文仅简略提及，未分析哪些特征对此边界最有区分力，未讨论对 practical application (如 data curation precision) 的影响。

- **修复要求**: Results 或 Discussion 中增加 gen-1/gen-2+ 分离困难分析段落。
- **Issue**: R7-W6

**W6. [warning] 缺少 Ghostbuster baseline** [R2 提出, R1 AGREE]

Ghostbuster (Verma et al., NAACL 2024) 是 feature engineering + trained classifier 范式，与本文方法直接可比。其缺失是 baseline 覆盖的 gap。QLoRA (Appendix E) 已部分覆盖 neural baseline 方向。

- **修复要求**: Table 4 增加 Ghostbuster；Related Work 讨论 RADAR 等排除理由。
- **Issue**: R7-W7

### Minor（不影响接收）

**M1.** Spearman ρ=0.60-0.63 描述为 "strong"，建议改为 "substantial" 或 "consistent monotonic trend"。[R1 提出, R2 部分同意]

**M2.** 3 个 orphan bib entries (energy_ood, mahalanobis_ood, ood_baseline)。self_consuming_mad/qwen3/llama3 author 字段与 OpenAlex 不一致。[R1, R2 共识]

**M3.** Abstract 中 NLL 缩写未展开。Topic drift R²=0.082 回归规格未文档化。[R1 提出, R2 AGREE]

**M4.** 缺少 Ghostbuster 和 ordinal regression survey (Gutierrez et al., 2016) 引用。[R1, R2 共识]

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全达成共识：

1. **Table 4 超参不公平** — proposed method 有 2× 模型容量优势，且 baseline 已在低容量下超越 (Must-Fix)
2. **Downstream 统计功效不足** — 3 seeds 无法支撑 negative claim，Contribution 3 应降级 (Must-Fix)
3. **gen-0 sharing inflates 3-class metric** — 应突出 binary F1 作为 primary metric
4. **DDR 解释需弱化** — Appendix H 反驳了 "regardless of input" claim
5. **Efficiency 未量化** — 4-det+surface 优于 proposed method 但无 cost 对比
6. **gen-1/gen-2+ 混淆** — 30% error rate 需正文讨论
7. **Ghostbuster baseline 缺失** — feature-combination 范式直接可比
8. **Instruction-tuned 退化** — 重要限制但可通过 repositioning 解决

## Reviewer Divergence [REBUT]

**方法新颖性**:
- **R2 (3.0/5)**: 全部 7 特征为已知指标，方法贡献为零，仅 empirical study。DDR 从 model collapse 理论可预见。Critical issue for main conference。
- **R1 (3.5/5)**: Task formulation 本身是方法贡献。DDR 与 model collapse 预测不同（inference-time vs training-time；tail decay 保持 stationary 与 collapse 的 tail shrinkage 相反）。Sufficient for Findings。
- **Director 判断**: R1 的反驳有说服力——DDR 确实与 model collapse 的预测方向不同，task formulation + evaluation framework 构成 Findings 级贡献。但 R2 的核心关切（对 main conference 新颖性不足）也成立。此分歧决定了 Findings vs Conference 的定位。

---

## Questions for Authors

**Q1.** Table 4 中若将所有方法统一使用 200/6 超参（或通过 grid search 各自选最优），各方法 F1 变化如何？

**Q2.** 能否增加 instruction-tuned 模型的实验（即使性能下降）？具体分析：RLHF 是破坏了 DDR pattern 本身，还是仅需要 classifier retrain？

**Q3.** Topic drift R²=0.082 的具体回归设置是什么？因变量是 classification error 还是 feature values？

**Q4.** Cross-domain 实验 (Appendix J) 使用 t=1.0 而主实验用 t=0.7，为什么不统一？

**Q5.** Downstream experiment 在更大规模 (>10k samples) 下是否测试过？

---

## Missing References

1. **Ghostbuster** (Verma et al., NAACL 2024) — feature-combination trained detector [R1, R2 共识]
2. **Ordinal regression survey** (Gutierrez et al., 2016) — task formulation 基础文献 [R1 提出, R2 AGREE]
3. **RADAR** (Hu et al., 2023) — 应在 Related Work 讨论排除理由 [R2 提出]

---

## External Review (Stanford Agentic Reviewer)

**状态**: 已跳过（用户未提交至 paperreview.ai）

---

## Overall Assessment

**Overall Score: borderline (3.25/5)**
- R1: 3.5/5 (Findings-Conference 边界)
- R2: 3.0/5 (Findings)
- **置信度**: 4/5（两位 Reviewer 均熟悉 AI text detection 领域）

**判断依据**:

论文定义了一个有意义的新任务 (ordinal depth estimation)，发现了一个有趣的 empirical pattern (DDR)，实验设计严谨、附录全面。这些是论文的显著优点。

但存在两个 Must-Fix 问题动摇核心 claims：(1) Table 4 的超参不公平可能使 proposed method 与 baselines 的差异消失甚至反转——这是实验诚信问题；(2) Downstream negative claim 缺乏统计功效，且 Contribution 3 与此前 "降级" 的 resolution 不一致。

Should-Fix 问题中，gen-0 sharing 导致 headline metric 含义模糊 (W1)、DDR 解释与自身 Appendix H 矛盾 (W2)、instruction-tuned framing 不匹配 (W4) 共同削弱了论文的整体说服力。

方法新颖性分歧是 Findings vs Conference 定位的核心：task formulation + DDR finding 足够支撑 Findings，但不足以支撑 main conference。

**建议**: 如果 N1 (统一超参重跑) 和 N2 (移除 Contribution 3 或增加 seeds) 能在 revision 中解决，论文达到 **Findings weak accept** 水平。当前状态为 **borderline**。

---

## Issue Tracker 同步

本轮新增/重开 12 个 issues (2 critical, 6 warning, 4 info)。详见 `review_issues.yaml`。

| ID | Summary | Severity | Status |
|----|---------|----------|--------|
| R1-W1 | Table 4 超参不公平 (recurrence) | critical | open |
| R1-W5 | Downstream 统计功效不足 (recurrence) | critical | open |
| R7-W1 | gen-0 sharing inflates 3-class F1 | warning | open |
| R7-W2 | DDR 解释缺形式化+与 Appendix H 矛盾 | warning | open |
| R7-W3 | 4-det+surface 优于 proposed, efficiency 未量化 | warning | open |
| R7-W4 | 方法新颖性分歧 (Findings vs Conference) | warning | open |
| R7-W5 | Instruction-tuned framing 不匹配 | warning | open |
| R7-W6 | gen-1/gen-2+ 混淆率讨论不足 | warning | open |
| R7-W7 | 缺 Ghostbuster baseline | warning | open |
| R7-M1 | ρ 措辞 overclaim | info | open |
| R7-M2 | Orphan bib + author errors | info | open |
| R7-M3 | NLL 未展开 + topic drift 规格缺失 | info | open |
| R7-M4 | Missing references | info | open |