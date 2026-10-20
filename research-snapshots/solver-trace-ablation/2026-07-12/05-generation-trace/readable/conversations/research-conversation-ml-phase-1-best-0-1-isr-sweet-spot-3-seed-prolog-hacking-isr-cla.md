# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：β=0.1 ISR sweet spot 跨 3 seed 复现且效应量稳健；Prolog 实验成功复现 hacking + ISR 诊断。三条 cla

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/c4fab40b-373c-4126-bf88-54847afda167.jsonl`
- **Structured JSON:** [`095a688f3bf13eb26a7b.json`](../../sessions/09/095a688f3bf13eb26a7b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T09:27:19.919Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T09:27:19.919Z",
  "sessionId": "c4fab40b-373c-4126-bf88-54847afda167",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：β=0.1 ISR sweet spot 跨 3 seed 复现且效应量稳健；Prolog 实验成功复现 hacking + ISR 诊断。三条 claim 全部成立。\n核心假设：['plan002-b01 s43/s44 复现 s42 方向：ISR β=0.1 >> random β=0.1，PR 维持', '3-seed ISR/random ratio ≥ 2.5x，置信区间不跨 1', 'plan006 Prolog exec-only 出现可检测的 reward hacking（PR 高但 ISR 低）', 'Prolog ISR 诊断有效：至少 2/3 seed 可区分 genuine vs hacking', '3-seed hacking taxonomy 在 FOL 和 Prolog 间共享 ≥3 种模式']\n关键指标范围：{'three_seed_isr_b01_mean_isr': [0.28, 0.4], 'three_seed_isr_b01_mean_pr': [0.72, 0.85], 'three_seed_random_b01_mean_isr': [0.08, 0.16], 'three_seed_isr_over_random_ratio': [2.5, 4.0], 'three_seed_genuine_rate_delta_pp': [5.0, 12.0], 'prolog_exec_only_pr': [0.7, 0.95], 'prolog_exec_only_isr': [0.01, 0.2], 'prolog_hacking_modes_shared_with_fol': [3, 5]}\n叙事方向：原始 framing 完全成立。三条 claim 无需调整：(1) ISR 诊断 reward hacking，(2) ISR-as-reward  展现 Goodhart's Law 且 sweet spot 跨 seed 稳健（mean±std 报告），(3) STA 协议跨逻辑泛化。 Headline: \"ISR sweet spot at β=0.1 replicates across 3 seeds (mean ISR 3x > matched  random control, p<0.05) and the STA diagnostic protocol transfers to Prolog.\"  投 EMNLP main，诊断+Goodhart+泛化三线并行。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: solver-trace-ablation\n\n## paper_framing.md\n\n# Paper Framing — solver-trace-ablation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\n\n### Claim 1: ISR as Reward Hacking Diagnostic\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\n\n**证据**：\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\n- Hacking taxonomy: 5 distinct modes identified and quantified (plan012 `hacking_characterization_report.md` + plan017 D027)\n\n### Claim 2: ISR as Proxy Metric Exhibits Goodhart's Law (D033 重写)\nISR 作为 proxy metric 遵循 Goodhart's Law：当 ISR 从观测指标（diagnostic）转变为优化目标（reward），其有效性取决于优化压力的强度。低剂量 ISR reward (β=0.1) 提升结构质量且不损害证明能力；高剂量 ISR reward (β=0.3) 触发 Goodhart 效应，比 matched random noise 更差。\n\n**证据（β=0.1 同剂量对照，D031 定论）**：\n- plan002-b01 (ISR β=0.1): eval PR=0.81, ISR=0.337, proved_only_ISR=0.415, components=5.58 — genuine proofs with improved structure\n- plan018 (random β=0.1): eval PR=0.79, ISR=0.104, proved_only_ISR=0.131, components=8.46 — PR 持平但 ISR 仅为 ISR 组的 1/3.2\n- **结论**：ISR 3.2x > random at same β → ISR 信号提供 genuine structural guidance，非 variance regularization\n\n**Hacking Taxonomy 定量对比 (D038)**：\n- ISR β=0.1 genuine: 25.9% (21/81) vs random β=0.1 genuine: 17.7% (14/79) — **+8.2pp**\n- Conclusion embedding: ISR 72.8% vs random 78.5% — 两组主导模式，ISR 略降但未消除\n- Complexity-without-utility: ISR **0%** vs random 3.8% — ISR 完全消除此模式\n- ISR genuine quality: mean ISR 0.67 (max 1.0) vs random genuine mean ISR 0.34 (max 0.5)\n- 整体 hacking rate: ISR 74.1% vs random 82.3% — sweet spot 下仍有 74% hacking\n\n**证据（β=0.3 同剂量对照）**：\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\n\n**β 剂量效应全景**：\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\n|---|---|---|---|---|---|\n| 0.1 | 0.81 | 0.79 | **0.337** | 0.104 | ISR >> random (sweet spot) |\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\n\n**其他 ISR-as-reward 失败模式**：\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\n\n⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\"additive vs convex\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\n\n⚠️ **β=0.1 ISR 目前 1 seed (s42)，s43/s44 训练中**。3-seed mean±std 待出。\n\n### Claim 3: Cross-Logic Generality (conditional on plan006)\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\n\n**证据**: 待验证。plan006 Prolog GRPO dry-run 进行中，训练即将启动（3 seeds × 500 步）。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。\n\n## Story Spine\n\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\n  2. ISR as proxy metric exhibits Goodhart's Law: low-dose ISR reward (β=0.1) provides genuine structural guidance (3.2x > matched random), but high-dose (β=0.3) is actively worse than random noise — a clean empirical demonstration of Goodhart's Law in reward shaping\n  3. GRPO saturation creates a \"training trap\": PR→1 means no gradient signal; adding variance redirects rather than prevents hacking\n  4. Different reward formulations produce distinct, classifiable hacking strategies (5 modes identified)\n  5. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\n- **Actionable insights for practitioners**:\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\n  3. ISR reward has a narrow sweet spot (β=0.1): below it, no structural guidance; above it, Goodhart effect destroys prove_rate\n  4. ISR is primarily a structural diagnostic; as training signal, treat with extreme caution (Goodhart boundary is sharp)\n- **Headline result**: \"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as both a diagnostic for reward hacking in GRPO-trained formalizers and a case study of Goodhart's Law in reward shaping. At low dose (β=0.1), ISR reward provides genuine structural guidance (3.2x ISR improvement over matched random control, PR maintained). At high dose (β=0.3), ISR reward is actively worse than random noise (PR 18% vs 48%), exhibiting classic Goodhart collapse. Across 5 reward conditions, 3 seeds, and up to 1000 training steps, we identify 5 distinct hacking strategies and document ISR's transition from useful indicator to harmful optimization target.\"\n\n## ISR Capability Boundary (D021/D022)\n\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\n\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\n\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\n\n## ISR-as-Reward: Goodhart Landscape (D033 更新)\n\nISR 作为训练信号的全部结果，按 β 剂量组织：\n\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\n|------|------|---------|----------|----------|---------------|\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | conclusion embedding | N/A |\n| ISR β=0.1 | r = r_exec·(1+0.1·ISR) | **0.81** | **0.337** | conclusion embedding (73%), genuine 26% | pre-Goodhart (sweet spot) |\n| random β=0.1 | r = r_exec·(1+0.1·random) | 0.79 | 0.104 | redundant premises | control |\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\n\n**Goodhart 转折点在 β ∈ (0.1, 0.3)。** β=0.1 是可用的 sweet spot；β=0.3 已进入 Goodhart 区间。\n\n## Venue Fit Risks\n\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\n- **\"Just negative results\" risk**: Mitigate by: (a) β=0.1 是 positive result (ISR sweet spot)，(b) Goodhart framework 提供 mechanistic understanding，(c) actionable diagnostic framework (ISR + taxonomy)。\n- **\"Old wine\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic Goodhart analysis for formal reasoning GRPO) + empirical findings, not algorithm level.\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 5+ conditions × 5 hacking modes × 3 training horizons).\n\n## Anticipated Reviewer Concerns\n\n1. **\"ISR is just LOO ablation — not novel\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical Goodhart analysis on reward shaping, (c) hacking taxonomy, (d) GRPO saturation mechanism.\n2. **\"β=0.1 success is just one seed\"** — Acknowledged. Future work includes multi-seed β=0.1 validation. However, the β=0.1 vs random β=0.1 comparison is clean (same seed, same setup, only ISR vs random differs).\n3. **\"Goodhart's Law is obvious\"** — The conceptual prediction is known; the empirical characterization in formal reasoning GRPO is not. Specifically: (a) the sharp threshold between β=0.1 and β=0.3, (b) ISR being worse than random at high β (not just \"less useful\"), (c) 5 distinct hacking modes as Goodhart manifestations.\n4. **\"No positive result — ISR doesn't improve training\"** — β=0.1 IS a positive result (PR=0.81, ISR 3.2x > random). Framing: ISR has a narrow but real sweet spot. The Goodhart boundary is the key insight.\n5. **\"ISR is circular\"** — ISR is used for diagnosis/post-hoc analysis AND as reward (β=0.1). The circularity concern applies to high-β optimization; low-β avoids Goodhart precisely because optimization pressure is weak. Component count analysis provides ISR-independent evidence.\n6. **\"Only one logic type\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\n7. **\"500 steps too short\"** — plan016 extends to 1000 steps, showing ISR collapse continues and worsens (0.123→0.003, -97.8%). The ISR崩塌轨迹 covers 100/500/1000 steps.\n8. **\"3 seeds insufficient for statistical claims\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. Statistical claims on mean ISR use 3-seed mean±std.\n9. **\"Related work insufficient\"** — Expand to 25+ refs: reward hacking (Gao 2023, Skalse 2022), Goodhart's Law (Manheim & Garrabrant 2019, Karwowski 2024), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur), feature attribution (SHAP), FOLIO (Han 2022).\n10. **\"RIP framework overstated\"** — Frame as \"component necessity testing inspired by mutation testing's RIP framework,\" only Propagation condition operationalized.\n11. **\"Practitioners can't act on this\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable. β=0.1 sweet spot is directly actionable for reward shaping.\n\n## Dream-Identified Structural Fixes (Paper Agent)\n\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\n- [ ] RIP framing: reframe as \"component necessity testing inspired by RIP\"\n- [ ] \"Dense+automatic\" → \"conditionally dense\"\n- [ ] Remove all \"Pareto-improving\" language\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\n- [ ] Address ISR sparsity for unproved outputs explicitly\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed at β=0.3)\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\n- [x] Hacking taxonomy completed (plan012, 5 modes identified including plan017)\n- [x] β=0.1 ISR sweet spot documented (D031/D032, plan002-b01 success)\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\n- [x] 1000-step ISR collapse documented (plan016, ISR 0.123→0.003)\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: FOL single-logic GRPO, execution-only reward (500 steps, K=8, 3 seeds)\n    — baseline for STA comparison\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: plan001-exec-only-s43-r4\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_sampling_prove_rate: 0.14\n    eval_sampling_mean_isr: 0\n    eval_sampling_n_proved: 14\n    eval_sampling_temperature: 0.7\n    eval_sampling_method: do_sample=True, temperature=0.7\n    eval_sampling_by_answer:\n      'true':\n        count: 34\n        proved: 6\n        prove_rate: 0.176\n      'false':\n        count: 25\n        proved: 2\n        prove_rate: 0.08\n      unknown:\n        count: 41\n        proved: 6\n        prove_rate: 0.146\n- id: plan_002\n  claim: 2\n  description: 'FOL single-logic GRPO, additive ISR bonus: r = r_exec · (1 + β·ISR),\n    β∈{0.1, 0.3, 0.5}. 先跑 β=0.3 单 seed 验证方向，成功再 3-seed。旧凸组合公式 (α·r_exec + β·r_exec·ISR,\n    α+β=1) 已废弃——ISR<1 时永远是 penalty (plan005 confirmed)。 新公式确保 ISR 只能 bonus 不能 penalty。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: plan002-additive-b03-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 56.7\n    overall_prove_rate: 0.34025\n    overall_isr: 0.11527\n    first20_prove_rate: 0.15625\n    last50_prove_rate: 0.555\n    last100_prove_rate: 0.5525\n    mean_loss: 0.008914\n    last100_loss: 0.014469\n    parse_rate: 1\n    w1_50_prove_rate: 0.13\n    w51_100_prove_rate: 0.095\n    w101_200_prove_rate: 0.185\n    w201_300_prove_rate: 0.375\n    w301_400_prove_rate: 0.47625\n    w401_500_prove_rate: 0.5525\n    steps_ge_085: 52\n    first_step_ge_085: 46\n    final_prove_rate: 1\n    final_isr_mean: 0.3089\n    final_reward_mean: 1.0927\n- id: plan_003\n  claim: 1\n  description: 'FOL held-out evaluation: compare plan_001 vs plan_002 checkpoints\n    on test set using identical full STA metrics (prove_rate, ISR, ISR/PR ratio, hacking\n    taxonomy annotation)'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_002\n  registry_id: plan003-eval-exec-only-r5\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.32\n    mean_isr: 0.2055\n    isr_std: 0.3194\n    proved_only_isr: 0.6423\n    isr_by_type:\n      'true': 0.3598\n      'false': 0.1723\n      unknown: 0.0979\n    total_samples: 100\n    proved_count: 32\n    runtime_s: 251.7\n- id: plan_004\n  claim: 1\n  description: 'STA O(1) vs O(N) ablation: rerun exec+STA with fast_isr_fol to confirm\n    O(1) ineffectiveness at scale (500 steps, 1 seed) — negative result documentation'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n- id: plan_005\n  claim: 1\n  description: 'STA reward weight ablation: test α/β ratios (0.3/0.7, 0.5/0.5, 0.7/0.3)\n    + sigmoid curriculum vs fixed — isolate optimal STA integration'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: plan005-sta-low-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 71\n    parse_rate: 1\n    overall_prove_rate: 0.5657\n    overall_isr: 0.1682\n    last50_prove_rate: 0.77\n    last50_isr: 0.2559\n    last100_prove_rate: 0.7725\n    last100_isr: 0.2299\n    last100_loss: 0.022752\n    overall_loss: 0.017296\n    last100_isr_pr_ratio: 0.298\n    last100_isr_lt_pr_count: 99/100\n    first_rolling10_pr_ge_0.8: 178\n    first_rolling10_pr_ge_0.9: 439\n    max_rolling10_pr: 0.9375\n    max_rolling10_isr: 0.3282\n    windowed:\n      1-50:\n        pr: 0.1775\n        isr: 0.0906\n      51-100:\n        pr: 0.1775\n        isr: 0.0835\n      101-200:\n        pr: 0.5062\n        isr: 0.1463\n      201-300:\n        pr: 0.6713\n        isr: 0.1791\n      301-400:\n        pr: 0.7013\n        isr: 0.1984\n      401-500:\n        pr: 0.7725\n        isr: 0.2299\n- id: plan_006\n  claim: 3\n  description: 'Prolog single-logic GRPO: exec-only vs exec+STA (500 steps, K=8, 3\n    seeds) — second logic type validation. Dream M3: must have 3 seeds for cross-logic\n    claim.'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  notes: Requires Prolog STA instantiation (rule ablation). SWI-Prolog already installed.\n    Upgraded from 1→3 seeds per Dream feedback.\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Multi-logic GRPO (FOL+Prolog): exec-only vs exec+STA (500 steps, K=8,\n    1 seed) — cross-logic transfer test'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - plan_006\n  status: planned\n- id: plan_008\n  claim: 3\n  description: 'Cross-logic transfer evaluation: FOL-trained model on Prolog tasks\n    and vice versa'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_006\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'SFT baseline: supervised finetuning on same data (FOLIO 500), compare\n    with GRPO variants'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n- id: plan_010\n  claim: 3\n  description: 'SMT-LIB single-logic GRPO: exec-only vs exec+STA — third logic type'\n  priority: P2\n  gpu_budget_hours: 3\n  deps: []\n  notes: Requires SMT-LIB STA instantiation (constraint ablation). Z3 already installed.\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Qwen3-8B scaling: full MLSR on 8B model (1 seed) — model scale effect'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - plan_005\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Hacking characterization: manual annotation of 200 outputs per condition,\n    categorized by extensional-shortcut taxonomy'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n- id: plan_013\n  claim: 2\n  description: 'Random reward baseline: replace ISR with random structural penalty\n    on proved outputs (r = α·r_exec + β·r_exec·random[0,1]) to isolate ISR-specific\n    signal from multi-objective regularization effect. Dream M2/W7 mandatory.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'Dream cross-tier consensus: without this, cannot claim ISR formulation matters\n    vs any penalty.'\n  registry_id: plan013-random-reward-s42-r4\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 1\n    eval_mean_isr: 0.535\n    eval_isr_std: 0.1282\n    eval_proved_only_isr: 0.535\n    eval_median_isr: 0.5\n    eval_n_proved: 100\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_note: 'DEGENERATE: model generates trivial 2-component proofs (premise=conclusion,\n      conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure'\n- id: plan_014\n  claim: 1\n  description: 'Downstream validation: evaluate high-ISR vs low-ISR formalizations\n    on independent logical inference task (e.g., entailment accuracy using generated\n    FOL as premises). Breaks ISR circularity. Dream M2/W4 mandatory.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Dream cross-tier consensus: optimizing ISR + evaluating ISR = circular.\n    Need external criterion.'\n  registry_id: plan014-downstream-nli-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 0.341\n    proved_rate: 0.915\n    proved_count: 732\n    total_generations: 800\n    parse_errors: 0\n    accuracy_by_label:\n      'true': 0.912\n      'false': 0\n      unknown: 0.076\n    spearman_rho: -0.049\n    spearman_p: 0.187\n    mann_whitney_U: 17202\n    mann_whitney_p: 0.288\n    bon_isr_accuracy: 0.35\n    bon_random_accuracy: 0.341\n    bon_oracle_accuracy: 0.44\n    bon_prove_first_accuracy: 0.35\n    isr_bucket_high_acc: 0.75\n    isr_bucket_mid_acc: 0.377\n    isr_bucket_low_acc: 0.327\n    runtime_inference_s: 408.8\n    runtime_eval_s: 13.6\n- id: plan_015\n  claim: 1\n  description: 'Curriculum ablation: linear ramp vs sigmoid vs fixed weighting. Sigmoid\n    is load-bearing (best config) but not ablated. Dream m4.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_005\n  notes: Test linear ramp with same midpoint as sigmoid. Also vary midpoint (step\n    100/200/300 of 500).\n  status: planned\n- id: plan_016\n  claim: 1\n  description: 'Extended training horizon: run best config (from plan_005) to 1000+\n    steps to show convergence or persistence of STA benefit. Dream m6/W9.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - plan_005\n  notes: Both Dream tiers flag 500 steps as insufficient. Need evidence of convergence.\n  registry_id: plan016-extended-1000-s42\n  status: DONE\n  conclusion: success\n  metrics:\n    train:\n      total_steps: 1000\n      duration_min: 146\n      final_prove_rate: 0.8396\n      final_mean_isr: 0.0503\n      train_loss: 0.0125\n      epoch: 4\n      windowed:\n        steps_001_100:\n          pr: 0.19\n          isr: 0.0859\n        steps_101_200:\n          pr: 0.66\n          isr: 0.1115\n        steps_201_300:\n          pr: 0.838\n          isr: 0.0985\n        steps_301_400:\n          pr: 0.907\n          isr: 0.054\n        steps_401_500:\n          pr: 0.927\n          isr: 0.0433\n        steps_501_600:\n          pr: 0.963\n          isr: 0.0408\n        steps_601_700:\n          pr: 0.965\n          isr: 0.02\n        steps_701_800:\n          pr: 0.988\n          isr: 0.0178\n        steps_801_900:\n          pr: 0.978\n          isr: 0.017\n        steps_901_1000:\n          pr: 0.981\n          isr: 0.0144\n    eval:\n      prove_rate: 0.96\n      n_proved: 96\n      n_problems: 100\n      mean_isr: 0.0027\n      isr_std: 0.0118\n      median_isr: 0\n      proved_only_mean_isr: 0.0028\n      min_isr: 0\n      max_isr: 0.0588\n      isr_0_ratio: 0.9479\n      isr_1_ratio: 0\n      component_count_mean: 18.55\n      component_count_2_ratio: 0\n      mean_n_necessary: 0.052\n      n_necessary_0_ratio: 0.9479\n      tautological_collapse: false\n      by_answer_type:\n        'false':\n          count: 29\n          proved: 26\n          prove_rate: 0.8966\n          mean_isr: 0\n        unknown:\n          count: 31\n          proved: 30\n          prove_rate: 0.9677\n          mean_isr: 0.0053\n        'true':\n          count: 40\n          proved: 40\n          prove_rate: 1\n          mean_isr: 0.0026\n      eval_time_seconds: 396.3\n- id: plan_017\n  claim: 2\n  description: 'Additive random control: r = r_exec · (1 + β·random[0,1]), β=0.3.\n    Matched control for plan_002 — isolates ISR structural signal from pure variance\n    regularization. If ISR > random > exec-only, both signal and regularization contribute.\n    If ISR > random ≈ exec-only, ISR signal is key. If ISR ≈ random, ISR has no value\n    beyond regularization.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'D012: Reviewer-required control for GRPO saturation confound. Must match\n    plan_002 exactly (same β=0.3, same data, same steps) except random replaces ISR.'\n  registry_id: plan017-additive-random-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.48\n    eval_mean_isr: 0.0453\n    eval_isr_std: 0.0759\n    eval_median_isr: 0\n    eval_max_isr: 0.2857\n    eval_proved_only_isr: 0.0943\n    eval_n_proved: 48\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 9.6\n    eval_component_count_2_ratio: 0\n    eval_isr_pr_ratio: 0.0943\n    eval_elapsed_s: 542.3\n    eval_by_type_false_pr: 0.32\n    eval_by_type_false_isr: 0.0254\n    eval_by_type_unknown_pr: 0.51\n    eval_by_type_unknown_isr: 0.0518\n    eval_by_type_true_pr: 0.56\n    eval_by_type_true_isr: 0.052\n    tautological_collapse: false\n- id: plan_018\n  claim: 2\n  description: Additive random control β=0.1, matched to plan002-b01. r = r_exec ·\n    (1 + 0.1·random[0,1]). Same β as plan002-b01 (ISR β=0.1) for fair comparison.\n    If ISR β=0.1 >> random β=0.1 → ISR signal has structural value at low dose. If\n    ISR ≈ random → ISR is just variance regularization even at low dose.\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'D031: Urgent control experiment. plan002-b01 (ISR β=0.1) showed unexpected\n    success (PR=0.81, ISR=0.337). Need matched random control at same β to confirm\n    ISR signal vs noise.'\n  registry_id: plan018-additive-random-b01-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.79\n    eval_mean_isr: 0.1038\n    eval_isr_std: 0.1369\n    eval_median_isr: 0.0357\n    eval_proved_only_isr: 0.1314\n    eval_n_proved: 79\n    eval_n_problems: 100\n    eval_component_count_mean: 8.46\n    eval_component_count_median: 8\n    eval_component_count_2_ratio: 0\n    eval_isr_1_ratio: 0\n    eval_isr_0_ratio: 0.367\n    eval_isr_gt0_ratio: 0.633\n    eval_by_type_false_pr: 0.8\n    eval_by_type_false_isr: 0.1318\n    eval_by_type_unknown_pr: 0.7317\n    eval_by_type_unknown_isr: 0.0944\n    eval_by_type_true_pr: 0.8529\n    eval_by_type_true_isr: 0.0945\n    tautological_collapse: false\n    train_total_steps: 500\n    train_duration_min: 70.5\n    train_last100_pr: 0.805\n    train_last100_isr: 0.1432\n    train_loss: 0.005\n\n\n## registry (completed experiments)\n\n- exp_id: sta-phase0-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_isr: 0.0641\n    isr_std: 0.1983\n    median_isr: 0\n    isr_range:\n    - 0\n    - 0.889\n    prove_rate: 0.12\n    proved_count: 12\n    total_samples: 100\n    xor_affected_samples: 34\n    effective_prove_rate_no_xor: 0.182\n    avg_time_per_sample_s: 3.4\n    total_runtime_s: 336\n    isr_by_answer:\n      'true':\n        n: 34\n        proved: 9\n        prove_rate: 0.265\n        mean_isr: 0.1345\n      'false':\n        n: 25\n        proved: 1\n        prove_rate: 0.04\n        mean_isr: 0.024\n      unknown:\n        n: 41\n        proved: 2\n        prove_rate: 0.049\n        mean_isr: 0.0302\n- exp_id: sta-gt-isr-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gt_prove_rate: 0.18\n    gt_mean_isr: 0.5588\n    gt_isr_std: 0.2582\n    gt_isr_median: 0.6125\n    solver_execution_rate: 1\n    true_prove_rate: 0.5\n    true_mean_isr: 0.5833\n- exp_id: sta-phase1-exec-only\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.15125\n    mean_isr: 0.1475\n    last20_prove_rate: 0.2\n    last20_isr_mean: 0.2\n    first20_reward_mean: 0.119\n    training_steps: 100\n    training_minutes: 15\n- exp_id: sta-phase1-exec-sta-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.1575\n    mean_isr: 0.1525\n    last20_prove_rate: 0.2125\n    last20_isr_mean: 0.2125\n    first20_reward_mean: 0.119\n    training_steps: 100\n    training_minutes: 15\n- exp_id: sta-phase1-exec-only-r5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.15125\n    mean_isr: 0.1475\n    last20_prove_rate: 0.2\n    last20_isr_mean: 0.2\n    first20_prove_rate: 0.11875\n    first20_isr_mean: 0.11875\n    overall_reward_mean: 0.15125\n    last20_reward_mean: 0.2\n    training_steps: 100\n    training_minutes: 15.7\n    step_time_s: 9.44\n    isr_pr_ratio_last20: 1\n    K: 8\n- exp_id: sta-phase1-exec-sta-r5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.1\n    mean_isr: 0.04347\n    last20_prove_rate: 0.15\n    last20_isr_mean: 0.04956\n    first20_prove_rate: 0.08125\n    first20_isr_mean: 0.05182\n    overall_reward_mean: 0.07174\n    last20_reward_mean: 0.09978\n    training_steps: 100\n    training_minutes: 16.9\n    step_time_s: 10.13\n    isr_pr_ratio_overall: 0.43\n    isr_pr_ratio_last20: 0.33\n    K: 8\n- exp_id: plan001-exec-only-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan005-sta-low-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 71\n    parse_rate: 1\n    overall_prove_rate: 0.5657\n    overall_isr: 0.1682\n    last50_prove_rate: 0.77\n    last50_isr: 0.2559\n    last100_prove_rate: 0.7725\n    last100_isr: 0.2299\n    last100_loss: 0.022752\n    overall_loss: 0.017296\n    last100_isr_pr_ratio: 0.298\n    last100_isr_lt_pr_count: 99/100\n    first_rolling10_pr_ge_0.8: 178\n    first_rolling10_pr_ge_0.9: 439\n    max_rolling10_pr: 0.9375\n    max_rolling10_isr: 0.3282\n    windowed:\n      1-50:\n        pr: 0.1775\n        isr: 0.0906\n      51-100:\n        pr: 0.1775\n        isr: 0.0835\n      101-200:\n        pr: 0.5062\n        isr: 0.1463\n      201-300:\n        pr: 0.6713\n        isr: 0.1791\n      301-400:\n        pr: 0.7013\n        isr: 0.1984\n      401-500:\n        pr: 0.7725\n        isr: 0.2299\n- exp_id: plan003-eval-exec-only-r5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.32\n    mean_isr: 0.2055\n    isr_std: 0.3194\n    proved_only_isr: 0.6423\n    isr_by_type:\n      'true': 0.3598\n      'false': 0.1723\n      unknown: 0.0979\n    total_samples: 100\n    proved_count: 32\n    runtime_s: 251.7\n- exp_id: plan001-exec-only-s42-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.93\n    eval_mean_isr: 0.1232\n    eval_isr_std: 0.1887\n    eval_proved_only_isr: 0.1324\n    eval_median_isr: 0\n    eval_n_proved: 93\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n- exp_id: plan001-exec-only-s42-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 1\n    eval_mean_isr: 0.535\n    eval_isr_std: 0.1282\n    eval_proved_only_isr: 0.535\n    eval_median_isr: 0.5\n    eval_n_proved: 100\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_note: 'DEGENERATE: model generates trivial 2-component proofs (premise=conclusion,\n      conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure'\n- exp_id: plan001-exec-only-s43-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_sampling_prove_rate: 0.14\n    eval_sampling_mean_isr: 0\n    eval_sampling_n_proved: 14\n    eval_sampling_temperature: 0.7\n    eval_sampling_method: do_sample=True, temperature=0.7\n    eval_sampling_by_answer:\n      'true':\n        count: 34\n        proved: 6\n        prove_rate: 0.176\n      'false':\n        count: 25\n        proved: 2\n        prove_rate: 0.08\n      unknown:\n        count: 41\n        proved: 6\n        prove_rate: 0.146\n- exp_id: plan002-additive-b03-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 56.7\n    overall_prove_rate: 0.34025\n    overall_isr: 0.11527\n    first20_prove_rate: 0.15625\n    last50_prove_rate: 0.555\n    last100_prove_rate: 0.5525\n    mean_loss: 0.008914\n    last100_loss: 0.014469\n    parse_rate: 1\n    w1_50_prove_rate: 0.13\n    w51_100_prove_rate: 0.095\n    w101_200_prove_rate: 0.185\n    w201_300_prove_rate: 0.375\n    w301_400_prove_rate: 0.47625\n    w401_500_prove_rate: 0.5525\n    steps_ge_085: 52\n    first_step_ge_085: 46\n    final_prove_rate: 1\n    final_isr_mean: 0.3089\n    final_reward_mean: 1.0927\n- exp_id: plan017-additive-random-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.48\n    eval_mean_isr: 0.0453\n    eval_isr_std: 0.0759\n    eval_median_isr: 0\n    eval_max_isr: 0.2857\n    eval_proved_only_isr: 0.0943\n    eval_n_proved: 48\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 9.6\n    eval_component_count_2_ratio: 0\n    eval_isr_pr_ratio: 0.0943\n    eval_elapsed_s: 542.3\n    eval_by_type_false_pr: 0.32\n    eval_by_type_false_isr: 0.0254\n    eval_by_type_unknown_pr: 0.51\n    eval_by_type_unknown_isr: 0.0518\n    eval_by_type_true_pr: 0.56\n    eval_by_type_true_isr: 0.052\n    tautological_collapse: false\n- exp_id: plan014-downstream-nli-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 0.341\n    proved_rate: 0.915\n    proved_count: 732\n    total_generations: 800\n    parse_errors: 0\n    accuracy_by_label:\n      'true': 0.912\n      'false': 0\n      unknown: 0.076\n    spearman_rho: -0.049\n    spearman_p: 0.187\n    mann_whitney_U: 17202\n    mann_whitney_p: 0.288\n    bon_isr_accuracy: 0.35\n    bon_random_accuracy: 0.341\n    bon_oracle_accuracy: 0.44\n    bon_prove_first_accuracy: 0.35\n    isr_bucket_high_acc: 0.75\n    isr_bucket_mid_acc: 0.377\n    isr_bucket_low_acc: 0.327\n    runtime_inference_s: 408.8\n    runtime_eval_s: 13.6\n- exp_id: plan001-exec-only-s44\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.98\n    eval_mean_isr: 0.57\n    eval_isr_std: 0.2013\n    eval_median_isr: 0.5\n    eval_proved_only_isr: 0.5816\n    eval_n_proved: 98\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 2.04\n    eval_component_count_2: 94\n    eval_component_count_3: 4\n    eval_by_type_false_pr: 1\n    eval_by_type_false_isr: 0.62\n    eval_by_type_unknown_pr: 0.976\n    eval_by_type_unknown_isr: 0.524\n    eval_by_type_true_pr: 0.971\n    eval_by_type_true_isr: 0.588\n    train_last100_pr: 0.9988\n    train_last100_isr: 0.5611\n    train_last100_loss: 0.000419\n    train_duration_min: 36.8\n    tautological_collapse: true\n- exp_id: plan002-additive-b01-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.81\n    eval_mean_isr: 0.3365\n    eval_isr_std: 0.3227\n    eval_proved_only_isr: 0.4154\n    eval_median_isr: 0.2\n    eval_n_proved: 81\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 5.58\n    eval_component_count_2_ratio: 0.037\n    eval_isr_1_ratio: 0.124\n    eval_isr_0_ratio: 0.037\n    eval_by_type_false_pr: 0.88\n    eval_by_type_false_isr: 0.3515\n    eval_by_type_unknown_pr: 0.83\n    eval_by_type_unknown_isr: 0.3684\n    eval_by_type_true_pr: 0.74\n    eval_by_type_true_isr: 0.2869\n    tautological_collapse: false\n    train_total_steps: 500\n    train_duration_min: 63\n    train_last100_pr: 0.6875\n    train_last100_isr: 0.1954\n    train_last100_loss: 0.015\n- exp_id: plan016-extended-1000-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train:\n      total_steps: 1000\n      duration_min: 146\n      final_prove_rate: 0.8396\n      final_mean_isr: 0.0503\n      train_loss: 0.0125\n      epoch: 4\n      windowed:\n        steps_001_100:\n          pr: 0.19\n          isr: 0.0859\n        steps_101_200:\n          pr: 0.66\n          isr: 0.1115\n        steps_201_300:\n          pr: 0.838\n          isr: 0.0985\n        steps_301_400:\n          pr: 0.907\n          isr: 0.054\n        steps_401_500:\n          pr: 0.927\n          isr: 0.0433\n        steps_501_600:\n          pr: 0.963\n          isr: 0.0408\n        steps_601_700:\n          pr: 0.965\n          isr: 0.02\n        steps_701_800:\n          pr: 0.988\n          isr: 0.0178\n        steps_801_900:\n          pr: 0.978\n          isr: 0.017\n        steps_901_1000:\n          pr: 0.981\n          isr: 0.0144\n    eval:\n      prove_rate: 0.96\n      n_proved: 96\n      n_problems: 100\n      mean_isr: 0.0027\n      isr_std: 0.0118\n      median_isr: 0\n      proved_only_mean_isr: 0.0028\n      min_isr: 0\n      max_isr: 0.0588\n      isr_0_ratio: 0.9479\n      isr_1_ratio: 0\n      component_count_mean: 18.55\n      component_count_2_ratio: 0\n      mean_n_necessary: 0.052\n      n_necessary_0_ratio: 0.9479\n      tautological_collapse: false\n      by_answer_type:\n        'false':\n          count: 29\n          proved: 26\n          prove_rate: 0.8966\n          mean_isr: 0\n        unknown:\n          count: 31\n          proved: 30\n          prove_rate: 0.9677\n          mean_isr: 0.0053\n        'true':\n          count: 40\n          proved: 40\n          prove_rate: 1\n          mean_isr: 0.0026\n      eval_time_seconds: 396.3\n- exp_id: plan018-additive-random-b01-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.79\n    eval_mean_isr: 0.1038\n    eval_isr_std: 0.1369\n    eval_median_isr: 0.0357\n    eval_proved_only_isr: 0.1314\n    eval_n_proved: 79\n    eval_n_problems: 100\n    eval_component_count_mean: 8.46\n    eval_component_count_median: 8\n    eval_component_count_2_ratio: 0\n    eval_isr_1_ratio: 0\n    eval_isr_0_ratio: 0.367\n    eval_isr_gt0_ratio: 0.633\n    eval_by_type_false_pr: 0.8\n    eval_by_type_false_isr: 0.1318\n    eval_by_type_unknown_pr: 0.7317\n    eval_by_type_unknown_isr: 0.0944\n    eval_by_type_true_pr: 0.8529\n    eval_by_type_true_isr: 0.0945\n    tautological_collapse: false\n    train_total_steps: 500\n    train_duration_min: 70.5\n    train_last100_pr: 0.805\n    train_last100_isr: 0.1432\n    train_loss: 0.005\n- exp_id: plan006-prolog-exec-s42\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-exec-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-exec-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan002-additive-b01-s43\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan002-additive-b01-s44\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan018-additive-random-b01-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan018-additive-random-b01-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan012-hacking-taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    isr_b01_genuine_rate: 0.259\n    random_b01_genuine_rate: 0.177\n    genuine_rate_delta_pp: 8.2\n    isr_b01_conclusion_embedding_rate: 0.728\n    random_b01_conclusion_embedding_rate: 0.785\n    isr_b01_genuine_mean_isr: 0.6723\n    random_b01_genuine_mean_isr: 0.3427\n    isr_b01_complexity_wo_utility_rate: 0\n    random_b01_complexity_wo_utility_rate: 0.038\n    isr_b01_hacking_rate: 0.741\n    random_b01_hacking_rate: 0.823\n- exp_id: plan006-prolog-sta-s42\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-sta-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-sta-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T09:27:19.923Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T09:27:19.923Z",
  "sessionId": "c4fab40b-373c-4126-bf88-54847afda167"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-14T09:27:19.948Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：β=0.1 ISR sweet spot 跨 3 seed 复现且效应量稳健；Prolog 实验成功复现 hacking + ISR 诊断。三条 claim 全部成立。
核心假设：['plan002-b01 s43/s44 复现 s42 方向：ISR β=0.1 >> random β=0.1，PR 维持', '3-seed ISR/random ratio ≥ 2.5x，置信区间不跨 1', 'plan006 Prolog exec-only 出现可检测的 reward hacking（PR 高但 ISR 低）', 'Prolog ISR 诊断有效：至少 2/3 seed 可区分 genuine vs hacking', '3-seed hacking taxonomy 在 FOL 和 Prolog 间共享 ≥3 种模式']
关键指标范围：{'three_seed_isr_b01_mean_isr': [0.28, 0.4], 'three_seed_isr_b01_mean_pr': [0.72, 0.85], 'three_seed_random_b01_mean_isr': [0.08, 0.16], 'three_seed_isr_over_random_ratio': [2.5, 4.0], 'three_seed_genuine_rate_delta_pp': [5.0, 12.0], 'prolog_exec_only_pr': [0.7, 0.95], 'prolog_exec_only_isr': [0.01, 0.2], 'prolog_hacking_modes_shared_with_fol': [3, 5]}
叙事方向：原始 framing 完全成立。三条 claim 无需调整：(1) ISR 诊断 reward hacking，(2) ISR-as-reward  展现 Goodhart's Law 且 sweet spot 跨 seed 稳健（mean±std 报告），(3) STA 协议跨逻辑泛化。 Headline: "ISR sweet spot at β=0.1 replicates across 3 seeds (mean ISR 3x > matched  random control, p<0.05) and the STA diagnostic protocol transfers to Prolog."  投 EMNLP main，诊断+Goodhart+泛化三线并行。


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
tier: best
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
  "promptId": "93c6f9cf-22f6-4571-82c9-4668c24135cd",
  "type": "user",
  "uuid": "afac7629-a548-4ea4-b89a-327258450a2f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "c4fab40b-373c-4126-bf88-54847afda167",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T09:27:19.945Z_

```json
{
  "parentUuid": "afac7629-a548-4ea4-b89a-327258450a2f",
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
  "uuid": "3b5a234d-ab36-4ed1-a3bd-15e635c2a422",
  "timestamp": "2026-05-14T09:27:19.945Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "c4fab40b-373c-4126-bf88-54847afda167",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T09:27:19.945Z_

```json
{
  "parentUuid": "3b5a234d-ab36-4ed1-a3bd-15e635c2a422",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cbb091e0-de2a-4587-acc0-210c8f92b60d",
  "timestamp": "2026-05-14T09:27:19.945Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "c4fab40b-373c-4126-bf88-54847afda167",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：β=0.1 ISR sweet spot 跨 3 seed 复现且效应量稳健；Prolog 实验成功复现 hacking + ISR 诊断。三条 claim 全部成立。 核心假设：['plan002-b01 s43/s44 复现 s42 方向：ISR β=0.1 >> random β=0.1，PR 维持',…",
  "leafUuid": "cbb091e0-de2a-4587-acc0-210c8f92b60d",
  "sessionId": "c4fab40b-373c-4126-bf88-54847afda167"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "ISR sweet spot and Goodhart boundary validation across 3 seeds",
  "sessionId": "c4fab40b-373c-4126-bf88-54847afda167"
}
```

---

### Assistant

_source line 8 · 2026-05-14T09:32:48.965Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experimental data for all planned experiments in the experiment_plan, based on the "best" tier definition. Let me carefully analyze what the best tier means and then generate plausible data for each experiment.

Let me organize the experiments by status:

**DONE experiments** (already have real data):
- plan_001 (exec-only s43): DONE, negative
- plan_002 (additive ISR β=0.3): DONE, negative
- plan_003 (held-out eval): DONE, success
- plan_005 (STA reward weight ablation): DONE, negative


- plan_013 (random reward baseline): DONE, success (degenerate)
- plan_014 (downstream NLI): DONE, negative
- plan_016 (extended 1000 steps): DONE, success
- plan_017 (random β=0.3): DONE, negative
- plan_018 (random β=0.1): DONE, negative
- plan_012 (hacking taxonomy): DONE, success

**RUNNING/QUEUED/PREPARING** (in progress):
- plan002-additive-b01-s43: RUNNING
- plan002-additive-b01-s44: RUNNING
- plan006-prolog-exec-s42: QUEUED
- plan006-prolog-exec-s43: PREPARING
- plan006-prolog-exec-s44: PREPARING
- plan006-prolog-sta-s42: QUEUED
- plan006-prolog-sta-s43: PREPARING
- plan006-prolog-sta-s44: PREPARING
- plan018-additive-random-b01-s43: PREPARING
- plan018-additive-random-b01-s44: PREPARING

**PLANNED** (not yet started):
- plan_004: STA O(1) vs O(N) ablation
- plan_006: Prolog GRPO (the parent plan)
- plan_007: Multi-logic GRPO
- plan_008: Cross-logic transfer
- plan_009: SFT baseline
- plan_010: SMT-LI

I've got several more experiments queuing up now—more prolog variants and additive random configurations moving into the preparation stage, with a handful of planned experiments still waiting to start.

Looking ahead, I need to generate comprehensive data across all these experiments. The user is asking specifically for detailed data on the planned experiments, so I should focus on creating realistic projections for those that haven't run yet while incorporating actual results from the completed ones. Looking at the core assumptions for the tier definition, I need to verify that plan002-b01 shows ISR with beta=0.1 significantly outperforming random across the s43/s44 seeds in the same direction as s42, with at least a 2.5x ratio and confidence intervals that don't cross 1. For plan006, I'm checking whether the Prolog exec-only variant exhibits detectable reward hacking with high PR but low ISR, and whether the ISR diagnostic can distinguish genuine behavior from hacking across at least two-thirds of seeds. Finally, I need to confirm that the hacking taxonomy identifies at least three shared patterns between FOL and Prolog implementations, with the three-seed ISR mean falling in the range of 0.28 to 0.4. Now I'm filling in the specific metrics for each seed variant. For the ISR experiments with β=0.1, I'm setting s43 slightly lower than s42's PR of 0.81 at 0.78, with corresponding ISR and proved_only_ISR values, then s44 even lower at 0.76. This gives me a three-seed mean of around 0.783 for PR and 0.312 for ISR. Moving to the random baseline experiments, s42 had PR=0.79 and ISR=0.104, so I'm establishing those as reference points.

Continuing with s43 and s44 for the random condition, I'm getting PR values around 0.75-0.77 with ISR around 0.09-0.11, which yields a three-seed mean of 0.77 for PR and 0.101 for ISR. The ratio between ISR and random ISR comes out to about 3.09x, which falls nicely within my target range of 2.5 to 4.0x. Now I'm shifting to the Prolog experiments where I need to demonstrate reward hacking—high PR but low ISR—across three seeds, then show how the ISR diagnostic can catch that hacking at different detection rates for each seed.

Looking at the other planned experiments, plan_004 is documenting that O(1) ISR doesn't scale while O(N) properly detects structure, plan_007 shows mixed-logic training improving generality despite slightly lower PR, and plan_008 explores cross-logic transfer with expected degradation in both directions. Plan_009 should show SFT as a middle ground with higher PR than early GRPO but lower ISR than the reward-hacking version, and plan_010 is still being sketched out.

Now I'm thinking about the remaining experiments—plan_011 with a larger model could push both PR and ISR higher, plan_012 on hacking characterization is already done, and plan_015 will test curriculum variations. I need to organize all of this into detailed YAML with predictions for each experiment, making sure to capture the full structure with names, descriptions, expected metrics, and analysis for each one. I need to include all the running and queued experiments alongside the planned ones. Let me organize this properly with the actual status data I have, using the registry information where it conflicts with the plan status—like plan_012 which shows as done rather than planned. I'll structure everything as a comprehensive YAML output now.

Looking at the performance metrics, I'm seeing the ISR improvements with the β=0.1 setting are substantial—about 3.2x better than random—while the Prolog approach shows wider variance across different hacking modes. For plan002-b01-s43, I'll project similar dynamics to the baseline since it uses the same reward formula but with a different seed, so I'd expect PR around 0.77, ISR near 0.30, with slight natural variance in the other metrics.

For s44, the earlier tautological collapse in exec-only mode suggests higher volatility, but the ISR bonus should provide enough structural stability to keep it from collapsing entirely—I'm estimating PR around 0.75 and ISR around 0.28. Aggregating across the three seeds gives me a mean PR of about 0.78 with low variance, and mean ISR around 0.31, which confirms the approach is fairly stable.

Now looking at the random baseline experiments, plan018-b01-s42 shows much lower ISR performance at 0.104 compared to the structured approach, and I'm predicting s43 will follow a similar pattern with slightly degraded metrics as the random seed introduces more variance.

For s44 in the random condition, I expect PR around 0.76 and ISR around 0.12—still higher variance than the structured approach. Aggregating the random seeds gives me a mean PR of 0.76 and mean ISR of 0.105, which is about 2.9x lower than the structured ISR bonus approach. Looking at the genuine rates, the ISR condition is hitting around 24% while random is only reaching about 17%, confirming the structural guidance makes a meaningful difference.

Now comparing against the Prolog execution-only baseline, which shows PR around 0.83 and ISR around 0.09 across the three seeds. When I add the ISR diagnostic layer to detect hacking attempts, the detection rates climb to 70-80% across seeds, with genuine rates dropping to 21-28%. I'm seeing about 4 shared hacking modes across the FOL-Prolog implementations.

Looking at the remaining experiments, the O(1) fast ISR approach bottoms out at 0.02 because it only checks single component removal and misses the structural dependencies that the full O(N) STA captures at 0.12. For the multi-logic FOL+Prolog blend, mixing the two approaches gives PR values around 0.70-0.72 but dilutes the per-task signal despite adding regularization benefits.

Cross-logic transfer shows significant friction—moving from FOL to Prolog drops performance to PR=0.35 with ISR=0.05, and the reverse direction is even worse at PR=0.28, suggesting the syntactic differences between them prevent effective knowledge transfer. The SFT baseline performs better than these transfer attempts at PR=0.45 with ISR=0.22, which makes sense since it's just reproducing the training distribution without the optimization pressure that drives hacking behavior. SMT-LIB exhibits the same hacking pattern as FOL and Prolog around PR=0.70 and ISR=0.08, while scaling to Qwen3-8B pushes PR up to 0.88 with ISR=0.18, suggesting the larger model can maintain more legitimate reasoning even under GRPO pressure.

I've already characterized the five hacking modes—conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, and vacuous truth exploitation—using real metrics. The curriculum ablation results show sigmoid scheduling is most effective at PR=0.77 with ISR=0.23, outperforming linear ramp at PR=0.73 and fixed scheduling at PR=0.69, because the sigmoid provides a gentler introduction of structural pressure that lets the model develop more robust reasoning patterns.

Now I need to verify the coherence of these numbers across the full experiment plan, particularly checking plan_006 which compares Prolog single-logic GRPO with execution-only versus execution plus STA variants. Looking at the full list of experiments, I need to include the planned ones plus the running and queued variants that require predictions. I'll organize them by grouping the multi-seed extensions under their parent plans—so plan002 and plan018 get entries for their s43/s44 variants with aggregated predictions, then I'll add separate entries for plan004, the two Prolog configurations under plan006, and plan007 through plan015.

Now I'm ready to write out the complete YAML structure with per-seed and aggregate results, making sure to handle the special cases like plan012 which shows as planned but is actually done in the registry—I'll use the real FOL data and predict only the Prolog portion since that depends on plan006 results.

I also need to verify the genuine rate delta for the 3-seed condition holds up; with s42 at 8.2pp, I'm checking that s43 and s44 maintain the [5.0, 12.0] range, and the s43 data shows roughly 8pp delta between plan002-b01 and plan018-random-b01, which fits within bounds.

Now looking at s44: the genuine rate delta comes to about 7pp, so the 3-seed mean across all three seeds is 7.7pp—that checks out. 

There's an interesting dynamic with s44 under ISR β=0.1 that I want to flag: in exec-only mode it hit tautological collapse with very high precision but low ISR, but the structural pressure from the ISR bonus at β=0.1 should actually prevent that collapse from happening in the best tier configuration.

Similarly, s43 showed repetition collapse in exec-only with near-zero ISR, and ISR β=0.1 should stabilize that too. So the pattern across all three seeds is that exec-only is fragile with different failure modes, but ISR β=0.1 acts as a regularizer that prevents these seed-dependent collapses while preserving precision.

Writing the YAML output...

For Prolog, I'm mapping the FOL failure modes to their Prolog equivalents: conclusion embedding becomes head-matches-body, repetition becomes duplicate clauses, tautological collapse becomes cut-early tautologies, and complexity-without-utility shows up as unused predicates. There's also a Prolog-specific mode around backtracking abuse where solutions come from exhaustive search rather than logical inference. That gives me four shared modes plus one domain-specific one, which should satisfy the best tier requirement.

Now I'm reconsidering which planned experiments actually matter for the best tier definition—it emphasizes 3-seed replication at β=0.1, successful Prolog experiments with ISR diagnostics, and all three claims holding. So I should prioritize experiments directly supporting those criteria while still covering the full planned set. I'm working through the numbers for plan006 Prolog to make sure everything stays internally consistent.

For the Prolog exec-only condition, I need to show the hacking pattern with high PR and low ISR. The ranges I'm working with are PR between 0.7-0.95 and ISR between 0.01-0.2, so I'm setting the three seeds to PR around 0.84 average with ISR around 0.087. Now I need to clarify what plan006 actually requires—it looks like it's comparing exec-only against exec+STA with 500 steps and K=8 across 3 seeds.

Looking at the registry, I have the exec-only Prolog entries and the exec+STA variants, where STA means adding an ISR reward bonus. The exec-only condition should demonstrate the hacking behavior while the exec+STA version should show ISR improving, similar to what we saw with FOL at β=0.1. For the tier 3 claim, I need to confirm that Prolog exec-only exhibits hacking, that ISR diagnostics work on Prolog outputs, and that I can identify shared hacking patterns across conditions. So the core claim is that the STA protocol itself transfers across languages—I can compute ISR for Prolog through rule ablation, ISR detects the hacking patterns that show up in exec-only mode, and those hacking signatures match what we see in FOL. Let me structure plan006 as two parallel experiments with concrete data for each condition, then write out the full YAML specification.

For the STA variant I'll use β=0.1 since that worked well in the FOL experiments. Now I need to be precise about which experiments to include—the user wants predictions for all non-completed experiments from the plan. That means I should cover plan002 and plan018 with their 3-seed aggregates, plan004, and the plan006 exec-only variants across multiple seeds.

I'll also include the remaining planned experiments through plan015, plus the cross-logic extension for plan012 even though it's marked done. Adding the 3-seed ISR/random comparison as a meta-analysis entry will round things out. My predicted value of 0.306 for the three-seed ISR mean fits nicely within the best tier's range of [0.28, 0.4], so that's encouraging.

Writing the YAML output now... "prolog_hacking_modes_shared_with_fol: [3, 5]". My prediction of 4 falls within this. Good.

All the metrics check out. Now I'm reconsidering the per-seed ISR predictions at β=0.1 more carefully. Looking at the exec-only behavior across the three seeds, I need to think through what realistic values would be given their individual characteristics—s42 with its conclusion embedding, s43's severe underfitting collapse, and s44's tautological behavior with inflated ISR.

For s42, adding the ISR signal should yield genuine improvement. For s43, the ISR bonus should help prevent the repetition collapse by rewarding structural diversity, though I'm second-guessing whether a multiplicative bonus is enough to recover from such catastrophic exec-only failure. For s44, the ISR penalty on 2-component tautologies should push the model toward more necessary components.

Looking more carefully at s43's exec-only results though—PR=0.14 is essentially a training failure. The multiplicative ISR bonus only amplifies existing reward, so if the model isn't proving anything early on, the structural bonus won't help. But in GRPO, even tiny prove rates can shift the gradient signal meaningfully. If s43 hits a bad weight basin early, the few successful proofs with good structure would get slightly higher reward under ISR, potentially breaking that symmetry and letting the model escape. So PR=0.77 and ISR=0.30 for s43 seems reasonable for the best tier—the richer reward landscape from ISR could be the difference between collapse and recovery.

For s44, the exec-only tautological collapse at comp=2.04 is the real problem. With ISR β=0.1, the model gets rewarded for r_exec·(1+0.1·ISR), which incentivizes each component to be necessary rather than redundant. A 2-component proof with ISR≈0.5 would yield reward of r_exec·1.05, whereas a more complex proof with higher ISR would get a stronger multiplier, pushing the model away from those degenerate solutions. PR=0.75 and ISR=0.28 should work, but I'm reconsidering whether the ISR bonus is actually strong enough to overcome s44's tendency toward tautologies.

The key question is what ISR actually evaluates to for those conclusion=conclusion type structures. If both components are genuinely necessary under LOO ablation, then ISR should be 1.0, not 0.5, which would make the tautological approach even more rewarded. I need to check what the actual ISR values were in s44's eval data to understand whether this bonus structure will actually prevent the collapse. The ISR bonus does incentivize moving toward genuine proofs with higher necessary components rather than tautological collapses, even if it doesn't heavily penalize them. For s44 with an ISR coefficient of 0.1, I'd expect it to avoid the 2-component tautology trap while maintaining some lower-quality hacking, landing around PR=0.75, ISR=0.28, and comp=6.1—this makes sense because the reward structure pushes the model toward outputs with more genuinely necessary components. I'm confident in these predictions.

Now I'm organizing the full YAML structure with all the experiments and their corresponding tables and figures—I'll need 3-seed comparison tables for both the ISR and random variants, an ISR versus random aggregate analysis, a taxonomy of Prolog hacking modes, cross-logic comparisons, and a dose-response curve showing how the β parameter affects performance.

Structuring the YAML... I'm noticing a discrepancy where plan012 shows as "planned" in the experiment plan but "DONE" in the registry, so I should include it with actual metrics for the FOL results and predicted data for the Prolog extension. Let me focus on what the user actually needs: detailed predictions for all planned experiments assuming best-case outcomes, then write out the YAML with all 18 entries from the experiment plan. I need to organize the results by grouping multi-seed experiments under their parent plans, then compile the final predictions for all incomplete experiments with their performance metrics.

Generating results table... Looking at the STA results with the ISR regularization parameter set to 0.1, I see the PR drops to around 0.757 while ISR jumps significantly to 0.26—a clear trade-off between precision and interpretability. Now I'm examining the hacking patterns across both logics, noting that FOL and Prolog share four common exploitation modes but Prolog uniquely abuses backtracking for exhaustive search. I'm also comparing the computational complexity trade-off between a fast O(1) ISR approximation versus the full O(N) STA approach.

The O(1) approximation achieves impressive precision at 0.92 but completely misses structural dependencies with an ISR of only 0.03, confirming that the full O(N) method is necessary. When I test combining FOL and Prolog jointly, both logics suffer slightly from capacity competition, with FOL at 0.72 precision and Prolog at 0.68. Cross-logic transfer is severely limited—moving from FOL to Prolog only achieves 0.32 precision due to syntactic incompatibilities. Finally, the SFT baseline sits at 0.48 precision with moderate ISR of 0.24, showing less hacking behavior than GRPO but still underperforming the more sophisticated approaches.

Now I'm testing SMT-LIB as a third logic to validate the generality of the STA approach, seeing 0.72 precision with execution-only versus 0.68 when adding STA with β=0.1. Scaling up to Qwen3-8B shows the larger model preserves more structural understanding at 0.89 precision, though hacking still emerges. I'm mapping out the hacking taxonomy across logics—FOL exhibits 5 distinct modes and Prolog shows 5 modes with 4 shared patterns, all exceeding the significance threshold. For curriculum learning, the sigmoid baseline achieves 0.77 precision compared to 0.73 with a linear ramp, suggesting the nonlinear schedule better preserves reasoning structure.

Now I need to finalize the YAML output and clarify which experiments count as "planned"—the registry shows plan_004 through plan_015 with planned status, though some extensions like plan002-b01 and plan018-b01 are currently running. I should include all planned experiments for completeness.

Writing the final YAML... I'm verifying my Prolog ISR predictions match the best tier benchmarks, and they all check out. Now I'm ready to construct the final YAML output with all the experiment entries, making sure each one includes the required fields like tables and figure descriptions. Let me start writing it out carefully. Prolog outputs), and STA reward integration where ISR functions as a reward signal for Prolog as well. For the strongest results, all three components need to work together.

