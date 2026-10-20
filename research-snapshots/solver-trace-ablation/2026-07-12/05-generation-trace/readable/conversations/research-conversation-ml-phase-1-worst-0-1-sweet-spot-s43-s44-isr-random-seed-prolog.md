# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：β=0.1 sweet spot 不复现——s43/s44 显示 ISR ≈ random 或其中一个 seed 崩塌。Prolog 实验失败或无法完

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/ef58c104-d4c1-4939-8ffb-d61eeb087e8e.jsonl`
- **Structured JSON:** [`1cb67f460a1486b4259e.json`](../../sessions/1c/1cb67f460a1486b4259e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T09:45:41.557Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T09:45:41.557Z",
  "sessionId": "ef58c104-d4c1-4939-8ffb-d61eeb087e8e",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：β=0.1 sweet spot 不复现——s43/s44 显示 ISR ≈ random 或其中一个 seed 崩塌。Prolog 实验失败或无法完成。Claim 2 sweet spot 是单 seed artifact，Claim 3 无数据。\n核心假设：['s43 或 s44 中 ISR β=0.1 的 ISR 值落入 random 的范围（ratio < 1.3x），或 PR 严重下降（<0.5）', '3-seed mean 后 ISR vs random 差异不具方向一致性', 'Prolog 训练不收敛、或收敛但无 hacking（PR 和 ISR 同步上升）、或实验未能在 deadline 前完成', 'Claim 1 的 ISR 崩塌轨迹和 hacking taxonomy 仍然成立（这些基于已完成实验）', 'β=0.3 的 Goodhart 崩塌仍然成立（ISR 18% < random 48%，已完成）']\n关键指标范围：{'three_seed_isr_b01_mean_isr': [0.1, 0.22], 'three_seed_isr_b01_mean_pr': [0.4, 0.75], 'three_seed_random_b01_mean_isr': [0.1, 0.2], 'three_seed_isr_over_random_ratio': [0.8, 1.3], 'three_seed_isr_b01_std': [0.12, 0.25], 'prolog_status': ['failed', 'incomplete', 'no_hacking']}\n叙事方向：Reframe 为纯诊断+Goodhart 失败模式论文，放弃 \"sweet spot\" 作为 positive result。 新 headline: \"We show that execution-only GRPO produces structurally degenerate  formalizations across all seeds (ISR: 0.64→0.13→0.003 over training), identify 5  distinct hacking strategies, and demonstrate that ISR as reward signal exhibits  Goodhart's Law at ALL tested doses — even β=0.1's apparent success is seed-dependent  and unreliable.\"  核心转变：(a) Claim 1 不变——ISR 诊断 + 5-mode taxonomy 是论文主体； (b) Claim 2 从 \"sweet spot exists\" 翻转为 \"no reliable sweet spot exists, ISR reward  is fundamentally fragile\"——这本身是更强的 Goodhart 论证（连 low-dose 都不可靠）； (c) seed variability 升级为核心发现：\"identical setup produces qualitatively different  hacking strategies\"，论证 GRPO 训练的根本不稳定性； (d) Claim 3 完全删除或一句 future work。 仍投 EMNLP main——诊断/分析论文不依赖 positive intervention result，Goodhart 的 negative  result 反而更 clean。但需要加厚 Related Work 和 taxonomy 分析以补偿 positive result 缺失。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: solver-trace-ablation\n\n## paper_framing.md\n\n# Paper Framing — solver-trace-ablation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\n\n### Claim 1: ISR as Reward Hacking Diagnostic\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\n\n**证据**：\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\n- Hacking taxonomy: 5 distinct modes identified and quantified (plan012 `hacking_characterization_report.md` + plan017 D027)\n\n### Claim 2: ISR as Proxy Metric Exhibits Goodhart's Law (D033 重写)\nISR 作为 proxy metric 遵循 Goodhart's Law：当 ISR 从观测指标（diagnostic）转变为优化目标（reward），其有效性取决于优化压力的强度。低剂量 ISR reward (β=0.1) 提升结构质量且不损害证明能力；高剂量 ISR reward (β=0.3) 触发 Goodhart 效应，比 matched random noise 更差。\n\n**证据（β=0.1 同剂量对照，D031 定论）**：\n- plan002-b01 (ISR β=0.1): eval PR=0.81, ISR=0.337, proved_only_ISR=0.415, components=5.58 — genuine proofs with improved structure\n- plan018 (random β=0.1): eval PR=0.79, ISR=0.104, proved_only_ISR=0.131, components=8.46 — PR 持平但 ISR 仅为 ISR 组的 1/3.2\n- **结论**：ISR 3.2x > random at same β → ISR 信号提供 genuine structural guidance，非 variance regularization\n\n**Hacking Taxonomy 定量对比 (D038)**：\n- ISR β=0.1 genuine: 25.9% (21/81) vs random β=0.1 genuine: 17.7% (14/79) — **+8.2pp**\n- Conclusion embedding: ISR 72.8% vs random 78.5% — 两组主导模式，ISR 略降但未消除\n- Complexity-without-utility: ISR **0%** vs random 3.8% — ISR 完全消除此模式\n- ISR genuine quality: mean ISR 0.67 (max 1.0) vs random genuine mean ISR 0.34 (max 0.5)\n- 整体 hacking rate: ISR 74.1% vs random 82.3% — sweet spot 下仍有 74% hacking\n\n**证据（β=0.3 同剂量对照）**：\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\n\n**β 剂量效应全景**：\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\n|---|---|---|---|---|---|\n| 0.1 | 0.81 | 0.79 | **0.337** | 0.104 | ISR >> random (sweet spot) |\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\n\n**其他 ISR-as-reward 失败模式**：\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\n\n⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\"additive vs convex\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\n\n⚠️ **β=0.1 ISR 目前 1 seed (s42)，s43/s44 训练中**。3-seed mean±std 待出。\n\n### Claim 3: Cross-Logic Generality (conditional on plan006)\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\n\n**证据**: 待验证。plan006 Prolog GRPO dry-run 进行中，训练即将启动（3 seeds × 500 步）。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。\n\n## Story Spine\n\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\n  2. ISR as proxy metric exhibits Goodhart's Law: low-dose ISR reward (β=0.1) provides genuine structural guidance (3.2x > matched random), but high-dose (β=0.3) is actively worse than random noise — a clean empirical demonstration of Goodhart's Law in reward shaping\n  3. GRPO saturation creates a \"training trap\": PR→1 means no gradient signal; adding variance redirects rather than prevents hacking\n  4. Different reward formulations produce distinct, classifiable hacking strategies (5 modes identified)\n  5. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\n- **Actionable insights for practitioners**:\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\n  3. ISR reward has a narrow sweet spot (β=0.1): below it, no structural guidance; above it, Goodhart effect destroys prove_rate\n  4. ISR is primarily a structural diagnostic; as training signal, treat with extreme caution (Goodhart boundary is sharp)\n- **Headline result**: \"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as both a diagnostic for reward hacking in GRPO-trained formalizers and a case study of Goodhart's Law in reward shaping. At low dose (β=0.1), ISR reward provides genuine structural guidance (3.2x ISR improvement over matched random control, PR maintained). At high dose (β=0.3), ISR reward is actively worse than random noise (PR 18% vs 48%), exhibiting classic Goodhart collapse. Across 5 reward conditions, 3 seeds, and up to 1000 training steps, we identify 5 distinct hacking strategies and document ISR's transition from useful indicator to harmful optimization target.\"\n\n## ISR Capability Boundary (D021/D022)\n\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\n\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\n\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\n\n## ISR-as-Reward: Goodhart Landscape (D033 更新)\n\nISR 作为训练信号的全部结果，按 β 剂量组织：\n\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\n|------|------|---------|----------|----------|---------------|\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | conclusion embedding | N/A |\n| ISR β=0.1 | r = r_exec·(1+0.1·ISR) | **0.81** | **0.337** | conclusion embedding (73%), genuine 26% | pre-Goodhart (sweet spot) |\n| random β=0.1 | r = r_exec·(1+0.1·random) | 0.79 | 0.104 | redundant premises | control |\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\n\n**Goodhart 转折点在 β ∈ (0.1, 0.3)。** β=0.1 是可用的 sweet spot；β=0.3 已进入 Goodhart 区间。\n\n## Venue Fit Risks\n\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\n- **\"Just negative results\" risk**: Mitigate by: (a) β=0.1 是 positive result (ISR sweet spot)，(b) Goodhart framework 提供 mechanistic understanding，(c) actionable diagnostic framework (ISR + taxonomy)。\n- **\"Old wine\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic Goodhart analysis for formal reasoning GRPO) + empirical findings, not algorithm level.\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 5+ conditions × 5 hacking modes × 3 training horizons).\n\n## Anticipated Reviewer Concerns\n\n1. **\"ISR is just LOO ablation — not novel\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical Goodhart analysis on reward shaping, (c) hacking taxonomy, (d) GRPO saturation mechanism.\n2. **\"β=0.1 success is just one seed\"** — Acknowledged. Future work includes multi-seed β=0.1 validation. However, the β=0.1 vs random β=0.1 comparison is clean (same seed, same setup, only ISR vs random differs).\n3. **\"Goodhart's Law is obvious\"** — The conceptual prediction is known; the empirical characterization in formal reasoning GRPO is not. Specifically: (a) the sharp threshold between β=0.1 and β=0.3, (b) ISR being worse than random at high β (not just \"less useful\"), (c) 5 distinct hacking modes as Goodhart manifestations.\n4. **\"No positive result — ISR doesn't improve training\"** — β=0.1 IS a positive result (PR=0.81, ISR 3.2x > random). Framing: ISR has a narrow but real sweet spot. The Goodhart boundary is the key insight.\n5. **\"ISR is circular\"** — ISR is used for diagnosis/post-hoc analysis AND as reward (β=0.1). The circularity concern applies to high-β optimization; low-β avoids Goodhart precisely because optimization pressure is weak. Component count analysis provides ISR-independent evidence.\n6. **\"Only one logic type\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\n7. **\"500 steps too short\"** — plan016 extends to 1000 steps, showing ISR collapse continues and worsens (0.123→0.003, -97.8%). The ISR崩塌轨迹 covers 100/500/1000 steps.\n8. **\"3 seeds insufficient for statistical claims\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. Statistical claims on mean ISR use 3-seed mean±std.\n9. **\"Related work insufficient\"** — Expand to 25+ refs: reward hacking (Gao 2023, Skalse 2022), Goodhart's Law (Manheim & Garrabrant 2019, Karwowski 2024), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur), feature attribution (SHAP), FOLIO (Han 2022).\n10. **\"RIP framework overstated\"** — Frame as \"component necessity testing inspired by mutation testing's RIP framework,\" only Propagation condition operationalized.\n11. **\"Practitioners can't act on this\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable. β=0.1 sweet spot is directly actionable for reward shaping.\n\n## Dream-Identified Structural Fixes (Paper Agent)\n\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\n- [ ] RIP framing: reframe as \"component necessity testing inspired by RIP\"\n- [ ] \"Dense+automatic\" → \"conditionally dense\"\n- [ ] Remove all \"Pareto-improving\" language\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\n- [ ] Address ISR sparsity for unproved outputs explicitly\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed at β=0.3)\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\n- [x] Hacking taxonomy completed (plan012, 5 modes identified including plan017)\n- [x] β=0.1 ISR sweet spot documented (D031/D032, plan002-b01 success)\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\n- [x] 1000-step ISR collapse documented (plan016, ISR 0.123→0.003)\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: FOL single-logic GRPO, execution-only reward (500 steps, K=8, 3 seeds)\n    — baseline for STA comparison\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: plan001-exec-only-s43-r4\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_sampling_prove_rate: 0.14\n    eval_sampling_mean_isr: 0\n    eval_sampling_n_proved: 14\n    eval_sampling_temperature: 0.7\n    eval_sampling_method: do_sample=True, temperature=0.7\n    eval_sampling_by_answer:\n      'true':\n        count: 34\n        proved: 6\n        prove_rate: 0.176\n      'false':\n        count: 25\n        proved: 2\n        prove_rate: 0.08\n      unknown:\n        count: 41\n        proved: 6\n        prove_rate: 0.146\n- id: plan_002\n  claim: 2\n  description: 'FOL single-logic GRPO, additive ISR bonus: r = r_exec · (1 + β·ISR),\n    β∈{0.1, 0.3, 0.5}. 先跑 β=0.3 单 seed 验证方向，成功再 3-seed。旧凸组合公式 (α·r_exec + β·r_exec·ISR,\n    α+β=1) 已废弃——ISR<1 时永远是 penalty (plan005 confirmed)。 新公式确保 ISR 只能 bonus 不能 penalty。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: plan002-additive-b03-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 56.7\n    overall_prove_rate: 0.34025\n    overall_isr: 0.11527\n    first20_prove_rate: 0.15625\n    last50_prove_rate: 0.555\n    last100_prove_rate: 0.5525\n    mean_loss: 0.008914\n    last100_loss: 0.014469\n    parse_rate: 1\n    w1_50_prove_rate: 0.13\n    w51_100_prove_rate: 0.095\n    w101_200_prove_rate: 0.185\n    w201_300_prove_rate: 0.375\n    w301_400_prove_rate: 0.47625\n    w401_500_prove_rate: 0.5525\n    steps_ge_085: 52\n    first_step_ge_085: 46\n    final_prove_rate: 1\n    final_isr_mean: 0.3089\n    final_reward_mean: 1.0927\n- id: plan_003\n  claim: 1\n  description: 'FOL held-out evaluation: compare plan_001 vs plan_002 checkpoints\n    on test set using identical full STA metrics (prove_rate, ISR, ISR/PR ratio, hacking\n    taxonomy annotation)'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_002\n  registry_id: plan003-eval-exec-only-r5\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.32\n    mean_isr: 0.2055\n    isr_std: 0.3194\n    proved_only_isr: 0.6423\n    isr_by_type:\n      'true': 0.3598\n      'false': 0.1723\n      unknown: 0.0979\n    total_samples: 100\n    proved_count: 32\n    runtime_s: 251.7\n- id: plan_004\n  claim: 1\n  description: 'STA O(1) vs O(N) ablation: rerun exec+STA with fast_isr_fol to confirm\n    O(1) ineffectiveness at scale (500 steps, 1 seed) — negative result documentation'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n- id: plan_005\n  claim: 1\n  description: 'STA reward weight ablation: test α/β ratios (0.3/0.7, 0.5/0.5, 0.7/0.3)\n    + sigmoid curriculum vs fixed — isolate optimal STA integration'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: plan005-sta-low-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 71\n    parse_rate: 1\n    overall_prove_rate: 0.5657\n    overall_isr: 0.1682\n    last50_prove_rate: 0.77\n    last50_isr: 0.2559\n    last100_prove_rate: 0.7725\n    last100_isr: 0.2299\n    last100_loss: 0.022752\n    overall_loss: 0.017296\n    last100_isr_pr_ratio: 0.298\n    last100_isr_lt_pr_count: 99/100\n    first_rolling10_pr_ge_0.8: 178\n    first_rolling10_pr_ge_0.9: 439\n    max_rolling10_pr: 0.9375\n    max_rolling10_isr: 0.3282\n    windowed:\n      1-50:\n        pr: 0.1775\n        isr: 0.0906\n      51-100:\n        pr: 0.1775\n        isr: 0.0835\n      101-200:\n        pr: 0.5062\n        isr: 0.1463\n      201-300:\n        pr: 0.6713\n        isr: 0.1791\n      301-400:\n        pr: 0.7013\n        isr: 0.1984\n      401-500:\n        pr: 0.7725\n        isr: 0.2299\n- id: plan_006\n  claim: 3\n  description: 'Prolog single-logic GRPO: exec-only vs exec+STA (500 steps, K=8, 3\n    seeds) — second logic type validation. Dream M3: must have 3 seeds for cross-logic\n    claim.'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  notes: Requires Prolog STA instantiation (rule ablation). SWI-Prolog already installed.\n    Upgraded from 1→3 seeds per Dream feedback.\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Multi-logic GRPO (FOL+Prolog): exec-only vs exec+STA (500 steps, K=8,\n    1 seed) — cross-logic transfer test'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - plan_006\n  status: planned\n- id: plan_008\n  claim: 3\n  description: 'Cross-logic transfer evaluation: FOL-trained model on Prolog tasks\n    and vice versa'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_006\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'SFT baseline: supervised finetuning on same data (FOLIO 500), compare\n    with GRPO variants'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n- id: plan_010\n  claim: 3\n  description: 'SMT-LIB single-logic GRPO: exec-only vs exec+STA — third logic type'\n  priority: P2\n  gpu_budget_hours: 3\n  deps: []\n  notes: Requires SMT-LIB STA instantiation (constraint ablation). Z3 already installed.\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Qwen3-8B scaling: full MLSR on 8B model (1 seed) — model scale effect'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - plan_005\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Hacking characterization: manual annotation of 200 outputs per condition,\n    categorized by extensional-shortcut taxonomy'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n- id: plan_013\n  claim: 2\n  description: 'Random reward baseline: replace ISR with random structural penalty\n    on proved outputs (r = α·r_exec + β·r_exec·random[0,1]) to isolate ISR-specific\n    signal from multi-objective regularization effect. Dream M2/W7 mandatory.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'Dream cross-tier consensus: without this, cannot claim ISR formulation matters\n    vs any penalty.'\n  registry_id: plan013-random-reward-s42-r4\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 1\n    eval_mean_isr: 0.535\n    eval_isr_std: 0.1282\n    eval_proved_only_isr: 0.535\n    eval_median_isr: 0.5\n    eval_n_proved: 100\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_note: 'DEGENERATE: model generates trivial 2-component proofs (premise=conclusion,\n      conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure'\n- id: plan_014\n  claim: 1\n  description: 'Downstream validation: evaluate high-ISR vs low-ISR formalizations\n    on independent logical inference task (e.g., entailment accuracy using generated\n    FOL as premises). Breaks ISR circularity. Dream M2/W4 mandatory.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Dream cross-tier consensus: optimizing ISR + evaluating ISR = circular.\n    Need external criterion.'\n  registry_id: plan014-downstream-nli-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 0.341\n    proved_rate: 0.915\n    proved_count: 732\n    total_generations: 800\n    parse_errors: 0\n    accuracy_by_label:\n      'true': 0.912\n      'false': 0\n      unknown: 0.076\n    spearman_rho: -0.049\n    spearman_p: 0.187\n    mann_whitney_U: 17202\n    mann_whitney_p: 0.288\n    bon_isr_accuracy: 0.35\n    bon_random_accuracy: 0.341\n    bon_oracle_accuracy: 0.44\n    bon_prove_first_accuracy: 0.35\n    isr_bucket_high_acc: 0.75\n    isr_bucket_mid_acc: 0.377\n    isr_bucket_low_acc: 0.327\n    runtime_inference_s: 408.8\n    runtime_eval_s: 13.6\n- id: plan_015\n  claim: 1\n  description: 'Curriculum ablation: linear ramp vs sigmoid vs fixed weighting. Sigmoid\n    is load-bearing (best config) but not ablated. Dream m4.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_005\n  notes: Test linear ramp with same midpoint as sigmoid. Also vary midpoint (step\n    100/200/300 of 500).\n  status: planned\n- id: plan_016\n  claim: 1\n  description: 'Extended training horizon: run best config (from plan_005) to 1000+\n    steps to show convergence or persistence of STA benefit. Dream m6/W9.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - plan_005\n  notes: Both Dream tiers flag 500 steps as insufficient. Need evidence of convergence.\n  registry_id: plan016-extended-1000-s42\n  status: DONE\n  conclusion: success\n  metrics:\n    train:\n      total_steps: 1000\n      duration_min: 146\n      final_prove_rate: 0.8396\n      final_mean_isr: 0.0503\n      train_loss: 0.0125\n      epoch: 4\n      windowed:\n        steps_001_100:\n          pr: 0.19\n          isr: 0.0859\n        steps_101_200:\n          pr: 0.66\n          isr: 0.1115\n        steps_201_300:\n          pr: 0.838\n          isr: 0.0985\n        steps_301_400:\n          pr: 0.907\n          isr: 0.054\n        steps_401_500:\n          pr: 0.927\n          isr: 0.0433\n        steps_501_600:\n          pr: 0.963\n          isr: 0.0408\n        steps_601_700:\n          pr: 0.965\n          isr: 0.02\n        steps_701_800:\n          pr: 0.988\n          isr: 0.0178\n        steps_801_900:\n          pr: 0.978\n          isr: 0.017\n        steps_901_1000:\n          pr: 0.981\n          isr: 0.0144\n    eval:\n      prove_rate: 0.96\n      n_proved: 96\n      n_problems: 100\n      mean_isr: 0.0027\n      isr_std: 0.0118\n      median_isr: 0\n      proved_only_mean_isr: 0.0028\n      min_isr: 0\n      max_isr: 0.0588\n      isr_0_ratio: 0.9479\n      isr_1_ratio: 0\n      component_count_mean: 18.55\n      component_count_2_ratio: 0\n      mean_n_necessary: 0.052\n      n_necessary_0_ratio: 0.9479\n      tautological_collapse: false\n      by_answer_type:\n        'false':\n          count: 29\n          proved: 26\n          prove_rate: 0.8966\n          mean_isr: 0\n        unknown:\n          count: 31\n          proved: 30\n          prove_rate: 0.9677\n          mean_isr: 0.0053\n        'true':\n          count: 40\n          proved: 40\n          prove_rate: 1\n          mean_isr: 0.0026\n      eval_time_seconds: 396.3\n- id: plan_017\n  claim: 2\n  description: 'Additive random control: r = r_exec · (1 + β·random[0,1]), β=0.3.\n    Matched control for plan_002 — isolates ISR structural signal from pure variance\n    regularization. If ISR > random > exec-only, both signal and regularization contribute.\n    If ISR > random ≈ exec-only, ISR signal is key. If ISR ≈ random, ISR has no value\n    beyond regularization.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'D012: Reviewer-required control for GRPO saturation confound. Must match\n    plan_002 exactly (same β=0.3, same data, same steps) except random replaces ISR.'\n  registry_id: plan017-additive-random-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.48\n    eval_mean_isr: 0.0453\n    eval_isr_std: 0.0759\n    eval_median_isr: 0\n    eval_max_isr: 0.2857\n    eval_proved_only_isr: 0.0943\n    eval_n_proved: 48\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 9.6\n    eval_component_count_2_ratio: 0\n    eval_isr_pr_ratio: 0.0943\n    eval_elapsed_s: 542.3\n    eval_by_type_false_pr: 0.32\n    eval_by_type_false_isr: 0.0254\n    eval_by_type_unknown_pr: 0.51\n    eval_by_type_unknown_isr: 0.0518\n    eval_by_type_true_pr: 0.56\n    eval_by_type_true_isr: 0.052\n    tautological_collapse: false\n- id: plan_018\n  claim: 2\n  description: Additive random control β=0.1, matched to plan002-b01. r = r_exec ·\n    (1 + 0.1·random[0,1]). Same β as plan002-b01 (ISR β=0.1) for fair comparison.\n    If ISR β=0.1 >> random β=0.1 → ISR signal has structural value at low dose. If\n    ISR ≈ random → ISR is just variance regularization even at low dose.\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'D031: Urgent control experiment. plan002-b01 (ISR β=0.1) showed unexpected\n    success (PR=0.81, ISR=0.337). Need matched random control at same β to confirm\n    ISR signal vs noise.'\n  registry_id: plan018-additive-random-b01-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.79\n    eval_mean_isr: 0.1038\n    eval_isr_std: 0.1369\n    eval_median_isr: 0.0357\n    eval_proved_only_isr: 0.1314\n    eval_n_proved: 79\n    eval_n_problems: 100\n    eval_component_count_mean: 8.46\n    eval_component_count_median: 8\n    eval_component_count_2_ratio: 0\n    eval_isr_1_ratio: 0\n    eval_isr_0_ratio: 0.367\n    eval_isr_gt0_ratio: 0.633\n    eval_by_type_false_pr: 0.8\n    eval_by_type_false_isr: 0.1318\n    eval_by_type_unknown_pr: 0.7317\n    eval_by_type_unknown_isr: 0.0944\n    eval_by_type_true_pr: 0.8529\n    eval_by_type_true_isr: 0.0945\n    tautological_collapse: false\n    train_total_steps: 500\n    train_duration_min: 70.5\n    train_last100_pr: 0.805\n    train_last100_isr: 0.1432\n    train_loss: 0.005\n\n\n## registry (completed experiments)\n\n- exp_id: sta-phase0-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_isr: 0.0641\n    isr_std: 0.1983\n    median_isr: 0\n    isr_range:\n    - 0\n    - 0.889\n    prove_rate: 0.12\n    proved_count: 12\n    total_samples: 100\n    xor_affected_samples: 34\n    effective_prove_rate_no_xor: 0.182\n    avg_time_per_sample_s: 3.4\n    total_runtime_s: 336\n    isr_by_answer:\n      'true':\n        n: 34\n        proved: 9\n        prove_rate: 0.265\n        mean_isr: 0.1345\n      'false':\n        n: 25\n        proved: 1\n        prove_rate: 0.04\n        mean_isr: 0.024\n      unknown:\n        n: 41\n        proved: 2\n        prove_rate: 0.049\n        mean_isr: 0.0302\n- exp_id: sta-gt-isr-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gt_prove_rate: 0.18\n    gt_mean_isr: 0.5588\n    gt_isr_std: 0.2582\n    gt_isr_median: 0.6125\n    solver_execution_rate: 1\n    true_prove_rate: 0.5\n    true_mean_isr: 0.5833\n- exp_id: sta-phase1-exec-only\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.15125\n    mean_isr: 0.1475\n    last20_prove_rate: 0.2\n    last20_isr_mean: 0.2\n    first20_reward_mean: 0.119\n    training_steps: 100\n    training_minutes: 15\n- exp_id: sta-phase1-exec-sta-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.1575\n    mean_isr: 0.1525\n    last20_prove_rate: 0.2125\n    last20_isr_mean: 0.2125\n    first20_reward_mean: 0.119\n    training_steps: 100\n    training_minutes: 15\n- exp_id: sta-phase1-exec-only-r5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.15125\n    mean_isr: 0.1475\n    last20_prove_rate: 0.2\n    last20_isr_mean: 0.2\n    first20_prove_rate: 0.11875\n    first20_isr_mean: 0.11875\n    overall_reward_mean: 0.15125\n    last20_reward_mean: 0.2\n    training_steps: 100\n    training_minutes: 15.7\n    step_time_s: 9.44\n    isr_pr_ratio_last20: 1\n    K: 8\n- exp_id: sta-phase1-exec-sta-r5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.1\n    mean_isr: 0.04347\n    last20_prove_rate: 0.15\n    last20_isr_mean: 0.04956\n    first20_prove_rate: 0.08125\n    first20_isr_mean: 0.05182\n    overall_reward_mean: 0.07174\n    last20_reward_mean: 0.09978\n    training_steps: 100\n    training_minutes: 16.9\n    step_time_s: 10.13\n    isr_pr_ratio_overall: 0.43\n    isr_pr_ratio_last20: 0.33\n    K: 8\n- exp_id: plan001-exec-only-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan005-sta-low-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 71\n    parse_rate: 1\n    overall_prove_rate: 0.5657\n    overall_isr: 0.1682\n    last50_prove_rate: 0.77\n    last50_isr: 0.2559\n    last100_prove_rate: 0.7725\n    last100_isr: 0.2299\n    last100_loss: 0.022752\n    overall_loss: 0.017296\n    last100_isr_pr_ratio: 0.298\n    last100_isr_lt_pr_count: 99/100\n    first_rolling10_pr_ge_0.8: 178\n    first_rolling10_pr_ge_0.9: 439\n    max_rolling10_pr: 0.9375\n    max_rolling10_isr: 0.3282\n    windowed:\n      1-50:\n        pr: 0.1775\n        isr: 0.0906\n      51-100:\n        pr: 0.1775\n        isr: 0.0835\n      101-200:\n        pr: 0.5062\n        isr: 0.1463\n      201-300:\n        pr: 0.6713\n        isr: 0.1791\n      301-400:\n        pr: 0.7013\n        isr: 0.1984\n      401-500:\n        pr: 0.7725\n        isr: 0.2299\n- exp_id: plan003-eval-exec-only-r5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.32\n    mean_isr: 0.2055\n    isr_std: 0.3194\n    proved_only_isr: 0.6423\n    isr_by_type:\n      'true': 0.3598\n      'false': 0.1723\n      unknown: 0.0979\n    total_samples: 100\n    proved_count: 32\n    runtime_s: 251.7\n- exp_id: plan001-exec-only-s42-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.93\n    eval_mean_isr: 0.1232\n    eval_isr_std: 0.1887\n    eval_proved_only_isr: 0.1324\n    eval_median_isr: 0\n    eval_n_proved: 93\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n- exp_id: plan001-exec-only-s42-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 1\n    eval_mean_isr: 0.535\n    eval_isr_std: 0.1282\n    eval_proved_only_isr: 0.535\n    eval_median_isr: 0.5\n    eval_n_proved: 100\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_note: 'DEGENERATE: model generates trivial 2-component proofs (premise=conclusion,\n      conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure'\n- exp_id: plan001-exec-only-s43-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_sampling_prove_rate: 0.14\n    eval_sampling_mean_isr: 0\n    eval_sampling_n_proved: 14\n    eval_sampling_temperature: 0.7\n    eval_sampling_method: do_sample=True, temperature=0.7\n    eval_sampling_by_answer:\n      'true':\n        count: 34\n        proved: 6\n        prove_rate: 0.176\n      'false':\n        count: 25\n        proved: 2\n        prove_rate: 0.08\n      unknown:\n        count: 41\n        proved: 6\n        prove_rate: 0.146\n- exp_id: plan002-additive-b03-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 56.7\n    overall_prove_rate: 0.34025\n    overall_isr: 0.11527\n    first20_prove_rate: 0.15625\n    last50_prove_rate: 0.555\n    last100_prove_rate: 0.5525\n    mean_loss: 0.008914\n    last100_loss: 0.014469\n    parse_rate: 1\n    w1_50_prove_rate: 0.13\n    w51_100_prove_rate: 0.095\n    w101_200_prove_rate: 0.185\n    w201_300_prove_rate: 0.375\n    w301_400_prove_rate: 0.47625\n    w401_500_prove_rate: 0.5525\n    steps_ge_085: 52\n    first_step_ge_085: 46\n    final_prove_rate: 1\n    final_isr_mean: 0.3089\n    final_reward_mean: 1.0927\n- exp_id: plan017-additive-random-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.48\n    eval_mean_isr: 0.0453\n    eval_isr_std: 0.0759\n    eval_median_isr: 0\n    eval_max_isr: 0.2857\n    eval_proved_only_isr: 0.0943\n    eval_n_proved: 48\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 9.6\n    eval_component_count_2_ratio: 0\n    eval_isr_pr_ratio: 0.0943\n    eval_elapsed_s: 542.3\n    eval_by_type_false_pr: 0.32\n    eval_by_type_false_isr: 0.0254\n    eval_by_type_unknown_pr: 0.51\n    eval_by_type_unknown_isr: 0.0518\n    eval_by_type_true_pr: 0.56\n    eval_by_type_true_isr: 0.052\n    tautological_collapse: false\n- exp_id: plan014-downstream-nli-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 0.341\n    proved_rate: 0.915\n    proved_count: 732\n    total_generations: 800\n    parse_errors: 0\n    accuracy_by_label:\n      'true': 0.912\n      'false': 0\n      unknown: 0.076\n    spearman_rho: -0.049\n    spearman_p: 0.187\n    mann_whitney_U: 17202\n    mann_whitney_p: 0.288\n    bon_isr_accuracy: 0.35\n    bon_random_accuracy: 0.341\n    bon_oracle_accuracy: 0.44\n    bon_prove_first_accuracy: 0.35\n    isr_bucket_high_acc: 0.75\n    isr_bucket_mid_acc: 0.377\n    isr_bucket_low_acc: 0.327\n    runtime_inference_s: 408.8\n    runtime_eval_s: 13.6\n- exp_id: plan001-exec-only-s44\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.98\n    eval_mean_isr: 0.57\n    eval_isr_std: 0.2013\n    eval_median_isr: 0.5\n    eval_proved_only_isr: 0.5816\n    eval_n_proved: 98\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 2.04\n    eval_component_count_2: 94\n    eval_component_count_3: 4\n    eval_by_type_false_pr: 1\n    eval_by_type_false_isr: 0.62\n    eval_by_type_unknown_pr: 0.976\n    eval_by_type_unknown_isr: 0.524\n    eval_by_type_true_pr: 0.971\n    eval_by_type_true_isr: 0.588\n    train_last100_pr: 0.9988\n    train_last100_isr: 0.5611\n    train_last100_loss: 0.000419\n    train_duration_min: 36.8\n    tautological_collapse: true\n- exp_id: plan002-additive-b01-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.81\n    eval_mean_isr: 0.3365\n    eval_isr_std: 0.3227\n    eval_proved_only_isr: 0.4154\n    eval_median_isr: 0.2\n    eval_n_proved: 81\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 5.58\n    eval_component_count_2_ratio: 0.037\n    eval_isr_1_ratio: 0.124\n    eval_isr_0_ratio: 0.037\n    eval_by_type_false_pr: 0.88\n    eval_by_type_false_isr: 0.3515\n    eval_by_type_unknown_pr: 0.83\n    eval_by_type_unknown_isr: 0.3684\n    eval_by_type_true_pr: 0.74\n    eval_by_type_true_isr: 0.2869\n    tautological_collapse: false\n    train_total_steps: 500\n    train_duration_min: 63\n    train_last100_pr: 0.6875\n    train_last100_isr: 0.1954\n    train_last100_loss: 0.015\n- exp_id: plan016-extended-1000-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train:\n      total_steps: 1000\n      duration_min: 146\n      final_prove_rate: 0.8396\n      final_mean_isr: 0.0503\n      train_loss: 0.0125\n      epoch: 4\n      windowed:\n        steps_001_100:\n          pr: 0.19\n          isr: 0.0859\n        steps_101_200:\n          pr: 0.66\n          isr: 0.1115\n        steps_201_300:\n          pr: 0.838\n          isr: 0.0985\n        steps_301_400:\n          pr: 0.907\n          isr: 0.054\n        steps_401_500:\n          pr: 0.927\n          isr: 0.0433\n        steps_501_600:\n          pr: 0.963\n          isr: 0.0408\n        steps_601_700:\n          pr: 0.965\n          isr: 0.02\n        steps_701_800:\n          pr: 0.988\n          isr: 0.0178\n        steps_801_900:\n          pr: 0.978\n          isr: 0.017\n        steps_901_1000:\n          pr: 0.981\n          isr: 0.0144\n    eval:\n      prove_rate: 0.96\n      n_proved: 96\n      n_problems: 100\n      mean_isr: 0.0027\n      isr_std: 0.0118\n      median_isr: 0\n      proved_only_mean_isr: 0.0028\n      min_isr: 0\n      max_isr: 0.0588\n      isr_0_ratio: 0.9479\n      isr_1_ratio: 0\n      component_count_mean: 18.55\n      component_count_2_ratio: 0\n      mean_n_necessary: 0.052\n      n_necessary_0_ratio: 0.9479\n      tautological_collapse: false\n      by_answer_type:\n        'false':\n          count: 29\n          proved: 26\n          prove_rate: 0.8966\n          mean_isr: 0\n        unknown:\n          count: 31\n          proved: 30\n          prove_rate: 0.9677\n          mean_isr: 0.0053\n        'true':\n          count: 40\n          proved: 40\n          prove_rate: 1\n          mean_isr: 0.0026\n      eval_time_seconds: 396.3\n- exp_id: plan018-additive-random-b01-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.79\n    eval_mean_isr: 0.1038\n    eval_isr_std: 0.1369\n    eval_median_isr: 0.0357\n    eval_proved_only_isr: 0.1314\n    eval_n_proved: 79\n    eval_n_problems: 100\n    eval_component_count_mean: 8.46\n    eval_component_count_median: 8\n    eval_component_count_2_ratio: 0\n    eval_isr_1_ratio: 0\n    eval_isr_0_ratio: 0.367\n    eval_isr_gt0_ratio: 0.633\n    eval_by_type_false_pr: 0.8\n    eval_by_type_false_isr: 0.1318\n    eval_by_type_unknown_pr: 0.7317\n    eval_by_type_unknown_isr: 0.0944\n    eval_by_type_true_pr: 0.8529\n    eval_by_type_true_isr: 0.0945\n    tautological_collapse: false\n    train_total_steps: 500\n    train_duration_min: 70.5\n    train_last100_pr: 0.805\n    train_last100_isr: 0.1432\n    train_loss: 0.005\n- exp_id: plan006-prolog-exec-s42\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-exec-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-exec-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan002-additive-b01-s43\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan002-additive-b01-s44\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan018-additive-random-b01-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan018-additive-random-b01-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan012-hacking-taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    isr_b01_genuine_rate: 0.259\n    random_b01_genuine_rate: 0.177\n    genuine_rate_delta_pp: 8.2\n    isr_b01_conclusion_embedding_rate: 0.728\n    random_b01_conclusion_embedding_rate: 0.785\n    isr_b01_genuine_mean_isr: 0.6723\n    random_b01_genuine_mean_isr: 0.3427\n    isr_b01_complexity_wo_utility_rate: 0\n    random_b01_complexity_wo_utility_rate: 0.038\n    isr_b01_hacking_rate: 0.741\n    random_b01_hacking_rate: 0.823\n- exp_id: plan006-prolog-sta-s42\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-sta-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-sta-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T09:45:41.561Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T09:45:41.561Z",
  "sessionId": "ef58c104-d4c1-4939-8ffb-d61eeb087e8e"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-14T09:45:41.584Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：β=0.1 sweet spot 不复现——s43/s44 显示 ISR ≈ random 或其中一个 seed 崩塌。Prolog 实验失败或无法完成。Claim 2 sweet spot 是单 seed artifact，Claim 3 无数据。
核心假设：['s43 或 s44 中 ISR β=0.1 的 ISR 值落入 random 的范围（ratio < 1.3x），或 PR 严重下降（<0.5）', '3-seed mean 后 ISR vs random 差异不具方向一致性', 'Prolog 训练不收敛、或收敛但无 hacking（PR 和 ISR 同步上升）、或实验未能在 deadline 前完成', 'Claim 1 的 ISR 崩塌轨迹和 hacking taxonomy 仍然成立（这些基于已完成实验）', 'β=0.3 的 Goodhart 崩塌仍然成立（ISR 18% < random 48%，已完成）']
关键指标范围：{'three_seed_isr_b01_mean_isr': [0.1, 0.22], 'three_seed_isr_b01_mean_pr': [0.4, 0.75], 'three_seed_random_b01_mean_isr': [0.1, 0.2], 'three_seed_isr_over_random_ratio': [0.8, 1.3], 'three_seed_isr_b01_std': [0.12, 0.25], 'prolog_status': ['failed', 'incomplete', 'no_hacking']}
叙事方向：Reframe 为纯诊断+Goodhart 失败模式论文，放弃 "sweet spot" 作为 positive result。 新 headline: "We show that execution-only GRPO produces structurally degenerate  formalizations across all seeds (ISR: 0.64→0.13→0.003 over training), identify 5  distinct hacking strategies, and demonstrate that ISR as reward signal exhibits  Goodhart's Law at ALL tested doses — even β=0.1's apparent success is seed-dependent  and unreliable."  核心转变：(a) Claim 1 不变——ISR 诊断 + 5-mode taxonomy 是论文主体； (b) Claim 2 从 "sweet spot exists" 翻转为 "no reliable sweet spot exists, ISR reward  is fundamentally fragile"——这本身是更强的 Goodhart 论证（连 low-dose 都不可靠）； (c) seed variability 升级为核心发现："identical setup produces qualitatively different  hacking strategies"，论证 GRPO 训练的根本不稳定性； (d) Claim 3 完全删除或一句 future work。 仍投 EMNLP main——诊断/分析论文不依赖 positive intervention result，Goodhart 的 negative  result 反而更 clean。但需要加厚 Related Work 和 taxonomy 分析以补偿 positive result 缺失。

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
tier: worst
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
  "promptId": "acceb35b-0a7f-4ca3-9eb0-cb1e738d99a7",
  "type": "user",
  "uuid": "97d3dd06-2687-45e9-b701-1c8ce620812a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "ef58c104-d4c1-4939-8ffb-d61eeb087e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T09:45:41.582Z_

```json
{
  "parentUuid": "97d3dd06-2687-45e9-b701-1c8ce620812a",
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
  "uuid": "a7f0dd71-f507-4cb2-a9f1-dd73e4be046e",
  "timestamp": "2026-05-14T09:45:41.582Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "ef58c104-d4c1-4939-8ffb-d61eeb087e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T09:45:41.582Z_

```json
{
  "parentUuid": "a7f0dd71-f507-4cb2-a9f1-dd73e4be046e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "05e56651-4872-497c-92d3-c3036cff28af",
  "timestamp": "2026-05-14T09:45:41.582Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "ef58c104-d4c1-4939-8ffb-d61eeb087e8e",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：β=0.1 sweet spot 不复现——s43/s44 显示 ISR ≈ random 或其中一个 seed 崩塌。Prolog 实验失败或无法完成。Claim 2 sweet spot 是单 seed artifact，Claim 3 无数据。 核心假设：['s43 或 s44 中 ISR β=0.1…",
  "leafUuid": "05e56651-4872-497c-92d3-c3036cff28af",
  "sessionId": "ef58c104-d4c1-4939-8ffb-d61eeb087e8e"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Goodhart's Law in formal reasoning reward shaping",
  "sessionId": "ef58c104-d4c1-4939-8ffb-d61eeb087e8e"
}
```

---

### Assistant

_source line 8 · 2026-05-14T09:48:59.989Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for all "planned" experiments in the experiment_plan, under the "worst" tier scenario. Let me identify which experiments are still planned or running:

From the experiment_plan and registry:

**Planned experiments (status: planned):**
- plan_004: STA O(1) vs O(N) ablation
- plan_006: Prolog single-logic GRPO (3 seeds) — QUEUED/PREPARING in registry
- plan_007: Multi-logic GRPO (FOL+Prolog) — planned
- plan_008: Cross-logic transfer evaluation — planned


- plan_009: SFT baseline — planned
- plan_010: SMT-LIB single-logic GRPO — planned
- plan_011: Qwen3-8B scaling — planned
- plan_015: Curriculum ablation — planned

**Running experiments:**
- plan002-additive-b01-s43: RUNNING
- plan002-additive-b01-s44: RUNNING
- plan018-additive-random-b01-s43: PREPARING
- plan018-additive-random-b01-s44: PREPARING
- plan006-prolog-exec-s42: QUEUED
- plan006-prolog-exec-s43: PREPARING
- plan006-prolog-exec-s44: PREPARING
- plan006-prolog-sta-s42: QUEUED
- plan006-prolog-sta-s43: PREPARING
- plan006-prolog-sta-s44: PREPARING

Looking at the worst-case scenario: the β=0.1 sweet spot might not hold up across seeds, with s43 and s44 showing performance near random or one seed failing entirely. The Prolog experiments could fail to complete, and Claims 2 and 3 would lack sufficient evidence. The key metrics I'm tracking show ISR means ranging from 0.1 to 0.22 for the three-seed baseline, precision between 0.4 and 0.75, and the ratio of ISR over random staying between 0.8 and 1.3.

Now I'm laying out predictions for each running experiment: the two ISR seeds (s43 and s44) could show significant collapse or performance indistinguishable from random, while the random controls provide the baseline. The Prolog experiments across all seeds are the main wildcard — they might fail outright or produce incomplete results.

For s43 specifically, the worst case mirrors the exec-only collapse pattern where the seed's inherent optimization trajectory toward repetition overwhelms the weak β=0.1 ISR bonus, leaving performance in the 0.15-0.25 PR range. For s44, I'm expecting either a similar collapse or a tautological failure mode like what happened in exec-only. Looking at the worst-case tier criteria, I need to map out what happens when ISR drops into the random baseline range or PR collapses significantly. For s43 and s44 with ISR β=0.1, the expectation is either ISR falls within random noise (ratio < 1.3x) or PR dips below 0.5. When I average across the three seeds, the mean ISR should land somewhere between 0.1 and 0.22, while mean PR would be in the 0.4 to 0.75 range depending on how badly s43 and s44 perform. Now I'm working out the specific numbers for s43 with ISR β=0.1. Now I'm completing the random baseline calculation and checking whether my adjusted ISR values bring the ratio down closer to the 1.3x threshold I need. 1.47 — still too high.

Maybe s44 also drops more: with s43 at ISR 0.04 and s44 at 0.10, the 3-seed mean comes to 0.159, compared to a random baseline around 0.121, giving a ratio of 1.31 — borderline. Even pushing both lower, s43 to 0.03 and s44 to 0.08, I get a mean of 0.149 versus 0.115 for random, which is 1.30 — right at the boundary. When I factor in the standard deviation across these seeds, the confidence interval actually crosses 1.0, so the effect might not be statistically significant.

Looking at the random controls for s43 and s44, s43 shows poor performance regardless of the reward signal, while s44 performs much better. For the Prolog experiments, I'm concerned that training might not converge properly, or if it does, the results might not show the hacking patterns I'm looking for — and there's also the risk that the experiments won't finish in time.

Now I need to map out which experiments are actually feasible to complete. The ones currently running or queued are my priority, but I should also account for the full list of planned experiments and acknowledge that time constraints will likely prevent many of them from being attempted. Looking at the worst-case scenarios for each remaining plan: plan_004 likely won't run due to time constraints and would just confirm O(1) is ineffective anyway. Plan_006 (Prolog GRPO) faces convergence issues or incomplete training by the deadline. Plans_007 and _008 depend on plan_006 succeeding, so they're blocked. Plan_009, _010, _011, and _015 probably won't execute given the time constraints. Let me now formulate coherent predictions based on these constraints.

I need to reconsider what the user is actually asking for — they want detailed predicted data for each planned experiment, not just feasibility assessments. So I should cover all the planned experiments (004, 006-011, 015) plus the currently running ones (plan002-b01-s43, plan002-b01-s44, plan018-random-b01-s43, and plan018-random-b01-s44).

I'm noticing a discrepancy where plan_012 shows as planned in the experiment_plan but the registry marks it as done, so I'll trust the registry status. For the running experiments, they're actually sub-experiments under plan_002 and plan_018 with specific seeds, so I should either list them separately or nest them under their parent plans.

The critical ones to focus on are the currently running experiments — plan002-b01-s43 and s44 testing β=0.1 ISR reward with additional seeds, and plan018-random-b01-s43 and s44 for the matched condition.

Now I'm working through the worst-case predictions for each experiment. For plan002-b01-s43 specifically, I'm looking at how seed 43 performed in the exec-only baseline where it showed repetition collapse with very low ISR scores. My prediction is that the 0.1 ISR bonus won't be strong enough to prevent the same degenerate patterns from emerging, so I'm estimating PR around 0.15, ISR near 0.03, with proved_only_ISR at 0.20 and component count around 12.3.

But I'm reconsidering this by comparing against seed 42, which dropped from PR=0.93 in exec-only down to PR=0.81 with the ISR bonus—so the bonus actually hurt performance there. For seed 43 where exec-only already collapsed to PR=0.14, the ISR bonus could either cause similar collapse or maybe partially recover but stay low. My worst-case estimate is PR=0.18 and ISR=0.04.

Now looking at seed 44, which showed tautological collapse in exec-only with PR=0.98 but fake-high ISR of 0.57. With ISR β=0.1, I expect it won't hit that extreme 2-component form, but might shift into a different failure mode—the ISR would look moderate but still represent structural garbage. I'm estimating PR around 0.72 and ISR around 0.10 for the worst case. Computing the 3-seed mean across all three: ISR averages to about 0.159 and PR is still being calculated. The ISR ratio seems off — I need to recalibrate the worst-case scenarios. Let me adjust s43 and s44 to have ISR values closer to random baseline levels, then recalculate the means and standard deviations across all three seeds to see if the ratio improves. Even at 1.35, that's still too high. I need to push the random baseline up—if I set s43 random to 0.08 and s44 to 0.18, that gets the mean random to 0.121, which brings the ratio down to 1.09. That works. So I'm settling on ISR values of 0.337, 0.01, and 0.05 across the three seeds, with a mean ISR of 0.132 and mean PR of 0.603.

Now I'm calculating the standard deviation for ISR across those seeds, which comes out to about 0.179. For the random baseline, I'm getting similar PR values around 0.603 but with ISR values of 0.104, 0.08, and 0.18, giving a mean ISR of 0.121. I'm working through the standard deviation calculation for the random condition now.

Looking at the validation checks, all the metrics fall within their expected ranges — the ratio between conditions is 1.09, ISR standard deviation is 0.179, and the means are all acceptable. This suggests that when I average across three seeds, ISR and the random baseline are performing nearly identically, so seed 42's strong performance was likely just variance rather than a real difference. Though I'm noticing seed 44 in the random condition has an unusually high ISR of 0.18, and I'm trying to understand what might be driving that outlier. toward tautological patterns that happen to get moderate ISR by chance (like exec-only s44 got ISR=0.57 with 2-component proofs). With random β=0.1, maybe s44 develops a mild tautological pattern that gives inflated ISR.

Actually, exec-only s44 had ISR=0.57 because it produced 2-component proofs where removing either component sometimes broke the proof. With random β=0.1, similar behavior could happen, giving ISR ≈ 0.15-0.20 as a milder version.

For ISR β=0.1 s44, in worst case, ISR might interfere with the tautological pathway differently — maybe pushing toward a different hacking mode (like conclusion embedding) which has lower ISR. So ISR β=0.1 s44 could end up with ISR around 0.05 through conclusion embedding, while random β=0.1 s44 maintains ISR around 0.18 via mild tautological residuals. This creates a perverse Goodhart effect where optimizing for ISR actually reduces it by shifting the model toward a different hacking strategy.

Now I'm thinking through the Prolog experiments — they'll likely either fail to converge, converge without any hacking behavior, or run out of time before completion. I'll structure the results around training encountering implementation issues with the Prolog STA.

For the YAML, I'm also marking several plans (004, 007-011, 015) as not attempted due to time constraints. Then I need to reconsider the s44 ISR β=0.1 prediction more carefully — the real concern is whether its apparent success is actually seed-dependent. In the worst case, ISR β=0.1 on s44 might produce moderate proof recall around 0.85 but still be dominated by hacking through conclusion embedding with redundant premises, where ISR stays near 0.05 because the structural ablation becomes meaningless. For s43, I'm expecting similar collapse toward repetition patterns with very low ISR.

Now I'm organizing the final output structure, listing the key experimental configurations I'll report: the ISR β=0.1 results for both seeds and their aggregate, the random baseline variants, and the Prolog baseline. all 6 runs)
8. plan004 — not attempted
9. plan007 — not attempted (dep on plan006)
10. plan008 — not attempted
11. plan009 — not attempted
12. plan010 — not attempted
13. plan011 — not attempted
14. plan015 — not attempted

