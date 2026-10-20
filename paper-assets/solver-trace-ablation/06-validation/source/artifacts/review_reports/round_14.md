---
round: 14
review_mode: continue
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T10:25:37.221227+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 14 Consolidated Review Report

**Paper**: Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners
**Venue**: ACL ARR May 2026 → EMNLP 2026 (Long Paper)
**Review Mode**: Continue (from Round 13)
**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性/写作)

---

## Summary

论文提出 Solver Trace Ablation (STA) 和 Irreducible Solver Rate (ISR) 来检测 GRPO 训练的 FOL 推理器中的 reward hacking。R14 修订响应了 R13 提出的大部分问题：ISR framing 从 "structural quality diagnostic" 精确化为 "component-necessity diagnostic"；Kim et al. (2026) 对比从一句话扩展为完整的三维度分析段落；Discussion 增加了 gated ISR 实验（TS→PG mode migration）作为 mitigation 分析的实证支撑；hacking modes 从不透明编号 (H1/H7/H8/H9) 重命名为描述性缩写 (CE/TS/PG/CI)；Abstract 消除了 single-seed cherry-picking (改用 3-seed aggregate ISR*=0.03±0.05)。

论文现已自我定位为 "empirical case study"，claims 普遍以 hedged 形式呈现。核心发现（所有测试 dose 下的 Goodhart collapse）有充分数据支撑，但概念新颖性（LOO 标准技术 + Goodhart 可预测性）仍是结构性限制。

---

## R13 Issue Resolution Status

**19 issues resolved in R14** (of 26 R13 open/in_progress items evaluated):

| Issue | Status | Resolution |
|-------|--------|------------|
| v13-R2-N2 (Kim et al. 对比) | ✅ RESOLVED | Related Work 新增 "Faithfulness in formalization" 段落，3 维度逐条对比 |
| v13-R1-W1 (ISR framing) | ✅ RESOLVED | Method §3.2: "ISR is a component-necessity diagnostic, not a reasoning-quality metric" |
| v13-R2-W5 (Table 2 聚合) | ✅ RESOLVED | Caption 标注 single-seed vs pooled |
| v13-R2-MITIGATION (Discussion 缺 mitigation) | ✅ RESOLVED | Gated ISR 实验 + reward ensembling + constrained optimization |
| v13-R1-Q4 (Prolog 无 random control) | ✅ RESOLVED | §4.3 显式声明限制 |
| v5-R2-W1 (Abstract cherry-picking) | ✅ RESOLVED | 3-seed aggregate 替代 single-seed |
| v4-R12-N2 (collapse claim 过强) | ✅ RESOLVED | "four tested doses" + "preliminary" |
| v4-R12-W6 (s43 eval 协议) | ✅ RESOLVED | 脚注已添加 |
| v4-R12-W7 (N-H upper bound) | ✅ RESOLVED | Table 1 caption + Method §3.5 标注 |
| v4-R1-W8 (统计功效) | ✅ RESOLVED | Wilson CIs 完整呈现 |
| v8-R12-N2 (scope mismatch) | ✅ RESOLVED | Hedging 充分 |
| v8-R1-N3 (术语滑移) | ✅ RESOLVED | H1→CE 等全文重命名无残留 |
| v5-R2-W3 (段落碎片化) | ✅ RESOLVED | 段落结构改善 |
| v6-R1-W2 (dose-response 统计) | ✅ RESOLVED | "preliminary" 标注 |
| v8-R1-W4 (多重比较) | ✅ RESOLVED | CMH 标注 "inflated" |
| v5-R1-N3 (Table 1 不对称) | ✅ RESOLVED | 标注清晰 |
| v10-R2-W8 (Discussion 过短) | ✅ RESOLVED | 14 行含实质 mitigation 内容 |
| v11-R1-W2 (taxonomy 验证) | ✅ RESOLVED | PG 降为 "lower prevalence" |
| v5-R2-MR / v11-R2-MR (引用) | ✅ RESOLVED | Llemma + Coste + Moskovitz 补充 |

