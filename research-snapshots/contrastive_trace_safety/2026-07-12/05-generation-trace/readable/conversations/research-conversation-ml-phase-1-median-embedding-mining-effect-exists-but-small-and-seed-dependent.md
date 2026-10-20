# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Embedding mining effect exists but small and seed-dependent; BM25 neutral;

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-3/02311cec-ed3a-4d41-9228-47b60120947d.jsonl`
- **Structured JSON:** [`1246335f59dbba414b09.json`](../../sessions/12/1246335f59dbba414b09.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T15:25:43.111Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T15:25:43.111Z",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Embedding mining effect exists but small and seed-dependent; BM25 neutral; criterion effect is main robust finding; need narrative pivot to methodology-first framing\n核心假设：['Qwen 3-seed mean embed-random Δ = +0.3–0.8pp，但 95% CI 下界接近零或轻微包含零', 'StarCoder embed mean Δ 在 -0.2 to +0.3pp，不显著（s42 negative confirmed by pattern）', 'BM25 ≈ random（Δ within ±0.5pp）— CoCoHaNeRe narrative pivot needed', 'D062 checkpoint criterion effect robust（+10–16pp），成为 paper 最强贡献', 'RepoBench-R shows directional consistency but CIs overlap', \"UniXcoder null + StarCoder weak = 'effect is encoder-specific, not universal'\", '3 seeds 对 <1pp effect 统计力度不足，reviewer 会质疑']\n关键指标范围：{'qwen_embed_vs_random_mean_R1_pp': [0.3, 0.8], 'starcoder_embed_vs_random_mean_R1_pp': [-0.2, 0.3], 'bm25_vs_random_mean_R1_pp': [-0.5, 0.5], 'checkpoint_criterion_effect_pp': [10.0, 16.0], 'repobench_embed_vs_random_R1_pp': [0.0, 0.8], 'cross_seed_std_within_strategy_pp': [1.5, 3.0], 'bootstrap_95ci_excludes_zero': False}\n叙事方向：切换到 Framing A：checkpoint selection criterion dominates mining strategy。 主贡献重排：(1) 发现 checkpoint 选择标准对 reported performance 的影响（+10-16pp）远大于 mining strategy 差异（<1pp）， 揭示领域内 evaluation methodology 系统性问题；(2) 在此框架下，embedding mining 作为 controlled experiment 的一个 condition， 在 Qwen 上有 marginal positive signal，但非 universal；(3) representation geometry 分析解释 why effect is encoder-dependent。 Claims 调整：将 \"reliable improvement\" 弱化为 \"conditional improvement on saturated-geometry encoders\"。 UniXcoder null + StarCoder weak 不再是 limitation 而是 evidence for geometry hypothesis。 BM25 neutral → 不能 claim CoCoHaNeRe 的 BM25 proxy 有害，改为 \"mining strategy choice matters less than evaluation methodology\"。 SWE-bench 完全不提。RepoBench-R 作为 supplementary validation。 温度消融（plan_021）变为 must-have 来排除 regime-specificity。 Statistical framing：承认 3 seeds underpowered for <1pp effects，用 effect size + CI 报告而非 p-value。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: structfuse-context\nfocus: 重点关注：(1) D062 checkpoint selection criterion effect (+16.3pp) 作为核心方法论贡献的说服力；(2) 当前双版本 framing (A: criterion dominates vs B: mining + methodology) 哪个更强；(3) UniXcoder null result 作为 architecture-scale boundary condition 的呈现方式；(4) 3 seeds 统计力度是否足够；(5) 缺少 SWE-bench downstream eval（OOD failure R@1=0.04）的影响\n\n## paper_framing.md\n\n# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are \"slow and ineffective\" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.\n\n2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.\n\n- **Headline result template**: \"Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective.\"\n\n## Core Insight\n\nOur pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval\" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]\n- Backup: \"Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### Evidence presentation strategy:\n- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)\n- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)\n- Both metrics show directionally consistent results; no goalpost-moving between metrics\n\n### In progress:\n- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.\n- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.\n- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Limitations\n\nEffect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions\"\n- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main\n\n### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]\n- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment\n- Pivot: \"systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal\"\n- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome\n- Claim 1 core preserved: \"Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling\"\n- Impact: BM25 result determines narrative nuance, not core contribution\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n&lt;!-- Claim 2 wording fix: 2026-05-15 -->\n&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->\n&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->\n&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->\n&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->\n&lt;!-- Status data refresh: s44 DONE, 4/9 runs, m1 90.5%, headline caveat: 2026-05-15 -->\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected\n    vs gold statistics'\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: m1_extraction\n  mvp_registry_id: mvp_p1_codeql_feasibility\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- id: plan_002\n  claim: 1\n  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,\n    3 seeds each, Qwen2.5-Coder-3B LoRA'\n  priority: P0\n  gpu_budget_hours: 200\n  deps:\n  - plan_001\n  registry_id: m2_embed_verify\n  mvp_registry_id: mvp_p2b_contrastive_training\n  full_registry_ids:\n  - m2_full_qwen\n  - m2_full_starcoder\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- id: plan_003\n  claim: 1\n  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best\n    checkpoint, Qwen3.6-27B agent'\n  priority: P0\n  gpu_budget_hours: 40\n  deps:\n  - plan_002\n  notes: eval script ready (eval_swebench.py), dry-run passed, 12 SWE-bench repos\n    pre-cloned to /root/autodl-tmp/structfuse/swebench_repos. Awaiting M2 checkpoint.\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no\n    LLM agent'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  notes: eval script ready (eval_repobench.py), dry-run passed. RepoBench-R data via\n    hf_hub_download. test_easy 8K instances (pool ~6), test_hard 8K (pool ~18). Awaiting\n    M2 checkpoint. [Dream fix] Must run with multiple seeds and report 95% CIs — dream\n    reviewers flagged inconsistent statistical reporting (CIs on SWE-bench but not\n    RepoBench-R) across all 3 tiers.\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding\n    negatives 何时最有害'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  notes: 'analysis script ready (analyze_stratified.py), dry-run passed. 3 strata:\n    repo size / pool size / query-positive similarity. Outputs stratified_results.json\n    + plots PDF. Awaiting M2 checkpoints for re-eval. [Dream fix] Must add 2 more\n    strata: (a) structural data availability (34% with dataflow vs 66% fallback) per\n    [B][M][W] all tiers, (b) neg_difficulty quartile analysis per [W] tier. Total\n    5 strata.'\n  status: planned\n- id: plan_006\n  claim: 3\n  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,\n    connected-but-not-gold ratio by repo size'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan_006_scalability\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- id: plan_007\n  claim: 1\n  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Ablation: fusion head (embedding-only vs structural-features-only\n    vs combined)'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether\n    data-flow helps'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_003\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Qualitative examples: 5-10 cases where structural negatives changed\n    retrieval outcome'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Second encoder validation: repeat M2 core comparison (3 strategies,\n    1 seed) on StarCoder-3B or CodeBERT to test architecture generality'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  dream_source: 'best-R1-W1, median-R2-W5: single encoder is primary generality concern.\n    Upgraded to P0 per Reviewer — this is the #1 factor separating WA from WR.'\n  registry_id: plan_013_starcoder\n  full_registry_id: m2_full_starcoder\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- id: plan_014\n  claim: 2\n  description: 'Temperature ablation: τ ∈ {0.05, 0.1, 0.2} for all 3 strategies, test\n    regime-specificity of embedding harm'\n  priority: P1\n  gpu_budget_hours: 70\n  deps:\n  - plan_002\n  dream_source: 'median-R1-W3: τ=0.05 unusually low, finding may be regime-specific'\n  status: planned\n- id: plan_015\n  claim: 2\n  description: 'Dynamic embedding mining baseline: re-mine embedding negatives per\n    epoch vs static (mine once from pretrained). Isolate selection criterion from\n    curriculum shift.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  dream_source: 'best-R1-W2, median-R1-W2: static vs dynamic mining is potential confound\n    for Claim 2'\n  status: planned\n- id: plan_016\n  claim: 1\n  description: 'Bootstrap CI for SWE-bench Lite: add 95% bootstrap confidence intervals\n    to end-to-end resolve rate evaluation'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  dream_source: 'best-R1-W3, worst-R1-W5: +2.0pp on 300 instances needs statistical\n    significance test'\n  status: planned\n- id: plan_017\n  claim: 1\n  description: 'Inference-time graph method comparison: discuss/compare with CodexGraph,\n    LocAgent — is StructFuse complementary or alternative? Analysis complete, document\n    in artifacts/analysis/plan017_literature_comparison.md. Discussion draft in artifacts/paper_drafts/discussion_draft.md.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  registry_id: plan_017_literature\n  dream_source: 'best-R2-W5: no comparison with inference-time graph methods'\n  notes: 'DONE (analysis only, no experiment). 8 papers surveyed (CodexGraph, LocAgent,\n    RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). All citations verified.\n    Conclusion: training-time vs inference-time are complementary, not competing.'\n  status: DONE\n  conclusion: success\n  metrics:\n    papers_surveyed: 8\n    citations_verified: 8\n    discussion_draft: artifacts/paper_drafts/discussion_v2.md\n    artifact_id: art_20260514_a2e1cd\n- id: plan_018\n  claim: 1\n  description: 'BM25 negative baseline: mine BM25-based hard negatives as 4th strategy,\n    train ≥1 seed × 2 encoders, compare R@1 with random/embedding/dataflow. Empirically\n    verify CoCoHaNeRe BM25-proxy caused the reported harm.'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers identify missing BM25\n    baseline as #1 structural gap. CoCoHaNeRe correction claim requires empirical\n    verification — without it the paper motivation is asserted but unverified.'\n  notes: 'Phase 1 (CPU, can start now): build BM25 index over training corpus, mine\n    top-k BM25 negatives per query using same protocol as other strategies, produce\n    bm25_training_data.jsonl. Phase 2 (GPU, after M2 frees up): train 1 seed × 2 encoders\n    with BM25 negatives (~7.5h each). 3 seeds preferred if GPU budget allows. Expected\n    result: BM25 negatives harm → confirms CoCoHaNeRe artifact → closes argument.'\n  status: planned\n- id: plan_019\n  claim: 1\n  description: 'Pool size sensitivity analysis: test strategy ranking stability at\n    pool={50, 100, 200, 500} candidates per query on SWE-smith validation.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers flag pool=50 as unrealistically\n    small. Strategy differences may not preserve at realistic pool sizes.'\n  notes: Requires M2 best checkpoints. Re-evaluate on expanded candidate pools. If\n    strategy ranking changes at pool>200, must discuss in paper.\n  status: planned\n- id: plan_020\n  claim: 1\n  description: 'UniXcoder multi-seed validation: repeat 3-strategy comparison with\n    seeds 43, 44 on UniXcoder-base (encoder-only, 125M). Statistical validation of\n    cross-architecture generalization beyond single seed.'\n  priority: P1\n  gpu_budget_hours: 6\n  deps:\n  - plan_002\n  notes: 'Depends on UniXcoder s42 completing successfully. UniXcoder 125M trains\n    very fast: 3 strategies serial takes ~2-3h total (confirmed by s42 run). s43+s44\n    = 2 runs × ~3h = ~6h. If time-constrained, at minimum run random+embedding s43\n    for paired comparison.'\n  status: planned\n- id: plan_021\n  claim: 2\n  description: 'Temperature ablation reduced: τ ∈ {0.05, 0.2} × random+embedding ×\n    Qwen × seed 42. Verify whether embedding mining advantage/harm is regime-specific.'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  notes: Reduced scope of plan_014 (70h full → 15h minimum). If τ=0.05 shows different\n    strategy ranking than τ=0.1 (current), confirms regime-specificity claim for Claim\n    2. Run after main training chains complete. Can expand to StarCoder if time allows.\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_p1_codeql_feasibility\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    timeout_rate: 0\n    repos_processed: 8\n    repos_skipped: 2\n    cg_mean_s: 29.6\n    cg_max_s: 119.8\n    df_mean_s: 43.4\n    df_max_s: 167.1\n    h2_connected_coverage: 0.014815\n    h2_disconnected_coverage: 0\n    h2_fisher_p: 6.5e-09\n    h2_gold_in_connected_ratio: 1\n    h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'\n- exp_id: mvp_p2a_linear_proxy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    df_bm25_auc: 0.78\n    bm25_only_auc: 0.476\n    auc_delta: 0.304\n    df_bm25_mrr: 0.556\n    bm25_only_mrr: 0.115\n    mrr_delta: 0.441\n    df_bm25_f1: 0.143\n    bm25_only_f1: 0.039\n    top_feature: is_connected (+2.82)\n    repos_evaluated: 3\n    note: 3 repos / 3 positive samples, directional evidence\n- exp_id: p2b-smoke-test\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke8\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-all-9runs\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_p2b_contrastive_training\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    random_s42_recall1: 0.984\n    random_s123_recall1: 0.984\n    random_s456_recall1: 0.992\n    embedding_s42_recall1: 0.874\n    random_mean_recall1: 0.987\n    runs_completed: 4\n    runs_failed: 5\n    failure_type: disk_full_torch_save\n- exp_id: mvp_p2b_contrastive_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_all\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_4runs_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_seed42:\n      recall@1: 0.9449\n      recall@5: 0.9843\n      recall@10: 0.9843\n    random_seed123:\n      recall@1: 0.9449\n      recall@5: 0.9921\n      recall@10: 0.9921\n    random_seed456:\n      recall@1: 0.9291\n      recall@5: 0.9921\n      recall@10: 0.9921\n    emb_dist_seed42:\n      recall@1: 0.6693\n      recall@5: 0.8898\n      recall@10: 0.9291\n    pool_size: 26\n    n_samples: 127\n- exp_id: p2b_5reruns\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_s42:\n      val_loss: 0.0347\n      recall@1: 0.9843\n    random_s123:\n      val_loss: 0.0446\n      recall@1: 0.9843\n    random_s456:\n      val_loss: 0.0188\n      recall@1: 0.9921\n    emb_dist_s42:\n      val_loss: 0.1876\n      recall@1: 0.874\n    emb_dist_s123:\n      val_loss: 0.1461\n      recall@1: 0.874\n    emb_dist_s456:\n      val_loss: 0.1281\n      recall@1: 0.8819\n    dataflow_s42:\n      val_loss: 0.1878\n      recall@1: 0.874\n    dataflow_s123:\n      val_loss: 0.146\n      recall@1: 0.874\n    dataflow_s456:\n      val_loss: 0.1278\n      recall@1: 0.8819\n    runs_completed: 9\n    runs_failed: 0\n    WARNING: dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds\n      — likely code bug in negative sampling\n- exp_id: p2b_dataflow_retrain\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: p2b_eval_4runs_pool50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pool_size: 50\n    n_samples: 127\n    random_s42:\n      recall@1: 0.496\n      recall@5: 0.843\n      recall@10: 0.945\n    random_s123:\n      recall@1: 0.535\n      recall@5: 0.85\n      recall@10: 0.921\n    random_s456:\n      recall@1: 0.543\n      recall@5: 0.843\n      recall@10: 0.953\n    emb_dist_s42:\n      recall@1: 0.488\n      recall@5: 0.835\n      recall@10: 0.874\n    random_mean:\n      recall@1: 0.525\n      recall@5: 0.845\n      recall@10: 0.94\n    emb_dist_vs_random_delta:\n      recall@1: -0.037\n      recall@5: -0.01\n      recall@10: -0.066\n- exp_id: d007_50repo_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances: 240\n    instances_with_extra_connected: 98\n    Z_pct: 40.8\n    avg_connected_minus_gold: 6\n    codeql_timeout_rate_pct: 4\n    by_repo_size:\n      small_lt50:\n        Z_pct: 38.6\n        avg_extra: 2.5\n      medium_50_200:\n        Z_pct: 55.7\n        avg_extra: 11.8\n      large_gt200:\n        Z_pct: 16.7\n        avg_extra: 8.8\n    decision: Z=40.8% >= 20% -> original method viable, proceed to M1\n- exp_id: m1_extraction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- exp_id: m2_early_pilot\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    pid: 795791\n    gpu: cuda:4\n    gpu_mem_mb: 9342\n    gpu_util_pct: 83\n    batch_size: 2\n    num_negatives: 3\n    max_seq_length: 1024\n    strategy_running: random (stuck at step 4000, epoch 3)\n    strategies_completed: 0/3\n    eval_1500:\n      val_loss: 0.5879\n      recall_at_1: 0.4693\n      recall_at_5: 0.4693\n      recall_at_10: 0.4693\n    eval_2000:\n      val_loss: 0.7089\n      recall_at_1: 0.4398\n    eval_2500:\n      val_loss: 0.6961\n      recall_at_1: 0.4291\n    eval_3000:\n      val_loss: 0.728\n      recall_at_1: 0.4104\n    eval_3500:\n      val_loss: 0.7022\n      recall_at_1: 0.4439\n    best_checkpoint: step_1500 (val_loss=0.5879, 6.2GB)\n    WARNING: recall@1=recall@5=recall@10 confirmed eval bug. Process hung after step\n      4000 (~45min no output). Overfitting after step 1500.\n    status_check_at: '2026-05-13T04:42:00Z'\n- exp_id: m2_early_pilot_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: m2_early_pilot_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: m2_embed_verify\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- exp_id: plan_013_starcoder\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- exp_id: plan_006_scalability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- exp_id: m2_full_qwen\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics:\n    random_s42:\n      status: DONE\n      epoch: 3/3\n      total_steps: 4242\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.4869\n        recall_at_1: 0.533\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.4651\n        recall_at_1: 0.553\n        recall_at_5: 0.959\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.5365\n        recall_at_1: 0.523\n        recall_at_5: 0.955\n        recall_at_10: 1\n      eval_2000:\n        val_loss: 0.5162\n        recall_at_1: 0.523\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_2500:\n        val_loss: 0.5264\n        recall_at_1: 0.527\n        recall_at_5: 0.956\n        recall_at_10: 1\n      eval_3000:\n        val_loss: 0.5406\n        recall_at_1: 0.536\n        recall_at_5: 0.956\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.4651, R@1=0.5527)\n      conclusion: Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357).\n        Full data helps.\n    random_s43:\n      status: DONE\n      epoch: early_stopped\n      total_steps_per_epoch: 1405\n      eval_500:\n        val_loss: 0.4476\n        recall_at_1: 0.5357\n      eval_1000:\n        val_loss: 0.4637\n        recall_at_1: 0.5285\n      eval_1500:\n        recall_at_1: 0.5554\n      best_by_val_loss: step 500 (val_loss=0.4476)\n      best_by_recall_at_1: step 1500 (R@1=0.5554)\n      conclusion: Early stopped at step 1500. Best R@1=0.5554, consistent with s42\n        (0.5527). val_loss and R@1 criterion diverge.\n    random_s44:\n      status: RUNNING\n      note: Auto-started 01:58 CST, epoch 1/2, 1408 batches/epoch\n    progress_snapshot: 2026-05-15T02:00 CST\n- exp_id: m2_full_starcoder\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    random_s42:\n      epoch: 3/3\n      current_step: 4200\n      total_steps: 4242\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.6194\n        recall_at_1: 0.435\n        recall_at_5: 0.905\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.6134\n        recall_at_1: 0.454\n        recall_at_5: 0.92\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.6528\n        recall_at_1: 0.449\n        recall_at_5: 0.906\n        recall_at_10: 1\n      eval_2000:\n        val_loss: 0.6698\n        recall_at_1: 0.4456\n        recall_at_5: 0.906\n        recall_at_10: 1\n      eval_2500:\n        val_loss: 0.6342\n        recall_at_1: 0.4604\n        recall_at_5: 0.9117\n        recall_at_10: 1\n      eval_3000:\n        val_loss: 0.6516\n        recall_at_1: 0.4544\n        recall_at_5: 0.9077\n        recall_at_10: 1\n      eval_3500:\n        val_loss: 0.6588\n        recall_at_1: 0.4534\n        recall_at_5: 0.9057\n        recall_at_10: 1\n      eval_4000:\n        val_loss: 0.6637\n        recall_at_1: 0.4547\n        recall_at_5: 0.9003\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.6134) / step_2500 (R@1=0.4604)\n      conclusion: effectively_complete (timeout at step 4200/4242, lr=7.8e-9, remaining\n        42 steps negligible)\n    progress_snapshot: 2026-05-15T01:50 CST\n- exp_id: m1_reextract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: neg_difficulty_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_128:\n      random:\n        pos_sim: 0.9804\n        neg_sim: 0.899\n        margin: 0.0816\n        pct_positive_margin: 77.8\n      embedding_distance:\n        pos_sim: 0.9804\n        neg_sim: 0.959\n        margin: 0.0209\n        pct_positive_margin: 60.7\n      dataflow_aware:\n        pos_sim: 0.9805\n        neg_sim: 0.95\n        margin: 0.0309\n        pct_positive_margin: 67.4\n    starcoder_128:\n      random:\n        pos_sim: 0.757\n        neg_sim: 0.553\n        margin: 0.2039\n        pct_positive_margin: 72.8\n      embedding_distance:\n        pos_sim: 0.784\n        neg_sim: 0.668\n        margin: 0.1159\n        pct_positive_margin: 59.2\n      dataflow_aware:\n        pos_sim: 0.761\n        neg_sim: 0.659\n        margin: 0.1022\n        pct_positive_margin: 62.8\n    qwen_2048:\n      random:\n        pos_sim: 0.9855\n        neg_sim: 0.9111\n        margin: 0.0743\n        margin_std: 0.2322\n        pct_positive_margin: 81.8\n      embedding_distance:\n        pos_sim: 0.9855\n        neg_sim: 0.9685\n        margin: 0.017\n        margin_std: 0.114\n        pct_positive_margin: 58.8\n      dataflow_aware:\n        pos_sim: 0.9856\n        neg_sim: 0.9563\n        margin: 0.0293\n        margin_std: 0.1407\n        pct_positive_margin: 73.9\n    starcoder_2048:\n      random:\n        pos_sim: 0.7985\n        neg_sim: 0.6045\n        margin: 0.194\n        margin_std: 0.2788\n        pct_positive_margin: 78\n      embedding_distance:\n        pos_sim: 0.8079\n        neg_sim: 0.7409\n        margin: 0.067\n        margin_std: 0.2056\n        pct_positive_margin: 55\n      dataflow_aware:\n        pos_sim: 0.8009\n        neg_sim: 0.6818\n        margin: 0.1192\n        margin_std: 0.2264\n        pct_positive_margin: 70.4\n    sc_qwen_margin_ratio_128:\n      random: 2.5\n      embedding_distance: 5.54\n      dataflow_aware: 3.3\n    sc_qwen_margin_ratio_2048:\n      random: 2.61\n      embedding_distance: 3.94\n      dataflow_aware: 4.07\n- exp_id: m1_reextract_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    all_jsonl_lines: 44173\n    structural_data_instances: 39750\n    structural_data_rate: 0.9\n    codeql_instances: 39730\n    beniget_fallback_instances: 4202\n    remaining_errors: 241\n    errors_replaced: 28035\n    errors_original: 28276\n    repos_completed: 71\n    repos_total: 72\n    skipped_repo: getmoto/moto\n    skip_reason: CodeQL call_graph.ql timeout, Director approved kill+skip (1.2% corpus,\n      zero structural data)\n    output_file_size_gb: 34\n    backup: all.jsonl.bak (6.2GB, pre-combine)\n    combine_stats_artifact: artifacts/m1_final_stats.json\n    combine_completed_at: 2026-05-16T11:13 CST\n- exp_id: plan_018_bm25\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics:\n    phase1_complete: true\n    seed_42:\n      train_records: 11308\n      val_records: 2980\n      train_size_mb: 1280.8\n      val_size_mb: 344.6\n    seed_43:\n      train_records: 11236\n      val_records: 3052\n      train_size_mb: 1280.9\n      val_size_mb: 316\n    seed_44:\n      train_records: 11264\n      val_records: 3024\n      train_size_mb: 1347.1\n      val_size_mb: 295.9\n    bm25_score_dist:\n      count: 392954\n      mean: 246.5\n      std: 155.96\n      p25: 128.38\n      p50: 228.41\n      p75: 347.85\n      max: 2585.74\n    overlap_overall:\n      bm25_vs_embedding: 0.871\n      bm25_vs_random: 0.762\n      bm25_vs_dataflow: 0.718\n      note: k=50 full candidate overlap from mining worker\n    overlap_stratified_top7_jaccard:\n      small_lt50:\n        repos: 39\n        bm25_vs_embedding: 0.668\n        bm25_vs_random: 0.411\n        bm25_vs_dataflow: 0.667\n      medium_50_200:\n        repos: 29\n        bm25_vs_embedding: 0.38\n        bm25_vs_random: 0.067\n        bm25_vs_dataflow: 0.363\n      large_200plus:\n        repos: 15\n        bm25_vs_embedding: 0.297\n        bm25_vs_random: 0.007\n        bm25_vs_dataflow: 0.405\n      matched_queries: 2920\n      total_queries: 12290\n      note: top-7 Jaccard on s42 matched queries only (24% match rate due to different\n        train/val splits)\n- exp_id: plan_015_dynamic\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: m2_full_starcoder_resumed\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    checked_at: 2026-05-16T11:13 CST\n    pid: 519791\n    pid_alive: true\n    gpu: cuda:1, 100% util, 53.5/97.9 GB\n    current_subrun: embedding_distance_s43 (5/8 in chain, step 200/1405, epoch 1)\n    completed_subruns:\n      random_s42:\n        best_R@1: 0.4604\n        best_val_loss: 0.6134\n      random_s43:\n        final_R@1: 0.4859\n        final_val_loss: 0.5503\n      random_s44:\n        final_R@1: 0.4897\n        final_val_loss: 0.6263\n      embedding_distance_s42:\n        final_R@1: 0.4376\n        best_R@1: 0.4567\n        best_val_loss: 0.6154\n        early_stop_step: 1500\n    chain_sequence: random_s43 → random_s44 → embed_s42(done) → embed_s43(running)\n      → embed_s44 → dataflow_s42 → dataflow_s43 → dataflow_s44\n    remaining_subruns:\n    - embed_s43 (running)\n    - embed_s44\n    - dataflow_s42\n    - dataflow_s43\n    - dataflow_s44\n    training_rate: ~9h per subrun\n    eta_full_chain: ~2026-05-18T16:00 CST (~45h)\n    CORRECTION_20260516: bm25_s42 removed — never trained. Running script is old 8-run\n      version without BM25. BM25 StarCoder training requires separate run_m2_full_bm25_starcoder.sh\n      after chain completes.\n- exp_id: m2_full_qwen_continued\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    checked_at: 2026-05-16T19:05 CST\n    pid: 337267\n    pid_alive: true\n    gpu: cuda:0, 99% util, 50.8/95.6 GB\n    current_subrun: dataflow_aware_s44 (7/9, step 1000/2816, epoch 1, loss=0.2142)\n    completed_subruns:\n    - name: random_s42\n      best_R@1: 0.5527\n      best_val_loss: 0.4651\n    - name: random_s43\n      best_R@1: 0.5554\n      best_val_loss: 0.4476\n    - name: random_s44\n      best_R@1: 0.6009\n      best_val_loss: 0.4252\n    - name: embedding_distance_s43\n      best_R@1: 0.5655\n      best_val_loss: 0.4876\n    - name: embedding_distance_s44\n      best_R@1: 0.5942\n      best_val_loss: 0.5123\n    - name: dataflow_aware_s43\n      best_R@1: 0.5564\n      best_val_loss: 0.5137\n    remaining_subruns:\n    - dataflow_aware_s44 (running)\n    - bm25_s43\n    - bm25_s44\n    eval_pool_size: 8\n    dataflow_s44_eval_500:\n      R@1: 0.5701\n- exp_id: plan_017_literature\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    papers_surveyed: 8\n    citations_verified: 8\n    discussion_draft: artifacts/paper_drafts/discussion_v2.md\n    artifact_id: art_20260514_a2e1cd\n- exp_id: plan_005_stratified\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics:\n    confound_analysis:\n      data_validity: ⚠️ R@1 值为 dry-run mock predictions，不可引用。仅分布结构（cross_tabulation.csv）有效。\n      valid_findings:\n        distribution_structure: rich-dataflow 99.3% 落在 large/xlarge repo，small repo\n          中完全不存在\n        correlation:\n          dataflow_edges_vs_repo_size_pearson_r: 0.089\n        cross_distribution:\n          rich_in_large_xlarge_pct: 99.3\n          rich_in_small: 0\n          moderate_in_large_xlarge_pct: 60.9\n        implication: 真实评估必须控制 pool_size 和 repo_size 来隔离 dataflow richness 独立效应\n      invalid_findings: 所有 R@1/R@5/MRR 值均为 mock predictions，策略排序 pattern 不可信，禁止引用\n      artifacts_path: /root/autodl-tmp/structfuse/artifacts/confound_analysis/\n      valid_artifact: cross_tabulation.csv\n- exp_id: plan_003_swebench_eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    checked_at: 2026-05-16T10:40 CST\n    pid_alive: false\n    eval_pid: 61328\n    completion: 100/100 instances for random_s42 (normal exit)\n    results_random_s42_100:\n      R@1: 0.04\n      R@5: 0.11\n      R@10: 0.14\n      R@20: 0.16\n      MRR: 0.0698\n      gold_coverage: 1\n      n_instances: 100\n      errors: 0\n    bm25_baseline_300:\n      R@1: 0.2733\n      R@5: 0.4667\n      R@10: 0.55\n      R@20: 0.6467\n      n_instances: 300\n    note: R@1=0.04 vs BM25=0.2733. Neural retriever 在 OOD 跨 repo 场景泛化失败。\n    director_decision: '2026-05-16: 放弃 SWE-bench 作为论文内容，不再重跑。外部验证改用 plan_004 RepoBench-R。'\n- exp_id: unixcoder-3strat-s42\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    random_s42:\n      status: DONE\n      best_val_loss: 0.4513\n      best_val_loss_step: 400\n      best_R@1: 0.5534\n      best_R@1_step: 1000\n      best_R@5: 0.9772\n      early_stopped_step: 1000\n    embedding_distance_s42:\n      status: DONE\n      best_val_loss: 0.4466\n      best_val_loss_step: 600\n      best_R@1: 0.5497\n      best_R@1_step: 600\n      best_R@5: 0.9772\n      early_stopped_step: 1200\n    dataflow_aware_s42:\n      status: DONE\n      best_val_loss: 0.4628\n      best_val_loss_step: 400\n      best_R@1: 0.551\n      best_R@1_step: 1000\n      best_R@5: 0.9755\n      early_stopped_step: 1000\n    summary:\n      R@1_range: 0.5497-0.5534 (0.37pp span)\n      strategy_ranking_R@1: random > dataflow > embedding\n      strategy_ranking_val_loss: embedding > random > dataflow\n      finding: No meaningful strategy differentiation on UniXcoder-base (125M). All\n        within noise floor.\n    artifact: artifacts/unixcoder-3strat-s42/analysis.json\n- exp_id: unixcoder_3strat_s42\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: qwen_random_s42_retrain\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: unixcoder-3strat-s43\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    random_s43:\n      status: DONE\n      best_R@1: 0.577\n      best_R@5: 0.977\n      best_val_loss: 0.429\n    embedding_distance_s43:\n      status: RUNNING\n    dataflow_aware_s43:\n      status: PENDING\n- exp_id: unixcoder-3strat-s44\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T15:25:43.115Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T15:25:43.115Z",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d"
}
```

