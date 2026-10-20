# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Capability trap 被结构性确认: diversity 可操控但 SICA 收益恒零; F2 per-problem 清晰展示 constr

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-3/ac90f59c-9ff1-4501-bfdb-c836f1ffbc83.jsonl`
- **Structured JSON:** [`acf9b307a2bfd5e5ea91.json`](../../sessions/ac/acf9b307a2bfd5e5ea91.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T14:49:52.692Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T14:49:52.692Z",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Capability trap 被结构性确认: diversity 可操控但 SICA 收益恒零; F2 per-problem 清晰展示 constraint 非判别性; 三条 claims 原样保留\n核心假设：['Temperature ablation: C0 随 T 单调递增 (T=0.3 C0≈25-35%, T=1.0 C0≈60-75%), 所有条件 |Δ| ≤ 3pp, p > 0.20', \"F2 per-problem (n≈307): constraint precision 均值 ≈ 0.50 (近随机), 与 vote_entropy 无相关 (slope ≈ 0) → scatter 可视化直接支撑 'regardless of diversity'\", \"exp-004 (7B) / exp-007 (72B) 产出至少 3 个 distinct C0 水平 (如 7B≈65%, 14B≈38%, 72B≈15%) → Claim 3 'diagnostic predictor' 成立\", '所有已完成 + 新完成实验中零个正向 p < 0.10; discordant pair SICA winrate ≈ 50%', 'exp-013 MaxSAT ≈ count-only 已确认, 与 F2 per-problem 数据形成双重 mechanism evidence']\n关键指标范围：{'temp_max_abs_delta_pp': [0, 3.0], 'f2_constraint_precision_mean': [0.48, 0.53], 'f2_precision_vs_entropy_slope': [-0.02, 0.02], 'aggregate_abs_weighted_delta_pp': [0, 0.8], 'n_exp_positive_p_below_010': 0, 'c0_scaling_distinct_levels': [3, 5], 'discordant_sica_winrate': [0.42, 0.55]}\n叙事方向：原始 Capability Trap framing 完全成立。Temperature ablation 作为 §5 新证据: 'We experimentally manipulate diversity via temperature and confirm the trap holds at all levels — this is structural, not a tuning failure.' F2 hero figure per-problem scatter 清晰可读, 无需 binning。三条 claim 措辞不改。Title 保持 'The Capability Trap'。强 EMNLP main submission, contribution = mechanism identification + first systematic negative result + zero-cost diagnostic。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\nfocus: 验证更新后的 capability trap framing: 机制从\"diversity-quality inverse correlation\"精确化为\"constraints lack discriminative power regardless of diversity level\"。新增 DeepSeek-R1-Distill-7B 作为第四个 instruction-scale 模型。F2 hero figure 现有 per-problem 数据 (n=307, vote_entropy vs exclusion_rate)。\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)\n\n1. **The Capability Trap**: Symbolic consensus methods face a fundamental tension: they require output diversity (C0>20%) to differ from voting, but extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to a noise injector. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B).\n2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.\n3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.\n\n## Core Insight\nSymbolic constraint consensus doesn't improve LLM reasoning because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these constraints lack the discriminative power to distinguish correct from incorrect answers. MAX-SAT optimization over non-discriminative constraints degenerates to noise injection, performing no better (often worse) than simple majority voting. We provide the first systematic empirical study characterizing this trap across 3 reasoning domains, 4 instruction-scale model families, and 1 full reasoning model.\n\n## Story Spine\n- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?\n- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.\n- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.\n- **Headline result**: \"Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis\n3. **\"Only Qwen models\"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B\n4. **\"Only one reasoning model\"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)\n5. **\"Only logic domain\"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.\n6. **\"MAX-SAT is over-engineering\"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.\n7. **\"Random tiebreak baseline\"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.\n8. **\"Why not just use a reasoning model?\"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.\n9. **\"How does this compare to Logic-LM / LINC?\"** → exp-015: Logic-LM × K baseline (CPU-only)\n10. **\"Weighted SC is simpler\"** → exp-016: Weighted SC baseline (CPU-only)\n11. **\"C0 is trivially derived\"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.\n12. **\"Within-family scaling?\"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.\n\n## Working Title\n**\"The Capability Trap: Why Symbolic Consensus Cannot Beat Majority Voting for LLM Reasoning\"**\n(Alternatives: \n- \"When Does Symbolic Consensus Help? An Empirical Answer: Rarely, and Here's Why\"\n- \"Diversity Without Quality: The Fundamental Limitation of Constraint-Based LLM Aggregation\")\n\n## Paper Structure (EMNLP 8pp + appendix)\n- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Capability Trap: C0 × Constraint Quality inverse correlation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Tiebreak Analysis: quality on tied questions only)\n- Main Figures: F1 (Method Pipeline), F2 (Capability Trap Scatter: C0 vs Constraint Precision, colored by domain, hero figure), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: flat line, contrasting with theoretical upper bound)\n- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data\n\n## Claim Risk Notes (Updated D035 + exp-014)\n- **Claim 1 mechanism refinement**: \"Inverse correlation between diversity and quality\" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: \"constraints lack discriminative power regardless of diversity level.\" Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.\n- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.\n- **Claim 3 gradient risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to \"binary indicator\". Need exp-004/007 for gradient data. OPEN.\n- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.\n- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.\n\n## Venue Fit Risks\n- EMNLP: Negative-results/analysis paper. Must answer \"so what should practitioners do?\" → C0 as deployment diagnostic + overhead analysis.\n- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.\n- Statistical power: Now strong (N>1,200 combined across powered tests).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes\n    odd K=11 to test if SICA value persists without exact ties. Key questions: does\n    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency\n    change with K?'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如\n    gap>0 → SICA has value beyond tiebreaking。\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Within-Qwen scaling dimension.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX\n    PRO 6000 单卡可放。\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。\n- id: exp-010\n  name: sica_mistral_7b\n  claim:\n  - 2\n  - 3\n  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family\n    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''\n    attack.'\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: DONE\n  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+\n    题（~3h GPU，margin 允许）。'\n  registry_id: exp-010-mistral-v3\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- id: exp-011\n  name: sica_llama_8b\n  claim:\n  - 2\n  - 3\n  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.\n    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation\n    同 exp-010。\n- id: exp-012\n  name: gsm8k_pilot_14b\n  claim:\n  - 2\n  - 3\n  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:\n    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer\n    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain\n    win.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable\n    insight.\n- id: exp-013\n  name: constraint_ablation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count\n    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:\n    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability\n    trap.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability\n    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'\n- id: exp-014\n  name: sica_deepseek_r1_llama_8b\n  claim:\n  - 2\n  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning\n    model data point with LLaMA base architecture: validates C0<5% generalizes beyond\n    QwQ-32B AND eliminates ''still Qwen family'' attack.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。\n- id: exp-015\n  name: logic_lm_baseline\n  claim:\n  - 1\n  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style\n    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT\n    multi-trace aggregation adds value beyond FOL extraction itself.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL\n    constraints 做单 trace verification then vote。'\n- id: exp-016\n  name: weighted_sc_baseline\n  claim:\n  - 1\n  - 3\n  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes\n    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.\n    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),\n    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count\n    weighted (no SAT)。'\n- id: exp-017\n  name: sica_strategyqa_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning\n    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected\n    constraint quality. Tests capability trap in best-case-diversity scenario.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability\n    trap（diversity high but quality low → no gain）。\n- id: exp-018\n  name: sica_arc_challenge_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,\n    4-choice format. Tests constraint mechanism in multi-choice scenario + different\n    domain.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)\n    + StrategyQA (binary) 形成答案格式多样性。\n- id: exp-019\n  name: constraint_quality_correlation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only analysis: compute constraint precision per domain × model,\n    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality\n    correlation. Uses data from exp-001/010/011/017/018.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-017\n  - exp-018\n  status: planned\n  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent\n    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have\n    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K6_sica: 0.733\n    K6_sc: 0.733\n    K6_gap_pp: 0\n    K8_sica: 0.733\n    K8_sc: 0.75\n    K8_gap_pp: -1.7\n    K11_sica: 0.733\n    K11_sc: 0.733\n    K11_gap_pp: 0\n    K12_sica: 0.7\n    K12_sc: 0.75\n    K12_gap_pp: -5\n    K16_sica: 0.717\n    K16_sc: 0.75\n    K16_gap_pp: -3.3\n    K20_sica: 0.7\n    K20_sc: 0.733\n    K20_gap_pp: -3.3\n    all_K_sica_leq_sc: true\n    larger_K_degrades_sica: true\n- exp_id: sica_constraint_ablation_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    maxsat_accuracy: 0.7649\n    count_only_accuracy: 0.7662\n    random_weight_accuracy: 0.7637\n    sc_baseline_accuracy: 0.7624\n    n_problems: 804\n    agreement_802_of_804: true\n    mcnemar_p_all_gt_0.7: true\n    note: approximate (raw z3 formulas unavailable, count-only/random-weight use proxy)\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwq_aggregate_c0_nominal_pct: 10.3\n    qwq_aggregate_c0_effective_pct: 2.6\n    qwen14b_c0_pct: 46\n    diversity_ratio_effective: 17.7\n    aime_delta_pp: 0\n    proofwriter_delta_pp: -5.9\n    aime_n: 22\n    proofwriter_n: 17\n    temp_diversity_n: 5\n    folio_n: 2\n    total_problems: 46\n    c0_threshold: 20\n    qwq_below_threshold: true\n- exp_id: exp-011-llama8b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-016-weighted-sc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7649\n    sc_uniform_accuracy: 0.7624\n    inv_length_accuracy: 0.7674\n    length_weighted_accuracy: 0.7525\n    constraint_count_accuracy: 0.7525\n    inv_length_vs_sc_p: 0.453\n    length_vs_sc_p: 0.153\n    inv_length_vs_sica_p: 0.864\n    length_vs_sica_p: 0.066\n    n_problems: 804\n    all_nonsignificant: true\n- exp_id: exp-010-mistral\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-011-llama8b-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-018-arc\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.5667\n    sc_accuracy: 0.5333\n    delta_pp: 3.33\n    mcnemar_chi2: 0.5\n    mcnemar_p: n.s.\n    bootstrap_ci_95:\n    - 0\n    - 8.33\n    bootstrap_p_delta_le_0: 0.1346\n    multi_candidate_rate: 0.1\n    contradiction_detected: 5\n    extraction_rate_problem: 1\n    extraction_rate_trace: 0.704\n    discordant_sica_wins: 2\n    discordant_sc_wins: 0\n- exp_id: pilot-constraint-filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 43\n    thresholds_tested:\n    - 1\n    - 2\n    - 3\n    - 5\n    - 7\n    best_gap_pp: 2.33\n    best_T: 1\n    sica_T1: 0.7674\n    sc: 0.7442\n    T5_gap: 0\n    T7_gap: 0\n    discriminative_ratio_count: 0.115\n    discriminative_ratio_weight: 0.372\n    effective_flip_rate: 0.174\n    multi_answer_problems: 23\n    unanimous_problems: 20\n    problems_disc_favors_different: 4\n- exp_id: exp-018-arc-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.95\n    sc_accuracy: 0.9667\n    delta_pp: -1.67\n    multi_candidate_rate: 0.05\n    extraction_rate: 1\n    contradiction_detected: 3\n    discordant_sica_wins: 0\n    discordant_sc_wins: 1\n    dataset: ARC-Challenge\n    model: Qwen2.5-14B-Instruct\n- exp_id: exp-011-llama8b-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6667\n    sc_accuracy: 0.6\n    delta_pp: 6.67\n    multi_candidate_rate: 0.6167\n    extraction_rate: 0.8556\n    answer_extraction_rate: 0.8958\n    contradiction_rate: 0.0527\n    problems_with_contradictions: 43\n    truncated_traces: 44\n    discordant_sica_wins: 5\n    discordant_sc_wins: 1\n    mcnemar_p: 0.2188\n    proofwriter_sica: 0.6333\n    proofwriter_sc: 0.6\n    proofwriter_delta_pp: 3.33\n    folio_sica: 0.7\n    folio_sc: 0.6\n    folio_delta_pp: 10\n    model: LLaMA-3.1-8B-Instruct\n    dataset: D012\n    wall_time_min: 66.4\n- exp_id: pilot-contrastive-prompt\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- exp_id: exp-019-llama8b-strategyqa-200\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    k: 12\n    sica_accuracy: 0.74\n    sc_accuracy: 0.72\n    delta_pp: 2\n    multi_candidate_rate: 0.41\n    mcnemar_p: 0.424\n    bootstrap_ci_95:\n    - -1.5\n    - 5.5\n    bootstrap_p_delta_le_0: 0.12\n    discordant_sica_wins: 9\n    discordant_sc_wins: 5\n    discordant_total: 14\n    discordant_rate: 0.07\n    sc_unanimous_rate: 0.545\n    model: LLaMA-3.1-8B-Instruct\n    dataset: StrategyQA\n    wall_time_min: 52\n- exp_id: exp-020-llama8b-folio-204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.608\n    sc_accuracy: 0.632\n    delta_pp: -2.45\n    mcnemar_p: 0.2668\n    bootstrap_ci_95:\n    - -5.88\n    - 0.98\n    bootstrap_p_sica_ge_sc: 0.1\n    discordant_sica_wins: 4\n    discordant_sc_wins: 9\n    discordant_total: 13\n    discordant_rate: 0.064\n    multi_candidate_rate: 0.618\n    extraction_rate: 0.942\n    answer_extraction_rate: 0.951\n    contradiction_rate: 0.062\n    both_wrong: 71\n    model: LLaMA-3.1-8B-Instruct\n    dataset: FOLIO-204\n    wall_time_min: 131.7\n- exp_id: exp-009-overhead-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 804\n    mean_total_wall_s: 61.6\n    mean_trace_gen_s: 31.6\n    trace_gen_pct: 51.3\n    mean_extract_s: 29\n    extract_pct: 47\n    mean_dedup_s: 1\n    dedup_pct: 1.6\n    mean_maxsat_s: 0.003\n    maxsat_pct: 0.005\n    sica_overhead_s: 30\n    sica_overhead_pct: 48.7\n    pw_overhead_pct: 51.3\n    folio_overhead_pct: 38.6\n    p50_overhead_pct: 48.9\n    p90_overhead_pct: 57.6\n- exp_id: exp-014-deepseek-r1-7b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6833\n    sc_accuracy: 0.7167\n    delta_pp: -3.33\n    multi_candidate_rate: 0.583\n    extraction_rate: 0.839\n    answer_extraction_rate: 0.939\n    truncated_traces: 72\n    contradiction_rate: 0.037\n    wall_time_min: 100.3\n    mcnemar_p: 0.4795\n    discordant_sica_wins: 0\n    discordant_sc_wins: 2\n    model: DeepSeek-R1-Distill-Qwen-7B\n    dataset: D012\n- exp_id: temperature-ablation-t03\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: temperature-ablation-t05\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: temperature-ablation-t10\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: temperature_ablation_t03_t05_t10\n  claim: Claim 1 (Capability Trap)\n  description: T=0.3/0.5/1.0 on Qwen-14B D012 60题。预期 T↑→C0↑ 但 gap 不变，证明 diversity\n    增加不改善 SICA。\n  estimated_gpu_hours: 3.0\n- name: gsm8k_pilot_30q\n  claim: Claim 2 (Operating Regime Empty)\n  description: Qwen-14B GSM8K 30题 pilot。数学推理域覆盖。预期 C0 低（14B 在 GSM8K 上 accuracy>80%）。\n  estimated_gpu_hours: 1.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T14:49:52.696Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T14:49:52.696Z",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83"
}
```

---

## Round 1

14 recorded events

### User

_source line 3 · 2026-05-17T14:49:52.718Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Capability trap 被结构性确认: diversity 可操控但 SICA 收益恒零; F2 per-problem 清晰展示 constraint 非判别性; 三条 claims 原样保留
核心假设：['Temperature ablation: C0 随 T 单调递增 (T=0.3 C0≈25-35%, T=1.0 C0≈60-75%), 所有条件 |Δ| ≤ 3pp, p > 0.20', "F2 per-problem (n≈307): constraint precision 均值 ≈ 0.50 (近随机), 与 vote_entropy 无相关 (slope ≈ 0) → scatter 可视化直接支撑 'regardless of diversity'", "exp-004 (7B) / exp-007 (72B) 产出至少 3 个 distinct C0 水平 (如 7B≈65%, 14B≈38%, 72B≈15%) → Claim 3 'diagnostic predictor' 成立", '所有已完成 + 新完成实验中零个正向 p < 0.10; discordant pair SICA winrate ≈ 50%', 'exp-013 MaxSAT ≈ count-only 已确认, 与 F2 per-problem 数据形成双重 mechanism evidence']
关键指标范围：{'temp_max_abs_delta_pp': [0, 3.0], 'f2_constraint_precision_mean': [0.48, 0.53], 'f2_precision_vs_entropy_slope': [-0.02, 0.02], 'aggregate_abs_weighted_delta_pp': [0, 0.8], 'n_exp_positive_p_below_010': 0, 'c0_scaling_distinct_levels': [3, 5], 'discordant_sica_winrate': [0.42, 0.55]}
叙事方向：原始 Capability Trap framing 完全成立。Temperature ablation 作为 §5 新证据: 'We experimentally manipulate diversity via temperature and confirm the trap holds at all levels — this is structural, not a tuning failure.' F2 hero figure per-problem scatter 清晰可读, 无需 binning。三条 claim 措辞不改。Title 保持 'The Capability Trap'。强 EMNLP main submission, contribution = mechanism identification + first systematic negative result + zero-cost diagnostic。

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
  "promptId": "6c00ffcb-4d3c-4fdd-8e45-b96e84d3f7da",
  "type": "user",
  "uuid": "5d890c78-5cfb-402f-a56a-02fd9443d842",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T14:49:52.717Z_

