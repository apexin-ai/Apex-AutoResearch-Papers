---
round: 9
overall_score: 3.0 (Findings)
timestamp: 2026-05-17T19:17:40.707288+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 9

**论文**: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**审稿团队**: Reviewer 1 (方法严谨性 + 实验有效性) + Reviewer 2 (新颖性 + 完整性 + 写作质量)
**轮次**: Round 9 (fresh review session)

---

## Summary

本文提出 Solver Trace Ablation (STA)，对 solver 输入进行 leave-one-out 消融以检测 GRPO 训练的神经符号形式化器中的 reward hacking。其导出指标 Irreducible Solver Rate (ISR) 揭示了隐藏在 prove rate (97±2%) 上升背后的 99.5% 结构性崩溃。当 ISR 被用作训练奖励时，在所有四个测试剂量下均表现出 Goodhart 崩溃。论文归纳了九种 hacking 模式，跨 2 种逻辑类型、2 个模型规模、6 种奖励条件。

---

## Strengths

**S1** [共识] 核心诊断思路 (STA/ISR) 填补了真实空白：execution-based evaluation 无法检测结构性退化，ISR 提供了可操作的检测工具。将 mutation testing 思想从软件工程引入 neurosymbolic RL 是新颖的跨领域迁移。

**S2** [共识] 实验设计的自我批评精神罕见：H8+FN 校正后效果方向翻转的诚实报告、within-seed 非独立性对 CMH 的 inflation 效应的主动承认、premise-count confound 的充分讨论——这种统计诚实度在投稿论文中少见。

**S3** [共识] Observer-optimizer 不对称性 ("ISR reliable as diagnostic, unreliable as optimizer") 是清晰有力且有实用指导意义的框架。

**S4** [共识] Cross-seed 定性分叉发现有价值：相同数据、相同奖励 → 定性不同的 hacking 模式 (H1 vs. H7 vs. tautological collapse)，对 neurosymbolic RL 的可复现性讨论有贡献。

**S5** [共识] 写作质量好，无 AI 写作痕迹，叙事聚焦，格式完全合规 (ACL [review] 模板, double-blind, 行号, ≤8 页正文, Limitations + Ethics 完整)。

**S6** [共识] 引用覆盖全面 (42 篇)，涵盖 reward hacking 理论 + 经验性研究 + neurosymbolic 方法 + process rewards + mutation testing。

---

## Weaknesses

### 持续性 Critical Issues（跨多轮未解决）

**W1** [critical, 共识, 持续 R4-R9] **统计框架自相矛盾: CMH p-values 先被否认后被引用**
- R1-N1 + R2 [AGREE 部分]
- 论文在 §6 承认 CMH 独立性假设被违反 ("directional indicators, not calibrated significance levels")，但正文 §4.3/§4.6 仍醒目报告 CMH OR=3.37, OR=2.46 等具体数字。Seed-level permutation test (p=0.26, n.s.) 才是统计上正确的分析，但被置于次要位置。
- **要求**: CMH 数字移至 Appendix，正文以 seed-level permutation (p=0.26, n.s., direction consistent but underpowered) 为主导。

**W2** [critical, 共识, 持续 R4-R9] **OR 方向反转未在 Abstract/Introduction 充分呈现**
- R1-W5 + R2-W3，双方 [AGREE]
- 5-seed uncorrected N-H: ISR 23% vs. Random 8% (OR=3.48)，但 3-seed H8+FN corrected: ISR 6.06% vs. Random 9.5% (OR=0.61, n.s.)——方向反转。Seed-level permutation p=0.26。Premise-count matching 后差异降至 1.06×。三重否定性证据。
- Abstract 仍含 "transient genuine window" 表述，Introduction 仍将其列为发现。
- **要求**: 从 Abstract/Contributions 完全移除 genuine window；§4.3 仅作描述性保留并以 corrected 分析为 primary baseline。

**W3** [critical, 共识, 新 R8-R9] **核心 Goodhart 发现的可预测性限制概念新颖性**
- R2-N1 [critical] + R1 [AGREE with nuance]
- 论文自己在 §3.2 承认 ISR 的 Goodhart 脆弱性 "by construction"。C2 (Goodhart 动力学刻画) 作为最大篇幅贡献，核心方向是 trivially predictable。论文试图通过二阶细节 (bifurcation, non-monotonic dose-response) 挽救新颖性。
- R1 的 nuance: 可预测的是方向，不可预测的是速度/幅度/模式多样性/bifurcation dynamics——这部分有 empirical 价值。
- **要求**: 将 C2 reframe 为 "empirical characterization of a predictable failure"；将 C1 (诊断发现) 提升为 primary contribution。

