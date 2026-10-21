---
round: 20
overall_score: 3/5 — Findings track acceptance recommended
timestamp: 2026-05-18T13:19:12.375864+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿合并报告 — Round 21

**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction
**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review May 2026)
**Reviewer 编排**: 2 人（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性）
**交叉回应**: R2 对 R1 完成正式 AGREE/REBUT（5 条全部 AGREE）；R1 对 R2 通过 aligned findings 实质覆盖（R1 agent session 在交叉分享请求送达后未重启，但 R1 修订版审稿已显式确认 R2-N3 并在所有关键问题上提出平行发现）
**外部审稿**: 未配置

---

## Summary

本文研究 self-consistency 类 confidence signals 在 LLM-based NER 中 quality estimation（QE）与 sample selection 之间的脱钩现象（correlation-selection gap）。在 4 个 NER benchmark、2 个 8B 模型家族和 1 个 4B ablation 上评估 5 种信号，发现所有信号均可实现可靠的 QE（ρ 达 0.45, AUROC 达 0.82），但仅 LP 在特定条件下（Few-NERD, degeneracy <15%, alignment ρ≈0.5）取得显著 selection 增益（+1.39pp）。论文诊断出两个阻塞机制——instance degeneracy 和 weak LP-quality alignment，提出"两条件"框架。Hidden state probes 证明即使模型内部表示包含更丰富信息，selection gap 依然存在。

---

## Strengths（两位 Reviewer 共识）

**S1** [概念框架] Per-sample vs. instance-level signal 的区分（Section 3.1）是论文最有洞察力的贡献。4/5 信号是 instance-level aggregates，对 selection 无信息量 by construction。这个 observation 直接解释了为什么高 ρ 不能转化为 selection。（R1 + R2 共识）

**S2** [实验系统性] 4 个数据集构成清晰的难度梯度（WNUT-17 signal-collapse → SciERC medium → Few-NERD low-degeneracy → CoNLL ceiling），每个服务于明确的实验功能。多种 ablation（temperature, LoRA rank, epoch, N-scaling, free-form decoding, hidden state probes, DeBERTa verifier, supervised combination）系统地排除 alternative explanations。（R1 + R2 共识）

**S3** [统计严谨性] Bootstrap CI（B=10,000）、TOST equivalence testing（含 external anchors）、MDE 计算、Bonferroni correction、sign test、Cohen's d。统计方法论在 ACL 投稿中属上乘，远超同类工作常见的"report p-value only"标准。Non-tied subset positive finding（+2.9pp, p=0.004）经 Bonferroni 校正后仍 significant。（R1 + R2 共识）

**S4** [Hidden state probe] Section 4.5 直接测试"需要更强信号"这一 natural follow-up。MLP probe ρ=0.388（比 LP 高 37%）但 selection 反而更差，有力封堵了"bottleneck 在 information loss"的 alternative explanation。（R2；R1 在主要优势中列出 LP compression 诊断分析为最有洞察力的贡献）

**S5** [Limitations 透明度] 主动报告所有已知弱点：SciERC seed sensitivity、epoch confound、scale gap、未测试的 per-sample signals、ε threshold 的 post-hoc 性质。透明度超过大多数投稿论文。（R1 + R2 共识）

**S6** [引用完整] 64 bib entries, 97 citations, 0 orphan, 0 missing, 无虚假引用。与最相关工作 Nédellec et al. (2026) 的定位精准。（R1 + R2 共识）

---

## Weaknesses

### Critical（需解决才能接收）

**C1** [页数超限 — desk-reject 级别] 正文约 9.5 页，超出 ACL 长文 ≤8 页限制（不含 Limitations/Ethics/References）。Discussion 是主要来源（6 个 \paragraph 子节）；Conclusion 从 page 9 开始并延伸至 page 10。
- **R1-N1 + R2-W1 共识**，无分歧。
- 建议：DALS 段落完整移至 appendix；LP compression 4 mechanisms 缩为 1-2 句 refer appendix；regime boundaries 段压缩为 3 句；Contribution list 数值细节精简。

**C2** [Title scope 过宽] Title 声称 "Structured Information Extraction"，但实验覆盖仅 NER（4 benchmarks，完整主线）+ RE（SciERC 单 benchmark，明确标为 "exploratory single-benchmark analysis"）。无 event extraction、slot filling 或其他 IE 子任务。
- **R1-W5 + R2-W2 共识**（此问题自 Round 1 起持续 open，Round 19 已推荐 Option B 改为 NER-specific，Round 21 两位 Reviewer 再次确认）。
- 建议方案 (a)（两位 Reviewer 一致推荐）：改 title 为 "...LLM-Based Named Entity Recognition" 或 "...Structured Output Selection"。

