# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/31e665a0-dae3-4463-8403-346ff6c49913.jsonl`
- **Structured JSON:** [`260dcb536b03ab7352af.json`](../../sessions/26/260dcb536b03ab7352af.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T09:25:52.821Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T09:25:52.821Z",
  "sessionId": "31e665a0-dae3-4463-8403-346ff6c49913",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: solver-trace-ablation\n\n## paper_framing.md\n\n# Paper Framing — solver-trace-ablation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\n\n### Claim 1: ISR as Reward Hacking Diagnostic\nSolver Trace Ablation (STA) derives ISR (Intensional Structural Reward) via component necessity testing (leave-one-out ablation on solver inputs). ISR detects reward hacking that prove_rate alone misses: exec-only GRPO achieves PR=93% but ISR collapses from 0.6423 (100 steps) to 0.1324 (500 steps) to 0.0027 (1000 steps), quantifying structural degeneration invisible to the execution reward.\n\n**证据**：\n- plan003: 100-step checkpoint held-out eval PR=32%, ISR=0.6423 (proved-only) — early training produces structurally sound formalizations\n- plan001-s42: 500-step checkpoint held-out eval PR=93%, ISR=0.1324, median_ISR=0.0 — late training achieves high prove_rate via structural shortcuts\n- **plan016**: 1000-step checkpoint eval PR=96%, ISR=**0.0027** — ISR 崩塌持续恶化，无回升。94.8% proved 样本 ISR=0。矛盾爆炸式崩塌（components 6.58→18.55）。延长训练是 reward hacking 随时间恶化的干净消融证据\n- ISR 崩塌轨迹完整链：0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步)\n- 3-seed consistency: s42 conclusion embedding (ISR=0.123), s43 repetition collapse (PR=13%, ISR=0), s44 tautological collapse (PR=98%, ISR=0.57 fake-high, n_comp=2.04)\n- Hacking taxonomy: 5 distinct modes identified and quantified (plan012 `hacking_characterization_report.md` + plan017 D027)\n\n### Claim 2: ISR as Proxy Metric Exhibits Goodhart's Law (D033 重写)\nISR 作为 proxy metric 遵循 Goodhart's Law：当 ISR 从观测指标（diagnostic）转变为优化目标（reward），其有效性取决于优化压力的强度。低剂量 ISR reward (β=0.1) 提升结构质量且不损害证明能力；高剂量 ISR reward (β=0.3) 触发 Goodhart 效应，比 matched random noise 更差。\n\n**证据（β=0.1 同剂量对照，D031 定论）**：\n- plan002-b01 (ISR β=0.1): eval PR=0.81, ISR=0.337, proved_only_ISR=0.415, components=5.58 — genuine proofs with improved structure\n- plan018 (random β=0.1): eval PR=0.79, ISR=0.104, proved_only_ISR=0.131, components=8.46 — PR 持平但 ISR 仅为 ISR 组的 1/3.2\n- **结论**：ISR 3.2x > random at same β → ISR 信号提供 genuine structural guidance，非 variance regularization\n\n**Hacking Taxonomy 定量对比 (D038)**：\n- ISR β=0.1 genuine: 25.9% (21/81) vs random β=0.1 genuine: 17.7% (14/79) — **+8.2pp**\n- Conclusion embedding: ISR 72.8% vs random 78.5% — 两组主导模式，ISR 略降但未消除\n- Complexity-without-utility: ISR **0%** vs random 3.8% — ISR 完全消除此模式\n- ISR genuine quality: mean ISR 0.67 (max 1.0) vs random genuine mean ISR 0.34 (max 0.5)\n- 整体 hacking rate: ISR 74.1% vs random 82.3% — sweet spot 下仍有 74% hacking\n\n**证据（β=0.3 同剂量对照）**：\n- plan002-b03 (ISR β=0.3): eval PR=0.18, ISR=0.026 — Goodhart 效应，PR 崩塌\n- plan017 (random β=0.3): eval PR=0.48, ISR=0.045 — random 比 ISR 好 2.7x PR\n- **结论**：高剂量 ISR 对训练 actively misleading (PR 18% < random 48%)\n\n**β 剂量效应全景**：\n| β | ISR reward PR | Random reward PR | ISR reward ISR | Random reward ISR | 解读 |\n|---|---|---|---|---|---|\n| 0.1 | 0.81 | 0.79 | **0.337** | 0.104 | ISR >> random (sweet spot) |\n| 0.3 | 0.18 | 0.48 | 0.026 | 0.045 | ISR << random (Goodhart) |\n\n**其他 ISR-as-reward 失败模式**：\n- plan005 凸组合 (α·r_exec + β·r_exec·ISR, α+β=1): ISR<1 时永远是 penalty → PR 下降 (D010)\n- plan013 convex random: PR=1.0 但 100% P→P tautological collapse (D018)\n\n⚠️ **措辞约束 (Reviewer D027)**: plan013 (0.9·r_exec+0.1·random) vs plan017 (r_exec·(1+0.3·random)) 公式结构不同，不可简化为\"additive vs convex\"对照。plan017 vs plan002 和 plan018 vs plan002-b01 的 ISR vs random 对比是纯净的（唯一变量是 random vs ISR）\n\n⚠️ **β=0.1 ISR 目前 1 seed (s42)，s43/s44 训练中**。3-seed mean±std 待出。\n\n### Claim 3: Cross-Logic Generality (conditional on plan006)\nSTA protocol is solver-agnostic: the 5-step derivation (pilot → collect shortcuts → classify → map RIP → design check) transfers to structurally different formal languages. Hacking modes and ISR diagnostic value replicate across FOL→Prover9 and Prolog→SWI-Prolog.\n\n**证据**: 待验证。plan006 Prolog GRPO dry-run 进行中，训练即将启动（3 seeds × 500 步）。如果 plan006 无法复现 hacking + ISR 诊断，此 claim 降级为 future work。\n\n## Story Spine\n\n- **Problem**: GRPO with execution-only rewards trains neurosymbolic formalizers that achieve high solve rates but produce structurally degenerate outputs (reward hacking). Current practice evaluates only prove_rate, missing structural quality entirely. No principled diagnostic exists for detecting and characterizing this failure mode.\n- **Existing approaches & gaps**: Mellgren et al. (2025) hand-craft Prolog-specific structure penalties. EVOM (2026) uses scalar execution rewards only. ExecVerify/EGCA derive trace-level rewards for code, not formal logic. No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools for it.\n- **Our contribution**: We propose STA (Solver Trace Ablation), applying component necessity testing (LOO ablation) to derive ISR as a **diagnostic metric** for structural integrity. Key findings:\n  1. ISR quantifies hacking invisible to prove_rate (64% → 13% → 0.3% collapse over training)\n  2. ISR as proxy metric exhibits Goodhart's Law: low-dose ISR reward (β=0.1) provides genuine structural guidance (3.2x > matched random), but high-dose (β=0.3) is actively worse than random noise — a clean empirical demonstration of Goodhart's Law in reward shaping\n  3. GRPO saturation creates a \"training trap\": PR→1 means no gradient signal; adding variance redirects rather than prevents hacking\n  4. Different reward formulations produce distinct, classifiable hacking strategies (5 modes identified)\n  5. ISR measures syntactic component necessity, not semantic faithfulness — this boundary is important for practitioners\n- **Actionable insights for practitioners**:\n  1. Never trust prove_rate alone — use ISR + component count as joint diagnostic\n  2. Single-seed GRPO results are unreliable (2/3 exec-only seeds collapse differently)\n  3. ISR reward has a narrow sweet spot (β=0.1): below it, no structural guidance; above it, Goodhart effect destroys prove_rate\n  4. ISR is primarily a structural diagnostic; as training signal, treat with extreme caution (Goodhart boundary is sharp)\n- **Headline result**: \"We demonstrate that ISR — a component necessity metric derived from solver trace ablation — serves as both a diagnostic for reward hacking in GRPO-trained formalizers and a case study of Goodhart's Law in reward shaping. At low dose (β=0.1), ISR reward provides genuine structural guidance (3.2x ISR improvement over matched random control, PR maintained). At high dose (β=0.3), ISR reward is actively worse than random noise (PR 18% vs 48%), exhibiting classic Goodhart collapse. Across 5 reward conditions, 3 seeds, and up to 1000 training steps, we identify 5 distinct hacking strategies and document ISR's transition from useful indicator to harmful optimization target.\"\n\n## ISR Capability Boundary (D021/D022)\n\n**ISR 度量的是 syntactic necessity（组件在证明中是否必要），不是 semantic faithfulness（formalization 是否忠实于自然语言语义）。**\n\nplan014 downstream NLI 验证结果（negative）精确刻画了这一边界：\n- Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, 不显著)\n- Best-of-N ISR selection vs random: +0.9pp (不显著)\n- 主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%\n\n**论文处理**：ISR-as-downstream-quality-proxy 降级为 **Limitation / Future Work**。plan014 结果作为 negative result 保留，精确刻画 ISR 能力边界。\n\n## ISR-as-Reward: Goodhart Landscape (D033 更新)\n\nISR 作为训练信号的全部结果，按 β 剂量组织：\n\n| 条件 | 公式 | eval PR | eval ISR | 退化模式 | Goodhart 阶段 |\n|------|------|---------|----------|----------|---------------|\n| exec-only (baseline) | r = r_exec | 0.93 (s42) | 0.123 | conclusion embedding | N/A |\n| ISR β=0.1 | r = r_exec·(1+0.1·ISR) | **0.81** | **0.337** | conclusion embedding (73%), genuine 26% | pre-Goodhart (sweet spot) |\n| random β=0.1 | r = r_exec·(1+0.1·random) | 0.79 | 0.104 | redundant premises | control |\n| ISR β=0.3 | r = r_exec·(1+0.3·ISR) | 0.18 | 0.026 | format collapse | post-Goodhart |\n| random β=0.3 | r = r_exec·(1+0.3·random) | 0.48 | 0.045 | complexity-without-utility | control |\n| convex combination | r = 0.9·r_exec + 0.1·ISR | 0.77 (train) | 0.230 (train) | ISR-PR separation | penalty effect |\n| convex random | r = 0.9·r_exec + 0.1·random | 1.00 | 0.535 (fake) | tautological | hacking |\n\n**Goodhart 转折点在 β ∈ (0.1, 0.3)。** β=0.1 是可用的 sweet spot；β=0.3 已进入 Goodhart 区间。\n\n## Venue Fit Risks\n\n- **EMNLP fit**: Diagnostic/analysis paper with Goodhart's Law case study in NLP + formal reasoning track. Empirical findings + mechanistic insight valued at EMNLP.\n- **\"Just negative results\" risk**: Mitigate by: (a) β=0.1 是 positive result (ISR sweet spot)，(b) Goodhart framework 提供 mechanistic understanding，(c) actionable diagnostic framework (ISR + taxonomy)。\n- **\"Old wine\" risk**: ISR = LOO ablation. Claim novelty at application level (first systematic Goodhart analysis for formal reasoning GRPO) + empirical findings, not algorithm level.\n- **Single-logic risk**: If plan006 Prolog doesn't happen, paper is FOL-only. Mitigate by emphasizing depth of analysis (3 seeds × 5+ conditions × 5 hacking modes × 3 training horizons).\n\n## Anticipated Reviewer Concerns\n\n1. **\"ISR is just LOO ablation — not novel\"** — Yes, explicitly acknowledge. Contribution is (a) applying it as hacking diagnostic for formal reasoning GRPO, (b) empirical Goodhart analysis on reward shaping, (c) hacking taxonomy, (d) GRPO saturation mechanism.\n2. **\"β=0.1 success is just one seed\"** — Acknowledged. Future work includes multi-seed β=0.1 validation. However, the β=0.1 vs random β=0.1 comparison is clean (same seed, same setup, only ISR vs random differs).\n3. **\"Goodhart's Law is obvious\"** — The conceptual prediction is known; the empirical characterization in formal reasoning GRPO is not. Specifically: (a) the sharp threshold between β=0.1 and β=0.3, (b) ISR being worse than random at high β (not just \"less useful\"), (c) 5 distinct hacking modes as Goodhart manifestations.\n4. **\"No positive result — ISR doesn't improve training\"** — β=0.1 IS a positive result (PR=0.81, ISR 3.2x > random). Framing: ISR has a narrow but real sweet spot. The Goodhart boundary is the key insight.\n5. **\"ISR is circular\"** — ISR is used for diagnosis/post-hoc analysis AND as reward (β=0.1). The circularity concern applies to high-β optimization; low-β avoids Goodhart precisely because optimization pressure is weak. Component count analysis provides ISR-independent evidence.\n6. **\"Only one logic type\"** — STA protocol is solver-agnostic; plan006 Prolog validates generality. If absent, acknowledge as limitation.\n7. **\"500 steps too short\"** — plan016 extends to 1000 steps, showing ISR collapse continues and worsens (0.123→0.003, -97.8%). The ISR崩塌轨迹 covers 100/500/1000 steps.\n8. **\"3 seeds insufficient for statistical claims\"** — The 3-seed divergence (3 different hacking modes from same setup) is itself a finding, not a limitation. Statistical claims on mean ISR use 3-seed mean±std.\n9. **\"Related work insufficient\"** — Expand to 25+ refs: reward hacking (Gao 2023, Skalse 2022), Goodhart's Law (Manheim & Garrabrant 2019, Karwowski 2024), GRPO (Shao 2024), formal reasoning (LeanDojo, Baldur), feature attribution (SHAP), FOLIO (Han 2022).\n10. **\"RIP framework overstated\"** — Frame as \"component necessity testing inspired by mutation testing's RIP framework,\" only Propagation condition operationalized.\n11. **\"Practitioners can't act on this\"** — 4 actionable insights listed in Story Spine. ISR + component count as joint diagnostic is immediately deployable. β=0.1 sweet spot is directly actionable for reward shaping.\n\n## Dream-Identified Structural Fixes (Paper Agent)\n\n- [ ] Related work: 6→25+ references (literature_map.yaml now has 33)\n- [ ] RIP framing: reframe as \"component necessity testing inspired by RIP\"\n- [ ] \"Dense+automatic\" → \"conditionally dense\"\n- [ ] Remove all \"Pareto-improving\" language\n- [ ] Acknowledge ISR = LOO ablation, cite feature attribution literature\n- [ ] Address ISR sparsity for unproved outputs explicitly\n- [ ] Add Goodhart's Law literature (Manheim & Garrabrant 2019, Karwowski 2024, Gao 2023)\n- [x] Convex combination → additive bonus (D010, then D020 confirmed all ISR-as-reward failed at β=0.3)\n- [x] ISR downstream validation → Limitation/Future Work (D021/D022, plan014 negative)\n- [x] Hacking taxonomy completed (plan012, 5 modes identified including plan017)\n- [x] β=0.1 ISR sweet spot documented (D031/D032, plan002-b01 success)\n- [x] β=0.1 random control confirms ISR structural value (D033, plan018 eval)\n- [x] 1000-step ISR collapse documented (plan016, ISR 0.123→0.003)\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: FOL single-logic GRPO, execution-only reward (500 steps, K=8, 3 seeds)\n    — baseline for STA comparison\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: plan001-exec-only-s43-r4\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_sampling_prove_rate: 0.14\n    eval_sampling_mean_isr: 0\n    eval_sampling_n_proved: 14\n    eval_sampling_temperature: 0.7\n    eval_sampling_method: do_sample=True, temperature=0.7\n    eval_sampling_by_answer:\n      'true':\n        count: 34\n        proved: 6\n        prove_rate: 0.176\n      'false':\n        count: 25\n        proved: 2\n        prove_rate: 0.08\n      unknown:\n        count: 41\n        proved: 6\n        prove_rate: 0.146\n- id: plan_002\n  claim: 2\n  description: 'FOL single-logic GRPO, additive ISR bonus: r = r_exec · (1 + β·ISR),\n    β∈{0.1, 0.3, 0.5}. 先跑 β=0.3 单 seed 验证方向，成功再 3-seed。旧凸组合公式 (α·r_exec + β·r_exec·ISR,\n    α+β=1) 已废弃——ISR<1 时永远是 penalty (plan005 confirmed)。 新公式确保 ISR 只能 bonus 不能 penalty。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: plan002-additive-b03-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 56.7\n    overall_prove_rate: 0.34025\n    overall_isr: 0.11527\n    first20_prove_rate: 0.15625\n    last50_prove_rate: 0.555\n    last100_prove_rate: 0.5525\n    mean_loss: 0.008914\n    last100_loss: 0.014469\n    parse_rate: 1\n    w1_50_prove_rate: 0.13\n    w51_100_prove_rate: 0.095\n    w101_200_prove_rate: 0.185\n    w201_300_prove_rate: 0.375\n    w301_400_prove_rate: 0.47625\n    w401_500_prove_rate: 0.5525\n    steps_ge_085: 52\n    first_step_ge_085: 46\n    final_prove_rate: 1\n    final_isr_mean: 0.3089\n    final_reward_mean: 1.0927\n- id: plan_003\n  claim: 1\n  description: 'FOL held-out evaluation: compare plan_001 vs plan_002 checkpoints\n    on test set using identical full STA metrics (prove_rate, ISR, ISR/PR ratio, hacking\n    taxonomy annotation)'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_002\n  registry_id: plan003-eval-exec-only-r5\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.32\n    mean_isr: 0.2055\n    isr_std: 0.3194\n    proved_only_isr: 0.6423\n    isr_by_type:\n      'true': 0.3598\n      'false': 0.1723\n      unknown: 0.0979\n    total_samples: 100\n    proved_count: 32\n    runtime_s: 251.7\n- id: plan_004\n  claim: 1\n  description: 'STA O(1) vs O(N) ablation: rerun exec+STA with fast_isr_fol to confirm\n    O(1) ineffectiveness at scale (500 steps, 1 seed) — negative result documentation'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n- id: plan_005\n  claim: 1\n  description: 'STA reward weight ablation: test α/β ratios (0.3/0.7, 0.5/0.5, 0.7/0.3)\n    + sigmoid curriculum vs fixed — isolate optimal STA integration'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: plan005-sta-low-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 71\n    parse_rate: 1\n    overall_prove_rate: 0.5657\n    overall_isr: 0.1682\n    last50_prove_rate: 0.77\n    last50_isr: 0.2559\n    last100_prove_rate: 0.7725\n    last100_isr: 0.2299\n    last100_loss: 0.022752\n    overall_loss: 0.017296\n    last100_isr_pr_ratio: 0.298\n    last100_isr_lt_pr_count: 99/100\n    first_rolling10_pr_ge_0.8: 178\n    first_rolling10_pr_ge_0.9: 439\n    max_rolling10_pr: 0.9375\n    max_rolling10_isr: 0.3282\n    windowed:\n      1-50:\n        pr: 0.1775\n        isr: 0.0906\n      51-100:\n        pr: 0.1775\n        isr: 0.0835\n      101-200:\n        pr: 0.5062\n        isr: 0.1463\n      201-300:\n        pr: 0.6713\n        isr: 0.1791\n      301-400:\n        pr: 0.7013\n        isr: 0.1984\n      401-500:\n        pr: 0.7725\n        isr: 0.2299\n- id: plan_006\n  claim: 3\n  description: 'Prolog single-logic GRPO: exec-only vs exec+STA (500 steps, K=8, 3\n    seeds) — second logic type validation. Dream M3: must have 3 seeds for cross-logic\n    claim.'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  notes: Requires Prolog STA instantiation (rule ablation). SWI-Prolog already installed.\n    Upgraded from 1→3 seeds per Dream feedback.\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Multi-logic GRPO (FOL+Prolog): exec-only vs exec+STA (500 steps, K=8,\n    1 seed) — cross-logic transfer test'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - plan_006\n  status: planned\n- id: plan_008\n  claim: 3\n  description: 'Cross-logic transfer evaluation: FOL-trained model on Prolog tasks\n    and vice versa'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_006\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'SFT baseline: supervised finetuning on same data (FOLIO 500), compare\n    with GRPO variants'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n- id: plan_010\n  claim: 3\n  description: 'SMT-LIB single-logic GRPO: exec-only vs exec+STA — third logic type'\n  priority: P2\n  gpu_budget_hours: 3\n  deps: []\n  notes: Requires SMT-LIB STA instantiation (constraint ablation). Z3 already installed.\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Qwen3-8B scaling: full MLSR on 8B model (1 seed) — model scale effect'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - plan_005\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Hacking characterization: manual annotation of 200 outputs per condition,\n    categorized by extensional-shortcut taxonomy'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n- id: plan_013\n  claim: 2\n  description: 'Random reward baseline: replace ISR with random structural penalty\n    on proved outputs (r = α·r_exec + β·r_exec·random[0,1]) to isolate ISR-specific\n    signal from multi-objective regularization effect. Dream M2/W7 mandatory.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'Dream cross-tier consensus: without this, cannot claim ISR formulation matters\n    vs any penalty.'\n  registry_id: plan013-random-reward-s42-r4\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 1\n    eval_mean_isr: 0.535\n    eval_isr_std: 0.1282\n    eval_proved_only_isr: 0.535\n    eval_median_isr: 0.5\n    eval_n_proved: 100\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_note: 'DEGENERATE: model generates trivial 2-component proofs (premise=conclusion,\n      conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure'\n- id: plan_014\n  claim: 1\n  description: 'Downstream validation: evaluate high-ISR vs low-ISR formalizations\n    on independent logical inference task (e.g., entailment accuracy using generated\n    FOL as premises). Breaks ISR circularity. Dream M2/W4 mandatory.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Dream cross-tier consensus: optimizing ISR + evaluating ISR = circular.\n    Need external criterion.'\n  registry_id: plan014-downstream-nli-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 0.341\n    proved_rate: 0.915\n    proved_count: 732\n    total_generations: 800\n    parse_errors: 0\n    accuracy_by_label:\n      'true': 0.912\n      'false': 0\n      unknown: 0.076\n    spearman_rho: -0.049\n    spearman_p: 0.187\n    mann_whitney_U: 17202\n    mann_whitney_p: 0.288\n    bon_isr_accuracy: 0.35\n    bon_random_accuracy: 0.341\n    bon_oracle_accuracy: 0.44\n    bon_prove_first_accuracy: 0.35\n    isr_bucket_high_acc: 0.75\n    isr_bucket_mid_acc: 0.377\n    isr_bucket_low_acc: 0.327\n    runtime_inference_s: 408.8\n    runtime_eval_s: 13.6\n- id: plan_015\n  claim: 1\n  description: 'Curriculum ablation: linear ramp vs sigmoid vs fixed weighting. Sigmoid\n    is load-bearing (best config) but not ablated. Dream m4.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_005\n  notes: Test linear ramp with same midpoint as sigmoid. Also vary midpoint (step\n    100/200/300 of 500).\n  status: planned\n- id: plan_016\n  claim: 1\n  description: 'Extended training horizon: run best config (from plan_005) to 1000+\n    steps to show convergence or persistence of STA benefit. Dream m6/W9.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - plan_005\n  notes: Both Dream tiers flag 500 steps as insufficient. Need evidence of convergence.\n  registry_id: plan016-extended-1000-s42\n  status: DONE\n  conclusion: success\n  metrics:\n    train:\n      total_steps: 1000\n      duration_min: 146\n      final_prove_rate: 0.8396\n      final_mean_isr: 0.0503\n      train_loss: 0.0125\n      epoch: 4\n      windowed:\n        steps_001_100:\n          pr: 0.19\n          isr: 0.0859\n        steps_101_200:\n          pr: 0.66\n          isr: 0.1115\n        steps_201_300:\n          pr: 0.838\n          isr: 0.0985\n        steps_301_400:\n          pr: 0.907\n          isr: 0.054\n        steps_401_500:\n          pr: 0.927\n          isr: 0.0433\n        steps_501_600:\n          pr: 0.963\n          isr: 0.0408\n        steps_601_700:\n          pr: 0.965\n          isr: 0.02\n        steps_701_800:\n          pr: 0.988\n          isr: 0.0178\n        steps_801_900:\n          pr: 0.978\n          isr: 0.017\n        steps_901_1000:\n          pr: 0.981\n          isr: 0.0144\n    eval:\n      prove_rate: 0.96\n      n_proved: 96\n      n_problems: 100\n      mean_isr: 0.0027\n      isr_std: 0.0118\n      median_isr: 0\n      proved_only_mean_isr: 0.0028\n      min_isr: 0\n      max_isr: 0.0588\n      isr_0_ratio: 0.9479\n      isr_1_ratio: 0\n      component_count_mean: 18.55\n      component_count_2_ratio: 0\n      mean_n_necessary: 0.052\n      n_necessary_0_ratio: 0.9479\n      tautological_collapse: false\n      by_answer_type:\n        'false':\n          count: 29\n          proved: 26\n          prove_rate: 0.8966\n          mean_isr: 0\n        unknown:\n          count: 31\n          proved: 30\n          prove_rate: 0.9677\n          mean_isr: 0.0053\n        'true':\n          count: 40\n          proved: 40\n          prove_rate: 1\n          mean_isr: 0.0026\n      eval_time_seconds: 396.3\n- id: plan_017\n  claim: 2\n  description: 'Additive random control: r = r_exec · (1 + β·random[0,1]), β=0.3.\n    Matched control for plan_002 — isolates ISR structural signal from pure variance\n    regularization. If ISR > random > exec-only, both signal and regularization contribute.\n    If ISR > random ≈ exec-only, ISR signal is key. If ISR ≈ random, ISR has no value\n    beyond regularization.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'D012: Reviewer-required control for GRPO saturation confound. Must match\n    plan_002 exactly (same β=0.3, same data, same steps) except random replaces ISR.'\n  registry_id: plan017-additive-random-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.48\n    eval_mean_isr: 0.0453\n    eval_isr_std: 0.0759\n    eval_median_isr: 0\n    eval_max_isr: 0.2857\n    eval_proved_only_isr: 0.0943\n    eval_n_proved: 48\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 9.6\n    eval_component_count_2_ratio: 0\n    eval_isr_pr_ratio: 0.0943\n    eval_elapsed_s: 542.3\n    eval_by_type_false_pr: 0.32\n    eval_by_type_false_isr: 0.0254\n    eval_by_type_unknown_pr: 0.51\n    eval_by_type_unknown_isr: 0.0518\n    eval_by_type_true_pr: 0.56\n    eval_by_type_true_isr: 0.052\n    tautological_collapse: false\n- id: plan_018\n  claim: 2\n  description: Additive random control β=0.1, matched to plan002-b01. r = r_exec ·\n    (1 + 0.1·random[0,1]). Same β as plan002-b01 (ISR β=0.1) for fair comparison.\n    If ISR β=0.1 >> random β=0.1 → ISR signal has structural value at low dose. If\n    ISR ≈ random → ISR is just variance regularization even at low dose.\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'D031: Urgent control experiment. plan002-b01 (ISR β=0.1) showed unexpected\n    success (PR=0.81, ISR=0.337). Need matched random control at same β to confirm\n    ISR signal vs noise.'\n  registry_id: plan018-additive-random-b01-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.79\n    eval_mean_isr: 0.1038\n    eval_isr_std: 0.1369\n    eval_median_isr: 0.0357\n    eval_proved_only_isr: 0.1314\n    eval_n_proved: 79\n    eval_n_problems: 100\n    eval_component_count_mean: 8.46\n    eval_component_count_median: 8\n    eval_component_count_2_ratio: 0\n    eval_isr_1_ratio: 0\n    eval_isr_0_ratio: 0.367\n    eval_isr_gt0_ratio: 0.633\n    eval_by_type_false_pr: 0.8\n    eval_by_type_false_isr: 0.1318\n    eval_by_type_unknown_pr: 0.7317\n    eval_by_type_unknown_isr: 0.0944\n    eval_by_type_true_pr: 0.8529\n    eval_by_type_true_isr: 0.0945\n    tautological_collapse: false\n    train_total_steps: 500\n    train_duration_min: 70.5\n    train_last100_pr: 0.805\n    train_last100_isr: 0.1432\n    train_loss: 0.005\n\n\n## registry (completed experiments)\n\n- exp_id: sta-phase0-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_isr: 0.0641\n    isr_std: 0.1983\n    median_isr: 0\n    isr_range:\n    - 0\n    - 0.889\n    prove_rate: 0.12\n    proved_count: 12\n    total_samples: 100\n    xor_affected_samples: 34\n    effective_prove_rate_no_xor: 0.182\n    avg_time_per_sample_s: 3.4\n    total_runtime_s: 336\n    isr_by_answer:\n      'true':\n        n: 34\n        proved: 9\n        prove_rate: 0.265\n        mean_isr: 0.1345\n      'false':\n        n: 25\n        proved: 1\n        prove_rate: 0.04\n        mean_isr: 0.024\n      unknown:\n        n: 41\n        proved: 2\n        prove_rate: 0.049\n        mean_isr: 0.0302\n- exp_id: sta-gt-isr-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gt_prove_rate: 0.18\n    gt_mean_isr: 0.5588\n    gt_isr_std: 0.2582\n    gt_isr_median: 0.6125\n    solver_execution_rate: 1\n    true_prove_rate: 0.5\n    true_mean_isr: 0.5833\n- exp_id: sta-phase1-exec-only\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.15125\n    mean_isr: 0.1475\n    last20_prove_rate: 0.2\n    last20_isr_mean: 0.2\n    first20_reward_mean: 0.119\n    training_steps: 100\n    training_minutes: 15\n- exp_id: sta-phase1-exec-sta-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.1575\n    mean_isr: 0.1525\n    last20_prove_rate: 0.2125\n    last20_isr_mean: 0.2125\n    first20_reward_mean: 0.119\n    training_steps: 100\n    training_minutes: 15\n- exp_id: sta-phase1-exec-only-r5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.15125\n    mean_isr: 0.1475\n    last20_prove_rate: 0.2\n    last20_isr_mean: 0.2\n    first20_prove_rate: 0.11875\n    first20_isr_mean: 0.11875\n    overall_reward_mean: 0.15125\n    last20_reward_mean: 0.2\n    training_steps: 100\n    training_minutes: 15.7\n    step_time_s: 9.44\n    isr_pr_ratio_last20: 1\n    K: 8\n- exp_id: sta-phase1-exec-sta-r5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.1\n    mean_isr: 0.04347\n    last20_prove_rate: 0.15\n    last20_isr_mean: 0.04956\n    first20_prove_rate: 0.08125\n    first20_isr_mean: 0.05182\n    overall_reward_mean: 0.07174\n    last20_reward_mean: 0.09978\n    training_steps: 100\n    training_minutes: 16.9\n    step_time_s: 10.13\n    isr_pr_ratio_overall: 0.43\n    isr_pr_ratio_last20: 0.33\n    K: 8\n- exp_id: plan001-exec-only-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan005-sta-low-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 71\n    parse_rate: 1\n    overall_prove_rate: 0.5657\n    overall_isr: 0.1682\n    last50_prove_rate: 0.77\n    last50_isr: 0.2559\n    last100_prove_rate: 0.7725\n    last100_isr: 0.2299\n    last100_loss: 0.022752\n    overall_loss: 0.017296\n    last100_isr_pr_ratio: 0.298\n    last100_isr_lt_pr_count: 99/100\n    first_rolling10_pr_ge_0.8: 178\n    first_rolling10_pr_ge_0.9: 439\n    max_rolling10_pr: 0.9375\n    max_rolling10_isr: 0.3282\n    windowed:\n      1-50:\n        pr: 0.1775\n        isr: 0.0906\n      51-100:\n        pr: 0.1775\n        isr: 0.0835\n      101-200:\n        pr: 0.5062\n        isr: 0.1463\n      201-300:\n        pr: 0.6713\n        isr: 0.1791\n      301-400:\n        pr: 0.7013\n        isr: 0.1984\n      401-500:\n        pr: 0.7725\n        isr: 0.2299\n- exp_id: plan003-eval-exec-only-r5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.32\n    mean_isr: 0.2055\n    isr_std: 0.3194\n    proved_only_isr: 0.6423\n    isr_by_type:\n      'true': 0.3598\n      'false': 0.1723\n      unknown: 0.0979\n    total_samples: 100\n    proved_count: 32\n    runtime_s: 251.7\n- exp_id: plan001-exec-only-s42-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.93\n    eval_mean_isr: 0.1232\n    eval_isr_std: 0.1887\n    eval_proved_only_isr: 0.1324\n    eval_median_isr: 0\n    eval_n_proved: 93\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n- exp_id: plan001-exec-only-s42-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 1\n    eval_mean_isr: 0.535\n    eval_isr_std: 0.1282\n    eval_proved_only_isr: 0.535\n    eval_median_isr: 0.5\n    eval_n_proved: 100\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_note: 'DEGENERATE: model generates trivial 2-component proofs (premise=conclusion,\n      conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure'\n- exp_id: plan001-exec-only-s43-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_sampling_prove_rate: 0.14\n    eval_sampling_mean_isr: 0\n    eval_sampling_n_proved: 14\n    eval_sampling_temperature: 0.7\n    eval_sampling_method: do_sample=True, temperature=0.7\n    eval_sampling_by_answer:\n      'true':\n        count: 34\n        proved: 6\n        prove_rate: 0.176\n      'false':\n        count: 25\n        proved: 2\n        prove_rate: 0.08\n      unknown:\n        count: 41\n        proved: 6\n        prove_rate: 0.146\n- exp_id: plan002-additive-b03-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 56.7\n    overall_prove_rate: 0.34025\n    overall_isr: 0.11527\n    first20_prove_rate: 0.15625\n    last50_prove_rate: 0.555\n    last100_prove_rate: 0.5525\n    mean_loss: 0.008914\n    last100_loss: 0.014469\n    parse_rate: 1\n    w1_50_prove_rate: 0.13\n    w51_100_prove_rate: 0.095\n    w101_200_prove_rate: 0.185\n    w201_300_prove_rate: 0.375\n    w301_400_prove_rate: 0.47625\n    w401_500_prove_rate: 0.5525\n    steps_ge_085: 52\n    first_step_ge_085: 46\n    final_prove_rate: 1\n    final_isr_mean: 0.3089\n    final_reward_mean: 1.0927\n- exp_id: plan017-additive-random-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.48\n    eval_mean_isr: 0.0453\n    eval_isr_std: 0.0759\n    eval_median_isr: 0\n    eval_max_isr: 0.2857\n    eval_proved_only_isr: 0.0943\n    eval_n_proved: 48\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 9.6\n    eval_component_count_2_ratio: 0\n    eval_isr_pr_ratio: 0.0943\n    eval_elapsed_s: 542.3\n    eval_by_type_false_pr: 0.32\n    eval_by_type_false_isr: 0.0254\n    eval_by_type_unknown_pr: 0.51\n    eval_by_type_unknown_isr: 0.0518\n    eval_by_type_true_pr: 0.56\n    eval_by_type_true_isr: 0.052\n    tautological_collapse: false\n- exp_id: plan014-downstream-nli-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 0.341\n    proved_rate: 0.915\n    proved_count: 732\n    total_generations: 800\n    parse_errors: 0\n    accuracy_by_label:\n      'true': 0.912\n      'false': 0\n      unknown: 0.076\n    spearman_rho: -0.049\n    spearman_p: 0.187\n    mann_whitney_U: 17202\n    mann_whitney_p: 0.288\n    bon_isr_accuracy: 0.35\n    bon_random_accuracy: 0.341\n    bon_oracle_accuracy: 0.44\n    bon_prove_first_accuracy: 0.35\n    isr_bucket_high_acc: 0.75\n    isr_bucket_mid_acc: 0.377\n    isr_bucket_low_acc: 0.327\n    runtime_inference_s: 408.8\n    runtime_eval_s: 13.6\n- exp_id: plan001-exec-only-s44\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.98\n    eval_mean_isr: 0.57\n    eval_isr_std: 0.2013\n    eval_median_isr: 0.5\n    eval_proved_only_isr: 0.5816\n    eval_n_proved: 98\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 2.04\n    eval_component_count_2: 94\n    eval_component_count_3: 4\n    eval_by_type_false_pr: 1\n    eval_by_type_false_isr: 0.62\n    eval_by_type_unknown_pr: 0.976\n    eval_by_type_unknown_isr: 0.524\n    eval_by_type_true_pr: 0.971\n    eval_by_type_true_isr: 0.588\n    train_last100_pr: 0.9988\n    train_last100_isr: 0.5611\n    train_last100_loss: 0.000419\n    train_duration_min: 36.8\n    tautological_collapse: true\n- exp_id: plan002-additive-b01-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.81\n    eval_mean_isr: 0.3365\n    eval_isr_std: 0.3227\n    eval_proved_only_isr: 0.4154\n    eval_median_isr: 0.2\n    eval_n_proved: 81\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 5.58\n    eval_component_count_2_ratio: 0.037\n    eval_isr_1_ratio: 0.124\n    eval_isr_0_ratio: 0.037\n    eval_by_type_false_pr: 0.88\n    eval_by_type_false_isr: 0.3515\n    eval_by_type_unknown_pr: 0.83\n    eval_by_type_unknown_isr: 0.3684\n    eval_by_type_true_pr: 0.74\n    eval_by_type_true_isr: 0.2869\n    tautological_collapse: false\n    train_total_steps: 500\n    train_duration_min: 63\n    train_last100_pr: 0.6875\n    train_last100_isr: 0.1954\n    train_last100_loss: 0.015\n- exp_id: plan016-extended-1000-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train:\n      total_steps: 1000\n      duration_min: 146\n      final_prove_rate: 0.8396\n      final_mean_isr: 0.0503\n      train_loss: 0.0125\n      epoch: 4\n      windowed:\n        steps_001_100:\n          pr: 0.19\n          isr: 0.0859\n        steps_101_200:\n          pr: 0.66\n          isr: 0.1115\n        steps_201_300:\n          pr: 0.838\n          isr: 0.0985\n        steps_301_400:\n          pr: 0.907\n          isr: 0.054\n        steps_401_500:\n          pr: 0.927\n          isr: 0.0433\n        steps_501_600:\n          pr: 0.963\n          isr: 0.0408\n        steps_601_700:\n          pr: 0.965\n          isr: 0.02\n        steps_701_800:\n          pr: 0.988\n          isr: 0.0178\n        steps_801_900:\n          pr: 0.978\n          isr: 0.017\n        steps_901_1000:\n          pr: 0.981\n          isr: 0.0144\n    eval:\n      prove_rate: 0.96\n      n_proved: 96\n      n_problems: 100\n      mean_isr: 0.0027\n      isr_std: 0.0118\n      median_isr: 0\n      proved_only_mean_isr: 0.0028\n      min_isr: 0\n      max_isr: 0.0588\n      isr_0_ratio: 0.9479\n      isr_1_ratio: 0\n      component_count_mean: 18.55\n      component_count_2_ratio: 0\n      mean_n_necessary: 0.052\n      n_necessary_0_ratio: 0.9479\n      tautological_collapse: false\n      by_answer_type:\n        'false':\n          count: 29\n          proved: 26\n          prove_rate: 0.8966\n          mean_isr: 0\n        unknown:\n          count: 31\n          proved: 30\n          prove_rate: 0.9677\n          mean_isr: 0.0053\n        'true':\n          count: 40\n          proved: 40\n          prove_rate: 1\n          mean_isr: 0.0026\n      eval_time_seconds: 396.3\n- exp_id: plan018-additive-random-b01-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.79\n    eval_mean_isr: 0.1038\n    eval_isr_std: 0.1369\n    eval_median_isr: 0.0357\n    eval_proved_only_isr: 0.1314\n    eval_n_proved: 79\n    eval_n_problems: 100\n    eval_component_count_mean: 8.46\n    eval_component_count_median: 8\n    eval_component_count_2_ratio: 0\n    eval_isr_1_ratio: 0\n    eval_isr_0_ratio: 0.367\n    eval_isr_gt0_ratio: 0.633\n    eval_by_type_false_pr: 0.8\n    eval_by_type_false_isr: 0.1318\n    eval_by_type_unknown_pr: 0.7317\n    eval_by_type_unknown_isr: 0.0944\n    eval_by_type_true_pr: 0.8529\n    eval_by_type_true_isr: 0.0945\n    tautological_collapse: false\n    train_total_steps: 500\n    train_duration_min: 70.5\n    train_last100_pr: 0.805\n    train_last100_isr: 0.1432\n    train_loss: 0.005\n- exp_id: plan006-prolog-exec-s42\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-exec-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-exec-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan002-additive-b01-s43\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan002-additive-b01-s44\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan018-additive-random-b01-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan018-additive-random-b01-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan012-hacking-taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    isr_b01_genuine_rate: 0.259\n    random_b01_genuine_rate: 0.177\n    genuine_rate_delta_pp: 8.2\n    isr_b01_conclusion_embedding_rate: 0.728\n    random_b01_conclusion_embedding_rate: 0.785\n    isr_b01_genuine_mean_isr: 0.6723\n    random_b01_genuine_mean_isr: 0.3427\n    isr_b01_complexity_wo_utility_rate: 0\n    random_b01_complexity_wo_utility_rate: 0.038\n    isr_b01_hacking_rate: 0.741\n    random_b01_hacking_rate: 0.823\n- exp_id: plan006-prolog-sta-s42\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-sta-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan006-prolog-sta-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T09:25:52.824Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T09:25:52.824Z",
  "sessionId": "31e665a0-dae3-4463-8403-346ff6c49913"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-14T09:25:52.848Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "11cf7fd2-60af-47c6-83fe-88831095dfe9",
  "type": "user",
  "uuid": "23aac7c7-dd1f-4654-93d8-e6e1f66cdc10",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "31e665a0-dae3-4463-8403-346ff6c49913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T09:25:52.846Z_

```json
{
  "parentUuid": "23aac7c7-dd1f-4654-93d8-e6e1f66cdc10",
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
  "uuid": "765d572f-148e-45b5-98f6-53ffc20750de",
  "timestamp": "2026-05-14T09:25:52.846Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "31e665a0-dae3-4463-8403-346ff6c49913",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T09:25:52.847Z_

```json
{
  "parentUuid": "765d572f-148e-45b5-98f6-53ffc20750de",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f8d0fd9a-d778-446a-a9ea-be67dfb6a5c5",
  "timestamp": "2026-05-14T09:25:52.847Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "31e665a0-dae3-4463-8403-346ff6c49913",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "f8d0fd9a-d778-446a-a9ea-be67dfb6a5c5",
  "sessionId": "31e665a0-dae3-4463-8403-346ff6c49913"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for solver-trace-ablation",
  "sessionId": "31e665a0-dae3-4463-8403-346ff6c49913"
}
```

---

### Assistant

_source line 8 · 2026-05-14T09:26:33.669Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this research project carefully to define three tiers for a Dream simulation.

The project is "solver-trace-ablation" targeting EMNLP 2026. Let me understand the key claims and current status:

**Claim 1 (ISR as Reward Hacking Diagnostic)**: Strong evidence. ISR collapse trajectory 0.6423 → 0.1324 → 0.0027 over 100/500/1000 steps. 3-seed consistency showing different hacking modes. 5 hacking modes identified. This claim is well-supported.


**Claim 2 (ISR as Proxy Metric Exhibits Goodhart's Law)**: The evidence is solid for one seed so far—β=0.1 gives a 3.2x improvement over random while β=0.3 triggers the collapse pattern. I've got the quantitative hacking taxonomy comparison done, but I'm still waiting on results from the other two seeds to confirm the pattern holds across runs.

**Claim 3 (Cross-Logic Generality)**: The Prolog experiments are queued and haven't produced results yet, so this one's still pending.

I've got several experiments actively running or in the queue right now, including the additional seeds for the β=0.1 condition.

The main questions I'm trying to answer are whether the ISR advantage at β=0.1 will replicate across all three seeds, whether the Prolog experiments will show the same hacking and ISR diagnostic patterns, and what the final mean performance looks like once everything finishes.

I'm mapping out three scenarios: best case where everything replicates cleanly with tight confidence intervals and the paper stays strong for EMNLP, median case where results partially hold but need some caveats and softened claims, and worst case where the ISR advantage doesn't replicate across the additional seeds.

Now I'm defining the specific metrics I need to track—the 3-seed mean ISR at β=0.1, the ISR-to-random ratio, and whether the Prolog experiments show consistent hacking patterns. Looking at the current seed 42 numbers to establish a baseline. Looking at the Prolog experiments, I need to see whether hacking is clearly detectable with high precision and low ISR, and whether the ISR diagnostic actually works across multiple seeds. The genuine rate comparison is also critical—I'm checking if the gap between ISR and random holds up or shrinks across different runs. Now I'm thinking through the narrative structure: a full three-claim paper would argue that ISR is a principled diagnostic for reward hacking in formal reasoning GRPO, but I need to verify the evidence supports that claim across the best, median, and worst-case scenarios. The worst-case framing shifts the narrative away from finding an optimal sweet spot toward emphasizing how fragile ISR optimization actually is—still a solid diagnostic paper for EMNLP, just with a different angle on what the findings mean. Now I'll structure this as YAML.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8d0fd9a-d778-446a-a9ea-be67dfb6a5c5",
  "isSidechain": false,
  "requestId": "req_011Cb2DnkZWa8SvD3Hv2DcUX",
  "type": "assistant",
  "uuid": "2d7aaf99-9c25-49ad-a194-17158cd81d72",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "31e665a0-dae3-4463-8403-346ff6c49913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpuFsHupwvnzSC7WbXLS5U",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21526,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3913,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21526,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3913,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21526
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

_source line 9 · 2026-05-14T09:27:16.566Z_

```yaml
tiers:
  best:
    meaning: "β=0.1 ISR sweet spot 跨 3 seed 复现且效应量稳健；Prolog 实验成功复现 hacking + ISR 诊断。三条 claim 全部成立。"
    key_assumptions:
      - "plan002-b01 s43/s44 复现 s42 方向：ISR β=0.1 >> random β=0.1，PR 维持"
      - "3-seed ISR/random ratio ≥ 2.5x，置信区间不跨 1"
      - "plan006 Prolog exec-only 出现可检测的 reward hacking（PR 高但 ISR 低）"
      - "Prolog ISR 诊断有效：至少 2/3 seed 可区分 genuine vs hacking"
      - "3-seed hacking taxonomy 在 FOL 和 Prolog 间共享 ≥3 种模式"
    number_ranges:
      three_seed_isr_b01_mean_isr: [0.28, 0.40]
      three_seed_isr_b01_mean_pr: [0.72, 0.85]
      three_seed_random_b01_mean_isr: [0.08, 0.16]
      three_seed_isr_over_random_ratio: [2.5, 4.0]
      three_seed_genuine_rate_delta_pp: [5.0, 12.0]
      prolog_exec_only_pr: [0.70, 0.95]
      prolog_exec_only_isr: [0.01, 0.20]
      prolog_hacking_modes_shared_with_fol: [3, 5]
    narrative_direction: >
      原始 framing 完全成立。三条 claim 无需调整：(1) ISR 诊断 reward hacking，(2) ISR-as-reward 
      展现 Goodhart's Law 且 sweet spot 跨 seed 稳健（mean±std 报告），(3) STA 协议跨逻辑泛化。
      Headline: "ISR sweet spot at β=0.1 replicates across 3 seeds (mean ISR 3x > matched 
      random control, p<0.05) and the STA diagnostic protocol transfers to Prolog." 
      投 EMNLP main，诊断+Goodhart+泛化三线并行。

  median:
    meaning: "β=0.1 sweet spot 方向性复现但效应量缩水或 variance 大；Prolog 部分成功或未完成。Claim 1 完整，Claim 2 需弱化置信度，Claim 3 降级。"
    key_assumptions:
      - "s43/s44 至少 1 个复现方向（ISR > random），但另一个效应弱或 PR 下降"
      - "3-seed ISR/random ratio 1.3–2.5x，置信区间可能跨 1"
      - "Prolog 训练收敛但 hacking 模式不清晰，或 ISR 诊断力弱于 FOL"
      - "β=0.1 genuine rate delta 缩至 2–5pp，不再显著"
      - "exec-only 3-seed ISR 崩塌轨迹仍然稳健（这是 Claim 1 的基础）"
    number_ranges:
      three_seed_isr_b01_mean_isr: [0.18, 0.30]
      three_seed_isr_b01_mean_pr: [0.60, 0.80]
      three_seed_random_b01_mean_isr: [0.10, 0.20]
      three_seed_isr_over_random_ratio: [1.3, 2.5]
      three_seed_genuine_rate_delta_pp: [1.0, 5.0]
      three_seed_isr_b01_std: [0.08, 0.15]
      prolog_exec_only_pr: [0.40, 0.75]
      prolog_hacking_detectable: ["unclear", "partial"]
    narrative_direction: >
      Claim 1（ISR 诊断）不受影响——ISR 崩塌轨迹和 hacking taxonomy 已有 3-seed 多条件数据。
      Claim 2 调整：sweet spot 存在但 fragile——"ISR β=0.1 shows directional improvement over 
      matched random (mean ratio ~1.8x) but high inter-seed variance suggests the sweet spot 
      is narrow and sensitive to initialization." 弱化 "3.2x" 为 mean±std 报告，不做显著性声明，
      改为 effect size + 方向性论述。Claim 3 降为 "Preliminary Evidence" 或 Future Work。
      论文重心从三线并行收缩为 Claim 1（诊断）+ Claim 2（Goodhart 案例研究，含不确定性讨论）。
      增补 seed-variability 本身作为发现（"same setup, 3 seeds, 3 different hacking strategies"）
      强化 GRPO 不稳定性论点。仍投 EMNLP main，但 scope 收窄。

  worst:
    meaning: "β=0.1 sweet spot 不复现——s43/s44 显示 ISR ≈ random 或其中一个 seed 崩塌。Prolog 实验失败或无法完成。Claim 2 sweet spot 是单 seed artifact，Claim 3 无数据。"
    key_assumptions:
      - "s43 或 s44 中 ISR β=0.1 的 ISR 值落入 random 的范围（ratio < 1.3x），或 PR 严重下降（<0.5）"
      - "3-seed mean 后 ISR vs random 差异不具方向一致性"
      - "Prolog 训练不收敛、或收敛但无 hacking（PR 和 ISR 同步上升）、或实验未能在 deadline 前完成"
      - "Claim 1 的 ISR 崩塌轨迹和 hacking taxonomy 仍然成立（这些基于已完成实验）"
      - "β=0.3 的 Goodhart 崩塌仍然成立（ISR 18% < random 48%，已完成）"
    number_ranges:
      three_seed_isr_b01_mean_isr: [0.10, 0.22]
      three_seed_isr_b01_mean_pr: [0.40, 0.75]
      three_seed_random_b01_mean_isr: [0.10, 0.20]
      three_seed_isr_over_random_ratio: [0.8, 1.3]
      three_seed_isr_b01_std: [0.12, 0.25]
      prolog_status: ["failed", "incomplete", "no_hacking"]
    narrative_direction: >
      Reframe 为纯诊断+Goodhart 失败模式论文，放弃 "sweet spot" 作为 positive result。
      新 headline: "We show that execution-only GRPO produces structurally degenerate 
      formalizations across all seeds (ISR: 0.64→0.13→0.003 over training), identify 5 
      distinct hacking strategies, and demonstrate that ISR as reward signal exhibits 
      Goodhart's Law at ALL tested doses — even β=0.1's apparent success is seed-dependent 
      and unreliable." 
      核心转变：(a) Claim 1 不变——ISR 诊断 + 5-mode taxonomy 是论文主体；
      (b) Claim 2 从 "sweet spot exists" 翻转为 "no reliable sweet spot exists, ISR reward 
      is fundamentally fragile"——这本身是更强的 Goodhart 论证（连 low-dose 都不可靠）；
      (c) seed variability 升级为核心发现："identical setup produces qualitatively different 
      hacking strategies"，论证 GRPO 训练的根本不稳定性；
      (d) Claim 3 完全删除或一句 future work。
      仍投 EMNLP main——诊断/分析论文不依赖 positive intervention result，Goodhart 的 negative 
      result 反而更 clean。但需要加厚 Related Work 和 taxonomy 分析以补偿 positive result 缺失。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d7aaf99-9c25-49ad-a194-17158cd81d72",
  "isSidechain": false,
  "requestId": "req_011Cb2DnkZWa8SvD3Hv2DcUX",
  "type": "assistant",
  "uuid": "5666493b-4186-4bdb-b2bd-ece5befcd596",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "31e665a0-dae3-4463-8403-346ff6c49913",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TpuFsHupwvnzSC7WbXLS5U",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21526,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3913,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21526,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3913,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21526
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "5666493b-4186-4bdb-b2bd-ece5befcd596",
  "sessionId": "31e665a0-dae3-4463-8403-346ff6c49913"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for solver-trace-ablation",
  "sessionId": "31e665a0-dae3-4463-8403-346ff6c49913"
}
```

---
