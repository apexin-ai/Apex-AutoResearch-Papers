# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：扩展后SICA-SC gap消失或反转——60q的+3.3pp是小样本噪声，tiebreaking无系统性优势 核心假设：['FOLIO扩展后gap缩

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/8c675d3e-c565-4a79-b341-e83a7a48d4d6.jsonl`
- **Structured JSON:** [`f85296c416d88b26a230.json`](../../sessions/f8/f85296c416d88b26a230.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T05:25:35.674Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T05:25:35.674Z",
  "sessionId": "8c675d3e-c565-4a79-b341-e83a7a48d4d6",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：扩展后SICA-SC gap消失或反转——60q的+3.3pp是小样本噪声，tiebreaking无系统性优势\n核心假设：['FOLIO扩展后gap缩小到<2pp，部分新题SICA反而输（constraint extraction引入噪声）', 'ProofWriter仍0pp或轻微负向', 'Combined gap <1pp，p>0.2——方向都不确定', 'K消融无清晰pattern——tiebreak频率变化但win rate不稳定', '7B的C0更高但SICA-SC gap≈0或负（高C0≠SICA有用，更多diversity可能是更多噪声）', 'C0与SICA增益无显著相关']\n关键指标范围：{'combined_gap_pp': [-1.0, 1.0], 'folio_gap_pp': [0.0, 2.5], 'proofwriter_gap_pp': [-1.5, 0.5], 'bootstrap_p_combined': [0.2, 0.5], 'c0_14b': [0.4, 0.55], 'c0_7b': [0.55, 0.75], 'c0_qwq': [0.0, 0.05], 'sica_7b_gap_pp': [-2.0, 1.5], 'tiebreak_win_rate': [0.45, 0.6], 'k_ablation_correlation_r': [0.0, 0.4]}\n叙事方向：三条原始claim全部不成立。必须完全reframe。新angle：\"A Negative Result Study on Symbolic Constraint Consensus\"或更建设性地：\"The Limits of Post-hoc Symbolic Verification in LLM Reasoning\"。核心论点转为：(1) 从reasoning traces中提取的 FOL constraints质量不足以系统性改进voting——extraction noise抵消了structural information的理论优势；(2) operating regime characterization仍成立但结论变为 \"symbolic consensus helps in neither regime\"——reasoning models不需要it（C0太低）， instruction models的diversity来自reasoning errors而非legitimate alternative paths，因此constraint weighting无法区分好坏traces；(3) 这揭示了一个deeper insight：current LLMs的reasoning traces不是formal proofs的noisy version， 而是根本不同的对象——symbolic extraction是category error。用exp-008的case study 作为evidence展示constraint quality failure modes。仍冲EMNLP——negative/analysis papers有先例，但需要extremely strong writing和深入的failure analysis。 同时准备AAAI 2027作为时间buffer。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\nfocus: Key tension: SICA's gain is entirely from principled tiebreaking (4/60 questions, all 6:6 ties). Reviewers will attack statistical significance (p=0.317) and question overhead vs benefit. The operating regime characterization (reasoning vs instruction model) is the primary intellectual contribution. Expanded 200+ question results and K ablation are planned but not yet available. ProofWriter shows 0pp gain — domain generalization is a weakness.\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Fallback: AAAI 2027 (Aug 1)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条)\n1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).\n2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is conditional on trace diversity — SICA adds value when model outputs are diverse (instruction models, C0>20%) but provably degenerates to SC when models are self-consistent (reasoning models, C0<5%). This is a model property, not a task property.\n3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.\n\n## Core Insight\nSymbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that model architecture (reasoning vs instruction) determines the operating regime. This transforms SICA from \"yet another ensemble method\" into \"a method with formally characterizable applicability boundaries.\"\n\n## Story Spine\n- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.\n- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.\n- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75% win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) and show it's governed by model type, not task type.\n- **Headline result template**: \"On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → exp-001: Expand to 200+ questions for statistical power\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K sensitivity showing benefit pattern; exp-009: overhead analysis\n3. **\"Only one non-reasoning model\"** → exp-004: Add Qwen2.5-7B for scaling; exp-007: 72B-AWQ for camera-ready\n4. **\"ProofWriter shows 0pp gain\"** → Domain analysis in exp-001 expanded results\n5. **\"Random tiebreak baseline closes the gap\"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison\n6. **\"Why not just use a reasoning model?\"** → exp-005: QwQ-32B data shows reasoning models are self-consistent (don't need consensus improvement), but instruction models (cheaper, more deployed) benefit from SICA\n\n## Venue Fit Risks\n- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the \"operating regime characterization\" — the tiebreaking mechanism is evidence, not the claim.\n- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.\n- Negative results: QwQ-32B data must be presented as insight (\"When Does Symbolic Consensus Degenerate?\"), not failure.\n- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: Expand D012 from 60 to 200+ questions (PW D5 ~100 + FOLIO ~100) for\n    statistical power on C3. Merge with D012 data for combined analysis.\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  status: planned\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,12,16,20) on D012''s 60 questions. Key questions:\n    does SICA benefit depend on tiebreaks? What happens at odd K (no even splits)?\n    How does tiebreak frequency change with K?'\n  priority: P0\n  gpu_budget_hours: 5\n  deps: []\n  status: planned\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: sica_d012_14b\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. For camera-ready if time permits.'\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T05:25:35.677Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T05:25:35.677Z",
  "sessionId": "8c675d3e-c565-4a79-b341-e83a7a48d4d6"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T05:25:35.703Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：扩展后SICA-SC gap消失或反转——60q的+3.3pp是小样本噪声，tiebreaking无系统性优势
核心假设：['FOLIO扩展后gap缩小到<2pp，部分新题SICA反而输（constraint extraction引入噪声）', 'ProofWriter仍0pp或轻微负向', 'Combined gap <1pp，p>0.2——方向都不确定', 'K消融无清晰pattern——tiebreak频率变化但win rate不稳定', '7B的C0更高但SICA-SC gap≈0或负（高C0≠SICA有用，更多diversity可能是更多噪声）', 'C0与SICA增益无显著相关']
关键指标范围：{'combined_gap_pp': [-1.0, 1.0], 'folio_gap_pp': [0.0, 2.5], 'proofwriter_gap_pp': [-1.5, 0.5], 'bootstrap_p_combined': [0.2, 0.5], 'c0_14b': [0.4, 0.55], 'c0_7b': [0.55, 0.75], 'c0_qwq': [0.0, 0.05], 'sica_7b_gap_pp': [-2.0, 1.5], 'tiebreak_win_rate': [0.45, 0.6], 'k_ablation_correlation_r': [0.0, 0.4]}
叙事方向：三条原始claim全部不成立。必须完全reframe。新angle："A Negative Result Study on Symbolic Constraint Consensus"或更建设性地："The Limits of Post-hoc Symbolic Verification in LLM Reasoning"。核心论点转为：(1) 从reasoning traces中提取的 FOL constraints质量不足以系统性改进voting——extraction noise抵消了structural information的理论优势；(2) operating regime characterization仍成立但结论变为 "symbolic consensus helps in neither regime"——reasoning models不需要it（C0太低）， instruction models的diversity来自reasoning errors而非legitimate alternative paths，因此constraint weighting无法区分好坏traces；(3) 这揭示了一个deeper insight：current LLMs的reasoning traces不是formal proofs的noisy version， 而是根本不同的对象——symbolic extraction是category error。用exp-008的case study 作为evidence展示constraint quality failure modes。仍冲EMNLP——negative/analysis papers有先例，但需要extremely strong writing和深入的failure analysis。 同时准备AAAI 2027作为时间buffer。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: symb_invariant_consensus
focus: Key tension: SICA's gain is entirely from principled tiebreaking (4/60 questions, all 6:6 ties). Reviewers will attack statistical significance (p=0.317) and question overhead vs benefit. The operating regime characterization (reasoning vs instruction model) is the primary intellectual contribution. Expanded 200+ question results and K ablation are planned but not yet available. ProofWriter shows 0pp gain — domain generalization is a weakness.

## paper_framing.md

# Paper Framing — symb_invariant_consensus

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25)
- Fallback: AAAI 2027 (Aug 1)
- Deadline: May 25, 2026 (ARR submission)

## Core Claims (3 条)
1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).
2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is conditional on trace diversity — SICA adds value when model outputs are diverse (instruction models, C0>20%) but provably degenerates to SC when models are self-consistent (reasoning models, C0<5%). This is a model property, not a task property.
3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.

## Core Insight
Symbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that model architecture (reasoning vs instruction) determines the operating regime. This transforms SICA from "yet another ensemble method" into "a method with formally characterizable applicability boundaries."

## Story Spine
- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.
- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.
- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75% win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) and show it's governed by model type, not task type.
- **Headline result template**: "On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty."

## Anticipated Reviewer Concerns & Defensive Experiments
1. **"Gains not statistically significant"** → exp-001: Expand to 200+ questions for statistical power
2. **"Only a better tiebreaker, not worth the overhead"** → exp-002: K sensitivity showing benefit pattern; exp-009: overhead analysis
3. **"Only one non-reasoning model"** → exp-004: Add Qwen2.5-7B for scaling; exp-007: 72B-AWQ for camera-ready
4. **"ProofWriter shows 0pp gain"** → Domain analysis in exp-001 expanded results
5. **"Random tiebreak baseline closes the gap"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison
6. **"Why not just use a reasoning model?"** → exp-005: QwQ-32B data shows reasoning models are self-consistent (don't need consensus improvement), but instruction models (cheaper, more deployed) benefit from SICA

## Venue Fit Risks
- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the "operating regime characterization" — the tiebreaking mechanism is evidence, not the claim.
- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.
- Negative results: QwQ-32B data must be presented as insight ("When Does Symbolic Consensus Degenerate?"), not failure.
- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.


## experiment_plan (with registry status)

- id: exp-001
  name: sica_expanded_14b
  claim:
  - 1
  - 2
  description: Expand D012 from 60 to 200+ questions (PW D5 ~100 + FOLIO ~100) for
    statistical power on C3. Merge with D012 data for combined analysis.
  priority: P0
  gpu_budget_hours: 4
  deps: []
  status: planned
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
  registry_id: sica_d012_14b
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
    high-baseline non-reasoning model. For camera-ready if time permits.'
  priority: P2
  gpu_budget_hours: 4
  deps:
  - exp-001
  status: planned
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
  priority: P2
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned


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
  status: QUEUED
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
  "promptId": "b4f74376-7bc7-438e-b632-0c905555f7d4",
  "type": "user",
  "uuid": "96798b15-a074-4952-a9b1-b41eea8b3821",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "8c675d3e-c565-4a79-b341-e83a7a48d4d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T05:25:35.702Z_

```json
{
  "parentUuid": "96798b15-a074-4952-a9b1-b41eea8b3821",
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
  "uuid": "70292832-9886-4260-a88f-028e18c52638",
  "timestamp": "2026-05-16T05:25:35.702Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "8c675d3e-c565-4a79-b341-e83a7a48d4d6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T05:25:35.702Z_

```json
{
  "parentUuid": "70292832-9886-4260-a88f-028e18c52638",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1972ab79-54af-4bd8-93dd-19def8d717ef",
  "timestamp": "2026-05-16T05:25:35.702Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "8c675d3e-c565-4a79-b341-e83a7a48d4d6",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：扩展后SICA-SC gap消失或反转——60q的+3.3pp是小样本噪声，tiebreaking无系统性优势 核心假设：['FOLIO扩展后gap缩小到<2pp，部分新题SICA反而输（constraint extraction引入噪声）', 'ProofWriter仍0pp或轻微负向', 'Combin…",
  "leafUuid": "1972ab79-54af-4bd8-93dd-19def8d717ef",
  "sessionId": "8c675d3e-c565-4a79-b341-e83a7a48d4d6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Negative result analysis on symbolic constraint consensus",
  "sessionId": "8c675d3e-c565-4a79-b341-e83a7a48d4d6"
}
```

---

### Assistant

_source line 8 · 2026-05-16T05:27:01.378Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experimental data for the "worst" tier scenario across all planned experiments in their experiment plan. Let me carefully go through each planned experiment and generate realistic worst-case data that aligns with the worst tier definition.

Let me review the worst tier definition:
- SICA-SC gap disappears or reverses after expansion
- The +3.3pp on 60q is small-sample noise
- Tiebreaking has no systematic advantage
- Core assumptions: FOLIO gap shrinks to <2pp, some new questions SICA loses, ProofWriter still 0pp or slightly negative, combined gap <1pp with p>0.2, K ablation shows no clear pattern, 7B has higher C0 but SICA gap ≈0 or negative, C0 and SICA gain not significantly correlated


- Now I'm setting the metric ranges for the worst-case scenario, with combined gap hovering near zero, FOLIO gap staying modest, ProofWriter showing minimal or negative effects, and the 7B model exhibiting higher baseline performance but negligible SICA advantage.

Looking at the planned experiments, I've got a series of validation studies lined up: expanding SICA to a larger question set, testing K sensitivity, comparing tiebreak strategies, scaling to 7B and 72B models, validating the C0 diagnostic approach, and running qualitative case studies to understand the constraint quality effects.

For the worst-case scenario where all three claims fail, the narrative hinges on the gap being statistical noise. I'm working through the specific numbers for each experiment now—starting with the expanded SICA run where I expect the gap to shrink dramatically as I add more questions from FOLIO and ProofWriter, eventually converging toward zero or slightly negative when pooled across datasets. Looking at the combined results across both datasets, I'm getting roughly equal performance between SICA and SC overall, with maybe a slight edge to SC. Let me settle on specific numbers that fit within the ranges I'm considering: FOLIO at 78.4% for SICA versus 76.5% for SC (a 1.9 percentage point gap), and ProofWriter at 62.3% for SICA versus 63.2% for SC (a 0.9 percentage point gap in SC's favor). I need to adjust the ProofWriter gap to fall within the [-1.5, 0.5] range, so -0.8pp works better. Now I'm fine-tuning the FOLIO numbers to hit exactly +1.5pp instead of +1.0pp, which means recalculating the question count and correct answer distribution. Now I'm laying out the full results across both datasets. For FOLIO, SICA edges out SC by about 1.9 percentage points, but ProofWriter actually shows SC slightly ahead by 0.9pp. When I combine them, the gap shrinks to essentially nothing at 0.5pp, with a bootstrap p-value of 0.38 suggesting this difference isn't statistically significant. Let me verify the math checks out: 82+68 gives 150 for SICA, 80+69 gives 149 for SC, which divides to roughly 70.75% versus 70.28%.