**C3** ["两条件"框架经验基础不足] 跨数据集仅 3 个数据点（CoNLL/SciERC/Few-NERD），论文自标 "exploratory given 5+ confounds"。15% degeneracy 阈值来自 Few-NERD per-entity-type 两个相邻点（Person 13.4% vs Art 19.8%），ρ≥0.3 阈值 data-dependent。
- **R1-N2 + R2-W4（partial）共识**。R2 从 novelty 角度指出同一 root issue：claim strength > evidence strength + novelty。
- 建议：降级 claim 为 "empirical pattern" / "approximate boundary in our data"，使用 "jointly observed" 而非暗示 theoretical thresholds；或增加数据集验证。

### Warning（影响评分但不一票否决）

**W1** [Epoch confound 正文处理不充分] 5-epoch Few-NERD LP gain 减半至 +0.62pp，接近 SciERC +0.61pp。框架区分力在统一 epoch 后减弱。当前仅 footnote + appendix 提及。Discussion 中 "Standard early stopping naturally selects the low-degeneracy regime" 是合理 counter-argument 但不够 prominent。
- R1-W1 提出 + R2 交叉回应 AGREE with nuance（within-instance alignment 差异 ρ≈0.5 vs ≈0.24 仍是关键区分因素）。
- 建议：正文正式呈现 epoch-controlled comparison，提升 alignment 差异的叙事地位。

**W2** [SciERC 系统性 underpowered] SciERC n=529, MDE≈1.5pp at 80% power。LP +0.61pp (p=0.193) 无法区分"真的没有效果"和"效果太小检测不到"。3-seed mean +0.04±0.48pp 本质是 noise。Few-NERD（n=32,565, MDE≈0.22pp）有 definitive power。
- **R1-W3 + R2-W5 共识**。
- 建议：将 Few-NERD 重新定位为 primary test bed；SciERC 标注为 "medium-difficulty, underpowered exploratory test bed"。

**W3** [DALS 定位 + data-snooping] (a) DALS 在 Discussion 中引入但无独立评估，与论文诊断性定位冲突。结果 seed-sensitive（SciERC: +0.19 to +1.14pp），CoNLL 仍 degradation。(b) ε=0.05 threshold 从 non-tied analysis 同数据 sweep 选出后在同一数据上评估，存在 circular optimization 风险。
- R2-W3 (positioning) + R1-W4 (data-snooping) 互补。R2 交叉回应 AGREE with refinement。
- 建议：DALS 移至 appendix 作为 exploratory extension；同时报告 held-out validation 或 leave-one-out 的 ε sensitivity。

**W4** [新颖性增量定位] 核心贡献是对已知 general phenomena 在 NER domain 的系统验证和命名。Correlation-selection gap 在 MBR 文献中是已知问题（Eikema et al. 2025 utility misalignment）；instance degeneracy 在 Kirk et al. (2024) 和 Yun et al. (2025) 已讨论 diversity collapse；capability trap 基于 3 scale points 的 observational trend。
- R2-W4 提出。
- EMNLP 接受 negative/diagnostic results 的前提是 (i) robustness 充分（满足）和 (ii) actionable insight 有意义（部分满足）。
- 建议：Introduction 更明确框定为 "first systematic empirical characterization of..."。

**W5** [LP ρ 跨表不一致] SciERC LP ρ 在 Table 1（0.205）和 Table 3（0.215）之间有 0.010 差异，两表标注相同 seed=42, N=8, gold-filtered。与 greedy F1 四值问题（W7）的累积效应影响数据信任。
- R1-W2 独立发现。
- 建议：排查根因并统一数值。

**W6** [Table 3 脚注过载] 7 个连续 `\footnotetext`，混合定义性信息（degeneracy 定义）、评估细节（oracle headroom）、confound 声明（epoch difference）和 per-dataset seed details。
- R2-W6 独立发现。
- 建议：degeneracy 定义移至首次使用处；per-dataset seed details 整合为 appendix table。目标 ≤2 个脚注。

**W7** [Greedy F1 多表数值不一致] SciERC greedy F1 在多个 tables 出现 0.640/0.644/0.645/0.650 四个值。每个差异有脚注解释，但审稿人看到同一 baseline 有 4 个数值会产生困惑。
- **R1 新发现 + R2-W7 共识**。
- 建议：统一 evaluation protocol，或在 Section 3.3 提前声明 protocol variants 及原因。

**W8** [缺失引用] (1) Farquhar et al. (Nature 2024) semantic entropy——与已引 Kuhn et al. (2023) 相关但不同，高影响力工作；(2) Chen et al. (2021) pass@k——best-of-N 在 code generation 的经典成功案例，可更好 contextualize NER selection failure；(3) 缺少 2023+ LLM-based NER calibration/confidence 中间层文献。
- R2 独立发现。

### Info（建议修改但不影响评分）

**I1** [Appendix 残留实验标识] exp\_025, exp\_027 应在投稿前删除。

