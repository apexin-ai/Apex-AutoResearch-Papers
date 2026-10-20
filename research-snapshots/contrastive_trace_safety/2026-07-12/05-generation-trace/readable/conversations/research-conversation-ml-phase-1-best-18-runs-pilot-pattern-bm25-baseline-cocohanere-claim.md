# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：全 18 runs 复现 pilot pattern，BM25 baseline 关闭 CoCoHaNeRe 论证，三条 claim 原样成立 核心假设

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/c009ff0c-5981-45ce-bb65-8ec7bd54e72e.jsonl`
- **Structured JSON:** [`eb836d521eb03905af24.json`](../../sessions/eb/eb836d521eb03905af24.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T16:26:59.610Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T16:26:59.610Z",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：全 18 runs 复现 pilot pattern，BM25 baseline 关闭 CoCoHaNeRe 论证，三条 claim 原样成立\n核心假设：['embedding-random R@1 delta 在两个 encoder 上 95% CI 下界 > 0', 'dataflow-random R@1 delta 在 Qwen 上 CI 下界 > 0，StarCoder 上 ≤ 0（条件性成立）', 'BM25 negatives 明确 harm（vs random delta 显著为负），实证关闭 CoCoHaNeRe proxy 论证', 'pool size 50→500 策略排名不翻转', 'SWE-bench Lite 下游 resolve rate 有可见提升']\n关键指标范围：{'qwen_emb_minus_random_R1_pp': [1.5, 2.5], 'starcoder_emb_minus_random_R1_pp': [1.0, 2.0], 'qwen_df_minus_random_R1_pp': [0.5, 1.5], 'starcoder_df_minus_random_R1_pp': [-1.0, 0.3], 'bm25_minus_random_R1_pp': [-4.0, -1.5], 'swebench_resolve_rate_delta_pp': [1.5, 4.0], 'repobench_R1_delta_pp': [1.0, 3.0], 'pool_ranking_stable_pct': [75, 100], 'bootstrap_CI_width_R1_pp': [0.5, 2.0], 'qwen_mean_R1_absolute': [0.53, 0.58], 'starcoder_mean_R1_absolute': [0.44, 0.5]}\n叙事方向：原始 framing 完全成立。Claim 1（embedding mining 纠正 misconception）有 BM25 baseline 实证支撑 + 两 encoder 统计显著。Claim 2（dataflow 条件性获益）由 Qwen/StarCoder 对比 + neg_difficulty margin 分析 + representation saturation 机制完整闭环。Claim 3 作为 supporting methodology 无需额外论证。标题可用 \"Correcting Misconceptions\" 强 framing， SWE-bench 数据作为 downstream validation 加固 practical relevance。EMNLP Main 强投。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: structfuse-context\nfocus: D030 修复后验证：新增 plan_018 BM25 baseline（关闭 CoCoHaNeRe correction 论证）、plan_019 pool size sensitivity、plan_004 多 seed CIs、plan_005 structural coverage 分层 + neg_difficulty quartile。Framing 修正：N=2 降级为 observation、Claim 3 降为 supporting methodology、StarCoder decoder-only。Reviewers 应重点评估：(1) BM25 baseline 是否关闭了上一轮最大缺口，(2) 新增实验是否充分回应了上一轮 median/worst 的 \"related work insufficient\" 和 \"effect size marginal\" 问题，(3) 修正后的 N=2 observation framing 是否足够。\n\n## paper_framing.md\n\n# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \"harm\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).\n\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\n\n- **Headline result template**: \"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\"\n\n## Core Insight\n\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\"\n- Backup: \"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\n- m1_reextract_v2: expanded extraction for higher coverage\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected\n    vs gold statistics'\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: m1_extraction\n  mvp_registry_id: mvp_p1_codeql_feasibility\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- id: plan_002\n  claim: 1\n  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,\n    3 seeds each, Qwen2.5-Coder-3B LoRA'\n  priority: P0\n  gpu_budget_hours: 200\n  deps:\n  - plan_001\n  registry_id: m2_embed_verify\n  mvp_registry_id: mvp_p2b_contrastive_training\n  full_registry_ids:\n  - m2_full_qwen\n  - m2_full_starcoder\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- id: plan_003\n  claim: 1\n  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best\n    checkpoint, Qwen3.6-27B agent'\n  priority: P0\n  gpu_budget_hours: 40\n  deps:\n  - plan_002\n  notes: eval script ready (eval_swebench.py), dry-run passed, 12 SWE-bench repos\n    pre-cloned to /root/autodl-tmp/structfuse/swebench_repos. Awaiting M2 checkpoint.\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no\n    LLM agent'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  notes: eval script ready (eval_repobench.py), dry-run passed. RepoBench-R data via\n    hf_hub_download. test_easy 8K instances (pool ~6), test_hard 8K (pool ~18). Awaiting\n    M2 checkpoint. [Dream fix] Must run with multiple seeds and report 95% CIs — dream\n    reviewers flagged inconsistent statistical reporting (CIs on SWE-bench but not\n    RepoBench-R) across all 3 tiers.\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding\n    negatives 何时最有害'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  notes: 'analysis script ready (analyze_stratified.py), dry-run passed. 3 strata:\n    repo size / pool size / query-positive similarity. Outputs stratified_results.json\n    + plots PDF. Awaiting M2 checkpoints for re-eval. [Dream fix] Must add 2 more\n    strata: (a) structural data availability (34% with dataflow vs 66% fallback) per\n    [B][M][W] all tiers, (b) neg_difficulty quartile analysis per [W] tier. Total\n    5 strata.'\n  status: planned\n- id: plan_006\n  claim: 3\n  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,\n    connected-but-not-gold ratio by repo size'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan_006_scalability\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- id: plan_007\n  claim: 1\n  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Ablation: fusion head (embedding-only vs structural-features-only\n    vs combined)'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether\n    data-flow helps'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_003\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Qualitative examples: 5-10 cases where structural negatives changed\n    retrieval outcome'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Second encoder validation: repeat M2 core comparison (3 strategies,\n    1 seed) on StarCoder-3B or CodeBERT to test architecture generality'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  dream_source: 'best-R1-W1, median-R2-W5: single encoder is primary generality concern.\n    Upgraded to P0 per Reviewer — this is the #1 factor separating WA from WR.'\n  registry_id: plan_013_starcoder\n  full_registry_id: m2_full_starcoder\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- id: plan_014\n  claim: 2\n  description: 'Temperature ablation: τ ∈ {0.05, 0.1, 0.2} for all 3 strategies, test\n    regime-specificity of embedding harm'\n  priority: P1\n  gpu_budget_hours: 70\n  deps:\n  - plan_002\n  dream_source: 'median-R1-W3: τ=0.05 unusually low, finding may be regime-specific'\n  status: planned\n- id: plan_015\n  claim: 2\n  description: 'Dynamic embedding mining baseline: re-mine embedding negatives per\n    epoch vs static (mine once from pretrained). Isolate selection criterion from\n    curriculum shift.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  dream_source: 'best-R1-W2, median-R1-W2: static vs dynamic mining is potential confound\n    for Claim 2'\n  status: planned\n- id: plan_016\n  claim: 1\n  description: 'Bootstrap CI for SWE-bench Lite: add 95% bootstrap confidence intervals\n    to end-to-end resolve rate evaluation'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  dream_source: 'best-R1-W3, worst-R1-W5: +2.0pp on 300 instances needs statistical\n    significance test'\n  status: planned\n- id: plan_017\n  claim: 1\n  description: 'Inference-time graph method comparison: discuss/compare with CodexGraph,\n    LocAgent — is StructFuse complementary or alternative? Analysis complete, document\n    in artifacts/analysis/plan017_literature_comparison.md. Discussion draft in artifacts/paper_drafts/discussion_draft.md.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  dream_source: 'best-R2-W5: no comparison with inference-time graph methods'\n  notes: 'DONE (analysis only, no experiment). 8 papers surveyed (CodexGraph, LocAgent,\n    RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). All citations verified.\n    Conclusion: training-time vs inference-time are complementary, not competing.'\n  status: planned\n- id: plan_018\n  claim: 1\n  description: 'BM25 negative baseline: mine BM25-based hard negatives as 4th strategy,\n    train ≥1 seed × 2 encoders, compare R@1 with random/embedding/dataflow. Empirically\n    verify CoCoHaNeRe BM25-proxy caused the reported harm.'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers identify missing BM25\n    baseline as #1 structural gap. CoCoHaNeRe correction claim requires empirical\n    verification — without it the paper motivation is asserted but unverified.'\n  notes: 'Phase 1 (CPU, can start now): build BM25 index over training corpus, mine\n    top-k BM25 negatives per query using same protocol as other strategies, produce\n    bm25_training_data.jsonl. Phase 2 (GPU, after M2 frees up): train 1 seed × 2 encoders\n    with BM25 negatives (~7.5h each). 3 seeds preferred if GPU budget allows. Expected\n    result: BM25 negatives harm → confirms CoCoHaNeRe artifact → closes argument.'\n  status: planned\n- id: plan_019\n  claim: 1\n  description: 'Pool size sensitivity analysis: test strategy ranking stability at\n    pool={50, 100, 200, 500} candidates per query on SWE-smith validation.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers flag pool=50 as unrealistically\n    small. Strategy differences may not preserve at realistic pool sizes.'\n  notes: Requires M2 best checkpoints. Re-evaluate on expanded candidate pools. If\n    strategy ranking changes at pool>200, must discuss in paper.\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_p1_codeql_feasibility\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    timeout_rate: 0\n    repos_processed: 8\n    repos_skipped: 2\n    cg_mean_s: 29.6\n    cg_max_s: 119.8\n    df_mean_s: 43.4\n    df_max_s: 167.1\n    h2_connected_coverage: 0.014815\n    h2_disconnected_coverage: 0\n    h2_fisher_p: 6.5e-09\n    h2_gold_in_connected_ratio: 1\n    h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'\n- exp_id: mvp_p2a_linear_proxy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    df_bm25_auc: 0.78\n    bm25_only_auc: 0.476\n    auc_delta: 0.304\n    df_bm25_mrr: 0.556\n    bm25_only_mrr: 0.115\n    mrr_delta: 0.441\n    df_bm25_f1: 0.143\n    bm25_only_f1: 0.039\n    top_feature: is_connected (+2.82)\n    repos_evaluated: 3\n    note: 3 repos / 3 positive samples, directional evidence\n- exp_id: p2b-smoke-test\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke8\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-all-9runs\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_p2b_contrastive_training\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    random_s42_recall1: 0.984\n    random_s123_recall1: 0.984\n    random_s456_recall1: 0.992\n    embedding_s42_recall1: 0.874\n    random_mean_recall1: 0.987\n    runs_completed: 4\n    runs_failed: 5\n    failure_type: disk_full_torch_save\n- exp_id: mvp_p2b_contrastive_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_all\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_4runs_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_seed42:\n      recall@1: 0.9449\n      recall@5: 0.9843\n      recall@10: 0.9843\n    random_seed123:\n      recall@1: 0.9449\n      recall@5: 0.9921\n      recall@10: 0.9921\n    random_seed456:\n      recall@1: 0.9291\n      recall@5: 0.9921\n      recall@10: 0.9921\n    emb_dist_seed42:\n      recall@1: 0.6693\n      recall@5: 0.8898\n      recall@10: 0.9291\n    pool_size: 26\n    n_samples: 127\n- exp_id: p2b_5reruns\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_s42:\n      val_loss: 0.0347\n      recall@1: 0.9843\n    random_s123:\n      val_loss: 0.0446\n      recall@1: 0.9843\n    random_s456:\n      val_loss: 0.0188\n      recall@1: 0.9921\n    emb_dist_s42:\n      val_loss: 0.1876\n      recall@1: 0.874\n    emb_dist_s123:\n      val_loss: 0.1461\n      recall@1: 0.874\n    emb_dist_s456:\n      val_loss: 0.1281\n      recall@1: 0.8819\n    dataflow_s42:\n      val_loss: 0.1878\n      recall@1: 0.874\n    dataflow_s123:\n      val_loss: 0.146\n      recall@1: 0.874\n    dataflow_s456:\n      val_loss: 0.1278\n      recall@1: 0.8819\n    runs_completed: 9\n    runs_failed: 0\n    WARNING: dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds\n      — likely code bug in negative sampling\n- exp_id: p2b_dataflow_retrain\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: p2b_eval_4runs_pool50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pool_size: 50\n    n_samples: 127\n    random_s42:\n      recall@1: 0.496\n      recall@5: 0.843\n      recall@10: 0.945\n    random_s123:\n      recall@1: 0.535\n      recall@5: 0.85\n      recall@10: 0.921\n    random_s456:\n      recall@1: 0.543\n      recall@5: 0.843\n      recall@10: 0.953\n    emb_dist_s42:\n      recall@1: 0.488\n      recall@5: 0.835\n      recall@10: 0.874\n    random_mean:\n      recall@1: 0.525\n      recall@5: 0.845\n      recall@10: 0.94\n    emb_dist_vs_random_delta:\n      recall@1: -0.037\n      recall@5: -0.01\n      recall@10: -0.066\n- exp_id: d007_50repo_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances: 240\n    instances_with_extra_connected: 98\n    Z_pct: 40.8\n    avg_connected_minus_gold: 6\n    codeql_timeout_rate_pct: 4\n    by_repo_size:\n      small_lt50:\n        Z_pct: 38.6\n        avg_extra: 2.5\n      medium_50_200:\n        Z_pct: 55.7\n        avg_extra: 11.8\n      large_gt200:\n        Z_pct: 16.7\n        avg_extra: 8.8\n    decision: Z=40.8% >= 20% -> original method viable, proceed to M1\n- exp_id: m1_extraction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- exp_id: m2_early_pilot\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    pid: 795791\n    gpu: cuda:4\n    gpu_mem_mb: 9342\n    gpu_util_pct: 83\n    batch_size: 2\n    num_negatives: 3\n    max_seq_length: 1024\n    strategy_running: random (stuck at step 4000, epoch 3)\n    strategies_completed: 0/3\n    eval_1500:\n      val_loss: 0.5879\n      recall_at_1: 0.4693\n      recall_at_5: 0.4693\n      recall_at_10: 0.4693\n    eval_2000:\n      val_loss: 0.7089\n      recall_at_1: 0.4398\n    eval_2500:\n      val_loss: 0.6961\n      recall_at_1: 0.4291\n    eval_3000:\n      val_loss: 0.728\n      recall_at_1: 0.4104\n    eval_3500:\n      val_loss: 0.7022\n      recall_at_1: 0.4439\n    best_checkpoint: step_1500 (val_loss=0.5879, 6.2GB)\n    WARNING: recall@1=recall@5=recall@10 confirmed eval bug. Process hung after step\n      4000 (~45min no output). Overfitting after step 1500.\n    status_check_at: '2026-05-13T04:42:00Z'\n- exp_id: m2_early_pilot_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: m2_early_pilot_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: m2_embed_verify\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- exp_id: plan_013_starcoder\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- exp_id: plan_006_scalability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- exp_id: m2_full_qwen\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics:\n    random_s42:\n      status: DONE\n      epoch: 3/3\n      total_steps: 4242\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.4869\n        recall_at_1: 0.533\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.4651\n        recall_at_1: 0.553\n        recall_at_5: 0.959\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.5365\n        recall_at_1: 0.523\n        recall_at_5: 0.955\n        recall_at_10: 1\n      eval_2000:\n        val_loss: 0.5162\n        recall_at_1: 0.523\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_2500:\n        val_loss: 0.5264\n        recall_at_1: 0.527\n        recall_at_5: 0.956\n        recall_at_10: 1\n      eval_3000:\n        val_loss: 0.5406\n        recall_at_1: 0.536\n        recall_at_5: 0.956\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.4651, R@1=0.5527)\n      conclusion: Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357).\n        Full data helps.\n    random_s43:\n      status: RUNNING\n      epoch: 1/2\n      current_step: 1200\n      total_steps: 2810\n      total_steps_per_epoch: 1405\n      eval_500:\n        val_loss: 0.4476\n        recall_at_1: 0.5357\n        recall_at_5: 0.9699\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.4638\n        recall_at_1: 0.5285\n        recall_at_5: 0.9672\n        recall_at_10: 1\n      note: Running on cuda:0. Best R@1=0.5357 at step 500. eval@1000 early_stopping\n        1/2. 2 epochs + patience=2.\n    progress_snapshot: 2026-05-15T00:19 CST\n- exp_id: m2_full_starcoder\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    random_s42:\n      epoch: 3/3\n      current_step: 4000\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.6194\n        recall_at_1: 0.435\n        recall_at_5: 0.905\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.6134\n        recall_at_1: 0.454\n        recall_at_5: 0.92\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.6528\n        recall_at_1: 0.449\n        recall_at_5: 0.906\n        recall_at_10: 1\n      eval_2000:\n        val_loss: 0.6698\n        recall_at_1: 0.4456\n        recall_at_5: 0.906\n        recall_at_10: 1\n      eval_3500:\n        val_loss: 0.6588\n        recall_at_1: 0.4534\n        recall_at_5: 0.9057\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.6134, R@1=0.454)\n      note: Step 4000, lr=2.07e-07, patience exhausted (5/0). Approaching natural\n        end. Watcher PID 309679 ready to auto-start s43.\n    progress_snapshot: 2026-05-15T00:19 CST\n- exp_id: m1_reextract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: neg_difficulty_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_128:\n      random:\n        pos_sim: 0.9804\n        neg_sim: 0.899\n        margin: 0.0816\n        pct_positive_margin: 77.8\n      embedding_distance:\n        pos_sim: 0.9804\n        neg_sim: 0.959\n        margin: 0.0209\n        pct_positive_margin: 60.7\n      dataflow_aware:\n        pos_sim: 0.9805\n        neg_sim: 0.95\n        margin: 0.0309\n        pct_positive_margin: 67.4\n    starcoder_128:\n      random:\n        pos_sim: 0.757\n        neg_sim: 0.553\n        margin: 0.2039\n        pct_positive_margin: 72.8\n      embedding_distance:\n        pos_sim: 0.784\n        neg_sim: 0.668\n        margin: 0.1159\n        pct_positive_margin: 59.2\n      dataflow_aware:\n        pos_sim: 0.761\n        neg_sim: 0.659\n        margin: 0.1022\n        pct_positive_margin: 62.8\n    qwen_2048:\n      random:\n        pos_sim: 0.9855\n        neg_sim: 0.9111\n        margin: 0.0743\n        margin_std: 0.2322\n        pct_positive_margin: 81.8\n      embedding_distance:\n        pos_sim: 0.9855\n        neg_sim: 0.9685\n        margin: 0.017\n        margin_std: 0.114\n        pct_positive_margin: 58.8\n      dataflow_aware:\n        pos_sim: 0.9856\n        neg_sim: 0.9563\n        margin: 0.0293\n        margin_std: 0.1407\n        pct_positive_margin: 73.9\n    starcoder_2048:\n      random:\n        pos_sim: 0.7985\n        neg_sim: 0.6045\n        margin: 0.194\n        margin_std: 0.2788\n        pct_positive_margin: 78\n      embedding_distance:\n        pos_sim: 0.8079\n        neg_sim: 0.7409\n        margin: 0.067\n        margin_std: 0.2056\n        pct_positive_margin: 55\n      dataflow_aware:\n        pos_sim: 0.8009\n        neg_sim: 0.6818\n        margin: 0.1192\n        margin_std: 0.2264\n        pct_positive_margin: 70.4\n    sc_qwen_margin_ratio_128:\n      random: 2.5\n      embedding_distance: 5.54\n      dataflow_aware: 3.3\n    sc_qwen_margin_ratio_2048:\n      random: 2.61\n      embedding_distance: 3.94\n      dataflow_aware: 4.07\n- exp_id: m1_reextract_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T16:26:59.614Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T16:26:59.614Z",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e"
}
```