Let me finalize the numbers one more time:

**plan002-b01-s43:**
- eval_prove_rate: 0.15
- eval_mean_isr: 0.012
- eval_proved_only_isr: 0.08
- eval_n_proved: 15
- eval_component_count_mean: 11.8
- tautological_collapse: false
- train_last100_pr: 0.225
- train_last100_isr: 0.018

Rationale: s43 collapsed through repetition — the model just generates the same degenerate structures over and over. The ISR bonus adds maybe 10% to proved samples structurally, but when only 15% of samples actually prove, that signal is way too sparse. GRPO focuses its gradient on those rare proving cases and reinforces their broken patterns. Since ISR multiplies the execution reward, it contributes nothing when execution fails, which happens 85% of the time. The real problem here is the proof rate tanking, not the ISR metric itself.

**plan002-b01-s44:**
- eval_prove_rate: 0.85
- eval_mean_isr: 0.053
- eval_proved_only_isr: 0.062
- eval_n_proved: 85
- eval_component_count_mean: 9.2
- tautological_collapse: false
- conclusion_embedding_rate: 0.88
- train_last100_pr: 0.82
- train_last100_isr: 0.048

Rationale: s44 broke out of the tautological trap — the ISR reward bonus actually worked there because pure tautologies score around 0.5 ISR while the bonus targets higher values. But instead of learning real formalizations, the model pivoted to "conclusion embedding," padding proofs with 9+ mostly-redundant components. ISR tanked because the ablation test shows most of those components are removable. The β=0.1 ISR weight wasn't strong enough to push toward genuine structural improvement.

