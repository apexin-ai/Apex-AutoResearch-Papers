---
round: 6
review_mode: continue
overall_score: 3.0
timestamp: 2026-05-22T04:26:22.796805+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 6

**论文**: Per-Example Predictive Multiplicity in Hybrid Recurrent Architectures
**目标 Venue**: EMNLP 2026（ARR 统一审稿）
**审稿模式**: Fresh（完整初审）
**Reviewer 编排**: 2 人（R1 方法严谨性/实验设计/统计方法，R2 新颖性/完整性/related work/写作质量）
**交叉分享**: 1 轮，收敛充分

---

## Summary

论文对 hybrid recurrent architectures 中 attention 对 per-example behavior 的影响进行了系统性分析。使用 Wang et al. (2025) 控制 model zoo（3 架构 × 5 attention ratio × 2 scale），在 10 个 benchmark 上评估 aggregate convergence，在 4 个 benchmark 上进行 per-example decomposition。核心发现：(1) per-example predictive multiplicity 呈 task-dependent spectrum（α = 0.14–0.30），(2) 仅 LAMBADA 显示 aggregate convergence（Bonferroni 校正后 p=.100），(3) aggregate convergence 与 per-example divergence 在 attention ratio 维度上 decouple。

---

## Strengths

**S1** 控制良好的实验设计——使用公开 model zoo，所有模型共享训练数据/tokenizer/超参数，仅改变架构和 attention 配置，有效隔离了架构效应。[R1, R2 共识]

**S2** 统计方法透明——诚实报告 Bonferroni 校正后 p=.100 不显著、bootstrap CI 为 "heuristic indicators"、GDN exclusion sensitivity analysis。这种透明性在实证论文中值得肯定。[R1, R2 共识]

**S3** 丰富的 Appendix（17 个附录）——涵盖 sensitivity analysis、cross-scale comparison、attention weight analysis、confidence margin 等，极大增强可重复性。[R1, R2 共识]

**S4** LAMBADA task-specific convergence 是有价值的经验发现——10 个 benchmark 中仅 retrieval task 显示 monotonic convergence，与 Zoology/Based 的 recall 理论框架一致。[R2]

**S5** Per-example 视角的系统性——将 predictive multiplicity 从 seed variation 扩展到 architectural variation，提供了新的分析维度。[R1]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [Critical, R1-N1 + R2 AGREE] **n=5 Spearman 统计效力严重不足**
核心 convergence 分析使用 Spearman ρ 在 5 个 attention ratio 上计算，仅 120 种排列，最小 p ≈ 0.008。LAMBADA raw p=.017，Bonferroni 校正后 p=.100 不满足任何常规显著性阈值。Abstract 和 Introduction 的表述暗示比统计证据实际支撑的更强结论。其余 9 个 benchmark 均未达到显著性。论文三个核心贡献之一（convergence 是 task-specific 且 attention-driven）缺乏充分统计根基。
→ 建议：Abstract/Intro 中用 "descriptive/suggestive/preliminary" 限定 convergence claim；考虑补充 power analysis。

**MF2** [Critical, R1-N2 + R2 AGREE] **单次训练 run 无法区分架构效应与 seed 效应**
所有 30 个配置来自单次 run。论文用 "3× Jaccard gap"（within-arch ~0.33 vs cross-arch ~0.10）作为 proxy evidence，但 R2 指出此比较混淆了 attention ratio variation 与 architecture variation——within-arch Jaccard 比较的是不同 attention ratio，不是不同 seed。D'Amour et al. (2022) 和 McCoy et al. (2020) 已记录同架构不同 seed 产生显著 per-example 差异。Contribution 1 中 "multiplicity is not addressable by seed averaging" 缺乏直接支撑。
→ 建议：至少对一个架构训练 2-3 个 seed baseline；若不可行，须将所有 cross-architecture per-example claim 降级为 "preliminary observations conditioned on single runs"。

