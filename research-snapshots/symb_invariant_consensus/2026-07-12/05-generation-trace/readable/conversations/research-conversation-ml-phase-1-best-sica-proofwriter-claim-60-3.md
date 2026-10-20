# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：扩展实验确认 SICA 在非推理模型上有统计显著增益，ProofWriter 出现非零增益，三条 claim 均可原样提交 核心假设：['60题的 +3

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/e6146a27-40f1-4f0e-823d-88606fe26a73.jsonl`
- **Structured JSON:** [`5d2d0f85bf838eeedcf9.json`](../../sessions/5d/5d2d0f85bf838eeedcf9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T05:42:14.737Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T05:42:14.737Z",
  "sessionId": "e6146a27-40f1-4f0e-823d-88606fe26a73",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：扩展实验确认 SICA 在非推理模型上有统计显著增益，ProofWriter 出现非零增益，三条 claim 均可原样提交\n核心假设：['60题的 +3.3pp gap 在 804 题上保持或扩大（非抽样偶然）', 'K=12 下 tie 频率足够高（≥8% 的题出现 tie），使 tiebreak 机制贡献稳健', 'ProofWriter D5 的 C0 ≥ 30%，SICA 在该域也能捕获部分增益', 'C0 与 SICA-SC gap 呈单调正相关，7B/14B/72B 三点拟合清晰']\n关键指标范围：{'sica_sc_gap_combined_pp': [3.0, 5.5], 'folio_gap_pp': [5.0, 8.0], 'proofwriter_gap_pp': [1.0, 3.0], 'bootstrap_p_combined': [0.01, 0.05], 'c0_combined_expanded': [0.4, 0.55], 'tiebreak_win_rate': [0.7, 0.85], 'tie_question_fraction': [0.08, 0.15], 'k_ablation_best_gap_pp': [4.0, 7.0]}\n叙事方向：原始 framing 完全成立。标题可用 \"Principled Symbolic Consensus Improves LLM Reasoning\"。 三条 claim 原样保留：C1 用扩展实验的显著 p 值支撑，C2 用 QwQ 负结果 + 多模型 C0 梯度支撑， C3 用 C0-gap 散点图支撑。ProofWriter 非零增益消除 \"domain-specific\" 攻击面。 Operating regime 作为理论贡献锦上添花，而非防御性 reframe。EMNLP main 强投。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\nfocus: Key tension: SICA's gain is entirely from principled tiebreaking (4/60 questions, all 6:6 ties). Reviewers will attack statistical significance (p=0.317) and question overhead vs benefit. The operating regime characterization (reasoning vs instruction model) is the primary intellectual contribution. Expanded 200+ question results and K ablation are planned but not yet available. ProofWriter shows 0pp gain — domain generalization is a weakness.\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Fallback: AAAI 2027 (Aug 1)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条)\n1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).\n2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is conditional on trace diversity — SICA adds value when model outputs are diverse (instruction models, C0>20%) but provably degenerates to SC when models are self-consistent (reasoning models, C0<5%). This is a model property, not a task property.\n3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.\n\n## Core Insight\nSymbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that model architecture (reasoning vs instruction) determines the operating regime. This transforms SICA from \"yet another ensemble method\" into \"a method with formally characterizable applicability boundaries.\"\n\n## Story Spine\n- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.\n- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.\n- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75% win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) and show it's governed by model type, not task type.\n- **Headline result template**: \"On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → exp-001: Expand to 200+ questions for statistical power\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K sensitivity showing benefit pattern; exp-009: overhead analysis\n3. **\"Only one non-reasoning model\"** → exp-004: Add Qwen2.5-7B for scaling; exp-007: 72B-AWQ for camera-ready\n4. **\"ProofWriter shows 0pp gain\"** → Domain analysis in exp-001 expanded results\n5. **\"Random tiebreak baseline closes the gap\"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison\n6. **\"Why not just use a reasoning model?\"** → exp-005: QwQ-32B data shows reasoning models are self-consistent (don't need consensus improvement), but instruction models (cheaper, more deployed) benefit from SICA\n\n## Venue Fit Risks\n- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the \"operating regime characterization\" — the tiebreaking mechanism is evidence, not the claim.\n- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.\n- Negative results: QwQ-32B data must be presented as insight (\"When Does Symbolic Consensus Degenerate?\"), not failure.\n- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: RUNNING\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,12,16,20) on D012''s 60 questions. Key questions:\n    does SICA benefit depend on tiebreaks? What happens at odd K (no even splits)?\n    How does tiebreak frequency change with K?'\n  priority: P0\n  gpu_budget_hours: 5\n  deps: []\n  status: planned\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Third model for Claim 2 operating regime.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: 'D019 升级 P2→P1. 执行顺序: exp-002 (K ablation) → exp-004 (7B) → exp-007 (72B-AWQ).\n    72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX PRO 6000 单卡可放。'\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T05:42:14.743Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T05:42:14.743Z",
  "sessionId": "e6146a27-40f1-4f0e-823d-88606fe26a73"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T05:42:14.767Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：扩展实验确认 SICA 在非推理模型上有统计显著增益，ProofWriter 出现非零增益，三条 claim 均可原样提交
核心假设：['60题的 +3.3pp gap 在 804 题上保持或扩大（非抽样偶然）', 'K=12 下 tie 频率足够高（≥8% 的题出现 tie），使 tiebreak 机制贡献稳健', 'ProofWriter D5 的 C0 ≥ 30%，SICA 在该域也能捕获部分增益', 'C0 与 SICA-SC gap 呈单调正相关，7B/14B/72B 三点拟合清晰']
关键指标范围：{'sica_sc_gap_combined_pp': [3.0, 5.5], 'folio_gap_pp': [5.0, 8.0], 'proofwriter_gap_pp': [1.0, 3.0], 'bootstrap_p_combined': [0.01, 0.05], 'c0_combined_expanded': [0.4, 0.55], 'tiebreak_win_rate': [0.7, 0.85], 'tie_question_fraction': [0.08, 0.15], 'k_ablation_best_gap_pp': [4.0, 7.0]}
叙事方向：原始 framing 完全成立。标题可用 "Principled Symbolic Consensus Improves LLM Reasoning"。 三条 claim 原样保留：C1 用扩展实验的显著 p 值支撑，C2 用 QwQ 负结果 + 多模型 C0 梯度支撑， C3 用 C0-gap 散点图支撑。ProofWriter 非零增益消除 "domain-specific" 攻击面。 Operating regime 作为理论贡献锦上添花，而非防御性 reframe。EMNLP main 强投。


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
    high-baseline non-reasoning model. Third model for Claim 2 operating regime.'
  priority: P1
  gpu_budget_hours: 4
  deps:
  - exp-001
  status: planned
  note: 'D019 升级 P2→P1. 执行顺序: exp-002 (K ablation) → exp-004 (7B) → exp-007 (72B-AWQ).
    72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX PRO 6000 单卡可放。'
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
  "promptId": "c3b0a104-aeb2-40fc-b1cc-42e2bda55502",
  "type": "user",
  "uuid": "c23993e9-a128-495f-b12f-25663e388c42",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e6146a27-40f1-4f0e-823d-88606fe26a73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T05:42:14.765Z_

```json
{
  "parentUuid": "c23993e9-a128-495f-b12f-25663e388c42",
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
  "uuid": "f61fa2a9-97af-41e5-92a1-524f6946aa12",
  "timestamp": "2026-05-16T05:42:14.765Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e6146a27-40f1-4f0e-823d-88606fe26a73",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T05:42:14.766Z_

```json
{
  "parentUuid": "f61fa2a9-97af-41e5-92a1-524f6946aa12",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0f2c7c22-7f9f-4989-8e34-b4902609d498",
  "timestamp": "2026-05-16T05:42:14.766Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e6146a27-40f1-4f0e-823d-88606fe26a73",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：扩展实验确认 SICA 在非推理模型上有统计显著增益，ProofWriter 出现非零增益，三条 claim 均可原样提交 核心假设：['60题的 +3.3pp gap 在 804 题上保持或扩大（非抽样偶然）', 'K=12 下 tie 频率足够高（≥8% 的题出现 tie），使 tiebreak 机制贡献…",
  "leafUuid": "0f2c7c22-7f9f-4989-8e34-b4902609d498",
  "sessionId": "e6146a27-40f1-4f0e-823d-88606fe26a73"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Symbolic consensus operating regime characterization on expanded datasets",
  "sessionId": "e6146a27-40f1-4f0e-823d-88606fe26a73"
}
```

---

### Assistant

_source line 8 · 2026-05-16T05:42:41.285Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment plan, under the "best" tier scenario. I need to provide result_rationale for each prediction explaining why these results would occur under this tier.

Let me go through each experiment and generate predictions based on the best tier definition:

**Best tier definition:**
- SICA's +3.3pp gap holds or grows on 804 questions
- Bootstrap p < 0.05
- ProofWriter shows non-zero gain
- C0-gap correlation is clear across 7B/14B/72B
- All 3 claims can be submitted as-is


Now I'm establishing the target ranges for each key metric under the best tier scenario, which will guide my predictions across all experiments.

For exp-001, I'm projecting that the expanded SICA model should show meaningful gains on FOLIO around 6 percentage points over the baseline, with a smaller but still positive improvement on ProofWriter, combining to roughly 3.5-4 percentage points overall gap with a p-value in the 0.02-0.03 range. For exp-002, I'm planning to test different K values across a smaller sample to identify the optimal configuration.

Now looking at the ablation results, it seems even K values produce more ties, with K=12 being the sweet spot where SICA's tiebreak advantage is most pronounced. For exp-003, I need to validate that SICA's tiebreak strategy significantly outperforms random and other baselines across the full dataset. For exp-004, I'm expecting the 7B model to show larger SICA gains since weaker models generate more diverse outputs and thus more ties for SICA to resolve. For exp-005, I'm starting to examine how QwQ-32B operates in this regime.

The QwQ data already exists with near-zero C0, so that just needs formatting. For exp-006, I want to plot the relationship between C0 and SICA gap across all model scales to show the clear monotonic pattern. For exp-007, the 72B AWQ variant should fall between the 14B and QwQ results with modest C0 and small gap. For exp-008, I'm planning qualitative case studies to illustrate where constraint quality matters most.

Now I'm thinking about exp-009 to analyze the wall-time overhead and demonstrate it's acceptable, then I'll organize all of this in YAML format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f2c7c22-7f9f-4989-8e34-b4902609d498",
  "isSidechain": false,
  "requestId": "req_011Cb5iMUjCvc2s7FthQ6mmC",
  "type": "assistant",
  "uuid": "7f002422-bd58-488f-9562-ce361b7087f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e6146a27-40f1-4f0e-823d-88606fe26a73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AfrN1GM6yZG26jRFpramsW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11035,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11035,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12142,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11035
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

_source line 9 · 2026-05-16T05:46:08.527Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。标题可用 "Principled Symbolic Consensus Improves LLM Reasoning"。
  三条 claim 原样保留：C1 用扩展实验的显著 p 值支撑，C2 用 QwQ 负结果 + 多模型 C0 梯度支撑，
  C3 用 C0-gap 散点图支撑。ProofWriter 非零增益消除 "domain-specific" 攻击面。
  Operating regime 作为理论贡献锦上添花，而非防御性 reframe。EMNLP main 强投。

imagined_experiments:
  - name: sica_expanded_14b
    plan_id: exp-001
    description: "Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12, T=0.7"
    expected_results:
      sica_accuracy_combined: 0.713
      sc_accuracy_combined: 0.675
      sica_sc_gap_combined_pp: 3.8
      folio_sica_accuracy: 0.794
      folio_sc_accuracy: 0.735
      folio_gap_pp: 5.9
      proofwriter_sica_accuracy: 0.686
      proofwriter_sc_accuracy: 0.668
      proofwriter_gap_pp: 1.8
      bootstrap_p_combined: 0.023
      bootstrap_p_folio: 0.018
      bootstrap_p_proofwriter: 0.11
      c0_combined: 0.47
      c0_folio: 0.42
      c0_proofwriter: 0.50
      tie_question_fraction_combined: 0.11
      tie_question_fraction_folio: 0.13
      tie_question_fraction_proofwriter: 0.10
      tiebreak_win_rate: 0.76
      total_constraints_raw: ~78000
      total_constraints_unique: ~23000
      maxsat_exclusion_rate: 0.031
      wall_time_hours: ~13
    result_rationale: >
      D012 的 60 题结果中，14B 的 C0=53.3%，说明约半数题存在多候选答案，SICA 有操作空间。
      扩展到 804 题后，FOLIO 从 30→204 题——该数据集本身推理链多样性高（FOL 翻译歧义多），
      C0 预期维持 ~42%，gap 从 6.7pp 略回归均值至 ~5.9pp（60 题的 6.7pp 含抽样方差上浮）。
      ProofWriter D5 是深度推理链（depth-5），14B 在长链上更容易产生中间步骤分歧，
      C0 预期 ~50%；但 PW 的正确答案更确定（二分类 True/False），
      MaxSAT 的约束质量在形式化推理上更高，使 tiebreak 有效但 margin 较小（1.8pp）。
      804 题的 bootstrap 显著性：combined gap 3.8pp 在 n=804 下标准误约 1.5pp，
      z≈2.5 对应 p≈0.023，落入 [0.01, 0.05] 区间。
      Tie 频率 ~11% 符合 K=12 偶数采样的概率预期：
      K=12 下 6:6 tie 概率约 C(12,6)/2^12 ≈ 0.225 乘以双候选题比例 ~0.47 ≈ 0.106。
      Tiebreak 胜率 76% 反映 MaxSAT 约束加权在多数情况下指向正确答案，
      但约 24% 的 tie 中约束本身也有噪声导致错判。
    tables:
      - name: "Table 1: Main Results — SICA vs SC on 804 Questions"
        columns: [Dataset, N, SC_Acc, SICA_Acc, Gap_pp, p_value, C0]
        rows:
          - [FOLIO, 204, 73.5, 79.4, +5.9, 0.018, 0.42]
          - [ProofWriter_D5, 600, 66.8, 68.6, +1.8, 0.11, 0.50]
          - [Combined, 804, 67.5, 71.3, +3.8, 0.023, 0.47]
      - name: "Table 2: Tiebreak Analysis (K=12)"
        columns: [Metric, FOLIO, ProofWriter, Combined]
        rows:
          - [Tie_questions, "27/204 (13.2%)", "60/600 (10.0%)", "87/804 (10.8%)"]
          - [SICA_wins_on_ties, "21/27 (77.8%)", "45/60 (75.0%)", "66/87 (75.9%)"]
          - [SC_wins_on_ties, "6/27 (22.2%)", "15/60 (25.0%)", "21/87 (24.1%)"]
    figures_description:
      - "Fig 1: Per-question accuracy delta (SICA − SC) histogram, 804 questions. 大部分 delta=0（非 tie 题），正向 spike 在 tie 题上清晰可见。"
      - "Fig 2: Accuracy vs question index, FOLIO 204 题，SC 和 SICA 曲线对比，标注 tie 题位置。"
    analysis: >
      核心发现：60→804 扩展后 gap 从 3.3pp 微增至 3.8pp（FOLIO 贡献主力），
      p 值从 0.226 降至 0.023，跨过 0.05 显著性门槛。
      ProofWriter 从 0pp 升至 1.8pp——虽然单域不显著（p=0.11），
      但非零增益消除了 "SICA only works on FOLIO" 的攻击面。
      Combined p=0.023 支撑 C1 的统计显著性 claim。
      Tie 频率 10.8% 落入预期区间 [8%, 15%]，说明 K=12 的 tie 机制是稳健的、非偶发的。

  - name: sica_k_ablation_14b
    plan_id: exp-002
    description: "K sensitivity (K=6,8,12,16,20) on D012's 60 questions"
    expected_results:
      K6_sica_acc: 0.717
      K6_sc_acc: 0.700
      K6_gap_pp: 1.7
      K6_tie_fraction: 0.067
      K6_c0: 0.483
      K8_sica_acc: 0.733
      K8_sc_acc: 0.700
      K8_gap_pp: 3.3
      K8_tie_fraction: 0.083
      K8_c0: 0.517
      K12_sica_acc: 0.733
      K12_sc_acc: 0.700
      K12_gap_pp: 3.3
      K12_tie_fraction: 0.117
      K12_c0: 0.533
      K16_sica_acc: 0.750
      K16_sc_acc: 0.700
      K16_gap_pp: 5.0
      K16_tie_fraction: 0.133
      K16_c0: 0.550
      K20_sica_acc: 0.767
      K20_sc_acc: 0.717
      K20_gap_pp: 5.0
      K20_tie_fraction: 0.117
      K20_c0: 0.567
      best_gap_K: 16
      best_gap_pp: 5.0
      gpu_hours: ~4.5
    result_rationale: >
      K ablation 的物理直觉：K 增大 → 采样更多 traces → 两个效应同时发生：
      (1) SC 的 majority vote 更稳定（law of large numbers），SC accuracy 微升；
      (2) 偶数 K 下 tie 概率先升后降（binomial 分布 C(K,K/2)/2^K 在 K=12~16 附近最高），
      且更多 traces 给 MaxSAT 更多约束信息，tiebreak 质量提升。
      K=6：tie 概率低（C(6,3)/2^6=0.3125，但仅对多候选题），约 3-4 题出现 tie，
      SICA 赢其中 2-3 题，gap 小（1.7pp）。
      K=8：tie 频率上升，gap 达到 3.3pp。
      K=12：已有实验数据，3.3pp 复现。
      K=16：tie 的绝对数虽然与 K=12 相近（binomial peak 开始移走），但约束数量翻倍，
      MaxSAT 对 tie 的判断更准确，gap 升至 5.0pp。这是 best-gap K。
      K=20：SC 自身稳定性提高（更多 votes 压低 tie 概率），tie_fraction 回落至与 K=12 持平，
      但 SC baseline 也升至 71.7%，gap 维持 5.0pp。
      总体呈现 "先升后平" 的 gap-vs-K 曲线，best gap 在 K=16，符合 [4.0, 7.0] 区间。
    tables:
      - name: "Table 3: K Ablation on 60 Questions (Qwen2.5-14B-Instruct)"
        columns: [K, SC_Acc, SICA_Acc, Gap_pp, Tie_Frac, C0, Constraints_per_Q]
        rows:
          - [6, 70.0, 71.7, +1.7, 6.7%, 0.483, ~80]
          - [8, 70.0, 73.3, +3.3, 8.3%, 0.517, ~110]
          - [12, 70.0, 73.3, +3.3, 11.7%, 0.533, ~150]
          - [16, 70.0, 75.0, +5.0, 13.3%, 0.550, ~195]
          - [20, 71.7, 76.7, +5.0, 11.7%, 0.567, ~240]
    figures_description:
      - "Fig 3: SICA-SC gap (pp) vs K, bar chart with tie_fraction overlay line. 显示 gap 随 K 增大先陡升后趋平。"
      - "Fig 4: Tiebreak win rate vs K, 显示约束数量增加提升 tiebreak 质量。"
    analysis: >
      K ablation 回答两个关键问题：(1) SICA 的增益是否仅依赖 tie——是的，非 tie 题上 SICA≡SC，
      但 tie 频率随 K 变化是可预测的（binomial 模型）；(2) 最佳 K 是什么——K=16 达到 peak gap 5.0pp，
      但 K=12 是 cost-performance 最优点（gap 3.3pp，GPU 时间仅 K=16 的 75%）。
      这为论文提供了 practical recommendation：K=12 作为默认值，K=16 如果预算允许。
      Odd-K 未测试（odd K 不产生精确 tie），留作 appendix 说明。

  - name: tiebreak_baseline_analysis
    plan_id: exp-003
    description: "Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available data"
    expected_results:
      # On expanded 804 questions (using exp-001 data)
      sica_acc_804: 0.713
      sc_alphabetical_acc_804: 0.675
      sc_random_acc_804: 0.681
      sc_first_seen_acc_804: 0.670
      sica_vs_random_gap_pp: 3.2
      sica_vs_alphabetical_gap_pp: 3.8
      sica_vs_first_seen_gap_pp: 4.3
      # On original 60 questions (D012 reanalysis)
      sica_tiebreak_win_60q: "4/5 (80%)"
      random_tiebreak_expected_60q: "2.5/5 (50%)"
      alphabetical_tiebreak_60q: "3/5 (60%)"
      first_seen_tiebreak_60q: "2/5 (40%)"
    result_rationale: >
      Tiebreak baseline 分析的关键在于：SC-random 是最公平的 baseline，因为它不引入系统性偏差。
      在 804 题上，SC-random 的期望准确率 = SC-deterministic 在非 tie 题上的准确率
      + 0.5 × tie 题数量 / 总题数（tie 时 50/50 猜对）。
      计算：非 tie 题 717/804 的 SC acc 约 73.1%，tie 题 87/804 随机猜对 ~50%，
      所以 SC-random ≈ 0.731 × (717/804) + 0.5 × (87/804) ≈ 0.681。
      SICA 在 tie 题上 76% win rate → SICA 比 random 多赢 ~26% × 87 ≈ 22.6 题 → gap ≈ 2.8pp。
      但 SICA 在约束明确的 tie 题上几乎必赢，在约束噪声大的 tie 题上也不比 random 差太多
      （MaxSAT 在约束矛盾时退化为多数约束投票，仍然 ≥ random），因此 gap 为正。
      这回答了 reviewer 的 "random tiebreak closes the gap" 攻击：
      不能，因为 SICA 的 tiebreak 是 informed（基于逻辑约束），胜率显著高于 chance。
    tables:
      - name: "Table 4: Tiebreak Strategy Comparison (804 Questions)"
        columns: [Method, Acc, Gap_vs_SICA_pp, Tiebreak_Mechanism]
        rows:
          - [SICA, 71.3, "—", "MaxSAT weighted constraints"]
          - [SC-random, 68.1, -3.2, "Uniform random on ties"]
          - [SC-alphabetical, 67.5, -3.8, "Alphabetical first on ties"]
          - [SC-first-seen, 67.0, -4.3, "First generated answer on ties"]
    figures_description:
      - "Fig 5: Tiebreak accuracy comparison bar chart, 仅在 tie 题子集上展示四种方法的准确率。SICA 76% vs random 50% vs alphabetical 55% vs first-seen 43%。"
    analysis: >
      SICA 对 SC-random（最公平 baseline）仍有 3.2pp 优势，说明增益不是 "刚好比一个差的 tiebreak 规则好"，
      而是 MaxSAT 约束确实编码了有用的推理信息。First-seen 最差（67.0%）因为第一条 trace 往往是
      greedy-like 的，遇到难题时更可能犯错。Alphabetical 的 60% 有偶然成分（某些答案碰巧排序靠前且正确）。

  - name: sica_7b_scaling
    plan_id: exp-004
    description: "Run SICA with Qwen2.5-7B-Instruct on same 60 questions"
    expected_results:
      sica_accuracy: 0.633
      sc_accuracy: 0.567
      sica_sc_gap_pp: 6.7
      c0_multi_candidate_rate: 0.683
      tie_question_fraction: 0.15
      tiebreak_win_rate: 0.78
      folio_sica: 0.700
      folio_sc: 0.600
      folio_gap_pp: 10.0
      proofwriter_sica: 0.600
      proofwriter_sc: 0.550
      proofwriter_gap_pp: 5.0
      bootstrap_p: 0.087
      total_constraints_raw: ~4800
      constraint_quality_vs_14b: "lower — more parse failures, ~15% extraction failure rate"
      gpu_hours: ~1.5
    result_rationale: >
      7B 模型比 14B 弱，两个关键效应：
      (1) SC baseline 更低（56.7% vs 70.0%），因为 7B 的推理能力更弱；
      (2) C0 更高（68.3% vs 53.3%），因为 7B 的 trace 多样性更大——
      弱模型对同一问题产生不同推理路径的概率更高，表现为更多多候选答案和更多 ties。
      更高的 C0 + 更多 ties → SICA 有更大操作空间 → gap 扩大至 6.7pp。
      但约束提取质量下降（7B 的 FOL 翻译更多语法错误），部分抵消了 diversity 带来的优势。
      净效应：gap 翻倍（6.7 vs 3.3），但 absolute accuracy 下降。
      这完美支撑 C2（operating regime）和 C3（C0 as predictor）：
      C0 从 14B 的 53% 升至 7B 的 68%，gap 从 3.3pp 升至 6.7pp，单调正相关。
      Bootstrap p=0.087 在 60 题上不显著（预期内，n 太小），但方向一致。
    tables:
      - name: "Table 5: 7B vs 14B Comparison (60 Questions)"
        columns: [Model, SC_Acc, SICA_Acc, Gap_pp, C0, Tie_Frac]
        rows:
          - [Qwen2.5-7B-Instruct, 56.7, 63.3, +6.7, 0.683, 0.150]
          - [Qwen2.5-14B-Instruct, 70.0, 73.3, +3.3, 0.533, 0.117]
    figures_description:
      - "Fig 6: C0 vs SICA-SC gap scatter plot (初步两点 + QwQ 零点)。7B 在右上角，14B 在中间，QwQ 在原点附近。"
    analysis: >
      7B 数据点完美落在 C0-gap 正相关线上。结合 QwQ 的 (C0=3.6%, gap=0pp) 数据点，
      三点已经初步支撑 C3 claim。等 72B 数据补上后四点拟合将更有说服力。
      一个有趣的 insight：7B 的 SICA gap 更大，但 absolute accuracy 更低。
      这意味着 SICA 不是 "让弱模型变强" 的银弹，而是 "在模型本身的能力范围内最大化共识质量"。

  - name: qwq_32b_operating_regime
    plan_id: exp-005
    description: "QwQ-32B negative results formatted for Operating Regime Analysis section"
    expected_results:
      # 已有数据，不需要新实验
      aime_c0: 0.0
      aime_sica_sc_gap: 0.0
      folio_c0: 0.0
      folio_sica_sc_gap: 0.0
      proofwriter_c0: 0.1875
      proofwriter_sica_sc_gap: 0.0
      combined_c0: 0.036
      combined_sica_sc_gap: 0.0
      n_total: 48
      trace_entropy_qwq: 0.12
      trace_entropy_14b: 1.83
      trace_entropy_7b: 2.41
    result_rationale: >
      QwQ-32B 是 reasoning model，其 CoT 过程内部已经执行了隐式的 "多路径搜索 + 自我验证"，
      导致不同 temperature 采样出的 traces 几乎收敛到同一答案（C0≈0%）。
      这不是因为 QwQ 更 "聪明"（它确实更聪明，但关键不在准确率），
      而是因为 reasoning model 的训练目标（extended thinking + verification）压缩了输出分布。
      SICA 需要 trace diversity 来工作——当所有 K 条 traces 给出相同答案，
      MaxSAT 无论怎么加权都只能选同一个答案。SICA 在数学上退化为 SC。
      Trace entropy 量化了这一点：QwQ 的 0.12 bits 对比 14B 的 1.83 bits（15x 差距）。
      ProofWriter 上 QwQ 有 18.75% C0，但 n=16 太小且增益为零——
      因为 C0=18.75% 中的多候选题上 QwQ 的 "错误" trace 其约束一致性也很高（reasoning model 连犯错都很自洽），
      MaxSAT 无法区分正确和错误的一致性约束。
    tables:
      - name: "Table 6: Operating Regime — Reasoning vs Instruction Models"
        columns: [Model, Type, C0, SICA-SC_Gap, Trace_Entropy, N]
        rows:
          - [QwQ-32B, Reasoning, "3.6%", "0.0pp", 0.12, 48]
          - [Qwen2.5-14B-Instruct, Instruction, "53.3%", "+3.3pp", 1.83, 60]
          - [Qwen2.5-7B-Instruct, Instruction, "68.3%", "+6.7pp", 2.41, 60]
    figures_description:
      - "Fig 7: Operating regime diagram. X 轴 = C0, Y 轴 = SICA-SC gap. 左侧 'degenerate zone' (C0<10%), 右侧 'effective zone' (C0>20%). QwQ 在左，两个 instruction models 在右。"
    analysis: >
      这是论文的核心 intellectual contribution。不说 "SICA 不如 reasoning model"，
      而是说 "SICA 和 reasoning model 解决不同的问题"：reasoning model 通过内部验证压缩了输出分布，
      不需要外部共识机制；instruction model 输出多样性高，需要也能够从外部共识中获益。
      这是一个 model property，不是 task property——同一个 task (FOLIO) 在两种模型上表现完全不同。

  - name: c0_diagnostic_validation
    plan_id: exp-006
    description: "Plot C0 vs SICA-SC gap across all models and K values. Validate C0 as predictor."
    expected_results:
      data_points:
        - {model: "QwQ-32B", K: 12, C0: 0.036, gap_pp: 0.0}
        - {model: "Qwen2.5-72B-AWQ", K: 12, C0: 0.30, gap_pp: 1.7}
        - {model: "Qwen2.5-14B-Instruct", K: 6, C0: 0.483, gap_pp: 1.7}
        - {model: "Qwen2.5-14B-Instruct", K: 8, C0: 0.517, gap_pp: 3.3}
        - {model: "Qwen2.5-14B-Instruct", K: 12, C0: 0.533, gap_pp: 3.3}
        - {model: "Qwen2.5-14B-Instruct", K: 16, C0: 0.550, gap_pp: 5.0}
        - {model: "Qwen2.5-14B-Instruct", K: 20, C0: 0.567, gap_pp: 5.0}
        - {model: "Qwen2.5-7B-Instruct", K: 12, C0: 0.683, gap_pp: 6.7}
      pearson_r: 0.94
      spearman_rho: 0.93
      linear_fit_slope: 10.2
      linear_fit_intercept: -2.1
      linear_fit_r2: 0.88
      c0_threshold_for_positive_gap: 0.21
    result_rationale: >
      C0 与 gap 的正相关来自因果链：C0 高 → 更多题存在多候选 → 更多 tie → SICA 有操作空间 → gap 大。
      这不是 confound（比如 "弱模型 C0 高且 gap 大是因为 baseline 低"），
      因为 K ablation 在同一模型上也展现了 C0-gap 正相关（K 增大 → C0 微增 → gap 增大），
      排除了模型能力这个 confound。
      8 个数据点（4 models × varying K）的 Pearson r=0.94，线性拟合 R²=0.88。
      斜率 10.2 表示 C0 每增加 10pp，SICA-SC gap 增加约 1.0pp。
      截距 -2.1 表示 C0 需要超过 ~21% 才能期望正增益——这与 QwQ 的 C0=3.6%→gap=0
      和 D016 precheck 的 C0≥20% 作为 go/no-go 门槛一致。
      Spearman ρ=0.93 确认单调性（非线性关系也 OK）。
    tables:
      - name: "Table 7: C0 as Predictor — Linear Regression"
        columns: [Metric, Value]
        rows:
          - [Pearson_r, 0.94]
          - [Spearman_ρ, 0.93]
          - [Slope, "10.2 pp gap per unit C0"]
          - [Intercept, "-2.1pp"]
          - [R², 0.88]
          - [C0_threshold, "0.21 (gap > 0)"]
    figures_description:
      - "Fig 8 (论文核心图): C0 vs SICA-SC gap 散点图。X 轴 C0 [0, 0.7], Y 轴 gap [-1, 8]pp。4 种 model 用不同 marker，同 model 不同 K 用颜色深浅。线性回归线 + 95% CI band。阴影区域标注 'Degenerate Zone' (C0<0.21) 和 'Effective Zone'。"
      - "Fig 9: C0 的计算不需要运行 MaxSAT（只需要 traces），所以是 zero-cost predictor。示意图展示 practitioner workflow: generate K traces → compute C0 → if C0>20% then run SICA, else use SC。"
    analysis: >
      C3 claim 的核心证据。Pearson r=0.94 和 R²=0.88 在 8 个数据点上非常强。
      reviewer 可能的攻击：(1) 只有 8 个点——回应是这是 4 个不同模型 + K 变化，覆盖了 C0 从 3.6% 到 68% 的全范围；
      (2) 因果方向不确定——回应是 C0 是 SICA 的输入（先于 MaxSAT 计算），因果方向明确；
      (3) 更多模型可能打破单调性——acknowledge as limitation，但当前 4 models 跨越了 3B-72B 规模和 reasoning/instruction 两种类型。

  - name: sica_72b_awq
    plan_id: exp-007
    description: "Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions"
    expected_results:
      sica_accuracy: 0.800
      sc_accuracy: 0.783
      sica_sc_gap_pp: 1.7
      c0_multi_candidate_rate: 0.30
      tie_question_fraction: 0.067
      tiebreak_win_rate: 0.75
      folio_sica: 0.867
      folio_sc: 0.833
      folio_gap_pp: 3.3
      proofwriter_sica: 0.767
      proofwriter_sc: 0.767
      proofwriter_gap_pp: 0.0
      bootstrap_p: 0.34
      constraint_quality: "higher than 14B — fewer parse errors, more precise FOL"
      gpu_hours: ~3.5
      gpu_mem_gib: ~52
    result_rationale: >
      72B 是 "强 instruction model"——比 14B 聪明但仍是 instruction 架构（非 reasoning model），
      所以 C0 不会像 QwQ 那样降到零，但会显著低于 14B。
      预期 C0=30%：72B 的推理一致性更高（更多题所有 traces 给出相同答案），
      但遇到真正难题时仍会产生 divergence。
      SC baseline 高（78.3%），已接近 FOLIO/PW 的天花板，留给 SICA 的空间很小。
      Tie 频率低（6.7%），只有 ~4 题出现 tie，其中 SICA 赢 3 题 → gap 1.7pp。
      ProofWriter 上 72B 的 accuracy 已经够高，tie 可能 0-1 题 → gap 0pp。
      这个结果完美支撑 operating regime 叙事：72B 在 QwQ（C0→0, gap→0）和 14B（C0=53%, gap=3.3pp）之间，
      形成 7B→14B→72B→QwQ 的 C0 递减、gap 递减梯度。
      Bootstrap p=0.34 在 60 题上不显著——预期内，因为只有 4 题 tie 无法产生统计 power。
      这正是为什么 exp-007 是 P1 而非 P0：它的价值在于 C0-gap 散点图的第四个点，
      不在于独立的显著性检验。
    tables:
      - name: "Table 8: Model Scaling — 7B / 14B / 72B / QwQ (60 Questions)"
        columns: [Model, Size, Type, SC_Acc, SICA_Acc, Gap_pp, C0]
        rows:
          - [Qwen2.5-7B-Instruct, 7B, Instruction, 56.7, 63.3, +6.7, 0.683]
          - [Qwen2.5-14B-Instruct, 14B, Instruction, 70.0, 73.3, +3.3, 0.533]
          - [Qwen2.5-72B-AWQ, 72B, Instruction, 78.3, 80.0, +1.7, 0.300]
          - [QwQ-32B, 32B, Reasoning, "—", "—", 0.0, 0.036]
    figures_description:
      - "Fig 10: 四模型的 C0 和 gap 条形图并列。清晰展示 instruction model 的 size↑ → C0↓ → gap↓ 梯度，以及 reasoning model 的断崖式 C0 下降。"
    analysis: >
      72B 数据确认了 operating regime 的 scaling dimension：即使在同一架构系列内，
      模型规模增大也会降低 trace diversity（更强的模型更自信、更一致），
      从而缩小 SICA 的操作空间。但关键区分是 "缩小" vs "消失"：
      72B 的 C0=30% 仍远高于 QwQ 的 3.6%，说明 instruction→reasoning 的跃迁才是决定性的，
      而非单纯的规模增大。这为论文提供了更精细的 insight。

  - name: constraint_quality_case_studies
    plan_id: exp-008
    description: "Qualitative analysis of extracted constraints on 5-10 representative questions"
    expected_results:
      cases_analyzed: 8
      categories:
        correct_and_helpful: 5
        correct_but_redundant: 1
        incorrect_but_excluded: 1
        incorrect_and_harmful: 1
      example_folio_tie_win:
        question_summary: "FOLIO question about organizational membership and property inheritance"
        k12_vote_split: "6 True : 6 False"
        sica_answer: "True (correct)"
        sc_alphabetical: "False (wrong)"
        key_constraint: "∀x(Member(x,Org) → HasProperty(x,P)), weight=0.83"
        why_sica_wins: "6 True-traces 提取的约束互相一致（满足率 92%），6 False-traces 的约束自相矛盾（满足率 61%），MaxSAT 正确偏向 True。"
      example_proofwriter_miss:
        question_summary: "PW D5 深度链推理，5步推导"
        sica_answer: "False (wrong)"
        correct_answer: "True"
        why_sica_fails: "中间步骤的 FOL 翻译错误（否定词遗漏），导致约束指向错误方向。7/12 traces 含相同翻译错误。"
      extraction_failure_rate: 0.02
      avg_constraints_per_trace: 13.2
      avg_unique_constraints_per_question: 28.7
    result_rationale: >
      Case study 的目的是让 reviewer 看到 SICA 不是黑盒——约束有语义可解释性。
      在 best tier 下，多数 case 展示 SICA 的约束确实编码了推理中的逻辑关系，
      MaxSAT 的加权机制合理地偏向了一致性更高的答案。
      选择 8 个 case：5 个 SICA 正确发挥、1 个冗余但无害、1 个错误约束被 exclusion 机制过滤、
      1 个 SICA 犯错的反例（诚实展示局限性）。
      FOLIO 的 tie-win case 最有说服力：展示 MaxSAT 如何利用约束一致性区分两组 traces。
      ProofWriter 的 failure case 揭示了约束提取的瓶颈（FOL 翻译质量），
      为 future work（更好的 FOL extractor）提供了明确方向。
    tables: []
    figures_description:
      - "Fig 11: 一个 FOLIO tie-win case 的完整可视化：12 条 traces 的投票分布、提取的约束集合、MaxSAT 权重、最终判决。用颜色编码正确/错误 traces 和满足/违反的约束。"
      - "Fig 12: 约束质量分布直方图：extraction rate、parse success rate、semantic correctness rate（人工标注 50 条约束）。"
    analysis: >
      Case studies 将 SICA 从 "accuracy number goes up" 提升为 "we understand WHY it goes up"。
      5/8 cases 展示了约束的语义意义，1/8 的 failure case 防止 reviewer 说 "cherry-picked"。
      这是 qualitative contribution，在 EMNLP 评审中有加分作用。

  - name: overhead_analysis
    plan_id: exp-009
    description: "Wall-time breakdown per question: generation, constraint extraction, MaxSAT solving"
    expected_results:
      avg_total_time_per_question_s: 58.3
      avg_generation_time_s: 42.1
      avg_extraction_time_s: 14.8
      avg_maxsat_time_s: 1.4
      generation_fraction: 0.722
      extraction_fraction: 0.254
      maxsat_fraction: 0.024
      overhead_vs_sc_multiplier: 1.39
      overhead_vs_sc_description: "SC 只需 generation (42.1s)，SICA 额外需要 extraction+MaxSAT (16.2s)，增加 39% wall time"
      marginal_cost_per_pp_gain: "4.3s per 1pp accuracy gain"
      maxsat_z3_avg_time_ms: 47
      maxsat_z3_max_time_ms: 312
      constraint_extraction_method: "LLM-based (same model, separate prompt)"
      extraction_tokens_per_question: ~2800
    result_rationale: >
      Overhead 分析对 reviewer concern "is it worth it" 至关重要。
      Generation 占 72% wall time——这与 SC 相同（K=12 条 traces），不是 SICA 的 overhead。
      SICA 的真正 overhead 是 constraint extraction (25%) + MaxSAT solving (2.4%)。
      Extraction 用同模型做 FOL 翻译，每条 trace ~2800 tokens，12 traces 串行处理需要 ~14.8s。
      MaxSAT (Z3) 平均 47ms 每题——trivially fast，因为约束数通常 <100（Z3 处理数千约束毫无压力）。
      总 overhead multiplier 1.39x 意味着每题多花 39% 时间换取 3.8pp accuracy gain——
      这在多数应用场景下是 acceptable 的 trade-off。
      进一步：extraction 可以并行化（12 traces 同时提取），理论上压缩到 ~3s，
      使 multiplier 降至 1.10x。但当前实现是串行的，论文报告实际数字更诚实。
    tables:
      - name: "Table 9: Overhead Analysis (Qwen2.5-14B-Instruct, K=12, 804 Questions)"
        columns: [Stage, Avg_Time_s, Fraction, Parallelizable]
        rows:
          - [Trace_Generation, 42.1, "72.2%", "Yes (vLLM batched)"]
          - [Constraint_Extraction, 14.8, "25.4%", "Yes (per-trace independent)"]
          - [MaxSAT_Solving, 1.4, "2.4%", "No (single Z3 call)"]
          - [Total, 58.3, "100%", ""]
          - [SC_Equivalent, 42.1, "—", ""]
          - [SICA_Overhead, 16.2, "+38.5%", ""]
    figures_description:
      - "Fig 13: Stacked bar chart 展示 per-question wall time 分解。SC bar 只有 generation，SICA bar 有 generation + extraction + MaxSAT。MaxSAT 几乎不可见（太小了）。"
    analysis: >
      Key talking point：SICA 的 "重" 在约束提取（LLM 调用），不在 MaxSAT 求解。
      这意味着 (1) overhead 随 LLM inference 成本线性下降（模型越快，overhead 越低），
      (2) MaxSAT 本身不是瓶颈（可以扩展到更多约束），
      (3) 如果用 fine-tuned 小模型做 extraction 可以进一步降低 overhead（future work）。
      39% overhead 换 3.8pp gain 的 cost-effectiveness 优于大多数 ensembling 方法
      （如 majority voting over 2K traces 需要 100% overhead 且 gain 通常 <2pp）。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f002422-bd58-488f-9562-ce361b7087f0",
  "isSidechain": false,
  "requestId": "req_011Cb5iMUjCvc2s7FthQ6mmC",
  "type": "assistant",
  "uuid": "646153c0-5296-4a7a-9220-31c6abbe2baa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "e6146a27-40f1-4f0e-823d-88606fe26a73",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AfrN1GM6yZG26jRFpramsW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11035,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12142,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11035,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12142,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11035,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11035
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：扩展实验确认 SICA 在非推理模型上有统计显著增益，ProofWriter 出现非零增益，三条 claim 均可原样提交 核心假设：['60题的 +3.3pp gap 在 804 题上保持或扩大（非抽样偶然）', 'K=12 下 tie 频率足够高（≥8% 的题出现 tie），使 tiebreak 机制贡献…",
  "leafUuid": "646153c0-5296-4a7a-9220-31c6abbe2baa",
  "sessionId": "e6146a27-40f1-4f0e-823d-88606fe26a73"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Symbolic consensus operating regime characterization on expanded datasets",
  "sessionId": "e6146a27-40f1-4f0e-823d-88606fe26a73"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：扩展实验确认 SICA 在非推理模型上有统计显著增益，ProofWriter 出现非零增益，三条 claim 均可原样提交 核心假设：['60题的 +3.3pp gap 在 804 题上保持或扩大（非抽样偶然）', 'K=12 下 tie 频率足够高（≥8% 的题出现 tie），使 tiebreak 机制贡献…",
  "leafUuid": "646153c0-5296-4a7a-9220-31c6abbe2baa",
  "sessionId": "e6146a27-40f1-4f0e-823d-88606fe26a73"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Symbolic consensus operating regime characterization on expanded datasets",
  "sessionId": "e6146a27-40f1-4f0e-823d-88606fe26a73"
}
```

---
