# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：核心 null 成立但边缘条件有噪声；F2 图可解读但需引导；部分 claim 措辞需软化 核心假设：['exp-012 GSM8K: C0 在 2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/e39c49cf-e3c1-4b30-97fe-e5ae0623d229.jsonl`
- **Structured JSON:** [`839cd357fb34f6fb141f.json`](../../sessions/83/839cd357fb34f6fb141f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T16:56:35.490Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T16:56:35.490Z",
  "sessionId": "e39c49cf-e3c1-4b30-97fe-e5ae0623d229",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：核心 null 成立但边缘条件有噪声；F2 图可解读但需引导；部分 claim 措辞需软化\n核心假设：['exp-012 GSM8K: C0 在 20-35%（高于预期），SICA≈SC 但 CI 宽，无法排除小正效应', 'F2 per-problem scatter 有异质性：部分子域 constraint precision 0.53-0.58，略高于随机但不足以翻转 aggregation 结果', 'exp-011 LLaMA-8B D012 +6.67pp (n=60) 被 reviewer 追问为 underpowered positive signal，需在 paper 中显式讨论', 'exp-013 ablation 基于 proxy（非原始 z3 formulas），reviewer 要求 robustness check 或 acknowledge limitation', 'Oracle 仅 FOLIO 单域，reviewer 要求 generalizability limitation paragraph']\n关键指标范围：{'remaining_max_abs_delta_pp': [2.0, 5.0], 'constraint_precision_mean': [0.5, 0.56], 'constraint_precision_vs_c0_r': [-0.15, 0.25], 'gsm8k_c0_pct': [18, 35], 'gsm8k_delta_pp': [-3.0, 3.0], 'combined_N_all_conditions': [1300, 1500], 'meta_analytic_delta_pp': [-0.5, 1.5], 'oracle_gap_pp': [8.0, 9.5], 'f2_non_discriminative_fraction': [0.7, 0.85]}\n叙事方向：Capability trap framing 基本成立但需精确化。Claim 1: 'lack discriminative power' → 'lack sufficient discriminative power in tested conditions'。Claim 2: 'empirically empty' → 'no condition achieves significant gains'（承认 underpowered 条件模糊性）。Claim 3: C0 necessary condition 成立但 insufficient 证据需更多 hedging。可能需对 LLaMA-8B 一个条件补 powered replication。论文从 'definitive characterization' 退为 'systematic empirical study with provisional characterization'。仍 EMNLP competitive，contribution 偏 benchmark+diagnostic 而非 mechanism insight。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\nfocus: Oracle experiment (exp-021) is the key new result: gold FOL + MAX-SAT = +8.82pp over SC (p<0.001), while self-extracted SICA = SC. This causally separates extraction failure from aggregation failure. Title/claims now scoped to self-extracted constraints (not symbolic consensus broadly). Temperature ablation shows C0 varies 30-43% but gap stays 0. Paper now has constructive direction (better extraction unlocks +8.82pp potential).\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)\n\n1. **The Capability Trap**: LLM self-extracted FOL constraint aggregation faces a fundamental tension: it requires output diversity (C0>20%) to differ from voting, but self-extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to counting. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B). [Scope: this finding characterizes same-model self-extraction pipelines; methods using external verifiers or trained extractors may not share this limitation.]\n2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.\n3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.\n\n## Core Insight\nLLM self-extracted FOL constraints don't improve majority voting because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these self-extracted constraints lack the discriminative power to distinguish correct from incorrect answers (precision ~0.50, no better than chance). MAX-SAT optimization over such non-discriminative constraints degenerates to counting, performing no better than simple majority voting.\n\n**Critical oracle result (exp-021)**: When gold FOL annotations replace self-extracted constraints, Oracle-SICA achieves +8.82pp over SC (p<0.001, n=204). This proves the MAX-SAT aggregation mechanism IS effective given discriminative constraints — the bottleneck is exclusively in LLM self-extraction quality, not in the aggregation paradigm itself.\n\nWe provide the first systematic empirical study (a) precisely localizing the failure mode to extraction quality via oracle control, (b) quantifying constraint non-discrimination at per-problem granularity (n=307), and (c) proving MAX-SAT adds nothing beyond counting when constraints lack discriminative power. [Positioning: Logic-LM and LINC documented that LLM-to-FOL translation is error-prone; our contribution is the oracle-controlled causal separation of extraction vs aggregation failure, plus systematic quantification and C0 as deployment diagnostic.]\n\n## Story Spine\n- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?\n- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.\n- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.\n- **Headline result**: \"Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis\n3. **\"Only Qwen models\"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B\n4. **\"Only one reasoning model\"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)\n5. **\"Only logic domain\"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.\n6. **\"MAX-SAT is over-engineering\"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.\n7. **\"Random tiebreak baseline\"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.\n8. **\"Why not just use a reasoning model?\"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.\n9. **\"How does this compare to Logic-LM / LINC?\"** → exp-015: Logic-LM × K baseline (CPU-only)\n10. **\"Weighted SC is simpler\"** → exp-016: Weighted SC baseline (CPU-only)\n11. **\"C0 is trivially derived\"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.\n12. **\"Within-family scaling?\"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.\n13. **\"Self-extraction confound — same model generates and extracts\"** → exp-021 Oracle FOLIO: **RESOLVED.** Gold FOL + Z3 + MAX-SAT = 88.24% vs SC = 79.41% (+8.82pp, p=6.15e-05). Aggregation mechanism IS effective with discriminative constraints. Bottleneck conclusively localized to LLM self-extraction quality. This is now a core contribution, not just a defensive experiment.\n14. **\"Published methods achieve gains on same benchmarks (DyLoS, Aristotle, FoVer)\"** → Acknowledge in Related Work and Discussion. Key distinction: those methods use trained/external verifiers, multi-paradigm solver selection, or logic-complete decomposition — all fundamentally different from same-model self-extraction. Our finding characterizes the specific failure mode of self-extraction pipelines, not symbolic reasoning broadly.\n15. **\"MAX-SAT formulation is just weighted voting\"** → Paper must explicitly describe cross-answer evaluation: constraints from trace t_i ARE/ARE NOT evaluated against other candidates. If structurally a weighted vote, acknowledge and frame contribution as \"even the most charitable interpretation (weighted vote with constraint-based weights) provides no gain.\"\n\n## Working Title\n**\"The Capability Trap: Why Self-Extracted Constraints Cannot Improve LLM Majority Voting\"**\n(Alternatives: \n- \"Diversity Without Discrimination: A Systematic Study of LLM-Extracted Constraint Aggregation\"\n- \"When Does Symbolic Aggregation Help? Characterizing the Failure Mode of Self-Extracted FOL Constraints\")\n\nNOTE (Dream D037): Title MUST be scoped to \"self-extracted constraints\" / \"SICA\" — NOT \"symbolic consensus\" broadly. Published methods (DyLoS, Aristotle, FoVer, LogicAgent) achieve gains on same benchmarks using different symbolic approaches. Our evidence covers one pipeline (same-model FOL extraction + MAX-SAT), not the entire paradigm.\n\n## Paper Structure (EMNLP 8pp + appendix)\n- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Oracle Control: Gold-FOL+MAX-SAT vs SC vs SICA-self, the key causal separation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Temperature Ablation: C0 varies 30-43% but Δ=0 throughout)\n- Main Figures: F1 (Method Pipeline), F2 (Per-problem scatter: vote entropy vs constraint exclusion rate, colored by flip type, n=307 multi-candidate problems from exp-001 — hero figure showing constraints fail to discriminate), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: experiment-level conditions, marker size ∝ sqrt(n), showing no correlation between diversity and SICA effectiveness)\n- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data\n\n## Claim Risk Notes (Updated D035 + exp-014)\n- **Claim 1 mechanism refinement**: \"Inverse correlation between diversity and quality\" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: \"constraints lack discriminative power regardless of diversity level.\" Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.\n- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.\n- **Claim 3 gradient → independence framing**: Temperature ablation confirms C0 varies (30%→38%→43%) but gap stays flat at 0.00pp (zero discordant across all temperatures). Data supports \"diversity is necessary but insufficient\" NOT \"gradient diagnostic.\" Claim 3 should be: \"C0 predicts when SICA cannot help (C0<5% → degenerate), but increasing diversity beyond the threshold provides no benefit — constraint quality remains the binding bottleneck regardless of diversity level.\" RESOLVED (temperature data in hand).\n- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.\n- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.\n\n## Required Citations (Dream D037 — minimum 30 references)\n\nPaper Agent MUST include these categories (non-exhaustive list of must-cite works):\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 ACL Findings (confidence-weighted SC), DiVeRSe (Li et al. 2023)\n- **Neuro-symbolic reasoning (positive results on same benchmarks)**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\n- **Test-time compute scaling**: Snell et al. 2025 (ICLR Oral), DeepSeek-R1 technical report (Nature 2025), Diversity-Aware Training for TTS (2025)\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd (Wang et al. 2024)\n- **Constraint satisfaction in NLP**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\n- **Negative results in NLP**: appropriate precedents for analysis/negative-result papers\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\n- **Reasoning model paradigm**: QwQ technical blog, o1 (OpenAI 2024)\n\n## Claim Scoping Rules (Dream D037)\n\n- n=60 conditions: present as \"suggestive/consistent with\" NOT \"confirming.\" Only n≥200 conditions can \"confirm\" null.\n- Combined N>1,300: acceptable if clearly stated that 804/1300 come from powered Qwen-14B condition.\n- Domain coverage: acknowledge that SICA operates meaningfully (C0>20%) primarily on formal logic; other domains are degenerate (C0<10%) due to model capability.\n- \"Capability trap\" framing: position as systematic quantification of a known challenge (not discovery). Our specific contributions: (a) per-problem precision analysis at n=307 granularity, (b) constraint ablation proving MAX-SAT ≈ counting, (c) C0 as deployment diagnostic.\n\n## Venue Fit Risks\n- EMNLP: Negative-results/analysis paper. Must answer \"so what should practitioners do?\" → C0 as deployment diagnostic + overhead analysis.\n- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.\n- Statistical power: Now strong (N>1,200 combined across powered tests).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes\n    odd K=11 to test if SICA value persists without exact ties. Key questions: does\n    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency\n    change with K?'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如\n    gap>0 → SICA has value beyond tiebreaking。\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Within-Qwen scaling dimension.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX\n    PRO 6000 单卡可放。\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。\n- id: exp-010\n  name: sica_mistral_7b\n  claim:\n  - 2\n  - 3\n  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family\n    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''\n    attack.'\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: DONE\n  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+\n    题（~3h GPU，margin 允许）。'\n  registry_id: exp-010-mistral-v3\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- id: exp-011\n  name: sica_llama_8b\n  claim:\n  - 2\n  - 3\n  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.\n    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation\n    同 exp-010。\n- id: exp-012\n  name: gsm8k_pilot_14b\n  claim:\n  - 2\n  - 3\n  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:\n    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer\n    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain\n    win.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable\n    insight.\n- id: exp-013\n  name: constraint_ablation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count\n    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:\n    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability\n    trap.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability\n    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'\n- id: exp-014\n  name: sica_deepseek_r1_llama_8b\n  claim:\n  - 2\n  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning\n    model data point with LLaMA base architecture: validates C0<5% generalizes beyond\n    QwQ-32B AND eliminates ''still Qwen family'' attack.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。\n- id: exp-015\n  name: logic_lm_baseline\n  claim:\n  - 1\n  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style\n    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT\n    multi-trace aggregation adds value beyond FOL extraction itself.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL\n    constraints 做单 trace verification then vote。'\n- id: exp-016\n  name: weighted_sc_baseline\n  claim:\n  - 1\n  - 3\n  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes\n    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.\n    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),\n    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count\n    weighted (no SAT)。'\n- id: exp-017\n  name: sica_strategyqa_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning\n    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected\n    constraint quality. Tests capability trap in best-case-diversity scenario.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability\n    trap（diversity high but quality low → no gain）。\n- id: exp-018\n  name: sica_arc_challenge_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,\n    4-choice format. Tests constraint mechanism in multi-choice scenario + different\n    domain.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)\n    + StrategyQA (binary) 形成答案格式多样性。\n- id: exp-019\n  name: constraint_quality_correlation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only analysis: compute constraint precision per domain × model,\n    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality\n    correlation. Uses data from exp-001/010/011/017/018.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-017\n  - exp-018\n  status: planned\n  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent\n    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have\n    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K6_sica: 0.733\n    K6_sc: 0.733\n    K6_gap_pp: 0\n    K8_sica: 0.733\n    K8_sc: 0.75\n    K8_gap_pp: -1.7\n    K11_sica: 0.733\n    K11_sc: 0.733\n    K11_gap_pp: 0\n    K12_sica: 0.7\n    K12_sc: 0.75\n    K12_gap_pp: -5\n    K16_sica: 0.717\n    K16_sc: 0.75\n    K16_gap_pp: -3.3\n    K20_sica: 0.7\n    K20_sc: 0.733\n    K20_gap_pp: -3.3\n    all_K_sica_leq_sc: true\n    larger_K_degrades_sica: true\n- exp_id: sica_constraint_ablation_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    maxsat_accuracy: 0.7649\n    count_only_accuracy: 0.7662\n    random_weight_accuracy: 0.7637\n    sc_baseline_accuracy: 0.7624\n    n_problems: 804\n    agreement_802_of_804: true\n    mcnemar_p_all_gt_0.7: true\n    note: approximate (raw z3 formulas unavailable, count-only/random-weight use proxy)\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwq_aggregate_c0_nominal_pct: 10.3\n    qwq_aggregate_c0_effective_pct: 2.6\n    qwen14b_c0_pct: 46\n    diversity_ratio_effective: 17.7\n    aime_delta_pp: 0\n    proofwriter_delta_pp: -5.9\n    aime_n: 22\n    proofwriter_n: 17\n    temp_diversity_n: 5\n    folio_n: 2\n    total_problems: 46\n    c0_threshold: 20\n    qwq_below_threshold: true\n- exp_id: exp-011-llama8b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-016-weighted-sc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7649\n    sc_uniform_accuracy: 0.7624\n    inv_length_accuracy: 0.7674\n    length_weighted_accuracy: 0.7525\n    constraint_count_accuracy: 0.7525\n    inv_length_vs_sc_p: 0.453\n    length_vs_sc_p: 0.153\n    inv_length_vs_sica_p: 0.864\n    length_vs_sica_p: 0.066\n    n_problems: 804\n    all_nonsignificant: true\n- exp_id: exp-010-mistral\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-011-llama8b-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-018-arc\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.5667\n    sc_accuracy: 0.5333\n    delta_pp: 3.33\n    mcnemar_chi2: 0.5\n    mcnemar_p: n.s.\n    bootstrap_ci_95:\n    - 0\n    - 8.33\n    bootstrap_p_delta_le_0: 0.1346\n    multi_candidate_rate: 0.1\n    contradiction_detected: 5\n    extraction_rate_problem: 1\n    extraction_rate_trace: 0.704\n    discordant_sica_wins: 2\n    discordant_sc_wins: 0\n- exp_id: pilot-constraint-filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 43\n    thresholds_tested:\n    - 1\n    - 2\n    - 3\n    - 5\n    - 7\n    best_gap_pp: 2.33\n    best_T: 1\n    sica_T1: 0.7674\n    sc: 0.7442\n    T5_gap: 0\n    T7_gap: 0\n    discriminative_ratio_count: 0.115\n    discriminative_ratio_weight: 0.372\n    effective_flip_rate: 0.174\n    multi_answer_problems: 23\n    unanimous_problems: 20\n    problems_disc_favors_different: 4\n- exp_id: exp-018-arc-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.95\n    sc_accuracy: 0.9667\n    delta_pp: -1.67\n    multi_candidate_rate: 0.05\n    extraction_rate: 1\n    contradiction_detected: 3\n    discordant_sica_wins: 0\n    discordant_sc_wins: 1\n    dataset: ARC-Challenge\n    model: Qwen2.5-14B-Instruct\n- exp_id: exp-011-llama8b-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6667\n    sc_accuracy: 0.6\n    delta_pp: 6.67\n    multi_candidate_rate: 0.6167\n    extraction_rate: 0.8556\n    answer_extraction_rate: 0.8958\n    contradiction_rate: 0.0527\n    problems_with_contradictions: 43\n    truncated_traces: 44\n    discordant_sica_wins: 5\n    discordant_sc_wins: 1\n    mcnemar_p: 0.2188\n    proofwriter_sica: 0.6333\n    proofwriter_sc: 0.6\n    proofwriter_delta_pp: 3.33\n    folio_sica: 0.7\n    folio_sc: 0.6\n    folio_delta_pp: 10\n    model: LLaMA-3.1-8B-Instruct\n    dataset: D012\n    wall_time_min: 66.4\n- exp_id: pilot-contrastive-prompt\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- exp_id: exp-019-llama8b-strategyqa-200\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    k: 12\n    sica_accuracy: 0.74\n    sc_accuracy: 0.72\n    delta_pp: 2\n    multi_candidate_rate: 0.41\n    mcnemar_p: 0.424\n    bootstrap_ci_95:\n    - -1.5\n    - 5.5\n    bootstrap_p_delta_le_0: 0.12\n    discordant_sica_wins: 9\n    discordant_sc_wins: 5\n    discordant_total: 14\n    discordant_rate: 0.07\n    sc_unanimous_rate: 0.545\n    model: LLaMA-3.1-8B-Instruct\n    dataset: StrategyQA\n    wall_time_min: 52\n- exp_id: exp-020-llama8b-folio-204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.608\n    sc_accuracy: 0.632\n    delta_pp: -2.45\n    mcnemar_p: 0.2668\n    bootstrap_ci_95:\n    - -5.88\n    - 0.98\n    bootstrap_p_sica_ge_sc: 0.1\n    discordant_sica_wins: 4\n    discordant_sc_wins: 9\n    discordant_total: 13\n    discordant_rate: 0.064\n    multi_candidate_rate: 0.618\n    extraction_rate: 0.942\n    answer_extraction_rate: 0.951\n    contradiction_rate: 0.062\n    both_wrong: 71\n    model: LLaMA-3.1-8B-Instruct\n    dataset: FOLIO-204\n    wall_time_min: 131.7\n- exp_id: exp-009-overhead-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 804\n    mean_total_wall_s: 61.6\n    mean_trace_gen_s: 31.6\n    trace_gen_pct: 51.3\n    mean_extract_s: 29\n    extract_pct: 47\n    mean_dedup_s: 1\n    dedup_pct: 1.6\n    mean_maxsat_s: 0.003\n    maxsat_pct: 0.005\n    sica_overhead_s: 30\n    sica_overhead_pct: 48.7\n    pw_overhead_pct: 51.3\n    folio_overhead_pct: 38.6\n    p50_overhead_pct: 48.9\n    p90_overhead_pct: 57.6\n- exp_id: exp-014-deepseek-r1-7b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6833\n    sc_accuracy: 0.7167\n    delta_pp: -3.33\n    multi_candidate_rate: 0.583\n    extraction_rate: 0.839\n    answer_extraction_rate: 0.939\n    truncated_traces: 72\n    contradiction_rate: 0.037\n    wall_time_min: 100.3\n    mcnemar_p: 0.4795\n    discordant_sica_wins: 0\n    discordant_sc_wins: 2\n    model: DeepSeek-R1-Distill-Qwen-7B\n    dataset: D012\n- exp_id: temperature-ablation-t03\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7333\n    delta_pp: 0\n    multi_candidate_rate: 0.3\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 0.3\n- exp_id: temperature-ablation-t05\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.7667\n    sc_accuracy: 0.7667\n    delta_pp: 0\n    multi_candidate_rate: 0.383\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 0.5\n- exp_id: temperature-ablation-t10\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.75\n    sc_accuracy: 0.75\n    delta_pp: 0\n    multi_candidate_rate: 0.433\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 1\n- exp_id: exp-021-oracle-folio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    oracle_sica_accuracy: 0.8824\n    sc_accuracy: 0.7941\n    sica_self_accuracy: 0.7941\n    oracle_vs_sc_delta_pp: 8.82\n    oracle_vs_sica_delta_pp: 8.82\n    mcnemar_p_oracle_vs_sc: 6.15e-05\n    z3_gold_agreement: 0.946\n    fol_parse_success: 1\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n    constraint_source: gold FOL annotations\n- exp_id: exp-012-gsm8k-pilot\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T16:56:35.494Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T16:56:35.494Z",
  "sessionId": "e39c49cf-e3c1-4b30-97fe-e5ae0623d229"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-17T16:56:35.519Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：核心 null 成立但边缘条件有噪声；F2 图可解读但需引导；部分 claim 措辞需软化
