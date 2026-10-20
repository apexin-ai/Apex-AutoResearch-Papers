# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：核心 null universality 被打破或机制证据链断裂；需根本性 reframe，但数据仍支撑 EMNLP 投稿 核心假设：["exp-01

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/c204f04f-d739-4e8b-8879-071fd2e07316.jsonl`
- **Structured JSON:** [`d8cb6bd2509b6b2b6cc0.json`](../../sessions/d8/d8cb6bd2509b6b2b6cc0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-17T17:00:38.847Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-17T17:00:38.847Z",
  "sessionId": "c204f04f-d739-4e8b-8879-071fd2e07316",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：核心 null universality 被打破或机制证据链断裂；需根本性 reframe，但数据仍支撑 EMNLP 投稿\n核心假设：[\"exp-012 GSM8K 或剩余条件出现 Δ>+4pp 且 p<0.05，打破 'universally empty' 叙事\", '或 F2 per-problem 分析揭示 constraint precision 双峰分布——部分问题 precision>0.7 被 low-precision 问题稀释，capability trap 非 uniform', '或 exp-013 ablation 在某子集上 MaxSAT > count-only（SAT solver 非完全 vacuous）', 'exp-011 FOLIO +10pp 信号在 domain-specific 分析中非纯噪声，LLaMA-8B×FOLIO 可能是 positive operating point', 'reviewer 认为 oracle 仅 FOLIO + powered test 仅 Qwen-14B，evidence 不足支撑 general claim']\n关键指标范围：{'remaining_max_abs_delta_pp': [4.0, 8.0], 'constraint_precision_mean': [0.52, 0.62], 'constraint_precision_vs_c0_r': [0.2, 0.45], 'gsm8k_c0_pct': [25, 50], 'gsm8k_delta_pp': [3.0, 8.0], 'combined_N_all_conditions': [1300, 1600], 'meta_analytic_delta_pp': [1.0, 3.0], 'oracle_gap_pp': [8.0, 9.5], 'f2_non_discriminative_fraction': [0.5, 0.7]}\n叙事方向：Capability trap 不再是 universal characterization，reframe 为 condition-dependent phenomenon。Title 改：'When Do Self-Extracted Constraints Improve LLM Reasoning? Characterizing the Capability Trap'。从 pure negative 转 boundary-condition analysis。三条 claims 重构为：(a) positive boundary — 识别 capability trap 发生的 sufficient conditions (model capacity × domain formalizability × precision threshold)，(b) mechanism — oracle 仍证明 aggregation 有效性 + capability trap 解释多数失败条件，(c) diagnostic — C0 + constraint precision 联合 deployment framework（非单独 C0）。Story 更复杂但 reviewer 可能认为更 nuanced。风险：不够 clean，可能被判 incremental。对策：强调 oracle causal separation 是不变的 contribution，boundary analysis 是 bonus。仍冲 EMNLP main，不降级。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: symb_invariant_consensus\nfocus: Oracle experiment (exp-021) is the key new result: gold FOL + MAX-SAT = +8.82pp over SC (p<0.001), while self-extracted SICA = SC. This causally separates extraction failure from aggregation failure. Title/claims now scoped to self-extracted constraints (not symbolic consensus broadly). Temperature ablation shows C0 varies 30-43% but gap stays 0. Paper now has constructive direction (better extraction unlocks +8.82pp potential).\n\n## paper_framing.md\n\n# Paper Framing — symb_invariant_consensus\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25)\n- Deadline: May 25, 2026 (ARR submission)\n\n## Core Claims (3 条) — D025 Capability Trap Analysis Paper (FINAL)\n\n1. **The Capability Trap**: LLM self-extracted FOL constraint aggregation faces a fundamental tension: it requires output diversity (C0>20%) to differ from voting, but self-extracted constraints lack discriminative power even when diversity is high. High C0 produces abundant constraints, but these constraints fail to distinguish correct from incorrect answers, reducing MAX-SAT to counting. Validated across 3 reasoning domains × 4 instruction-scale model families + 1 full reasoning model (QwQ-32B). [Scope: this finding characterizes same-model self-extraction pipelines; methods using external verifiers or trained extractors may not share this limitation.]\n2. **Operating Regime is Empirically Empty**: Five model families confirm SICA provides no accuracy gain over majority voting: (a) Qwen-14B n=804 Δ=+0.25pp n.s., (b) Mistral-7B n=60 Δ=0.0pp exact, (c) LLaMA-8B StrategyQA n=200 Δ=+2.0pp p=0.424, (d) LLaMA-8B FOLIO n=204 Δ=-2.4pp, (e) DeepSeek-R1-Distill-7B n=60 Δ=-3.3pp. Full reasoning model QwQ-32B shows near-zero diversity (C0<5%), making SICA degenerate to SC. Instruction-scale models (including distilled reasoning models) show high diversity (C0=38-62%) but constraints lack discriminative power. No tested condition achieves both requirements simultaneously.\n3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 is a zero-cost early stopping criterion for practitioners considering symbolic aggregation methods.\n\n## Core Insight\nLLM self-extracted FOL constraints don't improve majority voting because of a **capability trap**: the method needs output diversity (disagreement to resolve) AND discriminative constraints (to resolve it correctly). While instruction-scale models produce abundant diversity (C0=38-62%) and constraints, these self-extracted constraints lack the discriminative power to distinguish correct from incorrect answers (precision ~0.50, no better than chance). MAX-SAT optimization over such non-discriminative constraints degenerates to counting, performing no better than simple majority voting.\n\n**Critical oracle result (exp-021)**: When gold FOL annotations replace self-extracted constraints, Oracle-SICA achieves +8.82pp over SC (p<0.001, n=204). This proves the MAX-SAT aggregation mechanism IS effective given discriminative constraints — the bottleneck is exclusively in LLM self-extraction quality, not in the aggregation paradigm itself.\n\nWe provide the first systematic empirical study (a) precisely localizing the failure mode to extraction quality via oracle control, (b) quantifying constraint non-discrimination at per-problem granularity (n=307), and (c) proving MAX-SAT adds nothing beyond counting when constraints lack discriminative power. [Positioning: Logic-LM and LINC documented that LLM-to-FOL translation is error-prone; our contribution is the oracle-controlled causal separation of extraction vs aggregation failure, plus systematic quantification and C0 as deployment diagnostic.]\n\n## Story Spine\n- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?\n- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.\n- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 4 instruction-scale model families + 1 full reasoning model. We find SICA ≈ SC everywhere, and identify a structural reason: the **capability trap**.\n- **Headline result**: \"Across 3 reasoning domains and 5 models spanning instruction, distilled-reasoning, and full-reasoning architectures, SICA provides no significant accuracy gain over SC. Five models (combined N>1,300) show Δ ranging from -3.3pp to +2.0pp, none significant. The constraint ablation reveals MAX-SAT ≈ count-only ≈ random-weight. We identify the structural cause: a capability trap where extracted constraints lack discriminative power regardless of output diversity level.\"\n\n## Anticipated Reviewer Concerns & Defensive Experiments\n1. **\"Gains not statistically significant\"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.\n2. **\"Only a better tiebreaker, not worth the overhead\"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis\n3. **\"Only Qwen models\"** → 4 instruction-scale families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B\n4. **\"Only one reasoning model\"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)\n5. **\"Only logic domain\"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.\n6. **\"MAX-SAT is over-engineering\"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.\n7. **\"Random tiebreak baseline\"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.\n8. **\"Why not just use a reasoning model?\"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.\n9. **\"How does this compare to Logic-LM / LINC?\"** → exp-015: Logic-LM × K baseline (CPU-only)\n10. **\"Weighted SC is simpler\"** → exp-016: Weighted SC baseline (CPU-only)\n11. **\"C0 is trivially derived\"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.\n12. **\"Within-family scaling?\"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.\n13. **\"Self-extraction confound — same model generates and extracts\"** → exp-021 Oracle FOLIO: **RESOLVED.** Gold FOL + Z3 + MAX-SAT = 88.24% vs SC = 79.41% (+8.82pp, p=6.15e-05). Aggregation mechanism IS effective with discriminative constraints. Bottleneck conclusively localized to LLM self-extraction quality. This is now a core contribution, not just a defensive experiment.\n14. **\"Published methods achieve gains on same benchmarks (DyLoS, Aristotle, FoVer)\"** → Acknowledge in Related Work and Discussion. Key distinction: those methods use trained/external verifiers, multi-paradigm solver selection, or logic-complete decomposition — all fundamentally different from same-model self-extraction. Our finding characterizes the specific failure mode of self-extraction pipelines, not symbolic reasoning broadly.\n15. **\"MAX-SAT formulation is just weighted voting\"** → Paper must explicitly describe cross-answer evaluation: constraints from trace t_i ARE/ARE NOT evaluated against other candidates. If structurally a weighted vote, acknowledge and frame contribution as \"even the most charitable interpretation (weighted vote with constraint-based weights) provides no gain.\"\n\n## Working Title\n**\"The Capability Trap: Why Self-Extracted Constraints Cannot Improve LLM Majority Voting\"**\n(Alternatives: \n- \"Diversity Without Discrimination: A Systematic Study of LLM-Extracted Constraint Aggregation\"\n- \"When Does Symbolic Aggregation Help? Characterizing the Failure Mode of Self-Extracted FOL Constraints\")\n\nNOTE (Dream D037): Title MUST be scoped to \"self-extracted constraints\" / \"SICA\" — NOT \"symbolic consensus\" broadly. Published methods (DyLoS, Aristotle, FoVer, LogicAgent) achieve gains on same benchmarks using different symbolic approaches. Our evidence covers one pipeline (same-model FOL extraction + MAX-SAT), not the entire paradigm.\n\n## Paper Structure (EMNLP 8pp + appendix)\n- Main Tables: T1 (Main Results: models × domains, SICA vs SC), T2 (Oracle Control: Gold-FOL+MAX-SAT vs SC vs SICA-self, the key causal separation), T3 (Constraint Ablation: MaxSAT vs count-only vs random), T4 (Temperature Ablation: C0 varies 30-43% but Δ=0 throughout)\n- Main Figures: F1 (Method Pipeline), F2 (Per-problem scatter: vote entropy vs constraint exclusion rate, colored by flip type, n=307 multi-candidate problems from exp-001 — hero figure showing constraints fail to discriminate), F3 (Operating Regime Heatmap: all cells ≈ 0), F4 (C0 vs Gap: experiment-level conditions, marker size ∝ sqrt(n), showing no correlation between diversity and SICA effectiveness)\n- Appendix: K ablation (exp-002), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data\n\n## Claim Risk Notes (Updated D035 + exp-014)\n- **Claim 1 mechanism refinement**: \"Inverse correlation between diversity and quality\" framing NOT supported by data (experiment-level r=0.15, p=0.74). Correct framing: \"constraints lack discriminative power regardless of diversity level.\" Evidence: MaxSAT≈count-only (exp-013), high C0 + negative delta (exp-014 C0=58% Δ=-3.3pp, exp-020 C0=62% Δ=-2.4pp). OPEN — need per-problem F2 data from exp-001 to strengthen.\n- **Claim 2 expanded**: Five models now (added DeepSeek-R1-Distill-7B Δ=-3.3pp). DeepSeek reclassified as instruction-scale (C0=58%, not <5% as predicted). Only QwQ-32B is full reasoning model. RESOLVED.\n- **Claim 3 gradient → independence framing**: Temperature ablation confirms C0 varies (30%→38%→43%) but gap stays flat at 0.00pp (zero discordant across all temperatures). Data supports \"diversity is necessary but insufficient\" NOT \"gradient diagnostic.\" Claim 3 should be: \"C0 predicts when SICA cannot help (C0<5% → degenerate), but increasing diversity beyond the threshold provides no benefit — constraint quality remains the binding bottleneck regardless of diversity level.\" RESOLVED (temperature data in hand).\n- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite exp-011 as evidence of any positive signal.\n- **F2 hero figure data gap**: Experiment-level correlations (n=7) too weak. Must use per-problem granularity from exp-001 (n≈300+ multi-candidate problems). Agent tasked with this analysis. OPEN.\n\n## Required Citations (Dream D037 — minimum 30 references)\n\nPaper Agent MUST include these categories (non-exhaustive list of must-cite works):\n- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 ACL Findings (confidence-weighted SC), DiVeRSe (Li et al. 2023)\n- **Neuro-symbolic reasoning (positive results on same benchmarks)**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)\n- **Test-time compute scaling**: Snell et al. 2025 (ICLR Oral), DeepSeek-R1 technical report (Nature 2025), Diversity-Aware Training for TTS (2025)\n- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd (Wang et al. 2024)\n- **Constraint satisfaction in NLP**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)\n- **Negative results in NLP**: appropriate precedents for analysis/negative-result papers\n- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023\n- **Reasoning model paradigm**: QwQ technical blog, o1 (OpenAI 2024)\n\n## Claim Scoping Rules (Dream D037)\n\n- n=60 conditions: present as \"suggestive/consistent with\" NOT \"confirming.\" Only n≥200 conditions can \"confirm\" null.\n- Combined N>1,300: acceptable if clearly stated that 804/1300 come from powered Qwen-14B condition.\n- Domain coverage: acknowledge that SICA operates meaningfully (C0>20%) primarily on formal logic; other domains are degenerate (C0<10%) due to model capability.\n- \"Capability trap\" framing: position as systematic quantification of a known challenge (not discovery). Our specific contributions: (a) per-problem precision analysis at n=307 granularity, (b) constraint ablation proving MAX-SAT ≈ counting, (c) C0 as deployment diagnostic.\n\n## Venue Fit Risks\n- EMNLP: Negative-results/analysis paper. Must answer \"so what should practitioners do?\" → C0 as deployment diagnostic + overhead analysis.\n- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.\n- Statistical power: Now strong (N>1,200 combined across powered tests).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: sica_expanded_14b\n  claim:\n  - 1\n  - 2\n  description: 'Full-scale evaluation: PW D5 600 + FOLIO 204 = 804 questions, K=12,\n    T=0.7. Maximizes statistical power for C3 significance.'\n  priority: P0\n  gpu_budget_hours: 14\n  deps: []\n  registry_id: sica_expanded_14b\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- id: exp-002\n  name: sica_k_ablation_14b\n  claim:\n  - 1\n  description: 'K sensitivity (K=6,8,11,12,16,20) on D012''s 60 questions. Includes\n    odd K=11 to test if SICA value persists without exact ties. Key questions: does\n    SICA benefit depend on tiebreaks? What happens at odd K? How does tiebreak frequency\n    change with K?'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n  note: D024 增加 K=11（odd-K test, Dream 三档一致要求）。如 K=11 gap=0 → 确认 tie-only mechanism；如\n    gap>0 → SICA has value beyond tiebreaking。\n- id: exp-003\n  name: tiebreak_baseline_analysis\n  claim:\n  - 1\n  description: Compare SICA vs SC-random-tiebreak vs SC-deterministic on all available\n    data. CPU-only reanalysis. Quantify how much of SICA's gain survives against fair\n    baselines.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - sica_d012_14b\n  status: planned\n  note: 'Completed as CPU analysis, no registry entry. Results: SICA tiebreak 80%\n    (4/5) vs random 50% vs alphabetical 60% vs first-seen 40%. Artifact: art_20260516_47de9d'\n- id: exp-004\n  name: sica_7b_scaling\n  claim:\n  - 2\n  - 3\n  description: 'Run SICA with Qwen2.5-7B-Instruct on same 60 questions. Test: does\n    weaker model → higher C0 → larger SICA gain? Validates C0-as-predictor claim.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-005\n  name: qwq_32b_operating_regime\n  claim:\n  - 2\n  description: QwQ-32B negative results formatted for paper's Operating Regime Analysis\n    section. Data exists from MVP phase (AIME, MATH, ProofWriter, FOLIO). No new GPU\n    needed.\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  note: 'Data from QwQ-32B MVP experiments: sica_aime30_v3 (AIME 22题, 0% multi-candidate),\n    sica_proofwriter30_v2 (PW 16题, 18.75% multi-candidate), sica_folio30 (FOLIO 10题,\n    0% multi-candidate). Combined C0=3.6%, SICA≡SC across all domains.'\n- id: exp-006\n  name: c0_diagnostic_validation\n  claim:\n  - 3\n  description: Plot C0 vs SICA-SC gap across all models and K values. Validate C0\n    as predictor. CPU-only analysis over exp-001/002/004/005 results.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-002\n  - exp-004\n  status: planned\n- id: exp-007\n  name: sica_72b_awq\n  claim:\n  - 2\n  description: 'Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions. Scaling analysis:\n    high-baseline non-reasoning model. Within-Qwen scaling dimension.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n  note: D019 升级 P2→P1. 72B-AWQ 4-bit ~36GB weights + KV cache ≈ 50-60GB, 98GB RTX\n    PRO 6000 单卡可放。\n- id: exp-008\n  name: constraint_quality_case_studies\n  claim:\n  - 1\n  description: Qualitative analysis of extracted constraints on 5-10 representative\n    questions. Are constraints semantically meaningful? Do excluded constraints correspond\n    to reasoning errors?\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  name: overhead_analysis\n  claim:\n  - 1\n  description: 'Wall-time breakdown per question: generation, constraint extraction,\n    MaxSAT solving. Address ''is the overhead worth it'' concern.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: D021 升级 P2→P1. Reviewer 指出 EMNLP 审稿人对 practical impact 极敏感。\n- id: exp-010\n  name: sica_mistral_7b\n  claim:\n  - 2\n  - 3\n  description: 'Mistral-7B-Instruct-v0.3 on D012 60 questions (PW+FOLIO). Cross-family\n    validation: does C0 pattern hold outside Qwen? Eliminates ''Qwen-specific artifact''\n    attack.'\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: DONE\n  note: 'D021 新增. 必做——消除 Claim 2 致命弱点。Escalation: 若 C0>30% 且 gap>0 但 p>0.2，扩展到 200+\n    题（~3h GPU，margin 允许）。'\n  registry_id: exp-010-mistral-v3\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- id: exp-011\n  name: sica_llama_8b\n  claim:\n  - 2\n  - 3\n  description: LLaMA-3.1-8B-Instruct on D012 60 questions. Second non-Qwen family.\n    Combined with exp-010 gives 3-family coverage (Qwen/Mistral/LLaMA).\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D021 新增. 必做——3 家族是 EMNLP 最低门槛。需 HF_TOKEN（Meta license）或 ModelScope 镜像。Escalation\n    同 exp-010。\n- id: exp-012\n  name: gsm8k_pilot_14b\n  claim:\n  - 2\n  - 3\n  description: 'Qwen2.5-14B on GSM8K 30-question pilot (K=12). Cross-domain test:\n    is C0 high only in restricted-answer-space domains (NLI 3-class) or also in open-answer\n    math? If C0 low → C0=uncertainty signal (strengthens Claim 3). If C0 high → cross-domain\n    win.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 预测 C0<20% (14B too strong on GSM8K). Any result is publishable\n    insight.\n- id: exp-013\n  name: constraint_ablation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only ablation: SICA-MaxSAT vs SICA-count-only (constraint count\n    per answer, no satisfiability) vs SICA-random-weight. Critical for D025 pivot:\n    if MaxSAT ≈ count-only → aggregation mechanism is vacuous, confirming capability\n    trap.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D025 升级 P1→P0. 现在是 make-or-break: 如果 MaxSAT = count-only → 证明 SAT 解算无贡献（capability\n    trap 的 mechanism evidence）。必须用 exp-002 的 raw_constraints 数据。'\n- id: exp-014\n  name: sica_deepseek_r1_llama_8b\n  claim:\n  - 2\n  description: 'DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions. Second reasoning\n    model data point with LLaMA base architecture: validates C0<5% generalizes beyond\n    QwQ-32B AND eliminates ''still Qwen family'' attack.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps: []\n  status: planned\n  note: D021 新增. Reviewer 建议用 LLaMA 底座版本避免 Qwen 架构归属争议。\n- id: exp-015\n  name: logic_lm_baseline\n  claim:\n  - 1\n  description: Logic-LM × K + majority vote baseline on FOLIO. Run Logic-LM style\n    single-trace FOL verification K times, then majority vote. Isolates whether MAX-SAT\n    multi-trace aggregation adds value beyond FOL extraction itself.\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 三档一致要求 Logic-LM/LINC 比较。CPU-only: 用 exp-001 已有 traces + FOL\n    constraints 做单 trace verification then vote。'\n- id: exp-016\n  name: weighted_sc_baseline\n  claim:\n  - 1\n  - 3\n  description: 'Weighted SC baseline (Taubenfeld et al. 2024 style): weight votes\n    by trace confidence/length/perplexity. CPU-only reanalysis of exp-001/002 data.\n    Tests if simple weighting achieves same tiebreak quality without MAX-SAT.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n  note: 'D024 新增. Dream 提出 weighted SC 是最直接竞争 baseline。实现方式: (1) uniform weight (=SC),\n    (2) length-weighted, (3) log-prob weighted (如 traces 有 logprobs), (4) constraint-count\n    weighted (no SAT)。'\n- id: exp-017\n  name: sica_strategyqa_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on StrategyQA 60 questions (K=12). Commonsense reasoning\n    domain — high predicted C0 (35-50%) but implicit reasoning chains → low expected\n    constraint quality. Tests capability trap in best-case-diversity scenario.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. Reviewer 推荐 ROI 最高 benchmark。如 C0>30% 且 SICA≈SC → 直接证明 capability\n    trap（diversity high but quality low → no gain）。\n- id: exp-018\n  name: sica_arc_challenge_14b\n  claim:\n  - 1\n  - 2\n  description: Qwen2.5-14B on ARC-Challenge 60 questions (K=12). Science reasoning,\n    4-choice format. Tests constraint mechanism in multi-choice scenario + different\n    domain.\n  priority: P0\n  gpu_budget_hours: 1.5\n  deps: []\n  status: planned\n  note: D025 新增. 4选1格式测试 constraint mechanism 泛化能力。与 FOLIO (3-class) + GSM8K (open)\n    + StrategyQA (binary) 形成答案格式多样性。\n- id: exp-019\n  name: constraint_quality_correlation\n  claim:\n  - 1\n  - 2\n  description: 'CPU-only analysis: compute constraint precision per domain × model,\n    correlate with C0 and SICA-SC gap. Formalizes the capability trap as inverse C0-quality\n    correlation. Uses data from exp-001/010/011/017/018.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-017\n  - exp-018\n  status: planned\n  note: 'D025 新增. Hero figure (F2) 的数据来源。Constraint quality = (constraints consistent\n    with ground truth) / (total constraints). 预期: high C0 domains (StrategyQA) have\n    low quality, low C0 domains (math) have high quality but SICA=SC anyway.'\n\n\n## registry (completed experiments)\n\n- exp_id: crd_folio_main\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    divergence_rate: 0.422\n    diagnosis_rate: 0.872\n    error_types: 4\n    directed_advantage_pp: 4.7\n    directed_p_value: 0.63\n    localization_accuracy: 0.946\n    fol_accuracy: 0.789\n    code_accuracy: 0.598\n    oracle_accuracy: 0.878\n    pipeline_accuracy: 0.814\n    baseline_accuracy: 0.74\n    cost_multiplier: 5.76\n    dataset: FOLIO\n    n: 204\n- exp_id: smoke-test-5q\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: sica_smoke_5q\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.8\n    sc_accuracy: 0.8\n    extraction_rate: 1\n    problems_with_contradictions: 1\n    total_problems: 5\n    total_time_s: 3505\n    avg_time_per_problem_s: 701\n    per_problem:\n    - id: algebra/2470\n      level: 1\n      sica_correct: true\n      sc_correct: true\n      constraints: 27\n      unique: 9\n      excluded: 0\n    - id: prealgebra/65\n      level: 2\n      sica_correct: true\n      sc_correct: true\n      constraints: 26\n      unique: 2\n      excluded: 0\n    - id: number_theory/847\n      level: 3\n      sica_correct: true\n      sc_correct: true\n      constraints: 21\n      unique: 11\n      excluded: 0\n      note: 14 JSON parse failures, 1693s\n    - id: precalculus/1199\n      level: 4\n      sica_correct: false\n      sc_correct: false\n      constraints: 35\n      unique: 6\n      excluded: 0\n      note: graph-reading problem, model cannot see image\n    - id: algebra/2277\n      level: 5\n      sica_correct: true\n      sc_correct: true\n      constraints: 60\n      unique: 6\n      satisfied: 3\n      excluded: 3\n- exp_id: sica_temp_diversity\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temperatures_tested:\n    - 0.7\n    - 0.9\n    - 1\n    problems_tested: 3\n    problems_with_divergence: 0\n    finding: QwQ-32B produces zero answer divergence at all temperatures on MATH L4-5.\n      Reasoning model's deterministic chain dominates sampling randomness.\n    max_tokens_issue: 4096 tokens insufficient for some L5 problems (truncation)\n    recommendation: Use AIME 2024 (harder, ~79.5% acc) or non-reasoning model for\n      trace diversity\n- exp_id: mvp_math50_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_t07\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_aime30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 4/30\n    sica_accuracy_interim: 3/4 (75%)\n    sc_accuracy_interim: 3/4 (75%)\n    avg_time_per_problem_s: 557\n    p2_z3_error: Z3Exception on z3_maxsat.py:163, 0 constraints extracted\n    p5_vllm_stuck: vLLM timeout since ~22:11, retried multiple rounds\n    issue: vLLM service likely crashed or OOM at Problem 5\n    analysis_contradiction_rate_aime: 50% (2/4)\n    analysis_contradiction_rate_math: 20% (1/5)\n    analysis_unique_constraints_per_problem_aime: 18.7\n    analysis_exclusion_rate: 10.7%\n    analysis_sica_sc_agreement: 9/9 (100%)\n    analysis_signal: weak positive - mechanism works but SC too unanimous to flip\n    analysis_p2_failure: 0 constraints, 0 votes - answer extraction failure\n- exp_id: sica_aime30_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 22/30\n    sica_accuracy_interim: 16/22 (72.7%)\n    sc_accuracy_interim: 16/22 (72.7%)\n    sica_sc_gap_pp: 0\n    avg_time_per_problem_s: 645.9\n    runtime_h: 5.9\n    remaining_problems: 8\n    vote_diversity_analysis:\n      valid_problems: 16\n      total_problems: 22\n      multi_candidate_rate: 0\n      zero_vote_problems: 6\n      zero_vote_indices:\n      - 1\n      - 7\n      - 8\n      - 10\n      - 13\n      - 14\n      constraints_extracted: 19/22\n      exclusion_rate: 0.387\n      conclusion: All 16 valid problems have exactly 1 candidate answer. SICA≡SC structurally.\n        MaxSAT exclusion operates but cannot change final selection with only 1 candidate.\n    process_status: gone (cron miss 1/5)\n- exp_id: sica_proofwriter30\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    sica_accuracy: 0/30 (0.0%)\n    sc_accuracy: 0/30 (0.0%)\n    sica_sc_gap_pp: 0\n    total_wall_time_s: 238.9\n    total_wall_time_min: 4\n    avg_time_per_problem_s: 8\n    traces_generated: 0\n    constraints_extracted: 0\n    traces_with_constraints: 0\n    unique_constraints: 0\n    maxsat_satisfied: 0\n    maxsat_excluded: 0\n    multi_candidate_rate: N/A (no traces generated)\n    vote_diversity: N/A\n    z3_errors: 0\n    z3_timeouts: 0\n    problems_with_contradiction: 0\n    problems_with_votes: 0\n    failure_mode: ALL_400_BAD_REQUEST\n    failure_count: 30/30\n    root_cause: max_tokens=16384 equals max_model_len=16384, leaving 0 tokens for\n      prompt input. Every API call returns 400.\n- exp_id: sica_folio30\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_proofwriter30_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: sica_d016_c0_precheck\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    multi_candidate_rate_combined: 0.46\n    multi_candidate_rate_folio: 0.4\n    multi_candidate_rate_proofwriter: 0.5\n    sc_accuracy_combined: 0.73\n    sc_accuracy_folio: 0.8\n    sc_accuracy_proofwriter: 0.69\n    n_problems: 26\n    n_folio: 10\n    n_proofwriter: 16\n    K: 6\n    T: 0.7\n    total_time_s: 280\n    c0_gate: PASS (46% >= 20%)\n    model: Qwen2.5-14B-Instruct\n    vllm_gpu_mem_gib: 27.6\n    smoke_test: 2 problems end-to-end OK, constraints 21-26 per problem\n- exp_id: sica_d012_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7\n    sica_sc_gap_pp: 3.3\n    c0_multi_candidate_rate: 0.5333\n    c1_extraction_rate: 1\n    c2_contradiction_problems: 34\n    c3_gap_pp: 3.3\n    bootstrap_p: 0.2261\n    proofwriter_sica: 0.6667\n    proofwriter_sc: 0.6667\n    folio_sica: 0.8\n    folio_sc: 0.7333\n    total_constraints_raw: 5849\n    total_constraints_unique: 1735\n    maxsat_exclusion_rate: 0.0259\n    wall_time_min: 58.3\n    d012_verdict: ALL_PASS\n- exp_id: sica_expanded_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.765\n    sc_accuracy: 0.762\n    sica_sc_gap_pp: 0.3\n    n_problems: 804\n    multi_candidate_rate: 0.3818\n    folio_sica: 0.794\n    folio_sc: 0.794\n    folio_gap_pp: 0\n    folio_n: 204\n    proofwriter_sica: 0.755\n    proofwriter_sc: 0.752\n    proofwriter_gap_pp: 0.3\n    proofwriter_n: 600\n    extraction_rate: 0.89\n    answer_extraction_rate: 1\n    contradiction_rate: 0.022\n    problems_with_contradictions: 331\n    truncated_traces: 0\n    wall_time_min: 826\n- exp_id: sica_k_sensitivity_14b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K6_sica: 0.733\n    K6_sc: 0.733\n    K6_gap_pp: 0\n    K8_sica: 0.733\n    K8_sc: 0.75\n    K8_gap_pp: -1.7\n    K11_sica: 0.733\n    K11_sc: 0.733\n    K11_gap_pp: 0\n    K12_sica: 0.7\n    K12_sc: 0.75\n    K12_gap_pp: -5\n    K16_sica: 0.717\n    K16_sc: 0.75\n    K16_gap_pp: -3.3\n    K20_sica: 0.7\n    K20_sc: 0.733\n    K20_gap_pp: -3.3\n    all_K_sica_leq_sc: true\n    larger_K_degrades_sica: true\n- exp_id: sica_constraint_ablation_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    maxsat_accuracy: 0.7649\n    count_only_accuracy: 0.7662\n    random_weight_accuracy: 0.7637\n    sc_baseline_accuracy: 0.7624\n    n_problems: 804\n    agreement_802_of_804: true\n    mcnemar_p_all_gt_0.7: true\n    note: approximate (raw z3 formulas unavailable, count-only/random-weight use proxy)\n- exp_id: exp-005\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    qwq_aggregate_c0_nominal_pct: 10.3\n    qwq_aggregate_c0_effective_pct: 2.6\n    qwen14b_c0_pct: 46\n    diversity_ratio_effective: 17.7\n    aime_delta_pp: 0\n    proofwriter_delta_pp: -5.9\n    aime_n: 22\n    proofwriter_n: 17\n    temp_diversity_n: 5\n    folio_n: 2\n    total_problems: 46\n    c0_threshold: 20\n    qwq_below_threshold: true\n- exp_id: exp-011-llama8b\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-016-weighted-sc\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    sica_accuracy: 0.7649\n    sc_uniform_accuracy: 0.7624\n    inv_length_accuracy: 0.7674\n    length_weighted_accuracy: 0.7525\n    constraint_count_accuracy: 0.7525\n    inv_length_vs_sc_p: 0.453\n    length_vs_sc_p: 0.153\n    inv_length_vs_sica_p: 0.864\n    length_vs_sica_p: 0.066\n    n_problems: 804\n    all_nonsignificant: true\n- exp_id: exp-010-mistral\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-011-llama8b-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-018-arc\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-017-strategyqa-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.5667\n    sc_accuracy: 0.5333\n    delta_pp: 3.33\n    mcnemar_chi2: 0.5\n    mcnemar_p: n.s.\n    bootstrap_ci_95:\n    - 0\n    - 8.33\n    bootstrap_p_delta_le_0: 0.1346\n    multi_candidate_rate: 0.1\n    contradiction_detected: 5\n    extraction_rate_problem: 1\n    extraction_rate_trace: 0.704\n    discordant_sica_wins: 2\n    discordant_sc_wins: 0\n- exp_id: pilot-constraint-filtering\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 43\n    thresholds_tested:\n    - 1\n    - 2\n    - 3\n    - 5\n    - 7\n    best_gap_pp: 2.33\n    best_T: 1\n    sica_T1: 0.7674\n    sc: 0.7442\n    T5_gap: 0\n    T7_gap: 0\n    discriminative_ratio_count: 0.115\n    discriminative_ratio_weight: 0.372\n    effective_flip_rate: 0.174\n    multi_answer_problems: 23\n    unanimous_problems: 20\n    problems_disc_favors_different: 4\n- exp_id: exp-018-arc-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.95\n    sc_accuracy: 0.9667\n    delta_pp: -1.67\n    multi_candidate_rate: 0.05\n    extraction_rate: 1\n    contradiction_detected: 3\n    discordant_sica_wins: 0\n    discordant_sc_wins: 1\n    dataset: ARC-Challenge\n    model: Qwen2.5-14B-Instruct\n- exp_id: exp-011-llama8b-v3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6667\n    sc_accuracy: 0.6\n    delta_pp: 6.67\n    multi_candidate_rate: 0.6167\n    extraction_rate: 0.8556\n    answer_extraction_rate: 0.8958\n    contradiction_rate: 0.0527\n    problems_with_contradictions: 43\n    truncated_traces: 44\n    discordant_sica_wins: 5\n    discordant_sc_wins: 1\n    mcnemar_p: 0.2188\n    proofwriter_sica: 0.6333\n    proofwriter_sc: 0.6\n    proofwriter_delta_pp: 3.33\n    folio_sica: 0.7\n    folio_sc: 0.6\n    folio_delta_pp: 10\n    model: LLaMA-3.1-8B-Instruct\n    dataset: D012\n    wall_time_min: 66.4\n- exp_id: pilot-contrastive-prompt\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp-010-mistral-v3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.4833\n    sc_accuracy: 0.4833\n    delta_pp: 0\n    multi_candidate_rate: 0.5\n    extraction_rate: 0.8819\n    answer_extraction_rate: 1\n    contradiction_rate: 0.0562\n    discordant_sica_wins: 2\n    discordant_sc_wins: 2\n    mcnemar_p: 1\n    proofwriter_sica: 0.4\n    proofwriter_sc: 0.4\n    proofwriter_delta_pp: 0\n    folio_sica: 0.5667\n    folio_sc: 0.5667\n    folio_delta_pp: 0\n    truncated_traces: 0\n    model: Mistral-7B-Instruct-v0.3\n    dataset: D012\n- exp_id: exp-019-llama8b-strategyqa-200\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 200\n    k: 12\n    sica_accuracy: 0.74\n    sc_accuracy: 0.72\n    delta_pp: 2\n    multi_candidate_rate: 0.41\n    mcnemar_p: 0.424\n    bootstrap_ci_95:\n    - -1.5\n    - 5.5\n    bootstrap_p_delta_le_0: 0.12\n    discordant_sica_wins: 9\n    discordant_sc_wins: 5\n    discordant_total: 14\n    discordant_rate: 0.07\n    sc_unanimous_rate: 0.545\n    model: LLaMA-3.1-8B-Instruct\n    dataset: StrategyQA\n    wall_time_min: 52\n- exp_id: exp-020-llama8b-folio-204\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 204\n    k: 12\n    sica_accuracy: 0.608\n    sc_accuracy: 0.632\n    delta_pp: -2.45\n    mcnemar_p: 0.2668\n    bootstrap_ci_95:\n    - -5.88\n    - 0.98\n    bootstrap_p_sica_ge_sc: 0.1\n    discordant_sica_wins: 4\n    discordant_sc_wins: 9\n    discordant_total: 13\n    discordant_rate: 0.064\n    multi_candidate_rate: 0.618\n    extraction_rate: 0.942\n    answer_extraction_rate: 0.951\n    contradiction_rate: 0.062\n    both_wrong: 71\n    model: LLaMA-3.1-8B-Instruct\n    dataset: FOLIO-204\n    wall_time_min: 131.7\n- exp_id: exp-009-overhead-analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 804\n    mean_total_wall_s: 61.6\n    mean_trace_gen_s: 31.6\n    trace_gen_pct: 51.3\n    mean_extract_s: 29\n    extract_pct: 47\n    mean_dedup_s: 1\n    dedup_pct: 1.6\n    mean_maxsat_s: 0.003\n    maxsat_pct: 0.005\n    sica_overhead_s: 30\n    sica_overhead_pct: 48.7\n    pw_overhead_pct: 51.3\n    folio_overhead_pct: 38.6\n    p50_overhead_pct: 48.9\n    p90_overhead_pct: 57.6\n- exp_id: exp-014-deepseek-r1-7b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.6833\n    sc_accuracy: 0.7167\n    delta_pp: -3.33\n    multi_candidate_rate: 0.583\n    extraction_rate: 0.839\n    answer_extraction_rate: 0.939\n    truncated_traces: 72\n    contradiction_rate: 0.037\n    wall_time_min: 100.3\n    mcnemar_p: 0.4795\n    discordant_sica_wins: 0\n    discordant_sc_wins: 2\n    model: DeepSeek-R1-Distill-Qwen-7B\n    dataset: D012\n- exp_id: temperature-ablation-t03\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.7333\n    sc_accuracy: 0.7333\n    delta_pp: 0\n    multi_candidate_rate: 0.3\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 0.3\n- exp_id: temperature-ablation-t05\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.7667\n    sc_accuracy: 0.7667\n    delta_pp: 0\n    multi_candidate_rate: 0.383\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 0.5\n- exp_id: temperature-ablation-t10\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n: 60\n    k: 12\n    sica_accuracy: 0.75\n    sc_accuracy: 0.75\n    delta_pp: 0\n    multi_candidate_rate: 0.433\n    discordant_total: 0\n    model: Qwen2.5-14B-Instruct\n    dataset: D012\n    temperature: 1\n- exp_id: exp-021-oracle-folio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n: 204\n    k: 12\n    oracle_sica_accuracy: 0.8824\n    sc_accuracy: 0.7941\n    sica_self_accuracy: 0.7941\n    oracle_vs_sc_delta_pp: 8.82\n    oracle_vs_sica_delta_pp: 8.82\n    mcnemar_p_oracle_vs_sc: 6.15e-05\n    z3_gold_agreement: 0.946\n    fol_parse_success: 1\n    model: Qwen2.5-14B-Instruct\n    dataset: FOLIO-204\n    constraint_source: gold FOL annotations\n- exp_id: exp-012-gsm8k-pilot\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-17T17:00:38.851Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-17T17:00:38.851Z",
  "sessionId": "c204f04f-d739-4e8b-8879-071fd2e07316"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-17T17:00:38.876Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：核心 null universality 被打破或机制证据链断裂；需根本性 reframe，但数据仍支撑 EMNLP 投稿
核心假设：["exp-012 GSM8K 或剩余条件出现 Δ>+4pp 且 p<0.05，打破 'universally empty' 叙事", '或 F2 per-problem 分析揭示 constraint precision 双峰分布——部分问题 precision>0.7 被 low-precision 问题稀释，capability trap 非 uniform', '或 exp-013 ablation 在某子集上 MaxSAT > count-only（SAT solver 非完全 vacuous）', 'exp-011 FOLIO +10pp 信号在 domain-specific 分析中非纯噪声，LLaMA-8B×FOLIO 可能是 positive operating point', 'reviewer 认为 oracle 仅 FOLIO + powered test 仅 Qwen-14B，evidence 不足支撑 general claim']
关键指标范围：{'remaining_max_abs_delta_pp': [4.0, 8.0], 'constraint_precision_mean': [0.52, 0.62], 'constraint_precision_vs_c0_r': [0.2, 0.45], 'gsm8k_c0_pct': [25, 50], 'gsm8k_delta_pp': [3.0, 8.0], 'combined_N_all_conditions': [1300, 1600], 'meta_analytic_delta_pp': [1.0, 3.0], 'oracle_gap_pp': [8.0, 9.5], 'f2_non_discriminative_fraction': [0.5, 0.7]}
叙事方向：Capability trap 不再是 universal characterization，reframe 为 condition-dependent phenomenon。Title 改：'When Do Self-Extracted Constraints Improve LLM Reasoning? Characterizing the Capability Trap'。从 pure negative 转 boundary-condition analysis。三条 claims 重构为：(a) positive boundary — 识别 capability trap 发生的 sufficient conditions (model capacity × domain formalizability × precision threshold)，(b) mechanism — oracle 仍证明 aggregation 有效性 + capability trap 解释多数失败条件，(c) diagnostic — C0 + constraint precision 联合 deployment framework（非单独 C0）。Story 更复杂但 reviewer 可能认为更 nuanced。风险：不够 clean，可能被判 incremental。对策：强调 oracle causal separation 是不变的 contribution，boundary analysis 是 bonus。仍冲 EMNLP main，不降级。

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
  "promptId": "3ce786dc-5f99-4e68-a87a-76b2cbcab2f0",
  "type": "user",
  "uuid": "45651d9b-c44f-447b-a574-a1560fac6f86",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "c204f04f-d739-4e8b-8879-071fd2e07316",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-17T17:00:38.874Z_

```json
{
  "parentUuid": "45651d9b-c44f-447b-a574-a1560fac6f86",
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
  "uuid": "223b576c-0595-4732-81e3-dcfd6570b754",
  "timestamp": "2026-05-17T17:00:38.874Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "c204f04f-d739-4e8b-8879-071fd2e07316",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-17T17:00:38.874Z_

```json
{
  "parentUuid": "223b576c-0595-4732-81e3-dcfd6570b754",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3c1736f1-bac2-412b-85d3-d51f2c74aa33",
  "timestamp": "2026-05-17T17:00:38.874Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "c204f04f-d739-4e8b-8879-071fd2e07316",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：核心 null universality 被打破或机制证据链断裂；需根本性 reframe，但数据仍支撑 EMNLP 投稿 核心假设：[\"exp-012 GSM8K 或剩余条件出现 Δ>+4pp 且 p<0.05，打破 'universally empty' 叙事\", '或 F2 per-problem 分…",
  "leafUuid": "3c1736f1-bac2-412b-85d3-d51f2c74aa33",
  "sessionId": "c204f04f-d739-4e8b-8879-071fd2e07316"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "When do self-extracted constraints improve LLM reasoning",
  "sessionId": "c204f04f-d739-4e8b-8879-071fd2e07316"
}
```

---

### Assistant

_source line 8 · 2026-05-17T17:01:36.167Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment_plan, under the "worst" tier scenario. Let me carefully go through the worst tier definition and each planned experiment to produce realistic predictions.

The worst tier means:
- Core null universality is broken or mechanism evidence chain breaks
- Need fundamental reframe, but data still supports EMNLP submission
- Key assumptions that could trigger worst:
  1. exp-012 GSM8K or remaining conditions show Δ>+4pp with p<0.05, breaking "universally empty" narrative
  2. F2 per-problem analysis reveals constraint precision bimodal distribution — some problems precision>0.7 diluted by low-precision problems, capability trap is non-uniform
  3. exp-013 ablation shows MaxSAT > count-only on some subset (SAT solver not completely vacuous)
  4. exp-011 FOLIO +10pp signal is non-noise in domain-specific analysis, LLaMA-8B×FOLIO is a positive operating point
  5. Reviewer thinks oracle only on FOLIO + powered test only on Qwen-14B, evidence insufficient for general claim

Now I'm looking at the metric ranges that would characterize this worst-case scenario, with remaining absolute deltas between 4-8 percentage points and constraint precision averaging around 0.52-0.62.

The broader picture shows GSM8K performance drops in the 25-50% range with deltas of 3-8pp, oracle gaps around 8-9.5pp, and a substantial fraction of non-discriminative cases. The key insight is that the capability trap isn't a universal phenomenon anymore—it's really dependent on specific conditions. With that reframing in place, I need to work through the remaining planned experiments, particularly the sica_k_ablation_14b test, and see how the results would play out under these metric constraints.

Looking at the experiment status, most are still in the planning phase, though a few have completed runs in the registry despite being marked as planned. The gsm8k_pilot_14b is currently running, and I should account for how these various ablations and baseline analyses will fit into the overall narrative once they're executed. I'm seeing a pattern here—many experiments marked as "planned" in the experiment_plan actually have corresponding completed or in-progress entries in the registry. I need to reconcile these discrepancies and determine which ones to include in my predictions. Since the user asked for predictions on each planned experiment, I should account for all of them, noting which have already been executed or are currently running. I see there's a mismatch between the planned status and what's actually completed in the registry. Let me go through the planned experiments systematically—there are quite a few, from the ablation studies and baseline analyses to the scaling experiments across different model sizes and datasets. I'll need to generate worst-tier predictions for each of these, keeping in mind that some already have actual results recorded but the user wants the hypothetical worst-case scenario instead.

Starting with the ablation and baseline work: for the K ablation experiment, I'm imagining a scenario where certain K values barely show SICA outperforming SC, maybe with marginal gains on specific subsets that don't generalize well.

For the tiebreak baseline, the worst case would be that SICA's tiebreak advantage is clear but the effect size is larger than anticipated on particular subsets. The 7B scaling experiment might show Qwen-7B with a higher C0 and a suggestive positive gap around 4-5 percentage points, though it wouldn't reach statistical significance with the sample size. QwQ-32B would maintain the low C0 pattern consistent with the main findings, but possibly with anomalous behavior on one domain. Finally, the C0 diagnostic work could reveal a moderate positive correlation between C0 and the gap, which would actually undermine the claim that C0 is necessary but insufficient.

Looking at the larger models and additional datasets, the 72B-AWQ experiment shows lower C0 as expected, but in the few cases where results diverge, SICA wins consistently, suggesting that high-capacity models under constraints might be a viable approach. The case studies reveal a bimodal distribution where some problems have highly discriminative constraints while others are essentially noise. The overhead measurement doesn't shift under worst-case assumptions since it's just a factual measurement. LLaMA-8B on FOLIO shows a +10 percentage point signal that either replicates or partially replicates at larger sample sizes, indicating this is a genuine positive operating point. GSM8K shows moderate C0 around 25 percent.

Moving into the constraint and baseline comparisons, MaxSAT performs roughly equivalent to count-only overall, but on high-precision constraint problems it significantly outperforms. DeepSeek-R1 exhibits high C0 around 40-58 percent with a slight negative or null result that isn't as cleanly null as I'd want. Logic-LM with the K approach matches or slightly exceeds SICA's performance, which challenges whether SICA's mechanism is truly distinctive. Weighted inverse-length sampling for self-consistency also matches or beats SICA, pointing toward simpler alternatives being sufficient.

Looking at domain-specific results, StrategyQA shows high C0 in the 35-50 percent range with a modest positive gap, suggesting commonsense reasoning with high diversity can actually benefit from the approach. ARC-Challenge's 4-choice format presents some interesting performance dynamics. The constraint quality correlation analysis reveals a bimodal distribution in precision across problems and domains—some show high precision while others don't, indicating this is a condition-dependent phenomenon rather than universal. Now I'm organizing these findings into a structured YAML format with detailed rationales.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c1736f1-bac2-412b-85d3-d51f2c74aa33",
  "isSidechain": false,
  "requestId": "req_011Cb8VtsPqAgjt7KmboqFju",
  "type": "assistant",
  "uuid": "c8472d9b-cc24-446e-9ab8-a5d3b1dd7670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "c204f04f-d739-4e8b-8879-071fd2e07316",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAr85chwg84u2iZ6Qs7fdZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20448,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14944,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20448,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14944,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20448
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

_source line 9 · 2026-05-17T17:05:45.443Z_

```yaml
tier: worst
narrative_guidance: "Capability trap 不再是 universal characterization，reframe 为 condition-dependent phenomenon。Title 改：'When Do Self-Extracted Constraints Improve LLM Reasoning? Characterizing the Capability Trap'。从 pure negative 转 boundary-condition analysis。三条 claims 重构为：(a) positive boundary — 识别 capability trap 发生的 sufficient conditions (model capacity × domain formalizability × precision threshold)，(b) mechanism — oracle 仍证明 aggregation 有效性 + capability trap 解释多数失败条件，(c) diagnostic — C0 + constraint precision 联合 deployment framework（非单独 C0）。"

imagined_experiments:
  - name: "sica_k_ablation_14b"
    plan_id: "exp-002"
    description: "K sensitivity (K=6,8,11,12,16,20) on D012 60 questions"
    expected_results:
      K6_sica: 0.750
      K6_sc: 0.733
      K6_gap_pp: 1.7
      K8_sica: 0.767
      K8_sc: 0.750
      K8_gap_pp: 1.7
      K11_sica: 0.767
      K11_sc: 0.733
      K11_gap_pp: 3.3
      K12_sica: 0.733
      K12_sc: 0.700
      K12_gap_pp: 3.3
      K16_sica: 0.750
      K16_sc: 0.733
      K16_gap_pp: 1.7
      K20_sica: 0.733
      K20_sc: 0.717
      K20_gap_pp: 1.7
      K11_mcnemar_p: 0.157
      best_K_gap_pp: 3.3
      odd_K_gap_gt_0: true
    result_rationale: "Worst 档要求 universality 被打破。K=11（odd-K）仍出现 +3.3pp，证明 SICA 的增益不仅来自 tiebreak——odd-K 无精确平局，但 SICA 仍能通过 constraint exclusion 翻转少数问题。这打破了 'SICA value is purely tiebreak-driven' 叙事。虽然 p>0.1 因 n=60 power 不足，但方向一致且 K=11/K=12 两个 K 值重复 +3.3pp。需在论文中 reframe 为 'condition-dependent benefit at certain K ranges' 而非 'universally zero'。"
    tables:
      - "T_appendix_K_ablation: K × SICA/SC accuracy matrix"
    figures_description:
      - "K vs gap line plot showing non-monotonic but consistently positive gap across K values, challenging universal null"
    analysis: "K=11 odd-K positive gap 是 worst 档核心证据之一。如果 gap 仅存在于 even-K（tiebreak），可以 dismiss；但 odd-K +3.3pp 意味着 constraint exclusion 有 genuine discriminative value on this 60-question subset。Reframe: SICA has weak positive signal on D012-subset (Qwen-14B × formal logic × n=60) that doesn't survive power scaling (exp-001 n=804 shows +0.3pp)，但 heterogeneity 暗示 condition-dependence。"

  - name: "tiebreak_baseline_analysis"
    plan_id: "exp-003"
    description: "SICA vs SC-random-tiebreak vs SC-deterministic comparison"
    expected_results:
      sica_tiebreak_win_rate: 0.80
      random_tiebreak_win_rate: 0.50
      alphabetical_tiebreak_win_rate: 0.60
      first_seen_tiebreak_win_rate: 0.40
      n_tied_questions: 5
      tied_fraction: 0.083
      sica_net_gain_from_tiebreak_pp: 2.5
      sica_gain_beyond_tiebreak_pp: 1.0
    result_rationale: "Worst 档下，tiebreak 分析揭示 SICA 的 tiebreak 优势（80% win rate on ties）AND 有少量 non-tie flips。5/60 个问题有 exact tie，SICA 在其中 4/5 选对；另外还有 1 个非平局问题被 constraint exclusion 翻转。这意味着 SICA mechanism 不完全 reducible to tiebreak——有微弱但存在的 exclusion 效应。在 n=60 subset 上 beyond-tiebreak gain ≈ 1pp 不显著，但 existence 本身打破 'purely tiebreak' framing。"
    tables:
      - "T_tiebreak: Tiebreak method × win rate on tied questions"
    figures_description:
      - "Bar chart: tiebreak win rates across methods, SICA clearly highest"
    analysis: "Tiebreak 分析在 worst 档下支持 'SICA has genuine constraint signal on subset' 叙事。但 effect size 太小 to be practically meaningful（5 个 tie 中多赢 1-2 个 = 1-3pp on full set）。Paper 需 acknowledge SICA has weak positive signal in favorable conditions 而非 zero。"

  - name: "sica_7b_scaling"
    plan_id: "exp-004"
    description: "Qwen2.5-7B-Instruct on 60 questions, testing weaker model → higher C0 → larger gap"
    expected_results:
      sica_accuracy: 0.617
      sc_accuracy: 0.567
      delta_pp: 5.0
      mcnemar_p: 0.083
      multi_candidate_rate: 0.717
      c0_pct: 71.7
      extraction_rate: 0.82
      answer_extraction_rate: 0.91
      constraint_precision_mean: 0.54
      discordant_sica_wins: 4
      discordant_sc_wins: 1
      wall_time_min: 45
    result_rationale: "Worst 档的核心打破机制之一：weaker model (7B) 产生更高 C0 (71.7%) 且 delta=+5.0pp（p=0.083，接近 significance）。这暗示 capability trap 是 capacity-dependent 而非 universal。7B 模型 extraction quality 低（precision~0.54），但因为 baseline accuracy 也低（56.7%），constraints 的微弱 discriminative signal 足以翻转几个问题。C0-gap 正相关在 experiment-level 出现（7B: C0=72%, Δ=+5; 14B: C0=38%, Δ=+0.3; 72B: C0~15%, Δ≈0），产生 r=0.3-0.4 的 condition-level correlation。这打破了 'no correlation between diversity and benefit' 叙事。"
    tables:
      - "T1_main: add Qwen-7B row"
    figures_description:
      - "F4 C0 vs gap scatter: 7B point in upper-right quadrant, breaking flat-line narrative"
    analysis: "7B 的 +5pp 是 worst 档的 smoking gun。虽然 n=60 power 不足以达到 p<0.05，但方向与 LLaMA-8B exp-011 FOLIO +10pp 一致。Pattern emerges: weaker models on formal logic domains show positive gaps。需 reframe capability trap 为 'high-capacity models extract non-discriminative constraints; low-capacity models paradoxically benefit because their higher error rate creates more room for constraint-based correction'。"

  - name: "qwq_32b_operating_regime"
    plan_id: "exp-005"
    description: "QwQ-32B negative results formatted for paper"
    expected_results:
      qwq_aggregate_c0_effective_pct: 3.6
      qwq_aime_delta_pp: 0
      qwq_proofwriter_delta_pp: 0
      qwq_folio_delta_pp: 0
      total_problems: 46
      sica_degenerate_to_sc: true
      reasoning_model_c0_threshold_confirmed: true
    result_rationale: "QwQ-32B 在 worst 档下不变：C0<5%，SICA≡SC。Full reasoning model 的 deterministic chain 消除 diversity，SICA 结构性退化。这在 worst 档仍成立因为 worst 档打破的是 instruction-scale 模型的 universality，不是 reasoning model 的 behavior。QwQ 数据仍支持 Claim 3 (C0&lt;threshold → degenerate)。问题是 n=46 across heterogeneous tasks，reviewer 可能要求更多 reasoning model data points。"
    tables:
      - "T1_main: QwQ-32B row (C0<5%, SICA≡SC)"
    figures_description:
      - "F3 operating regime heatmap: QwQ row all gray (degenerate)"
    analysis: "QwQ 数据在 worst 档是 safe asset——不会产生 surprise。但 reviewer concern #4 ('only one reasoning model') 在 worst 档更尖锐：如果 instruction-scale 条件显示 condition-dependent gains，reviewer 会问 'what about reasoning models on tasks where they have moderate C0?' 可能需要 QwQ on easier tasks where it's not 100% accurate。"

  - name: "c0_diagnostic_validation"
    plan_id: "exp-006"
    description: "Plot C0 vs SICA-SC gap across all conditions"
    expected_results:
      n_conditions: 12
      pearson_r_c0_gap: 0.38
      pearson_p: 0.08
      spearman_rho: 0.42
      spearman_p: 0.06
      c0_below_5_all_zero_gap: true
      c0_above_30_gap_range_pp: [-3.3, 6.7]
      c0_above_30_mean_gap_pp: 1.8
      linear_model_r2: 0.14
      c0_threshold_5_specificity: 1.0
      c0_threshold_5_sensitivity: 0.0
    result_rationale: "Worst 档下，C0 与 gap 的 experiment-level correlation 是 moderate positive (r=0.38, p=0.08)，接近 significance。这与 best/mid 档 (r≈0.15, p=0.74) 截然不同。原因：7B 和 LLaMA-8B 条件的 high C0 + positive gap 拉高了 correlation。但 R²=0.14 说明 C0 只解释 14% variance——仍是 'necessary but insufficient' 但带有 weak positive predictive direction。Claim 3 需 reframe：C0 不仅是 binary gate (C0<5% → degenerate) 而是有 weak gradient effect（higher C0 correlates with slightly higher expected gap），但 variance 太大 for deployment use。"
    tables:
      - "T_c0_diagnostic: condition × C0 × gap × n"
    figures_description:
      - "F4 scatter with weak positive trend line, wide CI band, some negative outliers even at high C0"
    analysis: "Moderate correlation (r=0.38) 是 worst 档的 nuisance finding。不足以 claim C0 is predictive (p=0.08, R²=0.14)，但足以让 reviewer 质疑 'C0 is uninformative beyond threshold'。Paper 需 reframe Claim 3 为 joint diagnostic (C0 + constraint precision) 而非 C0 alone。"

  - name: "sica_72b_awq"
    plan_id: "exp-007"
    description: "Qwen2.5-72B-Instruct AWQ 4-bit on 60 questions"
    expected_results:
      sica_accuracy: 0.817
      sc_accuracy: 0.833
      delta_pp: -1.7
      multi_candidate_rate: 0.15
      c0_pct: 15.0
      extraction_rate: 0.93
      answer_extraction_rate: 1.0
      constraint_precision_mean: 0.61
      discordant_sica_wins: 0
      discordant_sc_wins: 1
      mcnemar_p: 1.0
      wall_time_min: 180
    result_rationale: "72B 高 baseline (83.3%) 导致 C0 低 (15%)——模型太 confident，answer space 近 unanimous。SICA 轻微 negative (-1.7pp) 因仅 9 个 multi-candidate 问题，constraint exclusion 在 1 个问题上错误翻转。Interesting finding for worst 档：constraint precision 在 72B 较高 (0.61 vs 14B 的 0.52)——bigger model extracts better constraints，但 C0 太低 to matter。这支持 reframed story：capability trap 有两个 regime：(1) weak model = high C0 + low precision = marginal benefit，(2) strong model = low C0 + high precision = degenerate。Sweet spot 可能存在于 intermediate capacity × formal domain。"
    tables:
      - "T1_main: Qwen-72B row"
      - "T_precision: model size vs constraint precision"
    figures_description:
      - "F4: 72B point in lower-left (low C0, zero gap) but with annotation showing higher precision"
    analysis: "72B 结果支持 within-family scaling narrative：model capacity ↑ → C0 ↓ + precision ↑，两者抵消使 gap≈0。但 combined with 7B (C0=72%, precision=0.54, gap=+5pp)，creates a capacity-dependent boundary story。Worst 档的 paper structure 需 show this scaling dimension explicitly。"

  - name: "constraint_quality_case_studies"
    plan_id: "exp-008"
    description: "Qualitative analysis of extracted constraints on 5-10 representative questions"
    expected_results:
      n_analyzed: 10
      high_precision_cases: 3
      low_precision_cases: 5
      mixed_precision_cases: 2
      high_precision_constraint_example: "ForAll(x, Human(x) -> Mortal(x)) correctly excludes wrong answer"
      low_precision_example: "Exists(x, Answer(x, 'True')) - tautologically matches any answer"
      bimodal_finding: true
      precision_gt_0p7_fraction: 0.3
      precision_lt_0p4_fraction: 0.5
    result_rationale: "Worst 档下 case study 揭示 bimodal pattern：30% 的问题有 precision>0.7 的 genuinely discriminative constraints（特别是 FOLIO 中有明确 logical structure 的问题），50% 的问题 constraints 基本 random (precision<0.4)。这支持 'capability trap 非 uniform' 假设——部分问题 constraints 有效但被 low-precision 多数稀释。Qualitative evidence 展示 failure mode diversity：(a) 语义空约束 (∀x, True)，(b) 约束复述答案 (circular)，(c) 约束正确但对所有答案等效 (non-discriminative despite being valid FOL)。"
    tables: []
    figures_description:
      - "Case study figure: 2 high-precision examples vs 2 low-precision examples, showing constraint-answer evaluation"
    analysis: "Case studies 在 worst 档是 double-edged：证明 mechanism CAN work (high-precision cases exist) 同时解释 WHY aggregate 结果 null (diluted by majority low-precision)。Paper 需 position as 'the capability trap is not a fundamental impossibility but a current extraction quality gap with identifiable conditions for success'。"

  - name: "sica_llama_8b"
    plan_id: "exp-011"
    description: "LLaMA-3.1-8B-Instruct on D012 60 questions"
    expected_results:
      sica_accuracy: 0.683
      sc_accuracy: 0.617
      delta_pp: 6.7
      mcnemar_p: 0.109
      multi_candidate_rate: 0.617
      c0_pct: 61.7
      extraction_rate: 0.856
      answer_extraction_rate: 0.896
      contradiction_rate: 0.053
      discordant_sica_wins: 5
      discordant_sc_wins: 1
      folio_sica: 0.700
      folio_sc: 0.600
      folio_delta_pp: 10.0
      proofwriter_sica: 0.633
      proofwriter_sc: 0.600
      proofwriter_delta_pp: 3.3
      wall_time_min: 66
    result_rationale: "Worst 档的关键 universality-breaker：LLaMA-8B on D012 显示 +6.7pp overall，FOLIO 子集 +10pp。虽然 mcnemar_p=0.109（n=60 power 不足），但 5:1 discordant ratio 方向强。FOLIO +10pp 特别有问题——与 exp-020 (n=204, LLaMA-8B×FOLIO, Δ=-2.4pp) 直接矛盾（D012 的 30 题 vs full FOLIO 204 题）。Worst 档假设这 60 题 subsample 碰巧包含了 LLaMA-8B constraints 高 precision 的问题（selection bias or genuine subpopulation）。如果 per-problem precision 分析（exp-019）确认 30% 问题 precision>0.7，则 +10pp 在 high-precision 子集是 real signal 被 low-precision 多数稀释。"
    tables:
      - "T1_main: LLaMA-8B row with per-domain breakdown"
    figures_description:
      - "Attention flag: LLaMA-8B×FOLIO-30 = +10pp vs LLaMA-8B×FOLIO-204 = -2.4pp discrepancy"
    analysis: "LLaMA-8B FOLIO +10pp 是 worst 档最棘手的数据点。两种解释：(1) n=30 抽样 variance (SE≈9pp，+10pp 在 1σ 内)，(2) D012 的 30 题偏向 high-formalizability 子集。Worst 档假设 (2) 部分成立——exp-019 per-problem analysis 将揭示 constraint precision 双峰分布，其中 FOLIO 高 precision 子集确实 SICA>SC。Paper 需 acknowledge positive operating point 而非 dismiss as noise。"

  - name: "gsm8k_pilot_14b"
    plan_id: "exp-012"
    description: "Qwen2.5-14B on GSM8K 30 questions (K=12)"
    expected_results:
      sica_accuracy: 0.867
      sc_accuracy: 0.800
      delta_pp: 6.7
      n: 30
      k: 12
      multi_candidate_rate: 0.367
      c0_pct: 36.7
      extraction_rate: 0.875
      answer_extraction_rate: 0.97
      constraint_precision_mean: 0.58
      discordant_sica_wins: 3
      discordant_sc_wins: 1
      mcnemar_p: 0.317
      bootstrap_p: 0.06
      wall_time_min: 25
    result_rationale: "Worst 档核心假设 #1：GSM8K 出现 Δ>+4pp。14B on GSM8K baseline ~80% (不像 reviewer 预测的 95%+)，因为 pilot 选取了 medium-hard 问题。C0=36.7% 在 worst 档范围内 [25,50]。+6.7pp 虽然 p=0.317 (n=30 underpowered)，但 bootstrap p=0.06 接近 significance。机制：数学问题的 FOL constraints 更 well-formed（numerical equalities like 'x + y = 15'），比 NLI 的 modal logic 更容易 correctly extract。Constraint precision 0.58 高于 FOLIO/PW 的 ~0.50，因为 math constraints 有 concrete numerical ground truth。这直接打破 'universally empty operating regime'——新 domain + moderate C0 + real constraint quality = genuine gain。"
    tables:
      - "T1_main: add GSM8K row (flagged as pilot, n=30)"
    figures_description:
      - "F4: GSM8K point in positive quadrant (C0=37%, gap=+6.7pp) breaking the flat line"
    analysis: "GSM8K +6.7pp 是 worst 档最具 reframe 压力的结果。即使 n=30 不 significant，combined with 7B (+5pp) 和 LLaMA-8B FOLIO (+10pp on subset)，形成 'there exist positive operating points' 的 consistent pattern。Paper 必须从 'capability trap is universal' → 'capability trap characterizes the majority of conditions but positive boundaries exist'。需额外 200+ 题 powered replication（exp-012 扩展）才能 confirm，但 pilot 数据足以 force reframe。"

  - name: "constraint_ablation"
    plan_id: "exp-013"
    description: "SICA-MaxSAT vs SICA-count-only vs SICA-random-weight"
    expected_results:
      maxsat_accuracy: 0.7649
      count_only_accuracy: 0.7587
      random_weight_accuracy: 0.7550
      sc_baseline_accuracy: 0.7624
      maxsat_vs_count_mcnemar_p: 0.317
      maxsat_vs_random_mcnemar_p: 0.157
      n_problems: 804
      agreement_maxsat_count: 798
      disagreement_maxsat_wins: 4
      disagreement_count_wins: 2
      high_precision_subset_n: 95
      high_precision_maxsat_acc: 0.821
      high_precision_count_acc: 0.789
      high_precision_gap_pp: 3.2
      high_precision_mcnemar_p: 0.083
    result_rationale: "Worst 档假设 #3：exp-013 ablation 在子集上 MaxSAT > count-only。Overall MaxSAT ≈ count-only（798/804 agree），但在 constraint precision>0.6 的 95 个问题子集上，MaxSAT 比 count-only 高 3.2pp (p=0.083)。这意味着 SAT solver 非完全 vacuous——当 constraints 有 genuine discriminative content 时，satisfiability structure 比 simple counting 更好。全局 null 是因为 709/804 个问题 constraints non-discriminative，MaxSAT 退化为 counting。On the subset where constraints matter, MaxSAT mechanism IS adding value。这打破 'aggregation mechanism is completely vacuous' 叙事。"
    tables:
      - "T3: Ablation results overall + high-precision subset breakdown"
    figures_description:
      - "Stratified ablation: overall MaxSAT≈count vs subset MaxSAT>count bar chart"
    analysis: "Subset MaxSAT>count-only (p=0.083) 是 worst 档 mechanism evidence 的关键 crack。Paper 需 acknowledge: 'When constraints are discriminative, the satisfiability structure of MAX-SAT provides additional signal beyond counting. The aggregation mechanism is not vacuous — it is starved of quality input.' 这实际上 STRENGTHENS oracle story (exp-021) 但 weakens 'mechanism is vacuous' claim。Reframe: mechanism is effective but latent, activated only by discriminative constraints。"

  - name: "sica_deepseek_r1_llama_8b"
    plan_id: "exp-014"
    description: "DeepSeek-R1-Distill-LLaMA-8B on D012 60 questions"
    expected_results:
      sica_accuracy: 0.700
      sc_accuracy: 0.717
      delta_pp: -1.7
      multi_candidate_rate: 0.55
      c0_pct: 55.0
      extraction_rate: 0.85
      answer_extraction_rate: 0.94
      truncated_traces: 65
      contradiction_rate: 0.04
      mcnemar_p: 1.0
      discordant_sica_wins: 1
      discordant_sc_wins: 2
      wall_time_min: 95
      model: "DeepSeek-R1-Distill-LLaMA-8B"
    result_rationale: "DeepSeek-R1-Distill-LLaMA-8B 在 worst 档 behaves like instruction model (C0=55%, high diversity) 但 SICA slightly negative (-1.7pp)。与 Qwen-based distill (exp-014 registry: C0=58.3%, Δ=-3.3pp) 一致。Distilled reasoning models 有 instruction-like diversity 但 constraint quality 比 pure instruction models 更差（truncated thinking traces → incomplete constraint extraction）。Worst 档下这个结果不打破 universality——它 confirms distilled models fall in same trap。但 LLaMA-base vs Qwen-base 的 subtle difference (LLaMA -1.7pp vs Qwen -3.3pp) 暗示 base architecture matters slightly。"
    tables:
      - "T1_main: DeepSeek-R1-Distill row (instruction-scale classification)"
    figures_description: []
    analysis: "DeepSeek-R1-Distill on LLaMA base 在 worst 档是 neutral data point——confirms capability trap on distilled models。不打破 nor 强化 universality。Reclassification 为 instruction-scale (C0>50%) 在 worst 档与其他档一致。"

  - name: "logic_lm_baseline"
    plan_id: "exp-015"
    description: "Logic-LM × K + majority vote baseline on FOLIO"
    expected_results:
      logic_lm_k12_accuracy: 0.779
      logic_lm_sc_accuracy: 0.794
      sica_accuracy: 0.794
      sc_accuracy: 0.794
      logic_lm_vs_sc_delta_pp: -1.5
      logic_lm_vs_sica_delta_pp: -1.5
      logic_lm_single_trace_accuracy: 0.755
      logic_lm_extraction_success_rate: 0.72
      n: 204
    result_rationale: "Worst 档下 Logic-LM×K baseline 略低于 SC (-1.5pp)，因为 Logic-LM 的 single-trace verification 方式在 K 次独立抽取中累积 extraction error。Logic-LM 单 trace accuracy (75.5%) 低于 SC (79.4%) 因为 FOL 翻译错误导致 false negative verifications。但关键 finding：Logic-LM×K accuracy (77.9%) 与 SICA (79.4%) 差距仅 1.5pp，且 Logic-LM 不需要 cross-trace MAX-SAT——simple per-trace FOL check + vote 已经 competitive。Reviewer 可能 argue 'multi-trace aggregation (SICA) provides minimal value over single-trace verification (Logic-LM style)' even when both fail to beat SC。"
    tables:
      - "T_baselines: Logic-LM × K vs SICA vs SC"
    figures_description:
      - "Baseline comparison bar chart: SC ≈ SICA > Logic-LM×K > Logic-LM-single"
    analysis: "Logic-LM 结果在 worst 档不直接打破 universality 但 complicates the story：如果 single-trace verification × vote ≈ multi-trace MAX-SAT aggregation，则 SICA 的 additional complexity (cross-answer constraint evaluation) provides no marginal benefit over simpler approach。Paper 需 address：'Even the richer MAX-SAT aggregation structure provides no benefit over simpler per-trace evaluation when extraction quality is the binding constraint.'"

  - name: "weighted_sc_baseline"
    plan_id: "exp-016"
    description: "Weighted SC baselines (length/confidence/constraint-count) on exp-001 data"
    expected_results:
      sica_accuracy: 0.7649
      sc_uniform_accuracy: 0.7624
      inv_length_accuracy: 0.7699
      length_weighted_accuracy: 0.7538
      constraint_count_accuracy: 0.7587
      inv_length_vs_sc_delta_pp: 0.75
      inv_length_vs_sc_p: 0.317
      inv_length_vs_sica_delta_pp: 0.50
      inv_length_vs_sica_p: 0.564
      n_problems: 804
      best_method: "inv_length"
      all_nonsignificant: true
    result_rationale: "Worst 档下 inverse-length weighted SC (76.99%) 略高于 SICA (76.49%) 和 SC (76.24%)，虽然不显著 (p=0.317)。这暗示 shorter traces（更 confident/decisive reasoning）作为 quality signal 比 FOL constraint satisfiability 更有效。Weighted SC 不需要 constraint extraction overhead（节省 48.7% time），performance comparable or slightly better。在 worst 档 'condition-dependent reframe' 中，这变成：simpler weighting heuristics capture similar or more signal than MAX-SAT on the majority of conditions；MAX-SAT only adds value on the high-precision subset (connecting to exp-013)。"
    tables:
      - "T_baselines: Weighted SC variants vs SICA vs SC"
    figures_description:
      - "Bar chart: all methods within 2pp of each other, error bars overlapping"
    analysis: "Inv-length slightly above SICA 在 worst 档是 uncomfortable：reviewer 可能 ask 'why use MAX-SAT if trace-length heuristic does equally well?'。Defense: (1) on high-precision subset MAX-SAT > all (exp-013 subset finding), (2) inv-length has no theoretical justification while MAX-SAT has principled mechanism that activates with quality constraints (oracle proof), (3) difference is n.s.。"

  - name: "sica_strategyqa_14b"
    plan_id: "exp-017"
    description: "Qwen2.5-14B on StrategyQA 60 questions"
    expected_results:
      sica_accuracy: 0.600
      sc_accuracy: 0.550
      delta_pp: 5.0
      mcnemar_p: 0.157
      multi_candidate_rate: 0.383
      c0_pct: 38.3
      extraction_rate: 0.72
      answer_extraction_rate: 0.95
      constraint_precision_mean: 0.55
      discordant_sica_wins: 4
      discordant_sc_wins: 1
      bootstrap_ci_95: [-1.67, 10.0]
      bootstrap_p: 0.07
      wall_time_min: 40
    result_rationale: "Worst 档假设 StrategyQA 出现 +5pp (p=0.157, n=60)。Commonsense 领域 C0=38.3%——模型在 yes/no binary questions 上有 moderate disagreement。Constraint quality (precision=0.55) 略高于 chance，足以在 4/5 discordant 问题上正确翻转。这是 worst 档 'condition-dependent' 证据之一：binary answer space + moderate diversity + commonsense domain = weak positive signal。机制：binary yes/no 使 constraint exclusion 更 powerful（排除一个 constraint 直接 flip answer），不像 NLI 3-class 或 math open-ended 需要更精确的 discrimination。"
    tables:
      - "T1_main: StrategyQA row"
    figures_description:
      - "Domain comparison: StrategyQA shows positive trend unlike FOLIO/PW which are null"
    analysis: "StrategyQA +5pp combined with GSM8K +6.7pp 形成 'new domains show positive signals' pattern。这不是单点 noise——两个不同 domain 独立产生 +5-7pp。Worst 档的 reframe 变为：capability trap 主要 afflicts formal logic domain with NLI-style 3-class answer space (FOLIO/PW)；binary or numerical domains with concrete constraints benefit more。"

  - name: "sica_arc_challenge_14b"
    plan_id: "exp-018"
    description: "Qwen2.5-14B on ARC-Challenge 60 questions (K=12)"
    expected_results:
      sica_accuracy: 0.917
      sc_accuracy: 0.933
      delta_pp: -1.7
      multi_candidate_rate: 0.067
      c0_pct: 6.7
      extraction_rate: 0.95
      answer_extraction_rate: 1.0
      discordant_sica_wins: 0
      discordant_sc_wins: 1
      mcnemar_p: 1.0
      wall_time_min: 30
    result_rationale: "ARC-Challenge 在 worst 档下 C0 极低 (6.7%)——14B 在 science questions 上太 confident (93.3% SC accuracy)，answer space 近 unanimous。仅 4 个 multi-candidate 问题，SICA 在 1 个上错误翻转。ARC 结果不打破 universality 反而 confirms C0 threshold story：high-accuracy condition → low diversity → SICA degenerate。但 C0=6.7% 是 borderline（threshold=5%），不像 QwQ 的 <3% 那么 clean。Worst 档需 consider moving threshold to 10% 或 framing as continuous gradient。"
    tables:
      - "T1_main: ARC-Challenge row (near-degenerate)"
    figures_description:
      - "F3 heatmap: ARC cell near-gray (borderline degenerate)"
    analysis: "ARC 在 worst 档是 supporting data for C0 threshold but with complication：如果 threshold 从 5% 调到 10%，ARC falls below → degenerate (consistent with -1.7pp)。但这使 C0 threshold 变成 tuned parameter 而非 principled cutoff。Paper 需 use 20% as threshold (original) or argue for continuous interpretation。"

  - name: "constraint_quality_correlation"
    plan_id: "exp-019"
    description: "Per-problem constraint precision analysis, correlate with C0 and gap"
    expected_results:
      n_problems_analyzed: 804
      n_multi_candidate: 307
      constraint_precision_mean: 0.52
      constraint_precision_std: 0.21
      constraint_precision_median: 0.48
      bimodal_test_dip_p: 0.04
      high_precision_cluster_n: 95
      high_precision_cluster_mean: 0.74
      low_precision_cluster_n: 212
      low_precision_cluster_mean: 0.41
      precision_vs_c0_per_problem_r: 0.31
      precision_vs_c0_p: 0.002
      precision_vs_sica_correct_r: 0.28
      precision_vs_sica_correct_p: 0.005
      high_precision_sica_win_rate: 0.68
      low_precision_sica_win_rate: 0.44
      f2_non_discriminative_fraction: 0.69
      domain_precision_folio: 0.54
      domain_precision_proofwriter: 0.50
      domain_precision_strategyqa: 0.58
      domain_precision_gsm8k: 0.62
    result_rationale: "Worst 档假设 #2：F2 per-problem 分析揭示 constraint precision 双峰分布。Hartigan dip test p=0.04 confirms bimodality。307 个 multi-candidate 问题分为两个 cluster：95 个 high-precision (mean=0.74) 和 212 个 low-precision (mean=0.41)。High-precision 子集 SICA win rate 68% vs low-precision 44%。Per-problem precision 与 SICA correctness 有 significant correlation (r=0.28, p=0.005)。Non-discriminative fraction=0.69（在 worst 档范围 [0.5, 0.7]）。这证明 capability trap 非 uniform——约 31% 的问题有 adequate constraint quality，但被 69% low-precision 问题稀释到 aggregate null。Precision 与 C0 的 per-problem correlation (r=0.31) 支持 condition-dependent story。"
    tables:
      - "T_precision: Precision distribution statistics + cluster breakdown"
      - "T_precision_domain: Domain × precision mean"
    figures_description:
      - "F2 (hero figure): Per-problem precision histogram showing clear bimodality with dashed line at 0.6 threshold"
      - "F2b: Precision vs SICA-correct scatter (n=307) with logistic regression curve"
      - "F2c: High-precision subset vs low-precision subset SICA/SC comparison bars"
    analysis: "Bimodal precision distribution 是 worst 档 paper 的 centerpiece finding。它解释了 (a) aggregate null (low-precision majority dilutes signal), (b) sporadic positive results on subsets (high-precision problems exist in all domains), (c) condition-dependent pattern (domains/models with more high-precision problems show positive gaps)。Reframed Claim 1 becomes: 'The capability trap is condition-dependent: ~31% of problems yield constraints with precision>0.6, sufficient for MAX-SAT to add value; the remaining 69% produce non-discriminative constraints that reduce MAX-SAT to counting.' 这 more nuanced 但 reviewer 可能认为 'just identifying that precision matters is not novel.' Defense: systematic quantification + oracle proof + C0 deployment diagnostic 作为 joint contribution。"

  - name: "sica_llama8b_strategyqa_200"
    plan_id: "exp-019 (extended)"
    description: "LLaMA-8B on StrategyQA 200 questions — powered replication of suggestive positive signal"
    expected_results:
      n: 200
      k: 12
      sica_accuracy: 0.740
      sc_accuracy: 0.720
      delta_pp: 2.0
      mcnemar_p: 0.424
      multi_candidate_rate: 0.41
      bootstrap_ci_95: [-1.5, 5.5]
      bootstrap_p: 0.12
      discordant_sica_wins: 9
      discordant_sc_wins: 5
    result_rationale: "Powered StrategyQA replication (n=200) 在 worst 档下 attenuates pilot signal：Δ=+2.0pp (vs pilot +5.0pp)，p=0.424 not significant。Regression to mean 部分消除了 n=60 pilot 的 positive signal。但 direction remains positive (9:5 discordant ratio)，CI includes both 0 and +5.5pp。Worst 档 interpretation：true effect is ~+2pp (small but real)，n=200 仍 underpowered to detect。Contributes to meta-analytic estimate 但 individually not significant。"
    tables:
      - "T1_main: LLaMA-8B × StrategyQA row (n=200)"
    figures_description: []
    analysis: "n=200 replication shows classic power problem：effect exists (~2pp) but too small for n=200 to detect reliably。Combined with other positive signals in worst 档 (GSM8K +6.7, 7B +5.0), meta-analytic estimate across positive-signal conditions ≈ +2-3pp。Not zero, but small enough that practical significance is debatable。"

  - name: "sica_llama8b_folio_204"
    plan_id: "exp-020 (powered FOLIO)"
    description: "LLaMA-8B on full FOLIO 204 questions — powered test of +10pp D012 signal"
    expected_results:
      n: 204
      k: 12
      sica_accuracy: 0.623
      sc_accuracy: 0.632
      delta_pp: -0.9
      mcnemar_p: 0.774
      multi_candidate_rate: 0.618
      discordant_sica_wins: 6
      discordant_sc_wins: 7
      constraint_precision_mean: 0.49
      high_precision_subset_n: 42
      high_precision_subset_delta_pp: 4.8
    result_rationale: "Full FOLIO 204 题 overall Δ=-0.9pp (null)，but worst 档 reveals heterogeneity：在 42 个 high-precision 子集 (precision>0.6) 上 SICA = +4.8pp。D012 的 30 题 FOLIO over-sampled 了 high-precision 问题（12/30 vs population rate 42/204=20.6%），解释了 +10pp artifact。真实 effect 在 high-precision subset ≈ +4.8pp，aggregate null 因 dilution。这支持 condition-dependent reframe 但 weakens 'LLaMA-8B×FOLIO is positive operating point' — 只有 subset 是 positive，不是全 domain。"
    tables:
      - "T1_main: LLaMA-8B × FOLIO row (n=204, with subset annotation)"
    figures_description:
      - "Subset analysis: high-precision problems show +4.8pp vs rest showing -2.5pp"
    analysis: "FOLIO 204 结果 resolves D012 +10pp anomaly：sampling artifact from small n that over-represented high-precision problems。True signal exists but only on ~20% of problems。This finding perfectly illustrates the worst-档 narrative：capability trap is real on majority of problems (80%) but not universal (20% show genuine benefit)。"

  - name: "overhead_analysis"
    plan_id: "exp-009"
    description: "Wall-time breakdown per question"
    expected_results:
      n: 804
      mean_total_wall_s: 61.6
      mean_trace_gen_s: 31.6
      trace_gen_pct: 51.3
      mean_extract_s: 29.0
      extract_pct: 47.0
      mean_maxsat_s: 0.003
      maxsat_pct: 0.005
      sica_overhead_pct: 48.7
      cost_per_question_extraction_only: "$0.018"
      breakeven_gain_needed_pp: 3.0
    result_rationale: "Overhead analysis 在 worst 档下 gains new significance：如果 condition-dependent gains 为 +2-5pp on favorable subsets，且 overhead=48.7%，则 cost-benefit analysis becomes interesting rather than trivially negative。Breakeven point ≈ 3pp（considering extraction doubles inference time）。Some worst-档 conditions (GSM8K +6.7, 7B +5.0) exceed breakeven，making SICA conditionally viable rather than universally wasteful。This feeds into the reframed story：practitioners should use C0 + domain formalizability to decide whether SICA overhead is justified。"
    tables:
      - "T_overhead: Time breakdown + cost-benefit analysis by condition"
    figures_description:
      - "Cost-benefit threshold line overlaid on condition-specific gains"
    analysis: "Overhead in worst 档 transitions from 'obviously not worth it' to 'depends on condition.' The deployment framework becomes genuinely useful rather than trivially 'never use SICA.'"

  - name: "meta_analysis_combined"
    plan_id: "cross-experiment synthesis"
    description: "Combined meta-analytic summary across all conditions"
    expected_results:
      total_conditions: 14
      combined_N: 1482
      positive_conditions: 4
      null_conditions: 7
      negative_conditions: 3
      meta_analytic_delta_pp: 1.8
      meta_analytic_ci_95: [0.2, 3.4]
      meta_analytic_p: 0.03
      heterogeneity_I2: 0.62
      heterogeneity_Q_p: 0.008
      positive_condition_mean_delta: 5.1
      null_condition_mean_delta: 0.1
      negative_condition_mean_delta: -2.5
      moderator_precision_p: 0.012
      moderator_c0_p: 0.09
      moderator_domain_formalizability_p: 0.04
    result_rationale: "Worst 档 meta-analytic estimate Δ=+1.8pp [0.2, 3.4]，technically significant (p=0.03) but clinically small。Critical：I²=0.62 indicates substantial heterogeneity (Q-test p=0.008)，meaning a single overall estimate is inappropriate。Moderator analysis reveals constraint precision (p=0.012) and domain formalizability (p=0.04) are significant moderators。This is the statistical backbone for 'condition-dependent phenomenon' reframe：overall small positive，but driven entirely by specific conditions，and other conditions are genuinely null or negative。"
    tables:
      - "T_meta: Forest plot data for all 14 conditions"
    figures_description:
      - "Forest plot: 14 conditions with CIs, overall diamond at +1.8pp, I²=0.62 annotation"
    analysis: "Meta-analytic positive overall (p=0.03) combined with high heterogeneity (I²=0.62) is worst 档的 statistical signature。Can't claim universal null (positive overall)，can't claim universal benefit (heterogeneity)。Must claim condition-dependent phenomenon。This is more complex but arguably more interesting than pure negative — reviewer reaction unpredictable。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8472d9b-cc24-446e-9ab8-a5d3b1dd7670",
  "isSidechain": false,
  "requestId": "req_011Cb8VtsPqAgjt7KmboqFju",
  "type": "assistant",
  "uuid": "8c6aa62a-c231-4310-bf6c-bc61f22b6925",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "c204f04f-d739-4e8b-8879-071fd2e07316",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAr85chwg84u2iZ6Qs7fdZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20448,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14944,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20448,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14944,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20448
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：核心 null universality 被打破或机制证据链断裂；需根本性 reframe，但数据仍支撑 EMNLP 投稿 核心假设：[\"exp-012 GSM8K 或剩余条件出现 Δ>+4pp 且 p<0.05，打破 'universally empty' 叙事\", '或 F2 per-problem 分…",
  "leafUuid": "8c6aa62a-c231-4310-bf6c-bc61f22b6925",
  "sessionId": "c204f04f-d739-4e8b-8879-071fd2e07316"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "When do self-extracted constraints improve LLM reasoning",
  "sessionId": "c204f04f-d739-4e8b-8879-071fd2e07316"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：核心 null universality 被打破或机制证据链断裂；需根本性 reframe，但数据仍支撑 EMNLP 投稿 核心假设：[\"exp-012 GSM8K 或剩余条件出现 Δ>+4pp 且 p<0.05，打破 'universally empty' 叙事\", '或 F2 per-problem 分…",
  "leafUuid": "8c6aa62a-c231-4310-bf6c-bc61f22b6925",
  "sessionId": "c204f04f-d739-4e8b-8879-071fd2e07316"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "When do self-extracted constraints improve LLM reasoning",
  "sessionId": "c204f04f-d739-4e8b-8879-071fd2e07316"
}
```

---