```json
{
  "parentUuid": "5d890c78-5cfb-402f-a56a-02fd9443d842",
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
  "uuid": "47ab4bc7-b75c-438e-8af1-78ecf15db506",
  "timestamp": "2026-05-17T14:49:52.717Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T14:49:52.717Z_

```json
{
  "parentUuid": "47ab4bc7-b75c-438e-8af1-78ecf15db506",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "03f90ffb-4a4b-437c-a40d-c20e5708d8a8",
  "timestamp": "2026-05-17T14:49:52.717Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Capability trap 被结构性确认: diversity 可操控但 SICA 收益恒零; F2 per-problem 清晰展示 constraint 非判别性; 三条 claims 原样保留 核心假设：['Temperature ablation: C0 随 T 单调递增 (T=0.3 C0≈25…",
  "leafUuid": "03f90ffb-4a4b-437c-a40d-c20e5708d8a8",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Temperature ablation validates capability trap mechanism",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83"
}
```

---

### Assistant

_source line 8 · 2026-05-17T14:49:56.608Z_

I'll analyze each planned experiment and generate detailed predictions consistent with the "best" tier definition. Let me first review the current state of completed experiments to calibrate my predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "03f90ffb-4a4b-437c-a40d-c20e5708d8a8",
  "isSidechain": false,
  "requestId": "req_011Cb8KvViEysH6stGPpypF3",
  "type": "assistant",
  "uuid": "7d65a2c8-4201-4fbb-9876-65a8f9fbd958",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013LbuEwr8Mk8sxy8kFpYRCu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18715,
      "cache_read_input_tokens": 11841,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 293,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18715
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

_source line 9 · 2026-05-17T14:50:02.387Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015sGrAfa1i6brQ4x8MkqM7W`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment data files",
  "prompt": "Search the repository at /home/ubuntu/.agent-ml-research-idea_gen_0513_3 for experiment result files, analysis scripts, and any temperature ablation data. I need to understand:\n1. Where raw experiment results are stored (look for directories like results/, experiments/, data/, outputs/)\n2. Any temperature ablation results that may already exist (the registry shows temperature-ablation-t03, t05, t10 as RUNNING)\n3. The F2 per-problem data from exp-001 (n≈307 multi-candidate problems)\n4. Any constraint quality / precision data\n\nSearch broadly - check YAML files, JSON files, CSV files, and Python analysis scripts. Report file paths and key content summaries."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d65a2c8-4201-4fbb-9876-65a8f9fbd958",
  "isSidechain": false,
  "requestId": "req_011Cb8KvViEysH6stGPpypF3",
  "type": "assistant",
  "uuid": "6485103f-c04d-4c1b-bd2b-9a7859d96d5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013LbuEwr8Mk8sxy8kFpYRCu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18715,
      "cache_read_input_tokens": 11841,
      "output_tokens": 293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18715,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 293,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18715,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18715
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

_source line 10 · 2026-05-17T14:51:23.506Z_

<details><summary>↩ Tool result · `toolu_015sGrAfa1i6brQ4x8MkqM7W`</summary>

````text
Perfect! Now I have comprehensive information. Let me compile the final report.

## Research Repository Analysis: Experiment Results & Temperature Ablation Status

### **1. RAW EXPERIMENT RESULTS STORAGE**

**Primary directories:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/` — Main experiment outputs
- `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/` — Worker execution logs and analysis results
- Server-side remote storage: `/root/symb_invariant_consensus/results/` on westd-32608 (AutoDL)

**Key experiment directories:**
- `/artifacts/exp-001/` — sica_expanded_14b (804 multi-dataset problems)
- `/artifacts/exp-009/` — Overhead analysis data
- `/artifacts/exp-010-mistral-v2/` — Mistral-7B cross-family validation
- `/artifacts/exp-011-llama8b/` — LLaMA-8B validation
- `/artifacts/exp-014/` — DeepSeek-R1-7B (RUNNING as of 2026-05-17)
- `/artifacts/exp-019/` — LLaMA-8B StrategyQA (constraint quality analysis)
- `/artifacts/exp-020/` — LLaMA-8B FOLIO (204 samples)

---

### **2. TEMPERATURE ABLATION STATUS**

**Registry entry (confirmed in global/registry.yaml):**

| Experiment ID | Temperature | Status | Created At | Updated At | Dataset |
|---|---|---|---|---|---|
| exp-021-temp-ablation-t03 | T=0.3 | PREPARING | 2026-05-17T12:01:51 | 2026-05-17T12:02:20 | Qwen2.5-14B on PW+FOLIO (60 problems) |
| exp-022-temp-ablation-t05 | T=0.5 | PREPARING | 2026-05-17T12:01:52 | 2026-05-17T12:02:22 | Qwen2.5-14B on PW+FOLIO (60 problems) |
| exp-023-temp-ablation-t10 | T=1.0 | PREPARING | 2026-05-17T12:01:52 | 2026-05-17T12:02:24 | Qwen2.5-14B on PW+FOLIO (60 problems) |

**Hypotheses:**
- T=0.3: Low diversity (C0 expected <30%) → SICA ≈ SC (constraint quality bottleneck)
- T=0.5: Medium diversity (C0 30-45%) → SICA ≈ SC (constraint quality insufficient)
- T=1.0: High diversity (C0 >60%) → SICA ≈ SC or worse (quality degradation cancels diversity gains)

**Setup files prepared:**
- Scripts location: `/projects/symb_invariant_consensus/scripts/`
  - `run_exp021_temp_t03.sh` — T=0.3 execution
  - `run_exp022_temp_t05.sh` — T=0.5 execution
  - `run_exp023_temp_t10.sh` — T=1.0 execution
- Model path: `/root/autodl-tmp/models/Qwen2.5-14B-Instruct`
- All scripts share: K=12, seed=42, max_tokens=4096, output to `results/exp0{21,22,23}_temp_t{0.3,0.5,1.0}/`

---

### **3. F2 PER-PROBLEM DATA (exp-001, n≈307 multi-candidate)**

**F2 metadata:**
- **File:** `/artifacts/exp-001/data/f2_per_problem_metadata.txt`
- **Remote location:** `/root/symb_invariant_consensus/analysis/f2_per_problem.csv`
- **Dimensions:** 307 rows (multi-candidate problems where n_unique_answers > 1)
- **Columns (13 total):**
  - problem_id, dataset, level, ground_truth
  - n_unique_answers, vote_entropy, constraint_count
  - constraint_exclusion_rate, sica_answer, sc_answer
  - sica_correct, sc_correct, sica_flipped

**F2 aggregated summary (quality_metrics.csv):**
- **File:** `/artifacts/quality_metrics.csv` and `/artifacts/_project/data/quality_metrics.csv`
- Contains constraint quality metrics across all experiments:

| Experiment | Model | Domain | N | SC Acc | SICA Acc | Δpp | C0 | Avg Unique Const | Density | Sat Ratio | Excl Rate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| exp001 | Qwen2.5-14B | PW+FOLIO | 804 | 76.24% | 76.49% | +0.25 | 3.9% | 21.5 | 9.17 | 0.977 | 0.023 |
| exp010 | Mistral-7B | PW+FOLIO | 60 | 48.33% | 48.33% | 0.0 | 6.7% | 20.5 | 5.47 | 0.948 | 0.052 |
| exp011 | LLaMA-8B | PW+FOLIO | 60 | 60.0% | 66.67% | +6.67 | 11.7% | 30.1 | 8.73 | 0.950 | 0.050 |
| exp017 | Qwen2.5-14B | StrategyQA | 60 | 53.33% | 56.67% | +3.33 | 3.3% | 1.0 | 1.02 | 0.954 | 0.046 |
| exp018 | Qwen2.5-14B | ARC | 60 | 96.67% | 95.0% | -1.67 | 1.7% | 1.1 | 1.02 | 0.975 | 0.025 |
| exp019 | LLaMA-8B | StrategyQA | 200 | 72.0% | 74.0% | +2.0 | 7.0% | 6.2 | 1.94 | 0.853 | 0.147 |
| exp020 | LLaMA-8B | FOLIO | 204 | 63.24% | 60.78% | -2.45 | 6.4% | 33.3 | 8.05 | 0.938 | 0.062 |

---

### **4. CONSTRAINT QUALITY & PRECISION DATA**

**Constraint quality analysis files:**

1. **exp019 Constraint Quality Analysis**
   - File: `/artifacts/exp-019/data/exp019_constraint_quality_pointer.txt`
   - Remote: `/root/symb_invariant_consensus/results/exp019_constraint_quality_analysis.json`
   - Remote: `/root/symb_invariant_consensus/results/exp019_constraint_quality_summary.csv`

2. **Quality Correlation Analysis (F2 metrics)**
   - Worker log: `/logs/workers/worker_analysis_constraint-quality-correlation_20260517T113142_result.json`
   - Summary: Spearman correlation analysis between C0 and constraint quality
   - **Key finding:** C0 vs satisfied_ratio ρ = -0.64 (p=0.13); C0 vs constraint_density r = +0.79 (p=0.04)
   - **Interpretation:** High C0 generates more constraints but lower quality (capability trap)

3. **Overhead Analysis (exp-009)**
   - File: `/artifacts/exp-009/data/overhead_analysis.json`
   - **Total SICA overhead:** 94.8% over SC baseline (31 sec/problem trace gen; 29 sec/problem constraint extraction)
   - **MaxSAT solver time:** Negligible (0.0026 sec/problem, 4.3e-05% of total)
   - **Breakdown:** 51.3% trace generation, 47.0% constraint extraction, 1.6% deduplication, ~0% solver

---

### **5. ANALYSIS SCRIPTS & PYTHON TOOLS**

**Execution scripts:**
- `/artifacts/run_mvp.py` — MVP pipeline runner
- `/artifacts/run_full_mvp.py` — Full-scale MVP pipeline
- Various shell scripts in `/artifacts/`: `run_exp017_strategyqa.sh`, `run_exp018_arc.sh`, `launch_mvp.sh`

**Analysis outputs (JSON/CSV):**
- `/artifacts/sica_k_sensitivity_14b/k_sensitivity_report.json` — K ablation analysis
- `/artifacts/exp-005/data/operating_regime_data.json` — QwQ-32B regime analysis
- `/artifacts/folio_c0_precheck_raw.json` — Diversity precheck data
- `/artifacts/_project/data/exp019_constraint_quality_analysis_c0_fixed.json` — Detailed constraint metrics

**Key analysis reports:**
- `/artifacts/exp-014/report/exp014_analysis.md` — DeepSeek-R1-7B negative result (C0=58.3% falsifies reasoning-model determinism hypothesis)
- `/artifacts/sica_expanded_14b/report/exp001_analysis_summary.txt` — Main exp-001 summary (804 problems)
- `/artifacts/_project/report/d016_model_pivot_report.md` — Infrastructure/model deployment log

---

### **6. CRITICAL FINDINGS SUMMARY**

**exp-001 Results (n=804, Qwen2.5-14B, PW+FOLIO):**
- SICA: 76.49% vs SC: 76.24% → **+0.25pp (NOT significant, p=0.7433)**
- Multi-candidate (307 problems): SICA 59.61% vs SC 58.96% → +0.65pp
- Unanimous (497 problems): 0.0pp delta
- **Key metric:** 65% of disagreements are SC ties (evidence for tiebreak-only mechanism)

**Constraint Quality Insight (exp-019 correlation analysis):**
- Logical domains (PW+FOLIO, FOLIO): Constraint density 5-9/trace, but high density ≠ high SICA gain
- Common-sense domains (StrategyQA, ARC): Constraint density ~1 (nearly impossible to extract symbolic constraints)
- **Sweet spot (LLaMA-8B PW+FOLIO):** High C0 (61.7%) + moderate constraint density (8.73) → +6.67pp gain
- **Counter-example (LLaMA-8B FOLIO only):** Same model, same domain, n=204 → -2.45pp (exp-011 +6.7pp is n=30 noise)

---

### **FILE STRUCTURE QUICK REFERENCE**

```
artifacts/
├── exp-001/data/f2_per_problem_metadata.txt
├── exp-009/data/overhead_analysis.json
├── exp-014/report/exp014_analysis.md
├── exp-019/data/exp019_constraint_quality_pointer.txt
├── exp-020/data/
├── sica_expanded_14b/
│   ├── data/sica_expanded_14b_config.txt
│   └── report/exp001_analysis_summary.txt
├── _project/data/
│   ├── quality_metrics.csv
│   ├── exp019_constraint_quality_analysis_c0_fixed.json
│   └── exp019_constraint_quality_summary_c0_fixed.csv
└── quality_metrics.csv
```

All temperature ablation scripts are prepared but still in PREPARING state. Remote data on westd-32608 requires SSH access to `/root/symb_invariant_consensus/results/`.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "6485103f-c04d-4c1b-bd2b-9a7859d96d5a",
  "isSidechain": false,
  "promptId": "6c00ffcb-4d3c-4fdd-8e45-b96e84d3f7da",
  "type": "user",
  "uuid": "02a6e9a4-c295-4fd7-80b1-3cdfad5c3067",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the repository at /home/ubuntu/.agent-ml-research-idea_gen_0513_3 for experiment result files, analysis scripts, and any temperature ablation data. I need to understand:\n1. Where raw experiment results are stored (look for directories like results/, experiments/, data/, outputs/)\n2. Any temperature ablation results that may already exist (the registry shows temperature-ablation-t03, t05, t10 as RUNNING)\n3. The F2 per-problem data from exp-001 (n≈307 multi-candidate problems)\n4. Any constraint quality / precision data\n\nSearch broadly - check YAML files, JSON files, CSV files, and Python analysis scripts. Report file paths and key content summaries.",
    "agentId": "ad27df6e0f3d8e566",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information. Let me compile the final report.\n\n## Research Repository Analysis: Experiment Results & Temperature Ablation Status\n\n### **1. RAW EXPERIMENT RESULTS STORAGE**\n\n**Primary directories:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/` — Main experiment outputs\n- `/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/logs/workers/` — Worker execution logs and analysis results\n- Server-side remote storage: `/root/symb_invariant_consensus/results/` on westd-32608 (AutoDL)\n\n**Key experiment directories:**\n- `/artifacts/exp-001/` — sica_expanded_14b (804 multi-dataset problems)\n- `/artifacts/exp-009/` — Overhead analysis data\n- `/artifacts/exp-010-mistral-v2/` — Mistral-7B cross-family validation\n- `/artifacts/exp-011-llama8b/` — LLaMA-8B validation\n- `/artifacts/exp-014/` — DeepSeek-R1-7B (RUNNING as of 2026-05-17)\n- `/artifacts/exp-019/` — LLaMA-8B StrategyQA (constraint quality analysis)\n- `/artifacts/exp-020/` — LLaMA-8B FOLIO (204 samples)\n\n---\n\n### **2. TEMPERATURE ABLATION STATUS**\n\n**Registry entry (confirmed in global/registry.yaml):**\n\n| Experiment ID | Temperature | Status | Created At | Updated At | Dataset |\n|---|---|---|---|---|---|\n| exp-021-temp-ablation-t03 | T=0.3 | PREPARING | 2026-05-17T12:01:51 | 2026-05-17T12:02:20 | Qwen2.5-14B on PW+FOLIO (60 problems) |\n| exp-022-temp-ablation-t05 | T=0.5 | PREPARING | 2026-05-17T12:01:52 | 2026-05-17T12:02:22 | Qwen2.5-14B on PW+FOLIO (60 problems) |\n| exp-023-temp-ablation-t10 | T=1.0 | PREPARING | 2026-05-17T12:01:52 | 2026-05-17T12:02:24 | Qwen2.5-14B on PW+FOLIO (60 problems) |\n\n**Hypotheses:**\n- T=0.3: Low diversity (C0 expected <30%) → SICA ≈ SC (constraint quality bottleneck)\n- T=0.5: Medium diversity (C0 30-45%) → SICA ≈ SC (constraint quality insufficient)\n- T=1.0: High diversity (C0 >60%) → SICA ≈ SC or worse (quality degradation cancels diversity gains)\n\n**Setup files prepared:**\n- Scripts location: `/projects/symb_invariant_consensus/scripts/`\n  - `run_exp021_temp_t03.sh` — T=0.3 execution\n  - `run_exp022_temp_t05.sh` — T=0.5 execution\n  - `run_exp023_temp_t10.sh` — T=1.0 execution\n- Model path: `/root/autodl-tmp/models/Qwen2.5-14B-Instruct`\n- All scripts share: K=12, seed=42, max_tokens=4096, output to `results/exp0{21,22,23}_temp_t{0.3,0.5,1.0}/`\n\n---\n\n### **3. F2 PER-PROBLEM DATA (exp-001, n≈307 multi-candidate)**\n\n**F2 metadata:**\n- **File:** `/artifacts/exp-001/data/f2_per_problem_metadata.txt`\n- **Remote location:** `/root/symb_invariant_consensus/analysis/f2_per_problem.csv`\n- **Dimensions:** 307 rows (multi-candidate problems where n_unique_answers > 1)\n- **Columns (13 total):**\n  - problem_id, dataset, level, ground_truth\n  - n_unique_answers, vote_entropy, constraint_count\n  - constraint_exclusion_rate, sica_answer, sc_answer\n  - sica_correct, sc_correct, sica_flipped\n\n**F2 aggregated summary (quality_metrics.csv):**\n- **File:** `/artifacts/quality_metrics.csv` and `/artifacts/_project/data/quality_metrics.csv`\n- Contains constraint quality metrics across all experiments:\n\n| Experiment | Model | Domain | N | SC Acc | SICA Acc | Δpp | C0 | Avg Unique Const | Density | Sat Ratio | Excl Rate |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n| exp001 | Qwen2.5-14B | PW+FOLIO | 804 | 76.24% | 76.49% | +0.25 | 3.9% | 21.5 | 9.17 | 0.977 | 0.023 |\n| exp010 | Mistral-7B | PW+FOLIO | 60 | 48.33% | 48.33% | 0.0 | 6.7% | 20.5 | 5.47 | 0.948 | 0.052 |\n| exp011 | LLaMA-8B | PW+FOLIO | 60 | 60.0% | 66.67% | +6.67 | 11.7% | 30.1 | 8.73 | 0.950 | 0.050 |\n| exp017 | Qwen2.5-14B | StrategyQA | 60 | 53.33% | 56.67% | +3.33 | 3.3% | 1.0 | 1.02 | 0.954 | 0.046 |\n| exp018 | Qwen2.5-14B | ARC | 60 | 96.67% | 95.0% | -1.67 | 1.7% | 1.1 | 1.02 | 0.975 | 0.025 |\n| exp019 | LLaMA-8B | StrategyQA | 200 | 72.0% | 74.0% | +2.0 | 7.0% | 6.2 | 1.94 | 0.853 | 0.147 |\n| exp020 | LLaMA-8B | FOLIO | 204 | 63.24% | 60.78% | -2.45 | 6.4% | 33.3 | 8.05 | 0.938 | 0.062 |\n\n---\n\n### **4. CONSTRAINT QUALITY & PRECISION DATA**\n\n**Constraint quality analysis files:**\n\n1. **exp019 Constraint Quality Analysis**\n   - File: `/artifacts/exp-019/data/exp019_constraint_quality_pointer.txt`\n   - Remote: `/root/symb_invariant_consensus/results/exp019_constraint_quality_analysis.json`\n   - Remote: `/root/symb_invariant_consensus/results/exp019_constraint_quality_summary.csv`\n\n2. **Quality Correlation Analysis (F2 metrics)**\n   - Worker log: `/logs/workers/worker_analysis_constraint-quality-correlation_20260517T113142_result.json`\n   - Summary: Spearman correlation analysis between C0 and constraint quality\n   - **Key finding:** C0 vs satisfied_ratio ρ = -0.64 (p=0.13); C0 vs constraint_density r = +0.79 (p=0.04)\n   - **Interpretation:** High C0 generates more constraints but lower quality (capability trap)\n\n3. **Overhead Analysis (exp-009)**\n   - File: `/artifacts/exp-009/data/overhead_analysis.json`\n   - **Total SICA overhead:** 94.8% over SC baseline (31 sec/problem trace gen; 29 sec/problem constraint extraction)\n   - **MaxSAT solver time:** Negligible (0.0026 sec/problem, 4.3e-05% of total)\n   - **Breakdown:** 51.3% trace generation, 47.0% constraint extraction, 1.6% deduplication, ~0% solver\n\n---\n\n### **5. ANALYSIS SCRIPTS & PYTHON TOOLS**\n\n**Execution scripts:**\n- `/artifacts/run_mvp.py` — MVP pipeline runner\n- `/artifacts/run_full_mvp.py` — Full-scale MVP pipeline\n- Various shell scripts in `/artifacts/`: `run_exp017_strategyqa.sh`, `run_exp018_arc.sh`, `launch_mvp.sh`\n\n**Analysis outputs (JSON/CSV):**\n- `/artifacts/sica_k_sensitivity_14b/k_sensitivity_report.json` — K ablation analysis\n- `/artifacts/exp-005/data/operating_regime_data.json` — QwQ-32B regime analysis\n- `/artifacts/folio_c0_precheck_raw.json` — Diversity precheck data\n- `/artifacts/_project/data/exp019_constraint_quality_analysis_c0_fixed.json` — Detailed constraint metrics\n\n**Key analysis reports:**\n- `/artifacts/exp-014/report/exp014_analysis.md` — DeepSeek-R1-7B negative result (C0=58.3% falsifies reasoning-model determinism hypothesis)\n- `/artifacts/sica_expanded_14b/report/exp001_analysis_summary.txt` — Main exp-001 summary (804 problems)\n- `/artifacts/_project/report/d016_model_pivot_report.md` — Infrastructure/model deployment log\n\n---\n\n### **6. CRITICAL FINDINGS SUMMARY**\n\n**exp-001 Results (n=804, Qwen2.5-14B, PW+FOLIO):**\n- SICA: 76.49% vs SC: 76.24% → **+0.25pp (NOT significant, p=0.7433)**\n- Multi-candidate (307 problems): SICA 59.61% vs SC 58.96% → +0.65pp\n- Unanimous (497 problems): 0.0pp delta\n- **Key metric:** 65% of disagreements are SC ties (evidence for tiebreak-only mechanism)\n\n**Constraint Quality Insight (exp-019 correlation analysis):**\n- Logical domains (PW+FOLIO, FOLIO): Constraint density 5-9/trace, but high density ≠ high SICA gain\n- Common-sense domains (StrategyQA, ARC): Constraint density ~1 (nearly impossible to extract symbolic constraints)\n- **Sweet spot (LLaMA-8B PW+FOLIO):** High C0 (61.7%) + moderate constraint density (8.73) → +6.67pp gain\n- **Counter-example (LLaMA-8B FOLIO only):** Same model, same domain, n=204 → -2.45pp (exp-011 +6.7pp is n=30 noise)\n\n---\n\n### **FILE STRUCTURE QUICK REFERENCE**\n\n```\nartifacts/\n├── exp-001/data/f2_per_problem_metadata.txt\n├── exp-009/data/overhead_analysis.json\n├── exp-014/report/exp014_analysis.md\n├── exp-019/data/exp019_constraint_quality_pointer.txt\n├── exp-020/data/\n├── sica_expanded_14b/\n│   ├── data/sica_expanded_14b_config.txt\n│   └── report/exp001_analysis_summary.txt\n├── _project/data/\n│   ├── quality_metrics.csv\n│   ├── exp019_constraint_quality_analysis_c0_fixed.json\n│   └── exp019_constraint_quality_summary_c0_fixed.csv\n└── quality_metrics.csv\n```\n\nAll temperature ablation scripts are prepared but still in PREPARING state. Remote data on westd-32608 requires SSH access to `/root/symb_invariant_consensus/results/`."
      }
    ],
    "totalDurationMs": 81108,
    "totalTokens": 63116,
    "totalToolUseCount": 51,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 57999,
      "output_tokens": 3058,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2053
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 3058,
          "cache_read_input_tokens": 57999,
          "cache_creation_input_tokens": 2053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2053,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 21,
      "searchCount": 0,
      "bashCount": 30,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "6485103f-c04d-4c1b-bd2b-9a7859d96d5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---

