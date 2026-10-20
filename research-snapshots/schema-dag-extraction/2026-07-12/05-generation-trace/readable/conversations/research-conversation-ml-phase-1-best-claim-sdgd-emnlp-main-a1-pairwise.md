# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：两条 claim 均以当前数据充分支撑，SDGD 负面结果被视为方法论贡献，论文被 EMNLP Main 接收 核心假设：['A1: Pairwise 

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/1e00b948-dfc5-4298-ba2f-145c6f5d5244.jsonl`
- **Structured JSON:** [`243cb6c359d80925bfa6.json`](../../sessions/24/243cb6c359d80925bfa6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T07:38:43.213Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T07:38:43.213Z",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：两条 claim 均以当前数据充分支撑，SDGD 负面结果被视为方法论贡献，论文被 EMNLP Main 接收\n核心假设：['A1: Pairwise SCS→confusion 的 r=0.11-0.13 被接受为有意义的效应量（reviewers 认可 noise floor 高的 IE 任务中此量级合理）', 'A2: 多通道退化模型（count→recall, confusability→type confusion）的正交性被 error taxonomy ρ≥0.95 充分证明', 'A3: FewRel 80-rel 的 3.4× amplification 被视为 schema complexity scaling 的强证据', 'A4: LLaMA FewRel 复现（Δ=-27.1pp, 87% of Qwen3）被接受为充分的 multi-model 验证', 'A5: MAVEN per-type centrality confound 被视为方法论贡献（何时聚合度量失效）而非负面证据', 'A6: SDGD 负面结果 + merge amplification 分析被视为诚实贡献（类比 negative results track）', 'A7: 纯实证研究格式被 EMNLP 接受（类比 Lost in the Middle, TACL 2024）']\n关键指标范围：{'arr_avg_score': [3.5, 4.0], 'claims_fully_supported': [2, 2], 'major_reviewer_weaknesses': [0, 1], 'cross_task_significant_replications': [3, 4], 'multi_model_effect_consistency': [0.85, 1.0], 'venue_probability_main': [0.55, 0.75], 'venue_probability_findings_or_above': [0.85, 0.95], 'rebuttal_flip_probability': [0.8, 1.0]}\n叙事方向：原始 framing 完全成立。标题级 claim: \"Pairwise type confusability independently predicts LLM IE degradation across three tasks and two models.\" 两条 claim 均以强证据支撑: Claim 1 靠 pairwise 相关性 + FewRel BCS-controlled gap + DocRED replication; Claim 2 靠 error taxonomy cross-task ρ≥0.95。SDGD 负面结果作为 Section 6 讨论， 指向 calibration-based 方向。MAVEN centrality confound 作为独立的方法论发现。 Embedding ablation 2×3 matrix 作为实践指南。不需要调整 claim 强度。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: schema-dag-extraction\n\n## paper_framing.md\n\n# Paper Framing — schema-dag-extraction\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\n- Commitment deadline: August 2, 2026\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\n- Deadline: ARR May 25, 2026 (10 days from today)\n\n## Core Claims (2 claims) — Revised per D019\n\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\n\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\n\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \"why naive decomposition fails\" is itself a contribution.\n\n## Story Spine — Revised per D012\n\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\n\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\n\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.\n\n- **Three-task validation**:\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\n\n- **Headline result template**: \"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid.\"\n\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\n\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\n\nThese channels are orthogonal and independently addressable.\n\n**Pairwise vs Aggregated Confusability**:\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\n\n## Evidence Hierarchy (D012)\n\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\n\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\n\n**Few-NERD (NER)** — Qwen3 embeddings:\n- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation\n- Nonzero-only Spearman ρ=0.272 (p=5e-5)\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\n- Immune to type frequency confound (operates at type-pair level)\n\n**MAVEN (ED)** — MiniLM embeddings:\n- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\n- Cross-task replication on same-domain schema\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\n\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\n\nLarge effect size, cross-task (RE), scaling with schema complexity:\n\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\n\n**16-rel sanity check** (exp_fewrel_formal):\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\n\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\n\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\n\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\n\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\n\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\n\nMethodological case study on when aggregated confusability measures fail:\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\n- This is stronger than \"domain boundary\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\n\n### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)\n\nIntraSub rate monotonically increases with BCS on both NER and RE:\n\n**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0\n**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)\n- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon\n- Same mechanism, different absolute magnitudes — consistent with cross-task expectations\n\nAdditional from extreme batch design:\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\n\n## Embedding Ablation (D010)\n\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\n\n### Per-type (Layer 2)\n| | Few-NERD | FewRel | MAVEN |\n|---|---|---|---|\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\n\n### Pairwise (Layer 1)\n| | Few-NERD | MAVEN |\n|---|---|---|\n| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |\n| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |\n\n### SCS→Empirical Confusion Validation (exp-015 fast)\n| | Qwen3 | MiniLM |\n|---|---|---|\n| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |\n| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |\n\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \"Lost in the Middle\" (TACL 2024).\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy | Experiment |\n|---------|------------------|------------|\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]\n    on Few-NERD with Qwen3-32B-FP8'\n  priority: P0\n  gpu_budget_hours: 3.5\n  deps: []\n  registry_id: exp001_count_baseline\n  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction\n    at low counts.\n  status: DONE\n  conclusion: success\n  metrics:\n    diagnosis: char offset 96.5% fabricated by model\n    text_match_reeval:\n      count_1:\n        f1: 0.184\n        precision: 0.105\n        recall: 0.72\n        pred_gold_ratio: 6.85\n      count_2:\n        f1: 0.123\n        precision: 0.068\n        recall: 0.698\n        pred_gold_ratio: 10.33\n      count_6:\n        f1: 0.155\n        precision: 0.088\n        recall: 0.62\n        pred_gold_ratio: 7.02\n      count_12:\n        f1: 0.246\n        precision: 0.16\n        recall: 0.539\n        pred_gold_ratio: 3.38\n      count_22:\n        f1: 0.322\n        precision: 0.232\n        recall: 0.527\n        pred_gold_ratio: 2.27\n      count_44:\n        f1: 0.473\n        precision: 0.414\n        recall: 0.551\n        pred_gold_ratio: 1.33\n      count_64:\n        f1: 0.463\n        precision: 0.52\n        recall: 0.418\n        pred_gold_ratio: 0.8\n    key_finding: recall monotonically decreases (0.72→0.42), precision monotonically\n      increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at\n      count_44\n    wrong_type_trend: 'type confusion increases with count: 0→2434, supports confusability\n      hypothesis'\n    spurious_dominant: spurious FPs (text in source but not entity) dominate at low\n      count, not hallucination\n    conclusion_text_match: F1 curve inversion caused by over-prediction confound,\n      NOT absence of confusability effect. Recall curve + type confusion pattern support\n      hypothesis.\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,\n    25 random + extreme batches on Few-NERD'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  registry_id: exp002_confusability_controlled\n  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion\n    rate 10-28x.\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp2_reeval_results.json (text_match, CLEAN)\n    primary_recall_vs_bcs:\n      count_6:\n        r: 0.2754\n        p: 0.1644\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.2219\n        p: 0.266\n        n: 27\n        verdict: FAIL\n      partial:\n        r: 0.2522\n        p: 0.0658\n        n: 54\n        verdict: FAIL\n    secondary_f1_vs_bcs:\n      count_6:\n        r: 0.1754\n        p: 0.3814\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.5012\n        p: 0.0077\n        n: 27\n        verdict: PASS\n      partial:\n        r: 0.3025\n        p: 0.0262\n        n: 54\n        verdict: PASS\n    mechanistic_confusion_rate:\n      random_batches:\n        count_6_high: 0.0157\n        count_6_low: 0.0088\n        ratio_6: 1.7\n        count_12_high: 0.0304\n        count_12_low: 0.0131\n        ratio_12: 2.4\n      extreme_batches:\n        count_6_high: 0.0728\n        count_6_low: 0.0014\n        ratio_6: 27.5\n        count_12_high: 0.048\n        count_12_low: 0.0061\n        ratio_12: 9.9\n      verdict: PASS\n    pairwise_confusion_analysis:\n      all:\n        n_pairs: 1953\n        pearson_r: 0.156\n        pearson_p: 4.6e-12\n        spearman_rho: 0.16\n        spearman_p: 1.3e-12\n      count_6:\n        n_pairs: 1770\n        pearson_r: 0.078\n        pearson_p: 0.001\n      count_12:\n        n_pairs: 1953\n        pearson_r: 0.147\n        pearson_p: 6.7e-11\n      nonzero_only:\n        all_spearman_rho: 0.254\n        all_spearman_p: 1.1e-06\n        count_12_pearson_r: 0.212\n        count_12_p: 0.00034\n      top_confused_pair: person-other <-> person-politician (BCS=0.934, confusion=156)\n    per_type_analysis:\n      n_types: 63\n      filter: freq>=5\n      micro_f1_vs_bcs:\n        pearson_r: -0.1828\n        pearson_p: 0.1516\n        spearman_rho: -0.2927\n        spearman_p: 0.0199\n        partial_r_ctrl_logfreq: -0.1998\n        partial_p: 0.1163\n      mean_f1_vs_bcs:\n        pearson_r: -0.1374\n        pearson_p: 0.283\n        spearman_rho: -0.2412\n        spearman_p: 0.0568\n        partial_r_ctrl_logfreq: -0.1428\n        partial_p: 0.2641\n      quartile_comparison:\n        low_bcs_cutoff: 0.798\n        high_bcs_cutoff: 0.827\n        low_bcs_f1: 0.3098\n        high_bcs_f1: 0.2275\n        delta_f1: -0.0823\n        low_bcs_freq: 2134\n        high_bcs_freq: 2049\n      confound_check:\n        bcs_vs_logfreq_r: 0.042\n        bcs_vs_logfreq_p: 0.74\n        logfreq_vs_f1_r: 0.25\n        logfreq_vs_f1_p: 0.048\n      verdict: Direction supports hypothesis. Spearman significant (p=0.02). Frequency\n        confound absent at type level (r=0.04).\n    overall_verdict: PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE\n      STRONG PASS, PER-TYPE DIRECTIONAL PASS\n- id: exp-003a\n  claim:\n  - 1\n  - 2\n  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination\n    instruction. Re-run exp1+exp2.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp003a_prompt_v2_rerun\n  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_mode: text_match\n    exp1_text_match:\n      count_1:\n        f1: 0.323\n        precision: 0.216\n        recall: 0.641\n        pred_gold_ratio: 2.97\n        n_batches: 64\n      count_2:\n        f1: 0.273\n        precision: 0.18\n        recall: 0.56\n        pred_gold_ratio: 3.11\n        n_batches: 5\n      count_6:\n        f1: 0.306\n        precision: 0.226\n        recall: 0.475\n        pred_gold_ratio: 2.1\n        n_batches: 5\n      count_12:\n        f1: 0.347\n        precision: 0.367\n        recall: 0.329\n        pred_gold_ratio: 0.9\n        n_batches: 5\n      count_22:\n        f1: 0.299\n        precision: 0.339\n        recall: 0.267\n        pred_gold_ratio: 0.79\n        n_batches: 5\n      count_44:\n        f1: 0.445\n        precision: 0.506\n        recall: 0.396\n        pred_gold_ratio: 0.78\n        n_batches: 5\n      count_64:\n        f1: 0.414\n        precision: 0.648\n        recall: 0.304\n        pred_gold_ratio: 0.47\n        n_batches: 5\n    exp2_text_match:\n      count_6:\n        f1: 0.32\n        precision: 0.26\n        recall: 0.416\n        pred_gold_ratio: 1.6\n        n_batches: 27\n      count_12:\n        f1: 0.306\n        precision: 0.291\n        recall: 0.323\n        pred_gold_ratio: 1.11\n        n_batches: 27\n    vs_exp001_delta:\n      count_1:\n        f1_delta: +0.139 (+76%)\n        precision_delta: +0.111 (+106%)\n        recall_delta: -0.079 (-11%)\n        overpred_fix: 6.85→2.97\n      count_6:\n        f1_delta: +0.151 (+97%)\n        precision_delta: +0.138 (+157%)\n        recall_delta: -0.145 (-23%)\n      count_12:\n        f1_delta: +0.101 (+41%)\n        precision_delta: +0.207 (+129%)\n        recall_delta: -0.210 (-39%)\n      count_44:\n        f1_delta: -0.028 (-6%)\n        precision_delta: +0.092 (+22%)\n        recall_delta: -0.155 (-28%)\n      count_64:\n        f1_delta: -0.049 (-11%)\n        precision_delta: +0.128 (+25%)\n        recall_delta: -0.114 (-27%)\n    key_finding: 'V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x\n      to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1).\n      But over-corrected at high counts: under-prediction (pred/gold<1) caused recall\n      drops of 27-39%, slightly lowering F1 at count_22-64.'\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MAVEN confusability study: count curve + within-count BCS correlation\n    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core\n    finding cross-task (NER→ED) with larger type space and known sibling confusion\n    (14.6-19.8%).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp-004\n  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs\n    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy\n    structure.'\n  status: DONE\n  conclusion: success\n  metrics:\n    n_event_types: 168\n    n_pairs: 14028\n    scs_mean: 0.2161\n    scs_std: 0.103\n    scs_max: 0.8368\n    scs_median: 0.2121\n    scs_q90: 0.3457\n    scs_q95: 0.3892\n    pairs_above_0.5: 119\n    pct_above_0.5: 0.85\n    train_docs: 2913\n    train_mentions: 77993\n    valid_docs: 710\n    valid_mentions: 18904\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n  status: planned\n- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n  status: planned\n- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.\n  status: planned\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional\n    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model\n    generalizability.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-003a\n  registry_id: exp012_llama_8b_r3\n  status: DONE\n  conclusion: failed\n- id: exp-016\n  claim:\n  - 1\n  - 2\n  description: 'FewRel cross-task replication: count curve + BCS correlation on FewRel\n    RE (80 relation types with --use_all). Replicates confusability effect NER→RE.\n    Pilot (fewrel_pilot) confirmed signal; formal run with full count curve [1,4,8,16,32,64,80].'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp_fewrel_formal\n  status_note: RUNNING (16-rel version). Will rerun with --use_all for 80-rel full\n    count curve after current run completes.\n  status: DONE\n  conclusion: success\n  metrics:\n    note: 16-rel sanity check only\n    exp1:\n      count_1:\n        mean_acc: 0.904\n        n_batches: 16\n      count_4:\n        mean_acc: 0.932\n        n_batches: 5\n      count_8:\n        mean_acc: 0.867\n        n_batches: 5\n      count_16:\n        mean_acc: 0.778\n        n_batches: 5\n        bcs: 0.9\n        zero_variance: true\n    exp2:\n      count_8_low_bcs:\n        acc: 0.889\n        bcs: 0.782\n      count_8_high_bcs:\n        acc: 0.798\n        bcs: 0.892\n      delta_bcs_effect: -0.091\n    trend: 'count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8%\n      (Δ=-9.1pp)'\n- id: exp-008\n  claim:\n  - 3\n  description: 'SDGD-zero on Few-NERD: confusability-minimizing batch composition\n    via embedding SCS + graph coloring. Compare vs single-pass full-schema baseline.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-003a\n  registry_id: exp008_sdgd_v2_fewnerd\n  status_note: 'DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass\n    baseline on Few-NERD. R1 (exp008_sdgd_zero_fewnerd) failed with script error.'\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 79\n    random_batch:\n      f1: 0.3007\n      precision: 0.3307\n      recall: 0.2758\n      batches: 8\n      time_s: 494\n    sdgd_zero:\n      f1: 0.2407\n      precision: 0.3244\n      recall: 0.1913\n      batches: 4\n      time_s: 261\n    per_type: killed before completion (3/4 modes done, Director approved kill)\n    vs_v1: confidence-gated merge did not improve over union merge. sdgd_zero 0.241\n      vs v1 0.251, random_batch 0.301 vs v1 0.320\n    key_finding: SDGD v2 confidence-gated merge + min_batch_size=8 failed to beat\n      single_pass baseline (F1=0.445). Both v1 and v2 confirm decomposition hurts\n      precision more than it helps recall. Claim 3 (SDGD framework) needs fundamental\n      rethink.\n- id: exp-009\n  claim:\n  - 3\n  description: 'SDGD-zero on MAVEN: confusability-minimizing batch composition on\n    168 event types. Compare vs single-pass + random batching. Cross-task validation\n    of SDGD framework (NER→ED).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-004\n  - exp-008\n  status: planned\n- id: exp-010\n  claim:\n  - 3\n  description: 'SDGD-cal on Few-NERD: empirical confusability from 5-10 calibration\n    examples (no gradients). Compare vs SDGD-zero.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-008\n  status: planned\n- id: exp-011\n  claim:\n  - 3\n  description: 'SDGD-cal on MAVEN: empirical confusability with calibration on 168\n    event types. Full comparison table.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-009\n  - exp-010\n  status: planned\n- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n  status: planned\n- id: exp-014\n  claim:\n  - 3\n  description: 'Ablation: per-type splitting (UniNER-style, 1 type per batch). Upper\n    bound on decomposition benefit. Reveals latency vs quality tradeoff.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n  status: planned\n- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp001_count_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    diagnosis: char offset 96.5% fabricated by model\n    text_match_reeval:\n      count_1:\n        f1: 0.184\n        precision: 0.105\n        recall: 0.72\n        pred_gold_ratio: 6.85\n      count_2:\n        f1: 0.123\n        precision: 0.068\n        recall: 0.698\n        pred_gold_ratio: 10.33\n      count_6:\n        f1: 0.155\n        precision: 0.088\n        recall: 0.62\n        pred_gold_ratio: 7.02\n      count_12:\n        f1: 0.246\n        precision: 0.16\n        recall: 0.539\n        pred_gold_ratio: 3.38\n      count_22:\n        f1: 0.322\n        precision: 0.232\n        recall: 0.527\n        pred_gold_ratio: 2.27\n      count_44:\n        f1: 0.473\n        precision: 0.414\n        recall: 0.551\n        pred_gold_ratio: 1.33\n      count_64:\n        f1: 0.463\n        precision: 0.52\n        recall: 0.418\n        pred_gold_ratio: 0.8\n    key_finding: recall monotonically decreases (0.72→0.42), precision monotonically\n      increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at\n      count_44\n    wrong_type_trend: 'type confusion increases with count: 0→2434, supports confusability\n      hypothesis'\n    spurious_dominant: spurious FPs (text in source but not entity) dominate at low\n      count, not hallucination\n    conclusion_text_match: F1 curve inversion caused by over-prediction confound,\n      NOT absence of confusability effect. Recall curve + type confusion pattern support\n      hypothesis.\n- exp_id: exp002_confusability_controlled\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp2_reeval_results.json (text_match, CLEAN)\n    primary_recall_vs_bcs:\n      count_6:\n        r: 0.2754\n        p: 0.1644\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.2219\n        p: 0.266\n        n: 27\n        verdict: FAIL\n      partial:\n        r: 0.2522\n        p: 0.0658\n        n: 54\n        verdict: FAIL\n    secondary_f1_vs_bcs:\n      count_6:\n        r: 0.1754\n        p: 0.3814\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.5012\n        p: 0.0077\n        n: 27\n        verdict: PASS\n      partial:\n        r: 0.3025\n        p: 0.0262\n        n: 54\n        verdict: PASS\n    mechanistic_confusion_rate:\n      random_batches:\n        count_6_high: 0.0157\n        count_6_low: 0.0088\n        ratio_6: 1.7\n        count_12_high: 0.0304\n        count_12_low: 0.0131\n        ratio_12: 2.4\n      extreme_batches:\n        count_6_high: 0.0728\n        count_6_low: 0.0014\n        ratio_6: 27.5\n        count_12_high: 0.048\n        count_12_low: 0.0061\n        ratio_12: 9.9\n      verdict: PASS\n    pairwise_confusion_analysis:\n      all:\n        n_pairs: 1953\n        pearson_r: 0.156\n        pearson_p: 4.6e-12\n        spearman_rho: 0.16\n        spearman_p: 1.3e-12\n      count_6:\n        n_pairs: 1770\n        pearson_r: 0.078\n        pearson_p: 0.001\n      count_12:\n        n_pairs: 1953\n        pearson_r: 0.147\n        pearson_p: 6.7e-11\n      nonzero_only:\n        all_spearman_rho: 0.254\n        all_spearman_p: 1.1e-06\n        count_12_pearson_r: 0.212\n        count_12_p: 0.00034\n      top_confused_pair: person-other <-> person-politician (BCS=0.934, confusion=156)\n    per_type_analysis:\n      n_types: 63\n      filter: freq>=5\n      micro_f1_vs_bcs:\n        pearson_r: -0.1828\n        pearson_p: 0.1516\n        spearman_rho: -0.2927\n        spearman_p: 0.0199\n        partial_r_ctrl_logfreq: -0.1998\n        partial_p: 0.1163\n      mean_f1_vs_bcs:\n        pearson_r: -0.1374\n        pearson_p: 0.283\n        spearman_rho: -0.2412\n        spearman_p: 0.0568\n        partial_r_ctrl_logfreq: -0.1428\n        partial_p: 0.2641\n      quartile_comparison:\n        low_bcs_cutoff: 0.798\n        high_bcs_cutoff: 0.827\n        low_bcs_f1: 0.3098\n        high_bcs_f1: 0.2275\n        delta_f1: -0.0823\n        low_bcs_freq: 2134\n        high_bcs_freq: 2049\n      confound_check:\n        bcs_vs_logfreq_r: 0.042\n        bcs_vs_logfreq_p: 0.74\n        logfreq_vs_f1_r: 0.25\n        logfreq_vs_f1_p: 0.048\n      verdict: Direction supports hypothesis. Spearman significant (p=0.02). Frequency\n        confound absent at type level (r=0.04).\n    overall_verdict: PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE\n      STRONG PASS, PER-TYPE DIRECTIONAL PASS\n- exp_id: exp003a_prompt_v2_rerun\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_mode: text_match\n    exp1_text_match:\n      count_1:\n        f1: 0.323\n        precision: 0.216\n        recall: 0.641\n        pred_gold_ratio: 2.97\n        n_batches: 64\n      count_2:\n        f1: 0.273\n        precision: 0.18\n        recall: 0.56\n        pred_gold_ratio: 3.11\n        n_batches: 5\n      count_6:\n        f1: 0.306\n        precision: 0.226\n        recall: 0.475\n        pred_gold_ratio: 2.1\n        n_batches: 5\n      count_12:\n        f1: 0.347\n        precision: 0.367\n        recall: 0.329\n        pred_gold_ratio: 0.9\n        n_batches: 5\n      count_22:\n        f1: 0.299\n        precision: 0.339\n        recall: 0.267\n        pred_gold_ratio: 0.79\n        n_batches: 5\n      count_44:\n        f1: 0.445\n        precision: 0.506\n        recall: 0.396\n        pred_gold_ratio: 0.78\n        n_batches: 5\n      count_64:\n        f1: 0.414\n        precision: 0.648\n        recall: 0.304\n        pred_gold_ratio: 0.47\n        n_batches: 5\n    exp2_text_match:\n      count_6:\n        f1: 0.32\n        precision: 0.26\n        recall: 0.416\n        pred_gold_ratio: 1.6\n        n_batches: 27\n      count_12:\n        f1: 0.306\n        precision: 0.291\n        recall: 0.323\n        pred_gold_ratio: 1.11\n        n_batches: 27\n    vs_exp001_delta:\n      count_1:\n        f1_delta: +0.139 (+76%)\n        precision_delta: +0.111 (+106%)\n        recall_delta: -0.079 (-11%)\n        overpred_fix: 6.85→2.97\n      count_6:\n        f1_delta: +0.151 (+97%)\n        precision_delta: +0.138 (+157%)\n        recall_delta: -0.145 (-23%)\n      count_12:\n        f1_delta: +0.101 (+41%)\n        precision_delta: +0.207 (+129%)\n        recall_delta: -0.210 (-39%)\n      count_44:\n        f1_delta: -0.028 (-6%)\n        precision_delta: +0.092 (+22%)\n        recall_delta: -0.155 (-28%)\n      count_64:\n        f1_delta: -0.049 (-11%)\n        precision_delta: +0.128 (+25%)\n        recall_delta: -0.114 (-27%)\n    key_finding: 'V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x\n      to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1).\n      But over-corrected at high counts: under-prediction (pred/gold<1) caused recall\n      drops of 27-39%, slightly lowering F1 at count_22-64.'\n- exp_id: exp-004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_event_types: 168\n    n_pairs: 14028\n    scs_mean: 0.2161\n    scs_std: 0.103\n    scs_max: 0.8368\n    scs_median: 0.2121\n    scs_q90: 0.3457\n    scs_q95: 0.3892\n    pairs_above_0.5: 119\n    pct_above_0.5: 0.85\n    train_docs: 2913\n    train_mentions: 77993\n    valid_docs: 710\n    valid_mentions: 18904\n- exp_id: exp004_maven_bcs\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    exp1_count_curve:\n      count_1:\n        n_batches: 64\n        exact_f1: 0.009\n        relaxed_f1: 0.106\n        bcs: 0\n      count_6:\n        n_batches: 5\n        exact_f1: 0.003\n        relaxed_f1: 0.103\n        bcs: 0.892\n      count_12:\n        n_batches: 5\n        exact_f1: 0.008\n        relaxed_f1: 0.146\n        bcs: 0.921\n      count_22:\n        n_batches: 5\n        exact_f1: 0.013\n        relaxed_f1: 0.185\n        bcs: 0.933\n      count_44:\n        n_batches: 5\n        exact_f1: 0.018\n        relaxed_f1: 0.247\n        bcs: 0.967\n      count_64:\n        n_batches: 5\n        exact_f1: 0.013\n        relaxed_f1: 0.245\n        bcs: 0.973\n    exp2_bcs_controlled:\n      count_6_high_bcs:\n        exact_f1: 0.0354\n        relaxed_f1: 0.211\n        bcs: 0.9447\n      count_6_low_bcs:\n        exact_f1: 0.0068\n        relaxed_f1: 0.089\n        bcs: 0.8709\n      count_12_high_bcs:\n        exact_f1: 0.0151\n        relaxed_f1: 0.1568\n        bcs: 0.9447\n      count_12_low_bcs:\n        exact_f1: 0.0068\n        relaxed_f1: 0.105\n        bcs: 0.9148\n    key_finding: 'MAVEN batch-level: high_bcs relaxed_F1 2.4x vs low_bcs (count_6).\n      Direction same as Few-NERD batch-level (positive). Pairwise + per-type analysis\n      needed to control frequency confound.'\n    note: exact_F1 very low (0.003-0.035), relaxed_F1 usable (0.089-0.247). Event\n      trigger boundary matching is fuzzy. A re-run (500 samples) is still in progress\n      in artifacts/exp004/.\n- exp_id: fewrel_pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    embedding: all-MiniLM-L6-v2\n    n_batches: 15\n    n_predictions: 374\n    count_4:\n      low_bcs_acc: 0.917\n      high_bcs_acc: 0.708\n      delta_pp: -20.9\n      low_bcs: 0.42\n      high_bcs: 0.97\n    count_8:\n      low_bcs_acc: 1\n      high_bcs_acc: 0.5\n      delta_pp: -50\n      low_bcs: 0.47\n      high_bcs: 0.97\n    count_16:\n      low_bcs_acc: 0.917\n      high_bcs_acc: 0.431\n      delta_pp: -48.6\n      low_bcs: 0.57\n      high_bcs: 0.97\n    key_finding: 'BCS-accuracy strong negative: high-BCS batches 43-71% vs low-BCS\n      92-100%. Effect increases with count. Cross-task (NER→RE) replication of confusability\n      hypothesis.'\n- exp_id: exp008_sdgd_zero_fewnerd\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp008_sdgd_zero_fewnerd_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 77.3\n    sdgd_zero:\n      f1: 0.2514\n      precision: 0.2096\n      recall: 0.3141\n      batches: 8\n      time_s: 408.7\n    random_batch:\n      f1: 0.3197\n      precision: 0.2491\n      recall: 0.4462\n      batches: 8\n      time_s: 476.1\n    per_type:\n      f1: 0.2915\n      precision: 0.194\n      recall: 0.5856\n      batches: 66\n      time_s: 2532.2\n    key_finding: All decomposition modes F1 < single_pass. Decomposition boosts recall\n      but kills precision (merge amplification). sdgd_zero worst F1, even below random_batch.\n- exp_id: exp_fewrel_formal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: 16-rel sanity check only\n    exp1:\n      count_1:\n        mean_acc: 0.904\n        n_batches: 16\n      count_4:\n        mean_acc: 0.932\n        n_batches: 5\n      count_8:\n        mean_acc: 0.867\n        n_batches: 5\n      count_16:\n        mean_acc: 0.778\n        n_batches: 5\n        bcs: 0.9\n        zero_variance: true\n    exp2:\n      count_8_low_bcs:\n        acc: 0.889\n        bcs: 0.782\n      count_8_high_bcs:\n        acc: 0.798\n        bcs: 0.892\n      delta_bcs_effect: -0.091\n    trend: 'count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8%\n      (Δ=-9.1pp)'\n- exp_id: exp_fewrel_formal_80rel\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_count_curve:\n      count_1:\n        acc: 0.8573\n        n_batches: 80\n        bcs: 0\n      count_4:\n        acc: 0.8667\n        n_batches: 5\n        bcs: 0.6335\n      count_8:\n        acc: 0.8021\n        n_batches: 5\n        bcs: 0.7175\n      count_16:\n        acc: 0.6958\n        n_batches: 5\n        bcs: 0.795\n      count_32:\n        acc: 0.6578\n        n_batches: 5\n        bcs: 0.8893\n      count_64:\n        acc: 0.5424\n        n_batches: 5\n        bcs: 0.9434\n      count_80:\n        acc: 0.5042\n        n_batches: 5\n        bcs: 0.9706\n    exp2_bcs_controlled:\n      count_8:\n        low_bcs_acc: 0.8229\n        low_bcs: 0.4715\n        high_bcs_acc: 0.5104\n        high_bcs: 0.9706\n        random_acc: 0.8025\n        delta_pp: -31.2\n      count_16:\n        low_bcs_acc: 0.8281\n        low_bcs: 0.5705\n        high_bcs_acc: 0.5156\n        high_bcs: 0.9706\n        random_acc: 0.7169\n        delta_pp: -31.2\n    vs_16rel:\n      degradation_16rel: -12.6pp (0.904→0.778)\n      degradation_80rel: -35.3pp (0.857→0.504)\n      bcs_effect_16rel: -9.1pp\n      bcs_effect_80rel: -31.2pp\n      amplification: 3.4x\n    key_finding: 80-rel count curve 0.857→0.504 (degradation 35.3pp, 远强于 16-rel 12.6pp).\n      BCS effect -31.2pp (3.4x amplification vs 16-rel). 更多 relations → 更大 confusion\n      space → 更强 degradation + BCS effect.\n- exp_id: exp008_sdgd_v2_fewnerd\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 79\n    random_batch:\n      f1: 0.3007\n      precision: 0.3307\n      recall: 0.2758\n      batches: 8\n      time_s: 494\n    sdgd_zero:\n      f1: 0.2407\n      precision: 0.3244\n      recall: 0.1913\n      batches: 4\n      time_s: 261\n    per_type: killed before completion (3/4 modes done, Director approved kill)\n    vs_v1: confidence-gated merge did not improve over union merge. sdgd_zero 0.241\n      vs v1 0.251, random_batch 0.301 vs v1 0.320\n    key_finding: SDGD v2 confidence-gated merge + min_batch_size=8 failed to beat\n      single_pass baseline (F1=0.445). Both v1 and v2 confirm decomposition hurts\n      precision more than it helps recall. Claim 3 (SDGD framework) needs fundamental\n      rethink.\n- exp_id: exp012_llama_fewnerd\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp007_error_taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_random:\n      bcs_zero:\n        n_fp: 6172\n        intra_sub_pct: 0\n        extra_sub_pct: 90.3\n        intra_sub_per_100_gold: 0\n      bcs_low:\n        n_fp: 2231\n        intra_sub_pct: 1.6\n        extra_sub_pct: 89.9\n        intra_sub_per_100_gold: 3.4\n      bcs_medium:\n        n_fp: 3843\n        intra_sub_pct: 10.6\n        extra_sub_pct: 78.1\n        intra_sub_per_100_gold: 6.47\n      bcs_high:\n        n_fp: 6188\n        intra_sub_pct: 49.4\n        extra_sub_pct: 30.8\n        intra_sub_per_100_gold: 12.93\n    correlation:\n      intra_sub_vs_bcs_spearman_rho: 1\n      intra_sub_vs_bcs_p: <0.001\n      chi_square: 6952\n      chi_square_p: ~0\n    exp2_controlled:\n      trend: IntraSub 3.2% -> 7.3% -> 8.6% (rho=1.0, p<0.001)\n    key_finding: 'BCS>=0.95: 49.4% FP are intra-batch type confusion (13/100 gold).\n      Hallucination+boundary <3%. LLM main error mode is type confusion, not hallucination.'\n- exp_id: exp012_llama_fewnerd_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp016_fewrel_error_taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    error_distribution:\n      zero_bcs:\n        bcs_mean: 0\n        correct_pct: 85.73\n        wrong_type_pct: 0\n        intra_sub_pct: 0\n        missed_pct: 14.27\n      low_bcs:\n        bcs_mean: 0.565\n        correct_pct: 85.42\n        wrong_type_pct: 4.17\n        intra_sub_pct: 4.17\n        missed_pct: 10.42\n      medium_bcs:\n        bcs_mean: 0.729\n        correct_pct: 75.7\n        wrong_type_pct: 13\n        intra_sub_pct: 13\n        missed_pct: 11.3\n      high_bcs:\n        bcs_mean: 0.86\n        correct_pct: 66.67\n        wrong_type_pct: 20.28\n        intra_sub_pct: 20.28\n        missed_pct: 13.05\n      very_high_bcs:\n        bcs_mean: 0.971\n        correct_pct: 52.03\n        wrong_type_pct: 32.25\n        intra_sub_pct: 32.25\n        missed_pct: 15.71\n    correlations:\n      intra_sub_vs_bcs_spearman: 0.9539\n      intra_sub_vs_bcs_p: <1e-6\n      accuracy_vs_bcs_spearman: -0.5821\n      accuracy_vs_bcs_p: <1e-6\n    cross_task:\n      ner_intra_sub_vs_bcs_rho: 1\n      re_intra_sub_vs_bcs_rho: 0.9539\n    key_finding: 100% of type confusion in RE is intra-batch (model only predicts\n      from schema). IntraSub vs BCS ρ=0.954 confirms NER finding. Missed rate flat\n      (10-16%), BCS drives confusion not detection failure.\n- exp_id: bootstrap_ci_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fewnerd_pairwise_r:\n      point: 0.112\n      ci_lower: 0.076\n      ci_upper: 0.156\n      n: 1953\n      note: point estimate 0.112 vs old 0.156 — re-run confirmed current value\n    maven_minilm_pairwise_r:\n      point: 0.129\n      ci_lower: 0.104\n      ci_upper: 0.156\n      n: 11026\n    fewrel_count8_delta_pp:\n      point: 31.2\n      ci_lower: 17.7\n      ci_upper: 42.7\n      n: 96+96\n    fewrel_count16_delta_pp:\n      point: 31.2\n      ci_lower: 22.9\n      ci_upper: 39.6\n      n: 192+192\n    fewnerd_pertype_rho:\n      point: -0.293\n      ci_lower: -0.492\n      ci_upper: -0.054\n      n: 63\n    confusion_ratio_count6:\n      point: 25.3\n      ci_lower: 6.1\n      ci_upper: 60.5\n    confusion_ratio_count12:\n      point: 21.2\n      ci_lower: 5.3\n      ci_upper: 52.2\n    key_finding: All CIs exclude null (0 for correlations, 1 for ratios). All effects\n      are directionally robust at 95% level.\n- exp_id: exp015_scs_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    all_pairs:\n      n: 1953\n      n_nonzero: 216\n      qwen3_spearman: 0.1682\n      qwen3_spearman_p: '7.3e-14'\n      qwen3_kendall: 0.1351\n      minilm_spearman: 0.1439\n      minilm_spearman_p: '1.7e-10'\n      minilm_kendall: 0.1152\n    nonzero_only:\n      n: 216\n      qwen3_spearman: 0.2722\n      qwen3_spearman_p: '5.0e-05'\n      qwen3_kendall: 0.2001\n      minilm_spearman: 0.306\n      minilm_spearman_p: '4.6e-06'\n      minilm_kendall: 0.2276\n    key_finding: Both embeddings significantly predict confusion (all p<1e-5). Qwen3\n      better overall (rho=0.168), MiniLM better on nonzero pairs (rho=0.306). SCS\n      is a valid but partial proxy — context, frequency, mention ambiguity also matter.\n- exp_id: exp012_llama_fewnerd_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_8b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_fewrel_40rel\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_awq\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp012_llama_fewnerd_r4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_8b_fewnerd\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_fewrel_40rel_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_fewrel_40rel_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_8b_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_llama_recall_count1: 0.702\n    exp1_llama_recall_count64: 0.273\n    exp1_recall_decline_pp: -42.9\n    exp1_per_batch_recall_corr_vs_qwen: 0.7249\n    exp1_llama_text_match_f1_range: 0.06-0.36\n    exp1_exact_f1: 0\n    exp1_note: exact/relaxed F1=0 due to missing char offsets, text_match is correct\n      metric\n- exp_id: exp012_llama_8b_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006_interaction_2x2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    cell_means_f1:\n      low_count_low_bcs: 0.324\n      low_count_high_bcs: 0.313\n      high_count_low_bcs: 0.325\n      high_count_high_bcs: 0.277\n    main_effects:\n      count: -0.018\n      bcs: -0.029\n    interaction:\n      estimate: -0.036\n      z: -0.667\n      p: 0.505\n      bcs_effect_at_low_count: -0.011\n      bcs_effect_at_high_count: -0.048\n    verdict: 交互方向符合 multiplicative 假设但统计不显著 (p=0.505)，未检测到显著交互效应\n- exp_id: exp012_llama_8b_r2_exp2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_fewrel_40rel_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_acc_count1: 0.858\n    exp1_acc_count4: 0.867\n    exp1_acc_count8: 0.802\n    exp1_acc_count16: 0.697\n    exp1_acc_count32: 0.658\n    exp1_acc_count40: 0.588\n    exp1_decline_pp: -27\n    exp2_bcs_delta_count8: 0.333\n    exp2_bcs_delta_count16: 0.318\n    exp2_low_bcs_acc_count8: 0.833\n    exp2_high_bcs_acc_count8: 0.5\n    exp2_low_bcs_acc_count16: 0.818\n    exp2_high_bcs_acc_count16: 0.5\n- exp_id: exp012_llama_fewrel_ch2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp2_bcs_controlled:\n      count_8:\n        low_bcs_acc: 0.7812\n        high_bcs_acc: 0.5104\n        delta_pp: -27.1\n      count_16:\n        low_bcs_acc: 0.7552\n        high_bcs_acc: 0.5156\n        delta_pp: -24\n    overall_correlation:\n      n_batches: 54\n      pearson_r: -0.39\n      pearson_p: 0.004\n      spearman_rho: -0.43\n      spearman_p: 0.001\n    cross_model_comparison:\n      llama_delta_pp: -27.1\n      qwen3_delta_pp: -31.2\n      ratio: 0.87\n      note: LLaMA effect = 87% of Qwen3, direction and magnitude consistent\n    no_floor_effect: true\n    mean_accuracy: 0.77\n    accuracy_range: 0.41-0.98\n    key_finding: 'BCS confusability effect cross-model replicated: LLaMA Δ=-27.1pp\n      (87% of Qwen3 -31.2pp). Pearson r=-0.39 (p=0.004), Spearman ρ=-0.43 (p=0.001).\n      No floor effect.'\n- exp_id: exp_fewrel_16rel_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_batches: 100\n    pool_size: 16\n    batch_size: 8\n    bcs_range:\n    - 0.6532\n    - 0.9002\n    quartile_delta:\n      Q4_minus_Q1_pp: -5.31\n      ci_95_lower: -9.45\n      ci_95_upper: -4.49\n      note: CI values from pre-D038 bootstrap, may need re-verification with MEAN-based\n        BCS\n    pearson_r_bcs_acc: -0.467\n    regression_slope:\n      slope: -0.509\n      ci_95_lower: -0.556\n      ci_95_upper: -0.349\n      r_squared: 0.218\n      p_value: 1.01e-12\n      interpretation: per +0.1 BCS → -5.09pp accuracy\n      note: CI from pre-D038 bootstrap\n    amplification_ratio:\n      quartile_16_vs_80: 4.2\n      ci_95_lower: 3.3\n      ci_95_upper: 6.95\n    key_finding: '16-rel pool BCS effect (MEAN-based, D038): Δ(Q4-Q1)=-5.31pp, r=-0.467.\n      Regression slope=-0.509. Bootstrap 1000 resamples. [D038 MEAN correction applied,\n      old values: r=-0.637/Δ=-7.42pp/slope=-0.449]'\n- exp_id: exp_fewrel_16rel_100batch\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_fewrel_80pool_16sub_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_batches: 100\n    pool_size: 80-rel pool, 16-type subsamples\n    batch_size: 8\n    mean_accuracy: 0.8077\n    mean_bcs: 0.557\n    bcs_range:\n    - 0.4578\n    - 0.6836\n    quartile_delta:\n      Q4_minus_Q1_pp: -3.92\n      ci_95_lower: -7.79\n      ci_95_upper: 0.42\n    pearson_r_bcs_acc: -0.221\n    pearson_p: 0.027\n    regression_slope:\n      slope: -0.401\n      ci_95_lower: -0.684\n      ci_95_upper: -0.062\n      interpretation: per +0.1 BCS → -4.01pp accuracy\n    key_finding: '80-pool 16-sub BCS effect directional: Δ(Q4-Q1)=-3.92pp CI crosses\n      zero [-7.79,+0.42], but regression slope=-0.401 CI[-0.684,-0.062] excludes zero.\n      Effect weaker than independent 16-rel pool (Δ=-7.42pp) due to narrower BCS range.'\n- exp_id: exp_maven_residualized_bcs\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    minilm:\n      raw_rho: 0.208\n      raw_p: 0.011\n      confound: log_freq\n      bcs_confound_r: 0.201\n      partial_r: 0.133\n      partial_p: 0.107\n    qwen3:\n      raw_rho: 0.184\n      raw_p: 0.025\n      confound: degree_centrality_0.7\n      bcs_confound_r: 0.854\n      partial_r: 0.063\n      partial_p: 0.442\n    joint_control:\n      qwen3_p: 0.439\n      minilm_p: 0.226\n      note: Both n.s. after controlling log_freq + degree jointly\n    key_finding: MAVEN BCS-F1 positive correlation is centrality artifact. MiniLM\n      confound=frequency, Qwen3 confound=degree centrality (r=0.854). After joint\n      control, both correlations vanish. Confirms pairwise SCS remains valid but per-type\n      aggregation fails on homogeneous schemas.\n- exp_id: exp_fewrel_v2_bcs_controlled\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_bcs_mean_acc: 0.8042\n    high_bcs_mean_acc: 0.725\n    delta_low_minus_high_pp: 7.92\n    bootstrap_ci_95_lower_pp: -5.21\n    bootstrap_ci_95_upper_pp: 21.46\n    n_bootstrap: 10000\n    n_batches_per_group: 5\n    samples_per_batch: 96\n    total_inferences: 960\n- exp_id: exp_docred_confusability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_relation_types: 96\n    n_eval_samples: 1240\n    total_inferences: 13618\n    count_curve:\n      count_1: 0.88\n      count_4: 0.77\n      count_8: 0.774\n      count_16: 0.524\n      count_32: 0.521\n      count_64: 0.424\n      count_96: 0.387\n    bcs_effect_count16:\n      low_bcs_acc: 0.679\n      high_bcs_acc: 0.447\n      gap: 0.233\n      spearman_r: -0.661\n      slope: -0.713\n      slope_95ci:\n      - -0.909\n      - -0.529\n    bcs_effect_count32:\n      low_bcs_acc: 0.578\n      high_bcs_acc: 0.403\n      gap: 0.176\n      spearman_r: -0.509\n      slope: -0.69\n      slope_95ci:\n      - -0.854\n      - -0.519\n- exp_id: bcs_max_to_mean_fix\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: exp_confusability_batch_composition\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_fewrel_v2_n25\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    n_low: 25\n    n_high: 25\n    low_bcs_mean_acc: 0.8521\n    high_bcs_mean_acc: 0.5967\n    delta_pp: 25.54\n    ci_95:\n    - 22.42\n    - 28.62\n    permutation_p: 0\n    pearson_r: -0.919\n    low_bcs_range:\n    - 0.356\n    - 0.367\n    high_bcs_range:\n    - 0.791\n    - 0.811\n    key_finding: v2 prompt does NOT eliminate confusability effect. At n=25 with wider\n      BCS separation, effect is massive (25.5pp) and highly significant. Prior n=5\n      result (7.9pp, CI crosses zero) was underpowered + narrow BCS contrast.\n- exp_id: exp_cross_embedding_sensitivity\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    fewnerd_qwen3:\n      pearson_r: 0.138\n      pearson_p: 1.0e-09\n      spearman_rho: 0.168\n      spearman_p: 7.3e-14\n    fewnerd_minilm:\n      pearson_r: 0.172\n      pearson_p: 2.0e-14\n      spearman_rho: 0.144\n      spearman_p: 1.7e-10\n    fewrel_minilm:\n      slope: -0.485\n      r: -0.398\n      p: 0.04\n    fewrel_qwen3:\n      slope: -0.542\n      r: -0.185\n      p: 0.356\n      note: BCS range compression (std=0.034 vs MiniLM 0.081), directional but n.s.\n    key_finding: SCS-confusion signal robust to embedding choice (both significant\n      on Few-NERD). MiniLM better for BCS due to designed-for-similarity. Qwen3 causal-LM\n      embeddings compress BCS range.\n- exp_id: exp017_gpt4o_mini_fewrel\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T07:38:43.217Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T07:38:43.217Z",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244"
}
```

