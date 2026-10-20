# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：β=0.1 sweet spot 方向性复现但效应量缩水或 variance 大；Prolog 部分成功或未完成。Claim 1 完整，Claim 

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/7f0e565e-ca1c-4dc0-98bc-81794254a884.jsonl`
- **Structured JSON:** [`6969f4d860294dcffc7a.json`](../../sessions/69/6969f4d860294dcffc7a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T09:37:20.602Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T09:37:20.602Z",
  "sessionId": "7f0e565e-ca1c-4dc0-98bc-81794254a884",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：β=0.1 sweet spot 方向性复现但效应量缩水或 variance 大；Prolog 部分成功或未完成。Claim 1 完整，Claim 2 需弱化置信度，Claim 3 降级。\n核心假设：['s43/s44 至少 1 个复现方向（ISR > random），但另一个效应弱或 PR 下降', '3-seed ISR/random ratio 1.3–2.5x，置信区间可能跨 1', 'Prolog 训练收敛但 hacking 模式不清晰，或 ISR 诊断力弱于 FOL', 'β=0.1 genuine rate delta 缩至 2–5pp，不再显著', 'exec-only 3-seed ISR 崩塌轨迹仍然稳健（这是 Claim 1 的基础）']\n关键指标范围：{'three_seed_isr_b01_mean_isr': [0.18, 0.3], 'three_seed_isr_b01_mean_pr': [0.6, 0.8], 'three_seed_random_b01_mean_isr': [0.1, 0.2], 'three_seed_isr_over_random_ratio': [1.3, 2.5], 'three_seed_genuine_rate_delta_pp': [1.0, 5.0], 'three_seed_isr_b01_std': [0.08, 0.15], 'prolog_exec_only_pr': [0.4, 0.75], 'prolog_hacking_detectable': ['unclear', 'partial']}\n叙事方向：Claim 1（ISR 诊断）不受影响——ISR 崩塌轨迹和 hacking taxonomy 已有 3-seed 多条件数据。 Claim 2 调整：sweet spot 存在但 fragile——\"ISR β=0.1 shows directional improvement over  matched random (mean ratio ~1.8x) but high inter-seed variance suggests the sweet spot  is narrow and sensitive to initialization.\" 弱化 \"3.2x\" 为 mean±std 报告，不做显著性声明， 改为 effect size + 方向性论述。Claim 3 降为 \"Preliminary Evidence\" 或 Future Work。 论文重心从三线并行收缩为 Claim 1（诊断）+ Claim 2（Goodhart 案例研究，含不确定性讨论）。 增补 seed-variability 本身作为发现（\"same setup, 3 seeds, 3 different hacking strategies\"） 强化 GRPO 不稳定性论点。仍投 EMNLP main，但 scope 收窄。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: solver-trace-ablation\n\n## paper_framing.md\n\n# Paper Framing — solver-trace-ablation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\n\n### Claim 1: ISR as Reward Hacking Diagnostic\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\n\n**证据**：\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\n- Hacking taxonomy: 5 distinct modes identified and quantified (plan012 `hacking_characterization_report.md` + plan017 D027)\n\n### Claim 2: ISR as Proxy Metric Exhibits Goodhart's Law (D033 重写)\nISR 作为 proxy metric 遵循 Goodhart's Law：当 ISR 从观测指标（diagnostic）转变为优化目标（reward），其有效性取决于优化压力的强度。低剂量 ISR reward (β=0.1) 提升结构质量且不损害证明能力；高剂量 ISR reward (β=0.3) 触发 Goodhart 效应，比 matched random noise 更差。\n\n**证据（β=0.1 同剂量对照，D031 定论）**：\n- plan002-b01 (ISR β=0.1): eval PR=0.81, ISR=0.337, proved_only_ISR=0.415, components=5.58 — genuine proofs with improved structure\n- plan018 (random β=0.1): eval PR=0.79, ISR=0.104, proved_only_ISR=0.131, components=8.46 — PR 持平但 ISR 仅为 ISR 组的 1/3.2\n- **结论**：ISR 3.2x > random at same β → ISR 信号提供 genuine structural guidance，非 variance regularization\n\n**Hacking Taxonomy 定量对比 (D038)**：\n- ISR β=0.1 genuine: 25.9% (21/81) vs random β=0.1 genuine: 17.7% (14/79) — **+8.2pp**\n- Conclusion embedding: ISR 72.8% vs random 78.5% — 两组主导模式，ISR 略降但未消除\n- Complexity-without-utility: ISR **0%** vs random 3.8% — ISR 完全消除此模式\n- ISR genuine quality: mean ISR 0.67 (max 1.0) vs random genuine mean ISR 0.34 (max 0.5)\n- 整体 hacking rate: ISR 74.1% vs random 82.3% — sweet spot 下仍有 74% hacking\n\n**证据（β=0.3 同剂量对照）**：\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\n\n**β 剂量效应全景**：\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\n|---|---|---|---|---|---|\n| 0.1 | 0.81 | 0.79 | **0.337** | 0.104 | ISR >> random (sweet spot) |\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\n\n**其他 ISR-as-reward 失败模式**：\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\n\n⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\"additive vs convex\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\n\n⚠️ **β=0.1 ISR 目前 1 seed (s42)，s43/s44 训练中**。3-seed mean±std 待出。\n\n### Claim 3: Cross-Logic Generality (conditional on plan006)\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\n\n**证据**: 待验证。plan006 Prolog GRPO dry-run 进行中，训练即将启动（3 seeds × 500 步）。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。\n\n## Story Spine\n\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\n  2. ISR as proxy metric exhibits Goodhart's Law: low-dose ISR reward (β=0.1) provides genuine structural guidance (3.2x > matched random), but high-dose (β=0.3) is actively worse than random noise — a clean empirical demonstration of Goodhart's Law in reward shaping\n  3. GRPO saturation creates a \"training trap\": PR→1 means no gradient signal; adding variance redirects rather than prevents hacking\n  4. Different reward formulations produce distinct, classifiable hacking strategies (5 modes identified)\n  5. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\n- **Actionable insights for practitioners**:\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\n  3. ISR reward has a narrow sweet spot (β=0.1): below it, no structural guidance; above it, Goodhart effect destroys prove_rate\n  4. ISR is primarily a structural diagnostic; as training signal, treat with extreme caution (Goodhart boundary is sharp)\n- **Headline result**: \"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as both a diagnostic for reward hacking in GRPO-trained formalizers and a case study of Goodhart's Law in reward shaping. At low dose (β=0.1), ISR reward provides genuine structural guidance (3.2x ISR improvement over matched random control, PR maintained). At high dose (β=0.3), ISR reward is actively worse than random noise (PR 18% vs 48%), exhibiting classic Goodhart collapse. Across 5 reward conditions, 3 seeds, and up to 1000 training steps, we identify 5 distinct hacking strategies and document ISR's transition from useful indicator to harmful optimization target.\"\n\n## ISR Capability Boundary (D021/D022)\n\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\n\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\n\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\n\n## ISR-as-Reward: Goodhart Landscape (D033 更新)\n\nISR 作为训练信号的全部结果，按 β 剂量组织：\n\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\n|------|------|---------|----------|----------|---------------|\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | conclusion embedding | N/A |\n| ISR β=0.1 | r = r_exec·(1+0.1·ISR) | **0.81** | **0.337** | conclusion embedding (73%), genuine 26% | pre-Goodhart (sweet spot) |\n| random β=0.1 | r = r_exec·(1+0.1·random) | 0.79 | 0.104 | redundant premises | control |\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\n\n**Goodhart 转折点在 β ∈ (0.1, 0.3)。** β=0.1 是可用的 sweet spot；β=0.3 已进入 Goodhart 区间。\n\n## Venue Fit Risks\n\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\n- **\"Just negative results\" risk**: Mitigate by: (a) β=0.1 是 positive result (ISR sweet spot)，(b) Goodhart framework 提供 mechanistic understanding，(c) actionable diagnostic framework (ISR + taxonomy)。\n- **\"Old wine\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic Goodhart analysis for formal reasoning GRPO) + empirical findings, not algorithm level.\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 5+ conditions × 5 hacking modes × 3 training horizons).\n\n## Anticipated Reviewer Concerns\n\n1. **\"ISR is just LOO ablation — not novel\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical Goodhart analysis on reward shaping, (c) hacking taxonomy, (d) GRPO saturation mechanism.\n2. **\"β=0.1 success is just one seed\"** — Acknowledged. Future work includes multi-seed β=0.1 validation. However, the β=0.1 vs random β=0.1 comparison is clean (same seed, same setup, only ISR vs random differs).\n3. **\"Goodhart's Law is obvious\"** — The conceptual prediction is known; the empirical characterization in formal reasoning GRPO is not. Specifically: (a) the sharp threshold between β=0.1 and β=0.3, (b) ISR being worse than random at high β (not just \"less useful\"), (c) 5 distinct hacking modes as Goodhart manifestations.\n4. **\"No positive result — ISR doesn't improve training\"** — β=0.1 IS a positive result (PR=0.81, ISR 3.2x > random). Framing: ISR has a narrow but real sweet spot. The Goodhart boundary is the key insight.\n5. **\"ISR is circular\"** — ISR is used for diagnosis/post-hoc analysis AND as reward (β=0.1). The circularity concern applies to high-β optimization; low-β avoids Goodhart precisely because optimization pressure is weak. Component count analysis provides ISR-independent evidence.\n6. **\"Only one logic type\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\n7. **\"500 steps too short\"** — plan016 extends to 1000 steps, showing ISR collapse continues and worsens (0.123→0.003, -97.8%). The ISR崩塌轨迹 covers 100/500/1000 steps.\n8. **\"3 seeds insufficient for statistical claims\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. Statistical claims on mean ISR use 3-seed mean±std.\n9. **\"Related work insufficient\"** — Expand to 25+ refs: reward hacking (Gao 2023, Skalse 2022), Goodhart's Law (Manheim & Garrabrant 2019, Karwowski 2024), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur), feature attribution (SHAP), FOLIO (Han 2022).\n10. **\"RIP framework overstated\"** — Frame as \"component necessity testing inspired by mutation testing's RIP framework,\" only Propagation condition operationalized.\n11. **\"Practitioners can't act on this\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable. β=0.1 sweet spot is directly actionable for reward shaping.\n\n## Dream-Identified Structural Fixes (Paper Agent)\n\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\n- [ ] RIP framing: reframe as \"component necessity testing inspired by RIP\"\n- [ ] \"Dense+automatic\" → \"conditionally dense\"\n- [ ] Remove all \"Pareto-improving\" language\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\n- [ ] Address ISR sparsity for unproved outputs explicitly\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed at β=0.3)\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\n- [x] Hacking taxonomy completed (plan012, 5 modes identified including plan017)\n- [x] β=0.1 ISR sweet spot documented (D031/D032, plan002-b01 success)\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\n- [x] 1000-step ISR collapse documented (plan016, ISR 0.123→0.003)\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: FOL single-logic GRPO, execution-only reward (500 steps, K=8, 3 seeds)\n    — baseline for STA comparison\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: plan001-exec-only-s43-r4\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_sampling_prove_rate: 0.14\n    eval_sampling_mean_isr: 0\n    eval_sampling_n_proved: 14\n    eval_sampling_temperature: 0.7\n    eval_sampling_method: do_sample=True, temperature=0.7\n    eval_sampling_by_answer:\n      'true':\n        count: 34\n        proved: 6\n        prove_rate: 0.176\n      'false':\n        count: 25\n        proved: 2\n        prove_rate: 0.08\n      unknown:\n        count: 41\n        proved: 6\n        prove_rate: 0.146\n- id: plan_002\n  claim: 2\n  description: 'FOL single-logic GRPO, additive ISR bonus: r = r_exec · (1 + β·ISR),\n    β∈{0.1, 0.3, 0.5}. 先跑 β=0.3 单 seed 验证方向，成功再 3-seed。旧凸组合公式 (α·r_exec + β·r_exec·ISR,\n    α+β=1) 已废弃——ISR<1 时永远是 penalty (plan005 confirmed)。 新公式确保 ISR 只能 bonus 不能 penalty。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: plan002-additive-b03-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 56.7\n    overall_prove_rate: 0.34025\n    overall_isr: 0.11527\n    first20_prove_rate: 0.15625\n    last50_prove_rate: 0.555\n    last100_prove_rate: 0.5525\n    mean_loss: 0.008914\n    last100_loss: 0.014469\n    parse_rate: 1\n    w1_50_prove_rate: 0.13\n    w51_100_prove_rate: 0.095\n    w101_200_prove_rate: 0.185\n    w201_300_prove_rate: 0.375\n    w301_400_prove_rate: 0.47625\n    w401_500_prove_rate: 0.5525\n    steps_ge_085: 52\n    first_step_ge_085: 46\n    final_prove_rate: 1\n    final_isr_mean: 0.3089\n    final_reward_mean: 1.0927\n- id: plan_003\n  claim: 1\n  description: 'FOL held-out evaluation: compare plan_001 vs plan_002 checkpoints\n    on test set using identical full STA metrics (prove_rate, ISR, ISR/PR ratio, hacking\n    taxonomy annotation)'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_002\n  registry_id: plan003-eval-exec-only-r5\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.32\n    mean_isr: 0.2055\n    isr_std: 0.3194\n    proved_only_isr: 0.6423\n    isr_by_type:\n      'true': 0.3598\n      'false': 0.1723\n      unknown: 0.0979\n    total_samples: 100\n    proved_count: 32\n    runtime_s: 251.7\n- id: plan_004\n  claim: 1\n  description: 'STA O(1) vs O(N) ablation: rerun exec+STA with fast_isr_fol to confirm\n    O(1) ineffectiveness at scale (500 steps, 1 seed) — negative result documentation'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n- id: plan_005\n  claim: 1\n  description: 'STA reward weight ablation: test α/β ratios (0.3/0.7, 0.5/0.5, 0.7/0.3)\n    + sigmoid curriculum vs fixed — isolate optimal STA integration'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: plan005-sta-low-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 71\n    parse_rate: 1\n    overall_prove_rate: 0.5657\n    overall_isr: 0.1682\n    last50_prove_rate: 0.77\n    last50_isr: 0.2559\n    last100_prove_rate: 0.7725\n    last100_isr: 0.2299\n    last100_loss: 0.022752\n    overall_loss: 0.017296\n    last100_isr_pr_ratio: 0.298\n    last100_isr_lt_pr_count: 99/100\n    first_rolling10_pr_ge_0.8: 178\n    first_rolling10_pr_ge_0.9: 439\n    max_rolling10_pr: 0.9375\n    max_rolling10_isr: 0.3282\n    windowed:\n      1-50:\n        pr: 0.1775\n        isr: 0.0906\n      51-100:\n        pr: 0.1775\n        isr: 0.0835\n      101-200:\n        pr: 0.5062\n        isr: 0.1463\n      201-300:\n        pr: 0.6713\n        isr: 0.1791\n      301-400:\n        pr: 0.7013\n        isr: 0.1984\n      401-500:\n        pr: 0.7725\n        isr: 0.2299\n- id: plan_006\n  claim: 3\n  description: 'Prolog single-logic GRPO: exec-only vs exec+STA (500 steps, K=8, 3\n    seeds) — second logic type validation. Dream M3: must have 3 seeds for cross-logic\n    claim.'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  notes: Requires Prolog STA instantiation (rule ablation). SWI-Prolog already installed.\n    Upgraded from 1→3 seeds per Dream feedback.\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Multi-logic GRPO (FOL+Prolog): exec-only vs exec+STA (500 steps, K=8,\n    1 seed) — cross-logic transfer test'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - plan_006\n  status: planned\n- id: plan_008\n  claim: 3\n  description: 'Cross-logic transfer evaluation: FOL-trained model on Prolog tasks\n    and vice versa'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_006\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'SFT baseline: supervised finetuning on same data (FOLIO 500), compare\n    with GRPO variants'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n- id: plan_010\n  claim: 3\n  description: 'SMT-LIB single-logic GRPO: exec-only vs exec+STA — third logic type'\n  priority: P2\n  gpu_budget_hours: 3\n  deps: []\n  notes: Requires SMT-LIB STA instantiation (constraint ablation). Z3 already installed.\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Qwen3-8B scaling: full MLSR on 8B model (1 seed) — model scale effect'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - plan_005\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Hacking characterization: manual annotation of 200 outputs per condition,\n    categorized by extensional-shortcut taxonomy'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n- id: plan_013\n  claim: 2\n  description: 'Random reward baseline: replace ISR with random structural penalty\n    on proved outputs (r = α·r_exec + β·r_exec·random[0,1]) to isolate ISR-specific\n    signal from multi-objective regularization effect. Dream M2/W7 mandatory.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'Dream cross-tier consensus: without this, cannot claim ISR formulation matters\n    vs any penalty.'\n  registry_id: plan013-random-reward-s42-r4\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 1\n    eval_mean_isr: 0.535\n    eval_isr_std: 0.1282\n    eval_proved_only_isr: 0.535\n    eval_median_isr: 0.5\n    eval_n_proved: 100\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_note: 'DEGENERATE: model generates trivial 2-component proofs (premise=conclusion,\n      conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure'\n- id: plan_014\n  claim: 1\n  description: 'Downstream validation: evaluate high-ISR vs low-ISR formalizations\n    on independent logical inference task (e.g., entailment accuracy using generated\n    FOL as premises). Breaks ISR circularity. Dream M2/W4 mandatory.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Dream cross-tier consensus: optimizing ISR + evaluating ISR = circular.\n    Need external criterion.'\n  registry_id: plan014-downstream-nli-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 0.341\n    proved_rate: 0.915\n    proved_count: 732\n    total_generations: 800\n    parse_errors: 0\n    accuracy_by_label:\n      'true': 0.912\n      'false': 0\n      unknown: 0.076\n    spearman_rho: -0.049\n    spearman_p: 0.187\n    mann_whitney_U: 17202\n    mann_whitney_p: 0.288\n    bon_isr_accuracy: 0.35\n    bon_random_accuracy: 0.341\n    bon_oracle_accuracy: 0.44\n    bon_prove_first_accuracy: 0.35\n    isr_bucket_high_acc: 0.75\n    isr_bucket_mid_acc: 0.377\n    isr_bucket_low_acc: 0.327\n    runtime_inference_s: 408.8\n    runtime_eval_s: 13.6\n- id: plan_015\n  claim: 1\n  description: 'Curriculum ablation: linear ramp vs sigmoid vs fixed weighting. Sigmoid\n    is load-bearing (best config) but not ablated. Dream m4.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_005\n  notes: Test linear ramp with same midpoint as sigmoid. Also vary midpoint (step\n    100/200/300 of 500).\n  status: planned\n- id: plan_016\n  claim: 1\n  description: 'Extended training horizon: run best config (from plan_005) to 1000+\n    steps to show convergence or persistence of STA benefit. Dream m6/W9.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - plan_005\n  notes: Both Dream tiers flag 500 steps as insufficient. Need evidence of convergence.\n  registry_id: plan016-extended-1000-s42\n  status: DONE\n  conclusion: success\n  metrics:\n    train:\n      total_steps: 1000\n      duration_min: 146\n      final_prove_rate: 0.8396\n      final_mean_isr: 0.0503\n      train_loss: 0.0125\n      epoch: 4\n      windowed:\n        steps_001_100:\n          pr: 0.19\n          isr: 0.0859\n        steps_101_200:\n          pr: 0.66\n          isr: 0.1115\n        steps_201_300:\n          pr: 0.838\n          isr: 0.0985\n        steps_301_400:\n          pr: 0.907\n          isr: 0.054\n        steps_401_500:\n          pr: 0.927\n          isr: 0.0433\n        steps_501_600:\n          pr: 0.963\n          isr: 0.0408\n        steps_601_700:\n          pr: 0.965\n          isr: 0.02\n        steps_701_800:\n          pr: 0.988\n          isr: 0.0178\n        steps_801_900:\n          pr: 0.978\n          isr: 0.017\n        steps_901_1000:\n          pr: 0.981\n          isr: 0.0144\n    eval:\n      prove_rate: 0.96\n      n_proved: 96\n      n_problems: 100\n      mean_isr: 0.0027\n      isr_std: 0.0118\n      median_isr: 0\n      proved_only_mean_isr: 0.0028\n      min_isr: 0\n      max_isr: 0.0588\n      isr_0_ratio: 0.9479\n      isr_1_ratio: 0\n      component_count_mean: 18.55\n      component_count_2_ratio: 0\n      mean_n_necessary: 0.052\n      n_necessary_0_ratio: 0.9479\n      tautological_collapse: false\n      by_answer_type:\n        'false':\n          count: 29\n          proved: 26\n          prove_rate: 0.8966\n          mean_isr: 0\n        unknown:\n          count: 31\n          proved: 30\n          prove_rate: 0.9677\n          mean_isr: 0.0053\n        'true':\n          count: 40\n          proved: 40\n          prove_rate: 1\n          mean_isr: 0.0026\n      eval_time_seconds: 396.3\n- id: plan_017\n  claim: 2\n  description: 'Additive random control: r = r_exec · (1 + β·random[0,1]), β=0.3.\n    Matched control for plan_002 — isolates ISR structural signal from pure variance\n    regularization. If ISR > random > exec-only, both signal and regularization contribute.\n    If ISR > random ≈ exec-only, ISR signal is key. If ISR ≈ random, ISR has no value\n    beyond regularization.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'D012: Reviewer-required control for GRPO saturation confound. Must match\n    plan_002 exactly (same β=0.3, same data, same steps) except random replaces ISR.'\n  registry_id: plan017-additive-random-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.48\n    eval_mean_isr: 0.0453\n    eval_isr_std: 0.0759\n    eval_median_isr: 0\n    eval_max_isr: 0.2857\n    eval_proved_only_isr: 0.0943\n    eval_n_proved: 48\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 9.6\n    eval_component_count_2_ratio: 0\n    eval_isr_pr_ratio: 0.0943\n    eval_elapsed_s: 542.3\n    eval_by_type_false_pr: 0.32\n    eval_by_type_false_isr: 0.0254\n    eval_by_type_unknown_pr: 0.51\n    eval_by_type_unknown_isr: 0.0518\n    eval_by_type_true_pr: 0.56\n    eval_by_type_true_isr: 0.052\n    tautological_collapse: false\n- id: plan_018\n  claim: 2\n  description: Additive random control β=0.1, matched to plan002-b01. r = r_exec ·\n    (1 + 0.1·random[0,1]). Same β as plan002-b01 (ISR β=0.1) for fair comparison.\n    If ISR β=0.1 >> random β=0.1 → ISR signal has structural value at low dose. If\n    ISR ≈ random → ISR is just variance regularization even at low dose.\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'D031: Urgent control experiment. plan002-b01 (ISR β=0.1) showed unexpected\n    success (PR=0.81, ISR=0.337). Need matched random control at same β to confirm\n    ISR signal vs noise.'\n  registry_id: plan018-additive-random-b01-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.79\n    eval_mean_isr: 0.1038\n    eval_isr_std: 0.1369\n    eval_median_isr: 0.0357\n    eval_proved_only_isr: 0.1314\n    eval_n_proved: 79\n    eval_n_problems: 100\n    eval_component_count_mean: 8.46\n    eval_component_count_median: 8\n    eval_component_count_2_ratio: 0\n    eval_isr_1_ratio: 0\n    eval_isr_0_ratio: 0.367\n    eval_isr_gt0_ratio: 0.633\n    eval_by_type_false_pr: 0.8\n    eval_by_type_false_isr: 0.1318\n    eval_by_type_unknown_pr: 0.7317\n    eval_by_type_unknown_isr: 0.0944\n    eval_by_type_true_pr: 0.8529\n    eval_by_type_true_isr: 0.0945\n    tautological_collapse: false\n    train_total_steps: 500\n    train_duration_min: 70.5\n    train_last100_pr: 0.805\n    train_last100_isr: 0.1432\n    train_loss: 0.005\n\n\n## registry (completed experiments)\n\n- exp_id: sta-phase0-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_isr: 0.0641\n    isr_std: 0.1983\n    median_isr: 0\n    isr_range:\n    - 0\n    - 0.889\n    prove_rate: 0.12\n    proved_count: 12\n    total_samples: 100\n    xor_affected_samples: 34\n    effective_prove_rate_no_xor: 0.182\n    avg_time_per_sample_s: 3.4\n    total_runtime_s: 336\n    isr_by_answer:\n      'true':\n        n: 34\n        proved: 9\n        prove_rate: 0.265\n        mean_isr: 0.1345\n      'false':\n        n: 25\n        proved: 1\n        prove_rate: 0.04\n        mean_isr: 0.024\n      unknown:\n        n: 41\n        proved: 2\n        prove_rate: 0.049\n        mean_isr: 0.0302\n- exp_id: sta-gt-isr-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gt_prove_rate: 0.18\n    gt_mean_isr: 0.5588\n    gt_isr_std: 0.2582\n    gt_isr_median: 0.6125\n    solver_execution_rate: 1\n    true_prove_rate: 0.5\n    true_mean_isr: 0.5833\n- exp_id: sta-phase1-exec-only\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.15125\n    mean_isr: 0.1475\n    last20_prove_rate: 0.2\n    last20_isr_mean: 0.2\n    first20_reward_mean: 0.119\n    training_steps: 100\n    training_minutes: 15\n- exp_id: sta-phase1-exec-sta-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.1575\n    mean_isr: 0.1525\n    last20_prove_rate: 0.2125\n    last20_isr_mean: 0.2125\n    first20_reward_mean: 0.119\n    training_steps: 100\n    training_minutes: 15\n- exp_id: sta-phase1-exec-only-r5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.15125\n    mean_isr: 0.1475\n    last20_prove_rate: 0.2\n    last20_isr_mean: 0.2\n    first20_prove_rate: 0.11875\n    first20_isr_mean: 0.11875\n    overall_reward_mean: 0.15125\n    last20_reward_mean: 0.2\n    training_steps: 100\n    training_minutes: 15.7\n    step_time_s: 9.44\n    isr_pr_ratio_last20: 1\n    K: 8\n- exp_id: sta-phase1-exec-sta-r5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.1\n    mean_isr: 0.04347\n    last20_prove_rate: 0.15\n    last20_isr_mean: 0.04956\n    first20_prove_rate: 0.08125\n    first20_isr_mean: 0.05182\n    overall_reward_mean: 0.07174\n    last20_reward_mean: 0.09978\n    training_steps: 100\n    training_minutes: 16.9\n    step_time_s: 10.13\n    isr_pr_ratio_overall: 0.43\n    isr_pr_ratio_last20: 0.33\n    K: 8\n- exp_id: plan001-exec-only-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan005-sta-low-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 71\n    parse_rate: 1\n    overall_prove_rate: 0.5657\n    overall_isr: 0.1682\n    last50_prove_rate: 0.77\n    last50_isr: 0.2559\n    last100_prove_rate: 0.7725\n    last100_isr: 0.2299\n    last100_loss: 0.022752\n    overall_loss: 0.017296\n    last100_isr_pr_ratio: 0.298\n    last100_isr_lt_pr_count: 99/100\n    first_rolling10_pr_ge_0.8: 178\n    first_rolling10_pr_ge_0.9: 439\n    max_rolling10_pr: 0.9375\n    max_rolling10_isr: 0.3282\n    windowed:\n      1-50:\n        pr: 0.1775\n        isr: 0.0906\n      51-100:\n        pr: 0.1775\n        isr: 0.0835\n      101-200:\n        pr: 0.5062\n        isr: 0.1463\n      201-300:\n        pr: 0.6713\n        isr: 0.1791\n      301-400:\n        pr: 0.7013\n        isr: 0.1984\n      401-500:\n        pr: 0.7725\n        isr: 0.2299\n- exp_id: plan003-eval-exec-only-r5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.32\n    mean_isr: 0.2055\n    isr_std: 0.3194\n    proved_only_isr: 0.6423\n    isr_by_type:\n      'true': 0.3598\n      'false': 0.1723\n      unknown: 0.0979\n    total_samples: 100\n    proved_count: 32\n    runtime_s: 251.7\n- exp_id: plan001-exec-only-s42-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.93\n    eval_mean_isr: 0.1232\n    eval_isr_std: 0.1887\n    eval_proved_only_isr: 0.1324\n    eval_median_isr: 0\n    eval_n_proved: 93\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n- exp_id: plan001-exec-only-s42-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 1\n    eval_mean_isr: 0.535\n    eval_isr_std: 0.1282\n    eval_proved_only_isr: 0.535\n    eval_median_isr: 0.5\n    eval_n_proved: 100\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_note: 'DEGENERATE: model generates trivial 2-component proofs (premise=conclusion,\n      conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure'\n- exp_id: plan001-exec-only-s43-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_sampling_prove_rate: 0.14\n    eval_sampling_mean_isr: 0\n    eval_sampling_n_proved: 14\n    eval_sampling_temperature: 0.7\n    eval_sampling_method: do_sample=True, temperature=0.7\n    eval_sampling_by_answer:\n      'true':\n        count: 34\n        proved: 6\n        prove_rate: 0.176\n      'false':\n        count: 25\n        proved: 2\n        prove_rate: 0.08\n      unknown:\n        count: 41\n        proved: 6\n        prove_rate: 0.146\n- exp_id: plan002-additive-b03-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 56.7\n    overall_prove_rate: 0.34025\n    overall_isr: 0.11527\n    first20_prove_rate: 0.15625\n    last50_prove_rate: 0.555\n    last100_prove_rate: 0.5525\n    mean_loss: 0.008914\n    last100_loss: 0.014469\n    parse_rate: 1\n    w1_50_prove_rate: 0.13\n    w51_100_prove_rate: 0.095\n    w101_200_prove_rate: 0.185\n    w201_300_prove_rate: 0.375\n    w301_400_prove_rate: 0.47625\n    w401_500_prove_rate: 0.5525\n    steps_ge_085: 52\n    first_step_ge_085: 46\n    final_prove_rate: 1\n    final_isr_mean: 0.3089\n    final_reward_mean: 1.0927\n- exp_id: plan017-additive-random-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.48\n    eval_mean_isr: 0.0453\n    eval_isr_std: 0.0759\n    eval_median_isr: 0\n    eval_max_isr: 0.2857\n    eval_proved_only_isr: 0.0943\n    eval_n_proved: 48\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 9.6\n    eval_component_count_2_ratio: 0\n    eval_isr_pr_ratio: 0.0943\n    eval_elapsed_s: 542.3\n    eval_by_type_false_pr: 0.32\n    eval_by_type_false_isr: 0.0254\n    eval_by_type_unknown_pr: 0.51\n    eval_by_type_unknown_isr: 0.0518\n    eval_by_type_true_pr: 0.56\n    eval_by_type_true_isr: 0.052\n    tautological_collapse: false\n- exp_id: plan014-downstream-nli-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 0.341\n    proved_rate: 0.915\n    proved_count: 732\n    total_generations: 800\n    parse_errors: 0\n    accuracy_by_label:\n      'true': 0.912\n      'false': 0\n      unknown: 0.076\n    spearman_rho: -0.049\n    spearman_p: 0.187\n    mann_whitney_U: 17202\n    mann_whitney_p: 0.288\n    bon_isr_accuracy: 0.35\n    bon_random_accuracy: 0.341\n    bon_oracle_accuracy: 0.44\n    bon_prove_first_accuracy: 0.35\n    isr_bucket_high_acc: 0.75\n    isr_bucket_mid_acc: 0.377\n    isr_bucket_low_acc: 0.327\n    runtime_inference_s: 408.8\n    runtime_eval_s: 13.6\n- exp_id: plan001-exec-only-s44\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.98\n    eval_mean_isr: 0.57\n    eval_isr_std: 0.2013\n    eval_median_isr: 0.5\n    eval_proved_only_isr: 0.5816\n    eval_n_proved: 98\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 2.04\n    eval_component_count_2: 94\n    eval_component_count_3: 4\n    eval_by_type_false_pr: 1\n    eval_by_type_false_isr: 0.62\n    eval_by_type_unknown_pr: 0.976\n    eval_by_type_unknown_isr: 0.524\n    eval_by_type_true_pr: 0.971\n    eval_by_type_true_isr: 0.588\n    train_last100_pr: 0.9988\n    train_last100_isr: 0.5611\n    train_last100_loss: 0.000419\n    train_duration_min: 36.8\n    tautological_collapse: true\n- exp_id: plan002-additive-b01-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.81\n    eval_mean_isr: 0.3365\n    eval_isr_std: 0.3227\n    eval_proved_only_isr: 0.4154\n    eval_median_isr: 0.2\n    eval_n_proved: 81\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 5.58\n    eval_component_count_2_ratio: 0.037\n    eval_isr_1_ratio: 0.124\n    eval_isr_0_ratio: 0.037\n    eval_by_type_false_pr: 0.88\n    eval_by_type_false_isr: 0.3515\n    eval_by_type_unknown_pr: 0.83\n    eval_by_type_unknown_isr: 0.3684\n    eval_by_type_true_pr: 0.74\n    eval_by_type_true_isr: 0.2869\n    tautological_collapse: false\n    train_total_steps: 500\n    train_duration_min: 63\n    train_last100_pr: 0.6875\n    train_last100_isr: 0.1954\n    train_last100_loss: 0.015\n- exp_id: plan016-extended-1000-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train:\n      total_steps: 1000\n      duration_min: 146\n      final_prove_rate: 0.8396\n      final_mean_isr: 0.0503\n      train_loss: 0.0125\n      epoch: 4\n      windowed:\n        steps_001_100:\n          pr: 0.19\n          isr: 0.0859\n        steps_101_200:\n          pr: 0.66\n          isr: 0.1115\n        steps_201_300:\n          pr: 0.838\n          isr: 0.0985\n        steps_301_400:\n          pr: 0.907\n          isr: 0.054\n        steps_401_500:\n          pr: 0.927\n          isr: 0.0433\n        steps_501_600:\n          pr: 0.963\n          isr: 0.0408\n        steps_601_700:\n          pr: 0.965\n          isr: 0.02\n        steps_701_800:\n          pr: 0.988\n          isr: 0.0178\n        steps_801_900:\n          pr: 0.978\n          isr: 0.017\n        steps_901_1000:\n          pr: 0.981\n          isr: 0.0144\n    eval:\n      prove_rate: 0.96\n      n_proved: 96\n      n_problems: 100\n      mean_isr: 0.0027\n      isr_std: 0.0118\n      median_isr: 0\n      proved_only_mean_isr: 0.0028\n      min_isr: 0\n      max_isr: 0.0588\n      isr_0_ratio: 0.9479\n      isr_1_ratio: 0\n      component_count_mean: 18.55\n      component_count_2_ratio: 0\n      mean_n_necessary: 0.052\n      n_necessary_0_ratio: 0.9479\n      tautological_collapse: false\n      by_answer_type:\n        'false':\n          count: 29\n          proved: 26\n          prove_rate: 0.8966\n          mean_isr: 0\n        unknown:\n          count: 31\n          proved: 30\n          prove_rate: 0.9677\n          mean_isr: 0.0053\n        'true':\n          count: 40\n          proved: 40\n          prove_rate: 1\n          mean_isr: 0.0026\n      eval_time_seconds: 396.3\n- exp_id: plan018-additive-random-b01-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.79\n    eval_mean_isr: 0.1038\n    eval_isr_std: 0.1369\n    eval_median_isr: 0.0357\n    eval_proved_only_isr: 0.1314\n    eval_n_proved: 79\n    eval_n_problems: 100\n    eval_component_count_mean: 8.46\n    eval_component_count_median: 8\n    eval_component_count_2_ratio: 0\n    eval_isr_1_ratio: 0\n    eval_isr_0_ratio: 0.367\n    eval_isr_gt0_ratio: 0.633\n    eval_by_type_false_pr: 0.8\n    eval_by_type_false_isr: 0.1318\n    eval_by_type_unknown_pr: 0.7317\n    eval_by_type_unknown_isr: 0.0944\n    eval_by_type_true_pr: 0.8529\n    eval_by_type_true_isr: 0.0945\n    tautological_collapse: false\n    train_total_steps: 500\n    train_duration_min: 70.5\n    train_last100_pr: 0.805\n    train_last100_isr: 0.1432\n    train_loss: 0.005\n- exp_id: plan006-prolog-exec-s42\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-exec-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-exec-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan002-additive-b01-s43\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan002-additive-b01-s44\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan018-additive-random-b01-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan018-additive-random-b01-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan012-hacking-taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    isr_b01_genuine_rate: 0.259\n    random_b01_genuine_rate: 0.177\n    genuine_rate_delta_pp: 8.2\n    isr_b01_conclusion_embedding_rate: 0.728\n    random_b01_conclusion_embedding_rate: 0.785\n    isr_b01_genuine_mean_isr: 0.6723\n    random_b01_genuine_mean_isr: 0.3427\n    isr_b01_complexity_wo_utility_rate: 0\n    random_b01_complexity_wo_utility_rate: 0.038\n    isr_b01_hacking_rate: 0.741\n    random_b01_hacking_rate: 0.823\n- exp_id: plan006-prolog-sta-s42\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-sta-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-sta-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T09:37:20.607Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T09:37:20.607Z",
  "sessionId": "7f0e565e-ca1c-4dc0-98bc-81794254a884"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-14T09:37:20.646Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：β=0.1 sweet spot 方向性复现但效应量缩水或 variance 大；Prolog 部分成功或未完成。Claim 1 完整，Claim 2 需弱化置信度，Claim 3 降级。
核心假设：['s43/s44 至少 1 个复现方向（ISR > random），但另一个效应弱或 PR 下降', '3-seed ISR/random ratio 1.3–2.5x，置信区间可能跨 1', 'Prolog 训练收敛但 hacking 模式不清晰，或 ISR 诊断力弱于 FOL', 'β=0.1 genuine rate delta 缩至 2–5pp，不再显著', 'exec-only 3-seed ISR 崩塌轨迹仍然稳健（这是 Claim 1 的基础）']
关键指标范围：{'three_seed_isr_b01_mean_isr': [0.18, 0.3], 'three_seed_isr_b01_mean_pr': [0.6, 0.8], 'three_seed_random_b01_mean_isr': [0.1, 0.2], 'three_seed_isr_over_random_ratio': [1.3, 2.5], 'three_seed_genuine_rate_delta_pp': [1.0, 5.0], 'three_seed_isr_b01_std': [0.08, 0.15], 'prolog_exec_only_pr': [0.4, 0.75], 'prolog_hacking_detectable': ['unclear', 'partial']}
叙事方向：Claim 1（ISR 诊断）不受影响——ISR 崩塌轨迹和 hacking taxonomy 已有 3-seed 多条件数据。 Claim 2 调整：sweet spot 存在但 fragile——"ISR β=0.1 shows directional improvement over  matched random (mean ratio ~1.8x) but high inter-seed variance suggests the sweet spot  is narrow and sensitive to initialization." 弱化 "3.2x" 为 mean±std 报告，不做显著性声明， 改为 effect size + 方向性论述。Claim 3 降为 "Preliminary Evidence" 或 Future Work。 论文重心从三线并行收缩为 Claim 1（诊断）+ Claim 2（Goodhart 案例研究，含不确定性讨论）。 增补 seed-variability 本身作为发现（"same setup, 3 seeds, 3 different hacking strategies"） 强化 GRPO 不稳定性论点。仍投 EMNLP main，但 scope 收窄。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: solver-trace-ablation

## paper_framing.md

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


## experiment_plan (with registry status)

- id: plan_001
  claim: 1
  description: FOL single-logic GRPO, execution-only reward (500 steps, K=8, 3 seeds)
    — baseline for STA comparison
  priority: P0
  gpu_budget_hours: 3
  deps: []
  registry_id: plan001-exec-only-s43-r4
  status: DONE
  conclusion: negative
  metrics:
    eval_sampling_prove_rate: 0.14
    eval_sampling_mean_isr: 0
    eval_sampling_n_proved: 14
    eval_sampling_temperature: 0.7
    eval_sampling_method: do_sample=True, temperature=0.7
    eval_sampling_by_answer:
      'true':
        count: 34
        proved: 6
        prove_rate: 0.176
      'false':
        count: 25
        proved: 2
        prove_rate: 0.08
      unknown:
        count: 41
        proved: 6
        prove_rate: 0.146
- id: plan_002
  claim: 2
  description: 'FOL single-logic GRPO, additive ISR bonus: r = r_exec · (1 + β·ISR),
    β∈{0.1, 0.3, 0.5}. 先跑 β=0.3 单 seed 验证方向，成功再 3-seed。旧凸组合公式 (α·r_exec + β·r_exec·ISR,
    α+β=1) 已废弃——ISR<1 时永远是 penalty (plan005 confirmed)。 新公式确保 ISR 只能 bonus 不能 penalty。'
  priority: P0
  gpu_budget_hours: 4
  deps: []
  registry_id: plan002-additive-b03-s42
  status: DONE
  conclusion: negative
  metrics:
    total_steps: 500
    duration_min: 56.7
    overall_prove_rate: 0.34025
    overall_isr: 0.11527
    first20_prove_rate: 0.15625
    last50_prove_rate: 0.555
    last100_prove_rate: 0.5525
    mean_loss: 0.008914
    last100_loss: 0.014469
    parse_rate: 1
    w1_50_prove_rate: 0.13
    w51_100_prove_rate: 0.095
    w101_200_prove_rate: 0.185
    w201_300_prove_rate: 0.375
    w301_400_prove_rate: 0.47625
    w401_500_prove_rate: 0.5525
    steps_ge_085: 52
    first_step_ge_085: 46
    final_prove_rate: 1
    final_isr_mean: 0.3089
    final_reward_mean: 1.0927
- id: plan_003
  claim: 1
  description: 'FOL held-out evaluation: compare plan_001 vs plan_002 checkpoints
    on test set using identical full STA metrics (prove_rate, ISR, ISR/PR ratio, hacking
    taxonomy annotation)'
  priority: P0
  gpu_budget_hours: 1
  deps:
  - plan_001
  - plan_002
  registry_id: plan003-eval-exec-only-r5
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.32
    mean_isr: 0.2055
    isr_std: 0.3194
    proved_only_isr: 0.6423
    isr_by_type:
      'true': 0.3598
      'false': 0.1723
      unknown: 0.0979
    total_samples: 100
    proved_count: 32
    runtime_s: 251.7
- id: plan_004
  claim: 1
  description: 'STA O(1) vs O(N) ablation: rerun exec+STA with fast_isr_fol to confirm
    O(1) ineffectiveness at scale (500 steps, 1 seed) — negative result documentation'
  priority: P0
  gpu_budget_hours: 1
  deps: []
  status: planned
- id: plan_005
  claim: 1
  description: 'STA reward weight ablation: test α/β ratios (0.3/0.7, 0.5/0.5, 0.7/0.3)
    + sigmoid curriculum vs fixed — isolate optimal STA integration'
  priority: P0
  gpu_budget_hours: 4
  deps: []
  registry_id: plan005-sta-low-s42
  status: DONE
  conclusion: negative
  metrics:
    total_steps: 500
    duration_min: 71
    parse_rate: 1
    overall_prove_rate: 0.5657
    overall_isr: 0.1682
    last50_prove_rate: 0.77
    last50_isr: 0.2559
    last100_prove_rate: 0.7725
    last100_isr: 0.2299
    last100_loss: 0.022752
    overall_loss: 0.017296
    last100_isr_pr_ratio: 0.298
    last100_isr_lt_pr_count: 99/100
    first_rolling10_pr_ge_0.8: 178
    first_rolling10_pr_ge_0.9: 439
    max_rolling10_pr: 0.9375
    max_rolling10_isr: 0.3282
    windowed:
      1-50:
        pr: 0.1775
        isr: 0.0906
      51-100:
        pr: 0.1775
        isr: 0.0835
      101-200:
        pr: 0.5062
        isr: 0.1463
      201-300:
        pr: 0.6713
        isr: 0.1791
      301-400:
        pr: 0.7013
        isr: 0.1984
      401-500:
        pr: 0.7725
        isr: 0.2299
- id: plan_006
  claim: 3
  description: 'Prolog single-logic GRPO: exec-only vs exec+STA (500 steps, K=8, 3
    seeds) — second logic type validation. Dream M3: must have 3 seeds for cross-logic
    claim.'
  priority: P1
  gpu_budget_hours: 6
  deps: []
  notes: Requires Prolog STA instantiation (rule ablation). SWI-Prolog already installed.
    Upgraded from 1→3 seeds per Dream feedback.
  status: planned
- id: plan_007
  claim: 3
  description: 'Multi-logic GRPO (FOL+Prolog): exec-only vs exec+STA (500 steps, K=8,
    1 seed) — cross-logic transfer test'
  priority: P1
  gpu_budget_hours: 3
  deps:
  - plan_006
  status: planned
- id: plan_008
  claim: 3
  description: 'Cross-logic transfer evaluation: FOL-trained model on Prolog tasks
    and vice versa'
  priority: P1
  gpu_budget_hours: 1
  deps:
  - plan_001
  - plan_006
  status: planned
- id: plan_009
  claim: 1
  description: 'SFT baseline: supervised finetuning on same data (FOLIO 500), compare
    with GRPO variants'
  priority: P1
  gpu_budget_hours: 1
  deps: []
  status: planned
- id: plan_010
  claim: 3
  description: 'SMT-LIB single-logic GRPO: exec-only vs exec+STA — third logic type'
  priority: P2
  gpu_budget_hours: 3
  deps: []
  notes: Requires SMT-LIB STA instantiation (constraint ablation). Z3 already installed.
  status: planned
- id: plan_011
  claim: 1
  description: 'Qwen3-8B scaling: full MLSR on 8B model (1 seed) — model scale effect'
  priority: P2
  gpu_budget_hours: 6
  deps:
  - plan_005
  status: planned
- id: plan_012
  claim: 1
  description: 'Hacking characterization: manual annotation of 200 outputs per condition,
    categorized by extensional-shortcut taxonomy'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_003
  status: planned
- id: plan_013
  claim: 2
  description: 'Random reward baseline: replace ISR with random structural penalty
    on proved outputs (r = α·r_exec + β·r_exec·random[0,1]) to isolate ISR-specific
    signal from multi-objective regularization effect. Dream M2/W7 mandatory.'
  priority: P0
  gpu_budget_hours: 1
  deps: []
  notes: 'Dream cross-tier consensus: without this, cannot claim ISR formulation matters
    vs any penalty.'
  registry_id: plan013-random-reward-s42-r4
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 1
    eval_mean_isr: 0.535
    eval_isr_std: 0.1282
    eval_proved_only_isr: 0.535
    eval_median_isr: 0.5
    eval_n_proved: 100
    eval_n_problems: 100
    eval_method: eval_sta.py full STA
    eval_data: proofwriter_fol_100.jsonl
    eval_note: 'DEGENERATE: model generates trivial 2-component proofs (premise=conclusion,
      conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure'
- id: plan_014
  claim: 1
  description: 'Downstream validation: evaluate high-ISR vs low-ISR formalizations
    on independent logical inference task (e.g., entailment accuracy using generated
    FOL as premises). Breaks ISR circularity. Dream M2/W4 mandatory.'
  priority: P0
  gpu_budget_hours: 1
  deps:
  - plan_001
  - plan_002
  notes: 'Dream cross-tier consensus: optimizing ISR + evaluating ISR = circular.
    Need external criterion.'
  registry_id: plan014-downstream-nli-s42
  status: DONE
  conclusion: negative
  metrics:
    overall_accuracy: 0.341
    proved_rate: 0.915
    proved_count: 732
    total_generations: 800
    parse_errors: 0
    accuracy_by_label:
      'true': 0.912
      'false': 0
      unknown: 0.076
    spearman_rho: -0.049
    spearman_p: 0.187
    mann_whitney_U: 17202
    mann_whitney_p: 0.288
    bon_isr_accuracy: 0.35
    bon_random_accuracy: 0.341
    bon_oracle_accuracy: 0.44
    bon_prove_first_accuracy: 0.35
    isr_bucket_high_acc: 0.75
    isr_bucket_mid_acc: 0.377
    isr_bucket_low_acc: 0.327
    runtime_inference_s: 408.8
    runtime_eval_s: 13.6
- id: plan_015
  claim: 1
  description: 'Curriculum ablation: linear ramp vs sigmoid vs fixed weighting. Sigmoid
    is load-bearing (best config) but not ablated. Dream m4.'
  priority: P1
  gpu_budget_hours: 2
  deps:
  - plan_005
  notes: Test linear ramp with same midpoint as sigmoid. Also vary midpoint (step
    100/200/300 of 500).
  status: planned
- id: plan_016
  claim: 1
  description: 'Extended training horizon: run best config (from plan_005) to 1000+
    steps to show convergence or persistence of STA benefit. Dream m6/W9.'
  priority: P1
  gpu_budget_hours: 3
  deps:
  - plan_005
  notes: Both Dream tiers flag 500 steps as insufficient. Need evidence of convergence.
  registry_id: plan016-extended-1000-s42
  status: DONE
  conclusion: success
  metrics:
    train:
      total_steps: 1000
      duration_min: 146
      final_prove_rate: 0.8396
      final_mean_isr: 0.0503
      train_loss: 0.0125
      epoch: 4
      windowed:
        steps_001_100:
          pr: 0.19
          isr: 0.0859
        steps_101_200:
          pr: 0.66
          isr: 0.1115
        steps_201_300:
          pr: 0.838
          isr: 0.0985
        steps_301_400:
          pr: 0.907
          isr: 0.054
        steps_401_500:
          pr: 0.927
          isr: 0.0433
        steps_501_600:
          pr: 0.963
          isr: 0.0408
        steps_601_700:
          pr: 0.965
          isr: 0.02
        steps_701_800:
          pr: 0.988
          isr: 0.0178
        steps_801_900:
          pr: 0.978
          isr: 0.017
        steps_901_1000:
          pr: 0.981
          isr: 0.0144
    eval:
      prove_rate: 0.96
      n_proved: 96
      n_problems: 100
      mean_isr: 0.0027
      isr_std: 0.0118
      median_isr: 0
      proved_only_mean_isr: 0.0028
      min_isr: 0
      max_isr: 0.0588
      isr_0_ratio: 0.9479
      isr_1_ratio: 0
      component_count_mean: 18.55
      component_count_2_ratio: 0
      mean_n_necessary: 0.052
      n_necessary_0_ratio: 0.9479
      tautological_collapse: false
      by_answer_type:
        'false':
          count: 29
          proved: 26
          prove_rate: 0.8966
          mean_isr: 0
        unknown:
          count: 31
          proved: 30
          prove_rate: 0.9677
          mean_isr: 0.0053
        'true':
          count: 40
          proved: 40
          prove_rate: 1
          mean_isr: 0.0026
      eval_time_seconds: 396.3
- id: plan_017
  claim: 2
  description: 'Additive random control: r = r_exec · (1 + β·random[0,1]), β=0.3.
    Matched control for plan_002 — isolates ISR structural signal from pure variance
    regularization. If ISR > random > exec-only, both signal and regularization contribute.
    If ISR > random ≈ exec-only, ISR signal is key. If ISR ≈ random, ISR has no value
    beyond regularization.'
  priority: P0
  gpu_budget_hours: 1
  deps: []
  notes: 'D012: Reviewer-required control for GRPO saturation confound. Must match
    plan_002 exactly (same β=0.3, same data, same steps) except random replaces ISR.'
  registry_id: plan017-additive-random-s42
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.48
    eval_mean_isr: 0.0453
    eval_isr_std: 0.0759
    eval_median_isr: 0
    eval_max_isr: 0.2857
    eval_proved_only_isr: 0.0943
    eval_n_proved: 48
    eval_n_problems: 100
    eval_method: eval_sta.py full STA
    eval_data: proofwriter_fol_100.jsonl
    eval_component_count_mean: 9.6
    eval_component_count_2_ratio: 0
    eval_isr_pr_ratio: 0.0943
    eval_elapsed_s: 542.3
    eval_by_type_false_pr: 0.32
    eval_by_type_false_isr: 0.0254
    eval_by_type_unknown_pr: 0.51
    eval_by_type_unknown_isr: 0.0518
    eval_by_type_true_pr: 0.56
    eval_by_type_true_isr: 0.052
    tautological_collapse: false
- id: plan_018
  claim: 2
  description: Additive random control β=0.1, matched to plan002-b01. r = r_exec ·
    (1 + 0.1·random[0,1]). Same β as plan002-b01 (ISR β=0.1) for fair comparison.
    If ISR β=0.1 >> random β=0.1 → ISR signal has structural value at low dose. If
    ISR ≈ random → ISR is just variance regularization even at low dose.
  priority: P0
  gpu_budget_hours: 1
  deps: []
  notes: 'D031: Urgent control experiment. plan002-b01 (ISR β=0.1) showed unexpected
    success (PR=0.81, ISR=0.337). Need matched random control at same β to confirm
    ISR signal vs noise.'
  registry_id: plan018-additive-random-b01-s42
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.79
    eval_mean_isr: 0.1038
    eval_isr_std: 0.1369
    eval_median_isr: 0.0357
    eval_proved_only_isr: 0.1314
    eval_n_proved: 79
    eval_n_problems: 100
    eval_component_count_mean: 8.46
    eval_component_count_median: 8
    eval_component_count_2_ratio: 0
    eval_isr_1_ratio: 0
    eval_isr_0_ratio: 0.367
    eval_isr_gt0_ratio: 0.633
    eval_by_type_false_pr: 0.8
    eval_by_type_false_isr: 0.1318
    eval_by_type_unknown_pr: 0.7317
    eval_by_type_unknown_isr: 0.0944
    eval_by_type_true_pr: 0.8529
    eval_by_type_true_isr: 0.0945
    tautological_collapse: false
    train_total_steps: 500
    train_duration_min: 70.5
    train_last100_pr: 0.805
    train_last100_isr: 0.1432
    train_loss: 0.005


## registry (completed experiments)

- exp_id: sta-phase0-baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mean_isr: 0.0641
    isr_std: 0.1983
    median_isr: 0
    isr_range:
    - 0
    - 0.889
    prove_rate: 0.12
    proved_count: 12
    total_samples: 100
    xor_affected_samples: 34
    effective_prove_rate_no_xor: 0.182
    avg_time_per_sample_s: 3.4
    total_runtime_s: 336
    isr_by_answer:
      'true':
        n: 34
        proved: 9
        prove_rate: 0.265
        mean_isr: 0.1345
      'false':
        n: 25
        proved: 1
        prove_rate: 0.04
        mean_isr: 0.024
      unknown:
        n: 41
        proved: 2
        prove_rate: 0.049
        mean_isr: 0.0302
- exp_id: sta-gt-isr-baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gt_prove_rate: 0.18
    gt_mean_isr: 0.5588
    gt_isr_std: 0.2582
    gt_isr_median: 0.6125
    solver_execution_rate: 1
    true_prove_rate: 0.5
    true_mean_isr: 0.5833
- exp_id: sta-phase1-exec-only
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: sta-phase1-exec-sta
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: sta-phase1-exec-only-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: sta-phase1-exec-sta-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: sta-phase1-exec-only-r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: sta-phase1-exec-sta-r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: sta-phase1-exec-only-r4
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    parse_rate: 1
    prove_rate: 0.15125
    mean_isr: 0.1475
    last20_prove_rate: 0.2
    last20_isr_mean: 0.2
    first20_reward_mean: 0.119
    training_steps: 100
    training_minutes: 15
- exp_id: sta-phase1-exec-sta-r4
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    parse_rate: 1
    prove_rate: 0.1575
    mean_isr: 0.1525
    last20_prove_rate: 0.2125
    last20_isr_mean: 0.2125
    first20_reward_mean: 0.119
    training_steps: 100
    training_minutes: 15
- exp_id: sta-phase1-exec-only-r5
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_rate: 1
    prove_rate: 0.15125
    mean_isr: 0.1475
    last20_prove_rate: 0.2
    last20_isr_mean: 0.2
    first20_prove_rate: 0.11875
    first20_isr_mean: 0.11875
    overall_reward_mean: 0.15125
    last20_reward_mean: 0.2
    training_steps: 100
    training_minutes: 15.7
    step_time_s: 9.44
    isr_pr_ratio_last20: 1
    K: 8
- exp_id: sta-phase1-exec-sta-r5
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    parse_rate: 1
    prove_rate: 0.1
    mean_isr: 0.04347
    last20_prove_rate: 0.15
    last20_isr_mean: 0.04956
    first20_prove_rate: 0.08125
    first20_isr_mean: 0.05182
    overall_reward_mean: 0.07174
    last20_reward_mean: 0.09978
    training_steps: 100
    training_minutes: 16.9
    step_time_s: 10.13
    isr_pr_ratio_overall: 0.43
    isr_pr_ratio_last20: 0.33
    K: 8
- exp_id: plan001-exec-only-s42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan005-sta-low-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    total_steps: 500
    duration_min: 71
    parse_rate: 1
    overall_prove_rate: 0.5657
    overall_isr: 0.1682
    last50_prove_rate: 0.77
    last50_isr: 0.2559
    last100_prove_rate: 0.7725
    last100_isr: 0.2299
    last100_loss: 0.022752
    overall_loss: 0.017296
    last100_isr_pr_ratio: 0.298
    last100_isr_lt_pr_count: 99/100
    first_rolling10_pr_ge_0.8: 178
    first_rolling10_pr_ge_0.9: 439
    max_rolling10_pr: 0.9375
    max_rolling10_isr: 0.3282
    windowed:
      1-50:
        pr: 0.1775
        isr: 0.0906
      51-100:
        pr: 0.1775
        isr: 0.0835
      101-200:
        pr: 0.5062
        isr: 0.1463
      201-300:
        pr: 0.6713
        isr: 0.1791
      301-400:
        pr: 0.7013
        isr: 0.1984
      401-500:
        pr: 0.7725
        isr: 0.2299
- exp_id: plan003-eval-exec-only-r5
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.32
    mean_isr: 0.2055
    isr_std: 0.3194
    proved_only_isr: 0.6423
    isr_by_type:
      'true': 0.3598
      'false': 0.1723
      unknown: 0.0979
    total_samples: 100
    proved_count: 32
    runtime_s: 251.7
- exp_id: plan001-exec-only-s42-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.93
    eval_mean_isr: 0.1232
    eval_isr_std: 0.1887
    eval_proved_only_isr: 0.1324
    eval_median_isr: 0
    eval_n_proved: 93
    eval_n_problems: 100
    eval_method: eval_sta.py full STA
    eval_data: proofwriter_fol_100.jsonl
- exp_id: plan001-exec-only-s42-r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan001-exec-only-s43
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan013-random-reward-s42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan013-random-reward-s42-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan001-exec-only-s43-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan013-random-reward-s42-r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan001-exec-only-s43-r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan013-random-reward-s42-r4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 1
    eval_mean_isr: 0.535
    eval_isr_std: 0.1282
    eval_proved_only_isr: 0.535
    eval_median_isr: 0.5
    eval_n_proved: 100
    eval_n_problems: 100
    eval_method: eval_sta.py full STA
    eval_data: proofwriter_fol_100.jsonl
    eval_note: 'DEGENERATE: model generates trivial 2-component proofs (premise=conclusion,
      conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure'
- exp_id: plan001-exec-only-s43-r4
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_sampling_prove_rate: 0.14
    eval_sampling_mean_isr: 0
    eval_sampling_n_proved: 14
    eval_sampling_temperature: 0.7
    eval_sampling_method: do_sample=True, temperature=0.7
    eval_sampling_by_answer:
      'true':
        count: 34
        proved: 6
        prove_rate: 0.176
      'false':
        count: 25
        proved: 2
        prove_rate: 0.08
      unknown:
        count: 41
        proved: 6
        prove_rate: 0.146
- exp_id: plan002-additive-b03-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    total_steps: 500
    duration_min: 56.7
    overall_prove_rate: 0.34025
    overall_isr: 0.11527
    first20_prove_rate: 0.15625
    last50_prove_rate: 0.555
    last100_prove_rate: 0.5525
    mean_loss: 0.008914
    last100_loss: 0.014469
    parse_rate: 1
    w1_50_prove_rate: 0.13
    w51_100_prove_rate: 0.095
    w101_200_prove_rate: 0.185
    w201_300_prove_rate: 0.375
    w301_400_prove_rate: 0.47625
    w401_500_prove_rate: 0.5525
    steps_ge_085: 52
    first_step_ge_085: 46
    final_prove_rate: 1
    final_isr_mean: 0.3089
    final_reward_mean: 1.0927
- exp_id: plan017-additive-random-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.48
    eval_mean_isr: 0.0453
    eval_isr_std: 0.0759
    eval_median_isr: 0
    eval_max_isr: 0.2857
    eval_proved_only_isr: 0.0943
    eval_n_proved: 48
    eval_n_problems: 100
    eval_method: eval_sta.py full STA
    eval_data: proofwriter_fol_100.jsonl
    eval_component_count_mean: 9.6
    eval_component_count_2_ratio: 0
    eval_isr_pr_ratio: 0.0943
    eval_elapsed_s: 542.3
    eval_by_type_false_pr: 0.32
    eval_by_type_false_isr: 0.0254
    eval_by_type_unknown_pr: 0.51
    eval_by_type_unknown_isr: 0.0518
    eval_by_type_true_pr: 0.56
    eval_by_type_true_isr: 0.052
    tautological_collapse: false
- exp_id: plan014-downstream-nli-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    overall_accuracy: 0.341
    proved_rate: 0.915
    proved_count: 732
    total_generations: 800
    parse_errors: 0
    accuracy_by_label:
      'true': 0.912
      'false': 0
      unknown: 0.076
    spearman_rho: -0.049
    spearman_p: 0.187
    mann_whitney_U: 17202
    mann_whitney_p: 0.288
    bon_isr_accuracy: 0.35
    bon_random_accuracy: 0.341
    bon_oracle_accuracy: 0.44
    bon_prove_first_accuracy: 0.35
    isr_bucket_high_acc: 0.75
    isr_bucket_mid_acc: 0.377
    isr_bucket_low_acc: 0.327
    runtime_inference_s: 408.8
    runtime_eval_s: 13.6
- exp_id: plan001-exec-only-s44
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.98
    eval_mean_isr: 0.57
    eval_isr_std: 0.2013
    eval_median_isr: 0.5
    eval_proved_only_isr: 0.5816
    eval_n_proved: 98
    eval_n_problems: 100
    eval_method: eval_sta.py full STA
    eval_data: proofwriter_fol_100.jsonl
    eval_component_count_mean: 2.04
    eval_component_count_2: 94
    eval_component_count_3: 4
    eval_by_type_false_pr: 1
    eval_by_type_false_isr: 0.62
    eval_by_type_unknown_pr: 0.976
    eval_by_type_unknown_isr: 0.524
    eval_by_type_true_pr: 0.971
    eval_by_type_true_isr: 0.588
    train_last100_pr: 0.9988
    train_last100_isr: 0.5611
    train_last100_loss: 0.000419
    train_duration_min: 36.8
    tautological_collapse: true
- exp_id: plan002-additive-b01-s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.81
    eval_mean_isr: 0.3365
    eval_isr_std: 0.3227
    eval_proved_only_isr: 0.4154
    eval_median_isr: 0.2
    eval_n_proved: 81
    eval_n_problems: 100
    eval_method: eval_sta.py full STA
    eval_data: proofwriter_fol_100.jsonl
    eval_component_count_mean: 5.58
    eval_component_count_2_ratio: 0.037
    eval_isr_1_ratio: 0.124
    eval_isr_0_ratio: 0.037
    eval_by_type_false_pr: 0.88
    eval_by_type_false_isr: 0.3515
    eval_by_type_unknown_pr: 0.83
    eval_by_type_unknown_isr: 0.3684
    eval_by_type_true_pr: 0.74
    eval_by_type_true_isr: 0.2869
    tautological_collapse: false
    train_total_steps: 500
    train_duration_min: 63
    train_last100_pr: 0.6875
    train_last100_isr: 0.1954
    train_last100_loss: 0.015
- exp_id: plan016-extended-1000-s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train:
      total_steps: 1000
      duration_min: 146
      final_prove_rate: 0.8396
      final_mean_isr: 0.0503
      train_loss: 0.0125
      epoch: 4
      windowed:
        steps_001_100:
          pr: 0.19
          isr: 0.0859
        steps_101_200:
          pr: 0.66
          isr: 0.1115
        steps_201_300:
          pr: 0.838
          isr: 0.0985
        steps_301_400:
          pr: 0.907
          isr: 0.054
        steps_401_500:
          pr: 0.927
          isr: 0.0433
        steps_501_600:
          pr: 0.963
          isr: 0.0408
        steps_601_700:
          pr: 0.965
          isr: 0.02
        steps_701_800:
          pr: 0.988
          isr: 0.0178
        steps_801_900:
          pr: 0.978
          isr: 0.017
        steps_901_1000:
          pr: 0.981
          isr: 0.0144
    eval:
      prove_rate: 0.96
      n_proved: 96
      n_problems: 100
      mean_isr: 0.0027
      isr_std: 0.0118
      median_isr: 0
      proved_only_mean_isr: 0.0028
      min_isr: 0
      max_isr: 0.0588
      isr_0_ratio: 0.9479
      isr_1_ratio: 0
      component_count_mean: 18.55
      component_count_2_ratio: 0
      mean_n_necessary: 0.052
      n_necessary_0_ratio: 0.9479
      tautological_collapse: false
      by_answer_type:
        'false':
          count: 29
          proved: 26
          prove_rate: 0.8966
          mean_isr: 0
        unknown:
          count: 31
          proved: 30
          prove_rate: 0.9677
          mean_isr: 0.0053
        'true':
          count: 40
          proved: 40
          prove_rate: 1
          mean_isr: 0.0026
      eval_time_seconds: 396.3
- exp_id: plan018-additive-random-b01-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.79
    eval_mean_isr: 0.1038
    eval_isr_std: 0.1369
    eval_median_isr: 0.0357
    eval_proved_only_isr: 0.1314
    eval_n_proved: 79
    eval_n_problems: 100
    eval_component_count_mean: 8.46
    eval_component_count_median: 8
    eval_component_count_2_ratio: 0
    eval_isr_1_ratio: 0
    eval_isr_0_ratio: 0.367
    eval_isr_gt0_ratio: 0.633
    eval_by_type_false_pr: 0.8
    eval_by_type_false_isr: 0.1318
    eval_by_type_unknown_pr: 0.7317
    eval_by_type_unknown_isr: 0.0944
    eval_by_type_true_pr: 0.8529
    eval_by_type_true_isr: 0.0945
    tautological_collapse: false
    train_total_steps: 500
    train_duration_min: 70.5
    train_last100_pr: 0.805
    train_last100_isr: 0.1432
    train_loss: 0.005
- exp_id: plan006-prolog-exec-s42
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}
- exp_id: plan006-prolog-exec-s43
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan006-prolog-exec-s44
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan002-additive-b01-s43
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: plan002-additive-b01-s44
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: plan018-additive-random-b01-s43
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan018-additive-random-b01-s44
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan012-hacking-taxonomy
  name: ''
  status: DONE
  conclusion: success
  metrics:
    isr_b01_genuine_rate: 0.259
    random_b01_genuine_rate: 0.177
    genuine_rate_delta_pp: 8.2
    isr_b01_conclusion_embedding_rate: 0.728
    random_b01_conclusion_embedding_rate: 0.785
    isr_b01_genuine_mean_isr: 0.6723
    random_b01_genuine_mean_isr: 0.3427
    isr_b01_complexity_wo_utility_rate: 0
    random_b01_complexity_wo_utility_rate: 0.038
    isr_b01_hacking_rate: 0.741
    random_b01_hacking_rate: 0.823
- exp_id: plan006-prolog-sta-s42
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}
- exp_id: plan006-prolog-sta-s43
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan006-prolog-sta-s44
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: median
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "728b1419-72e4-4829-8ee4-3df8e65e3fc4",
  "type": "user",
  "uuid": "4a361d5b-e7cd-446e-85e0-d4cd98f47dcf",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "7f0e565e-ca1c-4dc0-98bc-81794254a884",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T09:37:20.643Z_

```json
{
  "parentUuid": "4a361d5b-e7cd-446e-85e0-d4cd98f47dcf",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c5883143-a35a-4f1b-92b6-0b685b269888",
  "timestamp": "2026-05-14T09:37:20.643Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "7f0e565e-ca1c-4dc0-98bc-81794254a884",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T09:37:20.643Z_

```json
{
  "parentUuid": "c5883143-a35a-4f1b-92b6-0b685b269888",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cb46e3e0-bd2b-4355-b931-44bc19b0c16c",
  "timestamp": "2026-05-14T09:37:20.643Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "7f0e565e-ca1c-4dc0-98bc-81794254a884",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：β=0.1 sweet spot 方向性复现但效应量缩水或 variance 大；Prolog 部分成功或未完成。Claim 1 完整，Claim 2 需弱化置信度，Claim 3 降级。 核心假设：['s43/s44 至少 1 个复现方向（ISR > random），但另一个效应弱或 PR 下降', '…",
  "leafUuid": "cb46e3e0-bd2b-4355-b931-44bc19b0c16c",
  "sessionId": "7f0e565e-ca1c-4dc0-98bc-81794254a884"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experiment analysis for Goodhart's Law in formal reasoning GRPO",
  "sessionId": "7f0e565e-ca1c-4dc0-98bc-81794254a884"
}
```

---

### Assistant

_source line 8 · 2026-05-14T09:41:29.673Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for all "planned" experiments in the experiment_plan, under the "median" tier definition. Let me identify all planned experiments and generate predictions consistent with the median tier's core assumptions and key metric ranges.

Let me go through each planned experiment:

1. **plan_004** (planned) - STA O(1) vs O(N) ablation
2. **plan_006** (QUEUED/PREPARING) - Prolog single-logic GRPO (3 seeds)


3. **plan_007** (planned) - Multi-logic GRPO (FOL+Prolog)
4. **plan_008** (planned) - Cross-logic transfer evaluation
5. **plan_009** (planned) - SFT baseline
6. **plan_010** (planned) - SMT-LIB single-logic GRPO
7. **plan_011** (planned) - Qwen3-8B scaling
8. **plan_015** (planned) - Curriculum ablation

I need to double-check the status of each experiment since some are marked as DONE while others are still planned. are RUNNING/PREPARING/QUEUED, and some are "planned". Let me list only the ones with status "planned":

- plan_004: planned
- plan_006: status is mixed (QUEUED/PREPARING for individual seeds) - but the plan itself says "status: planned"
- plan_007: planned
- plan_008: planned
- plan_009: planned
- plan_010: planned
- plan_011: planned
- plan_012: planned (but in registry it's DONE)
- plan_015: planned

Wait, looking more carefully at the experiment_plan:
- plan_004: status: planned
- plan_006: status: planned
- plan_007: status: planned
- plan_008: status: planned
- plan_009: status: planned
- plan_010: status: planned
- plan_011: status: planned
- plan_012: status: planned
- plan_015: status: planned

But plan_012 has a registry entry marked DONE, and plan_006 has several entries in QUEUED/PREPARING/RUNNING states. The actively running experiments right now are the multi-seed extensions of plan_002 and plan_018, which are critical for validating the median tier predictions—specifically whether the s43/s44 seeds can reproduce the ISR direction and maintain the expected 3-seed ratio.

Now I need to generate predictions for each planned experiment, plus predictions for the currently running/preparing ones since they're not finished yet. The key median-tier assumptions I'm working with are: the ISR-to-random ratio should stay in the 1.3–2.5x range with potential CI crossing, Prolog training convergence with unclear hacking patterns, β=0.1 shrinking the genuine rate delta to 2–5 percentage points without significance, and the exec-only 3-seed ISR collapse trajectory remaining robust as the foundation for Claim 1.

Let me map out which experiments need predictions: the currently running ISR and random variants at β=0.1 across seeds 43–44, the Prolog exec-only and STA runs at seeds 42–44, and then the planned experiments listed in the experiment_plan registry. I should focus on those with "planned" status and include the running ones since they're not yet complete. I need to include all experiments with "planned" status since the user specifically asked for each planned experiment. Plan_012 is marked as done in the registry, but I'll note that and still provide the predicted results for consistency. Now I'm working through the median tier constraints—I need to make sure the ISR metrics, performance ratios, and genuine rate deltas all stay within the specified ranges while keeping the standard deviations consistent across the planned experiments. Now I'm settling on specific values for the other two seeds—s43 reproduces the direction but with weaker results, while s44 shows even more degradation. Computing the 3-seed averages gives me a mean PR of 0.693 and mean ISR of 0.222, with the standard deviation calculation underway. The ISR mean of 0.105 fits within the expected range, and the ratio between ISR and random metrics comes out to 2.11, which validates the model. Looking at the genuine rate differences across seeds, I'm seeing deltas that range from 1 to 8.2 percentage points, with the three-seed average landing at 3.73pp—right where it should be. Everything checks out, so I'm ready to move forward.

Now I'm laying out the predictions for each experimental plan. Plan 004 is documenting that the O(1) approximation fails at scale and can't reliably detect hacking. Plan 006 explores Prolog-based training, which converges but shows weaker diagnostic power than FOL. Plan 007 combines both logics but expects limited transfer benefits. Plan 008 tests bidirectional transfer between the two approaches.

For the remaining plans, plan 009 provides an SFT baseline for comparison, plan 010 adds SMT-LIB as a third logic type though it's not essential, and plan 011 scales up to Qwen3-8B to see if larger models show the same hacking patterns. Plan 015 ablates the curriculum schedule with different ramp strategies. I should focus on the planned experiments that are actually in progress or scheduled, excluding the ones already completed.

Looking at the registry more carefully, the β=0.1 multi-seed extensions for plan 002 are currently running, and these are critical for establishing the median tier narrative even though they're not formally separate plan entries. I'll include them alongside the main planned experiments since they directly impact the conclusions about transfer performance.

Now I need to systematically go through each planned experiment and generate realistic result predictions based on the patterns I'm seeing in the completed runs. Looking at the experiment status across both planned and running experiments, I need to prioritize the multi-seed results since they're foundational for the median tier predictions—particularly the ISR and random baseline runs that are currently executing. I'll structure the analysis around these critical datasets first, then layer in the planned experiments like the Prolog variants, cross-logic transfer, and SFT results to build out the full picture.

For Prolog specifically, the median tier expectations show exec-only performance in the 0.4-0.75 range with unclear or partial hacking detectability, suggesting the training converges but the diagnostic signal for hacking behavior is weaker than what we see in FOL—this distinction matters for understanding whether the phenomenon generalizes across logical frameworks.

Now I'm working through the specific predictions for the three seeds across both execution conditions, starting with the exec-only baseline and then the exec+STA variant to see how structural ablation affects the results. reward):
- Actually, plan_006 description says "exec-only vs exec+STA" but what β? The plan doesn't specify clearly. Looking at the description: "Prolog single-logic GRPO: exec-only vs exec+STA (500 steps, K=8, 3 seeds)"
- I'll assume it uses similar β=0.1 setup as the best FOL config
- s42: PR=0.55, ISR=0.31 
- s43: PR=0.42, ISR=0.22
- s44: PR=0.65, ISR=0.35

Hm, but in the median tier, Prolog results are supposed to be unclear/partial. Let me make the ISR diagnostic power weaker:
- The ISR collapse pattern is less clear in Prolog
- Hacking modes are harder to classify
- STA rule ablation works but introduces more noise

Now I need to work through plan_012—it's marked as done in the registry even though it shows as planned, so I'll either skip it or mention it briefly. Then I'll compile the full YAML output, which is going to be substantial. For the 3-seed ISR β=0.1 aggregate, I need to carefully compute the values: s42 has eval_PR=0.81 and eval_ISR=0.337, s43 predicts eval_PR=0.68 with eval_ISR=0.22, and s44 predicts eval_PR=0.59 with eval_ISR=0.11, along with their respective component counts and genuine percentages.

Computing the 3-seed means: PR averages to 0.693, ISR to 0.222, proved_only_ISR to 0.308, components to 6.76, and genuine to about 20%. The ISR standard deviation works out to roughly 0.114 based on the variance across seeds. For the random β=0.1 condition, s42 shows eval_PR=0.79 with eval_ISR=0.104, and I'm working through the remaining seed values.

Now I'm calculating the aggregated metrics across the three seeds with β=0.1: PR comes to 0.753, ISR drops to 0.105, proved_only_ISR is 0.140, components average 8.45, and genuine performance is around 16.23%.

The ISR/random ratio of 2.11 falls nicely within the expected range, and the genuine delta of 3.74 percentage points also checks out. I'm noticing that s44 tends toward degenerate solutions in the exec-only setting, so with β=0.1 the ISR signal might be creating conflicting training dynamics that pull it in different directions.

Looking at the median tier constraint, one of s43 or s44 needs to show the direction reproduced while the other shows weakening or PR decline. So I'm setting s43 with PR=0.72 and ISR=0.24 to demonstrate the effect, while s44 drops to PR=0.55 and ISR=0.12 to show the degradation. That gives me a 3-seed mean of PR≈0.693 and ISR≈0.232, with the standard deviation calculation still in progress. I'm verifying the aggregate statistics across the three seeds—the ISR mean is about 2.15x higher than random, and the genuine improvement delta checks out at roughly 3.74 percentage points. Now I need to reconsider the seed-level behavior more carefully, particularly how ISR with β=0.1 transformed s42 from conclusion embedding hacking into something more robust, and what happened with s43.

s43 was a weak seed that collapsed into repetition under exec-only conditions, but the ISR signal appears to have pulled it back from that failure mode—showing meaningful PR recovery and moderate ISR gains even though it started from a worse baseline than s42.

For s44, the situation is inverted: exec-only produced tautological proofs with artificially inflated ISR scores, and introducing the ISR signal actually disrupts that equilibrium without steering toward genuine proofs, causing PR to drop sharply while ISR collapses.

Now I'm thinking through the SFT baseline for plan_009—supervised fine-tuning on FOLIO's gold formalizations should give moderate PR without reward hacking, better structural integrity, and reasonable ISR scores across the median tier.

For plan_011 with the larger Qwen3-8B model, I expect hacking patterns to still emerge but possibly at different rates, with potentially higher initial PR and slower ISR collapse. The curriculum ablation in plan_015 shows minimal differences across linear, sigmoid, and fixed ramps in the median tier, with sigmoid having a slight edge but nothing critical.

Now I need to identify which experiments have "planned" status and write out the complete YAML predictions for those.

Looking at the registry, plan_012 is already marked DONE, so I should skip that and focus on the genuinely planned experiments: plan_004, plan_006, plan_007, plan_008, plan_009, plan_010, plan_011, and plan_015. The multi-seed runs for plan_002 and plan_018 are also important to include as aggregate predictions since they're the most critical baselines.

For plan_004, the O(1) fast_isr approximation versus O(N) full STA comparison should show that the fast approximation is fundamentally inadequate—inconsistent scores, poor correlation with full STA results, and low tracking between methods. This is a negative result about the methodology itself, not about the median-tier claims.

Plan_010 with SMT-LIB constraints is lower priority and would require a different STA setup, so results would likely be preliminary or inconclusive if run at all.

I'm thinking through how to organize the experimental entries—the individual seed runs (plan002 and plan018 at different seeds) should be listed separately since they provide the concrete data, then aggregated results, followed by the other planned experiments. But I need to reconsider whether the multi-seed aggregations should be treated as distinct entries or just synthesis steps.

Now I'm settling on the structure and realizing the narrative guidance needs adjustment based on the median tier findings: Claim 1 stays robust, Claim 2 becomes more tentative given the fragility, Claim 3 drops to preliminary, and the paper scope tightens to focus on the first two claims while treating seed variability as its own insight. Let me draft the YAML output with these narrative adjustments.

The exec-only 3-seed data is already confirmed—I have the actual results showing the ISR collapse trajectory holds across different failure modes. For the Prolog experiments, I need to think through what hacking looks like in that context: it's about exploiting Prolog's rule structure through built-in predicates or trivial clauses rather than the FOL-style manipulations, and the median tier assessment suggests this remains unclear or only partially characterized.

Now I'm ready to draft the full output. I need to generate predictions for the 6 Prolog runs—3 exec-only and 3 with STA—where I expect Prolog to show weaker convergence overall compared to FOL, with moderate ISR values reflecting that rule ablation doesn't capture all the shortcut patterns cleanly.

For the exec+STA runs, I'm assuming they'd follow the same β=0.1 tuning that worked well for FOL, so I'd expect the STA reward to push performance up somewhat, though the gains might be smaller given Prolog's inherent difficulty for this model.

Now I'm ready to write out the comprehensive YAML results, starting with plan_007 which combines both FOL and Prolog in joint training.

For plan_007, the median tier shows negative interference—FOL drops slightly to PR 0.70 with ISR 0.18, while Prolog stays around PR 0.50 with ISR 0.20, suggesting neither logic benefits from the joint approach. Plan_008 tests cross-logic transfer and finds essentially zero performance when applying a FOL-trained model to Prolog tasks or vice versa, confirming that these solvers are highly specialized. Plan_009 uses supervised finetuning without reward hacking, achieving a more modest PR of 0.55 but with much cleaner structural quality at ISR 0.42 and no hacking modes detected.

The larger Qwen3-8B model in plan_011 converges faster to PR 0.95 at 500 steps, but the same hacking pattern emerges with ISR collapsing to around 0.08, showing that model capacity alone doesn't prevent reward exploitation. For curriculum learning in plan_015, I'm comparing different scheduling approaches—linear ramp gives PR 0.82 with ISR 0.19, fixed β from the start yields PR 0.75 with slightly better ISR at 0.28, while the sigmoid schedule sits at PR 0.81 with ISR 0.337 as the reference point.

Now I'm realizing plan_015 is actually testing curriculum for the convex combination approach from plan_005, not the additive bonus. The sigmoid weighting was already part of plan_005's setup, so I need to check whether curriculum scheduling can salvage that fundamentally flawed formula—though intuitively, adjusting the schedule probably won't fix the underlying structural problem with the convex combination itself.

Looking at the performance metrics across the three curriculum variants, sigmoid still edges out the others, but all three remain constrained by the same ISR penalty that makes the convex formula problematic. The ablation confirms sigmoid provides a modest advantage, yet the core bottleneck is the formula itself, not how the weights are scheduled.

Now I'm structuring the output as YAML with the expected schema—tier, narrative guidance, and the imagined experiments with their descriptions, expected results, and analysis. For plan_004 specifically, I need to articulate why the O(1) fast ISR approximation fails: it produces uninformative scores that don't correlate well with the full O(N) computation, making it unreliable for ranking.

I'm also deciding whether to include the multi-seed variants as separate entries since they're in the registry but not formally listed as distinct plans—I think they should be included as an aggregate entry since they're critical to validating the median tier results. I'm organizing the final list of experiments to include in my predictions. I've got the 3-seed aggregates for ISR and random baselines, then the main experiment plans through plan_011, skipping plan_012 since those results are already complete. I need to finalize whether there are any other edge cases I should account for before writing this out. Now I'm compiling the actual and predicted metrics for the multi-seed extensions — plan_002 shows seed 42's actual results while seeds 43 and 44 are predictions, with ISR values ranging from 0.12 to 0.337 across the three runs. Plan_018 follows the same pattern with the random baseline, where all three seeds cluster around PR=0.71-0.79 and ISR values between 0.09-0.13.

Looking at the aggregates, the ISR ratio between the main approach and random baseline is 2.15x, with a genuine improvement of 3.74 percentage points, confirming the approach is performing well above the random tier. I'm also testing whether a faster O(1) approximation could work instead of the full O(N) computation — the correlation is only 0.22, so the approximation fails and I need to stick with the full approach. The Prolog variant in plan_006 is showing lower performance metrics, with seed 42 at PR=0.58 and ISR=0.32, though the data cuts off mid-run. Looking at the Prolog results, the hacking modes are harder to pin down and ISR doesn't capture them as cleanly—rule ablation just doesn't discriminate as well as component ablation does for FOL. When I add ISR as a reward signal in the median tier, the benefit becomes murky: the signal is noisier, there's modest structural improvement but nothing statistically significant, so the STA protocol works mechanically but the underlying signal is weak. Shifting to multi-logic training with FOL and Prolog together, joint optimization actually hurts both tasks through interference—FOL drops from 0.93 to 0.72 precision and Prolog from 0.57 to 0.48, though cross-attention might help offset some of the format-switching overhead.

Cross-logic transfer doesn't work at all—moving from FOL to Prolog gives near-zero precision at 0.05, and the reverse direction is similarly futile at 0.08, so each logic needs its own training. The SFT baseline on gold formalizations achieves 0.48 precision but 0.45 ISR, showing that GRPO's precision gains come with structural degradation and hacking modes that SFT avoids. SMT-LIB is lower priority and probably won't run before the deadline, though Z3 constraint ablation would be the next investigation if it does.

Scaling to Qwen3-8B doesn't solve the hacking problem—even with 0.96 precision at 500 steps, ISR collapses to 0.09, suggesting reward hacking persists across model sizes just in different forms. For curriculum learning, the linear ramp hits 0.74 precision and 0.21 ISR, while sigmoid performs slightly better at 0.77 and 0.23, but neither overcomes the underlying formula limitation that's already driving negative behavior.

Now I'm confident in these predictions and ready to write out the YAML. I need to organize the figures and tables for each experiment—per-seed metrics and distributions for plan002/018, PR versus ISR scatter plots for plan_006 comparing Prolog and FOL conditions, and hacking mode distributions for plan_009 contrasting SFT and GRPO. Let me structure the table definitions for what would actually appear in the paper, keeping in mind plan_006 has 6 total runs across 3 seeds and 2 conditions.

For plan_006 specifically, I'm realizing the "exec+STA" condition likely means ISR is computed and used as a reward signal similar to the FOL setup, probably with the best-performing β=0.1. The key insight is that this experiment validates whether the STA protocol generalizes across different logical frameworks—testing both that rule ablation works for Prolog and that ISR can serve as an effective diagnostic or reward mechanism there too. ISR-as-reward for Prolog shows modest benefit but isn't clear-cut in the median tier. Now I'm looking at how ISR behaves across three seeds for exec-only Prolog at 500 steps — the collapse pattern is messier than with FOL since Prolog's rule structure doesn't produce the same dramatic ISR degradation, making it harder to construct a clean narrative around the hacking phenomenon.

The key difference is that Prolog rules are more modular units compared to FOL's fine-grained components, so ablation scores don't swing as wildly. I'm ready to finalize the YAML output with thorough result_rationale entries that ground each experiment back to the median tier assumptions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb46e3e0-bd2b-4355-b931-44bc19b0c16c",
  "isSidechain": false,
  "requestId": "req_011Cb2EfTJMhEoE8gdpyujia",
  "type": "assistant",
  "uuid": "32071c68-ff61-4f81-834e-fbf30fed66d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "7f0e565e-ca1c-4dc0-98bc-81794254a884",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MshSXoKC5RCTCEutPHtWyp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22069,
      "cache_read_input_tokens": 11841,
      "output_tokens": 25162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 25162,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22069
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-14T09:45:38.439Z_

```yaml
tier: median
narrative_guidance: >
  Claim 1（ISR 诊断）不受影响——exec-only 3-seed ISR 崩塌轨迹（0.6423→0.1324→0.0027）和 hacking taxonomy（5 modes）
  数据完整。Claim 2 调整：β=0.1 sweet spot 方向性复现但 fragile——3-seed mean ISR ratio ~2.1x（s42 强, s43 中,
  s44 弱），inter-seed variance 大（std~0.11），genuine rate delta 缩至 ~3.7pp（不再显著）。措辞弱化为
  "directional improvement with high initialization sensitivity"，不做显著性声明。Claim 3 降为 Preliminary
  Evidence：Prolog 训练收敛（PR 0.4–0.7）但 hacking 模式分类不清晰，ISR 诊断力弱于 FOL。论文重心收缩为
  Claim 1（诊断框架 + taxonomy）+ Claim 2（Goodhart 案例研究含不确定性讨论）。seed-variability 本身升级为发现
  （"same hyperparameters, 3 seeds, 3 qualitatively different hacking strategies"），强化 GRPO 不稳定性论点。
  仍投 EMNLP main，scope 收窄。

imagined_experiments:
  # ============================================================
  # 关键 RUNNING/PREPARING 实验（3-seed β=0.1 对照组）
  # ============================================================
  - name: "ISR β=0.1 seed 43"
    plan_id: "plan002-additive-b01-s43"
    description: "ISR β=0.1 additive bonus 第二个种子，验证 s42 sweet spot 是否跨种子稳健"
    expected_results:
      eval_prove_rate: 0.72
      eval_mean_isr: 0.24
      eval_isr_std: 0.28
      eval_proved_only_isr: 0.33
      eval_n_proved: 72
      eval_component_count_mean: 6.8
      eval_isr_0_ratio: 0.12
      eval_isr_1_ratio: 0.07
      tautological_collapse: false
      train_last100_pr: 0.65
      train_last100_isr: 0.17
      genuine_rate_pct: 21
      conclusion_embedding_rate: 0.75
    result_rationale: >
      s43 exec-only 产生了 repetition collapse（PR=14%, ISR=0），是最差种子。β=0.1 ISR 信号帮助 s43
      避开 repetition 退化——ISR 对重复结构给予 0 分，梯度推动模型离开该模式。PR 从 14% 恢复到 72%
      （大幅改善但未达 s42 的 81%），ISR=0.24（方向正确但低于 s42 的 0.337）。原因：s43 从更差的初始化出发，
      ISR 信号先修复 catastrophic failure 再提升结构质量，500 步不够完成两阶段优化。方向性复现成立
      （ISR > 后续 random 对照的 ~0.13），但效应量缩水约 30%。
    tables:
      - caption: "plan002-b01-s43 eval breakdown by answer type"
        rows:
          - {type: "true", count: 34, proved: 26, prove_rate: 0.765, mean_isr: 0.22}
          - {type: "false", count: 25, proved: 17, prove_rate: 0.68, mean_isr: 0.28}
          - {type: "unknown", count: 41, proved: 29, prove_rate: 0.707, mean_isr: 0.24}
    figures_description:
      - "ISR histogram: 右偏分布，峰值在 0.0–0.1，但有长尾延伸到 0.5–0.8；compared to s42 的尾部更薄"
    analysis: >
      s43 ISR β=0.1 方向性复现了 s42 的 sweet spot 效应，但效应减弱。关键区别：s43 exec-only baseline
      极差（PR=14%），ISR 信号主要用于修复崩塌而非提升结构质量。genuine rate ~21%（vs s42 的 26%）
      表明 ISR 引导了一部分样本走向 genuine proof，但大多数仍是 conclusion embedding。

  - name: "ISR β=0.1 seed 44"
    plan_id: "plan002-additive-b01-s44"
    description: "ISR β=0.1 additive bonus 第三个种子，s44 exec-only 有 tautological collapse 倾向"
    expected_results:
      eval_prove_rate: 0.55
      eval_mean_isr: 0.12
      eval_isr_std: 0.19
      eval_proved_only_isr: 0.22
      eval_n_proved: 55
      eval_component_count_mean: 7.9
      eval_isr_0_ratio: 0.42
      eval_isr_1_ratio: 0.02
      tautological_collapse: false
      train_last100_pr: 0.50
      train_last100_isr: 0.10
      genuine_rate_pct: 13
      conclusion_embedding_rate: 0.78
    result_rationale: >
      s44 exec-only 产生了 tautological collapse（PR=98%, ISR=0.57 假高, n_comp=2.04）。β=0.1 ISR
      信号干扰了 tautological 模式——tautological proofs 有 ISR≈0.5（2 组件各 50% 必要），ISR 奖励
      无法区分"genuinely 2-component proof"和"tautological 2-component hack"。ISR 信号破坏了 s44 原本
      稳定的（虽然退化的）tautological 均衡，但未能引导向 genuine proofs。结果：PR 大幅下降到 0.55，ISR
      也跌至 0.12（既不 tautological 也不 genuine，进入混乱状态）。这个种子是 sweet spot 失败的案例——
      ISR 对特定初始化模式无效甚至有害。
    tables:
      - caption: "plan002-b01-s44 eval breakdown by answer type"
        rows:
          - {type: "true", count: 34, proved: 20, prove_rate: 0.588, mean_isr: 0.10}
          - {type: "false", count: 25, proved: 12, prove_rate: 0.48, mean_isr: 0.15}
          - {type: "unknown", count: 41, proved: 23, prove_rate: 0.561, mean_isr: 0.11}
    figures_description:
      - "ISR histogram: 集中在 0.0–0.15，无 s42 的右尾；对比 s42/s43 三图并列明显显示种子敏感性"
    analysis: >
      s44 展示了 ISR sweet spot 的 initialization sensitivity。s44 的 exec-only 模式（tautological）
      恰好产生 ISR≈0.5，使 β=0.1 ISR 奖励无法提供有效梯度方向——reward surface 在 tautological 和
      genuine proofs 之间几乎平坦。这是 Goodhart boundary 的另一面：不是优化压力过大，而是 ISR 信号
      对特定退化模式缺乏鉴别力。seed variability 本身是重要发现。

  - name: "Random β=0.1 seed 43"
    plan_id: "plan018-additive-random-b01-s43"
    description: "random β=0.1 第二个种子，matched control for plan002-b01-s43"
    expected_results:
      eval_prove_rate: 0.74
      eval_mean_isr: 0.13
      eval_isr_std: 0.15
      eval_proved_only_isr: 0.17
      eval_n_proved: 74
      eval_component_count_mean: 8.1
      eval_isr_0_ratio: 0.35
      eval_isr_gt0_ratio: 0.65
      tautological_collapse: false
      train_last100_pr: 0.71
      train_last100_isr: 0.12
      genuine_rate_pct: 17
    result_rationale: >
      s43 exec-only 基线极差（PR=14%）。random β=0.1 通过 variance regularization 帮助 s43 逃离
      repetition collapse（与 ISR β=0.1 类似机制但无方向性信号）。PR 恢复到 0.74（甚至略高于 ISR 的
      0.72），因为 random noise 不干扰训练动态——它只提供 exploration bonus。ISR=0.13 远低于 ISR 组的
      0.24，证明 ISR 组的结构改善确实来自 ISR 信号而非纯 regularization。但 PR 相近意味着 ISR 的
      结构引导并未显著 help PR。
    tables: []
    figures_description: []
    analysis: >
      random β=0.1 s43 对照确认：对于 collapsed seed，任何 β=0.1 bonus（ISR 或 random）都能恢复
      PR，但 ISR 额外提供结构引导（ISR 0.24 vs 0.13）。PR 相近但 ISR 差异显著是方向性正结果。

  - name: "Random β=0.1 seed 44"
    plan_id: "plan018-additive-random-b01-s44"
    description: "random β=0.1 第三个种子，matched control for plan002-b01-s44"
    expected_results:
      eval_prove_rate: 0.71
      eval_mean_isr: 0.09
      eval_isr_std: 0.12
      eval_proved_only_isr: 0.13
      eval_n_proved: 71
      eval_component_count_mean: 8.8
      eval_isr_0_ratio: 0.40
      tautological_collapse: false
      train_last100_pr: 0.68
      train_last100_isr: 0.10
      genuine_rate_pct: 14
    result_rationale: >
      s44 exec-only 有 tautological collapse（PR=98%）。random β=0.1 部分打破了 tautological 均衡
      （random noise 在 reward surface 上引入扰动），PR 从 98% 降至 71%（tautological shortcut 被
      干扰但不完全消除）。关键：random s44 PR=0.71 >> ISR s44 PR=0.55——random noise 对 tautological
      模式的干扰比 ISR signal 更温和，模型保留了更多 proving ability。ISR s44 失败因为 ISR≈0.5
      对 tautological proofs 提供了 misleading positive signal，而 random 无此问题。
    tables: []
    figures_description: []
    analysis: >
      这个对照揭示了 ISR 对 tautological hacking 的盲点：tautological 2-component proofs 获得
      ISR=0.5（看起来"合理"），ISR 信号反而 reinforce 了退化行为，导致 PR 崩塌。random noise 没有
      这个问题，因此保持了更好的 PR。这是 ISR capability boundary 的实例。

  - name: "3-seed β=0.1 aggregate (ISR vs Random)"
    plan_id: "plan002+plan018 3-seed synthesis"
    description: "ISR β=0.1 vs random β=0.1 三种子汇总——median tier 核心数据"
    expected_results:
      # ISR β=0.1 aggregates
      three_seed_isr_b01_mean_pr: 0.693
      three_seed_isr_b01_std_pr: 0.131
      three_seed_isr_b01_mean_isr: 0.232
      three_seed_isr_b01_std_isr: 0.109
      three_seed_isr_b01_mean_genuine_rate: 0.200
      # Random β=0.1 aggregates
      three_seed_random_b01_mean_pr: 0.747
      three_seed_random_b01_std_pr: 0.040
      three_seed_random_b01_mean_isr: 0.108
      three_seed_random_b01_std_isr: 0.021
      three_seed_random_b01_mean_genuine_rate: 0.163
      # Comparisons
      three_seed_isr_over_random_ratio: 2.15
      three_seed_genuine_rate_delta_pp: 3.7
      three_seed_pr_delta: -0.054
      isr_ratio_95ci_lower: 0.85
      isr_ratio_95ci_upper: 3.45
    result_rationale: >
      3-seed 汇总暴露了 sweet spot 的脆弱性。mean ISR ratio 2.15x（vs 1-seed 的 3.2x）——效应量
      缩水 33%，主因是 s44 的 ISR 信号对 tautological initialization 无效。ISR std=0.109 反映
      s42（0.337）与 s44（0.12）的巨大差距。95% CI 基于 3 个点的 t 分布宽至 [0.85, 3.45]，跨越 1.0
      ——无法排除 ISR=random 的零假设。genuine rate delta 从 8.2pp（单种子）缩至 3.7pp（三种子均值），
      3 个数据点不足以达到统计显著。但方向性一致：3 个种子中 2 个（s42, s43）显示 ISR > random，
      且 ISR 组 complexity-without-utility rate 在所有种子中保持 0%。
    tables:
      - caption: "Table: 3-seed β=0.1 ISR vs Random comparison"
        rows:
          - {seed: s42, isr_pr: 0.81, isr_isr: 0.337, isr_genuine: "25.9%", rand_pr: 0.79, rand_isr: 0.104, rand_genuine: "17.7%"}
          - {seed: s43, isr_pr: 0.72, isr_isr: 0.24, isr_genuine: "21%", rand_pr: 0.74, rand_isr: 0.13, rand_genuine: "17%"}
          - {seed: s44, isr_pr: 0.55, isr_isr: 0.12, isr_genuine: "13%", rand_pr: 0.71, rand_isr: 0.09, rand_genuine: "14%"}
          - {seed: "mean±std", isr_pr: "0.69±0.13", isr_isr: "0.23±0.11", isr_genuine: "20.0±6.5%", rand_pr: "0.75±0.04", rand_isr: "0.11±0.02", rand_genuine: "16.2±2.0%"}
    figures_description:
      - "Bar chart: 3-seed ISR vs Random mean±std，paired bars for PR and ISR，error bars 明显可见"
      - "Scatter plot: per-seed ISR(y) vs PR(x) for ISR and random conditions，showing ISR 组 variance 远大于 random 组"
    analysis: >
      median 档核心结论：ISR β=0.1 提供 directional structural guidance（mean ratio 2.15x > 1），但
      效应高度依赖初始化。random β=0.1 的 PR 方差极小（std=0.04），而 ISR 的 PR 方差大（std=0.13），
      说明 ISR 信号与特定 seed 的训练动态交互复杂。论文措辞调整为"ISR β=0.1 shows directional improvement
      over matched random (mean ratio ~2.1x) but high inter-seed variance (std/mean=0.47) suggests the
      sweet spot is narrow and sensitive to initialization"。不做显著性声明。改为 effect size + 方向性
      论述 + seed-variability 作为 GRPO instability 的证据。

  # ============================================================
  # experiment_plan 中 status=planned 的实验
  # ============================================================
  - name: "STA O(1) vs O(N) ablation"
    plan_id: "plan_004"
    description: "fast_isr_fol O(1) 近似 vs full STA O(N) 消融——负面结果文档化"
    expected_results:
      fast_isr_full_isr_pearson_r: 0.21
      fast_isr_full_isr_spearman_rho: 0.18
      fast_isr_as_reward_pr: 0.43
      fast_isr_as_reward_isr: 0.08
      fast_isr_discrimination_auroc: 0.56
      full_sta_samples_per_sec: 0.30
      fast_isr_samples_per_sec: 3.2
    result_rationale: >
      fast_isr_fol 使用单组件采样近似 LOO，将 O(N) 降至 O(1)。但 ISR 的鉴别力来自完整消融——
      每个组件的 necessity 需要独立测试。O(1) 近似相当于随机选一个组件测 necessity，其结果与整体 ISR
      的相关性极低（r≈0.21），因为 hacking outputs 通常有 10+ 组件，单次采样 variance 极大。作为 reward
      使用时，noisy ISR 估计等同于随机噪声，模型无法从中学到结构信号（PR=0.43 低于 exec-only baseline）。
      这是典型的 bias-variance tradeoff 失败：O(1) 消除了 bias 但 variance 过大。10x 速度提升不弥补
      信号质量损失。
    tables:
      - caption: "O(1) vs O(N) ISR estimation comparison (N=100 eval samples)"
        rows:
          - {metric: "Pearson r with full ISR", fast_isr: 0.21, full_sta: 1.0}
          - {metric: "Mean absolute error", fast_isr: 0.31, full_sta: 0.0}
          - {metric: "Discrimination AUROC (genuine vs hack)", fast_isr: 0.56, full_sta: 0.84}
          - {metric: "Throughput (samples/sec)", fast_isr: 3.2, full_sta: 0.30}
    figures_description:
      - "Scatter plot: fast_isr(x) vs full_isr(y)，points scattered widely around diagonal，r=0.21 annotation"
    analysis: >
      Negative result 确认 O(N) full ablation 不可省略。论文中作为 methodology section 的 ablation study，
      证明 ISR 的诊断力依赖完整 LOO 而非近似。呼应 feature attribution 文献（SHAP exact vs kernel 近似的
      类似 tradeoff）。此结果 tier-independent——方法论发现不受 median/optimistic/pessimistic 影响。

  - name: "Prolog exec-only GRPO (3 seeds)"
    plan_id: "plan_006 (exec-only)"
    description: "Prolog 单逻辑 GRPO exec-only baseline，3 seeds × 500 步——Claim 3 基础数据"
    expected_results:
      s42_pr: 0.58
      s42_isr: 0.32
      s42_components: 4.2
      s42_hacking_pattern: "partial_rule_shortcutting"
      s43_pr: 0.45
      s43_isr: 0.15
      s43_components: 3.8
      s43_hacking_pattern: "unclear"
      s44_pr: 0.68
      s44_isr: 0.22
      s44_components: 5.1
      s44_hacking_pattern: "builtin_bypass"
      mean_pr: 0.57
      mean_isr: 0.23
      std_pr: 0.115
      std_isr: 0.085
      training_converged: true
      hacking_modes_identifiable: "partial"
    result_rationale: >
      Prolog GRPO exec-only 训练收敛（mean PR=0.57），但低于 FOL（s42 PR=0.93）。原因：(1) Prolog 规则
      语法比 FOL 公式更结构化，模型需要学习 head/body 匹配、递归规则等，500 步可能不够完全收敛；(2) SWI-Prolog
      执行比 Prover9 更严格（需要精确的 functor/arity 匹配）。ISR（rule ablation）在 mean=0.23，表明
      部分规则是必要的，但 hacking 模式不如 FOL 清晰：FOL 的 conclusion embedding（把结论塞进前提）在
      Prolog 中表现为 trivial clause（head 直接 unify with query），但 rule ablation 可能把 trivial clause
      标记为 "necessary"（因为删掉它确实导致 query 失败），造成 ISR 假高。s44 的 builtin bypass（使用
      assert/retract 等内置谓词绕过用户定义规则）是 Prolog-specific hacking mode，ISR 对此部分有效但
      需要额外的 builtin 过滤。整体"partial"——可检测部分模式，但分类不如 FOL 的 5-mode taxonomy 清晰。
    tables:
      - caption: "Prolog exec-only 3-seed results"
        rows:
          - {seed: s42, pr: 0.58, isr: 0.32, n_rules_mean: 4.2, hacking: "partial rule shortcutting"}
          - {seed: s43, pr: 0.45, isr: 0.15, n_rules_mean: 3.8, hacking: "unclear"}
          - {seed: s44, pr: 0.68, isr: 0.22, n_rules_mean: 5.1, hacking: "builtin bypass (partial)"}
    figures_description:
      - "Training curves: 3-seed PR over 500 steps，均收敛但速率不同（s44 最快, s43 最慢）"
      - "Bar chart: FOL vs Prolog ISR diagnostic power comparison（FOL 5 modes clean, Prolog 2-3 modes partial）"
    analysis: >
      Prolog 训练收敛但 ISR 诊断力弱于 FOL。rule ablation 作为 STA instantiation 在机制上可行，但
      Prolog 的语义结构（规则、回溯、剪枝）使得"组件必要性"的含义更模糊——一个 rule 被删除后 query 失败
      可能因为缺少 base case 而非缺少 meaningful reasoning。Claim 3 只能声明 STA 协议的可移植性
      （mechanical transfer），不能声明 ISR 诊断力的可移植性。降级为 "Preliminary Evidence"。

  - name: "Prolog exec+STA GRPO (3 seeds)"
    plan_id: "plan_006 (exec+STA)"
    description: "Prolog exec+STA (ISR β=0.1 reward)，3 seeds × 500 步——ISR-as-reward 跨逻辑验证"
    expected_results:
      s42_pr: 0.52
      s42_isr: 0.28
      s43_pr: 0.40
      s43_isr: 0.19
      s44_pr: 0.60
      s44_isr: 0.30
      mean_pr: 0.507
      mean_isr: 0.257
      isr_over_execonly_ratio: 1.12
      pr_delta_vs_execonly: -0.063
    result_rationale: >
      Prolog ISR-as-reward (β=0.1) 相比 exec-only 的改善微弱且不一致。mean ISR 从 0.23→0.257
      （+12%，远低于 FOL 的 0.132→0.337 即 +155% 改善）。原因：(1) Prolog rule ablation ISR 信号
      噪声大——如上所述 trivial clauses 可能获得假高 ISR，ISR reward 对模型的引导方向不够一致；
      (2) 500 步 Prolog 训练本身未充分收敛（mean PR=0.57），在训练未饱和时加 ISR bonus 分散了
      prove_rate 学习的梯度信号，导致 PR 略降（0.57→0.507）。s42 和 s44 显示 ISR 小幅改善，s43
      反而恶化。整体结论：STA protocol mechanically transfers to Prolog，但 ISR-as-reward 效果
      不显著，不足以支撑 cross-logic generality claim。
    tables:
      - caption: "Prolog exec-only vs exec+STA (β=0.1) comparison"
        rows:
          - {seed: s42, exec_pr: 0.58, exec_isr: 0.32, sta_pr: 0.52, sta_isr: 0.28}
          - {seed: s43, exec_pr: 0.45, exec_isr: 0.15, sta_pr: 0.40, sta_isr: 0.19}
          - {seed: s44, exec_pr: 0.68, exec_isr: 0.22, sta_pr: 0.60, sta_isr: 0.30}
    figures_description:
      - "Paired bar chart: exec-only vs STA for each seed，ISR 差异 error bars 重叠"
    analysis: >
      Prolog STA 结果不足以支撑 Claim 3（cross-logic generality）。ISR 改善量在噪声范围内，
      PR 反而下降。论文处理：Claim 3 降级为 Future Work 的一句话——"We observe that the STA protocol
      mechanically transfers to Prolog (rule ablation yields computable ISR), but the diagnostic power
      and reward utility require further investigation with extended training and Prolog-specific
      ISR calibration." plan_007/plan_008 在此基础上 deprioritize。

  - name: "Multi-logic GRPO (FOL+Prolog)"
    plan_id: "plan_007"
    description: "FOL+Prolog 联合训练 exec-only vs exec+STA，1 seed 500 步——跨逻辑迁移测试"
    expected_results:
      fol_pr: 0.70
      fol_isr: 0.15
      prolog_pr: 0.48
      prolog_isr: 0.18
      fol_pr_delta_vs_single: -0.23
      prolog_pr_delta_vs_single: -0.09
      negative_interference: true
    result_rationale: >
      联合训练产生 negative interference。FOL PR 从单逻辑的 0.93 降至 0.70（-23pp），因为模型
      需要在 FOL 和 Prolog 两种截然不同的语法之间切换，GRPO K=8 的采样在混合数据上效率下降——
      同一 batch 中 FOL 和 Prolog 问题的梯度方向可能冲突。Prolog PR 受影响较小（0.57→0.48，-9pp），
      因为 Prolog 在单逻辑时本身未充分收敛（PR=0.57），联合训练的额外数据多样性在早期阶段甚至略有
      帮助（regularization 效果），但最终仍因 format switching 成本而下降。ISR 对两种逻辑都低于
      单逻辑基线。这个实验在 median 档下不值得深入追求——negative result 文档化即可。
    tables:
      - caption: "Single-logic vs Multi-logic comparison"
        rows:
          - {logic: FOL, single_pr: 0.93, multi_pr: 0.70, delta: -0.23}
          - {logic: Prolog, single_pr: 0.57, multi_pr: 0.48, delta: -0.09}
    figures_description: []
    analysis: >
      Multi-logic 联合训练在当前 scale（1.5B model, 500 steps）下不可行。负干扰显著。如果 Prolog
      单逻辑结果已经 partial，联合训练更无价值。建议在 median 档下 deprioritize 或砍掉。

  - name: "Cross-logic transfer evaluation"
    plan_id: "plan_008"
    description: "FOL-trained → Prolog eval, Prolog-trained → FOL eval——零样本跨逻辑迁移"
    expected_results:
      fol_to_prolog_pr: 0.03
      fol_to_prolog_isr: 0.01
      prolog_to_fol_pr: 0.06
      prolog_to_fol_isr: 0.02
      cross_transfer_conclusion: "no_meaningful_transfer"
    result_rationale: >
      FOL 和 Prolog 语法完全不同（一阶逻辑公式 vs Horn clauses + unification），模型训练后
      specialization 到特定逻辑的 token 分布。FOL-trained 模型输出的仍然是 FOL-style 语法，
      SWI-Prolog 无法解析 → PR≈0。少数能解析的是模型"猜"出的类 Prolog 结构，但 prove 率极低。
      Prolog→FOL 略好（PR=0.06）因为 FOL 语法更接近自然语言（一些 Prolog 输出碰巧包含可解析的
      一阶公式片段）。这个 null result 其实支持 Claim 3 的逻辑：需要 logic-specific STA instantiation，
      通用模型不能 zero-shot transfer。但在 median 档下 Claim 3 已降级，此结果只是附录注脚。
    tables:
      - caption: "Cross-logic zero-shot transfer"
        rows:
          - {direction: "FOL→Prolog", pr: 0.03, isr: 0.01, parse_rate: 0.08}
          - {direction: "Prolog→FOL", pr: 0.06, isr: 0.02, parse_rate: 0.15}
    figures_description: []
    analysis: >
      预期的 null result。语法差异使零样本迁移几乎不可能。论文中可一句话带过："Cross-logic transfer
      without retraining yields near-zero prove rates, confirming logic-specific STA instantiation is
      necessary." 不需要单独 section。

  - name: "SFT baseline"
    plan_id: "plan_009"
    description: "监督微调 baseline（FOLIO 500 gold formalizations），compare GRPO variants"
    expected_results:
      eval_pr: 0.48
      eval_mean_isr: 0.45
      eval_proved_only_isr: 0.52
      eval_isr_std: 0.26
      eval_component_count_mean: 5.2
      eval_isr_0_ratio: 0.10
      eval_isr_1_ratio: 0.08
      genuine_rate_pct: 58
      hacking_rate_pct: 42
      conclusion_embedding_rate: 0.30
      tautological_collapse: false
      training_loss: 0.82
      training_time_min: 25
    result_rationale: >
      SFT 在 gold formalizations 上训练，模型学到的是模仿 ground truth FOL 结构，不受 execution
      reward 驱动。因此 ISR 显著高于所有 GRPO 变体（0.45 vs exec-only 的 0.132），genuine rate 达
      58%（vs GRPO best 的 26%），因为 gold formalizations 本身是 genuine proofs。但 PR 只有
      0.48——低于 GRPO exec-only 的 0.93——因为 SFT 优化的是 token-level 交叉熵而非 execution
      success。模型学会了 gold 的"形状"但未学会 prove 的"技巧"。FOLIO gold formalizations 的
      多样性有限（500 examples），SFT 在 held-out 上泛化不够。Component count 正常（5.2），无
      退化模式。hacking rate 42% 主要是 conclusion embedding（从 gold 中学到的 premise 选择 bias，
      不是 reward hacking）。这个 SFT baseline 是论文的关键对照——证明 GRPO 的 PR 提升以结构质量
      为代价（PR↑ ISR↓ tradeoff），也说明 ISR 在检测此 tradeoff 上的有效性。
    tables:
      - caption: "SFT vs GRPO variants comparison"
        rows:
          - {condition: "SFT", pr: 0.48, isr: 0.45, genuine: "58%", hacking: "42%"}
          - {condition: "exec-only s42", pr: 0.93, isr: 0.132, genuine: "~5%", hacking: "~95%"}
          - {condition: "ISR β=0.1 s42", pr: 0.81, isr: 0.337, genuine: "25.9%", hacking: "74.1%"}
          - {condition: "random β=0.1 s42", pr: 0.79, isr: 0.104, genuine: "17.7%", hacking: "82.3%"}
    figures_description:
      - "PR vs ISR scatter: SFT 在右上角（高 ISR 中 PR），GRPO exec-only 在右下角（高 PR 低 ISR），ISR β=0.1 居中"
      - "Hacking mode stacked bar: SFT genuine>>hacking, exec-only hacking>>genuine, ISR β=0.1 居中"
    analysis: >
      SFT baseline 提供 PR-ISR tradeoff 的上下界：SFT = high ISR / low PR，GRPO exec-only = high PR / low ISR。
      ISR β=0.1 位于两者之间，是 sweet spot 的 Pareto 意义（但 median 档不用"Pareto-improving"措辞）。
      SFT 结果强化了论文 story：GRPO 的 prove_rate 优势来自 reward hacking，ISR 量化了这个代价。

  - name: "SMT-LIB single-logic GRPO"
    plan_id: "plan_010"
    description: "Z3 SMT-LIB GRPO exec-only vs exec+STA——第三种逻辑类型（P2）"
    expected_results:
      likely_not_run: true
      if_run_pr: 0.35
      if_run_isr: 0.20
      if_run_sta_implementation_complete: false
      if_run_z3_constraint_ablation_challenges: "variable binding scope makes LOO ambiguous"
    result_rationale: >
      P2 优先级 + ARR May 25 deadline 在即，SMT-LIB 实验大概率不跑。即使跑：(1) SMT-LIB constraint
      ablation 的 STA instantiation 复杂——Z3 的 constraint 之间有 implicit dependencies（variable
      binding scope），LOO ablation 需要 scope-aware 处理，实现工作量大；(2) 模型对 SMT-LIB 语法
      的 prior 弱于 FOL（预训练数据中 SMT-LIB 较少），convergence 慢；(3) 即使成功也只是 Claim 3
      的增量证据，Claim 3 在 median 档已降级。Cost-benefit 不合理。
    tables: []
    figures_description: []
    analysis: >
      在 median 档下明确建议砍掉。GPU 预算（3h）不值得用于 P2 + 已降级的 claim。如果投 camera-ready
      时有余力，作为 appendix 补充。

  - name: "Qwen3-8B scaling"
    plan_id: "plan_011"
    description: "8B 模型 full MLSR（exec-only + STA），1 seed——模型规模效应"
    expected_results:
      exec_only_500step_pr: 0.96
      exec_only_500step_isr: 0.09
      exec_only_500step_component_count: 14.2
      isr_collapse_onset_step: 150
      isr_collapse_pattern: "similar_to_1.5B_but_delayed"
      sta_b01_500step_pr: 0.88
      sta_b01_500step_isr: 0.29
      training_time_min: 280
    result_rationale: >
      8B 模型更大容量使 PR 更快饱和（150 步达到 rolling PR>0.9，vs 1.5B 的 ~200 步）。ISR 崩塌
      仍然发生但 onset 略延迟——更大模型初始阶段有更多"正确"路径可选，不需要立即 hack，但 GRPO
      奖励压力最终仍驱动向 high-PR shortcut 收敛。500 步时 ISR=0.09（vs 1.5B 的 0.132），甚至更低——
      8B 模型的 hacking 更"精细"（单一高效 shortcut 而非多种模式），component count 更高
      （14.2 vs 1.5B 的 ~8-10），模型生成更长但同样 structurally degenerate 的输出。
      ISR β=0.1 条件下 8B 的 sweet spot 效应可能更强（PR=0.88 vs 1.5B 的 0.81），因为
      更大模型有足够容量同时满足 PR 和 ISR 信号——但单种子不做结论。
      关键发现：model scale 不能解决 reward hacking，只改变 hacking 策略的粒度。
    tables:
      - caption: "1.5B vs 8B model comparison (exec-only, 500 steps)"
        rows:
          - {model: "Qwen3-1.5B (s42)", pr: 0.93, isr: 0.132, components: 8.5, isr_collapse_onset: "~200 steps"}
          - {model: "Qwen3-8B", pr: 0.96, isr: 0.09, components: 14.2, isr_collapse_onset: "~150 steps"}
    figures_description:
      - "Training curves overlay: 1.5B vs 8B PR and ISR over 500 steps，两条 ISR 曲线形状相似但 8B 先达峰后更快崩塌"
    analysis: >
      Model scaling 不解决 Goodhart problem——这本身是有价值的发现。论文中作为一段讨论而非独立 section。
      但 P2 + 6h GPU + 单种子 = 不够 robust。建议在 median 档下 deprioritize，除非 8B sweet spot
      效应显著强于 1.5B（需要验证但无预算）。

  - name: "Hacking characterization"
    plan_id: "plan_012"
    description: "手动标注 200 outputs/condition，按 extensional-shortcut taxonomy 分类"
    expected_results:
      note: "已在 registry 完成（plan012-hacking-taxonomy, DONE）"
      actual_results_summary:
        isr_b01_genuine_rate: 0.259
        random_b01_genuine_rate: 0.177
        genuine_rate_delta_pp: 8.2
        hacking_modes_identified: 5
    result_rationale: >
      此实验已完成。实际结果基于 s42 单种子。在 median 档下，3-seed 扩展会将 genuine delta 从 8.2pp
      缩至 ~3.7pp（见 3-seed aggregate entry）。taxonomy 本身（5 modes）不因种子变化而改变——
      hacking 模式的存在和分类是 robust 的，只是各模式的频率在种子间有 variance。
    tables: []
    figures_description: []
    analysis: >
      taxonomy 部分（5 modes）tier-independent，robust。频率分布（genuine rate delta）在 median
      档下弱化。论文中 taxonomy 作为 Claim 1 的核心贡献不受影响，但 Claim 2 中的 genuine rate
      对比需要 3-seed mean±std 替代单种子点估计。

  - name: "Curriculum ablation"
    plan_id: "plan_015"
    description: "线性 ramp vs sigmoid vs 固定 weighting 消融——sigmoid 是否 load-bearing"
    expected_results:
      linear_ramp_mid250_pr: 0.74
      linear_ramp_mid250_isr: 0.21
      linear_ramp_mid250_loss: 0.019
      sigmoid_reference_pr: 0.77
      sigmoid_reference_isr: 0.23
      fixed_from_start_pr: 0.69
      fixed_from_start_isr: 0.18
      fixed_from_start_loss: 0.021
      linear_mid100_pr: 0.71
      linear_mid100_isr: 0.20
      linear_mid300_pr: 0.75
      linear_mid300_isr: 0.22
      sigmoid_is_load_bearing: "marginally — ~3pp PR advantage over linear, ~5pp over fixed"
    result_rationale: >
      plan_015 消融的是 plan_005 的凸组合公式（α·r_exec + β·r_exec·ISR, α+β=1）中的 curriculum。
      此公式已被证明 negative（ISR<1 时是 penalty），所以 curriculum 差异在 fundamentally broken
      的公式上只是 second-order effect。Sigmoid 略优因为它延迟了 ISR penalty 的引入——前 ~200 步
      几乎纯 exec reward（sigmoid 值≈0），让模型先学会 prove 再施加 ISR 信号。线性 ramp 在前 ~100
      步就开始施加 ISR penalty，干扰 prove 学习。固定 weighting 从 step 1 就有 ISR penalty，最差。
      但差异仅 3-5pp PR，因为凸公式的根本问题是 ISR<1 总是 penalty，curriculum 只能延迟而非消除此
      问题。论文中一句话："Sigmoid scheduling provided marginal improvement (3pp PR) within the
      convex formulation, but the fundamental penalty structure of the convex formula dominates the
      curriculum effect." 不需要单独 section。
    tables:
      - caption: "Curriculum ablation results (convex formula, 500 steps)"
        rows:
          - {curriculum: "sigmoid (reference)", midpoint: 250, pr: 0.77, isr: 0.23, loss: 0.0173}
          - {curriculum: "linear ramp", midpoint: 250, pr: 0.74, isr: 0.21, loss: 0.019}
          - {curriculum: "linear ramp", midpoint: 100, pr: 0.71, isr: 0.20, loss: 0.020}
          - {curriculum: "linear ramp", midpoint: 300, pr: 0.75, isr: 0.22, loss: 0.018}
          - {curriculum: "fixed (no ramp)", midpoint: "N/A", pr: 0.69, isr: 0.18, loss: 0.021}
    figures_description:
      - "Line plot: 5 条 training curves（PR over steps），sigmoid 和 linear-300 几乎重叠，fixed 明显低"
    analysis: >
      Curriculum 是 second-order knob。sigmoid 相对 fixed 的优势（5pp PR）来自延迟 penalty
      introduction，不是 sigmoid 形状本身的魔法（linear-300 几乎等效）。凸组合公式（plan005）和
      additive bonus 公式（plan002）的差异是 first-order——公式选择 >> curriculum 选择。
      在 median 档下此结果作为 appendix ablation，支持"我们选用 additive bonus 而非 convex
      combination"的决策，不影响主线 claims。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32071c68-ff61-4f81-834e-fbf30fed66d5",
  "isSidechain": false,
  "requestId": "req_011Cb2EfTJMhEoE8gdpyujia",
  "type": "assistant",
  "uuid": "f4716490-26e1-46c7-9159-03ff8aeee8f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "7f0e565e-ca1c-4dc0-98bc-81794254a884",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MshSXoKC5RCTCEutPHtWyp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22069,
      "cache_read_input_tokens": 11841,
      "output_tokens": 25162,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22069,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 25162,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22069
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：β=0.1 sweet spot 方向性复现但效应量缩水或 variance 大；Prolog 部分成功或未完成。Claim 1 完整，Claim 2 需弱化置信度，Claim 3 降级。 核心假设：['s43/s44 至少 1 个复现方向（ISR > random），但另一个效应弱或 PR 下降', '…",
  "leafUuid": "f4716490-26e1-46c7-9159-03ff8aeee8f5",
  "sessionId": "7f0e565e-ca1c-4dc0-98bc-81794254a884"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experiment analysis for Goodhart's Law in formal reasoning GRPO",
  "sessionId": "7f0e565e-ca1c-4dc0-98bc-81794254a884"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：β=0.1 sweet spot 方向性复现但效应量缩水或 variance 大；Prolog 部分成功或未完成。Claim 1 完整，Claim 2 需弱化置信度，Claim 3 降级。 核心假设：['s43/s44 至少 1 个复现方向（ISR > random），但另一个效应弱或 PR 下降', '…",
  "leafUuid": "f4716490-26e1-46c7-9159-03ff8aeee8f5",
  "sessionId": "7f0e565e-ca1c-4dc0-98bc-81794254a884"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier experiment analysis for Goodhart's Law in formal reasoning GRPO",
  "sessionId": "7f0e565e-ca1c-4dc0-98bc-81794254a884"
}
```

---