### Assistant

_source line 11 · 2026-05-17T15:03:24.965Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive data to generate detailed predictions for each planned experiment in the "best" tier. Let me go through each experiment systematically.

Key calibration points from completed experiments:
- exp-001 (Qwen-14B, PW+FOLIO, n=804): C0=38.18%, Δ=+0.25pp, p=0.7433
- exp-010 (Mistral-7B, D012, n=60): C0=50%, Δ=0.0pp, p=1.0
- exp-011 (LLaMA-8B, D012, n=60): C0=61.7%, Δ=+6.67pp, p=0.2188 (noise at n=60)


- exp-014 (DeepSeek-R1-7B, D012, n=60): C0=58.3%, Δ=-3.33pp, p=0.4795
- exp-017 (Qwen-14B, StrategyQA, n=60): C0=10%, Δ=+3.33pp, n.s.
- exp-018 (Qwen-14B, ARC, n=60): C0=5%, Δ=-1.67pp
- exp-019 (LLaMA-8B, StrategyQA, n=200): C0=41%, Δ=+2.0pp

I'm now looking at the full set of calibration results across different model-dataset combinations to establish baseline performance and effect sizes before making predictions for the remaining experiments.

For the temperature ablation in the best-performing tier, I'm seeing that baseline calibration increases monotonically with temperature, ranging from about 25-35% at T=0.3 up to 60-75% at T=1.0, with all effect sizes staying small and non-significant. The constraint precision metric across problems averages around 50%, which suggests moderate discriminative power in the weighted constraint approach.

Looking at the remaining results, there's no meaningful correlation between constraint effectiveness and vote entropy, while both the 7B and 72B models generate at least three distinct calibration levels. Across all experiments, I haven't found any positive effects reaching statistical significance, and the discordant pair analysis shows the SICA method performing at chance level around 50% winrate.

Now I'm mapping out which planned experiments are still pending—most of the core ablations like K sensitivity and the 7B/72B scaling studies are either completed or essentially done, though I still need to finalize the diagnostic validation and case analysis work. I'm seeing a discrepancy between the experiment plan statuses and what's actually recorded in the registry. Most experiments are marked as "planned" in the plan itself, but many of them show as completed in the actual registry. Let me cross-reference these to identify which ones genuinely still need detailed predictions versus which ones have already been executed.

There are also some what_if experiments to account for like the temperature ablation and GSM8K pilot. The key insight here is that I need to generate predictions for all the planned experiments from the experiment plan document, regardless of whether they've already been run. For the ones that are already done, I should create predictions that align with what "best-tier" results would look like, since that's what the user is asking for. I need to generate predicted results for all the planned experiments that align with the "best" tier framing. Let me work through each one systematically—for experiments already completed, I'll use the actual results if they're consistent with best-tier expectations, otherwise I'll predict what best-tier results would look like.

For each experiment, I'm compiling the core components: the experiment identifier and plan reference, what we're testing, what outcomes we'd expect to see, the reasoning behind those predictions, and how to present the findings through tables and visualizations. The K ablation already has registry data showing SICA performing at or below SC across all K values, so I'll use that as the baseline for how best-tier results should look.

The tiebreak baseline is marked complete with SICA achieving 80% accuracy versus 50% random and 60% alphabetical, though the practical impact is limited since ties are infrequent. For the 7B scaling experiment, I need to establish at least three distinct C0 levels where the weaker model shows higher disagreement rates around 65%, which would support the diagnostic claim even if constraints themselves remain non-discriminative.

Moving through the remaining experiments: QwQ-32B confirms the method degenerates at very low C0 levels around 2.6%, and I'm plotting C0 against gap across conditions to show how the relationship flattens for high-C0 scenarios but exhibits a step function below 5%. The 72B-AWQ model demonstrates that stronger models produce lower C0 around 15%, which still prevents SICA from meaningfully diverging from SC. I'm also examining case studies to verify that constraints are syntactically sound but semantically uninformative, and checking the computational overhead analysis.

For the LLaMA-8B experiment at n=60, the +6.67pp gain isn't statistically significant at p=0.22, which aligns with what larger sample experiments show—essentially zero effect. Now I'm looking more closely at the per-problem constraint precision data, which hovers near 0.50 suggesting near-random performance, and I need to examine the slope patterns across these conditions.

For the temperature ablation, I'm trying to reconcile the what_if predictions with the best tier estimates—T=0.3 gives C0 around 25-35%, T=1.0 gives 60-75%, and I need to figure out where T=0.5 should fall in that range.

Now I'm noticing a discrepancy in the C0 values: the multi_candidate_rate from exp-001 shows 38.18% at T=0.7, but the quality_metrics table lists 3.9%—these are measuring different things, so I need to clarify which metric I'm actually using before writing up the results. I'm realizing the C0 column is actually the discordant rate between SICA and SC, not the multi-candidate rate—exp-019 shows discordant_rate = 7% matching C0 = 7.0%, and exp-020 shows 6.4% matching perfectly. The actual multi-candidate rates are much higher, ranging from 5% to 61.7% across the experiments.

Now I'm tracking the baseline multi-candidate rates for my temperature predictions: the Qwen-14B baseline at T=0.7 gives around 38% on the combined dataset and 53% on the D012 60-question subset, so I'd expect lower diversity at T=0.3 (roughly 25-35% C0) and higher at T=0.7.

Looking at what constraint precision ≈ 0.50 actually means—with 12 traces per problem and constraints extracted from each, a precision of 0.50 suggests the constraints are essentially random and can't distinguish correct answers from incorrect ones, which is the key evidence for the capability trap mechanism.

Now I'm compiling the full YAML with all planned experiments and what-if scenarios. I need to organize predictions for each experiment in YAML format. For the 7B model, I'm expecting much higher C0 around 65% since it's weaker and will have more disagreement, with SICA and SC accuracy both in the 55-60% range and minimal improvement. For the 72B-AWQ variant, the stronger model should push C0 down significantly to 15-20%, well below the 14B baseline.

Looking at the three distinct C0 levels across the Qwen family—7B at 65%, 14B at 38%, and 72B at 15%—this creates a clear progression that supports the claim about distinct performance tiers. Now I'm moving into the GSM8K pilot experiment.

For the 14B model on GSM8K, it performs exceptionally well with over 80% accuracy, but this confidence actually leads to low diversity in the C0 metric, which drops below 20%. This is interesting because it shows that when the model is highly confident, the self-consistency approach essentially degenerates—SICA becomes equivalent to SC. This validates C0 as a useful diagnostic tool for identifying when diversity breaks down.

I'm also examining the Logic-LM baseline approach, where applying verification K times followed by majority voting doesn't provide the expected benefits. The prediction is that Logic-LM-K, SC, and SICA all converge to similar performance, suggesting that single-trace FOL verification doesn't meaningfully improve the method.

For the temperature ablation study, I'm looking at how different temperature settings affect C0: at T=0.3, C0 is around 28% with minimal change and no statistical significance.  At T=0.5, C0 rises to about 40% with essentially no performance delta, and at T=1.0, C0 reaches 68% with a slight negative delta that's also not significant. The GSM8K pilot confirms the pattern—C0 stays very low at 10-15% because the 14B model is so strong on this task, and again SICA matches SC, reinforcing C0's value as a zero-cost diagnostic.

Now I'm analyzing the per-problem constraint precision data from the CPU constraint quality correlation experiment. Across the best tier, constraint precision hovers around 50% regardless of conditions, and there's no meaningful correlation between C0 and constraint precision.

I need to carefully map which experiments from the plan are actually "planned" status versus already done, so I can generate the right YAML output. Let me go through the list—exp-001 is done so I'll skip it, but exp-002 through exp-009 are all planned and should be included, and I need to check the rest of the list to see which ones are still pending. I'm realizing the key distinction here—I should generate predictions for what the best tier would achieve across all experiments, using the registry results as calibration points where they exist. For experiments already completed, I can cross-reference the actual outcomes to ensure my predictions stay grounded, but the goal is to construct a coherent best-tier performance profile in YAML format. There's a nuance with how to handle cases where the plan and registry diverge on specifics, like exp-011's actual configuration versus what was originally planned. At n=60 with roughly 4 discordant pairs expected, a 50/50 split would mean 2 wins each, giving Δ = 0pp. I'm realizing the best tier constraint on aggregate weighted delta allows individual experiments to show noise-driven variation up to around ±3pp, but the key requirement is that no single experiment should have p < 0.10. Let me use this to refine what best tier actually looks like.

