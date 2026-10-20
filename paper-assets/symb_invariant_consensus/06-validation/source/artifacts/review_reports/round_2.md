---
round: 2
review_mode: 
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T05:12:50.407694+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 圆桌审稿报告 — Round 4 (Final, Revised Paper)

**论文**: Beyond Self-Consistency: How Trace Independence Limits Symbolic Consensus in LLM Reasoning
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: 重新审稿（Fresh）— 修订版论文全文独立评审

---

## 审稿人配置与流程

| Reviewer | 类型 | 侧重 | 初审评分 |
|----------|------|------|---------|
| R1 | Dream | 方法+实验严谨性 | 3/6 (Borderline Reject, 6分制) |
| R2 | Agent | 新颖性+完整性+写作质量 | **3.5/5 (Borderline Conference, ARR标准)** |

**流程**：R1 + R2 独立初审 → Director 对 R1 全部 claim 独立验证（发现多处与实际论文不符）→ R1 验证后发现 + Director 独立发现交叉分享给 R2 → R2 逐条回应（7/7 AGREE）→ 完全收敛。

---

## ⚠️ Director 独立验证：Dream R1 版本偏差

Dream R1 的多个 critical claim 与实际论文不符：

| R1 声称 | 实际状态 | 判定 |
|---------|---------|------|
| MAX-SAT scoring function 未形式化定义 | Eq.(2)-(4) + Alg 1-2 完整 | **不正确** |
| Oracle 仅 1 数据集 | FOLIO + ProofWriter 双 Oracle | **不正确** |

R2 (Agent) 的审稿与实际论文完全一致，确认了 ~50 篇引用、完整形式化、双 Oracle、全面 Related Work 等。**本报告以 R2 的准确评估为主体，仅保留 R1 经验证后成立的发现。**

---

## Summary

论文评估 SICA，一个从 LLM reasoning traces 提取 FOL 式约束并通过 MAX-SAT 聚合答案的管线。在 7 个模型（7B-32B）、4 个推理域、2400+ 实例上系统测试，发现 SICA 仅在窄带（SC ~50-55%）内有正面趋势，提出 Type A/B/C 三种失败模式。双 Oracle 控制（FOLIO +14.22pp, ProofWriter +11.50pp, 均 p<0.001）因果定位瓶颈在约束提取质量。CJT/Eff-K 框架量化 trace 相关性。Entropy-conditioned mechanism 解释微观作用路径。9 种 remediation 策略全部失败。

---

## Strengths

**S1: 实验覆盖面与系统性。** 7 模型 × 4+ 域 × 14 非 Oracle 条件 + 2 Oracle 条件 + 3-seed 复制。覆盖面远超同类负面结果论文。

**S2: 双 Oracle 控制设计精巧。** FOLIO（gold FOL）+ ProofWriter（gold DSL）双独立数据集，产生 +14.22pp (p=2.0×10⁻⁷) 和 +11.50pp (p=9.21×10⁻¹⁵)。ProofWriter 的 per-subtype breakdown（RelNeg +17.86pp > AttNoneg +9.09pp）提供额外粒度。这是论文最有说服力的贡献。

**S3: Entropy-conditioned mechanism 是最有价值的新贡献。** （R2 特别强调）SICA gains 集中于 high-entropy 问题（+9.6pp, n=73），aggregate effect 取决于高 entropy 问题比例（Mistral 35.8% vs Qwen 10.3%）。Qwen2.5-14B 在高 entropy subgroup 内也达 +4.8pp 但 aggregate 仅 -0.49pp 因 subgroup 太小。这 elegant 地解释了 regime 依赖于模型强度的原因。

**S4: 约束消融干净利落。** MAX-SAT vs count-only 803/804 一致，直接证明 Z3 solver 退化为加权计票。

**S5: Variable naming inconsistency 的具体发现（56.4% cross-answer constraint pairs share zero Z3 variables）** 提供了 mechanistic insight：Z3 无法从不相关符号集中发现逻辑关系。

**S6: Type C（error amplification, Δ=−2.83pp, p=0.0095）是新发现**，提供了 SICA 何时 actively harm 的边界条件。

**S7: 形式化完整。** 5 equations, 2 algorithms, full prompts, α=0.5 explicit。

**S8: 文献覆盖充分（~50 引用）。** Related Work 5 段覆盖所有主要研究线。关键先行工作均已引用并 positioned。