**MF3** [Critical, R2-N1; R1 REBUT] **新颖性有限——核心发现是已有概念的直接套用** ⚠️ 存在分歧
R2 认为 decoupling 本质上是 underspecification/predictive multiplicity 文献的自然推论，缺乏新方法/指标/解决方案。R1 反驳称实证贡献超出概念套用——10 benchmark 仅 LAMBADA convergence、Transformer entrainment、decoupling 轨迹均为新经验知识。但 R1 也承认 excitement 上限受限。
→ 建议：深入分析 *why* 只有 LAMBADA 收敛；提出可操作的 per-example multiplicity 缓解策略。

**MF4** [Critical, R2-N2 + R1 AGREE] **缺乏 actionable insights**
Conclusion 称 "per-example evaluation should inform deployment decisions"，但未提供具体方法论指导。实践者读完论文后知道问题存在但不知如何应对。R1 认为对 empirical characterization paper 要求完整解决方案标准偏高，但建议至少增加 2-3 条可操作建议。
→ 建议：提供 practical protocol（何时做 per-example audit、Jaccard 阈值解读、基于 multiplicity 的架构选择准则）。

**MF5** [Critical, R1-N3 + R2-W4 AGREE] **仅 2 个 scale 点不支撑 "scale-dependent" claim**
340M 和 1.3B 两个数据点。Appendix 承认 "binary observation, not a scaling law"，但主文 Conclusion 弱化了此 caveat。
→ 建议：全文统一使用 "differs between 340M and 1.3B"，避免 "scale-dependent"。

### Should-Fix

**SF1** [Warning, R1-W3 + R2 升级] **GDN h3-1 的 16-head confound 削弱 LAMBADA convergence 结论**
排除 GDN 后 LAMBADA ρ 从 −1.0 弱化到 −0.7 (p=.233)，MMLU 从 −0.7 反转到 +0.6。R2 认为应接近 critical。LAMBADA convergence——论文最核心的发现之一——在排除被 confound 的 architecture 后不再显著。当前仅在 Appendix 讨论，应在主文 §4.1 正面讨论。

**SF2** [Warning, R1-W1 + R2 AGREE] **Binary per-example decomposition 丢失连续空间信息**
confidence 0.51→0.49 与 0.99→0.01 的 "hurt" 不可区分。§4.2 的 confidence margin 分析部分弥补但不充分。建议补充 log-probability shift 连续版本分析。

**SF3** [Warning, R2-W1 + R1 AGREE] **"Decoupling" 概念缺乏形式化定义**
核心概念从未给出精确数学定义，仅有自然语言描述。建议给出形式化定义并设定显著性检验标准。

**SF4** [Warning, R2-W3 + R1 部分 AGREE] **遗漏重要相关工作**
- Swayamdipta et al. (2020) "Dataset Cartography"——per-example 分析方法论先驱 [R1, R2 共识]
- Fu et al. (2023) "H3"——最早系统分析 hybrid SSM-attention [R1, R2 共识]
- Cooper et al. (2024) "Arbitrariness and Social Prediction"——per-example variance 的 fairness 影响 [R1, R2 共识]
- Black et al. (2022) "Model Multiplicity"——multiplicity 综述 [R2 提出，R1 需确认具体文献]

**SF5** [Warning, R1-W2 + R2 AGREE] **Bootstrap CI 在 n=3 架构上覆盖率远低于名义值**
论文 §3.5 坦承 "heuristic indicators"，但后续分析仍用这些 CI 支撑 claim。建议更明确提醒读者此局限。

**SF6** [Warning, R2-N3; R1 REBUT 降级] **研究范围过窄但 claim 过于 general** ⚠️ 存在分歧
R2 认为 3 架构/2 scale/1 model zoo 不足以支撑 "hybrid recurrent architectures" 的一般性结论，缺 Mamba-based/SSM-MoE hybrids。R1 反驳称控制实验设计是刻意 tradeoff，加入其他模型会引入训练条件混淆。共识：claim generality 应匹配证据 scope。