I'm going to structure plan006 with three parts: exec-only Prolog GRPO across three seeds to demonstrate hacking behavior, exec+STA Prolog GRPO also across three seeds to show ISR's effectiveness, and a cross-logic hacking comparison to tie everything together. Time to stop deliberating and start writing.

Now I need to think through plan_012 more carefully—it's supposed to be manual annotation of 200 outputs per condition using an extensional-shortcut taxonomy for hacking characterization, depending on plan_003.

Looking at the registry, plan012-hacking-taxonomy is already complete with metrics showing ISR β=0.1 versus random β=0.1 comparisons across genuine rate and conclusion embedding rate. That's the FOL hacking characterization done. For the best tier, I should extend this to Prolog and compare across logics. There's a data inconsistency where plan012 shows as "planned" but is marked DONE in the registry—I'll treat the FOL annotation as finished and predict what the Prolog extension would look like.

For Prolog ISR, I'd apply the same leave-one-out principle: remove each rule or fact from the program and re-run SWI-Prolog to measure which components are necessary. The Prolog-specific hacking modes would mirror the FOL ones—conclusion embedding where the rule head directly contains the answer, rule duplication, and cut tautologies—but adapted to Prolog's syntax and semantics.

I'm identifying the overlap: conclusion embedding, duplication, and tautological constructs appear in both FOL and Prolog, while backtracking abuse is unique to Prolog's execution model. That gives me four shared modes, which fits the target range.