**S9: 写作质量好，无 AI 痕迹**（R2 独立验证：零 em-dash，零黑名单词汇，零 -ing phrase endings）。

**S10: Limitations 诚实详尽**（11 条）。

---

## Weaknesses

### Must-Fix (Critical) — 3 items

**W1 [数据不一致]: 跨章节 Δ 数值矛盾。**
*R2 W4 + Director D1。交叉共识：critical。*

Abstract、Introduction（含 Contribution #1）、Discussion、Conclusion 均报告 Mistral-7B PW-D5 Δ=−4.67pp (Introduction 还标注 n=303)。但 Table 1 和 Experiments §4.2 报告 Δ=−2.83pp (n=600, p=0.0095)。四个叙述章节保留了旧实验数据，表格已更新至全量结果。

审稿人发现此类矛盾会系统性降低对所有定量结论的信任。**必须统一。**

---

**W2 [CJT Framing Gap]: 标题声称 "trace independence limits" 但 Oracle 数据证明 constraint quality 是瓶颈。**
*Director D2。R2 交叉回应中从 significant 提升为 critical。*

Oracle 实验使用**完全相同的 correlated traces**，仅替换约束来源（gold vs self-extracted），gain 从 ~0pp 跳至 +14.22pp。这证明 trace independence 不是瓶颈——同样的 correlated traces 在 gold constraints 下完美工作。

论文内部证据也指向 constraint quality：8.2% discriminative rate（§6.2）、56.4% zero shared variables（§6.2）、entropy mechanism（§6.5）。CJT/κ/Eff-K 解释的是 SC plateau（为什么更多 traces 不能持续提升投票），不是 SICA 失败（为什么约束聚合无效）。

论文将两个不同现象混为一谈：(1) SC plateau（由 trace correlation 解释 → CJT），(2) SICA 失败（由 constraint quality 解释 → discriminative rate）。标题和 framing 应区分这两个层次。

R2 建议的修复方向：要么调整标题强调 constraint quality，要么明确论证 trace correlation 如何通过双通道（直接限制投票多样性 + 间接限制约束多样性）同时影响两种机制。

---

**W3 [Goldilocks Zone 证据窄]: 所有正面证据来自 1 模型 × 1 数据集（2/3 seeds）。**
*R1-F3 + R2 N1。交叉共识：critical。*

14 个非 oracle 条件中：
- Goldilocks zone (SC 50-55%): 4 条件中 2 显著、1 边缘、1 无效
- Type A (SC ≥60%): 7 条件全部无效
- Type C (SC ≤40%): 1 条件显著负面
- Degenerate: 2 条件

7 个模型中仅 Mistral-7B 落在 Goldilocks zone。同一 SC 范围的 LogiQA 完全无效（Type B）。Goldilocks zone 实际需要两个条件同时满足：(1) SC 50-55%, (2) domain is formalizable，后者大大缩小了适用范围。

R2："更像是对 Mistral-7B FOLIO 特定条件的 characterization，而非可泛化的 regime description"。

---

### Should-Fix — 5 items

**W4: 多重比较校正未讨论。**
*R1-F1。R2 评为 should-fix（非 critical），Director 同意。*

14 条件 Bonferroni 阈值 ~0.0036，最佳 p=0.013 不 survive。但 R2 论证：论文核心 claim 是 "regime-dependent pattern" 而非单一 p-value，由 replication (2/3 seeds) + entropy mechanism (+9.6pp) + discriminative rate (8.2% CI) 共同支撑。Type C 的负面结果 (p=0.0095) 同样不 survive Bonferroni。

**修复**：报告 corrected p-values，承认单一条件不 survive，论证 converging evidence。

---

**W5: Oracle σ(c,a) 语义仍有歧义。**
*R2 W2。*

§4.3 声称 "scoring function (Eq. 2) remains unchanged"，但 oracle 用 Z3 per-answer evaluation 而非 source-trace indicator。一句澄清即可："In the oracle variant, σ(c, a) is determined by Z3 evaluation of constraint c under answer a, rather than by source-trace provenance."

---

**W6: Discussion 引用未定义数字。**
*R2 W3。*

Discussion §7 第 1 段："Confirmation bias reaches 62.3% (Qwen2.5-14B), override precision drops to 28.6%"——这两个指标在正文 experiments/analysis 部分从未定义或首次出现。override precision 全文无定义。

---

**W7: Remediation 策略缺乏实现细节。**
*R1-F5 + R2 agree (should-fix)。*