Now I'm checking the specific constraints: temperature delta capped at 3pp, precision mean between 0.48-0.53, the precision-entropy slope nearly flat, aggregate delta under 0.8pp, and the discordant SICA winrate should land between 42-55% across all experiments combined. I'm starting to compute what the current combined winrate looks like by pulling the discordant results from each experiment.

Looking at the individual experiment results, I'm seeing some outliers like exp-011-v3 at 83% and exp-017-v3 at 100%, but when I combine all the data excluding exp-001, I get 22 SICA wins and 20 SC wins, which gives me 52.4%—right in the target range. Now I need to estimate what exp-001 contributes to see if including it keeps me within bounds, given its sample size of 804 problems and SICA accuracy of 59.61%. I need to reconcile the experiment naming issue—the plan's exp-019 describes a CPU-only analysis examining constraint precision correlations, but the registry has exp-019 as a GPU experiment on Llama 8B with StrategyQA. They're different analyses sharing the same ID, so I'll need to be careful about which one I'm referencing when generating the best-tier predictions. I'm noticing there's a mismatch between the plan's exp-019 (constraint quality correlation analysis) and the registry's exp-019 (LLaMA-8B StrategyQA experiment) — they're different experiments sharing the same base ID. For my predictions, I'll use the plan's definition since that's what the claims reference. The same pattern applies to exp-011 and other entries where the plan and registry diverge. Now I'll draft the output following the plan's structure and including specific metrics. I'm cross-referencing the K ablation results against the existing sensitivity data—at K=12 the gap drops to -5 percentage points, which seems steep, so I need to verify this against the best tier constraints that limit aggregate weighted delta to 0.8pp and require no individual experiments showing positive SICA gains below p=0.10. The pattern across all K values should confirm that SICA never outperforms SC significantly, which aligns with the capability trap finding.

For the 7B model, I'm checking the baseline accuracy claims: the 14B C0 rate is 38.18% on the full set but 53.3% on the smaller D012 subset, so I need to calibrate the 7B SICA-SC delta around -1 to +1pp with p>0.50 to match the noise injection interpretation where smaller models show minimal gains. I'm settling on the D012 baseline values to establish the three distinct C0 levels across the Qwen models, then cross-referencing with the specific accuracy metrics for each tier to finalize the performance deltas. Looking at the temperature ablation results across different settings on the dataset, I'm seeing a clear pattern where lower temperatures reduce diversity—at T=0.3, C0 drops to 28% with SC and SICA converging around 75%, while higher temperatures like T=1.0 push C0 up to 68% but cause both metrics to drop and diverge slightly. The core issue with Logic-LM appears to be constraint quality rather than how those constraints are aggregated during verification.

For the GSM8K experiment, the model achieves very high accuracy (~85-90%) on this dataset, which means C0 stays low around 10-15% due to the model's confidence, and SICA essentially matches SC since there's little room for improvement. Now I need to map out which results go into each table and figure for the final write-up.

I'm checking the consistency constraints across all experiments: positive deltas need p-values below 0.10, aggregate weighted differences should stay under 0.8 percentage points, SICA's win rate across experiments should hover between 42-55%, temperature ablations capped at 3 percentage points, constraint precision around 50%, and at least three distinct C0 levels for the scaling analysis. Let me construct the complete YAML output with these constraints in mind. through my predictions:

Experiments with Δ predictions:
- exp-002 K=6: 0, K=8: -1.7, K=11: 0, K=12: -3.3, K=16: -3.3, K=20: -3.3
- exp-004 (7B): -1.7pp
- exp-005 (QwQ): 0pp
- exp-007 (72B): 0pp
- exp-011 (LLaMA-8B D012 n=60): +3.3pp
- exp-012 (GSM8K): 0pp
- exp-013 (ablation): MaxSAT 76.5%, count 76.6%, random 76.4%, SC 76.2%
- exp-014 (DeepSeek): -3.3pp
- exp-015 (Logic-LM): ≈ SC
- exp-016 (Weighted SC): all ≈ SC
- exp-017 (StrategyQA n=60): +3.3pp
- exp-018 (ARC n=60): -1.7pp

I'm also testing different temperature settings, where T=0.3 shows a modest +1pp gain, T=0.5 stays flat, and T=1.0 drops by 2pp. Now I need to verify whether any of these positive deltas are statistically significant. Checking the p-values: both exp-011 and exp-017 show +3.3pp improvements but with p-values around 0.30-0.35 given the small sample sizes, so they're not significant. The temperature effect at T=0.3 is also not significant with p > 0.50. Moving on to examine the discordant win rates across all experiments using the best tier predictions. Looking at the temperature variation experiments, they show minimal differences across the range tested. Tallying everything up, I'm getting around 33 SICA wins versus 36 SC wins across 69 discordant cases, which puts the overall winrate at 48%—right in the expected confidence interval. The aggregate weighted delta is heavily influenced by the larger experiments, particularly exp-001 with its substantial sample size and modest positive effect, while exp-019 and exp-020 pull in opposite directions, though the smaller n=60 studies contribute little to the overall picture.

Computing the weighted average across all experiments, the large samples dominate the calculation and push the aggregate delta to roughly +0.07pp, which comfortably falls within the acceptable range. This gives me confidence the results are internally consistent. Now I need to be precise about which experiments feed into the aggregate metrics for the YAML output—specifically, the aggregate weighted delta should span all experiments, and I should verify that no single experiment crosses the significance threshold.

Looking at the YAML structure, each experiment entry needs a name, plan ID, description, expected results as a metric dictionary, a rationale explaining why those results make sense, references to any tables and figures, and an analysis section. The rationale is particularly important since it tells the user the reasoning behind the projected outcomes.

For the K ablation experiment, I'm using the sensitivity data already in the registry to project realistic results across different K values, showing where SICA and SC converge or diverge based on the actual patterns observed. The actual K ablation data confirms the best tier pattern—SICA stays at or below SC across all K values, with odd K showing zero gaps since the mechanism relies purely on tiebreaking. For the tiebreak baseline, SICA achieves 80% accuracy on tied questions compared to random's 50%, and since ties represent about 17% of problems, this explains the performance difference in that tier.

Now I need to clarify which experiments are already complete with registry data versus which need predictions. I'll use actual results for the done experiments and construct reasonable best-tier predictions for the remaining ones, being careful to match the actual model names from the registry rather than the plan notes. v3, exp-011-v3, exp-013, exp-014, exp-016, exp-017-v3, exp-018-v2

Still need predictions: exp-004, exp-006, exp-007, exp-008, exp-012, exp-015, exp-019 (constraint quality correlation), temperature_ablation, gsm8k_pilot

For already done experiments, I'll check if actuals fit best tier and use them. For undone ones, I'll generate best-tier predictions.

Let me organize this more efficiently. I'll write the YAML directly now.

Let me focus on giving concise but complete predictions. The key unique value I provide is the result_rationale for each experiment - explaining WHY the best tier would produce these specific numbers.

OK let me just write it out. Here goes:

I'll compose the full YAML in my response. Let me structure it clearly.

Now for the temperature ablation experiments that are still running, I'm predicting the best-tier outcomes. At lower temperatures like 0.3, the model becomes more deterministic so fewer problems have multiple valid candidates, keeping constraint discrimination low. As temperature increases to 0.5 and beyond, we get more diversity in outputs, but the constraints remain non-discriminative across the range since the underlying quality doesn't improve. Looking at the performance across different temperatures, I'm seeing a clear pattern where lower temperatures maintain higher constraint accuracy while keeping SC accuracy stable around 73-77%, with the delta staying near zero across the board. Now I'm looking at the constraint quality metrics from the F2 analysis—precision hovers around 0.50 across domains with essentially zero correlation to diversity or entropy, which confirms that constraints simply aren't discriminative regardless of how much variation we introduce. The qualitative case studies show the constraints are syntactically valid FOL but lack the semantic power to actually guide the model.

For the Logic-LM baseline, I'm predicting it won't outperform the aggregation methods because the fundamental bottleneck is constraint quality itself—even with independent trace verification, we're still relying on the same non-discriminative constraints. And for the C0 diagnostic, I expect to see a flat line showing no gap between SICA and SC when constraint quality is above the threshold, then they converge when quality drops below 5%.

Now I'm ready to compile the full experiment list into YAML, making sure I capture all the planned experiments comprehensively. I'm working through how to handle the experiments that already have real data in the registry versus those that need predictions. For the ones with actual results, I should report those as-is since they're facts, not predictions. For the rest, I'll generate what the best tier would predict, making sure the numeric values stay consistent across the YAML structure.

Now I'm thinking through exp-011-v3's +6.67pp result—it's technically consistent with the best tier's prediction of no positive effects (p=0.22 is well above the 0.10 threshold), so even though it looks large, it's just noise at that sample size. The larger experiments like exp-019 and exp-020 with much bigger samples show smaller effects, which actually supports the capability trap narrative better.

For the Qwen scaling experiments, I need to think about how the trap manifests at both ends: the 7B model creates high disagreement because it's weak on these tasks, but its extracted constraints are too noisy to help, while the 72B model is strong enough that disagreement is rare and constraints rarely matter. So both should show SICA roughly equal to SC, just for different reasons. Let me map out the specific C0 values and accuracy patterns for each model size to make sure the results fit this story. correct answer)
  - Δ ≈ 0pp or -0.3pp
  - Discordant: ~1 SICA, ~1 SC win

These give nice C0 gradient: 15% → 53% → 65% (or 38% → 53% → 65% depending on reference)

Wait, I want to be careful. The 14B result is from D012 60 questions (C0=53.3%). For the paper's scaling figure, we'd show:
- 7B: C0=65%, Δ=-1.7pp
- 14B: C0=53%, Δ=-1.7pp to +3.3pp (varies by dataset)
- 72B: C0=15%, Δ=0pp

This shows C0 decreases with model scale (more capable = more deterministic), but SICA ≈ SC at all scales. Looking at the full 804-problem dataset for the 14B model gives C0=38%, which creates a different gradient. Either way—whether I anchor the 14B at 53% or 38%—I get three clearly distinct levels across the model sizes with meaningful gaps between them.

For the GSM8K pilot, the 14B model performs very strongly on math problems, so with K=12 traces most will converge on the correct answer, predicting a low C0 around 10-15%. This adds another data point to the scaling curve where SICA and SC are practically equivalent.

Now I'm setting up the temperature ablation predictions. The hypothesis expects monotonic increase in C0 as temperature rises, so I'm estimating T=0.3 should give around 25-35% while T=1.0 reaches 60-75%, with the baseline T=0.7 at 53%.

Checking the progression: 28% → 40% → 53% → 68% maintains strict monotonicity with all differences under 3 percentage points and sufficient statistical power across the board. Now I'm writing out the full YAML with precise numbers for each experiment entry.

Mapping the figures and tables to their source experiments: the main results table draws from the StrategyQA and FOLIO runs, the capability trap analysis comes from constraint quality correlations, the ablation study from the dedicated experiment, and the scatter plots and heatmaps from their respective analyses.

For the constraint quality correlation experiment, I need to clarify that this uses aggregated data from the earlier runs to compute constraint precision across domains and models, showing near-random performance with no meaningful correlation to entropy or C0 metrics.

Writing YAML output... Now I'm analyzing the per-problem constraint quality data from exp-019, computing precision scores and vote entropy for each of the ~307 multi-candidate problems, then plotting them against each other to show that constraint quality hovers around 50% regardless of diversity levels—this scatter plot is the key evidence that the capability trap mechanism holds regardless of how varied the voting distribution is. With that core figure locked in, I'm ready to write out the complete YAML entries for all experiments, starting with the ablation studies and tiebreak analysis. %) but ties rare (~17%), net impact negligible
3. exp-004: 7B → C0≈65%, Δ≈-1.7pp, weak model diversifies but constraints terrible
4. exp-005: QwQ-32B → C0<5%, SICA≡SC, reasoning model too deterministic
5. exp-006: C0 diagnostic → flat C0-vs-gap relationship, step function at C0<5%
6. exp-007: 72B → C0≈15%, Δ≈0pp, strong model too accurate for diversity
7. exp-008: Case studies → constraints syntactically valid but semantically non-discriminative
8. exp-009: Overhead → ~49% overhead, solver time negligible, extraction dominates
9. exp-011: LLaMA-8B → C0≈62%, Δ≈+3.3pp (n=60 noise), p=0.22
10. exp-012: GSM8K → C0≈12%, SICA≡SC, 14B too strong
11. exp-013: Ablation → MaxSAT ≈ count-only ≈ random-weight
12. exp-014: DeepSeek → C0≈58%, Δ≈-3.3pp, distilled reasoning = instruction behavior
13. exp-015: Logic-LM → ≈ SC, single-trace verification also uses non-discriminative constraints
14. exp-016: Weighted SC → all variants ≈ SC, weighting can't fix non-discriminative constraints
15. exp-017: StrategyQA → C0≈10%, Δ≈+3.3pp n.s., commonsense constraints barely extracted
16. exp-018: ARC → C0≈5%, Δ≈-1.7pp, 14B too accurate on science
17. exp-019: Constraint precision → mean≈0.50, no correlation with entropy, F2 hero figure
18. temp ablation: C0 monotonic 28%→68%, all |Δ| ≤ 2pp, diversity controllable but trap holds
19. GSM8K pilot: C0≈12%, SICA≡SC, supports C0 diagnostic

Now I'm checking the actual registry values for exp-017 to verify the StrategyQA results—the data shows C0 around 10% with SICA and SC nearly identical, which aligns with my earlier assessment that commonsense constraints are barely being extracted effectively.

Looking at exp-018 on ARC, the multi-candidate rate is even lower at 5%, suggesting the 14B model is too capable for that dataset to produce meaningful diversity. Both experiments reveal that C0 stays consistently low across these conditions, and the capability trap only breaks when working with weaker models like LLaMA.

For the F2 per-problem analysis, I need to focus on the 307 multi-candidate problems from exp-001 where diversity actually exists—even though C0 is only 38% overall, those specific problems let me measure how well constraints discriminate. Now I'm ready to finalize the YAML with all the numbers I need, though I still need to pin down specific accuracy baselines for exp-004 and exp-007 on the Qwen models.

Looking at the Qwen family performance on D012: the 7B-Instruct variant struggles significantly with formal logic, hitting around 55% accuracy with roughly 65% diversity and SICA performance around 53-55%, suggesting constraints add minimal value or slightly hurt. The 14B-Instruct performs much better at 73.3% with lower diversity around 53.3% and SICA matching that performance, yielding a modest gain. The 72B-Instruct-AWQ is the strongest performer at 87% accuracy but shows very low diversity at only 15%.

Across the three models, I'm seeing a clear pattern: diversity drops as model capability increases (65% down to 15%), accuracy climbs (55% to 87%), and the SICA-SC gap stays essentially flat across all scales. This suggests that C0 diversity is actually a weakness indicator—weaker models resort to more diverse answers—but higher diversity doesn't translate into SICA improvements. It's a capability trap where the model's fundamental limitations drive the diversity, not the other way around.

Now I'm ready to write out the comprehensive YAML summary.

Looking at exp-011 specifically, the actual result shows a +6.67pp gain at n=60, but that's well within noise margins given the standard error. The larger experiments with the same model (n=200 and n=204) both center around zero effect, so the true effect is probably close to that. I could either report the actual noisy result since it's not statistically inconsistent with the best tier threshold, or predict something closer to the typical +1pp effect I'm seeing elsewhere.

Since the actual result does satisfy the best tier constraint (p=0.22 passes the p > 0.10 cutoff), I'll go with what was observed. The same logic applies to exp-014, exp-017, and exp-018—all their actual results are consistent with best tier, so I'll use those. Now I need to compile the final YAML with all 19 entries in plan order.

For the experiments that required multiple attempts—exp-011 went through three iterations before succeeding, exp-017 had two failed runs then a successful third, and exp-018 needed a second attempt—I'm using the successful final versions for the results.

Now I'm ready to write this out. For the F2 per-problem analysis, I'm looking at a scatter plot where each of the 307 multi-candidate problems from exp-001 becomes a point, with vote entropy on the x-axis measuring the spread of the K=12 vote distribution and constraint precision on the y-axis showing how many constraints align with ground truth, with each point colored to distinguish patterns.

The data shows a flat horizontal band around 50% constraint precision regardless of vote entropy—whether votes are nearly unanimous or split fairly evenly, the constraints discriminate randomly between correct and incorrect answers, which is exactly what the capability trap looks like: diversity in voting exists but provides no actual discriminative power.

For the case studies, I'm planning to show representative examples where constraints either correctly support the right answer, incorrectly support wrong answers alongside the right one, or get ignored entirely by the solver—the core issue being that constraints latch onto surface-level features like variable names rather than capturing genuine logical structure.

For the Logic-LM baseline, I'm treating it as K independent single-trace verifications where each trace gets converted to FOL and checked with a solver, then the verification results are combined by majority vote—this should perform similarly to the other approaches since they're all fundamentally limited by the same underlying constraint quality.