**4 issues still open/actionable:**

1. **v4-R12-N3** [in_progress, critical → major]: OR 方向反转 (ISR N-H 6.06% < Random 9.5%) 未在正文讨论。两位 reviewer 一致认为应增加 1-2 句。这实际上强化核心论点（ISR reward 不仅未改善非 hacking 质量，反而可能更差）。
2. **v14-R12-GATED-S54** [open, warning]: Discussion 遗漏 s54 (96.7% non-hacking)，只报告 "2/3 seeds migrate to PG"。有选择性呈现嫌疑。建议补充完整 seed 分布。
3. **v5-R12-SFT-PR** [in_progress, critical]: §4.2 line 42 仍用 "RL-specific" 旧措辞，与 Abstract/Introduction/Discussion 中 "associated with RL optimization" 的 hedged 表述不一致。一处遗漏的统一化修改。
4. **v13-R2-W4** [open, info]: ~18 缩写，未添加 notation summary。描述性重命名 (CE/TS/PG/CI) 已显著改善可读性，降为 minor。

**Structural issues (in_progress, cannot be resolved by revision):**
- v8-R12-N1: 核心发现的可预测性限制概念新颖性
- v4-R2-W9 / v5-R2-N3: LOO 是标准技术，方法新颖性有限
- v6-R2-W8: Taxonomy 分类标准为规则+功能分析混合

---

## New Strengths (R14)

- **S7 (Gated ISR Experiment)**: Component-count gate 实验 (Appendix §B.11) 将论文从纯诊断扩展为诊断+mitigation 尝试。TS→PG mode migration 的 "blocking one Goodhart pathway redirects optimization pressure" 是非平凡发现。
- **S8 (Kim et al. Comparison)**: Related Work 的三维度对比（training vs inference, STA/ISR vs LLM-judge, universal gaming vs no-gaming + CE ≈ axiom-fabrication 互补性）质量高，展示了成熟的 positioning 能力。
- **S9 (Descriptive Mode Names)**: CE/TS/PG/CI 替代 H1/H7/H8/H9，大幅改善可读性和学术标准。
- **S10 (Mitigation Landscape)**: Discussion 现在有实质内容：gated ISR 实验数据 + reward ensembling (Coste 2024) + constrained optimization (Moskovitz 2024) + TRACE (Wang 2025)。

---

## Weaknesses

### Structural (无法通过修订解决)

**W-S1**: 核心概念新颖性有限。LOO 是标准消融技术，Goodhart collapse 在 proxy reward 设置下可预测。论文自我定位为 "empirical case study" 是诚实的，但这也意味着贡献以实证观察为主（seed-dependent dynamics, mode taxonomy, migration patterns），而非方法或理论突破。这决定了论文的 ceiling 在 Findings 到 Borderline Conference 之间。

### Fixable (可通过修订解决)

**W-F1** [warning]: OR 方向反转 (ISR N-H=6.06% < Random N-H=9.5%, corrected; matched cohort 同方向 2.3% vs 5.9%) 是论文最有力的证据之一，却未在正文任何位置讨论。ISR reward 不仅未改善非 hacking 质量，point estimate 实际更差。在 §4.3 或 Discussion 增加 1-2 句即可。

**W-F2** [warning]: Gated ISR 实验在 Discussion 中只报告 "2/3 seeds migrate to PG"，遗漏 s54 (96.7% non-hacking)。这构成选择性呈现：3 个 seed 中 1 个未 migrate 但未被提及。修改建议："2/3 seeds migrate to PG, while 1/3 sustains predominantly non-hacking output (96.7%); the outcome is highly seed-dependent with only 3 seeds。"

