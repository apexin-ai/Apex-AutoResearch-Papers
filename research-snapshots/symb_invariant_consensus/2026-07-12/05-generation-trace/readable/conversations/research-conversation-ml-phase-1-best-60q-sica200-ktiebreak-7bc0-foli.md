# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：扩展实验复现并放大60q趋势：SICA在200+问题上达到统计显著，K消融揭示清晰的tiebreak频率机制，7B验证C0预测器 核心假设：['FOLI

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/52123d52-397d-4387-94d9-355bd36d3839.jsonl`
- **Structured JSON:** [`2d71f8e32008c3789171.json`](../../sessions/2d/2d71f8e32008c3789171.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T05:18:04.647Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T05:18:04.647Z",
  "sessionId": "52123d52-397d-4387-94d9-355bd36d3839",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：扩展实验复现并放大60q趋势：SICA在200+问题上达到统计显著，K消融揭示清晰的tiebreak频率机制，7B验证C0预测器\n核心假设：['FOLIO +6.7pp在~100问题上保持或扩大（tiebreak不是60q采样噪声）', \"ProofWriter在扩展数据上出现正向gap（≥1pp），消除'单域有效'攻击面\", 'K消融显示偶数K→更多tie→更大SICA增益的单调关系，奇数K增益消失（机制证据）', '7B模型C0>60%且SICA-SC gap > 14B的gap，验证C0-as-predictor因果方向']\n关键指标范围：{'combined_gap_pp': [3.0, 5.5], 'folio_gap_pp': [5.0, 8.0], 'proofwriter_gap_pp': [1.0, 3.0], 'bootstrap_p_combined': [0.01, 0.05], 'c0_14b': [0.45, 0.6], 'c0_7b': [0.6, 0.75], 'c0_qwq': [0.0, 0.05], 'sica_7b_gap_pp': [4.0, 8.0], 'tiebreak_win_rate': [0.7, 0.85], 'k_ablation_correlation_r': [0.7, 0.95]}\n叙事方向：原始framing完全成立。三条claim均有统计支撑：(1) SICA在200+问题上显著优于SC， tiebreaking机制通过K消融得到因果验证；(2) operating regime通过14B/7B/QwQ三点 清晰划分，C0阈值20%有实证支撑；(3) C0作为zero-cost predictor在3个模型上 展现强相关。论文以\"When Does Symbolic Consensus Help?\"为主线， tiebreaking是mechanism section，operating regime是main contribution， C0是practical takeaway。EMNLP主会完全够格。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\nfocus: Key tension: SICA's gain is entirely from principled tiebreaking (4/60 questions, all 6:6 ties). Reviewers will attack statistical significance (p=0.317) and question overhead vs benefit. The operating regime characterization (reasoning vs instruction model) is the primary intellectual contribution. Expanded 200+ question results and K ablation are planned but not yet available. ProofWriter shows 0pp gain — domain generalization is a weakness.\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Fallback: AAAI 2027 (Aug 1)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条)\n1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).\n2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is conditional on trace diversity — SICA adds value when model outputs are diverse (instruction models, C0>20%) but provably degenerates to SC when models are self-consistent (reasoning models, C0<5%). This is a model property, not a task property.\n3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.\n\n## Core Insight\nSymbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that model architecture (reasoning vs instruction) determines the operating regime. This transforms SICA from \"yet another ensemble method\" into \"a method with formally characterizable applicability boundaries.\"\n\n## Story Spine\n- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.\n- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.\n- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75% win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) and show it's governed by model type, not task type.\n- **Headline result template**: \"On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → exp-001: Expand to 200+ questions for statistical power\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K sensitivity showing benefit pattern; exp-009: overhead analysis\n3. **\"Only one non-reasoning model\"** → exp-004: Add Qwen2.5-7B for scaling; exp-007: 72B-AWQ for camera-ready\n4. **\"ProofWriter shows 0pp gain\"** → Domain analysis in exp-001 expanded results\n5. **\"Random tiebreak baseline closes the gap\"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison\n6. **\"Why not just use a reasoning model?\"** → exp-005: QwQ-32B data shows reasoning models are self-consistent (don't need consensus improvement), but instruction models (cheaper, more deployed) benefit from SICA\n\n## Venue Fit Risks\n- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the \"operating regime characterization\" — the tiebreaking mechanism is evidence, not the claim.\n- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.\n- Negative results: QwQ-32B data must be presented as insight (\"When Does Symbolic Consensus Degenerate?\"), not failure.\n- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: Expand D012 from 60 to 200+ questions (PW D5 ~100 + FOLIO ~100) for\n    statistical power on C3. Merge with D012 data for combined analysis.\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  status: planned\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,12,16,20) on D012''s 60 questions. Key questions:\n    does SICA benefit depend on tiebreaks? What happens at odd K (no even splits)?\n    How does tiebreak frequency change with K?'\n  priority: P0\n  gpu_budget_hours: 5\n  deps: []\n  status: planned\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: sica_d012_14b\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. For camera-ready if time permits.'\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T05:18:04.652Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T05:18:04.652Z",
  "sessionId": "52123d52-397d-4387-94d9-355bd36d3839"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T05:18:04.693Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：扩展实验复现并放大60q趋势：SICA在200+问题上达到统计显著，K消融揭示清晰的tiebreak频率机制，7B验证C0预测器
核心假设：['FOLIO +6.7pp在~100问题上保持或扩大（tiebreak不是60q采样噪声）', "ProofWriter在扩展数据上出现正向gap（≥1pp），消除'单域有效'攻击面", 'K消融显示偶数K→更多tie→更大SICA增益的单调关系，奇数K增益消失（机制证据）', '7B模型C0>60%且SICA-SC gap > 14B的gap，验证C0-as-predictor因果方向']
关键指标范围：{'combined_gap_pp': [3.0, 5.5], 'folio_gap_pp': [5.0, 8.0], 'proofwriter_gap_pp': [1.0, 3.0], 'bootstrap_p_combined': [0.01, 0.05], 'c0_14b': [0.45, 0.6], 'c0_7b': [0.6, 0.75], 'c0_qwq': [0.0, 0.05], 'sica_7b_gap_pp': [4.0, 8.0], 'tiebreak_win_rate': [0.7, 0.85], 'k_ablation_correlation_r': [0.7, 0.95]}
叙事方向：原始framing完全成立。三条claim均有统计支撑：(1) SICA在200+问题上显著优于SC， tiebreaking机制通过K消融得到因果验证；(2) operating regime通过14B/7B/QwQ三点 清晰划分，C0阈值20%有实证支撑；(3) C0作为zero-cost predictor在3个模型上 展现强相关。论文以"When Does Symbolic Consensus Help?"为主线， tiebreaking是mechanism section，operating regime是main contribution， C0是practical takeaway。EMNLP主会完全够格。


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
  "promptId": "e0db4bac-3dc0-4876-9925-5659890d7364",
  "type": "user",
  "uuid": "ba665013-a022-4fd3-af6d-cdf3a13aa372",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "52123d52-397d-4387-94d9-355bd36d3839",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T05:18:04.691Z_

```json
{
  "parentUuid": "ba665013-a022-4fd3-af6d-cdf3a13aa372",
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
  "uuid": "66362f47-93bd-4caf-a596-a4a2788ab870",
  "timestamp": "2026-05-16T05:18:04.691Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "52123d52-397d-4387-94d9-355bd36d3839",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T05:18:04.691Z_

```json
{
  "parentUuid": "66362f47-93bd-4caf-a596-a4a2788ab870",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "09d7eca3-bf3c-426b-90d9-5a693bad4daa",
  "timestamp": "2026-05-16T05:18:04.691Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "52123d52-397d-4387-94d9-355bd36d3839",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：扩展实验复现并放大60q趋势：SICA在200+问题上达到统计显著，K消融揭示清晰的tiebreak频率机制，7B验证C0预测器 核心假设：['FOLIO +6.7pp在~100问题上保持或扩大（tiebreak不是60q采样噪声）', \"ProofWriter在扩展数据上出现正向gap（≥1pp），消除'单…",
  "leafUuid": "09d7eca3-bf3c-426b-90d9-5a693bad4daa",
  "sessionId": "52123d52-397d-4387-94d9-355bd36d3839"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 Best-Case Scenario Detailed Predictions",
  "sessionId": "52123d52-397d-4387-94d9-355bd36d3839"
}
```

---

### Assistant

_source line 8 · 2026-05-16T05:18:20.899Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment plan, under the "best" tier scenario. I need to produce a YAML block with imagined experiments, each with expected results, rationale, tables, figures, and analysis.

Let me carefully go through each planned experiment and generate predictions consistent with the "best" tier definition.

The best tier says:
- FOLIO +6.7pp holds or expands on ~100 questions
- ProofWriter shows positive gap ≥1pp
- K ablation shows even K → more ties → more SICA gain, odd K gain disappears


- 7B model C0 exceeds 60% with SICA-SC gap larger than 14B's, combined gap ranging 3.0-5.5pp across benchmarks, FOLIO gap 5.0-8.0pp, ProofWriter gap 1.0-3.0pp, and bootstrap p-values between 0.01-0.05 for combined results
- 14B C0 baseline 0.45-0.6, 7B C0 baseline 0.6-0.75, QwQ C0 near zero at 0.0-0.05, with 7B SICA gap 4.0-8.0pp and tiebreak win rate 0.7-0.85
- K ablation shows strong correlation of 0.7-0.95, and I'm planning nine experiments: expanding SICA to 200+ questions, testing K sensitivity, comparing tiebreak strategies, scaling to 7B and 72B models, validating C0 diagnostics, and conducting qualitative case studies on constraint quality

. Exp-005 with QwQ-32B is already complete, so I'll note that and move forward with detailed predictions for the remaining ones, including overhead analysis for wall-time breakdown.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09d7eca3-bf3c-426b-90d9-5a693bad4daa",
  "isSidechain": false,
  "requestId": "req_011Cb5gWb4iqi6Tq4nfSabJk",
  "type": "assistant",
  "uuid": "c7dde4f3-36ed-4a8f-b752-5075783ecec1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "52123d52-397d-4387-94d9-355bd36d3839",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174gkwPNpSxgUoqfBDYk6tH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11013,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11013,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11411,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11013,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11013
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

_source line 9 · 2026-05-16T05:22:04.667Z_

```yaml
tier: best
narrative_guidance: >
  原始framing完全成立。三条claim均有统计支撑：(1) SICA在200+问题上显著优于SC，
  tiebreaking机制通过K消融得到因果验证；(2) operating regime通过14B/7B/QwQ三点
  清晰划分，C0阈值20%有实证支撑；(3) C0作为zero-cost predictor在3个模型上
  展现强相关。论文以"When Does Symbolic Consensus Help?"为主线，
  tiebreaking是mechanism section，operating regime是main contribution，
  C0是practical takeaway。EMNLP主会完全够格。

imagined_experiments:
  - name: "sica_expanded_14b"
    plan_id: "exp-001"
    description: >
      在Qwen2.5-14B-Instruct上将评估集从60题扩展到204题（FOLIO 102题 + ProofWriter D5 102题），
      K=12, T=0.7。与D012的60题数据合并做统计检验。
    expected_results:
      n_total: 204
      n_folio: 102
      n_proofwriter: 102
      K: 12
      sica_accuracy_combined: 0.745
      sc_accuracy_combined: 0.706
      sica_sc_gap_pp_combined: 3.9
      folio_sica: 0.794
      folio_sc: 0.725
      folio_gap_pp: 6.9
      proofwriter_sica: 0.696
      proofwriter_sc: 0.686
      proofwriter_gap_pp: 1.0
      c0_combined: 0.51
      c0_folio: 0.54
      c0_proofwriter: 0.48
      bootstrap_p_combined: 0.023
      bootstrap_p_folio: 0.018
      bootstrap_p_proofwriter: 0.34
      tiebreak_questions: 17
      tiebreak_sica_wins: 13
      tiebreak_sica_win_rate: 0.765
      c1_extraction_rate: 0.98
      c2_contradiction_problems: 112
      maxsat_exclusion_rate: 0.031
      wall_time_min: 210
    result_rationale: >
      60题D012中FOLIO的+6.7pp来自4/30题的tiebreak翻转。在102题上，tiebreak事件按比例
      出现约8-9次（C0≈54%意味着约55题有多候选，其中K=12时约15%形成精确tie），
      SICA在其中约76%的case胜出（MAX-SAT权重正确选择了约束更一致的答案）。
      6.9pp的gap略高于60题的6.7pp，因为更大样本包含了更多FOLIO中语义复杂的多步推理题，
      这些题上14B的trace多样性更高（更多tie机会）。ProofWriter从0pp上升到1.0pp：
      D012的30题PW结果为0pp并非PW上SICA无效，而是30题中碰巧没有tiebreak翻转成功。
      扩展到102题后，约4-5个PW tiebreak中有2-3个SICA胜出，产生了小但正的gap。
      PW的gap小于FOLIO因为PW的推理链结构更模板化（depth-5推理步骤较固定），
      导致即使有多候选，约束质量的区分度不如FOLIO的自然语言推理场景。
      合并204题的bootstrap p=0.023达到p<0.05，因为FOLIO的强信号主导了combined结果。
      PW单独的p=0.34未达显著——这是预期的，论文中呈现为"正向趋势但需更大样本确认"，
      重点放在combined和FOLIO的显著性上。
    tables:
      - name: "Table 1: SICA vs SC Accuracy (Expanded, N=204)"
        columns: ["Dataset", "N", "SC Acc", "SICA Acc", "Gap (pp)", "p-value", "C0"]
        rows:
          - ["FOLIO", 102, 0.725, 0.794, "+6.9", 0.018, 0.54]
          - ["ProofWriter-D5", 102, 0.686, 0.696, "+1.0", 0.34, 0.48]
          - ["Combined", 204, 0.706, 0.745, "+3.9", 0.023, 0.51]
      - name: "Table 2: Tiebreak Analysis"
        columns: ["Metric", "Value"]
        rows:
          - ["Total questions with ties (K=12)", 17]
          - ["SICA wins on ties", 13]
          - ["SC wins on ties", 4]
          - ["SICA tiebreak win rate", "76.5%"]
          - ["SICA gain from non-tie questions", "0.0pp"]
    figures_description:
      - "Figure 1: Per-question SICA-SC accuracy difference heatmap (204题), 按C0排序。清晰可见C0>0.5区域集中了所有正向gain，C0=0区域SICA≡SC。"
      - "Figure 2: Bootstrap distribution of SICA-SC gap (10000 resamples), combined和FOLIO两个panel。FOLIO的95% CI完全在0以上 [+1.8, +12.1]，combined的CI为 [+0.5, +7.3]。"
    analysis: >
      这是论文的基础实验。204题的p=0.023确立了统计显著性，彻底解决了60题p=0.317的脆弱性问题。
      关键发现：SICA的gain 100%来自tiebreak问题——在非tie问题上SICA与SC答案完全一致。
      这不是弱点而是机制清晰性的证据：SICA是principled tiebreaker，不是magic ensemble。
      ProofWriter的+1.0pp虽小但为正，消除了"单域有效"的攻击面。论文中可以说
      "SICA在两个逻辑推理benchmark上均展现正向gain，在FOLIO上达到统计显著"。

  - name: "sica_k_ablation_14b"
    plan_id: "exp-002"
    description: >
      在D012的60题上测试K=6,8,12,16,20五个值（加上已有K=12作为baseline），
      分析tiebreak频率与SICA gain的关系。重点：偶数K vs 奇数K（如果加入K=9,11对比）。
    expected_results:
      k_values_tested: [6, 8, 12, 16, 20]
      results_by_k:
        k6:
          sica_acc: 0.717
          sc_acc: 0.683
          gap_pp: 3.4
          tie_count: 6
          tie_sica_wins: 5
          c0: 0.50
        k8:
          sica_acc: 0.733
          sc_acc: 0.700
          gap_pp: 3.3
          tie_count: 5
          tie_sica_wins: 4
          c0: 0.52
        k12:
          sica_acc: 0.733
          sc_acc: 0.700
          gap_pp: 3.3
          tie_count: 4
          tie_sica_wins: 3
          c0: 0.53
        k16:
          sica_acc: 0.750
          sc_acc: 0.700
          gap_pp: 5.0
          tie_count: 7
          tie_sica_wins: 6
          c0: 0.55
        k20:
          sica_acc: 0.750
          sc_acc: 0.717
          gap_pp: 3.3
          tie_count: 5
          tie_sica_wins: 4
          c0: 0.55
      correlation_tiecount_vs_gap_r: 0.82
      correlation_k_vs_c0_r: 0.88
      odd_k_test_k9:
        gap_pp: 0.0
        tie_count: 0
        note: "奇数K下majority vote无精确tie，SICA≡SC"
      wall_time_hours: 4.5
    result_rationale: >
      tiebreak频率机制的因果检验。偶数K产生精确tie的概率取决于K和候选分布：
      K=6时，2候选各3票的概率较高（C(6,3)×0.5^6≈31%对于50/50 split），产生约6个tie；
      K=8时概率略降（C(8,4)×0.5^8≈27%），但更多trace采样使C0略升，tie仍有5个；
      K=16时，虽然单题精确tie概率降低（C(16,8)×0.5^16≈20%），但更多trace带来
      更多多候选问题（C0升至0.55），且tie时SICA有更多约束可用（16条trace的MAX-SAT
      比6条更robust），win rate从K=6的83%升至K=16的86%。K=20时SC自身精度也上升
      （更多vote趋向正确答案），gap回落。关键机制证据：K=9（奇数）时tie=0，gap=0，
      因为majority vote在奇数K下总有唯一赢家，SICA无介入空间。这是最干净的因果证据——
      同样的数据、同样的模型，仅K的奇偶性就决定了SICA是否有gain。
      r=0.82的tiecount-gap相关说明SICA gain几乎完全由tiebreak频率驱动。
    tables:
      - name: "Table 3: K Ablation Results (N=60, 14B-Instruct)"
        columns: ["K", "SC Acc", "SICA Acc", "Gap (pp)", "Ties", "SICA Tie Wins", "C0"]
        rows:
          - [6, 0.683, 0.717, "+3.4", 6, 5, 0.50]
          - [8, 0.700, 0.733, "+3.3", 5, 4, 0.52]
          - ["9 (odd)", 0.700, 0.700, "0.0", 0, "N/A", 0.52]
          - [12, 0.700, 0.733, "+3.3", 4, 3, 0.53]
          - [16, 0.700, 0.750, "+5.0", 7, 6, 0.55]
          - [20, 0.717, 0.750, "+3.3", 5, 4, 0.55]
    figures_description:
      - "Figure 3a: 柱状图——tiebreak count vs K值。偶数K均有ties，K=9处ties=0（红色标注）。视觉上立即传达奇偶效应。"
      - "Figure 3b: 散点图——tiebreak frequency vs SICA-SC gap (pp)，标注r=0.82。每个点是一个K值。奇数K点在原点。线性趋势线清晰。"
      - "Figure 3c: SICA tiebreak win rate vs K。随K增大win rate微升（更多约束→更robust的MAX-SAT决策），但主要效应是tie frequency而非win rate。"
    analysis: >
      K消融提供了SICA机制的因果证据链：(1) SICA gain完全来自tiebreak（非tie问题gap=0）；
      (2) tiebreak频率由K的奇偶性和多候选率共同决定；(3) SICA在tie上的win rate>75%
      说明MAX-SAT权重确实在做有意义的约束聚合而非随机选择。
      论文中这构成Mechanism Section的核心：从"SICA works"到"we know WHY it works"。
      reviewer如果问"isn't this just a better coin flip"，K=9的零gain数据是决定性反驳——
      如果SICA有tie以外的gain通道，奇数K应该也有非零gap。

  - name: "tiebreak_baseline_analysis"
    plan_id: "exp-003"
    description: >
      在所有可用数据上比较三种tiebreak策略：SICA (MAX-SAT weighted)、SC-random（随机打破tie）、
      SC-deterministic（按字母序/固定规则打破tie）。CPU-only重分析。
    expected_results:
      n_total_60q: 60
      n_tie_questions_60q: 4
      sica_acc_on_ties: 0.75
      sc_random_acc_on_ties: 0.375
      sc_deterministic_acc_on_ties: 0.25
      sica_overall: 0.733
      sc_random_overall: 0.717
      sc_deterministic_overall: 0.700
      sica_vs_random_gap_pp: 1.6
      sica_vs_deterministic_gap_pp: 3.3
      n_total_204q: 204
      n_tie_questions_204q: 17
      sica_acc_on_ties_204q: 0.765
      sc_random_acc_on_ties_204q: 0.412
      sc_random_acc_on_ties_204q_std: 0.08
      sc_deterministic_acc_on_ties_204q: 0.294
      sica_vs_random_gap_pp_204q: 2.9
      sica_vs_deterministic_gap_pp_204q: 3.9
      random_baseline_bootstrap_p: 0.041
      monte_carlo_runs_for_random: 1000
    result_rationale: >
      SC-deterministic在60题数据上是现有baseline（alphabetical tiebreak），已知tie上只有1/4正确。
      SC-random的期望准确率等于tie选项中正确答案的比例：4个tie问题中，如果每题是2候选
      50/50 split，random的期望准确率=0.5×(正确答案在候选中的概率)。但实际上部分tie
      的候选答案不是均匀分布（有些tie是3路tie），使得random的期望值约37.5%。
      SICA在tie上75%（3/4）显著高于random的37.5%，说明MAX-SAT权重不只是比random好，
      而是捕捉了约束结构中的真实信号。在204题上，17个tie中SICA赢13个（76.5%），
      random的蒙特卡洛模拟（1000次）显示均值41.2%±8%，SICA显著优于random（p=0.041）。
      gap从+1.6pp（vs random）到+3.9pp（vs deterministic），说明SICA gain的约55%
      来自"比random好"（MAX-SAT的真实贡献），45%来自"random比deterministic好"
      （deterministic的选择恰好偏向错误答案）。论文需要报告vs random的gap作为
      SICA overhead的实际回报。
    tables:
      - name: "Table 4: Tiebreak Strategy Comparison (60q / 204q)"
        columns: ["Strategy", "Tie Acc (60q)", "Overall (60q)", "Tie Acc (204q)", "Overall (204q)"]
        rows:
          - ["SC-deterministic", "25.0%", "70.0%", "29.4%", "70.6%"]
          - ["SC-random (E[·])", "37.5%", "71.7%", "41.2±8%", "72.0%"]
          - ["SICA (MAX-SAT)", "75.0%", "73.3%", "76.5%", "74.5%"]
    figures_description:
      - "Figure 4: 三种tiebreak策略在tie问题上的准确率对比（bar chart with error bars for random）。SICA bar显著高于random的CI上界。"
    analysis: >
      直接回应"random tiebreak closes the gap"的reviewer concern。数据显示：
      (1) SICA vs random仍有显著gap（+2.9pp on 204q, p=0.041），说明MAX-SAT权重
      确实提取了有用信号；(2) 即使承认部分gain来自"确定性tiebreak恰好差"，
      SICA vs random的+2.9pp仍然是实质性改进；(3) 这进一步支持mechanism story——
      约束权重区分了推理质量高的trace和低的trace。

  - name: "sica_7b_scaling"
    plan_id: "exp-004"
    description: >
      在Qwen2.5-7B-Instruct上运行SICA，使用exp-001相同的问题集（或至少60题subset），
      K=12, T=0.7。验证：弱模型→更高C0→更大SICA gain。
    expected_results:
      model: "Qwen2.5-7B-Instruct"
      n_total: 60
      K: 12
      sica_accuracy: 0.617
      sc_accuracy: 0.550
      sica_sc_gap_pp: 6.7
      c0_multi_candidate_rate: 0.68
      c1_extraction_rate: 0.93
      c2_contradiction_problems: 38
      folio_sica: 0.633
      folio_sc: 0.567
      folio_gap_pp: 6.6
      proofwriter_sica: 0.600
      proofwriter_sc: 0.533
      proofwriter_gap_pp: 6.7
      tiebreak_questions: 8
      tiebreak_sica_wins: 6
      bootstrap_p: 0.068
      maxsat_exclusion_rate: 0.052
      wall_time_min: 35
    result_rationale: >
      7B模型比14B弱→两个效应叠加产生更大SICA gain：
      (1) 更高的C0（0.68 vs 14B的0.53）：7B的推理能力较弱，对同一问题产生更多样的答案
      （K=12条trace中约8条产生多候选），这意味着更多tiebreak机会。
      (2) SC baseline更低（55% vs 14B的70%）：弱模型的majority vote更容易出错，
      给SICA更大的改进空间。
      (3) tiebreak win rate保持在75%（6/8）：MAX-SAT的约束聚合能力不依赖模型强度，
      因为它是在约束层面做推理而非在答案层面。即使7B的约束质量略低
      （c1_extraction_rate=0.93 vs 14B的1.0），MAX-SAT仍能从noise中提取signal。
      6.7pp的gap大于14B的3.3pp，验证了C0-as-predictor的因果方向：
      C0更高→更多tie→更多SICA介入→更大gain。注意基线准确率从14B的70%降到55%，
      这是预期的——7B在逻辑推理上天然更弱。但SICA把7B的62%拉到接近14B SC的70%，
      这是一个有实际意义的结果（"SICA让便宜模型接近贵模型的SC性能"）。
      bootstrap p=0.068在60题上略高于0.05，但在204题扩展后预计可达显著。
    tables:
      - name: "Table 5: Model Scaling — SICA Effectiveness vs Model Size"
        columns: ["Model", "Params", "SC Acc", "SICA Acc", "Gap (pp)", "C0", "Type"]
        rows:
          - ["Qwen2.5-7B-Instruct", "7B", 0.550, 0.617, "+6.7", 0.68, "Instruction"]
          - ["Qwen2.5-14B-Instruct", "14B", 0.700, 0.733, "+3.3", 0.53, "Instruction"]
          - ["QwQ-32B", "32B", 0.733, 0.733, "0.0", 0.036, "Reasoning"]
    figures_description:
      - "Figure 5a: 散点图——C0 vs SICA-SC gap，三个模型点+线性拟合。7B在右上（高C0, 高gap），QwQ在左下（低C0, 零gap），14B居中。r≈0.99的近完美线性关系。"
      - "Figure 5b: Operating regime图——x轴C0, y轴SICA gain。阴影区域标注'SICA effective zone' (C0>20%) 和 'degeneration zone' (C0<5%)。三个模型点清晰落入各自区域。"
    analysis: >
      7B实验是operating regime claim的关键验证。三点数据（7B/14B/QwQ）在C0-gap空间
      形成近完美线性关系，建立了C0作为predictor的实证基础。更重要的是，7B的高gap
      证明了SICA对"部署中最常见的模型"（中小规模instruction models）最有价值——
      这是实际意义的论证。论文可以说："SICA's benefit scales inversely with model
      capability, making it most valuable for the cost-effective models practitioners
      actually deploy."

  - name: "qwq_32b_operating_regime"
    plan_id: "exp-005"
    description: >
      QwQ-32B负面结果格式化。数据已存在（来自MVP阶段的AIME/MATH/ProofWriter/FOLIO运行）。
    expected_results:
      status: "DONE — 数据已完成，无需新实验"
      c0_qwq_aime: 0.0
      c0_qwq_math: 0.0
      c0_qwq_folio: 0.036
      c0_qwq_proofwriter: 0.0
      sica_sc_gap_all_tasks: 0.0
      key_finding: >
        QwQ-32B在所有任务上C0<5%，SICA≡SC。reasoning model的chain-of-thought
        过程消除了trace间的答案多样性，使得K条trace几乎总是产生相同答案。
    result_rationale: >
      已完成实验。QwQ-32B作为reasoning model，其extended thinking过程（数千token的
      推理链）在采样时起到了"内部self-consistency"的作用——模型在生成最终答案前
      已经内部验证了多次，导致不同trace收敛到相同答案。C0≈0意味着没有tiebreak机会，
      SICA退化为SC。这不是SICA的失败，而是operating regime边界的经验证据。
    tables: []
    figures_description:
      - "（合并到Figure 5b的operating regime图中，QwQ点标注为'Reasoning Model — Degeneration Zone'）"
    analysis: >
      不需要新实验。重新格式化现有数据，在论文中作为Section 4.2 "When Symbolic Consensus
      Degenerates"的核心证据。叙事关键：这是insight而非failure。

  - name: "c0_diagnostic_validation"
    plan_id: "exp-006"
    description: >
      汇总exp-001/002/004/005所有模型和K值的数据，绘制C0 vs SICA-SC gap的系统性分析。
      验证C0作为zero-cost predictor的claim。CPU-only。
    expected_results:
      data_points: 18
      data_sources:
        - "7B: K=12, 1 point"
        - "14B: K=6,8,9,12,16,20, 6 points"
        - "QwQ: 4 tasks, 4 points"
        - "14B expanded (204q): K=12, 1 point"
        - "各K值下per-dataset拆分: ~6 additional points"
      pearson_r_c0_vs_gap: 0.91
      spearman_rho_c0_vs_gap: 0.88
      c0_threshold_20pct_accuracy: 1.0
      c0_threshold_20pct_meaning: >
        C0>20%的所有配置均有正向SICA gain；C0<20%的所有配置gap≤0.5pp
      linear_fit_slope: 0.11
      linear_fit_intercept: -1.8
      linear_fit_r2: 0.83
      practical_rule: "C0>20% → deploy SICA; C0<5% → skip (overhead not justified)"
    result_rationale: >
      C0与SICA gap的高相关（r=0.91）来自一个简单的因果链：C0↑ → 更多多候选问题 →
      更多potential ties → 更多SICA介入机会 → 更大gain。这是near-tautological的关系，
      但其实用价值在于：C0可以通过单次SC投票在零额外成本下计算（不需要运行约束提取
      和MAX-SAT），因此它是一个真正的zero-cost predictor。18个数据点覆盖了3个模型、
      6个K值、2个数据集，提供了足够的多样性来排除过拟合。
      20%阈值的选择是empirical：在C0=20%处，期望的tie问题数量约为n×0.2×P(tie|multi-candidate)，
      在K=12时约为n×0.2×0.15≈3%的问题有tie。如果这3%的tiebreak win rate是75%，
      总gain约为0.03×0.75×(1/n)，对于n=60这约1.5pp——勉强可检测。
      低于20%则tie太少，gain不可测。
    tables:
      - name: "Table 6: C0 as Predictor — All Configurations"
        columns: ["Model", "K", "Dataset", "C0", "SICA-SC Gap (pp)", "Predicted Gap (pp)"]
        rows:
          - ["7B", 12, "Combined", 0.68, 6.7, 5.7]
          - ["14B", 6, "Combined", 0.50, 3.4, 3.7]
          - ["14B", 12, "Combined", 0.53, 3.3, 4.0]
          - ["14B", 16, "Combined", 0.55, 5.0, 4.3]
          - ["14B", 12, "Expanded-204", 0.51, 3.9, 3.8]
          - ["QwQ", 12, "FOLIO", 0.036, 0.0, -1.4]
          - ["QwQ", 12, "AIME", 0.0, 0.0, -1.8]
    figures_description:
      - "Figure 6a: C0 vs SICA-SC gap 散点图（所有18个配置），线性回归拟合线，95% CI shading。三个模型用不同marker区分。清晰的正相关趋势，QwQ cluster在原点附近，7B在右上。"
      - "Figure 6b: C0阈值决策图——x轴C0，y轴binary {deploy SICA, skip SICA}。在C0=20%处画竖线，左侧全部是'skip'，右侧全部是'deploy'。完美分类准确率。"
      - "Figure 6c: 实际gap vs 线性预测gap的parity plot（y=x线）。R²=0.83标注。大多数点接近对角线。"
    analysis: >
      C0验证是论文的practical takeaway——让从业者在不运行完整SICA pipeline的情况下
      判断是否值得部署。r=0.91和阈值20%的完美分类给出了一个clean且actionable的规则。
      论文的Algorithm 2框可以是一个两步决策流程：(1) 运行SC，计算C0；
      (2) if C0>20%: run SICA; else: use SC result directly。
      这将SICA从"总是运行的overhead"变成"按需部署的工具"，直接回应overhead concern。

  - name: "sica_72b_awq"
    plan_id: "exp-007"
    description: >
      Qwen2.5-72B-Instruct AWQ 4-bit量化，60题，K=12。高基线非推理模型的scaling点。
      P2优先级，camera-ready时间允许则加入。
    expected_results:
      model: "Qwen2.5-72B-Instruct-AWQ-4bit"
      n_total: 60
      K: 12
      sica_accuracy: 0.800
      sc_accuracy: 0.783
      sica_sc_gap_pp: 1.7
      c0_multi_candidate_rate: 0.32
      c1_extraction_rate: 0.99
      folio_sica: 0.833
      folio_sc: 0.800
      folio_gap_pp: 3.3
      proofwriter_sica: 0.767
      proofwriter_sc: 0.767
      proofwriter_gap_pp: 0.0
      tiebreak_questions: 2
      tiebreak_sica_wins: 2
      bootstrap_p: 0.28
      wall_time_min: 120
    result_rationale: >
      72B instruction model的基线准确率高（SC≈78%），介于14B（70%）和QwQ（73%但reasoning model）
      之间。高基线意味着更少的错误答案→更少的答案多样性→更低的C0（0.32 vs 14B的0.53）。
      C0=0.32仍>20%阈值，所以SICA有gain，但gain小于14B（1.7pp vs 3.3pp），
      完美符合C0-gap线性关系的预测。PW上可能回到0pp（2个tie不够看到PW gain）。
      这个数据点填充了Figure 5a中7B和14B之间（以及14B和QwQ之间）的空白，
      使C0-gap关系更convincing。但60题的p=0.28不显著，所以这是supporting evidence
      而非standalone claim——这就是为什么它是P2。
    tables:
      - name: "Table 7 (camera-ready): Extended Scaling Analysis"
        columns: ["Model", "Params", "Quantization", "SC", "SICA", "Gap", "C0"]
        rows:
          - ["7B-Instruct", "7B", "FP16", 0.550, 0.617, "+6.7", 0.68]
          - ["14B-Instruct", "14B", "FP16", 0.700, 0.733, "+3.3", 0.53]
          - ["72B-Instruct", "72B", "AWQ-4bit", 0.783, 0.800, "+1.7", 0.32]
          - ["QwQ-32B", "32B", "FP16", 0.733, 0.733, "0.0", 0.036]
    figures_description:
      - "（72B点加入Figure 5a的C0 vs gap散点图，落在14B和QwQ之间，进一步确认线性趋势）"
    analysis: >
      72B数据补完了scaling story：从7B（最大gain）到14B（中等gain）到72B（小gain）
      到QwQ（零gain），SICA effectiveness随模型能力单调递减。但关键是这条曲线的
      驱动因素不是模型大小本身，而是C0——72B虽然大但不是reasoning model，所以仍有
      正向gain。这区分了"模型能力"和"推理范式"的效应，支持Claim 2（operating regime
      由模型类型决定，非大小）。

  - name: "constraint_quality_case_studies"
    plan_id: "exp-008"
    description: >
      对5-10个代表性问题做定性分析：约束是否语义有意义？被排除的约束是否对应推理错误？
    expected_results:
      n_case_studies: 8
      cases_selected:
        - type: "SICA wins tie (FOLIO)"
          count: 3
        - type: "SICA loses tie (FOLIO)"
          count: 1
        - type: "No tie, SICA=SC (FOLIO)"
          count: 2
        - type: "ProofWriter high-contradiction"
          count: 2
      qualitative_findings:
        constraint_semantic_validity: "6/8 cases show constraints that faithfully represent key logical relationships in the problem"
        excluded_constraint_analysis: "In 4/5 cases with exclusions, excluded constraints correspond to identifiable reasoning errors (wrong negation, scope confusion, missed premise)"
        failure_case_pattern: "SICA失败的1个tie case中，错误答案的trace恰好产生了更多internally-consistent但factually-wrong的约束（自洽但错误的推理链）"
        constraint_redundancy: "约40%的约束是语义重复（同一逻辑关系的不同FOL表达），MAX-SAT的去重+权重机制处理了这种冗余"
    result_rationale: >
      定性分析的预期基于SICA pipeline的设计：LLM生成的FOL约束是reasoning trace的
      形式化表示，因此高质量的trace应产生语义有效的约束。约束提取率c1=1.0（14B数据）
      说明LLM在FOLIO类型的自然语言推理上能可靠地生成FOL。被排除的约束（exclusion rate≈3%）
      理论上对应MAX-SAT判定为与多数约束矛盾的项——在推理任务中，这些通常是
      错误推理步骤的形式化。定性验证这一点为SICA的"约束提取→MAX-SAT聚合"pipeline
      提供了interpretability论证，回应"MAX-SAT是不是在做有意义的事情"的隐含质疑。
    tables: []
    figures_description:
      - "Figure 7: 两个case study的详细展示（一个SICA胜，一个SICA败）。展示原题→12条trace的答案分布→提取的约束（5-6条关键约束高亮）→MAX-SAT满足/排除结果→最终选择。类似于流程图+约束表的混合可视化。"
    analysis: >
      定性分析补充了定量结果的mechanistic story。论文中放2-3个代表性case study
      （可在appendix放完整8个），直观展示SICA在tie上胜出的原因（正确答案的trace
      产生了更多可满足的约束），以及SICA偶尔失败的原因（错误推理也可以是internally
      consistent的）。后者是honest的局限性讨论。

  - name: "overhead_analysis"
    plan_id: "exp-009"
    description: >
      Wall-time分解：每个问题的生成时间、约束提取时间、MAX-SAT求解时间。
      回应"overhead是否值得"的concern。
    expected_results:
      n_problems_analyzed: 60
      avg_breakdown_per_problem_s:
        trace_generation: 42.0
        constraint_extraction: 12.5
        maxsat_solving: 0.3
        total_sica: 54.8
        total_sc: 42.0
      overhead_ratio: 1.30
      overhead_breakdown_pct:
        generation: 76.6
        extraction: 22.8
        solving: 0.6
      extraction_is_parallelizable: true
      extraction_parallel_overhead_s: 3.2
      parallel_overhead_ratio: 1.08
      maxsat_median_time_ms: 12
      maxsat_max_time_ms: 340
      maxsat_scales_with: "n_constraints (linear in practice, theoretical worst-case NP)"
    result_rationale: >
      SICA相比SC的额外开销来自两步：约束提取（需要额外LLM调用将每条trace转换为FOL）
      和MAX-SAT求解。从D012数据看，60题×12 traces = 720次约束提取调用，总时间约750s，
      平均12.5s/问题。但这些调用是独立的，可以完全并行化——如果用12个并行worker，
      per-problem overhead降到约3s。MAX-SAT求解（Z3 partial MAX-SAT）在约束数量<100时
      通常在毫秒级完成。因此sequential overhead是30%（54.8s vs 42.0s），
      但parallel overhead只有8%（45.2s vs 42.0s）。相比SC的30%（sequential）或8%（parallel）
      额外成本，SICA在FOLIO上带来+6.9pp的准确率提升——这是高性价比的。
      论文可以argue："SICA adds <10% wall-time overhead when extraction is parallelized,
      while providing statistically significant accuracy gains."
    tables:
      - name: "Table 8: Computational Overhead Analysis"
        columns: ["Component", "Time/Problem (s)", "% of Total", "Parallelizable"]
        rows:
          - ["Trace Generation (K=12)", 42.0, "76.6%", "Yes (standard)"]
          - ["Constraint Extraction", 12.5, "22.8%", "Yes (per-trace)"]
          - ["MAX-SAT Solving", 0.3, "0.6%", "N/A (fast)"]
          - ["Total SICA", 54.8, "100%", "-"]
          - ["Total SC (baseline)", 42.0, "-", "-"]
          - ["Sequential Overhead", "+12.8s (+30%)", "-", "-"]
          - ["Parallel Overhead", "+3.2s (+8%)", "-", "-"]
    figures_description:
      - "Figure 8: Stacked bar chart——SC vs SICA的per-problem时间分解。SC只有generation bar，SICA有generation + extraction + solving三段。Solving段几乎不可见（<1%）。标注parallel overhead线。"
    analysis: >
      Overhead分析直接回应reviewer concern。关键message：
      (1) MAX-SAT本身几乎零成本（<1%）——overhead完全来自约束提取的LLM调用；
      (2) 约束提取可并行化，实际部署中overhead<10%；
      (3) 对比+6.9pp的FOLIO gain，8%的额外时间是高性价比的。
      论文中可以framing为："The symbolic reasoning component (MAX-SAT) adds negligible
      overhead; the cost is in constraint extraction, which is embarrassingly parallel."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7dde4f3-36ed-4a8f-b752-5075783ecec1",
  "isSidechain": false,
  "requestId": "req_011Cb5gWb4iqi6Tq4nfSabJk",
  "type": "assistant",
  "uuid": "f8db07a1-a169-4281-90b3-a62073f2197d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "52123d52-397d-4387-94d9-355bd36d3839",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0174gkwPNpSxgUoqfBDYk6tH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11013,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11013,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11411,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11013,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11013
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：扩展实验复现并放大60q趋势：SICA在200+问题上达到统计显著，K消融揭示清晰的tiebreak频率机制，7B验证C0预测器 核心假设：['FOLIO +6.7pp在~100问题上保持或扩大（tiebreak不是60q采样噪声）', \"ProofWriter在扩展数据上出现正向gap（≥1pp），消除'单…",
  "leafUuid": "f8db07a1-a169-4281-90b3-a62073f2197d",
  "sessionId": "52123d52-397d-4387-94d9-355bd36d3839"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 Best-Case Scenario Detailed Predictions",
  "sessionId": "52123d52-397d-4387-94d9-355bd36d3839"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：扩展实验复现并放大60q趋势：SICA在200+问题上达到统计显著，K消融揭示清晰的tiebreak频率机制，7B验证C0预测器 核心假设：['FOLIO +6.7pp在~100问题上保持或扩大（tiebreak不是60q采样噪声）', \"ProofWriter在扩展数据上出现正向gap（≥1pp），消除'单…",
  "leafUuid": "f8db07a1-a169-4281-90b3-a62073f2197d",
  "sessionId": "52123d52-397d-4387-94d9-355bd36d3839"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 Best-Case Scenario Detailed Predictions",
  "sessionId": "52123d52-397d-4387-94d9-355bd36d3839"
}
```

---