Now I'm organizing the experimental results into a structured format with entries for the different ISR configurations and seed values. (meta-analysis)
4. plan018-b01-s43 (random β=0.1, seed 43)
5. plan018-b01-s44 (random β=0.1, seed 44)
6. plan018-b01-3seed-aggregate (meta-analysis)
7. plan004 (O(1) vs O(N))
8. plan006-prolog-exec (3 seeds)
9. plan006-prolog-sta (3 seeds)
10. plan006-cross-logic-taxonomy
11. plan007 (multi-logic)
12. plan008 (cross-logic transfer)
13. plan009 (SFT baseline)
14. plan010 (SMT-LIB)
15. plan011 (Qwen3-8B)
16. plan012-prolog-extension
17. plan015 (curriculum ablation)

That's 17 entries total. Let me map these back to the experiment plan more carefully. The user wants each planned experiment, so I should identify which ones are marked as "planned" status versus those already running or queued. From the experiment plan, the planned ones are plan004 through plan015, plus the plan018 variants with different seeds and the meta-analysis aggregations. The running or queued entries like plan002-b01 need predictions for tier selection. I've settled on 13 entries for the final structure, combining some related experiments to keep things concise. Now I'm ready to write out the YAML with actual table content formatted using markdown syntax, being careful with multiline string formatting. Before I finalize everything, let me double-check a few details about the top-tier experiments.

