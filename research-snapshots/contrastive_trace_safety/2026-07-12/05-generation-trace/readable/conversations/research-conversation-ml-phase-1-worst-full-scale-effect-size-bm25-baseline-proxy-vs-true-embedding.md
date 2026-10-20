# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：full-scale effect size 消失或反转，BM25 baseline 未能区分 proxy vs true embedding，核心叙

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/1808fedb-4d27-4186-8ee0-7e0cdc8eaf16.jsonl`
- **Structured JSON:** [`2e3923b84a27cf9f6a76.json`](../../sessions/2e/2e3923b84a27cf9f6a76.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T16:40:07.992Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T16:40:07.992Z",
  "sessionId": "1808fedb-4d27-4186-8ee0-7e0cdc8eaf16",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：full-scale effect size 消失或反转，BM25 baseline 未能区分 proxy vs true embedding，核心叙事需重建\n核心假设：['embedding-random delta < 0.3pp 且 CI 明确包含 0（至少一个 encoder）', 'dataflow 在两个 encoder 上均无显著获益或 harm', 'BM25 negatives 表现与 embedding negatives 无统计差异 → CoCoHaNeRe correction 论证无法关闭', 'pool ≥ 200 时排名与 pool=50 不一致', 'SWE-bench 无可见差异或方向相反', '数据 pipeline 无 bug（排除实现错误后结果仍如此）']\n关键指标范围：{'qwen_emb_minus_random_R1_pp': [-0.5, 0.5], 'starcoder_emb_minus_random_R1_pp': [-0.8, 0.3], 'qwen_df_minus_random_R1_pp': [-1.0, 0.3], 'starcoder_df_minus_random_R1_pp': [-2.0, 0.0], 'bm25_minus_random_R1_pp': [-1.0, 0.5], 'swebench_resolve_rate_delta_pp': [-1.0, 0.5], 'repobench_R1_delta_pp': [-1.0, 0.5], 'pool_ranking_stable_pct': [0, 50], 'bootstrap_CI_width_R1_pp': [3.0, 6.0], 'qwen_mean_R1_absolute': [0.48, 0.53], 'starcoder_mean_R1_absolute': [0.4, 0.46]}\n叙事方向：三条原始 claim 均无法维持。Reframe 方向：negative result paper —— \"Why Hard Negative Mining Strategies Don't Differentiate for Code Retrieval at Scale\"。核心贡献变为： (1) 大规模控制实验表明 strategy 选择对 code retrieval 的影响被高估，pilot-scale 差异在 full-scale 消失（scale-dependent finding）；(2) representation geometry analysis 仍有价值——作为解释 *为什么* 策略差异消失的框架（margin 在训练后收敛，pretrained geometry 差异被 fine-tuning 抹平）；(3) CoCoHaNeRe 的 BM25-proxy 问题仍可报告为 methodological caution，但从 \"correction\" 降为 \"observation\"。论文定位从 positive contribution 转为 high-quality negative result + methodological contribution。EMNLP Main 仍可投 （negative result papers 有先例），但需要 (a) 足够大的实验规模证明 negative result 可信， (b) mechanistic explanation 为什么不 work，(c) actionable takeaway（practitioners 不需要花 GPU 时间做 fancy mining）。风险：reviewer 可能认为 \"nothing works\" 缺乏 novelty ——需用 representation geometry analysis 的解释深度来弥补。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: structfuse-context\nfocus: D030 修复后验证：新增 plan_018 BM25 baseline（关闭 CoCoHaNeRe correction 论证）、plan_019 pool size sensitivity、plan_004 多 seed CIs、plan_005 structural coverage 分层 + neg_difficulty quartile。Framing 修正：N=2 降级为 observation、Claim 3 降为 supporting methodology、StarCoder decoder-only。Reviewers 应重点评估：(1) BM25 baseline 是否关闭了上一轮最大缺口，(2) 新增实验是否充分回应了上一轮 median/worst 的 \"related work insufficient\" 和 \"effect size marginal\" 问题，(3) 修正后的 N=2 observation framing 是否足够。\n\n## paper_framing.md\n\n# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \"harm\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two decoder-only encoders with distinct pretraining corpora and representation geometries (Qwen2.5-Coder-3B, StarCoder2-3B).\n\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL provides a practical pipeline for computing structural connectivity at scale.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. [Dream [M][W] flag: this is supporting methodology, not a primary research contribution. Drop speculative generalization claims (molecular networks, etc.) — no evidence. Frame as practical tool that enables the study, not a standalone contribution.]\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\n\n- **Headline result template**: \"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\"\n\n## Core Insight\n\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\"\n- Backup: \"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; two decoder-only encoders with distinct pretraining (Fill vs FIM) and representation geometry (pos_sim 0.99 vs 0.80) provide meaningful variation | plan_013 (done), m2_full runs |\n| BM25 vs true embedding negatives? | Run BM25 negatives to empirically verify CoCoHaNeRe used BM25-proxy, closing the correction argument | plan_018 |\n| Pool size sensitivity? | Evaluate at pool {50, 100, 200, 500} to confirm strategy rankings hold at realistic sizes | plan_019 |\n| Stratified by structural data availability? | Report per-stratum R@1 for 34% with structural data vs 66% fallback | plan_005 (extended) |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\n- m1_reextract_v2: expanded extraction for higher coverage\n\n### Planned (priority order):\n- plan_018: BM25 negative baseline (Dream #1 consensus gap — closes CoCoHaNeRe correction argument)\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_019: Pool size sensitivity (Dream consensus — external validity)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark (with multi-seed CIs)\n- plan_015: Dynamic mining baseline\n- plan_005: Stratified analysis (extended: structural-available vs fallback stratum)\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected\n    vs gold statistics'\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: m1_extraction\n  mvp_registry_id: mvp_p1_codeql_feasibility\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- id: plan_002\n  claim: 1\n  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,\n    3 seeds each, Qwen2.5-Coder-3B LoRA'\n  priority: P0\n  gpu_budget_hours: 200\n  deps:\n  - plan_001\n  registry_id: m2_embed_verify\n  mvp_registry_id: mvp_p2b_contrastive_training\n  full_registry_ids:\n  - m2_full_qwen\n  - m2_full_starcoder\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- id: plan_003\n  claim: 1\n  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best\n    checkpoint, Qwen3.6-27B agent'\n  priority: P0\n  gpu_budget_hours: 40\n  deps:\n  - plan_002\n  notes: eval script ready (eval_swebench.py), dry-run passed, 12 SWE-bench repos\n    pre-cloned to /root/autodl-tmp/structfuse/swebench_repos. Awaiting M2 checkpoint.\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no\n    LLM agent'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  notes: eval script ready (eval_repobench.py), dry-run passed. RepoBench-R data via\n    hf_hub_download. test_easy 8K instances (pool ~6), test_hard 8K (pool ~18). Awaiting\n    M2 checkpoint. [Dream fix] Must run with multiple seeds and report 95% CIs — dream\n    reviewers flagged inconsistent statistical reporting (CIs on SWE-bench but not\n    RepoBench-R) across all 3 tiers.\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding\n    negatives 何时最有害'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  notes: 'analysis script ready (analyze_stratified.py), dry-run passed. 3 strata:\n    repo size / pool size / query-positive similarity. Outputs stratified_results.json\n    + plots PDF. Awaiting M2 checkpoints for re-eval. [Dream fix] Must add 2 more\n    strata: (a) structural data availability (34% with dataflow vs 66% fallback) per\n    [B][M][W] all tiers, (b) neg_difficulty quartile analysis per [W] tier. Total\n    5 strata.'\n  status: planned\n- id: plan_006\n  claim: 3\n  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,\n    connected-but-not-gold ratio by repo size'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan_006_scalability\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- id: plan_007\n  claim: 1\n  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Ablation: fusion head (embedding-only vs structural-features-only\n    vs combined)'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether\n    data-flow helps'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_003\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Qualitative examples: 5-10 cases where structural negatives changed\n    retrieval outcome'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Second encoder validation: repeat M2 core comparison (3 strategies,\n    1 seed) on StarCoder-3B or CodeBERT to test architecture generality'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  dream_source: 'best-R1-W1, median-R2-W5: single encoder is primary generality concern.\n    Upgraded to P0 per Reviewer — this is the #1 factor separating WA from WR.'\n  registry_id: plan_013_starcoder\n  full_registry_id: m2_full_starcoder\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- id: plan_014\n  claim: 2\n  description: 'Temperature ablation: τ ∈ {0.05, 0.1, 0.2} for all 3 strategies, test\n    regime-specificity of embedding harm'\n  priority: P1\n  gpu_budget_hours: 70\n  deps:\n  - plan_002\n  dream_source: 'median-R1-W3: τ=0.05 unusually low, finding may be regime-specific'\n  status: planned\n- id: plan_015\n  claim: 2\n  description: 'Dynamic embedding mining baseline: re-mine embedding negatives per\n    epoch vs static (mine once from pretrained). Isolate selection criterion from\n    curriculum shift.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  dream_source: 'best-R1-W2, median-R1-W2: static vs dynamic mining is potential confound\n    for Claim 2'\n  status: planned\n- id: plan_016\n  claim: 1\n  description: 'Bootstrap CI for SWE-bench Lite: add 95% bootstrap confidence intervals\n    to end-to-end resolve rate evaluation'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  dream_source: 'best-R1-W3, worst-R1-W5: +2.0pp on 300 instances needs statistical\n    significance test'\n  status: planned\n- id: plan_017\n  claim: 1\n  description: 'Inference-time graph method comparison: discuss/compare with CodexGraph,\n    LocAgent — is StructFuse complementary or alternative? Analysis complete, document\n    in artifacts/analysis/plan017_literature_comparison.md. Discussion draft in artifacts/paper_drafts/discussion_draft.md.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  dream_source: 'best-R2-W5: no comparison with inference-time graph methods'\n  notes: 'DONE (analysis only, no experiment). 8 papers surveyed (CodexGraph, LocAgent,\n    RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). All citations verified.\n    Conclusion: training-time vs inference-time are complementary, not competing.'\n  status: planned\n- id: plan_018\n  claim: 1\n  description: 'BM25 negative baseline: mine BM25-based hard negatives as 4th strategy,\n    train ≥1 seed × 2 encoders, compare R@1 with random/embedding/dataflow. Empirically\n    verify CoCoHaNeRe BM25-proxy caused the reported harm.'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers identify missing BM25\n    baseline as #1 structural gap. CoCoHaNeRe correction claim requires empirical\n    verification — without it the paper motivation is asserted but unverified.'\n  notes: 'Phase 1 (CPU, can start now): build BM25 index over training corpus, mine\n    top-k BM25 negatives per query using same protocol as other strategies, produce\n    bm25_training_data.jsonl. Phase 2 (GPU, after M2 frees up): train 1 seed × 2 encoders\n    with BM25 negatives (~7.5h each). 3 seeds preferred if GPU budget allows. Expected\n    result: BM25 negatives harm → confirms CoCoHaNeRe artifact → closes argument.'\n  status: planned\n- id: plan_019\n  claim: 1\n  description: 'Pool size sensitivity analysis: test strategy ranking stability at\n    pool={50, 100, 200, 500} candidates per query on SWE-smith validation.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers flag pool=50 as unrealistically\n    small. Strategy differences may not preserve at realistic pool sizes.'\n  notes: Requires M2 best checkpoints. Re-evaluate on expanded candidate pools. If\n    strategy ranking changes at pool>200, must discuss in paper.\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_p1_codeql_feasibility\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    timeout_rate: 0\n    repos_processed: 8\n    repos_skipped: 2\n    cg_mean_s: 29.6\n    cg_max_s: 119.8\n    df_mean_s: 43.4\n    df_max_s: 167.1\n    h2_connected_coverage: 0.014815\n    h2_disconnected_coverage: 0\n    h2_fisher_p: 6.5e-09\n    h2_gold_in_connected_ratio: 1\n    h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'\n- exp_id: mvp_p2a_linear_proxy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    df_bm25_auc: 0.78\n    bm25_only_auc: 0.476\n    auc_delta: 0.304\n    df_bm25_mrr: 0.556\n    bm25_only_mrr: 0.115\n    mrr_delta: 0.441\n    df_bm25_f1: 0.143\n    bm25_only_f1: 0.039\n    top_feature: is_connected (+2.82)\n    repos_evaluated: 3\n    note: 3 repos / 3 positive samples, directional evidence\n- exp_id: p2b-smoke-test\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke8\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-all-9runs\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_p2b_contrastive_training\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    random_s42_recall1: 0.984\n    random_s123_recall1: 0.984\n    random_s456_recall1: 0.992\n    embedding_s42_recall1: 0.874\n    random_mean_recall1: 0.987\n    runs_completed: 4\n    runs_failed: 5\n    failure_type: disk_full_torch_save\n- exp_id: mvp_p2b_contrastive_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_all\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_4runs_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_seed42:\n      recall@1: 0.9449\n      recall@5: 0.9843\n      recall@10: 0.9843\n    random_seed123:\n      recall@1: 0.9449\n      recall@5: 0.9921\n      recall@10: 0.9921\n    random_seed456:\n      recall@1: 0.9291\n      recall@5: 0.9921\n      recall@10: 0.9921\n    emb_dist_seed42:\n      recall@1: 0.6693\n      recall@5: 0.8898\n      recall@10: 0.9291\n    pool_size: 26\n    n_samples: 127\n- exp_id: p2b_5reruns\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_s42:\n      val_loss: 0.0347\n      recall@1: 0.9843\n    random_s123:\n      val_loss: 0.0446\n      recall@1: 0.9843\n    random_s456:\n      val_loss: 0.0188\n      recall@1: 0.9921\n    emb_dist_s42:\n      val_loss: 0.1876\n      recall@1: 0.874\n    emb_dist_s123:\n      val_loss: 0.1461\n      recall@1: 0.874\n    emb_dist_s456:\n      val_loss: 0.1281\n      recall@1: 0.8819\n    dataflow_s42:\n      val_loss: 0.1878\n      recall@1: 0.874\n    dataflow_s123:\n      val_loss: 0.146\n      recall@1: 0.874\n    dataflow_s456:\n      val_loss: 0.1278\n      recall@1: 0.8819\n    runs_completed: 9\n    runs_failed: 0\n    WARNING: dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds\n      — likely code bug in negative sampling\n- exp_id: p2b_dataflow_retrain\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: p2b_eval_4runs_pool50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pool_size: 50\n    n_samples: 127\n    random_s42:\n      recall@1: 0.496\n      recall@5: 0.843\n      recall@10: 0.945\n    random_s123:\n      recall@1: 0.535\n      recall@5: 0.85\n      recall@10: 0.921\n    random_s456:\n      recall@1: 0.543\n      recall@5: 0.843\n      recall@10: 0.953\n    emb_dist_s42:\n      recall@1: 0.488\n      recall@5: 0.835\n      recall@10: 0.874\n    random_mean:\n      recall@1: 0.525\n      recall@5: 0.845\n      recall@10: 0.94\n    emb_dist_vs_random_delta:\n      recall@1: -0.037\n      recall@5: -0.01\n      recall@10: -0.066\n- exp_id: d007_50repo_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances: 240\n    instances_with_extra_connected: 98\n    Z_pct: 40.8\n    avg_connected_minus_gold: 6\n    codeql_timeout_rate_pct: 4\n    by_repo_size:\n      small_lt50:\n        Z_pct: 38.6\n        avg_extra: 2.5\n      medium_50_200:\n        Z_pct: 55.7\n        avg_extra: 11.8\n      large_gt200:\n        Z_pct: 16.7\n        avg_extra: 8.8\n    decision: Z=40.8% >= 20% -> original method viable, proceed to M1\n- exp_id: m1_extraction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- exp_id: m2_early_pilot\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    pid: 795791\n    gpu: cuda:4\n    gpu_mem_mb: 9342\n    gpu_util_pct: 83\n    batch_size: 2\n    num_negatives: 3\n    max_seq_length: 1024\n    strategy_running: random (stuck at step 4000, epoch 3)\n    strategies_completed: 0/3\n    eval_1500:\n      val_loss: 0.5879\n      recall_at_1: 0.4693\n      recall_at_5: 0.4693\n      recall_at_10: 0.4693\n    eval_2000:\n      val_loss: 0.7089\n      recall_at_1: 0.4398\n    eval_2500:\n      val_loss: 0.6961\n      recall_at_1: 0.4291\n    eval_3000:\n      val_loss: 0.728\n      recall_at_1: 0.4104\n    eval_3500:\n      val_loss: 0.7022\n      recall_at_1: 0.4439\n    best_checkpoint: step_1500 (val_loss=0.5879, 6.2GB)\n    WARNING: recall@1=recall@5=recall@10 confirmed eval bug. Process hung after step\n      4000 (~45min no output). Overfitting after step 1500.\n    status_check_at: '2026-05-13T04:42:00Z'\n- exp_id: m2_early_pilot_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: m2_early_pilot_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: m2_embed_verify\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- exp_id: plan_013_starcoder\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- exp_id: plan_006_scalability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- exp_id: m2_full_qwen\n  name: ''\n  status: ANALYZING\n  conclusion: ''\n  metrics:\n    random_s42:\n      status: DONE\n      epoch: 3/3\n      total_steps: 4242\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.4869\n        recall_at_1: 0.533\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.4651\n        recall_at_1: 0.553\n        recall_at_5: 0.959\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.5365\n        recall_at_1: 0.523\n        recall_at_5: 0.955\n        recall_at_10: 1\n      eval_2000:\n        val_loss: 0.5162\n        recall_at_1: 0.523\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_2500:\n        val_loss: 0.5264\n        recall_at_1: 0.527\n        recall_at_5: 0.956\n        recall_at_10: 1\n      eval_3000:\n        val_loss: 0.5406\n        recall_at_1: 0.536\n        recall_at_5: 0.956\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.4651, R@1=0.5527)\n      conclusion: Overfit after step 1000. Best R@1=0.5527, +1.7pp vs pilot (0.5357).\n        Full data helps.\n    random_s43:\n      status: RUNNING\n      epoch: 1/2\n      current_step: 1200\n      total_steps: 2810\n      total_steps_per_epoch: 1405\n      eval_500:\n        val_loss: 0.4476\n        recall_at_1: 0.5357\n        recall_at_5: 0.9699\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.4638\n        recall_at_1: 0.5285\n        recall_at_5: 0.9672\n        recall_at_10: 1\n      note: Running on cuda:0. Best R@1=0.5357 at step 500. eval@1000 early_stopping\n        1/2. 2 epochs + patience=2.\n    progress_snapshot: 2026-05-15T00:19 CST\n- exp_id: m2_full_starcoder\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    random_s42:\n      epoch: 3/3\n      current_step: 4000\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.6194\n        recall_at_1: 0.435\n        recall_at_5: 0.905\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.6134\n        recall_at_1: 0.454\n        recall_at_5: 0.92\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.6528\n        recall_at_1: 0.449\n        recall_at_5: 0.906\n        recall_at_10: 1\n      eval_2000:\n        val_loss: 0.6698\n        recall_at_1: 0.4456\n        recall_at_5: 0.906\n        recall_at_10: 1\n      eval_3500:\n        val_loss: 0.6588\n        recall_at_1: 0.4534\n        recall_at_5: 0.9057\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.6134, R@1=0.454)\n      note: Step 4000, lr=2.07e-07, patience exhausted (5/0). Approaching natural\n        end. Watcher PID 309679 ready to auto-start s43.\n    progress_snapshot: 2026-05-15T00:19 CST\n- exp_id: m1_reextract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: neg_difficulty_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_128:\n      random:\n        pos_sim: 0.9804\n        neg_sim: 0.899\n        margin: 0.0816\n        pct_positive_margin: 77.8\n      embedding_distance:\n        pos_sim: 0.9804\n        neg_sim: 0.959\n        margin: 0.0209\n        pct_positive_margin: 60.7\n      dataflow_aware:\n        pos_sim: 0.9805\n        neg_sim: 0.95\n        margin: 0.0309\n        pct_positive_margin: 67.4\n    starcoder_128:\n      random:\n        pos_sim: 0.757\n        neg_sim: 0.553\n        margin: 0.2039\n        pct_positive_margin: 72.8\n      embedding_distance:\n        pos_sim: 0.784\n        neg_sim: 0.668\n        margin: 0.1159\n        pct_positive_margin: 59.2\n      dataflow_aware:\n        pos_sim: 0.761\n        neg_sim: 0.659\n        margin: 0.1022\n        pct_positive_margin: 62.8\n    qwen_2048:\n      random:\n        pos_sim: 0.9855\n        neg_sim: 0.9111\n        margin: 0.0743\n        margin_std: 0.2322\n        pct_positive_margin: 81.8\n      embedding_distance:\n        pos_sim: 0.9855\n        neg_sim: 0.9685\n        margin: 0.017\n        margin_std: 0.114\n        pct_positive_margin: 58.8\n      dataflow_aware:\n        pos_sim: 0.9856\n        neg_sim: 0.9563\n        margin: 0.0293\n        margin_std: 0.1407\n        pct_positive_margin: 73.9\n    starcoder_2048:\n      random:\n        pos_sim: 0.7985\n        neg_sim: 0.6045\n        margin: 0.194\n        margin_std: 0.2788\n        pct_positive_margin: 78\n      embedding_distance:\n        pos_sim: 0.8079\n        neg_sim: 0.7409\n        margin: 0.067\n        margin_std: 0.2056\n        pct_positive_margin: 55\n      dataflow_aware:\n        pos_sim: 0.8009\n        neg_sim: 0.6818\n        margin: 0.1192\n        margin_std: 0.2264\n        pct_positive_margin: 70.4\n    sc_qwen_margin_ratio_128:\n      random: 2.5\n      embedding_distance: 5.54\n      dataflow_aware: 3.3\n    sc_qwen_margin_ratio_2048:\n      random: 2.61\n      embedding_distance: 3.94\n      dataflow_aware: 4.07\n- exp_id: m1_reextract_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T16:40:07.996Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T16:40:07.996Z",
  "sessionId": "1808fedb-4d27-4186-8ee0-7e0cdc8eaf16"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-14T16:40:08.015Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：full-scale effect size 消失或反转，BM25 baseline 未能区分 proxy vs true embedding，核心叙事需重建
核心假设：['embedding-random delta < 0.3pp 且 CI 明确包含 0（至少一个 encoder）', 'dataflow 在两个 encoder 上均无显著获益或 harm', 'BM25 negatives 表现与 embedding negatives 无统计差异 → CoCoHaNeRe correction 论证无法关闭', 'pool ≥ 200 时排名与 pool=50 不一致', 'SWE-bench 无可见差异或方向相反', '数据 pipeline 无 bug（排除实现错误后结果仍如此）']
关键指标范围：{'qwen_emb_minus_random_R1_pp': [-0.5, 0.5], 'starcoder_emb_minus_random_R1_pp': [-0.8, 0.3], 'qwen_df_minus_random_R1_pp': [-1.0, 0.3], 'starcoder_df_minus_random_R1_pp': [-2.0, 0.0], 'bm25_minus_random_R1_pp': [-1.0, 0.5], 'swebench_resolve_rate_delta_pp': [-1.0, 0.5], 'repobench_R1_delta_pp': [-1.0, 0.5], 'pool_ranking_stable_pct': [0, 50], 'bootstrap_CI_width_R1_pp': [3.0, 6.0], 'qwen_mean_R1_absolute': [0.48, 0.53], 'starcoder_mean_R1_absolute': [0.4, 0.46]}
叙事方向：三条原始 claim 均无法维持。Reframe 方向：negative result paper —— "Why Hard Negative Mining Strategies Don't Differentiate for Code Retrieval at Scale"。核心贡献变为： (1) 大规模控制实验表明 strategy 选择对 code retrieval 的影响被高估，pilot-scale 差异在 full-scale 消失（scale-dependent finding）；(2) representation geometry analysis 仍有价值——作为解释 *为什么* 策略差异消失的框架（margin 在训练后收敛，pretrained geometry 差异被 fine-tuning 抹平）；(3) CoCoHaNeRe 的 BM25-proxy 问题仍可报告为 methodological caution，但从 "correction" 降为 "observation"。论文定位从 positive contribution 转为 high-quality negative result + methodological contribution。EMNLP Main 仍可投 （negative result papers 有先例），但需要 (a) 足够大的实验规模证明 negative result 可信， (b) mechanistic explanation 为什么不 work，(c) actionable takeaway（practitioners 不需要花 GPU 时间做 fancy mining）。风险：reviewer 可能认为 "nothing works" 缺乏 novelty ——需用 representation geometry analysis 的解释深度来弥补。

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
  "promptId": "646e856e-ac2e-4413-bac1-8dc8f4b81338",
  "type": "user",
  "uuid": "06190086-0458-4321-a1cf-a02cad547125",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "1808fedb-4d27-4186-8ee0-7e0cdc8eaf16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T16:40:08.014Z_

```json
{
  "parentUuid": "06190086-0458-4321-a1cf-a02cad547125",
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
  "uuid": "d01824a6-b3de-4e31-bcfa-3de70da16d53",
  "timestamp": "2026-05-14T16:40:08.014Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "1808fedb-4d27-4186-8ee0-7e0cdc8eaf16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T16:40:08.014Z_

```json
{
  "parentUuid": "d01824a6-b3de-4e31-bcfa-3de70da16d53",
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
  "uuid": "175a8c44-e412-4ad9-9ff5-ba98992cc3f8",
  "timestamp": "2026-05-14T16:40:08.014Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "1808fedb-4d27-4186-8ee0-7e0cdc8eaf16",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T16:40:08.014Z_

```json
{
  "parentUuid": "175a8c44-e412-4ad9-9ff5-ba98992cc3f8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "655a4db5-af08-4442-a4ae-54733499b641",
  "timestamp": "2026-05-14T16:40:08.014Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "1808fedb-4d27-4186-8ee0-7e0cdc8eaf16",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：full-scale effect size 消失或反转，BM25 baseline 未能区分 proxy vs true embedding，核心叙事需重建 核心假设：['embedding-random delta < 0.3pp 且 CI 明确包含 0（至少一个 encoder）', 'dataflo…",
  "leafUuid": "655a4db5-af08-4442-a4ae-54733499b641",
  "sessionId": "1808fedb-4d27-4186-8ee0-7e0cdc8eaf16"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate worst-case scenario for StructFuse hard negative mining study",
  "sessionId": "1808fedb-4d27-4186-8ee0-7e0cdc8eaf16"
}
```

---

### Assistant

_source line 9 · 2026-05-14T16:45:48.408Z_

I'll work through each planned experiment under the worst-case scenario, generating detailed predicted data consistent with the defined worst-tier parameters.

```yaml
tier: worst
narrative_guidance: >
  Full-scale effect sizes collapse. Embedding-distance mining shows no reliable advantage
  over random baselines once multi-seed CIs are computed; dataflow negatives show no
  benefit or slight harm on both encoders. BM25 negatives perform statistically
  indistinguishable from embedding negatives, preventing closure of the CoCoHaNeRe
  correction argument. Pool size scaling destabilizes strategy rankings. SWE-bench
  shows no downstream signal. The paper must pivot to a negative-result framing:
  "Why Hard Negative Mining Strategies Don't Differentiate for Code Retrieval at Scale."
  The salvageable contribution is the representation geometry analysis explaining
  *why* strategies converge (margins collapse post-fine-tuning), plus the methodological
  caution about BM25 proxies (downgraded from "correction" to "observation").

imagined_experiments:
  # ============================================================
  # plan_002 / m2_full_qwen — Full M2 Qwen 9-seed results
  # ============================================================
  - name: "M2 Full Qwen 9-seed 3-strategy training"
    plan_id: "plan_002 / m2_full_qwen"
    description: >
      9 seeds × 3 strategies (random, embedding_distance, dataflow_aware) on
      Qwen2.5-Coder-3B LoRA. Full training data (~44K instances). Pool=50 eval.
    expected_results:
      random_mean_R1: 0.5290
      random_std_R1: 0.0085
      random_95CI: [0.5224, 0.5356]
      embedding_distance_mean_R1: 0.5310
      embedding_distance_std_R1: 0.0092
      embedding_distance_95CI: [0.5239, 0.5381]
      dataflow_aware_mean_R1: 0.5245
      dataflow_aware_std_R1: 0.0110
      dataflow_aware_95CI: [0.5160, 0.5330]
      emb_minus_random_R1_pp: 0.20
      emb_minus_random_CI: [-0.62, 1.02]
      df_minus_random_R1_pp: -0.45
      df_minus_random_CI: [-1.50, 0.60]
      best_step_mode: 1000
      best_step_range: [500, 1500]
      overfit_onset_step: 1500
    result_rationale: >
      Pilot showed emb +2.0pp over random (0.5557 vs 0.5357), but that was 1 seed on
      pilot-scale data. At full scale with 9 seeds, seed variance dominates the small
      effect. The 2.0pp pilot delta shrinks to ~0.2pp because: (1) full training data
      (44K vs pilot subset) gives random negatives more coverage of the embedding space,
      reducing the advantage of curated hard negatives; (2) Qwen's extremely saturated
      pretrained space (pos_sim=0.9855) means all strategies produce negatives that
      are very close to the query — the margin between random_neg_sim (0.911) and
      emb_neg_sim (0.969) gets compressed further during fine-tuning as the encoder
      adjusts; (3) with 9 seeds, some seeds favor random (data order effects), some
      favor embedding, and the mean converges. The CI clearly includes 0, killing the
      claim that embedding mining "consistently improves" retrieval. Dataflow negatives
      show slight harm because at full scale, the 34% structural coverage means 66%
      of training instances fall back to random, diluting any signal; the structural
      negatives for the remaining 34% may be less informative than embedding negatives
      (dataflow disconnection doesn't guarantee semantic difficulty).
    tables:
      - name: "Table 2: Full-Scale R@1 by Strategy × Encoder (Qwen)"
        content: |
          Strategy          | Mean R@1 | Std   | 95% CI          | Δ vs Random | p (paired-t)
          ------------------|----------|-------|-----------------|-------------|-------------
          random            | 0.5290   | 0.009 | [0.522, 0.536]  | —           | —
          embedding_dist    | 0.5310   | 0.009 | [0.524, 0.538]  | +0.20pp     | 0.58
          dataflow_aware    | 0.5245   | 0.011 | [0.516, 0.533]  | −0.45pp     | 0.31
    figures_description:
      - "Box plot of R@1 across 9 seeds for 3 strategies (Qwen). Boxes heavily overlap. Median lines for random and embedding nearly coincident. Dataflow median slightly below but within IQR of both others."
      - "Learning curves (val_loss vs step) for all 27 runs, color-coded by strategy. All strategies converge to similar loss band [0.46–0.54] by step 1000, with divergence only in overfitting tail. No strategy consistently lower."
    analysis: >
      The pilot's +2.0pp embedding advantage was a seed-specific fluctuation. At full
      scale, the effect is +0.20pp with p=0.58 — no statistical significance. Dataflow
      shows a slight negative trend (−0.45pp) but also non-significant. Seed-to-seed
      variance (σ ≈ 0.009) exceeds the strategy effect, making it impossible to
      distinguish strategies on this encoder. This is consistent with Qwen's extreme
      representation saturation: when pos_sim=0.986, fine-tuning rapidly compresses
      any initial margin differences, and all strategies end up in the same loss basin.

  # ============================================================
  # plan_002 / m2_full_starcoder — Full M2 StarCoder 9-seed results
  # ============================================================
  - name: "M2 Full StarCoder 9-seed 3-strategy training"
    plan_id: "plan_002 / m2_full_starcoder"
    description: >
      9 seeds × 3 strategies on StarCoder2-3B. Same protocol as Qwen.
    expected_results:
      random_mean_R1: 0.4430
      random_std_R1: 0.0105
      random_95CI: [0.4349, 0.4511]
      embedding_distance_mean_R1: 0.4395
      embedding_distance_std_R1: 0.0120
      embedding_distance_95CI: [0.4302, 0.4488]
      dataflow_aware_mean_R1: 0.4280
      dataflow_aware_std_R1: 0.0135
      dataflow_aware_95CI: [0.4176, 0.4384]
      emb_minus_random_R1_pp: -0.35
      emb_minus_random_CI: [-1.40, 0.70]
      df_minus_random_R1_pp: -1.50
      df_minus_random_CI: [-3.10, 0.10]
      best_step_mode: 1000
      overfit_onset_step: 1500
    result_rationale: >
      StarCoder pilot showed embedding +1.56pp (0.5078 vs 0.4922), but pilot used
      post-hoc eval for random (no in-training eval), introducing measurement
      inconsistency. At full scale with 9 seeds and consistent eval: (1) StarCoder's
      healthier pretrained geometry (pos_sim=0.80) means random negatives already
      provide decent margin (0.194), so embedding mining's tighter margins (0.067) may
      actually hurt by making the contrastive task too hard early in training, causing
      some seeds to find worse optima; (2) the higher seed variance for StarCoder
      (σ=0.012 vs Qwen's 0.009) reflects the decoder-only architecture's sensitivity
      to initialization — FIM pretraining creates a less smooth loss landscape for
      retrieval fine-tuning; (3) dataflow negatives show the most harm (−1.50pp) because
      StarCoder's intact geometry already separates structural from non-structural
      code well, so forcing structural discrimination adds noise rather than signal.
      The CI for embedding nearly spans zero but slightly favors negative; for dataflow,
      the CI upper bound just barely touches zero, suggesting possible marginal harm.
    tables:
      - name: "Table 2 (continued): Full-Scale R@1 by Strategy × Encoder (StarCoder)"
        content: |
          Strategy          | Mean R@1 | Std   | 95% CI          | Δ vs Random | p (paired-t)
          ------------------|----------|-------|-----------------|-------------|-------------
          random            | 0.4430   | 0.011 | [0.435, 0.451]  | —           | —
          embedding_dist    | 0.4395   | 0.012 | [0.430, 0.449]  | −0.35pp     | 0.47
          dataflow_aware    | 0.4280   | 0.014 | [0.418, 0.438]  | −1.50pp     | 0.015
    figures_description:
      - "Box plot (StarCoder). Random and embedding boxes overlap almost entirely. Dataflow box shifted lower, with 2/9 seeds performing significantly worse (outliers below Q1). Suggests dataflow introduces training instability for some seeds."
    analysis: >
      StarCoder's full-scale results are worse than Qwen overall (R@1 ~0.44 vs ~0.53),
      consistent with decoder-only FIM pretraining being less suited for bidirectional
      retrieval. Critically, embedding mining does not help — the sign flipped from
      pilot (+1.56pp → −0.35pp). Dataflow shows possible harm (p=0.015), but with
      9 comparisons across the study, this doesn't survive multiple-testing correction
      (Bonferroni threshold ~0.006). The dominant finding is that no strategy
      differentiates reliably. Combined with Qwen, neither encoder shows a strategy
      effect that survives multi-seed evaluation.

  # ============================================================
  # plan_003 — SWE-bench Lite end-to-end
  # ============================================================
  - name: "M3a SWE-bench Lite end-to-end evaluation"
    plan_id: "plan_003"
    description: >
      3 strategies × best checkpoint per encoder, evaluated on SWE-bench Lite (300
      instances) with Qwen3.6-27B agent. Measures resolve rate.
    expected_results:
      qwen_random_resolve_rate: 0.2467
      qwen_embedding_resolve_rate: 0.2500
      qwen_dataflow_resolve_rate: 0.2433
      starcoder_random_resolve_rate: 0.2267
      starcoder_embedding_resolve_rate: 0.2233
      starcoder_dataflow_resolve_rate: 0.2200
      best_minus_worst_pp: 0.67
      swebench_resolve_rate_delta_pp: 0.33
      qwen_emb_minus_random_delta_pp: 0.33
      starcoder_emb_minus_random_delta_pp: -0.34
    result_rationale: >
      SWE-bench resolve rate is dominated by the LLM agent's reasoning ability, not
      retrieval quality. The retrieval step provides a candidate set, but the agent
      re-ranks and explores beyond the initial retrieval. With R@1 differences of
      <0.5pp at pool=50, the downstream task absorbs the noise entirely. Quantitatively:
      (1) at resolve rates of ~24%, a 1pp R@1 improvement translates to at most
      ~0.3pp resolve rate improvement (retrieval → localization → patch → test is a
      multi-stage pipeline where errors compound but also get corrected by the agent);
      (2) with 300 instances, the binomial CI for a 24% resolve rate is ±4.8pp — any
      sub-1pp strategy difference is invisible; (3) the agent's exploration strategy
      (re-reading files, searching for imports) effectively compensates for missed
      retrievals, especially for the dataflow-relevant cases where structural
      dependencies guide the agent's natural exploration. The numbers bounce randomly
      around ~24% with no interpretable pattern.
    tables:
      - name: "Table 4: SWE-bench Lite Resolve Rate"
        content: |
          Encoder   | Strategy   | Resolve Rate | Δ vs Random | 95% Binom CI
          ----------|------------|-------------|-------------|------------------
          Qwen      | random     | 24.67%      | —           | [19.9%, 29.4%]
          Qwen      | embedding  | 25.00%      | +0.33pp     | [20.2%, 29.8%]
          Qwen      | dataflow   | 24.33%      | −0.33pp     | [19.6%, 29.1%]
          StarCoder | random     | 22.67%      | —           | [18.0%, 27.3%]
          StarCoder | embedding  | 22.33%      | −0.34pp     | [17.7%, 27.0%]
          StarCoder | dataflow   | 22.00%      | −0.67pp     | [17.3%, 26.7%]
    figures_description:
      - "Bar chart with error bars. All 6 bars are between 22% and 25%, with CI whiskers spanning 18–30%. No visible separation. A dashed line at the SweRank reported rate (26%) sits within all CIs."
    analysis: >
      No downstream differentiation. The largest gap (Qwen-embedding vs StarCoder-dataflow)
      is 2.8pp, which is well within the ±5pp binomial CI. This confirms the worst-case
      prediction: when retrieval strategy differences are <0.5pp, the downstream task
      cannot detect them. The paper cannot claim any practical benefit from mining
      strategy choice. SWE-bench results must be reported transparently as showing
      no differentiation, which strengthens the negative-result narrative ("practitioners
      need not invest GPU time in fancy mining").

  # ============================================================
  # plan_004 — RepoBench-R cross-file retrieval
  # ============================================================
  - name: "M3b RepoBench-R cross-file retrieval evaluation"
    plan_id: "plan_004"
    description: >
      Retrieval-only evaluation on RepoBench-R (test_easy ~8K, test_hard ~8K).
      3 strategies × 2 encoders × 9 seeds. Report R@1 with 95% bootstrap CIs.
    expected_results:
      qwen_easy_random_mean_R1: 0.712
      qwen_easy_embedding_mean_R1: 0.715
      qwen_easy_dataflow_mean_R1: 0.709
      qwen_hard_random_mean_R1: 0.431
      qwen_hard_embedding_mean_R1: 0.434
      qwen_hard_dataflow_mean_R1: 0.427
      starcoder_easy_random_mean_R1: 0.685
      starcoder_easy_embedding_mean_R1: 0.681
      starcoder_easy_dataflow_mean_R1: 0.678
      starcoder_hard_random_mean_R1: 0.398
      starcoder_hard_embedding_mean_R1: 0.393
      starcoder_hard_dataflow_mean_R1: 0.389
      repobench_R1_delta_pp: 0.30
      bootstrap_CI_width_R1_pp: 3.5
    result_rationale: >
      RepoBench-R uses naturally small pools (~6 for easy, ~18 for hard), which
      compresses retrieval difficulty. At pool=6, even a mediocre encoder achieves
      high R@1 (>0.70 on easy), leaving little room for strategy differentiation.
      The training data (SWE-smith) and eval data (RepoBench-R) come from different
      distributions — SWE-smith is bug-fix focused while RepoBench is cross-file
      completion — so training signal transfer is lossy. With 9 seeds and bootstrap
      CIs, the inter-seed variance (~2-3pp) dwarfs the strategy effect (<0.5pp).
      The hard split shows more variance but still no consistent direction: embedding
      helps Qwen by 0.3pp but hurts StarCoder by 0.5pp, consistent with the full-scale
      result that strategy effects are noise. Dataflow shows slight consistent harm
      because the structural signal from SWE-smith repos doesn't transfer to RepoBench's
      different repo distribution.
    tables:
      - name: "Table 5: RepoBench-R R@1 by Strategy × Encoder × Split"
        content: |
          Split | Encoder   | random       | embedding    | dataflow     | Δ emb-rand
          ------|-----------|-------------|-------------|-------------|------------
          easy  | Qwen      | 71.2 ± 1.4  | 71.5 ± 1.5  | 70.9 ± 1.6  | +0.3pp
          easy  | StarCoder | 68.5 ± 1.6  | 68.1 ± 1.7  | 67.8 ± 1.8  | −0.4pp
          hard  | Qwen      | 43.1 ± 2.0  | 43.4 ± 2.1  | 42.7 ± 2.2  | +0.3pp
          hard  | StarCoder | 39.8 ± 2.2  | 39.3 ± 2.4  | 38.9 ± 2.5  | −0.5pp
          Note: ± indicates 95% bootstrap CI half-width. All CIs overlap across strategies.
    figures_description:
      - "Forest plot showing strategy deltas (embedding−random, dataflow−random) for both encoders × both splits. All 8 CIs cross zero. No consistent direction across encoders."
    analysis: >
      RepoBench-R confirms the SWE-smith full-scale finding: no strategy reliably
      differentiates on an external benchmark. The inconsistent sign across encoders
      (positive for Qwen, negative for StarCoder) is the signature of noise, not signal.
      CI widths of 3–5pp completely swamp the 0.3–0.5pp strategy effects. This
      external validation strengthens the negative-result claim: strategy choice
      doesn't matter even when measured on a different benchmark with different
      pool sizes and task formulation.

  # ============================================================
  # plan_005 — Stratified analysis (5 strata)
  # ============================================================
  - name: "Stratified analysis: 5-stratum deep dive"
    plan_id: "plan_005"
    description: >
      5 strata: (1) repo size, (2) pool size, (3) query-positive similarity,
      (4) structural data availability (34% vs 66%), (5) neg_difficulty quartile.
      Report per-stratum R@1 deltas for all 3 strategies × 2 encoders.
    expected_results:
      struct_available_emb_minus_random_qwen: 0.15
      struct_available_df_minus_random_qwen: 0.40
      struct_fallback_emb_minus_random_qwen: 0.25
      struct_fallback_df_minus_random_qwen: -0.90
      neg_diff_Q1_easy_emb_delta: 0.60
      neg_diff_Q4_hard_emb_delta: -0.30
      repo_small_emb_delta: 0.80
      repo_large_emb_delta: -0.15
      pool_small_emb_delta: 0.35
      pool_large_emb_delta: -0.20
      no_stratum_significant_after_correction: true
    result_rationale: >
      Stratified analysis reveals that the aggregate null result masks opposing
      sub-population effects that cancel out — but none are individually significant
      after multiple-testing correction. Structural data stratum: the 34% with
      dataflow data shows a tiny positive df effect (+0.4pp), but the 66% fallback
      (which uses random negatives labeled as "dataflow") dilutes and reverses it.
      This is expected because the fallback mechanism means the "dataflow" strategy
      is actually ~66% random, making the aggregate comparison (dataflow vs random)
      a comparison of (0.34×structural + 0.66×random) vs (1.0×random). The 34% pure
      structural signal is too diluted to surface. Neg_difficulty quartiles: the easiest
      quartile (Q1, high margin) shows slight embedding advantage because the encoder
      can exploit the difficulty gradient; the hardest quartile (Q4, near-zero margin)
      shows slight embedding harm because those negatives are false-negative-adjacent
      (too similar to be true negatives). But with 9 seeds, the per-quartile CIs are
      wide (~5pp) because each quartile has only ~25% of the data. Repo size and pool
      size strata show similar noisy, contradictory patterns.
    tables:
      - name: "Table 6: Per-Stratum Δ(embedding − random) R@1 (Qwen, pp)"
        content: |
          Stratum                  | N instances | Δ R@1 (pp) | 95% CI         | Sig?
          -------------------------|-------------|-----------|----------------|-----
          Repo small (<200)        |  4596       | +0.80     | [−1.5, +3.1]   | No
          Repo large (≥200)        | 39577       | −0.15     | [−0.9, +0.6]   | No
          Pool small (<30)         | 12044       | +0.35     | [−1.2, +1.9]   | No
          Pool large (≥30)         | 32129       | −0.20     | [−1.0, +0.6]   | No
          High q-pos sim (>0.95)   | 28800       | −0.10     | [−0.8, +0.6]   | No
          Low q-pos sim (≤0.95)    | 15373       | +0.55     | [−0.9, +2.0]   | No
          Struct available (34%)   | 15133       | +0.15     | [−1.2, +1.5]   | No
          Struct fallback (66%)    | 29040       | +0.25     | [−0.5, +1.0]   | No
          Neg diff Q1 (easiest)    | 11043       | +0.60     | [−1.5, +2.7]   | No
          Neg diff Q4 (hardest)    | 11043       | −0.30     | [−2.3, +1.7]   | No
    figures_description:
      - "Heatmap: 5 strata × 2 levels × 3 strategy comparisons. Color scale from blue (−2pp) to red (+2pp). Mostly pale/neutral colors. No consistent hot spot. Visual message: no sub-population rescues the finding."
      - "Per-stratum forest plot for dataflow−random on structural-available vs fallback sub-populations. The structural-available CI is [−0.8, +1.6], overlapping zero. The fallback CI is [−1.8, +0.0], suggesting possible harm from the fallback mechanism but not significant."
    analysis: >
      No stratum produces a significant strategy effect after Bonferroni correction
      (10 comparisons, α=0.005). The structural availability stratum is the most
      informative: it shows that the 34% with real structural data has a tiny positive
      dataflow signal, but this is completely washed out by the 66% fallback. This
      is actually a useful finding for the negative-result paper: it suggests that
      structural negative mining *might* help if structural data coverage were
      higher (>80%), but at practical extraction rates (34%), the benefit is
      undetectable. This becomes an actionable takeaway: "invest in extraction
      coverage before investing in mining strategy."

  # ============================================================
  # plan_014 — Temperature ablation
  # ============================================================
  - name: "Temperature ablation: τ ∈ {0.05, 0.1, 0.2}"
    plan_id: "plan_014"
    description: >
      3 temperatures × 3 strategies × 2 encoders. Tests whether the null result
      is regime-specific to τ=0.05.
    expected_results:
      tau_005_emb_minus_random_qwen: 0.20
      tau_010_emb_minus_random_qwen: 0.35
      tau_020_emb_minus_random_qwen: -0.10
      tau_005_emb_minus_random_starcoder: -0.35
      tau_010_emb_minus_random_starcoder: 0.15
      tau_020_emb_minus_random_starcoder: -0.55
      best_tau_overall: 0.05
      strategy_ranking_changes_across_tau: true
      any_tau_significant: false
    result_rationale: >
      Temperature controls the sharpness of the contrastive loss. At τ=0.05 (current),
      the loss is very sharp and the hardest negatives dominate the gradient —
      this should maximally differentiate strategies. If strategies don't differentiate
      at τ=0.05, they're unlikely to at τ=0.1 or 0.2 (where the loss is smoother
      and hard negatives matter less). The results confirm this: τ=0.1 shows slightly
      larger positive deltas for Qwen (the warmer loss surface allows more exploration),
      but still non-significant. τ=0.2 makes the loss too smooth, suppressing all
      hard-negative signal. Importantly, strategy rankings are unstable across τ:
      embedding beats random at τ=0.1 but loses at τ=0.2, confirming that the null
      result is not an artifact of temperature choice — there is genuinely no robust
      strategy advantage.
    tables:
      - name: "Table A1: Temperature × Strategy Interaction (R@1, Qwen)"
        content: |
          τ    | random | embedding | dataflow | Δ emb-rand | Δ df-rand
          -----|--------|-----------|----------|-----------|----------
          0.05 | 0.5290 | 0.5310    | 0.5245   | +0.20     | −0.45
          0.10 | 0.5215 | 0.5250    | 0.5200   | +0.35     | −0.15
          0.20 | 0.5040 | 0.5030    | 0.5015   | −0.10     | −0.25
    figures_description:
      - "Line plot: R@1 vs τ for each strategy. All three lines decline together as τ increases. Lines are nearly parallel with <0.5pp separation at any τ. No crossing pattern that would suggest a strategy-specific optimal temperature."
    analysis: >
      Temperature ablation confirms the null result is not regime-specific. The best
      overall R@1 is at τ=0.05 (sharpest), but strategy differences remain noise-level
      at all temperatures. τ=0.2 degrades all strategies uniformly by ~2.5pp, consistent
      with known contrastive learning theory (too-warm temperatures lose discriminative
      power). The instability of strategy rankings across τ is itself evidence
      against a true strategy effect — a real signal would produce consistent rankings
      regardless of temperature. Report in appendix as robustness check.

  # ============================================================
  # plan_015 — Dynamic mining baseline
  # ============================================================
  - name: "Dynamic embedding mining baseline"
    plan_id: "plan_015"
    description: >
      Re-mine embedding negatives per epoch vs static (mine once from pretrained).
      1 seed × 2 encoders. Tests whether static mining confound explains null result.
    expected_results:
      qwen_dynamic_R1: 0.5315
      qwen_static_R1: 0.5310
      qwen_dynamic_minus_static_pp: 0.05
      starcoder_dynamic_R1: 0.4400
      starcoder_static_R1: 0.4395
      starcoder_dynamic_minus_static_pp: 0.05
      mining_time_overhead_pct: 340
    result_rationale: >
      Dynamic mining re-computes negatives using the current encoder state each epoch,
      so negatives should be harder (adapted to the learned representation). However,
      in the worst case, this doesn't help because: (1) the encoder barely moves
      during 3 epochs of LoRA fine-tuning — the pretrained representation is 99%
      preserved, so dynamic and static negatives are nearly identical (the cosine
      similarity between epoch-0 and epoch-3 embeddings for any given sample is >0.995);
      (2) any benefit from harder negatives is offset by training instability (the
      loss landscape shifts each epoch, preventing convergence to a stable optimum);
      (3) the 3.4× time overhead (re-encoding 44K instances per epoch) makes this
      impractical for no gain. The delta of +0.05pp for both encoders is effectively
      zero, confirming that the null result is not an artifact of static mining.
    tables:
      - name: "Table A2: Static vs Dynamic Mining"
        content: |
          Encoder   | Static R@1 | Dynamic R@1 | Δ (pp) | Time overhead
          ----------|-----------|------------|--------|-------------
          Qwen      | 0.5310    | 0.5315     | +0.05  | +340%
          StarCoder | 0.4395    | 0.4400     | +0.05  | +340%
    figures_description:
      - "Scatter plot: per-instance R@1 agreement between static and dynamic. 98.5% of instances have identical predictions. The 1.5% that differ split evenly (static wins some, dynamic wins others). No systematic pattern."
    analysis: >
      Dynamic mining is a non-factor. The encoder doesn't change enough during LoRA
      fine-tuning to make dynamic negatives meaningfully different from static ones.
      This rules out the confound that our null result is caused by stale negatives.
      For the negative-result paper, this is useful: "even the theoretically optimal
      mining schedule (dynamic) cannot rescue strategy differentiation."

  # ============================================================
  # plan_016 — Bootstrap CI for SWE-bench
  # ============================================================
  - name: "Bootstrap CI for SWE-bench Lite resolve rates"
    plan_id: "plan_016"
    description: >
      10,000 bootstrap resamples for each strategy's resolve rate on SWE-bench Lite
      (300 instances). Tests statistical significance of resolve rate deltas.
    expected_results:
      qwen_random_resolve_rate: 0.2467
      qwen_random_bootstrap_CI: [0.198, 0.296]
      qwen_embedding_resolve_rate: 0.2500
      qwen_embedding_bootstrap_CI: [0.201, 0.299]
      qwen_dataflow_resolve_rate: 0.2433
      qwen_dataflow_bootstrap_CI: [0.196, 0.292]
      emb_minus_random_bootstrap_CI: [-0.048, 0.055]
      df_minus_random_bootstrap_CI: [-0.055, 0.048]
      any_comparison_significant: false
      bootstrap_CI_width_pp: 4.9
    result_rationale: >
      With 300 binary outcomes and a base rate of ~25%, the binomial standard error
      is √(0.25×0.75/300) = 0.025, giving a 95% CI half-width of ~5pp. The strategy
      deltas (<0.5pp) are 10× smaller than the CI width. Bootstrap resampling confirms
      the analytical calculation: all pairwise CIs include zero, with p-values >0.5.
      This is the expected worst-case outcome: SWE-bench's small N makes it impossible
      to detect sub-1pp retrieval differences in downstream task performance. Even a
      "true" 0.5pp retrieval improvement would need N≈60,000 instances to detect at
      α=0.05 in downstream resolve rate.
    tables:
      - name: "Table 4 (extended): Bootstrap CIs for SWE-bench Resolve Rates"
        content: |
          Comparison              | Δ (pp) | Bootstrap 95% CI | p-value
          ------------------------|--------|------------------|--------
          Qwen emb − random       | +0.33  | [−4.8, +5.5]    | 0.89
          Qwen df − random        | −0.33  | [−5.5, +4.8]    | 0.89
          SC emb − random         | −0.34  | [−5.5, +4.8]    | 0.89
          SC df − random          | −0.67  | [−5.8, +4.5]    | 0.80
    figures_description:
      - "Bootstrap distribution histograms for each pairwise delta. All approximately normal, centered near zero, with 95% bands spanning roughly ±5pp. The observed deltas are indistinguishable from the center of each distribution."
    analysis: >
      Bootstrap CIs formalize what the point estimates already suggest: SWE-bench
      cannot discriminate between mining strategies at the effect sizes observed.
      This is not a power problem we can fix — it's a fundamental limitation of
      using 300-instance downstream evaluation to detect <1pp retrieval differences.
      For the negative-result paper, this motivates the argument that practitioners
      should not over-invest in mining strategy optimization based on downstream
      benchmarks.

  # ============================================================
  # plan_018 — BM25 negative baseline
  # ============================================================
  - name: "BM25 negative baseline"
    plan_id: "plan_018"
    description: >
      Mine BM25-based hard negatives as 4th strategy. Train ≥1 seed × 2 encoders.
      Compare R@1 with random/embedding/dataflow to test whether BM25 negatives
      match embedding negatives (which would prevent closing the CoCoHaNeRe argument).
    expected_results:
      qwen_bm25_R1: 0.5275
      qwen_bm25_95CI: [0.515, 0.540]
      starcoder_bm25_R1: 0.4370
      starcoder_bm25_95CI: [0.420, 0.454]
      qwen_bm25_minus_random_pp: -0.15
      starcoder_bm25_minus_random_pp: -0.60
      qwen_bm25_minus_embedding_pp: -0.35
      starcoder_bm25_minus_embedding_pp: -0.25
      bm25_vs_embedding_p_value_qwen: 0.42
      bm25_vs_embedding_p_value_starcoder: 0.55
      bm25_minus_random_R1_pp: -0.38
      bm25_minus_random_CI: [-1.5, 0.7]
    result_rationale: >
      The worst case for the CoCoHaNeRe correction argument: BM25 negatives perform
      similarly to embedding negatives, making it impossible to claim that BM25-proxy
      was the source of CoCoHaNeRe's reported harm. Why this happens: (1) at full
      scale with 44K training instances, BM25 top-k negatives and embedding-distance
      top-k negatives have ~60% overlap — high-BM25 documents tend to also have high
      embedding similarity because both capture lexical/semantic relatedness; (2) the
      non-overlapping 40% doesn't create enough differential training signal to
      separate the strategies; (3) CoCoHaNeRe's reported -27pp harm was likely
      driven by other confounds (different training data scale, different
      encoder, different evaluation protocol) not captured by the BM25-vs-embedding
      distinction alone. In the worst case, BM25 negatives are slightly worse than
      random (−0.15pp Qwen, −0.60pp StarCoder) but the CIs include zero and overlap
      completely with embedding CIs. The CoCoHaNeRe correction argument cannot be
      closed: we can say "BM25 and embedding negatives produce similar results in our
      setup" but not "BM25-proxy caused the harm."
    tables:
      - name: "Table 3: 4-Strategy Comparison Including BM25 Baseline"
        content: |
          Encoder   | random | embedding | dataflow | BM25   | BM25−emb (pp) | p
          ----------|--------|-----------|----------|--------|---------------|------
          Qwen      | 0.5290 | 0.5310    | 0.5245   | 0.5275 | −0.35         | 0.42
          StarCoder | 0.4430 | 0.4395    | 0.4280   | 0.4370 | −0.25         | 0.55
    figures_description:
      - "Bar chart: 4 strategies for each encoder. All bars within 1.5pp of each other. BM25 bars sit between random and embedding for both encoders. Error bars (bootstrap 95% CI) overlap completely across all 4 strategies. Visual message: all strategies are equivalent."
      - "Venn diagram: overlap between BM25 top-3 negatives and embedding top-3 negatives per query. ~60% overlap. Caption explains this high overlap is why the strategies produce similar training outcomes."
    analysis: >
      The BM25 baseline delivers the worst possible outcome for the paper's original
      framing. BM25 ≈ embedding negatives means we cannot attribute CoCoHaNeRe's
      reported harm to their BM25-proxy methodology. The "correction" claim must be
      downgraded to an "observation": "We note that CoCoHaNeRe's reported large
      negative effect (−27pp) was not reproduced in our controlled setup with either
      BM25 or embedding negatives, suggesting the effect may be attributable to other
      experimental differences (scale, encoder, evaluation protocol) rather than the
      BM25-vs-embedding distinction specifically." This is much weaker than the
      original Claim 1 framing. For the negative-result paper, this finding actually
      strengthens the narrative: even the BM25-vs-embedding distinction that motivated
      the study turns out to be illusory at scale.

  # ============================================================
  # plan_019 — Pool size sensitivity
  # ============================================================
  - name: "Pool size sensitivity analysis"
    plan_id: "plan_019"
    description: >
      Evaluate strategy rankings at pool={50, 100, 200, 500} using M2 best
      checkpoints on SWE-smith validation.
    expected_results:
      pool_50:
        qwen_random_R1: 0.5290
        qwen_embedding_R1: 0.5310
        ranking: [embedding, random, dataflow]
      pool_100:
        qwen_random_R1: 0.4120
        qwen_embedding_R1: 0.4085
        ranking: [random, embedding, dataflow]
      pool_200:
        qwen_random_R1: 0.3240
        qwen_embedding_R1: 0.3265
        ranking: [embedding, dataflow, random]
      pool_500:
        qwen_random_R1: 0.2310
        qwen_embedding_R1: 0.2285
        ranking: [random, dataflow, embedding]
      pool_ranking_stable_pct: 25
      ranking_flips: 3
      kendall_tau_50_vs_500: 0.33
    result_rationale: >
      Pool size sensitivity exposes the fragility of strategy rankings. At pool=50
      (current), embedding slightly leads — but this is the artificial setting.
      As pool grows: (1) the absolute R@1 drops substantially because finding the
      gold file among 200 or 500 candidates is genuinely harder; (2) strategy
      rankings become unstable because the relative ordering depends on which
      specific distractor files are added to the pool — at pool=500, many repos
      don't have 500 files, so padding strategies introduce noise; (3) the
      models were trained with pool sizes effectively set by the negative sampling
      (3 negatives → effective pool ~4), so they're not calibrated for large-pool
      ranking; (4) the ranking instability (Kendall τ = 0.33 between pool=50 and
      pool=500) means the strategy comparison is not robust to evaluation protocol
      choices. Only 25% of the time does the pool=50 ranking agree with other pool
      sizes — well below the 50% threshold that would indicate stability.
    tables:
      - name: "Table 7: Strategy Ranking Stability Across Pool Sizes (Qwen)"
        content: |
          Pool | random R@1 | emb R@1  | df R@1   | Best strategy | Rank = pool50?
          -----|-----------|----------|----------|---------------|---------------
          50   | 0.5290    | 0.5310   | 0.5245   | embedding     | (reference)
          100  | 0.4120    | 0.4085   | 0.4050   | random        | No
          200  | 0.3240    | 0.3265   | 0.3250   | embedding     | Yes
          500  | 0.2310    | 0.2285   | 0.2295   | random        | No
      - name: "Table 7b: Strategy Ranking Stability (StarCoder)"
        content: |
          Pool | random R@1 | emb R@1  | df R@1   | Best strategy | Rank = pool50?
          -----|-----------|----------|----------|---------------|---------------
          50   | 0.4430    | 0.4395   | 0.4280   | random        | (reference)
          100  | 0.3410    | 0.3380   | 0.3310   | random        | Yes
          200  | 0.2620    | 0.2640   | 0.2590   | embedding     | No
          500  | 0.1780    | 0.1750   | 0.1770   | random        | Yes
    figures_description:
      - "Line plot: R@1 vs pool size (log scale x-axis) for 3 strategies, both encoders. All lines decline monotonically. Lines cross multiple times, showing ranking instability. Shaded bands (bootstrap CI) overlap at every pool size."
      - "Heatmap: Kendall τ rank correlation between all pool size pairs. Most values between 0.0 and 0.67, with no pair reaching τ > 0.67. Average τ = 0.33."
    analysis: >
      Pool size sensitivity confirms the worst case: strategy rankings are unstable.
      Rankings flip 3 times across 4 pool sizes, with stability at only 25%. This
      means the paper's strategy comparison is contingent on the evaluation protocol,
      not a property of the strategies themselves. For the negative-result paper,
      this is a strong finding: "strategy rankings are not robust to pool size choice,
      suggesting that reported differences in prior work may also be evaluation
      artifacts." The practical takeaway: don't optimize mining strategy based on
      a single pool size — the ranking you find may not hold at deployment scale.

  # ============================================================
  # plan_007 — Hop-count ablation
  # ============================================================
  - name: "Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding"
    plan_id: "plan_007"
    description: >
      Test whether expanding call-graph scope (1/2/3-hop) changes dataflow negative
      quality. 1 seed × Qwen.
    expected_results:
      hop1_R1: 0.5230
      hop2_R1: 0.5245
      hop3_R1: 0.5210
      hop2_minus_hop1_pp: 0.15
      hop3_minus_hop2_pp: -0.35
    result_rationale: >
      In the worst case, hop count doesn't matter because the dataflow strategy
      itself doesn't differentiate from random. 1-hop produces the most conservative
      connected set (fewer files connected → more negatives available → negatives
      are closer to embedding-based selection). 2-hop (current) is slightly better
      because it captures inter-procedural dependencies. 3-hop over-expands the
      connected set, marking too many files as connected and leaving fewer high-quality
      negatives. But all three are within noise of each other and within noise of
      random (0.5290), confirming that the structural signal pathway is not the
      bottleneck — the bottleneck is that no mining strategy differentiates at scale.
    tables:
      - name: "Table A3: Hop Count Ablation (Qwen, dataflow strategy)"
        content: |
          Hops | Connected files/query | Negatives available | R@1    | Δ vs random
          -----|----------------------|--------------------|---------|-----------
          1    | 2.1                  | 47.9               | 0.5230 | −0.60pp
          2    | 4.8                  | 45.2               | 0.5245 | −0.45pp
          3    | 11.3                 | 38.7               | 0.5210 | −0.80pp
    figures_description:
      - "Bar chart: R@1 for 3 hop counts + random baseline (dashed line). All bars below or at the dashed line. Minimal variation across hops."
    analysis: >
      Hop count ablation is uninformative in the worst case — it's optimizing within
      a strategy that doesn't work. The only useful observation: 3-hop over-expansion
      is slightly worse, suggesting that very broad connectivity definitions reduce
      negative quality. But the effect is tiny (0.35pp) and this entire analysis
      is moot given the overarching null result. Relegate to appendix.

  # ============================================================
  # plan_008 — Training data size scaling
  # ============================================================
  - name: "Ablation: training data size scaling"
    plan_id: "plan_008"
    description: >
      1K vs 3K vs 5K (full) training instances, all 3 strategies, 1 seed × Qwen.
      Tests whether strategy effects are scale-dependent.
    expected_results:
      size_1K:
        random_R1: 0.5050
        embedding_R1: 0.5180
        dataflow_R1: 0.5120
        emb_minus_random_pp: 1.30
      size_3K:
        random_R1: 0.5200
        embedding_R1: 0.5260
        dataflow_R1: 0.5210
        emb_minus_random_pp: 0.60
      size_5K:
        random_R1: 0.5290
        embedding_R1: 0.5310
        dataflow_R1: 0.5245
        emb_minus_random_pp: 0.20
      effect_trend: "strategy advantage monotonically decreases with scale"
    result_rationale: >
      This is the most important ablation for the negative-result narrative. At 1K
      instances (pilot-like scale), embedding mining shows a +1.3pp advantage — close
      to the pilot's +2.0pp, confirming that the pilot finding was real but
      scale-dependent. As training data increases to 3K and 5K, the advantage shrinks
      to 0.6pp and 0.2pp respectively. Mechanism: with more training data, the random
      negatives sample a wider swath of the embedding space, effectively approximating
      what curated embedding negatives provide. At small scale, curated negatives
      concentrate the training signal on the decision boundary; at large scale,
      random sampling covers the boundary adequately through sheer volume. This
      is a well-known phenomenon in contrastive learning (cf. SimCLR batch size
      scaling) and provides the mechanistic explanation for why pilot results didn't
      replicate at full scale.
    tables:
      - name: "Table 8: Scale-Dependent Strategy Effects"
        content: |
          Train size | random R@1 | embedding R@1 | Δ (pp) | df R@1  | Δ df-rand (pp)
          -----------|-----------|--------------|--------|---------|---------------
          1K         | 0.5050    | 0.5180       | +1.30  | 0.5120  | +0.70
          3K         | 0.5200    | 0.5260       | +0.60  | 0.5210  | +0.10
          5K (full)  | 0.5290    | 0.5310       | +0.20  | 0.5245  | −0.45
    figures_description:
      - "Line plot: Δ(embedding − random) vs training data size. Monotonically decreasing curve from +1.3pp at 1K to +0.2pp at 5K. Dashed horizontal line at 0. Extrapolation suggests the delta would cross zero around 6-7K instances. This is Figure 4 of the paper — the key evidence for the scale-dependent finding."
    analysis: >
      This is the paper's most compelling experiment. The scale-dependent effect
      provides the mechanistic story: hard negative mining helps at small scale but
      its advantage vanishes as random sampling catches up. This connects to the
      representation geometry analysis: at small scale, random negatives are too
      easy (high margin) and the encoder doesn't learn the decision boundary well.
      As scale increases, random negatives include enough hard examples by chance.
      This reframes the negative result as a positive finding: "scale is a substitute
      for curation in contrastive code retrieval." Actionable takeaway: if your
      training set is small (<2K), invest in mining; if large (>5K), random suffices.

  # ============================================================
  # plan_009 — Fusion head ablation
  # ============================================================
  - name: "Ablation: fusion head (embedding-only vs structural-only vs combined)"
    plan_id: "plan_009"
    description: >
      Test whether adding structural features at inference time helps. 3 heads ×
      best checkpoint × Qwen.
    expected_results:
      embedding_only_R1: 0.5310
      structural_only_R1: 0.3120
      combined_R1: 0.5285
      combined_minus_embedding_pp: -0.25
    result_rationale: >
      In the worst case, the structural signal is weak enough that adding it to the
      embedding at inference time actually hurts slightly (−0.25pp). The structural-only
      head (using only dataflow features) performs poorly (R@1=0.312) because
      structural connectivity alone is too coarse — many connected files are not
      relevant, and many relevant files are not connected. The combined head
      underperforms embedding-only because the structural features add noise: the
      model has to learn to ignore the structural channel for the 66% of instances
      without structural data, and this interferes with the embedding channel.
      This confirms that structural information is better used at training time
      (as negative selection criterion) than at inference time — but even at
      training time it doesn't help in the worst case.
    tables:
      - name: "Table A4: Fusion Head Ablation (Qwen)"
        content: |
          Head           | R@1    | R@5    | R@10   | Δ vs emb-only
          ---------------|--------|--------|--------|--------------
          Embedding only | 0.5310 | 0.9600 | 1.000  | —
          Structural only| 0.3120 | 0.6200 | 0.780  | −21.9pp
          Combined       | 0.5285 | 0.9550 | 0.998  | −0.25pp
    figures_description:
      - "Stacked bar chart showing contribution of each feature channel. Embedding channel dominates in all settings. Structural channel's learned weight approaches zero after training, confirming the model learns to ignore it."
    analysis: >
      Fusion head ablation confirms structural features don't add value at inference
      time. The model effectively learns to zero out the structural channel. This
      is consistent with the broader finding that structural information's role
      in code retrieval is minimal when the training set is large enough.

  # ============================================================
  # plan_010 — Distance-weighted vs binary dataflow
  # ============================================================
  - name: "Ablation: dataflow-distance weighted negatives vs binary"
    plan_id: "plan_010"
    description: >
      Compare binary connected/disconnected with distance-weighted negative
      selection (closer disconnected files weighted higher). 1 seed × Qwen.
    expected_results:
      binary_R1: 0.5245
      weighted_R1: 0.5255
      weighted_minus_binary_pp: 0.10
    result_rationale: >
      Distance weighting provides slightly more informative negatives by preferring
      disconnected files that are structurally close (1-2 hops from connected boundary).
      But the improvement (+0.10pp) is negligible because: (1) the base dataflow
      strategy already doesn't help, so refining it doesn't matter; (2) the distance
      information from CodeQL is noisy (call-graph hop counts don't perfectly
      correlate with structural relevance); (3) at 34% structural coverage,
      most instances don't have distance information, so the weighting applies
      to a minority of training examples.
    tables:
      - name: "Table A5: Distance Weighting Ablation"
        content: |
          Negative selection | R@1    | Δ vs random | Δ vs binary
          -------------------|--------|------------|-------------
          Random             | 0.5290 | —          | —
          Binary disconnect  | 0.5245 | −0.45pp   | —
          Distance weighted  | 0.5255 | −0.35pp   | +0.10pp
    figures_description: []
    analysis: >
      Marginal and uninformative. Confirms the dataflow pathway is not the lever.
      Appendix material only.

  # ============================================================
  # plan_011 — Failure analysis
  # ============================================================
  - name: "Failure analysis: 50 retrieval failures"
    plan_id: "plan_011"
    description: >
      Manual categorization of 50 cases where all strategies fail. Identify whether
      dataflow could have helped.
    expected_results:
      total_failures_analyzed: 50
      categories:
        gold_file_very_different: 18
        gold_file_in_different_language: 4
        config_or_test_files: 12
        very_large_repo_dilution: 8
        dataflow_could_help: 5
        ambiguous: 3
      dataflow_could_help_pct: 10
    result_rationale: >
      Most retrieval failures are cases where the gold file is fundamentally
      different from the query (bug report → config file, error message → test
      file). These are not addressable by any negative mining strategy because
      the core problem is the query-document mismatch, not the contrastive
      training signal. Only ~10% of failures involve cases where structural
      connectivity could plausibly help (e.g., gold file is structurally connected
      but lexically dissimilar). This low ceiling limits the potential upside of
      any structural approach.
    tables:
      - name: "Table 9: Failure Category Breakdown"
        content: |
          Category                        | Count | Pct  | Structural fix possible?
          --------------------------------|-------|------|------------------------
          Gold file lexically dissimilar  | 18    | 36%  | Unlikely
          Config / test / non-code files  | 12    | 24%  | No
          Large repo dilution (>500 files)| 8     | 16%  | Partial
          Cross-language dependency       | 4     | 8%   | No
          Structural connectivity helps   | 5     | 10%  | Yes
          Ambiguous                       | 3     | 6%   | Maybe
    figures_description:
      - "Pie chart of failure categories. Largest slice (36%) is 'lexically dissimilar gold file.' Only 10% slice is 'structural fix possible.'"
    analysis: >
      Failure analysis provides the ceiling argument for the negative-result paper:
      even a perfect structural negative mining strategy could only address ~10%
      of failure cases. The dominant failure mode (lexically dissimilar gold files)
      requires fundamentally different approaches (e.g., multi-modal queries that
      include error traces, stack traces, or issue descriptions). This explains
      *why* structural negatives don't help at scale: the failure distribution is
      dominated by cases where structure is irrelevant.

  # ============================================================
  # plan_012 — Qualitative examples
  # ============================================================
  - name: "Qualitative examples: strategy comparison"
    plan_id: "plan_012"
    description: >
      5-10 cases where strategies produce different retrieval outcomes. Cherry-pick
      both directions (structural helps, structural hurts).
    expected_results:
      examples_found: 7
      structural_helps: 2
      structural_hurts: 3
      no_clear_pattern: 2
    result_rationale: >
      In the worst case, qualitative examples cannot construct a compelling narrative
      because the effects go both directions. The 2 cases where structural negatives
      help are genuine (query about a function call, gold file is the callee 2 hops
      away), but the 3 cases where they hurt are equally compelling (structural
      negatives push the encoder to distinguish files that are actually both relevant,
      causing it to miss the gold file). The balanced count prevents cherry-picking
      a one-directional story.
    tables: []
    figures_description:
      - "Side-by-side retrieval rank comparison for 4 example queries. Two examples show dataflow improving rank (rank 8→3, rank 12→5). Two show dataflow worsening rank (rank 2→7, rank 4→11). Presented honestly with both directions."
    analysis: >
      Qualitative examples support the negative-result narrative: strategy choice
      cuts both ways, with no systematic direction. Use 2-3 examples in the paper
      to illustrate *why* strategies don't differentiate, not to argue for one strategy.

  # ============================================================
  # plan_017 — Inference-time graph method comparison
  # ============================================================
  - name: "Inference-time graph method comparison (analysis only)"
    plan_id: "plan_017"
    description: >
      Literature analysis comparing training-time (StructFuse) vs inference-time
      (CodexGraph, LocAgent, RANGER) graph-based approaches. No experiment.
    expected_results:
      papers_surveyed: 8
      conclusion: "complementary in theory, but our null result suggests training-time structural signal may be less valuable than inference-time navigation"
      key_finding: >
        Inference-time methods re-compute structural relevance per query using the
        actual query context, while training-time methods (ours) bake structural
        signal into the encoder via negative selection. Our null result suggests
        the baked-in signal gets washed out, while inference-time methods preserve
        it. This reframes our contribution: training-time structure is less effective
        than inference-time structure for code retrieval.
    result_rationale: >
      The literature comparison is more damaging in the worst case than it appears.
      If our structural mining doesn't help, but inference-time graph methods (LocAgent
      +8-12pp on SWE-bench, CodexGraph +5pp) do help, the implication is that
      structure matters but our approach to incorporating it (training-time negative
      selection) is the wrong mechanism. This shifts the paper from "structure helps
      conditionally" to "training-time structure doesn't help, and we explain why
      inference-time approaches succeed where we fail." The explanation: training-time
      mining fixes the structural signal at corpus construction time, but the relevant
      structure changes per query (different bugs involve different call chains).
      Inference-time methods adapt to the query.
    tables: []
    figures_description:
      - "Comparison table: training-time vs inference-time structural approaches. Columns: method, when structure is used, adaptation to query, reported gains. Shows inference-time methods consistently report larger gains."
    analysis: >
      This comparison is uncomfortable but essential for the negative-result paper.
      It provides the theoretical explanation for our null result: static structural
      mining at training time cannot capture query-specific structural relevance.
      The practical takeaway: if you want to leverage code structure for retrieval,
      invest in inference-time graph navigation (CodexGraph, LocAgent), not
      training-time negative mining. This is an actionable, non-obvious conclusion
      that justifies the paper's contribution.

  # ============================================================
  # Representation geometry post-training analysis (implicit in plan_005/neg_difficulty)
  # ============================================================
  - name: "Representation geometry convergence analysis"
    plan_id: "plan_005 (extended: post-training geometry)"
    description: >
      Measure pos_sim, neg_sim, margin for all strategies using fine-tuned encoders
      (not just pretrained). Tests whether fine-tuning erases pretrained geometry
      differences.
    expected_results:
      qwen_post_finetune:
        random:
          pos_sim: 0.9120
          neg_sim: 0.8450
          margin: 0.0670
        embedding:
          pos_sim: 0.9135
          neg_sim: 0.8620
          margin: 0.0515
        dataflow:
          pos_sim: 0.9128
          neg_sim: 0.8540
          margin: 0.0588
      starcoder_post_finetune:
        random:
          pos_sim: 0.8650
          neg_sim: 0.7920
          margin: 0.0730
        embedding:
          pos_sim: 0.8670
          neg_sim: 0.8100
          margin: 0.0570
        dataflow:
          pos_sim: 0.8660
          neg_sim: 0.8010
          margin: 0.0650
      margin_convergence_qwen_pct: 78
      margin_convergence_starcoder_pct: 65
    result_rationale: >
      Fine-tuning collapses the pretrained geometry differences. Pre-fine-tuning,
      Qwen (pos_sim=0.986) and StarCoder (pos_sim=0.798) had dramatically different
      geometries. Post-fine-tuning, both converge toward pos_sim ~0.87-0.91. The
      margins across strategies also converge: pretrained Qwen had random margin
      0.074 vs embedding margin 0.017 (4.4× ratio); post-fine-tuning, random margin
      0.067 vs embedding margin 0.052 (1.3× ratio). Fine-tuning acts as a geometry
      equalizer, pushing all representations toward the contrastive loss optimum
      regardless of the pretrained starting point. This explains why strategy
      differences that existed in the pretrained space don't translate to performance
      differences after training: the encoder adjusts its geometry to optimize the
      contrastive objective, and the specific negatives used matter less than the
      objective function itself. For Qwen, 78% of the pretrained margin difference
      between strategies is erased by fine-tuning. For StarCoder, 65% is erased.
    tables:
      - name: "Table 10: Representation Geometry Pre vs Post Fine-tuning"
        content: |
          Encoder   | Phase      | Metric     | random | embedding | dataflow | Ratio(rand/emb)
          ----------|------------|------------|--------|-----------|----------|---------------
          Qwen      | Pretrained | margin     | 0.074  | 0.017     | 0.029    | 4.35
          Qwen      | Fine-tuned | margin     | 0.067  | 0.052     | 0.059    | 1.29
          StarCoder | Pretrained | margin     | 0.194  | 0.067     | 0.119    | 2.90
          StarCoder | Fine-tuned | margin     | 0.073  | 0.057     | 0.065    | 1.28
    figures_description:
      - "Figure 5 (key paper figure): Margin distribution histograms pre vs post fine-tuning, 3 strategies overlaid. Pre-fine-tuning: clearly separated distributions. Post-fine-tuning: distributions converge to similar shape and location. Title: 'Fine-tuning erases pretrained geometry differences.' This is the mechanistic explanation figure."
      - "Scatter plot: pretrained margin vs post-training margin for each instance, colored by strategy. Points cluster around a diagonal but with compression toward a common band, showing convergence."
    analysis: >
      This is the paper's strongest contribution in the worst case: the mechanistic
      explanation for why strategy choice doesn't matter. Fine-tuning acts as a
      geometry equalizer — regardless of which negatives you use, the contrastive
      objective pushes the encoder toward the same representation geometry. The
      pretrained geometry (which determines initial negative difficulty) is a
      transient condition that gets erased. This explains why: (1) pilot-scale
      results showed strategy effects (not enough training to fully erase geometry),
      (2) full-scale results don't (enough training to converge), (3) temperature
      doesn't matter (the geometry convergence is objective-driven, not
      temperature-dependent). The representation geometry analysis transforms the
      negative result from "nothing works" to "everything converges" — a much
      more publishable framing.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "655a4db5-af08-4442-a4ae-54733499b641",
  "isSidechain": false,
  "requestId": "req_011Cb2nuPbjAjhgRq15h3kGr",
  "type": "assistant",
  "uuid": "48c9d364-2985-482d-97de-84905c3f771a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "1808fedb-4d27-4186-8ee0-7e0cdc8eaf16",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tXRXGy5Xy2GbuFLb2DJqs",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19386,
      "cache_read_input_tokens": 11447,
      "output_tokens": 16741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19386,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16741,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 19386,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19386
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：full-scale effect size 消失或反转，BM25 baseline 未能区分 proxy vs true embedding，核心叙事需重建 核心假设：['embedding-random delta < 0.3pp 且 CI 明确包含 0（至少一个 encoder）', 'dataflo…",
  "leafUuid": "48c9d364-2985-482d-97de-84905c3f771a",
  "sessionId": "1808fedb-4d27-4186-8ee0-7e0cdc8eaf16"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate worst-case scenario for StructFuse hard negative mining study",
  "sessionId": "1808fedb-4d27-4186-8ee0-7e0cdc8eaf16"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：full-scale effect size 消失或反转，BM25 baseline 未能区分 proxy vs true embedding，核心叙事需重建 核心假设：['embedding-random delta < 0.3pp 且 CI 明确包含 0（至少一个 encoder）', 'dataflo…",
  "leafUuid": "48c9d364-2985-482d-97de-84905c3f771a",
  "sessionId": "1808fedb-4d27-4186-8ee0-7e0cdc8eaf16"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Validate worst-case scenario for StructFuse hard negative mining study",
  "sessionId": "1808fedb-4d27-4186-8ee0-7e0cdc8eaf16"
}
```

---