Appendix Table A8 比前版改善，但 cross-model extraction (disc. rate=0%) 是 surprising null result，暗示问题不仅是 same-model bias，而是约束提取任务的结构性困难。值得至少一段展开讨论。

---

**W8: Eff-K 公式需归因 Kish (1965) 并 justify κ→ρ 替换。**
*R1-F2 + R2 agree (minor → should-fix)。*

κ（agreement corrected for chance）和 ρ（correlation）概念不同。论文用 Fleiss' κ 替代 Ladha 原始公式中的 ρ，这个替换需要 justify。

---

### Minor — 3 items

**W9**: "Four base architectures" 表述不准确（DeepSeek-R1-Distill/QwQ 均 Qwen 基础）。

**W10**: Appendix Table A2 含 Table 1 未包含的条件（ARC-Challenge, DeepSeek-R1-7B 等）——跨表不一致。

**W11**: Abstract 报告 best seed (+4.90pp) 未报告 3-seed mean (+2.61pp)。

---

## Questions for Authors

Q1: PW-D5 的正确 Δ 是 -4.67pp (n=303) 还是 -2.83pp (n=600)？

Q2: 如果 Holm-Bonferroni 校正后无条件保持显著，Goldilocks zone 是否应重新定位为 "observed trend" 而非 "confirmed zone"？

Q3: Oracle 用相同 correlated traces 获得 +14.22pp。这如何与标题 "trace independence limits" 兼容？请阐述 trace correlation 如何导致 constraint quality 下降的因果链。

Q4: Discussion 中 "confirmation bias reaches 62.3%" 和 "override precision drops to 28.6%" 的定义和来源？

Q5: Cross-model extraction (disc. rate=0%) 暗示问题超越 same-model bias。这对 "structural limitation" 结论有何影响？

---

## Missing References

- **Kish, L. (1965). Survey Sampling. Wiley.** — Eff-K 公式原始出处。
- 其余文献覆盖充分（~50 citations）。

---

## Overall Assessment

**评分: 3.0 (Findings)**

EMNLP 2026 ARR: 3 = Findings（可被 Findings 接收）。

### 评分理由

**支撑 Findings 的因素：**
- 实验覆盖系统全面（7 模型、4 域、2400+ 实例、3-seed 复制）
- 双 Oracle 控制是精巧的因果隔离，产生高度显著大效应
- Entropy-conditioned mechanism 是 elegant 的新贡献
- 约束消融（803/804）干净利落
- Variable naming inconsistency (56.4%) 是有 insight 的具体发现
- Type C error amplification 是新发现
- 形式化完整，文献充分，写作质量好，无 AI 痕迹

**阻止 3.5 (Borderline Conference) 的因素：**
- **数据不一致**（W1）：四个章节与 Table 1 数值矛盾，直接损害可信度
- **CJT framing gap**（W2）：标题与最强实验证据指向不同机制
- **Goldilocks zone 证据窄**（W3）：1 模型 × 1 域 × 2/3 seeds

**提升路径 (3.0 → 3.5)：**
R2 独立给出 3.5，条件为 W1 + W2 得到修复。修复 W1（统一数据）+ 解决 W2（调整标题/framing 或明确论证 trace correlation → constraint quality 的因果链）+ 在 abstract/intro 中诚实限定 W3（Goldilocks zone 证据范围）→ 可达 3.5 (Borderline Conference)。核心贡献（Oracle 控制 + entropy mechanism + failure taxonomy）在更精确的 framing 下将更加凸显。

---

## 与前版（"The Capability Trap"）改进评估

| 维度 | 前版 (3.0) | 修订版 | 改善幅度 |
|------|-----------|--------|---------|
| 核心 framing | 纯负面结果 | Regime-dependent + mechanism | ++ |
| Oracle | 1 dataset, +8.82pp | 2 datasets, +14.22/+11.50pp | ++ |
| Discriminative rate | 43 题, 无 CI | 804 题, [7.6, 8.8]% | +++ |
| 理论框架 | 无 | CJT/Eff-K + entropy | + |
| 引用 | ~41 | ~50 + CJT/formalization 线 | + |
| Positive evidence | 无 | Goldilocks zone (脆弱) | + |
| Replication | 无 | 3-seed (2/3) | + |
| Formalization | σ/α 缺失 | Eq.(1)-(5), Alg 1-2 | ++ |

修订版在几乎所有维度有实质性改进。残留问题（W1-W3）均可在一轮修订中解决。