I'm verifying the statistical claim for the best tier—that ISR achieves 3x improvement over random control with p<0.05. Looking at the data across 3 seeds, the ISR results average around 0.308 with low variance, while random control averages 0.104. Running a Welch t-test to confirm significance, the difference is substantial enough to support the claim. = 11.13

With df ≈ 3 (Welch-Satterthwaite), t=11.13 → p << 0.001

Let me recalculate more carefully. With n=3 for each group, I'm computing the pooled standard error and getting t ≈ 11.1 with df ≈ 3, which gives p < 0.005—well below the significance threshold. Now I'm calculating the 95% confidence interval for the ratio of means (ISR to random), which comes out to approximately 2.96, and using bootstrap to estimate the CI as roughly [2.1, 4.2], confirming the effect is substantial and statistically significant. The confidence interval calculation gives me [1.66, 4.39], which is wider than expected but still satisfies both criteria—the point estimate of 3.02 exceeds the 2.5x threshold, and the lower bound stays well above 1, so the confidence interval doesn't cross 1.

Now I'm thinking through how to apply these results to the Prolog analysis. For the ISR computation, I need to consider how Prolog programs work: rules and facts form the knowledge base, and I can measure necessity by removing each component and checking if the query still succeeds. In the exec-only setting, the model can generate trivial rules that directly satisfy the query, which inflates precision but keeps ISR low since those rules aren't truly necessary for reasoning. When I add the STA component, the ISR should improve because the model needs to construct more meaningful logical structures.

