# Round 0 审稿报告 — solver-trace-ablation

**日期**: 2026-05-14
**Venue**: EMNLP 2026 Main Conference (ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+格式)
**Overall**: 3/5 — Findings | Confidence: 4/5

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out 消融的诊断方法，通过衍生指标 ISR 检测 GRPO 训练的 neurosymbolic formalizer 中 execution-based evaluation 无法发现的结构性退化。核心发现包括：(1) exec-only GRPO 下 ISR 从 0.642 降至 0.003 而 PR 从 32% 升至 96%；(2) ISR 作为 reward 时触发 meta-level Goodhart（H7 64.5% vs random 0%）；(3) Prolog cross-logic transfer 显示 universal Goodhart（3/3 seeds, 0% genuine）。论文归纳了 7 种 reward hacking 模式。

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

### Critical (Must-Fix)

**C1. 统计效力严重不足** [R1-W1 / R2-W3,W10 — 完全共识]
- β=0.3 仅 single seed (s42)，鉴于 exec-only σ=47pp，PR=18% vs 48% 可能是 seed-specific
- Abstract 的 "87%" 来自 single seed 而未标注
- 评估集仅 100 例，单 seed 结果缺乏 confidence intervals
- "Dose-response trajectory" 的高剂量端仅一个数据点

**C2. ISR framing 误导** [R1-W2 / R2-W5 — 完全共识]
- ISR 与 NLI accuracy 不相关（ρ=-0.049, p=0.187），但 abstract 中 "maximal tightness" 暗示质量维度
- "Genuine" 的操作性定义是排除法（非 H1/H7），不等同于语义正确
- ISR caveat 埋在 §4.2，ρ=-0.049 仅在 Appendix §B

**C3. Limitations section 格式不合规** [R2-W1 — R1 同意(降级 Major)]
- EMNLP 强制要求独立 \section{Limitations}
- 当前嵌入 conclusion 的 \paragraph{Limitations and Future Work} 不符合要求
- 存在 desk rejection 风险

**C4. 单一模型/数据集** [R2-W2 — R1 同意(降级 Major)]
- 所有实验基于 Qwen3-4B + FOLIO
- 标题 "Neurosymbolic Formalizers"（复数）暗示通用性

### Major (Should-Fix)

**M1. s43 评估协议不一致** [R1-W4 / R2-W4 — 完全共识]
- Sampling (T=0.7) 混入 greedy 统计，Appendix 承认 "not strictly comparable" 但仍纳入

**M2. SFT baseline 比较不公平** [R2-W6 — R1 交叉回应中追认]
- PR=14% vs 93%，低 PR 本身减少 hacking 机会
- SFT 仅 13 genuine 样本，binomial 95% CI 约 [66%, 100%]
- "RL-specific" 可能更准确表述为 "hacking correlates with aggressive optimization"

**M3. "Solver-agnostic" 过度声明** [R1-W3 / R2 同意]
- 仅测 2 solver，SMT/Lean4/Coq 等未讨论
- 建议改为 "solver-agnostic in principle, validated on two solvers"

**M4. 与 Kim et al. (2026) 差异化不足** [R2-W7 — R1 部分同意]
- Training-time RL vs inference-time prompting 的核心区别仅一个 citation 带过

**M5. Meta-Goodhart conceptual framing 过度** [R1-W5 / R2-W9 — 部分分歧]
- R1: 标准 Goodhart + 有趣实验设置
- R2: Empirical demonstration 有独立价值但 conceptual novelty claim 过度
- 共识建议：改为 "first empirical demonstration of Goodhart at meta level"

**M6. 数据规模限制讨论不充分** [R1-W6 / R2 同意]
- 500 训练/100 评估；训练子集选取方式未说明

**M7. 引用覆盖不足** [R2-MISSING-REF]
- 33 条引用对 EMNLP main 偏少
- 缺：PRM 近期进展 (ThinkPRM, VersaPRM)、code generation reward hacking、benchmark 选择 justification