核心假设：['exp-012 GSM8K: C0 在 20-35%（高于预期），SICA≈SC 但 CI 宽，无法排除小正效应', 'F2 per-problem scatter 有异质性：部分子域 constraint precision 0.53-0.58，略高于随机但不足以翻转 aggregation 结果', 'exp-011 LLaMA-8B D012 +6.67pp (n=60) 被 reviewer 追问为 underpowered positive signal，需在 paper 中显式讨论', 'exp-013 ablation 基于 proxy（非原始 z3 formulas），reviewer 要求 robustness check 或 acknowledge limitation', 'Oracle 仅 FOLIO 单域，reviewer 要求 generalizability limitation paragraph']
关键指标范围：{'remaining_max_abs_delta_pp': [2.0, 5.0], 'constraint_precision_mean': [0.5, 0.56], 'constraint_precision_vs_c0_r': [-0.15, 0.25], 'gsm8k_c0_pct': [18, 35], 'gsm8k_delta_pp': [-3.0, 3.0], 'combined_N_all_conditions': [1300, 1500], 'meta_analytic_delta_pp': [-0.5, 1.5], 'oracle_gap_pp': [8.0, 9.5], 'f2_non_discriminative_fraction': [0.7, 0.85]}
叙事方向：Capability trap framing 基本成立但需精确化。Claim 1: 'lack discriminative power' → 'lack sufficient discriminative power in tested conditions'。Claim 2: 'empirically empty' → 'no condition achieves significant gains'（承认 underpowered 条件模糊性）。Claim 3: C0 necessary condition 成立但 insufficient 证据需更多 hedging。可能需对 LLaMA-8B 一个条件补 powered replication。论文从 'definitive characterization' 退为 'systematic empirical study with provisional characterization'。仍 EMNLP competitive，contribution 偏 benchmark+diagnostic 而非 mechanism insight。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: symb_invariant_consensus
focus: Oracle experiment (exp-021) is the key new result: gold FOL + MAX-SAT = +8.82pp over SC (p<0.001), while self-extracted SICA = SC. This causally separates extraction failure from aggregation failure. Title/claims now scoped to self-extracted constraints (not symbolic consensus broadly). Temperature ablation shows C0 varies 30-43% but gap stays 0. Paper now has constructive direction (better extraction unlocks +8.82pp potential).

