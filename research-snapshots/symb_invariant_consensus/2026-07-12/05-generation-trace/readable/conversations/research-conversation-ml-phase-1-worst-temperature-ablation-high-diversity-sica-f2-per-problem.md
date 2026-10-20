# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Temperature ablation 暴露 high-diversity 下边际 SICA 收益, 或 F2 per-problem 完全无模式 

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/517f0813-4684-4ada-9eba-b76e226870d5.jsonl`
- **Structured JSON:** [`b6cd5c3e461260d699b1.json`](../../sessions/b6/b6cd5c3e461260d699b1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T15:13:12.196Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T15:13:12.196Z",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Temperature ablation 暴露 high-diversity 下边际 SICA 收益, 或 F2 per-problem 完全无模式 → 'capability trap' 作为 mechanism claim 证据不足; 需 reframe 为 empirical survey\n核心假设：[\"T=1.0 出现 Δ > 5pp 且 p < 0.10 (≥7 discordant pairs 偏 SICA), 暗示 'regardless of diversity' 在极端 T 下不成立\", \"F2 per-problem: constraint precision 分散无可读模式 (R² < 0.01), 或 precision 偏高 (>0.57) 与 'non-discriminative' 叙事矛盾 → hero figure 概念失败\", 'Temperature 正向结果与 main results 叙事冲突: T=0.7 下 SICA ≈ SC 但 T=1.0 下 SICA > SC → trap 非结构性, 仅是 default 操作条件的局限', '≥1 个实验达 p < 0.10 正向; discordant winrate 在某条件下偏离 50%']\n关键指标范围：{'temp_max_abs_delta_pp': [5.0, 10.0], 'f2_constraint_precision_mean': [0.5, 0.65], 'f2_precision_vs_entropy_slope': [-0.05, 0.12], 'aggregate_abs_weighted_delta_pp': [1.0, 2.5], 'n_exp_positive_p_below_010': [1, 2], 'c0_scaling_distinct_levels': [1, 2], 'discordant_sica_winrate': [0.55, 0.7]}\n叙事方向：从 'structural impossibility' reframe 为 'first systematic empirical survey of symbolic consensus across models, domains, and operating conditions'。放弃 'capability trap' 作为 mechanism claim, 保留为 descriptive label。Hero figure 方案 B: temperature × model response-surface heatmap (展示 SICA-SC gap 的 landscape, 绝大部分区域 ≈ 0 但角落有边际正值)。若 T=1.0 正向: 加 'boundary conditions' 节 — high T 部分打破 trap 但伴随 extraction rate 下降 + output coherence 退化, 得出 'the overhead negates the marginal gain' 结论。Title 改为 'When Does Symbolic Consensus Help? A Systematic Empirical Study'。仍冲 EMNLP, novelty 从 mechanism identification 转向 comprehensive negative-result coverage + practical operating guidelines (C0 gate + temperature-overhead tradeoff)。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\nfocus: 验证更新后的 capability trap framing: 机制从\"diversity-quality inverse correlation\"精确化为\"constraints lack discriminative power regardless of diversity level\"。新增 DeepSeek-R1-Distill-7B 作为第四个 instruction-scale 模型。F2 hero figure 现有 per-problem 数据 (n=307, vote_entropy vs exclusion_rate)。\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)\n\n1. **The Capability Trap**: Symbolic consensus methods face a fundamental tension: they require output diversity (C0>20%) to differ from voting, but extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to a noise injector. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B).\n2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.\n3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.\n\n## Core Insight\nSymbolic constraint consensus doesn't improve LLM reasoning because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these constraints lack the discriminative power to distinguish correct from incorrect answers. MAX-SAT optimization over non-discriminative constraints degenerates to noise injection, performing no better (often worse) than simple majority voting. We provide the first systematic empirical study characterizing this trap across 3 reasoning domains, 4 instruction-scale model families, and 1 full reasoning model.\n\n## Story Spine\n- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?\n- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.\n- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.\n- **Headline result**: \"Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis\n3. **\"Only Qwen models\"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B\n4. **\"Only one reasoning model\"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)\n5. **\"Only logic domain\"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.\n6. **\"MAX-SAT is over-engineering\"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.\n7. **\"Random tiebreak baseline\"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.\n8. **\"Why not just use a reasoning model?\"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.\n9. **\"How does this compare to Logic-LM / LINC?\"** → exp-015: Logic-LM × K baseline (CPU-only)\n10. **\"Weighted SC is simpler\"** → exp-016: Weighted SC baseline (CPU-only)\n11. **\"C0 is trivially derived\"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.\n12. **\"Within-family scaling?\"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.\n\n## Working Title\n**\"The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning\"**\n(Alternatives: \n- \"When Does Symbolic Consensus Help? An Empirical Answer: Rarely, and Here's Why\"\n- \"Diversity Without Quality: The Fundamental Limitation of Constraint-Based LLM Aggregation\")\n\n## Paper Structure (EMNLP 8pp + appendix)\n- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Capability Trap: C0 × Constraint Quality inverse correlation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Tiebreak Analysis: quality on tied questions only)\n- Main Figures: F1 (Method Pipeline), F2 (Capability Trap Scatter: C0 vs Constraint Precision, colored by domain, hero figure), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: flat line, contrasting with theoretical upper bound)\n- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data\n\n## Claim Risk Notes (Updated D035 + exp-014)\n- **Claim 1 mechanism refinement**: \"Inverse correlation between diversity and quality\" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: \"constraints lack discriminative power regardless of diversity level.\" Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.\n- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.\n- **Claim 3 gradient risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to \"binary indicator\". Need exp-004/007 for gradient data. OPEN.\n- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.\n- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.\n\n## Venue Fit Risks\n- EMNLP: Negative-results/analysis paper. Must answer \"so what should practitioners do?\" → C0 as deployment diagnostic + overhead analysis.\n- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.\n- Statistical power: Now strong (N>1,200 combined across powered tests).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes\n    odd K=11 to test if SICA value persists without exact ties. Key questions: does\n    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency\n    change with K?'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如\n    gap>0 → SICA has value beyond tiebreaking。\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Within-Qwen scaling dimension.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX\n    PRO 6000 单卡可放。\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。\n- id: exp-010\n  name: sica_mistral_7b\n  claim:\n  - 2\n  - 3\n  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family\n    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''\n    attack.'\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: DONE\n  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+\n    题（~3h GPU，margin 允许）。'\n  registry_id: exp-010-mistral-v3\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- id: exp-011\n  name: sica_llama_8b\n  claim:\n  - 2\n  - 3\n  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.\n    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation\n    同 exp-010。\n- id: exp-012\n  name: gsm8k_pilot_14b\n  claim:\n  - 2\n  - 3\n  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:\n    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer\n    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain\n    win.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable\n    insight.\n- id: exp-013\n  name: constraint_ablation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count\n    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:\n    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability\n    trap.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability\n    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'\n- id: exp-014\n  name: sica_deepseek_r1_llama_8b\n  claim:\n  - 2\n  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning\n    model data point with LLaMA base architecture: validates C0<5% generalizes beyond\n    QwQ-32B AND eliminates ''still Qwen family'' attack.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。\n- id: exp-015\n  name: logic_lm_baseline\n  claim:\n  - 1\n  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style\n    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT\n    multi-trace aggregation adds value beyond FOL extraction itself.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL\n    constraints 做单 trace verification then vote。'\n- id: exp-016\n  name: weighted_sc_baseline\n  claim:\n  - 1\n  - 3\n  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes\n    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.\n    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),\n    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count\n    weighted (no SAT)。'\n- id: exp-017\n  name: sica_strategyqa_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning\n    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected\n    constraint quality. Tests capability trap in best-case-diversity scenario.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability\n    trap（diversity high but quality low → no gain）。\n- id: exp-018\n  name: sica_arc_challenge_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,\n    4-choice format. Tests constraint mechanism in multi-choice scenario + different\n    domain.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)\n    + StrategyQA (binary) 形成答案格式多样性。\n- id: exp-019\n  name: constraint_quality_correlation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only analysis: compute constraint precision per domain × model,\n    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality\n    correlation. Uses data from exp-001/010/011/017/018.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-017\n  - exp-018\n  status: planned\n  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent\n    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have\n    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K6_sica: 0.733\n    K6_sc: 0.733\n    K6_gap_pp: 0\n    K8_sica: 0.733\n    K8_sc: 0.75\n    K8_gap_pp: -1.7\n    K11_sica: 0.733\n    K11_sc: 0.733\n    K11_gap_pp: 0\n    K12_sica: 0.7\n    K12_sc: 0.75\n    K12_gap_pp: -5\n    K16_sica: 0.717\n    K16_sc: 0.75\n    K16_gap_pp: -3.3\n    K20_sica: 0.7\n    K20_sc: 0.733\n    K20_gap_pp: -3.3\n    all_K_sica_leq_sc: true\n    larger_K_degrades_sica: true\n- exp_id: sica_constraint_ablation_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    maxsat_accuracy: 0.7649\n    count_only_accuracy: 0.7662\n    random_weight_accuracy: 0.7637\n    sc_baseline_accuracy: 0.7624\n    n_problems: 804\n    agreement_802_of_804: true\n    mcnemar_p_all_gt_0.7: true\n    note: approximate (raw z3 formulas unavailable, count-only/random-weight use proxy)\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwq_aggregate_c0_nominal_pct: 10.3\n    qwq_aggregate_c0_effective_pct: 2.6\n    qwen14b_c0_pct: 46\n    diversity_ratio_effective: 17.7\n    aime_delta_pp: 0\n    proofwriter_delta_pp: -5.9\n    aime_n: 22\n    proofwriter_n: 17\n    temp_diversity_n: 5\n    folio_n: 2\n    total_problems: 46\n    c0_threshold: 20\n    qwq_below_threshold: true\n- exp_id: exp-011-llama8b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-016-weighted-sc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7649\n    sc_uniform_accuracy: 0.7624\n    inv_length_accuracy: 0.7674\n    length_weighted_accuracy: 0.7525\n    constraint_count_accuracy: 0.7525\n    inv_length_vs_sc_p: 0.453\n    length_vs_sc_p: 0.153\n    inv_length_vs_sica_p: 0.864\n    length_vs_sica_p: 0.066\n    n_problems: 804\n    all_nonsignificant: true\n- exp_id: exp-010-mistral\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-011-llama8b-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-018-arc\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.5667\n    sc_accuracy: 0.5333\n    delta_pp: 3.33\n    mcnemar_chi2: 0.5\n    mcnemar_p: n.s.\n    bootstrap_ci_95:\n    - 0\n    - 8.33\n    bootstrap_p_delta_le_0: 0.1346\n    multi_candidate_rate: 0.1\n    contradiction_detected: 5\n    extraction_rate_problem: 1\n    extraction_rate_trace: 0.704\n    discordant_sica_wins: 2\n    discordant_sc_wins: 0\n- exp_id: pilot-constraint-filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 43\n    thresholds_tested:\n    - 1\n    - 2\n    - 3\n    - 5\n    - 7\n    best_gap_pp: 2.33\n    best_T: 1\n    sica_T1: 0.7674\n    sc: 0.7442\n    T5_gap: 0\n    T7_gap: 0\n    discriminative_ratio_count: 0.115\n    discriminative_ratio_weight: 0.372\n    effective_flip_rate: 0.174\n    multi_answer_problems: 23\n    unanimous_problems: 20\n    problems_disc_favors_different: 4\n- exp_id: exp-018-arc-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.95\n    sc_accuracy: 0.9667\n    delta_pp: -1.67\n    multi_candidate_rate: 0.05\n    extraction_rate: 1\n    contradiction_detected: 3\n    discordant_sica_wins: 0\n    discordant_sc_wins: 1\n    dataset: ARC-Challenge\n    model: Qwen2.5-14B-Instruct\n- exp_id: exp-011-llama8b-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6667\n    sc_accuracy: 0.6\n    delta_pp: 6.67\n    multi_candidate_rate: 0.6167\n    extraction_rate: 0.8556\n    answer_extraction_rate: 0.8958\n    contradiction_rate: 0.0527\n    problems_with_contradictions: 43\n    truncated_traces: 44\n    discordant_sica_wins: 5\n    discordant_sc_wins: 1\n    mcnemar_p: 0.2188\n    proofwriter_sica: 0.6333\n    proofwriter_sc: 0.6\n    proofwriter_delta_pp: 3.33\n    folio_sica: 0.7\n    folio_sc: 0.6\n    folio_delta_pp: 10\n    model: LLaMA-3.1-8B-Instruct\n    dataset: D012\n    wall_time_min: 66.4\n- exp_id: pilot-contrastive-prompt\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- exp_id: exp-019-llama8b-strategyqa-200\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    k: 12\n    sica_accuracy: 0.74\n    sc_accuracy: 0.72\n    delta_pp: 2\n    multi_candidate_rate: 0.41\n    mcnemar_p: 0.424\n    bootstrap_ci_95:\n    - -1.5\n    - 5.5\n    bootstrap_p_delta_le_0: 0.12\n    discordant_sica_wins: 9\n    discordant_sc_wins: 5\n    discordant_total: 14\n    discordant_rate: 0.07\n    sc_unanimous_rate: 0.545\n    model: LLaMA-3.1-8B-Instruct\n    dataset: StrategyQA\n    wall_time_min: 52\n- exp_id: exp-020-llama8b-folio-204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.608\n    sc_accuracy: 0.632\n    delta_pp: -2.45\n    mcnemar_p: 0.2668\n    bootstrap_ci_95:\n    - -5.88\n    - 0.98\n    bootstrap_p_sica_ge_sc: 0.1\n    discordant_sica_wins: 4\n    discordant_sc_wins: 9\n    discordant_total: 13\n    discordant_rate: 0.064\n    multi_candidate_rate: 0.618\n    extraction_rate: 0.942\n    answer_extraction_rate: 0.951\n    contradiction_rate: 0.062\n    both_wrong: 71\n    model: LLaMA-3.1-8B-Instruct\n    dataset: FOLIO-204\n    wall_time_min: 131.7\n- exp_id: exp-009-overhead-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 804\n    mean_total_wall_s: 61.6\n    mean_trace_gen_s: 31.6\n    trace_gen_pct: 51.3\n    mean_extract_s: 29\n    extract_pct: 47\n    mean_dedup_s: 1\n    dedup_pct: 1.6\n    mean_maxsat_s: 0.003\n    maxsat_pct: 0.005\n    sica_overhead_s: 30\n    sica_overhead_pct: 48.7\n    pw_overhead_pct: 51.3\n    folio_overhead_pct: 38.6\n    p50_overhead_pct: 48.9\n    p90_overhead_pct: 57.6\n- exp_id: exp-014-deepseek-r1-7b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6833\n    sc_accuracy: 0.7167\n    delta_pp: -3.33\n    multi_candidate_rate: 0.583\n    extraction_rate: 0.839\n    answer_extraction_rate: 0.939\n    truncated_traces: 72\n    contradiction_rate: 0.037\n    wall_time_min: 100.3\n    mcnemar_p: 0.4795\n    discordant_sica_wins: 0\n    discordant_sc_wins: 2\n    model: DeepSeek-R1-Distill-Qwen-7B\n    dataset: D012\n- exp_id: temperature-ablation-t03\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: temperature-ablation-t05\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: temperature-ablation-t10\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: temperature_ablation_t03_t05_t10\n  claim: Claim 1 (Capability Trap)\n  description: T=0.3/0.5/1.0 on Qwen-14B D012 60题。预期 T↑→C0↑ 但 gap 不变，证明 diversity\n    增加不改善 SICA。\n  estimated_gpu_hours: 3.0\n- name: gsm8k_pilot_30q\n  claim: Claim 2 (Operating Regime Empty)\n  description: Qwen-14B GSM8K 30题 pilot。数学推理域覆盖。预期 C0 低（14B 在 GSM8K 上 accuracy>80%）。\n  estimated_gpu_hours: 1.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T15:13:12.200Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T15:13:12.200Z",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-17T15:13:12.226Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Temperature ablation 暴露 high-diversity 下边际 SICA 收益, 或 F2 per-problem 完全无模式 → 'capability trap' 作为 mechanism claim 证据不足; 需 reframe 为 empirical survey
核心假设：["T=1.0 出现 Δ > 5pp 且 p < 0.10 (≥7 discordant pairs 偏 SICA), 暗示 'regardless of diversity' 在极端 T 下不成立", "F2 per-problem: constraint precision 分散无可读模式 (R² < 0.01), 或 precision 偏高 (>0.57) 与 'non-discriminative' 叙事矛盾 → hero figure 概念失败", 'Temperature 正向结果与 main results 叙事冲突: T=0.7 下 SICA ≈ SC 但 T=1.0 下 SICA > SC → trap 非结构性, 仅是 default 操作条件的局限', '≥1 个实验达 p < 0.10 正向; discordant winrate 在某条件下偏离 50%']
关键指标范围：{'temp_max_abs_delta_pp': [5.0, 10.0], 'f2_constraint_precision_mean': [0.5, 0.65], 'f2_precision_vs_entropy_slope': [-0.05, 0.12], 'aggregate_abs_weighted_delta_pp': [1.0, 2.5], 'n_exp_positive_p_below_010': [1, 2], 'c0_scaling_distinct_levels': [1, 2], 'discordant_sica_winrate': [0.55, 0.7]}
叙事方向：从 'structural impossibility' reframe 为 'first systematic empirical survey of symbolic consensus across models, domains, and operating conditions'。放弃 'capability trap' 作为 mechanism claim, 保留为 descriptive label。Hero figure 方案 B: temperature × model response-surface heatmap (展示 SICA-SC gap 的 landscape, 绝大部分区域 ≈ 0 但角落有边际正值)。若 T=1.0 正向: 加 'boundary conditions' 节 — high T 部分打破 trap 但伴随 extraction rate 下降 + output coherence 退化, 得出 'the overhead negates the marginal gain' 结论。Title 改为 'When Does Symbolic Consensus Help? A Systematic Empirical Study'。仍冲 EMNLP, novelty 从 mechanism identification 转向 comprehensive negative-result coverage + practical operating guidelines (C0 gate + temperature-overhead tradeoff)。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: symb_invariant_consensus
focus: 验证更新后的 capability trap framing: 机制从"diversity-quality inverse correlation"精确化为"constraints lack discriminative power regardless of diversity level"。新增 DeepSeek-R1-Distill-7B 作为第四个 instruction-scale 模型。F2 hero figure 现有 per-problem 数据 (n=307, vote_entropy vs exclusion_rate)。

## paper_framing.md

# Paper Framing — symb_invariant_consensus

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25)
- Deadline: May 25, 2026 (ARR submission)

## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)

1. **The Capability Trap**: Symbolic consensus methods face a fundamental tension: they require output diversity (C0>20%) to differ from voting, but extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to a noise injector. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B).
2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.
3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.

## Core Insight
Symbolic constraint consensus doesn't improve LLM reasoning because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these constraints lack the discriminative power to distinguish correct from incorrect answers. MAX-SAT optimization over non-discriminative constraints degenerates to noise injection, performing no better (often worse) than simple majority voting. We provide the first systematic empirical study characterizing this trap across 3 reasoning domains, 4 instruction-scale model families, and 1 full reasoning model.

## Story Spine
- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?
- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.
- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.
- **Headline result**: "Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level."

## Anticipated Reviewer Concerns & Defensive Experiments
1. **"Gains not statistically significant"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.
2. **"Only a better tiebreaker, not worth the overhead"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis
3. **"Only Qwen models"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B
4. **"Only one reasoning model"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)
5. **"Only logic domain"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.
6. **"MAX-SAT is over-engineering"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.
7. **"Random tiebreak baseline"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.
8. **"Why not just use a reasoning model?"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.
9. **"How does this compare to Logic-LM / LINC?"** → exp-015: Logic-LM × K baseline (CPU-only)
10. **"Weighted SC is simpler"** → exp-016: Weighted SC baseline (CPU-only)
11. **"C0 is trivially derived"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.
12. **"Within-family scaling?"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.

## Working Title
**"The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning"**
(Alternatives: 
- "When Does Symbolic Consensus Help? An Empirical Answer: Rarely, and Here's Why"
- "Diversity Without Quality: The Fundamental Limitation of Constraint-Based LLM Aggregation")

## Paper Structure (EMNLP 8pp + appendix)
- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Capability Trap: C0 × Constraint Quality inverse correlation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Tiebreak Analysis: quality on tied questions only)
- Main Figures: F1 (Method Pipeline), F2 (Capability Trap Scatter: C0 vs Constraint Precision, colored by domain, hero figure), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: flat line, contrasting with theoretical upper bound)
- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data

## Claim Risk Notes (Updated D035 + exp-014)
- **Claim 1 mechanism refinement**: "Inverse correlation between diversity and quality" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: "constraints lack discriminative power regardless of diversity level." Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.
- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.
- **Claim 3 gradient risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to "binary indicator". Need exp-004/007 for gradient data. OPEN.
- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.
- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.

## Venue Fit Risks
- EMNLP: Negative-results/analysis paper. Must answer "so what should practitioners do?" → C0 as deployment diagnostic + overhead analysis.
- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.
- Statistical power: Now strong (N>1,200 combined across powered tests).


## experiment_plan (with registry status)

- id: exp-001
  name: sica_expanded_14b
  claim:
  - 1
  - 2
  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,
    T=0.7. Maximizes statistical power for C3 significance.'
  priority: P0
  gpu_budget_hours: 14
  deps: []
  registry_id: sica_expanded_14b
  status: DONE
  conclusion: success
  metrics:
    sica_accuracy: 0.765
    sc_accuracy: 0.762
    sica_sc_gap_pp: 0.3
    n_problems: 804
    multi_candidate_rate: 0.3818
    folio_sica: 0.794
    folio_sc: 0.794
    folio_gap_pp: 0
    folio_n: 204
    proofwriter_sica: 0.755
    proofwriter_sc: 0.752
    proofwriter_gap_pp: 0.3
    proofwriter_n: 600
    extraction_rate: 0.89
    answer_extraction_rate: 1
    contradiction_rate: 0.022
    problems_with_contradictions: 331
    truncated_traces: 0
    wall_time_min: 826
- id: exp-002
  name: sica_k_ablation_14b
  claim:
  - 1
  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes
    odd K=11 to test if SICA value persists without exact ties. Key questions: does
    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency
    change with K?'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  status: planned
  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如
    gap>0 → SICA has value beyond tiebreaking。
- id: exp-003
  name: tiebreak_baseline_analysis
  claim:
  - 1
  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available
    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair
    baselines.
  priority: P0
  gpu_budget_hours: 0
  deps:
  - sica_d012_14b
  status: planned
  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%
    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'
- id: exp-004
  name: sica_7b_scaling
  claim:
  - 2
  - 3
  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does
    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-001
  status: planned
- id: exp-005
  name: qwq_32b_operating_regime
  claim:
  - 2
  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis
    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU
    needed.
  priority: P1
  gpu_budget_hours: 0
  deps: []
  status: planned
  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),
    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,
    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'
- id: exp-006
  name: c0_diagnostic_validation
  claim:
  - 3
  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0
    as predictor. CPU-only analysis over exp-001/002/004/005 results.
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  - exp-002
  - exp-004
  status: planned
- id: exp-007
  name: sica_72b_awq
  claim:
  - 2
  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:
    high-baseline non-reasoning model. Within-Qwen scaling dimension.'
  priority: P1
  gpu_budget_hours: 4
  deps:
  - exp-001
  status: planned
  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX
    PRO 6000 单卡可放。
- id: exp-008
  name: constraint_quality_case_studies
  claim:
  - 1
  description: Qualitative analysis of extracted constraints on 5-10 representative
    questions. Are constraints semantically meaningful? Do excluded constraints correspond
    to reasoning errors?
  priority: P2
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned
- id: exp-009
  name: overhead_analysis
  claim:
  - 1
  description: 'Wall-time breakdown per question: generation, constraint extraction,
    MaxSAT solving. Address ''is the overhead worth it'' concern.'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned
  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。
- id: exp-010
  name: sica_mistral_7b
  claim:
  - 2
  - 3
  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family
    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''
    attack.'
  priority: P0
  gpu_budget_hours: 1.5
  deps: []
  status: DONE
  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+
    题（~3h GPU，margin 允许）。'
  registry_id: exp-010-mistral-v3
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.4833
    sc_accuracy: 0.4833
    delta_pp: 0
    multi_candidate_rate: 0.5
    extraction_rate: 0.8819
    answer_extraction_rate: 1
    contradiction_rate: 0.0562
    discordant_sica_wins: 2
    discordant_sc_wins: 2
    mcnemar_p: 1
    proofwriter_sica: 0.4
    proofwriter_sc: 0.4
    proofwriter_delta_pp: 0
    folio_sica: 0.5667
    folio_sc: 0.5667
    folio_delta_pp: 0
    truncated_traces: 0
    model: Mistral-7B-Instruct-v0.3
    dataset: D012
- id: exp-011
  name: sica_llama_8b
  claim:
  - 2
  - 3
  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.
    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).
  priority: P0
  gpu_budget_hours: 1.5
  deps: []
  status: planned
  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation
    同 exp-010。
- id: exp-012
  name: gsm8k_pilot_14b
  claim:
  - 2
  - 3
  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:
    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer
    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain
    win.'
  priority: P1
  gpu_budget_hours: 1
  deps: []
  status: planned
  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable
    insight.
- id: exp-013
  name: constraint_ablation
  claim:
  - 1
  - 2
  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count
    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:
    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability
    trap.'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned
  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability
    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'
- id: exp-014
  name: sica_deepseek_r1_llama_8b
  claim:
  - 2
  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning
    model data point with LLaMA base architecture: validates C0<5% generalizes beyond
    QwQ-32B AND eliminates ''still Qwen family'' attack.'
  priority: P1
  gpu_budget_hours: 2
  deps: []
  status: planned
  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。
- id: exp-015
  name: logic_lm_baseline
  claim:
  - 1
  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style
    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT
    multi-trace aggregation adds value beyond FOL extraction itself.
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned
  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL
    constraints 做单 trace verification then vote。'
- id: exp-016
  name: weighted_sc_baseline
  claim:
  - 1
  - 3
  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes
    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.
    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned
  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),
    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count
    weighted (no SAT)。'
- id: exp-017
  name: sica_strategyqa_14b
  claim:
  - 1
  - 2
  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning
    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected
    constraint quality. Tests capability trap in best-case-diversity scenario.
  priority: P0
  gpu_budget_hours: 1.5
  deps: []
  status: planned
  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability
    trap（diversity high but quality low → no gain）。
- id: exp-018
  name: sica_arc_challenge_14b
  claim:
  - 1
  - 2
  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,
    4-choice format. Tests constraint mechanism in multi-choice scenario + different
    domain.
  priority: P0
  gpu_budget_hours: 1.5
  deps: []
  status: planned
  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)
    + StrategyQA (binary) 形成答案格式多样性。
- id: exp-019
  name: constraint_quality_correlation
  claim:
  - 1
  - 2
  description: 'CPU-only analysis: compute constraint precision per domain × model,
    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality
    correlation. Uses data from exp-001/010/011/017/018.'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-001
  - exp-017
  - exp-018
  status: planned
  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent
    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have
    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'


## registry (completed experiments)

- exp_id: crd_folio_main
  name: ''
  status: DONE
  conclusion: success
  metrics:
    divergence_rate: 0.422
    diagnosis_rate: 0.872
    error_types: 4
    directed_advantage_pp: 4.7
    directed_p_value: 0.63
    localization_accuracy: 0.946
    fol_accuracy: 0.789
    code_accuracy: 0.598
    oracle_accuracy: 0.878
    pipeline_accuracy: 0.814
    baseline_accuracy: 0.74
    cost_multiplier: 5.76
    dataset: FOLIO
    n: 204
- exp_id: smoke-test-5q
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: sica_smoke_5q
  name: ''
  status: DONE
  conclusion: success
  metrics:
    sica_accuracy: 0.8
    sc_accuracy: 0.8
    extraction_rate: 1
    problems_with_contradictions: 1
    total_problems: 5
    total_time_s: 3505
    avg_time_per_problem_s: 701
    per_problem:
    - id: algebra/2470
      level: 1
      sica_correct: true
      sc_correct: true
      constraints: 27
      unique: 9
      excluded: 0
    - id: prealgebra/65
      level: 2
      sica_correct: true
      sc_correct: true
      constraints: 26
      unique: 2
      excluded: 0
    - id: number_theory/847
      level: 3
      sica_correct: true
      sc_correct: true
      constraints: 21
      unique: 11
      excluded: 0
      note: 14 JSON parse failures, 1693s
    - id: precalculus/1199
      level: 4
      sica_correct: false
      sc_correct: false
      constraints: 35
      unique: 6
      excluded: 0
      note: graph-reading problem, model cannot see image
    - id: algebra/2277
      level: 5
      sica_correct: true
      sc_correct: true
      constraints: 60
      unique: 6
      satisfied: 3
      excluded: 3
- exp_id: sica_temp_diversity
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    temperatures_tested:
    - 0.7
    - 0.9
    - 1
    problems_tested: 3
    problems_with_divergence: 0
    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.
      Reasoning model's deterministic chain dominates sampling randomness.
    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)
    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for
      trace diversity
- exp_id: mvp_math50_t07
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: sica_aime30_t07
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: sica_aime30_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    progress: 4/30
    sica_accuracy_interim: 3/4 (75%)
    sc_accuracy_interim: 3/4 (75%)
    avg_time_per_problem_s: 557
    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted
    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds
    issue: vLLM service likely crashed or OOM at Problem 5
    analysis_contradiction_rate_aime: 50% (2/4)
    analysis_contradiction_rate_math: 20% (1/5)
    analysis_unique_constraints_per_problem_aime: 18.7
    analysis_exclusion_rate: 10.7%
    analysis_sica_sc_agreement: 9/9 (100%)
    analysis_signal: weak positive - mechanism works but SC too unanimous to flip
    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure
- exp_id: sica_aime30_v3
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    progress: 22/30
    sica_accuracy_interim: 16/22 (72.7%)
    sc_accuracy_interim: 16/22 (72.7%)
    sica_sc_gap_pp: 0
    avg_time_per_problem_s: 645.9
    runtime_h: 5.9
    remaining_problems: 8
    vote_diversity_analysis:
      valid_problems: 16
      total_problems: 22
      multi_candidate_rate: 0
      zero_vote_problems: 6
      zero_vote_indices:
      - 1
      - 7
      - 8
      - 10
      - 13
      - 14
      constraints_extracted: 19/22
      exclusion_rate: 0.387
      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.
        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.
    process_status: gone (cron miss 1/5)
- exp_id: sica_proofwriter30
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    sica_accuracy: 0/30 (0.0%)
    sc_accuracy: 0/30 (0.0%)
    sica_sc_gap_pp: 0
    total_wall_time_s: 238.9
    total_wall_time_min: 4
    avg_time_per_problem_s: 8
    traces_generated: 0
    constraints_extracted: 0
    traces_with_constraints: 0
    unique_constraints: 0
    maxsat_satisfied: 0
    maxsat_excluded: 0
    multi_candidate_rate: N/A (no traces generated)
    vote_diversity: N/A
    z3_errors: 0
    z3_timeouts: 0
    problems_with_contradiction: 0
    problems_with_votes: 0
    failure_mode: ALL_400_BAD_REQUEST
    failure_count: 30/30
    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for
      prompt input. Every API call returns 400.
- exp_id: sica_folio30
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: sica_proofwriter30_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: sica_d016_c0_precheck
  name: ''
  status: DONE
  conclusion: success
  metrics:
    multi_candidate_rate_combined: 0.46
    multi_candidate_rate_folio: 0.4
    multi_candidate_rate_proofwriter: 0.5
    sc_accuracy_combined: 0.73
    sc_accuracy_folio: 0.8
    sc_accuracy_proofwriter: 0.69
    n_problems: 26
    n_folio: 10
    n_proofwriter: 16
    K: 6
    T: 0.7
    total_time_s: 280
    c0_gate: PASS (46% >= 20%)
    model: Qwen2.5-14B-Instruct
    vllm_gpu_mem_gib: 27.6
    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem
- exp_id: sica_d012_14b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    sica_accuracy: 0.7333
    sc_accuracy: 0.7
    sica_sc_gap_pp: 3.3
    c0_multi_candidate_rate: 0.5333
    c1_extraction_rate: 1
    c2_contradiction_problems: 34
    c3_gap_pp: 3.3
    bootstrap_p: 0.2261
    proofwriter_sica: 0.6667
    proofwriter_sc: 0.6667
    folio_sica: 0.8
    folio_sc: 0.7333
    total_constraints_raw: 5849
    total_constraints_unique: 1735
    maxsat_exclusion_rate: 0.0259
    wall_time_min: 58.3
    d012_verdict: ALL_PASS
- exp_id: sica_expanded_14b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    sica_accuracy: 0.765
    sc_accuracy: 0.762
    sica_sc_gap_pp: 0.3
    n_problems: 804
    multi_candidate_rate: 0.3818
    folio_sica: 0.794
    folio_sc: 0.794
    folio_gap_pp: 0
    folio_n: 204
    proofwriter_sica: 0.755
    proofwriter_sc: 0.752
    proofwriter_gap_pp: 0.3
    proofwriter_n: 600
    extraction_rate: 0.89
    answer_extraction_rate: 1
    contradiction_rate: 0.022
    problems_with_contradictions: 331
    truncated_traces: 0
    wall_time_min: 826
- exp_id: sica_k_sensitivity_14b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K6_sica: 0.733
    K6_sc: 0.733
    K6_gap_pp: 0
    K8_sica: 0.733
    K8_sc: 0.75
    K8_gap_pp: -1.7
    K11_sica: 0.733
    K11_sc: 0.733
    K11_gap_pp: 0
    K12_sica: 0.7
    K12_sc: 0.75
    K12_gap_pp: -5
    K16_sica: 0.717
    K16_sc: 0.75
    K16_gap_pp: -3.3
    K20_sica: 0.7
    K20_sc: 0.733
    K20_gap_pp: -3.3
    all_K_sica_leq_sc: true
    larger_K_degrades_sica: true
- exp_id: sica_constraint_ablation_013
  name: ''
  status: DONE
  conclusion: success
  metrics:
    maxsat_accuracy: 0.7649
    count_only_accuracy: 0.7662
    random_weight_accuracy: 0.7637
    sc_baseline_accuracy: 0.7624
    n_problems: 804
    agreement_802_of_804: true
    mcnemar_p_all_gt_0.7: true
    note: approximate (raw z3 formulas unavailable, count-only/random-weight use proxy)
- exp_id: exp-005
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    qwq_aggregate_c0_nominal_pct: 10.3
    qwq_aggregate_c0_effective_pct: 2.6
    qwen14b_c0_pct: 46
    diversity_ratio_effective: 17.7
    aime_delta_pp: 0
    proofwriter_delta_pp: -5.9
    aime_n: 22
    proofwriter_n: 17
    temp_diversity_n: 5
    folio_n: 2
    total_problems: 46
    c0_threshold: 20
    qwq_below_threshold: true
- exp_id: exp-011-llama8b
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-016-weighted-sc
  name: ''
  status: DONE
  conclusion: success
  metrics:
    sica_accuracy: 0.7649
    sc_uniform_accuracy: 0.7624
    inv_length_accuracy: 0.7674
    length_weighted_accuracy: 0.7525
    constraint_count_accuracy: 0.7525
    inv_length_vs_sc_p: 0.453
    length_vs_sc_p: 0.153
    inv_length_vs_sica_p: 0.864
    length_vs_sica_p: 0.066
    n_problems: 804
    all_nonsignificant: true
- exp_id: exp-010-mistral
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-011-llama8b-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-017-strategyqa
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-018-arc
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-010-mistral-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-017-strategyqa-v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-017-strategyqa-v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.5667
    sc_accuracy: 0.5333
    delta_pp: 3.33
    mcnemar_chi2: 0.5
    mcnemar_p: n.s.
    bootstrap_ci_95:
    - 0
    - 8.33
    bootstrap_p_delta_le_0: 0.1346
    multi_candidate_rate: 0.1
    contradiction_detected: 5
    extraction_rate_problem: 1
    extraction_rate_trace: 0.704
    discordant_sica_wins: 2
    discordant_sc_wins: 0
- exp_id: pilot-constraint-filtering
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 43
    thresholds_tested:
    - 1
    - 2
    - 3
    - 5
    - 7
    best_gap_pp: 2.33
    best_T: 1
    sica_T1: 0.7674
    sc: 0.7442
    T5_gap: 0
    T7_gap: 0
    discriminative_ratio_count: 0.115
    discriminative_ratio_weight: 0.372
    effective_flip_rate: 0.174
    multi_answer_problems: 23
    unanimous_problems: 20
    problems_disc_favors_different: 4
- exp_id: exp-018-arc-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.95
    sc_accuracy: 0.9667
    delta_pp: -1.67
    multi_candidate_rate: 0.05
    extraction_rate: 1
    contradiction_detected: 3
    discordant_sica_wins: 0
    discordant_sc_wins: 1
    dataset: ARC-Challenge
    model: Qwen2.5-14B-Instruct
- exp_id: exp-011-llama8b-v3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.6667
    sc_accuracy: 0.6
    delta_pp: 6.67
    multi_candidate_rate: 0.6167
    extraction_rate: 0.8556
    answer_extraction_rate: 0.8958
    contradiction_rate: 0.0527
    problems_with_contradictions: 43
    truncated_traces: 44
    discordant_sica_wins: 5
    discordant_sc_wins: 1
    mcnemar_p: 0.2188
    proofwriter_sica: 0.6333
    proofwriter_sc: 0.6
    proofwriter_delta_pp: 3.33
    folio_sica: 0.7
    folio_sc: 0.6
    folio_delta_pp: 10
    model: LLaMA-3.1-8B-Instruct
    dataset: D012
    wall_time_min: 66.4
- exp_id: pilot-contrastive-prompt
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp-010-mistral-v3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.4833
    sc_accuracy: 0.4833
    delta_pp: 0
    multi_candidate_rate: 0.5
    extraction_rate: 0.8819
    answer_extraction_rate: 1
    contradiction_rate: 0.0562
    discordant_sica_wins: 2
    discordant_sc_wins: 2
    mcnemar_p: 1
    proofwriter_sica: 0.4
    proofwriter_sc: 0.4
    proofwriter_delta_pp: 0
    folio_sica: 0.5667
    folio_sc: 0.5667
    folio_delta_pp: 0
    truncated_traces: 0
    model: Mistral-7B-Instruct-v0.3
    dataset: D012
- exp_id: exp-019-llama8b-strategyqa-200
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 200
    k: 12
    sica_accuracy: 0.74
    sc_accuracy: 0.72
    delta_pp: 2
    multi_candidate_rate: 0.41
    mcnemar_p: 0.424
    bootstrap_ci_95:
    - -1.5
    - 5.5
    bootstrap_p_delta_le_0: 0.12
    discordant_sica_wins: 9
    discordant_sc_wins: 5
    discordant_total: 14
    discordant_rate: 0.07
    sc_unanimous_rate: 0.545
    model: LLaMA-3.1-8B-Instruct
    dataset: StrategyQA
    wall_time_min: 52
- exp_id: exp-020-llama8b-folio-204
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 204
    k: 12
    sica_accuracy: 0.608
    sc_accuracy: 0.632
    delta_pp: -2.45
    mcnemar_p: 0.2668
    bootstrap_ci_95:
    - -5.88
    - 0.98
    bootstrap_p_sica_ge_sc: 0.1
    discordant_sica_wins: 4
    discordant_sc_wins: 9
    discordant_total: 13
    discordant_rate: 0.064
    multi_candidate_rate: 0.618
    extraction_rate: 0.942
    answer_extraction_rate: 0.951
    contradiction_rate: 0.062
    both_wrong: 71
    model: LLaMA-3.1-8B-Instruct
    dataset: FOLIO-204
    wall_time_min: 131.7
- exp_id: exp-009-overhead-analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 804
    mean_total_wall_s: 61.6
    mean_trace_gen_s: 31.6
    trace_gen_pct: 51.3
    mean_extract_s: 29
    extract_pct: 47
    mean_dedup_s: 1
    dedup_pct: 1.6
    mean_maxsat_s: 0.003
    maxsat_pct: 0.005
    sica_overhead_s: 30
    sica_overhead_pct: 48.7
    pw_overhead_pct: 51.3
    folio_overhead_pct: 38.6
    p50_overhead_pct: 48.9
    p90_overhead_pct: 57.6
- exp_id: exp-014-deepseek-r1-7b
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.6833
    sc_accuracy: 0.7167
    delta_pp: -3.33
    multi_candidate_rate: 0.583
    extraction_rate: 0.839
    answer_extraction_rate: 0.939
    truncated_traces: 72
    contradiction_rate: 0.037
    wall_time_min: 100.3
    mcnemar_p: 0.4795
    discordant_sica_wins: 0
    discordant_sc_wins: 2
    model: DeepSeek-R1-Distill-Qwen-7B
    dataset: D012
- exp_id: temperature-ablation-t03
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: temperature-ablation-t05
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: temperature-ablation-t10
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}


## what_if (hypothetical experiments — additive)

- name: temperature_ablation_t03_t05_t10
  claim: Claim 1 (Capability Trap)
  description: T=0.3/0.5/1.0 on Qwen-14B D012 60题。预期 T↑→C0↑ 但 gap 不变，证明 diversity
    增加不改善 SICA。
  estimated_gpu_hours: 3.0
- name: gsm8k_pilot_30q
  claim: Claim 2 (Operating Regime Empty)
  description: Qwen-14B GSM8K 30题 pilot。数学推理域覆盖。预期 C0 低（14B 在 GSM8K 上 accuracy>80%）。
  estimated_gpu_hours: 1.0

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
  "promptId": "f7166fa2-af48-4120-b7de-cfc9c5dbd9c3",
  "type": "user",
  "uuid": "527ea593-2071-4298-b3d3-2687aba26ea3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T15:13:12.223Z_

```json
{
  "parentUuid": "527ea593-2071-4298-b3d3-2687aba26ea3",
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
  "uuid": "b5b537aa-7938-4334-b548-275c4c333c1d",
  "timestamp": "2026-05-17T15:13:12.223Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T15:13:12.223Z_

```json
{
  "parentUuid": "b5b537aa-7938-4334-b548-275c4c333c1d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4c6b969f-cfea-498f-8535-7820e5f9b1be",
  "timestamp": "2026-05-17T15:13:12.223Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Temperature ablation 暴露 high-diversity 下边际 SICA 收益, 或 F2 per-problem 完全无模式 → 'capability trap' 作为 mechanism claim 证据不足; 需 reframe 为 empirical survey 核心假设：…",
  "leafUuid": "4c6b969f-cfea-498f-8535-7820e5f9b1be",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Symbolic consensus capability trap empirical study",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5"
}
```

---

### Assistant

_source line 8 · 2026-05-17T15:13:15.643Z_

I'll analyze the experiment plan and generate detailed worst-tier predictions. Let me first review the current state of completed experiments and the specific worst-tier definitions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c6b969f-cfea-498f-8535-7820e5f9b1be",
  "isSidechain": false,
  "requestId": "req_011Cb8MhfAdmW9vnrm5Jc6HA",
  "type": "assistant",
  "uuid": "d5615879-d7c6-4020-87e7-679f59882a79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4oMwUecEDzBaxa3G15uyA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18798,
      "cache_read_input_tokens": 11841,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 250,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18798
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

_source line 9 · 2026-05-17T15:13:20.732Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0123qpvvq3odioXTCCCSPMPj`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan and registry",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0513_3, find all files related to experiment_plan, registry, what_if experiments, and paper_framing. I need to understand: 1) Which experiments have status \"planned\" in the experiment plan. 2) The detailed metrics from completed experiments. 3) Any temperature ablation data. Search broadly for YAML/JSON/MD files containing experiment definitions. Also look for any files with \"worst\" or \"tier\" or \"dream\" in the name."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d5615879-d7c6-4020-87e7-679f59882a79",
  "isSidechain": false,
  "requestId": "req_011Cb8MhfAdmW9vnrm5Jc6HA",
  "type": "assistant",
  "uuid": "1853e588-a070-4561-80d6-1d583e7708f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S4oMwUecEDzBaxa3G15uyA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18798,
      "cache_read_input_tokens": 11841,
      "output_tokens": 250,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18798,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 250,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18798
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

_source line 10 · 2026-05-17T15:14:06.091Z_

<details><summary>↩ Tool result · `toolu_0123qpvvq3odioXTCCCSPMPj`</summary>

```text
Excellent! Now I have enough information to provide a comprehensive summary. Let me compile my findings:

## Summary of Experiment Plans, Registries, and Dream Reports

Based on my comprehensive search through the `/home/ubuntu/.agent-ml-research-idea_gen_0513_3` directory, here's what I found:

### **1) EXPERIMENTS WITH STATUS "PLANNED"**

#### **cross_representation_disagreement_diagno project:**
From `/projects/cross_representation_disagreement_diagno/experiment_plan.yaml`:
- **exp-002**: Cross-model ablation (FOLIO) - DeepSeek V4 Pro + Qwen3-32B comparison (Priority P0)
- **exp-003**: ProofWriter extension with pilot (Priority P0, pilot_required: true)
- **exp-004**: MATH Level 5 expansion with SymPy/Python (Priority P0)
- **exp-005**: Repair mechanism improvement - multi-round repair with error-specific strategies (Priority P0)
- **exp-006**: Unknown sample deep analysis (Priority P1)
- **exp-007**: Selection vs Repair ablation (Priority P0)
- **exp-008**: Error Taxonomy ablation (Priority P1)
- **exp-009**: Statistical significance testing across benchmarks (Priority P1)
- **exp-010**: Qwen3-8B ablation (Priority P2)
- **exp-011**: GPQA Diamond extension (Priority P2)
- **exp-012**: Self-consistency baseline comparison (Priority P0)
- **exp-013**: Error Taxonomy cross-model validation (Priority P1)

#### **symb_invariant_consensus project:**
From `/projects/symb_invariant_consensus/experiment_plan.yaml`:
- **exp-002**: K sensitivity ablation (K=6,8,11,12,16,20) (Priority P0, **status: planned**)
- **exp-004**: Qwen2.5-7B scaling test (Priority P1, **status: planned**)
- **exp-006**: C0 diagnostic validation analysis (Priority P1, **status: planned**)
- **exp-007**: Qwen2.5-72B-AWQ evaluation (Priority P1, **status: planned**)
- **exp-008**: Constraint quality case studies (Priority P2, **status: planned**)
- **exp-009**: Overhead analysis (Priority P1, **status: planned**)
- **exp-010**: Mistral-7B validation (Priority P0, **status: planned**)
- **exp-011**: LLaMA-8B validation (Priority P0, **status: planned**)
- **exp-012**: GSM8K pilot (Priority P1, **status: planned**)
- **exp-013**: Constraint ablation (Priority P0, **status: planned**)
- **exp-014**: DeepSeek-R1-LLaMA-8B (Priority P1, **status: planned**)
- **exp-015**: Logic-LM baseline (Priority P1, **status: planned**)
- **exp-016**: Weighted SC baseline (Priority P1, **status: planned**)
- **exp-017**: StrategyQA evaluation (Priority P0, **status: planned**)
- **exp-018**: ARC-Challenge evaluation (Priority P0, **status: planned**)
- **exp-019**: Constraint quality correlation (Priority P0, **status: planned**)

### **2) DETAILED METRICS FROM COMPLETED EXPERIMENTS**

#### **cross_representation_disagreement_diagno (FOLIO dataset, 204 samples):**
From `/projects/cross_representation_disagreement_diagno/registry.yaml - mvp_pipeline_004`:
- **C1 (Disagree Rate)**: 42.16% (86/204 all_mode); 38.52% (52/135 excl_unknown)
- **C2 (Diagnostic Rate)**: 87.21% (75/86 all_mode); 84.62% (44/52 excl_unknown)
- **C4 (Targeted Repair Delta)**: +4.65pp (all_mode); -1.92pp (excl_unknown)
- **C5 (Localization Accuracy)**: 53.03% (35/66, 95% CI: [41.0%, 65.1%])
- **FOL:Code Asymmetry**: 56:10 ratio (5.6:1 - FOL significantly outperforms Code)
- **Cost Multiplier**: 5.76x (Code accuracy: 59.8%, Pipeline: 81.4%, Oracle: 87.8%)
- **Fisher p-value (C4)**: 0.626 (all_mode); 1.0 (excl_unknown)
- **Phi coefficient**: 0.189 (p=0.007) - FOL/Code failures moderately correlated

#### **symb_invariant_consensus (SICA method, full expanded results):**
From `/projects/symb_invariant_consensus/registry.yaml - sica_expanded_14b` (804 questions: 600 PW + 204 FOLIO):
- **SICA vs SC Gap**: +0.3pp (non-significant, p=0.38)
- **FOLIO Subset**: +2.0pp gap (p=0.14, borderline)
- **ProofWriter Subset**: -0.4pp gap (p=0.62, negative)
- **C0 (Multi-candidate Rate)**: 38.18% (38% of problems have multiple answer candidates)
- **Extraction Rate**: 89% (constraints extracted from traces)
- **Contradiction Rate**: 2.2% (331/804 problems with contradictions)
- **K=12 Ablation Results**:
  - K=6: SICA 73.3%, SC 73.3% (Δ=0pp)
  - K=12: SICA 73.3%, SC 75.0% (Δ=-5pp, SICA actually worse)
  - K=20: SICA 70%, SC 73.3% (Δ=-3.3pp)
- **LLaMA-3.1-8B**: +6.67pp (significant finding for weaker models, p=0.22 borderline)
- **Mistral-7B**: Δ=0pp (48.33% both)
- **ARC-Challenge**: -1.67pp (SICA 95% vs SC 96.67%)
- **StrategyQA**: +3.33pp (SICA 56.67% vs SC 53.33%, non-significant)

### **3) TEMPERATURE ABLATION DATA**

From `/global/checkpoints/`:
Three temperature ablation experiments are **PREPARING** status (scheduled but not yet run):
- **exp-021-temp-ablation-t03**: Temperature=0.3 (low diversity test)
  - Hypothesis: Low temp → very low C0 → SICA≈SC
  - Created: 2026-05-17T12:01:51Z
  
- **exp-022-temp-ablation-t05**: Temperature=0.5 (medium-low)
  - Created: 2026-05-17T12:01:52Z
  
- **exp-023-temp-ablation-t10**: Temperature=1.0 (high diversity)
  - Created: 2026-05-17T12:01:52Z

Note: From symb_invariant_consensus registry, there's completed analysis:
- **sica_temp_diversity** experiment (QwQ-32B): temperatures tested [0.7, 0.9, 1.0]
  - Finding: **NEGATIVE** - QwQ-32B produces zero answer divergence at all temperatures
  - Conclusion: Reasoning models are too deterministic; temperature sampling doesn't help

### **4) DREAM REPORT FINDINGS (Best/Median/Worst Tiers)**

#### **cross_representation_disagreement_diagno Dream Reports:**

**Best Tier (dream_20260515T060408)**: 
- Original dual-track framing fully validated across three benchmarks
- Claims 1-3 require no downgrade for EMNLP Main submission
- Recommended for direct EMNLP Main

**Worst Tier (dream_20260515T071730)**:
- D025 pivot: SICA ≈ SC (+0.3pp combined, non-significant)
- FOLIO gap shrinks to +2pp on 204 questions
- ProofWriter flat or negative
- Paper reframes to: "Characterizing When Symbolic Consensus Methods Fail"
- Recommends EMNLP Findings (primary) or AAAI 2027 (fallback)

#### **symb_invariant_consensus Dream Reports (dream_20260516T155754 - worst tier):**

Key findings across dream tier evaluations:
- **C0 as Necessary But Not Sufficient**: High C0 (38-65%) doesn't guarantee SICA>SC
- **Constraint Quality Bottleneck**: Only ~62% of extracted constraints are semantically correct
- **Tiebreak Analysis**: SICA wins ~58% of tiebreak situations (barely better than random 50%)
- **Operating Regime Characterization**: 
  - Reasoning models (C0<5%): Converged regime, SICA≡SC
  - Instruction models (C0>20%): Diverse regime with small/noisy gains
  - **Threshold**: C0>20% necessary but not sufficient for gains
- **MaxSAT Mechanism**: MaxSAT ≈ count-only ablation (Δ=0.1pp, p=0.72)
  - Solver sophistication adds negligible value when constraints are noisy

### **5) PAPER FRAMING FILES**

Located in:
- `/projects/cross_representation_disagreement_diagno/paper_framing.md`
- `/projects/symb_invariant_consensus/paper_framing.md`
- Multiple dream report versions in `artifacts/dream_reports/dream_*/[best|median|worst]/paper_framing.md`

These contain detailed narrative guidance for paper positioning based on experimental outcomes.

### **6) KEY FILES IDENTIFIED**

**Experiment Plans:**
- `/projects/cross_representation_disagreement_diagno/experiment_plan.yaml`
- `/projects/symb_invariant_consensus/experiment_plan.yaml`

**Registries:**
- `/projects/cross_representation_disagreement_diagno/registry.yaml`
- `/projects/symb_invariant_consensus/registry.yaml`
- `/projects/cross_representation_disagreement_diagno/dream_registry.yaml`
- `/projects/symb_invariant_consensus/dream_registry.yaml`
- `/global/registry.yaml`

**Checkpoint Files (temp ablation):**
- `/global/checkpoints/exp-021-temp-ablation-t03_PREPARING_*.json`
- `/global/checkpoints/exp-022-temp-ablation-t05_PREPARING_*.json`
- `/global/checkpoints/exp-023-temp-ablation-t10_PREPARING_*.json`
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1853e588-a070-4561-80d6-1d583e7708f6",
  "isSidechain": false,
  "promptId": "f7166fa2-af48-4120-b7de-cfc9c5dbd9c3",
  "type": "user",
  "uuid": "dee76565-f168-46f9-b31f-b93187be2d17",
  "toolUseResult": {
    "status": "completed",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0513_3, find all files related to experiment_plan, registry, what_if experiments, and paper_framing. I need to understand: 1) Which experiments have status \"planned\" in the experiment plan. 2) The detailed metrics from completed experiments. 3) Any temperature ablation data. Search broadly for YAML/JSON/MD files containing experiment definitions. Also look for any files with \"worst\" or \"tier\" or \"dream\" in the name.",
    "agentId": "a6b72841437d9b218",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now I have enough information to provide a comprehensive summary. Let me compile my findings:\n\n## Summary of Experiment Plans, Registries, and Dream Reports\n\nBased on my comprehensive search through the `/home/ubuntu/.agent-ml-research-idea_gen_0513_3` directory, here's what I found:\n\n### **1) EXPERIMENTS WITH STATUS \"PLANNED\"**\n\n#### **cross_representation_disagreement_diagno project:**\nFrom `/projects/cross_representation_disagreement_diagno/experiment_plan.yaml`:\n- **exp-002**: Cross-model ablation (FOLIO) - DeepSeek V4 Pro + Qwen3-32B comparison (Priority P0)\n- **exp-003**: ProofWriter extension with pilot (Priority P0, pilot_required: true)\n- **exp-004**: MATH Level 5 expansion with SymPy/Python (Priority P0)\n- **exp-005**: Repair mechanism improvement - multi-round repair with error-specific strategies (Priority P0)\n- **exp-006**: Unknown sample deep analysis (Priority P1)\n- **exp-007**: Selection vs Repair ablation (Priority P0)\n- **exp-008**: Error Taxonomy ablation (Priority P1)\n- **exp-009**: Statistical significance testing across benchmarks (Priority P1)\n- **exp-010**: Qwen3-8B ablation (Priority P2)\n- **exp-011**: GPQA Diamond extension (Priority P2)\n- **exp-012**: Self-consistency baseline comparison (Priority P0)\n- **exp-013**: Error Taxonomy cross-model validation (Priority P1)\n\n#### **symb_invariant_consensus project:**\nFrom `/projects/symb_invariant_consensus/experiment_plan.yaml`:\n- **exp-002**: K sensitivity ablation (K=6,8,11,12,16,20) (Priority P0, **status: planned**)\n- **exp-004**: Qwen2.5-7B scaling test (Priority P1, **status: planned**)\n- **exp-006**: C0 diagnostic validation analysis (Priority P1, **status: planned**)\n- **exp-007**: Qwen2.5-72B-AWQ evaluation (Priority P1, **status: planned**)\n- **exp-008**: Constraint quality case studies (Priority P2, **status: planned**)\n- **exp-009**: Overhead analysis (Priority P1, **status: planned**)\n- **exp-010**: Mistral-7B validation (Priority P0, **status: planned**)\n- **exp-011**: LLaMA-8B validation (Priority P0, **status: planned**)\n- **exp-012**: GSM8K pilot (Priority P1, **status: planned**)\n- **exp-013**: Constraint ablation (Priority P0, **status: planned**)\n- **exp-014**: DeepSeek-R1-LLaMA-8B (Priority P1, **status: planned**)\n- **exp-015**: Logic-LM baseline (Priority P1, **status: planned**)\n- **exp-016**: Weighted SC baseline (Priority P1, **status: planned**)\n- **exp-017**: StrategyQA evaluation (Priority P0, **status: planned**)\n- **exp-018**: ARC-Challenge evaluation (Priority P0, **status: planned**)\n- **exp-019**: Constraint quality correlation (Priority P0, **status: planned**)\n\n### **2) DETAILED METRICS FROM COMPLETED EXPERIMENTS**\n\n#### **cross_representation_disagreement_diagno (FOLIO dataset, 204 samples):**\nFrom `/projects/cross_representation_disagreement_diagno/registry.yaml - mvp_pipeline_004`:\n- **C1 (Disagree Rate)**: 42.16% (86/204 all_mode); 38.52% (52/135 excl_unknown)\n- **C2 (Diagnostic Rate)**: 87.21% (75/86 all_mode); 84.62% (44/52 excl_unknown)\n- **C4 (Targeted Repair Delta)**: +4.65pp (all_mode); -1.92pp (excl_unknown)\n- **C5 (Localization Accuracy)**: 53.03% (35/66, 95% CI: [41.0%, 65.1%])\n- **FOL:Code Asymmetry**: 56:10 ratio (5.6:1 - FOL significantly outperforms Code)\n- **Cost Multiplier**: 5.76x (Code accuracy: 59.8%, Pipeline: 81.4%, Oracle: 87.8%)\n- **Fisher p-value (C4)**: 0.626 (all_mode); 1.0 (excl_unknown)\n- **Phi coefficient**: 0.189 (p=0.007) - FOL/Code failures moderately correlated\n\n#### **symb_invariant_consensus (SICA method, full expanded results):**\nFrom `/projects/symb_invariant_consensus/registry.yaml - sica_expanded_14b` (804 questions: 600 PW + 204 FOLIO):\n- **SICA vs SC Gap**: +0.3pp (non-significant, p=0.38)\n- **FOLIO Subset**: +2.0pp gap (p=0.14, borderline)\n- **ProofWriter Subset**: -0.4pp gap (p=0.62, negative)\n- **C0 (Multi-candidate Rate)**: 38.18% (38% of problems have multiple answer candidates)\n- **Extraction Rate**: 89% (constraints extracted from traces)\n- **Contradiction Rate**: 2.2% (331/804 problems with contradictions)\n- **K=12 Ablation Results**:\n  - K=6: SICA 73.3%, SC 73.3% (Δ=0pp)\n  - K=12: SICA 73.3%, SC 75.0% (Δ=-5pp, SICA actually worse)\n  - K=20: SICA 70%, SC 73.3% (Δ=-3.3pp)\n- **LLaMA-3.1-8B**: +6.67pp (significant finding for weaker models, p=0.22 borderline)\n- **Mistral-7B**: Δ=0pp (48.33% both)\n- **ARC-Challenge**: -1.67pp (SICA 95% vs SC 96.67%)\n- **StrategyQA**: +3.33pp (SICA 56.67% vs SC 53.33%, non-significant)\n\n### **3) TEMPERATURE ABLATION DATA**\n\nFrom `/global/checkpoints/`:\nThree temperature ablation experiments are **PREPARING** status (scheduled but not yet run):\n- **exp-021-temp-ablation-t03**: Temperature=0.3 (low diversity test)\n  - Hypothesis: Low temp → very low C0 → SICA≈SC\n  - Created: 2026-05-17T12:01:51Z\n  \n- **exp-022-temp-ablation-t05**: Temperature=0.5 (medium-low)\n  - Created: 2026-05-17T12:01:52Z\n  \n- **exp-023-temp-ablation-t10**: Temperature=1.0 (high diversity)\n  - Created: 2026-05-17T12:01:52Z\n\nNote: From symb_invariant_consensus registry, there's completed analysis:\n- **sica_temp_diversity** experiment (QwQ-32B): temperatures tested [0.7, 0.9, 1.0]\n  - Finding: **NEGATIVE** - QwQ-32B produces zero answer divergence at all temperatures\n  - Conclusion: Reasoning models are too deterministic; temperature sampling doesn't help\n\n### **4) DREAM REPORT FINDINGS (Best/Median/Worst Tiers)**\n\n#### **cross_representation_disagreement_diagno Dream Reports:**\n\n**Best Tier (dream_20260515T060408)**: \n- Original dual-track framing fully validated across three benchmarks\n- Claims 1-3 require no downgrade for EMNLP Main submission\n- Recommended for direct EMNLP Main\n\n**Worst Tier (dream_20260515T071730)**:\n- D025 pivot: SICA ≈ SC (+0.3pp combined, non-significant)\n- FOLIO gap shrinks to +2pp on 204 questions\n- ProofWriter flat or negative\n- Paper reframes to: \"Characterizing When Symbolic Consensus Methods Fail\"\n- Recommends EMNLP Findings (primary) or AAAI 2027 (fallback)\n\n#### **symb_invariant_consensus Dream Reports (dream_20260516T155754 - worst tier):**\n\nKey findings across dream tier evaluations:\n- **C0 as Necessary But Not Sufficient**: High C0 (38-65%) doesn't guarantee SICA>SC\n- **Constraint Quality Bottleneck**: Only ~62% of extracted constraints are semantically correct\n- **Tiebreak Analysis**: SICA wins ~58% of tiebreak situations (barely better than random 50%)\n- **Operating Regime Characterization**: \n  - Reasoning models (C0<5%): Converged regime, SICA≡SC\n  - Instruction models (C0>20%): Diverse regime with small/noisy gains\n  - **Threshold**: C0>20% necessary but not sufficient for gains\n- **MaxSAT Mechanism**: MaxSAT ≈ count-only ablation (Δ=0.1pp, p=0.72)\n  - Solver sophistication adds negligible value when constraints are noisy\n\n### **5) PAPER FRAMING FILES**\n\nLocated in:\n- `/projects/cross_representation_disagreement_diagno/paper_framing.md`\n- `/projects/symb_invariant_consensus/paper_framing.md`\n- Multiple dream report versions in `artifacts/dream_reports/dream_*/[best|median|worst]/paper_framing.md`\n\nThese contain detailed narrative guidance for paper positioning based on experimental outcomes.\n\n### **6) KEY FILES IDENTIFIED**\n\n**Experiment Plans:**\n- `/projects/cross_representation_disagreement_diagno/experiment_plan.yaml`\n- `/projects/symb_invariant_consensus/experiment_plan.yaml`\n\n**Registries:**\n- `/projects/cross_representation_disagreement_diagno/registry.yaml`\n- `/projects/symb_invariant_consensus/registry.yaml`\n- `/projects/cross_representation_disagreement_diagno/dream_registry.yaml`\n- `/projects/symb_invariant_consensus/dream_registry.yaml`\n- `/global/registry.yaml`\n\n**Checkpoint Files (temp ablation):**\n- `/global/checkpoints/exp-021-temp-ablation-t03_PREPARING_*.json`\n- `/global/checkpoints/exp-022-temp-ablation-t05_PREPARING_*.json`\n- `/global/checkpoints/exp-023-temp-ablation-t10_PREPARING_*.json`"
      }
    ],
    "totalDurationMs": 45352,
    "totalTokens": 116234,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2587,
      "cache_read_input_tokens": 110932,
      "output_tokens": 2708,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2587
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 2708,
          "cache_read_input_tokens": 110932,
          "cache_creation_input_tokens": 2587,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2587,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 12,
      "searchCount": 10,
      "bashCount": 4,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "1853e588-a070-4561-80d6-1d583e7708f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T15:14:14.821Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YLBhwvSKwFUYXhCnQ4HA3o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dee76565-f168-46f9-b31f-b93187be2d17",
  "isSidechain": false,
  "requestId": "req_011Cb8MmdSZP3EBpbq4cj8eP",
  "type": "assistant",
  "uuid": "13e9d40d-5724-44e2-9aed-ff94dab634ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuxPVFSnG1auqhFdPeK1h9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2960,
      "cache_read_input_tokens": 30639,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2960,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 30639,
          "cache_creation_input_tokens": 2960,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2960
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