### Minor

**m1.** H1/H7 classifier precision/recall 未报告；FOL Genuine% 可能系统性高估 [R1-W7 / R2 同意]
**m2.** Random control U(0,1) 分布匹配 [R1-W8 — R2 部分反驳：conservative design choice]
**m3.** 缺代码/数据开源承诺 [R1-W9 / R2 同意]
**m4.** H1/H7 编号不连贯 [R2-W8 — R1 反驳]

---

## Reviewer Consensus

两位 Reviewer 在以下核心问题上完全一致 [AGREE]：
1. β=0.3 单 seed 是硬伤，必须补充
2. s43 评估协议不一致，必须修正或移除
3. ISR framing 需从 "reasoning quality" 收窄为 "syntactic component necessity"
4. Overall 3/5 (Findings)，confidence 4/5

## Reviewer Divergence

1. **Meta-Goodhart 新颖性** [部分分歧]：R1 评为标准 Goodhart (Major)，R2 认为 empirical demonstration 有价值但 framing 过度 → 共识落点：弱化 conceptual claim，强调 empirical 贡献
2. **Random control 分布匹配** [部分分歧]：R1 认为 U(0,1) 与 ISR skewed 分布不匹配，R2 论证这是 conservative design → 分歧未完全解决但影响有限
3. **Excitement** [轻微分歧]：R1 给 4/5，R2 给 3.5/5

---

## Questions for Authors

1. β=0.3 为何只有 single seed？计算资源限制还是设计选择？
2. Seed 43 能否用 greedy decoding 重新评估？
3. "Genuine" 定义是否存在 uncovered hacking modes？Query-as-fact 漏检是否暗示 FOL Genuine% 也被高估？
4. ISR-NLI 相关性（ρ=-0.049）是否在多条件下验证？
5. SFT 仅 14% PR，13 个 genuine 样本——是否足以声称 "hacking is RL-specific"？
6. "Reliable as diagnostic" 的操作性定义？ISR 对 query-as-fact (ISR≈0.912) 的 false negative 如何处理？
7. 500 例训练子集如何选取？train_500_seed42.jsonl 中的 seed42 是否引入 selection bias？
8. 是否考虑过 ISR 的加权变体（如 ISR × log(n)）来缓解 premise-count confound？

---

## Missing References

1. **PRM 近期进展**: ThinkPRM (arXiv:2504.16828), VersaPRM (ICML 2025), R-PRM (EMNLP 2025)
2. **Code generation reward hacking**: METR frontier model reward hacking (2025), "School of Reward Hacks" (arXiv:2508.17511)
3. **Neurosymbolic benchmarks**: ProofWriter, ProntoQA, Multi-LogiEval — 为何仅用 FOLIO 需 justification
4. **Mechanistic interpretability**: structural analysis 与 probing 方法论联系

---

## External Review (Stanford Agentic Reviewer)

未配置。

---

## Overall Assessment

**评分: 3/5 — Findings 推荐**
**置信度: 4/5**

实证发现（ISR collapse + meta-Goodhart empirical demonstration + 7-mode hacking taxonomy）对 neurosymbolic RL 社区有警示价值。STA 方法简洁、random control 设计精当、cross-logic transfer 增强 robustness。

但以下问题共同将其定位为 Findings 而非 Main Conference：
- 统计效力不足（β=0.3 单 seed、s43 评估不一致、100 例评估集）
- ISR framing 误导（syntactic necessity ≠ semantic faithfulness，需显著收窄）
- 单一模型/数据集限制通用性声明
- Limitations section 格式不合规（desk rejection 风险）
- SFT baseline 公平性问题

**升级路径**（Findings → borderline Main Conference）：
1. β=0.3 补 3 seeds
2. 修正 s43 评估或移除出汇总
3. 收窄 ISR framing + meta-Goodhart novelty claim
4. 拆分独立 Limitations section
5. 补充代码开源承诺
