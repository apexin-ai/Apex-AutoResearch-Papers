# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：exp-001 confirms gains with statistical significance; cross-family and ablat

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/e1f050df-93c8-4723-a6a9-64d60ce0f070.jsonl`
- **Structured JSON:** [`91c38fcab0e218652168.json`](../../sessions/91/91c38fcab0e218652168.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T15:58:59.296Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T15:58:59.296Z",
  "sessionId": "e1f050df-93c8-4723-a6a9-64d60ce0f070",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：exp-001 confirms gains with statistical significance; cross-family and ablation all validate\n核心假设：['FOLIO gain sustains at +4pp or above on 204 questions', 'ProofWriter shows modest positive gap (+1-3pp) on 600 questions', 'Combined gap statistically significant (p<0.05 bootstrap)', 'Cross-family (Mistral/LLaMA) both show C0>25% and positive SICA-SC gap', 'Constraint ablation shows MaxSAT > count-only by ≥2pp', 'C0 shows gradient across model scales (7B>14B>72B)']\n关键指标范围：{'combined_gap_pp': [2.5, 5.0], 'folio_gap_pp': [4.0, 8.0], 'proofwriter_gap_pp': [1.0, 3.0], 'bootstrap_p_combined': [0.01, 0.05], 'c0_14b_expanded': [0.35, 0.55], 'c0_mistral_7b': [0.3, 0.6], 'c0_llama_8b': [0.3, 0.6], 'cross_family_gap_pp': [1.5, 5.0], 'maxsat_vs_count_only_pp': [2.0, 5.0], 'tiebreak_win_rate': [0.7, 0.85]}\n叙事方向：Original framing holds — SICA is a principled, effective method with formally characterizable operating regime. All 3 claims stand at full strength. Hero figure (C0 vs gap scatter) shows clean threshold with gradient. Paper tells a complete story: method + when it works + why + how to know in advance.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Fallback: AAAI 2027 (Aug 1)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条)\n1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).\n2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is governed by trace diversity (C0), which reflects effective output diversity — SICA adds value when C0>20% (diverse outputs, disagreement to resolve) but degenerates to SC when C0<5% (converged outputs, no disagreement). C0 empirically correlates with task-relative model confidence: instruction models show high C0 on challenging tasks, reasoning models show low C0 universally. Validated across 3 model families (Qwen, Mistral, LLaMA) and 2 reasoning architectures (QwQ, DeepSeek-R1). [Note: \"C0 → epistemic uncertainty\" connection reserved for Discussion, not formal claim — reviewer risk of terminology abuse per UQ community standards.]\n3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.\n\n## Core Insight\nSymbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that trace diversity (C0) — reflecting task-relative model confidence rather than model family or task domain alone — determines the operating regime. This transforms SICA from \"yet another ensemble method\" into \"a method with formally characterizable applicability boundaries,\" validated across 3 model families and multiple reasoning domains.\n\n## Story Spine\n- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.\n- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.\n- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75%+ win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) — a zero-cost diagnostic reflecting effective output diversity — and validate across 3 model families (Qwen, Mistral, LLaMA), 2 reasoning architectures (QwQ, DeepSeek-R1), and multiple domains (logic, math).\n- **Headline result template**: \"On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → exp-001: Expand to 804 questions for statistical power\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K sensitivity; exp-009: overhead analysis (P1); exp-013: constraint ablation (MaxSAT vs count-only vs random-weight)\n3. **\"Only Qwen models — family-specific artifact?\"** → exp-010: Mistral-7B + exp-011: LLaMA-8B (3-family validation)\n4. **\"Only one reasoning model\"** → exp-014: DeepSeek-R1-Distill-7B (second reasoning architecture)\n5. **\"Only logic domain — restricted answer space\"** → exp-012: GSM8K pilot with 14B (cross-domain C0 test)\n6. **\"ProofWriter shows 0pp gain\"** → Domain analysis in exp-001 expanded results\n7. **\"Random tiebreak baseline closes the gap\"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison (done on D012, will re-run on expanded)\n8. **\"Why not just use a reasoning model?\"** → exp-005: QwQ-32B + exp-014: DeepSeek-R1 show reasoning models are self-consistent → SICA redundant; instruction models (cheaper, more deployed) benefit\n9. **\"MAX-SAT is over-engineering\"** → exp-013: Constraint ablation proves satisfiability checking adds value over simple counting\n10. **\"Within-family scaling?\"** → exp-004: 7B + exp-007: 72B-AWQ show C0 trend within Qwen family\n\n## Working Title\n**\"When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation\"**\n(Alternatives: \"Beyond Majority Voting: Using Trace Diversity to Predict When Symbolic Consensus Improves LLM Reasoning\")\n\n## Paper Structure (EMNLP 8pp + appendix)\n- Main Tables: T1 (Main Results 7 models × datasets), T2 (Tiebreak Comparison), T3 (K Sensitivity), T4 (Overhead)\n- Main Figures: F1 (Pipeline), F2 (C0 vs Gap Scatter — hero figure), F3 (Operating Regime Heatmap), F4 (K Curve)\n- Appendix: Constraint Ablation (exp-013), Case Studies (exp-008), GSM8K (exp-012), Per-Problem Detail\n\n## Claim Risk Notes\n- **Claim 1 make-or-break**: exp-013 constraint ablation. If MaxSAT ≈ count-only → reframe as \"principled weighting\" not \"satisfiability-based reasoning\"\n- **Claim 3 downgrade risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to \"binary indicator\" not \"continuous predictor\". Gradient depends on 7B C0 >> 14B C0 >> 72B C0.\n- **\"Epistemic uncertainty\" terminology**: Reserve for Discussion section only. Main text uses \"effective output diversity\" / \"task-relative model confidence\". UQ community would attack formal misuse.\n\n## Contingency Plan (D023)\n**Trigger**: exp-001 完整结果 SICA ≤ SC（gap ≤ 0pp 或不显著）\n**Strategy**: Option A (Analysis Paper) + Option C (FOLIO sub-claim if positive)\n- 论文主线从\"SICA improves accuracy\"转为\"characterizing operating conditions of symbolic consensus\"\n- C0 threshold pattern 成为核心贡献（\"at what C0 level does SICA begin to match/exceed SC?\")\n- FOLIO 正向结果嵌入为\"domain formality → effectiveness\"子 claim\n- Claim 1 弱化为\"principled + interpretable tiebreaking\"（不 claim accuracy gain）\n- 需补：constraint extraction quality vs delta 相关性分析（CPU-only）\n- Venue: EMNLP Main (30-35%) / Findings (60-70%) / AAAI 2027 fallback\n**Decision point**: exp-001 FOLIO 70题的 C0 和 delta\n\n## Venue Fit Risks\n- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the \"operating regime characterization\" — the tiebreaking mechanism is evidence, not the claim.\n- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.\n- Negative results: QwQ-32B data must be presented as insight (\"When Does Symbolic Consensus Degenerate?\"), not failure.\n- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.\n- **[D023 新增]** If SICA ≤ SC globally: pivot to analysis paper. Must answer \"so what should practitioners do?\" → C0 as deployment diagnostic.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: RUNNING\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,12,16,20) on D012''s 60 questions. Key questions:\n    does SICA benefit depend on tiebreaks? What happens at odd K (no even splits)?\n    How does tiebreak frequency change with K?'\n  priority: P0\n  gpu_budget_hours: 5\n  deps: []\n  status: planned\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Within-Qwen scaling dimension.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX\n    PRO 6000 单卡可放。\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。\n- id: exp-010\n  name: sica_mistral_7b\n  claim:\n  - 2\n  - 3\n  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family\n    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''\n    attack.'\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+\n    题（~3h GPU，margin 允许）。'\n- id: exp-011\n  name: sica_llama_8b\n  claim:\n  - 2\n  - 3\n  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.\n    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation\n    同 exp-010。\n- id: exp-012\n  name: gsm8k_pilot_14b\n  claim:\n  - 2\n  - 3\n  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:\n    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer\n    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain\n    win.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable\n    insight.\n- id: exp-013\n  name: constraint_ablation\n  claim:\n  - 1\n  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count\n    per answer, no satisfiability) vs SICA-random-weight. Tests whether MAX-SAT is\n    essential or over-engineering.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 新增. 防御 'over-engineering' reviewer attack. CPU-only, 零 GPU 成本。\n- id: exp-014\n  name: sica_deepseek_r1_llama_8b\n  claim:\n  - 2\n  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning\n    model data point with LLaMA base architecture: validates C0<5% generalizes beyond\n    QwQ-32B AND eliminates ''still Qwen family'' attack.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T15:58:59.300Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T15:58:59.300Z",
  "sessionId": "e1f050df-93c8-4723-a6a9-64d60ce0f070"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T15:58:59.323Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：exp-001 confirms gains with statistical significance; cross-family and ablation all validate
核心假设：['FOLIO gain sustains at +4pp or above on 204 questions', 'ProofWriter shows modest positive gap (+1-3pp) on 600 questions', 'Combined gap statistically significant (p<0.05 bootstrap)', 'Cross-family (Mistral/LLaMA) both show C0>25% and positive SICA-SC gap', 'Constraint ablation shows MaxSAT > count-only by ≥2pp', 'C0 shows gradient across model scales (7B>14B>72B)']
关键指标范围：{'combined_gap_pp': [2.5, 5.0], 'folio_gap_pp': [4.0, 8.0], 'proofwriter_gap_pp': [1.0, 3.0], 'bootstrap_p_combined': [0.01, 0.05], 'c0_14b_expanded': [0.35, 0.55], 'c0_mistral_7b': [0.3, 0.6], 'c0_llama_8b': [0.3, 0.6], 'cross_family_gap_pp': [1.5, 5.0], 'maxsat_vs_count_only_pp': [2.0, 5.0], 'tiebreak_win_rate': [0.7, 0.85]}
叙事方向：Original framing holds — SICA is a principled, effective method with formally characterizable operating regime. All 3 claims stand at full strength. Hero figure (C0 vs gap scatter) shows clean threshold with gradient. Paper tells a complete story: method + when it works + why + how to know in advance.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: symb_invariant_consensus

## paper_framing.md

# Paper Framing — symb_invariant_consensus

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25)
- Fallback: AAAI 2027 (Aug 1)
- Deadline: May 25, 2026 (ARR submission)

## Core Claims (3 条)
1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).
2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is governed by trace diversity (C0), which reflects effective output diversity — SICA adds value when C0>20% (diverse outputs, disagreement to resolve) but degenerates to SC when C0<5% (converged outputs, no disagreement). C0 empirically correlates with task-relative model confidence: instruction models show high C0 on challenging tasks, reasoning models show low C0 universally. Validated across 3 model families (Qwen, Mistral, LLaMA) and 2 reasoning architectures (QwQ, DeepSeek-R1). [Note: "C0 → epistemic uncertainty" connection reserved for Discussion, not formal claim — reviewer risk of terminology abuse per UQ community standards.]
3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.

## Core Insight
Symbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that trace diversity (C0) — reflecting task-relative model confidence rather than model family or task domain alone — determines the operating regime. This transforms SICA from "yet another ensemble method" into "a method with formally characterizable applicability boundaries," validated across 3 model families and multiple reasoning domains.

## Story Spine
- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.
- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.
- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75%+ win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) — a zero-cost diagnostic reflecting effective output diversity — and validate across 3 model families (Qwen, Mistral, LLaMA), 2 reasoning architectures (QwQ, DeepSeek-R1), and multiple domains (logic, math).
- **Headline result template**: "On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty."

## Anticipated Reviewer Concerns & Defensive Experiments
1. **"Gains not statistically significant"** → exp-001: Expand to 804 questions for statistical power
2. **"Only a better tiebreaker, not worth the overhead"** → exp-002: K sensitivity; exp-009: overhead analysis (P1); exp-013: constraint ablation (MaxSAT vs count-only vs random-weight)
3. **"Only Qwen models — family-specific artifact?"** → exp-010: Mistral-7B + exp-011: LLaMA-8B (3-family validation)
4. **"Only one reasoning model"** → exp-014: DeepSeek-R1-Distill-7B (second reasoning architecture)
5. **"Only logic domain — restricted answer space"** → exp-012: GSM8K pilot with 14B (cross-domain C0 test)
6. **"ProofWriter shows 0pp gain"** → Domain analysis in exp-001 expanded results
7. **"Random tiebreak baseline closes the gap"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison (done on D012, will re-run on expanded)
8. **"Why not just use a reasoning model?"** → exp-005: QwQ-32B + exp-014: DeepSeek-R1 show reasoning models are self-consistent → SICA redundant; instruction models (cheaper, more deployed) benefit
9. **"MAX-SAT is over-engineering"** → exp-013: Constraint ablation proves satisfiability checking adds value over simple counting
10. **"Within-family scaling?"** → exp-004: 7B + exp-007: 72B-AWQ show C0 trend within Qwen family

## Working Title
**"When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation"**
(Alternatives: "Beyond Majority Voting: Using Trace Diversity to Predict When Symbolic Consensus Improves LLM Reasoning")

## Paper Structure (EMNLP 8pp + appendix)
- Main Tables: T1 (Main Results 7 models × datasets), T2 (Tiebreak Comparison), T3 (K Sensitivity), T4 (Overhead)
- Main Figures: F1 (Pipeline), F2 (C0 vs Gap Scatter — hero figure), F3 (Operating Regime Heatmap), F4 (K Curve)
- Appendix: Constraint Ablation (exp-013), Case Studies (exp-008), GSM8K (exp-012), Per-Problem Detail

## Claim Risk Notes
- **Claim 1 make-or-break**: exp-013 constraint ablation. If MaxSAT ≈ count-only → reframe as "principled weighting" not "satisfiability-based reasoning"
- **Claim 3 downgrade risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to "binary indicator" not "continuous predictor". Gradient depends on 7B C0 >> 14B C0 >> 72B C0.
- **"Epistemic uncertainty" terminology**: Reserve for Discussion section only. Main text uses "effective output diversity" / "task-relative model confidence". UQ community would attack formal misuse.

## Contingency Plan (D023)
**Trigger**: exp-001 完整结果 SICA ≤ SC（gap ≤ 0pp 或不显著）
**Strategy**: Option A (Analysis Paper) + Option C (FOLIO sub-claim if positive)
- 论文主线从"SICA improves accuracy"转为"characterizing operating conditions of symbolic consensus"
- C0 threshold pattern 成为核心贡献（"at what C0 level does SICA begin to match/exceed SC?")
- FOLIO 正向结果嵌入为"domain formality → effectiveness"子 claim
- Claim 1 弱化为"principled + interpretable tiebreaking"（不 claim accuracy gain）
- 需补：constraint extraction quality vs delta 相关性分析（CPU-only）
- Venue: EMNLP Main (30-35%) / Findings (60-70%) / AAAI 2027 fallback
**Decision point**: exp-001 FOLIO 70题的 C0 和 delta

## Venue Fit Risks
- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the "operating regime characterization" — the tiebreaking mechanism is evidence, not the claim.
- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.
- Negative results: QwQ-32B data must be presented as insight ("When Does Symbolic Consensus Degenerate?"), not failure.
- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.
- **[D023 新增]** If SICA ≤ SC globally: pivot to analysis paper. Must answer "so what should practitioners do?" → C0 as deployment diagnostic.


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
  status: RUNNING
- id: exp-002
  name: sica_k_ablation_14b
  claim:
  - 1
  description: 'K sensitivity (K=6,8,12,16,20) on D012''s 60 questions. Key questions:
    does SICA benefit depend on tiebreaks? What happens at odd K (no even splits)?
    How does tiebreak frequency change with K?'
  priority: P0
  gpu_budget_hours: 5
  deps: []
  status: planned
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
  status: planned
  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+
    题（~3h GPU，margin 允许）。'
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
  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count
    per answer, no satisfiability) vs SICA-random-weight. Tests whether MAX-SAT is
    essential or over-engineering.'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned
  note: D021 新增. 防御 'over-engineering' reviewer attack. CPU-only, 零 GPU 成本。
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
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: sica_k_sensitivity_14b
  name: ''
  status: QUEUED
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
  "promptId": "a18790a0-c187-4510-8d2f-45b1defc496a",
  "type": "user",
  "uuid": "46f4a40d-e058-4223-b574-ecce2ea5d759",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e1f050df-93c8-4723-a6a9-64d60ce0f070",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T15:58:59.322Z_

```json
{
  "parentUuid": "46f4a40d-e058-4223-b574-ecce2ea5d759",
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
  "uuid": "7b535e74-c31e-4a24-974a-b6b67d807cc5",
  "timestamp": "2026-05-16T15:58:59.322Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e1f050df-93c8-4723-a6a9-64d60ce0f070",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T15:58:59.322Z_

```json
{
  "parentUuid": "7b535e74-c31e-4a24-974a-b6b67d807cc5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a18cb4f0-3e3f-4b90-ad35-3c097d1e99dc",
  "timestamp": "2026-05-16T15:58:59.322Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e1f050df-93c8-4723-a6a9-64d60ce0f070",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：exp-001 confirms gains with statistical significance; cross-family and ablation all validate 核心假设：['FOLIO gain sustains at +4pp or above on 204 questions',…",
  "leafUuid": "a18cb4f0-3e3f-4b90-ad35-3c097d1e99dc",
  "sessionId": "e1f050df-93c8-4723-a6a9-64d60ce0f070"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 best-tier experiment predictions with rationales",
  "sessionId": "e1f050df-93c8-4723-a6a9-64d60ce0f070"
}
```

---

### Assistant

_source line 8 · 2026-05-16T15:59:18.452Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each "planned" experiment in the experiment_plan, assuming the "best" tier outcome. I need to provide result_rationale for each prediction explaining why these results would occur under the best-case scenario.

Let me go through each planned experiment:

1. exp-001 (sica_expanded_14b) - RUNNING, so I should include it
2. exp-002 (sica_k_ablation_14b) - planned
3. exp-003 (tiebreak_baseline_analysis) - planned


4. exp-004 (sica_7b_scaling) - planned
5. exp-005 (qwq_32b_operating_regime) - planned
6. exp-006 (c0_diagnostic_validation) - planned
7. exp-007 (sica_72b_awq) - planned
8. exp-008 (constraint_quality_case_studies) - planned
9. exp-009 (overhead_analysis) - planned
10. exp-010 (sica_mistral_7b) - planned
11. exp-011 (sica_llama_8b) - planned
12. exp-012 (gsm8k_pilot_14b) - planned
13. exp-013 (constraint_ablation) - planned
14. exp-014 - planned

I need to continue working through the remaining experiments and generate predicted best-case results for each one. (sica_deepseek_r1_llama_8b) - planned

The best tier definition:
- exp-001 confirms gains with statistical significance; cross-family and ablation all validate
- Core hypotheses:
  - FOLIO gain sustains at +4pp or above on 204 questions
  - ProofWriter shows modest positive gap (+1-3pp) on 600 questions
  - Combined gap statistically significant (p<0.05 bootstrap)
  - Cross-family (Mistral/LLaMA) both show C0>25% and positive SICA-SC gap
  - Constraint ablation shows MaxSAT > count-only by ≥2pp
  - C0 shows gradient across model scales (7B>14B>72B)

Now I'm mapping out the expected ranges for each key metric across the experiments—combined gap between 2.5-5pp, FOLIO gains hitting 4-8pp, ProofWriter's more modest 1-3pp improvement, and the bootstrap p-value staying below 0.05. I'm also tracking the C0 performance across different model sizes and families, the MaxSAT constraint advantage, and tiebreak win rates to build out detailed predictions for each experiment configuration.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a18cb4f0-3e3f-4b90-ad35-3c097d1e99dc",
  "isSidechain": false,
  "requestId": "req_011Cb6XPF3xnCp9mansTrKzP",
  "type": "assistant",
  "uuid": "213c4057-dcff-422b-8a1f-32f6222afcfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e1f050df-93c8-4723-a6a9-64d60ce0f070",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8beL7jHqEeLXzFpoGaYpU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12803,
      "cache_read_input_tokens": 11841,
      "output_tokens": 9727,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 9727,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12803
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

_source line 9 · 2026-05-16T16:02:24.853Z_

```yaml
tier: best
narrative_guidance: "Original framing holds — SICA is a principled, effective method with formally characterizable operating regime. All 3 claims stand at full strength. Hero figure (C0 vs gap scatter) shows clean threshold with gradient. Paper tells a complete story: method + when it works + why + how to know in advance."

imagined_experiments:
  - name: "sica_expanded_14b"
    plan_id: "exp-001"
    description: "Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12, T=0.7"
    expected_results:
      sica_accuracy_combined: 0.763
      sc_accuracy_combined: 0.728
      combined_gap_pp: 3.5
      folio_sica_accuracy: 0.814
      folio_sc_accuracy: 0.760
      folio_gap_pp: 5.4
      proofwriter_sica_accuracy: 0.745
      proofwriter_sc_accuracy: 0.722
      proofwriter_gap_pp: 2.3
      c0_combined: 0.43
      c0_folio: 0.48
      c0_proofwriter: 0.41
      bootstrap_p_combined: 0.018
      bootstrap_p_folio: 0.032
      bootstrap_p_proofwriter: 0.087
      total_constraints_raw: 78500
      total_constraints_unique: 22100
      maxsat_exclusion_rate: 0.031
      tiebreak_problems: 68
      tiebreak_sica_win_rate: 0.78
      wall_time_hours: 12.5
    result_rationale: "D012 pilot showed +6.7pp on FOLIO (30q) and 0pp on PW (30q). At scale, FOLIO gain regresses toward mean but stays strong (+5.4pp) because FOLIO's formal logic structure aligns perfectly with FOL constraint extraction — the method's sweet spot. ProofWriter emerges positive (+2.3pp) because 600 questions reveal a long tail of genuinely ambiguous depth-5 problems where trace diversity creates actionable ties; the pilot's 0pp was a small-sample floor effect (30q × 67% unanimous = only 10 contested problems). Combined significance achieves p=0.018 because 804 questions with 43% multi-candidate rate yields ~345 problems where SICA can differentiate, providing sufficient statistical power. The C0 sustains near pilot levels (pilot was 53%) because 14B-Instruct remains uncertain on logic reasoning at T=0.7 — these are genuinely difficult for a 14B instruction model."
    tables:
      - "T1: Main Results (14B row, FOLIO + PW columns)"
      - "T2: Tiebreak Analysis (68 tie problems, win/loss/draw)"
    figures_description:
      - "F2 data points: (C0=0.48, gap=5.4) for FOLIO-14B, (C0=0.41, gap=2.3) for PW-14B"
    analysis: "Core P0 result validates all three claims. FOLIO's stronger gain than PW reflects domain alignment: FOLIO premises are already near-FOL, so constraint extraction is high-fidelity. PW depth-5 has longer chains where extraction noise accumulates, diluting signal. The 78 tiebreak problems with 78% SICA win rate directly supports Claim 1. Bootstrap p=0.018 clears significance threshold."

  - name: "sica_k_ablation_14b"
    plan_id: "exp-002"
    description: "K sensitivity (K=6,8,12,16,20) on D012's 60 questions"
    expected_results:
      k6_sica_accuracy: 0.717
      k6_sc_accuracy: 0.700
      k6_gap_pp: 1.7
      k6_c0: 0.38
      k6_tiebreak_freq: 0.12
      k8_sica_accuracy: 0.733
      k8_sc_accuracy: 0.700
      k8_gap_pp: 3.3
      k8_c0: 0.45
      k8_tiebreak_freq: 0.22
      k12_sica_accuracy: 0.750
      k12_sc_accuracy: 0.700
      k12_gap_pp: 5.0
      k12_c0: 0.53
      k12_tiebreak_freq: 0.30
      k16_sica_accuracy: 0.750
      k16_sc_accuracy: 0.717
      k16_gap_pp: 3.3
      k16_c0: 0.55
      k16_tiebreak_freq: 0.25
      k20_sica_accuracy: 0.750
      k20_sc_accuracy: 0.733
      k20_gap_pp: 1.7
      k20_c0: 0.57
      k20_tiebreak_freq: 0.18
      optimal_k: 12
      wall_time_hours: 4.2
    result_rationale: "K=12 is optimal because it balances two opposing forces: (1) more samples increase C0 (more chances to surface minority answers), but (2) more samples also strengthen majority signal, reducing tie frequency. At K=6, too few samples → low C0 (38%) and few ties for SICA to resolve. At K=12, C0 peaks in utility — enough diversity to surface genuine alternatives without majority domination. At K=16/20, majority voting becomes so strong that ties become rare again (SC itself converges), and SICA's tiebreaking advantage shrinks even though C0 is nominally higher. The gap curve is thus non-monotonic: rises to K=12, plateaus, then narrows. This makes physical sense — SICA helps most when voting is close, not when it's unanimous or when majority dominates by large margin."
    tables:
      - "T3: K Sensitivity (5 rows × metrics)"
    figures_description:
      - "F4: K vs accuracy curve (SICA and SC lines), with tiebreak frequency overlay"
      - "F2 additional data points: 5 points at different K values showing C0-gap relationship within single model"
    analysis: "K=12 sweet spot confirms paper's default choice is principled, not cherry-picked. The non-monotonic gap pattern reveals SICA's mechanism: it specifically resolves close calls. At high K, SC self-resolves most ties through volume. This insight strengthens the 'principled tiebreaking' narrative — SICA is most valuable precisely where SC is least certain."

  - name: "tiebreak_baseline_analysis"
    plan_id: "exp-003"
    description: "Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available data"
    expected_results:
      sica_tiebreak_accuracy: 0.78
      sc_random_tiebreak_accuracy: 0.50
      sc_alphabetical_accuracy: 0.55
      sc_first_seen_accuracy: 0.45
      sc_longest_chain_accuracy: 0.52
      n_tiebreak_problems: 68
      sica_vs_random_p_value: 0.003
      sica_unique_wins: 21
      sica_unique_losses: 6
      random_equivalent_problems: 41
    result_rationale: "On 68 tied problems from exp-001 expanded data, SICA achieves 78% because MaxSAT constraint weighting genuinely captures reasoning quality signal — traces with more satisfiable constraints tend to contain fewer logical errors. Random tiebreak hits 50% by definition (chance on binary/ternary outcomes). Alphabetical gets 55% due to mild label-answer correlation in FOLIO (True slightly more common). First-seen gets 45% (slight anti-correlation with generation order). The 28pp gap over random (78% vs 50%) on 68 problems is significant at p=0.003 (binomial test), providing direct evidence that SICA's tiebreaking mechanism captures real signal rather than getting lucky. This is the cleanest possible defense against the 'random baseline closes the gap' attack."
    tables:
      - "T2: Tiebreak Comparison (5 strategies × win rate)"
    figures_description:
      - "Bar chart: tiebreak accuracy by method, with significance brackets"
    analysis: "The 28pp gap between SICA and random tiebreaking is the single most defensible number in the paper. It isolates SICA's contribution from any sampling or dataset artifact. 68 tie problems give sufficient power for a binomial test. This directly refutes Reviewer Concern #7."

  - name: "sica_7b_scaling"
    plan_id: "exp-004"
    description: "Qwen2.5-7B-Instruct on same 60 questions, testing weaker model → higher C0 → larger gain"
    expected_results:
      sica_accuracy: 0.633
      sc_accuracy: 0.583
      gap_pp: 5.0
      c0: 0.65
      folio_sica: 0.700
      folio_sc: 0.633
      folio_gap_pp: 6.7
      proofwriter_sica: 0.600
      proofwriter_sc: 0.567
      proofwriter_gap_pp: 3.3
      bootstrap_p: 0.14
      constraints_per_problem: 72
      extraction_rate: 0.95
      exclusion_rate: 0.045
      wall_time_hours: 1.8
    result_rationale: "7B model is weaker → lower base accuracy (58% vs 70% for 14B) but critically higher C0 (65% vs 53%). The weaker model genuinely doesn't know the answer to many problems, producing diverse candidate answers across 12 traces. This higher C0 gives SICA more contested problems to work with, yielding a larger absolute gap (+5.0pp vs +3.3pp for 14B). The mechanism is clear: 7B generates more traces with different answers → more ties → more opportunities for MaxSAT to pick the better-supported answer. Extraction rate stays high (95%) because Qwen-7B still follows instruction format well. Bootstrap p=0.14 on 60 questions isn't significant alone, but combined with 14B data and the clear C0-gap gradient, it validates the predictive relationship."
    tables:
      - "T1: Main Results (7B row)"
    figures_description:
      - "F2: (C0=0.65, gap=5.0) point — highest C0 in Qwen family, validates gradient"
      - "F3: Operating Regime Heatmap (7B column shows darker 'SICA helps' region)"
    analysis: "7B confirms the C0 gradient hypothesis within Qwen family: 7B (C0=0.65, gap=5.0) > 14B (C0=0.53, gap=3.3) > 72B (predicted C0~0.25, gap~1.0). This three-point gradient is the hero evidence for Claim 3. The lower absolute accuracy is expected and not a weakness — the paper's point is that SICA helps uncertain models, not that it makes weak models strong."

  - name: "qwq_32b_operating_regime"
    plan_id: "exp-005"
    description: "QwQ-32B negative results formatted for Operating Regime Analysis"
    expected_results:
      c0_combined: 0.036
      c0_aime: 0.0
      c0_folio: 0.0
      c0_proofwriter: 0.1875
      sica_sc_gap_pp: 0.0
      n_aime: 22
      n_folio: 10
      n_proofwriter: 16
      n_combined: 48
      reasoning_model_unanimous_rate: 0.964
      conclusion: "SICA≡SC when C0<5%"
    result_rationale: "QwQ-32B is a reasoning model with extended chain-of-thought that self-corrects during generation. Even at T=0.7, the reasoning chain converges to the same answer across all 12 samples because the model's internal verification loop dominates stochastic sampling. C0=3.6% means only ~2 out of 48 problems ever produce a second candidate answer. With no ties to break, SICA degenerates to SC structurally — MaxSAT confirms the unanimous winner. This is the perfect negative control: the method correctly does nothing when there's nothing to resolve. The contrast with instruction models (C0=43-65%) demonstrates that C0 reflects reasoning architecture, not task difficulty — same tasks, radically different C0."
    tables:
      - "T1: Main Results (QwQ-32B row, gap=0.0)"
    figures_description:
      - "F2: (C0=0.036, gap=0.0) point — anchors the left side of the scatter plot"
      - "F3: Operating Regime Heatmap (QwQ column is uniformly 'SICA=SC' zone)"
    analysis: "QwQ data transforms from 'failed experiment' into strongest evidence for Claim 2. The C0=3.6% vs instruction model C0=43-65% gap on identical tasks proves that trace diversity reflects model architecture/confidence, not task properties. This is the key insight: 'symbolic consensus helps when there IS disagreement to resolve.' Paper frames this as positive contribution, not limitation."

  - name: "c0_diagnostic_validation"
    plan_id: "exp-006"
    description: "Plot C0 vs SICA-SC gap across all models and K values"
    expected_results:
      n_data_points: 14
      pearson_r: 0.89
      spearman_rho: 0.91
      c0_threshold_20pct_sensitivity: 1.0
      c0_threshold_20pct_specificity: 1.0
      linear_fit_slope: 0.09
      linear_fit_intercept: -0.015
      auc_binary_classifier: 0.96
      models_included: ["Qwen-7B", "Qwen-14B", "Qwen-72B", "QwQ-32B", "Mistral-7B", "LLaMA-8B", "DeepSeek-R1-8B"]
      k_values_included: [6, 8, 12, 16, 20]
    result_rationale: "With 14 data points spanning C0 from 0.036 (QwQ) to 0.65 (Qwen-7B), the scatter plot shows a clean positive relationship (r=0.89) because the mechanism is causal: higher C0 → more ties → more SICA tiebreaking opportunities → larger gap. The threshold at C0=20% has perfect sensitivity/specificity because below 20%, there simply aren't enough multi-candidate problems for SICA to accumulate a measurable gap (even at 78% tiebreak accuracy, <20% ties on 60 questions = <12 contested problems = <3 expected flips = noise). The relationship isn't perfectly linear (it's bounded above by tiebreak accuracy × tie frequency) but is monotonically positive across the observed range. AUC=0.96 for binary classification ('will SICA help?') validates C0 as a zero-cost deployment diagnostic."
    tables: []
    figures_description:
      - "F2 (Hero Figure): C0 vs gap scatter, 14 points, with threshold line at C0=20%, linear fit, and confidence band. Points colored by model family (Qwen=blue, Mistral=orange, LLaMA=green, QwQ/DeepSeek=red). Clear separation between reasoning models (bottom-left cluster) and instruction models (upper-right spread)."
    analysis: "This is the paper's hero figure. The clean correlation (r=0.89) across 3 families, 2 architectures, and 5 K values demonstrates that C0 is a universal predictor of SICA utility. The figure alone tells the paper's story: check C0 before deploying SICA. Practitioners can compute C0 from existing SC samples at zero additional cost."

  - name: "sica_72b_awq"
    plan_id: "exp-007"
    description: "Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions"
    expected_results:
      sica_accuracy: 0.833
      sc_accuracy: 0.817
      gap_pp: 1.7
      c0: 0.25
      folio_sica: 0.867
      folio_sc: 0.867
      folio_gap_pp: 0.0
      proofwriter_sica: 0.833
      proofwriter_sc: 0.800
      proofwriter_gap_pp: 3.3
      bootstrap_p: 0.38
      constraints_per_problem: 95
      extraction_rate: 0.98
      wall_time_hours: 3.8
    result_rationale: "72B is a strong instruction model with high base accuracy (82%) but still non-reasoning, so it retains some trace diversity (C0=25%) — enough to stay above the 20% threshold but much lower than 14B (53%) or 7B (65%). The gap is small (+1.7pp) because few problems are contested, but it's positive because those contested problems still benefit from MaxSAT resolution. FOLIO gap hits 0pp because 72B gets nearly all FOLIO problems right with SC alone (87% accuracy → few ties). ProofWriter retains a gap because depth-5 reasoning chains remain challenging even for 72B. This completes the within-Qwen gradient: 7B (C0=0.65, +5.0pp) > 14B (C0=0.53, +3.3pp) > 72B (C0=0.25, +1.7pp), showing C0 and gap both decrease monotonically with scale."
    tables:
      - "T1: Main Results (72B row)"
    figures_description:
      - "F2: (C0=0.25, gap=1.7) point — completes 3-point Qwen gradient"
      - "Inset: Qwen scaling curve (3 points connected by line)"
    analysis: "72B provides the critical third point for the within-family scaling gradient. The monotonic C0 decrease with scale (65% → 53% → 25%) directly maps to gap decrease (5.0 → 3.3 → 1.7), providing causal evidence that model capability (reflected as lower C0) reduces SICA's opportunity. At C0=25% the model is at the boundary — still above threshold but barely. This supports Claim 3's 'continuous predictor' framing over 'binary indicator'."

  - name: "constraint_quality_case_studies"
    plan_id: "exp-008"
    description: "Qualitative analysis of extracted constraints on 5-10 representative questions"
    expected_results:
      problems_analyzed: 8
      semantically_meaningful_rate: 0.85
      excluded_constraints_are_errors_rate: 0.75
      constraint_types: ["implication", "universal_quantification", "negation", "conjunction", "disjunction"]
      sica_correct_sc_wrong_cases: 3
      interpretable_reason_rate: 1.0
      folio_constraint_quality: "high - premises map directly to FOL"
      proofwriter_constraint_quality: "medium - longer chains introduce noise"
    result_rationale: "FOLIO premises are designed as near-FOL natural language, so constraint extraction produces semantically faithful FOL formulas 85%+ of the time. When MaxSAT excludes constraints, they predominantly (75%) correspond to traces with genuine reasoning errors — the model made a logical misstep, producing an inconsistent constraint set. The 3 cases where SICA corrects SC are interpretable: in each, the correct-answer traces produce mutually consistent constraints while incorrect-answer traces contain contradictions that MaxSAT identifies and downweights. This qualitative evidence makes the quantitative gains mechanistically interpretable for reviewers."
    tables: []
    figures_description:
      - "Case study box (Appendix): 2-3 example problems showing extracted constraints, MaxSAT solution, and how SICA flips SC's wrong answer"
    analysis: "Case studies provide the interpretability layer reviewers demand. They show SICA isn't a black box — the constraint extraction and MaxSAT resolution have semantically meaningful behavior. The 75% error-exclusion rate means MaxSAT genuinely identifies bad reasoning, not just random noise filtering."

  - name: "overhead_analysis"
    plan_id: "exp-009"
    description: "Wall-time breakdown per question: generation, constraint extraction, MaxSAT solving"
    expected_results:
      avg_total_time_per_problem_s: 85
      generation_time_s: 72
      generation_fraction: 0.847
      constraint_extraction_time_s: 11
      extraction_fraction: 0.129
      maxsat_solving_time_s: 2
      maxsat_fraction: 0.024
      overhead_vs_sc_pct: 15.3
      marginal_cost_per_pp_gain: "4.4s per +1pp"
      gpu_cost_fraction: 0.98
      cpu_only_fraction: 0.02
    result_rationale: "Generation dominates (85%) because K=12 traces with Qwen-14B at ~512 tokens each requires 12 forward passes through a 14B model. Constraint extraction adds 13% — it's an additional LLM call per trace but with a shorter prompt/response (extract FOL from single trace). MaxSAT solving is negligible (2%) because Z3 solves weighted partial MaxSAT on ~20-100 constraints in milliseconds. Total overhead vs vanilla SC (which also needs K=12 generations) is only 15% — the extraction call is the only addition. This means SICA's cost is dominated by the same generation cost SC already pays. The 15% overhead for +3.5pp gain is a favorable trade-off reviewers can evaluate quantitatively."
    tables:
      - "T4: Overhead Breakdown (generation/extraction/solving × time/fraction)"
    figures_description:
      - "Stacked bar chart: time breakdown per component, showing generation dominates"
    analysis: "The 15% overhead number is the key reviewer-facing metric. Since SC already requires K generations, SICA only adds constraint extraction (one additional short LLM call per trace). MaxSAT is free (CPU, milliseconds). This pre-empts the 'impractical overhead' objection — the marginal cost is one extraction call per trace, amortized over K=12 samples that were already being generated."

  - name: "sica_mistral_7b"
    plan_id: "exp-010"
    description: "Mistral-7B-Instruct-v0.3 on D012 60 questions, cross-family validation"
    expected_results:
      sica_accuracy: 0.617
      sc_accuracy: 0.583
      gap_pp: 3.3
      c0: 0.55
      folio_sica: 0.667
      folio_sc: 0.633
      folio_gap_pp: 3.3
      proofwriter_sica: 0.600
      proofwriter_sc: 0.567
      proofwriter_gap_pp: 3.3
      bootstrap_p: 0.19
      constraints_per_problem: 58
      extraction_rate: 0.92
      exclusion_rate: 0.038
      wall_time_hours: 1.3
    result_rationale: "Mistral-7B is a comparable-scale instruction model to Qwen-7B but from a completely different training pipeline (Mistral AI vs Alibaba). It shows C0=55% because at 7B scale, instruction models are genuinely uncertain on formal logic tasks regardless of training family. The gap (+3.3pp) is positive and within the best-tier range [1.5, 5.0] because the same mechanism applies: diverse traces → ties → MaxSAT resolution. Extraction rate is slightly lower (92% vs 95% for Qwen) because Mistral's instruction following is marginally less consistent, but still high enough for the pipeline to function. Bootstrap p=0.19 on 60 questions isn't significant alone, but the point is cross-family replication of the C0-gap pattern, not individual significance. The key finding: C0=55% (>25% threshold) confirms this isn't a Qwen-specific artifact."
    tables:
      - "T1: Main Results (Mistral-7B row)"
    figures_description:
      - "F2: (C0=0.55, gap=3.3) point in orange — aligns with Qwen trend line"
      - "F3: Mistral column in heatmap"
    analysis: "Mistral replication eliminates the single most dangerous reviewer attack: 'Qwen-specific artifact.' C0=55% and positive gap demonstrate that the mechanism is architecture-independent — any instruction model with sufficient uncertainty shows the same pattern. Combined with LLaMA (exp-011), this gives 3-family coverage meeting EMNLP minimum bar."

  - name: "sica_llama_8b"
    plan_id: "exp-011"
    description: "LLaMA-3.1-8B-Instruct on D012 60 questions, third family"
    expected_results:
      sica_accuracy: 0.600
      sc_accuracy: 0.567
      gap_pp: 3.3
      c0: 0.52
      folio_sica: 0.633
      folio_sc: 0.600
      folio_gap_pp: 3.3
      proofwriter_sica: 0.567
      proofwriter_sc: 0.533
      proofwriter_gap_pp: 3.3
      bootstrap_p: 0.21
      constraints_per_problem: 55
      extraction_rate: 0.90
      exclusion_rate: 0.042
      wall_time_hours: 1.4
    result_rationale: "LLaMA-3.1-8B is Meta's instruction-tuned model at similar scale to Mistral-7B. It shows C0=52% — slightly lower than Mistral (55%) because LLaMA-3.1's instruction tuning is somewhat more consistent, but still well above the 20% threshold. The +3.3pp gap confirms the pattern holds across a third completely independent model family. Base accuracy is slightly lower than Mistral (57% vs 58%) reflecting minor capability differences at this scale. Extraction rate is 90% — LLaMA's chat template is slightly different and occasionally produces traces that don't parse cleanly, but the pipeline is robust enough to handle this. The 3-family convergence (Qwen C0=53%, Mistral C0=55%, LLaMA C0=52% — all ~50-55% at 7-14B scale) strongly suggests C0 is a property of task-model capability interaction, not training data or architecture specifics."
    tables:
      - "T1: Main Results (LLaMA-8B row)"
    figures_description:
      - "F2: (C0=0.52, gap=3.3) point in green — clusters with Mistral, confirms family-independence"
    analysis: "LLaMA provides the third family for EMNLP's implicit '3 model families' requirement. The clustering of all three 7-8B instruction models at C0≈50-55% with gap≈3-5pp is powerful evidence that the phenomenon is universal to instruction-tuned models at this capability level. Combined cross-family result: mean gap = +3.3pp, all C0 > 25%, all gaps positive."

  - name: "gsm8k_pilot_14b"
    plan_id: "exp-012"
    description: "Qwen2.5-14B on GSM8K 30-question pilot (K=12), cross-domain test"
    expected_results:
      sica_accuracy: 0.900
      sc_accuracy: 0.900
      gap_pp: 0.0
      c0: 0.10
      constraints_per_problem: 42
      extraction_rate: 0.88
      exclusion_rate: 0.02
      multi_candidate_problems: 3
      wall_time_hours: 0.8
    result_rationale: "Qwen2.5-14B achieves ~90% on GSM8K because it's an easy benchmark for this model class. With 90% accuracy and K=12, most problems have 11-12 traces agreeing on the correct answer → C0=10% (only 3/30 problems have any diversity). This low C0 is NOT because the constraint extraction fails — extraction rate is still 88% — but because the model simply knows the answers. SICA=SC because there are no ties to break. This is the ideal 'negative control for a different reason': on logic tasks, 14B shows high C0 because the tasks challenge it; on arithmetic, the same model shows low C0 because it's too capable. This proves C0 reflects task-relative difficulty, strengthening Claim 3's 'practical diagnostic' framing — if you see low C0, don't bother with SICA regardless of domain."
    tables:
      - "Appendix table: GSM8K pilot results"
    figures_description:
      - "F2: (C0=0.10, gap=0.0) point — same model as (C0=0.48, gap=5.4), different task. Arrow annotation: 'same model, task-dependent C0'"
      - "F3: GSM8K column shows 14B in 'SICA=SC' zone (contrasts with logic column)"
    analysis: "GSM8K confirms C0 is task-relative, not model-fixed. The same 14B model shows C0=48% on FOLIO but C0=10% on GSM8K — proving C0 reflects model-task interaction, not just model weakness. This is a key insight for practitioners: compute C0 on YOUR task before deciding to deploy SICA. For paper, this adds the cross-domain dimension without requiring SICA to 'work' on easy tasks."

  - name: "constraint_ablation"
    plan_id: "exp-013"
    description: "SICA-MaxSAT vs SICA-count-only vs SICA-random-weight, CPU-only"
    expected_results:
      maxsat_accuracy: 0.763
      count_only_accuracy: 0.737
      random_weight_accuracy: 0.728
      maxsat_vs_count_only_gap_pp: 2.6
      maxsat_vs_random_weight_gap_pp: 3.5
      count_only_vs_sc_gap_pp: 0.9
      maxsat_tiebreak_accuracy: 0.78
      count_only_tiebreak_accuracy: 0.62
      random_weight_tiebreak_accuracy: 0.51
      n_problems_where_methods_differ: 22
      maxsat_wins_over_count: 14
      count_wins_over_maxsat: 5
      ties_between_methods: 3
    result_rationale: "MaxSAT beats count-only by 2.6pp because satisfiability checking adds genuine signal beyond constraint counting. Count-only asks 'which answer has more supporting constraints?' — this captures quantity but not quality. MaxSAT asks 'which answer has the most internally consistent constraint set?' — this captures whether the reasoning chains are logically coherent, not just numerous. On the 22 problems where they differ, MaxSAT wins 14 vs count-only's 5 because constraint consistency correlates with reasoning correctness: a correct reasoning chain produces constraints that form a satisfiable set, while an incorrect chain often produces contradictions. Random-weight performs near SC-random (51% tiebreak accuracy) confirming that the weighting scheme matters. The 2.6pp gap (within [2.0, 5.0] best-tier range) directly refutes the 'over-engineering' objection — MaxSAT's satisfiability reasoning is genuinely load-bearing."
    tables:
      - "Appendix Table: Constraint Ablation (3 methods × accuracy + tiebreak performance)"
    figures_description:
      - "Bar chart: Accuracy by method (MaxSAT > count-only > random-weight > SC-baseline)"
    analysis: "This is the make-or-break experiment for Claim 1's 'principled tiebreaking through satisfiability' framing. The 2.6pp MaxSAT advantage over count-only proves that the SAT-solving machinery adds value — it's not just counting constraints, it's verifying their mutual consistency. If this were ≤1pp, we'd need to reframe as 'principled weighting.' At 2.6pp, the current framing ('satisfiability-based reasoning aggregation') is fully supported."

  - name: "sica_deepseek_r1_llama_8b"
    plan_id: "exp-014"
    description: "DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions, second reasoning model"
    expected_results:
      sica_accuracy: 0.717
      sc_accuracy: 0.717
      gap_pp: 0.0
      c0: 0.05
      folio_sica: 0.767
      folio_sc: 0.767
      folio_gap_pp: 0.0
      proofwriter_sica: 0.700
      proofwriter_sc: 0.700
      proofwriter_gap_pp: 0.0
      constraints_per_problem: 85
      extraction_rate: 0.93
      multi_candidate_problems: 3
      reasoning_trace_avg_tokens: 1800
      wall_time_hours: 1.8
    result_rationale: "DeepSeek-R1-Distill-LLaMA-8B is a reasoning-distilled model — it has internalized the extended chain-of-thought pattern from R1 into an 8B LLaMA architecture. Despite being much smaller than QwQ-32B, it still shows C0=5% because the reasoning distillation teaches the model to self-verify, producing convergent outputs regardless of sampling temperature. Only 3/60 problems show any diversity. SICA=SC identically because with no ties, MaxSAT simply confirms the unanimous vote. This is crucial: it demonstrates that low C0 is a property of REASONING TRAINING (distillation/RL for chain-of-thought), not model size (QwQ is 32B, DeepSeek-R1-distill is 8B) or model family (QwQ is Qwen-based, this is LLaMA-based). The contrast with LLaMA-3.1-8B-Instruct (same base architecture, C0=52%) is dramatic: same LLaMA-8B base, but instruction-tuned vs reasoning-distilled produces C0=52% vs C0=5%."
    tables:
      - "T1: Main Results (DeepSeek-R1-8B row, gap=0.0)"
    figures_description:
      - "F2: (C0=0.05, gap=0.0) point — clusters with QwQ at bottom-left"
      - "Annotation arrow between LLaMA-8B-Instruct (C0=52%) and DeepSeek-R1-LLaMA-8B (C0=5%): 'same base, different training → different C0'"
    analysis: "DeepSeek-R1 provides the second reasoning model negative control with a different base architecture. The LLaMA-8B-Instruct vs DeepSeek-R1-LLaMA-8B comparison is the paper's most elegant evidence: same base model, but instruction tuning → C0=52% while reasoning distillation → C0=5%. This proves C0 reflects training regime (reasoning vs instruction), not architecture or scale. It also eliminates the 'QwQ is still Qwen family' attack, since this uses LLaMA base."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "213c4057-dcff-422b-8a1f-32f6222afcfc",
  "isSidechain": false,
  "requestId": "req_011Cb6XPF3xnCp9mansTrKzP",
  "type": "assistant",
  "uuid": "93326989-d56d-416d-9ece-4c3177dafae3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e1f050df-93c8-4723-a6a9-64d60ce0f070",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q8beL7jHqEeLXzFpoGaYpU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12803,
      "cache_read_input_tokens": 11841,
      "output_tokens": 9727,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12803,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 9727,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12803,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12803
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：exp-001 confirms gains with statistical significance; cross-family and ablation all validate 核心假设：['FOLIO gain sustains at +4pp or above on 204 questions',…",
  "leafUuid": "93326989-d56d-416d-9ece-4c3177dafae3",
  "sessionId": "e1f050df-93c8-4723-a6a9-64d60ce0f070"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 best-tier experiment predictions with rationales",
  "sessionId": "e1f050df-93c8-4723-a6a9-64d60ce0f070"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：exp-001 confirms gains with statistical significance; cross-family and ablation all validate 核心假设：['FOLIO gain sustains at +4pp or above on 204 questions',…",
  "leafUuid": "93326989-d56d-416d-9ece-4c3177dafae3",
  "sessionId": "e1f050df-93c8-4723-a6a9-64d60ce0f070"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 best-tier experiment predictions with rationales",
  "sessionId": "e1f050df-93c8-4723-a6a9-64d60ce0f070"
}
```

---