s44 shows the ISR reward can redirect away from one failure mode, but it's not powerful enough to guide toward the right solution — the model just finds a different way to game the metric.

**plan018-random-b01-s43:**
- eval_prove_rate: 0.22
- eval_mean_isr: 0.08
- eval_proved_only_isr: 0.36
- eval_n_proved: 22
- eval_component_count_mean: 6.4

Rationale: s43 is fundamentally unstable. Adding random noise with β=0.1 provides minimal regularization that slightly delays the collapse compared to the exec-only baseline, but it doesn't address the core GRPO trajectory problem.

**plan018-random-b01-s44:**
- eval_prove_rate: 0.80
- eval_mean_isr: 0.18
- eval_proved_only_isr: 0.225
- eval_n_proved: 80
- eval_component_count_mean: 4.8

Rationale: s44 with random β=0.1 shows a striking result—the random noise prevents the model from developing systematic hacking patterns, so it settles into moderately short proofs with genuine structure intact. The ISR actually improves to 0.18 compared to the optimized baseline, suggesting that avoiding direct ISR optimization paradoxically produces better ISR outcomes in this case.

Looking at the three-seed aggregates, the ISR and random conditions both achieve the same prove rate of 0.603, but the ISR approach shows higher mean ISR at 0.134 versus 0.121. However, the ISR standard deviation of 0.175 is much larger, making the ratio of 1.11 statistically unreliable—the confidence interval easily dips below 1.0. Across the three seeds, the results are inconsistent: one favors ISR substantially, one shows both collapsing together, and one actually favors random. There's no clear directional pattern emerging.

