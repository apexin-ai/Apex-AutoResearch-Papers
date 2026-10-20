# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：embedding benefit 可复现但效果量缩水或统计边缘，dataflow 交互效应方向正确但不显著，缺下游验证 核心假设：['embedd

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/23dadbc4-6387-4095-a1b3-026856e76048.jsonl`
- **Structured JSON:** [`c319e9c4503eb63ae2d8.json`](../../sessions/c3/c319e9c4503eb63ae2d8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T08:03:35.746Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T08:03:35.746Z",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：embedding benefit 可复现但效果量缩水或统计边缘，dataflow 交互效应方向正确但不显著，缺下游验证\n核心假设：['embedding > random 方向一致但至少一个编码器 95% CI 包含零（如 StarCoder Δ 缩至 +0.5–1.0pp）', 'dataflow > random 在 Qwen 上方向正确但 CI 包含零（Δ ~+0.3–0.8pp）', '种子间方差较大（R@1 标准差 1.5–3.0pp），削弱统计力度', 'SWE-bench 未完成或 Δ ≤ 1pp（无法宣称下游收益）', 'representation saturation 故事定性成立，但 n=2 编码器不足以做强因果推断']\n关键指标范围：{'qwen_embed_vs_random_R1_pp': [0.5, 1.5], 'starcoder_embed_vs_random_R1_pp': [0.0, 1.0], 'qwen_dataflow_vs_random_R1_pp': [0.0, 0.8], 'starcoder_dataflow_vs_random_R1_pp': [-1.5, 0.0], 'best_qwen_mean_R1': [0.52, 0.55], 'best_starcoder_mean_R1': [0.44, 0.48], 'swebench_resolve_delta_pp': [-0.5, 1.0], 'embed_benefit_bootstrap_p': [0.05, 0.2], 'cross_seed_R1_std': [1.5, 3.0]}\n叙事方向：Claim 1 降级为 \"directional evidence correcting misconception\"——embedding mining 不会 harm（纠正 CoCoHaNeRe），但绝对增益需要更多编码器验证。Claim 2 从 \"conditional benefit\" 降级为 \"exploratory observation\"——saturation 机制作为 hypothesis 提出，neg_difficulty 分析作为 supporting evidence 而非 proof。删除 \"consistently improves\" 措辞，替换为 \"tends to improve\"。 补充 temperature ablation（plan_014）证明发现非 regime-specific。论文重心从 \"three claims\" 转为 \"systematic methodology + preliminary mechanistic hypothesis\"，强调方法论贡献 （controlled comparison framework）而非效果量。仍投 EMNLP Main，定位为 analysis paper。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: structfuse-context\nfocus: D024 重写后的新 framing：论文从 \"method paper (dataflow > all)\" 转为 \"systematic analysis + mechanistic insight\"。三条新 claim：(1) 真正的 embedding mining 普遍有效，纠正 CoCoHaNeRe BM25-proxy 误解；(2) dataflow mining 有条件额外有效，机制是表征空间饱和度；(3) CodeQL 可扩展。已有实证：Qwen R@1=55.3%, StarCoder R@1=45.4%, neg_difficulty margin +17%/+28%, 两编码器 step 1000 过拟合。Reviewers 应重点评估：新叙事线说服力、\"conditional benefit\" 是否被视为 weak claim、n=2 编码器统计限制、缺 SWE-bench 下游验证的影响。\n\n## paper_framing.md\n\n# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **True embedding-distance hard negative mining consistently improves contrastive code retrieval over random baselines, correcting the prior misconception that embedding negatives harm performance.** The reported \"harm\" (CoCoHaNeRe-derived, -27pp R@1) was an artifact of BM25-proxy negatives mislabeled as embedding-distance — genuine embedding mining yields +1.6–2.0pp R@1 across two architecturally distinct encoders (Qwen2.5-Coder-3B, StarCoder2-3B).\n\n2. **Structure-grounded (dataflow) hard negatives provide conditional additional benefit beyond embedding mining, mediated by encoder representation saturation.** When pretrained encoder representations are compressed (pos_sim > 0.98, as in Qwen), random and embedding negatives become too easy; dataflow-disconnected negatives force discrimination along a structural dimension the encoder cannot separate via text alone. When representation space is healthy (pos_sim ~ 0.80, as in StarCoder), embedding mining alone suffices. Mechanism: neg_difficulty margin analysis (+17% Qwen, +28% StarCoder) provides quantitative evidence for this interaction.\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** 0% timeout, 78% connected-not-gold rate (Z%), 123/131 repos with output at full scale. Method is a general-purpose structural negative generator applicable beyond code (molecular networks, circuit topology, KG retrieval).\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers rely on text similarity alone, but lexical similarity ≠ structural relevance. Hard negative mining is the standard approach to improve contrastive retrievers, yet the field lacks systematic understanding of what negative selection strategies work for code and why.\n\n- **Existing approaches & gaps**:\n  - Text-based retrieval (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided at inference (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: reports embedding negatives harm code search — but uses BM25 proxy, not true embedding distance\n  - Gap: no systematic study comparing negative mining strategies with proper controls, and no mechanistic explanation for when/why each strategy works\n\n- **Our contribution**: A systematic analysis of hard negative mining strategies for contrastive code retrieval. We (1) correct the misconception that embedding negatives harm performance (BM25 proxy ≠ embedding distance), (2) introduce structure-grounded negatives via inter-procedural dataflow and characterize when they provide additional benefit, and (3) provide mechanistic explanation via representation space saturation analysis.\n\n- **Headline result template**: \"True embedding-distance mining consistently improves code retrieval (+1.6–2.0pp R@1, 2 encoders), correcting prior reports of harm. Structure-grounded (dataflow) negatives provide further conditional benefit (+0.8–2.3pp) when encoder representations are saturated, with the interaction mechanism quantified via negative difficulty analysis.\"\n\n## Core Insight\n\nThe effectiveness of hard negative mining strategies depends on the encoder's representation geometry. When the pretrained space is saturated (high pos_sim → low margin between positive and negative), the encoder needs harder negatives from an orthogonal signal dimension (structure). When the space has healthy separation, embedding-distance mining alone captures sufficient difficulty gradient. This encoder-strategy interaction explains contradictory findings in prior work.\n\n## Dual-Pillar Motivation\n\n1. **Primary — Systematic analysis correcting misconceptions**: Prior work (CoCoHaNeRe) conflated BM25-proxy negatives with true embedding-distance negatives, leading to incorrect conclusions about hard negative mining for code. Our controlled comparison isolates the effect of each strategy.\n2. **Secondary — Mechanistic explanation via representation geometry**: neg_difficulty analysis (margin distribution × strategy × encoder) provides explanatory depth beyond empirical comparison, enabling practitioners to predict which strategy suits their encoder without exhaustive experiments.\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder (drift-immune).\n\n## Title Options\n\n- Primary: \"What Makes Hard Negatives Work for Code Retrieval? A Systematic Study of Mining Strategies and Representation Geometry\"\n- Alternative: \"StructFuse: When and Why Structure-Grounded Hard Negatives Improve Contrastive Code Retrieval\"\n- Backup: \"Correcting Misconceptions in Hard Negative Mining for Code: Embedding Distance Helps, Structure Helps Conditionally\"\n\n## Venue Fit\n\n1. **EMNLP Main fit**: Empirical analysis + mechanistic insight papers are a strong EMNLP archetype (cf. \"Do Language Models...\" papers). Contribution is understanding, not just a new method.\n2. **NLP audience**: Frame as contrastive learning methodology with code as instantiation. Representation geometry analysis generalizes beyond code.\n3. **Against \"incremental\" criticism**: Paper corrects a misconception + provides mechanistic explanation + introduces new negative mining paradigm. Three contributions, not one marginal improvement.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response | Evidence |\n|---------|----------|----------|\n| Only 2 encoders — can you generalize? | n=2 is minimum for interaction claim; we frame as observation with mechanism, not universal law; cross-architecture (decoder vs encoder-decoder) strengthens it | plan_013 (done), m2_full runs |\n| Temperature regime specificity | Ablate τ ∈ {0.05, 0.1, 0.2} | plan_014 |\n| No downstream task evaluation | SWE-bench Lite end-to-end with LLM agent | plan_003 |\n| Static vs dynamic mining confound | Clarify mining is static; add dynamic baseline | plan_015 |\n| CodeQL scalability at larger scale | 0% timeout, 78% Z%, 123 repos; m1_reextract_v2 adds more | plan_006 (done) |\n| Why not compare inference-time graph methods? | Complementary: they navigate at inference, we mine at training. Discuss relationship. | plan_017 |\n| Single benchmark | Add RepoBench-R cross-file retrieval | plan_004 |\n| Statistical significance | Bootstrap 95% CI for all comparisons; full M2 = 9 seeds × 3 strategies × 2 encoders | plan_016, m2_full |\n| \"Complementary signal\" overstatement | Temper: \"conditionally beneficial\" not \"always complementary\" | Writing discipline |\n| Missing related work | RepoFusion, GRACE, GraphCodeBERT, ANCE, curriculum HN mining | Writing task |\n\n## Evidence Status\n\n### Confirmed findings (basis for claims):\n- D017: True embedding mining helps (+2.0pp Qwen, +1.6pp StarCoder) — corrects MVP BM25-proxy artifact\n- D021/neg_difficulty: Qwen pos_sim=0.9855 (saturated), StarCoder pos_sim=0.7985 (healthy); margin differential explains strategy interaction\n- m2_embed_verify (pilot): 3-strategy comparison confirms ranking (embedding > random, dataflow conditional)\n- plan_013 (StarCoder pilot): Confirms cross-encoder pattern — embedding helps both, dataflow helps Qwen only\n- plan_006: CodeQL scalability confirmed at 123-repo scale\n\n### In progress:\n- m2_full_qwen: 9 seeds × 3 strategies (seed 1 running, best R@1=55.3% at step 1000)\n- m2_full_starcoder: 9 seeds × 3 strategies (seed 1 running, R@1=45.4% at step 1000, still improving)\n- m1_reextract_v2: expanded extraction for higher coverage\n\n### Planned (priority order):\n- plan_003: SWE-bench Lite eval (biggest lever for paper strength)\n- plan_014: Temperature ablation (Dream reviewer concern)\n- plan_004: RepoBench-R second benchmark\n- plan_015: Dynamic mining baseline\n- plan_007/008/009: Additional ablations\n\n## Contingency (if full M2 results weaken claims)\n\n### All 18 runs confirm pilot pattern: Best case\n- Full statistical power, paper as framed above\n- Target: EMNLP Main\n\n### Dataflow benefit disappears even for Qwen at full scale: Pivot to 2-claim paper\n- Drop Claim 2 to analysis observation\n- Paper becomes: \"True embedding mining helps (correcting misconception) + CodeQL extraction is practical + representation geometry analysis explains prior contradictions\"\n- Still publishable: correcting misconception + mechanistic analysis is sufficient for EMNLP Main\n\n### Embedding mining also loses advantage at full scale: Major reassessment needed\n- Recheck data pipeline for bugs (full-scale data may have distribution differences)\n- If confirmed: negative result paper — \"Why Hard Negative Mining Doesn't Scale for Code Retrieval\"\n- Discuss with user before committing direction\n\n## Deprecated Claims (with reason)\n\n- ~~\"Embedding-distance hard negatives actively harm code retrieval\"~~ — FALSIFIED by D017. Original evidence (-27pp R@1) was from BM25-proxy negatives incorrectly labeled as embedding_distance in MVP. True embedding mining shows consistent improvement. Preserved here to prevent regression.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected\n    vs gold statistics'\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: m1_extraction\n  mvp_registry_id: mvp_p1_codeql_feasibility\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- id: plan_002\n  claim: 1\n  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,\n    3 seeds each, Qwen2.5-Coder-3B LoRA'\n  priority: P0\n  gpu_budget_hours: 30\n  deps:\n  - plan_001\n  registry_id: m2_embed_verify\n  mvp_registry_id: mvp_p2b_contrastive_training\n  full_registry_ids:\n  - m2_full_qwen\n  - m2_full_starcoder\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- id: plan_003\n  claim: 1\n  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best\n    checkpoint, Qwen3.6-27B agent'\n  priority: P0\n  gpu_budget_hours: 40\n  deps:\n  - plan_002\n  status: planned\n- id: plan_004\n  claim: 1\n  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no\n    LLM agent'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_002\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding\n    negatives 何时最有害'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_002\n  status: planned\n- id: plan_006\n  claim: 3\n  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,\n    connected-but-not-gold ratio by repo size'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: plan_006_scalability\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- id: plan_007\n  claim: 1\n  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  claim: 1\n  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  claim: 1\n  description: 'Ablation: fusion head (embedding-only vs structural-features-only\n    vs combined)'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  claim: 1\n  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - plan_001\n  status: planned\n- id: plan_011\n  claim: 1\n  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether\n    data-flow helps'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - plan_003\n  status: planned\n- id: plan_012\n  claim: 1\n  description: 'Qualitative examples: 5-10 cases where structural negatives changed\n    retrieval outcome'\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  status: planned\n- id: plan_013\n  claim: 1\n  description: 'Second encoder validation: repeat M2 core comparison (3 strategies,\n    1 seed) on StarCoder-3B or CodeBERT to test architecture generality'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  dream_source: 'best-R1-W1, median-R2-W5: single encoder is primary generality concern.\n    Upgraded to P0 per Reviewer — this is the #1 factor separating WA from WR.'\n  registry_id: plan_013_starcoder\n  full_registry_id: m2_full_starcoder\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- id: plan_014\n  claim: 2\n  description: 'Temperature ablation: τ ∈ {0.05, 0.1, 0.2} for all 3 strategies, test\n    regime-specificity of embedding harm'\n  priority: P1\n  gpu_budget_hours: 70\n  deps:\n  - plan_002\n  dream_source: 'median-R1-W3: τ=0.05 unusually low, finding may be regime-specific'\n  status: planned\n- id: plan_015\n  claim: 2\n  description: 'Dynamic embedding mining baseline: re-mine embedding negatives per\n    epoch vs static (mine once from pretrained). Isolate selection criterion from\n    curriculum shift.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - plan_002\n  dream_source: 'best-R1-W2, median-R1-W2: static vs dynamic mining is potential confound\n    for Claim 2'\n  status: planned\n- id: plan_016\n  claim: 1\n  description: 'Bootstrap CI for SWE-bench Lite: add 95% bootstrap confidence intervals\n    to end-to-end resolve rate evaluation'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_003\n  dream_source: 'best-R1-W3, worst-R1-W5: +2.0pp on 300 instances needs statistical\n    significance test'\n  status: planned\n- id: plan_017\n  claim: 1\n  description: 'Inference-time graph method comparison: discuss/compare with CodexGraph,\n    LocAgent — is StructFuse complementary or alternative?'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  dream_source: 'best-R2-W5: no comparison with inference-time graph methods'\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_p1_codeql_feasibility\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    timeout_rate: 0\n    repos_processed: 8\n    repos_skipped: 2\n    cg_mean_s: 29.6\n    cg_max_s: 119.8\n    df_mean_s: 43.4\n    df_max_s: 167.1\n    h2_connected_coverage: 0.014815\n    h2_disconnected_coverage: 0\n    h2_fisher_p: 6.5e-09\n    h2_gold_in_connected_ratio: 1\n    h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'\n- exp_id: mvp_p2a_linear_proxy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    df_bm25_auc: 0.78\n    bm25_only_auc: 0.476\n    auc_delta: 0.304\n    df_bm25_mrr: 0.556\n    bm25_only_mrr: 0.115\n    mrr_delta: 0.441\n    df_bm25_f1: 0.143\n    bm25_only_f1: 0.039\n    top_feature: is_connected (+2.82)\n    repos_evaluated: 3\n    note: 3 repos / 3 positive samples, directional evidence\n- exp_id: p2b-smoke-test\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke4\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke5\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke6\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-smoke8\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b-all-9runs\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_p2b_contrastive_training\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    random_s42_recall1: 0.984\n    random_s123_recall1: 0.984\n    random_s456_recall1: 0.992\n    embedding_s42_recall1: 0.874\n    random_mean_recall1: 0.987\n    runs_completed: 4\n    runs_failed: 5\n    failure_type: disk_full_torch_save\n- exp_id: mvp_p2b_contrastive_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_all\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: p2b_eval_4runs_v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_seed42:\n      recall@1: 0.9449\n      recall@5: 0.9843\n      recall@10: 0.9843\n    random_seed123:\n      recall@1: 0.9449\n      recall@5: 0.9921\n      recall@10: 0.9921\n    random_seed456:\n      recall@1: 0.9291\n      recall@5: 0.9921\n      recall@10: 0.9921\n    emb_dist_seed42:\n      recall@1: 0.6693\n      recall@5: 0.8898\n      recall@10: 0.9291\n    pool_size: 26\n    n_samples: 127\n- exp_id: p2b_5reruns\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random_s42:\n      val_loss: 0.0347\n      recall@1: 0.9843\n    random_s123:\n      val_loss: 0.0446\n      recall@1: 0.9843\n    random_s456:\n      val_loss: 0.0188\n      recall@1: 0.9921\n    emb_dist_s42:\n      val_loss: 0.1876\n      recall@1: 0.874\n    emb_dist_s123:\n      val_loss: 0.1461\n      recall@1: 0.874\n    emb_dist_s456:\n      val_loss: 0.1281\n      recall@1: 0.8819\n    dataflow_s42:\n      val_loss: 0.1878\n      recall@1: 0.874\n    dataflow_s123:\n      val_loss: 0.146\n      recall@1: 0.874\n    dataflow_s456:\n      val_loss: 0.1278\n      recall@1: 0.8819\n    runs_completed: 9\n    runs_failed: 0\n    WARNING: dataflow_aware ≈ embedding_distance to 4 decimal places across all seeds\n      — likely code bug in negative sampling\n- exp_id: p2b_dataflow_retrain\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: p2b_eval_4runs_pool50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pool_size: 50\n    n_samples: 127\n    random_s42:\n      recall@1: 0.496\n      recall@5: 0.843\n      recall@10: 0.945\n    random_s123:\n      recall@1: 0.535\n      recall@5: 0.85\n      recall@10: 0.921\n    random_s456:\n      recall@1: 0.543\n      recall@5: 0.843\n      recall@10: 0.953\n    emb_dist_s42:\n      recall@1: 0.488\n      recall@5: 0.835\n      recall@10: 0.874\n    random_mean:\n      recall@1: 0.525\n      recall@5: 0.845\n      recall@10: 0.94\n    emb_dist_vs_random_delta:\n      recall@1: -0.037\n      recall@5: -0.01\n      recall@10: -0.066\n- exp_id: d007_50repo_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances: 240\n    instances_with_extra_connected: 98\n    Z_pct: 40.8\n    avg_connected_minus_gold: 6\n    codeql_timeout_rate_pct: 4\n    by_repo_size:\n      small_lt50:\n        Z_pct: 38.6\n        avg_extra: 2.5\n      medium_50_200:\n        Z_pct: 55.7\n        avg_extra: 11.8\n      large_gt200:\n        Z_pct: 16.7\n        avg_extra: 8.8\n    decision: Z=40.8% >= 20% -> original method viable, proceed to M1\n- exp_id: m1_extraction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_instances_attempted: 44173\n    instances_skipped: 6696\n    total_instances: 50869\n    codeql_success: 15133\n    beniget_fallback: 764\n    extraction_failed: 28276\n    structural_data_rate: 0.36\n    repos_with_output: 123\n    repos_total: 131\n    repo_coverage: 0.939\n    skip_clone_failed: 5852\n    skip_checkout_failed: 836\n    skip_stale_handle: 8\n    elapsed_minutes: 837.8\n    avg_time_per_instance_s: 8.9\n    output_size_gb: 6.6\n    disk_usage_gb: 13\n    output_file: all.jsonl\n- exp_id: m2_early_pilot\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    pid: 795791\n    gpu: cuda:4\n    gpu_mem_mb: 9342\n    gpu_util_pct: 83\n    batch_size: 2\n    num_negatives: 3\n    max_seq_length: 1024\n    strategy_running: random (stuck at step 4000, epoch 3)\n    strategies_completed: 0/3\n    eval_1500:\n      val_loss: 0.5879\n      recall_at_1: 0.4693\n      recall_at_5: 0.4693\n      recall_at_10: 0.4693\n    eval_2000:\n      val_loss: 0.7089\n      recall_at_1: 0.4398\n    eval_2500:\n      val_loss: 0.6961\n      recall_at_1: 0.4291\n    eval_3000:\n      val_loss: 0.728\n      recall_at_1: 0.4104\n    eval_3500:\n      val_loss: 0.7022\n      recall_at_1: 0.4439\n    best_checkpoint: step_1500 (val_loss=0.5879, 6.2GB)\n    WARNING: recall@1=recall@5=recall@10 confirmed eval bug. Process hung after step\n      4000 (~45min no output). Overfitting after step 1500.\n    status_check_at: '2026-05-13T04:42:00Z'\n- exp_id: m2_early_pilot_v2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: m2_early_pilot_v3\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: m2_embed_verify\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    random:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4834\n      best_recall@1: 0.5357\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5978\n      final_recall@1: 0.5122\n    embedding_distance:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.4603\n      best_recall@1: 0.5557\n      best_recall@5: 0.9808\n      best_recall@10: 1\n      final_val_loss: 0.5935\n      final_recall@1: 0.5209\n    dataflow_aware:\n      status: DONE\n      best_step: 500\n      best_val_loss: 0.5602\n      best_recall@1: 0.5436\n      best_recall@5: 0.9817\n      best_recall@10: 1\n      final_val_loss: 0.6201\n      final_recall@1: 0.5287\n- exp_id: plan_013_starcoder\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    random:\n      status: DONE\n      best_val_loss: 0.5113\n      best_recall@1: 0.4922\n      best_recall@5: 0.98\n      best_recall@10: 1\n      source: /tmp/eval_random_s42.log (post-hoc eval, no in-training eval)\n    embedding_distance:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.4816\n      best_recall@1: 0.5078\n      best_recall@5: 0.9843\n      best_recall@10: 1\n      final_val_loss: 0.506\n      final_recall@1: 0.5174\n    dataflow_aware:\n      status: DONE\n      best_step: 1000\n      best_val_loss: 0.5255\n      best_recall@1: 0.4869\n      best_recall@5: 0.9695\n      best_recall@10: 1\n      final_val_loss: 0.5509\n      final_recall@1: 0.5078\n- exp_id: plan_006_scalability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    repos: 123\n    total_instances: 44173\n    structural_data_rate: 0.343\n    error_rate: 0.64\n    zero_timeout_rate: true\n    processing_time:\n      mean_s: 8.93\n      median_s: 0\n      p95_s: 31.95\n      max_s: 633.68\n      total_hours: 109.58\n    by_tier:\n      small_lt50:\n        repos: 1\n        instances: 500\n        error_rate: 0.054\n        struct_rate: 0.81\n        z_pct_mean: 0.284\n        z_pct_median: 0\n      medium_50_200:\n        repos: 17\n        instances: 4096\n        error_rate: 0.485\n        struct_rate: 0.472\n        z_pct_mean: 0.444\n        z_pct_median: 0.5\n      large_200_500:\n        repos: 40\n        instances: 13628\n        error_rate: 0.639\n        struct_rate: 0.343\n        z_pct_mean: 0.604\n        z_pct_median: 0.857\n      xlarge_500plus:\n        repos: 29\n        instances: 25949\n        error_rate: 0.676\n        struct_rate: 0.314\n        z_pct_mean: 0.812\n        z_pct_median: 0.96\n    instance_distribution:\n      lt10: 1\n      '10_50': 17\n      '50_200': 36\n      '200_500': 40\n      500plus: 29\n    artifact: plan006_full_scalability.json\n- exp_id: m2_full_qwen\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    random_s42:\n      epoch: 3/3\n      current_step: 2950\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.4869\n        recall_at_1: 0.533\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.4651\n        recall_at_1: 0.553\n        recall_at_5: 0.959\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.5365\n        recall_at_1: 0.523\n        recall_at_5: 0.955\n        recall_at_10: 1\n      eval_2000:\n        val_loss: 0.5162\n        recall_at_1: 0.523\n        recall_at_5: 0.954\n        recall_at_10: 1\n      eval_2500:\n        val_loss: 0.5264\n        recall_at_1: 0.527\n        recall_at_5: 0.956\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.4651, R@1=0.553)\n    progress_snapshot: 2026-05-14T13:37 CST\n- exp_id: m2_full_starcoder\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    random_s42:\n      epoch: 2/3\n      current_step: 2000\n      total_steps_per_epoch: 1414\n      eval_500:\n        val_loss: 0.6194\n        recall_at_1: 0.435\n        recall_at_5: 0.905\n        recall_at_10: 1\n      eval_1000:\n        val_loss: 0.6134\n        recall_at_1: 0.454\n        recall_at_5: 0.92\n        recall_at_10: 1\n      eval_1500:\n        val_loss: 0.6528\n        recall_at_1: 0.449\n        recall_at_5: 0.906\n        recall_at_10: 1\n      best_checkpoint: step_1000 (val_loss=0.6134, R@1=0.454)\n    progress_snapshot: 2026-05-14T13:37 CST\n- exp_id: m1_reextract\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: neg_difficulty_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwen_128:\n      random:\n        pos_sim: 0.9804\n        neg_sim: 0.899\n        margin: 0.0816\n        pct_positive_margin: 77.8\n      embedding_distance:\n        pos_sim: 0.9804\n        neg_sim: 0.959\n        margin: 0.0209\n        pct_positive_margin: 60.7\n      dataflow_aware:\n        pos_sim: 0.9805\n        neg_sim: 0.95\n        margin: 0.0309\n        pct_positive_margin: 67.4\n    starcoder_128:\n      random:\n        pos_sim: 0.757\n        neg_sim: 0.553\n        margin: 0.2039\n        pct_positive_margin: 72.8\n      embedding_distance:\n        pos_sim: 0.784\n        neg_sim: 0.668\n        margin: 0.1159\n        pct_positive_margin: 59.2\n      dataflow_aware:\n        pos_sim: 0.761\n        neg_sim: 0.659\n        margin: 0.1022\n        pct_positive_margin: 62.8\n    qwen_2048:\n      random:\n        pos_sim: 0.9855\n        neg_sim: 0.9111\n        margin: 0.0743\n        margin_std: 0.2322\n        pct_positive_margin: 81.8\n      embedding_distance:\n        pos_sim: 0.9855\n        neg_sim: 0.9685\n        margin: 0.017\n        margin_std: 0.114\n        pct_positive_margin: 58.8\n      dataflow_aware:\n        pos_sim: 0.9856\n        neg_sim: 0.9563\n        margin: 0.0293\n        margin_std: 0.1407\n        pct_positive_margin: 73.9\n    starcoder_2048:\n      random:\n        pos_sim: 0.7985\n        neg_sim: 0.6045\n        margin: 0.194\n        margin_std: 0.2788\n        pct_positive_margin: 78\n      embedding_distance:\n        pos_sim: 0.8079\n        neg_sim: 0.7409\n        margin: 0.067\n        margin_std: 0.2056\n        pct_positive_margin: 55\n      dataflow_aware:\n        pos_sim: 0.8009\n        neg_sim: 0.6818\n        margin: 0.1192\n        margin_std: 0.2264\n        pct_positive_margin: 70.4\n    sc_qwen_margin_ratio_128:\n      random: 2.5\n      embedding_distance: 5.54\n      dataflow_aware: 3.3\n    sc_qwen_margin_ratio_2048:\n      random: 2.61\n      embedding_distance: 3.94\n      dataflow_aware: 4.07\n- exp_id: m1_reextract_v2\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T08:03:35.750Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T08:03:35.750Z",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-14T08:03:35.771Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：embedding benefit 可复现但效果量缩水或统计边缘，dataflow 交互效应方向正确但不显著，缺下游验证
核心假设：['embedding > random 方向一致但至少一个编码器 95% CI 包含零（如 StarCoder Δ 缩至 +0.5–1.0pp）', 'dataflow > random 在 Qwen 上方向正确但 CI 包含零（Δ ~+0.3–0.8pp）', '种子间方差较大（R@1 标准差 1.5–3.0pp），削弱统计力度', 'SWE-bench 未完成或 Δ ≤ 1pp（无法宣称下游收益）', 'representation saturation 故事定性成立，但 n=2 编码器不足以做强因果推断']
关键指标范围：{'qwen_embed_vs_random_R1_pp': [0.5, 1.5], 'starcoder_embed_vs_random_R1_pp': [0.0, 1.0], 'qwen_dataflow_vs_random_R1_pp': [0.0, 0.8], 'starcoder_dataflow_vs_random_R1_pp': [-1.5, 0.0], 'best_qwen_mean_R1': [0.52, 0.55], 'best_starcoder_mean_R1': [0.44, 0.48], 'swebench_resolve_delta_pp': [-0.5, 1.0], 'embed_benefit_bootstrap_p': [0.05, 0.2], 'cross_seed_R1_std': [1.5, 3.0]}
叙事方向：Claim 1 降级为 "directional evidence correcting misconception"——embedding mining 不会 harm（纠正 CoCoHaNeRe），但绝对增益需要更多编码器验证。Claim 2 从 "conditional benefit" 降级为 "exploratory observation"——saturation 机制作为 hypothesis 提出，neg_difficulty 分析作为 supporting evidence 而非 proof。删除 "consistently improves" 措辞，替换为 "tends to improve"。 补充 temperature ablation（plan_014）证明发现非 regime-specific。论文重心从 "three claims" 转为 "systematic methodology + preliminary mechanistic hypothesis"，强调方法论贡献 （controlled comparison framework）而非效果量。仍投 EMNLP Main，定位为 analysis paper。


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
  "promptId": "f6b77d69-ceb2-4404-9351-c1b3b8fc68ec",
  "type": "user",
  "uuid": "18b7566c-ce5e-455b-8daf-0718a609588a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T08:03:35.769Z_

```json
{
  "parentUuid": "18b7566c-ce5e-455b-8daf-0718a609588a",
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
  "uuid": "71b4ddff-7ed0-45bf-9577-a84205d6a90f",
  "timestamp": "2026-05-14T08:03:35.769Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T08:03:35.769Z_

```json
{
  "parentUuid": "71b4ddff-7ed0-45bf-9577-a84205d6a90f",
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
  "uuid": "66fa4577-b0c8-49ae-a94c-b5771aff00bc",
  "timestamp": "2026-05-14T08:03:35.769Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-14T08:03:35.769Z_

```json
{
  "parentUuid": "66fa4577-b0c8-49ae-a94c-b5771aff00bc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9942fe91-ce0a-4164-b515-f8d8c3ee88d6",
  "timestamp": "2026-05-14T08:03:35.769Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：embedding benefit 可复现但效果量缩水或统计边缘，dataflow 交互效应方向正确但不显著，缺下游验证 核心假设：['embedding > random 方向一致但至少一个编码器 95% CI 包含零（如 StarCoder Δ 缩至 +0.5–1.0pp）', 'dataflow >…",
  "leafUuid": "9942fe91-ce0a-4164-b515-f8d8c3ee88d6",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict median-tier results for StructFuse contrastive code retrieval",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048"
}
```

---

### Assistant

_source line 9 · 2026-05-14T08:03:52.777Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each "planned" experiment in the experiment_plan, under the "median" tier definition. I need to go through each planned experiment and generate expected results with rationales explaining why those results would occur under the median scenario.

Let me identify all planned experiments:
- plan_003: SWE-bench Lite eval (P0)
- plan_004: RepoBench-R cross-file retrieval (P1)
- plan_005: Embedding vs random deep analysis (P1)
- plan_007: 1-hop vs 2-hop vs 3-hop ablation (P1)


- plan_008: Training data size scaling (P1)
- plan_009: Fusion head ablation (P1)
- plan_010: Dataflow-distance weighted negatives (P2)
- plan_011: Failure analysis (P1)
- plan_012: Qualitative examples (P2)
- plan_014: Temperature ablation (P1)
- plan_015: Dynamic mining baseline (P1)
- plan_016: Bootstrap CI for SWE-bench (P0)
- plan_017: Inference-time graph method comparison (P1)

Now I need to think about what the running experiments might be and how they relate to the planned ones.

Looking at the median tier results, the embedding benefits are reproducible but the effect sizes are shrinking or becoming statistically marginal. The dataflow interactions show the right direction but lack significance, and there's no downstream validation yet. I'm seeing the metric ranges across both models—Qwen's embedding versus random ranges from 0.5 to 1.5 while StarCoder's is 0.0 to 1.0, and the dataflow comparisons show Qwen at 0.0 to 0.8 versus StarCoder's negative range of -1.5 to 0.0. The best Qwen mean R1 is hovering around 0.52 to 0.55.

Now I'm looking at the rest of the performance bounds—StarCoder's best mean R1 sits between 0.44 and 0.48, the SWE-bench resolve delta spans -0.5 to 1.0, embedding benefit bootstrap p-values range from 0.05 to 0.2, and cross-seed R1 standard deviation is between 1.5 and 3.0. With these ranges in mind, I'm ready to build out detailed predictions for each of the planned experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9942fe91-ce0a-4164-b515-f8d8c3ee88d6",
  "isSidechain": false,
  "requestId": "req_011Cb27WpRneCMwiXzb5JmVL",
  "type": "assistant",
  "uuid": "f281c84e-5b96-4881-8a64-5afe078a42e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEaAEKxveNGji97Jq2M5B2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17568,
      "cache_read_input_tokens": 11447,
      "output_tokens": 9381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17568,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 9381,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 17568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17568
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

_source line 10 · 2026-05-14T08:06:33.769Z_

```yaml
tier: median
narrative_guidance: >
  Claim 1 降级为 "directional evidence"——embedding mining 方向一致但 95% CI 宽，至少一个编码器包含零。
  Claim 2 降为 "exploratory observation"——dataflow 在 Qwen 上方向正确但不显著，StarCoder 上甚至略负。
  论文重心转向方法论贡献（controlled comparison framework + representation geometry analysis），
  效果量作为 preliminary evidence 呈现。SWE-bench 未能提供有说服力的下游验证。
  "tends to improve" 替代 "consistently improves"。仍投 EMNLP Main，定位 analysis paper。

imagined_experiments:
  - name: "SWE-bench Lite end-to-end evaluation"
    plan_id: plan_003
    description: "3 strategies × best checkpoint, Qwen3.6-27B agent, 300 SWE-bench Lite instances"
    expected_results:
      random_resolve_rate_pct: 18.3
      embedding_distance_resolve_rate_pct: 18.7
      dataflow_aware_resolve_rate_pct: 18.0
      embed_vs_random_delta_pp: 0.4
      dataflow_vs_random_delta_pp: -0.3
      retrieval_recall_at_5_random: 0.41
      retrieval_recall_at_5_embed: 0.43
      retrieval_recall_at_5_dataflow: 0.42
      instances_evaluated: 287
      instances_failed_agent_error: 13
    result_rationale: >
      median 档下 SWE-bench Δ ≤ 1pp。原因：(1) 300 实例中仅 ~50% 的 bug 与 retrieval 质量相关，
      其余受 patch generation 瓶颈限制——retriever 的 +1pp R@1 优势在 end-to-end pipeline 中被稀释；
      (2) SWE-bench 的 repo 分布与训练集 SWE-smith 有 domain shift，
      m2_full 训练中观测到的 step 1000 后过拟合加剧了这种 gap；
      (3) agent 的 file selection 依赖多轮交互，单次 retrieval 改进的边际效用递减。
      embedding 略优于 random 但幅度 <1pp，dataflow 因在 unseen repos 上结构信号噪声更大反而微跌。
      整体 resolve rate ~18% 处于 baseline agent 的正常水平，无法宣称下游收益。
    tables:
      - name: "Table: SWE-bench Lite Resolve Rate by Strategy"
        columns: ["Strategy", "Resolve Rate (%)", "Δ vs Random (pp)", "Retrieval R@5"]
        rows:
          - ["random", "18.3", "—", "0.41"]
          - ["embedding_distance", "18.7", "+0.4", "0.43"]
          - ["dataflow_aware", "18.0", "−0.3", "0.42"]
    figures_description:
      - "Bar chart: resolve rate ± 95% binomial CI per strategy, 三根 bar 的 CI 完全重叠"
    analysis: >
      SWE-bench 无法区分三种策略。写入论文时定位为 "downstream evaluation shows no statistically
      distinguishable difference"，并 acknowledge retrieval gains 在 end-to-end pipeline 中
      被 generation bottleneck 稀释。这不否定 retrieval 改进，但不能用作 downstream evidence。

  - name: "RepoBench-R cross-file retrieval evaluation"
    plan_id: plan_004
    description: "retrieval-only evaluation on RepoBench-R, 3 strategies × best checkpoint, 两个编码器"
    expected_results:
      qwen_random_R1: 0.312
      qwen_embed_R1: 0.325
      qwen_dataflow_R1: 0.318
      starcoder_random_R1: 0.274
      starcoder_embed_R1: 0.279
      starcoder_dataflow_R1: 0.268
      qwen_embed_vs_random_delta_pp: 1.3
      starcoder_embed_vs_random_delta_pp: 0.5
      qwen_dataflow_vs_random_delta_pp: 0.6
      starcoder_dataflow_vs_random_delta_pp: -0.6
    result_rationale: >
      RepoBench-R 的 cross-file retrieval 与 SWE-smith 训练分布差异显著——RepoBench 侧重
      next-line completion 的上下文文件，粒度更细且不直接对应 bug-fix file selection。
      median 档下 embedding 优势方向保持但缩水：Qwen ~+1.3pp（pilot 中 +2.0pp 缩水约 35%，
      因 domain shift 和 evaluation granularity 不同），StarCoder ~+0.5pp（CI 将包含零）。
      Dataflow 在 Qwen 上仅 +0.6pp（RepoBench 的文件间 dataflow 关系与训练时 CodeQL 提取的
      分布不匹配），StarCoder 上略负。绝对 R@1 水平较低（0.27-0.33）因 RepoBench candidate pool
      远大于 m2 验证集的 pool=50。方向一致性为 "directional evidence" 叙事提供第二个 benchmark 支持，
      但效果量不足以做强声明。
    tables:
      - name: "Table: RepoBench-R R@1 by Encoder × Strategy"
        columns: ["Encoder", "random", "embedding", "dataflow", "embed Δ", "dataflow Δ"]
        rows:
          - ["Qwen2.5-Coder-3B", "0.312", "0.325", "0.318", "+1.3pp", "+0.6pp"]
          - ["StarCoder2-3B", "0.274", "0.279", "0.268", "+0.5pp", "−0.6pp"]
    figures_description:
      - "Grouped bar chart: R@1 per encoder × strategy，附 bootstrap 95% CI"
    analysis: >
      RepoBench-R 结果与 SWE-smith eval 方向一致但效果量更小，增强 "directional evidence" 论点。
      写入论文时强调 cross-benchmark consistency of direction 而非 magnitude。

  - name: "Embedding vs random deep analysis by repo complexity"
    plan_id: plan_005
    description: "按 repo size/complexity 分层分析 embedding negatives 的效果"
    expected_results:
      small_repos_lt50_embed_delta_pp: 2.1
      medium_repos_50_200_embed_delta_pp: 1.0
      large_repos_200_500_embed_delta_pp: 0.3
      xlarge_repos_500plus_embed_delta_pp: -0.2
      complexity_correlation_r: -0.41
      complexity_correlation_p: 0.08
    result_rationale: >
      median 档下 embedding benefit 在小 repo 上最明显（candidate pool 小，embedding distance
      能有效区分 near-miss），但随 repo 规模增大效果递减甚至反转。原因：大 repo 中 embedding space
      拥挤程度更高，pretrained encoder 的 representation 更接近 saturation，
      embedding-distance mining 选出的 negatives 与 random 的 difficulty 差异缩小。
      相关性方向正确（r ≈ −0.41）但 p=0.08 不显著——样本量仅 123 repos 中有结构数据的子集，
      power 不足。此分析为 Claim 2 的 saturation 机制提供 supporting but inconclusive evidence。
    tables:
      - name: "Table: Embedding Δ by Repo Size Tier (Qwen)"
        columns: ["Tier", "N repos", "embed Δ R@1 (pp)", "mean neg_difficulty margin"]
        rows:
          - ["<50 instances", "1", "+2.1", "0.068"]
          - ["50–200", "17", "+1.0", "0.032"]
          - ["200–500", "40", "+0.3", "0.019"]
          - ["500+", "29", "−0.2", "0.014"]
    figures_description:
      - "Scatter plot: repo size (x) vs embedding benefit Δ (y), with regression line and 95% CI band"
      - "Box plot: neg_difficulty margin distribution by repo size tier"
    analysis: >
      趋势方向支持 saturation hypothesis 但统计力度不足（p=0.08）。
      论文中作为 "exploratory analysis suggesting repo complexity moderates embedding benefit"，
      n=2 编码器 × uneven tier sizes 限制了因果推断。

  - name: "1-hop vs 2-hop vs 3-hop call-graph bounding ablation"
    plan_id: plan_007
    description: "测试不同 call-graph 深度对 dataflow negative 质量的影响"
    expected_results:
      hop1_qwen_R1: 0.531
      hop2_qwen_R1: 0.538
      hop3_qwen_R1: 0.534
      hop1_coverage_pct: 42.1
      hop2_coverage_pct: 34.3
      hop3_coverage_pct: 28.7
      hop2_vs_hop1_delta_pp: 0.7
      hop3_vs_hop2_delta_pp: -0.4
    result_rationale: >
      median 档下 hop 数的 ablation 呈倒 U 型但差异不大。2-hop（当前设置）略优于 1-hop
      因为覆盖了更多真实的 transitive dependencies，但 3-hop 引入过多 spurious connections
      （大 repo 中 3-hop 几乎把所有文件连通），diluting structural signal。
      差异仅 ~0.7pp，在 cross-seed 方差 1.5-3.0pp 的背景下不显著。
      Coverage 随 hop 增加而下降（disconnected files 减少 → 可选 negative 减少）。
      这说明当前 2-hop 设置合理但并非 critical design choice。
    tables:
      - name: "Table: Hop Depth Ablation (Qwen, dataflow strategy)"
        columns: ["Hops", "R@1", "Coverage (%)", "Avg negatives/query"]
        rows:
          - ["1-hop", "0.531", "42.1", "8.3"]
          - ["2-hop", "0.538", "34.3", "5.7"]
          - ["3-hop", "0.534", "28.7", "3.9"]
    figures_description:
      - "Line plot: R@1 vs hop depth, with error bars from 3 seeds"
    analysis: >
      2-hop 是 sweet spot 但差异在噪声范围内。论文中简要报告作为 design justification，
      不作为独立 finding。

  - name: "Training data size scaling ablation"
    plan_id: plan_008
    description: "1K vs 3K vs 5K training instances, 测试 data scaling behavior"
    expected_results:
      size_1k_qwen_R1: 0.518
      size_3k_qwen_R1: 0.541
      size_5k_qwen_R1: 0.538
      size_1k_embed_delta_pp: 1.8
      size_3k_embed_delta_pp: 1.1
      size_5k_embed_delta_pp: 0.9
      size_1k_starcoder_R1: 0.432
      size_3k_starcoder_R1: 0.451
      size_5k_starcoder_R1: 0.448
    result_rationale: >
      median 档下 data scaling 呈 diminishing returns：1K→3K 有明显提升（+2.3pp），
      3K→5K 几乎持平甚至微降（过拟合加剧，与 m2_full 观察到的 step 1000 后过拟合一致）。
      更关键的是 embedding benefit Δ 随数据量增加而缩小：1K 时 Δ=1.8pp（小数据下 hard negative
      质量差异被放大），5K 时 Δ=0.9pp（更多数据提供足够 coverage，减少对 mining 策略的依赖）。
      这对 median 叙事不利——暗示在更大数据规模下 embedding benefit 可能进一步缩水。
    tables:
      - name: "Table: Data Scaling × Strategy (Qwen, embedding strategy)"
        columns: ["Train Size", "random R@1", "embed R@1", "Δ (pp)"]
        rows:
          - ["1K", "0.500", "0.518", "+1.8"]
          - ["3K", "0.530", "0.541", "+1.1"]
          - ["5K", "0.529", "0.538", "+0.9"]
    figures_description:
      - "Line plot: R@1 vs training data size, separate lines for random/embed/dataflow"
      - "Bar chart: embed Δ at each data size, showing diminishing gap"
    analysis: >
      Diminishing benefit at larger data scale 是 median 档的典型特征——方向正确但实际意义
      随 scale 递减。论文中诚实报告，作为 limitation 的一部分。

  - name: "Fusion head ablation"
    plan_id: plan_009
    description: "embedding-only vs structural-features-only vs combined scoring"
    expected_results:
      embed_only_qwen_R1: 0.538
      struct_only_qwen_R1: 0.489
      combined_qwen_R1: 0.541
      embed_only_starcoder_R1: 0.451
      struct_only_starcoder_R1: 0.412
      combined_starcoder_R1: 0.448
      combined_vs_embed_only_delta_pp: 0.3
    result_rationale: >
      median 档下 structural features alone 表现较差（R@1=0.489），因为 CodeQL dataflow
      features 是 binary/sparse 的，单独使用缺乏 fine-grained discrimination。
      Combined (embed + struct) 仅比 embed-only 好 +0.3pp——structural signal
      的增量贡献在融合后被稀释，且 combined model 有更多参数容易过拟合（与 step 1000
      过拟合现象一致）。StarCoder 上 combined 甚至略低于 embed-only（-0.3pp），
      因为 StarCoder 的 healthy representation space 不需要额外维度的信号。
      这进一步支持 "conditional benefit" 的定性结论但效果量太小。
    tables:
      - name: "Table: Fusion Head Ablation"
        columns: ["Head", "Qwen R@1", "StarCoder R@1"]
        rows:
          - ["embed-only", "0.538", "0.451"]
          - ["struct-only", "0.489", "0.412"]
          - ["combined", "0.541", "0.448"]
    figures_description:
      - "Stacked bar chart showing contribution decomposition of embed vs struct features"
    analysis: >
      Combined head 增益微乎其微，论文中报告为 "structural features provide marginal
      additive benefit in fusion"。不值得作为独立 contribution point。

  - name: "Dataflow-distance weighted negatives ablation"
    plan_id: plan_010
    description: "weighted sampling by dataflow distance vs binary connected/disconnected"
    expected_results:
      binary_qwen_R1: 0.538
      weighted_qwen_R1: 0.535
      binary_starcoder_R1: 0.448
      weighted_starcoder_R1: 0.444
    result_rationale: >
      median 档下 weighted sampling 不优于 binary。原因：CodeQL 提取的 dataflow distance
      分布高度 bimodal（connected with distance 1-2 占大多数，disconnected 占其余），
      smooth weighting 在这种分布上退化为近似 binary。且 weighted 引入的额外超参数
      （distance decay function）在 n=123 repos 的数据量下难以 tune，noise 抵消了
      理论上的 curriculum benefit。这是一个 null result，说明 binary structural signal
      已捕获大部分可用信息。
    tables:
      - name: "Table: Weighted vs Binary Dataflow Negatives"
        columns: ["Method", "Qwen R@1", "StarCoder R@1"]
        rows:
          - ["binary (current)", "0.538", "0.448"]
          - ["distance-weighted", "0.535", "0.444"]
    figures_description:
      - "Histogram of dataflow distances showing bimodal distribution"
    analysis: >
      Null result，论文中用一句话在 ablation section 报告："distance-weighted sampling
      does not improve over binary selection, likely due to the bimodal distance distribution."

  - name: "SWE-bench failure analysis"
    plan_id: plan_011
    description: "50 SweRank/BM25 failure cases 分类分析"
    expected_results:
      total_analyzed: 50
      category_retrieval_miss: 18
      category_generation_fail: 22
      category_test_flaky: 4
      category_multi_file_needed: 6
      retrieval_miss_where_dataflow_helps: 5
      retrieval_miss_where_dataflow_neutral: 10
      retrieval_miss_where_dataflow_hurts: 3
      pct_dataflow_helps_of_retrieval_miss: 27.8
    result_rationale: >
      median 档下 failure analysis 揭示 SWE-bench 上 retrieval 并非主要瓶颈——
      50 个失败案例中仅 18 个（36%）是因为 retrieval miss，其余是 generation/test issues。
      在 18 个 retrieval miss 中，dataflow 仅帮助 5 个（27.8%）——这些是跨文件依赖链上的
      bug，dataflow connectivity 确实提供了有用信号。但 10 个 neutral（文件间无 dataflow
      关系或关系被 CodeQL 漏提取）和 3 个 hurt（dataflow 引入 noise 反而 distract）
      使整体效果被抵消。这解释了为什么 plan_003 中 SWE-bench resolve rate 差异 <1pp。
    tables:
      - name: "Table: Failure Category Distribution"
        columns: ["Category", "Count", "%"]
        rows:
          - ["Retrieval miss", "18", "36%"]
          - ["Generation failure", "22", "44%"]
          - ["Flaky test", "4", "8%"]
          - ["Multi-file needed", "6", "12%"]
      - name: "Table: Dataflow Impact on Retrieval Misses"
        columns: ["Dataflow effect", "Count", "%"]
        rows:
          - ["Helps", "5", "27.8%"]
          - ["Neutral", "10", "55.6%"]
          - ["Hurts", "3", "16.7%"]
    figures_description:
      - "Sankey diagram: failure categories → dataflow impact"
      - "Concrete example pair: one case where dataflow helped (cross-module dependency) and one where it hurt (false connectivity)"
    analysis: >
      Failure analysis 提供定性 insight 但定量上支持 "generation bottleneck dominates
      retrieval differences" 的结论。论文中用于 explain 为什么 SWE-bench Δ 小，
      并 motivate future work on generation-aware retrieval。

  - name: "Qualitative examples"
    plan_id: plan_012
    description: "5-10 cases where structural negatives changed retrieval outcome"
    expected_results:
      positive_examples_found: 4
      negative_examples_found: 2
      ambiguous_examples: 2
      total_curated: 8
    result_rationale: >
      median 档下能找到 4 个 convincing positive examples（dataflow negative 帮助
      retriever 区分 lexically similar but structurally unrelated files），但也有
      2 个 negative examples（dataflow 引入的 structural bias 导致 miss）。
      这与 median 的 "directional but not definitive" 叙事一致。8 个案例中
      pattern 不够 clean 来支持强因果推断——n=2 编码器 + case-by-case 分析
      只能说明 mechanism 是 plausible 而非 proven。
    tables: []
    figures_description:
      - "Figure: 2 positive + 1 negative case study panels, showing query → retrieved files → gold files, with dataflow graph overlay"
    analysis: >
      精选 cases 放入论文 qualitative section，明确标注 positive 和 negative examples
      以保持学术诚实。reviewer 会 appreciate balanced presentation。

  - name: "Temperature ablation"
    plan_id: plan_014
    description: "τ ∈ {0.05, 0.1, 0.2}, 3 strategies × 2 encoders"
    expected_results:
      qwen_tau005_random_R1: 0.521
      qwen_tau005_embed_R1: 0.534
      qwen_tau005_dataflow_R1: 0.530
      qwen_tau010_random_R1: 0.533
      qwen_tau010_embed_R1: 0.543
      qwen_tau010_dataflow_R1: 0.538
      qwen_tau020_random_R1: 0.524
      qwen_tau020_embed_R1: 0.531
      qwen_tau020_dataflow_R1: 0.527
      starcoder_tau005_random_R1: 0.438
      starcoder_tau005_embed_R1: 0.443
      starcoder_tau005_dataflow_R1: 0.430
      starcoder_tau010_random_R1: 0.449
      starcoder_tau010_embed_R1: 0.456
      starcoder_tau010_dataflow_R1: 0.441
      starcoder_tau020_random_R1: 0.442
      starcoder_tau020_embed_R1: 0.446
      starcoder_tau020_dataflow_R1: 0.435
      embed_benefit_direction_consistent_across_tau: true
      dataflow_benefit_direction_inconsistent: true
      optimal_tau: 0.1
    result_rationale: >
      median 档下 temperature ablation 证明 embedding > random 的方向在所有 τ 值下一致
      （这是好消息，说明发现非 regime-specific）。但 Δ 在 τ=0.05 和 τ=0.2 下缩小：
      τ=0.05 时 loss landscape 过于 sharp，所有策略表现都下降，差异被 noise 淹没；
      τ=0.2 时 loss 太平滑，hard negatives 的难度梯度被抹平。τ=0.1 是 sweet spot。
      Dataflow 的方向在 τ 间不一致——τ=0.05 时 Qwen 上 dataflow 略优于 random，
      τ=0.2 时略劣——进一步支持 "conditional and fragile" 的定性判断。
      Cross-seed 方差在 τ=0.05 下最大（~3.0pp std），τ=0.1 最稳定（~1.8pp std）。
    tables:
      - name: "Table: Temperature × Strategy R@1 (Qwen)"
        columns: ["τ", "random", "embed", "dataflow", "embed Δ", "dataflow Δ"]
        rows:
          - ["0.05", "0.521", "0.534", "0.530", "+1.3", "+0.9"]
          - ["0.10", "0.533", "0.543", "0.538", "+1.0", "+0.5"]
          - ["0.20", "0.524", "0.531", "0.527", "+0.7", "+0.3"]
      - name: "Table: Temperature × Strategy R@1 (StarCoder)"
        columns: ["τ", "random", "embed", "dataflow", "embed Δ", "dataflow Δ"]
        rows:
          - ["0.05", "0.438", "0.443", "0.430", "+0.5", "−0.8"]
          - ["0.10", "0.449", "0.456", "0.441", "+0.7", "−0.8"]
          - ["0.20", "0.442", "0.446", "0.435", "+0.4", "−0.7"]
    figures_description:
      - "Heatmap: τ × strategy, cell color = R@1, separate panels for Qwen and StarCoder"
      - "Line plot: embed Δ vs τ, showing consistent positive direction"
    analysis: >
      Temperature ablation 是 median 档的关键正面结果之一：embedding benefit 方向 robust across τ。
      论文中重点报告此 robustness 作为 Claim 1 的 supporting evidence，
      同时 acknowledge Claim 2 (dataflow) 的 τ-sensitivity 作为 limitation。

  - name: "Dynamic mining baseline"
    plan_id: plan_015
    description: "re-mine embedding negatives per epoch vs static (mine once from pretrained)"
    expected_results:
      static_qwen_R1: 0.543
      dynamic_qwen_R1: 0.547
      static_starcoder_R1: 0.456
      dynamic_starcoder_R1: 0.452
      dynamic_vs_static_qwen_delta_pp: 0.4
      dynamic_vs_static_starcoder_delta_pp: -0.4
      dynamic_compute_overhead_factor: 3.2
    result_rationale: >
      median 档下 dynamic mining 在 Qwen 上微优（+0.4pp）但 StarCoder 上微劣（-0.4pp），
      差异在 noise 范围内。原因：(1) static mining 在仅 3 epoch 的训练中 representation
      drift 有限——encoder 是 LoRA fine-tune，参数变化量小，pretrained 时的 embedding distance
      排序在训练后基本保持；(2) dynamic re-mining 引入计算开销（3.2x）但因 LoRA 的低 drift
      几乎不改变 negative selection；(3) StarCoder 上 dynamic 略差可能因 re-mining 引入的
      randomness（每次 re-mining 的 batch 不完全一致）。结论：static vs dynamic 不是
      关键 confound，当前 static 设计合理。
    tables:
      - name: "Table: Static vs Dynamic Mining"
        columns: ["Mining", "Qwen R@1", "StarCoder R@1", "GPU hours"]
        rows:
          - ["Static (current)", "0.543", "0.456", "3.5"]
          - ["Dynamic (per-epoch)", "0.547", "0.452", "11.2"]
    figures_description:
      - "Bar chart: static vs dynamic R@1, with compute cost annotation"
    analysis: >
      Null result for practical purposes. 论文中一句话报告："dynamic re-mining does not
      significantly improve over static mining given the limited representation drift
      in LoRA fine-tuning (3 epochs)"。排除了 reviewer concern about static/dynamic confound。

  - name: "Bootstrap CI for SWE-bench Lite"
    plan_id: plan_016
    description: "95% bootstrap CI for resolve rate differences"
    expected_results:
      embed_vs_random_delta_pp: 0.4
      embed_vs_random_95ci_lower: -1.8
      embed_vs_random_95ci_upper: 2.6
      dataflow_vs_random_delta_pp: -0.3
      dataflow_vs_random_95ci_lower: -2.5
      dataflow_vs_random_95ci_upper: 1.9
      bootstrap_n: 10000
      embed_vs_random_p_value: 0.34
    result_rationale: >
      median 档下 SWE-bench 的 Δ ≤ 1pp，在 300 instances 上 bootstrap CI 极宽。
      300 实例的 binomial 标准误约 ±2.2pp（at resolve rate ~18%），
      所以 Δ=0.4pp 的 95% CI 为 [-1.8, +2.6]，包含零。p=0.34 远不显著。
      这是 median 档的核心弱点：无法宣称下游收益。
      Dataflow 的 CI 同样包含零且 point estimate 为负。
    tables:
      - name: "Table: SWE-bench Bootstrap CI"
        columns: ["Comparison", "Δ (pp)", "95% CI", "p-value"]
        rows:
          - ["embed vs random", "+0.4", "[−1.8, +2.6]", "0.34"]
          - ["dataflow vs random", "−0.3", "[−2.5, +1.9]", "0.41"]
    figures_description:
      - "Forest plot: point estimates with 95% CI bars, reference line at zero"
    analysis: >
      CI 均包含零，论文中必须诚实报告 "no statistically significant difference in
      downstream resolve rate"。但可同时 argue retrieval-level improvements
      (plan_002/plan_013) 的 bootstrap CI 更紧（pool=50 的 val set 上），
      downstream pipeline 的 noise 是 confound 而非 evidence against retrieval gains。

  - name: "Inference-time graph method comparison discussion"
    plan_id: plan_017
    description: "与 CodexGraph, LocAgent 等 inference-time 方法的定位比较"
    expected_results:
      comparison_type: "qualitative_discussion"
      codexgraph_reported_R1_improvement_pp: 5.2
      locagent_reported_resolve_rate_pct: 26.3
      structfuse_retrieval_R1: 0.543
      key_distinction: "training-time vs inference-time structural signal"
      complementarity_argument_strength: "moderate"
    result_rationale: >
      median 档下此项为 qualitative discussion 而非实验。StructFuse（training-time
      structural mining）与 CodexGraph/LocAgent（inference-time graph navigation）
      在方法论上互补：前者提升 base retriever 质量，后者在 inference 时做 multi-hop
      reasoning。但 median 档下 StructFuse 的 absolute improvement 较小（+1pp R@1），
      complementarity argument 的说服力为 "moderate"——reviewer 可能问 "if inference-time
      methods already get +5pp, why bother with +1pp training-time improvement?"
      回应：training-time improvement 是 zero-cost at inference，可叠加使用。
    tables:
      - name: "Table: Training-time vs Inference-time Structural Methods"
        columns: ["Method", "Type", "Structural Signal", "Inference Cost", "Reported Gain"]
        rows:
          - ["StructFuse (ours)", "training-time", "CodeQL dataflow", "zero", "+0.5–1.5pp R@1"]
          - ["CodexGraph", "inference-time", "LLM-built graph", "high (LLM calls)", "+5.2pp R@1"]
          - ["LocAgent", "inference-time", "call graph navigation", "moderate", "26.3% resolve"]
    figures_description:
      - "Comparison table in Related Work section"
    analysis: >
      Discussion section 而非实验。定位 StructFuse 为 complementary approach——
      zero inference cost, improves base retriever that inference-time methods build upon.
      Acknowledge median 档的 modest gains 使此 argument 需要 future work validation。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f281c84e-5b96-4881-8a64-5afe078a42e2",
  "isSidechain": false,
  "requestId": "req_011Cb27WpRneCMwiXzb5JmVL",
  "type": "assistant",
  "uuid": "2ff78487-833e-4ebd-babc-2c9eb6c4d32e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEaAEKxveNGji97Jq2M5B2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17568,
      "cache_read_input_tokens": 11447,
      "output_tokens": 9381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17568,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 9381,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 17568,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17568
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：embedding benefit 可复现但效果量缩水或统计边缘，dataflow 交互效应方向正确但不显著，缺下游验证 核心假设：['embedding > random 方向一致但至少一个编码器 95% CI 包含零（如 StarCoder Δ 缩至 +0.5–1.0pp）', 'dataflow >…",
  "leafUuid": "2ff78487-833e-4ebd-babc-2c9eb6c4d32e",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict median-tier results for StructFuse contrastive code retrieval",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：embedding benefit 可复现但效果量缩水或统计边缘，dataflow 交互效应方向正确但不显著，缺下游验证 核心假设：['embedding > random 方向一致但至少一个编码器 95% CI 包含零（如 StarCoder Δ 缩至 +0.5–1.0pp）', 'dataflow >…",
  "leafUuid": "2ff78487-833e-4ebd-babc-2c9eb6c4d32e",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Predict median-tier results for StructFuse contrastive code retrieval",
  "sessionId": "23dadbc4-6387-4095-a1b3-026856e76048"
}
```

---
