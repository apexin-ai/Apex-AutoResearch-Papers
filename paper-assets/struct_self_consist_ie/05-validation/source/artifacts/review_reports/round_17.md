---
round: 17
overall_score: borderline
timestamp: 2026-05-17T07:27:12.723647+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 17 审稿报告

**论文**: "Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction"
**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计, R2: 新颖性+完整性+写作质量)
**流程**: Round 1 独立审稿 → 交叉分享 → 收敛判断 → 汇总

---

## Summary

本文系统评估了 5 种 confidence signals（4 个 instance-level + 1 个 per-sample LP）在 LLM-based NER 中的质量估计（QE）和 best-of-N 样本选择表现。核心发现是 "correlation-selection gap"：QE 成功（ρ up to 0.38 on SciERC, 0.42 on Few-NERD; AUROC up to 0.82）但 selection 失败，归因于三层机制——instance-level signals by construction 不能排名候选、instance degeneracy (10-58%) 消除 MBR headroom、LP compression (median range 0.041 nats) 限制 per-sample 信号。LP selection 在低 degeneracy regime (Few-NERD, 10%) 显著有效 (+1.36pp, p<0.001)，在高 degeneracy regime 失败。实验覆盖 4 个 NER benchmark、2 个 model families (Qwen3-8B, LLaMA-3.1-8B)、4B ablation，统计方法严谨（bootstrap CI, TOST, Bonferroni）。

---

## Strengths

1. **问题定义有价值**: "Correlation-selection gap" 将 QE 和 selection 明确解耦，指出 prior work 长期混淆的两个任务。Instance-level vs per-sample 的形式化区分简洁且数学正确。[R1 S1, R2 S1 — AGREE]

2. **实验设计系统**: 4 个 NER benchmark 构成 difficulty gradient（WNUT collapse → SciERC medium → Few-NERD low-degeneracy → CoNLL ceiling），角色清晰。两个 model families + 4B/3B ablation + LoRA-rank ablation 排除多种 confound。[R1 S2, R2 S2 — AGREE]

3. **统计严谨性远超平均**: Bootstrap CI (B=10,000)、paired sign tests、TOST equivalence testing、Bonferroni correction、Kendall's W ranking stability。负面结果使用 TOST 避免 "absence of evidence = evidence of absence" 谬误。明确区分 effect size 和 statistical significance。[R1 S3, R2 S3 — AGREE]

4. **三层诊断逻辑递进**: (a) by construction → (b) degeneracy → (c) compression。Supervised verifier baseline 确认 bottleneck 在 feature space（而非 aggregation），free-form ablation 和 entity-token LP 排除替代假说。[R1 S4, R2 S4 — AGREE]

5. **负面结果表达审慎**: 使用 "inversely associated with" 而非 "causes"，"necessary but not sufficient" 限定 claim，Limitations 详尽。[R1 S5]

6. **Appendix 丰富**: FK independence test、SJ normalizer robustness、ε robustness、thinking token impact、OOD analysis 等覆盖大多数潜在反驳。[R1 S6]

7. **引用覆盖充分**: 59 篇引用，覆盖 self-consistency、MBR decoding、uncertainty estimation、best-of-N、diversity collapse 等方向。与 Yao et al. (2026) 的区分清楚。[R2 S5]

---

## Weaknesses

### Critical (Must-Fix)

**W1. Degeneracy-gating 跨数据集因果证据薄弱 (n=3)**
[R1-W1, R2-Q1 — 强共识]
核心 claim "LP selection effectiveness is inversely associated with degeneracy" 仅基于 3 个 dataset-level 数据点（CoNLL 58% → SciERC 21% → Few-NERD 10%），单调排列概率 1/6。Figure 3 pooled correlation (ρ=-0.57, p=0.066, n=11) 混合两个粒度的观测（3 dataset-level + 8 entity-type-level），违反独立性假设。Entity-type-level evidence (n=8, ρ=-0.881, p=0.004) 更有力但共享训练 pipeline。建议：(a) 增加 1-2 个数据集；(b) 不 pool 不同粒度；(c) 控制 entity type frequency 作为 confound。

