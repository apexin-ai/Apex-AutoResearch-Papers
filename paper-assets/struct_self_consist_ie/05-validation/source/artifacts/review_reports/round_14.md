---
round: 14
overall_score: borderline
timestamp: 2026-05-16T08:02:12.882972+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 14

**论文**: "Strong Predictors, Weak Selectors: The Correlation-Selection Gap in LLM-Based Named Entity Recognition"
**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**截止日期**: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+相关工作+写作格式）
**审稿轮次**: Round 1 独立初审 → 交叉分享 (完整原文转发 + 逐条 AGREE/REBUT) → 收敛判断：**1 轮收敛**

---

## Summary

本文评估 LLM-based NER 中 5 种置信信号（SJ, VC, FK, EM, LP）在质量估计和 best-of-N 选择上的表现。核心发现 "correlation-selection gap"：信号能预测哪些 instance 做得好（ρ=0.38 on SciERC），但无法选出比 greedy decoding 更好的样本。论文诊断两种失败机制——instance degeneracy（21-58% instances 产生相同 F1）和 LP compression（median within-instance range 0.041 nats），并通过 free-form decoding、entity-token LP isolation、verbalized confidence 三步消融链验证 compression 是 model/task 内在属性。实验覆盖三数据集难度梯度、两个模型族（Qwen3, LLaMA-3.1）、两种规模（4B, 8B）。

---

## Strengths

**S1. 概念贡献有实践价值** [R1-S1, R2 同意]
QE/selection 解耦是本文核心洞察。实践者可能误以为高 ρ 信号能做 best-of-N 选择——本文明确指出这一 fallacy。在 IE 领域尚未被清晰阐述。

**S2. 诊断消融链逻辑严密** [R1-S2, R2 同意]
Free-form decoding (std ratio 0.97, 4 seeds) → entity-token LP (4× variance 但 -2.0pp selection) → verbalized confidence (更压缩) → 每步排除一个 hypothesis 并有量化证据。RE free-form 反向效果恰当标注为 regime-dependent。

**S3. 统计实践远超 NLP 论文平均水平** [R1-S3, R2-Soundness 4/5]
Bootstrap CI (B=10,000)、TOST equivalence testing（含 3 组外部锚定 δ）、Fisher combined p、ε sensitivity sweep、multi-seed Kendall's W、FK independence permutation test。方法论上非常负责。

**S4. 三数据集难度梯度设计精巧** [R1-S4, R2 同意]
SciERC (medium, 65% F1) + CoNLL (ceiling-effect, 91%) + WNUT-17 (collapse, 52% zero-F1)，各自角色明确标注。避免了将 boundary conditions 过度 claim 为 validation。

**S5. Instance degeneracy 量化分析有信息量** [R1-S5, R2 同意]
Table 5 的 degeneracy 统计（constant F1/constant utility/oracle gap closed/within-instance ρ）是本文最有价值的实证贡献之一。MBR 社区讨论 utility degradation，但 "utility IS good (ρ=0.524) yet headroom IS eliminated" 是更精确的诊断。

**S6. 透明度高** [R1-S5, R2-Reproducibility 4/5]
主动提出 confounds（thinking token 三重论证、SJ normalizer robustness、LOO-SJ equivalence、ε sensitivity、external TOST anchors），代码承诺释放。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [CONSENSUS] Contribution #1 framing 混淆 definitional tautology 与 empirical failure**
- R1-N1 提出，R2-W3 独立提出，交叉分享强共识
- 4/5 信号是 instance-level aggregates → 给所有候选分配相同 QE 分数 → 不能直接选择。这是 by construction 的属性，非 empirical finding。论文用 MBR/consensus-proximity 转化为 per-sample ranking 后仍失败才是 empirical finding（within-instance ρ=0.524 但 21% instances 无 headroom）。LP 的 compression 也是独立的 empirical failure。
- 当前 Abstract/Introduction 将 "5 signals all fail at selection" 作为统一 narrative，夸大了 surprise factor。Section 5 (Discussion) 有两层区分但未向前传递至 Abstract/Introduction。
- **此问题已持续 12 轮（R3-W2 → R14），是最核心 framing 障碍。**
- 行动：Abstract/Intro 明确拆分三层——(a) instance-level 信号需 MBR 转换 (acknowledged design property, not surprising), (b) MBR 转换后仍失败 despite positive within-instance ρ (empirical), (c) LP per-sample 但 compressed (empirical)。