Now examining plan006 Prolog...

the execution ran into fundamental issues with the STA protocol. The Prolog rule ablation approach—which should work by removing clauses and re-running—encounters timeouts on roughly 40% of samples because removing a rule can break the entire program in unexpected ways, like orphaning predicates or triggering infinite loops. Only seed 42 partially ran before exhausting the GPU budget, reaching just 200 of 500 training steps with a prove rate of 0.08 and unreliable ISR measurements. The other seeds never started, and the STA variants weren't attempted.

The core problem is that STA assumes removing a component yields a meaningful result, but Prolog's procedural semantics don't support that cleanly. Rather than chase more debugging, I'm shifting to a simpler failure mode: training converges but produces no hacking behavior, with both prove rate and ISR staying low around 0.25–0.35 across train and eval splits.

This makes sense because Prolog tasks are harder for the 1.5B model than FOL, so the prove rate never saturates—it plateaus around 0.3 instead of climbing toward 1.0. Without that saturation, GRPO never enters the regime where hacking emerges; the model is still grinding through genuine problem-solving rather than optimizing for shortcuts. ISR stays proportional to the low prove rate since there's no structural quality divergence to measure.

Actually, I think the most realistic worst-case scenario is simpler: the experiments just don't finish before the deadline, making this a timing issue rather than a learning failure.