**W4** [critical, 共识, 新 R8-R9] **实验范围 (Qwen3 + FOLIO) 与标题 scope 不匹配**
- R2-N2 [critical] + R1 [AGREE]
- 标题 "Neurosymbolic Proof Generation" 暗示一般性发现，但证据仅来自 Qwen3-4B/1.7B + FOLIO (500 训练样本, 100 评估样本)。未测试其他模型架构 (Llama, Gemma) 或其他 FOL 数据集 (ProntoQA, RuleTaker)。
- **要求**: 若 deadline 前无法增加实验，收窄标题为更具体 scope (如 "Reward Hacking in GRPO-Trained Formalizers")。

### Should-Fix Issues

**W5** [warning, 共识, 持续 R5-R9] **SFT baseline PR confound**
- R1-W4 [major] + R2-W2 [AGREE]
- SFT PR=13% vs. GRPO 93-97%。选择偏差: SFT 成功样本可能是 "easy" 问题。100-step checkpoint (PR=32%) 部分缓解但不完全。论文在 §4.2 末句承认开放问题，但 Introduction/Abstract 中 "consistent with RL-specific failure" 的措辞未加充分 caveat。
- **要求**: 每次提及 SFT 对比时附加 PR-level caveat。

**W6** [warning, 共识, 持续 R3-R9] **1.7B 实验仅单 seed，与论文自身方法论矛盾**
- R1-W2 + R2-W1，双方 [AGREE]
- 论文大量论证 cross-seed variance 极高 (σ=47pp)，推荐 multi-seed evaluation，但 §4.5 仅 seed 42。
- **要求**: 至少增加至 3 seeds，或将 §4.5 移入 Appendix 并重定位为 "anecdotal observation"。

**W7** [warning, 共识, 持续 R6-R9] **Hacking taxonomy 系统性不足**
- R1-W6 + R2-W4，双方 [AGREE 部分]
- 9 类中 H1/H7/H8 占 >90%；其余 6 类中至少 4 个是单 seed/单条件孤立观察。分类器验证仅 50 样本，无 confusion matrix。Residual classification inflate non-hacking rate。
- **要求**: 区分 "robust modes" (H1/H7/H8: multi-seed) vs. "isolated observations"；增加验证样本量。

**W8** [warning, 共识, 持续 R6-R9] **Dose-response claim 基于不均匀 seed 数**
- β=0.1 用 5 seeds，β=0.05/0.2/0.3 用 3 seeds。4 个 dose points 不足以刻画非单调模式。
- **要求**: "Non-monotonic dose-response" 弱化为 descriptive pattern。

**W9** [warning, 共识, 持续 R5-R9] **Abstract 数据堆砌**
- ~10 个具体数字 (97±2%, 99.5%, 92%, ISR≥0.5, β=0.1, 23% vs 8%, nine modes 等)。审稿人 30 秒内难以抓住关键 takeaway。
- **要求**: 删减至 4-5 个关键数字，删除 genuine window 相关数字。

**W10** [warning, 新 R9] **§4.4 标题 "Cross-Logic Diagnostic Transfer" 措辞过强**
- R1-W7 + R2 [AGREE]。实际是在不同设置下重新运行 STA，非 ML 意义上的 transfer。
- **要求**: 改为 "Cross-Logic Replication" 或 "STA on Prolog"。

**W11** [warning, 新 R9, 分歧] **Premise-count confound 对 ISR-as-diagnostic 的影响范围**
- R1-W3 [critical]: ISR 应定位为 "non-redundancy metric"，confound 影响所有用途。
- R2 [REBUT]: confound 主要影响 ISR-as-reward，不影响 ISR-as-diagnostic (同 seed 时间序列)。
- **Director 裁决**: R2 的区分有道理——C1 不依赖 cross-condition ISR 比较。但论文应在 §3.2 进一步澄清 confound 在不同使用场景下的影响差异。降级为 warning。

### Minor Issues