Breaking down the FOLIO results more carefully, the original 30 questions show SICA at 80% versus SC at 73.3%, but when I look at the new 74 questions, both methods perform identically at 78.4%. This tells me the gap in FOLIO came from just a couple of tie-breaking wins on the original questions, and the new data doesn't replicate that pattern. For ProofWriter, the original 30 questions had both methods tied, but the new 78 questions show SC pulling ahead slightly at 62.8% compared to SICA's 61.5%.

Now I'm testing different K values in the ablation study to see how the ensemble size affects performance. At K=6, SICA edges out SC by 1.7 percentage points with a high tie frequency, but the pattern isn't consistent across other K values. The gap shrinks at K=12 and nearly disappears at K=20, suggesting the advantage isn't stable across different ensemble configurations. Looking at the performance metrics across different K values, the gap between SICA and SC shows no meaningful correlation with K itself, and while tie frequency does weakly correlate with SICA's advantage, the K=10 result appears to be an outlier driven by lucky tie outcomes rather than a systematic pattern. Now I'm examining a separate analysis comparing SICA against both random and deterministic tiebreak strategies on the original dataset, where SICA's edge over random selection turns out to be quite modest in the worst-performing tier.

The results diverge sharply depending on dataset size: on the original 60 questions, SICA gains about 2.5 percentage points over random tiebreaking, with a notable advantage on tie questions specifically, but when expanded to 212 questions, that gap essentially vanishes to near zero, and the tie-question win rates equalize between SICA and random selection.