## paper_framing.md

# Paper Framing — symb_invariant_consensus

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25)
- Deadline: May 25, 2026 (ARR submission)

## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)

1. **The Capability Trap**: LLM self-extracted FOL constraint aggregation faces a fundamental tension: it requires output diversity (C0>20%) to differ from voting, but self-extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to counting. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B). [Scope: this finding characterizes same-model self-extraction pipelines; methods using external verifiers or trained extractors may not share this limitation.]
2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.
3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.

## Core Insight
LLM self-extracted FOL constraints don't improve majority voting because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these self-extracted constraints lack the discriminative power to distinguish correct from incorrect answers (precision ~0.50, no better than chance). MAX-SAT optimization over such non-discriminative constraints degenerates to counting, performing no better than simple majority voting.

**Critical oracle result (exp-021)**: When gold FOL annotations replace self-extracted constraints, Oracle-SICA achieves +8.82pp over SC (p<0.001, n=204). This proves the MAX-SAT aggregation mechanism IS effective given discriminative constraints — the bottleneck is exclusively in LLM self-extraction quality, not in the aggregation paradigm itself.

We provide the first systematic empirical study (a) precisely localizing the failure mode to extraction quality via oracle control, (b) quantifying constraint non-discrimination at per-problem granularity (n=307), and (c) proving MAX-SAT adds nothing beyond counting when constraints lack discriminative power. [Positioning: Logic-LM and LINC documented that LLM-to-FOL translation is error-prone; our contribution is the oracle-controlled causal separation of extraction vs aggregation failure, plus systematic quantification and C0 as deployment diagnostic.]

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
13. **"Self-extraction confound — same model generates and extracts"** → exp-021 Oracle FOLIO: **RESOLVED.** Gold FOL + Z3 + MAX-SAT = 88.24% vs SC = 79.41% (+8.82pp, p=6.15e-05). Aggregation mechanism IS effective with discriminative constraints. Bottleneck conclusively localized to LLM self-extraction quality. This is now a core contribution, not just a defensive experiment.
14. **"Published methods achieve gains on same benchmarks (DyLoS, Aristotle, FoVer)"** → Acknowledge in Related Work and Discussion. Key distinction: those methods use trained/external verifiers, multi-paradigm solver selection, or logic-complete decomposition — all fundamentally different from same-model self-extraction. Our finding characterizes the specific failure mode of self-extraction pipelines, not symbolic reasoning broadly.
15. **"MAX-SAT formulation is just weighted voting"** → Paper must explicitly describe cross-answer evaluation: constraints from trace t_i ARE/ARE NOT evaluated against other candidates. If structurally a weighted vote, acknowledge and frame contribution as "even the most charitable interpretation (weighted vote with constraint-based weights) provides no gain."

