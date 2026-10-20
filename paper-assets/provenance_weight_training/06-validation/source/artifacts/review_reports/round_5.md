---
round: 5
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-19T14:22:07.349909+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 6 (Fresh Review)

**论文**: "When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in LM Pretraining"
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR)
**投稿类别**: Findings
**Reviewer 编排**: R1（方法严谨性 + 实验设计 + 统计有效性）, R2（新颖性 + 相关工作 + 写作质量 + 格式合规）
**审稿模式**: Fresh（重新审稿，当作初审）

---

## Summary

本文研究 detect-and-reweight 范式在 LLM 预训练中处理合成数据污染的有效性。通过 Qwen3-0.6B continued pretraining 受控实验（132M FineWeb tokens, ρ=0.4, 3 seeds），识别两个评估混淆因子：(1) Detect & Remove 的 PPL 优势完全归因于多 epoch 曝光（epoch-matched 后 Δ=0.006, N=3）；(2) in-distribution PPL 改善不迁移 OOD（OpenWebText +0.06, Wikipedia +0.14），属 distribution matching 而非 quality gain。同时提出 dual-constrained adaptive b* 框架，用 α_eff quality floor 和 ESS stability ceiling 替代 per-model grid search。方法在 ρ=0.2 失效、1.7B 无效果、Llama-3.2-3B 退化。

## Strengths

**S1. Epoch confound 分析是论文最强贡献。** [全票共识]
Epoch-matched 控制实验（Table 1）干净利落地证明 D&R 的 0.360 PPL 优势在等 epoch 条件下缩减至 0.006（N=3）。D&R threshold sensitivity 的 U 形曲线在 epoch-matched 后变为单调递减（Figure 4, Table 6），揭示 U 形最优点完全是多 epoch 假象。这个发现对社区有实质指导价值：后续比较 filtering 与 reweighting 必须控制 content epoch。

**S2. Distribution matching 洞察有独立价值。** [全票共识]
In-distribution PPL 改善在 OOD 上反转的观察是对 contamination-aware reweighting 整体评估方法论的有效警示。论文自承 "in-distribution PPL may be an inadequate metric" 体现了罕见的学术诚实。

**S3. 异常诚实的自我评估。** [全票共识]
Abstract 直接陈述 "method fails at ρ=0.2 and shows no effect at 1.7B"；Limitations 覆盖 6 个维度（self-contamination、scale、contamination range、detector coverage、evaluation、effect size），不回避任何负面结果。

**S4. 数学框架清晰简洁。** [全票共识]
Propositions 1-2 正确（α_eff 单调递增、ESS 单调递减）。Algorithm 1 简洁可复现。Opposing monotonicity 提供良好理论直觉。

**S5. 系统消融设计。** [全票共识]
Table 2 的 5+2 method 比较建立清晰的 ablation hierarchy（Adaptive < Uniform < ESS-only < Random）。τ, n_min, batch size, detector type sensitivity 全面覆盖。

**S6. 可复现性高。** [全票共识: R1 4/5, R2 4/5]
训练超参数、detector 规格（Appendix K）、算法细节完整。代码承诺发布。

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [Must-Fix] 实验规模过窄，标题级 claim 与证据不匹配。** [全票共识: R1-N2, R2-W1]
全部主实验基于单一模型族（Qwen3-0.6B）、单一数据集（FineWeb 132M）、3 seeds。1.7B 仅 2 seeds 且 Δ=-0.01（无效果）。Llama-3.2-3B 作为 trainee 单 seed 退化 Δ=+0.20。标题 "When Does Detect-and-Reweight Work?" 暗示普适性回答，但证据仅覆盖 "Qwen3-0.6B / FineWeb / ρ=0.4 / self-contamination" 这一特定配置。
→ 建议：(a) 补充 1.7B 3-seed 完整实验 + 第二模型族验证，或 (b) 标题/claims 明确限定 scope。

**W2 [Must-Fix] 方法实际价值被自身发现削弱。** [全票共识: R1-N3, R2-W2]
In-distribution PPL 改善 Δ=-0.043（0.6B, ρ=0.4）不迁移 OOD（OWT +0.06, Wiki +0.14, 仅 seed 42），downstream 4/5 tasks 略降（Table 7），论文自承 distribution matching 而非 quality gain。OOD 评估——最重要的负面发现——仅基于单 seed（"checkpoints for other seeds not retained"），证据最弱。实际价值缩减为节省 ~16 GPU-hours grid search（0.6B）。
→ 建议：(a) 补充 3-seed OOD + multi-seed downstream 评估，(b) 或重新定位为 analysis paper 而非 method paper。