Looking at the 7B model scaling experiment, SICA actually underperforms compared to standard self-consistency—it's 1.7 points worse on the full set, and notably worse on FOLIO by 3.3 points, suggesting the approach breaks down on weaker models.

The bootstrap test confirms this isn't just noise; the p-value of 0.72 indicates the direction is genuinely wrong. The constraint extraction quality degrades significantly with the weaker model, so SICA's weighting mechanism ends up being counterproductive rather than beneficial.

Now I'm checking whether the diversity metric C0 actually correlates with SICA's performance gains across different model scales and sampling parameters, plotting the relationship across the 14B experiments with varying K values to see if there's a consistent pattern.

Looking at the correlation analysis, the Pearson r of 0.25 with p=0.52 is nowhere near significant. C0 doesn't predict SICA benefit at all—the hypothesis that constraint diversity drives improvement is fundamentally wrong.

Moving to the 72B-Instruct AWQ experiment on the 60-question set, which again shows no SICA advantage despite the stronger model having lower diversity.

But the qualitative case studies are where things get interesting. I'm seeing the real failure modes: the FOL translations are semantically incorrect about 30% of the time, constraints get extracted in multiple slightly different forms and over-counted, many constraints are tautological or irrelevant to the actual answer choices, and when reasoning traces are wrong, they produce consistent but incorrect constraints that reinforce the wrong answers. This explains why SICA fails in the worst tier—the constraint extraction process itself is fundamentally broken.

Looking at the overhead analysis, the picture gets worse. Generation takes up 70% of the time, constraint extraction another 20%, and MAX-SAT solving is only 2%. The total wall-time overhead compared to plain SC is 30% for essentially zero accuracy gain—about 18 seconds per question added for no benefit. This makes the computational cost completely unjustifiable.

Now I need to verify which experiments are actually planned versus already done. exp-005 is finished, so I'm working with 8 remaining experiments to generate data for. I should make sure the numbers are internally consistent and realistic since these will inform the paper's framing. Let me structure the YAML output carefully, with rationales that explain why each result occurs under the worst-case tier assumptions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1972ab79-54af-4bd8-93dd-19def8d717ef",
  "isSidechain": false,
  "requestId": "req_011Cb5h5qGQiqzwLVS3WDWkB",
  "type": "assistant",
  "uuid": "856a2722-fdc7-4302-859a-2a361ca4d6f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "8c675d3e-c565-4a79-b341-e83a7a48d4d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155NEi95pc6dnctRvVdDyHU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11126,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15109,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11126
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

_source line 9 · 2026-05-16T05:30:14.944Z_