---

## Round 1

18 recorded events

### User

_source line 3 · 2026-05-16T07:38:43.247Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：两条 claim 均以当前数据充分支撑，SDGD 负面结果被视为方法论贡献，论文被 EMNLP Main 接收
核心假设：['A1: Pairwise SCS→confusion 的 r=0.11-0.13 被接受为有意义的效应量（reviewers 认可 noise floor 高的 IE 任务中此量级合理）', 'A2: 多通道退化模型（count→recall, confusability→type confusion）的正交性被 error taxonomy ρ≥0.95 充分证明', 'A3: FewRel 80-rel 的 3.4× amplification 被视为 schema complexity scaling 的强证据', 'A4: LLaMA FewRel 复现（Δ=-27.1pp, 87% of Qwen3）被接受为充分的 multi-model 验证', 'A5: MAVEN per-type centrality confound 被视为方法论贡献（何时聚合度量失效）而非负面证据', 'A6: SDGD 负面结果 + merge amplification 分析被视为诚实贡献（类比 negative results track）', 'A7: 纯实证研究格式被 EMNLP 接受（类比 Lost in the Middle, TACL 2024）']
关键指标范围：{'arr_avg_score': [3.5, 4.0], 'claims_fully_supported': [2, 2], 'major_reviewer_weaknesses': [0, 1], 'cross_task_significant_replications': [3, 4], 'multi_model_effect_consistency': [0.85, 1.0], 'venue_probability_main': [0.55, 0.75], 'venue_probability_findings_or_above': [0.85, 0.95], 'rebuttal_flip_probability': [0.8, 1.0]}
叙事方向：原始 framing 完全成立。标题级 claim: "Pairwise type confusability independently predicts LLM IE degradation across three tasks and two models." 两条 claim 均以强证据支撑: Claim 1 靠 pairwise 相关性 + FewRel BCS-controlled gap + DocRED replication; Claim 2 靠 error taxonomy cross-task ρ≥0.95。SDGD 负面结果作为 Section 6 讨论， 指向 calibration-based 方向。MAVEN centrality confound 作为独立的方法论发现。 Embedding ablation 2×3 matrix 作为实践指南。不需要调整 claim 强度。


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
  "promptId": "e31cdcbc-6ab2-4d77-9b1c-a2e42d262137",
  "type": "user",
  "uuid": "c1d917b7-5884-44fe-89be-2e1b3a5135b3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T07:38:43.244Z_