**W2. LoRA rank=8 ablation 的 "necessary but not sufficient" claim 缺乏关键数据**
[R1-W2/Q1, R2-Q2 — 强共识]
Rank=8 降低 degeneracy (21%→7.2%) 但 LP selection 仍失败，论文据此声称 degeneracy "necessary but not sufficient"。但未报告 rank=8 下 LP 的 median within-instance range 和 tied fraction。如果 rank=8 下 LP compression 更严重（因模型能力下降），则 selection failure 可归因于 compression 加剧而非 degeneracy 不充分。同时 rank=8 降低了 greedy F1 (0.645→0.640)，无法做 clean causal attribution。Few-NERD 10% degeneracy → LP works, rank=8 SciERC 7.2% → LP fails 的矛盾需更好解释。

**W3. Few-NERD 3 epochs vs 其他 5 epochs 训练差异未在主文披露**
[R1-W6, R2 strongly AGREE — 强共识]
主文 Section 4.1 说 "5 epochs" 暗示统一设置，Appendix 才披露 Few-NERD 仅 3 epochs。Under-training 直接降低 model convergence → 降低 degeneracy。Few-NERD 的低 degeneracy (10%) 可能部分源自训练不足而非 dataset intrinsic property。这严重削弱 "degeneracy is dataset-specific" 和跨数据集 degeneracy-gating 的因果论证。需：(a) 主文披露差异；(b) 解释原因；(c) 补充 5-epoch degeneracy 数据。

**W4. 缺乏可操作的 positive contribution**
[R2-W3, R1 AGREE — 强共识]
论文全部 takeaway 是 "closing the gap requires trained verifiers"，但不训练 verifier、不提出新 signal。已测试的 remedy 全部失败（entity-token LP, LP×VC, supervised combination, verbalized confidence）。纯诊断性 negative result 论文需要极强 insight novelty 或可操作性来补偿。Few-NERD LP +1.36pp 是 positive result，但被 framing 为诊断证据而非实用方法。建议：(a) reframe LP 在低 degeneracy regime 的成功为 actionable finding；(b) 提供 degeneracy-based decision rule。

### Should-Fix

**W5. 负面结果缺少 power analysis**
[R1-W3, R2 AGREE]
SciERC (n=529, 2 seeds) 检测 1pp 效应的 power 约 50-60%。p=0.29 无法区分 "真无效果" 和 "检测不到"。Few-NERD (n=32,565) 才是 definitive evidence。建议加 post-hoc power analysis 或明确指出 Few-NERD 是 definitive。

**W6. "Compression is model-intrinsic" 与 RE free-form 结果矛盾但主文未 qualify**
[R1-W4, R2 AGREE]
NER free-form ablation std ratio 0.97 → "model-intrinsic"。但 RE free-form +2.35pp (p=0.025) 直接证明 constraints DO compress LP for RE。Abstract/Introduction 中 "compressed to near-ineffectiveness" 未限定为 NER-specific。

**W7. em-dash (---) 过度使用（约 90 处），AI 写作风格痕迹**
[R2-W4, R1 AGREE]
正文约 35 处，Appendix 约 55 处。平均每段 1-2 个解释性 em-dash。审稿人最敏感的 AI 写作标志。建议正文减至 ≤10 处。

**W8. Abstract 和 Introduction 过度堆砌数字**
[R2-W5, R1 AGREE]
Abstract 约 180 words 含 15+ 个具体数字。实验报告风格而非 story-driven。建议保留 3-4 个最关键数字，其余用定性描述。

**W9. Discussion section 过长 (2+ 页, 14 个 sub-topics)**
[R2-W8, R1 AGREE]
N-scaling, temperature, verbalized confidence, signal combinations 等 ablation 内容适合移入 Appendix。可释放 ~1 page 用于改善 framing 或增加 constructive contribution。

**W10. Supervised verifier baseline feature space 过于受限**
[R2-Q4, R1 AGREE]
5 个 features 中 4 个是 instance-level aggregates，encode 不了 per-sample discriminative information。"Bottleneck lies in the feature space" 仅适用于这 5 个 features，不能泛化。

**W11. 与 Yao et al. (2026) 差异化叙述位置不够显著**
[R2-W6, R1 partial REBUT]
差异化内容存在但在 Introduction 中不够 upfront。R1 认为差异充分，R2 认为应更显著。共识：Introduction 应更前置差异化。

