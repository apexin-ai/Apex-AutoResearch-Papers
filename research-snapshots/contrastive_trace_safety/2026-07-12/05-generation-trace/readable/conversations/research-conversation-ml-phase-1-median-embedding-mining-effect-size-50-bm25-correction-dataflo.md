# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：embedding mining 优势存在但 effect size 缩水约 50%，BM25 部分支持 correction 论证，dataflo

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/88a154e2-ebab-4a41-bc2d-3efe45f9111c.jsonl`
- **Structured JSON:** [`408edbc0c4db3cb6f2b0.json`](../../sessions/40/408edbc0c4db3cb6f2b0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T16:33:01.540Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T16:33:01.540Z",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：embedding mining 优势存在但 effect size 缩水约 50%，BM25 部分支持 correction 论证，dataflow 条件性获益噪声大\n核心假设：['embedding-random delta 正向但 CI 较宽，个别 seed 差异 < 0.5pp', 'dataflow-random delta 在 Qwen 上 CI 包含 0（方向正确但不显著）', 'BM25 negatives harm 方向正确但 delta 小（-0.5 ~ -1.5pp），与 random 差异 p > 0.05', 'pool ≥ 200 时 embedding 与 dataflow 排名偶有交叉', 'SWE-bench delta < 1pp 或 CI 包含 0']\n关键指标范围：{'qwen_emb_minus_random_R1_pp': [0.5, 1.5], 'starcoder_emb_minus_random_R1_pp': [0.3, 1.0], 'qwen_df_minus_random_R1_pp': [-0.3, 0.8], 'starcoder_df_minus_random_R1_pp': [-1.5, 0.0], 'bm25_minus_random_R1_pp': [-1.5, -0.3], 'swebench_resolve_rate_delta_pp': [-0.5, 1.5], 'repobench_R1_delta_pp': [0.0, 1.5], 'pool_ranking_stable_pct': [50, 75], 'bootstrap_CI_width_R1_pp': [2.0, 4.0], 'qwen_mean_R1_absolute': [0.51, 0.55], 'starcoder_mean_R1_absolute': [0.42, 0.47]}\n叙事方向：Claim 1 需降级：embedding mining \"tends to help\" 而非 \"consistently improves\"， CoCoHaNeRe correction 从 \"empirically verified\" 改为 \"BM25 proxy 方向一致但 effect size 不足以排除其他混杂因素\"。Claim 2 降级为 exploratory observation：dataflow 条件性获益的 evidence 不足以支撑独立 claim，合并到 Claim 1 作为 \"strategy-encoder interaction analysis\" 的一个 case。论文重心从 \"correcting misconception + mechanistic explanation\" 移向 \"systematic empirical comparison + representation geometry analysis as explanatory framework\"。需补充 related work 深度对比（ANCE, curriculum mining）来弥补 effect size 不足。标题用 \"Systematic Study\" 而非 \"Correcting Misconceptions\"。仍投 EMNLP Main， 但定位从 strong empirical contribution 调整为 analysis paper。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: structfuse-context\nfocus: D030 修复后验证：新增 plan_018 BM25 baseline（关闭 CoCoHaNeRe correction 论证）、plan_019 pool size sensitivity、plan_004 多 seed CIs、plan_005 structural coverage 分层 + neg_difficulty quartile。Framing 修正：N=2 降级为 observation、Claim 3 降为 supporting methodology、StarCoder decoder-only。Reviewers 应重点评估：(1) BM25 baseline 是否关闭了上一轮最大缺口，(2) 新增实验是否充分回应了上一轮 median/worst 的 \"related work insufficient\" 和 \"effect size marginal\" 问题，(3) 修正后的 N=2 observation framing 是否足够。\n\n## paper_framing.md\n\n# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \"harm\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).\n\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\n\n- **Headline result template**: \"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\"\n\n## Core Insight\n\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\"\n- Backup: \"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\n- m1_reextract_v2: expanded extraction for higher coverage\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected\n    vs gold statistics'\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: m1_extraction\n  mvp_registry_id: mvp_p1_codeql_feasibility\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- id: plan_002\n  claim: 1\n  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,\n    3 seeds each, Qwen2.5-Coder-3B LoRA'\n  priority: P0\n  gpu_budget_hours: 200\n  deps:\n  - plan_001\n  registry_id: m2_embed_verify\n  mvp_registry_id: mvp_p2b_contrastive_training\n  full_registry_ids:\n  - m2_full_qwen\n  - m2_full_starcoder\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- id: plan_003\n  claim: 1\n  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best\n    checkpoint, Qwen3.6-27B agent'\n  priority: P0\n  gpu_budget_hours: 40\n  deps:\n  - plan_002\n  notes: eval script ready (eval_swebench.py), dry-run passed, 12 SWE-bench repos\n    pre-cloned to /root/autodl-tmp/structfuse/swebench_repos. Awaiting M2 checkpoint.\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no\n    LLM agent'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  notes: eval script ready (eval_repobench.py), dry-run passed. RepoBench-R data via\n    hf_hub_download. test_easy 8K instances (pool ~6), test_hard 8K (pool ~18). Awaiting\n    M2 checkpoint. [Dream fix] Must run with multiple seeds and report 95% CIs — dream\n    reviewers flagged inconsistent statistical reporting (CIs on SWE-bench but not\n    RepoBench-R) across all 3 tiers.\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding\n    negatives 何时最有害'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  notes: 'analysis script ready (analyze_stratified.py), dry-run passed. 3 strata:\n    repo size / pool size / query-positive similarity. Outputs stratified_results.json\n    + plots PDF. Awaiting M2 checkpoints for re-eval. [Dream fix] Must add 2 more\n    strata: (a) structural data availability (34% with dataflow vs 66% fallback) per\n    [B][M][W] all tiers, (b) neg_difficulty quartile analysis per [W] tier. Total\n    5 strata.'\n  status: planned\n- id: plan_006\n  claim: 3\n  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,\n    connected-but-not-gold ratio by repo size'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan_006_scalability\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- id: plan_007\n  claim: 1\n  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Ablation: fusion head (embedding-only vs structural-features-only\n    vs combined)'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether\n    data-flow helps'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_003\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Qualitative examples: 5-10 cases where structural negatives changed\n    retrieval outcome'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Second encoder validation: repeat M2 core comparison (3 strategies,\n    1 seed) on StarCoder-3B or CodeBERT to test architecture generality'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  dream_source: 'best-R1-W1, median-R2-W5: single encoder is primary generality concern.\n    Upgraded to P0 per Reviewer — this is the #1 factor separating WA from WR.'\n  registry_id: plan_013_starcoder\n  full_registry_id: m2_full_starcoder\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- id: plan_014\n  claim: 2\n  description: 'Temperature ablation: τ ∈ {0.05, 0.1, 0.2} for all 3 strategies, test\n    regime-specificity of embedding harm'\n  priority: P1\n  gpu_budget_hours: 70\n  deps:\n  - plan_002\n  dream_source: 'median-R1-W3: τ=0.05 unusually low, finding may be regime-specific'\n  status: planned\n- id: plan_015\n  claim: 2\n  description: 'Dynamic embedding mining baseline: re-mine embedding negatives per\n    epoch vs static (mine once from pretrained). Isolate selection criterion from\n    curriculum shift.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  dream_source: 'best-R1-W2, median-R1-W2: static vs dynamic mining is potential confound\n    for Claim 2'\n  status: planned\n- id: plan_016\n  claim: 1\n  description: 'Bootstrap CI for SWE-bench Lite: add 95% bootstrap confidence intervals\n    to end-to-end resolve rate evaluation'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  dream_source: 'best-R1-W3, worst-R1-W5: +2.0pp on 300 instances needs statistical\n    significance test'\n  status: planned\n- id: plan_017\n  claim: 1\n  description: 'Inference-time graph method comparison: discuss/compare with CodexGraph,\n    LocAgent — is StructFuse complementary or alternative? Analysis complete, document\n    in artifacts/analysis/plan017_literature_comparison.md. Discussion draft in artifacts/paper_drafts/discussion_draft.md.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  dream_source: 'best-R2-W5: no comparison with inference-time graph methods'\n  notes: 'DONE (analysis only, no experiment). 8 papers surveyed (CodexGraph, LocAgent,\n    RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). All citations verified.\n    Conclusion: training-time vs inference-time are complementary, not competing.'\n  status: planned\n- id: plan_018\n  claim: 1\n  description: 'BM25 negative baseline: mine BM25-based hard negatives as 4th strategy,\n    train ≥1 seed × 2 encoders, compare R@1 with random/embedding/dataflow. Empirically\n    verify CoCoHaNeRe BM25-proxy caused the reported harm.'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers identify missing BM25\n    baseline as #1 structural gap. CoCoHaNeRe correction claim requires empirical\n    verification — without it the paper motivation is asserted but unverified.'\n  notes: 'Phase 1 (CPU, can start now): build BM25 index over training corpus, mine\n    top-k BM25 negatives per query using same protocol as other strategies, produce\n    bm25_training_data.jsonl. Phase 2 (GPU, after M2 frees up): train 1 seed × 2 encoders\n    with BM25 negatives (~7.5h each). 3 seeds preferred if GPU budget allows. Expected\n    result: BM25 negatives harm → confirms CoCoHaNeRe artifact → closes argument.'\n  status: planned\n- id: plan_019\n  claim: 1\n  description: 'Pool size sensitivity analysis: test strategy ranking stability at\n    pool={50, 100, 200, 500} candidates per query on SWE-smith validation.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers flag pool=50 as unrealistically\n    small. Strategy differences may not preserve at realistic pool sizes.'\n  notes: Requires M2 best checkpoints. Re-evaluate on expanded candidate pools. If\n    strategy ranking changes at pool>200, must discuss in paper.\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_p1_codeql_feasibility\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    timeout_rate: 0\n    repos_processed: 8\n    repos_skipped: 2\n    cg_mean_s: 29.6\n    cg_max_s: 119.8\n    df_mean_s: 43.4\n    df_max_s: 167.1\n    h2_connected_coverage: 0.014815\n    h2_disconnected_coverage: 0\n    h2_fisher_p: 6.5e-09\n    h2_gold_in_connected_ratio: 1\n    h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'\n- exp_id: mvp_p2a_linear_proxy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    df_bm25_auc: 0.78\n    bm25_only_auc: 0.476\n    auc_delta: 0.304\n    df_bm25_mrr: 0.556\n    bm25_only_mrr: 0.115\n    mrr_delta: 0.441\n    df_bm25_f1: 0.143\n    bm25_only_f1: 0.039\n    top_feature: is_connected (+2.82)\n    repos_evaluated: 3\n    note: 3 repos / 3 positive samples, directional evidence\n- exp_id: p2b-smoke-test\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke8\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-all-9runs\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_p2b_contrastive_training\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    random_s42_recall1: 0.984\n    random_s123_recall1: 0.984\n    random_s456_recall1: 0.992\n    embedding_s42_recall1: 0.874\n    random_mean_recall1: 0.987\n    runs_completed: 4\n    runs_failed: 5\n    failure_type: disk_full_torch_save\n- exp_id: mvp_p2b_contrastive_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_all\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_4runs_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_seed42:\n      recall@1: 0.9449\n      recall@5: 0.9843\n      recall@10: 0.9843\n    random_seed123:\n      recall@1: 0.9449\n      recall@5: 0.9921\n      recall@10: 0.9921\n    random_seed456:\n      recall@1: 0.9291\n      recall@5: 0.9921\n      recall@10: 0.9921\n    emb_dist_seed42:\n      recall@1: 0.6693\n      recall@5: 0.8898\n      recall@10: 0.9291\n    pool_size: 26\n    n_samples: 127\n- exp_id: p2b_5reruns\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_s42:\n      val_loss: 0.0347\n      recall@1: 0.9843\n    random_s123:\n      val_loss: 0.0446\n      recall@1: 0.9843\n    random_s456:\n      val_loss: 0.0188\n      recall@1: 0.9921\n    emb_dist_s42:\n      val_loss: 0.1876\n      recall@1: 0.874\n    emb_dist_s123:\n      val_loss: 0.1461\n      recall@1: 0.874\n    emb_dist_s456:\n      val_loss: 0.1281\n      recall@1: 0.8819\n    dataflow_s42:\n      val_loss: 0.1878\n      recall@1: 0.874\n    dataflow_s123:\n      val_loss: 0.146\n      recall@1: 0.874\n    dataflow_s456:\n      val_loss: 0.1278\n      recall@1: 0.8819\n    runs_completed: 9\n    runs_failed: 0\n    WARNING: dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds\n      — likely code bug in negative sampling\n- exp_id: p2b_dataflow_retrain\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: p2b_eval_4runs_pool50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pool_size: 50\n    n_samples: 127\n    random_s42:\n      recall@1: 0.496\n      recall@5: 0.843\n      recall@10: 0.945\n    random_s123:\n      recall@1: 0.535\n      recall@5: 0.85\n      recall@10: 0.921\n    random_s456:\n      recall@1: 0.543\n      recall@5: 0.843\n      recall@10: 0.953\n    emb_dist_s42:\n      recall@1: 0.488\n      recall@5: 0.835\n      recall@10: 0.874\n    random_mean:\n      recall@1: 0.525\n      recall@5: 0.845\n      recall@10: 0.94\n    emb_dist_vs_random_delta:\n      recall@1: -0.037\n      recall@5: -0.01\n      recall@10: -0.066\n- exp_id: d007_50repo_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances: 240\n    instances_with_extra_connected: 98\n    Z_pct: 40.8\n    avg_connected_minus_gold: 6\n    codeql_timeout_rate_pct: 4\n    by_repo_size:\n      small_lt50:\n        Z_pct: 38.6\n        avg_extra: 2.5\n      medium_50_200:\n        Z_pct: 55.7\n        avg_extra: 11.8\n      large_gt200:\n        Z_pct: 16.7\n        avg_extra: 8.8\n    decision: Z=40.8% >= 20% -> original method viable, proceed to M1\n- exp_id: m1_extraction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- exp_id: m2_early_pilot\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    pid: 795791\n    gpu: cuda:4\n    gpu_mem_mb: 9342\n    gpu_util_pct: 83\n    batch_size: 2\n    num_negatives: 3\n    max_seq_length: 1024\n    strategy_running: random (stuck at step 4000, epoch 3)\n    strategies_completed: 0/3\n    eval_1500:\n      val_loss: 0.5879\n      recall_at_1: 0.4693\n      recall_at_5: 0.4693\n      recall_at_10: 0.4693\n    eval_2000:\n      val_loss: 0.7089\n      recall_at_1: 0.4398\n    eval_2500:\n      val_loss: 0.6961\n      recall_at_1: 0.4291\n    eval_3000:\n      val_loss: 0.728\n      recall_at_1: 0.4104\n    eval_3500:\n      val_loss: 0.7022\n      recall_at_1: 0.4439\n    best_checkpoint: step_1500 (val_loss=0.5879, 6.2GB)\n    WARNING: recall@1=recall@5=recall@10 confirmed eval bug. Process hung after step\n      4000 (~45min no output). Overfitting after step 1500.\n    status_check_at: '2026-05-13T04:42:00Z'\n- exp_id: m2_early_pilot_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: m2_early_pilot_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: m2_embed_verify\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- exp_id: plan_013_starcoder\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- exp_id: plan_006_scalability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- exp_id: m2_full_qwen\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics:\n    random_s42:\n      status: DONE\n      epoch: 3/3\n      total_steps: 4242\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.4869\n        recall_at_1: 0.533\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.4651\n        recall_at_1: 0.553\n        recall_at_5: 0.959\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.5365\n        recall_at_1: 0.523\n        recall_at_5: 0.955\n        recall_at_10: 1\n      eval_2000:\n        val_loss: 0.5162\n        recall_at_1: 0.523\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_2500:\n        val_loss: 0.5264\n        recall_at_1: 0.527\n        recall_at_5: 0.956\n        recall_at_10: 1\n      eval_3000:\n        val_loss: 0.5406\n        recall_at_1: 0.536\n        recall_at_5: 0.956\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.4651, R@1=0.5527)\n      conclusion: Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357).\n        Full data helps.\n    random_s43:\n      status: RUNNING\n      epoch: 1/2\n      current_step: 1200\n      total_steps: 2810\n      total_steps_per_epoch: 1405\n      eval_500:\n        val_loss: 0.4476\n        recall_at_1: 0.5357\n        recall_at_5: 0.9699\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.4638\n        recall_at_1: 0.5285\n        recall_at_5: 0.9672\n        recall_at_10: 1\n      note: Running on cuda:0. Best R@1=0.5357 at step 500. eval@1000 early_stopping\n        1/2. 2 epochs + patience=2.\n    progress_snapshot: 2026-05-15T00:19 CST\n- exp_id: m2_full_starcoder\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    random_s42:\n      epoch: 3/3\n      current_step: 4000\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.6194\n        recall_at_1: 0.435\n        recall_at_5: 0.905\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.6134\n        recall_at_1: 0.454\n        recall_at_5: 0.92\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.6528\n        recall_at_1: 0.449\n        recall_at_5: 0.906\n        recall_at_10: 1\n      eval_2000:\n        val_loss: 0.6698\n        recall_at_1: 0.4456\n        recall_at_5: 0.906\n        recall_at_10: 1\n      eval_3500:\n        val_loss: 0.6588\n        recall_at_1: 0.4534\n        recall_at_5: 0.9057\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.6134, R@1=0.454)\n      note: Step 4000, lr=2.07e-07, patience exhausted (5/0). Approaching natural\n        end. Watcher PID 309679 ready to auto-start s43.\n    progress_snapshot: 2026-05-15T00:19 CST\n- exp_id: m1_reextract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: neg_difficulty_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_128:\n      random:\n        pos_sim: 0.9804\n        neg_sim: 0.899\n        margin: 0.0816\n        pct_positive_margin: 77.8\n      embedding_distance:\n        pos_sim: 0.9804\n        neg_sim: 0.959\n        margin: 0.0209\n        pct_positive_margin: 60.7\n      dataflow_aware:\n        pos_sim: 0.9805\n        neg_sim: 0.95\n        margin: 0.0309\n        pct_positive_margin: 67.4\n    starcoder_128:\n      random:\n        pos_sim: 0.757\n        neg_sim: 0.553\n        margin: 0.2039\n        pct_positive_margin: 72.8\n      embedding_distance:\n        pos_sim: 0.784\n        neg_sim: 0.668\n        margin: 0.1159\n        pct_positive_margin: 59.2\n      dataflow_aware:\n        pos_sim: 0.761\n        neg_sim: 0.659\n        margin: 0.1022\n        pct_positive_margin: 62.8\n    qwen_2048:\n      random:\n        pos_sim: 0.9855\n        neg_sim: 0.9111\n        margin: 0.0743\n        margin_std: 0.2322\n        pct_positive_margin: 81.8\n      embedding_distance:\n        pos_sim: 0.9855\n        neg_sim: 0.9685\n        margin: 0.017\n        margin_std: 0.114\n        pct_positive_margin: 58.8\n      dataflow_aware:\n        pos_sim: 0.9856\n        neg_sim: 0.9563\n        margin: 0.0293\n        margin_std: 0.1407\n        pct_positive_margin: 73.9\n    starcoder_2048:\n      random:\n        pos_sim: 0.7985\n        neg_sim: 0.6045\n        margin: 0.194\n        margin_std: 0.2788\n        pct_positive_margin: 78\n      embedding_distance:\n        pos_sim: 0.8079\n        neg_sim: 0.7409\n        margin: 0.067\n        margin_std: 0.2056\n        pct_positive_margin: 55\n      dataflow_aware:\n        pos_sim: 0.8009\n        neg_sim: 0.6818\n        margin: 0.1192\n        margin_std: 0.2264\n        pct_positive_margin: 70.4\n    sc_qwen_margin_ratio_128:\n      random: 2.5\n      embedding_distance: 5.54\n      dataflow_aware: 3.3\n    sc_qwen_margin_ratio_2048:\n      random: 2.61\n      embedding_distance: 3.94\n      dataflow_aware: 4.07\n- exp_id: m1_reextract_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T16:33:01.544Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T16:33:01.544Z",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-14T16:33:01.565Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：embedding mining 优势存在但 effect size 缩水约 50%，BM25 部分支持 correction 论证，dataflow 条件性获益噪声大
核心假设：['embedding-random delta 正向但 CI 较宽，个别 seed 差异 < 0.5pp', 'dataflow-random delta 在 Qwen 上 CI 包含 0（方向正确但不显著）', 'BM25 negatives harm 方向正确但 delta 小（-0.5 ~ -1.5pp），与 random 差异 p > 0.05', 'pool ≥ 200 时 embedding 与 dataflow 排名偶有交叉', 'SWE-bench delta < 1pp 或 CI 包含 0']
关键指标范围：{'qwen_emb_minus_random_R1_pp': [0.5, 1.5], 'starcoder_emb_minus_random_R1_pp': [0.3, 1.0], 'qwen_df_minus_random_R1_pp': [-0.3, 0.8], 'starcoder_df_minus_random_R1_pp': [-1.5, 0.0], 'bm25_minus_random_R1_pp': [-1.5, -0.3], 'swebench_resolve_rate_delta_pp': [-0.5, 1.5], 'repobench_R1_delta_pp': [0.0, 1.5], 'pool_ranking_stable_pct': [50, 75], 'bootstrap_CI_width_R1_pp': [2.0, 4.0], 'qwen_mean_R1_absolute': [0.51, 0.55], 'starcoder_mean_R1_absolute': [0.42, 0.47]}
叙事方向：Claim 1 需降级：embedding mining "tends to help" 而非 "consistently improves"， CoCoHaNeRe correction 从 "empirically verified" 改为 "BM25 proxy 方向一致但 effect size 不足以排除其他混杂因素"。Claim 2 降级为 exploratory observation：dataflow 条件性获益的 evidence 不足以支撑独立 claim，合并到 Claim 1 作为 "strategy-encoder interaction analysis" 的一个 case。论文重心从 "correcting misconception + mechanistic explanation" 移向 "systematic empirical comparison + representation geometry analysis as explanatory framework"。需补充 related work 深度对比（ANCE, curriculum mining）来弥补 effect size 不足。标题用 "Systematic Study" 而非 "Correcting Misconceptions"。仍投 EMNLP Main， 但定位从 strong empirical contribution 调整为 analysis paper。


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
  "promptId": "0f5c36be-f921-4c51-bee2-6826297c6264",
  "type": "user",
  "uuid": "0df7b252-f017-4318-9f1f-1ecb38c0d527",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T16:33:01.564Z_

```json
{
  "parentUuid": "0df7b252-f017-4318-9f1f-1ecb38c0d527",
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
  "uuid": "95450960-08fd-4736-8706-b8a61e4ee8f4",
  "timestamp": "2026-05-14T16:33:01.564Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T16:33:01.564Z_

```json
{
  "parentUuid": "95450960-08fd-4736-8706-b8a61e4ee8f4",
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
  "uuid": "826b35ee-6cde-4c64-a64e-6797eec3a8bf",
  "timestamp": "2026-05-14T16:33:01.564Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T16:33:01.564Z_

```json
{
  "parentUuid": "826b35ee-6cde-4c64-a64e-6797eec3a8bf",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ad6460b5-1e34-405b-972f-17fabddde92e",
  "timestamp": "2026-05-14T16:33:01.564Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：embedding mining 优势存在但 effect size 缩水约 50%，BM25 部分支持 correction 论证，dataflow 条件性获益噪声大 核心假设：['embedding-random delta 正向但 CI 较宽，个别 seed 差异 < 0.5pp', 'datafl…",
  "leafUuid": "ad6460b5-1e34-405b-972f-17fabddde92e",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic empirical analysis of hard negative mining strategies for code retrieval",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c"
}
```

---

### Assistant

_source line 9 · 2026-05-14T16:35:08.082Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined/predicted experimental results for all "planned" experiments in the experiment_plan, under the **median** tier scenario they've defined.

Let me carefully go through each planned experiment and generate predictions consistent with the median tier definition:

**Median tier key characteristics:**
- Embedding mining advantage exists but effect size shrinks ~50%
- BM25 partially supports correction argument
- Dataflow conditional benefit is noisy
- Key metric ranges provided
- Narrative: Claims need downgrading

**Planned experiments to predict:**
1. plan_003: SWE-bench Lite eval


2. plan_004: RepoBench-R cross-file retrieval (with multi-seed CIs)
3. plan_005: Stratified analysis (5 strata)
4. plan_007: 1-hop vs 2-hop vs 3-hop call-graph bounding
5. plan_008: Training data size scaling
6. plan_009: Fusion head ablation
7. plan_010: Dataflow-distance weighted negatives
8. plan_011: Failure analysis
9. plan_012: Qualitative examples
10. plan_014: Temperature ablation
11. plan_015: Dynamic mining baseline
12. plan_016: Bootstrap CI for S
13. plan_017: Inference-time graph method comparison (analysis only, marked as done)
14. plan_018: BM25 negative baseline
15. plan_019: Pool size sensitivity

Now I'm looking at the pilot results to estimate what the full runs might show. The Qwen model shows consistent gains from embedding and dataflow approaches, while StarCoder's dataflow variant actually underperforms slightly, which is interesting to note when extrapolating.

Looking at the full experiment results so far, I can see the random baselines are holding steady around 0.55 for Qwen and 0.45 for StarCoder. When I project the deltas from the pilots onto these full-run numbers, the improvements appear to compress by roughly half at the median tier—embedding gains shrink from around 2pp down to 1pp for Qwen, and the dataflow approach shows much tighter ranges, sometimes even dipping negative for StarCoder.

The stability metrics look reasonable too: pool ranking consistency stays in the 50-75% range, bootstrap confidence intervals are between 2-4pp wide, and the absolute retrieval rates cluster around 0.53 for Qwen and 0.445 for StarCoder. Now I'm organizing these findings into the full YAML structure, starting with the SWE-bench Lite experiment at 300 instances.

For SWE-bench Lite, I'm expecting small effect sizes since retrieval improvements don't translate cleanly to end-to-end resolution—the agent's generation capability is the bottleneck. Even a 1pp gain in R@1 only means a couple more correctly retrieved files out of 300, and the agent still needs to solve the task. The median resolve rate delta should stay under 1pp with confidence intervals that include zero, embedding strategies showing maybe 0.5pp improvement while dataflow remains marginal.

Moving to RepoBench-R, I'm looking at both easy and hard test sets with multiple seeds and confidence intervals. The easy subset has a constrained pool of about 6 files so strategies compress together, while the hard subset with ~18 files in the pool gives slightly more room for differentiation. The median delta should land in that 0-1.5pp range, and the confidence intervals will reflect the variance across seeds.

I'm also planning stratified analysis across five dimensions—repo size, pool size, query-positive similarity, structural data availability, and negative difficulty quartiles. The results are noisy overall, but the structural data stratum is interesting: cases with dataflow information show conditional benefit at 34%, while the 66% without it show nothing. The hardest negatives in the top quartile might show some benefit, but the bottom quartile doesn't.

For the hop ablation, I'm comparing 1-hop versus 2-hop versus 3-hop retrieval depths. The current 2-hop default seems right—1-hop is too restrictive with fewer negatives, 3-hop is too loose, and the effect differences between them are small anyway.

I'm also examining training data scaling with 1K, 3K, and 5K instances to see if more training data helps close the gap.

Looking at the fusion head ablation next—comparing embedding-only versus structural-only versus combined approaches. The embedding-only version performs nearly as well as the combined model, while structural-only is noticeably worse, so the combined approach only gives marginal gains.

For the dataflow-distance weighting, I'm testing weighted versus binary approaches, but the difference is marginal and not statistically significant.

I'm doing a failure analysis on 50 cases to understand where dataflow helps, though the patterns aren't emerging strongly. I can also pull 5-10 qualitative examples that show promise, but I'm aware those are cherry-picked.

Finally, I'm ablating the temperature parameter across 0.05, 0.1, and 0.2 to see if that affects the results. default is 0.05
- Median: τ=0.1 may be better, strategy ranking partially preserved

**plan_015: Dynamic mining**
- Dynamic vs static
- Median: dynamic slightly better but confounds interpretation

**plan_016: Bootstrap CI for SWE-bench**
- Median: CIs wide, include 0 for most comparisons

**plan_017: Literature comparison**
- Already done as analysis

**plan_018: BM25 baseline**
- Key experiment
- Median: BM25 negatives harm but delta small (-0.5 to -1.5pp), partially supports correction
- p > 0.05 vs random

**plan_019: Pool size sensitivity**
- Pool {50, 100, 200, 500}
- Median: ranking stable at 50-100, starts to wobble at 200+, crossing at 500 with [50, 75]% stability

Now I'm working out the absolute R@1 values for the YAML. I'm targeting Qwen around 0.530 for random and StarCoder around 0.443, then layering in the deltas I've observed—embedding gains roughly 1pp for Qwen and 0.7pp for StarCoder, while dataflow shows more modest improvements around 0.3pp. I see there are 15 planned experiments total, including plan_018 and plan_019. For the m2_full results that several of these depend on, I'm working with anchor metrics around a 0.53 mean for Qwen and 0.445 for StarCoder, with bootstrap confidence intervals around 3 percentage points wide. Now I'm extrapolating what the multi-seed results would look like across these experiments.

For Qwen, I'm estimating the random baseline at 0.530 with individual seed values around 0.521, 0.535, and 0.534, then modeling how embedding and dataflow approaches would shift those means by roughly +1.0pp and +0.3pp respectively. For StarCoder, the random baseline sits around 0.443 with embedding showing a modest +0.7pp improvement and dataflow actually declining by about -0.6pp. Given that the confidence intervals are roughly ±1.5pp, I need to keep these deltas in perspective when evaluating significance.

Now I'm reconsidering how to properly calculate the confidence interval for the delta itself—the CI width of 3pp applies to the individual R@1 scores, not directly to the difference between strategies. The delta's CI would depend on the correlation between paired measurements, so with paired bootstrap it could actually be narrower than I initially thought.

Looking at the specific deltas across models and strategies: Qwen's embedding-random shows the strongest positive signal at +1.0pp but the CI still crosses zero, while StarCoder's embedding-random is weaker at +0.7pp. The dataflow-random deltas are even less convincing—Qwen's +0.3pp and StarCoder's -0.6pp both clearly include zero in their confidence intervals.

For the BM25 baseline, the delta sits around -0.9pp which is actually moving away from random performance, and the effect isn't statistically significant anyway. On the pool sensitivity front, I'm seeing stability metrics in the 50-75% range, suggesting moderate consistency in the ranking results.

Now looking at SWE-bench, the resolve rate differences are tiny—less than a percentage point across all approaches on 300 instances, so these aren't meaningful improvements. RepoBench-R shows similarly marginal gains around 0.75pp, and I need to examine what the actual test set performance looks like.

For temperature tuning, τ=0.1 performs slightly better than the current τ=0.05 across strategies, though the ranking starts to break down at τ=0.2, suggesting this finding is somewhat dependent on the specific regime. Dynamic mining during training shows a modest edge for embedding-based approaches, but it doesn't fundamentally shift the overall conclusions.

Looking at the hop distance ablation, 2-hop gives the best median performance—1-hop is too restrictive and forces fallback to random sampling, while 3-hop introduces noise without meaningful structural benefit, all within sub-0.5pp margins. For data scaling, the embedding advantage emerges gradually from 1K to 5K instances, growing sub-linearly rather than proportionally. Finally, combining embedding and structural fusion heads yields only marginal gains over embedding alone, while structural-only performs noticeably worse due to information loss.

Now examining the failure analysis—I'm categorizing 50 cases where SweRank and BM25 fail to see which ones benefit from dataflow reasoning, finding that maybe 30-40% are fundamentally structural problems but dataflow only helps in a subset of those. For the qualitative examples, I can cherry-pick 5-10 compelling cases, though they won't be fully representative of the broader patterns.

I have enough signal to write the comprehensive YAML now, accounting for what tables and figures each experiment produces alongside the analysis text. I need to note that m2_full_qwen and m2_full_starcoder are still running, so I'll structure around that constraint.

For the m2_full results, I'm predicting the median performance across both models: Qwen shows random around 0.530 R@1, embedding slightly better at 0.540, and dataflow dropping back to 0.533 across the three seeds. Starcoder follows a similar pattern with comparable numbers.

Now I'm noticing the observed s42 value for Qwen's random strategy is already 0.5527, which sits near the upper bound of my predicted median range, so I need to recalibrate my expectations for what the full results should look like. Looking at the variance across seeds, s42 hitting 0.5527 is notably higher than s43's trajectory around 0.536, which suggests there's real fluctuation in the results. I'm reconsidering whether the median tier metric represents an average across seeds that pulls the overall mean down, even though individual full-scale runs are outperforming the pilot baseline. ranges are:
- qwen_mean_R1_absolute: [0.51, 0.55] - I think this is the mean R@1 for the BEST strategy on Qwen
  
Actually no, looking more carefully, I think "qwen_mean_R1_absolute" means the mean R@1 for Qwen encoder, probably averaged across strategies or for the primary comparison. Given the range [0.51, 0.55], and the pilot results (random=0.5357, embedding=0.5557, dataflow=0.5436), this seems like it could be the mean across strategies.

In the pilot: mean of (0.5357, 0.5557, 0.5436) = 0.545. That's within [0.51, 0.55].

For median tier, I'd put it at ~0.535, slightly below the pilot due to seed variance. Actually, I'm overthinking this—the user gave me ranges, so let me just pick coherent values within them. I'll set Qwen random at 0.530, embedding at 0.540 with a +1.0pp delta, and dataflow at 0.532 with a +0.2pp delta. For StarCoder, I'm going with random at 0.443, embedding at 0.450 with a +0.7pp delta, and dataflow at 0.437 with a -0.6pp delta.

Now I'm verifying these aggregate to the right ranges: Qwen averages to 0.534 (within [0.51, 0.55]) and StarCoder to 0.443 (within [0.42, 0.47]). Both check out. Now I need to build out the full YAML with expected results, rationales, tables, and figures for each experiment, keeping confidence intervals around 3pp wide. best R@1=0.5527 at step 1000. In the median scenario, the other seeds would be lower. So maybe:
- s42: 0.553 (observed)
- s43: 0.521
- s44: 0.516
- mean: 0.530

That's a big spread. Is 3.7pp spread across seeds realistic? With bootstrap_CI_width of [2.0, 4.0], yes. The CI width comes from the seed variance and eval set variance.

For embedding:
- s42: 0.558
- s43: 0.530
- s44: 0.532
- mean: 0.540

For dataflow:
- s42: 0.545
- s43: 0.524
- s44: 0.527
- mean: 0.532

Now I'm checking the deltas across seeds. In s42, embedding gains 0.5pp over random but dataflow drops 0.8pp, which seems odd given the positive overall mean delta. Let me recalculate the per-seed improvements: embedding shows consistent gains across all three seeds (0.5pp, 0.9pp, 1.6pp), while dataflow is negative for s42 but positive for s43 and s44 (−0.8pp, +0.3pp, +1.0pp).

The mean deltas work out to embedding at +1.0pp and dataflow at +0.2pp, which matches the median tier prediction—noisy results where dataflow sometimes helps and sometimes hurts. The confidence interval for the dataflow improvement would span roughly [−1.5, +1.5], clearly crossing zero. Now I'm ready to structure the YAML output with experiment metadata, expected results including summary metrics and confidence bounds, rationale for the results, and descriptions of the tables and figures I'll include.

Writing YAML experiments...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad6460b5-1e34-405b-972f-17fabddde92e",
  "isSidechain": false,
  "requestId": "req_011Cb2nMxK68YvBNNb4Rw5se",
  "type": "assistant",
  "uuid": "f3f9e060-4e67-44c4-8370-b77b02b95a6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127iQNCuhLTpHHT9akZmchr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19285,
      "cache_read_input_tokens": 11447,
      "output_tokens": 22311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 22311,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 19285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19285
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

_source line 10 · 2026-05-14T16:40:05.412Z_

```yaml
tier: median
narrative_guidance: >
  Claim 1 降级为 "tends to help"：embedding mining 方向正确但 effect size 缩水约 50%，
  多 seed CI 宽（2–4pp），个别 seed delta < 0.5pp。BM25 baseline 方向一致（harm）但
  delta 小且 p > 0.05，CoCoHaNeRe correction 论证从 "empirically verified" 改为
  "BM25 proxy 方向一致但 effect size 不足以排除混杂"。Claim 2 降级为 exploratory
  observation：dataflow 在 Qwen 上 CI 包含 0，StarCoder 上方向为负，合并进 Claim 1
  作为 strategy-encoder interaction case。SWE-bench delta < 1pp 且 CI 包含 0，
  无法作为独立 evidence。论文重心移向 systematic empirical comparison + representation
  geometry analysis。标题用 "Systematic Study"，定位 analysis paper。

imagined_experiments:
  # ============================================================
  # plan_003: SWE-bench Lite end-to-end
  # ============================================================
  - name: "SWE-bench Lite End-to-End Evaluation"
    plan_id: "plan_003"
    description: "3 strategies × best checkpoint (Qwen), Qwen3.6-27B agent, 300 SWE-bench Lite instances"
    expected_results:
      random_resolve_rate_pct: 23.0
      random_resolved_count: 69
      embedding_resolve_rate_pct: 23.7
      embedding_resolved_count: 71
      dataflow_resolve_rate_pct: 23.3
      dataflow_resolved_count: 70
      emb_minus_random_delta_pp: 0.7
      df_minus_random_delta_pp: 0.3
      total_instances: 300
      retrieval_R1_on_swebench_random: 0.41
      retrieval_R1_on_swebench_embedding: 0.42
      retrieval_R1_on_swebench_dataflow: 0.41
    result_rationale: >
      SWE-bench Lite 的 resolve rate 由 agent 生成能力主导，retrieval 只是 pipeline
      的第一步。median 档下 retrieval R@1 delta 仅 ~1pp，传导到 end-to-end 后进一步
      衰减：即使 retrieval 多找对 1-2 个 file，agent 是否能利用这个 file 生成正确 patch
      是独立的噪声源。300 instances 上 2 个 count 的差异对应 ~0.7pp，远不够 statistical
      significance。此外 SWE-bench 的 repo 分布与 SWE-smith training 分布有 domain shift，
      进一步压缩了 retrieval improvement 的传导效率。
    tables:
      - name: "Table: SWE-bench Lite Resolve Rate by Strategy"
        columns: ["Strategy", "Resolved", "Total", "Rate (%)", "Δ vs Random (pp)"]
        rows:
          - ["random", 69, 300, 23.0, "—"]
          - ["embedding", 71, 300, 23.7, "+0.7"]
          - ["dataflow", 70, 300, 23.3, "+0.3"]
      - name: "Table: Retrieval-Stage R@1 on SWE-bench Repos"
        columns: ["Strategy", "R@1", "R@5"]
        rows:
          - ["random", 0.41, 0.78]
          - ["embedding", 0.42, 0.79]
          - ["dataflow", 0.41, 0.78]
    figures_description:
      - "Bar chart: resolve rate by strategy with 95% bootstrap CI error bars. All three bars overlap heavily, CI bands span ~4pp each."
      - "Scatter plot: per-instance retrieval correctness vs resolve outcome, colored by strategy. Shows that retrieval success is necessary but not sufficient — many correctly-retrieved instances still fail at generation."
    analysis: >
      SWE-bench delta 不足以支撑独立 claim。resolve rate 差异 < 1pp，在 N=300 上无统计
      显著性（见 plan_016）。Retrieval-stage R@1 差异同样微小（~1pp），说明 SWE-smith
      到 SWE-bench 的 domain gap 进一步压平了 strategy 差异。论文中应作为 "sanity check"
      而非 primary evidence 呈现：确认 negative mining 策略不 harm downstream performance，
      但不能 claim 显著 improvement。需在 limitation 中讨论 300 instances 的 power
      不足问题。

  # ============================================================
  # plan_004: RepoBench-R cross-file retrieval
  # ============================================================
  - name: "RepoBench-R Cross-File Retrieval Evaluation"
    plan_id: "plan_004"
    description: "3 strategies × 3 seeds × 2 encoders, RepoBench-R test_easy (8K, pool~6) + test_hard (8K, pool~18), with 95% CIs"
    expected_results:
      qwen_test_easy:
        random_R1_mean: 0.682
        embedding_R1_mean: 0.688
        dataflow_R1_mean: 0.685
        emb_minus_random_pp: 0.6
        emb_minus_random_CI: [-0.2, 1.4]
      qwen_test_hard:
        random_R1_mean: 0.394
        embedding_R1_mean: 0.404
        dataflow_R1_mean: 0.398
        emb_minus_random_pp: 1.0
        emb_minus_random_CI: [-0.1, 2.1]
      starcoder_test_easy:
        random_R1_mean: 0.621
        embedding_R1_mean: 0.626
        dataflow_R1_mean: 0.618
        emb_minus_random_pp: 0.5
        emb_minus_random_CI: [-0.3, 1.3]
      starcoder_test_hard:
        random_R1_mean: 0.338
        embedding_R1_mean: 0.346
        dataflow_R1_mean: 0.333
        emb_minus_random_pp: 0.8
        emb_minus_random_CI: [-0.4, 2.0]
      overall_delta_pp_range: [0.0, 1.5]
    result_rationale: >
      RepoBench-R 的 test_easy pool 仅 ~6 candidates，所有策略接近 ceiling，strategy
      差异被压缩到 < 1pp。test_hard pool ~18 提供更多区分空间，delta 稍大（~1pp）但仍在
      CI 包含 0 的边缘。RepoBench-R 与 SWE-smith 的 task 定义不同（cross-file completion
      vs bug-fix retrieval），domain shift 进一步削弱了 training-time strategy 差异的
      传导。8K instances 的大样本量使 per-strategy CI 较窄（~1.5pp width），但 delta 的
      CI 仍 ~2pp width，因为 strategy 间的 paired variance 较大。Dataflow 在 StarCoder
      上一致为负（-0.5pp），符合 pilot 发现的 encoder-strategy interaction pattern。
    tables:
      - name: "Table: RepoBench-R R@1 by Strategy × Encoder × Difficulty"
        columns: ["Encoder", "Split", "Random", "Embedding", "Dataflow", "Emb Δ (pp)", "DF Δ (pp)"]
        rows:
          - ["Qwen", "easy", "68.2 ± 0.7", "68.8 ± 0.8", "68.5 ± 0.9", "+0.6", "+0.3"]
          - ["Qwen", "hard", "39.4 ± 1.0", "40.4 ± 1.1", "39.8 ± 1.2", "+1.0", "+0.4"]
          - ["StarCoder", "easy", "62.1 ± 0.6", "62.6 ± 0.7", "61.8 ± 0.8", "+0.5", "−0.3"]
          - ["StarCoder", "hard", "33.8 ± 0.9", "34.6 ± 1.0", "33.3 ± 1.1", "+0.8", "−0.5"]
    figures_description:
      - "Grouped bar chart: R@1 by strategy for each (encoder × split) combination, with 95% seed-level CI error bars. Easy splits visually flat, hard splits show small embedding advantage with overlapping CIs."
      - "Delta plot (forest plot style): embedding-random and dataflow-random deltas with CIs for each (encoder × split). Most CIs cross zero; Qwen hard is the only condition where the lower bound approaches 0."
    analysis: >
      RepoBench-R 提供了 second benchmark 覆盖，方向一致（embedding ≥ random > dataflow
      on StarCoder），但 effect size 不足以独立支撑 claim。test_hard 上的 delta 稍大，
      说明 pool size 对 strategy 效果有调节作用（与 plan_019 呼应）。论文中报告为
      "directional consistency across benchmarks" 而非 "significant improvement on
      second benchmark"。CIs 需在 Table 中完整展示以示 transparency。

  # ============================================================
  # plan_005: Stratified analysis (5 strata)
  # ============================================================
  - name: "Stratified Retrieval Analysis (5 Strata)"
    plan_id: "plan_005"
    description: "分层分析：repo size / pool size / query-pos similarity / structural data availability / neg_difficulty quartile"
    expected_results:
      stratum_1_repo_size:
        small_lt50_emb_delta_pp: 1.8
        medium_50_200_emb_delta_pp: 1.2
        large_200_500_emb_delta_pp: 0.6
        xlarge_500plus_emb_delta_pp: 0.4
      stratum_2_pool_size:
        pool_lt10_emb_delta_pp: 0.3
        pool_10_50_emb_delta_pp: 1.1
        pool_50plus_emb_delta_pp: 0.7
      stratum_3_query_pos_sim:
        high_sim_gt098_emb_delta_pp: 0.5
        medium_sim_090_098_emb_delta_pp: 1.3
        low_sim_lt090_emb_delta_pp: 1.0
      stratum_4_structural_availability:
        with_dataflow_34pct:
          random_R1: 0.538
          embedding_R1: 0.548
          dataflow_R1: 0.544
          df_minus_random_pp: 0.6
          emb_minus_random_pp: 1.0
        fallback_66pct:
          random_R1: 0.526
          embedding_R1: 0.536
          dataflow_R1: 0.527
          df_minus_random_pp: 0.1
          emb_minus_random_pp: 1.0
      stratum_5_neg_difficulty_quartile:
        Q1_easiest:
          emb_delta_pp: 0.3
          df_delta_pp: -0.2
        Q2:
          emb_delta_pp: 0.8
          df_delta_pp: 0.1
        Q3:
          emb_delta_pp: 1.4
          df_delta_pp: 0.5
        Q4_hardest:
          emb_delta_pp: 1.6
          df_delta_pp: 1.2
    result_rationale: >
      Repo size 分层：小 repo 的 pool 小、diversity 低，embedding mining 更容易找到有意义
      的 hard negatives，所以 delta 最大。大 repo 中 pool 大但 noise 也大（更多 unrelated
      files），embedding mining 优势被稀释。Pool size 分层与 repo size 部分共线但不完全：
      pool < 10 时 all strategies 接近 ceiling 所以 delta 小；pool 10-50 是 sweet spot；
      pool 50+ 时 noise 增加。Query-pos similarity 分层：high sim (> 0.98，Qwen 主导)
      表明 representation 已饱和，embedding negatives 不够 hard，delta 小；medium sim
      区间 embedding mining 最 effective。Structural availability 分层：34% 有 dataflow
      数据的 instances 上 dataflow strategy 有 +0.6pp 优势（真正用到了 structural signal），
      但 66% fallback instances 上 dataflow ≈ random（因为 fallback 到 random sampling），
      整体被 dilute。Neg difficulty quartile：Q4（最难 negatives）时 embedding 和
      dataflow 都 help 最多，因为这些 cases 正是模型最 confuse 的地方，harder negatives
      提供最大 gradient signal。但 Q1-Q2 占比大，dilute 了整体 effect。
    tables:
      - name: "Table: Embedding Delta by Repo Size Stratum (Qwen)"
        columns: ["Stratum", "N instances", "Random R@1", "Emb R@1", "Δ (pp)", "95% CI"]
        rows:
          - ["small (<50)", 500, 0.571, 0.589, "+1.8", "[-0.5, 4.1]"]
          - ["medium (50-200)", 4096, 0.542, 0.554, "+1.2", "[0.0, 2.4]"]
          - ["large (200-500)", 13628, 0.531, 0.537, "+0.6", "[-0.3, 1.5]"]
          - ["xlarge (500+)", 25949, 0.524, 0.528, "+0.4", "[-0.5, 1.3]"]
      - name: "Table: Strategy Delta by Structural Data Availability (Qwen)"
        columns: ["Stratum", "N", "Random R@1", "Emb R@1", "DF R@1", "Emb Δ", "DF Δ"]
        rows:
          - ["with dataflow (34%)", "~15K", 0.538, 0.548, 0.544, "+1.0", "+0.6"]
          - ["fallback (66%)", "~29K", 0.526, 0.536, 0.527, "+1.0", "+0.1"]
      - name: "Table: Strategy Delta by Neg Difficulty Quartile (Qwen)"
        columns: ["Quartile", "Margin range", "Emb Δ (pp)", "DF Δ (pp)"]
        rows:
          - ["Q1 (easiest)", "> 0.15", "+0.3", "−0.2"]
          - ["Q2", "0.08–0.15", "+0.8", "+0.1"]
          - ["Q3", "0.02–0.08", "+1.4", "+0.5"]
          - ["Q4 (hardest)", "< 0.02", "+1.6", "+1.2"]
    figures_description:
      - "Heatmap: strategy delta (pp) across (stratum × strategy) combinations. Color intensity encodes delta magnitude. Shows clear gradient for neg_difficulty quartile but noisy pattern for repo size."
      - "Line plot: embedding delta vs pool size (continuous), with LOESS smoothing. Shows inverted-U shape peaking at pool ~30-50, declining at pool > 100."
      - "Stacked bar: proportion of instances in each stratum, overlaid with per-stratum delta. Visualizes that the high-delta strata (small repo, Q4 difficulty) contain few instances, explaining why overall delta is modest."
    analysis: >
      分层分析揭示了 effect size heterogeneity：embedding mining 在 small repo / high
      difficulty / medium similarity 条件下效果最好，但这些条件在实际分布中占比小。
      Structural availability 分层确认了 dataflow 的 conditional benefit 完全来自有
      structural data 的 34%（delta +0.6pp），fallback 的 66% 贡献为零。这解释了为什么
      overall dataflow delta 被 dilute 到接近 0。Neg difficulty quartile 分析提供了
      最清晰的 mechanistic story：当 negatives 足够 hard（Q4），both strategies help；
      当 negatives 太 easy（Q1），neither helps much。这支持 representation geometry
      explanation 但 effect size 不足以作为独立 claim。

  # ============================================================
  # plan_007: Hop-count ablation
  # ============================================================
  - name: "Call-Graph Hop-Count Ablation"
    plan_id: "plan_007"
    description: "1-hop vs 2-hop vs 3-hop call-graph bounding for dataflow negative selection"
    expected_results:
      qwen_1hop_df_R1: 0.530
      qwen_2hop_df_R1: 0.532
      qwen_3hop_df_R1: 0.529
      starcoder_1hop_df_R1: 0.434
      starcoder_2hop_df_R1: 0.437
      starcoder_3hop_df_R1: 0.436
      qwen_2hop_minus_1hop_pp: 0.2
      qwen_2hop_minus_3hop_pp: 0.3
      eligible_negatives_per_query:
        hop_1: 3.2
        hop_2: 8.7
        hop_3: 14.1
      fallback_to_random_pct:
        hop_1: 42
        hop_2: 28
        hop_3: 18
    result_rationale: >
      1-hop 限制太严格：平均每 query 只有 3.2 个 eligible dataflow-disconnected negatives，
      42% 的 queries 不得不 fallback 到 random，稀释了 structural signal。2-hop 是
      precision-recall sweet spot：8.7 eligible negatives 足够采样，fallback 率降到 28%。
      3-hop 进一步扩大 candidate pool 但引入 semantically distant files（3-hop 以外的
      files 很可能本来就和 query 无关），负 signal 质量下降，反而略差于 2-hop。但三者
      差异均 < 0.5pp，在 noise range 内，不构成 strong ablation signal。这也反映了
      median 档下 dataflow strategy 本身 effect size 就小，hop-count 作为 second-order
      effect 自然更小。
    tables:
      - name: "Table: Dataflow R@1 by Hop Count"
        columns: ["Encoder", "1-hop", "2-hop", "3-hop", "Best"]
        rows:
          - ["Qwen", 0.530, 0.532, 0.529, "2-hop"]
          - ["StarCoder", 0.434, 0.437, 0.436, "2-hop"]
      - name: "Table: Negative Pool Statistics by Hop Count"
        columns: ["Hops", "Mean eligible neg/query", "Fallback-to-random %"]
        rows:
          - [1, 3.2, "42%"]
          - [2, 8.7, "28%"]
          - [3, 14.1, "18%"]
    figures_description:
      - "Line plot: R@1 vs hop count (1, 2, 3) for both encoders. Nearly flat lines with error bars overlapping, showing 2-hop is marginally best."
      - "Histogram: distribution of eligible negatives per query at each hop count. 1-hop heavily left-skewed (many zeros), 2-hop more balanced, 3-hop right-shifted."
    analysis: >
      2-hop 作为默认设置是合理的，但 ablation signal 太弱（< 0.5pp）无法 claim hop count
      是 critical design choice。放入 appendix 作为 hyperparameter justification 即可。
      更重要的 takeaway 是 1-hop 的 high fallback rate（42%），说明 inter-procedural
      dataflow 的 coverage 本身就有限——这与 plan_005 structural availability 分层的
      34% 数字一致。

  # ============================================================
  # plan_008: Training data size scaling
  # ============================================================
  - name: "Training Data Size Scaling"
    plan_id: "plan_008"
    description: "1K vs 3K vs 5K training instances × 3 strategies, Qwen encoder"
    expected_results:
      qwen_1K:
        random_R1: 0.498
        embedding_R1: 0.501
        dataflow_R1: 0.495
        emb_delta_pp: 0.3
      qwen_3K:
        random_R1: 0.519
        embedding_R1: 0.528
        dataflow_R1: 0.521
        emb_delta_pp: 0.9
      qwen_5K:
        random_R1: 0.530
        embedding_R1: 0.540
        dataflow_R1: 0.532
        emb_delta_pp: 1.0
      scaling_slope_R1_per_1K: 0.008
    result_rationale: >
      1K instances 时所有策略都 underfit：training data 不足以让 contrastive loss 充分
      学习，absolute R@1 低（~0.50）。Embedding mining 在 1K 时优势最小（+0.3pp），
      因为 1K instances 中 embedding-distance 的 top-k negatives 覆盖了 corpus 的较小
      subset，mining quality 受限于 candidate pool diversity。3K 到 5K 的 scaling 呈
      sub-linear 增长（+1.1pp absolute from 3K→5K vs +2.1pp from 1K→3K），说明
      returns diminishing。Strategy delta 的 scaling 也 sub-linear：embedding 优势在
      3K 时已接近 5K 水平。这表明 effect size 的上限由 pretrained representation quality
      决定，不会随 data 无限增大。
    tables:
      - name: "Table: R@1 by Data Size × Strategy (Qwen)"
        columns: ["Size", "Random", "Embedding", "Dataflow", "Emb Δ (pp)"]
        rows:
          - ["1K", 0.498, 0.501, 0.495, "+0.3"]
          - ["3K", 0.519, 0.528, 0.521, "+0.9"]
          - ["5K (full)", 0.530, 0.540, 0.532, "+1.0"]
    figures_description:
      - "Line plot: R@1 vs training size for each strategy. Three upward-sloping lines with diminishing returns. Embedding line consistently above random but gap narrows at 1K."
      - "Bar chart: embedding delta (pp) at each data size. Shows delta growing from 0.3 to 1.0 as data increases, suggesting mining benefit requires sufficient data diversity."
    analysis: >
      Data scaling 是 positive signal：说明 embedding mining 的 benefit 不是 overfitting
      artifact（否则小数据时 delta 应更大）。但 sub-linear scaling 和 5K 时仍只有 +1.0pp
      的 delta 说明 pretrained representation quality 是 bottleneck，更多 data 不会
      dramatically 改变 strategy ranking。适合放入 appendix，支撑 "mining benefit is
      real but modest" 的 narrative。

  # ============================================================
  # plan_009: Fusion head ablation
  # ============================================================
  - name: "Fusion Head Ablation"
    plan_id: "plan_009"
    description: "Embedding-only vs structural-features-only vs combined scoring head"
    expected_results:
      qwen_embedding_only_R1: 0.539
      qwen_structural_only_R1: 0.412
      qwen_combined_R1: 0.541
      starcoder_embedding_only_R1: 0.449
      starcoder_structural_only_R1: 0.378
      starcoder_combined_R1: 0.451
      combined_minus_embedding_only_pp: 0.2
    result_rationale: >
      Structural-features-only（仅用 dataflow connectivity、call-graph distance 等
      discrete features）大幅落后，因为 binary/categorical structural features 的
      信息量远不及 dense embedding。Combined head 相比 embedding-only 仅 +0.2pp，
      因为在 median 档下 structural signal 本身就弱（plan_005 已示），fusion 无法
      从弱 signal 中 extract 出更多 information。这说明 structural information 的
      value 主要体现在 negative selection（training time）而非 scoring（inference time）。
    tables:
      - name: "Table: Fusion Head Ablation R@1"
        columns: ["Encoder", "Emb-only", "Struct-only", "Combined", "Combined−Emb (pp)"]
        rows:
          - ["Qwen", 0.539, 0.412, 0.541, "+0.2"]
          - ["StarCoder", 0.449, 0.378, 0.451, "+0.2"]
    figures_description:
      - "Bar chart: R@1 by head type × encoder. Structural-only bar dramatically lower, combined and embedding-only nearly identical."
    analysis: >
      确认 StructFuse 的 value 在 training-time negative selection 而非 inference-time
      feature fusion。Combined head 的 marginal gain 可能不值得 inference-time 的
      CodeQL dependency。论文中作为 appendix ablation，支撑 "negative selection is the
      key mechanism" 的 argument。

  # ============================================================
  # plan_010: Dataflow-distance weighted negatives
  # ============================================================
  - name: "Dataflow-Distance Weighted vs Binary Negatives"
    plan_id: "plan_010"
    description: "Weighted sampling by dataflow distance vs binary connected/disconnected"
    expected_results:
      qwen_binary_df_R1: 0.532
      qwen_weighted_df_R1: 0.535
      starcoder_binary_df_R1: 0.437
      starcoder_weighted_df_R1: 0.439
      weighted_minus_binary_pp: 0.3
      weighted_minus_binary_CI: [-0.8, 1.4]
    result_rationale: >
      Distance-weighted sampling 理论上应该更好：给距离更远（更 disconnected）的
      negatives 更高采样概率，提供更 clean 的 structural signal。但在 median 档下
      dataflow strategy 本身 effect size 就小，在此基础上的 second-order refinement
      自然更小（+0.3pp），CI 宽且包含 0。实际上 binary 和 weighted 的差异主要来自
      少数 outlier queries（dataflow distance 分布高度 skewed），大多数 queries 的
      negatives 在两种 scheme 下 overlap 很大。
    tables:
      - name: "Table: Binary vs Weighted Dataflow Negatives"
        columns: ["Encoder", "Binary DF R@1", "Weighted DF R@1", "Δ (pp)"]
        rows:
          - ["Qwen", 0.532, 0.535, "+0.3"]
          - ["StarCoder", 0.437, 0.439, "+0.2"]
    figures_description:
      - "Paired scatter: per-query R@1 difference (weighted − binary) vs dataflow distance range. Most queries cluster near 0 difference; outliers with high distance range show positive delta."
    analysis: >
      Effect 太小，不值得增加 pipeline complexity。Binary 作为默认 simple choice 是合理的。
      放入 appendix 一句话即可。

  # ============================================================
  # plan_011: Failure analysis
  # ============================================================
  - name: "SWE-bench Failure Analysis"
    plan_id: "plan_011"
    description: "50 SweRank/BM25 failures, categorize by whether dataflow helps"
    expected_results:
      total_failures_analyzed: 50
      category_structural_gap: 14
      category_lexical_gap: 18
      category_multi_file_dependency: 8
      category_other: 10
      df_helps_in_structural_gap_pct: 57
      df_helps_overall_pct: 28
      emb_helps_overall_pct: 36
    result_rationale: >
      50 个 failure cases 中，仅 14 个（28%）属于 structural gap（即 gold file 与 query
      有 dataflow 关系但无 lexical similarity）。在这 14 个中，dataflow strategy 成功
      retrieve 了 8 个（57%），但剩余 6 个仍然 fail 因为 structural data 不覆盖（34%
      coverage limitation）。最大的 failure category 是 lexical gap（36%，query 描述
      与 target file 用语完全不同），这两种 strategy 都无法解决。这解释了为什么 overall
      effect size 小：真正 benefit from structural signal 的 cases 只占 ~28%，且其中
      仍有近半 coverage 不足。
    tables:
      - name: "Table: Failure Category Distribution"
        columns: ["Category", "Count", "%", "DF helps", "Emb helps"]
        rows:
          - ["Structural gap", 14, "28%", "8 (57%)", "5 (36%)"]
          - ["Lexical gap", 18, "36%", "3 (17%)", "6 (33%)"]
          - ["Multi-file dependency", 8, "16%", "4 (50%)", "5 (63%)"]
          - ["Other", 10, "20%", "1 (10%)", "2 (20%)"]
    figures_description:
      - "Stacked horizontal bar: failure categories with sub-bars showing DF-helps vs DF-not-helps. Structural gap bar has the highest DF-helps proportion but is a minority category."
    analysis: >
      Failure analysis 提供了 qualitative evidence 支撑 "structural signal helps in
      specific conditions" 的 narrative，但也暴露了 ceiling：真正 structural gap 的
      cases 只占 28%，coverage 限制了其中一半。适合放入 Section 5 的 analysis 段落，
      不足以 support independent claim。

  # ============================================================
  # plan_012: Qualitative examples
  # ============================================================
  - name: "Qualitative Case Studies"
    plan_id: "plan_012"
    description: "5-10 cases where structural negatives changed retrieval outcome"
    expected_results:
      total_cases_selected: 7
      cases_df_uniquely_helps: 3
      cases_emb_uniquely_helps: 2
      cases_both_help: 2
      avg_gold_rank_improvement_df: 4.2
      avg_gold_rank_improvement_emb: 2.8
    result_rationale: >
      Cherry-picking 7 个 illustrative cases。3 个 cases 中 dataflow strategy 将 gold
      file 从 rank 8-15 提升到 rank 1-3（大幅改善），这些 cases 的共同特征是 gold file
      与 query 有 call-chain dependency 但无 keyword overlap。2 个 cases 中 embedding
      strategy 独特帮助（gold file 与 query 有 similar variable naming 但 random
      negatives 中缺少 near-miss distractors）。但 cherry-picked cases 不代表 overall
      distribution（见 plan_011 的 28% structural gap rate）。
    tables:
      - name: "Table: Selected Qualitative Cases"
        columns: ["Case", "Repo", "Issue type", "Random rank", "Emb rank", "DF rank", "Key observation"]
        rows:
          - [1, "repo_A", "missing import", 12, 8, 2, "DF finds cross-module callee"]
          - [2, "repo_B", "API mismatch", 9, 3, 4, "Emb finds similar naming"]
          - [3, "repo_C", "config propagation", 15, 11, 1, "DF traces config flow"]
          - [4, "repo_D", "type error", 6, 2, 3, "Both find related types"]
          - [5, "repo_E", "null pointer", 11, 7, 3, "DF finds data source"]
          - [6, "repo_F", "method override", 4, 1, 5, "Emb captures signature sim"]
          - [7, "repo_G", "circular dep", 14, 10, 2, "DF traces dependency cycle"]
    figures_description:
      - "Side-by-side code snippets for top 3 DF-helps cases, showing query → gold file with dataflow path highlighted. Annotated with rank under each strategy."
    analysis: >
      Qualitative examples 是论文的 illustration 而非 evidence。选择具有 pedagogical
      value 的 cases 来解释 mechanism。在 median 档下，需要 caveat "these are selected
      to illustrate the mechanism; overall effect size is modest (Table X)"。

  # ============================================================
  # plan_014: Temperature ablation
  # ============================================================
  - name: "Temperature Ablation"
    plan_id: "plan_014"
    description: "τ ∈ {0.05, 0.1, 0.2} × 3 strategies × 2 encoders"
    expected_results:
      qwen:
        tau_005:
          random_R1: 0.530
          embedding_R1: 0.540
          dataflow_R1: 0.532
          emb_delta_pp: 1.0
        tau_010:
          random_R1: 0.537
          embedding_R1: 0.545
          dataflow_R1: 0.537
          emb_delta_pp: 0.8
        tau_020:
          random_R1: 0.521
          embedding_R1: 0.526
          dataflow_R1: 0.520
          emb_delta_pp: 0.5
      starcoder:
        tau_005:
          random_R1: 0.443
          embedding_R1: 0.450
          dataflow_R1: 0.437
          emb_delta_pp: 0.7
        tau_010:
          random_R1: 0.451
          embedding_R1: 0.457
          dataflow_R1: 0.446
          emb_delta_pp: 0.6
        tau_020:
          random_R1: 0.435
          embedding_R1: 0.438
          dataflow_R1: 0.430
          emb_delta_pp: 0.3
      optimal_tau: 0.1
      strategy_ranking_preserved_across_tau: true
      delta_shrinks_at_high_tau: true
    result_rationale: >
      τ=0.05（当前默认）可能过低：contrastive loss 的 gradient 过于 sharp，模型对 hard
      negatives 过度 sensitive，导致 overfitting（plan_002 中 step 500 后即 overfit）。
      τ=0.1 在 median 档下反而略好：gradient 更 smooth，模型更 robust，absolute R@1
      比 τ=0.05 高 ~0.7pp（Qwen）和 ~0.8pp（StarCoder）。但 strategy delta 在 τ=0.1
      时略小（0.8pp vs 1.0pp Qwen），因为 smoother gradient 也 smooth 掉了 hard
      negative 的 extra signal。τ=0.2 过高：loss landscape 太 flat，training signal 不足，
      all strategies 退化。关键发现：strategy ranking（embedding > random ≥ dataflow）
      在所有 τ 下保持一致，说明 finding 不是 regime-specific。但 delta 随 τ 增大而
      缩小，表明在 optimal τ 下 effect size 可能更小。这是 median 档的典型 pattern：
      finding 方向 robust 但 magnitude 依赖 hyperparameter。
    tables:
      - name: "Table: R@1 by Temperature × Strategy (Qwen)"
        columns: ["τ", "Random", "Embedding", "Dataflow", "Emb Δ (pp)", "Best strat"]
        rows:
          - [0.05, 0.530, 0.540, 0.532, "+1.0", "embedding"]
          - [0.10, 0.537, 0.545, 0.537, "+0.8", "embedding"]
          - [0.20, 0.521, 0.526, 0.520, "+0.5", "embedding"]
      - name: "Table: R@1 by Temperature × Strategy (StarCoder)"
        columns: ["τ", "Random", "Embedding", "Dataflow", "Emb Δ (pp)", "Best strat"]
        rows:
          - [0.05, 0.443, 0.450, 0.437, "+0.7", "embedding"]
          - [0.10, 0.451, 0.457, 0.446, "+0.6", "embedding"]
          - [0.20, 0.435, 0.438, 0.430, "+0.3", "embedding"]
    figures_description:
      - "Line plot: R@1 vs τ for each strategy, dual-panel (Qwen | StarCoder). All strategies show inverted-U with peak at τ=0.1. Embedding line consistently above random."
      - "Bar chart: embedding delta (pp) vs τ. Monotonically decreasing from τ=0.05 to τ=0.2, showing that harder temperature amplifies strategy differences."
    analysis: >
      Temperature ablation 提供两个 key findings：(1) strategy ranking 在 τ 范围内
      preserved（robustness check passed），(2) optimal τ 可能是 0.1 而非 0.05，但在
      optimal τ 下 embedding delta 只有 0.6-0.8pp。这要求论文报告 best-τ 结果时
      acknowledge effect size 进一步缩小。建议报告 τ=0.05 作为 primary（与 prior work
      对齐）加 τ sensitivity 在 appendix。如果 reviewer 质疑 regime-specificity，
      可以 argue ranking preserved 但 concede magnitude is τ-dependent。

  # ============================================================
  # plan_015: Dynamic mining baseline
  # ============================================================
  - name: "Dynamic vs Static Embedding Mining"
    plan_id: "plan_015"
    description: "Dynamic re-mine embedding negatives per epoch vs static (mine once from pretrained), Qwen encoder"
    expected_results:
      qwen_static_emb_R1: 0.540
      qwen_dynamic_emb_R1: 0.544
      dynamic_minus_static_pp: 0.4
      dynamic_minus_static_CI: [-0.8, 1.6]
      training_time_ratio_dynamic_vs_static: 2.3
    result_rationale: >
      Dynamic mining 每个 epoch 用 current encoder 重新计算 embeddings 并 re-mine
      negatives，理论上 negatives 始终 adaptive to current model state。但在 median
      档下 static mining 本身 effect size 就小（+1.0pp），dynamic 的 incremental gain
      仅 +0.4pp，因为 (1) training 只跑 2-3 epochs，encoder 变化不大，re-mining 的
      negatives 与 static 的 overlap 很大（estimated > 80% overlap），(2) dynamic
      mining 需要 per-epoch full-corpus encoding，training time 翻 2.3x，cost-benefit
      不划算。CI 包含 0，说明 gain 不 significant。这个结果也部分缓解了 "static mining
      confound" 的 reviewer concern：dynamic 没有 dramatically 改变 picture。
    tables:
      - name: "Table: Static vs Dynamic Embedding Mining (Qwen)"
        columns: ["Mining", "R@1", "Δ vs static (pp)", "Train time (h)", "CI"]
        rows:
          - ["static", 0.540, "—", 7.5, "—"]
          - ["dynamic", 0.544, "+0.4", 17.3, "[-0.8, 1.6]"]
    figures_description:
      - "Bar chart: R@1 for static vs dynamic with CI error bars. Bars nearly equal height with overlapping CIs."
      - "Venn diagram or overlap histogram: negative set overlap between static and dynamic at epoch 1, 2, 3. Shows > 80% overlap at all epochs."
    analysis: >
      Dynamic mining 是 expensive 的 marginal improvement。论文中一句话 dismiss
      this confound："We additionally tested dynamic re-mining (per-epoch) and found
      no significant improvement over static mining (Δ=+0.4pp, p=0.38), likely because
      the encoder changes minimally over 2-3 epochs."

  # ============================================================
  # plan_016: Bootstrap CI for SWE-bench
  # ============================================================
  - name: "Bootstrap CI for SWE-bench Resolve Rate"
    plan_id: "plan_016"
    description: "95% bootstrap confidence intervals for all strategy comparisons on SWE-bench Lite"
    expected_results:
      n_bootstrap_samples: 10000
      random_resolve_rate_pct: 23.0
      random_CI: [18.3, 27.7]
      embedding_resolve_rate_pct: 23.7
      embedding_CI: [18.7, 28.3]
      dataflow_resolve_rate_pct: 23.3
      dataflow_CI: [18.3, 28.0]
      emb_minus_random_delta_pp: 0.7
      emb_minus_random_CI: [-3.2, 4.5]
      emb_minus_random_p_value: 0.62
      df_minus_random_delta_pp: 0.3
      df_minus_random_CI: [-3.8, 4.4]
      df_minus_random_p_value: 0.78
      any_comparison_significant: false
    result_rationale: >
      N=300 binary outcomes（resolve/not-resolve）的 bootstrap CI 很宽：individual
      strategy 的 CI width ~9.5pp，paired delta 的 CI width ~7.7pp。这是因为 binary
      outcome 的 variance 最大（Bernoulli variance = p(1-p) ≈ 0.18），300 instances
      给出的 standard error ≈ sqrt(0.18/300) ≈ 0.024 = 2.4pp，95% CI ≈ ±4.7pp。
      在 delta < 1pp 的情况下，不可能 achieve significance。这是 fundamental power
      limitation，不是方法问题。Even with 3000 instances (full SWE-bench)，delta 0.7pp
      仍需要 N > 15000 才能 detect with 80% power。
    tables:
      - name: "Table: SWE-bench Bootstrap CIs"
        columns: ["Comparison", "Δ (pp)", "95% CI", "p-value", "Significant?"]
        rows:
          - ["emb − random", "+0.7", "[-3.2, 4.5]", 0.62, "No"]
          - ["df − random", "+0.3", "[-3.8, 4.4]", 0.78, "No"]
          - ["emb − df", "+0.3", "[-3.5, 4.2]", 0.73, "No"]
    figures_description:
      - "Forest plot: paired delta with 95% CI for each comparison. All CIs cross zero, none close to significance."
      - "Power analysis curve: required N to detect Δ=0.7pp at 80% power. Shows N > 15000, far beyond SWE-bench Lite's 300."
    analysis: >
      SWE-bench CIs 确认 end-to-end evaluation 对 retrieval strategy 的 sensitivity
      不足。这不是 negative result 而是 power limitation。论文中必须 transparently 报告
      "SWE-bench evaluation confirms no strategy harms downstream performance, but
      the benchmark is underpowered to detect the retrieval-stage deltas we observe
      (< 1pp)"。Power analysis figure 可放入 appendix 支撑此 argument。

  # ============================================================
  # plan_017: Inference-time graph method comparison
  # ============================================================
  - name: "Inference-Time Graph Method Literature Comparison"
    plan_id: "plan_017"
    description: "Analysis-only comparison with CodexGraph, LocAgent, RANGER etc. (no experiment)"
    expected_results:
      papers_compared: 8
      key_distinction: "training-time mining vs inference-time navigation"
      complementary_not_competing: true
      overlap_with_our_approach: "minimal — they inject structure at inference, we use structure for training data curation"
    result_rationale: >
      8 篇 inference-time graph 方法（CodexGraph, LocAgent, RANGER, GraphCoder, ARISE,
      RepoGraph, CodeGRAG, CodeRAG）都在 inference 时构建或查询 code graph。与 StructFuse
      的区别是 fundamental：我们在 training time 用 graph 选 negatives，他们在 inference
      time 用 graph navigate。二者理论上 complementary（可以用 StructFuse 训练的
      retriever 作为这些 inference-time methods 的 backbone）。但 median 档下我们
      没有实验验证 complementarity，只能 argue in principle。这个 literature gap 在
      前几轮 review 中被 flagged（best-R2-W5），written comparison 应该足够 address。
    tables:
      - name: "Table: Comparison with Inference-Time Graph Methods"
        columns: ["Method", "Graph type", "When used", "Scope", "Complementary?"]
        rows:
          - ["CodexGraph", "Repository graph", "Inference", "Navigation", "Yes"]
          - ["LocAgent", "Code structure", "Inference", "Localization", "Yes"]
          - ["RANGER", "AST + deps", "Inference", "Ranking", "Yes"]
          - ["StructFuse (ours)", "Dataflow", "Training", "Neg mining", "—"]
    figures_description:
      - "Taxonomy diagram: 2×2 matrix of (training/inference) × (text-only/structure-enhanced) methods, positioning StructFuse in the training+structure quadrant alongside ANCE/curriculum mining in training+text."
    analysis: >
      Discussion section 需要明确 position StructFuse 为 complementary approach，not
      competing with inference-time methods。这也为 future work 提供了 natural extension：
      combine StructFuse-trained retriever with inference-time graph navigation。
      Median 档下这是 speculative future work 而非 verified claim。

  # ============================================================
  # plan_018: BM25 negative baseline
  # ============================================================
  - name: "BM25 Hard Negative Baseline"
    plan_id: "plan_018"
    description: "BM25-based hard negatives as 4th strategy, 1 seed × 2 encoders, compare with random/embedding/dataflow"
    expected_results:
      qwen_bm25_R1: 0.521
      qwen_random_R1: 0.530
      qwen_embedding_R1: 0.540
      qwen_bm25_minus_random_pp: -0.9
      qwen_bm25_minus_random_CI: [-2.8, 1.0]
      qwen_bm25_minus_random_p_value: 0.12
      starcoder_bm25_R1: 0.436
      starcoder_random_R1: 0.443
      starcoder_embedding_R1: 0.450
      starcoder_bm25_minus_random_pp: -0.7
      starcoder_bm25_minus_random_CI: [-2.5, 1.1]
      starcoder_bm25_minus_random_p_value: 0.18
      bm25_rank: "worst among 4 strategies"
      bm25_vs_embedding_delta_pp_qwen: -1.9
      bm25_vs_embedding_delta_pp_starcoder: -1.4
    result_rationale: >
      BM25 negatives 是 lexical-similarity top-k，与 true embedding distance negatives
      的 selection 方式 fundamentally 不同。BM25 top-k 主要 capture keyword overlap
      （function names, import statements），这些 "negatives" 中很多实际上是 semantically
      related（可能包含 false negatives / actual positives mislabeled as negatives），
      导致 noisy training signal。在 median 档下，BM25 harm 方向正确（-0.9pp Qwen,
      -0.7pp StarCoder），但 delta 小于 CoCoHaNeRe 报告的 -27pp。原因：(1) 我们的
      training pipeline 更 robust（proper temperature, early stopping），(2) pool=50
      限制了 BM25 negatives 的 "hardness"（不像 CoCoHaNeRe 的 full-corpus mining）。
      p > 0.05 说明 harm 不 significant，but direction is consistent。这 partially
      closes the correction argument：可以 say "BM25-proxy negatives harm in the
      direction CoCoHaNeRe reports, but the magnitude in our controlled setup is much
      smaller, suggesting their -27pp included other confounds beyond negative source"。
      不能 fully close（p > 0.05），只能 partially support。
    tables:
      - name: "Table: 4-Strategy Comparison R@1"
        columns: ["Strategy", "Qwen R@1", "StarCoder R@1", "Qwen Δ vs Random", "StarCoder Δ vs Random"]
        rows:
          - ["random", 0.530, 0.443, "—", "—"]
          - ["embedding", 0.540, 0.450, "+1.0", "+0.7"]
          - ["dataflow", 0.532, 0.437, "+0.2", "−0.6"]
          - ["BM25", 0.521, 0.436, "−0.9", "−0.7"]
      - name: "Table: BM25 vs Embedding Delta (the CoCoHaNeRe gap)"
        columns: ["Encoder", "BM25 R@1", "Emb R@1", "Δ (pp)", "CoCoHaNeRe reported", "Our explanation"]
        rows:
          - ["Qwen", 0.521, 0.540, "−1.9", "−27", "Different mining protocol, pool size, pipeline robustness"]
          - ["StarCoder", 0.436, 0.450, "−1.4", "n/a", "Consistent direction, smaller magnitude"]
    figures_description:
      - "Bar chart: R@1 for 4 strategies × 2 encoders. BM25 bar clearly lowest, embedding highest. Error bars (1-seed, bootstrap over eval set) show BM25 CI overlapping random."
      - "Scatter plot: per-query BM25-negative similarity vs embedding-negative similarity, colored by whether query was correctly retrieved. Shows that BM25 negatives cluster in a different similarity region (high lexical, medium semantic) than embedding negatives (high semantic)."
      - "Venn diagram: overlap between BM25 top-5 negatives and embedding top-5 negatives. Shows ~30% overlap, confirming they are selecting different negative populations."
    analysis: >
      BM25 baseline 是 median 档下最重要的新增实验。它 partially 但不 fully closes the
      CoCoHaNeRe correction argument。方向一致（BM25 harm, embedding help）支撑了
      "proxy conflation" 的 narrative，但 delta 太小（-0.9pp vs -27pp）且 p > 0.05
      意味着 argument 需要 soften。论文叙事从 "we prove CoCoHaNeRe was wrong" 调整为
      "we observe that BM25-proxy negatives trend toward harm while true embedding
      negatives trend toward benefit, consistent with the hypothesis that CoCoHaNeRe's
      reported -27pp harm was amplified by proxy conflation and other uncontrolled
      factors"。这是 median 档 framing 的核心转变。Need related work 深度对比
      （ANCE, curriculum mining, DPR hard negatives）来 contextualize 为什么
      effect size 在 code domain 普遍 modest。

  # ============================================================
  # plan_019: Pool size sensitivity
  # ============================================================
  - name: "Pool Size Sensitivity Analysis"
    plan_id: "plan_019"
    description: "Strategy ranking stability at pool={50, 100, 200, 500} on SWE-smith validation"
    expected_results:
      qwen:
        pool_50:
          random_R1: 0.530
          embedding_R1: 0.540
          dataflow_R1: 0.532
          ranking: "emb > df > rand"
        pool_100:
          random_R1: 0.412
          embedding_R1: 0.421
          dataflow_R1: 0.413
          ranking: "emb > df ≈ rand"
        pool_200:
          random_R1: 0.328
          embedding_R1: 0.335
          dataflow_R1: 0.330
          ranking: "emb > df ≈ rand"
        pool_500:
          random_R1: 0.241
          embedding_R1: 0.246
          dataflow_R1: 0.244
          ranking: "emb ≈ df ≈ rand"
      starcoder:
        pool_50:
          random_R1: 0.443
          embedding_R1: 0.450
          dataflow_R1: 0.437
          ranking: "emb > rand > df"
        pool_100:
          random_R1: 0.339
          embedding_R1: 0.345
          dataflow_R1: 0.334
          ranking: "emb > rand > df"
        pool_200:
          random_R1: 0.268
          embedding_R1: 0.272
          dataflow_R1: 0.271
          ranking: "emb ≈ df ≈ rand"
        pool_500:
          random_R1: 0.194
          embedding_R1: 0.196
          dataflow_R1: 0.197
          ranking: "df ≈ emb ≈ rand"
      pool_ranking_stable_pct: 62.5
      ranking_crossover_threshold: "pool ≥ 200"
      absolute_R1_decline_per_10x_pool: 0.18
    result_rationale: >
      Pool size 增大时所有 strategies 的 absolute R@1 大幅下降（从 pool=50 的 ~53% 到
      pool=500 的 ~24%），因为 retrieval 的 baseline difficulty 增加。Strategy delta
      也随 pool 增大而压缩：pool=50 时 embedding delta=+1.0pp，pool=500 时仅 +0.5pp。
      原因是大 pool 中 distractors 更 diverse，training-time 的 hard negative strategy
      只 prepare 了模型应对特定 difficulty 分布，但 pool=500 时 test-time 的 difficulty
      distribution 超出了 training-time 的 coverage。在 pool ≥ 200 时偶有 ranking
      交叉（StarCoder pool=500 时 dataflow 反超 embedding by 0.1pp），但差异在 noise
      range 内。Overall ranking stability 62.5%（8 个 encoder×pool 组合中 5 个保持
      embedding > rest），低于 best 档的 >80% 但高于 worst 档的 <50%。这说明 finding
      "directionally holds but weakens" at larger pools，需在论文中 caveat。
    tables:
      - name: "Table: R@1 by Pool Size × Strategy (Qwen)"
        columns: ["Pool", "Random", "Embedding", "Dataflow", "Emb Δ (pp)", "Ranking stable?"]
        rows:
          - [50, 0.530, 0.540, 0.532, "+1.0", "✓"]
          - [100, 0.412, 0.421, 0.413, "+0.9", "✓"]
          - [200, 0.328, 0.335, 0.330, "+0.7", "✓"]
          - [500, 0.241, 0.246, 0.244, "+0.5", "✓"]
      - name: "Table: R@1 by Pool Size × Strategy (StarCoder)"
        columns: ["Pool", "Random", "Embedding", "Dataflow", "Emb Δ (pp)", "Ranking stable?"]
        rows:
          - [50, 0.443, 0.450, 0.437, "+0.7", "✓"]
          - [100, 0.339, 0.345, 0.334, "+0.6", "✓"]
          - [200, 0.268, 0.272, 0.271, "+0.4", "~"]
          - [500, 0.194, 0.196, 0.197, "+0.2", "✗"]
    figures_description:
      - "Line plot: R@1 vs pool size (log scale) for each strategy, dual-panel. All lines decline; strategy gap narrows visibly at pool=200+."
      - "Delta plot: embedding-random delta (pp) vs pool size. Monotonically declining curve, approaching zero at pool=500."
      - "Heatmap: strategy ranking (1st/2nd/3rd) at each pool size × encoder. Shows transition from stable ranking at pool≤100 to unstable at pool≥200."
    figures_description:
      - "Line plot: R@1 vs pool size (log scale) for each strategy, dual-panel (Qwen | StarCoder). All lines decline; strategy gap narrows visibly at pool ≥ 200."
      - "Delta plot: embedding−random delta (pp) vs pool size. Monotonically declining curve, approaching zero at pool = 500."
      - "Heatmap: strategy ranking (1st/2nd/3rd) at each pool size × encoder. Transition from stable ranking at pool ≤ 100 to unstable at pool ≥ 200."
    analysis: >
      Pool size sensitivity 是 median 档下最重要的 external validity check。结果显示
      embedding mining 优势 real 但 diminishing with pool size。论文需要 honestly
      discuss：(1) pool=50 是 validation setup，real-world repo pool 通常 200-1000+，
      (2) at realistic pool sizes the advantage shrinks to ~0.5pp。这强化了
      "systematic study" 而非 "strong method contribution" 的 positioning。建议在
      main paper 中报告 pool=50 和 pool=200 的双 benchmark，并在 limitation 中讨论
      pool=500 的 convergence。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3f9e060-4e67-44c4-8370-b77b02b95a6d",
  "isSidechain": false,
  "requestId": "req_011Cb2nMxK68YvBNNb4Rw5se",
  "type": "assistant",
  "uuid": "bde97d4a-476e-4c16-a4ca-8f71e70ae202",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0127iQNCuhLTpHHT9akZmchr",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19285,
      "cache_read_input_tokens": 11447,
      "output_tokens": 22311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19285,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 22311,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 19285,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19285
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：embedding mining 优势存在但 effect size 缩水约 50%，BM25 部分支持 correction 论证，dataflow 条件性获益噪声大 核心假设：['embedding-random delta 正向但 CI 较宽，个别 seed 差异 < 0.5pp', 'datafl…",
  "leafUuid": "bde97d4a-476e-4c16-a4ca-8f71e70ae202",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic empirical analysis of hard negative mining strategies for code retrieval",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：embedding mining 优势存在但 effect size 缩水约 50%，BM25 部分支持 correction 论证，dataflow 条件性获益噪声大 核心假设：['embedding-random delta 正向但 CI 较宽，个别 seed 差异 < 0.5pp', 'datafl…",
  "leafUuid": "bde97d4a-476e-4c16-a4ca-8f71e70ae202",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic empirical analysis of hard negative mining strategies for code retrieval",
  "sessionId": "88a154e2-ebab-4a41-bc2d-3efe45f9111c"
}
```

---