```json
{
  "parentUuid": "c1d917b7-5884-44fe-89be-2e1b3a5135b3",
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
  "uuid": "b9e7a188-5622-4d2e-be98-8cd796d776a5",
  "timestamp": "2026-05-16T07:38:43.244Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T07:38:43.244Z_

```json
{
  "parentUuid": "b9e7a188-5622-4d2e-be98-8cd796d776a5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c81cb03e-28c9-4b4e-8d69-0f5a825d0705",
  "timestamp": "2026-05-16T07:38:43.244Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：两条 claim 均以当前数据充分支撑，SDGD 负面结果被视为方法论贡献，论文被 EMNLP Main 接收 核心假设：['A1: Pairwise SCS→confusion 的 r=0.11-0.13 被接受为有意义的效应量（reviewers 认可 noise floor 高的 IE 任务中此量级合理…",
  "leafUuid": "c81cb03e-28c9-4b4e-8d69-0f5a825d0705",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-task confusability effect sizes with multi-model validation",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244"
}
```

---

### Assistant

_source line 8 · 2026-05-16T07:39:23.209Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each "planned" experiment in the experiment_plan, under the "best" tier scenario. Let me identify which experiments are still "planned":

1. **exp-005** - DocRED confusability study (but wait, there's a registry entry `exp_docred_confusability` that's DONE with conclusion: success. So this might actually be done. Let me check - the experiment_plan shows status: planned, but the registry has it completed. I'll treat it based on the plan status.)

Actually, looking more carefully:
- exp-005: status: planned (DocRED)


- exp-006: status: planned (but registry shows `exp006_interaction_2x2` DONE, conclusion: negative)
- exp-007: status: planned (but registry shows `exp007_error_taxonomy` DONE, conclusion: success)
- exp-009: status: planned (SDGD-zero on MAVEN)
- exp-010: status: planned (SDGD-cal on Few-NERD)
- exp-011: status: planned (SDGD-cal on MAVEN)
- exp-013: status: planned (Random batching ablation)
- exp-014: status: planned (Per-type splitting ablation)
- exp-015: status: planned

So I have a discrepancy where some experiments marked as "planned" in the plan already have completed entries in the registry. I'll go with the plan status as the source of truth for what to generate predictions for. I see that several experiments marked as "planned" in the experiment_plan have already been completed and logged in the registry with actual results. Rather than predicting outcomes for experiments that are already done, I should use their actual results as the foundation and extrapolate predictions for the remaining planned experiments under the "best" tier scenario.

The "best" tier represents a successful outcome where both main claims are fully supported, the SDGD negative result is framed as a methodological contribution, the paper gets accepted at EMNLP Main, all key assumptions hold, and we achieve strong cross-task replication effects with high model consistency. For each planned experiment, I need to generate predicted data that aligns with this best-case scenario.

Looking at the experiments already in the registry, exp-005 on DocRED with 96 relation types shows the count curve degrading clearly from 0.88 to 0.387 as we scale up, with a 23.3 percentage point gap at count_16 and a strong negative correlation (r=-0.661) — these are exactly the best-tier results we'd want. For exp-006, the interaction test came back non-significant (p=0.505), which actually supports our framing of count and confusability as orthogonal channels rather than conflicting with it. And exp-007's error taxonomy analysis shows the expected monotonic increase in IntraSub errors as BCS grows, confirming the pattern we're looking for.

For the remaining experiments, I'm tracking that exp-009 through exp-011 are still planned but not yet in the registry. The SDGD experiments on both MAVEN and Few-NERD are expected to show negative results — single-pass should outperform SDGD-zero, and even with calibration on Few-NERD, we'd likely see only marginal gains that still fall short of the baseline. The key contribution here is documenting why these approaches fail rather than expecting them to succeed.

Looking at the ablation studies, exp-013 with random batching gives me concrete evidence from the registry that random grouping (F1=0.3007) sits between single-pass (0.4451) and SDGD-zero, which isolates that the confusability-aware grouping itself isn't the bottleneck — the merge operation is. The per-type splitting experiment should reveal the theoretical upper bound on what decomposition could achieve, showing high recall but still constrained by precision issues. And exp-015 on SCS validation has already been completed successfully.

Now I'm checking the SCS correlation results from the registry — both Qwen3 and MiniLM show statistically significant relationships between SCS and confusion patterns, which validates that the metric captures something meaningful about model behavior. I'm ready to compile the full YAML predictions for the best tier with these empirical findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c81cb03e-28c9-4b4e-8d69-0f5a825d0705",
  "isSidechain": false,
  "requestId": "req_011Cb5sEdY8w29wMgvHUcPg6",
  "type": "assistant",
  "uuid": "afc1157b-e5e0-4dbd-a125-fa612ef3616d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013uY9MTyizE2stwHbsM5nV5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26488,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1749,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1749,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26488
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

_source line 9 · 2026-05-16T07:39:23.214Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01DiQCLLw5sxB5EF5KfocudY`</summary>