### Minor

**m1** Figure 1 panel (b) 趋势线区分度不足；axis labels 和 legend 字号偏小（~正文 60-65%）
**m2** Figure 2 scatter plot axis labels 和数据点标注字号偏小
**m3** Table 1 信息过于密集，建议部分可视化
**m4** Limitations 缺少对 "仅使用 accuracy" 这一限制的讨论
**m5** Abstract 中 "first systematic" 应限定 scope 为 "in the context of hybrid recurrent architectures"

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：
1. n=5 Spearman 统计效力不足（MF1）
2. 单次 run 无法分离 seed 与 architecture 效应（MF2）
3. 2 个 scale 点不支撑 "scale-dependent" claim（MF5）
4. 缺乏 actionable insights（MF4）
5. GDN 16-head confound 应在主文讨论（SF1）
6. Binary decomposition 信息损失（SF2）
7. Decoupling 需形式化定义（SF3）
8. Bootstrap n=3 可靠性问题（SF5）
9. 遗漏重要相关工作（SF4，部分）

## Reviewer Divergence

**分歧 1：新颖性评估（MF3）**
- R2 (3.0): 核心发现是 underspecification/multiplicity 文献的直接推论，无新方法/指标/解决方案，excitement 不足
- R1 (3.5): 实证贡献超出概念套用——LAMBADA-only convergence、Transformer entrainment、decoupling 轨迹均为新经验知识；但同意 excitement 上限受限

**分歧 2：研究范围严重性（SF6）**
- R2: Must-Fix（缺 Mamba-based hybrids、更大 scale）
- R1: Should-Fix（控制实验设计是刻意 tradeoff，扩大范围会引入混淆）

---

## Questions（需要作者澄清）

Q1. 预期 within-architecture seed variance 相对于 cross-architecture variance 的量级？是否有间接证据？[R1, R2]
Q2. LAMBADA monotonic convergence 是否可能源于 task-attention alignment 而非架构属性？[R2]
Q3. GDN 排除后 MMLU ρ 从 −0.7 反转到 +0.6 如何解释？[R1]
Q4. multiplicity spectrum（α）是否与 benchmark sample size 存在 confound？[R2]
Q5. "3× architecture influence" 估计换用 Cohen's κ 是否稳定？[R1]
Q6. 是否考虑过用 token-level log-probability 作为连续指标替代 binary decomposition？[R1]

---

## Missing References

| 工作 | 原因 | 来源 |
|------|------|------|
| Swayamdipta et al. (2020) "Dataset Cartography" | Per-example 分析方法论先驱 | R1+R2 共识 |
| Fu et al. (2023) "H3: Hungry Hungry Hippos" | 最早系统分析 hybrid SSM-attention | R1+R2 共识 |
| Cooper et al. (2024) "Arbitrariness and Social Prediction" | Per-example variance 的 fairness 影响 | R1+R2 共识 |
| Black et al. (2022) "Model Multiplicity" | Multiplicity 综述 | R2 提出 |

---

## External Review

**状态：未请求**（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成（2 warning + 3 info），结果如下：

**⚠️ Warning**
1. **Page 3-4 视觉单调**：连续 2 页纯文本（Related Work + Method §3.1-3.3），无任何 figure/table/display equation 穿插。建议将 model zoo 配置或 task taxonomy 以小型 summary table 呈现，或将 Figure 2 提前。
2. **Display items 偏少**：主正文 8 页仅 4 个 display items（2 figure + 2 table），对实证论文偏少（典型 5-8 个）。大量实验结果以行内数字呈现，降低可读性。建议将 Appendix 核心表格（per-example effect counts 或 normalized Jaccard）提升至主正文。

**ℹ️ Info**
3. Figure 1 axis labels 和 legend 字号偏小（约正文 60-65%），打印版可能需辨认。
4. Figure 2 同样字号偏小。
5. 主正文无 display equation，方法论定义全部以行内公式呈现，建议将 1-2 个核心度量公式提为 display equation。