**W3 [Must-Fix] Self-contamination 设计限制外部效度。** [全票共识: R1-N2, R2-W3]
Generator = trainee（Qwen3-0.6B）使检测人为偏易（AUC=0.94 with TF-IDF+LR）。真实 web 污染来自多源异构模型。唯一 cross-model 实验（Llama-3.2-3B generator, Appendix M）single-seed、无 PPL、"checkpoints not retained"。Llama Δ=+0.20 退化不仅是 "未验证"，是方法在第二模型族上失败的直接证据。
→ 建议：补充 cross-model 实验（含 PPL + checkpoint 保留），或进一步收窄 scope 至 self-contamination continued pretraining。

**W4 [Must-Fix] 统计声明不一致。** [全票共识: R1-N1, R2-W4]
Abstract 称 adaptive "matches grid-search performance"，但 95% CI [-0.039, 0.101] 包含退化至 +0.10 PPL 的可能。同时，adaptive vs. uniform paired Δ（-0.041, -0.043, -0.045; SD=0.002）的 paired t-test 会高度显著（t≈-37, df=2），但论文声称 "N=3 precludes formal significance testing"。论文同时在 over-claiming（CI 包含退化→"matches"）和 under-claiming（可做的 paired test→"precludes"）之间矛盾。
→ 建议：(1) "matches" 改为 "approaches"；(2) 执行 paired t-test 并注明 df=2 局限。

### Should-Fix

**W5 [Should-Fix] τ=0.8 推荐缺乏充分验证。** [全票共识: R1-W3, R2-W6]
τ sweep（Table 4）基于 single seed ρ=0.4。ρ=0.6 最优偏移至 τ=0.7。τ=0.7 vs τ=0.8 PPL 差仅 0.026，在 seed variance 内。τ 是方法唯一需设置的关键超参——验证不成比例地薄弱。
→ 建议：至少 multi-seed τ sweep at ρ=0.4。

**W6 [Should-Fix] B=4 下 α_eff 仅 5 离散值，连续框架叙事不匹配。** [共识: R1-W4, R2-W5; R1 认为可降至 Minor]
Pearson r=0.706 仅解释 ~50% 方差。Bisection search 在 5 个离散值上退化为查表。连续优化框架（Propositions 1-2）对 B=4 是 over-engineering。论文 Section 3.3 line 74 简短提及但不够显著。B∈{4,8,16} PPL<0.01 差异实际上削弱了连续公式的必要性。
→ 建议：更显著讨论离散化现实；添加 proxy error sensitivity analysis。

**W7 [Should-Fix] 遗漏重要相关工作。** [共识 2/3, 分歧 1/3]
- Katharopoulos & Fleuret (2018) "Not All Samples Are Created Equal" [全票共识]
- Ren et al. (2018) "Learning to Reweight Examples for Robust Deep Learning" [全票共识]
- Chen et al. (2024) "Take the Bull by the Horns" [R2 坚持, R1 认为 LESS 已覆盖; Director 判定：应引用并区分 loss-driven vs provenance-driven]

**W8 [Should-Fix] 1.7B 实验不足。** [全票共识: R1-W2]
仅 2 seeds, 无 grid-best 对比, Δ=-0.01。报告语气过于平淡（"no evidence of either improvement or degradation"），未充分强调对 scalability 的负面含义。
→ 建议：补充第 3 seed 或显著标注为 preliminary observation。

### Minor

**W9 [Minor] D&R epoch-matched LR schedule confound。** [分歧: R1 flag, R2 rebut]
R1 指出 epoch-matched D&R 用 6,103-step schedule 但仅训练 2,533 步。R2 反驳：confound 方向保守（higher LR favors D&R），Table 1 caption 已说明。双方共识定性结论不受影响。

**W10 [Minor] Proposition 2 证明表述不精确。** [全票共识]
"2 Var_{π²}[ln(1-q)]" 不是严格的 π²-weighted variance。非负性结论成立但表述应修正。

**W11 [Minor] Eq. 4 inf+s.t. 混合形式非标准。** [全票共识] 建议改写为 piecewise 显式形式。