---

## Round 1

17 recorded events

### User

_source line 3 · 2026-05-16T15:25:43.136Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Embedding mining effect exists but small and seed-dependent; BM25 neutral; criterion effect is main robust finding; need narrative pivot to methodology-first framing
核心假设：['Qwen 3-seed mean embed-random Δ = +0.3–0.8pp，但 95% CI 下界接近零或轻微包含零', 'StarCoder embed mean Δ 在 -0.2 to +0.3pp，不显著（s42 negative confirmed by pattern）', 'BM25 ≈ random（Δ within ±0.5pp）— CoCoHaNeRe narrative pivot needed', 'D062 checkpoint criterion effect robust（+10–16pp），成为 paper 最强贡献', 'RepoBench-R shows directional consistency but CIs overlap', "UniXcoder null + StarCoder weak = 'effect is encoder-specific, not universal'", '3 seeds 对 <1pp effect 统计力度不足，reviewer 会质疑']
关键指标范围：{'qwen_embed_vs_random_mean_R1_pp': [0.3, 0.8], 'starcoder_embed_vs_random_mean_R1_pp': [-0.2, 0.3], 'bm25_vs_random_mean_R1_pp': [-0.5, 0.5], 'checkpoint_criterion_effect_pp': [10.0, 16.0], 'repobench_embed_vs_random_R1_pp': [0.0, 0.8], 'cross_seed_std_within_strategy_pp': [1.5, 3.0], 'bootstrap_95ci_excludes_zero': False}
叙事方向：切换到 Framing A：checkpoint selection criterion dominates mining strategy。 主贡献重排：(1) 发现 checkpoint 选择标准对 reported performance 的影响（+10-16pp）远大于 mining strategy 差异（<1pp）， 揭示领域内 evaluation methodology 系统性问题；(2) 在此框架下，embedding mining 作为 controlled experiment 的一个 condition， 在 Qwen 上有 marginal positive signal，但非 universal；(3) representation geometry 分析解释 why effect is encoder-dependent。 Claims 调整：将 "reliable improvement" 弱化为 "conditional improvement on saturated-geometry encoders"。 UniXcoder null + StarCoder weak 不再是 limitation 而是 evidence for geometry hypothesis。 BM25 neutral → 不能 claim CoCoHaNeRe 的 BM25 proxy 有害，改为 "mining strategy choice matters less than evaluation methodology"。 SWE-bench 完全不提。RepoBench-R 作为 supplementary validation。 温度消融（plan_021）变为 must-have 来排除 regime-specificity。 Statistical framing：承认 3 seeds underpowered for <1pp effects，用 effect size + CI 报告而非 p-value。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: structfuse-context
focus: 重点关注：(1) D062 checkpoint selection criterion effect (+16.3pp) 作为核心方法论贡献的说服力；(2) 当前双版本 framing (A: criterion dominates vs B: mining + methodology) 哪个更强；(3) UniXcoder null result 作为 architecture-scale boundary condition 的呈现方式；(4) 3 seeds 统计力度是否足够；(5) 缺少 SWE-bench downstream eval（OOD failure R@1=0.04）的影响

## paper_framing.md

# Paper Framing — StructFuse

## Target Venue
- Primary: EMNLP 2026 Main
- Deadline: ARR May 25, 2026

## Core Claims (3)

1. **Simple static embedding-distance mining provides a reliable retrieval improvement for contrastive code retrieval at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies.** CoCoHaNeRe (ACM TOSEM 2025) argues non-differentiable embedding negatives are "slow and ineffective" compared to gradient-based methods — our results show that in structural code retrieval, simple embedding-distance mining yields (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) R@1 over random baselines across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B), without requiring gradient-based mechanisms.

2. **[Exploratory observation] Structure-grounded (dataflow) negatives interact with encoder representation geometry, but do not consistently outperform embedding mining.** Pilot data shows dataflow < embedding on both encoders (Qwen: -1.2pp, StarCoder: -1.0pp R@1 vs embedding). The interaction pattern — Qwen (saturated, pos_sim > 0.98) shows smaller gap than StarCoder (healthy, pos_sim ~ 0.80) — suggests representation geometry mediates strategy effectiveness. neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) offers preliminary mechanistic evidence for this interaction. Pending: multi-seed confirmation + plan_005 stratified analysis + plan_015 dynamic mining control. This is reported as an observation with mechanistic hypothesis, not an established finding.

3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]

## Story Spine

- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.

- **Existing approaches & gaps**:
  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies
  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal
  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
  - CoCoHaNeRe (ACM TOSEM 2025): argues gradient-based hard negative methods outperform non-differentiable embedding negatives — but does not test simple static embedding-distance mining in structural code retrieval settings
  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works

- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) show that simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling, establishing a strong baseline for future work on more sophisticated mining strategies, (2) [exploratory] observe that structure-grounded (dataflow) negatives interact with encoder representation geometry and offer preliminary mechanistic analysis of when/why different strategies may yield different outcomes, and (3) validate findings on downstream SWE-bench task evaluation.

- **Headline result template**: "Simple static embedding-distance mining improves code retrieval in pilot and initial M2 seed (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; consistency across remaining seeds pending; 2 encoders), providing a reliable zero-cost baseline for future work on more sophisticated mining strategies. Structure-grounded (dataflow) negatives show encoder-dependent interaction patterns — representation geometry analysis via negative difficulty offers a candidate mechanistic explanation for when different mining strategies are effective."

## Core Insight

Our pilot data suggests that the effectiveness of hard negative mining strategies may depend on the encoder's representation geometry — a hypothesis derived from two encoders and requiring broader validation. The three strategies explore different dimensions of difficulty: (1) random — no signal baseline; (2) embedding-distance — semantic similarity via pretrained encoder cosine similarity; (3) dataflow-aware — structural filtering (CodeQL-connected files) + lexical similarity (BM25 top-K ranking). When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure + lexical). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction, if confirmed, could help explain contradictory findings in prior work.

## Dual-Pillar Motivation

1. **Primary — Simple embedding mining as reliable zero-cost baseline**: Prior work (CoCoHaNeRe, ACM TOSEM 2025) uses expensive gradient-based hard negative methods for code search. Our controlled comparison shows simple static embedding-distance mining provides a reliable improvement at zero additional computational cost over random sampling, establishing a strong baseline and isolating the effect of each strategy.
2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) offers preliminary explanatory depth beyond empirical comparison, offering a candidate heuristic (pos_sim threshold) that, if validated on more encoders, could help practitioners select strategies without exhaustive experiments.

## Formal Definition

Given retrieval domain D, structural graph G, query q:
**structure-grounded hard negative** = argmax_{x ∈ D : ¬reachable_G(x,q) ∧ x ∉ gold(q)} BM25(q, x)

The structural graph is externally fixed and does not update with the encoder (drift-immune). Negatives are selected from structurally unreachable files (i.e., x ∉ R_G(q), not connected via CodeQL data-flow to the query), ranked by BM25 (lexical similarity).

## Title Options

- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
- Alternative: "Static Embedding Negatives as a Zero-Cost Baseline for Contrastive Code Retrieval" [contingent: activate only if M2 dataflow conditional benefit confirmed across encoders]
- Backup: "Simple Embedding Mining Suffices: A Zero-Cost Baseline for Hard Negative Mining in Code Retrieval"

## Venue Fit

1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
3. **Against "incremental" criticism**: Paper demonstrates a reliable zero-cost baseline + offers preliminary mechanistic analysis of strategy × encoder interaction + validates on downstream task. Three contributions, not one marginal improvement.

## Anticipated Reviewer Concerns

| Concern | Response | Evidence |
|---------|----------|----------|
| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |
| BM25 vs true embedding negatives? | Run BM25 negatives to empirically compare with embedding-distance mining, grounding the comparison against CoCoHaNeRe's gradient-based premise | plan_018 |
| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |
| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |
| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |

## Evidence Status

### Confirmed findings (basis for claims):
- D017: True embedding mining helps (pilot: +2.0pp Qwen, +1.6pp StarCoder; M2 seed 43: +0.52pp best_by_R@1, +0.82pp mean fixed-checkpoint; final range pending s42/s44 completion) — establishes reliable zero-cost baseline
- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential is consistent with hypothesized strategy interaction
- m2_embed_verify (pilot): 3-strategy comparison is consistent with pilot ranking (embedding > random, dataflow conditional)
- plan_013 (StarCoder pilot): Consistent with cross-encoder pattern — embedding helps both, dataflow appears to help Qwen only
- plan_006: CodeQL scalability confirmed at 123-repo scale

### Evidence presentation strategy:
- Primary table: best_by_R@1 (standard practice — select best checkpoint per run by validation R@1)
- Supplementary: fixed-checkpoint comparison as robustness check (not a replacement for best_by_R@1)
- Both metrics show directionally consistent results; no goalpost-moving between metrics

### In progress:
- m2_full_qwen: random s42 DONE (R@1=0.5527), s43 DONE (R@1=0.5554), s44 DONE (R@1=0.6009, early stopped step 500), embedding_distance_s43 DONE (R@1=0.5606, early stopped step 1500). 4/9 runs complete, ~35h remaining.
- m2_full_starcoder: random s42 DONE (R@1=0.4604, from parent), s43 RUNNING (eval@500 R@1=0.4708). 1/9+ runs complete, ~65-70h remaining.
- m1_reextract_v2: 90.5% complete (25,582/28,276), 0 ERROR, ETA ~19:00 CST May 15

### Planned (priority order):
- plan_018: BM25 negative baseline (Dream #1 consensus gap — grounds comparison against CoCoHaNeRe's premise)
- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
- plan_019: Pool size sensitivity (Dream consensus — external validity)
- plan_014: Temperature ablation (Dream reviewer concern)
- plan_004: RepoBench-R second benchmark (with multi-seed CIs)
- plan_015: Dynamic mining baseline
- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)
- plan_007/008/009: Additional ablations

## Limitations

Effect size is smaller than pilot estimates, likely because full-scale training data provides stronger random baselines, reducing the marginal value of targeted negative selection.

## Contingency (if full M2 results weaken claims)

### All 18 runs confirm pilot pattern: Best case
- Full statistical power, paper as framed above
- Target: EMNLP Main

### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
- Drop Claim 2 to analysis observation
- Paper becomes: "Simple embedding mining provides reliable zero-cost improvement + CodeQL extraction is practical + representation geometry analysis may help explain prior contradictions"
- Still publishable: reliable zero-cost baseline demonstration + mechanistic analysis is sufficient for EMNLP Main

### BM25 negatives ≈ random (not harmful): Narrative pivot needed [D030 contingency]
- If plan_018 shows BM25 negatives perform ≈ random (not << random), the narrative positioning needs adjustment
- Pivot: "systematic comparison reveals embedding-distance mining is the only strategy that consistently helps, establishing it as a reliable zero-cost baseline even when BM25 provides no signal"
- Paper remains valid as systematic analysis — the core finding (simple embedding mining provides reliable improvement) stands regardless of BM25 outcome
- Claim 1 core preserved: "Simple static embedding-distance mining provides a reliable retrieval improvement at zero additional computational cost over random sampling"
- Impact: BM25 result determines narrative nuance, not core contribution

### Embedding mining also loses advantage at full scale: Major reassessment needed
- Recheck data pipeline for bugs (full-scale data may have distribution differences)
- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
- Discuss with user before committing direction

## Deprecated Claims (with reason)

- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.

&lt;!-- Claim 2 wording fix: 2026-05-15 -->
&lt;!-- D041 dataflow-aware BM25 fix: 2026-05-15 -->
&lt;!-- D041 formal definition fix: reachable_G → ¬reachable_G, 2026-05-15 -->
&lt;!-- Claim 2 exploratory wording unification: 2026-05-15 -->
&lt;!-- D049 Claim 1 framing update: numbers, narrative softening, evidence strategy, limitations: 2026-05-15 -->
&lt;!-- Status data refresh: s44 DONE, 4/9 runs, m1 90.5%, headline caveat: 2026-05-15 -->


## experiment_plan (with registry status)

- id: plan_001
  claim: 1
  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected
    vs gold statistics'
  priority: P0
  gpu_budget_hours: 0
  deps: []
  registry_id: m1_extraction
  mvp_registry_id: mvp_p1_codeql_feasibility
  status: DONE
  conclusion: success
  metrics:
    total_instances_attempted: 44173
    instances_skipped: 6696
    total_instances: 50869
    codeql_success: 15133
    beniget_fallback: 764
    extraction_failed: 28276
    structural_data_rate: 0.36
    repos_with_output: 123
    repos_total: 131
    repo_coverage: 0.939
    skip_clone_failed: 5852
    skip_checkout_failed: 836
    skip_stale_handle: 8
    elapsed_minutes: 837.8
    avg_time_per_instance_s: 8.9
    output_size_gb: 6.6
    disk_usage_gb: 13
    output_file: all.jsonl
- id: plan_002
  claim: 1
  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,
    3 seeds each, Qwen2.5-Coder-3B LoRA'
  priority: P0
  gpu_budget_hours: 200
  deps:
  - plan_001
  registry_id: m2_embed_verify
  mvp_registry_id: mvp_p2b_contrastive_training
  full_registry_ids:
  - m2_full_qwen
  - m2_full_starcoder
  status: DONE
  conclusion: success
  metrics:
    random:
      status: DONE
      best_step: 500
      best_val_loss: 0.4834
      best_recall@1: 0.5357
      best_recall@5: 0.9808
      best_recall@10: 1
      final_val_loss: 0.5978
      final_recall@1: 0.5122
    embedding_distance:
      status: DONE
      best_step: 500
      best_val_loss: 0.4603
      best_recall@1: 0.5557
      best_recall@5: 0.9808
      best_recall@10: 1
      final_val_loss: 0.5935
      final_recall@1: 0.5209
    dataflow_aware:
      status: DONE
      best_step: 500
      best_val_loss: 0.5602
      best_recall@1: 0.5436
      best_recall@5: 0.9817
      best_recall@10: 1
      final_val_loss: 0.6201
      final_recall@1: 0.5287
- id: plan_003
  claim: 1
  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best
    checkpoint, Qwen3.6-27B agent'
  priority: P0
  gpu_budget_hours: 40
  deps:
  - plan_002
  notes: eval script ready (eval_swebench.py), dry-run passed, 12 SWE-bench repos
    pre-cloned to /root/autodl-tmp/structfuse/swebench_repos. Awaiting M2 checkpoint.
  status: planned
- id: plan_004
  claim: 1
  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no
    LLM agent'
  priority: P1
  gpu_budget_hours: 15
  deps:
  - plan_002
  notes: eval script ready (eval_repobench.py), dry-run passed. RepoBench-R data via
    hf_hub_download. test_easy 8K instances (pool ~6), test_hard 8K (pool ~18). Awaiting
    M2 checkpoint. [Dream fix] Must run with multiple seeds and report 95% CIs — dream
    reviewers flagged inconsistent statistical reporting (CIs on SWE-bench but not
    RepoBench-R) across all 3 tiers.
  status: planned
- id: plan_005
  claim: 2
  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding
    negatives 何时最有害'
  priority: P1
  gpu_budget_hours: 5
  deps:
  - plan_002
  notes: 'analysis script ready (analyze_stratified.py), dry-run passed. 3 strata:
    repo size / pool size / query-positive similarity. Outputs stratified_results.json
    + plots PDF. Awaiting M2 checkpoints for re-eval. [Dream fix] Must add 2 more
    strata: (a) structural data availability (34% with dataflow vs 66% fallback) per
    [B][M][W] all tiers, (b) neg_difficulty quartile analysis per [W] tier. Total
    5 strata.'
  status: planned
- id: plan_006
  claim: 3
  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,
    connected-but-not-gold ratio by repo size'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: plan_006_scalability
  status: DONE
  conclusion: success
  metrics:
    repos: 123
    total_instances: 44173
    structural_data_rate: 0.343
    error_rate: 0.64
    zero_timeout_rate: true
    processing_time:
      mean_s: 8.93
      median_s: 0
      p95_s: 31.95
      max_s: 633.68
      total_hours: 109.58
    by_tier:
      small_lt50:
        repos: 1
        instances: 500
        error_rate: 0.054
        struct_rate: 0.81
        z_pct_mean: 0.284
        z_pct_median: 0
      medium_50_200:
        repos: 17
        instances: 4096
        error_rate: 0.485
        struct_rate: 0.472
        z_pct_mean: 0.444
        z_pct_median: 0.5
      large_200_500:
        repos: 40
        instances: 13628
        error_rate: 0.639
        struct_rate: 0.343
        z_pct_mean: 0.604
        z_pct_median: 0.857
      xlarge_500plus:
        repos: 29
        instances: 25949
        error_rate: 0.676
        struct_rate: 0.314
        z_pct_mean: 0.812
        z_pct_median: 0.96
    instance_distribution:
      lt10: 1
      '10_50': 17
      '50_200': 36
      '200_500': 40
      500plus: 29
    artifact: plan006_full_scalability.json
- id: plan_007
  claim: 1
  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'
  priority: P1
  gpu_budget_hours: 20
  deps:
  - plan_001
  status: planned
- id: plan_008
  claim: 1
  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'
  priority: P1
  gpu_budget_hours: 15
  deps:
  - plan_001
  status: planned
- id: plan_009
  claim: 1
  description: 'Ablation: fusion head (embedding-only vs structural-features-only
    vs combined)'
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan_002
  status: planned
- id: plan_010
  claim: 1
  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'
  priority: P2
  gpu_budget_hours: 10
  deps:
  - plan_001
  status: planned
- id: plan_011
  claim: 1
  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether
    data-flow helps'
  priority: P1
  gpu_budget_hours: 5
  deps:
  - plan_003
  status: planned
- id: plan_012
  claim: 1
  description: 'Qualitative examples: 5-10 cases where structural negatives changed
    retrieval outcome'
  priority: P2
  gpu_budget_hours: 0
  deps:
  - plan_003
  status: planned
- id: plan_013
  claim: 1
  description: 'Second encoder validation: repeat M2 core comparison (3 strategies,
    1 seed) on StarCoder-3B or CodeBERT to test architecture generality'
  priority: P0
  gpu_budget_hours: 15
  deps:
  - plan_001
  dream_source: 'best-R1-W1, median-R2-W5: single encoder is primary generality concern.
    Upgraded to P0 per Reviewer — this is the #1 factor separating WA from WR.'
  registry_id: plan_013_starcoder
  full_registry_id: m2_full_starcoder
  status: DONE
  conclusion: negative
  metrics:
    random:
      status: DONE
      best_val_loss: 0.5113
      best_recall@1: 0.4922
      best_recall@5: 0.98
      best_recall@10: 1
      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)
    embedding_distance:
      status: DONE
      best_step: 1000
      best_val_loss: 0.4816
      best_recall@1: 0.5078
      best_recall@5: 0.9843
      best_recall@10: 1
      final_val_loss: 0.506
      final_recall@1: 0.5174
    dataflow_aware:
      status: DONE
      best_step: 1000
      best_val_loss: 0.5255
      best_recall@1: 0.4869
      best_recall@5: 0.9695
      best_recall@10: 1
      final_val_loss: 0.5509
      final_recall@1: 0.5078
- id: plan_014
  claim: 2
  description: 'Temperature ablation: τ ∈ {0.05, 0.1, 0.2} for all 3 strategies, test
    regime-specificity of embedding harm'
  priority: P1
  gpu_budget_hours: 70
  deps:
  - plan_002
  dream_source: 'median-R1-W3: τ=0.05 unusually low, finding may be regime-specific'
  status: planned
- id: plan_015
  claim: 2
  description: 'Dynamic embedding mining baseline: re-mine embedding negatives per
    epoch vs static (mine once from pretrained). Isolate selection criterion from
    curriculum shift.'
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan_002
  dream_source: 'best-R1-W2, median-R1-W2: static vs dynamic mining is potential confound
    for Claim 2'
  status: planned
- id: plan_016
  claim: 1
  description: 'Bootstrap CI for SWE-bench Lite: add 95% bootstrap confidence intervals
    to end-to-end resolve rate evaluation'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_003
  dream_source: 'best-R1-W3, worst-R1-W5: +2.0pp on 300 instances needs statistical
    significance test'
  status: planned
- id: plan_017
  claim: 1
  description: 'Inference-time graph method comparison: discuss/compare with CodexGraph,
    LocAgent — is StructFuse complementary or alternative? Analysis complete, document
    in artifacts/analysis/plan017_literature_comparison.md. Discussion draft in artifacts/paper_drafts/discussion_draft.md.'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_002
  registry_id: plan_017_literature
  dream_source: 'best-R2-W5: no comparison with inference-time graph methods'
  notes: 'DONE (analysis only, no experiment). 8 papers surveyed (CodexGraph, LocAgent,
    RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). All citations verified.
    Conclusion: training-time vs inference-time are complementary, not competing.'
  status: DONE
  conclusion: success
  metrics:
    papers_surveyed: 8
    citations_verified: 8
    discussion_draft: artifacts/paper_drafts/discussion_v2.md
    artifact_id: art_20260514_a2e1cd
- id: plan_018
  claim: 1
  description: 'BM25 negative baseline: mine BM25-based hard negatives as 4th strategy,
    train ≥1 seed × 2 encoders, compare R@1 with random/embedding/dataflow. Empirically
    verify CoCoHaNeRe BM25-proxy caused the reported harm.'
  priority: P0
  gpu_budget_hours: 15
  deps:
  - plan_001
  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers identify missing BM25
    baseline as #1 structural gap. CoCoHaNeRe correction claim requires empirical
    verification — without it the paper motivation is asserted but unverified.'
  notes: 'Phase 1 (CPU, can start now): build BM25 index over training corpus, mine
    top-k BM25 negatives per query using same protocol as other strategies, produce
    bm25_training_data.jsonl. Phase 2 (GPU, after M2 frees up): train 1 seed × 2 encoders
    with BM25 negatives (~7.5h each). 3 seeds preferred if GPU budget allows. Expected
    result: BM25 negatives harm → confirms CoCoHaNeRe artifact → closes argument.'
  status: planned
- id: plan_019
  claim: 1
  description: 'Pool size sensitivity analysis: test strategy ranking stability at
    pool={50, 100, 200, 500} candidates per query on SWE-smith validation.'
  priority: P1
  gpu_budget_hours: 5
  deps:
  - plan_002
  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers flag pool=50 as unrealistically
    small. Strategy differences may not preserve at realistic pool sizes.'
  notes: Requires M2 best checkpoints. Re-evaluate on expanded candidate pools. If
    strategy ranking changes at pool>200, must discuss in paper.
  status: planned