## Working Title
**"The Capability Trap: Why Self-Extracted Constraints Cannot Improve LLM Majority Voting"**
(Alternatives: 
- "Diversity Without Discrimination: A Systematic Study of LLM-Extracted Constraint Aggregation"
- "When Does Symbolic Aggregation Help? Characterizing the Failure Mode of Self-Extracted FOL Constraints")

NOTE (Dream D037): Title MUST be scoped to "self-extracted constraints" / "SICA" — NOT "symbolic consensus" broadly. Published methods (DyLoS, Aristotle, FoVer, LogicAgent) achieve gains on same benchmarks using different symbolic approaches. Our evidence covers one pipeline (same-model FOL extraction + MAX-SAT), not the entire paradigm.

## Paper Structure (EMNLP 8pp + appendix)
- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Oracle Control: Gold-FOL+MAX-SAT vs SC vs SICA-self, the key causal separation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Temperature Ablation: C0 varies 30-43% but Δ=0 throughout)
- Main Figures: F1 (Method Pipeline), F2 (Per-problem scatter: vote entropy vs constraint exclusion rate, colored by flip type, n=307 multi-candidate problems from exp-001 — hero figure showing constraints fail to discriminate), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: experiment-level conditions, marker size ∝ sqrt(n), showing no correlation between diversity and SICA effectiveness)
- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data

## Claim Risk Notes (Updated D035 + exp-014)
- **Claim 1 mechanism refinement**: "Inverse correlation between diversity and quality" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: "constraints lack discriminative power regardless of diversity level." Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.
- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.
- **Claim 3 gradient → independence framing**: Temperature ablation confirms C0 varies (30%→38%→43%) but gap stays flat at 0.00pp (zero discordant across all temperatures). Data supports "diversity is necessary but insufficient" NOT "gradient diagnostic." Claim 3 should be: "C0 predicts when SICA cannot help (C0<5% → degenerate), but increasing diversity beyond the threshold provides no benefit — constraint quality remains the binding bottleneck regardless of diversity level." RESOLVED (temperature data in hand).
- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.
- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.

## Required Citations (Dream D037 — minimum 30 references)

Paper Agent MUST include these categories (non-exhaustive list of must-cite works):
- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 ACL Findings (confidence-weighted SC), DiVeRSe (Li et al. 2023)
- **Neuro-symbolic reasoning (positive results on same benchmarks)**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)
- **Test-time compute scaling**: Snell et al. 2025 (ICLR Oral), DeepSeek-R1 technical report (Nature 2025), Diversity-Aware Training for TTS (2025)
- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd (Wang et al. 2024)
- **Constraint satisfaction in NLP**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)
- **Negative results in NLP**: appropriate precedents for analysis/negative-result papers
- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023
- **Reasoning model paradigm**: QwQ technical blog, o1 (OpenAI 2024)

## Claim Scoping Rules (Dream D037)

- n=60 conditions: present as "suggestive/consistent with" NOT "confirming." Only n≥200 conditions can "confirm" null.
- Combined N>1,300: acceptable if clearly stated that 804/1300 come from powered Qwen-14B condition.
- Domain coverage: acknowledge that SICA operates meaningfully (C0>20%) primarily on formal logic; other domains are degenerate (C0<10%) due to model capability.
- "Capability trap" framing: position as systematic quantification of a known challenge (not discovery). Our specific contributions: (a) per-problem precision analysis at n=307 granularity, (b) constraint ablation proving MAX-SAT ≈ counting, (c) C0 as deployment diagnostic.

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
  status: DONE
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.7333
    sc_accuracy: 0.7333
    delta_pp: 0
    multi_candidate_rate: 0.3
    discordant_total: 0
    model: Qwen2.5-14B-Instruct
    dataset: D012
    temperature: 0.3
- exp_id: temperature-ablation-t05
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.7667
    sc_accuracy: 0.7667
    delta_pp: 0
    multi_candidate_rate: 0.383
    discordant_total: 0
    model: Qwen2.5-14B-Instruct
    dataset: D012
    temperature: 0.5
- exp_id: temperature-ablation-t10
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n: 60
    k: 12
    sica_accuracy: 0.75
    sc_accuracy: 0.75
    delta_pp: 0
    multi_candidate_rate: 0.433
    discordant_total: 0
    model: Qwen2.5-14B-Instruct
    dataset: D012
    temperature: 1
- exp_id: exp-021-oracle-folio
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n: 204
    k: 12
    oracle_sica_accuracy: 0.8824
    sc_accuracy: 0.7941
    sica_self_accuracy: 0.7941
    oracle_vs_sc_delta_pp: 8.82
    oracle_vs_sica_delta_pp: 8.82
    mcnemar_p_oracle_vs_sc: 6.15e-05
    z3_gold_agreement: 0.946
    fol_parse_success: 1
    model: Qwen2.5-14B-Instruct
    dataset: FOLIO-204
    constraint_source: gold FOL annotations
- exp_id: exp-012-gsm8k-pilot
  name: ''
  status: RUNNING
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
  "promptId": "7dfa7075-50be-45ac-97d4-bdf94c055805",
  "type": "user",
  "uuid": "15332bc4-158a-42f7-bae5-2b0f38ceed93",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e39c49cf-e3c1-4b30-97fe-e5ae0623d229",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T16:56:35.517Z_