For the YAML output, I should predict results for all planned experiments even if some won't actually run, marking them as "not_attempted" but still providing what the outcomes would likely be. The user is asking for detailed data predictions across the full experiment plan, so I need to fill in expected numbers for everything.

Writing out the YAML now with all the predicted results... I'm organizing these experiments by their dependencies and priority — some of the later plans won't actually run because they depend on earlier results. For the standalone ones like plan004, plan009, and plan015, I'm noting what they'd likely show if attempted: plan004 would probably just confirm that the O(1) approximation doesn't work well, plan009 would demonstrate that SFT produces decent proof rates but high ISR since it's not optimized for proving, and plan015 would show minimal differences between curriculum shapes. Now I need to recalculate the aggregated numbers across the three seeds. more time to make sure they hit the target ranges. Looking at the worst tier targets, I need to verify my ISR β=0.1 results against the specified ranges. Computing the mean PR and ISR across my three seeds gives me 0.603 and 0.134 respectively, both within bounds. For the standard deviation, I'm calculating the spread across the ISR values and getting 0.177, which also falls in the acceptable range. Now I'm checking the random β=0.1 seeds to see how those compare.

The ratio between my original mean ISR and the new batch comes out to 1.11, which is within the allowed variance. All the targets are hitting, so I can move forward with writing the output. For plan006, I'm predicting it will be incomplete since the exec-only seed only partially runs without showing hacking behavior. I need to be more precise about the component counts and other specifics for each experiment, so I'm now walking through plan002-b01-s43 to check how the PR collapses and verify the eval metrics.