**W12 [Minor] ρ 定义时机。** [全票共识] Token-level vs document-level 区分（Section 4 脚注 1）应在 Section 3.1 首次使用 ρ 时说明。

**W13 [Minor] Figure 1 可读性。** [全票共识] 标注过小；"degradation zone" b≥2 的参照基准未明确（以 uniform 为基准）。

**W14 [Minor] Checklist E1 AI 辅助声明。** [分歧: R2 flag, R1 rebut] R2 建议具名 AI 工具；R1 认为当前声明满足 ARR 要求。非阻塞问题。

## Reviewer Consensus

[AGREE — 双方达成共识的关键判断]
1. Epoch confound 分析是论文最强、最新颖的贡献
2. Distribution matching 洞察有价值但非突破性
3. Adaptive b* 方法实际价值薄弱（效果小、不迁移 OOD、不 scale、仅 Qwen3）
4. Self-contamination 是根本限制，需更广实验或更窄声明
5. 统计声明需收紧（"matches"→"approaches"；paired t-test 应做）
6. OOD 评估仅 single seed + checkpoints 未保留 = 实验管理缺失
7. τ=0.8 验证不足
8. 论文诚实的自我评估值得肯定
9. 论文应定位为 analysis paper 而非 method paper

## Reviewer Divergence

[R1: 3.0 (Findings) vs R2: 2.5 (Borderline Findings) — 0.5 档分歧]
- **分歧根源**：R1 赋予 epoch confound 更高的独立分析贡献权重，认为足以支撑 Findings；R2 更侧重方法贡献薄弱和实验规模狭窄的负面影响。
- **R1-W1 (LR schedule confound)**：R1 标记；R2 反驳（保守方向）。双方同意结论不受影响。
- **R2-W7 (Chen et al. 2024)**：R2 坚持引用；R1 认为现有覆盖足够。
- **R2-W10 (Checklist E1)**：R2 标记；R1 反驳（满足要求）。

## Questions for Authors

1. **Paired t-test 为何未做？** Adaptive vs. uniform paired SD=0.002，t≈-37 极度显著。论文声称 "N=3 precludes formal significance testing" 过于保守——paired designs N 小时仍可做。[全票共识]
2. **OOD 评估为何仅 seed 42？Checkpoints 为何未保留？** 这是存储限制还是实验设计疏忽？对于声称分析 distribution matching 的论文，OOD 是核心分析。[全票共识]
3. **Llama Δ=+0.20 归因？** Detector 是否针对 Llama 生成文本重训？如果用 Qwen3 训练的 detector 直接应用于 Llama 文本，退化可能反映 detector domain shift 而非方法失败。[R1 提出, R2 认同]
4. **Reweighting 边际价值是否随规模递减？** 0.6B→1.7B 趋势（Δ: -0.043→-0.01）是否暗示更大模型对合成数据更鲁棒，reweighting 本身不必要？论文未讨论此 implication。[全票共识]
5. **Domain-heterogeneous contamination 行为？** 真实 web 污染是 domain-skewed 的（某些 domain ρ≈0, 某些 ρ≈0.8）。Per-batch adaptive 理论上可处理此变异，但未被验证。[R1 提出]
6. **Grid-best b=0.3 的 3-seed 实验是否为 post-hoc selection 后才跑的？** 如果 full grid 仅在 seed 42 上完成，然后针对 b=0.3 补跑 seed 123/456，则 3-seed mean 存在 selection bias。[R2 提出]

## Missing References

1. **Katharopoulos & Fleuret (2018)** "Not All Samples Are Created Equal: Deep Learning with Importance Sampling" — importance sampling for DNN training, loss-driven vs provenance-driven 对照。[全票共识]
2. **Ren et al. (2018)** "Learning to Reweight Examples for Robust Deep Learning" — meta-learning sample weights, learned vs rule-based 对照。[全票共识]
3. **Chen et al. (2024)** "Take the Bull by the Horns: Hard Sample-Reweighted Continual Training Improves LLM Generalization" (arXiv:2402.14270) — instance-level reweighting for LLM continual pretraining, 直接相关 setting。[R2 坚持, R1 认为 LESS 已覆盖; Director: 应引用并区分]

## External Review (Stanford Agentic Reviewer)

未配置。

## Visual Layout Check（非评分项）

**Status: timeout**（运行 798 秒后超时，无结果返回）。视觉审查 Agent 未能在时限内完成 PDF 渲染和逐页检查。此部分无可用数据。

## Overall Assessment