```json
{
  "pattern": "**/*experiment_plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afc1157b-e5e0-4dbd-a125-fa612ef3616d",
  "isSidechain": false,
  "requestId": "req_011Cb5sEdY8w29wMgvHUcPg6",
  "type": "assistant",
  "uuid": "79554594-863c-4525-93f0-fdee43f40198",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013uY9MTyizE2stwHbsM5nV5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26488,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1749,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1749,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26488
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

_source line 10 · 2026-05-16T07:39:23.237Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Kh7bD3ckf75a2pcUdYL1En`</summary>

```json
{
  "pattern": "**/*registry*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79554594-863c-4525-93f0-fdee43f40198",
  "isSidechain": false,
  "requestId": "req_011Cb5sEdY8w29wMgvHUcPg6",
  "type": "assistant",
  "uuid": "f7f81860-e6e3-4814-b832-2133ec763d27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013uY9MTyizE2stwHbsM5nV5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26488,
      "cache_read_input_tokens": 11841,
      "output_tokens": 1749,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26488,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1749,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26488
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

_source line 11 · 2026-05-16T07:39:23.264Z_

<details><summary>↩ Tool result · `toolu_01DiQCLLw5sxB5EF5KfocudY`</summary>

```text
projects/collapse-aware-mixing/artifacts/experiment_plan.yaml
projects/schema-dag-extraction/experiment_plan.lock
projects/schema-dag-extraction/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79554594-863c-4525-93f0-fdee43f40198",
  "isSidechain": false,
  "promptId": "e31cdcbc-6ab2-4d77-9b1c-a2e42d262137",
  "type": "user",
  "uuid": "c83de4c0-e4e5-459d-8b5f-675206ee36d3",
  "toolUseResult": {
    "filenames": [
      "projects/collapse-aware-mixing/artifacts/experiment_plan.yaml",
      "projects/schema-dag-extraction/experiment_plan.lock",
      "projects/schema-dag-extraction/experiment_plan.yaml"
    ],
    "durationMs": 41,
    "numFiles": 3,
    "truncated": false
  },
  "sourceToolAssistantUUID": "79554594-863c-4525-93f0-fdee43f40198",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T07:39:23.271Z_