- id: plan_020
  claim: 1
  description: 'UniXcoder multi-seed validation: repeat 3-strategy comparison with
    seeds 43, 44 on UniXcoder-base (encoder-only, 125M). Statistical validation of
    cross-architecture generalization beyond single seed.'
  priority: P1
  gpu_budget_hours: 6
  deps:
  - plan_002
  notes: 'Depends on UniXcoder s42 completing successfully. UniXcoder 125M trains
    very fast: 3 strategies serial takes ~2-3h total (confirmed by s42 run). s43+s44
    = 2 runs × ~3h = ~6h. If time-constrained, at minimum run random+embedding s43
    for paired comparison.'
  status: planned
- id: plan_021
  claim: 2
  description: 'Temperature ablation reduced: τ ∈ {0.05, 0.2} × random+embedding ×
    Qwen × seed 42. Verify whether embedding mining advantage/harm is regime-specific.'
  priority: P1
  gpu_budget_hours: 15
  deps:
  - plan_002
  notes: Reduced scope of plan_014 (70h full → 15h minimum). If τ=0.05 shows different
    strategy ranking than τ=0.1 (current), confirms regime-specificity claim for Claim
    2. Run after main training chains complete. Can expand to StarCoder if time allows.
  status: planned


## registry (completed experiments)

- exp_id: mvp_p1_codeql_feasibility
  name: ''
  status: DONE
  conclusion: success
  metrics:
    timeout_rate: 0
    repos_processed: 8
    repos_skipped: 2
    cg_mean_s: 29.6
    cg_max_s: 119.8
    df_mean_s: 43.4
    df_max_s: 167.1
    h2_connected_coverage: 0.014815
    h2_disconnected_coverage: 0
    h2_fisher_p: 6.5e-09
    h2_gold_in_connected_ratio: 1
    h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'
- exp_id: mvp_p2a_linear_proxy
  name: ''
  status: DONE
  conclusion: success
  metrics:
    df_bm25_auc: 0.78
    bm25_only_auc: 0.476
    auc_delta: 0.304
    df_bm25_mrr: 0.556
    bm25_only_mrr: 0.115
    mrr_delta: 0.441
    df_bm25_f1: 0.143
    bm25_only_f1: 0.039
    top_feature: is_connected (+2.82)
    repos_evaluated: 3
    note: 3 repos / 3 positive samples, directional evidence
- exp_id: p2b-smoke-test
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke3
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke4
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke5
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke6
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke7
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-smoke8
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b-all-9runs
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_p2b_contrastive_training
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    random_s42_recall1: 0.984
    random_s123_recall1: 0.984
    random_s456_recall1: 0.992
    embedding_s42_recall1: 0.874
    random_mean_recall1: 0.987
    runs_completed: 4
    runs_failed: 5
    failure_type: disk_full_torch_save
- exp_id: mvp_p2b_contrastive_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b_eval_all
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: p2b_eval_4runs_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    random_seed42:
      recall@1: 0.9449
      recall@5: 0.9843
      recall@10: 0.9843
    random_seed123:
      recall@1: 0.9449
      recall@5: 0.9921
      recall@10: 0.9921
    random_seed456:
      recall@1: 0.9291
      recall@5: 0.9921
      recall@10: 0.9921
    emb_dist_seed42:
      recall@1: 0.6693
      recall@5: 0.8898
      recall@10: 0.9291
    pool_size: 26
    n_samples: 127
- exp_id: p2b_5reruns
  name: ''
  status: DONE
  conclusion: success
  metrics:
    random_s42:
      val_loss: 0.0347
      recall@1: 0.9843
    random_s123:
      val_loss: 0.0446
      recall@1: 0.9843
    random_s456:
      val_loss: 0.0188
      recall@1: 0.9921
    emb_dist_s42:
      val_loss: 0.1876
      recall@1: 0.874
    emb_dist_s123:
      val_loss: 0.1461
      recall@1: 0.874
    emb_dist_s456:
      val_loss: 0.1281
      recall@1: 0.8819
    dataflow_s42:
      val_loss: 0.1878
      recall@1: 0.874
    dataflow_s123:
      val_loss: 0.146
      recall@1: 0.874
    dataflow_s456:
      val_loss: 0.1278
      recall@1: 0.8819
    runs_completed: 9
    runs_failed: 0
    WARNING: dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds
      — likely code bug in negative sampling
- exp_id: p2b_dataflow_retrain
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: p2b_eval_4runs_pool50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pool_size: 50
    n_samples: 127
    random_s42:
      recall@1: 0.496
      recall@5: 0.843
      recall@10: 0.945
    random_s123:
      recall@1: 0.535
      recall@5: 0.85
      recall@10: 0.921
    random_s456:
      recall@1: 0.543
      recall@5: 0.843
      recall@10: 0.953
    emb_dist_s42:
      recall@1: 0.488
      recall@5: 0.835
      recall@10: 0.874
    random_mean:
      recall@1: 0.525
      recall@5: 0.845
      recall@10: 0.94
    emb_dist_vs_random_delta:
      recall@1: -0.037
      recall@5: -0.01
      recall@10: -0.066
- exp_id: d007_50repo_overlap
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_instances: 240
    instances_with_extra_connected: 98
    Z_pct: 40.8
    avg_connected_minus_gold: 6
    codeql_timeout_rate_pct: 4
    by_repo_size:
      small_lt50:
        Z_pct: 38.6
        avg_extra: 2.5
      medium_50_200:
        Z_pct: 55.7
        avg_extra: 11.8
      large_gt200:
        Z_pct: 16.7
        avg_extra: 8.8
    decision: Z=40.8% >= 20% -> original method viable, proceed to M1
- exp_id: m1_extraction
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_instances_attempted: 44173
    instances_skipped: 6696
    total_instances: 50869
    codeql_success: 15133
    beniget_fallback: 764
    extraction_failed: 28276
    structural_data_rate: 0.36
    repos_with_output: 123
    repos_total: 131
    repo_coverage: 0.939
    skip_clone_failed: 5852
    skip_checkout_failed: 836
    skip_stale_handle: 8
    elapsed_minutes: 837.8
    avg_time_per_instance_s: 8.9
    output_size_gb: 6.6
    disk_usage_gb: 13
    output_file: all.jsonl
- exp_id: m2_early_pilot
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    pid: 795791
    gpu: cuda:4
    gpu_mem_mb: 9342
    gpu_util_pct: 83
    batch_size: 2
    num_negatives: 3
    max_seq_length: 1024
    strategy_running: random (stuck at step 4000, epoch 3)
    strategies_completed: 0/3
    eval_1500:
      val_loss: 0.5879
      recall_at_1: 0.4693
      recall_at_5: 0.4693
      recall_at_10: 0.4693
    eval_2000:
      val_loss: 0.7089
      recall_at_1: 0.4398
    eval_2500:
      val_loss: 0.6961
      recall_at_1: 0.4291
    eval_3000:
      val_loss: 0.728
      recall_at_1: 0.4104
    eval_3500:
      val_loss: 0.7022
      recall_at_1: 0.4439
    best_checkpoint: step_1500 (val_loss=0.5879, 6.2GB)
    WARNING: recall@1=recall@5=recall@10 confirmed eval bug. Process hung after step
      4000 (~45min no output). Overfitting after step 1500.
    status_check_at: '2026-05-13T04:42:00Z'
- exp_id: m2_early_pilot_v2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: m2_early_pilot_v3
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: m2_embed_verify
  name: ''
  status: DONE
  conclusion: success
  metrics:
    random:
      status: DONE
      best_step: 500
      best_val_loss: 0.4834
      best_recall@1: 0.5357
      best_recall@5: 0.9808
      best_recall@10: 1
      final_val_loss: 0.5978
      final_recall@1: 0.5122
    embedding_distance:
      status: DONE
      best_step: 500
      best_val_loss: 0.4603
      best_recall@1: 0.5557
      best_recall@5: 0.9808
      best_recall@10: 1
      final_val_loss: 0.5935
      final_recall@1: 0.5209
    dataflow_aware:
      status: DONE
      best_step: 500
      best_val_loss: 0.5602
      best_recall@1: 0.5436
      best_recall@5: 0.9817
      best_recall@10: 1
      final_val_loss: 0.6201
      final_recall@1: 0.5287
- exp_id: plan_013_starcoder
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    random:
      status: DONE
      best_val_loss: 0.5113
      best_recall@1: 0.4922
      best_recall@5: 0.98
      best_recall@10: 1
      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)
    embedding_distance:
      status: DONE
      best_step: 1000
      best_val_loss: 0.4816
      best_recall@1: 0.5078
      best_recall@5: 0.9843
      best_recall@10: 1
      final_val_loss: 0.506
      final_recall@1: 0.5174
    dataflow_aware:
      status: DONE
      best_step: 1000
      best_val_loss: 0.5255
      best_recall@1: 0.4869
      best_recall@5: 0.9695
      best_recall@10: 1
      final_val_loss: 0.5509
      final_recall@1: 0.5078
- exp_id: plan_006_scalability
  name: ''
  status: DONE
  conclusion: success
  metrics:
    repos: 123
    total_instances: 44173
    structural_data_rate: 0.343
    error_rate: 0.64
    zero_timeout_rate: true
    processing_time:
      mean_s: 8.93
      median_s: 0
      p95_s: 31.95
      max_s: 633.68
      total_hours: 109.58
    by_tier:
      small_lt50:
        repos: 1
        instances: 500
        error_rate: 0.054
        struct_rate: 0.81
        z_pct_mean: 0.284
        z_pct_median: 0
      medium_50_200:
        repos: 17
        instances: 4096
        error_rate: 0.485
        struct_rate: 0.472
        z_pct_mean: 0.444
        z_pct_median: 0.5
      large_200_500:
        repos: 40
        instances: 13628
        error_rate: 0.639
        struct_rate: 0.343
        z_pct_mean: 0.604
        z_pct_median: 0.857
      xlarge_500plus:
        repos: 29
        instances: 25949
        error_rate: 0.676
        struct_rate: 0.314
        z_pct_mean: 0.812
        z_pct_median: 0.96
    instance_distribution:
      lt10: 1
      '10_50': 17
      '50_200': 36
      '200_500': 40
      500plus: 29
    artifact: plan006_full_scalability.json
- exp_id: m2_full_qwen
  name: ''
  status: ANALYZING
  conclusion: ''
  metrics:
    random_s42:
      status: DONE
      epoch: 3/3
      total_steps: 4242
      total_steps_per_epoch: 1414
      eval_500:
        val_loss: 0.4869
        recall_at_1: 0.533
        recall_at_5: 0.954
        recall_at_10: 1
      eval_1000:
        val_loss: 0.4651
        recall_at_1: 0.553
        recall_at_5: 0.959
        recall_at_10: 1
      eval_1500:
        val_loss: 0.5365
        recall_at_1: 0.523
        recall_at_5: 0.955
        recall_at_10: 1
      eval_2000:
        val_loss: 0.5162
        recall_at_1: 0.523
        recall_at_5: 0.954
        recall_at_10: 1
      eval_2500:
        val_loss: 0.5264
        recall_at_1: 0.527
        recall_at_5: 0.956
        recall_at_10: 1
      eval_3000:
        val_loss: 0.5406
        recall_at_1: 0.536
        recall_at_5: 0.956
        recall_at_10: 1
      best_checkpoint: step_1000 (val_loss=0.4651, R@1=0.5527)
      conclusion: Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357).
        Full data helps.
    random_s43:
      status: DONE
      epoch: early_stopped
      total_steps_per_epoch: 1405
      eval_500:
        val_loss: 0.4476
        recall_at_1: 0.5357
      eval_1000:
        val_loss: 0.4637
        recall_at_1: 0.5285
      eval_1500:
        recall_at_1: 0.5554
      best_by_val_loss: step 500 (val_loss=0.4476)
      best_by_recall_at_1: step 1500 (R@1=0.5554)
      conclusion: Early stopped at step 1500. Best R@1=0.5554, consistent with s42
        (0.5527). val_loss and R@1 criterion diverge.
    random_s44:
      status: RUNNING
      note: Auto-started 01:58 CST, epoch 1/2, 1408 batches/epoch
    progress_snapshot: 2026-05-15T02:00 CST
- exp_id: m2_full_starcoder
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    random_s42:
      epoch: 3/3
      current_step: 4200
      total_steps: 4242
      total_steps_per_epoch: 1414
      eval_500:
        val_loss: 0.6194
        recall_at_1: 0.435
        recall_at_5: 0.905
        recall_at_10: 1
      eval_1000:
        val_loss: 0.6134
        recall_at_1: 0.454
        recall_at_5: 0.92
        recall_at_10: 1
      eval_1500:
        val_loss: 0.6528
        recall_at_1: 0.449
        recall_at_5: 0.906
        recall_at_10: 1
      eval_2000:
        val_loss: 0.6698
        recall_at_1: 0.4456
        recall_at_5: 0.906
        recall_at_10: 1
      eval_2500:
        val_loss: 0.6342
        recall_at_1: 0.4604
        recall_at_5: 0.9117
        recall_at_10: 1
      eval_3000:
        val_loss: 0.6516
        recall_at_1: 0.4544
        recall_at_5: 0.9077
        recall_at_10: 1
      eval_3500:
        val_loss: 0.6588
        recall_at_1: 0.4534
        recall_at_5: 0.9057
        recall_at_10: 1
      eval_4000:
        val_loss: 0.6637
        recall_at_1: 0.4547
        recall_at_5: 0.9003
        recall_at_10: 1
      best_checkpoint: step_1000 (val_loss=0.6134) / step_2500 (R@1=0.4604)
      conclusion: effectively_complete (timeout at step 4200/4242, lr=7.8e-9, remaining
        42 steps negligible)
    progress_snapshot: 2026-05-15T01:50 CST
- exp_id: m1_reextract
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: neg_difficulty_analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    qwen_128:
      random:
        pos_sim: 0.9804
        neg_sim: 0.899
        margin: 0.0816
        pct_positive_margin: 77.8
      embedding_distance:
        pos_sim: 0.9804
        neg_sim: 0.959
        margin: 0.0209
        pct_positive_margin: 60.7
      dataflow_aware:
        pos_sim: 0.9805
        neg_sim: 0.95
        margin: 0.0309
        pct_positive_margin: 67.4
    starcoder_128:
      random:
        pos_sim: 0.757
        neg_sim: 0.553
        margin: 0.2039
        pct_positive_margin: 72.8
      embedding_distance:
        pos_sim: 0.784
        neg_sim: 0.668
        margin: 0.1159
        pct_positive_margin: 59.2
      dataflow_aware:
        pos_sim: 0.761
        neg_sim: 0.659
        margin: 0.1022
        pct_positive_margin: 62.8
    qwen_2048:
      random:
        pos_sim: 0.9855
        neg_sim: 0.9111
        margin: 0.0743
        margin_std: 0.2322
        pct_positive_margin: 81.8
      embedding_distance:
        pos_sim: 0.9855
        neg_sim: 0.9685
        margin: 0.017
        margin_std: 0.114
        pct_positive_margin: 58.8
      dataflow_aware:
        pos_sim: 0.9856
        neg_sim: 0.9563
        margin: 0.0293
        margin_std: 0.1407
        pct_positive_margin: 73.9
    starcoder_2048:
      random:
        pos_sim: 0.7985
        neg_sim: 0.6045
        margin: 0.194
        margin_std: 0.2788
        pct_positive_margin: 78
      embedding_distance:
        pos_sim: 0.8079
        neg_sim: 0.7409
        margin: 0.067
        margin_std: 0.2056
        pct_positive_margin: 55
      dataflow_aware:
        pos_sim: 0.8009
        neg_sim: 0.6818
        margin: 0.1192
        margin_std: 0.2264
        pct_positive_margin: 70.4
    sc_qwen_margin_ratio_128:
      random: 2.5
      embedding_distance: 5.54
      dataflow_aware: 3.3
    sc_qwen_margin_ratio_2048:
      random: 2.61
      embedding_distance: 3.94
      dataflow_aware: 4.07
- exp_id: m1_reextract_v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    all_jsonl_lines: 44173
    structural_data_instances: 39750
    structural_data_rate: 0.9
    codeql_instances: 39730
    beniget_fallback_instances: 4202
    remaining_errors: 241
    errors_replaced: 28035
    errors_original: 28276
    repos_completed: 71
    repos_total: 72
    skipped_repo: getmoto/moto
    skip_reason: CodeQL call_graph.ql timeout, Director approved kill+skip (1.2% corpus,
      zero structural data)
    output_file_size_gb: 34
    backup: all.jsonl.bak (6.2GB, pre-combine)
    combine_stats_artifact: artifacts/m1_final_stats.json
    combine_completed_at: 2026-05-16T11:13 CST
- exp_id: plan_018_bm25
  name: ''
  status: QUEUED
  conclusion: ''
  metrics:
    phase1_complete: true
    seed_42:
      train_records: 11308
      val_records: 2980
      train_size_mb: 1280.8
      val_size_mb: 344.6
    seed_43:
      train_records: 11236
      val_records: 3052
      train_size_mb: 1280.9
      val_size_mb: 316
    seed_44:
      train_records: 11264
      val_records: 3024
      train_size_mb: 1347.1
      val_size_mb: 295.9
    bm25_score_dist:
      count: 392954
      mean: 246.5
      std: 155.96
      p25: 128.38
      p50: 228.41
      p75: 347.85
      max: 2585.74
    overlap_overall:
      bm25_vs_embedding: 0.871
      bm25_vs_random: 0.762
      bm25_vs_dataflow: 0.718
      note: k=50 full candidate overlap from mining worker
    overlap_stratified_top7_jaccard:
      small_lt50:
        repos: 39
        bm25_vs_embedding: 0.668
        bm25_vs_random: 0.411
        bm25_vs_dataflow: 0.667
      medium_50_200:
        repos: 29
        bm25_vs_embedding: 0.38
        bm25_vs_random: 0.067
        bm25_vs_dataflow: 0.363
      large_200plus:
        repos: 15
        bm25_vs_embedding: 0.297
        bm25_vs_random: 0.007
        bm25_vs_dataflow: 0.405
      matched_queries: 2920
      total_queries: 12290
      note: top-7 Jaccard on s42 matched queries only (24% match rate due to different
        train/val splits)
- exp_id: plan_015_dynamic
  name: ''
  status: QUEUED
  conclusion: ''
  metrics: {}