_source line 12 · 2026-05-17T15:14:14.833Z_

<details><summary>↩ Tool result · `toolu_01YLBhwvSKwFUYXhCnQ4HA3o`</summary>

```text
1	experiments:
2	- id: exp-001
3	  name: sica_expanded_14b
4	  claim:
5	  - 1
6	  - 2
7	  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,
8	    T=0.7. Maximizes statistical power for C3 significance.'
9	  priority: P0
10	  gpu_budget_hours: 14
11	  deps: []
12	  registry_id: sica_expanded_14b
13	  status: running
14	- id: exp-002
15	  name: sica_k_ablation_14b
16	  claim:
17	  - 1
18	  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes
19	    odd K=11 to test if SICA value persists without exact ties. Key questions: does
20	    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency
21	    change with K?'
22	  priority: P0
23	  gpu_budget_hours: 6
24	  deps: []
25	  status: planned
26	  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如
27	    gap>0 → SICA has value beyond tiebreaking。
28	- id: exp-003
29	  name: tiebreak_baseline_analysis
30	  claim:
31	  - 1
32	  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available
33	    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair
34	    baselines.
35	  priority: P0
36	  gpu_budget_hours: 0
37	  deps:
38	  - sica_d012_14b
39	  status: done
40	  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%
41	    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'
42	- id: exp-004
43	  name: sica_7b_scaling
44	  claim:
45	  - 2
46	  - 3
47	  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does
48	    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'
49	  priority: P1
50	  gpu_budget_hours: 2
51	  deps:
52	  - exp-001
53	  status: planned
54	- id: exp-005
55	  name: qwq_32b_operating_regime
56	  claim:
57	  - 2
58	  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis
59	    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU
60	    needed.
61	  priority: P1
62	  gpu_budget_hours: 0
63	  deps: []
64	  status: done
65	  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),
66	    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,
67	    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'
68	- id: exp-006
69	  name: c0_diagnostic_validation
70	  claim:
71	  - 3
72	  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0
73	    as predictor. CPU-only analysis over exp-001/002/004/005 results.
74	  priority: P1
75	  gpu_budget_hours: 0
76	  deps:
77	  - exp-001
78	  - exp-002
79	  - exp-004
80	  status: planned
81	- id: exp-007
82	  name: sica_72b_awq
83	  claim:
84	  - 2
85	  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:
86	    high-baseline non-reasoning model. Within-Qwen scaling dimension.'
87	  priority: P1
88	  gpu_budget_hours: 4
89	  deps:
90	  - exp-001
91	  status: planned
92	  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX
93	    PRO 6000 单卡可放。
94	- id: exp-008
95	  name: constraint_quality_case_studies
96	  claim:
97	  - 1
98	  description: Qualitative analysis of extracted constraints on 5-10 representative
99	    questions. Are constraints semantically meaningful? Do excluded constraints correspond
100	    to reasoning errors?
101	  priority: P2
102	  gpu_budget_hours: 0
103	  deps:
104	  - exp-001
105	  status: planned
106	- id: exp-009
107	  name: overhead_analysis
108	  claim:
109	  - 1
110	  description: 'Wall-time breakdown per question: generation, constraint extraction,
111	    MaxSAT solving. Address ''is the overhead worth it'' concern.'
112	  priority: P1
113	  gpu_budget_hours: 0
114	  deps:
115	  - exp-001
116	  status: planned
117	  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。
118	- id: exp-010
119	  name: sica_mistral_7b
120	  claim:
121	  - 2
122	  - 3
123	  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family
124	    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''
125	    attack.'
126	  priority: P0
127	  gpu_budget_hours: 1.5
128	  deps: []
129	  status: planned
130	  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+
131	    题（~3h GPU，margin 允许）。'
132	  registry_id: exp-010-mistral-v3
133	- id: exp-011
134	  name: sica_llama_8b
135	  claim:
136	  - 2
137	  - 3
138	  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.
139	    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).
140	  priority: P0
141	  gpu_budget_hours: 1.5
142	  deps: []
143	  status: planned
144	  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation
145	    同 exp-010。
146	- id: exp-012
147	  name: gsm8k_pilot_14b
148	  claim:
149	  - 2
150	  - 3
151	  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:
152	    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer
153	    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain
154	    win.'
155	  priority: P1
156	  gpu_budget_hours: 1
157	  deps: []
158	  status: planned
159	  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable
160	    insight.
161	- id: exp-013
162	  name: constraint_ablation
163	  claim:
164	  - 1
165	  - 2
166	  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count
167	    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:
168	    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability
169	    trap.'
170	  priority: P0
171	  gpu_budget_hours: 0
172	  deps:
173	  - exp-001
174	  status: planned
175	  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability
176	    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'
177	- id: exp-014
178	  name: sica_deepseek_r1_llama_8b
179	  claim:
180	  - 2
181	  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning
182	    model data point with LLaMA base architecture: validates C0<5% generalizes beyond
183	    QwQ-32B AND eliminates ''still Qwen family'' attack.'
184	  priority: P1
185	  gpu_budget_hours: 2
186	  deps: []
187	  status: planned
188	  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。
189	- id: exp-015
190	  name: logic_lm_baseline
191	  claim:
192	  - 1
193	  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style
194	    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT
195	    multi-trace aggregation adds value beyond FOL extraction itself.
196	  priority: P1
197	  gpu_budget_hours: 0
198	  deps:
199	  - exp-001
200	  status: planned
201	  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL
202	    constraints 做单 trace verification then vote。'
203	- id: exp-016
204	  name: weighted_sc_baseline
205	  claim:
206	  - 1
207	  - 3
208	  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes
209	    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.
210	    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'
211	  priority: P1
212	  gpu_budget_hours: 0
213	  deps:
214	  - exp-001
215	  status: planned
216	  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),
217	    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count
218	    weighted (no SAT)。'
219	- id: exp-017
220	  name: sica_strategyqa_14b
221	  claim:
222	  - 1
223	  - 2
224	  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning
225	    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected
226	    constraint quality. Tests capability trap in best-case-diversity scenario.
227	  priority: P0
228	  gpu_budget_hours: 1.5
229	  deps: []
230	  status: planned
231	  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability
232	    trap（diversity high but quality low → no gain）。
233	- id: exp-018
234	  name: sica_arc_challenge_14b
235	  claim:
236	  - 1
237	  - 2
238	  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,
239	    4-choice format. Tests constraint mechanism in multi-choice scenario + different
240	    domain.
241	  priority: P0
242	  gpu_budget_hours: 1.5
243	  deps: []
244	  status: planned
245	  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)
246	    + StrategyQA (binary) 形成答案格式多样性。
247	- id: exp-019
248	  name: constraint_quality_correlation
249	  claim:
250	  - 1
251	  - 2
252	  description: 'CPU-only analysis: compute constraint precision per domain × model,
253	    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality
254	    correlation. Uses data from exp-001/010/011/017/018.'
255	  priority: P0
256	  gpu_budget_hours: 0
257	  deps:
258	  - exp-001
259	  - exp-017
260	  - exp-018
261	  status: planned
262	  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent
263	    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have
264	    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'
265	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13e9d40d-5724-44e2-9aed-ff94dab634ca",
  "isSidechain": false,
  "promptId": "f7166fa2-af48-4120-b7de-cfc9c5dbd9c3",
  "type": "user",
  "uuid": "5a9f0f98-946b-4f44-999c-872229d087ff",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/experiment_plan.yaml",
      "content": "experiments:\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: running\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes\n    odd K=11 to test if SICA value persists without exact ties. Key questions: does\n    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency\n    change with K?'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如\n    gap>0 → SICA has value beyond tiebreaking。\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: done\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: done\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Within-Qwen scaling dimension.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX\n    PRO 6000 单卡可放。\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。\n- id: exp-010\n  name: sica_mistral_7b\n  claim:\n  - 2\n  - 3\n  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family\n    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''\n    attack.'\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+\n    题（~3h GPU，margin 允许）。'\n  registry_id: exp-010-mistral-v3\n- id: exp-011\n  name: sica_llama_8b\n  claim:\n  - 2\n  - 3\n  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.\n    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation\n    同 exp-010。\n- id: exp-012\n  name: gsm8k_pilot_14b\n  claim:\n  - 2\n  - 3\n  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:\n    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer\n    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain\n    win.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable\n    insight.\n- id: exp-013\n  name: constraint_ablation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count\n    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:\n    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability\n    trap.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability\n    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'\n- id: exp-014\n  name: sica_deepseek_r1_llama_8b\n  claim:\n  - 2\n  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning\n    model data point with LLaMA base architecture: validates C0<5% generalizes beyond\n    QwQ-32B AND eliminates ''still Qwen family'' attack.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。\n- id: exp-015\n  name: logic_lm_baseline\n  claim:\n  - 1\n  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style\n    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT\n    multi-trace aggregation adds value beyond FOL extraction itself.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL\n    constraints 做单 trace verification then vote。'\n- id: exp-016\n  name: weighted_sc_baseline\n  claim:\n  - 1\n  - 3\n  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes\n    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.\n    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),\n    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count\n    weighted (no SAT)。'\n- id: exp-017\n  name: sica_strategyqa_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning\n    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected\n    constraint quality. Tests capability trap in best-case-diversity scenario.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability\n    trap（diversity high but quality low → no gain）。\n- id: exp-018\n  name: sica_arc_challenge_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,\n    4-choice format. Tests constraint mechanism in multi-choice scenario + different\n    domain.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)\n    + StrategyQA (binary) 形成答案格式多样性。\n- id: exp-019\n  name: constraint_quality_correlation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only analysis: compute constraint precision per domain × model,\n    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality\n    correlation. Uses data from exp-001/010/011/017/018.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-017\n  - exp-018\n  status: planned\n  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent\n    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have\n    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'\n",
      "numLines": 265,
      "startLine": 1,
      "totalLines": 265
    }
  },
  "sourceToolAssistantUUID": "13e9d40d-5724-44e2-9aed-ff94dab634ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-17T15:14:14.868Z_

````json
{
  "parentUuid": "5a9f0f98-946b-4f44-999c-872229d087ff",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**symb_invariant_consensus**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"symb_invariant_consensus\")` 或 `load_project_config(\"symb_invariant_consensus\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### paper-writing-norms\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **ssh-env-setup** — 远程服务器 Python/CUDA 环境搭建规范——discovery-first 流程、PEP 668 处理、PyTorch 版本选择。当需要在远程服务器搭建训练环境时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ssh-env-setup.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/symb_invariant_consensus/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "d495b2cf-b27b-4687-a21f-fa0f781256df",
  "timestamp": "2026-05-17T15:14:14.868Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Temperature ablation 暴露 high-diversity 下边际 SICA 收益, 或 F2 per-problem 完全无模式 → 'capability trap' 作为 mechanism claim 证据不足; 需 reframe 为 empirical survey 核心假设：…",
  "leafUuid": "d495b2cf-b27b-4687-a21f-fa0f781256df",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Symbolic consensus capability trap empirical study",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5"
}
```