<details><summary>↩ Tool result · `toolu_01Kh7bD3ckf75a2pcUdYL1En`</summary>

```text
global/logs/workers/registry.lock
projects/collapse-aware-mixing/registry.lock
projects/collapse-aware-mixing/dream_registry.lock
projects/schema-dag-extraction/registry.lock
projects/schema-dag-extraction/dream_registry.lock
projects/collapse-aware-mixing/registry.yaml
global/registry.lock
global/registry.yaml
projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/backends/registry.py
projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/tests/test_backend_registry.py
projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/backends/__pycache__/registry.cpython-314.pyc
projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/tests/__pycache__/test_backend_registry.cpython-314.pyc
projects/schema-dag-extraction/dream_registry.yaml.bak
projects/schema-dag-extraction/dream_registry.yaml
global/logs/workers/registry.json.bak
global/logs/workers/registry.json
projects/schema-dag-extraction/registry.yaml
global/logs/registry_audit.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7f81860-e6e3-4814-b832-2133ec763d27",
  "isSidechain": false,
  "promptId": "e31cdcbc-6ab2-4d77-9b1c-a2e42d262137",
  "type": "user",
  "uuid": "fd3c77bb-3e22-4190-8fc7-1c36e853c3df",
  "toolUseResult": {
    "filenames": [
      "global/logs/workers/registry.lock",
      "projects/collapse-aware-mixing/registry.lock",
      "projects/collapse-aware-mixing/dream_registry.lock",
      "projects/schema-dag-extraction/registry.lock",
      "projects/schema-dag-extraction/dream_registry.lock",
      "projects/collapse-aware-mixing/registry.yaml",
      "global/registry.lock",
      "global/registry.yaml",
      "projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/backends/registry.py",
      "projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/tests/test_backend_registry.py",
      "projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/backends/__pycache__/registry.cpython-314.pyc",
      "projects/schema-dag-extraction/.venv/lib/python3.14/site-packages/matplotlib/tests/__pycache__/test_backend_registry.cpython-314.pyc",
      "projects/schema-dag-extraction/dream_registry.yaml.bak",
      "projects/schema-dag-extraction/dream_registry.yaml",
      "global/logs/workers/registry.json.bak",
      "global/logs/workers/registry.json",
      "projects/schema-dag-extraction/registry.yaml",
      "global/logs/registry_audit.jsonl"
    ],
    "durationMs": 29,
    "numFiles": 18,
    "truncated": false
  },
  "sourceToolAssistantUUID": "f7f81860-e6e3-4814-b832-2133ec763d27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T07:39:28.151Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tgp9CuFayXigEJqdZYEBho`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml",
  "offset": 0,
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd3c77bb-3e22-4190-8fc7-1c36e853c3df",
  "isSidechain": false,
  "requestId": "req_011Cb5sHamXjmTSPMW3BSH9B",
  "type": "assistant",
  "uuid": "bbb96d65-6c3d-47d0-ade8-3ab48ea84f61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MjTtc3FRsTppuH2SGzNCK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2163,
      "cache_read_input_tokens": 38329,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2163,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 38329,
          "cache_creation_input_tokens": 2163,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2163
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

_source line 14 · 2026-05-16T07:39:28.178Z_

<details><summary>↩ Tool result · `toolu_01Tgp9CuFayXigEJqdZYEBho`</summary>

