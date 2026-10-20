# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：扩展实验增益接近零或为负，tiebreak 有效但 tie 极少，accuracy claim 不可持续，需完全 reframe 为分析/诊断贡献 核

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/a0daf9ff-2536-4882-956b-5d4805db895f.jsonl`
- **Structured JSON:** [`41cdd169c26c20b03a5b.json`](../../sessions/41/41cdd169c26c20b03a5b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T06:00:14.575Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T06:00:14.575Z",
  "sessionId": "a0daf9ff-2536-4882-956b-5d4805db895f",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：扩展实验增益接近零或为负，tiebreak 有效但 tie 极少，accuracy claim 不可持续，需完全 reframe 为分析/诊断贡献\n核心假设：['60题的 +3.3pp 是小样本噪声，804 题 gap < 1.5pp', 'K=12 下 even-split tie 极少（< 3%），tiebreak 机制正确但几乎无触发场景', 'MaxSAT exclusion rate 在扩展数据上仍很低（< 3%），constraint 对多数题不改变投票分布', 'C0 在 14B 扩展集上降至 25-35%（60题高估了 diversity）']\n关键指标范围：{'sica_sc_gap_combined_pp': [-0.5, 1.5], 'folio_gap_pp': [0.5, 3.5], 'proofwriter_gap_pp': [-1.5, 0.0], 'bootstrap_p_combined': [0.15, 0.5], 'c0_combined_expanded': [0.22, 0.35], 'tiebreak_win_rate': [0.5, 0.65], 'tie_question_fraction': [0.01, 0.04], 'k_ablation_best_gap_pp': [0.5, 2.5]}\n叙事方向：彻底放弃 accuracy improvement claim。Reframe 为： \"Why Symbolic Consensus Fails: A Diagnostic Framework for Constraint-Based LLM Aggregation\"。 核心贡献变为三层：(1) C0 diagnostic framework — 零成本判断任何 consensus method 是否值得部署， (2) 推理模型 vs 指令模型的 trace diversity 根因分析（不是 SICA 特有的发现， 而是对所有 ensemble/consensus 方法都成立的架构层洞察）， (3) 对 \"symbolic structure helps reasoning\" 这一宽泛假设的精确化否定条件。 Tiebreak 机制的高 win rate 作为 \"method is correct but regime is narrow\" 的证据。 QwQ 负结果从配角升为主角。这是一篇 \"characterization + negative result\" 的 paper， 用 Findings of EMNLP 或 EMNLP main short 投，仍不降级 venue 但可能需要接受 非 main long 的 track。若坚持 main long，需补充 2-3 个额外模型（7B、72B、Llama） 来撑起 operating regime 分析的广度。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\nfocus: Key tension: SICA's gain is entirely from principled tiebreaking (4/60 questions, all 6:6 ties). Reviewers will attack statistical significance (p=0.317) and question overhead vs benefit. The operating regime characterization (reasoning vs instruction model) is the primary intellectual contribution. Expanded 200+ question results and K ablation are planned but not yet available. ProofWriter shows 0pp gain — domain generalization is a weakness.\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Fallback: AAAI 2027 (Aug 1)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条)\n1. **Principled Tiebreaking**: SICA resolves Self-Consistency voting ties through symbolic constraint weighting, achieving higher accuracy than arbitrary tiebreak rules on logic reasoning benchmarks (FOLIO +6.7pp, combined +3.3pp on 60 questions; target: statistically significant on 200+ questions).\n2. **Operating Regime Characterization**: The effectiveness of symbolic consensus is conditional on trace diversity — SICA adds value when model outputs are diverse (instruction models, C0>20%) but provably degenerates to SC when models are self-consistent (reasoning models, C0<5%). This is a model property, not a task property.\n3. **C0 as Practical Diagnostic**: Multi-candidate rate (C0) serves as a zero-cost predictor of whether SICA deployment will yield gains over SC, enabling practitioners to decide without running full symbolic analysis.\n\n## Core Insight\nSymbolic constraint consensus doesn't uniformly improve reasoning — it specifically helps when there IS disagreement to resolve. We provide the first systematic study of WHEN symbolic consensus adds value, revealing that model architecture (reasoning vs instruction) determines the operating regime. This transforms SICA from \"yet another ensemble method\" into \"a method with formally characterizable applicability boundaries.\"\n\n## Story Spine\n- **Problem**: Self-Consistency (SC) aggregates LLM reasoning paths via majority voting but treats all chains as opaque votes, discarding the logical structure within them. When votes are tied, SC falls back to arbitrary rules (alphabetical, random) with no principled resolution.\n- **Existing approaches & gaps**: SC (Wang et al. 2023) — pure voting, no reasoning structure. USC (Chen et al. 2023) — universal SC, still voting-based. None exploit the formal logical structure within reasoning traces for consensus, and none characterize when symbolic methods help vs. don't.\n- **Our framing**: SICA extracts first-order logic constraints from reasoning traces and uses weighted partial MAX-SAT to find the globally consistent answer. We show this provides principled tiebreaking (75% win rate on ties vs 25% for SC) but only when trace diversity exists. We formalize this as C0 (multi-candidate rate) and show it's governed by model type, not task type.\n- **Headline result template**: \"On FOLIO, SICA achieves 80.0% vs SC's 73.3% (+6.7pp) with Qwen2.5-14B-Instruct. On the same benchmarks with QwQ-32B, SICA degenerates to SC (C0=3.6%), revealing that symbolic consensus effectiveness is governed by trace diversity, not task difficulty.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → exp-001: Expand to 200+ questions for statistical power\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K sensitivity showing benefit pattern; exp-009: overhead analysis\n3. **\"Only one non-reasoning model\"** → exp-004: Add Qwen2.5-7B for scaling; exp-007: 72B-AWQ for camera-ready\n4. **\"ProofWriter shows 0pp gain\"** → Domain analysis in exp-001 expanded results\n5. **\"Random tiebreak baseline closes the gap\"** → exp-003: Direct SICA vs SC-random vs SC-deterministic comparison\n6. **\"Why not just use a reasoning model?\"** → exp-005: QwQ-32B data shows reasoning models are self-consistent (don't need consensus improvement), but instruction models (cheaper, more deployed) benefit from SICA\n\n## Venue Fit Risks\n- EMNLP: Contribution may feel narrow if framed as ONLY tiebreaking. Primary intellectual contribution is the \"operating regime characterization\" — the tiebreaking mechanism is evidence, not the claim.\n- Cross-discipline: Combines formal logic (MAX-SAT) with NLP (LLM reasoning). MAX-SAT needs clear explanation for NLP audience.\n- Negative results: QwQ-32B data must be presented as insight (\"When Does Symbolic Consensus Degenerate?\"), not failure.\n- Statistical power: 60-question results are fragile. 200+ question expansion is prerequisite for credible submission.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: RUNNING\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,12,16,20) on D012''s 60 questions. Key questions:\n    does SICA benefit depend on tiebreaks? What happens at odd K (no even splits)?\n    How does tiebreak frequency change with K?'\n  priority: P0\n  gpu_budget_hours: 5\n  deps: []\n  status: planned\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Third model for Claim 2 operating regime.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: 'D019 升级 P2→P1. 执行顺序: exp-002 (K ablation) → exp-004 (7B) → exp-007 (72B-AWQ).\n    72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX PRO 6000 单卡可放。'\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T06:00:14.579Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T06:00:14.579Z",
  "sessionId": "a0daf9ff-2536-4882-956b-5d4805db895f"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T06:00:14.620Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：扩展实验增益接近零或为负，tiebreak 有效但 tie 极少，accuracy claim 不可持续，需完全 reframe 为分析/诊断贡献
核心假设：['60题的 +3.3pp 是小样本噪声，804 题 gap < 1.5pp', 'K=12 下 even-split tie 极少（< 3%），tiebreak 机制正确但几乎无触发场景', 'MaxSAT exclusion rate 在扩展数据上仍很低（< 3%），constraint 对多数题不改变投票分布', 'C0 在 14B 扩展集上降至 25-35%（60题高估了 diversity）']
关键指标范围：{'sica_sc_gap_combined_pp': [-0.5, 1.5], 'folio_gap_pp': [0.5, 3.5], 'proofwriter_gap_pp': [-1.5, 0.0], 'bootstrap_p_combined': [0.15, 0.5], 'c0_combined_expanded': [0.22, 0.35], 'tiebreak_win_rate': [0.5, 0.65], 'tie_question_fraction': [0.01, 0.04], 'k_ablation_best_gap_pp': [0.5, 2.5]}
叙事方向：彻底放弃 accuracy improvement claim。Reframe 为： "Why Symbolic Consensus Fails: A Diagnostic Framework for Constraint-Based LLM Aggregation"。 核心贡献变为三层：(1) C0 diagnostic framework — 零成本判断任何 consensus method 是否值得部署， (2) 推理模型 vs 指令模型的 trace diversity 根因分析（不是 SICA 特有的发现， 而是对所有 ensemble/consensus 方法都成立的架构层洞察）， (3) 对 "symbolic structure helps reasoning" 这一宽泛假设的精确化否定条件。 Tiebreak 机制的高 win rate 作为 "method is correct but regime is narrow" 的证据。 QwQ 负结果从配角升为主角。这是一篇 "characterization + negative result" 的 paper， 用 Findings of EMNLP 或 EMNLP main short 投，仍不降级 venue 但可能需要接受 非 main long 的 track。若坚持 main long，需补充 2-3 个额外模型（7B、72B、Llama） 来撑起 operating regime 分析的广度。

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
  "promptId": "21979fbe-edf0-4795-b99f-ccc187e0947c",
  "type": "user",
  "uuid": "66a3f7b5-aa70-4e8c-acce-47ef5798f3ed",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "a0daf9ff-2536-4882-956b-5d4805db895f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T06:00:14.619Z_

```json
{
  "parentUuid": "66a3f7b5-aa70-4e8c-acce-47ef5798f3ed",
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
  "uuid": "67360774-6c60-4e12-b92c-e6453d2b2bc0",
  "timestamp": "2026-05-16T06:00:14.619Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "a0daf9ff-2536-4882-956b-5d4805db895f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T06:00:14.619Z_

```json
{
  "parentUuid": "67360774-6c60-4e12-b92c-e6453d2b2bc0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7591087f-0335-43c4-99c9-83f8cec43e8a",
  "timestamp": "2026-05-16T06:00:14.619Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "a0daf9ff-2536-4882-956b-5d4805db895f",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：扩展实验增益接近零或为负，tiebreak 有效但 tie 极少，accuracy claim 不可持续，需完全 reframe 为分析/诊断贡献 核心假设：['60题的 +3.3pp 是小样本噪声，804 题 gap < 1.5pp', 'K=12 下 even-split tie 极少（< 3%），ti…",
  "leafUuid": "7591087f-0335-43c4-99c9-83f8cec43e8a",
  "sessionId": "a0daf9ff-2536-4882-956b-5d4805db895f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing symbolic consensus effectiveness through operating regime analysis",
  "sessionId": "a0daf9ff-2536-4882-956b-5d4805db895f"
}
```

---

### Assistant

_source line 8 · 2026-05-16T06:00:44.746Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment plan, assuming the "worst" tier outcome. They want me to explain the rationale for each prediction under this worst-case scenario.

Let me carefully go through each experiment and predict what would happen in the worst tier:

**Worst tier definition:**
- 60题的 +3.3pp 是小样本噪声，804 题 gap < 1.5pp
- K=12 下 even-split tie 极少（< 3%），tiebreak 机制正确但几乎无触发场景


- MaxSAT exclusion rate 在扩展数据上仍很低（< 3%），constraint 对多数题不改变投票分布
- C0 在 14B 扩展集上降至 25-35%（60题高估了 diversity）

Now I'm looking at the expected metric ranges across these experiments to establish the baseline for worst-case predictions.

The key insight is that I need to completely shift away from claiming accuracy improvements and instead position this as a diagnostic study that characterizes how different constraints affect model behavior. Looking at the first experiment with the expanded 14B setup, the gap collapses dramatically under worst-case conditions—dropping from 3.3 percentage points down to nearly zero—while C0 plummets from 53% to around 28%, suggesting ProofWriter likely contributes nothing or negative signal. FOLIO maintains some positive effect but it's heavily diluted by the larger dataset. For the K ablation study, I'm planning to test different ensemble sizes to see how the tiebreak dynamics shift across K values of 6, 8, 12, and 16.

The remaining experiments are designed to stress-test this finding: the tiebreak baseline analysis will show that even with high win rates on ties, the overall accuracy gain is negligible when ties become rare in the expanded data; the 7B scaling experiment will explore whether weaker models generate more diverse outputs but lower-quality constraints; and the QwQ 32B experiment will examine how a much stronger model operates under these same conditions.

For the diagnostic and case study experiments, I'm planning to validate whether C0 actually correlates with the SICA gap across all conditions, then look at constraint quality qualitatively to see if they're often trivial or shallow. The 72B AWQ experiment will test whether higher capability models show even lower C0 and minimal gaps, while the overhead analysis will measure whether the computational cost of SICA justifies the small accuracy improvements we're seeing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7591087f-0335-43c4-99c9-83f8cec43e8a",
  "isSidechain": false,
  "requestId": "req_011Cb5jj5YukuKbHPTcZtpAM",
  "type": "assistant",
  "uuid": "a743d8a2-f619-491e-899f-35d05dc1442a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "a0daf9ff-2536-4882-956b-5d4805db895f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQmdWLLTWr7X8EKGwGyY7L",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11193,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8928,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11193,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8928,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11193
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

_source line 9 · 2026-05-16T06:03:24.605Z_

```yaml
tier: worst
narrative_guidance: >
  彻底放弃 accuracy improvement claim。Reframe 为：
  "Why Symbolic Consensus Fails: A Diagnostic Framework for Constraint-Based LLM Aggregation"。
  核心贡献变为三层：(1) C0 diagnostic framework — 零成本判断任何 consensus method 是否值得部署，
  (2) 推理模型 vs 指令模型的 trace diversity 根因分析，
  (3) 对 "symbolic structure helps reasoning" 假设的精确化否定条件。
  Tiebreak 机制的高 win rate 作为 "method is correct but regime is narrow" 的证据。
  QwQ 负结果从配角升为主角。目标 venue 调整为 Findings of EMNLP 或 EMNLP short。

imagined_experiments:
  - name: "sica_expanded_14b"
    plan_id: "exp-001"
    description: "PW D5 600 + FOLIO 204 = 804 questions, K=12, T=0.7, Qwen2.5-14B-Instruct"
    expected_results:
      sica_accuracy_combined: 0.695
      sc_accuracy_combined: 0.688
      sica_sc_gap_combined_pp: 0.7
      folio_sica_accuracy: 0.755
      folio_sc_accuracy: 0.735
      folio_gap_pp: 2.0
      proofwriter_sica_accuracy: 0.665
      proofwriter_sc_accuracy: 0.670
      proofwriter_gap_pp: -0.5
      bootstrap_p_combined: 0.32
      bootstrap_p_folio: 0.18
      c0_combined: 0.28
      c0_folio: 0.32
      c0_proofwriter: 0.25
      maxsat_exclusion_rate: 0.022
      tie_question_fraction: 0.025
      tiebreak_triggered_n: ~20
      tiebreak_win_rate: 0.60
      wall_time_hours: ~13
    result_rationale: >
      60题的C0=53%严重高估了总体diversity。扩展至804题后，大量ProofWriter D5题目对14B而言
      要么太简单（12/12一致正确）要么模式化错误（12/12一致错误），C0降至25-28%。
      FOLIO 204题中约32%有多候选，但多数多候选题的split是9:3或10:2而非6:6，
      MaxSAT在非tie情况下几乎不改变majority结果（exclusion rate仅2.2%）。
      真正的6:6 tie在K=12下约占2.5%（~20题），tiebreak在这20题上win rate约60%，
      贡献约0.7pp的combined gap。ProofWriter因其closed-world逻辑的规律性，
      14B在大样本上反而因constraint extraction引入微量噪声导致-0.5pp。
      Bootstrap p=0.32远未达显著性，confirm了小样本噪声假设。
    tables:
      - name: "Table 2: Expanded Results (804 Questions)"
        columns: ["Domain", "N", "SC Acc", "SICA Acc", "Gap (pp)", "C0", "Ties", "p-value"]
        rows:
          - ["FOLIO", 204, "73.5%", "75.5%", "+2.0", "0.32", "6 (2.9%)", "0.18"]
          - ["ProofWriter D5", 600, "67.0%", "66.5%", "-0.5", "0.25", "14 (2.3%)", "0.71"]
          - ["Combined", 804, "68.8%", "69.5%", "+0.7", "0.28", "20 (2.5%)", "0.32"]
          - ["D012 (reference)", 60, "70.0%", "73.3%", "+3.3", "0.53", "4 (6.7%)", "0.23"]
    figures_description:
      - "Fig 2: C0 histogram showing bimodal distribution — FOLIO questions cluster at C0>0.3 and C0=0, ProofWriter heavily concentrated at C0=0"
      - "Fig 3: Per-question SICA-SC difference vs C0, showing gain concentrated in C0>0.4 band but high variance"
    analysis: >
      关键发现：60题D012样本的C0=53%是selection bias——那60题本身就是从pilot中挑出的
      有趣/困难题目。扩展到完整benchmark后，绝大多数题对14B-Instruct而言diversity不足。
      SICA的正确性在tie scenario中得到验证（60% win rate > 25% random baseline），
      但tie场景太少（2.5%）导致aggregate gain不显著。
      这直接支持reframe：方法正确但operating regime狭窄。

  - name: "sica_k_ablation_14b"
    plan_id: "exp-002"
    description: "K=6,8,12,16,20 on D012's 60 questions, T=0.7, Qwen2.5-14B-Instruct"
    expected_results:
      k6_gap_pp: 1.7
      k6_c0: 0.40
      k6_tie_fraction: 0.033
      k8_gap_pp: 0.0
      k8_c0: 0.45
      k8_tie_fraction: 0.017
      k12_gap_pp: 3.3
      k12_c0: 0.53
      k12_tie_fraction: 0.067
      k16_gap_pp: 1.7
      k16_c0: 0.55
      k16_tie_fraction: 0.033
      k20_gap_pp: 0.0
      k20_c0: 0.58
      k20_tie_fraction: 0.017
      best_k: 12
      best_gap_pp: 3.3
      odd_k_gap_pp: 0.0
      correlation_c0_gap: 0.35
    result_rationale: >
      K ablation在worst档下揭示SICA gain完全是tie-driven artifact：
      - K=12恰好是唯一在这60题上产生较多even-split tie的值（4题=6.7%）
      - K=6时tie需要3:3，概率更低但发生1-2次；K=8需要4:4，几乎不发生
      - K=16/20时，larger sample使majority更稳定，tie概率指数下降
      - C0随K单调增加（更多samples→更可能出现minority answer），但tie fraction
        不单调——它取决于specific split概率
      - 如果测试odd K（K=7,9,11），tie在majority voting下数学上不可能，gap=0
      这证明SICA的gain机制是且仅是tiebreaking，没有通过constraint weighting
      在非tie场景改变outcome。MaxSAT exclusion在所有K下都<3%，
      从未翻转过一个non-tie majority。
    tables:
      - name: "Table 3: K Sensitivity Analysis"
        columns: ["K", "C0", "Tie Fraction", "SICA Acc", "SC Acc", "Gap (pp)", "Exclusion Rate"]
        rows:
          - [6, "40%", "3.3%", "71.7%", "70.0%", "+1.7", "2.8%"]
          - [8, "45%", "1.7%", "70.0%", "70.0%", "0.0", "2.5%"]
          - [12, "53%", "6.7%", "73.3%", "70.0%", "+3.3", "2.6%"]
          - [16, "55%", "3.3%", "71.7%", "70.0%", "+1.7", "2.4%"]
          - [20, "58%", "1.7%", "70.0%", "70.0%", "0.0", "2.2%"]
    figures_description:
      - "Fig 4: K vs Gap (pp) showing non-monotonic pattern — gap spikes only where tie fraction happens to be high, not where C0 is highest"
      - "Fig 5: Tie probability theoretical curve (binomial) vs observed, showing K=12 is near-optimal for tie generation but still produces ties on <7% of questions"
    analysis: >
      K ablation是worst档的核心evidence：它证明SICA gain完全由tie frequency决定，
      而非由constraint quality或MaxSAT reasoning决定。C0和gap的相关性仅0.35，
      因为C0测量的是diversity存在性，而gain需要diversity恰好50:50。
      这支持reframe中的"method is correct but regime is narrow"论点。
      Paper中应呈现为"SICA's mechanism activates only at exact vote parity"。

  - name: "tiebreak_baseline_analysis"
    plan_id: "exp-003"
    description: "SICA vs SC-random vs SC-deterministic on all available data (exp-001 results)"
    expected_results:
      expanded_tie_questions_n: 20
      sica_tiebreak_accuracy: 0.60
      random_tiebreak_expected_accuracy: 0.50
      alphabetical_tiebreak_accuracy: 0.45
      first_seen_tiebreak_accuracy: 0.40
      sica_vs_random_gap_on_ties_pp: 10.0
      sica_vs_random_gap_overall_pp: 0.25
      binomial_p_sica_vs_random: 0.25
    result_rationale: >
      在expanded 804题上，tie仅~20题。SICA在这20题上60% accuracy（12/20正确），
      random baseline期望50%（10/20），差距仅2题。Binomial test p=0.25（20次试验中
      观察12+ success vs null=0.5），远不显著。
      虽然per-tie的win rate（60%>50%）方向正确，但：
      (1) 样本太小无法统计确认优势
      (2) 即使优势真实，对overall accuracy贡献仅0.25pp（20题×10%÷804题）
      Alphabetical/first-seen表现更差验证了"任意tiebreak确实有害"，但SICA的优势
      幅度太小且统计不显著。这是"correct but narrow"的直接数字化呈现。
    tables:
      - name: "Table 4: Tiebreak Strategy Comparison (Tie Questions Only)"
        columns: ["Strategy", "Acc on Ties (N=20)", "Overall Acc (N=804)", "vs Random (pp)"]
        rows:
          - ["SICA (MaxSAT weighted)", "60.0%", "69.5%", "+0.25"]
          - ["Random (expected)", "50.0%", "69.3%", "—"]
          - ["Alphabetical", "45.0%", "69.1%", "-0.12"]
          - ["First-seen", "40.0%", "69.0%", "-0.25"]
    figures_description:
      - "Fig 6: Tiebreak accuracy comparison with 95% CI error bars — all strategies' CIs overlap heavily due to N=20"
    analysis: >
      Tiebreak analysis在worst档下支撑的narrative是：SICA作为tiebreak mechanism
      方向正确（优于random和deterministic），但operating regime（tie frequency=2.5%）
      使其对aggregate performance的贡献可以忽略。
      Paper framing：不claim accuracy gain，而是用tiebreak win rate作为
      "symbolic constraints carry real information"的evidence，然后pivot到
      "but the regime where this information matters is vanishingly narrow for current models"。

  - name: "sica_7b_scaling"
    plan_id: "exp-004"
    description: "Qwen2.5-7B-Instruct on same 60 questions, K=12, T=0.7"
    expected_results:
      sc_accuracy: 0.583
      sica_accuracy: 0.600
      sica_sc_gap_pp: 1.7
      c0_multi_candidate_rate: 0.65
      tie_fraction: 0.10
      tiebreak_win_rate: 0.50
      maxsat_exclusion_rate: 0.018
      constraint_quality_score: 0.45
      extraction_failure_rate: 0.12
    result_rationale: >
      7B模型验证了C0-as-predictor的方向性（C0=65% > 14B的53%），但在worst档下
      暴露了C0的insufficiency：更高的diversity不一定转化为更大的SICA gain。
      原因：7B的constraint extraction质量显著下降——更弱的模型生成的reasoning traces
      逻辑结构更松散，extracted FOL constraints更多是malformed或语义空洞的，
      MaxSAT weighting基于低质量constraints做出的决策不比random好。
      Tie fraction确实更高（10% vs 6.7%），但tiebreak win rate降至chance level（50%），
      因为constraint信号被noise淹没。最终gap仅1.7pp且完全不显著。
      这对paper的贡献：C0是necessary but not sufficient condition——
      还需要constraint quality（隐含model capability threshold）。
    tables:
      - name: "Table 5: Model Scaling and C0"
        columns: ["Model", "Params", "SC Acc", "C0", "Tie%", "Tiebreak WR", "Gap (pp)"]
        rows:
          - ["QwQ-32B", "32B (reasoning)", "72.7%", "0.036", "0%", "N/A", "0.0"]
          - ["Qwen2.5-14B-Instruct", "14B", "70.0%", "0.53", "6.7%", "75%", "+3.3"]
          - ["Qwen2.5-7B-Instruct", "7B", "58.3%", "0.65", "10%", "50%", "+1.7"]
    figures_description:
      - "Fig 7: Model capability vs C0 vs SICA gap — showing inverted-U relationship where optimal SICA regime requires both sufficient diversity AND sufficient constraint quality"
    analysis: >
      7B结果在worst档下是double-edged：一方面验证了C0与model type的关系（weaker→more diverse），
      另一方面破坏了C0作为单一predictor的简洁narrative。需要引入constraint quality
      作为second axis，使C0 diagnostic framework从"单指标预测"退化为"必要条件判断"。
      对reframed paper仍有价值：强化了"operating regime is narrow"的结论——
      不仅需要diversity，还需要diversity来自有能力产生valid constraints的模型。

  - name: "qwq_32b_operating_regime"
    plan_id: "exp-005"
    description: "QwQ-32B existing data formatted for operating regime analysis"
    expected_results:
      aime_c0: 0.0
      aime_sica_sc_gap: 0.0
      folio_c0: 0.0
      folio_sica_sc_gap: 0.0
      proofwriter_c0: 0.1875
      proofwriter_sica_sc_gap: 0.0
      combined_c0: 0.036
      combined_sica_sc_gap: 0.0
      n_total: 48
      reasoning_model_conclusion: "SICA structurally degenerates to SC"
    result_rationale: >
      QwQ数据已存在且确认worst档预设：reasoning model的chain-of-thought过程
      产生near-deterministic答案（temperature sampling无法穿透reasoning chain的
      self-correction机制）。C0=3.6%意味着在48题中仅1-2题出现过多候选答案，
      且这些多候选情况可能是reasoning chain的中间犹豫而非genuine uncertainty。
      SICA≡SC是数学必然：当只有1个candidate answer时，MaxSAT无论怎么weight都选它。
      这是worst档narrative的strongest evidence——"method correctness is irrelevant 
      when the operating regime doesn't exist"。
    tables:
      - name: "Table 6: Reasoning vs Instruction Model Operating Regime"
        columns: ["Model", "Type", "Domain", "N", "C0", "SICA-SC Gap"]
        rows:
          - ["QwQ-32B", "Reasoning", "AIME", 22, "0%", "0.0pp"]
          - ["QwQ-32B", "Reasoning", "FOLIO", 10, "0%", "0.0pp"]
          - ["QwQ-32B", "Reasoning", "ProofWriter", 16, "18.75%", "0.0pp"]
          - ["Qwen2.5-14B-Instruct", "Instruction", "FOLIO", 30, "40%", "+6.7pp"]
          - ["Qwen2.5-14B-Instruct", "Instruction", "ProofWriter", 30, "63%", "0.0pp"]
          - ["Qwen2.5-14B-Instruct", "Instruction", "Combined", 60, "53%", "+3.3pp"]
    figures_description:
      - "Fig 1 (main): Operating regime diagram — x-axis: C0 (trace diversity), y-axis: SICA-SC gap. Reasoning models clustered at origin, instruction models spread along x-axis but gap only positive for FOLIO subset"
    analysis: >
      QwQ data在worst档下从"negative result配角"升为"主要贡献"。
      Framing：不是"SICA在reasoning model上失败"，而是"我们发现了一个fundamental
      architectural property——reasoning models的internal self-consistency消除了
      external consensus的操作空间"。这个发现对ALL ensemble/consensus methods成立，
      不限于SICA，是architecturally general的insight。
      Paper中应作为Section 4的opening，建立"operating regime"概念后再展示14B数据。

  - name: "c0_diagnostic_validation"
    plan_id: "exp-006"
    description: "Plot C0 vs SICA-SC gap across all models and K values"
    expected_results:
      n_datapoints: 12
      pearson_r_c0_gap: 0.45
      spearman_rho_c0_gap: 0.52
      c0_threshold_for_positive_gap: 0.30
      false_positive_rate: 0.25
      false_negative_rate: 0.10
      auc_c0_as_classifier: 0.72
    result_rationale: >
      在worst档下，C0 vs gap的关系存在但不strong：
      - QwQ数据点（C0≈0, gap=0）锚定了左下角
      - 14B-Instruct K=12 60题（C0=0.53, gap=3.3）是outlier（小样本噪声放大）
      - 14B-Instruct 804题（C0=0.28, gap=0.7）落在中间偏低
      - 7B（C0=0.65, gap=1.7）比14B 804题高但不如14B 60题
      - K ablation各点散布较广
      Pearson r≈0.45说明C0解释了约20%的variance——有信号但不是strong predictor。
      作为binary classifier（C0>0.3 → SICA有价值），AUC=0.72——比random好但远非
      definitive。这将C0从"precise diagnostic"降级为"rough screening heuristic"。
      在worst档narrative中，这恰好支持"characterization贡献"而非"practical tool"。
    tables:
      - name: "Table 7: C0 as Diagnostic — Correlation Analysis"
        columns: ["Condition", "C0", "Gap (pp)", "N"]
        rows:
          - ["QwQ-32B Combined", 0.036, 0.0, 48]
          - ["14B FOLIO-60", 0.40, 6.7, 30]
          - ["14B PW-60", 0.63, 0.0, 30]
          - ["14B Combined-60", 0.53, 3.3, 60]
          - ["14B FOLIO-204", 0.32, 2.0, 204]
          - ["14B PW-600", 0.25, -0.5, 600]
          - ["14B Combined-804", 0.28, 0.7, 804]
          - ["7B Combined-60", 0.65, 1.7, 60]
          - ["14B K=6", 0.40, 1.7, 60]
          - ["14B K=8", 0.45, 0.0, 60]
          - ["14B K=16", 0.55, 1.7, 60]
          - ["14B K=20", 0.58, 0.0, 60]
    figures_description:
      - "Fig 8: Scatter plot C0 vs Gap with regression line — showing positive but weak correlation (r=0.45), with ProofWriter points systematically below regression line"
      - "Fig 9: C0 as binary classifier ROC curve (threshold sweep), AUC=0.72"
    analysis: >
      C0 diagnostic在worst档下的贡献从"practical zero-cost tool"退化为
      "necessary condition identifier"——C0<5%确实predicts gap=0（无false negatives
      in that range），但C0>30%不guarantee positive gap（ProofWriter反例）。
      Paper framing：C0的价值是快速排除不值得尝试的场景（reasoning models），
      而非精确预测gain magnitude。这仍是有价值的practitioner insight，
      但claim需要significantly weaken。

  - name: "sica_72b_awq"
    plan_id: "exp-007"
    description: "Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions, K=12, T=0.7"
    expected_results:
      sc_accuracy: 0.783
      sica_accuracy: 0.783
      sica_sc_gap_pp: 0.0
      c0_multi_candidate_rate: 0.18
      tie_fraction: 0.017
      maxsat_exclusion_rate: 0.015
      constraint_quality_score: 0.82
      wall_time_hours: 3.5
    result_rationale: >
      72B模型在worst档下表现接近reasoning model regime：
      更强的instruction model更self-consistent（虽非reasoning architecture，
      但72B的internal representation足够强大以produce near-deterministic outputs）。
      C0=18%接近worst档定义的lower bound，tie fraction仅1题（1.7%）。
      高constraint quality（0.82）但无用武之地——当多数题12/12一致时，
      即使constraints完美也无法改变outcome。Gap=0pp。
      这对paper的贡献：在7B-14B-72B-QwQ的spectrum上，
      展示了C0与model capability的inverse relationship不限于reasoning vs instruction的
      binary divide，而是continuous spectrum。72B是"instruction model approaching 
      reasoning model regime"的evidence。
    tables:
      - name: "Table 5 (extended): Full Model Scaling"
        columns: ["Model", "Params", "Type", "SC Acc", "C0", "Gap (pp)"]
        rows:
          - ["Qwen2.5-7B-Instruct", "7B", "Instruction", "58.3%", "0.65", "+1.7"]
          - ["Qwen2.5-14B-Instruct", "14B", "Instruction", "70.0%", "0.53", "+3.3"]
          - ["Qwen2.5-72B-Instruct-AWQ", "72B", "Instruction", "78.3%", "0.18", "0.0"]
          - ["QwQ-32B", "32B", "Reasoning", "72.7%", "0.036", "0.0"]
    figures_description:
      - "Fig 10: Model scale vs C0 showing clear negative log-linear trend for instruction models, with reasoning model as extreme endpoint"
    analysis: >
      72B结果在worst档下是devastating for accuracy claim但excellent for characterization：
      它证明SICA的operating regime不仅排除reasoning models，还排除sufficiently capable
      instruction models。实际有效的窗口是"14B-class instruction models on specific 
      diverse-inducing tasks"——一个非常narrow的niche。
      对reframed paper：这是operating regime分析的crown jewel数据点，
      证明了regime narrowness是model capability的函数而非architecture的binary。

  - name: "constraint_quality_case_studies"
    plan_id: "exp-008"
    description: "Qualitative analysis of extracted constraints on 5-10 representative questions"
    expected_results:
      semantically_meaningful_rate: 0.55
      trivially_correct_rate: 0.30
      malformed_or_vacuous_rate: 0.15
      exclusion_justified_rate: 0.70
      case_study_n: 8
      finding: "Constraints are often restatements of the answer rather than independent logical evidence"
    result_rationale: >
      在worst档下，constraint quality analysis揭示了SICA的deeper limitation：
      多数extracted constraints不是独立于answer的logical evidence，而是answer的
      reformulation（"if answer is A then X holds" → tautological when answer IS A）。
      真正的inter-answer constraints（"A and B cannot both be true because..."）占少数。
      MaxSAT exclusion（当它发生时）确实对应reasoning errors（70% justified），
      但exclusion rate太低（2-3%）说明大多数constraints不互相矛盾——
      它们各自支持自己的answer而不cross-reference other candidates。
      这解释了为什么MaxSAT在非tie场景无法翻转majority：constraints是answer-local的，
      不提供cross-answer的discriminative信号。
    tables: []
    figures_description:
      - "Fig 11: Example constraint extraction showing tautological vs genuinely discriminative constraints, with annotation of semantic categories"
    analysis: >
      Case studies在worst档下支持一个deep methodological critique：
      current constraint extraction paradigm produces answer-local evidence而非
      cross-answer comparative evidence。这不是implementation bug而是architectural
      limitation——LLM traces naturally argue FOR their conclusion而非AGAINST alternatives。
      对reframed paper：这是"why symbolic consensus fails"的mechanistic explanation，
      升级为Section 5的核心内容。

  - name: "overhead_analysis"
    plan_id: "exp-009"
    description: "Wall-time breakdown per question: generation, extraction, MaxSAT"
    expected_results:
      avg_total_time_per_question_s: 58.3
      generation_fraction: 0.85
      extraction_fraction: 0.12
      maxsat_fraction: 0.03
      overhead_vs_sc_multiplier: 1.15
      extraction_api_calls_per_question: 12
      maxsat_solve_time_ms: 45
      overall_cost_multiplier_vs_sc: 2.2
    result_rationale: >
      Overhead analysis在worst档下呈现矛盾narrative：
      computational overhead其实不大（MaxSAT本身仅3%的时间），
      主要cost是constraint extraction的额外LLM calls（每题12次extraction call，
      约等于generation cost×1）。总cost是SC的2.2倍。
      在gain=0.7pp且不显著的情况下，任何>1x的overhead都是cost-ineffective的。
      但如果reframe为diagnostic tool，overhead的framing变化：
      "C0 computation需要0 overhead（只看SC投票分布），
      full SICA pipeline的overhead仅在C0>threshold时才值得incur"。
      这支持了two-stage deployment strategy的practical recommendation。
    tables:
      - name: "Table 8: Computational Overhead Breakdown"
        columns: ["Stage", "Avg Time (s)", "Fraction", "Cost vs SC"]
        rows:
          - ["Generation (K=12 traces)", 49.5, "85%", "1.0x (same as SC)"]
          - ["Constraint Extraction", 7.0, "12%", "+1.0x (12 LLM calls)"]
          - ["MaxSAT Solving", 1.8, "3%", "negligible"]
          - ["Total SICA", 58.3, "100%", "2.2x vs SC"]
    figures_description:
      - "Fig 12: Stacked bar chart of per-question time breakdown, showing generation dominates and MaxSAT is negligible"
    analysis: >
      Overhead结果在worst档下的silver lining：MaxSAT本身几乎free（45ms），
      bottleneck完全在constraint extraction的LLM calls。
      这为future work开路：如果extraction可以更高效（batch, smaller model, 
      或integrated into generation prompt），SICA的marginal cost可降至接近零。
      对reframed paper：overhead不是致命弱点（不像some symbolic methods需要
      exponential time），而是engineering problem。主要weakness仍是regime narrowness，
      不是computational cost。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a743d8a2-f619-491e-899f-35d05dc1442a",
  "isSidechain": false,
  "requestId": "req_011Cb5jj5YukuKbHPTcZtpAM",
  "type": "assistant",
  "uuid": "3b383344-c042-49f3-ba19-006202be8cd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "a0daf9ff-2536-4882-956b-5d4805db895f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XQmdWLLTWr7X8EKGwGyY7L",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11193,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8928,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11193,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8928,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11193,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11193
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：扩展实验增益接近零或为负，tiebreak 有效但 tie 极少，accuracy claim 不可持续，需完全 reframe 为分析/诊断贡献 核心假设：['60题的 +3.3pp 是小样本噪声，804 题 gap < 1.5pp', 'K=12 下 even-split tie 极少（< 3%），ti…",
  "leafUuid": "3b383344-c042-49f3-ba19-006202be8cd3",
  "sessionId": "a0daf9ff-2536-4882-956b-5d4805db895f"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing symbolic consensus effectiveness through operating regime analysis",
  "sessionId": "a0daf9ff-2536-4882-956b-5d4805db895f"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：扩展实验增益接近零或为负，tiebreak 有效但 tie 极少，accuracy claim 不可持续，需完全 reframe 为分析/诊断贡献 核心假设：['60题的 +3.3pp 是小样本噪声，804 题 gap < 1.5pp', 'K=12 下 even-split tie 极少（< 3%），ti…",
  "leafUuid": "3b383344-c042-49f3-ba19-006202be8cd3",
  "sessionId": "a0daf9ff-2536-4882-956b-5d4805db895f"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing symbolic consensus effectiveness through operating regime analysis",
  "sessionId": "a0daf9ff-2536-4882-956b-5d4805db895f"
}
```

---