**MF2. [CONSENSUS] Selection gap 有效验证仅限 SciERC 单数据集**
- R1-N2 提出，R2 AGREE
- CoNLL oracle headroom 仅 4pp（论文正确标注为 ceiling-effect control），WNUT-17 信号 collapse（capability boundary）。真正验证 selection gap 的 non-trivial setting 仅 SciERC。Table 6 中 LLaMA/SciERC 在同一数据集上用不同模型 replicate 了 gap，增加了模型维度信心，但仍限于单一 difficulty regime。
- Section 4.3 "The pattern holds across CoNLL and WNUT-17" 中 CoNLL 的 "holding" 原因是无 headroom（ceiling effect），非信号失败——qualitatively 不同的原因。
- 行动：增加 medium-difficulty 数据集（如 Few-NERD subset）或进一步软化 generalization claim。Section 4.3 需区分 ceiling-effect holding 与 signal-failure holding。

**MF3. [CONSENSUS] 与 Yao et al. (2026) 增量贡献界定不清**
- R2-N1 提出，R1 AGREE
- Section 1 line 8 用一句话概括差异（"leaving open" 三个问题），但未说明 Yao et al. 使用 hard-prompting 而非 fine-tuned models 这一关键方法论差异。如果 instance degeneracy 是 fine-tuning 产物（高 confidence convergence），则本文最核心的 failure mechanism 不存在于 Yao et al. 的设置中——这恰好构成最强差异化论点，但论文未利用。
- 行动：Related Work 增加对比段落，将 fine-tuning → low diversity → degeneracy 作为与 Yao et al. 的关键区分。

**MF4. [PARTIAL DIVERGENCE → CONSENSUS ON ACTION] Gap 与 MBR 社区已知结论的定位**
- R2-N2 提出（gap 是 MBR 已知现象的重标签化），R1 REBUT（instance degeneracy ≠ utility mismatch：MBR 文献讨论 utility function 不 align with quality，本文中 SJ utility DOES correlate with F1 within instances (ρ=0.524)，失败来自 headroom elimination）
- 分歧点：R2 认为 novelty 有限（2.5/5），R1 认为 degeneracy 是 qualitatively 新机制（3.0/5）
- **实质共识**：Contribution #1 应从 "identifying the gap" 调整为 "diagnosing two specific failure mechanisms (instance degeneracy + LP compression) that explain why QE does not translate to selection in fine-tuned IE models"。需在 Related Work 中明确讨论与 Eikema et al. (2025) MBR utility degradation 的区别。

**MF5. [CONSENSUS] 缺少两篇直接相关文献**
- R2-N3 提出，R1 CONDITIONAL AGREE，Review Director 已验证存在
- (1) **Schall & de Melo (RANLP 2025)** "The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance" — 直接研究 constrained decoding 对 LP distribution 的影响，与 hypothesis (b)(c) 高度相关。本文 free-form ablation 已 empirically 排除 (b)(c) 对 NER 的解释力，引用可强化 "we know this hypothesis and rule it out"。[ACL Anthology 已确认]
- (2) **Yun et al. (Findings EMNLP 2025)** "The Price of Format: Diversity Collapse in LLMs" — format templates → diversity collapse，与 instance degeneracy 话题相关但不同（output-level degeneracy vs token-level diversity）。[ACL Anthology 已确认]
- (3) **Park et al. (NeurIPS 2024)** "Grammar-Aligned Decoding" — constrained decoding 同线，与 Willard & Louf (2023) 互补。[NeurIPS proceedings 已确认]

---

### Should-Fix（影响评分但不阻塞接收）

**SF1. [CONSENSUS] "Moderate-to-strong" QE 措辞有误导性**
- R2-W1 提出，R1 AGREE
- ρ=0.38 (SciERC) 按 Cohen (1988) 属 medium effect。ρ=0.45 来自 CoNLL ceiling-effect control，且该数据集的 ρ 因 zero/non-zero boundary inflate +0.03-0.05 (Section 3.3 footnote)。建议 Abstract 改用 "moderate" 或明确标注 ρ=0.45 来源。

**SF2. [CONSENSUS] 论文定位应明确为 diagnostic study**
- R2-W2 提出，R1 AGREE
- 论文同时尝试 practical guidance (Section 5 "Practical recommendations") 和 mechanism diagnosis，但 actionable takeaway 薄弱（"use VC for QE, trained verifiers for selection"）。明确定位为 diagnostic/analytical study 会使期望对齐。

**SF3. [CONSENSUS] Scale ablation (4B vs 8B) 证据力不足 + 缺少 4B degeneracy 数据**
- R1-W1 提出，R2-W4 同意
- 仅 2 个规模点（同一模型家族 Qwen3），scale 范围极窄（同属 small-model regime）。4B 的 constant F1 fraction、oracle headroom 未报告，无法判断 gap 是 task difficulty 还是 degeneracy pattern 驱动。Abstract "at two model scales (4B and 8B)" 未限定为 narrow range。

