# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：核心 negative result (SICA ≈ SC) 稳固, 但 mechanism evidence 有噪声; F2 需 binned 可

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/ecf2953d-324d-49a6-8fc1-127e33d095cd.jsonl`
- **Structured JSON:** [`9f8f2dbefa9b654b1992.json`](../../sessions/9f/9f8f2dbefa9b654b1992.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T15:08:21.447Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T15:08:21.447Z",
  "sessionId": "ecf2953d-324d-49a6-8fc1-127e33d095cd",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：核心 negative result (SICA ≈ SC) 稳固, 但 mechanism evidence 有噪声; F2 需 binned 可视化; C0 仅二值非梯度; claims 措辞需软化\n核心假设：['Temperature ablation: C0 大致随 T 增加但某 T 条件出现 |Δ| = 4-6pp (p > 0.15, n=60 功效不足以排除噪声)', 'F2 per-problem: constraint precision 均值 0.52-0.56 (略高于随机), 与 entropy 有弱正相关 → raw scatter 嘈杂, 需 binned box-plot + CI band 才可读', \"Scaling 仅得 2 个 C0 cluster (instruction-scale ~40-60% vs reasoning <5%), 无中间态 → Claim 3 降级 'binary early-stopping gate'\", '零个实验 p < 0.10, 但 1-2 个方向性噪声点 (Δ 可达 +5pp on n=60)', 'exp-013 ablation 仍为主要 mechanism evidence, F2 降为辅助角色']\n关键指标范围：{'temp_max_abs_delta_pp': [3.0, 6.0], 'f2_constraint_precision_mean': [0.52, 0.57], 'f2_precision_vs_entropy_slope': [0.01, 0.05], 'aggregate_abs_weighted_delta_pp': [0.5, 1.5], 'n_exp_positive_p_below_010': 0, 'c0_scaling_distinct_levels': [2, 2], 'discordant_sica_winrate': [0.45, 0.6]}\n叙事方向：Claim 1 从 'structural trap' 软化为 'empirically pervasive limitation across tested conditions and scales'。Claim 3 从 'diagnostic predictor' 降为 'binary early-stopping gate (C0 < 5% → skip)'。F2 改 binned box-plot + 95% CI band, 正文承认 per-problem noise 但强调 aggregate consistency。Temperature ablation 入正文但 hedge: 'across the tested temperature range (0.3–1.0)'。用 5 models × 3 domains 广度弥补 mechanism 深度不足。仍可行 EMNLP submission, contribution 第三条 (C0 diagnostic) 弱化为半页讨论而非独立 claim。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\nfocus: 验证更新后的 capability trap framing: 机制从\"diversity-quality inverse correlation\"精确化为\"constraints lack discriminative power regardless of diversity level\"。新增 DeepSeek-R1-Distill-7B 作为第四个 instruction-scale 模型。F2 hero figure 现有 per-problem 数据 (n=307, vote_entropy vs exclusion_rate)。\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)\n\n1. **The Capability Trap**: Symbolic consensus methods face a fundamental tension: they require output diversity (C0>20%) to differ from voting, but extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to a noise injector. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B).\n2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.\n3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.\n\n## Core Insight\nSymbolic constraint consensus doesn't improve LLM reasoning because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these constraints lack the discriminative power to distinguish correct from incorrect answers. MAX-SAT optimization over non-discriminative constraints degenerates to noise injection, performing no better (often worse) than simple majority voting. We provide the first systematic empirical study characterizing this trap across 3 reasoning domains, 4 instruction-scale model families, and 1 full reasoning model.\n\n## Story Spine\n- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?\n- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.\n- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.\n- **Headline result**: \"Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis\n3. **\"Only Qwen models\"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B\n4. **\"Only one reasoning model\"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)\n5. **\"Only logic domain\"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.\n6. **\"MAX-SAT is over-engineering\"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.\n7. **\"Random tiebreak baseline\"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.\n8. **\"Why not just use a reasoning model?\"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.\n9. **\"How does this compare to Logic-LM / LINC?\"** → exp-015: Logic-LM × K baseline (CPU-only)\n10. **\"Weighted SC is simpler\"** → exp-016: Weighted SC baseline (CPU-only)\n11. **\"C0 is trivially derived\"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.\n12. **\"Within-family scaling?\"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.\n\n## Working Title\n**\"The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning\"**\n(Alternatives: \n- \"When Does Symbolic Consensus Help? An Empirical Answer: Rarely, and Here's Why\"\n- \"Diversity Without Quality: The Fundamental Limitation of Constraint-Based LLM Aggregation\")\n\n## Paper Structure (EMNLP 8pp + appendix)\n- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Capability Trap: C0 × Constraint Quality inverse correlation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Tiebreak Analysis: quality on tied questions only)\n- Main Figures: F1 (Method Pipeline), F2 (Capability Trap Scatter: C0 vs Constraint Precision, colored by domain, hero figure), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: flat line, contrasting with theoretical upper bound)\n- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data\n\n## Claim Risk Notes (Updated D035 + exp-014)\n- **Claim 1 mechanism refinement**: \"Inverse correlation between diversity and quality\" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: \"constraints lack discriminative power regardless of diversity level.\" Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.\n- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.\n- **Claim 3 gradient risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to \"binary indicator\". Need exp-004/007 for gradient data. OPEN.\n- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.\n- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.\n\n## Venue Fit Risks\n- EMNLP: Negative-results/analysis paper. Must answer \"so what should practitioners do?\" → C0 as deployment diagnostic + overhead analysis.\n- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.\n- Statistical power: Now strong (N>1,200 combined across powered tests).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes\n    odd K=11 to test if SICA value persists without exact ties. Key questions: does\n    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency\n    change with K?'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如\n    gap>0 → SICA has value beyond tiebreaking。\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Within-Qwen scaling dimension.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX\n    PRO 6000 单卡可放。\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。\n- id: exp-010\n  name: sica_mistral_7b\n  claim:\n  - 2\n  - 3\n  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family\n    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''\n    attack.'\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: DONE\n  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+\n    题（~3h GPU，margin 允许）。'\n  registry_id: exp-010-mistral-v3\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- id: exp-011\n  name: sica_llama_8b\n  claim:\n  - 2\n  - 3\n  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.\n    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation\n    同 exp-010。\n- id: exp-012\n  name: gsm8k_pilot_14b\n  claim:\n  - 2\n  - 3\n  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:\n    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer\n    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain\n    win.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable\n    insight.\n- id: exp-013\n  name: constraint_ablation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count\n    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:\n    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability\n    trap.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability\n    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'\n- id: exp-014\n  name: sica_deepseek_r1_llama_8b\n  claim:\n  - 2\n  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning\n    model data point with LLaMA base architecture: validates C0<5% generalizes beyond\n    QwQ-32B AND eliminates ''still Qwen family'' attack.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。\n- id: exp-015\n  name: logic_lm_baseline\n  claim:\n  - 1\n  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style\n    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT\n    multi-trace aggregation adds value beyond FOL extraction itself.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL\n    constraints 做单 trace verification then vote。'\n- id: exp-016\n  name: weighted_sc_baseline\n  claim:\n  - 1\n  - 3\n  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes\n    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.\n    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),\n    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count\n    weighted (no SAT)。'\n- id: exp-017\n  name: sica_strategyqa_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning\n    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected\n    constraint quality. Tests capability trap in best-case-diversity scenario.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability\n    trap（diversity high but quality low → no gain）。\n- id: exp-018\n  name: sica_arc_challenge_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,\n    4-choice format. Tests constraint mechanism in multi-choice scenario + different\n    domain.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)\n    + StrategyQA (binary) 形成答案格式多样性。\n- id: exp-019\n  name: constraint_quality_correlation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only analysis: compute constraint precision per domain × model,\n    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality\n    correlation. Uses data from exp-001/010/011/017/018.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-017\n  - exp-018\n  status: planned\n  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent\n    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have\n    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K6_sica: 0.733\n    K6_sc: 0.733\n    K6_gap_pp: 0\n    K8_sica: 0.733\n    K8_sc: 0.75\n    K8_gap_pp: -1.7\n    K11_sica: 0.733\n    K11_sc: 0.733\n    K11_gap_pp: 0\n    K12_sica: 0.7\n    K12_sc: 0.75\n    K12_gap_pp: -5\n    K16_sica: 0.717\n    K16_sc: 0.75\n    K16_gap_pp: -3.3\n    K20_sica: 0.7\n    K20_sc: 0.733\n    K20_gap_pp: -3.3\n    all_K_sica_leq_sc: true\n    larger_K_degrades_sica: true\n- exp_id: sica_constraint_ablation_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    maxsat_accuracy: 0.7649\n    count_only_accuracy: 0.7662\n    random_weight_accuracy: 0.7637\n    sc_baseline_accuracy: 0.7624\n    n_problems: 804\n    agreement_802_of_804: true\n    mcnemar_p_all_gt_0.7: true\n    note: approximate (raw z3 formulas unavailable, count-only/random-weight use proxy)\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwq_aggregate_c0_nominal_pct: 10.3\n    qwq_aggregate_c0_effective_pct: 2.6\n    qwen14b_c0_pct: 46\n    diversity_ratio_effective: 17.7\n    aime_delta_pp: 0\n    proofwriter_delta_pp: -5.9\n    aime_n: 22\n    proofwriter_n: 17\n    temp_diversity_n: 5\n    folio_n: 2\n    total_problems: 46\n    c0_threshold: 20\n    qwq_below_threshold: true\n- exp_id: exp-011-llama8b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-016-weighted-sc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7649\n    sc_uniform_accuracy: 0.7624\n    inv_length_accuracy: 0.7674\n    length_weighted_accuracy: 0.7525\n    constraint_count_accuracy: 0.7525\n    inv_length_vs_sc_p: 0.453\n    length_vs_sc_p: 0.153\n    inv_length_vs_sica_p: 0.864\n    length_vs_sica_p: 0.066\n    n_problems: 804\n    all_nonsignificant: true\n- exp_id: exp-010-mistral\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-011-llama8b-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-018-arc\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.5667\n    sc_accuracy: 0.5333\n    delta_pp: 3.33\n    mcnemar_chi2: 0.5\n    mcnemar_p: n.s.\n    bootstrap_ci_95:\n    - 0\n    - 8.33\n    bootstrap_p_delta_le_0: 0.1346\n    multi_candidate_rate: 0.1\n    contradiction_detected: 5\n    extraction_rate_problem: 1\n    extraction_rate_trace: 0.704\n    discordant_sica_wins: 2\n    discordant_sc_wins: 0\n- exp_id: pilot-constraint-filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 43\n    thresholds_tested:\n    - 1\n    - 2\n    - 3\n    - 5\n    - 7\n    best_gap_pp: 2.33\n    best_T: 1\n    sica_T1: 0.7674\n    sc: 0.7442\n    T5_gap: 0\n    T7_gap: 0\n    discriminative_ratio_count: 0.115\n    discriminative_ratio_weight: 0.372\n    effective_flip_rate: 0.174\n    multi_answer_problems: 23\n    unanimous_problems: 20\n    problems_disc_favors_different: 4\n- exp_id: exp-018-arc-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.95\n    sc_accuracy: 0.9667\n    delta_pp: -1.67\n    multi_candidate_rate: 0.05\n    extraction_rate: 1\n    contradiction_detected: 3\n    discordant_sica_wins: 0\n    discordant_sc_wins: 1\n    dataset: ARC-Challenge\n    model: Qwen2.5-14B-Instruct\n- exp_id: exp-011-llama8b-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6667\n    sc_accuracy: 0.6\n    delta_pp: 6.67\n    multi_candidate_rate: 0.6167\n    extraction_rate: 0.8556\n    answer_extraction_rate: 0.8958\n    contradiction_rate: 0.0527\n    problems_with_contradictions: 43\n    truncated_traces: 44\n    discordant_sica_wins: 5\n    discordant_sc_wins: 1\n    mcnemar_p: 0.2188\n    proofwriter_sica: 0.6333\n    proofwriter_sc: 0.6\n    proofwriter_delta_pp: 3.33\n    folio_sica: 0.7\n    folio_sc: 0.6\n    folio_delta_pp: 10\n    model: LLaMA-3.1-8B-Instruct\n    dataset: D012\n    wall_time_min: 66.4\n- exp_id: pilot-contrastive-prompt\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- exp_id: exp-019-llama8b-strategyqa-200\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    k: 12\n    sica_accuracy: 0.74\n    sc_accuracy: 0.72\n    delta_pp: 2\n    multi_candidate_rate: 0.41\n    mcnemar_p: 0.424\n    bootstrap_ci_95:\n    - -1.5\n    - 5.5\n    bootstrap_p_delta_le_0: 0.12\n    discordant_sica_wins: 9\n    discordant_sc_wins: 5\n    discordant_total: 14\n    discordant_rate: 0.07\n    sc_unanimous_rate: 0.545\n    model: LLaMA-3.1-8B-Instruct\n    dataset: StrategyQA\n    wall_time_min: 52\n- exp_id: exp-020-llama8b-folio-204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.608\n    sc_accuracy: 0.632\n    delta_pp: -2.45\n    mcnemar_p: 0.2668\n    bootstrap_ci_95:\n    - -5.88\n    - 0.98\n    bootstrap_p_sica_ge_sc: 0.1\n    discordant_sica_wins: 4\n    discordant_sc_wins: 9\n    discordant_total: 13\n    discordant_rate: 0.064\n    multi_candidate_rate: 0.618\n    extraction_rate: 0.942\n    answer_extraction_rate: 0.951\n    contradiction_rate: 0.062\n    both_wrong: 71\n    model: LLaMA-3.1-8B-Instruct\n    dataset: FOLIO-204\n    wall_time_min: 131.7\n- exp_id: exp-009-overhead-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 804\n    mean_total_wall_s: 61.6\n    mean_trace_gen_s: 31.6\n    trace_gen_pct: 51.3\n    mean_extract_s: 29\n    extract_pct: 47\n    mean_dedup_s: 1\n    dedup_pct: 1.6\n    mean_maxsat_s: 0.003\n    maxsat_pct: 0.005\n    sica_overhead_s: 30\n    sica_overhead_pct: 48.7\n    pw_overhead_pct: 51.3\n    folio_overhead_pct: 38.6\n    p50_overhead_pct: 48.9\n    p90_overhead_pct: 57.6\n- exp_id: exp-014-deepseek-r1-7b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6833\n    sc_accuracy: 0.7167\n    delta_pp: -3.33\n    multi_candidate_rate: 0.583\n    extraction_rate: 0.839\n    answer_extraction_rate: 0.939\n    truncated_traces: 72\n    contradiction_rate: 0.037\n    wall_time_min: 100.3\n    mcnemar_p: 0.4795\n    discordant_sica_wins: 0\n    discordant_sc_wins: 2\n    model: DeepSeek-R1-Distill-Qwen-7B\n    dataset: D012\n- exp_id: temperature-ablation-t03\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: temperature-ablation-t05\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: temperature-ablation-t10\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: temperature_ablation_t03_t05_t10\n  claim: Claim 1 (Capability Trap)\n  description: T=0.3/0.5/1.0 on Qwen-14B D012 60题。预期 T↑→C0↑ 但 gap 不变，证明 diversity\n    增加不改善 SICA。\n  estimated_gpu_hours: 3.0\n- name: gsm8k_pilot_30q\n  claim: Claim 2 (Operating Regime Empty)\n  description: Qwen-14B GSM8K 30题 pilot。数学推理域覆盖。预期 C0 低（14B 在 GSM8K 上 accuracy>80%）。\n  estimated_gpu_hours: 1.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T15:08:21.450Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T15:08:21.450Z",
  "sessionId": "ecf2953d-324d-49a6-8fc1-127e33d095cd"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-17T15:08:21.496Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：核心 negative result (SICA ≈ SC) 稳固, 但 mechanism evidence 有噪声; F2 需 binned 可视化; C0 仅二值非梯度; claims 措辞需软化
核心假设：['Temperature ablation: C0 大致随 T 增加但某 T 条件出现 |Δ| = 4-6pp (p > 0.15, n=60 功效不足以排除噪声)', 'F2 per-problem: constraint precision 均值 0.52-0.56 (略高于随机), 与 entropy 有弱正相关 → raw scatter 嘈杂, 需 binned box-plot + CI band 才可读', "Scaling 仅得 2 个 C0 cluster (instruction-scale ~40-60% vs reasoning <5%), 无中间态 → Claim 3 降级 'binary early-stopping gate'", '零个实验 p < 0.10, 但 1-2 个方向性噪声点 (Δ 可达 +5pp on n=60)', 'exp-013 ablation 仍为主要 mechanism evidence, F2 降为辅助角色']
关键指标范围：{'temp_max_abs_delta_pp': [3.0, 6.0], 'f2_constraint_precision_mean': [0.52, 0.57], 'f2_precision_vs_entropy_slope': [0.01, 0.05], 'aggregate_abs_weighted_delta_pp': [0.5, 1.5], 'n_exp_positive_p_below_010': 0, 'c0_scaling_distinct_levels': [2, 2], 'discordant_sica_winrate': [0.45, 0.6]}
叙事方向：Claim 1 从 'structural trap' 软化为 'empirically pervasive limitation across tested conditions and scales'。Claim 3 从 'diagnostic predictor' 降为 'binary early-stopping gate (C0 < 5% → skip)'。F2 改 binned box-plot + 95% CI band, 正文承认 per-problem noise 但强调 aggregate consistency。Temperature ablation 入正文但 hedge: 'across the tested temperature range (0.3–1.0)'。用 5 models × 3 domains 广度弥补 mechanism 深度不足。仍可行 EMNLP submission, contribution 第三条 (C0 diagnostic) 弱化为半页讨论而非独立 claim。

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
  "promptId": "270c166d-98d4-4ab9-b280-641fa2821d1c",
  "type": "user",
  "uuid": "ea0e692c-4de8-4ad4-af80-aa85ca730ed5",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ecf2953d-324d-49a6-8fc1-127e33d095cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T15:08:21.486Z_

```json
{
  "parentUuid": "ea0e692c-4de8-4ad4-af80-aa85ca730ed5",
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
  "uuid": "639724de-c195-46d4-90e3-3584f22d0054",
  "timestamp": "2026-05-17T15:08:21.486Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ecf2953d-324d-49a6-8fc1-127e33d095cd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T15:08:21.486Z_

```json
{
  "parentUuid": "639724de-c195-46d4-90e3-3584f22d0054",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "20a96440-ac3c-432e-b641-2f645e34f8e7",
  "timestamp": "2026-05-17T15:08:21.486Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ecf2953d-324d-49a6-8fc1-127e33d095cd",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 negative result (SICA ≈ SC) 稳固, 但 mechanism evidence 有噪声; F2 需 binned 可视化; C0 仅二值非梯度; claims 措辞需软化 核心假设：['Temperature ablation: C0 大致随 T 增加但某 T 条件出现 |…",
  "leafUuid": "20a96440-ac3c-432e-b641-2f645e34f8e7",
  "sessionId": "ecf2953d-324d-49a6-8fc1-127e33d095cd"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier capability trap characterization with binned F2 analysis",
  "sessionId": "ecf2953d-324d-49a6-8fc1-127e33d095cd"
}
```

---

### Assistant

_source line 8 · 2026-05-17T15:09:25.801Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, based on the "median" tier definition provided. I need to provide result_rationale for each prediction explaining why this result would occur in the median tier.

Let me go through each planned experiment and generate predictions consistent with the median tier characteristics:

**Median tier key characteristics:**
- Core negative result (SICA ≈ SC) is solid
- Mechanism evidence has noise
- F2 needs binned visualization
- C0 is only binary, not gradient
- Claims need softened wording


- Temperature ablation shows noisy C0 increases across conditions with some gaps reaching 4-6 percentage points (insufficient power at n=60)
- F2 per-problem analysis reveals constraint precision clustering around 0.52-0.56 with weak positive entropy correlation
- Scaling experiments display only two distinct C0 clusters rather than a gradient, separating instruction-following (40-60%) from reasoning tasks (<5%)
- Zero-shot experiments achieve p-values below 0.10 but contain 1-2 directional noise points with deltas up to 5 percentage points at n=60
- exp-013 ablation remains the primary mechanism evidence while F2 gets relegated to supporting role

Now I'm working through the specific predictions for each experiment: some entries like sica_k_sensitivity_14b already exist in the registry as completed, but the experiment plan lists them as planned status. I need to identify which ones are actually pending—exp-004 on 7B scaling and exp-005 with QwQ-32B look like the genuine planned experiments, while others like the tiebreak baseline appear to have been completed as CPU analysis already. I'm noticing some inconsistencies in the experiment registry that need sorting out. Exp-019 shows "constraint_quality_correlation" in the plan but the registry entry is actually a different experiment on LLaMA-8B with StrategyQA. Similarly, exp-014 was supposed to use LLaMA-8B but the registry shows it ran with DeepSeek-R1-Distill-Qwen-7B instead, which is a different model entirely.

Now looking at the what_if experiments, I see temperature_ablation is currently running across multiple temperature settings, and there's also gsm8k_pilot_30q to account for. The user is asking me to generate detailed predictions for all planned experiments, so I need to create median-tier predicted data for each one regardless of whether registry entries already exist—the actual results show what happened, but I should generate what the median tier prediction would look like for completeness. I've identified all the planned experiments from the list, and now I'm working through the median tier predictions by establishing the expected ranges for key metrics like temperature deltas, constraint precision, and the relationship between precision and entropy.

Now I'm examining the K ablation experiment in detail—testing how SICA performs against SC across different constraint counts from 6 to 20 on a 60-question set. The critical finding is that at odd K values like 11, the gap closes to zero, which suggests the mechanism relies on tie-breaking rather than genuine performance differences, and larger K values introduce more noise that slightly favors SC.

For the tiebreak baseline, SICA achieves around 75-80% quality as a tiebreaker compared to random's 50% and alphabetical's 55-60%, but ties occur too infrequently to meaningfully impact overall results. The 7B scaling experiment shows Qwen's smaller model has higher C0 rates (55-65%) with lower baseline accuracy, yet the SICA-SC gap remains near zero, and the data splits into two distinct clusters around instruction versus reasoning tasks. Finally, QwQ-32B essentially shows near-zero diversity with C0 under 5%, making SICA and SC functionally equivalent.

Now I'm looking at the diagnostic validation through CPU analysis, which reveals only two clusters—instruction tasks hovering around 40-60% C0 with negligible gaps, and reasoning tasks below 5% C0—with no gradient pattern between them. The 72B AWQ model shows lower C0 rates (25-35%) than the 14B baseline but still falls within the instruction cluster range. Examining case studies qualitatively, the constraints are syntactically correct but semantically fail to discriminate meaningfully. The overhead analysis confirms roughly 49% computational cost from constraint extraction and solving with zero performance gain. Finally, LLaMA 8B shows C0 around 50%.

Looking at the remaining experiments, the 8B model's C0 sits at 50-65% with a small gap increase of 2-5 percentage points, though this appears to be noise given the small sample size. GSM8K performs poorly because the 14B model is already strong on that benchmark, making SICA and SC essentially equivalent. The constraint ablation is revealing—MaxSAT, count-only, and random-weight approaches all cluster within 0.5 percentage points of each other, suggesting the underlying mechanism is vacuous. Logic-LM with K iterations matches SC performance, indicating that FOL extraction alone provides no benefit. The weighted SC experiment is still being analyzed. ighting schemes ≈ SC, none significant

**exp-017 (StrategyQA)**
- Median: C0 moderate (~10-20% due to binary answers), SICA ≈ SC. Gap +1-3pp n.s.

**exp-018 (ARC-Challenge)**
- Median: C0 low (~5-15% because 14B is strong on ARC), SICA ≈ SC. Gap ~-1 to +1pp.

**exp-019 (constraint quality correlation)**
- CPU analysis. Median: constraint precision ~0.52-0.56 across domains, weak positive correlation with entropy (slope 0.01-0.05), noisy per-problem scatter

**Temperature ablation (what-if)**
- T=0.3/0.5/1.0: C0 increases with T but the variance is noisy around 4-6pp at certain temperatures. The overall trend shows diversity growing while the gap remains flat.

**GSM8K pilot (what-if)**
- Mirrors the pattern from exp-012.

Now I'm ready to write out the full YAML output with all the experiment details.

Generating YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20a96440-ac3c-432e-b641-2f645e34f8e7",
  "isSidechain": false,
  "requestId": "req_011Cb8MLE9eHgAHfeLgWx4WS",
  "type": "assistant",
  "uuid": "690fc69b-ee77-48aa-b46b-5400493750e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ecf2953d-324d-49a6-8fc1-127e33d095cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xwGj4QTX5UcA19hpHEBvY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18738,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18738,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15191,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18738
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

_source line 9 · 2026-05-17T15:13:09.732Z_

```yaml
tier: median
narrative_guidance: >
  Claim 1 从 'structural trap' 软化为 'empirically pervasive limitation across tested conditions and scales'。
  Claim 3 从 'diagnostic predictor' 降为 'binary early-stopping gate (C0 < 5% → skip)'。
  F2 改 binned box-plot + 95% CI band，正文承认 per-problem noise 但强调 aggregate consistency。
  Temperature ablation 入正文但 hedge: 'across the tested temperature range (0.3–1.0)'。
  用 5 models × 3 domains 广度弥补 mechanism 深度不足。C0 diagnostic 弱化为半页讨论而非独立 claim。
  零个实验 p < 0.10；1-2 个方向性噪声点 Δ 可达 +5pp (n=60)。exp-013 ablation 仍为主要 mechanism evidence。

imagined_experiments:

  # ── exp-002: K ablation ──────────────────────────────────────────────
  - name: sica_k_ablation_14b
    plan_id: exp-002
    description: >
      Qwen2.5-14B K=6,8,11,12,16,20 on D012 60 questions。
      核心问题：SICA 是否仅在 even-K tie 时有价值？K=11 (odd) 是关键测试。
    expected_results:
      K6_sica_accuracy: 0.733
      K6_sc_accuracy: 0.733
      K6_delta_pp: 0.0
      K8_sica_accuracy: 0.717
      K8_sc_accuracy: 0.733
      K8_delta_pp: -1.7
      K11_sica_accuracy: 0.733
      K11_sc_accuracy: 0.733
      K11_delta_pp: 0.0
      K12_sica_accuracy: 0.733
      K12_sc_accuracy: 0.700
      K12_delta_pp: 3.3
      K16_sica_accuracy: 0.717
      K16_sc_accuracy: 0.733
      K16_delta_pp: -1.7
      K20_sica_accuracy: 0.700
      K20_sc_accuracy: 0.717
      K20_delta_pp: -1.7
      max_abs_delta_pp: 3.3
      all_p_gt_015: true
      K11_odd_gap: 0.0
      sica_leq_sc_at_large_K: true
    result_rationale: >
      n=60 功效不足——每个 K 条件的 SE ≈ 5-6pp，因此 ±3pp 波动完全在噪声范围内。
      K=11 (odd) delta=0 是关键信号：odd-K 几乎无 tie，SICA 无 tiebreak 优势时退化为 SC，
      证明 SICA 的全部增益来自 tiebreak 而非 constraint 信息。
      大 K (16,20) 轻微劣于 SC，因为更多 trace 引入更多低质量 constraints，
      MaxSAT 在噪声 constraints 上的 exclusion 偶尔排除正确答案。
      无任何 K 值达到 p < 0.15，与 median 档 "零个实验 p < 0.10" 一致。
    tables:
      - name: T_K_ablation
        description: K × (SICA, SC, Δpp, p-value) 表格，附 tiebreak frequency 列
    figures_description:
      - "Line plot: K (x) vs Δpp (y)，flat at ~0 with ±3pp noise band。标注 K=11 odd 点。"
    analysis: >
      SICA ≤ SC at all K ≥ 16; K=11 (odd) gap=0 确认 tie-only mechanism。
      Larger K does not help — noise injection from additional low-quality constraints。
      结论：SICA 对 K 值不敏感，其全部价值仅在 even-K tie 场景。

  # ── exp-003: tiebreak baseline ───────────────────────────────────────
  - name: tiebreak_baseline_analysis
    plan_id: exp-003
    description: >
      CPU-only：SICA vs SC-random-tiebreak vs SC-deterministic vs SC-alphabetical
      在所有已有数据上。量化 SICA 的 tiebreak 质量。
    expected_results:
      n_tied_questions: 32
      tied_question_pct: 5.3
      sica_tiebreak_accuracy: 0.781
      random_tiebreak_accuracy: 0.500
      alphabetical_tiebreak_accuracy: 0.594
      first_seen_tiebreak_accuracy: 0.438
      sica_vs_random_on_tied_p: 0.031
      overall_sica_accuracy: 0.765
      overall_random_tiebreak_accuracy: 0.756
      overall_gap_from_tiebreak_pp: 0.9
    result_rationale: >
      Tied questions 仅占 ~5% (约 32/600+)，因此 tiebreak quality 对 overall accuracy 的贡献
      被 denominator 严重稀释（0.78 × 5% ≈ +0.9pp）。SICA 在 tied subset 上确实优于 random
      (78% vs 50%, p~0.03)，但 tied subset 太小，使得 overall 影响可忽略。
      这与 median 档一致：mechanism 在微观上有效（tiebreak 确实更好），但 operating regime 太窄（ties 太少），
      整体收益被噪声淹没。alphabetical > random 因为正确答案在某些 domain 有字母偏好。
    tables:
      - name: T_tiebreak
        description: Tiebreak method × (tied accuracy, overall accuracy, Δ vs random)
    figures_description: []
    analysis: >
      SICA is a superior tiebreaker (78% vs 50%) but ties are ≤5% of problems。
      Overall impact: <1pp。Confirms capability trap at scale — even when constraints
      have information, it's exercised too rarely to matter。

  # ── exp-004: Qwen 7B scaling ────────────────────────────────────────
  - name: sica_7b_scaling
    plan_id: exp-004
    description: >
      Qwen2.5-7B-Instruct on D012 60 questions, K=12, T=0.7。
      测试: weaker model → higher C0 → larger SICA gain?
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.583
      sc_accuracy: 0.567
      delta_pp: 1.7
      mcnemar_p: 0.73
      multi_candidate_rate: 0.617
      c0_pct: 61.7
      extraction_rate: 0.82
      answer_extraction_rate: 0.88
      contradiction_rate: 0.068
      baseline_acc_drop_vs_14b: -16.3
      constraint_precision_mean: 0.51
    result_rationale: >
      7B 能力弱于 14B，SC baseline ~57% (vs 14B 的 70%)。更弱的模型产生更多 diversity
      (C0 ~62% vs 14B 的 ~46%)，但提取的 constraints 质量也更差 (precision ~0.51 ≈ random)。
      更高 C0 × 更低 precision = 净效果为零，delta +1.7pp 完全在 n=60 噪声范围内 (SE ≈ 6pp)。
      这正是 capability trap：diversity 增加了但 discriminative power 没有跟上。
      extraction_rate 下降 (0.82 vs 0.89) 反映 7B 生成的 reasoning trace 格式更不规范。
      此结果填入 C0 scatter 的 instruction-scale cluster，C0=62% 但 gap≈0。
    tables:
      - name: T_7b_row
        description: 添加到 T1 Main Results 的一行
    figures_description:
      - "F4 C0 vs Gap scatter 增加一点 (C0=62%, Δ=+1.7pp)，在 instruction cluster 内。"
    analysis: >
      C0 从 46%→62% 但 gap 不变。Confirms: diversity alone is insufficient。
      7B 落入 instruction-scale cluster (C0=40-65%)，无中间态，支持 binary C0 interpretation。

  # ── exp-005: QwQ-32B operating regime ────────────────────────────────
  - name: qwq_32b_operating_regime
    plan_id: exp-005
    description: >
      QwQ-32B 已有 MVP 数据 (AIME/MATH/PW/FOLIO) 重新格式化为 paper 的 Operating Regime 节。
      CPU-only，无新 GPU。
    expected_results:
      total_problems: 46
      qwq_c0_effective_pct: 2.8
      qwq_c0_nominal_pct: 10.5
      aime_sica_accuracy: 0.727
      aime_sc_accuracy: 0.727
      aime_delta_pp: 0.0
      aime_c0_pct: 0.0
      aime_n: 22
      proofwriter_sica_accuracy: 0.588
      proofwriter_sc_accuracy: 0.647
      proofwriter_delta_pp: -5.9
      proofwriter_c0_pct: 18.8
      proofwriter_n: 17
      folio_c0_pct: 0.0
      folio_n: 2
      temp_diversity_n: 5
      temp_diversity_divergence: 0
    result_rationale: >
      QwQ-32B 是 full reasoning model，deterministic chain dominates sampling randomness。
      即使 T=0.7-1.0，reasoning chain 的确定性使得 12 个 trace 几乎总是收敛到同一答案，
      effective C0 ~3% (只有少数 PW 题有 2 个 candidate)。SICA ≡ SC structurally——
      MaxSAT exclusion 操作无法改变 unanimous vote。PW 上 -5.9pp 来自 2 个 exclusion
      意外排除了正确答案的少数 multi-candidate 问题。
      这是 capability trap 的 "左墙"：reasoning model 太 consistent → 无 diversity → SICA redundant。
    tables:
      - name: T_qwq_row
        description: QwQ-32B 行添加到 T1，C0<5% 标注 "degenerates to SC"
    figures_description:
      - "F4: QwQ-32B 点在 C0≈3% 处，gap=0。与 instruction cluster (C0=40-60%) 形成鲜明两簇。"
    analysis: >
      QwQ-32B: C0<5%, SICA≡SC。Reasoning model 的 chain-of-thought 消除了 output diversity，
      使 symbolic consensus 退化为 majority vote。支持 Claim 2 的 "reasoning model" 分支。

  # ── exp-006: C0 diagnostic validation ────────────────────────────────
  - name: c0_diagnostic_validation
    plan_id: exp-006
    description: >
      CPU-only: 汇总所有 model × domain 的 C0 vs SICA-SC gap scatter。验证 C0 作为 predictor。
    expected_results:
      n_datapoints: 12
      c0_cluster_high_mean: 48.2
      c0_cluster_high_range: [38, 62]
      c0_cluster_high_gap_mean_pp: 0.3
      c0_cluster_low_mean: 3.1
      c0_cluster_low_range: [0, 5]
      c0_cluster_low_gap_mean_pp: -1.2
      n_distinct_clusters: 2
      intermediate_c0_points: 0
      pearson_r: 0.08
      pearson_p: 0.81
      c0_below_5_always_gap_leq_0: true
      c0_above_30_gap_range_pp: [-3.3, 3.3]
    result_rationale: >
      Median 档只有 2 个 C0 cluster：instruction-scale (C0=38-62%) 和 reasoning (C0<5%)。
      无中间态——没有 C0=15-25% 的数据点（7B/14B 都在 40%+ 区间，QwQ 在 <5%）。
      两个 cluster 内 gap 方差大 (instruction cluster 内 Δ 从 -3.3pp 到 +3.3pp)，
      因此 C0 vs gap 的线性相关极弱 (r≈0.08)。C0 唯一可靠的 predictive power 是
      "C0<5% → gap=0"，即 binary gate，而非 gradient predictor。
      这迫使 Claim 3 降级为 "binary early-stopping gate" 而非 "diagnostic predictor"。
    tables:
      - name: T_c0_scatter_data
        description: Model × Domain × C0 × Δpp 汇总表
    figures_description:
      - "F4 修订版: C0 (x) vs Δpp (y) scatter, 仅两簇, 无回归线。用虚线标注 C0=5% threshold。"
    analysis: >
      仅 2 个 cluster，无 gradient。C0 的价值是 binary gate: C0<5% → 跳过 SICA。
      C0>30% 不预测任何方向的 gain。Claim 3 降级为半页讨论。

  # ── exp-007: Qwen 72B AWQ ───────────────────────────────────────────
  - name: sica_72b_awq
    plan_id: exp-007
    description: >
      Qwen2.5-72B-Instruct AWQ 4-bit on D012 60 questions, K=12, T=0.7。
      Within-Qwen scaling: 高 baseline non-reasoning model。
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.817
      sc_accuracy: 0.833
      delta_pp: -1.7
      mcnemar_p: 0.65
      multi_candidate_rate: 0.383
      c0_pct: 38.3
      extraction_rate: 0.91
      answer_extraction_rate: 1.0
      contradiction_rate: 0.018
      baseline_acc_gain_vs_14b: +13.3
      constraint_precision_mean: 0.54
    result_rationale: >
      72B 更强 → SC baseline 更高 (~83% vs 14B 的 70%)。C0 下降到 ~38% (vs 14B 的 46%)
      因为更强模型更 consistent，但仍远高于 5% threshold → 落入 instruction-scale cluster。
      Delta -1.7pp 在 n=60 噪声范围内。72B 的 constraints 质量略好 (precision 0.54)
      但提升微弱，不足以改变 outcome。
      关键贡献：在 C0 scatter 中填入 C0=38% 点，与 7B (C0=62%) 和 14B (C0=46%) 一起
      展示 within-family C0 随 scale 递减趋势，但三点都在 instruction cluster 内。
      无中间态 (C0 没有从 40% 跌到 15%)——从 instruction 直接跳到 reasoning (<5%)。
    tables:
      - name: T_72b_row
        description: 72B 行添加到 T1 Main Results
    figures_description:
      - "F4: Qwen 三点 (7B C0=62%, 14B C0=46%, 72B C0=38%) 连线，都在 instruction cluster，gap≈0。"
    analysis: >
      72B C0=38%，仍在 instruction cluster。Within-Qwen scaling 展示 C0 递减但无质变。
      三个 Qwen scale 点都在 capability trap 内——更高 accuracy 但 constraints 仍不 discriminative。

  # ── exp-008: case studies ────────────────────────────────────────────
  - name: constraint_quality_case_studies
    plan_id: exp-008
    description: >
      5-10 个代表性问题的 constraint 质量定性分析。
      Constraints 是否语义有意义？被排除的 constraints 是否对应推理错误？
    expected_results:
      n_cases: 8
      constraints_syntactically_valid_pct: 85
      constraints_semantically_relevant_pct: 62
      constraints_discriminative_pct: 18
      exclusion_correct_pct: 45
      case_categories:
        unanimous_correct: 3
        unanimous_wrong: 1
        multi_candidate_sica_correct: 2
        multi_candidate_sica_wrong: 2
    result_rationale: >
      Median 档下，constraints 的核心问题是 discriminative power 不足而非 extraction failure。
      大多数 constraints 是合法 FOL 且语义相关 (~62%)，但只有 ~18% 能区分正确/错误答案。
      原因：LLM 从 trace 中提取的 constraints 倾向于 tautological（"如果 A 那么 A" 型）
      或 overly general（"答案必须是正数" 型），对所有 candidate answers 都满足。
      被 MaxSAT exclusion 排除的 constraints 中，约一半确实对应推理错误 (45%)，
      但另一半是有效但与 solver 冲突的 constraints——即 false positive exclusion。
      这支持 capability trap narrative：extraction 工作了，但提取出的东西缺乏信息量。
    tables: []
    figures_description:
      - "Box: 2 个对比 case study (一个 SICA 正确翻转，一个 SICA 错误翻转)，展示 constraint 质量差异。"
    analysis: >
      Constraints 有语法正确性但缺 discriminative power。Case studies 为 exp-013 的
      "MaxSAT ≈ count-only" 提供定性解释：当 constraints 无法区分答案时，
      MaxSAT 的 satisfiability reasoning 退化为 constraint counting。

  # ── exp-009: overhead analysis ───────────────────────────────────────
  - name: overhead_analysis
    plan_id: exp-009
    description: >
      Wall-time breakdown: generation / constraint extraction / MaxSAT solving。
      每问题成本。
    expected_results:
      n: 804
      mean_total_wall_s: 62.0
      mean_trace_gen_s: 32.0
      trace_gen_pct: 51.6
      mean_extraction_s: 29.0
      extraction_pct: 46.8
      mean_dedup_s: 0.9
      dedup_pct: 1.5
      mean_maxsat_s: 0.004
      maxsat_pct: 0.006
      sica_overhead_vs_sc_pct: 48.4
      sica_overhead_s_per_problem: 30.0
      pw_overhead_pct: 51.0
      folio_overhead_pct: 39.0
    result_rationale: >
      Trace generation 和 constraint extraction 各占 ~50% 时间。MaxSAT solving 本身极快
      (<0.01%)——Z3 在这个 scale 的 FOL 问题上几乎即时。核心 overhead 来自 LLM constraint
      extraction call (对每个 trace 做一次 extraction prompt)。
      这意味着 SICA 的计算成本是 SC 的 ~2x (12 traces + 12 extraction calls vs 12 traces)。
      对于 Δ≈0pp 的收益，~2x overhead 是不可接受的 ROI。
      Median 档下这个数据直接支持 "practical recommendation: use SC" 的结论。
    tables:
      - name: T_overhead
        description: Pipeline stage × (mean_s, pct, p50, p90)
    figures_description:
      - "Stacked bar: trace_gen / extraction / dedup / maxsat 各阶段耗时占比。"
    analysis: >
      SICA 增加 ~49% overhead (主要是 constraint extraction LLM calls)。
      结合 Δ≈0pp，cost-benefit 结论明确：SC 是更好的 default。

  # ── exp-011: LLaMA 8B ───────────────────────────────────────────────
  - name: sica_llama_8b
    plan_id: exp-011
    description: >
      LLaMA-3.1-8B-Instruct on D012 60 questions, K=12。
      第二个 non-Qwen family，消除 Qwen-specific artifact。
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.650
      sc_accuracy: 0.600
      delta_pp: 5.0
      mcnemar_p: 0.29
      multi_candidate_rate: 0.600
      c0_pct: 60.0
      extraction_rate: 0.86
      answer_extraction_rate: 0.90
      contradiction_rate: 0.053
      truncated_traces: 40
      discordant_sica_wins: 4
      discordant_sc_wins: 1
      proofwriter_sica: 0.600
      proofwriter_sc: 0.567
      proofwriter_delta_pp: 3.3
      folio_sica: 0.700
      folio_sc: 0.633
      folio_delta_pp: 6.7
    result_rationale: >
      LLaMA-8B 是 median 档中 1-2 个 "方向性噪声点" 之一——Δ=+5pp 看似 positive 但
      p=0.29 远超显著性阈值 (n=60 SE ≈ 6pp)。高 C0 (~60%) 反映 8B 模型能力不足导致的
      高 diversity (多个 candidate 答案)。discordant pair 4:1 偏向 SICA 但样本太小。
      关键：这不是 real signal，而是 n=60 的 sampling noise。exp-019 (n=200 StrategyQA)
      和 exp-020 (n=204 FOLIO) 用 LLaMA-8B 做的 powered test 将显示 gap 收缩到
      +2pp 和 -2.4pp，证明 D012 的 +5pp 是 upward noise。
      truncated_traces=40 (7%) 反映 8B 生成更长更散的 reasoning traces。
    tables:
      - name: T_llama_row
        description: LLaMA-8B 行添加到 T1 Main Results
    figures_description: []
    analysis: >
      Δ=+5pp 是 n=60 噪声 (p=0.29)。将与 exp-019/020 的 powered tests 一起展示，
      证明 small-n 估计的不可靠性。正文必须 hedge 此数据点。

  # ── exp-012: GSM8K pilot ────────────────────────────────────────────
  - name: gsm8k_pilot_14b
    plan_id: exp-012
    description: >
      Qwen2.5-14B on GSM8K 30 questions, K=12。
      Cross-domain: 开放答案数学域的 C0 行为。
    expected_results:
      n: 30
      k: 12
      sica_accuracy: 0.867
      sc_accuracy: 0.867
      delta_pp: 0.0
      multi_candidate_rate: 0.133
      c0_pct: 13.3
      extraction_rate: 0.93
      constraint_precision_mean: 0.58
    result_rationale: >
      Qwen-14B 在 GSM8K 上 accuracy >85%，模型足够强使得大部分问题 12 个 trace 收敛到
      同一正确答案。C0 ~13%——低于 NLI 域的 46% 但高于 reasoning model 的 <5%。
      然而 n=30 仅 4 个 multi-candidate 问题，太少以至于 SICA 无法展示任何 signal。
      此结果介于两个 cluster 之间 (C0=13% 在 5-30% 区间)，但 n 太小不能视为
      可靠的 "intermediate" 数据点。在 exp-006 scatter 中标注为 pilot (open marker)。
      constraint_precision 略高 (0.58) 因为数学 constraints 更 well-defined，
      但样本太小无统计意义。
    tables:
      - name: T_gsm8k_pilot_row
        description: GSM8K pilot 行，标注 n=30 pilot
    figures_description: []
    analysis: >
      C0=13% — 低于 instruction-scale cluster 均值但 n 太小。
      放入 appendix 作为 "domain coverage" 数据点而非主 claim 的证据。

  # ── exp-013: constraint ablation (CRITICAL) ──────────────────────────
  - name: constraint_ablation
    plan_id: exp-013
    description: >
      CPU-only: MaxSAT vs count-only vs random-weight。
      如果 MaxSAT ≈ count-only → constraint satisfiability 信息无贡献，
      confirming capability trap mechanism。
    expected_results:
      n: 804
      maxsat_accuracy: 0.765
      count_only_accuracy: 0.766
      random_weight_accuracy: 0.764
      sc_baseline_accuracy: 0.762
      maxsat_vs_countonly_delta_pp: -0.1
      maxsat_vs_random_delta_pp: 0.1
      countonly_vs_sc_delta_pp: 0.4
      agreement_maxsat_countonly: 801
      agreement_all_three: 799
      mcnemar_maxsat_vs_countonly_p: 0.82
      mcnemar_maxsat_vs_random_p: 0.78
      problems_where_method_differs: 5
    result_rationale: >
      这是 median 档的 make-or-break evidence。MaxSAT ≈ count-only ≈ random-weight
      (三者在 804 题中 799 题给出相同答案)。这证明 Z3 solver 的 satisfiability reasoning
      没有贡献任何信息——constraint count 已经捕获了全部 signal。
      原因：当 constraints 缺乏 discriminative power (precision ≈ 0.53) 时，
      MaxSAT 的 "满足尽可能多 constraints" 策略退化为 "选择有最多 constraints 的答案"，
      即 count-only。random-weight 也 ≈ count-only 因为权重在 noise 上的加和仍趋向 count。
      5 个 divergent 问题中 MaxSAT 胜 2 败 3，无系统性优势。
      这是 capability trap 的 mechanistic core：solver 是 vacuous layer。
    tables:
      - name: T3_constraint_ablation
        description: Method × (accuracy, vs-SC Δpp, inter-method agreement rate)
    figures_description:
      - "Bar chart: MaxSAT / count-only / random-weight / SC，四个几乎等高的 bar + error bars 重叠。"
    analysis: >
      MaxSAT ≈ count-only ≈ random-weight (agreement 99.4%)。
      SAT solver 在 non-discriminative constraints 上是 no-op。
      这是论文最重要的 mechanism evidence — 入 Section 5 正文。

  # ── exp-015: Logic-LM baseline ──────────────────────────────────────
  - name: logic_lm_baseline
    plan_id: exp-015
    description: >
      Logic-LM × K + majority vote on FOLIO。
      用 exp-001 已有 traces 做 single-trace FOL verification then vote。
    expected_results:
      n_folio: 204
      logic_lm_k12_accuracy: 0.789
      sc_k12_accuracy: 0.794
      sica_k12_accuracy: 0.794
      logic_lm_vs_sc_delta_pp: -0.5
      logic_lm_vs_sica_delta_pp: -0.5
      logic_lm_fol_verify_rate: 0.72
      logic_lm_fol_reject_rate: 0.28
      logic_lm_reject_correct_pct: 0.31
    result_rationale: >
      Logic-LM 对每个 trace 独立做 FOL verification，reject 不可验证的 traces，
      然后对剩余 traces majority vote。FOL verification reject rate ~28%——
      很多 traces 的 FOL 无法被 solver 验证 (timeout, 格式错误, etc.)。
      被 reject 的 traces 中 31% 实际上是正确的 → verification 本身有 noise。
      最终 accuracy 0.789 ≈ SC (0.794)，因为 reject 噪声抵消了 verification 的
      potential benefit。Logic-LM × K 并不优于简单 SC。
      这从另一个角度支持 capability trap：不仅 MaxSAT aggregation 无效，
      single-trace FOL verification 也无法 reliably 筛选 trace quality。
    tables:
      - name: T_logiclm_baseline
        description: Logic-LM × K vs SC vs SICA on FOLIO
    figures_description: []
    analysis: >
      Logic-LM × K ≈ SC ≈ SICA on FOLIO。FOL verification 本身 noisy (reject 31% correct traces)。
      Symbolic methods 的 limitation 不限于 aggregation——单 trace verification 也 unreliable。

  # ── exp-016: weighted SC baseline ───────────────────────────────────
  - name: weighted_sc_baseline
    plan_id: exp-016
    description: >
      Weighted SC (uniform / inv-length / length / constraint-count) on exp-001 数据。
      CPU-only。
    expected_results:
      n: 804
      sc_uniform_accuracy: 0.762
      inv_length_accuracy: 0.767
      length_weighted_accuracy: 0.753
      constraint_count_accuracy: 0.753
      inv_length_vs_sc_p: 0.45
      length_vs_sc_p: 0.15
      constraint_count_vs_sc_p: 0.20
      inv_length_vs_sica_p: 0.86
      all_nonsignificant: true
    result_rationale: >
      inv-length 略好于 SC (+0.5pp) 因为更短 traces 倾向于更 confident 更 correct (7B 级别下
      长 traces 往往是 hedging / 错误推理的信号)。但 p=0.45 远非显著。
      length-weighted 反而 worse (-0.9pp) 因为长 traces 不一定更好。
      constraint-count weighted 也 worse (-0.9pp) 因为更多 constraints 不等于更好的推理。
      所有 weighting schemes 都 non-significant vs SC，SICA 无优势 vs inv-length。
      结论：simple weighting 是 SICA 的直接竞争者，且同样无效。
    tables:
      - name: T_weighted_sc
        description: Weighting method × (accuracy, Δ vs SC, p-value)
    figures_description: []
    analysis: >
      所有 weighting methods ≈ SC (none significant)。SICA 的 MaxSAT 不优于 simple heuristics。
      进一步确认 aggregation mechanism 无信息贡献。

  # ── exp-017: StrategyQA 14B ─────────────────────────────────────────
  - name: sica_strategyqa_14b
    plan_id: exp-017
    description: >
      Qwen2.5-14B on StrategyQA 60 questions, K=12。
      Commonsense reasoning, binary answer, 预期 high diversity。
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.567
      sc_accuracy: 0.533
      delta_pp: 3.3
      mcnemar_p: 0.48
      bootstrap_p_delta_le_0: 0.13
      multi_candidate_rate: 0.10
      c0_pct: 10.0
      extraction_rate_problem: 1.0
      extraction_rate_trace: 0.70
      contradiction_detected: 5
      discordant_sica_wins: 2
      discordant_sc_wins: 0
    result_rationale: >
      StrategyQA 是 binary (yes/no) → 14B 足够强使大部分问题 SC unanimous，
      C0 仅 ~10% (低于预期的 35-50%)。binary answer space 限制了 diversity——
      不像 NLI 的 3-class 或 math 的 open-ended。
      Delta +3.3pp 来自 2 个 discordant pairs (SICA 全赢)，但 n=60 binary outcome
      的噪声极大，p=0.48。bootstrap CI 包含 0。
      这是 median 档的另一个 "方向性噪声点"——看似 positive 但不可靠。
      extraction_rate_trace 仅 70% 因为 commonsense reasoning traces 格式更自由，
      FOL extraction 常失败。这本身就是 capability trap 的一个 facet：
      非形式推理更难转化为 formal constraints。
    tables:
      - name: T_strategyqa_row
        description: StrategyQA 行添加到 T1 Main Results
    figures_description: []
    analysis: >
      C0=10%，低于预期。Binary answer format 限制 diversity。
      Δ=+3.3pp non-significant (p=0.48)。Commonsense traces 的 extraction rate 较低。

  # ── exp-018: ARC-Challenge 14B ──────────────────────────────────────
  - name: sica_arc_challenge_14b
    plan_id: exp-018
    description: >
      Qwen2.5-14B on ARC-Challenge 60 questions, K=12。
      Science reasoning, 4-choice。
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.950
      sc_accuracy: 0.967
      delta_pp: -1.7
      multi_candidate_rate: 0.05
      c0_pct: 5.0
      extraction_rate: 1.0
      contradiction_detected: 3
      discordant_sica_wins: 0
      discordant_sc_wins: 1
    result_rationale: >
      14B 在 ARC-Challenge 上极强 (SC ~97%)，几乎所有问题 12 个 trace unanimous correct。
      C0 仅 ~5%——接近 reasoning model 的 cluster。仅 3 个 multi-candidate 问题，
      其中 1 个 SICA exclusion 错误排除了正确答案 → Δ=-1.7pp。
      ARC-Challenge 对 14B 太简单——ceiling effect 使得 SICA 无 operating space。
      4-choice format 和 science domain 的 constraints 实际上 extraction 良好 (rate=1.0)
      但无用武之地因为答案几乎 unanimous。
      放入 T1 作为 "domain breadth" 证据，但 C0 ~5% 意味着 ARC 数据对 capability trap
      的 mechanism 讨论贡献有限。
    tables:
      - name: T_arc_row
        description: ARC-Challenge 行添加到 T1 Main Results
    figures_description: []
    analysis: >
      C0=5%, SC 已 97%。Ceiling effect → SICA 无空间。
      验证 capability trap 的另一面：当 model 够强时 diversity 消失。

  # ── exp-019: constraint quality correlation (F2 hero figure) ────────
  - name: constraint_quality_correlation
    plan_id: exp-019
    description: >
      CPU-only: per-problem constraint precision × vote entropy × C0 × SICA-SC gap。
      F2 hero figure 的数据源。
    expected_results:
      n_per_problem: 307
      constraint_precision_mean: 0.538
      constraint_precision_std: 0.21
      constraint_precision_median: 0.53
      precision_vs_entropy_pearson_r: 0.09
      precision_vs_entropy_pearson_p: 0.11
      precision_vs_entropy_slope: 0.028
      binned_precision_low_entropy: 0.51
      binned_precision_mid_entropy: 0.54
      binned_precision_high_entropy: 0.57
      bin_n_low: 102
      bin_n_mid: 105
      bin_n_high: 100
      binned_ci_overlap: true
      aggregate_precision_by_domain:
        proofwriter: 0.54
        folio: 0.52
        strategyqa: 0.55
      f2_raw_scatter_r_squared: 0.008
    result_rationale: >
      Per-problem constraint precision 均值 0.538 (barely above random 0.50)，
      与 entropy 有极弱正相关 (r=0.09, p=0.11)。raw scatter 极嘈杂 (R²=0.008)
      因为每个 problem 的 constraint 数量变异大 (5-40+)，且 precision 的 per-problem
      估计本身有高方差。
      binned box-plot 显示方向性趋势 (low→mid→high entropy 对应 0.51→0.54→0.57 precision)
      但 95% CI 重叠。这是 median 档定义的核心特征：aggregate 方向一致但 per-problem noise
      大，需要 binned visualization 才可读。
      F2 不能作为独立 evidence——必须与 exp-013 (MaxSAT ≈ count-only) 搭配。
      正文承认 "per-problem precision is noisy (σ=0.21)" 但强调
      "aggregate constraint precision is consistently near chance (0.52-0.56 across domains)"。
    tables:
      - name: T_constraint_precision
        description: Domain × (precision mean, std, n)
    figures_description:
      - >
        F2 hero figure (修订版): 三列 binned box-plot (low/mid/high vote_entropy)，
        y = constraint_precision, 每 bin ~100 points。加 95% CI band (灰色)。
        右侧 marginal: per-domain means with error bars。
        Caption: "Constraint precision near chance across entropy bins;
        binned means show weak positive trend but CIs overlap."
    analysis: >
      F2 从 scatter 改为 binned box-plot。Per-problem noise 太大无法用 raw scatter 展示。
      Aggregate constraint precision 0.52-0.56 ≈ chance，
      是 capability trap 的 population-level evidence。降级为辅助角色，exp-013 是主力。

  # ── what-if: temperature ablation ───────────────────────────────────
  - name: temperature_ablation_t03_t05_t10
    plan_id: what-if
    description: >
      Qwen-14B T=0.3/0.5/1.0 on D012 60 questions, K=12。
      测试 temperature → diversity → SICA gain 因果链。
    expected_results:
      t03_sica_accuracy: 0.750
      t03_sc_accuracy: 0.750
      t03_delta_pp: 0.0
      t03_c0_pct: 30.0
      t03_multi_candidate_rate: 0.30
      t05_sica_accuracy: 0.733
      t05_sc_accuracy: 0.733
      t05_delta_pp: 0.0
      t05_c0_pct: 40.0
      t05_multi_candidate_rate: 0.40
      t07_ref_sica_accuracy: 0.733
      t07_ref_sc_accuracy: 0.700
      t07_ref_delta_pp: 3.3
      t07_ref_c0_pct: 53.3
      t10_sica_accuracy: 0.700
      t10_sc_accuracy: 0.717
      t10_delta_pp: -1.7
      t10_c0_pct: 58.3
      t10_multi_candidate_rate: 0.583
      c0_increases_with_temp: true
      gap_uncorrelated_with_temp: true
      max_abs_delta_pp: 3.3
      worst_noise_point_T: 0.7
      any_p_below_010: false
    result_rationale: >
      Temperature 确实增加 diversity: C0 从 T=0.3 的 30% 到 T=1.0 的 58%。
      但 SICA-SC gap 与 T 无相关: T=0.3 gap=0, T=0.5 gap=0, T=0.7 gap=+3.3, T=1.0 gap=-1.7。
      T=0.7 的 +3.3pp 和 T=1.0 的 -1.7pp 都是 n=60 噪声 (SE ≈ 6pp)。
      这直接反驳 "increasing diversity helps SICA" hypothesis，支持 capability trap：
      diversity 上升但 constraint quality 不变 → gap 停留在 noise band 内。
      关键 median 档特征：某个 T 条件出现 |Δ|=3-5pp (p>0.15)，功效不足以排除噪声。
      T=0.3 的 C0=30% 和 T=1.0 的 C0=58% 都在 instruction cluster 内。
      正文入 Section 5 但 hedge: "across the tested temperature range (0.3-1.0), 
      increasing diversity did not translate to SICA gains."
    tables:
      - name: T_temp_ablation
        description: T × (C0, SICA, SC, Δpp, p-value) 表格
    figures_description:
      - >
        Dual y-axis: T (x) vs C0% (left y, ascending line) vs Δpp (right y, flat ~0 with noise)。
        标注 noise band (±SE)。Visual message: C0 rises but gap stays flat。
    analysis: >
      Temperature 控制 diversity 但不控制 SICA 收益。C0 monotonically increases with T
      但 gap 在 noise band 内波动。Supports capability trap: diversity is not the bottleneck。

  # ── what-if: GSM8K pilot ────────────────────────────────────────────
  - name: gsm8k_pilot_30q
    plan_id: what-if
    description: >
      Qwen-14B GSM8K 30 questions, K=12。
      数学域覆盖，预期 C0 低。
    expected_results:
      n: 30
      k: 12
      sica_accuracy: 0.867
      sc_accuracy: 0.867
      delta_pp: 0.0
      multi_candidate_rate: 0.133
      c0_pct: 13.3
      extraction_rate: 0.93
      constraint_precision_mean: 0.58
    result_rationale: >
      与 exp-012 预测一致 (同一实验)。14B 在 GSM8K 上 accuracy 高 → C0 低 (~13%)。
      仅 ~4 个 multi-candidate 问题，SICA 无空间。数学 constraints (等式、不等式)
      比 NLI constraints 更 well-formed，precision 略高 (0.58)，但样本太小无意义。
      作为 appendix domain coverage 数据点。
    tables: []
    figures_description: []
    analysis: >
      C0=13%, 接近 ceiling-effect 区域。与 ARC-Challenge 类似——model 太强导致 SICA redundant。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "690fc69b-ee77-48aa-b46b-5400493750e5",
  "isSidechain": false,
  "requestId": "req_011Cb8MLE9eHgAHfeLgWx4WS",
  "type": "assistant",
  "uuid": "a911f052-4822-495c-9559-398dfd53d14d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ecf2953d-324d-49a6-8fc1-127e33d095cd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013xwGj4QTX5UcA19hpHEBvY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18738,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15191,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18738,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15191,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18738
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 negative result (SICA ≈ SC) 稳固, 但 mechanism evidence 有噪声; F2 需 binned 可视化; C0 仅二值非梯度; claims 措辞需软化 核心假设：['Temperature ablation: C0 大致随 T 增加但某 T 条件出现 |…",
  "leafUuid": "a911f052-4822-495c-9559-398dfd53d14d",
  "sessionId": "ecf2953d-324d-49a6-8fc1-127e33d095cd"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier capability trap characterization with binned F2 analysis",
  "sessionId": "ecf2953d-324d-49a6-8fc1-127e33d095cd"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 negative result (SICA ≈ SC) 稳固, 但 mechanism evidence 有噪声; F2 需 binned 可视化; C0 仅二值非梯度; claims 措辞需软化 核心假设：['Temperature ablation: C0 大致随 T 增加但某 T 条件出现 |…",
  "leafUuid": "a911f052-4822-495c-9559-398dfd53d14d",
  "sessionId": "ecf2953d-324d-49a6-8fc1-127e33d095cd"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier capability trap characterization with binned F2 analysis",
  "sessionId": "ecf2953d-324d-49a6-8fc1-127e33d095cd"
}
```

---