On FOLIO, Logic-LM sometimes works in isolation, but when multiple traces are combined through voting, the approach collapses back to self-consistency because the verification outcome ends up correlating with model confidence rather than actual correctness.

For the weighted self-consistency experiment, I'm testing different weighting schemes—uniform, inverse-length, length-weighted, and constraint-count weighted—but the actual results show they all cluster around the same accuracy with no significant differences, so none of these variations help.

Now I'm compiling the YAML summary... Writing the YAML output...

The results across model families confirm the core findings: temperature variations shift diversity substantially but don't close the SICA-SC gap, the diagnostic predictor holds across Qwen's different scales, and solver choice makes no meaningful difference—all pointing to a structural constraint rather than a tuning problem. The three claims stay as written, title unchanged, ready for submission.

Now I'm planning ablation experiments to stress-test these conclusions, particularly examining how K values affect the SICA-SC relationship on the 14B model across different problem sets to isolate whether tiebreaking mechanisms drive the observed gaps. Looking at the performance metrics across different K values, the noise accumulation pattern becomes clearer—larger K values inject more non-discriminative constraints that degrade SICA's accuracy, with the statistical tests confirming these gaps are real effects rather than sampling noise. The odd K=11 case is particularly revealing since it eliminates the tiebreak mechanism entirely, showing SICA collapses to SC performance when forced to make actual discriminative choices.

Now I'm examining the tiebreak baseline analysis, which directly tests whether SICA's gains come purely from breaking tied questions. The expected results show SICA achieves 80% accuracy on tied problems compared to random's 50%, suggesting the mechanism is indeed just tiebreaking on the roughly 17% of problems where SC produces ties. over_random_pp: 0.5
      sica_net_gain_note: "80% on 10 questions = 8 correct; random = 5; net +3 correct out of 60 → +5pp on tied subset but +0.5pp overall"
    result_rationale: >
      SICA 在 tied questions 上表现最好 (80%) 因为 MaxSAT 的 constraint weighting 比随机选择
      更有信息——但仅限于 tie 场景。Random tiebreak 50% 是理论期望值。关键在于 tied questions
      仅占 ~17% (K=12 偶数 K 才产生 tie)，即使 SICA 在 tie 上完胜，对整体准确率的贡献
      被 base 稀释到 <1pp。This is why exp-002 K=11 (odd, no ties) shows gap=0。

Now I'm looking at the tiebreak analysis with a bar chart showing SICA's 80% accuracy on tied questions compared to random at 50%, alphabetical at 60%, and first-seen at 40%—this directly addresses the reviewer's concern that SICA is merely a tiebreaker by acknowledging it's effective at that specific task, but ties are too infrequent at K=12 to meaningfully impact overall performance, and the gap shrinks further as K increases.

Now I'm examining an ablation study comparing MaxSAT against simpler alternatives like count-only weighting and random weights on the original dataset of 804 problems, with expected accuracies all clustering tightly around 76-77% and McNemar p-values consistently above 0.5, indicating no statistically significant differences between these constraint-weighting approaches. Looking at the constraint ablation results, all four aggregation methods produce nearly identical accuracy around 76.4% with overlapping error bars — this is the critical evidence that MaxSAT optimization provides no real advantage over simple counting. Combined with the earlier finding that constraint precision hovers around 0.50, I have two converging pieces of evidence: constraints themselves lack discriminative power, and even if they did, the solver can't extract meaningful signal from them. This double mechanism evidence directly supports the capability trap hypothesis and should anchor the core argument in section 4.1.

Now looking at the StrategyQA experiment with Qwen2.5-14B across 60 problems with K=12, the results show SICA achieving 56.67% versus standard chain-of-thought at 53.33%, a 3.33 percentage point gap that doesn't reach statistical significance (McNemar p > 0.30, bootstrap p = 0.1346). The multi-candidate rate is quite low at 10%, and trace extraction succeeded in about 70% of cases, with SICA winning 2 discordant pairs while standard chain-of-thought won none. The commonsense reasoning domain shows much lower constraint coverage than expected — only 10% compared to the 35-50% the plan predicted, likely because the 14B model struggles with this task. B 在 commonsense binary 判断上已经足够强，大多数问题的 12 条推理链一致，只有 6 题出现多个候选答案，其中 2 题 SICA 成功翻转。虽然获得 +3.33pp 的提升，但这在统计上不显著（n=60，标准误约 6pp，bootstrap p=0.13）。约束提取率仅 70.4%，因为 commonsense 推理链缺乏可形式化的逻辑结构，这进一步限制了 SICA 的操作空间，导致在低 C0 和低提取率的双重制约下，SICA 几乎无法发挥作用。

StrategyQA 的结果挑战了我对最优多样性假设的预期——commonsense 领域对强模型而言并非最高多样性的场景。但这反而暴露了能力陷阱：即使 C0 恰好足够产生少量不一致的配对，SICA 仍然无法获得显著优势，这与 ARC（C0=5%）和 FOLIO（C0≈38%）形成了跨域对比。

现在看 ARC-Challenge 的实验设计：Qwen2.5-14B 在 60 题科学推理任务上达到 96.7% 的准确率，但多候选率仅 5%，这意味着模型在科学推理上已经非常强。

唯一的不一致出现在 SC 赢的情况，是因为 SICA 的 MaxSAT 约束排除了正确答案。虽然 4 选一的格式理论上应该增加多样性，但模型能力过强反而压制了这种格式效应，5% 的多候选率接近了 QwQ-32B 的退化阈值。

看 ARC-Challenge 的结果，Qwen-14B 的 SC 已经达到 96.7%，这是该数据集的天花板，SICA 反而微幅下降 1.7 个百分点，因为求解器在极少数多候选问题上引入了噪声。对比 FOLIO 的表现（准确率约 79%，多候选率约 38%），能力越强的模型多样性越低，SICA 的效果就越差，这支持了我关于诊断解释的论断。

现在看约 307 个多候选问题的约束质量分析，平均精度在 0.505 左右，但约束精度和投票熵之间几乎没有相关性（R² 仅 0.002，p 值 0.42），FOLIO 和 ProofWriter 的精度表现相近（分别 0.512 和 0.498），跨域差异也不显著（p 值 0.60），约 28% 的问题精度低于 0.4，25% 高于 0.6。

根本原因是 LLM 提取的一阶逻辑约束只捕捉了推理轨迹的表面结构特征（变量命名、逻辑连接词模式），而非真正的语义正确性，导致正确和错误的轨迹因为都使用相同的逻辑形式（if-then、forall 等）而无法被区分，这个限制是结构性的，与投票分布的集中度无关。

FOLIO 和 ProofWriter 的精度几乎相同（0.51 vs 0.50），说明这个问题在跨域上是一致的。

现在我在描述这个核心发现的可视化——一个散点图展示了投票熵和约束精度之间的关系，307 个数据点分布在随机精度线周围，没有明显的趋势，回归线几乎水平，这个图清晰地传达了能力陷阱的本质。

关键是这个图用每个具体问题的粒度（n=307）展示了多样性存在且可变，但约束质量始终停留在随机水平，这与表格中 MaxSAT 接近计数方法的结果形成了双重机制证据：约束本身缺乏判别力，求解器因此无法提取信号。这个每问题级别的分析在统计力上比实验级别的相关性强两个数量级。

现在开始规划 P1 实验，包括 Qwen2.5-7B 的缩放实验。

我在查看 D012 中 60 个问题的预期结果，这涉及弱模型到高 C0 的内部 Qwen 缩放。

现在看到 7B 模型在形式逻辑上明显弱于 14B 版本，导致大量答案不一致，但这也意味着 SICA 有更多可操作的多候选问题——尽管约束质量下降，MaxSAT 优化变得更加随机，最终净效果是 SICA 略微落后约 1.7 个百分点。

这完美展现了弱模型端的能力陷阱：多样性充足但质量缺失。我需要在主要结果表中突出 Qwen-7B 的表现，用热力图展示不同配置下的运作状态，并在对比图中标注 7B 的数据点，显示它如何与 72B 和 14B 形成对比。

通过 Qwen 系列的三个规模，我看到了一个清晰的模式：7B 的 C0 达到 65%，14B 在 38-53% 之间，72B 则降至 15%。这个反向关系验证了 C0 作为能力代理的有效性，但关键是三个规模上 SICA-SC 的差距都接近零，说明高 C0 本身不足以产生性能收益。对于第三个主张，7B 的 65% C0 提供了最强有力的证据，展示了"C0 高但无收益"的情况。

现在转向 QwQ-32B 的负面结果。

这个模型的 C0 低于 5%，SICA 完全退化为 SC，这些数据来自 MVP 阶段的测试。

QwQ-32B 作为推理模型，其确定性的思维链压制了采样多样性——即使温度设为 0.7，12 条轨迹几乎总是产生相同答案，有效 C0 仅 2.6%，与指令微调模型的 38-65% 形成鲜明对比。在 AIME 的 22 道题上完全一致，ProofWriter 虽有少量分歧但 SICA 反而下降 5.9 个百分点，这表明 QwQ-32B 陷入了另一种能力陷阱：模型足够强大反而导致无多样性，使得 SICA 结构性退化为 SC。名义 C0 10.3% 与有效 C0 2.6% 的差距源于答案的一致性。

现在看表格和图表数据，QwQ-32B 行在热力图中全灰色（C0<5%，SICA≡SC），与指令模型行形成对比。这些结果是论证"操作区间空缺"的关键证据：推理模型过于确定导致方法退化，而指令模型虽有较高 C0 但 Δ≈0，说明没有模型同时达到充分多样性和判别约束的平衡点。2.6% 的有效 C0 远低于 20% 阈值，支撑了核心论点。

现在规划一个诊断验证实验，用 CPU 计算 C0 与 SICA-SC 差距的关系，检验 C0 作为预测指标的有效性，涵盖 12 个数据点，C0 范围从 2.6% 到 65%。

结果显示 C0 与差距无显著线性相关性（r²=0.08, p=0.37），但在 C0 低于 5% 的两个条件下确实观察到 SICA 与 SC 一致，而 C0 高于 20% 时平均差距接近零，这验证了 C0 作为必要条件的阈值功能。

跨越 Qwen 的三个规模级别和其他模型族的约五个不同 C0 水平中，高 C0 值并未带来正向收益，F4 散点图清晰展示了这种"高 C0 但零增益"的平坦特征。

F4 是第三个主张的核心图表，揭示了 C0 的明显分化：低于 5% 时方法退化，超过 20% 时虽然可以运作但无法获得收益，而理想的"甜蜜点"（C0 > 20% 且显著正向收益）中没有数据点。理论上界表明如果约束条件足够判别性，SICA 在 C0 为 40-60% 时本可获得 3-10 个百分点的提升，这种未实现的潜力正是能力陷阱的本质。接下来在 Qwen2.5-72B 上进行 AWQ 4 位量化实验，预期生成 60 个数据点。

现在看到 72B 模型在 D012 上的实际表现：标准链式思维达到 86.7% 的准确率，但 C0 仅为 15%，意味着只有 9 道题目产生了多个候选答案。这个强大的模型在大多数问题上 12 条推理路径都能达成一致，验证了我之前的假设。

少数不一致的情况（估计 2 对）中双方各赢一题，最终相互抵消。提取率高达 93% 且矛盾率极低（仅 1%），说明 72B 生成的约束条件质量确实更优——但这恰好暴露了一个问题：C0 太低意味着没有足够的多候选问题让 SICA 方法发挥作用，这是强模型端的能力陷阱，质量提升反而导致多样性消失。

在 Qwen 系列的纵向对比中，72B 是低多样性的锚点。从 7B（C0=65%，Δ=-1.7pp）到 14B（C0=53%，Δ≈0）再到 72B（C0=15%，Δ=0），清晰展现了 C0 随模型规模单调递减的趋势，而间隙保持在零附近。即使 AWQ 量化引入少量噪声，72B 的 C0 可能略有提升但仍远低于 14B。这个数据点对第三个主张至关重要——它证明了在同一模型族内扩展规模时，本质上是在用多样性换取准确性。

现在看一下性能开销的分解：在 804 个样本上，总耗时约 61.6 秒，其中生成占 51.3%，约 31.6 秒，约束提取占 47%，约 29 秒，去重只需 1 秒，MaxSAT 求解几乎可以忽略。相比标准方法，这个方案的额外开销约 48.7%。

关键观察是 LLM 的约束提取成本很高——每条 trace 都需要一次额外推理来解析一阶逻辑，但 MaxSAT 求解本身极快，说明瓶颈在约束质量而非求解复杂度。如果这些约束能有效区分，这个开销可能是值得的，但目前看来增加 49% 的计算成本却没有带来性能提升。

这意味着对实践者来说，简单约束（SC）同样有效且快一倍，是更优的选择。

现在我在分析开销的细节。求解器时间不到0.01%，这表明MaxSAT公式本身的计算效率不是瓶颈——真正的问题在于约束输入的质量。

接下来我在验证第三个模型族的结果。用LLaMA-3.1-8B在60个问题、12个候选答案上测试，预期SICA精度约67%，而SC精度60%，差异约6.7个百分点。数据显示多候选率61.7%，答案提取率89.6%，矛盾率5.3%，其中SICA在有分歧的案例中赢5次，SC只赢1次。

不过McNemar检验p值为0.22，说明这个差异可能只是采样噪声——标准误差约6个百分点，样本量只有60。虽然5:1的分歧比例看起来很强，但绝对数量只有6对，所以需要在更大样本上验证，比如用同一模型在StrategyQA（200个问题）和FOLIO（204个问题）上的后续实验。

截断的traces占44/720，是由于8B模型的上下文限制，但对SICA和SC的影响是对称的，不会改变结论。这个结果在论文中作为一个案例研究，说明在样本量较小时统计功效的重要性。

exp-011的+6.67pp是整个研究中最大的正向差异，但exp-019/020用更大样本量（n=200+）在同一模型上显示真实效应接近零，这恰好证明了小样本的正信号在更严格的复制中不成立——这本身就是一个重要的方法论启示。加上Qwen和Mistral，LLaMA-8B作为第三个指令规模的模型族，满足了EMNLP对三个模型族的最低要求。现在转向Qwen2.5-14B在GSM8K上的30题试点实验。

在这个数学推理任务中，14B模型在GSM8K上的准确率极高（约87%），多候选率仅约10%（3题），这反映了模型在这个领域的强大能力。开放式数学答案虽然有更大的答案空间，但模型足以收敛到正确数值。提取率较低（75%）是因为将数学推理过程形式化为一阶逻辑比逻辑推导更困难。零不一致对意味着SICA和SC在所有30题上完全一致，而10%左右的多候选率与ARC和StrategyQA的模式相似，都反映了14B模型在这些任务上的过强能力。

这个数据点为第三个主张增加了数学领域的证据，表明当模型在目标领域足够强时，多候选率自然降低，方法的操作空间受限。

同时，我注意到约束提取在数学域的可行性——75%的提取率可以接受但低于逻辑域的89%，说明领域特性确实影响了提取质量。现在我在查看DeepSeek-R1蒸馏模型在60个问题上的验证结果，包括准确率、多候选率和提取率等关键指标。

关键发现是这个7B模型的C0达到58.3%，表现得完全像指令微调模型而非推理模型，说明参数量不足以维持R1的确定性推理链，蒸馏后反而退化成高多样性行为，导致SICA相比SC下降3.3个百分点。

截断的traces占比最多（720条中72条），因为R1风格的长推理链加上7B的上下文限制，这证实了蒸馏推理并不等于完整推理——参数规模是决定性因素。我在整理主要结果表和对比分析，包括QwQ-32B的完整推理（C0=2.6%）与DeepSeek-R1-7B的蒸馏推理（C0=58.3%）的对照。

exp-014解决了一个分类问题：DeepSeek-R1-7B的行为表现（C0=58%）应该归入指令规模模型而非推理模型，这意味着需要按照实际行为而非训练方法来重新定义模型分类。我在论文中将DeepSeek-R1-7B重新标记为"具有推理风格训练的指令规模模型"，这样可以避免审稿人质疑只测试了一个推理模型。现在开始设计Logic-LM基线实验，在FOLIO数据集上进行多次单轨迹一阶逻辑验证。

验证结果显示Logic-LM-K方法通过独立验证每条推理轨迹（提取FOL、求解器检查、通过/失败），然后对结果进行多数投票，最终准确率与自洽性方法相当。

但高达92%的验证通过率表明求解器对几乎所有轨迹都返回可满足，无论轨迹是否正确——这与SICA的约束精度约为0.50的问题相同，说明约束本身缺乏判别力。验证实际上退化为格式检查：只要FOL语法正确，求解器就通过，这消除了"也许聚合是问题所在，单轨迹验证效果更好"的反驳。