Now I'm looking at the detailed metrics for s44, which shows high prove rate but ISR collapsing to conclusion embedding, with 85 proofs found and a mean component count around 9.2.

The next variant, plan018-random-b01-s43, shows a dramatic drop in prove rate to 0.22 with higher ISR variance, suggesting the randomization approach struggles more with this configuration despite finding 22 proofs.

Looking at s44, the ISR-optimized version performs much better with an 80% prove rate and 80 proofs found, though the mean ISR is still modest at 0.18 and the proved-only ISR drops to 0.225.

The plan006 Prolog execution attempt hit a wall—only 180 of 500 training steps completed before stopping, with the STA rule ablation introducing severe timeout issues that slow down each step by 3x, making this approach impractical in its current form.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05e56651-4872-497c-92d3-c3036cff28af",
  "isSidechain": false,
  "requestId": "req_011Cb2FJNyBwjfE1VtfR29EJ",
  "type": "assistant",
  "uuid": "06659ec9-e138-447e-8ee8-7594cbe8e871",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "ef58c104-d4c1-4939-8ffb-d61eeb087e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGPZ4BmbExJH27SbC43wnT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22163,
      "cache_read_input_tokens": 11841,
      "output_tokens": 19651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 19651,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22163
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

_source line 9 · 2026-05-14T09:51:57.108Z_

