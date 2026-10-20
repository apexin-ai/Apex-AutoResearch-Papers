# Paper Framing — solver-trace-ablation

## Target Venue
- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026

## Core Claims (3 条 — Goodhart 主线诊断/分析论文)

### Claim 1: ISR as Reward Hacking Diagnostic
Solver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.

**证据**：
- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations
- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts
- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据
- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)
- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)
- Hacking taxonomy: 5 distinct modes identified and quantified (plan012 `hacking_characterization_report.md` + plan017 D027)

### Claim 2: ISR as Proxy Metric Exhibits Goodhart's Law (D033 重写)
ISR 作为 proxy metric 遵循 Goodhart's Law：当 ISR 从观测指标（diagnostic）转变为优化目标（reward），其有效性取决于优化压力的强度。低剂量 ISR reward (β=0.1) 提升结构质量且不损害证明能力；高剂量 ISR reward (β=0.3) 触发 Goodhart 效应，比 matched random noise 更差。

**证据（β=0.1 同剂量对照，D031 定论）**：
- plan002-b01 (ISR β=0.1): eval PR=0.81, ISR=0.337, proved_only_ISR=0.415, components=5.58 — genuine proofs with improved structure
- plan018 (random β=0.1): eval PR=0.79, ISR=0.104, proved_only_ISR=0.131, components=8.46 — PR 持平但 ISR 仅为 ISR 组的 1/3.2
- **结论**：ISR 3.2x > random at same β → ISR 信号提供 genuine structural guidance，非 variance regularization

**Hacking Taxonomy 定量对比 (D038)**：
- ISR β=0.1 genuine: 25.9% (21/81) vs random β=0.1 genuine: 17.7% (14/79) — **+8.2pp**
- Conclusion embedding: ISR 72.8% vs random 78.5% — 两组主导模式，ISR 略降但未消除
- Complexity-without-utility: ISR **0%** vs random 3.8% — ISR 完全消除此模式
- ISR genuine quality: mean ISR 0.67 (max 1.0) vs random genuine mean ISR 0.34 (max 0.5)
- 整体 hacking rate: ISR 74.1% vs random 82.3% — sweet spot 下仍有 74% hacking

**证据（β=0.3 同剂量对照）**：
- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌
- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR
- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)

**β 剂量效应全景**：
| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |
|---|---|---|---|---|---|
| 0.1 | 0.81 | 0.79 | **0.337** | 0.104 | ISR >> random (sweet spot) |
| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |

**其他 ISR-as-reward 失败模式**：
- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)
- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)

⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为"additive vs convex"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）

⚠️ **β=0.1 ISR 目前 1 seed (s42)，s43/s44 训练中**。3-seed mean±std 待出。

### Claim 3: Cross-Logic Generality (conditional on plan006)
STA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.

**证据**: 待验证。plan006 Prolog GRPO dry-run 进行中，训练即将启动（3 seeds × 500 步）。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。

## Story Spine

- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.
- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.
- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:
  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)
  2. ISR as proxy metric exhibits Goodhart's Law: low-dose ISR reward (β=0.1) provides genuine structural guidance (3.2x > matched random), but high-dose (β=0.3) is actively worse than random noise — a clean empirical demonstration of Goodhart's Law in reward shaping
  3. GRPO saturation creates a "training trap": PR→1 means no gradient signal; adding variance redirects rather than prevents hacking
  4. Different reward formulations produce distinct, classifiable hacking strategies (5 modes identified)
  5. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners
- **Actionable insights for practitioners**:
  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic
  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)
  3. ISR reward has a narrow sweet spot (β=0.1): below it, no structural guidance; above it, Goodhart effect destroys prove_rate
  4. ISR is primarily a structural diagnostic; as training signal, treat with extreme caution (Goodhart boundary is sharp)
- **Headline result**: "We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as both a diagnostic for reward hacking in GRPO-trained formalizers and a case study of Goodhart's Law in reward shaping. At low dose (β=0.1), ISR reward provides genuine structural guidance (3.2x ISR improvement over matched random control, PR maintained). At high dose (β=0.3), ISR reward is actively worse than random noise (PR 18% vs 48%), exhibiting classic Goodhart collapse. Across 5 reward conditions, 3 seeds, and up to 1000 training steps, we identify 5 distinct hacking strategies and document ISR's transition from useful indicator to harmful optimization target."