Logic-LM基线直接回应了审稿人的疑虑，证明单轨迹验证同样失败，根本原因不在聚合架构，而在于约束本身的非判别性——这强化了能力陷阱的论点，无论是单轨迹验证还是多轨迹优化都无法克服非判别约束的限制。现在我在检查加权自洽性基线的实验设计，测试不同的权重方案对验证准确率的影响。

所有权重方案的性能都与标准自洽性相近，因为轨迹层面的信号（长度、约束数量）同样缺乏判别力，反向长度权重略有提升但不显著，而长度和约束计数权重则略低于基线。

关键在于简单的权重调整无法修复非判别性约束的根本问题——问题不在权重方案本身，而在于底层信号质量。

现在我在规划下一阶段的实验，通过定性分析代表性问题的约束来深入理解这个瓶颈。

初步结果表明，LLM 提取的约束主要捕捉题目的前提条件而非推理步骤，这解释了为什么正确和错误的推理轨迹会共享相同的约束——两者都正确理解了题目，但错误发生在推理链的更深层位置。

这导致约束集合在两种轨迹间高度重叠，精度约为 0.50。案例研究通过并排比较同一问题的正确和错误轨迹中的约束，直观展示了这一现象，其中大多数约束是共享的前提，而特定于轨迹的约束同样可能支持正确或错误的答案。

这解释了为什么 MaxSAT 的表现与仅计数方法相当——如果约束主要在轨迹间共享，那么可满足性结构对答案正确性没有信息价值。

现在转向温度参数的消融实验，在 Qwen-14B 上测试不同的温度设置来操纵生成多样性。

我在查看 T=0.3、0.5 和 1.0 的性能指标，包括准确率、提取率和统计显著性检验结果。

现在看到 T=1.0 时准确率下降到 0.70，而且 C0 百分比随温度单调递增，最大差异为 1.7 个百分点，所有 p 值都大于 0.02。

SC 准确率在较低温度下保持在 73-77% 之间，但在 T=1.0 时下降到 70%，这反映了更高温度下的随机错误增加。SICA 和 SC 之间的差异在所有温度设置下都保持在 1.7 个百分点以内。

在 T=0.3 时只有 17 道题目出现多个候选答案，而在 T=1.0 时这个数字增加到 41 道，这导致约束条件的质量下降，MaxSAT 在处理更嘈杂的约束时出现了一次错误排除。由于样本量为 60，标准误差约为 5-6 个百分点，所有 p 值都超过 0.20，表明真实效应接近零。这些实验结果证实了通过温度操纵多样性的假设。

现在我在规划第 5 节的可视化方案：一个双轴图表，左轴显示 C0 随温度单调递增，右轴显示 SICA-SC 差距始终保持在零附近，这直观地说明了能力陷阱的结构性本质。

或者用四面板条形图，每个面板对应一个温度值，展示 SC 和 SICA 的精度几乎相同，同时标注 C0 值的递增趋势。温度消融实验是论文中最有力的因果证据——通过主动操控多样性而非仅观察不同模型间的差异，我能排除混淆因素，证明在同一模型、同一数据集、仅改变温度的条件下，C0 从 28% 连续上升到 68%，但差距始终为零。这直接回应了审稿人可能提出的"也许你还没找到合适的多样性水平"这类质疑。

现在看到 GSM8K 的试点实验设计，用 Qwen2.5-14B 在 30 个问题上测试数学推理，预期 SICA 和 SC 的精度都在 86.7%，差距同样为零。

数学领域虽然答案空间更开放（具体数值而非选择题），理论上应该增加多样性，但 14B 的能力足以让模型收敛到相同答案。提取率较低（75%）是因为数值计算步骤难以形式化为一阶逻辑，而在那 10% 有多个候选答案的问题上，约束精度预计在 0.48 左右，略低于逻辑领域的 0.50。

这是因为数学约束更脆弱——一个计算错误就会使整条约束链失效。最终结果是 SICA 和 SC 表现相当。

现在看 GSM8K 在跨领域覆盖中的角色，它为数学推理添加了一个新维度。C0 值为 10% 与 ARC（5%）和 StrategyQA（10%）一致，反映出 14B 在所有这些"较简单"的领域上都有较低的约束覆盖率。这再次确认了 SICA 和 SC 的等价性。

约束提取管道在数学领域的可行性也得到了验证，75% 的提取率是可以接受的。

现在检查这些 YAML 数据的一致性——验证没有正的 Δ 伴随显著的 p 值，温度消融的最大差异在可接受范围内，F2 精度和斜率都符合预期，C0 跨模型大小有明显的分层，以及不一致对的胜率分布在合理范围内。

对于不一致对的计算，我需要区分主要实验和 K 值消融变体。从主要实验来看，exp-001 和 exp-004 的数据显示 SICA 和 SC 之间的胜负关系，这些才应该被纳入最终的不一致对统计中。

现在我在逐个检查其他实验的结果，包括不同模型、数据集和参数配置下的表现，以便汇总完整的不一致对计数。

最后计算出总共34个SICA和33个SC，这给出了50.7%的胜率，恰好落在预期的置信区间内。接下来我需要计算加权的绝对差值，根据每个实验的样本量来权衡其贡献。

我注意到有些实验的差值相当大，比如exp-011的加权贡献达到400，这表明需要重新审视这个指标的定义——它应该是所有有符号差值的加权平均，然后取绝对值。

现在我在计算这个加权平均，把每个实验的样本量乘以它的差值，加总后除以总样本量，得到约0.198pp，这在[0, 0.8]的范围内。

即使排除掉那些what_if实验或加入温度消融实验，结果仍然保持在合理范围内——大约0.117pp。所以一致性检查都通过了。现在我需要把exp-012和exp-005也纳入加权平均的计算中。 I'm verifying that the constraint quality correlation results make sense—the precision hovers just above chance at 0.505 with modest variation, and the relationship between vote entropy and precision is essentially flat with negligible explanatory power, confirming these variables aren't meaningfully connected.

Now I'm preparing the final YAML output and need to determine which experiments to include. The prompt specifies only planned experiments, so I'm excluding exp-001 and exp-010 since they're already done, and compiling the list of remaining planned studies.

I'm noticing a potential duplicate—exp-012 from the plan and gsm8k_pilot_30q from the what-if section both appear to be testing Qwen-14B on GSM8K with 30 questions, just with slightly different naming conventions. I'm noticing that exp-012 and the gsm8k_pilot_30q in the what_if section are actually the same experiment with identical configurations, so I should list exp-012 in the main planned experiments and treat the what_if version as a cross-reference. The temperature ablation experiments in what_if correspond to the running temperature-ablation variants in the registry, so those belong in the what_if section as planned additions. Verifying I have all the planned experiments from the plan—scanning through, I count 17 that are marked as planned, excluding the two that are already done. Adding the two what_if experiments brings me to 19 total entries, which matches what was requested. Now I'm ready to generate the YAML output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02a6e9a4-c295-4fd7-80b1-3cdfad5c3067",
  "isSidechain": false,
  "requestId": "req_011Cb8L3BmBxyXQfuUr2Dbeq",
  "type": "assistant",
  "uuid": "f3530220-8359-40e0-99e7-4acf2bc45258",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjZshHmiK3n27YHkSie6Mc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3360,
      "cache_read_input_tokens": 30556,
      "output_tokens": 52018,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3360,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 52018,
          "cache_read_input_tokens": 30556,
          "cache_creation_input_tokens": 3360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3360
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

_source line 12 · 2026-05-17T15:08:18.858Z_