---

## Overall Assessment

**评分：3.0（Findings）**
**置信度：4/5**

### 评分理由

论文在实验设计控制和统计透明性上达到了较高标准，使用公开 model zoo 的控制变量设计是值得肯定的方法论选择。LAMBADA task-specific convergence 和 per-example multiplicity spectrum 是有价值的经验发现。

但以下问题共同制约了评分：

1. **统计效力不足**（MF1）：核心 convergence claim 的唯一显著 benchmark（LAMBADA）在 Bonferroni 校正后 p=.100 不显著，且排除 GDN confound 后进一步弱化到 p=.233。论文最核心的定量发现缺乏充分的统计根基。

2. **实验设计根本缺陷**（MF2）：单次 run 无法区分架构效应与 seed 效应。这是 predictive multiplicity 研究中的根本性问题——先前文献的核心发现恰恰是不同 seed 产生 per-example 差异。

3. **新颖性受限**（MF3）：虽然 R1 为实证贡献辩护，但 R2 的关切有合理基础——核心概念框架（multiplicity, underspecification, decoupling）均来自先前工作，本文的增量贡献主要是将已有指标应用于新场景，且未提出新方法或解决方案。

4. **缺乏 actionable insights**（MF4）：论文停留在 "问题存在" 的描述层面，未为实践者提供可操作的指导。

综合考虑，论文适合 Findings 接收：实验设计严谨、统计方法透明、经验发现有参考价值，但 novelty 和 impact 不足以支撑主会议。如果作者能提供 multi-seed baseline 数据并弱化 convergence claim 措辞，评分可提升至 3.5 (Borderline Conference)。

---

## Detailed Comments

### Section 1 (Introduction)
- "attention-driven aggregate convergence" 措辞暗示因果关系，但 Bonferroni 后 p=.100 不显著，应使用 "suggestive" 或 "preliminary"
- "first systematic per-example analysis" 应加 scope 限定 "in hybrid recurrent architectures"
- Contribution list 第 1 条 "multiplicity is not addressable by seed averaging" 缺乏直接实验支撑

### Section 3 (Method)
- §3.1 应提及 GDN h3-1 的 16-head 差异（目前仅在 Appendix）
- §3.4 helped/hurt/unchanged 分类首次出现时解释简略，应注明 binary decomposition 的局限性
- §3.5 BCa 技术细节建议移至 Appendix，主文保留结论

### Section 4 (Experiments)
- §4.1 "only LAMBADA exhibits monotonic convergence" 应在主文中补充 GDN exclusion sensitivity
- §4.2 confidence margin 分析部分弥补了 binary decomposition 不足，但建议增加 log-probability shift 连续分析
- §4.3 "decoupling" 概念应给出形式化定义（如 $\text{Corr}(\sigma_t, J_t) \not\neq 0$ 的可检验假设）
- §4.3 "3× architecture influence" 比较的是 within-arch（across attention ratios）vs cross-arch，非 seed vs architecture

### Section 5 (Conclusion)
- "scale-dependent" 应改为 "differs between 340M and 1.3B"
- 建议增加 2-3 条可操作建议（per-example audit protocol、Jaccard 阈值、架构选择准则）

### Related Work
- 应补充 Swayamdipta et al. (2020)、Fu et al. (2023) H3、Cooper et al. (2024)
- 与 Gorbett et al. (2026) cross-model disagreement 的关系可进一步讨论

### Limitations
- 缺少对 "仅使用 accuracy" 这一限制的讨论（loss、perplexity 等连续指标可能揭示不同模式）

### Format
- 正文在 8 页限制以内 ✓
- Limitations 3 段符合 EMNLP 要求 ✓
- Ethics Statement 存在 ✓
- ACL 模板 [review] 模式 ✓
- 匿名提交 ✓