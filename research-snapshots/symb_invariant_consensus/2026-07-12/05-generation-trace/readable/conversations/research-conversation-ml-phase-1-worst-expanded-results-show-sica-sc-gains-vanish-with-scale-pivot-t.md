# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Expanded results show SICA ≈ SC; gains vanish with scale; pivot to analysis

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/a7e65dd3-b494-43d7-ae29-482a1923e8f3.jsonl`
- **Structured JSON:** [`8964a34013643c0de470.json`](../../sessions/89/8964a34013643c0de470.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T16:10:40.069Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T16:10:40.069Z",
  "sessionId": "a7e65dd3-b494-43d7-ae29-482a1923e8f3",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Expanded results show SICA ≈ SC; gains vanish with scale; pivot to analysis/characterization paper\n核心假设：[\"FOLIO gap shrinks to ≤+2pp on 204 questions (D012's +6.7 was small-sample artifact)\", 'ProofWriter shows 0 or slightly negative gap', 'Combined gap ≤+1pp, not significant (p>0.2)', 'C0 pattern still holds (high C0 for instruction models, low for reasoning models)', \"But high C0 does NOT translate to SICA>SC — diversity exists but MaxSAT doesn't exploit it effectively\", 'Constraint extraction quality is the bottleneck (noisy FOL, wrong exclusions)', 'Cross-family shows similar pattern — C0 high but gap ≈ 0']\n关键指标范围：{'combined_gap_pp': [-0.5, 1.0], 'folio_gap_pp': [0.0, 2.5], 'proofwriter_gap_pp': [-1.5, 0.5], 'bootstrap_p_combined': [0.15, 0.5], 'c0_14b_expanded': [0.3, 0.55], 'c0_mistral_7b': [0.2, 0.5], 'c0_llama_8b': [0.2, 0.5], 'cross_family_gap_pp': [-1.0, 1.5], 'maxsat_vs_count_only_pp': [-1.0, 1.0], 'tiebreak_win_rate': [0.5, 0.65]}\n叙事方向：Activate D023 contingency. Core reframe: 'Characterizing When Symbolic Consensus Methods Fail — and Why Trace Diversity Is Necessary But Not Sufficient.' Claim 1 becomes 'SICA provides interpretable tiebreaking' (no accuracy claim). Claim 2 survives intact — operating regime characterization is the paper's primary contribution, now framed as explaining failure modes. New angle: C0 measures output diversity but constraint extraction quality is the missing second condition. Add constraint-quality-vs-gap correlation analysis (CPU-only). Claim 3 reframes as 'C0 as necessary condition diagnostic' (high C0 needed but not sufficient). The intellectual contribution is the negative-result insight: why naive symbolic aggregation doesn't straightforwardly improve over voting despite intuitive appeal. Target EMNLP Findings (primary) or AAAI 2027 Main (fallback with additional method improvements).\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Fallback: AAAI 2027 (Aug 1)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条)\n1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).\n2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is governed by trace diversity (C0), which reflects effective output diversity — SICA adds value when C0>20% (diverse outputs, disagreement to resolve) but degenerates to SC when C0<5% (converged outputs, no disagreement). C0 empirically correlates with task-relative model confidence: instruction models show high C0 on challenging tasks, reasoning models show low C0 universally. Validated across 3 model families (Qwen, Mistral, LLaMA) and 2 reasoning architectures (QwQ, DeepSeek-R1). [Note: \"C0 → epistemic uncertainty\" connection reserved for Discussion, not formal claim — reviewer risk of terminology abuse per UQ community standards.]\n3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.\n\n## Core Insight\nSymbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that trace diversity (C0) — reflecting task-relative model confidence rather than model family or task domain alone — determines the operating regime. This transforms SICA from \"yet another ensemble method\" into \"a method with formally characterizable applicability boundaries,\" validated across 3 model families and multiple reasoning domains.\n\n## Story Spine\n- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.\n- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.\n- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75%+ win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) — a zero-cost diagnostic reflecting effective output diversity — and validate across 3 model families (Qwen, Mistral, LLaMA), 2 reasoning architectures (QwQ, DeepSeek-R1), and multiple domains (logic, math).\n- **Headline result template**: \"On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → exp-001: Expand to 804 questions for statistical power\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K sensitivity; exp-009: overhead analysis (P1); exp-013: constraint ablation (MaxSAT vs count-only vs random-weight)\n3. **\"Only Qwen models — family-specific artifact?\"** → exp-010: Mistral-7B + exp-011: LLaMA-8B (3-family validation)\n4. **\"Only one reasoning model\"** → exp-014: DeepSeek-R1-Distill-7B (second reasoning architecture)\n5. **\"Only logic domain — restricted answer space\"** → exp-012: GSM8K pilot with 14B (cross-domain C0 test)\n6. **\"ProofWriter shows 0pp gain\"** → Domain analysis in exp-001 expanded results\n7. **\"Random tiebreak baseline closes the gap\"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison (done on D012, will re-run on expanded)\n8. **\"Why not just use a reasoning model?\"** → exp-005: QwQ-32B + exp-014: DeepSeek-R1 show reasoning models are self-consistent → SICA redundant; instruction models (cheaper, more deployed) benefit\n9. **\"MAX-SAT is over-engineering\"** → exp-013: Constraint ablation proves satisfiability checking adds value over simple counting\n10. **\"Within-family scaling?\"** → exp-004: 7B + exp-007: 72B-AWQ show C0 trend within Qwen family\n\n## Working Title\n**\"When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation\"**\n(Alternatives: \"Beyond Majority Voting: Using Trace Diversity to Predict When Symbolic Consensus Improves LLM Reasoning\")\n\n## Paper Structure (EMNLP 8pp + appendix)\n- Main Tables: T1 (Main Results 7 models × datasets), T2 (Tiebreak Comparison), T3 (K Sensitivity), T4 (Overhead)\n- Main Figures: F1 (Pipeline), F2 (C0 vs Gap Scatter — hero figure), F3 (Operating Regime Heatmap), F4 (K Curve)\n- Appendix: Constraint Ablation (exp-013), Case Studies (exp-008), GSM8K (exp-012), Per-Problem Detail\n\n## Claim Risk Notes\n- **Claim 1 make-or-break**: exp-013 constraint ablation. If MaxSAT ≈ count-only → reframe as \"principled weighting\" not \"satisfiability-based reasoning\"\n- **Claim 3 downgrade risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to \"binary indicator\" not \"continuous predictor\". Gradient depends on 7B C0 >> 14B C0 >> 72B C0.\n- **\"Epistemic uncertainty\" terminology**: Reserve for Discussion section only. Main text uses \"effective output diversity\" / \"task-relative model confidence\". UQ community would attack formal misuse.\n\n## Contingency Plan (D023)\n**Trigger**: exp-001 完整结果 SICA ≤ SC（gap ≤ 0pp 或不显著）\n**Strategy**: Option A (Analysis Paper) + Option C (FOLIO sub-claim if positive)\n- 论文主线从\"SICA improves accuracy\"转为\"characterizing operating conditions of symbolic consensus\"\n- C0 threshold pattern 成为核心贡献（\"at what C0 level does SICA begin to match/exceed SC?\")\n- FOLIO 正向结果嵌入为\"domain formality → effectiveness\"子 claim\n- Claim 1 弱化为\"principled + interpretable tiebreaking\"（不 claim accuracy gain）\n- 需补：constraint extraction quality vs delta 相关性分析（CPU-only）\n- Venue: EMNLP Main (30-35%) / Findings (60-70%) / AAAI 2027 fallback\n**Decision point**: exp-001 FOLIO 70题的 C0 和 delta\n\n## Venue Fit Risks\n- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the \"operating regime characterization\" — the tiebreaking mechanism is evidence, not the claim.\n- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.\n- Negative results: QwQ-32B data must be presented as insight (\"When Does Symbolic Consensus Degenerate?\"), not failure.\n- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.\n- **[D023 新增]** If SICA ≤ SC globally: pivot to analysis paper. Must answer \"so what should practitioners do?\" → C0 as deployment diagnostic.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: RUNNING\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,12,16,20) on D012''s 60 questions. Key questions:\n    does SICA benefit depend on tiebreaks? What happens at odd K (no even splits)?\n    How does tiebreak frequency change with K?'\n  priority: P0\n  gpu_budget_hours: 5\n  deps: []\n  status: planned\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Within-Qwen scaling dimension.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX\n    PRO 6000 单卡可放。\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。\n- id: exp-010\n  name: sica_mistral_7b\n  claim:\n  - 2\n  - 3\n  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family\n    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''\n    attack.'\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+\n    题（~3h GPU，margin 允许）。'\n- id: exp-011\n  name: sica_llama_8b\n  claim:\n  - 2\n  - 3\n  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.\n    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation\n    同 exp-010。\n- id: exp-012\n  name: gsm8k_pilot_14b\n  claim:\n  - 2\n  - 3\n  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:\n    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer\n    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain\n    win.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable\n    insight.\n- id: exp-013\n  name: constraint_ablation\n  claim:\n  - 1\n  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count\n    per answer, no satisfiability) vs SICA-random-weight. Tests whether MAX-SAT is\n    essential or over-engineering.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 新增. 防御 'over-engineering' reviewer attack. CPU-only, 零 GPU 成本。\n- id: exp-014\n  name: sica_deepseek_r1_llama_8b\n  claim:\n  - 2\n  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning\n    model data point with LLaMA base architecture: validates C0<5% generalizes beyond\n    QwQ-32B AND eliminates ''still Qwen family'' attack.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T16:10:40.074Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T16:10:40.074Z",
  "sessionId": "a7e65dd3-b494-43d7-ae29-482a1923e8f3"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T16:10:40.104Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Expanded results show SICA ≈ SC; gains vanish with scale; pivot to analysis/characterization paper
核心假设：["FOLIO gap shrinks to ≤+2pp on 204 questions (D012's +6.7 was small-sample artifact)", 'ProofWriter shows 0 or slightly negative gap', 'Combined gap ≤+1pp, not significant (p>0.2)', 'C0 pattern still holds (high C0 for instruction models, low for reasoning models)', "But high C0 does NOT translate to SICA>SC — diversity exists but MaxSAT doesn't exploit it effectively", 'Constraint extraction quality is the bottleneck (noisy FOL, wrong exclusions)', 'Cross-family shows similar pattern — C0 high but gap ≈ 0']
关键指标范围：{'combined_gap_pp': [-0.5, 1.0], 'folio_gap_pp': [0.0, 2.5], 'proofwriter_gap_pp': [-1.5, 0.5], 'bootstrap_p_combined': [0.15, 0.5], 'c0_14b_expanded': [0.3, 0.55], 'c0_mistral_7b': [0.2, 0.5], 'c0_llama_8b': [0.2, 0.5], 'cross_family_gap_pp': [-1.0, 1.5], 'maxsat_vs_count_only_pp': [-1.0, 1.0], 'tiebreak_win_rate': [0.5, 0.65]}
叙事方向：Activate D023 contingency. Core reframe: 'Characterizing When Symbolic Consensus Methods Fail — and Why Trace Diversity Is Necessary But Not Sufficient.' Claim 1 becomes 'SICA provides interpretable tiebreaking' (no accuracy claim). Claim 2 survives intact — operating regime characterization is the paper's primary contribution, now framed as explaining failure modes. New angle: C0 measures output diversity but constraint extraction quality is the missing second condition. Add constraint-quality-vs-gap correlation analysis (CPU-only). Claim 3 reframes as 'C0 as necessary condition diagnostic' (high C0 needed but not sufficient). The intellectual contribution is the negative-result insight: why naive symbolic aggregation doesn't straightforwardly improve over voting despite intuitive appeal. Target EMNLP Findings (primary) or AAAI 2027 Main (fallback with additional method improvements).

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
  "promptId": "5dcff72f-2a7a-45c5-b434-e9c1359d6662",
  "type": "user",
  "uuid": "712df288-7cec-40c2-b821-81dab59e5ce3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "a7e65dd3-b494-43d7-ae29-482a1923e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T16:10:40.102Z_

```json
{
  "parentUuid": "712df288-7cec-40c2-b821-81dab59e5ce3",
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
  "uuid": "79a882a4-6d54-4e36-91e8-0209e3bc5441",
  "timestamp": "2026-05-16T16:10:40.102Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "a7e65dd3-b494-43d7-ae29-482a1923e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T16:10:40.102Z_

```json
{
  "parentUuid": "79a882a4-6d54-4e36-91e8-0209e3bc5441",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "07db033e-eaef-481f-b6b9-b755ee488976",
  "timestamp": "2026-05-16T16:10:40.102Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "a7e65dd3-b494-43d7-ae29-482a1923e8f3",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Expanded results show SICA ≈ SC; gains vanish with scale; pivot to analysis/characterization paper 核心假设：[\"FOLIO gap shrinks to ≤+2pp on 204 questions (D01…",
  "leafUuid": "07db033e-eaef-481f-b6b9-b755ee488976",
  "sessionId": "a7e65dd3-b494-43d7-ae29-482a1923e8f3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing when symbolic consensus fails with trace diversity",
  "sessionId": "a7e65dd3-b494-43d7-ae29-482a1923e8f3"
}
```

---

### Assistant

_source line 8 · 2026-05-16T16:11:11.699Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment data for every "planned" experiment in the experiment_plan, under the "worst" tier scenario. I need to provide result_rationale for each prediction explaining why this result would occur in this tier.

Let me go through each planned experiment and generate worst-tier predictions based on the defined worst-tier characteristics:

Worst tier key characteristics:
- Combined gap: [-0.5, 1.0] pp
- FOLIO gap: [0.0, 2.5] pp
- ProofWriter gap: [-1.5, 0.5] pp
- Bootstrap p combined: [0.15, 0.5]


- C0 14B expanded: [0.3, 0.55]
- C0 Mistral 7B: [0.2, 0.5]
- C0 LLaMA 8B: [0.2, 0.5]
- Cross-family gap: [-1.0, 1.5] pp
- MaxSAT vs count-only: [-1.0, 1.0] pp
- Tiebreak win rate: [0.5, 0.65]

Now I'm looking at the performance ranges across different model sizes and configurations, where the narrative suggests SICA performs roughly equivalent to standard chain-of-thought, improvements diminish as models scale up, and the focus shifts toward analyzing why these patterns emerge.

The core insight is reframing this as a characterization study—understanding when and why symbolic consensus methods fail rather than just measuring their gains. The bottleneck appears to be constraint extraction quality, not the consensus mechanism itself. I'm mapping out eight planned experiments ranging from the currently running full-scale evaluation to ablations on key parameters like K sensitivity, cross-model scaling effects, and diagnostic validation of the C0 metric, with the final experiments targeting constraint quality analysis and larger model variants.

Now I'm laying out the remaining experiments: overhead profiling, cross-family model comparisons with Mistral and LLaMA, a cross-domain pilot on GSM8K, constraint ablation studies comparing MaxSAT against simpler counting approaches, and a second reasoning model variant. For the worst-performing tier, I'm expecting FOLIO's gap to shrink substantially from the initial +6.7 percentage points down to around +2 on the full question set, while ProofWriter likely shows minimal or negative gains—the earlier small-sample results were probably noise.

The key insight emerging is that even when C0 scores are high for instruction-following tasks, this doesn't reliably translate to SICA outperforming SC, suggesting constraint extraction quality is the real limiting factor. This pattern should hold across different model families too. Now I'm working through the detailed predictions for each experiment, starting with the main 804-question set where I expect FOLIO to show a modest +2 point advantage, ProofWriter to be essentially flat, and the combined results to hover near zero with no statistical significance.

For the sensitivity analysis on K values, the gap fluctuates between 0-3 points depending on how often tiebreaks occur, with odd K values producing fewer ties and slightly tighter gaps. The tiebreak baseline experiment reveals that SICA's win rate on tiebreaks is only around 58%, much weaker than the 80% we see in other datasets, and when I apply random tiebreaking instead, the gap nearly closes entirely. Scaling to 7B models shows higher constraint overlap but introduces more noise, while the 32B QwQ results are already in the data showing essentially no difference between methods. The diagnostic work on C0 confirms it's weakly correlated with performance gaps—necessary but far from sufficient—and the 72B AWQ model appears to have very low constraint overlap.

Looking at the remaining experiments, I'm seeing a consistent pattern: stronger models like DeepSeek-R1 and the 72B variant show minimal constraint overlap and negligible gaps, while weaker models produce more diverse constraints but also noisier ones. The case studies reveal that many constraints are syntactically correct but semantically problematic, and the overhead per question is substantial. Across different model sizes and datasets—Mistral 7B, LLaMA 8B, GSM8K—the constraint overlap stays low and gaps remain small, with the MaxSAT formulation performing essentially the same as simpler counting approaches.

Now I'm organizing all these findings into a structured YAML format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07db033e-eaef-481f-b6b9-b755ee488976",
  "isSidechain": false,
  "requestId": "req_011Cb6YGuDJtUzvyrTtJ7gJp",
  "type": "assistant",
  "uuid": "6cf8ccad-5772-4141-893d-9e1772d13855",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "a7e65dd3-b494-43d7-ae29-482a1923e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8WtQXikLihmpqWLRPDFyQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12987,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15077,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15077,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12987
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

_source line 9 · 2026-05-16T16:15:18.602Z_

```yaml
tier: worst
narrative_guidance: >
  Activate D023 contingency. Expanded results confirm D012's +6.7pp was a small-sample artifact —
  FOLIO gap shrinks to ~+2pp on 204 questions, ProofWriter flat or slightly negative, combined gap
  ≤+1pp and non-significant (p>0.2). C0 pattern robustly replicates across 3 families and 2 reasoning
  architectures, but high C0 does NOT translate to SICA>SC. The paper pivots to: "Characterizing When
  Symbolic Consensus Methods Fail — and Why Trace Diversity Is Necessary But Not Sufficient." Primary
  contribution becomes operating regime characterization (Claim 2 intact). Claim 1 weakens to
  "interpretable tiebreaking" without accuracy claims. New analysis: constraint extraction quality is
  the missing second condition — noisy FOL and incorrect exclusions explain why diversity alone doesn't
  help. Target EMNLP Findings (primary) or AAAI 2027 Main (fallback with method improvements).

imagined_experiments:
  - name: sica_expanded_14b
    plan_id: exp-001
    description: "Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12, T=0.7"
    expected_results:
      n_total: 804
      n_folio: 204
      n_proofwriter: 600
      sica_accuracy_combined: 0.765
      sc_accuracy_combined: 0.762
      sica_sc_gap_combined_pp: 0.3
      bootstrap_p_combined: 0.38
      sica_accuracy_folio: 0.755
      sc_accuracy_folio: 0.735
      sica_sc_gap_folio_pp: 2.0
      bootstrap_p_folio: 0.14
      sica_accuracy_proofwriter: 0.769
      sc_accuracy_proofwriter: 0.773
      sica_sc_gap_proofwriter_pp: -0.4
      bootstrap_p_proofwriter: 0.62
      c0_multi_candidate_rate_combined: 0.38
      c0_folio: 0.42
      c0_proofwriter: 0.36
      c1_extraction_rate: 0.97
      total_constraints_unique: ~23000
      maxsat_exclusion_rate: 0.031
      wall_time_hours: ~13
      tiebreak_problems: ~45
      tiebreak_sica_wins: 26
      tiebreak_sica_win_rate: 0.58
    result_rationale: >
      D012's +6.7pp FOLIO gap was inflated by small-sample variance (30 questions, ~5 lucky tiebreaks).
      On 204 FOLIO questions the gap regresses toward the mean: more questions have clear SC majorities
      where SICA cannot intervene, and tiebreak cases (~20%) show only modest SICA advantage (~58% win
      rate vs 50% random). ProofWriter D5 is inherently harder for constraint extraction — its multi-hop
      chains produce FOL with nested quantifiers that the LLM-based extractor frequently mis-translates,
      leading to noisy constraints that cancel out or slightly hurt via incorrect exclusions. The combined
      gap (+0.3pp) is well within noise at p=0.38. C0 remains at ~38% for instruction-tuned 14B
      (genuine output diversity exists), confirming that diversity is necessary but not sufficient —
      constraint quality is the bottleneck preventing MaxSAT from exploiting that diversity.
    tables:
      - name: "T1 (Main Results — 14B rows)"
        content: |
          | Dataset     |   N | SC Acc | SICA Acc | Δpp  | p-val | C0    |
          |-------------|-----|--------|----------|------|-------|-------|
          | FOLIO       | 204 | 73.5%  | 75.5%   | +2.0 | 0.14  | 0.42  |
          | PW-D5       | 600 | 77.3%  | 76.9%   | −0.4 | 0.62  | 0.36  |
          | Combined    | 804 | 76.2%  | 76.5%   | +0.3 | 0.38  | 0.38  |
      - name: "T2 (Tiebreak Comparison — expanded)"
        content: |
          | Method           | Tie Wins | Tie Acc | Overall Δ vs SC-det |
          |------------------|----------|---------|---------------------|
          | SICA (MaxSAT)    | 26/45    | 57.8%  | +0.3pp              |
          | SC-random        | ~22/45   | ~50%   | +0.0pp              |
          | SC-deterministic | 20/45    | 44.4%  | baseline            |
    figures_description:
      - "F2 (C0 vs Gap Scatter): 14B-expanded point sits at (C0=0.38, gap=+0.3pp), far below the regression line implied by D012. FOLIO sub-point at (0.42, +2.0) still positive but weak. PW sub-point at (0.36, −0.4) negative. The scatter shows no clear positive correlation between C0 and gap — high C0 is necessary for any chance of improvement but does not guarantee it."
    analysis: >
      The key finding is that 804-question power kills the accuracy claim. FOLIO retains a positive
      trend (+2.0pp, p=0.14 — borderline) but PW drags the combined result to noise. The pivot
      insight: C0=38% means ~300 questions have multi-candidate votes, yet MaxSAT picks the right
      candidate only ~1pp more often than random among those. Constraint extraction error analysis
      becomes critical — expect ~15-20% of extracted FOL to be semantically incorrect, and exclusion
      rate (3.1%) is too conservative to matter. The paper must now argue that C0 *identifies* where
      symbolic methods could help, not that the current implementation *does* help.

  - name: sica_k_ablation_14b
    plan_id: exp-002
    description: "K sensitivity (K=6,8,12,16,20) on D012's 60 questions"
    expected_results:
      results_by_k:
        K6:
          sica_accuracy: 0.717
          sc_accuracy: 0.700
          gap_pp: 1.7
          c0: 0.383
          tiebreak_count: 8
          tiebreak_sica_wins: 5
        K8:
          sica_accuracy: 0.717
          sc_accuracy: 0.700
          gap_pp: 1.7
          c0: 0.450
          tiebreak_count: 6
          tiebreak_sica_wins: 4
        K12:
          sica_accuracy: 0.733
          sc_accuracy: 0.700
          gap_pp: 3.3
          c0: 0.533
          tiebreak_count: 5
          tiebreak_sica_wins: 4
        K16:
          sica_accuracy: 0.717
          sc_accuracy: 0.717
          gap_pp: 0.0
          c0: 0.533
          tiebreak_count: 3
          tiebreak_sica_wins: 2
        K20:
          sica_accuracy: 0.733
          sc_accuracy: 0.733
          gap_pp: 0.0
          c0: 0.550
          tiebreak_count: 2
          tiebreak_sica_wins: 1
      wall_time_hours: ~4.5
    result_rationale: >
      In worst tier, the K ablation reveals that SICA's gain is almost entirely mediated by tiebreaking,
      and tiebreak frequency drops sharply with higher K. At K=6, even splits (3-3) are common (~8/60),
      giving SICA chances to intervene. At K=12 (original), 5 ties remain and SICA wins most. But at
      K=16 and K=20, the law of large numbers kicks in — SC majorities solidify, ties become rare
      (2-3 problems), and the gap collapses to 0pp. C0 increases slightly with K (more samples → more
      chance of diverse answers) but this doesn't translate to accuracy because the additional diversity
      is in minority votes that SC correctly outvotes anyway. The pattern confirms SICA is a tiebreaker,
      not a systematic improver — at sufficiently high K, ties vanish and so does the gap.
    tables:
      - name: "T3 (K Sensitivity)"
        content: |
          | K  | SC Acc | SICA Acc | Δpp  | C0    | #Ties | Tie WR |
          |----|--------|----------|------|-------|-------|--------|
          | 6  | 70.0%  | 71.7%   | +1.7 | 0.383 | 8     | 62.5%  |
          | 8  | 70.0%  | 71.7%   | +1.7 | 0.450 | 6     | 66.7%  |
          | 12 | 70.0%  | 73.3%   | +3.3 | 0.533 | 5     | 80.0%  |
          | 16 | 71.7%  | 71.7%   | 0.0  | 0.533 | 3     | 66.7%  |
          | 20 | 73.3%  | 73.3%   | 0.0  | 0.550 | 2     | 50.0%  |
    figures_description:
      - "F4 (K Curve): Two-panel. Left: SICA and SC accuracy vs K — lines converge and overlap by K=16. Right: tie count vs K — exponential decay from 8 (K=6) to 2 (K=20). Visual proof that SICA benefit is purely a function of tie frequency, not systematic constraint exploitation."
    analysis: >
      This is actually a useful result for the worst-tier narrative: it cleanly demonstrates that
      SICA operates exclusively through tiebreaking. The paper reframes this as a principled finding —
      at what K does the tiebreak channel close? The K curve becomes evidence for the "necessary but
      not sufficient" story. SC accuracy itself improves with K (70% → 73.3%), confirming that more
      samples help SC directly. SICA's value-add is confined to the K<16 regime where ties are common.

  - name: tiebreak_baseline_analysis
    plan_id: exp-003
    description: "Compare SICA vs SC-random vs SC-deterministic on all available data (expanded)"
    expected_results:
      dataset: expanded_804
      sica_tiebreak_accuracy: 0.578
      sc_random_tiebreak_accuracy: 0.50
      sc_deterministic_tiebreak_accuracy: 0.444
      sica_overall_accuracy: 0.765
      sc_random_overall_accuracy: 0.763
      sc_deterministic_overall_accuracy: 0.762
      tiebreak_count: 45
      sica_unique_wins_vs_random: 4
      random_unique_wins_vs_sica: 3
    result_rationale: >
      On 804 questions, ~45 have tied SC votes. SICA resolves these at 57.8% (slightly better than
      random 50%) but the gap between SICA and SC-random on overall accuracy is only 0.2pp — within
      noise. The D012 result (80% tiebreak win rate on 5 ties) was a 5-trial coin flip that happened
      to land favorably. At 45 ties, regression to the mean is severe. The fundamental issue: MaxSAT
      constraint weighting has low signal-to-noise ratio because extracted FOL constraints are often
      semantically incorrect or trivially satisfied by all candidates. The "principled" advantage over
      random is real but tiny — maybe 8pp in tie accuracy, translating to <0.5pp in overall accuracy.
    tables: []
    figures_description:
      - "Bar chart: tiebreak resolution accuracy for SICA (57.8%), SC-random (50%), SC-deterministic (44.4%). Error bars from bootstrap show overlapping CIs between SICA and SC-random."
    analysis: >
      This result is the worst-tier's most damaging finding for Claim 1. The honest conclusion: SICA
      provides a slightly-better-than-random tiebreak, but the advantage is not statistically
      distinguishable from luck at N=45 ties. The paper must present this transparently and pivot to
      interpretability: "SICA provides an auditable, constraint-based reason for its tiebreak choice,
      even when the accuracy advantage is marginal."

  - name: sica_7b_scaling
    plan_id: exp-004
    description: "Qwen2.5-7B-Instruct on D012 60 questions, testing C0 scaling"
    expected_results:
      model: Qwen2.5-7B-Instruct
      n: 60
      sica_accuracy: 0.583
      sc_accuracy: 0.567
      gap_pp: 1.7
      bootstrap_p: 0.42
      c0_multi_candidate_rate: 0.65
      c1_extraction_rate: 0.92
      maxsat_exclusion_rate: 0.048
      tiebreak_count: 10
      tiebreak_sica_wins: 6
      folio_sica: 0.633
      folio_sc: 0.600
      proofwriter_sica: 0.533
      proofwriter_sc: 0.533
      wall_time_hours: ~1.8
    result_rationale: >
      7B is weaker → lower baseline accuracy (SC ~56.7% vs 14B's 70%) and higher C0 (65% vs 53.3%).
      This confirms the C0-as-uncertainty hypothesis: weaker models produce more diverse (less
      confident) outputs. However, in worst tier, higher C0 still doesn't translate to meaningful
      SICA gains (+1.7pp, p=0.42). Why: the 7B model generates even noisier FOL constraints than 14B.
      Its constraint extraction quality is substantially worse — more hallucinated predicates, incorrect
      logical structures, irrelevant constraints. So while there are more tiebreak opportunities (10 vs
      5 on 60 questions), SICA's tiebreak resolution accuracy is lower (~60%) because the signal in
      constraints degrades faster than the opportunity increases. The net effect is a small, non-
      significant gap. This is the crux of the worst-tier insight: C0 (diversity) increases with
      weakness, but constraint quality decreases — these forces cancel.
    tables:
      - name: "T1 (Main Results — 7B row)"
        content: |
          | Model          | Dataset  |  N | SC Acc | SICA Acc | Δpp  | p    | C0   |
          |----------------|----------|----|--------|----------|------|------|------|
          | Qwen2.5-7B-Ins | Combined | 60 | 56.7%  | 58.3%   | +1.7 | 0.42 | 0.65 |
          | Qwen2.5-7B-Ins | FOLIO    | 30 | 60.0%  | 63.3%   | +3.3 | 0.35 | 0.60 |
          | Qwen2.5-7B-Ins | PW-D5    | 30 | 53.3%  | 53.3%   | 0.0  | 0.50 | 0.70 |
    figures_description:
      - "F2 addition: 7B point at (C0=0.65, gap=+1.7pp). Higher C0 than 14B but gap still small. Visually reinforces that C0 is necessary but not sufficient."
    analysis: >
      7B validates the C0 scaling direction (weaker → higher C0) which is good for Claim 2. But the
      non-significant gap despite C0=65% is the worst-tier's central negative result. New analysis
      opportunity: plot constraint extraction quality (measured by semantic coherence or predicate
      consistency) against model size. Hypothesis: quality drops faster than diversity rises, creating
      a "diversity-quality tradeoff" that explains the null result. This becomes a key figure in the
      reframed analysis paper.

  - name: qwq_32b_operating_regime
    plan_id: exp-005
    description: "QwQ-32B data formatted for Operating Regime Analysis (existing data, no new GPU)"
    expected_results:
      model: QwQ-32B
      data_sources:
        - sica_aime30_v3
        - sica_proofwriter30_v2
        - sica_folio30
      c0_combined: 0.036
      c0_aime: 0.0
      c0_proofwriter: 0.1875
      c0_folio: 0.0
      sica_sc_gap_pp: 0.0
      n_total: 48
      regime_classification: converged
      sica_degenerate: true
    result_rationale: >
      Existing data. QwQ-32B's extended thinking produces near-deterministic outputs — the reasoning
      chain is so dominant that temperature sampling barely perturbs the final answer. C0=3.6% means
      SICA ≡ SC in >96% of cases. This is the clean negative pole of the operating regime: when the
      model is sufficiently confident (reasoning models on any task), symbolic consensus has nothing to
      aggregate. In worst tier, this data point is even more valuable — it's the strongest evidence for
      Claim 2 (operating regime exists) and survives intact because it's a structural result, not a
      quantitative one. The only nuance: PW shows C0=18.75% (3/16 problems) but on too few questions
      to matter, and even there SICA=SC.
    tables:
      - name: "T1 (Main Results — QwQ row)"
        content: |
          | Model   | Dataset  |  N | SC Acc | SICA Acc | Δpp | C0    | Regime    |
          |---------|----------|----|--------|----------|-----|-------|-----------|
          | QwQ-32B | AIME     | 22 | 72.7%  | 72.7%   | 0.0 | 0.00  | Converged |
          | QwQ-32B | PW-D5    | 16 | —      | —        | 0.0 | 0.188 | Converged |
          | QwQ-32B | FOLIO    | 10 | —      | —        | 0.0 | 0.00  | Converged |
          | QwQ-32B | Combined | 48 | —      | —        | 0.0 | 0.036 | Converged |
    figures_description:
      - "F2 addition: QwQ-32B cluster at (C0≈0.04, gap=0.0). Anchor point at bottom-left corner, clearly separated from instruction model cluster."
      - "F3 (Operating Regime Heatmap): QwQ row shows uniformly cold (blue) cells across all domains."
    analysis: >
      This is the cleanest data in the paper and survives all tiers. In worst tier, it becomes even
      more prominent — the operating regime characterization is now the primary contribution, and QwQ
      is the clean negative anchor. Frame as: "Reasoning models represent the converged regime where
      symbolic consensus is structurally redundant."

  - name: c0_diagnostic_validation
    plan_id: exp-006
    description: "C0 vs SICA-SC gap analysis across all models and K values (CPU-only)"
    expected_results:
      data_points:
        - model: Qwen2.5-14B-Instruct
          K: 12
          dataset: expanded_combined
          c0: 0.38
          gap_pp: 0.3
        - model: Qwen2.5-14B-Instruct
          K: 6
          dataset: d012_60
          c0: 0.383
          gap_pp: 1.7
        - model: Qwen2.5-14B-Instruct
          K: 16
          dataset: d012_60
          c0: 0.533
          gap_pp: 0.0
        - model: Qwen2.5-14B-Instruct
          K: 20
          dataset: d012_60
          c0: 0.550
          gap_pp: 0.0
        - model: Qwen2.5-7B-Instruct
          K: 12
          dataset: d012_60
          c0: 0.65
          gap_pp: 1.7
        - model: QwQ-32B
          K: 12
          dataset: combined_48
          c0: 0.036
          gap_pp: 0.0
        - model: Qwen2.5-72B-AWQ
          K: 12
          dataset: d012_60
          c0: 0.18
          gap_pp: 0.0
        - model: Mistral-7B-v0.3
          K: 12
          dataset: d012_60
          c0: 0.35
          gap_pp: 0.5
        - model: LLaMA-3.1-8B
          K: 12
          dataset: d012_60
          c0: 0.30
          gap_pp: 1.0
        - model: DeepSeek-R1-LLaMA-8B
          K: 12
          dataset: d012_60
          c0: 0.042
          gap_pp: 0.0
      pearson_r_c0_gap: 0.28
      pearson_p: 0.43
      binary_threshold_analysis:
        c0_threshold: 0.20
        above_threshold_mean_gap_pp: 0.7
        below_threshold_mean_gap_pp: 0.0
        above_threshold_positive_rate: 0.57
    result_rationale: >
      In worst tier, C0 shows a weak positive correlation with gap (r=0.28, p=0.43) — directionally
      correct but far from significant. The scatter plot reveals two clusters: (1) reasoning models at
      bottom-left (C0<5%, gap=0), (2) instruction models spread across C0=18-65% with gaps scattered
      between -0.4pp and +2.0pp. Within the instruction cluster, there is NO clear monotonic
      relationship — 7B has highest C0 (0.65) but only +1.7pp, while 14B-expanded has C0=0.38 but
      only +0.3pp. The binary diagnostic (C0>20% → "SICA might help") has a 57% positive rate —
      barely better than a coin flip for predicting actual gains. C0 reliably identifies the converged
      regime (C0<5% → gap=0, 100% accurate) but cannot predict magnitude in the diverse regime. This
      downgrades Claim 3 from "continuous predictor" to "binary necessary-condition diagnostic."
    tables:
      - name: "C0 Diagnostic Summary"
        content: |
          | Regime       | C0 Range | N models | Mean Gap | Gap > 0 Rate |
          |--------------|----------|----------|----------|--------------|
          | Converged    | < 5%     | 2        | 0.0pp    | 0%           |
          | Transitional | 5–20%   | 1        | 0.0pp    | 0%           |
          | Diverse      | > 20%    | 7        | 0.7pp    | 57%          |
    figures_description:
      - "F2 (Hero Figure — C0 vs Gap Scatter): 10 data points. Two clear clusters: reasoning models anchored at (C0<5%, gap=0) and instruction models scattered broadly at (C0=18-65%, gap=-0.4 to +2.0). No regression line shown (r=0.28 is misleading). Instead, shaded regions mark 'Converged' (C0<5%), 'Transitional' (5-20%), 'Diverse' (>20%). Key visual: the diverse region has both positive and negative gaps — C0 is necessary but not sufficient."
    analysis: >
      The C0 diagnostic validation is mixed. The good news: C0 perfectly identifies where SICA is
      structurally useless (converged regime). The bad news: within the diverse regime, C0 doesn't
      predict whether SICA helps. The reframed claim: "C0 as a necessary-condition diagnostic — use it
      to avoid wasting compute on symbolic consensus when the model is already converged, but do not
      use it to promise accuracy gains." New analysis for the paper: add a second axis — constraint
      extraction quality — and show that the interaction of C0 × quality predicts gap better than C0
      alone.

  - name: sica_72b_awq
    plan_id: exp-007
    description: "Qwen2.5-72B-Instruct AWQ 4-bit on D012 60 questions"
    expected_results:
      model: Qwen2.5-72B-Instruct-AWQ
      n: 60
      sica_accuracy: 0.817
      sc_accuracy: 0.817
      gap_pp: 0.0
      bootstrap_p: 0.50
      c0_multi_candidate_rate: 0.18
      c1_extraction_rate: 0.98
      tiebreak_count: 1
      folio_sica: 0.867
      folio_sc: 0.867
      proofwriter_sica: 0.767
      proofwriter_sc: 0.767
      wall_time_hours: ~3.5
    result_rationale: >
      72B is near the ceiling of instruction models — high baseline accuracy (~81.7%) and low C0
      (18%). The model is confident enough that most questions converge to a single candidate across
      K=12 samples, leaving at most 1 tie. 72B sits in the transitional zone between instruction and
      reasoning model behavior: not fully converged like QwQ but far less diverse than 7B or 14B. In
      worst tier, 72B shows exactly 0pp gap — it's strong enough that its SC answers are already
      correct, and the rare disagreements are on genuinely hard questions where constraint extraction
      is unreliable. This creates the clean within-family scaling story: 7B (C0=65%, gap≈+1.7) → 14B
      (C0=38%, gap≈+0.3) → 72B (C0=18%, gap=0.0), confirming that SICA's opportunity window closes
      as model capability increases.
    tables:
      - name: "T1 (Main Results — 72B row)"
        content: |
          | Model              | Dataset  |  N | SC Acc | SICA Acc | Δpp | C0   |
          |--------------------|----------|----|--------|----------|-----|------|
          | Qwen2.5-72B-AWQ   | Combined | 60 | 81.7%  | 81.7%   | 0.0 | 0.18 |
          | Qwen2.5-72B-AWQ   | FOLIO    | 30 | 86.7%  | 86.7%   | 0.0 | 0.13 |
          | Qwen2.5-72B-AWQ   | PW-D5    | 30 | 76.7%  | 76.7%   | 0.0 | 0.23 |
    figures_description:
      - "F2 addition: 72B at (C0=0.18, gap=0.0). Falls in the transitional zone. Within-Qwen trajectory: 7B→14B→72B traces a path from upper-right toward lower-left, showing C0 decreasing with scale and gap collapsing."
    analysis: >
      72B provides the crucial middle data point for within-family scaling. In worst tier, the
      monotonic C0 decrease (65%→38%→18%) with model size confirms that C0 reflects effective model
      confidence. But the gap trajectory (1.7→0.3→0.0) shows diminishing returns are severe — by 72B,
      SICA is completely redundant. This supports the reframed narrative: SICA is a technique for
      small-to-medium instruction models where output diversity exists but baseline accuracy is low
      enough for tiebreaks to matter. As models improve, SICA's operating window closes from both
      sides (fewer ties AND higher baseline).

  - name: constraint_quality_case_studies
    plan_id: exp-008
    description: "Qualitative analysis of extracted constraints on 5-10 representative questions"
    expected_results:
      n_analyzed: 8
      semantic_correctness_rate: 0.62
      error_categories:
        hallucinated_predicates: 0.15
        wrong_quantifier_scope: 0.10
        missing_negation: 0.08
        irrelevant_constraint: 0.05
      exclusion_correctness:
        correctly_excluded: 0.55
        incorrectly_excluded: 0.30
        should_have_excluded: 0.15
      sica_correct_and_constraints_correct: 3
      sica_correct_but_constraints_noisy: 1
      sica_wrong_and_constraints_wrong: 2
      sica_wrong_despite_constraints_ok: 2
    result_rationale: >
      In worst tier, the case study analysis reveals the smoking gun: constraint extraction quality is
      mediocre (~62% semantically correct). The LLM-based FOL extractor hallucinates predicates that
      don't appear in the original reasoning trace (~15%), mishandles quantifier scope (~10%), and
      occasionally drops negations (~8%). MaxSAT operates faithfully on these constraints, but
      garbage-in-garbage-out: when 38% of constraints are noisy, the satisfiability signal is diluted.
      Exclusion analysis is particularly damning — 30% of excluded constraints were actually correct
      (false exclusion), meaning MaxSAT is throwing away valid evidence. Among SICA's wrong answers,
      2/4 had reasonable constraints but MaxSAT weighted the wrong candidate due to accumulation of
      small errors. This is the core explanation for why high C0 doesn't translate to gains.
    tables: []
    figures_description:
      - "Case study figure: side-by-side comparison of a SICA-correct and SICA-wrong example. Left: correct case shows clean FOL extraction, appropriate exclusion, MaxSAT selects right answer. Right: wrong case shows hallucinated predicate in 2 constraints, incorrect exclusion of a valid constraint, MaxSAT tipped toward wrong answer."
    analysis: >
      This is the most important analysis for the reframed paper. The constraint quality breakdown
      provides the "missing second condition" for the pivot narrative: trace diversity (C0) enables
      MaxSAT to consider alternatives, but constraint extraction fidelity determines whether MaxSAT
      can discriminate correctly. The 62% semantic correctness rate on 14B suggests that current LLM
      FOL extraction is insufficient for reliable symbolic consensus. Future work direction: improve
      constraint extraction (fine-tuned extractor, multi-round verification) before expecting SICA
      to deliver systematic gains.

  - name: overhead_analysis
    plan_id: exp-009
    description: "Wall-time breakdown per question: generation, constraint extraction, MaxSAT solving"
    expected_results:
      mean_total_time_per_question_s: 58.2
      breakdown:
        generation_s: 42.5
        generation_pct: 0.730
        constraint_extraction_s: 14.1
        constraint_extraction_pct: 0.242
        maxsat_solving_s: 0.8
        maxsat_solving_pct: 0.014
        overhead_other_s: 0.8
        overhead_other_pct: 0.014
      sica_overhead_vs_sc_pct: 0.27
      sc_only_time_per_question_s: 42.5
      sica_marginal_cost_s: 15.7
      maxsat_p99_time_s: 3.2
      constraint_extraction_gpu_required: true
    result_rationale: >
      Generation dominates (73% of time) because K=12 traces must be generated regardless for SC.
      SICA's marginal overhead is constraint extraction (24.2%) + MaxSAT (1.4%) = ~27% wall-time
      increase. Constraint extraction requires a second LLM call per trace (extracting FOL), making
      it GPU-bound. MaxSAT solving is negligible (<1s) since problems have ~200-300 constraints with
      3-5 candidates. In worst tier, this overhead is particularly unflattering: 27% more compute for
      +0.3pp combined gain is a terrible cost-benefit ratio. Even the FOLIO-only case (+2.0pp for
      27% overhead) is questionable. The paper must present this honestly — SICA overhead is moderate
      in absolute terms but cannot be justified by the accuracy gains in this tier.
    tables:
      - name: "T4 (Overhead Analysis)"
        content: |
          | Component               | Mean (s) | % Total | GPU Required |
          |-------------------------|----------|---------|--------------|
          | Trace Generation (K=12) | 42.5     | 73.0%   | Yes          |
          | Constraint Extraction   | 14.1     | 24.2%   | Yes          |
          | MaxSAT Solving          | 0.8      | 1.4%    | No           |
          | Other (I/O, parsing)    | 0.8      | 1.4%    | No           |
          | **Total SICA**          | **58.2** | 100%    |              |
          | SC-only baseline        | 42.5     | —       | Yes          |
          | **SICA marginal cost**  | **15.7** | +27%    |              |
    figures_description:
      - "Stacked bar chart: SICA vs SC wall-time per question. SC bar: 42.5s (generation only). SICA bar: 42.5s generation + 14.1s extraction + 0.8s MaxSAT. Visual emphasis on the marginal 27% cost."
    analysis: >
      The overhead story is manageable for an analysis paper — the 27% overhead is presented as a
      characterization datum, not justified by accuracy. The reframe: "SICA's compute cost is
      dominated by constraint extraction, not MaxSAT. Future efficiency gains should target extraction
      (batching, caching, distilled extractor) rather than solver optimization." Note: MaxSAT is
      trivially fast, which at least validates the solver-side engineering.

  - name: sica_mistral_7b
    plan_id: exp-010
    description: "Mistral-7B-Instruct-v0.3 on D012 60 questions, cross-family validation"
    expected_results:
      model: Mistral-7B-Instruct-v0.3
      n: 60
      sica_accuracy: 0.517
      sc_accuracy: 0.512
      gap_pp: 0.5
      bootstrap_p: 0.48
      c0_multi_candidate_rate: 0.35
      c1_extraction_rate: 0.88
      maxsat_exclusion_rate: 0.042
      tiebreak_count: 6
      tiebreak_sica_wins: 3
      folio_sica: 0.567
      folio_sc: 0.533
      folio_gap_pp: 3.3
      proofwriter_sica: 0.467
      proofwriter_sc: 0.490
      proofwriter_gap_pp: -2.3
      wall_time_hours: ~1.2
    result_rationale: >
      Mistral-7B is weaker than Qwen-14B on logic tasks (baseline ~51%), producing moderate C0
      (35%). In worst tier, the gap is negligible (+0.5pp, p=0.48). Cross-family C0 pattern holds
      (instruction model → moderate-to-high C0), validating Claim 2's generality. But the gap pattern
      also generalizes in the wrong direction: high C0 + poor constraint extraction = no gain. Mistral
      7B's instruction following for FOL extraction is notably weaker than Qwen — extraction rate
      drops to 88% (vs 97% for Qwen-14B), and extracted constraints are lower quality. The FOLIO/PW
      split shows FOLIO slightly positive (+3.3pp) but PW negative (-2.3pp), mirroring the 14B
      pattern at lower absolute levels. This confirms the domain effect is robust across families.
    tables:
      - name: "T1 (Main Results — Mistral row)"
        content: |
          | Model              | Dataset  |  N | SC Acc | SICA Acc | Δpp  | p    | C0   |
          |--------------------|----------|----|--------|----------|------|------|------|
          | Mistral-7B-v0.3    | Combined | 60 | 51.2%  | 51.7%   | +0.5 | 0.48 | 0.35 |
          | Mistral-7B-v0.3    | FOLIO    | 30 | 53.3%  | 56.7%   | +3.3 | 0.30 | 0.40 |
          | Mistral-7B-v0.3    | PW-D5    | 30 | 49.0%  | 46.7%   | −2.3 | 0.72 | 0.30 |
    figures_description:
      - "F2 addition: Mistral-7B at (C0=0.35, gap=+0.5). Clusters with other instruction models in the diverse regime but with near-zero gap."
    analysis: >
      Mistral validates the cross-family C0 pattern but reinforces the worst-tier story: diversity
      alone is insufficient. The extraction rate drop (88% vs 97%) is a concrete datapoint for the
      constraint-quality argument. The FOLIO/PW split replicating across families is actually a
      useful finding — it suggests domain formality (FOLIO's cleaner logical structure) is a second
      factor beyond C0. This gives the paper a 2D characterization: C0 × domain_formality.

  - name: sica_llama_8b
    plan_id: exp-011
    description: "LLaMA-3.1-8B-Instruct on D012 60 questions, third family for cross-family validation"
    expected_results:
      model: LLaMA-3.1-8B-Instruct
      n: 60
      sica_accuracy: 0.500
      sc_accuracy: 0.490
      gap_pp: 1.0
      bootstrap_p: 0.44
      c0_multi_candidate_rate: 0.30
      c1_extraction_rate: 0.85
      maxsat_exclusion_rate: 0.038
      tiebreak_count: 5
      tiebreak_sica_wins: 3
      folio_sica: 0.533
      folio_sc: 0.500
      folio_gap_pp: 3.3
      proofwriter_sica: 0.467
      proofwriter_sc: 0.480
      proofwriter_gap_pp: -1.3
      wall_time_hours: ~1.3
    result_rationale: >
      LLaMA-8B is the weakest instruction model tested, with baseline ~49% and C0=30%. The gap
      (+1.0pp) is directionally positive but non-significant (p=0.44). LLaMA's FOL extraction quality
      is the lowest of the three families (extraction rate 85%) — its instruction-following for
      structured output is weaker than Qwen or Mistral. C0=30% is lower than expected for a weak
      model, likely because LLaMA-8B's errors are more "confused" than "diverse" — it often produces
      the same wrong answer repeatedly rather than exploring alternatives. The FOLIO/PW split again
      holds: FOLIO positive, PW negative. Three-family coverage with consistent C0 pattern but
      consistently null accuracy gap is the strongest possible evidence for the "necessary but not
      sufficient" thesis.
    tables:
      - name: "T1 (Main Results — LLaMA row)"
        content: |
          | Model              | Dataset  |  N | SC Acc | SICA Acc | Δpp  | p    | C0   |
          |--------------------|----------|----|--------|----------|------|------|------|
          | LLaMA-3.1-8B-Ins   | Combined | 60 | 49.0%  | 50.0%   | +1.0 | 0.44 | 0.30 |
          | LLaMA-3.1-8B-Ins   | FOLIO    | 30 | 50.0%  | 53.3%   | +3.3 | 0.32 | 0.37 |
          | LLaMA-3.1-8B-Ins   | PW-D5    | 30 | 48.0%  | 46.7%   | −1.3 | 0.65 | 0.23 |
    figures_description:
      - "F2 addition: LLaMA-8B at (C0=0.30, gap=+1.0). Three-family instruction cluster now visible in scatter: Qwen-14B, Mistral-7B, LLaMA-8B all in diverse regime (C0=0.30-0.38) with gaps 0.3-1.0pp."
    analysis: >
      LLaMA completes the 3-family validation for Claim 2. The lower C0 (0.30 vs Mistral's 0.35 and
      Qwen-14B's 0.38) is an interesting nuance — model family affects C0 at similar parameter counts.
      The extraction rate hierarchy (Qwen 97% > Mistral 88% > LLaMA 85%) provides direct evidence for
      the constraint-quality hypothesis. Combined with Mistral and Qwen data, the paper can argue that
      both output diversity (C0) and extraction fidelity are needed, and current systems satisfy only
      the first condition.

  - name: gsm8k_pilot_14b
    plan_id: exp-012
    description: "Qwen2.5-14B on GSM8K 30-question pilot, cross-domain C0 test"
    expected_results:
      model: Qwen2.5-14B-Instruct
      dataset: GSM8K
      n: 30
      sica_accuracy: 0.900
      sc_accuracy: 0.900
      gap_pp: 0.0
      c0_multi_candidate_rate: 0.10
      c1_extraction_rate: 0.93
      tiebreak_count: 0
      sc_baseline_accuracy: 0.900
      unique_answers_per_problem_mean: 1.1
      wall_time_hours: ~0.8
    result_rationale: >
      14B is too strong for GSM8K (SC baseline 90%). The model converges to the correct answer in 11
      of 12 traces on most problems, producing very low C0 (10%). This is expected: GSM8K is an easy
      benchmark for 14B-class instruction models. The open-ended answer space (integers) might have
      produced diversity, but the problems are computationally straightforward enough that the model
      is confident. C0=10% is actually lower than on FOLIO (42%) or PW (36%), confirming that C0
      reflects task-relative difficulty, not answer-space structure. In worst tier, this is a clean
      negative result that strengthens the C0 story: when the model is confident (regardless of domain
      or answer space), C0 is low and SICA is redundant. The intellectual contribution is distinguishing
      "C0 reflects confidence, not answer-space cardinality."
    tables:
      - name: "Cross-domain C0 Comparison"
        content: |
          | Domain | Answer Space | 14B SC Acc | 14B C0 | SICA Δpp |
          |--------|-------------|------------|--------|----------|
          | FOLIO  | 3-class NLI | 73.5%      | 0.42   | +2.0     |
          | PW-D5  | 3-class NLI | 77.3%      | 0.36   | −0.4     |
          | GSM8K  | Open integer| 90.0%      | 0.10   | 0.0      |
    figures_description:
      - "F2 addition: GSM8K point at (C0=0.10, gap=0.0). Falls in transitional-to-converged zone despite open answer space. Undermines the 'restricted answer space drives C0' hypothesis."
    analysis: >
      GSM8K pilot provides a clean cross-domain datapoint. In worst tier, it's especially useful
      because it refutes the reviewer concern that C0 is an artifact of restricted answer spaces
      (3-class NLI). C0 is low on GSM8K not because answers can't be diverse, but because the model
      is confident. This is a genuine insight for the analysis paper: C0 as a confidence proxy rather
      than an answer-space artifact.

  - name: constraint_ablation
    plan_id: exp-013
    description: "CPU-only ablation: SICA-MaxSAT vs count-only vs random-weight on expanded data"
    expected_results:
      dataset: expanded_804
      methods:
        maxsat_full:
          accuracy: 0.765
          gap_vs_sc_pp: 0.3
          tiebreak_win_rate: 0.578
        count_only:
          accuracy: 0.764
          gap_vs_sc_pp: 0.2
          tiebreak_win_rate: 0.556
        random_weight:
          accuracy: 0.763
          gap_vs_sc_pp: 0.1
          tiebreak_win_rate: 0.533
        sc_deterministic:
          accuracy: 0.762
          gap_vs_sc_pp: 0.0
          tiebreak_win_rate: 0.444
      maxsat_vs_count_only_pp: 0.1
      maxsat_vs_random_weight_pp: 0.2
      pairwise_p_maxsat_vs_count: 0.72
    result_rationale: >
      In worst tier, MaxSAT ≈ count-only (Δ=0.1pp, p=0.72). The satisfiability checking that makes
      MaxSAT "principled" adds almost nothing over simply counting how many constraints support each
      answer. Why: with ~62% semantic correctness in extracted constraints, the satisfiability signal
      is too noisy to differentiate from counting. Both methods are marginally better than random
      weights (which is marginally better than deterministic SC), forming a weak monotonic ordering
      that fails significance at every step. The total spread from worst (SC-deterministic) to best
      (MaxSAT) is only 0.3pp. This is the worst-tier's most damaging result for the "MaxSAT is
      essential" sub-claim — the solver's satisfiability reasoning is being drowned by noise from
      upstream constraint extraction errors.
    tables:
      - name: "Constraint Ablation"
        content: |
          | Method          | Accuracy | Δ vs SC | Tie WR | Δ vs MaxSAT |
          |-----------------|----------|---------|--------|-------------|
          | SICA-MaxSAT     | 76.5%    | +0.3pp  | 57.8%  | —           |
          | SICA-Count-Only | 76.4%    | +0.2pp  | 55.6%  | −0.1pp      |
          | SICA-Random-Wt  | 76.3%    | +0.1pp  | 53.3%  | −0.2pp      |
          | SC-Deterministic| 76.2%    | baseline| 44.4%  | −0.3pp      |
    figures_description:
      - "Bar chart: accuracy by method, all bars within 0.3pp. Error bars heavily overlapping. Visual message: MaxSAT adds no statistically detectable value over simpler alternatives."
    analysis: >
      The ablation is devastating for the "MaxSAT is necessary" argument. The paper must reframe:
      "Constraint-based approaches provide a monotonic improvement gradient from random → counting →
      satisfiability, but the magnitude is governed by constraint quality. With current extraction
      fidelity (~62%), the satisfiability signal is below the noise floor." This motivates future work
      on extraction quality rather than solver sophistication. The positive spin: the monotonic
      ordering is at least directionally correct, suggesting that with better constraints, MaxSAT
      could differentiate itself.

  - name: sica_deepseek_r1_llama_8b
    plan_id: exp-014
    description: "DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions, second reasoning architecture"
    expected_results:
      model: DeepSeek-R1-Distill-LLaMA-8B
      n: 60
      sica_accuracy: 0.650
      sc_accuracy: 0.650
      gap_pp: 0.0
      bootstrap_p: 0.50
      c0_multi_candidate_rate: 0.042
      c1_extraction_rate: 0.95
      maxsat_exclusion_rate: 0.025
      tiebreak_count: 0
      folio_sica: 0.700
      folio_sc: 0.700
      proofwriter_sica: 0.600
      proofwriter_sc: 0.600
      wall_time_hours: ~1.8
    result_rationale: >
      DeepSeek-R1-Distill-LLaMA-8B is a reasoning-distilled model on LLaMA architecture, eliminating
      the "Qwen architecture" confound from QwQ-32B. Despite being only 8B parameters (much weaker
      baseline than QwQ-32B's 72.7%), it still shows near-zero C0 (4.2%) because the reasoning
      distillation process produces deterministic chain-of-thought behavior. The model "thinks through"
      each problem systematically, converging to the same answer across samples. C0=4.2% with zero
      tiebreaks means SICA ≡ SC structurally, mirroring QwQ-32B. This validates the key claim:
      reasoning-model convergence is a property of the training methodology (RL/distillation for
      extended reasoning), not model size or architecture family. A 8B reasoning model converges as
      strongly as a 32B one. This is the second clean anchor point for the converged regime,
      eliminating both the architecture and scale confounds.
    tables:
      - name: "T1 (Main Results — DeepSeek-R1 row)"
        content: |
          | Model                    | Dataset  |  N | SC Acc | SICA Acc | Δpp | C0    | Regime    |
          |--------------------------|----------|----|--------|----------|-----|-------|-----------|
          | DS-R1-Distill-LLaMA-8B   | Combined | 60 | 65.0%  | 65.0%   | 0.0 | 0.042 | Converged |
          | DS-R1-Distill-LLaMA-8B   | FOLIO    | 30 | 70.0%  | 70.0%   | 0.0 | 0.033 | Converged |
          | DS-R1-Distill-LLaMA-8B   | PW-D5    | 30 | 60.0%  | 60.0%   | 0.0 | 0.050 | Converged |
    figures_description:
      - "F2 addition: DeepSeek-R1 at (C0=0.042, gap=0.0). Clusters tightly with QwQ-32B at bottom-left despite different architecture (LLaMA vs Qwen) and different scale (8B vs 32B). Strong visual evidence that reasoning training, not architecture or scale, drives convergence."
      - "F3 (Heatmap): DeepSeek-R1 row matches QwQ pattern — uniformly cold across all domains."
    analysis: >
      DeepSeek-R1 is the cleanest control experiment in the paper. It isolates training methodology
      (reasoning distillation) as the causal factor for convergence, separating it from architecture
      (LLaMA ≠ Qwen) and scale (8B ≠ 32B). Combined with LLaMA-3.1-8B-Instruct (same architecture,
      C0=30%, instruction-tuned), this creates a perfect minimal pair: same architecture, same scale,
      different training → dramatically different C0. This is the strongest evidence for "C0 reflects
      training methodology, not model family or size" and survives intact in worst tier because it's
      a structural finding.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cf8ccad-5772-4141-893d-9e1772d13855",
  "isSidechain": false,
  "requestId": "req_011Cb6YGuDJtUzvyrTtJ7gJp",
  "type": "assistant",
  "uuid": "582110e5-a91d-4f5a-9b8d-35171895b268",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "a7e65dd3-b494-43d7-ae29-482a1923e8f3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U8WtQXikLihmpqWLRPDFyQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12987,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15077,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12987,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15077,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 12987,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12987
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Expanded results show SICA ≈ SC; gains vanish with scale; pivot to analysis/characterization paper 核心假设：[\"FOLIO gap shrinks to ≤+2pp on 204 questions (D01…",
  "leafUuid": "582110e5-a91d-4f5a-9b8d-35171895b268",
  "sessionId": "a7e65dd3-b494-43d7-ae29-482a1923e8f3"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing when symbolic consensus fails with trace diversity",
  "sessionId": "a7e65dd3-b494-43d7-ae29-482a1923e8f3"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Expanded results show SICA ≈ SC; gains vanish with scale; pivot to analysis/characterization paper 核心假设：[\"FOLIO gap shrinks to ≤+2pp on 204 questions (D01…",
  "leafUuid": "582110e5-a91d-4f5a-9b8d-35171895b268",
  "sessionId": "a7e65dd3-b494-43d7-ae29-482a1923e8f3"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing when symbolic consensus fails with trace diversity",
  "sessionId": "a7e65dd3-b494-43d7-ae29-482a1923e8f3"
}
```

---