---

### Assistant

_source line 16 · 2026-05-17T15:20:43.661Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the project. Let me analyze each planned experiment in the experiment_plan and generate worst-tier predictions based on the worst-tier definition provided.

The worst tier means:
1. Temperature ablation reveals that at high diversity (T=1.0), SICA shows marginal positive gains (Δ > 5pp, p < 0.10), undermining the "regardless of diversity" claim
2. F2 per-problem data shows no readable pattern (R² < 0.01) OR precision is too high (>0.57), contradicting the "non-discriminative" narrative


3. Temperature results create a conflicting narrative where SICA performs similarly to SC at T=0.7 but outperforms it at T=1.0, suggesting the trap isn't fundamentally structural but rather a limitation of the default operating conditions
4. At least one experiment crosses the p < 0.10 threshold showing positive results

I'm now looking at the specific metric ranges that define worst-tier performance: temperature deltas between 5-10 percentage points, constraint precision hovering in the 0.5-0.65 range, precision-entropy slopes between -0.05 and 0.12, and aggregate weighted deltas from 1.0-2.0 percentage points.

The narrative needs a fundamental shift—moving away from claiming a structural capability trap and instead positioning this as the first systematic empirical investigation into when symbolic consensus actually helps. The centerpiece becomes a temperature by model response-surface heatmap showing how performance varies across conditions, with a new title reflecting this exploratory framing.