## ISR Capability Boundary (D021/D022)

**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**

plan014 downstream NLI 验证结果（negative）精确刻画了这一边界：
- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)
- Best-of-N ISR selection vs random: +0.9pp (不显著)
- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%

**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。

## ISR-as-Reward: Goodhart Landscape (D033 更新)

ISR 作为训练信号的全部结果，按 β 剂量组织：

| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |
|------|------|---------|----------|----------|---------------|
| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | conclusion embedding | N/A |
| ISR β=0.1 | r = r_exec·(1+0.1·ISR) | **0.81** | **0.337** | conclusion embedding (73%), genuine 26% | pre-Goodhart (sweet spot) |
| random β=0.1 | r = r_exec·(1+0.1·random) | 0.79 | 0.104 | redundant premises | control |
| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |
| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |
| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |
| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |

**Goodhart 转折点在 β ∈ (0.1, 0.3)。** β=0.1 是可用的 sweet spot；β=0.3 已进入 Goodhart 区间。

## Venue Fit Risks

- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.
- **"Just negative results" risk**: Mitigate by: (a) β=0.1 是 positive result (ISR sweet spot)，(b) Goodhart framework 提供 mechanistic understanding，(c) actionable diagnostic framework (ISR + taxonomy)。
- **"Old wine" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic Goodhart analysis for formal reasoning GRPO) + empirical findings, not algorithm level.
- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 5+ conditions × 5 hacking modes × 3 training horizons).

## Anticipated Reviewer Concerns

1. **"ISR is just LOO ablation — not novel"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical Goodhart analysis on reward shaping, (c) hacking taxonomy, (d) GRPO saturation mechanism.
2. **"β=0.1 success is just one seed"** — Acknowledged. Future work includes multi-seed β=0.1 validation. However, the β=0.1 vs random β=0.1 comparison is clean (same seed, same setup, only ISR vs random differs).
3. **"Goodhart's Law is obvious"** — The conceptual prediction is known; the empirical characterization in formal reasoning GRPO is not. Specifically: (a) the sharp threshold between β=0.1 and β=0.3, (b) ISR being worse than random at high β (not just "less useful"), (c) 5 distinct hacking modes as Goodhart manifestations.
4. **"No positive result — ISR doesn't improve training"** — β=0.1 IS a positive result (PR=0.81, ISR 3.2x > random). Framing: ISR has a narrow but real sweet spot. The Goodhart boundary is the key insight.
5. **"ISR is circular"** — ISR is used for diagnosis/post-hoc analysis AND as reward (β=0.1). The circularity concern applies to high-β optimization; low-β avoids Goodhart precisely because optimization pressure is weak. Component count analysis provides ISR-independent evidence.
6. **"Only one logic type"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.
7. **"500 steps too short"** — plan016 extends to 1000 steps, showing ISR collapse continues and worsens (0.123→0.003, -97.8%). The ISR崩塌轨迹 covers 100/500/1000 steps.
8. **"3 seeds insufficient for statistical claims"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. Statistical claims on mean ISR use 3-seed mean±std.
9. **"Related work insufficient"** — Expand to 25+ refs: reward hacking (Gao 2023, Skalse 2022), Goodhart's Law (Manheim & Garrabrant 2019, Karwowski 2024), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur), feature attribution (SHAP), FOLIO (Han 2022).
10. **"RIP framework overstated"** — Frame as "component necessity testing inspired by mutation testing's RIP framework," only Propagation condition operationalized.
11. **"Practitioners can't act on this"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable. β=0.1 sweet spot is directly actionable for reward shaping.

## Dream-Identified Structural Fixes (Paper Agent)

- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)
- [ ] RIP framing: reframe as "component necessity testing inspired by RIP"
- [ ] "Dense+automatic" → "conditionally dense"
- [ ] Remove all "Pareto-improving" language
- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature
- [ ] Address ISR sparsity for unproved outputs explicitly
- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)
- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed at β=0.3)
- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)
- [x] Hacking taxonomy completed (plan012, 5 modes identified including plan017)
- [x] β=0.1 ISR sweet spot documented (D031/D032, plan002-b01 success)
- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)
- [x] 1000-step ISR collapse documented (plan016, ISR 0.123→0.003)