```yaml
tier: worst
narrative_guidance: >
  三条原始claim全部不成立。+3.3pp是60q小样本噪声，扩展后gap蒸发。Tiebreaking win rate回归50%——
  无系统性优势。C0与SICA增益无相关性——高diversity带来的是更多噪声而非更多信号。必须完全reframe为
  negative result paper："The Limits of Post-hoc Symbolic Verification in LLM Reasoning"。
  核心论点：从reasoning traces中提取的FOL constraints质量不足以支撑系统性改进，constraint extraction
  是对LLM reasoning traces的category error。用exp-008的failure mode taxonomy作为主要贡献。
  仍冲EMNLP——negative/analysis papers有先例（需extremely strong writing），同时准备AAAI 2027。

imagined_experiments:
  - name: sica_expanded_14b
    plan_id: exp-001
    description: >
      Qwen2.5-14B-Instruct在扩展数据集上运行SICA vs SC。FOLIO扩展至104题，ProofWriter扩展至108题，
      合计212题。与原60题D012数据合并分析。
    expected_results:
      n_folio: 104
      n_proofwriter: 108
      n_combined: 212
      folio_sica_acc: 0.788
      folio_sc_acc: 0.769
      folio_gap_pp: 1.9
      folio_new_74q_sica_acc: 0.784
      folio_new_74q_sc_acc: 0.784
      folio_new_74q_gap_pp: 0.0
      proofwriter_sica_acc: 0.630
      proofwriter_sc_acc: 0.639
      proofwriter_gap_pp: -0.9
      combined_sica_acc: 0.708
      combined_sc_acc: 0.703
      combined_gap_pp: 0.5
      bootstrap_p_combined: 0.38
      bootstrap_p_folio: 0.31
      bootstrap_p_proofwriter: 0.62
      c0_combined: 0.47
      c0_folio: 0.43
      c0_proofwriter: 0.51
      tie_questions_total: 10
      tie_sica_wins: 5
      tie_sc_wins: 5
      tiebreak_win_rate: 0.50
      c1_extraction_rate: 0.98
      total_constraints_raw: 18740
      total_constraints_unique: 4820
      maxsat_exclusion_rate: 0.031
      wall_time_min: 195
    result_rationale: >
      原60题的+3.3pp完全来自4个6:6 tie的SICA胜出（4/6=67% win rate）。扩展后新增152题中，
      tie出现频率符合预期（~5%），但SICA在新tie上的win rate回归到50%——与随机无异。
      关键现象：原30道FOLIO的+6.7pp保持（这是历史数据），但新74道FOLIO上SICA与SC完全相同（0pp）。
      这说明原始gap是小样本中tiebreak碰巧对了几道题，而非SICA有系统性优势。
      ProofWriter扩展后出现轻微负向（-0.9pp），因为constraint extraction在ProofWriter的
      closed-world assumption下引入噪声——提取的FOL约束有时将正确trace降权。
      合并后+0.5pp，p=0.38，远不显著。连方向都不确定。
    tables:
      - caption: "Table 1: SICA vs SC accuracy on expanded benchmarks (K=10, T=0.7, Qwen2.5-14B-Instruct)"
        columns: [Dataset, N, SICA_Acc, SC_Acc, Gap_pp, p_bootstrap, C0]
        rows:
          - [FOLIO (original 30), 30, 80.0, 73.3, "+6.7", 0.14, 0.53]
          - [FOLIO (new 74), 74, 78.4, 78.4, "0.0", 0.50, 0.39]
          - [FOLIO (all), 104, 78.8, 76.9, "+1.9", 0.31, 0.43]
          - [ProofWriter (original 30), 30, 66.7, 66.7, "0.0", 0.50, 0.53]
          - [ProofWriter (new 78), 78, 61.5, 62.8, "-1.3", 0.58, 0.50]
          - [ProofWriter (all), 108, 63.0, 63.9, "-0.9", 0.62, 0.51]
          - [Combined (original 60), 60, 73.3, 70.0, "+3.3", 0.23, 0.53]
          - [Combined (all), 212, 70.8, 70.3, "+0.5", 0.38, 0.47]
      - caption: "Table 2: Tiebreak analysis — original vs expanded"
        columns: [Dataset, N_ties, SICA_wins, SC_wins, Win_rate]
        rows:
          - [Original 60q, 6, 4, 2, 0.67]
          - [New 152q, 4, 1, 3, 0.25]
          - [All 212q, 10, 5, 5, 0.50]
    figures_description:
      - "Fig 1: Bar chart showing SICA-SC gap on original 60q vs expanded 212q. Gap从+3.3pp缩减到+0.5pp，error bar覆盖0。"
      - "Fig 2: Per-question SICA-SC correctness差异散点图。212题中仅15题有差异（SICA对8题，SC对7题），其余197题完全一致。"
    analysis: >
      扩展后的核心发现：SICA和SC在绝大多数题目上（93%）给出完全相同的答案——MAX-SAT reweighting
      几乎从不改变majority vote结果。仅在tie situations下有区别，而SICA的tie resolution
      并不优于随机。原始+3.3pp是6个tie中碰巧赢了4个的结果（p(≥4|6, 0.5)=0.34），
      完全在随机波动范围内。Claim 1（principled tiebreaking）不成立。

  - name: sica_k_ablation_14b
    plan_id: exp-002
    description: >
      K sensitivity实验，在原60题上测试K=6,8,12,16,20（K=10为已有baseline）。
      检验SICA benefit是否随K变化呈现系统性pattern。
    expected_results:
      k_values: [6, 8, 10, 12, 16, 20]
      sica_acc_by_k: [0.717, 0.733, 0.733, 0.717, 0.700, 0.717]
      sc_acc_by_k: [0.700, 0.717, 0.700, 0.717, 0.717, 0.700]
      gap_pp_by_k: [1.7, 1.7, 3.3, 0.0, -1.7, 1.7]
      tie_freq_by_k: [0.25, 0.13, 0.10, 0.08, 0.05, 0.03]
      tie_win_rate_by_k: [0.53, 0.50, 0.67, 0.40, 0.33, 0.50]
      c0_by_k: [0.60, 0.55, 0.53, 0.50, 0.45, 0.42]
      correlation_k_vs_gap_r: 0.08
      correlation_k_vs_gap_p: 0.88
      correlation_tiefreq_vs_gap_r: 0.35
      correlation_tiefreq_vs_gap_p: 0.50
      k_ablation_correlation_r: 0.18
      wall_time_hours_total: 4.8
    result_rationale: >
      K增大时tie频率按预期下降（偶数K在K=6时~25%的题有tie，K=20时仅~3%），但SICA在tie上的
      win rate完全无pattern：K=10碰巧最高（67%=4/6 wins），K=16最低（33%=1/3）。
      这恰好说明win rate受极小样本量支配——每个K值下tie数量仅3-15个，任何单个K的win rate
      都无统计意义。Gap在-1.7到+3.3pp之间随机波动，与K无单调关系（r=0.08）。
      奇数K测试（如K=9,11）可完全消除ties，但本实验设计中未包含——这本身就暗示了
      SICA的整个contribution可以被"用奇数K"这个trivial baseline替代。
    tables:
      - caption: "Table 3: SICA vs SC across K values (60q, Qwen2.5-14B-Instruct)"
        columns: [K, SICA_Acc, SC_Acc, Gap_pp, N_ties, Tie_Win_Rate, C0]
        rows:
          - [6, 71.7, 70.0, "+1.7", 15, 0.53, 0.60]
          - [8, 73.3, 71.7, "+1.7", 8, 0.50, 0.55]
          - [10, 73.3, 70.0, "+3.3", 6, 0.67, 0.53]
          - [12, 71.7, 71.7, "0.0", 5, 0.40, 0.50]
          - [16, 70.0, 71.7, "-1.7", 3, 0.33, 0.45]
          - [20, 71.7, 70.0, "+1.7", 2, 0.50, 0.42]
    figures_description:
      - "Fig 3: 双Y轴折线图。X=K，左Y=SICA-SC gap(pp)，右Y=tie frequency。Gap随机波动（无趋势），tie freq单调下降。两者之间无因果关系的视觉暗示。"
      - "Fig 4: Scatter plot of tie_win_rate vs K with error bars (Wilson interval)。所有点的CI都跨越0.5线，无任何K值的win rate显著偏离随机。"
    analysis: >
      K消融彻底否定了"SICA benefit随K系统性变化"的假设。Gap序列[+1.7, +1.7, +3.3, 0.0, -1.7, +1.7]
      看起来就是围绕0的随机游走。K=10的+3.3pp是最大值纯属偶然。
      更致命的是：如果SICA真的通过constraint quality提供了principled tiebreaking，
      那么在tie更频繁的低K下（K=6, 15个tie），win rate应该收敛到一个>0.5的稳定值——
      但实际观察到的0.53与0.5无显著差异（p=0.65, one-sided binomial test）。
      Claim 1的tiebreaking机制在足够多的tie样本下仍然无法展示系统性优势。

  - name: tiebreak_baseline_analysis
    plan_id: exp-003
    description: >
      CPU-only reanalysis。在所有可用数据上比较SICA vs SC-random-tiebreak vs SC-deterministic。
      量化SICA的gain中有多少survives against fair random baseline。
    expected_results:
      # On original 60q
      orig60_sc_det_acc: 0.700
      orig60_sc_random_acc_mean: 0.711
      orig60_sc_random_acc_std: 0.018
      orig60_sica_acc: 0.733
      orig60_sica_vs_random_gap_pp: 2.2
      orig60_sica_vs_random_p: 0.29
      # On expanded 212q
      exp212_sc_det_acc: 0.703
      exp212_sc_random_acc_mean: 0.706
      exp212_sc_random_acc_std: 0.008
      exp212_sica_acc: 0.708
      exp212_sica_vs_random_gap_pp: 0.2
      exp212_sica_vs_random_p: 0.46
      # Tie-only analysis (212q)
      tie_n: 10
      tie_sica_correct: 5
      tie_random_expected_correct: 5.0
      tie_random_std: 1.1
      tiebreak_win_rate_vs_random: 0.50
    result_rationale: >
      SC-deterministic的tiebreak规则（alphabetical/first-encountered）在某些题上系统性偏差
      （比如"True"排在"False"前面），导致它在60q上比random低1.1pp。SICA看起来比SC-det
      好3.3pp，但其中~1pp来自"不用deterministic tiebreak"这个trivial改进。
      对比SC-random（公平baseline），SICA在60q上仅+2.2pp（p=0.29），在212q上仅+0.2pp（p=0.46）。
      换言之，SICA的实际contribution在扩展后与random tiebreak无法区分。
      这是最具破坏性的结果：SICA的整个pipeline（constraint extraction + MAX-SAT）
      在统计上不优于一个coin flip。
    tables:
      - caption: "Table 4: Three-way comparison — SICA vs SC-random vs SC-deterministic"
        columns: [Dataset, N, SC_Det, SC_Random_Mean, SICA, SICA_vs_Random_pp, p]
        rows:
          - [Original 60q, 60, 70.0, 71.1, 73.3, "+2.2", 0.29]
          - [Expanded 212q, 212, 70.3, 70.6, 70.8, "+0.2", 0.46]
          - [FOLIO 104q, 104, 76.9, 77.4, 78.8, "+1.4", 0.35]
          - [ProofWriter 108q, 108, 63.9, 64.0, 63.0, "-1.0", 0.67]
    figures_description:
      - "Fig 5: Bootstrap distribution图。三种方法的accuracy分布高度重叠。SICA的分布中心几乎与SC-random重合。"
    analysis: >
      引入SC-random baseline后，SICA的gain进一步缩水。在212q上+0.2pp vs random——
      这意味着整个constraint extraction + MAX-SAT pipeline（额外30%计算开销）的净效果
      等价于掷硬币。SC-deterministic之所以低，是因为alphabetical tie rule在FOLIO上
      系统性偏向"False"（而正确答案分布略偏"True"）。这是一个baseline artifact，
      不应归功于SICA的"principled"机制。

  - name: sica_7b_scaling
    plan_id: exp-004
    description: >
      Qwen2.5-7B-Instruct在60题上运行SICA。测试弱模型→高C0→更大SICA gain的假设。
    expected_results:
      n_combined: 60
      n_folio: 30
      n_proofwriter: 30
      c0_combined: 0.65
      c0_folio: 0.60
      c0_proofwriter: 0.70
      sc_acc_combined: 0.583
      sc_acc_folio: 0.667
      sc_acc_proofwriter: 0.500
      sica_acc_combined: 0.567
      sica_acc_folio: 0.633
      sica_acc_proofwriter: 0.500
      sica_sc_gap_pp: -1.7
      folio_gap_pp: -3.3
      proofwriter_gap_pp: 0.0
      bootstrap_p: 0.72
      c1_extraction_rate: 0.92
      constraint_quality_issues: 0.34
      total_constraints_raw: 4200
      total_constraints_unique: 1950
      maxsat_exclusion_rate: 0.068
      wall_time_min: 35
    result_rationale: >
      7B模型的C0=0.65（显著高于14B的0.53），验证了"弱模型更多样"的预测。
      但SICA反而亏了1.7pp。原因：高diversity来自reasoning errors而非legitimate alternative
      reasoning paths。7B的reasoning traces质量更低——FOL extraction的语义准确率仅~66%
      （vs 14B的~82%），导致constraint weighting将错误trace与正确trace等权对待甚至偏好错误trace。
      具体机制：7B在FOLIO上经常生成plausible-looking但logically flawed的推理链，
      这些链产生internally consistent但semantically wrong的constraints，MAX-SAT反而将
      它们的权重提升。这直接否定了"C0 as predictor"——高C0伴随的是constraint noise，
      不是constraint signal。Claim 2和Claim 3同时失败。
    tables:
      - caption: "Table 5: Model scaling — SICA effectiveness across model sizes"
        columns: [Model, Params, C0, SC_Acc, SICA_Acc, Gap_pp, p]
        rows:
          - [QwQ-32B, 32B, 0.036, 73.3, 73.3, "0.0", 0.50]
          - [Qwen2.5-14B-Instruct, 14B, 0.53, 70.0, 73.3, "+3.3", 0.23]
          - [Qwen2.5-7B-Instruct, 7B, 0.65, 58.3, 56.7, "-1.7", 0.72]
    figures_description:
      - "Fig 6: C0 vs SICA-SC gap scatter（3个model data points）。14B是唯一正向点，但仅3个点无法fit任何有意义的关系。7B的高C0对应负gap，直接反驳C0-as-predictor。"
    analysis: >
      7B实验是worst tier最致命的证据。它揭示了SICA方法论的根本缺陷：
      constraint extraction假设reasoning traces是formal proof的noisy version，
      但7B的traces根本不是——它们是pattern matching的output，其中的"logical structure"
      是superficial的。提取出的FOL constraints看起来像逻辑公式，但语义上经常是错的。
      MAX-SAT在garbage-in时给出garbage-out，甚至worse-than-garbage因为它给noisy constraints
      赋予了undeserved的confidence。这支持worst tier的核心reframing：
      symbolic extraction是category error。

  - name: c0_diagnostic_validation
    plan_id: exp-006
    description: >
      跨所有模型和K值绘制C0 vs SICA-SC gap。验证C0作为SICA部署决策predictor的有效性。
    expected_results:
      data_points: 9
      # (model, K, C0, gap_pp)
      scatter_data:
        - {model: "14B", k: 6, c0: 0.60, gap_pp: 1.7}
        - {model: "14B", k: 8, c0: 0.55, gap_pp: 1.7}
        - {model: "14B", k: 10, c0: 0.53, gap_pp: 3.3}
        - {model: "14B", k: 12, c0: 0.50, gap_pp: 0.0}
        - {model: "14B", k: 16, c0: 0.45, gap_pp: -1.7}
        - {model: "14B", k: 20, c0: 0.42, gap_pp: 1.7}
        - {model: "7B", k: 10, c0: 0.65, gap_pp: -1.7}
        - {model: "QwQ-32B", k: 10, c0: 0.036, gap_pp: 0.0}
        - {model: "14B-expanded", k: 10, c0: 0.47, gap_pp: 0.5}
      pearson_r: 0.22
      pearson_p: 0.57
      spearman_rho: 0.18
      spearman_p: 0.64
      linear_fit_r2: 0.05
      c0_threshold_analysis: >
        No threshold of C0 cleanly separates positive from negative SICA gaps.
        C0>0.5 includes both the best (+3.3pp at C0=0.53) and worst (-1.7pp at C0=0.65) outcomes.
    result_rationale: >
      C0测量的是vote diversity，但SICA gain需要的不仅是diversity——还需要constraint quality。
      C0无法区分"diverse because multiple valid reasoning paths"（SICA能帮忙的情况）
      和"diverse because model is confused"（SICA帮倒忙的情况）。
      在9个data points上，Pearson r=0.22（p=0.57），完全不显著。R²=0.05意味着C0仅解释
      5%的SICA gap方差。即使增加更多data points，趋势方向都不确定——
      7B的(C0=0.65, gap=-1.7)是一个强力反例，直接打破了C0→gain的单调假设。
      Claim 3（C0 as practical diagnostic）彻底不成立。
    tables:
      - caption: "Table 6: C0 vs SICA-SC gap across all conditions"
        columns: [Model, K, N, C0, SICA_Gap_pp, Constraint_Quality_Est]
        rows:
          - [Qwen2.5-14B, 6, 60, 0.60, "+1.7", 0.81]
          - [Qwen2.5-14B, 8, 60, 0.55, "+1.7", 0.82]
          - [Qwen2.5-14B, 10, 60, 0.53, "+3.3", 0.82]
          - [Qwen2.5-14B, 12, 60, 0.50, "0.0", 0.80]
          - [Qwen2.5-14B, 16, 60, 0.45, "-1.7", 0.79]
          - [Qwen2.5-14B, 20, 60, 0.42, "+1.7", 0.78]
          - [Qwen2.5-14B, 10, 212, 0.47, "+0.5", 0.80]
          - [Qwen2.5-7B, 10, 60, 0.65, "-1.7", 0.66]
          - [QwQ-32B, 10, 60, 0.036, "0.0", 0.91]
    figures_description:
      - "Fig 7: Scatter plot of C0 (x-axis) vs SICA-SC gap (y-axis) with linear regression line。R²=0.05，regression line几乎水平。7B点在右下（高C0，负gap），直观否定C0-as-predictor。不同model用不同marker，K variations用同色不同大小。"
      - "Fig 8: 添加constraint quality estimate作为color dimension的版本。Shows C0 alone insufficient——need C0×quality interaction，但这需要running SICA才能获得，defeating the purpose of a 'zero-cost predictor'。"
    analysis: >
      C0 diagnostic的失败有一个deeper insight：C0是一个necessary but not sufficient condition。
      C0≈0（QwQ）时SICA确实degenerates to SC（这部分成立），但C0>0时SICA是否有益
      取决于diversity的来源——是reasoning quality variation还是reasoning error variation。
      C0无法区分这两者。要做到这一点需要实际运行constraint extraction评估quality，
      但那样C0就不再是"zero-cost predictor"了。Claim 3的formulation从根本上有缺陷。

  - name: sica_72b_awq
    plan_id: exp-007
    description: >
      Qwen2.5-72B-Instruct AWQ 4-bit在60题上运行。Scaling analysis的最高点。
    expected_results:
      n_combined: 60
      c0_combined: 0.35
      c0_folio: 0.30
      c0_proofwriter: 0.40
      sc_acc_combined: 0.783
      sica_acc_combined: 0.783
      sica_sc_gap_pp: 0.0
      folio_sica: 0.867
      folio_sc: 0.867
      folio_gap_pp: 0.0
      proofwriter_sica: 0.700
      proofwriter_sc: 0.700
      proofwriter_gap_pp: 0.0
      tie_questions: 2
      tie_sica_wins: 1
      tie_sc_wins: 1
      tiebreak_win_rate: 0.50
      c1_extraction_rate: 0.98
      maxsat_exclusion_rate: 0.018
      wall_time_min: 82
    result_rationale: >
      72B是最强的instruction model，baseline accuracy最高（78.3% vs 14B的70.0%）。
      C0=0.35——比14B低（0.53），因为更强的模型更自洽，但仍远高于QwQ（0.036）。
      尽管C0>0且constraint quality应该最高（最强的instruction model），gap仍然精确为0pp。
      仅2个tie，1:1 split。这个结果对SICA特别不利：即使在constraint quality最好的条件下
      （72B的traces最接近"formal proof的noisy version"这一假设），SICA仍然无法提供任何改进。
      这说明问题不仅是constraint quality——即使constraints是好的，MAX-SAT reweighting
      在非tie情况下也无法翻转majority vote（因为正确answer通常已经是majority）。
    tables:
      - caption: "Table 7: Full model scaling analysis"
        columns: [Model, Params, Type, C0, SC_Acc, SICA_Acc, Gap_pp, N_ties]
        rows:
          - [QwQ-32B, 32B, Reasoning, 0.036, 73.3, 73.3, "0.0", 0]
          - [Qwen2.5-72B-AWQ, 72B, Instruction, 0.35, 78.3, 78.3, "0.0", 2]
          - [Qwen2.5-14B, 14B, Instruction, 0.53, 70.0, 73.3, "+3.3", 6]
          - [Qwen2.5-7B, 7B, Instruction, 0.65, 58.3, 56.7, "-1.7", 18]
    figures_description:
      - "Fig 9: Model size (x-axis, log scale) vs SICA-SC gap (y-axis)。仅14B显示正向gap，其他三个model都是0或负。Inverted-U shape if you squint，但更准确的描述是'random noise around 0 with one lucky outlier'。"
    analysis: >
      72B数据加上7B形成了一个完整的反驳叙事：
      7B（C0=0.65）→ gap=-1.7pp（constraints太noisy，SICA反而有害）
      14B（C0=0.53）→ gap=+3.3pp（60q上看起来有效，212q上缩减到+0.5pp）
      72B（C0=0.35）→ gap=0.0pp（constraints好但tie太少，无施展空间）
      QwQ（C0=0.04）→ gap=0.0pp（无diversity，SICA≡SC）
      不存在任何model regime where SICA systematically helps。14B在60q上的+3.3pp
      是四个model中唯一的正值，且已被exp-001证明是noise。

  - name: constraint_quality_case_studies
    plan_id: exp-008
    description: >
      对10道代表性题目进行constraint extraction质量的定性分析。分类failure modes。
    expected_results:
      n_case_studies: 10
      n_folio: 5
      n_proofwriter: 5
      failure_mode_taxonomy:
        semantic_error_rate: 0.31
        paraphrase_duplication_rate: 0.22
        tautological_constraint_rate: 0.15
        answer_leakage_rate: 0.08
        irrelevant_constraint_rate: 0.18
        clean_constraint_rate: 0.38
      case_study_summaries:
        - id: "folio_q12"
          issue: "Semantic error"
          detail: "Model translates 'All birds can fly' as ∀x(Bird(x)→Fly(x)) but context implies penguins are birds. Extraction misses implicit domain restriction."
        - id: "folio_q47"
          issue: "Paraphrase duplication"
          detail: "Same constraint extracted 4 times in slightly different variable names (x vs y vs z). MAX-SAT over-weights this constraint, creating artificial consensus for wrong answer."
        - id: "pw_q23"
          issue: "Tautological"
          detail: "Extracted constraint 'A→A' contributes nothing but consumes MAX-SAT budget."
        - id: "folio_q31"
          issue: "Answer leakage"
          detail: "Constraint directly encodes the model's final answer rather than intermediate reasoning. MAX-SAT just reconstructs majority vote with extra steps."
        - id: "pw_q45"
          issue: "Wrong FOL structure"
          detail: "Nested quantifier scope error: ∃x∀y should be ∀y∃x. Flipped scope changes truth value, incorrect constraint gets high weight."
      constraint_accuracy_by_model:
        qwen_14b: 0.69
        qwen_7b: 0.52
        qwq_32b: 0.85
    result_rationale: >
      定性分析揭示了SICA方法论的根本问题：LLM reasoning traces不是formal proofs，
      从中提取的FOL constraints继承了traces的所有缺陷并引入了新的extraction artifacts。
      五类failure modes：
      (1) Semantic errors (31%)——FOL translation与natural language meaning不匹配；
      (2) Paraphrase duplication (22%)——同一约束被提取多次导致MAX-SAT过度加权；
      (3) Tautologies (15%)——无信息量的constraints浪费MAX-SAT capacity；
      (4) Answer leakage (8%)——constraint直接编码答案而非推理结构，MAX-SAT退化为fancy voting；
      (5) Irrelevant (18%)——与题目答案无关的constraints。
      仅38%的constraints是clean的。这解释了为什么MAX-SAT reweighting无法系统性改进结果——
      它在用noisy signals去reweight已经noisy的votes。
    tables:
      - caption: "Table 8: Constraint failure mode taxonomy"
        columns: [Failure_Mode, Frequency, Impact_on_SICA, Example]
        rows:
          - [Semantic Error, "31%", "Misweights traces based on incorrect logic", "∀x(Bird→Fly) missing domain restriction"]
          - [Paraphrase Duplication, "22%", "Over-weights repeated constraints", "Same fact with different variable names"]
          - [Tautological, "15%", "Dilutes signal-to-noise ratio", "A→A type constraints"]
          - [Answer Leakage, "8%", "SICA degenerates to weighted vote", "Constraint encodes final answer directly"]
          - [Irrelevant, "18%", "Adds noise to MAX-SAT objective", "Constraints about unused premises"]
          - [Clean, "38%", "Intended behavior", "Correctly captures reasoning step"]
    figures_description:
      - "Fig 10: Pie chart of constraint failure modes。Clean constraints仅38%——majority of extracted information is noise。"
      - "Fig 11: Side-by-side对比：原始reasoning trace → extracted FOL → ground truth FOL（人工标注）for 3 representative examples。Visual demonstration of extraction noise。"
    analysis: >
      这是worst tier paper的核心贡献。Failure mode taxonomy将"SICA doesn't work"的
      observational claim升级为"here's exactly why it doesn't work"的mechanistic explanation。
      最重要的insight是answer leakage (8%)和paraphrase duplication (22%)的组合效应：
      当constraints直接编码答案（leakage）且同一答案的constraints被重复计数（duplication），
      MAX-SAT实质上在做一个biased version of majority vote——不是principled reweighting，
      而是amplified echo。这支持了reframing的核心论点：symbolic extraction是category error。
      LLM traces的"逻辑结构"是surface-level pattern，不是可靠的formal objects。

  - name: overhead_analysis
    plan_id: exp-009
    description: >
      Wall-time breakdown分析。量化SICA相对于plain SC的计算开销。
    expected_results:
      per_question_breakdown_14b:
        generation_s: 42.3
        constraint_extraction_s: 11.8
        fol_parsing_s: 1.2
        maxsat_solving_s: 0.9
        io_overhead_s: 2.1
        total_sica_s: 58.3
        total_sc_s: 42.3
        overhead_pct: 37.8
      per_question_breakdown_7b:
        generation_s: 28.5
        constraint_extraction_s: 9.2
        fol_parsing_s: 0.8
        maxsat_solving_s: 0.7
        io_overhead_s: 1.5
        total_sica_s: 40.7
        total_sc_s: 28.5
        overhead_pct: 42.8
      per_question_breakdown_72b:
        generation_s: 78.4
        constraint_extraction_s: 14.6
        fol_parsing_s: 1.5
        maxsat_solving_s: 1.1
        io_overhead_s: 2.8
        total_sica_s: 98.4
        total_sc_s: 78.4
        overhead_pct: 25.5
      accuracy_per_second_14b:
        sc: 0.01655
        sica: 0.01214
      accuracy_per_second_ratio: 0.73
    result_rationale: >
      SICA的overhead主要来自constraint extraction（需要额外LLM调用将reasoning traces
      翻译为FOL）。MAX-SAT solving本身很快（<1s/question），但extraction需要~12s/question
      （14B情况下）。总overhead约38%。在worst tier下，这38%的额外计算换来的是+0.5pp
      （212q）或-1.7pp（7B）的"改进"——accuracy-per-compute严格劣于plain SC。
      即使在best case（14B 60q, +3.3pp），cost-effectiveness也很差：
      每1pp的gain需要额外13%的计算（3.3pp / 37.8% overhead ≈ 0.087 pp/% overhead），
      而且这个gain在扩展后消失了。
    tables:
      - caption: "Table 9: SICA overhead analysis"
        columns: [Model, SC_Time_s, SICA_Time_s, Overhead_pct, Gap_pp, pp_per_overhead_pct]
        rows:
          - [Qwen2.5-14B (60q), 42.3, 58.3, "37.8%", "+3.3", 0.087]
          - [Qwen2.5-14B (212q), 42.3, 58.3, "37.8%", "+0.5", 0.013]
          - [Qwen2.5-7B, 28.5, 40.7, "42.8%", "-1.7", -0.040]
          - [Qwen2.5-72B-AWQ, 78.4, 98.4, "25.5%", "0.0", 0.000]
      - caption: "Table 10: Wall-time breakdown (per question, seconds)"
        columns: [Component, 7B, 14B, 72B]
        rows:
          - [Generation (shared w/ SC), 28.5, 42.3, 78.4]
          - [Constraint Extraction, 9.2, 11.8, 14.6]
          - [FOL Parsing, 0.8, 1.2, 1.5]
          - [MAX-SAT Solving, 0.7, 0.9, 1.1]
          - [I/O Overhead, 1.5, 2.1, 2.8]
          - [Total SICA-only, 12.2, 16.0, 20.0]
    figures_description:
      - "Fig 12: Stacked bar chart showing per-question time breakdown。Generation dominates (>70%)，但SICA-specific components (extraction+solving) 仍占25-30%的额外开销，且不带来accuracy gain。"
      - "Fig 13: Cost-effectiveness scatter: x=overhead%, y=gap_pp。所有点都在低效区域（高overhead，低或负gain）。与理想对角线（high gain, low overhead）距离遥远。"
    analysis: >
      Overhead analysis在worst tier下变成一个argument amplifier：不仅gap不显著，
      而且为了获得这个不显著的gap付出了38%的额外计算。
      Accuracy-per-compute ratio: SC在14B上每秒产出0.0166%的accuracy，
      SICA仅0.0121%——SICA严格不如SC efficient。
      对于negative result paper，这个数据支持一个constructive recommendation：
      如果有38%的额外compute budget，更好的用法是增加K（从10到14），
      这在SC框架内就能获得更稳定的majority vote，而无需引入constraint extraction的noise。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "856a2722-fdc7-4302-859a-2a361ca4d6f7",
  "isSidechain": false,
  "requestId": "req_011Cb5h5qGQiqzwLVS3WDWkB",
  "type": "assistant",
  "uuid": "b6b260d5-fbcf-4bd3-9b1f-d92aaa4c739c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "8c675d3e-c565-4a79-b341-e83a7a48d4d6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155NEi95pc6dnctRvVdDyHU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11126,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15109,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11126,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15109,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11126
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：扩展后SICA-SC gap消失或反转——60q的+3.3pp是小样本噪声，tiebreaking无系统性优势 核心假设：['FOLIO扩展后gap缩小到<2pp，部分新题SICA反而输（constraint extraction引入噪声）', 'ProofWriter仍0pp或轻微负向', 'Combin…",
  "leafUuid": "b6b260d5-fbcf-4bd3-9b1f-d92aaa4c739c",
  "sessionId": "8c675d3e-c565-4a79-b341-e83a7a48d4d6"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Negative result analysis on symbolic constraint consensus",
  "sessionId": "8c675d3e-c565-4a79-b341-e83a7a48d4d6"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：扩展后SICA-SC gap消失或反转——60q的+3.3pp是小样本噪声，tiebreaking无系统性优势 核心假设：['FOLIO扩展后gap缩小到<2pp，部分新题SICA反而输（constraint extraction引入噪声）', 'ProofWriter仍0pp或轻微负向', 'Combin…",
  "leafUuid": "b6b260d5-fbcf-4bd3-9b1f-d92aaa4c739c",
  "sessionId": "8c675d3e-c565-4a79-b341-e83a7a48d4d6"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Negative result analysis on symbolic constraint consensus",
  "sessionId": "8c675d3e-c565-4a79-b341-e83a7a48d4d6"
}
```

---
