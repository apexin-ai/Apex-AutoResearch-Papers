# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：核心假设部分验证，部分 reviewer 质疑效应量或覆盖面，论文落入 EMNLP Findings 或需 rebuttal 挽救 核心假设：["A

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/c3c703d5-f588-4e67-b762-e7ebe9792a81.jsonl`
- **Structured JSON:** [`80c66843b5d8ce028cdf.json`](../../sessions/80/80c66843b5d8ce028cdf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T07:43:09.849Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T07:43:09.849Z",
  "sessionId": "c3c703d5-f588-4e67-b762-e7ebe9792a81",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：核心假设部分验证，部分 reviewer 质疑效应量或覆盖面，论文落入 EMNLP Findings 或需 rebuttal 挽救\n核心假设：[\"A1 部分成立: Pairwise r=0.11-0.13 被质疑为'统计显著但实际意义有限'，需补充 FewRel 的大效应量（Δ=-31pp）来说服\", 'A2 成立: Error taxonomy 证据清晰，无争议', 'A3 成立: Scaling 证据充分', 'A4 部分成立: Reviewers 指出 LLaMA 仅在 FewRel 成功，Few-NERD 多次失败是 generalizability 短板', 'A5 争议: 1-2 位 reviewer 视 MAVEN per-type 正方向为 counter-evidence，centrality confound 解释被要求补充定量验证', \"A6 争议: 'No practical method' 被标记为主要弱点，SDGD 负面结果不足以弥补\", 'A7 基本成立: 实证研究格式被接受，但被要求补充更强的 practical implications']\n关键指标范围：{'arr_avg_score': [3.0, 3.5], 'claims_fully_supported': [1, 2], 'major_reviewer_weaknesses': [2, 3], 'cross_task_significant_replications': [2, 3], 'multi_model_effect_consistency': [0.7, 0.85], 'venue_probability_main': [0.15, 0.35], 'venue_probability_findings_or_above': [0.5, 0.7], 'rebuttal_flip_probability': [0.4, 0.65]}\n叙事方向：需要调整 claim 强度和重心分配。\"independently predicts\" 软化为 \"is associated with\" 或 \"contributes to predicting\"。将 FewRel 的大效应量（Δ=-31pp, -27pp cross-model） 提升为 headline evidence，pairwise r=0.11-0.13 降级为 supplementary cross-task validation。 Claim 2（multi-channel）保持不变，error taxonomy 是最无争议的证据。 补充一个 \"practitioner guideline\" 小节：基于发现给出 schema 设计的具体建议 （e.g., 避免 BCS>0.8 的类型同批出现），弥补没有可用方法的短板。 MAVEN centrality confound 可能需要追加 synthetic schema 实验来定量验证聚合失效条件。 Rebuttal 重点: (1) effect size 在 IE 任务中的合理性论证, (2) LLaMA NER 失败的技术原因 (模型输出格式问题而非假设不成立), (3) 补充 1-2 个 reviewer 要求的分析。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: schema-dag-extraction\n\n## paper_framing.md\n\n# Paper Framing — schema-dag-extraction\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\n- Commitment deadline: August 2, 2026\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\n- Deadline: ARR May 25, 2026 (10 days from today)\n\n## Core Claims (2 claims) — Revised per D019\n\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\n\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\n\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \"why naive decomposition fails\" is itself a contribution.\n\n## Story Spine — Revised per D012\n\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\n\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\n\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.\n\n- **Three-task validation**:\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\n\n- **Headline result template**: \"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid.\"\n\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\n\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\n\nThese channels are orthogonal and independently addressable.\n\n**Pairwise vs Aggregated Confusability**:\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\n\n## Evidence Hierarchy (D012)\n\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\n\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\n\n**Few-NERD (NER)** — Qwen3 embeddings:\n- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation\n- Nonzero-only Spearman ρ=0.272 (p=5e-5)\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\n- Immune to type frequency confound (operates at type-pair level)\n\n**MAVEN (ED)** — MiniLM embeddings:\n- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\n- Cross-task replication on same-domain schema\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\n\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\n\nLarge effect size, cross-task (RE), scaling with schema complexity:\n\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\n\n**16-rel sanity check** (exp_fewrel_formal):\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\n\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\n\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\n\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\n\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\n\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\n\nMethodological case study on when aggregated confusability measures fail:\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\n- This is stronger than \"domain boundary\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\n\n### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)\n\nIntraSub rate monotonically increases with BCS on both NER and RE:\n\n**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0\n**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)\n- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon\n- Same mechanism, different absolute magnitudes — consistent with cross-task expectations\n\nAdditional from extreme batch design:\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\n\n## Embedding Ablation (D010)\n\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\n\n### Per-type (Layer 2)\n| | Few-NERD | FewRel | MAVEN |\n|---|---|---|---|\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\n\n### Pairwise (Layer 1)\n| | Few-NERD | MAVEN |\n|---|---|---|\n| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |\n| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |\n\n### SCS→Empirical Confusion Validation (exp-015 fast)\n| | Qwen3 | MiniLM |\n|---|---|---|\n| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |\n| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |\n\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \"Lost in the Middle\" (TACL 2024).\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy | Experiment |\n|---------|------------------|------------|\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]\n    on Few-NERD with Qwen3-32B-FP8'\n  priority: P0\n  gpu_budget_hours: 3.5\n  deps: []\n  registry_id: exp001_count_baseline\n  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction\n    at low counts.\n  status: DONE\n  conclusion: success\n  metrics:\n    diagnosis: char offset 96.5% fabricated by model\n    text_match_reeval:\n      count_1:\n        f1: 0.184\n        precision: 0.105\n        recall: 0.72\n        pred_gold_ratio: 6.85\n      count_2:\n        f1: 0.123\n        precision: 0.068\n        recall: 0.698\n        pred_gold_ratio: 10.33\n      count_6:\n        f1: 0.155\n        precision: 0.088\n        recall: 0.62\n        pred_gold_ratio: 7.02\n      count_12:\n        f1: 0.246\n        precision: 0.16\n        recall: 0.539\n        pred_gold_ratio: 3.38\n      count_22:\n        f1: 0.322\n        precision: 0.232\n        recall: 0.527\n        pred_gold_ratio: 2.27\n      count_44:\n        f1: 0.473\n        precision: 0.414\n        recall: 0.551\n        pred_gold_ratio: 1.33\n      count_64:\n        f1: 0.463\n        precision: 0.52\n        recall: 0.418\n        pred_gold_ratio: 0.8\n    key_finding: recall monotonically decreases (0.72→0.42), precision monotonically\n      increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at\n      count_44\n    wrong_type_trend: 'type confusion increases with count: 0→2434, supports confusability\n      hypothesis'\n    spurious_dominant: spurious FPs (text in source but not entity) dominate at low\n      count, not hallucination\n    conclusion_text_match: F1 curve inversion caused by over-prediction confound,\n      NOT absence of confusability effect. Recall curve + type confusion pattern support\n      hypothesis.\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,\n    25 random + extreme batches on Few-NERD'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  registry_id: exp002_confusability_controlled\n  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion\n    rate 10-28x.\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp2_reeval_results.json (text_match, CLEAN)\n    primary_recall_vs_bcs:\n      count_6:\n        r: 0.2754\n        p: 0.1644\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.2219\n        p: 0.266\n        n: 27\n        verdict: FAIL\n      partial:\n        r: 0.2522\n        p: 0.0658\n        n: 54\n        verdict: FAIL\n    secondary_f1_vs_bcs:\n      count_6:\n        r: 0.1754\n        p: 0.3814\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.5012\n        p: 0.0077\n        n: 27\n        verdict: PASS\n      partial:\n        r: 0.3025\n        p: 0.0262\n        n: 54\n        verdict: PASS\n    mechanistic_confusion_rate:\n      random_batches:\n        count_6_high: 0.0157\n        count_6_low: 0.0088\n        ratio_6: 1.7\n        count_12_high: 0.0304\n        count_12_low: 0.0131\n        ratio_12: 2.4\n      extreme_batches:\n        count_6_high: 0.0728\n        count_6_low: 0.0014\n        ratio_6: 27.5\n        count_12_high: 0.048\n        count_12_low: 0.0061\n        ratio_12: 9.9\n      verdict: PASS\n    pairwise_confusion_analysis:\n      all:\n        n_pairs: 1953\n        pearson_r: 0.156\n        pearson_p: 4.6e-12\n        spearman_rho: 0.16\n        spearman_p: 1.3e-12\n      count_6:\n        n_pairs: 1770\n        pearson_r: 0.078\n        pearson_p: 0.001\n      count_12:\n        n_pairs: 1953\n        pearson_r: 0.147\n        pearson_p: 6.7e-11\n      nonzero_only:\n        all_spearman_rho: 0.254\n        all_spearman_p: 1.1e-06\n        count_12_pearson_r: 0.212\n        count_12_p: 0.00034\n      top_confused_pair: person-other <-> person-politician (BCS=0.934, confusion=156)\n    per_type_analysis:\n      n_types: 63\n      filter: freq>=5\n      micro_f1_vs_bcs:\n        pearson_r: -0.1828\n        pearson_p: 0.1516\n        spearman_rho: -0.2927\n        spearman_p: 0.0199\n        partial_r_ctrl_logfreq: -0.1998\n        partial_p: 0.1163\n      mean_f1_vs_bcs:\n        pearson_r: -0.1374\n        pearson_p: 0.283\n        spearman_rho: -0.2412\n        spearman_p: 0.0568\n        partial_r_ctrl_logfreq: -0.1428\n        partial_p: 0.2641\n      quartile_comparison:\n        low_bcs_cutoff: 0.798\n        high_bcs_cutoff: 0.827\n        low_bcs_f1: 0.3098\n        high_bcs_f1: 0.2275\n        delta_f1: -0.0823\n        low_bcs_freq: 2134\n        high_bcs_freq: 2049\n      confound_check:\n        bcs_vs_logfreq_r: 0.042\n        bcs_vs_logfreq_p: 0.74\n        logfreq_vs_f1_r: 0.25\n        logfreq_vs_f1_p: 0.048\n      verdict: Direction supports hypothesis. Spearman significant (p=0.02). Frequency\n        confound absent at type level (r=0.04).\n    overall_verdict: PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE\n      STRONG PASS, PER-TYPE DIRECTIONAL PASS\n- id: exp-003a\n  claim:\n  - 1\n  - 2\n  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination\n    instruction. Re-run exp1+exp2.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp003a_prompt_v2_rerun\n  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_mode: text_match\n    exp1_text_match:\n      count_1:\n        f1: 0.323\n        precision: 0.216\n        recall: 0.641\n        pred_gold_ratio: 2.97\n        n_batches: 64\n      count_2:\n        f1: 0.273\n        precision: 0.18\n        recall: 0.56\n        pred_gold_ratio: 3.11\n        n_batches: 5\n      count_6:\n        f1: 0.306\n        precision: 0.226\n        recall: 0.475\n        pred_gold_ratio: 2.1\n        n_batches: 5\n      count_12:\n        f1: 0.347\n        precision: 0.367\n        recall: 0.329\n        pred_gold_ratio: 0.9\n        n_batches: 5\n      count_22:\n        f1: 0.299\n        precision: 0.339\n        recall: 0.267\n        pred_gold_ratio: 0.79\n        n_batches: 5\n      count_44:\n        f1: 0.445\n        precision: 0.506\n        recall: 0.396\n        pred_gold_ratio: 0.78\n        n_batches: 5\n      count_64:\n        f1: 0.414\n        precision: 0.648\n        recall: 0.304\n        pred_gold_ratio: 0.47\n        n_batches: 5\n    exp2_text_match:\n      count_6:\n        f1: 0.32\n        precision: 0.26\n        recall: 0.416\n        pred_gold_ratio: 1.6\n        n_batches: 27\n      count_12:\n        f1: 0.306\n        precision: 0.291\n        recall: 0.323\n        pred_gold_ratio: 1.11\n        n_batches: 27\n    vs_exp001_delta:\n      count_1:\n        f1_delta: +0.139 (+76%)\n        precision_delta: +0.111 (+106%)\n        recall_delta: -0.079 (-11%)\n        overpred_fix: 6.85→2.97\n      count_6:\n        f1_delta: +0.151 (+97%)\n        precision_delta: +0.138 (+157%)\n        recall_delta: -0.145 (-23%)\n      count_12:\n        f1_delta: +0.101 (+41%)\n        precision_delta: +0.207 (+129%)\n        recall_delta: -0.210 (-39%)\n      count_44:\n        f1_delta: -0.028 (-6%)\n        precision_delta: +0.092 (+22%)\n        recall_delta: -0.155 (-28%)\n      count_64:\n        f1_delta: -0.049 (-11%)\n        precision_delta: +0.128 (+25%)\n        recall_delta: -0.114 (-27%)\n    key_finding: 'V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x\n      to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1).\n      But over-corrected at high counts: under-prediction (pred/gold<1) caused recall\n      drops of 27-39%, slightly lowering F1 at count_22-64.'\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MAVEN confusability study: count curve + within-count BCS correlation\n    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core\n    finding cross-task (NER→ED) with larger type space and known sibling confusion\n    (14.6-19.8%).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp-004\n  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs\n    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy\n    structure.'\n  status: DONE\n  conclusion: success\n  metrics:\n    n_event_types: 168\n    n_pairs: 14028\n    scs_mean: 0.2161\n    scs_std: 0.103\n    scs_max: 0.8368\n    scs_median: 0.2121\n    scs_q90: 0.3457\n    scs_q95: 0.3892\n    pairs_above_0.5: 119\n    pct_above_0.5: 0.85\n    train_docs: 2913\n    train_mentions: 77993\n    valid_docs: 710\n    valid_mentions: 18904\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n  status: planned\n- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n  status: planned\n- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.\n  status: planned\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional\n    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model\n    generalizability.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-003a\n  registry_id: exp012_llama_8b_r3\n  status: DONE\n  conclusion: failed\n- id: exp-016\n  claim:\n  - 1\n  - 2\n  description: 'FewRel cross-task replication: count curve + BCS correlation on FewRel\n    RE (80 relation types with --use_all). Replicates confusability effect NER→RE.\n    Pilot (fewrel_pilot) confirmed signal; formal run with full count curve [1,4,8,16,32,64,80].'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp_fewrel_formal\n  status_note: RUNNING (16-rel version). Will rerun with --use_all for 80-rel full\n    count curve after current run completes.\n  status: DONE\n  conclusion: success\n  metrics:\n    note: 16-rel sanity check only\n    exp1:\n      count_1:\n        mean_acc: 0.904\n        n_batches: 16\n      count_4:\n        mean_acc: 0.932\n        n_batches: 5\n      count_8:\n        mean_acc: 0.867\n        n_batches: 5\n      count_16:\n        mean_acc: 0.778\n        n_batches: 5\n        bcs: 0.9\n        zero_variance: true\n    exp2:\n      count_8_low_bcs:\n        acc: 0.889\n        bcs: 0.782\n      count_8_high_bcs:\n        acc: 0.798\n        bcs: 0.892\n      delta_bcs_effect: -0.091\n    trend: 'count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8%\n      (Δ=-9.1pp)'\n- id: exp-008\n  claim:\n  - 3\n  description: 'SDGD-zero on Few-NERD: confusability-minimizing batch composition\n    via embedding SCS + graph coloring. Compare vs single-pass full-schema baseline.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-003a\n  registry_id: exp008_sdgd_v2_fewnerd\n  status_note: 'DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass\n    baseline on Few-NERD. R1 (exp008_sdgd_zero_fewnerd) failed with script error.'\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 79\n    random_batch:\n      f1: 0.3007\n      precision: 0.3307\n      recall: 0.2758\n      batches: 8\n      time_s: 494\n    sdgd_zero:\n      f1: 0.2407\n      precision: 0.3244\n      recall: 0.1913\n      batches: 4\n      time_s: 261\n    per_type: killed before completion (3/4 modes done, Director approved kill)\n    vs_v1: confidence-gated merge did not improve over union merge. sdgd_zero 0.241\n      vs v1 0.251, random_batch 0.301 vs v1 0.320\n    key_finding: SDGD v2 confidence-gated merge + min_batch_size=8 failed to beat\n      single_pass baseline (F1=0.445). Both v1 and v2 confirm decomposition hurts\n      precision more than it helps recall. Claim 3 (SDGD framework) needs fundamental\n      rethink.\n- id: exp-009\n  claim:\n  - 3\n  description: 'SDGD-zero on MAVEN: confusability-minimizing batch composition on\n    168 event types. Compare vs single-pass + random batching. Cross-task validation\n    of SDGD framework (NER→ED).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-004\n  - exp-008\n  status: planned\n- id: exp-010\n  claim:\n  - 3\n  description: 'SDGD-cal on Few-NERD: empirical confusability from 5-10 calibration\n    examples (no gradients). Compare vs SDGD-zero.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-008\n  status: planned\n- id: exp-011\n  claim:\n  - 3\n  description: 'SDGD-cal on MAVEN: empirical confusability with calibration on 168\n    event types. Full comparison table.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-009\n  - exp-010\n  status: planned\n- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n  status: planned\n- id: exp-014\n  claim:\n  - 3\n  description: 'Ablation: per-type splitting (UniNER-style, 1 type per batch). Upper\n    bound on decomposition benefit. Reveals latency vs quality tradeoff.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n  status: planned\n- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp001_count_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    diagnosis: char offset 96.5% fabricated by model\n    text_match_reeval:\n      count_1:\n        f1: 0.184\n        precision: 0.105\n        recall: 0.72\n        pred_gold_ratio: 6.85\n      count_2:\n        f1: 0.123\n        precision: 0.068\n        recall: 0.698\n        pred_gold_ratio: 10.33\n      count_6:\n        f1: 0.155\n        precision: 0.088\n        recall: 0.62\n        pred_gold_ratio: 7.02\n      count_12:\n        f1: 0.246\n        precision: 0.16\n        recall: 0.539\n        pred_gold_ratio: 3.38\n      count_22:\n        f1: 0.322\n        precision: 0.232\n        recall: 0.527\n        pred_gold_ratio: 2.27\n      count_44:\n        f1: 0.473\n        precision: 0.414\n        recall: 0.551\n        pred_gold_ratio: 1.33\n      count_64:\n        f1: 0.463\n        precision: 0.52\n        recall: 0.418\n        pred_gold_ratio: 0.8\n    key_finding: recall monotonically decreases (0.72→0.42), precision monotonically\n      increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at\n      count_44\n    wrong_type_trend: 'type confusion increases with count: 0→2434, supports confusability\n      hypothesis'\n    spurious_dominant: spurious FPs (text in source but not entity) dominate at low\n      count, not hallucination\n    conclusion_text_match: F1 curve inversion caused by over-prediction confound,\n      NOT absence of confusability effect. Recall curve + type confusion pattern support\n      hypothesis.\n- exp_id: exp002_confusability_controlled\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp2_reeval_results.json (text_match, CLEAN)\n    primary_recall_vs_bcs:\n      count_6:\n        r: 0.2754\n        p: 0.1644\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.2219\n        p: 0.266\n        n: 27\n        verdict: FAIL\n      partial:\n        r: 0.2522\n        p: 0.0658\n        n: 54\n        verdict: FAIL\n    secondary_f1_vs_bcs:\n      count_6:\n        r: 0.1754\n        p: 0.3814\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.5012\n        p: 0.0077\n        n: 27\n        verdict: PASS\n      partial:\n        r: 0.3025\n        p: 0.0262\n        n: 54\n        verdict: PASS\n    mechanistic_confusion_rate:\n      random_batches:\n        count_6_high: 0.0157\n        count_6_low: 0.0088\n        ratio_6: 1.7\n        count_12_high: 0.0304\n        count_12_low: 0.0131\n        ratio_12: 2.4\n      extreme_batches:\n        count_6_high: 0.0728\n        count_6_low: 0.0014\n        ratio_6: 27.5\n        count_12_high: 0.048\n        count_12_low: 0.0061\n        ratio_12: 9.9\n      verdict: PASS\n    pairwise_confusion_analysis:\n      all:\n        n_pairs: 1953\n        pearson_r: 0.156\n        pearson_p: 4.6e-12\n        spearman_rho: 0.16\n        spearman_p: 1.3e-12\n      count_6:\n        n_pairs: 1770\n        pearson_r: 0.078\n        pearson_p: 0.001\n      count_12:\n        n_pairs: 1953\n        pearson_r: 0.147\n        pearson_p: 6.7e-11\n      nonzero_only:\n        all_spearman_rho: 0.254\n        all_spearman_p: 1.1e-06\n        count_12_pearson_r: 0.212\n        count_12_p: 0.00034\n      top_confused_pair: person-other <-> person-politician (BCS=0.934, confusion=156)\n    per_type_analysis:\n      n_types: 63\n      filter: freq>=5\n      micro_f1_vs_bcs:\n        pearson_r: -0.1828\n        pearson_p: 0.1516\n        spearman_rho: -0.2927\n        spearman_p: 0.0199\n        partial_r_ctrl_logfreq: -0.1998\n        partial_p: 0.1163\n      mean_f1_vs_bcs:\n        pearson_r: -0.1374\n        pearson_p: 0.283\n        spearman_rho: -0.2412\n        spearman_p: 0.0568\n        partial_r_ctrl_logfreq: -0.1428\n        partial_p: 0.2641\n      quartile_comparison:\n        low_bcs_cutoff: 0.798\n        high_bcs_cutoff: 0.827\n        low_bcs_f1: 0.3098\n        high_bcs_f1: 0.2275\n        delta_f1: -0.0823\n        low_bcs_freq: 2134\n        high_bcs_freq: 2049\n      confound_check:\n        bcs_vs_logfreq_r: 0.042\n        bcs_vs_logfreq_p: 0.74\n        logfreq_vs_f1_r: 0.25\n        logfreq_vs_f1_p: 0.048\n      verdict: Direction supports hypothesis. Spearman significant (p=0.02). Frequency\n        confound absent at type level (r=0.04).\n    overall_verdict: PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE\n      STRONG PASS, PER-TYPE DIRECTIONAL PASS\n- exp_id: exp003a_prompt_v2_rerun\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_mode: text_match\n    exp1_text_match:\n      count_1:\n        f1: 0.323\n        precision: 0.216\n        recall: 0.641\n        pred_gold_ratio: 2.97\n        n_batches: 64\n      count_2:\n        f1: 0.273\n        precision: 0.18\n        recall: 0.56\n        pred_gold_ratio: 3.11\n        n_batches: 5\n      count_6:\n        f1: 0.306\n        precision: 0.226\n        recall: 0.475\n        pred_gold_ratio: 2.1\n        n_batches: 5\n      count_12:\n        f1: 0.347\n        precision: 0.367\n        recall: 0.329\n        pred_gold_ratio: 0.9\n        n_batches: 5\n      count_22:\n        f1: 0.299\n        precision: 0.339\n        recall: 0.267\n        pred_gold_ratio: 0.79\n        n_batches: 5\n      count_44:\n        f1: 0.445\n        precision: 0.506\n        recall: 0.396\n        pred_gold_ratio: 0.78\n        n_batches: 5\n      count_64:\n        f1: 0.414\n        precision: 0.648\n        recall: 0.304\n        pred_gold_ratio: 0.47\n        n_batches: 5\n    exp2_text_match:\n      count_6:\n        f1: 0.32\n        precision: 0.26\n        recall: 0.416\n        pred_gold_ratio: 1.6\n        n_batches: 27\n      count_12:\n        f1: 0.306\n        precision: 0.291\n        recall: 0.323\n        pred_gold_ratio: 1.11\n        n_batches: 27\n    vs_exp001_delta:\n      count_1:\n        f1_delta: +0.139 (+76%)\n        precision_delta: +0.111 (+106%)\n        recall_delta: -0.079 (-11%)\n        overpred_fix: 6.85→2.97\n      count_6:\n        f1_delta: +0.151 (+97%)\n        precision_delta: +0.138 (+157%)\n        recall_delta: -0.145 (-23%)\n      count_12:\n        f1_delta: +0.101 (+41%)\n        precision_delta: +0.207 (+129%)\n        recall_delta: -0.210 (-39%)\n      count_44:\n        f1_delta: -0.028 (-6%)\n        precision_delta: +0.092 (+22%)\n        recall_delta: -0.155 (-28%)\n      count_64:\n        f1_delta: -0.049 (-11%)\n        precision_delta: +0.128 (+25%)\n        recall_delta: -0.114 (-27%)\n    key_finding: 'V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x\n      to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1).\n      But over-corrected at high counts: under-prediction (pred/gold<1) caused recall\n      drops of 27-39%, slightly lowering F1 at count_22-64.'\n- exp_id: exp-004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_event_types: 168\n    n_pairs: 14028\n    scs_mean: 0.2161\n    scs_std: 0.103\n    scs_max: 0.8368\n    scs_median: 0.2121\n    scs_q90: 0.3457\n    scs_q95: 0.3892\n    pairs_above_0.5: 119\n    pct_above_0.5: 0.85\n    train_docs: 2913\n    train_mentions: 77993\n    valid_docs: 710\n    valid_mentions: 18904\n- exp_id: exp004_maven_bcs\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    exp1_count_curve:\n      count_1:\n        n_batches: 64\n        exact_f1: 0.009\n        relaxed_f1: 0.106\n        bcs: 0\n      count_6:\n        n_batches: 5\n        exact_f1: 0.003\n        relaxed_f1: 0.103\n        bcs: 0.892\n      count_12:\n        n_batches: 5\n        exact_f1: 0.008\n        relaxed_f1: 0.146\n        bcs: 0.921\n      count_22:\n        n_batches: 5\n        exact_f1: 0.013\n        relaxed_f1: 0.185\n        bcs: 0.933\n      count_44:\n        n_batches: 5\n        exact_f1: 0.018\n        relaxed_f1: 0.247\n        bcs: 0.967\n      count_64:\n        n_batches: 5\n        exact_f1: 0.013\n        relaxed_f1: 0.245\n        bcs: 0.973\n    exp2_bcs_controlled:\n      count_6_high_bcs:\n        exact_f1: 0.0354\n        relaxed_f1: 0.211\n        bcs: 0.9447\n      count_6_low_bcs:\n        exact_f1: 0.0068\n        relaxed_f1: 0.089\n        bcs: 0.8709\n      count_12_high_bcs:\n        exact_f1: 0.0151\n        relaxed_f1: 0.1568\n        bcs: 0.9447\n      count_12_low_bcs:\n        exact_f1: 0.0068\n        relaxed_f1: 0.105\n        bcs: 0.9148\n    key_finding: 'MAVEN batch-level: high_bcs relaxed_F1 2.4x vs low_bcs (count_6).\n      Direction same as Few-NERD batch-level (positive). Pairwise + per-type analysis\n      needed to control frequency confound.'\n    note: exact_F1 very low (0.003-0.035), relaxed_F1 usable (0.089-0.247). Event\n      trigger boundary matching is fuzzy. A re-run (500 samples) is still in progress\n      in artifacts/exp004/.\n- exp_id: fewrel_pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    embedding: all-MiniLM-L6-v2\n    n_batches: 15\n    n_predictions: 374\n    count_4:\n      low_bcs_acc: 0.917\n      high_bcs_acc: 0.708\n      delta_pp: -20.9\n      low_bcs: 0.42\n      high_bcs: 0.97\n    count_8:\n      low_bcs_acc: 1\n      high_bcs_acc: 0.5\n      delta_pp: -50\n      low_bcs: 0.47\n      high_bcs: 0.97\n    count_16:\n      low_bcs_acc: 0.917\n      high_bcs_acc: 0.431\n      delta_pp: -48.6\n      low_bcs: 0.57\n      high_bcs: 0.97\n    key_finding: 'BCS-accuracy strong negative: high-BCS batches 43-71% vs low-BCS\n      92-100%. Effect increases with count. Cross-task (NER→RE) replication of confusability\n      hypothesis.'\n- exp_id: exp008_sdgd_zero_fewnerd\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp008_sdgd_zero_fewnerd_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 77.3\n    sdgd_zero:\n      f1: 0.2514\n      precision: 0.2096\n      recall: 0.3141\n      batches: 8\n      time_s: 408.7\n    random_batch:\n      f1: 0.3197\n      precision: 0.2491\n      recall: 0.4462\n      batches: 8\n      time_s: 476.1\n    per_type:\n      f1: 0.2915\n      precision: 0.194\n      recall: 0.5856\n      batches: 66\n      time_s: 2532.2\n    key_finding: All decomposition modes F1 < single_pass. Decomposition boosts recall\n      but kills precision (merge amplification). sdgd_zero worst F1, even below random_batch.\n- exp_id: exp_fewrel_formal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: 16-rel sanity check only\n    exp1:\n      count_1:\n        mean_acc: 0.904\n        n_batches: 16\n      count_4:\n        mean_acc: 0.932\n        n_batches: 5\n      count_8:\n        mean_acc: 0.867\n        n_batches: 5\n      count_16:\n        mean_acc: 0.778\n        n_batches: 5\n        bcs: 0.9\n        zero_variance: true\n    exp2:\n      count_8_low_bcs:\n        acc: 0.889\n        bcs: 0.782\n      count_8_high_bcs:\n        acc: 0.798\n        bcs: 0.892\n      delta_bcs_effect: -0.091\n    trend: 'count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8%\n      (Δ=-9.1pp)'\n- exp_id: exp_fewrel_formal_80rel\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_count_curve:\n      count_1:\n        acc: 0.8573\n        n_batches: 80\n        bcs: 0\n      count_4:\n        acc: 0.8667\n        n_batches: 5\n        bcs: 0.6335\n      count_8:\n        acc: 0.8021\n        n_batches: 5\n        bcs: 0.7175\n      count_16:\n        acc: 0.6958\n        n_batches: 5\n        bcs: 0.795\n      count_32:\n        acc: 0.6578\n        n_batches: 5\n        bcs: 0.8893\n      count_64:\n        acc: 0.5424\n        n_batches: 5\n        bcs: 0.9434\n      count_80:\n        acc: 0.5042\n        n_batches: 5\n        bcs: 0.9706\n    exp2_bcs_controlled:\n      count_8:\n        low_bcs_acc: 0.8229\n        low_bcs: 0.4715\n        high_bcs_acc: 0.5104\n        high_bcs: 0.9706\n        random_acc: 0.8025\n        delta_pp: -31.2\n      count_16:\n        low_bcs_acc: 0.8281\n        low_bcs: 0.5705\n        high_bcs_acc: 0.5156\n        high_bcs: 0.9706\n        random_acc: 0.7169\n        delta_pp: -31.2\n    vs_16rel:\n      degradation_16rel: -12.6pp (0.904→0.778)\n      degradation_80rel: -35.3pp (0.857→0.504)\n      bcs_effect_16rel: -9.1pp\n      bcs_effect_80rel: -31.2pp\n      amplification: 3.4x\n    key_finding: 80-rel count curve 0.857→0.504 (degradation 35.3pp, 远强于 16-rel 12.6pp).\n      BCS effect -31.2pp (3.4x amplification vs 16-rel). 更多 relations → 更大 confusion\n      space → 更强 degradation + BCS effect.\n- exp_id: exp008_sdgd_v2_fewnerd\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 79\n    random_batch:\n      f1: 0.3007\n      precision: 0.3307\n      recall: 0.2758\n      batches: 8\n      time_s: 494\n    sdgd_zero:\n      f1: 0.2407\n      precision: 0.3244\n      recall: 0.1913\n      batches: 4\n      time_s: 261\n    per_type: killed before completion (3/4 modes done, Director approved kill)\n    vs_v1: confidence-gated merge did not improve over union merge. sdgd_zero 0.241\n      vs v1 0.251, random_batch 0.301 vs v1 0.320\n    key_finding: SDGD v2 confidence-gated merge + min_batch_size=8 failed to beat\n      single_pass baseline (F1=0.445). Both v1 and v2 confirm decomposition hurts\n      precision more than it helps recall. Claim 3 (SDGD framework) needs fundamental\n      rethink.\n- exp_id: exp012_llama_fewnerd\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp007_error_taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_random:\n      bcs_zero:\n        n_fp: 6172\n        intra_sub_pct: 0\n        extra_sub_pct: 90.3\n        intra_sub_per_100_gold: 0\n      bcs_low:\n        n_fp: 2231\n        intra_sub_pct: 1.6\n        extra_sub_pct: 89.9\n        intra_sub_per_100_gold: 3.4\n      bcs_medium:\n        n_fp: 3843\n        intra_sub_pct: 10.6\n        extra_sub_pct: 78.1\n        intra_sub_per_100_gold: 6.47\n      bcs_high:\n        n_fp: 6188\n        intra_sub_pct: 49.4\n        extra_sub_pct: 30.8\n        intra_sub_per_100_gold: 12.93\n    correlation:\n      intra_sub_vs_bcs_spearman_rho: 1\n      intra_sub_vs_bcs_p: <0.001\n      chi_square: 6952\n      chi_square_p: ~0\n    exp2_controlled:\n      trend: IntraSub 3.2% -> 7.3% -> 8.6% (rho=1.0, p<0.001)\n    key_finding: 'BCS>=0.95: 49.4% FP are intra-batch type confusion (13/100 gold).\n      Hallucination+boundary <3%. LLM main error mode is type confusion, not hallucination.'\n- exp_id: exp012_llama_fewnerd_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp016_fewrel_error_taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    error_distribution:\n      zero_bcs:\n        bcs_mean: 0\n        correct_pct: 85.73\n        wrong_type_pct: 0\n        intra_sub_pct: 0\n        missed_pct: 14.27\n      low_bcs:\n        bcs_mean: 0.565\n        correct_pct: 85.42\n        wrong_type_pct: 4.17\n        intra_sub_pct: 4.17\n        missed_pct: 10.42\n      medium_bcs:\n        bcs_mean: 0.729\n        correct_pct: 75.7\n        wrong_type_pct: 13\n        intra_sub_pct: 13\n        missed_pct: 11.3\n      high_bcs:\n        bcs_mean: 0.86\n        correct_pct: 66.67\n        wrong_type_pct: 20.28\n        intra_sub_pct: 20.28\n        missed_pct: 13.05\n      very_high_bcs:\n        bcs_mean: 0.971\n        correct_pct: 52.03\n        wrong_type_pct: 32.25\n        intra_sub_pct: 32.25\n        missed_pct: 15.71\n    correlations:\n      intra_sub_vs_bcs_spearman: 0.9539\n      intra_sub_vs_bcs_p: <1e-6\n      accuracy_vs_bcs_spearman: -0.5821\n      accuracy_vs_bcs_p: <1e-6\n    cross_task:\n      ner_intra_sub_vs_bcs_rho: 1\n      re_intra_sub_vs_bcs_rho: 0.9539\n    key_finding: 100% of type confusion in RE is intra-batch (model only predicts\n      from schema). IntraSub vs BCS ρ=0.954 confirms NER finding. Missed rate flat\n      (10-16%), BCS drives confusion not detection failure.\n- exp_id: bootstrap_ci_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fewnerd_pairwise_r:\n      point: 0.112\n      ci_lower: 0.076\n      ci_upper: 0.156\n      n: 1953\n      note: point estimate 0.112 vs old 0.156 — re-run confirmed current value\n    maven_minilm_pairwise_r:\n      point: 0.129\n      ci_lower: 0.104\n      ci_upper: 0.156\n      n: 11026\n    fewrel_count8_delta_pp:\n      point: 31.2\n      ci_lower: 17.7\n      ci_upper: 42.7\n      n: 96+96\n    fewrel_count16_delta_pp:\n      point: 31.2\n      ci_lower: 22.9\n      ci_upper: 39.6\n      n: 192+192\n    fewnerd_pertype_rho:\n      point: -0.293\n      ci_lower: -0.492\n      ci_upper: -0.054\n      n: 63\n    confusion_ratio_count6:\n      point: 25.3\n      ci_lower: 6.1\n      ci_upper: 60.5\n    confusion_ratio_count12:\n      point: 21.2\n      ci_lower: 5.3\n      ci_upper: 52.2\n    key_finding: All CIs exclude null (0 for correlations, 1 for ratios). All effects\n      are directionally robust at 95% level.\n- exp_id: exp015_scs_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    all_pairs:\n      n: 1953\n      n_nonzero: 216\n      qwen3_spearman: 0.1682\n      qwen3_spearman_p: '7.3e-14'\n      qwen3_kendall: 0.1351\n      minilm_spearman: 0.1439\n      minilm_spearman_p: '1.7e-10'\n      minilm_kendall: 0.1152\n    nonzero_only:\n      n: 216\n      qwen3_spearman: 0.2722\n      qwen3_spearman_p: '5.0e-05'\n      qwen3_kendall: 0.2001\n      minilm_spearman: 0.306\n      minilm_spearman_p: '4.6e-06'\n      minilm_kendall: 0.2276\n    key_finding: Both embeddings significantly predict confusion (all p<1e-5). Qwen3\n      better overall (rho=0.168), MiniLM better on nonzero pairs (rho=0.306). SCS\n      is a valid but partial proxy — context, frequency, mention ambiguity also matter.\n- exp_id: exp012_llama_fewnerd_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_8b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_fewrel_40rel\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_awq\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp012_llama_fewnerd_r4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_8b_fewnerd\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_fewrel_40rel_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_fewrel_40rel_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_8b_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_llama_recall_count1: 0.702\n    exp1_llama_recall_count64: 0.273\n    exp1_recall_decline_pp: -42.9\n    exp1_per_batch_recall_corr_vs_qwen: 0.7249\n    exp1_llama_text_match_f1_range: 0.06-0.36\n    exp1_exact_f1: 0\n    exp1_note: exact/relaxed F1=0 due to missing char offsets, text_match is correct\n      metric\n- exp_id: exp012_llama_8b_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006_interaction_2x2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    cell_means_f1:\n      low_count_low_bcs: 0.324\n      low_count_high_bcs: 0.313\n      high_count_low_bcs: 0.325\n      high_count_high_bcs: 0.277\n    main_effects:\n      count: -0.018\n      bcs: -0.029\n    interaction:\n      estimate: -0.036\n      z: -0.667\n      p: 0.505\n      bcs_effect_at_low_count: -0.011\n      bcs_effect_at_high_count: -0.048\n    verdict: 交互方向符合 multiplicative 假设但统计不显著 (p=0.505)，未检测到显著交互效应\n- exp_id: exp012_llama_8b_r2_exp2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_fewrel_40rel_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_acc_count1: 0.858\n    exp1_acc_count4: 0.867\n    exp1_acc_count8: 0.802\n    exp1_acc_count16: 0.697\n    exp1_acc_count32: 0.658\n    exp1_acc_count40: 0.588\n    exp1_decline_pp: -27\n    exp2_bcs_delta_count8: 0.333\n    exp2_bcs_delta_count16: 0.318\n    exp2_low_bcs_acc_count8: 0.833\n    exp2_high_bcs_acc_count8: 0.5\n    exp2_low_bcs_acc_count16: 0.818\n    exp2_high_bcs_acc_count16: 0.5\n- exp_id: exp012_llama_fewrel_ch2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp2_bcs_controlled:\n      count_8:\n        low_bcs_acc: 0.7812\n        high_bcs_acc: 0.5104\n        delta_pp: -27.1\n      count_16:\n        low_bcs_acc: 0.7552\n        high_bcs_acc: 0.5156\n        delta_pp: -24\n    overall_correlation:\n      n_batches: 54\n      pearson_r: -0.39\n      pearson_p: 0.004\n      spearman_rho: -0.43\n      spearman_p: 0.001\n    cross_model_comparison:\n      llama_delta_pp: -27.1\n      qwen3_delta_pp: -31.2\n      ratio: 0.87\n      note: LLaMA effect = 87% of Qwen3, direction and magnitude consistent\n    no_floor_effect: true\n    mean_accuracy: 0.77\n    accuracy_range: 0.41-0.98\n    key_finding: 'BCS confusability effect cross-model replicated: LLaMA Δ=-27.1pp\n      (87% of Qwen3 -31.2pp). Pearson r=-0.39 (p=0.004), Spearman ρ=-0.43 (p=0.001).\n      No floor effect.'\n- exp_id: exp_fewrel_16rel_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_batches: 100\n    pool_size: 16\n    batch_size: 8\n    bcs_range:\n    - 0.6532\n    - 0.9002\n    quartile_delta:\n      Q4_minus_Q1_pp: -5.31\n      ci_95_lower: -9.45\n      ci_95_upper: -4.49\n      note: CI values from pre-D038 bootstrap, may need re-verification with MEAN-based\n        BCS\n    pearson_r_bcs_acc: -0.467\n    regression_slope:\n      slope: -0.509\n      ci_95_lower: -0.556\n      ci_95_upper: -0.349\n      r_squared: 0.218\n      p_value: 1.01e-12\n      interpretation: per +0.1 BCS → -5.09pp accuracy\n      note: CI from pre-D038 bootstrap\n    amplification_ratio:\n      quartile_16_vs_80: 4.2\n      ci_95_lower: 3.3\n      ci_95_upper: 6.95\n    key_finding: '16-rel pool BCS effect (MEAN-based, D038): Δ(Q4-Q1)=-5.31pp, r=-0.467.\n      Regression slope=-0.509. Bootstrap 1000 resamples. [D038 MEAN correction applied,\n      old values: r=-0.637/Δ=-7.42pp/slope=-0.449]'\n- exp_id: exp_fewrel_16rel_100batch\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_fewrel_80pool_16sub_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_batches: 100\n    pool_size: 80-rel pool, 16-type subsamples\n    batch_size: 8\n    mean_accuracy: 0.8077\n    mean_bcs: 0.557\n    bcs_range:\n    - 0.4578\n    - 0.6836\n    quartile_delta:\n      Q4_minus_Q1_pp: -3.92\n      ci_95_lower: -7.79\n      ci_95_upper: 0.42\n    pearson_r_bcs_acc: -0.221\n    pearson_p: 0.027\n    regression_slope:\n      slope: -0.401\n      ci_95_lower: -0.684\n      ci_95_upper: -0.062\n      interpretation: per +0.1 BCS → -4.01pp accuracy\n    key_finding: '80-pool 16-sub BCS effect directional: Δ(Q4-Q1)=-3.92pp CI crosses\n      zero [-7.79,+0.42], but regression slope=-0.401 CI[-0.684,-0.062] excludes zero.\n      Effect weaker than independent 16-rel pool (Δ=-7.42pp) due to narrower BCS range.'\n- exp_id: exp_maven_residualized_bcs\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    minilm:\n      raw_rho: 0.208\n      raw_p: 0.011\n      confound: log_freq\n      bcs_confound_r: 0.201\n      partial_r: 0.133\n      partial_p: 0.107\n    qwen3:\n      raw_rho: 0.184\n      raw_p: 0.025\n      confound: degree_centrality_0.7\n      bcs_confound_r: 0.854\n      partial_r: 0.063\n      partial_p: 0.442\n    joint_control:\n      qwen3_p: 0.439\n      minilm_p: 0.226\n      note: Both n.s. after controlling log_freq + degree jointly\n    key_finding: MAVEN BCS-F1 positive correlation is centrality artifact. MiniLM\n      confound=frequency, Qwen3 confound=degree centrality (r=0.854). After joint\n      control, both correlations vanish. Confirms pairwise SCS remains valid but per-type\n      aggregation fails on homogeneous schemas.\n- exp_id: exp_fewrel_v2_bcs_controlled\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_bcs_mean_acc: 0.8042\n    high_bcs_mean_acc: 0.725\n    delta_low_minus_high_pp: 7.92\n    bootstrap_ci_95_lower_pp: -5.21\n    bootstrap_ci_95_upper_pp: 21.46\n    n_bootstrap: 10000\n    n_batches_per_group: 5\n    samples_per_batch: 96\n    total_inferences: 960\n- exp_id: exp_docred_confusability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_relation_types: 96\n    n_eval_samples: 1240\n    total_inferences: 13618\n    count_curve:\n      count_1: 0.88\n      count_4: 0.77\n      count_8: 0.774\n      count_16: 0.524\n      count_32: 0.521\n      count_64: 0.424\n      count_96: 0.387\n    bcs_effect_count16:\n      low_bcs_acc: 0.679\n      high_bcs_acc: 0.447\n      gap: 0.233\n      spearman_r: -0.661\n      slope: -0.713\n      slope_95ci:\n      - -0.909\n      - -0.529\n    bcs_effect_count32:\n      low_bcs_acc: 0.578\n      high_bcs_acc: 0.403\n      gap: 0.176\n      spearman_r: -0.509\n      slope: -0.69\n      slope_95ci:\n      - -0.854\n      - -0.519\n- exp_id: bcs_max_to_mean_fix\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: exp_confusability_batch_composition\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_fewrel_v2_n25\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    n_low: 25\n    n_high: 25\n    low_bcs_mean_acc: 0.8521\n    high_bcs_mean_acc: 0.5967\n    delta_pp: 25.54\n    ci_95:\n    - 22.42\n    - 28.62\n    permutation_p: 0\n    pearson_r: -0.919\n    low_bcs_range:\n    - 0.356\n    - 0.367\n    high_bcs_range:\n    - 0.791\n    - 0.811\n    key_finding: v2 prompt does NOT eliminate confusability effect. At n=25 with wider\n      BCS separation, effect is massive (25.5pp) and highly significant. Prior n=5\n      result (7.9pp, CI crosses zero) was underpowered + narrow BCS contrast.\n- exp_id: exp_cross_embedding_sensitivity\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    fewnerd_qwen3:\n      pearson_r: 0.138\n      pearson_p: 1.0e-09\n      spearman_rho: 0.168\n      spearman_p: 7.3e-14\n    fewnerd_minilm:\n      pearson_r: 0.172\n      pearson_p: 2.0e-14\n      spearman_rho: 0.144\n      spearman_p: 1.7e-10\n    fewrel_minilm:\n      slope: -0.485\n      r: -0.398\n      p: 0.04\n    fewrel_qwen3:\n      slope: -0.542\n      r: -0.185\n      p: 0.356\n      note: BCS range compression (std=0.034 vs MiniLM 0.081), directional but n.s.\n    key_finding: SCS-confusion signal robust to embedding choice (both significant\n      on Few-NERD). MiniLM better for BCS due to designed-for-similarity. Qwen3 causal-LM\n      embeddings compress BCS range.\n- exp_id: exp017_gpt4o_mini_fewrel\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T07:43:09.853Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T07:43:09.853Z",
  "sessionId": "c3c703d5-f588-4e67-b762-e7ebe9792a81"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T07:43:09.878Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：核心假设部分验证，部分 reviewer 质疑效应量或覆盖面，论文落入 EMNLP Findings 或需 rebuttal 挽救
核心假设：["A1 部分成立: Pairwise r=0.11-0.13 被质疑为'统计显著但实际意义有限'，需补充 FewRel 的大效应量（Δ=-31pp）来说服", 'A2 成立: Error taxonomy 证据清晰，无争议', 'A3 成立: Scaling 证据充分', 'A4 部分成立: Reviewers 指出 LLaMA 仅在 FewRel 成功，Few-NERD 多次失败是 generalizability 短板', 'A5 争议: 1-2 位 reviewer 视 MAVEN per-type 正方向为 counter-evidence，centrality confound 解释被要求补充定量验证', "A6 争议: 'No practical method' 被标记为主要弱点，SDGD 负面结果不足以弥补", 'A7 基本成立: 实证研究格式被接受，但被要求补充更强的 practical implications']
关键指标范围：{'arr_avg_score': [3.0, 3.5], 'claims_fully_supported': [1, 2], 'major_reviewer_weaknesses': [2, 3], 'cross_task_significant_replications': [2, 3], 'multi_model_effect_consistency': [0.7, 0.85], 'venue_probability_main': [0.15, 0.35], 'venue_probability_findings_or_above': [0.5, 0.7], 'rebuttal_flip_probability': [0.4, 0.65]}
叙事方向：需要调整 claim 强度和重心分配。"independently predicts" 软化为 "is associated with" 或 "contributes to predicting"。将 FewRel 的大效应量（Δ=-31pp, -27pp cross-model） 提升为 headline evidence，pairwise r=0.11-0.13 降级为 supplementary cross-task validation。 Claim 2（multi-channel）保持不变，error taxonomy 是最无争议的证据。 补充一个 "practitioner guideline" 小节：基于发现给出 schema 设计的具体建议 （e.g., 避免 BCS>0.8 的类型同批出现），弥补没有可用方法的短板。 MAVEN centrality confound 可能需要追加 synthetic schema 实验来定量验证聚合失效条件。 Rebuttal 重点: (1) effect size 在 IE 任务中的合理性论证, (2) LLaMA NER 失败的技术原因 (模型输出格式问题而非假设不成立), (3) 补充 1-2 个 reviewer 要求的分析。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: schema-dag-extraction

## paper_framing.md

# Paper Framing — schema-dag-extraction

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25 cycle)
- Commitment deadline: August 2, 2026
- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)
- Deadline: ARR May 25, 2026 (10 days from today)

## Core Claims (2 claims) — Revised per D019

1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.

2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.

~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — "why naive decomposition fails" is itself a contribution.

## Story Spine — Revised per D012

- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.

- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.

- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.

- **Three-task validation**:
  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio
  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel
  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)

- **Headline result template**: "Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid."

## Core Insight — Multi-Channel Degradation + Pairwise Robustness

Schema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:
- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.
- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.

These channels are orthogonal and independently addressable.

**Pairwise vs Aggregated Confusability**:
- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).
- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.
- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.

## Evidence Hierarchy (D012)

### Tier 1: PRIMARY — Pairwise SCS → Confusion

The cleanest evidence. Directly measures: are semantically similar type pairs more often confused?

**Few-NERD (NER)** — Qwen3 embeddings:
- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation
- Nonzero-only Spearman ρ=0.272 (p=5e-5)
- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)
- Immune to type frequency confound (operates at type-pair level)

**MAVEN (ED)** — MiniLM embeddings:
- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap
- Nonzero-only Spearman ρ=+0.191 (p<0.001)
- Cross-task replication on same-domain schema
- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas

### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication

Large effect size, cross-task (RE), scaling with schema complexity:

**Formal 80-rel study** (exp_fewrel_formal_80rel):
- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97
- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)
- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)
- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)

**16-rel sanity check** (exp_fewrel_formal):
- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)

**Pilot extreme batches** (fewrel_pilot, MiniLM):
- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp

Key insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling

### Tier 3: SUPPORTING — Few-NERD Per-type Analysis

Bridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:
- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings
- Partial r=-0.200 (p=0.116) controlling for log-frequency
- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)
- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)
- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal

### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound

Methodological case study on when aggregated confusability measures fail:
- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction
- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation
- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure
- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)
- This is stronger than "domain boundary" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition

### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)

IntraSub rate monotonically increases with BCS on both NER and RE:

**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0
**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)
- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon
- Same mechanism, different absolute magnitudes — consistent with cross-task expectations

Additional from extreme batch design:
- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS
- Random batches: 1.7-2.4x ratio (still significant, smaller effect)

## Embedding Ablation (D010)

2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}

### Per-type (Layer 2)
| | Few-NERD | FewRel | MAVEN |
|---|---|---|---|
| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |
| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |

### Pairwise (Layer 1)
| | Few-NERD | MAVEN |
|---|---|---|
| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |
| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |

### SCS→Empirical Confusion Validation (exp-015 fast)
| | Qwen3 | MiniLM |
|---|---|---|
| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |
| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |

**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.

## Venue Fit Risks

- **"Just an empirical study"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels "Lost in the Middle" (TACL 2024).
- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.
- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).
- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.
- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.

## Anticipated Reviewer Concerns

| Concern | Response Strategy | Experiment |
|---------|------------------|------------|
| Only one model | LLaMA-3.3-70B replication | exp-012 |
| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |
| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |
| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |
| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |
| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |
| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |
| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |
| Latency overhead | Report API calls and wall-clock time | exp-008 |


## experiment_plan (with registry status)

- id: exp-001
  claim:
  - 1
  - 2
  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]
    on Few-NERD with Qwen3-32B-FP8'
  priority: P0
  gpu_budget_hours: 3.5
  deps: []
  registry_id: exp001_count_baseline
  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction
    at low counts.
  status: DONE
  conclusion: success
  metrics:
    diagnosis: char offset 96.5% fabricated by model
    text_match_reeval:
      count_1:
        f1: 0.184
        precision: 0.105
        recall: 0.72
        pred_gold_ratio: 6.85
      count_2:
        f1: 0.123
        precision: 0.068
        recall: 0.698
        pred_gold_ratio: 10.33
      count_6:
        f1: 0.155
        precision: 0.088
        recall: 0.62
        pred_gold_ratio: 7.02
      count_12:
        f1: 0.246
        precision: 0.16
        recall: 0.539
        pred_gold_ratio: 3.38
      count_22:
        f1: 0.322
        precision: 0.232
        recall: 0.527
        pred_gold_ratio: 2.27
      count_44:
        f1: 0.473
        precision: 0.414
        recall: 0.551
        pred_gold_ratio: 1.33
      count_64:
        f1: 0.463
        precision: 0.52
        recall: 0.418
        pred_gold_ratio: 0.8
    key_finding: recall monotonically decreases (0.72→0.42), precision monotonically
      increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at
      count_44
    wrong_type_trend: 'type confusion increases with count: 0→2434, supports confusability
      hypothesis'
    spurious_dominant: spurious FPs (text in source but not entity) dominate at low
      count, not hallucination
    conclusion_text_match: F1 curve inversion caused by over-prediction confound,
      NOT absence of confusability effect. Recall curve + type confusion pattern support
      hypothesis.
- id: exp-002
  claim:
  - 1
  - 2
  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,
    25 random + extreme batches on Few-NERD'
  priority: P0
  gpu_budget_hours: 3
  deps:
  - exp-001
  registry_id: exp002_confusability_controlled
  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion
    rate 10-28x.
  status: DONE
  conclusion: success
  metrics:
    data_source: exp2_reeval_results.json (text_match, CLEAN)
    primary_recall_vs_bcs:
      count_6:
        r: 0.2754
        p: 0.1644
        n: 27
        verdict: FAIL
      count_12:
        r: 0.2219
        p: 0.266
        n: 27
        verdict: FAIL
      partial:
        r: 0.2522
        p: 0.0658
        n: 54
        verdict: FAIL
    secondary_f1_vs_bcs:
      count_6:
        r: 0.1754
        p: 0.3814
        n: 27
        verdict: FAIL
      count_12:
        r: 0.5012
        p: 0.0077
        n: 27
        verdict: PASS
      partial:
        r: 0.3025
        p: 0.0262
        n: 54
        verdict: PASS
    mechanistic_confusion_rate:
      random_batches:
        count_6_high: 0.0157
        count_6_low: 0.0088
        ratio_6: 1.7
        count_12_high: 0.0304
        count_12_low: 0.0131
        ratio_12: 2.4
      extreme_batches:
        count_6_high: 0.0728
        count_6_low: 0.0014
        ratio_6: 27.5
        count_12_high: 0.048
        count_12_low: 0.0061
        ratio_12: 9.9
      verdict: PASS
    pairwise_confusion_analysis:
      all:
        n_pairs: 1953
        pearson_r: 0.156
        pearson_p: 4.6e-12
        spearman_rho: 0.16
        spearman_p: 1.3e-12
      count_6:
        n_pairs: 1770
        pearson_r: 0.078
        pearson_p: 0.001
      count_12:
        n_pairs: 1953
        pearson_r: 0.147
        pearson_p: 6.7e-11
      nonzero_only:
        all_spearman_rho: 0.254
        all_spearman_p: 1.1e-06
        count_12_pearson_r: 0.212
        count_12_p: 0.00034
      top_confused_pair: person-other <-> person-politician (BCS=0.934, confusion=156)
    per_type_analysis:
      n_types: 63
      filter: freq>=5
      micro_f1_vs_bcs:
        pearson_r: -0.1828
        pearson_p: 0.1516
        spearman_rho: -0.2927
        spearman_p: 0.0199
        partial_r_ctrl_logfreq: -0.1998
        partial_p: 0.1163
      mean_f1_vs_bcs:
        pearson_r: -0.1374
        pearson_p: 0.283
        spearman_rho: -0.2412
        spearman_p: 0.0568
        partial_r_ctrl_logfreq: -0.1428
        partial_p: 0.2641
      quartile_comparison:
        low_bcs_cutoff: 0.798
        high_bcs_cutoff: 0.827
        low_bcs_f1: 0.3098
        high_bcs_f1: 0.2275
        delta_f1: -0.0823
        low_bcs_freq: 2134
        high_bcs_freq: 2049
      confound_check:
        bcs_vs_logfreq_r: 0.042
        bcs_vs_logfreq_p: 0.74
        logfreq_vs_f1_r: 0.25
        logfreq_vs_f1_p: 0.048
      verdict: Direction supports hypothesis. Spearman significant (p=0.02). Frequency
        confound absent at type level (r=0.04).
    overall_verdict: PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE
      STRONG PASS, PER-TYPE DIRECTIONAL PASS
- id: exp-003a
  claim:
  - 1
  - 2
  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination
    instruction. Re-run exp1+exp2.'
  priority: P0
  gpu_budget_hours: 3
  deps:
  - exp-001
  - exp-002
  registry_id: exp003a_prompt_v2_rerun
  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.
  status: DONE
  conclusion: success
  metrics:
    eval_mode: text_match
    exp1_text_match:
      count_1:
        f1: 0.323
        precision: 0.216
        recall: 0.641
        pred_gold_ratio: 2.97
        n_batches: 64
      count_2:
        f1: 0.273
        precision: 0.18
        recall: 0.56
        pred_gold_ratio: 3.11
        n_batches: 5
      count_6:
        f1: 0.306
        precision: 0.226
        recall: 0.475
        pred_gold_ratio: 2.1
        n_batches: 5
      count_12:
        f1: 0.347
        precision: 0.367
        recall: 0.329
        pred_gold_ratio: 0.9
        n_batches: 5
      count_22:
        f1: 0.299
        precision: 0.339
        recall: 0.267
        pred_gold_ratio: 0.79
        n_batches: 5
      count_44:
        f1: 0.445
        precision: 0.506
        recall: 0.396
        pred_gold_ratio: 0.78
        n_batches: 5
      count_64:
        f1: 0.414
        precision: 0.648
        recall: 0.304
        pred_gold_ratio: 0.47
        n_batches: 5
    exp2_text_match:
      count_6:
        f1: 0.32
        precision: 0.26
        recall: 0.416
        pred_gold_ratio: 1.6
        n_batches: 27
      count_12:
        f1: 0.306
        precision: 0.291
        recall: 0.323
        pred_gold_ratio: 1.11
        n_batches: 27
    vs_exp001_delta:
      count_1:
        f1_delta: +0.139 (+76%)
        precision_delta: +0.111 (+106%)
        recall_delta: -0.079 (-11%)
        overpred_fix: 6.85→2.97
      count_6:
        f1_delta: +0.151 (+97%)
        precision_delta: +0.138 (+157%)
        recall_delta: -0.145 (-23%)
      count_12:
        f1_delta: +0.101 (+41%)
        precision_delta: +0.207 (+129%)
        recall_delta: -0.210 (-39%)
      count_44:
        f1_delta: -0.028 (-6%)
        precision_delta: +0.092 (+22%)
        recall_delta: -0.155 (-28%)
      count_64:
        f1_delta: -0.049 (-11%)
        precision_delta: +0.128 (+25%)
        recall_delta: -0.114 (-27%)
    key_finding: 'V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x
      to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1).
      But over-corrected at high counts: under-prediction (pred/gold<1) caused recall
      drops of 27-39%, slightly lowering F1 at count_22-64.'
- id: exp-004
  claim:
  - 1
  - 2
  - 3
  description: 'MAVEN confusability study: count curve + within-count BCS correlation
    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core
    finding cross-task (NER→ED) with larger type space and known sibling confusion
    (14.6-19.8%).'
  priority: P0
  gpu_budget_hours: 4
  deps:
  - exp-003a
  registry_id: exp-004
  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs
    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy
    structure.'
  status: DONE
  conclusion: success
  metrics:
    n_event_types: 168
    n_pairs: 14028
    scs_mean: 0.2161
    scs_std: 0.103
    scs_max: 0.8368
    scs_median: 0.2121
    scs_q90: 0.3457
    scs_q95: 0.3892
    pairs_above_0.5: 119
    pct_above_0.5: 0.85
    train_docs: 2913
    train_mentions: 77993
    valid_docs: 710
    valid_mentions: 18904
- id: exp-005
  claim:
  - 1
  - 2
  description: 'DocRED confusability study: count curve + BCS correlation on DocRED
    (96 relation types). Scaling stress test.'
  priority: P1
  gpu_budget_hours: 5
  deps:
  - exp-003a
  status: planned
- id: exp-006
  claim:
  - 2
  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}
    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-003a
  status: planned
- id: exp-007
  claim:
  - 2
  description: 'Error taxonomy: systematic FP classification (type_substitution /
    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic
    evidence for multi-channel model.'
  priority: P1
  gpu_budget_hours: 1
  deps:
  - exp-002
  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic
    BCS-binned analysis.
  status: planned
- id: exp-012
  claim:
  - 1
  - 2
  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional
    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model
    generalizability.'
  priority: P0
  gpu_budget_hours: 6
  deps:
  - exp-003a
  registry_id: exp012_llama_8b_r3
  status: DONE
  conclusion: failed
- id: exp-016
  claim:
  - 1
  - 2
  description: 'FewRel cross-task replication: count curve + BCS correlation on FewRel
    RE (80 relation types with --use_all). Replicates confusability effect NER→RE.
    Pilot (fewrel_pilot) confirmed signal; formal run with full count curve [1,4,8,16,32,64,80].'
  priority: P0
  gpu_budget_hours: 4
  deps:
  - exp-003a
  registry_id: exp_fewrel_formal
  status_note: RUNNING (16-rel version). Will rerun with --use_all for 80-rel full
    count curve after current run completes.
  status: DONE
  conclusion: success
  metrics:
    note: 16-rel sanity check only
    exp1:
      count_1:
        mean_acc: 0.904
        n_batches: 16
      count_4:
        mean_acc: 0.932
        n_batches: 5
      count_8:
        mean_acc: 0.867
        n_batches: 5
      count_16:
        mean_acc: 0.778
        n_batches: 5
        bcs: 0.9
        zero_variance: true
    exp2:
      count_8_low_bcs:
        acc: 0.889
        bcs: 0.782
      count_8_high_bcs:
        acc: 0.798
        bcs: 0.892
      delta_bcs_effect: -0.091
    trend: 'count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8%
      (Δ=-9.1pp)'
- id: exp-008
  claim:
  - 3
  description: 'SDGD-zero on Few-NERD: confusability-minimizing batch composition
    via embedding SCS + graph coloring. Compare vs single-pass full-schema baseline.'
  priority: P0
  gpu_budget_hours: 3
  deps:
  - exp-003a
  registry_id: exp008_sdgd_v2_fewnerd
  status_note: 'DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass
    baseline on Few-NERD. R1 (exp008_sdgd_zero_fewnerd) failed with script error.'
  status: DONE
  conclusion: negative
  metrics:
    single_pass:
      f1: 0.4451
      precision: 0.5631
      recall: 0.3679
      batches: 1
      time_s: 79
    random_batch:
      f1: 0.3007
      precision: 0.3307
      recall: 0.2758
      batches: 8
      time_s: 494
    sdgd_zero:
      f1: 0.2407
      precision: 0.3244
      recall: 0.1913
      batches: 4
      time_s: 261
    per_type: killed before completion (3/4 modes done, Director approved kill)
    vs_v1: confidence-gated merge did not improve over union merge. sdgd_zero 0.241
      vs v1 0.251, random_batch 0.301 vs v1 0.320
    key_finding: SDGD v2 confidence-gated merge + min_batch_size=8 failed to beat
      single_pass baseline (F1=0.445). Both v1 and v2 confirm decomposition hurts
      precision more than it helps recall. Claim 3 (SDGD framework) needs fundamental
      rethink.
- id: exp-009
  claim:
  - 3
  description: 'SDGD-zero on MAVEN: confusability-minimizing batch composition on
    168 event types. Compare vs single-pass + random batching. Cross-task validation
    of SDGD framework (NER→ED).'
  priority: P0
  gpu_budget_hours: 4
  deps:
  - exp-004
  - exp-008
  status: planned
- id: exp-010
  claim:
  - 3
  description: 'SDGD-cal on Few-NERD: empirical confusability from 5-10 calibration
    examples (no gradients). Compare vs SDGD-zero.'
  priority: P1
  gpu_budget_hours: 4
  deps:
  - exp-008
  status: planned
- id: exp-011
  claim:
  - 3
  description: 'SDGD-cal on MAVEN: empirical confusability with calibration on 168
    event types. Full comparison table.'
  priority: P1
  gpu_budget_hours: 4
  deps:
  - exp-009
  - exp-010
  status: planned
- id: exp-013
  claim:
  - 3
  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.
    Isolates confusability-aware grouping from batch count reduction.'
  priority: P0
  gpu_budget_hours: 3
  deps:
  - exp-008
  status: planned
- id: exp-014
  claim:
  - 3
  description: 'Ablation: per-type splitting (UniNER-style, 1 type per batch). Upper
    bound on decomposition benefit. Reveals latency vs quality tradeoff.'
  priority: P1
  gpu_budget_hours: 3
  deps:
  - exp-008
  status: planned
- id: exp-015
  claim:
  - 1
  description: 'SCS validation: Spearman/Kendall rank correlation between embedding
    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'
  priority: P1
  gpu_budget_hours: 1
  deps:
  - exp-010
  status: planned


## registry (completed experiments)

- exp_id: exp001_count_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    diagnosis: char offset 96.5% fabricated by model
    text_match_reeval:
      count_1:
        f1: 0.184
        precision: 0.105
        recall: 0.72
        pred_gold_ratio: 6.85
      count_2:
        f1: 0.123
        precision: 0.068
        recall: 0.698
        pred_gold_ratio: 10.33
      count_6:
        f1: 0.155
        precision: 0.088
        recall: 0.62
        pred_gold_ratio: 7.02
      count_12:
        f1: 0.246
        precision: 0.16
        recall: 0.539
        pred_gold_ratio: 3.38
      count_22:
        f1: 0.322
        precision: 0.232
        recall: 0.527
        pred_gold_ratio: 2.27
      count_44:
        f1: 0.473
        precision: 0.414
        recall: 0.551
        pred_gold_ratio: 1.33
      count_64:
        f1: 0.463
        precision: 0.52
        recall: 0.418
        pred_gold_ratio: 0.8
    key_finding: recall monotonically decreases (0.72→0.42), precision monotonically
      increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at
      count_44
    wrong_type_trend: 'type confusion increases with count: 0→2434, supports confusability
      hypothesis'
    spurious_dominant: spurious FPs (text in source but not entity) dominate at low
      count, not hallucination
    conclusion_text_match: F1 curve inversion caused by over-prediction confound,
      NOT absence of confusability effect. Recall curve + type confusion pattern support
      hypothesis.
- exp_id: exp002_confusability_controlled
  name: ''
  status: DONE
  conclusion: success
  metrics:
    data_source: exp2_reeval_results.json (text_match, CLEAN)
    primary_recall_vs_bcs:
      count_6:
        r: 0.2754
        p: 0.1644
        n: 27
        verdict: FAIL
      count_12:
        r: 0.2219
        p: 0.266
        n: 27
        verdict: FAIL
      partial:
        r: 0.2522
        p: 0.0658
        n: 54
        verdict: FAIL
    secondary_f1_vs_bcs:
      count_6:
        r: 0.1754
        p: 0.3814
        n: 27
        verdict: FAIL
      count_12:
        r: 0.5012
        p: 0.0077
        n: 27
        verdict: PASS
      partial:
        r: 0.3025
        p: 0.0262
        n: 54
        verdict: PASS
    mechanistic_confusion_rate:
      random_batches:
        count_6_high: 0.0157
        count_6_low: 0.0088
        ratio_6: 1.7
        count_12_high: 0.0304
        count_12_low: 0.0131
        ratio_12: 2.4
      extreme_batches:
        count_6_high: 0.0728
        count_6_low: 0.0014
        ratio_6: 27.5
        count_12_high: 0.048
        count_12_low: 0.0061
        ratio_12: 9.9
      verdict: PASS
    pairwise_confusion_analysis:
      all:
        n_pairs: 1953
        pearson_r: 0.156
        pearson_p: 4.6e-12
        spearman_rho: 0.16
        spearman_p: 1.3e-12
      count_6:
        n_pairs: 1770
        pearson_r: 0.078
        pearson_p: 0.001
      count_12:
        n_pairs: 1953
        pearson_r: 0.147
        pearson_p: 6.7e-11
      nonzero_only:
        all_spearman_rho: 0.254
        all_spearman_p: 1.1e-06
        count_12_pearson_r: 0.212
        count_12_p: 0.00034
      top_confused_pair: person-other <-> person-politician (BCS=0.934, confusion=156)
    per_type_analysis:
      n_types: 63
      filter: freq>=5
      micro_f1_vs_bcs:
        pearson_r: -0.1828
        pearson_p: 0.1516
        spearman_rho: -0.2927
        spearman_p: 0.0199
        partial_r_ctrl_logfreq: -0.1998
        partial_p: 0.1163
      mean_f1_vs_bcs:
        pearson_r: -0.1374
        pearson_p: 0.283
        spearman_rho: -0.2412
        spearman_p: 0.0568
        partial_r_ctrl_logfreq: -0.1428
        partial_p: 0.2641
      quartile_comparison:
        low_bcs_cutoff: 0.798
        high_bcs_cutoff: 0.827
        low_bcs_f1: 0.3098
        high_bcs_f1: 0.2275
        delta_f1: -0.0823
        low_bcs_freq: 2134
        high_bcs_freq: 2049
      confound_check:
        bcs_vs_logfreq_r: 0.042
        bcs_vs_logfreq_p: 0.74
        logfreq_vs_f1_r: 0.25
        logfreq_vs_f1_p: 0.048
      verdict: Direction supports hypothesis. Spearman significant (p=0.02). Frequency
        confound absent at type level (r=0.04).
    overall_verdict: PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE
      STRONG PASS, PER-TYPE DIRECTIONAL PASS
- exp_id: exp003a_prompt_v2_rerun
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_mode: text_match
    exp1_text_match:
      count_1:
        f1: 0.323
        precision: 0.216
        recall: 0.641
        pred_gold_ratio: 2.97
        n_batches: 64
      count_2:
        f1: 0.273
        precision: 0.18
        recall: 0.56
        pred_gold_ratio: 3.11
        n_batches: 5
      count_6:
        f1: 0.306
        precision: 0.226
        recall: 0.475
        pred_gold_ratio: 2.1
        n_batches: 5
      count_12:
        f1: 0.347
        precision: 0.367
        recall: 0.329
        pred_gold_ratio: 0.9
        n_batches: 5
      count_22:
        f1: 0.299
        precision: 0.339
        recall: 0.267
        pred_gold_ratio: 0.79
        n_batches: 5
      count_44:
        f1: 0.445
        precision: 0.506
        recall: 0.396
        pred_gold_ratio: 0.78
        n_batches: 5
      count_64:
        f1: 0.414
        precision: 0.648
        recall: 0.304
        pred_gold_ratio: 0.47
        n_batches: 5
    exp2_text_match:
      count_6:
        f1: 0.32
        precision: 0.26
        recall: 0.416
        pred_gold_ratio: 1.6
        n_batches: 27
      count_12:
        f1: 0.306
        precision: 0.291
        recall: 0.323
        pred_gold_ratio: 1.11
        n_batches: 27
    vs_exp001_delta:
      count_1:
        f1_delta: +0.139 (+76%)
        precision_delta: +0.111 (+106%)
        recall_delta: -0.079 (-11%)
        overpred_fix: 6.85→2.97
      count_6:
        f1_delta: +0.151 (+97%)
        precision_delta: +0.138 (+157%)
        recall_delta: -0.145 (-23%)
      count_12:
        f1_delta: +0.101 (+41%)
        precision_delta: +0.207 (+129%)
        recall_delta: -0.210 (-39%)
      count_44:
        f1_delta: -0.028 (-6%)
        precision_delta: +0.092 (+22%)
        recall_delta: -0.155 (-28%)
      count_64:
        f1_delta: -0.049 (-11%)
        precision_delta: +0.128 (+25%)
        recall_delta: -0.114 (-27%)
    key_finding: 'V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x
      to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1).
      But over-corrected at high counts: under-prediction (pred/gold<1) caused recall
      drops of 27-39%, slightly lowering F1 at count_22-64.'
- exp_id: exp-004
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_event_types: 168
    n_pairs: 14028
    scs_mean: 0.2161
    scs_std: 0.103
    scs_max: 0.8368
    scs_median: 0.2121
    scs_q90: 0.3457
    scs_q95: 0.3892
    pairs_above_0.5: 119
    pct_above_0.5: 0.85
    train_docs: 2913
    train_mentions: 77993
    valid_docs: 710
    valid_mentions: 18904
- exp_id: exp004_maven_bcs
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    exp1_count_curve:
      count_1:
        n_batches: 64
        exact_f1: 0.009
        relaxed_f1: 0.106
        bcs: 0
      count_6:
        n_batches: 5
        exact_f1: 0.003
        relaxed_f1: 0.103
        bcs: 0.892
      count_12:
        n_batches: 5
        exact_f1: 0.008
        relaxed_f1: 0.146
        bcs: 0.921
      count_22:
        n_batches: 5
        exact_f1: 0.013
        relaxed_f1: 0.185
        bcs: 0.933
      count_44:
        n_batches: 5
        exact_f1: 0.018
        relaxed_f1: 0.247
        bcs: 0.967
      count_64:
        n_batches: 5
        exact_f1: 0.013
        relaxed_f1: 0.245
        bcs: 0.973
    exp2_bcs_controlled:
      count_6_high_bcs:
        exact_f1: 0.0354
        relaxed_f1: 0.211
        bcs: 0.9447
      count_6_low_bcs:
        exact_f1: 0.0068
        relaxed_f1: 0.089
        bcs: 0.8709
      count_12_high_bcs:
        exact_f1: 0.0151
        relaxed_f1: 0.1568
        bcs: 0.9447
      count_12_low_bcs:
        exact_f1: 0.0068
        relaxed_f1: 0.105
        bcs: 0.9148
    key_finding: 'MAVEN batch-level: high_bcs relaxed_F1 2.4x vs low_bcs (count_6).
      Direction same as Few-NERD batch-level (positive). Pairwise + per-type analysis
      needed to control frequency confound.'
    note: exact_F1 very low (0.003-0.035), relaxed_F1 usable (0.089-0.247). Event
      trigger boundary matching is fuzzy. A re-run (500 samples) is still in progress
      in artifacts/exp004/.
- exp_id: fewrel_pilot
  name: ''
  status: DONE
  conclusion: success
  metrics:
    embedding: all-MiniLM-L6-v2
    n_batches: 15
    n_predictions: 374
    count_4:
      low_bcs_acc: 0.917
      high_bcs_acc: 0.708
      delta_pp: -20.9
      low_bcs: 0.42
      high_bcs: 0.97
    count_8:
      low_bcs_acc: 1
      high_bcs_acc: 0.5
      delta_pp: -50
      low_bcs: 0.47
      high_bcs: 0.97
    count_16:
      low_bcs_acc: 0.917
      high_bcs_acc: 0.431
      delta_pp: -48.6
      low_bcs: 0.57
      high_bcs: 0.97
    key_finding: 'BCS-accuracy strong negative: high-BCS batches 43-71% vs low-BCS
      92-100%. Effect increases with count. Cross-task (NER→RE) replication of confusability
      hypothesis.'
- exp_id: exp008_sdgd_zero_fewnerd
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp008_sdgd_zero_fewnerd_r2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    single_pass:
      f1: 0.4451
      precision: 0.5631
      recall: 0.3679
      batches: 1
      time_s: 77.3
    sdgd_zero:
      f1: 0.2514
      precision: 0.2096
      recall: 0.3141
      batches: 8
      time_s: 408.7
    random_batch:
      f1: 0.3197
      precision: 0.2491
      recall: 0.4462
      batches: 8
      time_s: 476.1
    per_type:
      f1: 0.2915
      precision: 0.194
      recall: 0.5856
      batches: 66
      time_s: 2532.2
    key_finding: All decomposition modes F1 < single_pass. Decomposition boosts recall
      but kills precision (merge amplification). sdgd_zero worst F1, even below random_batch.
- exp_id: exp_fewrel_formal
  name: ''
  status: DONE
  conclusion: success
  metrics:
    note: 16-rel sanity check only
    exp1:
      count_1:
        mean_acc: 0.904
        n_batches: 16
      count_4:
        mean_acc: 0.932
        n_batches: 5
      count_8:
        mean_acc: 0.867
        n_batches: 5
      count_16:
        mean_acc: 0.778
        n_batches: 5
        bcs: 0.9
        zero_variance: true
    exp2:
      count_8_low_bcs:
        acc: 0.889
        bcs: 0.782
      count_8_high_bcs:
        acc: 0.798
        bcs: 0.892
      delta_bcs_effect: -0.091
    trend: 'count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8%
      (Δ=-9.1pp)'
- exp_id: exp_fewrel_formal_80rel
  name: ''
  status: DONE
  conclusion: success
  metrics:
    exp1_count_curve:
      count_1:
        acc: 0.8573
        n_batches: 80
        bcs: 0
      count_4:
        acc: 0.8667
        n_batches: 5
        bcs: 0.6335
      count_8:
        acc: 0.8021
        n_batches: 5
        bcs: 0.7175
      count_16:
        acc: 0.6958
        n_batches: 5
        bcs: 0.795
      count_32:
        acc: 0.6578
        n_batches: 5
        bcs: 0.8893
      count_64:
        acc: 0.5424
        n_batches: 5
        bcs: 0.9434
      count_80:
        acc: 0.5042
        n_batches: 5
        bcs: 0.9706
    exp2_bcs_controlled:
      count_8:
        low_bcs_acc: 0.8229
        low_bcs: 0.4715
        high_bcs_acc: 0.5104
        high_bcs: 0.9706
        random_acc: 0.8025
        delta_pp: -31.2
      count_16:
        low_bcs_acc: 0.8281
        low_bcs: 0.5705
        high_bcs_acc: 0.5156
        high_bcs: 0.9706
        random_acc: 0.7169
        delta_pp: -31.2
    vs_16rel:
      degradation_16rel: -12.6pp (0.904→0.778)
      degradation_80rel: -35.3pp (0.857→0.504)
      bcs_effect_16rel: -9.1pp
      bcs_effect_80rel: -31.2pp
      amplification: 3.4x
    key_finding: 80-rel count curve 0.857→0.504 (degradation 35.3pp, 远强于 16-rel 12.6pp).
      BCS effect -31.2pp (3.4x amplification vs 16-rel). 更多 relations → 更大 confusion
      space → 更强 degradation + BCS effect.
- exp_id: exp008_sdgd_v2_fewnerd
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    single_pass:
      f1: 0.4451
      precision: 0.5631
      recall: 0.3679
      batches: 1
      time_s: 79
    random_batch:
      f1: 0.3007
      precision: 0.3307
      recall: 0.2758
      batches: 8
      time_s: 494
    sdgd_zero:
      f1: 0.2407
      precision: 0.3244
      recall: 0.1913
      batches: 4
      time_s: 261
    per_type: killed before completion (3/4 modes done, Director approved kill)
    vs_v1: confidence-gated merge did not improve over union merge. sdgd_zero 0.241
      vs v1 0.251, random_batch 0.301 vs v1 0.320
    key_finding: SDGD v2 confidence-gated merge + min_batch_size=8 failed to beat
      single_pass baseline (F1=0.445). Both v1 and v2 confirm decomposition hurts
      precision more than it helps recall. Claim 3 (SDGD framework) needs fundamental
      rethink.
- exp_id: exp012_llama_fewnerd
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp007_error_taxonomy
  name: ''
  status: DONE
  conclusion: success
  metrics:
    exp1_random:
      bcs_zero:
        n_fp: 6172
        intra_sub_pct: 0
        extra_sub_pct: 90.3
        intra_sub_per_100_gold: 0
      bcs_low:
        n_fp: 2231
        intra_sub_pct: 1.6
        extra_sub_pct: 89.9
        intra_sub_per_100_gold: 3.4
      bcs_medium:
        n_fp: 3843
        intra_sub_pct: 10.6
        extra_sub_pct: 78.1
        intra_sub_per_100_gold: 6.47
      bcs_high:
        n_fp: 6188
        intra_sub_pct: 49.4
        extra_sub_pct: 30.8
        intra_sub_per_100_gold: 12.93
    correlation:
      intra_sub_vs_bcs_spearman_rho: 1
      intra_sub_vs_bcs_p: <0.001
      chi_square: 6952
      chi_square_p: ~0
    exp2_controlled:
      trend: IntraSub 3.2% -> 7.3% -> 8.6% (rho=1.0, p<0.001)
    key_finding: 'BCS>=0.95: 49.4% FP are intra-batch type confusion (13/100 gold).
      Hallucination+boundary <3%. LLM main error mode is type confusion, not hallucination.'
- exp_id: exp012_llama_fewnerd_r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp016_fewrel_error_taxonomy
  name: ''
  status: DONE
  conclusion: success
  metrics:
    error_distribution:
      zero_bcs:
        bcs_mean: 0
        correct_pct: 85.73
        wrong_type_pct: 0
        intra_sub_pct: 0
        missed_pct: 14.27
      low_bcs:
        bcs_mean: 0.565
        correct_pct: 85.42
        wrong_type_pct: 4.17
        intra_sub_pct: 4.17
        missed_pct: 10.42
      medium_bcs:
        bcs_mean: 0.729
        correct_pct: 75.7
        wrong_type_pct: 13
        intra_sub_pct: 13
        missed_pct: 11.3
      high_bcs:
        bcs_mean: 0.86
        correct_pct: 66.67
        wrong_type_pct: 20.28
        intra_sub_pct: 20.28
        missed_pct: 13.05
      very_high_bcs:
        bcs_mean: 0.971
        correct_pct: 52.03
        wrong_type_pct: 32.25
        intra_sub_pct: 32.25
        missed_pct: 15.71
    correlations:
      intra_sub_vs_bcs_spearman: 0.9539
      intra_sub_vs_bcs_p: <1e-6
      accuracy_vs_bcs_spearman: -0.5821
      accuracy_vs_bcs_p: <1e-6
    cross_task:
      ner_intra_sub_vs_bcs_rho: 1
      re_intra_sub_vs_bcs_rho: 0.9539
    key_finding: 100% of type confusion in RE is intra-batch (model only predicts
      from schema). IntraSub vs BCS ρ=0.954 confirms NER finding. Missed rate flat
      (10-16%), BCS drives confusion not detection failure.
- exp_id: bootstrap_ci_analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    fewnerd_pairwise_r:
      point: 0.112
      ci_lower: 0.076
      ci_upper: 0.156
      n: 1953
      note: point estimate 0.112 vs old 0.156 — re-run confirmed current value
    maven_minilm_pairwise_r:
      point: 0.129
      ci_lower: 0.104
      ci_upper: 0.156
      n: 11026
    fewrel_count8_delta_pp:
      point: 31.2
      ci_lower: 17.7
      ci_upper: 42.7
      n: 96+96
    fewrel_count16_delta_pp:
      point: 31.2
      ci_lower: 22.9
      ci_upper: 39.6
      n: 192+192
    fewnerd_pertype_rho:
      point: -0.293
      ci_lower: -0.492
      ci_upper: -0.054
      n: 63
    confusion_ratio_count6:
      point: 25.3
      ci_lower: 6.1
      ci_upper: 60.5
    confusion_ratio_count12:
      point: 21.2
      ci_lower: 5.3
      ci_upper: 52.2
    key_finding: All CIs exclude null (0 for correlations, 1 for ratios). All effects
      are directionally robust at 95% level.
- exp_id: exp015_scs_validation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    all_pairs:
      n: 1953
      n_nonzero: 216
      qwen3_spearman: 0.1682
      qwen3_spearman_p: '7.3e-14'
      qwen3_kendall: 0.1351
      minilm_spearman: 0.1439
      minilm_spearman_p: '1.7e-10'
      minilm_kendall: 0.1152
    nonzero_only:
      n: 216
      qwen3_spearman: 0.2722
      qwen3_spearman_p: '5.0e-05'
      qwen3_kendall: 0.2001
      minilm_spearman: 0.306
      minilm_spearman_p: '4.6e-06'
      minilm_kendall: 0.2276
    key_finding: Both embeddings significantly predict confusion (all p<1e-5). Qwen3
      better overall (rho=0.168), MiniLM better on nonzero pairs (rho=0.306). SCS
      is a valid but partial proxy — context, frequency, mention ambiguity also matter.
- exp_id: exp012_llama_fewnerd_r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp012_llama_8b
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_fewrel_40rel
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp012_llama_awq
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp012_llama_fewnerd_r4
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp012_llama_8b_fewnerd
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_fewrel_40rel_r2
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp_fewrel_40rel_r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp012_llama_8b_r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    exp1_llama_recall_count1: 0.702
    exp1_llama_recall_count64: 0.273
    exp1_recall_decline_pp: -42.9
    exp1_per_batch_recall_corr_vs_qwen: 0.7249
    exp1_llama_text_match_f1_range: 0.06-0.36
    exp1_exact_f1: 0
    exp1_note: exact/relaxed F1=0 due to missing char offsets, text_match is correct
      metric
- exp_id: exp012_llama_8b_r3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: exp006_interaction_2x2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    cell_means_f1:
      low_count_low_bcs: 0.324
      low_count_high_bcs: 0.313
      high_count_low_bcs: 0.325
      high_count_high_bcs: 0.277
    main_effects:
      count: -0.018
      bcs: -0.029
    interaction:
      estimate: -0.036
      z: -0.667
      p: 0.505
      bcs_effect_at_low_count: -0.011
      bcs_effect_at_high_count: -0.048
    verdict: 交互方向符合 multiplicative 假设但统计不显著 (p=0.505)，未检测到显著交互效应
- exp_id: exp012_llama_8b_r2_exp2
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: exp_fewrel_40rel_r4
  name: ''
  status: DONE
  conclusion: success
  metrics:
    exp1_acc_count1: 0.858
    exp1_acc_count4: 0.867
    exp1_acc_count8: 0.802
    exp1_acc_count16: 0.697
    exp1_acc_count32: 0.658
    exp1_acc_count40: 0.588
    exp1_decline_pp: -27
    exp2_bcs_delta_count8: 0.333
    exp2_bcs_delta_count16: 0.318
    exp2_low_bcs_acc_count8: 0.833
    exp2_high_bcs_acc_count8: 0.5
    exp2_low_bcs_acc_count16: 0.818
    exp2_high_bcs_acc_count16: 0.5
- exp_id: exp012_llama_fewrel_ch2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    exp2_bcs_controlled:
      count_8:
        low_bcs_acc: 0.7812
        high_bcs_acc: 0.5104
        delta_pp: -27.1
      count_16:
        low_bcs_acc: 0.7552
        high_bcs_acc: 0.5156
        delta_pp: -24
    overall_correlation:
      n_batches: 54
      pearson_r: -0.39
      pearson_p: 0.004
      spearman_rho: -0.43
      spearman_p: 0.001
    cross_model_comparison:
      llama_delta_pp: -27.1
      qwen3_delta_pp: -31.2
      ratio: 0.87
      note: LLaMA effect = 87% of Qwen3, direction and magnitude consistent
    no_floor_effect: true
    mean_accuracy: 0.77
    accuracy_range: 0.41-0.98
    key_finding: 'BCS confusability effect cross-model replicated: LLaMA Δ=-27.1pp
      (87% of Qwen3 -31.2pp). Pearson r=-0.39 (p=0.004), Spearman ρ=-0.43 (p=0.001).
      No floor effect.'
- exp_id: exp_fewrel_16rel_bootstrap
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_batches: 100
    pool_size: 16
    batch_size: 8
    bcs_range:
    - 0.6532
    - 0.9002
    quartile_delta:
      Q4_minus_Q1_pp: -5.31
      ci_95_lower: -9.45
      ci_95_upper: -4.49
      note: CI values from pre-D038 bootstrap, may need re-verification with MEAN-based
        BCS
    pearson_r_bcs_acc: -0.467
    regression_slope:
      slope: -0.509
      ci_95_lower: -0.556
      ci_95_upper: -0.349
      r_squared: 0.218
      p_value: 1.01e-12
      interpretation: per +0.1 BCS → -5.09pp accuracy
      note: CI from pre-D038 bootstrap
    amplification_ratio:
      quartile_16_vs_80: 4.2
      ci_95_lower: 3.3
      ci_95_upper: 6.95
    key_finding: '16-rel pool BCS effect (MEAN-based, D038): Δ(Q4-Q1)=-5.31pp, r=-0.467.
      Regression slope=-0.509. Bootstrap 1000 resamples. [D038 MEAN correction applied,
      old values: r=-0.637/Δ=-7.42pp/slope=-0.449]'
- exp_id: exp_fewrel_16rel_100batch
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: exp_fewrel_80pool_16sub_bootstrap
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_batches: 100
    pool_size: 80-rel pool, 16-type subsamples
    batch_size: 8
    mean_accuracy: 0.8077
    mean_bcs: 0.557
    bcs_range:
    - 0.4578
    - 0.6836
    quartile_delta:
      Q4_minus_Q1_pp: -3.92
      ci_95_lower: -7.79
      ci_95_upper: 0.42
    pearson_r_bcs_acc: -0.221
    pearson_p: 0.027
    regression_slope:
      slope: -0.401
      ci_95_lower: -0.684
      ci_95_upper: -0.062
      interpretation: per +0.1 BCS → -4.01pp accuracy
    key_finding: '80-pool 16-sub BCS effect directional: Δ(Q4-Q1)=-3.92pp CI crosses
      zero [-7.79,+0.42], but regression slope=-0.401 CI[-0.684,-0.062] excludes zero.
      Effect weaker than independent 16-rel pool (Δ=-7.42pp) due to narrower BCS range.'
- exp_id: exp_maven_residualized_bcs
  name: ''
  status: DONE
  conclusion: success
  metrics:
    minilm:
      raw_rho: 0.208
      raw_p: 0.011
      confound: log_freq
      bcs_confound_r: 0.201
      partial_r: 0.133
      partial_p: 0.107
    qwen3:
      raw_rho: 0.184
      raw_p: 0.025
      confound: degree_centrality_0.7
      bcs_confound_r: 0.854
      partial_r: 0.063
      partial_p: 0.442
    joint_control:
      qwen3_p: 0.439
      minilm_p: 0.226
      note: Both n.s. after controlling log_freq + degree jointly
    key_finding: MAVEN BCS-F1 positive correlation is centrality artifact. MiniLM
      confound=frequency, Qwen3 confound=degree centrality (r=0.854). After joint
      control, both correlations vanish. Confirms pairwise SCS remains valid but per-type
      aggregation fails on homogeneous schemas.
- exp_id: exp_fewrel_v2_bcs_controlled
  name: ''
  status: DONE
  conclusion: success
  metrics:
    low_bcs_mean_acc: 0.8042
    high_bcs_mean_acc: 0.725
    delta_low_minus_high_pp: 7.92
    bootstrap_ci_95_lower_pp: -5.21
    bootstrap_ci_95_upper_pp: 21.46
    n_bootstrap: 10000
    n_batches_per_group: 5
    samples_per_batch: 96
    total_inferences: 960
- exp_id: exp_docred_confusability
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_relation_types: 96
    n_eval_samples: 1240
    total_inferences: 13618
    count_curve:
      count_1: 0.88
      count_4: 0.77
      count_8: 0.774
      count_16: 0.524
      count_32: 0.521
      count_64: 0.424
      count_96: 0.387
    bcs_effect_count16:
      low_bcs_acc: 0.679
      high_bcs_acc: 0.447
      gap: 0.233
      spearman_r: -0.661
      slope: -0.713
      slope_95ci:
      - -0.909
      - -0.529
    bcs_effect_count32:
      low_bcs_acc: 0.578
      high_bcs_acc: 0.403
      gap: 0.176
      spearman_r: -0.509
      slope: -0.69
      slope_95ci:
      - -0.854
      - -0.519
- exp_id: bcs_max_to_mean_fix
  name: ''
  status: PREPARING
  conclusion: success
  metrics: {}
- exp_id: exp_confusability_batch_composition
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp_fewrel_v2_n25
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    n_low: 25
    n_high: 25
    low_bcs_mean_acc: 0.8521
    high_bcs_mean_acc: 0.5967
    delta_pp: 25.54
    ci_95:
    - 22.42
    - 28.62
    permutation_p: 0
    pearson_r: -0.919
    low_bcs_range:
    - 0.356
    - 0.367
    high_bcs_range:
    - 0.791
    - 0.811
    key_finding: v2 prompt does NOT eliminate confusability effect. At n=25 with wider
      BCS separation, effect is massive (25.5pp) and highly significant. Prior n=5
      result (7.9pp, CI crosses zero) was underpowered + narrow BCS contrast.
- exp_id: exp_cross_embedding_sensitivity
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    fewnerd_qwen3:
      pearson_r: 0.138
      pearson_p: 1.0e-09
      spearman_rho: 0.168
      spearman_p: 7.3e-14
    fewnerd_minilm:
      pearson_r: 0.172
      pearson_p: 2.0e-14
      spearman_rho: 0.144
      spearman_p: 1.7e-10
    fewrel_minilm:
      slope: -0.485
      r: -0.398
      p: 0.04
    fewrel_qwen3:
      slope: -0.542
      r: -0.185
      p: 0.356
      note: BCS range compression (std=0.034 vs MiniLM 0.081), directional but n.s.
    key_finding: SCS-confusion signal robust to embedding choice (both significant
      on Few-NERD). MiniLM better for BCS due to designed-for-similarity. Qwen3 causal-LM
      embeddings compress BCS range.
- exp_id: exp017_gpt4o_mini_fewrel
  name: ''
  status: PREPARING
  conclusion: killed
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
  "promptId": "5fd9c5db-9fd1-4f34-a058-6833826146fc",
  "type": "user",
  "uuid": "a979151c-6447-4e5d-baee-4c92f9181e8e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "c3c703d5-f588-4e67-b762-e7ebe9792a81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T07:43:09.876Z_

```json
{
  "parentUuid": "a979151c-6447-4e5d-baee-4c92f9181e8e",
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
  "uuid": "de738a42-20c1-45b5-8f04-fdf3b29b2a87",
  "timestamp": "2026-05-16T07:43:09.876Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "c3c703d5-f588-4e67-b762-e7ebe9792a81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T07:43:09.876Z_

```json
{
  "parentUuid": "de738a42-20c1-45b5-8f04-fdf3b29b2a87",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "08f5f9e6-656e-4d97-a526-b6d4e36c3642",
  "timestamp": "2026-05-16T07:43:09.876Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "c3c703d5-f588-4e67-b762-e7ebe9792a81",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心假设部分验证，部分 reviewer 质疑效应量或覆盖面，论文落入 EMNLP Findings 或需 rebuttal 挽救 核心假设：[\"A1 部分成立: Pairwise r=0.11-0.13 被质疑为'统计显著但实际意义有限'，需补充 FewRel 的大效应量（Δ=-31pp）来说服\", '…",
  "leafUuid": "08f5f9e6-656e-4d97-a526-b6d4e36c3642",
  "sessionId": "c3c703d5-f588-4e67-b762-e7ebe9792a81"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier schema confusability study with cross-task validation",
  "sessionId": "c3c703d5-f588-4e67-b762-e7ebe9792a81"
}
```

---

### Assistant

_source line 8 · 2026-05-16T07:46:59.776Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "median" tier scenario they've defined. Let me identify all planned experiments:

1. **exp-005** (DocRED confusability study) - status: planned
2. **exp-006** (Interaction effect 2x2) - status: planned... wait, looking at the registry, exp006_interaction_2x2 is DONE with conclusion: negative. But in the experiment_plan it says status: planned. Let me re-check.


Actually, there's a discrepancy between the experiment_plan and the registry. Several experiments marked as "planned" in the plan are already completed in the registry—exp-006, exp-007, and exp-015 all show as done with their conclusions, while exp-005, exp-009, exp-010, exp-011, exp-013, and exp-014 remain genuinely planned.

Wait, I need to check exp-005 again—exp_docred_confusability is actually in the registry as done too. So the truly outstanding planned experiments are exp-009 through exp-014, excluding the ones already completed. The user is asking for detailed data on each planned experiment from the plan, so I should focus on those remaining ones.

Actually, I'm realizing the user wants me to simulate what median-tier results would look like for these planned experiments—this is a prediction exercise for paper planning. Let me identify all the experiments still marked as planned: the DocRED confusability study, the 2x2 interaction effect, error taxonomy, SDGD-zero on MAVEN, SDGD-cal on Few-NERD, SDGD-cal on MAVEN, and the two ablation studies on batching and per-type splitting. 9. exp-015: SCS validation

But some of these are already done in the registry. The user said "每个 planned 实验" — I think they want predictions for experiments still listed as "planned" in the experiment_plan. Even if some have since been completed in the registry, the user specifically asked about the "planned" ones from the experiment_plan.

Actually, I think the user wants me to generate imagined/predicted results for ALL planned experiments to create a complete median-tier simulation. This is a standard research planning exercise — "what would the full set of results look like if we land in the median tier?"

Let me think about what median tier means for each experiment. For the median tier, I'm looking at ARR average scores around 3.0-3.5, with 1-2 claims fully supported, 2-3 major reviewer weaknesses, 2-3 cross-task significant replications, and multi-model effect consistency around 0.7. The venue probabilities would be 0.15-0.35 for main track and 0.5-0.7 for findings or above, with rebuttal flip probability between 0.4-0.65.

For the narrative adjustments, A1 would partially hold with pairwise correlations questioned as statistically significant but practically limited, A2 holds with clear error taxonomy, A3 has sufficient scaling evidence, A4 partially holds with LLaMA succeeding only on FewRel while Few-NERD shows generalizability issues, A5 gets disputed with MAVEN per-type results seen as counter-evidence by a couple reviewers, A6 is marked as a major weakness around the lack of practical methods, and A7 basically holds but needs stronger practical implications. Now I'm ready to predict results for each planned experiment. experiment:

**exp-005: DocRED confusability study**

The DocRED experiment is already in the registry with real results, but since the user wants predictions for planned experiments, I'll treat it as such. For median-tier performance, I'd expect the count curve to replicate with roughly 50 percentage points of degradation across relation types, but the BCS-controlled effect would be weaker than FewRel due to document-level RE introducing additional confounds beyond just schema complexity.

**exp-006: Interaction 2x2**

This one's also already completed in the registry, but predicting median-tier results: the interaction effect wouldn't reach statistical significance, which aligns with what the actual results showed.

**exp-007: Error taxonomy**

The error taxonomy experiment succeeded, showing intraSub errors monotonically increasing with BCS across tasks with perfect rank correlation — this is the clearest evidence without controversy.

**exp-009: SDGD-zero on MAVEN**

SDGD-zero fails on MAVEN just like it did on Few-NERD, and with 168 entity types the merge amplification problem gets even worse, confirming that no practical method emerges from this approach.

**exp-010: SDGD-cal on Few-NERD**

The calibration-based variant shows modest gains over the zero-shot version but still underperforms single-pass baselines, leaving reviewers frustrated that even this refinement doesn't solve the core problem.

**exp-011 through exp-015**

The calibrated approach on MAVEN shows similar modest improvement but remains negative, random batching lands between single-pass and zero-shot confirming decomposition itself is the issue, per-type splitting maximizes recall at the cost of precision revealing merge amplification as the true bottleneck, and the SCS validation confirms significant correlation between the metric and empirical confusion across both embedding approaches.

Now I need to reconcile which experiments are already in the registry versus still planned.

Generating median-tier predictions for all planned experiments, treating this as a simulation exercise where even completed experiments get predicted results that may differ from what was actually observed.

Constructing the YAML output with tier, narrative guidance, and detailed predictions for each experiment with rationales. 力证据但被 1-2 位 reviewer 质疑为 task-specific。Error taxonomy 是最无争议的贡献。SDGD 全线负面结果使 "no practical method" 成为主要弱点。LLaMA 仅在 FewRel 成功复现，Few-NERD 多次失败被标记为 generalizability concern。MAVEN per-type 正方向需要更强的 centrality confound 解释。论文落入 EMNLP Findings 或需 rebuttal 挽救进入 main。

现在我在规划 DocRED 的混淆度研究，用 count curve 和 BCS 控制实验来验证跨任务的效应，预期看到随着关系类型数量增加性能显著下降，以及高混淆度样本在控制后的性能差异。

DocRED 作为文档级关系抽取任务，复杂度高于句子级的 FewRel，因为每个文档包含多个实体对且推理需要跨越多个句子，这会降低基线准确率。96 种关系类型的语义重叠程度介于 FewRel 的 80 种和 Few-NERD 的 66 种之间。

Count curve 的性能下降约 41 个百分点，虽然弱于 FewRel 80-rel 的 35 个百分点，但这是因为 DocRED 的基线本身更低。BCS 效应显示 Δ=-16pp，弱于 FewRel 的 -31pp，说明文档级多实体对的上下文稀释了纯混淆性信号。Pairwise 相关系数 r=0.09 接近显著性边界，可能引发审稿人对文档级关系抽取中额外变异源（如实体对距离和跨句推理）是否混淆了混淆性信号的质疑。

现在看 DocRED 在 Qwen3-32B 上的计数曲线数据，随着样本数增加，准确率从 72% 逐步下降到 31%，而 BCS 均值则从 0 上升到 0.95，这提供了跨任务一致但不够决定性的证据。

进一步的 BCS 控制实验显示，低 BCS 条件下准确率为 55%，高 BCS 条件下仅 39%，与随机基线的 47% 相比，负相关关系明显但斜率仍需进一步验证。

DocRED 上的效应确实弱于句子级关系抽取，可能源于文档级任务引入的额外噪声，而且在更大样本量（count=32）时 BCS 效应的显著性边界（p=0.06）表明信号不够稳定。与 FewRel 的效应量差异需要在 rebuttal 中解释，但关键是强调文档级设置本身更具挑战性，方向一致性已有价值，配对分析仍保持显著。接下来要设计 2×2 交互效应实验来进一步分离低/高 count 和低/高 BCS 的组合影响。 我在分析为什么这个交互效应虽然方向符合乘法假设（高count下BCS效应更强），但统计上不显著——主要是因为Few-NERD的样本量太小（每个单元格只有27个样本），count对比度有限（count_6和count_12差异不大），而且BCS的变异范围很窄（0.75-0.90），这些因素都压缩了效应空间，使得需要更大的样本量（约60-80）才能检测到这个中等大小的交互效应。

FewRel上3.4倍的放大效果间接支持交互确实存在，但由于实验设计不同，无法直接对比，审稿人可能会认为证据还不够完整。

现在看交互项的统计检验结果——虽然p值为0.48表示不显著，但效应方向一致，这是典型的样本量不足导致的结果。我应该如实报告这个限制，并讨论审稿人可能要求的补充工作，比如功效分析或在FewRel的80-rel数据上进行正式的2×2设计验证。

接下来我需要系统地分类错误类型，按照替换错误、边界错误、假阴性和幻觉等维度，在不同BCS分位上统计FewNERD和FewRel的表现，预期看到随BCS增加而错误率显著上升的趋势。 Looking at the error taxonomy table across Few-NERD, the pattern is unmistakable: as BCS increases from 0 to High, IntraSub jumps from nearly 0% to 48%, while ExtraSub plummets from 90% down to 31%, providing the clearest mechanical evidence for claim 2.

The FewRel data reinforces this with a similar monotonic trend—correct predictions drop from 85.7% at zero BCS to 52% at very high, while IntraSub errors climb steadily from 0% to 32%. The cross-task replication with near-perfect correlations (NER ρ=1.0, RE ρ=0.95) gives this error taxonomy analysis the strongest empirical foundation, something all reviewers would accept.

The main vulnerability is sample size in the low-BCS bins, but the effect magnitude is large enough to overcome that concern. Now I'm looking at the MAVEN experiment with 168 event types, comparing single-pass, random batching, and SDGD-zero approaches. The results show SDGD-zero underperforming significantly—relaxed F1 of 0.14 versus 0.245 for single-pass—because the sheer number of types amplifies the merge problem with each batch combination.

The semantic homogeneity of MAVEN's event types (all from FrameNet hierarchy) means even SDGD's grouping can't fully separate similar categories, and the inherent fuzziness in event trigger boundary matching gets worse after decomposition and merging. The performance degradation ratio of 0.57 is actually steeper than Few-NERD's 0.53, which aligns with the expectation that more types create more merge conflicts.

Random batching falls between single-pass and SDGD-zero at 0.18, confirming that the grouping strategy itself isn't the bottleneck—decomposition is. Looking at the performance metrics across these methods, the results consistently show SDGD's negative impact holds across different batch configurations, though this deepens the core weakness that no practical method has emerged yet.

The MAVEN results follow the same pattern as Few-NERD, with SDGD-zero failing again. This reinforces that merge amplification is an inherent obstacle in decomposition, but I need to reframe this in the discussion as a contribution toward understanding why decomposition fails in the first place, pointing toward calibration-based approaches as the path forward.

Now I'm looking at the calibration experiments on Few-NERD. With 5-10 calibration examples, the confusability-based approach shows modest gains—F1 improves from 0.24 to around 0.32, which is better than random batching but still significantly below the single-pass baseline at 0.445. The calibration overhead is reasonable at 45-85 seconds, and the improvement over zero-shot is about 8 percentage points, though we're still 12.5 points away from single-pass performance.

The core issue is that calibration helps capture the model's actual confusion patterns, but it can't overcome the fundamental structural problem of merge amplification—when combining outputs from multiple batches, conflicts accumulate regardless of grouping quality. The marginal returns from calibration plateau quickly; 5 examples already capture the main confusion pairs, so 10 examples only marginally improve results. This positions the method as directionally sound but practically limited—reviewers would likely see it as interesting conceptually but not compelling enough for real-world adoption.

Generating markdown table... 可能的反应：(1) "为什么不探索更好的 merge strategy？"——合理的 future work 方向；(2) "calibration 的 overhead 是否值得？"——45s 额外开销换取 8pp 改善，投资回报率低。论文应将此定位为 "diagnosing the bottleneck" 而非 "solving the problem"。

在 MAVEN 的 168 个类型上测试 SDGD-cal，我看到 calibration 同样带来约 5pp 的改善，但成本更高——需要 180-350 秒来覆盖 14028 个类型对。问题在于 MAVEN 的语义同质性意味着几乎所有类型对都存在混淆，没有清晰的安全同批集合，所以边际收益更小。10-shot 相比 5-shot 只有微小改善，因为额外的 calibration 数据收益递减。

这个跨任务的一致性模式表明 merge amplification 是结构性问题，而非特定任务的伪影。

不过审稿人会在这里最强烈地质疑这个方法的实用性。为了应对这个批评，我需要设计一个随机分组的对照实验，用相同数量的批次但随机组成，来隔离出 confusability-aware 分组的增量贡献。我在 Few-NERD 和 MAVEN 上都预期看到随机分组的性能显著低于 SDGD，这会证明我们的分组策略确实有意义。

但现在看到的结果有点出乎意料——随机分组反而表现得更好（Few-NERD 上 0.31 对比 0.24，MAVEN 上 0.18 对比 0.14）。这看起来很矛盾，但仔细分析后我意识到问题所在：SDGD-zero 的最小批次大小约束导致某些类型数量过少的批次，当提示中的类型太少时，模型缺乏足够的上下文来理解任务范围，反而产生更多虚假预测；而随机分组的批次大小分布更均匀，上下文也更平衡。

更关键的是，confusability-aware 分组把所有"简单"类型聚在一起、所有"困难"类型也聚在一起，导致困难批次的合并变得异常困难——这是 SDGD-zero 设计上的缺陷，但不否定 confusability 信号本身的有效性。

不过真正重要的发现是：所有分解方法都远低于单次通过的性能，这说明问题的根本不在于如何分解，而在于在当前合并策略下是否应该分解。这进一步证实了合并放大是根本瓶颈的论点。

现在我想看看极端情况——每个批次只包含一种类型，这样能展示分解收益的理论上界。根据预期结果，Few-NERD 上会有 66 个批次，F1 只有 0.29，虽然召回率能提升 22 个百分点，但精度会下降 37 个百分点。

这反映了一个关键的权衡：当完全消除类型混淆时，每个提示词可以专注于单一类型，注意力不会被分散，所以召回率大幅提升；但合并 66 个独立批次的结果时，同一个 span 会被多个类型"声称"，导致冲突激增，精度严重下降。这清楚地说明了合并放大效应的机制。

在 MAVEN 的 168 个类型上，这个问题更加极端。现在我在查看不同分解方法的对比表，看单次传递、按类型分解等方案在 Few-NERD 上的表现差异。

Per-type 方法虽然大幅提升了召回率，但精度下降得很厉害，而且计算成本飙升到 2500 秒。这些数据和可视化图表清楚地显示了精度-召回的权衡关系，证实了分解策略确实能改善某些指标，但需要更聪明的合并策略来平衡这些矛盾。

审稿人可能会指出这没有给出实际解决方案。

现在我在验证嵌入空间中的相似度排序是否能预测实际的混淆矩阵，用 Spearman 和 Kendall 相关系数来衡量这种对应关系。

结果显示相关性很弱（全对的 ρ=0.14-0.17），主要是因为大多数类型对从未被混淆过，产生了大量的并列排名；但当只看有非零混淆的对时，相关性明显提升到 0.27-0.31，说明 SCS 在预测实际混淆时是有效的，只是被大量零值对拉低了整体相关性。

有趣的是，Qwen3 在全对上表现更好，而 MiniLM 在非零对上表现更好，这暗示提取模型的嵌入更善于捕捉混淆的阈值，而通用嵌入则更善于捕捉混淆程度的梯度差异。

不过，即使相关性达到 ρ=0.17，审阅者可能仍会质疑这对实际应用是否足够有用——毕竟只能解释 3% 的方差，很难基于此做出有意义的分组决策。现在我看到了具体的相关性数据表，展示了不同嵌入模型在各个子集上的 Spearman 和 Kendall 相关系数。

在非零混淆子集中，相关性明显更强（ρ 达到 0.27-0.31），这表明 SCS 作为代理虽然整体解释力有限，但在特定场景下确实有用。我还看到了散点图和 ROC 曲线的描述，进一步验证了这种非线性关系和预测能力。

关键是要向审稿人解释，SCS 不需要完美——只要方向正确就能改善批处理策略，而低 R² 值反映的是混淆受多个因素影响，包括上下文、频率和提及歧义。SDGD-cal 通过使用实证混淆绕过了嵌入选择的问题，但我意识到中等水平的审稿人可能仍然对"有效但部分代理"的表述感到不满意。

现在我需要检查实验计划是否已更新，或者是否还有其他文件需要查看，但用户已经在提示中提供了所有必要的背景信息。我还想更仔细地重新考虑中等层级的叙述指导，确保所有理由都基于特定的中等层级假设。有些实验已经完成了。

对于中等层级的预测，我应该使用实际数据还是进行预测？我认为用户希望我预测在中等结果情景下结果会是什么样子，这可能与实际结果不完全一致。但由于许多实验已经完成且有已知结果，我的预测应该与现有的实际数据保持一致。

现在我需要为真正未运行的实验进行预测。

对于已完成的实验（如exp-005 DocRED），我应该使用实际数据，但要考虑这些结果在中等层级解释中的含义——虽然实际数据显示了很强的效果，但在中等层级的背景下，我需要思考审阅者会如何理解这些数据。

让我生成完整的YAML，对已有数据的实验使用实际数字，对未运行的实验进行预测。

我应该为中等层级生成合理的预测结果，这些结果既要有说服力，又要为审阅者的批评留出空间。

现在让我完成YAML配置，确保所有计划的实验都有相应的中等层级预测。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08f5f9e6-656e-4d97-a526-b6d4e36c3642",
  "isSidechain": false,
  "requestId": "req_011Cb5saJ7tkdxc5MHDqCJu1",
  "type": "assistant",
  "uuid": "0fd7ee98-a190-4468-a167-01f95ecc042b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "c3c703d5-f588-4e67-b762-e7ebe9792a81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RANoYDe9So1E4CntECBcRN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26578,
      "cache_read_input_tokens": 11841,
      "output_tokens": 22716,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 22716,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26578
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

_source line 9 · 2026-05-16T07:50:03.049Z_

```yaml
tier: median
narrative_guidance: >
  Pairwise confusability signal 跨任务复现但效应量偏小（r=0.11-0.13），FewRel Δ=-31pp 是 headline
  但被部分 reviewer 质疑为 RE-specific。Error taxonomy 无争议（A2 成立）。SDGD 全线负面，
  "no practical method" 是 1-2 位 reviewer 的 major weakness。LLaMA Few-NERD 多次失败是 
  generalizability 短板。MAVEN per-type 正方向需更强的 centrality confound 定量论证。
  整体落入 Findings 或需 rebuttal 挽救。

imagined_experiments:
  - name: "DocRED Confusability Study"
    plan_id: "exp-005"
    description: "DocRED 96 relation types count curve + BCS 控制实验，跨 NER→sentRE→docRE 验证"
    expected_results:
      count_curve:
        count_1_acc: 0.74
        count_4_acc: 0.66
        count_8_acc: 0.59
        count_16_acc: 0.48
        count_32_acc: 0.43
        count_64_acc: 0.36
        count_96_acc: 0.32
        degradation_pp: -42.0
      bcs_controlled_count16:
        low_bcs_acc: 0.56
        high_bcs_acc: 0.40
        delta_pp: -16.0
        spearman_r: -0.42
        spearman_p: 0.028
      bcs_controlled_count32:
        low_bcs_acc: 0.50
        high_bcs_acc: 0.37
        delta_pp: -13.0
        spearman_r: -0.36
        spearman_p: 0.055
      pairwise_scs_confusion:
        pearson_r: 0.09
        ci_95: [0.04, 0.14]
        n_pairs: 4560
    result_rationale: >
      DocRED 是 document-level RE，baseline 比 sentence-level FewRel 低 ~12pp（跨句推理、
      多 entity-pair 干扰）。Count curve 退化 42pp，与 FewRel 80-rel 的 35pp 量级一致但
      更大——96 types + document-level complexity 双重加剧。BCS 效应 Δ=-16pp 存在但弱于 
      FewRel 的 -31pp：document-level 的每篇文档含多个 entity pairs，relation 决策受 
      entity pair distance、跨句推理等非 confusability 因素影响，稀释了纯 BCS 信号。
      Pairwise r=0.09 刚好显著（CI 排除零但上界仅 0.14），reviewer 会质疑 document-level 
      增加的噪声源是否被充分控制。count_32 p=0.055 刚好不显著，给 reviewer 留下"cherry-pick 
      count 条件"的把柄。Median 档位下，DocRED 提供"方向一致但不具决定性"的第四任务证据。
    tables:
      - name: "Table: DocRED Count Curve (Qwen3-32B)"
        content: |
          | Count | Acc   | BCS_mean | N_batches |
          |-------|-------|----------|-----------|
          | 1     | 0.740 | 0        | 96        |
          | 4     | 0.660 | 0.53     | 5         |
          | 8     | 0.590 | 0.64     | 5         |
          | 16    | 0.480 | 0.73     | 5         |
          | 32    | 0.430 | 0.83     | 5         |
          | 64    | 0.360 | 0.91     | 5         |
          | 96    | 0.320 | 0.95     | 5         |
      - name: "Table: DocRED BCS-Controlled"
        content: |
          | Count | Low-BCS Acc | High-BCS Acc | Δ(pp)  | ρ     | p     |
          |-------|-------------|--------------|--------|-------|-------|
          | 16    | 0.560       | 0.400        | -16.0  | -0.42 | 0.028 |
          | 32    | 0.500       | 0.370        | -13.0  | -0.36 | 0.055 |
    figures_description:
      - "Count curve: monotonic decline 0.74→0.32，steepest segment 8→16"
      - "BCS-accuracy scatter (count=16): negative slope 但置信带较宽"
    analysis: >
      方向复现但信号偏弱。Reviewer 会指出：(1) count_32 p 值 borderline；(2) document-level 
      引入未控制的 confound（entity pair distance, 跨句推理）；(3) pairwise r=0.09 低于 
      Few-NERD/MAVEN 的 0.11-0.13。Rebuttal 需强调 harder setting 下方向一致的价值，
      并补充 entity-pair distance 控制分析。

  - name: "Interaction Effect 2×2"
    plan_id: "exp-006"
    description: "{low/high count} × {low/high BCS} 检验 count 和 confusability 的交互效应"
    expected_results:
      cell_means_f1:
        low_count_low_bcs: 0.324
        low_count_high_bcs: 0.313
        high_count_low_bcs: 0.325
        high_count_high_bcs: 0.277
      main_effect_count_pp: -1.8
      main_effect_bcs_pp: -2.9
      interaction_z: -0.67
      interaction_p: 0.50
      bcs_effect_at_low_count_pp: -1.1
      bcs_effect_at_high_count_pp: -4.8
    result_rationale: >
      交互方向符合 multiplicative 假设（高 count 下 BCS 效应 4.4× 于低 count），但 
      p=0.50 远不显著。根本原因是 Few-NERD 实验设计的固有限制：(1) count 对比仅 6 vs 12，
      差异过小（FewRel 的 3.4× amplification 用的是 16 vs 80）；(2) BCS 范围窄 
      (0.75-0.90)，Few-NERD 66 types 中高相似度集中在 person 子类、location 子类；
      (3) n=27 per cell，power analysis 估计需 n≈80 才能在此效应量下达到 0.8 power。
      这不是假设被否定——是实验 underpowered。但 median 档 reviewer 不会区分 "underpowered 
      null" 和 "true null"，会标注为 "interaction claim not supported"。
    tables:
      - name: "Table: 2×2 Interaction Design (Few-NERD F1)"
        content: |
          |              | Low BCS | High BCS | BCS Δ  |
          |--------------|---------|----------|--------|
          | Count=6      | 0.324   | 0.313    | -0.011 |
          | Count=12     | 0.325   | 0.277    | -0.048 |
          | Count Δ      | +0.001  | -0.036   |        |
          | Interaction: z=-0.67, p=0.50 (n.s.)        |
    figures_description:
      - "Interaction plot: 两条线（low/high BCS）跨 count 水平，方向 non-parallel 但 CI 大量重叠"
    analysis: >
      需要在论文中如实报告 null result 并提供 power analysis。FewRel 16→80 的 3.4× 
      amplification 作为 indirect interaction evidence。Reviewer 可能要求在 80-rel pool 
      上做正式 2×2 作为 rebuttal 补充分析。

  - name: "Error Taxonomy"
    plan_id: "exp-007"
    description: "系统性 FP 分类跨 BCS bins，multi-channel 机械性证据"
    expected_results:
      fewnerd_intra_sub_by_bcs:
        bcs_zero_pct: 0.0
        bcs_low_pct: 1.6
        bcs_medium_pct: 10.6
        bcs_high_pct: 49.4
        rho: 1.0
        p: "<0.001"
      fewrel_intra_sub_by_bcs:
        bcs_zero_pct: 0.0
        bcs_low_pct: 4.2
        bcs_medium_pct: 13.0
        bcs_high_pct: 20.3
        bcs_very_high_pct: 32.3
        rho: 0.954
        p: "<1e-6"
      cross_task:
        ner_rho: 1.0
        re_rho: 0.954
      extra_sub: 0.0
      hallucination_pct: "<3%"
      missed_rate_range: "10-16%"
    result_rationale: >
      Error taxonomy 是 median 档中最无争议的证据（A2 完全成立）。IntraSub 与 BCS 的 
      perfect/near-perfect monotonic 关系直接验证了 multi-channel model 的核心机制：
      confusability 导致 type confusion（IntraSub）而非 detection failure（missed rate 
      不变 10-16%）。几个关键支撑点：(1) extra_sub=0，type confusion 严格是 intra-batch 
      现象，模型只从当前 schema 中选类型；(2) hallucination<3%，LLM 的主错误模式是 
      "选错类型" 而非 "编造实体"；(3) cross-task replication 几乎完美（NER ρ=1.0, 
      RE ρ=0.954），同一机制跨 NER 和 RE。即使在 median 档位，reviewer 也不会质疑这个分析。
      这是论文的 "safe anchor"。
    tables:
      - name: "Table: Error Taxonomy — Few-NERD (NER)"
        content: |
          | BCS Bin  | N_FP | IntraSub% | ExtraSub% | Other%  |
          |----------|------|-----------|-----------|---------|
          | 0        | 6172 | 0.0       | 90.3      | 9.7     |
          | Low      | 2231 | 1.6       | 89.9      | 8.5     |
          | Medium   | 3843 | 10.6      | 78.1      | 11.3    |
          | High     | 6188 | 49.4      | 30.8      | 19.8    |
      - name: "Table: Error Taxonomy — FewRel 80-rel (RE)"
        content: |
          | BCS Bin    | Correct% | IntraSub% | Missed% |
          |------------|----------|-----------|---------|
          | Zero       | 85.7     | 0.0       | 14.3    |
          | Low        | 85.4     | 4.2       | 10.4    |
          | Medium     | 75.7     | 13.0      | 11.3    |
          | High       | 66.7     | 20.3      | 13.0    |
          | Very High  | 52.0     | 32.3      | 15.7    |
      - name: "Table: Cross-task Monotonicity"
        content: |
          | Task | IntraSub vs BCS ρ | p       |
          |------|-------------------|---------|
          | NER  | 1.000             | <0.001  |
          | RE   | 0.954             | <1e-6   |
    figures_description:
      - "Stacked bar: FP composition 从 ExtraSub-dominant (BCS=0) 翻转为 IntraSub-dominant (BCS>0.95)"
      - "Cross-task overlay: NER 和 RE IntraSub curves 近乎平行上升"
    analysis: >
      论文最强的机械性证据，也是 Claim 2 的核心支撑。Cross-task ρ={1.0, 0.954} 是整篇论文
      中最具说服力的数字。Median 档 reviewer 对此无异议。建议在论文中将此作为 Section 4 
      的第一个分析呈现（先建立机制理解，再展示 pairwise/scaling 证据）。

  - name: "SDGD-zero on MAVEN"
    plan_id: "exp-009"
    description: "SDGD-zero 在 MAVEN 168 event types 上测试，对比 single-pass + random"
    expected_results:
      single_pass:
        relaxed_f1: 0.247
        precision: 0.32
        recall: 0.20
        batches: 1
        time_s: 130
      random_batch:
        relaxed_f1: 0.175
        precision: 0.14
        recall: 0.23
        batches: 12
        time_s: 950
      sdgd_zero:
        relaxed_f1: 0.135
        precision: 0.12
        recall: 0.155
        batches: 8
        time_s: 680
      per_type:
        relaxed_f1: 0.110
        precision: 0.07
        recall: 0.30
        batches: 168
        time_s: 9200
    result_rationale: >
      MAVEN 168 types 使所有 decomposition 方法的表现更差，原因层叠：(1) 168 types 产生 
      更多 batches，每次 merge 引入更多冲突——merge amplification 与 batch 数量超线性增长；
      (2) MAVEN event types 语义高度同质（均为 FrameNet 层级，SCS mean=0.216, 
      119 pairs>0.5），SDGD-zero 的 graph coloring 无法有效分离——色数极高，被迫使用 
      大量 small batches 或在同 batch 内保留高 SCS pairs；(3) event trigger boundary 
      本身模糊（exact F1 仅 0.01-0.03），decomposition 后 merge 多个 batch 的 trigger 
      predictions 进一步恶化边界匹配。SDGD-zero F1=0.135 vs single-pass 0.247，退化比
      (0.55) 与 Few-NERD 上一致 (0.24/0.45=0.53)。Random batch 再次优于 SDGD-zero 
      (0.175 vs 0.135)——SDGD 的不均匀 batch size 在 MAVEN 上伤害更大。Per-type (168 batches) 
      recall 最高但 precision 崩溃（0.07），9200s 延迟不可接受。
      Median 档位下，此实验巩固 "merge amplification 是跨任务的结构性障碍"，但同时加深 
      "no practical method" 这一 major weakness。
    tables:
      - name: "Table: SDGD Comparison — MAVEN 168 types"
        content: |
          | Method      | Relaxed F1 | P     | R     | k   | Time(s) |
          |-------------|------------|-------|-------|-----|---------|
          | Single-pass | 0.247      | 0.320 | 0.200 | 1   | 130     |
          | Random      | 0.175      | 0.140 | 0.230 | 12  | 950     |
          | SDGD-zero   | 0.135      | 0.120 | 0.155 | 8   | 680     |
          | Per-type    | 0.110      | 0.070 | 0.300 | 168 | 9200    |
    figures_description:
      - "Bar chart: single-pass 大幅领先，所有 decomposition 方法均为负面"
      - "Cross-dataset comparison: Few-NERD vs MAVEN decomposition penalty 一致"
    analysis: >
      与 Few-NERD 模式完全一致。论文中应将 Few-NERD + MAVEN 的 SDGD 负面结果并排呈现，
      强调 "decomposition penalty 是 task-agnostic 的结构性问题"。同时明确指出 merge 
      strategy 是瓶颈（不是 grouping quality），为 future work 指明方向。Reviewer 的核心
      质疑仍然是 "如果你的方法不 work，这篇论文的 practical value 是什么？"。

  - name: "SDGD-cal on Few-NERD"
    plan_id: "exp-010"
    description: "基于 5-10 个 calibration examples 的 empirical confusability graph，对比 SDGD-zero"
    expected_results:
      sdgd_cal_5shot:
        f1: 0.295
        precision: 0.34
        recall: 0.26
        batches: 5
        time_s: 370
        calibration_overhead_s: 50
      sdgd_cal_10shot:
        f1: 0.315
        precision: 0.36
        recall: 0.28
        batches: 5
        time_s: 370
        calibration_overhead_s: 90
      vs_baselines:
        sdgd_zero_f1: 0.241
        random_batch_f1: 0.301
        single_pass_f1: 0.445
        cal5_vs_zero_pp: "+5.4"
        cal10_vs_zero_pp: "+7.4"
        cal10_vs_single_pass_pp: "-13.0"
    result_rationale: >
      Calibration 用 empirical confusion matrix 替代 embedding SCS，绕过了 embedding 
      选择问题，直接捕捉模型实际 confusion pattern。改善来源：(1) empirical confusion 
      比 SCS 更准确地识别 true confusion pairs（SCS 只解释 ~3% 方差，empirical 解释更多）；
      (2) 基于实际错误的 graph 更 sparse（大部分 type pairs 从不 confused），graph coloring 
      产生更均衡的 batches。但仍远低于 single-pass (-13pp) 的原因不变：merge amplification 
      与 grouping quality 关系不大，是 decomposition 本身的结构性问题——即使完美分组避免了 
      所有 confusion pairs，合并多个 batch 的输出时同一 span 仍会被多个 batch "认领"。
      5-shot vs 10-shot 差异小（0.295 vs 0.315），因为 5 个样本已识别出主要 confusion 
      clusters（person 子类、location 子类）。Median 档位下，SDGD-cal 展示了 "right 
      direction" 但 Δ=+7pp 不构成 practical improvement，reviewer 评价 "interesting 
      diagnostically but not actionable"。
    tables:
      - name: "Table: SDGD-cal vs Baselines (Few-NERD)"
        content: |
          | Method        | F1    | P     | R     | k | Extra(s) |
          |---------------|-------|-------|-------|---|----------|
          | Single-pass   | 0.445 | 0.563 | 0.368 | 1 | 0        |
          | Random        | 0.301 | 0.331 | 0.276 | 8 | 0        |
          | SDGD-zero     | 0.241 | 0.324 | 0.191 | 4 | 0        |
          | SDGD-cal (5)  | 0.295 | 0.340 | 0.260 | 5 | 50       |
          | SDGD-cal (10) | 0.315 | 0.360 | 0.280 | 5 | 90       |
    figures_description:
      - "Bar chart: F1 阶梯 SDGD-zero < SDGD-cal ≈ Random << Single-pass"
      - "Precision-Recall scatter: 所有 decomposition 方法位于 single-pass 的 Pareto 劣势区"
    analysis: >
      SDGD-cal ≈ Random batch 的事实 is telling：即使用最好的 grouping signal，结果也不比
      随机好多少。这进一步证实瓶颈是 merge 不是 grouping。论文中应明确写出这个 implication。
      Reviewer 的追问："为什么不探索 confidence-weighted merge / NMS-style 去重？"——
      这是合理的 future work 方向，v2 已尝试 confidence-gated 但未奏效，说明问题比 
      simple filtering 更深。

  - name: "SDGD-cal on MAVEN"
    plan_id: "exp-011"
    description: "SDGD-cal 在 MAVEN 168 types 上的表现"
    expected_results:
      sdgd_cal_5shot:
        relaxed_f1: 0.165
        precision: 0.15
        recall: 0.185
        batches: 10
        calibration_overhead_s: 200
      sdgd_cal_10shot:
        relaxed_f1: 0.180
        precision: 0.17
        recall: 0.195
        batches: 10
        calibration_overhead_s: 380
      vs_baselines:
        single_pass_f1: 0.247
        sdgd_zero_f1: 0.135
        cal10_vs_zero_pp: "+4.5"
        cal10_vs_single_pass_pp: "-6.7"
    result_rationale: >
      MAVEN 上 calibration 的边际改善比 Few-NERD 更小（+4.5pp vs +7.4pp），原因：
      (1) 168 types 的 confusion space 更大（14028 pairs），5-10 个 calibration samples 
      覆盖率更低——每个 sample 最多涉及 ~10 types，需要 O(168) 个 samples 才能充分覆盖；
      (2) MAVEN 语义同质性导致 confusion graph 极其 dense（几乎所有 type pairs 都有非零 
      confusion），graph coloring 的 chromatic number 很高，无论怎么分组都有大量 high-SCS 
      pairs 共存；(3) 200-380s 的 calibration overhead 在 168 types 上不可忽略，但换来的 
      仅 4.5pp 改善，投资回报率极低。SDGD-cal 仍远低于 single-pass (-6.7pp)。
      Cross-task 一致的负面结果强化了结论，但也强化了 "no practical method" 的弱点。
    tables:
      - name: "Table: SDGD-cal vs Baselines (MAVEN)"
        content: |
          | Method        | Relaxed F1 | k  | Calibration(s) |
          |---------------|------------|----|----------------|
          | Single-pass   | 0.247      | 1  | 0              |
          | Random        | 0.175      | 12 | 0              |
          | SDGD-zero     | 0.135      | 8  | 0              |
          | SDGD-cal (5)  | 0.165      | 10 | 200            |
          | SDGD-cal (10) | 0.180      | 10 | 380            |
    figures_description:
      - "Cross-dataset SDGD comparison: Few-NERD 和 MAVEN bar charts 并排，模式一致"
    analysis: >
      建议在论文中将 exp-009 和 exp-011 合并为一个 "SDGD Results" subsection，呈现 
      cross-task 一致的 hierarchy: single-pass > random ≈ cal > zero。
      明确定位为 "negative result with diagnostic value"——理解 WHY decomposition fails 
      本身是贡献，指向 calibration-aware merge (非 calibration-aware grouping) 作为 
      correct next step。

  - name: "Random Batching Ablation"
    plan_id: "exp-013"
    description: "与 SDGD 相同 batch count k 的 random composition，隔离 confusability-aware grouping 的增量"
    expected_results:
      fewnerd_k4:
        random_f1: 0.305
        sdgd_zero_f1: 0.241
        delta_pp: "+6.4"
      fewnerd_k8:
        random_f1: 0.295
        sdgd_zero_f1: 0.220
        delta_pp: "+7.5"
      maven_k8:
        random_f1: 0.175
        sdgd_zero_f1: 0.135
        delta_pp: "+4.0"
      single_pass_f1_fewnerd: 0.445
      single_pass_f1_maven: 0.247
    result_rationale: >
      Random batching 在所有条件下优于 SDGD-zero，看似反直觉但有清晰解释：
      (1) SDGD-zero 的 graph coloring + min_batch_size 约束产生高度不均匀的 batch sizes——
      某些 batch 仅含 3-4 types，prompt 中类型太少时模型缺乏任务范围 context，对每个类型 
      过度 predict（high recall, terrible precision）；random batching 的 batch size 更均匀，
      避免了这一退化模式；(2) SDGD-zero 将所有 "hard" (high-SCS) types 集中到同一个 
      batch，这些 batch 的 precision 崩溃；random 分散了 hard pairs，每个 batch 混合 
      easy+hard，整体更 balanced；(3) confusability-aware grouping 的正确 operationalization 
      应是 "将 confusable pairs 分开"，但 SDGD-zero 的贪心 coloring 在约束下反而集中了 
      难题。这说明 SDGD-zero 的分组算法有 design flaw，不否定 confusability signal 本身。
      Median 档位下，"SDGD-zero < random" 是 reviewer 最容易攻击的点之一。
    tables:
      - name: "Table: Random vs SDGD-zero Ablation"
        content: |
          | Dataset  | k | Random F1 | SDGD-zero F1 | Single-pass F1 |
          |----------|---|-----------|--------------|----------------|
          | Few-NERD | 4 | 0.305     | 0.241        | 0.445          |
          | Few-NERD | 8 | 0.295     | 0.220        | 0.445          |
          | MAVEN    | 8 | 0.175     | 0.135        | 0.247          |
    figures_description:
      - "Bar chart: 三组对比（k=4, k=8, MAVEN k=8），random 始终优于 SDGD-zero"
    analysis: >
      关键 takeaway 不是 "confusability-aware grouping 无用"，而是 "当前的 SDGD-zero 
      实现的分组策略有副作用（batch size 不均匀、hard type 集中化）抵消了 grouping 收益"。
      论文应 (1) 诚实报告 random > SDGD-zero；(2) 分析原因（batch size distribution, 
      hard-batch concentration）；(3) 指出 all decomposition << single-pass，真正的瓶颈是 
      merge 不是 grouping。Reviewer 可能追问 "为什么不修复 SDGD 的 batch size 问题？"——
      合理的 rebuttal 是 exp-010 的 SDGD-cal 部分解决了这个问题但仍低于 single-pass。

  - name: "Per-type Splitting (UniNER-style)"
    plan_id: "exp-014"
    description: "每 batch 仅含 1 type，decomposition 的理论上限"
    expected_results:
      fewnerd:
        f1: 0.290
        precision: 0.195
        recall: 0.585
        batches: 66
        time_s: 2550
        intra_sub_rate: 0.0
        recall_vs_single_pass_pp: "+21.7"
        precision_vs_single_pass_pp: "-36.8"
        f1_vs_single_pass_pp: "-15.5"
      maven:
        relaxed_f1: 0.145
        precision: 0.085
        recall: 0.46
        batches: 168
        time_s: 9500
    result_rationale: >
      Per-type splitting 完全消除了 type confusion (IntraSub=0)——每个 batch 只有一个类型，
      不可能把 entity 标为 "wrong" type。这验证了 multi-channel model 的 Channel 1 预测：
      Recall 从 0.368 跃升至 0.585 (+21.7pp)，因为每个 prompt 只需关注一个类型，
      attention 不被稀释，不遗漏。但 Precision 从 0.563 崩溃到 0.195 (-36.8pp)——
      66 个 batch 的 union merge 引入大量冲突：同一 text span 被 person-scholar、
      person-scientist、person-other 各自 "认领"，union merge 保留所有 predictions，
      precision 崩溃。F1 净效果为负 (-15.5pp)。
      MAVEN 168 types 更极端——recall 高但 precision 更低（0.085），因为 168 个 single-type 
      batch 的 merge 冲突呈 O(k²) 增长。
      这清晰展示了 decomposition 的 fundamental tradeoff：分解减少 miss (Channel 1 benefit)，
      但 merge 产生 false positives (new Channel 3 problem)。当前所有 merge strategy 
      （union, confidence-gated）都不能解决 O(k) batches 的冲突。
    tables:
      - name: "Table: Full Decomposition Spectrum (Few-NERD)"
        content: |
          | Method      | F1    | P     | R     | k  | IntraSub | Time(s) |
          |-------------|-------|-------|-------|----|----------|---------|
          | Single-pass | 0.445 | 0.563 | 0.368 | 1  | baseline | 79      |
          | Random (k=8)| 0.295 | 0.330 | 0.270 | 8  | moderate | 494     |
          | SDGD-zero   | 0.241 | 0.324 | 0.191 | 4  | low      | 261     |
          | SDGD-cal    | 0.315 | 0.360 | 0.280 | 5  | low      | 460     |
          | Per-type    | 0.290 | 0.195 | 0.585 | 66 | 0        | 2550    |
    figures_description:
      - "Precision-Recall tradeoff: per-type 在 high-recall/low-precision 极端，single-pass 在 balanced 区"
      - "Stacked bar: recall gain vs precision loss，per-type 的 precision loss 完全 dominate"
    analysis: >
      Per-type 的 recall 优势是 decomposition 正确直觉的最好证据——问题确实在 merge。
      论文结构建议：先展示 per-type 的 recall gain (证明 decomposition 有理论价值)，
      再展示所有方法的 precision collapse (证明 merge amplification 是瓶颈)，
      最后指出 "future work needs better merge, not better grouping"。
      Reviewer 会欣赏这个清晰的 ablation 分析。1-2 位 reviewer 仍会标注 "the paper 
      identifies the problem but doesn't solve it" 作为 major weakness，这是 median 档
      避不开的。

  - name: "SCS Validation"
    plan_id: "exp-015"
    description: "Spearman/Kendall correlation between embedding SCS 和 empirical confusion matrix"
    expected_results:
      all_pairs:
        n: 1953
        qwen3_spearman: 0.168
        qwen3_p: "7.3e-14"
        qwen3_kendall: 0.135
        minilm_spearman: 0.144
        minilm_p: "1.7e-10"
        minilm_kendall: 0.115
      nonzero_only:
        n: 216
        qwen3_spearman: 0.272
        qwen3_p: "5.0e-5"
        qwen3_kendall: 0.200
        minilm_spearman: 0.306
        minilm_p: "4.6e-6"
        minilm_kendall: 0.228
      variance_explained:
        all_pairs_r_squared: "2.8-4.8%"
        nonzero_r_squared: "7.4-9.4%"
    result_rationale: >
      SCS 是有效但不完美的 confusion proxy。All-pairs ρ 偏低（0.14-0.17）的根本原因是 
      data 极度 zero-inflated：88.9% 的 type pairs 从未被混淆（confusion=0），产生大量 
      ties 压缩 rank correlation。Nonzero-only ρ 跳升到 0.27-0.31，说明 SCS 能有效区分 
      "哪些 pairs 被混淆得更多" 但不太能预测 "哪些 pairs 会被混淆"。
      Qwen3 在 all-pairs 上更好（ρ=0.168 vs 0.144）——extraction model 的 embedding 
      更好地捕捉 "是否会混淆" 的 threshold，因为 embedding space 与 model 的 internal 
      representation 对齐。MiniLM 在 nonzero-only 上更好（ρ=0.306 vs 0.272）——sentence 
      similarity model 的 fine-grained similarity gradient 更平滑，更好地排序 confusion 
      程度。
      Median 档位下，reviewer 的主要质疑是 R²=3-5%：如果你的 proxy 只解释 3-5% 的方差，
      基于它构建的 SDGD 分组怎么可能有效？这恰好与 SDGD-zero 的失败一致——SCS 作为 grouping 
      signal 太 noisy。论文应将此定位为 "validating the existence of the signal" 而非 
      "validating its practical sufficiency"，并指向 SDGD-cal (empirical confusion) 
      作为正确的 operationalization 路径。
    tables:
      - name: "Table: SCS → Empirical Confusion Validation"
        content: |
          | Subset        | Embedding | Spearman ρ | p        | Kendall τ | R²     |
          |---------------|-----------|------------|----------|-----------|--------|
          | All (n=1953)  | Qwen3     | 0.168      | 7.3e-14  | 0.135     | ~4.8%  |
          | All (n=1953)  | MiniLM    | 0.144      | 1.7e-10  | 0.115     | ~2.8%  |
          | Nonzero (216) | Qwen3     | 0.272      | 5.0e-5   | 0.200     | ~7.4%  |
          | Nonzero (216) | MiniLM    | 0.306      | 4.6e-6   | 0.228     | ~9.4%  |
    figures_description:
      - "SCS vs confusion scatter: 大量零值集中在 x 轴，nonzero 区域显示 positive trend"
      - "Embedding 对比: Qwen3 vs MiniLM 的 SCS-confusion curves 在 nonzero 区域交叉"
    analysis: >
      SCS validation 支撑了 "confusability signal exists" 但也暴露了 "signal is weak for 
      practical use"。这与 SDGD 的负面结果形成一致叙事：pairwise SCS 作为分析工具有效
      （cross-task 显著），作为工程工具不足（R²太低）。论文应诚实呈现这个 gap，并将 
      SDGD-cal (bypassing embedding entirely) 作为 pragmatic 替代方案。
      Reviewer 可能追问 AUC（SCS 预测 nonzero confusion 的分类能力），预估 AUC≈0.65-0.70，
      属于 "above chance but far from reliable" 水平。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fd7ee98-a190-4468-a167-01f95ecc042b",
  "isSidechain": false,
  "requestId": "req_011Cb5saJ7tkdxc5MHDqCJu1",
  "type": "assistant",
  "uuid": "7cbe5d2d-c731-452e-ae61-5f9da0125653",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "c3c703d5-f588-4e67-b762-e7ebe9792a81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RANoYDe9So1E4CntECBcRN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26578,
      "cache_read_input_tokens": 11841,
      "output_tokens": 22716,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26578,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 22716,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26578
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心假设部分验证，部分 reviewer 质疑效应量或覆盖面，论文落入 EMNLP Findings 或需 rebuttal 挽救 核心假设：[\"A1 部分成立: Pairwise r=0.11-0.13 被质疑为'统计显著但实际意义有限'，需补充 FewRel 的大效应量（Δ=-31pp）来说服\", '…",
  "leafUuid": "7cbe5d2d-c731-452e-ae61-5f9da0125653",
  "sessionId": "c3c703d5-f588-4e67-b762-e7ebe9792a81"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier schema confusability study with cross-task validation",
  "sessionId": "c3c703d5-f588-4e67-b762-e7ebe9792a81"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心假设部分验证，部分 reviewer 质疑效应量或覆盖面，论文落入 EMNLP Findings 或需 rebuttal 挽救 核心假设：[\"A1 部分成立: Pairwise r=0.11-0.13 被质疑为'统计显著但实际意义有限'，需补充 FewRel 的大效应量（Δ=-31pp）来说服\", '…",
  "leafUuid": "7cbe5d2d-c731-452e-ae61-5f9da0125653",
  "sessionId": "c3c703d5-f588-4e67-b762-e7ebe9792a81"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier schema confusability study with cross-task validation",
  "sessionId": "c3c703d5-f588-4e67-b762-e7ebe9792a81"
}
```

---
