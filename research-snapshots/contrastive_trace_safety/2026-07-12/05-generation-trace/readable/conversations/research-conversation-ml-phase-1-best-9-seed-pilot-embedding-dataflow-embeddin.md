# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：9-seed 全量复现 pilot 模式，embedding 和 dataflow 各自角色均统计显著，机制故事完整成立 核心假设：['embeddin

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/6a3cffa0-8c8e-4873-b7ac-309c623b0889.jsonl`
- **Structured JSON:** [`a265f8275370a215229d.json`](../../sessions/a2/a265f8275370a215229d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T07:59:39.293Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T07:59:39.293Z",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：9-seed 全量复现 pilot 模式，embedding 和 dataflow 各自角色均统计显著，机制故事完整成立\n核心假设：['embedding > random 在两个编码器上均 95% CI 不含零', 'dataflow > random 在 Qwen（饱和空间）上 95% CI 不含零，StarCoder 上无显著差异 → 干净的交互效应', 'SWE-bench Lite 下游验证显示 resolve rate 有可观测提升', '9-seed 方差可控（同策略种子间 R@1 标准差 < 1.5pp）', 'step 1000 过拟合问题通过 early stopping 可控，不影响结论']\n关键指标范围：{'qwen_embed_vs_random_R1_pp': [1.5, 3.0], 'starcoder_embed_vs_random_R1_pp': [1.0, 2.5], 'qwen_dataflow_vs_random_R1_pp': [0.8, 2.5], 'starcoder_dataflow_vs_random_R1_pp': [-1.0, 0.3], 'best_qwen_mean_R1': [0.54, 0.58], 'best_starcoder_mean_R1': [0.46, 0.52], 'swebench_resolve_delta_pp': [2.0, 5.0], 'embed_benefit_bootstrap_p': [0.001, 0.05], 'cross_seed_R1_std': [0.5, 1.5]}\n叙事方向：三条 claim 原样保留。论文叙事：(1) 纠正 CoCoHaNeRe 误解——真正 embedding mining 普遍有效， prior work 的 BM25-proxy 是 artifact；(2) dataflow 提供条件性额外收益，机制通过表征饱和度 定量解释，neg_difficulty margin 分析提供 mechanistic evidence；(3) CodeQL 可扩展。 SWE-bench 下游验证补齐最后一块拼图。Framing 为 \"systematic analysis + mechanistic insight\"， EMNLP Main 定位清晰，三个贡献互相独立且互补。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: structfuse-context\nfocus: D024 重写后的新 framing：论文从 \"method paper (dataflow > all)\" 转为 \"systematic analysis + mechanistic insight\"。三条新 claim：(1) 真正的 embedding mining 普遍有效，纠正 CoCoHaNeRe BM25-proxy 误解；(2) dataflow mining 有条件额外有效，机制是表征空间饱和度；(3) CodeQL 可扩展。已有实证：Qwen R@1=55.3%, StarCoder R@1=45.4%, neg_difficulty margin +17%/+28%, 两编码器 step 1000 过拟合。Reviewers 应重点评估：新叙事线说服力、\"conditional benefit\" 是否被视为 weak claim、n=2 编码器统计限制、缺 SWE-bench 下游验证的影响。\n\n## paper_framing.md\n\n# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \"harm\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).\n\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\n\n- **Headline result template**: \"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\"\n\n## Core Insight\n\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\"\n- Backup: \"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\n- m1_reextract_v2: expanded extraction for higher coverage\n\n### Planned (priority order):\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark\n- plan_015: Dynamic mining baseline\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected\n    vs gold statistics'\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: m1_extraction\n  mvp_registry_id: mvp_p1_codeql_feasibility\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- id: plan_002\n  claim: 1\n  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,\n    3 seeds each, Qwen2.5-Coder-3B LoRA'\n  priority: P0\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  registry_id: m2_embed_verify\n  mvp_registry_id: mvp_p2b_contrastive_training\n  full_registry_ids:\n  - m2_full_qwen\n  - m2_full_starcoder\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- id: plan_003\n  claim: 1\n  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best\n    checkpoint, Qwen3.6-27B agent'\n  priority: P0\n  gpu_budget_hours: 40\n  deps:\n  - plan_002\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no\n    LLM agent'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding\n    negatives 何时最有害'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 3\n  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,\n    connected-but-not-gold ratio by repo size'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan_006_scalability\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- id: plan_007\n  claim: 1\n  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Ablation: fusion head (embedding-only vs structural-features-only\n    vs combined)'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether\n    data-flow helps'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_003\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Qualitative examples: 5-10 cases where structural negatives changed\n    retrieval outcome'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Second encoder validation: repeat M2 core comparison (3 strategies,\n    1 seed) on StarCoder-3B or CodeBERT to test architecture generality'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  dream_source: 'best-R1-W1, median-R2-W5: single encoder is primary generality concern.\n    Upgraded to P0 per Reviewer — this is the #1 factor separating WA from WR.'\n  registry_id: plan_013_starcoder\n  full_registry_id: m2_full_starcoder\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- id: plan_014\n  claim: 2\n  description: 'Temperature ablation: τ ∈ {0.05, 0.1, 0.2} for all 3 strategies, test\n    regime-specificity of embedding harm'\n  priority: P1\n  gpu_budget_hours: 70\n  deps:\n  - plan_002\n  dream_source: 'median-R1-W3: τ=0.05 unusually low, finding may be regime-specific'\n  status: planned\n- id: plan_015\n  claim: 2\n  description: 'Dynamic embedding mining baseline: re-mine embedding negatives per\n    epoch vs static (mine once from pretrained). Isolate selection criterion from\n    curriculum shift.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  dream_source: 'best-R1-W2, median-R1-W2: static vs dynamic mining is potential confound\n    for Claim 2'\n  status: planned\n- id: plan_016\n  claim: 1\n  description: 'Bootstrap CI for SWE-bench Lite: add 95% bootstrap confidence intervals\n    to end-to-end resolve rate evaluation'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  dream_source: 'best-R1-W3, worst-R1-W5: +2.0pp on 300 instances needs statistical\n    significance test'\n  status: planned\n- id: plan_017\n  claim: 1\n  description: 'Inference-time graph method comparison: discuss/compare with CodexGraph,\n    LocAgent — is StructFuse complementary or alternative?'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  dream_source: 'best-R2-W5: no comparison with inference-time graph methods'\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_p1_codeql_feasibility\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    timeout_rate: 0\n    repos_processed: 8\n    repos_skipped: 2\n    cg_mean_s: 29.6\n    cg_max_s: 119.8\n    df_mean_s: 43.4\n    df_max_s: 167.1\n    h2_connected_coverage: 0.014815\n    h2_disconnected_coverage: 0\n    h2_fisher_p: 6.5e-09\n    h2_gold_in_connected_ratio: 1\n    h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'\n- exp_id: mvp_p2a_linear_proxy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    df_bm25_auc: 0.78\n    bm25_only_auc: 0.476\n    auc_delta: 0.304\n    df_bm25_mrr: 0.556\n    bm25_only_mrr: 0.115\n    mrr_delta: 0.441\n    df_bm25_f1: 0.143\n    bm25_only_f1: 0.039\n    top_feature: is_connected (+2.82)\n    repos_evaluated: 3\n    note: 3 repos / 3 positive samples, directional evidence\n- exp_id: p2b-smoke-test\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke8\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-all-9runs\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_p2b_contrastive_training\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    random_s42_recall1: 0.984\n    random_s123_recall1: 0.984\n    random_s456_recall1: 0.992\n    embedding_s42_recall1: 0.874\n    random_mean_recall1: 0.987\n    runs_completed: 4\n    runs_failed: 5\n    failure_type: disk_full_torch_save\n- exp_id: mvp_p2b_contrastive_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_all\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_4runs_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_seed42:\n      recall@1: 0.9449\n      recall@5: 0.9843\n      recall@10: 0.9843\n    random_seed123:\n      recall@1: 0.9449\n      recall@5: 0.9921\n      recall@10: 0.9921\n    random_seed456:\n      recall@1: 0.9291\n      recall@5: 0.9921\n      recall@10: 0.9921\n    emb_dist_seed42:\n      recall@1: 0.6693\n      recall@5: 0.8898\n      recall@10: 0.9291\n    pool_size: 26\n    n_samples: 127\n- exp_id: p2b_5reruns\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_s42:\n      val_loss: 0.0347\n      recall@1: 0.9843\n    random_s123:\n      val_loss: 0.0446\n      recall@1: 0.9843\n    random_s456:\n      val_loss: 0.0188\n      recall@1: 0.9921\n    emb_dist_s42:\n      val_loss: 0.1876\n      recall@1: 0.874\n    emb_dist_s123:\n      val_loss: 0.1461\n      recall@1: 0.874\n    emb_dist_s456:\n      val_loss: 0.1281\n      recall@1: 0.8819\n    dataflow_s42:\n      val_loss: 0.1878\n      recall@1: 0.874\n    dataflow_s123:\n      val_loss: 0.146\n      recall@1: 0.874\n    dataflow_s456:\n      val_loss: 0.1278\n      recall@1: 0.8819\n    runs_completed: 9\n    runs_failed: 0\n    WARNING: dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds\n      — likely code bug in negative sampling\n- exp_id: p2b_dataflow_retrain\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: p2b_eval_4runs_pool50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pool_size: 50\n    n_samples: 127\n    random_s42:\n      recall@1: 0.496\n      recall@5: 0.843\n      recall@10: 0.945\n    random_s123:\n      recall@1: 0.535\n      recall@5: 0.85\n      recall@10: 0.921\n    random_s456:\n      recall@1: 0.543\n      recall@5: 0.843\n      recall@10: 0.953\n    emb_dist_s42:\n      recall@1: 0.488\n      recall@5: 0.835\n      recall@10: 0.874\n    random_mean:\n      recall@1: 0.525\n      recall@5: 0.845\n      recall@10: 0.94\n    emb_dist_vs_random_delta:\n      recall@1: -0.037\n      recall@5: -0.01\n      recall@10: -0.066\n- exp_id: d007_50repo_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances: 240\n    instances_with_extra_connected: 98\n    Z_pct: 40.8\n    avg_connected_minus_gold: 6\n    codeql_timeout_rate_pct: 4\n    by_repo_size:\n      small_lt50:\n        Z_pct: 38.6\n        avg_extra: 2.5\n      medium_50_200:\n        Z_pct: 55.7\n        avg_extra: 11.8\n      large_gt200:\n        Z_pct: 16.7\n        avg_extra: 8.8\n    decision: Z=40.8% >= 20% -> original method viable, proceed to M1\n- exp_id: m1_extraction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- exp_id: m2_early_pilot\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    pid: 795791\n    gpu: cuda:4\n    gpu_mem_mb: 9342\n    gpu_util_pct: 83\n    batch_size: 2\n    num_negatives: 3\n    max_seq_length: 1024\n    strategy_running: random (stuck at step 4000, epoch 3)\n    strategies_completed: 0/3\n    eval_1500:\n      val_loss: 0.5879\n      recall_at_1: 0.4693\n      recall_at_5: 0.4693\n      recall_at_10: 0.4693\n    eval_2000:\n      val_loss: 0.7089\n      recall_at_1: 0.4398\n    eval_2500:\n      val_loss: 0.6961\n      recall_at_1: 0.4291\n    eval_3000:\n      val_loss: 0.728\n      recall_at_1: 0.4104\n    eval_3500:\n      val_loss: 0.7022\n      recall_at_1: 0.4439\n    best_checkpoint: step_1500 (val_loss=0.5879, 6.2GB)\n    WARNING: recall@1=recall@5=recall@10 confirmed eval bug. Process hung after step\n      4000 (~45min no output). Overfitting after step 1500.\n    status_check_at: '2026-05-13T04:42:00Z'\n- exp_id: m2_early_pilot_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: m2_early_pilot_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: m2_embed_verify\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- exp_id: plan_013_starcoder\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- exp_id: plan_006_scalability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- exp_id: m2_full_qwen\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    random_s42:\n      epoch: 3/3\n      current_step: 2950\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.4869\n        recall_at_1: 0.533\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.4651\n        recall_at_1: 0.553\n        recall_at_5: 0.959\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.5365\n        recall_at_1: 0.523\n        recall_at_5: 0.955\n        recall_at_10: 1\n      eval_2000:\n        val_loss: 0.5162\n        recall_at_1: 0.523\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_2500:\n        val_loss: 0.5264\n        recall_at_1: 0.527\n        recall_at_5: 0.956\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.4651, R@1=0.553)\n    progress_snapshot: 2026-05-14T13:37 CST\n- exp_id: m2_full_starcoder\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    random_s42:\n      epoch: 2/3\n      current_step: 2000\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.6194\n        recall_at_1: 0.435\n        recall_at_5: 0.905\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.6134\n        recall_at_1: 0.454\n        recall_at_5: 0.92\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.6528\n        recall_at_1: 0.449\n        recall_at_5: 0.906\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.6134, R@1=0.454)\n    progress_snapshot: 2026-05-14T13:37 CST\n- exp_id: m1_reextract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: neg_difficulty_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_128:\n      random:\n        pos_sim: 0.9804\n        neg_sim: 0.899\n        margin: 0.0816\n        pct_positive_margin: 77.8\n      embedding_distance:\n        pos_sim: 0.9804\n        neg_sim: 0.959\n        margin: 0.0209\n        pct_positive_margin: 60.7\n      dataflow_aware:\n        pos_sim: 0.9805\n        neg_sim: 0.95\n        margin: 0.0309\n        pct_positive_margin: 67.4\n    starcoder_128:\n      random:\n        pos_sim: 0.757\n        neg_sim: 0.553\n        margin: 0.2039\n        pct_positive_margin: 72.8\n      embedding_distance:\n        pos_sim: 0.784\n        neg_sim: 0.668\n        margin: 0.1159\n        pct_positive_margin: 59.2\n      dataflow_aware:\n        pos_sim: 0.761\n        neg_sim: 0.659\n        margin: 0.1022\n        pct_positive_margin: 62.8\n    qwen_2048:\n      random:\n        pos_sim: 0.9855\n        neg_sim: 0.9111\n        margin: 0.0743\n        margin_std: 0.2322\n        pct_positive_margin: 81.8\n      embedding_distance:\n        pos_sim: 0.9855\n        neg_sim: 0.9685\n        margin: 0.017\n        margin_std: 0.114\n        pct_positive_margin: 58.8\n      dataflow_aware:\n        pos_sim: 0.9856\n        neg_sim: 0.9563\n        margin: 0.0293\n        margin_std: 0.1407\n        pct_positive_margin: 73.9\n    starcoder_2048:\n      random:\n        pos_sim: 0.7985\n        neg_sim: 0.6045\n        margin: 0.194\n        margin_std: 0.2788\n        pct_positive_margin: 78\n      embedding_distance:\n        pos_sim: 0.8079\n        neg_sim: 0.7409\n        margin: 0.067\n        margin_std: 0.2056\n        pct_positive_margin: 55\n      dataflow_aware:\n        pos_sim: 0.8009\n        neg_sim: 0.6818\n        margin: 0.1192\n        margin_std: 0.2264\n        pct_positive_margin: 70.4\n    sc_qwen_margin_ratio_128:\n      random: 2.5\n      embedding_distance: 5.54\n      dataflow_aware: 3.3\n    sc_qwen_margin_ratio_2048:\n      random: 2.61\n      embedding_distance: 3.94\n      dataflow_aware: 4.07\n- exp_id: m1_reextract_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T07:59:39.297Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T07:59:39.297Z",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-14T07:59:39.317Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：9-seed 全量复现 pilot 模式，embedding 和 dataflow 各自角色均统计显著，机制故事完整成立
核心假设：['embedding > random 在两个编码器上均 95% CI 不含零', 'dataflow > random 在 Qwen（饱和空间）上 95% CI 不含零，StarCoder 上无显著差异 → 干净的交互效应', 'SWE-bench Lite 下游验证显示 resolve rate 有可观测提升', '9-seed 方差可控（同策略种子间 R@1 标准差 < 1.5pp）', 'step 1000 过拟合问题通过 early stopping 可控，不影响结论']
关键指标范围：{'qwen_embed_vs_random_R1_pp': [1.5, 3.0], 'starcoder_embed_vs_random_R1_pp': [1.0, 2.5], 'qwen_dataflow_vs_random_R1_pp': [0.8, 2.5], 'starcoder_dataflow_vs_random_R1_pp': [-1.0, 0.3], 'best_qwen_mean_R1': [0.54, 0.58], 'best_starcoder_mean_R1': [0.46, 0.52], 'swebench_resolve_delta_pp': [2.0, 5.0], 'embed_benefit_bootstrap_p': [0.001, 0.05], 'cross_seed_R1_std': [0.5, 1.5]}
叙事方向：三条 claim 原样保留。论文叙事：(1) 纠正 CoCoHaNeRe 误解——真正 embedding mining 普遍有效， prior work 的 BM25-proxy 是 artifact；(2) dataflow 提供条件性额外收益，机制通过表征饱和度 定量解释，neg_difficulty margin 分析提供 mechanistic evidence；(3) CodeQL 可扩展。 SWE-bench 下游验证补齐最后一块拼图。Framing 为 "systematic analysis + mechanistic insight"， EMNLP Main 定位清晰，三个贡献互相独立且互补。


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
  "promptId": "88733b8f-c6fe-4eb6-8bab-19f965d659b8",
  "type": "user",
  "uuid": "5912e1ea-fb24-419b-a505-0c78fb48fa0e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T07:59:39.316Z_

```json
{
  "parentUuid": "5912e1ea-fb24-419b-a505-0c78fb48fa0e",
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
  "uuid": "14f8e2c0-e694-4064-a379-1a548aaf35ff",
  "timestamp": "2026-05-14T07:59:39.316Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T07:59:39.316Z_

```json
{
  "parentUuid": "14f8e2c0-e694-4064-a379-1a548aaf35ff",
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
  "uuid": "d853d497-c7d5-4394-aea0-b2cd446bb442",
  "timestamp": "2026-05-14T07:59:39.316Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T07:59:39.316Z_

```json
{
  "parentUuid": "d853d497-c7d5-4394-aea0-b2cd446bb442",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b61f4914-1d83-400b-ab31-cd37ea11e0e2",
  "timestamp": "2026-05-14T07:59:39.316Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：9-seed 全量复现 pilot 模式，embedding 和 dataflow 各自角色均统计显著，机制故事完整成立 核心假设：['embedding > random 在两个编码器上均 95% CI 不含零', 'dataflow > random 在 Qwen（饱和空间）上 95% CI 不含零，St…",
  "leafUuid": "b61f4914-1d83-400b-ab31-cd37ea11e0e2",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Detailed experimental predictions and mechanistic rationales",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889"
}
```

---

### Assistant

_source line 9 · 2026-05-14T07:59:59.629Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for all "planned" experiments in the experiment_plan, under the "best" tier definition they've provided. Let me carefully go through each planned experiment and generate predictions consistent with the best-case scenario.

Let me identify all planned experiments:
- plan_003: SWE-bench Lite end-to-end evaluation (planned)
- plan_004: RepoBench-R cross-file retrieval (planned)
- plan_005: Embedding vs random depth analysis (planned)
- plan_007: Ablation: 1-hop vs 2-hop vs 3-hop (planned)


- plan_008: Ablation: training data size scaling (planned)
- plan_009: Ablation: fusion head (planned)
- plan_010: Ablation: dataflow-distance weighted negatives (planned)
- plan_011: Failure analysis (planned)
- plan_012: Qualitative examples (planned)
- plan_014: Temperature ablation (planned)
- plan_015: Dynamic embedding mining baseline (planned)
- plan_016: Bootstrap CI for SWE-bench Lite (planned)
- plan_017: Inference-time graph method comparison (planned)

Now I need to understand what the "best" tier means to properly generate predictions that align with that definition.

Looking at the 9-seed reproduction results, both embedding and dataflow components show statistical significance, and the mechanism story holds together. I'm examining the expected ranges from the running experiments to calibrate my predictions for the planned ablations—the embedding gains look stronger for Qwen than StarCoder, while dataflow contributions are more modest and potentially negative for StarCoder.

Now I'm compiling the metric ranges for the full runs and working through the bootstrap significance estimates. I need to extrapolate from the pilot results where Qwen showed consistent embedding benefits but StarCoder's gains were smaller, then construct detailed predictions with rationales for each outcome.

Generating YAML predictions...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b61f4914-1d83-400b-ab31-cd37ea11e0e2",
  "isSidechain": false,
  "requestId": "req_011Cb27DPXMbYPP8wUqdD9io",
  "type": "assistant",
  "uuid": "8db458b1-abb0-40b3-b8f5-6a6b37ed2704",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUpvZLyouksaPLxM77Rys6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17501,
      "cache_read_input_tokens": 11447,
      "output_tokens": 11756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11756,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 17501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17501
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

_source line 10 · 2026-05-14T08:03:33.239Z_

```yaml
tier: best
narrative_guidance: >
  9-seed 全量复现完全确认 pilot 模式。Embedding mining 在两个编码器上均显著优于 random（bootstrap 95% CI 不含零），
  dataflow 在 Qwen 上提供条件性额外收益而在 StarCoder 上无显著差异，产生干净的交互效应。
  SWE-bench 下游验证显示可观测的 resolve rate 提升。机制故事（表征饱和度 → 策略有效性）通过 neg_difficulty margin、
  温度消融、动态挖掘对照三条证据线完整闭合。论文三条 claim 均有充分统计支撑，EMNLP Main 定位清晰。

imagined_experiments:

  - name: "SWE-bench Lite End-to-End Evaluation"
    plan_id: "plan_003"
    description: "3 strategies × best checkpoint on SWE-bench Lite (300), Qwen3.6-27B agent, 测 resolve rate"
    expected_results:
      random_resolve_rate: 0.227
      embedding_distance_resolve_rate: 0.250
      dataflow_aware_resolve_rate: 0.260
      embed_vs_random_delta_pp: 2.3
      dataflow_vs_random_delta_pp: 3.3
      dataflow_vs_embed_delta_pp: 1.0
      total_instances: 300
      instances_resolved_random: 68
      instances_resolved_embed: 75
      instances_resolved_dataflow: 78
      retrieval_recall1_random: 0.533
      retrieval_recall1_embed: 0.556
      retrieval_recall1_dataflow: 0.548
    result_rationale: >
      best 档下 retrieval 质量提升能传导到下游 resolve rate。Qwen best checkpoint embedding R@1≈0.556 vs random 0.533，
      差值 2.3pp 在 300 实例上对应约 7 个额外正确 retrieval → 其中部分转化为 resolve。
      转化率不是 1:1（retrieval 改善不等于 repair 改善，LLM agent 有自身能力上限），
      但 best 档假设转化效率约 30-40%，即 ~7 个额外正确 retrieval 中约 2-3 个转为 resolve。
      Dataflow 在 Qwen 上的条件性收益（pilot +0.8pp R@1）进一步贡献约 1pp resolve delta。
      总体 swebench_resolve_delta_pp 落在 [2.0, 5.0] 范围的中低段，
      因为 retrieval → repair 的衰减是系统性的。SWE-bench Lite 300 实例规模下，
      2-3pp 差异虽小但在 best 档下 bootstrap CI 可检测。
    tables:
      - caption: "SWE-bench Lite Resolve Rate by Retrieval Strategy"
        columns: [Strategy, Resolve_Rate, Delta_vs_Random, Instances_Resolved]
        rows:
          - [random, "22.7%", "—", 68]
          - [embedding_distance, "25.0%", "+2.3pp", 75]
          - [dataflow_aware, "26.0%", "+3.3pp", 78]
    figures_description:
      - "Bar chart: resolve rate × strategy, error bars from bootstrap resampling"
      - "Venn diagram: 3 strategies 各自独立解决的 instances 重叠情况，突出 dataflow-unique solves"
    analysis: >
      Resolve rate 提升确认 retrieval 质量改善能传导到实际软件工程任务。Dataflow 策略独立解决了 5 个
      random/embed 均失败的 instance（多为跨文件 dataflow 依赖），支持 Claim 2 的条件性收益叙事。
      Embed 策略独立解决 3 个（多为同文件内近义函数混淆），支持 Claim 1。

  - name: "RepoBench-R Cross-File Retrieval Evaluation"
    plan_id: "plan_004"
    description: "3 strategies × best checkpoint on RepoBench-R, retrieval-only evaluation"
    expected_results:
      random_recall1: 0.412
      embedding_distance_recall1: 0.431
      dataflow_aware_recall1: 0.438
      random_mrr: 0.508
      embedding_distance_mrr: 0.529
      dataflow_aware_mrr: 0.534
      embed_vs_random_R1_delta_pp: 1.9
      dataflow_vs_random_R1_delta_pp: 2.6
      total_queries: 1200
    result_rationale: >
      RepoBench-R 是 cross-file retrieval benchmark，天然偏向有结构依赖的查询（import/call 关系）。
      在 best 档下，embedding 改善幅度与 SWE-smith 内部 eval 一致（~2pp），
      dataflow 的额外收益在此 benchmark 上可能略大于 SWE-smith（因 RepoBench-R 的 cross-file
      性质与 dataflow connectivity 天然对齐），但差异不会很大因为训练数据来自 SWE-smith 而非 RepoBench，
      存在 domain gap。整体 R@1 低于 SWE-smith 内部 eval（0.41 vs 0.53），
      因为 pool size 和 query 分布不同。关键是方向一致且差异可检测。
    tables:
      - caption: "RepoBench-R Retrieval Performance"
        columns: [Strategy, "R@1", "R@5", "R@10", MRR]
        rows:
          - [random, 0.412, 0.687, 0.793, 0.508]
          - [embedding_distance, 0.431, 0.704, 0.808, 0.529]
          - [dataflow_aware, 0.438, 0.711, 0.812, 0.534]
    figures_description:
      - "Grouped bar chart: R@1, R@5, R@10 × strategy on RepoBench-R"
    analysis: >
      第二 benchmark 确认 SWE-smith 上的发现不是 benchmark-specific artifact。
      策略排序一致（dataflow ≥ embed > random），增强论文的 external validity。

  - name: "Embedding vs Random Stratified Analysis"
    plan_id: "plan_005"
    description: "按 repo size/complexity 分层，分析 embedding negatives 的收益分布"
    expected_results:
      small_repo_lt50_embed_delta_pp: 0.8
      medium_repo_50_200_embed_delta_pp: 2.1
      large_repo_200_500_embed_delta_pp: 2.8
      xlarge_repo_500plus_embed_delta_pp: 1.5
      high_complexity_embed_delta_pp: 2.9
      low_complexity_embed_delta_pp: 1.2
      correlation_repo_size_vs_delta: 0.31
      correlation_complexity_vs_delta: 0.42
    result_rationale: >
      best 档下 embedding mining 普遍有效但收益分布不均。中大型 repo（50-500 files）收益最大，
      因为 pool 中有足够多的 near-miss 候选（lexically similar but not gold），
      embedding mining 能有效挑选最有信息量的 hard negatives。小型 repo pool 太小、
      embedding mining 退化为近似 random；超大型 repo 结构复杂度使得 embedding distance
      与 relevance 的相关性下降（太多 "远但相关" 的文件）。Complexity（cyclomatic complexity 或
      import depth）比 size 更好地预测 embedding mining 收益，
      因为高复杂度代码中相似但无关的文件更多。
    tables:
      - caption: "Embedding Mining Benefit by Repo Tier"
        columns: [Tier, N_Instances, Embed_R1, Random_R1, Delta_pp]
        rows:
          - [small (<50), 500, 0.568, 0.560, "+0.8"]
          - [medium (50-200), 4096, 0.551, 0.530, "+2.1"]
          - [large (200-500), 13628, 0.542, 0.514, "+2.8"]
          - [xlarge (500+), 25949, 0.528, 0.513, "+1.5"]
    figures_description:
      - "Scatter plot: repo complexity vs embed-random delta, with regression line"
      - "Box plot: delta distribution by repo size tier"
    analysis: >
      收益分布分析提供 practical guidance：embedding mining 对中大型项目最有效，
      与表征空间中 near-miss 候选密度的直觉一致。复杂度比 size 更具预测力，
      提示 negative mining 策略选择应考虑代码结构特征而非简单规模。

  - name: "Hop Distance Ablation"
    plan_id: "plan_007"
    description: "1-hop vs 2-hop vs 3-hop call-graph bounding for dataflow extraction"
    expected_results:
      hop1_connected_rate: 0.12
      hop2_connected_rate: 0.34
      hop3_connected_rate: 0.58
      hop1_z_pct: 0.18
      hop2_z_pct: 0.41
      hop3_z_pct: 0.62
      hop2_qwen_R1: 0.548
      hop1_qwen_R1: 0.541
      hop3_qwen_R1: 0.544
      hop2_extraction_time_s: 8.9
      hop3_extraction_time_s: 23.4
    result_rationale: >
      2-hop 是 sweet spot。1-hop 太严格：大多数 repo 中直接 dataflow 连接的文件对稀少（12%），
      导致 connected-not-gold set 太小，dataflow negative mining 退化为近似 random。
      3-hop 太宽松：58% 的文件对被标记为 connected，negative pool 被过度稀释，
      且提取时间增长 2.6x（路径爆炸）。2-hop（当前默认）在 coverage（34%）和
      selectivity（Z=41%）之间取得平衡，R@1 最高。这一结果支持 Claim 3 中的
      "scope-bounded" 设计选择。
    tables:
      - caption: "Hop Distance Impact on Extraction and Training"
        columns: [Hops, Connected_Rate, Z_Pct, Extraction_Time_s, Qwen_R1]
        rows:
          - [1, "12%", "18%", 4.2, 0.541]
          - [2, "34%", "41%", 8.9, 0.548]
          - [3, "58%", "62%", 23.4, 0.544]
    figures_description:
      - "Line chart: R@1 vs hop distance, with extraction time on secondary y-axis"
    analysis: >
      2-hop 最优确认了设计选择的合理性。3-hop 的 R@1 回落说明过度扩展 connectivity
      范围会引入噪声连接，削弱 structural negative 的信息量。

  - name: "Training Data Size Scaling"
    plan_id: "plan_008"
    description: "1K vs 3K vs 5K training instances, 测 strategy 收益是否随数据量变化"
    expected_results:
      1k_random_R1: 0.498
      1k_embed_R1: 0.521
      1k_dataflow_R1: 0.518
      3k_random_R1: 0.525
      3k_embed_R1: 0.548
      3k_dataflow_R1: 0.543
      5k_random_R1: 0.533
      5k_embed_R1: 0.556
      5k_dataflow_R1: 0.548
      embed_delta_1k: 2.3
      embed_delta_3k: 2.3
      embed_delta_5k: 2.3
      dataflow_delta_1k: 2.0
      dataflow_delta_3k: 1.8
      dataflow_delta_5k: 1.5
    result_rationale: >
      best 档下 embedding mining 的收益对数据量 robust（~2.3pp 几乎不变），
      因为 embedding distance 提供的信息增益是 strategy-intrinsic 的，不依赖数据量。
      Dataflow 收益随数据量增加略有递减（2.0→1.5pp），因为更多数据使 random baseline
      也能隐式覆盖部分结构相关的 hard negatives（大数定律），缩小了 dataflow 的
      marginal 贡献。但即使在 5K 下，dataflow 在 Qwen 上的条件性收益仍然存在。
      绝对性能随数据量单调增长但边际递减（符合 neural scaling 预期）。
    tables:
      - caption: "Strategy Benefit by Training Data Size"
        columns: [Size, Random_R1, Embed_R1, Embed_Delta, Dataflow_R1, DF_Delta]
        rows:
          - [1K, 0.498, 0.521, "+2.3", 0.518, "+2.0"]
          - [3K, 0.525, 0.548, "+2.3", 0.543, "+1.8"]
          - [5K, 0.533, 0.556, "+2.3", 0.548, "+1.5"]
    figures_description:
      - "Line chart: R@1 vs data size, 3 lines for 3 strategies, showing parallel scaling for embed and convergence for dataflow"
    analysis: >
      Embedding mining 收益的 scale-invariance 强化 Claim 1（普遍有效）。
      Dataflow 收益的轻微递减可解释为 "structural signal 被 larger random samples 部分替代"，
      但不消失——支持 Claim 2 的 "conditional benefit" 定位。

  - name: "Fusion Head Ablation"
    plan_id: "plan_009"
    description: "Embedding-only vs structural-features-only vs combined fusion head"
    expected_results:
      embed_only_R1: 0.556
      structural_only_R1: 0.487
      combined_R1: 0.549
      embed_only_vs_combined_delta: 0.7
    result_rationale: >
      best 档下的核心发现是 embedding-only 已经很强（因为我们的方法是 training-time mining
      而非 inference-time fusion）。Structural-features-only 单独很弱（R@1=0.487，
      低于 random baseline 的 0.533），说明结构信息不能替代语义相似度，只能补充。
      Combined fusion head 反而比 embed-only 略低（0.549 vs 0.556），因为加入 structural
      features 作为 inference-time signal 引入噪声（CodeQL extraction 覆盖率仅 34%，
      inference 时 missing features 是常态）。这一结果强化论文叙事：结构信息的价值在于
      training-time negative mining（改善表征学习），而非 inference-time feature。
    tables:
      - caption: "Fusion Head Comparison (Qwen, best checkpoint)"
        columns: [Head, "R@1", "R@5", Note]
        rows:
          - [embed_only, 0.556, 0.961, "Our default"]
          - [structural_only, 0.487, 0.872, "Below random baseline"]
          - [combined, 0.549, 0.958, "Marginal degradation vs embed_only"]
    figures_description:
      - "Bar chart: R@1 by fusion head type"
    analysis: >
      Ablation 清晰区分了 structural information 的两种使用方式：training-time mining（有效）
      vs inference-time feature（无效或有害）。这是对 inference-time graph methods
      （CodexGraph, LocAgent）的重要区分点，支持 plan_017 的讨论。

  - name: "Dataflow-Distance Weighted Negatives"
    plan_id: "plan_010"
    description: "Binary connected/disconnected vs dataflow-distance weighted negative sampling"
    expected_results:
      binary_qwen_R1: 0.548
      weighted_qwen_R1: 0.551
      binary_starcoder_R1: 0.489
      weighted_starcoder_R1: 0.490
      weighted_vs_binary_qwen_delta: 0.3
      weighted_vs_binary_starcoder_delta: 0.1
    result_rationale: >
      Distance-weighted sampling 对 Qwen 有微弱额外收益（+0.3pp），因为在饱和空间中
      更细粒度的 difficulty gradation 提供略好的 curriculum 效果——离 gold 越远的
      disconnected file 越 "easy"，给予更低采样权重，让训练集中在 hard disconnected 上。
      但差异很小因为 binary 已经是一个合理的 proxy（connected vs disconnected 的
      distinction 捕获了主要信号）。StarCoder 上差异可忽略，与 Claim 2 一致——
      dataflow 信号在非饱和空间中 marginal，更细的 granularity 自然也 marginal。
      总体结论：binary 足够，weighted 是 diminishing return。
    tables:
      - caption: "Binary vs Weighted Dataflow Negatives"
        columns: [Method, Qwen_R1, StarCoder_R1]
        rows:
          - [binary (default), 0.548, 0.489]
          - [distance-weighted, 0.551, 0.490]
    figures_description:
      - "Histogram: negative difficulty distribution under binary vs weighted sampling"
    analysis: >
      Binary 简单且接近最优，weighted 的微弱改善不足以 justify 额外复杂度。
      这一 negative result 反而简化了方法描述——"disconnected = hard negative" 无需更复杂的定义。

  - name: "SWE-bench Failure Analysis"
    plan_id: "plan_011"
    description: "50 个 SweRank/BM25 failures，按 dataflow 是否 help 分类"
    expected_results:
      total_failures_analyzed: 50
      dataflow_helps_count: 18
      dataflow_helps_pct: 36
      failure_categories:
        cross_file_dependency: 14
        same_file_semantic: 12
        missing_context: 10
        llm_reasoning_failure: 8
        other: 6
      dataflow_helps_by_category:
        cross_file_dependency: 11
        same_file_semantic: 3
        missing_context: 3
        llm_reasoning_failure: 1
        other: 0
    result_rationale: >
      36% 的 BM25/SweRank failure 中 dataflow mining 能提供帮助——这些 case 主要是
      cross-file dependency 类型（gold file 与 query file 有 dataflow 连接但 lexical
      similarity 低）。这个比例与 Z%=41%（connected-not-gold rate）高度一致：
      如果 ~40% 的 instances 有 structural signal 可利用，那么在 failures 中
      dataflow helps 的比例也应在类似量级。Same-file semantic failures 中 dataflow
      偶尔帮助（因为相同文件内的函数调用也被 dataflow graph 捕获），但这不是主要机制。
      LLM reasoning failures 与 retrieval 无关，dataflow 自然无法帮助。
    tables:
      - caption: "Failure Analysis: Where Dataflow Helps"
        columns: [Category, Count, DF_Helps, DF_Help_Rate]
        rows:
          - [cross_file_dependency, 14, 11, "79%"]
          - [same_file_semantic, 12, 3, "25%"]
          - [missing_context, 10, 3, "30%"]
          - [llm_reasoning_failure, 8, 1, "12%"]
          - [other, 6, 0, "0%"]
    figures_description:
      - "Stacked bar chart: failure categories with dataflow-helps overlay"
      - "3 representative case studies with retrieval ranking diff"
    analysis: >
      Dataflow 最大价值在 cross-file dependency failures（79% help rate），
      精确对齐了 Claim 2 的 "structural dimension the encoder cannot separate via text alone" 叙事。

  - name: "Qualitative Case Studies"
    plan_id: "plan_012"
    description: "5-10 个 structural negatives 改变 retrieval outcome 的代表性 case"
    expected_results:
      total_cases: 8
      categories:
        import_chain_recovery: 3
        utility_vs_core_disambiguation: 2
        test_file_suppression: 2
        config_dependency_detection: 1
    result_rationale: >
      best 档下可以找到 8 个 clean case studies，覆盖四种典型模式。
      Import chain recovery 最多（3 个），因为这是 dataflow connectivity 最直接的信号类型：
      gold file 通过 import chain 与 query file 连接，但 lexical similarity 很低（不同功能模块），
      random/embed mining 无法区分 "lexically similar but structurally irrelevant" negatives。
      Utility vs core disambiguation（2 个）展示 dataflow 如何将 utils.py 类文件正确
      判断为 connected（有 dataflow 到 core 的数据流）而非 false negative。
      Test file suppression（2 个）展示 test files 虽 lexically similar 但 dataflow
      disconnected，被正确降权。
    tables: []
    figures_description:
      - "Figure: 4-panel case study，每 panel 展示 query、gold、top-3 retrieval（random vs dataflow），附 dataflow graph 子图"
    analysis: >
      Case studies 提供 mechanistic evidence 的具体实例化，让 reviewer 直观理解
      "structural dimension" 到底意味着什么。选择覆盖四种不同模式以展示 generality。

  - name: "Temperature Ablation"
    plan_id: "plan_014"
    description: "τ ∈ {0.05, 0.1, 0.2} × 3 strategies × Qwen, 测 regime-specificity"
    expected_results:
      tau_005:
        random_R1: 0.518
        embed_R1: 0.542
        dataflow_R1: 0.539
        embed_delta: 2.4
        dataflow_delta: 2.1
      tau_010:
        random_R1: 0.533
        embed_R1: 0.556
        dataflow_R1: 0.548
        embed_delta: 2.3
        dataflow_delta: 1.5
      tau_020:
        random_R1: 0.521
        embed_R1: 0.539
        dataflow_R1: 0.530
        embed_delta: 1.8
        dataflow_delta: 0.9
      optimal_tau: 0.10
      embed_benefit_robust_across_tau: true
      dataflow_benefit_strongest_at_low_tau: true
    result_rationale: >
      best 档下 embedding mining 在所有 τ 值下均有正收益（1.8-2.4pp），确认 Claim 1 的
      robustness。τ=0.1 是 sweet spot（pilot 已用的值），R@1 最高。τ=0.05 过低导致
      contrastive loss landscape 太 sharp，所有 strategy 绝对性能下降但 relative ranking 不变。
      τ=0.2 过高使 loss 过于平滑，strategy 差异缩小。Dataflow 收益随 τ 增大而递减
      （2.1→1.5→0.9pp），因为高温度下 contrastive loss 对 hard vs easy negatives 的
      区分度降低，structural difficulty gradient 被稀释。这一发现提供了 mechanistic insight：
      dataflow 的 value proposition 是提供更 hard 的 negatives，
      而 temperature 控制了 model 对 hardness 的敏感度。
    tables:
      - caption: "Temperature × Strategy Interaction (Qwen)"
        columns: [τ, Random_R1, Embed_R1, Embed_Δ, DF_R1, DF_Δ]
        rows:
          - [0.05, 0.518, 0.542, "+2.4", 0.539, "+2.1"]
          - [0.10, 0.533, 0.556, "+2.3", 0.548, "+1.5"]
          - [0.20, 0.521, 0.539, "+1.8", 0.530, "+0.9"]
    figures_description:
      - "Line chart: R@1 vs τ, 3 strategy lines, 显示 strategy gap 随 τ 变化"
      - "Heatmap: τ × strategy interaction strength (delta from random)"
    analysis: >
      Temperature 消融排除了 "finding is τ-specific" 的 reviewer concern。
      Embedding benefit 对 τ robust；dataflow benefit 在低 τ 下最强，
      提供 practitioner guidance（如果 encoder 空间饱和 + 低温度 → dataflow 最有价值）。

  - name: "Dynamic Embedding Mining Baseline"
    plan_id: "plan_015"
    description: "每 epoch 重新 mine embedding negatives vs 静态一次性 mine，隔离 selection criterion 和 curriculum shift"
    expected_results:
      static_embed_R1: 0.556
      dynamic_embed_R1: 0.561
      dynamic_vs_static_delta: 0.5
      dynamic_dataflow_R1: 0.552
      static_dataflow_R1: 0.548
      dynamic_training_time_multiplier: 2.8
    result_rationale: >
      Dynamic mining 提供微弱改善（+0.5pp），因为随训练进行 encoder representation 会 drift，
      重新 mine 能保持 negatives 的 hardness。但差异很小（<1pp），说明 static mining
      在 3 epoch 短训练中 drift 不严重——pretrained encoder 的 representation 在
      LoRA fine-tune 中变化有限（LoRA rank=16，参数量仅为全量的 0.3%）。
      关键发现：static vs dynamic 的差异远小于 strategy 差异（embed vs random = 2.3pp
      vs dynamic vs static = 0.5pp），确认 selection criterion（embedding distance vs random）
      是 primary driver，而非 curriculum shift。这排除了 "embed helps only because
      of implicit curriculum" 的 alternative explanation。
      Dynamic 的 2.8x 训练时间开销使其不实用。
    tables:
      - caption: "Static vs Dynamic Mining"
        columns: [Mining, Strategy, R1, Training_Time_h]
        rows:
          - [static, embedding, 0.556, 3.2]
          - [dynamic, embedding, 0.561, 9.0]
          - [static, dataflow, 0.548, 3.2]
          - [dynamic, dataflow, 0.552, 9.0]
    figures_description:
      - "Bar chart: static vs dynamic × strategy, with training time annotation"
    analysis: >
      Static mining 在成本效益上远优于 dynamic。更重要的是，排除了 curriculum confound：
      embedding mining 的收益来自 selection criterion 本身（挑到 truly hard negatives），
      而非 training dynamics。

  - name: "Bootstrap CI for SWE-bench Lite"
    plan_id: "plan_016"
    description: "9-seed × 3 strategies 的 bootstrap 95% CI for resolve rate"
    expected_results:
      random_resolve_mean: 0.227
      random_resolve_ci: [0.195, 0.259]
      embed_resolve_mean: 0.250
      embed_resolve_ci: [0.218, 0.282]
      dataflow_resolve_mean: 0.260
      dataflow_resolve_ci: [0.226, 0.294]
      embed_vs_random_delta_mean: 2.3
      embed_vs_random_delta_ci: [0.4, 4.2]
      embed_vs_random_p_value: 0.012
      dataflow_vs_random_delta_ci: [0.5, 5.8]
      dataflow_vs_random_p_value: 0.008
      bootstrap_iterations: 10000
    result_rationale: >
      300 instances × 9 seeds 提供足够的 bootstrap 统计量力。best 档下 embed_vs_random
      的 95% CI 不含零（[0.4, 4.2]pp），p=0.012，通过显著性检验。
      CI 宽度 ~4pp 反映 SWE-bench 300 的固有 variance（每个 instance 是 binary outcome，
      binomial variance 较大）。9 seeds 降低了 training variance 的贡献，
      但 evaluation set size（300）是 CI 宽度的主要 bottleneck。
      Cross-seed R@1 标准差 ~1.0pp（在 [0.5, 1.5] 范围内），
      确认 training 方差可控。Dataflow CI 也不含零但上界更宽（[0.5, 5.8]），
      反映条件性收益的 inherent higher variance。
    tables:
      - caption: "Bootstrap 95% CI for SWE-bench Lite Resolve Rate"
        columns: [Comparison, Delta_pp, "95% CI", p_value, Significant]
        rows:
          - [embed vs random, "+2.3", "[0.4, 4.2]", 0.012, "Yes"]
          - [dataflow vs random, "+3.3", "[0.5, 5.8]", 0.008, "Yes"]
          - [dataflow vs embed, "+1.0", "[-0.8, 2.8]", 0.134, "No"]
    figures_description:
      - "Forest plot: pairwise strategy comparisons with bootstrap CIs"
      - "Violin plot: per-seed resolve rates by strategy"
    analysis: >
      Embed vs random 和 dataflow vs random 均显著，但 dataflow vs embed 不显著
      （CI 含零）。这精确对应 Claim 2 的 "conditional" 定位——dataflow 相对 random 有显著收益
      但相对 embed 的 incremental 在 300 instances 上力度不足。论文可如实报告此 pattern
      并讨论 statistical power limitation。

  - name: "Inference-Time Graph Method Comparison Discussion"
    plan_id: "plan_017"
    description: "与 CodexGraph, LocAgent 等 inference-time graph methods 的概念对比与定位"
    expected_results:
      comparison_dimensions: 4
      structfuse_strengths: ["training-time, no inference overhead", "model-agnostic mining", "compatible with any retriever"]
      inference_methods_strengths: ["dynamic graph, adapts to query", "no precomputation needed", "can leverage runtime call stacks"]
      complementarity_score: "high"
      empirical_comparison: "not applicable (different paradigm)"
    result_rationale: >
      这是 discussion section 的概念分析而非实验。best 档下不需要实际跑 inference-time
      baselines（GPU budget=0），而是提供清晰的 taxonomy：StructFuse 是 training-time
      structural signal injection（改善表征学习），inference-time methods 是 navigation-time
      structural signal（改善检索路径）。两者 complementary 而非 competitive。
      核心区别：StructFuse 是 offline（一次 mine、反复 train），inference methods 是
      online（每次 query 重新构建 graph）。StructFuse 的 overhead 在 training 时
      已 amortize，inference 零成本；inference methods 每次 query 有额外延迟。
      但 inference methods 能适应 query-specific context（如运行时调用栈），StructFuse 不能。
    tables:
      - caption: "Training-Time vs Inference-Time Structural Methods"
        columns: [Dimension, StructFuse, CodexGraph_LocAgent]
        rows:
          - [Signal injection, "Training (negative mining)", "Inference (graph navigation)"]
          - [Inference overhead, "Zero", "Per-query graph traversal"]
          - [Graph freshness, "Static (pretrained)", "Dynamic (query-adaptive)"]
          - [Compatibility, "Any contrastive retriever", "Specific agent framework"]
    figures_description:
      - "Taxonomy figure: 2×2 matrix (training/inference × structural/textual) positioning StructFuse and related work"
    analysis: >
      清晰定位避免了 "why not compare with X" 的 reviewer 质疑。
      Complementarity framing 开启了 future work 方向（combine training-time mining + inference-time navigation）。

  - name: "M2 Full Qwen 9-Seed Results"
    plan_id: "plan_002 (full: m2_full_qwen)"
    description: "9 seeds × 3 strategies, Qwen2.5-Coder-3B, 全量 3-strategy 对比"
    expected_results:
      random_mean_R1: 0.533
      random_std_R1: 0.008
      random_seeds: [0.527, 0.530, 0.531, 0.533, 0.534, 0.535, 0.536, 0.538, 0.540]
      embedding_mean_R1: 0.556
      embedding_std_R1: 0.009
      embedding_seeds: [0.547, 0.550, 0.553, 0.555, 0.556, 0.558, 0.559, 0.561, 0.564]
      dataflow_mean_R1: 0.548
      dataflow_std_R1: 0.010
      dataflow_seeds: [0.538, 0.541, 0.544, 0.547, 0.548, 0.550, 0.552, 0.555, 0.558]
      embed_vs_random_delta_pp: 2.3
      dataflow_vs_random_delta_pp: 1.5
      dataflow_vs_embed_delta_pp: -0.8
      embed_vs_random_bootstrap_p: 0.003
      dataflow_vs_random_bootstrap_p: 0.018
      cross_seed_R1_std_max: 1.0
      best_checkpoint_step: 1000
      step_1000_overfitting: "controlled via early stopping at step 500-1000"
    result_rationale: >
      Pilot 数据（单 seed）显示 random=0.5357, embed=0.5557, dataflow=0.5436。
      best 档下 9-seed 平均值保持一致趋势但因 seed variance 略有修正。
      Qwen pos_sim=0.9855 的饱和空间使 random negatives 太 easy（margin=0.074），
      embedding mining 有效因为挑选 harder negatives（margin=0.017）。
      Dataflow 的条件性收益（+1.5pp vs random）通过更 hard 的 structural negatives
      进一步压缩 margin（margin=0.029），但 incremental 小于 embed 因为 embedding distance
      已经捕获了大部分 difficulty gradient。Cross-seed std ~0.8-1.0pp，
      在 [0.5, 1.5] 范围内，说明 training 方差可控。Step 1000 过拟合通过 early stopping
      at best validation loss 解决，不影响结论。
    tables:
      - caption: "M2 Full Qwen: 9-Seed Summary"
        columns: [Strategy, Mean_R1, Std_R1, "95% CI", Best_Step]
        rows:
          - [random, 0.533, 0.008, "[0.527, 0.539]", 1000]
          - [embedding_distance, 0.556, 0.009, "[0.549, 0.563]", 1000]
          - [dataflow_aware, 0.548, 0.010, "[0.540, 0.556]", "500-1000"]
    figures_description:
      - "Box plot: per-seed R@1 by strategy, 9 points each"
      - "Learning curve: val_loss vs step, 3 strategies × 9 seeds (band plot)"
    analysis: >
      9-seed 全量结果是论文的 primary evidence for Claims 1 & 2。
      Embedding > random 的 p=0.003 提供强统计支持。
      Dataflow > random 的 p=0.018 提供充分支持但力度略弱（higher variance），
      精确对应 "conditional benefit" 叙事。

  - name: "M2 Full StarCoder 9-Seed Results"
    plan_id: "plan_002 (full: m2_full_starcoder)"
    description: "9 seeds × 3 strategies, StarCoder2-3B, 全量交互效应验证"
    expected_results:
      random_mean_R1: 0.490
      random_std_R1: 0.009
      embedding_mean_R1: 0.507
      embedding_std_R1: 0.010
      dataflow_mean_R1: 0.488
      dataflow_std_R1: 0.011
      embed_vs_random_delta_pp: 1.7
      dataflow_vs_random_delta_pp: -0.2
      embed_vs_random_bootstrap_p: 0.008
      dataflow_vs_random_bootstrap_p: 0.62
      cross_seed_R1_std_max: 1.1
    result_rationale: >
      StarCoder pos_sim=0.7985（健康空间），random negatives 已提供足够 difficulty gradient
      （margin=0.194）。Embedding mining 仍然有效（+1.7pp, p=0.008），因为 embedding distance
      选择的 negatives 更 informative regardless of space geometry——这是 Claim 1 的关键证据
      （两个编码器均显著）。Dataflow 在 StarCoder 上无显著差异（-0.2pp, p=0.62），
      产生干净的交互效应：dataflow 的 structural negatives 在非饱和空间中不提供
      beyond-embedding 的信息增量，因为 encoder 已能通过 text alone 区分结构上不同的文件。
      这一 null result 是论文 mechanistic story 的关键支撑——
      不是所有方法在所有条件下都有效，而是有清晰的条件边界。
    tables:
      - caption: "M2 Full StarCoder: 9-Seed Summary"
        columns: [Strategy, Mean_R1, Std_R1, "95% CI", p_vs_random]
        rows:
          - [random, 0.490, 0.009, "[0.483, 0.497]", "—"]
          - [embedding_distance, 0.507, 0.010, "[0.499, 0.515]", 0.008]
          - [dataflow_aware, 0.488, 0.011, "[0.479, 0.497]", 0.62]
    figures_description:
      - "Interaction plot: encoder × strategy, 显示 Qwen 和 StarCoder 的 dataflow 交互效应"
    analysis: >
      StarCoder 的 clean null result for dataflow 是论文 strongest mechanistic evidence。
      两编码器的交互效应 pattern（embed always helps, dataflow conditional on saturation）
      完美对应表征空间几何学解释。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8db458b1-abb0-40b3-b8f5-6a6b37ed2704",
  "isSidechain": false,
  "requestId": "req_011Cb27DPXMbYPP8wUqdD9io",
  "type": "assistant",
  "uuid": "cb1882ac-0338-4fc6-9235-2774502b5c67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WUpvZLyouksaPLxM77Rys6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17501,
      "cache_read_input_tokens": 11447,
      "output_tokens": 11756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17501,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11756,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 17501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17501
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：9-seed 全量复现 pilot 模式，embedding 和 dataflow 各自角色均统计显著，机制故事完整成立 核心假设：['embedding > random 在两个编码器上均 95% CI 不含零', 'dataflow > random 在 Qwen（饱和空间）上 95% CI 不含零，St…",
  "leafUuid": "cb1882ac-0338-4fc6-9235-2774502b5c67",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Detailed experimental predictions and mechanistic rationales",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：9-seed 全量复现 pilot 模式，embedding 和 dataflow 各自角色均统计显著，机制故事完整成立 核心假设：['embedding > random 在两个编码器上均 95% CI 不含零', 'dataflow > random 在 Qwen（饱和空间）上 95% CI 不含零，St…",
  "leafUuid": "cb1882ac-0338-4fc6-9235-2774502b5c67",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Detailed experimental predictions and mechanistic rationales",
  "sessionId": "6a3cffa0-8c8e-4873-b7ac-309c623b0889"
}
```

---
