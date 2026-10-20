# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/263d3c39-27c7-4994-a66d-4427b1b10f55.jsonl`
- **Structured JSON:** [`748f97f4280d73ec1489.json`](../../sessions/74/748f97f4280d73ec1489.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T14:08:37.746Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T14:08:37.746Z",
  "sessionId": "263d3c39-27c7-4994-a66d-4427b1b10f55",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: schema-dag-extraction\nfocus: 80-rel FewRel formal results now available (Δ=-31.2pp, 3.4x scaling). SDGD-zero negative (exp-008). exp-012 multi-model in progress. Evaluate whether Claim 3 (SDGD) should pivot to analysis-only paper or attempt SDGD v2.\n\n## paper_framing.md\n\n# Paper Framing — schema-dag-extraction\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 25 cycle)\n- Commitment deadline: August 2, 2026\n- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)\n- Deadline: ARR May 25, 2026 (10 days from today)\n\n## Core Claims (3 conditions) — Revised per D012\n\n1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) extreme-batch accuracy gap on FewRel, (c) >=2 models.\n\n2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.\n\n3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the pairwise-similarity-thresholded graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). SDGD directly leverages pairwise confusability (validated signal), avoiding per-type aggregation confounds. Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).\n\n## Story Spine — Revised per D012\n\n- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.\n\n- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.\n\n- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We operationalize pairwise confusability into SDGD, a principled framework for confusability-minimizing schema decomposition.\n\n- **Three-task validation**:\n  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.156 (p<1e-11), per-type ρ=-0.293 (p=0.02), 10-28x confusion ratio\n  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel\n  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)\n\n- **Headline result template**: \"Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.12-0.16, p<1e-6), with 10-28x more type confusion errors in high-confusability batches. On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid. SDGD-zero, operating on pairwise similarity, improves F1 by X points over single-pass on Few-NERD.\"\n\n## Core Insight — Multi-Channel Degradation + Pairwise Robustness\n\nSchema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:\n- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.\n- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.\n\nThese channels are orthogonal and independently addressable.\n\n**Pairwise vs Aggregated Confusability**:\n- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.156) and MAVEN (MiniLM, r=0.120).\n- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.\n- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.\n\n## Evidence Hierarchy (D012)\n\n### Tier 1: PRIMARY — Pairwise SCS → Confusion\n\nThe cleanest evidence. Directly measures: are semantically similar type pairs more often confused?\n\n**Few-NERD (NER)** — Qwen3 embeddings:\n- Pearson r=0.156 (p=4.6e-12, n=1953 type pairs)\n- Nonzero-only Spearman ρ=0.254 (p=1.1e-6)\n- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)\n- Immune to type frequency confound (operates at type-pair level)\n\n**MAVEN (ED)** — MiniLM embeddings:\n- Pearson r=+0.120 (p≈0, n=11026 type pairs)\n- Nonzero-only Spearman ρ=+0.191 (p<0.001)\n- Cross-task replication on same-domain schema\n- Note: Qwen3 pairwise not significant on MAVEN (r=-0.007, p=0.41) — embedding choice matters for pairwise signal in homogeneous schemas\n\n### Tier 2: STRONG SECONDARY — FewRel Cross-Task Replication\n\nLarge effect size, cross-task (RE), scaling with schema complexity:\n\n**Formal 80-rel study** (exp_fewrel_formal_80rel):\n- Count curve: acc 85.7% (count=1) → 50.4% (count=80), BCS 0→0.97\n- BCS-controlled: count_8 low-BCS 82.3% vs high-BCS 51.0% (Δ=-31.2pp)\n- BCS-controlled: count_16 low-BCS 82.8% vs high-BCS 51.6% (Δ=-31.2pp)\n- **Scaling**: vs 16-rel, degradation 2.8x (35.3pp vs 12.6pp), BCS effect 3.4x (-31.2pp vs -9.1pp)\n\n**16-rel sanity check** (exp_fewrel_formal):\n- count_8: low-BCS 88.9% vs high-BCS 79.8% (Δ=-9.1pp)\n\n**Pilot extreme batches** (fewrel_pilot, MiniLM):\n- count_4: Δ=-20.9pp, count_8: Δ=-50.0pp, count_16: Δ=-48.6pp\n\nKey insight: confusability effect amplifies with schema size — direct evidence for multi-channel degradation scaling\n\n### Tier 3: SUPPORTING — Few-NERD Per-type Analysis\n\nBridges pairwise and batch-level, demonstrates per-type signal in cross-domain schema:\n- Spearman ρ=-0.293 (p=0.020, n=63 types, freq≥5) — Qwen3 embeddings\n- Partial r=-0.200 (p=0.116) controlling for log-frequency\n- Quartile comparison: high-BCS types F1=0.228 vs low-BCS F1=0.310 (Δ=-8.2pp)\n- BCS-frequency uncorrelated at type level (r=0.042, p=0.74)\n- MiniLM per-type: ρ≈0 (p=0.97) — extraction model alignment required for per-type signal\n\n### Tier 4: DISCUSSION — MAVEN Per-type Centrality Confound\n\nMethodological case study on when aggregated confusability measures fail:\n- Qwen3 per-type: ρ=+0.189 (p=0.021) — OPPOSITE direction\n- MiniLM per-type: ρ=+0.208 (p=0.011) — ALSO positive, ruling out embedding compression as sole explanation\n- Both embeddings agree: positive direction on MAVEN is an intrinsic property of the type structure\n- Explanation: in homogeneous schemas, mean BCS conflates confusability with type centrality (types with many semantic neighbors → common/central types → higher F1)\n- This is stronger than \"domain boundary\" — it identifies the specific mechanism (aggregation confound) rather than just the boundary condition\n\n### Tier 5: MECHANISTIC — Error Taxonomy\n\nConfusion rate differential demonstrates the mechanism:\n- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS\n- Random batches: 1.7-2.4x ratio (still significant, smaller effect)\n- Type confusion errors increase with count AND with confusability (additive)\n\n## Embedding Ablation (D010)\n\n2×3 matrix: {Qwen3, MiniLM} × {Few-NERD, FewRel, MAVEN}\n\n### Per-type (Layer 2)\n| | Few-NERD | FewRel | MAVEN |\n|---|---|---|---|\n| Qwen3 | ρ=-0.293 ✓ | pending | ρ=+0.189 ✗ |\n| MiniLM | ρ≈0 ✗ | Δ=21-50pp ✓ | ρ=+0.208 ✗ |\n\n### Pairwise (Layer 1)\n| | Few-NERD | MAVEN |\n|---|---|---|\n| Qwen3 | r=0.156 ✓ | r=-0.007 ✗ |\n| MiniLM | — | r=+0.120 ✓ |\n\n**Interpretation**: No single embedding dominates. Extraction-model embeddings (Qwen3) capture per-type confusability in cross-domain schemas. Generic embeddings (MiniLM) capture pairwise confusability in same-domain schemas. SDGD should use task-appropriate embeddings; SDGD-cal (empirical confusion) bypasses embedding choice entirely.\n\n## Venue Fit Risks\n\n- **\"Just an empirical study\"**: Mitigated by SDGD as direct operationalization. Controlled experimental design parallels \"Lost in the Middle\" (TACL 2024).\n- **Training-free IE relevance**: Cite deployment scenarios — clinical, regulatory, multilingual.\n- **Multi-model generalizability**: Qwen3-32B primary + LLaMA-3.3-70B (exp-012).\n- **MAVEN doesn't support hypothesis?**: Pairwise MiniLM does support it. Per-type centrality confound is methodological contribution, not failure.\n- **Embedding sensitivity**: 2×3 ablation matrix is itself a contribution — characterizes when which proxy works.\n\n## Anticipated Reviewer Concerns\n\n| Concern | Response Strategy | Experiment |\n|---------|------------------|------------|\n| Only one model | LLaMA-3.3-70B replication | exp-012 |\n| Cross-task replication | Pairwise: Few-NERD ✓ + MAVEN MiniLM ✓. Batch: FewRel ✓. Three tasks. | exp-002, exp-004, fewrel |\n| No practical method | SDGD framework (-zero, -cal) | exp-008 to exp-011 |\n| Confusability measure validity | Embedding ablation (D010) + pairwise vs per-type analysis | D010, exp-015 |\n| Effect size small | Pairwise r=0.12-0.16 + FewRel Δ=21-50pp + confusion ratio 10-28x | multiple |\n| MAVEN per-type opposite | Centrality confound analysis; pairwise still works | MAVEN MiniLM |\n| Embedding choice matters? | 2×3 ablation table; SDGD-cal bypasses embedding entirely | D010 |\n| Why not per-type splitting? | SDGD vs per-type vs random ablation | exp-013, exp-014 |\n| Latency overhead | Report API calls and wall-clock time | exp-008 |\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  description: 'Count curve baseline: recall/precision/F1 across type counts [1,2,6,12,22,44,66]\n    on Few-NERD with Qwen3-32B-FP8'\n  priority: P0\n  gpu_budget_hours: 3.5\n  deps: []\n  registry_id: exp001_count_baseline\n  status_note: DONE. Recall 0.72->0.42 monotonic. WrongType 0->2434. Over-prediction\n    at low counts.\n  status: DONE\n  conclusion: success\n  metrics:\n    diagnosis: char offset 96.5% fabricated by model\n    text_match_reeval:\n      count_1:\n        f1: 0.184\n        precision: 0.105\n        recall: 0.72\n        pred_gold_ratio: 6.85\n      count_2:\n        f1: 0.123\n        precision: 0.068\n        recall: 0.698\n        pred_gold_ratio: 10.33\n      count_6:\n        f1: 0.155\n        precision: 0.088\n        recall: 0.62\n        pred_gold_ratio: 7.02\n      count_12:\n        f1: 0.246\n        precision: 0.16\n        recall: 0.539\n        pred_gold_ratio: 3.38\n      count_22:\n        f1: 0.322\n        precision: 0.232\n        recall: 0.527\n        pred_gold_ratio: 2.27\n      count_44:\n        f1: 0.473\n        precision: 0.414\n        recall: 0.551\n        pred_gold_ratio: 1.33\n      count_64:\n        f1: 0.463\n        precision: 0.52\n        recall: 0.418\n        pred_gold_ratio: 0.8\n    key_finding: recall monotonically decreases (0.72→0.42), precision monotonically\n      increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at\n      count_44\n    wrong_type_trend: 'type confusion increases with count: 0→2434, supports confusability\n      hypothesis'\n    spurious_dominant: spurious FPs (text in source but not entity) dominate at low\n      count, not hallucination\n    conclusion_text_match: F1 curve inversion caused by over-prediction confound,\n      NOT absence of confusability effect. Recall curve + type confusion pattern support\n      hypothesis.\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: 'Confusability controlled: within-count r(metric, BCS) at count=6/12,\n    25 random + extreme batches on Few-NERD'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  registry_id: exp002_confusability_controlled\n  status_note: DONE. Partial r=0.303 (p=0.026), count_12 r=0.501 (p=0.008). Confusion\n    rate 10-28x.\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp2_reeval_results.json (text_match, CLEAN)\n    primary_recall_vs_bcs:\n      count_6:\n        r: 0.2754\n        p: 0.1644\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.2219\n        p: 0.266\n        n: 27\n        verdict: FAIL\n      partial:\n        r: 0.2522\n        p: 0.0658\n        n: 54\n        verdict: FAIL\n    secondary_f1_vs_bcs:\n      count_6:\n        r: 0.1754\n        p: 0.3814\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.5012\n        p: 0.0077\n        n: 27\n        verdict: PASS\n      partial:\n        r: 0.3025\n        p: 0.0262\n        n: 54\n        verdict: PASS\n    mechanistic_confusion_rate:\n      random_batches:\n        count_6_high: 0.0157\n        count_6_low: 0.0088\n        ratio_6: 1.7\n        count_12_high: 0.0304\n        count_12_low: 0.0131\n        ratio_12: 2.4\n      extreme_batches:\n        count_6_high: 0.0728\n        count_6_low: 0.0014\n        ratio_6: 27.5\n        count_12_high: 0.048\n        count_12_low: 0.0061\n        ratio_12: 9.9\n      verdict: PASS\n    pairwise_confusion_analysis:\n      all:\n        n_pairs: 1953\n        pearson_r: 0.156\n        pearson_p: 4.6e-12\n        spearman_rho: 0.16\n        spearman_p: 1.3e-12\n      count_6:\n        n_pairs: 1770\n        pearson_r: 0.078\n        pearson_p: 0.001\n      count_12:\n        n_pairs: 1953\n        pearson_r: 0.147\n        pearson_p: 6.7e-11\n      nonzero_only:\n        all_spearman_rho: 0.254\n        all_spearman_p: 1.1e-06\n        count_12_pearson_r: 0.212\n        count_12_p: 0.00034\n      top_confused_pair: person-other <-> person-politician (BCS=0.934, confusion=156)\n    per_type_analysis:\n      n_types: 63\n      filter: freq>=5\n      micro_f1_vs_bcs:\n        pearson_r: -0.1828\n        pearson_p: 0.1516\n        spearman_rho: -0.2927\n        spearman_p: 0.0199\n        partial_r_ctrl_logfreq: -0.1998\n        partial_p: 0.1163\n      mean_f1_vs_bcs:\n        pearson_r: -0.1374\n        pearson_p: 0.283\n        spearman_rho: -0.2412\n        spearman_p: 0.0568\n        partial_r_ctrl_logfreq: -0.1428\n        partial_p: 0.2641\n      quartile_comparison:\n        low_bcs_cutoff: 0.798\n        high_bcs_cutoff: 0.827\n        low_bcs_f1: 0.3098\n        high_bcs_f1: 0.2275\n        delta_f1: -0.0823\n        low_bcs_freq: 2134\n        high_bcs_freq: 2049\n      confound_check:\n        bcs_vs_logfreq_r: 0.042\n        bcs_vs_logfreq_p: 0.74\n        logfreq_vs_f1_r: 0.25\n        logfreq_vs_f1_p: 0.048\n      verdict: Direction supports hypothesis. Spearman significant (p=0.02). Frequency\n        confound absent at type level (r=0.04).\n    overall_verdict: PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE\n      STRONG PASS, PER-TYPE DIRECTIONAL PASS\n- id: exp-003a\n  claim:\n  - 1\n  - 2\n  description: 'Prompt v2 rerun: clean data without offset fabrication, anti-hallucination\n    instruction. Re-run exp1+exp2.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  - exp-002\n  registry_id: exp003a_prompt_v2_rerun\n  status_note: FAILED (EXIT_CODE=2 syntax error). Needs fix and re-run.\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_mode: text_match\n    exp1_text_match:\n      count_1:\n        f1: 0.323\n        precision: 0.216\n        recall: 0.641\n        pred_gold_ratio: 2.97\n        n_batches: 64\n      count_2:\n        f1: 0.273\n        precision: 0.18\n        recall: 0.56\n        pred_gold_ratio: 3.11\n        n_batches: 5\n      count_6:\n        f1: 0.306\n        precision: 0.226\n        recall: 0.475\n        pred_gold_ratio: 2.1\n        n_batches: 5\n      count_12:\n        f1: 0.347\n        precision: 0.367\n        recall: 0.329\n        pred_gold_ratio: 0.9\n        n_batches: 5\n      count_22:\n        f1: 0.299\n        precision: 0.339\n        recall: 0.267\n        pred_gold_ratio: 0.79\n        n_batches: 5\n      count_44:\n        f1: 0.445\n        precision: 0.506\n        recall: 0.396\n        pred_gold_ratio: 0.78\n        n_batches: 5\n      count_64:\n        f1: 0.414\n        precision: 0.648\n        recall: 0.304\n        pred_gold_ratio: 0.47\n        n_batches: 5\n    exp2_text_match:\n      count_6:\n        f1: 0.32\n        precision: 0.26\n        recall: 0.416\n        pred_gold_ratio: 1.6\n        n_batches: 27\n      count_12:\n        f1: 0.306\n        precision: 0.291\n        recall: 0.323\n        pred_gold_ratio: 1.11\n        n_batches: 27\n    vs_exp001_delta:\n      count_1:\n        f1_delta: +0.139 (+76%)\n        precision_delta: +0.111 (+106%)\n        recall_delta: -0.079 (-11%)\n        overpred_fix: 6.85→2.97\n      count_6:\n        f1_delta: +0.151 (+97%)\n        precision_delta: +0.138 (+157%)\n        recall_delta: -0.145 (-23%)\n      count_12:\n        f1_delta: +0.101 (+41%)\n        precision_delta: +0.207 (+129%)\n        recall_delta: -0.210 (-39%)\n      count_44:\n        f1_delta: -0.028 (-6%)\n        precision_delta: +0.092 (+22%)\n        recall_delta: -0.155 (-28%)\n      count_64:\n        f1_delta: -0.049 (-11%)\n        precision_delta: +0.128 (+25%)\n        recall_delta: -0.114 (-27%)\n    key_finding: 'V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x\n      to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1).\n      But over-corrected at high counts: under-prediction (pred/gold<1) caused recall\n      drops of 27-39%, slightly lowering F1 at count_22-64.'\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MAVEN confusability study: count curve + within-count BCS correlation\n    on MAVEN Event Detection (168 event types, FrameNet hierarchy). Replicates core\n    finding cross-task (NER→ED) with larger type space and known sibling confusion\n    (14.6-19.8%).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp-004\n  status_note: 'DONE (success). MAVEN count curve replicated. Also: exp004_maven_bcs\n    (negative) — BCS within-count correlation weaker on MAVEN due to FrameNet hierarchy\n    structure.'\n  status: DONE\n  conclusion: success\n  metrics:\n    n_event_types: 168\n    n_pairs: 14028\n    scs_mean: 0.2161\n    scs_std: 0.103\n    scs_max: 0.8368\n    scs_median: 0.2121\n    scs_q90: 0.3457\n    scs_q95: 0.3892\n    pairs_above_0.5: 119\n    pct_above_0.5: 0.85\n    train_docs: 2913\n    train_mentions: 77993\n    valid_docs: 710\n    valid_mentions: 18904\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  description: 'DocRED confusability study: count curve + BCS correlation on DocRED\n    (96 relation types). Scaling stress test.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003a\n  status: planned\n- id: exp-006\n  claim:\n  - 2\n  description: 'Interaction effect 2x2: {low count, high count} x {low BCS, high BCS}\n    on Few-NERD. Tests additive vs multiplicative interaction between count and confusability.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-003a\n  status: planned\n- id: exp-007\n  claim:\n  - 2\n  description: 'Error taxonomy: systematic FP classification (type_substitution /\n    boundary_error / false_negative / hallucination) across BCS bins. Mechanistic\n    evidence for multi-channel model.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-002\n  status_note: Partially done via reeval_text_match.py FP three-way. Needs systematic\n    BCS-binned analysis.\n  status: planned\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'Multi-model validation: replicate exp-002 protocol with >=1 additional\n    model (candidate: Qwen2.5-72B-Instruct or LLaMA-3.3-70B-Instruct). Addresses single-model\n    generalizability.'\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-003a\n  registry_id: exp012_llama_fewnerd\n  status: QUEUED\n- id: exp-016\n  claim:\n  - 1\n  - 2\n  description: 'FewRel cross-task replication: count curve + BCS correlation on FewRel\n    RE (80 relation types with --use_all). Replicates confusability effect NER→RE.\n    Pilot (fewrel_pilot) confirmed signal; formal run with full count curve [1,4,8,16,32,64,80].'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-003a\n  registry_id: exp_fewrel_formal\n  status_note: RUNNING (16-rel version). Will rerun with --use_all for 80-rel full\n    count curve after current run completes.\n  status: DONE\n  conclusion: success\n  metrics:\n    note: 16-rel sanity check only\n    exp1:\n      count_1:\n        mean_acc: 0.904\n        n_batches: 16\n      count_4:\n        mean_acc: 0.932\n        n_batches: 5\n      count_8:\n        mean_acc: 0.867\n        n_batches: 5\n      count_16:\n        mean_acc: 0.778\n        n_batches: 5\n        bcs: 0.9\n        zero_variance: true\n    exp2:\n      count_8_low_bcs:\n        acc: 0.889\n        bcs: 0.782\n      count_8_high_bcs:\n        acc: 0.798\n        bcs: 0.892\n      delta_bcs_effect: -0.091\n    trend: 'count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8%\n      (Δ=-9.1pp)'\n- id: exp-008\n  claim:\n  - 3\n  description: 'SDGD-zero on Few-NERD: confusability-minimizing batch composition\n    via embedding SCS + graph coloring. Compare vs single-pass full-schema baseline.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-003a\n  registry_id: exp008_sdgd_zero_fewnerd_r2\n  status_note: 'DONE (negative). R2 attempt: SDGD-zero did not outperform single-pass\n    baseline on Few-NERD. R1 (exp008_sdgd_zero_fewnerd) failed with script error.'\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 77.3\n    sdgd_zero:\n      f1: 0.2514\n      precision: 0.2096\n      recall: 0.3141\n      batches: 8\n      time_s: 408.7\n    random_batch:\n      f1: 0.3197\n      precision: 0.2491\n      recall: 0.4462\n      batches: 8\n      time_s: 476.1\n    per_type:\n      f1: 0.2915\n      precision: 0.194\n      recall: 0.5856\n      batches: 66\n      time_s: 2532.2\n    key_finding: All decomposition modes F1 < single_pass. Decomposition boosts recall\n      but kills precision (merge amplification). sdgd_zero worst F1, even below random_batch.\n- id: exp-009\n  claim:\n  - 3\n  description: 'SDGD-zero on MAVEN: confusability-minimizing batch composition on\n    168 event types. Compare vs single-pass + random batching. Cross-task validation\n    of SDGD framework (NER→ED).'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-004\n  - exp-008\n  status: planned\n- id: exp-010\n  claim:\n  - 3\n  description: 'SDGD-cal on Few-NERD: empirical confusability from 5-10 calibration\n    examples (no gradients). Compare vs SDGD-zero.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-008\n  status: planned\n- id: exp-011\n  claim:\n  - 3\n  description: 'SDGD-cal on MAVEN: empirical confusability with calibration on 168\n    event types. Full comparison table.'\n  priority: P1\n  gpu_budget_hours: 4\n  deps:\n  - exp-009\n  - exp-010\n  status: planned\n- id: exp-013\n  claim:\n  - 3\n  description: 'Ablation: random batching -- same batch count k as SDGD, random composition.\n    Isolates confusability-aware grouping from batch count reduction.'\n  priority: P0\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n  status: planned\n- id: exp-014\n  claim:\n  - 3\n  description: 'Ablation: per-type splitting (UniNER-style, 1 type per batch). Upper\n    bound on decomposition benefit. Reveals latency vs quality tradeoff.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-008\n  status: planned\n- id: exp-015\n  claim:\n  - 1\n  description: 'SCS validation: Spearman/Kendall rank correlation between embedding\n    SCS and empirical confusion matrix. Validates embedding proxy for practical use.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-010\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: exp001_count_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    diagnosis: char offset 96.5% fabricated by model\n    text_match_reeval:\n      count_1:\n        f1: 0.184\n        precision: 0.105\n        recall: 0.72\n        pred_gold_ratio: 6.85\n      count_2:\n        f1: 0.123\n        precision: 0.068\n        recall: 0.698\n        pred_gold_ratio: 10.33\n      count_6:\n        f1: 0.155\n        precision: 0.088\n        recall: 0.62\n        pred_gold_ratio: 7.02\n      count_12:\n        f1: 0.246\n        precision: 0.16\n        recall: 0.539\n        pred_gold_ratio: 3.38\n      count_22:\n        f1: 0.322\n        precision: 0.232\n        recall: 0.527\n        pred_gold_ratio: 2.27\n      count_44:\n        f1: 0.473\n        precision: 0.414\n        recall: 0.551\n        pred_gold_ratio: 1.33\n      count_64:\n        f1: 0.463\n        precision: 0.52\n        recall: 0.418\n        pred_gold_ratio: 0.8\n    key_finding: recall monotonically decreases (0.72→0.42), precision monotonically\n      increases (0.11→0.52) due to over-prediction reduction. F1 inverted-U peak at\n      count_44\n    wrong_type_trend: 'type confusion increases with count: 0→2434, supports confusability\n      hypothesis'\n    spurious_dominant: spurious FPs (text in source but not entity) dominate at low\n      count, not hallucination\n    conclusion_text_match: F1 curve inversion caused by over-prediction confound,\n      NOT absence of confusability effect. Recall curve + type confusion pattern support\n      hypothesis.\n- exp_id: exp002_confusability_controlled\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    data_source: exp2_reeval_results.json (text_match, CLEAN)\n    primary_recall_vs_bcs:\n      count_6:\n        r: 0.2754\n        p: 0.1644\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.2219\n        p: 0.266\n        n: 27\n        verdict: FAIL\n      partial:\n        r: 0.2522\n        p: 0.0658\n        n: 54\n        verdict: FAIL\n    secondary_f1_vs_bcs:\n      count_6:\n        r: 0.1754\n        p: 0.3814\n        n: 27\n        verdict: FAIL\n      count_12:\n        r: 0.5012\n        p: 0.0077\n        n: 27\n        verdict: PASS\n      partial:\n        r: 0.3025\n        p: 0.0262\n        n: 54\n        verdict: PASS\n    mechanistic_confusion_rate:\n      random_batches:\n        count_6_high: 0.0157\n        count_6_low: 0.0088\n        ratio_6: 1.7\n        count_12_high: 0.0304\n        count_12_low: 0.0131\n        ratio_12: 2.4\n      extreme_batches:\n        count_6_high: 0.0728\n        count_6_low: 0.0014\n        ratio_6: 27.5\n        count_12_high: 0.048\n        count_12_low: 0.0061\n        ratio_12: 9.9\n      verdict: PASS\n    pairwise_confusion_analysis:\n      all:\n        n_pairs: 1953\n        pearson_r: 0.156\n        pearson_p: 4.6e-12\n        spearman_rho: 0.16\n        spearman_p: 1.3e-12\n      count_6:\n        n_pairs: 1770\n        pearson_r: 0.078\n        pearson_p: 0.001\n      count_12:\n        n_pairs: 1953\n        pearson_r: 0.147\n        pearson_p: 6.7e-11\n      nonzero_only:\n        all_spearman_rho: 0.254\n        all_spearman_p: 1.1e-06\n        count_12_pearson_r: 0.212\n        count_12_p: 0.00034\n      top_confused_pair: person-other <-> person-politician (BCS=0.934, confusion=156)\n    per_type_analysis:\n      n_types: 63\n      filter: freq>=5\n      micro_f1_vs_bcs:\n        pearson_r: -0.1828\n        pearson_p: 0.1516\n        spearman_rho: -0.2927\n        spearman_p: 0.0199\n        partial_r_ctrl_logfreq: -0.1998\n        partial_p: 0.1163\n      mean_f1_vs_bcs:\n        pearson_r: -0.1374\n        pearson_p: 0.283\n        spearman_rho: -0.2412\n        spearman_p: 0.0568\n        partial_r_ctrl_logfreq: -0.1428\n        partial_p: 0.2641\n      quartile_comparison:\n        low_bcs_cutoff: 0.798\n        high_bcs_cutoff: 0.827\n        low_bcs_f1: 0.3098\n        high_bcs_f1: 0.2275\n        delta_f1: -0.0823\n        low_bcs_freq: 2134\n        high_bcs_freq: 2049\n      confound_check:\n        bcs_vs_logfreq_r: 0.042\n        bcs_vs_logfreq_p: 0.74\n        logfreq_vs_f1_r: 0.25\n        logfreq_vs_f1_p: 0.048\n      verdict: Direction supports hypothesis. Spearman significant (p=0.02). Frequency\n        confound absent at type level (r=0.04).\n    overall_verdict: PRIMARY FAIL, SECONDARY PARTIAL PASS, MECHANISTIC PASS, PAIRWISE\n      STRONG PASS, PER-TYPE DIRECTIONAL PASS\n- exp_id: exp003a_prompt_v2_rerun\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_mode: text_match\n    exp1_text_match:\n      count_1:\n        f1: 0.323\n        precision: 0.216\n        recall: 0.641\n        pred_gold_ratio: 2.97\n        n_batches: 64\n      count_2:\n        f1: 0.273\n        precision: 0.18\n        recall: 0.56\n        pred_gold_ratio: 3.11\n        n_batches: 5\n      count_6:\n        f1: 0.306\n        precision: 0.226\n        recall: 0.475\n        pred_gold_ratio: 2.1\n        n_batches: 5\n      count_12:\n        f1: 0.347\n        precision: 0.367\n        recall: 0.329\n        pred_gold_ratio: 0.9\n        n_batches: 5\n      count_22:\n        f1: 0.299\n        precision: 0.339\n        recall: 0.267\n        pred_gold_ratio: 0.79\n        n_batches: 5\n      count_44:\n        f1: 0.445\n        precision: 0.506\n        recall: 0.396\n        pred_gold_ratio: 0.78\n        n_batches: 5\n      count_64:\n        f1: 0.414\n        precision: 0.648\n        recall: 0.304\n        pred_gold_ratio: 0.47\n        n_batches: 5\n    exp2_text_match:\n      count_6:\n        f1: 0.32\n        precision: 0.26\n        recall: 0.416\n        pred_gold_ratio: 1.6\n        n_batches: 27\n      count_12:\n        f1: 0.306\n        precision: 0.291\n        recall: 0.323\n        pred_gold_ratio: 1.11\n        n_batches: 27\n    vs_exp001_delta:\n      count_1:\n        f1_delta: +0.139 (+76%)\n        precision_delta: +0.111 (+106%)\n        recall_delta: -0.079 (-11%)\n        overpred_fix: 6.85→2.97\n      count_6:\n        f1_delta: +0.151 (+97%)\n        precision_delta: +0.138 (+157%)\n        recall_delta: -0.145 (-23%)\n      count_12:\n        f1_delta: +0.101 (+41%)\n        precision_delta: +0.207 (+129%)\n        recall_delta: -0.210 (-39%)\n      count_44:\n        f1_delta: -0.028 (-6%)\n        precision_delta: +0.092 (+22%)\n        recall_delta: -0.155 (-28%)\n      count_64:\n        f1_delta: -0.049 (-11%)\n        precision_delta: +0.128 (+25%)\n        recall_delta: -0.114 (-27%)\n    key_finding: 'V2 prompt dramatically reduced over-prediction (pred/gold from 6.85x\n      to 2.97x at count_1), boosting precision and F1 at low counts (+76% F1 at count_1).\n      But over-corrected at high counts: under-prediction (pred/gold<1) caused recall\n      drops of 27-39%, slightly lowering F1 at count_22-64.'\n- exp_id: exp-004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_event_types: 168\n    n_pairs: 14028\n    scs_mean: 0.2161\n    scs_std: 0.103\n    scs_max: 0.8368\n    scs_median: 0.2121\n    scs_q90: 0.3457\n    scs_q95: 0.3892\n    pairs_above_0.5: 119\n    pct_above_0.5: 0.85\n    train_docs: 2913\n    train_mentions: 77993\n    valid_docs: 710\n    valid_mentions: 18904\n- exp_id: exp004_maven_bcs\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    exp1_count_curve:\n      count_1:\n        n_batches: 64\n        exact_f1: 0.009\n        relaxed_f1: 0.106\n        bcs: 0\n      count_6:\n        n_batches: 5\n        exact_f1: 0.003\n        relaxed_f1: 0.103\n        bcs: 0.892\n      count_12:\n        n_batches: 5\n        exact_f1: 0.008\n        relaxed_f1: 0.146\n        bcs: 0.921\n      count_22:\n        n_batches: 5\n        exact_f1: 0.013\n        relaxed_f1: 0.185\n        bcs: 0.933\n      count_44:\n        n_batches: 5\n        exact_f1: 0.018\n        relaxed_f1: 0.247\n        bcs: 0.967\n      count_64:\n        n_batches: 5\n        exact_f1: 0.013\n        relaxed_f1: 0.245\n        bcs: 0.973\n    exp2_bcs_controlled:\n      count_6_high_bcs:\n        exact_f1: 0.0354\n        relaxed_f1: 0.211\n        bcs: 0.9447\n      count_6_low_bcs:\n        exact_f1: 0.0068\n        relaxed_f1: 0.089\n        bcs: 0.8709\n      count_12_high_bcs:\n        exact_f1: 0.0151\n        relaxed_f1: 0.1568\n        bcs: 0.9447\n      count_12_low_bcs:\n        exact_f1: 0.0068\n        relaxed_f1: 0.105\n        bcs: 0.9148\n    key_finding: 'MAVEN batch-level: high_bcs relaxed_F1 2.4x vs low_bcs (count_6).\n      Direction same as Few-NERD batch-level (positive). Pairwise + per-type analysis\n      needed to control frequency confound.'\n    note: exact_F1 very low (0.003-0.035), relaxed_F1 usable (0.089-0.247). Event\n      trigger boundary matching is fuzzy. A re-run (500 samples) is still in progress\n      in artifacts/exp004/.\n- exp_id: fewrel_pilot\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    embedding: all-MiniLM-L6-v2\n    n_batches: 15\n    n_predictions: 374\n    count_4:\n      low_bcs_acc: 0.917\n      high_bcs_acc: 0.708\n      delta_pp: -20.9\n      low_bcs: 0.42\n      high_bcs: 0.97\n    count_8:\n      low_bcs_acc: 1\n      high_bcs_acc: 0.5\n      delta_pp: -50\n      low_bcs: 0.47\n      high_bcs: 0.97\n    count_16:\n      low_bcs_acc: 0.917\n      high_bcs_acc: 0.431\n      delta_pp: -48.6\n      low_bcs: 0.57\n      high_bcs: 0.97\n    key_finding: 'BCS-accuracy strong negative: high-BCS batches 43-71% vs low-BCS\n      92-100%. Effect increases with count. Cross-task (NER→RE) replication of confusability\n      hypothesis.'\n- exp_id: exp008_sdgd_zero_fewnerd\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: exp008_sdgd_zero_fewnerd_r2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    single_pass:\n      f1: 0.4451\n      precision: 0.5631\n      recall: 0.3679\n      batches: 1\n      time_s: 77.3\n    sdgd_zero:\n      f1: 0.2514\n      precision: 0.2096\n      recall: 0.3141\n      batches: 8\n      time_s: 408.7\n    random_batch:\n      f1: 0.3197\n      precision: 0.2491\n      recall: 0.4462\n      batches: 8\n      time_s: 476.1\n    per_type:\n      f1: 0.2915\n      precision: 0.194\n      recall: 0.5856\n      batches: 66\n      time_s: 2532.2\n    key_finding: All decomposition modes F1 < single_pass. Decomposition boosts recall\n      but kills precision (merge amplification). sdgd_zero worst F1, even below random_batch.\n- exp_id: exp_fewrel_formal\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    note: 16-rel sanity check only\n    exp1:\n      count_1:\n        mean_acc: 0.904\n        n_batches: 16\n      count_4:\n        mean_acc: 0.932\n        n_batches: 5\n      count_8:\n        mean_acc: 0.867\n        n_batches: 5\n      count_16:\n        mean_acc: 0.778\n        n_batches: 5\n        bcs: 0.9\n        zero_variance: true\n    exp2:\n      count_8_low_bcs:\n        acc: 0.889\n        bcs: 0.782\n      count_8_high_bcs:\n        acc: 0.798\n        bcs: 0.892\n      delta_bcs_effect: -0.091\n    trend: 'count↑ → accuracy↓ confirmed. BCS effect: low-BCS 88.9% vs high-BCS 79.8%\n      (Δ=-9.1pp)'\n- exp_id: exp_fewrel_formal_80rel\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_count_curve:\n      count_1:\n        acc: 0.8573\n        n_batches: 80\n        bcs: 0\n      count_4:\n        acc: 0.8667\n        n_batches: 5\n        bcs: 0.6335\n      count_8:\n        acc: 0.8021\n        n_batches: 5\n        bcs: 0.7175\n      count_16:\n        acc: 0.6958\n        n_batches: 5\n        bcs: 0.795\n      count_32:\n        acc: 0.6578\n        n_batches: 5\n        bcs: 0.8893\n      count_64:\n        acc: 0.5424\n        n_batches: 5\n        bcs: 0.9434\n      count_80:\n        acc: 0.5042\n        n_batches: 5\n        bcs: 0.9706\n    exp2_bcs_controlled:\n      count_8:\n        low_bcs_acc: 0.8229\n        low_bcs: 0.4715\n        high_bcs_acc: 0.5104\n        high_bcs: 0.9706\n        random_acc: 0.8025\n        delta_pp: -31.2\n      count_16:\n        low_bcs_acc: 0.8281\n        low_bcs: 0.5705\n        high_bcs_acc: 0.5156\n        high_bcs: 0.9706\n        random_acc: 0.7169\n        delta_pp: -31.2\n    vs_16rel:\n      degradation_16rel: -12.6pp (0.904→0.778)\n      degradation_80rel: -35.3pp (0.857→0.504)\n      bcs_effect_16rel: -9.1pp\n      bcs_effect_80rel: -31.2pp\n      amplification: 3.4x\n    key_finding: 80-rel count curve 0.857→0.504 (degradation 35.3pp, 远强于 16-rel 12.6pp).\n      BCS effect -31.2pp (3.4x amplification vs 16-rel). 更多 relations → 更大 confusion\n      space → 更强 degradation + BCS effect.\n- exp_id: exp008_sdgd_v2_fewnerd\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp012_llama_fewnerd\n  name: ''\n  status: QUEUED\n  conclusion: ''\n  metrics: {}\n- exp_id: exp007_error_taxonomy\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    exp1_random:\n      bcs_zero:\n        n_fp: 6172\n        intra_sub_pct: 0\n        extra_sub_pct: 90.3\n        intra_sub_per_100_gold: 0\n      bcs_low:\n        n_fp: 2231\n        intra_sub_pct: 1.6\n        extra_sub_pct: 89.9\n        intra_sub_per_100_gold: 3.4\n      bcs_medium:\n        n_fp: 3843\n        intra_sub_pct: 10.6\n        extra_sub_pct: 78.1\n        intra_sub_per_100_gold: 6.47\n      bcs_high:\n        n_fp: 6188\n        intra_sub_pct: 49.4\n        extra_sub_pct: 30.8\n        intra_sub_per_100_gold: 12.93\n    correlation:\n      intra_sub_vs_bcs_spearman_rho: 1\n      intra_sub_vs_bcs_p: <0.001\n      chi_square: 6952\n      chi_square_p: ~0\n    exp2_controlled:\n      trend: IntraSub 3.2% -> 7.3% -> 8.6% (rho=1.0, p<0.001)\n    key_finding: 'BCS>=0.95: 49.4% FP are intra-batch type confusion (13/100 gold).\n      Hallucination+boundary <3%. LLM main error mode is type confusion, not hallucination.'\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T14:08:37.750Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T14:08:37.750Z",
  "sessionId": "263d3c39-27c7-4994-a66d-4427b1b10f55"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-15T14:08:37.771Z_

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
focus: 80-rel FewRel formal results now available (Δ=-31.2pp, 3.4x scaling). SDGD-zero negative (exp-008). exp-012 multi-model in progress. Evaluate whether Claim 3 (SDGD) should pivot to analysis-only paper or attempt SDGD v2.

## paper_framing.md

# Paper Framing — schema-dag-extraction

## Target Venue
- Primary: EMNLP 2026 Main (ARR May 25 cycle)
- Commitment deadline: August 2, 2026
- Fallback: EMNLP 2026 Findings (same ARR cycle, commitment August 26)
- Deadline: ARR May 25, 2026 (10 days from today)

## Core Claims (3 conditions) — Revised per D012

1. **Confusability Independence**: Type confusability independently predicts extraction quality degradation in training-free LLM IE, beyond what type count alone explains. The signal is strongest and most robust at the **type-pair level** (pairwise SCS → confusion), validated across NER (Few-NERD), RE (FewRel), and ED (MAVEN with MiniLM). Per-type aggregation (mean BCS) introduces a centrality confound in semantically homogeneous schemas. Evidence required: (a) significant pairwise SCS-confusion correlation on >=2 datasets, (b) extreme-batch accuracy gap on FewRel, (c) >=2 models.

2. **Multi-Channel Degradation**: Count and confusability degrade extraction through orthogonal channels -- count causes entity omission (recall decline), while confusability causes type confusion errors (correct spans labeled with wrong types). Evidence required: error taxonomy showing differential error types per channel, monotonic trends in separate metrics.

3. **SDGD Effectiveness**: Confusability-aware schema decomposition (SDGD) -- partitioning types into low-confusability batches via graph coloring on the pairwise-similarity-thresholded graph -- yields significant F1 gains over single-pass and heuristic decomposition on complex schemas (>=30 types). SDGD directly leverages pairwise confusability (validated signal), avoiding per-type aggregation confounds. Evidence required: SDGD > single-pass, SDGD > random batching (same k), SDGD >= per-type splitting (with lower latency).

## Story Spine — Revised per D012

- **Problem**: Training-free LLM IE degrades severely on complex schemas (20-60 F1 gap vs supervised). All existing decomposition approaches operate on unvalidated assumptions about WHAT makes schemas complex for LLMs.

- **Existing approaches & their gaps**: UniNER splits per-type (gains 3.3 F1 but loses cross-type context, no criterion for when to split). LLM-PEE uses similarity as implicit confusability proxy (never validated empirically). No prior work isolates confusability from count, or characterizes when aggregated confusability measures lose signal.

- **Our framing**: We conduct the first controlled empirical study isolating type confusability from type count in training-free LLM IE across three tasks (NER, RE, ED). We discover: (1) a multi-channel degradation model (count→recall, confusability→type confusion), (2) pairwise type confusability is a robust cross-task signal, (3) per-type aggregation of confusability is confounded by type centrality in homogeneous schemas. We operationalize pairwise confusability into SDGD, a principled framework for confusability-minimizing schema decomposition.

- **Three-task validation**:
  - NER (Few-NERD, 66 types, cross-domain): Pairwise r=0.156 (p<1e-11), per-type ρ=-0.293 (p=0.02), 10-28x confusion ratio
  - RE (FewRel, 80 relations, cross-domain): BCS-controlled Δ=-31.2pp (80-rel formal); count curve acc 85.7%→50.4%; BCS effect scales 3.4x vs 16-rel
  - ED (MAVEN, 168 event types, same-domain): Pairwise MiniLM r=0.120 (p≈0); per-type positive (centrality confound case study)

- **Headline result template**: "Pairwise type confusability independently predicts extraction degradation across NER, RE, and ED tasks (r=0.12-0.16, p<1e-6), with 10-28x more type confusion errors in high-confusability batches. On semantically homogeneous schemas, per-type aggregation obscures the signal through centrality confounding, but pairwise confusability remains valid. SDGD-zero, operating on pairwise similarity, improves F1 by X points over single-pass on Few-NERD."

## Core Insight — Multi-Channel Degradation + Pairwise Robustness

Schema-induced degradation in LLM IE is not a single phenomenon but a multi-channel process:
- **Channel 1 (Count -> Recall)**: More types in the prompt → attention dilution → entities missed. Monotonic, near-linear. Addressable by reducing batch size.
- **Channel 2 (Confusability -> Type Confusion)**: Semantically similar co-present types → interference during type assignment → correct entities labeled with wrong types. Addressable by separating confusable types into different batches.

These channels are orthogonal and independently addressable.

**Pairwise vs Aggregated Confusability**:
- **Pairwise confusability** (SCS between type pairs) is robust across all tasks and schema types. Validated on Few-NERD (Qwen3, r=0.156) and MAVEN (MiniLM, r=0.120).
- **Per-type aggregation** (mean BCS = average pairwise similarity to all other types) introduces a centrality confound: in semantically homogeneous schemas (MAVEN), types with many semantic neighbors are central, well-represented types that LLMs extract well → positive correlation (high mean BCS → high F1), masking the pairwise confusability signal.
- **SDGD operates at pairwise level**, directly using the validated signal to construct the confusability graph for decomposition. It avoids the aggregation confound entirely.

## Evidence Hierarchy (D012)

### Tier 1: PRIMARY — Pairwise SCS → Confusion

The cleanest evidence. Directly measures: are semantically similar type pairs more often confused?

**Few-NERD (NER)** — Qwen3 embeddings:
- Pearson r=0.156 (p=4.6e-12, n=1953 type pairs)
- Nonzero-only Spearman ρ=0.254 (p=1.1e-6)
- Top confused pairs are all high-BCS semantic neighbors (person-other ↔ person-politician, BCS=0.934)
- Immune to type frequency confound (operates at type-pair level)

**MAVEN (ED)** — MiniLM embeddings:
- Pearson r=+0.120 (p≈0, n=11026 type pairs)
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

### Tier 5: MECHANISTIC — Error Taxonomy

Confusion rate differential demonstrates the mechanism:
- Extreme batches: high-BCS 10-28x more type confusion errors vs low-BCS
- Random batches: 1.7-2.4x ratio (still significant, smaller effect)
- Type confusion errors increase with count AND with confusability (additive)

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
| Qwen3 | r=0.156 ✓ | r=-0.007 ✗ |
| MiniLM | — | r=+0.120 ✓ |

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
  registry_id: exp012_llama_fewnerd
  status: QUEUED
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
  registry_id: exp008_sdgd_zero_fewnerd_r2
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
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp012_llama_fewnerd
  name: ''
  status: QUEUED
  conclusion: ''
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
  "promptId": "27c0e228-a26d-49e4-a204-4ebc150acb0a",
  "type": "user",
  "uuid": "7f908cb2-79f1-444f-9ae4-93e5dd1d5551",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "263d3c39-27c7-4994-a66d-4427b1b10f55",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T14:08:37.769Z_

```json
{
  "parentUuid": "7f908cb2-79f1-444f-9ae4-93e5dd1d5551",
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
  "uuid": "38652622-e9fc-4784-a482-c911031771e4",
  "timestamp": "2026-05-15T14:08:37.769Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "263d3c39-27c7-4994-a66d-4427b1b10f55",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T14:08:37.769Z_

```json
{
  "parentUuid": "38652622-e9fc-4784-a482-c911031771e4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4dde5d40-cc6a-4b2b-bf4f-918710559b1f",
  "timestamp": "2026-05-15T14:08:37.769Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "263d3c39-27c7-4994-a66d-4427b1b10f55",
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
  "leafUuid": "4dde5d40-cc6a-4b2b-bf4f-918710559b1f",
  "sessionId": "263d3c39-27c7-4994-a66d-4427b1b10f55"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-scenario Dream model for schema-dag extraction",
  "sessionId": "263d3c39-27c7-4994-a66d-4427b1b10f55"
}
```

---

### Assistant

_source line 8 · 2026-05-15T14:09:07.717Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the research context carefully to define three tiers of Dream simulation scenarios.

Key facts from the data:

**Claim 1 (Confusability Independence)** - STRONG
- Pairwise SCS→confusion: Few-NERD r=0.156 (p<1e-11), MAVEN MiniLM r=0.120 (p≈0) — both significant
- Per-type: Few-NERD ρ=-0.293 (p=0.02), MAVEN positive (centrality confound)
- FewRel 80-rel: Δ=-31.2pp, 3.4x scaling


- Confusion ratio reaches 10-28x in extreme batches

**Claim 2 (Multi-Channel Degradation)** - STRONG
- Count→recall shows consistent monotonic decline
- Confusability→type confusion: error taxonomy reveals BCS≥0.95 correlates with 49.4% intra-batch type confusion
- These channels operate independently

**Claim 3 (SDGD Effectiveness)** - NEGATIVE
- SDGD-zero achieves F1=0.2514 compared to single-pass F1=0.4451, making it substantially worse
- All decomposition variants underperform the baseline single-pass approach
- The decomposition strategy improves recall but severely compromises precision through merge amplification

I've got two critical experiments still pending: the LLaMA multi-model test to see if the confusability pattern holds across different architectures, and SDGD v2 to address the merge amplification issue. With the May 25 deadline just ten days away, the paper's viability hinges on whether LLaMA replicates the signal and whether the revised SDGD approach can recover positive results—otherwise I'm looking at framing this as a pure analysis paper without the methodological contribution.

Now I'm mapping out the outcome scenarios and what they mean for the paper's direction. In the best case, both experiments succeed and I keep the current framing. If LLaMA shows weaker but consistent results while SDGD stays negative, I pivot to emphasizing the empirical analysis of multi-channel degradation and treat SDGD as an informed negative result. Worst case is LLaMA fails to replicate entirely, which raises model-specific artifact concerns, but I'd still need to target EMNLP with a reframed version.

I'm now setting specific metric thresholds to evaluate each scenario—for the LLaMA experiment on Few-NERD, I'm looking at whether the pairwise correlation reaches 0.10 with p<0.01 for the best case, or falls in the 0.05-0.10 range for a median outcome.

For SDGD v2, the key threshold is whether it outperforms single-pass by at least 2 percentage points, versus staying roughly equivalent or even underperforming.

The narrative hinges on these results too. The strongest story frames this as the first controlled study isolating confusability from frequency effects in LLM information extraction, with pairwise confusability as a robust generalizable signal that SDGD can operationalize into gains. The median narrative focuses on the empirical study itself—documenting the degradation channels and establishing confusability as a cross-task signal, even if SDGD doesn't deliver the performance boost.

The weakest framing still has value: it characterizes schema complexity as model-dependent and multifaceted, identifies failure modes like merge amplification and centrality confounding, and contributes a framework for understanding schema-induced degradation even if decomposition doesn't help.

Now I'm moving to write up the YAML summary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dde5d40-cc6a-4b2b-bf4f-918710559b1f",
  "isSidechain": false,
  "requestId": "req_011Cb4VAE368GqBYPu153fme",
  "type": "assistant",
  "uuid": "f67a2564-e1eb-470e-b479-c234e78c945e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "263d3c39-27c7-4994-a66d-4427b1b10f55",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1UjdyfiEdJDadpezJ4hTe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20191,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2619,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20191
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

_source line 9 · 2026-05-15T14:09:35.800Z_

```yaml
tiers:
  best:
    meaning: "LLaMA replicates pairwise confusability signal (cross-model validated); SDGD v2 with merge-dedup achieves F1 gain over single-pass. All three claims hold."
    key_assumptions:
      - "exp-012 LLaMA pairwise r≥0.10 (p<0.01) on Few-NERD, confusion ratio ≥5x"
      - "SDGD v2 solves merge amplification (precision drop <5pp vs single-pass)"
      - "SDGD v2 F1 > single-pass on Few-NERD (≥66 types) by ≥2pp"
      - "Embedding sensitivity does not block SDGD practical use (Qwen3 or MiniLM sufficient per task)"
    number_ranges:
      llama_pairwise_r: [0.10, 0.20]
      llama_pairwise_p: [1e-12, 0.01]
      llama_confusion_ratio_extreme: [5, 30]
      sdgd_v2_f1_delta_vs_single_pass: [0.02, 0.08]
      sdgd_v2_precision_drop_vs_single_pass: [-0.05, 0.02]
      cross_model_bcs_effect_delta_pp: [-35, -15]
    narrative_direction: "Original 3-claim framing intact. Empirical study (Claims 1+2) validated cross-task (NER/RE/ED) and cross-model (Qwen3/LLaMA). SDGD (Claim 3) as principled operationalization with positive results. Centrality confound as methodological contribution. Headline: pairwise confusability is a generalizable, actionable signal for LLM IE schema design."

  median:
    meaning: "LLaMA directionally consistent but weaker; SDGD v2 marginal or negative. Paper pivots to analysis-only with SDGD as informed negative result."
    key_assumptions:
      - "exp-012 LLaMA pairwise r=0.05-0.10 or p in (0.01, 0.05) — directional but not compelling standalone"
      - "LLaMA per-type or batch-level shows some consistency (not contradictory)"
      - "SDGD v2 still ≤ single-pass F1 (merge amplification partially mitigated but not solved)"
      - "Pairwise signal remains robust on Qwen3 across tasks (already confirmed)"
    number_ranges:
      llama_pairwise_r: [0.05, 0.12]
      llama_pairwise_p: [0.001, 0.05]
      llama_confusion_ratio_extreme: [2, 8]
      sdgd_v2_f1_delta_vs_single_pass: [-0.05, 0.01]
      sdgd_v2_precision_drop_vs_single_pass: [-0.15, -0.03]
      cross_model_bcs_effect_delta_pp: [-20, -5]
    narrative_direction: "Downgrade Claim 3 from 'SDGD is effective' to 'SDGD reveals merge amplification as a fundamental bottleneck in decomposition-based IE.' Paper becomes: (1) first controlled multi-channel degradation study cross-task, (2) pairwise confusability as robust signal + centrality confound analysis, (3) why naive decomposition fails — merge amplification as previously uncharacterized failure mode. Frame SDGD-zero negative as a contribution: explains why UniNER/LLM-PEE gains are modest and inconsistent. Weaker multi-model evidence handled by softening 'generalizes across models' to 'consistent direction across models, strongest on primary model.' Still EMNLP Main viable; Findings likely if reviewers want stronger multi-model."

  worst:
    meaning: "LLaMA fails to replicate (contradictory or null); SDGD v2 negative. Confusability signal appears model-specific to Qwen3."
    key_assumptions:
      - "exp-012 LLaMA pairwise r<0.05 or wrong direction or p>0.05"
      - "LLaMA batch-level BCS effect <5pp (noise-level)"
      - "SDGD v2 no improvement over v1 (merge amplification fundamental)"
      - "Reviewer will flag single-model as fatal weakness for Claim 1 generalizability"
    number_ranges:
      llama_pairwise_r: [-0.03, 0.05]
      llama_pairwise_p: [0.05, 0.90]
      llama_confusion_ratio_extreme: [0.8, 2.5]
      sdgd_v2_f1_delta_vs_single_pass: [-0.19, -0.05]
      sdgd_v2_precision_drop_vs_single_pass: [-0.35, -0.10]
      cross_model_bcs_effect_delta_pp: [-5, 2]
    narrative_direction: "Reframe entirely: drop 'generalizable signal' claim, pivot to 'model-specific schema sensitivity analysis.' Core angle becomes: LLMs encode schema structure differently — Qwen3 exhibits strong confusability-driven degradation while LLaMA does not, revealing that schema complexity is not an intrinsic property but a model-schema interaction. Paper becomes a methodological framework paper: (1) the multi-channel degradation framework as a diagnostic tool, (2) the 2×3 embedding ablation + cross-model divergence as evidence that one-size-fits-all decomposition is doomed, (3) centrality confound + merge amplification as cautionary results for the field. Drop SDGD as a method contribution entirely; reposition as 'why principled decomposition is harder than it looks.' Still target EMNLP Main — analogous to 'negative results that reframe assumptions' papers. Fallback to Findings if Main reviewers want positive method results."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f67a2564-e1eb-470e-b479-c234e78c945e",
  "isSidechain": false,
  "requestId": "req_011Cb4VAE368GqBYPu153fme",
  "type": "assistant",
  "uuid": "e201c1bd-cf7a-4017-bb94-2f16e6328055",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18",
  "sessionId": "263d3c39-27c7-4994-a66d-4427b1b10f55",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1UjdyfiEdJDadpezJ4hTe",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20191,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2619,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20191,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2619,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 20191,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20191
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
  "leafUuid": "e201c1bd-cf7a-4017-bb94-2f16e6328055",
  "sessionId": "263d3c39-27c7-4994-a66d-4427b1b10f55"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-scenario Dream model for schema-dag extraction",
  "sessionId": "263d3c39-27c7-4994-a66d-4427b1b10f55"
}
```

---
