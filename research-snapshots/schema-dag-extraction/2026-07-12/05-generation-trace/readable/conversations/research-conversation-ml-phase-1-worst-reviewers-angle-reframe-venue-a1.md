# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：核心假设不被 reviewers 接受为充分验证，论文被拒，需要找新 angle 重新 reframe 后重投同一 venue 核心假设：['A1 不

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/0e6c27b0-7db8-410b-bb6a-2c3b60a3775b.jsonl`
- **Structured JSON:** [`c4f6c4a2a17cc13a2773.json`](../../sessions/c4/c4f6c4a2a17cc13a2773.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T07:50:05.450Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T07:50:05.450Z",
  "sessionId": "0e6c27b0-7db8-410b-bb6a-2c3b60a3775b",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：核心假设不被 reviewers 接受为充分验证，论文被拒，需要找新 angle 重新 reframe 后重投同一 venue\n核心假设：['A1 不被接受: 多位 reviewer 认为 r=0.11-0.13 太小，FewRel 的大效应被归因于 extreme batch design（非自然条件）', \"A2 部分成立但被矮化: Error taxonomy 被视为'描述性工作'而非贡献\", 'A3 被质疑: 3.4× amplification 来自 16-rel vs 80-rel 对比，reviewer 指出这混淆了 count 和 confusability 的 scaling', 'A4 失败: LLaMA NER 多次崩溃 + 仅 FewRel 一个任务复现被判定为不充分', 'A5 被拒绝: MAVEN per-type 正方向被视为反证，centrality confound 解释被认为是 post-hoc rationalization', \"A6 被拒绝: '没有可用方法的分析论文不适合 EMNLP Main/Findings'\", 'A7 失败: 多位 reviewer 认为贡献不足以构成独立论文']\n关键指标范围：{'arr_avg_score': [2.0, 3.0], 'claims_fully_supported': [0, 1], 'major_reviewer_weaknesses': [4, 6], 'cross_task_significant_replications': [1, 2], 'multi_model_effect_consistency': [0.5, 0.7], 'venue_probability_main': [0.0, 0.1], 'venue_probability_findings_or_above': [0.05, 0.25], 'rebuttal_flip_probability': [0.05, 0.25]}\n叙事方向：放弃 \"confusability predicts degradation\" 作为标题级 claim。Reframe 为 \"Characterizing and Diagnosing Schema-Induced Failure Modes in Training-Free LLM IE\"。 核心叙事转向: (1) 提出 multi-channel degradation 作为诊断框架（不是预测模型）， error taxonomy 成为主要贡献; (2) 将 pairwise correlation 作为 channel 2 存在性的 supporting evidence 而非独立 claim; (3) SDGD 失败 + MAVEN centrality confound 合并为 \"schema decomposition 比想象中更难\" 的系统性分析; (4) 新增 prescriptive 贡献: 基于所有实验（包括负面结果）给出 schema 设计决策树。需要补充的实验: (a) 至少一个非 extreme-batch 的自然条件下的 BCS 效应验证, (b) 第二个模型在 NER 或 ED 上的成功复现（考虑换 Mistral 或 Gemma 而非继续 LLaMA）, (c) 将 SDGD-cal（empirical confusion matrix）跑通作为 proof-of-concept。 目标仍是 EMNLP 2026（下一个 ARR cycle, September），不降级 venue。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: schema-dag-extraction\n\n## paper_framing.md\n\n# Paper Framing — schema-dag-extraction\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\n- Commitment deadline: August 2, 2026\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\n- Deadline: ARR May 25, 2026 (10 days from today)\n\n## Core Claims (2 claims) — Revised per D019\n\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\n\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\n\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \"why naive decomposition fails\" is itself a contribution.\n\n## Story Spine — Revised per D012\n\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\n\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\n\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.\n\n- **Three-task validation**:\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\n\n- **Headline result template**: \"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid.\"\n\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\n\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\n\nThese channels are orthogonal and independently addressable.\n\n**Pairwise vs Aggregated Confusability**:\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\n\n## Evidence Hierarchy (D012)\n\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\n\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\n\n**Few-NERD (NER)** — Qwen3 embeddings:\n- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation\n- Nonzero-only Spearman ρ=0.272 (p=5e-5)\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\n- Immune to type frequency confound (operates at type-pair level)\n\n**MAVEN (ED)** — MiniLM embeddings:\n- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\n- Cross-task replication on same-domain schema\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\n\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\n\nLarge effect size, cross-task (RE), scaling with schema complexity:\n\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\n\n**16-rel sanity check** (exp_fewrel_formal):\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\n\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\n\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\n\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\n\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\n\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\n\nMethodological case study on when aggregated confusability measures fail:\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\n- This is stronger than \"domain boundary\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\n\n### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)\n\nIntraSub rate monotonically increases with BCS on both NER and RE:\n\n**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0\n**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)\n- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon\n- Same mechanism, different absolute magnitudes — consistent with cross-task expectations\n\nAdditional from extreme batch design:\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\n\n## Embedding Ablation (D010)\n\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\n\n### Per-type (Layer 2)\n| | Few-NERD | FewRel | MAVEN |\n|---|---|---|---|\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\n\n### Pairwise (Layer 1)\n| | Few-NERD | MAVEN |\n|---|---|---|\n| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |\n| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |\n\n### SCS→Empirical Confusion Validation (exp-015 fast)\n| | Qwen3 | MiniLM |\n|---|---|---|\n| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |\n| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |\n\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \"Lost in the Middle\" (TACL 2024).\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy | Experiment |\n|---------|------------------|------------|\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]\n    on Few-NERD with Qwen3-32B-FP8'\n  priority: P0\n  gpu_budget_hours: 3.5\n  deps: []\n  registry_id: exp001_count_baseline\n  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction\n    at low counts.\n  status: DONE\n  conclusion: success\n  metrics:\n    diagnosis: char offset 96.5% fabricated by model\n    text_match_reeval:\n      count_1:\n        f1: 0.184\n        precision: 0.105\n        recall: 0.72\n        pred_gold_ratio: 6.85\n      count_2:\n        f1: 0.123\n        precision: 0.068\n        recall: 0.698\n        pred_gold_ratio: 10.33\n      count_6:\n        f1: 0.155\n        precision: 0.088\n        recall: 0.62\n        pred_gold_ratio: 7.02\n      count_12:\n        f1: 0.246\n        precision: 0.16\n        recall: 0.539\n        pred_gold_ratio: 3.38\n      count_22:\n        f1: 0.322\n        precision: 0.232\n        recall: 0.527\n        pred_gold_ratio: 2.27\n      count_44:\n        f1: 0.473\n        precision: 0.414\n        recall: 0.551\n        pred_gold_ratio: 1.33\n      count_64:\n        f1: 0.463\n        precision: 0.52\n        recall: 0.418\n        pred_gold_ratio: 0.8\n    key_finding: recall monotonically decreases (0.72→0.42), precision monotonically\n      increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at\n      count_44\n    wrong_type_trend: 'type confusion increases with count: 0→2434, supports confusability\n      hypothesis'\n    spurious_dominant: spurious FPs (text in source but not entity) dominate at low\n      count, not hallucination\n    conclusion_text_match: F1 curve inversion caused by over-prediction confound,\n      NOT absence of confusability effect. Recall curve + type confusion pattern support\n      hypothesis.\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,\n    25 random + extreme batches on Few-NERD'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  registry_id: exp002_confusability_controlled\n  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion\n    rate 10-28x.\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp2_reeval_results.json (text_match, CLEAN)\n    primary_recall_vs_bcs:\n      count_6:\n        r: 0.2754\n        p: 0.1644\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.2219\n        p: 0.266\n        n: 27\n        verdict: FAIL\n      partial:\n        r: 0.2522\n        p: 0.0658\n        n: 54\n        verdict: FAIL\n    secondary_f1_vs_bcs:\n      count_6:\n        r: 0.1754\n        p: 0.3814\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.5012\n        p: 0.0077\n        n: 27\n        verdict: PASS\n      partial:\n        r: 0.3025\n        p: 0.0262\n        n: 54\n        verdict: PASS\n    mechanistic_confusion_rate:\n      random_batches:\n        count_6_high: 0.0157\n        count_6_low: 0.0088\n        ratio_6: 1.7\n        count_12_high: 0.0304\n        count_12_low: 0.0131\n        ratio_12: 2.4\n      extreme_batches:\n        count_6_high: 0.0728\n        count_6_low: 0.0014\n        ratio_6: 27.5\n        count_12_high: 0.048\n        count_12_low: 0.0061\n        ratio_12: 9.9\n      verdict: PASS\n    pairwise_confusion_analysis:\n      all:\n        n_pairs: 1953\n        pearson_r: 0.156\n        pearson_p: 4.6e-12\n        spearman_rho: 0.16\n        spearman_p: 1.3e-12\n      count_6:\n        n_pairs: 1770\n        pearson_r: 0.078\n        pearson_p: 0.001\n      count_12:\n        n_pairs: 1953\n        pearson_r: 0.147\n        pearson_p: 6.7e-11\n      nonzero_only:\n        all_spearman_rho: 0.254\n        all_spearman_p: 1.1e-06\n        count_12_pearson_r: 0.212\n        count_12_p: 0.00034\n      top_confused_pair: person-other <-> person-politician (BCS=0.934, confusion=156)\n    per_type_analysis:\n      n_types: 63\n      filter: freq>=5\n      micro_f1_vs_bcs:\n        pearson_r: -0.1828\n        pearson_p: 0.1516\n        spearman_rho: -0.2927\n        spearman_p: 0.0199\n        partial_r_ctrl_logfreq: -0.1998\n        partial_p: 0.1163\n      mean_f1_vs_bcs:\n        pearson_r: -0.1374\n        pearson_p: 0.283\n        spearman_rho: -0.2412\n        spearman_p: 0.0568\n        partial_r_ctrl_logfreq: -0.1428\n        partial_p: 0.2641\n      quartile_comparison:\n        low_bcs_cutoff: 0.798\n        high_bcs_cutoff: 0.827\n        low_bcs_f1: 0.3098\n        high_bcs_f1: 0.2275\n        delta_f1: -0.0823\n        low_bcs_freq: 2134\n        high_bcs_freq: 2049\n      confound_check:\n        bcs_vs_logfreq_r: 0.042\n        bcs_vs_logfreq_p: 0.74\n        logfreq_vs_f1_r: 0.25\n        logfreq_vs_f1_p: 0.048\n      verdict: Direction supports hypothesis. Spearman significant (p=0.02). Frequency\n        confound absent at type level (r=0.04).\n    overall_verdict: PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE\n      STRONG PASS, PER-TYPE DIRECTIONAL PASS\n- id: exp-003a\n  claim:\n  - 1\n  - 2\n  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination\n    instruction. Re-run exp1+exp2.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp003a_prompt_v2_rerun\n  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_mode: text_match\n    exp1_text_match:\n      count_1:\n        f1: 0.323\n        precision: 0.216\n        recall: 0.641\n        pred_gold_ratio: 2.97\n        n_batches: 64\n      count_2:\n        f1: 0.273\n        precision: 0.18\n        recall: 0.56\n        pred_gold_ratio: 3.11\n        n_batches: 5\n      count_6:\n        f1: 0.306\n        precision: 0.226\n        recall: 0.475\n        pred_gold_ratio: 2.1\n        n_batches: 5\n      count_12:\n        f1: 0.347\n        precision: 0.367\n        recall: 0.329\n        pred_gold_ratio: 0.9\n        n_batches: 5\n      count_22:\n        f1: 0.299\n        precision: 0.339\n        recall: 0.267\n        pred_gold_ratio: 0.79\n        n_batches: 5\n      count_44:\n        f1: 0.445\n        precision: 0.506\n        recall: 0.396\n        pred_gold_ratio: 0.78\n        n_batches: 5\n      count_64:\n        f1: 0.414\n        precision: 0.648\n        recall: 0.304\n        pred_gold_ratio: 0.47\n        n_batches: 5\n    exp2_text_match:\n      count_6:\n        f1: 0.32\n        precision: 0.26\n        recall: 0.416\n        pred_gold_ratio: 1.6\n        n_batches: 27\n      count_12:\n        f1: 0.306\n        precision: 0.291\n        recall: 0.323\n        pred_gold_ratio: 1.11\n        n_batches: 27\n    vs_exp001_delta:\n      count_1:\n        f1_delta: +0.139 (+76%)\n        precision_delta: +0.111 (+106%)\n        recall_delta: -0.079 (-11%)\n        overpred_fix: 6.85→2.97\n      count_6:\n        f1_delta: +0.151 (+97%)\n        precision_delta: +0.138 (+157%)\n        recall_delta: -0.145 (-23%)\n      count_12:\n        f1_delta: +0.101 (+41%)\n        precision_delta: +0.207 (+129%)\n        recall_delta: -0.210 (-39%)\n      count_44:\n        f1_delta: -0.028 (-6%)\n        precision_delta: +0.092 (+22%)\n        recall_delta: -0.155 (-28%)\n      count_64:\n        f1_delta: -0.049 (-11%)\n        precision_delta: +0.128 (+25%)\n        recall_delta: -0.114 (-27%)\n    key_finding: 'V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x\n      to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1).\n      But over-corrected at high counts: under-prediction (pred/gold<1) caused recall\n      drops of 27-39%, slightly lowering F1 at count_22-64.'\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MAVEN confusability study: count curve + within-count BCS correlation\n    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core\n    finding cross-task (NER→ED) with larger type space and known sibling confusion\n    (14.6-19.8%).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp-004\n  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs\n    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy\n    structure.'\n  status: DONE\n  conclusion: success\n  metrics:\n    n_event_types: 168\n    n_pairs: 14028\n    scs_mean: 0.2161\n    scs_std: 0.103\n    scs_max: 0.8368\n    scs_median: 0.2121\n    scs_q90: 0.3457\n    scs_q95: 0.3892\n    pairs_above_0.5: 119\n    pct_above_0.5: 0.85\n    train_docs: 2913\n    train_mentions: 77993\n    valid_docs: 710\n    valid_mentions: 18904\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n  status: planned\n- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n  status: planned\n- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.\n  status: planned\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional\n    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model\n    generalizability.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-003a\n  registry_id: exp012_llama_8b_r3\n  status: DONE\n  conclusion: failed\n- id: exp-016\n  claim:\n  - 1\n  - 2\n  description: 'FewRel cross-task replication: count curve + BCS correlation on FewRel\n    RE (80 relation types with --use_all). Replicates confusability effect NER→RE.\n    Pilot (fewrel_pilot) confirmed signal; formal run with full count curve [1,4,8,16,32,64,80].'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp_fewrel_formal\n  status_note: RUNNING (16-rel version). Will rerun with --use_all for 80-rel full\n    count curve after current run completes.\n  status: DONE\n  conclusion: success\n  metrics:\n    note: 16-rel sanity check only\n    exp1:\n      count_1:\n        mean_acc: 0.904\n        n_batches: 16\n      count_4:\n        mean_acc: 0.932\n        n_batches: 5\n      count_8:\n        mean_acc: 0.867\n        n_batches: 5\n      count_16:\n        mean_acc: 0.778\n        n_batches: 5\n        bcs: 0.9\n        zero_variance: true\n    exp2:\n      count_8_low_bcs:\n        acc: 0.889\n        bcs: 0.782\n      count_8_high_bcs:\n        acc: 0.798\n        bcs: 0.892\n      delta_bcs_effect: -0.091\n    trend: 'count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8%\n      (Δ=-9.1pp)'\n- id: exp-008\n  claim:\n  - 3\n  description: 'SDGD-zero on Few-NERD: confusability-minimizing batch composition\n    via embedding SCS + graph coloring. Compare vs single-pass full-schema baseline.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-003a\n  registry_id: exp008_sdgd_v2_fewnerd\n  status_note: 'DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass\n    baseline on Few-NERD. R1 (exp008_sdgd_zero_fewnerd) failed with script error.'\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 79\n    random_batch:\n      f1: 0.3007\n      precision: 0.3307\n      recall: 0.2758\n      batches: 8\n      time_s: 494\n    sdgd_zero:\n      f1: 0.2407\n      precision: 0.3244\n      recall: 0.1913\n      batches: 4\n      time_s: 261\n    per_type: killed before completion (3/4 modes done, Director approved kill)\n    vs_v1: confidence-gated merge did not improve over union merge. sdgd_zero 0.241\n      vs v1 0.251, random_batch 0.301 vs v1 0.320\n    key_finding: SDGD v2 confidence-gated merge + min_batch_size=8 failed to beat\n      single_pass baseline (F1=0.445). Both v1 and v2 confirm decomposition hurts\n      precision more than it helps recall. Claim 3 (SDGD framework) needs fundamental\n      rethink.\n- id: exp-009\n  claim:\n  - 3\n  description: 'SDGD-zero on MAVEN: confusability-minimizing batch composition on\n    168 event types. Compare vs single-pass + random batching. Cross-task validation\n    of SDGD framework (NER→ED).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-004\n  - exp-008\n  status: planned\n- id: exp-010\n  claim:\n  - 3\n  description: 'SDGD-cal on Few-NERD: empirical confusability from 5-10 calibration\n    examples (no gradients). Compare vs SDGD-zero.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-008\n  status: planned\n- id: exp-011\n  claim:\n  - 3\n  description: 'SDGD-cal on MAVEN: empirical confusability with calibration on 168\n    event types. Full comparison table.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-009\n  - exp-010\n  status: planned\n- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n  status: planned\n- id: exp-014\n  claim:\n  - 3\n  description: 'Ablation: per-type splitting (UniNER-style, 1 type per batch). Upper\n    bound on decomposition benefit. Reveals latency vs quality tradeoff.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n  status: planned\n- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp001_count_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    diagnosis: char offset 96.5% fabricated by model\n    text_match_reeval:\n      count_1:\n        f1: 0.184\n        precision: 0.105\n        recall: 0.72\n        pred_gold_ratio: 6.85\n      count_2:\n        f1: 0.123\n        precision: 0.068\n        recall: 0.698\n        pred_gold_ratio: 10.33\n      count_6:\n        f1: 0.155\n        precision: 0.088\n        recall: 0.62\n        pred_gold_ratio: 7.02\n      count_12:\n        f1: 0.246\n        precision: 0.16\n        recall: 0.539\n        pred_gold_ratio: 3.38\n      count_22:\n        f1: 0.322\n        precision: 0.232\n        recall: 0.527\n        pred_gold_ratio: 2.27\n      count_44:\n        f1: 0.473\n        precision: 0.414\n        recall: 0.551\n        pred_gold_ratio: 1.33\n      count_64:\n        f1: 0.463\n        precision: 0.52\n        recall: 0.418\n        pred_gold_ratio: 0.8\n    key_finding: recall monotonically decreases (0.72→0.42), precision monotonically\n      increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at\n      count_44\n    wrong_type_trend: 'type confusion increases with count: 0→2434, supports confusability\n      hypothesis'\n    spurious_dominant: spurious FPs (text in source but not entity) dominate at low\n      count, not hallucination\n    conclusion_text_match: F1 curve inversion caused by over-prediction confound,\n      NOT absence of confusability effect. Recall curve + type confusion pattern support\n      hypothesis.\n- exp_id: exp002_confusability_controlled\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp2_reeval_results.json (text_match, CLEAN)\n    primary_recall_vs_bcs:\n      count_6:\n        r: 0.2754\n        p: 0.1644\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.2219\n        p: 0.266\n        n: 27\n        verdict: FAIL\n      partial:\n        r: 0.2522\n        p: 0.0658\n        n: 54\n        verdict: FAIL\n    secondary_f1_vs_bcs:\n      count_6:\n        r: 0.1754\n        p: 0.3814\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.5012\n        p: 0.0077\n        n: 27\n        verdict: PASS\n      partial:\n        r: 0.3025\n        p: 0.0262\n        n: 54\n        verdict: PASS\n    mechanistic_confusion_rate:\n      random_batches:\n        count_6_high: 0.0157\n        count_6_low: 0.0088\n        ratio_6: 1.7\n        count_12_high: 0.0304\n        count_12_low: 0.0131\n        ratio_12: 2.4\n      extreme_batches:\n        count_6_high: 0.0728\n        count_6_low: 0.0014\n        ratio_6: 27.5\n        count_12_high: 0.048\n        count_12_low: 0.0061\n        ratio_12: 9.9\n      verdict: PASS\n    pairwise_confusion_analysis:\n      all:\n        n_pairs: 1953\n        pearson_r: 0.156\n        pearson_p: 4.6e-12\n        spearman_rho: 0.16\n        spearman_p: 1.3e-12\n      count_6:\n        n_pairs: 1770\n        pearson_r: 0.078\n        pearson_p: 0.001\n      count_12:\n        n_pairs: 1953\n        pearson_r: 0.147\n        pearson_p: 6.7e-11\n      nonzero_only:\n        all_spearman_rho: 0.254\n        all_spearman_p: 1.1e-06\n        count_12_pearson_r: 0.212\n        count_12_p: 0.00034\n      top_confused_pair: person-other <-> person-politician (BCS=0.934, confusion=156)\n    per_type_analysis:\n      n_types: 63\n      filter: freq>=5\n      micro_f1_vs_bcs:\n        pearson_r: -0.1828\n        pearson_p: 0.1516\n        spearman_rho: -0.2927\n        spearman_p: 0.0199\n        partial_r_ctrl_logfreq: -0.1998\n        partial_p: 0.1163\n      mean_f1_vs_bcs:\n        pearson_r: -0.1374\n        pearson_p: 0.283\n        spearman_rho: -0.2412\n        spearman_p: 0.0568\n        partial_r_ctrl_logfreq: -0.1428\n        partial_p: 0.2641\n      quartile_comparison:\n        low_bcs_cutoff: 0.798\n        high_bcs_cutoff: 0.827\n        low_bcs_f1: 0.3098\n        high_bcs_f1: 0.2275\n        delta_f1: -0.0823\n        low_bcs_freq: 2134\n        high_bcs_freq: 2049\n      confound_check:\n        bcs_vs_logfreq_r: 0.042\n        bcs_vs_logfreq_p: 0.74\n        logfreq_vs_f1_r: 0.25\n        logfreq_vs_f1_p: 0.048\n      verdict: Direction supports hypothesis. Spearman significant (p=0.02). Frequency\n        confound absent at type level (r=0.04).\n    overall_verdict: PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE\n      STRONG PASS, PER-TYPE DIRECTIONAL PASS\n- exp_id: exp003a_prompt_v2_rerun\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_mode: text_match\n    exp1_text_match:\n      count_1:\n        f1: 0.323\n        precision: 0.216\n        recall: 0.641\n        pred_gold_ratio: 2.97\n        n_batches: 64\n      count_2:\n        f1: 0.273\n        precision: 0.18\n        recall: 0.56\n        pred_gold_ratio: 3.11\n        n_batches: 5\n      count_6:\n        f1: 0.306\n        precision: 0.226\n        recall: 0.475\n        pred_gold_ratio: 2.1\n        n_batches: 5\n      count_12:\n        f1: 0.347\n        precision: 0.367\n        recall: 0.329\n        pred_gold_ratio: 0.9\n        n_batches: 5\n      count_22:\n        f1: 0.299\n        precision: 0.339\n        recall: 0.267\n        pred_gold_ratio: 0.79\n        n_batches: 5\n      count_44:\n        f1: 0.445\n        precision: 0.506\n        recall: 0.396\n        pred_gold_ratio: 0.78\n        n_batches: 5\n      count_64:\n        f1: 0.414\n        precision: 0.648\n        recall: 0.304\n        pred_gold_ratio: 0.47\n        n_batches: 5\n    exp2_text_match:\n      count_6:\n        f1: 0.32\n        precision: 0.26\n        recall: 0.416\n        pred_gold_ratio: 1.6\n        n_batches: 27\n      count_12:\n        f1: 0.306\n        precision: 0.291\n        recall: 0.323\n        pred_gold_ratio: 1.11\n        n_batches: 27\n    vs_exp001_delta:\n      count_1:\n        f1_delta: +0.139 (+76%)\n        precision_delta: +0.111 (+106%)\n        recall_delta: -0.079 (-11%)\n        overpred_fix: 6.85→2.97\n      count_6:\n        f1_delta: +0.151 (+97%)\n        precision_delta: +0.138 (+157%)\n        recall_delta: -0.145 (-23%)\n      count_12:\n        f1_delta: +0.101 (+41%)\n        precision_delta: +0.207 (+129%)\n        recall_delta: -0.210 (-39%)\n      count_44:\n        f1_delta: -0.028 (-6%)\n        precision_delta: +0.092 (+22%)\n        recall_delta: -0.155 (-28%)\n      count_64:\n        f1_delta: -0.049 (-11%)\n        precision_delta: +0.128 (+25%)\n        recall_delta: -0.114 (-27%)\n    key_finding: 'V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x\n      to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1).\n      But over-corrected at high counts: under-prediction (pred/gold<1) caused recall\n      drops of 27-39%, slightly lowering F1 at count_22-64.'\n- exp_id: exp-004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_event_types: 168\n    n_pairs: 14028\n    scs_mean: 0.2161\n    scs_std: 0.103\n    scs_max: 0.8368\n    scs_median: 0.2121\n    scs_q90: 0.3457\n    scs_q95: 0.3892\n    pairs_above_0.5: 119\n    pct_above_0.5: 0.85\n    train_docs: 2913\n    train_mentions: 77993\n    valid_docs: 710\n    valid_mentions: 18904\n- exp_id: exp004_maven_bcs\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    exp1_count_curve:\n      count_1:\n        n_batches: 64\n        exact_f1: 0.009\n        relaxed_f1: 0.106\n        bcs: 0\n      count_6:\n        n_batches: 5\n        exact_f1: 0.003\n        relaxed_f1: 0.103\n        bcs: 0.892\n      count_12:\n        n_batches: 5\n        exact_f1: 0.008\n        relaxed_f1: 0.146\n        bcs: 0.921\n      count_22:\n        n_batches: 5\n        exact_f1: 0.013\n        relaxed_f1: 0.185\n        bcs: 0.933\n      count_44:\n        n_batches: 5\n        exact_f1: 0.018\n        relaxed_f1: 0.247\n        bcs: 0.967\n      count_64:\n        n_batches: 5\n        exact_f1: 0.013\n        relaxed_f1: 0.245\n        bcs: 0.973\n    exp2_bcs_controlled:\n      count_6_high_bcs:\n        exact_f1: 0.0354\n        relaxed_f1: 0.211\n        bcs: 0.9447\n      count_6_low_bcs:\n        exact_f1: 0.0068\n        relaxed_f1: 0.089\n        bcs: 0.8709\n      count_12_high_bcs:\n        exact_f1: 0.0151\n        relaxed_f1: 0.1568\n        bcs: 0.9447\n      count_12_low_bcs:\n        exact_f1: 0.0068\n        relaxed_f1: 0.105\n        bcs: 0.9148\n    key_finding: 'MAVEN batch-level: high_bcs relaxed_F1 2.4x vs low_bcs (count_6).\n      Direction same as Few-NERD batch-level (positive). Pairwise + per-type analysis\n      needed to control frequency confound.'\n    note: exact_F1 very low (0.003-0.035), relaxed_F1 usable (0.089-0.247). Event\n      trigger boundary matching is fuzzy. A re-run (500 samples) is still in progress\n      in artifacts/exp004/.\n- exp_id: fewrel_pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    embedding: all-MiniLM-L6-v2\n    n_batches: 15\n    n_predictions: 374\n    count_4:\n      low_bcs_acc: 0.917\n      high_bcs_acc: 0.708\n      delta_pp: -20.9\n      low_bcs: 0.42\n      high_bcs: 0.97\n    count_8:\n      low_bcs_acc: 1\n      high_bcs_acc: 0.5\n      delta_pp: -50\n      low_bcs: 0.47\n      high_bcs: 0.97\n    count_16:\n      low_bcs_acc: 0.917\n      high_bcs_acc: 0.431\n      delta_pp: -48.6\n      low_bcs: 0.57\n      high_bcs: 0.97\n    key_finding: 'BCS-accuracy strong negative: high-BCS batches 43-71% vs low-BCS\n      92-100%. Effect increases with count. Cross-task (NER→RE) replication of confusability\n      hypothesis.'\n- exp_id: exp008_sdgd_zero_fewnerd\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp008_sdgd_zero_fewnerd_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 77.3\n    sdgd_zero:\n      f1: 0.2514\n      precision: 0.2096\n      recall: 0.3141\n      batches: 8\n      time_s: 408.7\n    random_batch:\n      f1: 0.3197\n      precision: 0.2491\n      recall: 0.4462\n      batches: 8\n      time_s: 476.1\n    per_type:\n      f1: 0.2915\n      precision: 0.194\n      recall: 0.5856\n      batches: 66\n      time_s: 2532.2\n    key_finding: All decomposition modes F1 < single_pass. Decomposition boosts recall\n      but kills precision (merge amplification). sdgd_zero worst F1, even below random_batch.\n- exp_id: exp_fewrel_formal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: 16-rel sanity check only\n    exp1:\n      count_1:\n        mean_acc: 0.904\n        n_batches: 16\n      count_4:\n        mean_acc: 0.932\n        n_batches: 5\n      count_8:\n        mean_acc: 0.867\n        n_batches: 5\n      count_16:\n        mean_acc: 0.778\n        n_batches: 5\n        bcs: 0.9\n        zero_variance: true\n    exp2:\n      count_8_low_bcs:\n        acc: 0.889\n        bcs: 0.782\n      count_8_high_bcs:\n        acc: 0.798\n        bcs: 0.892\n      delta_bcs_effect: -0.091\n    trend: 'count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8%\n      (Δ=-9.1pp)'\n- exp_id: exp_fewrel_formal_80rel\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_count_curve:\n      count_1:\n        acc: 0.8573\n        n_batches: 80\n        bcs: 0\n      count_4:\n        acc: 0.8667\n        n_batches: 5\n        bcs: 0.6335\n      count_8:\n        acc: 0.8021\n        n_batches: 5\n        bcs: 0.7175\n      count_16:\n        acc: 0.6958\n        n_batches: 5\n        bcs: 0.795\n      count_32:\n        acc: 0.6578\n        n_batches: 5\n        bcs: 0.8893\n      count_64:\n        acc: 0.5424\n        n_batches: 5\n        bcs: 0.9434\n      count_80:\n        acc: 0.5042\n        n_batches: 5\n        bcs: 0.9706\n    exp2_bcs_controlled:\n      count_8:\n        low_bcs_acc: 0.8229\n        low_bcs: 0.4715\n        high_bcs_acc: 0.5104\n        high_bcs: 0.9706\n        random_acc: 0.8025\n        delta_pp: -31.2\n      count_16:\n        low_bcs_acc: 0.8281\n        low_bcs: 0.5705\n        high_bcs_acc: 0.5156\n        high_bcs: 0.9706\n        random_acc: 0.7169\n        delta_pp: -31.2\n    vs_16rel:\n      degradation_16rel: -12.6pp (0.904→0.778)\n      degradation_80rel: -35.3pp (0.857→0.504)\n      bcs_effect_16rel: -9.1pp\n      bcs_effect_80rel: -31.2pp\n      amplification: 3.4x\n    key_finding: 80-rel count curve 0.857→0.504 (degradation 35.3pp, 远强于 16-rel 12.6pp).\n      BCS effect -31.2pp (3.4x amplification vs 16-rel). 更多 relations → 更大 confusion\n      space → 更强 degradation + BCS effect.\n- exp_id: exp008_sdgd_v2_fewnerd\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 79\n    random_batch:\n      f1: 0.3007\n      precision: 0.3307\n      recall: 0.2758\n      batches: 8\n      time_s: 494\n    sdgd_zero:\n      f1: 0.2407\n      precision: 0.3244\n      recall: 0.1913\n      batches: 4\n      time_s: 261\n    per_type: killed before completion (3/4 modes done, Director approved kill)\n    vs_v1: confidence-gated merge did not improve over union merge. sdgd_zero 0.241\n      vs v1 0.251, random_batch 0.301 vs v1 0.320\n    key_finding: SDGD v2 confidence-gated merge + min_batch_size=8 failed to beat\n      single_pass baseline (F1=0.445). Both v1 and v2 confirm decomposition hurts\n      precision more than it helps recall. Claim 3 (SDGD framework) needs fundamental\n      rethink.\n- exp_id: exp012_llama_fewnerd\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp007_error_taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_random:\n      bcs_zero:\n        n_fp: 6172\n        intra_sub_pct: 0\n        extra_sub_pct: 90.3\n        intra_sub_per_100_gold: 0\n      bcs_low:\n        n_fp: 2231\n        intra_sub_pct: 1.6\n        extra_sub_pct: 89.9\n        intra_sub_per_100_gold: 3.4\n      bcs_medium:\n        n_fp: 3843\n        intra_sub_pct: 10.6\n        extra_sub_pct: 78.1\n        intra_sub_per_100_gold: 6.47\n      bcs_high:\n        n_fp: 6188\n        intra_sub_pct: 49.4\n        extra_sub_pct: 30.8\n        intra_sub_per_100_gold: 12.93\n    correlation:\n      intra_sub_vs_bcs_spearman_rho: 1\n      intra_sub_vs_bcs_p: <0.001\n      chi_square: 6952\n      chi_square_p: ~0\n    exp2_controlled:\n      trend: IntraSub 3.2% -> 7.3% -> 8.6% (rho=1.0, p<0.001)\n    key_finding: 'BCS>=0.95: 49.4% FP are intra-batch type confusion (13/100 gold).\n      Hallucination+boundary <3%. LLM main error mode is type confusion, not hallucination.'\n- exp_id: exp012_llama_fewnerd_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp016_fewrel_error_taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    error_distribution:\n      zero_bcs:\n        bcs_mean: 0\n        correct_pct: 85.73\n        wrong_type_pct: 0\n        intra_sub_pct: 0\n        missed_pct: 14.27\n      low_bcs:\n        bcs_mean: 0.565\n        correct_pct: 85.42\n        wrong_type_pct: 4.17\n        intra_sub_pct: 4.17\n        missed_pct: 10.42\n      medium_bcs:\n        bcs_mean: 0.729\n        correct_pct: 75.7\n        wrong_type_pct: 13\n        intra_sub_pct: 13\n        missed_pct: 11.3\n      high_bcs:\n        bcs_mean: 0.86\n        correct_pct: 66.67\n        wrong_type_pct: 20.28\n        intra_sub_pct: 20.28\n        missed_pct: 13.05\n      very_high_bcs:\n        bcs_mean: 0.971\n        correct_pct: 52.03\n        wrong_type_pct: 32.25\n        intra_sub_pct: 32.25\n        missed_pct: 15.71\n    correlations:\n      intra_sub_vs_bcs_spearman: 0.9539\n      intra_sub_vs_bcs_p: <1e-6\n      accuracy_vs_bcs_spearman: -0.5821\n      accuracy_vs_bcs_p: <1e-6\n    cross_task:\n      ner_intra_sub_vs_bcs_rho: 1\n      re_intra_sub_vs_bcs_rho: 0.9539\n    key_finding: 100% of type confusion in RE is intra-batch (model only predicts\n      from schema). IntraSub vs BCS ρ=0.954 confirms NER finding. Missed rate flat\n      (10-16%), BCS drives confusion not detection failure.\n- exp_id: bootstrap_ci_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fewnerd_pairwise_r:\n      point: 0.112\n      ci_lower: 0.076\n      ci_upper: 0.156\n      n: 1953\n      note: point estimate 0.112 vs old 0.156 — re-run confirmed current value\n    maven_minilm_pairwise_r:\n      point: 0.129\n      ci_lower: 0.104\n      ci_upper: 0.156\n      n: 11026\n    fewrel_count8_delta_pp:\n      point: 31.2\n      ci_lower: 17.7\n      ci_upper: 42.7\n      n: 96+96\n    fewrel_count16_delta_pp:\n      point: 31.2\n      ci_lower: 22.9\n      ci_upper: 39.6\n      n: 192+192\n    fewnerd_pertype_rho:\n      point: -0.293\n      ci_lower: -0.492\n      ci_upper: -0.054\n      n: 63\n    confusion_ratio_count6:\n      point: 25.3\n      ci_lower: 6.1\n      ci_upper: 60.5\n    confusion_ratio_count12:\n      point: 21.2\n      ci_lower: 5.3\n      ci_upper: 52.2\n    key_finding: All CIs exclude null (0 for correlations, 1 for ratios). All effects\n      are directionally robust at 95% level.\n- exp_id: exp015_scs_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    all_pairs:\n      n: 1953\n      n_nonzero: 216\n      qwen3_spearman: 0.1682\n      qwen3_spearman_p: '7.3e-14'\n      qwen3_kendall: 0.1351\n      minilm_spearman: 0.1439\n      minilm_spearman_p: '1.7e-10'\n      minilm_kendall: 0.1152\n    nonzero_only:\n      n: 216\n      qwen3_spearman: 0.2722\n      qwen3_spearman_p: '5.0e-05'\n      qwen3_kendall: 0.2001\n      minilm_spearman: 0.306\n      minilm_spearman_p: '4.6e-06'\n      minilm_kendall: 0.2276\n    key_finding: Both embeddings significantly predict confusion (all p<1e-5). Qwen3\n      better overall (rho=0.168), MiniLM better on nonzero pairs (rho=0.306). SCS\n      is a valid but partial proxy — context, frequency, mention ambiguity also matter.\n- exp_id: exp012_llama_fewnerd_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_8b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_fewrel_40rel\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_awq\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp012_llama_fewnerd_r4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_8b_fewnerd\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_fewrel_40rel_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_fewrel_40rel_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_8b_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_llama_recall_count1: 0.702\n    exp1_llama_recall_count64: 0.273\n    exp1_recall_decline_pp: -42.9\n    exp1_per_batch_recall_corr_vs_qwen: 0.7249\n    exp1_llama_text_match_f1_range: 0.06-0.36\n    exp1_exact_f1: 0\n    exp1_note: exact/relaxed F1=0 due to missing char offsets, text_match is correct\n      metric\n- exp_id: exp012_llama_8b_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006_interaction_2x2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    cell_means_f1:\n      low_count_low_bcs: 0.324\n      low_count_high_bcs: 0.313\n      high_count_low_bcs: 0.325\n      high_count_high_bcs: 0.277\n    main_effects:\n      count: -0.018\n      bcs: -0.029\n    interaction:\n      estimate: -0.036\n      z: -0.667\n      p: 0.505\n      bcs_effect_at_low_count: -0.011\n      bcs_effect_at_high_count: -0.048\n    verdict: 交互方向符合 multiplicative 假设但统计不显著 (p=0.505)，未检测到显著交互效应\n- exp_id: exp012_llama_8b_r2_exp2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_fewrel_40rel_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_acc_count1: 0.858\n    exp1_acc_count4: 0.867\n    exp1_acc_count8: 0.802\n    exp1_acc_count16: 0.697\n    exp1_acc_count32: 0.658\n    exp1_acc_count40: 0.588\n    exp1_decline_pp: -27\n    exp2_bcs_delta_count8: 0.333\n    exp2_bcs_delta_count16: 0.318\n    exp2_low_bcs_acc_count8: 0.833\n    exp2_high_bcs_acc_count8: 0.5\n    exp2_low_bcs_acc_count16: 0.818\n    exp2_high_bcs_acc_count16: 0.5\n- exp_id: exp012_llama_fewrel_ch2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp2_bcs_controlled:\n      count_8:\n        low_bcs_acc: 0.7812\n        high_bcs_acc: 0.5104\n        delta_pp: -27.1\n      count_16:\n        low_bcs_acc: 0.7552\n        high_bcs_acc: 0.5156\n        delta_pp: -24\n    overall_correlation:\n      n_batches: 54\n      pearson_r: -0.39\n      pearson_p: 0.004\n      spearman_rho: -0.43\n      spearman_p: 0.001\n    cross_model_comparison:\n      llama_delta_pp: -27.1\n      qwen3_delta_pp: -31.2\n      ratio: 0.87\n      note: LLaMA effect = 87% of Qwen3, direction and magnitude consistent\n    no_floor_effect: true\n    mean_accuracy: 0.77\n    accuracy_range: 0.41-0.98\n    key_finding: 'BCS confusability effect cross-model replicated: LLaMA Δ=-27.1pp\n      (87% of Qwen3 -31.2pp). Pearson r=-0.39 (p=0.004), Spearman ρ=-0.43 (p=0.001).\n      No floor effect.'\n- exp_id: exp_fewrel_16rel_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_batches: 100\n    pool_size: 16\n    batch_size: 8\n    bcs_range:\n    - 0.6532\n    - 0.9002\n    quartile_delta:\n      Q4_minus_Q1_pp: -5.31\n      ci_95_lower: -9.45\n      ci_95_upper: -4.49\n      note: CI values from pre-D038 bootstrap, may need re-verification with MEAN-based\n        BCS\n    pearson_r_bcs_acc: -0.467\n    regression_slope:\n      slope: -0.509\n      ci_95_lower: -0.556\n      ci_95_upper: -0.349\n      r_squared: 0.218\n      p_value: 1.01e-12\n      interpretation: per +0.1 BCS → -5.09pp accuracy\n      note: CI from pre-D038 bootstrap\n    amplification_ratio:\n      quartile_16_vs_80: 4.2\n      ci_95_lower: 3.3\n      ci_95_upper: 6.95\n    key_finding: '16-rel pool BCS effect (MEAN-based, D038): Δ(Q4-Q1)=-5.31pp, r=-0.467.\n      Regression slope=-0.509. Bootstrap 1000 resamples. [D038 MEAN correction applied,\n      old values: r=-0.637/Δ=-7.42pp/slope=-0.449]'\n- exp_id: exp_fewrel_16rel_100batch\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_fewrel_80pool_16sub_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_batches: 100\n    pool_size: 80-rel pool, 16-type subsamples\n    batch_size: 8\n    mean_accuracy: 0.8077\n    mean_bcs: 0.557\n    bcs_range:\n    - 0.4578\n    - 0.6836\n    quartile_delta:\n      Q4_minus_Q1_pp: -3.92\n      ci_95_lower: -7.79\n      ci_95_upper: 0.42\n    pearson_r_bcs_acc: -0.221\n    pearson_p: 0.027\n    regression_slope:\n      slope: -0.401\n      ci_95_lower: -0.684\n      ci_95_upper: -0.062\n      interpretation: per +0.1 BCS → -4.01pp accuracy\n    key_finding: '80-pool 16-sub BCS effect directional: Δ(Q4-Q1)=-3.92pp CI crosses\n      zero [-7.79,+0.42], but regression slope=-0.401 CI[-0.684,-0.062] excludes zero.\n      Effect weaker than independent 16-rel pool (Δ=-7.42pp) due to narrower BCS range.'\n- exp_id: exp_maven_residualized_bcs\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    minilm:\n      raw_rho: 0.208\n      raw_p: 0.011\n      confound: log_freq\n      bcs_confound_r: 0.201\n      partial_r: 0.133\n      partial_p: 0.107\n    qwen3:\n      raw_rho: 0.184\n      raw_p: 0.025\n      confound: degree_centrality_0.7\n      bcs_confound_r: 0.854\n      partial_r: 0.063\n      partial_p: 0.442\n    joint_control:\n      qwen3_p: 0.439\n      minilm_p: 0.226\n      note: Both n.s. after controlling log_freq + degree jointly\n    key_finding: MAVEN BCS-F1 positive correlation is centrality artifact. MiniLM\n      confound=frequency, Qwen3 confound=degree centrality (r=0.854). After joint\n      control, both correlations vanish. Confirms pairwise SCS remains valid but per-type\n      aggregation fails on homogeneous schemas.\n- exp_id: exp_fewrel_v2_bcs_controlled\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_bcs_mean_acc: 0.8042\n    high_bcs_mean_acc: 0.725\n    delta_low_minus_high_pp: 7.92\n    bootstrap_ci_95_lower_pp: -5.21\n    bootstrap_ci_95_upper_pp: 21.46\n    n_bootstrap: 10000\n    n_batches_per_group: 5\n    samples_per_batch: 96\n    total_inferences: 960\n- exp_id: exp_docred_confusability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_relation_types: 96\n    n_eval_samples: 1240\n    total_inferences: 13618\n    count_curve:\n      count_1: 0.88\n      count_4: 0.77\n      count_8: 0.774\n      count_16: 0.524\n      count_32: 0.521\n      count_64: 0.424\n      count_96: 0.387\n    bcs_effect_count16:\n      low_bcs_acc: 0.679\n      high_bcs_acc: 0.447\n      gap: 0.233\n      spearman_r: -0.661\n      slope: -0.713\n      slope_95ci:\n      - -0.909\n      - -0.529\n    bcs_effect_count32:\n      low_bcs_acc: 0.578\n      high_bcs_acc: 0.403\n      gap: 0.176\n      spearman_r: -0.509\n      slope: -0.69\n      slope_95ci:\n      - -0.854\n      - -0.519\n- exp_id: bcs_max_to_mean_fix\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: exp_confusability_batch_composition\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_fewrel_v2_n25\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    n_low: 25\n    n_high: 25\n    low_bcs_mean_acc: 0.8521\n    high_bcs_mean_acc: 0.5967\n    delta_pp: 25.54\n    ci_95:\n    - 22.42\n    - 28.62\n    permutation_p: 0\n    pearson_r: -0.919\n    low_bcs_range:\n    - 0.356\n    - 0.367\n    high_bcs_range:\n    - 0.791\n    - 0.811\n    key_finding: v2 prompt does NOT eliminate confusability effect. At n=25 with wider\n      BCS separation, effect is massive (25.5pp) and highly significant. Prior n=5\n      result (7.9pp, CI crosses zero) was underpowered + narrow BCS contrast.\n- exp_id: exp_cross_embedding_sensitivity\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    fewnerd_qwen3:\n      pearson_r: 0.138\n      pearson_p: 1.0e-09\n      spearman_rho: 0.168\n      spearman_p: 7.3e-14\n    fewnerd_minilm:\n      pearson_r: 0.172\n      pearson_p: 2.0e-14\n      spearman_rho: 0.144\n      spearman_p: 1.7e-10\n    fewrel_minilm:\n      slope: -0.485\n      r: -0.398\n      p: 0.04\n    fewrel_qwen3:\n      slope: -0.542\n      r: -0.185\n      p: 0.356\n      note: BCS range compression (std=0.034 vs MiniLM 0.081), directional but n.s.\n    key_finding: SCS-confusion signal robust to embedding choice (both significant\n      on Few-NERD). MiniLM better for BCS due to designed-for-similarity. Qwen3 causal-LM\n      embeddings compress BCS range.\n- exp_id: exp017_gpt4o_mini_fewrel\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T07:50:05.454Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T07:50:05.454Z",
  "sessionId": "0e6c27b0-7db8-410b-bb6a-2c3b60a3775b"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T07:50:05.479Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：核心假设不被 reviewers 接受为充分验证，论文被拒，需要找新 angle 重新 reframe 后重投同一 venue
核心假设：['A1 不被接受: 多位 reviewer 认为 r=0.11-0.13 太小，FewRel 的大效应被归因于 extreme batch design（非自然条件）', "A2 部分成立但被矮化: Error taxonomy 被视为'描述性工作'而非贡献", 'A3 被质疑: 3.4× amplification 来自 16-rel vs 80-rel 对比，reviewer 指出这混淆了 count 和 confusability 的 scaling', 'A4 失败: LLaMA NER 多次崩溃 + 仅 FewRel 一个任务复现被判定为不充分', 'A5 被拒绝: MAVEN per-type 正方向被视为反证，centrality confound 解释被认为是 post-hoc rationalization', "A6 被拒绝: '没有可用方法的分析论文不适合 EMNLP Main/Findings'", 'A7 失败: 多位 reviewer 认为贡献不足以构成独立论文']
关键指标范围：{'arr_avg_score': [2.0, 3.0], 'claims_fully_supported': [0, 1], 'major_reviewer_weaknesses': [4, 6], 'cross_task_significant_replications': [1, 2], 'multi_model_effect_consistency': [0.5, 0.7], 'venue_probability_main': [0.0, 0.1], 'venue_probability_findings_or_above': [0.05, 0.25], 'rebuttal_flip_probability': [0.05, 0.25]}
叙事方向：放弃 "confusability predicts degradation" 作为标题级 claim。Reframe 为 "Characterizing and Diagnosing Schema-Induced Failure Modes in Training-Free LLM IE"。 核心叙事转向: (1) 提出 multi-channel degradation 作为诊断框架（不是预测模型）， error taxonomy 成为主要贡献; (2) 将 pairwise correlation 作为 channel 2 存在性的 supporting evidence 而非独立 claim; (3) SDGD 失败 + MAVEN centrality confound 合并为 "schema decomposition 比想象中更难" 的系统性分析; (4) 新增 prescriptive 贡献: 基于所有实验（包括负面结果）给出 schema 设计决策树。需要补充的实验: (a) 至少一个非 extreme-batch 的自然条件下的 BCS 效应验证, (b) 第二个模型在 NER 或 ED 上的成功复现（考虑换 Mistral 或 Gemma 而非继续 LLaMA）, (c) 将 SDGD-cal（empirical confusion matrix）跑通作为 proof-of-concept。 目标仍是 EMNLP 2026（下一个 ARR cycle, September），不降级 venue。

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
  "promptId": "7227d3cb-e413-4f1a-8265-e84bfbf9650c",
  "type": "user",
  "uuid": "b45bde4b-a170-4bb2-b57b-46d841b61053",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "0e6c27b0-7db8-410b-bb6a-2c3b60a3775b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T07:50:05.477Z_

```json
{
  "parentUuid": "b45bde4b-a170-4bb2-b57b-46d841b61053",
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
  "uuid": "9f2d56aa-95b8-421c-a82c-5c9455a2b92d",
  "timestamp": "2026-05-16T07:50:05.477Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "0e6c27b0-7db8-410b-bb6a-2c3b60a3775b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T07:50:05.477Z_

```json
{
  "parentUuid": "9f2d56aa-95b8-421c-a82c-5c9455a2b92d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "569cfdb0-6674-4303-a680-1ed2aa03c268",
  "timestamp": "2026-05-16T07:50:05.477Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "0e6c27b0-7db8-410b-bb6a-2c3b60a3775b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：核心假设不被 reviewers 接受为充分验证，论文被拒，需要找新 angle 重新 reframe 后重投同一 venue 核心假设：['A1 不被接受: 多位 reviewer 认为 r=0.11-0.13 太小，FewRel 的大效应被归因于 extreme batch design（非自然条件）'…",
  "leafUuid": "569cfdb0-6674-4303-a680-1ed2aa03c268",
  "sessionId": "0e6c27b0-7db8-410b-bb6a-2c3b60a3775b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe confusability study with prescriptive schema design framework",
  "sessionId": "0e6c27b0-7db8-410b-bb6a-2c3b60a3775b"
}
```

---

### Assistant

_source line 8 · 2026-05-16T07:51:13.597Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predictions for each "planned" experiment in the experiment_plan, under the "worst" tier scenario. Let me identify all planned experiments:

1. **exp-005** - DocRED confusability study (96 relation types)
2. **exp-006** - Interaction effect 2x2 — Wait, this is already DONE with conclusion "negative". Let me re-check...
3. **exp-007** - Error taxonomy — already DONE
4. **exp-009** - SDGD-zero on MAVEN


5. **exp-010** - SDGD-cal on Few-NERD
6. **exp-011** - SDGD-cal on MAVEN
7. **exp-013** - Ablation: random batching
8. **exp-014** - Ablation: per-type splitting

Let me verify which ones actually have `status: planned` in the experiment plan rather than relying on my initial scan.

Looking at the registry entries, I'm noticing a discrepancy — several experiments marked as planned in the plan file show completion status in the registry. For instance, exp-006 shows as planned but the registry has it marked done with a negative conclusion, and exp-007 appears planned but is actually completed successfully. Same with exp-015. I should follow the experiment_plan status field since that's what the user specifically asked me to work from, but this inconsistency is worth noting as I proceed. I'm identifying which experiments are truly still planned versus already completed in the registry. The ones with `status: planned` in the experiment_plan are exp-005, exp-009, exp-010, exp-011, exp-013, and exp-014, though exp-006, exp-007, and exp-015 also show as planned despite being marked done in the registry. I'll go with the literal `status: planned` entries and generate worst-case predictions for all of them. Under the worst tier scenario, the core assumptions wouldn't be accepted by reviewers, which will shape how I frame these predictions.

For the worst-case narrative, I'm reframing the work as "Characterizing and Diagnosing Schema-Induced Failure Modes in Training-Free LLM IE" where the error taxonomy becomes the main contribution, with pairwise correlation as supporting evidence and SDGD failure analysis showing that schema decomposition is harder than expected. The experiments would need to demonstrate specific failure patterns and provide a prescriptive schema design decision tree to make this framing work.

Looking at what would actually constitute evidence for this worst-case tier, I need weak or non-significant results on new datasets, SDGD-cal also failing, multi-model replication not working well, and effects that are present but easily dismissed. Now I'm checking the experiment registry and noticing that the DocRED confusability study appears to have already been completed under a different ID, though the experiment plan still lists it as planned—I need to reconcile what's actually been run versus what's documented.

After cross-referencing the registry, I can see that exp-005, exp-006, exp-007, and exp-015 have corresponding completed entries, while exp-009, exp-010, exp-011, exp-013, and exp-014 are the ones that are genuinely still planned and need worst-case predictions.

The user is asking me to expand on all experiments marked as planned in the experiment plan, so I should cover all of them and note where they've actually been completed. For the worst-case scenario analysis, I'm thinking through what would happen if these experiments ran under adverse conditions. Starting with exp-005 on DocRED: since it involves document-level relation extraction with longer contexts, the model would likely struggle with maintaining coherence across the document, making the confusability effect harder to detect cleanly due to the added complexity of multi-hop reasoning and coreference resolution.

But I'm realizing DocRED is already in the registry showing strong results, so under a worst-case interpretation, reviewers would dismiss it as just another artifact of the experimental design rather than a genuine finding. I need to clarify what the user actually wants here — are they asking me to predict what the results would look like if run under worst conditions, or how reviewers would interpret existing results? Looking back at the worst tier definition, it seems like the core hypothesis wouldn't be accepted as sufficiently validated, leading to rejection and the need to reframe the work before resubmitting.

Given those seven key assumptions about what would fail or be dismissed in the worst case, I'm now thinking through how each planned experiment would actually perform or be perceived under that scenario.

For DocRED, the results would likely show some effect but the document-level reasoning introduces confounds that make the findings less convincing—the count effect might appear but the BCS effect would be weak or muddled. The 2x2 interaction test would probably fail to reach significance, leaving me unable to distinguish whether the effects are additive or multiplicative, which undermines the independent channels argument. The error taxonomy analysis would show the pattern exists but reviewers would dismiss it as merely descriptive work rather than a real contribution, even if IntraSub errors do increase with BCS. On MAVEN with zero-shot SDGD, the approach would fail even worse than Few-NERD given the 168 types and resulting merge amplification. And calibration data on Few-NERD would provide minimal help—the method still can't outperform a single-pass baseline.

With MAVEN's calibration approach, the problem gets worse because 168 types means the confusion matrix becomes extremely sparse with only 5-10 examples per type. Random batching performs just as well as confusability-aware grouping, suggesting that the decomposition strategy itself doesn't matter much. Per-type splitting achieves the best recall but tanks precision from losing cross-type context, and the latency cost of 66-168 API calls makes it impractical. The SCS validation shows only weak correlation—reviewers would point out that 0.17-0.31 correlation means it explains less than 10% of the actual confusion variance.

Now I need to map these results against what the worst-tier evaluation requires: a natural-condition BCS effect validation, successful reproduction on a second model, and a working proof-of-concept with SDGD-cal. The evidence shows the BCS effect is weak under natural conditions, the second model (Mistral/Gemma) has similar issues, and while SDGD-cal runs, it doesn't actually beat the baseline.

Structuring this as a YAML prediction...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "569cfdb0-6674-4303-a680-1ed2aa03c268",
  "isSidechain": false,
  "requestId": "req_011Cb5t6vGrG3TRj9MXJRp6e",
  "type": "assistant",
  "uuid": "2308f0e7-45ae-4db1-a517-535f847bfed5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "0e6c27b0-7db8-410b-bb6a-2c3b60a3775b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018jsics2x5QcLRKdA8qZ1Zw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26647,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12360,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26647
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

_source line 9 · 2026-05-16T07:54:20.197Z_

```yaml
tier: worst
narrative_guidance: >
  放弃 "confusability predicts degradation" 作为标题级 claim。Reframe 为 
  "Characterizing and Diagnosing Schema-Induced Failure Modes in Training-Free LLM IE"。
  核心叙事转向: (1) multi-channel degradation 作为诊断框架（不是预测模型），error taxonomy 成为主要贡献;
  (2) pairwise correlation 作为 channel 2 存在性的 supporting evidence 而非独立 claim;
  (3) SDGD 失败 + MAVEN centrality confound 合并为 "schema decomposition 比想象中更难" 的系统性分析;
  (4) 新增 prescriptive 贡献: 基于所有实验（包括负面结果）给出 schema 设计决策树。
  补充实验均未达到 reviewers 预期的验证标准：自然条件 BCS 效应弱且不稳健，第二模型 NER 复现再次失败，
  SDGD-cal 仅勉强跑通但无性能优势。

imagined_experiments:
  - name: "DocRED Confusability Study"
    plan_id: "exp-005"
    description: >
      Count curve + BCS correlation on DocRED (96 relation types). 
      Document-level RE, long-context, multi-hop reasoning required.
    expected_results:
      count_curve_acc_count1: 0.82
      count_curve_acc_count16: 0.48
      count_curve_acc_count96: 0.31
      bcs_effect_count16_delta_pp: -8.3
      bcs_effect_count16_ci_lower: -16.1
      bcs_effect_count16_ci_upper: 0.5
      pearson_r_bcs_acc_count16: -0.22
      pearson_p: 0.14
      spearman_rho: -0.19
      spearman_p: 0.21
      n_batches_per_condition: 5
    result_rationale: >
      DocRED 是 document-level RE，每个文档包含多个实体对和多跳推理。模型 degradation 的主要驱动力
      是 long-context attention dilution 和 cross-sentence reasoning failure，而非 type confusion。
      Count curve 存在但主因是 prompt 长度限制而非 confusability。BCS effect 方向正确但 CI 跨零，
      因为：(1) DocRED 96 个 relation type 分布极其不均（top-10 占 60%+ mentions），低频 type 本身
      accuracy 就不稳定；(2) document-level 的 entity pair 定位错误（wrong entity pair）远多于
      type confusion，diluting BCS signal；(3) n=5 batches per condition 带来高方差。
      Reviewers 会指出这与 FewRel 不同——FewRel 是 sentence-level 单 triple 分类，DocRED 是
      document-level multi-triple extraction，任务复杂度差异使得直接比较不 valid。
    tables:
      - name: "Table: DocRED Count Curve"
        columns: [count, accuracy, bcs_mean, n_batches]
        rows:
          - [1, 0.82, 0.0, 96]
          - [4, 0.74, 0.52, 5]
          - [8, 0.63, 0.64, 5]
          - [16, 0.48, 0.73, 5]
          - [32, 0.41, 0.82, 5]
          - [64, 0.35, 0.91, 5]
          - [96, 0.31, 0.95, 5]
      - name: "Table: DocRED BCS-Controlled (count=16)"
        columns: [condition, accuracy, bcs_mean, n_batches]
        rows:
          - [low_bcs, 0.52, 0.58, 5]
          - [high_bcs, 0.44, 0.92, 5]
          - [random, 0.48, 0.73, 5]
    figures_description:
      - "Scatter: BCS vs accuracy at count=16, 5 batches per condition, no clear trend visible with n=5"
      - "Count curve: monotonic decline but steeper than FewRel due to document complexity confound"
    analysis: >
      Count curve 存在 (0.82→0.31) 但无法分离 count effect 和 prompt-length effect（DocRED 
      documents 平均 8 sentences，16 types × entity pair descriptions 已接近 context window 压力）。
      BCS effect 方向正确但 n=5 导致 CI 跨零 ([-16.1, +0.5]pp)，reviewer 判定为 inconclusive。
      与 FewRel sentence-level 的 -31.2pp 形成鲜明对比——reviewer 会论证 FewRel 大效应是
      因为 extreme batch design（top/bottom 5% BCS）在句子级分类任务上人为放大了差异，
      而 DocRED 更接近 "自然条件" 恰恰显示效应微弱。这直接支持 A1 ("FewRel 大效应归因于 extreme batch design")。

  - name: "Interaction Effect 2×2"
    plan_id: "exp-006"
    description: >
      {low count, high count} × {low BCS, high BCS} on Few-NERD.
      Tests additive vs multiplicative interaction between count and confusability.
    expected_results:
      low_count_low_bcs_f1: 0.33
      low_count_high_bcs_f1: 0.31
      high_count_low_bcs_f1: 0.32
      high_count_high_bcs_f1: 0.28
      interaction_z: -0.67
      interaction_p: 0.50
      main_effect_count_pp: -1.8
      main_effect_bcs_pp: -2.9
      bcs_effect_at_low_count: -2.0
      bcs_effect_at_high_count: -4.0
    result_rationale: >
      2×2 设计中 Few-NERD 的 BCS range 受限（random batches BCS 集中在 0.79-0.87），
      导致 low/high BCS 对比不够极端。交互效应方向符合 multiplicative 假设（high count 时 BCS 
      effect 更大）但统计功效不足（p=0.50）。原因：(1) Few-NERD 66 types 中 random sampling 
      难以构造 BCS 真正 low 的 batch（类型普遍高度相似）；(2) count 的两个水平（6 vs 12）
      差异不够大，真正的 multiplicative 效应需要更大的 count span；(3) 每个 cell 仅 ~13 batches，
      检验 interaction 需要更大 n。Reviewer 会说 "声称 orthogonal channels 但无法检测到 
      interaction，说明所谓的 multi-channel model 缺乏统计支持"。
    tables:
      - name: "Table: 2×2 ANOVA Cell Means (F1)"
        columns: [condition, low_bcs, high_bcs, marginal]
        rows:
          - [low_count (6), 0.33, 0.31, 0.32]
          - [high_count (12), 0.32, 0.28, 0.30]
          - [marginal, 0.325, 0.295, "-"]
    figures_description:
      - "Interaction plot: two nearly parallel lines (low/high count), slight divergence at high BCS but well within error bars"
    analysis: >
      交互项 p=0.50 意味着无法区分 additive 和 multiplicative model。这对 "orthogonal channels" 
      claim 是双面的——orthogonality 可以解释为 additive（不交互），但 reviewer 会问 "如果真是
      independent channels，为什么在 FewRel 上 count 和 BCS 如此共线（80-rel 中 BCS 从 0.63 
      涨到 0.97）？" 无法给出 clean separation evidence 削弱了 Claim 2 的核心论证。

  - name: "Error Taxonomy (BCS-binned)"
    plan_id: "exp-007"
    description: >
      Systematic FP classification (intra_sub / extra_sub / boundary / hallucination) 
      across BCS bins. Mechanistic evidence for multi-channel model.
    expected_results:
      bcs_zero_intra_sub_pct: 0.0
      bcs_low_intra_sub_pct: 1.6
      bcs_medium_intra_sub_pct: 10.6
      bcs_high_intra_sub_pct: 49.4
      intra_sub_vs_bcs_rho: 1.0
      extra_sub_still_dominant_at_medium: true
      hallucination_pct_overall: 2.8
      boundary_error_pct_overall: 0.4
    result_rationale: >
      Error taxonomy 技术上是成功的——IntraSub 与 BCS 完美单调相关 (ρ=1.0)。但在 worst 档，
      reviewer 视角是：(1) "这只是在确认一个 trivially expected 的结果——当你把相似 types 放一起，
      模型当然更容易混淆它们，这不需要实验来证明"；(2) taxonomy 本身（4 类 FP）被视为
      "描述性分类" 而非方法论贡献；(3) 没有 actionable insight——知道 high-BCS 导致 type confusion 
      但 SDGD 无法利用这个 insight 改善性能；(4) BCS binning 的阈值选择（0/low/medium/high）
      被质疑为 post-hoc，没有先验理论指导为什么在这些阈值处分割。
      Reviewer 3 会写："The error taxonomy confirms intuitions but does not constitute 
      a methodological contribution. The monotonic trend is expected and does not advance 
      our understanding beyond 'similar things are confused more often.'"
    tables:
      - name: "Table: Error Distribution by BCS Bin (Few-NERD)"
        columns: [bcs_bin, n_fp, intra_sub_pct, extra_sub_pct, boundary_pct, halluc_pct]
        rows:
          - [zero (0.0), 6172, 0.0, 90.3, 0.5, 9.2]
          - [low (0.75-0.85), 2231, 1.6, 89.9, 0.3, 8.2]
          - [medium (0.85-0.95), 3843, 10.6, 78.1, 0.4, 10.9]
          - [high (0.95+), 6188, 49.4, 30.8, 0.6, 19.2]
      - name: "Table: Cross-task IntraSub Correlation"
        columns: [task, rho, p, n_bins]
        rows:
          - [NER (Few-NERD), 1.0, "<0.001", 4]
          - [RE (FewRel 80-rel), 0.954, "<1e-6", 5]
    figures_description:
      - "Stacked bar chart: error type proportions shift from extra_sub-dominated to intra_sub-dominated as BCS increases"
      - "Line plot: IntraSub rate monotonically increasing across BCS bins, both tasks"
    analysis: >
      作为 worst 档的核心问题不是结果本身（结果干净），而是 reviewer 的 framing 评判。
      多位 reviewer 会将此归类为 "analysis paper without actionable contribution"。
      具体批评：(a) "trivially expected result dressed up as finding"，(b) taxonomy 仅 4 类且
      定义直接来自 span matching logic 而非需要创新分类框架，(c) cross-task 一致性被承认但
      "consistency of a trivial finding across tasks does not elevate it to a contribution"。
      在 reframe 后的论文中，error taxonomy 从 "supporting evidence" 升级为 "primary contribution"，
      但 reviewer 仍然需要看到这个 taxonomy 如何指导具体的系统设计决策才会接受。

  - name: "SDGD-zero on MAVEN"
    plan_id: "exp-009"
    description: >
      Confusability-minimizing batch composition via embedding SCS + graph coloring 
      on MAVEN (168 event types). Compare vs single-pass + random batching.
    expected_results:
      single_pass_relaxed_f1: 0.245
      random_batch_relaxed_f1: 0.178
      sdgd_zero_relaxed_f1: 0.152
      per_type_relaxed_f1: 0.135
      single_pass_batches: 1
      sdgd_zero_batches: 12
      random_batch_batches: 12
      per_type_batches: 168
      sdgd_zero_time_s: 980
      merge_amplification_factor: 3.2
    result_rationale: >
      MAVEN 168 types 放大了 Few-NERD 上已观察到的 merge amplification 问题。原因：
      (1) 168 types 的 graph coloring 产生 12+ batches，每个 batch ~14 types，merge 时
      同一 trigger 在多个 batch 中被不同 type 标注，dedup 逻辑无法可靠选择正确 type；
      (2) MAVEN event triggers 本身 boundary 模糊（单词或短语均可），multi-batch extraction 
      产生更多 boundary-inconsistent predictions 需要合并；(3) MAVEN 的 same-domain homogeneous 
      schema 意味着即使 "low-BCS" batch 中 types 仍然相似度较高（mean SCS=0.216, 远高于 
      Few-NERD 跨 domain 的情况），confusability-aware grouping 的边际收益极小；
      (4) Qwen3 在 MAVEN 上 exact_F1 本身极低（0.003-0.035），分解后更差。
      这与 Few-NERD 结果一致：sdgd_zero < random_batch < single_pass。进一步确认
      "naive decomposition fundamentally breaks multi-type extraction" 的结论。
    tables:
      - name: "Table: SDGD-zero vs Baselines (MAVEN, relaxed_F1)"
        columns: [method, relaxed_f1, precision, recall, batches, time_s]
        rows:
          - [single_pass, 0.245, 0.312, 0.201, 1, 85]
          - [random_batch (k=12), 0.178, 0.195, 0.164, 12, 870]
          - [sdgd_zero, 0.152, 0.224, 0.115, 12, 980]
          - [per_type, 0.135, 0.098, 0.218, 168, 12400]
    figures_description:
      - "Bar chart: F1 comparison across 4 methods, single_pass dominates"
      - "Precision-Recall tradeoff scatter: decomposition methods shift toward low-precision high-recall quadrant"
    analysis: >
      MAVEN 上 SDGD-zero 再次败于 single-pass，且败幅更大（-38% relative 对比 Few-NERD 的 -46%）。
      Per-type splitting（类似 UniNER）recall 最高但 precision 崩溃——168 batches 的 merge 
      产生大量 conflicting predictions。Reviewer 会总结："decomposition is strictly harmful 
      across both NER and ED, regardless of whether grouping is random or confusability-aware. 
      The paper identifies a problem (confusability) but offers no working solution."
      这直接触发 A6："没有可用方法的分析论文不适合 EMNLP Main/Findings"。

  - name: "SDGD-cal on Few-NERD"
    plan_id: "exp-010"
    description: >
      Empirical confusability from 5-10 calibration examples (no gradients). 
      Build confusion matrix from calibration, use as edge weights for graph coloring.
    expected_results:
      calibration_samples: 10
      empirical_confusion_matrix_sparsity: 0.94
      sdgd_cal_f1: 0.268
      sdgd_zero_f1: 0.241
      single_pass_f1: 0.445
      random_batch_f1: 0.301
      improvement_over_sdgd_zero_pp: 2.7
      still_below_single_pass: true
      calibration_time_s: 450
      total_time_s: 720
    result_rationale: >
      SDGD-cal 用 empirical confusion 替代 embedding SCS 作为 confusability proxy，
      理论上更准确。但 worst 档下的问题：(1) 10 个 calibration samples 对 66 types 
      产生极度稀疏的 confusion matrix（66×66=4356 cells，10 samples 仅观察到 ~260 个
      非零 cells），大量 type pairs 无观测数据退化为 SCS fallback；(2) calibration 数据
      的 confusion pattern 与 test 数据不一致（不同文本域、不同实体分布），empirical 
      confusion matrix 的 generalization 差；(3) 即使 graph coloring 用了更准确的 weights，
      merge amplification 问题不变——根本瓶颈是 merge strategy 而非 grouping quality；
      (4) 比 sdgd_zero 好 2.7pp 但仍远低于 single_pass（-17.7pp），证明问题不在 
      confusability estimation 而在 decomposition paradigm 本身。
      Reviewer 结论："SDGD-cal demonstrates that better confusability estimation does not 
      address the fundamental merge problem, confirming that schema decomposition is not 
      a viable approach without solving the merge challenge first."
    tables:
      - name: "Table: SDGD-cal vs Baselines (Few-NERD)"
        columns: [method, f1, precision, recall, batches, total_time_s]
        rows:
          - [single_pass, 0.445, 0.563, 0.368, 1, 79]
          - [random_batch (k=8), 0.301, 0.331, 0.276, 8, 494]
          - [sdgd_zero, 0.241, 0.324, 0.191, 4, 261]
          - [sdgd_cal (n=10), 0.268, 0.341, 0.221, 5, 720]
      - name: "Table: Calibration Matrix Properties"
        columns: [metric, value]
        rows:
          - [total_type_pairs, 4356]
          - [observed_nonzero, 263]
          - [sparsity, 0.94]
          - [scs_fallback_pairs, 4093]
          - [cal_vs_scs_rank_agreement, 0.58]
    figures_description:
      - "Heatmap: empirical confusion matrix (very sparse, few bright cells)"
      - "Bar chart: F1 progression from sdgd_zero → sdgd_cal → random → single_pass"
    analysis: >
      SDGD-cal 作为 "proof-of-concept" 勉强跑通了，但其结果恰恰证明了 reviewer 的担忧：
      confusability-aware decomposition 即使使用 ground-truth confusion 信号也无法 beat 
      naive single-pass。这不是 estimation 问题而是 architecture 问题。在 reframe 后的论文中，
      这被定位为 "negative result contributing to understanding: why naive decomposition fails"，
      但 A6 的 reviewer 仍会认为 "identifying that something doesn't work is not a 
      contribution unless you explain WHY at a deeper mechanistic level and propose 
      what WOULD work"。SDGD-cal 的 marginal improvement (+2.7pp over sdgd_zero) 
      被视为 "noise-level improvement that confirms the approach is fundamentally limited"。

  - name: "SDGD-cal on MAVEN"
    plan_id: "exp-011"
    description: >
      Empirical confusability with calibration on 168 event types.
      Full comparison table across all methods on MAVEN.
    expected_results:
      calibration_samples: 10
      confusion_matrix_sparsity: 0.97
      sdgd_cal_relaxed_f1: 0.161
      sdgd_zero_relaxed_f1: 0.152
      single_pass_relaxed_f1: 0.245
      random_batch_relaxed_f1: 0.178
      improvement_over_sdgd_zero_pp: 0.9
      calibration_time_s: 1200
      total_time_s: 2200
    result_rationale: >
      MAVEN 168 types 使 calibration 更加 hopeless：168×168=28224 type pairs，10 samples 
      仅能覆盖 ~840 cells（sparsity 0.97）。绝大多数 type pair 的 confusability 仍然依赖 
      SCS fallback。在 same-domain homogeneous schema 中，SCS 本身区分力弱（Qwen3 pairwise 
      r=-0.007 on MAVEN），所以 fallback 到 SCS 等于 fallback 到 noise。
      Cal 相比 zero 仅提升 0.9pp（noise level），因为：(1) 绝大多数 edges 仍用 SCS；
      (2) 观察到 confusion 的 type pairs 往往是 high-frequency types，低频 types 在 
      calibration 中根本不出现；(3) merge amplification 在 168 types 上比 66 types 更严重
      （更多 batch→更多 conflicting triggers→更低 precision）。
    tables:
      - name: "Table: Full Comparison (MAVEN, relaxed_F1)"
        columns: [method, relaxed_f1, delta_vs_single_pass, time_s, api_calls]
        rows:
          - [single_pass, 0.245, "—", 85, 710]
          - [random_batch (k=12), 0.178, -27.3%, 870, 8520]
          - [sdgd_zero, 0.152, -38.0%, 980, 8520]
          - [sdgd_cal (n=10), 0.161, -34.3%, 2200, 15620]
          - [per_type, 0.135, -44.9%, 12400, 119280]
    figures_description:
      - "Bar chart: all methods below single_pass, progressive degradation with decomposition"
      - "Cost-benefit plot: API calls vs F1, showing decomposition wastes compute"
    analysis: >
      MAVEN 上 SDGD-cal 的 near-zero improvement 彻底关闭了 "calibration rescues decomposition" 
      的叙事。在 worst 档论文中，这被呈现为：schema decomposition 面临 fundamental 
      tradeoff——减少 batch 内 confusability 必然增加 batch 数量→增加 merge conflicts→
      降低 precision。该 tradeoff 在 type 数量大（168）且语义同质的 schema 上尤为严重。
      这是 valuable negative knowledge，但 reviewer 不认为 negative results alone 
      构成足够的 contribution for EMNLP Main。

  - name: "Ablation: Random Batching"
    plan_id: "exp-013"
    description: >
      Same batch count k as SDGD, random composition.
      Isolates confusability-aware grouping from batch count reduction.
    expected_results:
      random_k4_f1: 0.312
      sdgd_zero_k4_f1: 0.241
      random_k8_f1: 0.301
      sdgd_zero_k8_f1: 0.251
      random_better_than_sdgd: true
      p_random_vs_sdgd: 0.03
      single_pass_f1: 0.445
    result_rationale: >
      Random batching consistently outperforms SDGD-zero，这是 worst 档中最致命的发现之一。
      原因分析：SDGD 的 graph coloring 优化 minimum BCS 的同时，产生 unbalanced batch sizes
      （某些 batch 仅 2-3 types，其他 14+ types）。小 batch 的 type coverage 不足导致模型
      "以为" 只有这几个 type 存在→将所有 entities 都分配到少数 types→precision 在小 batch 极低。
      Random batching 产生 balanced sizes，每个 batch ~8 types，模型行为更稳定。
      这直接攻击 Claim 1 的 operationalization："即使 confusability IS a real signal，
      利用它进行 schema decomposition 反而 HURTS 性能"。Reviewer："The confusability signal 
      exists but is not actionable — identifying it does not lead to improvement."
    tables:
      - name: "Table: Random vs SDGD Ablation (Few-NERD)"
        columns: [method, k, f1, precision, recall, mean_batch_size, batch_size_std]
        rows:
          - [single_pass, 1, 0.445, 0.563, 0.368, 66, 0]
          - [random, 4, 0.312, 0.298, 0.327, 16.5, 1.2]
          - [sdgd_zero, 4, 0.241, 0.324, 0.191, 16.5, 8.3]
          - [random, 8, 0.301, 0.331, 0.276, 8.3, 0.9]
          - [sdgd_zero, 8, 0.251, 0.210, 0.314, 8.3, 5.7]
    figures_description:
      - "Paired bar chart: at every k, random > sdgd_zero"
      - "Box plot: batch size distribution — SDGD highly variable, random uniform"
    analysis: >
      Random > SDGD 是 worst 档核心 devastating evidence。它说明 confusability-aware grouping 
      的 benefit（减少 within-batch confusion）被其 cost（unbalanced batches + suboptimal 
      coverage）抵消甚至反转。Reviewer 总结："The authors demonstrate that type confusability 
      correlates with degradation, but their attempt to operationalize this finding 
      (SDGD) performs WORSE than random decomposition. This undermines the practical 
      significance of the entire confusability analysis." 在 reframe 后的叙事中，这被
      解释为 "balanced batch size matters more than BCS minimization for merge quality"，
      但 reviewer 认为这属于 "obvious in hindsight" 且 "should have been anticipated 
      before running SDGD"。

  - name: "Ablation: Per-type Splitting (UniNER-style)"
    plan_id: "exp-014"
    description: >
      1 type per batch (upper bound on decomposition benefit). 
      Reveals latency vs quality tradeoff.
    expected_results:
      per_type_f1: 0.292
      per_type_precision: 0.194
      per_type_recall: 0.586
      single_pass_f1: 0.445
      latency_multiplier: 32x
      api_calls: 4224
      time_s: 2530
      merge_conflict_rate: 0.34
    result_rationale: >
      Per-type splitting 消除了 all type confusion（每个 batch 仅 1 type，无法 confuse），
      验证 Channel 2 的 existence。但 merge amplification 最为严重：(1) 66 batches 中
      同一 text span 被多个 type 独立 "认领"（每个 type 的 prompt 让模型 over-extract 
      属于该 type 的 mentions）；(2) recall 最高 (0.586) 因为 per-type prompt 给模型
      最大的 freedom 去找该 type 的 mentions，但 precision 崩溃 (0.194) 因为 union 
      merge 无法判断哪个 type assignment 正确；(3) 32x latency 使其 impractical。
      Reviewer 视角：(a) "highest recall proves that decomposition CAN recover missed 
      entities"——但对应的 precision 崩溃说明 merge 是 unsolved 的；(b) "without a working 
      merge strategy, per-type splitting is not a viable method, just a diagnostic tool"；
      (c) 32x latency 在 deployment scenarios（作者 cite 的 clinical/regulatory）中
      完全不可接受。
    tables:
      - name: "Table: Decomposition Spectrum (Few-NERD)"
        columns: [method, f1, precision, recall, batches, time_s, latency_vs_single]
        rows:
          - [single_pass (k=1), 0.445, 0.563, 0.368, 1, 79, 1x]
          - [sdgd_zero (k=4), 0.241, 0.324, 0.191, 4, 261, 3.3x]
          - [random (k=8), 0.301, 0.331, 0.276, 8, 494, 6.3x]
          - [sdgd_cal (k=5), 0.268, 0.341, 0.221, 5, 720, 9.1x]
          - [per_type (k=66), 0.292, 0.194, 0.586, 66, 2530, 32x]
    figures_description:
      - "Precision-Recall tradeoff curve: as k increases, recall rises but precision drops faster"
      - "Pareto frontier: single_pass dominates all decomposition methods on F1 vs latency"
    analysis: >
      Per-type 结果确认了一个 paradox：消除 type confusion 提升了 recall 但无法提升 F1，
      因为 merge precision loss > confusion reduction gain。这在 worst 档中被 reviewer 
      解读为：(1) "the confusability problem exists but is dominated by the merge problem"；
      (2) "any decomposition approach (including future work) must first solve merge 
      before confusability-aware grouping becomes relevant"；(3) "the paper's theoretical 
      contribution (confusability → degradation) is correct but currently has zero 
      practical utility"。Pareto 分析显示 single_pass dominates 所有分解方法，
      直接支持 A6 的 critique。

  - name: "SCS Validation (Embedding vs Empirical)"
    plan_id: "exp-015"
    description: >
      Spearman/Kendall rank correlation between embedding SCS and empirical confusion matrix.
      Validates embedding proxy for practical use.
    expected_results:
      all_pairs_qwen3_spearman: 0.168
      all_pairs_qwen3_p: 7.3e-14
      all_pairs_minilm_spearman: 0.144
      all_pairs_minilm_p: 1.7e-10
      nonzero_only_qwen3_spearman: 0.272
      nonzero_only_minilm_spearman: 0.306
      variance_explained_all: 0.028
      variance_explained_nonzero: 0.094
    result_rationale: >
      SCS validation 统计上显著（p<1e-10），但 reviewer 关注的是 effect size 和 practical 
      utility。ρ=0.168 all-pairs 意味着 SCS 仅解释 2.8% 的 confusion variance。即使在 
      nonzero-only subset（已经是 cherry-picked 的最优子集），ρ=0.306 也仅解释 9.4%。
      Reviewer 批评：(1) "SCS is statistically significant due to n=1953 but practically 
      useless as a predictor — R²=3% means 97% of confusion is driven by other factors"；
      (2) "the gap between SCS and empirical confusion (ρ=0.17-0.31) means that 
      SDGD-zero based on SCS is building on a very weak signal"；(3) "nonzero-only 
      analysis is selection on the dependent variable — of course similarity predicts 
      confusion GIVEN that confusion occurred"；(4) 两个 embedding 在不同 conditions 下
      表现不同（Qwen3 better overall, MiniLM better nonzero-only）被视为 "the proxy 
      is not robust, which embedding to use is itself a hyperparameter"。
    tables:
      - name: "Table: SCS → Empirical Confusion Validation"
        columns: [subset, embedding, spearman_rho, p_value, R_squared, n]
        rows:
          - [all pairs, Qwen3, 0.168, 7.3e-14, 0.028, 1953]
          - [all pairs, MiniLM, 0.144, 1.7e-10, 0.021, 1953]
          - [nonzero only, Qwen3, 0.272, 5.0e-5, 0.074, 216]
          - [nonzero only, MiniLM, 0.306, 4.6e-6, 0.094, 216]
    figures_description:
      - "Scatter: SCS vs empirical confusion rate, massive spread with weak linear trend"
      - "Residual plot showing substantial unexplained variance at all SCS levels"
    analysis: >
      SCS validation 是 worst 档中 A1 critique 的具体化。Reviewer 的核心论点：
      "r=0.11-0.13 for SCS→degradation 和 ρ=0.17-0.31 for SCS→confusion 都 too small 
      to be practically meaningful。作者将 'statistically significant' 等同于 'meaningful'，
      但在 n=1953 下，ρ=0.05 都可以 significant。真正的问题是：这个 signal 强到足以 
      support schema design decisions 吗？R²=3% 的 predictor 不能用于 prescriptive guidance。"
      这直接挑战了 reframe 后论文的 "schema design decision tree" 贡献——如果 underlying 
      signal 仅解释 3% variance，任何基于它的 decision tree 都是 unreliable 的。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2308f0e7-45ae-4db1-a517-535f847bfed5",
  "isSidechain": false,
  "requestId": "req_011Cb5t6vGrG3TRj9MXJRp6e",
  "type": "assistant",
  "uuid": "624c68b4-5202-4f28-b1ab-6dc41261b0aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "0e6c27b0-7db8-410b-bb6a-2c3b60a3775b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018jsics2x5QcLRKdA8qZ1Zw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 26647,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12360,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 26647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26647
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：核心假设不被 reviewers 接受为充分验证，论文被拒，需要找新 angle 重新 reframe 后重投同一 venue 核心假设：['A1 不被接受: 多位 reviewer 认为 r=0.11-0.13 太小，FewRel 的大效应被归因于 extreme batch design（非自然条件）'…",
  "leafUuid": "624c68b4-5202-4f28-b1ab-6dc41261b0aa",
  "sessionId": "0e6c27b0-7db8-410b-bb6a-2c3b60a3775b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe confusability study with prescriptive schema design framework",
  "sessionId": "0e6c27b0-7db8-410b-bb6a-2c3b60a3775b"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：核心假设不被 reviewers 接受为充分验证，论文被拒，需要找新 angle 重新 reframe 后重投同一 venue 核心假设：['A1 不被接受: 多位 reviewer 认为 r=0.11-0.13 太小，FewRel 的大效应被归因于 extreme batch design（非自然条件）'…",
  "leafUuid": "624c68b4-5202-4f28-b1ab-6dc41261b0aa",
  "sessionId": "0e6c27b0-7db8-410b-bb6a-2c3b60a3775b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe confusability study with prescriptive schema design framework",
  "sessionId": "0e6c27b0-7db8-410b-bb6a-2c3b60a3775b"
}
```

---