**SF4. [CONSENSUS] ε=0.05 threshold non-tied subset 结果定位过强**
- R1-W5 提出，R2 AGREE
- ε sweep 0.01-0.20 gain 单调递增，0.05 非 natural split point。Discussion 将 non-tied subset +2.9pp (p=0.004) 用作 "confirming compression as the bottleneck" 的主要证据，超出 exploratory framing 允许的 claim 强度。Limitations 承认 "post-hoc exploratory choice" 但 Discussion 未体现。Bonferroni over 5 signals ≠ correction over 7ε × 5 signals。

**SF5. [CONSENSUS] Greedy (T=0) 修辞需调整**
- R1-W4 提出，R2 部分 REBUT（practitioner 视角有价值但修辞需改）
- "Surpassing all N=8 selection strategies" 暗示 greedy 是 selection 的公平 competitor。实际上 greedy 和 sampling+selection 解决不同问题。建议定位为 "practical cost-free alternative"。需区分：(a) 只要单输出 → greedy wins, (b) 需要 diverse outputs + QE → sampling 仍有价值。

**SF6. [CONSENSUS] Fisher combined p (2-seed) 呈现权重过高**
- R1-W2 提出，R2 REBUT（核心论证依赖 d=0.038 + bootstrap CI + TOST，非 Fisher）
- 实质共识：Fisher p 呈现权重应降低，bootstrap CI 和 effect size 作为主要推断依据。

**SF7. [CONSENSUS] Kendall's W (n=3) 应定位为 sanity check**
- R1-W3 提出，R2 AGREE
- n=3 下 W=1.0 在 α=0.05 不显著。3-seed 功能是排除 catastrophic seed sensitivity，非统计推断依据。不应在 abstract 中作为 robustness evidence 首行引用。

---

### Minor（不影响接收）

**M1.** [R1-M1, R2 同意] SJ 命名：分母用 max(|g_i|,|g_j|) 而非 union。Footnote 已说明且 Appendix Table 5 证明 Δρ<0.01，但名称可能误导。建议首次使用时加注。

**M2.** [R1-M2] 主表 seed=42 单 seed vs multi-seed mean 选择不一致（Table 1 VC=0.379 vs Table 7 mean=0.386±0.019）。Caption 应更明确说明。

**M3.** [R1-M3] Correlation-selection gap 操作性定义出现在 Section 4.3，但 Abstract/Introduction 已大量使用。建议 Introduction 首次使用时给出 one-sentence 定义。

**M4.** [R1-M4] Table 2 → Discussion non-tied subset 之间缺少 forward pointer。

**M5.** [R1-Q5] Random (0.610) vs Single (0.645) 差距 3.5pp 来源不清。两者期望值应相同（E[F1] under T=1.0），除非定义不同。需澄清。

**M6.** [R2-W5, R1 PARTIALLY AGREE] LP compression hypotheses (b) 与 (d) 区分不够显式。(b)=constrained decoding 强制 schema tokens vs (d)=model 自主赋予高 LP。建议一句话明确 "constraint-imposed vs model-learned" 区别。

**M7.** [R2] "Cost-free greedy decoding" 措辞不精确（greedy 仍需 forward pass）。

---

## Reviewer Consensus

**强共识（两位独立提出或一方提出另一方 AGREE，无 REBUT）：**
- [AGREE] MF1: Framing tautology（R3-W2 延续至 R14，最核心问题）
- [AGREE] MF2: 单数据集 selection 验证
- [AGREE] MF3: Yao et al. 差异化
- [AGREE] MF5: 缺失文献（已验证）
- [AGREE] SF1-SF7: 全部 should-fix 项
- [AGREE] M1-M7: 全部 minor 项

## Reviewer Divergence

**MF4: Gap 与 MBR 社区已知结论的关系**
- R2 立场：gap 在很大程度上是 MBR 社区已知现象（"good metric correlation ≠ good selection"）在 IE 场景下的重新标签化。Eikema et al. (2025) 已发现 MBR utilities degrade on structured outputs。论文贡献应定位为 mechanism diagnosis 而非全新发现。
- R1 立场：Instance degeneracy 是 qualitatively 不同于 utility mismatch 的新机制。MBR 文献中的失败是 utility function 不 align with human quality；本文中 SJ utility DOES capture quality (within-instance ρ=0.524)，但 degeneracy 消除了 headroom。这不是重标签化。
- 评估：两方论点均有道理。R1 的反驳更精确（MBR utility degradation ≠ headroom elimination），但 R2 关于 framing 调整的建议（"diagnosing" 而非 "identifying"）被 R1 接受。**行动方向明确：reframe contribution 定位。**