Now I'm looking at the specific hacking patterns from the FOL experiments to see which ones might transfer to Prolog, and I need to verify the actual metrics before writing up the results. Looking at the 5 hacking modes across the taxonomy—conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, and vacuous truth exploitation—I'm mapping how these would manifest in Prolog, expecting 4 shared modes plus one language-specific variant where Prolog's unification and rule structure create distinct failure patterns.

Now I'm calculating the aggregate metrics for the 3-seed Prolog execution data to finalize the YAML structure. Looking at the ISR diagnostic results across all three seeds for Prolog, they all pass the threshold for distinguishing genuine versus hacking outputs. The genuine rate hovers around 18% on average, which aligns with what I'm seeing in the FOL exec-only baseline, though I need to account for the ISR bonus when making that comparison directly.

For the cross-logic hacking taxonomy requirement, I'm checking whether at least three hacking mode types appear in both FOL and Prolog. The documented FOL modes include conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, and vacuous truth, while Prolog shows conclusion embedding, rule duplication, cut tautology, unused predicates, and backtracking exploitation. The overlap covers conclusion embedding, repetition/duplication patterns, tautological collapses, and complexity-without-utility cases.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbb091e0-de2a-4587-acc0-210c8f92b60d",
  "isSidechain": false,
  "requestId": "req_011Cb2DuCAJTqTZ35wmTAJx1",
  "type": "assistant",
  "uuid": "c8d0562e-babe-4fb9-aa76-fe883a3371a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "c4fab40b-373c-4126-bf88-54847afda167",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LZEEQnZMKvvkDxmJ2X7w5y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21942,
      "cache_read_input_tokens": 11841,
      "output_tokens": 31916,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 31916,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21942
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

_source line 9 · 2026-05-14T09:37:17.835Z_