---

## Round 1

22 recorded events

### User

_source line 3 · 2026-05-14T16:26:59.635Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：全 18 runs 复现 pilot pattern，BM25 baseline 关闭 CoCoHaNeRe 论证，三条 claim 原样成立
核心假设：['embedding-random R@1 delta 在两个 encoder 上 95% CI 下界 > 0', 'dataflow-random R@1 delta 在 Qwen 上 CI 下界 > 0，StarCoder 上 ≤ 0（条件性成立）', 'BM25 negatives 明确 harm（vs random delta 显著为负），实证关闭 CoCoHaNeRe proxy 论证', 'pool size 50→500 策略排名不翻转', 'SWE-bench Lite 下游 resolve rate 有可见提升']
关键指标范围：{'qwen_emb_minus_random_R1_pp': [1.5, 2.5], 'starcoder_emb_minus_random_R1_pp': [1.0, 2.0], 'qwen_df_minus_random_R1_pp': [0.5, 1.5], 'starcoder_df_minus_random_R1_pp': [-1.0, 0.3], 'bm25_minus_random_R1_pp': [-4.0, -1.5], 'swebench_resolve_rate_delta_pp': [1.5, 4.0], 'repobench_R1_delta_pp': [1.0, 3.0], 'pool_ranking_stable_pct': [75, 100], 'bootstrap_CI_width_R1_pp': [0.5, 2.0], 'qwen_mean_R1_absolute': [0.53, 0.58], 'starcoder_mean_R1_absolute': [0.44, 0.5]}
叙事方向：原始 framing 完全成立。Claim 1（embedding mining 纠正 misconception）有 BM25 baseline 实证支撑 + 两 encoder 统计显著。Claim 2（dataflow 条件性获益）由 Qwen/StarCoder 对比 + neg_difficulty margin 分析 + representation saturation 机制完整闭环。Claim 3 作为 supporting methodology 无需额外论证。标题可用 "Correcting Misconceptions" 强 framing， SWE-bench 数据作为 downstream validation 加固 practical relevance。EMNLP Main 强投。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: structfuse-context
focus: D030 修复后验证：新增 plan_018 BM25 baseline（关闭 CoCoHaNeRe correction 论证）、plan_019 pool size sensitivity、plan_004 多 seed CIs、plan_005 structural coverage 分层 + neg_difficulty quartile。Framing 修正：N=2 降级为 observation、Claim 3 降为 supporting methodology、StarCoder decoder-only。Reviewers 应重点评估：(1) BM25 baseline 是否关闭了上一轮最大缺口，(2) 新增实验是否充分回应了上一轮 median/worst 的 "related work insufficient" 和 "effect size marginal" 问题，(3) 修正后的 N=2 observation framing 是否足够。

## paper_framing.md

# Paper Framing — StructFuse

## Target Venue
- Primary: EMNLP 2026 Main
- Deadline: ARR May 25, 2026

## Core Claims (3)

1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported "harm" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).

2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.

3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]

## Story Spine

- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.

- **Existing approaches & gaps**:
  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies
  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal
  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance
  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works

- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.

- **Headline result template**: "True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis."

## Core Insight

The effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.

## Dual-Pillar Motivation

1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.
2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.

## Formal Definition

Given retrieval domain D, structural graph G, similarity function s, query q:
**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)

The structural graph is externally fixed and does not update with the encoder (drift-immune).

## Title Options

- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
- Alternative: "StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval"
- Backup: "Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally"

## Venue Fit

1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
3. **Against "incremental" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.

## Anticipated Reviewer Concerns

| Concern | Response | Evidence |
|---------|----------|----------|
| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |
| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |
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
- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact
- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
- plan_006: CodeQL scalability confirmed at 123-repo scale

### In progress:
- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)
- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)
- m1_reextract_v2: expanded extraction for higher coverage

### Planned (priority order):
- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)
- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
- plan_019: Pool size sensitivity (Dream consensus — external validity)
- plan_014: Temperature ablation (Dream reviewer concern)
- plan_004: RepoBench-R second benchmark (with multi-seed CIs)
- plan_015: Dynamic mining baseline
- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)
- plan_007/008/009: Additional ablations

## Contingency (if full M2 results weaken claims)

### All 18 runs confirm pilot pattern: Best case
- Full statistical power, paper as framed above
- Target: EMNLP Main

### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
- Drop Claim 2 to analysis observation
- Paper becomes: "True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main

### Embedding mining also loses advantage at full scale: Major reassessment needed
- Recheck data pipeline for bugs (full-scale data may have distribution differences)
- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
- Discuss with user before committing direction

## Deprecated Claims (with reason)

- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.


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
  dream_source: 'best-R2-W5: no comparison with inference-time graph methods'
  notes: 'DONE (analysis only, no experiment). 8 papers surveyed (CodexGraph, LocAgent,
    RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). All citations verified.
    Conclusion: training-time vs inference-time are complementary, not competing.'
  status: planned
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
      status: RUNNING
      epoch: 1/2
      current_step: 1200
      total_steps: 2810
      total_steps_per_epoch: 1405
      eval_500:
        val_loss: 0.4476
        recall_at_1: 0.5357
        recall_at_5: 0.9699
        recall_at_10: 1
      eval_1000:
        val_loss: 0.4638
        recall_at_1: 0.5285
        recall_at_5: 0.9672
        recall_at_10: 1
      note: Running on cuda:0. Best R@1=0.5357 at step 500. eval@1000 early_stopping
        1/2. 2 epochs + patience=2.
    progress_snapshot: 2026-05-15T00:19 CST
- exp_id: m2_full_starcoder
  name: ''
  status: RUNNING
  conclusion: ''
  metrics:
    random_s42:
      epoch: 3/3
      current_step: 4000
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
      eval_3500:
        val_loss: 0.6588
        recall_at_1: 0.4534
        recall_at_5: 0.9057
        recall_at_10: 1
      best_checkpoint: step_1000 (val_loss=0.6134, R@1=0.454)
      note: Step 4000, lr=2.07e-07, patience exhausted (5/0). Approaching natural
        end. Watcher PID 309679 ready to auto-start s43.
    progress_snapshot: 2026-05-15T00:19 CST
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
  status: RUNNING
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
  "promptId": "31f911b9-2b77-479d-b3c3-7ac091b3c562",
  "type": "user",
  "uuid": "a0d95484-b180-473a-8c7b-d07ac6527079",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T16:26:59.634Z_

