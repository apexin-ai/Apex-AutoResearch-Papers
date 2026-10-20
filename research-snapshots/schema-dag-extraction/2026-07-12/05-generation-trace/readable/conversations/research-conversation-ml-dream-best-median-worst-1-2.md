# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/e29e0c1a-a118-4d50-b730-11d6e018290b.jsonl`
- **Structured JSON:** [`bbe0d157eb28dddbe73a.json`](../../sessions/bb/bbe0d157eb28dddbe73a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T07:35:40.641Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T07:35:40.641Z",
  "sessionId": "e29e0c1a-a118-4d50-b730-11d6e018290b",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: schema-dag-extraction\n\n## paper_framing.md\n\n# Paper Framing — schema-dag-extraction\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\n- Commitment deadline: August 2, 2026\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\n- Deadline: ARR May 25, 2026 (10 days from today)\n\n## Core Claims (2 claims) — Revised per D019\n\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. The effect amplifies with schema complexity (3.4× between 16-type and 80-type schemas). Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) BCS-controlled accuracy gap on FewRel, (c) >=2 models.\n\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Cross-task validated: NER IntraSub ρ=1.0, RE IntraSub ρ=0.954. Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\n\n~~3. **SDGD Effectiveness**~~ — **DROPPED (D019)**: SDGD-zero v1 F1=0.251, v2 F1=0.241, both far below single-pass baseline 0.445. Merge amplification is an intrinsic challenge of schema decomposition that merge strategies (union+dedup, confidence-gated) cannot resolve. **Discussed as negative result + future work direction** — \"why naive decomposition fails\" is itself a contribution.\n\n## Story Spine — Revised per D012\n\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\n\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\n\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal that amplifies with schema complexity, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We further show that naive confusability-aware decomposition (SDGD) fails due to merge amplification — a structural challenge that points to calibration-based approaches as future work.\n\n- **Three-task validation**:\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.112 [0.076, 0.156] (n=1953), per-type ρ=-0.293 [-0.492, -0.054] (p=0.02), 10-28x confusion ratio\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\n\n- **Headline result template**: \"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.11-0.13, all CIs exclude zero), with 10-28x more type confusion errors in high-confusability batches. The effect amplifies with schema complexity: 3.4× stronger BCS effect on 80-type vs 16-type schemas (Δ=-31.2pp vs -9.1pp). On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid.\"\n\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\n\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\n\nThese channels are orthogonal and independently addressable.\n\n**Pairwise vs Aggregated Confusability**:\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.112 [0.076, 0.156]) and MAVEN (MiniLM, r=0.129 [0.104, 0.156]). SCS validated as effective confusion proxy: Qwen3 ρ=0.168 (p=7e-14), MiniLM ρ=0.306 nonzero-only (p=5e-6).\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\n\n## Evidence Hierarchy (D012)\n\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\n\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\n\n**Few-NERD (NER)** — Qwen3 embeddings:\n- Pearson r=0.112 [0.076, 0.156] (n=1953 type pairs) — corrected via bootstrap recomputation\n- Nonzero-only Spearman ρ=0.272 (p=5e-5)\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\n- Immune to type frequency confound (operates at type-pair level)\n\n**MAVEN (ED)** — MiniLM embeddings:\n- Pearson r=+0.129 [0.104, 0.156] (n=11026 type pairs) — corrected via bootstrap\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\n- Cross-task replication on same-domain schema\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\n\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\n\nLarge effect size, cross-task (RE), scaling with schema complexity:\n\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\n\n**16-rel sanity check** (exp_fewrel_formal):\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\n\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\n\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\n\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\n\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\n\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\n\nMethodological case study on when aggregated confusability measures fail:\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\n- This is stronger than \"domain boundary\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\n\n### Tier 5: MECHANISTIC — Error Taxonomy (Cross-Task)\n\nIntraSub rate monotonically increases with BCS on both NER and RE:\n\n**Few-NERD (NER, exp-007)**: IntraSub 0%→1.6%→10.6%→49.4%, ρ=1.0\n**FewRel 80-rel (RE)**: IntraSub 0%→4.2%→13.0%→20.3%→32.3%, ρ=0.954 (p=0.0, n=154 batches)\n- extra_sub=0 on both tasks — type confusion is purely intra-batch phenomenon\n- Same mechanism, different absolute magnitudes — consistent with cross-task expectations\n\nAdditional from extreme batch design:\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\n\n## Embedding Ablation (D010)\n\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\n\n### Per-type (Layer 2)\n| | Few-NERD | FewRel | MAVEN |\n|---|---|---|---|\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\n\n### Pairwise (Layer 1)\n| | Few-NERD | MAVEN |\n|---|---|---|\n| Qwen3 | r=0.112 [0.076,0.156] ✓ | r=-0.007 ✗ |\n| MiniLM | — | r=+0.129 [0.104,0.156] ✓ |\n\n### SCS→Empirical Confusion Validation (exp-015 fast)\n| | Qwen3 | MiniLM |\n|---|---|---|\n| All pairs ρ | 0.168 (p=7e-14) ✓ | 0.144 (p=2e-10) ✓ |\n| Nonzero-only ρ | 0.272 (p=5e-5) | 0.306 (p=5e-6) ✓ |\n\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \"Lost in the Middle\" (TACL 2024).\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy | Experiment |\n|---------|------------------|------------|\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]\n    on Few-NERD with Qwen3-32B-FP8'\n  priority: P0\n  gpu_budget_hours: 3.5\n  deps: []\n  registry_id: exp001_count_baseline\n  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction\n    at low counts.\n  status: DONE\n  conclusion: success\n  metrics:\n    diagnosis: char offset 96.5% fabricated by model\n    text_match_reeval:\n      count_1:\n        f1: 0.184\n        precision: 0.105\n        recall: 0.72\n        pred_gold_ratio: 6.85\n      count_2:\n        f1: 0.123\n        precision: 0.068\n        recall: 0.698\n        pred_gold_ratio: 10.33\n      count_6:\n        f1: 0.155\n        precision: 0.088\n        recall: 0.62\n        pred_gold_ratio: 7.02\n      count_12:\n        f1: 0.246\n        precision: 0.16\n        recall: 0.539\n        pred_gold_ratio: 3.38\n      count_22:\n        f1: 0.322\n        precision: 0.232\n        recall: 0.527\n        pred_gold_ratio: 2.27\n      count_44:\n        f1: 0.473\n        precision: 0.414\n        recall: 0.551\n        pred_gold_ratio: 1.33\n      count_64:\n        f1: 0.463\n        precision: 0.52\n        recall: 0.418\n        pred_gold_ratio: 0.8\n    key_finding: recall monotonically decreases (0.72→0.42), precision monotonically\n      increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at\n      count_44\n    wrong_type_trend: 'type confusion increases with count: 0→2434, supports confusability\n      hypothesis'\n    spurious_dominant: spurious FPs (text in source but not entity) dominate at low\n      count, not hallucination\n    conclusion_text_match: F1 curve inversion caused by over-prediction confound,\n      NOT absence of confusability effect. Recall curve + type confusion pattern support\n      hypothesis.\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,\n    25 random + extreme batches on Few-NERD'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  registry_id: exp002_confusability_controlled\n  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion\n    rate 10-28x.\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp2_reeval_results.json (text_match, CLEAN)\n    primary_recall_vs_bcs:\n      count_6:\n        r: 0.2754\n        p: 0.1644\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.2219\n        p: 0.266\n        n: 27\n        verdict: FAIL\n      partial:\n        r: 0.2522\n        p: 0.0658\n        n: 54\n        verdict: FAIL\n    secondary_f1_vs_bcs:\n      count_6:\n        r: 0.1754\n        p: 0.3814\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.5012\n        p: 0.0077\n        n: 27\n        verdict: PASS\n      partial:\n        r: 0.3025\n        p: 0.0262\n        n: 54\n        verdict: PASS\n    mechanistic_confusion_rate:\n      random_batches:\n        count_6_high: 0.0157\n        count_6_low: 0.0088\n        ratio_6: 1.7\n        count_12_high: 0.0304\n        count_12_low: 0.0131\n        ratio_12: 2.4\n      extreme_batches:\n        count_6_high: 0.0728\n        count_6_low: 0.0014\n        ratio_6: 27.5\n        count_12_high: 0.048\n        count_12_low: 0.0061\n        ratio_12: 9.9\n      verdict: PASS\n    pairwise_confusion_analysis:\n      all:\n        n_pairs: 1953\n        pearson_r: 0.156\n        pearson_p: 4.6e-12\n        spearman_rho: 0.16\n        spearman_p: 1.3e-12\n      count_6:\n        n_pairs: 1770\n        pearson_r: 0.078\n        pearson_p: 0.001\n      count_12:\n        n_pairs: 1953\n        pearson_r: 0.147\n        pearson_p: 6.7e-11\n      nonzero_only:\n        all_spearman_rho: 0.254\n        all_spearman_p: 1.1e-06\n        count_12_pearson_r: 0.212\n        count_12_p: 0.00034\n      top_confused_pair: person-other <-> person-politician (BCS=0.934, confusion=156)\n    per_type_analysis:\n      n_types: 63\n      filter: freq>=5\n      micro_f1_vs_bcs:\n        pearson_r: -0.1828\n        pearson_p: 0.1516\n        spearman_rho: -0.2927\n        spearman_p: 0.0199\n        partial_r_ctrl_logfreq: -0.1998\n        partial_p: 0.1163\n      mean_f1_vs_bcs:\n        pearson_r: -0.1374\n        pearson_p: 0.283\n        spearman_rho: -0.2412\n        spearman_p: 0.0568\n        partial_r_ctrl_logfreq: -0.1428\n        partial_p: 0.2641\n      quartile_comparison:\n        low_bcs_cutoff: 0.798\n        high_bcs_cutoff: 0.827\n        low_bcs_f1: 0.3098\n        high_bcs_f1: 0.2275\n        delta_f1: -0.0823\n        low_bcs_freq: 2134\n        high_bcs_freq: 2049\n      confound_check:\n        bcs_vs_logfreq_r: 0.042\n        bcs_vs_logfreq_p: 0.74\n        logfreq_vs_f1_r: 0.25\n        logfreq_vs_f1_p: 0.048\n      verdict: Direction supports hypothesis. Spearman significant (p=0.02). Frequency\n        confound absent at type level (r=0.04).\n    overall_verdict: PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE\n      STRONG PASS, PER-TYPE DIRECTIONAL PASS\n- id: exp-003a\n  claim:\n  - 1\n  - 2\n  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination\n    instruction. Re-run exp1+exp2.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp003a_prompt_v2_rerun\n  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_mode: text_match\n    exp1_text_match:\n      count_1:\n        f1: 0.323\n        precision: 0.216\n        recall: 0.641\n        pred_gold_ratio: 2.97\n        n_batches: 64\n      count_2:\n        f1: 0.273\n        precision: 0.18\n        recall: 0.56\n        pred_gold_ratio: 3.11\n        n_batches: 5\n      count_6:\n        f1: 0.306\n        precision: 0.226\n        recall: 0.475\n        pred_gold_ratio: 2.1\n        n_batches: 5\n      count_12:\n        f1: 0.347\n        precision: 0.367\n        recall: 0.329\n        pred_gold_ratio: 0.9\n        n_batches: 5\n      count_22:\n        f1: 0.299\n        precision: 0.339\n        recall: 0.267\n        pred_gold_ratio: 0.79\n        n_batches: 5\n      count_44:\n        f1: 0.445\n        precision: 0.506\n        recall: 0.396\n        pred_gold_ratio: 0.78\n        n_batches: 5\n      count_64:\n        f1: 0.414\n        precision: 0.648\n        recall: 0.304\n        pred_gold_ratio: 0.47\n        n_batches: 5\n    exp2_text_match:\n      count_6:\n        f1: 0.32\n        precision: 0.26\n        recall: 0.416\n        pred_gold_ratio: 1.6\n        n_batches: 27\n      count_12:\n        f1: 0.306\n        precision: 0.291\n        recall: 0.323\n        pred_gold_ratio: 1.11\n        n_batches: 27\n    vs_exp001_delta:\n      count_1:\n        f1_delta: +0.139 (+76%)\n        precision_delta: +0.111 (+106%)\n        recall_delta: -0.079 (-11%)\n        overpred_fix: 6.85→2.97\n      count_6:\n        f1_delta: +0.151 (+97%)\n        precision_delta: +0.138 (+157%)\n        recall_delta: -0.145 (-23%)\n      count_12:\n        f1_delta: +0.101 (+41%)\n        precision_delta: +0.207 (+129%)\n        recall_delta: -0.210 (-39%)\n      count_44:\n        f1_delta: -0.028 (-6%)\n        precision_delta: +0.092 (+22%)\n        recall_delta: -0.155 (-28%)\n      count_64:\n        f1_delta: -0.049 (-11%)\n        precision_delta: +0.128 (+25%)\n        recall_delta: -0.114 (-27%)\n    key_finding: 'V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x\n      to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1).\n      But over-corrected at high counts: under-prediction (pred/gold<1) caused recall\n      drops of 27-39%, slightly lowering F1 at count_22-64.'\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MAVEN confusability study: count curve + within-count BCS correlation\n    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core\n    finding cross-task (NER→ED) with larger type space and known sibling confusion\n    (14.6-19.8%).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp-004\n  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs\n    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy\n    structure.'\n  status: DONE\n  conclusion: success\n  metrics:\n    n_event_types: 168\n    n_pairs: 14028\n    scs_mean: 0.2161\n    scs_std: 0.103\n    scs_max: 0.8368\n    scs_median: 0.2121\n    scs_q90: 0.3457\n    scs_q95: 0.3892\n    pairs_above_0.5: 119\n    pct_above_0.5: 0.85\n    train_docs: 2913\n    train_mentions: 77993\n    valid_docs: 710\n    valid_mentions: 18904\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n  status: planned\n- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n  status: planned\n- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.\n  status: planned\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional\n    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model\n    generalizability.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-003a\n  registry_id: exp012_llama_8b_r3\n  status: DONE\n  conclusion: failed\n- id: exp-016\n  claim:\n  - 1\n  - 2\n  description: 'FewRel cross-task replication: count curve + BCS correlation on FewRel\n    RE (80 relation types with --use_all). Replicates confusability effect NER→RE.\n    Pilot (fewrel_pilot) confirmed signal; formal run with full count curve [1,4,8,16,32,64,80].'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp_fewrel_formal\n  status_note: RUNNING (16-rel version). Will rerun with --use_all for 80-rel full\n    count curve after current run completes.\n  status: DONE\n  conclusion: success\n  metrics:\n    note: 16-rel sanity check only\n    exp1:\n      count_1:\n        mean_acc: 0.904\n        n_batches: 16\n      count_4:\n        mean_acc: 0.932\n        n_batches: 5\n      count_8:\n        mean_acc: 0.867\n        n_batches: 5\n      count_16:\n        mean_acc: 0.778\n        n_batches: 5\n        bcs: 0.9\n        zero_variance: true\n    exp2:\n      count_8_low_bcs:\n        acc: 0.889\n        bcs: 0.782\n      count_8_high_bcs:\n        acc: 0.798\n        bcs: 0.892\n      delta_bcs_effect: -0.091\n    trend: 'count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8%\n      (Δ=-9.1pp)'\n- id: exp-008\n  claim:\n  - 3\n  description: 'SDGD-zero on Few-NERD: confusability-minimizing batch composition\n    via embedding SCS + graph coloring. Compare vs single-pass full-schema baseline.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-003a\n  registry_id: exp008_sdgd_v2_fewnerd\n  status_note: 'DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass\n    baseline on Few-NERD. R1 (exp008_sdgd_zero_fewnerd) failed with script error.'\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 79\n    random_batch:\n      f1: 0.3007\n      precision: 0.3307\n      recall: 0.2758\n      batches: 8\n      time_s: 494\n    sdgd_zero:\n      f1: 0.2407\n      precision: 0.3244\n      recall: 0.1913\n      batches: 4\n      time_s: 261\n    per_type: killed before completion (3/4 modes done, Director approved kill)\n    vs_v1: confidence-gated merge did not improve over union merge. sdgd_zero 0.241\n      vs v1 0.251, random_batch 0.301 vs v1 0.320\n    key_finding: SDGD v2 confidence-gated merge + min_batch_size=8 failed to beat\n      single_pass baseline (F1=0.445). Both v1 and v2 confirm decomposition hurts\n      precision more than it helps recall. Claim 3 (SDGD framework) needs fundamental\n      rethink.\n- id: exp-009\n  claim:\n  - 3\n  description: 'SDGD-zero on MAVEN: confusability-minimizing batch composition on\n    168 event types. Compare vs single-pass + random batching. Cross-task validation\n    of SDGD framework (NER→ED).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-004\n  - exp-008\n  status: planned\n- id: exp-010\n  claim:\n  - 3\n  description: 'SDGD-cal on Few-NERD: empirical confusability from 5-10 calibration\n    examples (no gradients). Compare vs SDGD-zero.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-008\n  status: planned\n- id: exp-011\n  claim:\n  - 3\n  description: 'SDGD-cal on MAVEN: empirical confusability with calibration on 168\n    event types. Full comparison table.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-009\n  - exp-010\n  status: planned\n- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n  status: planned\n- id: exp-014\n  claim:\n  - 3\n  description: 'Ablation: per-type splitting (UniNER-style, 1 type per batch). Upper\n    bound on decomposition benefit. Reveals latency vs quality tradeoff.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n  status: planned\n- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp001_count_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    diagnosis: char offset 96.5% fabricated by model\n    text_match_reeval:\n      count_1:\n        f1: 0.184\n        precision: 0.105\n        recall: 0.72\n        pred_gold_ratio: 6.85\n      count_2:\n        f1: 0.123\n        precision: 0.068\n        recall: 0.698\n        pred_gold_ratio: 10.33\n      count_6:\n        f1: 0.155\n        precision: 0.088\n        recall: 0.62\n        pred_gold_ratio: 7.02\n      count_12:\n        f1: 0.246\n        precision: 0.16\n        recall: 0.539\n        pred_gold_ratio: 3.38\n      count_22:\n        f1: 0.322\n        precision: 0.232\n        recall: 0.527\n        pred_gold_ratio: 2.27\n      count_44:\n        f1: 0.473\n        precision: 0.414\n        recall: 0.551\n        pred_gold_ratio: 1.33\n      count_64:\n        f1: 0.463\n        precision: 0.52\n        recall: 0.418\n        pred_gold_ratio: 0.8\n    key_finding: recall monotonically decreases (0.72→0.42), precision monotonically\n      increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at\n      count_44\n    wrong_type_trend: 'type confusion increases with count: 0→2434, supports confusability\n      hypothesis'\n    spurious_dominant: spurious FPs (text in source but not entity) dominate at low\n      count, not hallucination\n    conclusion_text_match: F1 curve inversion caused by over-prediction confound,\n      NOT absence of confusability effect. Recall curve + type confusion pattern support\n      hypothesis.\n- exp_id: exp002_confusability_controlled\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp2_reeval_results.json (text_match, CLEAN)\n    primary_recall_vs_bcs:\n      count_6:\n        r: 0.2754\n        p: 0.1644\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.2219\n        p: 0.266\n        n: 27\n        verdict: FAIL\n      partial:\n        r: 0.2522\n        p: 0.0658\n        n: 54\n        verdict: FAIL\n    secondary_f1_vs_bcs:\n      count_6:\n        r: 0.1754\n        p: 0.3814\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.5012\n        p: 0.0077\n        n: 27\n        verdict: PASS\n      partial:\n        r: 0.3025\n        p: 0.0262\n        n: 54\n        verdict: PASS\n    mechanistic_confusion_rate:\n      random_batches:\n        count_6_high: 0.0157\n        count_6_low: 0.0088\n        ratio_6: 1.7\n        count_12_high: 0.0304\n        count_12_low: 0.0131\n        ratio_12: 2.4\n      extreme_batches:\n        count_6_high: 0.0728\n        count_6_low: 0.0014\n        ratio_6: 27.5\n        count_12_high: 0.048\n        count_12_low: 0.0061\n        ratio_12: 9.9\n      verdict: PASS\n    pairwise_confusion_analysis:\n      all:\n        n_pairs: 1953\n        pearson_r: 0.156\n        pearson_p: 4.6e-12\n        spearman_rho: 0.16\n        spearman_p: 1.3e-12\n      count_6:\n        n_pairs: 1770\n        pearson_r: 0.078\n        pearson_p: 0.001\n      count_12:\n        n_pairs: 1953\n        pearson_r: 0.147\n        pearson_p: 6.7e-11\n      nonzero_only:\n        all_spearman_rho: 0.254\n        all_spearman_p: 1.1e-06\n        count_12_pearson_r: 0.212\n        count_12_p: 0.00034\n      top_confused_pair: person-other <-> person-politician (BCS=0.934, confusion=156)\n    per_type_analysis:\n      n_types: 63\n      filter: freq>=5\n      micro_f1_vs_bcs:\n        pearson_r: -0.1828\n        pearson_p: 0.1516\n        spearman_rho: -0.2927\n        spearman_p: 0.0199\n        partial_r_ctrl_logfreq: -0.1998\n        partial_p: 0.1163\n      mean_f1_vs_bcs:\n        pearson_r: -0.1374\n        pearson_p: 0.283\n        spearman_rho: -0.2412\n        spearman_p: 0.0568\n        partial_r_ctrl_logfreq: -0.1428\n        partial_p: 0.2641\n      quartile_comparison:\n        low_bcs_cutoff: 0.798\n        high_bcs_cutoff: 0.827\n        low_bcs_f1: 0.3098\n        high_bcs_f1: 0.2275\n        delta_f1: -0.0823\n        low_bcs_freq: 2134\n        high_bcs_freq: 2049\n      confound_check:\n        bcs_vs_logfreq_r: 0.042\n        bcs_vs_logfreq_p: 0.74\n        logfreq_vs_f1_r: 0.25\n        logfreq_vs_f1_p: 0.048\n      verdict: Direction supports hypothesis. Spearman significant (p=0.02). Frequency\n        confound absent at type level (r=0.04).\n    overall_verdict: PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE\n      STRONG PASS, PER-TYPE DIRECTIONAL PASS\n- exp_id: exp003a_prompt_v2_rerun\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_mode: text_match\n    exp1_text_match:\n      count_1:\n        f1: 0.323\n        precision: 0.216\n        recall: 0.641\n        pred_gold_ratio: 2.97\n        n_batches: 64\n      count_2:\n        f1: 0.273\n        precision: 0.18\n        recall: 0.56\n        pred_gold_ratio: 3.11\n        n_batches: 5\n      count_6:\n        f1: 0.306\n        precision: 0.226\n        recall: 0.475\n        pred_gold_ratio: 2.1\n        n_batches: 5\n      count_12:\n        f1: 0.347\n        precision: 0.367\n        recall: 0.329\n        pred_gold_ratio: 0.9\n        n_batches: 5\n      count_22:\n        f1: 0.299\n        precision: 0.339\n        recall: 0.267\n        pred_gold_ratio: 0.79\n        n_batches: 5\n      count_44:\n        f1: 0.445\n        precision: 0.506\n        recall: 0.396\n        pred_gold_ratio: 0.78\n        n_batches: 5\n      count_64:\n        f1: 0.414\n        precision: 0.648\n        recall: 0.304\n        pred_gold_ratio: 0.47\n        n_batches: 5\n    exp2_text_match:\n      count_6:\n        f1: 0.32\n        precision: 0.26\n        recall: 0.416\n        pred_gold_ratio: 1.6\n        n_batches: 27\n      count_12:\n        f1: 0.306\n        precision: 0.291\n        recall: 0.323\n        pred_gold_ratio: 1.11\n        n_batches: 27\n    vs_exp001_delta:\n      count_1:\n        f1_delta: +0.139 (+76%)\n        precision_delta: +0.111 (+106%)\n        recall_delta: -0.079 (-11%)\n        overpred_fix: 6.85→2.97\n      count_6:\n        f1_delta: +0.151 (+97%)\n        precision_delta: +0.138 (+157%)\n        recall_delta: -0.145 (-23%)\n      count_12:\n        f1_delta: +0.101 (+41%)\n        precision_delta: +0.207 (+129%)\n        recall_delta: -0.210 (-39%)\n      count_44:\n        f1_delta: -0.028 (-6%)\n        precision_delta: +0.092 (+22%)\n        recall_delta: -0.155 (-28%)\n      count_64:\n        f1_delta: -0.049 (-11%)\n        precision_delta: +0.128 (+25%)\n        recall_delta: -0.114 (-27%)\n    key_finding: 'V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x\n      to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1).\n      But over-corrected at high counts: under-prediction (pred/gold<1) caused recall\n      drops of 27-39%, slightly lowering F1 at count_22-64.'\n- exp_id: exp-004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_event_types: 168\n    n_pairs: 14028\n    scs_mean: 0.2161\n    scs_std: 0.103\n    scs_max: 0.8368\n    scs_median: 0.2121\n    scs_q90: 0.3457\n    scs_q95: 0.3892\n    pairs_above_0.5: 119\n    pct_above_0.5: 0.85\n    train_docs: 2913\n    train_mentions: 77993\n    valid_docs: 710\n    valid_mentions: 18904\n- exp_id: exp004_maven_bcs\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    exp1_count_curve:\n      count_1:\n        n_batches: 64\n        exact_f1: 0.009\n        relaxed_f1: 0.106\n        bcs: 0\n      count_6:\n        n_batches: 5\n        exact_f1: 0.003\n        relaxed_f1: 0.103\n        bcs: 0.892\n      count_12:\n        n_batches: 5\n        exact_f1: 0.008\n        relaxed_f1: 0.146\n        bcs: 0.921\n      count_22:\n        n_batches: 5\n        exact_f1: 0.013\n        relaxed_f1: 0.185\n        bcs: 0.933\n      count_44:\n        n_batches: 5\n        exact_f1: 0.018\n        relaxed_f1: 0.247\n        bcs: 0.967\n      count_64:\n        n_batches: 5\n        exact_f1: 0.013\n        relaxed_f1: 0.245\n        bcs: 0.973\n    exp2_bcs_controlled:\n      count_6_high_bcs:\n        exact_f1: 0.0354\n        relaxed_f1: 0.211\n        bcs: 0.9447\n      count_6_low_bcs:\n        exact_f1: 0.0068\n        relaxed_f1: 0.089\n        bcs: 0.8709\n      count_12_high_bcs:\n        exact_f1: 0.0151\n        relaxed_f1: 0.1568\n        bcs: 0.9447\n      count_12_low_bcs:\n        exact_f1: 0.0068\n        relaxed_f1: 0.105\n        bcs: 0.9148\n    key_finding: 'MAVEN batch-level: high_bcs relaxed_F1 2.4x vs low_bcs (count_6).\n      Direction same as Few-NERD batch-level (positive). Pairwise + per-type analysis\n      needed to control frequency confound.'\n    note: exact_F1 very low (0.003-0.035), relaxed_F1 usable (0.089-0.247). Event\n      trigger boundary matching is fuzzy. A re-run (500 samples) is still in progress\n      in artifacts/exp004/.\n- exp_id: fewrel_pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    embedding: all-MiniLM-L6-v2\n    n_batches: 15\n    n_predictions: 374\n    count_4:\n      low_bcs_acc: 0.917\n      high_bcs_acc: 0.708\n      delta_pp: -20.9\n      low_bcs: 0.42\n      high_bcs: 0.97\n    count_8:\n      low_bcs_acc: 1\n      high_bcs_acc: 0.5\n      delta_pp: -50\n      low_bcs: 0.47\n      high_bcs: 0.97\n    count_16:\n      low_bcs_acc: 0.917\n      high_bcs_acc: 0.431\n      delta_pp: -48.6\n      low_bcs: 0.57\n      high_bcs: 0.97\n    key_finding: 'BCS-accuracy strong negative: high-BCS batches 43-71% vs low-BCS\n      92-100%. Effect increases with count. Cross-task (NER→RE) replication of confusability\n      hypothesis.'\n- exp_id: exp008_sdgd_zero_fewnerd\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp008_sdgd_zero_fewnerd_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 77.3\n    sdgd_zero:\n      f1: 0.2514\n      precision: 0.2096\n      recall: 0.3141\n      batches: 8\n      time_s: 408.7\n    random_batch:\n      f1: 0.3197\n      precision: 0.2491\n      recall: 0.4462\n      batches: 8\n      time_s: 476.1\n    per_type:\n      f1: 0.2915\n      precision: 0.194\n      recall: 0.5856\n      batches: 66\n      time_s: 2532.2\n    key_finding: All decomposition modes F1 < single_pass. Decomposition boosts recall\n      but kills precision (merge amplification). sdgd_zero worst F1, even below random_batch.\n- exp_id: exp_fewrel_formal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: 16-rel sanity check only\n    exp1:\n      count_1:\n        mean_acc: 0.904\n        n_batches: 16\n      count_4:\n        mean_acc: 0.932\n        n_batches: 5\n      count_8:\n        mean_acc: 0.867\n        n_batches: 5\n      count_16:\n        mean_acc: 0.778\n        n_batches: 5\n        bcs: 0.9\n        zero_variance: true\n    exp2:\n      count_8_low_bcs:\n        acc: 0.889\n        bcs: 0.782\n      count_8_high_bcs:\n        acc: 0.798\n        bcs: 0.892\n      delta_bcs_effect: -0.091\n    trend: 'count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8%\n      (Δ=-9.1pp)'\n- exp_id: exp_fewrel_formal_80rel\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_count_curve:\n      count_1:\n        acc: 0.8573\n        n_batches: 80\n        bcs: 0\n      count_4:\n        acc: 0.8667\n        n_batches: 5\n        bcs: 0.6335\n      count_8:\n        acc: 0.8021\n        n_batches: 5\n        bcs: 0.7175\n      count_16:\n        acc: 0.6958\n        n_batches: 5\n        bcs: 0.795\n      count_32:\n        acc: 0.6578\n        n_batches: 5\n        bcs: 0.8893\n      count_64:\n        acc: 0.5424\n        n_batches: 5\n        bcs: 0.9434\n      count_80:\n        acc: 0.5042\n        n_batches: 5\n        bcs: 0.9706\n    exp2_bcs_controlled:\n      count_8:\n        low_bcs_acc: 0.8229\n        low_bcs: 0.4715\n        high_bcs_acc: 0.5104\n        high_bcs: 0.9706\n        random_acc: 0.8025\n        delta_pp: -31.2\n      count_16:\n        low_bcs_acc: 0.8281\n        low_bcs: 0.5705\n        high_bcs_acc: 0.5156\n        high_bcs: 0.9706\n        random_acc: 0.7169\n        delta_pp: -31.2\n    vs_16rel:\n      degradation_16rel: -12.6pp (0.904→0.778)\n      degradation_80rel: -35.3pp (0.857→0.504)\n      bcs_effect_16rel: -9.1pp\n      bcs_effect_80rel: -31.2pp\n      amplification: 3.4x\n    key_finding: 80-rel count curve 0.857→0.504 (degradation 35.3pp, 远强于 16-rel 12.6pp).\n      BCS effect -31.2pp (3.4x amplification vs 16-rel). 更多 relations → 更大 confusion\n      space → 更强 degradation + BCS effect.\n- exp_id: exp008_sdgd_v2_fewnerd\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 79\n    random_batch:\n      f1: 0.3007\n      precision: 0.3307\n      recall: 0.2758\n      batches: 8\n      time_s: 494\n    sdgd_zero:\n      f1: 0.2407\n      precision: 0.3244\n      recall: 0.1913\n      batches: 4\n      time_s: 261\n    per_type: killed before completion (3/4 modes done, Director approved kill)\n    vs_v1: confidence-gated merge did not improve over union merge. sdgd_zero 0.241\n      vs v1 0.251, random_batch 0.301 vs v1 0.320\n    key_finding: SDGD v2 confidence-gated merge + min_batch_size=8 failed to beat\n      single_pass baseline (F1=0.445). Both v1 and v2 confirm decomposition hurts\n      precision more than it helps recall. Claim 3 (SDGD framework) needs fundamental\n      rethink.\n- exp_id: exp012_llama_fewnerd\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp007_error_taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_random:\n      bcs_zero:\n        n_fp: 6172\n        intra_sub_pct: 0\n        extra_sub_pct: 90.3\n        intra_sub_per_100_gold: 0\n      bcs_low:\n        n_fp: 2231\n        intra_sub_pct: 1.6\n        extra_sub_pct: 89.9\n        intra_sub_per_100_gold: 3.4\n      bcs_medium:\n        n_fp: 3843\n        intra_sub_pct: 10.6\n        extra_sub_pct: 78.1\n        intra_sub_per_100_gold: 6.47\n      bcs_high:\n        n_fp: 6188\n        intra_sub_pct: 49.4\n        extra_sub_pct: 30.8\n        intra_sub_per_100_gold: 12.93\n    correlation:\n      intra_sub_vs_bcs_spearman_rho: 1\n      intra_sub_vs_bcs_p: <0.001\n      chi_square: 6952\n      chi_square_p: ~0\n    exp2_controlled:\n      trend: IntraSub 3.2% -> 7.3% -> 8.6% (rho=1.0, p<0.001)\n    key_finding: 'BCS>=0.95: 49.4% FP are intra-batch type confusion (13/100 gold).\n      Hallucination+boundary <3%. LLM main error mode is type confusion, not hallucination.'\n- exp_id: exp012_llama_fewnerd_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp016_fewrel_error_taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    error_distribution:\n      zero_bcs:\n        bcs_mean: 0\n        correct_pct: 85.73\n        wrong_type_pct: 0\n        intra_sub_pct: 0\n        missed_pct: 14.27\n      low_bcs:\n        bcs_mean: 0.565\n        correct_pct: 85.42\n        wrong_type_pct: 4.17\n        intra_sub_pct: 4.17\n        missed_pct: 10.42\n      medium_bcs:\n        bcs_mean: 0.729\n        correct_pct: 75.7\n        wrong_type_pct: 13\n        intra_sub_pct: 13\n        missed_pct: 11.3\n      high_bcs:\n        bcs_mean: 0.86\n        correct_pct: 66.67\n        wrong_type_pct: 20.28\n        intra_sub_pct: 20.28\n        missed_pct: 13.05\n      very_high_bcs:\n        bcs_mean: 0.971\n        correct_pct: 52.03\n        wrong_type_pct: 32.25\n        intra_sub_pct: 32.25\n        missed_pct: 15.71\n    correlations:\n      intra_sub_vs_bcs_spearman: 0.9539\n      intra_sub_vs_bcs_p: <1e-6\n      accuracy_vs_bcs_spearman: -0.5821\n      accuracy_vs_bcs_p: <1e-6\n    cross_task:\n      ner_intra_sub_vs_bcs_rho: 1\n      re_intra_sub_vs_bcs_rho: 0.9539\n    key_finding: 100% of type confusion in RE is intra-batch (model only predicts\n      from schema). IntraSub vs BCS ρ=0.954 confirms NER finding. Missed rate flat\n      (10-16%), BCS drives confusion not detection failure.\n- exp_id: bootstrap_ci_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fewnerd_pairwise_r:\n      point: 0.112\n      ci_lower: 0.076\n      ci_upper: 0.156\n      n: 1953\n      note: point estimate 0.112 vs old 0.156 — re-run confirmed current value\n    maven_minilm_pairwise_r:\n      point: 0.129\n      ci_lower: 0.104\n      ci_upper: 0.156\n      n: 11026\n    fewrel_count8_delta_pp:\n      point: 31.2\n      ci_lower: 17.7\n      ci_upper: 42.7\n      n: 96+96\n    fewrel_count16_delta_pp:\n      point: 31.2\n      ci_lower: 22.9\n      ci_upper: 39.6\n      n: 192+192\n    fewnerd_pertype_rho:\n      point: -0.293\n      ci_lower: -0.492\n      ci_upper: -0.054\n      n: 63\n    confusion_ratio_count6:\n      point: 25.3\n      ci_lower: 6.1\n      ci_upper: 60.5\n    confusion_ratio_count12:\n      point: 21.2\n      ci_lower: 5.3\n      ci_upper: 52.2\n    key_finding: All CIs exclude null (0 for correlations, 1 for ratios). All effects\n      are directionally robust at 95% level.\n- exp_id: exp015_scs_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    all_pairs:\n      n: 1953\n      n_nonzero: 216\n      qwen3_spearman: 0.1682\n      qwen3_spearman_p: '7.3e-14'\n      qwen3_kendall: 0.1351\n      minilm_spearman: 0.1439\n      minilm_spearman_p: '1.7e-10'\n      minilm_kendall: 0.1152\n    nonzero_only:\n      n: 216\n      qwen3_spearman: 0.2722\n      qwen3_spearman_p: '5.0e-05'\n      qwen3_kendall: 0.2001\n      minilm_spearman: 0.306\n      minilm_spearman_p: '4.6e-06'\n      minilm_kendall: 0.2276\n    key_finding: Both embeddings significantly predict confusion (all p<1e-5). Qwen3\n      better overall (rho=0.168), MiniLM better on nonzero pairs (rho=0.306). SCS\n      is a valid but partial proxy — context, frequency, mention ambiguity also matter.\n- exp_id: exp012_llama_fewnerd_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_8b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_fewrel_40rel\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_awq\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp012_llama_fewnerd_r4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_8b_fewnerd\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_fewrel_40rel_r2\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp_fewrel_40rel_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp012_llama_8b_r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_llama_recall_count1: 0.702\n    exp1_llama_recall_count64: 0.273\n    exp1_recall_decline_pp: -42.9\n    exp1_per_batch_recall_corr_vs_qwen: 0.7249\n    exp1_llama_text_match_f1_range: 0.06-0.36\n    exp1_exact_f1: 0\n    exp1_note: exact/relaxed F1=0 due to missing char offsets, text_match is correct\n      metric\n- exp_id: exp012_llama_8b_r3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp006_interaction_2x2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    cell_means_f1:\n      low_count_low_bcs: 0.324\n      low_count_high_bcs: 0.313\n      high_count_low_bcs: 0.325\n      high_count_high_bcs: 0.277\n    main_effects:\n      count: -0.018\n      bcs: -0.029\n    interaction:\n      estimate: -0.036\n      z: -0.667\n      p: 0.505\n      bcs_effect_at_low_count: -0.011\n      bcs_effect_at_high_count: -0.048\n    verdict: 交互方向符合 multiplicative 假设但统计不显著 (p=0.505)，未检测到显著交互效应\n- exp_id: exp012_llama_8b_r2_exp2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: exp_fewrel_40rel_r4\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_acc_count1: 0.858\n    exp1_acc_count4: 0.867\n    exp1_acc_count8: 0.802\n    exp1_acc_count16: 0.697\n    exp1_acc_count32: 0.658\n    exp1_acc_count40: 0.588\n    exp1_decline_pp: -27\n    exp2_bcs_delta_count8: 0.333\n    exp2_bcs_delta_count16: 0.318\n    exp2_low_bcs_acc_count8: 0.833\n    exp2_high_bcs_acc_count8: 0.5\n    exp2_low_bcs_acc_count16: 0.818\n    exp2_high_bcs_acc_count16: 0.5\n- exp_id: exp012_llama_fewrel_ch2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp2_bcs_controlled:\n      count_8:\n        low_bcs_acc: 0.7812\n        high_bcs_acc: 0.5104\n        delta_pp: -27.1\n      count_16:\n        low_bcs_acc: 0.7552\n        high_bcs_acc: 0.5156\n        delta_pp: -24\n    overall_correlation:\n      n_batches: 54\n      pearson_r: -0.39\n      pearson_p: 0.004\n      spearman_rho: -0.43\n      spearman_p: 0.001\n    cross_model_comparison:\n      llama_delta_pp: -27.1\n      qwen3_delta_pp: -31.2\n      ratio: 0.87\n      note: LLaMA effect = 87% of Qwen3, direction and magnitude consistent\n    no_floor_effect: true\n    mean_accuracy: 0.77\n    accuracy_range: 0.41-0.98\n    key_finding: 'BCS confusability effect cross-model replicated: LLaMA Δ=-27.1pp\n      (87% of Qwen3 -31.2pp). Pearson r=-0.39 (p=0.004), Spearman ρ=-0.43 (p=0.001).\n      No floor effect.'\n- exp_id: exp_fewrel_16rel_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_batches: 100\n    pool_size: 16\n    batch_size: 8\n    bcs_range:\n    - 0.6532\n    - 0.9002\n    quartile_delta:\n      Q4_minus_Q1_pp: -5.31\n      ci_95_lower: -9.45\n      ci_95_upper: -4.49\n      note: CI values from pre-D038 bootstrap, may need re-verification with MEAN-based\n        BCS\n    pearson_r_bcs_acc: -0.467\n    regression_slope:\n      slope: -0.509\n      ci_95_lower: -0.556\n      ci_95_upper: -0.349\n      r_squared: 0.218\n      p_value: 1.01e-12\n      interpretation: per +0.1 BCS → -5.09pp accuracy\n      note: CI from pre-D038 bootstrap\n    amplification_ratio:\n      quartile_16_vs_80: 4.2\n      ci_95_lower: 3.3\n      ci_95_upper: 6.95\n    key_finding: '16-rel pool BCS effect (MEAN-based, D038): Δ(Q4-Q1)=-5.31pp, r=-0.467.\n      Regression slope=-0.509. Bootstrap 1000 resamples. [D038 MEAN correction applied,\n      old values: r=-0.637/Δ=-7.42pp/slope=-0.449]'\n- exp_id: exp_fewrel_16rel_100batch\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: exp_fewrel_80pool_16sub_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_batches: 100\n    pool_size: 80-rel pool, 16-type subsamples\n    batch_size: 8\n    mean_accuracy: 0.8077\n    mean_bcs: 0.557\n    bcs_range:\n    - 0.4578\n    - 0.6836\n    quartile_delta:\n      Q4_minus_Q1_pp: -3.92\n      ci_95_lower: -7.79\n      ci_95_upper: 0.42\n    pearson_r_bcs_acc: -0.221\n    pearson_p: 0.027\n    regression_slope:\n      slope: -0.401\n      ci_95_lower: -0.684\n      ci_95_upper: -0.062\n      interpretation: per +0.1 BCS → -4.01pp accuracy\n    key_finding: '80-pool 16-sub BCS effect directional: Δ(Q4-Q1)=-3.92pp CI crosses\n      zero [-7.79,+0.42], but regression slope=-0.401 CI[-0.684,-0.062] excludes zero.\n      Effect weaker than independent 16-rel pool (Δ=-7.42pp) due to narrower BCS range.'\n- exp_id: exp_maven_residualized_bcs\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    minilm:\n      raw_rho: 0.208\n      raw_p: 0.011\n      confound: log_freq\n      bcs_confound_r: 0.201\n      partial_r: 0.133\n      partial_p: 0.107\n    qwen3:\n      raw_rho: 0.184\n      raw_p: 0.025\n      confound: degree_centrality_0.7\n      bcs_confound_r: 0.854\n      partial_r: 0.063\n      partial_p: 0.442\n    joint_control:\n      qwen3_p: 0.439\n      minilm_p: 0.226\n      note: Both n.s. after controlling log_freq + degree jointly\n    key_finding: MAVEN BCS-F1 positive correlation is centrality artifact. MiniLM\n      confound=frequency, Qwen3 confound=degree centrality (r=0.854). After joint\n      control, both correlations vanish. Confirms pairwise SCS remains valid but per-type\n      aggregation fails on homogeneous schemas.\n- exp_id: exp_fewrel_v2_bcs_controlled\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    low_bcs_mean_acc: 0.8042\n    high_bcs_mean_acc: 0.725\n    delta_low_minus_high_pp: 7.92\n    bootstrap_ci_95_lower_pp: -5.21\n    bootstrap_ci_95_upper_pp: 21.46\n    n_bootstrap: 10000\n    n_batches_per_group: 5\n    samples_per_batch: 96\n    total_inferences: 960\n- exp_id: exp_docred_confusability\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_relation_types: 96\n    n_eval_samples: 1240\n    total_inferences: 13618\n    count_curve:\n      count_1: 0.88\n      count_4: 0.77\n      count_8: 0.774\n      count_16: 0.524\n      count_32: 0.521\n      count_64: 0.424\n      count_96: 0.387\n    bcs_effect_count16:\n      low_bcs_acc: 0.679\n      high_bcs_acc: 0.447\n      gap: 0.233\n      spearman_r: -0.661\n      slope: -0.713\n      slope_95ci:\n      - -0.909\n      - -0.529\n    bcs_effect_count32:\n      low_bcs_acc: 0.578\n      high_bcs_acc: 0.403\n      gap: 0.176\n      spearman_r: -0.509\n      slope: -0.69\n      slope_95ci:\n      - -0.854\n      - -0.519\n- exp_id: bcs_max_to_mean_fix\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: exp_confusability_batch_composition\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp_fewrel_v2_n25\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    n_low: 25\n    n_high: 25\n    low_bcs_mean_acc: 0.8521\n    high_bcs_mean_acc: 0.5967\n    delta_pp: 25.54\n    ci_95:\n    - 22.42\n    - 28.62\n    permutation_p: 0\n    pearson_r: -0.919\n    low_bcs_range:\n    - 0.356\n    - 0.367\n    high_bcs_range:\n    - 0.791\n    - 0.811\n    key_finding: v2 prompt does NOT eliminate confusability effect. At n=25 with wider\n      BCS separation, effect is massive (25.5pp) and highly significant. Prior n=5\n      result (7.9pp, CI crosses zero) was underpowered + narrow BCS contrast.\n- exp_id: exp_cross_embedding_sensitivity\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    fewnerd_qwen3:\n      pearson_r: 0.138\n      pearson_p: 1.0e-09\n      spearman_rho: 0.168\n      spearman_p: 7.3e-14\n    fewnerd_minilm:\n      pearson_r: 0.172\n      pearson_p: 2.0e-14\n      spearman_rho: 0.144\n      spearman_p: 1.7e-10\n    fewrel_minilm:\n      slope: -0.485\n      r: -0.398\n      p: 0.04\n    fewrel_qwen3:\n      slope: -0.542\n      r: -0.185\n      p: 0.356\n      note: BCS range compression (std=0.034 vs MiniLM 0.081), directional but n.s.\n    key_finding: SCS-confusion signal robust to embedding choice (both significant\n      on Few-NERD). MiniLM better for BCS due to designed-for-similarity. Qwen3 causal-LM\n      embeddings compress BCS range.\n- exp_id: exp017_gpt4o_mini_fewrel\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T07:35:40.645Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T07:35:40.645Z",
  "sessionId": "e29e0c1a-a118-4d50-b730-11d6e018290b"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-16T07:35:40.665Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d68431c4-e447-44c2-8204-594b2ddc9bd0",
  "type": "user",
  "uuid": "63383aff-b899-4d0e-a4ef-b7682f509820",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "e29e0c1a-a118-4d50-b730-11d6e018290b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T07:35:40.663Z_

```json
{
  "parentUuid": "63383aff-b899-4d0e-a4ef-b7682f509820",
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
  "uuid": "f6eadf7e-80ba-4b0f-8d4d-bea5f2d1fd4a",
  "timestamp": "2026-05-16T07:35:40.663Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "e29e0c1a-a118-4d50-b730-11d6e018290b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T07:35:40.664Z_

```json
{
  "parentUuid": "f6eadf7e-80ba-4b0f-8d4d-bea5f2d1fd4a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5eca5fe4-a63b-46a4-a033-e230e5ebc7de",
  "timestamp": "2026-05-16T07:35:40.664Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "e29e0c1a-a118-4d50-b730-11d6e018290b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "5eca5fe4-a63b-46a4-a033-e230e5ebc7de",
  "sessionId": "e29e0c1a-a118-4d50-b730-11d6e018290b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three scenario tiers for schema-dag extraction paper",
  "sessionId": "e29e0c1a-a118-4d50-b730-11d6e018290b"
}
```

---

### Assistant

_source line 8 · 2026-05-16T07:37:51.822Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze this research project carefully to define three tiers for a Dream simulation.

The project is about schema-DAG extraction - specifically studying how type confusability affects training-free LLM information extraction. Let me understand the current state:

**Core Claims (after D019 revision):**
1. Confusability Independence: Type confusability independently predicts extraction quality degradation
2. Multi-Channel Degradation: Count and confusability degrade through orthogonal channels
3. SDGD Effectiveness: DROPPED - negative result

**What's done:**
- Pairwise SCS→confusion correlation validated on Few-NERD (r=0.112) and MAVEN MiniLM (r=0.129)


- FewRel shows a dramatic count effect with -31.2pp drop on 80-relation tasks and 3.4x amplification, while error patterns remain consistent across tasks with near-perfect correlation (ρ=1.0 for NER, ρ=0.954 for RE)
- MAVEN's centrality confound has been analyzed, bootstrap confidence intervals exclude null across the board, and LLaMA replicates the FewRel pattern at 87% of Qwen's magnitude
- SDGD decomposition actually hurts performance more than it helps, both embedding approaches show significant SCS effects, and I'm still working through the DocRED count analysis

Now looking at what's actually failed or problematic: the LLaMA Few-NERD experiments keep crashing despite FewRel working fine, though the DocRED confusability analysis did complete successfully, the 2x2 interaction test came back negative, and Qwen's pairwise MAVEN correlations aren't significant while per-type results show the expected centrality confound direction but lose significance after controlling for frequency in Few-NERD. Still need to run SDGD-zero and SDGD-calibration on MAVEN to finish the planned experiments.

With the ARR deadline just 10 days away, I'm thinking through what the paper actually claims now—it's framed as an empirical study of confusability in training-free LLM information extraction, with SDGD as a negative result showing confusability independence and multi-channel degradation. The remaining experiments could still shift things, but most of the core work is already done, so it really comes down to how well I can write this up and whether reviewers buy the framing.

I'm mapping out three scenarios: best case where all results hold and reviewers see value in the empirical rigor and negative finding, median case where some effect sizes get questioned and I need to soften claims, and worst case where the work gets dismissed as incremental and the small correlations and failed replications become fatal flaws. To evaluate these properly, I need to track the key metrics like the pairwise confusion correlations and the accuracy gaps when controlling for other factors. Δpp)
3. Error taxonomy monotonicity (ρ)
4. Cross-task replication count
5. Multi-model replication success
6. Reviewer scores (for venue acceptance)

Actually, for a Dream simulation, I should think about what the "simulation" would test. Given that most experiments are done, the Dream simulation is likely about:
- How the remaining 9 days of work go
- Whether additional experiments succeed
- How the paper is received at review

Let me define the tiers more carefully:

**Best:**
- Meaning: All claims fully validated with existing + any remaining experiments; paper accepted at EMNLP Main
- Key assumptions: (1) pairwise confusability signal replicates if tested on additional models/datasets, (2) reviewers value controlled empirical methodology, (3) negative SDGD result seen as contribution, (4) effect sizes (r=0.11-0.13) accepted as meaningful given the noise floor
- Metrics: ARR scores ≥3.5 average, all CIs remain excluding null, cross-task ρ for error taxonomy stays >0.9
- Narrative: Original framing holds — first controlled study isolating confusability from count, multi-channel model validated across 3 tasks + 2 models

**Median:**
- Meaning: Paper accepted at EMNLP Findings (not Main), or needs major revision
- Key assumptions: (1) Some reviewers push back on small pairwise effect sizes, (2) LLaMA failure on NER noted as weakness, (3) MAVEN per-type confound seen as limiting rather than contributing
- Metrics: ARR scores 3.0-3.5, some concerns about generalizability
- Narrative: Need to soften "independently predicts" to "is associated with," acknowledging that the effect sizes and model limitations constrain how strongly I can claim the confusability mechanism

. I should emphasize FewRel large-effect results more, downplay pairwise correlations

**Worst:**
- Meaning: Paper rejected, needs substantial rework for resubmission
- Key assumptions: (1) Reviewers view r=0.11-0.13 as too small to be meaningful, (2) LLaMA NER failure and interaction non-significance (p=0.505) seen as evidence against claims, (3) no practical method (SDGD failed) makes paper seem incomplete, (4) "just an empirical study" criticism not adequately mitigated
- Metrics: ARR scores <3.0, multiple reviewers flag same issues
- Narrative: Reframe away from "confusability predicts degradation" toward "characterizing failure modes of LLM IE" — emphasize the error taxonomy and multi-channel model as the core contribution, use pairwise correlation as supporting evidence rather than the main claim

For the Worst case, I'd pivot the narrative to focus on what we've learned about *how* LLMs fail at IE tasks, with confusability as one lens among several. The error taxonomy becomes the hero, not the confusability mechanism.

For the Median case, I'm hedging claims and leaning on the strongest results (FewRel) while acknowledging limitations.

For the Best case, the controlled methodology and replication across tasks/models is the strength.

Now, what should I actually do in the next 9 days to maximize the probability of Best or Median?

1. **Finalize the error taxonomy** — make sure it's robust and well-documented
2. **Run additional model tests** if feasible (e.g., GPT-4, Mistral) to show generalization
3. **Strengthen the SDGD analysis** — explain why it failed and what that tells us
4. **Write the paper** with careful framing:
   - Lead with the controlled study design
   - Present the error taxonomy as a contribution
   - Frame confusability as one explanatory factor, not the only one
   - Acknowledge effect sizes and limitations upfront
5. **Prepare for revision** — anticipate reviewer concerns and address them preemptively

I think the key insight is that the paper's strength is in the *methodology* (controlled study, multi-channel model, error taxonomy) rather than in the magnitude of individual effect sizes. If I lead with that, I'm more likely to land in Best or Median.

Let me start writing. evidence rather than headline claim

Now I'm thinking through what specific numbers might still be uncertain. For the pairwise correlations, those experiments are already done, so the real unknowns are whether any remaining experiments will run and how reviewers will perceive the work. The Dream simulation probably hinges on completing the remaining planned experiments over the next 9 days and the eventual review outcome.

Looking at what's still uncertain: they've been trying to get a second model working on NER but LLaMA failed multiple times, there was a negative interaction effect in exp-006, and there might be additional datasets to test. Most of the priority experiments are actually done already though.

For the simulation, I should focus on metrics that are still in flux—whether they attempt any remaining experiments and what the EMNLP review scores end up being. The pairwise correlations are locked in around 0.11-0.13, the controlled comparison on FewRel is fixed at -31.2pp, the multi-model replication with LLaMA is done at -27.1pp, and the error taxonomy consistency is already 0.95-1.0. The real variable is the ARR reviewer scores. The worst-case scenario would require substantial reworking and resubmission. But I'm realizing the user actually asked about Dream simulation tiers—predicting the research outcome holistically, not just the review. Given where things stand with 10 days left, most experiments complete, and the failed SDGD result dropped as a negative finding, the real question is whether the current narrative around the multi-model approach is strong enough to carry the paper. Now I'm working through the metrics that actually matter for this prediction—specifically tracking which dataset and embedding combinations show significant pairwise effects, since that's where the uncertainty really lies. I need to get NER working with a second model to strengthen the multi-model replication story, though LLaMA has failed multiple times. The real question is whether the 2x2 interaction will hold up under scrutiny, and I'm realizing I should focus my remaining effort on what's genuinely uncertain rather than trying to optimize every metric at once. The main uncertainties now are the review outcome and a few remaining experiments still in progress. I'm structuring the tiers around what the final evidence package looks like: a best case where all results hold and new replications on LLaMA and DocRED strengthen the multi-model coverage, leading to EMNLP Main acceptance; a median scenario where existing results suffice but reviewers request revisions, landing in EMNLP Findings; and a worst case where small effect sizes get dismissed and I need to substantially reframe the contribution, though still aiming for EMNLP.

For the specific metrics across these scenarios, I'm mapping out expected ranges for pairwise correlations, batch composition effects, reviewer scores, and cross-task replication rates to anchor what success looks like at each tier.

Now I'm thinking through the multi-model validation piece—whether results hold across different architectures and task combinations—and then I need to nail down the core assumptions that either hold or break under scrutiny, starting with whether the pairwise confusion signal is actually robust enough to drive the findings. cross-task signal (r=0.10-0.15, CIs exclude zero)
**A2**: Multi-channel degradation (count→recall, confusability→type confusion) is a real, orthogonal decomposition
**A3**: The effect amplifies with schema complexity (FewRel 3.4x scaling)
**A4**: Multi-model generalizability (beyond Qwen3-32B)
**A5**: The centrality confound explanation for MAVEN per-type is accepted as a methodological contribution (not a failure)
**A6**: Negative SDGD result is valued as an honest contribution (not seen as "paper has no method")
**A7**: Reviewers accept empirical study format for EMNLP (analogous to "Lost in the Middle")

Now for each tier:

**Best**: A1-A7 all hold
**Median**: A1-A3 hold, A4 partial (FewRel only), A5-A6 questioned but accepted with caveats, A7 holds
**Worst**: A1-A3 hold but effect sizes questioned, A4 fails, A5-A6 rejected, A7 doesn't hold

Now I'm looking at what's actually fixed versus what still needs to be determined. I have the core metrics pinned down—the pairwise correlations across Few-NERD and MAVEN, the FewRel degradation numbers, and the error taxonomy agreement scores—so I can work with those as anchors for the different outcome scenarios.

The real variables are whether the batch composition experiment finishes successfully, what new experiments might emerge in the remaining time, and crucially how the reviewers will interpret all this evidence. The venue outcome hinges on whether they see the negative SDGD result as a genuine contribution or a weakness, and whether the narrative about confusability as a decomposable phenomenon feels coherent to them.

For the YAML, I need metrics that directly influence reviewer perception: average scores they'd give, how many tasks show clean significant results, whether effect sizes replicate consistently across models, the overall coherence of the story, and whether the credibility of the effect sizes themselves holds up under scrutiny. I should also track practical metrics like the number of significant replications across the different task-model combinations and the ratio of effect sizes between models to show replication strength.

Writing the YAML now... are genuinely predictive and have the consistency property:

1. `pairwise_r_min_across_tasks`: minimum pairwise r across datasets where signal is claimed
   - Best: [0.10, 0.16] — all above 0.10
   - Median: [0.05, 0.12] — some weaker
   - Worst: [0.00, 0.08] — some fail to replicate or new analysis undermines

Wait, but the experiments are done. The pairwise r values are fixed. The uncertainty is in how they're interpreted.

Maybe I should frame metrics differently. I could track how many of the 2 claims survive review, the average reviewer scores, how many new supporting experiments get completed before the deadline, and what the venue tier ends up being. But actually, given where the project stands, the cleanest approach is to focus on what's still uncertain: the outcome of remaining experiments like the batch composition study, the paper's quality and persuasiveness, and how the review process unfolds. So I'm thinking about tracking the success rate of those remaining experiments, the individual reviewer scores, the meta-reviewer's decision, whether a rebuttal could flip borderline reviewers, how many of the datasets show clean replication, and validation across different models. _strength`: number of model×task cells with significant BCS effect

OK I think I'm overthinking this. Let me just write a clear, practical YAML that captures the three scenarios well. I'll focus on what's truly at stake for this paper in the next ~10 days and at review time.

Here's my final structure:

**Best**: Everything that can go right does. Remaining experiments confirm. Paper is tightly written. Reviewers are receptive.
- Assumptions: A1-A7 hold. Remaining running experiment (batch_composition) succeeds. Writing is excellent.
- Metrics: ARR avg 3.5-4.0, 0-1 major weaknesses flagged, 3-4 clean cross-task replications
- Narrative: Original framing holds. "First controlled empirical study" + "multi-channel model" + "pairwise robustness" all stand as contributions.

**Median**: Core results hold but with caveats. Some reviewer concerns but manageable. I'd soften the language around independent prediction, lean on FewRel and the error taxonomy as the main evidence, treat MAVEN and NER as supporting validation, and reframe the whole thing as an empirical characterization rather than a predictive model.

**Worst**: Core hypothesis survives but paper gets rejected. Effect sizes get questioned, A4 fails to replicate, and I need to find a completely different angle to make this work. Now I'm setting the metric ranges for the scoring dimensions—defining what constitutes strong, moderate, and weak performance across claims support, rebuttal potential, experimental outcomes, and venue fit for both the main narrative and findings-focused submission.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eca5fe4-a63b-46a4-a033-e230e5ebc7de",
  "isSidechain": false,
  "requestId": "req_011Cb5s1ApfyN7PZi6DZAJph",
  "type": "assistant",
  "uuid": "e7043598-21aa-490f-b9e9-116de3342718",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "e29e0c1a-a118-4d50-b730-11d6e018290b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ijWhaiiXTDrFmMAqGJtTK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25967,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8393,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25967
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

_source line 9 · 2026-05-16T07:38:39.907Z_

```yaml
tiers:
  best:
    meaning: "两条 claim 均以当前数据充分支撑，SDGD 负面结果被视为方法论贡献，论文被 EMNLP Main 接收"
    key_assumptions:
      - "A1: Pairwise SCS→confusion 的 r=0.11-0.13 被接受为有意义的效应量（reviewers 认可 noise floor 高的 IE 任务中此量级合理）"
      - "A2: 多通道退化模型（count→recall, confusability→type confusion）的正交性被 error taxonomy ρ≥0.95 充分证明"
      - "A3: FewRel 80-rel 的 3.4× amplification 被视为 schema complexity scaling 的强证据"
      - "A4: LLaMA FewRel 复现（Δ=-27.1pp, 87% of Qwen3）被接受为充分的 multi-model 验证"
      - "A5: MAVEN per-type centrality confound 被视为方法论贡献（何时聚合度量失效）而非负面证据"
      - "A6: SDGD 负面结果 + merge amplification 分析被视为诚实贡献（类比 negative results track）"
      - "A7: 纯实证研究格式被 EMNLP 接受（类比 Lost in the Middle, TACL 2024）"
    number_ranges:
      arr_avg_score: [3.5, 4.0]
      claims_fully_supported: [2, 2]
      major_reviewer_weaknesses: [0, 1]
      cross_task_significant_replications: [3, 4]  # NER+RE+ED+DocRED
      multi_model_effect_consistency: [0.85, 1.0]  # LLaMA/Qwen3 ratio
      venue_probability_main: [0.55, 0.75]
      venue_probability_findings_or_above: [0.85, 0.95]
      rebuttal_flip_probability: [0.8, 1.0]
    narrative_direction: >
      原始 framing 完全成立。标题级 claim: "Pairwise type confusability independently predicts
      LLM IE degradation across three tasks and two models." 两条 claim 均以强证据支撑:
      Claim 1 靠 pairwise 相关性 + FewRel BCS-controlled gap + DocRED replication;
      Claim 2 靠 error taxonomy cross-task ρ≥0.95。SDGD 负面结果作为 Section 6 讨论，
      指向 calibration-based 方向。MAVEN centrality confound 作为独立的方法论发现。
      Embedding ablation 2×3 matrix 作为实践指南。不需要调整 claim 强度。

  median:
    meaning: "核心假设部分验证，部分 reviewer 质疑效应量或覆盖面，论文落入 EMNLP Findings 或需 rebuttal 挽救"
    key_assumptions:
      - "A1 部分成立: Pairwise r=0.11-0.13 被质疑为'统计显著但实际意义有限'，需补充 FewRel 的大效应量（Δ=-31pp）来说服"
      - "A2 成立: Error taxonomy 证据清晰，无争议"
      - "A3 成立: Scaling 证据充分"
      - "A4 部分成立: Reviewers 指出 LLaMA 仅在 FewRel 成功，Few-NERD 多次失败是 generalizability 短板"
      - "A5 争议: 1-2 位 reviewer 视 MAVEN per-type 正方向为 counter-evidence，centrality confound 解释被要求补充定量验证"
      - "A6 争议: 'No practical method' 被标记为主要弱点，SDGD 负面结果不足以弥补"
      - "A7 基本成立: 实证研究格式被接受，但被要求补充更强的 practical implications"
    number_ranges:
      arr_avg_score: [3.0, 3.5]
      claims_fully_supported: [1, 2]
      major_reviewer_weaknesses: [2, 3]
      cross_task_significant_replications: [2, 3]
      multi_model_effect_consistency: [0.70, 0.85]
      venue_probability_main: [0.15, 0.35]
      venue_probability_findings_or_above: [0.50, 0.70]
      rebuttal_flip_probability: [0.4, 0.65]
    narrative_direction: >
      需要调整 claim 强度和重心分配。"independently predicts" 软化为 "is associated with"
      或 "contributes to predicting"。将 FewRel 的大效应量（Δ=-31pp, -27pp cross-model）
      提升为 headline evidence，pairwise r=0.11-0.13 降级为 supplementary cross-task validation。
      Claim 2（multi-channel）保持不变，error taxonomy 是最无争议的证据。
      补充一个 "practitioner guideline" 小节：基于发现给出 schema 设计的具体建议
      （e.g., 避免 BCS>0.8 的类型同批出现），弥补没有可用方法的短板。
      MAVEN centrality confound 可能需要追加 synthetic schema 实验来定量验证聚合失效条件。
      Rebuttal 重点: (1) effect size 在 IE 任务中的合理性论证, (2) LLaMA NER 失败的技术原因
      (模型输出格式问题而非假设不成立), (3) 补充 1-2 个 reviewer 要求的分析。

  worst:
    meaning: "核心假设不被 reviewers 接受为充分验证，论文被拒，需要找新 angle 重新 reframe 后重投同一 venue"
    key_assumptions:
      - "A1 不被接受: 多位 reviewer 认为 r=0.11-0.13 太小，FewRel 的大效应被归因于 extreme batch design（非自然条件）"
      - "A2 部分成立但被矮化: Error taxonomy 被视为'描述性工作'而非贡献"
      - "A3 被质疑: 3.4× amplification 来自 16-rel vs 80-rel 对比，reviewer 指出这混淆了 count 和 confusability 的 scaling"
      - "A4 失败: LLaMA NER 多次崩溃 + 仅 FewRel 一个任务复现被判定为不充分"
      - "A5 被拒绝: MAVEN per-type 正方向被视为反证，centrality confound 解释被认为是 post-hoc rationalization"
      - "A6 被拒绝: '没有可用方法的分析论文不适合 EMNLP Main/Findings'"
      - "A7 失败: 多位 reviewer 认为贡献不足以构成独立论文"
    number_ranges:
      arr_avg_score: [2.0, 3.0]
      claims_fully_supported: [0, 1]
      major_reviewer_weaknesses: [4, 6]
      cross_task_significant_replications: [1, 2]  # reviewers only accept FewRel + maybe NER error taxonomy
      multi_model_effect_consistency: [0.50, 0.70]
      venue_probability_main: [0.0, 0.10]
      venue_probability_findings_or_above: [0.05, 0.25]
      rebuttal_flip_probability: [0.05, 0.25]
    narrative_direction: >
      放弃 "confusability predicts degradation" 作为标题级 claim。Reframe 为
      "Characterizing and Diagnosing Schema-Induced Failure Modes in Training-Free LLM IE"。
      核心叙事转向: (1) 提出 multi-channel degradation 作为诊断框架（不是预测模型），
      error taxonomy 成为主要贡献; (2) 将 pairwise correlation 作为 channel 2 存在性的
      supporting evidence 而非独立 claim; (3) SDGD 失败 + MAVEN centrality confound 合并为
      "schema decomposition 比想象中更难" 的系统性分析; (4) 新增 prescriptive 贡献:
      基于所有实验（包括负面结果）给出 schema 设计决策树。需要补充的实验:
      (a) 至少一个非 extreme-batch 的自然条件下的 BCS 效应验证,
      (b) 第二个模型在 NER 或 ED 上的成功复现（考虑换 Mistral 或 Gemma 而非继续 LLaMA）,
      (c) 将 SDGD-cal（empirical confusion matrix）跑通作为 proof-of-concept。
      目标仍是 EMNLP 2026（下一个 ARR cycle, September），不降级 venue。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7043598-21aa-490f-b9e9-116de3342718",
  "isSidechain": false,
  "requestId": "req_011Cb5s1ApfyN7PZi6DZAJph",
  "type": "assistant",
  "uuid": "993fa080-2b47-4346-9025-182e356a8d8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "e29e0c1a-a118-4d50-b730-11d6e018290b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012ijWhaiiXTDrFmMAqGJtTK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 25967,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8393,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 25967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8393,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 25967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 25967
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "993fa080-2b47-4346-9025-182e356a8d8f",
  "sessionId": "e29e0c1a-a118-4d50-b730-11d6e018290b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three scenario tiers for schema-dag extraction paper",
  "sessionId": "e29e0c1a-a118-4d50-b730-11d6e018290b"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "993fa080-2b47-4346-9025-182e356a8d8f",
  "sessionId": "e29e0c1a-a118-4d50-b730-11d6e018290b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three scenario tiers for schema-dag extraction paper",
  "sessionId": "e29e0c1a-a118-4d50-b730-11d6e018290b"
}
```

---