**Overall Score: 3.0 — Findings**
**Confidence: 4/5**

**ACL ARR 维度评分：**

| 维度 | 分数 | 理由 |
|------|------|------|
| Soundness | 3.5/5 | 数学正确；实验设计周全（epoch-matched controls 出色）；但 N=3 统计效力有限，OOD/1.7B/cross-model 证据薄弱 |
| Excitement | 2.5/5 | Epoch confound 分析对领域有启示但属 incremental；方法实际收益微弱 |
| Reproducibility | 4/5 | 超参数、算法、detector 规格完整；代码待发布 |

**评分理由：**

论文的核心价值在分析贡献而非方法贡献：(1) epoch confound 发现干净地揭示了 D&R 优势的来源，对社区评估方法论有实质指导意义；(2) distribution matching 观察警示 in-distribution PPL 可能是不充分的 contamination mitigation 评估指标。这两个分析发现的组合达到 EMNLP Findings 门槛。

Adaptive b* 方法数学上优雅但实际价值有限：效果量微弱（Δ=-0.043 PPL at 0.6B），不迁移 OOD，1.7B 无效果，Llama 退化，适用范围窄（仅 Qwen3, ρ≥0.4, self-contamination, discriminative detector）。实际操作收益仅为节省 ~16 GPU-hours grid search at 0.6B。

论文诚实的自我批评是显著优点——几乎所有弱点都被主动披露——但实验规模（单一模型族/单一数据集/self-contamination）限制了分析发现和方法的泛化性。

**接收条件**（Must-Fix）：
1. 统计声明对齐：Abstract "matches" → "approaches"；执行 paired t-test 带 df=2 caveat
2. Scope 对齐：标题/claims 与实际证据范围匹配（或补充 1.7B 3-seed + 第二模型族实验）
3. Self-contamination：补充 cross-model 实验（含 PPL + checkpoint 保留），或在 Abstract/Introduction 显著限定 scope
4. OOD 证据加强：3-seed OOD 评估（保留 checkpoints），multi-seed downstream

## Detailed Comments

### Abstract
- "matches grid-search performance" → 改为 "approaches"（CI [-0.039, 0.101] 包含退化）
- 正面：failure modes（ρ=0.2, 1.7B）前置披露
- 正面："N=3, we report effect sizes and directional consistency" 措辞恰当

### Introduction
- Scope caveat（"continued pretraining on moderate-scale corpora with known contamination"）存在但应更突出
- 三条贡献结构清晰、排序合理（epoch confound → distribution matching → adaptive tool）

### Related Work
- 五段结构（model collapse → detection → domain mixing → instance reweighting → theory）系统全面
- 与 Drayson et al. (2025) 三点区分讨论充分
- 需补充 3 篇引用（Katharopoulos 2018, Ren 2018, Chen 2024）

### Method
- Dual-constraint 框架优雅
- B=4 离散化 Section 3.3 line 74 提及但过于简短，与 Propositions/bisection 的连续叙事不匹配
- "Empirically motivated minimum intervention design choice" 定位恰当
- Proposition 2 证明 Var_{π²} 表述需修正

### Experimental Setup
- 规格完整（lr, optimizer, schedule, hardware, precision, seq len）
- 6 方法对比全面
- Self-contamination 限制应在此节讨论，不仅在 Limitations

### Results
- Table 1（epoch-matched）是论文最强 exhibit
- Table 2 建立清晰的 ablation hierarchy
- Section 5.2 OOD/Scale 是关键但证据最弱的部分（single seed OOD, 2-seed 1.7B）
- Detector comparison（3 detectors, single seed）suggestive but inconclusive

### Discussion
- 5 段结构覆盖关键主题
- "Distribution matching, not quality gain" 是重要的自我批评
- "Deployment considerations" 实际且诚实
- 建议增加讨论：reweighting 边际价值可能随模型规模递减

### Conclusion
- 适度谦虚，不过度声明
- "Code and data will be released upon acceptance" 标准

### Limitations
- 异常全面（6 维度）
- 论文自身的 Limitations 比许多 reviewer reports 更详尽

### 格式合规
- ACL review template 正确使用（\usepackage[review]{acl}）
- Double-blind：author = Anonymous, 未检测到身份泄露
- Responsible NLP Research Checklist 存在且实质填写
- Limitations section 在 Conclusion 后、References 前，不计入页数
- 正文 ≤8 页（PDF 确认）