```yaml
tier: best
narrative_guidance: >
  Capability trap 被结构性确认。Temperature ablation (§5) 展示 diversity 通过 temperature
  可连续操控 (C0: 28%→68%), 但 SICA-SC gap 在所有温度下恒为零 (|Δ|≤1.7pp, 全部 p>0.30)
  ——这是结构性限制而非调参失败。F2 hero figure per-problem scatter (n=307) 直观展示
  constraint precision ≈ 0.50 (近随机) 且与 vote_entropy 无相关 (slope=0.003, r²<0.01),
  无需 binning 即清晰可读。Qwen 7B/14B/72B 产出三个 distinct C0 水平 (65%/53%/15%),
  Claim 3 diagnostic predictor 成立。五个模型族 combined N>1300 全部 SICA≈SC (最大
  |Δ|=6.67pp 但 p=0.22, 零个 p<0.10)。MaxSAT≈count-only≈random-weight 确认 solver
  无贡献, 与 F2 per-problem 形成双重机制证据。Discordant pair aggregate winrate=50.7%
  (34/67), weighted Δ=+0.20pp——统计上精确为零。三条 claims 措辞不改, title
  "The Capability Trap" 不变。强 EMNLP main submission, contribution = mechanism
  identification + first systematic negative result + zero-cost diagnostic。

imagined_experiments:
  # ============================================================
  # P0 Experiments
  # ============================================================
  - name: sica_k_ablation_14b
    plan_id: exp-002
    description: "K=6/8/11/12/16/20 sensitivity on D012 60q, 含 odd K=11 tiebreak 隔离测试"
    expected_results:
      n: 60
      K6_sica: 0.733
      K6_sc: 0.733
      K6_delta_pp: 0.0
      K8_sica: 0.733
      K8_sc: 0.750
      K8_delta_pp: -1.7
      K11_sica: 0.733
      K11_sc: 0.733
      K11_delta_pp: 0.0
      K12_sica: 0.700
      K12_sc: 0.750
      K12_delta_pp: -5.0
      K16_sica: 0.717
      K16_sc: 0.750
      K16_delta_pp: -3.3
      K20_sica: 0.700
      K20_sc: 0.733
      K20_delta_pp: -3.3
      all_K_sica_leq_sc: true
      larger_K_degrades_sica: true
      mcnemar_p_all_gt_020: true
    result_rationale: >
      SICA ≤ SC at all K 因为 MaxSAT over non-discriminative constraints 只注入噪声。
      K=11 (odd) Δ=0 是关键: odd K 消除 SC ties, SICA 失去唯一有效机制 (tiebreaking),
      collapse to SC。Larger K (16, 20) 放大噪声注入——更多 traces → 更多 non-discriminative
      constraints → MaxSAT 更大概率排除正确答案。-5pp at K=12 和 -3.3pp at K=16/20
      反映此噪声累积。All p>0.20 因 n=60 (SE≈5-6pp), 个体波动是 sampling noise
      叠加在 true effect ≈ 0 之上。
    tables:
      - "Appendix: K sensitivity table (all K × accuracy)"
    figures_description:
      - "Appendix figure: SICA-SC gap (y) vs K (x), 水平参考线 y=0, 各点 error bars 均跨零。Larger K 呈弱负趋势。K=11 精确命中零线。"
    analysis: >
      K ablation 消除 'wrong K' counterargument。K=11 odd-K test 最锐利: 若 SICA
      在 tiebreaking 之外有价值, gap 应在 odd K 也存在; gap=0 确认 SICA = tiebreaker。
      Combined with exp-003 (tiebreak 仅占 17% 问题), SICA 的唯一 mechanism 被量化为
      micro-scale effect。Paper §4.2 mechanism analysis。

  - name: tiebreak_baseline_analysis
    plan_id: exp-003
    description: "CPU-only: SICA vs SC-random vs SC-alphabetical vs SC-first-seen tiebreak 比较"
    expected_results:
      n_tied_questions: 10
      pct_tied_of_total: 0.167
      sica_tiebreak_accuracy: 0.80
      random_tiebreak_accuracy: 0.50
      alphabetical_tiebreak_accuracy: 0.60
      first_seen_tiebreak_accuracy: 0.40
      sica_net_gain_over_random_on_all_60: 0.5
    result_rationale: >
      SICA 在 tied questions 上 80% 正确, 因为 constraint weighting 即使不判别 correct
      vs incorrect, 对 tie (两个 answer 票数相等) 仍能通过微弱信号打破平衡。但 tied
      questions 仅占 17% (K=12 even-K 才产生 tie)。10 题中多赢 3 题 (vs random)
      对 60 题整体贡献 +0.5pp——在 SE≈6pp 的噪声中不可见。Random 50% 是理论
      期望值; alphabetical 60% 反映答案选项 label 与正确答案的偶然相关; first-seen
      40% 因为 model 首条 trace 并非最准确。
    tables:
      - "T4: Tiebreak Analysis (tied subset)"
    figures_description:
      - "T4 bar chart: 四种 tiebreak 方法在 tied subset 上的 accuracy。SICA 80% 显著最高, 但 caption 标注 'ties = 17% of problems, net impact < 1pp on full set'。"
    analysis: >
      回应 reviewer 'SICA is just a better tiebreaker'。Answer: yes, and an effective
      one, but ties are structurally rare at K=12. At odd K (exp-002 K=11), ties = 0,
      SICA≡SC。Even at even K, 80% × 17% = 1.3% net correct → <1pp overall。
      Cost-benefit: 49% overhead (exp-009) for <1pp on tied subset = not worthwhile。

  - name: sica_constraint_ablation
    plan_id: exp-013
    description: "CPU-only ablation: MaxSAT vs count-only vs random-weight on exp-001 (n=804)"
    expected_results:
      n: 804
      maxsat_accuracy: 0.7649
      count_only_accuracy: 0.7662
      random_weight_accuracy: 0.7637
      sc_baseline_accuracy: 0.7624
      agreement_802_of_804: true
      maxsat_vs_count_mcnemar_p: 0.99
      maxsat_vs_random_mcnemar_p: 0.85
      maxsat_vs_sc_mcnemar_p: 0.74
      all_pairwise_nonsignificant: true
    result_rationale: >
      MaxSAT ≈ count-only 因为 constraint satisfiability 不携带判别信息。当 constraints
      对正确/错误答案同等满足时, solver 的优化退化为计数: satisfiability structure 无
      贡献。Random-weight ≈ MaxSAT 因为权重差异在 non-discriminative constraints 上是
      纯噪声。802/804 题四种方法答案一致, 仅 2 题分歧 (互相抵消)。这直接证明 SAT
      解算机制空洞化——是 capability trap 的 mechanism evidence。
    tables:
      - "T3: Constraint Ablation (MaxSAT vs count-only vs random-weight vs SC)"
    figures_description:
      - "T3 grouped bar: 四种方法 accuracy 几乎等高 (~76.4%), error bars 完全重叠。Visual message: solver adds nothing beyond counting。"
    analysis: >
      Make-or-break evidence for capability trap mechanism。如果 MaxSAT ≈ count-only,
      solver 无附加值——constraints 没有 exploitable satisfiability structure。Combined
      with F2 (precision≈0.50), 形成双重机制证据: (1) constraints 不判别 (F2),
      (2) solver 因此无法提取信号 (T3)。Paper §4.1 核心机制结果。exp-013 + exp-019
      共同构成 Claim 1 的 evidence base。

  - name: sica_strategyqa_14b
    plan_id: exp-017
    description: "Qwen2.5-14B on StrategyQA 60q (K=12), commonsense reasoning domain"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.5667
      sc_accuracy: 0.5333
      delta_pp: 3.33
      mcnemar_p: ">0.30"
      bootstrap_p: 0.1346
      multi_candidate_rate: 0.10
      extraction_rate_trace: 0.704
      discordant_sica_wins: 2
      discordant_sc_wins: 0
      model: Qwen2.5-14B-Instruct
      dataset: StrategyQA
    result_rationale: >
      StrategyQA C0=10% 远低于 plan 预期 (35-50%), 因为 14B 在 binary commonsense (yes/no)
      上足够强, 大多数问题 12 traces 一致。仅 6 题多候选, 2 题 SICA 翻转正确。+3.33pp
      non-significant (n=60 SE≈6pp, bootstrap p=0.13)。Extraction rate 仅 70.4% (commonsense
      推理链缺少可形式化逻辑结构), 进一步限制 SICA 操作空间。2:0 discordant ratio
      看似 SICA 占优, 但 n=2 discordant pairs 无统计意义。
    tables:
      - "T1: Main Results (StrategyQA × Qwen-14B row)"
      - "F3: Operating Regime Heatmap (StrategyQA × Qwen-14B cell)"
    figures_description:
      - "T1 row: StrategyQA | Qwen-14B | SC 53.3% | SICA 56.7% | Δ +3.3 | p n.s. | C0=10%"
    analysis: >
      StrategyQA 结果挑战 best-case-diversity 假设: commonsense domain 并非 diversity
      最高场景 (对强模型而言)。但强化 capability trap: 即使 C0 恰好产生少量 discordant,
      SICA 仍无显著优势。与 ARC (C0=5%) 和 PW+FOLIO (C0=38%) 形成三域覆盖。

  - name: sica_arc_challenge_14b
    plan_id: exp-018
    description: "Qwen2.5-14B on ARC-Challenge 60q (K=12), 科学推理 4 选 1"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.950
      sc_accuracy: 0.9667
      delta_pp: -1.67
      multi_candidate_rate: 0.05
      extraction_rate: 1.0
      discordant_sica_wins: 0
      discordant_sc_wins: 1
      model: Qwen2.5-14B-Instruct
      dataset: ARC-Challenge
    result_rationale: >
      14B 在 ARC-Challenge SC 高达 96.7%, C0 仅 5% (3 题多候选)。模型对 science 常识
      足够自信, 12 traces 几乎总一致。唯一 discordant pair SC 赢——MaxSAT 排除了正确
      答案的 constraint。4-choice format 理论上增加 diversity (更多选项), 但 14B 能力
      过强, format 效应被 capability 压制。C0=5% 接近 QwQ-32B 退化阈值。
    tables:
      - "T1: Main Results (ARC × Qwen-14B row)"
      - "F3: Operating Regime Heatmap (ARC × Qwen-14B cell)"
    figures_description:
      - "T1 row: ARC | Qwen-14B | SC 96.7% | SICA 95.0% | Δ -1.7 | C0=5%"
    analysis: >
      ARC 是 14B 的 ceiling 域: SC 已达 96.7%, 无提升空间。SICA 微损 (-1.7pp) 因为
      solver 在极少数 multi-candidate 问题上注入噪声。与 FOLIO (acc ~79%, C0 ~38%)
      对比展示 capability-diversity 反向关系: high accuracy → low C0 → method degenerates。

  - name: constraint_quality_correlation
    plan_id: exp-019
    description: "CPU-only: per-problem constraint precision vs vote_entropy (exp-001 n≈307 multi-candidate). F2 hero figure"
    expected_results:
      n_multi_candidate: 307
      constraint_precision_mean: 0.505
      constraint_precision_std: 0.148
      constraint_precision_median: 0.500
      precision_vs_entropy_slope: 0.003
      precision_vs_entropy_r_squared: 0.002
      precision_vs_entropy_p: 0.42
      folio_precision_mean: 0.512
      proofwriter_precision_mean: 0.498
      cross_domain_precision_diff_p: 0.60
      fraction_precision_below_040: 0.28
      fraction_precision_above_060: 0.25
      discordant_pair_sica_winrate_overall: 0.48
    result_rationale: >
      Constraint precision ≈ 0.50 (近随机) 因为 LLM 提取的 FOL constraints 捕获推理
      trace 的表面结构 (变量命名、逻辑连接词模式) 而非深层语义正确性。正确和错误 traces
      共享相似表面结构 (都使用 if-then/forall/exists), 导致 constraints 无法区分二者。
      Slope ≈ 0 因为此限制是 structural 的: 无论 vote 分布多分散 (高 entropy) 或多集中
      (低 entropy), constraint discriminative power 都不变——它取决于 extraction quality
      而非 diversity level。FOLIO 和 ProofWriter precision 几乎相同 (0.512 vs 0.498,
      差异 p=0.60), 说明跨域一致。28% 问题 precision<0.40 (constraints 反向判别),
      25% precision>0.60 (偶然判别), 呈对称分布围绕 0.50。
    tables:
      - "T2: Constraint Quality Summary (precision by domain × model)"
    figures_description:
      - >
        F2 (Hero Figure): Scatter, x=vote_entropy (0.3–1.8), y=constraint_precision (0–1.0)。
        307 points, blue=ProofWriter, orange=FOLIO。水平参考线 y=0.50。Points 形成
        diffuse 水平带, 中心在 0.50, 无可见趋势。Regression line 近乎水平 (slope=0.003)。
        Caption: 'Constraint precision is near-random (mean=0.50) regardless of output
        diversity, confirming constraints lack discriminative power at all diversity levels.'
        Per-problem granularity 无需 binning, 每个 dot = 一个具体问题, 信息密度高。
    analysis: >
      F2 是论文 hero figure, 一图传达 capability trap: diversity (x) 存在且可变, 但
      constraint quality (y) 恒为随机水平。'Regardless of diversity' 可视化为 slope=0。
      与 T3 (MaxSAT≈count-only) 形成双重机制证据: (1) constraints 不判别 (F2),
      (2) solver 因此无法提取信号 (T3)。Per-problem granularity (n=307) 比
      experiment-level correlation (n=7, r=0.15 p=0.74) 统计力强两个数量级,
      是 D035 识别的 F2 data gap 的完整解决。

  # ============================================================
  # P1 Experiments
  # ============================================================
  - name: sica_7b_scaling
    plan_id: exp-004
    description: "Qwen2.5-7B-Instruct on D012 60q. Within-Qwen weak model, high C0"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.533
      sc_accuracy: 0.550
      delta_pp: -1.7
      multi_candidate_rate: 0.65
      extraction_rate: 0.82
      answer_extraction_rate: 0.88
      contradiction_rate: 0.08
      discordant_sica_wins: 2
      discordant_sc_wins: 3
      mcnemar_p: 0.65
      proofwriter_sica: 0.500
      proofwriter_sc: 0.533
      folio_sica: 0.567
      folio_sc: 0.567
      model: Qwen2.5-7B-Instruct
    result_rationale: >
      7B 在 formal logic 上显著弱于 14B (SC 55% vs 73%), 产生大量 answer disagreement
      (C0=65%)。但更弱模型也提取更差 constraints: extraction_rate 89%→82%,
      contradiction_rate 2.2%→8%。高 C0 意味着更多 multi-candidate 问题可操作,
      但 constraints 质量更差意味着 MaxSAT 优化方向更随机。5 discordant pairs 中
      SC 赢 3 个: MaxSAT 在 noisy constraints 上更大概率排除正确答案。
      这完美展示 capability trap weak-model 端: diversity abundant, quality absent。
    tables:
      - "T1 appendix: Qwen-7B row"
      - "F4: C0 vs Gap (7B 数据点: C0=65%, Δ=-1.7pp)"
    figures_description:
      - "F4 scatter: 7B 位于 high-C0 端 (x=65%) below zero line (y=-1.7pp)。与 72B (x=15%, y=0) 和 14B (x=53%, y≈0) 共同形成 within-Qwen scaling 趋势线。"
    analysis: >
      7B 提供 within-Qwen scaling 的 high-diversity anchor。Combined with 14B (C0=53%)
      and 72B (C0≈15%), 三个 distinct C0 levels within single model family 成立
      (c0_scaling_distinct_levels=3)。C0 与 model scale 反向 (7B→65%, 14B→53%, 72B→15%)
      验证 C0 as capability proxy。但 SICA-SC gap 在三个 scale 都 ≈ 0, 证明 C0 是
      necessary but insufficient。For Claim 3: C0=65% + Δ=-1.7pp 是 'high C0 but no
      gain' 的最强数据点。

  - name: qwq_32b_operating_regime
    plan_id: exp-005
    description: "QwQ-32B negative results: C0<5%, SICA≡SC. CPU-only格式化 MVP 已有数据"
    expected_results:
      total_problems: 46
      qwq_c0_nominal_pct: 10.3
      qwq_c0_effective_pct: 2.6
      qwen14b_c0_pct: 46.0
      diversity_ratio: 17.7
      aime_delta_pp: 0.0
      aime_n: 22
      proofwriter_delta_pp: -5.9
      proofwriter_n: 17
      folio_n: 2
      c0_below_20_threshold: true
      sica_structurally_degenerate: true
    result_rationale: >
      QwQ-32B 作为 full reasoning model, deterministic chain-of-thought 压制 sampling
      diversity: 即使 T=0.7, 12 traces 几乎总产生相同答案 (effective C0=2.6%)。AIME 22
      题 0% multi-candidate (完全一致)。Nominal C0=10.3% vs effective C0=2.6% 的差距来自
      answer extraction 格式噪声 (如 "30" vs "30.0"), 非真实 reasoning divergence。
      ProofWriter -5.9pp 是 n=17 噪声 (SE≈12pp)。QwQ-32B 展示 capability trap strong-
      reasoning 端: model 足够强 → 无 diversity → SICA 结构性退化为 SC。
    tables:
      - "T1: Main Results (QwQ-32B row, all cells 'SICA≡SC')"
      - "F3: Operating Regime Heatmap (QwQ-32B column 全灰)"
    figures_description:
      - "F3: QwQ-32B row 全灰 (C0<5% → degenerate)。与 instruction model rows 形成 sharp 对比。"
    analysis: >
      QwQ-32B 是 Claim 2 'operating regime empty' 的一极: full reasoning → no diversity
      → method degenerates。对称地, instruction models 展示另一极: high diversity → no
      constraint quality → method fails。No model hits the sweet spot。C0=2.6% 远低于
      20% 阈值, 直接支撑 Claim 3 early-stopping criterion。

  - name: c0_diagnostic_validation
    plan_id: exp-006
    description: "CPU-only: C0 vs SICA-SC gap 散点, 跨所有 models/K/domains, 验证 C0 as predictor"
    expected_results:
      n_conditions: 14
      c0_range_pct: [2.6, 65.0]
      gap_range_pp: [-3.3, 6.67]
      regression_slope: -0.02
      regression_r_squared: 0.06
      regression_p: 0.40
      c0_below_5_n: 3
      c0_below_5_mean_abs_gap: 0.6
      c0_above_20_n: 8
      c0_above_20_mean_gap: 0.1
      c0_above_20_all_p_gt_010: true
      distinct_c0_levels_qwen_family: 3
      distinct_c0_levels_all_models: 5
    result_rationale: >
      C0 与 gap 无线性关系 (r²=0.06, p=0.40) 因为 gap 在所有 C0 水平围绕 0 波动。
      C0<5% 条件 (QwQ-32B 2.6%, ARC-14B 5%, StrategyQA-14B 10%) SICA≡SC: 方法
      结构性退化。C0>20% 条件 (Qwen-7B 65%, LLaMA-8B 62%, DeepSeek-R1-7B 58%, Mistral
      50%, Qwen-14B 53%) mean gap≈0: diversity 存在但 constraints 不判别。
      Within-Qwen 三水平 (15%/53%/65%) + DeepSeek (58%) + LLaMA (62%) ≈ 5 distinct
      levels。F4 展示理论上界 vs 实际数据的 gap = capability trap 的视觉量化。
    tables:
      - "F4: C0 vs Gap (所有条件)"
    figures_description:
      - >
        F4: x=C0 (0–70%), y=SICA-SC gap (-6 to +8pp)。~14 data points, all cluster
        around y=0。Dashed theoretical upper bound curve (if constraints were perfect,
        gap ∝ C0)。实际数据与理论上界之间的 gap = capability trap magnitude。
        Grey zone: C0<5% (degeneration zone)。Red zone: C0>20%, gap≈0 (trap zone)。
        No point in upper-right quadrant (the sweet spot is empty)。
    analysis: >
      F4 是 Claim 3 核心 figure。Bifurcation 清晰: C0<5% → degenerate (grey),
      C0>20% → trapped (red), no sweet spot。理论上界展示 SICA 在 C0=50% 时应有
      5-10pp gain if constraints discriminative——this unrealized potential IS the trap。
      C0 因此是 zero-cost early stopping criterion: compute C0, if <20% stop (method
      degenerate), if >20% stop (trap guarantees no gain)。Either way, don't proceed。

  - name: sica_72b_awq
    plan_id: exp-007
    description: "Qwen2.5-72B-Instruct-AWQ on D012 60q. Within-Qwen strong model, low C0"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.867
      sc_accuracy: 0.867
      delta_pp: 0.0
      multi_candidate_rate: 0.15
      extraction_rate: 0.93
      answer_extraction_rate: 1.0
      contradiction_rate: 0.01
      discordant_sica_wins: 1
      discordant_sc_wins: 1
      mcnemar_p: 1.0
      proofwriter_sica: 0.833
      proofwriter_sc: 0.833
      folio_sica: 0.900
      folio_sc: 0.900
      model: Qwen2.5-72B-Instruct-AWQ
    result_rationale: >
      72B SC accuracy 高达 86.7%, C0 仅 15% (9 题多候选)。能力强到大部分问题 12 traces
      一致。Extraction_rate 高 (93%), contradiction_rate 极低 (1%)——72B 的 constraints
      质量确实更好。但 C0 太低, 没有足够 multi-candidate 问题让 SICA 操作。
      仅 ~2 discordant pairs, 各赢一题, 净 Δ=0。AWQ 4-bit quantization 可能引入
      微量额外噪声, 使 C0 略高于 full-precision 72B (否则可能 C0<10%), 但仍远低于
      14B。这是 capability trap strong-model 端: quality improves but diversity vanishes。
    tables:
      - "T1 appendix: Qwen-72B row"
      - "F4: C0 vs Gap (72B 数据点: C0=15%, Δ=0)"
    figures_description:
      - "F4: 72B 位于 low-C0 端 (x=15%, y=0)。与 7B (x=65%, y=-1.7) 和 14B (x=53%, y≈0) 形成 within-Qwen 三点连线, 展示 C0 scaling with model size。"
    analysis: >
      72B 是 within-Qwen scaling 的 low-diversity anchor。三点连线清晰展示 C0 随
      model scale 单调递减 (65%→53%→15%) 但 gap 恒为 ≈0。这证明 'even when you
      scale up within a family, you trade diversity for accuracy without ever hitting
      the sweet spot'。72B extraction quality 最高 (93%, 1% contradiction) 佐证
      strong model → better constraints, 但 futile when C0 is low。

  - name: overhead_analysis
    plan_id: exp-009
    description: "exp-001 Wall-time breakdown: trace generation, constraint extraction, MaxSAT"
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
      sica_overhead_over_sc_pct: 48.7
      p50_overhead_pct: 48.9
      p90_overhead_pct: 57.6
    result_rationale: >
      SICA 相比 SC 增加 ~49% wall time, 几乎全部来自 constraint extraction (一次额外
      LLM inference pass per trace, 解析 FOL)。MaxSAT solver 本身极快 (0.003s, <0.01%
      总时间)——瓶颈不在 solver complexity 而在 extraction cost。如果 constraints 是
      discriminative 的, 49% overhead 可能值得 (每 query 多花 30s 换 5pp+ accuracy);
      但 Δ≈0 意味着 49% 额外计算换零收益。P90 overhead 57.6% 来自长 traces (FOLIO
      domain), extraction 时间与 trace 长度成正比。
    tables:
      - "Appendix: Overhead breakdown table"
    figures_description:
      - "Stacked bar: trace gen 51.3% + extraction 47% + dedup 1.6% + solver 0.005%。Caption: 'solver is negligible; LLM extraction calls dominate overhead'。"
    analysis: >
      回应 reviewer 'is the overhead worth it': 不值得。49% overhead = 零精度收益。
      SC 是 Pareto dominant (same accuracy, half the cost)。Solver time <0.01% 表明
      MaxSAT formulation 计算效率不是问题——问题在于输入质量。This strengthens
      practical guidance: even if future work improves constraint quality, the extraction
      cost remains substantial。

  - name: sica_llama_8b
    plan_id: exp-011
    description: "LLaMA-3.1-8B-Instruct on D012 60q. 第三 instruction-scale 家族"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.6667
      sc_accuracy: 0.6000
      delta_pp: 6.67
      multi_candidate_rate: 0.617
      extraction_rate: 0.856
      answer_extraction_rate: 0.896
      contradiction_rate: 0.053
      truncated_traces: 44
      discordant_sica_wins: 5
      discordant_sc_wins: 1
      mcnemar_p: 0.22
      model: LLaMA-3.1-8B-Instruct
    result_rationale: >
      LLaMA-8B C0=62%, SC=60% (instruction-scale models 中最弱)。+6.67pp 是 n=60
      采样噪声: SE≈6pp, 1.1σ deviation, p=0.22 non-significant。5:1 discordant ratio
      看似强烈, 但绝对数量小 (6 pairs)。关键验证来自同模型更大 n: exp-019 (StrategyQA
      n=200, Δ=+2.0pp p=0.42) 和 exp-020 (FOLIO n=204, Δ=-2.45pp p=0.27) 确认 true
      effect 接近 0。正 delta 与 负 delta 在不同 domains 交替出现 = 纯噪声。
      44/720 truncated traces 因 8B context limit, 但 truncation 对 SICA/SC 影响对称。
    tables:
      - "T1: Main Results (LLaMA-8B D012 row)"
    figures_description:
      - "T1 row: D012 | LLaMA-8B | SC 60.0% | SICA 66.7% | Δ +6.7 | p=0.22 n.s."
    analysis: >
      exp-011 的 +6.67pp 是全研究最大正 delta, 但 exp-019/020 (同模型 n=200+) 展示
      true effect ≈ 0。Paper framing: 'small-sample positive signal does not survive
      powered replication'——本身是方法论 lesson。LLaMA-8B 作为第三 instruction-scale
      family (加 Qwen/Mistral), 满足 EMNLP 三家族最低门槛。

  - name: gsm8k_pilot_14b
    plan_id: exp-012
    description: "Qwen2.5-14B on GSM8K 30q pilot (K=12). 数学推理域覆盖"
    expected_results:
      n: 30
      k: 12
      sica_accuracy: 0.867
      sc_accuracy: 0.867
      delta_pp: 0.0
      multi_candidate_rate: 0.10
      extraction_rate: 0.75
      answer_extraction_rate: 0.95
      discordant_sica_wins: 0
      discordant_sc_wins: 0
      model: Qwen2.5-14B-Instruct
      dataset: GSM8K
    result_rationale: >
      14B 在 GSM8K accuracy ~87%, C0 ≈ 10%。开放式数学答案 (具体数字) 理论上有更大
      answer space, 但模型能力足以收敛到正确数值。Extraction rate 偏低 (75%) 因为数值
      计算步骤难以 FOL 形式化 (例 "3×5+2=17" → FOL 表达不自然)。0 discordant pairs →
      SICA ≡ SC on all 30 题。C0≈10% 类似 ARC/StrategyQA: 14B 在 'easier' domains
      上能力过强, diversity 不足。
    tables:
      - "Appendix: Cross-domain (GSM8K row)"
      - "F4: C0 vs Gap (GSM8K point)"
    figures_description:
      - "F4 data point: GSM8K C0=10%, Δ=0, 位于 low-C0 degeneration zone 边缘。"
    analysis: >
      GSM8K 确认: 当模型在目标 domain 足够强时, C0 自然低, SICA 无操作空间。
      Extraction rate 75% (vs logic domain 89%) 说明 domain 影响 extraction feasibility。
      Appendix material, 回应 'what about math reasoning' 的 reviewer。

  - name: sica_deepseek_r1_llama_8b
    plan_id: exp-014
    description: "DeepSeek-R1-Distill-Qwen-7B on D012 60q. Distilled reasoning model 行为验证"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.683
      sc_accuracy: 0.717
      delta_pp: -3.33
      multi_candidate_rate: 0.583
      extraction_rate: 0.839
      answer_extraction_rate: 0.939
      truncated_traces: 72
      contradiction_rate: 0.037
      discordant_sica_wins: 0
      discordant_sc_wins: 2
      mcnemar_p: 0.48
      model: DeepSeek-R1-Distill-Qwen-7B
    result_rationale: >
      关键发现: C0=58.3%, 行为完全像 instruction-scale model, 非 plan 预期的 reasoning
      model (C0<5%)。7B 参数量不足以维持 R1 的 deterministic reasoning chain——蒸馏后
      小模型在 7B 容量下退化为高 diversity 行为。Δ=-3.33pp: 2 discordant pairs SC 全赢,
      MaxSAT constraint 排除恰好排错。Truncated traces 最多 (72/720), 因 R1 风格长
      reasoning + 7B context 限制。结论: distilled reasoning ≠ full reasoning,
      参数量是决定性因素, 非训练方法。
    tables:
      - "T1: Main Results (DeepSeek-R1-7B row)"
      - "Appendix: Reasoning model comparison (QwQ C0=2.6% vs DeepSeek C0=58.3%)"
    figures_description:
      - "Appendix table: QwQ-32B (full reasoning, C0=2.6%) vs DeepSeek-R1-7B (distilled, C0=58.3%)。Caption: 'Distillation at 7B recovers instruction-scale behavior'。"
    analysis: >
      exp-014 解决分类问题: DeepSeek-R1-7B 归入 instruction-scale (C0=58%) 非 reasoning
      (C0<5%)。Model taxonomy 应以行为 (C0 水平) 而非训练方法定义。Paper 重分类
      DeepSeek-R1-7B 为 'instruction-scale with reasoning-style training', 避免
      reviewer 'only one reasoning model' 攻击。QwQ-32B remains sole full reasoning model。

  - name: logic_lm_baseline
    plan_id: exp-015
    description: "Logic-LM × K: single-trace FOL verification K 次后 vote, CPU-only on FOLIO"
    expected_results:
      n: 204
      k: 12
      logic_lm_k_accuracy: 0.789
      sc_accuracy: 0.794
      sica_accuracy: 0.794
      logic_lm_vs_sc_delta_pp: -0.5
      logic_lm_vs_sica_delta_pp: -0.5
      verification_pass_rate: 0.92
      verification_discriminative: false
      mcnemar_logic_lm_vs_sc_p: 0.82
    result_rationale: >
      Logic-LM-K 将每条 trace 独立验证 (extract FOL → solver check → pass/fail) 后
      majority vote。Accuracy ≈ SC 因为 verification pass rate 极高 (92%): solver 对
      大部分 traces 返回 satisfiable, 无论 trace 是否正确。原因同 SICA: constraints
      不判别。'Verification' 退化为 'format check'——只要 FOL syntax 正确 solver 就
      pass。这消除 'maybe aggregation is the problem, single-trace verification works
      better' 反论。瓶颈是 constraint quality, 非 aggregation architecture。
    tables:
      - "Appendix: Logic-LM × K baseline comparison"
    figures_description:
      - "Appendix table row: FOLIO | Logic-LM-K 78.9% ≈ SC 79.4% ≈ SICA 79.4%。"
    analysis: >
      回应 reviewer 'compare to Logic-LM/LINC'。Answer: Logic-LM-K 也 ≈ SC, 因为
      bottleneck 是 extraction quality 非 aggregation method。Single-trace verification
      也失败, 因为 underlying constraints non-discriminative。This generalizes the
      capability trap beyond SICA to any FOL-constraint-based method。

  - name: weighted_sc_baseline
    plan_id: exp-016
    description: "Weighted SC (Taubenfeld 2024 style): uniform/inv-length/length/constraint-count on exp-001"
    expected_results:
      n: 804
      sc_uniform_accuracy: 0.7624
      sica_maxsat_accuracy: 0.7649
      inv_length_accuracy: 0.7674
      length_weighted_accuracy: 0.7525
      constraint_count_accuracy: 0.7525
      inv_length_vs_sc_p: 0.453
      length_vs_sc_p: 0.153
      inv_length_vs_sica_p: 0.864
      all_nonsignificant: true
    result_rationale: >
      所有 weighting 方案 ≈ SC, 因为 trace-level 信号 (长度、constraint 数量) 同样
      不具判别性。Inv-length 略高 (+0.50pp, p=0.45): shorter traces 可能稍 more focused,
      但效果不显著。Length-weighted 和 constraint-count 略低 (-1pp): longer/more-constrained
      traces 未必更正确 (可能是 model 在错误路径上 elaborating)。关键 insight: 简单
      weighting 也无法修复 non-discriminative 信号, 因为问题在底层信号质量而非权重方案。
    tables:
      - "Appendix: Weighted SC comparison table"
    figures_description:
      - "Appendix bar chart: 五种方法 accuracy 在 ±1pp 内, error bars 全部重叠。"
    analysis: >
      Weighted SC 是最直接竞争 baseline。All variants ≈ SC 确认: (1) 无简单 weighting
      能 rescue method, (2) bottleneck 是 signal quality 非 aggregation sophistication。
      SICA 失败不是因为 MaxSAT over-engineering, 而是因为 input signals (constraints)
      non-discriminative。Any aggregation over non-discriminative signals degenerates to
      counting, which ≈ voting。

  # ============================================================
  # P2 Experiments
  # ============================================================
  - name: constraint_quality_case_studies
    plan_id: exp-008
    description: "8 representative problems 定性分析: constraints 为何 non-discriminative"
    expected_results:
      n_case_studies: 8
      correct_trace_precision: 0.52
      incorrect_trace_precision: 0.48
      constraint_overlap_rate: 0.78
      typical_constraint_types:
        - "conditional (if-then)"
        - "universal quantifier (forall)"
        - "negation"
        - "predicate application"
      discriminative_constraints_pct: 0.12
    result_rationale: >
      Non-discrimination 的 root cause: LLM 提取的 constraints 主要 formalize 题目
      premises (前提条件) 而非 reasoning steps (推理步骤)。Premises 对正确/错误 traces
      共享 (都正确读取了题目)——constraint overlap rate 78%。推理错误发生在 inference
      chain 更深位置: 这些错误要么不被 formalized (extraction 跳过复杂推导), 要么被
      formalized 为看起来合理但语义不同的 constraints (surface structure 相似)。
      仅 12% constraints 是 truly discriminative (只出现在正确或只出现在错误 traces),
      且方向随机 (一半 favor correct, 一半 favor incorrect)。
    tables: []
    figures_description:
      - >
        Appendix case study: side-by-side 正确 trace 和错误 trace 的 constraints。
        Highlighted: shared constraints (majority, ~78%) and trace-specific (minority, ~22%)。
        Caption: 'Most constraints formalize shared premises; trace-specific constraints
        are equally likely to support correct or incorrect answers.'
    analysis: >
      Case studies 提供定性理解, 补充 F2 定量证据。Reader 直观看到 WHY precision ≈ 0.50:
      constraints capture what the model reads (premises), not how it reasons (inference)。
      也解释 WHY MaxSAT ≈ count-only: 如果 constraints mostly shared, satisfiability
      structure carries no information about answer correctness。1-2 examples 进 §4.1,
      其余进 appendix。

  # ============================================================
  # What-if Experiments
  # ============================================================
  - name: temperature_ablation_t03_t05_t10
    plan_id: what-if-temp
    description: "T=0.3/0.5/1.0 on Qwen-14B D012 60q. Temperature 操控 diversity, 验证 trap 结构性"
    expected_results:
      dataset: D012
      model: Qwen2.5-14B-Instruct
      n: 60
      k: 12
      t03_c0_pct: 28.3
      t03_sc_accuracy: 0.767
      t03_sica_accuracy: 0.767
      t03_delta_pp: 0.0
      t03_discordant_sica: 1
      t03_discordant_sc: 1
      t03_mcnemar_p: 1.0
      t03_extraction_rate: 0.91
      t05_c0_pct: 41.7
      t05_sc_accuracy: 0.750
      t05_sica_accuracy: 0.750
      t05_delta_pp: 0.0
      t05_discordant_sica: 1
      t05_discordant_sc: 1
      t05_mcnemar_p: 1.0
      t05_extraction_rate: 0.90
      t10_c0_pct: 68.3
      t10_sc_accuracy: 0.700
      t10_sica_accuracy: 0.683
      t10_delta_pp: -1.7
      t10_discordant_sica: 1
      t10_discordant_sc: 2
      t10_mcnemar_p: 0.56
      t10_extraction_rate: 0.87
      baseline_t07_c0_pct: 53.3
      baseline_t07_delta_pp: 0.0
      c0_monotonic_increase: true
      c0_sequence: "28.3% → 41.7% → 53.3% → 68.3%"
      max_abs_delta_pp: 1.7
      all_p_gt_020: true
    result_rationale: >
      Temperature 直接控制 sampling distribution entropy, 因此 C0 随 T 单调递增:
      T=0.3 时 logit distribution 尖锐, traces 集中到 modal answer, 仅 17 题多候选;
      T=1.0 时分布平坦, 41 题多候选。这是 structural: T→entropy→C0 是因果链。

      SC accuracy 随 T 先平后降: T=0.3-0.7 SC≈73-77% (集中在正确答案近邻),
      T=1.0 SC 降到 70% (更多随机错误破坏多数票)。已知 SC behavior。

      SICA-SC gap 在所有 T 下 |Δ| ≤ 1.7pp:
      - T=0.3 (C0=28%): 仅 17 题多候选, 1 discordant, 1:1 → Δ=0。少数 multi-candidate
        问题上 constraints 恰好一胜一负。
      - T=0.5 (C0=42%): 25 题多候选, constraints 仍 non-discriminative → Δ=0。
        更多 problems 可操作, 但操作方向随机。
      - T=1.0 (C0=68%): 41 题多候选, constraints 质量因 noisier traces 进一步下降
        (高温 traces 更长、更散漫, extraction noise 增加) → Δ=-1.7pp。MaxSAT 在
        嘈杂 constraints 上做了一次净错误排除。

      All p>0.20 at n=60 (SE≈5-6pp)。True effect = 0 at all temperatures。
    tables:
      - "§5 Table: Temperature ablation (T × C0 × SC × SICA × Δ)"
    figures_description:
      - >
        §5 Figure (dual-axis): Left y=C0 (blue bars), 单调递增 28→42→53→68。
        Right y=SICA-SC gap (red line+dots), 平坦在 0 附近, error bars 均跨零。
        X-axis: T (0.3, 0.5, 0.7, 1.0)。Caption: 'Increasing temperature monotonically
        increases output diversity (C0) but does not improve SICA over SC, confirming
        the capability trap is structural, not a tuning failure.'
      - >
        Alternative: 2×2 panel, each T 一个 mini bar chart (SC vs SICA)。
        C0 标注在每个 panel 上。Visual: bars 等高, C0 label 递增。
    analysis: >
      Temperature ablation 是论文最强 causal evidence: 通过实验操控 diversity (非仅
      跨模型观察), 确认 diversity↑ 不改善 SICA。排除 confounders: 同一模型、同一数据、
      只改 T, C0 从 28% 到 68% 连续变化, gap 恒为 0。如 reviewer 问 'maybe you
      haven't found the right diversity level': this answers definitively — we swept
      the full range, it doesn't help。与 F2 互补: F2 shows WHY (precision≈0.50),
      temp ablation shows THAT (gap=0 at all diversity levels)。§5 new evidence for
      EMNLP submission。

  - name: gsm8k_pilot_30q
    plan_id: what-if-gsm8k
    description: "等同 exp-012。Qwen-14B on GSM8K 30q, 数学推理域 pilot"
    expected_results:
      note: "同 exp-012, 参见上方 gsm8k_pilot_14b entry"
      n: 30
      k: 12
      sica_accuracy: 0.867
      sc_accuracy: 0.867
      delta_pp: 0.0
      multi_candidate_rate: 0.10
      extraction_rate: 0.75
      model: Qwen2.5-14B-Instruct
      dataset: GSM8K
    result_rationale: >
      与 exp-012 相同实验。14B 在 GSM8K accuracy ~87%, C0 ~10%。数学推理的 open-ended
      answer space (具体数字) 理论上增加 diversity, 但 14B 能力收敛到正确数值。
      Extraction rate 偏低 (75%) 因为数值计算难以 FOL 化。SICA ≡ SC。
      作为 appendix cross-domain data point, 为 'what about math' reviewer concern
      提供证据。
    tables:
      - "Appendix: GSM8K row (同 exp-012)"
    figures_description:
      - "F4 data point: GSM8K C0=10%, Δ=0"
    analysis: >
      与 exp-012 完全重复。收录条件: 如果 GPU budget 允许, 作为第四个 domain 进入
      appendix (主文已有 FOLIO + StrategyQA + ARC + ProofWriter 四域)。
```

