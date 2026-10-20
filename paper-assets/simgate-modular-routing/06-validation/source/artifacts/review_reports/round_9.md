---
round: 9
overall_score: borderline
timestamp: 2026-05-16T19:18:18.129634+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 9 审稿报告 — simgate-modular-routing

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Venue**: EMNLP 2026 Main Conference Long Paper (ARR May cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）
**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达共识）

---

## Summary

本文提出 episode-level counterfactual analysis 框架和 Death Avoidance Factor (DAF) 指标，分解 modular LLM agent 的 routing signal 来源。在 ScienceWorld（11/30 task types, N=245, Qwen2.5-7B-Instruct）上发现 78.9% 的 non-tie routing labels 由 death asymmetry 驱动，DAF=90.4%（P=100）。Trained router 在 held-out episodes 上低于 chance baseline（47.1% vs 50%）。跨环境分析（MATH N=300, ALFWorld N=135）和跨模型复制（Llama-3.1-8B, N=70）提供辅助证据。

---

## Strengths

**S1. 问题定位精准。** 在 routing 文献集中于"如何 route"时，退后一步问"什么驱动 routing signal"——是被忽视的元问题，具有方法论价值。

**S2. 框架设计简洁可复现。** Algorithm 1 完备无歧义，仅需 paired episode outcomes，environment-agnostic 属性通过三个结构迥异环境得到演示。

**S3. 统计报告诚实严谨。** p=0.079 始终标注 "not reaching α=0.05"，r=0.97 标注 "partly structural"，Bootstrap/LOO/Spearman 三重 robustness，8-seed cross-split evaluation。

**S4. 多层次 robustness 检验。** LOO (r: 0.963-0.980), Spearman ρ=0.986, 10K bootstrap, penalty sweep (P=10-500), reasoning-depth ablation, data scaling (25%-800%), capacity scaling (0.6B-4B), cross-model replication。

**S5. Negative result 呈现诚实且有建设性。** Router diagnostic 清晰展示 always-deterministic 的 trivial near-optimality，对社区有建设性信息。

**S6. Limitations 坦诚具体。** 19/30 exclusion, penalty amplification, single-pass ReAct, distribution shift (DAgger), 7-8B scale limitation 均明确列出。

---

## Weaknesses

### Must-Fix (Critical)

**W1. DAF=90.4% headline number 被 penalty magnitude 机械放大 [Consensus]**
- DAF = δP/(δP + Δ_nd) 是 P 的单调递增函数。在 P=100 时 90.4% 接近同义反复（"当 penalty 是 score gap 的 35 倍时，penalty 项主导总 gap"）。P=10 时仅 50.4%。
- 78.9% penalty-independent metric 更稳健但仍处于从属位置。
- 论文自承 "mathematical consequence, not empirical finding"（§3.4），但 Abstract/Conclusion 的 framing 仍以 DAF 为核心卖点。
- **要求**：将 78.9% death-asymmetry label fraction 提升为 PRIMARY quantitative claim；或论证 P=100 具有外部效度（typical catastrophic penalty magnitude across environments）。

**W2. r=0.97 结构性耦合呈现不足 [Consensus]**
- 当 DAF=90.4%（即 Δ_full ≈ δ·P），Corr(δ, δ·P + ε) → 1 是代数必然。
- Abstract 标 "partly structural" 不够——应为 "largely a mathematical consequence of death dominance"。Conclusion 完全未提及。
- Partial correlation（控制 δ·P）预计 r ≈ 0，证实这不是独立经验证据。
- **要求**：Conclusion 加强 qualifier；或将 r=0.97 从 Contribution-level claim 降级为 robustness diagnostic。

**W3. Cross-env "validation" 近循环 [Consensus]**
- MATH（无 death → 无 death signal）是 absence-of-evidence，不是 positive replication。ALFWorld 识别不同 mechanism 但不验证 DAF 量化能力。
- 真正的 validation 需要第二个有 catastrophic failure 的环境（如 NetHack/Crafter）重现 similar DAF。
- Contribution 3 标为 "cross-context validation" 属 overselling。
- **要求**：重新定性为 "framework applicability demonstration"；或补充第二个 death-penalty 环境数据。

**W4. Data scaling ablation 用 augmentation 代替真实数据 [Consensus]**
- Paraphrase augmentation 不等比例放大 majority class（89.6%→97.7%），不创造新 routing patterns。
- 无法区分 "signal 不存在" 和 "augmentation 无法创造 signal"。论文自估需 ~1,350 真实 pairs 但未执行。
- **要求**：弱化为 "augmentation-based scaling provides no improvement; real-data scaling (requiring ~1,350 episode pairs for 50 minority-class examples) remains open"。

### Should-Fix (Warning)

**W5. Capacity scaling: 3 个不可比数据点 [Consensus]**
- 0.6B=50.67%, 1.7B=47.1%, 4B=58.96%——非单调。1.7B 用 8 seeds vs 4 seeds for others。仅 4B 一个点超越 baseline。
- "Capacity-dependent limitation" 结论单薄。

**W6. MATH p=0.079 underpowered [Consensus]**
- Post-hoc power 估计 ~42%。Non-significance 可能纯粹因为 insufficient N。
- 应报告 power analysis 或 TOST equivalence test。

**W7. Llama replication (N=70, 0 internal-preferred) 不足 [Consensus]**
- 零 minority-class observations → 只能说 "death-rate asymmetry direction generalizes"，不能说 "framework generalizes"。

**W8. Bootstrap CI 在结构耦合下 overconfident [Consensus]**
- CI [0.952, 0.995] 度量 sampling variance，不度量 external validity（换一组 task types 是否成立）。

**W9. Over-generalization: Abstract/Conclusion qualifier 不够突出 [R2 raised, R1 partially agrees]**
- "In environments with catastrophic failure modes" qualifier 存在但可能在快速阅读中被遗漏。

**W10. "Internal modality" 混淆 hallucination 与 reasoning [Consensus]**
- 如果 "internal + observation verification" 降低 death rate 至 ~16%，DAF 会 collapse。
- 真正 bottleneck 可能是 observation accuracy 而非 computation mode——缺 verification ablation。

### Nice-to-Fix (Info)

**W11.** 术语不一致：modality/strategy/computation type 混用。
**W12.** 78.9%（label-level）与 90.4%（score-level）并列时语义不清。
**W13.** SCI=0.2147 缺 null distribution baseline。

---

## Reviewer Consensus

两位 Reviewer 在以下关键判断上完全一致 [AGREE]：
1. DAF headline framing 存在 penalty-parameter 机械放大问题
2. r=0.97 大部分是结构性耦合的数学必然
3. Cross-env evidence 是 absence-of-evidence 而非 positive validation
4. Data scaling augmentation 不能替代 real-data scaling
5. 方法论框架本身（Algorithm 1 + DAF + counterfactual labeling）是 solid 的
6. Negative result（router fails）有 community value
7. 统计报告和 robustness checks 质量高
8. 论文处于 Findings track / borderline 水平

---

## Reviewer Divergence

| 问题 | R1 | R2 | Director 判定 |
|------|----|----|--------------|
| "Routing reduces to safety-first selection" 是否 overclaim | 部分反驳——论文有 qualifier | Critical overclaim | **Warning**：qualifier 存在但不够突出 |
| "Obvious observation" 低估贡献 | 反驳——framework+量化+negative result 三层贡献 | 核心 insight 可能不够 surprising | 采纳 R1：量化精度和诊断框架是非 trivial 贡献 |
| Figure/Table 信息密度 | 反驳——8页限制下正常做法 | 提出改进建议 | Minor，不影响接收 |
| EMNLP audience fit | 反驳——*CL 有先例 | 存在张力但不 disqualifying | 不构成问题 |
| 63% tasks excluded | — | 部分反驳——有 anti-cherry-picking 证据 | 排除有方法论正当性，但 generalization 担忧成立 |

---

## Questions（需作者回应）

**Q1.** Partial correlation (控制 δ·P 后) 的 residual r 是多少？如果 ≈ 0，r=0.97 应如何重新定位？

**Q2.** 如果 "internal + observation verification"（每步后 call environment 确认 state），预计 death rate 降到多少？这是否使 DAF 大幅下降？

**Q3.** 能否在 NetHack/Crafter 等有 catastrophic failure 的第二环境复现 DAF？

**Q4.** MATH 实验 post-hoc power 是多少？是否 sufficient to detect effect < 5pp？

**Q5.** P=100 在 ScienceWorld score range (0-100 normalized) 中处于什么位置？这对 DAF 的 external validity 意味着什么？

**Q6.** 1.7B vs 0.6B 的非单调结果（47.1% < 50.67%）是否由配置差异（8 seeds vs 4 seeds）解释？

---

## Missing References

- **Lakens 2017** — Equivalence testing (TOST) for non-significant results
- **Cohen 1988 / Brysbaert & Stevens 2018** — Power analysis reporting standards
- **AgentBench** (Liu et al., 2023) — Multi-environment LLM agent benchmark
- **WebArena** (Zhou et al., 2024) — Interactive web environment with failure modes
- **LATS** (Zhou et al., 2023) — Language Agent Tree Search
- **Safe RLHF** (Dai et al., 2024) — Catastrophic failure in safety alignment
- **ToolBench** (Qin et al., 2023) — Tool use benchmark with failure modes
- **MINT** (Wang et al., 2024) — Multi-turn interactive evaluation

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置中未检测到 `external_review.paperreview_ai.enabled: true`）。

---

## Overall Assessment

**评分**: borderline (3.0/5)
**置信度**: 4/5

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 3.0 | 3.0 |
| Reproducibility | 4.0 | 4.5 | 4.25 |
| Overall | 3.0 | 3.0 | **3.0** |

**综合判断**：方法论框架设计 solid（Algorithm 1 + DAF 指标简洁可复现），统计报告诚实严谨（robustness checks 充分），negative result 对社区有建设性。但存在 4 个 Critical 问题：(1) 核心 quantitative claim 的 magnitude 由 environment parameter 控制而非 empirical discovery；(2) r=0.97 的独立经验证据性被高估；(3) "cross-context validation" 本质是 absence-of-evidence；(4) data scaling ablation 无法区分 signal absence 和 method limitation。这些共同削弱了论文的 informativeness 和 generalizability。

**可接收路径**：修复 W1-W4 的 framing/claim 问题（无需新实验，纯 writing），将论文定位为 "single-environment case study + diagnostic framework proposal"，降低泛化声称，r=0.97 和 DAF 给予正确数学定性。如此可达 weak accept 水平。如果能补充第二个 death-penalty 环境数据，可进一步提升至 accept。

---

## Detailed Comments

### Abstract
- "DAF = 90.4%" 应降级，以 "78.9% of non-tie routing labels are driven by death asymmetry (penalty-independent)" 为 lead
- "partly structural" → "largely a mathematical consequence" 或更长 explanation
- 最后一句 "routing problem reduces to safety-first modality selection" 需加 "in environments with catastrophic failure modes" qualifier（当前版本已有 "in environments with catastrophic failure modes" 但结构上不够突出）

### §3.4 (DAF Definition)
- 明确：DAF 的 informativeness 在于 **给定环境 penalty 设定下** 的 routing signal 构成，而非跨环境 universal law
- 考虑添加 "DAF should be interpreted relative to the environment's penalty magnitude" 的显式 caveat

### §4.1 (Death Decomposition)
- r=0.97 需要更强的结构性耦合说明：当 Var(P·Δ_d) ≫ Var(Δ_nd) 时 high correlation 是 mathematical given，而论文数据恰好满足此条件
- §4.1 当前 3-sentence caveat 是 R8 修改的结果——但 Abstract/Conclusion 未同步到位

### §4.3 (Router Diagnostic)
- Data scaling 结论需弱化：明确区分 "step-level scarcity (ruled out)" vs "episode-level minority-class diversity (open question requiring ~1,350 real pairs)"
- Capacity scaling 非单调性需 acknowledge——当前 Table 8 caption 有 caveat 但正文表述过于 confident

### §5 (Discussion)
- "Cross-environment evidence" 段：MATH 从 "validation" 重新定性为 "consistent with framework prediction (no death → no death signal)"
- Framework applicability 段的 qualifier 应 propagate 到 Abstract 和 Conclusion

### Contribution 3
- "Cross-context validation" → "Cross-context applicability demonstration"
- 当前 evidence 支持 "framework correctly identifies different mechanisms in different environments"，不支持 "DAF quantification generalizes"