```json
{
  "parentUuid": "a0d95484-b180-473a-8c7b-d07ac6527079",
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
  "uuid": "0bc642d6-84e2-49ab-b4aa-e406dc792ded",
  "timestamp": "2026-05-14T16:26:59.634Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T16:26:59.634Z_

```json
{
  "parentUuid": "0bc642d6-84e2-49ab-b4aa-e406dc792ded",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "5bf8190b-0415-4f70-949c-3f453202b15c",
  "timestamp": "2026-05-14T16:26:59.634Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T16:26:59.634Z_

```json
{
  "parentUuid": "5bf8190b-0415-4f70-949c-3f453202b15c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b6a6215d-3b2a-4ab8-9908-341596549956",
  "timestamp": "2026-05-14T16:26:59.634Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：全 18 runs 复现 pilot pattern，BM25 baseline 关闭 CoCoHaNeRe 论证，三条 claim 原样成立 核心假设：['embedding-random R@1 delta 在两个 encoder 上 95% CI 下界 > 0', 'dataflow-random R@…",
  "leafUuid": "b6a6215d-3b2a-4ab8-9908-341596549956",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic empirical validation of hard negative mining strategies for code retrieval",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e"
}
```

---

### Assistant

_source line 9 · 2026-05-14T16:27:06.742Z_

I'll analyze the experiment plan and generate detailed predicted data for the "best" tier. Let me first review the existing metrics and plan details to ensure consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6a6215d-3b2a-4ab8-9908-341596549956",
  "isSidechain": false,
  "requestId": "req_011Cb2muHBQVUxuDM4dczHGc",
  "type": "assistant",
  "uuid": "6ab0e2d7-9cf0-4356-8d93-a16791908dde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7sMbb2aFC23MEvDkMcDwv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19194,
      "cache_read_input_tokens": 11447,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 123,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 19194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19194
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

_source line 10 · 2026-05-14T16:27:07.987Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PqDnpWHdQ5qFnV8wqLhHRc`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ab0e2d7-9cf0-4356-8d93-a16791908dde",
  "isSidechain": false,
  "requestId": "req_011Cb2muHBQVUxuDM4dczHGc",
  "type": "assistant",
  "uuid": "ab59e227-2491-49c1-96cc-4359fd70d390",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y7sMbb2aFC23MEvDkMcDwv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19194,
      "cache_read_input_tokens": 11447,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19194,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 123,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 19194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19194
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

_source line 11 · 2026-05-14T16:27:08.009Z_

<details><summary>↩ Tool result · `toolu_01PqDnpWHdQ5qFnV8wqLhHRc`</summary>

```text
.claude/sessions/no_project_3780bb6c/CLAUDE.md
.claude/sessions/no_project_3780bb6c/AGENTS.md
.claude/sessions/idea_reviewer_7aba9979/CLAUDE.md
.claude/sessions/idea_reviewer_7aba9979/AGENTS.md
projects/structfuse-context/artifacts/mvp_p1_codeql_feasibility/report/mvp_phase1_report.md
projects/structfuse-context/artifacts/mvp_p2b_contrastive_training/report/failure_diagnosis.md
projects/structfuse-context/task_context/history/director/loop_1.md
projects/structfuse-context/task_context/history/agent/loop_1.md
projects/structfuse-context/task_context/history/agent/loop_1_1778635668.md
projects/structfuse-context/task_context/history/reviewer/loop_2.md
projects/structfuse-context/artifacts/_project/report/50repo_overlap_report.md
projects/structfuse-context/docs/IDEA_BRIEF.md
projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/review_report.md
projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/median/review_report.md
projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/worst/review_report.md
projects/structfuse-context/docs/handoff_20260513.md
projects/structfuse-context/task_context/history/reviewer/loop_3.md
projects/structfuse-context/task_context/history/agent/loop_2.md
projects/structfuse-context/task_context/history/agent/loop_2_1778708899.md
projects/structfuse-context/artifacts/disk_cleanup_report_20260513.md
projects/structfuse-context/artifacts/_project/report/scalability_summary.md
projects/structfuse-context/artifacts/plan_006/scalability_summary.md
projects/structfuse-context/artifacts/m1_progress_0513.md
projects/structfuse-context/artifacts/bjb1_status_check.md
projects/structfuse-context/artifacts/_project/report/pilot_results_summary.md
projects/structfuse-context/artifacts/_project/report/pilot_results_summary_64aa24.md
projects/structfuse-context/task_context/history/reviewer/loop_1.md
projects/structfuse-context/.claude/sessions/agent_cb55d4ab/CLAUDE.md
projects/structfuse-context/.claude/sessions/agent_cb55d4ab/AGENTS.md
projects/structfuse-context/task_context/history/director/loop_2.md
projects/structfuse-context/task_context/history/reviewer/loop_4.md
projects/structfuse-context/memory.md
projects/structfuse-context/task_context/history/agent/loop_3.md
projects/structfuse-context/artifacts/rename_safety_report.md
projects/structfuse-context/artifacts/plan003_swebench_eval_plan.md
projects/structfuse-context/task_context/history/director/loop_3.md
projects/structfuse-context/task_context/history/reviewer/loop_5.md
projects/structfuse-context/artifacts/plan003_eval_readiness.md
projects/structfuse-context/task_context/history/director/loop_4.md
projects/structfuse-context/task_context/history/reviewer/loop_6.md
projects/structfuse-context/task_context/history/agent/loop_4.md
projects/structfuse-context/artifacts/training_status_snapshot.md
projects/structfuse-context/artifacts/swebench_eval_readiness.md
projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md
projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/paper_framing.md
projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper_framing.md
projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/review_report.md
projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/review_report.md
projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/review_report.md
projects/structfuse-context/artifacts/analysis/plan017_literature_comparison.md
projects/structfuse-context/report.md
projects/structfuse-context/artifacts/m2_full_qwen_analysis.md
projects/structfuse-context/artifacts/m2_full_qwen/report/m2_full_qwen_analysis.md
projects/structfuse-context/task_context/history/agent/loop_5.md
projects/structfuse-context/.claude/sessions/agent_2bc11d4f/CLAUDE.md
projects/structfuse-context/.claude/sessions/agent_2bc11d4f/AGENTS.md
projects/structfuse-context/task_context/agent.md
projects/structfuse-context/task_context/reviewer.md
projects/structfuse-context/artifacts/m2_qwen_status_check.md
projects/structfuse-context/artifacts/m2_full_starcoder/report/m2_starcoder_status_check.md
projects/structfuse-context/artifacts/m2_starcoder_status_check.md
projects/structfuse-context/artifacts/status_check_loop6.md
projects/structfuse-context/task_context/director.md
projects/structfuse-context/artifacts/_project/report/plan_015_dynamic_mining_design.md
projects/structfuse-context/ROADMAP.md
projects/structfuse-context/.claude/sessions/agent_204785e5/CLAUDE.md
projects/structfuse-context/.claude/sessions/agent_204785e5/AGENTS.md
projects/structfuse-context/.claude/sessions/reviewer_65cfe724/CLAUDE.md
projects/structfuse-context/.claude/sessions/reviewer_65cfe724/AGENTS.md
.claude/CLAUDE.md
AGENTS.md
projects/structfuse-context/.claude/CLAUDE.md
projects/structfuse-context/AGENTS.md
projects/structfuse-context/.claude/sessions/director_3a5c0d9a/CLAUDE.md
projects/structfuse-context/.claude/sessions/director_3a5c0d9a/AGENTS.md
projects/structfuse-context/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab59e227-2491-49c1-96cc-4359fd70d390",
  "isSidechain": false,
  "promptId": "31f911b9-2b77-479d-b3c3-7ac091b3c562",
  "type": "user",
  "uuid": "6abcb68a-4882-4464-8ed6-309b3f2f8dab",
  "toolUseResult": {
    "filenames": [
      ".claude/sessions/no_project_3780bb6c/CLAUDE.md",
      ".claude/sessions/no_project_3780bb6c/AGENTS.md",
      ".claude/sessions/idea_reviewer_7aba9979/CLAUDE.md",
      ".claude/sessions/idea_reviewer_7aba9979/AGENTS.md",
      "projects/structfuse-context/artifacts/mvp_p1_codeql_feasibility/report/mvp_phase1_report.md",
      "projects/structfuse-context/artifacts/mvp_p2b_contrastive_training/report/failure_diagnosis.md",
      "projects/structfuse-context/task_context/history/director/loop_1.md",
      "projects/structfuse-context/task_context/history/agent/loop_1.md",
      "projects/structfuse-context/task_context/history/agent/loop_1_1778635668.md",
      "projects/structfuse-context/task_context/history/reviewer/loop_2.md",
      "projects/structfuse-context/artifacts/_project/report/50repo_overlap_report.md",
      "projects/structfuse-context/docs/IDEA_BRIEF.md",
      "projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/review_report.md",
      "projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/median/review_report.md",
      "projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/worst/review_report.md",
      "projects/structfuse-context/docs/handoff_20260513.md",
      "projects/structfuse-context/task_context/history/reviewer/loop_3.md",
      "projects/structfuse-context/task_context/history/agent/loop_2.md",
      "projects/structfuse-context/task_context/history/agent/loop_2_1778708899.md",
      "projects/structfuse-context/artifacts/disk_cleanup_report_20260513.md",
      "projects/structfuse-context/artifacts/_project/report/scalability_summary.md",
      "projects/structfuse-context/artifacts/plan_006/scalability_summary.md",
      "projects/structfuse-context/artifacts/m1_progress_0513.md",
      "projects/structfuse-context/artifacts/bjb1_status_check.md",
      "projects/structfuse-context/artifacts/_project/report/pilot_results_summary.md",
      "projects/structfuse-context/artifacts/_project/report/pilot_results_summary_64aa24.md",
      "projects/structfuse-context/task_context/history/reviewer/loop_1.md",
      "projects/structfuse-context/.claude/sessions/agent_cb55d4ab/CLAUDE.md",
      "projects/structfuse-context/.claude/sessions/agent_cb55d4ab/AGENTS.md",
      "projects/structfuse-context/task_context/history/director/loop_2.md",
      "projects/structfuse-context/task_context/history/reviewer/loop_4.md",
      "projects/structfuse-context/memory.md",
      "projects/structfuse-context/task_context/history/agent/loop_3.md",
      "projects/structfuse-context/artifacts/rename_safety_report.md",
      "projects/structfuse-context/artifacts/plan003_swebench_eval_plan.md",
      "projects/structfuse-context/task_context/history/director/loop_3.md",
      "projects/structfuse-context/task_context/history/reviewer/loop_5.md",
      "projects/structfuse-context/artifacts/plan003_eval_readiness.md",
      "projects/structfuse-context/task_context/history/director/loop_4.md",
      "projects/structfuse-context/task_context/history/reviewer/loop_6.md",
      "projects/structfuse-context/task_context/history/agent/loop_4.md",
      "projects/structfuse-context/artifacts/training_status_snapshot.md",
      "projects/structfuse-context/artifacts/swebench_eval_readiness.md",
      "projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md",
      "projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/paper_framing.md",
      "projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/paper_framing.md",
      "projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/review_report.md",
      "projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/review_report.md",
      "projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/review_report.md",
      "projects/structfuse-context/artifacts/analysis/plan017_literature_comparison.md",
      "projects/structfuse-context/report.md",
      "projects/structfuse-context/artifacts/m2_full_qwen_analysis.md",
      "projects/structfuse-context/artifacts/m2_full_qwen/report/m2_full_qwen_analysis.md",
      "projects/structfuse-context/task_context/history/agent/loop_5.md",
      "projects/structfuse-context/.claude/sessions/agent_2bc11d4f/CLAUDE.md",
      "projects/structfuse-context/.claude/sessions/agent_2bc11d4f/AGENTS.md",
      "projects/structfuse-context/task_context/agent.md",
      "projects/structfuse-context/task_context/reviewer.md",
      "projects/structfuse-context/artifacts/m2_qwen_status_check.md",
      "projects/structfuse-context/artifacts/m2_full_starcoder/report/m2_starcoder_status_check.md",
      "projects/structfuse-context/artifacts/m2_starcoder_status_check.md",
      "projects/structfuse-context/artifacts/status_check_loop6.md",
      "projects/structfuse-context/task_context/director.md",
      "projects/structfuse-context/artifacts/_project/report/plan_015_dynamic_mining_design.md",
      "projects/structfuse-context/ROADMAP.md",
      "projects/structfuse-context/.claude/sessions/agent_204785e5/CLAUDE.md",
      "projects/structfuse-context/.claude/sessions/agent_204785e5/AGENTS.md",
      "projects/structfuse-context/.claude/sessions/reviewer_65cfe724/CLAUDE.md",
      "projects/structfuse-context/.claude/sessions/reviewer_65cfe724/AGENTS.md",
      ".claude/CLAUDE.md",
      "AGENTS.md",
      "projects/structfuse-context/.claude/CLAUDE.md",
      "projects/structfuse-context/AGENTS.md",
      "projects/structfuse-context/.claude/sessions/director_3a5c0d9a/CLAUDE.md",
      "projects/structfuse-context/.claude/sessions/director_3a5c0d9a/AGENTS.md",
      "projects/structfuse-context/paper_framing.md"
    ],
    "durationMs": 14,
    "numFiles": 76,
    "truncated": false
  },
  "sourceToolAssistantUUID": "ab59e227-2491-49c1-96cc-4359fd70d390",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T16:27:21.224Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K6XJztF95vFCSpMbmzPrQ2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6abcb68a-4882-4464-8ed6-309b3f2f8dab",
  "isSidechain": false,
  "requestId": "req_011Cb2mutwTnD3MggfBvEv4a",
  "type": "assistant",
  "uuid": "9e307ba8-d7f6-4246-a46a-5c2ec0aeb05e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPYPXUzVUSQK7Y8XrEfw97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1852,
      "cache_read_input_tokens": 30641,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1852,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 30641,
          "cache_creation_input_tokens": 1852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1852
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

_source line 13 · 2026-05-14T16:27:21.240Z_

<details><summary>↩ Tool result · `toolu_01K6XJztF95vFCSpMbmzPrQ2`</summary>

```text
1	# Paper Framing — StructFuse
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main
5	- Deadline: ARR May 25, 2026
6	
7	## Core Claims (3)
8	
9	1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported "harm" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).
10	
11	2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.
12	
13	3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).
14	
15	## Story Spine
16	
17	- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.
18	
19	- **Existing approaches & gaps**:
20	  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies
21	  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal
22	  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
23	  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance
24	  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works
25	
26	- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.
27	
28	- **Headline result template**: "True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis."
29	
30	## Core Insight
31	
32	The effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.
33	
34	## Dual-Pillar Motivation
35	
36	1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.
37	2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.
38	
39	## Formal Definition
40	
41	Given retrieval domain D, structural graph G, similarity function s, query q:
42	**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)
43	
44	The structural graph is externally fixed and does not update with the encoder (drift-immune).
45	
46	## Title Options
47	
48	- Primary: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
49	- Alternative: "StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval"
50	- Backup: "Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally"
51	
52	## Venue Fit
53	
54	1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. "Do Language Models..." papers). Contribution is understanding, not just a new method.
55	2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.
56	3. **Against "incremental" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.
57	
58	## Anticipated Reviewer Concerns
59	
60	| Concern | Response | Evidence |
61	|---------|----------|----------|
62	| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |
63	| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |
64	| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |
65	| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |
66	| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |
67	| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |
68	| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |
69	| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |
70	| "Complementary signal" overstatement | Temper: "conditionally beneficial" not "always complementary" | Writing discipline |
71	| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |
72	
73	## Evidence Status
74	
75	### Confirmed findings (basis for claims):
76	- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact
77	- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction
78	- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)
79	- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only
80	- plan_006: CodeQL scalability confirmed at 123-repo scale
81	
82	### In progress:
83	- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)
84	- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)
85	- m1_reextract_v2: expanded extraction for higher coverage
86	
87	### Planned (priority order):
88	- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
89	- plan_014: Temperature ablation (Dream reviewer concern)
90	- plan_004: RepoBench-R second benchmark
91	- plan_015: Dynamic mining baseline
92	- plan_007/008/009: Additional ablations
93	
94	## Contingency (if full M2 results weaken claims)
95	
96	### All 18 runs confirm pilot pattern: Best case
97	- Full statistical power, paper as framed above
98	- Target: EMNLP Main
99	
100	### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper
101	- Drop Claim 2 to analysis observation
102	- Paper becomes: "True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions"
103	- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main
104	
105	### Embedding mining also loses advantage at full scale: Major reassessment needed
106	- Recheck data pipeline for bugs (full-scale data may have distribution differences)
107	- If confirmed: negative result paper — "Why Hard Negative Mining Doesn't Scale for Code Retrieval"
108	- Discuss with user before committing direction
109	
110	## Deprecated Claims (with reason)
111	
112	- ~~"Embedding-distance hard negatives actively harm code retrieval"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e307ba8-d7f6-4246-a46a-5c2ec0aeb05e",
  "isSidechain": false,
  "promptId": "31f911b9-2b77-479d-b3c3-7ac091b3c562",
  "type": "user",
  "uuid": "5ae404f5-3808-4d1f-8e89-30bbae77ead3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/paper_framing.md",
      "content": "# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \"harm\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).\n\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\n\n- **Headline result template**: \"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\"\n\n## Core Insight\n\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\"\n- Backup: \"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\n- m1_reextract_v2: expanded extraction for higher coverage\n\n### Planned (priority order):\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark\n- plan_015: Dynamic mining baseline\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n",
      "numLines": 113,
      "startLine": 1,
      "totalLines": 113
    }
  },
  "sourceToolAssistantUUID": "9e307ba8-d7f6-4246-a46a-5c2ec0aeb05e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T16:27:21.835Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RsRHAAmkBSEZ8WH3Efu1hY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/review_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ae404f5-3808-4d1f-8e89-30bbae77ead3",
  "isSidechain": false,
  "requestId": "req_011Cb2mutwTnD3MggfBvEv4a",
  "type": "assistant",
  "uuid": "f4ae0409-7aeb-4811-a6af-a984cda3c9ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KPYPXUzVUSQK7Y8XrEfw97",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1852,
      "cache_read_input_tokens": 30641,
      "output_tokens": 188,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1852,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 188,
          "cache_read_input_tokens": 30641,
          "cache_creation_input_tokens": 1852,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1852
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

_source line 15 · 2026-05-14T16:27:21.839Z_

<details><summary>↩ Tool result · `toolu_01RsRHAAmkBSEZ8WH3Efu1hY`</summary>

```text
1	---
2	dream_id: dream_20260514T075732
3	tier: best
4	overall_score: 4/6 Weak Accept
5	timestamp: 2026-05-14T08:33:59.100296+00:00
6	---
7	
8	---
9	dream_id: dream_20260514T075732
10	tier: best
11	reviewer: R1 (Methods and Experiments)
12	overall_score: 4/6 Weak Accept
13	timestamp: 2026-05-14
14	---
15	
16	# R1 Review: Methods and Experiments
17	
18	**Paper**: "What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry"
19	
20	---
21	
22	## Summary
23	
24	The paper presents a controlled comparison of three hard negative mining strategies (random, embedding-distance, dataflow-aware) for contrastive code retrieval, evaluated across two 3B-parameter encoders with 9 seeds each. The main findings are that embedding-distance mining consistently improves R@1 (+2.3pp Qwen, +1.7pp StarCoder), while dataflow-aware mining provides conditional benefit mediated by representation saturation (significant on Qwen, null on StarCoder). The experimental design is ambitious and the ablation suite is commendably broad, but several methodological concerns -- including the generalizability of the "representation geometry" theory from only 2 encoders, unrealistic retrieval pool sizes, missing baselines, and discrepancies between reported and actual result maturity -- undermine the strength of the claims.
25	
26	---
27	
28	## Strengths
29	
30	- **Exemplary experimental scale and statistical discipline.** 54 training runs (2 x 3 x 9) with paired bootstrap 95% CIs and explicit p-values for all main comparisons is well above the standard for this subfield. The paper does not rely on single-seed results, and the statistical testing is appropriate (bootstrap CIs, paired comparisons).
31	
32	- **Comprehensive ablation suite with clear analytical purpose.** Each ablation (temperature, hop depth, data scaling, fusion head, static vs. dynamic mining, binary vs. weighted dataflow) answers a specific methodological question rather than padding the paper. The dynamic mining baseline (Table 13) is particularly valuable for ruling out curriculum effects as a confound, and the fusion head ablation (Table 11) cleanly separates training-time mining value from inference-time feature injection.
33	
34	- **Honest reporting of null and conditional results.** The StarCoder dataflow null (p=0.62), the dataflow-vs-embed non-significance (p=0.134 on SWE-bench), and the diminishing returns at scale (Table 10) are reported transparently. Many papers would suppress these findings.
35	
36	- **Mechanistically motivated analysis.** The representation saturation explanation (pos_sim 0.986 vs. 0.799) goes beyond "method X beats method Y" to provide a predictive framework. If validated, the pos_sim diagnostic could be a genuinely useful practitioner tool.
37	
38	- **Clean experimental control.** The comparison holds all variables constant except the negative selection strategy -- same data, same encoder, same LoRA configuration, same training schedule. This is the correct way to study the effect of a single factor.
39	
40	- **SWE-bench Lite end-to-end evaluation.** Including downstream task evaluation, even though the results are positive, adds credibility beyond retrieval-only metrics.
41	
42	---
43	
44	## Weaknesses
45	
46	### Major
47	
48	1. **Generalizability from N=2 encoders is fundamentally limited (Section 5, Discussion).** The paper's central mechanistic claim -- that representation saturation mediates the effectiveness of structural negatives -- rests on exactly two data points: Qwen (saturated, pos_sim=0.986) and StarCoder (healthy, pos_sim=0.799). This is insufficient to establish a functional relationship. The two encoders also differ in pretraining data, pretraining objective, tokenizer, and model family, meaning the observed interaction could be driven by any of these confounds rather than representation geometry per se. The paper characterizes StarCoder2-3B as "encoder-decoder" (Section 3.4), but StarCoder2-3B is decoder-only (autoregressive), making the claimed "architecturally distinct" comparison misleading. At minimum, the paper needs (a) to correct the architectural characterization, and (b) to explicitly acknowledge that the saturation theory is an observation from N=2, not a validated mechanism.
49	
50	2. **Pool size of 50 candidates per query is unrealistically small (Section 3.4, implicitly).** Real-world repositories contain hundreds to thousands of files. A pool of 50 means the retriever is choosing among ~50 files, which inflates absolute recall numbers and may mask differences between strategies that would emerge at realistic pool sizes. The paper does not discuss this design choice or its implications for external validity. At pool=50, even random selection has a 2% baseline chance per candidate, making R@1 in the 0.50+ range less impressive. The RepoBench-R evaluation (Table 5) uses a different pool size but this is not specified.
51	
52	3. **Missing BM25 negative baseline.** The paper's headline narrative -- correcting CoCoHaNeRe's finding that embedding negatives harm code search -- attributes the prior result to BM25-proxy negatives mislabeled as embedding-distance. Yet the paper never runs actual BM25 negatives to demonstrate that the harm is BM25-specific. This is the single most important missing experiment given the framing. Without it, the "correction" is argumentative rather than empirical.
53	
54	4. **SWE-bench Lite results appear inflated relative to project state.** The paper reports +2.3pp (embedding) and +3.3pp (dataflow) resolve-rate gains over random on SWE-bench Lite, with bootstrap CIs excluding zero (Table 4). However, training data from the project's internal decision log (D018, D019, D026, D027) shows that as of the review date, the full M2 runs (9 seeds per strategy per encoder) are still in progress, with only seed 1 partially completed for each encoder. The pilot results (D017) from 1 seed show much smaller effects (+2.0pp Qwen embedding, with dataflow ranking dependent on checkpoint selection criterion). The SWE-bench results reported in the "best" paper variant are substantially stronger than the evidence base supports. If these are projected/simulated results, this must be disclosed.
55	
56	5. **No error bars or CIs on RepoBench-R results (Table 5).** RepoBench-R results are reported as single numbers without seeds, confidence intervals, or significance tests. Given that the reported deltas (e.g., +1.9pp R@1 for embedding on Qwen) are small, these may not be statistically distinguishable from zero. For a paper that emphasizes statistical rigor on the SWE-smith results, the asymmetry in reporting standards is conspicuous.
57	
58	6. **SWE-smith validation results mentioned but not shown.** Section 4 references SWE-smith validation R@1 as the primary evaluation metric, and the main tables (Tables 1-2) report these. But the actual validation set construction, size, and overlap with training data are not described. Given that the project logs show severe overfitting (best checkpoint at step 1000 out of 4242, D026), the validation protocol is critical for interpreting results, yet insufficiently documented.
59	
60	7. **34% structural coverage dilutes the dataflow signal (Section 3.3, implicit).** Only 34.3% of training instances receive dataflow-mined negatives; the remaining 65.7% fall back to alternative selection (presumably embedding or random). The reported +1.5pp dataflow improvement (Table 1, Qwen) averages over all instances including those that received no structural signal. Stratified results (structural-available vs. fallback) are absent. The true per-instance effect of dataflow mining on instances where it actually applies could be much larger (or much smaller) than the reported average. This stratification is essential for interpreting the result.
61	
62	### Minor
63	
64	8. **Table 6 "<50 instances" tier has N=1 repo.** Including a tier with a single repository is misleading and inflates the apparent trend. The correlation r=-0.41 (p=0.08) is heavily influenced by this outlier. The tier should either be removed or its N=1 status should be prominently flagged with appropriate caveats.
65	
66	9. **LoRA rank 16, 3 epochs may be insufficient.** With LoRA rank 16 (a low-rank adapter), the encoder's representational capacity to learn from different negative strategies is limited. Strategy differences might only emerge with fuller fine-tuning. The paper does not discuss whether LoRA's low-rank bottleneck could compress away the differences between strategies. The observed overfitting at step 1000 (1/4 through training) suggests the learning dynamics are dominated by regularization effects, not data effects.
67	
68	10. **Checkpoint selection criterion ambiguity.** The project history (D017) reveals that strategy rankings change depending on whether checkpoints are selected by best validation loss or best R@1. The paper does not specify which criterion is used. Given that this choice can reverse the ordering of strategies (dataflow > embedding by peak R@1 vs. embedding > dataflow by val_loss for Qwen, per D017), this is a material omission.
69	
70	11. **All references render as [?].** The bibliography is broken -- every citation in the compiled paper appears as [?]. This makes it impossible to verify the related work coverage or the CoCoHaNeRe critique. For a paper whose central claim involves correcting a prior work's methodology, unresolvable citations are a serious presentation issue.
71	
72	12. **Number of negatives per query (K) not stated.** The method section defines "select k negatives" but never specifies the value of K used in experiments. This is a basic reproducibility gap.
73	
74	13. **Overfitting patterns not reported.** Project logs show train_loss dropping to 0.04 while val_loss remains at 0.52 (D026), yet the paper does not discuss overfitting or show learning curves. Strategy-specific overfitting patterns could be informative (e.g., does dataflow overfit faster due to fewer unique negatives?).
75	
76	---
77	
78	## Questions for Authors
79	
80	1. **SWE-bench result provenance.** Tables 3-4 report SWE-bench Lite results with bootstrap CIs excluding zero for embedding and dataflow vs. random. Are these from completed 9-seed runs, or projected from pilot data? If the full M2 runs are still in progress, what is the actual evidence base for these numbers?
81	
82	2. **Checkpoint selection criterion.** Which checkpoint is used for the main results -- best by validation loss, or best by R@1? Your project logs (D017) show these criteria produce different strategy rankings. Have you reported both, and if not, why?
83	
84	3. **Stratified dataflow results.** What is the R@1 delta for the ~34% of instances that actually receive dataflow-mined negatives vs. the ~66% that fall back? This decomposition is essential for understanding whether the dataflow signal is strong-but-diluted or weak-throughout.
85	
86	4. **BM25 baseline omission.** The paper's narrative hinges on CoCoHaNeRe using "BM25-proxy negatives mislabeled as embedding-distance." Can you provide specific textual evidence from CoCoHaNeRe supporting this claim? And why not run BM25 negatives as a fourth strategy to close the argument empirically?
87	
88	5. **Pool size sensitivity.** How do strategy differences change as pool size increases from 50 to 200 or 500? If differences shrink at realistic pool sizes, this would substantially weaken the practical relevance of the findings.
89	
90	---
91	
92	## Minor Issues
93	
94	- Section 3.4: StarCoder2-3B is described as "Encoder-decoder" -- it is decoder-only. Correct throughout.
95	- Table 6 (stratified analysis in the best paper) vs. Table 6 (median paper): the two variants report completely different stratification schemes (by file count vs. by instance count), suggesting the analysis is not yet stable.
96	- Abstract line "SWE-bench Lite end-to-end evaluation with a Qwen3.6-27B agent" -- only Qwen retriever checkpoints are used for SWE-bench, not StarCoder. This asymmetry should be acknowledged.
97	- The paper name "StructFuse" implies a fusion system, but the best-performing approach is pure embedding mining without fusion (Table 11 shows fusion slightly degrades performance). The name is misleading.
98	- Hop depth ablation (Table 9): the "best" paper reports clean improvements (2-hop optimal), while the median paper (Table 9) reports differences "within noise range." The discrepancy in framing across tiers suggests cherry-picking of presentation.
99	- Section 3.3 reports "131 SWE-smith repositories" but only "123/131 repos producing valid output" -- the 8 failures are not analyzed.
100	
101	---
102	
103	## Overall Assessment
104	
105	This paper tackles a genuinely important question -- what makes hard negatives work for code retrieval -- with commendable experimental rigor in its design (9 seeds, bootstrap CIs, extensive ablations). The representation saturation insight, if validated on more encoders, could become a useful diagnostic tool for practitioners. However, the paper is undermined by (a) the N=2 encoder limitation that makes the "representation geometry" theory an observation rather than a validated mechanism, (b) missing baselines (BM25) that are critical to the headline narrative, (c) potential discrepancies between reported results and actual experimental maturity, (d) unrealistic pool sizes that limit external validity, and (e) several reporting gaps (no CIs on RepoBench, no stratification by structural coverage, checkpoint criterion unspecified). The paper is above-average in experimental discipline but below the bar for confident acceptance at a top venue in its current form. Addressing the BM25 baseline, the stratified analysis, and the pool size sensitivity would move it toward acceptance.
106	
107	---
108	
109	## Score: 4 / 6 (Weak Accept)
110	
111	The experimental design is sound in principle and the analytical depth is genuine, but critical baselines are missing, the mechanistic theory is underpowered (N=2), and several reporting gaps weaken trust. A revision addressing the major concerns would likely push this to a 5.
112	
113	## Confidence: 4 / 5 (High)
114	
115	I have expertise in contrastive learning, code retrieval, and hard negative mining. I have closely examined the paper's claims against the available evidence, including internal project artifacts. I am confident in my assessment of the methodological strengths and weaknesses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4ae0409-7aeb-4811-a6af-a984cda3c9ce",
  "isSidechain": false,
  "promptId": "31f911b9-2b77-479d-b3c3-7ac091b3c562",
  "type": "user",
  "uuid": "a73ac4bf-7b6b-4a27-8686-0916e112622a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/review_report.md",
      "content": "---\ndream_id: dream_20260514T075732\ntier: best\noverall_score: 4/6 Weak Accept\ntimestamp: 2026-05-14T08:33:59.100296+00:00\n---\n\n---\ndream_id: dream_20260514T075732\ntier: best\nreviewer: R1 (Methods and Experiments)\noverall_score: 4/6 Weak Accept\ntimestamp: 2026-05-14\n---\n\n# R1 Review: Methods and Experiments\n\n**Paper**: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n\n---\n\n## Summary\n\nThe paper presents a controlled comparison of three hard negative mining strategies (random, embedding-distance, dataflow-aware) for contrastive code retrieval, evaluated across two 3B-parameter encoders with 9 seeds each. The main findings are that embedding-distance mining consistently improves R@1 (+2.3pp Qwen, +1.7pp StarCoder), while dataflow-aware mining provides conditional benefit mediated by representation saturation (significant on Qwen, null on StarCoder). The experimental design is ambitious and the ablation suite is commendably broad, but several methodological concerns -- including the generalizability of the \"representation geometry\" theory from only 2 encoders, unrealistic retrieval pool sizes, missing baselines, and discrepancies between reported and actual result maturity -- undermine the strength of the claims.\n\n---\n\n## Strengths\n\n- **Exemplary experimental scale and statistical discipline.** 54 training runs (2 x 3 x 9) with paired bootstrap 95% CIs and explicit p-values for all main comparisons is well above the standard for this subfield. The paper does not rely on single-seed results, and the statistical testing is appropriate (bootstrap CIs, paired comparisons).\n\n- **Comprehensive ablation suite with clear analytical purpose.** Each ablation (temperature, hop depth, data scaling, fusion head, static vs. dynamic mining, binary vs. weighted dataflow) answers a specific methodological question rather than padding the paper. The dynamic mining baseline (Table 13) is particularly valuable for ruling out curriculum effects as a confound, and the fusion head ablation (Table 11) cleanly separates training-time mining value from inference-time feature injection.\n\n- **Honest reporting of null and conditional results.** The StarCoder dataflow null (p=0.62), the dataflow-vs-embed non-significance (p=0.134 on SWE-bench), and the diminishing returns at scale (Table 10) are reported transparently. Many papers would suppress these findings.\n\n- **Mechanistically motivated analysis.** The representation saturation explanation (pos_sim 0.986 vs. 0.799) goes beyond \"method X beats method Y\" to provide a predictive framework. If validated, the pos_sim diagnostic could be a genuinely useful practitioner tool.\n\n- **Clean experimental control.** The comparison holds all variables constant except the negative selection strategy -- same data, same encoder, same LoRA configuration, same training schedule. This is the correct way to study the effect of a single factor.\n\n- **SWE-bench Lite end-to-end evaluation.** Including downstream task evaluation, even though the results are positive, adds credibility beyond retrieval-only metrics.\n\n---\n\n## Weaknesses\n\n### Major\n\n1. **Generalizability from N=2 encoders is fundamentally limited (Section 5, Discussion).** The paper's central mechanistic claim -- that representation saturation mediates the effectiveness of structural negatives -- rests on exactly two data points: Qwen (saturated, pos_sim=0.986) and StarCoder (healthy, pos_sim=0.799). This is insufficient to establish a functional relationship. The two encoders also differ in pretraining data, pretraining objective, tokenizer, and model family, meaning the observed interaction could be driven by any of these confounds rather than representation geometry per se. The paper characterizes StarCoder2-3B as \"encoder-decoder\" (Section 3.4), but StarCoder2-3B is decoder-only (autoregressive), making the claimed \"architecturally distinct\" comparison misleading. At minimum, the paper needs (a) to correct the architectural characterization, and (b) to explicitly acknowledge that the saturation theory is an observation from N=2, not a validated mechanism.\n\n2. **Pool size of 50 candidates per query is unrealistically small (Section 3.4, implicitly).** Real-world repositories contain hundreds to thousands of files. A pool of 50 means the retriever is choosing among ~50 files, which inflates absolute recall numbers and may mask differences between strategies that would emerge at realistic pool sizes. The paper does not discuss this design choice or its implications for external validity. At pool=50, even random selection has a 2% baseline chance per candidate, making R@1 in the 0.50+ range less impressive. The RepoBench-R evaluation (Table 5) uses a different pool size but this is not specified.\n\n3. **Missing BM25 negative baseline.** The paper's headline narrative -- correcting CoCoHaNeRe's finding that embedding negatives harm code search -- attributes the prior result to BM25-proxy negatives mislabeled as embedding-distance. Yet the paper never runs actual BM25 negatives to demonstrate that the harm is BM25-specific. This is the single most important missing experiment given the framing. Without it, the \"correction\" is argumentative rather than empirical.\n\n4. **SWE-bench Lite results appear inflated relative to project state.** The paper reports +2.3pp (embedding) and +3.3pp (dataflow) resolve-rate gains over random on SWE-bench Lite, with bootstrap CIs excluding zero (Table 4). However, training data from the project's internal decision log (D018, D019, D026, D027) shows that as of the review date, the full M2 runs (9 seeds per strategy per encoder) are still in progress, with only seed 1 partially completed for each encoder. The pilot results (D017) from 1 seed show much smaller effects (+2.0pp Qwen embedding, with dataflow ranking dependent on checkpoint selection criterion). The SWE-bench results reported in the \"best\" paper variant are substantially stronger than the evidence base supports. If these are projected/simulated results, this must be disclosed.\n\n5. **No error bars or CIs on RepoBench-R results (Table 5).** RepoBench-R results are reported as single numbers without seeds, confidence intervals, or significance tests. Given that the reported deltas (e.g., +1.9pp R@1 for embedding on Qwen) are small, these may not be statistically distinguishable from zero. For a paper that emphasizes statistical rigor on the SWE-smith results, the asymmetry in reporting standards is conspicuous.\n\n6. **SWE-smith validation results mentioned but not shown.** Section 4 references SWE-smith validation R@1 as the primary evaluation metric, and the main tables (Tables 1-2) report these. But the actual validation set construction, size, and overlap with training data are not described. Given that the project logs show severe overfitting (best checkpoint at step 1000 out of 4242, D026), the validation protocol is critical for interpreting results, yet insufficiently documented.\n\n7. **34% structural coverage dilutes the dataflow signal (Section 3.3, implicit).** Only 34.3% of training instances receive dataflow-mined negatives; the remaining 65.7% fall back to alternative selection (presumably embedding or random). The reported +1.5pp dataflow improvement (Table 1, Qwen) averages over all instances including those that received no structural signal. Stratified results (structural-available vs. fallback) are absent. The true per-instance effect of dataflow mining on instances where it actually applies could be much larger (or much smaller) than the reported average. This stratification is essential for interpreting the result.\n\n### Minor\n\n8. **Table 6 \"<50 instances\" tier has N=1 repo.** Including a tier with a single repository is misleading and inflates the apparent trend. The correlation r=-0.41 (p=0.08) is heavily influenced by this outlier. The tier should either be removed or its N=1 status should be prominently flagged with appropriate caveats.\n\n9. **LoRA rank 16, 3 epochs may be insufficient.** With LoRA rank 16 (a low-rank adapter), the encoder's representational capacity to learn from different negative strategies is limited. Strategy differences might only emerge with fuller fine-tuning. The paper does not discuss whether LoRA's low-rank bottleneck could compress away the differences between strategies. The observed overfitting at step 1000 (1/4 through training) suggests the learning dynamics are dominated by regularization effects, not data effects.\n\n10. **Checkpoint selection criterion ambiguity.** The project history (D017) reveals that strategy rankings change depending on whether checkpoints are selected by best validation loss or best R@1. The paper does not specify which criterion is used. Given that this choice can reverse the ordering of strategies (dataflow > embedding by peak R@1 vs. embedding > dataflow by val_loss for Qwen, per D017), this is a material omission.\n\n11. **All references render as [?].** The bibliography is broken -- every citation in the compiled paper appears as [?]. This makes it impossible to verify the related work coverage or the CoCoHaNeRe critique. For a paper whose central claim involves correcting a prior work's methodology, unresolvable citations are a serious presentation issue.\n\n12. **Number of negatives per query (K) not stated.** The method section defines \"select k negatives\" but never specifies the value of K used in experiments. This is a basic reproducibility gap.\n\n13. **Overfitting patterns not reported.** Project logs show train_loss dropping to 0.04 while val_loss remains at 0.52 (D026), yet the paper does not discuss overfitting or show learning curves. Strategy-specific overfitting patterns could be informative (e.g., does dataflow overfit faster due to fewer unique negatives?).\n\n---\n\n## Questions for Authors\n\n1. **SWE-bench result provenance.** Tables 3-4 report SWE-bench Lite results with bootstrap CIs excluding zero for embedding and dataflow vs. random. Are these from completed 9-seed runs, or projected from pilot data? If the full M2 runs are still in progress, what is the actual evidence base for these numbers?\n\n2. **Checkpoint selection criterion.** Which checkpoint is used for the main results -- best by validation loss, or best by R@1? Your project logs (D017) show these criteria produce different strategy rankings. Have you reported both, and if not, why?\n\n3. **Stratified dataflow results.** What is the R@1 delta for the ~34% of instances that actually receive dataflow-mined negatives vs. the ~66% that fall back? This decomposition is essential for understanding whether the dataflow signal is strong-but-diluted or weak-throughout.\n\n4. **BM25 baseline omission.** The paper's narrative hinges on CoCoHaNeRe using \"BM25-proxy negatives mislabeled as embedding-distance.\" Can you provide specific textual evidence from CoCoHaNeRe supporting this claim? And why not run BM25 negatives as a fourth strategy to close the argument empirically?\n\n5. **Pool size sensitivity.** How do strategy differences change as pool size increases from 50 to 200 or 500? If differences shrink at realistic pool sizes, this would substantially weaken the practical relevance of the findings.\n\n---\n\n## Minor Issues\n\n- Section 3.4: StarCoder2-3B is described as \"Encoder-decoder\" -- it is decoder-only. Correct throughout.\n- Table 6 (stratified analysis in the best paper) vs. Table 6 (median paper): the two variants report completely different stratification schemes (by file count vs. by instance count), suggesting the analysis is not yet stable.\n- Abstract line \"SWE-bench Lite end-to-end evaluation with a Qwen3.6-27B agent\" -- only Qwen retriever checkpoints are used for SWE-bench, not StarCoder. This asymmetry should be acknowledged.\n- The paper name \"StructFuse\" implies a fusion system, but the best-performing approach is pure embedding mining without fusion (Table 11 shows fusion slightly degrades performance). The name is misleading.\n- Hop depth ablation (Table 9): the \"best\" paper reports clean improvements (2-hop optimal), while the median paper (Table 9) reports differences \"within noise range.\" The discrepancy in framing across tiers suggests cherry-picking of presentation.\n- Section 3.3 reports \"131 SWE-smith repositories\" but only \"123/131 repos producing valid output\" -- the 8 failures are not analyzed.\n\n---\n\n## Overall Assessment\n\nThis paper tackles a genuinely important question -- what makes hard negatives work for code retrieval -- with commendable experimental rigor in its design (9 seeds, bootstrap CIs, extensive ablations). The representation saturation insight, if validated on more encoders, could become a useful diagnostic tool for practitioners. However, the paper is undermined by (a) the N=2 encoder limitation that makes the \"representation geometry\" theory an observation rather than a validated mechanism, (b) missing baselines (BM25) that are critical to the headline narrative, (c) potential discrepancies between reported results and actual experimental maturity, (d) unrealistic pool sizes that limit external validity, and (e) several reporting gaps (no CIs on RepoBench, no stratification by structural coverage, checkpoint criterion unspecified). The paper is above-average in experimental discipline but below the bar for confident acceptance at a top venue in its current form. Addressing the BM25 baseline, the stratified analysis, and the pool size sensitivity would move it toward acceptance.\n\n---\n\n## Score: 4 / 6 (Weak Accept)\n\nThe experimental design is sound in principle and the analytical depth is genuine, but critical baselines are missing, the mechanistic theory is underpowered (N=2), and several reporting gaps weaken trust. A revision addressing the major concerns would likely push this to a 5.\n\n## Confidence: 4 / 5 (High)\n\nI have expertise in contrastive learning, code retrieval, and hard negative mining. I have closely examined the paper's claims against the available evidence, including internal project artifacts. I am confident in my assessment of the methodological strengths and weaknesses.",
      "numLines": 115,
      "startLine": 1,
      "totalLines": 115
    }
  },
  "sourceToolAssistantUUID": "f4ae0409-7aeb-4811-a6af-a984cda3c9ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16 · 2026-05-14T16:27:21.949Z_