**W-F3** [warning]: §4.2 line 42 仍用 "RL-specific" 旧措辞，与 Abstract/Introduction/Discussion 的 hedged 表述 ("associated with RL optimization, though the large prove-rate gap prevents definitive causal attribution") 不一致。遗漏的统一化修改，一处改动即可修复。

**W-F4** [info]: Limitations section 从 R13 的 ~14 行压缩至 6-7 行。8 页限制下可理解，但不再是 R13 评价的 "论文亮点"。SFT n=39 限制未单独提及。关键限制讨论散落在正文各处和 Appendix。

---

## Questions for Authors

1. ISR N-H=6.06% < Random N-H=9.5% 的方向反转是否有意未在正文讨论？若有意，理由是什么？
2. Gated ISR 的 s54 (96.7% non-hacking, 3.3% PG) 为何未在 Discussion 中与 s52/s53 一并报告？
3. §4.2 line 42 的 "RL-specific" 是否为修改遗漏？

---

## Missing References

无新增缺失引用。引用覆盖充足。

---

## Cross-Reviewer Consensus

| Topic | R1 | R2 | Consensus |
|-------|----|----|-----------|
| OR 反转需正文讨论 | AGREE | AGREE | ✅ 一致 |
| s54 遗漏需补充 | AGREE | AGREE | ✅ 一致 |
| §4.2 "RL-specific" 遗漏 | AGREE | AGREE | ✅ 一致 |
| Gated ISR 是有价值增量 | AGREE | AGREE | ✅ 一致 |
| Kim et al. 对比质量 | AGREE (充分) | AGREE (充分且有深度) | ✅ 一致 |
| ISR framing 校正 | RESOLVED | RESOLVED | ✅ 一致 |
| Mode 重命名改善 | AGREE | AGREE | ✅ 一致 |
| Abstract cherry-picking 消除 | RESOLVED | RESOLVED | ✅ 一致 |
| 概念新颖性结构性限制 | Partially (empirical rigor 有价值) | Yes (LOO+Goodhart 可预测) | ⚠️ 分歧在权重 |
| Overall 评分 | 3.5 | 3.0 | ⚠️ 半分分歧 |

**分歧分析**: R1 (3.5) 认为 empirical rigor（matched cohort design、gated ISR、taxonomy precision）有独立价值，接近 Borderline Conference。R2 (3.0) 认为 LOO+Goodhart 的可预测性限制了 excitement，尽管承认 gated ISR 的 mode migration 是非平凡发现（将 novelty 从 2.5 上调至 3.0）。这是合理的价值判断分歧，非事实性矛盾。

---

## Overall Assessment

**Score: 3.0 (Findings)**
**Range: 3.0 - 3.5**
**Confidence: 4/5**

R14 修订质量高：19 项 R13 问题得到解决，新增的 gated ISR 实验和 Kim et al. 三维度对比是实质性改进。论文在可修改的范围内已接近最优状态。

剩余可修的问题（OR 反转讨论、s54 补充、§4.2 措辞统一）均为 1-2 句改动，不影响整体评价。

评分锚定为 3.0 (Findings) 的核心原因是结构性的：(1) LOO 是标准消融技术，不构成方法贡献；(2) Goodhart collapse 在 proxy reward 设置下概念上可预测，empirical details（hacking mode taxonomy, migration patterns）有增量价值但不构成 Conference 级别的 novelty threshold；(3) 实验范围限于单模型/单数据集/单算法。论文诚实地自我定位为 "empirical case study"，Findings 是恰当的归宿。

如果 R15 修复 W-F1 至 W-F3，评分不会实质改变（仍为 3.0-3.5 区间），因为限制因素是结构性的。

---

## Issue Tracker Summary (R14)

Total: 97 issues across 15 rounds
- Resolved: 83 (85.6%)
- In Progress: 8 (8.2%, 含 4 个结构性问题)
- Open: 5 (5.2%, 含 2 个 dormant + 3 个 actionable)
- Won't Fix: 1 (1.0%)