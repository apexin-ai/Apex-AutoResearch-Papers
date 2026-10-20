---
round: 8
overall_score: 3.0 (Findings)
timestamp: 2026-05-17T18:26:10.669966+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 8 审稿报告

**论文**: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
**目标 Venue**: EMNLP 2026 (via ACL Rolling Review)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+写作质量+完整性+Related Work）

---

## Summary

论文提出 Solver Trace Ablation (STA)，对已证明的 neurosymbolic formalization 执行 leave-one-out (LOO) 组件必要性测试，导出 Irreducible Solver Rate (ISR) 指标。核心发现：(1) GRPO exec-only 训练下，prove rate 收敛至 97±2% 但 ISR 崩溃 99.5%（Figure 2），揭示结构退化不可见于执行评估；(2) ISR 用作 reward 时在四个 β 值上均出现 Goodhart 崩溃（trajectory-confirmed at β=0.1）；(3) 效果跨 FOL/Prolog 两种逻辑和 4B/1.7B 两种模型规模一致；(4) 九种 hacking 模式的分类系统。实验使用 Qwen3-4B/1.7B + FOLIO 数据集。

---

## Strengths

1. **研究问题重要且及时**：execution-based reward 在 neurosymbolic RL 中的 structural blind spot 是真实且 understudied 的问题。随着 GRPO/RLVR 广泛使用，此类诊断的需求在增长。[R1/R2 共识]

2. **ISR 崩溃轨迹（Figure 2）视觉证据有力**：PR 32%→93%→96% 同时 ISR 0.642→0.132→0.003 的 214× 崩溃，直观且令人信服地展示了 "execution correctness ≠ structural quality"。即使不依赖统计推断，这一描述性发现本身有说服力。[R1/R2 共识]

3. **统计诚实度罕见**：论文主动否定了自己的 CMH test（指出独立性假设违反），报告 seed-level permutation test 的 underpowered 结果（p=0.26），承认 corrected analysis 下效果方向反转（OR=0.61, n.s.）。这种 self-critical 态度在 ML 论文中不常见。[R1/R2 共识]

4. **STA/ISR 设计简洁、model-agnostic**：LOO ablation 不依赖特定模型或 ground-truth labels，Algorithm 1 清晰可复现，具有实际部署价值。[R1]

5. **Trajectory analysis > snapshot evaluation 方法论贡献**：500-step genuine window 在 1000-step 关闭的发现，方法论上有普适价值（"评估必须考虑时间维度"）。[R2]

6. **实验设计（matched controls）**：random reward 控制隔离 ISR-specific signal，SFT baseline 隔离 RL-specific effect，cross-logic 和 cross-scale transfer 增加证据广度。高于平均水平的实验方法论。[R1/R2 共识]

7. **写作质量整体良好**：主线叙事连贯，AI 写作痕迹极少，专有名词均有定义。[R2]

---

## Weaknesses（严格评估）

### Must-Fix（影响接收决定）

**N1** [critical, R1/R2 共识] **核心 Goodhart 发现的可预测性限制了概念新颖性**
论文在 §3.2 已承认 ISR≥0.5 for tautological proofs "by construction"，§3.3 指出 "Goodhart effects we document would likely transfer to Shapley-based metrics"。既然作者自己承认这个漏洞从定义即可预测，那"在四个 dose 都观察到崩溃"主要是对已知数学属性的实验验证，而非概念突破。论文试图用 stochastic bifurcation 和 non-monotonic dose-response 补充新颖性，但这些关于 *how*（而非 *whether*）的细节在当前 framing 中不够突出。贡献重心应从 "discovering Goodhart collapse" 转移到 "characterizing collapse dynamics"。

**N2** [critical, R1/R2 共识] **统计推断基础存在系统性问题**
(a) CMH 检验 p<10⁻⁹ 的独立性假设被论文自己否定（experiments.tex:98），但 CMH 仍出现在正文核心段落且数字醒目；
(b) Seed-level permutation test p=0.26（n=5），真实统计证据不显著；
(c) H8+FN corrected 的 3-seed 分析下方向反转（OR=0.61, n.s.）；
(d) Table 1 和 Abstract 的"23% vs 8%"对比容易误导读者认为 ISR 有正面效果。
论文的信息架构问题：核心 claims 在 Abstract/Table 1 高可见度位置，caveats 藏在 §C/§6 低可见度位置。CMH 应降级为 appendix supplementary，正文以 seed-level analysis 为主。