````json
{
  "parentUuid": "a73ac4bf-7b6b-4a27-8686-0916e112622a",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**structfuse-context**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"structfuse-context\")` 或 `load_project_config(\"structfuse-context\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/structfuse-context/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "122f3bda-dcbe-4cd7-8257-df5643ac4ef9",
  "timestamp": "2026-05-14T16:27:21.949Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：全 18 runs 复现 pilot pattern，BM25 baseline 关闭 CoCoHaNeRe 论证，三条 claim 原样成立 核心假设：['embedding-random R@1 delta 在两个 encoder 上 95% CI 下界 > 0', 'dataflow-random R@…",
  "leafUuid": "122f3bda-dcbe-4cd7-8257-df5643ac4ef9",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic empirical validation of hard negative mining strategies for code retrieval",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e"
}
```

---

### Assistant

_source line 19 · 2026-05-14T16:28:18.493Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the project. Let me synthesize all the information and generate the detailed predicted data for every "planned" experiment in the experiment_plan, under the "best" tier assumption.

Let me list all the planned experiments:
1. plan_003: SWE-bench Lite eval
2. plan_004: RepoBench-R cross-file retrieval (with multi-seed CIs)
3. plan_005: Stratified analysis (extended: structural-available vs fallback + neg_difficulty quartile)
4. plan_007: Ablation: 1-hop vs 2-hop vs 3-hop


5. plan_008: Ablation: training data size scaling
6. plan_009: Ablation: fusion head
7. plan_010: Ablation: dataflow-distance weighted vs binary
8. plan_011: Failure analysis
9. plan_012: Qualitative examples
10. plan_014: Temperature ablation
11. plan_015: Dynamic mining baseline
12. plan_016: Bootstrap CI for SWE-bench
13. plan_017: Inference-time graph method comparison (analysis only, mostly done)
14. plan_018: BM25 negative baseline
15. plan_019: Pool size sensitivity

I'll generate predicted data for all of these under the "best" tier assumption.

Looking at the 18 replication runs that follow the pilot pattern, the BM25 baseline effectively addresses the CoCoHaNeRe concern, and the three main claims hold up. Now I'm examining the metric ranges across different model configurations—embedding-based approaches show consistent gains of 1-2.5 points, dataflow methods vary more widely from -1 to 1.5 points, while BM25 shows negative deltas around -4 to -1.5, and the downstream task improvements on SWE-bench and RepoBench range from 1.5 to 4 points.

I'm now constructing the detailed YAML specification with predicted values for the best-tier experiments, starting with m2_full where I'm setting Qwen's random baseline around 0.545, with embedding-based retrieval pushing it to roughly 0.565 and dataflow methods to about 0.555.

For StarCoder, I'm working with a lower baseline around 0.460, where embedding retrieval gains about 1.5 percentage points but dataflow shows minimal improvement. Moving into plan_003 for SWE-bench Lite evaluation, I'm estimating the embedding strategy yields a 2.5pp improvement over random while dataflow reaches 3.2pp, and I'm starting to map out plan_004's RepoBench-R results with multi-seed confidence intervals.

Now looking at the remaining experiments: RepoBench shows embedding gains of 1.9pp for Qwen and 1.4pp for StarCoder with tight confidence intervals, stratified analysis reveals clear performance separation across repository characteristics, the hop depth ablation confirms 2-hop is optimal, data scaling from 1K to 5K instances shows consistent monotonic gains with stable strategy rankings, the fusion head ablation indicates embedding-only retrieval performs as well as or better than combined approaches, and finally the dataflow-distance weighting shows marginal improvements with weighted variants slightly outperforming binary versions.

For the remaining analyses, I'm planning failure categorization across 50 cases to demonstrate where dataflow helps, qualitative examples to illustrate the approach, temperature sensitivity checks showing stable rankings across τ values, a comparison of static versus dynamic mining to rule out curriculum effects, bootstrap confidence intervals for SWE-bench excluding zero, BM25 negative baselines showing a 2.5pp penalty that settles the CoCoHaNeRe debate, and pool size sensitivity tests.

Now I'm working through the specific numbers for each benchmark. For SWE-bench Lite, the random baseline sits around 22%, embedding retrieval gets to 24.3% with a 2.3pp gain, and dataflow pushes it to 25.3% for another 3.3pp—the improvement comes from how dataflow captures cross-function dependencies that matter in patch contexts. I'm starting to fill in the detailed results for RepoBench-R as well. → differences smaller (ceiling effect)
- test_hard: pool ~18 → more room for differentiation
- Qwen embedding vs random on test_hard: +2.1pp R@1
- StarCoder embedding vs random on test_hard: +1.5pp R@1
- With CIs from 9 seeds

plan_005 (Stratified):
- structural-available stratum (34%): dataflow advantage amplified (+2.8pp Qwen)
- fallback stratum (66%): dataflow ≈ embedding (no structural signal)
- neg_difficulty Q4 (hardest quartile): largest dataflow gain

plan_007 (Hop depth):
- 1-hop: too restrictive, lower coverage, +0.4pp
- 2-hop: optimal balance, +1.0pp
- 3-hop: introduces noise, +0.7pp

plan_008 (Data size):
- 1K: unstable, high variance
- 3K: moderate, strategy ranking holds
- 5K: best, full signal

plan_009 (Fusion head):
- embedding-only: best or tied
- structural-features-only: worse
- combined: slightly below embedding-only (interference)

plan_010 (Weighted vs binary):
- weighted: +0.3pp over binary on Qwen
- binary: simpler, nearly as good

plan_011 (Failure analysis):
- 50 failures → categories

plan_012 (Qualitative):
- 5-10 compelling examples

plan_014 (Temperature):
- τ=0.05: all strategies improve, ranking preserved
- τ=0.1: default, baseline results
- τ=0.2: strategies converge slightly, ranking preserved

Now I'm working through the remaining ablations—data size shows 5K gives the cleanest signal while 1K is too noisy, the fusion head experiments reveal embedding-only performs best with structural features actually hurting when combined, and temperature sensitivity is minimal across the range tested with strategy rankings staying consistent.

For the dynamic mining comparison, the results are nearly identical to static approaches with only a 0.2pp difference, which rules out curriculum learning as a confound. The bootstrap confidence intervals on SWE-bench show embedding and dataflow both significantly outperform random with tight p-values, and the BM25 baseline actually underperforms random retrieval on both models, which settles the CoCoHaNeRe debate. Pool size effects are more pronounced on the harder test set where there's more room for differentiation.

Now I'm checking the final numbers across both models to ensure consistency before writing out the YAML configuration. The Qwen results show embedding gains of 2.0pp and dataflow at 1.0pp over random, while StarCoder shows slightly smaller deltas at 1.5pp for embedding, with all estimates having tight standard errors. All the metrics are checking out within their expected ranges, so I'm ready to generate the full output now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "122f3bda-dcbe-4cd7-8257-df5643ac4ef9",
  "isSidechain": false,
  "requestId": "req_011Cb2mvvJ6dcf49edM1U3mf",
  "type": "assistant",
  "uuid": "c8ee7631-2a5d-4dcd-a2b9-c56d823da71d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pmrmQAf7f8JHXhpZETQ1L",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11544,
      "cache_read_input_tokens": 32493,
      "output_tokens": 17808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17808,
          "cache_read_input_tokens": 32493,
          "cache_creation_input_tokens": 11544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11544
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

_source line 20 · 2026-05-14T16:32:58.997Z_

```yaml
tier: best
narrative_guidance: >
  全 18 runs（9 seeds × 2 encoders × 3 strategies）完整复现 pilot pattern。
  Embedding mining 在两个 encoder 上均显著优于 random（Qwen +2.0pp, StarCoder +1.5pp, 95% CI 下界 > 0）。
  Dataflow 在 Qwen 上条件性获益（+1.0pp, CI 下界 > 0），StarCoder 上无显著差异（-0.2pp, CI 含零）。
  BM25 baseline 实证关闭 CoCoHaNeRe 论证（BM25 vs random: Qwen -2.5pp, StarCoder -2.7pp）。
  SWE-bench Lite downstream +2.5pp embedding, +3.2pp dataflow resolve rate delta。
  三条 claim 原样成立，EMNLP Main 强投 framing 无需调整。
  M2 full anchors — Qwen random R@1=0.545, embedding=0.565, dataflow=0.555;
  StarCoder random R@1=0.460, embedding=0.475, dataflow=0.458。

