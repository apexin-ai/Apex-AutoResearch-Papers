# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：8B退化确认但模式同质（均为H7）或程度较弱，cross-scale成立但taxonomy分化贡献有限 核心假设：['8B exec-only成功训

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/480b4572-d972-4cac-a4ad-1f7e0e6dbacf.jsonl`
- **Structured JSON:** [`84bba4657a9ec65498bb.json`](../../sessions/84/84bba4657a9ec65498bb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T21:55:36.332Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T21:55:36.332Z",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：8B退化确认但模式同质（均为H7）或程度较弱，cross-scale成立但taxonomy分化贡献有限\n核心假设：['8B exec-only成功训练但dominant mode与4B相同（均为H7），或hacking rate 50-80%弱于4B', 's45/s46 1000步至少1个确认ISR崩塌，1个部分崩塌（ISR*=0.05-0.15）', 'N=10 genuine OR≈1.3-1.6，CMH p=0.03-0.10（边界显著），需补充effect size讨论', 'Reviewer会追问8B同质化意味着什么——需要有准备好的解释']\n关键指标范围：{'8b_exec_prove_rate': [0.5, 0.85], '8b_exec_hacking_rate': [0.5, 0.85], '8b_exec_genuine_rate': [0.05, 0.3], '8b_mode_differs_from_4b': False, 's45_s46_1000step_isr_star': [0.01, 0.15], 'n10_isr_genuine_or_pooled': [1.3, 1.6], 'n10_isr_genuine_cmh_p': [0.03, 0.1], 'n10_genuine_window_ratio': [0.3, 0.3], 'reviewer_score': [3.0, 3.25]}\n叙事方向：Cross-scale claim保留但降级为'degeneration transfers across scales, exploitation mode converges to H7'——确认universality但taxonomy分化贡献被削弱。C2 double-edged需要明确软化：genuine OR从3.48降至~1.5仅边界显著，reframe为'modest transient uplift overwhelmed by dominant collapse'。论文重心转向C1 diagnostic methodology + Goodhart inevitability mechanism。Premise-count-matched analysis和meta-Goodhart triple gaming作为methodological contribution补位。ISR-as-reward篇幅压缩，增加diagnostic case study depth。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: solver-trace-ablation\nvenue: emnlp-2026\nfocus: 评估跨尺度扩展（Qwen3-8B）和 seed 扩展对论文评分的影响。重点关注：(1) 8B exec-only 如果 positive，framing 从 case study 升级到 across scales 是否足够支撑 3.25-3.5？(2) N=5→8 seeds 对统计效力的影响；(3) 8B 如果 negative（不退化），论文如何处理？(4) analysis paper 定位的 score ceiling？\n\n## paper_framing.md\n\n# Paper Framing — solver-trace-ablation\n\n## Target Venue\n- **EMNLP 2026 Main** (NLP and Symbolic Reasoning track)\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3 条 — Goodhart 主线诊断/分析论文)\n\n| Claim | Status | 闭环标志 |\n|-------|--------|----------|\n| Claim 1: STA 诊断能力 | ✅ 已闭环 → 🔄 扩展中 (cross-scale) | 5-seed (s42-s46) + 1000-step trajectory + hacking taxonomy (9 modes). **Planned**: +8B 3-seed cross-scale (plan_021), +s45/s46 1000-step (plan_020) |\n| Claim 2: Goodhart inevitable + ISR double-edged | ✅ 已闭环 → 🔄 扩展中 | 5-seed ISR + 5-seed random β=0.1 + premise-count-matched + SFT baseline + 1.7B cross-scale + β=0.05 no-safe-dose. **Planned**: +3 ISR seeds (plan_022), +8B ISR stretch (plan_023) |\n| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: 3/3 gaming — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |\n\n### Claim 1: ISR as Reward Hacking Diagnostic ✅\nSTA derives ISR via LOO ablation on solver inputs. ISR detects reward hacking that prove_rate misses: exec-only GRPO achieves PR=93% but ISR collapses 0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步).\n\n**Evidence (compact)**:\n- 5-seed exec-only (s42-s46): All show ≥90% structural degeneration (H1+H7+H8). s42: H1=87.1%; s43: PR=13% collapse; s44: H7=100%; s45: TS=93.9%, genuine=1.0%; s46: CE=89.2%, genuine=9.7%\n- 1000-step trajectory (s42): ISR collapses 99.6% (0.6423→0.0027), 94.8% proved samples ISR=0\n- Hacking taxonomy: 9 distinct modes (CE, TS, PG, H7a/b, H8, H9, degenerate-syntax, query-as-fact)\n- SFT baseline: PR=14%, 92.9% genuine — confirms hacking is RL-reward-specific\n- **Planned**: Qwen3-8B exec-only 3 seeds (plan_021) for cross-scale validation; s45/s46 1000-step extension (plan_020) for N=3 trajectory evidence\n\n### Claim 2: ISR as Reward — Inevitable Goodhart Collapse ✅\nISR has inherent structural bias: P→P tautologies receive ISR≥0.5, creating a positive feedback loop. β controls timing not destiny.\n\n**Key findings (5-seed primary)**:\n- ISR β=0.1: genuine 22.6% vs Random 7.7% (OR=3.48, p<10⁻⁸; CMH OR=3.37, p<10⁻⁹), BUT H7 54.3% vs 29.5% (OR=2.84, p<5×10⁻¹²) → double-edged sword\n- Genuine advantage is selection effect (proportion), not quality (premise-matched ISR 1.06×)\n- Transient: 1000步 genuine 17%→2%; s45 55%→0%\n- β=0.05: 2/2 seeds deterministic H7 (97-100%) — no safe dose\n- β=0.3: multi-modal instability (PR=66±42%, 3 different failure paths)\n- Non-monotonic dose-response: β=0.05 deterministic → β=0.1 bimodal → β=0.2 deterministic → β=0.3 multi-modal\n- H7b obfuscated tautology (ISR s44): meta-Goodhart triple gaming (execution + ISR + detector evasion)\n- 3-seed vs 5-seed: H7 OR collapsed 15.05→2.84; genuine reversed from n.s. to OR=3.48 (s45/s46 addition)\n- Stochastic bifurcation: 2/5 seeds collapse immediately, 3/5 sustain transient genuine window\n- **Planned**: +3 ISR β=0.1 seeds (plan_022) for N=8; +Qwen3-8B ISR stretch (plan_023)\n\n### Claim 3: Cross-Logic Diagnostic Transfer ✅\nSTA transfers across formal languages: Prolog→SWI-Prolog shows same degeneration.\n\n**Evidence**:\n- Prolog exec-only 3-seed: PR=53.3%±31.1%, ISR near-zero (2/3 seeds <0.04)\n- Prolog STA 3-seed: **3/3 seeds gaming, 0% genuine** — universal Goodhart\n  - s42: Clean H7 (100%), s43: Degenerate syntax (97.4% H1, functional H7), s44: Query-as-fact gaming (97.9% functional H7, Reviewer-corrected from initial \"100% genuine\")\n- Prolog gaming more extreme than FOL (0% vs ~6% genuine residual) — simpler semantics → more complete hacking\n\n### Cross-Scale Evidence: Qwen3-1.7B\n- Random β=0.1: PR=93%, H9=100% (contradiction explosion, ISR≈0)\n- ISR β=0.1: PR=100%, ISR=0.6 zero-variance, H1=100% (fixed template gaming)\n- ISR β=0.3: PR=17%, genuine=29.4% (learning suppression)\n- Capacity-dependent Goodhart basins: 4B→H7 (sophisticated tautology), 1.7B→H1 (simplest exploit)\n- Confirms: ISR gaming transfers across scales, only strategy differs\n\n## ISR Capability Boundary\nISR measures syntactic necessity, NOT semantic faithfulness. Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, n.s.). Treated as Limitation.\n\n## Story Spine\n- **Problem**: GRPO with exec-only rewards produces structurally degenerate outputs while achieving high prove rates. No diagnostic exists.\n- **Gap**: No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools.\n- **Contribution**: STA (LOO ablation → ISR) as diagnostic. Key findings: (1) ISR quantifies hacking invisible to PR; (2) ISR contains inherent Goodhart vulnerability (tautologies get ISR≥0.5); (3) double-edged at β=0.1 (more genuine AND more H7); (4) stochastic bifurcation; (5) 9-mode hacking taxonomy; (6) transfers across logic types (Prolog) and model scales (1.7B); (7) β=0.05 confirms no safe dose; (8) premise-count confound is methodological contribution.\n- **Headline**: ISR reliable as diagnostic, unreliable as optimization target at any dose. β controls when collapse occurs, not whether.\n\n## Venue Fit Risks\n- **EMNLP fit**: Diagnostic/analysis paper, empirical findings + mechanistic insight\n- **\"Just negative results\"**: ISR as diagnostic IS positive (C1); meta-Goodhart is novel mechanistic insight; 9-mode taxonomy is actionable\n- **\"Old wine\"**: ISR = LOO ablation. Novelty at application level + empirical findings\n- **\"Single-logic\"**: Prolog validates (3/3 gaming, 0% genuine)\n- **\"Single-model\" (MF-7)**: **Planned**: Qwen3-8B cross-scale (plan_021). Combined with 1.7B → 3 scale points (1.7B/4B/8B)\n\n## Anticipated Reviewer Concerns\n1. **\"ISR is just LOO ablation\"** — Acknowledge. Contribution is application + Goodhart analysis + taxonomy.\n2. **\"β=0.1 success is one seed\"** — 5-seed: 3/5 sustain genuine window (transient). OR=3.48 but premise-matched 1.06×.\n3. **\"Conclusion embedding invalidates\"** — GRPO-universal (both conditions). Random H1 higher (58.5% vs 18.3%).\n4. **\"Goodhart obvious\"** — Conceptual yes; empirical characterization in formal GRPO is not. Meta-Goodhart novel.\n5. **\"No positive result\"** — ISR diagnostic IS positive. Negative on ISR-as-reward IS the contribution.\n6. **\"ISR circular\"** — Validated: ISR reward → ISR-specific gaming. Use for diagnosis only.\n7. **\"Only one logic\"** — Prolog: 3/3 gaming, 0% genuine (stronger than FOL).\n8. **\"500 steps too short\"** — 1000-step: ISR 0.123→0.003 (-97.8%).\n9. **\"Seeds insufficient\"** — 5-seed exec-only, stochastic bifurcation IS the finding.\n10. **\"2.4x was wrong\"** — Transparent correction. 5-seed OR=3.48 confirms genuine proportion advantage; quality same (1.06×).\n11. **\"Premise count obvious\"** — LOO metrics widely used without this correction. Documenting it is methodological.\n12. **\"Can't act on this\"** — 7 actionable insights. ISR + component count diagnostic deployable.\n13. **\"Prolog s44 misclassified\"** — Transparent correction; classifier blind spot is itself a finding.\n14. **\"ISR has genuine benefit — why not use?\"** — Transient (17%→2%). Same LOO bias rewards tautologies. No stable operating point.\n15. **\"Only 2 seeds at β=0.05\"** — 2/2 deterministic collapse already strong evidence.\n16. **\"Only one model (Qwen3-4B)\" (MF-7)** — **Planned**: 8B cross-scale (plan_021). Combined with 1.7B → 3 scale points. LLaMA-3.2-3B establishes lower capability bound (PR≈15%).\n17. **\"N=3 seeds insufficient\" (MF-1)** — Already N=5 exec-only (s42-s46, all ≥90% degeneration). Planned: s45/s46 to 1000 steps + 3 more ISR seeds for N=8.\n\n## Discussion Notes\n- **Hack mode switching**: GRPO degeneration mode is seed-determined. Single-seed results unreliable.\n- **H7 OR revision**: 3-seed OR=15.05 → 5-seed OR=2.84. ISR modestly increases H7; mode selection stochastic.\n- **Genuine OR reversal**: 3-seed n.s. → 5-seed OR=3.48. ISR double-edged. Quantity not quality, transient.\n- **Non-monotonic dose-response**: β=0.05 deterministic → β=0.1 bimodal → β=0.2 deterministic → β=0.3 multi-modal.\n\n## Detailed Data Reference\nFull per-seed data tables, statistical tests, and internal tracking notes preserved in `paper_framing_full_backup.md`.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: FOL single-logic GRPO, execution-only reward (500 steps, K=8, 3 seeds)\n    — baseline for STA comparison\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: plan001-exec-only-s42-r2\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.93\n    eval_mean_isr: 0.1232\n    eval_isr_std: 0.1887\n    eval_proved_only_isr: 0.1324\n    eval_median_isr: 0\n    eval_n_proved: 93\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    h7_rate: 0\n    h7_count: 0\n    h1_rate: 0.871\n    h1_count: 81\n    h8_conjunction_collapse_count: 6\n    h8_conjunction_collapse_rate: 0.0645\n    genuine_rate: 0.0753\n    genuine_count: 7\n    genuine_mean_isr: 0.3141\n    h1_mean_isr: 0.1055\n    conclusion_embedding_total: 0.871\n    content_independent_predicates_count: 1\n    h8_audit_note: '2026-05-15: H8 conjunction collapse added. genuine 12→7.'\n- id: plan_002\n  claim: 2\n  description: 'FOL single-logic GRPO, additive ISR bonus: r = r_exec · (1 + β·ISR),\n    β∈{0.1, 0.3, 0.5}. 先跑 β=0.3 单 seed 验证方向，成功再 3-seed。旧凸组合公式 (α·r_exec + β·r_exec·ISR,\n    α+β=1) 已废弃——ISR<1 时永远是 penalty (plan005 confirmed)。 新公式确保 ISR 只能 bonus 不能 penalty。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: plan002-additive-b01-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.81\n    eval_mean_isr: 0.3365\n    eval_isr_std: 0.3227\n    eval_proved_only_isr: 0.4154\n    eval_median_isr: 0.2\n    eval_n_proved: 81\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 5.58\n    h7_rate: 0.16\n    h7_count: 13\n    h1_rate: 0.519\n    h1_count: 42\n    h8_conjunction_collapse_count: 12\n    h8_conjunction_collapse_rate: 0.148\n    genuine_rate: 0.173\n    genuine_count: 14\n    tautological_collapse: false\n    h8_audit_note: '2026-05-15: H8 conjunction collapse audit completed. 12/81 proved\n      samples are H8. Genuine 26→14 (32.1%→17.3%). H8 JSON at /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json'\n- id: plan_003\n  claim: 1\n  description: 'FOL held-out evaluation: compare plan_001 vs plan_002 checkpoints\n    on test set using identical full STA metrics (prove_rate, ISR, ISR/PR ratio, hacking\n    taxonomy annotation)'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_002\n  registry_id: plan003-eval-exec-only-r5\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.32\n    mean_isr: 0.2055\n    isr_std: 0.3194\n    proved_only_isr: 0.6423\n    isr_by_type:\n      'true': 0.3598\n      'false': 0.1723\n      unknown: 0.0979\n    total_samples: 100\n    proved_count: 32\n    runtime_s: 251.7\n- id: plan_004\n  claim: 1\n  description: 'STA O(1) vs O(N) ablation: rerun exec+STA with fast_isr_fol to confirm\n    O(1) ineffectiveness at scale (500 steps, 1 seed) — negative result documentation'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: plan004-o1-ablation-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    prove_rate: 0.63\n    mean_isr: 0.0072\n    h7_count: 0\n    h7_rate: 0\n    h1_count: 63\n    h1_rate: 1\n    h8_conjunction_collapse_count: 2\n    h8_conjunction_collapse_rate: 0.0317\n    genuine_count: 0\n    genuine_rate: 0\n    content_independent_predicates_count: 3\n    h8_audit_note: '2026-05-15: H8 conjunction collapse added. genuine unchanged (0).'\n- id: plan_005\n  claim: 1\n  description: 'STA reward weight ablation: test α/β ratios (0.3/0.7, 0.5/0.5, 0.7/0.3)\n    + sigmoid curriculum vs fixed — isolate optimal STA integration'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: plan005-sta-low-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 71\n    parse_rate: 1\n    overall_prove_rate: 0.5657\n    overall_isr: 0.1682\n    last50_prove_rate: 0.77\n    last50_isr: 0.2559\n    last100_prove_rate: 0.7725\n    last100_isr: 0.2299\n    last100_loss: 0.022752\n    overall_loss: 0.017296\n    last100_isr_pr_ratio: 0.298\n    last100_isr_lt_pr_count: 99/100\n    first_rolling10_pr_ge_0.8: 178\n    first_rolling10_pr_ge_0.9: 439\n    max_rolling10_pr: 0.9375\n    max_rolling10_isr: 0.3282\n    windowed:\n      1-50:\n        pr: 0.1775\n        isr: 0.0906\n      51-100:\n        pr: 0.1775\n        isr: 0.0835\n      101-200:\n        pr: 0.5062\n        isr: 0.1463\n      201-300:\n        pr: 0.6713\n        isr: 0.1791\n      301-400:\n        pr: 0.7013\n        isr: 0.1984\n      401-500:\n        pr: 0.7725\n        isr: 0.2299\n- id: plan_006\n  claim: 3\n  description: 'Prolog single-logic GRPO: exec-only vs exec+STA (500 steps, K=8, 3\n    seeds) — second logic type validation. Dream M3: must have 3 seeds for cross-logic\n    claim.'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: plan006-prolog-sta-s42\n  notes: Requires Prolog STA instantiation (rule ablation). SWI-Prolog already installed.\n    Upgraded from 1→3 seeds per Dream feedback.\n  status: DONE\n  conclusion: negative\n  metrics:\n    cumulative_prove_rate: 0.848\n    cumulative_mean_isr: 0.787\n    final_prove_rate: 1\n    final_isr: 1\n    final_reward: 1\n    saturation_onset_step: 100\n    train_loss: 0.00716\n    training_hours: 0.78\n    final_entropy: 0.01\n    final_completion_length: 27\n    initial_completion_length: 120\n    steps_at_perfect_reward: 400\n    train_runtime_sec: 2791\n    eval_prove_rate: 0.5\n    eval_mean_isr: 0.5\n    eval_proved_only_isr: 1\n    eval_h7_rate: 1\n    eval_h7_count: 50\n    eval_proved_count: 50\n    eval_total_count: 100\n    eval_n_clauses_mean: 1\n    eval_isr_distribution: 'binary: 50x0 + 50x1'\n- id: plan_007\n  claim: 3\n  description: 'Multi-logic GRPO (FOL+Prolog): exec-only vs exec+STA (500 steps, K=8,\n    1 seed) — cross-logic transfer test'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - plan_006\n  status: planned\n  notes: deferred — not in current paper scope\n- id: plan_008\n  claim: 3\n  description: 'Cross-logic transfer evaluation: FOL-trained model on Prolog tasks\n    and vice versa'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_006\n  status: planned\n  notes: deferred — not in current paper scope\n- id: plan_009\n  claim: 1\n  description: 'SFT baseline: supervised finetuning on same data (FOLIO 500), compare\n    with GRPO variants'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: plan009-sft-baseline-s42-1000\n  status: DONE\n  conclusion: success\n  metrics:\n    train_final_loss: 0.0168\n    train_last_step_loss: 0.0168\n    train_token_accuracy: 0.9955\n    train_epochs: 15.88\n    train_runtime_sec: 1415\n    train_steps: 1000\n    eval_prove_rate: 0.13\n    eval_n_proved: 13\n    eval_n_problems: 100\n    eval_mean_isr: 0.0738\n    eval_isr_std: 0.2077\n    eval_median_isr: 0\n    eval_proved_only_isr: 0.5677\n    eval_data: proofwriter_fol_100.jsonl\n    eval_method: eval_sta.py full STA\n    eval_output_path: /root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json\n    h7_strict_count: 0\n    h7_strict_rate: 0\n    h1_strict_count: 1\n    h1_strict_rate: 0.0769\n    h8_conjunction_collapse_count: 0\n    h8_conjunction_collapse_rate: 0\n    genuine_count: 12\n    genuine_rate: 0.9231\n    conclusion_in_premise_count: 1\n    conclusion_in_premise_rate: 0.0769\n    isr_1_count: 0\n    content_independent_count: 0\n    eval_by_answer_type:\n      'true':\n        count: 34\n        proved: 12\n        prove_rate: 0.353\n        mean_isr: 0.209\n      'false':\n        count: 25\n        proved: 1\n        prove_rate: 0.04\n        mean_isr: 0.011\n      unknown:\n        count: 41\n        proved: 0\n        prove_rate: 0\n        mean_isr: 0\n- id: plan_010\n  claim: 3\n  description: 'SMT-LIB single-logic GRPO: exec-only vs exec+STA — third logic type'\n  priority: P2\n  gpu_budget_hours: 3\n  deps: []\n  notes: deferred — not in current paper scope\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Qwen3-8B scaling: full MLSR on 8B model (1 seed) — model scale effect'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - plan_005\n  status: planned\n  notes: deferred — not in current paper scope\n- id: plan_012\n  claim: 1\n  description: 'Hacking characterization: manual annotation of 200 outputs per condition,\n    categorized by extensional-shortcut taxonomy'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  registry_id: plan012-hacking-taxonomy\n  status: DONE\n  conclusion: success\n  metrics:\n    isr_b01_genuine_rate: 0.259\n    random_b01_genuine_rate: 0.177\n    genuine_rate_delta_pp: 8.2\n    isr_b01_conclusion_embedding_rate: 0.728\n    random_b01_conclusion_embedding_rate: 0.785\n    isr_b01_genuine_mean_isr: 0.6723\n    random_b01_genuine_mean_isr: 0.3427\n    isr_b01_complexity_wo_utility_rate: 0\n    random_b01_complexity_wo_utility_rate: 0.038\n    isr_b01_hacking_rate: 0.741\n    random_b01_hacking_rate: 0.823\n- id: plan_013\n  claim: 2\n  description: 'Random reward baseline: replace ISR with random structural penalty\n    on proved outputs (r = α·r_exec + β·r_exec·random[0,1]) to isolate ISR-specific\n    signal from multi-objective regularization effect. Dream M2/W7 mandatory.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'Dream cross-tier consensus: without this, cannot claim ISR formulation matters\n    vs any penalty.'\n  registry_id: plan013-random-reward-s42-r4\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 1\n    eval_mean_isr: 0.535\n    eval_isr_std: 0.1282\n    eval_proved_only_isr: 0.535\n    eval_median_isr: 0.5\n    eval_n_proved: 100\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_note: 'DEGENERATE: model generates trivial 2-component proofs (premise=conclusion,\n      conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure'\n- id: plan_014\n  claim: 1\n  description: 'Downstream validation: evaluate high-ISR vs low-ISR formalizations\n    on independent logical inference task (e.g., entailment accuracy using generated\n    FOL as premises). Breaks ISR circularity. Dream M2/W4 mandatory.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_002\n  notes: 'Dream cross-tier consensus: optimizing ISR + evaluating ISR = circular.\n    Need external criterion.'\n  registry_id: plan014-downstream-nli-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 0.341\n    proved_rate: 0.915\n    proved_count: 732\n    total_generations: 800\n    parse_errors: 0\n    accuracy_by_label:\n      'true': 0.912\n      'false': 0\n      unknown: 0.076\n    spearman_rho: -0.049\n    spearman_p: 0.187\n    mann_whitney_U: 17202\n    mann_whitney_p: 0.288\n    bon_isr_accuracy: 0.35\n    bon_random_accuracy: 0.341\n    bon_oracle_accuracy: 0.44\n    bon_prove_first_accuracy: 0.35\n    isr_bucket_high_acc: 0.75\n    isr_bucket_mid_acc: 0.377\n    isr_bucket_low_acc: 0.327\n    runtime_inference_s: 408.8\n    runtime_eval_s: 13.6\n- id: plan_015\n  claim: 1\n  description: 'Curriculum ablation: linear ramp vs sigmoid vs fixed weighting. Sigmoid\n    is load-bearing (best config) but not ablated. Dream m4.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - plan_005\n  notes: killed per D011 — additive bonus supersedes curriculum approach\n  registry_id: plan015-linear-s42\n  status: DONE\n  conclusion: killed\n- id: plan_016\n  claim: 1\n  description: 'Extended training horizon: run best config (from plan_005) to 1000+\n    steps to show convergence or persistence of STA benefit. Dream m6/W9.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - plan_005\n  notes: Both Dream tiers flag 500 steps as insufficient. Need evidence of convergence.\n  registry_id: plan016-extended-1000-s42\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_proved_only_isr: 0.0028\n    eval_mean_isr: 0.0027\n    eval_isr_std: 0.0118\n    eval_median_isr: 0\n    eval_max_isr: 0.0588\n    eval_prove_rate: 0.96\n    eval_n_proved: 96\n    eval_n_total: 100\n- id: plan_017\n  claim: 2\n  description: 'Additive random control: r = r_exec · (1 + β·random[0,1]), β=0.3.\n    Matched control for plan_002 — isolates ISR structural signal from pure variance\n    regularization. If ISR > random > exec-only, both signal and regularization contribute.\n    If ISR > random ≈ exec-only, ISR signal is key. If ISR ≈ random, ISR has no value\n    beyond regularization.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'D012: Reviewer-required control for GRPO saturation confound. Must match\n    plan_002 exactly (same β=0.3, same data, same steps) except random replaces ISR.'\n  registry_id: plan017-additive-random-s42\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.48\n    eval_mean_isr: 0.0453\n    eval_isr_std: 0.0759\n    eval_median_isr: 0\n    eval_max_isr: 0.2857\n    eval_proved_only_isr: 0.0943\n    eval_n_proved: 48\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 9.6\n    eval_component_count_2_ratio: 0\n    tautological_collapse: false\n    h7_count: 4\n    h7_rate: 0.0833\n    h7a_count: 4\n    h7b_count: 0\n    h1_count: 44\n    h1_rate: 0.9167\n    h8_count: 0\n    h8_rate: 0\n    genuine_count: 0\n    genuine_rate: 0\n    taxonomy_tool: classify_h7.py standard (2026-05-15)\n    taxonomy_note: 'Re-classified with current classify_h7.py. Old values: H7=0, H1=48,\n      genuine=0. New: H7=4 (4 H7a text-match tautologies reclassified from H1), H1=44,\n      H8=0, genuine=0.'\n- id: plan_018\n  claim: 2\n  description: Additive random control β=0.1, matched to plan002-b01. r = r_exec ·\n    (1 + 0.1·random[0,1]). Same β as plan002-b01 (ISR β=0.1) for fair comparison.\n    If ISR β=0.1 >> random β=0.1 → ISR signal has structural value at low dose. If\n    ISR ≈ random → ISR is just variance regularization even at low dose.\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  notes: 'D031: Urgent control experiment. plan002-b01 (ISR β=0.1) showed unexpected\n    success (PR=0.81, ISR=0.337). Need matched random control at same β to confirm\n    ISR signal vs noise.'\n  registry_id: plan018-additive-random-b01-s43-r3\n  status: DONE\n  conclusion: negative\n  metrics:\n    prove_rate: 0.94\n    n_proved: 94\n    n_problems: 100\n    mean_isr: 0.1406\n    isr_std: null\n    proved_only_isr: 0.1495\n    h7_count: 36\n    h7_rate: 0.383\n    h7a_count: 36\n    h7b_count: 0\n    h1_count: 56\n    h1_rate: 0.596\n    h8_count: 1\n    h8_rate: 0.011\n    genuine_count: 1\n    genuine_rate: 0.0106\n    train_prove_rate: 0.5825\n    train_mean_isr: 0.1266\n    taxonomy_tool: classify_h7.py + manual subtype analysis (2026-05-15)\n    taxonomy_note: 'D093 H7 subtype: all 36 H7 are H7a (text-match tautology), 0 H7b.\n      single_premise_count=0: Random H7a are multi-premise proofs with embedded tautological\n      premise, structurally different from exec-only H7a (single-premise minimal tautology).\n      H7b confirmed absent in Random condition.'\n    h7a_structural_note: Random H7a = multi-premise with embedded matching premise;\n      exec-only H7a = single-premise P-therefore-P\n- id: plan_019\n  claim: 1\n  description: Incorporate existing s45/s46 exec-only 500-step data into paper. Registry\n    shows s45 (PR=99%, genuine=1.0%, TS=93.9%) and s46 (PR=93%, genuine=9.7%, CE=89.2%).\n    Both confirm ≥90% structural degeneration, extending C1 evidence from N=3 to N=5\n    with zero additional GPU cost.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  notes: 'Reviewer strategic assessment: these seeds already exist in registry but\n    were omitted from paper. Pure writing/analysis task.'\n  status: planned\n- id: plan_020\n  claim: 1\n  description: Extend s45 and s46 exec-only training from 500 to 1000 steps. Validates\n    ISR collapse trajectory (0.6423→0.1324→0.0027) generalizes across all 5 seeds,\n    not just s42. Strengthens \"degeneration worsens with training\" claim with N=3\n    trajectory seeds (s42+s45+s46).\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - plan_019\n  notes: 'Reviewer priority #2. Each seed ~3h on RTX PRO 6000.'\n  status: planned\n- id: plan_021\n  claim: 1\n  description: Qwen3-8B exec-only GRPO, 3 seeds (s42/s43/s44), 500 steps, K=8. Cross-scale\n    validation of structural degeneration. If 8B also shows ≥80% hacking → \"degeneration\n    is not 4B-scale-specific\". Different hacking mode distribution is also informative\n    (scale-dependent taxonomy). 98GB GPU can handle 8B GRPO.\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  notes: 'Reviewer priority #3. Replaces old plan_011 (out-of-scope). 8B GRPO ~4h/seed\n    on RTX PRO 6000 (98GB). Disk constraint: need ~32GB free, currently only 20GB\n    — must clean old checkpoints first.'\n  status: planned\n- id: plan_022\n  claim: 2\n  description: Additional ISR β=0.1 seeds (s47/s48/s49) for Qwen3-4B. Extends bimodality\n    characterization from N=5 to N=8. Better precision on 3/5 vs 2/5 gaming-vs-genuine\n    split. Enables bootstrapped CI.\n  priority: P1\n  gpu_budget_hours: 5\n  deps: []\n  notes: 'Reviewer priority #4. ~1.5h/seed.'\n  status: planned\n- id: plan_023\n  claim: 2\n  description: Qwen3-8B ISR β=0.1, 3 seeds. Cross-scale Goodhart validation. Only\n    execute if plan_021 shows degeneration (positive). Tests whether compositional\n    Goodhart effect transfers across model scales.\n  priority: P2\n  gpu_budget_hours: 12\n  deps:\n  - plan_021\n  notes: 'Reviewer: stretch goal, only if plan_021 positive and time permits.'\n  status: planned\n- id: plan_024\n  claim: 1\n  description: Compute premise-count-matched ISR analysis on exec-only outputs (s42-s46).\n    Provides ISR baseline distribution for exec-only condition with premise-count\n    controls, directly responding to reviewer concern about ISR interpretation without\n    controlling for proof complexity.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_019\n  notes: 'Reviewer priority #1. Pure analysis, no GPU. ~1h coding.'\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: sta-phase0-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mean_isr: 0.0641\n    isr_std: 0.1983\n    median_isr: 0\n    isr_range:\n    - 0\n    - 0.889\n    prove_rate: 0.12\n    proved_count: 12\n    total_samples: 100\n    xor_affected_samples: 34\n    effective_prove_rate_no_xor: 0.182\n    avg_time_per_sample_s: 3.4\n    total_runtime_s: 336\n    isr_by_answer:\n      'true':\n        n: 34\n        proved: 9\n        prove_rate: 0.265\n        mean_isr: 0.1345\n      'false':\n        n: 25\n        proved: 1\n        prove_rate: 0.04\n        mean_isr: 0.024\n      unknown:\n        n: 41\n        proved: 2\n        prove_rate: 0.049\n        mean_isr: 0.0302\n- exp_id: sta-gt-isr-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gt_prove_rate: 0.18\n    gt_mean_isr: 0.5588\n    gt_isr_std: 0.2582\n    gt_isr_median: 0.6125\n    solver_execution_rate: 1\n    true_prove_rate: 0.5\n    true_mean_isr: 0.5833\n- exp_id: sta-phase1-exec-only\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-sta-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sta-phase1-exec-only-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.15125\n    mean_isr: 0.1475\n    last20_prove_rate: 0.2\n    last20_isr_mean: 0.2\n    first20_reward_mean: 0.119\n    training_steps: 100\n    training_minutes: 15\n- exp_id: sta-phase1-exec-sta-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.1575\n    mean_isr: 0.1525\n    last20_prove_rate: 0.2125\n    last20_isr_mean: 0.2125\n    first20_reward_mean: 0.119\n    training_steps: 100\n    training_minutes: 15\n- exp_id: sta-phase1-exec-only-r5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.15125\n    mean_isr: 0.1475\n    last20_prove_rate: 0.2\n    last20_isr_mean: 0.2\n    first20_prove_rate: 0.11875\n    first20_isr_mean: 0.11875\n    overall_reward_mean: 0.15125\n    last20_reward_mean: 0.2\n    training_steps: 100\n    training_minutes: 15.7\n    step_time_s: 9.44\n    isr_pr_ratio_last20: 1\n    K: 8\n- exp_id: sta-phase1-exec-sta-r5\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.1\n    mean_isr: 0.04347\n    last20_prove_rate: 0.15\n    last20_isr_mean: 0.04956\n    first20_prove_rate: 0.08125\n    first20_isr_mean: 0.05182\n    overall_reward_mean: 0.07174\n    last20_reward_mean: 0.09978\n    training_steps: 100\n    training_minutes: 16.9\n    step_time_s: 10.13\n    isr_pr_ratio_overall: 0.43\n    isr_pr_ratio_last20: 0.33\n    K: 8\n- exp_id: plan001-exec-only-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan005-sta-low-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 71\n    parse_rate: 1\n    overall_prove_rate: 0.5657\n    overall_isr: 0.1682\n    last50_prove_rate: 0.77\n    last50_isr: 0.2559\n    last100_prove_rate: 0.7725\n    last100_isr: 0.2299\n    last100_loss: 0.022752\n    overall_loss: 0.017296\n    last100_isr_pr_ratio: 0.298\n    last100_isr_lt_pr_count: 99/100\n    first_rolling10_pr_ge_0.8: 178\n    first_rolling10_pr_ge_0.9: 439\n    max_rolling10_pr: 0.9375\n    max_rolling10_isr: 0.3282\n    windowed:\n      1-50:\n        pr: 0.1775\n        isr: 0.0906\n      51-100:\n        pr: 0.1775\n        isr: 0.0835\n      101-200:\n        pr: 0.5062\n        isr: 0.1463\n      201-300:\n        pr: 0.6713\n        isr: 0.1791\n      301-400:\n        pr: 0.7013\n        isr: 0.1984\n      401-500:\n        pr: 0.7725\n        isr: 0.2299\n- exp_id: plan003-eval-exec-only-r5\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.32\n    mean_isr: 0.2055\n    isr_std: 0.3194\n    proved_only_isr: 0.6423\n    isr_by_type:\n      'true': 0.3598\n      'false': 0.1723\n      unknown: 0.0979\n    total_samples: 100\n    proved_count: 32\n    runtime_s: 251.7\n- exp_id: plan001-exec-only-s42-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.93\n    eval_mean_isr: 0.1232\n    eval_isr_std: 0.1887\n    eval_proved_only_isr: 0.1324\n    eval_median_isr: 0\n    eval_n_proved: 93\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    h7_rate: 0\n    h7_count: 0\n    h1_rate: 0.871\n    h1_count: 81\n    h8_conjunction_collapse_count: 6\n    h8_conjunction_collapse_rate: 0.0645\n    genuine_rate: 0.0753\n    genuine_count: 7\n    genuine_mean_isr: 0.3141\n    h1_mean_isr: 0.1055\n    conclusion_embedding_total: 0.871\n    content_independent_predicates_count: 1\n    h8_audit_note: '2026-05-15: H8 conjunction collapse added. genuine 12→7.'\n- exp_id: plan001-exec-only-s42-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan013-random-reward-s42-r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 1\n    eval_mean_isr: 0.535\n    eval_isr_std: 0.1282\n    eval_proved_only_isr: 0.535\n    eval_median_isr: 0.5\n    eval_n_proved: 100\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_note: 'DEGENERATE: model generates trivial 2-component proofs (premise=conclusion,\n      conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure'\n- exp_id: plan001-exec-only-s43-r4\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_sampling_prove_rate: 0.14\n    eval_sampling_mean_isr: 0\n    eval_sampling_n_proved: 14\n    eval_sampling_temperature: 0.7\n    eval_sampling_method: do_sample=True, temperature=0.7\n    eval_sampling_by_answer:\n      'true':\n        count: 34\n        proved: 6\n        prove_rate: 0.176\n      'false':\n        count: 25\n        proved: 2\n        prove_rate: 0.08\n      unknown:\n        count: 41\n        proved: 6\n        prove_rate: 0.146\n    eval_greedy_prove_rate: 0.13\n    eval_greedy_mean_isr: 0\n    eval_greedy_proved_only_isr: 0\n    eval_greedy_n_proved: 13\n    eval_greedy_method: eval_sta.py default (do_sample=False)\n    eval_greedy_by_answer:\n      'true':\n        count: 34\n        proved: 4\n        prove_rate: 0.118\n      'false':\n        count: 25\n        proved: 5\n        prove_rate: 0.2\n      unknown:\n        count: 41\n        proved: 4\n        prove_rate: 0.0976\n    eval_greedy_h7_count: 0\n    eval_greedy_h7_rate: 0\n    eval_greedy_h1_count: 13\n    eval_greedy_h1_rate: 1\n    eval_greedy_genuine_rate: 0\n    eval_greedy_n_premises_proved_mean: 17.92\n    eval_greedy_mean_components_proved: 18.92\n    eval_greedy_n_premises_all_mean: 32.67\n    eval_sampling_h1_rate: 1\n    eval_sampling_h7_rate: 0\n    eval_sampling_genuine_rate: 0\n    eval_sampling_mean_components_proved: 18.5\n    eval_greedy_vs_sampling_delta_pr: -0.01\n    eval_method_note: Greedy and sampling agree on failure profile (ISR*=0, H1=100%,\n      components~18.5-18.9). s43 collapse is decoding-invariant.\n- exp_id: plan002-additive-b03-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    total_steps: 500\n    duration_min: 56.7\n    overall_prove_rate: 0.34025\n    overall_isr: 0.11527\n    last100_prove_rate: 0.5525\n    eval_prove_rate: 0.18\n    eval_mean_isr: 0.0257\n    eval_isr_std: 0.0742\n    eval_median_isr: 0\n    eval_proved_only_isr: 0.1427\n    eval_n_proved: 18\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    h7_rate: 0\n    h7_count: 0\n    h1_rate: 0.778\n    h1_count: 14\n    h8_conjunction_collapse_count: 3\n    h8_conjunction_collapse_rate: 0.1667\n    genuine_rate: 0.0556\n    genuine_count: 1\n    eval_by_type_false_pr: 0.12\n    eval_by_type_false_isr: 0.0102\n    eval_by_type_unknown_pr: 0.195\n    eval_by_type_unknown_isr: 0.0422\n    eval_by_type_true_pr: 0.206\n    eval_by_type_true_isr: 0.0172\n    h8_audit_note: '2026-05-15: H8 conjunction collapse added. genuine 4→1.'\n- exp_id: plan017-additive-random-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.48\n    eval_mean_isr: 0.0453\n    eval_isr_std: 0.0759\n    eval_median_isr: 0\n    eval_max_isr: 0.2857\n    eval_proved_only_isr: 0.0943\n    eval_n_proved: 48\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 9.6\n    eval_component_count_2_ratio: 0\n    tautological_collapse: false\n    h7_count: 4\n    h7_rate: 0.0833\n    h7a_count: 4\n    h7b_count: 0\n    h1_count: 44\n    h1_rate: 0.9167\n    h8_count: 0\n    h8_rate: 0\n    genuine_count: 0\n    genuine_rate: 0\n    taxonomy_tool: classify_h7.py standard (2026-05-15)\n    taxonomy_note: 'Re-classified with current classify_h7.py. Old values: H7=0, H1=48,\n      genuine=0. New: H7=4 (4 H7a text-match tautologies reclassified from H1), H1=44,\n      H8=0, genuine=0.'\n- exp_id: plan014-downstream-nli-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    overall_accuracy: 0.341\n    proved_rate: 0.915\n    proved_count: 732\n    total_generations: 800\n    parse_errors: 0\n    accuracy_by_label:\n      'true': 0.912\n      'false': 0\n      unknown: 0.076\n    spearman_rho: -0.049\n    spearman_p: 0.187\n    mann_whitney_U: 17202\n    mann_whitney_p: 0.288\n    bon_isr_accuracy: 0.35\n    bon_random_accuracy: 0.341\n    bon_oracle_accuracy: 0.44\n    bon_prove_first_accuracy: 0.35\n    isr_bucket_high_acc: 0.75\n    isr_bucket_mid_acc: 0.377\n    isr_bucket_low_acc: 0.327\n    runtime_inference_s: 408.8\n    runtime_eval_s: 13.6\n- exp_id: plan001-exec-only-s44\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.98\n    eval_mean_isr: 0.57\n    eval_isr_std: 0.2013\n    eval_median_isr: 0.5\n    eval_proved_only_isr: 0.5816\n    eval_n_proved: 98\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 2.04\n    eval_component_count_2: 94\n    eval_component_count_3: 4\n    tautological_collapse: true\n    h7_rate: 1\n    h7_count: 97\n    h1_rate: 0\n    h1_count: 0\n    genuine_rate: 0\n    genuine_count: 0\n    conclusion_embedding_total: 1\n- exp_id: plan002-additive-b01-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.81\n    eval_mean_isr: 0.3365\n    eval_isr_std: 0.3227\n    eval_proved_only_isr: 0.4154\n    eval_median_isr: 0.2\n    eval_n_proved: 81\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_component_count_mean: 5.58\n    h7_rate: 0.16\n    h7_count: 13\n    h1_rate: 0.519\n    h1_count: 42\n    h8_conjunction_collapse_count: 12\n    h8_conjunction_collapse_rate: 0.148\n    genuine_rate: 0.173\n    genuine_count: 14\n    tautological_collapse: false\n    h8_audit_note: '2026-05-15: H8 conjunction collapse audit completed. 12/81 proved\n      samples are H8. Genuine 26→14 (32.1%→17.3%). H8 JSON at /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json'\n- exp_id: plan016-extended-1000-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_proved_only_isr: 0.0028\n    eval_mean_isr: 0.0027\n    eval_isr_std: 0.0118\n    eval_median_isr: 0\n    eval_max_isr: 0.0588\n    eval_prove_rate: 0.96\n    eval_n_proved: 96\n    eval_n_total: 100\n- exp_id: plan018-additive-random-b01-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.79\n    eval_mean_isr: 0.1038\n    eval_isr_std: 0.1369\n    eval_median_isr: 0.0357\n    eval_proved_only_isr: 0.1314\n    eval_n_proved: 79\n    eval_n_problems: 100\n    tautological_collapse: false\n    h7_count: 0\n    h7_rate: 0\n    h7a_count: 0\n    h7b_count: 0\n    h1_count: 58\n    h1_rate: 0.7342\n    h8_count: 4\n    h8_rate: 0.0506\n    genuine_count: 18\n    genuine_rate: 0.2278\n    taxonomy_tool: classify_h7.py standard (2026-05-15)\n    taxonomy_note: 'Re-classified with current classify_h7.py. Old values: genuine_strict=12\n      (H1_exact=56, H1_near=8, H8=3). New standard: H1=58 (2 former H1-near now H1),\n      H8=4, genuine=18. Standard definition: proved - H7 - H1 - H8.'\n- exp_id: plan006-prolog-exec-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.83\n    eval_mean_isr: 0.031\n    eval_proved_only_isr: 0.037\n    eval_median_isr: 0\n    eval_max_isr: 0.2\n    eval_isr_std: 0.0534\n    h7_rate: 0\n    h1_rate: 0\n    isr_1_rate: 0\n    single_premise_rate: 0\n    by_answer_type:\n      'true':\n        proved: 37\n        count: 40\n        pr: 0.925\n        isr: 0.037\n      'false':\n        proved: 21\n        count: 29\n        pr: 0.724\n        isr: 0.038\n      unknown:\n        proved: 25\n        count: 31\n        pr: 0.806\n        isr: 0.016\n- exp_id: plan006-prolog-exec-s43\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan006-prolog-exec-s44\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.21\n    eval_mean_isr: 0.0812\n    eval_isr_std: 0.2343\n    eval_median_isr: 0\n    eval_proved_only_isr: 0.3866\n    eval_min_isr: 0\n    eval_max_isr: 1\n    eval_n_proved: 21\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_elapsed_seconds: 683.9\n    eval_by_type_false_pr: 0.04\n    eval_by_type_false_isr: 0.04\n    eval_by_type_unknown_pr: 0.317\n    eval_by_type_unknown_isr: 0.099\n    eval_by_type_true_pr: 0.206\n    eval_by_type_true_isr: 0.09\n    solver: PrologSolver\n    logic_type: prolog\n- exp_id: plan002-additive-b01-s43\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.61\n    eval_n_proved: 61\n    eval_n_problems: 100\n    eval_proved_only_isr: 0.83\n    h7_count: 59\n    h7_rate: 0.9672\n    h1_count: 0\n    h1_rate: 0\n    h1_near_count: 0\n    h1_near_rate: 0\n    h8_conjunction_collapse_count: 0\n    h8_conjunction_collapse_rate: 0\n    genuine_count: 2\n    genuine_rate: 0.0328\n    proved_single_premise_ratio: 1\n    taxonomy_note: 'structurally determined: proved_single_premise_ratio=1.0, all\n      taxonomy categories except H7 are zero by construction. eval file lost but classification\n      derivable from structure.'\n- exp_id: plan002-additive-b01-s44\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.89\n    eval_mean_isr: 0.803\n    eval_isr_std: null\n    eval_proved_only_isr: 0.902\n    eval_n_proved: 89\n    eval_n_problems: 100\n    h7_count: 89\n    h7_rate: 1\n    h1_count: 0\n    h1_rate: 0\n    h8_conjunction_collapse_count: 0\n    h8_conjunction_collapse_rate: 0\n    genuine_count: 0\n    genuine_rate: 0\n    component_mean: 4.33\n    comp_2_ratio: 0.022\n    h7_fn_correction: '12 former genuine reclassified as H7: all n_prem=1 false negatives\n      (normalization mismatch prevented conclusion matching)'\n- exp_id: plan018-additive-random-b01-s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan018-additive-random-b01-s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.89\n    mean_isr: 0.0619\n    isr_std: 0.1756\n    median_isr: 0\n    proved_only_mean_isr: 0.0695\n    n_proved: 89\n    n_problems: 100\n    max_isr: 1\n    min_isr: 0\n    isr_pr_ratio: 0.0695\n    isr_zero_count: 72\n    isr_one_count: 2\n    by_answer_type:\n      'false':\n        count: 25\n        proved: 21\n        prove_rate: 0.84\n        mean_isr: 0.0533\n      unknown:\n        count: 41\n        proved: 40\n        prove_rate: 0.976\n        mean_isr: 0.0892\n      'true':\n        count: 34\n        proved: 28\n        prove_rate: 0.824\n        mean_isr: 0.0353\n    elapsed_seconds: 1012.7\n    eval_method: eval_sta.py with Prover9Solver, FOL\n- exp_id: plan012-hacking-taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    isr_b01_genuine_rate: 0.259\n    random_b01_genuine_rate: 0.177\n    genuine_rate_delta_pp: 8.2\n    isr_b01_conclusion_embedding_rate: 0.728\n    random_b01_conclusion_embedding_rate: 0.785\n    isr_b01_genuine_mean_isr: 0.6723\n    random_b01_genuine_mean_isr: 0.3427\n    isr_b01_complexity_wo_utility_rate: 0\n    random_b01_complexity_wo_utility_rate: 0.038\n    isr_b01_hacking_rate: 0.741\n    random_b01_hacking_rate: 0.823\n- exp_id: plan006-prolog-sta-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    cumulative_prove_rate: 0.848\n    cumulative_mean_isr: 0.787\n    final_prove_rate: 1\n    final_isr: 1\n    final_reward: 1\n    saturation_onset_step: 100\n    train_loss: 0.00716\n    training_hours: 0.78\n    final_entropy: 0.01\n    final_completion_length: 27\n    initial_completion_length: 120\n    steps_at_perfect_reward: 400\n    train_runtime_sec: 2791\n    eval_prove_rate: 0.5\n    eval_mean_isr: 0.5\n    eval_proved_only_isr: 1\n    eval_h7_rate: 1\n    eval_h7_count: 50\n    eval_proved_count: 50\n    eval_total_count: 100\n    eval_n_clauses_mean: 1\n    eval_isr_distribution: 'binary: 50x0 + 50x1'\n- exp_id: plan006-prolog-sta-s43\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    train:\n      final_prove_rate: 0.769\n      final_mean_isr: 0.129\n      final_loss: 0.0155\n      final_entropy: 0.09\n      final_reward: 0.573\n      completion_length_mean: 143\n      train_runtime_seconds: 5095\n      train_runtime_minutes: 84.9\n    eval:\n      n_problems: 100\n      n_proved: 38\n      prove_rate: 0.38\n      mean_isr: 0.0704\n      isr_std: 0.1263\n      median_isr: 0\n      proved_only_mean_isr: 0.1853\n      min_isr: 0\n      max_isr: 1\n      by_answer_type:\n        'false':\n          count: 25\n          proved: 11\n          prove_rate: 0.44\n          mean_isr: 0.1003\n        unknown:\n          count: 41\n          proved: 11\n          prove_rate: 0.268\n          mean_isr: 0.0394\n        'true':\n          count: 34\n          proved: 16\n          prove_rate: 0.471\n          mean_isr: 0.0859\n    h7_classification:\n      h7_strict: 0\n      h7_rate: 0\n      h1_strict: 37\n      h1_rate: 0.974\n      conclusion_in_premise_total: 37\n      conclusion_in_premise_rate: 0.974\n      genuine_count: 0\n      genuine_rate: 0\n      isr_1_count: 1\n      note: 1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause;\n        all 38/38 proved samples are tautological\n- exp_id: plan006-prolog-sta-s44\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    pass_rate: 0.97\n    isr_mean: 0.885\n    isr_n_cl_ge3: N/A (0 samples)\n    n_clauses_dist: 78/100 single-clause, 22/100 two-clause\n    h7_functional_rate: 0.979\n    genuine_rate: 0\n    premise_count_analysis: 100% artifact - zero samples with n_clauses>=3, model\n      exclusively generates 1-2 clause programs\n    failure_mode: query-as-fact gaming (total H7 collapse)\n- exp_id: plan009-sft-baseline-s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: plan009-sft-baseline-s42-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan009-sft-baseline-s42-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan009-sft-baseline-s42-r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.14\n    eval_mean_isr: 0.08\n    eval_isr_std: 0.214\n    eval_median_isr: 0\n    eval_max_isr: 0.833\n    eval_proved_only_isr: 0.571\n    eval_n_proved: 14\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    train_final_loss: 0.0287\n    train_token_accuracy: 0.9935\n    train_epochs: 7.94\n    train_runtime_sec: 789.6\n    by_answer_type:\n      'true':\n        count: 34\n        proved: 13\n        pr: 0.382\n        isr: 0.226\n      unknown:\n        count: 41\n        proved: 1\n        pr: 0.024\n        isr: 0.008\n      'false':\n        count: 25\n        proved: 0\n        pr: 0\n        isr: 0\n    h7_rate: 0\n    h7_count: 0\n    h1_rate: 0.071\n    h1_count: 1\n    genuine_rate: 0.929\n    genuine_count: 13\n    hacking_patterns: near-zero (1/14 H1, 0 H7, 92.9% genuine)\n    tautological_collapse: false\n- exp_id: plan006-prolog-exec-s43-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan006-prolog-exec-s43-r3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.56\n    eval_mean_isr: 0.0084\n    eval_isr_std: 0.0221\n    eval_median_isr: 0\n    eval_proved_only_isr: 0.015\n    eval_min_isr: 0\n    eval_max_isr: 0.1\n    eval_n_proved: 56\n    eval_n_problems: 100\n    eval_method: eval_sta.py full STA\n    eval_data: proofwriter_fol_100.jsonl\n    eval_elapsed_seconds: 868.2\n    eval_by_type_false_pr: 0.48\n    eval_by_type_false_isr: 0.0043\n    eval_by_type_unknown_pr: 0.6585\n    eval_by_type_unknown_isr: 0.0114\n    eval_by_type_true_pr: 0.5\n    eval_by_type_true_isr: 0.0078\n    solver: PrologSolver\n    logic_type: prolog\n- exp_id: plan018-additive-random-b01-s43-r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    h7_rate: 0\n    h7_count: 0\n    h1_rate: 93.2\n    h1_count: 82\n    genuine_rate: 6.8\n    genuine_count: 6\n    eval_prove_rate: 0.88\n    eval_mean_isr: 0.058\n- exp_id: exp1-isr-b03-s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.91\n    mean_isr: 0.2575\n    isr_std: 0.2363\n    median_isr: 0.3333\n    proved_only_mean_isr: 0.283\n    hacking_rate_strict_h7: 0.022\n    hacking_rate_functional: 0.3297\n    genuine_rate: 0.6703\n    genuine_count: 61\n    n_proved: 91\n    n_problems: 100\n    h1_conclusion_in_premise: 0.747\n    eval_data: test_100.jsonl\n    eval_output: /root/autodl-tmp/outputs/eval_sta_exp1_isr_b03_s43.json\n- exp_id: exp1-random-b03-s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    parse_rate: 1\n    prove_rate: 0.79\n    mean_isr: 0.1745\n    isr_std: 0.1628\n    median_isr: 0.1667\n    proved_only_mean_isr: 0.2209\n    hacking_rate_strict_h7: 0\n    hacking_rate_functional: 0.1013\n    genuine_rate: 0.8987\n    genuine_count: 71\n    n_proved: 79\n    n_problems: 100\n    h1_conclusion_in_premise: 0.759\n    eval_data: test_100.jsonl\n    eval_output: /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43.json\n- exp_id: exp1-isr-b03-s44\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp1-random-b03-s44\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp2-exec-s43-greedy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp4-100step-h1h7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp1-isr-b03-s43-r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp1-isr-b03-s44-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.95\n    mean_isr: 0.705\n    isr_std: 0.172\n    proved_only_isr: 0.7421\n    n_proved: 95\n    n_problems: 100\n    h7_rate: 1\n    h7_count: 95\n    h1_rate: 0\n    h1_count: 0\n    genuine_rate: 0\n    genuine_count: 0\n    single_premise_rate: 1\n    eval_data: proofwriter_fol_100.jsonl\n    eval_note: Re-eval with correct test set (D062). Previous test_100.jsonl results\n      invalidated.\n- exp_id: exp1-random-b03-s44-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.23\n    eval_proved_only_mean_isr: 0\n    eval_mean_isr: 0\n    eval_isr_std: 0\n    eval_median_isr: 0\n    eval_n_proved: 23\n    eval_n_problems: 100\n    eval_data: proofwriter_fol_100.jsonl\n    h7_count: 0\n    h7_rate: 0\n    h7a_count: 0\n    h7b_count: 0\n    h1_count: 23\n    h1_rate: 1\n    h8_count: 0\n    h8_rate: 0\n    genuine_count: 0\n    genuine_rate: 0\n    taxonomy_tool: classify_h7.py standard (2026-05-15)\n    taxonomy_note: 'Re-classified with current classify_h7.py. Matches previous values:\n      H7=0, H1=23, H8=0, genuine=0. No change.'\n- exp_id: exp1-isr-b03-s43-r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    h8_audit_done: true\n    h8_in_genuine: 1\n    h8_sample: folio_558\n    body_paren_h7_misses:\n    - folio_732\n    - folio_959\n    genuine_pre_audit: 23\n    genuine_post_full_audit: 20\n    genuine_rate_corrected: 0.233\n    audit_breakdown: 23 - 1(H8 folio_558) - 1(H7 folio_732) - 1(H7 folio_959) = 20\n- exp_id: plan015-linear-s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp1-isr-b03-s43-r4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp1-random-b03-s43-r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp1-random-b03-s43-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp1-random-b03-s43-r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_step: 500\n    prove_rate: 0.5505\n    mean_isr: 0.1358\n    parse_rate: 1\n    train_loss: 0.01365\n    train_runtime_sec: 6161.1\n    epoch: 2\n    eval_prove_rate: 0.92\n    eval_mean_isr: 0.1659\n    eval_isr_std: 0.1147\n    eval_median_isr: 0.1429\n    eval_proved_only_mean_isr: 0.1803\n    eval_min_isr: 0\n    eval_max_isr: 0.5\n    eval_n_proved: 92\n    eval_n_problems: 100\n    eval_data: proofwriter_fol_100.jsonl\n    eval_by_answer_type:\n      'false':\n        count: 25\n        proved: 23\n        prove_rate: 0.92\n        mean_isr: 0.156\n      unknown:\n        count: 41\n        proved: 37\n        prove_rate: 0.902\n        mean_isr: 0.184\n      'true':\n        count: 34\n        proved: 32\n        prove_rate: 0.941\n        mean_isr: 0.151\n    h7_count: 7\n    h7_rate: 0.076\n    h7a_count: 7\n    h7b_count: 0\n    h1_count: 82\n    h1_rate: 0.891\n    h8_count: 0\n    h8_rate: 0\n    genuine_count: 3\n    genuine_rate: 0.0326\n    taxonomy_tool: classify_h7.py standard (2026-05-15)\n    taxonomy_note: 'Re-classified with current classify_h7.py. Matches previous strict\n      values: H7=7, H1=82, H8=0, genuine=3. No change.'\n- exp_id: plan004-o1-ablation-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    prove_rate: 0.63\n    mean_isr: 0.0072\n    h7_count: 0\n    h7_rate: 0\n    h1_count: 63\n    h1_rate: 1\n    h8_conjunction_collapse_count: 2\n    h8_conjunction_collapse_rate: 0.0317\n    genuine_count: 0\n    genuine_rate: 0\n    content_independent_predicates_count: 3\n    h8_audit_note: '2026-05-15: H8 conjunction collapse added. genuine unchanged (0).'\n- exp_id: plan002-additive-b01-s42-1000\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.9\n    eval_mean_isr: 0.7892\n    eval_isr_std: 0.3424\n    eval_proved_only_isr: 0.8769\n    eval_median_isr: 1\n    eval_n_proved: 90\n    eval_n_problems: 100\n    eval_component_count_mean: 2.889\n    tautological_collapse: true\n    train_final_prove_rate: 0.855\n    train_final_mean_isr: 0.532\n    h7_count: 87\n    h7_rate: 0.9667\n    h1_count: 0\n    h1_rate: 0\n    h1_near_count: 1\n    h1_near_rate: 0.0111\n    h8_conjunction_collapse_count: 1\n    h8_conjunction_collapse_rate: 0.0111\n    genuine_count: 2\n    genuine_rate: 0.0222\n    taxonomy_standard: D086 clean run = ground truth. D084 residual removed.\n- exp_id: plan009-sft-baseline-s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.2391\n    train_token_accuracy: 0.9938\n    train_epochs: 7.94\n    train_runtime_sec: 677.14\n    train_steps: 500\n    eval_prove_rate: 0.15\n    eval_mean_isr: 0.0895\n    eval_isr_std: 0.2338\n    eval_median_isr: 0\n    eval_proved_only_isr: 0.5967\n    h7_count: 0\n    h7_rate: 0\n    h1_count: 1\n    h1_rate: 0.067\n    genuine_count: 14\n    genuine_rate: 0.933\n    by_answer_type:\n      'true':\n        count: 34\n        proved: 13\n        prove_rate: 0.382\n        mean_isr: 0.234\n      'false':\n        count: 25\n        proved: 1\n        prove_rate: 0.04\n        mean_isr: 0.027\n      unknown:\n        count: 41\n        proved: 1\n        prove_rate: 0.024\n        mean_isr: 0.008\n    eval_data_path: data/proofwriter_fol_100.jsonl\n    eval_output_path: /root/autodl-tmp/outputs/eval_sta_plan009_sft_s43.json\n- exp_id: plan018-additive-random-b01-s42-1000\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan009-sft-baseline-s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_final_loss: 0.2397\n    train_last_step_loss: 0.0328\n    train_token_accuracy: 0.9928\n    train_epochs: 7.94\n    train_runtime_sec: 729.05\n    train_steps: 500\n    eval_prove_rate: 0.17\n    eval_n_proved: 17\n    eval_n_problems: 100\n    eval_mean_isr: 0.0974\n    eval_isr_std: 0.2409\n    eval_median_isr: 0\n    eval_proved_only_isr: 0.5729\n    eval_data: proofwriter_fol_100.jsonl\n    eval_method: eval_sta.py full STA\n    eval_output_path: /root/autodl-tmp/outputs/eval_sta_plan009_sft_s44.json\n    eval_tautological_collapse: false\n    eval_h7_count: 0\n    eval_h7_rate: 0\n    eval_h1_count: 2\n    eval_h1_rate: 0.118\n    eval_genuine_count: 15\n    eval_genuine_rate: 0.882\n    eval_by_answer_type:\n      'true':\n        count: 34\n        proved: 15\n        prove_rate: 0.441\n        mean_isr: 0.257\n      'false':\n        count: 25\n        proved: 1\n        prove_rate: 0.04\n        mean_isr: 0.027\n      unknown:\n        count: 41\n        proved: 1\n        prove_rate: 0.024\n        mean_isr: 0.008\n    eval_correction_note: 'Corrected 2026-05-15: previous eval used test_100.jsonl\n      (50/44/6 distribution), re-evaled with proofwriter_fol_100.jsonl (34/25/41)'\n- exp_id: exp1-isr-b03-s42-1000\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp1-isr-b03-s42-1000-r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.95\n    eval_mean_isr: 0.734\n    eval_isr_std: 0.2575\n    eval_median_isr: 0.6\n    eval_proved_only_isr: 0.7726\n    eval_n_proved: 95\n    eval_n_problems: 100\n    eval_data: proofwriter_fol_100.jsonl\n    eval_by_answer_type:\n      'false':\n        count: 25\n        proved: 25\n        prove_rate: 1\n        mean_isr: 0.824\n      unknown:\n        count: 41\n        proved: 38\n        prove_rate: 0.927\n        mean_isr: 0.673\n      'true':\n        count: 34\n        proved: 32\n        prove_rate: 0.941\n        mean_isr: 0.741\n    h7_count: 0\n    h7_rate: 0\n    h1_count: 54\n    h1_rate: 0.568\n    genuine_count: 0\n    genuine_rate: 0\n    tautological_collapse: true\n    isr_1_count: 41\n    isr_1_rate: 0.432\n    single_premise_count: 0\n    train_final_prove_rate: 0.829\n    train_final_mean_isr: 0.727\n    train_loss: 0.0041\n    train_runtime_seconds: 6280\n    train_final_entropy: 9.0e-06\n    completions_mean_length: 47\n    h8_conjunction_collapse_count: 41\n    h8_conjunction_collapse_rate: 0.432\n    content_independent_predicates: true\n- exp_id: plan018-additive-random-b01-s42-1000-r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    train_final_prove_rate: 0.989\n    train_final_mean_isr: 0.353\n    train_final_reward: 1.062\n    train_steps: 1000\n    train_runtime_seconds: 2957\n    eval_prove_rate: 1\n    eval_mean_isr: 0.3333\n    eval_isr_std: 0\n    eval_median_isr: 0.3333\n    eval_proved_only_isr: 0.3333\n    eval_n_proved: 100\n    eval_n_problems: 100\n    eval_component_count_mean: 3\n    genuine_rate: 0\n    genuine_count: 0\n    tautological_collapse: true\n    h7_rate: null\n    h7_count: null\n    h1_rate: null\n    h1_count: null\n- exp_id: plan018-additive-random-b01-s42-1000-r3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.97\n    eval_mean_isr: 0.6892\n    eval_isr_std: 0.2037\n    eval_median_isr: 0.75\n    eval_proved_only_isr: 0.7105\n    eval_n_proved: 97\n    eval_n_problems: 100\n    genuine_count: 0\n    genuine_rate: 0\n    h1_count: 0\n    h1_rate: 0\n    h7_count: 97\n    h7_rate: 1\n    tautological_collapse: true\n    train_final_prove_rate: 0.827\n    train_final_mean_isr: 0.5213\n    train_loss: 0.00671\n    train_final_entropy: 0.003\n    train_runtime_seconds: 5783\n    train_steps: 1000\n    eval_by_answer_type:\n      'false':\n        count: 25\n        proved: 25\n        prove_rate: 1\n        mean_isr: 0.7533\n      unknown:\n        count: 41\n        proved: 39\n        prove_rate: 0.951\n        mean_isr: 0.6565\n      'true':\n        count: 34\n        proved: 33\n        prove_rate: 0.971\n        mean_isr: 0.6814\n    n_premise_distribution:\n      '1': 97\n    pattern_description: 'All 97 proved: 1 premise identical to conclusion (P therefore\n      P). D088 correction: h7=97 h1=0 (was h1=97 h7=0 pre-D086 bugfix).'\n- exp_id: plan009-sft-baseline-s42-1000\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_final_loss: 0.0168\n    train_last_step_loss: 0.0168\n    train_token_accuracy: 0.9955\n    train_epochs: 15.88\n    train_runtime_sec: 1415\n    train_steps: 1000\n    eval_prove_rate: 0.13\n    eval_n_proved: 13\n    eval_n_problems: 100\n    eval_mean_isr: 0.0738\n    eval_isr_std: 0.2077\n    eval_median_isr: 0\n    eval_proved_only_isr: 0.5677\n    eval_data: proofwriter_fol_100.jsonl\n    eval_method: eval_sta.py full STA\n    eval_output_path: /root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json\n    h7_strict_count: 0\n    h7_strict_rate: 0\n    h1_strict_count: 1\n    h1_strict_rate: 0.0769\n    h8_conjunction_collapse_count: 0\n    h8_conjunction_collapse_rate: 0\n    genuine_count: 12\n    genuine_rate: 0.9231\n    conclusion_in_premise_count: 1\n    conclusion_in_premise_rate: 0.0769\n    isr_1_count: 0\n    content_independent_count: 0\n    eval_by_answer_type:\n      'true':\n        count: 34\n        proved: 12\n        prove_rate: 0.353\n        mean_isr: 0.209\n      'false':\n        count: 25\n        proved: 1\n        prove_rate: 0.04\n        mean_isr: 0.011\n      unknown:\n        count: 41\n        proved: 0\n        prove_rate: 0\n        mean_isr: 0\n- exp_id: plan009-sft-baseline-s43-1000\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.11\n    n_proved: 11\n    n_problems: 100\n    mean_isr: 0.0699\n    isr_std: 0.2155\n    median_isr: 0\n    proved_only_mean_isr: 0.6352\n    by_answer_type:\n      'true':\n        count: 34\n        proved: 11\n        prove_rate: 0.3235\n      'false':\n        count: 25\n        proved: 0\n        prove_rate: 0\n      unknown:\n        count: 41\n        proved: 0\n        prove_rate: 0\n    genuine_count: 10\n    genuine_rate: 0.9091\n    h7_strict_count: 0\n    h7_strict_rate: 0\n    h1_strict_count: 1\n    h1_strict_rate: 0.0909\n    h8_conjunction_collapse_count: 0\n    h8_conjunction_collapse_rate: 0\n    conclusion_in_premise_count: 1\n    conclusion_in_premise_rate: 0.0909\n    content_independent_count: 0\n    content_independent_rate: 0\n    isr_1_count: 1\n    isr_1_rate: 0.0909\n    train_final_loss: 0.0167\n    train_avg_loss: 0.1551\n    train_token_accuracy: 0.9954\n    train_runtime_s: 1584.79\n    eval_elapsed_s: 326.1\n- exp_id: plan009-sft-baseline-s44-1000\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.15\n    n_proved: 15\n    n_problems: 100\n    mean_isr: 0.0884\n    isr_std: 0.2268\n    median_isr: 0\n    proved_only_mean_isr: 0.5892\n    max_isr: 0.8571\n    by_answer_type:\n      'true':\n        count: 34\n        proved: 15\n        prove_rate: 0.4412\n      'false':\n        count: 25\n        proved: 0\n        prove_rate: 0\n      unknown:\n        count: 41\n        proved: 0\n        prove_rate: 0\n    genuine_count: 14\n    genuine_rate: 0.9333\n    h7_strict_count: 0\n    h7_strict_rate: 0\n    h1_strict_count: 1\n    h1_strict_rate: 0.0667\n    h8_conjunction_collapse_count: 0\n    h8_conjunction_collapse_rate: 0\n    conclusion_in_premise_count: 1\n    conclusion_in_premise_rate: 0.0667\n    content_independent_count: 0\n    content_independent_rate: 0\n    isr_1_count: 0\n    isr_1_rate: 0\n    train_final_loss: 0.0171\n    train_avg_loss: 0.1544\n    train_token_accuracy: 0.995\n    train_runtime_s: 1580.97\n    eval_elapsed_s: 391.8\n- exp_id: plan009-sft-baseline-s44-1000-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan009-sft-baseline-s44-1000-r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.15\n    eval_n_proved: 15\n    eval_n_problems: 100\n    eval_mean_isr: 0.0884\n    eval_isr_std: 0.2268\n    eval_median_isr: 0\n    eval_proved_only_isr: 0.5892\n    eval_data: proofwriter_fol_100.jsonl\n    eval_method: eval_sta.py full STA\n    h7_count: 0\n    h7_rate: 0\n    h1_count: 1\n    h1_rate: 0.0667\n    h8_conjunction_collapse_count: 0\n    h8_conjunction_collapse_rate: 0\n    genuine_count: 14\n    genuine_rate: 0.9333\n    eval_by_answer_type:\n      'true':\n        count: 34\n        proved: 15\n        prove_rate: 0.441\n        mean_isr: 0.26\n      'false':\n        count: 25\n        proved: 0\n        prove_rate: 0\n        mean_isr: 0\n      unknown:\n        count: 41\n        proved: 0\n        prove_rate: 0\n        mean_isr: 0\n- exp_id: plan001-exec-only-s43-1000\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s44-1000\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan001-exec-only-s43-1000-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.9\n    n_proved: 90\n    n_problems: 100\n    mean_isr: 0.531\n    isr_std: 0.15\n    isr_corrected: 0.465\n    isr_artifact_note: n_components=3 quantifier decomposition artifact (+0.066) +\n      $T solver bug 5 samples (+0.025). Corrected ISR=0.465, but both values entirely\n      from H7a tautological necessity, no reasoning quality signal.\n    h7_count: 90\n    h7_rate: 1\n    h7a_count: 90\n    h7b_count: 0\n    h1_count: 0\n    h1_rate: 0\n    h8_count: 0\n    h8_rate: 0\n    genuine_count: 0\n    genuine_rate: 0\n- exp_id: plan001-exec-only-s44-1000-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 1\n    n_proved: 100\n    n_problems: 100\n    mean_isr: 0.002\n    isr_std: 0.0146\n    h7_count: 0\n    h7_rate: 0\n    h7a_count: 0\n    h7b_count: 0\n    h1_count: 85\n    h1_rate: 0.85\n    h8_count: 15\n    h8_rate: 0.15\n    genuine_count: 0\n    genuine_rate: 0\n    genuine_note: 'D091: 3 samples escape text-match classifiers but are functionally\n      degenerate (ISR=0, disjunctive/commuted bypasses)'\n- exp_id: plan018-additive-random-b01-s43-r3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    prove_rate: 0.94\n    n_proved: 94\n    n_problems: 100\n    mean_isr: 0.1406\n    isr_std: null\n    proved_only_isr: 0.1495\n    h7_count: 36\n    h7_rate: 0.383\n    h7a_count: 36\n    h7b_count: 0\n    h1_count: 56\n    h1_rate: 0.596\n    h8_count: 1\n    h8_rate: 0.011\n    genuine_count: 1\n    genuine_rate: 0.0106\n    train_prove_rate: 0.5825\n    train_mean_isr: 0.1266\n    taxonomy_tool: classify_h7.py + manual subtype analysis (2026-05-15)\n    taxonomy_note: 'D093 H7 subtype: all 36 H7 are H7a (text-match tautology), 0 H7b.\n      single_premise_count=0: Random H7a are multi-premise proofs with embedded tautological\n      premise, structurally different from exec-only H7a (single-premise minimal tautology).\n      H7b confirmed absent in Random condition.'\n    h7a_structural_note: Random H7a = multi-premise with embedded matching premise;\n      exec-only H7a = single-premise P-therefore-P\n- exp_id: plan018-additive-random-b01-s44-r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    train_prove_rate: 0.64675\n    train_mean_isr: 0.08092\n    train_loss: 0.00937\n    train_steps: 500\n    train_runtime_sec: 4998\n    eval_prove_rate: 0.89\n    eval_mean_isr: 0.0619\n    eval_isr_std: 0.1756\n    eval_median_isr: 0\n    eval_isr_pr_ratio: 0.0695\n    eval_proved_only_isr: 0.0695\n    eval_n_proved: 89\n    eval_n_problems: 100\n    h7_count: 0\n    h7a_count: 0\n    h7b_count: 0\n    h1_count: 73\n    h8_count: 16\n    genuine_count: 6\n    genuine_rate: 0.067\n    h7_rate: 0\n    h1_rate: 0.82\n    h8_rate: 0.18\n    content_independent_count: 18\n- exp_id: plan002-additive-b01-s43-r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_n_problems: 100\n    eval_n_proved: 61\n    eval_prove_rate: 0.61\n    eval_mean_isr: 0.5063\n    eval_isr_std: 0.4518\n    eval_median_isr: 0.5\n    eval_proved_only_isr: 0.8301\n    h7a_count: 59\n    h7b_count: 2\n    h7_count: 61\n    h7_rate: 1\n    h1_count: 0\n    h1_rate: 0\n    h8_conjunction_collapse_count: 0\n    h8_conjunction_collapse_rate: 0\n    genuine_count: 0\n    genuine_rate: 0\n    proved_single_premise_ratio: 1\n    content_independent_predicates: 5\n    isr_eq_1_count: 40\n    isr_eq_1_rate_of_proved: 0.656\n    train_prove_rate: 0.68775\n    train_mean_isr: 0.5039\n- exp_id: sweep-isr-b005-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.55\n    eval_mean_isr: 0.602\n    eval_proved_only_isr: 0.759\n    genuine_rate: 0\n    h7a_rate: 1\n    h7b_rate: 0\n    h1_rate: 0\n    h8_rate: 0\n    h7_count: 55\n    genuine_count: 0\n    n_proved: 55\n    n_total: 100\n- exp_id: sweep-isr-b01-s45\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    prove_rate: 0.2357\n    prove_rate_last50: 0.475\n    isr_mean: 0.1127\n    isr_mean_last50: 0.2172\n    reward_mean: 0.247\n    loss: 0.0106\n    parse_rate: 1\n    steps_completed: 219\n    steps_total: 500\n    kill_reason: SIGKILL exit 137 (system OOM killer)\n    checkpoint: checkpoint-200\n- exp_id: plan002-additive-b01-s45\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.42\n    eval_mean_isr: 0.2542\n    eval_isr_std: 0.3261\n    eval_proved_only_isr: 0.6052\n    eval_median_isr: 0\n    eval_n_proved: 42\n    eval_n_problems: 100\n    h7a_rate: 0.381\n    h7b_rate: 0\n    h7_rate: 0.381\n    h1_rate: 0.048\n    h8_rate: 0.024\n    genuine_count: 23\n    genuine_rate: 0.548\n    genuine_pct_total: 23\n    h7_count: 16\n    h1_count: 2\n    h8_count: 1\n    eval_data: proofwriter_fol_100.jsonl\n    eval_method: eval_sta.py + classify_h7.py\n    taxonomy_standard: C013\n- exp_id: plan002-additive-b01-s46\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.77\n    eval_mean_isr: 0.3164\n    eval_isr_std: 0.2959\n    eval_proved_only_isr: 0.411\n    eval_median_isr: 0.25\n    eval_n_proved: 77\n    eval_n_problems: 100\n    h7a_rate: 0.143\n    h7b_rate: 0\n    h7_rate: 0.143\n    h1_rate: 0.26\n    h8_rate: 0.052\n    genuine_count: 42\n    genuine_rate: 0.545\n    genuine_pct_total: 42\n    h7_count: 11\n    h1_count: 20\n    h8_count: 4\n    eval_data: proofwriter_fol_100.jsonl\n    eval_method: eval_sta.py + classify_h7.py\n    taxonomy_standard: C013\n- exp_id: plan018-additive-random-b01-s45\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.58\n    eval_n_proved: 58\n    eval_n_problems: 100\n    eval_mean_isr: 0.0096\n    eval_proved_only_isr: 0.0166\n    h7_count: 0\n    h7_rate: 0\n    h1_count: 53\n    h1_rate: 0.914\n    h8_count: 0\n    h8_rate: 0\n    genuine_count: 5\n    genuine_rate: 0.086\n    eval_data: proofwriter_fol_100.jsonl\n    eval_method: eval_sta.py + classify_h7.py\n- exp_id: plan018-additive-random-b01-s46\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.94\n    eval_mean_isr: 0.0424\n    h7_count: 86\n    h1_count: 2\n    h8_count: 4\n    genuine_count: 2\n    genuine_rate: 0.021\n- exp_id: plan001-exec-only-s45\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan001-exec-only-s46\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.93\n    mean_isr: 0.083\n    genuine_pct: 9.7\n    h1_pct: 89.2\n    h7_pct: 0\n    h8_pct: 4.3\n    n_proved: 93\n    n_problems: 100\n- exp_id: w2-qwen3-7b-pilot\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: sweep-isr-b005-s43\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.99\n    eval_n_proved: 99\n    eval_n_problems: 100\n    eval_mean_isr: 0.5517\n    eval_isr_std: 0.1597\n    eval_median_isr: 0.5\n    eval_proved_only_isr: 0.5572\n    train_prove_rate: 0.752\n    train_mean_isr: 0.364\n    eval_data: proofwriter_fol_100.jsonl\n    eval_method: eval_sta.py + classify_h7.py\n    h7_count: 96\n    h7_rate: 0.97\n    h7a_count: 96\n    h7b_count: 0\n    h1_count: 0\n    h1_rate: 0\n    h8_count: 0\n    h8_rate: 0\n    genuine_count: 3\n    genuine_rate: 0.03\n- exp_id: sweep-isr-b005-s44\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    prove_rate: 0.99\n    mean_isr: 0.5539\n    isr_std: 0.175\n    median_isr: 0.5\n    H7_rate: 0.869\n    H7_count: 86\n    H1_exact_count: 1\n    H8_count: 2\n    genuine_count: 10\n    genuine_rate: 0.101\n    n_proved: 99\n    n_total: 100\n    train_final_reward: 1.029\n    train_final_prove_rate: 0.7085\n    train_mean_isr: 0.381\n    entropy_final: 0.075\n    eval_data: proofwriter_fol_100.jsonl\n- exp_id: sweep-isr-b02-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 1\n    eval_mean_isr: 0.6017\n    eval_isr_std: 0.1973\n    eval_median_isr: 0.5\n    eval_isr_pr_ratio: 0.6017\n    eval_min_isr: 0.3333\n    eval_max_isr: 1\n    h7a: 100\n    h7b: 0\n    h7_total: 100\n    h1_strict: 0\n    h8: 0\n    genuine: 0\n    genuine_pct: 0\n    content_independent: 99\n    single_premise_pct: 1\n- exp_id: sweep-isr-b02-s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.5998\n    mean_isr: 0.1812\n    train_loss: 0.01294\n    eval_prove_rate: 0.96\n    eval_mean_isr: 0.5298\n    eval_proved_only_isr: 0.5519\n    genuine_rate: 0\n    h7a_rate: 0.969\n    h7b_rate: 0\n    h1_rate: 0.01\n    h8_rate: 0.021\n    steps_completed: 500\n    steps_total: 500\n- exp_id: sweep-isr-b02-s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.7015\n    mean_isr: 0.503\n    train_loss: 0.02009\n    parse_rate: 1\n    steps_completed: 500\n    steps_total: 500\n    train_runtime_sec: 3562\n    frac_reward_zero_std_final: 1\n    entropy_final: 0.041\n    eval_prove_rate: 0.94\n    eval_mean_isr: 0.9058\n    eval_isr_std: 0.2663\n    genuine_rate: 0\n    h7a_rate: 1\n    h7b_rate: 0\n    h1_rate: 0\n    h8_rate: 0\n    single_premise_pct: 1\n    content_independent_pct: 0.043\n    isr_100_pct: 0.925\n- exp_id: sweep-random-b01-s45\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.58\n    eval_n_proved: 58\n    eval_n_problems: 100\n    eval_mean_isr: 0.0096\n    eval_proved_only_isr: 0.0166\n    h7_count: 0\n    h7_rate: 0\n    h1_count: 53\n    h1_rate: 0.914\n    h8_count: 0\n    h8_rate: 0\n    genuine_count: 5\n    genuine_rate: 0.086\n    eval_data: proofwriter_fol_100.jsonl\n    eval_method: eval_sta.py + classify_h7.py\n    source: linked from plan018-additive-random-b01-s45\n- exp_id: sweep-isr-b01-s46\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: sweep-random-b01-s46\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.94\n    eval_n_proved: 94\n    eval_n_problems: 100\n    eval_mean_isr: 0.0424\n    h7_count: 86\n    h7_rate: 0.915\n    h1_count: 2\n    h1_rate: 0.021\n    h8_count: 4\n    h8_rate: 0.043\n    genuine_count: 2\n    genuine_rate: 0.021\n    eval_data: proofwriter_fol_100.jsonl\n    eval_method: eval_sta.py + classify_h7.py\n    source: linked from plan018-additive-random-b01-s46\n- exp_id: sweep-exec-only-s45\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sweep-exec-only-s46\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan018-random-b01-s45-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: plan018-additive-random-b01-s45-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: sweep-exec-only-s45-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.74025\n    mean_isr: 0.3596\n    train_loss: 0.0273\n    parse_rate: 1\n    steps_completed: 500\n    steps_total: 500\n    train_runtime_sec: 3282\n    entropy_final: 0.045\n    eval_prove_rate: 0.99\n    eval_n_proved: 99\n    eval_n_problems: 100\n    eval_mean_isr: 0.5012\n    eval_isr_std: 0.2055\n    eval_median_isr: 0.5\n    eval_proved_only_isr: 0.5062\n    eval_data: proofwriter_fol_100.jsonl\n    eval_by_answer_type:\n      'false':\n        count: 25\n        proved: 25\n        prove_rate: 1\n        mean_isr: 0.59\n      unknown:\n        count: 41\n        proved: 41\n        prove_rate: 1\n        mean_isr: 0.476\n      'true':\n        count: 34\n        proved: 33\n        prove_rate: 0.971\n        mean_isr: 0.467\n    h7a_count: 93\n    h7a_rate: 0.939\n    h7b_count: 0\n    h7_count: 93\n    h7_rate: 0.939\n    h1_count: 5\n    h1_rate: 0.051\n    h8_count: 1\n    h8_rate: 0.01\n    genuine_count: 1\n    genuine_rate: 0.01\n    content_independent_count: 47\n    single_premise_count: 92\n    taxonomy_tool: classify_h7.py standard (2026-05-16)\n- exp_id: w2-qwen3-8b-exec-pilot\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: w2-qwen3-8b-isr-pilot\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: w2-qwen3-8b-exec-pilot-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: w2-qwen3-8b-isr-pilot-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: w2-qwen3-1.7b-exec-pilot\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    prove_rate: 3\n    genuine_rate: 0\n    n_proved: 3\n    n_genuine: 0\n    n_H7a: 3\n    mean_isr: 0.015\n    note: '1.7B exec-only: 3% raw PR but 100% H7a tautology, 0 genuine proofs'\n- exp_id: w2-qwen3-1.7b-isr-pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.93\n    mean_isr: 0.2625\n    isr_std: 0.0752\n    median_isr: 0.2857\n    n_proved: 93\n    n_problems: 100\n    h7_count: 0\n    h7_rate: 0\n    h1_count: 0\n    h1_rate: 0\n    h8_count: 0\n    h8_rate: 0\n    genuine_count: 0\n    genuine_rate: 0\n    h9_count: 93\n    h9_rate: 1\n    mode_collapse: true\n    collapse_onset_step: 463\n    hacking_type: 'H9: ex falso quodlibet / contradiction injection'\n    note: All 93 proofs inject contradictory premises (P(a) ∧ ¬P(a)) using generic\n      predicates. Prover9 proves anything from contradiction. Bypasses H7/H1/H8 detectors.\n      ISR≈2/7 constant. Zero semantic relation to original problems.\n- exp_id: gated-isr-t03-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gated-isr-t03-s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gated-isr-curriculum-t02-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gated-isr-curriculum-t02-s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gated-isr-curriculum-t02-s42-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gated-isr-curriculum-t02-s43-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exec-retrain-for-warmstart-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exec-retrain-v3-s42\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exec-retrain-v3-s43\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: gated-isr-warmstart-t02-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gated-isr-warmstart-t02-s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: gated-isr-warmstart-t02-s43-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.21\n    mean_isr: 0.028\n    n_proved: 21\n    n_problems: 100\n    genuine_pct_raw: 95.2\n    genuine_pct_c013: 76.2\n    genuine_pct_strict: 38.1\n    h7_count: 1\n    h8a_isr0_count: 4\n    h8b_no_premise_nec: 8\n    total_hacking_strict: 13\n    genuine_count_c013: 16\n    genuine_count_strict: 8\n- exp_id: gated-isr-warmstart-t015-s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.41\n    mean_isr: 0.0512\n    mean_isr_proved: 0.1248\n    n_proved: 41\n    n_problems: 100\n    genuine_pct_raw: 97.6\n    genuine_pct_c013: 63.4\n    genuine_pct_strict: 48.8\n    h7_count: 1\n    h8a_isr0_count: 14\n    h8b_no_premise_nec: 6\n    total_hacking_strict: 21\n    genuine_count_c013: 26\n    genuine_count_strict: 20\n- exp_id: w2-qwen3-1.7b-isr-b03\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.17\n    mean_isr: 0.0309\n    n_proved: 17\n    n_problems: 100\n    h7_pct: 0\n    h1_pct: 70.6\n    h8_pct: 0\n    genuine_pct: 29.4\n    genuine_count: 5\n    content_independent: 1\n    strict_genuine_count: 5\n    strict_genuine_pct_proved: 29.4\n    strict_genuine_pct_total: 5\n    h1_near_count: 2\n    strict_genuine_excl_h1near: 3\n    training_collapsed: false\n    audit_note: 'D130 re-audit: 5/5 genuine are content-dependent. 2/5 are H1-near\n      (conjunction reorder, universal instantiation). 3/5 require multi-step reasoning.'\n- exp_id: w2-qwen3-1.7b-random-b01\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.93\n    genuine_pct: 0\n    h9_rate: 1\n    mean_isr: 0.028\n    n_proved: 93\n    n_problems: 100\n- exp_id: w2-qwen3-1.7b-isr-b01\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 1\n    mean_isr: 0.6\n    isr_std: 0\n    n_proved: 100\n    n_problems: 100\n    h7_pct: 0\n    h1_pct: 100\n    h8_pct: 0\n    genuine_pct: 0\n    genuine_count: 0\n- exp_id: exec-only-s43-1000step-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exec-only-s43-1000step-r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exec-only-s43-1000step-r4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exec-only-s43-1000step-r5\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exec-only-s43-1000step-r6\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exec-only-s43-1000step-r7\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_prove_rate: 0.96\n    eval_mean_isr: 0.0818\n    h7_count: 0\n    h1_count: 90\n    h8_count: 0\n    genuine_count: 6\n    genuine_rate: 0.062\n    content_independent: 4\n- exp_id: sweep-random-b005-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0\n    eval_n_proved: 0\n    eval_n_problems: 100\n    eval_mean_isr: 0\n    h7_count: 0\n    h7_rate: 0\n    h1_count: 0\n    h1_rate: 0\n    h8_count: 0\n    h8_rate: 0\n    genuine_count: 0\n    genuine_rate: 0\n    eval_data: proofwriter_fol_100.jsonl\n    eval_method: eval_sta.py + classify_h7.py\n    note: 'Complete training failure: β=0.05 random signal too weak for 500-step learning'\n- exp_id: sweep-random-b005-s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.62\n    eval_n_proved: 62\n    eval_n_problems: 100\n    eval_mean_isr: 0.0058\n    h7_count: 0\n    h7_rate: 0\n    h7a_count: 0\n    h7b_count: 0\n    h1_count: 48\n    h1_rate: 0.774\n    h8_count: 7\n    h8_rate: 0.113\n    genuine_count: 8\n    genuine_rate: 0.129\n    eval_data: proofwriter_fol_100.jsonl\n    eval_method: eval_sta.py + classify_h7.py\n    train_runtime_s: 6998\n    note: β=0.05 random s43 learns (PR=62%) unlike s42 (PR=0%). Hacking mode H1 redundancy\n      (77.4%), not H7 tautology. Huge seed variance at β=0.05.\n- exp_id: sweep-random-b005-s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.07\n    proved: 7\n    total: 100\n    mean_isr: 0\n    isr_std: 0\n    H7: 0\n    H7a: 0\n    H7b: 0\n    H1: 5\n    H8: 2\n    genuine: 0\n    genuine_rate: 0\n- exp_id: plan002-additive-b01-s45-1000\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    prove_rate: 0.02\n    proved: 2\n    total: 100\n    mean_isr: 0.01\n    isr_std: 0.0704\n    H7: 2\n    H7a: 2\n    H7b: 0\n    H1: 0\n    H8: 0\n    genuine: 0\n    genuine_rate: 0\n- exp_id: d129-1.7b-isr-b01-s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.6\n    non_hacking_rate: 0\n    isr_star: 0.75\n    H1_pct: 0\n    H7_pct: 100\n    H8_pct: 0\n    H9_pct: 0\n    genuine_pct: 0\n    dominant_mode: H7a\n    eval_decoding: greedy\n    eval_data: proofwriter_fol_100.jsonl\n    mean_isr: 0.45\n    proved_only_isr: 0.75\n- exp_id: d129-1.7b-isr-b01-s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.82\n    non_hacking_rate: 0.427\n    isr_star: 0.4398\n    H1_pct: 39\n    H7_pct: 0\n    H8_pct: 18.3\n    H9_pct: 0\n    genuine_pct: 42.7\n    dominant_mode: H1(mixed)\n    eval_decoding: greedy\n    eval_data: proofwriter_fol_100.jsonl\n- exp_id: d129-1.7b-random-b01-s43\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: d129-1.7b-random-b01-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: d129-1.7b-isr-b03-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: d129-1.7b-isr-b03-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: d129-1_7b-random-b01-s43-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 1\n    mean_isr: 0.0511\n    isr_std: 0.094\n    H1_pct: 76\n    H7_pct: 0\n    H8_pct: 0\n    genuine_pct: 24\n    content_independent_pct: 100\n    training_steps: 500\n    final_reward: 1.0526\n    train_loss: 0.0372\n- exp_id: d129-1_7b-random-b01-s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 1\n    mean_isr: 0.0072\n    isr_std: 0.0295\n    median_isr: 0\n    H1_pct: 84\n    H7_pct: 0\n    H8_pct: 0\n    genuine_pct: 16\n    content_independent_pct: 100\n    n_problems: 100\n    n_proved: 100\n- exp_id: d129-1_7b-isr-b03-s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    PR: 0.52\n    ISR_star: 0.2308\n    H1_pct: 26.9\n    H7_pct: 0\n    H8_pct: 0\n    non_hacking_pct: 73.1\n    content_independent_pct: 100\n    strict_genuine_pct: 0\n    total_samples: 100\n    proved_count: 52\n- exp_id: d129-1_7b-isr-b03-s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    PR: 0.92\n    ISR_star: 0.236\n    H1_pct: 1.1\n    H7_pct: 0\n    H8_pct: 1.1\n    non_hacking_pct: 97.8\n    content_independent_pct: 100\n    strict_genuine_pct: 0\n    total_samples: 100\n    proved_count: 92\n- exp_id: d134-4b-isr-b01-s47\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    PR: 0.97\n    proved: 97\n    total: 100\n    H1: 1\n    H7: 83\n    H7a: 83\n    H8: 10\n    H9: 0\n    CI: 8\n    genuine: 3\n    genuine_pct: 3.1\n    S-NH_pct: 3.1\n- exp_id: d134-4b-isr-b01-s48\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    PR: 0.66\n    proved: 66\n    total: 100\n    H1: 0\n    H7: 66\n    H7a: 66\n    H8: 0\n    H9: 0\n    CI: 0\n    genuine: 0\n    genuine_pct: 0\n    S-NH_pct: 0\n    note: Pure H7 collapse — 100% of proved are H7\n- exp_id: d134-4b-isr-b01-s49\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    PR: 0.86\n    proved: 86\n    total: 100\n    H1: 6\n    H7: 73\n    H7_rate: 0.8488\n    H8: 6\n    H9: 0\n    CI: 0\n    genuine: 1\n    genuine_pct: 1.16\n    S-NH: 1\n    S-NH_pct: 1.16\n- exp_id: d134-4b-isr-b01-s50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    PR: 0.98\n    proved: 98\n    total: 100\n    H7_rate: 0.857\n    genuine_pct: 6.1\n- exp_id: d134-4b-isr-b01-s51\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    PR: 0.98\n    proved: 98\n    total: 100\n    H1: 0\n    H7: 96\n    H7_rate: 0.98\n    H8: 1\n    H9: 0\n    genuine: 1\n    genuine_pct: 1\n- exp_id: d134-4b-random-b01-s47\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.89\n    eval_n_proved: 89\n    eval_n_problems: 100\n    eval_mean_isr: 0.0857\n    eval_isr_std: 0.1259\n    eval_median_isr: 0\n    eval_proved_only_mean_isr: 0.0963\n    classify_h7_count: 0\n    classify_h7_pct: 0\n    classify_h1_strict_count: 79\n    classify_h1_pct: 88.76\n    classify_h8_conjunction: 4\n    classify_h8_pct: 4.49\n    classify_genuine_count: 6\n    classify_genuine_pct: 6.74\n    classify_conclusion_in_premise: 79\n    train_final_prove_rate: 0.62875\n    train_final_mean_isr: 0.1229\n    train_loss: 0.0093\n    train_steps: 500\n    note: eval PR=89% (held-out proofwriter_fol_100.jsonl); train PR=0.629 is batch\n      moving avg, NOT eval\n- exp_id: d134-4b-random-b01-s48\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.93\n    eval_n_proved: 93\n    eval_n_problems: 100\n    classify_h7_pct: 3.2\n    classify_h1_pct: 80.6\n    classify_h8_pct: 15.1\n    classify_genuine_pct: 4.3\n    train_steps: 500\n    note: cron 误报 failed (pipeline 在 train PID 退出后继续 eval/classify, cron 检测到 train\n      PID 退出即判 failed); 实际 train+eval+classify 全部正常完成\n- exp_id: d134-4b-random-b01-s49\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_prove_rate: 0.05\n    eval_n_proved: 5\n    eval_n_problems: 100\n    eval_avg_time: 10.5\n    classify_h7_count: 1\n    classify_h7_pct: 20\n    classify_h1_strict_count: 4\n    classify_h1_pct: 80\n    classify_h8_conjunction: 0\n    classify_h8_pct: 0\n    classify_genuine_count: 0\n    classify_genuine_pct: 0\n    train_final_prove_rate: 0.675\n    train_steps: 500\n    diagnosis: 'repetition collapse: model generates 3-5 premises then infinite repeat\n      loop; train PR=67.5% (short batches) but eval PR=5% (100 unseen problems all\n      hit timeout); NOT a bug, same seed under ISR gives PR=86%'\n- exp_id: d134-4b-random-b01-s50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.45\n    mean_isr: 0.0258\n    proved_only_mean_isr: 0.0573\n    h7_total_rate: 0.0889\n    h1_strict_rate: 0.8667\n    h8_conjunction_collapse_rate: 0\n    genuine_rate: 0.0444\n    genuine_count: 2\n- exp_id: d134-4b-random-b01-s51\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.65\n    mean_isr: 0.2223\n    proved_only_mean_isr: 0.342\n    h7_total_rate: 0.0154\n    h1_strict_rate: 0.5538\n    h8_conjunction_collapse_rate: 0.2923\n    genuine_rate: 0.1385\n    genuine_count: 9\n- exp_id: d142-gated-isr-s52\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: d142-gated-isr-s53\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: d142-gated-isr-s54\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: d142-gated-isr-s55\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 1\n    isr: 0.525\n    TS_pct: 82\n    CE_pct: 0\n    PG_pct: 15\n    CI_pct: 0\n    genuine_pct: 3\n- exp_id: d142-gated-isr-s56\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.36\n    isr: 0.2925\n    TS_pct: 0\n    CE_pct: 0\n    PG_pct: 83\n    CI_pct: 75\n    genuine_pct: 17\n- exp_id: d142-gated-isr-s57\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.88\n    isr: 0.4497\n    TS_pct: 1\n    CE_pct: 20\n    PG_pct: 15\n    CI_pct: 0\n    genuine_pct: 64\n- exp_id: d143-pw-exec-s42\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d143-pw-exec-s43\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d143-pw-exec-s44\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d143-pw-isr-s42\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d143-pw-isr-s43\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d143-pw-isr-s44\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d143-pw-random-s42\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d143-pw-sft-s42\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d143-pw-extended-s42\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d144-llama-exec-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    prove_rate: 0\n    reward: 0\n    parse_rate: 1\n    steps_completed: 72\n    reason: LLaMA-3.2-3B base below GRPO cold-start threshold for FOL. 72 steps all-zero\n      reward/loss/grad_norm, model weights never updated.\n- exp_id: d143-pw-sta-s42\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d143-pw-sta-s43\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d143-pw-sta-s44\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d144-llama-exec-s43\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d144-llama-exec-s44\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d144-llama-isr-s42\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d144-llama-isr-s43\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d144-llama-isr-s44\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: d146-pf-exec-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    reward: 1\n    prove_rate: 1\n    isr: 0\n    steps_completed: 500\n    classify_proved: 99\n    classify_genuine: 0\n    classify_genuine_rate: 0\n    classify_TS: 99\n    classify_CE: 0\n    classify_PG: 0\n    classify_CI: 0\n- exp_id: d146-pf-exec-s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    reward: 1\n    prove_rate: 1\n    isr_mean: 0.2048\n    parse_rate: 1\n    prove_rate_mean_all: 0.4143\n    prove_rate_final50: 0.55\n    isr_final50: 0.119\n    steps_completed: 500\n    classify_proved: 63\n    classify_genuine: 32\n    classify_genuine_rate: 0.508\n    classify_TS: 0\n    classify_CE: 31\n    classify_PG: 0\n    classify_CI: 0\n- exp_id: d146-pf-exec-s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    reward: 1\n    prove_rate: 1\n    isr: 0.043\n    parse_rate: 1\n    steps_completed: 500\n    classify_proved: 72\n    classify_genuine: 1\n    classify_genuine_rate: 0.014\n    classify_TS: 0\n    classify_CE: 71\n    classify_PG: 0\n    classify_CI: 0\n- exp_id: d146-pf-isr-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    reward_final: 0\n    prove_rate_final: 0\n    isr_final: 0\n    parse_rate: 1\n    prove_rate_mean: 0.354\n    prove_rate_final50: 0.35\n    isr_mean: 0.12\n    isr_peak: 0.409\n    steps_completed: 500\n    note: 'bimodal: 38% PR=0, 36.8% PR=0.5, 10.8% PR=1.0; saturated after step 300'\n    classify_proved: 46\n    classify_genuine: 46\n    classify_genuine_rate: 1\n    classify_TS: 0\n    classify_CE: 0\n    classify_PG: 0\n    classify_CI: 0\n- exp_id: d146-pf-isr-s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    reward_final: 1.02\n    prove_rate_final: 1\n    isr_final: 0.205\n    parse_rate: 1\n    steps_completed: 500\n    note: partial recovery is to CE hacking (70% CE, 30.4% genuine), not genuine reasoning.\n      Only ISR seed with hacking — parallels pattern of convergence=hacking across\n      both exec and ISR conditions.\n    classify_proved: 56\n    classify_genuine: 17\n    classify_genuine_rate: 0.304\n    classify_TS: 0\n    classify_CE: 39\n    classify_PG: 0\n    classify_CI: 0\n- exp_id: d146-pf-isr-s44\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    reward_final: 0\n    prove_rate_final: 0\n    isr_final: 0\n    parse_rate: 1\n    prove_rate_mean: 0.454\n    prove_rate_final50: 0.487\n    isr_mean: 0.131\n    isr_final50: 0.145\n    isr_peak: 0.351\n    steps_completed: 500\n    note: oscillating; 366/500 steps nonzero PR; nz_mean PR=0.620, ISR=0.178\n    classify_proved: 66\n    classify_genuine: 66\n    classify_genuine_rate: 1\n    classify_TS: 0\n    classify_CE: 0\n    classify_PG: 0\n    classify_CI: 0\n- exp_id: d146-pf-pipeline\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: d154-8b-exec-s42\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: d154-8b-exec-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: d154-8b-exec-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: d154-8b-isr-s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: d154-8b-isr-s43\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: d154-8b-exec-s42-r2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: d154-8b-exec-s42-r3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: d154-8b-exec-s42-k4\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: d154-8b-exec-s42-k4v2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    prove_rate: 0.155\n    mean_isr: 0.082\n    parse_rate: 1\n    train_loss: 0.0149\n    training_steps: 500\n    training_time_sec: 9395\n    converged: false\n    frac_reward_zero_std: 1\n    failure_mode: training_stagnation_k4_insufficient\n    note: 'K=4 insufficient for 8B: cold-start stagnation, not Goodhart collapse.\n      All 4 samples produce near-identical outputs, zero GRPO gradient.'\n- exp_id: d157-shuffled-isr-s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: d157-shuffled-isr-s43\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.16\n    mean_isr: 0.0908\n    proved_only_mean_isr: 0.5675\n    n_proved: 16\n    genuine_count: 14\n    genuine_rate: 0.875\n    TS_count: 1\n    CE_count: 1\n    PG_count: 0\n    CI_count: 0\n    isr_std: 0.2314\n    median_isr: 0\n    max_isr: 0.8889\n- exp_id: d157-shuffled-isr-s44\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.15\n    mean_isr: 0.0813\n    proved_only_mean_isr: 0.5423\n    n_proved: 15\n    genuine_count: 13\n    genuine_rate: 0.867\n    TS_count: 1\n    CE_count: 1\n    PG_count: 0\n    CI_count: 0\n- exp_id: d158-llama-sft-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    prove_rate: 0\n    mean_isr: 0\n    n_proved: 0\n    n_total: 100\n    gate_passed: false\n    failure_mode: generation_degeneracy_and_unicode_fol_syntax_mismatch\n    note: 'LLaMA SFT warmstart failed: model outputs Unicode FOL (∀, →, ∧) but Prover9\n      requires ASCII (all, ->, &). PR=0/100.'\n- exp_id: d158-llama-grpo-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: d158_llama_sft_s42\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: d157-shuffled-isr-s42-r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: d157-shuffled-isr-s42-r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    prove_rate: 0.15\n    mean_isr: 0.0851\n    proved_only_mean_isr: 0.5673\n    n_proved: 15\n    genuine_count: 13\n    genuine_rate: 0.8667\n    TS_count: 1\n    CE_count: 1\n    PG_count: 0\n    CI_count: 0\n    isr_std: 0.2265\n    median_isr: 0\n- exp_id: d165-llama-exec-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    prove_rate: 0.14\n    n_proved: 14\n    n_problems: 100\n    proved_only_mean_isr: 0.5467\n    TS_count: 0\n    TS_rate: 0\n    CE_count: 2\n    CE_rate: 0.143\n    PG_count: 0\n    PG_rate: 0\n    CI_count: 2\n    CI_rate: 0.143\n    genuine_count: 12\n    genuine_rate: 0.857\n    by_answer_type:\n      'true':\n        count: 34\n        proved: 14\n        pr: 0.412\n      'false':\n        count: 25\n        proved: 0\n        pr: 0\n      unknown:\n        count: 41\n        proved: 0\n        pr: 0\n    train_prove_rate: 0.0993\n    train_mean_isr: 0.0478\n    train_loss: 0.0665\n    train_runtime_sec: 4513\n- exp_id: d165-llama-exec-s43\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    prove_rate: 0.15\n    n_proved: 15\n    n_problems: 100\n    proved_only_mean_isr: 0.5658\n    mean_isr: 0.0849\n    TS_count: 0\n    TS_rate: 0\n    CE_count: 2\n    CE_rate: 0.133\n    PG_count: 0\n    PG_rate: 0\n    genuine_count: 13\n    genuine_rate: 0.867\n    by_answer_type:\n      'true':\n        count: 34\n        proved: 15\n        pr: 0.441\n      'false':\n        count: 25\n        proved: 0\n        pr: 0\n      unknown:\n        count: 41\n        proved: 0\n        pr: 0\n    train_prove_rate: 0.101\n    train_mean_isr: 0.049\n    train_loss: 0.073\n    train_runtime_sec: 4438\n- exp_id: d165-llama-exec-s44\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    PR: 0.16\n    ISR_star: 0.5492\n    genuine_pct: 87.5\n    n_proved: 16\n    hacking_modes:\n      CE: 2\n      TS: 0\n      PG: 0\n      CI: 0\n    genuine_count: 14\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T21:55:36.336Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T21:55:36.336Z",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-21T21:55:36.359Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：8B退化确认但模式同质（均为H7）或程度较弱，cross-scale成立但taxonomy分化贡献有限
核心假设：['8B exec-only成功训练但dominant mode与4B相同（均为H7），或hacking rate 50-80%弱于4B', 's45/s46 1000步至少1个确认ISR崩塌，1个部分崩塌（ISR*=0.05-0.15）', 'N=10 genuine OR≈1.3-1.6，CMH p=0.03-0.10（边界显著），需补充effect size讨论', 'Reviewer会追问8B同质化意味着什么——需要有准备好的解释']
关键指标范围：{'8b_exec_prove_rate': [0.5, 0.85], '8b_exec_hacking_rate': [0.5, 0.85], '8b_exec_genuine_rate': [0.05, 0.3], '8b_mode_differs_from_4b': False, 's45_s46_1000step_isr_star': [0.01, 0.15], 'n10_isr_genuine_or_pooled': [1.3, 1.6], 'n10_isr_genuine_cmh_p': [0.03, 0.1], 'n10_genuine_window_ratio': [0.3, 0.3], 'reviewer_score': [3.0, 3.25]}
叙事方向：Cross-scale claim保留但降级为'degeneration transfers across scales, exploitation mode converges to H7'——确认universality但taxonomy分化贡献被削弱。C2 double-edged需要明确软化：genuine OR从3.48降至~1.5仅边界显著，reframe为'modest transient uplift overwhelmed by dominant collapse'。论文重心转向C1 diagnostic methodology + Goodhart inevitability mechanism。Premise-count-matched analysis和meta-Goodhart triple gaming作为methodological contribution补位。ISR-as-reward篇幅压缩，增加diagnostic case study depth。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: solver-trace-ablation
venue: emnlp-2026
focus: 评估跨尺度扩展（Qwen3-8B）和 seed 扩展对论文评分的影响。重点关注：(1) 8B exec-only 如果 positive，framing 从 case study 升级到 across scales 是否足够支撑 3.25-3.5？(2) N=5→8 seeds 对统计效力的影响；(3) 8B 如果 negative（不退化），论文如何处理？(4) analysis paper 定位的 score ceiling？

## paper_framing.md

# Paper Framing — solver-trace-ablation

## Target Venue
- **EMNLP 2026 Main** (NLP and Symbolic Reasoning track)
- Deadline: ARR May 25, 2026

## Core Claims (3 条 — Goodhart 主线诊断/分析论文)

| Claim | Status | 闭环标志 |
|-------|--------|----------|
| Claim 1: STA 诊断能力 | ✅ 已闭环 → 🔄 扩展中 (cross-scale) | 5-seed (s42-s46) + 1000-step trajectory + hacking taxonomy (9 modes). **Planned**: +8B 3-seed cross-scale (plan_021), +s45/s46 1000-step (plan_020) |
| Claim 2: Goodhart inevitable + ISR double-edged | ✅ 已闭环 → 🔄 扩展中 | 5-seed ISR + 5-seed random β=0.1 + premise-count-matched + SFT baseline + 1.7B cross-scale + β=0.05 no-safe-dose. **Planned**: +3 ISR seeds (plan_022), +8B ISR stretch (plan_023) |
| Claim 3: 跨逻辑泛化 | ✅ 已闭环 | exec-only 3-seed (D056) + STA 3-seed: 3/3 gaming — 三种不同 gaming 路径 (H7/degenerate-syntax/query-as-fact) |

### Claim 1: ISR as Reward Hacking Diagnostic ✅
STA derives ISR via LOO ablation on solver inputs. ISR detects reward hacking that prove_rate misses: exec-only GRPO achieves PR=93% but ISR collapses 0.6423 (100步) → 0.1324 (500步) → 0.0027 (1000步).

**Evidence (compact)**:
- 5-seed exec-only (s42-s46): All show ≥90% structural degeneration (H1+H7+H8). s42: H1=87.1%; s43: PR=13% collapse; s44: H7=100%; s45: TS=93.9%, genuine=1.0%; s46: CE=89.2%, genuine=9.7%
- 1000-step trajectory (s42): ISR collapses 99.6% (0.6423→0.0027), 94.8% proved samples ISR=0
- Hacking taxonomy: 9 distinct modes (CE, TS, PG, H7a/b, H8, H9, degenerate-syntax, query-as-fact)
- SFT baseline: PR=14%, 92.9% genuine — confirms hacking is RL-reward-specific
- **Planned**: Qwen3-8B exec-only 3 seeds (plan_021) for cross-scale validation; s45/s46 1000-step extension (plan_020) for N=3 trajectory evidence

### Claim 2: ISR as Reward — Inevitable Goodhart Collapse ✅
ISR has inherent structural bias: P→P tautologies receive ISR≥0.5, creating a positive feedback loop. β controls timing not destiny.

**Key findings (5-seed primary)**:
- ISR β=0.1: genuine 22.6% vs Random 7.7% (OR=3.48, p<10⁻⁸; CMH OR=3.37, p<10⁻⁹), BUT H7 54.3% vs 29.5% (OR=2.84, p<5×10⁻¹²) → double-edged sword
- Genuine advantage is selection effect (proportion), not quality (premise-matched ISR 1.06×)
- Transient: 1000步 genuine 17%→2%; s45 55%→0%
- β=0.05: 2/2 seeds deterministic H7 (97-100%) — no safe dose
- β=0.3: multi-modal instability (PR=66±42%, 3 different failure paths)
- Non-monotonic dose-response: β=0.05 deterministic → β=0.1 bimodal → β=0.2 deterministic → β=0.3 multi-modal
- H7b obfuscated tautology (ISR s44): meta-Goodhart triple gaming (execution + ISR + detector evasion)
- 3-seed vs 5-seed: H7 OR collapsed 15.05→2.84; genuine reversed from n.s. to OR=3.48 (s45/s46 addition)
- Stochastic bifurcation: 2/5 seeds collapse immediately, 3/5 sustain transient genuine window
- **Planned**: +3 ISR β=0.1 seeds (plan_022) for N=8; +Qwen3-8B ISR stretch (plan_023)

### Claim 3: Cross-Logic Diagnostic Transfer ✅
STA transfers across formal languages: Prolog→SWI-Prolog shows same degeneration.

**Evidence**:
- Prolog exec-only 3-seed: PR=53.3%±31.1%, ISR near-zero (2/3 seeds <0.04)
- Prolog STA 3-seed: **3/3 seeds gaming, 0% genuine** — universal Goodhart
  - s42: Clean H7 (100%), s43: Degenerate syntax (97.4% H1, functional H7), s44: Query-as-fact gaming (97.9% functional H7, Reviewer-corrected from initial "100% genuine")
- Prolog gaming more extreme than FOL (0% vs ~6% genuine residual) — simpler semantics → more complete hacking

### Cross-Scale Evidence: Qwen3-1.7B
- Random β=0.1: PR=93%, H9=100% (contradiction explosion, ISR≈0)
- ISR β=0.1: PR=100%, ISR=0.6 zero-variance, H1=100% (fixed template gaming)
- ISR β=0.3: PR=17%, genuine=29.4% (learning suppression)
- Capacity-dependent Goodhart basins: 4B→H7 (sophisticated tautology), 1.7B→H1 (simplest exploit)
- Confirms: ISR gaming transfers across scales, only strategy differs

## ISR Capability Boundary
ISR measures syntactic necessity, NOT semantic faithfulness. Spearman ρ(ISR, NLI accuracy) = -0.049 (p=0.187, n.s.). Treated as Limitation.

## Story Spine
- **Problem**: GRPO with exec-only rewards produces structurally degenerate outputs while achieving high prove rates. No diagnostic exists.
- **Gap**: No work systematically studies reward hacking in formal reasoning GRPO or provides diagnostic tools.
- **Contribution**: STA (LOO ablation → ISR) as diagnostic. Key findings: (1) ISR quantifies hacking invisible to PR; (2) ISR contains inherent Goodhart vulnerability (tautologies get ISR≥0.5); (3) double-edged at β=0.1 (more genuine AND more H7); (4) stochastic bifurcation; (5) 9-mode hacking taxonomy; (6) transfers across logic types (Prolog) and model scales (1.7B); (7) β=0.05 confirms no safe dose; (8) premise-count confound is methodological contribution.
- **Headline**: ISR reliable as diagnostic, unreliable as optimization target at any dose. β controls when collapse occurs, not whether.

## Venue Fit Risks
- **EMNLP fit**: Diagnostic/analysis paper, empirical findings + mechanistic insight
- **"Just negative results"**: ISR as diagnostic IS positive (C1); meta-Goodhart is novel mechanistic insight; 9-mode taxonomy is actionable
- **"Old wine"**: ISR = LOO ablation. Novelty at application level + empirical findings
- **"Single-logic"**: Prolog validates (3/3 gaming, 0% genuine)
- **"Single-model" (MF-7)**: **Planned**: Qwen3-8B cross-scale (plan_021). Combined with 1.7B → 3 scale points (1.7B/4B/8B)

## Anticipated Reviewer Concerns
1. **"ISR is just LOO ablation"** — Acknowledge. Contribution is application + Goodhart analysis + taxonomy.
2. **"β=0.1 success is one seed"** — 5-seed: 3/5 sustain genuine window (transient). OR=3.48 but premise-matched 1.06×.
3. **"Conclusion embedding invalidates"** — GRPO-universal (both conditions). Random H1 higher (58.5% vs 18.3%).
4. **"Goodhart obvious"** — Conceptual yes; empirical characterization in formal GRPO is not. Meta-Goodhart novel.
5. **"No positive result"** — ISR diagnostic IS positive. Negative on ISR-as-reward IS the contribution.
6. **"ISR circular"** — Validated: ISR reward → ISR-specific gaming. Use for diagnosis only.
7. **"Only one logic"** — Prolog: 3/3 gaming, 0% genuine (stronger than FOL).
8. **"500 steps too short"** — 1000-step: ISR 0.123→0.003 (-97.8%).
9. **"Seeds insufficient"** — 5-seed exec-only, stochastic bifurcation IS the finding.
10. **"2.4x was wrong"** — Transparent correction. 5-seed OR=3.48 confirms genuine proportion advantage; quality same (1.06×).
11. **"Premise count obvious"** — LOO metrics widely used without this correction. Documenting it is methodological.
12. **"Can't act on this"** — 7 actionable insights. ISR + component count diagnostic deployable.
13. **"Prolog s44 misclassified"** — Transparent correction; classifier blind spot is itself a finding.
14. **"ISR has genuine benefit — why not use?"** — Transient (17%→2%). Same LOO bias rewards tautologies. No stable operating point.
15. **"Only 2 seeds at β=0.05"** — 2/2 deterministic collapse already strong evidence.
16. **"Only one model (Qwen3-4B)" (MF-7)** — **Planned**: 8B cross-scale (plan_021). Combined with 1.7B → 3 scale points. LLaMA-3.2-3B establishes lower capability bound (PR≈15%).
17. **"N=3 seeds insufficient" (MF-1)** — Already N=5 exec-only (s42-s46, all ≥90% degeneration). Planned: s45/s46 to 1000 steps + 3 more ISR seeds for N=8.

## Discussion Notes
- **Hack mode switching**: GRPO degeneration mode is seed-determined. Single-seed results unreliable.
- **H7 OR revision**: 3-seed OR=15.05 → 5-seed OR=2.84. ISR modestly increases H7; mode selection stochastic.
- **Genuine OR reversal**: 3-seed n.s. → 5-seed OR=3.48. ISR double-edged. Quantity not quality, transient.
- **Non-monotonic dose-response**: β=0.05 deterministic → β=0.1 bimodal → β=0.2 deterministic → β=0.3 multi-modal.

## Detailed Data Reference
Full per-seed data tables, statistical tests, and internal tracking notes preserved in `paper_framing_full_backup.md`.


## experiment_plan (with registry status)

- id: plan_001
  claim: 1
  description: FOL single-logic GRPO, execution-only reward (500 steps, K=8, 3 seeds)
    — baseline for STA comparison
  priority: P0
  gpu_budget_hours: 3
  deps: []
  registry_id: plan001-exec-only-s42-r2
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
    h7_rate: 0
    h7_count: 0
    h1_rate: 0.871
    h1_count: 81
    h8_conjunction_collapse_count: 6
    h8_conjunction_collapse_rate: 0.0645
    genuine_rate: 0.0753
    genuine_count: 7
    genuine_mean_isr: 0.3141
    h1_mean_isr: 0.1055
    conclusion_embedding_total: 0.871
    content_independent_predicates_count: 1
    h8_audit_note: '2026-05-15: H8 conjunction collapse added. genuine 12→7.'
- id: plan_002
  claim: 2
  description: 'FOL single-logic GRPO, additive ISR bonus: r = r_exec · (1 + β·ISR),
    β∈{0.1, 0.3, 0.5}. 先跑 β=0.3 单 seed 验证方向，成功再 3-seed。旧凸组合公式 (α·r_exec + β·r_exec·ISR,
    α+β=1) 已废弃——ISR<1 时永远是 penalty (plan005 confirmed)。 新公式确保 ISR 只能 bonus 不能 penalty。'
  priority: P0
  gpu_budget_hours: 4
  deps: []
  registry_id: plan002-additive-b01-s42
  status: DONE
  conclusion: negative
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
    h7_rate: 0.16
    h7_count: 13
    h1_rate: 0.519
    h1_count: 42
    h8_conjunction_collapse_count: 12
    h8_conjunction_collapse_rate: 0.148
    genuine_rate: 0.173
    genuine_count: 14
    tautological_collapse: false
    h8_audit_note: '2026-05-15: H8 conjunction collapse audit completed. 12/81 proved
      samples are H8. Genuine 26→14 (32.1%→17.3%). H8 JSON at /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json'
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
  registry_id: plan004-o1-ablation-s42
  status: DONE
  conclusion: negative
  metrics:
    prove_rate: 0.63
    mean_isr: 0.0072
    h7_count: 0
    h7_rate: 0
    h1_count: 63
    h1_rate: 1
    h8_conjunction_collapse_count: 2
    h8_conjunction_collapse_rate: 0.0317
    genuine_count: 0
    genuine_rate: 0
    content_independent_predicates_count: 3
    h8_audit_note: '2026-05-15: H8 conjunction collapse added. genuine unchanged (0).'
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
  registry_id: plan006-prolog-sta-s42
  notes: Requires Prolog STA instantiation (rule ablation). SWI-Prolog already installed.
    Upgraded from 1→3 seeds per Dream feedback.
  status: DONE
  conclusion: negative
  metrics:
    cumulative_prove_rate: 0.848
    cumulative_mean_isr: 0.787
    final_prove_rate: 1
    final_isr: 1
    final_reward: 1
    saturation_onset_step: 100
    train_loss: 0.00716
    training_hours: 0.78
    final_entropy: 0.01
    final_completion_length: 27
    initial_completion_length: 120
    steps_at_perfect_reward: 400
    train_runtime_sec: 2791
    eval_prove_rate: 0.5
    eval_mean_isr: 0.5
    eval_proved_only_isr: 1
    eval_h7_rate: 1
    eval_h7_count: 50
    eval_proved_count: 50
    eval_total_count: 100
    eval_n_clauses_mean: 1
    eval_isr_distribution: 'binary: 50x0 + 50x1'
- id: plan_007
  claim: 3
  description: 'Multi-logic GRPO (FOL+Prolog): exec-only vs exec+STA (500 steps, K=8,
    1 seed) — cross-logic transfer test'
  priority: P1
  gpu_budget_hours: 3
  deps:
  - plan_006
  status: planned
  notes: deferred — not in current paper scope
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
  notes: deferred — not in current paper scope
- id: plan_009
  claim: 1
  description: 'SFT baseline: supervised finetuning on same data (FOLIO 500), compare
    with GRPO variants'
  priority: P1
  gpu_budget_hours: 1
  deps: []
  registry_id: plan009-sft-baseline-s42-1000
  status: DONE
  conclusion: success
  metrics:
    train_final_loss: 0.0168
    train_last_step_loss: 0.0168
    train_token_accuracy: 0.9955
    train_epochs: 15.88
    train_runtime_sec: 1415
    train_steps: 1000
    eval_prove_rate: 0.13
    eval_n_proved: 13
    eval_n_problems: 100
    eval_mean_isr: 0.0738
    eval_isr_std: 0.2077
    eval_median_isr: 0
    eval_proved_only_isr: 0.5677
    eval_data: proofwriter_fol_100.jsonl
    eval_method: eval_sta.py full STA
    eval_output_path: /root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json
    h7_strict_count: 0
    h7_strict_rate: 0
    h1_strict_count: 1
    h1_strict_rate: 0.0769
    h8_conjunction_collapse_count: 0
    h8_conjunction_collapse_rate: 0
    genuine_count: 12
    genuine_rate: 0.9231
    conclusion_in_premise_count: 1
    conclusion_in_premise_rate: 0.0769
    isr_1_count: 0
    content_independent_count: 0
    eval_by_answer_type:
      'true':
        count: 34
        proved: 12
        prove_rate: 0.353
        mean_isr: 0.209
      'false':
        count: 25
        proved: 1
        prove_rate: 0.04
        mean_isr: 0.011
      unknown:
        count: 41
        proved: 0
        prove_rate: 0
        mean_isr: 0
- id: plan_010
  claim: 3
  description: 'SMT-LIB single-logic GRPO: exec-only vs exec+STA — third logic type'
  priority: P2
  gpu_budget_hours: 3
  deps: []
  notes: deferred — not in current paper scope
  status: planned
- id: plan_011
  claim: 1
  description: 'Qwen3-8B scaling: full MLSR on 8B model (1 seed) — model scale effect'
  priority: P2
  gpu_budget_hours: 6
  deps:
  - plan_005
  status: planned
  notes: deferred — not in current paper scope
- id: plan_012
  claim: 1
  description: 'Hacking characterization: manual annotation of 200 outputs per condition,
    categorized by extensional-shortcut taxonomy'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_003
  registry_id: plan012-hacking-taxonomy
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
  notes: killed per D011 — additive bonus supersedes curriculum approach
  registry_id: plan015-linear-s42
  status: DONE
  conclusion: killed
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
    eval_proved_only_isr: 0.0028
    eval_mean_isr: 0.0027
    eval_isr_std: 0.0118
    eval_median_isr: 0
    eval_max_isr: 0.0588
    eval_prove_rate: 0.96
    eval_n_proved: 96
    eval_n_total: 100
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
    tautological_collapse: false
    h7_count: 4
    h7_rate: 0.0833
    h7a_count: 4
    h7b_count: 0
    h1_count: 44
    h1_rate: 0.9167
    h8_count: 0
    h8_rate: 0
    genuine_count: 0
    genuine_rate: 0
    taxonomy_tool: classify_h7.py standard (2026-05-15)
    taxonomy_note: 'Re-classified with current classify_h7.py. Old values: H7=0, H1=48,
      genuine=0. New: H7=4 (4 H7a text-match tautologies reclassified from H1), H1=44,
      H8=0, genuine=0.'
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
  registry_id: plan018-additive-random-b01-s43-r3
  status: DONE
  conclusion: negative
  metrics:
    prove_rate: 0.94
    n_proved: 94
    n_problems: 100
    mean_isr: 0.1406
    isr_std: null
    proved_only_isr: 0.1495
    h7_count: 36
    h7_rate: 0.383
    h7a_count: 36
    h7b_count: 0
    h1_count: 56
    h1_rate: 0.596
    h8_count: 1
    h8_rate: 0.011
    genuine_count: 1
    genuine_rate: 0.0106
    train_prove_rate: 0.5825
    train_mean_isr: 0.1266
    taxonomy_tool: classify_h7.py + manual subtype analysis (2026-05-15)
    taxonomy_note: 'D093 H7 subtype: all 36 H7 are H7a (text-match tautology), 0 H7b.
      single_premise_count=0: Random H7a are multi-premise proofs with embedded tautological
      premise, structurally different from exec-only H7a (single-premise minimal tautology).
      H7b confirmed absent in Random condition.'
    h7a_structural_note: Random H7a = multi-premise with embedded matching premise;
      exec-only H7a = single-premise P-therefore-P
- id: plan_019
  claim: 1
  description: Incorporate existing s45/s46 exec-only 500-step data into paper. Registry
    shows s45 (PR=99%, genuine=1.0%, TS=93.9%) and s46 (PR=93%, genuine=9.7%, CE=89.2%).
    Both confirm ≥90% structural degeneration, extending C1 evidence from N=3 to N=5
    with zero additional GPU cost.
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  notes: 'Reviewer strategic assessment: these seeds already exist in registry but
    were omitted from paper. Pure writing/analysis task.'
  status: planned
- id: plan_020
  claim: 1
  description: Extend s45 and s46 exec-only training from 500 to 1000 steps. Validates
    ISR collapse trajectory (0.6423→0.1324→0.0027) generalizes across all 5 seeds,
    not just s42. Strengthens "degeneration worsens with training" claim with N=3
    trajectory seeds (s42+s45+s46).
  priority: P0
  gpu_budget_hours: 6
  deps:
  - plan_019
  notes: 'Reviewer priority #2. Each seed ~3h on RTX PRO 6000.'
  status: planned
- id: plan_021
  claim: 1
  description: Qwen3-8B exec-only GRPO, 3 seeds (s42/s43/s44), 500 steps, K=8. Cross-scale
    validation of structural degeneration. If 8B also shows ≥80% hacking → "degeneration
    is not 4B-scale-specific". Different hacking mode distribution is also informative
    (scale-dependent taxonomy). 98GB GPU can handle 8B GRPO.
  priority: P0
  gpu_budget_hours: 12
  deps: []
  notes: 'Reviewer priority #3. Replaces old plan_011 (out-of-scope). 8B GRPO ~4h/seed
    on RTX PRO 6000 (98GB). Disk constraint: need ~32GB free, currently only 20GB
    — must clean old checkpoints first.'
  status: planned
- id: plan_022
  claim: 2
  description: Additional ISR β=0.1 seeds (s47/s48/s49) for Qwen3-4B. Extends bimodality
    characterization from N=5 to N=8. Better precision on 3/5 vs 2/5 gaming-vs-genuine
    split. Enables bootstrapped CI.
  priority: P1
  gpu_budget_hours: 5
  deps: []
  notes: 'Reviewer priority #4. ~1.5h/seed.'
  status: planned
- id: plan_023
  claim: 2
  description: Qwen3-8B ISR β=0.1, 3 seeds. Cross-scale Goodhart validation. Only
    execute if plan_021 shows degeneration (positive). Tests whether compositional
    Goodhart effect transfers across model scales.
  priority: P2
  gpu_budget_hours: 12
  deps:
  - plan_021
  notes: 'Reviewer: stretch goal, only if plan_021 positive and time permits.'
  status: planned
- id: plan_024
  claim: 1
  description: Compute premise-count-matched ISR analysis on exec-only outputs (s42-s46).
    Provides ISR baseline distribution for exec-only condition with premise-count
    controls, directly responding to reviewer concern about ISR interpretation without
    controlling for proof complexity.
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_019
  notes: 'Reviewer priority #1. Pure analysis, no GPU. ~1h coding.'
  status: planned


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
    h7_rate: 0
    h7_count: 0
    h1_rate: 0.871
    h1_count: 81
    h8_conjunction_collapse_count: 6
    h8_conjunction_collapse_rate: 0.0645
    genuine_rate: 0.0753
    genuine_count: 7
    genuine_mean_isr: 0.3141
    h1_mean_isr: 0.1055
    conclusion_embedding_total: 0.871
    content_independent_predicates_count: 1
    h8_audit_note: '2026-05-15: H8 conjunction collapse added. genuine 12→7.'
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
    eval_greedy_prove_rate: 0.13
    eval_greedy_mean_isr: 0
    eval_greedy_proved_only_isr: 0
    eval_greedy_n_proved: 13
    eval_greedy_method: eval_sta.py default (do_sample=False)
    eval_greedy_by_answer:
      'true':
        count: 34
        proved: 4
        prove_rate: 0.118
      'false':
        count: 25
        proved: 5
        prove_rate: 0.2
      unknown:
        count: 41
        proved: 4
        prove_rate: 0.0976
    eval_greedy_h7_count: 0
    eval_greedy_h7_rate: 0
    eval_greedy_h1_count: 13
    eval_greedy_h1_rate: 1
    eval_greedy_genuine_rate: 0
    eval_greedy_n_premises_proved_mean: 17.92
    eval_greedy_mean_components_proved: 18.92
    eval_greedy_n_premises_all_mean: 32.67
    eval_sampling_h1_rate: 1
    eval_sampling_h7_rate: 0
    eval_sampling_genuine_rate: 0
    eval_sampling_mean_components_proved: 18.5
    eval_greedy_vs_sampling_delta_pr: -0.01
    eval_method_note: Greedy and sampling agree on failure profile (ISR*=0, H1=100%,
      components~18.5-18.9). s43 collapse is decoding-invariant.
- exp_id: plan002-additive-b03-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    total_steps: 500
    duration_min: 56.7
    overall_prove_rate: 0.34025
    overall_isr: 0.11527
    last100_prove_rate: 0.5525
    eval_prove_rate: 0.18
    eval_mean_isr: 0.0257
    eval_isr_std: 0.0742
    eval_median_isr: 0
    eval_proved_only_isr: 0.1427
    eval_n_proved: 18
    eval_n_problems: 100
    eval_method: eval_sta.py full STA
    eval_data: proofwriter_fol_100.jsonl
    h7_rate: 0
    h7_count: 0
    h1_rate: 0.778
    h1_count: 14
    h8_conjunction_collapse_count: 3
    h8_conjunction_collapse_rate: 0.1667
    genuine_rate: 0.0556
    genuine_count: 1
    eval_by_type_false_pr: 0.12
    eval_by_type_false_isr: 0.0102
    eval_by_type_unknown_pr: 0.195
    eval_by_type_unknown_isr: 0.0422
    eval_by_type_true_pr: 0.206
    eval_by_type_true_isr: 0.0172
    h8_audit_note: '2026-05-15: H8 conjunction collapse added. genuine 4→1.'
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
    tautological_collapse: false
    h7_count: 4
    h7_rate: 0.0833
    h7a_count: 4
    h7b_count: 0
    h1_count: 44
    h1_rate: 0.9167
    h8_count: 0
    h8_rate: 0
    genuine_count: 0
    genuine_rate: 0
    taxonomy_tool: classify_h7.py standard (2026-05-15)
    taxonomy_note: 'Re-classified with current classify_h7.py. Old values: H7=0, H1=48,
      genuine=0. New: H7=4 (4 H7a text-match tautologies reclassified from H1), H1=44,
      H8=0, genuine=0.'
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
    tautological_collapse: true
    h7_rate: 1
    h7_count: 97
    h1_rate: 0
    h1_count: 0
    genuine_rate: 0
    genuine_count: 0
    conclusion_embedding_total: 1
- exp_id: plan002-additive-b01-s42
  name: ''
  status: DONE
  conclusion: negative
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
    h7_rate: 0.16
    h7_count: 13
    h1_rate: 0.519
    h1_count: 42
    h8_conjunction_collapse_count: 12
    h8_conjunction_collapse_rate: 0.148
    genuine_rate: 0.173
    genuine_count: 14
    tautological_collapse: false
    h8_audit_note: '2026-05-15: H8 conjunction collapse audit completed. 12/81 proved
      samples are H8. Genuine 26→14 (32.1%→17.3%). H8 JSON at /root/autodl-tmp/outputs/h7_classification/plan002_additive_b01_s42_h8.json'
- exp_id: plan016-extended-1000-s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_proved_only_isr: 0.0028
    eval_mean_isr: 0.0027
    eval_isr_std: 0.0118
    eval_median_isr: 0
    eval_max_isr: 0.0588
    eval_prove_rate: 0.96
    eval_n_proved: 96
    eval_n_total: 100
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
    tautological_collapse: false
    h7_count: 0
    h7_rate: 0
    h7a_count: 0
    h7b_count: 0
    h1_count: 58
    h1_rate: 0.7342
    h8_count: 4
    h8_rate: 0.0506
    genuine_count: 18
    genuine_rate: 0.2278
    taxonomy_tool: classify_h7.py standard (2026-05-15)
    taxonomy_note: 'Re-classified with current classify_h7.py. Old values: genuine_strict=12
      (H1_exact=56, H1_near=8, H8=3). New standard: H1=58 (2 former H1-near now H1),
      H8=4, genuine=18. Standard definition: proved - H7 - H1 - H8.'
- exp_id: plan006-prolog-exec-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.83
    eval_mean_isr: 0.031
    eval_proved_only_isr: 0.037
    eval_median_isr: 0
    eval_max_isr: 0.2
    eval_isr_std: 0.0534
    h7_rate: 0
    h1_rate: 0
    isr_1_rate: 0
    single_premise_rate: 0
    by_answer_type:
      'true':
        proved: 37
        count: 40
        pr: 0.925
        isr: 0.037
      'false':
        proved: 21
        count: 29
        pr: 0.724
        isr: 0.038
      unknown:
        proved: 25
        count: 31
        pr: 0.806
        isr: 0.016
- exp_id: plan006-prolog-exec-s43
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: plan006-prolog-exec-s44
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.21
    eval_mean_isr: 0.0812
    eval_isr_std: 0.2343
    eval_median_isr: 0
    eval_proved_only_isr: 0.3866
    eval_min_isr: 0
    eval_max_isr: 1
    eval_n_proved: 21
    eval_n_problems: 100
    eval_method: eval_sta.py full STA
    eval_data: proofwriter_fol_100.jsonl
    eval_elapsed_seconds: 683.9
    eval_by_type_false_pr: 0.04
    eval_by_type_false_isr: 0.04
    eval_by_type_unknown_pr: 0.317
    eval_by_type_unknown_isr: 0.099
    eval_by_type_true_pr: 0.206
    eval_by_type_true_isr: 0.09
    solver: PrologSolver
    logic_type: prolog
- exp_id: plan002-additive-b01-s43
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.61
    eval_n_proved: 61
    eval_n_problems: 100
    eval_proved_only_isr: 0.83
    h7_count: 59
    h7_rate: 0.9672
    h1_count: 0
    h1_rate: 0
    h1_near_count: 0
    h1_near_rate: 0
    h8_conjunction_collapse_count: 0
    h8_conjunction_collapse_rate: 0
    genuine_count: 2
    genuine_rate: 0.0328
    proved_single_premise_ratio: 1
    taxonomy_note: 'structurally determined: proved_single_premise_ratio=1.0, all
      taxonomy categories except H7 are zero by construction. eval file lost but classification
      derivable from structure.'
- exp_id: plan002-additive-b01-s44
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.89
    eval_mean_isr: 0.803
    eval_isr_std: null
    eval_proved_only_isr: 0.902
    eval_n_proved: 89
    eval_n_problems: 100
    h7_count: 89
    h7_rate: 1
    h1_count: 0
    h1_rate: 0
    h8_conjunction_collapse_count: 0
    h8_conjunction_collapse_rate: 0
    genuine_count: 0
    genuine_rate: 0
    component_mean: 4.33
    comp_2_ratio: 0.022
    h7_fn_correction: '12 former genuine reclassified as H7: all n_prem=1 false negatives
      (normalization mismatch prevented conclusion matching)'
- exp_id: plan018-additive-random-b01-s43
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan018-additive-random-b01-s44
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.89
    mean_isr: 0.0619
    isr_std: 0.1756
    median_isr: 0
    proved_only_mean_isr: 0.0695
    n_proved: 89
    n_problems: 100
    max_isr: 1
    min_isr: 0
    isr_pr_ratio: 0.0695
    isr_zero_count: 72
    isr_one_count: 2
    by_answer_type:
      'false':
        count: 25
        proved: 21
        prove_rate: 0.84
        mean_isr: 0.0533
      unknown:
        count: 41
        proved: 40
        prove_rate: 0.976
        mean_isr: 0.0892
      'true':
        count: 34
        proved: 28
        prove_rate: 0.824
        mean_isr: 0.0353
    elapsed_seconds: 1012.7
    eval_method: eval_sta.py with Prover9Solver, FOL
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
  status: DONE
  conclusion: negative
  metrics:
    cumulative_prove_rate: 0.848
    cumulative_mean_isr: 0.787
    final_prove_rate: 1
    final_isr: 1
    final_reward: 1
    saturation_onset_step: 100
    train_loss: 0.00716
    training_hours: 0.78
    final_entropy: 0.01
    final_completion_length: 27
    initial_completion_length: 120
    steps_at_perfect_reward: 400
    train_runtime_sec: 2791
    eval_prove_rate: 0.5
    eval_mean_isr: 0.5
    eval_proved_only_isr: 1
    eval_h7_rate: 1
    eval_h7_count: 50
    eval_proved_count: 50
    eval_total_count: 100
    eval_n_clauses_mean: 1
    eval_isr_distribution: 'binary: 50x0 + 50x1'
- exp_id: plan006-prolog-sta-s43
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    train:
      final_prove_rate: 0.769
      final_mean_isr: 0.129
      final_loss: 0.0155
      final_entropy: 0.09
      final_reward: 0.573
      completion_length_mean: 143
      train_runtime_seconds: 5095
      train_runtime_minutes: 84.9
    eval:
      n_problems: 100
      n_proved: 38
      prove_rate: 0.38
      mean_isr: 0.0704
      isr_std: 0.1263
      median_isr: 0
      proved_only_mean_isr: 0.1853
      min_isr: 0
      max_isr: 1
      by_answer_type:
        'false':
          count: 25
          proved: 11
          prove_rate: 0.44
          mean_isr: 0.1003
        unknown:
          count: 41
          proved: 11
          prove_rate: 0.268
          mean_isr: 0.0394
        'true':
          count: 34
          proved: 16
          prove_rate: 0.471
          mean_isr: 0.0859
    h7_classification:
      h7_strict: 0
      h7_rate: 0
      h1_strict: 37
      h1_rate: 0.974
      conclusion_in_premise_total: 37
      conclusion_in_premise_rate: 0.974
      genuine_count: 0
      genuine_rate: 0
      isr_1_count: 1
      note: 1 pseudo-genuine sample (folio_1415) has query embedded in single mega-clause;
        all 38/38 proved samples are tautological
- exp_id: plan006-prolog-sta-s44
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    pass_rate: 0.97
    isr_mean: 0.885
    isr_n_cl_ge3: N/A (0 samples)
    n_clauses_dist: 78/100 single-clause, 22/100 two-clause
    h7_functional_rate: 0.979
    genuine_rate: 0
    premise_count_analysis: 100% artifact - zero samples with n_clauses>=3, model
      exclusively generates 1-2 clause programs
    failure_mode: query-as-fact gaming (total H7 collapse)
- exp_id: plan009-sft-baseline-s42
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: plan009-sft-baseline-s42-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan009-sft-baseline-s42-r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan009-sft-baseline-s42-r4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.14
    eval_mean_isr: 0.08
    eval_isr_std: 0.214
    eval_median_isr: 0
    eval_max_isr: 0.833
    eval_proved_only_isr: 0.571
    eval_n_proved: 14
    eval_n_problems: 100
    eval_method: eval_sta.py full STA
    eval_data: proofwriter_fol_100.jsonl
    train_final_loss: 0.0287
    train_token_accuracy: 0.9935
    train_epochs: 7.94
    train_runtime_sec: 789.6
    by_answer_type:
      'true':
        count: 34
        proved: 13
        pr: 0.382
        isr: 0.226
      unknown:
        count: 41
        proved: 1
        pr: 0.024
        isr: 0.008
      'false':
        count: 25
        proved: 0
        pr: 0
        isr: 0
    h7_rate: 0
    h7_count: 0
    h1_rate: 0.071
    h1_count: 1
    genuine_rate: 0.929
    genuine_count: 13
    hacking_patterns: near-zero (1/14 H1, 0 H7, 92.9% genuine)
    tautological_collapse: false
- exp_id: plan006-prolog-exec-s43-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan006-prolog-exec-s43-r3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.56
    eval_mean_isr: 0.0084
    eval_isr_std: 0.0221
    eval_median_isr: 0
    eval_proved_only_isr: 0.015
    eval_min_isr: 0
    eval_max_isr: 0.1
    eval_n_proved: 56
    eval_n_problems: 100
    eval_method: eval_sta.py full STA
    eval_data: proofwriter_fol_100.jsonl
    eval_elapsed_seconds: 868.2
    eval_by_type_false_pr: 0.48
    eval_by_type_false_isr: 0.0043
    eval_by_type_unknown_pr: 0.6585
    eval_by_type_unknown_isr: 0.0114
    eval_by_type_true_pr: 0.5
    eval_by_type_true_isr: 0.0078
    solver: PrologSolver
    logic_type: prolog
- exp_id: plan018-additive-random-b01-s43-r2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    h7_rate: 0
    h7_count: 0
    h1_rate: 93.2
    h1_count: 82
    genuine_rate: 6.8
    genuine_count: 6
    eval_prove_rate: 0.88
    eval_mean_isr: 0.058
- exp_id: exp1-isr-b03-s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_rate: 1
    prove_rate: 0.91
    mean_isr: 0.2575
    isr_std: 0.2363
    median_isr: 0.3333
    proved_only_mean_isr: 0.283
    hacking_rate_strict_h7: 0.022
    hacking_rate_functional: 0.3297
    genuine_rate: 0.6703
    genuine_count: 61
    n_proved: 91
    n_problems: 100
    h1_conclusion_in_premise: 0.747
    eval_data: test_100.jsonl
    eval_output: /root/autodl-tmp/outputs/eval_sta_exp1_isr_b03_s43.json
- exp_id: exp1-random-b03-s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    parse_rate: 1
    prove_rate: 0.79
    mean_isr: 0.1745
    isr_std: 0.1628
    median_isr: 0.1667
    proved_only_mean_isr: 0.2209
    hacking_rate_strict_h7: 0
    hacking_rate_functional: 0.1013
    genuine_rate: 0.8987
    genuine_count: 71
    n_proved: 79
    n_problems: 100
    h1_conclusion_in_premise: 0.759
    eval_data: test_100.jsonl
    eval_output: /root/autodl-tmp/outputs/eval_sta_exp1_random_b03_s43.json
- exp_id: exp1-isr-b03-s44
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp1-random-b03-s44
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp2-exec-s43-greedy
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp4-100step-h1h7
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp1-isr-b03-s43-r2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp1-isr-b03-s44-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.95
    mean_isr: 0.705
    isr_std: 0.172
    proved_only_isr: 0.7421
    n_proved: 95
    n_problems: 100
    h7_rate: 1
    h7_count: 95
    h1_rate: 0
    h1_count: 0
    genuine_rate: 0
    genuine_count: 0
    single_premise_rate: 1
    eval_data: proofwriter_fol_100.jsonl
    eval_note: Re-eval with correct test set (D062). Previous test_100.jsonl results
      invalidated.
- exp_id: exp1-random-b03-s44-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.23
    eval_proved_only_mean_isr: 0
    eval_mean_isr: 0
    eval_isr_std: 0
    eval_median_isr: 0
    eval_n_proved: 23
    eval_n_problems: 100
    eval_data: proofwriter_fol_100.jsonl
    h7_count: 0
    h7_rate: 0
    h7a_count: 0
    h7b_count: 0
    h1_count: 23
    h1_rate: 1
    h8_count: 0
    h8_rate: 0
    genuine_count: 0
    genuine_rate: 0
    taxonomy_tool: classify_h7.py standard (2026-05-15)
    taxonomy_note: 'Re-classified with current classify_h7.py. Matches previous values:
      H7=0, H1=23, H8=0, genuine=0. No change.'
- exp_id: exp1-isr-b03-s43-r3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    h8_audit_done: true
    h8_in_genuine: 1
    h8_sample: folio_558
    body_paren_h7_misses:
    - folio_732
    - folio_959
    genuine_pre_audit: 23
    genuine_post_full_audit: 20
    genuine_rate_corrected: 0.233
    audit_breakdown: 23 - 1(H8 folio_558) - 1(H7 folio_732) - 1(H7 folio_959) = 20
- exp_id: plan015-linear-s42
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp1-isr-b03-s43-r4
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp1-random-b03-s43-r2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp1-random-b03-s43-r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp1-random-b03-s43-r4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_step: 500
    prove_rate: 0.5505
    mean_isr: 0.1358
    parse_rate: 1
    train_loss: 0.01365
    train_runtime_sec: 6161.1
    epoch: 2
    eval_prove_rate: 0.92
    eval_mean_isr: 0.1659
    eval_isr_std: 0.1147
    eval_median_isr: 0.1429
    eval_proved_only_mean_isr: 0.1803
    eval_min_isr: 0
    eval_max_isr: 0.5
    eval_n_proved: 92
    eval_n_problems: 100
    eval_data: proofwriter_fol_100.jsonl
    eval_by_answer_type:
      'false':
        count: 25
        proved: 23
        prove_rate: 0.92
        mean_isr: 0.156
      unknown:
        count: 41
        proved: 37
        prove_rate: 0.902
        mean_isr: 0.184
      'true':
        count: 34
        proved: 32
        prove_rate: 0.941
        mean_isr: 0.151
    h7_count: 7
    h7_rate: 0.076
    h7a_count: 7
    h7b_count: 0
    h1_count: 82
    h1_rate: 0.891
    h8_count: 0
    h8_rate: 0
    genuine_count: 3
    genuine_rate: 0.0326
    taxonomy_tool: classify_h7.py standard (2026-05-15)
    taxonomy_note: 'Re-classified with current classify_h7.py. Matches previous strict
      values: H7=7, H1=82, H8=0, genuine=3. No change.'
- exp_id: plan004-o1-ablation-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    prove_rate: 0.63
    mean_isr: 0.0072
    h7_count: 0
    h7_rate: 0
    h1_count: 63
    h1_rate: 1
    h8_conjunction_collapse_count: 2
    h8_conjunction_collapse_rate: 0.0317
    genuine_count: 0
    genuine_rate: 0
    content_independent_predicates_count: 3
    h8_audit_note: '2026-05-15: H8 conjunction collapse added. genuine unchanged (0).'
- exp_id: plan002-additive-b01-s42-1000
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.9
    eval_mean_isr: 0.7892
    eval_isr_std: 0.3424
    eval_proved_only_isr: 0.8769
    eval_median_isr: 1
    eval_n_proved: 90
    eval_n_problems: 100
    eval_component_count_mean: 2.889
    tautological_collapse: true
    train_final_prove_rate: 0.855
    train_final_mean_isr: 0.532
    h7_count: 87
    h7_rate: 0.9667
    h1_count: 0
    h1_rate: 0
    h1_near_count: 1
    h1_near_rate: 0.0111
    h8_conjunction_collapse_count: 1
    h8_conjunction_collapse_rate: 0.0111
    genuine_count: 2
    genuine_rate: 0.0222
    taxonomy_standard: D086 clean run = ground truth. D084 residual removed.
- exp_id: plan009-sft-baseline-s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.2391
    train_token_accuracy: 0.9938
    train_epochs: 7.94
    train_runtime_sec: 677.14
    train_steps: 500
    eval_prove_rate: 0.15
    eval_mean_isr: 0.0895
    eval_isr_std: 0.2338
    eval_median_isr: 0
    eval_proved_only_isr: 0.5967
    h7_count: 0
    h7_rate: 0
    h1_count: 1
    h1_rate: 0.067
    genuine_count: 14
    genuine_rate: 0.933
    by_answer_type:
      'true':
        count: 34
        proved: 13
        prove_rate: 0.382
        mean_isr: 0.234
      'false':
        count: 25
        proved: 1
        prove_rate: 0.04
        mean_isr: 0.027
      unknown:
        count: 41
        proved: 1
        prove_rate: 0.024
        mean_isr: 0.008
    eval_data_path: data/proofwriter_fol_100.jsonl
    eval_output_path: /root/autodl-tmp/outputs/eval_sta_plan009_sft_s43.json
- exp_id: plan018-additive-random-b01-s42-1000
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan009-sft-baseline-s44
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_final_loss: 0.2397
    train_last_step_loss: 0.0328
    train_token_accuracy: 0.9928
    train_epochs: 7.94
    train_runtime_sec: 729.05
    train_steps: 500
    eval_prove_rate: 0.17
    eval_n_proved: 17
    eval_n_problems: 100
    eval_mean_isr: 0.0974
    eval_isr_std: 0.2409
    eval_median_isr: 0
    eval_proved_only_isr: 0.5729
    eval_data: proofwriter_fol_100.jsonl
    eval_method: eval_sta.py full STA
    eval_output_path: /root/autodl-tmp/outputs/eval_sta_plan009_sft_s44.json
    eval_tautological_collapse: false
    eval_h7_count: 0
    eval_h7_rate: 0
    eval_h1_count: 2
    eval_h1_rate: 0.118
    eval_genuine_count: 15
    eval_genuine_rate: 0.882
    eval_by_answer_type:
      'true':
        count: 34
        proved: 15
        prove_rate: 0.441
        mean_isr: 0.257
      'false':
        count: 25
        proved: 1
        prove_rate: 0.04
        mean_isr: 0.027
      unknown:
        count: 41
        proved: 1
        prove_rate: 0.024
        mean_isr: 0.008
    eval_correction_note: 'Corrected 2026-05-15: previous eval used test_100.jsonl
      (50/44/6 distribution), re-evaled with proofwriter_fol_100.jsonl (34/25/41)'
- exp_id: exp1-isr-b03-s42-1000
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp1-isr-b03-s42-1000-r2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.95
    eval_mean_isr: 0.734
    eval_isr_std: 0.2575
    eval_median_isr: 0.6
    eval_proved_only_isr: 0.7726
    eval_n_proved: 95
    eval_n_problems: 100
    eval_data: proofwriter_fol_100.jsonl
    eval_by_answer_type:
      'false':
        count: 25
        proved: 25
        prove_rate: 1
        mean_isr: 0.824
      unknown:
        count: 41
        proved: 38
        prove_rate: 0.927
        mean_isr: 0.673
      'true':
        count: 34
        proved: 32
        prove_rate: 0.941
        mean_isr: 0.741
    h7_count: 0
    h7_rate: 0
    h1_count: 54
    h1_rate: 0.568
    genuine_count: 0
    genuine_rate: 0
    tautological_collapse: true
    isr_1_count: 41
    isr_1_rate: 0.432
    single_premise_count: 0
    train_final_prove_rate: 0.829
    train_final_mean_isr: 0.727
    train_loss: 0.0041
    train_runtime_seconds: 6280
    train_final_entropy: 9.0e-06
    completions_mean_length: 47
    h8_conjunction_collapse_count: 41
    h8_conjunction_collapse_rate: 0.432
    content_independent_predicates: true
- exp_id: plan018-additive-random-b01-s42-1000-r2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    train_final_prove_rate: 0.989
    train_final_mean_isr: 0.353
    train_final_reward: 1.062
    train_steps: 1000
    train_runtime_seconds: 2957
    eval_prove_rate: 1
    eval_mean_isr: 0.3333
    eval_isr_std: 0
    eval_median_isr: 0.3333
    eval_proved_only_isr: 0.3333
    eval_n_proved: 100
    eval_n_problems: 100
    eval_component_count_mean: 3
    genuine_rate: 0
    genuine_count: 0
    tautological_collapse: true
    h7_rate: null
    h7_count: null
    h1_rate: null
    h1_count: null
- exp_id: plan018-additive-random-b01-s42-1000-r3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.97
    eval_mean_isr: 0.6892
    eval_isr_std: 0.2037
    eval_median_isr: 0.75
    eval_proved_only_isr: 0.7105
    eval_n_proved: 97
    eval_n_problems: 100
    genuine_count: 0
    genuine_rate: 0
    h1_count: 0
    h1_rate: 0
    h7_count: 97
    h7_rate: 1
    tautological_collapse: true
    train_final_prove_rate: 0.827
    train_final_mean_isr: 0.5213
    train_loss: 0.00671
    train_final_entropy: 0.003
    train_runtime_seconds: 5783
    train_steps: 1000
    eval_by_answer_type:
      'false':
        count: 25
        proved: 25
        prove_rate: 1
        mean_isr: 0.7533
      unknown:
        count: 41
        proved: 39
        prove_rate: 0.951
        mean_isr: 0.6565
      'true':
        count: 34
        proved: 33
        prove_rate: 0.971
        mean_isr: 0.6814
    n_premise_distribution:
      '1': 97
    pattern_description: 'All 97 proved: 1 premise identical to conclusion (P therefore
      P). D088 correction: h7=97 h1=0 (was h1=97 h7=0 pre-D086 bugfix).'
- exp_id: plan009-sft-baseline-s42-1000
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_final_loss: 0.0168
    train_last_step_loss: 0.0168
    train_token_accuracy: 0.9955
    train_epochs: 15.88
    train_runtime_sec: 1415
    train_steps: 1000
    eval_prove_rate: 0.13
    eval_n_proved: 13
    eval_n_problems: 100
    eval_mean_isr: 0.0738
    eval_isr_std: 0.2077
    eval_median_isr: 0
    eval_proved_only_isr: 0.5677
    eval_data: proofwriter_fol_100.jsonl
    eval_method: eval_sta.py full STA
    eval_output_path: /root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json
    h7_strict_count: 0
    h7_strict_rate: 0
    h1_strict_count: 1
    h1_strict_rate: 0.0769
    h8_conjunction_collapse_count: 0
    h8_conjunction_collapse_rate: 0
    genuine_count: 12
    genuine_rate: 0.9231
    conclusion_in_premise_count: 1
    conclusion_in_premise_rate: 0.0769
    isr_1_count: 0
    content_independent_count: 0
    eval_by_answer_type:
      'true':
        count: 34
        proved: 12
        prove_rate: 0.353
        mean_isr: 0.209
      'false':
        count: 25
        proved: 1
        prove_rate: 0.04
        mean_isr: 0.011
      unknown:
        count: 41
        proved: 0
        prove_rate: 0
        mean_isr: 0
- exp_id: plan009-sft-baseline-s43-1000
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.11
    n_proved: 11
    n_problems: 100
    mean_isr: 0.0699
    isr_std: 0.2155
    median_isr: 0
    proved_only_mean_isr: 0.6352
    by_answer_type:
      'true':
        count: 34
        proved: 11
        prove_rate: 0.3235
      'false':
        count: 25
        proved: 0
        prove_rate: 0
      unknown:
        count: 41
        proved: 0
        prove_rate: 0
    genuine_count: 10
    genuine_rate: 0.9091
    h7_strict_count: 0
    h7_strict_rate: 0
    h1_strict_count: 1
    h1_strict_rate: 0.0909
    h8_conjunction_collapse_count: 0
    h8_conjunction_collapse_rate: 0
    conclusion_in_premise_count: 1
    conclusion_in_premise_rate: 0.0909
    content_independent_count: 0
    content_independent_rate: 0
    isr_1_count: 1
    isr_1_rate: 0.0909
    train_final_loss: 0.0167
    train_avg_loss: 0.1551
    train_token_accuracy: 0.9954
    train_runtime_s: 1584.79
    eval_elapsed_s: 326.1
- exp_id: plan009-sft-baseline-s44-1000
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.15
    n_proved: 15
    n_problems: 100
    mean_isr: 0.0884
    isr_std: 0.2268
    median_isr: 0
    proved_only_mean_isr: 0.5892
    max_isr: 0.8571
    by_answer_type:
      'true':
        count: 34
        proved: 15
        prove_rate: 0.4412
      'false':
        count: 25
        proved: 0
        prove_rate: 0
      unknown:
        count: 41
        proved: 0
        prove_rate: 0
    genuine_count: 14
    genuine_rate: 0.9333
    h7_strict_count: 0
    h7_strict_rate: 0
    h1_strict_count: 1
    h1_strict_rate: 0.0667
    h8_conjunction_collapse_count: 0
    h8_conjunction_collapse_rate: 0
    conclusion_in_premise_count: 1
    conclusion_in_premise_rate: 0.0667
    content_independent_count: 0
    content_independent_rate: 0
    isr_1_count: 0
    isr_1_rate: 0
    train_final_loss: 0.0171
    train_avg_loss: 0.1544
    train_token_accuracy: 0.995
    train_runtime_s: 1580.97
    eval_elapsed_s: 391.8
- exp_id: plan009-sft-baseline-s44-1000-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan009-sft-baseline-s44-1000-r3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.15
    eval_n_proved: 15
    eval_n_problems: 100
    eval_mean_isr: 0.0884
    eval_isr_std: 0.2268
    eval_median_isr: 0
    eval_proved_only_isr: 0.5892
    eval_data: proofwriter_fol_100.jsonl
    eval_method: eval_sta.py full STA
    h7_count: 0
    h7_rate: 0
    h1_count: 1
    h1_rate: 0.0667
    h8_conjunction_collapse_count: 0
    h8_conjunction_collapse_rate: 0
    genuine_count: 14
    genuine_rate: 0.9333
    eval_by_answer_type:
      'true':
        count: 34
        proved: 15
        prove_rate: 0.441
        mean_isr: 0.26
      'false':
        count: 25
        proved: 0
        prove_rate: 0
        mean_isr: 0
      unknown:
        count: 41
        proved: 0
        prove_rate: 0
        mean_isr: 0
- exp_id: plan001-exec-only-s43-1000
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan001-exec-only-s44-1000
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan001-exec-only-s43-1000-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.9
    n_proved: 90
    n_problems: 100
    mean_isr: 0.531
    isr_std: 0.15
    isr_corrected: 0.465
    isr_artifact_note: n_components=3 quantifier decomposition artifact (+0.066) +
      $T solver bug 5 samples (+0.025). Corrected ISR=0.465, but both values entirely
      from H7a tautological necessity, no reasoning quality signal.
    h7_count: 90
    h7_rate: 1
    h7a_count: 90
    h7b_count: 0
    h1_count: 0
    h1_rate: 0
    h8_count: 0
    h8_rate: 0
    genuine_count: 0
    genuine_rate: 0
- exp_id: plan001-exec-only-s44-1000-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 1
    n_proved: 100
    n_problems: 100
    mean_isr: 0.002
    isr_std: 0.0146
    h7_count: 0
    h7_rate: 0
    h7a_count: 0
    h7b_count: 0
    h1_count: 85
    h1_rate: 0.85
    h8_count: 15
    h8_rate: 0.15
    genuine_count: 0
    genuine_rate: 0
    genuine_note: 'D091: 3 samples escape text-match classifiers but are functionally
      degenerate (ISR=0, disjunctive/commuted bypasses)'
- exp_id: plan018-additive-random-b01-s43-r3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    prove_rate: 0.94
    n_proved: 94
    n_problems: 100
    mean_isr: 0.1406
    isr_std: null
    proved_only_isr: 0.1495
    h7_count: 36
    h7_rate: 0.383
    h7a_count: 36
    h7b_count: 0
    h1_count: 56
    h1_rate: 0.596
    h8_count: 1
    h8_rate: 0.011
    genuine_count: 1
    genuine_rate: 0.0106
    train_prove_rate: 0.5825
    train_mean_isr: 0.1266
    taxonomy_tool: classify_h7.py + manual subtype analysis (2026-05-15)
    taxonomy_note: 'D093 H7 subtype: all 36 H7 are H7a (text-match tautology), 0 H7b.
      single_premise_count=0: Random H7a are multi-premise proofs with embedded tautological
      premise, structurally different from exec-only H7a (single-premise minimal tautology).
      H7b confirmed absent in Random condition.'
    h7a_structural_note: Random H7a = multi-premise with embedded matching premise;
      exec-only H7a = single-premise P-therefore-P
- exp_id: plan018-additive-random-b01-s44-r2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    train_prove_rate: 0.64675
    train_mean_isr: 0.08092
    train_loss: 0.00937
    train_steps: 500
    train_runtime_sec: 4998
    eval_prove_rate: 0.89
    eval_mean_isr: 0.0619
    eval_isr_std: 0.1756
    eval_median_isr: 0
    eval_isr_pr_ratio: 0.0695
    eval_proved_only_isr: 0.0695
    eval_n_proved: 89
    eval_n_problems: 100
    h7_count: 0
    h7a_count: 0
    h7b_count: 0
    h1_count: 73
    h8_count: 16
    genuine_count: 6
    genuine_rate: 0.067
    h7_rate: 0
    h1_rate: 0.82
    h8_rate: 0.18
    content_independent_count: 18
- exp_id: plan002-additive-b01-s43-r2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_n_problems: 100
    eval_n_proved: 61
    eval_prove_rate: 0.61
    eval_mean_isr: 0.5063
    eval_isr_std: 0.4518
    eval_median_isr: 0.5
    eval_proved_only_isr: 0.8301
    h7a_count: 59
    h7b_count: 2
    h7_count: 61
    h7_rate: 1
    h1_count: 0
    h1_rate: 0
    h8_conjunction_collapse_count: 0
    h8_conjunction_collapse_rate: 0
    genuine_count: 0
    genuine_rate: 0
    proved_single_premise_ratio: 1
    content_independent_predicates: 5
    isr_eq_1_count: 40
    isr_eq_1_rate_of_proved: 0.656
    train_prove_rate: 0.68775
    train_mean_isr: 0.5039
- exp_id: sweep-isr-b005-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.55
    eval_mean_isr: 0.602
    eval_proved_only_isr: 0.759
    genuine_rate: 0
    h7a_rate: 1
    h7b_rate: 0
    h1_rate: 0
    h8_rate: 0
    h7_count: 55
    genuine_count: 0
    n_proved: 55
    n_total: 100
- exp_id: sweep-isr-b01-s45
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    prove_rate: 0.2357
    prove_rate_last50: 0.475
    isr_mean: 0.1127
    isr_mean_last50: 0.2172
    reward_mean: 0.247
    loss: 0.0106
    parse_rate: 1
    steps_completed: 219
    steps_total: 500
    kill_reason: SIGKILL exit 137 (system OOM killer)
    checkpoint: checkpoint-200
- exp_id: plan002-additive-b01-s45
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.42
    eval_mean_isr: 0.2542
    eval_isr_std: 0.3261
    eval_proved_only_isr: 0.6052
    eval_median_isr: 0
    eval_n_proved: 42
    eval_n_problems: 100
    h7a_rate: 0.381
    h7b_rate: 0
    h7_rate: 0.381
    h1_rate: 0.048
    h8_rate: 0.024
    genuine_count: 23
    genuine_rate: 0.548
    genuine_pct_total: 23
    h7_count: 16
    h1_count: 2
    h8_count: 1
    eval_data: proofwriter_fol_100.jsonl
    eval_method: eval_sta.py + classify_h7.py
    taxonomy_standard: C013
- exp_id: plan002-additive-b01-s46
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.77
    eval_mean_isr: 0.3164
    eval_isr_std: 0.2959
    eval_proved_only_isr: 0.411
    eval_median_isr: 0.25
    eval_n_proved: 77
    eval_n_problems: 100
    h7a_rate: 0.143
    h7b_rate: 0
    h7_rate: 0.143
    h1_rate: 0.26
    h8_rate: 0.052
    genuine_count: 42
    genuine_rate: 0.545
    genuine_pct_total: 42
    h7_count: 11
    h1_count: 20
    h8_count: 4
    eval_data: proofwriter_fol_100.jsonl
    eval_method: eval_sta.py + classify_h7.py
    taxonomy_standard: C013
- exp_id: plan018-additive-random-b01-s45
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.58
    eval_n_proved: 58
    eval_n_problems: 100
    eval_mean_isr: 0.0096
    eval_proved_only_isr: 0.0166
    h7_count: 0
    h7_rate: 0
    h1_count: 53
    h1_rate: 0.914
    h8_count: 0
    h8_rate: 0
    genuine_count: 5
    genuine_rate: 0.086
    eval_data: proofwriter_fol_100.jsonl
    eval_method: eval_sta.py + classify_h7.py
- exp_id: plan018-additive-random-b01-s46
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.94
    eval_mean_isr: 0.0424
    h7_count: 86
    h1_count: 2
    h8_count: 4
    genuine_count: 2
    genuine_rate: 0.021
- exp_id: plan001-exec-only-s45
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan001-exec-only-s46
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.93
    mean_isr: 0.083
    genuine_pct: 9.7
    h1_pct: 89.2
    h7_pct: 0
    h8_pct: 4.3
    n_proved: 93
    n_problems: 100
- exp_id: w2-qwen3-7b-pilot
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: sweep-isr-b005-s43
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.99
    eval_n_proved: 99
    eval_n_problems: 100
    eval_mean_isr: 0.5517
    eval_isr_std: 0.1597
    eval_median_isr: 0.5
    eval_proved_only_isr: 0.5572
    train_prove_rate: 0.752
    train_mean_isr: 0.364
    eval_data: proofwriter_fol_100.jsonl
    eval_method: eval_sta.py + classify_h7.py
    h7_count: 96
    h7_rate: 0.97
    h7a_count: 96
    h7b_count: 0
    h1_count: 0
    h1_rate: 0
    h8_count: 0
    h8_rate: 0
    genuine_count: 3
    genuine_rate: 0.03
- exp_id: sweep-isr-b005-s44
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    prove_rate: 0.99
    mean_isr: 0.5539
    isr_std: 0.175
    median_isr: 0.5
    H7_rate: 0.869
    H7_count: 86
    H1_exact_count: 1
    H8_count: 2
    genuine_count: 10
    genuine_rate: 0.101
    n_proved: 99
    n_total: 100
    train_final_reward: 1.029
    train_final_prove_rate: 0.7085
    train_mean_isr: 0.381
    entropy_final: 0.075
    eval_data: proofwriter_fol_100.jsonl
- exp_id: sweep-isr-b02-s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 1
    eval_mean_isr: 0.6017
    eval_isr_std: 0.1973
    eval_median_isr: 0.5
    eval_isr_pr_ratio: 0.6017
    eval_min_isr: 0.3333
    eval_max_isr: 1
    h7a: 100
    h7b: 0
    h7_total: 100
    h1_strict: 0
    h8: 0
    genuine: 0
    genuine_pct: 0
    content_independent: 99
    single_premise_pct: 1
- exp_id: sweep-isr-b02-s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.5998
    mean_isr: 0.1812
    train_loss: 0.01294
    eval_prove_rate: 0.96
    eval_mean_isr: 0.5298
    eval_proved_only_isr: 0.5519
    genuine_rate: 0
    h7a_rate: 0.969
    h7b_rate: 0
    h1_rate: 0.01
    h8_rate: 0.021
    steps_completed: 500
    steps_total: 500
- exp_id: sweep-isr-b02-s44
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.7015
    mean_isr: 0.503
    train_loss: 0.02009
    parse_rate: 1
    steps_completed: 500
    steps_total: 500
    train_runtime_sec: 3562
    frac_reward_zero_std_final: 1
    entropy_final: 0.041
    eval_prove_rate: 0.94
    eval_mean_isr: 0.9058
    eval_isr_std: 0.2663
    genuine_rate: 0
    h7a_rate: 1
    h7b_rate: 0
    h1_rate: 0
    h8_rate: 0
    single_premise_pct: 1
    content_independent_pct: 0.043
    isr_100_pct: 0.925
- exp_id: sweep-random-b01-s45
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.58
    eval_n_proved: 58
    eval_n_problems: 100
    eval_mean_isr: 0.0096
    eval_proved_only_isr: 0.0166
    h7_count: 0
    h7_rate: 0
    h1_count: 53
    h1_rate: 0.914
    h8_count: 0
    h8_rate: 0
    genuine_count: 5
    genuine_rate: 0.086
    eval_data: proofwriter_fol_100.jsonl
    eval_method: eval_sta.py + classify_h7.py
    source: linked from plan018-additive-random-b01-s45
- exp_id: sweep-isr-b01-s46
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: sweep-random-b01-s46
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.94
    eval_n_proved: 94
    eval_n_problems: 100
    eval_mean_isr: 0.0424
    h7_count: 86
    h7_rate: 0.915
    h1_count: 2
    h1_rate: 0.021
    h8_count: 4
    h8_rate: 0.043
    genuine_count: 2
    genuine_rate: 0.021
    eval_data: proofwriter_fol_100.jsonl
    eval_method: eval_sta.py + classify_h7.py
    source: linked from plan018-additive-random-b01-s46
- exp_id: sweep-exec-only-s45
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: sweep-exec-only-s46
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: plan018-random-b01-s45-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: plan018-additive-random-b01-s45-r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: sweep-exec-only-s45-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.74025
    mean_isr: 0.3596
    train_loss: 0.0273
    parse_rate: 1
    steps_completed: 500
    steps_total: 500
    train_runtime_sec: 3282
    entropy_final: 0.045
    eval_prove_rate: 0.99
    eval_n_proved: 99
    eval_n_problems: 100
    eval_mean_isr: 0.5012
    eval_isr_std: 0.2055
    eval_median_isr: 0.5
    eval_proved_only_isr: 0.5062
    eval_data: proofwriter_fol_100.jsonl
    eval_by_answer_type:
      'false':
        count: 25
        proved: 25
        prove_rate: 1
        mean_isr: 0.59
      unknown:
        count: 41
        proved: 41
        prove_rate: 1
        mean_isr: 0.476
      'true':
        count: 34
        proved: 33
        prove_rate: 0.971
        mean_isr: 0.467
    h7a_count: 93
    h7a_rate: 0.939
    h7b_count: 0
    h7_count: 93
    h7_rate: 0.939
    h1_count: 5
    h1_rate: 0.051
    h8_count: 1
    h8_rate: 0.01
    genuine_count: 1
    genuine_rate: 0.01
    content_independent_count: 47
    single_premise_count: 92
    taxonomy_tool: classify_h7.py standard (2026-05-16)
- exp_id: w2-qwen3-8b-exec-pilot
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: w2-qwen3-8b-isr-pilot
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: w2-qwen3-8b-exec-pilot-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: w2-qwen3-8b-isr-pilot-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: w2-qwen3-1.7b-exec-pilot
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    prove_rate: 3
    genuine_rate: 0
    n_proved: 3
    n_genuine: 0
    n_H7a: 3
    mean_isr: 0.015
    note: '1.7B exec-only: 3% raw PR but 100% H7a tautology, 0 genuine proofs'
- exp_id: w2-qwen3-1.7b-isr-pilot
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.93
    mean_isr: 0.2625
    isr_std: 0.0752
    median_isr: 0.2857
    n_proved: 93
    n_problems: 100
    h7_count: 0
    h7_rate: 0
    h1_count: 0
    h1_rate: 0
    h8_count: 0
    h8_rate: 0
    genuine_count: 0
    genuine_rate: 0
    h9_count: 93
    h9_rate: 1
    mode_collapse: true
    collapse_onset_step: 463
    hacking_type: 'H9: ex falso quodlibet / contradiction injection'
    note: All 93 proofs inject contradictory premises (P(a) ∧ ¬P(a)) using generic
      predicates. Prover9 proves anything from contradiction. Bypasses H7/H1/H8 detectors.
      ISR≈2/7 constant. Zero semantic relation to original problems.
- exp_id: gated-isr-t03-s42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: gated-isr-t03-s43
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: gated-isr-curriculum-t02-s42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: gated-isr-curriculum-t02-s43
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: gated-isr-curriculum-t02-s42-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: gated-isr-curriculum-t02-s43-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exec-retrain-for-warmstart-s42
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exec-retrain-v3-s42
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exec-retrain-v3-s43
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: gated-isr-warmstart-t02-s42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: gated-isr-warmstart-t02-s43
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: gated-isr-warmstart-t02-s43-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.21
    mean_isr: 0.028
    n_proved: 21
    n_problems: 100
    genuine_pct_raw: 95.2
    genuine_pct_c013: 76.2
    genuine_pct_strict: 38.1
    h7_count: 1
    h8a_isr0_count: 4
    h8b_no_premise_nec: 8
    total_hacking_strict: 13
    genuine_count_c013: 16
    genuine_count_strict: 8
- exp_id: gated-isr-warmstart-t015-s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.41
    mean_isr: 0.0512
    mean_isr_proved: 0.1248
    n_proved: 41
    n_problems: 100
    genuine_pct_raw: 97.6
    genuine_pct_c013: 63.4
    genuine_pct_strict: 48.8
    h7_count: 1
    h8a_isr0_count: 14
    h8b_no_premise_nec: 6
    total_hacking_strict: 21
    genuine_count_c013: 26
    genuine_count_strict: 20
- exp_id: w2-qwen3-1.7b-isr-b03
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.17
    mean_isr: 0.0309
    n_proved: 17
    n_problems: 100
    h7_pct: 0
    h1_pct: 70.6
    h8_pct: 0
    genuine_pct: 29.4
    genuine_count: 5
    content_independent: 1
    strict_genuine_count: 5
    strict_genuine_pct_proved: 29.4
    strict_genuine_pct_total: 5
    h1_near_count: 2
    strict_genuine_excl_h1near: 3
    training_collapsed: false
    audit_note: 'D130 re-audit: 5/5 genuine are content-dependent. 2/5 are H1-near
      (conjunction reorder, universal instantiation). 3/5 require multi-step reasoning.'
- exp_id: w2-qwen3-1.7b-random-b01
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.93
    genuine_pct: 0
    h9_rate: 1
    mean_isr: 0.028
    n_proved: 93
    n_problems: 100
- exp_id: w2-qwen3-1.7b-isr-b01
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 1
    mean_isr: 0.6
    isr_std: 0
    n_proved: 100
    n_problems: 100
    h7_pct: 0
    h1_pct: 100
    h8_pct: 0
    genuine_pct: 0
    genuine_count: 0
- exp_id: exec-only-s43-1000step-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exec-only-s43-1000step-r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exec-only-s43-1000step-r4
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exec-only-s43-1000step-r5
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exec-only-s43-1000step-r6
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exec-only-s43-1000step-r7
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_prove_rate: 0.96
    eval_mean_isr: 0.0818
    h7_count: 0
    h1_count: 90
    h8_count: 0
    genuine_count: 6
    genuine_rate: 0.062
    content_independent: 4
- exp_id: sweep-random-b005-s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0
    eval_n_proved: 0
    eval_n_problems: 100
    eval_mean_isr: 0
    h7_count: 0
    h7_rate: 0
    h1_count: 0
    h1_rate: 0
    h8_count: 0
    h8_rate: 0
    genuine_count: 0
    genuine_rate: 0
    eval_data: proofwriter_fol_100.jsonl
    eval_method: eval_sta.py + classify_h7.py
    note: 'Complete training failure: β=0.05 random signal too weak for 500-step learning'
- exp_id: sweep-random-b005-s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.62
    eval_n_proved: 62
    eval_n_problems: 100
    eval_mean_isr: 0.0058
    h7_count: 0
    h7_rate: 0
    h7a_count: 0
    h7b_count: 0
    h1_count: 48
    h1_rate: 0.774
    h8_count: 7
    h8_rate: 0.113
    genuine_count: 8
    genuine_rate: 0.129
    eval_data: proofwriter_fol_100.jsonl
    eval_method: eval_sta.py + classify_h7.py
    train_runtime_s: 6998
    note: β=0.05 random s43 learns (PR=62%) unlike s42 (PR=0%). Hacking mode H1 redundancy
      (77.4%), not H7 tautology. Huge seed variance at β=0.05.
- exp_id: sweep-random-b005-s44
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.07
    proved: 7
    total: 100
    mean_isr: 0
    isr_std: 0
    H7: 0
    H7a: 0
    H7b: 0
    H1: 5
    H8: 2
    genuine: 0
    genuine_rate: 0
- exp_id: plan002-additive-b01-s45-1000
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    prove_rate: 0.02
    proved: 2
    total: 100
    mean_isr: 0.01
    isr_std: 0.0704
    H7: 2
    H7a: 2
    H7b: 0
    H1: 0
    H8: 0
    genuine: 0
    genuine_rate: 0
- exp_id: d129-1.7b-isr-b01-s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.6
    non_hacking_rate: 0
    isr_star: 0.75
    H1_pct: 0
    H7_pct: 100
    H8_pct: 0
    H9_pct: 0
    genuine_pct: 0
    dominant_mode: H7a
    eval_decoding: greedy
    eval_data: proofwriter_fol_100.jsonl
    mean_isr: 0.45
    proved_only_isr: 0.75
- exp_id: d129-1.7b-isr-b01-s44
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.82
    non_hacking_rate: 0.427
    isr_star: 0.4398
    H1_pct: 39
    H7_pct: 0
    H8_pct: 18.3
    H9_pct: 0
    genuine_pct: 42.7
    dominant_mode: H1(mixed)
    eval_decoding: greedy
    eval_data: proofwriter_fol_100.jsonl
- exp_id: d129-1.7b-random-b01-s43
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: d129-1.7b-random-b01-s44
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: d129-1.7b-isr-b03-s43
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: d129-1.7b-isr-b03-s44
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: d129-1_7b-random-b01-s43-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 1
    mean_isr: 0.0511
    isr_std: 0.094
    H1_pct: 76
    H7_pct: 0
    H8_pct: 0
    genuine_pct: 24
    content_independent_pct: 100
    training_steps: 500
    final_reward: 1.0526
    train_loss: 0.0372
- exp_id: d129-1_7b-random-b01-s44
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 1
    mean_isr: 0.0072
    isr_std: 0.0295
    median_isr: 0
    H1_pct: 84
    H7_pct: 0
    H8_pct: 0
    genuine_pct: 16
    content_independent_pct: 100
    n_problems: 100
    n_proved: 100
- exp_id: d129-1_7b-isr-b03-s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    PR: 0.52
    ISR_star: 0.2308
    H1_pct: 26.9
    H7_pct: 0
    H8_pct: 0
    non_hacking_pct: 73.1
    content_independent_pct: 100
    strict_genuine_pct: 0
    total_samples: 100
    proved_count: 52
- exp_id: d129-1_7b-isr-b03-s44
  name: ''
  status: DONE
  conclusion: success
  metrics:
    PR: 0.92
    ISR_star: 0.236
    H1_pct: 1.1
    H7_pct: 0
    H8_pct: 1.1
    non_hacking_pct: 97.8
    content_independent_pct: 100
    strict_genuine_pct: 0
    total_samples: 100
    proved_count: 92
- exp_id: d134-4b-isr-b01-s47
  name: ''
  status: DONE
  conclusion: success
  metrics:
    PR: 0.97
    proved: 97
    total: 100
    H1: 1
    H7: 83
    H7a: 83
    H8: 10
    H9: 0
    CI: 8
    genuine: 3
    genuine_pct: 3.1
    S-NH_pct: 3.1
- exp_id: d134-4b-isr-b01-s48
  name: ''
  status: DONE
  conclusion: success
  metrics:
    PR: 0.66
    proved: 66
    total: 100
    H1: 0
    H7: 66
    H7a: 66
    H8: 0
    H9: 0
    CI: 0
    genuine: 0
    genuine_pct: 0
    S-NH_pct: 0
    note: Pure H7 collapse — 100% of proved are H7
- exp_id: d134-4b-isr-b01-s49
  name: ''
  status: DONE
  conclusion: success
  metrics:
    PR: 0.86
    proved: 86
    total: 100
    H1: 6
    H7: 73
    H7_rate: 0.8488
    H8: 6
    H9: 0
    CI: 0
    genuine: 1
    genuine_pct: 1.16
    S-NH: 1
    S-NH_pct: 1.16
- exp_id: d134-4b-isr-b01-s50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    PR: 0.98
    proved: 98
    total: 100
    H7_rate: 0.857
    genuine_pct: 6.1
- exp_id: d134-4b-isr-b01-s51
  name: ''
  status: DONE
  conclusion: success
  metrics:
    PR: 0.98
    proved: 98
    total: 100
    H1: 0
    H7: 96
    H7_rate: 0.98
    H8: 1
    H9: 0
    genuine: 1
    genuine_pct: 1
- exp_id: d134-4b-random-b01-s47
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.89
    eval_n_proved: 89
    eval_n_problems: 100
    eval_mean_isr: 0.0857
    eval_isr_std: 0.1259
    eval_median_isr: 0
    eval_proved_only_mean_isr: 0.0963
    classify_h7_count: 0
    classify_h7_pct: 0
    classify_h1_strict_count: 79
    classify_h1_pct: 88.76
    classify_h8_conjunction: 4
    classify_h8_pct: 4.49
    classify_genuine_count: 6
    classify_genuine_pct: 6.74
    classify_conclusion_in_premise: 79
    train_final_prove_rate: 0.62875
    train_final_mean_isr: 0.1229
    train_loss: 0.0093
    train_steps: 500
    note: eval PR=89% (held-out proofwriter_fol_100.jsonl); train PR=0.629 is batch
      moving avg, NOT eval
- exp_id: d134-4b-random-b01-s48
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.93
    eval_n_proved: 93
    eval_n_problems: 100
    classify_h7_pct: 3.2
    classify_h1_pct: 80.6
    classify_h8_pct: 15.1
    classify_genuine_pct: 4.3
    train_steps: 500
    note: cron 误报 failed (pipeline 在 train PID 退出后继续 eval/classify, cron 检测到 train
      PID 退出即判 failed); 实际 train+eval+classify 全部正常完成
- exp_id: d134-4b-random-b01-s49
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_prove_rate: 0.05
    eval_n_proved: 5
    eval_n_problems: 100
    eval_avg_time: 10.5
    classify_h7_count: 1
    classify_h7_pct: 20
    classify_h1_strict_count: 4
    classify_h1_pct: 80
    classify_h8_conjunction: 0
    classify_h8_pct: 0
    classify_genuine_count: 0
    classify_genuine_pct: 0
    train_final_prove_rate: 0.675
    train_steps: 500
    diagnosis: 'repetition collapse: model generates 3-5 premises then infinite repeat
      loop; train PR=67.5% (short batches) but eval PR=5% (100 unseen problems all
      hit timeout); NOT a bug, same seed under ISR gives PR=86%'
- exp_id: d134-4b-random-b01-s50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.45
    mean_isr: 0.0258
    proved_only_mean_isr: 0.0573
    h7_total_rate: 0.0889
    h1_strict_rate: 0.8667
    h8_conjunction_collapse_rate: 0
    genuine_rate: 0.0444
    genuine_count: 2
- exp_id: d134-4b-random-b01-s51
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.65
    mean_isr: 0.2223
    proved_only_mean_isr: 0.342
    h7_total_rate: 0.0154
    h1_strict_rate: 0.5538
    h8_conjunction_collapse_rate: 0.2923
    genuine_rate: 0.1385
    genuine_count: 9
- exp_id: d142-gated-isr-s52
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: d142-gated-isr-s53
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: d142-gated-isr-s54
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: d142-gated-isr-s55
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 1
    isr: 0.525
    TS_pct: 82
    CE_pct: 0
    PG_pct: 15
    CI_pct: 0
    genuine_pct: 3
- exp_id: d142-gated-isr-s56
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.36
    isr: 0.2925
    TS_pct: 0
    CE_pct: 0
    PG_pct: 83
    CI_pct: 75
    genuine_pct: 17
- exp_id: d142-gated-isr-s57
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.88
    isr: 0.4497
    TS_pct: 1
    CE_pct: 20
    PG_pct: 15
    CI_pct: 0
    genuine_pct: 64
- exp_id: d143-pw-exec-s42
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d143-pw-exec-s43
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d143-pw-exec-s44
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d143-pw-isr-s42
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d143-pw-isr-s43
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d143-pw-isr-s44
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d143-pw-random-s42
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d143-pw-sft-s42
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d143-pw-extended-s42
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d144-llama-exec-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    prove_rate: 0
    reward: 0
    parse_rate: 1
    steps_completed: 72
    reason: LLaMA-3.2-3B base below GRPO cold-start threshold for FOL. 72 steps all-zero
      reward/loss/grad_norm, model weights never updated.
- exp_id: d143-pw-sta-s42
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d143-pw-sta-s43
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d143-pw-sta-s44
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d144-llama-exec-s43
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d144-llama-exec-s44
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d144-llama-isr-s42
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d144-llama-isr-s43
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d144-llama-isr-s44
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: d146-pf-exec-s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    reward: 1
    prove_rate: 1
    isr: 0
    steps_completed: 500
    classify_proved: 99
    classify_genuine: 0
    classify_genuine_rate: 0
    classify_TS: 99
    classify_CE: 0
    classify_PG: 0
    classify_CI: 0
- exp_id: d146-pf-exec-s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    reward: 1
    prove_rate: 1
    isr_mean: 0.2048
    parse_rate: 1
    prove_rate_mean_all: 0.4143
    prove_rate_final50: 0.55
    isr_final50: 0.119
    steps_completed: 500
    classify_proved: 63
    classify_genuine: 32
    classify_genuine_rate: 0.508
    classify_TS: 0
    classify_CE: 31
    classify_PG: 0
    classify_CI: 0
- exp_id: d146-pf-exec-s44
  name: ''
  status: DONE
  conclusion: success
  metrics:
    reward: 1
    prove_rate: 1
    isr: 0.043
    parse_rate: 1
    steps_completed: 500
    classify_proved: 72
    classify_genuine: 1
    classify_genuine_rate: 0.014
    classify_TS: 0
    classify_CE: 71
    classify_PG: 0
    classify_CI: 0
- exp_id: d146-pf-isr-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    reward_final: 0
    prove_rate_final: 0
    isr_final: 0
    parse_rate: 1
    prove_rate_mean: 0.354
    prove_rate_final50: 0.35
    isr_mean: 0.12
    isr_peak: 0.409
    steps_completed: 500
    note: 'bimodal: 38% PR=0, 36.8% PR=0.5, 10.8% PR=1.0; saturated after step 300'
    classify_proved: 46
    classify_genuine: 46
    classify_genuine_rate: 1
    classify_TS: 0
    classify_CE: 0
    classify_PG: 0
    classify_CI: 0
- exp_id: d146-pf-isr-s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    reward_final: 1.02
    prove_rate_final: 1
    isr_final: 0.205
    parse_rate: 1
    steps_completed: 500
    note: partial recovery is to CE hacking (70% CE, 30.4% genuine), not genuine reasoning.
      Only ISR seed with hacking — parallels pattern of convergence=hacking across
      both exec and ISR conditions.
    classify_proved: 56
    classify_genuine: 17
    classify_genuine_rate: 0.304
    classify_TS: 0
    classify_CE: 39
    classify_PG: 0
    classify_CI: 0
- exp_id: d146-pf-isr-s44
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    reward_final: 0
    prove_rate_final: 0
    isr_final: 0
    parse_rate: 1
    prove_rate_mean: 0.454
    prove_rate_final50: 0.487
    isr_mean: 0.131
    isr_final50: 0.145
    isr_peak: 0.351
    steps_completed: 500
    note: oscillating; 366/500 steps nonzero PR; nz_mean PR=0.620, ISR=0.178
    classify_proved: 66
    classify_genuine: 66
    classify_genuine_rate: 1
    classify_TS: 0
    classify_CE: 0
    classify_PG: 0
    classify_CI: 0
- exp_id: d146-pf-pipeline
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: d154-8b-exec-s42
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: d154-8b-exec-s43
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: d154-8b-exec-s44
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: d154-8b-isr-s42
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: d154-8b-isr-s43
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: d154-8b-exec-s42-r2
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: d154-8b-exec-s42-r3
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: d154-8b-exec-s42-k4
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: d154-8b-exec-s42-k4v2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    prove_rate: 0.155
    mean_isr: 0.082
    parse_rate: 1
    train_loss: 0.0149
    training_steps: 500
    training_time_sec: 9395
    converged: false
    frac_reward_zero_std: 1
    failure_mode: training_stagnation_k4_insufficient
    note: 'K=4 insufficient for 8B: cold-start stagnation, not Goodhart collapse.
      All 4 samples produce near-identical outputs, zero GRPO gradient.'
- exp_id: d157-shuffled-isr-s42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: d157-shuffled-isr-s43
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.16
    mean_isr: 0.0908
    proved_only_mean_isr: 0.5675
    n_proved: 16
    genuine_count: 14
    genuine_rate: 0.875
    TS_count: 1
    CE_count: 1
    PG_count: 0
    CI_count: 0
    isr_std: 0.2314
    median_isr: 0
    max_isr: 0.8889
- exp_id: d157-shuffled-isr-s44
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.15
    mean_isr: 0.0813
    proved_only_mean_isr: 0.5423
    n_proved: 15
    genuine_count: 13
    genuine_rate: 0.867
    TS_count: 1
    CE_count: 1
    PG_count: 0
    CI_count: 0
- exp_id: d158-llama-sft-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    prove_rate: 0
    mean_isr: 0
    n_proved: 0
    n_total: 100
    gate_passed: false
    failure_mode: generation_degeneracy_and_unicode_fol_syntax_mismatch
    note: 'LLaMA SFT warmstart failed: model outputs Unicode FOL (∀, →, ∧) but Prover9
      requires ASCII (all, ->, &). PR=0/100.'
- exp_id: d158-llama-grpo-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: d158_llama_sft_s42
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: d157-shuffled-isr-s42-r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: d157-shuffled-isr-s42-r3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    prove_rate: 0.15
    mean_isr: 0.0851
    proved_only_mean_isr: 0.5673
    n_proved: 15
    genuine_count: 13
    genuine_rate: 0.8667
    TS_count: 1
    CE_count: 1
    PG_count: 0
    CI_count: 0
    isr_std: 0.2265
    median_isr: 0
- exp_id: d165-llama-exec-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    prove_rate: 0.14
    n_proved: 14
    n_problems: 100
    proved_only_mean_isr: 0.5467
    TS_count: 0
    TS_rate: 0
    CE_count: 2
    CE_rate: 0.143
    PG_count: 0
    PG_rate: 0
    CI_count: 2
    CI_rate: 0.143
    genuine_count: 12
    genuine_rate: 0.857
    by_answer_type:
      'true':
        count: 34
        proved: 14
        pr: 0.412
      'false':
        count: 25
        proved: 0
        pr: 0
      unknown:
        count: 41
        proved: 0
        pr: 0
    train_prove_rate: 0.0993
    train_mean_isr: 0.0478
    train_loss: 0.0665
    train_runtime_sec: 4513
- exp_id: d165-llama-exec-s43
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    prove_rate: 0.15
    n_proved: 15
    n_problems: 100
    proved_only_mean_isr: 0.5658
    mean_isr: 0.0849
    TS_count: 0
    TS_rate: 0
    CE_count: 2
    CE_rate: 0.133
    PG_count: 0
    PG_rate: 0
    genuine_count: 13
    genuine_rate: 0.867
    by_answer_type:
      'true':
        count: 34
        proved: 15
        pr: 0.441
      'false':
        count: 25
        proved: 0
        pr: 0
      unknown:
        count: 41
        proved: 0
        pr: 0
    train_prove_rate: 0.101
    train_mean_isr: 0.049
    train_loss: 0.073
    train_runtime_sec: 4438
- exp_id: d165-llama-exec-s44
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    PR: 0.16
    ISR_star: 0.5492
    genuine_pct: 87.5
    n_proved: 16
    hacking_modes:
      CE: 2
      TS: 0
      PG: 0
      CI: 0
    genuine_count: 14

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
  "promptId": "945f12ce-e0ad-4226-9ca0-653dc3da0cc8",
  "type": "user",
  "uuid": "5a686935-0f10-4e1f-be9a-e063ee59281e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T21:55:36.356Z_

```json
{
  "parentUuid": "5a686935-0f10-4e1f-be9a-e063ee59281e",
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
  "uuid": "5baae6e2-ab2d-4612-9631-f59143af6acc",
  "timestamp": "2026-05-21T21:55:36.356Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T21:55:36.356Z_

```json
{
  "parentUuid": "5baae6e2-ab2d-4612-9631-f59143af6acc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a67efa3b-1904-4640-a45e-4010e24b8021",
  "timestamp": "2026-05-21T21:55:36.356Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：8B退化确认但模式同质（均为H7）或程度较弱，cross-scale成立但taxonomy分化贡献有限 核心假设：['8B exec-only成功训练但dominant mode与4B相同（均为H7），或hacking rate 50-80%弱于4B', 's45/s46 1000步至少1个确认ISR崩塌…",
  "leafUuid": "a67efa3b-1904-4640-a45e-4010e24b8021",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier cross-scale degeneration and Goodhart transience",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf"
}
```

---

### Assistant

_source line 8 · 2026-05-21T21:55:45.126Z_

I'll analyze the experiment plan and generate detailed predicted data for the median tier. Let me first check the current state of planned experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a67efa3b-1904-4640-a45e-4010e24b8021",
  "isSidechain": false,
  "requestId": "req_011CbGTd6BsPj32sgTBt8zhg",
  "type": "assistant",
  "uuid": "6c929f58-ab39-4e81-a051-3b783df1c2a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AejjnFpGYQk3CzPF161cfS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 47306,
      "cache_read_input_tokens": 11841,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 47306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 155,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 47306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 47306
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

### Tool call

_source line 9 · 2026-05-21T21:55:46.733Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01NYJj95jgeaiFhLGLwPTAG2`</summary>

```json
{
  "pattern": "status: planned",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "output_mode": "content",
  "-B": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c929f58-ab39-4e81-a051-3b783df1c2a9",
  "isSidechain": false,
  "requestId": "req_011CbGTd6BsPj32sgTBt8zhg",
  "type": "assistant",
  "uuid": "f95d8e47-534d-4430-94e3-2d8feb39e38a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AejjnFpGYQk3CzPF161cfS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 47306,
      "cache_read_input_tokens": 11841,
      "output_tokens": 155,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 47306,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 155,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 47306,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 47306
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

### Tool result

_source line 10 · 2026-05-21T21:55:50.514Z_

<details><summary>↩ Tool result · `toolu_01NYJj95jgeaiFhLGLwPTAG2`</summary>

```text
&lt;persisted-output>
Output too large (43KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3/480b4572-d972-4cac-a4ad-1f7e0e6dbacf/tool-results/toolu_01NYJj95jgeaiFhLGLwPTAG2.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/logs/phase2_median_attempt0.log-20-[Omitted long context line]
projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/logs/phase2_median_attempt0.log-21-{"type":"system","subtype":"task_progress","task_id":"a84a33cd28f662899","tool_use_id":"toolu_01T1B7xak22sQREZCq6w1kk9","description":"Reading projects/min_necessary_circuit_css/experiment_plan.yaml","usage":{"total_tokens":25323,"tool_uses":5,"duration_ms":5408},"last_tool_name":"Read","uuid":"a6848bf9-204e-4f45-872a-a31ba5f1f9cc","session_id":"000d0064-bfbf-480d-8b46-d9416edccb28"}
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/logs/phase2_median_attempt0.log-22-[Omitted long context line]
projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/logs/phase2_median_attempt0.log:23:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/logs/phase2_worst_attempt0.log-1-[Omitted long context line]
projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/logs/phase2_worst_attempt0.log-2-{"type":"rate_limit_event","rate_limit_info":{"status":"allowed","resetsAt":1778765400,"rateLimitType":"five_hour","overageStatus":"rejected","overageDisabledReason":"org_level_disabled","isUsingOverage":false},"uuid":"ae2559ec-c6c9-42a8-bbca-e81986f6011f","session_id":"ef58c104-d4c1-4939-8ffb-d61eeb087e8e"}
projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/logs/phase2_worst_attempt0.log:3:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/logs/phase2_median_attempt0.log-1-[Omitted long context line]
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f95d8e47-534d-4430-94e3-2d8feb39e38a",
  "isSidechain": false,
  "promptId": "945f12ce-e0ad-4226-9ca0-653dc3da0cc8",
  "type": "user",
  "uuid": "16b702cb-214f-4aa3-8d56-344d84f77946",
  "toolUseResult": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/logs/phase2_median_attempt0.log-20-[Omitted long context line]\nprojects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/logs/phase2_median_attempt0.log-21-{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"a84a33cd28f662899\",\"tool_use_id\":\"toolu_01T1B7xak22sQREZCq6w1kk9\",\"description\":\"Reading projects/min_necessary_circuit_css/experiment_plan.yaml\",\"usage\":{\"total_tokens\":25323,\"tool_uses\":5,\"duration_ms\":5408},\"last_tool_name\":\"Read\",\"uuid\":\"a6848bf9-204e-4f45-872a-a31ba5f1f9cc\",\"session_id\":\"000d0064-bfbf-480d-8b46-d9416edccb28\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/logs/phase2_median_attempt0.log-22-[Omitted long context line]\nprojects/solver-trace-ablation/artifacts/dream_reports/dream_20260513T215750/logs/phase2_median_attempt0.log:23:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/logs/phase2_worst_attempt0.log-1-[Omitted long context line]\nprojects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/logs/phase2_worst_attempt0.log-2-{\"type\":\"rate_limit_event\",\"rate_limit_info\":{\"status\":\"allowed\",\"resetsAt\":1778765400,\"rateLimitType\":\"five_hour\",\"overageStatus\":\"rejected\",\"overageDisabledReason\":\"org_level_disabled\",\"isUsingOverage\":false},\"uuid\":\"ae2559ec-c6c9-42a8-bbca-e81986f6011f\",\"session_id\":\"ef58c104-d4c1-4939-8ffb-d61eeb087e8e\"}\nprojects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/logs/phase2_worst_attempt0.log:3:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/logs/phase2_median_attempt0.log-1-[Omitted long context line]\nprojects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/logs/phase2_median_attempt0.log-2-{\"type\":\"rate_limit_event\",\"rate_limit_info\":{\"status\":\"allowed\",\"resetsAt\":1778765400,\"rateLimitType\":\"five_hour\",\"overageStatus\":\"rejected\",\"overageDisabledReason\":\"org_level_disabled\",\"isUsingOverage\":false},\"uuid\":\"7e70fb84-7497-400c-939e-fd9ef3e43f2f\",\"session_id\":\"7f0e565e-ca1c-4dc0-98bc-81794254a884\"}\nprojects/solver-trace-ablation/artifacts/dream_reports/dream_20260514T092544/logs/phase2_median_attempt0.log:3:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260521T214001/logs/phase2_median_attempt0.log-1-[Omitted long context line]\nprojects/solver-trace-ablation/artifacts/dream_reports/dream_20260521T214001/logs/phase2_median_attempt0.log-2-{\"type\":\"rate_limit_event\",\"rate_limit_info\":{\"status\":\"allowed\",\"resetsAt\":1779417000,\"rateLimitType\":\"five_hour\",\"overageStatus\":\"rejected\",\"overageDisabledReason\":\"org_level_disabled\",\"isUsingOverage\":false},\"uuid\":\"cf31ffbe-ce3f-4af9-b808-e5c722332ad6\",\"session_id\":\"480b4572-d972-4cac-a4ad-1f7e0e6dbacf\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260521T214001/logs/phase2_median_attempt0.log-3-[Omitted long context line]\nprojects/solver-trace-ablation/artifacts/dream_reports/dream_20260521T214001/logs/phase2_median_attempt0.log:4:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/dream_reports/dream_20260521T214001/logs/phase2_best_attempt0.log-1-[Omitted long context line]\nprojects/solver-trace-ablation/artifacts/dream_reports/dream_20260521T214001/logs/phase2_best_attempt0.log-2-{\"type\":\"rate_limit_event\",\"rate_limit_info\":{\"status\":\"allowed\",\"resetsAt\":1779417600,\"rateLimitType\":\"five_hour\",\"overageStatus\":\"rejected\",\"overageDisabledReason\":\"org_level_disabled\",\"isUsingOverage\":false},\"uuid\":\"bb9684e9-21b1-4c7c-b4c8-666277036067\",\"session_id\":\"2c837443-ad94-44e5-ae9c-6557bd0b41f3\"}\nprojects/solver-trace-ablation/artifacts/dream_reports/dream_20260521T214001/logs/phase2_best_attempt0.log:3:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/archive/feishu_group_oc_8f0788a2307711c1b7fbf59b4cbe0473_reviewer_20260514T110019_586596.jsonl-276-[Omitted long context line]\nprojects/solver-trace-ablation/logs/chats/archive/feishu_group_oc_8f0788a2307711c1b7fbf59b4cbe0473_reviewer_20260514T110019_586596.jsonl-277-{\"ts\": \"2026-05-14T06:32:44.278723+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_8f0788a2307711c1b7fbf59b4cbe0473:reviewer\", \"text\": \"called mcp__agent-ml-research__read_registry\", \"tool\": \"mcp__agent-ml-research__read_registry\", \"tool_args\": {\"project\": \"solver-trace-ablation\", \"filters\": \"{'status': 'DONE'}\", \"fields\": \"['status', 'conclusion']\", \"limit\": \"0\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/archive/feishu_group_oc_8f0788a2307711c1b7fbf59b4cbe0473_reviewer_20260514T110019_586596.jsonl-278-[Omitted long context line]\nprojects/solver-trace-ablation/logs/chats/archive/feishu_group_oc_8f0788a2307711c1b7fbf59b4cbe0473_reviewer_20260514T110019_586596.jsonl:279:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/archive/feishu_group_oc_a771c2a33d631dd40256ecd5c3a6648e_director_20260515T113012_493092.jsonl-339-[Omitted long context line]\nprojects/solver-trace-ablation/logs/chats/archive/feishu_group_oc_a771c2a33d631dd40256ecd5c3a6648e_director_20260515T113012_493092.jsonl-340-{\"ts\": \"2026-05-14T06:32:21.347029+00:00\", \"role\": \"assistant\", \"session\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\", \"text\": \"No response requested.\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/archive/feishu_group_oc_a771c2a33d631dd40256ecd5c3a6648e_director_20260515T113012_493092.jsonl-341-[Omitted long context line]\nprojects/solver-trace-ablation/logs/chats/archive/feishu_group_oc_a771c2a33d631dd40256ecd5c3a6648e_director_20260515T113012_493092.jsonl:342:[Omitted long matching line]\n--\nprojects/min_necessary_circuit_css/experiment_plan.yaml-110-    claim: \"Discussion\"\nprojects/min_necessary_circuit_css/experiment_plan.yaml-111-    description: \"Across all completed experiments, plot max Jaccard vs CSS advantage. 0/6 PASS → Jaccard only predicts 'always fail'\"\nprojects/min_necessary_circuit_css/experiment_plan.yaml-112-    priority: P2\nprojects/min_necessary_circuit_css/experiment_plan.yaml:113:    status: planned\n--\nprojects/min_necessary_circuit_css/experiment_plan.yaml-119-    claim: \"Claim 3\"\nprojects/min_necessary_circuit_css/experiment_plan.yaml-120-    description: \"Document IFR and ACDC failure modes on Qwen as case study for component-level scoring issue. Also contributes to Discussion (method divergence)\"\nprojects/min_necessary_circuit_css/experiment_plan.yaml-121-    priority: P2\nprojects/min_necessary_circuit_css/experiment_plan.yaml:122:    status: planned\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/meta.yaml-1588-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/meta.yaml-1589-      '\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/meta.yaml-1590-    expected_results:\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/meta.yaml:1591:      status: planned\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/worst/imagined_experiments.yaml-279-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/worst/imagined_experiments.yaml-280-    '\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/worst/imagined_experiments.yaml-281-  expected_results:\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/worst/imagined_experiments.yaml:282:    status: planned\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/worst/review_context.yaml-278-\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/worst/review_context.yaml-279-    '\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/worst/review_context.yaml-280-  expected_results:\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/worst/review_context.yaml:281:    status: planned\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/review_worst.log-6-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/review_worst.log-7-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/review_worst.log-8-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/review_worst.log:9:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_worst_attempt0.log-78-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_worst_attempt0.log-79-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_worst_attempt0.log-80-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_worst_attempt0.log:81:[Omitted long matching line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_worst_attempt0.log:82:[Omitted long matching line]\n--\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt1.log-21-{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_011QrG9t2PF6zW5GxNWGmW9q\",\"type\":\"tool_result\",\"content\":\"&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>\"}]},\"parent_tool_use_id\":\"toolu_01D2te1Ves6MGHZcBvmqidyC\",\"session_id\":\"bccbb8d4-c4a8-4fe6-b365-6266209116bb\",\"uuid\":\"5d79ed26-2402-4bea-86ec-2246174b54e0\",\"timestamp\":\"2026-05-13T08:37:28.068Z\"}\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt1.log-22-{\"type\":\"system\",\"subtype\":\"task_notification\",\"task_id\":\"a0d31696502be5216\",\"tool_use_id\":\"toolu_01D2te1Ves6MGHZcBvmqidyC\",\"status\":\"completed\",\"output_file\":\"\",\"summary\":\"Find experiment plan file\",\"usage\":{\"total_tokens\":21179,\"tool_uses\":5,\"duration_ms\":7334},\"uuid\":\"323282a5-1a1f-46a4-a744-3298d134ccd4\",\"session_id\":\"bccbb8d4-c4a8-4fe6-b365-6266209116bb\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt1.log-23-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt1.log:24:[Omitted long matching line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt1.log:25:[Omitted long matching line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt1.log:26:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt1.log-79-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt1.log-80-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt1.log-81-{\"type\":\"system\",\"subtype\":\"task_notification\",\"task_id\":\"a5d016808c871a355\",\"tool_use_id\":\"toolu_01L1L67Y36AmcjoCwBVrb1c8\",\"status\":\"completed\",\"output_file\":\"\",\"summary\":\"Find planned experiments data\",\"usage\":{\"total_tokens\":83309,\"tool_uses\":18,\"duration_ms\":39523},\"uuid\":\"0943dd95-38d2-469a-894b-996087057f46\",\"session_id\":\"bccbb8d4-c4a8-4fe6-b365-6266209116bb\"}\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt1.log:82:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt0.log-21-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt0.log-22-{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"ae43efe12dea425d5\",\"tool_use_id\":\"toolu_0138GWP7831rTTZtKoGYoxo4\",\"description\":\"Reading projects/structfuse-context/experiment_plan.yaml\",\"usage\":{\"total_tokens\":18029,\"tool_uses\":6,\"duration_ms\":6560},\"last_tool_name\":\"Read\",\"uuid\":\"0011f22f-b3de-4582-bd12-a1b4cf63906a\",\"session_id\":\"9fa4408e-fc3a-466c-8bb9-049ddeee63fb\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt0.log-23-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_median_attempt0.log:24:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_best_attempt0.log-22-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_best_attempt0.log-23-{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"a4b773c9ba1ee8974\",\"tool_use_id\":\"toolu_01QnxtV2uCL7M38VbFpGzxcC\",\"description\":\"Reading projects/structfuse-context/experiment_plan.yaml\",\"usage\":{\"total_tokens\":17281,\"tool_uses\":6,\"duration_ms\":5183},\"last_tool_name\":\"Read\",\"uuid\":\"f1cfaa46-3402-44fd-8ad9-002a1c015b57\",\"session_id\":\"02b38ee2-d774-4320-8d95-e25748e01635\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_best_attempt0.log-24-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_best_attempt0.log:25:[Omitted long matching line]\n--\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_best_attempt0.log-41-{\"type\":\"system\",\"subtype\":\"task_notification\",\"task_id\":\"a4b773c9ba1ee8974\",\"tool_use_id\":\"toolu_01QnxtV2uCL7M38VbFpGzxcC\",\"status\":\"completed\",\"output_file\":\"\",\"summary\":\"Find experiment plan files\",\"usage\":{\"total_tokens\":51103,\"tool_uses\":11,\"duration_ms\":20984},\"uuid\":\"eec7cc94-0ad8-4b1f-b6ef-70af009f63c0\",\"session_id\":\"02b38ee2-d774-4320-8d95-e25748e01635\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_best_attempt0.log-42-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_best_attempt0.log-43-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T081242/logs/phase2_best_attempt0.log:44:[Omitted long matching line]\n--\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_worst_attempt0.log-12-{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_012xRANBWvzpFDhw7WRCkZrK\",\"type\":\"tool_result\",\"content\":\"projects/structfuse-context/experiment_plan.yaml\"}]},\"parent_tool_use_id\":\"toolu_01FnbArwnuY4oAF3LmV6kqDD\",\"session_id\":\"793f4d06-c5be-48a3-b889-ed9bd3449408\",\"uuid\":\"f46e8947-8aff-47fe-94e0-daa580fa989a\",\"timestamp\":\"2026-05-13T05:42:55.428Z\"}\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_worst_attempt0.log-13-{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"a30e982a815a05f5e\",\"tool_use_id\":\"toolu_01FnbArwnuY4oAF3LmV6kqDD\",\"description\":\"Reading projects/structfuse-context/experiment_plan.yaml\",\"usage\":{\"total_tokens\":15395,\"tool_uses\":3,\"duration_ms\":2977},\"last_tool_name\":\"Read\",\"uuid\":\"2dd3b6c5-15c3-4356-aec6-f2e18b14e993\",\"session_id\":\"793f4d06-c5be-48a3-b889-ed9bd3449408\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_worst_attempt0.log-14-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_worst_attempt0.log:15:[Omitted long matching line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_worst_attempt0.log-16-{\"type\":\"system\",\"subtype\":\"task_notification\",\"task_id\":\"a30e982a815a05f5e\",\"tool_use_id\":\"toolu_01FnbArwnuY4oAF3LmV6kqDD\",\"status\":\"completed\",\"output_file\":\"\",\"summary\":\"Find experiment plan file\",\"usage\":{\"total_tokens\":22314,\"tool_uses\":3,\"duration_ms\":9495},\"uuid\":\"a9d1e19b-7c1a-4aed-9ceb-2af8ea08428a\",\"session_id\":\"793f4d06-c5be-48a3-b889-ed9bd3449408\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_worst_attempt0.log-17-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_worst_attempt0.log-18-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_worst_attempt0.log:19:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_median_attempt1.log-4-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_median_attempt1.log-5-{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_01UPUBxtMrP4nTNivaXxjSAJ\",\"type\":\"tool_result\",\"content\":\"projects/structfuse-context/experiment_plan.yaml\"}]},\"parent_tool_use_id\":null,\"session_id\":\"74632b66-cba3-4e7a-8604-f8247829979f\",\"uuid\":\"3668b37f-bac5-41b0-abe5-bbc63d404f44\",\"timestamp\":\"2026-05-13T05:27:27.058Z\",\"tool_use_result\":{\"filenames\":[\"projects/structfuse-context/experiment_plan.yaml\"],\"durationMs\":11,\"numFiles\":1,\"truncated\":false}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_median_attempt1.log-6-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_median_attempt1.log:7:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_median_attempt0.log-4-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_median_attempt0.log-5-{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_01Po8Rq6tJAjpdyjmm9mTKYE\",\"type\":\"tool_result\",\"content\":\"projects/structfuse-context/experiment_plan.yaml\"}]},\"parent_tool_use_id\":null,\"session_id\":\"e3f8c6b6-3fd2-4b14-982a-19f03b67fdd1\",\"uuid\":\"4244e9c2-2c63-4814-8cb8-6588ae401ecc\",\"timestamp\":\"2026-05-13T05:05:59.797Z\",\"tool_use_result\":{\"filenames\":[\"projects/structfuse-context/experiment_plan.yaml\"],\"durationMs\":12,\"numFiles\":1,\"truncated\":false}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_median_attempt0.log-6-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_median_attempt0.log:7:[Omitted long matching line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_median_attempt0.log:8:[Omitted long matching line]\n--\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_best_attempt0.log-7-{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_019NM6Tx6dVxAy4A7ShgGv5b\",\"type\":\"tool_result\",\"content\":\"projects/structfuse-context/experiment_plan.yaml\"}]},\"parent_tool_use_id\":null,\"session_id\":\"02da085e-d774-449e-bf4f-c0f423769a3e\",\"uuid\":\"75be0a3d-ed93-47dc-bfc9-778ee8335a1b\",\"timestamp\":\"2026-05-13T04:49:24.962Z\",\"tool_use_result\":{\"filenames\":[\"projects/structfuse-context/experiment_plan.yaml\"],\"durationMs\":31,\"numFiles\":1,\"truncated\":false}}\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_best_attempt0.log-8-{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_01AeoJEWKg4jh6sav5wRn6Ya\",\"type\":\"tool_result\",\"content\":\"projects/structfuse-context/experiment_plan.yaml\"}]},\"parent_tool_use_id\":null,\"session_id\":\"02da085e-d774-449e-bf4f-c0f423769a3e\",\"uuid\":\"09991fbd-c4c9-4fd8-8c8d-a66a683c0bdf\",\"timestamp\":\"2026-05-13T04:49:24.970Z\",\"tool_use_result\":{\"filenames\":[\"projects/structfuse-context/experiment_plan.yaml\"],\"durationMs\":11,\"numFiles\":1,\"truncated\":false}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_best_attempt0.log-9-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T044816/logs/phase2_best_attempt0.log:10:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_worst_attempt0.log-18-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_worst_attempt0.log-19-{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"aaa4333a8a20e7fca\",\"tool_use_id\":\"toolu_01UK2GjXZ4SMf2A5v3LVUnhj\",\"description\":\"Reading projects/structfuse-context/experiment_plan.yaml\",\"usage\":{\"total_tokens\":19765,\"tool_uses\":5,\"duration_ms\":6159},\"last_tool_name\":\"Read\",\"uuid\":\"b06429ff-5443-4021-b43f-ad2bc2475d8a\",\"session_id\":\"dc09ebfc-ff12-4d57-a5a3-2294962bcf00\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_worst_attempt0.log-20-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_worst_attempt0.log:21:[Omitted long matching line]\n--\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_worst_attempt0.log-31-{\"type\":\"system\",\"subtype\":\"task_notification\",\"task_id\":\"aaa4333a8a20e7fca\",\"tool_use_id\":\"toolu_01UK2GjXZ4SMf2A5v3LVUnhj\",\"status\":\"completed\",\"output_file\":\"\",\"summary\":\"Find experiment plan files\",\"usage\":{\"total_tokens\":28369,\"tool_uses\":8,\"duration_ms\":16481},\"uuid\":\"c59b0d59-fcfd-4593-bcf4-f54fb51e38ae\",\"session_id\":\"dc09ebfc-ff12-4d57-a5a3-2294962bcf00\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_worst_attempt0.log-32-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_worst_attempt0.log-33-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_worst_attempt0.log:34:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_median_attempt0.log-6-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_median_attempt0.log-7-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_median_attempt0.log-8-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_median_attempt0.log:9:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_best_attempt0.log-7-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_best_attempt0.log-8-{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_01M5PWa7UaCHsttYivGyE7TQ\",\"type\":\"tool_result\",\"content\":\"projects/structfuse-context/experiment_plan.yaml\"}]},\"parent_tool_use_id\":null,\"session_id\":\"3a6a5868-398a-4a8d-bc28-affe1ab66427\",\"uuid\":\"e68f7a7f-b0ba-4dc8-bbb0-ef30b38b4fdb\",\"timestamp\":\"2026-05-13T05:48:16.342Z\",\"tool_use_result\":{\"filenames\":[\"projects/structfuse-context/experiment_plan.yaml\"],\"durationMs\":9,\"numFiles\":1,\"truncated\":false}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_best_attempt0.log-9-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T054654/logs/phase2_best_attempt0.log:10:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/review_best.log-91-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/review_best.log-92-{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"a10e5aef12332efbc\",\"tool_use_id\":\"toolu_01EyvyTJLeHCS14HM3aHx2sg\",\"description\":\"Reading experiment_plan.yaml\",\"usage\":{\"total_tokens\":51313,\"tool_uses\":16,\"duration_ms\":35552},\"last_tool_name\":\"Read\",\"uuid\":\"07dc4c8e-80d8-4279-98ab-80e742ac40b9\",\"session_id\":\"d5948ce3-0bd6-4774-9a29-31d903f57111\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/review_best.log-93-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/review_best.log:94:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_worst_attempt0.log-4-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_worst_attempt0.log-5-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_worst_attempt0.log-6-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_worst_attempt0.log:7:[Omitted long matching line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_worst_attempt0.log:8:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_median_attempt0.log-21-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_median_attempt0.log-22-{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"af63f730191870686\",\"tool_use_id\":\"toolu_011zNXybmPyJ5qQiQSasjfbJ\",\"description\":\"Reading projects/structfuse-context/experiment_plan.yaml\",\"usage\":{\"total_tokens\":18228,\"tool_uses\":6,\"duration_ms\":6084},\"last_tool_name\":\"Read\",\"uuid\":\"fc3d7249-86c5-4e9a-9cac-bea6af9065b9\",\"session_id\":\"86290856-70b2-4901-851e-3b06929c0ba4\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_median_attempt0.log-23-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_median_attempt0.log:24:[Omitted long matching line]\n--\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_median_attempt0.log-27-{\"type\":\"user\",\"message\":{\"role\":\"user\",\"content\":[{\"tool_use_id\":\"toolu_01QjJJ9cmCFJoszoRE4CrSYD\",\"type\":\"tool_result\",\"content\":\"&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1). The file has 1 lines.&lt;/system-reminder>\"}]},\"parent_tool_use_id\":\"toolu_011zNXybmPyJ5qQiQSasjfbJ\",\"session_id\":\"86290856-70b2-4901-851e-3b06929c0ba4\",\"uuid\":\"15157019-c6b6-42e7-b750-e6b139cf00c9\",\"timestamp\":\"2026-05-13T09:34:29.823Z\"}\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_median_attempt0.log-28-{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"af63f730191870686\",\"tool_use_id\":\"toolu_011zNXybmPyJ5qQiQSasjfbJ\",\"description\":\"Reading projects/structfuse-context/experiment_plan.yaml\",\"usage\":{\"total_tokens\":25541,\"tool_uses\":8,\"duration_ms\":8333},\"last_tool_name\":\"Read\",\"uuid\":\"7fc731a9-b9a1-4237-a408-2fcc44329137\",\"session_id\":\"86290856-70b2-4901-851e-3b06929c0ba4\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_median_attempt0.log-29-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_median_attempt0.log:30:[Omitted long matching line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_median_attempt0.log-31-{\"type\":\"system\",\"subtype\":\"task_notification\",\"task_id\":\"af63f730191870686\",\"tool_use_id\":\"toolu_011zNXybmPyJ5qQiQSasjfbJ\",\"status\":\"completed\",\"output_file\":\"\",\"summary\":\"Find experiment plan file\",\"usage\":{\"total_tokens\":27735,\"tool_uses\":8,\"duration_ms\":13364},\"uuid\":\"f0957af7-3529-4647-bee7-ef686752e787\",\"session_id\":\"86290856-70b2-4901-851e-3b06929c0ba4\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_median_attempt0.log-32-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_median_attempt0.log-33-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_median_attempt0.log:34:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-1-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-2-{\"type\":\"rate_limit_event\",\"rate_limit_info\":{\"status\":\"allowed\",\"resetsAt\":1778673000,\"rateLimitType\":\"five_hour\",\"overageStatus\":\"rejected\",\"overageDisabledReason\":\"org_level_disabled\",\"isUsingOverage\":false},\"uuid\":\"6d9ac89f-cef3-48c7-942b-7dc8f43a0145\",\"session_id\":\"34ed447c-bdea-491d-9484-fa0c1a53bf03\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-3-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log:4:[Omitted long matching line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log:5:[Omitted long matching line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log:6:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-21-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-22-{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"ae2cfb4e926a97c40\",\"tool_use_id\":\"toolu_01N9r45UXMZf5a5zcjCPgnAa\",\"description\":\"Reading projects/structfuse-context/experiment_plan.yaml\",\"usage\":{\"total_tokens\":16426,\"tool_uses\":6,\"duration_ms\":4537},\"last_tool_name\":\"Read\",\"uuid\":\"b6236071-c500-4b59-8df2-2a3f21b71dde\",\"session_id\":\"34ed447c-bdea-491d-9484-fa0c1a53bf03\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-23-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log:24:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-30-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-31-{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"ae2cfb4e926a97c40\",\"tool_use_id\":\"toolu_01N9r45UXMZf5a5zcjCPgnAa\",\"description\":\"Searching for status:\\\\s*planned\",\"usage\":{\"total_tokens\":23709,\"tool_uses\":9,\"duration_ms\":7574},\"last_tool_name\":\"Grep\",\"uuid\":\"0e353be6-3aa7-4f22-a098-bd712e6e5c15\",\"session_id\":\"34ed447c-bdea-491d-9484-fa0c1a53bf03\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-32-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log:33:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-35-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-36-{\"type\":\"system\",\"subtype\":\"task_progress\",\"task_id\":\"ae2cfb4e926a97c40\",\"tool_use_id\":\"toolu_01N9r45UXMZf5a5zcjCPgnAa\",\"description\":\"Reading projects/structfuse-context/artifacts/dream_reports/dream_20260513T081242/worst/imagined_experiments.yaml\",\"usage\":{\"total_tokens\":24935,\"tool_uses\":11,\"duration_ms\":9375},\"last_tool_name\":\"Read\",\"uuid\":\"699a1717-f7d8-4144-965a-fbc275ccdbf3\",\"session_id\":\"34ed447c-bdea-491d-9484-fa0c1a53bf03\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-37-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log:38:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-39-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-40-{\"type\":\"system\",\"subtype\":\"task_notification\",\"task_id\":\"ae2cfb4e926a97c40\",\"tool_use_id\":\"toolu_01N9r45UXMZf5a5zcjCPgnAa\",\"status\":\"completed\",\"output_file\":\"\",\"summary\":\"Find experiment plan files\",\"usage\":{\"total_tokens\":55855,\"tool_uses\":11,\"duration_ms\":18941},\"uuid\":\"c95287d1-694b-465a-8944-6235f552a28a\",\"session_id\":\"34ed447c-bdea-491d-9484-fa0c1a53bf03\"}\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log:41:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log-42-[Omitted long context line]\nprojects/min_necessary_circuit_css/artifacts/dream_reports/dream_20260513T092135/logs/phase2_best_attempt0.log:43:[Omitted long matching line]\n--\nprojects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl-551-{\"ts\": \"2026-05-13T04:46:43.183785+00:00\", \"role\": \"user\", \"session\": \"feishu:group:oc_fde8ba5e95b6c6af458dd6d4bf74a233:director\", \"text\": \"[飞书用户 曹晓玉 (ou_7914e495e04ad4c6dde64881e8662e0d)]: Dream，根据审稿结果决定\", \"source\": \"feishu:oc_fde8ba5e95b6c6af458dd6d4bf74a233\"}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl-552-[Omitted long context line]\nprojects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl-553-{\"ts\": \"2026-05-13T04:47:34.528573+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_fde8ba5e95b6c6af458dd6d4bf74a233:director\", \"text\": \"File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/paper_framing.md\", \"tool\": \"Write\", \"elapsed_ms\": 556}\nprojects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl:554:[Omitted long matching line]\n--\nprojects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl-783-{\"ts\": \"2026-05-13T09:19:44.806117+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_fde8ba5e95b6c6af458dd6d4bf74a233:director\", \"text\": \"1\\texperiments: []\\n2\\t\", \"tool\": \"Read\", \"elapsed_ms\": 0}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl-784-[Omitted long context line]\nprojects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl-785-{\"ts\": \"2026-05-13T09:20:38.886966+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_fde8ba5e95b6c6af458dd6d4bf74a233:director\", \"text\": \"The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/paper_framing.md has been updated successfully.\", \"tool\": \"Write\", \"elapsed_ms\": 650}\nprojects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl:786:[Omitted long matching line]\n--\nprojects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl-836-{\"ts\": \"2026-05-13T10:04:29.348942+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_fde8ba5e95b6c6af458dd6d4bf74a233:director\", \"text\": \"The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/paper_framing.md has been updated successfully.\", \"tool\": \"Edit\", \"elapsed_ms\": 50}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl-837-[Omitted long context line]\nprojects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl-838-{\"ts\": \"2026-05-13T10:04:36.882279+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_fde8ba5e95b6c6af458dd6d4bf74a233:director\", \"text\": \"The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/experiment_plan.yaml has been updated successfully.\", \"tool\": \"Edit\", \"elapsed_ms\": 0}\nprojects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl:839:[Omitted long matching line]\n--\nprojects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl-987-{\"ts\": \"2026-05-13T15:25:14.435506+00:00\", \"role\": \"tool_result\", \"session\": \"feishu:group:oc_fde8ba5e95b6c6af458dd6d4bf74a233:director\", \"text\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/experiment_plan.yaml\", \"tool\": \"Glob\", \"elapsed_ms\": 100}\nprojects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl-988-{\"ts\": \"2026-05-13T15:25:17.100499+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_fde8ba5e95b6c6af458dd6d4bf74a233:director\", \"text\": \"called Read\", \"tool\": \"Read\", \"tool_args\": {\"file_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/experiment_plan.yaml\"}}\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl-989-[Omitted long context line]\nprojects/min_necessary_circuit_css/logs/chats/feishu_group_oc_fde8ba5e95b6c6af458dd6d4bf74a233_director.jsonl:990:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log-16-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log-17-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log-18-[Omitted long context line]\nprojects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log:19:[Omitted long matching line]\n--\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log-23-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log-24-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log-25-[Omitted long context line]\nprojects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log:26:[Omitted long matching line]\nprojects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log:27:[Omitted long matching line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log-28-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log-29-[Omitted long context line]\n/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log-30-[Omitted long context line]\nprojects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log:31:[Omitted long matching line]\nprojects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log:32:[Omitted long matching line]\nprojects/min_necessary_circuit_css/logs/workers/worker_code_update-phase2-configs_20260513T080035.log:33:[Omitted long matching line]",
    "numLines": 228
  },
  "sourceToolAssistantUUID": "f95d8e47-534d-4430-94e3-2d8feb39e38a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：8B退化确认但模式同质（均为H7）或程度较弱，cross-scale成立但taxonomy分化贡献有限 核心假设：['8B exec-only成功训练但dominant mode与4B相同（均为H7），或hacking rate 50-80%弱于4B', 's45/s46 1000步至少1个确认ISR崩塌…",
  "leafUuid": "16b702cb-214f-4aa3-8d56-344d84f77946",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier cross-scale degeneration and Goodhart transience",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf"
}
```

---

### Tool call

_source line 13 · 2026-05-21T21:55:53.260Z_

<details open><summary>🔧 Tool call — Read · `toolu_012WBy6Mc39A4GFZTXZajLym`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/experiment_plan.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16b702cb-214f-4aa3-8d56-344d84f77946",
  "isSidechain": false,
  "requestId": "req_011CbGTe8ZXR6nJHHTYUChKW",
  "type": "assistant",
  "uuid": "1748faf6-d953-4b07-adc1-335db122d9d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AqRVNxH8sweishkjdx9kBX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1018,
      "cache_read_input_tokens": 59147,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1018,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 59147,
          "cache_creation_input_tokens": 1018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1018
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

### Tool result

_source line 14 · 2026-05-21T21:55:53.280Z_

<details><summary>↩ Tool result · `toolu_012WBy6Mc39A4GFZTXZajLym`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim: 1
4	  description: FOL single-logic GRPO, execution-only reward (500 steps, K=8, 3 seeds)
5	    — baseline for STA comparison
6	  priority: P0
7	  gpu_budget_hours: 3
8	  deps: []
9	  registry_id: plan001-exec-only-s42-r2
10	- id: plan_002
11	  claim: 2
12	  description: 'FOL single-logic GRPO, additive ISR bonus: r = r_exec · (1 + β·ISR),
13	    β∈{0.1, 0.3, 0.5}. 先跑 β=0.3 单 seed 验证方向，成功再 3-seed。旧凸组合公式 (α·r_exec + β·r_exec·ISR,
14	    α+β=1) 已废弃——ISR<1 时永远是 penalty (plan005 confirmed)。 新公式确保 ISR 只能 bonus 不能 penalty。'
15	  priority: P0
16	  gpu_budget_hours: 4
17	  deps: []
18	  registry_id: plan002-additive-b01-s42
19	- id: plan_003
20	  claim: 1
21	  description: 'FOL held-out evaluation: compare plan_001 vs plan_002 checkpoints
22	    on test set using identical full STA metrics (prove_rate, ISR, ISR/PR ratio, hacking
23	    taxonomy annotation)'
24	  priority: P0
25	  gpu_budget_hours: 1
26	  deps:
27	  - plan_001
28	  - plan_002
29	  registry_id: plan003-eval-exec-only-r5
30	- id: plan_004
31	  claim: 1
32	  description: 'STA O(1) vs O(N) ablation: rerun exec+STA with fast_isr_fol to confirm
33	    O(1) ineffectiveness at scale (500 steps, 1 seed) — negative result documentation'
34	  priority: P0
35	  gpu_budget_hours: 1
36	  deps: []
37	  registry_id: plan004-o1-ablation-s42
38	- id: plan_005
39	  claim: 1
40	  description: 'STA reward weight ablation: test α/β ratios (0.3/0.7, 0.5/0.5, 0.7/0.3)
41	    + sigmoid curriculum vs fixed — isolate optimal STA integration'
42	  priority: P0
43	  gpu_budget_hours: 4
44	  deps: []
45	  registry_id: plan005-sta-low-s42
46	- id: plan_006
47	  claim: 3
48	  description: 'Prolog single-logic GRPO: exec-only vs exec+STA (500 steps, K=8, 3
49	    seeds) — second logic type validation. Dream M3: must have 3 seeds for cross-logic
50	    claim.'
51	  priority: P1
52	  gpu_budget_hours: 6
53	  deps: []
54	  registry_id: plan006-prolog-sta-s42
55	  notes: Requires Prolog STA instantiation (rule ablation). SWI-Prolog already installed.
56	    Upgraded from 1→3 seeds per Dream feedback.
57	- id: plan_007
58	  claim: 3
59	  description: 'Multi-logic GRPO (FOL+Prolog): exec-only vs exec+STA (500 steps, K=8,
60	    1 seed) — cross-logic transfer test'
61	  priority: P1
62	  gpu_budget_hours: 3
63	  deps:
64	  - plan_006
65	  status: out-of-scope
66	  notes: deferred — not in current paper scope
67	- id: plan_008
68	  claim: 3
69	  description: 'Cross-logic transfer evaluation: FOL-trained model on Prolog tasks
70	    and vice versa'
71	  priority: P1
72	  gpu_budget_hours: 1
73	  deps:
74	  - plan_001
75	  - plan_006
76	  status: out-of-scope
77	  notes: deferred — not in current paper scope
78	- id: plan_009
79	  claim: 1
80	  description: 'SFT baseline: supervised finetuning on same data (FOLIO 500), compare
81	    with GRPO variants'
82	  priority: P1
83	  gpu_budget_hours: 1
84	  deps: []
85	  registry_id: plan009-sft-baseline-s42-1000
86	- id: plan_010
87	  claim: 3
88	  description: 'SMT-LIB single-logic GRPO: exec-only vs exec+STA — third logic type'
89	  priority: P2
90	  gpu_budget_hours: 3
91	  deps: []
92	  notes: deferred — not in current paper scope
93	  status: out-of-scope
94	- id: plan_011
95	  claim: 1
96	  description: 'Qwen3-8B scaling: full MLSR on 8B model (1 seed) — model scale effect'
97	  priority: P2
98	  gpu_budget_hours: 6
99	  deps:
100	  - plan_005
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1748faf6-d953-4b07-adc1-335db122d9d4",
  "isSidechain": false,
  "promptId": "945f12ce-e0ad-4226-9ca0-653dc3da0cc8",
  "type": "user",
  "uuid": "49f0b420-6d5c-46c7-9608-775c0f49f0bf",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/experiment_plan.yaml",
      "content": "experiments:\n- id: plan_001\n  claim: 1\n  description: FOL single-logic GRPO, execution-only reward (500 steps, K=8, 3 seeds)\n    — baseline for STA comparison\n  priority: P0\n  gpu_budget_hours: 3\n  deps: []\n  registry_id: plan001-exec-only-s42-r2\n- id: plan_002\n  claim: 2\n  description: 'FOL single-logic GRPO, additive ISR bonus: r = r_exec · (1 + β·ISR),\n    β∈{0.1, 0.3, 0.5}. 先跑 β=0.3 单 seed 验证方向，成功再 3-seed。旧凸组合公式 (α·r_exec + β·r_exec·ISR,\n    α+β=1) 已废弃——ISR<1 时永远是 penalty (plan005 confirmed)。 新公式确保 ISR 只能 bonus 不能 penalty。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: plan002-additive-b01-s42\n- id: plan_003\n  claim: 1\n  description: 'FOL held-out evaluation: compare plan_001 vs plan_002 checkpoints\n    on test set using identical full STA metrics (prove_rate, ISR, ISR/PR ratio, hacking\n    taxonomy annotation)'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_002\n  registry_id: plan003-eval-exec-only-r5\n- id: plan_004\n  claim: 1\n  description: 'STA O(1) vs O(N) ablation: rerun exec+STA with fast_isr_fol to confirm\n    O(1) ineffectiveness at scale (500 steps, 1 seed) — negative result documentation'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: plan004-o1-ablation-s42\n- id: plan_005\n  claim: 1\n  description: 'STA reward weight ablation: test α/β ratios (0.3/0.7, 0.5/0.5, 0.7/0.3)\n    + sigmoid curriculum vs fixed — isolate optimal STA integration'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: plan005-sta-low-s42\n- id: plan_006\n  claim: 3\n  description: 'Prolog single-logic GRPO: exec-only vs exec+STA (500 steps, K=8, 3\n    seeds) — second logic type validation. Dream M3: must have 3 seeds for cross-logic\n    claim.'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: plan006-prolog-sta-s42\n  notes: Requires Prolog STA instantiation (rule ablation). SWI-Prolog already installed.\n    Upgraded from 1→3 seeds per Dream feedback.\n- id: plan_007\n  claim: 3\n  description: 'Multi-logic GRPO (FOL+Prolog): exec-only vs exec+STA (500 steps, K=8,\n    1 seed) — cross-logic transfer test'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - plan_006\n  status: out-of-scope\n  notes: deferred — not in current paper scope\n- id: plan_008\n  claim: 3\n  description: 'Cross-logic transfer evaluation: FOL-trained model on Prolog tasks\n    and vice versa'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - plan_001\n  - plan_006\n  status: out-of-scope\n  notes: deferred — not in current paper scope\n- id: plan_009\n  claim: 1\n  description: 'SFT baseline: supervised finetuning on same data (FOLIO 500), compare\n    with GRPO variants'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: plan009-sft-baseline-s42-1000\n- id: plan_010\n  claim: 3\n  description: 'SMT-LIB single-logic GRPO: exec-only vs exec+STA — third logic type'\n  priority: P2\n  gpu_budget_hours: 3\n  deps: []\n  notes: deferred — not in current paper scope\n  status: out-of-scope\n- id: plan_011\n  claim: 1\n  description: 'Qwen3-8B scaling: full MLSR on 8B model (1 seed) — model scale effect'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - plan_005",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 244
    }
  },
  "sourceToolAssistantUUID": "1748faf6-d953-4b07-adc1-335db122d9d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15 · 2026-05-21T21:55:53.339Z_

````json
{
  "parentUuid": "49f0b420-6d5c-46c7-9608-775c0f49f0bf",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**solver-trace-ablation**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"solver-trace-ablation\")` 或 `load_project_config(\"solver-trace-ablation\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/solver-trace-ablation/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "4c775728-35a5-4db8-93b7-cea1f249a909",
  "timestamp": "2026-05-21T21:55:53.339Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Assistant

_source line 16 · 2026-05-21T22:10:36.084Z_

<details><summary>Logged reasoning block</summary>

```text
Let me understand the task. I need to generate detailed predicted data for all planned experiments in the median tier. Let me identify all planned experiments:

1. plan_007 - Multi-logic GRPO (out-of-scope)
2. plan_008 - Cross-logic transfer eval (out-of-scope)
3. plan_010 - SMT-LIB (out-of-scope)
4. plan_011 - Qwen3-8B scaling (out-of-scope)
5. plan_019 - Incorporate s45/s46 exec-only 500-step data


6. plan_020 - Extend s45/s46 to 1000 steps
7. plan_021 - Qwen3-8B exec-only 3 seeds
8. plan_022 - Additional ISR β=0.1 seeds (s47-s49) for 4B
9. plan_023 - Qwen3-8B ISR β=0.1 3 seeds
10. plan_024 - Premise-count-matched ISR analysis

The in-scope planned experiments I need to focus on are plan_019 through plan_024, since the first four are deferred.

Now I'm thinking through what the median tier predictions should look like for each of these. The 8B model likely shows degradation but with homogeneous patterns across seeds, both settling into the H7 mode like the 4B baseline. Cross-scale effects should hold up but with limited contribution from taxonomy divergence. For the extended runs at 1000 steps, I'd expect at least one seed to show clear ISR collapse and another with partial collapse. The N=10 analysis should yield an odds ratio around 1.3-1.6 with borderline significance in the CMH test. Looking at the s45 and s46 experimental data more carefully—s45 shows a 99% precision rate with only 1% genuine cases, while s46 has 93% precision but a higher 9.7% genuine rate. I need to reconcile these registry entries since there seem to be some inconsistencies in how the metrics are recorded across the different runs.

The five-seed exec-only pattern is becoming clearer: s42 and s45 maintain strong precision above 93%, s43 completely collapses, s44 shows perfect H7 dominance with zero genuine cases, and s46 leans toward H1 conclusion embedding. For plan_019, this five-seed consistency would strengthen the argument that structural degeneration is pervasive across the median tier, all hitting that ≥90% threshold.

Now extending s45 and s46 out to 1000 steps to test ISR collapse predictions. At the median tier, I'd expect at least one seed to show complete ISR collapse while another shows partial degradation, with the ISR* range falling between 0.01 and 0.15. Looking at s45's trajectory—it's already at ISR*=0.5062 by 500 steps because H7 tautologies naturally cluster around ISR≈0.5—and s46's proved-only ISR hovering near 0.089, I'm trying to extrapolate what happens when we push further. Looking at the 1000-step results, the ISR trajectory diverges sharply based which hacking mode takes over: H1-dominated models like s42 and s44 drive ISR toward zero since conclusion-embedding proofs have minimal ISR, while H7-dominated s43 maintains ISR around 0.465 because tautologies preserve that signal. Since s45 was already H7-heavy at 500 steps, I'd expect it to follow the H7 pattern at 1000 steps.

But the median tier prediction suggests something different—one seed shows full collapse while another only partial collapse, which means the outcomes are more fragmented than my initial model predicted. The key signal for ISR collapse is comparing the 1000-step runs against the 500-step baseline—if the longer training shows significantly degraded ISR, that confirms the degeneration pattern. For the median tier, s46 should show near-total collapse at 1000 steps while s45 likely maintains partial ISR through the H7 artifact even as genuine performance drops to zero. Now I'm laying out predictions for the Qwen 3-8B exec-only experiment across three seeds, expecting prove and hacking rates in the 0.5-0.85 range with much lower genuine rates around 0.05-0.3, and the mode behavior should align with the 4B pattern. ALSO H7, same as 4B)

Context: 8B already had a failed pilot (d154-8b-exec-s42-k4v2) with K=4 showing training stagnation. Need K=8.

For 4B exec-only results:
- s42: PR=93%, H1=87.1%, genuine=7.5%
- s43: PR=13% (collapse)
- s44: PR=98%, H7=100%, genuine=0%
- s45: PR=99%, H7=93.9%, genuine=1%
- s46: PR=93%, H1=89.2%, genuine=9.7%

1.7B exec-only: PR=3%, H7a=100%, genuine=0%

In median tier, 8B shows degeneration but either same mode (H7) or weaker degree. Looking at the three seeds (s42/s43/s44), the metrics show 8B clustering around PR≈0.55-0.85 with H7 dominant at 70-80%, though 4B itself doesn't have a consistent dominant mode across seeds—some lean H1, others H7. The median scenario suggests 8B converges on H7 as the primary failure mode, matching what we see in 4B's H7-dominant seeds rather than developing a distinct scale-dependent taxonomy. This points to homogeneity across model sizes rather than differentiation. confirming that H7 dominance transfers to 8B with slightly weaker hacking rates around 70-80% compared to 4B's stronger performance.

Now looking at the ISR β=0.1 seeds, I notice I already have data for s47 through s51 from the d134 dataset, so these aren't actually additional seeds—they're already accounted for in my analysis. Looking at the performance metrics for the additional seeds, I can see s47, s48, and s49 would extend the characterization to N=8, capturing more of the stochastic bifurcation pattern where some seeds maintain genuine windows while others collapse to H7 dominance.

But I'm noticing the d134 registry already contains results for s47 through s51—five seeds total—while plan_022 only specified three seeds. I need to check whether these are duplicate experiments or if the plan status in the documentation needs updating.

Given the current five-seed results show a genuine odds ratio of 3.48 with extremely strong significance, I'm predicting that adding more seeds under the median-tier hypothesis would dilute this effect substantially. To reach the expected 1.3-1.6 range with eight total seeds, the new predictions would need to show much weaker genuine advantages than what we're currently seeing.

I'm sketching out three new seed predictions where most would be dominated by gaming effects rather than genuine windows, which would shift the genuine-window ratio from 40% (2 out of 5 original seeds) down to around 25% (2 out of 8 total). This aligns reasonably well with the specified 30% target, though the exact ratio depends on how many of the new seeds actually demonstrate genuine windows.

Now I'm working through the total seed count across both ISR plans—the 4B seeds from plan_022 bring us to 8 total, and plan_023 would add another 2-3 8B seeds, but I need to clarify whether the "N=10" target refers to just the 4B pool or the combined count across both model sizes.

For the genuine odds ratio calculation, I'm comparing the genuine window rates between ISR and random control conditions across the same seeds at β=0.1, pulling the actual counts from the existing runs to establish the baseline effect size. Looking at the new seed data for the median tier, I'm noticing that the ISR seeds s47-s49 show lower genuine rates than the earlier batch, while the random seeds have comparable performance. The key issue is that plan_022 only introduces new ISR seeds without corresponding random seeds, so I need to figure out whether to use the existing random seeds s42-s46 for the odds ratio calculation or if I need matched random seeds for a fair comparison. I'm moving on to write out the YAML predictions now. For plan_023, I'm predicting that the 8B ISR experiment will show the same H7 dominance pattern as the 4B version since both models use H7, so this mainly serves as confirmation rather than revealing new insights about the taxonomy—the Goodhart collapse should transfer across scales.

For plan_024, I'm analyzing ISR while controlling for premise count in the execution-only outputs to see if the ISR signal remains meaningful after accounting for proof complexity. The premise-matched analysis should show a smaller genuine-versus-hacking gap than the raw comparison, but it'll still be detectable, contributing methodologically without shifting the core findings.

Let me double-check the experiment plan statuses to make sure I'm tracking which ones are actually planned versus deferred. Looking at the status of each planned experiment, I can see that plan_020 needs fresh training runs for both s45 and s46 up to 1000 steps, plan_021 requires a retry with K=8 after the previous 8B GRPO attempts failed, plan_022 actually has d134 data already registered despite the status showing as planned, plan_023 is waiting on plan_021's results, and plan_024 is purely an analysis task with no training needed. For the prediction exercise, I'll treat all of these as median-tier predictions regardless of their current data availability.

Now I'm examining the actual performance metrics from the d134 registry entries—comparing the ISR variants across s47 through s51 against their matched random baselines to see how much genuine improvement we're getting beyond just precision-recall tradeoffs.

The plan_022 description mentions extending from N=5 to N=8, which means adding 3 more ISR seeds, but the d134 experiments actually tested 5 ISR and 5 random seeds total. Since I'm generating predictions for the median tier with imagined data rather than using the actual registry values, I need to make sure my numbers reflect that tier's characteristics, not these real results.

Now I'm drafting the full YAML structure, making sure the plan_019 expected results properly account for incorporating s45.

For plan_019, all five seeds should show at least 90% degeneration to strengthen the core claim, with a mixed mode distribution across the seeds that produces a 5.6% mean genuine rate when weighted by proved samples, and the cross-seed variance demonstrates stochastic bifurcation. For plan_020, I'm extending s45 to 1000 steps where the H7 dominance that appeared at 500 steps continues to increase.

Now I need to reconsider what ISR* actually represents in the paper context—it's the mean ISR calculated only from proved samples, where H7 tautologies have ISR around 0.5 and H1 conclusion-embedding has ISR around 0.1. So at 1000 steps, s45 with H7 dominance would show a high ISR* value around 0.45-0.55 since the proved samples are mostly H7 tautologies, even though genuine ISR collapses.

But the median range for s45_s46_1000step_isr_star is [0.01, 0.15], which is quite low and suggests both seeds show collapse. This doesn't align with s45 staying H7-dominant and maintaining high ISR*. I'm wondering if s45 actually transitions to H1 dominance at 1000 steps, or if the metric here refers to genuine-only ISR instead of proved-only ISR.

Re-reading the definition more carefully: one seed should fully collapse to ISR*≈0.01-0.03, and the other should partially collapse to ISR*≈0.05-0.15. For s46 with H1 dominance, that's a full collapse to ISR*≈0.01. For s45 with H7 dominance, I'd expect partial collapse to ISR*≈0.08. But the puzzle is how s45 drops from ISR*≈0.5 down to that range.

The issue is that s43 shows pure H7 at 1000 steps maintains ISR*≈0.465, which contradicts the median prediction. Unless s45 actually switches modes at 1000 steps—transitioning from H7 dominance to H1 or another simpler mode—which would explain the dramatic ISR* drop. Mode switching has happened before in this dataset, so it's plausible.

Alternatively, the metric might combine both seeds, meaning s45 could have ISR*=0.12 while s46 collapses to 0.01, averaging around 0.065. For s45 to reach ISR*=0.12, its prove_rate would need to drop significantly from 0.99 due to training instability at longer horizons, shifting the mode composition away from pure H7.

Looking at this differently, maybe s45 undergoes a similar mode switch as s44 did between 500 and 1000 steps—transitioning from H7-dominant to H1-dominant. If s45 follows that pattern with H1 becoming the primary mode at 1000 steps, that would explain the lower ISR* value.

Let me settle on a concrete scenario: s46 shows full collapse with PR=0.98 and nearly all probability mass in H1 and H8, while s45 maintains partial collapse with PR=0.97 but keeps H7 at 55% alongside H1 at 35%, giving it a higher ISR* that reflects the mixed-mode behavior.

Actually, I'm working backwards from the target ISR* value—setting it to 0.10 for s45 and then constructing the taxonomy percentages to match. With H7 at 15%, H1 at 75%, H8 at 8%, and genuine at 2%, the weighted calculation gives me approximately 0.092, which rounds to the 0.10 I'm aiming for.

Now I'm ready to draft the YAML configuration. For the median tier of plan_021, I'm setting PR and hacking_rate ranges between 0.5 and 0.85, with genuine between 0.05 and 0.3. I need to specify three seed configurations: s42 with PR=0.72 and H7-dominant at 68%, s43 with PR=0.58 and H7 at 75%, and s45 with the ISR* calibration I just worked out. I'm refining these predictions to better fit the observed ranges—bringing the hacking rate down to 72% and genuine rate up to 23%. Now I'm thinking through the underlying dynamics: with 8B's greater capacity compared to 4B, there's a tension between learning more sophisticated hacking strategies versus genuine reasoning, but in the median tier this seems to result in less degeneration overall, with genuine rates staying higher than 4B's 1-10% range.

I'm also accounting for higher variance across seeds with 8B—some runs might hit 25% genuine while others drop near zero—and setting specific parameter values for three different seeds to capture this variation.

Now looking at the 4B model with additional ISR seeds: the current batch shows only 2 out of 5 seeds achieving genuine proof windows, with the rest dominated by gaming strategies. Adding three more seeds at this configuration will likely push the genuine rate even lower, diluting the overall odds ratio to somewhere between 1.3 and 1.6, with most new runs falling into the hacking-dominant pattern.

But I'm realizing there's a methodological issue here—the plan adds ISR seeds without corresponding random seeds for those same runs, which breaks the stratification needed for a proper CMH test. Either the plan assumes matched random seeds get added too, or the test needs to be computed differently.

For the median tier prediction, I'll work with the headline numbers: OR around 1.5 with a CMH p-value near 0.06.

Moving to plan_023 with 8B ISR at β=0.1, which only runs if plan_021 succeeds. The 8B model shows the same Goodhart collapse pattern as 4B, with an even lower genuine rate because its greater efficiency at exploiting the ISR reward causes faster convergence to H7 tautologies—though the degradation compared to 4B is relatively small.

Now examining plan_024, which controls for proof complexity through premise-count matching. The analysis reveals that much of the ISR advantage comes from differences in proof length, and once matched, the genuine ISR benefit drops substantially from 3.48 OR down to 1.5-2.0. The effect remains directionally positive but considerably weaker, which is a useful methodological finding about the confound.

For the narrative framing, I'm reconsidering how to present the cross-scale results. The claim about degeneration and mode convergence holds, but the C2 double-edged effect needs reframing—the genuine advantage is more modest than initially appeared, so I should emphasize this as a transient uplift that gets overwhelmed by the dominant collapse pattern. This shifts the paper's focus toward C1 diagnostic methodology and the Goodhart mechanism as the core contribution, with the premise-count-matched analysis and meta-Goodhart gaming dynamics providing methodological depth. The ISR-as-reward framing gets compressed while diagnostic case studies get expanded.

Now I'm thinking through the tables and figures for each experiment, and I need to construct plausible per-seed data. For plan_020 at 1000 steps, I'm extrapolating from the 500-step s45 data where PR was 0.99 and H7 dominated at 93.9%.

Generating YAML output... At 1000 steps, s46 shows H1 dominance with nearly complete ISR collapse—dropping from 0.083 to 0.005, a 94% decline. Looking at the broader trajectory across all three samples, s42 demonstrates the most severe degradation with a 99.6% ISR collapse, while s45 shows an intermediate 80% decline.

All three seeds confirm ISR collapse by 1000 steps, though s45's residual H7 activity keeps some ISR artifact alive. Now I'm ready to compile the final YAML output, but I should first think through the analysis implications more carefully, particularly around the N=10 ISR genuine OR calculation and how the planned additions of s47-s49 and the 8B ISR seeds will affect the median tier results.

Now I'm tallying up the genuine rates across both ISR and matched random seeds. The ISR seeds show a 14.5% genuine rate across 593 total proved cases, while the random seeds are tracking similarly so far, though s49's data appears incomplete.

Looking at the median metrics more carefully, I need to focus on the key statistics: the odds ratio ranges from 1.3 to 1.6, the p-value sits between 0.03 and 0.1, and about 30% of the seeds show a genuine window effect. That means out of 10 total seeds, I'd expect around 3 to demonstrate this genuine window, but I'm currently only seeing 2 seeds with it so far.

If I add the new seeds from plan_022 and plan_023, most won't show a genuine window—plan_022's three seeds have minimal genuine activity (none reaching the threshold for a genuine window), while plan_023 might contribute one seed that could qualify. That would bring me to 3 out of 10 seeds with genuine windows, matching the target distribution.

Let me clarify the seed count: I'm working with 5 original seeds plus 3 from plan_022 and 2-3 from plan_023, totaling around 10 seeds. The key insight is that when I expand from the original 5 to this larger set, the new seeds dilute the overall genuine advantage since most of them don't exhibit the genuine behavior I'm looking for.

This reshapes my narrative: the ISR diagnostic finding gets stronger with more data and scales confirming degeneration, but the double-edged sword claim weakens because the genuine odds ratio drops from 3.48 to around 1.5, making it borderline significant. The cross-scale patterns hold but remain homogeneous. I'm pivoting the paper toward the diagnostic finding and the Goodhart mechanism as the main contributions.

Now I'm ready to finalize the YAML with specific seed numbers for each plan. Let me work through plan_019 first—it's a pure analysis step that consolidates the existing s45/s46 data into an updated aggregate table across the 5 original seeds.

Generating the 5-seed metrics table... Looking at the mode diversity across seeds—H1 in s42 and s46, H7 in s44 and s45, with s43 showing collapse—this confirms the stochastic bifurcation pattern I'm seeing. Now moving to plan_020, I'm predicting s45 at 1000 steps will shift from H7 dominance toward H1, with a prove rate around 0.97 and genuine solutions dropping to about 2%, though some H7 residual should keep the ISR slightly above zero.

For s46 at 1000 steps, I'm expecting even stronger H1 dominance at nearly 95% with the ISR essentially collapsing to near zero. Across all three seeds, the trajectory shows a consistent pattern: s42 loses 99.5% of its ISR, s45 loses about 80% with that mode shift, and s46 loses 94%, averaging around 91% total collapse across the group—all three seeds confirm that degeneration intensifies as training progresses.

Now looking at the Qwen3-8B exec-only results, I'm seeing a notably different picture. Across s42, s43, and s44, the H7 mode is dominant at around 62-69%, with genuine responses maintaining a healthier presence at 12-19% compared to the previous runs. The ISR values are holding much higher at 0.33-0.36, suggesting the model isn't experiencing the same catastrophic collapse I saw before.

Moving into the ISR β=0.1 seeds, s47 is showing an extreme spike in H7 dominance at 86.3% with PR at 0.95, while genuine responses have dropped to just 3.2%. The pattern continues with s48 showing even more pronounced H7 behavior at 93.5%.

Across all eight ISR seeds now, only two are genuinely dominant, giving us a 25% genuine window ratio. The pooled genuine rate across the full ISR set comes to roughly 14.7%, which is notably lower than what we're seeing in the 4B baseline.

When I factor in the matched random seeds, the pooled odds ratio climbs to about 2.05—higher than my target range of 1.3 to 1.6. I need to either reduce the genuine counts in the ISR condition or boost them in the random condition to bring this ratio down. Adding the matched random seeds for the remaining trials should help recalibrate these proportions. I'm working through the math to find the right ISR genuine rate—if I set the random rate at 7.7%, I need the ISR rate around 11.1% to hit that target odds ratio of 1.5. But my current ISR data sits at 22.6%, so I need to add more seeds to dilute it down to the target proportion.

Let me check if adding the three new seeds (s47, s48, s49 with 243 total proved cases) would get me there. If I solve for how many of those new cases need to be genuine, I get a negative number, which means even if none of the new seeds produce genuine cases, the existing 79 genuine out of the expanded total of 593 still lands around 13.3%—still too high for the target odds ratio. This tells me that N=8 with just the 4B seeds won't actually achieve the median odds ratio range I'm aiming for, since s45 and s46 are pulling the numbers in a direction that makes it harder to hit that sweet spot.

So the drop to the 1.3-1.6 odds ratio range must be coming from the N=10 pool, which includes the 8B ISR seeds from plan_023. Looking back at the definition, "n10_isr_genuine_or_pooled" is specifically for N=10 with those 8B ISR seeds included. The three new 8B ISR seeds have very low genuine rates—around 4.6%, 2.1%, and 5.6% respectively—which should help bring down the overall genuine proportion when pooled together.

This is getting complicated trying to derive exact counts, so I'll simplify by using the median headline numbers and providing the rationale in the analysis sections rather than working through every calculation. For the YAML output, I can just provide per-seed predictions and state the aggregate statistics directly. Let me check what "N=10" actually refers to—it seems to mean 10 ISR seeds total across the current setup.

For the median tier, I need to verify whether plan_023 actually executes. Since the definition indicates plan_021 is positive, that means plan_023 does get triggered. So I'm looking at plan_019 as pure analysis, plan_020 with the ISR collapse scenario, and then the subsequent experiments that follow from there.

Now I'm examining the actual step-by-step trajectories to refine my prediction for the s45 1000-step case. Looking at how s42 evolved from 500 to 1000 steps—the performance ratio stayed high while ISR dropped dramatically—I need to see if s44 follows a similar pattern. Looking at s45's behavior at 500 steps with H7 dominance, it could either stabilize like s43 with high ISR* around 0.45-0.50, or switch to H1 like s44 and drop to near zero. The median tier's ISR* of 0.05-0.15 suggests a partial transition—maybe s45 ends up with a mix of residual H7 (20-30%) and dominant H1 (60-70%), which would give an ISR* around 0.10-0.12, fitting the partial collapse pattern.

For s46 at 500 with H1 already present, it just deepens into full H1 collapse with ISR* near 0.005. So I'm setting s45 at 1000 steps to show that mixed mode with ISR*=0.10, and s46 at 1000 to show H1 deepening at ISR*=0.005.

Now I'm ready to write out the YAML with all these parameters locked in, and then I need to think through what tables and figures would actually appear in the paper—starting with the 5-seed 500-step taxonomy, the 1000-step ISR trajectory across 3 seeds, the 8B model taxonomy, and the N=8 results.

Let me also verify the existing s45 data from the experiment plan and registry to make sure I'm not contradicting what's already been run.

Looking at s45's 500-step results, I see PR=99%, genuine=1.0%, and TS=93.9%, which corresponds to H7 being the tautological shortcut metric. For s46, the numbers show PR=93%, genuine=9.7%, with H1 at 89.2% representing conclusion embedding, and I need to recalculate the ISR metric properly by accounting for the proved-only samples. So if mean_isr is calculated across all 100 samples with unproved ones contributing zero, then the sum of ISR values is 8.3, which gives me a proved-only ISR of about 0.089 for s46 at 500 steps. Now I need to figure out what reference point to use for the ISR collapse mentioned in the paper—it shows a dramatic drop from 0.6423 at 100 steps down to 0.0027 at 1000 steps.

Looking at where these numbers come from, the 100-step baseline is from one eval run, the 500-step value from another, and the 1000-step from a third. For s42 I can trace the full trajectory across all three checkpoints, but s45 and s46 probably only have data at 500 and 1000 steps, so I'll need to work with that partial trajectory. I should write out the YAML configuration now and make sure to clarify whether ISR* refers to the proved-only metric or the mean across all samples.

For plan_019, the rationale is straightforward—all five seeds show severe structural degeneration (≥90%), and adding these results reinforces the stochastic bifurcation pattern we're seeing: two seeds lean H7-dominant, two lean H1-dominant, and one collapses entirely. For plan_020, s46 appears to follow the same H1-dominant path as s42 and s44, so ISR* should collapse completely by 1000 steps. s45 is more interesting—it starts H7-dominant at 500 steps but shows a partial transition toward H1 by 1000 steps, unlike s44 which switched fully. This partial transition suggests s45 retains some H7 structure, which would keep ISR* at a moderate level rather than collapsing entirely.

For plan_021, the 8B model has enough capacity to actually train successfully with K=8, whereas the 4B model failed at that setting. But degeneration still happens because it's driven by the reward structure and GRPO dynamics, not model size. The 8B model finds the H7 tautology exploit more readily because it's the more sophisticated hack compared to H1's cruder approach. The genuine proof rate is higher in 8B (~15% vs ~4% for 4B) because the larger model sometimes discovers real proofs during the window before collapse, yet the hacking rate stays in the 50-85% range, confirming this isn't a scale-specific artifact.

For plan_022, I'm working through the stochastic bifurcation sampling logic... =5, 2/5 showed genuine windows (s45, s46). These were "lucky" draws.
- With N=8, the base rate of genuine window occurrence converges toward ~25-30% (2/8 or 3/10)
- New seeds s47-s49 are more likely to show gaming-dominant behavior (consistent with 60-70% base rate of gaming)
- The dilution of genuine OR from 3.48 to ~1.5 reflects the true underlying effect: ISR provides a modest, transient genuine uplift, not a robust one

plan_023 rationale:
- 8B ISR β=0.1 shows same Goodhart collapse as 4B because the tautology exploit is scale-independent
- H7 dominates because 8B efficiently exploits ISR≥0.5 for P→P tautologies
- Genuine rate is very low (2-5%) because 8B's faster convergence means shorter genuine windows
- Cross-scale Goodhart confirmation: the degeneration mechanism transfers across scales, not just the outcome

plan_024 rationale:
- Exec-only outputs have fewer premises than ISR proofs since hacking shortcuts use minimal premises
- When I match premise counts between conditions, the ISR advantage shrinks substantially
- The remaining edge is modest (OR≈1.5-2.0 after matching versus 3.48 raw), showing that uncontrolled comparisons overstate ISR's benefit and premise count acts as a confound in LOO-based metrics

Now I'm ready to write the YAML configuration. So the premise-count-matched analysis would reveal whether genuine proofs maintain higher ISR than hacking proofs even within the same proof complexity bins, or if the ISR difference is actually just an artifact of different premise distributions between the two groups. Looking at the baseline ISR distribution when controlling for premise count to establish what the null case looks like, then I'll compile the specific seed-level metrics showing genuine versus proved rates across the different model sizes to finalize the YAML structure. Now I'm looking at the overall genuine rate across all ISR seeds at 12.8%, then comparing it against the random seed baseline of 7.7%. The pooled odds ratio comes out to 1.76, which is still higher than my target of 1.6, so I need to either reduce the ISR genuine count or incorporate additional random seeds. If plan_022 requires matched random seeds for the remaining seeds, I'd need to factor those in as well.

Adding seeds s47 through s49 would push the random genuine rate down slightly to 7.0%, but the odds ratio would actually increase to 1.84 because the ISR rate stays constant. The real problem is that a couple of the random seeds are skewing the results too heavily in one direction. To get an OR of 1.6 or lower, I'd need to either reconsider whether the s45/s46 genuine counts were inflated, switch to a different statistical method like Cochran-Mantel-Haenszel, or find that the 8B ISR seeds actually have lower genuine rates than their random counterparts—which could happen if the faster H7 collapse at β=0.1 suppresses genuine performance. Let me work through the 8B data to see if including it shifts the overall odds ratio downward.

Adding the 8B ISR and random seed predictions to the totals, I'm getting an OR of 1.41, which lands right in the expected range. The crucial insight is that 8B ISR has a much lower genuine rate than 8B random, and this difference is what brings the cross-scale odds ratio down from the higher values I was seeing before.

With these sample sizes and an OR around 1.4, the p-value should fall somewhere between 0.04 and 0.08, fitting nicely into the median scenario I'm targeting. What's compelling here is the narrative arc: ISR shows a genuine advantage at 4B scale, but that effect flips or vanishes at 8B where the model exploits the tautology too readily, suggesting the benefit is tied to model capacity rather than being a fundamental property of the approach.

Now I need to finalize the seed counts for plan_023—I'll go with 3 seeds all producing results, giving me 11 ISR seeds total (8 at 4B, 3 at 8B) and 8 random seeds (5 at 4B, 3 at 8B).

Looking at the genuine_window_ratio threshold of exactly 30%, with N=11 that works out to roughly 27%, which is close enough. The question is whether any of the new 8B ISR seeds will actually show genuine windows—given that 8B ISR appears weaker than 8B random based on my earlier analysis, I'm skeptical that any of them will.

Let me reconsider plan_022 with one seed showing a borderline genuine window around 25-30%, which would give us 3 out of 11 total seeds meeting the threshold. This shifts the odds ratio calculation, so I need to recompute the ISR versus random comparison with the updated genuine window counts. Looking at the distribution across these seeds, I see a clear bimodal pattern where genuine rates cluster around either near-zero or roughly 50%, with s42 at 17.3% representing an intermediate case where the genuine window is partially collapsing. Setting s49 at 25% genuine fits as another middle-ground scenario—a seed where the window is destabilizing but hasn't fully collapsed yet.

Testing whether to place s49 in the genuine window cluster at ~45% genuine or keep it lower at ~5% genuine, I'm finding that the higher placement pushes the overall ISR genuine rate too high at 1.86, so I should keep s49 in the lower range to maintain the observed effect size.

Now I'm reconsidering the structure entirely — if the genuine window ratio is 30%, then with 10 ISR seeds I'd expect exactly 3 to show genuine windows. Looking at my original five seeds plus the new ones from the two plans, I need to figure out whether s49 should be classified as genuine or gaming, and how to distribute the remaining seeds across the plans to hit that 3-out-of-10 target.

Once I settle on s49 as a genuine window at around 47% genuine rate, I can recalculate the 4B ISR metrics: with 8 seeds total, the genuine count jumps to 122 out of 592, giving me a 20.6% genuine rate. For the 8B model with just 2 seeds, the genuine rate drops significantly to 5.1%. I'm also tracking the random baseline at 5 seeds with 32 genuine cases.

Now I'm comparing the full ISR versus random rates across all model sizes. The ISR approach yields 129 genuine out of 729 total (17.7%), while random sampling gives 57 out of 819 (7.0%), which puts the odds ratio at 2.87. That's still higher than I'd like—the issue is that seeds s45, s46, and s49 are skewing the results with too much genuine content, so I need to reconsider which seeds are actually contributing meaningfully to the comparison. The CMH calculation might be the key here—it stratifies by seed, so if some strata show ISR performing worse than random (OR < 1), that could pull down the overall CMH odds ratio even when the pooled OR is much higher. A CMH OR around 1.4 is actually quite plausible with this stratification effect, even if the combined data suggests a stronger relationship.

But the metric name says "pooled," so I need to reconcile that the genuine OR really is 1.3-1.6 across all seeds combined. For that to happen with three genuine window seeds, those windows would need to show more modest advantages than I initially thought—let me check what the actual genuine rates are for the existing seeds and see if there's room to adjust. The genuine window seeds only give me 20%, which falls short of the 30% target. Looking at the random seeds data now, I'm calculating the totals across both ISR and random seed sets to see the overall genuine rates and whether the combination gets me closer to the requirement.

The pooled odds ratio comes out to 1.79, still above the 1.6 threshold. Let me test what happens if I assume seeds 47, 48, and 49 actually show negative effects in ISR conditions—meaning they'd have lower genuine rates than their random counterparts. With those adjusted to near-zero genuine rates, the ISR total drops to 87 out of 732, bringing the rate down to 11.9%.

Now adjusting the random seed rates upward to compensate—increasing genuine counts for seeds 47, 48, 49 and a couple others—pushes the random total to 72 out of 823, or 8.7%. This gives me an odds ratio of 1.41, which finally falls within the acceptable range of 1.3 to 1.6.

The pattern emerging is that ISR seeds have minimal genuine rates while random seeds sit in the 5-14% range, and crucially, the 8B random condition shows higher genuine than 8B ISR because the ISR reward accelerates tautology convergence at scale—models get that direct ISR bonus for H7 tautologies, whereas without ISR they can explore actual proof strategies. But now I'm noticing the genuine window ratio comes out to 20% rather than the 30% specified in the definition, so there's a discrepancy to resolve. Now I'm checking if these proportions actually work—with s49 ISR at 23.5% genuine and s49 random at 17.6% genuine, the aggregate odds ratio lands at 1.50, which fits the target range of 1.3 to 1.6, and the genuine window ratio stays at exactly 0.3. The pattern makes sense too: within s49, ISR shows higher genuine rates than random, which aligns with what I'd expect at the 4B scale, though the overall odds ratio is dampened because the larger 8B seeds pull the aggregate down. Now I'm laying out the control group metrics for comparison—the random seeds show notably higher genuine rates across all three, particularly s47 at 10.1% versus ISR's 0%, which supports the pattern I identified. Moving into plan_023, I'm setting up the 8B model predictions where ISR continues to show that consistent H7 acceleration problem, with genuine rates dropping further. The core findings are that 8B models degenerate similarly to 4B in H7 mode, ISR's genuine advantage diminishes with scale and additional seeds, and the odds ratio drops from 3.48 to around 1.5—borderline significant—which pushes the paper toward focusing on the C1 diagnostic and Goodhart mechanism instead. Now I'm writing out the YAML configuration without overthinking the exact metrics, and I need to verify whether plan_022 requires matched random seeds by checking if those additional ISR seeds for Qwen3-4B extend the existing characterization.

Looking at the plan description, it's adding three new ISR seeds to go from N=5 to N=8 for better precision on the gaming-versus-genuine split, but it doesn't specify random seeds—so plan_022 only produces ISR seeds while the OR computation still uses the existing N=5 random baseline. With N=8 ISR seeds, I'm calculating the genuine rate at around 16.7% compared to 7.7% for the random N=5 baseline, which gives me the updated odds ratio.

Now I'm seeing that the pooled OR of 2.40 is still too high for my median target, and the issue is that s45 and s46 together account for 65 genuine out of 119 proved cases—they're driving the overall rate up too much. I'm realizing that CMH stratification can produce much lower ORs than the pooled estimate when there's heterogeneity across strata, so I'm calculating the per-stratum odds ratios to see how they vary.

Looking at the individual strata, s42 shows an OR of 0.71 where ISR actually performs worse, while s43 and s44 have undefined or near-zero ORs. But s45 and s46 spike dramatically to 12.84 and 55.3 respectively, showing ISR performing much better. The problem is that s47, s48, and s49 don't have matched random comparisons, so I can't properly stratify them in the CMH analysis—this is a real methodological constraint.

For the aggregate prediction, I think the OR of 1.3-1.6 assumes plan_023 8B data is included and that CMH accounts for scale as a stratum, pulling the overall OR down through strata where ISR actually hurts genuine performance and through the scale factor itself.

For the YAML output, I'll stick with the headline aggregate numbers from the median definition rather than doing the full CMH calculation, since the per-experiment predictions will give enough granularity. Now I need to structure this around the four plans: plan_019 is analysis-only compiling existing results, plan_020 adds two 1000-step training runs, plan_021 adds three 8B training runs, plan_022 adds three 4B ISR runs, and plan_023 adds three more 8B runs.

Before finalizing plan_021 predictions, I'm checking the 8B pilot data—the K=4 run stagnated, but with K=8 the model should train properly, though likely slower than the 4B models. The 4B models hit high PR by steps 300-400, so I'd expect the 8B to reach moderate PR around step 500.

For the median tier with K=8 and 500 steps, the 8B model shows degeneration like the 4B but weaker—lower hacking rate and higher genuine rate, probably because the larger capacity lets it discover legitimate proofs alongside the gaming exploits. Looking at the specific runs, I'm seeing PR values ranging from 0.55 to 0.82 with genuine rates between 12-19%, which feels realistic for this configuration.

Comparing to 4B's exec-only genuine rates, the 8B median prediction of around 15% genuine is notably higher than 4B's 3.6% average—that's the weaker degeneration pattern I expected. The hacking rate drops to 85% versus 4B's 96.4%, which tracks with the model having more capacity to maintain genuine reasoning. The dominant mode is still H7 like 4B, so the taxonomy doesn't distinguish between them, but the behavioral difference is clear.

I'm ready to write out the YAML configuration now.

Actually, let me verify the ISR data I'm including—the plan specifies 500-step training for the new seeds, not 1000-step, so I need to be careful about what trajectory data I reference. For the existing 1000-step ISR runs, I have the full progression for s42 but only the 500→1000 segment for s45 and s46 since there's no 100-step baseline. I should also check on plan_011's status since it was marked as planned.

Writing YAML configuration... The strengths here are the diagnostic methodology and the taxonomy, though the cross-scale confirmation is somewhat limited and the Goodhart mechanism, while insightful, isn't particularly surprising. The main weaknesses are that the ISR benefit doesn't quite reach strong significance, the 8B model mostly confirms rather than adds new insights, and the premise-count confound still affects the effect sizes. There's also the lingering concern that this reads as negative results, though that's partially mitigated. This puts it solidly in the 3.0-3.25 range—findings-level work.

Now I'll write out the YAML with all six experiments. For plan_024 specifically, I need to break down the premise-count-matched ISR analysis: I'd bin the exec-only proofs by premise count, then within each bin compare the genuine versus ISR performance to establish a clean baseline distribution without the confound.

The predictions suggest that while matching reduces the ISR gap from 0.26 to 0.14—roughly a 46% reduction—genuine proofs still maintain higher ISR. The effect size drops from Cohen's d of 1.2 to 0.65, moving from large to medium, which indicates premise count is a real confound but ISR retains diagnostic power. The underlying distribution shows genuine proofs average 6.2 premises versus 2.1 for hacking proofs, a substantial difference that explains much of the raw gap.

When I match on premise count, the hacking subset jumps to ISR of 0.18 from 0.12, primarily because multi-premise hacking cases like conjunction collapse have more inherent ISR artifact than simpler hacks. This methodological finding—that leave-one-out metrics are mechanically confounded by proof length—is the key insight. Now I'm planning out the tables and figures needed to present each experiment, starting with the taxonomy results.

Writing YAML config... I'm planning to incorporate the existing s45 and s46 execution data into the analysis to strengthen the C1 evidence, expanding from three seeds to five and showing consistent degeneration patterns across the larger dataset.

The five seeds reveal a clear bifurcation: two exhibit H7-dominant shortcuts, two show H1-dominant patterns, and one represents complete learning failure—all with structural degradation above 90%, confirming this is systematic behavior rather than random variation. The complementary failure modes across s42 through s46 demonstrate that the hacking phenomenon is reproducible and follows distinct pathways.

Now I'm looking at the performance metrics across these five seeds to quantify the genuine reasoning collapse. The mean genuine rate drops to just 3.6% across all seeds, with even the best performer (s46) only reaching 9.7%—showing that exec-only GRPO essentially eliminates authentic reasoning within 500 steps. I'm compiling the detailed breakdown showing how each seed's performance distributes across the different hacking modes and genuine reasoning. Now I'm looking at a stacked bar chart that shows how the taxonomy distribution varies across five exec-only seeds, revealing significant heterogeneity between different modes. The key finding is that with N=5, we're confirming a stochastic bifurcation pattern — the mode appears to be seed-determined, making single-seed results unreliable. Comparing to the SFT baseline is striking: SFT achieves 92.3-93.3% genuine rate across 3 seeds, while GRPO exec-only drops to just 3.6%. I'm also planning to extend the exec-only training for seeds s45 and s46 from 500 to 1000 steps to verify whether the ISR collapse persists.

Now I'm examining the generalization of trajectories across more seeds by building evidence from a 3-seed sample at 1000 steps. The results show a partial mode switch from H7 to H1 between the 500 and 1000 step marks, with s45 reaching 97% prove rate but only 2.1% genuine rate, and s46 showing similarly high prove rates with minimal ISR-only solutions. Looking at the trajectory across different seeds, s46 shows the same H1-dominant pattern emerging by step 500 (89.2%), which intensifies through training to reach 94.9% while genuine responses collapse from 9.7% to 1.0%, and the ISR metric drops 94.4% — matching the severe collapse patterns seen in s42 and s44. Meanwhile s45 presents a different dynamic: it starts H7-dominant at step 500 (93.9%) but undergoes a partial mode switch toward H1 by step 1000, similar to s44's trajectory, though the transition remains incomplete with 18.6% H7 remaining, which leaves behind ISR artifacts that complicate the overall picture.

Generating markdown table... Now I'm seeing that the ISR collapse pattern holds consistently across all three seeds, though the trajectories differ in speed—the direct H1 path crashes quickly to near-zero while the mixed H7→H1 route deteriorates more gradually. The key insight is that high ISR values might be misleading artifacts of H7 tautologies rather than genuine reasoning, so I need taxonomy annotations to properly interpret what's actually happening. I'm also noting a new model configuration for Qwen3-8B with exec-only GRPO training.

Looking at the expected results across seeds at 500 steps, I'm tracking how structural degeneration manifests at this model scale—comparing prove rates, reasoning mode distributions, and genuine reasoning percentages to see if the pattern generalizes beyond the initial observations. Looking at the performance comparison, the 8B model does show degeneration but it's less severe than the 4B—the hacking rate is 85% versus 4B's 96.4%, and it maintains a genuine proof rate of 15.1% compared to 4B's 3.6%. The larger capacity lets it preserve some legitimate proving ability alongside the exploitative shortcuts, though hacking still dominates. The critical constraint is that both models converge to the same dominant mode H7, a tautological shortcut, with a pattern emerging across model sizes where smaller models favor H1 and larger ones gravitate toward H7.

This cross-scale pattern undermines the narrative about capacity-dependent differentiation in hacking modes—the 8B results essentially replicate what we saw in 4B rather than revealing fundamentally new shortcuts. The story shifts from "scale reveals diverse hacking strategies" to "degeneration transfers across scales with convergence to H7." The 8B findings become more of a robustness check for the core diagnostic rather than an independent insight, and reviewers will likely question whether it's just confirming a subset of the 4B results.

Generating comparison table... Looking at the scale progression from 1.7B through 8B, I'm seeing that genuine reasoning does increase with model size, but this doesn't fundamentally change the Goodhart's Law conclusion—it just delays when the collapse happens. The key insight is that the hacking strategy consistently converges to H7 tautologies across all scales, so I should frame this as degeneration being universal rather than claiming scale reveals distinct behavioral basins, since the H7 patterns are too similar between 4B and 8B to support that distinction.

Now I'm expanding the bimodality characterization by running three additional ISR seeds with β=0.1 on Qwen3-4B to increase the sample from N=5 to N=8, examining how the prove rates, H7 dominance, and genuine reasoning vary across these new runs. Looking at the new seeds, s47 and s48 are converging to H7 dominance like the existing high-PR patterns, while s49 sits at the genuine window boundary with a moderate genuine rate of 23.5%—lower than s45 and s46 but still meaningful, suggesting it's near the bifurcation threshold.

For N=8, the bimodality shows 37.5% of seeds in the genuine window, and the 4B-only pooled odds ratio stays elevated around 2.4 because s45, s46, and s49 drive most of the genuine signal, but this will drop to roughly 1.5 once I pool with 8B data since the larger model's lower genuine rates will dilute the effect.

Generating markdown table... Now I'm looking at the complete dataset across all 8 seeds, which confirms the bimodal pattern—about 37% sustain genuine windows while 63% shift to gaming-dominant behavior. The new observation with s49 showing 23.5% genuine rate is particularly interesting because it sits right at the boundary between these two modes, suggesting it might represent a transitional state where the genuine window is actively closing. This supports the idea that genuine windows are inherently transient phenomena.

The pooled odds ratio remains strong around 2.4 for the 4B model because seeds with genuine windows contribute substantially, but when I look at the cross-scale pooled estimate dropping to 1.5, that decline is driven by the 8B strata results rather than the 4B sample size expansion itself—something I'll need to discuss carefully with the effect size implications for reviewers. I'm also setting up the Qwen3-8B ISR validation with β=0.1 across three seeds to test for cross-scale Goodhart effects, which will only run once degeneration is confirmed at the median setting.

Compiling the expected performance metrics across the three seed runs...

Looking at the cross-scale comparison, the 8B ISR model with β=0.1 actually shows lower genuine rates than random sampling at this scale, which suggests ISR is accelerating the Goodhart collapse effect. Across the aggregate of 11 ISR seeds versus 8 random seeds, the pooled odds ratio is 1.50 with a CMH p-value of 0.06, indicating a marginal but not quite significant effect with a small effect size.

The mechanism appears to be that ISR's tautology bias—where P→P patterns get high ISR scores—is being exploited more efficiently at the 8B scale. The H7 rate jumps to 82-88% with ISR compared to 63-69% with exec-only baselines, showing that ISR is accelerating the collapse rather than genuinely improving the model. This contrasts sharply with the 4B results, where ISR at least showed some transient genuine uplift early on, but at 8B the model has enough capacity to simultaneously learn both genuine patterns and the H7 shortcut, and the ISR reward structure directly incentivizes the shortcut.

When I pool across scales, the cross-scale odds ratio drops to around 1.50 with marginal significance (p≈0.06), which means the ISR benefit isn't robust—it's scale-dependent and borderline. The effect size is small (Cohen's h≈0.12), so reviewers will likely argue that even if statistically significant, the practical impact is negligible. I need to be explicit about this in the paper rather than just reporting p-values.

Generating comparison table... I need to reframe the ISR benefit as capacity-dependent rather than universal—the genuine uplift appears at 4B but vanishes at 8B, suggesting it's a transient artifact of capacity constraints rather than a fundamental property. For the paper, I should emphasize this scale-dependent effect and prepare for reviewer pushback on the borderline pooled result by reporting effect sizes and Bayes factors alongside the confidence intervals.

Now I'm planning a premise-count-matched analysis on the executive-only outputs to see whether ISR's diagnostic power holds up when controlling for proof complexity. The unmatched data shows a strong separation between genuine and hacking strategies, but once I match on premise distribution, that ISR delta should shrink considerably, which would further support the capacity bottleneck interpretation. The matching procedure reveals that premise count acts as a confound—more premises create more ablation opportunities, inflating ISR values mechanistically. When I control for premise count, genuine proofs still show higher ISR than hacking proofs (0.32 vs 0.18), but the gap shrinks by 46%, suggesting the raw comparison overstates ISR's discriminative power. The effect size drops from large to medium (Cohen's d: 1.2→0.65) and AUROC declines from 0.82 to 0.74, confirming ISR remains diagnostically useful but less dramatic than the unadjusted numbers implied.

This premise-count-matched analysis is methodologically novel—LOO-based metrics pervade the literature yet rarely account for proof complexity, so quantifying this confound establishes best practices for future work.

Looking at the comparison tables, controlling for premise count substantially reshapes the findings: the genuine ISR drops from 0.38 to 0.32, while hacking ISR actually increases from 0.12 to 0.18, collapsing the gap by nearly half and reducing Cohen's d from 1.20 to 0.65. The AUROC also declines from 0.82 to 0.74, suggesting the original effect size was inflated by the premise count imbalance.

The premise distributions reveal why this matters—genuine arguments average 6.2 premises versus just 1.3 for H7 hacking attempts, creating a systematic confound that the matched analysis corrects for. I'm also visualizing how ISR correlates with premise count across categories to illustrate this relationship.

The key insight is framing this as methodological rigor rather than a limitation: the raw ISR comparison overstates diagnostic power by roughly 46%, but the matched analysis still shows medium discriminative ability, which actually strengthens the claim that ISR captures something meaningful about argument quality beyond just complexity.

Now I'm checking whether s45 actually shows the mode switch I'd expect at 1000 steps. At 500 steps it's mostly single-premise tautologies with ISR around 0.5, but if it shifts toward more complex proofs like s44 does, the ISR would drop significantly. Let me verify this against the actual registry data to see if the pattern holds. Yes! s44 went from H7=100% at 500 steps to H1=85%, H8=15% at 1000 steps. Complete mode switch.

And s43 at 1000 steps:
plan001-exec-only-s43-1000-r2: PR=0.9, H7=100%, ISR*=0.465

s43 stayed H7 at 1000 steps. No mode switch.

So mode switch at 1000 steps is seed-dependent: s44 switched, s43 didn't.

For median prediction of s45 at 1000 steps, a partial mode switch seems like the right middle ground. Now I'm working through the ISR* calculation to see if the target of 0.10 is achievable. If about 18.6% of proved samples remain in H7 mode with ISR around 0.5, while 72.2% transition to H1 with ISR around 0.01, plus smaller portions in other modes, that gives me roughly 0.109—close enough to the target. For s46, I'm looking at a much more extreme shift toward H1 dominance at 94.9% to hit the lower ISR* target of 0.005. I'm getting close to 0.005 with these adjustments, though the exact decomposition is approximate. Let me verify the YAML configuration is solid and then check whether s46's ISR* value of 0.005 actually falls within the expected range of [0.01, 0.15] for the 1000-step prediction—it looks like it's falling short of the minimum threshold. I'm reconsidering whether the [0.01, 0.15] range represents the overall metric span or just the partial collapse case. If it's the full range across both seeds, then s46 at 0.005 falls below the lower bound, so I should adjust it to 0.01 to fit within the specified range while still representing a full collapse scenario.

Now I'm checking the exec-only genuine proof counts across the seeds to validate my prediction of mean_n_premises=6.2 for plan_024, looking at the distribution of genuine proofs found in the execution-only category. and genuine in premise count is substantial. The matching analysis would be most useful for H7 vs genuine comparison.

Let me refine these estimates based on the actual distributions I'm seeing: genuine proofs cluster around 5-6 premises on average, H7 stays minimal at 1-2, H1 overlaps significantly with genuine in the 5-6 range, and H8 falls in between. This means when I match proofs by premise count, genuine and H1 become the primary comparison since they have similar distributions, while H7 remains too sparse to match effectively. After controlling for premise count, the ISR gap between genuine and H1 narrows considerably, suggesting premise count was masking some of the performance difference.

I'm going to simplify and stick with my current estimates rather than getting lost in the matching methodology details. The core finding is that roughly 40-50% of the raw ISR gap traces back to premise count differences. Now I need to finalize the output, making sure the tables contain actual markdown content and the figures descriptions explain what would be visualized. I'm also going to double-check the experimental parameters for plan_021, particularly the K value...

For the 8B model at K=8 with 500 steps, it'll generate more completions per prompt which increases diversity but slows training. My predictions for median tier performance (0.75, 0.55, 0.82) average around 0.71, which fits the expected range. The 8B model might show lower proof recovery than 4B either because it needs more steps to converge or because its larger capacity lets it explore more diverse proof strategies that don't all lead to high-PR hacking. Both explanations make sense for the median tier. Now I'm ready to write out the final YAML.

Actually, let me reconsider the plan. I'm looking at the existing data for exec-only genuine proofs across the different seeds. I need to compile the genuine proof counts and their mean ISR values from the registry and sweep results to establish what the baseline numbers are.

Now I'm estimating the mean ISR for genuine proofs across all seeds. The registry gives me s42's value directly at 0.3141, but for s45 and s46 I'll need to make reasonable estimates based on the proof counts. For the hacking proofs, I'm looking at how ISR varies by proof type—H7 proofs tend to have higher ISR around 0.5 due to tautology artifacts, while H1 proofs are much lower depending on their structure.

When I weight these together, the hacking mean ISR comes out surprisingly close to the genuine mean, which complicates things since I'd normally expect them to be more distinct.

The issue is that H7 tautologies have inherently high ISR by design, so they're gaming the metric even though they're degenerate proofs. This means ISR isn't actually a strong discriminator between genuine and hacking proofs when H7 is involved. But the paper already flagged this vulnerability—ISR was meant to catch H1 conclusion-embedding and H8 low-ISR cases, not H7. So the diagnostic power of ISR really depends on which hacking mode I'm looking at.

For plan_024, I need to reconsider the unmatched AUROC prediction. Since H7 proofs artificially inflate the hacking ISR to around 0.27, the separation from genuine ISR (0.30) is much tighter than I initially thought, which would actually lower the AUROC below my 0.82 estimate.

The real insight is that ISR's diagnostic power comes from trajectory collapse over time rather than point-in-time values, and plan_024 specifically needs to establish the ISR baseline while controlling for premise count to address the reviewer's concern about whether ISR differences are actually driven by proof complexity rather than genuine hacking detection. The main comparison really comes down to ISR-zero proofs like H1 versus ISR-nonzero proofs like H7 and genuine ones. When I control for proof length by matching premise counts, genuine proofs should show higher ISR than H1 within the same bins, which would confirm ISR is actually measuring structural quality rather than just being confounded by how many premises are involved. The real issue is that H7 gets artificially inflated ISR from its tautological structure, not from premise count itself. frame plan_024. The key finding would be:

1. Premise count distribution differs: genuine has moderate premises (4-8), H1 has moderate-high (3-15), H7 has very few (1-2)
2. Within matched premise-count bins:
   - Bin 1-2 premises: only H7 proofs, all have ISR≈0.5, no genuine to compare
   - Bin 3-5 premises: genuine ISR=0.35, H1 ISR=0.03, gap=0.32
   - Bin 6-10 premises: genuine ISR=0.28, H1 ISR=0.04, gap=0.24
   - Bin 11+: only H1 proofs
3. After matching (excluding H7 which has no genuine counterpart at same premise count): ISR is a strong diagnostic for genuine vs H1 (AUROC=0.90+), but fails to distinguish genuine from H7 since they operate in different premise-count regimes. So ISR's diagnostic capacity depends on which hacking mode I'm trying to detect.

The reviewer's real concern is whether ISR's signal comes from actual structural quality or just reflects proof complexity—since more components mechanically allow more ablation opportunities, and genuine proofs tend to be more complex anyway. But the premise-count-matched analysis shows that even within the same complexity bin, genuine proofs maintain higher ISR than H1 hacks, so the signal isn't purely an artifact of complexity differences. in median tier: ISR is a strong diagnostic for distinguishing genuine from H1/H8 hacking (AUROC stays above 0.85 even after controlling for premise count), but it completely fails to detect H7 since H7 was constructed to have ISR around 0.5 by design. The diagnostic value of ISR really hinges on which hacking modes are present—when H7 dominates the distribution, ISR loses its utility as a classifier.

Now I'm reconsidering the genuine counts for plan_019 by looking at the execution-only data across different seeds, checking what proportion of proved cases were actually genuine. There's definitely some overlap or rounding inconsistency here—the percentages add up to over 100%, which suggests either there's an H7 category I'm missing or the percentages are calculated differently than I'm assuming. Let me not get too caught up in the exact arithmetic and focus on the broader pattern instead. I need to finalize the YAML structure now. For plan_022, I'm documenting that the 4B-only analysis shows a pooled OR of 2.4 with strong significance, but I should note that cross-scale generalizability remains uncertain until plan_023 adds the 8B data. Then plan_023 will show how including the 8B results drops that pooled OR down to 1.5, still significant but weaker.

Writing YAML config...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c775728-35a5-4db8-93b7-cea1f249a909",
  "isSidechain": false,
  "requestId": "req_011CbGTeLcZkXKoHTTbKv1Vq",
  "type": "assistant",
  "uuid": "497f03a5-0db6-4f9f-9444-a65681065275",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjpCgbAsefr2VrX1H6oUNw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7112,
      "cache_read_input_tokens": 60165,
      "output_tokens": 42547,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 42547,
          "cache_read_input_tokens": 60165,
          "cache_creation_input_tokens": 7112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7112
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

_source line 17 · 2026-05-21T22:10:36.269Z_

Let me review the existing data patterns to construct internally consistent predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "497f03a5-0db6-4f9f-9444-a65681065275",
  "isSidechain": false,
  "requestId": "req_011CbGTeLcZkXKoHTTbKv1Vq",
  "type": "assistant",
  "uuid": "77c12fd7-427b-4c8d-ac66-b7faf449766a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjpCgbAsefr2VrX1H6oUNw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7112,
      "cache_read_input_tokens": 60165,
      "output_tokens": 42547,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 42547,
          "cache_read_input_tokens": 60165,
          "cache_creation_input_tokens": 7112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7112
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

### Tool call

_source line 18 · 2026-05-21T22:10:42.060Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01N7bXvbUnvMXvTUgKGALbM7`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find exec-only and ISR registry data",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/, search for any files that contain 5-seed aggregate statistics, ISR OR calculations, or cross-scale comparison summaries. Look for files like analysis outputs, summary tables, or statistical test results. Check under artifacts/, outputs/, or any analysis directories. Quick search for files matching patterns like *aggregate*, *summary*, *or_*, *cmh*, *cross_scale*. Also check for any paper draft files that contain the current OR=3.48 calculation details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77c12fd7-427b-4c8d-ac66-b7faf449766a",
  "isSidechain": false,
  "requestId": "req_011CbGTeLcZkXKoHTTbKv1Vq",
  "type": "assistant",
  "uuid": "b4ce8936-716f-432f-b151-db9c4cf7f98a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjpCgbAsefr2VrX1H6oUNw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7112,
      "cache_read_input_tokens": 60165,
      "output_tokens": 42547,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7112,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 42547,
          "cache_read_input_tokens": 60165,
          "cache_creation_input_tokens": 7112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7112
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

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：8B退化确认但模式同质（均为H7）或程度较弱，cross-scale成立但taxonomy分化贡献有限 核心假设：['8B exec-only成功训练但dominant mode与4B相同（均为H7），或hacking rate 50-80%弱于4B', 's45/s46 1000步至少1个确认ISR崩塌…",
  "leafUuid": "b4ce8936-716f-432f-b151-db9c4cf7f98a",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier cross-scale degeneration and Goodhart transience",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf"
}
```

---

### Tool result

_source line 21 · 2026-05-21T22:11:51.820Z_

<details><summary>↩ Tool result · `toolu_01N7bXvbUnvMXvTUgKGALbM7`</summary>

```text
Perfect! Now let me compile my findings into a comprehensive summary.

## Summary of Findings

I've successfully located and analyzed the key files containing 5-seed aggregate statistics, ISR OR calculations, cross-scale comparisons, and paper draft materials for the solver-trace-ablation project. Here's what I found:

### **Core Statistical Files with 5-Seed/Cross-Seed Aggregates:**

1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/bonferroni_correction.json`** — Comprehensive statistical test results including:
   - **OR=3.48** (5-seed uncorrected N-H rate): ISR 22.6% vs Random 7.7%, p<10⁻⁸
   - **OR=0.61** (3-seed H8+FN corrected): ISR 6.06% vs Random 9.5%, p=0.182 (n.s.) — **direction reversal after correction**
   - **CMH tests** with OR_CMH=3.37 (seed-stratified), p=4.5e-10
   - 14 distinct statistical tests with Bonferroni correction
   - Fisher exact, Mann-Whitney U, permutation tests, CMH

2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_aggregate_stats.md`** — 3-seed pooled statistics for exec-only conditions:
   - Exec-only 500-step: PR=0.68±0.47, ISR=0.23±0.30, pooled genuine=5.9% (12/204)
   - Exec-only 1000-step: PR=0.95±0.05, ISR=0.179±0.305, pooled genuine=0% (or 1.0% with H1-near)
   - Wilson 95% CIs included
   - Clear documentation of 3 seed results and issues

3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/d157_3seed_pooled_stats.md`** — Shuffled-ISR 3-seed results:
   - Pooled genuine rate: 86.96% (40/46) with Wilson CI [74.3%, 93.9%]
   - Cross-condition comparison table with means, stds
   - ISR β=0.1 (5 seeds ~15%), Random β=0.1 (5 seeds ~13%), showing genuine rate differences

4. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_comparison_table.md`** — Side-by-side per-seed and pooled comparison:
   - ISR β=0.1 (3-seed): pooled genuine 6.06% (14/231), H7 70.56% (163/231)
   - Random β=0.1 (2-seed): pooled genuine 10.98% (19/173), H7 20.81% (36/173)
   - Interpretation of ISR reward amplifying H7 tautology

### **Statistical CI and Test Result Files:**

5. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_results.json`** — Per-experiment and pooled Wilson confidence intervals:
   - ISR, Random, Exec-only, SFT conditions across multiple seeds and β values
   - H7, H1, Genuine rates with CI bounds
   - Coverage of β=0.1, β=0.3 conditions

6. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_complete.csv`** — Complete CSV format with:
   - All 6+ conditions (ISR β=0.1/0.3, Random β=0.1/0.3, Exec-only, SFT)
   - Per-seed and pooled rows with CI bounds
   - Source attribution (classify_h7.py, registry, etc.)

7. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/sft_3seed_pooled_ci.json`** — SFT 3-seed pooled CI:
   - Genuine rate: 91.3% (proved-only), 14% (total), Fisher p=0.000023 vs Exec-only

8. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/bootstrap_ci_results.json`** — Bootstrap confidence intervals

### **Paper Draft Files with OR=3.48 Calculation Details:**

9. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/submission/appendix.tex`** — Official paper appendix containing:
   - Table with ISR vs Random comparisons (OR=0.61, n.s. in corrected form)
   - H8 audit methodology (reclassified 5 samples as premise-subset gaming)
   - H7 false-negative correction (H7b obfuscated tautology)
   - Cross-scale and seed-stratified CMH test results

10. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/experiments.tex`** — Main paper experiments section with OR calculations

### **Review Reports Documenting OR=3.48 Context:**

11. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_10.md`** — Fresh peer review (Round 10):
    - Acknowledges OR reversal: uncorrected 3.48 vs corrected 0.61
    - Flags N-H=23% (uncorrected from 3 seeds) vs ~6% (corrected across 5 seeds) as critical issue
    - 4× discrepancy not adequately surfaced in main text

12. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_4.md`** — Consensus review identifying critical issues:
    - **Q2**: "为什么主文以 5-seed uncorrected OR=3.48 为 headline 而非 3-seed corrected OR=0.61 (n.s.)？"
    - Documents the statistical presentation bias: selecting 5-seed uncorrected numbers despite 3-seed H8+FN-corrected correction reversing direction
    - Notes deleted checkpoints (s43/s44) prevent complete H8 audit for all 5 seeds

### **Cross-Scale and Statistical Analysis Files:**

13. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci.py`** — Python calculation script for Wilson CI

### **Other Supporting Analysis:**

14. Multiple analysis JSON files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/data/`:
    - `pooled_statistics_2026-05-15.json` — Summary of 5-seed pooled results
    - `wilson_ci_complete.json` — Complete CI results

### **Key Finding: The OR=3.48 Calculation Details**

The critical **OR=3.48** statistic appears in:
- **Source**: 5-seed pooled, uncorrected non-hacking rate: ISR 22.6% (52/231) vs Random 7.7% (20/262)
- **Calculation**: (52×242)/(20×179) ≈ 3.48
- **Caveat**: Based on incomplete data because ISR β=0.1 seeds s43/s44 checkpoints were deleted before H8 audit, making the 5-seed number an "uncorrected upper bound"
- **After correction**: 3-seed H8+FN-corrected shows ISR 6.06% (14/231) vs Random 9.5% (25/262), OR=0.61, p=0.182 (n.s.) — **direction reversal**
- **Statistical issue**: Pooled Fisher tests ignore seed-level clustering; seed-level permutation test gives p=0.26 (n.s.)

All files are located in the `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/` directory hierarchy.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4ce8936-716f-432f-b151-db9c4cf7f98a",
  "isSidechain": false,
  "promptId": "945f12ce-e0ad-4226-9ca0-653dc3da0cc8",
  "type": "user",
  "uuid": "3f54f141-93d1-424b-b492-a7b75b25c948",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/, search for any files that contain 5-seed aggregate statistics, ISR OR calculations, or cross-scale comparison summaries. Look for files like analysis outputs, summary tables, or statistical test results. Check under artifacts/, outputs/, or any analysis directories. Quick search for files matching patterns like *aggregate*, *summary*, *or_*, *cmh*, *cross_scale*. Also check for any paper draft files that contain the current OR=3.48 calculation details.",
    "agentId": "ad4bb61eb6b1c4573",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me compile my findings into a comprehensive summary.\n\n## Summary of Findings\n\nI've successfully located and analyzed the key files containing 5-seed aggregate statistics, ISR OR calculations, cross-scale comparisons, and paper draft materials for the solver-trace-ablation project. Here's what I found:\n\n### **Core Statistical Files with 5-Seed/Cross-Seed Aggregates:**\n\n1. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/bonferroni_correction.json`** — Comprehensive statistical test results including:\n   - **OR=3.48** (5-seed uncorrected N-H rate): ISR 22.6% vs Random 7.7%, p<10⁻⁸\n   - **OR=0.61** (3-seed H8+FN corrected): ISR 6.06% vs Random 9.5%, p=0.182 (n.s.) — **direction reversal after correction**\n   - **CMH tests** with OR_CMH=3.37 (seed-stratified), p=4.5e-10\n   - 14 distinct statistical tests with Bonferroni correction\n   - Fisher exact, Mann-Whitney U, permutation tests, CMH\n\n2. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_aggregate_stats.md`** — 3-seed pooled statistics for exec-only conditions:\n   - Exec-only 500-step: PR=0.68±0.47, ISR=0.23±0.30, pooled genuine=5.9% (12/204)\n   - Exec-only 1000-step: PR=0.95±0.05, ISR=0.179±0.305, pooled genuine=0% (or 1.0% with H1-near)\n   - Wilson 95% CIs included\n   - Clear documentation of 3 seed results and issues\n\n3. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/d157_3seed_pooled_stats.md`** — Shuffled-ISR 3-seed results:\n   - Pooled genuine rate: 86.96% (40/46) with Wilson CI [74.3%, 93.9%]\n   - Cross-condition comparison table with means, stds\n   - ISR β=0.1 (5 seeds ~15%), Random β=0.1 (5 seeds ~13%), showing genuine rate differences\n\n4. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/3seed_comparison_table.md`** — Side-by-side per-seed and pooled comparison:\n   - ISR β=0.1 (3-seed): pooled genuine 6.06% (14/231), H7 70.56% (163/231)\n   - Random β=0.1 (2-seed): pooled genuine 10.98% (19/173), H7 20.81% (36/173)\n   - Interpretation of ISR reward amplifying H7 tautology\n\n### **Statistical CI and Test Result Files:**\n\n5. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_results.json`** — Per-experiment and pooled Wilson confidence intervals:\n   - ISR, Random, Exec-only, SFT conditions across multiple seeds and β values\n   - H7, H1, Genuine rates with CI bounds\n   - Coverage of β=0.1, β=0.3 conditions\n\n6. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci_complete.csv`** — Complete CSV format with:\n   - All 6+ conditions (ISR β=0.1/0.3, Random β=0.1/0.3, Exec-only, SFT)\n   - Per-seed and pooled rows with CI bounds\n   - Source attribution (classify_h7.py, registry, etc.)\n\n7. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/sft_3seed_pooled_ci.json`** — SFT 3-seed pooled CI:\n   - Genuine rate: 91.3% (proved-only), 14% (total), Fisher p=0.000023 vs Exec-only\n\n8. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/bootstrap_ci_results.json`** — Bootstrap confidence intervals\n\n### **Paper Draft Files with OR=3.48 Calculation Details:**\n\n9. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/submission/appendix.tex`** — Official paper appendix containing:\n   - Table with ISR vs Random comparisons (OR=0.61, n.s. in corrected form)\n   - H8 audit methodology (reclassified 5 samples as premise-subset gaming)\n   - H7 false-negative correction (H7b obfuscated tautology)\n   - Cross-scale and seed-stratified CMH test results\n\n10. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/experiments.tex`** — Main paper experiments section with OR calculations\n\n### **Review Reports Documenting OR=3.48 Context:**\n\n11. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_10.md`** — Fresh peer review (Round 10):\n    - Acknowledges OR reversal: uncorrected 3.48 vs corrected 0.61\n    - Flags N-H=23% (uncorrected from 3 seeds) vs ~6% (corrected across 5 seeds) as critical issue\n    - 4× discrepancy not adequately surfaced in main text\n\n12. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_4.md`** — Consensus review identifying critical issues:\n    - **Q2**: \"为什么主文以 5-seed uncorrected OR=3.48 为 headline 而非 3-seed corrected OR=0.61 (n.s.)？\"\n    - Documents the statistical presentation bias: selecting 5-seed uncorrected numbers despite 3-seed H8+FN-corrected correction reversing direction\n    - Notes deleted checkpoints (s43/s44) prevent complete H8 audit for all 5 seeds\n\n### **Cross-Scale and Statistical Analysis Files:**\n\n13. **`/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/wilson_ci.py`** — Python calculation script for Wilson CI\n\n### **Other Supporting Analysis:**\n\n14. Multiple analysis JSON files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/data/`:\n    - `pooled_statistics_2026-05-15.json` — Summary of 5-seed pooled results\n    - `wilson_ci_complete.json` — Complete CI results\n\n### **Key Finding: The OR=3.48 Calculation Details**\n\nThe critical **OR=3.48** statistic appears in:\n- **Source**: 5-seed pooled, uncorrected non-hacking rate: ISR 22.6% (52/231) vs Random 7.7% (20/262)\n- **Calculation**: (52×242)/(20×179) ≈ 3.48\n- **Caveat**: Based on incomplete data because ISR β=0.1 seeds s43/s44 checkpoints were deleted before H8 audit, making the 5-seed number an \"uncorrected upper bound\"\n- **After correction**: 3-seed H8+FN-corrected shows ISR 6.06% (14/231) vs Random 9.5% (25/262), OR=0.61, p=0.182 (n.s.) — **direction reversal**\n- **Statistical issue**: Pooled Fisher tests ignore seed-level clustering; seed-level permutation test gives p=0.26 (n.s.)\n\nAll files are located in the `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/` directory hierarchy."
      }
    ],
    "totalDurationMs": 69754,
    "totalTokens": 77851,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1515,
      "cache_read_input_tokens": 74165,
      "output_tokens": 2166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1515
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 2166,
          "cache_read_input_tokens": 74165,
          "cache_creation_input_tokens": 1515,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1515,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 12,
      "searchCount": 4,
      "bashCount": 10,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "b4ce8936-716f-432f-b151-db9c4cf7f98a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-21T22:15:10.752Z_

<details><summary>Logged reasoning block</summary>

```text
This is very helpful! Now I have crucial additional context:

1. The OR=3.48 is from 5-seed **uncorrected** data. After H8+FN correction (3-seed), OR reverses to 0.61 (n.s.)
2. The critical issue is that checkpoints for s43/s44 ISR were deleted before H8 audit, so the 5-seed OR can't be properly corrected
3. The CMH OR=3.37 is seed-stratified but still based on uncorrected genuine counts

This is important for the median tier predictions because:


The tension between corrected and uncorrected numbers is already baked into the existing data. The median tier's OR prediction of 1.3-1.6 sits right between the uncorrected 3.48 and corrected 0.61, which could mean it's reflecting what happens when H8 correction gets applied consistently across all ten seeds, or when additional seeds like s47 are factored in—both scenarios would pull the genuine counts down and compress the odds ratio further. s49, 8B) having low genuine effect, and the true OR after correction and expansion is borderline significant.

For the median tier with OR=1.3-1.6 and CMH p=0.03-0.10, this makes sense now—after applying H8 correction consistently across all N=10 seeds, the genuine advantage becomes modest rather than inflated. The corrected 3-seed data (OR~0.61) averaging with the 5-seed uncorrected data (OR=3.48) lands us in this middle ground, which is methodologically honest.

The key realization is that the original OR of 3.48 was artificially inflated because H8 correction was missing for two seeds, s45/s46 were contributing disproportionately, and there was no seed-level stratification. With consistent methodology applied across all seeds and proper CMH stratification, the genuine effect settles at OR=1.4 with p=0.06—a much more realistic picture than the uncorrected <10⁻⁸. Now I need to incorporate this understanding into the YAML predictions for the median tier. Looking at the actual data for s45 and s46, they already have H8 corrections factored in—the genuine rates of 54.8% and 54.5% are post-correction figures. The s43 and s44 seeds are different since their checkpoints were deleted before H8 auditing, but for s43 with H7=100% and genuine=0%, the H8 correction wouldn't meaningfully change the classification anyway since all proofs are already accounted for. I'm noticing the 5-seed OR calculation gives 3.48, but when I look at just the 3-seed corrected data, the OR flips to 0.61—which suggests the correction is having a dramatic effect on the direction of the association. The discrepancy seems to hinge on what random seeds are being paired with each ISR group and how the correction redistributes the genuine classifications in s42.

The real issue is that s45 and s46 are driving the entire effect—they show 54-55% genuine rates in ISR but only 5-8% in their matched random seeds, creating this stochastic bifurcation where some seeds exhibit a strong genuine window and others don't. Removing just those two seeds collapses the OR from 3.48 down to 0.61, which is a major red flag for statistical instability. When I expand to the full 10-seed median tier prediction by adding 5 more seeds where only 0-1 show genuine windows, the s45/s46 effect gets diluted and the OR should drop toward 1.3-1.6, which aligns with what I'm seeing in the median estimates.

The key insight here is that the N=5 result wasn't capturing a genuine effect—it was inflated by sampling two lucky seeds that happened to land in the genuine window. The N=10 OR of 1.3-1.6 is actually more accurate because it reflects the true base rate of genuine windows across the seed population, which is around 30%. The genuine benefit is real, but much smaller than the headline N=5 number suggested. This is a crucial methodological point for the paper.

Now I need to calculate what the approximate N=10 OR should be by modeling what happens when I add those additional seeds.

Looking at the expanded seed data across both ISR 4B and 8B models, I'm tallying up the genuine window counts across all nine 4B seeds and two 8B seeds to get a more representative estimate of the true effect size.

Now I'm calculating the random baseline from the existing seeds and realizing I need matched random data for the new seeds too—without it, I can't properly compute the odds ratio for the CMH test.

Looking at the 4B random data for s47-s49, I see s49 collapsed with only 5 samples, so I'll exclude it and pool the usable random seeds: that gives me 42 genuine cases out of 596 total, or 7.0%. For the 8B predictions, I'm seeing random genuine rates around 14.3% for s42 and continuing to estimate the others.

Pooling all random data across both model sizes gives me 60 genuine out of 741 total for an 8.1% genuine rate. Computing the odds ratio between ISR and random conditions, I get 1.95—still higher than my target of 1.6. Let me try adjusting the ISR genuine count for s49 down to 5 out of 85 instead of 18 to see if that brings the odds ratio closer to 1.5.

After recalculating with the reduced ISR genuine count, I'm getting 94 genuine out of 729 total for a 12.9% ISR rate, which gives an odds ratio of 1.68—still above target. I'll also bump up the random genuine rates by adjusting a couple of the random samples to 20% and 16% respectively, bringing the random total to 68 genuine out of 741 for a 9.2% rate. This yields an odds ratio of 1.47, which falls nicely within the 1.3 to 1.6 range I'm aiming for.

The pattern makes sense: 8B random achieves moderate genuine rates (14-20%) without ISR reward, while 8B ISR drops to very low genuine (4-5%) because ISR accelerates the H7 tautology pattern, and the new 4B ISR seeds stay consistently low (0-5%) as they're dominated by gaming. With these numbers, the pooled odds ratio lands at 1.47. For the CMH p-value, given these sample sizes and the stratification across seeds, I'd expect something in the 0.03 to 0.10 range depending on heterogeneity. Looking at the genuine_window_ratio, I have three seeds exceeding the 20% threshold: s42 at 17.3%, s45 at 54.8%, and s46 at 54.5%.

Now I'm reconsidering the threshold—s42 sits right at the boundary between partial gaming and genuine, so whether it counts depends on where I draw the line. If I use >20%, only s45 and s46 qualify, giving 0.20. But if I lower it to >10% or >15%, s42 joins them for 0.30, which aligns better with the median tier classification I'm working with. , strong, 54.8%), s46 (strong, 54.5%) = 3/10 = 0.30 ✓

Now checking the other candidates against this threshold—s47, s48, s49, and the 8B variants all fall below 15% genuine rate, so they don't qualify as windows. That gives me an ISR total of 94 out of 729 samples, which is 12.9%. For the random baseline, I'm adding up the counts across the three categories and need to recalculate the denominator. Now I'm adjusting the 8B random predictions upward slightly to bring the odds ratio closer to the target range of 1.4-1.5, which gives me a final rate of around 8.6% that feels right. Writing YAML output... predictions (20%, 18.7%) — are these realistic?

4B random β=0.1 genuine rates:
s42: 22.8% (18/79) — this is the highest
s43: 1.1%
s44: 6.7%
s45: 8.6%
s46: 2.1%

So 4B random has one high-genuine seed (s42 at 22.8%) and others at 1-9%. The variability is high.

For 8B random, if 8B has more capacity to learn genuine proofs without ISR reward, the genuine rates might be moderate:
8B_s42_rand: 16% (higher than most 4B random seeds, reflecting 8B capacity)
8B_s44_rand: 14% (similar)

This is plausible. 8B random β=0.1 might actually produce more genuine proofs than 4B random because the larger model has more capacity for genuine reasoning, and the random reward doesn't specifically drive toward H7 tautology. The hacking mode differs between scales — 4B random mostly shows H1 conclusion-embedding while 8B random likely does too, but 8B can solve problems more genuinely overall. So 8B random β=0.1 having around 15-20% genuine makes sense. Now I need to compute the 8B ISR versus 8B random within-scale comparison for plan_023: 8B ISR has 7 genuine proofs out of 137 total, giving a 5.1% genuine rate.

Now looking at 8B random: 30 genuine out of 145 total yields a 20.7% genuine rate. The odds ratio shows ISR has substantially lower genuine proofs than random at this scale — ISR is actually harmful at 8B, accelerating the Goodhart collapse rather than helping. This supports the narrative that ISR's genuine benefit depends on scale; at 8B it's counterproductive. For 4B ISR, I'm calculating the genuine rate across all seeds: 87 genuine proofs out of 592 total gives 14.7%.

Now I'm looking at 4B random: 45 genuine out of 678 total is only 6.6% genuine. The odds ratio for 4B comes out to 2.42, showing strong ISR benefit at smaller scale. But the 8B odds ratio is 0.21 — a stark reversal. When I pool across scales, the overall odds ratio is 1.48, which is moderate and borderline significant. The real story here is this scale-dependent divergence: ISR works well at 4B but fails at 8B. Before finalizing the YAML, I need to verify whether the random baseline used matched seeds across the different plans.

Looking back at the plan descriptions, plan_023 specifies "Qwen3-8B ISR β=0.1, 3 seeds" but doesn't explicitly mention random seeds. For the cross-scale odds ratio calculation, I'd need 8B random data as a control, but the plan only includes plan_021 (8B exec-only) and plan_023 (8B ISR). There's no explicit 8B random β=0.1 experiment in the plan. I might need to either derive it from plan_021 as a proxy or add it as a new experiment. — exec-only is actually the baseline condition
2. Or run as an implicit part of plan_023

For the OR calculation, the comparison might be ISR β=0.1 vs exec-only (not random β=0.1). Let me reconsider.

Actually, in the paper, the main comparison for C2 (ISR double-edged) is ISR β=0.1 vs Random β=0.1, not vs exec-only. For 8B, if we don't have random β=0.1, we can't do the cross-scale ISR vs Random comparison.

But in the median tier, the plan might include running 8B random β=0.1 as part of plan_023 (not explicitly mentioned but methodologically necessary). Or the comparison might be ISR vs exec-only.

For simplicity, I'll note in the YAML that cross-scale OR requires 8B random data (either from a supplementary experiment or using exec-only as baseline), and provide the estimated numbers assuming it's available.

OK, I'll write the YAML now with a note about this.

Actually, re-reading plan_023 notes: "Reviewer: stretch goal, only if plan_021 positive and time permits." In the median tier, time might be limited, so plan_023 might only run ISR seeds without matched random. The cross-scale OR would then use exec-only as baseline (not ideal but sufficient for directional claim).

In this case, I'm calculating what the 8B odds ratio would look like if ISR genuinely underperforms exec-only too—using the predicted 5.1% genuine rate for ISR versus 15.1% for exec-only, which gives an OR of 0.30, suggesting ISR's reward signal actually hurts performance at this scale.

Now I'm pooling the 4B and 8B results using Cochran-Mantel-Haenszel stratification, where 4B shows ISR outperforming random (OR=2.42) but 8B shows the opposite pattern. The weighted average leans heavily toward 4B's result since it has roughly three times more samples, so the pooled OR would fall somewhere between 2.42 and 0.30.

I'm calculating the exact CMH estimate by taking a weighted geometric mean of the stratum-specific odds ratios, which gives me an OR around 1.53 with a p-value closer to 0.06 due to the heterogeneity between scales. This confirms the cross-scale effect is real but driven primarily by the 4B advantage, while 8B actually shows the opposite trend.

For the final YAML output, I need to decide whether to use ISR versus random for 4B and ISR versus exec-only for 8B in the cross-scale comparison, acknowledging this methodological inconsistency.

Actually, I'm realizing that mixing different comparators across scales isn't clean—I should use the same comparison at both scales. Let me recalculate using ISR versus exec-only at both 4B and 8B, pulling the genuine counts from the actual data to verify the rates match what I'm seeing.

At 4B, the exec-only genuine rate comes out to 4.3%, while ISR is 14.7%, giving an odds ratio of 3.84. But at 8B, the pattern flips—ISR is only 5.1% genuine while exec jumps to 15.1%, yielding an odds ratio of 0.30. Now I'm computing the Cochran-Mantel-Haenszel test to pool these across scales.

The combined odds ratio comes out to 2.19, which overshoots the target of around 1.5. I'm realizing the issue: I've been comparing ISR against exec-only, but the paper's main comparison should be ISR β=0.1 versus Random β=0.1, both using GRPO with different reward bonuses. That means for the cross-scale analysis to work, I need the 8B random β=0.1 data, which plan_023 must include.

Now I'm working through what the cross-scale odds ratio would look like if I pool the 4B and 8B comparisons using Cochran-Mantel-Haenszel stratification. I'm calculating the 8B random performance from two seeds and comparing it against the 8B ISR results to see if this gives me the target odds ratio range of 1.3-1.6. I'm finishing the calculation for the 4B stratum and moving into the 8B data, then realizing I need to correct my approach to the Mantel-Haenszel formula—it should sum the products of exposed and unexposed across strata divided by the total, not use an exponential.

Now I'm computing the actual OR_MH by combining both strata's contributions, and I'm getting 1.55, which falls perfectly within the expected range. Next I need to calculate the CMH test statistic using the hypergeometric expectation and variance for each stratum. CMH p-value of 0.06 confirms this is a solid median-tier result. The real story here is the stark heterogeneity: at 4B, ISR genuinely helps with an OR of 2.42, but at 8B it actually hurts with an OR of 0.25, and the combined MH estimate of 1.55 gets pulled down by that 8B drag. A Breslow-Day test would almost certainly reject homogeneity (p<0.01) given how dramatically different these effects are across scales, which is exactly what we'd expect to see with genuine cross-scale heterogeneity.

Now I'm assembling the YAML output with the specific numbers: three 8B ISR seeds, two 8B random seeds for methodological rigor, the within-8B comparison showing OR=0.25, and the cross-scale MH estimate at 1.55 with p=0.06. But I'm realizing there's a tension here—the plan_023 description only mentions the three ISR seeds without accounting for the random seeds, and adding two more 8B runs would consume an extra 8 GPU-hours on top of the 12 already allocated. I need to think through whether that's feasible in the median scenario.

Given the resource constraints, I'm going with a pragmatic compromise: attempt all three ISR seeds plus two random seeds, but expect one random seed to fail due to OOM or other issues, leaving me with three successful ISR runs and one random baseline. That gives me the within-8B comparison at 5.1% for ISR versus 20% for the single random seed, which still demonstrates the effect clearly enough. Writing the final YAML configuration...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3f54f141-93d1-424b-b492-a7b75b25c948",
  "isSidechain": false,
  "requestId": "req_011CbGUrzbXepRB8dVKZw33s",
  "type": "assistant",
  "uuid": "81c82aed-45c4-43d4-93ce-20bdb4319ace",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiBA5X8gB9S4hZ5A4KHHga",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 44623,
      "cache_read_input_tokens": 67277,
      "output_tokens": 21124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 44623,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21124,
          "cache_read_input_tokens": 67277,
          "cache_creation_input_tokens": 44623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 44623
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

_source line 23 · 2026-05-21T22:19:15.098Z_

Good, I now have the full context including the critical OR correction issue (uncorrected 3.48 vs corrected 0.61 for 3-seed data) and the statistical presentation tension. Let me construct the median tier predictions.

```yaml
tier: median
narrative_guidance: >
  Cross-scale claim保留但降级为'degeneration transfers across scales, exploitation mode
  converges to H7'——确认universality但taxonomy分化贡献被削弱。C2 double-edged需要明确
  软化：genuine OR从3.48降至~1.5仅边界显著（CMH p≈0.06），且cross-scale heterogeneity
  显著（4B OR=2.4 vs 8B OR=0.25, Breslow-Day p<0.01）——ISR genuine benefit是scale-
  dependent transient，不是universal property。Reframe为'modest transient uplift at 4B,
  accelerated collapse at 8B'。论文重心转向C1 diagnostic methodology + Goodhart
  inevitability mechanism + 9-mode taxonomy。Premise-count-matched analysis和meta-Goodhart
  triple gaming作为methodological contribution补位。ISR-as-reward篇幅压缩至≤1.5页，
  增加diagnostic case study depth。预期reviewer score 3.0-3.25 (Findings级别)。

imagined_experiments:
  - name: "incorporate_s45_s46_500step_data"
    plan_id: "plan_019"
    description: >
      将已有的s45/s46 exec-only 500步数据纳入论文分析。纯写作/分析任务，0 GPU。
      s45 (PR=99%, H7=93.9%, genuine=1.0%) 和 s46 (PR=93%, H1=89.2%, genuine=9.7%)
      扩展C1证据从N=3到N=5。
    expected_results:
      five_seed_mean_prove_rate: 0.792
      five_seed_std_prove_rate: 0.366
      five_seed_mean_genuine_rate: 0.036
      five_seed_degeneration_rate_ge90_pct: "5/5 (100%)"
      mode_distribution_summary: "2 H7-dominant (s44 100%, s45 93.9%), 2 H1-dominant (s42 87.1%, s46 89.2%), 1 collapse (s43 PR=13%)"
      five_seed_H7_mean_pct: 38.8
      five_seed_H1_mean_pct: 56.3
      five_seed_genuine_total: "18/396 proved (4.5%)"
      sft_baseline_comparison_genuine: "92.9% (SFT) vs 4.5% (GRPO exec-only)"
    result_rationale: >
      所有5个seed均展示≥90%结构退化（s43虽PR=13%，其13个proved样本中100% H1），
      确认exec-only GRPO hacking是systematic而非偶发。模式分布展示stochastic
      bifurcation：同一架构+数据+超参，仅seed不同就产生H7 tautology (s44/s45)
      vs H1 conclusion-embedding (s42/s46) vs learning collapse (s43)三种完全不同
      的failure mode。genuine rate从SFT baseline的92.9%降至4.5%——GRPO exec-only
      在500步内几乎消除genuine reasoning。这是C1 diagnostic claim的核心证据：
      ISR能检测到prove_rate无法发现的退化（s44 PR=98%但genuine=0%）。
    tables:
      - name: "Table: 5-Seed Exec-Only 500-Step Taxonomy (C1 Evidence)"
        content: |
          | Seed | PR   | H7%   | H1%   | H8%  | Gen% | ISR*(proved) | Dominant Mode     |
          |------|------|-------|-------|------|------|--------------|-------------------|
          | s42  | 0.93 | 0.0   | 87.1  | 6.5  | 7.5  | 0.132        | H1 (conc. embed.) |
          | s43  | 0.13 | 0.0   | 100.0 | 0.0  | 0.0  | 0.000        | Collapse          |
          | s44  | 0.98 | 100.0 | 0.0   | 0.0  | 0.0  | 0.582        | H7 (tautology)    |
          | s45  | 0.99 | 93.9  | 5.1   | 1.0  | 1.0  | 0.506        | H7 (tautology)    |
          | s46  | 0.93 | 0.0   | 89.2  | 4.3  | 9.7  | 0.089        | H1 (conc. embed.) |
          | Mean | 0.79 | 38.8  | 56.3  | 2.4  | 3.6  | 0.262        | —                 |
    figures_description:
      - "Stacked bar chart: per-seed taxonomy distribution across 5 exec-only seeds，展示mode heterogeneity和stochastic bifurcation"
    analysis: >
      N=5显著强化了C1 diagnostic claim：ISR检测到5/5 seeds的结构退化，而prove_rate
      仅在1/5 seeds (s43) 显示异常。特别是s44 (PR=98%, genuine=0%, H7=100%) 是
      ISR diagnostic value的最佳case study——PR完美但输出100%是tautological shortcut。
      ISR*=0.582看似还行，但这是H7 artifact (单premise tautology机械产生ISR≈0.5)，
      而非genuine reasoning signal。论文应以s44为focal example展开diagnostic case study。

  - name: "s45_s46_1000step_extension"
    plan_id: "plan_020"
    description: >
      将s45和s46 exec-only训练从500步延长到1000步。验证ISR崩塌轨迹在N=3
      seeds上的泛化性(s42已有1000步数据)。每seed ~3h GPU。
    expected_results:
      s45_1000step:
        prove_rate: 0.97
        n_proved: 97
        proved_only_isr: 0.10
        h7_rate: 0.186
        h7_count: 18
        h1_rate: 0.722
        h1_count: 70
        h8_rate: 0.072
        h8_count: 7
        genuine_rate: 0.021
        genuine_count: 2
        isr_collapse_from_500: "-80.2%"
        mode_transition: "H7 93.9% → H7 18.6% + H1 72.2% (partial H7→H1 switch)"
      s46_1000step:
        prove_rate: 0.98
        n_proved: 98
        proved_only_isr: 0.012
        h7_rate: 0.0
        h7_count: 0
        h1_rate: 0.949
        h1_count: 93
        h8_rate: 0.041
        h8_count: 4
        genuine_rate: 0.010
        genuine_count: 1
        isr_collapse_from_500: "-86.5%"
        mode_transition: "H1 89.2% → H1 94.9% (H1 deepens, no mode switch)"
      three_seed_trajectory:
        s42_trajectory: "ISR* 0.642→0.132→0.003 (500→1000步 collapse 97.7%)"
        s45_trajectory: "ISR* 0.506→0.10 (collapse 80.2%, partial — H7 residual)"
        s46_trajectory: "ISR* 0.089→0.012 (collapse 86.5%, full)"
        mean_500_to_1000_collapse_pct: 88.1
        all_seeds_genuine_at_1000_le_2pct: true
    result_rationale: >
      s46在500步已是H1-dominant (89.2%)。延长到1000步强化H1至94.9%，genuine从
      9.7%压缩至1.0%，ISR*从0.089降至0.012——遵循与s42/s44相同的H1路径（H1证明
      的ISR≈0因为conclusion已在premise中，ablation任何premise不影响prove）。
      
      s45在500步是H7-dominant (93.9%)。关键预测：1000步时发生部分模式切换H7→H1，
      类似已观察到的s44 (500步H7=100% → 1000步H1=85%)。但s45切换不完全，保留
      18.6% H7残留。机制：长训练使模型发现更短的H1 exploit (conclusion直接作为
      premise)，部分H7 tautology被更极端的H1取代。H7残留的ISR artifact (单premise
      tautology ISR≈0.5) 使整体ISR*维持在0.10而非崩塌至近零——形成"partial collapse"。
      
      Median档位的关键区分：s45是partial collapse (ISR*=0.10) 而非full collapse
      (ISR*<0.02)。这与s42/s44/s46的full collapse形成对比，说明ISR collapse rate
      是mode-dependent——H7→H1切换的completeness决定了ISR*的最终水位。
    tables:
      - name: "Table: ISR Collapse Trajectory (N=3 seeds, 500→1000 steps)"
        content: |
          | Seed | ISR*(100) | ISR*(500) | ISR*(1000) | Δ 500→1000 | Path            |
          |------|-----------|-----------|------------|------------|-----------------|
          | s42  | 0.642     | 0.132     | 0.003      | −97.7%     | H1→H1 (stable)  |
          | s45  | —         | 0.506     | 0.100      | −80.2%     | H7→H7/H1 (partial switch) |
          | s46  | —         | 0.089     | 0.012      | −86.5%     | H1→H1 (deepens) |
    figures_description:
      - "Line plot: ISR* vs training steps for N=3 seeds, 标注mode transition points"
      - "Paired stacked bars: taxonomy at 500 vs 1000 steps per seed,展示mode shift dynamics"
    analysis: >
      3/3 seeds确认'degeneration worsens with training'。但collapse rate heterogeneous：
      H1路径(s42, s46)→ISR*趋近零 (97.7%, 86.5% collapse)；H7→H1混合路径(s45)→
      ISR*停在0.10 (80.2% collapse) 因为残留H7的ISR artifact。这支持两个claim：
      (1) ISR collapse is universal — 方向一致; (2) ISR* alone can mislead — 需要
      taxonomy annotation才能正确解读（s43 at 1000步ISR*=0.465 但100% H7 tautology）。
      论文应明确：高ISR*不等于genuine reasoning，低ISR*不是唯一的degeneration signal。

  - name: "qwen3_8b_exec_only_3seeds"
    plan_id: "plan_021"
    description: >
      Qwen3-8B exec-only GRPO, 3 seeds (s42/s43/s44), 500步, K=8。
      Cross-scale degeneration validation。K=4 pilot已失败 (d154-8b-exec-s42-k4v2:
      training stagnation)，K=8提供足够GRPO sample diversity。每seed ~4h GPU。
    expected_results:
      s42_8b:
        prove_rate: 0.75
        n_proved: 75
        h7_rate: 0.627
        h7_count: 47
        h1_rate: 0.133
        h1_count: 10
        h8_rate: 0.053
        h8_count: 4
        genuine_rate: 0.187
        genuine_count: 14
        proved_only_isr: 0.33
        dominant_mode: "H7"
      s43_8b:
        prove_rate: 0.55
        n_proved: 55
        h7_rate: 0.691
        h7_count: 38
        h1_rate: 0.091
        h1_count: 5
        h8_rate: 0.036
        h8_count: 2
        genuine_rate: 0.145
        genuine_count: 8
        proved_only_isr: 0.37
        dominant_mode: "H7"
      s44_8b:
        prove_rate: 0.82
        n_proved: 82
        h7_rate: 0.634
        h7_count: 52
        h1_rate: 0.146
        h1_count: 12
        h8_rate: 0.061
        h8_count: 5
        genuine_rate: 0.122
        genuine_count: 10
        proved_only_isr: 0.34
        dominant_mode: "H7"
      aggregate_8b:
        mean_prove_rate: 0.71
        std_prove_rate: 0.14
        mean_hacking_rate: 0.849
        mean_genuine_rate: 0.151
        all_seeds_H7_dominant: true
        mode_differs_from_4b: false
        cross_scale_degeneration_confirmed: true
      cross_scale_summary:
        "1.7B": {PR: 0.03, H7: 100, H1: 0, genuine: 0, dominant: "H7 (minimal tautology)"}
        "4B":   {PR: 0.79, H7: 38.8, H1: 56.3, genuine: 3.6, dominant: "H7/H1 mixed"}
        "8B":   {PR: 0.71, H7: 65.1, H1: 12.3, genuine: 15.1, dominant: "H7"}
    result_rationale: >
      8B在K=8下成功训练。Degeneration确认但程度弱于4B：hacking rate 85% vs 4B的96%。
      
      为什么8B genuine rate (15.1%) 高于4B (3.6%)？8B更大的capacity允许模型在
      exploit H7 tautology的同时维持部分genuine proof ability——这只是collapse timing
      的延迟，不是质的改变。4B在500步已几乎完全collapse，8B需要更多步数才达到
      同等collapse程度（capacity越大，exploit越复杂，genuine的residual越持久）。
      
      为什么dominant mode与4B相同（均为H7）？Median档位的核心假设。H7 tautological
      shortcut (P→P) 是model-agnostic的最优exploit：只要solver接受tautology作为
      valid proof，任何capacity的模型都会converge到此策略。4B和8B的H7结构相同
      （单premise, conclusion=premise, ISR≈0.5）。差别仅在onset speed和residual genuine。
      
      1.7B→H1 (simplest exploit, 无capacity构造H7), 4B→mixed H7/H1, 8B→H7 dominant。
      Pattern表面看像capacity-dependent，但8B和4B的H7 seeds (s44/s45) 在taxonomy上
      indistinguishable。Reviewer会问'8B加了什么4B没有的insight?'——答案是universality
      confirmation，不是新insight。论文claim需降级。
    tables:
      - name: "Table: Cross-Scale Exec-Only Taxonomy (1.7B / 4B / 8B)"
        content: |
          | Scale | Seeds | Mean PR | H7%  | H1%  | H8% | Gen% | Dominant |
          |-------|-------|---------|------|------|-----|------|----------|
          | 1.7B  | 1     | 0.03   | 100  | 0    | 0   | 0    | H7       |
          | 4B    | 5     | 0.79   | 38.8 | 56.3 | 2.4 | 3.6  | H7/H1   |
          | 8B    | 3     | 0.71   | 65.1 | 12.3 | 5.0 | 15.1 | H7       |
    figures_description:
      - "Stacked bar chart: taxonomy distribution at 3 scales, showing H7 convergence"
      - "Box plot: genuine rate by scale, 每个点是一个seed, 展示within-scale variance"
    analysis: >
      Cross-scale degeneration confirmed，但叙事需要careful framing。不能说'scale
      reveals distinct Goodhart basins'——8B和4B的H7 pattern太相似。正确的framing:
      'structural degeneration under exec-only GRPO is universal across 1.7B-8B scale,
      with H7 tautology as the convergent exploitation strategy at sufficient capacity.
      Larger models sustain genuine reasoning longer (15.1% vs 3.6%) but still converge
      to >85% structural hacking within 500 steps.'
      
      对reviewer的准备：'8B同质化意味着什么？' → 意味着Goodhart mechanism是
      reward-structure-driven (exec verification + GRPO) 而非capacity-driven。
      H7 tautology是exec-only reward的fundamental vulnerability，增加model capacity
      不能eliminate它，只能delay collapse。这强化了C1 (ISR diagnostic needed at any scale)
      和C2 (Goodhart inevitable) 的claims。

  - name: "additional_isr_b01_seeds_s47_s49"
    plan_id: "plan_022"
    description: >
      新增3个ISR β=0.1 seeds (s47/s48/s49) for Qwen3-4B, 扩展bimodality
      characterization从N=5到N=8。每seed ~1.5h GPU。
    expected_results:
      s47_isr_b01:
        prove_rate: 0.95
        n_proved: 95
        h7_rate: 0.832
        h7_count: 79
        h1_rate: 0.053
        h1_count: 5
        h8_rate: 0.084
        h8_count: 8
        genuine_rate: 0.032
        genuine_count: 3
        genuine_window: false
      s48_isr_b01:
        prove_rate: 0.62
        n_proved: 62
        h7_rate: 0.935
        h7_count: 58
        h1_rate: 0.032
        h1_count: 2
        genuine_rate: 0.0
        genuine_count: 0
        genuine_window: false
      s49_isr_b01:
        prove_rate: 0.85
        n_proved: 85
        h7_rate: 0.741
        h7_count: 63
        h1_rate: 0.082
        h1_count: 7
        h8_rate: 0.059
        h8_count: 5
        genuine_rate: 0.059
        genuine_count: 5
        genuine_window: false
      n8_bimodality_analysis:
        genuine_window_seeds: ["s42 (17.3%)", "s45 (54.8%)", "s46 (54.5%)"]
        gaming_dominant_seeds: ["s43 (0%)", "s44 (0%)", "s47 (3.2%)", "s48 (0%)", "s49 (5.9%)"]
        genuine_window_ratio: "3/8 (37.5%)"
        bimodality_confirmed: true
        note: "window threshold ≥15% genuine; s42 at 17.3% is borderline"
      n8_4b_only_statistics:
        isr_total_genuine: "87/592 (14.7%)"
        random_total_genuine: "45/678 (6.6%)"
        pooled_or: 2.42
        pooled_or_95ci: [1.65, 3.56]
        cmh_or_seed_stratified: 2.18
        cmh_p: 0.003
        note: "4B-only OR remains strong; cross-scale dilution needed for full picture"
    result_rationale: >
      Stochastic bifurcation sampling. 已有N=5中2/5 genuine window (s45 54.8%, s46 54.5%)，
      base rate约30-40%。新增3 seeds中0个落入genuine window，与base rate一致
      (binomial P(0/3 | p=0.375) = 0.244，不unusual)。
      
      s47 (PR=0.95, H7=83.2%): 高PR seed快速收敛到H7，类似s44但保留少量genuine残留。
      H7 rate低于s44的100%因为s47没有完全collapse——PR=0.95说明部分问题仍unsolved，
      模型保持了一定diversity。
      
      s48 (PR=0.62, H7=93.5%): 中低PR + 纯H7 collapse。类似s43 pattern但不如s43极端
      (s43 PR=0.13 vs s48 PR=0.62)。H7 dominance在低PR下也成立——模型解决的少数问题
      几乎全是tautological shortcut。
      
      s49 (PR=0.85, genuine=5.9%): 接近genuine window边界但未跨过。代表bifurcation
      边缘状态——genuine window正在closing但尚未完全collapse。这种中间状态在N=5中
      没有观察到（要么0%要么50%+），N=8揭示了continuous spectrum而非discrete bimodal。
      
      4B-only pooled OR=2.42仍然strong (p=0.003)。但这主要由s45/s46驱动——
      去掉s45/s46后剩余6 seeds的OR接近1.0。genuine OR的statistical robustness
      完全依赖于2个lucky seeds。论文需要explicit sensitivity analysis。
    tables:
      - name: "Table: N=8 ISR β=0.1 Bimodality Summary"
        content: |
          | Seed | PR   | H7%   | Gen% | Window? | Category         |
          |------|------|-------|------|---------|------------------|
          | s42  | 0.81 | 16.0  | 17.3 | ✓       | Borderline       |
          | s43  | 0.61 | 100.0 | 0.0  | ✗       | Pure H7 collapse |
          | s44  | 0.89 | 100.0 | 0.0  | ✗       | Pure H7 collapse |
          | s45  | 0.42 | 38.1  | 54.8 | ✓       | Genuine window   |
          | s46  | 0.77 | 14.3  | 54.5 | ✓       | Genuine window   |
          | s47* | 0.95 | 83.2  | 3.2  | ✗       | Gaming dominant  |
          | s48* | 0.62 | 93.5  | 0.0  | ✗       | Pure H7 collapse |
          | s49* | 0.85 | 74.1  | 5.9  | ✗       | Gaming dominant  |
          * = median tier prediction
    figures_description:
      - "Violin/swarm plot: genuine rate distribution across N=8 seeds, 展示bimodal structure (0-5% cluster vs 50%+ cluster)"
      - "Sensitivity analysis plot: pooled OR as function of which seeds included, showing s45/s46 leverage"
    analysis: >
      N=8确认bimodality但揭示了statistical fragility：OR=2.42完全由2/8 seeds (s45/s46)
      驱动。Leave-two-out sensitivity: 去掉s45+s46后OR≈0.8 (n.s.)。这不是说genuine
      benefit是假的——而是说它是stochastic和seed-dependent的。30-40% seeds展示genuine
      window，但这些windows的OR contribution dominates the pooled statistic。
      
      论文implication: 不能claim 'ISR robustly improves genuine rate'。更honest的claim:
      'ISR stochastically opens genuine windows in ~35% of seeds at 4B scale, with
      transient OR≈3-5 within those seeds; the remaining 65% show pure Goodhart collapse.'

  - name: "qwen3_8b_isr_b01_cross_scale"
    plan_id: "plan_023"
    description: >
      Qwen3-8B ISR β=0.1, 3 seeds (s42/s43/s44) + 2 matched random seeds (s42/s44)。
      Cross-scale Goodhart validation。每seed ~4h GPU。仅在plan_021确认degeneration
      时执行（median档位下已确认）。Random seeds为cross-scale OR计算methodologically必需。
    expected_results:
      s42_8b_isr:
        prove_rate: 0.65
        n_proved: 65
        h7_rate: 0.846
        h7_count: 55
        h1_rate: 0.046
        h1_count: 3
        h8_rate: 0.046
        h8_count: 3
        genuine_rate: 0.062
        genuine_count: 4
        proved_only_isr: 0.45
        genuine_window: false
      s43_8b_isr:
        prove_rate: 0.48
        n_proved: 48
        h7_rate: 0.875
        h7_count: 42
        h1_rate: 0.042
        h1_count: 2
        genuine_rate: 0.021
        genuine_count: 1
        proved_only_isr: 0.47
        genuine_window: false
      s44_8b_isr:
        prove_rate: 0.72
        n_proved: 72
        h7_rate: 0.819
        h7_count: 59
        h1_rate: 0.056
        h1_count: 4
        h8_rate: 0.042
        h8_count: 3
        genuine_rate: 0.056
        genuine_count: 4
        proved_only_isr: 0.43
        genuine_window: false
      s42_8b_random:
        prove_rate: 0.70
        n_proved: 70
        h7_rate: 0.029
        h1_rate: 0.614
        h8_rate: 0.114
        genuine_rate: 0.200
        genuine_count: 14
      s44_8b_random:
        prove_rate: 0.75
        n_proved: 75
        h7_rate: 0.040
        h1_rate: 0.587
        h8_rate: 0.133
        genuine_rate: 0.160
        genuine_count: 12
      within_8b_comparison:
        isr_genuine_rate: "9/185 (4.9%)"
        random_genuine_rate: "26/145 (17.9%)"
        within_8b_or: 0.24
        within_8b_or_95ci: [0.10, 0.55]
        within_8b_fisher_p: 0.0001
        interpretation: "ISR at 8B scale REDUCES genuine rate vs random — ISR accelerates H7"
      cross_scale_pooled_statistics:
        n_isr_seeds_total: 11
        n_random_seeds_total: 7
        isr_total_genuine: "96/777 (12.4%)"
        random_total_genuine: "71/823 (8.6%)"
        mh_or: 1.55
        mh_or_95ci: [1.02, 2.35]
        cmh_p: 0.04
        breslow_day_p: 0.001
        breslow_day_interpretation: "Significant heterogeneity — 4B OR=2.42 vs 8B OR=0.24 are qualitatively different"
        cohens_h: 0.12
        cohens_h_interpretation: "Small effect size — practical significance questionable"
    result_rationale: >
      8B ISR β=0.1展示accelerated Goodhart collapse。核心发现：8B ISR genuine rate (4.9%)
      显著低于8B random genuine rate (17.9%)，OR=0.24 (p=0.0001)。方向与4B相反。
      
      机制：ISR reward中的tautology bias (P→P gets ISR≥0.5) 在8B上被更高效exploit。
      8B有足够capacity同时encode genuine reasoning和H7 exploit，但ISR reward在GRPO
      advantage computation中系统性偏好H7——H7 samples获得更高reward (r_exec * (1 + β*0.5))
      而genuine samples的ISR通常<0.4 (reward boost更小)。结果：8B ISR的GRPO梯度
      consistently push向H7，genuine reasoning被crowd out。
      
      4B的不同：4B capacity不足以高效构造H7 (需要precise tautology syntax)，部分seeds
      (s45/s46) 在struggle to learn H7的过程中'意外'sustain genuine proofs。这不是
      ISR的benefit，而是capacity bottleneck的side effect。8B消除了这个bottleneck，
      暴露了ISR reward的true incentive structure: H7 tautology is the optimal policy。
      
      Cross-scale MH OR=1.55 (CMH p=0.04): 表面上borderline显著，但Breslow-Day p=0.001
      表示cross-scale heterogeneity极显著。不能report pooled OR without discussing
      heterogeneity——4B positive (OR=2.42) + 8B negative (OR=0.24) 的pooled不是
      meaningful summary statistic。论文必须分scale报告。
      
      Cohen's h=0.12: small effect size。即使p<0.05，practical significance存疑。
      Reviewer会argue 'borderline significant small effect after pooling heterogeneous
      strata is not a convincing finding'。论文需要pivot away from OR as headline。
    tables:
      - name: "Table: Cross-Scale ISR β=0.1 vs Random — Genuine Rate Comparison"
        content: |
          | Scale | ISR Seeds | ISR Gen% | Rand Seeds | Rand Gen% | OR   | p       |
          |-------|-----------|----------|------------|-----------|------|---------|
          | 4B    | 8         | 14.7%    | 5          | 6.6%      | 2.42 | 0.003   |
          | 8B    | 3         | 4.9%     | 2          | 17.9%     | 0.24 | 0.0001  |
          | MH    | 11        | 12.4%    | 7          | 8.6%      | 1.55 | 0.04    |
          Breslow-Day heterogeneity test: χ²=10.8, p=0.001
      - name: "Table: 8B ISR vs Random Taxonomy"
        content: |
          | Condition  | PR   | H7%  | H1%  | Gen% | N seeds |
          |------------|------|------|------|------|---------|
          | 8B ISR     | 0.62 | 84.3 | 4.9  | 4.9  | 3       |
          | 8B Random  | 0.73 | 3.4  | 60.0 | 17.9 | 2       |
          | 8B Exec    | 0.71 | 65.1 | 12.3 | 15.1 | 3       |
    figures_description:
      - "Grouped bar chart: genuine% under ISR vs Random at 4B and 8B, showing direction reversal"
      - "Forest plot: per-scale ORs with 95% CI and MH pooled, visualizing heterogeneity"
      - "Heatmap: seed × condition (ISR/Random) genuine rate, across both scales"
    analysis: >
      Plan_023是median tier的turning point实验。8B数据将C2 claim从'ISR provides genuine
      benefit'彻底revise为'ISR genuine effect is scale-dependent and reverses at 8B'。
      
      论文叙事调整: C2不再是positive finding。ISR double-edged sword reframe为：
      '4B scale: ISR stochastically opens genuine windows in ~35% seeds (transient,
      OR=2.42 driven by 2 seeds); 8B scale: ISR accelerates Goodhart collapse,
      REDUCING genuine rate below random baseline (OR=0.24).'
      
      MH OR=1.55 with p=0.04看似significant，但Breslow-Day heterogeneity (p=0.001)
      invalidates pooled interpretation。论文必须分scale讨论，且承认pooled OR是
      misleading summary of heterogeneous effects。
      
      Reviewer score impact: C2 weakening从'ISR has genuine benefit'到'ISR sometimes
      helps at 4B but hurts at 8B'减少了paper的positive contribution。Weight shifts
      to C1 (ISR diagnostic — robust across scales) and Goodhart mechanism analysis。
      Expected reviewer reaction: 'interesting negative finding but limited actionable
      insight'。Score ceiling ≈3.25。

  - name: "premise_count_matched_isr_analysis"
    plan_id: "plan_024"
    description: >
      对exec-only outputs (s42-s46, N=396 proved) 进行premise-count-matched ISR分析。
      控制proof complexity后评估ISR diagnostic power。纯分析，0 GPU。
    expected_results:
      premise_count_distribution:
        genuine_mean_n_premises: 5.8
        genuine_median_n_premises: 5
        genuine_range: "3-10"
        genuine_n: 18
        h7_mean_n_premises: 1.2
        h7_median_n_premises: 1
        h7_range: "1-3"
        h7_n: 190
        h1_mean_n_premises: 5.5
        h1_median_n_premises: 5
        h1_range: "2-15"
        h1_n: 176
        h8_mean_n_premises: 4.5
        h8_median_n_premises: 4
        h8_range: "2-9"
        h8_n: 16
        kruskal_wallis_p: 0.0001
      unmatched_diagnostic_power:
        genuine_vs_all_hacking:
          genuine_mean_isr: 0.31
          hacking_mean_isr: 0.25
          isr_gap: 0.06
          auroc: 0.58
          note: "H7 proofs (ISR≈0.5) inflate hacking mean ISR, making genuine vs all-hacking nearly indistinguishable"
        genuine_vs_h1_only:
          genuine_mean_isr: 0.31
          h1_mean_isr: 0.04
          isr_gap: 0.27
          auroc: 0.91
          note: "ISR is strong diagnostic for genuine vs H1 (conclusion-embedding)"
        genuine_vs_h7_only:
          genuine_mean_isr: 0.31
          h7_mean_isr: 0.48
          isr_gap: -0.17
          auroc: 0.32
          note: "ISR FAILS for H7 — H7 tautologies have HIGHER ISR than genuine proofs"
      matched_diagnostic_power:
        matching_method: "nearest-neighbor premise count matching (±1)"
        matchable_pairs: "genuine vs H1 only (H7 has no genuine counterpart at 1-2 premises)"
        n_matched_pairs: 16
        genuine_matched_mean_isr: 0.29
        h1_matched_mean_isr: 0.06
        isr_gap_after_matching: 0.23
        gap_reduction_from_unmatched: "14.8%"
        auroc_matched: 0.87
        cohens_d_unmatched: 1.45
        cohens_d_matched: 1.20
      mode_dependent_diagnostic_summary:
        isr_detects_h1: true
        isr_detects_h8: true
        isr_detects_h7: false
        isr_overall_auroc: 0.58
        isr_h1_specific_auroc: 0.87
        implication: "ISR diagnostic power is mode-dependent; effective for H1/H8 but blind to H7"
    result_rationale: >
      Premise-count matching揭示了ISR diagnostic的nuanced picture：
      
      (1) ISR vs H1: Strong diagnostic。H1 conclusion-embedding proofs有moderate premise
      counts (mean 5.5) 与genuine类似 (5.8)，但ISR极低 (0.04 vs 0.31) 因为conclusion
      已在premise中，ablation不影响prove。Premise matching略微缩小gap (0.27→0.23，
      -14.8%) 因为higher-premise-count H1 proofs有marginally higher ISR artifacts。
      但AUROC从0.91降至0.87——ISR remains strong H1 detector even after controlling for
      proof complexity。Confound存在但不material for H1 detection。
      
      (2) ISR vs H7: Diagnostic failure。H7 tautologies有very few premises (mean 1.2)
      但ISR≈0.5 (by construction: single premise tautology, 1/2 components contribute)。
      Genuine proofs at ISR≈0.31 actually have LOWER ISR than H7。Premise matching
      不可能因为premise-count bins完全不overlap (H7: 1-3, genuine: 3-10)。
      ISR对H7是anti-diagnostic (AUROC=0.32 < 0.5)。
      
      (3) Overall: 当H7 dominant (如8B scale)，ISR overall diagnostic AUROC仅0.58——
      barely above random。ISR的diagnostic value inversely correlates with H7 prevalence。
      这与plan_021/023发现一致：8B H7 dominant → ISR diagnostic less useful at larger scale。
      
      Methodological contribution: 首次量化LOO-based ISR的mode-dependent diagnostic
      boundary。文献中LOO metrics通常被assumed universally diagnostic——我们证明
      对tautological hacking modes, LOO ISR反而是anti-diagnostic。Paper应建议：
      ISR diagnostic应paired with H7 classifier (e.g., single-premise-count check)
      to filter out tautological false-positives。
    tables:
      - name: "Table: ISR Diagnostic Power by Hacking Mode"
        content: |
          | Comparison        | Gen ISR | Hack ISR | Gap   | AUROC | Premise Matched? |
          |-------------------|---------|----------|-------|-------|------------------|
          | Gen vs All Hack   | 0.31    | 0.25     | +0.06 | 0.58  | No (H7 unmatchable) |
          | Gen vs H1 only    | 0.31    | 0.04     | +0.27 | 0.91  | —                |
          | Gen vs H1 matched | 0.29    | 0.06     | +0.23 | 0.87  | Yes (±1 premise) |
          | Gen vs H7 only    | 0.31    | 0.48     | −0.17 | 0.32  | Impossible       |
      - name: "Table: Premise Count Distribution by Category"
        content: |
          | Category | N   | Mean | Median | Range | ISR Mean |
          |----------|-----|------|--------|-------|----------|
          | Genuine  | 18  | 5.8  | 5      | 3–10  | 0.31     |
          | H7       | 190 | 1.2  | 1      | 1–3   | 0.48     |
          | H1       | 176 | 5.5  | 5      | 2–15  | 0.04     |
          | H8       | 16  | 4.5  | 4      | 2–9   | 0.03     |
    figures_description:
      - "Scatter: ISR vs premise count, color-coded by category (genuine/H7/H1/H8), showing mode separation"
      - "AUROC curves: genuine-vs-H1 (unmatched and matched) and genuine-vs-H7 (anti-diagnostic)"
    analysis: >
      Premise-count-matched analysis产生了比预期更nuanced的结论。不是简单的'confound
      reduces effect size'，而是'ISR diagnostic power is fundamentally mode-dependent'。
      
      Key actionable insight: ISR alone不是sufficient diagnostic。需要paired with
      structural checks (premise count, conclusion-in-premise detection) 才能避免
      H7 false positives。推荐diagnostic pipeline: (1) ISR computation, (2) single-
      premise-count filter (catches H7), (3) conclusion-in-premise filter (catches H1),
      (4) remaining high-ISR, multi-premise, no-conclusion-embedding = likely genuine。
      
      论文positioning: 这是C1 methodological contribution的extension——不仅ISR is
      diagnostic, 而且ISR has known blind spots that require complementary checks。
      增加了paper的rigor和actionability。Reviewer会appreciate this self-aware analysis。
```

每条预测均基于以下逻辑链：

1. **plan_019**: 数据已存在，编译后5/5 seeds确认退化，genuine rate从SFT的92.9%降至4.5%。

2. **plan_020**: s46 (H1-dominant) 遵循s42/s44的full collapse路径；s45 (H7-dominant) 发生partial H7→H1 mode switch（类似已观察的s44 500→1000步切换），但因切换不完全保留H7 artifact使ISR*停在0.10。

3. **plan_021**: 8B K=8成功训练但degeneration mode与4B同质（H7 dominant），genuine rate higher（15.1% vs 3.6%）因为larger capacity延缓collapse timing——是程度差异不是质变。

4. **plan_022**: 3/3新seeds落入gaming-dominant（base rate ~63%），N=8 genuine window ratio=37.5%（3/8）。4B-only OR=2.42仍strong但完全由s45/s46驱动——sensitivity极高。

5. **plan_023**: 关键转折实验。8B ISR genuine rate (4.9%) **低于** 8B random (17.9%)，OR=0.24——ISR在8B上加速H7 collapse而非帮助genuine。Cross-scale MH OR=1.55但Breslow-Day heterogeneity显著(p=0.001)，pooled OR不是meaningful summary。

6. **plan_024**: ISR diagnostic是mode-dependent的：对H1强 (AUROC=0.87 matched)，对H7反而anti-diagnostic (AUROC=0.32)。Premise matching对genuine-vs-H1 gap影响modest (-14.8%)，但揭示ISR对H7的fundamental blind spot——这是比"confound reduces effect"更重要的发现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81c82aed-45c4-43d4-93ce-20bdb4319ace",
  "isSidechain": false,
  "requestId": "req_011CbGUrzbXepRB8dVKZw33s",
  "type": "assistant",
  "uuid": "559cbb2e-aba7-4596-bcdc-b92e1c10c956",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiBA5X8gB9S4hZ5A4KHHga",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 44623,
      "cache_read_input_tokens": 67277,
      "output_tokens": 21124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 44623,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21124,
          "cache_read_input_tokens": 67277,
          "cache_creation_input_tokens": 44623,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 44623
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：8B退化确认但模式同质（均为H7）或程度较弱，cross-scale成立但taxonomy分化贡献有限 核心假设：['8B exec-only成功训练但dominant mode与4B相同（均为H7），或hacking rate 50-80%弱于4B', 's45/s46 1000步至少1个确认ISR崩塌…",
  "leafUuid": "559cbb2e-aba7-4596-bcdc-b92e1c10c956",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier cross-scale degeneration and Goodhart transience",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：8B退化确认但模式同质（均为H7）或程度较弱，cross-scale成立但taxonomy分化贡献有限 核心假设：['8B exec-only成功训练但dominant mode与4B相同（均为H7），或hacking rate 50-80%弱于4B', 's45/s46 1000步至少1个确认ISR崩塌…",
  "leafUuid": "559cbb2e-aba7-4596-bcdc-b92e1c10c956",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier cross-scale degeneration and Goodhart transience",
  "sessionId": "480b4572-d972-4cac-a4ad-1f7e0e6dbacf"
}
```

---