**W12. Selection 实验 seed coverage 有限**
[R1-W5, R2 partial REBUT]
QE 仅 1 seed，selection 仅 2 seeds。Few-NERD 核心结果 (LP +1.36pp) 是 1-seed result。R2 反驳：n=32,565 的 within-seed power 极高。共识：training seed stochasticity 的影响虽合理推断为小（multi-seed stability σ≤0.026），但严格来说未被验证。

### Minor

**M1.** Abstract 中 MBR 缩写未展开 [R2-M2]
**M2.** Table 3 EM/VC 无 p 值未解释（方向为负）[R2-M3]
**M3.** Figure 3 "~15%" degeneracy threshold 缺乏精确定义 [R2-M4]
**M4.** SJ normalizer claim "Δρ<0.01" 应改为 "|Δρ|≤0.009" [R1-W7]
**M5.** Table 3 vs Table 4 greedy F1 不一致（gold-filtered vs full-set），footnote 存在但容易被忽略 [R1-W8]
**M6.** "leverage" 用词 (Appendix L235) [R2-M1]

---

## Reviewer Consensus [AGREE]

1. **实验执行质量高**: 统计方法、ablation 覆盖、负面结果处理均远超平均。[R1 3.5 + R2 4 Soundness]
2. **Degeneracy-gating 因果证据不足**: n=3 datasets, pooled granularity, Few-NERD epoch confound, LoRA rank=8 混淆变量。
3. **缺乏 positive contribution**: 诊断有深度但无可操作方法。多种 remedy 已测试（全 negative），这有价值但降低了 excitement。
4. **写作可改进**: em-dash 过多、数字堆砌、Discussion 过长。
5. **Reproducibility 高**: 模型/数据集公开，超参数详细，承诺 code release。

## Reviewer Divergence [分歧记录]

1. **Overall score**: R1 = Borderline Accept (3.5/5), R2 = Borderline Reject (3.0/5, leaning Findings)
2. **Excitement**: R1 = 3.5, R2 = 2.5
3. **分歧本质**: 纯诊断性论文（strong execution + negative result + diagnostic value）是否满足 EMNLP main conference 门槛。R1 认为 "correlation-selection gap" 概念化 + 三层诊断的系统性 + Few-NERD positive result 足以构成 borderline accept；R2 认为核心发现的 novelty（partially definitional + partially known phenomena）和 actionability 不够 main conference，更适合 Findings。
4. **Degeneracy as trivial correlate**: R2 初始 claim degeneracy = model success 的 trivial correlate；R1 用 Few-NERD (75% F1, 10% degen) 和 4B/8B 对比反驳，证明 degeneracy 不完全是 capability proxy。R2 在交叉中部分接受但维持 deeper point：论文需 disentangle degeneracy 的多个 driver。

---

## Questions (需要作者澄清)

**Q1.** LoRA rank=8 下 LP 的 median within-instance range、tied fraction、pooled within-instance ρ(LP,F1) 是多少？[R1-Q1, R2 AGREE — 关键缺失数据]

**Q2.** Few-NERD 训练为何仅 3 epochs？5 epochs 下的 degeneracy rate 和 LP selection 效果是多少？[R1-Q2, R2 AGREE — 关键 confound]

**Q3.** Within-instance SJ-F1 ρ=0.52 的 distribution 如何？多少比例的 non-degenerate instances 有 ρ<0？[R1-Q4, R2 partial concern]

**Q4.** Entity-type-level degeneracy-LP gain 分析是否控制了 entity type frequency 或 average entity count per sentence 作为 confound？[R1-Q5, R2 AGREE]

**Q5.** Supervised verifier 加入 token-level features（如 per-entity LP 分布统计）能否 close gap？[R2-Q4, R1 AGREE]

**Q6.** Few-NERD 低 degeneracy 是否主要因 8 entity types（vs CoNLL 4 types）导致 output space 更大？如果是，degeneracy 主要是 output space size 函数。[R2-Q1]

---

## Missing References

1. **Byerly & Khashabi (2024)** "Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems" — SC 中 correlated errors 导致失败的分析 [R2-W7; R1 质疑此引用是否存在，需作者核实]
2. **Diverse Beam Search** (Vijayakumar et al., 2016) — diversity-promoting decoding 作为 degeneracy 的潜在缓解 [R2]
3. **CRF-based calibration 经典工作** — structured prediction uncertainty estimation [R2]
4. **Zhang et al. (2024) DeepMind test-time compute scaling** — fine-tuned model diversity collapse 与 test-time compute 关系 [R1; R2 指出 Snell et al. 2025 已覆盖 ICLR 版本]