**一致性验证摘要**:
- **n_exp_positive_p_below_010 = 0**: 全部实验 p > 0.10 (最小 p = 0.13 at exp-017)
- **temp_max_abs_delta_pp = 1.7**: 在 [0, 3.0] 范围内
- **f2_constraint_precision_mean = 0.505**: 在 [0.48, 0.53] 范围内
- **f2_precision_vs_entropy_slope = 0.003**: 在 [-0.02, 0.02] 范围内
- **aggregate weighted |Δ| = +0.20pp**: 在 [0, 0.8] 范围内
- **c0_scaling_distinct_levels = 3** (Qwen 7B/14B/72B: 65%/53%/15%): 在 [3, 5] 范围内
- **discordant SICA winrate = 34/67 = 50.7%**: 在 [0.42, 0.55] 范围内

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3530220-8359-40e0-99e7-4acf2bc45258",
  "isSidechain": false,
  "requestId": "req_011Cb8L3BmBxyXQfuUr2Dbeq",
  "type": "assistant",
  "uuid": "8925bb39-eefe-421c-bdc8-5040fe6f9a4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjZshHmiK3n27YHkSie6Mc",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3360,
      "cache_read_input_tokens": 30556,
      "output_tokens": 52018,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3360,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 52018,
          "cache_read_input_tokens": 30556,
          "cache_creation_input_tokens": 3360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3360
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Capability trap 被结构性确认: diversity 可操控但 SICA 收益恒零; F2 per-problem 清晰展示 constraint 非判别性; 三条 claims 原样保留 核心假设：['Temperature ablation: C0 随 T 单调递增 (T=0.3 C0≈25…",
  "leafUuid": "8925bb39-eefe-421c-bdc8-5040fe6f9a4b",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Temperature ablation validates capability trap mechanism",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Capability trap 被结构性确认: diversity 可操控但 SICA 收益恒零; F2 per-problem 清晰展示 constraint 非判别性; 三条 claims 原样保留 核心假设：['Temperature ablation: C0 随 T 单调递增 (T=0.3 C0≈25…",
  "leafUuid": "8925bb39-eefe-421c-bdc8-5040fe6f9a4b",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Temperature ablation validates capability trap mechanism",
  "sessionId": "ac90f59c-9ff1-4501-bfdb-c836f1ffbc83"
}
```

---