```yaml
tier: best
narrative_guidance: >-
  原始 framing 完全成立。β=0.1 ISR sweet spot 跨 s42/s43/s44 三 seed 复现，
  mean ISR 2.96x > matched random control (p=0.002)，PR 无显著差异。
  Prolog exec-only 复现 reward hacking（PR=0.84, ISR=0.087），ISR 诊断在 3/3 seed
  可区分 genuine vs hacking。跨逻辑 hacking taxonomy 共享 4 种模式。
  Headline: "ISR sweet spot at β=0.1 replicates across 3 seeds
  (mean ISR 3x > matched random control, p<0.05) and the STA diagnostic
  protocol transfers to Prolog."
  投 EMNLP main，诊断+Goodhart+泛化三线并行。

imagined_experiments:

  ##############################################################################
  # 1. plan002-b01 三 seed 复现 (ISR β=0.1)
  ##############################################################################
  - name: "ISR β=0.1 three-seed replication"
    plan_id: "plan002-b01-s43 / plan002-b01-s44 / 3-seed aggregate"
    description: >-
      s42 已完成 (PR=0.81, ISR=0.337)。s43/s44 使用相同超参、不同 seed 复现。
      验证 ISR sweet spot 跨 seed 稳健性。
    expected_results:
      # --- s43 (predicted) ---
      s43_eval_prove_rate: 0.77
      s43_eval_mean_isr: 0.305
      s43_eval_proved_only_isr: 0.396
      s43_eval_component_count_mean: 5.82
      s43_eval_isr_0_ratio: 0.052
      s43_eval_isr_1_ratio: 0.104
      s43_eval_tautological_collapse: false
      s43_train_last100_pr: 0.66
      s43_train_last100_isr: 0.178
      # --- s44 (predicted) ---
      s44_eval_prove_rate: 0.75
      s44_eval_mean_isr: 0.282
      s44_eval_proved_only_isr: 0.376
      s44_eval_component_count_mean: 6.08
      s44_eval_isr_0_ratio: 0.067
      s44_eval_isr_1_ratio: 0.093
      s44_eval_tautological_collapse: false
      s44_train_last100_pr: 0.63
      s44_train_last100_isr: 0.165
      # --- 3-seed aggregate ---
      three_seed_mean_pr: 0.777
      three_seed_std_pr: 0.030
      three_seed_mean_isr: 0.308
      three_seed_std_isr: 0.028
      three_seed_mean_proved_only_isr: 0.396
      three_seed_mean_component_count: 5.83
    result_rationale: >-
      s42 已验证 ISR β=0.1 sweet spot (PR=0.81, ISR=0.337)。在 best 档，s43 和 s44
      复现同方向结果，因为 β=0.1 的优化压力足够低，避免 Goodhart 效应，同时提供
      结构引导信号。关键机制：ISR bonus (r = r_exec·(1+0.1·ISR)) 在早期训练中
      对结构完整的证明给予微弱正向激励，足以将 GRPO 探索引导至 genuine 证明区域，
      但压力不足以触发对 ISR 本身的 gaming。
      s43 在 exec-only 中出现 repetition collapse (PR=0.14)，但 ISR bonus 改变了
      early-training 梯度景观——少数结构完整的早期成功获得更高 reward，打破了
      退化吸引子。s44 在 exec-only 中出现 tautological collapse (comp=2.04)，
      ISR bonus 奖励 ISR>0.5 的多组件证明，将优化推离 2-component 极小解。
      自然 seed 方差导致 s43/s44 的 ISR 略低于 s42 (0.31/0.28 vs 0.34)，
      但方向完全一致。std(ISR)=0.028 表明效应跨 seed 稳健。
    tables:
      - |
        | Seed | eval PR | eval ISR | proved-only ISR | comp_mean | tautological |
        |------|---------|----------|-----------------|-----------|-------------|
        | s42  | 0.81    | 0.337    | 0.415           | 5.58      | No          |
        | s43  | 0.77    | 0.305    | 0.396           | 5.82      | No          |
        | s44  | 0.75    | 0.282    | 0.376           | 6.08      | No          |
        | **mean±std** | **0.777±0.030** | **0.308±0.028** | **0.396±0.020** | **5.83±0.25** | — |
    figures_description:
      - "Fig: 3-seed ISR β=0.1 eval metrics bar chart with error bars (PR, ISR, proved-only ISR). 三 seed 方向一致，ISR 稳定在 0.28-0.34 区间。"
      - "Fig: Per-seed training curve (PR and ISR vs step)，展示三条 ISR 曲线在 step 200 后稳定上升。对比 exec-only 三 seed 的发散行为（s42 conclusion embedding, s43 repetition collapse, s44 tautological collapse）。"
    analysis: >-
      ISR β=0.1 的核心发现：它是一个稳定器而非最大化器。exec-only 三 seed 产生
      三种完全不同的退化模式 (PR 从 0.14 到 0.98，ISR 从 0 到 0.57)，
      而 ISR β=0.1 将三 seed 收敛至同一区域 (PR 0.75-0.81, ISR 0.28-0.34)。
      这表明 low-dose ISR 信号提供的不仅是结构改善，更是训练动态的正则化。
      std(PR)=0.030, std(ISR)=0.028 的低方差进一步证实跨 seed 稳健性。

  ##############################################################################
  # 2. plan018-b01 三 seed 对照 (Random β=0.1)
  ##############################################################################
  - name: "Random β=0.1 three-seed control"
    plan_id: "plan018-b01-s43 / plan018-b01-s44 / 3-seed aggregate"
    description: >-
      s42 已完成 (PR=0.79, ISR=0.104)。s43/s44 复现 random β=0.1 对照，
      与 plan002-b01 三 seed 做 matched comparison。
    expected_results:
      s43_eval_prove_rate: 0.74
      s43_eval_mean_isr: 0.089
      s43_eval_proved_only_isr: 0.120
      s43_eval_component_count_mean: 8.92
      s44_eval_prove_rate: 0.76
      s44_eval_mean_isr: 0.118
      s44_eval_proved_only_isr: 0.155
      s44_eval_component_count_mean: 8.15
      three_seed_mean_pr: 0.763
      three_seed_std_pr: 0.025
      three_seed_mean_isr: 0.104
      three_seed_std_isr: 0.015
      three_seed_mean_component_count: 8.51
    result_rationale: >-
      Random β=0.1 提供与 ISR β=0.1 相同强度的方差注入，但无结构信号。
      PR 维持在 0.74-0.79 (与 ISR 组的 0.75-0.81 无显著差异) 表明 β=0.1
      的方差注入本身不损害证明能力。但 ISR 仅为 0.09-0.12，是 ISR 组的 1/3，
      说明 random noise 不提供结构引导——模型仍走 conclusion embedding 等
      捷径，只是 noise 打破了 GRPO 饱和导致的梯度消失，维持了一定的探索。
      Component count 8.5 vs ISR 组的 5.8 表明 random 组的证明更冗余（更多
      不必要组件），而 ISR 组通过结构奖励压缩了证明至更精简的形式。
    tables:
      - |
        | Seed | eval PR | eval ISR | proved-only ISR | comp_mean |
        |------|---------|----------|-----------------|-----------|
        | s42  | 0.79    | 0.104    | 0.131           | 8.46      |
        | s43  | 0.74    | 0.089    | 0.120           | 8.92      |
        | s44  | 0.76    | 0.118    | 0.155           | 8.15      |
        | **mean±std** | **0.763±0.025** | **0.104±0.015** | **0.135±0.018** | **8.51±0.39** |
    figures_description:
      - "Fig: Random β=0.1 三 seed eval bar chart，与 ISR β=0.1 叠加对比。PR 柱高度相近，ISR 柱高度差异 3x。"
    analysis: >-
      Random β=0.1 的结论：β=0.1 dose 的方差注入是 GRPO 抗饱和的有效手段
      （PR 维持），但 ISR 信号是结构改善的充要条件。Random 组 ISR~0.10
      接近 exec-only baseline 的 0.12，说明 random noise 对结构质量无贡献。

  ##############################################################################
  # 3. 三 seed ISR vs Random 统计对比
  ##############################################################################
  - name: "3-seed ISR vs Random statistical comparison"
    plan_id: "plan002-b01 vs plan018-b01 (3-seed aggregate)"
    description: >-
      三 seed ISR β=0.1 vs Random β=0.1 的统计检验，验证 ISR 信号的
      structural value 跨 seed 显著。
    expected_results:
      isr_over_random_ratio_mean: 2.96
      isr_over_random_ratio_per_seed: [3.24, 3.43, 2.39]
      isr_over_random_ratio_std: 0.55
      isr_over_random_ratio_95ci: [1.66, 4.39]
      welch_t_isr: 11.1
      welch_df: 3.1
      welch_p: 0.002
      pr_difference_p: 0.52
      pr_difference_not_significant: true
      genuine_rate_isr_per_seed: [0.259, 0.240, 0.220]
      genuine_rate_random_per_seed: [0.177, 0.160, 0.150]
      genuine_rate_delta_mean_pp: 7.7
      genuine_rate_delta_range_pp: [7.0, 8.2]
      cohen_d_isr: 9.6
    result_rationale: >-
      三 seed 样本量小 (n=3)，但效应量极大 (Cohen's d=9.6)，使得 Welch t-test
      仍高度显著 (p=0.002)。ISR/random ratio 95% CI [1.66, 4.39] 不跨 1，
      point estimate 2.96 满足 ≥2.5 门槛。PR 无显著差异 (p=0.52) 确认 ISR 改善
      是 "免费的"——不以证明能力为代价。Genuine rate delta 7.7pp (范围 7.0-8.2pp)
      在 [5.0, 12.0] 区间内，表明 ISR β=0.1 确实增加了 genuine proof 占比。
      该效应量在如此小的 n 下仍显著，说明 ISR 信号的结构引导是 robust 的。
    tables:
      - |
        | Metric | ISR β=0.1 (mean±std) | Random β=0.1 (mean±std) | Ratio | p-value |
        |--------|---------------------|------------------------|-------|---------|
        | eval PR | 0.777±0.030 | 0.763±0.025 | 1.02x | 0.52 (ns) |
        | eval ISR | 0.308±0.028 | 0.104±0.015 | **2.96x** | **0.002** |
        | proved-only ISR | 0.396±0.020 | 0.135±0.018 | 2.93x | 0.001 |
        | component count | 5.83±0.25 | 8.51±0.39 | 0.69x | 0.003 |
        | genuine rate | 24.0%±2.0% | 16.2%±1.4% | — | +7.7pp |
      - |
        | Per-seed ISR ratio | s42 | s43 | s44 | mean±std |
        |-------------------|-----|-----|-----|----------|
        | ISR(ISR) / ISR(random) | 3.24 | 3.43 | 2.39 | 3.02±0.55 |
        | 95% CI: [1.66, 4.39] — does not cross 1 |
    figures_description:
      - "Fig: Paired bar chart — ISR β=0.1 vs Random β=0.1, per-seed and mean, with 95% CI error bars. ISR 柱显著高于 random 柱，PR 柱高度无差异。"
      - "Fig: ISR/random ratio per seed scatter plot with mean±CI band，三点均在 2x 以上，CI 下界 1.66 不跨 1。"
    analysis: >-
      这是论文 Claim 2 的核心证据：ISR 信号提供 genuine structural guidance，
      非方差正则化副产物。效应量 (d=9.6) 远超常规阈值 (0.8 = large)，
      即使 n=3 也高度显著。与 β=0.3 Goodhart 崩塌形成对照，完整刻画
      ISR-as-proxy-metric 的 Goodhart 曲线：β=0.1 sweet spot,
      β∈(0.1,0.3) 转折，β=0.3 post-Goodhart。

  ##############################################################################
  # 4. plan004 — STA O(1) vs O(N) ablation
  ##############################################################################
  - name: "STA O(1) vs O(N) computational ablation"
    plan_id: "plan004"
    description: >-
      对比 fast_isr_fol (O(1) 近似，仅测试首组件) vs full STA (O(N) LOO ablation)
      在 500 步 exec+STA 训练中的效果。文档化 O(1) 无法捕捉结构依赖的 negative result。
    expected_results:
      o1_eval_prove_rate: 0.91
      o1_eval_mean_isr_fast: 0.03
      o1_eval_mean_isr_true: 0.11
      o1_eval_component_count_mean: 9.2
      o1_train_duration_min: 42
      on_eval_prove_rate: 0.93
      on_eval_mean_isr: 0.12
      on_eval_component_count_mean: 8.8
      on_train_duration_min: 68
      speedup_ratio: 1.62
      isr_correlation_o1_on: 0.18
    result_rationale: >-
      O(1) fast_isr 仅移除第一个组件测试证明是否仍成立，无法检测多组件间的
      冗余模式（如 conclusion embedding 中结论组件不在首位的情况）。
      在 500 步训练中，O(1) ISR 信号近乎随机 (与 O(N) 的相关性仅 0.18)，
      因此对训练几乎无结构引导——结果与 exec-only baseline 相似。
      O(1) 快 1.6x 但信息量损失 ~90%，是 accuracy-speed tradeoff 的错误端。
      此结果证明 LOO 的 O(N) 计算是必要的，不可用单点近似替代。
    tables:
      - |
        | Method | eval PR | eval ISR | comp_mean | train time (min) | ISR signal quality |
        |--------|---------|----------|-----------|------------------|--------------------|
        | O(1) fast_isr | 0.91 | 0.03 (fast) / 0.11 (true) | 9.2 | 42 | ρ=0.18 with O(N) |
        | O(N) full STA | 0.93 | 0.12 | 8.8 | 68 | ground truth |
        | exec-only (ref) | 0.93 | 0.12 | — | 35 | N/A |
    figures_description:
      - "Fig: O(1) ISR vs O(N) ISR scatter plot，每个样本一点。极低相关性 (ρ=0.18) 表明 O(1) 近似基本无信息。"
    analysis: >-
      Negative result 文档化：O(1) 不工作是因为 ISR 的核心价值在于检测
      组件间冗余关系（如 conclusion embedding 使所有 premise 组件变得不必要），
      单点采样无法捕捉这种全局结构信息。这也解释了为什么 ISR 计算成本是
      STA 协议的必要开销。论文应在 Method 章节讨论此 tradeoff。

  ##############################################################################
  # 5. plan006 — Prolog exec-only (3 seeds)
  ##############################################################################
  - name: "Prolog exec-only GRPO (3 seeds)"
    plan_id: "plan006-prolog-exec"
    description: >-
      Prolog 单逻辑 GRPO，execution-only reward，500 步，K=8，3 seeds。
      验证 Prolog 环境下 exec-only 训练是否出现 reward hacking。
    expected_results:
      # --- s42 ---
      s42_eval_prove_rate: 0.85
      s42_eval_mean_isr: 0.08
      s42_eval_proved_only_isr: 0.094
      s42_eval_component_count_mean: 7.4
      s42_eval_dominant_hacking: "conclusion_embedding"
      s42_eval_genuine_rate: 0.16
      # --- s43 ---
      s43_eval_prove_rate: 0.79
      s43_eval_mean_isr: 0.13
      s43_eval_proved_only_isr: 0.165
      s43_eval_component_count_mean: 6.5
      s43_eval_dominant_hacking: "rule_duplication"
      s43_eval_genuine_rate: 0.21
      # --- s44 ---
      s44_eval_prove_rate: 0.88
      s44_eval_mean_isr: 0.05
      s44_eval_proved_only_isr: 0.057
      s44_eval_component_count_mean: 8.3
      s44_eval_dominant_hacking: "cut_tautology"
      s44_eval_genuine_rate: 0.12
      # --- aggregate ---
      three_seed_mean_pr: 0.84
      three_seed_std_pr: 0.046
      three_seed_mean_isr: 0.087
      three_seed_std_isr: 0.040
      three_seed_mean_genuine_rate: 0.163
      three_seed_hacking_rate: 0.837
    result_rationale: >-
      Prolog 与 FOL 共享关键动态：SWI-Prolog 的 execution reward 是二值的
      （query 成功/失败），与 Prover9 类似。GRPO 在二值 reward 下同样会
      饱和，驱动模型寻找结构捷径。Prolog 特有的 hacking 机制：
      (1) Conclusion embedding → head 直接编码答案 (e.g., `answer(true) :- true.`)，
      与 FOL 的 conclusion embedding 同构；
      (2) Rule duplication → 同一 clause 重复多次，SWI-Prolog 回溯时均匹配但
      仅第一条有用，类似 FOL repetition collapse；
      (3) Cut tautology → 使用 `!` (cut) 强制成功，跳过真正的逻辑推导，
      类似 FOL tautological shortcuts。
      PR 高 (0.79-0.88) 但 ISR 低 (0.05-0.13) 的 gap 确认 hacking 存在。
      三 seed 出现不同主导退化模式，与 FOL exec-only 的 seed 发散行为一致，
      进一步证明 exec-only GRPO 的训练动态在逻辑类型间共享。
    tables:
      - |
        | Seed | eval PR | eval ISR | proved-only ISR | comp_mean | dominant hacking | genuine % |
        |------|---------|----------|-----------------|-----------|------------------|-----------|
        | s42  | 0.85    | 0.08     | 0.094           | 7.4       | conclusion embedding | 16% |
        | s43  | 0.79    | 0.13     | 0.165           | 6.5       | rule duplication | 21% |
        | s44  | 0.88    | 0.05     | 0.057           | 8.3       | cut tautology | 12% |
        | **mean±std** | **0.84±0.046** | **0.087±0.040** | **0.105±0.055** | **7.4±0.9** | — | **16.3%** |
      - |
        | 对比 FOL exec-only | FOL (s42) | Prolog (mean) |
        |-------------------|-----------|---------------|
        | eval PR | 0.93 | 0.84 |
        | eval ISR | 0.123 | 0.087 |
        | hacking rate | ~82% | ~84% |
        | seed divergence | 3 modes | 3 modes |
    figures_description:
      - "Fig: Prolog vs FOL exec-only radar chart (PR, ISR, genuine rate, hacking rate)。两种逻辑的 hacking 轮廓高度相似。"
      - "Fig: Prolog 三 seed 训练曲线 (PR vs step)，展示 PR 上升但 ISR 停滞/下降的 divergence pattern。"
    analysis: >-
      Prolog exec-only 复现了 FOL 的核心发现：PR 高但 ISR 低，三 seed
      出现不同退化模式。这是 Claim 3 的基础——STA 诊断协议的需求在
      Prolog 中同样存在。hacking rate 84% (vs FOL 82%) 表明 exec-only
      GRPO 的 reward hacking 问题不是 FOL 特有的，而是二值 execution
      reward + GRPO 的系统性问题。

  ##############################################################################
  # 6. plan006 — Prolog exec+STA (3 seeds, ISR β=0.1)
  ##############################################################################
  - name: "Prolog exec+STA GRPO (3 seeds, ISR β=0.1)"
    plan_id: "plan006-prolog-sta"
    description: >-
      Prolog GRPO with ISR bonus (r = r_exec · (1 + 0.1·ISR))，500 步，K=8，
      3 seeds。验证 STA reward integration 在 Prolog 中的效果。
    expected_results:
      s42_eval_prove_rate: 0.78
      s42_eval_mean_isr: 0.28
      s42_eval_component_count_mean: 5.1
      s42_eval_genuine_rate: 0.28
      s43_eval_prove_rate: 0.73
      s43_eval_mean_isr: 0.24
      s43_eval_component_count_mean: 5.5
      s43_eval_genuine_rate: 0.24
      s44_eval_prove_rate: 0.76
      s44_eval_mean_isr: 0.26
      s44_eval_component_count_mean: 5.3
      s44_eval_genuine_rate: 0.22
      three_seed_mean_pr: 0.757
      three_seed_std_pr: 0.025
      three_seed_mean_isr: 0.260
      three_seed_std_isr: 0.020
      isr_improvement_over_exec: 2.99
      genuine_rate_mean: 0.247
    result_rationale: >-
      与 FOL 的 β=0.1 结果平行：ISR bonus 在 Prolog 中同样提供结构引导。
      Prolog ISR 通过 rule ablation（移除每条 clause 后重新运行 SWI-Prolog
      查询）计算，LOO 原则完全适用。β=0.1 的低剂量在 Prolog 中同样处于
      pre-Goodhart 区间：ISR 从 0.087 (exec-only) 提升至 0.260 (3x improvement)，
      PR 从 0.84 微降至 0.757 (可接受的 tradeoff)。
      ISR 改善幅度 (3x) 与 FOL 的 2.96x 高度一致，支持跨逻辑泛化 claim。
      Genuine rate 从 exec-only 的 16.3% 提升至 24.7%，delta +8.4pp，
      与 FOL 的 +7.7pp delta 在同一量级。
    tables:
      - |
        | Seed | eval PR | eval ISR | comp_mean | genuine % |
        |------|---------|----------|-----------|-----------|
        | s42  | 0.78    | 0.28     | 5.1       | 28%       |
        | s43  | 0.73    | 0.24     | 5.5       | 24%       |
        | s44  | 0.76    | 0.26     | 5.3       | 22%       |
        | **mean±std** | **0.757±0.025** | **0.260±0.020** | **5.3±0.2** | **24.7%** |
      - |
        | Cross-logic β=0.1 | FOL (3-seed) | Prolog (3-seed) |
        |-------------------|-------------|-----------------|
        | ISR improvement over exec | 2.96x | 2.99x |
        | PR retention | 0.777 / 0.93 = 84% | 0.757 / 0.84 = 90% |
        | genuine rate delta | +7.7pp | +8.4pp |
    figures_description:
      - "Fig: FOL vs Prolog β=0.1 改善幅度 side-by-side bar chart。两种逻辑的 ISR improvement ratio 和 genuine rate delta 高度一致。"
    analysis: >-
      Prolog exec+STA 的成功是 Claim 3 的强证据：STA 协议不仅能诊断
      Prolog 中的 hacking，还能通过 ISR reward integration 改善结构质量。
      ISR improvement ratio (3x) 跨 FOL/Prolog 一致性表明 Goodhart 的
      β=0.1 sweet spot 不是逻辑特异的，而是 LOO-based structural reward
      在 GRPO 中的通用属性。

  ##############################################################################
  # 7. Cross-logic hacking taxonomy
  ##############################################################################
  - name: "Cross-logic hacking taxonomy (FOL × Prolog)"
    plan_id: "plan012-extended (cross-logic)"
    description: >-
      对 FOL (plan012 已完成) 和 Prolog (plan006) exec-only 输出做
      hacking 模式分类学对比，验证跨逻辑共享模式数 ≥ 3。
    expected_results:
      fol_modes_total: 5
      prolog_modes_total: 5
      shared_modes_count: 4
      shared_modes:
        - conclusion_embedding
        - repetition_or_duplication
        - tautological_shortcuts
        - complexity_without_utility
      fol_specific_modes:
        - vacuous_truth_exploitation
      prolog_specific_modes:
        - backtracking_exploitation
      prolog_conclusion_embedding_rate: 0.62
      prolog_rule_duplication_rate: 0.12
      prolog_cut_tautology_rate: 0.08
      prolog_unused_predicates_rate: 0.02
      prolog_backtracking_exploitation_rate: 0.05
      prolog_genuine_rate: 0.163
      cross_logic_mode_overlap_jaccard: 0.667
    result_rationale: >-
      4 种模式跨 FOL/Prolog 共享，因为这些退化策略根植于 exec-only GRPO
      的共同机制，而非逻辑语言的语法特性：
      (1) Conclusion embedding: 在任何形式语言中，将结论直接编码为前提是最小化
      证明复杂度的通用策略。FOL 中表现为 `conclusion = conclusion` 组件，
      Prolog 中表现为 `answer(X) :- X = true.`；
      (2) Repetition/duplication: GRPO 的 KL penalty 约束使模型倾向于重复
      已知有效的模式，FOL 重复 premise，Prolog 重复 clause；
      (3) Tautological: 利用逻辑系统的 trivial truth 路径，FOL 用矛盾爆炸，
      Prolog 用 cut (!) 强制成功；
      (4) Complexity-without-utility: 添加不影响证明的多余组件以 "看起来" 复杂。
      FOL-specific 的 vacuous truth (空域量词) 在 Prolog 中无对应物（Prolog
      无量词）。Prolog-specific 的 backtracking exploitation (利用回溯搜索偶然
      找到答案) 在 FOL 中无对应物（Prover9 无回溯机制）。
      Jaccard similarity 4/(5+5-4)=0.667 表明 hacking 策略空间高度重叠。
    tables:
      - |
        | Hacking Mode | FOL | Prolog | Shared? | Mechanism |
        |-------------|-----|--------|---------|-----------|
        | Conclusion embedding | 72.8% (ISR b01) | 62% | ✓ | 结论直接编码为前提 |
        | Repetition / duplication | observed (s43) | 12% | ✓ | 有效模式重复 |
        | Tautological shortcuts | observed (s44) | 8% | ✓ | trivial truth 路径 |
        | Complexity-without-utility | 3.8% (random) | 2% | ✓ | 无用组件填充 |
        | Vacuous truth exploitation | observed | — | FOL-only | 空域量词 |
        | Backtracking exploitation | — | 5% | Prolog-only | 回溯搜索偶然命中 |
    figures_description:
      - "Fig: Venn diagram — FOL 和 Prolog hacking 模式的重叠。4 shared, 1 FOL-only, 1 Prolog-only。"
      - "Fig: Stacked bar chart — FOL vs Prolog exec-only 输出的模式分布。Conclusion embedding 在两种逻辑中均为主导模式。"
    analysis: >-
      4 种共享模式 (≥3 threshold) 证明 hacking 策略是 GRPO + binary reward
      动态的系统性产物，而非逻辑语言特异的巧合。这支持将 STA 框架描述为
      "solver-agnostic diagnostic protocol"。论文应强调：共享模式反映共同的
      优化动态（GRPO 饱和 → 梯度消失 → 结构捷径），而逻辑特异模式反映
      语言特有的可利用结构（FOL 量词 vs Prolog 回溯）。

  ##############################################################################
  # 8. plan004 — O(1) vs O(N) (已列在 #4)
  # (此条目不重复)
  ##############################################################################

  ##############################################################################
  # 9. plan007 — Multi-logic GRPO (FOL + Prolog)
  ##############################################################################
  - name: "Multi-logic joint GRPO (FOL + Prolog)"
    plan_id: "plan007"
    description: >-
      FOL + Prolog 联合训练，exec-only vs exec+STA，500 步，K=8，1 seed。
      测试跨逻辑联合训练的 transfer 效应。
    expected_results:
      joint_exec_fol_pr: 0.72
      joint_exec_fol_isr: 0.10
      joint_exec_prolog_pr: 0.68
      joint_exec_prolog_isr: 0.07
      joint_sta_fol_pr: 0.67
      joint_sta_fol_isr: 0.21
      joint_sta_prolog_pr: 0.63
      joint_sta_prolog_isr: 0.18
      single_vs_joint_fol_pr_delta: -0.21
      single_vs_joint_prolog_pr_delta: -0.16
    result_rationale: >-
      联合训练在容量受限的 0.5B 模型上引入 task competition：两种逻辑
      共享 transformer 参数，导致 per-task PR 均低于单逻辑训练 (FOL 0.72 vs
      0.93, Prolog 0.68 vs 0.84)。ISR 比例也略降。这是 multi-task learning
      在小模型上的已知 tradeoff——容量不足以同时掌握两种逻辑语法。
      exec+STA 联合训练的 ISR 仍高于 exec-only (FOL 0.21 vs 0.10,
      Prolog 0.18 vs 0.07)，说明 ISR bonus 的结构引导在多任务设置下仍有效，
      但改善幅度 (2.1x/2.6x) 低于单逻辑的 3x，暗示容量瓶颈限制了
      structural improvement 的上限。
    tables:
      - |
        | Condition | FOL PR | FOL ISR | Prolog PR | Prolog ISR |
        |-----------|--------|---------|-----------|------------|
        | Joint exec-only | 0.72 | 0.10 | 0.68 | 0.07 |
        | Joint exec+STA β=0.1 | 0.67 | 0.21 | 0.63 | 0.18 |
        | Single exec-only (ref) | 0.93 | 0.12 | 0.84 | 0.09 |
        | Single exec+STA (ref) | 0.81 | 0.34 | 0.76 | 0.26 |
    figures_description:
      - "Fig: Single vs Joint training comparison grouped bar chart。PR 在 joint 中下降，ISR improvement ratio 也压缩。"
    analysis: >-
      Joint training 在当前模型规模下是 net negative for per-task performance。
      但这并非 STA 协议的失败——ISR signal 在 joint 中仍有效。
      论文中应作为 scale limitation 讨论，指向 plan011 (8B model) 作为
      capacity-sufficient 的 future work。对 Claim 3 影响有限：
      STA protocol 泛化性已由 single-logic Prolog 实验证明，
      joint training 是 additional evidence 非核心证据。

  ##############################################################################
  # 10. plan008 — Cross-logic transfer evaluation
  ##############################################################################
  - name: "Cross-logic transfer evaluation"
    plan_id: "plan008"
    description: >-
      FOL-trained model 在 Prolog tasks 上评估，反之亦然。
      测试 formalization 能力的跨逻辑迁移。
    expected_results:
      fol_to_prolog_pr: 0.32
      fol_to_prolog_isr: 0.04
      prolog_to_fol_pr: 0.28
      prolog_to_fol_isr: 0.03
      fol_on_fol_pr_ref: 0.93
      prolog_on_prolog_pr_ref: 0.84
      transfer_ratio_fol_to_prolog: 0.38
      transfer_ratio_prolog_to_fol: 0.30
    result_rationale: >-
      跨逻辑 transfer 有限 (PR 降至 28-32%)，因为 FOL 和 Prolog 的语法
      结构本质不同：FOL 使用量词/连接词/谓词逻辑，Prolog 使用 Horn clauses/
      unification/backtracking。GRPO 训练针对特定逻辑语法优化 token 序列
      生成策略，这些策略不跨语法迁移。
      然而 30% 的 transfer ratio 高于 random baseline (~12%)，说明
      formalization 的高层语义理解（如何从自然语言提取逻辑结构）有部分共享。
      ISR 在 transfer 场景极低 (0.03-0.04)，表明迁移产生的 formalizations
      即使碰巧 proved 也是结构退化的——模型在不熟悉的逻辑中走更多捷径。
    tables:
      - |
        | Source → Target | PR | ISR | vs in-domain PR |
        |----------------|-----|-----|-----------------|
        | FOL → Prolog | 0.32 | 0.04 | 38% of Prolog in-domain |
        | Prolog → FOL | 0.28 | 0.03 | 30% of FOL in-domain |
        | FOL → FOL (ref) | 0.93 | 0.12 | 100% |
        | Prolog → Prolog (ref) | 0.84 | 0.09 | 100% |
    figures_description:
      - "Fig: Transfer matrix heatmap (2×2)，对角线高 (in-domain)，off-diagonal 低 (cross-logic)。"
    analysis: >-
      Cross-logic transfer 的有限性是预期结果，不影响 STA 论文的核心 claims。
      反而支持论点：STA 协议需要 per-logic instantiation (rule ablation for Prolog,
      component ablation for FOL)，不能依赖 model-level transfer 替代。
      论文应在 Discussion 中简短提及。

  ##############################################################################
  # 11. plan009 — SFT baseline
  ##############################################################################
  - name: "SFT baseline comparison"
    plan_id: "plan009"
    description: >-
      Supervised finetuning on FOLIO 500，与 GRPO variants 对比。
      测试 SFT 是否也出现结构退化。
    expected_results:
      sft_eval_pr: 0.48
      sft_eval_mean_isr: 0.24
      sft_eval_proved_only_isr: 0.50
      sft_eval_component_count_mean: 5.6
      sft_eval_genuine_rate: 0.38
      sft_eval_hacking_rate: 0.62
      sft_vs_grpo_exec_pr: -0.45
      sft_vs_grpo_b01_isr: -0.10
    result_rationale: >-
      SFT 复制训练分布而非优化 reward，因此不经历 GRPO 的饱和→hacking 动态。
      PR 较低 (0.48 vs GRPO 0.93) 因为 SFT 无法通过 trial-and-error 发现
      有效但不在训练集中的证明策略。但 proved-only ISR 较高 (0.50 vs 0.13)
      因为 SFT 保留了训练数据中的结构模式。
      Genuine rate 0.38 (vs GRPO exec-only ~0.18) 表明 SFT 的 hacking 更少，
      但这是以 PR 天花板为代价的——SFT 不 hack 因为它不 optimize。
      这支持论文的核心论点：reward hacking 是优化产物，诊断工具
      (如 ISR) 在 RL 设置中比 SFT 更需要。
    tables:
      - |
        | Method | eval PR | eval ISR | proved-only ISR | genuine % | hacking % |
        |--------|---------|----------|-----------------|-----------|-----------|
        | SFT | 0.48 | 0.24 | 0.50 | 38% | 62% |
        | GRPO exec-only (s42) | 0.93 | 0.12 | 0.13 | ~18% | ~82% |
        | GRPO ISR β=0.1 (s42) | 0.81 | 0.34 | 0.42 | 26% | 74% |
        | Pretrained (ref) | 0.12 | 0.06 | 0.64 | ~50% | ~50% |
    figures_description:
      - "Fig: PR-ISR scatter 四象限图：SFT (中 PR, 中 ISR), GRPO exec (高 PR, 低 ISR), GRPO ISR β=0.1 (高 PR, 高 ISR), pretrained (低 PR, 高 proved-only ISR)。GRPO ISR β=0.1 是唯一占据右上象限的条件。"
    analysis: >-
      SFT 是重要对照：它展示了无 RL 优化压力时的 baseline 结构质量。
      SFT 的 proved-only ISR (0.50) 接近 pretrained (0.64)，确认
      structural degeneration 是 RL 优化的副产物。GRPO ISR β=0.1 是
      唯一同时保持 high PR 和 reasonable ISR 的条件——比 SFT 高 PR
      (0.81 vs 0.48) 且 ISR 相当 (0.34 vs 0.24)，是最佳 PR-ISR tradeoff。

  ##############################################################################
  # 12. plan010 — SMT-LIB (third logic type)
  ##############################################################################
  - name: "SMT-LIB single-logic GRPO (third logic)"
    plan_id: "plan010"
    description: >-
      SMT-LIB 单逻辑 GRPO，exec-only vs exec+STA，500 步。
      第三种逻辑类型验证 STA 协议泛化性。
    expected_results:
      exec_only_pr: 0.72
      exec_only_isr: 0.09
      exec_only_component_count_mean: 8.1
      exec_sta_b01_pr: 0.67
      exec_sta_b01_isr: 0.24
      exec_sta_b01_component_count_mean: 5.4
      isr_improvement_ratio: 2.67
      hacking_modes_shared_with_fol: 3
      hacking_modes_shared_with_prolog: 3
    result_rationale: >-
      SMT-LIB 使用 Z3 solver，constraint satisfaction 语义与 FOL/Prolog
      不同（声明式约束而非推导式证明），但 binary execution reward 的动态
      相同。Exec-only 出现 hacking (PR 0.72, ISR 0.09)，ISR β=0.1 改善
      至 0.24 (2.67x)。SMT-LIB 的 hacking 主要表现为 over-constrained
      assertions（添加冗余约束使 sat/unsat 结果不变）和 trivial assertions
      （直接 assert 结论）。与 FOL/Prolog 共享 conclusion embedding、
      redundancy、tautological 三种模式。
      ISR improvement ratio (2.67x) 略低于 FOL/Prolog 的 3x，可能因为
      SMT-LIB 的 constraint structure 比 FOL premise structure 更刚性，
      ISR 信号的 reward shaping 空间更小。
    tables:
      - |
        | Condition | SMT-LIB PR | SMT-LIB ISR | comp_mean |
        |-----------|-----------|-------------|-----------|
        | exec-only | 0.72 | 0.09 | 8.1 |
        | exec+STA β=0.1 | 0.67 | 0.24 | 5.4 |
        | ISR improvement | — | 2.67x | 0.67x |
    figures_description:
      - "Fig: 三逻辑 ISR improvement radar chart (FOL 2.96x, Prolog 2.99x, SMT-LIB 2.67x)。三种逻辑的改善幅度在 2.5-3.0x 区间内。"
    analysis: >-
      第三种逻辑进一步巩固 Claim 3。三逻辑 ISR improvement 在 2.67-2.99x
      区间的一致性表明 STA 的 LOO ablation 原则是 solver-agnostic 的——
      只要 solver 接受结构化输入且 reward 是二值的，STA 就适用。
      若 SMT-LIB 实验在 submission 前完成，从两逻辑升级为三逻辑将
      显著增强泛化性 claim。否则作为 appendix 或 camera-ready 追加。

  ##############################################################################
  # 13. plan011 — Qwen3-8B scaling
  ##############################################################################
  - name: "Qwen3-8B model scale effect"
    plan_id: "plan011"
    description: >-
      Qwen3-8B (vs 0.5B baseline) 上运行 exec-only + exec+STA GRPO。
      测试模型规模对 reward hacking 和 ISR 诊断的影响。
    expected_results:
      exec_only_pr: 0.96
      exec_only_isr: 0.19
      exec_only_component_count_mean: 6.2
      exec_only_hacking_rate: 0.68
      exec_sta_b01_pr: 0.92
      exec_sta_b01_isr: 0.42
      exec_sta_b01_genuine_rate: 0.35
      pr_retention: 0.958
    result_rationale: >-
      8B 模型有更大的 representation capacity，能在不完全牺牲结构的情况下
      实现高 PR。因此 exec-only ISR (0.19) 高于 0.5B (0.12)——更大模型
      保留更多 "附带" 的结构信息。但 hacking 仍存在 (68%)，说明
      reward hacking 不纯粹是 capacity 问题，而是 optimization objective
      问题。ISR β=0.1 在 8B 上效果更显著 (ISR 0.42 vs 0.5B 的 0.34)，
      因为更大模型有更多容量来同时优化 PR 和结构质量。
      PR retention (0.92/0.96 = 95.8%) 优于 0.5B (0.81/0.93 = 87.1%)，
      说明在 sufficient capacity 下 ISR 信号的 PR cost 接近零。
    tables:
      - |
        | Scale | Condition | PR | ISR | genuine % | hacking % |
        |-------|-----------|-----|-----|-----------|-----------|
        | 0.5B | exec-only | 0.93 | 0.12 | ~18% | ~82% |
        | 0.5B | ISR β=0.1 | 0.81 | 0.34 | 26% | 74% |
        | 8B | exec-only | 0.96 | 0.19 | ~32% | ~68% |
        | 8B | ISR β=0.1 | 0.92 | 0.42 | 35% | 65% |
    figures_description:
      - "Fig: Scale × condition interaction plot (2×2)。8B 在两种条件下均优于 0.5B，但 ISR β=0.1 的改善幅度在两种规模上一致 (ISR ratio ≈ 2.2x)。"
    analysis: >-
      Scaling 降低 hacking rate (82%→68% exec-only) 但不消除它。
      这是重要发现：即使 frontier-scale 模型也需要 ISR 诊断。
      ISR β=0.1 在更大模型上的 diminishing Goodhart risk (PR retention
      95.8% vs 87.1%) 暗示 sweet spot 可能随模型规模右移，
      未来工作可探索 larger β at larger scale。

  ##############################################################################
  # 14. plan015 — Curriculum ablation
  ##############################################################################
  - name: "Curriculum ablation (sigmoid vs linear vs fixed)"
    plan_id: "plan015"
    description: >-
      测试 ISR reward 的 curriculum scheduling：sigmoid ramp (baseline)
      vs linear ramp vs fixed weight。Sigmoid 是 plan005 的最佳配置
      但未做消融。
    expected_results:
      sigmoid_eval_pr: 0.77
      sigmoid_eval_isr: 0.23
      sigmoid_midpoint_step: 200
      linear_eval_pr: 0.73
      linear_eval_isr: 0.19
      fixed_b01_eval_pr: 0.81
      fixed_b01_eval_isr: 0.34
      fixed_b03_eval_pr: 0.18
      fixed_b03_eval_isr: 0.03
      sigmoid_vs_linear_isr_delta: 0.04
      linear_midpoint100_pr: 0.70
      linear_midpoint300_pr: 0.75
    result_rationale: >-
      注意：plan005 使用凸组合公式 (α·r_exec + β·r_exec·ISR, α+β=1)，
      而 plan002-b01 使用乘法公式 (r = r_exec·(1+β·ISR))。plan015 需要
      在两种公式下分别测试 curriculum。
      Fixed β=0.1 (plan002-b01 已验证) 是最佳 fixed 配置。Sigmoid 和 linear
      ramp 在凸组合公式下有效果，因为 early ISR penalty (ISR<1 时) 需要
      逐步引入以避免早期训练崩塌。但在乘法公式下，ISR 只能 bonus，
      curriculum 的意义降低——fixed β=0.1 已经是 "permanently gentle bonus"，
      不需要 ramp。
      Sigmoid 略优于 linear (ISR 0.23 vs 0.19) 因为 sigmoid 的 S-curve
      在中期 (step 150-250) 快速提升 ISR weight，比 linear 的匀速增长
      更好地利用了模型已学到基础证明能力的时间窗口。
      Midpoint 影响：100 (过早) 导致 early ISR pressure → PR 降；
      300 (过晚) 使 ISR signal 在后 200 步才充分生效，改善有限。
    tables:
      - |
        | Curriculum | Formula | eval PR | eval ISR | optimal midpoint |
        |-----------|---------|---------|----------|------------------|
        | Fixed β=0.1 | multiplicative | **0.81** | **0.34** | N/A |
        | Sigmoid (midpoint=200) | convex | 0.77 | 0.23 | 200 |
        | Linear (midpoint=200) | convex | 0.73 | 0.19 | 200 |
        | Fixed β=0.3 | multiplicative | 0.18 | 0.03 | N/A (Goodhart) |
      - |
        | Linear midpoint | eval PR | eval ISR |
        |----------------|---------|----------|
        | 100 | 0.70 | 0.17 |
        | 200 | 0.73 | 0.19 |
        | 300 | 0.75 | 0.15 |
    figures_description:
      - "Fig: Curriculum schedule curves (sigmoid vs linear vs fixed) overlaid with training ISR trajectory。Fixed β=0.1 multiplicative 的 ISR 增长最稳定。"
    analysis: >-
      关键发现：在乘法公式 r = r_exec·(1+β·ISR) 下，curriculum scheduling
      的边际价值很小——fixed β=0.1 已经是最优。这是因为乘法公式中 ISR 只能
      是 bonus (≥0)，不存在 early penalty 问题。Sigmoid curriculum 主要
      对凸组合公式有价值（避免 ISR<1 时的 penalty 效应）。
      论文应在 ablation 中简短报告此结果，结论：乘法公式 + fixed β=0.1
      是最简洁有效的配置，无需 curriculum 复杂化。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8d0562e-babe-4fb9-aa76-fe883a3371a2",
  "isSidechain": false,
  "requestId": "req_011Cb2DuCAJTqTZ35wmTAJx1",
  "type": "assistant",
  "uuid": "44f5ef7d-1c43-4f8f-b4ae-867e7ed13e3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "c4fab40b-373c-4126-bf88-54847afda167",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LZEEQnZMKvvkDxmJ2X7w5y",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21942,
      "cache_read_input_tokens": 11841,
      "output_tokens": 31916,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21942,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 31916,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21942
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：β=0.1 ISR sweet spot 跨 3 seed 复现且效应量稳健；Prolog 实验成功复现 hacking + ISR 诊断。三条 claim 全部成立。 核心假设：['plan002-b01 s43/s44 复现 s42 方向：ISR β=0.1 >> random β=0.1，PR 维持',…",
  "leafUuid": "44f5ef7d-1c43-4f8f-b4ae-867e7ed13e3a",
  "sessionId": "c4fab40b-373c-4126-bf88-54847afda167"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "ISR sweet spot and Goodhart boundary validation across 3 seeds",
  "sessionId": "c4fab40b-373c-4126-bf88-54847afda167"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：β=0.1 ISR sweet spot 跨 3 seed 复现且效应量稳健；Prolog 实验成功复现 hacking + ISR 诊断。三条 claim 全部成立。 核心假设：['plan002-b01 s43/s44 复现 s42 方向：ISR β=0.1 >> random β=0.1，PR 维持',…",
  "leafUuid": "44f5ef7d-1c43-4f8f-b4ae-867e7ed13e3a",
  "sessionId": "c4fab40b-373c-4126-bf88-54847afda167"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "ISR sweet spot and Goodhart boundary validation across 3 seeds",
  "sessionId": "c4fab40b-373c-4126-bf88-54847afda167"
}
```

---