```text
0	experiments:
1	- id: exp-001
2	  claim:
3	  - 1
4	  - 2
5	  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]
6	    on Few-NERD with Qwen3-32B-FP8'
7	  priority: P0
8	  gpu_budget_hours: 3.5
9	  deps: []
10	  registry_id: exp001_count_baseline
11	  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction
12	    at low counts.
13	- id: exp-002
14	  claim:
15	  - 1
16	  - 2
17	  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,
18	    25 random + extreme batches on Few-NERD'
19	  priority: P0
20	  gpu_budget_hours: 3
21	  deps:
22	  - exp-001
23	  registry_id: exp002_confusability_controlled
24	  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion
25	    rate 10-28x.
26	- id: exp-003a
27	  claim:
28	  - 1
29	  - 2
30	  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination
31	    instruction. Re-run exp1+exp2.'
32	  priority: P0
33	  gpu_budget_hours: 3
34	  deps:
35	  - exp-001
36	  - exp-002
37	  registry_id: exp003a_prompt_v2_rerun
38	  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.
39	- id: exp-004
40	  claim:
41	  - 1
42	  - 2
43	  - 3
44	  description: 'MAVEN confusability study: count curve + within-count BCS correlation
45	    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core
46	    finding cross-task (NER→ED) with larger type space and known sibling confusion
47	    (14.6-19.8%).'
48	  priority: P0
49	  gpu_budget_hours: 4
50	  deps:
51	  - exp-003a
52	  registry_id: exp-004
53	  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs
54	    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy
55	    structure.'
56	- id: exp-005
57	  claim:
58	  - 1
59	  - 2
60	  description: 'DocRED confusability study: count curve + BCS correlation on DocRED
61	    (96 relation types). Scaling stress test.'
62	  priority: P1
63	  gpu_budget_hours: 5
64	  deps:
65	  - exp-003a
66	- id: exp-006
67	  claim:
68	  - 2
69	  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}
70	    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'
71	  priority: P1
72	  gpu_budget_hours: 2
73	  deps:
74	  - exp-003a
75	- id: exp-007
76	  claim:
77	  - 2
78	  description: 'Error taxonomy: systematic FP classification (type_substitution /
79	    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic
80	    evidence for multi-channel model.'
81	  priority: P1
82	  gpu_budget_hours: 1
83	  deps:
84	  - exp-002
85	  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic
86	    BCS-binned analysis.
87	- id: exp-012
88	  claim:
89	  - 1
90	  - 2
91	  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional
92	    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model
93	    generalizability.'
94	  priority: P0
95	  gpu_budget_hours: 6
96	  deps:
97	  - exp-003a
98	  registry_id: exp012_llama_8b_r3
99	- id: exp-016
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbb96d65-6c3d-47d0-ade8-3ab48ea84f61",
  "isSidechain": false,
  "promptId": "e31cdcbc-6ab2-4d77-9b1c-a2e42d262137",
  "type": "user",
  "uuid": "5efc7cc7-e4a0-42ba-861f-b5481564e186",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/experiment_plan.yaml",
      "content": "experiments:\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]\n    on Few-NERD with Qwen3-32B-FP8'\n  priority: P0\n  gpu_budget_hours: 3.5\n  deps: []\n  registry_id: exp001_count_baseline\n  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction\n    at low counts.\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,\n    25 random + extreme batches on Few-NERD'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  registry_id: exp002_confusability_controlled\n  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion\n    rate 10-28x.\n- id: exp-003a\n  claim:\n  - 1\n  - 2\n  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination\n    instruction. Re-run exp1+exp2.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp003a_prompt_v2_rerun\n  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MAVEN confusability study: count curve + within-count BCS correlation\n    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core\n    finding cross-task (NER→ED) with larger type space and known sibling confusion\n    (14.6-19.8%).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp-004\n  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs\n    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy\n    structure.'\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional\n    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model\n    generalizability.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-003a\n  registry_id: exp012_llama_8b_r3\n- id: exp-016",
      "numLines": 100,
      "startLine": 0,
      "totalLines": 183
    }
  },
  "sourceToolAssistantUUID": "bbb96d65-6c3d-47d0-ade8-3ab48ea84f61",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15 · 2026-05-16T07:39:28.299Z_

````json
{
  "parentUuid": "5efc7cc7-e4a0-42ba-861f-b5481564e186",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**schema-dag-extraction**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"schema-dag-extraction\")` 或 `load_project_config(\"schema-dag-extraction\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/schema-dag-extraction/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "5156ba7d-a881-49c5-889f-f0bc407d95e5",
  "timestamp": "2026-05-16T07:39:28.299Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：两条 claim 均以当前数据充分支撑，SDGD 负面结果被视为方法论贡献，论文被 EMNLP Main 接收 核心假设：['A1: Pairwise SCS→confusion 的 r=0.11-0.13 被接受为有意义的效应量（reviewers 认可 noise floor 高的 IE 任务中此量级合理…",
  "leafUuid": "5156ba7d-a881-49c5-889f-f0bc407d95e5",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-task confusability effect sizes with multi-model validation",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244"
}
```

---

### Assistant

_source line 18 · 2026-05-16T07:43:07.484Z_

I have all the context needed. Let me produce the detailed best-tier predictions for each planned experiment.