---

## Questions for Authors（需回答以支撑接收）

**Q1.** [R1-Q1, R2-Q1] Instance degeneracy 是 fine-tuning artifact 还是 task 固有属性？如果 hard-prompted models（如 Yao et al. 设置）也有 high degeneracy，则结论不同。这直接影响 remedy 方向（diversity-promoting training vs. trained verifiers）。

**Q2.** [R1-Q2] Selection 实验为何用 2-seed 而非 3-seed（QE 用了 3-seed）？

**Q3.** [R1-Q3] MBR within-instance ρ=0.524 对 degenerate instances（F1 方差=0）如何处理？excluded or assigned 0？

**Q4.** [R1-Q4, R2-Q4] RE free-form reversal (+1.8pp) 是否限定 "compression is intrinsic" 为 NER-specific？

**Q5.** [R1-Q5] Random (0.610) vs Single (0.645) 3.5pp 差距来源？

**Q6.** [R2-Q2] LP × VC 等简单 signal combination 是否测试过？如果仅需几行代码且未做，需解释 scope limitation 的合理性。

**Q7.** [R2-Q3] Entity-token LP CoNLL 上 variance ≈ 0 — 是否暗示 fine-tuned models 将 entity tokens 视为 deterministic vocabulary？

---

## Missing References

**已验证存在（Must-Add）：**
1. Schall & de Melo (RANLP 2025) "The Hidden Cost of Structure: How Constrained Decoding Affects Language Model Performance" — constrained decoding ↔ LP distribution [ACL Anthology: 2025.ranlp-1.124]
2. Yun et al. (Findings EMNLP 2025) "The Price of Format: Diversity Collapse in LLMs" — format → diversity collapse [ACL Anthology: 2025.findings-emnlp.836]
3. Park et al. (NeurIPS 2024) "Grammar-Aligned Decoding" — constrained decoding [NeurIPS 2024 proceedings]

**R1 建议（非 critical，论文已有 6 篇 MBR 引用）：**
4. Pasad et al. — MBR for seq2seq（MBR-for-MT 线，非必须）
5. Bertsch et al. "It's MBR All the Way Down"（MBR-for-MT 线，非必须）

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**评分：Borderline (2.75/5)**
- R1: 3.0/5 (Borderline), Confidence 4/5
- R2: 2.5/5 (Between Findings and substantial revisions), Confidence 4/5

**评分理由：**

论文实验设计扎实、统计实践优秀、消融链完整——这些方法论品质本身值得认可。Instance degeneracy 的量化分析和 LP compression 诊断链是有价值的实证贡献。

但存在两个核心障碍：

1. **Framing 问题（MF1, 持续 12 轮）**：论文最核心的概念贡献——correlation-selection gap——部分是 definitional tautology（4/5 信号 by construction 不能选择），部分是 empirical finding（MBR 转换失败 + LP compression）。这一区分在 Discussion 中存在但未传递至 Abstract/Introduction。当前 framing 夸大了 surprise factor，使得 informed reviewer 在第一印象上就会质疑 novelty。

2. **Novelty 定位（MF4）**："Good QE ≠ good selection" 在 MBR 社区有先例；本文的增量贡献在于 IE-specific failure mechanisms。如果 reframe 为 "diagnosing two specific failure mechanisms" 而非 "identifying a new gap"，贡献会更准确也更有说服力。

**建议：**
- 如果能在 rebuttal 中 (a) reframe contribution 区分 trivial/non-trivial, (b) 补充 4B degeneracy 数据, (c) 添加缺失文献, 论文适合 **EMNLP 2026 Findings**。
- 对于 Main Conference，单数据集 selection 验证（MF2）和 novelty 定位（MF4）是较大障碍，需额外数据或更强的理论贡献。

**置信度：4/5** — 两位 Reviewer 在 uncertainty estimation、MBR decoding、IE evaluation、统计方法方面均有充分背景。

---

## Issue Tracker 更新摘要

**本轮新增 issues：** 7（R14-N1/N2/W1/W2/W3/M1/M2/M3）
**本轮确认解决：** 4（R11-W7 greedy baseline, R12-M1 four mechanisms, R12-M3 oh2026 year, R13-W1 RE appendix, R13-M1 bib entries）
**持续 open/in_progress：** R0-C3, R3-W2, R7-C2, R11-W1, R11-W2, R11-W3, R11-W6, R12-N1, R12-W1, R12-W2 等
**最长未解决 issue：** R3-W2 (tautology framing, Round 3 → Round 14, 持续 12 轮)