**I2** ["Capability trap" 措辞] 论文自己展示 temperature 和 early stopping 可部分控制 degeneracy，与 "trap" 暗示的不可逃脱性矛盾。建议改为 "capability-diversity tension"。
- R1-W3 + R2-W9 共识。

**I3** [少量 -ing 短语] 3 处（experiments.tex:183, discussion.tex:20, introduction.tex:18），均在可接受范围但建议改写。

---

## Questions（合并去重）

**Q1** [Epoch × dataset interaction] 能否提供 3-epoch SciERC 的 within-instance alignment ρ 和 LP selection 的 3-seed mean？这将判断 epoch confound 在多大程度上解释 SciERC-vs-Few-NERD 差异。（R2-Q1）

**Q2** [Hidden state pooling] Hidden state probe 使用 mean-pooled final-layer hidden state。是否尝试过 entity-position-only pooling 或 attention-weighted pooling？（R2-Q2）

**Q3** [Per-entity-type effective df] Per-entity-type analysis within Few-NERD（ρ=-0.881, p=0.004, n=8）的 effective df 问题：如果 effective df 为 4，p-value 会升至多少？（R2-Q3）

**Q4** [未测试的 per-sample signals] LP 是当前唯一的 per-sample signal 且唯一有正面 selection 结果。为什么没有测试 Self-Certainty (Kang et al. 2025) 和 P(True) (Kadavath et al. 2022)？如果它们 also fail，加强 "gap is fundamental" 论证；如果 succeed，则 gap 是 LP-specific。（R2-Q4）

**Q5** [DALS τ validation] DALS 的 τ=0.05 如果用 leave-one-out 或 held-out validation 来选择，gain 是否 substantially change？（R2-Q5）

---

## Overall Assessment

### 评分汇总

| 维度 | R1 | R2 | 合并 |
|------|-----|-----|------|
| Overall | 3/5 (Findings) | 3/5 (Findings) | **3/5 (Findings track)** |
| Soundness | 3/5 | 3.5/5 | 3.25/5 |
| Excitement | 3/5 | 2.5/5 | 2.75/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

### 合并判断

**Overall: 3/5 — Findings track acceptance recommended（附条件）**

这是一篇实验严谨、统计透明的诊断性研究。Per-sample vs instance-level 的概念区分有真实贡献，hidden state probe 封堵 alternative explanation 巧妙，统计方法论显著高于同类工作。

**接收的 hard blockers（必须解决）：**
1. 正文超页限（~9.5 vs 8 页）—— desk-reject 级别
2. Title scope 过宽 —— overclaiming 级别

**影响评分的 substantive concerns：**
3. "两条件"框架 claim strength > evidence strength（3 数据点 + data-dependent thresholds）
4. Headline positive result 受 epoch confound 影响，正文处理不充分
5. SciERC 作为 primary test bed 系统性 underpowered
6. 新颖性增量有限（对已知现象的 domain-specific 系统验证和命名）

**如果 (1)-(2) 解决、(3)-(6) 适当调整，论文适合 Findings track。进入 Main Conference 需要：(a) 更多数据集验证"两条件"框架，或 (b) 更多 per-sample signals 扩展 selection 分析。**

### 交叉回应收敛状态

- R2 → R1：5 条正式回应，全部 [AGREE]（N1 框架证据薄、N2 epoch confound、W1 SciERC underpowered、W2 DALS data-snooping、W3 capability trap）
- R1 → R2：通过 aligned findings 实质覆盖（W5 确认 R2-N3 title scope；平行发现覆盖页数超限、SciERC underpowered、DALS、greedy F1 不一致）
- **无未解决分歧**。所有关键问题两位 Reviewer 一致。

---

## AI 写作痕迹检查

- Em-dash（—）：全文零使用 ✓
- En-dash（–）：仅数字范围，正确用法 ✓
- -ing 结尾短语：3 处，可接受范围 ⚠
- 过度分段：无 ✓
- 黑名单用词：无 ✓
- "Furthermore/Moreover/Additionally"：零使用 ✓
- **整体判断**：写作质量高，AI 痕迹控制得当。

## 格式合规性

- `\documentclass[11pt]{article}` + `\usepackage[review]{acl}` ✓
- `\author{Anonymous}` ✓
- 行号：review option 自动生成 ✓
- Limitations section：存在 ✓
- Ethics Statement：存在 ✓
- **正文超限：~9.5 页** ✗ （C1）
- Appendix 内部标识 ✗ （I1）

## References 完整性

- 64 bib entries, 97 citations, 0 orphan, 0 missing
- 3 online not found（近期 preprint 未被索引）
- 4 mismatch（author name 格式差异，非虚假引用）
- **无虚假引用** ✓

---

*报告由 Review Director 基于 Reviewer 1（方法严谨性 + 实验设计）和 Reviewer 2（新颖性 + 完整性）的圆桌审稿合成。*