imagined_experiments:
  # ============================================================
  # plan_003: SWE-bench Lite end-to-end evaluation
  # ============================================================
  - name: "SWE-bench Lite End-to-End Evaluation"
    plan_id: "plan_003"
    description: >
      3 strategies × best Qwen checkpoint, Qwen3.6-27B agent, 300 SWE-bench Lite instances.
      Retriever 提供 top-k context files，agent 生成 patch，评估 resolve rate。
    expected_results:
      random_resolve_rate: 0.220
      random_resolved_count: 66
      embedding_resolve_rate: 0.245
      embedding_resolved_count: 73
      dataflow_resolve_rate: 0.252
      dataflow_resolved_count: 76
      embedding_minus_random_pp: 2.5
      dataflow_minus_random_pp: 3.2
      dataflow_minus_embedding_pp: 0.7
      total_instances: 300
      retriever_top_k: 5
      agent_model: "Qwen3.6-27B"
    result_rationale: >
      Embedding retriever 在 SWE-bench 上提升 +2.5pp，因为 bug-fix patch 通常涉及与 issue 描述
      语义相似但非完全匹配的文件——embedding mining 训练使 retriever 更擅长区分"近似但无关"
      与"近似且相关"的文件。Dataflow 额外提升 +0.7pp（总 +3.2pp vs random）因为 SWE-bench
      patch 经常跨函数/跨模块（约 40% 涉及 caller-callee 关系），dataflow negatives 训练使
      retriever 理解"调用链上的文件更可能共同出现在 patch 中"。Delta 幅度从 retrieval R@1
      的 +2.0/+1.0pp 放大到下游 resolve rate 的 +2.5/+3.2pp，符合检索质量在端到端任务中
      的杠杆效应——正确检索一个关键文件可以使原本完全失败的 patch 变为可解决。
      效果幅度在 swebench_resolve_rate_delta_pp [1.5, 4.0] 范围内。
    tables:
      - name: "Table 4: SWE-bench Lite Resolve Rate"
        columns: ["Strategy", "Resolved", "Total", "Rate (%)", "Δ vs Random (pp)"]
        rows:
          - ["random", 66, 300, 22.0, "—"]
          - ["embedding", 73, 300, 24.3, "+2.3"]
          - ["dataflow", 76, 300, 25.3, "+3.3"]
      - name: "Table 4b: SWE-bench by Patch Complexity"
        columns: ["Patch Type", "N", "random (%)", "embedding (%)", "dataflow (%)"]
        rows:
          - ["single-file", 189, 28.0, 30.7, 30.2]
          - ["multi-file", 111, 11.7, 14.4, 17.1]
    figures_description:
      - "Fig 5: SWE-bench resolve rate bar chart (3 strategies) with bootstrap 95% CI whiskers"
      - "Fig 5b: Scatter plot — retrieval R@1 rank vs resolve rate per instance, colored by strategy"
    analysis: >
      Multi-file patches（占 37%）是 dataflow 拉开差距的主要来源：dataflow 在 multi-file
      上 +5.4pp vs random，远大于 single-file 的 +2.2pp。这与 Claim 2 一致——dataflow
      negatives 使 retriever 更好地理解跨模块依赖。Embedding vs random 在 multi-file
      上也有 +2.7pp，说明更难的 negatives 普遍有益。总体 resolve rate 22-25% 与
      SweRank/SWE-Fixer 文献报告的 retriever-only baseline 一致。

  # ============================================================
  # plan_004: RepoBench-R cross-file retrieval
  # ============================================================
  - name: "RepoBench-R Cross-File Retrieval with Multi-Seed CIs"
    plan_id: "plan_004"
    description: >
      RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 9 seeds × 3 strategies
      × 2 encoders，报告 R@1 均值 + 95% bootstrap CI。
    expected_results:
      qwen_test_hard:
        random_R1_mean: 0.621
        random_R1_ci: [0.614, 0.628]
        embedding_R1_mean: 0.642
        embedding_R1_ci: [0.634, 0.650]
        dataflow_R1_mean: 0.633
        dataflow_R1_ci: [0.624, 0.642]
        embedding_minus_random_pp: 2.1
        dataflow_minus_random_pp: 1.2
      qwen_test_easy:
        random_R1_mean: 0.843
        embedding_R1_mean: 0.855
        dataflow_R1_mean: 0.850
        embedding_minus_random_pp: 1.2
      starcoder_test_hard:
        random_R1_mean: 0.574
        random_R1_ci: [0.566, 0.582]
        embedding_R1_mean: 0.589
        embedding_R1_ci: [0.580, 0.598]
        dataflow_R1_mean: 0.572
        dataflow_R1_ci: [0.562, 0.582]
        embedding_minus_random_pp: 1.5
        dataflow_minus_random_pp: -0.2
      starcoder_test_easy:
        random_R1_mean: 0.812
        embedding_R1_mean: 0.822
        dataflow_R1_mean: 0.810
      repobench_R1_delta_pp_embedding_avg: 1.8
      bootstrap_CI_width_R1_pp_avg: 1.2
    result_rationale: >
      RepoBench-R 是 cross-file completion 任务，pool 更小（6-18），绝对 R@1 更高。
      Embedding mining 在两个 encoder 上均显著提升 test_hard R@1（Qwen +2.1pp, StarCoder +1.5pp），
      因为 pool=18 仍有足够 distractors 使 mining 质量差异体现。Test_easy pool=6 接近
      ceiling，delta 被压缩但方向一致。Dataflow 在 Qwen test_hard 上 +1.2pp 但 CI 刚好
      排除零，StarCoder 上无效（-0.2pp，CI 含零）——与 SWE-smith 上的 encoder-strategy
      interaction 完全一致，说明 pattern 跨 benchmark 稳定。CI 宽度 ~1.2pp 在
      bootstrap_CI_width_R1_pp [0.5, 2.0] 范围内，9 seeds 提供足够统计功效。
    tables:
      - name: "Table 5: RepoBench-R Results (test_hard, pool≈18)"
        columns: ["Encoder", "Strategy", "R@1 (%)", "95% CI", "Δ vs Random (pp)"]
        rows:
          - ["Qwen", "random", 62.1, "[61.4, 62.8]", "—"]
          - ["Qwen", "embedding", 64.2, "[63.4, 65.0]", "+2.1"]
          - ["Qwen", "dataflow", 63.3, "[62.4, 64.2]", "+1.2"]
          - ["StarCoder", "random", 57.4, "[56.6, 58.2]", "—"]
          - ["StarCoder", "embedding", 58.9, "[58.0, 59.8]", "+1.5"]
          - ["StarCoder", "dataflow", 57.2, "[56.2, 58.2]", "−0.2"]
    figures_description:
      - "Fig 6: RepoBench-R R@1 grouped bar chart (2 encoders × 3 strategies) with CI whiskers, test_easy vs test_hard side by side"
    analysis: >
      Cross-benchmark 一致性是 best tier 的关键证据：embedding mining 在 SWE-smith 和
      RepoBench-R 上均显著提升两个 encoder，dataflow 条件性获益仅限 Qwen。这排除了
      "结果仅限单一 benchmark" 的 reviewer concern。Test_easy 上 delta 被压缩（pool=6
      ceiling effect）是预期行为，反向验证了 pool size 对绝对效果幅度的调节作用。

  # ============================================================
  # plan_005: Stratified analysis (extended)
  # ============================================================
  - name: "Stratified Analysis with Structural Coverage & Neg Difficulty Quartiles"
    plan_id: "plan_005"
    description: >
      5 层分层分析：repo size / pool size / query-positive similarity / structural data
      availability (34% vs 66%) / neg_difficulty quartile。使用 M2 best checkpoints
      在 SWE-smith validation 上重新评估。
    expected_results:
      stratum_structural_available:
        with_dataflow_34pct:
          qwen_dataflow_minus_random_pp: 2.8
          qwen_dataflow_minus_embedding_pp: 1.3
          starcoder_dataflow_minus_random_pp: 0.1
          n_instances: ~5200
        fallback_66pct:
          qwen_dataflow_minus_random_pp: 0.1
          qwen_dataflow_minus_embedding_pp: -0.2
          starcoder_dataflow_minus_random_pp: -0.3
          n_instances: ~10000
      stratum_neg_difficulty_quartile:
        Q1_easiest:
          qwen_embedding_minus_random_pp: 0.8
          qwen_dataflow_minus_random_pp: 0.3
        Q2:
          qwen_embedding_minus_random_pp: 1.5
          qwen_dataflow_minus_random_pp: 0.7
        Q3:
          qwen_embedding_minus_random_pp: 2.4
          qwen_dataflow_minus_random_pp: 1.2
        Q4_hardest:
          qwen_embedding_minus_random_pp: 3.2
          qwen_dataflow_minus_random_pp: 2.1
      stratum_repo_size:
        small_lt50: { embedding_delta_pp: 2.8, n: ~500 }
        medium_50_200: { embedding_delta_pp: 2.2, n: ~4100 }
        large_200_500: { embedding_delta_pp: 1.8, n: ~5500 }
        xlarge_500plus: { embedding_delta_pp: 1.6, n: ~5100 }
      stratum_pool_size:
        pool_lt20: { embedding_delta_pp: 1.0, dataflow_delta_pp: 0.3 }
        pool_20_50: { embedding_delta_pp: 2.1, dataflow_delta_pp: 1.0 }
        pool_gt50: { embedding_delta_pp: 2.5, dataflow_delta_pp: 1.4 }
      stratum_query_pos_sim:
        high_sim_gt095: { embedding_delta_pp: 2.6, dataflow_delta_pp: 1.8 }
        medium_sim_085_095: { embedding_delta_pp: 1.9, dataflow_delta_pp: 0.8 }
        low_sim_lt085: { embedding_delta_pp: 1.2, dataflow_delta_pp: 0.2 }
    result_rationale: >
      Structural-available stratum（34%）上 dataflow 优势放大到 +2.8pp（Qwen），因为这些
      instance 实际接收了 dataflow-disconnected negatives——真实训练信号未被 fallback 稀释。
      Fallback stratum（66%）上 dataflow ≈ embedding（±0.2pp），因为 fallback 时 dataflow
      策略退化为 embedding 或 random 选择，无结构信号注入。这一分解直接回应 reviewer 关于
      "34% coverage 稀释 signal" 的 concern——真实 per-instance 效果是 +2.8pp 而非 pooled
      +1.0pp。Neg_difficulty Q4（最难 quartile）上 delta 最大（embedding +3.2pp, dataflow
      +2.1pp），符合 representation saturation 理论——Qwen 在高 pos_sim 区域最需要 harder
      negatives，而 Q4 恰好是 margin 最小、分辨最难的 instances。Q1（最容易）delta 最小
      因为 random negatives 已经足够容易区分。Repo size 上 small repo delta 更大因为
      小 repo 的 candidate pool 更集中，mining 策略差异更容易体现。
    tables:
      - name: "Table 7: Stratified R@1 Delta by Structural Data Availability (Qwen)"
        columns: ["Stratum", "N", "random R@1", "embedding R@1", "dataflow R@1", "df−rand (pp)"]
        rows:
          - ["With dataflow (34%)", "~5.2K", 53.1, 55.4, 55.9, "+2.8"]
          - ["Fallback (66%)", "~10K", 55.2, 57.3, 55.3, "+0.1"]
          - ["Overall", "~15.2K", 54.5, 56.5, 55.5, "+1.0"]
      - name: "Table 7b: R@1 Delta by Neg Difficulty Quartile (Qwen)"
        columns: ["Quartile", "margin_mean", "emb−rand (pp)", "df−rand (pp)"]
        rows:
          - ["Q1 (easiest)", 0.142, "+0.8", "+0.3"]
          - ["Q2", 0.078, "+1.5", "+0.7"]
          - ["Q3", 0.031, "+2.4", "+1.2"]
          - ["Q4 (hardest)", 0.008, "+3.2", "+2.1"]
    figures_description:
      - "Fig 7: Heatmap — R@1 delta (strategy × stratum), separate panels for Qwen and StarCoder"
      - "Fig 8: Neg difficulty quartile vs R@1 delta line plot, 3 strategies overlaid"
    analysis: >
      Stratified analysis 提供了论文中最强的 mechanistic 证据。Neg_difficulty Q4 的 +3.2pp
      embedding delta 是 overall +2.0pp 的 1.6 倍——越难的 instances 从 harder negatives
      获益越多，这是 representation saturation 理论的直接预测。Structural-available vs
      fallback 分解消除了 "diluted signal" concern 并揭示 dataflow 的真实 per-instance
      效果（+2.8pp）远大于 pooled 报告值。

  # ============================================================
  # plan_007: Hop depth ablation
  # ============================================================
  - name: "Call-Graph Hop Depth Ablation (1/2/3-hop)"
    plan_id: "plan_007"
    description: >
      比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量的影响。
      Qwen encoder, 1 seed, SWE-smith validation。
    expected_results:
      hop_1:
        R1: 0.548
        connected_coverage_pct: 12.4
        negatives_per_query_mean: 18.2
      hop_2:
        R1: 0.555
        connected_coverage_pct: 34.3
        negatives_per_query_mean: 31.7
      hop_3:
        R1: 0.551
        connected_coverage_pct: 58.6
        negatives_per_query_mean: 42.1
      optimal_hop: 2
      hop2_minus_hop1_pp: 0.7
      hop3_minus_hop2_pp: -0.4
    result_rationale: >
      2-hop 是最优平衡点。1-hop 太保守——仅 12.4% coverage 意味着大部分 instance 没有足够的
      connected 节点来定义 "disconnected" negatives，退化为 random。3-hop 过于宽松——58.6%
      coverage 下 "disconnected" 的定义变得太窄，许多语义相关但间接连接的文件被错误排除在
      negative pool 外，引入噪声。2-hop 的 34.3% coverage（与 M1 extraction 的 structural
      data rate 一致）在 "enough connected nodes to define meaningful disconnection" 和
      "disconnected set still contains genuinely unrelated files" 之间取得平衡。
    tables:
      - name: "Table 9: Hop Depth Ablation (Qwen, dataflow strategy)"
        columns: ["Hops", "Coverage (%)", "Neg/query", "R@1 (%)", "Δ vs 2-hop (pp)"]
        rows:
          - [1, 12.4, 18.2, 54.8, "−0.7"]
          - [2, 34.3, 31.7, 55.5, "—"]
          - [3, 58.6, 42.1, 55.1, "−0.4"]
    figures_description:
      - "Fig S1: Hop depth vs R@1 line plot with coverage % on secondary y-axis"
    analysis: >
      2-hop optimal 符合 inter-procedural dataflow 的语义：1-hop = 直接 caller/callee，
      2-hop = caller 的 caller 或 callee 的 callee（一层间接调用），3-hop 开始包含
      过于间接的关系。论文可以强调 2-hop 选择有 principled 依据而非纯粹 empirical tuning。

  # ============================================================
  # plan_008: Training data size scaling
  # ============================================================
  - name: "Training Data Size Scaling (1K/3K/5K)"
    plan_id: "plan_008"
    description: >
      固定 Qwen encoder + embedding strategy，训练数据从 1K / 3K / 5K instances 增长，
      观察 R@1 变化和策略排名稳定性。
    expected_results:
      size_1K:
        random_R1: 0.510
        embedding_R1: 0.522
        dataflow_R1: 0.515
        embedding_minus_random_pp: 1.2
        seed_std: 0.015
      size_3K:
        random_R1: 0.532
        embedding_R1: 0.550
        dataflow_R1: 0.541
        embedding_minus_random_pp: 1.8
        seed_std: 0.010
      size_5K:
        random_R1: 0.545
        embedding_R1: 0.565
        dataflow_R1: 0.555
        embedding_minus_random_pp: 2.0
        seed_std: 0.008
      ranking_stable: true
      monotonic_improvement: true
    result_rationale: >
      策略排名在 1K/3K/5K 三个尺度上保持一致（embedding > dataflow > random），但 delta
      幅度随数据量增大而增大——1K 时 +1.2pp，5K 时 +2.0pp。这是因为更大的训练集提供更多
      diverse negatives，使 mining 策略的差异更充分地体现。1K 时 seed 方差较大（std=0.015）
      因为 negative 多样性不足，个别 seed 的 negative 采样偶然性影响结果。5K 时方差收敛
      （std=0.008），mining 策略的信号超过采样噪声。No diminishing returns at 5K suggests
      further scaling could help, but is beyond scope。
    tables:
      - name: "Table 10: Data Size Scaling (Qwen)"
        columns: ["Size", "random R@1", "embedding R@1", "dataflow R@1", "emb−rand (pp)", "σ across seeds"]
        rows:
          - ["1K", 51.0, 52.2, 51.5, "+1.2", 1.5]
          - ["3K", 53.2, 55.0, 54.1, "+1.8", 1.0]
          - ["5K", 54.5, 56.5, 55.5, "+2.0", 0.8]
    figures_description:
      - "Fig S2: R@1 vs training size for 3 strategies, with shaded seed variance bands"
    analysis: >
      Monotonic scaling + stable ranking 表明结果不是 small-data artifact。5K 时未见
      diminishing returns，暗示更大数据集可能进一步放大差异。这对 reviewer "effect size
      marginal" concern 有价值——delta 仍在增长，当前 +2.0pp 是下界而非上界。

  # ============================================================
  # plan_009: Fusion head ablation
  # ============================================================
  - name: "Fusion Head Ablation"
    plan_id: "plan_009"
    description: >
      比较 embedding-only / structural-features-only / combined fusion head，
      隔离 training-time mining 价值与 inference-time feature injection。
    expected_results:
      embedding_only:
        qwen_R1: 0.565
        starcoder_R1: 0.475
      structural_features_only:
        qwen_R1: 0.498
        starcoder_R1: 0.421
      combined_fusion:
        qwen_R1: 0.561
        starcoder_R1: 0.472
      embedding_only_minus_combined_pp: 0.4
      conclusion: "mining > fusion; structural features at inference add noise"
    result_rationale: >
      Embedding-only（仅用 embedding mining 训练的 retriever，inference 时不注入结构特征）
      表现最好或 tied with combined。Combined fusion 略低 0.4pp 因为 inference-time
      structural features 引入了不精确的 CodeQL connectivity 信号——recall 某些 CodeQL
      extraction 失败的 instance 反而被错误降权。Structural-features-only（不用 mining 训练，
      仅在 inference 注入结构特征）远低于 embedding-only（-6.7pp Qwen），证明核心价值在
      training-time negative mining 而非 inference-time feature engineering。
      这一结果对 paper framing 极为重要：StructFuse 的贡献是 mining strategy，不是 fusion。
    tables:
      - name: "Table 11: Fusion Head Ablation"
        columns: ["Configuration", "Qwen R@1 (%)", "StarCoder R@1 (%)"]
        rows:
          - ["embedding-only (ours)", 56.5, 47.5]
          - ["structural-features-only", 49.8, 42.1]
          - ["combined fusion", 56.1, 47.2]
    figures_description:
      - "Fig S3: Ablation bar chart comparing 3 fusion configurations"
    analysis: >
      训练时注入 structural signal 通过 negative mining（间接信号）比 inference 时直接注入
      structural features（直接信号）更有效。可能原因：mining 让 encoder 自己学习结构相关的
      representation，而直接注入 features 绕过了 encoder 的学习过程，且 CodeQL 34% coverage
      意味着 66% instance 在 inference 时收到 zero-vector structural features，引入 noise。

  # ============================================================
  # plan_010: Weighted vs binary dataflow negatives
  # ============================================================
  - name: "Dataflow-Distance Weighted vs Binary Negatives"
    plan_id: "plan_010"
    description: >
      比较 binary connected/disconnected 与 dataflow-distance weighted negative sampling。
      Weighted: disconnected 且 hop-distance 更远的文件被赋予更高采样概率。
    expected_results:
      binary_qwen_R1: 0.555
      weighted_qwen_R1: 0.558
      binary_starcoder_R1: 0.458
      weighted_starcoder_R1: 0.459
      weighted_minus_binary_qwen_pp: 0.3
      weighted_minus_binary_starcoder_pp: 0.1
    result_rationale: >
      Weighted 在 Qwen 上仅微弱提升 +0.3pp（不显著），StarCoder 上几乎无差异。
      原因：binary disconnected/connected 已经捕获了最关键的 structural distinction——
      "是否在调用链上"。进一步按 hop distance 加权引入的额外信号被 noise 抵消：距离更远
      不一定意味着更好的 negative（一个完全无关的 utility 文件可能 hop=∞ 但也是 trivial negative）。
      Binary 的简洁性是优势——fewer hyperparameters, same effect。
    tables:
      - name: "Table S1: Weighted vs Binary Dataflow Negatives"
        columns: ["Method", "Qwen R@1 (%)", "StarCoder R@1 (%)", "Δ vs Binary (pp)"]
        rows:
          - ["Binary (default)", 55.5, 45.8, "—"]
          - ["Distance-weighted", 55.8, 45.9, "+0.3 / +0.1"]
    figures_description: []
    analysis: >
      Binary is sufficient — complexity of weighted sampling not justified.
      论文可在 ablation section 用一句话报告这一 negative result，
      强化 "simple binary structural signal is the key insight" 的 narrative。

  # ============================================================
  # plan_011: Failure analysis
  # ============================================================
  - name: "SWE-bench Failure Analysis (50 cases)"
    plan_id: "plan_011"
    description: >
      从 random retriever 的 SWE-bench 失败案例中抽样 50 个，人工分类失败原因，
      标注 dataflow 信号是否可能帮助。
    expected_results:
      total_analyzed: 50
      category_breakdown:
        retrieval_failure_wrong_files: 22
        retrieval_success_but_agent_fail: 15
        insufficient_context_window: 7
        test_environment_issue: 4
        ambiguous_issue_description: 2
      dataflow_could_help:
        yes: 14
        partially: 5
        no: 31
      dataflow_help_rate: 0.28
      key_pattern: >
        14/22 retrieval failures involve cross-module dependencies where the gold
        file is a caller/callee of a retrieved-but-wrong file — dataflow connectivity
        would directly address these.
    result_rationale: >
      50 个失败中 22 个是 retrieval failure（检索到错误文件），其中 14 个涉及跨模块依赖——
      被检索的文件和 gold 文件有高文本相似度但分属不同 call chain。Dataflow negatives 训练
      恰好针对这类 confound。15 个 retrieval success but agent fail 说明 retrieval 不是
      唯一瓶颈——agent 的 patch 生成能力也是限制因素。这为论文提供了 "ceiling analysis"：
      即使 perfect retrieval，resolve rate 上限约 85%（15% 是 agent 能力限制）。
    tables:
      - name: "Table S2: Failure Category Breakdown"
        columns: ["Category", "Count", "% of 50", "Dataflow Could Help?"]
        rows:
          - ["Retrieval: wrong files", 22, 44, "14/22 (64%)"]
          - ["Retrieval OK, agent fail", 15, 30, "N/A"]
          - ["Context window limit", 7, 14, "5/7 partially"]
          - ["Test env issue", 4, 8, "No"]
          - ["Ambiguous issue", 2, 4, "No"]
    figures_description:
      - "Fig S4: Sankey diagram — failure flow from retrieval stage to resolution outcome"
    analysis: >
      28% of failures could benefit from dataflow signal, consistent with the observed
      +3.2pp resolve rate improvement. The 64% rate within retrieval failures confirms
      that cross-module dependency is the primary retrieval challenge, directly supporting
      Claim 2's motivation.

  # ============================================================
  # plan_012: Qualitative examples
  # ============================================================
  - name: "Qualitative Examples (5-10 cases)"
    plan_id: "plan_012"
    description: >
      从 SWE-bench 和 SWE-smith 中选取 5-10 个 dataflow negatives 改变检索结果的典型案例，
      展示 structural signal 的具体作用机制。
    expected_results:
      total_examples: 8
      example_categories:
        caller_callee_confusion: 3
        utility_file_distraction: 2
        cross_module_import_chain: 2
        test_file_vs_source: 1
      illustrative_example:
        issue: "django/django#12345 — QuerySet.filter() returns wrong results with nested Q objects"
        random_retriever_top1: "django/db/models/query.py (text match on 'filter')"
        dataflow_retriever_top1: "django/db/models/sql/query.py (actual SQL generation called by filter)"
        gold: "django/db/models/sql/query.py"
        explanation: >
          Random retriever picks query.py (contains 'filter' method signature) but the bug is in
          sql/query.py (the downstream SQL builder called by filter). Dataflow training teaches
          the model that sql/query.py is structurally connected to query.py via 2-hop call chain,
          making it a better negative for other instances, which in turn improves the model's
          ability to rank the actual implementation file higher.
    result_rationale: >
      8 个案例覆盖 4 个失败模式：caller-callee confusion（3 个，最常见——文本相似的 wrapper
      函数 vs 实际实现）、utility file distraction（2 个——高文本重叠的 helper 文件干扰）、
      cross-module import chain（2 个——A 导入 B 导入 C，bug 在 C 但文本匹配 A）、test vs
      source（1 个——test file 包含几乎完整的 source code 复制）。这些案例具体展示了
      "lexical similarity ≠ structural relevance" 的核心 insight。
    tables: []
    figures_description:
      - "Fig 9: Side-by-side retrieval ranking visualization for 3 representative cases, showing file dependency graph with highlighted paths"
    analysis: >
      Qualitative examples serve as the paper's "aha moment" — they make the abstract
      representation geometry argument concrete. Reviewer-facing value: even skeptics
      who question statistical significance can see the mechanism operating on real code.

  # ============================================================
  # plan_014: Temperature ablation
  # ============================================================
  - name: "Temperature Ablation τ ∈ {0.05, 0.1, 0.2}"
    plan_id: "plan_014"
    description: >
      3 temperatures × 3 strategies × 2 encoders, 1 seed each.
      测试 strategy ranking 是否 regime-specific。
    expected_results:
      tau_005:
        qwen_random_R1: 0.558
        qwen_embedding_R1: 0.577
        qwen_dataflow_R1: 0.569
        qwen_embedding_minus_random_pp: 1.9
        starcoder_random_R1: 0.470
        starcoder_embedding_R1: 0.485
        starcoder_dataflow_R1: 0.467
        starcoder_embedding_minus_random_pp: 1.5
      tau_010:
        qwen_random_R1: 0.545
        qwen_embedding_R1: 0.565
        qwen_dataflow_R1: 0.555
        qwen_embedding_minus_random_pp: 2.0
        starcoder_random_R1: 0.460
        starcoder_embedding_R1: 0.475
        starcoder_dataflow_R1: 0.458
        starcoder_embedding_minus_random_pp: 1.5
      tau_020:
        qwen_random_R1: 0.530
        qwen_embedding_R1: 0.546
        qwen_dataflow_R1: 0.538
        qwen_embedding_minus_random_pp: 1.6
        starcoder_random_R1: 0.448
        starcoder_embedding_R1: 0.461
        starcoder_dataflow_R1: 0.447
        starcoder_embedding_minus_random_pp: 1.3
      ranking_preserved_across_tau: true
      optimal_tau: 0.05
    result_rationale: >
      Strategy ranking（embedding > dataflow > random for Qwen; embedding > random ≈ dataflow
      for StarCoder）在三个 temperature 下保持一致。τ=0.05 绝对性能最高因为 sharper
      temperature 使 contrastive loss 更有效地区分相似度差异（harder gradient signal）。
      τ=0.2 下所有策略性能下降且 delta 缩小（1.6pp vs 2.0pp），因为 softer temperature
      减弱了 negative 选择质量的影响——当所有 similarity 被压缩到窄范围内，hard vs easy
      negatives 的梯度差异变小。关键结论：findings 不是 temperature-regime-specific，
      直接回应 median reviewer 的 "τ=0.05 unusually low" concern。
    tables:
      - name: "Table 8: Temperature Ablation (R@1 %)"
        columns: ["τ", "Encoder", "random", "embedding", "dataflow", "emb−rand (pp)"]
        rows:
          - [0.05, "Qwen", 55.8, 57.7, 56.9, "+1.9"]
          - [0.05, "StarCoder", 47.0, 48.5, 46.7, "+1.5"]
          - [0.10, "Qwen", 54.5, 56.5, 55.5, "+2.0"]
          - [0.10, "StarCoder", 46.0, 47.5, 45.8, "+1.5"]
          - [0.20, "Qwen", 53.0, 54.6, 53.8, "+1.6"]
          - [0.20, "StarCoder", 44.8, 46.1, 44.7, "+1.3"]
    figures_description:
      - "Fig S5: Temperature × strategy interaction plot (R@1 on y-axis, τ on x-axis, separate lines per strategy)"
    analysis: >
      Ranking stability across τ 是重要的 robustness evidence。τ=0.2 下 delta 缩小但
      不翻转，说明 mining quality 的价值在不同 loss sharpness 下都存在。Paper 可以报告
      τ=0.05 作为 alternative best configuration 但选择 τ=0.1 作为 default（更常见的
      literature default）。

  # ============================================================
  # plan_015: Dynamic mining baseline
  # ============================================================
  - name: "Dynamic vs Static Embedding Mining"
    plan_id: "plan_015"
    description: >
      Dynamic: 每 epoch 重新用当前 encoder 挖 embedding negatives。
      Static: 仅用 pretrained encoder 挖一次（当前做法）。
      Qwen + StarCoder, 1 seed each。
    expected_results:
      qwen_static_R1: 0.565
      qwen_dynamic_R1: 0.568
      qwen_dynamic_minus_static_pp: 0.3
      starcoder_static_R1: 0.475
      starcoder_dynamic_R1: 0.477
      starcoder_dynamic_minus_static_pp: 0.2
      dynamic_significant: false
      curriculum_confound_ruled_out: true
    result_rationale: >
      Dynamic mining 仅微弱提升 +0.2-0.3pp（不显著），因为 LoRA rank 16 的 fine-tuning
      只轻微改变 embedding space——pretrained encoder 的 nearest neighbors 在训练后
      仍然大部分相同。这排除了 "static mining 的优势来自 curriculum effect（early epochs
      看到 harder negatives 然后 negatives 变 stale）" 的 confound——即使更新 negatives，
      效果几乎不变。对 Claim 2 很重要：说明 mining strategy 的选择（what to mine）比
      mining schedule（when to mine）更关键。Dynamic mining 的 compute overhead（每 epoch
      重新 encode + kNN）不 justified。
    tables:
      - name: "Table 13: Static vs Dynamic Embedding Mining"
        columns: ["Encoder", "Static R@1 (%)", "Dynamic R@1 (%)", "Δ (pp)", "p-value"]
        rows:
          - ["Qwen", 56.5, 56.8, "+0.3", 0.41]
          - ["StarCoder", 47.5, 47.7, "+0.2", 0.53]
    figures_description:
      - "Fig S6: Learning curves for static vs dynamic mining, overlaid"
    analysis: >
      Static ≈ dynamic 是 clean negative result，强化了论文 narrative：关键是 negative
      的 semantic quality（embedding vs random vs dataflow），不是 freshness。
      也简化了 practitioner recommendation——mine once from pretrained, no need for
      per-epoch re-mining。

  # ============================================================
  # plan_016: Bootstrap CI for SWE-bench
  # ============================================================
  - name: "Bootstrap CIs for SWE-bench Lite Resolve Rate"
    plan_id: "plan_016"
    description: >
      对 plan_003 的 SWE-bench 结果计算 10K bootstrap resamples 的 95% CI，
      报告 paired difference CIs 和 p-values。
    expected_results:
      embedding_minus_random:
        delta_pp: 2.5
        ci_95: [0.7, 4.3]
        p_value: 0.018
        significant: true
      dataflow_minus_random:
        delta_pp: 3.2
        ci_95: [1.0, 5.5]
        p_value: 0.008
        significant: true
      dataflow_minus_embedding:
        delta_pp: 0.7
        ci_95: [-1.5, 2.9]
        p_value: 0.134
        significant: false
      bootstrap_n: 10000
      sample_size: 300
    result_rationale: >
      Embedding vs random CI [0.7, 4.3] 排除零（p=0.018），确认 embedding mining 在下游
      任务上的统计显著提升。Dataflow vs random 更显著（p=0.008）因为 delta 更大且 SWE-bench
      中 cross-module patches 对 dataflow signal 响应一致。Dataflow vs embedding 不显著
      （p=0.134, CI 含零）——300 instances 的 power 不足以区分 +0.7pp 的小 delta，这是
      expected：retrieval level 的 ~1pp 差异在下游 binary resolve 结果上被放大和噪声化。
      CI 宽度 ~3.6pp 反映 300 样本的 inherent variance——SWE-bench Lite 不是为精确 delta
      估计设计的 benchmark。
    tables:
      - name: "Table 4c: SWE-bench Bootstrap Significance Tests"
        columns: ["Comparison", "Δ (pp)", "95% CI", "p-value"]
        rows:
          - ["embedding − random", "+2.5", "[+0.7, +4.3]", 0.018]
          - ["dataflow − random", "+3.2", "[+1.0, +5.5]", 0.008]
          - ["dataflow − embedding", "+0.7", "[−1.5, +2.9]", 0.134]
    figures_description:
      - "Fig 5c: Bootstrap distribution histograms for the 3 pairwise comparisons"
    analysis: >
      CI 下界 > 0 for both mining strategies vs random 是 EMNLP reviewer 需要的统计保证。
      Dataflow vs embedding 不显著是 honest reporting 且与 Claim 2 的 "conditional" framing
      一致——dataflow 的额外价值不是 universally separable at SWE-bench scale。

  # ============================================================
  # plan_017: Inference-time graph method comparison
  # ============================================================
  - name: "Inference-Time Graph Method Literature Comparison"
    plan_id: "plan_017"
    description: >
      文献分析（非实验）：与 CodexGraph, LocAgent, RANGER 等 inference-time 图方法的
      系统比较。已完成 8 篇论文 survey。
    expected_results:
      papers_surveyed: 8
      key_distinction: "training-time mining (ours) vs inference-time graph navigation"
      complementarity_evidence: >
        All 8 methods operate at inference time; StructFuse mines at training time.
        The two approaches are complementary — StructFuse improves the base retriever
        that graph methods navigate over.
      papers_list:
        - CodexGraph
        - LocAgent
        - RANGER
        - GraphCoder
        - ARISE
        - RepoGraph
        - CodeGRAG
        - CodeRAG
    result_rationale: >
      8 篇 inference-time graph 方法均在推理阶段构建/遍历代码图，而 StructFuse 在训练阶段
      通过 negative mining 将结构信号蒸馏进 encoder。两者正交：StructFuse 产出更好的 base
      retriever，inference-time 方法在此基础上进一步 re-rank/navigate。无直接可比性因为
      实验设置完全不同（LocAgent 用 LLM agent + tool calls，我们用 embedding retrieval）。
      Discussion section 应明确 "complementary, not competing" 的定位。
    tables:
      - name: "Table S3: Comparison with Inference-Time Graph Methods"
        columns: ["Method", "Graph Stage", "Graph Type", "Complementary?"]
        rows:
          - ["StructFuse (ours)", "Training", "Dataflow (CodeQL)", "—"]
          - ["CodexGraph", "Inference", "Code graph DB", "Yes"]
          - ["LocAgent", "Inference", "Repo structure", "Yes"]
          - ["RANGER", "Inference", "Call graph", "Yes"]
          - ["ARISE", "Inference", "Intra-proc dataflow", "Partially (intra only)"]
    figures_description: []
    analysis: >
      Discussion 中用 2 段落即可。不要 overclaim StructFuse 优于这些方法——它们解决不同问题。
      Highlight: StructFuse 是唯一在 training time 利用结构信号的方法，且不增加 inference cost。

  # ============================================================
  # plan_018: BM25 negative baseline
  # ============================================================
  - name: "BM25 Negative Baseline — Closing CoCoHaNeRe Argument"
    plan_id: "plan_018"
    description: >
      BM25-based hard negatives 作为第 4 策略，1+ seed × 2 encoders。
      验证 CoCoHaNeRe 报告的 "embedding negatives harm" 实际是 BM25-proxy artifact。
    expected_results:
      qwen:
        bm25_R1: 0.520
        random_R1: 0.545
        embedding_R1: 0.565
        dataflow_R1: 0.555
        bm25_minus_random_pp: -2.5
        embedding_minus_bm25_pp: 4.5
      starcoder:
        bm25_R1: 0.433
        random_R1: 0.460
        embedding_R1: 0.475
        dataflow_R1: 0.458
        bm25_minus_random_pp: -2.7
        embedding_minus_bm25_pp: 4.2
      bm25_harms_both_encoders: true
      cocohanere_artifact_confirmed: true
      bm25_minus_random_avg_pp: -2.6
    result_rationale: >
      BM25 negatives 在两个 encoder 上均 harm performance（Qwen -2.5pp, StarCoder -2.7pp
      vs random），直接复现了 CoCoHaNeRe 报告的负面效果方向。关键 insight：BM25 negatives
      选取的是 lexically similar 但 semantically ambiguous 的文件——它们与 query 共享大量
      token overlap（function names, variable names, import patterns），但这种 overlap
      恰恰是 contrastive learning 需要利用来区分 positive/negative 的信号。用 BM25 选的
      negatives 让模型学会 ignore lexical cues，但这些 cues 在 code retrieval 中是有效信号。
      相比之下，true embedding distance negatives 选取的是 semantically similar（在 pretrained
      embedding space 中近）但与 query 不同的文件，这迫使模型学习更 fine-grained semantic
      distinctions。BM25 vs embedding 的 4.5pp 差距（Qwen）是论文中最大的 single pairwise
      comparison，构成 Claim 1 correction argument 的 empirical closure。
      效果幅度在 bm25_minus_random_R1_pp [-4.0, -1.5] 范围内。
    tables:
      - name: "Table 3: Full 4-Strategy Comparison Including BM25 Baseline"
        columns: ["Encoder", "Strategy", "R@1 (%)", "95% CI", "Δ vs Random (pp)"]
        rows:
          - ["Qwen", "BM25", 52.0, "[51.2, 52.8]", "−2.5"]
          - ["Qwen", "random", 54.5, "[53.8, 55.2]", "—"]
          - ["Qwen", "dataflow", 55.5, "[54.6, 56.4]", "+1.0"]
          - ["Qwen", "embedding", 56.5, "[55.8, 57.2]", "+2.0"]
          - ["StarCoder", "BM25", 43.3, "[42.3, 44.3]", "−2.7"]
          - ["StarCoder", "random", 46.0, "[45.1, 46.9]", "—"]
          - ["StarCoder", "dataflow", 45.8, "[44.8, 46.8]", "−0.2"]
          - ["StarCoder", "embedding", 47.5, "[46.6, 48.4]", "+1.5"]
    figures_description:
      - "Fig 3: 4-strategy R@1 bar chart with BM25 highlighted in red, showing the harm direction. Annotation arrow from BM25 to embedding with '4.5pp gap — the CoCoHaNeRe artifact'"
      - "Fig 4: Neg similarity distribution histograms for BM25 vs embedding vs random vs dataflow, showing BM25 occupies a different region of similarity space"
    analysis: >
      BM25 baseline 是 best tier 论文的 crown jewel experiment。它将 Claim 1 从 "argumentative
      correction" 升级为 "empirical demonstration"：我们不仅指出 CoCoHaNeRe 用了 BM25 proxy，
      还实际运行 BM25 negatives 复现了 harm effect，然后展示 true embedding negatives 方向相反。
      4-strategy ordering BM25 < random < dataflow ≤ embedding 清晰展示了 negative mining
      strategy 的 quality spectrum。Reviewer 对 "correction without evidence" 的 concern
      被彻底关闭。

  # ============================================================
  # plan_019: Pool size sensitivity
  # ============================================================
  - name: "Pool Size Sensitivity (50/100/200/500)"
    plan_id: "plan_019"
    description: >
      在 SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints，
      测试 strategy ranking 在更 realistic pool sizes 下的稳定性。
    expected_results:
      qwen:
        pool_50:
          random_R1: 0.545
          embedding_R1: 0.565
          dataflow_R1: 0.555
          embedding_minus_random_pp: 2.0
        pool_100:
          random_R1: 0.428
          embedding_R1: 0.447
          dataflow_R1: 0.438
          embedding_minus_random_pp: 1.9
        pool_200:
          random_R1: 0.342
          embedding_R1: 0.359
          dataflow_R1: 0.351
          embedding_minus_random_pp: 1.7
        pool_500:
          random_R1: 0.261
          embedding_R1: 0.276
          dataflow_R1: 0.269
          embedding_minus_random_pp: 1.5
      starcoder:
        pool_50:
          random_R1: 0.460
          embedding_R1: 0.475
          dataflow_R1: 0.458
          embedding_minus_random_pp: 1.5
        pool_100:
          random_R1: 0.358
          embedding_R1: 0.372
          dataflow_R1: 0.357
          embedding_minus_random_pp: 1.4
        pool_200:
          random_R1: 0.282
          embedding_R1: 0.295
          dataflow_R1: 0.281
          embedding_minus_random_pp: 1.3
        pool_500:
          random_R1: 0.214
          embedding_R1: 0.225
          dataflow_R1: 0.213
          embedding_minus_random_pp: 1.1
      ranking_stable_across_pools: true
      pool_ranking_stable_pct: 100
      delta_shrinkage_rate: "~0.15pp per doubling of pool size"
    result_rationale: >
      Strategy ranking（embedding > dataflow > random for Qwen; embedding > random ≈ dataflow
      for StarCoder）在 pool 50→500 全程保持稳定（pool_ranking_stable_pct = 100%）。
      绝对 R@1 随 pool 增大而下降（50→500 约 halved），因为 larger pool = more distractors
      = harder task。Embedding-random delta 从 2.0pp (pool=50) 缓慢缩小至 1.5pp (pool=500)，
      缩小幅度约 25%，但方向和显著性保持。原因：pool=500 时 random negatives 中偶然出现
      "hard" negative 的概率增加（base rate effect），部分缩小了 mining 策略的差异。
      但核心 signal 不消失——embedding mining 在 pool=500 仍有 +1.5pp Qwen, +1.1pp StarCoder。
      Dataflow 在 Qwen 上从 +1.0pp (pool=50) 降至 +0.8pp (pool=500) 但保持正值。
      这直接回应 reviewer "pool=50 unrealistically small" concern：即使 10x pool 扩大，
      strategy ranking 完全不翻转。
    tables:
      - name: "Table 12: Pool Size Sensitivity (R@1 %)"
        columns: ["Pool", "Encoder", "random", "embedding", "dataflow", "emb−rand (pp)", "Ranking"]
        rows:
          - [50, "Qwen", 54.5, 56.5, 55.5, "+2.0", "E>D>R"]
          - [100, "Qwen", 42.8, 44.7, 43.8, "+1.9", "E>D>R"]
          - [200, "Qwen", 34.2, 35.9, 35.1, "+1.7", "E>D>R"]
          - [500, "Qwen", 26.1, 27.6, 26.9, "+1.5", "E>D>R"]
          - [50, "StarCoder", 46.0, 47.5, 45.8, "+1.5", "E>R>D"]
          - [100, "StarCoder", 35.8, 37.2, 35.7, "+1.4", "E>R>D"]
          - [200, "StarCoder", 28.2, 29.5, 28.1, "+1.3", "E>R≈D"]
          - [500, "StarCoder", 21.4, 22.5, 21.3, "+1.1", "E>R≈D"]
    figures_description:
      - "Fig 10: Pool size (x-axis, log scale) vs R@1 (y-axis) for 3 strategies, separate panels for Qwen and StarCoder. Shaded bands between embedding and random lines highlight persistent delta."
      - "Fig 10b: Delta (embedding − random) vs pool size, showing graceful degradation"
    analysis: >
      Pool size sensitivity 是外部有效性的关键证据。100% ranking stability 在 50→500
      全程保持是 best tier 的标志。Delta 的 graceful degradation（非 collapse）说明
      mining strategy 的价值是 robust 的。论文可以明确声明："Strategy rankings are stable
      across pool sizes spanning an order of magnitude (50–500), with embedding mining
      maintaining a statistically significant advantage even at the largest pool tested."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8ee7631-2a5d-4dcd-a2b9-c56d823da71d",
  "isSidechain": false,
  "requestId": "req_011Cb2mvvJ6dcf49edM1U3mf",
  "type": "assistant",
  "uuid": "e91fbf39-e6e8-46b4-be0f-2a372dcb2fbc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017pmrmQAf7f8JHXhpZETQ1L",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11544,
      "cache_read_input_tokens": 32493,
      "output_tokens": 17808,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11544,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 17808,
          "cache_read_input_tokens": 32493,
          "cache_creation_input_tokens": 11544,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11544
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：全 18 runs 复现 pilot pattern，BM25 baseline 关闭 CoCoHaNeRe 论证，三条 claim 原样成立 核心假设：['embedding-random R@1 delta 在两个 encoder 上 95% CI 下界 > 0', 'dataflow-random R@…",
  "leafUuid": "e91fbf39-e6e8-46b4-be0f-2a372dcb2fbc",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic empirical validation of hard negative mining strategies for code retrieval",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：全 18 runs 复现 pilot pattern，BM25 baseline 关闭 CoCoHaNeRe 论证，三条 claim 原样成立 核心假设：['embedding-random R@1 delta 在两个 encoder 上 95% CI 下界 > 0', 'dataflow-random R@…",
  "leafUuid": "e91fbf39-e6e8-46b4-be0f-2a372dcb2fbc",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic empirical validation of hard negative mining strategies for code retrieval",
  "sessionId": "c009ff0c-5981-45ce-bb65-8ec7bd54e72e"
}
```

---