Looking at what's actually planned: K ablation, 7B scaling, C0 diagnostic validation, 72B AWQ quantization, and constraint quality experiments still need to run.

But there's a discrepancy between the plan and what's already completed—several experiments marked as planned actually have finished runs in the registry, including the overhead analysis, Mistral-7B, LLaMA-8B, constraint ablation, and DeepSeek-R1 variants. I need to reconcile which experiments are genuinely still pending versus which have already been executed. I'm cross-referencing the experiment plan against the registry to identify which experiments are marked as planned but actually show completion status—there's a discrepancy between the CLAUDE.md context and the yaml file that I need to reconcile to get an accurate picture of what still needs detailed predictions. I'm seeing a discrepancy between what's marked as "planned" in the experiment_plan section and what actually exists in the registry. Most experiments from exp-002 through exp-019 are listed as planned, plus a couple of what-if experiments, but the registry shows many of these already have completion status or registry IDs assigned. I'm seeing the full list of planned experiments now — exp-011 through exp-019 are all marked as planned. Even though some of these have completed entries in the registry, the user wants me to generate worst-case scenario data for every single one listed as planned in the experiment_plan, treating this as a hypothetical exercise regardless of actual completion status. Looking at the temperature ablation results, the T=1.0 condition shows differences exceeding 5 percentage points with marginal significance, which undermines the claim that performance holds regardless of diversity. The per-problem scatter plots don't show any consistent pattern supporting the non-discriminative hypothesis, and a few experiments actually reveal weak positive signals. This means I can't sustain the "structural impossibility" framing—I need to reposition this as an empirical investigation instead.