**M1** Table 1 注释系统过复杂 (†, ‡, ††, ★)，建议拆分为 primary conditions + cross-scale 两张表。
**M2** Introduction 过载定量结果 (ISR*: 0.642→0.132→0.003; PR σ=47pp; OR=147 等)，数字应留给 Experiments。
**M3** Figure 1 Panel (a) 信息密度一般 (标准 NL→formal→solver pipeline)，可压缩。
**M4** §3.2 Shapley 讨论第三个理由 ("Goodhart effects would likely transfer") 是循环论证。
**M5** 训练时 sampling vs 评估时 greedy decoding 策略不一致未被讨论。
**M6** 论文标题 "Valid" 有歧义 (execution validity vs logical validity)。
**M7** 术语不一致: "genuine"/"non-hacking"/"structurally sound" 交替使用导致语义滑移。应统一为 "non-hacking"。

---

## Reviewer Consensus [AGREE]

以下问题两位 Reviewer 达成共识：

1. **总评 3.0 (Findings)**: 双方一致
2. **CMH p-values 应降至 Appendix**: R1 [critical] + R2 [AGREE 部分]
3. **Genuine window 从 Abstract/Contributions 移除**: R1 + R2 双方 [AGREE]
4. **单一数据集限制泛化性**: R1 + R2 双方 [AGREE]
5. **1.7B 单 seed 与方法论矛盾**: R1 + R2 双方 [AGREE]
6. **SFT PR confound 真实存在**: R1 + R2 双方 [AGREE]
7. **Taxonomy 应区分 robust vs isolated modes**: R1 + R2 双方 [AGREE]
8. **Cross-logic "transfer" 措辞过强**: R1 + R2 双方 [AGREE]
9. **Goodhart novelty 有限但 empirical characterization 有价值**: R1 [nuance] + R2 [critical]
10. **写作质量好，无 AI 痕迹，格式完全合规**: R1 + R2 双方 [AGREE]

---

## Reviewer Divergence [REBUT]

**唯一实质性分歧: Premise-count confound 的影响范围**

- **R1 立场** [critical]: ISR 定义对 premise count 有结构性依赖，影响所有用途。ISR 应重新定位为 "component non-redundancy metric" 而非 "structural integrity metric"。论文中所有 "structural integrity" 措辞应弱化。
- **R2 立场** [REBUT]: ISR 作为诊断 (C1) 使用时是同 seed 时间序列分析 (ISR* 0.642→0.132→0.003)，不依赖 cross-condition 比较，因此 premise-count confound 不影响 C1 核心发现。Confound 主要影响 ISR-as-reward 的 cross-condition 比较 (§4.3)，论文已在 §3.2 和 Appendix C 充分讨论。
- **Director 裁决**: R2 的区分有技术道理。C1 的 99.5% collapse trajectory 是 within-seed 观察，premise-count 变化本身是 degeneration 的表征 (mean n: 6.58→18.55)。但 R1 关于 "structural integrity" 措辞精确度的要求合理。降级为 warning (W11)，要求 §3.2 澄清不同使用场景下的 confound 影响。

---

## Questions

以下问题需要作者澄清（按优先级排序）：

**Q1** [R1+R2, 高优先级] 如果使用 premise-count-normalized ISR（如 ISR / E[ISR | n]）作为 reward，Goodhart collapse 是否仍然发生？如不行，原因是什么？

**Q2** [R1+R2, 高优先级] ISR 是否被测试过作为 rejection filter（丢弃 ISR < threshold 的输出）而非 continuous reward？Filter 不提供优化梯度，可能避免 Goodhart collapse。

**Q3** [R1, 中优先级] ISR=1 的 proofs 是否一定语义正确？能否提供 ISR=1 但语义错误的反例？

**Q4** [R2, 中优先级] 不同模型家族（Llama, Gemma）或 instruction-tuned vs. base 模型是否会产生本质不同的 hacking 动力学？

**Q5** [R2, 中优先级] 增加训练数据规模（如 5000 examples），hacking 的普遍性和模式分布是否会改变？

**Q6** [R1, 低优先级] STA 的 false-negative rate 是多少？Solver 内在冗余是否会导致 STA 低估 necessity？

**Q7** [R1, 低优先级] "99.5% structural collapse" 精确指 ISR* 从 0.642 降至 0.003 的相对下降？还是 ISR=0 的样本比例？

---

## Missing References

**共识推荐引用：**
- Uesato et al. (2022) "Solving Math Word Problems with Process- and Outcome-Based Feedback" — process vs outcome feedback 对比，与 ISR vs PR 概念对应 (R1 提出, R2 [AGREE])

