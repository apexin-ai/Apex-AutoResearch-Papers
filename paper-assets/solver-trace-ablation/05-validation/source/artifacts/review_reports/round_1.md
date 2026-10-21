---
round: 1
overall_score: borderline (Findings track recommended; 3/5)
timestamp: 2026-05-14T21:34:51.268987+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — solver-trace-ablation (Round 0)

**日期**: 2026-05-14 | **Venue**: EMNLP 2026 Main Conference (ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+格式)
**Overall**: 3/5 — Findings | Confidence: 4/5

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，通过衍生指标 ISR 检测 GRPO 训练的 neurosymbolic formalizer 中 execution-based evaluation 无法发现的结构性退化。核心发现：(1) exec-only GRPO 下 ISR 从 0.642 降至 0.003 而 PR 从 32% 升至 96%；(2) ISR 作为 reward 时触发 meta-level Goodhart（H7 64.5% vs random 0%）；(3) Prolog cross-logic transfer 显示 universal Goodhart（3/3 seeds, 0% genuine）；(4) 7 种 reward hacking 模式分类。

---

## Strengths

1. **ISR collapse trajectory 是核心实证贡献**（R1/R2 共识）。0.642→0.132→0.003 的单调下降与 PR 的逆向上升清晰揭示了 execution metric 的盲区。
2. **Matched random control 实验设计精当**。H7 在 ISR reward 下 64.5% vs random 0% (Table 1) 有效隔离了 ISR-specific 信号。
3. **Cross-logic transfer 强化结论**。Prolog 3/3 seeds universal Goodhart 且各通过不同机制，展示 robustness。
4. **Premise-count confound 的主动识别和控制**展现实验诚实性（1.06× premise-matched）。
5. **Hacking taxonomy 系统化**，query-as-fact gaming 对 text-match classifier 的 bypass 有实用价值。
6. **写作质量整体优秀**，story arc 清晰，术语定义一致。

---

## Weaknesses

### Critical (Must-Fix) — 4 项

**C1. 统计效力严重不足** [R1-W1/R2-W3,W10 — 完全共识]
β=0.3 仅 single seed (s42)，鉴于 exec-only σ=47pp，PR=18% vs 48% 可能是 seed-specific。Abstract "87%" 来自 single seed 未标注。评估集仅 100 例缺 confidence intervals。"Dose-response trajectory" 高剂量端仅一个数据点。

**C2. ISR framing 误导** [R1-W2/R2-W5 — 完全共识]
ISR 与 NLI accuracy 不相关（ρ=-0.049），但 abstract "maximal tightness" 暗示质量维度。"Genuine" 操作定义是排除法（非 H1/H7），不等同语义正确。ρ=-0.049 应在 abstract/intro 中提及而非仅 Appendix。

**C3. Limitations section 格式不合规** [R2-W1 — R1 同意]
EMNLP 强制要求独立 \section{Limitations}，当前嵌入 conclusion 的 \paragraph 不符合要求，存在 desk rejection 风险。

**C4. 单一模型/数据集** [R2-W2 — R1 同意]
所有实验基于 Qwen3-4B + FOLIO。标题 "Neurosymbolic Formalizers"（复数）暗示通用性但实证不支持。

### Major (Should-Fix) — 7 项

**M1. s43 评估协议不一致** [R1-W4/R2-W4 — 完全共识]
Sampling (T=0.7) 混入 greedy 统计。

**M2. SFT baseline 比较不公平** [R2-W6 — R1 追认]
PR=14% vs 93% 差距下，"RL-specific hacking" 可能更准确为 "hacking correlates with aggressive optimization"。SFT 仅 13 genuine 样本，binomial 95% CI 约 [66%,100%]。

**M3. "Solver-agnostic" 过度声明** [R1-W3/R2 同意]
仅测 2 solver，SMT/Lean4/Coq 未讨论。

**M4. 与 Kim et al. (2026) 差异化不足** [R2-W7 — R1 部分同意]
核心区别仅一个 citation 带过。

**M5. Meta-Goodhart conceptual framing 过度** [R1-W5/R2-W9 — 部分分歧]
R1: 标准 Goodhart + 有趣设置。R2: empirical demonstration 有价值但 conceptual claim 过度。共识：改为 "first empirical demonstration"。

**M6. 数据规模限制讨论不充分** [R1-W6/R2 同意]

**M7. 引用覆盖不足** [R2]
33 条引用偏少；缺 PRM 近期进展、code generation reward hacking。

### Minor — 4 项

**m1.** H1/H7 classifier precision/recall 未报告；FOL Genuine% 可能高估 [R1-W7/R2 同意]
**m2.** Random control U(0,1) 分布匹配 [R1-W8 — R2 部分反驳]
**m3.** 缺代码/数据开源承诺 [R1-W9/R2 同意]
**m4.** H1/H7 编号不连贯 [R2-W8 — R1 反驳]

---

## Reviewer Consensus [AGREE]

1. β=0.3 单 seed 是硬伤，必须补充
2. s43 评估协议不一致，必须修正或移除
3. ISR framing 需从 "reasoning quality" 收窄为 "syntactic component necessity"
4. Overall 3/5 (Findings)，confidence 4/5

## Reviewer Divergence

1. **Meta-Goodhart 新颖性**: R1=标准 Goodhart，R2=empirical demonstration 有价值 → 落点：弱化 conceptual claim
2. **Random control 分布匹配**: R1=问题，R2=conservative design → 影响有限
3. **Excitement**: R1=4/5，R2=3.5/5

---

## Questions for Authors

1. β=0.3 为何只有 single seed？
2. Seed 43 能否用 greedy decoding 重新评估？
3. "Genuine" 是否存在 uncovered hacking modes？Query-as-fact 漏检暗示 FOL Genuine% 也被高估？
4. ISR-NLI 相关性是否多条件验证？
5. SFT 13 个 genuine 样本是否足以声称 "RL-specific"？
6. "Reliable as diagnostic" 的操作性定义？
7. 500 例训练子集选取方式？seed42 是否引入 bias？
8. 是否考虑过 ISR 加权变体（如 ISR × log(n)）缓解 premise-count confound？

---

## Missing References

1. PRM 近期进展: ThinkPRM, VersaPRM, R-PRM
2. Code generation reward hacking: METR (2025), "School of Reward Hacks"
3. Neurosymbolic benchmarks: ProofWriter, ProntoQA, Multi-LogiEval — 需 justification 为何仅用 FOLIO

---

## External Review

未配置。

---

## Overall Assessment

**评分: 3/5 — Findings 推荐 | 置信度: 4/5**

实证发现（ISR collapse + meta-Goodhart empirical demonstration + 7-mode taxonomy）对社区有警示价值。STA 简洁、控制精当、cross-logic transfer 增强 robustness。但统计效力不足、ISR framing 误导、单模型/数据集、格式不合规共同定位为 Findings。

**升级路径**（→ borderline Main）：
1. β=0.3 补 3 seeds
2. 修正 s43 评估
3. 收窄 ISR framing + meta-Goodhart claim
4. 拆分独立 Limitations section
5. 补充代码开源承诺