```yaml
tier: best
narrative_guidance: >
  在 best 档下，两条 claim 均以充分证据支撑。Claim 1 (Confusability Independence) 靠 pairwise SCS→confusion 的跨任务 r=0.11-0.13 + FewRel BCS-controlled Δ=-31.2pp + DocRED replication + LLaMA 87% consistency。Claim 2 (Multi-Channel Degradation) 靠 error taxonomy IntraSub ρ≥0.95 + 2x2 additive framing + count→recall / confusability→type confusion 分离。SDGD 负面结果被视为 honest contribution（merge amplification 是结构性挑战），MAVEN centrality confound 被视为方法论贡献。论文以纯实证研究格式投 EMNLP Main，reviewer 认可 noise floor 高的 IE 任务中 r=0.11-0.13 为有意义效应量。

imagined_experiments:
  - name: "DocRED Confusability Study"
    plan_id: "exp-005"
    description: "DocRED 96 relation types 的 count curve + BCS correlation，作为 Claim 1 的第三个 RE 数据集 replication"
    expected_results:
      count_curve_acc_count1: 0.875
      count_curve_acc_count4: 0.782
      count_curve_acc_count8: 0.768
      count_curve_acc_count16: 0.531
      count_curve_acc_count32: 0.515
      count_curve_acc_count64: 0.428
      count_curve_acc_count96: 0.392
      bcs_effect_count16_low_acc: 0.685
      bcs_effect_count16_high_acc: 0.452
      bcs_effect_count16_gap_pp: 23.3
      bcs_effect_count16_spearman_r: -0.661
      bcs_effect_count16_slope: -0.713
      bcs_effect_count16_slope_ci: [-0.909, -0.529]
      bcs_effect_count32_low_acc: 0.581
      bcs_effect_count32_high_acc: 0.406
      bcs_effect_count32_gap_pp: 17.5
      bcs_effect_count32_spearman_r: -0.509
      total_inferences: 13618
    result_rationale: >
      DocRED 有 96 relation types，复杂度介于 FewRel-80 和 MAVEN-168 之间。在 best 档下，
      count curve 展现从 0.88 到 0.39 的 49pp 下降（强于 FewRel-16 的 12.6pp，略弱于 FewRel-80 的 35.3pp，
      因为 DocRED relations 语义分布更均匀，部分 relation 有明确文档上下文辅助消歧）。
      BCS effect 在 count_16 达 23.3pp gap，slope CI 排除零——这是因为 DocRED 的 document-level RE
      有更长上下文可消歧部分 confusion，但 schema 的 96 types 中存在大量语义相邻 relation（如 country/nationality,
      employer/member_of），使 BCS 信号显著。Spearman r=-0.661 强于 FewRel 的 batch-level correlation，
      因为 DocRED evaluation 天然 per-relation 且文档内 relation density 更高，给 BCS 更多 variance 可解释。
      这为 Claim 1 提供第四个数据集的 cross-task replication。
    tables:
      - name: "DocRED Count Curve"
        columns: ["count", "accuracy", "n_batches", "mean_bcs"]
        rows:
          - [1, 0.875, 96, 0.0]
          - [4, 0.782, 5, 0.61]
          - [8, 0.768, 5, 0.72]
          - [16, 0.531, 5, 0.79]
          - [32, 0.515, 5, 0.88]
          - [64, 0.428, 5, 0.94]
          - [96, 0.392, 5, 0.97]
      - name: "DocRED BCS-Controlled Accuracy"
        columns: ["count", "low_bcs_acc", "high_bcs_acc", "delta_pp", "spearman_r", "p"]
        rows:
          - [16, 0.685, 0.452, -23.3, -0.661, "<0.001"]
          - [32, 0.581, 0.406, -17.5, -0.509, 0.003]
    figures_description:
      - "DocRED count curve plot (acc vs type count) with 95% CI bands，同 FewRel 对比"
      - "BCS-accuracy scatter plot at count_16 with regression line and slope CI"
    analysis: >
      DocRED 复制了 FewRel 的核心发现：(1) count↑ → accuracy↓ 单调下降，(2) 控制 count 后 BCS 独立预测
      degradation (slope=-0.713, CI 排除零)。与 FewRel-80 对比，DocRED BCS effect 在 count_16 为 23.3pp vs
      FewRel 31.2pp——差异来自 DocRED 文档级上下文提供更多 disambiguation cue。但方向和显著性完全一致，
      构成第三个 RE 数据集的 cross-task validation。此实验巩固 Claim 1 的 "independently predicts" 论述。

  - name: "Interaction Effect 2x2"
    plan_id: "exp-006"
    description: "Few-NERD 上 {low count, high count} × {low BCS, high BCS} 的 2×2 factorial，检验 count 和 confusability 的 additive vs multiplicative 交互"
    expected_results:
      cell_f1_low_count_low_bcs: 0.324
      cell_f1_low_count_high_bcs: 0.313
      cell_f1_high_count_low_bcs: 0.325
      cell_f1_high_count_high_bcs: 0.277
      main_effect_count: -0.018
      main_effect_bcs: -0.029
      interaction_estimate: -0.036
      interaction_z: -0.667
      interaction_p: 0.505
      bcs_effect_at_low_count: -0.011
      bcs_effect_at_high_count: -0.048
    result_rationale: >
      在 best 档下，交互效应方向符合 multiplicative 假设（高 count + 高 BCS 组合下降最多），
      但统计上不显著 (p=0.505)。这实际上 SUPPORTS Claim 2 的 "orthogonal channels" framing——
      如果 count 和 confusability 真的通过独立通道（recall vs type confusion）影响 degradation，
      那么两者的总效应是 additive 而非 multiplicative。p=0.505 表明没有证据支持 super-additive interaction，
      与 orthogonality 假设一致。BCS effect at high count (-0.048) 略大于 at low count (-0.011)，
      但差异不显著——这与 FewRel 的 scaling 发现方向一致（更多 types → 更大 confusability space），
      但 Few-NERD 的 count 对比范围（6 vs 12）不够大，无法检测到显著交互。
      Reviewer 可能追问为何无交互，rebuttal 回应：orthogonal channels 预测的就是 additive 而非 multiplicative。
    tables:
      - name: "2x2 Factorial Results"
        columns: ["", "Low BCS", "High BCS", "BCS Effect"]
        rows:
          - ["Low Count (6)", 0.324, 0.313, -0.011]
          - ["High Count (12)", 0.325, 0.277, -0.048]
          - ["Count Effect", +0.001, -0.036, ""]
    figures_description:
      - "Interaction plot: 两条线 (low/high count) across BCS levels，近乎平行但 high-count 线略陡"
    analysis: >
      非显著交互 (p=0.505) 支撑 orthogonal channels 假设。Count 和 confusability 通过不同 error mode
      independently 影响 extraction quality——count 通过 recall drop（attention dilution），
      confusability 通过 type confusion（semantic interference）。两者是 additive 而非 synergistic。
      这一发现与 error taxonomy (exp-007) 中 IntraSub 仅与 BCS 相关、recall 仅与 count 相关的 pattern 一致。

  - name: "Error Taxonomy Systematic Analysis"
    plan_id: "exp-007"
    description: "跨 BCS bins 的系统化 FP 分类 (intra_sub / extra_sub / boundary / hallucination)，为 Claim 2 提供 mechanistic 证据"
    expected_results:
      bcs_zero_intra_sub_pct: 0.0
      bcs_zero_extra_sub_pct: 90.3
      bcs_low_intra_sub_pct: 1.6
      bcs_medium_intra_sub_pct: 10.6
      bcs_high_intra_sub_pct: 49.4
      intra_sub_per_100_gold_bcs_high: 12.93
      intra_sub_vs_bcs_spearman_rho: 1.0
      intra_sub_vs_bcs_p: "<0.001"
      chi_square: 6952
      chi_square_p: "~0"
      exp2_controlled_trend: "IntraSub 3.2% → 7.3% → 8.6% (rho=1.0)"
      hallucination_pct_across_bins: "<3%"
      cross_task_fewrel_intra_sub_rho: 0.954
    result_rationale: >
      在 best 档下，error taxonomy 展现近乎完美的单调关系：IntraSub (intra-batch type substitution)
      从 BCS=0 时的 0% 单调上升至 BCS≥0.95 时的 49.4%。这是因为 LLM 在 type assignment 阶段
      进行的是 soft attention over prompt-listed types——当两个 semantically similar types 共现于
      同一 batch prompt 中，attention weights 在它们之间分散，导致 type confusion。BCS=0 意味着
      batch 内无其他类型（单类型），自然不可能发生 intra-batch confusion。随着 BCS 增加（更多语义相邻
      类型共现），confusion 概率单调上升。ρ=1.0（4 个 ordered bins 完美单调）是 best 档下自然的结果。
      关键证据：hallucination < 3% 说明 LLM 的主要失败模式不是凭空捏造，而是在已知实体上标错类型——
      这直接验证了 "confusability → type confusion" 通道的存在。cross-task replication (FewRel ρ=0.954)
      证明此机制不限于 NER，在 RE 中同样成立。
    tables:
      - name: "Error Distribution by BCS Bin (Few-NERD)"
        columns: ["BCS Bin", "n_FP", "IntraSub%", "ExtraSub%", "IntraSub/100gold"]
        rows:
          - ["0 (single type)", 6172, 0.0, 90.3, 0.0]
          - ["Low (0.75-0.82)", 2231, 1.6, 89.9, 3.4]
          - ["Medium (0.82-0.88)", 3843, 10.6, 78.1, 6.5]
          - ["High (0.88-0.95+)", 6188, 49.4, 30.8, 12.9]
      - name: "Cross-Task Error Taxonomy Comparison"
        columns: ["Task", "IntraSub vs BCS ρ", "p-value", "Extra_sub=0?"]
        rows:
          - ["NER (Few-NERD)", 1.0, "<0.001", "No (extra exists)"]
          - ["RE (FewRel 80-rel)", 0.954, "<1e-6", "Yes (closed schema)"]
    figures_description:
      - "Stacked bar chart: error type proportions across 4 BCS bins，IntraSub 从蓝色小条逐渐占满"
      - "Dual-axis line plot: IntraSub rate (left) and Recall (right) vs BCS bin，展示正交通道"
    analysis: >
      Error taxonomy 提供了 Claim 2 的 mechanistic 支撑核心证据。两个通道完全分离：
      (1) IntraSub 仅与 BCS 相关（ρ=1.0），与 count 独立——即使 count 固定，高 BCS batch 仍产生
      更多 type confusion。(2) Recall decline 仅与 count 相关（exp-001 count curve），BCS 不影响
      detection probability 本身。这证明 count → recall drop 和 confusability → type confusion
      是 orthogonal degradation channels，可 independently 操作（减 count 提 recall，分 confusable types 减 confusion）。
      FewRel 的 ρ=0.954 表明 100% 的 RE type confusion 是 intra-batch 的（因为 closed-schema RE
      模型只能从 prompt-given relations 中选择），进一步巩固了 pairwise confusability 作为 causal mechanism 的地位。

  - name: "SDGD-zero on MAVEN (168 Event Types)"
    plan_id: "exp-009"
    description: "SDGD-zero 在 MAVEN 168 event types 上的 cross-task 验证。预期 negative result 与 Few-NERD 一致——merge amplification 是结构性问题"
    expected_results:
      single_pass_relaxed_f1: 0.247
      single_pass_precision: 0.285
      single_pass_recall: 0.218
      single_pass_batches: 1
      single_pass_time_s: 135
      sdgd_zero_relaxed_f1: 0.142
      sdgd_zero_precision: 0.108
      sdgd_zero_recall: 0.208
      sdgd_zero_batches: 12
      sdgd_zero_time_s: 820
      random_batch_relaxed_f1: 0.178
      random_batch_precision: 0.145
      random_batch_recall: 0.231
      random_batch_batches: 12
      random_batch_time_s: 780
      recall_improvement_sdgd_vs_single: "+(-0.01)"
      precision_drop_sdgd_vs_single: -0.177
      merge_amplification_ratio: 2.6
    result_rationale: >
      MAVEN 有 168 event types，decomposition 需要更多 batches（~12-14 vs Few-NERD 的 4-8）。
      在 best 档下，SDGD-zero 的 merge amplification 问题在 MAVEN 上更为严重，因为：
      (1) event trigger 的 boundary matching 本就模糊（exact F1 接近 0，relaxed F1 ~0.25），
      decomposed batches 各自产生 slightly different trigger boundaries → merge 时无法精确 dedup。
      (2) 168 types 意味着 confusability graph 更密（MAVEN 语义均匀），SDGD 切分后仍有 residual
      confusability within batches（因为切分只能 minimize 而非 eliminate）。
      (3) 同 Few-NERD 一致，decomposition 提升 recall（每个 batch 关注更少 types → 更少 miss）但
      merge 产生大量 duplicate/conflicting predictions → precision 暴跌。
      SDGD-zero 0.142 < random_batch 0.178 < single_pass 0.247——与 Few-NERD 的 ordering 完全一致，
      证明 merge amplification 是跨任务的结构性挑战。这被 best 档 framing 为诚实的 negative result，
      指向 calibration-based merge（SDGD-cal）或 single-pass + type-aware prompt engineering 作为 future work。
    tables:
      - name: "MAVEN SDGD-zero Comparison"
        columns: ["Mode", "Relaxed F1", "Precision", "Recall", "Batches", "Time(s)"]
        rows:
          - ["Single-pass", 0.247, 0.285, 0.218, 1, 135]
          - ["Random batch", 0.178, 0.145, 0.231, 12, 780]
          - ["SDGD-zero", 0.142, 0.108, 0.208, 12, 820]
      - name: "Cross-Task Decomposition Failure Pattern"
        columns: ["Dataset", "single_pass F1", "sdgd_zero F1", "sdgd/single ratio"]
        rows:
          - ["Few-NERD (NER)", 0.445, 0.241, 0.54]
          - ["MAVEN (ED)", 0.247, 0.142, 0.57]
    figures_description:
      - "Bar chart: F1 comparison across modes (single/random/sdgd) for MAVEN，标注与 Few-NERD 的 pattern 一致"
      - "Precision-Recall tradeoff scatter: 标注 merge amplification 如何 shift 各 mode 的 P-R 位置"
    analysis: >
      SDGD-zero 在 MAVEN 上的失败模式与 Few-NERD 完全一致：decomposition 略提 recall 但
      merge amplification 严重损害 precision。sdgd/single ratio (0.57) 与 Few-NERD (0.54) 接近，
      说明 merge amplification 是一个与数据集无关的结构性问题。在 best 档叙事中，这被框架为
      "naive confusability-aware decomposition 的 fundamental limitation"——虽然 pairwise SCS
      能正确识别 confusable pairs（已被 exp-015 验证），但 decompose-then-merge 策略本身
      引入了新的 error source（duplicate predictions, boundary inconsistency across batches）。
      论文 Section 6 用此结果论证：future work 应探索 calibration-based 方法（利用 empirical confusion
      直接 post-hoc correct predictions，而非 decompose input）。

  - name: "SDGD-cal on Few-NERD (Empirical Calibration)"
    plan_id: "exp-010"
    description: "SDGD-cal 用 5-10 calibration examples 构建 empirical confusion matrix 替代 embedding SCS。比较 vs SDGD-zero 和 single-pass"
    expected_results:
      single_pass_f1: 0.445
      sdgd_zero_f1: 0.241
      sdgd_cal_f1: 0.285
      sdgd_cal_precision: 0.295
      sdgd_cal_recall: 0.276
      sdgd_cal_batches: 5
      sdgd_cal_time_s: 380
      calibration_cost_examples: 10
      calibration_cost_inferences: 640
      improvement_over_zero: "+0.044 (+18%)"
      still_below_single_pass: "-0.160 (-36%)"
      empirical_confusion_vs_scs_rho: 0.42
      merge_amplification_reduced: "partially (better dedup with confidence)"
    result_rationale: >
      在 best 档下，SDGD-cal 比 SDGD-zero 有中等改善（+18% F1）但仍远不及 single-pass。原因：
      (1) empirical confusion matrix 确实比 embedding SCS 更准确（ρ=0.42 vs SCS 的 ρ=0.17-0.31
      with actual confusion），因此 SDGD-cal 的 batch composition 更好——truly confusable pairs
      被更有效地分开。(2) 但 merge amplification 问题与 batch composition quality 部分正交——
      即使 batch 内 confusion 降低，merge 时的 duplicate/conflict 问题仍存在。SDGD-cal 用
      empirical confusion 做 confidence-weighted merge（confused type pairs 的 predictions 以更高
      threshold 保留），所以 precision 略好于 SDGD-zero。(3) 然而，few-shot calibration 本身
      引入 variance——10 examples per type pair 不足以精确估计 confusion probability，导致
      部分 truly confusable pairs 仍被 assigned 到同一 batch。
      此结果在 best 档叙事中的作用：证明 problem 不在于 confusability 估计的质量，而在于
      decompose-then-merge 架构本身。这是一个 principled negative result，指向 "不要 decompose，
      而是 post-hoc calibrate" 的 future direction。
    tables:
      - name: "SDGD Variants Comparison (Few-NERD)"
        columns: ["Method", "F1", "Precision", "Recall", "Calibration Cost"]
        rows:
          - ["Single-pass", 0.445, 0.563, 0.368, "—"]
          - ["SDGD-zero (embedding)", 0.241, 0.324, 0.191, "0 examples"]
          - ["SDGD-cal (empirical)", 0.285, 0.295, 0.276, "10 examples × 66 types"]
          - ["Random batch", 0.301, 0.331, 0.276, "—"]
    figures_description:
      - "SDGD variant comparison bar chart with single-pass reference line"
      - "Scatter: empirical confusion rate vs embedding SCS for all type pairs (n=1953)，colored by SDGD-cal assignment"
    analysis: >
      SDGD-cal 改善了 batch composition quality（empirical confusion 比 SCS 更准确），但
      仍不能克服 merge amplification。关键 insight：decomposition 的 fundamental bottleneck 是
      merge 而非 partition。即使 partition 完美（zero intra-batch confusion），multi-batch merge
      仍产生 conflicting predictions。这意味着 confusability-aware 方法的正确 application 不是
      decompose input，而是 (1) post-hoc confusion matrix correction，或 (2) prompt engineering
      让模型自身 attend to confusable types（如 contrastive type descriptions）。

  - name: "SDGD-cal on MAVEN (168 Event Types)"
    plan_id: "exp-011"
    description: "SDGD-cal 在 MAVEN 上的 cross-task 测试，完成 full comparison table"
    expected_results:
      single_pass_relaxed_f1: 0.247
      sdgd_zero_relaxed_f1: 0.142
      sdgd_cal_relaxed_f1: 0.168
      sdgd_cal_precision: 0.132
      sdgd_cal_recall: 0.230
      sdgd_cal_batches: 8
      sdgd_cal_time_s: 650
      calibration_cost_examples: 5
      calibration_cost_inferences: 840
      improvement_over_zero_pct: "+18%"
      ratio_to_single_pass: 0.68
    result_rationale: >
      MAVEN 上 SDGD-cal vs SDGD-zero 的改善幅度与 Few-NERD 相近（~18%），因为改善来源一致：
      empirical confusion 比 SCS 更好地捕捉 MAVEN 特有的 confusable event pairs（如
      Killing↔Attack, Arranging↔Gathering）。但 MAVEN 的 168 types 意味着 calibration
      需要 significantly more examples（168×167/2 = 14028 pairs，每 pair 至少 5 examples），
      实际只用 5 examples per pair 的 subset → 估计 noisy。此外 MAVEN 的 trigger boundary
      天然模糊（event trigger ≠ named entity，span 定义歧义大），merge 时 boundary conflict
      比 NER 更严重。sdgd_cal/single ratio = 0.68，略好于 Few-NERD 的 0.64，但仍 far below par。
      在 best 档叙事中，MAVEN 复制 Few-NERD 的 failure pattern 是好事——它证明 merge amplification
      是 task-agnostic 的，不是某个 dataset 的 artifact。
    tables:
      - name: "MAVEN Full Comparison Table"
        columns: ["Method", "Relaxed F1", "Precision", "Recall", "Batches"]
        rows:
          - ["Single-pass (168 types)", 0.247, 0.285, 0.218, 1]
          - ["Random batch (k=12)", 0.178, 0.145, 0.231, 12]
          - ["SDGD-zero", 0.142, 0.108, 0.208, 12]
          - ["SDGD-cal (5-shot)", 0.168, 0.132, 0.230, 8]
      - name: "Cross-Task SDGD Failure Summary"
        columns: ["Dataset", "Task", "sdgd-cal/single", "merge_amplification"]
        rows:
          - ["Few-NERD", "NER", 0.64, "2.1x duplicate rate"]
          - ["MAVEN", "ED", 0.68, "2.6x duplicate rate"]
    figures_description:
      - "Grouped bar chart: Few-NERD vs MAVEN across all 4 methods，展示 pattern 一致性"
    analysis: >
      MAVEN 上的 SDGD 全面复制了 Few-NERD 的结论：decomposition 无法 outperform single-pass
      是因为 merge amplification 而非 partition quality。SDGD-cal 改善了 partition（fewer
      intra-batch confusions）但 merge 瓶颈不变。两个 dataset 的 sdgd-cal/single ratio
      convergent (0.64, 0.68) 表明这是一个 ~35% degradation 的稳定 structural cost。
      论文最终 framing：confusability 的价值不在于 decomposition，而在于 (1) diagnostic（预测哪些 schema
      区域 LLM 会出错），(2) 指导 future calibration-based approaches。

  - name: "Random Batching Ablation"
    plan_id: "exp-013"
    description: "与 SDGD 相同 batch count k，但 random composition。Isolates confusability-aware grouping from batch count reduction"
    expected_results:
      single_pass_f1: 0.445
      random_batch_k4_f1: 0.321
      random_batch_k8_f1: 0.301
      sdgd_zero_k4_f1: 0.241
      sdgd_zero_k8_f1: 0.218
      random_better_than_sdgd: true
      random_vs_sdgd_delta: "+0.080"
      both_below_single: true
      intra_batch_confusion_random: 0.034
      intra_batch_confusion_sdgd: 0.018
      intra_batch_confusion_single: 0.049
    result_rationale: >
      在 best 档下，random batching 优于 SDGD-zero (F1 0.301 vs 0.241)。这一 counterintuitive
      结果的原因：SDGD-zero 为了 minimize intra-batch confusability，倾向于产生 fewer but larger
      batches（将 all low-confusability types 放一起 → 产生一个巨大的 "easy" batch 和几个小的
      "hard" batches）。这种不均匀 partition 使得 merge 时大 batch 的 predictions dominate
      而小 batch 的 minority types 被 overwhelm。Random batching 产生更均匀的 batch sizes →
      merge 更 balanced。

      但 random batch 仍 << single-pass，证明 decomposition 本身（不只是 partition quality）
      是 root cause of degradation。这个 ablation 在论文中的关键作用：排除 "SDGD failed because
      confusability-aware grouping doesn't work" 的解读——实际上 confusability-aware grouping
      确实减少了 intra-batch confusion (0.018 vs 0.034)，但 merge amplification 的 negative effect
      超过了 confusion reduction 的 positive effect。
    tables:
      - name: "Random vs SDGD Ablation"
        columns: ["Method", "F1", "IntraBatch Confusion Rate", "Merge Duplicates"]
        rows:
          - ["Single-pass (k=1)", 0.445, 0.049, "—"]
          - ["Random (k=4)", 0.321, 0.034, "1.8x"]
          - ["Random (k=8)", 0.301, 0.028, "2.1x"]
          - ["SDGD-zero (k=4)", 0.241, 0.018, "2.4x"]
          - ["SDGD-zero (k=8)", 0.218, 0.012, "2.8x"]
    figures_description:
      - "Decomposition overhead analysis: F1 vs batch count k，with random and SDGD lines both declining"
      - "IntraBatch confusion rate vs F1 scatter: SDGD 有更低的 confusion 但更低的 F1"
    analysis: >
      此 ablation 精确定位了 SDGD 失败的原因层次：(1) 所有 decomposition 都比 single-pass 差
      → merge 是瓶颈；(2) SDGD 比 random 更差 → confusability-aware grouping 的 unbalanced
      partition 使 merge 更难；(3) SDGD 确实降低了 intra-batch confusion (0.018 vs 0.034)
      → confusability signal 本身有效，但 application 方式错误。
      结论：confusability 信息的价值在于 diagnosis 而非 naive decomposition。

  - name: "Per-type Splitting (UniNER-style)"
    plan_id: "exp-014"
    description: "每 type 一个 batch（k=66 for Few-NERD），upper bound on decomposition recall benefit，latency vs quality tradeoff"
    expected_results:
      single_pass_f1: 0.445
      single_pass_recall: 0.368
      single_pass_precision: 0.563
      per_type_f1: 0.292
      per_type_recall: 0.586
      per_type_precision: 0.194
      per_type_batches: 66
      per_type_time_s: 2540
      per_type_api_calls: 66
      recall_gain_vs_single: "+0.218 (+59%)"
      precision_loss_vs_single: "-0.369 (-66%)"
      latency_multiplier: "32x"
      merge_duplicate_rate: 3.4
      per_type_vs_sdgd_recall: "+0.395"
      per_type_vs_sdgd_f1: "+0.051"
    result_rationale: >
      Per-type splitting 是 decomposition 的极端形式——每个 batch 只含一个 type，完全消除
      intra-batch confusability (BCS=0)。在 best 档下，recall 达到最高值 0.586（vs single-pass 0.368），
      因为 LLM 在 single-type prompt 下只需回答 "这段文本中有没有 X type 的 entity"——
      一个比 "从 66 个 types 中为每个 entity 选正确 type" 简单得多的 binary detection task。
      但 precision 暴跌至 0.194：(1) 模型对 single-type prompt 过度 eager（每次都倾向于
      "找到" 该 type 的 entity，false positive rate 高）——这在 exp-001 count_1 已观测到
      (pred/gold=2.97)；(2) 66 个 batch 的 merge 产生大量 duplicate predictions（同一 span
      被多个 type-specific batches 标注）。

      Per-type 的 F1=0.292 优于 SDGD-zero (0.241) 但仍远不及 single-pass (0.445)。
      这说明即使 zero confusability 也无法 compensate merge amplification 的 cost。
      Latency 是 32x（66 次 API call vs 1 次），从实践角度完全不可接受。
      在论文中的作用：作为 decomposition 的 upper bound，证明 "即使最极端的分离也不如不分离"。
    tables:
      - name: "Decomposition Spectrum"
        columns: ["Method", "F1", "Precision", "Recall", "Batches", "IntraBatch BCS", "Time(s)"]
        rows:
          - ["Single-pass (all types)", 0.445, 0.563, 0.368, 1, 0.95, 79]
          - ["SDGD-zero (minimized)", 0.241, 0.324, 0.191, 4, 0.72, 261]
          - ["Random (k=8)", 0.301, 0.331, 0.276, 8, 0.85, 494]
          - ["Per-type (k=66)", 0.292, 0.194, 0.586, 66, 0.0, 2540]
    figures_description:
      - "Precision-Recall curve: 各 decomposition mode 标注在 P-R space，single-pass 占据最优 F1 位置"
      - "Latency-F1 tradeoff plot: per-type 以巨大 latency cost 获得 marginal recall gain"
    analysis: >
      Per-type splitting 揭示了 decomposition 的 fundamental paradox：分离越彻底，recall 越高
      （0.586 >> 0.368），但 merge noise 也越大 → precision 崩塌。F1 的 harmonic mean 性质
      意味着 precision 的大幅下降无法被 recall 的中等提升补偿。
      此结果为论文提供了一个清晰的 design principle：confusability-aware batch composition 的
      correct application 不是 decompose-then-merge，而是 (1) single-pass extraction + post-hoc
      confusion-aware calibration，或 (2) contrastive type descriptions in prompt 帮助模型
      区分 confusable types without decomposing the input。

  - name: "SCS Validation (Embedding Proxy)"
    plan_id: "exp-015"
    description: "SCS vs empirical confusion matrix 的 rank correlation，验证 embedding 作为 confusability proxy 的有效性"
    expected_results:
      all_pairs_n: 1953
      all_pairs_nonzero_n: 216
      qwen3_all_spearman: 0.168
      qwen3_all_spearman_p: "7.3e-14"
      qwen3_all_kendall: 0.135
      minilm_all_spearman: 0.144
      minilm_all_spearman_p: "1.7e-10"
      minilm_all_kendall: 0.115
      qwen3_nonzero_spearman: 0.272
      qwen3_nonzero_p: "5.0e-05"
      minilm_nonzero_spearman: 0.306
      minilm_nonzero_p: "4.6e-06"
      minilm_nonzero_kendall: 0.228
      qwen3_better_overall: true
      minilm_better_nonzero: true
    result_rationale: >
      在 best 档下，SCS 被验证为 statistically significant 但 partial 的 confusion proxy。
      两个 embedding 都显著预测 empirical confusion (all p < 1e-5)——这是 A1 成立的前提
      （reviewer 接受 r=0.11-0.13 为有意义效应量的前提是 SCS 被验证为 valid proxy）。

      Qwen3 在 all-pairs 上更强 (ρ=0.168 vs 0.144)，因为 Qwen3 是 extraction model 本身——
      其 embedding space 直接反映 model 如何 represent types，因此 type similarity in Qwen3 space
      = type confusability for Qwen3。MiniLM 在 nonzero-only pairs 上更强 (ρ=0.306 vs 0.272)，
      因为 MiniLM 是专门为 sentence similarity 设计的——一旦过滤掉 zero-confusion pairs
      （大多是 trivially dissimilar types），MiniLM 在 actually-confused pairs 中更好地
      rank similarity differences。

      关键 insight：SCS 是 "valid but partial" proxy——context, frequency, mention ambiguity
      also matter。这意味着 (1) SCS 足以支撑 Claim 1 的相关性分析，(2) 但不足以做 precision
      decomposition（解释为什么 SDGD-zero < SDGD-cal）。这恰好支撑了论文的 "empirical confusion
      matrix as future direction" narrative。
    tables:
      - name: "SCS vs Empirical Confusion Correlation"
        columns: ["Embedding", "Scope", "Spearman ρ", "p-value", "Kendall τ"]
        rows:
          - ["Qwen3-32B", "All pairs (n=1953)", 0.168, "7.3e-14", 0.135]
          - ["Qwen3-32B", "Nonzero only (n=216)", 0.272, "5.0e-05", 0.200]
          - ["MiniLM-L6-v2", "All pairs (n=1953)", 0.144, "1.7e-10", 0.115]
          - ["MiniLM-L6-v2", "Nonzero only (n=216)", 0.306, "4.6e-06", 0.228]
    figures_description:
      - "Hexbin plot: SCS (x) vs empirical confusion count (y)，two panels for Qwen3 and MiniLM"
      - "ROC curve: SCS as binary predictor of 'will this pair be confused?' at various thresholds"
    analysis: >
      SCS validation 完成两个关键论证：(1) embedding similarity IS a valid proxy for LLM confusion
      (所有 p < 1e-5)，因此 Claim 1 中使用 SCS 作为 confusability measure 是 methodologically sound。
      (2) SCS is PARTIAL (ρ ~0.17-0.31, not 0.8+)，说明 confusability 还有 SCS 未捕捉的维度
      （如 context-dependent ambiguity, frequency-driven familiarity, instruction-following bias）。
      这个 "valid but partial" 结论同时支撑了：(a) paper 的 main claim（SCS 有效），和
      (b) negative SDGD result 的合理性（SCS 不够精确做 surgical decomposition），以及
      (c) future work direction（empirical confusion bypass embedding entirely）。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5156ba7d-a881-49c5-889f-f0bc407d95e5",
  "isSidechain": false,
  "requestId": "req_011Cb5sHx2xMMBSTerDzQXRT",
  "type": "assistant",
  "uuid": "18bbdf32-3e44-4b76-9838-fb01a4822de7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYHJr42yUzMHPVZgoJ72WC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6394,
      "cache_read_input_tokens": 40492,
      "output_tokens": 11008,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6394,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11008,
          "cache_read_input_tokens": 40492,
          "cache_creation_input_tokens": 6394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6394
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

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：两条 claim 均以当前数据充分支撑，SDGD 负面结果被视为方法论贡献，论文被 EMNLP Main 接收 核心假设：['A1: Pairwise SCS→confusion 的 r=0.11-0.13 被接受为有意义的效应量（reviewers 认可 noise floor 高的 IE 任务中此量级合理…",
  "leafUuid": "18bbdf32-3e44-4b76-9838-fb01a4822de7",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-task confusability effect sizes with multi-model validation",
  "sessionId": "1e00b948-dfc5-4298-ba2f-145c6f5d5244"
}
```

---
