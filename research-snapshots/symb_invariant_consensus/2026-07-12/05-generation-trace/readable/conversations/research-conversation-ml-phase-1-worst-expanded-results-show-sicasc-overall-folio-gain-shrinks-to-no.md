# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Expanded results show SICA≈SC overall; FOLIO gain shrinks to noise at scale

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/9ab0fddf-13bd-4258-a788-5a3c235fb9c5.jsonl`
- **Structured JSON:** [`114a1ef669561b81ba15.json`](../../sessions/11/114a1ef669561b81ba15.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T12:51:27.776Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T12:51:27.776Z",
  "sessionId": "9ab0fddf-13bd-4258-a788-5a3c235fb9c5",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Expanded results show SICA≈SC overall; FOLIO gain shrinks to noise at scale; D023 contingency triggered — must pivot to analysis paper\n核心假设：['FOLIO gap ≤+2pp at 204-question scale, p>0.20', 'Combined gap ≤+0.5pp (effectively zero)', 'Cross-family C0 pattern holds (C0>20% for instruction models) BUT high C0 does not reliably translate to SICA>SC', 'MaxSAT ≈ count-only (no satisfiability value)', 'Tiebreak win rate 50-60% (barely above random on expanded set)', 'Core failure: constraint extraction quality insufficient to consistently beat voting even when traces diverge']\n关键指标范围：{'folio_gap_pp': [-1.0, 2.0], 'combined_gap_pp': [-1.0, 0.5], 'bootstrap_p_folio': [0.2, 0.5], 'bootstrap_p_combined': [0.35, 0.6], 'c0_14b_expanded': [0.3, 0.5], 'c0_mistral_7b': [0.15, 0.4], 'c0_llama_8b': [0.15, 0.4], 'c0_deepseek_r1': [0.0, 0.08], 'tiebreak_win_rate': [0.45, 0.6], 'maxsat_vs_countonly_delta_pp': [-1.0, 0.5], 'c0_7b': [0.4, 0.65], 'c0_72b': [0.2, 0.45]}\n叙事方向：D023 activated. All 3 original claims abandoned as accuracy claims. Paper pivots to: 'Why Doesn't Symbolic Consensus Improve LLM Reasoning? A Diagnostic Study.' New contribution structure: (1) C0 as a reliable zero-cost indicator of output diversity across model families — characterizes WHEN models disagree, not IF symbolic methods help; (2) Negative result on constraint-based aggregation — identifies failure modes (extraction noise, shallow constraints that don't capture deep reasoning errors); (3) Taxonomy of reasoning model vs instruction model behavior under sampling — reasoning models are structurally self-consistent regardless of temperature/K. Supplement with constraint-quality-vs-delta correlation analysis (CPU-only). Frame QwQ/DeepSeek convergence as novel finding about reasoning model internals. Target: EMNLP Findings (50-60%) with AAAI 2027 Main as fallback if reviewers want more models.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Fallback: AAAI 2027 (Aug 1)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条)\n1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).\n2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is governed by trace diversity (C0), which reflects effective output diversity — SICA adds value when C0>20% (diverse outputs, disagreement to resolve) but degenerates to SC when C0<5% (converged outputs, no disagreement). C0 empirically correlates with task-relative model confidence: instruction models show high C0 on challenging tasks, reasoning models show low C0 universally. Validated across 3 model families (Qwen, Mistral, LLaMA) and 2 reasoning architectures (QwQ, DeepSeek-R1). [Note: \"C0 → epistemic uncertainty\" connection reserved for Discussion, not formal claim — reviewer risk of terminology abuse per UQ community standards.]\n3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.\n\n## Core Insight\nSymbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that trace diversity (C0) — reflecting task-relative model confidence rather than model family or task domain alone — determines the operating regime. This transforms SICA from \"yet another ensemble method\" into \"a method with formally characterizable applicability boundaries,\" validated across 3 model families and multiple reasoning domains.\n\n## Story Spine\n- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.\n- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.\n- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75%+ win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) — a zero-cost diagnostic reflecting effective output diversity — and validate across 3 model families (Qwen, Mistral, LLaMA), 2 reasoning architectures (QwQ, DeepSeek-R1), and multiple domains (logic, math).\n- **Headline result template**: \"On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → exp-001: Expand to 804 questions for statistical power\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K sensitivity; exp-009: overhead analysis (P1); exp-013: constraint ablation (MaxSAT vs count-only vs random-weight)\n3. **\"Only Qwen models — family-specific artifact?\"** → exp-010: Mistral-7B + exp-011: LLaMA-8B (3-family validation)\n4. **\"Only one reasoning model\"** → exp-014: DeepSeek-R1-Distill-7B (second reasoning architecture)\n5. **\"Only logic domain — restricted answer space\"** → exp-012: GSM8K pilot with 14B (cross-domain C0 test)\n6. **\"ProofWriter shows 0pp gain\"** → Domain analysis in exp-001 expanded results\n7. **\"Random tiebreak baseline closes the gap\"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison (done on D012, will re-run on expanded)\n8. **\"Why not just use a reasoning model?\"** → exp-005: QwQ-32B + exp-014: DeepSeek-R1 show reasoning models are self-consistent → SICA redundant; instruction models (cheaper, more deployed) benefit\n9. **\"MAX-SAT is over-engineering\"** → exp-013: Constraint ablation proves satisfiability checking adds value over simple counting\n10. **\"Within-family scaling?\"** → exp-004: 7B + exp-007: 72B-AWQ show C0 trend within Qwen family\n\n## Working Title\n**\"When Does Symbolic Consensus Help? Characterizing the Operating Regime of Constraint-Based Reasoning Aggregation\"**\n(Alternatives: \"Beyond Majority Voting: Using Trace Diversity to Predict When Symbolic Consensus Improves LLM Reasoning\")\n\n## Paper Structure (EMNLP 8pp + appendix)\n- Main Tables: T1 (Main Results 7 models × datasets), T2 (Tiebreak Comparison), T3 (K Sensitivity), T4 (Overhead)\n- Main Figures: F1 (Pipeline), F2 (C0 vs Gap Scatter — hero figure), F3 (Operating Regime Heatmap), F4 (K Curve)\n- Appendix: Constraint Ablation (exp-013), Case Studies (exp-008), GSM8K (exp-012), Per-Problem Detail\n\n## Claim Risk Notes\n- **Claim 1 make-or-break**: exp-013 constraint ablation. If MaxSAT ≈ count-only → reframe as \"principled weighting\" not \"satisfiability-based reasoning\"\n- **Claim 3 downgrade risk**: If C0 has only 2 clusters (high/low) with no gradient → weaken to \"binary indicator\" not \"continuous predictor\". Gradient depends on 7B C0 >> 14B C0 >> 72B C0.\n- **\"Epistemic uncertainty\" terminology**: Reserve for Discussion section only. Main text uses \"effective output diversity\" / \"task-relative model confidence\". UQ community would attack formal misuse.\n\n## Contingency Plan (D023)\n**Trigger**: exp-001 完整结果 SICA ≤ SC（gap ≤ 0pp 或不显著）\n**Strategy**: Option A (Analysis Paper) + Option C (FOLIO sub-claim if positive)\n- 论文主线从\"SICA improves accuracy\"转为\"characterizing operating conditions of symbolic consensus\"\n- C0 threshold pattern 成为核心贡献（\"at what C0 level does SICA begin to match/exceed SC?\")\n- FOLIO 正向结果嵌入为\"domain formality → effectiveness\"子 claim\n- Claim 1 弱化为\"principled + interpretable tiebreaking\"（不 claim accuracy gain）\n- 需补：constraint extraction quality vs delta 相关性分析（CPU-only）\n- Venue: EMNLP Main (30-35%) / Findings (60-70%) / AAAI 2027 fallback\n**Decision point**: exp-001 FOLIO 70题的 C0 和 delta\n\n## Venue Fit Risks\n- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the \"operating regime characterization\" — the tiebreaking mechanism is evidence, not the claim.\n- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.\n- Negative results: QwQ-32B data must be presented as insight (\"When Does Symbolic Consensus Degenerate?\"), not failure.\n- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.\n- **[D023 新增]** If SICA ≤ SC globally: pivot to analysis paper. Must answer \"so what should practitioners do?\" → C0 as deployment diagnostic.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: RUNNING\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,12,16,20) on D012''s 60 questions. Key questions:\n    does SICA benefit depend on tiebreaks? What happens at odd K (no even splits)?\n    How does tiebreak frequency change with K?'\n  priority: P0\n  gpu_budget_hours: 5\n  deps: []\n  status: planned\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Within-Qwen scaling dimension.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX\n    PRO 6000 单卡可放。\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。\n- id: exp-010\n  name: sica_mistral_7b\n  claim:\n  - 2\n  - 3\n  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family\n    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''\n    attack.'\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+\n    题（~3h GPU，margin 允许）。'\n- id: exp-011\n  name: sica_llama_8b\n  claim:\n  - 2\n  - 3\n  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.\n    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation\n    同 exp-010。\n- id: exp-012\n  name: gsm8k_pilot_14b\n  claim:\n  - 2\n  - 3\n  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:\n    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer\n    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain\n    win.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable\n    insight.\n- id: exp-013\n  name: constraint_ablation\n  claim:\n  - 1\n  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count\n    per answer, no satisfiability) vs SICA-random-weight. Tests whether MAX-SAT is\n    essential or over-engineering.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 新增. 防御 'over-engineering' reviewer attack. CPU-only, 零 GPU 成本。\n- id: exp-014\n  name: sica_deepseek_r1_llama_8b\n  claim:\n  - 2\n  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning\n    model data point with LLaMA base architecture: validates C0<5% generalizes beyond\n    QwQ-32B AND eliminates ''still Qwen family'' attack.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T12:51:27.780Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T12:51:27.780Z",
  "sessionId": "9ab0fddf-13bd-4258-a788-5a3c235fb9c5"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T12:51:27.802Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Expanded results show SICA≈SC overall; FOLIO gain shrinks to noise at scale; D023 contingency triggered — must pivot to analysis paper
核心假设：['FOLIO gap ≤+2pp at 204-question scale, p>0.20', 'Combined gap ≤+0.5pp (effectively zero)', 'Cross-family C0 pattern holds (C0>20% for instruction models) BUT high C0 does not reliably translate to SICA>SC', 'MaxSAT ≈ count-only (no satisfiability value)', 'Tiebreak win rate 50-60% (barely above random on expanded set)', 'Core failure: constraint extraction quality insufficient to consistently beat voting even when traces diverge']
关键指标范围：{'folio_gap_pp': [-1.0, 2.0], 'combined_gap_pp': [-1.0, 0.5], 'bootstrap_p_folio': [0.2, 0.5], 'bootstrap_p_combined': [0.35, 0.6], 'c0_14b_expanded': [0.3, 0.5], 'c0_mistral_7b': [0.15, 0.4], 'c0_llama_8b': [0.15, 0.4], 'c0_deepseek_r1': [0.0, 0.08], 'tiebreak_win_rate': [0.45, 0.6], 'maxsat_vs_countonly_delta_pp': [-1.0, 0.5], 'c0_7b': [0.4, 0.65], 'c0_72b': [0.2, 0.45]}
叙事方向：D023 activated. All 3 original claims abandoned as accuracy claims. Paper pivots to: 'Why Doesn't Symbolic Consensus Improve LLM Reasoning? A Diagnostic Study.' New contribution structure: (1) C0 as a reliable zero-cost indicator of output diversity across model families — characterizes WHEN models disagree, not IF symbolic methods help; (2) Negative result on constraint-based aggregation — identifies failure modes (extraction noise, shallow constraints that don't capture deep reasoning errors); (3) Taxonomy of reasoning model vs instruction model behavior under sampling — reasoning models are structurally self-consistent regardless of temperature/K. Supplement with constraint-quality-vs-delta correlation analysis (CPU-only). Frame QwQ/DeepSeek convergence as novel finding about reasoning model internals. Target: EMNLP Findings (50-60%) with AAAI 2027 Main as fallback if reviewers want more models.

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
  "promptId": "9a401902-2efe-4035-8332-db0600b15e40",
  "type": "user",
  "uuid": "e3d38289-4df2-4058-b98f-60bfa2db5e98",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "9ab0fddf-13bd-4258-a788-5a3c235fb9c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T12:51:27.801Z_

```json
{
  "parentUuid": "e3d38289-4df2-4058-b98f-60bfa2db5e98",
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
  "uuid": "0ffe51f8-751f-4916-87d5-8a031df6606b",
  "timestamp": "2026-05-16T12:51:27.801Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "9ab0fddf-13bd-4258-a788-5a3c235fb9c5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T12:51:27.801Z_

```json
{
  "parentUuid": "0ffe51f8-751f-4916-87d5-8a031df6606b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8931b2e4-9150-4bc2-a73a-5d69fe61f50d",
  "timestamp": "2026-05-16T12:51:27.801Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "9ab0fddf-13bd-4258-a788-5a3c235fb9c5",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Expanded results show SICA≈SC overall; FOLIO gain shrinks to noise at scale; D023 contingency triggered — must pivot to analysis paper 核心假设：['FOLIO gap ≤+…",
  "leafUuid": "8931b2e4-9150-4bc2-a73a-5d69fe61f50d",
  "sessionId": "9ab0fddf-13bd-4258-a788-5a3c235fb9c5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Symbolic consensus operating regime under worst-case scenario",
  "sessionId": "9ab0fddf-13bd-4258-a788-5a3c235fb9c5"
}
```

---

### Assistant

_source line 8 · 2026-05-16T12:51:40.303Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experimental data for every "planned" experiment in the experiment_plan, specifically for the "worst" tier scenario. I need to produce a single YAML block with the worst-case predictions for each planned experiment, with result_rationale explaining why each result would occur under this tier.

Let me go through each planned experiment:

1. exp-001 (sica_expanded_14b) - RUNNING, but I should predict its results
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
14. exp-014 (sica_deepseek_r1_llama_8b) - planned

Now I need to construct worst-case scenario results for all of these, considering factors like model scaling limitations, constraint overhead, and performance degradation across different architectures and datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8931b2e4-9150-4bc2-a73a-5d69fe61f50d",
  "isSidechain": false,
  "requestId": "req_011Cb6H5r1GpieEycPytQVrk",
  "type": "assistant",
  "uuid": "140a8897-9fb5-4b81-869c-706c9ed80303",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "9ab0fddf-13bd-4258-a788-5a3c235fb9c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVZrcHp2y3tR29LYjyp63k",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13011,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11545,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11545,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13011
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

_source line 9 · 2026-05-16T12:55:12.878Z_

```yaml
tier: worst
narrative_guidance: >
  D023 triggered. All 3 original accuracy claims abandoned. Paper pivots to
  "Why Doesn't Symbolic Consensus Improve LLM Reasoning? A Diagnostic Study."
  Contributions restructured: (1) C0 as zero-cost diversity indicator across model
  families — characterizes WHEN models disagree, not IF symbolic methods help;
  (2) Negative result on constraint-based aggregation — identifies failure modes
  (extraction noise, shallow constraints); (3) Taxonomy of reasoning vs instruction
  model behavior under sampling. Target EMNLP Findings (50-60%), AAAI 2027 fallback.

imagined_experiments:
  - name: sica_expanded_14b
    plan_id: exp-001
    description: "PW D5 600 + FOLIO 204 = 804 questions, K=12, T=0.7, Qwen2.5-14B-Instruct"
    expected_results:
      n_total: 804
      n_folio: 204
      n_pw: 600
      sica_accuracy_combined: 0.723
      sc_accuracy_combined: 0.720
      combined_gap_pp: 0.3
      bootstrap_p_combined: 0.42
      sica_accuracy_folio: 0.755
      sc_accuracy_folio: 0.740
      folio_gap_pp: 1.5
      bootstrap_p_folio: 0.28
      sica_accuracy_pw: 0.712
      sc_accuracy_pw: 0.713
      pw_gap_pp: -0.1
      bootstrap_p_pw: 0.55
      c0_folio: 0.38
      c0_pw: 0.42
      c0_combined: 0.41
      maxsat_exclusion_rate: 0.031
      tiebreak_count_folio: 18
      tiebreak_count_pw: 55
      tiebreak_sica_win_rate: 0.55
      wall_time_h: 13.5
    result_rationale: >
      D012的60题FOLIO +6.7pp是小样本方差膨胀的产物。扩展到204题后，FOLIO的gain从+6.7pp
      回归到+1.5pp（p=0.28），因为D012中SICA赢的那几道tiebreak题恰好是高信息量的，但在
      更大样本中tiebreak题的比例被稀释、且新增题中constraint extraction质量参差不齐——
      约30%的FOLIO新增题涉及复杂嵌套量词，extraction产生shallow/错误constraints，MaxSAT
      解与count-only等价。PW在600题规模上SICA与SC几乎完全一致（-0.1pp），因为PW的逻辑
      结构虽然更formal，但14B在PW D5上的SC已经接近ceiling（~71%），剩余错题多为模型
      根本理解不了的推理链，constraint extraction无法挽救。Combined gap仅+0.3pp，
      bootstrap p=0.42，远未达到显著性。核心问题：constraint extraction的噪声在大样本
      中不再被幸运tiebreak掩盖。
    tables:
      - name: "T1_main_results_expanded"
        content: |
          | Dataset    |   N | SC Acc | SICA Acc | Gap (pp) | p-value |  C0  |
          |------------|-----|--------|----------|----------|---------|------|
          | FOLIO      | 204 | 74.0%  |  75.5%   |   +1.5   |  0.28   | 0.38 |
          | PW-D5      | 600 | 71.3%  |  71.2%   |   -0.1   |  0.55   | 0.42 |
          | Combined   | 804 | 72.0%  |  72.3%   |   +0.3   |  0.42   | 0.41 |
          | D012 (ref) |  60 | 70.0%  |  73.3%   |   +3.3   |  0.23   | 0.53 |
    figures_description:
      - "Bar chart: D012 vs Expanded FOLIO gap收缩可视化，误差条重叠"
      - "Per-question delta histogram: 大多数delta=0，少数±1，分布近似对称"
    analysis: >
      D023 trigger确认。FOLIO gap ≤+2pp且p>0.20，combined gap ≈0。论文必须pivot。
      但C0=0.38-0.42的数据仍然有价值——证明14B instruction model在这些任务上确实产生
      trace diversity，只是symbolic aggregation无法有效利用这些diversity。

  - name: sica_k_ablation_14b
    plan_id: exp-002
    description: "K sensitivity (K=6,8,12,16,20) on D012's 60 questions"
    expected_results:
      k6_sica_acc: 0.717
      k6_sc_acc: 0.700
      k6_gap_pp: 1.7
      k6_c0: 0.45
      k6_tiebreak_count: 8
      k8_sica_acc: 0.717
      k8_sc_acc: 0.700
      k8_gap_pp: 1.7
      k8_c0: 0.48
      k8_tiebreak_count: 6
      k12_sica_acc: 0.733
      k12_sc_acc: 0.700
      k12_gap_pp: 3.3
      k12_c0: 0.53
      k12_tiebreak_count: 5
      k16_sica_acc: 0.717
      k16_sc_acc: 0.717
      k16_gap_pp: 0.0
      k16_c0: 0.52
      k16_tiebreak_count: 3
      k20_sica_acc: 0.717
      k20_sc_acc: 0.717
      k20_gap_pp: 0.0
      k20_c0: 0.50
      k20_tiebreak_count: 2
      wall_time_h: 4.8
    result_rationale: >
      K=12时的+3.3pp是D012原始结果的复现，但这个gain几乎完全来自tiebreak场景。
      K=6/8（奇数tiebreak不可能或更少）时gap降到+1.7pp，因为偶数K下tie更频繁但
      SICA在tie上的win rate仅~55%，所以净gain不稳定。K=16/20时tie几乎消失（majority
      更decisive），gap归零。这揭示了一个致命模式：SICA的gain完全依赖于tiebreak频率，
      而非对非tie题的改进。K增大→tie减少→gain消失，说明SICA不是在做更好的推理聚合，
      只是在coin-flip场景中略好于random。C0随K略有变化但基本稳定在0.45-0.53，说明
      trace diversity是模型固有属性而非K的函数——这一点对analysis paper有价值。
    tables:
      - name: "T3_k_sensitivity"
        content: |
          |  K  | SC Acc | SICA Acc | Gap | C0   | #Ties | Tie Win% |
          |-----|--------|----------|-----|------|-------|----------|
          |  6  | 70.0%  |  71.7%   | 1.7 | 0.45 |   8   |  56.3%   |
          |  8  | 70.0%  |  71.7%   | 1.7 | 0.48 |   6   |  55.0%   |
          | 12  | 70.0%  |  73.3%   | 3.3 | 0.53 |   5   |  60.0%   |
          | 16  | 71.7%  |  71.7%   | 0.0 | 0.52 |   3   |  50.0%   |
          | 20  | 71.7%  |  71.7%   | 0.0 | 0.50 |   2   |  50.0%   |
    figures_description:
      - "F4_k_curve: Gap vs K折线图，显示gap在K>12后趋零"
      - "Tiebreak frequency vs K: 明显下降曲线"
    analysis: >
      Worst tier下K ablation暴露SICA的核心弱点：gain完全是tiebreak artifact。
      对analysis paper有价值：说明constraint-based方法在非tie场景无法改变SC的选择，
      因为extraction noise使constraint分布与answer正确性无相关性。

  - name: tiebreak_baseline_analysis
    plan_id: exp-003
    description: "SICA vs SC-random vs SC-deterministic tiebreak comparison, CPU reanalysis"
    expected_results:
      n_tiebreak_problems_d012: 5
      sica_tiebreak_win_rate: 0.60
      sc_random_tiebreak_expected_win_rate: 0.50
      sc_alphabetical_win_rate: 0.60
      sc_first_seen_win_rate: 0.40
      n_tiebreak_problems_expanded: 73
      sica_tiebreak_win_rate_expanded: 0.534
      sc_random_expected_expanded: 0.50
      bootstrap_p_sica_vs_random_expanded: 0.31
      sica_minus_random_gap_on_ties_pp: 3.4
      overall_sica_vs_sc_random_gap_pp: 0.1
    result_rationale: >
      D012上5个tiebreak题SICA赢4个（80%）是小样本幸运。扩展到exp-001的73个tiebreak题后，
      SICA的tiebreak win rate回归到53.4%——仅比random的50%高3.4pp，bootstrap p=0.31，
      不显著。核心原因：constraint extraction在tiebreak题上的质量与非tiebreak题无差异，
      而tiebreak题本身是模型"真不确定"的题，extracted constraints同样嘈杂、浅层，
      MaxSAT无法从噪声中提取信号。SICA略高于random可能只是因为MaxSAT倾向于选择
      constraint数更多的answer，而这与正确性有微弱正相关（正确reasoning chain产生
      略多parseable constraints）。但这个效应太弱，无法在统计上与random区分。
    tables:
      - name: "T2_tiebreak_comparison"
        content: |
          | Tiebreak Method    | D012 (5 ties) | Expanded (73 ties) | p vs random |
          |--------------------|---------------|--------------------|-------------|
          | SICA (MaxSAT)      |   80.0%       |     53.4%          |    0.31     |
          | SC-random          |   50.0%       |     50.0% (E)      |     —       |
          | SC-alphabetical    |   60.0%       |     49.3%          |    0.48     |
          | SC-first-seen      |   40.0%       |     50.7%          |    0.47     |
    figures_description:
      - "Tiebreak win rate bar chart with 95% CI whiskers: 所有方法的CI严重重叠"
    analysis: >
      Worst tier核心证据之一。SICA的tiebreak优势在大样本中消失，与random不可区分。
      对analysis paper的contribution：证明constraint extraction的质量不足以在
      真正ambiguous的题上提供信号——constraints是shallow syntactic patterns，
      不capture deep reasoning validity。

  - name: sica_7b_scaling
    plan_id: exp-004
    description: "Qwen2.5-7B-Instruct on 60 questions, within-Qwen scaling"
    expected_results:
      sica_accuracy: 0.583
      sc_accuracy: 0.567
      gap_pp: 1.7
      bootstrap_p: 0.38
      c0: 0.55
      c0_folio: 0.50
      c0_pw: 0.58
      sc_accuracy_folio: 0.600
      sc_accuracy_pw: 0.545
      sica_accuracy_folio: 0.633
      sica_accuracy_pw: 0.545
      maxsat_exclusion_rate: 0.045
      constraint_quality_score: 0.42
      wall_time_h: 1.8
    result_rationale: >
      7B模型更弱→C0更高（0.55 vs 14B的0.53），符合"weaker model = more diversity"假设。
      但SICA gain仅+1.7pp（p=0.38），不显著。原因：虽然7B产生更多diversity（更多tie和
      multi-candidate问题），但7B的constraint extraction质量更差——7B生成的reasoning
      traces更短、逻辑结构更松散，LLM-based extraction从这些traces中提取的constraints
      更浅层、更多噪声。高C0+低extraction quality=SICA无法利用diversity。这是worst tier
      的核心失败模式：C0确实预测diversity，但diversity≠SICA can help，因为中间的
      constraint extraction是bottleneck。FOLIO上有微弱+3.3pp是因为FOLIO答案空间
      只有3类（True/False/Unknown），即使noisy constraints也能偶尔选对。
    tables:
      - name: "scaling_7b_row"
        content: |
          | Model | SC Acc | SICA Acc | Gap | p    | C0   |
          |-------|--------|----------|-----|------|------|
          | 7B    | 56.7%  |  58.3%   | 1.7 | 0.38 | 0.55 |
          | 14B   | 70.0%  |  73.3%   | 3.3 | 0.23 | 0.53 |
    figures_description:
      - "C0 vs model size scatter点 (7B, 14B)：C0随size略降，但gap并非随C0线性增"
    analysis: >
      C0高但gap不显著——直接反驳"C0 predicts SICA gain"的简单叙事。
      对analysis paper：C0 predicts diversity (✓) 但不 predict gain (✗)，
      因为constraint extraction quality是hidden confounder。

  - name: qwq_32b_operating_regime
    plan_id: exp-005
    description: "QwQ-32B existing data formatted for operating regime analysis"
    expected_results:
      c0_aime: 0.0
      c0_pw: 0.188
      c0_folio: 0.0
      c0_combined: 0.036
      sica_sc_gap_pp: 0.0
      n_total: 48
      finding: "Reasoning model structurally self-consistent across all domains and temperatures"
      temperature_effect: "Zero diversity at T=0.7, 0.9, 1.0"
    result_rationale: >
      这是已有数据的重新整理，不产生新结果。QwQ-32B的C0=3.6%已经确认reasoning model
      的structural self-consistency。在worst tier下这个数据点的价值反而增强——它是
      analysis paper的核心finding之一：reasoning models (QwQ, DeepSeek-R1) 的
      extended thinking chain使输出高度确定性，温度采样无法打破这个determinism。
      这不是SICA的失败，而是reasoning model internals的特性。
    tables:
      - name: "qwq_operating_regime"
        content: |
          | Domain | N  | C0    | SC Acc | SICA Acc | Gap |
          |--------|----|-------|--------|----------|-----|
          | AIME   | 22 | 0.0%  | 72.7%  |  72.7%   | 0.0 |
          | PW     | 16 | 18.8% | ~69%   |  ~69%    | 0.0 |
          | FOLIO  | 10 | 0.0%  |  —     |   —      | 0.0 |
    figures_description:
      - "C0 heatmap row for QwQ-32B: 几乎全白（near-zero diversity across domains）"
    analysis: >
      对analysis paper是正面贡献：reasoning model的self-consistency是一个有发表价值的
      empirical finding。Frame为"reasoning models represent a fundamentally different
      operating regime where symbolic consensus is structurally redundant"。

  - name: c0_diagnostic_validation
    plan_id: exp-006
    description: "C0 vs SICA-SC gap scatter across all models and K values, CPU analysis"
    expected_results:
      n_datapoints: 12
      pearson_r_c0_vs_gap: 0.31
      pearson_p: 0.33
      spearman_rho: 0.27
      binary_threshold_accuracy: 0.75
      c0_threshold_used: 0.20
      high_c0_avg_gap: 0.8
      low_c0_avg_gap: 0.0
      high_c0_points: 8
      low_c0_points: 4
    result_rationale: >
      在worst tier下，C0与gap的连续相关性很弱（r=0.31, p=0.33），因为高C0的数据点
      （7B/14B/Mistral/LLaMA instruction models）虽然都有C0>20%，但gap分布在
      [-1pp, +2pp]之间，无清晰趋势。二值分类（C0>20% → potential gain vs C0<20% →
      no gain）准确率75%，但这主要是因为low-C0点（QwQ, DeepSeek-R1）gap全为0，
      而不是因为high-C0点gap都>0。实质上C0只能区分"reasoning vs instruction"，
      不能在instruction model内部预测gain大小。这使得Claim 3从"continuous predictor"
      弱化为"binary family classifier"——而这基本等于直接看模型是否是reasoning model，
      C0作为diagnostic的增量价值存疑。
    tables:
      - name: "c0_diagnostic_summary"
        content: |
          | Model              | Type        | C0    | Gap(pp) |
          |--------------------|-------------|-------|---------|
          | Qwen2.5-7B        | instruction | 0.55  |  +1.7   |
          | Qwen2.5-14B (D012)| instruction | 0.53  |  +3.3   |
          | Qwen2.5-14B (exp) | instruction | 0.41  |  +0.3   |
          | Qwen2.5-72B-AWQ   | instruction | 0.32  |  +0.5   |
          | Mistral-7B         | instruction | 0.35  |  -0.5   |
          | LLaMA-8B           | instruction | 0.30  |  +1.0   |
          | QwQ-32B            | reasoning   | 0.04  |   0.0   |
          | DeepSeek-R1-8B     | reasoning   | 0.05  |   0.0   |
    figures_description:
      - "F2_hero: C0 vs Gap scatter, 两个明显cluster（reasoning near origin, instruction scattered along C0=0.3-0.55 with gap≈0），无清晰正相关线"
      - "F3_heatmap: model × domain C0 heatmap，颜色深浅对比清晰但gap column灰度几乎无变化"
    analysis: >
      C0作为continuous predictor失败，仅作为binary indicator区分reasoning/instruction。
      对analysis paper：C0的价值从"predict gain"转为"characterize model behavior"——
      一个关于模型内部一致性的诊断工具，而非SICA部署决策工具。

  - name: sica_72b_awq
    plan_id: exp-007
    description: "Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions"
    expected_results:
      sica_accuracy: 0.783
      sc_accuracy: 0.783
      gap_pp: 0.0
      bootstrap_p: 0.50
      c0: 0.32
      c0_folio: 0.27
      c0_pw: 0.35
      sc_accuracy_folio: 0.833
      sc_accuracy_pw: 0.750
      maxsat_exclusion_rate: 0.022
      wall_time_h: 3.8
    result_rationale: >
      72B模型更强→SC accuracy更高（78.3% vs 14B的70%），C0降到0.32（更confident→
      更少diversity）。Gap=0pp因为：(1) 高accuracy意味着SC已经选对了大部分题，
      剩余错题是72B根本做不对的hard题；(2) C0=0.32虽然>20%但tiebreak题更少（约3个），
      样本太小无法产生可见gap；(3) 72B的constraint extraction质量虽然比7B/14B好，
      但在它做错的题上constraints同样misleading。这个数据点支持"stronger model →
      less room for SICA"的叙事，但也支持worst tier的核心论点：即使在C0>20%的
      optimal operating range内，SICA也不能reliably beat SC。
    tables:
      - name: "scaling_72b_row"
        content: |
          | Model | SC Acc | SICA Acc | Gap | p    | C0   |
          |-------|--------|----------|-----|------|------|
          | 7B    | 56.7%  |  58.3%   | 1.7 | 0.38 | 0.55 |
          | 14B   | 70.0%  |  73.3%   | 3.3 | 0.23 | 0.53 |
          | 72B   | 78.3%  |  78.3%   | 0.0 | 0.50 | 0.32 |
    figures_description:
      - "Within-Qwen scaling curve: SC acc上升, C0下降, gap先升后降呈倒U但peak也不显著"
    analysis: >
      72B数据点完善了within-family scaling故事。对analysis paper：展示了一个
      "sweet spot"幻觉——14B似乎是optimal，但扩展到大样本后14B的gap也消失。
      真正的故事是constraint extraction quality不随model size scaling。

  - name: constraint_quality_case_studies
    plan_id: exp-008
    description: "Qualitative analysis of 5-10 representative questions' extracted constraints"
    expected_results:
      n_analyzed: 8
      semantically_meaningful_rate: 0.45
      shallow_pattern_rate: 0.35
      noise_rate: 0.20
      correct_exclusion_rate: 0.30
      false_exclusion_rate: 0.15
      missed_error_rate: 0.55
      finding: "Constraints are predominantly surface-level pattern matches, not deep logical validators"
    result_rationale: >
      定性分析揭示constraint extraction的根本问题：(1) ~45%的constraints语义上有意义
      但过于浅层（如"answer must be True or False"）,不能区分正确/错误推理；
      (2) ~35%是shallow pattern matches（从推理trace中提取的句法模式而非逻辑约束）；
      (3) ~20%是纯噪声（extraction hallucination或parse error）。关键发现：在SICA
      选错而SC选对的题上，constraints质量与选对的题无显著差异——说明MaxSAT不是在
      "选择better constrained answer"，而是在"基于noisy signal做coin flip"。
      正确排除（exclusion导致正确答案翻转）仅30%，意味着大部分exclusion是neutral或harmful。
    tables: []
    figures_description:
      - "Constraint quality taxonomy figure: 3层饼图 (meaningful/shallow/noise)"
      - "Case study boxes: 2个SICA-correct + 2个SICA-wrong的constraint对比"
    analysis: >
      这是analysis paper最有叙事价值的实验之一。定性证据直接支撑"why doesn't it work"
      的故事：extraction bottleneck。LLM-based constraint extraction无法从free-form
      reasoning traces中提取足够faithful的逻辑约束。

  - name: overhead_analysis
    plan_id: exp-009
    description: "Wall-time breakdown per question: generation, extraction, MaxSAT"
    expected_results:
      avg_total_time_per_question_s: 45.2
      avg_generation_time_s: 38.5
      avg_extraction_time_s: 5.8
      avg_maxsat_time_s: 0.9
      generation_fraction: 0.852
      extraction_fraction: 0.128
      maxsat_fraction: 0.020
      overhead_vs_sc_percent: 17.4
      finding: "SICA adds ~17% wall-time overhead over SC, dominated by extraction LLM calls"
    result_rationale: >
      Generation（vLLM inference）占~85%时间，这与SC相同。SICA的额外overhead来自
      constraint extraction（~13%，每个trace一次extraction LLM call）和MaxSAT solving
      （~2%，Z3在小规模constraint sets上极快）。总overhead ~17%在worst tier下意味着
      "付出17%时间代价换来0pp gain"——对analysis paper来说这是一个重要的负面数据点。
      但也说明overhead不是failure的原因（不是"太贵所以不值"而是"even with acceptable
      cost it doesn't help"）。Extraction时间可优化（batch inference）但不改变
      fundamental result。
    tables:
      - name: "T4_overhead"
        content: |
          | Phase       | Time(s) | Fraction | Notes                    |
          |-------------|---------|----------|--------------------------|
          | Generation  |  38.5   |  85.2%   | Same as SC               |
          | Extraction  |   5.8   |  12.8%   | 1 LLM call per trace     |
          | MaxSAT      |   0.9   |   2.0%   | Z3, <100 constraints     |
          | **Total**   |  45.2   | 100.0%   | +17.4% vs SC baseline    |
    figures_description:
      - "Stacked bar: generation(blue) >> extraction(orange) >> maxsat(red)"
    analysis: >
      Overhead moderate但gain为零——cost-benefit明确为负。对analysis paper有价值：
      排除"overhead是barrier"假说，聚焦在extraction quality而非computational cost。

  - name: sica_mistral_7b
    plan_id: exp-010
    description: "Mistral-7B-Instruct-v0.3 on D012 60 questions, cross-family validation"
    expected_results:
      sica_accuracy: 0.550
      sc_accuracy: 0.567
      gap_pp: -1.7
      bootstrap_p: 0.65
      c0: 0.35
      c0_folio: 0.30
      c0_pw: 0.38
      sc_accuracy_folio: 0.633
      sc_accuracy_pw: 0.523
      sica_accuracy_folio: 0.600
      sica_accuracy_pw: 0.523
      maxsat_exclusion_rate: 0.052
      constraint_parse_error_rate: 0.12
      wall_time_h: 1.3
    result_rationale: >
      Mistral-7B是一个关键的cross-family数据点。C0=0.35（>20%，instruction model
      特征确认跨家族成立），但gap为负（-1.7pp）。原因：Mistral的reasoning trace风格与
      Qwen不同——更短、更conversational、逻辑结构更隐式。基于Qwen trace风格tuned的
      constraint extraction prompt在Mistral traces上效果更差（parse error rate 12%
      vs Qwen的~3%），产生更多noisy constraints。MaxSAT在noisy constraints下做出
      worse-than-random的selection（exclusion rate 5.2%但exclusion更多是false positive）。
      FOLIO上SICA反而比SC低3.3pp：3道FOLIO题上SICA的constraint-based选择选错了。
      这是worst tier的smoking gun：SICA不仅不帮忙，在extraction quality差的情况下
      actively harmful。
    tables:
      - name: "mistral_row"
        content: |
          | Model       | SC Acc | SICA Acc | Gap   | p    | C0   |
          |-------------|--------|----------|-------|------|------|
          | Mistral-7B  | 56.7%  |  55.0%   | -1.7  | 0.65 | 0.35 |
    figures_description:
      - "Cross-family C0 comparison bar chart: Mistral C0与Qwen-7B同level，但gap方向相反"
    analysis: >
      Worst tier关键证据：high C0 + negative gap。C0 pattern跨家族成立（instruction
      models都有high C0），但这不translate to SICA gains。Extraction quality是
      family-specific的，没有universal effectiveness。对analysis paper：constraint
      extraction的family-specificity是一个重要failure mode。

  - name: sica_llama_8b
    plan_id: exp-011
    description: "LLaMA-3.1-8B-Instruct on D012 60 questions, third model family"
    expected_results:
      sica_accuracy: 0.533
      sc_accuracy: 0.517
      gap_pp: 1.7
      bootstrap_p: 0.40
      c0: 0.30
      c0_folio: 0.27
      c0_pw: 0.32
      sc_accuracy_folio: 0.567
      sc_accuracy_pw: 0.485
      sica_accuracy_folio: 0.600
      sica_accuracy_pw: 0.485
      maxsat_exclusion_rate: 0.038
      wall_time_h: 1.2
    result_rationale: >
      LLaMA-8B的SC accuracy最低（51.7%），C0=0.30（instruction model，high diversity
      confirmed）。Gap=+1.7pp（p=0.40），方向正确但不显著。LLaMA的reasoning traces比
      Mistral更structured（更接近Qwen风格），extraction quality中等，所以gap没有变负。
      但在这么低的accuracy base上+1.7pp可能只是noise（1题的差异）。C0=0.30低于7B Qwen
      的0.55，可能因为LLaMA-8B在PW/FOLIO上部分题直接输出random答案而非structured
      reasoning，这些"collapsed"traces有相同的non-answer，被误计为low diversity。
      三家族一起看：Qwen +1.7, Mistral -1.7, LLaMA +1.7，平均gap≈+0.6pp——实质为零。
    tables:
      - name: "llama_row"
        content: |
          | Model      | SC Acc | SICA Acc | Gap  | p    | C0   |
          |------------|--------|----------|------|------|------|
          | LLaMA-8B   | 51.7%  |  53.3%   | +1.7 | 0.40 | 0.30 |
    figures_description:
      - "Three-family C0 bar chart: all >0.20, confirming cross-family pattern"
    analysis: >
      三家族validation完成：C0 pattern holds (all instruction models C0>20%)，
      但SICA gain inconsistent across families (Qwen略正, Mistral负, LLaMA略正)。
      对analysis paper：C0 as diversity indicator validated; SICA as accuracy method invalidated。

  - name: gsm8k_pilot_14b
    plan_id: exp-012
    description: "Qwen2.5-14B on GSM8K 30-question pilot, cross-domain C0 test"
    expected_results:
      sica_accuracy: 0.900
      sc_accuracy: 0.900
      gap_pp: 0.0
      c0: 0.10
      n_multi_candidate: 3
      sc_baseline_high: true
      constraint_extraction_issues: "Numeric answer space makes constraint extraction trivial but useless"
      wall_time_h: 0.8
    result_rationale: >
      GSM8K对14B来说太简单（SC=90%），C0=10%远低于FOLIO/PW的38-42%。14B在GSM8K上
      高度self-consistent因为这些是grade school math——模型confident且通常正确。
      C0=10%中的3道multi-candidate题是calculation errors（不同traces算出不同数字），
      constraint extraction对numeric answers基本无意义（constraints变成"answer=72"
      vs "answer=84"这种trivial形式，MaxSAT退化为counting）。Gap=0pp。
      这个结果对analysis paper有双面价值：(1) 证明C0反映task-relative model confidence
      （14B在easy math上confident→low C0, 在logic reasoning上uncertain→high C0）；
      (2) 证明SICA在open-answer domain无additional failure mode，只是没value。
    tables:
      - name: "gsm8k_row"
        content: |
          | Dataset | Model | SC Acc | SICA Acc | Gap | C0   |
          |---------|-------|--------|----------|-----|------|
          | GSM8K   | 14B   | 90.0%  |  90.0%   | 0.0 | 0.10 |
          | FOLIO   | 14B   | 74.0%  |  75.5%   | 1.5 | 0.38 |
          | PW-D5   | 14B   | 71.3%  |  71.2%   |-0.1 | 0.42 |
    figures_description:
      - "Cross-domain C0 comparison: GSM8K(low) vs FOLIO/PW(high)，支持task-relative confidence叙事"
    analysis: >
      C0 as task-relative confidence indicator validated。14B在easy tasks上low C0，
      hard tasks上high C0。但这不help SICA's accuracy case。对analysis paper：
      丰富了C0的characterization story。

  - name: constraint_ablation
    plan_id: exp-013
    description: "SICA-MaxSAT vs SICA-count-only vs SICA-random-weight, CPU ablation"
    expected_results:
      n_problems: 804
      maxsat_accuracy: 0.723
      count_only_accuracy: 0.722
      random_weight_accuracy: 0.718
      maxsat_vs_countonly_gap_pp: 0.1
      maxsat_vs_random_gap_pp: 0.5
      sc_accuracy: 0.720
      bootstrap_p_maxsat_vs_countonly: 0.48
      tiebreak_agreement_maxsat_countonly: 0.89
      finding: "MaxSAT satisfiability checking adds no value over simple constraint counting"
    result_rationale: >
      这是Claim 1的make-or-break实验。在worst tier下MaxSAT≈count-only（gap仅0.1pp,
      p=0.48）。原因：MaxSAT的附加价值来自satisfiability checking——检测constraints
      之间的逻辑一致性，排除internally contradictory constraint sets。但实际extracted
      constraints几乎都是独立的（无cross-constraint logical dependencies），因为
      extraction prompt从each trace independently提取，不产生inter-constraint
      implications。结果Z3的satisfiability solver对所有constraint sets都返回SAT
      （没有unsatisfiable subsets to detect），MaxSAT退化为weighted counting。
      Tiebreak上MaxSAT和count-only的选择89%一致。Random-weight略差但差距也很小
      （0.5pp），说明constraint count本身与正确性的相关性非常微弱。
    tables:
      - name: "constraint_ablation"
        content: |
          | Method        | Accuracy | vs SC  | vs MaxSAT | p vs MaxSAT |
          |---------------|----------|--------|-----------|-------------|
          | SICA-MaxSAT   | 72.3%    | +0.3pp |    —      |      —      |
          | SICA-CountOnly| 72.2%    | +0.2pp |  -0.1pp   |    0.48     |
          | SICA-RandWt   | 71.8%    | -0.2pp |  -0.5pp   |    0.35     |
          | SC baseline   | 72.0%    |   —    |  -0.3pp   |    0.42     |
    figures_description:
      - "Ablation bar chart with error bars: 四种方法几乎等高"
    analysis: >
      MaxSAT is over-engineering confirmed。但在analysis paper中这是一个有价值的
      negative finding：formal satisfiability checking对LLM-extracted constraints
      无附加价值，因为constraints缺乏inter-dependencies。Reframe为"when does
      formal reasoning over constraints add value? When constraints have structure."

  - name: sica_deepseek_r1_llama_8b
    plan_id: exp-014
    description: "DeepSeek-R1-Distill-LLaMA-8B on 60 questions, second reasoning model"
    expected_results:
      sica_accuracy: 0.633
      sc_accuracy: 0.633
      gap_pp: 0.0
      c0: 0.05
      c0_folio: 0.03
      c0_pw: 0.06
      sc_accuracy_folio: 0.700
      sc_accuracy_pw: 0.590
      temperature_invariance: true
      wall_time_h: 1.8
    result_rationale: >
      DeepSeek-R1-Distill-LLaMA-8B是第二个reasoning model数据点。C0=5%（与QwQ-32B的
      3.6%相近），SICA≡SC。虽然这是8B的distilled版本（base是LLaMA而非Qwen），其
      reasoning training使其表现出与QwQ-32B相同的self-consistency特征：extended
      thinking chain deterministically converges to single answer regardless of
      temperature sampling。C0=5%中的微量diversity来自PW（6%），可能是因为distillation
      在logic domain上不如QwQ-32B彻底，少数题的reasoning chain有细微分歧。
      关键确认：self-consistency是reasoning training的产物而非architecture/family
      的产物（LLaMA base instruction model C0=30%, 同LLaMA base reasoning model C0=5%）。
    tables:
      - name: "reasoning_models_combined"
        content: |
          | Model              | Base   | Type      | C0   | Gap  |
          |--------------------|--------|-----------|------|------|
          | QwQ-32B            | Qwen   | reasoning | 3.6% | 0.0  |
          | DeepSeek-R1-8B     | LLaMA  | reasoning | 5.0% | 0.0  |
          | LLaMA-3.1-8B-Inst | LLaMA  | instruct  | 30%  | +1.7 |
    figures_description:
      - "Same-base comparison: LLaMA-8B-Instruct(C0=30%) vs DeepSeek-R1-LLaMA-8B(C0=5%)——same architecture, reasoning training eliminates diversity"
    analysis: >
      对analysis paper的核心贡献之一：reasoning training fundamentally changes
      output diversity characteristics。Same LLaMA-8B base, instruction版C0=30%,
      reasoning版C0=5%。这是关于reasoning model internals的novel finding：
      reasoning training doesn't just improve accuracy, it collapses the output
      distribution. Frame为understanding WHY reasoning models are self-consistent.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "140a8897-9fb5-4b81-869c-706c9ed80303",
  "isSidechain": false,
  "requestId": "req_011Cb6H5r1GpieEycPytQVrk",
  "type": "assistant",
  "uuid": "9e4fb24f-3869-43d8-b85a-88bcaa2e5065",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "9ab0fddf-13bd-4258-a788-5a3c235fb9c5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DVZrcHp2y3tR29LYjyp63k",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13011,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11545,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13011,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11545,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13011
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Expanded results show SICA≈SC overall; FOLIO gain shrinks to noise at scale; D023 contingency triggered — must pivot to analysis paper 核心假设：['FOLIO gap ≤+…",
  "leafUuid": "9e4fb24f-3869-43d8-b85a-88bcaa2e5065",
  "sessionId": "9ab0fddf-13bd-4258-a788-5a3c235fb9c5"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Symbolic consensus operating regime under worst-case scenario",
  "sessionId": "9ab0fddf-13bd-4258-a788-5a3c235fb9c5"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Expanded results show SICA≈SC overall; FOLIO gain shrinks to noise at scale; D023 contingency triggered — must pivot to analysis paper 核心假设：['FOLIO gap ≤+…",
  "leafUuid": "9e4fb24f-3869-43d8-b85a-88bcaa2e5065",
  "sessionId": "9ab0fddf-13bd-4258-a788-5a3c235fb9c5"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Symbolic consensus operating regime under worst-case scenario",
  "sessionId": "9ab0fddf-13bd-4258-a788-5a3c235fb9c5"
}
```

---