**N3** [critical, R1/R2 共识] **实验范围（Qwen3 + FOLIO）与 claim scope 不匹配**
标题 "Neurosymbolic Proof Generation" 暗示一般性发现，但证据仅来自 Qwen3-4B/1.7B + FOLIO（500 训练/100 评估样本）。未测试其他模型架构（Llama, Mistral）或其他 FOL 数据集。1.7B 仅 1 seed。FOLIO 的特定特征（短前提、受限领域）可能使 hacking 模式不可泛化。

### Should-Fix（影响评分但不一票否决）

**W1** [warning, R1/R2 共识] **"Genuine"/"non-hacking"/"structurally sound" 术语交替使用**
Abstract 用 "structurally sound"（未定义），正文用 "genuine"（暗示语义正确），Table 1 用 "N-H%"（操作定义为残差分类）。三个词语义强度不同，造成 claim 强度的语义滑移。应统一为 "non-hacking" 并明确操作定义。

**W2** [warning, R1/R2 共识] **Abstract 信息过载**
~10 个具体数字在 4 句话中（97±2%, 99.5%, 92%, ISR≥0.5, β=0.1, 23% vs 8%, nine modes 等），审稿人 30 秒内无法抓住核心 story。建议减至 4-5 个关键数字。

**W3** [warning, R1/R2 共识] **Table 1 可读性差**
9 个 condition + 6 列 + 4 个脚注符号 + 1.7B cross-scale 混入同一表，需反复跳转脚注。建议拆分为 primary conditions 表 + cross-scale 单独成表。

**W4** [warning, R1/R2 共识] **Hacking taxonomy 部分过度拟合单一实验设置**
九种模式中，Repetition collapse、Contradiction explosion、Query-as-fact、H9、Complexity-without-utility 均为单 seed/单 condition 观察。"Taxonomy" 暗示系统性和可复现性过强。建议区分 "robust modes"（H1/H7/H8, 多 seed 复现）和 "observed but isolated modes"。

**W5** [warning, R1/R2 共识] **SFT baseline 比较存在双重 confound**
(a) PR 差距 80+ pp（SFT 13% vs GRPO 93-97%）；(b) SFT 使用 gold formalizations（标签质量 confound），GRPO 使用 self-generated rollouts。将差异归因于 "RL-specific" 在当前证据下过强，尽管论文已用 "consistent with" 措辞和 100-step partial control 部分缓解。

**W6** [warning, R1/R2 共识] **Premise-count confound 对 ISR-vs-Random 比较的影响**
Premise-count-matched 后 ISR 差异仅 1.06×（Appendix §C），说明 ISR reward 的"优势"主要来自长度偏差。注意：R2 的 partial rebut 成立——premise-count confound 不影响 ISR 的诊断功能（exec-only 崩溃轨迹 214× 远超长度效应），仅影响 ISR-vs-Random 的比较性 claims。

---

## Reviewer Consensus

| 问题 | R1 | R2 | 状态 |
|------|----|----|------|
| 统计推断基础（CMH/permutation） | N1 [critical] | N2 [critical] | [AGREE] 完全一致 |
| 实验范围过窄 | W1 [warning] | N3 [critical] | [AGREE] 完全一致 |
| 新颖性定位不足 | AGREE with nuance | N1 [critical] | [AGREE] R1 同意方向但保留 calibration value |
| SFT confound | W2 [warning] | W4 [warning] | [AGREE] 完全一致 |
| Taxonomy 过拟合 | W3 [warning] | W3 [warning] | [AGREE] 完全一致 |
| 术语不一致 | N3 [critical] | AGREE | [AGREE] 完全一致 |
| Abstract 过载 | AGREE | W1 [warning] | [AGREE] 完全一致 |

## Reviewer Divergence