**建议考虑：**
- Khalaf et al. (NeurIPS 2025) "Inference-Time Reward Hacking in Large Language Models" — 与论文 training-time vs inference-time 区分直接相关 (R2 提出)
- "Reward Hacking as Equilibrium under Finite Evaluation" (arXiv:2603.28063, 2026) — 理论互补 (R2 提出, 真实性待确认)

**已确认不需要：**
- Cobbe et al. (2021) — R2 rebuts: 数学文字题 verifier 与本文设置本质不同
- Gao et al. (2023) — R1 提出但 R2 确认已引用

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 2.5/5 | 3.5/5 | 3.0/5 |
| Excitement | 3.5/5 | 2.5/5 | 3.0/5 |
| Overall | 3.0 | 3.0 | **3.0** |
| Confidence | 4/5 | 4/5 | 4/5 |

**评分解读 (EMNLP 2026 ARR)**:
- 3.0 = Findings（可被 Findings 接收）
- 距主会议接收 (4.0) 有显著差距
- 距 Borderline Conference (3.5) 需解决至少 W1-W4 中的 2-3 个

**核心判断**: STA/ISR 作为诊断工具的概念有价值，observer-optimizer 不对称性框架清晰有力。但四个 critical 问题限制了当前版本的可接收性：(1) 统计呈现架构需重组 (CMH→Appendix, permutation→primary)；(2) genuine window 在三重检验后不成立但仍列为发现；(3) 核心 Goodhart 发现可从定义预测，需 reframe；(4) 实验范围与标题 scope 不匹配。

**修改建议优先级**:
1. [紧急, deadline 前可完成] 统计呈现重组 + genuine window 移除 + 术语统一 (W1, W2, M7)
2. [紧急, deadline 前可完成] 标题收窄 + C2 reframe + Abstract 精简 (W3, W4, W9)
3. [重要, deadline 前可部分完成] SFT caveat 加强 + taxonomy 区分 + cross-logic 标题修改 (W5, W7, W10)
4. [理想但非必须] 增加 seeds/数据集, normalized ISR 实验 (W6, W8, Q1-Q2)

---

## Detailed Comments（逐节）

### Abstract
- 信息密度过高 (~10 个数字)，建议保留 "99.5% collapse" 和 "Goodhart collapse at all tested doses" 两个核心数据点
- "transient genuine window" 应删除（三重检验后不成立）
- "structurally sound" 应改为 "non-hacking"
- "trajectory-confirmed at β=0.1" 过于细节化

### Introduction (§1)
- 叙事结构完整 (blind spot → STA → ISR as reward → contributions)
- 过载定量结果 (ISR*: 0.642→0.132→0.003; PR σ=47pp; OR=147)——数字留给 Experiments
- C4 声明与证据强度不匹配（多数 taxonomy 模式为孤立观察）
- SFT 对比需加 PR-level caveat

### Related Work (§2)
- 结构清晰，与 Kim et al. (2026) 区分精确
- 与 Ng (1999) reward shaping 的理论联系有洞察力
- 建议增加 Uesato et al. (2022) 引用

### Method (§3)
- Algorithm 1 清晰，ISR 定义明确
- LOO vs. Shapley 讨论充分但第三个理由循环论证
- §3.2 premise-count confound 讨论值得肯定，但应增加不同使用场景下的影响区分

### Experiments (§4)
- §4.2 (ISR as Diagnostic): 最强部分。Figure 2 有力。Cross-seed divergence 分析有价值
- §4.3 (Goodhart Effects): 统计呈现需重组。β 呈现顺序应为升序。Genuine window 降级为描述性
- §4.4 (Cross-Logic): 标题 "Transfer" 过强，改为 "Replication"
- §4.5 (Cross-Scale): 单 seed，建议移入 Appendix 或大幅压缩
- §4.6 (Taxonomy): Table 2 好，但应区分 robust vs isolated modes

### Discussion & Conclusion (§5)
- 核心 takeaway 清晰。建议增加 ISR-as-filter 和 count-normalized ISR 的 future work 讨论

### Limitations (§6)
- 详尽且诚实（temporal snapshot, seed counts, cross-scale, data scale）——显著优势
- 建议更突出 statistical power 不足和 premise-count confound 的具体影响

### 格式合规
- ✓ ≤8 页正文 (§1-§5 在 page 8 完成)
- ✓ ACL LaTeX [review] 模板
- ✓ Double-blind ("Anonymous ACL submission", URL [anonymized])
- ✓ 行号可见
- ✓ Limitations + Ethics 完整
- ✓ 无 AI 写作痕迹