Now working through the worst-case scenarios for each planned experiment: for the K ablation, some intermediate K values might show SICA slightly outperforming SC when diversity is high, complicating the narrative that SICA stays below SC across all settings. The tiebreak analysis already has partial results suggesting SICA's tiebreak quality is reasonably competitive.

The 7B scaling experiment shows high baseline agreement (>65%) but marginal positive deltas around 3-5pp with borderline significance, hinting that weaker models combined with higher diversity might create conditions where SICA gains emerge. For QwQ-32B, the sample is small (n=46) with very low effective C0 at 2.6%, which still supports the main claim but represents a data limitation. The C0 diagnostic experiment's worst case would be a binary clustering pattern with no meaningful threshold and poor fit, suggesting C0 isn't a useful gradient indicator. The 72B AWQ results show C0 around 15%, and I'm continuing to assess what this means for the overall pattern.

Looking at the remaining experiments, the case studies reveal that constraints sometimes carry semantic weight, making it harder to dismiss them as purely non-discriminative. The overhead analysis shows substantial costs (~50%) but high extraction rates, which complicates the argument that SICA isn't worth attempting. Mistral-7B presents high C0 (~50%) with zero delta, supporting the trap hypothesis, though the sample size (n=60) leaves room for borderline directional signal. LLaMA-8B is the critical case—it shows a +6.67pp delta matching the registry with p≈0.07, which is the core problem undermining the narrative.

The math domain pilot also shows moderate C0 (20-30%) with marginal positive gains, suggesting the signal isn't isolated to instruction-following. The constraint ablation reveals MaxSAT outperforms count-only by 1-2pp, indicating the mechanism has some substance. DeepSeek-R1 complicates things further with surprisingly high C0 (~55-60%) despite being a reasoning model, blurring the instruction/reasoning distinction. Finally, Logic-LM achieves comparable results to SICA through single-trace FOL verification, suggesting the multi-trace aggregation may not add meaningful value beyond standard verification approaches.

Weighted self-consistency matches or exceeds SICA's performance, indicating a simpler baseline achieves the same effect. StrategyQA presents an anomaly with unexpectedly low C0 (~10%) on a binary task, or possibly high C0 with marginal delta gains. ARC-Challenge shows C0 near zero because the 14B model is too capable, reducing SICA to trivial self-consistency. The constraint quality correlation is weak (r < 0.2) with no discernible pattern, undermining the hero figure hypothesis. Temperature ablation at T=1.0 yields +7pp improvement (p = 0.08), which challenges the claim that results hold regardless of diversity settings.

Now I'm assembling the full YAML output while ensuring internal consistency with the worst-tier classification. I need to identify which experiments are explicitly marked as planned in the original plan versus those already executed, then include all the planned ones along with the what-if scenarios like the temperature ablation and GSM8K pilot variants. Looking at the experiment_plan more carefully, I see that exp-003 and exp-005 both have status marked as planned even though their notes indicate they're actually done or have existing data—I should include them with the other planned experiments.

Now examining the worst-tier predictions, there are some key contradictions: at T=1.0 the model shows differences greater than 5 percentage points with marginal significance, which undermines the claim about diversity-invariant behavior; the per-problem constraint precision is wildly inconsistent across F2, either nearly zero or suspiciously high; and there's a trap where SICA and SC converge at T=0.7 but diverge again at T=1.0.

The next set of constraints involves checking that at least one experiment reaches marginal significance with discordant pairs favoring SICA, and that the winrate deviates from 50-50 in certain conditions. I'm now looking at the specific metric ranges I need to satisfy: temperature-driven deltas between 5-10 percentage points, constraint precision averaging 0.5-0.65, a slope between precision and entropy from -0.05 to 0.12, aggregate weighted differences of 1-2.5 percentage points, one or two experiments hitting p < 0.10, one to two distinct scaling levels, and discordant winrates between 55-70%.

Now I'm constructing the full YAML structure and need to ensure everything stays internally consistent, starting with the LLaMA-8B worst-tier case. Looking at the registry data for the K sensitivity experiment, the previous results show SICA performing worse or equal across all K values, so I need to recalibrate my expectations for the worst tier—setting some low K values to show marginal positive gains while keeping higher K values negative to match the observed pattern.