- exp_id: m2_full_starcoder_resumed
  name: ''
  status: RUNNING
  conclusion: ''
  metrics:
    checked_at: 2026-05-16T11:13 CST
    pid: 519791
    pid_alive: true
    gpu: cuda:1, 100% util, 53.5/97.9 GB
    current_subrun: embedding_distance_s43 (5/8 in chain, step 200/1405, epoch 1)
    completed_subruns:
      random_s42:
        best_R@1: 0.4604
        best_val_loss: 0.6134
      random_s43:
        final_R@1: 0.4859
        final_val_loss: 0.5503
      random_s44:
        final_R@1: 0.4897
        final_val_loss: 0.6263
      embedding_distance_s42:
        final_R@1: 0.4376
        best_R@1: 0.4567
        best_val_loss: 0.6154
        early_stop_step: 1500
    chain_sequence: random_s43 → random_s44 → embed_s42(done) → embed_s43(running)
      → embed_s44 → dataflow_s42 → dataflow_s43 → dataflow_s44
    remaining_subruns:
    - embed_s43 (running)
    - embed_s44
    - dataflow_s42
    - dataflow_s43
    - dataflow_s44
    training_rate: ~9h per subrun
    eta_full_chain: ~2026-05-18T16:00 CST (~45h)
    CORRECTION_20260516: bm25_s42 removed — never trained. Running script is old 8-run
      version without BM25. BM25 StarCoder training requires separate run_m2_full_bm25_starcoder.sh
      after chain completes.
- exp_id: m2_full_qwen_continued
  name: ''
  status: RUNNING
  conclusion: ''
  metrics:
    checked_at: 2026-05-16T19:05 CST
    pid: 337267
    pid_alive: true
    gpu: cuda:0, 99% util, 50.8/95.6 GB
    current_subrun: dataflow_aware_s44 (7/9, step 1000/2816, epoch 1, loss=0.2142)
    completed_subruns:
    - name: random_s42
      best_R@1: 0.5527
      best_val_loss: 0.4651
    - name: random_s43
      best_R@1: 0.5554
      best_val_loss: 0.4476
    - name: random_s44
      best_R@1: 0.6009
      best_val_loss: 0.4252
    - name: embedding_distance_s43
      best_R@1: 0.5655
      best_val_loss: 0.4876
    - name: embedding_distance_s44
      best_R@1: 0.5942
      best_val_loss: 0.5123
    - name: dataflow_aware_s43
      best_R@1: 0.5564
      best_val_loss: 0.5137
    remaining_subruns:
    - dataflow_aware_s44 (running)
    - bm25_s43
    - bm25_s44
    eval_pool_size: 8
    dataflow_s44_eval_500:
      R@1: 0.5701
- exp_id: plan_017_literature
  name: ''
  status: DONE
  conclusion: success
  metrics:
    papers_surveyed: 8
    citations_verified: 8
    discussion_draft: artifacts/paper_drafts/discussion_v2.md
    artifact_id: art_20260514_a2e1cd
- exp_id: plan_005_stratified
  name: ''
  status: PREPARING
  conclusion: ''
  metrics:
    confound_analysis:
      data_validity: ⚠️ R@1 值为 dry-run mock predictions，不可引用。仅分布结构（cross_tabulation.csv）有效。
      valid_findings:
        distribution_structure: rich-dataflow 99.3% 落在 large/xlarge repo，small repo
          中完全不存在
        correlation:
          dataflow_edges_vs_repo_size_pearson_r: 0.089
        cross_distribution:
          rich_in_large_xlarge_pct: 99.3
          rich_in_small: 0
          moderate_in_large_xlarge_pct: 60.9
        implication: 真实评估必须控制 pool_size 和 repo_size 来隔离 dataflow richness 独立效应
      invalid_findings: 所有 R@1/R@5/MRR 值均为 mock predictions，策略排序 pattern 不可信，禁止引用
      artifacts_path: /root/autodl-tmp/structfuse/artifacts/confound_analysis/
      valid_artifact: cross_tabulation.csv
- exp_id: plan_003_swebench_eval
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    checked_at: 2026-05-16T10:40 CST
    pid_alive: false
    eval_pid: 61328
    completion: 100/100 instances for random_s42 (normal exit)
    results_random_s42_100:
      R@1: 0.04
      R@5: 0.11
      R@10: 0.14
      R@20: 0.16
      MRR: 0.0698
      gold_coverage: 1
      n_instances: 100
      errors: 0
    bm25_baseline_300:
      R@1: 0.2733
      R@5: 0.4667
      R@10: 0.55
      R@20: 0.6467
      n_instances: 300
    note: R@1=0.04 vs BM25=0.2733. Neural retriever 在 OOD 跨 repo 场景泛化失败。
    director_decision: '2026-05-16: 放弃 SWE-bench 作为论文内容，不再重跑。外部验证改用 plan_004 RepoBench-R。'
- exp_id: unixcoder-3strat-s42
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    random_s42:
      status: DONE
      best_val_loss: 0.4513
      best_val_loss_step: 400
      best_R@1: 0.5534
      best_R@1_step: 1000
      best_R@5: 0.9772
      early_stopped_step: 1000
    embedding_distance_s42:
      status: DONE
      best_val_loss: 0.4466
      best_val_loss_step: 600
      best_R@1: 0.5497
      best_R@1_step: 600
      best_R@5: 0.9772
      early_stopped_step: 1200
    dataflow_aware_s42:
      status: DONE
      best_val_loss: 0.4628
      best_val_loss_step: 400
      best_R@1: 0.551
      best_R@1_step: 1000
      best_R@5: 0.9755
      early_stopped_step: 1000
    summary:
      R@1_range: 0.5497-0.5534 (0.37pp span)
      strategy_ranking_R@1: random > dataflow > embedding
      strategy_ranking_val_loss: embedding > random > dataflow
      finding: No meaningful strategy differentiation on UniXcoder-base (125M). All
        within noise floor.
    artifact: artifacts/unixcoder-3strat-s42/analysis.json
- exp_id: unixcoder_3strat_s42
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: qwen_random_s42_retrain
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: unixcoder-3strat-s43
  name: ''
  status: RUNNING
  conclusion: ''
  metrics:
    random_s43:
      status: DONE
      best_R@1: 0.577
      best_R@5: 0.977
      best_val_loss: 0.429
    embedding_distance_s43:
      status: RUNNING
    dataflow_aware_s43:
      status: PENDING
- exp_id: unixcoder-3strat-s44
  name: ''
  status: PREPARING
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
  "promptId": "777bb3ce-2450-4d56-bd31-860c0f6e7a8e",
  "type": "user",
  "uuid": "8c2d9aa2-e29f-4d5b-804d-a420d9d78940",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T15:25:43.134Z_

```json
{
  "parentUuid": "8c2d9aa2-e29f-4d5b-804d-a420d9d78940",
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
  "uuid": "539bc2b6-4c09-4185-b41c-c6b94883769d",
  "timestamp": "2026-05-16T15:25:43.134Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T15:25:43.134Z_

```json
{
  "parentUuid": "539bc2b6-4c09-4185-b41c-c6b94883769d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9dff2220-791d-40b3-bcb5-83f8837f6a6d",
  "timestamp": "2026-05-16T15:25:43.134Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Embedding mining effect exists but small and seed-dependent; BM25 neutral; criterion effect is main robust finding; need narrative pivot to methodology-f…",
  "leafUuid": "9dff2220-791d-40b3-bcb5-83f8837f6a6d",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict median-tier results across 9 experiment plans",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d"
}
```

---

### Assistant

_source line 8 · 2026-05-16T15:28:07.573Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, based on the "median" tier definition provided at the top. Let me carefully analyze what the median tier means and predict results for each planned experiment accordingly.

Key median tier characteristics:
- Qwen 3-seed mean embed-random Δ = +0.3–0.8pp, but 95% CI lower bound near zero or slightly includes zero
- StarCoder embed mean Δ in -0.2 to +0.3pp, not significant (s42 negative confirmed by pattern)


- BM25 shows negligible effect (Δ within ±0.5pp) — the narrative needs to pivot toward CoCoHaNeRe
- D062 checkpoint criterion emerges as the robust effect (+10–16pp), positioning it as the paper's strongest contribution
- RepoBench-R demonstrates directional consistency but confidence intervals overlap
- UniXcoder null combined with StarCoder's weak signal suggests the effect is encoder-specific rather than universal
- With only 3 seeds for sub-1pp effects, statistical power is insufficient and reviewers will likely challenge this
- The bootstrap 95% CI doesn't exclude zero
- I should reframe the narrative around checkpoint selection criterion as the dominant factor over mining strategy

Now I need to work through each planned experiment and generate predicted data accordingly. Looking at the remaining experiments to prioritize, I'm seeing which ones are still pending versus completed. From the m2_full_qwen results, I can see the performance across different random seeds and mining strategies—the embedding distance and dataflow-aware approaches are showing competitive results in the 0.55-0.59 range, with the early-stopped random seed hitting 0.6009.

Comparing across models, the Qwen results are notably stronger than StarCoder's performance in the 0.45-0.49 range, and UniXcoder's results are clustering tightly around 0.55 across different strategies, suggesting the mining approach matters less than the model choice. I'm now thinking about what's driving the s44 random seed's higher performance—whether it's the checkpoint selection criterion or something else about that particular run. Looking at s43 more closely, the difference between selecting by val_loss versus R@1 is only about 2 percentage points, which doesn't match the 10-16pp range claimed in the median tier. For s44, early stopping at step 500 achieved R@1=0.6009, suggesting the checkpoint selection criterion might have a larger effect than what I'm seeing in these individual cases—I need to understand whether the 10-16pp figure refers to a different comparison, like choosing the best checkpoint versus a fixed one. So the criterion effect is about how different checkpoint selection methods—whether by validation loss, R@1 on a small pool, fixed steps, or early stopping—can produce 10-16 percentage point differences in the final reported metric. The key insight is that selecting a checkpoint optimized for one criterion (like R@1 on pool=8) versus evaluating it on a different test set (pool=50) creates this large discrepancy.

Now I'm moving through the planned experiments to see which ones are still pending and what I'd expect to find in the median tier scenario. Most of these haven't been completed yet—things like the RepoBench-R evaluation, stratified analysis, the hop-distance ablations, training data scaling, fusion head ablation, and various other diagnostic experiments. I need to think through what the median tier would show for each of these. Looking at the actual results from the completed Qwen runs, I'm seeing the random seed baseline across three seeds averaging around 0.57, while the embedding distance variant shows modest improvements in the 0.56-0.57 range for the seeds we have data on. I need to track down whether we have the full embedding results for seed 42 to complete the comparison. Looking at the actual deltas between embed and random seeds, I see embed_s43 outperformed its random counterpart by about 1 percentage point, while embed_s44 actually underperformed by roughly 0.67 points. To figure out what embed_s42 needs to be, I'm working backwards from the target mean improvement of 0.3-0.8 percentage points across all three seeds.

Now I'm checking the m2_full_qwen registry entry to see what value was actually recorded there, since it might already have the embedding distance result I need.

Looking at the completed subruns in m2_full_qwen_continued, I can see embedding_distance_s43 hit 0.5655 and s44 reached 0.5942, while dataflow_aware_s43 came in at 0.5564. But I'm still missing embedding_distance_s42 and the dataflow_aware variants for s42 and s44, plus the BM25 results for s43 and s44 on Qwen. For StarCoder, the random seeds are tracking around 0.46-0.49, and I need to find where the embedding_s42 result landed.

Now I'm moving on to construct predictions for the median tier by mapping out what the complete dataset should look like. Let me go through the planned experiments that are either still in progress or queued—there's RepoBench-R, the stratified analysis that's currently preparing, the 1-hop versus multi-hop comparison, data size scaling, fusion head variants, dataflow-distance weighting, and failure analysis, among others.

I also need to account for the running experiments first to establish baseline numbers that the other experiments depend on, so let me start by predicting when those will finish.

Now I'm looking at the key finding from the median tier results: checkpoint selection criterion has a massive 10-16 percentage point impact, which is much larger than the mining strategy effect itself. This shifts the narrative from "mining helps" to "how you choose which checkpoint to report matters significantly." Let me examine the actual checkpoint performance across evaluation points to understand this effect properly—for instance, with the Qwen random seed 42 run, performance varies noticeably depending which checkpoint I pick, ranging from 0.533 to 0.553 across different evaluation steps. Looking at the performance numbers, I'm realizing the criterion effect might be about how checkpoint selection on a small validation pool (8 items) versus evaluation on a larger, more realistic pool (50 items) can shift which checkpoint is actually best. With only 8 items, R@1 scores get artificially inflated since ranking 1 correct out of 8 is much easier than out of 50—so the checkpoint that looks best during training might perform quite differently when evaluated at scale, potentially explaining that 10-16pp gap.

But examining the actual data, the difference between pool=8 and pool=50 is only about 2.5pp, which doesn't match. I think I need to reframe this—the real effect might be that selecting a checkpoint based on validation loss versus selecting by R@1 can produce dramatically different results when both are evaluated on the same test set.

Actually, I think I've found it. The gap comes from cherry-picking the best seed and checkpoint combination on pool=8 (like random_s44 at 0.6009) versus evaluating that same checkpoint on pool=50, which could drop to 0.44-0.46. That's the 14-16pp difference—pool=8 validation inflates the metrics significantly.

So the real insight is that evaluation methodology matters far more than mining strategy choice. The pool size effect dwarfs the <1pp differences between strategies, which means researchers need to standardize their evaluation setup before comparing approaches.

Now I'm thinking through what the planned experiments would actually show. For plan_019 specifically, which tests pool size sensitivity with the Qwen embeddings, I can predict the performance curve across different pool sizes starting from the training evaluation data I have.

The pattern is clear: as pool size increases from 8 to 500, recall drops dramatically from around 0.55 down to 0.18-0.24, with that initial jump from pool=8 to pool=50 accounting for most of the 10-14pp decline. Meanwhile, any differences between strategies stay below 1pp at each pool size.

Now I need to write out the full predictions for all the planned experiments. Let me start with the running experiments that are close to completion, like the full Qwen setup, and work through what the final metrics should look like once everything finishes.

For the embedding distance approach with seed 42, I'm predicting around 0.5585 based on the pilot results, which would put the embedding mean at 0.5727. The random baseline comes in at 0.5697, giving me about a 0.30pp advantage for embeddings—on the lower end of what I'd expect, mainly because seed 44 had an unusually strong random result.

The dataflow-aware approach is trickier. I'm predicting 0.5480 for seed 42 and around 0.5720 for seed 44 based on the current eval, which averages to 0.5588. But that gives me a -1.09pp delta against random, which feels too pessimistic for the median tier. Let me reconsider what's actually happening here. Calculating the embed_s42 values for different delta scenarios—0.5584 for +0.3pp, 0.5644 for +0.5pp, and 0.5734 for +0.8pp—so I'll use 0.5606 as a middle ground since it matches the embedding_distance_s43 R@1 value from the earlier m2_full_qwen checkpoint. Let me check the continued run to see what's actually happening there.

Looking at the m2_full_qwen_continued results, embedding_distance_s43 shows best_R@1=0.5655, so I'll set embed_s42 to 0.5613, which gives a mean of 0.5737 and a delta of +0.40pp against random—right in the expected range. Now for the dataflow metrics: s43 is at 0.5564, s44 is currently at 0.5701 with a predicted best of 0.5720, and I'm estimating s42 at 0.5510, which puts the dataflow mean around 0.5598.

That's actually a -0.99pp delta against random, which seems surprisingly negative. But looking back at the pilot data, embedding showed a +2.0pp advantage while dataflow was only +0.79pp, so in the full-scale results the effects are dampening. The dataflow signal might genuinely be weaker or even slightly negative in the median tier. The real issue here is that s44's random baseline is anomalously high at 0.6009 compared to the other seeds around 0.5527, which is skewing these comparisons. 0.5554 for s42/s43). This creates a situation where even if embedding helps on average, the seed variance (cross_seed_std_within_strategy = 1.5-3.0pp) swamps the effect.

Let me compute:
- Random: s42=0.5527, s43=0.5554, s44=0.6009 → mean=0.5697, std=2.74pp
- Embed: s42=0.5613, s43=0.5655, s44=0.5942 → mean=0.5737, std=1.81pp  
- The cross-seed std within strategy for random is 2.74pp, which is within the 1.5-3.0pp range stated in median tier.

For StarCoder, I'm checking whether the embed-random difference falls within the -0.2 to +0.3pp range. The random seeds give me a mean of 0.4787, and working through the embed estimates with the one actual value I have (s42=0.4567), I'm adjusting the other seed predictions to land the overall embed mean around 0.4762, which puts the delta at roughly -0.25pp—just slightly outside the stated bounds, so I'm refining those estimates.

Now I'm thinking about the checkpoint criterion effect, which should show a +10-16pp boost when comparing the same checkpoint across different pool sizes. The plan_019 experiment demonstrates this by evaluating on pool=8 versus pool=50, where the smaller pool shows R@1 around 0.55-0.60 and the larger pool drops to around 0.

42-0.46—a significant 10-16pp difference. This means the checkpoint selected as "best" during validation on a smaller pool might actually perform worse on a larger pool, which is a substantial finding.

Now I'm organizing which experiments are still planned versus already completed, so I can construct the full YAML with the queued and preparing experiments. Now I'm organizing the response with a structured YAML format that includes the tier classification, narrative context, and detailed predictions for each experiment with supporting rationale.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dff2220-791d-40b3-bcb5-83f8837f6a6d",
  "isSidechain": false,
  "requestId": "req_011Cb6Ur6WQmu2mvCaUoZigL",
  "type": "assistant",
  "uuid": "1c3cb7cb-5331-4767-afcc-3c8065442d74",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ke29q9HXHqPC6NFnVvCGCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23690,
      "cache_read_input_tokens": 11841,
      "output_tokens": 7674,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 7674,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23690
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

### Tool call

_source line 9 · 2026-05-16T15:28:08.200Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NtNEdPreGpVp3BAhaz76JR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/.claude/CLAUDE.md",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c3cb7cb-5331-4767-afcc-3c8065442d74",
  "isSidechain": false,
  "requestId": "req_011Cb6Ur6WQmu2mvCaUoZigL",
  "type": "assistant",
  "uuid": "58e6b0d1-5414-4153-bf1d-67a2760b7a86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ke29q9HXHqPC6NFnVvCGCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 23690,
      "cache_read_input_tokens": 11841,
      "output_tokens": 7674,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23690,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 7674,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 23690,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23690
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

### Tool result

_source line 10 · 2026-05-16T15:28:08.222Z_

<details><summary>↩ Tool result · `toolu_01NtNEdPreGpVp3BAhaz76JR`</summary>

```text
1	
2	## 输出风格
3	
4	- 回复简洁直接，不说废话
5	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
6	- 不要复述用户的问题
7	- 不要给未被要求的建议或补充说明
8	- 推理要彻底，但输出只保留结论和必要信息
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58e6b0d1-5414-4153-bf1d-67a2760b7a86",
  "isSidechain": false,
  "promptId": "777bb3ce-2450-4d56-bd31-860c0f6e7a8e",
  "type": "user",
  "uuid": "05bdc2d6-71c8-4b12-bacd-df5b7ab065d9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "58e6b0d1-5414-4153-bf1d-67a2760b7a86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Embedding mining effect exists but small and seed-dependent; BM25 neutral; criterion effect is main robust finding; need narrative pivot to methodology-f…",
  "leafUuid": "05bdc2d6-71c8-4b12-bacd-df5b7ab065d9",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict median-tier results across 9 experiment plans",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d"
}
```

---

### Tool call

_source line 13 · 2026-05-16T15:28:14.064Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RLLyaspov2qDFPhUrXvwNJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5/memory/MEMORY.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05bdc2d6-71c8-4b12-bacd-df5b7ab065d9",
  "isSidechain": false,
  "requestId": "req_011Cb6V2oEtmoQao8f8sYtxc",
  "type": "assistant",
  "uuid": "f37c32da-b876-4c9a-b569-6383221f0a90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Zje1qz1Z38DpptY46wHCn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7830,
      "cache_read_input_tokens": 35531,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7830,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 105,
          "cache_read_input_tokens": 35531,
          "cache_creation_input_tokens": 7830,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7830
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

### Tool result

_source line 14 · 2026-05-16T15:28:14.082Z_

<details><summary>↩ Tool result · reported error · `toolu_01RLLyaspov2qDFPhUrXvwNJ`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f37c32da-b876-4c9a-b569-6383221f0a90",
  "isSidechain": false,
  "promptId": "777bb3ce-2450-4d56-bd31-860c0f6e7a8e",
  "type": "user",
  "uuid": "b6b4f52f-2678-473e-9add-5cad27f8ea04",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5.",
  "sourceToolAssistantUUID": "f37c32da-b876-4c9a-b569-6383221f0a90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-16T15:33:19.563Z_

```yaml
tier: median
narrative_guidance: |
  切换到 Framing A：checkpoint selection criterion dominates mining strategy。
  主贡献重排：(1) 发现 checkpoint 选择标准对 reported performance 的影响（+10-16pp）远大于 mining strategy 差异（<1pp），
  揭示领域内 evaluation methodology 系统性问题；(2) 在此框架下，embedding mining 作为 controlled experiment 的一个 condition，
  在 Qwen 上有 marginal positive signal，但非 universal；(3) representation geometry 分析解释 why effect is encoder-dependent。
  BM25 neutral → 不能 claim CoCoHaNeRe 的 BM25 proxy 有害，改为 "mining strategy choice matters less than evaluation methodology"。
  Statistical framing：承认 3 seeds underpowered for <1pp effects，用 effect size + CI 报告而非 p-value。

