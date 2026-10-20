# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：FOLIO增益在扩展后缩小但仍正向，ProofWriter仍无增益，K消融有方向性但噪声大，统计显著性边缘 核心假设：['FOLIO gap从+6.

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/7a4553d3-7c73-4cf5-891f-9f1e40bddb33.jsonl`
- **Structured JSON:** [`7006170d47f54f26eaa0.json`](../../sessions/70/7006170d47f54f26eaa0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T05:22:07.146Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T05:22:07.146Z",
  "sessionId": "7a4553d3-7c73-4cf5-891f-9f1e40bddb33",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：FOLIO增益在扩展后缩小但仍正向，ProofWriter仍无增益，K消融有方向性但噪声大，统计显著性边缘\n核心假设：['FOLIO gap从+6.7pp缩小到+3-4pp（部分tiebreak wins被更大样本稀释）', 'ProofWriter在扩展数据上仍~0pp（domain差异真实存在，不是样本量问题）', 'K消融方向正确（偶K > 奇K）但不单调，个别K值有反转', '7B的C0更高，但SICA-SC gap与14B相近（C0预测方向对但非线性）', 'bootstrap p在0.05-0.15之间——单侧可argue，双侧不显著']\n关键指标范围：{'combined_gap_pp': [1.5, 3.0], 'folio_gap_pp': [3.0, 5.0], 'proofwriter_gap_pp': [-0.5, 1.0], 'bootstrap_p_combined': [0.05, 0.15], 'c0_14b': [0.4, 0.55], 'c0_7b': [0.55, 0.7], 'c0_qwq': [0.0, 0.05], 'sica_7b_gap_pp': [1.5, 4.0], 'tiebreak_win_rate': [0.6, 0.75], 'k_ablation_correlation_r': [0.4, 0.7]}\n叙事方向：Claim 1需降级：不能说\"SICA显著优于SC\"，改为\"SICA provides principled tiebreaking with consistent positive direction (p<0.15, N=200+)\"，强调effect direction的 一致性而非单次p值。Claim 2成为论文核心贡献——operating regime characterization 不依赖SICA绝对增益大小，只需要\"instruction model有增益、reasoning model无增益\" 的定性对比成立。Claim 3弱化为\"C0 correlates with SICA benefit directionally\" 而非strong predictor。ProofWriter零增益需正面处理：作为domain-specific evidence 说明symbolic extraction quality matters（PW的FOL结构更规则，tie更少）。 补充constraint quality case study (exp-008) 增强mechanistic理解。 论文重心从\"SICA improves accuracy\"转向\"understanding when and why symbolic consensus helps\"——一篇characterization paper而非method paper。仍投EMNLP主会。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\nfocus: Key tension: SICA's gain is entirely from principled tiebreaking (4/60 questions, all 6:6 ties). Reviewers will attack statistical significance (p=0.317) and question overhead vs benefit. The operating regime characterization (reasoning vs instruction model) is the primary intellectual contribution. Expanded 200+ question results and K ablation are planned but not yet available. ProofWriter shows 0pp gain — domain generalization is a weakness.\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Fallback: AAAI 2027 (Aug 1)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条)\n1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).\n2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is conditional on trace diversity — SICA adds value when model outputs are diverse (instruction models, C0>20%) but provably degenerates to SC when models are self-consistent (reasoning models, C0<5%). This is a model property, not a task property.\n3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.\n\n## Core Insight\nSymbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that model architecture (reasoning vs instruction) determines the operating regime. This transforms SICA from \"yet another ensemble method\" into \"a method with formally characterizable applicability boundaries.\"\n\n## Story Spine\n- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.\n- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.\n- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75% win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) and show it's governed by model type, not task type.\n- **Headline result template**: \"On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → exp-001: Expand to 200+ questions for statistical power\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K sensitivity showing benefit pattern; exp-009: overhead analysis\n3. **\"Only one non-reasoning model\"** → exp-004: Add Qwen2.5-7B for scaling; exp-007: 72B-AWQ for camera-ready\n4. **\"ProofWriter shows 0pp gain\"** → Domain analysis in exp-001 expanded results\n5. **\"Random tiebreak baseline closes the gap\"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison\n6. **\"Why not just use a reasoning model?\"** → exp-005: QwQ-32B data shows reasoning models are self-consistent (don't need consensus improvement), but instruction models (cheaper, more deployed) benefit from SICA\n\n## Venue Fit Risks\n- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the \"operating regime characterization\" — the tiebreaking mechanism is evidence, not the claim.\n- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.\n- Negative results: QwQ-32B data must be presented as insight (\"When Does Symbolic Consensus Degenerate?\"), not failure.\n- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: Expand D012 from 60 to 200+ questions (PW D5 ~100 + FOLIO ~100) for\n    statistical power on C3. Merge with D012 data for combined analysis.\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  status: planned\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,12,16,20) on D012''s 60 questions. Key questions:\n    does SICA benefit depend on tiebreaks? What happens at odd K (no even splits)?\n    How does tiebreak frequency change with K?'\n  priority: P0\n  gpu_budget_hours: 5\n  deps: []\n  status: planned\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: sica_d012_14b\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. For camera-ready if time permits.'\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T05:22:07.151Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T05:22:07.151Z",
  "sessionId": "7a4553d3-7c73-4cf5-891f-9f1e40bddb33"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T05:22:07.205Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：FOLIO增益在扩展后缩小但仍正向，ProofWriter仍无增益，K消融有方向性但噪声大，统计显著性边缘
核心假设：['FOLIO gap从+6.7pp缩小到+3-4pp（部分tiebreak wins被更大样本稀释）', 'ProofWriter在扩展数据上仍~0pp（domain差异真实存在，不是样本量问题）', 'K消融方向正确（偶K > 奇K）但不单调，个别K值有反转', '7B的C0更高，但SICA-SC gap与14B相近（C0预测方向对但非线性）', 'bootstrap p在0.05-0.15之间——单侧可argue，双侧不显著']
关键指标范围：{'combined_gap_pp': [1.5, 3.0], 'folio_gap_pp': [3.0, 5.0], 'proofwriter_gap_pp': [-0.5, 1.0], 'bootstrap_p_combined': [0.05, 0.15], 'c0_14b': [0.4, 0.55], 'c0_7b': [0.55, 0.7], 'c0_qwq': [0.0, 0.05], 'sica_7b_gap_pp': [1.5, 4.0], 'tiebreak_win_rate': [0.6, 0.75], 'k_ablation_correlation_r': [0.4, 0.7]}
叙事方向：Claim 1需降级：不能说"SICA显著优于SC"，改为"SICA provides principled tiebreaking with consistent positive direction (p<0.15, N=200+)"，强调effect direction的 一致性而非单次p值。Claim 2成为论文核心贡献——operating regime characterization 不依赖SICA绝对增益大小，只需要"instruction model有增益、reasoning model无增益" 的定性对比成立。Claim 3弱化为"C0 correlates with SICA benefit directionally" 而非strong predictor。ProofWriter零增益需正面处理：作为domain-specific evidence 说明symbolic extraction quality matters（PW的FOL结构更规则，tie更少）。 补充constraint quality case study (exp-008) 增强mechanistic理解。 论文重心从"SICA improves accuracy"转向"understanding when and why symbolic consensus helps"——一篇characterization paper而非method paper。仍投EMNLP主会。


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
  "promptId": "56924407-0f5d-441d-97a1-dc290ccd53d3",
  "type": "user",
  "uuid": "c2ec9171-1a64-461a-8181-5ec16de12e53",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "7a4553d3-7c73-4cf5-891f-9f1e40bddb33",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T05:22:07.204Z_

```json
{
  "parentUuid": "c2ec9171-1a64-461a-8181-5ec16de12e53",
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
  "uuid": "4dd73062-25bd-4e0e-9bdc-e1588b9fb0e0",
  "timestamp": "2026-05-16T05:22:07.204Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "7a4553d3-7c73-4cf5-891f-9f1e40bddb33",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T05:22:07.204Z_

```json
{
  "parentUuid": "4dd73062-25bd-4e0e-9bdc-e1588b9fb0e0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "6b83b914-e24d-47dd-b816-668c85e5e43a",
  "timestamp": "2026-05-16T05:22:07.204Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "7a4553d3-7c73-4cf5-891f-9f1e40bddb33",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：FOLIO增益在扩展后缩小但仍正向，ProofWriter仍无增益，K消融有方向性但噪声大，统计显著性边缘 核心假设：['FOLIO gap从+6.7pp缩小到+3-4pp（部分tiebreak wins被更大样本稀释）', 'ProofWriter在扩展数据上仍~0pp（domain差异真实存在，不是样…",
  "leafUuid": "6b83b914-e24d-47dd-b816-668c85e5e43a",
  "sessionId": "7a4553d3-7c73-4cf5-891f-9f1e40bddb33"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "SICA Expanded Results on 200+ Questions with K Ablation and C0 Validation",
  "sessionId": "7a4553d3-7c73-4cf5-891f-9f1e40bddb33"
}
```

---

### Assistant

_source line 8 · 2026-05-16T05:22:53.568Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experimental results for all "planned" experiments in the experiment plan, under the "median" tier definition they've provided. I need to produce a single YAML block with the specified format.

Let me go through each planned experiment and generate median-tier results:

1. **exp-001: sica_expanded_14b** - Expand from 60 to 200+ questions
2. **exp-002: sica_k_ablation_14b** - K sensitivity analysis
3. **exp-003: tiebreak_baseline_analysis** - SICA vs SC-random vs SC-deterministic


4. **exp-004: sica_7b_scaling** - Qwen2.5-7B-Instruct
5. **exp-006: c0_diagnostic_validation** - C0 vs SICA-SC gap plot
6. **exp-007: sica_72b_awq** - Qwen2.5-72B AWQ
7. **exp-008: constraint_quality_case_studies** - Qualitative analysis
8. **exp-009: overhead_analysis** - Wall-time breakdown

Since exp-005 is already complete, I'll skip that one. Now I'm working through the median-tier assumptions for each remaining experiment.

Under median conditions, I'm expecting the FOLIO gap to narrow from 6.7pp down to 3-5pp, ProofWriter to stay around 0pp, the K ablation to show the right direction but with some noise, and the 7B model to have higher C0 while maintaining a similar SICA-SC gap compared to 14B. The bootstrap p-value should land between 0.05-0.15, combined gap around 1.5-3.0pp, tiebreak win rate between 0.6-0.75, and K ablation correlation somewhere in the 0.4-0.7 range.

For exp-001 with the expanded 14B setup, I'm looking at over 200 questions split roughly evenly between FOLIO and ProofWriter. The combined gap should come in around 2.0pp, FOLIO gap near 4.0pp, and ProofWriter gap essentially at zero.

The reason the original 60-question run showed that inflated 6.7pp on FOLIO was because it had only a handful of ties and SICA won most of them — that was partly luck with the small sample. When I scale up to 200+ questions, more ties naturally emerge, but SICA doesn't win all of them since some are genuinely ambiguous even with the constraints applied. ProofWriter's FOL structures are more uniform, creating fewer ties overall, and when ties do occur the constraint quality doesn't provide much differentiation.

Now I'm setting up exp-002 to test the K ablation across different values like 6, 8, 12, 16, and 20 on the original 60-question set.

For the K ablation, even values create structural opportunities for ties (like 6:6 or 8:8 splits), which is where SICA's tiebreaking advantage shows up, but odd values don't have that symmetry. The relationship between K and the performance gap isn't straightforward though — as K increases, exact ties become less likely since votes distribute across more candidates, so the benefit plateaus or even dips. The correlation between K and gap is around 0.55, which is positive but noisy because 60 questions just don't generate enough tie instances to get clean signal at each K value.

Looking at the tiebreak baseline comparison, SICA wins about 67% of ties compared to random's expected 50%, which is a solid advantage but smaller than its edge over deterministic alphabetical selection. That makes sense because deterministic selection is systematically wrong on ties while random gets 50% right by luck, so SICA's real gain is mainly against the random baseline. The 7B model shows higher constraint weighting around 0.62 and a SICA-SC gap of about 2.5 percentage points, which falls within the expected ranges, though the SC baseline itself is lower than what we see with the 14B model, suggesting the smaller model produces more diverse outputs.

The weaker 7B model generates noisier constraints from its first-order logic extraction, so despite having more tiebreak opportunities from that diversity, SICA can't capitalize on them as effectively. This keeps the gap around 2.5 percentage points, similar to the 14B results, which suggests C0 predicts the direction of improvement but the relationship isn't strictly linear. Looking at the correlation across different models and K values, I'm seeing directional alignment between higher C0 and larger gaps, but the correlation is moderate at around 0.55 across all data points, likely because the sample size is small with only a handful of model variants and K configurations.

The scatter becomes clearer when I look at specific points: QwQ sits at C0≈3.6% with essentially no gap, the 7B model at C0≈62% shows ~2.5pp gap, and 14B at C0≈47% shows ~2.0pp gap. The relationship is sublinear because at very high C0 values, the model becomes too confused to extract meaningful constraints. Moving to the 72B model, it has lower C0 than 14B around 0.30-0.40 since it's more self-consistent, and the gap shrinks to roughly 1.0-2.0pp, which aligns with the pattern that stronger models produce better constraint quality even when they're less diverse.

Now I'm looking at qualitative case studies across a handful of questions to see how well the constraints actually capture reasoning—some are clearly meaningful while others are noisy, which supports the mechanistic story but with important caveats about false positives. For the overhead analysis, I'm examining the wall time breakdown and finding that LLM generation dominates the cost, constraint extraction adds around 15-20% overhead, and MaxSAT solving is negligible, so the total overhead compared to bare self-consistency is roughly 20-30% just for the extraction step.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b83b914-e24d-47dd-b816-668c85e5e43a",
  "isSidechain": false,
  "requestId": "req_011Cb5gpTvMY2ZJcGT4juN6d",
  "type": "assistant",
  "uuid": "d6fb49c8-93f3-4e5f-b24d-8bdb5fc24532",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "7a4553d3-7c73-4cf5-891f-9f1e40bddb33",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VfT5udU95NACYGn5greyZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11114,
      "cache_read_input_tokens": 11841,
      "output_tokens": 9898,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 9898,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11114
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

_source line 9 · 2026-05-16T05:25:33.159Z_

```yaml
tier: median
narrative_guidance: >
  Claim 1需降级为"consistent positive direction"而非"significant improvement"。
  Claim 2成为核心贡献——operating regime characterization只需定性对比成立。
  Claim 3弱化为directional correlation。ProofWriter零增益作为domain evidence正面处理。
  论文重心转向"understanding when and why symbolic consensus helps"——characterization paper。

imagined_experiments:
  - name: sica_expanded_14b
    plan_id: exp-001
    description: "Expand to 200+ questions (FOLIO 104 + ProofWriter D5 108), merge with D012 for combined N=212 analysis"
    expected_results:
      n_total: 212
      n_folio: 104
      n_proofwriter: 108
      sica_accuracy_combined: 0.743
      sc_accuracy_combined: 0.722
      combined_gap_pp: 2.1
      folio_sica: 0.798
      folio_sc: 0.760
      folio_gap_pp: 3.8
      proofwriter_sica: 0.694
      proofwriter_sc: 0.685
      proofwriter_gap_pp: 0.9
      c0_combined: 0.47
      c0_folio: 0.52
      c0_proofwriter: 0.42
      bootstrap_p_combined: 0.088
      bootstrap_p_folio: 0.062
      bootstrap_p_proofwriter: 0.41
      tiebreak_instances_total: 28
      tiebreak_sica_wins: 18
      tiebreak_sica_losses: 10
      tiebreak_win_rate: 0.643
      total_constraints_raw: 19840
      total_constraints_unique: 5120
      maxsat_exclusion_rate: 0.031
      wall_time_min: 205
    result_rationale: >
      FOLIO gap从D012的+6.7pp缩小到+3.8pp，因为原始60题中4个tiebreak全胜是小样本运气——
      扩展后tiebreak实例从4增到~15，SICA胜率从100%回归到~65%（部分tie中约束质量不足以区分正确答案）。
      ProofWriter维持近零增益(+0.9pp, p=0.41不显著)：PW的FOL结构规则，模型提取的约束同质性高，
      tie本身就少(C0=0.42 vs FOLIO的0.52)，且tie中约束权重无法有效区分——PW的错误更多来自
      推理链遗漏前提而非逻辑矛盾。Combined bootstrap p=0.088落在0.05-0.15区间：
      单侧可argue方向性证据(p<0.10)，但双侧检验不显著(p=0.176)。
    tables:
      - name: "Table 2: Expanded Results (N=212)"
        columns: [Dataset, N, SC_Acc, SICA_Acc, Gap_pp, p_bootstrap, C0]
        rows:
          - [FOLIO, 104, 76.0, 79.8, "+3.8", 0.062, 0.52]
          - [ProofWriter, 108, 68.5, 69.4, "+0.9", 0.41, 0.42]
          - [Combined, 212, 72.2, 74.3, "+2.1", 0.088, 0.47]
      - name: "Table 3: Tiebreak Resolution Analysis"
        columns: [Dataset, Ties, SICA_Win, SICA_Loss, Win_Rate]
        rows:
          - [FOLIO, 16, 11, 5, 0.688]
          - [ProofWriter, 12, 7, 5, 0.583]
          - [Combined, 28, 18, 10, 0.643]
    figures_description:
      - "Fig 2: Per-question SICA vs SC correctness heatmap (212 questions), highlighting tie instances with color coding for SICA win/loss"
    analysis: >
      Combined gap +2.1pp with p=0.088 supports "consistent positive direction" framing but not strong significance.
      FOLIO单独p=0.062接近显著，是论文最强evidence。ProofWriter的+0.9pp在噪声范围内。
      Tiebreak win rate 64.3%显著优于random 50% (binomial p=0.096, N=28)，
      但不如D012的100% (4/4)——确认小样本膨胀效应。
      策略：report one-sided p<0.10 for combined, 强调effect direction一致性跨两个dataset，
      ProofWriter作为"boundary condition"证据——当domain FOL结构规则时SICA增益边际化。

  - name: sica_k_ablation_14b
    plan_id: exp-002
    description: "K=6,8,12,16,20 sensitivity on D012's 60 questions, analyzing tiebreak frequency and SICA gap as function of K"
    expected_results:
      k6_sica_acc: 0.717
      k6_sc_acc: 0.700
      k6_gap_pp: 1.7
      k6_tie_count: 6
      k6_c0: 0.48
      k8_sica_acc: 0.733
      k8_sc_acc: 0.700
      k8_gap_pp: 3.3
      k8_tie_count: 5
      k8_c0: 0.50
      k10_sica_acc: 0.733
      k10_sc_acc: 0.700
      k10_gap_pp: 3.3
      k10_tie_count: 4
      k10_c0: 0.533
      k12_sica_acc: 0.750
      k12_sc_acc: 0.717
      k12_gap_pp: 3.3
      k12_tie_count: 3
      k12_c0: 0.55
      k16_sica_acc: 0.733
      k16_sc_acc: 0.717
      k16_gap_pp: 1.7
      k16_tie_count: 2
      k16_c0: 0.58
      k20_sica_acc: 0.750
      k20_sc_acc: 0.733
      k20_gap_pp: 1.7
      k20_tie_count: 2
      k20_c0: 0.60
      k_gap_correlation_r: 0.52
      k_gap_correlation_p: 0.29
      odd_k_check_k9_gap_pp: 0.0
      odd_k_check_k11_gap_pp: 0.0
      wall_time_hours: 4.8
    result_rationale: >
      K消融方向正确但非单调：偶数K有tiebreak可能（结构性），奇数K几乎无精确tie。
      K=8和K=10(D012原始)表现最好——K足够大产生diversity但tie概率尚可。
      K=6时tie最多(6个)因为6:0/5:1/4:2/3:3分布中3:3概率~31%（二项分布近似），
      但每个tie只有6条trace的约束信息，解析力弱，SICA只赢4/6。
      K=16/20时tie极少（精确8:8或10:10概率<5%），SICA几乎无用武之地——
      但SC本身准确率上升（更多vote稳定了majority）。
      相关性r=0.52说明K与gap有正方向关联但p=0.29（仅5个点），不能claim统计关系。
      核心发现：SICA benefit的来源确实是tiebreaking——在odd K实验中gap精确归零，
      这是mechanistic validation而非statistical claim。
    tables:
      - name: "Table 4: K Sensitivity Analysis (N=60)"
        columns: [K, SC_Acc, SICA_Acc, Gap_pp, Ties, Tie_SICA_Wins, C0]
        rows:
          - [6, 70.0, 71.7, "+1.7", 6, 4, 0.48]
          - [8, 70.0, 73.3, "+3.3", 5, 4, 0.50]
          - ["10*", 70.0, 73.3, "+3.3", 4, 4, 0.53]
          - [12, 71.7, 75.0, "+3.3", 3, 3, 0.55]
          - [16, 71.7, 73.3, "+1.7", 2, 2, 0.58]
          - [20, 73.3, 75.0, "+1.7", 2, 2, 0.60]
      - name: "Table 5: Odd K Control"
        columns: [K, SC_Acc, SICA_Acc, Gap_pp, Ties]
        rows:
          - [9, 70.0, 70.0, "0.0", 0]
          - [11, 71.7, 71.7, "0.0", 0]
    figures_description:
      - "Fig 3: K vs SICA-SC gap (pp) with tie count on secondary axis. Shows non-monotonic relationship with peak at K=8-12"
      - "Fig 4: Odd vs Even K comparison — structural proof that SICA gain comes exclusively from tiebreak resolution"
    analysis: >
      K消融的核心价值不是找最优K，而是mechanistic proof：odd K → 0 gap确认SICA的
      entire gain来自tiebreak resolution，非其他pathway。这是defense against reviewer
      "SICA只是噪声"的strongest evidence——噪声不会在odd/even间产生系统性差异。
      Non-monotonicity (K=16 gap < K=12 gap)因为高K时tie概率指数下降，
      不损害论文claims——反而支持"SICA operates specifically on ties"的precision。
      r=0.52不够strong predictor，在论文中报告为"directional"而非"predictive"。

  - name: tiebreak_baseline_analysis
    plan_id: exp-003
    description: "CPU reanalysis: SICA vs SC-random-tiebreak vs SC-alphabetical on all 60 D012 questions"
    expected_results:
      sc_deterministic_acc: 0.700
      sc_random_acc_mean: 0.717
      sc_random_acc_std: 0.023
      sica_acc: 0.733
      sica_vs_deterministic_gap_pp: 3.3
      sica_vs_random_gap_pp: 1.7
      random_vs_deterministic_gap_pp: 1.7
      sica_vs_random_bootstrap_p: 0.22
      tiebreak_sica_correct: 3
      tiebreak_random_expected_correct: 2.0
      tiebreak_deterministic_correct: 1
      total_ties: 4
      n_questions: 60
    result_rationale: >
      D012有4个tie (6:6 splits)。SC-deterministic在这4个tie中只答对1个(alphabetical bias)。
      SC-random期望答对2个(50% per tie × 4 ties)。SICA答对3个(75% win rate on ties)。
      所以SICA vs random的gap只有+1.7pp(1个额外正确)，而vs deterministic是+3.3pp(2个额外正确)。
      在仅4个tie的small sample上，SICA vs random的p值很高(0.22)——无法统计区分。
      但这正是median档的定义：方向正确，统计力不足。需要exp-001的28个tie来获得更好的power。
      关键insight：D012报告的+3.3pp gap中，约一半来自deterministic tiebreak的系统性bias
      (alphabetical偏向错误答案)，另一半来自SICA的真实constraint-based resolution。
    tables:
      - name: "Table 6: Tiebreak Baseline Comparison (D012, N=60)"
        columns: [Method, Accuracy, Gap_vs_SICA, Ties_Correct, p_vs_SICA]
        rows:
          - [SC-Deterministic, 70.0%, "-3.3pp", "1/4", 0.317]
          - [SC-Random (mean), 71.7%, "-1.7pp", "2.0/4", 0.22]
          - [SICA, 73.3%, "—", "3/4", "—"]
    figures_description:
      - "Fig 5: Tiebreak resolution comparison — bar chart showing correct resolution rate across methods on tie instances"
    analysis: >
      这个实验对论文framing至关重要：必须承认SC-random是比SC-deterministic更公平的baseline。
      SICA vs random在D012上不显著，但在exp-001的expanded data(28 ties, 64.3% win rate)上
      binomial test给p=0.096——边缘但可报告。论文策略：(1)承认deterministic baseline inflates gap，
      (2)报告vs random的gap和p值transparently，(3)argue即使vs random，64.3% win rate
      在repeated application中有practical value，(4)odd/even K实验作为mechanistic证据
      补充statistical weakness。

  - name: sica_7b_scaling
    plan_id: exp-004
    description: "Qwen2.5-7B-Instruct on same 60 D012 questions, testing C0-as-predictor hypothesis"
    expected_results:
      sica_accuracy: 0.683
      sc_accuracy: 0.650
      sica_sc_gap_pp: 3.3
      c0_multi_candidate_rate: 0.633
      c0_folio: 0.70
      c0_proofwriter: 0.57
      folio_sica: 0.733
      folio_sc: 0.700
      folio_gap_pp: 3.3
      proofwriter_sica: 0.633
      proofwriter_sc: 0.600
      proofwriter_gap_pp: 3.3
      bootstrap_p_combined: 0.18
      tiebreak_instances: 7
      tiebreak_sica_wins: 5
      tiebreak_win_rate: 0.714
      constraint_quality_degradation: 0.15
      extraction_failures: 3
      wall_time_min: 35
    result_rationale: >
      7B模型更弱→答案更分散→C0从14B的0.53升到0.63(符合0.55-0.70区间)。
      更多tie instances(7 vs 14B的4)给SICA更多resolution机会。
      但constraint质量下降：7B的FOL提取更noisy(3个extraction failures，约束语义准确率降低)。
      净效果：gap_pp=3.3与14B相同(不是更大)——higher C0带来更多opportunity但lower constraint
      quality降低per-tie win rate。这验证了C0预测方向(7B有增益)但关系非线性：
      C0从0.53→0.63(+19%)，gap从3.3→3.3(+0%)，因为constraint quality是confounding factor。
      ProofWriter在7B上意外出现+3.3pp——因为7B在PW上错误更多且更diverse(不像14B那样
      一致性地犯同一种错误)，给SICA提供了differentiation空间。但N=30, p=0.18不显著。
    tables:
      - name: "Table 7: Model Scaling Comparison"
        columns: [Model, Params, C0, SC_Acc, SICA_Acc, Gap_pp, Ties, Win_Rate]
        rows:
          - [Qwen2.5-7B-Instruct, 7B, 0.63, 65.0, 68.3, "+3.3", 7, 0.714]
          - [Qwen2.5-14B-Instruct, 14B, 0.53, 70.0, 73.3, "+3.3", 4, 0.750]
          - [QwQ-32B (reasoning), 32B, 0.036, 72.7, 72.7, "0.0", 0, "N/A"]
    figures_description:
      - "Fig 6: C0 vs SICA-SC gap across models. Three points showing positive direction but non-linear relationship"
    analysis: >
      7B结果validates Claim 2的direction但complicates Claim 3。C0确实higher且有增益(vs QwQ的0)，
      但gap大小不随C0线性增长。论文需将Claim 3从"C0 predicts magnitude"弱化为
      "C0 predicts whether SICA will help (binary gate)"——threshold约在C0>20%时有增益，
      <5%时无增益，但20-70%区间内magnitude由constraint quality而非C0 alone决定。
      7B的PW增益是surprise(14B上为0)——可能因为sample size或因为7B的error pattern不同。
      不过度interpret，在论文中note为"suggestive but N too small for conclusion"。

  - name: c0_diagnostic_validation
    plan_id: exp-006
    description: "Cross-model C0 vs SICA-SC gap scatter plot and correlation analysis"
    expected_results:
      data_points: 8
      models_included: [Qwen2.5-7B, Qwen2.5-14B, QwQ-32B]
      k_values_included: [6, 8, 10, 12, 16, 20]
      pearson_r: 0.58
      pearson_p: 0.13
      spearman_rho: 0.64
      spearman_p: 0.086
      binary_gate_accuracy: 1.0
      binary_gate_threshold_c0: 0.20
      above_threshold_mean_gap: 2.6
      below_threshold_mean_gap: 0.0
      r_within_instruction_models: 0.41
    result_rationale: >
      跨所有模型和K值，共8个独立数据点(7B×1, 14B×6 K values, QwQ×1)。
      Pearson r=0.58主要由QwQ的极端点(C0≈0.04, gap=0)驱动——去掉QwQ后
      只在instruction models间r=0.41(weak)。这说明C0作为binary gate很强
      (C0>20% → 有增益, <5% → 无增益, accuracy=100%)，但作为magnitude predictor很弱。
      Spearman rho=0.64稍好因为不假设线性关系。p=0.086/0.13在边缘——
      8个点的power本身就不够做strong correlation claim。
      这决定了Claim 3在论文中的framing：diagnostic gate而非quantitative predictor。
    tables:
      - name: "Table 8: C0 Diagnostic Summary"
        columns: [Model, K, C0, Gap_pp, Regime]
        rows:
          - [QwQ-32B, 10, 0.036, 0.0, degenerate]
          - [14B-Instruct, 6, 0.48, 1.7, active]
          - [14B-Instruct, 8, 0.50, 3.3, active]
          - [14B-Instruct, 10, 0.53, 3.3, active]
          - [14B-Instruct, 12, 0.55, 3.3, active]
          - [14B-Instruct, 16, 0.58, 1.7, active]
          - [14B-Instruct, 20, 0.60, 1.7, active]
          - [7B-Instruct, 10, 0.63, 3.3, active]
    figures_description:
      - "Fig 7: C0 vs SICA-SC gap scatter plot with binary threshold annotation at C0=0.20. Clear separation between degenerate regime (QwQ) and active regime (instruction models)"
      - "Fig 8: Within active regime, C0 vs gap showing weak/non-significant correlation — gap determined by factors beyond C0 alone"
    analysis: >
      C0 validation的核心结论：C0是excellent binary classifier (reasoning vs instruction regime)
      但poor quantitative predictor within the active regime。论文应present C0 as
      "practitioner decision tool"——compute C0 on small pilot (5-10 questions), if <10% don't deploy SICA,
      if >20% SICA will likely help。不claim C0 predicts how much it helps。
      这是median档的typical outcome：方向性insight成立但quantitative precision不足。

  - name: sica_72b_awq
    plan_id: exp-007
    description: "Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions for scaling curve"
    expected_results:
      sica_accuracy: 0.783
      sc_accuracy: 0.767
      sica_sc_gap_pp: 1.7
      c0_multi_candidate_rate: 0.35
      folio_sica: 0.867
      folio_sc: 0.833
      folio_gap_pp: 3.3
      proofwriter_sica: 0.700
      proofwriter_sc: 0.700
      proofwriter_gap_pp: 0.0
      tiebreak_instances: 2
      tiebreak_sica_wins: 1
      bootstrap_p: 0.35
      wall_time_min: 180
    result_rationale: >
      72B是instruction model但更强→更self-consistent→C0降到0.35(14B的0.53和QwQ的0.036之间)。
      SC baseline更高(76.7% vs 14B的70.0%)——stronger model少犯错。
      Ties更少(仅2个)因为72B的majority更decisive。SICA仅赢1/2 ties，gap=1.7pp。
      bootstrap p=0.35完全不显著(N=60, 仅1题差异)。
      这对论文的价值：confirms scaling trend (bigger instruction model → lower C0 → less SICA benefit)，
      支撑"instruction model size是operating regime的gradual axis"的narrative。
      但统计上是noise——camera-ready inclusion取决于是否加强story还是dilute it。
    tables:
      - name: "Table 9: Full Scaling Curve"
        columns: [Model, Type, Params, C0, SC_Acc, SICA_Acc, Gap_pp]
        rows:
          - [Qwen2.5-7B-Instruct, instruction, 7B, 0.63, 65.0, 68.3, "+3.3"]
          - [Qwen2.5-14B-Instruct, instruction, 14B, 0.53, 70.0, 73.3, "+3.3"]
          - [Qwen2.5-72B-Instruct-AWQ, instruction, 72B, 0.35, 76.7, 78.3, "+1.7"]
          - [QwQ-32B, reasoning, 32B, 0.04, 72.7, 72.7, "0.0"]
    figures_description:
      - "Fig 9: Model parameters vs C0 and SICA gap — showing smooth degradation for instruction models, discontinuous drop for reasoning model"
    analysis: >
      72B填充了scaling curve但statistical power极弱。Camera-ready decision：
      如果72B支持narrative(C0随size降)则include as one data point in Fig 9。
      如果reviewer要求removal(not significant)可safely drop。不是essential evidence。
      Key insight for paper：instruction model scaling是C0的continuous axis，
      reasoning model training是discontinuous regime shift——architecture > scale for C0。

  - name: constraint_quality_case_studies
    plan_id: exp-008
    description: "Qualitative analysis of 5-10 representative questions from exp-001 expanded data"
    expected_results:
      questions_analyzed: 8
      categories:
        sica_correct_tie_won: 3
        sica_correct_tie_lost: 1
        non_tie_agreement: 3
        extraction_failure: 1
      findings:
        constraints_semantic_accuracy: 0.72
        excluded_correspond_to_errors: 0.67
        constraint_redundancy_rate: 0.45
        meaningful_weight_differentiation: 0.625
      case_highlights:
        - type: "SICA win — correct constraint weighting"
          description: "FOLIO q47: 6:6 tie, correct answer's traces produce 12 unique non-contradictory constraints vs 8 for incorrect answer. MaxSAT weight correctly resolves."
        - type: "SICA loss — noisy extraction"
          description: "FOLIO q82: 6:6 tie, incorrect answer has more constraints due to verbose but flawed reasoning chain. Quantity overwhelms quality."
        - type: "Non-tie validation"
          description: "PW q33: 8:2 majority correct, SICA confirms — excluded constraints (2) both from minority incorrect traces."
    result_rationale: >
      Median档的constraint quality是"good enough to beat random but not reliably correct"。
      72%语义准确率意味着约28%的约束是noisy或错误的——这解释了为什么tiebreak win rate是
      64-75%而非接近100%。Excluded constraints 67%对应真实推理错误——有意义但不完美。
      45%冗余率说明不同traces经常提取相同约束(同一推理步骤)，constraint diversity比trace diversity低。
      Case studies的价值：为reviewer提供"mechanistic understanding"的concrete evidence，
      补充纯statistical evidence的不足。一个好的SICA-win case + 一个failure case = honest presentation。
    tables: []
    figures_description:
      - "Fig 10: Constraint extraction example — side-by-side FOL constraints from correct vs incorrect reasoning traces on a FOLIO tiebreak question"
      - "Fig 11: Constraint quality taxonomy — breakdown of semantic accuracy, redundancy, and exclusion correspondence"
    analysis: >
      Case studies在median档是论文的critical补充——当statistical evidence是borderline时，
      mechanistic transparency builds reviewer trust。Strategy：选最clean的SICA-win case
      作为motivating example(可能放Section 1)，选一个failure case放Section 5 limitations。
      Constraint quality = 72% accuracy confirms SICA不是"optimal"——future work可improve
      extraction quality (better prompting, verification step) for stronger gains。
      这也explains为什么C0 alone不predict gap magnitude：constraint quality是hidden variable。

  - name: overhead_analysis
    plan_id: exp-009
    description: "Wall-time breakdown per phase on exp-001 data"
    expected_results:
      avg_total_time_per_question_s: 58.2
      breakdown:
        generation_s: 42.5
        generation_pct: 73.0
        constraint_extraction_s: 12.8
        constraint_extraction_pct: 22.0
        maxsat_solving_s: 0.3
        maxsat_solving_pct: 0.5
        answer_aggregation_s: 2.6
        answer_aggregation_pct: 4.5
      sc_equivalent_time_s: 42.5
      sica_overhead_vs_sc_pct: 37.0
      sica_overhead_absolute_s: 15.7
      marginal_cost_per_question_extraction_only: "$0.003"
      total_run_cost_212q: "$0.64"
      maxsat_timeout_rate: 0.005
      batch_throughput_questions_per_hour: 62
    result_rationale: >
      Generation (K=10 traces)是bottleneck且SC也需要这步——所以SICA的marginal overhead
      仅是constraint extraction(22%)和MaxSAT(0.5%)。MaxSAT solving几乎instant(<1s per problem)
      因为constraint数量小(~30 unique per problem)，Z3处理trivial。
      Extraction是主要overhead source：每条trace需要LLM call提取FOL(或regex parsing)。
      37% overhead在"是否worth it"的argument中是reasonable——如果gain是+2-4pp on a benchmark
      where random gets 50% and state-of-art gets 75%，+2pp是meaningful improvement at moderate cost。
      但reviewer可能argue"37% more compute for 2pp gain is not practical"——
      defense: (1) generation cost is sunk (user already runs SC), (2) extraction可batch/parallelize,
      (3) marginal dollar cost <$1 for full benchmark run。
    tables:
      - name: "Table 10: Computational Overhead Analysis"
        columns: [Phase, Time_s, Pct_Total, Shared_with_SC]
        rows:
          - [Trace Generation (K=10), 42.5, "73%", Yes]
          - [Constraint Extraction, 12.8, "22%", No]
          - [MaxSAT Solving, 0.3, "0.5%", No]
          - [Answer Aggregation, 2.6, "4.5%", "Partial"]
          - [Total, 58.2, "100%", "—"]
          - [SICA Marginal Overhead, 15.7, "37%*", "—"]
    figures_description:
      - "Fig 12: Stacked bar chart — time breakdown per phase, with SC-shared portion highlighted"
    analysis: >
      Overhead analysis的framing：不是"SICA costs 37% more"而是"SICA adds 16s per question
      on top of generation that SC already requires"。Dollar cost framing($0.003/question marginal)
      更compelling than percentage。Reviewer可能ask "why not just increase K instead of adding
      extraction overhead?"——answer from exp-002: increasing K alone doesn't help when ties still occur
      and random resolution is needed; SICA resolves ties principally regardless of K。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6fb49c8-93f3-4e5f-b24d-8bdb5fc24532",
  "isSidechain": false,
  "requestId": "req_011Cb5gpTvMY2ZJcGT4juN6d",
  "type": "assistant",
  "uuid": "09c39084-c176-4f45-a3a8-f29a384c26fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "7a4553d3-7c73-4cf5-891f-9f1e40bddb33",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VfT5udU95NACYGn5greyZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11114,
      "cache_read_input_tokens": 11841,
      "output_tokens": 9898,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11114,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 9898,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11114,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11114
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：FOLIO增益在扩展后缩小但仍正向，ProofWriter仍无增益，K消融有方向性但噪声大，统计显著性边缘 核心假设：['FOLIO gap从+6.7pp缩小到+3-4pp（部分tiebreak wins被更大样本稀释）', 'ProofWriter在扩展数据上仍~0pp（domain差异真实存在，不是样…",
  "leafUuid": "09c39084-c176-4f45-a3a8-f29a384c26fa",
  "sessionId": "7a4553d3-7c73-4cf5-891f-9f1e40bddb33"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "SICA Expanded Results on 200+ Questions with K Ablation and C0 Validation",
  "sessionId": "7a4553d3-7c73-4cf5-891f-9f1e40bddb33"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：FOLIO增益在扩展后缩小但仍正向，ProofWriter仍无增益，K消融有方向性但噪声大，统计显著性边缘 核心假设：['FOLIO gap从+6.7pp缩小到+3-4pp（部分tiebreak wins被更大样本稀释）', 'ProofWriter在扩展数据上仍~0pp（domain差异真实存在，不是样…",
  "leafUuid": "09c39084-c176-4f45-a3a8-f29a384c26fa",
  "sessionId": "7a4553d3-7c73-4cf5-891f-9f1e40bddb33"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "SICA Expanded Results on 200+ Questions with K Ablation and C0 Validation",
  "sessionId": "7a4553d3-7c73-4cf5-891f-9f1e40bddb33"
}
```

---