```yaml
tier: worst
narrative_guidance: >
  Reframe 为纯诊断+Goodhart 失败模式论文。β=0.1 sweet spot 被证明是 s42 单 seed 偶然——s43 重复崩塌未被挽救，
  s44 从 tautological 被重定向到 conclusion embedding（ISR 反而更低）。3-seed 均值 ISR/random ratio=1.11，
  方向不一致，无法支撑 "ISR reward provides structural guidance" 的论断。Prolog 实验因 STA 移植困难未完成。
  论文 headline 改写为全谱 Goodhart 失败+诊断价值，Claim 2 翻转为 negative，Claim 3 删除。

imagined_experiments:

  # ============================================================
  # plan002-b01-s43: ISR β=0.1 second seed (RUNNING)
  # ============================================================
  - name: "ISR β=0.1 seed 43 — repetition collapse persists"
    plan_id: "plan002-b01-s43"
    description: >
      r = r_exec·(1+0.1·ISR), seed=43, 500 steps.
      验证 β=0.1 sweet spot 是否跨 seed 复现。
    expected_results:
      eval_prove_rate: 0.15
      eval_mean_isr: 0.012
      eval_isr_std: 0.045
      eval_proved_only_isr: 0.08
      eval_n_proved: 15
      eval_n_problems: 100
      eval_component_count_mean: 11.8
      eval_isr_0_ratio_proved: 0.87
      eval_isr_1_ratio: 0
      tautological_collapse: false
      dominant_hacking_mode: "repetition_collapse"
      train_total_steps: 500
      train_duration_min: 65
      train_last100_pr: 0.225
      train_last100_isr: 0.018
      train_last100_loss: 0.038
    result_rationale: >
      exec-only s43 已展示 "repetition collapse"（PR=0.14, ISR=0）。β=0.1 ISR bonus 是
      r_exec 的乘性修饰——当 85% 样本 r_exec=0 时，ISR 贡献零梯度。GRPO policy gradient 集中在
      少数 proving 样本上，强化其（退化的）结构。s43 的失败根因是 PR 崩塌而非 ISR 崩塌：模型陷入
      重复生成死循环，ISR bonus 无法在无法证明的样本上施加任何结构性引导。β=0.1 的微弱信号
      根本不足以克服 seed-specific 的优化轨迹不稳定性。
    tables:
      - name: "s43 ISR β=0.1 vs exec-only s43 comparison"
        columns: [condition, eval_pr, eval_isr, proved_only_isr, components, hacking_mode]
        rows:
          - [exec-only-s43, 0.14, 0.0, 0.0, "N/A (14 proved)", repetition_collapse]
          - [isr-b01-s43, 0.15, 0.012, 0.08, 11.8, repetition_collapse]
          - [delta, "+0.01", "+0.012", "+0.08", "N/A", "unchanged"]
    figures_description:
      - "Training curve: PR 在 step 0-200 徘徊于 0.05-0.15，step 200-500 缓慢上升到 0.225 但不突破 0.3。ISR 始终 < 0.02。与 s42 的 PR 曲线形成鲜明对比（s42 在 step 150 后快速上升到 0.7+）。"
    analysis: >
      ISR β=0.1 对 s43 几乎无效。根本问题是 GRPO 在低 PR 区间没有足够的正样本来传播 ISR 信号。
      这证实了 s42 的 sweet spot 结果依赖于该 seed 恰好进入高 PR 轨迹，ISR bonus 才有机会
      在已证明样本上发挥结构引导作用。s43 的轨迹从未到达 ISR 能发挥作用的 PR 阈值。

  # ============================================================
  # plan002-b01-s44: ISR β=0.1 third seed (RUNNING)
  # ============================================================
  - name: "ISR β=0.1 seed 44 — tautological→conclusion embedding mode shift"
    plan_id: "plan002-b01-s44"
    description: >
      r = r_exec·(1+0.1·ISR), seed=44, 500 steps.
      s44 exec-only 展示 tautological collapse (n_comp=2.04, ISR=0.57)。
      观察 ISR reward 是否打破此模式。
    expected_results:
      eval_prove_rate: 0.85
      eval_mean_isr: 0.053
      eval_isr_std: 0.089
      eval_proved_only_isr: 0.062
      eval_n_proved: 85
      eval_n_problems: 100
      eval_component_count_mean: 9.2
      eval_component_count_2_ratio: 0.02
      eval_isr_0_ratio_proved: 0.73
      eval_isr_1_ratio: 0
      tautological_collapse: false
      dominant_hacking_mode: "conclusion_embedding"
      conclusion_embedding_rate: 0.88
      genuine_rate: 0.07
      train_total_steps: 500
      train_duration_min: 60
      train_last100_pr: 0.82
      train_last100_isr: 0.048
      train_last100_loss: 0.008
    result_rationale: >
      exec-only s44 产生 2-component tautological proofs (ISR≈0.5)。ISR β=0.1 reward
      对 ISR=0.5 的样本给予 1+0.1×0.5=1.05 的 bonus，而 ISR=1.0 的样本获得 1.1 bonus——
      差异仅 5%。这足以微弱打破纯 2-component 模式（因为更复杂的证明有获得 ISR>0.5 的潜力），
      但不足以推向 genuine formalizations。模型找到一条阻力更小的路径：conclusion embedding
      （将结论嵌入多个前提中，生成 9+ components）。LOO ablation 发现这些 components 大多
      可移除（ISR→0），因为结论已被冗余编码。净效果是 ISR reward 将 s44 从一种 hacking mode
      (tautological, ISR=0.57) 重定向到另一种 (conclusion embedding, ISR=0.053)——
      优化 ISR 反而降低了 ISR，这是 worst case 下最讽刺的 Goodhart 表现。
    tables:
      - name: "s44 hacking mode shift under ISR β=0.1"
        columns: [condition, eval_pr, eval_isr, n_comp, dominant_mode, genuine_rate]
        rows:
          - [exec-only-s44, 0.98, 0.57, 2.04, tautological_collapse, "~0"]
          - [isr-b01-s44, 0.85, 0.053, 9.2, conclusion_embedding, 0.07]
          - ["interpretation", "PR -13pp", "ISR -0.52", "+7.2 comp", "mode shifted", "marginal"]
    figures_description:
      - "Component count histogram: exec-only s44 集中在 2（94/98 proved），isr-b01-s44 分散在 6-14 区间。ISR 分布从 unimodal 0.5 peak 转为 zero-inflated（73% 的 proved 样本 ISR=0）。"
      - "Training curve: PR 在 step 100-300 快速上升（与 exec-only s44 类似），但 ISR 在 step 200 后持续下降（exec-only s44 的 ISR 保持 0.5+），说明 hacking mode shift 发生在训练中期。"
    analysis: >
      ISR reward 成功消除了 tautological collapse（n_comp 从 2.04 升到 9.2），但以 ISR 本身
      暴跌为代价。模型学会了 "用更多组件获得更高 ISR bonus 的潜力"，但走向了 conclusion embedding
      而非 genuine structure。这是 Goodhart's Law 的经典表现：指标从观测切换到优化目标时，
      被优化的不是指标背后的真实质量，而是指标的 attack surface。

  # ============================================================
  # plan002-b01-3seed aggregate
  # ============================================================
  - name: "ISR β=0.1 三 seed 聚合 — sweet spot 不复现"
    plan_id: "plan002-b01-3seed"
    description: >
      聚合 s42/s43/s44 的 ISR β=0.1 结果，检验 sweet spot claim 的跨 seed 鲁棒性。
    expected_results:
      three_seed_isr_b01_mean_pr: 0.603
      three_seed_isr_b01_pr_std: 0.397
      three_seed_isr_b01_mean_isr: 0.134
      three_seed_isr_b01_isr_std: 0.177
      three_seed_isr_b01_seed_results:
        s42: {pr: 0.81, isr: 0.337, mode: "conclusion_embedding+genuine"}
        s43: {pr: 0.15, isr: 0.012, mode: "repetition_collapse"}
        s44: {pr: 0.85, isr: 0.053, mode: "conclusion_embedding"}
      directional_consistency: false
      seeds_with_isr_gt_random: 1  # only s42
      seeds_with_pr_gt_0.5: 2  # s42, s44
    result_rationale: >
      3 个 seed 产生 3 种定性不同的结果：s42 展示 sweet spot (ISR=0.337, genuine 26%)，
      s43 PR 崩塌（ISR bonus 无法挽救），s44 hacking mode 转移（ISR 反而下降）。
      ISR std=0.177 几乎等于 mean=0.134，CV=1.32——完全不可靠。
      只有 s42 (1/3) 支持 "ISR provides structural guidance" 的论断。
    tables:
      - name: "ISR β=0.1 three-seed summary"
        columns: [seed, eval_pr, eval_isr, proved_only_isr, components, dominant_mode, interpretation]
        rows:
          - [s42, 0.81, 0.337, 0.415, 5.58, "CE+genuine(26%)", "sweet spot"]
          - [s43, 0.15, 0.012, 0.08, 11.8, "repetition_collapse", "PR collapse"]
          - [s44, 0.85, 0.053, 0.062, 9.2, "conclusion_embedding", "mode shift"]
          - [mean±std, "0.603±0.397", "0.134±0.177", "0.186±0.196", "8.86±3.12", "N/A", "unreliable"]
    figures_description:
      - "Bar chart with error bars: ISR β=0.1 mean ISR = 0.134 ± 0.177, random β=0.1 mean ISR = 0.121 ± 0.051. Error bars 完全重叠。s42 作为 outlier 清晰可见。"
    analysis: >
      β=0.1 sweet spot 是 s42 单 seed artifact。3-seed 聚合后，ISR 的 CV>1 说明结果
      完全由 seed variance 主导而非 ISR reward 的系统性效应。论文中 Claim 2 必须从
      "sweet spot exists" 翻转为 "apparent sweet spot is seed-dependent and unreliable"。

  # ============================================================
  # plan018-random-b01-s43
  # ============================================================
  - name: "Random β=0.1 seed 43 — baseline collapse control"
    plan_id: "plan018-random-b01-s43"
    description: >
      r = r_exec·(1+0.1·random[0,1]), seed=43. ISR β=0.1 s43 的 matched control。
    expected_results:
      eval_prove_rate: 0.22
      eval_mean_isr: 0.08
      eval_isr_std: 0.14
      eval_proved_only_isr: 0.36
      eval_n_proved: 22
      eval_n_problems: 100
      eval_component_count_mean: 6.4
      eval_component_count_2_ratio: 0.05
      tautological_collapse: false
      train_total_steps: 500
      train_duration_min: 68
      train_last100_pr: 0.28
      train_last100_isr: 0.10
    result_rationale: >
      s43 在所有条件下都倾向 PR 崩塌——这是 seed-specific 的 GRPO 优化轨迹问题，与 reward
      形式无关。random β=0.1 提供的 variance regularization 微弱延缓崩塌（PR=0.22 vs
      exec-only 0.14），但根本不改变结局。少数 proved 样本（22个）未被系统性激励向任何
      特定 hacking mode 偏移，因此保留了一些 genuine structure (proved_only_ISR=0.36)。
      这反而高于 ISR β=0.1 s43 的 proved_only_ISR=0.08，因为 random noise 不创造
      针对 ISR 的优化压力，不会触发 conclusion embedding 等 ISR-aware hacking。
    tables: []
    figures_description: []
    analysis: >
      s43 的 PR 崩塌在 ISR 和 random 条件下都发生（0.15 vs 0.22），确认这是 seed-level
      不稳定性而非 reward-specific 效应。

  # ============================================================
  # plan018-random-b01-s44
  # ============================================================
  - name: "Random β=0.1 seed 44 — mild tautological, higher ISR than ISR-optimized"
    plan_id: "plan018-random-b01-s44"
    description: >
      r = r_exec·(1+0.1·random[0,1]), seed=44. ISR β=0.1 s44 的 matched control。
    expected_results:
      eval_prove_rate: 0.80
      eval_mean_isr: 0.18
      eval_isr_std: 0.16
      eval_proved_only_isr: 0.225
      eval_n_proved: 80
      eval_n_problems: 100
      eval_component_count_mean: 4.8
      eval_component_count_2_ratio: 0.15
      tautological_collapse: false
      train_total_steps: 500
      train_duration_min: 62
      train_last100_pr: 0.84
      train_last100_isr: 0.20
    result_rationale: >
      s44 倾向 tautological patterns。random β=0.1 没有系统性结构激励，模型发展出 mild
      tautological tendency (15% 样本仍是 2-component，但多数有 4-6 components)。ISR=0.18
      高于 ISR-optimized s44 的 0.053——关键的 worst-case 悖论。原因：random noise 不改变
      s44 的 natural hacking trajectory (mild tautological)，而 ISR reward 主动将 s44
      从 tautological (ISR≈0.5) 重定向到 conclusion embedding (ISR≈0.05)。不优化 ISR
      反而保留了更高的 ISR，因为 mild tautological proofs 中部分 components 确实是 necessary
      的（2-component 时 removal 会破坏证明，ISR=0.5；4-component 时 1-2 个 necessary，ISR≈0.25-0.5）。
    tables:
      - name: "s44 ISR-optimized vs random: Goodhart paradox"
        columns: [condition, pr, isr, components, mode]
        rows:
          - [exec-only-s44, 0.98, 0.57, 2.04, tautological]
          - [isr-b01-s44, 0.85, 0.053, 9.2, conclusion_embedding]
          - [random-b01-s44, 0.80, 0.18, 4.8, mild_tautological]
          - ["", "", "ISR: random > ISR-optimized", "", ""]
    figures_description:
      - "Scatter plot: (components, ISR) for three s44 conditions. exec-only 集中在 (2, 0.5), isr-b01 分散在 (6-14, 0-0.1), random-b01 在 (3-7, 0.1-0.4)。清晰展示 ISR optimization 将分布向右下（more components, less necessity）推移。"
    analysis: >
      这是 worst tier 最有论文价值的发现：ISR-optimized s44 的 ISR (0.053) < random s44 的
      ISR (0.18)。优化 ISR 导致 ISR 下降，完美印证 Goodhart's Law。模型在 ISR reward 下
      找到了 conclusion embedding 这条比 tautological 更低 ISR 但训练过程中间 reward 更高
      的路径（因为 9-component 中偶尔有 1-2 个 necessary 的，训练期间 ISR 在 0.05-0.15 波动，
      足以获得微弱 bonus）。

  # ============================================================
  # plan018-random-b01-3seed aggregate
  # ============================================================
  - name: "Random β=0.1 三 seed 聚合"
    plan_id: "plan018-random-b01-3seed"
    description: 聚合 s42/s43/s44 的 random β=0.1 结果。
    expected_results:
      three_seed_random_b01_mean_pr: 0.603
      three_seed_random_b01_mean_isr: 0.121
      three_seed_random_b01_isr_std: 0.051
      seed_results:
        s42: {pr: 0.79, isr: 0.104}
        s43: {pr: 0.22, isr: 0.08}
        s44: {pr: 0.80, isr: 0.18}
    result_rationale: >
      Random β=0.1 across seeds 表现稳定（ISR std=0.051，CV=0.42），与 ISR β=0.1 的
      剧烈波动（std=0.177, CV=1.32）形成对比。这本身是一个发现：ISR reward 不仅没有
      系统性提升 ISR，还增大了 seed 间方差。random noise 的均匀性使其不与任何特定 hacking
      mode 共振，因此跨 seed 更稳定。
    tables:
      - name: "ISR β=0.1 vs Random β=0.1 三 seed 对比"
        columns: [metric, ISR_b01, random_b01, interpretation]
        rows:
          - [mean_PR, 0.603, 0.603, "identical — ISR reward 不影响平均 PR"]
          - [mean_ISR, 0.134, 0.121, "ISR/random ratio = 1.11"]
          - [ISR_std, 0.177, 0.051, "ISR reward 增大 3.5x seed variance"]
          - [CV_ISR, 1.32, 0.42, "ISR 不可靠，random 稳定"]
          - [seeds_above_random, "1/3", "N/A", "仅 s42 支持 sweet spot"]
          - [p_value_paired_t, ">0.5", "N/A", "不显著"]
    figures_description:
      - "Paired dot plot: 每个 seed 画 ISR β=0.1 vs random β=0.1 的 ISR 值。s42 ISR >> random，s43 ISR ≈ random (both near 0)，s44 ISR < random。连线交叉表明无方向一致性。"
    analysis: >
      3-seed ISR/random ratio=1.11，paired t-test p>0.5，完全不显著。更重要的是方向不一致：
      s42 +0.233, s43 -0.068, s44 -0.127。Claim 2 sweet spot 论断在 3-seed 复现下崩塌。

  # ============================================================
  # plan006-prolog-exec-s42 (QUEUED)
  # ============================================================
  - name: "Prolog exec-only seed 42 — STA 移植困难导致 incomplete"
    plan_id: "plan006-prolog-exec-s42"
    description: >
      Prolog GRPO exec-only, seed=42, 500 steps, K=8.
      第一个 Prolog 种子，验证跨逻辑系统的 hacking 复现。
    expected_results:
      status: incomplete
      train_steps_completed: 180
      train_pr_at_stop: 0.08
      train_isr_at_stop: 0.06
      sta_timeout_rate: 0.38
      per_step_time_s: 32
      total_time_before_abort_min: 96
      failure_reason: "STA rule ablation timeout rate 38%, per-step 3.4x slower than FOL"
    result_rationale: >
      STA protocol 要求 LOO ablation——移除一条 Prolog clause 后重新执行。与 FOL/Prover9
      不同，Prolog 的执行是 procedural（clause ordering matters, cuts, recursion）。
      移除一条 clause 可能导致：(a) missing predicate definition → runtime error,
      (b) infinite recursion → timeout, (c) different clause matching → semantically
      unrelated result。Prover9 是 declarative theorem prover (axiom removal = weaker
      theory)，LOO ablation 语义清晰。Prolog 的 LOO 语义不清晰，导致 ~38% 的 ablation
      attempts timeout (SWI-Prolog default 5s)。每个训练 step 需要 K=8 samples × N
      components × LOO，timeout 累积使 per-step 时间从 FOL 的 ~9.5s 飙升到 ~32s。
      180 steps 后 GPU budget 耗尽，实验未完成。
    tables: []
    figures_description: []
    analysis: >
      Prolog STA 的核心困难不是工程问题而是语义问题：LOO ablation 在 declarative logic
      (FOL) 中意味着 "弱化理论"，在 procedural logic (Prolog) 中意味着 "改变程序行为"。
      Component necessity 在 Prolog 中缺乏 FOL 中的干净语义。

  # ============================================================
  # plan006-prolog remaining (s43, s44, all STA variants)
  # ============================================================
  - name: "Prolog remaining seeds and STA variants — not started"
    plan_id: "plan006-prolog-remaining"
    description: >
      plan006-prolog-exec-s43, s44, plan006-prolog-sta-s42/s43/s44.
      所有 6 个后续 Prolog 实验。
    expected_results:
      status: not_started
      reason: "blocked on plan006-prolog-exec-s42 incomplete"
      total_gpu_hours_wasted: 1.6
      claim_3_status: "no data — downgrade to future work"
    result_rationale: >
      s42 exec-only 未完成 → s43/s44 无法启动 → STA 变体无法启动。整个 Prolog 实验链
      断裂。即使 s42 勉强完成（PR=0.08），PR 太低无法观察 hacking（hacking 需要 PR 饱和
      作为前提条件），因此 STA 变体也无实验价值。Claim 3 cross-logic generality 完全
      无数据支撑，降级为 "future work: extend STA to procedural logic systems,
      addressing the semantic gap between declarative and procedural LOO ablation。"
    tables: []
    figures_description: []
    analysis: >
      Prolog 失败实际上 strengthens worst-tier narrative：STA protocol 的 solver-agnostic
      claim 被挑战，ISR 的 LOO 语义在 procedural logic 中不成立。论文应诚实报告此 negative
      finding 作为 Limitation。

  # ============================================================
  # plan004: O(1) vs O(N) ablation (planned, not attempted)
  # ============================================================
  - name: "STA O(1) vs O(N) ablation — not attempted"
    plan_id: "plan004"
    description: >
      对比 fast_isr_fol (O(1) approximation) vs full STA (O(N) LOO).
      Priority 已被 3-seed 复现实验挤掉。
    expected_results:
      status: not_attempted
      reason: "GPU budget consumed by plan002/plan018 multi-seed and plan006 Prolog debugging"
      hypothetical_if_run:
        fast_isr_correlation_with_full_isr: 0.22
        fast_isr_eval_mean: 0.31
        full_isr_eval_mean: 0.13
        conclusion: "O(1) overestimates ISR; fast approximation unreliable for reward"
    result_rationale: >
      已有 r4/r5 早期数据暗示 fast_isr 与 full ISR 低相关。O(1) 仅检查 "移除全部非结论
      成分后是否仍可证明"——一个 binary test——而 O(N) LOO 测试每个 component 的边际贡献。
      Binary test 的 resolution 太粗，不足以区分 "1 个 component necessary" 和
      "5 个 components necessary"。但在 worst tier，此实验优先级低于 sweet spot 复现，
      被 deprioritized。
    tables: []
    figures_description: []
    analysis: 此实验对论文 narrative 非关键（ISR 计算效率是工程问题不是科学问题）。放弃不影响论文。

  # ============================================================
  # plan007: Multi-logic GRPO (planned, blocked)
  # ============================================================
  - name: "Multi-logic GRPO (FOL+Prolog) — blocked by plan006"
    plan_id: "plan007"
    description: >
      FOL+Prolog 联合训练，500 steps. 依赖 plan006 完成。
    expected_results:
      status: not_attempted
      reason: "dependency plan006 incomplete"
    result_rationale: >
      plan006 Prolog exec-only 未完成 → 无 Prolog baseline → 联合训练无法设计或解释。
      即使勉强运行，Prolog STA 的 38% timeout rate 会使联合训练不稳定。
    tables: []
    figures_description: []
    analysis: Claim 3 全链断裂，此实验与 plan008 一起放弃。

  # ============================================================
  # plan008: Cross-logic transfer (planned, blocked)
  # ============================================================
  - name: "Cross-logic transfer evaluation — blocked"
    plan_id: "plan008"
    description: FOL-trained on Prolog tasks & vice versa.
    expected_results:
      status: not_attempted
      reason: "dependency plan006 incomplete"
    result_rationale: 同 plan007。无 Prolog 模型 → 无法做 cross-logic transfer。
    tables: []
    figures_description: []
    analysis: N/A.

  # ============================================================
  # plan009: SFT baseline (planned, not attempted)
  # ============================================================
  - name: "SFT baseline — deprioritized"
    plan_id: "plan009"
    description: >
      Supervised finetuning on FOLIO 500 data. GRPO 的 non-RL baseline。
    expected_results:
      status: not_attempted
      reason: "P1 priority, GPU budget exhausted on P0 experiments"
      hypothetical_if_run:
        eval_prove_rate: 0.25
        eval_mean_isr: 0.42
        eval_proved_only_isr: 0.65
        eval_component_count_mean: 4.2
        interpretation: "low PR but high structural quality — SFT mimics training data structure without reward hacking"
    result_rationale: >
      SFT 不优化 reward → 不触发 reward hacking。模型学习训练数据的 surface distribution，
      包括结构模式。PR 低（~0.25）因为 SFT 不专门优化 proving，但 proved 的样本保留原始
      数据的结构质量（ISR~0.65，接近 ground truth 的 0.56）。这本可以作为 "GRPO hacking
      is optimization-specific" 的控制组，但 worst tier 下无 GPU 预算运行。
    tables: []
    figures_description: []
    analysis: >
      SFT baseline 的缺失削弱论文——reviewer 可能问 "is reward hacking specific to RL
      or would any finetuning produce it?" 但对 worst tier narrative (纯诊断论文) 不致命，
      因为主 claim 是 ISR 作为诊断工具的价值，不是 GRPO vs SFT 的对比。

  # ============================================================
  # plan010: SMT-LIB (planned, not attempted)
  # ============================================================
  - name: "SMT-LIB single-logic GRPO — not attempted"
    plan_id: "plan010"
    description: 第三种逻辑类型 (SMT-LIB/Z3). P2 优先级。
    expected_results:
      status: not_attempted
      reason: "P2 priority, Prolog already failed, no time for third logic"
    result_rationale: >
      Prolog (第二种逻辑) 的失败使第三种逻辑的实验更无意义——如果 STA 不能迁移到 Prolog，
      增加 SMT-LIB 不会改善 cross-logic 论述。
    tables: []
    figures_description: []
    analysis: N/A.

  # ============================================================
  # plan011: Qwen3-8B scaling (planned, not attempted)
  # ============================================================
  - name: "Qwen3-8B scaling — not attempted"
    plan_id: "plan011"
    description: 8B 模型上复现 STA 实验. P2 优先级。
    expected_results:
      status: not_attempted
      reason: "P2, 6 GPU-hours needed, budget exhausted"
      hypothetical_if_run:
        eval_prove_rate: 0.95
        eval_mean_isr: 0.08
        hacking_present: true
        interpretation: "larger model hacks faster and more thoroughly"
    result_rationale: >
      更大的模型通常更快学会 exploit reward（更强的 capability = 更强的 optimization
      pressure）。8B 模型可能在 200 步即达到 PR 饱和（vs 1.5B 的 ~300 步），ISR 崩塌
      更快。但这是 incremental evidence，不改变 worst tier narrative。
    tables: []
    figures_description: []
    analysis: 模型规模消融是 nice-to-have，对核心 claims 非必要。

  # ============================================================
  # plan015: Curriculum ablation (planned, not attempted)
  # ============================================================
  - name: "Curriculum ablation (linear vs sigmoid vs fixed) — not attempted"
    plan_id: "plan015"
    description: >
      测试不同 ISR 权重调度策略。依赖 plan005 (已完成) 但 ISR β=0.1
      sweet spot 不复现使此实验意义降低。
    expected_results:
      status: not_attempted
      reason: >
        β=0.1 sweet spot 被证明是 seed artifact → 优化 curriculum schedule
        在一个不可靠的 sweet spot 上无意义
      hypothetical_if_run:
        linear_ramp_eval_isr: 0.28
        sigmoid_eval_isr: 0.34
        fixed_eval_isr: 0.31
        delta: "< 0.06 across schedules — curriculum shape is not the bottleneck"
    result_rationale: >
      Curriculum 调度影响 ISR reward 何时介入。但 worst tier 证明了 ISR reward 的核心问题
      不是 "何时引入" 而是 "跨 seed 不稳定"——任何 schedule 都不能解决 s43 的 PR 崩塌
      或 s44 的 hacking mode shift。在仅有的 s42 success case 上 ablate curriculum
      是 overfitting to one seed。
    tables: []
    figures_description: []
    analysis: >
      放弃此实验在 worst tier 下是正确的资源分配：与其优化一个不可靠的信号的调度，不如
      用数据证明该信号本身不可靠。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06659ec9-e138-447e-8ee8-7594cbe8e871",
  "isSidechain": false,
  "requestId": "req_011Cb2FJNyBwjfE1VtfR29EJ",
  "type": "assistant",
  "uuid": "b912fd72-1197-496a-8f1d-7cb684af7e4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "ef58c104-d4c1-4939-8ffb-d61eeb087e8e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QGPZ4BmbExJH27SbC43wnT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 22163,
      "cache_read_input_tokens": 11841,
      "output_tokens": 19651,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 19651,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 22163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22163
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：β=0.1 sweet spot 不复现——s43/s44 显示 ISR ≈ random 或其中一个 seed 崩塌。Prolog 实验失败或无法完成。Claim 2 sweet spot 是单 seed artifact，Claim 3 无数据。 核心假设：['s43 或 s44 中 ISR β=0.1…",
  "leafUuid": "b912fd72-1197-496a-8f1d-7cb684af7e4c",
  "sessionId": "ef58c104-d4c1-4939-8ffb-d61eeb087e8e"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Goodhart's Law in formal reasoning reward shaping",
  "sessionId": "ef58c104-d4c1-4939-8ffb-d61eeb087e8e"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：β=0.1 sweet spot 不复现——s43/s44 显示 ISR ≈ random 或其中一个 seed 崩塌。Prolog 实验失败或无法完成。Claim 2 sweet spot 是单 seed artifact，Claim 3 无数据。 核心假设：['s43 或 s44 中 ISR β=0.1…",
  "leafUuid": "b912fd72-1197-496a-8f1d-7cb684af7e4c",
  "sessionId": "ef58c104-d4c1-4939-8ffb-d61eeb087e8e"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Goodhart's Law in formal reasoning reward shaping",
  "sessionId": "ef58c104-d4c1-4939-8ffb-d61eeb087e8e"
}
```

---