imagined_experiments:
  # ============================================================
  # 已完成实验的 full-scale 最终结果预测（running → completion）
  # ============================================================

  - name: "M2 Full Qwen 完整 9-run 最终结果"
    plan_id: "plan_002 / m2_full_qwen_continued"
    description: "3 strategies × 3 seeds × Qwen2.5-Coder-3B 全量训练收敛后完整对比"
    expected_results:
      # Random
      random_s42_R@1: 0.5527
      random_s43_R@1: 0.5554
      random_s44_R@1: 0.6009
      random_mean_R@1: 0.5697
      random_std_pp: 2.74
      # Embedding distance
      embed_s42_R@1: 0.5613
      embed_s43_R@1: 0.5655
      embed_s44_R@1: 0.5942
      embed_mean_R@1: 0.5737
      embed_std_pp: 1.81
      # Dataflow aware
      dataflow_s42_R@1: 0.5510
      dataflow_s43_R@1: 0.5564
      dataflow_s44_R@1: 0.5720
      dataflow_mean_R@1: 0.5598
      dataflow_std_pp: 1.10
      # Deltas
      embed_vs_random_mean_delta_pp: 0.40
      dataflow_vs_random_mean_delta_pp: -0.99
      embed_vs_random_95CI_pp: [-0.8, 1.6]
      dataflow_vs_random_95CI_pp: [-2.2, 0.2]
      cross_seed_std_random_pp: 2.74
      bootstrap_95ci_embed_excludes_zero: false
    result_rationale: |
      s44 random 异常高（0.6009 vs s42/s43 ~0.554）导致 random mean 被拉高，embed_s44 也高但不及 random_s44，
      使得 paired delta 在 s44 上为负（-0.67pp）。s42 和 s43 embed 各高 +0.86pp 和 +1.01pp。
      三个 seed 的 delta 方差大（std≈0.9pp），3 sample 的 95% CI 宽度约 2.4pp，下界包含零。
      这是 median 档核心特征：effect exists but underpowered detection。
      Dataflow 因缺少结构数据的 instance（66% fallback to random）稀释了效果，mean slightly below random。
    tables:
      - name: "Table 1: Qwen2.5-Coder-3B R@1 (pool=8, best_by_R@1 checkpoint)"
        columns: [Strategy, s42, s43, s44, Mean, Std, "Δ vs Random"]
        rows:
          - [Random, 0.5527, 0.5554, 0.6009, 0.5697, 0.0274, "—"]
          - [Embedding, 0.5613, 0.5655, 0.5942, 0.5737, 0.0181, "+0.40pp"]
          - [Dataflow, 0.5510, 0.5564, 0.5720, 0.5598, 0.0110, "-0.99pp"]
    figures_description:
      - "Fig 1: Per-seed paired delta (embed-random) bar chart with error bars showing seed-level inconsistency"
    analysis: |
      Embed 在 2/3 seeds 上有正 delta（s42: +0.86pp, s43: +1.01pp），但 s44 为 -0.67pp。
      Mean delta +0.40pp 是 real signal 但 95% CI [-0.8, 1.6] 包含零。
      Dataflow 整体不如 random，因为 66% 的 instance 实际拿到的是 random fallback negatives。
      Cross-seed variance (2.74pp for random) >> strategy effect (0.4pp)，这是 paper pivot 到
      methodology framing 的关键数据支撑。

  - name: "M2 Full StarCoder 完整 9-run 最终结果"
    plan_id: "plan_002 / m2_full_starcoder_resumed"
    description: "3 strategies × 3 seeds × StarCoder2-3B 全量训练"
    expected_results:
      random_s42_R@1: 0.4604
      random_s43_R@1: 0.4859
      random_s44_R@1: 0.4897
      random_mean_R@1: 0.4787
      random_std_pp: 1.62
      embed_s42_R@1: 0.4567
      embed_s43_R@1: 0.4870
      embed_s44_R@1: 0.4905
      embed_mean_R@1: 0.4781
      embed_std_pp: 1.85
      dataflow_s42_R@1: 0.4490
      dataflow_s43_R@1: 0.4780
      dataflow_s44_R@1: 0.4830
      dataflow_mean_R@1: 0.4700
      dataflow_std_pp: 1.88
      embed_vs_random_mean_delta_pp: -0.06
      dataflow_vs_random_mean_delta_pp: -0.87
      embed_vs_random_95CI_pp: [-1.4, 1.3]
      bootstrap_95ci_embed_excludes_zero: false
    result_rationale: |
      StarCoder embed_s42 已确认为负（0.4567 vs random 0.4604 = -0.37pp）。
      s43/s44 embed 会 track random closely（StarCoder 有 healthy geometry，pos_sim≈0.80，
      margin 本身充足，embedding mining 提供的额外 difficulty gradient 不如 Qwen 有效）。
      Mean delta 落在 -0.2 to +0.3pp 中间偏负。Dataflow 更弱因为 StarCoder embedding space
      对 structural signal 的敏感度更低（margin 本身大，dataflow negatives 没有提供足够的 incremental difficulty）。
    tables:
      - name: "Table 2: StarCoder2-3B R@1 (pool=8, best_by_R@1 checkpoint)"
        columns: [Strategy, s42, s43, s44, Mean, Std, "Δ vs Random"]
        rows:
          - [Random, 0.4604, 0.4859, 0.4897, 0.4787, 0.0162, "—"]
          - [Embedding, 0.4567, 0.4870, 0.4905, 0.4781, 0.0185, "-0.06pp"]
          - [Dataflow, 0.4490, 0.4780, 0.4830, 0.4700, 0.0188, "-0.87pp"]
    figures_description:
      - "Fig 2: StarCoder strategy comparison — all strategies within noise floor"
    analysis: |
      StarCoder 确认 embedding mining 无效。与 Qwen 的差异来自 representation geometry：
      pos_sim=0.80 意味着 random negatives 已有足够 margin（0.194），embedding mining 的额外
      difficulty 不产生 learning signal gain。这支持 "effect is encoder-specific" 论断。

  # ============================================================
  # BM25 Baseline（plan_018 核心预测）
  # ============================================================

  - name: "BM25 Negative Baseline 训练"
    plan_id: "plan_018"
    description: "BM25-based hard negatives 作为第 4 策略，3 seeds × 2 encoders 训练对比"
    expected_results:
      # Qwen BM25
      qwen_bm25_s42_R@1: 0.5540
      qwen_bm25_s43_R@1: 0.5580
      qwen_bm25_s44_R@1: 0.5980
      qwen_bm25_mean_R@1: 0.5700
      qwen_bm25_vs_random_delta_pp: 0.03
      # StarCoder BM25
      starcoder_bm25_s42_R@1: 0.4580
      starcoder_bm25_s43_R@1: 0.4830
      starcoder_bm25_s44_R@1: 0.4870
      starcoder_bm25_mean_R@1: 0.4760
      starcoder_bm25_vs_random_delta_pp: -0.27
      # Cross-strategy
      bm25_vs_random_pooled_delta_pp: [-0.5, 0.5]
      bm25_vs_embedding_qwen_delta_pp: -0.37
    result_rationale: |
      BM25 negatives 与 random 几乎无差异。原因：BM25 top-k 与 embedding top-k 有 87.1% overlap
      （已从 phase1 overlap analysis 确认），但 BM25 ranking ≠ embedding ranking，
      实际选中的 top-7 在 medium/large repo 上 Jaccard 仅 0.30-0.38。
      BM25 选出的 negatives 在 lexical space 中是 hard 的，但不一定在 encoder embedding space 中是 hard 的。
      对于 Qwen（saturated space），BM25 negatives 的 effective difficulty 介于 random 和 embedding 之间，
      但因为 Qwen space 几乎所有 pairs 都高相似度，BM25 的 lexical-hard 不等于 embedding-hard。
      对于 StarCoder（healthy space），BM25 和 random 都落在 "sufficient margin" 区间，无差异。
      关键结论：不能 claim CoCoHaNeRe 的 BM25 方法有害。Narrative pivot to "strategy choice < methodology"。
    tables:
      - name: "Table 3: BM25 vs Other Strategies (R@1 pool=8)"
        columns: [Encoder, Random, BM25, Embedding, Dataflow]
        rows:
          - [Qwen, 0.5697, 0.5700, 0.5737, 0.5598]
          - [StarCoder, 0.4787, 0.4760, 0.4781, 0.4700]
    figures_description:
      - "Fig 3: 4-strategy comparison showing all strategies within 1pp of random — mining choice is dominated by methodology"
    analysis: |
      BM25 ≈ random 否定了原始 narrative（CoCoHaNeRe BM25 proxy harmful）。
      Paper 必须 pivot：不是 "BM25 harms" 而是 "all strategies ≈ equivalent when checkpoint criterion dominates"。
      这实际上 strengthens Framing A——如果连最 effortful 的 mining 都只有 <1pp 差异，
      那 checkpoint selection criterion (+10-16pp) 才是真正需要关注的 methodology gap。

  # ============================================================
  # Pool Size Sensitivity（plan_019 — demonstrates criterion effect）
  # ============================================================

  - name: "Pool Size Sensitivity Analysis"
    plan_id: "plan_019"
    description: "在 pool={8, 50, 100, 200, 500} 上评估策略排序稳定性"
    expected_results:
      # Qwen embed best checkpoint
      qwen_embed_pool_8_R@1: 0.5737
      qwen_embed_pool_50_R@1: 0.4320
      qwen_embed_pool_100_R@1: 0.3650
      qwen_embed_pool_200_R@1: 0.2880
      qwen_embed_pool_500_R@1: 0.1950
      # Qwen random best checkpoint
      qwen_random_pool_8_R@1: 0.5697
      qwen_random_pool_50_R@1: 0.4280
      qwen_random_pool_100_R@1: 0.3610
      qwen_random_pool_200_R@1: 0.2840
      qwen_random_pool_500_R@1: 0.1910
      # Strategy delta stability
      embed_vs_random_delta_pool_8_pp: 0.40
      embed_vs_random_delta_pool_50_pp: 0.40
      embed_vs_random_delta_pool_100_pp: 0.40
      embed_vs_random_delta_pool_200_pp: 0.40
      embed_vs_random_delta_pool_500_pp: 0.40
      # Criterion effect
      criterion_effect_pool8_vs_pool50_pp: 14.2
      criterion_effect_pool8_vs_pool100_pp: 20.9
      strategy_ranking_preserved_across_pools: true
    result_rationale: |
      Pool size 增大时 absolute R@1 急剧下降（从 pool=8 的 ~0.57 到 pool=50 的 ~0.43，drop 14pp），
      因为正确答案在更大 candidate pool 中更难排到第一。
      但 strategy delta 保持稳定（~0.4pp），因为 mining strategy 影响的是 encoder 的 relative ranking ability，
      与 pool size 无关。
      这是 paper 最强的 methodology insight：pool=8 validation 产生的 absolute R@1 数字
      在 pool=50 test 上 drop 10-16pp。如果研究者用 pool=8 选 checkpoint 再在 pool=50 报告，
      选中的 checkpoint 不一定是 pool=50 上最优的——这个 criterion mismatch 的 effect 远大于 strategy difference。
      具体而言：同一 checkpoint 在 pool=8 上 R@1=0.57 但在 pool=50 上只有 0.43，
      而另一个 checkpoint 可能 pool=8 上 R@1=0.55（被 criterion reject）但 pool=50 上 R@1=0.45（实际更好）。
      这个 +10-16pp criterion effect 就是 pool-size-driven checkpoint selection mismatch。
    tables:
      - name: "Table 4: R@1 by Pool Size (Qwen, embedding strategy, mean across seeds)"
        columns: [Pool, R@1, "Δ vs pool=8"]
        rows:
          - [8, 0.5737, "—"]
          - [50, 0.4320, "-14.2pp"]
          - [100, 0.3650, "-20.9pp"]
          - [200, 0.2880, "-28.6pp"]
          - [500, 0.1950, "-37.9pp"]
      - name: "Table 5: Strategy Δ Stability Across Pool Sizes"
        columns: [Pool, "Embed-Random Δ", "Dataflow-Random Δ", "BM25-Random Δ"]
        rows:
          - [8, "+0.40pp", "-0.99pp", "+0.03pp"]
          - [50, "+0.38pp", "-1.05pp", "+0.05pp"]
          - [100, "+0.42pp", "-0.92pp", "-0.02pp"]
          - [200, "+0.39pp", "-1.01pp", "+0.08pp"]
          - [500, "+0.41pp", "-0.98pp", "+0.01pp"]
    figures_description:
      - "Fig 4: Dual-axis plot — left: absolute R@1 drops sharply with pool size; right: strategy delta remains flat at <1pp"
      - "Fig 5: Criterion effect visualization — same checkpoint, two pool sizes, 14pp gap annotated"
    analysis: |
      Strategy ranking 在所有 pool size 下保持一致（embed > random > dataflow），但 delta < 1pp。
      绝对 R@1 随 pool 增大下降 ~14pp (pool 8→50)，这就是 "criterion effect" 的来源：
      如果用 pool=8 validation 选择 checkpoint，切换到 pool=50 test 时报告值 drop 10-16pp。
      更重要的是，pool=8 上的 "best checkpoint" 不一定是 pool=50 上的 best——
      不同 checkpoint 在不同 pool size 下的 ranking 会 shuffle。
      这是 paper 的核心方法论贡献，远比 <1pp 的 strategy delta 有实际意义。

  # ============================================================
  # D062 Checkpoint Criterion Effect 直接展示
  # ============================================================

  - name: "Checkpoint Selection Criterion Effect Analysis"
    plan_id: "plan_019 (derived)"
    description: "直接量化：不同 checkpoint 选择标准对 reported R@1 的影响"
    expected_results:
      # Same run, different checkpoint selection
      qwen_random_s42_best_by_valloss_R@1_pool50: 0.4150
      qwen_random_s42_best_by_R@1_pool8_R@1_pool50: 0.4280
      qwen_random_s42_best_by_R@1_pool50_R@1_pool50: 0.4420
      # Criterion effect magnitude
      criterion_gap_valloss_vs_R@1pool50_pp: 2.70
      criterion_gap_R@1pool8_vs_R@1pool50_pp: 1.40
      # Combined with seed effect
      best_seed_best_criterion_R@1_pool50: 0.4580
      worst_seed_worst_criterion_R@1_pool50: 0.3980
      total_methodology_range_pp: 6.0
      # vs strategy effect
      strategy_effect_max_pp: 0.40
      methodology_vs_strategy_ratio: 15.0
    result_rationale: |
      在 pool=50 evaluation 上，checkpoint criterion 差异可达 2-3pp per run。
      跨 seed 时（best seed + best criterion vs worst seed + worst criterion），总 methodology range 达 6pp。
      如果进一步考虑 pool=8 training validation 与 pool=50 test 的 mismatch（14pp absolute drop），
      以及不同 epoch 的 checkpoint 在 pool=50 上的排序变化（best pool=8 ≠ best pool=50），
      整个 "methodology confound" 量级为 10-16pp（包含 pool effect + criterion selection + seed variance）。
      相比之下，strategy effect 最大 0.4pp。ratio = 15-40x。
      这就是 paper 最强贡献：researchers 应该先解决 methodology（pool size, criterion, seed aggregation），
      再讨论 mining strategy。
    tables:
      - name: "Table 6: Methodology Confound Decomposition"
        columns: [Source, "Effect Size (pp)", Controllable]
        rows:
          - ["Pool size (8→50)", "14.2", "Yes — report on realistic pool"]
          - ["Checkpoint criterion (val_loss vs R@1)", "2.7", "Yes — use target metric"]
          - ["Seed variance", "2.7", "Partially — report mean±std"]
          - ["Mining strategy", "0.4", "Choice variable"]
          - ["Total methodology range", "10-16", "—"]
    figures_description:
      - "Fig 6: Stacked bar showing methodology effect decomposition — strategy is <5% of total variation"
    analysis: |
      这是 median 档 paper 的核心贡献。从 "mining strategy matters" 转向
      "evaluation methodology dominates, mining strategy is noise"。
      具体分解：pool size effect(14pp) > seed variance(2.7pp) > criterion(2.7pp) >> strategy(0.4pp)。
      Paper 的 prescriptive contribution：(1) 永远报告 pool=50+ 的 R@1；
      (2) 用目标 metric 选 checkpoint 而非 val_loss；(3) 报告 mean±CI 跨 seeds。

  # ============================================================
  # RepoBench-R（plan_004）
  # ============================================================

  - name: "RepoBench-R Cross-file Retrieval Evaluation"
    plan_id: "plan_004"
    description: "RepoBench-R test_easy/test_hard 上 3 strategies × 3 seeds 评估"
    expected_results:
      # test_easy (pool~6)
      qwen_random_easy_R@1_mean: 0.6820
      qwen_embed_easy_R@1_mean: 0.6870
      qwen_dataflow_easy_R@1_mean: 0.6790
      embed_vs_random_easy_delta_pp: 0.50
      embed_vs_random_easy_95CI_pp: [-0.3, 1.3]
      # test_hard (pool~18)
      qwen_random_hard_R@1_mean: 0.4150
      qwen_embed_hard_R@1_mean: 0.4190
      qwen_dataflow_hard_R@1_mean: 0.4110
      embed_vs_random_hard_delta_pp: 0.40
      embed_vs_random_hard_95CI_pp: [-0.5, 1.3]
      # StarCoder
      starcoder_random_hard_R@1_mean: 0.3580
      starcoder_embed_hard_R@1_mean: 0.3570
      starcoder_embed_vs_random_hard_delta_pp: -0.10
      # CIs overlap
      ci_overlap_easy: true
      ci_overlap_hard: true
    result_rationale: |
      RepoBench-R 是 cross-file retrieval task，与 SWE-smith 相比 domain shift 较小
      （同为 code retrieval 而非 repair），所以模型 transfer 好于 SWE-bench（OOD failure）。
      Direction 一致（Qwen embed > random）但效果量与 SWE-smith 内部评估一致（~0.4-0.5pp），
      95% CI 因为 bootstrap over 8K instances 虽然窄一些但仍包含零
      （因为 per-instance variance 大，且效果量太小）。
      StarCoder 同样 null，与 SWE-smith 结果一致。
      RepoBench-R 的主要价值是 "directional consistency" 而非 "statistical confirmation"。
    tables:
      - name: "Table 7: RepoBench-R Results (mean R@1 ± 95% CI)"
        columns: [Encoder, Split, Random, Embedding, "Δ (CI)"]
        rows:
          - ["Qwen", "easy", "0.682", "0.687", "+0.5pp (-0.3, 1.3)"]
          - ["Qwen", "hard", "0.415", "0.419", "+0.4pp (-0.5, 1.3)"]
          - ["StarCoder", "easy", "0.612", "0.611", "-0.1pp (-0.9, 0.7)"]
          - ["StarCoder", "hard", "0.358", "0.357", "-0.1pp (-1.0, 0.8)"]
    figures_description:
      - "Fig 7: RepoBench-R delta plot with CIs — directional consistency for Qwen but CIs include zero"
    analysis: |
      RepoBench-R 作为 supplementary validation 支持 directional claim 但不提供 statistical significance。
      在 median 档的 methodology-first framing 下，这反而 reinforces 主论点：
      <1pp effects 即使 directionally consistent 也无法在 standard evaluation 中 reliably detect。

  # ============================================================
  # Temperature Ablation（plan_021 reduced scope）
  # ============================================================

  - name: "Temperature Ablation Reduced"
    plan_id: "plan_021"
    description: "τ ∈ {0.05, 0.2} × random+embedding × Qwen × seed 42"
    expected_results:
      # τ=0.05 (very sharp)
      tau005_random_R@1: 0.5350
      tau005_embed_R@1: 0.5410
      tau005_embed_vs_random_pp: 0.60
      # τ=0.1 (current default)
      tau010_random_R@1: 0.5527
      tau010_embed_R@1: 0.5613
      tau010_embed_vs_random_pp: 0.86
      # τ=0.2 (softer)
      tau020_random_R@1: 0.5680
      tau020_embed_R@1: 0.5700
      tau020_embed_vs_random_pp: 0.20
      # Regime specificity
      strategy_ranking_preserved: true
      delta_magnitude_varies: true
      tau005_vs_tau010_absolute_gap_pp: 1.77
      tau020_vs_tau010_absolute_gap_pp: 1.53
    result_rationale: |
      τ=0.05 使 loss landscape 更 sharp，对 hard negatives 更 sensitive——理论上应放大 mining effect。
      实际上 τ=0.05 更容易 overfit（已在 pilot 中观察到），absolute R@1 略低于 τ=0.10。
      但 embed-random delta 在 τ=0.05 下 slightly larger（0.6pp vs 0.86pp... 实际上更小）。
      τ=0.20 使 contrastive loss 更 smooth，random 和 embed 差异缩小（0.2pp），
      因为 softer temperature 减少了 hard negative 的 informative gradient signal。
      关键结论：strategy ranking 在所有 τ 下保持（embed ≥ random），但 effect magnitude 与 τ 相关。
      这意味着 mining effect 不是 regime-specific artifact，但其 practical significance 受 τ 调制。
      对 methodology framing：τ 选择（absolute R@1 vary ~2pp across τ）也是一个 methodology confound，
      量级仍 > strategy effect（0.2-0.9pp）。
    tables:
      - name: "Table 8: Temperature × Strategy Interaction (Qwen, s42)"
        columns: [τ, "Random R@1", "Embed R@1", "Δ (pp)"]
        rows:
          - [0.05, 0.5350, 0.5410, "+0.60"]
          - [0.10, 0.5527, 0.5613, "+0.86"]
          - [0.20, 0.5680, 0.5700, "+0.20"]
    figures_description:
      - "Fig 8: Temperature effect on absolute R@1 (~2pp range) vs strategy effect (<1pp) — another methodology factor"
    analysis: |
      Embed advantage 在所有 τ 下存在但 magnitude 随 τ 变化。这 rules out "effect is τ=0.1 artifact"。
      同时也展示了 τ 是另一个 methodology confound（2pp range），再次支持 criterion-dominates framing。

  # ============================================================
  # Dynamic Mining（plan_015）
  # ============================================================

  - name: "Dynamic Embedding Mining Baseline"
    plan_id: "plan_015"
    description: "每 epoch 重新 mine embedding negatives vs 只用 pretrained（static）"
    expected_results:
      qwen_static_embed_R@1: 0.5613
      qwen_dynamic_embed_R@1: 0.5640
      dynamic_vs_static_delta_pp: 0.27
      starcoder_static_embed_R@1: 0.4567
      starcoder_dynamic_embed_R@1: 0.4590
      dynamic_vs_static_sc_delta_pp: 0.23
      dynamic_overhead_factor: 3.2
    result_rationale: |
      Dynamic mining 理论上应 better 因为 negatives adapt to evolving encoder。
      但实际提升微小（~0.2-0.3pp）因为：(1) LoRA 只 fine-tune adapter，base embedding 变化小；
      (2) 3 epochs 太短，encoder drift 有限；(3) Qwen saturated space 意味着 re-mining 后
      top-k negatives 几乎不变（cos sim 都在 0.96+ 区间，ranking 高度稳定）。
      训练时间 3.2x（每 epoch 需要重新 encode 全 corpus + mine），ROI 极低。
      结论：static mining 是合理 baseline，dynamic 不是 confound。
    tables:
      - name: "Table 9: Static vs Dynamic Mining"
        columns: [Encoder, Static, Dynamic, "Δ (pp)", "Time multiplier"]
        rows:
          - [Qwen, 0.5613, 0.5640, "+0.27", "3.2x"]
          - [StarCoder, 0.4567, 0.4590, "+0.23", "3.2x"]
    figures_description:
      - "Fig 9: Negligible dynamic benefit — validates static mining as non-confounded baseline"
    analysis: |
      Dynamic mining 仅提供 ~0.25pp marginal gain over static，且 computational cost 3.2x。
      This validates that static mining is a fair comparison point（reviewer concern addressed）。
      Also supports narrative：even "better" mining only adds 0.25pp → methodology still dominates。

  # ============================================================
  # UniXcoder Multi-seed（plan_020）
  # ============================================================

  - name: "UniXcoder Multi-seed Validation"
    plan_id: "plan_020"
    description: "UniXcoder-base 125M 上 3 strategies × 3 seeds 统计验证"
    expected_results:
      # s42 (actual)
      unixcoder_random_s42_R@1: 0.5534
      unixcoder_embed_s42_R@1: 0.5497
      unixcoder_dataflow_s42_R@1: 0.5510
      # s43 predictions
      unixcoder_random_s43_R@1: 0.5770
      unixcoder_embed_s43_R@1: 0.5740
      unixcoder_dataflow_s43_R@1: 0.5755
      # s44 predictions
      unixcoder_random_s44_R@1: 0.5620
      unixcoder_embed_s44_R@1: 0.5590
      unixcoder_dataflow_s44_R@1: 0.5600
      # Means
      unixcoder_random_mean_R@1: 0.5641
      unixcoder_embed_mean_R@1: 0.5609
      unixcoder_dataflow_mean_R@1: 0.5622
      embed_vs_random_mean_pp: -0.32
      dataflow_vs_random_mean_pp: -0.19
      all_within_noise: true
      max_span_across_strategies_pp: 0.37
    result_rationale: |
      UniXcoder s42 已确认 null result（0.37pp span across all strategies）。
      Multi-seed 会重复这个 pattern：UniXcoder 作为 encoder-only 125M model，
      其 representation 是 mean-pooled 而非 last-token，embedding space 结构与 decoder-only 不同。
      Mining strategy 对 encoder-only architecture 完全无效的原因：
      (1) 125M params 的 adapter 容量有限，hard negatives 的额外 gradient 无法被 absorbed；
      (2) encoder-only mean-pooling 产生的 similarity distribution 不同于 decoder last-token，
      mining 不 align with the model's actual difficulty gradient。
      这个 null result 在 paper 中不再是 limitation 而是 positive evidence：
      "effect is encoder-specific, confirming geometry hypothesis"。
    tables:
      - name: "Table 10: UniXcoder-base Results (complete null)"
        columns: [Seed, Random, Embed, Dataflow, "Max Span"]
        rows:
          - [42, 0.5534, 0.5497, 0.5510, "0.37pp"]
          - [43, 0.5770, 0.5740, 0.5755, "0.30pp"]
          - [44, 0.5620, 0.5590, 0.5600, "0.30pp"]
          - [Mean, 0.5641, 0.5609, 0.5622, "0.32pp"]
    figures_description:
      - "Fig 10: UniXcoder — flat lines across strategies, contrasted with Qwen's marginal slope"
    analysis: |
      UniXcoder null + StarCoder weak = 'effect is encoder-specific, not universal'。
      在 methodology-first framing 下，这反而 strengthens 论文：即使最 favorable 的条件
      （Qwen saturated geometry）也只有 <1pp effect，其他 architecture 完全 null。
      Mining strategy choice 在 typical evaluation 中完全不 matter。

  # ============================================================
  # Stratified Analysis（plan_005）
  # ============================================================

  - name: "Stratified Analysis by Structural Data Availability"
    plan_id: "plan_005"
    description: "5 strata 分析：repo size, pool size, query-pos similarity, structural data availability, neg_difficulty quartile"
    expected_results:
      # Stratum 1: structural data available (34%)
      rich_dataflow_embed_vs_random_delta_pp: 0.55
      # Stratum 2: fallback (66%)
      fallback_embed_vs_random_delta_pp: 0.30
      # Confound
      rich_dataflow_99pct_in_large_repos: true
      cannot_isolate_dataflow_from_repo_size: true
      # Pool size strata
      small_pool_lt20_delta_pp: 0.60
      large_pool_gt100_delta_pp: 0.35
      # neg_difficulty quartile
      q1_low_difficulty_delta_pp: 0.15
      q4_high_difficulty_delta_pp: 0.70
      # Overall pattern
      difficulty_gradient_predicts_benefit: true
      but_all_effects_within_ci_noise: true
    result_rationale: |
      Stratified analysis 会显示 directional patterns：
      (1) Rich-dataflow instances（34%）show slightly larger embed benefit because these instances 
          tend to be in complex repos where random negatives are worse-quality；
      (2) 但 99.3% rich-dataflow 在 large/xlarge repos，无法解耦 dataflow richness 和 repo complexity；
      (3) neg_difficulty quartile 最有解释力：high-difficulty negatives（Q4）对应更大的 embed benefit，
          因为 embed mining 选出的 negatives 比 random 更接近 difficulty optimal zone；
      (4) 所有 strata 的 effect 都在 noise floor 内（CI 包含 zero）。
      这支持 geometry hypothesis 但不能作为 statistical evidence。
    tables:
      - name: "Table 11: Stratified embed-random Δ (Qwen, all seeds pooled)"
        columns: [Stratum, N, "Δ (pp)", "95% CI"]
        rows:
          - ["Rich dataflow (34%)", "~4800", "+0.55", "(-0.4, 1.5)"]
          - ["Fallback (66%)", "~9300", "+0.30", "(-0.5, 1.1)"]
          - ["Small repo (<50 files)", "~500", "+0.80", "(-1.5, 3.1)"]
          - ["Large repo (200+ files)", "~8600", "+0.35", "(-0.5, 1.2)"]
          - ["neg_difficulty Q1 (easy)", "~3500", "+0.15", "(-0.8, 1.1)"]
          - ["neg_difficulty Q4 (hard)", "~3500", "+0.70", "(-0.3, 1.7)"]
    figures_description:
      - "Fig 11: Stratified delta forest plot — all CIs include zero but directional pattern visible"
      - "Fig 12: neg_difficulty quartile × strategy interaction — monotonic trend supports geometry hypothesis"
    analysis: |
      Stratified analysis 提供 mechanistic depth 但无 statistical power。
      在 median 档 framing 中作为 "exploratory evidence for geometry hypothesis"。
      关键 insight：confound between repo_size 和 dataflow_richness 意味着
      不能单独 attribute benefit to structural information。

  # ============================================================
  # Hop Ablation（plan_007）
  # ============================================================

  - name: "1-hop vs 2-hop vs 3-hop Call-graph Bounding"
    plan_id: "plan_007"
    description: "CodeQL 提取时 data-flow scope 对 connected set 大小和 downstream training 的影响"
    expected_results:
      # Connected set statistics
      hop1_connected_mean_files: 3.2
      hop2_connected_mean_files: 8.7
      hop3_connected_mean_files: 18.4
      # Z% (connected-not-gold)
      hop1_Z_pct: 0.52
      hop2_Z_pct: 0.78
      hop3_Z_pct: 0.89
      # Training impact (Qwen, s42)
      hop1_dataflow_R@1: 0.5480
      hop2_dataflow_R@1: 0.5510
      hop3_dataflow_R@1: 0.5490
      hop_effect_range_pp: 0.30
    result_rationale: |
      增加 hop 数扩大 connected set（从 3.2 到 18.4 mean files），增加 Z%，
      但 downstream training 差异极小（0.3pp range）。原因：
      (1) Dataflow strategy 本身效果已经 ≈ random（median 档 dataflow-random ≈ -1pp），
          所以 connected set 的精确度差异被掩盖；
      (2) 更多 hops 包含更多 spurious connections（transitive dependencies 不等于 semantic relatedness），
          noise 抵消了 coverage gain；
      (3) 在 2-hop（当前设置）下 Z%=78% 已经 adequate——大部分 true positives 已被 captured。
    tables:
      - name: "Table 12: Hop Depth Ablation"
        columns: [Hops, "Mean connected files", "Z%", "Dataflow R@1"]
        rows:
          - [1, 3.2, "52%", 0.5480]
          - [2, 8.7, "78%", 0.5510]
          - [3, 18.4, "89%", 0.5490]
    figures_description:
      - "Fig 13: Hop depth vs connected set size (log scale) — diminishing returns past 2-hop"
    analysis: |
      2-hop 是合理 default（coverage/noise trade-off），但 choice of hop depth
      对 downstream training 几乎无影响。又一个 methodology variant (hop depth) 
      whose effect << criterion effect。

  # ============================================================
  # Training Data Size Scaling（plan_008）
  # ============================================================

  - name: "Training Data Size Scaling"
    plan_id: "plan_008"
    description: "1K vs 3K vs 5K vs 11K+ instances 的 scaling 行为"
    expected_results:
      # Qwen random s42
      size_1K_R@1: 0.5050
      size_3K_R@1: 0.5310
      size_5K_R@1: 0.5430
      size_11K_R@1: 0.5527
      # Embed-random delta at each size
      size_1K_embed_delta_pp: 1.20
      size_3K_embed_delta_pp: 0.80
      size_5K_embed_delta_pp: 0.55
      size_11K_embed_delta_pp: 0.86
      # Scaling law
      random_scaling_log_slope: 0.023
      effect_diminishes_with_data: true
    result_rationale: |
      更多数据提升 absolute performance（log-linear scaling），但同时 diminishes mining advantage。
      原因：larger random corpus 本身 covers 更多 hard negatives by chance，
      reducing the marginal value of targeted mining。
      At 1K，random sampling 的 coverage 差，mining 的相对优势大（+1.2pp）；
      at 11K，random 已经 sample 了 enough hard examples that mining only adds +0.86pp。
      这解释了为何 full-scale effect < pilot effect（pilot 用较小数据集）。
      在 methodology framing 中：data size（5pp range from 1K→11K）是又一个 >> strategy effect 的 factor。
    tables:
      - name: "Table 13: Data Size Scaling"
        columns: [Size, "Random R@1", "Embed R@1", "Δ (pp)"]
        rows:
          - ["1K", 0.505, 0.517, "+1.20"]
          - ["3K", 0.531, 0.539, "+0.80"]
          - ["5K", 0.543, 0.548, "+0.55"]
          - ["11K", 0.553, 0.561, "+0.86"]
    figures_description:
      - "Fig 14: Log-linear scaling curves for random and embed — converging at larger data sizes"
    analysis: |
      Data size effect (5pp) >> strategy effect (<1pp)。Mining advantage diminishes with more data，
      suggesting that at even larger scale the effect may vanish entirely。
      11K 的 delta 略回弹（0.86 > 0.55 at 5K）可能是 noise 或 composition effect（
      更多 instances 中包含更多 hard cases where mining helps）。

  # ============================================================
  # Bootstrap CI for Final Claims（plan_016 adapted）
  # ============================================================

  - name: "Bootstrap 95% CI for All Claims"
    plan_id: "plan_016 (adapted from SWE-bench to main results)"
    description: "对 SWE-smith validation 上的 strategy comparisons 做 bootstrap CI（SWE-bench 已放弃）"
    expected_results:
      # Qwen embed vs random
      qwen_embed_vs_random_bootstrap_mean_pp: 0.40
      qwen_embed_vs_random_bootstrap_95CI_pp: [-0.82, 1.62]
      qwen_embed_vs_random_p_value: 0.26
      ci_excludes_zero: false
      # Qwen dataflow vs random
      qwen_dataflow_vs_random_bootstrap_mean_pp: -0.99
      qwen_dataflow_vs_random_bootstrap_95CI_pp: [-2.45, 0.47]
      # StarCoder embed vs random
      starcoder_embed_vs_random_bootstrap_mean_pp: -0.06
      starcoder_embed_vs_random_bootstrap_95CI_pp: [-1.52, 1.40]
      # BM25 vs random (pooled)
      bm25_vs_random_bootstrap_mean_pp: -0.12
      bm25_vs_random_bootstrap_95CI_pp: [-1.20, 0.96]
      # Effect sizes
      qwen_embed_cohens_d: 0.18
      starcoder_embed_cohens_d: 0.03
      power_analysis_required_seeds_for_05pp: 12
    result_rationale: |
      With only 3 seeds per condition, 95% CI is approximately mean ± t(0.025, df=2) × SE。
      For cross_seed_std = 2.7pp and n=3：SE = 2.7/√3 = 1.56pp, t(0.025,2)=4.3 → CI = ±6.7pp... 
      这太宽了。实际上 bootstrap CI 用的是 paired delta（each seed 的 embed - random），
      paired delta std 更小（~1.0pp因为 seeds co-vary）。
      Paired delta: s42=+0.86, s43=+1.01, s44=-0.67 → mean=0.40, std=0.93, SE=0.54。
      95% CI (bootstrap percentile) ≈ [-0.82, 1.62]，包含零。
      Cohen's d = 0.40/2.2 = 0.18（small effect）。
      Power analysis：要 detect 0.5pp effect with 80% power at α=0.05，需要 ~12 seeds。
      3 seeds 的 statistical power 对 <1pp effect 约为 15-20%，underpowered。
    tables:
      - name: "Table 14: Statistical Summary (all comparisons)"
        columns: [Comparison, "Mean Δ (pp)", "95% CI", "Cohen's d", "p-value"]
        rows:
          - ["Qwen Embed-Random", "+0.40", "(-0.82, 1.62)", "0.18", "0.26"]
          - ["Qwen Dataflow-Random", "-0.99", "(-2.45, 0.47)", "0.42", "0.12"]
          - ["StarCoder Embed-Random", "-0.06", "(-1.52, 1.40)", "0.03", "0.94"]
          - ["BM25-Random (pooled)", "-0.12", "(-1.20, 0.96)", "0.05", "0.82"]
    figures_description:
      - "Fig 15: Forest plot of all strategy comparisons with 95% CIs — none exclude zero"
      - "Fig 16: Power curve showing 3 seeds gives ~18% power for 0.5pp detection"
    analysis: |
      所有 CI 都包含零。这不意味着 effect 不存在，而是 3 seeds 对 <1pp effects 统计力度不足。
      Paper 的 honest framing：report effect sizes + CIs，承认 underpowered，
      argue that the FINDING is "methodology matters more" not "mining helps"。

  # ============================================================
  # Fusion Head Ablation（plan_009）
  # ============================================================

  - name: "Fusion Head Ablation"
    plan_id: "plan_009"
    description: "embedding-only vs structural-features-only vs combined retrieval"
    expected_results:
      embedding_only_R@1: 0.5613
      structural_only_R@1: 0.3200
      combined_R@1: 0.5650
      combined_vs_embed_delta_pp: 0.37
    result_rationale: |
      Structural features alone（graph-based without neural embedding）表现差
      因为 coverage 只有 34%（66% instances 无 structural data → random guess）。
      Combined（embedding + structural re-rank）marginal gain over embedding-only（+0.37pp）
      因为 structural signal 只在 34% instances 上有效，且其信号与 embedding 高度相关
      （connected files 通常也是 embedding-similar files，overlap 87%）。
      这进一步支持 "mining strategy 差异小" 的 narrative。
    tables:
      - name: "Table 15: Fusion Head Ablation"
        columns: [Method, "R@1", Coverage]
        rows:
          - ["Embedding only", 0.5613, "100%"]
          - ["Structural only", 0.3200, "34% effective"]
          - ["Combined", 0.5650, "100%"]
    figures_description: []
    analysis: |
      Structural signal alone insufficient due to coverage gap。
      Combined 仅 marginal gain，reinforcing that embedding-based retrieval
      captures most of what structural information provides。

  # ============================================================
  # Dataflow-distance Weighted（plan_010）
  # ============================================================

  - name: "Dataflow-distance Weighted Negatives"
    plan_id: "plan_010"
    description: "按 dataflow distance 连续加权 vs 二值 connected/disconnected"
    expected_results:
      binary_dataflow_R@1: 0.5510
      weighted_dataflow_R@1: 0.5530
      weighted_vs_binary_delta_pp: 0.20
    result_rationale: |
      Connected/disconnected 二值划分已经 capture 了 structural signal 的主要信息量。
      连续权重（distance = 1 vs 2 vs 3 hops）只提供 marginal refinement（+0.2pp），
      因为 (1) distance distribution 本身 noisy（CodeQL 的 hop count 不是 clean metric），
      (2) 二值判断（is_connected）在 linear proxy 中已是 top feature (+2.82 coefficient），
      graded distance 的 incremental information content 有限。
    tables: []
    figures_description: []
    analysis: |
      Minimal improvement over binary。Further confirms that structural signal
      is coarse-grained (connected vs not) rather than fine-grained (distance-weighted).

  # ============================================================
  # Failure Analysis（plan_011）
  # ============================================================

  - name: "Failure Analysis on SWE-bench Failures"
    plan_id: "plan_011"
    description: "50 BM25 baseline failures 分类分析"
    expected_results:
      total_analyzed: 50
      category_cross_repo_import: 12
      category_test_only_change: 15
      category_distant_dependency: 8
      category_config_files: 7
      category_other: 8
      dataflow_could_help_pct: 16
      dataflow_irrelevant_pct: 72
      dataflow_would_hurt_pct: 12
    result_rationale: |
      SWE-bench 的 R@1=0.04 failure 主要来自 OOD 问题（不同 repo 分布），
      而非 mining strategy 不足。分析 50 个 BM25 failure case：
      大多数是 test file changes（30%）和 cross-repo import patterns（24%）——
      这些情况下 dataflow mining 无法帮助，因为 (1) test files 通常不在 dataflow graph 中，
      (2) SWE-bench 的 repo 不在训练集中。
      只有 ~16% cases 理论上 dataflow 可以帮助（distant dependency chains）。
      这 reinforces director decision to drop SWE-bench from paper。
    tables:
      - name: "Table 16: Failure Case Taxonomy"
        columns: [Category, Count, "Dataflow relevance"]
        rows:
          - ["Test-only changes", 15, "Irrelevant"]
          - ["Cross-repo import", 12, "Irrelevant"]
          - ["Distant dependency", 8, "Could help"]
          - ["Config/build files", 7, "Irrelevant"]
          - ["Other", 8, "Mixed"]
    figures_description: []
    analysis: |
      SWE-bench failure is OOD generalization problem, not mining strategy problem。
      Confirms paper should not mention SWE-bench。RepoBench-R is better external validation。

  # ============================================================
  # Qualitative Examples（plan_012）
  # ============================================================

  - name: "Qualitative Retrieval Examples"
    plan_id: "plan_012"
    description: "5-10 cases where embedding mining changed retrieval outcome vs random"
    expected_results:
      total_diff_cases_found: 23
      selected_for_paper: 5
      pattern_A_embed_promotes_import_chain: 2
      pattern_B_embed_demotes_unrelated_similar: 2
      pattern_C_marginal_reranking: 1
      avg_rank_change_in_selected: 3.2
    result_rationale: |
      由于 overall delta 只有 ~0.4pp (pool=8)，找到 embed mining 改变 R@1 outcome 的
      cases 需要 search relatively large eval set。在 ~1400 instances 中，
      约 23 cases 的 top-1 因 strategy 不同而变化（1.6% cases）。
      选出的 5 cases 展示 3 个 pattern：
      (1) Embed mining 正确将 import-chain neighbor 排到 top（2 cases）；
      (2) Embed mining 正确降低了 lexically similar but unrelated files（2 cases）；
      (3) Marginal re-ranking where embed barely wins（1 case）。
      Avg rank change 只有 3.2 positions（不是 dramatic re-ordering）。
      Qualitative 支持 directional argument 但 quantitative impact is small。
    tables: []
    figures_description:
      - "Fig 17: 2-3 cherry-picked examples showing embed mining vs random retrieval outcome difference"
    analysis: |
      Qualitative examples 提供 intuition 但数量少（only 1.6% instances affected）。
      在 paper 中作为 "illustrative" 而非 "representative"。

  # ============================================================
  # Full Temperature Ablation（plan_014 — if time allows）
  # ============================================================

  - name: "Full Temperature Ablation"
    plan_id: "plan_014"
    description: "τ ∈ {0.05, 0.1, 0.2} × all 3 strategies × 2 encoders"
    expected_results:
      # Qwen
      qwen_tau005_random_R@1: 0.5350
      qwen_tau005_embed_R@1: 0.5410
      qwen_tau005_dataflow_R@1: 0.5300
      qwen_tau020_random_R@1: 0.5680
      qwen_tau020_embed_R@1: 0.5700
      qwen_tau020_dataflow_R@1: 0.5650
      # StarCoder
      starcoder_tau005_random_R@1: 0.4350
      starcoder_tau005_embed_R@1: 0.4340
      starcoder_tau020_random_R@1: 0.4900
      starcoder_tau020_embed_R@1: 0.4890
      # Key findings
      tau_effect_on_absolute_R@1_pp: 3.3
      tau_effect_on_strategy_delta: "preserves ranking but modulates magnitude"
      strategy_ranking_invariant_to_tau: true
    result_rationale: |
      Full ablation extends plan_021 to StarCoder and dataflow。
      StarCoder 在所有 τ 下保持 null（embed ≈ random），因为 geometry effect 与 τ 独立。
      τ 对 absolute R@1 的影响（~3.3pp across Qwen）是 yet another methodology confound。
      Strategy ranking invariant confirms mining effect is real (if small) but regime-independent。
    tables:
      - name: "Table 17: Full τ × Strategy × Encoder Grid"
        columns: [Encoder, τ, Random, Embed, Dataflow, "Embed-Random Δ"]
        rows:
          - [Qwen, 0.05, 0.535, 0.541, 0.530, "+0.60pp"]
          - [Qwen, 0.10, 0.553, 0.561, 0.551, "+0.86pp"]
          - [Qwen, 0.20, 0.568, 0.570, 0.565, "+0.20pp"]
          - [StarCoder, 0.05, 0.435, 0.434, 0.430, "-0.10pp"]
          - [StarCoder, 0.10, 0.460, 0.457, 0.449, "-0.37pp"]
          - [StarCoder, 0.20, 0.490, 0.489, 0.485, "-0.10pp"]
    figures_description:
      - "Fig 18: Heatmap of R@1 across τ × strategy × encoder — shows τ dominates"
    analysis: |
      τ effect (3.3pp) is another methodology confound >> strategy effect。
      Strategy ranking consistent across τ but magnitude varies → not a τ-specific artifact。

  # ============================================================
  # Completed running experiments final prediction
  # ============================================================

  - name: "UniXcoder 3-strat s43 Completion"
    plan_id: "plan_020 (partial)"
    description: "UniXcoder s43 embedding + dataflow 完成"
    expected_results:
      embed_s43_R@1: 0.5740
      dataflow_s43_R@1: 0.5755
      random_s43_R@1: 0.5770
      max_span_pp: 0.30
      confirms_null: true
    result_rationale: |
      s43 random 已完成（0.577）。Embed 和 dataflow 会在 ±0.3pp 内。
      UniXcoder 125M encoder-only 对 mining strategy 完全不敏感，
      multi-seed 只是 confirm s42 的 null with more confidence。
    tables: []
    figures_description: []
    analysis: "Confirms UniXcoder null. 3-encoder evidence: Qwen marginal, StarCoder null, UniXcoder null."

  # ============================================================
  # Summary: Criterion Effect as Paper Core
  # ============================================================

  - name: "D062 综合 Criterion Effect 验证"
    plan_id: "derived from plan_019 + plan_021 + full results"
    description: "综合所有实验量化 checkpoint criterion effect vs mining strategy effect"
    expected_results:
      methodology_factors:
        pool_size_effect_pp: 14.2
        temperature_effect_pp: 3.3
        seed_variance_pp: 2.7
        checkpoint_criterion_pp: 2.7
        data_size_effect_5x_pp: 4.8
        total_methodology_range_pp: 16.0
      strategy_factors:
        best_mining_strategy_effect_pp: 0.40
        strategy_as_pct_of_methodology: 2.5
      paper_framing_support:
        ratio_methodology_to_strategy: 40
        claim_strength: "Strong — criterion effect is 40× larger than best strategy effect"
        narrative: "Evaluation methodology (pool size, criterion, seed, τ) accounts for >95% of variance in reported results. Mining strategy choice is a rounding error."
    result_rationale: |
      汇总所有 methodology confounds：pool_size(14pp) + τ(3.3pp) + seed(2.7pp) + criterion(2.7pp) + data_size(4.8pp)。
      总 methodology range 约 16pp（不是简单加法，因为有重叠和 interaction），
      而 best mining strategy effect = 0.4pp。
      这是 paper 的核心贡献：发现 evaluation methodology 的系统性问题，
      mining strategy 的 reported effects 在文献中可能 largely driven by methodology choices 而非 true signal。
      这解释了为何 prior work 有 contradictory findings（不同 papers 用不同 pool sizes, τ, criterion）。
      Prescriptive contribution：建议 community 标准化 evaluation protocol。
    tables:
      - name: "Table 18: Methodology Confound Summary (Paper Core Contribution)"
        columns: [Factor, "Effect Range (pp)", "vs Strategy δ (0.4pp)"]
        rows:
          - ["Evaluation pool size (8→50)", "14.2", "35×"]
          - ["Training data size (1K→11K)", "4.8", "12×"]
          - ["Temperature (0.05→0.20)", "3.3", "8×"]
          - ["Seed variance (within strategy)", "2.7", "7×"]
          - ["Checkpoint criterion (loss vs R@1)", "2.7", "7×"]
          - ["Mining strategy (best case)", "0.4", "1×"]
    figures_description:
      - "Fig 19 (Paper Hero Figure): Bar chart showing methodology factors dwarfing strategy effect — visual argument for paper's thesis"
    analysis: |
      这是 median 档 paper 最终形态的核心数据。叙事从 "embedding mining helps code retrieval"
      转变为 "evaluation methodology choices dominate mining strategy effects by 40×—
      the field needs standardized evaluation protocols before claiming mining improvements"。
      Claims 重排：(1) methodology dominance (+10-16pp vs <1pp), (2) within controlled methodology
      embedding shows conditional marginal benefit on saturated-geometry encoders, (3) geometry analysis
      explains encoder-specificity。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6b4f52f-2678-473e-9add-5cad27f8ea04",
  "isSidechain": false,
  "requestId": "req_011Cb6V3Es1bMZaBdhtPK8jZ",
  "type": "assistant",
  "uuid": "92d6c2be-2100-4cbc-9243-cdd8623a2f01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0134pHwmLqZib8CAbYosNoLA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 156,
      "cache_read_input_tokens": 43361,
      "output_tokens": 16530,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 156,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16530,
          "cache_read_input_tokens": 43361,
          "cache_creation_input_tokens": 156,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 156
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

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Embedding mining effect exists but small and seed-dependent; BM25 neutral; criterion effect is main robust finding; need narrative pivot to methodology-f…",
  "leafUuid": "92d6c2be-2100-4cbc-9243-cdd8623a2f01",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict median-tier results across 9 experiment plans",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Embedding mining effect exists but small and seed-dependent; BM25 neutral; criterion effect is main robust finding; need narrative pivot to methodology-f…",
  "leafUuid": "92d6c2be-2100-4cbc-9243-cdd8623a2f01",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict median-tier results across 9 experiment plans",
  "sessionId": "02311cec-ed3a-4d41-9228-47b60120947d"
}
```

---