Now examining the scaling behavior: the 7B model shows a much higher baseline (68% vs 14B's 38%) with a stronger delta of +5.0pp, though still marginally significant. This suggests weaker models have more inherent diversity that allows constraint-based aggregation to help more, but the effect remains inconsistent. The diagnostic experiment reveals a stark bimodal distribution in C0 clusters—reasoning models cluster near zero while instruction models cluster high, with no intermediate states, indicating the mechanism is fundamentally tied to model instruction-following capacity rather than a continuous diversity threshold.

The 72B AWQ experiment breaks this binary pattern with an intermediate C0 value of 22%, showing a modest +3.3pp improvement. This suggests a sweet spot exists where models are strong enough for consistency but not so deterministic that they lose the diversity needed for SICA to help.

Looking at the case studies, I'm finding that constraints do have real discriminative power at the individual example level—3 out of 8 cases show constraints correctly distinguishing right from wrong answers. The issue isn't that constraints are fundamentally broken, but that the aggregate signal gets drowned out by noise.

On the computational side, extraction overhead is substantial at 48% but extraction succeeds 89% of the time, and MaxSAT solving is negligible. This undermines the "not worth the effort" argument when the extraction rate is this high and solving is this fast.

For Mistral-7B with n=60, I'm seeing zero improvement—50% baseline with no delta—which fits the trap narrative of high diversity yielding nothing, though the small sample size raises questions about statistical power.

LLaMA-8B is the critical case: a marginal +6.67pp gain at p=0.08, just missing significance, with SICA winning 5 times versus SC winning once. The high truncation rate in this model seems to be the limiting factor.

Now looking at the GSM8K pilot with n=30, I'm seeing a moderate baseline of 27% with only +3.3pp improvement and p≈0.35, so the signal is well within noise. More importantly, the baseline isn't as low as I'd predicted, which weakens the claim that low confidence predicts uncertainty.

For the constraint ablation experiment on CPU with 804 samples, MaxSAT accuracy sits at 0.765. count-only = 0.764, random-weight = 0.763, SC = 0.762. All within 0.3pp. BUT count-only slightly > random-weight → constraints have marginal counting value.
- Result rationale: MaxSAT ≈ count-only confirms satisfiability reasoning adds nothing. But the fact that count-only ≈ random-weight ≈ SC within 0.3pp means even counting is marginal. This mostly supports the trap but with enough noise that a reviewer could argue "the effect is just underpowered."

**exp-014 (DeepSeek-R1-7B, n=60)**:
- Worst: C0 = 58% (instruction-scale behavior!), delta = -3.3pp. Distilled reasoning model behaves like instruction model. This is actually GOOD for the paper because 7B capacity can't sustain deterministic reasoning chains even after distillation from R1—the model just produces diverse outputs like any instruction-tuned 7B, making constraints non-discriminative and actually harmful.

**exp-015 (Logic-LM baseline, CPU)**:
- Logic-LM with K-way majority voting hits 0.79 on FOLIO, matching SICA's 0.794, which cleanly shows that simple FOL extraction plus voting achieves the same result as the entire MAX-SAT aggregation pipeline—the apparatus adds nothing.

**exp-016 (Weighted SC, CPU, n=804)**:
- Inverse-length weighted SC = 0.767 slightly outperforms both SICA and standard SC, suggesting that preferring shorter traces captures the same signal as constraint-based filtering without the extraction overhead, which directly undermines SICA's value.

**exp-017 (StrategyQA, n=60)**:
- C0 = 10% with delta = +3.3pp (p ≈ 0.13), showing that despite the binary answer space, the 14B model is already confident on StrategyQA with low diversity, so the small gain comes only from the handful of problems where SICA resolves multiple candidates correctly—unreliable given the small sample.

I'm noticing the registry already has exp...

Actually, let me check what's already recorded. The registry shows exp-017-strategyqa-v3 with C0=10%, Δ=+3.33pp, p≈0.13, which aligns with the worst-tier pattern.

**exp-018 (ARC-Challenge, n=60)**:
- C0 = 5% with delta = -1.67pp, meaning the 14B model is already very strong on ARC with almost no diversity to exploit, so SICA's rare constraint exclusions occasionally flip correct answers to incorrect.

The registry confirms exp-018-arc-v2: C0=5%, Δ=-1.67pp.

**exp-019 (Constraint quality correlation, CPU)**:
- Per-problem constraint precision averages 0.57, which falls within the worst-tier range, and I'm now examining how precision correlates with...

Actually, looking at the slope and R² values, there's essentially no readable pattern—the scatter plot is formless. This could mean either constraints are too diffusely scattered to show a relationship with vote entropy, or alternatively, precision is higher than expected, which would contradict the non-discriminative narrative.

**temperature_ablation (what_if, n=60)**:
- At T=0.3, C0 = 15% with delta = +1.7pp (p ≈ 0.70), and at T=0.5, C0 = 28% with delta = +1.7pp...
- T=1.0 is the critical worst-tier result: C0 = 72%, delta = +8.3pp, p = 0.07. At extreme diversity, the 72% multi-candidate rate gives SICA many opportunities to exercise constraints, and some constraints do become discriminative when diverse traces explore more solution paths. But extraction rate drops to ~0.75 from 0.89 at T=0.7, and output coherence degrades, so the marginal gain comes at a real quality cost.

**gsm8k_pilot (what_if, n=30)**:
- C0 = 23%, delta = +3.3pp, p ≈ 0.40.
- 14B is strong on GSM8K but not perfectly unanimous. The moderate diversity shows marginal positive signal at small n, which is underpowered but suggestive.

Now I'm constructing the full YAML output with precise metrics, rationale, tables, and analysis for each experiment. But I'm noticing a conflict: exp-019 in the experiment_plan is "constraint_quality_correlation" (CPU analysis), yet there's also a registry entry "exp-019-llama8b-strategyqa-200" which is a different experiment entirely. These are the same ID in different contexts. Let me clarify which is which.

The experiment_plan clearly defines exp-019 as the constraint quality correlation study, while the registry entry appears to be an additional run outside the plan. Similarly, exp-020 (LLaMA-8B FOLIO 204) is in the registry but not in the plan. I'll focus my output on the planned experiments but note these additional registry results as context. For exp-003, the plan shows it as completed CPU analysis with SICA tiebreak results at 80%.

Now I'm going through the experiment_plan to identify all experiments marked as "planned" status, including those with notes indicating they're already done or have data available. I'm realizing the user wants worst-tier predictions for all planned experiments, regardless of whether some already have actual results in the registry. The worst-case scenario data represents hypothetical outcomes that could occur, distinct from what's already been measured. Since the experiment_plan status hasn't been fully updated to reflect completed runs, I should generate predictions for everything marked as planned.

Now I'm constructing the complete YAML with detailed metrics and analysis, making sure the worst-tier narrative is internally consistent—most experiments show SICA holding close to SC, but with a few marginal breakthroughs at extreme conditions like high temperature diversity and smaller model sizes. I'm realizing the McNemar test for exp-011 actually gives p = 0.22 with those discordant pairs, which doesn't meet the p < 0.10 threshold—I'd need something closer to 7 vs 1 to get there. So for the worst tier's count of 1-2 experiments with p < 0.10, the temperature ablation at T=1.0 is likely the main candidate, and I need to verify whether that's actually one of the planned experiments.

For LLaMA-8B, I could adjust the D012 results to show 7 vs 2 discordant pairs instead, which gives a McNemar p-value just under 0.10 and a delta of about 8.3 percentage points—more realistic for n=60 than the larger effect I was considering.

But I need to be careful not to mix metrics. The worst-tier thresholds include temperature ablation deltas, experiment counts with p < 0.10, and SICA win rates across conditions, so I should think through which experiments could plausibly hit p < 0.10 and how they fit together.

For the LLaMA-8B D012 experiment, I'm considering setting the results at the edge of worst-tier: a +8.3pp improvement with 7 discordant wins for SICA against 2 for SC, which gives a McNemar p around 0.096—right at that threshold. This keeps the narrative consistent with the paper's framing while staying within the defined tier boundaries.

Now I'm looking at the temperature ablation at T=1.0, which shows slightly stronger results: +8.3pp delta, 7 SICA wins to 1 SC win, and a McNemar p of 0.070. Combined with the primary experiment, this gives me two results below the p=0.10 threshold, hitting the upper bound for worst-tier positive findings. I'm also tracking the extraction rates and diversity metrics—the primary shows 62% C0 with extraction at 0.83, while the ablation drops to 0.75 extraction but climbs to 72% C0. Now I need to compute the aggregate weighted delta across all experiments to complete the picture. showing Δ ≈ +8pp, the weighted average (by n) should be in [1.0, 2.5].
  - exp-001: n=804, Δ=+0.3pp → contributes 0.3*804 = 241.2
  - exp-010: n=60, Δ=0pp → 0
  - exp-011: n=60, Δ=+8.3pp → 498
  - exp-014: n=60, Δ=-3.3pp → |198|
  - exp-017: n=60, Δ=+3.3pp → 198
  - exp-018: n=60, Δ=-1.7pp → |102|
  - temp T=1.0: n=60, Δ=+8.3pp → 498
  - etc.
  Total n ≈ 1164, and when I sum up the weighted contributions I get 1735.2, which gives an average of 1.49pp — right in the target range.

Now looking at c0_scaling_distinct_levels, I'm seeing only 1-2 distinct C0 levels across the board. The reasoning model shows C0 below 5%, while the instruction models range from 22-68%, which suggests a pretty stark divide between model types.

For discordant_sica_winrate, I need to aggregate across experiments. Most are coming in around 50-77%, but some are pushing above the 0.7 ceiling, so I'm adjusting downward slightly to keep them within bounds.

The real tension is between needing a strong discordant imbalance for statistical significance on McNemar's test while also keeping the aggregate winrate constrained. I realize now that the [0.55, 0.7] range applies across all experiments combined, not individually, so I can have variation—some experiments with higher winrates balanced by others at 50% or lower to bring the overall average into range.

Now I'm laying out the specific discordant counts across experiments to see if I can hit both the significance threshold and the aggregate constraint.

Finishing the last few experiments and tallying everything up: SICA comes out ahead 35 to 19 across all the discordant pairs, giving me an aggregate win rate of 64.8%, which sits comfortably in the target range. Looking at the individual experiments, exp-011 with its 7-2 split is the only one that approaches statistical significance at p = 0.096. I'm ready to finalize the output now. Let me reconsider a few experiments first—exp-003 already has completed results showing SICA's tiebreak mechanism at 80%, which is actually strong performance but problematic for the narrative since it suggests the tiebreak has real value. For exp-005 with QwQ-32B, the data is sparse at n=46 with only 2.6% effective C0, so I'll use that in the worst-case tier. Now I'll draft the full YAML structure with comprehensive coverage.

Generating YAML output... Looking through the experiment plan more carefully, I see that exp-003 and exp-005 both have "planned" status but actually contain real data in their notes—exp-003 has the SICA tiebreak results and exp-005 references the QwQ-32B MVP experiments. For the worst-tier interpretation, I should generate predictions that align with what would make the analysis most challenging, using the actual data where it exists as a foundation.

For the temperature ablation experiments that are currently running (temperature-ablation-t03, t05, t10), I'll predict their outcomes in the worst-tier scenario. Now I need to think through the consistency constraints carefully—particularly around f2_constraint_precision_mean, which sits in the 0.5-0.65 range. At 57% average precision, constraints are correct more than half the time, which actually contradicts a "non-discriminative" narrative since that's better than random for 3-class tasks. I need to reconcile this tension in how I frame the worst-tier results.

Looking at f2_precision_vs_entropy_slope being near zero, there's no meaningful relationship between vote diversity and constraint quality, which supports the weak discriminativity story. But if precision is genuinely 57% and uncorrelated with entropy, I can't claim constraints completely lack discriminative power—I need to reframe this as "weakly discriminative across all conditions" rather than "non-discriminative." For the n_exp_positive_p_below_010 count of 2, I'm checking whether temperature_ablation is categorized as a planned experiment or a what_if scenario in the experiment plan. Looking at the p-values across experiments, I see exp-011 at 0.096 and the temperature ablation at T=1.0 with 0.034, both falling below the 0.10 threshold. The worst-tier definition specifically highlights the temperature ablation as the primary scenario where Δ > 5pp with p < 0.10, so I'll count both experiments and set n_exp_positive_p_below_010 to 2.

Now I need to verify the scaling behavior across model sizes — checking whether the C0 values show a smooth gradient or distinct levels. Looking at the Qwen models (7B at 68%, 14B at 38%, 72B at 22%), these appear as three separate levels rather than the 1-2 distinct levels the worst tier expects, which would actually disqualify this from the worst tier classification.

Let me recalibrate the values so the larger models cluster together — bringing 7B down to 58%, keeping 14B at 38%, and adjusting 72B to 32% creates a clearer two-level pattern where the smaller model stands apart and the larger ones converge.

Now I need to think through the aggregate_abs_weighted_delta_pp metric across all experiments, starting with the one I've already computed. Now I'm computing the aggregate absolute weighted difference across all experiments by multiplying each effect size by its sample size, summing those products, and dividing by the total sample count to get a pooled estimate. The total comes to 1.69pp, which stays within the acceptable range. Everything checks out, so I'm ready to structure the output as YAML. I need to organize all the experiments with their metadata—name, plan ID, description, expected results, rationale, and associated tables and figures. Since some experiments contribute to shared tables rather than generating their own, I should map out which experiments feed into each table before writing this out.

Writing the YAML structure... I'm continuing through the experiment plan, adding more specialized evaluations like constraint ablation studies, different model variants with SICA, baseline comparisons with logic-based and weighted self-consistency approaches, and additional dataset benchmarks across StrategyQA and ARC Challenge, plus a temperature sensitivity analysis.

Now I'm looking at a GSM8K pilot with 30 questions as another what-if scenario, and thinking through the Logic-LM baseline results more carefully—specifically how the multi-trace MAX-SAT aggregation compares to simpler voting approaches on FOLIO, which actually gives us a clean signal about where the added complexity provides value. The 4-point gap between SICA and Logic-LM suggests SICA's multi-trace aggregation is actually doing something useful, which contradicts the core claim. Let me reconsider what "worst" really means here — it's not about methodological dominance, but about results that undermine the paper's narrative about the capability trap. Results where SICA sometimes beats SC, or where the findings are messy and contradictory, are what make the paper hardest to write cleanly.

For the Logic-LM baseline, the truly problematic scenario is when Logic-LM itself outperforms both SICA and SC, because that reveals the trap isn't about constraints in general but specifically about how MAX-SAT aggregation fails to capture their value — a much more nuanced argument the paper would need to make. For the weighted SC experiment, simple inverse-length weighting beating SICA would undermine the entire motivation for constraint extraction, though the lack of statistical significance softens the blow.

Now I'm compiling the ablation results across different K values to see where SICA's performance stabilizes and where it diverges from the baseline.

Looking at the tiebreak analysis, SICA handles those edge cases much better than random or alphabetical approaches, though the practical impact is limited since ties are rare in real scenarios.

The 7B model scaling experiment shows SICA maintains its advantage even with smaller models, though the effect size is larger and statistical significance is borderline.

With the QwQ reasoning model, both methods converge completely—there's no meaningful difference anymore, suggesting these advanced models have fundamentally different behavior.

The C0 diagnostic reveals something interesting: confidence scores cluster into just two groups rather than spreading across a range, which means C0 acts more like a binary switch than a continuous predictor of performance gaps.

The 72B AWQ results are encouraging—SICA pulls ahead again with a solid margin, and this time we're seeing an intermediate C0 value rather than the binary clustering from before.

Looking at the case studies, most of the extracted constraints aren't actually helping—only a few problems have semantically meaningful discriminative constraints that improve SICA, while others just add noise.

The computational cost is substantial though: extraction takes up nearly half the overhead, while the actual MaxSAT solving is negligible. But the performance gain is so small it barely justifies the expense.

Smaller models like Mistral and LLaMA show the methods converging again with no improvement, and the C0 values are climbing higher, suggesting confidence becomes less informative as model size decreases.

LLaMA-8B is the outlier—it shows a meaningful 8.3pp gain with strong discordance, but the extraction rate and truncated traces are concerning, which is why this result stands out as problematic.

The GSM8K pilot shows modest gains, and the constraint ablation reveals that the specific weighting scheme doesn't matter much—all variants perform nearly identically within measurement noise.

DeepSeek-R1 actually performs worse with SICA, Logic-LM demonstrates that the underlying constraints have value but our aggregation method is losing that signal, and the weighted variants don't improve over the baseline.

StrategyQA shows another small SICA advantage, though again not statistically significant.

ARC-Challenge is nearly perfect for both methods with SC slightly ahead, and when I look at constraint quality directly, there's no correlation between precision and entropy—the "hero figure" hypothesis doesn't hold up across the 307 multi-candidate problems I examined.

The temperature ablation is interesting: at lower temperatures SICA and SC stay equal, but at T=1.0 with much higher disagreement, SICA pulls ahead by 8.3 percentage points, suggesting the method gains value when the base model is more uncertain.

Now looking at the GSM8K pilot results, I'm seeing extraction and coherence rates around 0.76-0.85, with SICA again outperforming SC by 3.3 points. Before I write this up in YAML, I need to verify the worst-tier thresholds—checking that constraint precision stays below 0.65 and the entropy correlation remains near zero to confirm the "capability trap" mechanism.

Checking my predictions against the tier definitions: the F2 constraint precision comes in at 0.57, the precision-entropy slope at 0.03, and R² at 0.008, all within the expected ranges. The temperature ablation shows an 8.3 point improvement at T=1.0, which fits the 5-10 point window. The aggregate weighted delta lands around 1.5pp as expected, and I'm counting two experiments with p-values below 0.01, matching the predicted range.

For the clustering analysis, I see two distinct levels forming around the 5% and 22-68% boundaries. The discordant SICA win rate comes to roughly 64.8%, sitting comfortably in the 0.55-0.7 range. All the metrics align with my predictions, so I'm ready to structure the YAML output.

Now I need to think about how to organize this efficiently—mapping which main paper tables this experiment feeds into and what visualizations would best represent the data without unnecessary repetition.

Most experiments map to one of the core tables: T1 for main results across models and domains, T2 for the capability trap analysis, T3 for constraint ablations, or T4 for tiebreak analysis. Some are supplementary material. I'm assigning each experiment to its primary contribution—exp-004 and exp-007 go to T1 and F4, exp-019 anchors F2 and T2, while others like exp-002 and exp-009 belong in the appendix. The temperature ablation might shift to a response surface heatmap if the per-problem F2 figure doesn't work out.

Speaking of which, I'm noticing a real tension in the worst tier results. The scatter plot between vote entropy and exclusion rate shows almost no correlation, and the constraint precision sits at 0.57—which is moderately discriminative, not the weak signal I'd expect. These aren't just noise; they're pointing to a genuine contradiction in the narrative. The constraints are actually somewhat effective at filtering, but that effectiveness doesn't correlate with diversity levels, which undermines the whole premise that constraint quality depends on response variation.

The reframing here is crucial: instead of claiming constraints are non-discriminative, I need to argue they're weakly discriminative but below the threshold where that marginal signal can overcome voting noise. It's a more nuanced failure mode—less punchy, but more honest about what the data shows. This shifts the mechanism from a clean "constraints don't work" to "constraints work just barely, which isn't enough."

Now I'm ready to write out the full YAML structure with all these assignments and this refined understanding of the failure mode.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d495b2cf-b27b-4687-a21f-fa0f781256df",
  "isSidechain": false,
  "requestId": "req_011Cb8MnGuKYxnB1BC18JimQ",
  "type": "assistant",
  "uuid": "12c9dae0-b910-42a3-8a9b-0fe9b28673c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01116SJ44oSeT626KWyiCaiP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10284,
      "cache_read_input_tokens": 33599,
      "output_tokens": 34677,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 34677,
          "cache_read_input_tokens": 33599,
          "cache_creation_input_tokens": 10284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10284
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

_source line 17 · 2026-05-17T15:26:04.110Z_

```yaml
tier: worst
narrative_guidance: >
  从 'structural impossibility' 全面退守为 'first systematic empirical survey of symbolic consensus
  across models, domains, and operating conditions'。核心问题：(1) Temperature ablation T=1.0 暴露
  Δ=+8.3pp (p=0.034)，打破 'regardless of diversity' 声明；(2) LLaMA-8B D012 达 p=0.096，成为
  第二个边际正向结果；(3) F2 per-problem constraint precision 均值 0.57 — 高于 random (0.33 for 3-class),
  与 'non-discriminative' 叙事矛盾；(4) C0 仅有 2 个聚类（<5% vs 22-68%），无梯度，沦为 trivial binary
  indicator。放弃 'capability trap' 作为 mechanism claim，降级为 descriptive label。Hero figure 切换
  Plan B: temperature × model response-surface heatmap（绝大部分区域 ≈ 0 但 T=1.0 角落有正值）。
  加 'boundary conditions' 节：T=1.0 部分打破 trap 但 extraction rate 下降 + output coherence 退化
  → overhead negates marginal gain。Title 改为 'When Does Symbolic Consensus Help? A Systematic
  Empirical Study'。仍冲 EMNLP，novelty 从 mechanism identification 转向 comprehensive negative-result
  coverage + practical operating guidelines (C0 gate + temperature-overhead tradeoff)。
  关键数值: aggregate_abs_weighted_delta_pp ≈ 1.5pp, n_exp_positive_p_below_010 = 2,
  discordant_sica_winrate ≈ 0.65, c0_scaling_distinct_levels = 2,
  f2_constraint_precision_mean = 0.57, f2_precision_vs_entropy_R2 = 0.008。

imagined_experiments:

  - name: sica_k_ablation_14b
    plan_id: exp-002
    description: "K sensitivity (K=6,8,11,12,16,20) on D012 60 questions, Qwen-14B"
    expected_results:
      K6_sica: 0.750
      K6_sc: 0.733
      K6_gap_pp: 1.7
      K8_sica: 0.750
      K8_sc: 0.750
      K8_gap_pp: 0.0
      K11_sica: 0.750
      K11_sc: 0.750
      K11_gap_pp: 0.0
      K12_sica: 0.733
      K12_sc: 0.750
      K12_gap_pp: -1.7
      K16_sica: 0.717
      K16_sc: 0.733
      K16_gap_pp: -1.7
      K20_sica: 0.717
      K20_sc: 0.733
      K20_gap_pp: -1.7
      tiebreak_rate_K6: 0.183
      tiebreak_rate_K12: 0.267
      tiebreak_rate_K20: 0.050
      all_K_sica_leq_sc: false
      n: 60
    result_rationale: >
      Worst 档下 K=6 出现 +1.7pp 正向 delta。原因：低 K 时每条 trace 权重大，diversity 自然较高，
      SICA 的 constraint filtering 在少样本高 diversity 场景有边际价值。K=11 (odd) gap=0 确认
      tiebreak-only mechanism：去除 exact tie 后 SICA 无额外价值。K≥12 时 SICA 退化：更多 traces
      引入更多 low-quality constraints，noise injection 效应压过任何 signal。整体模式非单调——
      low K 弱正向、odd K 零、high K 弱负向——使 'SICA ≤ SC at all K' 叙述失效，需改为
      'K-dependent with no consistent advantage'。
    tables:
      - "Appendix Table A1: K-ablation results (K × accuracy × gap × tiebreak rate)"
    figures_description:
      - "Appendix Figure: K vs SICA-SC gap line chart，带 error bar (bootstrap 95% CI)。K=6 正向点打破单调递减趋势。"
    analysis: >
      K=6 的 +1.7pp 在 n=60 下 SE≈5pp，统计上无意义 (p>0.5)，但在图上形成一个视觉上的正向点，
      reviewer 可能追问 'why not use K=6?'。应对策略：在 appendix 说明 K=6 下 SC 本身 variance 更大 (fewer votes)，
      +1.7pp 在 bootstrap CI [-5.0, +8.3] 内完全兼容零效应。K=11 (odd) gap=0 是核心证据：
      无 tie 时 SICA 完全等价于 SC，确认 SICA 的全部潜在价值来自 tiebreaking。论文可保留此结论。

  - name: tiebreak_baseline_analysis
    plan_id: exp-003
    description: "SICA vs SC-random-tiebreak vs SC-deterministic on tied questions, CPU reanalysis"
    expected_results:
      n_tied_questions: 5
      sica_tiebreak_accuracy: 0.80
      random_tiebreak_accuracy: 0.50
      alphabetical_tiebreak_accuracy: 0.60
      first_seen_tiebreak_accuracy: 0.40
      tied_question_fraction: 0.083
      n_total_problems: 60
    result_rationale: >
      SICA 在 tied questions 上表现出色 (80% vs random 50%)，证明 constraint-based tiebreaking
      有真实价值。但问题在于 tied questions 极少 (5/60 = 8.3%)：即使 SICA 每次 tie 都选对，
      对总体 accuracy 的贡献仅 ~0.083 × 0.30 ≈ +2.5pp。Worst 档的问题：80% tiebreak quality
      给 reviewer 一个 'method works on ties, just needs more ties' 的反驳切入点，暗示
      在更极端的 diversity 条件（如 T=1.0）下 SICA 可能有更大价值。这与温度 ablation 正向结果
      形成叙事共振，削弱 trap 的 'structural' 性质。
    tables:
      - "T4: Tiebreak Analysis (method × accuracy on tied subset × contribution to overall gap)"
    figures_description: []
    analysis: >
      Tiebreak quality 80% 本身是一个 positive result，论文不能忽略。应策略性地呈现：
      在 T4 中同时展示 'accuracy on ties' (SICA wins) 和 'contribution to total accuracy'
      (negligible)。用 'effective contribution' = tiebreak_quality × tie_rate 量化：
      0.80 × 0.083 = 6.6% effective contribution → translates to ~2pp at best。
      在 worst 档叙事中，这成为 'boundary conditions' 节的辅助论据。

  - name: sica_7b_scaling
    plan_id: exp-004
    description: "Qwen2.5-7B-Instruct on D012 60 questions, within-Qwen scaling"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.600
      sc_accuracy: 0.567
      delta_pp: 3.3
      multi_candidate_rate: 0.65
      extraction_rate: 0.82
      answer_extraction_rate: 0.88
      contradiction_rate: 0.068
      truncated_traces: 30
      discordant_sica_wins: 4
      discordant_sc_wins: 2
      mcnemar_p: 0.41
      proofwriter_sica: 0.567
      proofwriter_sc: 0.533
      proofwriter_delta_pp: 3.3
      folio_sica: 0.633
      folio_sc: 0.600
      folio_delta_pp: 3.3
      c0_level_cluster: high
    result_rationale: >
      7B 模型更弱 → baseline 更低 (SC≈57%) → diversity 更高 (C0=65% vs 14B 的 38%)。
      Higher diversity 给 SICA 更多操作空间，产生 +3.3pp 边际正向 delta。但 p=0.41 完全
      在噪声范围内。Worst 档的核心问题：7B 和 14B 的 C0 都在 {30-68%} 聚类中，无法构成
      'C0 gradient' → c0_scaling_distinct_levels 仍为 2（{<5%} vs {30-68%}）。
      +3.3pp delta 虽不显著，但方向一致地为正，给 reviewer 'underpowered positive' 解读空间。
      Truncation 较高 (30/720 traces) 引入 confound：truncated traces 可能产生 artifact diversity。
    tables:
      - "T1 row: Qwen-7B | PW/FOLIO | 0.600 vs 0.567 | +3.3pp | p=0.41"
    figures_description:
      - "F4 data point: C0=65%, gap=+3.3pp — 在 C0-vs-gap 散点图中形成最右侧正向点"
    analysis: >
      7B 结果在 worst 档中制造叙事摩擦：delta 方向为正，且比 14B (+0.3pp) 更大。
      Reviewer 可能论证 'the method works better on weaker models where diversity is higher'，
      要求 larger-n 验证。防御：(1) n=60 SE≈6pp，+3.3pp 在 CI 内含零；(2) extraction rate
      下降到 82% 意味 constraint quality 更差；(3) 即使真实效应为 +3pp，overhead 约 50%
      使 cost/gain ratio 不合理。但这些论证相比 'trap is structural' 明显更弱。

  - name: qwq_32b_operating_regime
    plan_id: exp-005
    description: "QwQ-32B negative control — data from MVP phase, formatted for paper"
    expected_results:
      qwq_aggregate_c0_nominal_pct: 10.3
      qwq_aggregate_c0_effective_pct: 2.6
      qwen14b_c0_pct: 46.0
      diversity_ratio_effective: 17.7
      aime_delta_pp: 0.0
      proofwriter_delta_pp: -5.9
      aime_n: 22
      proofwriter_n: 17
      temp_diversity_n: 5
      folio_n: 2
      total_problems: 46
      c0_threshold: 20
      qwq_below_threshold: true
      sica_eq_sc_all_domains: true
    result_rationale: >
      QwQ-32B 作为 full reasoning model，deterministic chain 主导 sampling randomness，
      C0 effective 仅 2.6%。SICA ≡ SC 是结构性的——only 1-2 candidate answers per problem，
      MaxSAT exclusion 无 target。这一结果干净地支持 'low C0 → method degenerates' 叙述。
      Worst 档的问题不在结果本身，而在数据量：total n=46 且分布不均 (AIME 22, PW 17,
      temperature 5, FOLIO 2)，统计功效极低。Reviewer 可质疑 'n=46 不足以得出 C0<5%
      是 generalizable 的结论'。
    tables:
      - "T1 row: QwQ-32B | AIME/PW/FOLIO | SICA≡SC | C0=2.6%"
    figures_description:
      - "F4 data point: C0=2.6%, gap=0pp — 左下角 anchor point"
    analysis: >
      QwQ-32B 数据是论文最干净的 negative control，worst 档下仍可正常使用。风险在于
      reviewer 要求 larger-n QwQ 验证或其他 reasoning model (e.g., o1-mini, Gemini 2.5 Flash Thinking)
      → 超出 GPU budget。在 worst 叙事中，QwQ-32B 作为 'converged regime' 示例仍成立，
      但 'operating regime is empirically empty' 的强声明需要更多 reasoning model 数据点。

  - name: c0_diagnostic_validation
    plan_id: exp-006
    description: "C0 vs SICA-SC gap scatter across all models/conditions, CPU analysis"
    expected_results:
      n_data_points: 12
      c0_values_observed: [2.6, 5.0, 10.0, 22.0, 27.0, 38.0, 50.0, 58.0, 62.0, 65.0, 72.0]
      gap_values_observed: [0.0, -1.7, 3.3, 1.7, 3.3, 0.3, 0.0, -3.3, 8.3, 3.3, 8.3]
      linear_R2: 0.08
      linear_slope_pp_per_pct: 0.09
      linear_p_value: 0.37
      distinct_clusters: 2
      cluster_low_c0_range: [0, 10]
      cluster_high_c0_range: [22, 72]
      cluster_low_mean_gap: -0.9
      cluster_high_mean_gap: 1.8
    result_rationale: >
      C0 与 gap 之间无显著线性关系 (R²=0.08, p=0.37)。数据点自然分为两个聚类：
      reasoning models (C0<10%, gap≈0) 和 instruction models (C0=22-72%, gap 散布于 -3.3 到 +8.3pp)。
      无中间 C0 值 (10-22% 区间空白) → C0 仅能做 binary classification (reasoning vs instruction)，
      不是 gradient diagnostic。Worst 档的核心问题：instruction-scale 聚类内部 gap 方差极大
      (从 -3.3 到 +8.3pp)，C0 对 gap 无预测力。'C0 as necessary-but-insufficient diagnostic'
      降级为 'C0 as trivial model-type classifier'。
    tables:
      - "Appendix Table: All (model, domain, C0, gap) data points"
    figures_description:
      - "F4: C0 vs SICA-SC gap scatter plot，两个明显聚类用不同颜色。R²=0.08 回归线几乎水平。注释说明 cluster gap。"
    analysis: >
      F4 在 worst 档下仍可展示，但叙事从 'C0 predicts gap (negative correlation)' 变为
      'C0 discriminates two regimes (low/high) but provides no gradient information'。
      Claim 3 必须弱化：C0 是 'binary indicator' 而非 'diagnostic tool'。
      唯一的挽救空间是加 exp-004 (7B) 和 exp-007 (72B) 数据后 within-Qwen-family C0
      确实单调递减 (65% → 38% → 22%)，但 gap 不单调 → C0 gradient 存在但无预测力。

  - name: sica_72b_awq
    plan_id: exp-007
    description: "Qwen2.5-72B-Instruct AWQ 4-bit on D012 60 questions"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.867
      sc_accuracy: 0.850
      delta_pp: 1.7
      multi_candidate_rate: 0.22
      extraction_rate: 0.91
      answer_extraction_rate: 0.97
      contradiction_rate: 0.015
      truncated_traces: 5
      discordant_sica_wins: 3
      discordant_sc_wins: 2
      mcnemar_p: 0.65
      c0_level_cluster: high
    result_rationale: >
      72B 的 baseline 高 (SC=85%)，diversity 中等 (C0=22%)。C0=22% 刚过 20% threshold 但
      远低于 7B (65%) 和 14B (38%) → 在 Qwen family 内 C0 确实随 scale 递减。
      +1.7pp delta 方向为正但完全在噪声内 (p=0.65)。Worst 档问题：C0=22% 是唯一的
      intermediate C0 值，本应填补 'gradient' 缺口，但 gap 仍不显著 → C0 gradient 存在
      但对 gap 无预测力。72B 的正向 delta 为 reviewer 提供 'scale helps tiebreaking'
      的假设空间。
    tables:
      - "T1 row: Qwen-72B | PW/FOLIO | 0.867 vs 0.850 | +1.7pp | p=0.65"
    figures_description:
      - "F4 data point: C0=22%, gap=+1.7pp — 填充 mid-C0 区域"
    analysis: >
      72B 是 within-Qwen scaling 维度的关键数据点。C0 sequence: 7B=65% → 14B=38% → 72B=22%
      → QwQ-32B=2.6% 形成单调递减，但 gap sequence: +3.3 → +0.3 → +1.7 → 0 不单调。
      这意味 C0 gradient 存在 (c0_scaling_distinct_levels 勉强算 2)，但 gap 与 C0 不共变。
      论文可在 appendix 展示 Qwen-family 4 点的 C0 trend，标注 'monotonic C0 decrease
      with scale, but no corresponding gap trend'。

  - name: constraint_quality_case_studies
    plan_id: exp-008
    description: "Qualitative analysis of 8 representative questions' constraints"
    expected_results:
      n_cases: 8
      semantically_meaningful: 3
      correctly_discriminative: 2
      non_discriminative: 3
      actively_misleading: 2
      constraint_categories:
        tautological: 3
        partial_correct: 2
        fully_correct: 2
        contradiction_with_ground_truth: 1
    result_rationale: >
      8 个 case study 中，3 个的 constraints 语义上有意义且可区分正确/错误答案。
      特别是 FOLIO 形式逻辑问题中，FOL constraints 直接编码推理步骤，部分 constraints
      确实 discriminative。这与 aggregate 统计 (precision=0.57) 一致——constraints 并非
      completely non-discriminative，而是 weakly discriminative。Worst 档问题：qualitative
      evidence 展示 constraints CAN work on individual problems，削弱 'constraints lack
      discriminative power' 的绝对表述。Reviewer 可论证 'the method works, just needs
      better constraint extraction'。
    tables: []
    figures_description:
      - "In-text Box/Figure: 2 个 case study — 一个 constraints 正确区分答案 (positive example)，一个 constraints 为 tautological (negative example)"
    analysis: >
      Case studies 在 worst 档下成为双刃剑：positive examples 展示 method 的理论潜力，
      negative examples 展示当前 extraction 的局限。论文应选择性呈现：main text 放
      一个 positive + 一个 negative (balanced)，appendix 放全部 8 个。叙事调整为
      'constraints are occasionally discriminative but too noisy in aggregate to improve
      over majority voting'。

  - name: overhead_analysis
    plan_id: exp-009
    description: "Wall-time breakdown per question from exp-001 data"
    expected_results:
      n: 804
      mean_total_wall_s: 61.6
      mean_trace_gen_s: 31.6
      trace_gen_pct: 51.3
      mean_extract_s: 29.0
      extract_pct: 47.0
      mean_dedup_s: 1.0
      dedup_pct: 1.6
      mean_maxsat_s: 0.003
      maxsat_pct: 0.005
      sica_overhead_pct: 48.7
      pw_overhead_pct: 51.3
      folio_overhead_pct: 38.6
      p50_overhead_pct: 48.9
      p90_overhead_pct: 57.6
      overhead_gain_ratio: 162.3
    result_rationale: >
      SICA 额外开销约 48.7%（主要来自 constraint extraction LLM call），MaxSAT 解算
      开销可忽略 (<0.01%)。Overhead/gain ratio = 48.7%/0.3pp ≈ 162（每 1pp gain 需
      162% overhead）。Worst 档问题：如果 T=1.0 下 gain=+8.3pp，overhead/gain ratio
      变为 48.7%/8.3pp ≈ 5.9 — 这就 reasonable 了。Reviewer 会指出 'at T=1.0
      the overhead-to-gain ratio is acceptable'，要求 boundary conditions 节量化
      T=1.0 的真实 overhead（extraction rate 下降 → 更多 retry → overhead 可能更高）。
    tables:
      - "Appendix Table: Overhead breakdown (component × mean time × % total)"
    figures_description:
      - "Appendix Figure: stacked bar chart showing time breakdown per component"
    analysis: >
      Overhead analysis 在 worst 档需要扩展：增加 T=1.0 条件下的 overhead 分析。
      预计 T=1.0 时 extraction rate 从 89% 降至 76% → 更多 retry / empty extractions
      → actual overhead 从 48.7% 升至 ~65%。在 boundary conditions 节中呈现：
      'T=1.0 gain of +8.3pp comes with 65% overhead increase, effectively doubling
      compute for a marginal and non-robust improvement'。

  - name: sica_mistral_7b
    plan_id: exp-010
    description: "Mistral-7B-Instruct-v0.3 on D012 60 questions"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.483
      sc_accuracy: 0.483
      delta_pp: 0.0
      multi_candidate_rate: 0.50
      extraction_rate: 0.882
      answer_extraction_rate: 1.0
      contradiction_rate: 0.056
      discordant_sica_wins: 2
      discordant_sc_wins: 2
      mcnemar_p: 1.0
      proofwriter_sica: 0.400
      proofwriter_sc: 0.400
      folio_sica: 0.567
      folio_sc: 0.567
      truncated_traces: 0
    result_rationale: >
      Mistral-7B 产生高 diversity (C0=50%) 但 delta 精确为 0。Discordant pairs 完美
      平衡 (2:2)，McNemar p=1.0。这是 capability trap 的教科书案例：abundance of diversity
      (C0=50%) + zero gain → constraints are non-discriminative on this model。
      Worst 档下 Mistral 结果实际上 HELPS the paper（干净的 negative result），但它
      也暴露了一个问题：为什么 Mistral delta=0 而 LLaMA delta=+8.3pp？两者都是 7B
      instruction models with similar C0 (50% vs 62%)。这个不一致使 'model-agnostic trap'
      叙述受到挑战。
    tables:
      - "T1 row: Mistral-7B | PW/FOLIO | 0.483 vs 0.483 | 0pp | p=1.0"
    figures_description:
      - "F4 data point: C0=50%, gap=0pp"
    analysis: >
      Mistral 和 LLaMA 的对比是 worst 档的 key tension：两个 7B instruction models，
      相似的 C0 (50% vs 62%)，但 delta 完全不同 (0pp vs +8.3pp)。论文必须解释这个差异。
      可能的解释：(1) LLaMA 有 48 truncated traces → artifact diversity; (2) Mistral
      的 constraint quality 恰好平衡 (equal quality for correct and incorrect answers);
      (3) sample variance at n=60。策略：在论文中明确标注 LLaMA 的 truncation confound，
      并用 exp-019/020 的 large-n LLaMA 数据 (Δ=+2.0pp p=0.424 / Δ=-2.4pp p=0.267)
      论证 n=60 的 +8.3pp 是 noise。

  - name: sica_llama_8b
    plan_id: exp-011
    description: "LLaMA-3.1-8B-Instruct on D012 60 questions"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.683
      sc_accuracy: 0.600
      delta_pp: 8.3
      multi_candidate_rate: 0.62
      extraction_rate: 0.83
      answer_extraction_rate: 0.89
      contradiction_rate: 0.055
      truncated_traces: 48
      discordant_sica_wins: 7
      discordant_sc_wins: 2
      mcnemar_p: 0.096
      proofwriter_sica: 0.633
      proofwriter_sc: 0.600
      proofwriter_delta_pp: 3.3
      folio_sica: 0.733
      folio_sc: 0.600
      folio_delta_pp: 13.3
      discordant_sica_winrate: 0.778
    result_rationale: >
      LLaMA-8B 是 worst 档的核心 problematic result。+8.3pp delta 达 McNemar p=0.096
      (< 0.10 threshold)，7:2 discordant ratio 强烈偏向 SICA。FOLIO subset 尤其突出
      (+13.3pp)。但有严重 confound：48/720 traces 被 truncated，truncation 可能
      人为产生 diverse partial answers → SICA 从 truncation-induced diversity 中获益，
      而非从 genuine constraint quality。另一 confound：SC baseline 异常低 (60%)，
      远低于 Qwen-14B (76.2%)，暗示 LLaMA-8B 的 reasoning quality 不稳定，
      高 variance baseline 更容易产生 spurious positive deltas。
      Registry 中 exp-019 (LLaMA StrategyQA n=200 Δ=+2.0pp p=0.424) 和
      exp-020 (LLaMA FOLIO n=204 Δ=-2.4pp p=0.267) 的 large-n 结果均不支持
      positive signal → 强烈暗示 n=60 的 +8.3pp 是 noise。
    tables:
      - "T1 row: LLaMA-8B | PW/FOLIO | 0.683 vs 0.600 | +8.3pp | p=0.096*"
    figures_description:
      - "F4 data point: C0=62%, gap=+8.3pp — 散点图右上角 outlier，需要 annotation"
    analysis: >
      This is THE experiment that forces the worst-tier reframe。防御策略层级：
      (1) Primary: exp-019/020 large-n 结果否定 LLaMA positive signal → n=60 是 noise；
      (2) Secondary: 48 truncated traces confound → 不是 clean comparison；
      (3) Tertiary: Bonferroni correction across 5+ model families → p=0.096 不 survive
      multiple testing correction (threshold ≈ 0.02)。
      但 reviewer 反驳：'even if this specific result is noise, combined with T=1.0
      positive result, there's suggestive evidence that extreme diversity conditions
      can unlock marginal SICA gains'。论文必须在 boundary conditions 节正面回应：
      承认 marginal gains exist at extreme diversity but argue they're dominated by
      overhead and instability。

  - name: gsm8k_pilot_14b
    plan_id: exp-012
    description: "Qwen2.5-14B on GSM8K 30-question pilot (K=12)"
    expected_results:
      n: 30
      k: 12
      sica_accuracy: 0.800
      sc_accuracy: 0.767
      delta_pp: 3.3
      multi_candidate_rate: 0.27
      extraction_rate: 0.85
      answer_extraction_rate: 0.93
      contradiction_rate: 0.033
      discordant_sica_wins: 2
      discordant_sc_wins: 1
      mcnemar_p: 0.56
      c0_interpretation: moderate
    result_rationale: >
      14B 在 GSM8K 上 accuracy ~77-80%（不是预期的 >85%），C0=27% 中等偏高（预期 <20%）。
      原因：K=12 traces 中部分含 arithmetic error 的不同路径，产生 moderate diversity。
      +3.3pp delta 在 n=30 下完全无信息量 (SE≈8pp)，但 C0=27% 本身是有价值的数据点——
      填充 F4 散点图的 mid-C0 区域 (与 72B 的 C0=22% 接近)。Worst 档问题：C0=27%
      不如预期的 <20%，意味 '14B on easy tasks has low C0' 假设未成立，
      weakening 'C0 reflects task difficulty / model confidence' 叙事。
    tables:
      - "Appendix row or T1 extension: Qwen-14B GSM8K | 0.800 vs 0.767 | +3.3pp | p=0.56"
    figures_description:
      - "F4 data point: C0=27%, gap=+3.3pp"
    analysis: >
      GSM8K pilot 在 worst 档下价值有限（n=30 太小），但 C0=27% 是有用的 intermediate 数据点。
      策略：放 appendix，注明 pilot。如果扩展到 200 题，预计 delta 回归到 ~0-1pp。
      不扩展的理由：GSM8K 不是 NLI/logic domain，与论文主要 scope (formal reasoning) 距离较远，
      reviewer 不太会 insist on full GSM8K 实验。

  - name: constraint_ablation
    plan_id: exp-013
    description: "MaxSAT vs count-only vs random-weight on exp-001 data (n=804)"
    expected_results:
      n: 804
      maxsat_accuracy: 0.765
      count_only_accuracy: 0.764
      random_weight_accuracy: 0.763
      sc_baseline_accuracy: 0.762
      maxsat_vs_count_delta_pp: 0.1
      maxsat_vs_random_delta_pp: 0.2
      count_vs_sc_delta_pp: 0.2
      mcnemar_maxsat_vs_count_p: 0.85
      mcnemar_maxsat_vs_random_p: 0.72
      agreement_rate_maxsat_count: 0.998
      n_disagreements: 2
    result_rationale: >
      MaxSAT ≈ count-only ≈ random-weight ≈ SC，四种方法在 804 题中仅 2 题不同。
      这是 capability trap 的最强证据之一：satisfiability reasoning (MaxSAT) 相比
      简单计数 (count-only) 无任何贡献，证明 constraints 的 logical structure 未被利用，
      SAT solver 实质上退化为 constraint counter。Worst 档下这一结果仍然干净地支持论文，
      BUT 如果结合 T=1.0 的 positive result，reviewer 可能要求在 T=1.0 条件下
      重做 ablation → 如果 T=1.0 的 MaxSAT > count-only → 表明 high diversity 下
      constraint satisfiability 变得 informative → 直接推翻 'mechanism is vacuous'。
      论文需要 hedge: 'at default operating conditions (T=0.7), the mechanism is vacuous'.
    tables:
      - "T3: Constraint Ablation (method × accuracy × pairwise McNemar p)"
    figures_description: []
    analysis: >
      T3 在 worst 档下需要加 caveat: 'ablation performed at T=0.7; results may differ
      at extreme temperatures where constraint quality distribution changes'。
      如果不做 T=1.0 ablation → reviewer 会视为 major limitation。如果做了且 MaxSAT >
      count-only at T=1.0 → paper narrative needs fundamental restructuring。
      策略：在 main text 只报 T=0.7 ablation, appendix acknowledge T=1.0 ablation
      as future work。但这在 worst 档 reviewer standards 下可能不够。

  - name: sica_deepseek_r1_llama_8b
    plan_id: exp-014
    description: "DeepSeek-R1-Distill-Qwen-7B on D012 60 questions"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.683
      sc_accuracy: 0.717
      delta_pp: -3.3
      multi_candidate_rate: 0.583
      extraction_rate: 0.839
      answer_extraction_rate: 0.939
      truncated_traces: 72
      contradiction_rate: 0.037
      mcnemar_p: 0.48
      discordant_sica_wins: 0
      discordant_sc_wins: 2
      model_reclassification: instruction_scale
    result_rationale: >
      DeepSeek-R1-Distill-7B 被重新分类为 instruction-scale model：C0=58%（远非预期的 <5%），
      行为完全像 7B instruction model 而非 reasoning model。Distillation 在 7B 容量下
      不足以产生 deterministic reasoning chains。-3.3pp delta 表明 constraints 积极有害
      （SICA 比 SC 差）。72 truncated traces 最多（vs LLaMA 的 48）→ reasoning 风格
      的长 traces 在 context window 内被截断更多。Worst 档下 DeepSeek 结果 helps the paper
      (clear negative) 但 reclassification 创建叙事复杂性：原计划将其作为 'second reasoning model'，
      现在只有 QwQ-32B 一个 reasoning model 数据点。
    tables:
      - "T1 row: DeepSeek-R1-7B | PW/FOLIO | 0.683 vs 0.717 | -3.3pp | instruction-scale"
    figures_description:
      - "F4 data point: C0=58%, gap=-3.3pp — 高 diversity 负 gap，强支撑 trap"
    analysis: >
      DeepSeek reclassification 在 worst 档是 mixed：它增强了 instruction-scale 的 coverage
      (now 4 families) 但削弱了 reasoning model coverage (only QwQ-32B)。
      Reviewer concern: 'you only tested one reasoning model' → mitigate by arguing
      QwQ-32B at C0=2.6% is structurally determined (reasoning models converge by design)
      and DeepSeek-R1's reclassification itself is an insight (distillation ≠ reasoning at 7B)。
      -3.3pp 的负向 delta 是论文 strongest per-experiment negative result，可用于
      'constraints can actively hurt when extraction quality is low' 叙事。

  - name: logic_lm_baseline
    plan_id: exp-015
    description: "Logic-LM × K + majority vote on FOLIO, CPU reanalysis"
    expected_results:
      n_folio: 204
      logic_lm_k_vote_accuracy: 0.809
      sica_accuracy_folio: 0.794
      sc_accuracy_folio: 0.794
      logic_lm_vs_sica_delta_pp: 1.5
      logic_lm_vs_sc_delta_pp: 1.5
      mcnemar_logic_lm_vs_sica_p: 0.38
      single_trace_logic_lm_accuracy: 0.775
      k_used: 12
    result_rationale: >
      Logic-LM (单 trace FOL 验证 repeated K times + vote) 在 FOLIO 上达到 0.809，
      略高于 SICA 的 0.794 和 SC 的 0.794。差异不显著 (p=0.38) 但方向上 Logic-LM > SICA。
      这暗示 multi-trace MAX-SAT aggregation 不仅无益，可能不如 single-trace verification
      重复后投票。原因：Logic-LM 对每条 trace 做完整 FOL consistency check（通过/不通过），
      这比 MAX-SAT 的 soft constraint aggregation 更有 discriminative power——
      一条 trace 如果内部逻辑不一致，Logic-LM 直接排除它，而 SICA 仍将其 constraints
      纳入 aggregation。Worst 档问题：Logic-LM > SICA 意味 'there IS value in FOL
      constraints, but SICA's aggregation destroys it' → reviewer 可论证 'fix the
      aggregation, don't abandon the approach'。
    tables:
      - "Appendix Table: Logic-LM × K vs SICA vs SC on FOLIO"
    figures_description: []
    analysis: >
      Logic-LM comparison 在 worst 档下是 double-edged：(1) confirms FOL extraction itself
      has value → good for paper's relevance; (2) suggests SICA's MAX-SAT aggregation
      is the wrong approach → reviewer may argue for better aggregation rather than
      abandoning symbolic consensus。论文防御：Logic-LM × K 的 1.5pp advantage 不显著，
      且 Logic-LM 的 overhead 更高 (K independent FOL checks vs 1 extraction + 1 MaxSAT)，
      overhead-adjusted performance 可能 comparable。

  - name: weighted_sc_baseline
    plan_id: exp-016
    description: "Weighted SC baselines on exp-001 data (n=804)"
    expected_results:
      n: 804
      sc_uniform_accuracy: 0.762
      inv_length_accuracy: 0.770
      length_weighted_accuracy: 0.753
      constraint_count_accuracy: 0.753
      sica_maxsat_accuracy: 0.765
      inv_length_vs_sc_p: 0.42
      inv_length_vs_sica_p: 0.79
      length_vs_sc_p: 0.16
      all_nonsignificant: true
    result_rationale: >
      Inverse-length weighted SC (偏好短 traces) 达 0.770，略高于 SICA (0.765) 和 SC (0.762)。
      Length-weighted 和 constraint-count weighted 反而更差 (0.753)。所有差异不显著。
      Worst 档解读：一个 zero-cost heuristic (inverse-length weighting) 匹配或微超 SICA
      → SICA 的 constraint extraction + MaxSAT 开销完全多余。但 inv-length 的 advantage
      也不显著 (p=0.42 vs SC) → 实质上所有方法等价。'Simple weighting ≈ SICA ≈ SC'
      强化 'nothing helps' 叙事，但 reviewer 可能 focus on inv-length 的 0.770 →
      'there IS a slightly better method, just not yours'。
    tables:
      - "Appendix Table: Weighted SC variants (method × accuracy × p vs SC)"
    figures_description: []
    analysis: >
      Weighted SC 结果在 worst 档下可用于 'SICA is no better than simple heuristics' 论点。
      但 inv-length 的微弱优势暗示 trace quality selection (短 traces = 更 confident)
      可能是 right direction，而 SICA 的 constraint-based selection 是 wrong direction。
      论文可在 discussion 中 acknowledge 'lightweight quality proxies like trace length
      may be more effective than formal constraint extraction'。

  - name: sica_strategyqa_14b
    plan_id: exp-017
    description: "Qwen2.5-14B on StrategyQA 60 questions (K=12)"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.567
      sc_accuracy: 0.533
      delta_pp: 3.3
      multi_candidate_rate: 0.10
      extraction_rate_problem: 1.0
      extraction_rate_trace: 0.704
      contradiction_detected: 5
      discordant_sica_wins: 2
      discordant_sc_wins: 0
      mcnemar_p: 0.16
      bootstrap_p_delta_le_0: 0.135
    result_rationale: >
      StrategyQA 的 C0=10% 意外地低——binary task (yes/no) 预期 C0 应该高 (30-50%)。
      原因：Qwen-14B 在 commonsense reasoning 上相对 confident，12 traces 中大多数
      agree on same answer。低 C0 使 SICA 退化为近 SC (only 10% problems have multiple
      candidates)。+3.3pp delta 来自极少的 discordant pairs (2:0)，p=0.16 不显著。
      Worst 档问题：(1) C0=10% 打破 'StrategyQA should have high C0' 预期 → domain
      difficulty 与 C0 的关系比预想复杂；(2) +3.3pp 虽不显著但方向一致为正，
      与 LLaMA StrategyQA (exp-019, Δ=+2.0pp) 方向一致 → suggestive cross-model positive
      signal in StrategyQA domain。
    tables:
      - "T1 column: StrategyQA | Qwen-14B | 0.567 vs 0.533 | +3.3pp | p=0.16"
    figures_description:
      - "F3 cell: StrategyQA × Qwen-14B → +3.3pp (colored but n.s.)"
    analysis: >
      StrategyQA 的 low C0 在 worst 档是一个 minor complication。本来预期 'binary task
      → high C0 → test capability trap'，实际 C0=10% → test is underpowered。
      论文处理：在 T1 标注 C0=10% 并解释 '14B commonsense confidence limits diversity'。
      +3.3pp delta 可在 F3 heatmap 中展示但不强调。StrategyQA 作为 'third domain'
      的角色弱化——它更像 ARC 的 low-C0 场景而非预期的 high-C0 场景。

  - name: sica_arc_challenge_14b
    plan_id: exp-018
    description: "Qwen2.5-14B on ARC-Challenge 60 questions (K=12)"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.950
      sc_accuracy: 0.967
      delta_pp: -1.7
      multi_candidate_rate: 0.05
      extraction_rate: 1.0
      contradiction_detected: 3
      discordant_sica_wins: 0
      discordant_sc_wins: 1
      c0_interpretation: near_degenerate
    result_rationale: >
      ARC-Challenge 的 C0=5% 极低——Qwen-14B 在 science reasoning 上 baseline 高 (SC=96.7%)，
      几乎所有题目 unanimous。SICA 退化为 SC，唯一的 discordant pair 是 SC 赢。
      -1.7pp delta 来自 1 个 problem 的 constraint misfire。Worst 档下 ARC 结果干净
      地支持 'low C0 → degeneration' 叙事，但暴露一个问题：C0=5% 意味 ARC-Challenge
      对 14B 太简单，不是 meaningful test bed。Reviewer 可能要求 harder science tasks
      (e.g., GPQA) 或 weaker model on ARC → 超出 budget。
    tables:
      - "T1 column: ARC | Qwen-14B | 0.950 vs 0.967 | -1.7pp"
    figures_description:
      - "F3 cell: ARC × Qwen-14B → -1.7pp (grey, near-degenerate)"
    analysis: >
      ARC 在 worst 档是最弱的 domain data point：C0=5% 使它成为 QwQ-32B 类的
      'degenerate' case 而非真正的 'third domain test'。论文需要在 discussion 中
      acknowledge 'ARC-Challenge may be too easy for 14B models to provide a meaningful
      test of symbolic consensus methods'。如果 ARC 和 StrategyQA 都是 low-C0 (5%, 10%),
      则论文只有 FOLIO + ProofWriter 两个真正的 high-C0 domains → 'three domains'
      claim weakened。

  - name: constraint_quality_correlation
    plan_id: exp-019
    description: "Per-problem constraint precision analysis, CPU (n≈307 multi-candidate problems from exp-001)"
    expected_results:
      n_multi_candidate_problems: 307
      constraint_precision_mean: 0.57
      constraint_precision_std: 0.23
      constraint_precision_median: 0.58
      precision_vs_vote_entropy_R2: 0.008
      precision_vs_vote_entropy_slope: 0.03
      precision_vs_vote_entropy_p: 0.12
      precision_vs_exclusion_rate_R2: 0.003
      precision_vs_exclusion_rate_slope: -0.01
      precision_by_domain_pw: 0.55
      precision_by_domain_folio: 0.62
      precision_above_random_3class: true
      precision_above_random_binary: true
      hero_figure_verdict: failed
    result_rationale: >
      Per-problem constraint precision 平均 0.57 (std 0.23)，显著高于 3-class random (0.33)
      和 binary random (0.50)。这直接与 'constraints lack discriminative power' 叙事矛盾——
      constraints ARE weakly discriminative，精度 57% 意味着接近 6/10 的 constraints
      正确指向 ground truth。但 precision 与 vote_entropy 几乎无关 (R²=0.008, slope=0.03)：
      diversity level 不影响 constraint quality。Hero figure (precision vs entropy scatter)
      是一个 formless cloud，无可读模式。FOLIO precision (0.62) 高于 ProofWriter (0.55)，
      可能因为 FOLIO 的形式逻辑结构更适合 FOL constraint extraction。
      Worst 档核心问题：precision=0.57 > 0.50 → constraints 并非 'non-discriminative'，
      它们是 'weakly discriminative'。Paper claim 必须从 'constraints lack discriminative
      power' 重写为 'constraints have insufficient discriminative power to overcome
      aggregation noise at practical sample sizes'。
    tables:
      - "T2: Constraint Quality (domain × precision mean ± std × n)"
    figures_description:
      - "F2 Plan B: temperature × model response-surface heatmap 替代原 hero figure。原 precision vs entropy scatter 降为 appendix figure with annotation 'R²=0.008, no systematic pattern'"
      - "F2 Appendix: scatter plot of constraint precision vs vote_entropy, n=307, color by domain, annotated with R² and regression line"
    analysis: >
      F2 hero figure 概念失败是 worst 档的 defining moment for paper structure。
      原计划的 scatter plot (C0 vs constraint precision, showing inverse correlation)
      变成 formless cloud。Plan B: response-surface heatmap (temperature × model,
      cell color = SICA-SC gap)，展示 gap landscape 绝大部分 ≈ 0 但 T=1.0 角落有正值。
      这是一个 weaker but still publishable figure，叙事从 'here's why the trap exists'
      变为 'here's where the trap holds and where it breaks down'。
      Precision=0.57 的重新解读需要更长的 analysis 段落：'Constraints are weakly
      discriminative (precision 0.57 vs 0.33 random) but this 7pp advantage over
      chance is insufficient to reliably flip majority vote outcomes. At K=12 with
      C0=38%, only ~3-4 multi-candidate problems per experiment set, and constraints
      correct 57% of the time, the expected number of correct flips is ~2 — comparable
      to noise.'

  - name: temperature_ablation_t03_t05_t10
    plan_id: what_if_01
    description: "T=0.3/0.5/1.0 on Qwen-14B D012 60题, diversity-gap relationship"
    expected_results:
      t03_n: 60
      t03_c0: 0.18
      t03_sica_accuracy: 0.750
      t03_sc_accuracy: 0.733
      t03_delta_pp: 1.7
      t03_extraction_rate: 0.93
      t03_mcnemar_p: 0.65
      t03_discordant_sica: 2
      t03_discordant_sc: 1
      t05_n: 60
      t05_c0: 0.30
      t05_sica_accuracy: 0.750
      t05_sc_accuracy: 0.733
      t05_delta_pp: 1.7
      t05_extraction_rate: 0.91
      t05_mcnemar_p: 0.55
      t05_discordant_sica: 3
      t05_discordant_sc: 2
      t10_n: 60
      t10_c0: 0.72
      t10_sica_accuracy: 0.817
      t10_sc_accuracy: 0.733
      t10_delta_pp: 8.3
      t10_extraction_rate: 0.76
      t10_answer_coherence_rate: 0.85
      t10_mcnemar_p: 0.034
      t10_discordant_sica: 7
      t10_discordant_sc: 1
      t10_discordant_sica_winrate: 0.875
      temp_max_abs_delta_pp: 8.3
      c0_vs_temp_correlation: 0.98
      gap_vs_temp_monotonic: true
    result_rationale: >
      Temperature ablation 是 worst 档的 defining experiment。T 与 C0 高度相关 (r=0.98)：
      T=0.3→C0=18%, T=0.5→C0=30%, T=0.7→C0=38% (baseline), T=1.0→C0=72%。
      关键发现：T=1.0 下 SICA 显著优于 SC (+8.3pp, p=0.034)，7:1 discordant ratio。
      这打破 'regardless of diversity' 声明——在极端 diversity 下 SICA 确实有优势。
      但伴随成本：extraction rate 从 89% (T=0.7) 降至 76% (T=1.0)，answer coherence
      从 ~98% 降至 85%。15% incoherent outputs 意味实际 usable diversity 低于 C0 暗示的。
      T=0.3 和 T=0.5 的 delta 为 +1.7pp，均不显著 (p>0.5)，与 T=0.7 的 +0.3pp
      (exp-001 n=804) 方向一致但大小不同（n=60 variance）。
      Gap vs temperature 单调递增暗示 'more diversity → more SICA gain'，直接否定
      capability trap 作为 structural mechanism：trap 在 default T=0.7 下成立，
      但在 T=1.0 下 partially broken → trap 不是 structural，只是 default operating
      condition 的产物。
    tables:
      - "Table (boundary conditions section): Temperature × C0 × SICA × SC × Δ × p × extraction rate"
    figures_description:
      - "F2 Plan B (response-surface heatmap): X=temperature [0.3,0.5,0.7,1.0], Y=model [Qwen-7B,14B,72B,QwQ], cell color=SICA-SC gap。绝大部分 cells ≈ 0 (blue/white), T=1.0 × instruction models 角落有 +5-8pp 正值 (warm color)。在 heatmap 旁加 extraction rate overlay (contour lines) 展示 extraction 在高 T 区域退化。"
      - "Appendix Figure: T vs delta line chart with extraction rate secondary axis, 展示 gain-overhead tradeoff"
    analysis: >
      Temperature ablation 的 T=1.0 positive result (p=0.034) 是 worst 档的最大叙事挑战。
      论文必须加 'boundary conditions' 节正面回应：
      (1) T=1.0 的 +8.3pp 伴随 extraction rate 从 89% 降至 76% → 约 24% 的 traces
      产生 empty/corrupt constraints → MaxSAT input quality 退化；
      (2) Answer coherence 从 ~98% 降至 85% → 15% 的 outputs 本身质量低 → 这些 outputs
      的 constraints 是 noise；
      (3) 如果将 overhead 折入：T=0.7 overhead ≈ 49%，T=1.0 overhead ≈ 65%
      (因 extraction retry) → effective cost per question 增加 ~30%；
      (4) 结论：'T=1.0 partially breaks the trap but at a cost that negates the gain.
      The marginal +8.3pp requires 65% additional compute, operating in a regime where
      15% of outputs are incoherent. Practitioners seeking this marginal gain would be
      better served by simply increasing K at T=0.7.'
      
      这一 framing 将 T=1.0 positive result 转化为 'the trap has a theoretical escape
      hatch that is practically useless'。但 reviewer 可反驳：'(1) overhead analysis
      is not done at T=1.0, you're speculating; (2) incoherence at T=1.0 is model-specific
      and may not apply to larger models; (3) p=0.034 < 0.05, this is a real effect.'

  - name: gsm8k_pilot_30q
    plan_id: what_if_02
    description: "Qwen-14B GSM8K 30-question pilot, math reasoning domain"
    expected_results:
      n: 30
      k: 12
      sica_accuracy: 0.800
      sc_accuracy: 0.767
      delta_pp: 3.3
      multi_candidate_rate: 0.23
      extraction_rate: 0.85
      answer_extraction_rate: 0.93
      contradiction_rate: 0.033
      discordant_sica_wins: 2
      discordant_sc_wins: 1
      mcnemar_p: 0.56
    result_rationale: >
      与 exp-012 相同实验。C0=23% 中等——14B 在 GSM8K 上不完全 confident，部分 arithmetic
      步骤产生不同答案。+3.3pp 在 n=30 下无信息量。此实验在 worst 档下价值在于
      提供一个 math domain 数据点 (与 NLI/science domains 互补)，但 n=30 太小无法
      影响任何 claim。如不扩展到 200+ 题，GSM8K 只能放 appendix 且不计入 main claims。
    tables:
      - "Appendix: GSM8K pilot results (same as exp-012)"
    figures_description:
      - "F4 data point: C0=23%, gap=+3.3pp (small marker, annotated 'pilot n=30')"
    analysis: >
      GSM8K pilot 在 worst 档下是 'nice to have' 但不改变任何 narrative。C0=23%
      填充 F4 mid-range 但 n=30 误差带太宽。不建议投入 GPU budget 扩展，除非 reviewer
      explicit 要求 math domain coverage。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "12c9dae0-b910-42a3-8a9b-0fe9b28673c1",
  "isSidechain": false,
  "requestId": "req_011Cb8MnGuKYxnB1BC18JimQ",
  "type": "assistant",
  "uuid": "ccdc17c0-ba27-4ce4-a07e-3ab32b3d3473",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01116SJ44oSeT626KWyiCaiP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10284,
      "cache_read_input_tokens": 33599,
      "output_tokens": 34677,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10284,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 34677,
          "cache_read_input_tokens": 33599,
          "cache_creation_input_tokens": 10284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10284
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Temperature ablation 暴露 high-diversity 下边际 SICA 收益, 或 F2 per-problem 完全无模式 → 'capability trap' 作为 mechanism claim 证据不足; 需 reframe 为 empirical survey 核心假设：…",
  "leafUuid": "ccdc17c0-ba27-4ce4-a07e-3ab32b3d3473",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Symbolic consensus capability trap empirical study",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Temperature ablation 暴露 high-diversity 下边际 SICA 收益, 或 F2 per-problem 完全无模式 → 'capability trap' 作为 mechanism claim 证据不足; 需 reframe 为 empirical survey 核心假设：…",
  "leafUuid": "ccdc17c0-ba27-4ce4-a07e-3ab32b3d3473",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Symbolic consensus capability trap empirical study",
  "sessionId": "517f0813-4684-4ada-9eba-b76e226870d5"
}
```

---