---

## Overall Assessment

**Score: Borderline (3.25/5)**
**Confidence: 4/5**

这是一篇实验工作量大、统计处理严谨、ablation 覆盖度高的论文。"Correlation-selection gap" 概念对社区有 guidance 价值，三层诊断结构清晰，Few-NERD 的 positive result 证明 LP selection 在低 degeneracy regime 可行。

但论文面临以下核心问题：
1. **因果证据薄弱**：degeneracy-gating 的跨数据集证据仅 n=3 且 Few-NERD 存在 epoch confound，LoRA ablation 有混淆变量
2. **Novelty/actionability 不足**：三层诊断中第一层 (instance-level limitation) 是 definitional，第二层 (degeneracy) 与已知 diversity collapse 有重叠，第三层 (LP compression) 是 specific but limited impact。缺乏可操作的 positive method contribution
3. **写作问题**：em-dash 过多 (~90)、Abstract 数字堆砌、Discussion 过长

**投稿建议**: 介于 Main Conference 和 Findings 之间。如果能在 rebuttal/revision 中：(a) 补充 LoRA rank=8 LP compression 数据，(b) 澄清 Few-NERD epoch confound（最好补 5-epoch 数据），(c) reframe LP 在低 degeneracy regime 的成功为 actionable finding 并提供 decision rule，(d) 大幅减少 em-dash 和 Abstract 数字，可升至 weak accept。否则建议 Findings。

---

## Detailed Comments (逐节)

### Abstract
- 信息密度过高，15+ 数字在 ~180 words 中
- "Correlation-selection gap" 首次出现时需一句释义
- "Compressed to near-ineffectiveness" 未限定 NER-specific
- MBR 缩写未展开

### Introduction
- 叙事线清晰（self-consistency success → NER structural challenge → gap → diagnosis）
- Contribution 2 和 3 有重叠（degeneracy 既是 gap 原因又是 regime boundary）
- 与 Yao et al. 的差异化位置不够 upfront
- Contribution list 中 by-construction limitation 应标注为 conceptual note 而非 empirical finding

### Method (Section 3)
- 形式化清晰正确，5 个 signal 定义完整
- FK adaptation 有 independence test 支撑（Appendix）
- SJ 分母用 max 非标准 Jaccard，footnote 有说明但 naming 可改进

### Experiments (Section 4)
- 数据集选择合理且角色分工清晰
- 训练细节充分（Table 7），但 Few-NERD 3 epochs 需在主文披露
- vLLM 版本号未报告
- Table 3 vs Table 4 evaluation protocol 差异需更显著标注

### Discussion (Section 5)
- 内容丰富但过长，14 个 sub-topics 可压缩
- "Why the gap exists" 是核心，degeneracy + LP compression 分析有力
- Entity-token LP ablation (negative result) 有价值
- Signal combination + supervised verifier 确认 feature space bottleneck
- Practical considerations 实用（N=8 suffices for QE）

### Conclusion
- 过于简短（10 行），未讨论 broader implications
- 建议增加 practical guidance summary

### Limitations
- 全面且诚实
- 建议补充：power analysis limitation、Few-NERD epoch confound

---

## 官方维度打分（ACL ARR Review Form 综合）

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 4/5 | 3.75/5 |
| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5/5 | 3/5 | 3.25/5 |

---

## Issue Tracker 更新摘要 (Round 17)

**新增 issues**: 6 个
- R17-W1 [critical]: LoRA rank=8 LP compression 数据缺失
- R17-W2 [critical]: Few-NERD 3 epochs confound 未在主文披露
- R17-W3 [warning]: em-dash 过度使用 (~90 处)
- R17-W4 [warning]: Discussion 过长
- R17-W5 [warning]: Supervised verifier 结论过度泛化
- R17-M1/M2/M3 [info]: 缩写、p 值、threshold 精度

**跨轮次 recurring issues 仍 open**: R0-C3, R3-W2, R12-N1, R13-W2, R14-W1, R16-N1 等
**跨轮次已解决 issues**: 34 个（Rounds 0-15）