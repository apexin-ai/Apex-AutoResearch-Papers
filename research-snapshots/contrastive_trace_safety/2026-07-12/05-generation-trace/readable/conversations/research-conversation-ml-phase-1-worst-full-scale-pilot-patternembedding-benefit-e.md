# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：full-scale 多种子结果未复现 pilot pattern——embedding benefit 消失或反转，核心假设不成立 核心假设：['e

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/d3badb30-4425-4866-a4c6-532af99a2625.jsonl`
- **Structured JSON:** [`80bc8c3324b96e84b809.json`](../../sessions/80/80bc8c3324b96e84b809.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T08:06:36.410Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T08:06:36.410Z",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：full-scale 多种子结果未复现 pilot pattern——embedding benefit 消失或反转，核心假设不成立\n核心假设：['embedding vs random Δ 在至少一个编码器上为负或 < 0.3pp（pilot 的 +2.0pp 是种子/数据噪声）', 'dataflow benefit 在所有条件下消失', 'full-scale 数据分布与 pilot 存在系统性差异（覆盖率、难度分布变化）', 'representation saturation 故事无法解释 full-scale 结果——机制假设被反驳或不完整', 'SWE-bench 无差异或不可行']\n关键指标范围：{'qwen_embed_vs_random_R1_pp': [-1.0, 0.3], 'starcoder_embed_vs_random_R1_pp': [-1.5, 0.3], 'qwen_dataflow_vs_random_R1_pp': [-2.0, 0.3], 'starcoder_dataflow_vs_random_R1_pp': [-2.5, 0.0], 'best_qwen_mean_R1': [0.5, 0.54], 'best_starcoder_mean_R1': [0.42, 0.46], 'swebench_resolve_delta_pp': [-1.0, 0.5], 'embed_benefit_bootstrap_p': [0.2, 1.0], 'cross_seed_R1_std': [2.5, 5.0]}\n叙事方向：原始三条 claim 全部不成立，需完全 reframe。新角度：(1) \"Why Hard Negative Mining Doesn't Generalize for Code Retrieval\"——negative result paper，论证 pilot-scale 结论不可靠， small-scale 评估是领域普遍问题（CoCoHaNeRe 的错也是我们 pilot 的错）；(2) 表征几何分析 作为独立贡献——不用于解释策略差异（因为差异不存在），而用于诊断编码器质量和预测训练难度， 提出 \"representation saturation index\" 作为通用工具；(3) CodeQL pipeline 作为开源 infrastructure 贡献（claim 3 不受影响）。论文标题改为 \"A Cautionary Tale: Scale, Seeds, and the Fragility of Hard Negative Mining for Code Retrieval\"。仍投 EMNLP Main—— negative result + methodological contribution 是 EMNLP 接受的论文类型。需要先排查 data pipeline bug（full-scale 数据分布是否变化），确认是真实 negative result 而非工程错误。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: structfuse-context\nfocus: D024 重写后的新 framing：论文从 \"method paper (dataflow > all)\" 转为 \"systematic analysis + mechanistic insight\"。三条新 claim：(1) 真正的 embedding mining 普遍有效，纠正 CoCoHaNeRe BM25-proxy 误解；(2) dataflow mining 有条件额外有效，机制是表征空间饱和度；(3) CodeQL 可扩展。已有实证：Qwen R@1=55.3%, StarCoder R@1=45.4%, neg_difficulty margin +17%/+28%, 两编码器 step 1000 过拟合。Reviewers 应重点评估：新叙事线说服力、\"conditional benefit\" 是否被视为 weak claim、n=2 编码器统计限制、缺 SWE-bench 下游验证的影响。\n\n## paper_framing.md\n\n# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \"harm\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).\n\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\n\n- **Headline result template**: \"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\"\n\n## Core Insight\n\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\"\n- Backup: \"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\n- m1_reextract_v2: expanded extraction for higher coverage\n\n### Planned (priority order):\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark\n- plan_015: Dynamic mining baseline\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected\n    vs gold statistics'\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: m1_extraction\n  mvp_registry_id: mvp_p1_codeql_feasibility\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- id: plan_002\n  claim: 1\n  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,\n    3 seeds each, Qwen2.5-Coder-3B LoRA'\n  priority: P0\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  registry_id: m2_embed_verify\n  mvp_registry_id: mvp_p2b_contrastive_training\n  full_registry_ids:\n  - m2_full_qwen\n  - m2_full_starcoder\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- id: plan_003\n  claim: 1\n  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best\n    checkpoint, Qwen3.6-27B agent'\n  priority: P0\n  gpu_budget_hours: 40\n  deps:\n  - plan_002\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no\n    LLM agent'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding\n    negatives 何时最有害'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 3\n  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,\n    connected-but-not-gold ratio by repo size'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan_006_scalability\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- id: plan_007\n  claim: 1\n  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Ablation: fusion head (embedding-only vs structural-features-only\n    vs combined)'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether\n    data-flow helps'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_003\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Qualitative examples: 5-10 cases where structural negatives changed\n    retrieval outcome'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Second encoder validation: repeat M2 core comparison (3 strategies,\n    1 seed) on StarCoder-3B or CodeBERT to test architecture generality'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  dream_source: 'best-R1-W1, median-R2-W5: single encoder is primary generality concern.\n    Upgraded to P0 per Reviewer — this is the #1 factor separating WA from WR.'\n  registry_id: plan_013_starcoder\n  full_registry_id: m2_full_starcoder\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- id: plan_014\n  claim: 2\n  description: 'Temperature ablation: τ ∈ {0.05, 0.1, 0.2} for all 3 strategies, test\n    regime-specificity of embedding harm'\n  priority: P1\n  gpu_budget_hours: 70\n  deps:\n  - plan_002\n  dream_source: 'median-R1-W3: τ=0.05 unusually low, finding may be regime-specific'\n  status: planned\n- id: plan_015\n  claim: 2\n  description: 'Dynamic embedding mining baseline: re-mine embedding negatives per\n    epoch vs static (mine once from pretrained). Isolate selection criterion from\n    curriculum shift.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  dream_source: 'best-R1-W2, median-R1-W2: static vs dynamic mining is potential confound\n    for Claim 2'\n  status: planned\n- id: plan_016\n  claim: 1\n  description: 'Bootstrap CI for SWE-bench Lite: add 95% bootstrap confidence intervals\n    to end-to-end resolve rate evaluation'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  dream_source: 'best-R1-W3, worst-R1-W5: +2.0pp on 300 instances needs statistical\n    significance test'\n  status: planned\n- id: plan_017\n  claim: 1\n  description: 'Inference-time graph method comparison: discuss/compare with CodexGraph,\n    LocAgent — is StructFuse complementary or alternative?'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  dream_source: 'best-R2-W5: no comparison with inference-time graph methods'\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_p1_codeql_feasibility\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    timeout_rate: 0\n    repos_processed: 8\n    repos_skipped: 2\n    cg_mean_s: 29.6\n    cg_max_s: 119.8\n    df_mean_s: 43.4\n    df_max_s: 167.1\n    h2_connected_coverage: 0.014815\n    h2_disconnected_coverage: 0\n    h2_fisher_p: 6.5e-09\n    h2_gold_in_connected_ratio: 1\n    h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'\n- exp_id: mvp_p2a_linear_proxy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    df_bm25_auc: 0.78\n    bm25_only_auc: 0.476\n    auc_delta: 0.304\n    df_bm25_mrr: 0.556\n    bm25_only_mrr: 0.115\n    mrr_delta: 0.441\n    df_bm25_f1: 0.143\n    bm25_only_f1: 0.039\n    top_feature: is_connected (+2.82)\n    repos_evaluated: 3\n    note: 3 repos / 3 positive samples, directional evidence\n- exp_id: p2b-smoke-test\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke8\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-all-9runs\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_p2b_contrastive_training\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    random_s42_recall1: 0.984\n    random_s123_recall1: 0.984\n    random_s456_recall1: 0.992\n    embedding_s42_recall1: 0.874\n    random_mean_recall1: 0.987\n    runs_completed: 4\n    runs_failed: 5\n    failure_type: disk_full_torch_save\n- exp_id: mvp_p2b_contrastive_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_all\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_4runs_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_seed42:\n      recall@1: 0.9449\n      recall@5: 0.9843\n      recall@10: 0.9843\n    random_seed123:\n      recall@1: 0.9449\n      recall@5: 0.9921\n      recall@10: 0.9921\n    random_seed456:\n      recall@1: 0.9291\n      recall@5: 0.9921\n      recall@10: 0.9921\n    emb_dist_seed42:\n      recall@1: 0.6693\n      recall@5: 0.8898\n      recall@10: 0.9291\n    pool_size: 26\n    n_samples: 127\n- exp_id: p2b_5reruns\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_s42:\n      val_loss: 0.0347\n      recall@1: 0.9843\n    random_s123:\n      val_loss: 0.0446\n      recall@1: 0.9843\n    random_s456:\n      val_loss: 0.0188\n      recall@1: 0.9921\n    emb_dist_s42:\n      val_loss: 0.1876\n      recall@1: 0.874\n    emb_dist_s123:\n      val_loss: 0.1461\n      recall@1: 0.874\n    emb_dist_s456:\n      val_loss: 0.1281\n      recall@1: 0.8819\n    dataflow_s42:\n      val_loss: 0.1878\n      recall@1: 0.874\n    dataflow_s123:\n      val_loss: 0.146\n      recall@1: 0.874\n    dataflow_s456:\n      val_loss: 0.1278\n      recall@1: 0.8819\n    runs_completed: 9\n    runs_failed: 0\n    WARNING: dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds\n      — likely code bug in negative sampling\n- exp_id: p2b_dataflow_retrain\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: p2b_eval_4runs_pool50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pool_size: 50\n    n_samples: 127\n    random_s42:\n      recall@1: 0.496\n      recall@5: 0.843\n      recall@10: 0.945\n    random_s123:\n      recall@1: 0.535\n      recall@5: 0.85\n      recall@10: 0.921\n    random_s456:\n      recall@1: 0.543\n      recall@5: 0.843\n      recall@10: 0.953\n    emb_dist_s42:\n      recall@1: 0.488\n      recall@5: 0.835\n      recall@10: 0.874\n    random_mean:\n      recall@1: 0.525\n      recall@5: 0.845\n      recall@10: 0.94\n    emb_dist_vs_random_delta:\n      recall@1: -0.037\n      recall@5: -0.01\n      recall@10: -0.066\n- exp_id: d007_50repo_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances: 240\n    instances_with_extra_connected: 98\n    Z_pct: 40.8\n    avg_connected_minus_gold: 6\n    codeql_timeout_rate_pct: 4\n    by_repo_size:\n      small_lt50:\n        Z_pct: 38.6\n        avg_extra: 2.5\n      medium_50_200:\n        Z_pct: 55.7\n        avg_extra: 11.8\n      large_gt200:\n        Z_pct: 16.7\n        avg_extra: 8.8\n    decision: Z=40.8% >= 20% -> original method viable, proceed to M1\n- exp_id: m1_extraction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- exp_id: m2_early_pilot\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    pid: 795791\n    gpu: cuda:4\n    gpu_mem_mb: 9342\n    gpu_util_pct: 83\n    batch_size: 2\n    num_negatives: 3\n    max_seq_length: 1024\n    strategy_running: random (stuck at step 4000, epoch 3)\n    strategies_completed: 0/3\n    eval_1500:\n      val_loss: 0.5879\n      recall_at_1: 0.4693\n      recall_at_5: 0.4693\n      recall_at_10: 0.4693\n    eval_2000:\n      val_loss: 0.7089\n      recall_at_1: 0.4398\n    eval_2500:\n      val_loss: 0.6961\n      recall_at_1: 0.4291\n    eval_3000:\n      val_loss: 0.728\n      recall_at_1: 0.4104\n    eval_3500:\n      val_loss: 0.7022\n      recall_at_1: 0.4439\n    best_checkpoint: step_1500 (val_loss=0.5879, 6.2GB)\n    WARNING: recall@1=recall@5=recall@10 confirmed eval bug. Process hung after step\n      4000 (~45min no output). Overfitting after step 1500.\n    status_check_at: '2026-05-13T04:42:00Z'\n- exp_id: m2_early_pilot_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: m2_early_pilot_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: m2_embed_verify\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- exp_id: plan_013_starcoder\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- exp_id: plan_006_scalability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- exp_id: m2_full_qwen\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    random_s42:\n      epoch: 3/3\n      current_step: 2950\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.4869\n        recall_at_1: 0.533\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.4651\n        recall_at_1: 0.553\n        recall_at_5: 0.959\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.5365\n        recall_at_1: 0.523\n        recall_at_5: 0.955\n        recall_at_10: 1\n      eval_2000:\n        val_loss: 0.5162\n        recall_at_1: 0.523\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_2500:\n        val_loss: 0.5264\n        recall_at_1: 0.527\n        recall_at_5: 0.956\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.4651, R@1=0.553)\n    progress_snapshot: 2026-05-14T13:37 CST\n- exp_id: m2_full_starcoder\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    random_s42:\n      epoch: 2/3\n      current_step: 2000\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.6194\n        recall_at_1: 0.435\n        recall_at_5: 0.905\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.6134\n        recall_at_1: 0.454\n        recall_at_5: 0.92\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.6528\n        recall_at_1: 0.449\n        recall_at_5: 0.906\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.6134, R@1=0.454)\n    progress_snapshot: 2026-05-14T13:37 CST\n- exp_id: m1_reextract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: neg_difficulty_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_128:\n      random:\n        pos_sim: 0.9804\n        neg_sim: 0.899\n        margin: 0.0816\n        pct_positive_margin: 77.8\n      embedding_distance:\n        pos_sim: 0.9804\n        neg_sim: 0.959\n        margin: 0.0209\n        pct_positive_margin: 60.7\n      dataflow_aware:\n        pos_sim: 0.9805\n        neg_sim: 0.95\n        margin: 0.0309\n        pct_positive_margin: 67.4\n    starcoder_128:\n      random:\n        pos_sim: 0.757\n        neg_sim: 0.553\n        margin: 0.2039\n        pct_positive_margin: 72.8\n      embedding_distance:\n        pos_sim: 0.784\n        neg_sim: 0.668\n        margin: 0.1159\n        pct_positive_margin: 59.2\n      dataflow_aware:\n        pos_sim: 0.761\n        neg_sim: 0.659\n        margin: 0.1022\n        pct_positive_margin: 62.8\n    qwen_2048:\n      random:\n        pos_sim: 0.9855\n        neg_sim: 0.9111\n        margin: 0.0743\n        margin_std: 0.2322\n        pct_positive_margin: 81.8\n      embedding_distance:\n        pos_sim: 0.9855\n        neg_sim: 0.9685\n        margin: 0.017\n        margin_std: 0.114\n        pct_positive_margin: 58.8\n      dataflow_aware:\n        pos_sim: 0.9856\n        neg_sim: 0.9563\n        margin: 0.0293\n        margin_std: 0.1407\n        pct_positive_margin: 73.9\n    starcoder_2048:\n      random:\n        pos_sim: 0.7985\n        neg_sim: 0.6045\n        margin: 0.194\n        margin_std: 0.2788\n        pct_positive_margin: 78\n      embedding_distance:\n        pos_sim: 0.8079\n        neg_sim: 0.7409\n        margin: 0.067\n        margin_std: 0.2056\n        pct_positive_margin: 55\n      dataflow_aware:\n        pos_sim: 0.8009\n        neg_sim: 0.6818\n        margin: 0.1192\n        margin_std: 0.2264\n        pct_positive_margin: 70.4\n    sc_qwen_margin_ratio_128:\n      random: 2.5\n      embedding_distance: 5.54\n      dataflow_aware: 3.3\n    sc_qwen_margin_ratio_2048:\n      random: 2.61\n      embedding_distance: 3.94\n      dataflow_aware: 4.07\n- exp_id: m1_reextract_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T08:06:36.414Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T08:06:36.414Z",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-14T08:06:36.451Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：full-scale 多种子结果未复现 pilot pattern——embedding benefit 消失或反转，核心假设不成立
核心假设：['embedding vs random Δ 在至少一个编码器上为负或 < 0.3pp（pilot 的 +2.0pp 是种子/数据噪声）', 'dataflow benefit 在所有条件下消失', 'full-scale 数据分布与 pilot 存在系统性差异（覆盖率、难度分布变化）', 'representation saturation 故事无法解释 full-scale 结果——机制假设被反驳或不完整', 'SWE-bench 无差异或不可行']
关键指标范围：{'qwen_embed_vs_random_R1_pp': [-1.0, 0.3], 'starcoder_embed_vs_random_R1_pp': [-1.5, 0.3], 'qwen_dataflow_vs_random_R1_pp': [-2.0, 0.3], 'starcoder_dataflow_vs_random_R1_pp': [-2.5, 0.0], 'best_qwen_mean_R1': [0.5, 0.54], 'best_starcoder_mean_R1': [0.42, 0.46], 'swebench_resolve_delta_pp': [-1.0, 0.5], 'embed_benefit_bootstrap_p': [0.2, 1.0], 'cross_seed_R1_std': [2.5, 5.0]}
叙事方向：原始三条 claim 全部不成立，需完全 reframe。新角度：(1) "Why Hard Negative Mining Doesn't Generalize for Code Retrieval"——negative result paper，论证 pilot-scale 结论不可靠， small-scale 评估是领域普遍问题（CoCoHaNeRe 的错也是我们 pilot 的错）；(2) 表征几何分析 作为独立贡献——不用于解释策略差异（因为差异不存在），而用于诊断编码器质量和预测训练难度， 提出 "representation saturation index" 作为通用工具；(3) CodeQL pipeline 作为开源 infrastructure 贡献（claim 3 不受影响）。论文标题改为 "A Cautionary Tale: Scale, Seeds, and the Fragility of Hard Negative Mining for Code Retrieval"。仍投 EMNLP Main—— negative result + methodological contribution 是 EMNLP 接受的论文类型。需要先排查 data pipeline bug（full-scale 数据分布是否变化），确认是真实 negative result 而非工程错误。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: structfuse-context
focus: D024 重写后的新 framing：论文从 "method paper (dataflow > all)" 转为 "systematic analysis + mechanistic insight"。三条新 claim：(1) 真正的 embedding mining 普遍有效，纠正 CoCoHaNeRe BM25-proxy 误解；(2) dataflow mining 有条件额外有效，机制是表征空间饱和度；(3) CodeQL 可扩展。已有实证：Qwen R@1=55.3%, StarCoder R@1=45.4%, neg_difficulty margin +17%/+28%, 两编码器 step 1000 过拟合。Reviewers 应重点评估：新叙事线说服力、"conditional benefit" 是否被视为 weak claim、n=2 编码器统计限制、缺 SWE-bench 下游验证的影响。

## paper_framing.md

# Paper Framing — StructFuse

## Target Venue
- Primary: EMNLP 2026 Main
- Deadline: ARR May 25, 2026

## Core Claims (3)

1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported "harm" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).

2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.

3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).

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
| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |
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
- plan_003: SWE-bench Lite eval (biggest lever for paper strength)
- plan_014: Temperature ablation (Dream reviewer concern)
- plan_004: RepoBench-R second benchmark
- plan_015: Dynamic mining baseline
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
  gpu_budget_hours: 30
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
  status: planned
- id: plan_004
  claim: 1
  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no
    LLM agent'
  priority: P1
  gpu_budget_hours: 15
  deps:
  - plan_002
  status: planned
- id: plan_005
  claim: 2
  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding
    negatives 何时最有害'
  priority: P1
  gpu_budget_hours: 5
  deps:
  - plan_002
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
    LocAgent — is StructFuse complementary or alternative?'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_002
  dream_source: 'best-R2-W5: no comparison with inference-time graph methods'
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
  status: RUNNING
  conclusion: ''
  metrics:
    random_s42:
      epoch: 3/3
      current_step: 2950
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
      best_checkpoint: step_1000 (val_loss=0.4651, R@1=0.553)
    progress_snapshot: 2026-05-14T13:37 CST
- exp_id: m2_full_starcoder
  name: ''
  status: RUNNING
  conclusion: ''
  metrics:
    random_s42:
      epoch: 2/3
      current_step: 2000
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
      best_checkpoint: step_1000 (val_loss=0.6134, R@1=0.454)
    progress_snapshot: 2026-05-14T13:37 CST
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
  "promptId": "78b1d59e-5a49-469a-ab4c-014599749c4d",
  "type": "user",
  "uuid": "4e302b9b-8d44-4464-8067-bbd155e62571",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T08:06:36.449Z_

```json
{
  "parentUuid": "4e302b9b-8d44-4464-8067-bbd155e62571",
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
  "uuid": "4dc1e0b2-de2a-45a3-9207-c2b05d7553e0",
  "timestamp": "2026-05-14T08:06:36.449Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T08:06:36.449Z_

```json
{
  "parentUuid": "4dc1e0b2-de2a-45a3-9207-c2b05d7553e0",
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
  "uuid": "1b6df25d-e7a0-4b44-b0a4-f4edd6c9d5e1",
  "timestamp": "2026-05-14T08:06:36.449Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T08:06:36.449Z_

```json
{
  "parentUuid": "1b6df25d-e7a0-4b44-b0a4-f4edd6c9d5e1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2d2e8bb4-3c78-4c28-950f-306e36ea762d",
  "timestamp": "2026-05-14T08:06:36.449Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：full-scale 多种子结果未复现 pilot pattern——embedding benefit 消失或反转，核心假设不成立 核心假设：['embedding vs random Δ 在至少一个编码器上为负或 < 0.3pp（pilot 的 +2.0pp 是种子/数据噪声）', 'dataflow…",
  "leafUuid": "2d2e8bb4-3c78-4c28-950f-306e36ea762d",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze negative result scenario for StructFuse paper",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625"
}
```

---

### Assistant

_source line 9 · 2026-05-14T08:07:02.901Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for all "planned" experiments in the experiment_plan, under the "worst" tier scenario. Let me carefully go through each planned experiment and predict what would happen if the worst case materializes.

Let me identify all planned experiments:
- plan_003: SWE-bench Lite eval (planned)
- plan_004: RepoBench-R (planned)
- plan_005: Embedding vs random deep analysis (planned)
- plan_007: 1-hop vs 2-hop vs 3-hop ablation (planned)


- plan_008: Training data size scaling (planned)
- plan_009: Fusion head ablation (planned)
- plan_010: Dataflow-distance weighted negatives (planned)
- plan_011: Failure analysis (planned)
- plan_012: Qualitative examples (planned)
- plan_014: Temperature ablation (planned)
- plan_015: Dynamic mining baseline (planned)
- plan_016: Bootstrap CI for SWE-bench (planned)
- plan_017: Inference-time graph method comparison (planned)

I should also factor in the RUNNING experiments m2_full_qwen and m2_full_starcoder since they'll inform the worst-case predictions.

Looking at the worst-case scenarios: the embedding and dataflow benefits could disappear or even reverse at full scale, the core assumptions might not hold, or the full-scale data distribution could diverge from what we saw in the pilot. The metric ranges show pretty wide confidence intervals—embedding gains could swing from -1.0 to 0.3 for Qwen and -1.5 to 0.3 for StarCoder, while dataflow ranges from -2.0 to 0.3 and -2.5 to 0.0 respectively. The absolute performance numbers are tighter, with best Qwen R1 between 0.5 and 0.54 and best StarCoder between 0.42 and 0.46.

Now looking at the additional metric ranges and starting to map out the detailed predictions. The SWE-bench resolve delta could range from -1.0 to 0.5 percentage points, and the embedding benefit bootstrap p-value spans 0.2 to 1.0, suggesting high uncertainty about whether the effect is even real. Cross-seed variance is substantial at 2.5 to 5.0 percentage points.

For the m2_full baseline, I'm expecting Qwen to hit around 0.52 mean R@1 with embedding gains somewhere between -0.5 and +0.3 percentage points (essentially noise), while StarCoder lands around 0.44 with a -1.0 to +0.3 range. The high cross-seed variance means individual runs will bounce around quite a bit. Now I'm working through what each planned experiment would actually show given these constraints, starting with how SWE-bench performance would look if the embedding benefit has already disappeared.

Across the remaining experiments, the pattern becomes clear: embedding and dataflow mining don't provide consistent signal. The RepoBench-R results would mirror this lack of benefit, the stratified analysis by repo complexity would reveal the inconsistency, and neither hop distance ablations nor data scaling would rescue the approach. Even architectural changes like fusion heads or distance weighting can't create signal that isn't there in the underlying data. The failure analysis would struggle to find systematic cases where dataflow actually helps, and while qualitative examples might exist, they'd likely be cherry-picked rather than representative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d2e8bb4-3c78-4c28-950f-306e36ea762d",
  "isSidechain": false,
  "requestId": "req_011Cb27k8uQFKeyfhLccZpAi",
  "type": "assistant",
  "uuid": "6636e07e-5e1d-4011-9777-5e0e701a4c9a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyqcsyAwAyzXxrBzwkxmHP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17612,
      "cache_read_input_tokens": 11447,
      "output_tokens": 15432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17612,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15432,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 17612,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17612
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

_source line 10 · 2026-05-14T08:11:44.327Z_

```yaml
tier: worst
narrative_guidance: >
  原始三条 claim 全部不成立。Pilot 阶段观察到的 embedding benefit (+2.0pp Qwen, +1.6pp StarCoder)
  在 full-scale 多种子实验中未复现——策略间差异被种子方差淹没，bootstrap p 值远离显著。
  Dataflow benefit 在所有条件下消失。论文需完全 reframe 为 negative result paper：
  "A Cautionary Tale: Scale, Seeds, and the Fragility of Hard Negative Mining for Code Retrieval"。
  核心贡献转为：(1) 证明 pilot-scale 结论在 HN mining for code 领域普遍不可靠，
  (2) representation saturation index 作为独立诊断工具，
  (3) CodeQL pipeline 作为开源 infrastructure。
  在展开实验前必须先排查 data pipeline bug（full-scale 训练数据分布 vs pilot 是否存在
  覆盖率/难度/repo 组成的系统性偏移），确认是真实 negative result 而非工程错误。

imagined_experiments:
  # ============================================================
  # M2 Full-scale training (RUNNING, predicted final outcome)
  # ============================================================
  - name: "M2 Full Qwen — 9 seeds × 3 strategies 最终结果"
    plan_id: "plan_002"
    description: >
      Qwen2.5-Coder-3B 在 full-scale 数据上完成全部 27 runs (9 seeds × 3 strategies)。
      当前仅 random_s42 完成（R@1=0.553 at step 1000），预测全部完成后的汇总。
    expected_results:
      random_mean_R1: 0.523
      random_std_R1: 0.031
      embedding_distance_mean_R1: 0.521
      embedding_distance_std_R1: 0.035
      dataflow_aware_mean_R1: 0.515
      dataflow_aware_std_R1: 0.038
      embed_vs_random_delta_pp: -0.2
      dataflow_vs_random_delta_pp: -0.8
      best_single_run_R1: 0.553
      worst_single_run_R1: 0.478
      cross_seed_R1_std_pp: 3.1
      best_strategy_by_seed_count:
        random_wins: 4
        embedding_wins: 3
        dataflow_wins: 2
      overfitting_step_median: 1000
    result_rationale: >
      Pilot 的 +2.0pp embed benefit 来自单种子（s42）在小规模数据上的幸运波动。
      Full-scale 数据量从 ~2K 增至 ~15K instances，数据分布发生系统性变化：
      (1) large/xlarge repos 占比从 pilot 的 ~30% 升至 ~60%，这些 repos 的 structural_data_rate
      仅 0.31-0.34，embedding negatives 的质量下降；
      (2) 训练集难度分布更均匀，pilot 中 embedding mining 选出的"难"样本在 full-scale
      中不再难于 random——因为 random pool 本身已足够难；
      (3) Qwen 的 pos_sim=0.9855 表征饱和在 full-scale 下更严重，所有策略都面临
      margin 过小的问题（embedding margin=0.017, 但 random margin 也仅 0.074），
      导致策略间差异被优化噪声覆盖。9 个种子的 std~3pp 远大于策略间 delta~0.2pp。
    tables:
      - name: "Table 2: Qwen Full-Scale R@1 by Strategy × Seed"
        columns: [seed, random, embedding, dataflow]
        rows:
          - [42, 0.553, 0.547, 0.538]
          - [123, 0.528, 0.534, 0.521]
          - [456, 0.512, 0.498, 0.503]
          - [789, 0.541, 0.543, 0.530]
          - [1024, 0.498, 0.510, 0.496]
          - [2048, 0.519, 0.522, 0.512]
          - [3000, 0.505, 0.503, 0.478]
          - [4096, 0.530, 0.517, 0.525]
          - [5000, 0.523, 0.515, 0.532]
        footer: "Mean±std: random 0.523±0.031, embed 0.521±0.035, dataflow 0.515±0.038"
    figures_description:
      - "Fig 2a: Box plot of R@1 across 9 seeds, 3 strategies. Boxes heavily overlap, medians nearly identical. Whiskers for all strategies span ~0.48-0.55. No visible separation between strategy distributions."
      - "Fig 2b: Per-seed R@1 line plot (x=seed, y=R@1, color=strategy). Lines interleave chaotically with no consistent ordering — random leads in 4 seeds, embedding in 3, dataflow in 2."
    analysis: >
      策略间 delta (<1pp) 远小于种子间方差 (std~3pp)。Pilot 单种子结果是方差范围内的
      正常波动。这是 worst 档的核心发现：embedding benefit 是 pilot-scale 的统计幻觉。

  - name: "M2 Full StarCoder — 9 seeds × 3 strategies 最终结果"
    plan_id: "plan_013"
    description: >
      StarCoder2-3B full-scale 27 runs。当前 random_s42 R@1=0.454 at step 1000。
    expected_results:
      random_mean_R1: 0.443
      random_std_R1: 0.028
      embedding_distance_mean_R1: 0.435
      embedding_distance_std_R1: 0.033
      dataflow_aware_mean_R1: 0.428
      dataflow_aware_std_R1: 0.040
      embed_vs_random_delta_pp: -0.8
      dataflow_vs_random_delta_pp: -1.5
      cross_seed_R1_std_pp: 3.4
    result_rationale: >
      StarCoder pilot 已经是 negative conclusion（dataflow R@1=0.487 < random 0.492）。
      Full-scale 放大了这个趋势：(1) StarCoder 表征空间 "healthy"（pos_sim=0.80），
      random negatives 已提供足够梯度（margin=0.194），embedding/dataflow 引入的更难
      negatives 反而导致训练不稳定——loss landscape 更尖锐，不同种子落入不同局部最优；
      (2) dataflow negatives 在 StarCoder 上 margin=0.119 vs embedding 0.067，
      dataflow 实际上更"容易"，但 full-scale 下这个 margin 差异未能转化为性能优势，
      因为 StarCoder 的问题不是 negative difficulty 而是编码器容量限制（3B 参数
      + LoRA rank 受限时，更难 negatives 导致梯度冲突）。Cross-seed std 3.4pp 进一步
      确认策略差异 (<1.5pp) 不可靠。
    tables:
      - name: "Table 3: StarCoder Full-Scale R@1 by Strategy × Seed"
        columns: [seed, random, embedding, dataflow]
        rows:
          - [42, 0.454, 0.448, 0.442]
          - [123, 0.440, 0.425, 0.418]
          - [456, 0.462, 0.456, 0.440]
          - [789, 0.435, 0.430, 0.412]
          - [1024, 0.448, 0.442, 0.435]
          - [2048, 0.425, 0.418, 0.398]
          - [3000, 0.458, 0.450, 0.448]
          - [4096, 0.430, 0.422, 0.425]
          - [5000, 0.438, 0.428, 0.430]
        footer: "Mean±std: random 0.443±0.028, embed 0.435±0.033, dataflow 0.428±0.040"
    figures_description:
      - "Fig 2c: StarCoder box plot 与 Qwen 类似，三策略完全重叠。Dataflow 的 whisker 下端更低（0.398），显示更大不稳定性。"
    analysis: >
      StarCoder 上 dataflow 甚至表现最差（-1.5pp vs random），方向与 pilot 一致但
      幅度更大。Embedding 也未能帮助。结论：两编码器在 full-scale 下均不支持任何
      非 random 策略的优势。

  # ============================================================
  # plan_003: SWE-bench Lite
  # ============================================================
  - name: "M3a SWE-bench Lite End-to-End Evaluation"
    plan_id: "plan_003"
    description: >
      SWE-bench Lite (300 instances) end-to-end evaluation，使用 Qwen3.6-27B agent，
      对比 3 个 strategy 的 best checkpoint 作为 retriever。
    expected_results:
      random_resolve_rate: 0.187
      embedding_resolve_rate: 0.190
      dataflow_resolve_rate: 0.183
      embed_vs_random_delta_pp: 0.3
      dataflow_vs_random_delta_pp: -0.4
      swebench_resolve_delta_pp: 0.3
      retrieval_R1_on_swebench:
        random: 0.42
        embedding: 0.43
        dataflow: 0.41
      n_instances_evaluated: 287
      n_instances_failed: 13
    result_rationale: >
      SWE-bench Lite 的 resolve rate 由 retrieval → agent pipeline 多阶段组成，
      retriever 差异被下游 agent 的 stochasticity 大幅稀释。即使 retrieval R@1 差异
      存在 1pp，经过 agent 的 code generation + apply patch + test 环节后，resolve rate
      差异被压缩到 <0.5pp。具体原因：
      (1) SWE-bench 中很多 "easy" instances（~30%）任何 retriever 都能找到正确文件，
      策略差异为零；
      (2) "hard" instances（~25%）任何 retriever 都找不到，agent 依赖推理能力而非检索；
      (3) 只有 ~45% 的中间难度 instances 中 retrieval 策略可能产生差异，但 agent
      的 code generation variance（温度、context window 限制）进一步模糊了信号；
      (4) 300 instances 中有效差异空间 ~135 个，0.3pp delta 对应仅 ~1 个额外解决的
      instance，完全在噪声范围内。此外 full-scale retriever 本身策略间差异已消失，
      SWE-bench 只是进一步确认。
    tables:
      - name: "Table 5: SWE-bench Lite Resolve Rates"
        columns: [strategy, resolve_rate, retrieval_R1, n_resolved, n_total]
        rows:
          - [random, 0.187, 0.42, 54, 287]
          - [embedding_distance, 0.190, 0.43, 55, 287]
          - [dataflow_aware, 0.183, 0.41, 53, 287]
        footer: "Best delta: +0.3pp (embed vs random), not significant (p=0.89 McNemar)"
    figures_description:
      - "Fig 5: Bar chart of resolve rates, 3 bars nearly identical height (~18.5%), error bars from bootstrap overlap entirely. A horizontal dashed line shows SweRank baseline at ~19% for reference — our best retriever 略低于 published SweRank."
    analysis: >
      SWE-bench 结果不仅不支持 embedding/dataflow 策略的优势，甚至所有策略的 resolve rate
      都低于 SweRank baseline。这暗示 full-scale 训练可能引入了某种 regression（数据分布
      偏移？）。需排查训练数据与 SWE-bench 的 domain overlap。

  # ============================================================
  # plan_004: RepoBench-R
  # ============================================================
  - name: "M3b RepoBench-R Cross-File Retrieval"
    plan_id: "plan_004"
    description: >
      RepoBench-R 作为第二基准，retrieval-only 评估，无 LLM agent。
    expected_results:
      random_R1: 0.312
      embedding_R1: 0.308
      dataflow_R1: 0.295
      embed_vs_random_delta_pp: -0.4
      dataflow_vs_random_delta_pp: -1.7
      random_R5: 0.58
      embedding_R5: 0.57
      dataflow_R5: 0.56
      pretrained_baseline_R1: 0.285
    result_rationale: >
      RepoBench-R 是 cross-file completion 任务，与 SWE-smith 的 bug localization
      分布差异更大。Full-scale 训练在 SWE-smith 上 overfit 的模型在 RepoBench 上
      表现出不同的行为模式：
      (1) 所有策略都优于 pretrained baseline（+2-3pp），说明 contrastive fine-tuning
      本身有效，但策略间差异在 domain shift 下被进一步压缩；
      (2) Dataflow negatives 在 RepoBench 上表现最差，因为 SWE-smith 的 dataflow 结构
      （bug-fix oriented）与 RepoBench 的 completion-oriented 代码结构不匹配——
      SWE-smith 中 disconnected = irrelevant 的假设在 completion 场景中不成立；
      (3) Embedding negatives 略低于 random 是因为 full-scale embedding mining 选出的
      negatives 过度 fit 到 SWE-smith 的相似性分布，domain shift 后反而损害泛化。
    tables:
      - name: "Table 6: RepoBench-R Results (Qwen encoder)"
        columns: [strategy, R@1, R@5, R@10, MRR]
        rows:
          - [pretrained, 0.285, 0.52, 0.68, 0.401]
          - [random, 0.312, 0.58, 0.73, 0.438]
          - [embedding_distance, 0.308, 0.57, 0.72, 0.432]
          - [dataflow_aware, 0.295, 0.56, 0.71, 0.418]
    figures_description:
      - "Fig 6: Grouped bar chart comparing SWE-smith val vs RepoBench-R R@1。两个 benchmark 上策略排序不一致——SWE-smith 上 embed≈random>dataflow，RepoBench 上 random>embed>dataflow。"
    analysis: >
      RepoBench-R 进一步证明策略差异不稳定且 domain-dependent。Dataflow 策略的负迁移
      尤其严重（-1.7pp），支持 negative result 叙事中 "structural negatives 不 generalize"
      的论点。

  # ============================================================
  # plan_005: Embedding vs Random 深度分层分析
  # ============================================================
  - name: "Embedding vs Random Deep Stratified Analysis"
    plan_id: "plan_005"
    description: >
      按 repo size、code complexity、neg_difficulty 分层分析 embedding negatives 的效果。
    expected_results:
      by_repo_size:
        small_lt50:
          random_R1: 0.61
          embedding_R1: 0.59
          delta_pp: -2.0
        medium_50_200:
          random_R1: 0.54
          embedding_R1: 0.55
          delta_pp: 1.0
        large_200_500:
          random_R1: 0.51
          embedding_R1: 0.50
          delta_pp: -1.0
        xlarge_500plus:
          random_R1: 0.48
          embedding_R1: 0.48
          delta_pp: 0.0
      by_neg_difficulty_quartile:
        easy_q1_delta_pp: 0.5
        medium_q2_delta_pp: -0.3
        hard_q3_delta_pp: -1.2
        hardest_q4_delta_pp: -2.1
      correlation_margin_vs_benefit: -0.15
      correlation_repo_size_vs_benefit: -0.08
    result_rationale: >
      分层分析揭示 embedding benefit 不是"消失"而是"抵消"——在某些 strata 正向、
      其他 strata 负向，总和接近零：
      (1) Small repos 上 embedding mining 实际有害（-2pp），因为小 repo 的 file pool
      只有 ~10-50 个文件，embedding mining 选出的 "nearest" negative 往往就是 gold file
      的近邻（同一个 module），形成 false hard negatives 损害训练信号；
      (2) Medium repos 上 embedding 略有优势（+1pp），因为 pool 足够大使 mining 选到
      真正的 hard negatives，且难度梯度合理；
      (3) Large/xlarge repos 上差异消失，因为 random sampling 在大 pool 中已经有合理
      概率采到 moderately hard negatives，embedding mining 的额外选择性优势被稀释；
      (4) 按 neg_difficulty 分层更清晰：最难 quartile（margin 最小）中 embedding 有害
      （-2.1pp），因为过难的 negatives 导致梯度冲突/训练不稳定。这解释了为什么
      full-scale（更多 large repos → 更多 hard quartile instances）中 benefit 消失。
    tables:
      - name: "Table 7: Embedding Benefit by Repo Size"
        columns: [repo_tier, n_instances, random_R1, embed_R1, delta_pp]
        rows:
          - [small (<50), 500, 0.610, 0.590, -2.0]
          - [medium (50-200), 4096, 0.540, 0.550, +1.0]
          - [large (200-500), 13628, 0.510, 0.500, -1.0]
          - [xlarge (500+), 25949, 0.480, 0.480, 0.0]
    figures_description:
      - "Fig 7a: Scatter plot of per-instance embedding benefit (Δ R@1) vs neg_difficulty margin. Weak negative correlation (r=-0.15). Cloud centered around zero, no clear trend."
      - "Fig 7b: Heatmap of embedding benefit across repo_size × difficulty quartile. Only one cell (medium × easy) is clearly positive. Most cells near zero or negative."
    analysis: >
      核心发现：embedding benefit 是 repo size 和 negative difficulty 的函数，
      在 pilot 的 data composition 下恰好为正，在 full-scale 的 data composition 下
      恰好为零或负。这不是方法失败，而是 pilot evaluation bias——小规模评估
      over-represents 中等 repo，恰好是 embedding mining 的 sweet spot。

  # ============================================================
  # plan_007: Hop Ablation
  # ============================================================
  - name: "Hop-Distance Call-Graph Bounding Ablation"
    plan_id: "plan_007"
    description: >
      1-hop vs 2-hop vs 3-hop call-graph bounding 对 dataflow negative 质量的影响。
    expected_results:
      hop_1:
        connected_pct: 0.12
        disconnected_neg_margin: 0.035
        training_R1: 0.513
      hop_2:
        connected_pct: 0.34
        disconnected_neg_margin: 0.029
        training_R1: 0.515
      hop_3:
        connected_pct: 0.58
        disconnected_neg_margin: 0.022
        training_R1: 0.510
      delta_1hop_vs_2hop_pp: -0.2
      delta_2hop_vs_3hop_pp: 0.5
      all_vs_random_best_pp: -0.8
    result_rationale: >
      Hop distance 改变 connected/disconnected 的划分粒度，但在 worst 档下无法拯救
      dataflow 策略：
      (1) 1-hop 过于严格（仅 12% connected），大量 gold-relevant files 被错误标记为
      disconnected，产生大量 false hard negatives → 训练信号受损；
      (2) 2-hop（当前设置）是 pilot 中的最优，但 full-scale 下效果与 random 无异；
      (3) 3-hop 过于宽泛（58% connected），disconnected pool 缩小到几乎只剩 truly
      unrelated files，这些 negatives 太容易（margin=0.022），训练信号退化为
      接近 random sampling 的效果但 pool 更小；
      (4) 三种 hop 设置的 R@1 范围仅 0.510-0.515，都低于 random baseline 0.523，
      说明 structural bounding 本身在 full-scale 下不是一个有效的 negative selection
      维度——问题出在 "结构断开≠语义无关" 这个核心假设。
    tables:
      - name: "Table 8: Hop-Distance Ablation (Qwen, seed 42)"
        columns: [hops, connected_pct, disconn_margin, R@1, vs_random_pp]
        rows:
          - [1, 0.12, 0.035, 0.513, -1.0]
          - [2, 0.34, 0.029, 0.515, -0.8]
          - [3, 0.58, 0.022, 0.510, -1.3]
          - [random, "-", "-", 0.523, 0.0]
    figures_description:
      - "Fig 8: Line plot of R@1 vs hop distance, with random baseline as horizontal dashed line. All 3 hop settings below baseline. Curve is nearly flat."
    analysis: >
      Hop distance 是 second-order 参数——当 first-order 效应（结构断开作为 hardness proxy）
      本身无效时，调节粒度无法改变结论。

  # ============================================================
  # plan_008: Data Size Scaling
  # ============================================================
  - name: "Training Data Size Scaling Ablation"
    plan_id: "plan_008"
    description: >
      1K vs 3K vs 5K（当前 full-scale ~15K instances 中子采样）对策略差异的影响。
    expected_results:
      size_1k:
        random_R1: 0.505
        embedding_R1: 0.518
        dataflow_R1: 0.512
        embed_delta_pp: 1.3
      size_3k:
        random_R1: 0.515
        embedding_R1: 0.520
        dataflow_R1: 0.513
        embed_delta_pp: 0.5
      size_5k:
        random_R1: 0.520
        embedding_R1: 0.521
        dataflow_R1: 0.516
        embed_delta_pp: 0.1
      size_15k_full:
        random_R1: 0.523
        embedding_R1: 0.521
        dataflow_R1: 0.515
        embed_delta_pp: -0.2
      embed_benefit_slope_per_1k: -0.11
    result_rationale: >
      这个 ablation 精确解释了 pilot-to-full-scale discrepancy 的机制：
      (1) 1K instances（≈pilot 规模）复现了 pilot 的 embedding benefit（+1.3pp），
      确认 pilot 结果本身没有 bug——在小规模下 embedding mining 确实有效；
      (2) 随数据量增长，benefit 单调递减（斜率≈-0.11pp per 1K instances）；
      (3) 原因是 data scaling 改变了有效 negative difficulty 分布——1K 时 random pool
      中真正 hard 的 negatives 极少（小 pool → 大多是 easy negatives），embedding mining
      通过选择 nearest neighbors 提供了必要的 difficulty gradient。但随着 pool 增大，
      random sampling 的"命中率"自然上升，embedding mining 的增量价值趋零；
      (4) 5K 处 delta 已缩至 0.1pp（不显著），15K 处反转为 -0.2pp；
      (5) 这是 negative result paper 的关键证据：small-scale evaluation 系统性高估
      hard negative mining 的收益，因为 scale 本身就是一种隐性的 negative difficulty
      调节器。
    tables:
      - name: "Table 9: Data Size × Strategy Interaction"
        columns: [data_size, random_R1, embed_R1, dataflow_R1, embed_delta]
        rows:
          - ["1K", 0.505, 0.518, 0.512, +1.3]
          - ["3K", 0.515, 0.520, 0.513, +0.5]
          - ["5K", 0.520, 0.521, 0.516, +0.1]
          - ["15K (full)", 0.523, 0.521, 0.515, -0.2]
    figures_description:
      - "Fig 9: Dual-axis plot. Left axis: R@1 for each strategy (3 lines converging as data size grows). Right axis: embed_delta_pp (descending line crossing zero between 5K and 15K). Clear visual narrative of benefit disappearing with scale."
    analysis: >
      这张图是论文的核心 figure——直观展示 "hard negative mining 的收益随数据规模递减
      并最终消失" 的 scaling law。对 negative result paper 的贡献极大，因为它提供了
      可预测的量化关系，而非仅仅 "结果没复现" 的定性陈述。

  # ============================================================
  # plan_009: Fusion Head Ablation
  # ============================================================
  - name: "Fusion Head Architecture Ablation"
    plan_id: "plan_009"
    description: >
      Embedding-only vs structural-features-only vs combined fusion head，
      测试结构特征是否通过不同 fusion 方式提供价值。
    expected_results:
      embedding_only_R1: 0.523
      structural_only_R1: 0.385
      combined_R1: 0.519
      embed_only_vs_combined_pp: 0.4
    result_rationale: >
      Fusion head 架构无法从无到有创造 structural signal 的价值：
      (1) Embedding-only head 与 random strategy 性能相当（0.523），因为 LoRA fine-tuned
      embeddings 本身已捕获了足够的 code similarity 信息；
      (2) Structural-features-only head 大幅下降至 0.385——结构特征（is_connected,
      dataflow_distance, call_graph_hops）单独不足以判断 relevance，因为大部分
      file pairs 的结构特征是 sparse 的（structural_data_rate=0.34，66% pairs 无结构信息）；
      (3) Combined head 反而略低于 embedding-only（-0.4pp），因为 noisy structural features
      干扰了 embedding signal——当 66% instances 的结构特征为 null/zero 时，
      fusion layer 必须学会忽略结构维度，但 LoRA 的低秩约束使这个 "ignore" 信号
      不够干净；
      (4) 这进一步支持了 structural signal 在 full-scale 下无效的结论。
    tables:
      - name: "Table 10: Fusion Head Ablation (Qwen, seed 42)"
        columns: [head_type, R@1, R@5, val_loss]
        rows:
          - [embedding_only, 0.523, 0.955, 0.486]
          - [structural_features, 0.385, 0.780, 0.812]
          - [combined, 0.519, 0.950, 0.495]
    figures_description:
      - "Fig A1 (appendix): Attention weight visualization for combined head — structural feature attention weights converge toward zero during training, model learns to ignore them."
    analysis: >
      结构特征作为独立信号维度不足，作为辅助信号有害。这排除了 "也许 dataflow 信号有用
      但 negative mining 不是正确的注入方式" 的替代假设。

  # ============================================================
  # plan_010: Dataflow-Distance Weighted Negatives
  # ============================================================
  - name: "Dataflow-Distance Weighted vs Binary Negatives"
    plan_id: "plan_010"
    description: >
      连续 dataflow distance 加权 vs 二元 connected/disconnected 的 negative selection。
    expected_results:
      binary_disconnected_R1: 0.515
      distance_weighted_R1: 0.517
      delta_pp: 0.2
      vs_random_pp: -0.6
    result_rationale: >
      Distance weighting 是对 binary disconnected 的细化——用 shortest dataflow path
      length 作为权重偏好更远的（更 disconnected）negatives。但在 worst 档下改进微乎其微
      （+0.2pp vs binary），因为：
      (1) 核心问题不是 negative selection 的粒度，而是 structural disconnection 作为
      hardness proxy 本身的有效性——weighted 版本在一个无效信号上做更精细的选择，
      不改变根本问题；
      (2) 距离信息 noisy——CodeQL 的 dataflow path 是 approximation，real shortest path
      与 estimated path 的相关性仅 ~0.6（由于 scope bounding），weighting 基于 noisy
      distance 引入额外噪声；
      (3) 两个版本都低于 random baseline（-0.6pp），进一步确认结构信号无效。
    tables: []
    figures_description:
      - "Fig A2 (appendix): Histogram of dataflow distances for weighted negatives. Most distances clustered at 2-3 hops, very few at 5+. Distribution too concentrated to provide meaningful difficulty gradient."
    analysis: >
      细化无效信号的粒度不改善性能。这是对 "也许我们只需要更好的结构度量" 假设的反驳。

  # ============================================================
  # plan_011: Failure Analysis
  # ============================================================
  - name: "Failure Analysis: 50 SweRank/BM25 Failures"
    plan_id: "plan_011"
    description: >
      对 50 个 SweRank/BM25 检索失败的 SWE-bench instances 进行手动分类，
      分析 dataflow 信号是否能帮助。
    expected_results:
      n_analyzed: 50
      categories:
        cross_file_dependency: 18
        naming_ambiguity: 12
        scattered_changes: 9
        test_file_confusion: 7
        other: 4
      dataflow_could_help: 6
      dataflow_actually_helped: 2
      dataflow_hurt: 3
      dataflow_neutral: 39
    result_rationale: >
      手动分析 50 个失败案例后发现 dataflow 信号能帮助的场景远少于预期：
      (1) Cross-file dependency（18 cases）是 dataflow 理论上的 sweet spot，但实际
      仅 4/18 有可用的 CodeQL dataflow 路径——其余 14 个的 dependency 是通过 import、
      type reference 或 configuration 而非 data flow，CodeQL 的 inter-procedural
      analysis 未覆盖这些；
      (2) Naming ambiguity（12 cases）中 dataflow 无法帮助——问题是同名函数/类在
      不同 module 中，structural 和 textual signal 同时失效；
      (3) 6 个理论上 dataflow 可帮助的 cases 中，仅 2 个实际在 dataflow-trained model
      中被正确检索——另 4 个因训练不稳定/过拟合而性能退化抵消了理论优势；
      (4) 3 个 cases 中 dataflow 实际有害——将结构上相关但 gold set 外的文件排入
      top-1，挤掉了正确答案。
    tables:
      - name: "Table 11: Failure Category Analysis"
        columns: [category, count, df_could_help, df_actually_helped, df_hurt]
        rows:
          - [cross_file_dep, 18, 4, 1, 1]
          - [naming_ambiguity, 12, 0, 0, 1]
          - [scattered_changes, 9, 2, 1, 1]
          - [test_confusion, 7, 0, 0, 0]
          - [other, 4, 0, 0, 0]
          - [total, 50, 6, 2, 3]
    figures_description:
      - "Fig 10: Sankey diagram from failure categories → dataflow applicability → actual outcome. Visual shows most flow going to 'neutral' — dataflow signal is irrelevant to most failure modes."
    analysis: >
      Dataflow 的理论覆盖面（12% = 6/50 可能帮助）和实际有效率（4% = 2/50 实际帮助）
      远低于立论所需。对 negative result paper 的贡献：提供 error taxonomy 证明
      structural signal 的适用范围窄于预期。

  # ============================================================
  # plan_012: Qualitative Examples
  # ============================================================
  - name: "Qualitative Examples: Structural Negatives Impact"
    plan_id: "plan_012"
    description: >
      挑选 5-10 个 structural negatives 改变检索结果的定性案例。
    expected_results:
      positive_examples_found: 3
      negative_examples_found: 4
      neutral_examples: 3
      net_narrative: negative
    result_rationale: >
      在 worst 档下，能找到的正面案例数量与负面案例相当甚至更少：
      (1) 3 个正面案例：dataflow training 将结构相关文件从 top-5 提升到 top-1，
      但这些改善也出现在 embedding strategy 的部分种子中，不能归因于 dataflow；
      (2) 4 个负面案例：dataflow training 将结构上相近但 gold set 外的文件推高排名，
      挤掉了正确答案。典型模式：文件 A 通过 data flow 连接到 gold file B，
      dataflow 策略错误地将 A 排在 B 之前；
      (3) 3 个中性案例：dataflow 改变了 top-10 内的排序但不影响 top-1/top-5；
      (4) 定性分析 net negative，无法支撑 paper 中的正面叙事。对 negative result paper
      可用——展示 structural negatives 的 failure modes。
    tables: []
    figures_description:
      - "Fig A3: Side-by-side retrieval ranking comparison (random vs dataflow) for 3 positive and 3 negative cases. Each case shows query, top-5 files, gold files highlighted. Negative cases are more dramatic — rank drops from 1→4."
    analysis: >
      定性证据反而支持 negative result 叙事。典型 failure mode（structural proximity ≠
      task relevance）是重要的methodological insight。

  # ============================================================
  # plan_014: Temperature Ablation
  # ============================================================
  - name: "Temperature Ablation: τ ∈ {0.05, 0.1, 0.2}"
    plan_id: "plan_014"
    description: >
      三个温度 × 三个策略，测试 embedding benefit 是否是温度 regime-specific。
    expected_results:
      tau_005:
        random_R1: 0.498
        embedding_R1: 0.485
        dataflow_R1: 0.475
        embed_delta_pp: -1.3
      tau_010:
        random_R1: 0.523
        embedding_R1: 0.521
        dataflow_R1: 0.515
        embed_delta_pp: -0.2
      tau_020:
        random_R1: 0.510
        embedding_R1: 0.508
        dataflow_R1: 0.502
        embed_delta_pp: -0.2
      best_overall_tau: 0.10
      any_tau_with_significant_embed_benefit: false
    result_rationale: >
      温度调节改变 contrastive loss 对 similarity margin 的敏感度，但无法拯救无效的
      mining strategy：
      (1) τ=0.05 使 loss 对 margin 极其敏感——在 Qwen 的 saturated space
      （pos_sim=0.9855, embedding neg_sim=0.9685, margin=0.017）中，如此小的 margin
      在 τ=0.05 下产生几乎相同的 loss 贡献，embedding negatives 等于 random。
      但更严重的是 τ=0.05 放大了个别 extreme negative 的梯度，导致训练不稳定，
      所有策略性能下降（尤其 dataflow，因为 dataflow negatives 的 margin distribution
      更 heavy-tailed）；
      (2) τ=0.10（当前默认）是最优温度，但策略间无显著差异；
      (3) τ=0.20 使 loss 对 margin 不够敏感——hard negatives 的额外 difficulty 被
      soft temperature 压缩，embedding/dataflow mining 的理论优势被进一步稀释；
      (4) 没有任何温度 regime 能让 embedding benefit 达到统计显著，因为 full-scale
      下策略间的 "信号" 本身不存在（是 pilot 的噪声），温度只是调节 loss landscape
      的曲率，不能创造信号。
    tables:
      - name: "Table 12: Temperature × Strategy Interaction (Qwen, mean of 3 seeds)"
        columns: [tau, random, embedding, dataflow, best_strategy]
        rows:
          - [0.05, 0.498, 0.485, 0.475, random]
          - [0.10, 0.523, 0.521, 0.515, random]
          - [0.20, 0.510, 0.508, 0.502, random]
    figures_description:
      - "Fig 11: 3×3 heatmap (τ × strategy), color = R@1. Random column consistently darkest (highest). No cell in embed/dataflow columns exceeds corresponding random cell."
    analysis: >
      Temperature 不是 confound——在所有温度 regime 下，random 策略都是最优或并列最优。
      排除了 "pilot 的 embedding benefit 是因为 τ=0.1 恰好适合 embedding mining" 的假设。

  # ============================================================
  # plan_015: Dynamic Mining Baseline
  # ============================================================
  - name: "Dynamic Embedding Mining vs Static"
    plan_id: "plan_015"
    description: >
      Per-epoch 重新 mining embedding negatives vs 一次性从 pretrained model mining。
    expected_results:
      static_embedding_R1: 0.521
      dynamic_epoch1_R1: 0.521
      dynamic_epoch2_R1: 0.519
      dynamic_epoch3_R1: 0.515
      dynamic_mean_R1: 0.518
      dynamic_vs_static_pp: -0.3
      dynamic_vs_random_pp: -0.5
    result_rationale: >
      Dynamic mining 理论上解决 "pretrained embedding 与 fine-tuned embedding 偏移导致
      negatives 过时" 的问题。但在 worst 档下非但不改善，反而略有下降：
      (1) Epoch 1 dynamic ≈ static（因为 epoch 1 开始时 model 就是 pretrained，
      mining 结果相同）；
      (2) Epoch 2-3 的 re-mining 产生了 curriculum shift 效应——随着 model 改善，
      nearest neighbors 改变，新选出的 negatives 更难但也更 noisy（因为 fine-tuned
      model 的 embedding space 在 LoRA 下只部分更新，re-mining 的 nearest neighbors
      可能是 LoRA 的 artifacts 而非真正的 hard negatives）；
      (3) Re-mining 引入的计算开销显著（每 epoch 需重新编码全部 ~44K instances，
      ~2h per re-mining），cost-benefit 明显不值得；
      (4) Dynamic mining 的失败进一步证明问题不是 "mining 过时" 而是 "mining 本身
      在大规模下无效"。
    tables:
      - name: "Table 13: Static vs Dynamic Mining (Qwen, seed 42)"
        columns: [method, epoch1_R1, epoch2_R1, epoch3_R1, best_R1]
        rows:
          - [static, 0.540, 0.530, 0.512, 0.540]
          - [dynamic, 0.540, 0.525, 0.505, 0.540]
          - [random, 0.535, 0.528, 0.510, 0.535]
    figures_description:
      - "Fig A4: Training curves (R@1 vs step) for static, dynamic, random. Three nearly overlapping curves with dynamic showing slightly more variance."
    analysis: >
      Dynamic mining 排除了 "staleness" 作为 embedding mining 失效的解释。
      Mining 策略本身在大规模下不提供增量价值。

  # ============================================================
  # plan_016: Bootstrap CI for SWE-bench
  # ============================================================
  - name: "Bootstrap CI for SWE-bench Resolve Rates"
    plan_id: "plan_016"
    description: >
      10,000 bootstrap resamples 计算 SWE-bench resolve rate 的 95% CI。
    expected_results:
      random_resolve_rate: 0.187
      random_95ci: [0.143, 0.232]
      embedding_resolve_rate: 0.190
      embedding_95ci: [0.147, 0.235]
      dataflow_resolve_rate: 0.183
      dataflow_95ci: [0.140, 0.228]
      embed_vs_random_delta: 0.003
      embed_vs_random_delta_95ci: [-0.038, 0.045]
      embed_benefit_bootstrap_p: 0.78
      dataflow_vs_random_delta: -0.004
      dataflow_vs_random_delta_95ci: [-0.048, 0.038]
    result_rationale: >
      Bootstrap CI 极宽（±4-5pp），因为 SWE-bench Lite 仅 300 instances，
      有效样本更少（~287 after failures）：
      (1) 单策略 CI 宽度 ~9pp（±4.5pp），策略间 delta（0.3pp）远小于 CI 宽度；
      (2) Paired delta CI [-3.8pp, +4.5pp] 包含零且两侧几乎对称——没有任何方向性信号；
      (3) Bootstrap p=0.78 远高于任何合理显著性阈值，确认 delta 不显著；
      (4) 即使使用 pilot 阶段的 +2.0pp delta，在 n=287 下的 power analysis 显示
      需要 ~2000 instances 才能在 α=0.05 下 detect 2pp 的差异——SWE-bench Lite
      本质上 underpowered for 这个效应量；
      (5) 对 negative result paper 有力：不仅 point estimate 接近零，统计检验也
      确认无法拒绝零假设。
    tables:
      - name: "Table 14: SWE-bench Bootstrap Statistics"
        columns: [comparison, delta_pp, 95%_CI, p_value, interpretation]
        rows:
          - [embed vs random, +0.3, "[-3.8, +4.5]", 0.78, not significant]
          - [dataflow vs random, -0.4, "[-4.8, +3.8]", 0.68, not significant]
          - [dataflow vs embed, -0.7, "[-5.2, +3.5]", 0.55, not significant]
    figures_description:
      - "Fig 12: Bootstrap distribution of embed_vs_random delta. Gaussian-shaped, centered near zero. Vertical dashed lines at 95% CI. Shaded region under the null hypothesis. ~78% of distribution above zero but CI includes large negative values."
    analysis: >
      统计分析确认 SWE-bench 差异不显著。Power analysis 证明 SWE-bench Lite 的 n=300
      本质上无法 detect <5pp 的 retriever 差异——这本身是一个 methodological contribution
      for the negative result paper。

  # ============================================================
  # plan_017: Inference-Time Graph Method Comparison
  # ============================================================
  - name: "Inference-Time Graph Method Discussion"
    plan_id: "plan_017"
    description: >
      与 CodexGraph, LocAgent 等 inference-time graph 方法的定性比较讨论。
    expected_results:
      locagent_reported_resolve_rate: 0.262
      our_best_resolve_rate: 0.190
      codexgraph_reported_R1: 0.48
      our_best_R1: 0.523
      complementarity_evidence: none
    result_rationale: >
      Inference-time graph methods 在 SWE-bench 上的表现远优于我们的 training-time
      structural mining approach：
      (1) LocAgent 报告 26.2% resolve rate（vs 我们的 ~19%），差距主要来自
      LocAgent 使用 runtime graph navigation（动态探索 call graph at inference），
      而我们的 structural signal 仅用于 static training-time negative selection——
      本质是两种完全不同的信息利用方式；
      (2) 在 worst 档下我们无法证明 "training-time structural mining 与 inference-time
      graph navigation 互补"——因为 training-time mining 本身无效，所以无互补可言；
      (3) 这个比较反而支持 inference-time graph methods 是更有效的结构信息利用范式——
      structural signal 的价值在 navigation（决定下一步看什么文件）而非 mining
      （决定训练用什么负样本）；
      (4) 对 negative result paper 的 framing 有帮助：可以用 inference-time methods
      的成功来反衬 training-time mining 的失败，论证 "structural information 有价值
      但应在 inference time 使用" 这一 insight。
    tables:
      - name: "Table 15: Training-Time vs Inference-Time Structure Utilization"
        columns: [method, structure_usage, SWE_bench_resolve, retrieval_R1]
        rows:
          - [ours (random), training negatives, 0.187, 0.523]
          - [ours (dataflow), training negatives, 0.183, 0.515]
          - [LocAgent, inference navigation, 0.262, "-"]
          - [CodexGraph, inference navigation, "-", 0.48*]
        footer: "*CodexGraph R@1 on different benchmark, not directly comparable"
    figures_description:
      - "Fig 13: Conceptual diagram contrasting training-time mining (static, one-shot selection → training data → fixed model) vs inference-time navigation (dynamic, per-query graph exploration). Highlight: structural signal is most valuable when it can adapt to the specific query."
    analysis: >
      这个比较将 negative result 升华为 positive insight：结构信息的价值在于 query-adaptive
      navigation，而非 static negative mining。这为 related work section 提供了
      coherent narrative。

  # ============================================================
  # 额外：Data Pipeline Bug Check（worst 档必需）
  # ============================================================
  - name: "Data Pipeline Distribution Audit"
    plan_id: "pre_analysis"
    description: >
      排查 full-scale 训练数据与 pilot 数据的分布差异，确认 negative result 是真实的
      而非工程错误。
    expected_results:
      pilot_vs_full_repo_overlap: 0.85
      pilot_mean_files_per_repo: 45
      full_mean_files_per_repo: 185
      pilot_difficulty_distribution_ks_p: 0.003
      pilot_structural_rate: 0.58
      full_structural_rate: 0.34
      data_bug_found: false
      distribution_shift_confirmed: true
      shift_severity: moderate
    result_rationale: >
      Full-scale 数据没有 pipeline bug，但存在明确的分布偏移：
      (1) Pilot 用了 ~2K instances 从 8-10 个 medium-size repos，structural_data_rate=0.58
      （大部分 instances 有结构信息）。Full-scale 15K instances 来自 123 repos，
      dominated by large/xlarge repos（69/123），structural_data_rate=0.34——
      几乎一半 instances 在 full-scale 中没有结构信息，dataflow strategy 只能 fallback
      到 random selection；
      (2) KS test 确认难度分布显著不同（p=0.003）——full-scale 中 easy instances
      （大 repo 中的 trivially locatable bugs）比例更高，被所有策略轻松解决，
      稀释了策略间差异；
      (3) 这不是 "bug" 而是 "pilot selection bias"——pilot repos 被挑选为 CodeQL-friendly
      （high structural coverage），不代表真实分布。这个 audit 本身是重要的
      methodological contribution，论证了 pilot evaluation 的 sampling bias 问题。
    tables:
      - name: "Table A1: Pilot vs Full-Scale Data Distribution"
        columns: [metric, pilot, full_scale, p_value]
        rows:
          - [n_instances, ~2000, 15133, "-"]
          - [n_repos, 8, 123, "-"]
          - [structural_rate, 0.58, 0.34, "<0.001"]
          - [mean_files_per_repo, 45, 185, "<0.001"]
          - [median_neg_margin_embed, 0.025, 0.017, 0.003]
          - [pct_large_repos, 0.30, 0.56, "<0.001"]
    figures_description:
      - "Fig A5: Overlaid density plots of neg_difficulty margin for pilot (blue) vs full-scale (red) data. Full-scale distribution shifted left (easier negatives) with heavier right tail. Clear visual evidence of distribution shift."
    analysis: >
      Distribution audit 确认 negative result 是真实的——pilot selection bias 导致了
      不可复现的初始结论。这个 audit 是 negative result paper 的必要组成部分，
      否则 reviewer 会质疑 "是不是你代码有 bug"。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6636e07e-5e1d-4011-9777-5e0e701a4c9a",
  "isSidechain": false,
  "requestId": "req_011Cb27k8uQFKeyfhLccZpAi",
  "type": "assistant",
  "uuid": "0adfe838-ae6e-4438-b1f2-1dfc6622c94d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyqcsyAwAyzXxrBzwkxmHP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17612,
      "cache_read_input_tokens": 11447,
      "output_tokens": 15432,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17612,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15432,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 17612,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17612
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：full-scale 多种子结果未复现 pilot pattern——embedding benefit 消失或反转，核心假设不成立 核心假设：['embedding vs random Δ 在至少一个编码器上为负或 < 0.3pp（pilot 的 +2.0pp 是种子/数据噪声）', 'dataflow…",
  "leafUuid": "0adfe838-ae6e-4438-b1f2-1dfc6622c94d",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze negative result scenario for StructFuse paper",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：full-scale 多种子结果未复现 pilot pattern——embedding benefit 消失或反转，核心假设不成立 核心假设：['embedding vs random Δ 在至少一个编码器上为负或 < 0.3pp（pilot 的 +2.0pp 是种子/数据噪声）', 'dataflow…",
  "leafUuid": "0adfe838-ae6e-4438-b1f2-1dfc6622c94d",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze negative result scenario for StructFuse paper",
  "sessionId": "d3badb30-4425-4866-a4c6-532af99a2625"
}
```

---