```json
{
  "parentUuid": "15332bc4-158a-42f7-bae5-2b0f38ceed93",
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
  "uuid": "52d1dc04-b315-4bd8-a577-f88feb4bd22b",
  "timestamp": "2026-05-17T16:56:35.517Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e39c49cf-e3c1-4b30-97fe-e5ae0623d229",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T16:56:35.517Z_

```json
{
  "parentUuid": "52d1dc04-b315-4bd8-a577-f88feb4bd22b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c5b16cf5-8c14-435c-93de-a053b0a0be58",
  "timestamp": "2026-05-17T16:56:35.517Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e39c49cf-e3c1-4b30-97fe-e5ae0623d229",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 null 成立但边缘条件有噪声；F2 图可解读但需引导；部分 claim 措辞需软化 核心假设：['exp-012 GSM8K: C0 在 20-35%（高于预期），SICA≈SC 但 CI 宽，无法排除小正效应', 'F2 per-problem scatter 有异质性：部分子域 constra…",
  "leafUuid": "c5b16cf5-8c14-435c-93de-a053b0a0be58",
  "sessionId": "e39c49cf-e3c1-4b30-97fe-e5ae0623d229"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing LLM self-extracted constraint aggregation failure",
  "sessionId": "e39c49cf-e3c1-4b30-97fe-e5ae0623d229"
}
```

---

### Assistant

_source line 8 · 2026-05-17T16:57:21.261Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, based on the "median" tier definition. Let me carefully go through each planned experiment and generate predictions consistent with the median tier characteristics.

Let me review the median tier definition:
- Core null holds but edge conditions have noise
- F2 figure is interpretable but needs guidance
- Some claims need softened wording
- Key assumptions include things like GSM8K C0 at 20-35%, SICA≈SC but wide CI, per-problem scatter heterogeneity, LLaMA-8B underpowered positive signal, ablation based on proxy, Oracle only FOLIO


- Now I'm setting the specific metric ranges for the predicted data: remaining max absolute delta around 2-5 percentage points, constraint precision between 0.5-0.56, the correlation between constraint precision and C0 ranging from -0.15 to 0.25, GSM8K C0 performance in the 18-35% range, GSM8K deltas between -3 and 3 percentage points, total sample size across conditions between 1300-1500, meta-analytic effects from -0.5 to 1.5 percentage points, and oracle gap estimates between 8-9.5 percentage points.

Looking through the experiment plan now to identify which ones are actually planned versus already completed. I'm seeing some discrepancies between the plan status and what's in the registry—for instance, exp-002 is marked as planned but the registry shows a sensitivity analysis already done, exp-003 has a completion note despite being listed as planned, and exp-005 shows as done in the registry. I need to work through the full list to clarify which experiments still need to be executed. Looking at the remaining experiments in the registry - exp-017 through exp-019 - I see most have already been completed with real results, but the user is asking me to generate predicted median-tier data for all planned experiments regardless. Let me clarify what they're actually requesting: they want me to create simulated results across the median scenario for each experiment in the plan, treating this as a prediction exercise even where actual results already exist. I see there's a lot of planned experiments with completed registry entries, so I need to generate predicted results for all of them under the median tier scenario. Let me work through each experiment systematically—for the K ablation, I'd expect SICA to match SC across all K values with some noise, and odd K like 11 should show the tie-only mechanism clearly. The tiebreak baseline already has results but I'll apply median tier assumptions. For the 7B scaling test, a weaker model means higher initial constraint violation but similar SICA-SC behavior with maybe slight positive noise. I'll continue through the rest of the planned experiments with similar reasoning about how median tier conditions affect each result. The GSM8K pilot is currently running with C0 in the 20-35% range showing SICA≈SC, while constraint ablation shows MaxSAT performing equivalently to simpler baselines. DeepSeek-R1 reclassified as instruction-scale with high C0 and neutral or slightly negative SICA, and across Logic-LM, weighted SC variants, and StrategyQA experiments, I'm seeing consistent patterns where the signal remains weak or indistinguishable from the control.

Now looking at the remaining experiments—StrategyQA shows high C0 but low actual performance due to binary answers, ARC-Challenge has low C0 with SICA≈SC, and the constraint quality correlation analysis reveals only weak precision around 0.50-0.56 with no meaningful relationship to C0. I need to synthesize these results into the YAML output, generating predicted data consistent with the median tier patterns I'm observing across all these runs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5b16cf5-8c14-435c-93de-a053b0a0be58",
  "isSidechain": false,
  "requestId": "req_011Cb8VavvQaKb4qbAVtn3Qu",
  "type": "assistant",
  "uuid": "b4db2519-331f-465e-afcd-a4e90a2c0a3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e39c49cf-e3c1-4b30-97fe-e5ae0623d229",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LaAqqcYMjnMD3wUkWMYSvQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20366,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11650,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11650,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20366
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

_source line 9 · 2026-05-17T17:00:36.096Z_

```yaml
tier: median
narrative_guidance: >
  核心 null（SICA≈SC）在所有 powered 条件中成立，但 LLaMA-8B D012 (n=60) 出现 underpowered positive signal (+4.5pp, p≈0.22)，
  reviewer 会追问是否需要 powered replication。GSM8K C0 落在 25% 左右（高于预期），但 gap 仍≈0，strengthens "C0 necessary
  but insufficient" claim。F2 scatter 有明显异质性：部分 FOLIO 子问题 constraint precision 0.55，但 aggregated 仍
  non-discriminative。所有 claim 措辞需从 definitive 退到 systematic study。exp-013 ablation 基于 proxy 重构而非原始
  z3 公式，reviewer 会要求 acknowledge limitation 或 robustness check。Oracle 仅 FOLIO 单域，需写 generalizability
  limitation paragraph。论文仍 EMNLP competitive，contribution 偏 benchmark+diagnostic。

imagined_experiments:
  - name: sica_k_ablation_14b
    plan_id: exp-002
    description: "K=6,8,11,12,16,20 sensitivity on D012 60 questions"
    expected_results:
      K6_sica: 0.733
      K6_sc: 0.733
      K6_gap_pp: 0.0
      K8_sica: 0.750
      K8_sc: 0.750
      K8_gap_pp: 0.0
      K11_sica: 0.733
      K11_sc: 0.733
      K11_gap_pp: 0.0
      K12_sica: 0.733
      K12_sc: 0.700
      K12_gap_pp: 3.3
      K16_sica: 0.717
      K16_sc: 0.733
      K16_gap_pp: -1.7
      K20_sica: 0.700
      K20_sc: 0.717
      K20_gap_pp: -1.7
      odd_K11_gap: 0.0
      all_K_significant: false
      tie_fraction_K12: 0.083
      tie_fraction_K6: 0.0
    result_rationale: >
      Median 档下 K=11（奇数 K）gap 精确为 0，确认 SICA 的微小增益完全来自 tiebreak mechanism。
      偶数 K 出现 tie 概率 ~5-8%，SICA 在 tie 上胜率高（~80%），但 tie 太稀少无法产生 aggregate-level significance。
      K=12 出现 +3.3pp 是 D012 小样本噪声（n=60, SE≈6pp），exp-001 (n=804) 已经收敛到 +0.3pp。
      较大 K (16,20) 略微负向，因为更多 traces 降低 tie 频率且 constraint extraction 引入更多噪声。
    tables:
      - "T_appendix: K ablation table, 6 rows × (K, SICA%, SC%, Δpp, tie_rate, p)"
    figures_description:
      - "Appendix figure: K vs Δpp line plot with 95% bootstrap CI bands, all CIs cross zero"
    analysis: >
      K=11 gap=0 是 capability trap 的直接证据：奇数 K 无 tie，SICA 退化为 SC。
      论文中需写 "SICA's occasional marginal advantage at even K is entirely attributable
      to its superior tiebreak mechanism, not to constraint-based reasoning."

  - name: tiebreak_baseline_analysis
    plan_id: exp-003
    description: "SICA vs SC-random-tiebreak vs SC-deterministic on all data, CPU-only"
    expected_results:
      n_tied_problems: 41
      n_total: 804
      tie_rate: 0.051
      sica_tiebreak_accuracy: 0.78
      random_tiebreak_accuracy: 0.49
      alphabetical_tiebreak_accuracy: 0.56
      first_seen_tiebreak_accuracy: 0.44
      sica_overall_vs_random_overall_gap_pp: 0.25
      sica_overall_vs_random_overall_p: 0.72
    result_rationale: >
      Median 档下 tie 仅占 ~5% 问题。SICA 在 tied 子集上显著优于 random（~78% vs 49%），
      但 tied 子集太小（~41/804），所以 overall accuracy 差异仅 ~0.25pp，不显著。
      这支持 "SICA is a better tiebreaker but ties are too rare to matter" 叙事。
      alphabetical 略高于 random 因为 NLI label 排序碰巧与某些 ground truth 相关（FOLIO 的 True/False/Unknown）。
    tables:
      - "T_appendix: Tiebreak comparison table on tied subset (n=41)"
    figures_description: []
    analysis: >
      论文中可用一段 prose 报告：on the 5.1% of problems with ties, SICA resolves 78% correctly
      vs 49% for random, but this advantage is insufficient to produce significant
      aggregate gains given the low tie rate.

  - name: sica_7b_scaling
    plan_id: exp-004
    description: "Qwen2.5-7B-Instruct on D012 60 questions, within-Qwen scaling"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.600
      sc_accuracy: 0.617
      delta_pp: -1.67
      multi_candidate_rate: 0.617
      extraction_rate: 0.82
      answer_extraction_rate: 0.91
      contradiction_rate: 0.065
      mcnemar_p: 0.73
      constraint_precision_mean: 0.51
      c0_pct: 61.7
    result_rationale: >
      Median 档下 7B 比 14B 更弱：baseline accuracy 降至 ~60%，C0 升至 ~62%（更多 disagreement 因为
      模型更不确定）。高 C0 + 低 constraint quality（precision ~0.51, 接近 random）= capability trap
      经典表现。Delta 略负但在噪声范围内。这强化 "高 diversity 不等于 gain" 的 claim，
      但 n=60 只能作为 suggestive evidence。
    tables:
      - "T1 main results 增加一行 Qwen2.5-7B"
    figures_description:
      - "F4 C0-vs-gap scatter 增加一个 marker (C0≈62%, Δ≈-1.7pp)"
    analysis: >
      与 14B (C0=38%, Δ=+0.3pp) 形成对比：C0 更高但 gap 仍≈0 甚至略负。
      支持 capability trap 但 n=60 只能写 "consistent with"。如 reviewer 追问 within-family scaling，
      可加 72B 数据点形成 3-point trend。

  - name: qwq_32b_operating_regime
    plan_id: exp-005
    description: "QwQ-32B existing data formatted for Operating Regime Analysis"
    expected_results:
      qwq_aggregate_c0_effective_pct: 2.8
      qwq_sica_eq_sc: true
      aime_c0_pct: 0.0
      aime_delta_pp: 0.0
      proofwriter_c0_pct: 5.3
      proofwriter_delta_pp: -3.3
      folio_c0_pct: 0.0
      folio_delta_pp: 0.0
      total_n: 46
      qwq_categorization: "full reasoning model, C0<5%"
    result_rationale: >
      QwQ-32B 作为 full reasoning model 产生高度一致的 reasoning chains，C0 有效值 <3%。
      这使 SICA 结构性退化为 SC（只有一个 candidate answer 时 MAX-SAT 无法选择不同答案）。
      Median 档下 PW 出现微弱负信号（-3.3pp）但 n=17 完全在噪声内。
      数据支持 C0 threshold diagnostic：C0<5% → SICA 注定无效。
    tables:
      - "T1 main results QwQ-32B 行 (C0<5%, Δ=0.0pp)"
      - "F3 operating regime heatmap: QwQ 占据左下角 (low C0, Δ≈0)"
    figures_description:
      - "F3 heatmap: QwQ-32B data points clustered at C0≈0-5%, Δ≈0"
    analysis: >
      QwQ-32B 证明 full reasoning model 不需要 SICA（已经 internally consistent）。
      与 DeepSeek-R1-Distill-7B (C0=58%) 形成鲜明对比——蒸馏版不保留 deterministic reasoning。
      论文中定位为 "reasoning models make SICA redundant; distilled models make it ineffective."

  - name: c0_diagnostic_validation
    plan_id: exp-006
    description: "C0 vs SICA-SC gap across all models/K values, CPU analysis"
    expected_results:
      n_conditions: 12
      c0_range: [0.0, 62.0]
      gap_range: [-3.3, 3.3]
      pearson_r: 0.08
      pearson_p: 0.80
      c0_threshold_5_sensitivity: 1.0
      c0_threshold_5_specificity: 0.0
      c0_below_5_all_zero_gap: true
      c0_above_20_mean_gap_pp: 0.15
      c0_above_20_gap_sd: 2.8
    result_rationale: >
      Median 档下 C0 作为 binary diagnostic 有效（C0<5% → gap≡0，sensitivity=1.0），
      但作为 continuous predictor 无用（r≈0.08，无相关性）。C0>20% 的条件 gap 均值接近 0 且方差大，
      说明 diversity 是 necessary but not sufficient。这正是 median 档的核心发现：
      C0 可以判断 "不可能有效" 但不能预测 "会有效"。
    tables:
      - "T_appendix: all conditions × (model, domain, K, n, C0, Δpp, p)"
    figures_description:
      - "F4: experiment-level C0 vs Δpp scatter, marker size ∝ sqrt(n), horizontal band at Δ=0, vertical line at C0=5%"
    analysis: >
      Claim 3 措辞调整为 "C0 is a necessary-but-insufficient condition and a zero-cost
      early stopping criterion: C0<5% guarantees SICA=SC, but C0>20% does not predict gains."
      r≈0.08 表明 diversity 和 effectiveness 之间没有梯度关系，只有 threshold 关系。

  - name: sica_72b_awq
    plan_id: exp-007
    description: "Qwen2.5-72B-Instruct AWQ on D012 60 questions"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.817
      sc_accuracy: 0.833
      delta_pp: -1.67
      multi_candidate_rate: 0.217
      extraction_rate: 0.93
      answer_extraction_rate: 1.0
      contradiction_rate: 0.018
      mcnemar_p: 0.65
      c0_pct: 21.7
    result_rationale: >
      72B 模型 baseline 更高 (~83%)，C0 降至 ~22%（模型更自信，disagreement 更少）。
      C0 刚好在 20% threshold 边缘，SICA 有极少 multi-candidate 问题可操作，但 constraint quality 
      仍不足以产生 positive gap。Delta 略负（-1.67pp）但在 n=60 噪声内。
      Within-Qwen scaling trend: 7B (C0=62%, Δ≈-1.7) → 14B (C0=38%, Δ=+0.3) → 72B (C0=22%, Δ≈-1.7)。
      无单调关系，confirming capability trap 不是简单的 scale 问题。
    tables:
      - "T1 main results 增加 Qwen2.5-72B 行"
    figures_description:
      - "F4 增加 72B marker (C0≈22%, Δ≈-1.7pp, large marker due to Qwen family)"
    analysis: >
      72B 是 within-family scaling 的关键数据点。C0 随 scale 下降（62%→38%→22%），
      但 gap 不随 C0 单调变化。如 reviewer 追问 "would 72B+ work?"，可指出 C0→0 趋势
      意味着更大模型会像 QwQ-32B 一样使 SICA 退化，而非改善。

  - name: constraint_quality_case_studies
    plan_id: exp-008
    description: "5-10 representative questions qualitative analysis"
    expected_results:
      n_cases: 8
      syntactically_valid_rate: 0.89
      semantically_meaningful_rate: 0.62
      discriminative_constraints_rate: 0.15
      common_failure_modes:
        tautological: 0.35
        overly_general: 0.28
        contradicts_reasoning: 0.12
        correct_but_non_discriminative: 0.25
    result_rationale: >
      Median 档下 constraints 大多语法正确但语义浅薄。~35% 是 tautological（如 "the answer must be
      consistent with the premises"），~28% overly general（如 "if A then B" 但 A,B 都被所有 trace 满足），
      ~25% correct but non-discriminative（约束正确但所有 candidate answers 都满足）。
      仅 ~15% 的 constraints 真正具有 discriminative power，且这些往往也是错误率最高的。
      这为 F2 scatter 中 constraint precision ≈ 0.50-0.55 提供了定性解释。
    tables: []
    figures_description:
      - "Table in appendix: 4 representative cases with extracted constraints, ground truth, and failure mode annotation"
    analysis: >
      Case studies 提供 capability trap 的 qualitative evidence。论文中选 2 个 hero cases：
      (1) high-diversity problem where all constraints are tautological → MAX-SAT = counting;
      (2) one genuinely discriminative constraint exists but is outweighed by 20+ non-discriminative ones.

  - name: overhead_analysis
    plan_id: exp-009
    description: "Wall-time breakdown per question from exp-001 data"
    expected_results:
      n: 804
      mean_total_wall_s: 62.0
      mean_trace_gen_s: 32.0
      trace_gen_pct: 51.6
      mean_extract_s: 28.5
      extract_pct: 46.0
      mean_dedup_s: 1.2
      dedup_pct: 1.9
      mean_maxsat_s: 0.003
      maxsat_pct: 0.005
      sica_overhead_vs_sc_pct: 48.0
      sica_overhead_s: 29.7
      p90_total_s: 105.0
      p90_overhead_pct: 56.0
    result_rationale: >
      Median 档下 SICA 额外开销约 48%（constraint extraction ~29s per problem）。
      MAX-SAT solving 本身极快（<3ms），开销完全来自 LLM-based extraction pass。
      这意味着 SICA 近似 double 了 SC 的 inference cost，且 gain ≈ 0pp。
      对 reviewer "is the overhead worth it" 的回答明确是 no。
    tables:
      - "T_appendix: overhead breakdown (gen/extract/dedup/maxsat) with percentiles"
    figures_description:
      - "Appendix bar chart: stacked time breakdown per phase"
    analysis: >
      论文中报告 "SICA incurs ~48% overhead over SC, with constraint extraction accounting
      for 96% of the additional cost. Given zero significant accuracy gain, the overhead
      is not justified. However, if extraction quality improves (cf. oracle result),
      the solving overhead (0.005%) would remain negligible." 这连接到 oracle 作为 constructive direction。

  - name: sica_llama_8b
    plan_id: exp-011
    description: "LLaMA-3.1-8B-Instruct on D012 60 questions"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.650
      sc_accuracy: 0.600
      delta_pp: 5.0
      multi_candidate_rate: 0.60
      extraction_rate: 0.86
      answer_extraction_rate: 0.90
      contradiction_rate: 0.05
      mcnemar_p: 0.25
      discordant_sica_wins: 4
      discordant_sc_wins: 1
      truncated_traces: 40
      proofwriter_delta_pp: 3.3
      folio_delta_pp: 6.7
    result_rationale: >
      Median 档核心假设之一：LLaMA-8B D012 出现 +5pp (n=60) 的 underpowered positive signal。
      p≈0.25 不显著，SE≈6pp 意味着 CI 包含 0。这是最棘手的条件——reviewer 会问 "is this a real signal
      or noise?" 需要在论文中显式讨论为 underpowered observation，并指出 exp-019/020 (n=200+) 
      在相同模型不同域上确认 null。高 truncation rate (40/720 traces) 引入 extraction noise，
      可能是 false positive 的来源。
    tables:
      - "T1 main results LLaMA-8B D012 行 (标注 n=60, suggestive)"
    figures_description:
      - "F4 marker with wide CI error bar"
    analysis: >
      论文措辞："+5.0pp on D012 (n=60, p=0.25) is consistent with sampling noise given
      the 6pp standard error. LLaMA-8B on StrategyQA (n=200, Δ=+2.0pp, p=0.42) and
      FOLIO (n=204, Δ=-2.4pp, p=0.27) with adequate power confirm the null."
      如 reviewer 坚持要 powered replication，备选是扩展 D012 到 200 题（~3h GPU）。

  - name: gsm8k_pilot_14b
    plan_id: exp-012
    description: "Qwen2.5-14B on GSM8K 30-question pilot"
    expected_results:
      n: 30
      k: 12
      sica_accuracy: 0.867
      sc_accuracy: 0.867
      delta_pp: 0.0
      multi_candidate_rate: 0.267
      c0_pct: 26.7
      extraction_rate: 0.78
      answer_extraction_rate: 0.95
      contradiction_rate: 0.03
      discordant_total: 0
      constraint_precision: 0.52
    result_rationale: >
      Median 档下 GSM8K C0 落在 20-35% 范围（这里 26.7%），高于 reviewer 预期的 <20%。
      14B 在 GSM8K 上 baseline 高 (~87%)，大多数问题 unanimous。C0=26.7% 意味着 ~8/30 问题有
      multi-candidate，但这些问题的 constraint precision ≈ 0.52（数学 constraints 看似精确但
      对 open-answer 域 discriminative power 仍低）。Delta = 0pp 因为 constraints 无法区分
      正确与错误的数值答案。这支持 "C0>20% 但 gain=0" 的 capability trap narrative。
    tables:
      - "T_appendix: GSM8K pilot results"
    figures_description:
      - "F4 增加 GSM8K marker (C0≈27%, Δ=0pp)"
    analysis: >
      GSM8K 结果的论文价值：(1) 数学域 C0 高于预期，排除 "C0 high only in restricted-answer domains" 假设；
      (2) 即使 open-answer + 高 C0，gap 仍= 0，strengthening capability trap。
      但 n=30 只能写 "pilot study suggests"。Reviewer 可能要求扩展。

  - name: constraint_ablation
    plan_id: exp-013
    description: "MaxSAT vs count-only vs random-weight CPU ablation on exp-001"
    expected_results:
      maxsat_accuracy: 0.765
      count_only_accuracy: 0.766
      random_weight_accuracy: 0.763
      sc_baseline_accuracy: 0.762
      n_problems: 804
      maxsat_vs_count_mcnemar_p: 0.82
      maxsat_vs_random_mcnemar_p: 0.71
      agreement_maxsat_count: 802
      agreement_maxsat_random: 800
      proxy_based: true
    result_rationale: >
      Median 档下 MaxSAT≈count-only≈random-weight，三者 agreement >99.5%。
      这是 capability trap 的 mechanism evidence：MAX-SAT 解算器无贡献，因为 constraints 
      无 discriminative power 时 satisfiability 退化为 counting。
      关键 caveat：ablation 基于 proxy 重构（非原始 z3 公式），reviewer 会要求 acknowledge 
      或做 robustness check。Median 档下这个 limitation 可以通过 "results are consistent
      across all three ablation variants" 来 partially defend。
    tables:
      - "T3: Constraint Ablation table (MaxSAT, count-only, random-weight, SC)"
    figures_description: []
    analysis: >
      T3 是 paper 的核心 mechanism table。措辞："MAX-SAT optimization provides no advantage
      over simple constraint counting (agreement on 802/804 problems), confirming that
      satisfiability structure is not leveraged — the solver degenerates to a vote counter."
      必须加 footnote acknowledging proxy-based reconstruction limitation。

  - name: sica_deepseek_r1_llama_8b
    plan_id: exp-014
    description: "DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.683
      sc_accuracy: 0.717
      delta_pp: -3.33
      multi_candidate_rate: 0.583
      extraction_rate: 0.84
      answer_extraction_rate: 0.94
      truncated_traces: 70
      contradiction_rate: 0.038
      mcnemar_p: 0.48
      discordant_sica_wins: 0
      discordant_sc_wins: 2
      c0_pct: 58.3
      model: "DeepSeek-R1-Distill-Qwen-7B"
      reclassified_as: "instruction-scale"
    result_rationale: >
      Median 档核心假设：DeepSeek-R1-Distill-7B 表现为 instruction-scale model（C0=58%），
      而非 full reasoning model（预期 C0<5%）。7B 容量不足以维持 deterministic reasoning chains。
      Delta = -3.3pp（SICA 反而更差），因为 high C0 + low quality constraints + 高 truncation 
      导致 MAX-SAT exclusion 有时排除了正确答案的 traces。这是 capability trap 的极端表现：
      diversity 最高的条件反而最差。论文中重新分类为 instruction-scale 而非 reasoning model。
    tables:
      - "T1 main results DeepSeek-R1-Distill-7B 行"
    figures_description:
      - "F4: DeepSeek marker at (C0≈58%, Δ≈-3.3pp) — 最右上象限"
    analysis: >
      论文叙事调整："distilled reasoning models at 7B scale behave identically to instruction
      models (C0=58% vs <5% for full QwQ-32B), suggesting that deterministic reasoning
      requires sufficient model capacity." 这消除了 "second reasoning model" 数据点，
      但增加了 instruction-scale 模型覆盖（现在 5 个 instruction-scale models）。

  - name: logic_lm_baseline
    plan_id: exp-015
    description: "Logic-LM × K + majority vote on FOLIO, CPU-only"
    expected_results:
      n: 204
      k: 12
      logic_lm_k_accuracy: 0.779
      sc_accuracy: 0.794
      sica_accuracy: 0.794
      logic_lm_vs_sc_delta_pp: -1.47
      logic_lm_fol_parse_success: 0.73
      logic_lm_single_trace_accuracy: 0.72
    result_rationale: >
      Median 档下 Logic-LM × K ≈ SC 或略低。Logic-LM 对每条 trace 独立做 FOL verification，
      then majority vote。单 trace verification accuracy ~72%（受 FOL translation error 影响），
      K=12 后 majority vote 提升到 ~78%，但仍不及 SC 的 79.4%。
      原因：Logic-LM 的 single-trace FOL verification 会误判一些正确 traces 为 invalid，
      减少了 effective vote pool。SICA 避免了这个问题因为它做 cross-trace aggregation。
      但两者都不优于 SC，说明 FOL extraction quality 是共同瓶颈。
    tables:
      - "T_appendix: Logic-LM × K vs SC vs SICA comparison"
    figures_description: []
    analysis: >
      论文中用 1-2 段报告：Logic-LM × K approach provides an alternative to MAX-SAT
      aggregation but suffers from the same extraction quality bottleneck. Its slightly
      lower accuracy reflects the additional failure mode of single-trace verification
      rejecting correct reasoning traces with imperfect FOL translations.

  - name: weighted_sc_baseline
    plan_id: exp-016
    description: "Weighted SC variants on exp-001 data, CPU-only"
    expected_results:
      n: 804
      sc_uniform: 0.762
      inv_length_weighted: 0.767
      length_weighted: 0.753
      constraint_count_weighted: 0.753
      inv_length_vs_sc_p: 0.45
      length_vs_sc_p: 0.15
      constraint_count_vs_sc_p: 0.22
      all_nonsignificant: true
      best_weighting: "inverse-length"
      best_weighting_gap_pp: 0.5
    result_rationale: >
      Median 档下所有 weighting schemes ≈ SC，none significant。Inverse-length 略优 (+0.5pp)
      因为较短 traces 倾向于更自信的模型输出，但效果微弱。Length-weighted 和 constraint-count weighted 
      略差，因为较长 traces / 更多 constraints 不意味着更准确。
      这 eliminates "weighted SC is a simpler alternative" concern：如果 weighted SC 也无效，
      问题不在 aggregation method 而在 signal quality。
    tables:
      - "T_appendix: Weighted SC variants comparison"
    figures_description: []
    analysis: >
      论文中报告："Neither MAX-SAT (SICA) nor simpler weighted voting schemes improve
      over uniform majority voting, confirming that the bottleneck lies in signal
      quality rather than aggregation methodology." 直接回应 Taubenfeld et al. 2024。

  - name: sica_strategyqa_14b
    plan_id: exp-017
    description: "Qwen2.5-14B on StrategyQA 60 questions"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.567
      sc_accuracy: 0.550
      delta_pp: 1.67
      multi_candidate_rate: 0.10
      c0_pct: 10.0
      extraction_rate_trace: 0.71
      extraction_rate_problem: 1.0
      mcnemar_p: 0.75
      bootstrap_p_delta_le_0: 0.18
      discordant_sica_wins: 2
      discordant_sc_wins: 1
    result_rationale: >
      Median 档下 StrategyQA C0 意外地低 (~10%)，因为 binary (Yes/No) 答案空间 + 14B 足够强
      使大多数问题 unanimous。高 C0 预测（35-50%）未实现是 median 档的特征之一——
      模型在 commonsense 上比预期更一致。低 C0 意味着 SICA 几乎无操作空间。
      +1.67pp 来自极少数 discordant problems，不显著。
      但 trace extraction rate 较低 (71%)，因为 commonsense reasoning chains 不易转化为 FOL。
    tables:
      - "T1 main results StrategyQA 行 (标注 low C0)"
    figures_description:
      - "F3 heatmap: StrategyQA cell at low C0, Δ≈0"
    analysis: >
      StrategyQA 低 C0 意味着它不是 capability trap 的好测试域（C0 太低，SICA 退化为 SC）。
      论文中需 acknowledge："SICA operates meaningfully (C0>20%) primarily on formal logic
      domains; binary-answer commonsense reasoning produces insufficient diversity
      for the method to diverge from SC."

  - name: sica_arc_challenge_14b
    plan_id: exp-018
    description: "Qwen2.5-14B on ARC-Challenge 60 questions"
    expected_results:
      n: 60
      k: 12
      sica_accuracy: 0.950
      sc_accuracy: 0.967
      delta_pp: -1.67
      multi_candidate_rate: 0.05
      c0_pct: 5.0
      extraction_rate: 1.0
      contradiction_detected: 3
      discordant_sica_wins: 0
      discordant_sc_wins: 1
    result_rationale: >
      Median 档下 ARC-Challenge C0 极低 (~5%)，因为 14B 在 ARC-Challenge 上 baseline ~97%
      （4-choice 格式 + science knowledge 是 14B 的强项）。几乎所有问题 unanimous。
      仅 3/60 问题有 multi-candidate，其中 1 个 SICA 选错（constraint 误导）。
      Delta = -1.67pp 但完全在噪声内。ARC 加入论文主要为 domain diversity，非 capability trap evidence。
    tables:
      - "T1 main results ARC-Challenge 行"
    figures_description:
      - "F3 heatmap: ARC cell at C0≈5%, Δ≈0"
    analysis: >
      ARC-Challenge 和 StrategyQA 一样 C0 太低。论文中作为 "domain coverage" 贡献，
      但需 acknowledge 这些域的 null result 是因为 method degenerates 而非 capability trap。
      真正测试 capability trap 的域只有 FOLIO 和 ProofWriter（C0>30%）。

  - name: constraint_quality_correlation
    plan_id: exp-019
    description: "Constraint precision per domain × model, correlation with C0 and gap"
    expected_results:
      n_conditions_analyzed: 8
      constraint_precision_overall_mean: 0.527
      constraint_precision_folio_qwen14b: 0.54
      constraint_precision_pw_qwen14b: 0.52
      constraint_precision_folio_llama8b: 0.51
      constraint_precision_strategyqa_qwen14b: 0.53
      constraint_precision_folio_mistral7b: 0.50
      precision_vs_c0_r: 0.12
      precision_vs_c0_p: 0.78
      precision_vs_gap_r: 0.35
      precision_vs_gap_p: 0.39
      f2_non_discriminative_fraction: 0.78
      per_problem_precision_sd: 0.18
      subgroup_high_precision_fraction: 0.15
      subgroup_high_precision_mean: 0.57
    result_rationale: >
      Median 档下 constraint precision 全局均值 ~0.527（略高于 0.50 random baseline 但不足以
      产生 aggregate gains）。跨域 × 模型 variation 很小（0.50-0.54），说明 precision 不依赖于
      特定域或模型——是 self-extraction 的系统性限制。
      Per-problem scatter 有异质性：~78% 问题的 precision 在 0.45-0.55（non-discriminative），
      ~15% 在 0.55-0.58（部分 discriminative 但不够翻转 aggregation）。
      这些 partially discriminative 问题集中在 FOLIO 的特定 sub-patterns 上。
      precision vs C0 无相关 (r=0.12)，precision vs gap 弱正相关 (r=0.35) 但不显著，
      意味着 "constraints 质量是独立瓶颈，不随 diversity 或 domain 变化"。
    tables:
      - "T_appendix: constraint precision by domain × model matrix"
    figures_description:
      - "F2 (hero figure): per-problem scatter of vote entropy vs constraint exclusion rate, colored by flip outcome (n=307 multi-candidate problems). 78% of problems cluster near precision≈0.50 line. Heterogeneous tail visible but insufficient to shift aggregate."
    analysis: >
      F2 是 paper 最重要的 figure，但 median 档下需要引导解读。论文中加 annotation arrows
      标注 (1) "non-discriminative cluster" (78% of problems), (2) "partially discriminative tail"
      (15%), (3) "rare discriminative outliers" (7%). 
      Key sentence: "While 15% of problems show constraint precision 0.55-0.58, this partial
      discrimination is insufficient to overcome the 78% majority of non-discriminative problems
      in aggregate. The oracle experiment confirms that with truly discriminative constraints
      (gold FOL, precision≈0.95), the same aggregation mechanism achieves +8.82pp."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4db2519-331f-465e-afcd-a4e90a2c0a3b",
  "isSidechain": false,
  "requestId": "req_011Cb8VavvQaKb4qbAVtn3Qu",
  "type": "assistant",
  "uuid": "d744ef91-d319-45d7-b500-83d931b72816",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e39c49cf-e3c1-4b30-97fe-e5ae0623d229",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LaAqqcYMjnMD3wUkWMYSvQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20366,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11650,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20366,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11650,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20366,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20366
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 null 成立但边缘条件有噪声；F2 图可解读但需引导；部分 claim 措辞需软化 核心假设：['exp-012 GSM8K: C0 在 20-35%（高于预期），SICA≈SC 但 CI 宽，无法排除小正效应', 'F2 per-problem scatter 有异质性：部分子域 constra…",
  "leafUuid": "d744ef91-d319-45d7-b500-83d931b72816",
  "sessionId": "e39c49cf-e3c1-4b30-97fe-e5ae0623d229"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing LLM self-extracted constraint aggregation failure",
  "sessionId": "e39c49cf-e3c1-4b30-97fe-e5ae0623d229"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心 null 成立但边缘条件有噪声；F2 图可解读但需引导；部分 claim 措辞需软化 核心假设：['exp-012 GSM8K: C0 在 20-35%（高于预期），SICA≈SC 但 CI 宽，无法排除小正效应', 'F2 per-problem scatter 有异质性：部分子域 constra…",
  "leafUuid": "d744ef91-d319-45d7-b500-83d931b72816",
  "sessionId": "e39c49cf-e3c1-4b30-97fe-e5ae0623d229"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing LLM self-extracted constraint aggregation failure",
  "sessionId": "e39c49cf-e3c1-4b30-97fe-e5ae0623d229"
}
```

---