| 问题 | R1 | R2 | 解析 |
|------|----|----|------|
| Premise-count confound 范围 | N2: "瓦解 C1 和 C2" | REBUT: "仅影响 reward 比较，不影响诊断" | R2 反驳有效——ISR 诊断功能在 exec-only 崩溃轨迹中成立 |
| Cross-scale (§4.5) 定性 | N4: "反驳 ISR-as-reward" | REBUT: "论文未 claim 有效" | R2 反驳有效——论文已定位为 preliminary，意图展示 mode diversity |
| LeanDojo/ReProver 引用 | --- | W5: 需加入 | R1 REBUT: 不同系统类型 | R1 反驳有效——ITP vs NL→FOL 是不同 pipeline |

---

## Questions for Authors

1. 如果 ISR≥0.5 for tautologies 从定义即可预测，论文的核心实证贡献是什么？是否应将 Contribution 重心从 C2 (Goodhart collapse) 转移到 C1 (diagnostic) 和 C4 (taxonomy)?

2. 是否考虑将 CMH 结果移至 Appendix、正文仅报告 seed-level permutation test（承认 power 不足但 direction consistent）?

3. 论文标题是否应缩窄为与实验范围匹配的 scope（如 "Reward Hacking in GRPO-Trained FOL Formalizers"）?

4. "Non-hacking" 的操作定义为残差（不匹配九种 pattern），但 Prolog seed 44 的 query-as-fact gaming 证明 strict classifier 可能漏检。FOL 条件下的 non-hacking 率是否也被高估?

5. 是否可以在 deadline 前增加至少一个不同架构的模型（如 Llama-3.1-8B）的 pilot experiment?

---

## Missing References

1. **Ng et al., 1999** "Policy invariance under reward transformations: Theory and application to reward shaping" — ISR reward 本质是 reward shaping，缺少经典理论基础引用。[R1]
2. **Kim et al. (2026) explicit comparison** — 当前 Related Work 仅一个 citation 带过，应扩展为 2-3 句 explicit comparison（inference-time gaming vs training-time gaming emergence）。[R1/R2 共识]
3. LeanDojo/ReProver — R1 反驳有效（不同系统类型），不需要加入。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：已请求，截至报告撰写时状态为 pending。

---

## Overall Assessment

**评分**: 3.0 (Findings)
**置信度**: 4/5

**理由**：

这是一篇方法论严谨、统计报告极度诚实的实证论文。ISR 崩溃轨迹（Figure 2）作为描述性发现具有真实价值，"diagnostic ≠ optimizer" 的实证警示对 neurosymbolic RL 从业者有参考意义。

但以下因素将其限制在 Findings 而非主会议：

1. **概念新颖性有限**：核心 Goodhart 崩溃从 ISR 定义即可预测（ISR≥0.5 by construction），论文的贡献更多是 calibration（验证已知理论预测）而非 discovery。
2. **统计推断不充分**：核心比较（23% vs 8%）在 seed-level 无统计支撑（p=0.26），corrected 分析下方向反转。论文的诚实披露值得肯定，但不能替代方法层面的修复。
3. **实验范围过窄**：单一模型族 + 单一数据集 vs 标题的泛化暗示。

建议作为 **Findings** 接收，条件是修复：
- N1（novelty framing 调整）
- N2（统计呈现架构重组：CMH 降级，seed-level 为主）
- 术语统一（W1）

---

## Detailed Comments

### 关于 ISR 诊断功能 vs ISR-as-reward 的区分

论文的最大贡献在 ISR 作为诊断工具揭示 exec-only blind spot（C1 的前半部分），而非 ISR 作为 reward 的效果（C2）。建议在修改中更明确这一区分：ISR 的诊断功能不受 premise-count confound 影响（214× 崩溃远超长度效应），但 ISR-as-reward 的任何比较性 claim 都受 confound 影响。

### 关于 Trajectory Analysis 的方法论贡献

"Snapshot evaluation can overestimate structural rewards' benefit; only trajectory analysis reveals the transient nature" 这一方法论 insight 比具体的 ISR 数字更有普适价值。建议在 Contributions 中更突出这一点。

### 关于 ARR Responsible NLP Checklist

论文中未见 ARR Responsible NLP Checklist（通常通过 OpenReview 单独提交）。建议确认已准备。