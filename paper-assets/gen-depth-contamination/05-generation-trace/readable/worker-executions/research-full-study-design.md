# research full study design

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_research_full_study_design_20260512T124814.log`
- **Structured JSON:** [`b501f183697dd774f82e.json`](../../sessions/b5/b501f183697dd774f82e.json)

## Before a recorded user message

36 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "2bbb7981-ec9b-4af9-84cc-27ffeab18ef7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778601000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "023b045f-5f75-46b7-96ad-75d85ed128e9",
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0"
}
```

---

### Assistant

_source line 4_

Let me read the required documents first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "38763ba7-aa34-4ed3-b910-19923358b09a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHpnKcUuAv49uJuYYVH9iE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12127,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12127
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0191pYB925MJ2yTnhGvMqpGx`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "2ce3a124-b53c-4ee9-89d0-641e4c3031d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CHpnKcUuAv49uJuYYVH9iE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12127,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12127
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-12T12:48:24.007Z_

<details><summary>↩ Tool result · `toolu_0191pYB925MJ2yTnhGvMqpGx`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "387b7234-339f-497f-ae01-9a158f315d44",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me read all three documents in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "6a8f88c0-9039-4ad7-a505-50e9dcc48c02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGHN1xJBSGZ2EeFvw3Jwny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 443,
      "cache_read_input_tokens": 23968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 443
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01GCnfLVqFCdRS1FqQHm9Nsz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "1f3ab535-b0b7-4d19-a0fc-5aefbf43c817",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGHN1xJBSGZ2EeFvw3Jwny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 443,
      "cache_read_input_tokens": 23968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 443
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-12T12:48:28.967Z_

<details><summary>↩ Tool result · `toolu_01GCnfLVqFCdRS1FqQHm9Nsz`</summary>

```text
1	# Idea Brief: How Deep Is Your Fake? Estimating Generational Depth of Recursive Synthetic Text for Quality-Aware Data Curation
2	
3	
4	- **Idea ID**: `idea_013`
5	- **Created**: 2026-05-12
6	- **Approved**: 2026-05-12
7	- **Source**: foreign:be-idea-gen-0509-4
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026) — primary target with compressed 10-day experiment plan and parallel writing, AAAI 2027 (abstract deadline July 25, 2026; paper deadline August 1, 2026) — fallback with additional time for full 100K corpus, extended cross-scale analysis, and polished writing, ICLR 2027 (expected submission deadline ~September 2026) — fallback allowing thorough cross-domain evaluation and larger-scale experiments
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme "New Missions for NLP Research" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.
14	
15	Direction: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.
16	
17	Contribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.
21	2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.
22	3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.
23	
24	This is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.
25	
26	Tag: direction=data_governance, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].
27	
28	## Core Problem
29	
30	As web data becomes increasingly contaminated with multi-generation synthetic text, training corpora contain outputs of unknown recursive provenance — text generated by models that were themselves trained on synthetic outputs. Current data curation treats synthetic text as a binary category, but quality degrades nonlinearly with generational depth, with the sharpest distributional changes (tail disappearance, diversity loss) occurring in early generations. Can we estimate the generational depth of synthetic text and use this graded signal for more effective quality-aware training data filtering?
31	
32	## Opportunity / Why Now
33	
34	Existing contamination and machine-generated text detection operates at a binary level (synthetic vs. real), leaving a critical gap: the quality difference between first-generation and fourth-generation synthetic text is substantial but unexploited. Drayson et al. (EMNLP 2025) demonstrate that detection features evolve systematically across 100 generations and that detectability increases with depth — but stop short of building a depth classifier. DivEye (TMLR 2026) extracts 9 surprisal-based features for binary detection; Surplexity (2024) filters training data by surprise without even distinguishing human from AI text. Min-K%++ (ICLR 2025) improves membership inference but ignores depth. Schaeffer et al. (2025) identify 8 conflicting definitions of 'model collapse' and argue catastrophic collapse is unlikely under realistic conditions — but acknowledge that tail disappearance and diversity loss ARE real, practical harms that accumulate with recursive training. Verification-based approaches (Yi et al., arXiv 2025; Feng et al., ICLR 2025) use external verifiers to filter synthetic data quality, but neither estimates depth — they treat quality as a binary pass/fail signal from the verifier rather than estimating how many recursive steps produced the text. No method estimates how many recursive generation steps a text has undergone, despite strong evidence that degradation follows a predictable trajectory. This gap is newly fillable because controlled multi-generation corpora can be efficiently constructed with small open-weight models, and the feature evolution documented by Drayson et al. provides empirical grounding that depth-discriminative signals exist. Characterizing where depth discrimination breaks down (the saturation boundary) is itself a valuable contribution for the data curation community.
35	
36	## Landscape (SOTA & Limitations)
37	
38	The landscape spans four research threads that our work bridges:
39	
40	**Thread 1 — Synthetic text detection (binary):** Min-K% and Min-K%++ (ICLR 2025) detect pre-training membership via token probability analysis. DivEye (TMLR 2026) uses 9 surprisal-based statistical features — distributional moments, first- and second-order differences of token surprisal — for interpretable binary detection, outperforming zero-shot baselines by up to 33.2%. Surplexity (2024) proposes filtering by high surprise to mitigate collapse without distinguishing human from AI text. ConStat (NeurIPS 2024) detects contamination via performance gaps on rephrased samples. All operate at the binary level.
41	
42	**Thread 2 — Model collapse and recursive training dynamics:** Shumailov et al. (Nature 2024) demonstrate progressive tail disappearance and diversity loss across recursive training generations, with early model collapse (tail loss) preceding late collapse (mode conflation). The Strong Model Collapse paper (ICLR 2025) provides theoretical foundations. Schaeffer et al. (2025) challenge collapse definitions, identifying 8 distinct meanings and arguing that under realistic conditions (data accumulation, not replacement), catastrophic collapse requires 'trillions of models.' Bakshi et al. (arXiv 2026) show statistical conditions under which iterative training on contaminated sources can actually improve performance. Falahati et al. (arXiv May 2026) prove that pluralistic curation prevents collapse theoretically. The BIML recursive pollution framework (2026) distinguishes gradual pollution from catastrophic collapse, arguing models can become 'unusable disasters' well before full collapse.
43	
44	**Thread 3 — Synthetic data verification and quality-aware curation:** DATAPROPHET (ICLR 2026) introduces training-free data quality metrics combining perplexity, similarity, and diversity for multimodal synthetic data selection. Feng et al. (ICLR 2025) demonstrate that verification — using external signals to select high-quality synthetic samples — prevents model collapse, providing theoretical conditions under which even imperfect verifiers suffice. Yi et al. (arXiv 2025) extend this by showing that injecting information through an external verifier reverses the collapse trajectory, though long-term performance converges to the verifier's knowledge center. Both verification approaches operate at a binary quality gate level rather than estimating the recursive provenance of the text. Drayson et al. (EMNLP 2025) demonstrate that binary machine-generated text detection prevents collapse and improves performance via importance resampling, tracking feature evolution across 100 generations of GPT-2 and SmolLM2 (124M–1.7B). They show features like diversity, Self-BLEU, and perplexity distributions shift systematically with generation depth — empirically grounding the premise that depth-discriminative signals exist — but build only a binary detector.
45	
46	**The gap:** No existing work builds a practical depth-estimation algorithm. Drayson et al. characterize feature evolution across generations but do not predict depth. DivEye and Surplexity detect or filter synthetic text without generation awareness. Verification methods (Feng et al., Yi et al.) filter by quality but do not distinguish a first-generation text from a fourth-generation one. The recursive training literature (Shumailov, Bakshi, Falahati) models degradation dynamics but proposes no detection methods. We fill this gap with the first ordinal depth classifier, enabling graduated quality-aware filtering where later-generation text is downweighted proportionally rather than binary-excluded.
47	
48	## Proposed Approach
49	
50	**Phase 0 — Pilot saturation study (Days 1-3, hard gate):** Using a single model (Pythia-1.4B) and one seed dataset (C4 subset, 50K documents), generate a 10-depth recursive chain to empirically characterize where depth discrimination saturates. Extract DivEye-style surprisal features plus vocabulary diversity metrics at each depth and measure inter-depth discriminability (pairwise classifier accuracy, distribution overlap). This pilot determines the effective discrimination horizon K and informs the choice of depth granularity for the full study. We hypothesize K ≈ 3-5 based on Shumailov et al.'s observation that tail disappearance is sharpest in early generations. **Critical gating decision:** If K ≤ 2, the primary contribution pivots to saturation boundary characterization (see Saturation Fallback Plan below). The pilot MUST complete by Day 3 to avoid wasted compute downstream.
51	
52	**Saturation Fallback Plan (activated if K ≤ 2):** If depth discrimination saturates at depth ≤2, a 3-class classifier (human/gen-1/gen-2+) is only marginally more informative than binary detection. In this case, we pivot the primary contribution to a comprehensive characterization of the saturation boundary itself: (a) **Per-feature saturation analysis:** Which features plateau first — surprisal dynamics, vocabulary diversity metrics, or tail-thinning metrics? Plotting per-feature discriminability curves across depth reveals the degradation mechanisms that become indistinguishable earliest vs. latest. (b) **Cross-model saturation comparison:** Does OLMo-1B saturate at a different depth than Pythia-1.4B or Qwen2.5-1.8B? If different architectures/training regimes produce different saturation profiles, this guides model-specific curation strategies. (c) **Decoding strategy effects on saturation:** Do temperature, top-k, and nucleus sampling shift the saturation boundary? High-temperature decoding might preserve diversity longer, extending discriminability. (d) **Scale effects on saturation:** Does the 7B model (Qwen2.5-7B) produce depth chains that saturate at a different point than 1B models? If larger models saturate later, this has direct implications for real-world contamination from frontier models. These analyses make the saturation boundary characterization itself an EMNLP-quality contribution, providing actionable guidance for when depth-aware curation is effective vs. when binary detection suffices.
53	
54	**Phase 1 — Multi-generation corpus construction (Days 2-5, overlapping with Phase 0):** Construct controlled depth-labeled corpora using three small open-weight model families: Pythia-1B/1.4B (EleutherAI), OLMo-1B (AI2), and Qwen2.5-0.5B/1.8B (Alibaba). Starting from human-written seeds (C4 and Wikipedia subsets, 50K documents each — reduced from 100K for initial submission; full 100K corpus reserved for camera-ready), iteratively feed outputs back as prompts through 5 generation depths (0=human, 1-4=synthetic). Each (model, seed, depth) combination produces a depth-labeled subcorpus. Depth chains are sequential per model but parallelizable across model families.
55	
56	**Phase 2 — Feature extraction and depth-discriminative analysis (Days 4-7):** Extract features at three levels, designed to extend and complement DivEye's binary features for ordinal prediction: (a) Token-level: the 9 DivEye surprisal statistics (distributional moments + first/second-order differences) plus Min-K%-style low-probability token fractions at multiple K thresholds, providing a surprisal feature set that captures both distributional shape and temporal dynamics; (b) Sequence-level: vocabulary diversity decay metrics — type-token ratio, hapax legomena ratio, n-gram novelty (proportion of n-grams not seen in a reference human corpus), and Self-BLEU — capturing the progressive homogenization documented by Drayson et al.; (c) Distributional-level: tail-thinning metrics — kurtosis and entropy of the vocabulary frequency distribution, proportion of vocabulary below frequency thresholds — capturing the specific tail disappearance mechanism identified by Shumailov et al. Conduct feature importance analysis to identify which features drive depth discrimination vs. merely distinguish human from synthetic.
57	
58	**Phase 3 — Ordinal depth classifier (Days 6-8):** Train an ordinal regression classifier (CORAL/CORN framework) to predict generation depth (0 through K, where K is determined by the pilot), comparing against gradient-boosted baselines (LightGBM) and a simple MLP. Evaluate both exact-depth accuracy and coarse-grained classification (human/shallow/deep), since the pilot may reveal that fine-grained discrimination degenerates beyond a certain depth. Report calibration curves and confidence intervals. If the pilot shows saturation at depth K < 4, reframe as (K+1)-class classification and activate the Saturation Fallback Plan for supplementary analyses.
59	
60	**Phase 4 — Depth-aware filtering validation (Days 7-10):** Demonstrate practical utility by comparing four filtering strategies on downstream NLP benchmarks: knowledge-intensive reasoning via MMLU subsets and HellaSwag, and text generation quality via XSum summarization: (a) No filtering (baseline); (b) Binary filtering using DivEye features (remove all detected synthetic text); (c) Depth-aware weighted filtering where documents are downweighted proportionally to estimated depth (weight = 1/(1 + α·depth)); (d) Surplexity-based filtering (filter by high surprise). These benchmarks are chosen because MMLU and HellaSwag are sensitive to data quality differences in pretraining data curation (demonstrated by DataComp-LM and FineWeb-Edu evaluations), unlike well-saturated benchmarks (SST-2, AG News) where small quality improvements may not produce statistically significant gaps. Test cross-model generalization: train depth chains on Pythia, evaluate classifier on OLMo- and Qwen-generated chains.
61	
62	**Phase 4b — Cross-scale generalization probe (Days 8-10, parallel with Phase 4):** Generate a small depth chain (1K documents × 3 depths: 0, 1, 2) from Qwen2.5-7B to test whether depth features learned from 1B-scale models transfer to text generated by a 7B model. This is critical because real-world synthetic contamination primarily comes from much larger models (GPT-4, Claude, Gemini). While a full cross-scale study is beyond scope, even a small-scale probe revealing transfer (or lack thereof) provides valuable evidence about practical applicability. Cost: ~5-8 additional H100-hours.
63	
64	**Phase 5 — Naturalistic validation (Days 9-10):** Apply the trained depth classifier to a sample of recent Common Crawl data (CC-2025/2026 snapshots). Since ground-truth depth labels are unavailable for wild data, validate via proxy signals, ensuring at least one proxy is feature-orthogonal to the classifier's input features to avoid tautological correlation: (a) Correlation between predicted depth and AlignScore (NLI-based factual consistency evaluation against reference corpus documents), which measures information alignment via a unified function trained on NLI, QA, and fact verification tasks — this is feature-orthogonal because AlignScore evaluates semantic accuracy, not surprisal statistics or vocabulary distributions; (b) Correlation with independently-measured vocabulary richness metrics computed by a method distinct from the classifier's features (e.g., moving average type-token ratio with different window sizes); (c) Correlation with binary AI-detection scores from existing tools (DivEye, GPTZero) as a sanity check; (d) Qualitative analysis of high-predicted-depth samples to check face validity. This validates that the classifier produces meaningful signals on naturalistic data, not just controlled corpora.
65	
66	**Parallel writing plan (Days 1-14):** Writing begins from Day 1 and runs continuously alongside experiments. Days 1-3: Introduction and related work (leveraging existing landscape analysis). Days 4-6: Methods section (feature extraction, classifier design). Days 7-9: Results section (populated as experiments complete). Days 10-12: Discussion, analysis figures, ablation tables. Days 12-14: Final formatting, camera-ready figures, submission checklist, responsible NLP checklist. A co-author or the primary researcher allocates ~3 hours/day to writing during experimental phases.
67	
68	**Contributions (ordered by importance):** (1) The first practical generation-depth estimation algorithm for recursively generated synthetic text, moving beyond binary detection; (2) Empirical characterization of the depth-discrimination saturation boundary — at which generation depth do texts become statistically indistinguishable, which features saturate first, and how does saturation vary by model family, scale, and decoding strategy? — providing actionable guidance for data curation practitioners; (3) Demonstration that depth-aware graduated filtering outperforms both binary filtering and no filtering on challenging downstream tasks (MMLU, HellaSwag, XSum); (4) Cross-model and cross-scale depth generalization analysis, including a 7B-scale probe; (5) Feature importance analysis revealing which degradation signals (surprisal dynamics, vocabulary decay, tail thinning) are most depth-discriminative.
69	
70	## Resource Estimate
71	
72	- **auto_research**: {'claude_api_cost': '$150-280 (~1800-2500 Opus turns for end-to-end experiment design, execution, analysis, and draft generation)', 'estimated_gpu_cost': '$225-375', 'gpu_hours': '~150h H100 (exhaustive feature/model/hyperparameter search; cross-scale experiments at 7B; comprehensive saturation analysis across all models and decoding strategies; full downstream evaluation suite)', 'gpu_utilization': 'GPU idle <10%: agent runs continuous pipeline, parallelizing corpus generation across model families and overlapping feature extraction with downstream evaluation', 'risk_note': 'Agent may over-explore feature combinations without converging on a principled feature set; if pilot shows saturation at depth 2, agent should automatically activate the saturation fallback plan and redirect compute to per-feature/cross-model saturation analyses rather than continuing to optimize the depth classifier', 'speed_bottleneck': 'Sequential depth chain generation (each depth requires output from previous depth); mitigated by parallelizing across 3 model families and 2 seed datasets simultaneously. 7B cross-scale experiment adds ~8h but can run on a separate GPU. 2 H100s sufficient for 10-day timeline; 4 H100s enable 8-day completion.', 'team': '0 (initial setup only: seed data paths, model weights, evaluation benchmark specification)', 'timeline': '8-10 days with 2-4 H100s available concurrently; parallel writing tracked by agent'}
73	- **human_in_loop**: {'claude_api_cost': '$60-100 (~600-900 Opus turns for experiment planning, code generation, and result interpretation)', 'estimated_gpu_cost': '$195-325', 'gpu_hours': '~130h H100 (same base experiments plus agent-initiated feature selection sweeps and additional cross-model/cross-scale combinations)', 'gpu_utilization': 'GPU idle ~25-35%: agent queues experiments and runs analysis between human check-ins', 'risk_note': 'Saturation boundary determination requires human judgment about whether to activate the fallback plan if K ≤ 2; agent may over-optimize ordinal accuracy on controlled data without assessing generalizability', 'team': '1 researcher, ~30min/day for approving feature sets, evaluating saturation analysis, and reviewing draft sections', 'timeline': '8-10 days experiments + parallel writing; 14-day total to submission'}
74	- **manual**: {'estimated_gpu_cost': '$165-275 (at $1.50-2.50/hr H100 spot pricing, May 2026 rates)', 'gpu_hours': '~110h H100 (pilot saturation study ~15h; corpus generation across 3 model families × 5 depths at 50K docs/seed ~20h; 7B cross-scale probe ~8h; feature extraction ~8h; classifier training ~5h; downstream evaluation on MMLU/HellaSwag/XSum ~20h; naturalistic validation ~8h; ablations + saturation fallback analyses ~26h)', 'gpu_utilization': 'GPU idle ~40-50% of wall-clock time due to analysis iterations and writing between runs', 'team': '1-2 researchers, with ~3 hours/day writing allocation during experimental phase', 'timeline': '10 days experiments + 4 days final writing (writing starts Day 1 in parallel); targets EMNLP ARR May 25, 2026'}
75	
76	## Key References
77	
78	- AI models collapse when trained on recursively generated data (Shumailov et al., Nature 2024)
79	- Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models (ICLR 2025)
80	- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024)
81	- Strong Model Collapse (ICLR 2025)
82	- Machine-generated text detection prevents language model collapse (Drayson et al., EMNLP 2025)
83	- Position: Model Collapse Does Not Mean What You Think (Schaeffer et al., 2025)
84	- Diversity Boosts AI-Generated Text Detection / DivEye (TMLR 2026)
85	- Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI (2024)
86	- DATAPROPHET: Training-Free Data Quality Metric (ICLR 2026)
87	- Curated Synthetic Data Doesn't Have to Collapse (Falahati et al., arXiv May 2026)
88	- From Collapse to Improvement: Statistical Perspectives on Iterative Training on Contaminated Sources (Bakshi et al., arXiv 2026)
89	- Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World (Kazdan et al., ICML 2025)
90	- Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data (AAAI Workshop 2026)
91	- A Comprehensive Survey of Contamination Detection Methods in Large Language Models (TMLR 2025)
92	- Recursive Pollution and Model Collapse Are Not the Same (BIML 2026)
93	- Generalization or Memorization: Data Contamination and Trustworthy Evaluation for LLMs (Findings of ACL 2024)
94	- Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence (Yi et al., arXiv 2510.16657, 2025)
95	- Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification (Feng et al., ICLR 2025)
96	- AlignScore: Evaluating Factual Consistency with a Unified Alignment Function (ACL 2023)
97	- Rank consistent ordinal regression for neural networks / CORAL (Cao et al., Pattern Recognition 2020)
98	
99	## Reviewer Evaluation
100	
101	**Scores**:
102	  - clarity: **{'rationale': 'Exceptionally well-structured: five phases with clear dependencies, a hard gating decision by Day 3, a detailed saturation fallback plan with four sub-analyses, ordered contributions, and cross-references to specific prior work at each methodological choice. The landscape analysis accurately positions the work relative to four distinct research threads.', 'score': 4}**/5
103	  - feasibility: **{'rationale': 'Compute budget (110-150h H100) fits within the 200h constraint using the specified small models (Pythia-1B/1.4B, OLMo-1B, Qwen2.5-0.5B/1.8B). The Phase 0 pilot with a hard Day-3 gate is excellent scientific methodology. The saturation fallback plan is comprehensive and turns the primary risk into a contribution. The 14-day timeline is tight but the parallel writing plan and overlapping phases make it realistic.', 'score': 4}**/5
104	  - impact: **{'rationale': "Fills a verified gap between binary detection (DivEye, Min-K%++) and quality-aware curation (Feng et al., Yi et al.) with the first depth-graded quality signal. Perfectly aligned with EMNLP 2026's confirmed special theme on data contamination and synthetic data feedback loops. Even if depth discrimination saturates early, the saturation characterization itself — which features plateau first, how saturation varies by model family and decoding strategy — provides actionable guidance for the data curation community.", 'score': 4}**/5
105	  - novelty: **{'rationale': 'Verified novel across 14+ targeted searches: no existing work frames generational depth estimation as a prediction task. Drayson et al. (EMNLP 2025) and Guo et al. (NAACL 2024) characterize feature evolution across generations descriptively, but neither builds a depth classifier or proposes depth-aware filtering. The ordinal depth estimation formulation and graduated filtering application are genuinely new contributions.', 'score': 4}**/5
106	
107	## Human Review Note
108	
109	## Agent 审核结果（完整三阶段 pipeline）
110	
111	**Verdict**: PASS
112	
113	**入口三重共识 (X)**: 28.0%
114	**终审自评 (Y)**: 34.0%
115	**出口三重共识 (Z)**: 36.0%
116	**Z 区间**: [31.0%, 42.0%]
117	**真实提升 (Z-X)**: +8.0 pp
118	**幻觉幅度 (Y-Z)**: -2.0 pp
119	**出口一致性**: 高
120	**出口三次评估**: [35.0, 38.0, 37.0]
121	
122	### 优化方案 / 拒绝详情
123	【优化方案】
124	
125	1. [标题 / 核心定位] — 在标题不变的前提下，Introduction 开头前两段建立 **"demand-side ordinal provenance estimation"** 的一句话 elevator pitch，与 supply-side watermarking、point membership inference、binary detection 形成三维对比矩阵。原始 proposal 直接进入方法描述，缺少清晰的 positioning niche。 — 命中 Novelty（positioning clarity）+ Significance（reviewer 前 30 秒形成正确印象）
126	
127	2. [核心 framing / Introduction] — 将 **saturation boundary 从 fallback contribution 提升为一阶科学量**。原始 proposal 写 "If saturation occurs at very shallow depths (K ≤ 2), we provide a comprehensive saturation characterization as the primary contribution"——这种 hedging 让 reviewer 认为作者对核心假设信心不足。改为正面 claim：saturation boundary K* 本身是首次系统测量的基本量，其位置无论高低都有独立科学价值。删除所有 "If…then" 对冲语句。 — 命中 Novelty + Contribution Clarity（消除"作者自己不确定主贡献是什么"的致命印象）
128	
129	3. [理论框架 / Introduction + Method] — 新增 **信道级联 + Data Processing Inequality 框架**。将递归生成建模为 iterated lossy channel，K* 定义为 I(X₀; Xₖ) 降至不可区分阈值的临界深度——这是一个 **information-theoretic impossibility boundary**，不仅是分类器的能力上限，而是任何方法都无法逾越的信息论极限。用 JSD 作为 computationally tractable MI proxy（明确标注为近似，承认 unigram 层面的局限）。原始 proposal 完全没有理论框架。 — 命中 Novelty（从"empirical measurement"升级为"theory + validation"）+ Technical Soundness
130	
131	4. [理论框架 / Introduction + Results] — 新增 **exponential vs. polynomial MI 衰减假设检验**作为论文叙事弧线。提出 empirically motivated hypothesis：greedy decoding → 近似指数衰减（快速收敛到 fixed point），high-temperature sampling → 较慢多项式衰减（随机性延缓同质化）。设计为 hypothesis testing format（AIC/BIC model comparison）。注意措辞校准：标为"empirically motivated hypotheses"而非"theoretical predictions"，避免 overclaim。 — 命中 Novelty + Soundness（hypothesis-driven 研究范式比 exploratory 更受审稿人认可）
132	
133	5. [贡献结构 / 全文] — **大幅精简 scope**，从原始 proposal 的"everything in one paper"收窄为两个核心贡献 + 一个 application case study。C1：depth estimation + K* characterization（含降解序分析和假设检验）；C2：depth-graduated curation。Model collapse monitoring 降为 Discussion 中的 1 段 case study。Heterogeneous model chain、human editing robustness、Common Crawl 验证移入 appendix。原始 proposal 试图同时覆盖太多方向，有 "a mile wide and an inch deep" 的风险。 — 命中 Technical Soundness（每个贡献有足够展开空间）+ 降低 reviewer 认知负担
134	
135	6. [Contribution 1 分析亮点 / Results] — 将 feature group ablation 升格为 **"linguistic degradation ordering"科学发现**：按 saturation depth 排序 feature group，揭示递归生成中语言维度的逐层坍缩结构（如 vocabulary diversity 可能先于 semantic coherence 坍缩）。用 heatmap（feature group × depth → discriminative power）可视化。原始 proposal 没有此分析维度。 — 命中 Analysis Depth / Insight（从"分类器 works"到"我们揭示了递归生成的结构性规律"）
136	
137	7. [Contribution 2 方法论 / Method] — 将 **depth-graduated curation 升格为独立 paradigm**（原始 proposal 中压缩在验证段落），给出理论动机（binary filtering 在 threshold 附近信息损失最大，ordinal signal 允许 soft weighting），并将加权方案从任意 1/k 改为 **从 depth-quality 衰减曲线经验推导**（weight ∝ quality(k)/quality(0)）。与 data mixing 文献（DoReMi）建立连接：depth-graduated weighting 是 provenance-aware domain reweighting，比 DoReMi 更轻量且有可解释语义。 — 命中 Practical Impact + Contribution Clarity + Significance
138	
139	8. [Motivation / Introduction] — 新增 **JPEG 重压缩跨模态类比**（1-2 句话）："Just as forensic image analysis estimates the number of JPEG recompression cycles, we establish generational depth estimation as a research paradigm for text." 降低理解门槛，暗示更大研究方向。原始 proposal 无此 framing。 — 命中 Clarity / Motivation
140	
141	9. [Motivation / Introduction + Broader Impact] — 新增 **model collapse early-warning 叙事线**：depth distribution 作为 model collapse 的 leading indicator（depth ≥ K 占比上升 → collapse risk 积累）。虽然降为 case study，但在 Introduction 和 broader impact 中建立联系大幅增强 significance。连接 Datasheets for Datasets / Data Statements，定位为 automated provenance documentation tool。原始 proposal 仅引用 Shumailov et al. 但未建立此联系。 — 命中 Significance + Broader Impact
142	
143	10. [Related Work] — 大幅扩展覆盖面：(a) **watermarking 互补定位**（supply-side vs. demand-side，正交互补）；(b) **Min-K%++ 关系讨论**（membership ≠ ordinal depth）；(c) **model attribution / source identification**（"which model" vs. "how many generations"，正交可组合）；(d) **最新检测工作**（Binoculars, RAID benchmark）；(e) **data mixing 文献**（DoReMi, Data Mixing Laws）；(f) **Shumailov et al. 差异化 sharpen**（macro phenomenon understanding vs. micro forensic tool）。原始 proposal 仅覆盖 binary detection 和 verification-based filtering。 — 命中 Related Work Coverage（堵住多个 reviewer 攻击面）
144	
145	11. [实验设计 / Corpus Construction] — 新增 **decoding strategy 作为显式 controlled variable**（greedy, nucleus p=0.9/0.95, temperature T=0.7/1.0/1.2）。原始 proposal 提到 "across decoding strategies" 但未展开。这直接支撑 exponential vs. polynomial 假设检验，且几乎零额外成本。 — 命中 Analysis Depth + Thoroughness
146	
147	12. [实验设计 / Corpus Construction] — 新增 **retrain-chain ecological validity check**（1 个 model family + 1 个 decoding strategy，3-4 depth levels，LoRA fine-tuning），报告 prompt-chain vs. retrain-chain 的 feature distribution 对比和 cross-setting transfer accuracy。原始 proposal 完全没有考虑 prompt-chain 与真实递归污染路径的差异。 — 命中 Technical Soundness（回应"方法在真实场景下有没有用"的核心质疑）
148	
149	13. [实验设计 / Appendix] — 新增以下 robustness analyses 作为 appendix 内容：(a) **heterogeneous model chain**（交替不同模型生成）；(b) **human editing robustness**（simulated span replacement、paraphrasing）；(c) **Common Crawl naturalistic validation**。原始 proposal 无此设计。Clean chains 明确定位为 theoretical upper bound，real-world depth estimates 定位为 ordinal quality proxies。 — 命中 Experimental Rigor
150	
151	14. [Feature Extraction / Method] — 修正 **n-gram overlap feature 的 data leakage 问题**。原始 proposal 的 "cross-depth n-gram overlap decay rate" 需要 paired original text，inference 时不可用。拆分为：(a) analysis-only metric（用于降解序研究）；(b) inference-time computable variant（self-repetition n-gram statistics、与 reference human corpus 的统计距离）。 — 命中 Technical Soundness（消除 data leakage 这一 reject-worthy 问题）
152	
153	15. [Feature Extraction / Method] — 新增 **systematic feature design** 的诚实定位：标为 "systematic and principled feature design informed by the recursive generation mechanism"，而非 overclaim 为 "novel feature contributions"。新增 token-level perplexity distribution shape features（skewness, kurtosis, entropy）。 — 命中 Technical Soundness（诚实定位避免 overclaim）
154	
155	16. [Classification / Method] — 新增系统 ablation 和 baseline 对比：(a) **ordinal vs. multinomial vs. standard regression**（证明 ordinal structure 必要性）；(b) **learned representation baseline**（frozen LM embeddings + MLP vs. hand-crafted features）；(c) **LLM zero-shot/few-shot depth estimation baseline**（验证 depth estimation 需要专门方法）；(d) **LLM-as-judge quality scoring baseline**（验证 depth signal 与 LLM quality judgment 正交）；(e) **binary detector confidence as depth proxy**（Binoculars/DetectGPT score vs. true depth Spearman correlation）。原始 proposal 仅有 CORAL/CORN + 现有 filtering methods 对比。 — 命中 Baseline Completeness（堵住"为什么不直接用 X"的多个质疑）
156	
157	17. [Cross-Scale Generalization / Method] — 增强 cross-scale 策略：(a) 将 probe 扩展到 **8B-14B 范围**（Llama-3-8B 或 Qwen2.5-14B）；(b) WildChat/LMSYS-Chat 上的 **formal feature trend analysis**（含 MMD domain shift quantification）；(c) 明确 **practical deployment scope 为开源模型生态（7B-14B）**；(d) frontier model limitation 扩展为 **principled discussion**（RLHF/instruction-tuning 对 depth signal 的影响、API-only access 对 feature 计算的限制）。原始 proposal 仅有 Qwen2.5-7B 一个 cross-scale probe。 — 命中 Significance（论证实际部署价值）
158	
159	18. [Downstream Curation / Experimental Validation] — 大幅增强 curation 实验严格性：(a) **contamination severity 维度**（10%/30%/50% synthetic injection）；(b) **cross-model transfer**（classifier 训 on model A, curate model B）；(c) **unknown depth distribution condition**；(d) **data-quality-sensitive tasks**（held-out perplexity, factual QA，不仅限于 MMLU）；(e) **binary filtering threshold 选择协议明确化**；(f) **bootstrap CIs + paired significance tests**；(g) **实验逻辑链显式说明**。原始 proposal 对 filtering 实验的公平性和统计显著性没有详细设计。 — 命中 Technical Soundness + Experimental Rigor
160	
161	19. [Depth vs. Quality Analysis / Experimental Validation] — 新增 **depth-quality 单调性直接验证**。原始 proposal 隐含假设 depth 与 quality 单调递减但未验证。新增多维度 quality proxy 曲线，验证单调性成立条件。如非单调，graduated filtering 适应为 depth-features → predicted quality → weight。 — 命中 Technical Soundness（验证核心前提假设）
162	
163	20. [K* Contingency / Experimental Validation] — 新增 **显式 contingency 讨论**：K*≤3 时贡献重定位为首次量化 fundamental resolution limit + decoding strategy 对 K* 的调控效应 + 即使 coarse ordinal signal 仍有 calibration 优势。原始 proposal 的 "If…then" 结构是结构性风险。 — 命中 Soundness + Reviewer 心理管理
164	
165	【主要风险】:
166	1. **K* 实验结果不确定性**：如果在大多数 model/decoding 配置下 K*≤2，论文的 empirical richness 和 graduated curation 收益都会受限。虽有 contingency plan（fundamental resolution limit characterization + decoding strategy modulation），但 reviewer 仍可能评为 "interesting characterization but limited practical impact"。这是无法通过 proposal 优化消除的固有风险。
167	2. **"Good problem + standard method" 框架**：核心分类 pipeline 是 feature engineering + off-the-shelf ordinal regression（CORAL/CORN），审稿人可能认为方法论贡献不足。信息论框架和假设检验提升了分析深度，但分类器本身没有方法论突破。对于偏重 methods 的审稿人，这可能是 borderline reject 的理由。
168	
169	【实施评估】:
170	- 计算资源: 主实验（corpus generation + feature extraction + classifier training）可在 2-4 块 A100 上完成，估计 1-2 周。Retrain-chain validation（1 config, LoRA fine-tuning, 3-4 depth levels）约 2-3 天额外 GPU 时间。Cross-scale probe（7B-14B 模型生成 + 特征提取）约 3-5 天。总计 GPU 需求约 2-3 周集中使用。不需要大规模集群。
171	- 数据需求: C4 和 Wikipedia 子集（50K documents each）——公开可得。WildChat / LMSYS-Chat——公开可得。无需私有或受限数据集。
172	- 人工介入: 无需人工标注（ground-truth depth labels 由 generation pipeline 自动产生）。无需专家评审。唯一的人工环节是实验设计决策和论文写作。
173	- 训练需求: 需要模型训练，但规模有限。(a) Ordinal regression classifier（CORAL/CORN）：轻量级，训练时间可忽略。(b) Retrain-chain 的 LoRA fine-tuning：Pythia-1B 级别，每轮约 1-2 小时。(c) 不需要从头预训练任何 LLM。(d) 下游 curation 评估需要在 curated data 上训练小模型（≤1.8B），但这也是标准规模。
174	- 新 Benchmark: 不需要构建新的公开 benchmark。构建的 multi-depth corpus 是实验工具而非独立 benchmark 贡献（但可作为 artifact release）。
175	- 预估周期: Corpus generation + feature extraction: 2-3 周；Classifier training + ablation: 1 周；Downstream curation experiments: 1-2 周；Cross-scale + retrain-chain validation: 1-2 周；Analysis + writing: 2-3 周。**总计约 8-12 周**（从启动到可投稿），假设 GPU 资源持续可用。如果 GPU 间歇使用，可能延长至 12-16 周。EMNLP 2026 投稿 deadline 前有充足时间。
176	
177	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "90e33219-f629-49dc-832b-6ce2f0db96c7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/IDEA_BRIEF.md",
      "content": "# Idea Brief: How Deep Is Your Fake? Estimating Generational Depth of Recursive Synthetic Text for Quality-Aware Data Curation\n\n\n- **Idea ID**: `idea_013`\n- **Created**: 2026-05-12\n- **Approved**: 2026-05-12\n- **Source**: foreign:be-idea-gen-0509-4\n- **Level**: top-tier\n- **Target Venues**: EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026) — primary target with compressed 10-day experiment plan and parallel writing, AAAI 2027 (abstract deadline July 25, 2026; paper deadline August 1, 2026) — fallback with additional time for full 100K corpus, extended cross-scale analysis, and polished writing, ICLR 2027 (expected submission deadline ~September 2026) — fallback allowing thorough cross-domain evaluation and larger-scale experiments\n\n## Seed Topic\n\nTarget: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.\n\nDirection: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.\n\nContribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.\n2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.\n3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.\n\nThis is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.\n\nTag: direction=data_governance, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].\n\n## Core Problem\n\nAs web data becomes increasingly contaminated with multi-generation synthetic text, training corpora contain outputs of unknown recursive provenance — text generated by models that were themselves trained on synthetic outputs. Current data curation treats synthetic text as a binary category, but quality degrades nonlinearly with generational depth, with the sharpest distributional changes (tail disappearance, diversity loss) occurring in early generations. Can we estimate the generational depth of synthetic text and use this graded signal for more effective quality-aware training data filtering?\n\n## Opportunity / Why Now\n\nExisting contamination and machine-generated text detection operates at a binary level (synthetic vs. real), leaving a critical gap: the quality difference between first-generation and fourth-generation synthetic text is substantial but unexploited. Drayson et al. (EMNLP 2025) demonstrate that detection features evolve systematically across 100 generations and that detectability increases with depth — but stop short of building a depth classifier. DivEye (TMLR 2026) extracts 9 surprisal-based features for binary detection; Surplexity (2024) filters training data by surprise without even distinguishing human from AI text. Min-K%++ (ICLR 2025) improves membership inference but ignores depth. Schaeffer et al. (2025) identify 8 conflicting definitions of 'model collapse' and argue catastrophic collapse is unlikely under realistic conditions — but acknowledge that tail disappearance and diversity loss ARE real, practical harms that accumulate with recursive training. Verification-based approaches (Yi et al., arXiv 2025; Feng et al., ICLR 2025) use external verifiers to filter synthetic data quality, but neither estimates depth — they treat quality as a binary pass/fail signal from the verifier rather than estimating how many recursive steps produced the text. No method estimates how many recursive generation steps a text has undergone, despite strong evidence that degradation follows a predictable trajectory. This gap is newly fillable because controlled multi-generation corpora can be efficiently constructed with small open-weight models, and the feature evolution documented by Drayson et al. provides empirical grounding that depth-discriminative signals exist. Characterizing where depth discrimination breaks down (the saturation boundary) is itself a valuable contribution for the data curation community.\n\n## Landscape (SOTA & Limitations)\n\nThe landscape spans four research threads that our work bridges:\n\n**Thread 1 — Synthetic text detection (binary):** Min-K% and Min-K%++ (ICLR 2025) detect pre-training membership via token probability analysis. DivEye (TMLR 2026) uses 9 surprisal-based statistical features — distributional moments, first- and second-order differences of token surprisal — for interpretable binary detection, outperforming zero-shot baselines by up to 33.2%. Surplexity (2024) proposes filtering by high surprise to mitigate collapse without distinguishing human from AI text. ConStat (NeurIPS 2024) detects contamination via performance gaps on rephrased samples. All operate at the binary level.\n\n**Thread 2 — Model collapse and recursive training dynamics:** Shumailov et al. (Nature 2024) demonstrate progressive tail disappearance and diversity loss across recursive training generations, with early model collapse (tail loss) preceding late collapse (mode conflation). The Strong Model Collapse paper (ICLR 2025) provides theoretical foundations. Schaeffer et al. (2025) challenge collapse definitions, identifying 8 distinct meanings and arguing that under realistic conditions (data accumulation, not replacement), catastrophic collapse requires 'trillions of models.' Bakshi et al. (arXiv 2026) show statistical conditions under which iterative training on contaminated sources can actually improve performance. Falahati et al. (arXiv May 2026) prove that pluralistic curation prevents collapse theoretically. The BIML recursive pollution framework (2026) distinguishes gradual pollution from catastrophic collapse, arguing models can become 'unusable disasters' well before full collapse.\n\n**Thread 3 — Synthetic data verification and quality-aware curation:** DATAPROPHET (ICLR 2026) introduces training-free data quality metrics combining perplexity, similarity, and diversity for multimodal synthetic data selection. Feng et al. (ICLR 2025) demonstrate that verification — using external signals to select high-quality synthetic samples — prevents model collapse, providing theoretical conditions under which even imperfect verifiers suffice. Yi et al. (arXiv 2025) extend this by showing that injecting information through an external verifier reverses the collapse trajectory, though long-term performance converges to the verifier's knowledge center. Both verification approaches operate at a binary quality gate level rather than estimating the recursive provenance of the text. Drayson et al. (EMNLP 2025) demonstrate that binary machine-generated text detection prevents collapse and improves performance via importance resampling, tracking feature evolution across 100 generations of GPT-2 and SmolLM2 (124M–1.7B). They show features like diversity, Self-BLEU, and perplexity distributions shift systematically with generation depth — empirically grounding the premise that depth-discriminative signals exist — but build only a binary detector.\n\n**The gap:** No existing work builds a practical depth-estimation algorithm. Drayson et al. characterize feature evolution across generations but do not predict depth. DivEye and Surplexity detect or filter synthetic text without generation awareness. Verification methods (Feng et al., Yi et al.) filter by quality but do not distinguish a first-generation text from a fourth-generation one. The recursive training literature (Shumailov, Bakshi, Falahati) models degradation dynamics but proposes no detection methods. We fill this gap with the first ordinal depth classifier, enabling graduated quality-aware filtering where later-generation text is downweighted proportionally rather than binary-excluded.\n\n## Proposed Approach\n\n**Phase 0 — Pilot saturation study (Days 1-3, hard gate):** Using a single model (Pythia-1.4B) and one seed dataset (C4 subset, 50K documents), generate a 10-depth recursive chain to empirically characterize where depth discrimination saturates. Extract DivEye-style surprisal features plus vocabulary diversity metrics at each depth and measure inter-depth discriminability (pairwise classifier accuracy, distribution overlap). This pilot determines the effective discrimination horizon K and informs the choice of depth granularity for the full study. We hypothesize K ≈ 3-5 based on Shumailov et al.'s observation that tail disappearance is sharpest in early generations. **Critical gating decision:** If K ≤ 2, the primary contribution pivots to saturation boundary characterization (see Saturation Fallback Plan below). The pilot MUST complete by Day 3 to avoid wasted compute downstream.\n\n**Saturation Fallback Plan (activated if K ≤ 2):** If depth discrimination saturates at depth ≤2, a 3-class classifier (human/gen-1/gen-2+) is only marginally more informative than binary detection. In this case, we pivot the primary contribution to a comprehensive characterization of the saturation boundary itself: (a) **Per-feature saturation analysis:** Which features plateau first — surprisal dynamics, vocabulary diversity metrics, or tail-thinning metrics? Plotting per-feature discriminability curves across depth reveals the degradation mechanisms that become indistinguishable earliest vs. latest. (b) **Cross-model saturation comparison:** Does OLMo-1B saturate at a different depth than Pythia-1.4B or Qwen2.5-1.8B? If different architectures/training regimes produce different saturation profiles, this guides model-specific curation strategies. (c) **Decoding strategy effects on saturation:** Do temperature, top-k, and nucleus sampling shift the saturation boundary? High-temperature decoding might preserve diversity longer, extending discriminability. (d) **Scale effects on saturation:** Does the 7B model (Qwen2.5-7B) produce depth chains that saturate at a different point than 1B models? If larger models saturate later, this has direct implications for real-world contamination from frontier models. These analyses make the saturation boundary characterization itself an EMNLP-quality contribution, providing actionable guidance for when depth-aware curation is effective vs. when binary detection suffices.\n\n**Phase 1 — Multi-generation corpus construction (Days 2-5, overlapping with Phase 0):** Construct controlled depth-labeled corpora using three small open-weight model families: Pythia-1B/1.4B (EleutherAI), OLMo-1B (AI2), and Qwen2.5-0.5B/1.8B (Alibaba). Starting from human-written seeds (C4 and Wikipedia subsets, 50K documents each — reduced from 100K for initial submission; full 100K corpus reserved for camera-ready), iteratively feed outputs back as prompts through 5 generation depths (0=human, 1-4=synthetic). Each (model, seed, depth) combination produces a depth-labeled subcorpus. Depth chains are sequential per model but parallelizable across model families.\n\n**Phase 2 — Feature extraction and depth-discriminative analysis (Days 4-7):** Extract features at three levels, designed to extend and complement DivEye's binary features for ordinal prediction: (a) Token-level: the 9 DivEye surprisal statistics (distributional moments + first/second-order differences) plus Min-K%-style low-probability token fractions at multiple K thresholds, providing a surprisal feature set that captures both distributional shape and temporal dynamics; (b) Sequence-level: vocabulary diversity decay metrics — type-token ratio, hapax legomena ratio, n-gram novelty (proportion of n-grams not seen in a reference human corpus), and Self-BLEU — capturing the progressive homogenization documented by Drayson et al.; (c) Distributional-level: tail-thinning metrics — kurtosis and entropy of the vocabulary frequency distribution, proportion of vocabulary below frequency thresholds — capturing the specific tail disappearance mechanism identified by Shumailov et al. Conduct feature importance analysis to identify which features drive depth discrimination vs. merely distinguish human from synthetic.\n\n**Phase 3 — Ordinal depth classifier (Days 6-8):** Train an ordinal regression classifier (CORAL/CORN framework) to predict generation depth (0 through K, where K is determined by the pilot), comparing against gradient-boosted baselines (LightGBM) and a simple MLP. Evaluate both exact-depth accuracy and coarse-grained classification (human/shallow/deep), since the pilot may reveal that fine-grained discrimination degenerates beyond a certain depth. Report calibration curves and confidence intervals. If the pilot shows saturation at depth K < 4, reframe as (K+1)-class classification and activate the Saturation Fallback Plan for supplementary analyses.\n\n**Phase 4 — Depth-aware filtering validation (Days 7-10):** Demonstrate practical utility by comparing four filtering strategies on downstream NLP benchmarks: knowledge-intensive reasoning via MMLU subsets and HellaSwag, and text generation quality via XSum summarization: (a) No filtering (baseline); (b) Binary filtering using DivEye features (remove all detected synthetic text); (c) Depth-aware weighted filtering where documents are downweighted proportionally to estimated depth (weight = 1/(1 + α·depth)); (d) Surplexity-based filtering (filter by high surprise). These benchmarks are chosen because MMLU and HellaSwag are sensitive to data quality differences in pretraining data curation (demonstrated by DataComp-LM and FineWeb-Edu evaluations), unlike well-saturated benchmarks (SST-2, AG News) where small quality improvements may not produce statistically significant gaps. Test cross-model generalization: train depth chains on Pythia, evaluate classifier on OLMo- and Qwen-generated chains.\n\n**Phase 4b — Cross-scale generalization probe (Days 8-10, parallel with Phase 4):** Generate a small depth chain (1K documents × 3 depths: 0, 1, 2) from Qwen2.5-7B to test whether depth features learned from 1B-scale models transfer to text generated by a 7B model. This is critical because real-world synthetic contamination primarily comes from much larger models (GPT-4, Claude, Gemini). While a full cross-scale study is beyond scope, even a small-scale probe revealing transfer (or lack thereof) provides valuable evidence about practical applicability. Cost: ~5-8 additional H100-hours.\n\n**Phase 5 — Naturalistic validation (Days 9-10):** Apply the trained depth classifier to a sample of recent Common Crawl data (CC-2025/2026 snapshots). Since ground-truth depth labels are unavailable for wild data, validate via proxy signals, ensuring at least one proxy is feature-orthogonal to the classifier's input features to avoid tautological correlation: (a) Correlation between predicted depth and AlignScore (NLI-based factual consistency evaluation against reference corpus documents), which measures information alignment via a unified function trained on NLI, QA, and fact verification tasks — this is feature-orthogonal because AlignScore evaluates semantic accuracy, not surprisal statistics or vocabulary distributions; (b) Correlation with independently-measured vocabulary richness metrics computed by a method distinct from the classifier's features (e.g., moving average type-token ratio with different window sizes); (c) Correlation with binary AI-detection scores from existing tools (DivEye, GPTZero) as a sanity check; (d) Qualitative analysis of high-predicted-depth samples to check face validity. This validates that the classifier produces meaningful signals on naturalistic data, not just controlled corpora.\n\n**Parallel writing plan (Days 1-14):** Writing begins from Day 1 and runs continuously alongside experiments. Days 1-3: Introduction and related work (leveraging existing landscape analysis). Days 4-6: Methods section (feature extraction, classifier design). Days 7-9: Results section (populated as experiments complete). Days 10-12: Discussion, analysis figures, ablation tables. Days 12-14: Final formatting, camera-ready figures, submission checklist, responsible NLP checklist. A co-author or the primary researcher allocates ~3 hours/day to writing during experimental phases.\n\n**Contributions (ordered by importance):** (1) The first practical generation-depth estimation algorithm for recursively generated synthetic text, moving beyond binary detection; (2) Empirical characterization of the depth-discrimination saturation boundary — at which generation depth do texts become statistically indistinguishable, which features saturate first, and how does saturation vary by model family, scale, and decoding strategy? — providing actionable guidance for data curation practitioners; (3) Demonstration that depth-aware graduated filtering outperforms both binary filtering and no filtering on challenging downstream tasks (MMLU, HellaSwag, XSum); (4) Cross-model and cross-scale depth generalization analysis, including a 7B-scale probe; (5) Feature importance analysis revealing which degradation signals (surprisal dynamics, vocabulary decay, tail thinning) are most depth-discriminative.\n\n## Resource Estimate\n\n- **auto_research**: {'claude_api_cost': '$150-280 (~1800-2500 Opus turns for end-to-end experiment design, execution, analysis, and draft generation)', 'estimated_gpu_cost': '$225-375', 'gpu_hours': '~150h H100 (exhaustive feature/model/hyperparameter search; cross-scale experiments at 7B; comprehensive saturation analysis across all models and decoding strategies; full downstream evaluation suite)', 'gpu_utilization': 'GPU idle <10%: agent runs continuous pipeline, parallelizing corpus generation across model families and overlapping feature extraction with downstream evaluation', 'risk_note': 'Agent may over-explore feature combinations without converging on a principled feature set; if pilot shows saturation at depth 2, agent should automatically activate the saturation fallback plan and redirect compute to per-feature/cross-model saturation analyses rather than continuing to optimize the depth classifier', 'speed_bottleneck': 'Sequential depth chain generation (each depth requires output from previous depth); mitigated by parallelizing across 3 model families and 2 seed datasets simultaneously. 7B cross-scale experiment adds ~8h but can run on a separate GPU. 2 H100s sufficient for 10-day timeline; 4 H100s enable 8-day completion.', 'team': '0 (initial setup only: seed data paths, model weights, evaluation benchmark specification)', 'timeline': '8-10 days with 2-4 H100s available concurrently; parallel writing tracked by agent'}\n- **human_in_loop**: {'claude_api_cost': '$60-100 (~600-900 Opus turns for experiment planning, code generation, and result interpretation)', 'estimated_gpu_cost': '$195-325', 'gpu_hours': '~130h H100 (same base experiments plus agent-initiated feature selection sweeps and additional cross-model/cross-scale combinations)', 'gpu_utilization': 'GPU idle ~25-35%: agent queues experiments and runs analysis between human check-ins', 'risk_note': 'Saturation boundary determination requires human judgment about whether to activate the fallback plan if K ≤ 2; agent may over-optimize ordinal accuracy on controlled data without assessing generalizability', 'team': '1 researcher, ~30min/day for approving feature sets, evaluating saturation analysis, and reviewing draft sections', 'timeline': '8-10 days experiments + parallel writing; 14-day total to submission'}\n- **manual**: {'estimated_gpu_cost': '$165-275 (at $1.50-2.50/hr H100 spot pricing, May 2026 rates)', 'gpu_hours': '~110h H100 (pilot saturation study ~15h; corpus generation across 3 model families × 5 depths at 50K docs/seed ~20h; 7B cross-scale probe ~8h; feature extraction ~8h; classifier training ~5h; downstream evaluation on MMLU/HellaSwag/XSum ~20h; naturalistic validation ~8h; ablations + saturation fallback analyses ~26h)', 'gpu_utilization': 'GPU idle ~40-50% of wall-clock time due to analysis iterations and writing between runs', 'team': '1-2 researchers, with ~3 hours/day writing allocation during experimental phase', 'timeline': '10 days experiments + 4 days final writing (writing starts Day 1 in parallel); targets EMNLP ARR May 25, 2026'}\n\n## Key References\n\n- AI models collapse when trained on recursively generated data (Shumailov et al., Nature 2024)\n- Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models (ICLR 2025)\n- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024)\n- Strong Model Collapse (ICLR 2025)\n- Machine-generated text detection prevents language model collapse (Drayson et al., EMNLP 2025)\n- Position: Model Collapse Does Not Mean What You Think (Schaeffer et al., 2025)\n- Diversity Boosts AI-Generated Text Detection / DivEye (TMLR 2026)\n- Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI (2024)\n- DATAPROPHET: Training-Free Data Quality Metric (ICLR 2026)\n- Curated Synthetic Data Doesn't Have to Collapse (Falahati et al., arXiv May 2026)\n- From Collapse to Improvement: Statistical Perspectives on Iterative Training on Contaminated Sources (Bakshi et al., arXiv 2026)\n- Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World (Kazdan et al., ICML 2025)\n- Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data (AAAI Workshop 2026)\n- A Comprehensive Survey of Contamination Detection Methods in Large Language Models (TMLR 2025)\n- Recursive Pollution and Model Collapse Are Not the Same (BIML 2026)\n- Generalization or Memorization: Data Contamination and Trustworthy Evaluation for LLMs (Findings of ACL 2024)\n- Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence (Yi et al., arXiv 2510.16657, 2025)\n- Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification (Feng et al., ICLR 2025)\n- AlignScore: Evaluating Factual Consistency with a Unified Alignment Function (ACL 2023)\n- Rank consistent ordinal regression for neural networks / CORAL (Cao et al., Pattern Recognition 2020)\n\n## Reviewer Evaluation\n\n**Scores**:\n  - clarity: **{'rationale': 'Exceptionally well-structured: five phases with clear dependencies, a hard gating decision by Day 3, a detailed saturation fallback plan with four sub-analyses, ordered contributions, and cross-references to specific prior work at each methodological choice. The landscape analysis accurately positions the work relative to four distinct research threads.', 'score': 4}**/5\n  - feasibility: **{'rationale': 'Compute budget (110-150h H100) fits within the 200h constraint using the specified small models (Pythia-1B/1.4B, OLMo-1B, Qwen2.5-0.5B/1.8B). The Phase 0 pilot with a hard Day-3 gate is excellent scientific methodology. The saturation fallback plan is comprehensive and turns the primary risk into a contribution. The 14-day timeline is tight but the parallel writing plan and overlapping phases make it realistic.', 'score': 4}**/5\n  - impact: **{'rationale': \"Fills a verified gap between binary detection (DivEye, Min-K%++) and quality-aware curation (Feng et al., Yi et al.) with the first depth-graded quality signal. Perfectly aligned with EMNLP 2026's confirmed special theme on data contamination and synthetic data feedback loops. Even if depth discrimination saturates early, the saturation characterization itself — which features plateau first, how saturation varies by model family and decoding strategy — provides actionable guidance for the data curation community.\", 'score': 4}**/5\n  - novelty: **{'rationale': 'Verified novel across 14+ targeted searches: no existing work frames generational depth estimation as a prediction task. Drayson et al. (EMNLP 2025) and Guo et al. (NAACL 2024) characterize feature evolution across generations descriptively, but neither builds a depth classifier or proposes depth-aware filtering. The ordinal depth estimation formulation and graduated filtering application are genuinely new contributions.', 'score': 4}**/5\n\n## Human Review Note\n\n## Agent 审核结果（完整三阶段 pipeline）\n\n**Verdict**: PASS\n\n**入口三重共识 (X)**: 28.0%\n**终审自评 (Y)**: 34.0%\n**出口三重共识 (Z)**: 36.0%\n**Z 区间**: [31.0%, 42.0%]\n**真实提升 (Z-X)**: +8.0 pp\n**幻觉幅度 (Y-Z)**: -2.0 pp\n**出口一致性**: 高\n**出口三次评估**: [35.0, 38.0, 37.0]\n\n### 优化方案 / 拒绝详情\n【优化方案】\n\n1. [标题 / 核心定位] — 在标题不变的前提下，Introduction 开头前两段建立 **\"demand-side ordinal provenance estimation\"** 的一句话 elevator pitch，与 supply-side watermarking、point membership inference、binary detection 形成三维对比矩阵。原始 proposal 直接进入方法描述，缺少清晰的 positioning niche。 — 命中 Novelty（positioning clarity）+ Significance（reviewer 前 30 秒形成正确印象）\n\n2. [核心 framing / Introduction] — 将 **saturation boundary 从 fallback contribution 提升为一阶科学量**。原始 proposal 写 \"If saturation occurs at very shallow depths (K ≤ 2), we provide a comprehensive saturation characterization as the primary contribution\"——这种 hedging 让 reviewer 认为作者对核心假设信心不足。改为正面 claim：saturation boundary K* 本身是首次系统测量的基本量，其位置无论高低都有独立科学价值。删除所有 \"If…then\" 对冲语句。 — 命中 Novelty + Contribution Clarity（消除\"作者自己不确定主贡献是什么\"的致命印象）\n\n3. [理论框架 / Introduction + Method] — 新增 **信道级联 + Data Processing Inequality 框架**。将递归生成建模为 iterated lossy channel，K* 定义为 I(X₀; Xₖ) 降至不可区分阈值的临界深度——这是一个 **information-theoretic impossibility boundary**，不仅是分类器的能力上限，而是任何方法都无法逾越的信息论极限。用 JSD 作为 computationally tractable MI proxy（明确标注为近似，承认 unigram 层面的局限）。原始 proposal 完全没有理论框架。 — 命中 Novelty（从\"empirical measurement\"升级为\"theory + validation\"）+ Technical Soundness\n\n4. [理论框架 / Introduction + Results] — 新增 **exponential vs. polynomial MI 衰减假设检验**作为论文叙事弧线。提出 empirically motivated hypothesis：greedy decoding → 近似指数衰减（快速收敛到 fixed point），high-temperature sampling → 较慢多项式衰减（随机性延缓同质化）。设计为 hypothesis testing format（AIC/BIC model comparison）。注意措辞校准：标为\"empirically motivated hypotheses\"而非\"theoretical predictions\"，避免 overclaim。 — 命中 Novelty + Soundness（hypothesis-driven 研究范式比 exploratory 更受审稿人认可）\n\n5. [贡献结构 / 全文] — **大幅精简 scope**，从原始 proposal 的\"everything in one paper\"收窄为两个核心贡献 + 一个 application case study。C1：depth estimation + K* characterization（含降解序分析和假设检验）；C2：depth-graduated curation。Model collapse monitoring 降为 Discussion 中的 1 段 case study。Heterogeneous model chain、human editing robustness、Common Crawl 验证移入 appendix。原始 proposal 试图同时覆盖太多方向，有 \"a mile wide and an inch deep\" 的风险。 — 命中 Technical Soundness（每个贡献有足够展开空间）+ 降低 reviewer 认知负担\n\n6. [Contribution 1 分析亮点 / Results] — 将 feature group ablation 升格为 **\"linguistic degradation ordering\"科学发现**：按 saturation depth 排序 feature group，揭示递归生成中语言维度的逐层坍缩结构（如 vocabulary diversity 可能先于 semantic coherence 坍缩）。用 heatmap（feature group × depth → discriminative power）可视化。原始 proposal 没有此分析维度。 — 命中 Analysis Depth / Insight（从\"分类器 works\"到\"我们揭示了递归生成的结构性规律\"）\n\n7. [Contribution 2 方法论 / Method] — 将 **depth-graduated curation 升格为独立 paradigm**（原始 proposal 中压缩在验证段落），给出理论动机（binary filtering 在 threshold 附近信息损失最大，ordinal signal 允许 soft weighting），并将加权方案从任意 1/k 改为 **从 depth-quality 衰减曲线经验推导**（weight ∝ quality(k)/quality(0)）。与 data mixing 文献（DoReMi）建立连接：depth-graduated weighting 是 provenance-aware domain reweighting，比 DoReMi 更轻量且有可解释语义。 — 命中 Practical Impact + Contribution Clarity + Significance\n\n8. [Motivation / Introduction] — 新增 **JPEG 重压缩跨模态类比**（1-2 句话）：\"Just as forensic image analysis estimates the number of JPEG recompression cycles, we establish generational depth estimation as a research paradigm for text.\" 降低理解门槛，暗示更大研究方向。原始 proposal 无此 framing。 — 命中 Clarity / Motivation\n\n9. [Motivation / Introduction + Broader Impact] — 新增 **model collapse early-warning 叙事线**：depth distribution 作为 model collapse 的 leading indicator（depth ≥ K 占比上升 → collapse risk 积累）。虽然降为 case study，但在 Introduction 和 broader impact 中建立联系大幅增强 significance。连接 Datasheets for Datasets / Data Statements，定位为 automated provenance documentation tool。原始 proposal 仅引用 Shumailov et al. 但未建立此联系。 — 命中 Significance + Broader Impact\n\n10. [Related Work] — 大幅扩展覆盖面：(a) **watermarking 互补定位**（supply-side vs. demand-side，正交互补）；(b) **Min-K%++ 关系讨论**（membership ≠ ordinal depth）；(c) **model attribution / source identification**（\"which model\" vs. \"how many generations\"，正交可组合）；(d) **最新检测工作**（Binoculars, RAID benchmark）；(e) **data mixing 文献**（DoReMi, Data Mixing Laws）；(f) **Shumailov et al. 差异化 sharpen**（macro phenomenon understanding vs. micro forensic tool）。原始 proposal 仅覆盖 binary detection 和 verification-based filtering。 — 命中 Related Work Coverage（堵住多个 reviewer 攻击面）\n\n11. [实验设计 / Corpus Construction] — 新增 **decoding strategy 作为显式 controlled variable**（greedy, nucleus p=0.9/0.95, temperature T=0.7/1.0/1.2）。原始 proposal 提到 \"across decoding strategies\" 但未展开。这直接支撑 exponential vs. polynomial 假设检验，且几乎零额外成本。 — 命中 Analysis Depth + Thoroughness\n\n12. [实验设计 / Corpus Construction] — 新增 **retrain-chain ecological validity check**（1 个 model family + 1 个 decoding strategy，3-4 depth levels，LoRA fine-tuning），报告 prompt-chain vs. retrain-chain 的 feature distribution 对比和 cross-setting transfer accuracy。原始 proposal 完全没有考虑 prompt-chain 与真实递归污染路径的差异。 — 命中 Technical Soundness（回应\"方法在真实场景下有没有用\"的核心质疑）\n\n13. [实验设计 / Appendix] — 新增以下 robustness analyses 作为 appendix 内容：(a) **heterogeneous model chain**（交替不同模型生成）；(b) **human editing robustness**（simulated span replacement、paraphrasing）；(c) **Common Crawl naturalistic validation**。原始 proposal 无此设计。Clean chains 明确定位为 theoretical upper bound，real-world depth estimates 定位为 ordinal quality proxies。 — 命中 Experimental Rigor\n\n14. [Feature Extraction / Method] — 修正 **n-gram overlap feature 的 data leakage 问题**。原始 proposal 的 \"cross-depth n-gram overlap decay rate\" 需要 paired original text，inference 时不可用。拆分为：(a) analysis-only metric（用于降解序研究）；(b) inference-time computable variant（self-repetition n-gram statistics、与 reference human corpus 的统计距离）。 — 命中 Technical Soundness（消除 data leakage 这一 reject-worthy 问题）\n\n15. [Feature Extraction / Method] — 新增 **systematic feature design** 的诚实定位：标为 \"systematic and principled feature design informed by the recursive generation mechanism\"，而非 overclaim 为 \"novel feature contributions\"。新增 token-level perplexity distribution shape features（skewness, kurtosis, entropy）。 — 命中 Technical Soundness（诚实定位避免 overclaim）\n\n16. [Classification / Method] — 新增系统 ablation 和 baseline 对比：(a) **ordinal vs. multinomial vs. standard regression**（证明 ordinal structure 必要性）；(b) **learned representation baseline**（frozen LM embeddings + MLP vs. hand-crafted features）；(c) **LLM zero-shot/few-shot depth estimation baseline**（验证 depth estimation 需要专门方法）；(d) **LLM-as-judge quality scoring baseline**（验证 depth signal 与 LLM quality judgment 正交）；(e) **binary detector confidence as depth proxy**（Binoculars/DetectGPT score vs. true depth Spearman correlation）。原始 proposal 仅有 CORAL/CORN + 现有 filtering methods 对比。 — 命中 Baseline Completeness（堵住\"为什么不直接用 X\"的多个质疑）\n\n17. [Cross-Scale Generalization / Method] — 增强 cross-scale 策略：(a) 将 probe 扩展到 **8B-14B 范围**（Llama-3-8B 或 Qwen2.5-14B）；(b) WildChat/LMSYS-Chat 上的 **formal feature trend analysis**（含 MMD domain shift quantification）；(c) 明确 **practical deployment scope 为开源模型生态（7B-14B）**；(d) frontier model limitation 扩展为 **principled discussion**（RLHF/instruction-tuning 对 depth signal 的影响、API-only access 对 feature 计算的限制）。原始 proposal 仅有 Qwen2.5-7B 一个 cross-scale probe。 — 命中 Significance（论证实际部署价值）\n\n18. [Downstream Curation / Experimental Validation] — 大幅增强 curation 实验严格性：(a) **contamination severity 维度**（10%/30%/50% synthetic injection）；(b) **cross-model transfer**（classifier 训 on model A, curate model B）；(c) **unknown depth distribution condition**；(d) **data-quality-sensitive tasks**（held-out perplexity, factual QA，不仅限于 MMLU）；(e) **binary filtering threshold 选择协议明确化**；(f) **bootstrap CIs + paired significance tests**；(g) **实验逻辑链显式说明**。原始 proposal 对 filtering 实验的公平性和统计显著性没有详细设计。 — 命中 Technical Soundness + Experimental Rigor\n\n19. [Depth vs. Quality Analysis / Experimental Validation] — 新增 **depth-quality 单调性直接验证**。原始 proposal 隐含假设 depth 与 quality 单调递减但未验证。新增多维度 quality proxy 曲线，验证单调性成立条件。如非单调，graduated filtering 适应为 depth-features → predicted quality → weight。 — 命中 Technical Soundness（验证核心前提假设）\n\n20. [K* Contingency / Experimental Validation] — 新增 **显式 contingency 讨论**：K*≤3 时贡献重定位为首次量化 fundamental resolution limit + decoding strategy 对 K* 的调控效应 + 即使 coarse ordinal signal 仍有 calibration 优势。原始 proposal 的 \"If…then\" 结构是结构性风险。 — 命中 Soundness + Reviewer 心理管理\n\n【主要风险】:\n1. **K* 实验结果不确定性**：如果在大多数 model/decoding 配置下 K*≤2，论文的 empirical richness 和 graduated curation 收益都会受限。虽有 contingency plan（fundamental resolution limit characterization + decoding strategy modulation），但 reviewer 仍可能评为 \"interesting characterization but limited practical impact\"。这是无法通过 proposal 优化消除的固有风险。\n2. **\"Good problem + standard method\" 框架**：核心分类 pipeline 是 feature engineering + off-the-shelf ordinal regression（CORAL/CORN），审稿人可能认为方法论贡献不足。信息论框架和假设检验提升了分析深度，但分类器本身没有方法论突破。对于偏重 methods 的审稿人，这可能是 borderline reject 的理由。\n\n【实施评估】:\n- 计算资源: 主实验（corpus generation + feature extraction + classifier training）可在 2-4 块 A100 上完成，估计 1-2 周。Retrain-chain validation（1 config, LoRA fine-tuning, 3-4 depth levels）约 2-3 天额外 GPU 时间。Cross-scale probe（7B-14B 模型生成 + 特征提取）约 3-5 天。总计 GPU 需求约 2-3 周集中使用。不需要大规模集群。\n- 数据需求: C4 和 Wikipedia 子集（50K documents each）——公开可得。WildChat / LMSYS-Chat——公开可得。无需私有或受限数据集。\n- 人工介入: 无需人工标注（ground-truth depth labels 由 generation pipeline 自动产生）。无需专家评审。唯一的人工环节是实验设计决策和论文写作。\n- 训练需求: 需要模型训练，但规模有限。(a) Ordinal regression classifier（CORAL/CORN）：轻量级，训练时间可忽略。(b) Retrain-chain 的 LoRA fine-tuning：Pythia-1B 级别，每轮约 1-2 小时。(c) 不需要从头预训练任何 LLM。(d) 下游 curation 评估需要在 curated data 上训练小模型（≤1.8B），但这也是标准规模。\n- 新 Benchmark: 不需要构建新的公开 benchmark。构建的 multi-depth corpus 是实验工具而非独立 benchmark 贡献（但可作为 artifact release）。\n- 预估周期: Corpus generation + feature extraction: 2-3 周；Classifier training + ablation: 1 周；Downstream curation experiments: 1-2 周；Cross-scale + retrain-chain validation: 1-2 周；Analysis + writing: 2-3 周。**总计约 8-12 周**（从启动到可投稿），假设 GPU 资源持续可用。如果 GPU 间歇使用，可能延长至 12-16 周。EMNLP 2026 投稿 deadline 前有充足时间。\n\n",
      "numLines": 177,
      "startLine": 1,
      "totalLines": 177
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01XTwpjf8GnSqRVUffkiKd79`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "93427722-d4d2-4147-ae14-30677a4b6a09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGHN1xJBSGZ2EeFvw3Jwny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 443,
      "cache_read_input_tokens": 23968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 443
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T12:48:29.567Z_

<details><summary>↩ Tool result · `toolu_01XTwpjf8GnSqRVUffkiKd79`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md\", \"content\": \"# gen-depth-contamination — Research Dashboard\\n\\n> 最后更新: 2026-05-12 11:16 UTC | 更新原因: 修正模型型号 1.8B→1.5B-Instruct，更新进展状态\\n\\n## 核心方向\\n估计递归生成合成文本的代际深度（generational depth），构建首个 ordinal depth classifier，实现 depth-aware graduated filtering 替代 binary detection。核心科学量：判别饱和边界 K*。\\n\\n## 当前进展\\n- **阶段**: MVP 验证（执行中）\\n- **基础设施**: autodl-4090d（1×RTX 4090D 24GB, cuda:0）\\n- **实验**: mvp_pilot_sat_v1 PREPARING，Agent 在编写 pipeline 代码\\n\\n## MVP 验证方案\\n**核心假设**: 递归生成文本在统计特征空间上存在可分辨的代际差异，且差异随深度呈系统性趋势。\\n\\n**方案**（对应 IDEA_BRIEF Phase 0 pilot saturation study）:\\n- 模型: **Qwen2.5-1.5B-Instruct**（Qwen2.5 系列无 1.8B；用 Instruct 更接近真实世界合成文本来源，full study 再对比 base vs Instruct）\\n- 种子数据: C4 子集 5K docs\\n- 深度链: depth 0(human) → depth 1-5（递归生成）\\n- 生成方式: **prompt-chain**（upper bound estimate，retrain-chain 留到 research 阶段）\\n- 解码策略: **nucleus sampling p=0.95, T=1.0**\\n- 特征（15 维）: surprisal 9 维 + vocab diversity 3 维 + tail-thinning 3 维\\n- 评估: pairwise depth AUC + JSD + LightGBM ordinal 分类\\n\\n**K* 操作性定义**: K* = max k s.t. AUC(depth k-1 vs k) > 0.60\\n\\n**Pass/Fail 标准**:\\n- ✅ Pass: K* ≥ 3 且 AUC(depth 0 vs 1) > 0.70\\n- ⚠️ Conditional Pass: K* = 2，但特征趋势清晰 → saturation characterization 路线\\n- ❌ Fail: K* ≤ 1 或特征无系统性趋势\\n\\n**预估资源**: 1×RTX 4090D，约 8-12 GPU 小时\\n\\n## 近期任务\\n- [x] GPU 服务器到位\\n- [x] 项目配置绑定\\n- [ ] Agent 完成 pipeline 代码 + 环境搭建\\n- [ ] 生成 depth chain（C4 5K × 6 depths）\\n- [ ] 特征提取 + pairwise AUC + JSD 分析\\n- [ ] 判定 K* → MVP gate 决策\\n\\n## GPU 预算\\n1×RTX 4090D 24GB @ autodl-4090d（cuda:0）\\n\\n## 关键风险\\n1. K* ≤ 2 → saturation characterization 路线仍可投\\n2. 方法论贡献薄弱 → 信道级联 + DPI 理论框架可补强\\n3. EMNLP ARR May 25 deadline 仅 13 天 → MVP 必须 2 天内完成\\n4. Reviewer SSH 不通，无法独立核实环境 → 需跟进修复\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D001 | 2026-05-12 | MVP 方案：Qwen2.5-1.8B + C4 5K docs 做 pilot saturatio | — |\\n\\n\\n\\n\", \"total_chars\": 1736, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "f864c12e-cd61-4db4-aada-891b4be4c9f0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md\\\", \\\"content\\\": \\\"# gen-depth-contamination — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-12 11:16 UTC | 更新原因: 修正模型型号 1.8B→1.5B-Instruct，更新进展状态\\\\n\\\\n## 核心方向\\\\n估计递归生成合成文本的代际深度（generational depth），构建首个 ordinal depth classifier，实现 depth-aware graduated filtering 替代 binary detection。核心科学量：判别饱和边界 K*。\\\\n\\\\n## 当前进展\\\\n- **阶段**: MVP 验证（执行中）\\\\n- **基础设施**: autodl-4090d（1×RTX 4090D 24GB, cuda:0）\\\\n- **实验**: mvp_pilot_sat_v1 PREPARING，Agent 在编写 pipeline 代码\\\\n\\\\n## MVP 验证方案\\\\n**核心假设**: 递归生成文本在统计特征空间上存在可分辨的代际差异，且差异随深度呈系统性趋势。\\\\n\\\\n**方案**（对应 IDEA_BRIEF Phase 0 pilot saturation study）:\\\\n- 模型: **Qwen2.5-1.5B-Instruct**（Qwen2.5 系列无 1.8B；用 Instruct 更接近真实世界合成文本来源，full study 再对比 base vs Instruct）\\\\n- 种子数据: C4 子集 5K docs\\\\n- 深度链: depth 0(human) → depth 1-5（递归生成）\\\\n- 生成方式: **prompt-chain**（upper bound estimate，retrain-chain 留到 research 阶段）\\\\n- 解码策略: **nucleus sampling p=0.95, T=1.0**\\\\n- 特征（15 维）: surprisal 9 维 + vocab diversity 3 维 + tail-thinning 3 维\\\\n- 评估: pairwise depth AUC + JSD + LightGBM ordinal 分类\\\\n\\\\n**K* 操作性定义**: K* = max k s.t. AUC(depth k-1 vs k) > 0.60\\\\n\\\\n**Pass/Fail 标准**:\\\\n- ✅ Pass: K* ≥ 3 且 AUC(depth 0 vs 1) > 0.70\\\\n- ⚠️ Conditional Pass: K* = 2，但特征趋势清晰 → saturation characterization 路线\\\\n- ❌ Fail: K* ≤ 1 或特征无系统性趋势\\\\n\\\\n**预估资源**: 1×RTX 4090D，约 8-12 GPU 小时\\\\n\\\\n## 近期任务\\\\n- [x] GPU 服务器到位\\\\n- [x] 项目配置绑定\\\\n- [ ] Agent 完成 pipeline 代码 + 环境搭建\\\\n- [ ] 生成 depth chain（C4 5K × 6 depths）\\\\n- [ ] 特征提取 + pairwise AUC + JSD 分析\\\\n- [ ] 判定 K* → MVP gate 决策\\\\n\\\\n## GPU 预算\\\\n1×RTX 4090D 24GB @ autodl-4090d（cuda:0）\\\\n\\\\n## 关键风险\\\\n1. K* ≤ 2 → saturation characterization 路线仍可投\\\\n2. 方法论贡献薄弱 → 信道级联 + DPI 理论框架可补强\\\\n3. EMNLP ARR May 25 deadline 仅 13 天 → MVP 必须 2 天内完成\\\\n4. Reviewer SSH 不通，无法独立核实环境 → 需跟进修复\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D001 | 2026-05-12 | MVP 方案：Qwen2.5-1.8B + C4 5K docs 做 pilot saturatio | — |\\\\n\\\\n\\\\n\\\\n\\\", \\\"total_chars\\\": 1736, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md\", \"content\": \"# gen-depth-contamination — Research Dashboard\\n\\n> 最后更新: 2026-05-12 11:16 UTC | 更新原因: 修正模型型号 1.8B→1.5B-Instruct，更新进展状态\\n\\n## 核心方向\\n估计递归生成合成文本的代际深度（generational depth），构建首个 ordinal depth classifier，实现 depth-aware graduated filtering 替代 binary detection。核心科学量：判别饱和边界 K*。\\n\\n## 当前进展\\n- **阶段**: MVP 验证（执行中）\\n- **基础设施**: autodl-4090d（1×RTX 4090D 24GB, cuda:0）\\n- **实验**: mvp_pilot_sat_v1 PREPARING，Agent 在编写 pipeline 代码\\n\\n## MVP 验证方案\\n**核心假设**: 递归生成文本在统计特征空间上存在可分辨的代际差异，且差异随深度呈系统性趋势。\\n\\n**方案**（对应 IDEA_BRIEF Phase 0 pilot saturation study）:\\n- 模型: **Qwen2.5-1.5B-Instruct**（Qwen2.5 系列无 1.8B；用 Instruct 更接近真实世界合成文本来源，full study 再对比 base vs Instruct）\\n- 种子数据: C4 子集 5K docs\\n- 深度链: depth 0(human) → depth 1-5（递归生成）\\n- 生成方式: **prompt-chain**（upper bound estimate，retrain-chain 留到 research 阶段）\\n- 解码策略: **nucleus sampling p=0.95, T=1.0**\\n- 特征（15 维）: surprisal 9 维 + vocab diversity 3 维 + tail-thinning 3 维\\n- 评估: pairwise depth AUC + JSD + LightGBM ordinal 分类\\n\\n**K* 操作性定义**: K* = max k s.t. AUC(depth k-1 vs k) > 0.60\\n\\n**Pass/Fail 标准**:\\n- ✅ Pass: K* ≥ 3 且 AUC(depth 0 vs 1) > 0.70\\n- ⚠️ Conditional Pass: K* = 2，但特征趋势清晰 → saturation characterization 路线\\n- ❌ Fail: K* ≤ 1 或特征无系统性趋势\\n\\n**预估资源**: 1×RTX 4090D，约 8-12 GPU 小时\\n\\n## 近期任务\\n- [x] GPU 服务器到位\\n- [x] 项目配置绑定\\n- [ ] Agent 完成 pipeline 代码 + 环境搭建\\n- [ ] 生成 depth chain（C4 5K × 6 depths）\\n- [ ] 特征提取 + pairwise AUC + JSD 分析\\n- [ ] 判定 K* → MVP gate 决策\\n\\n## GPU 预算\\n1×RTX 4090D 24GB @ autodl-4090d（cuda:0）\\n\\n## 关键风险\\n1. K* ≤ 2 → saturation characterization 路线仍可投\\n2. 方法论贡献薄弱 → 信道级联 + DPI 理论框架可补强\\n3. EMNLP ARR May 25 deadline 仅 13 天 → MVP 必须 2 天内完成\\n4. Reviewer SSH 不通，无法独立核实环境 → 需跟进修复\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D001 | 2026-05-12 | MVP 方案：Qwen2.5-1.8B + C4 5K docs 做 pilot saturatio | — |\\n\\n\\n\\n\", \"total_chars\": 1736, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_019nbYYBoQx4bYgj5dmcN3Bk`</summary>

```json
{
  "project": "gen-depth-contamination",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "bc2fcdd7-10a2-4d50-9026-32905328f988",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGHN1xJBSGZ2EeFvw3Jwny",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 443,
      "cache_read_input_tokens": 23968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 443
      },
      "output_tokens": 41,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T12:48:30.128Z_

<details><summary>↩ Tool result · `toolu_019nbYYBoQx4bYgj5dmcN3Bk`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/memory.md\", \"content\": \"# Memory — gen-depth-contamination\\n\\n## 已知问题\\n\\n### right-padding (2026-05-12)\\nMVP pipeline 使用 right-padding（transformers 默认）。Director 确认对 MVP 判定无影响（所有 depth 一致受影响），不中断当前实验。**full study 阶段必须修复为 `tokenizer.padding_side = \\\"left\\\"`**，否则 batch 生成时 padding tokens 会影响生成质量的绝对水平。\\n\\n## AutoDL 环境经验\\n\\n### C4 数据集加载 (2026-05-12)\\nAutoDL 代理下 `load_dataset(\\\"allenai/c4\\\", \\\"en\\\", streaming=True)` 会触发全量文件树解析（数千个 shard 的分页 API 请求），ProxyError 无限重试。修复：用单 shard URL 直接加载 + `HF_ENDPOINT=https://hf-mirror.com` 中转。\\n\\n### 环境变量必须固化到启动脚本 (2026-05-12)\\nAutoDL 上 `source /etc/network_turbo`、SSL 证书、HF 配置等环境变量不能只在 shell session 里 export，必须写入 `run_mvp.sh` 等包装脚本，否则 tmux session 里不生效。\\n\", \"total_chars\": 646, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "d51eb56e-4a14-4b34-8386-b60b3cfbcded",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/memory.md\\\", \\\"content\\\": \\\"# Memory — gen-depth-contamination\\\\n\\\\n## 已知问题\\\\n\\\\n### right-padding (2026-05-12)\\\\nMVP pipeline 使用 right-padding（transformers 默认）。Director 确认对 MVP 判定无影响（所有 depth 一致受影响），不中断当前实验。**full study 阶段必须修复为 `tokenizer.padding_side = \\\\\\\"left\\\\\\\"`**，否则 batch 生成时 padding tokens 会影响生成质量的绝对水平。\\\\n\\\\n## AutoDL 环境经验\\\\n\\\\n### C4 数据集加载 (2026-05-12)\\\\nAutoDL 代理下 `load_dataset(\\\\\\\"allenai/c4\\\\\\\", \\\\\\\"en\\\\\\\", streaming=True)` 会触发全量文件树解析（数千个 shard 的分页 API 请求），ProxyError 无限重试。修复：用单 shard URL 直接加载 + `HF_ENDPOINT=https://hf-mirror.com` 中转。\\\\n\\\\n### 环境变量必须固化到启动脚本 (2026-05-12)\\\\nAutoDL 上 `source /etc/network_turbo`、SSL 证书、HF 配置等环境变量不能只在 shell session 里 export，必须写入 `run_mvp.sh` 等包装脚本，否则 tmux session 里不生效。\\\\n\\\", \\\"total_chars\\\": 646, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/memory.md\", \"content\": \"# Memory — gen-depth-contamination\\n\\n## 已知问题\\n\\n### right-padding (2026-05-12)\\nMVP pipeline 使用 right-padding（transformers 默认）。Director 确认对 MVP 判定无影响（所有 depth 一致受影响），不中断当前实验。**full study 阶段必须修复为 `tokenizer.padding_side = \\\"left\\\"`**，否则 batch 生成时 padding tokens 会影响生成质量的绝对水平。\\n\\n## AutoDL 环境经验\\n\\n### C4 数据集加载 (2026-05-12)\\nAutoDL 代理下 `load_dataset(\\\"allenai/c4\\\", \\\"en\\\", streaming=True)` 会触发全量文件树解析（数千个 shard 的分页 API 请求），ProxyError 无限重试。修复：用单 shard URL 直接加载 + `HF_ENDPOINT=https://hf-mirror.com` 中转。\\n\\n### 环境变量必须固化到启动脚本 (2026-05-12)\\nAutoDL 上 `source /etc/network_turbo`、SSL 证书、HF 配置等环境变量不能只在 shell session 里 export，必须写入 `run_mvp.sh` 等包装脚本，否则 tmux session 里不生效。\\n\", \"total_chars\": 646, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have all three documents. Let me analyze the information and create the full study plan.

Key facts from the documents:

**From IDEA_BRIEF:**
- Phase 0: Pilot saturation study (Days 1-3) - currently running as MVP
- Phase 1: Multi-generation corpus construction (Days 2-5)
- Phase 2: Feature extraction and depth-discriminative analysis (Days 4-7)
- Phase 3: Ordinal depth classifier (Days 6-8)
- Phase 4: Depth-aware filtering validation (Days 7-10)


- Phase 4b: Cross-scale generalization probe (Days 8-10)
- Phase 5: Naturalistic validation (Days 9-10)

Models mentioned: Pythia-1B/1.4B, OLMo-1B, Qwen2.5-0.5B/1.8B (originally), now MVP uses Qwen2.5-1.5B-Instruct. Seed data comes from C4 and Wikipedia subsets, 50K documents each (reduced from 100K). Depth ranges from 0-5 with 6 levels total. Features include DivEye surprisal (9 dimensions) plus vocab diversity and tail-thinning metrics.

The reviewer flagged several important considerations: I should treat decoding strategy as a controlled variable with multiple settings like greedy, nucleus sampling at different p values, and temperature variations. I need to validate the retrain-chain for ecological validity and push the cross-scale testing up to 8B-14B models. The contamination severity dimension should span 10%, 30%, and 50% synthetic injection levels, and I should include more baseline comparisons.

Looking at the roadmap specifics: the MVP targets Qwen2.5-1.5B-Instruct with C4 at 5K docs, depth 0→5, and nucleus p=0.95 with T=1.0. I'm running on autodl-4090d with a single RTX 4090D (24GB), and there's an EMNLP ARR deadline on May 25—that's 13 days away from May 12. The MVP should take 8-12 GPU hours. I also need to fix the right-padding issue by switching to left-padding.

Now I'm working through the practical constraints of the 4090D setup. With 24GB VRAM on a single GPU, the smaller models like Qwen2.5-1.5B, Pythia-1.4B, and OLMo-1B all fit comfortably in fp16 (around 2-3GB each), but Qwen2.5-7B is tight at 14GB with KV cache overhead for longer sequences. The retrain-chain using LoRA fine-tuning will add significant computational time, so I need to calculate the actual timeline carefully against the deadline.

Looking at the GPU hour requirements, the MVP baseline with 5K documents across 6 depths takes roughly 8-12 hours per model. Scaling to the full 50K document corpus would balloon to 80-120 hours per model per decoding strategy, which is completely infeasible within 13 days on a single GPU. I need to be strategic about what's actually achievable—with 312 GPU hours maximum assuming continuous utilization, I can't run the full study as originally scoped.

For the MVP specifically, generating 25K samples (5K docs × 5 depths) with the 1.5B model should take around 5 hours, while the 7B model would be 3-4x slower at roughly 15-20 hours. This leaves me with a choice: either stick with 5K documents and expand the number of models and decoding strategies I can test, or find a middle ground that balances breadth and depth within my time constraints.

Looking at Option 1, running 4 models across 5 different decoding strategies at 5 depths would consume about 175 hours just for generation, plus another 40-50 hours for feature extraction, training, and evaluation—bringing me to around 220-230 hours, which is tight but feasible. Option 2 of scaling to 10K documents for the core experiments while keeping 5K for ablations might give me better statistical power without exceeding my budget.

I should also factor in the retrain-chain experiments with LoRA fine-tuning on Pythia, which would add another 15-20 hours across all depths. With all this mapped out, I'm ready to finalize the experimental plan.

Now I'm recalculating the generation time more carefully. The MVP uses 5K documents across 6 depths, where depth 0 is human-written and depths 1-5 are model-generated. Each generation step takes the previous depth's output and generates new text, so I'm looking at 5 generation passes. With Qwen2.5-1.5B generating roughly 500 tokens per document at about 50 tokens per second on a 4090D, that's 2.5 million tokens total, which works out to around 14 hours across all 5 depths with batch processing.

With batch sizes of 8, I can compress that down to 10-15 hours total, which aligns with the 8-12 hour estimate. So I'll stick with 5K documents as my baseline for all experiments—matching the MVP scope—and note that the camera-ready version can scale up to 10-50K if needed.

For the full study, I'm settling on Qwen2.5-1.5B-Instruct as the MVP model, then comparing against Pythia-1.4B, OLMo-1B, and Qwen2.5-7B-Instruct, with different decoding strategies to test.

Now I'm mapping out the full experimental matrix: 4 models × 5 strategies gives 20 configurations, but I don't need to run all of them. I'm prioritizing by impact—P0 experiments are the core claims needed for submission, P1 are important ablations I'd like to include, and P2 is appendix material. The P0 set covers multi-model depth chains to show cross-model generalization, a decoding strategy ablation on one model, a cross-scale probe with the 7B model, the depth classifier itself, and downstream filtering comparisons on MMLU and HellaSwag. P1 adds more model-strategy combinations, a retrain-chain experiment, and a contamination severity ablation.

Now I'm estimating GPU hours for the P0 generation phase, which looks like it'll take 60-80 hours total. I'm breaking down each configuration: the Qwen 1.5B nucleus sampling run is already done at 8 hours, Pythia-1.4B needs about 8 hours, OLMo-1B is faster at 6 hours since it's smaller, and Qwen 7B will take around 20 hours. I'm still working through the remaining strategy configurations to get a full picture of the compute budget. Looking at the downstream evaluation more carefully, I realize I need to decide between pre-training from scratch, continued pre-training, or just evaluating existing models on contaminated benchmarks. Continued pre-training on a small model like Pythia-1.4B with different data mixtures seems most practical—that's roughly 3-5 hours per run on a 4090D, and with 8-12 different filtering and contamination combinations, I'm looking at 30-60 hours total. This timeline is getting tight, so I should probably shift some work to P1 and focus the core experiments on the most promising filtering strategies.

I'm mapping out the actual time budget now: P0 needs about 115 hours, P0+P1 together around 155 hours, leaving room for P2 if things go smoothly. The MVP is already consuming 8-12 hours, so I have roughly 300 hours left from the 312 available. The real bottleneck though isn't GPU hours—it's the 13-day wall-clock deadline, since many experiments have to run sequentially, especially the depth chain experiments.

Looking at how to parallelize across the timeline: different model families can run independently, so I could stack Pythia, OLMo, and multiple Qwen strategies back-to-back over days 2-4, finishing P0 generation in about 2.7 days. Then feature extraction and classifier training would take roughly 13 hours combined on days 4-5, followed by downstream evaluation over days 5-7.

For P1 experiments and contamination severity analysis, I'm looking at another 1.7 days, with analysis and remaining work on day 9-10, and writing pushed to days 10-13. The real constraint here is the sequential generation chains—each depth level depends on the previous one. But recalculating the actual timing: a single chain across 5 depths with 5K documents on a 1.5B model is about 8 hours total, not per depth, which gives me more breathing room than I initially thought. The MVP itself takes 5-7 hours, so I should anchor the schedule there and build out from that baseline.

Now I need to be strategic about which experiments actually run on the 4090D and in what order, since that's my bottleneck. Let me document the model specs I'm working with—Qwen2.5-1.5B, Pythia-1.4B, and OLMo-1B all fit comfortably in fp16 on the card, so I have flexibility there.

For the 7B model, I'm checking whether Qwen2.5-7B-Instruct will actually fit—it's around 14GB in fp16, which leaves about 10GB for KV cache and batch operations on a 24GB card, so it should work with conservative batch sizes. B params → 32 layers, GQA, each layer has K,V of size (num_kv_heads × head_dim × seq_len × 2 bytes). For Qwen2.5-7B: 28 layers, 4 KV heads, 128 head_dim → 28 × 4 × 128 × 2048 × 2 × 2 = ~115MB per batch. With batch_size=4: ~460MB. So KV cache is manageable.
- Total with activations: ~16-17GB for batch_size=4 → fits in 24GB

For larger batch sizes or longer sequences, might need to reduce batch_size to 1-2.

OK, I'm confident 7B fits on 4090D. Let me proceed with writing the plan.

I'll use bf16 since the 4090D supports it and it's standard for modern models. For the LoRA setup, I'm thinking rank 16-32 for a small model, alpha around 32-64, targeting q_proj and v_proj with maybe k_proj and o_proj as well. Training on each depth's 5K document corpus for 3 epochs at 2e-4 learning rate should take roughly 1-2 hours per depth on the 4090D, so the full chain across 5 depths plus generation time comes to about 15-25 hours total. Now I'll write out the comprehensive plan.

For the downstream evaluation, I need to set up a careful comparison. I'll continue pre-train a base model like Pythia-1.4B on datasets filtered different ways—no filtering, binary filtering to remove all synthetic data, depth-graduated downweighting, and surplexity-based filtering—then evaluate each approach on MMLU and HellaSwag. With 4 filtering strategies and 3 contamination levels, that's 12 runs at roughly 2-3 hours each for continued pre-training on 5K documents.

The full pipeline would take about 42 hours total: 30 hours for pre-training across all runs and 12 hours for evaluation using lm-eval-harness. It's substantial but feasible.

For the depth classifier itself, 5K documents per depth level gives me 30K total samples across 6 depth classes, which is solid for training a LightGBM or CORAL classifier with 15 features.

The real constraint emerges when I multiply across all experimental conditions: 4 models × 5 strategies × 6 depths × 5K documents = 600K total documents to process. Feature extraction at that scale becomes the bottleneck.

I need to handle model availability carefully—Qwen2.5-7B-Instruct is on ModelScope which is faster on AutoDL, but Pythia and OLMo might require using a HF mirror endpoint instead. Before diving into the implementation, I should check if there's any existing code or artifacts I can build on.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "efd6345e-17e8-42c9-baf8-f8716e660324",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKKtdDSEEw4oUEDYAcQuQG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13213,
      "cache_read_input_tokens": 24411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13213
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 15_

Now let me check what code/artifacts exist already.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "1ef6c295-fb51-4bba-8973-fd15c22bd344",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKKtdDSEEw4oUEDYAcQuQG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13213,
      "cache_read_input_tokens": 24411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13213
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Glob · `toolu_01N1FJPktTFk4fgSiZbzU8WP`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "ab302b94-acec-4b2b-97a9-15f2553289b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKKtdDSEEw4oUEDYAcQuQG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13213,
      "cache_read_input_tokens": 24411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13213
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_01GjqDkWAUx8UikGk2eBv36h`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "8407d0a8-5f8e-4453-a0b3-226bde3154ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JKKtdDSEEw4oUEDYAcQuQG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13213,
      "cache_read_input_tokens": 24411,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13213
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T12:50:17.828Z_

<details><summary>↩ Tool result · `toolu_01N1FJPktTFk4fgSiZbzU8WP`</summary>

```text
artifacts/gpu_optimization_report.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "2c4b56ca-5f4b-4b84-8d07-d6d219f6870e",
  "tool_use_result": {
    "filenames": [
      "artifacts/gpu_optimization_report.txt"
    ],
    "durationMs": 12,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T12:50:17.833Z_

<details><summary>↩ Tool result · `toolu_01GjqDkWAUx8UikGk2eBv36h`</summary>

```text
scripts/run_pipeline.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "bd781f85-e243-4107-9674-c7fd17a3820d",
  "tool_use_result": {
    "filenames": [
      "scripts/run_pipeline.py"
    ],
    "durationMs": 9,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01CaQsdfr9yxSqjNKTv9RDSV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/gpu_optimization_report.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "c78293ee-3f6b-4d4e-9971-1c36e5e1e6dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFhM6NxjThSNdEd1bZBRCS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5264,
      "cache_read_input_tokens": 37624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5264
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T12:50:20.846Z_

<details><summary>↩ Tool result · `toolu_01CaQsdfr9yxSqjNKTv9RDSV`</summary>

```text
1	GPU Utilization & Batch Size Optimization Report
2	=================================================
3	Date: 2026-05-12
4	Target: mvp_pilot_sat_v1 on autodl-4090d (RTX 4090D, 24GB)
5	Model: Qwen2.5-1.5B-Instruct (fp16, ~3GB static weight)
6	
7	1. 当前 GPU 利用率和显存占用
8	--------------------------
9	- GPU Compute Utilization: 45%
10	- VRAM Used: 3865 MiB / 24564 MiB (15.7%)
11	- Power: 156W / 425W (37%)
12	- Temperature: 49°C
13	- 进程 PID: 5933 (python), 占用 3856 MiB
14	
15	结论：GPU 严重 underutilized，显存空闲 ~20GB，算力利用不到一半。
16	
17	2. 当前 Batch Size 配置
18	-----------------------
19	- Step 3 (生成): --batch_size=16 (默认值，未覆盖)
20	- Step 4 (特征提取): --feat_batch_size=8 (默认值)
21	- 每 depth 313 batches (5000/16), ~6.2s/batch, ~32min/depth
22	- 共 5 个 depth → Step 3 总计 ~162 min
23	
24	3. 显存估算与推荐 Batch Size
25	-----------------------------
26	
27	### Step 3: 生成阶段 (model.generate)
28	
29	当前显存分解:
30	  - 模型权重 (fp16): ~3000 MiB
31	  - KV cache + 激活 (bs=16): ~865 MiB
32	  - 合计: ~3865 MiB
33	
34	Qwen2.5-1.5B GQA (num_kv_heads=2, head_dim=128, 28 layers):
35	  - KV cache/token/layer: 2×2×128×2B = 1KB
36	  - Per sequence (768 tokens max): 768×28KB ≈ 21.5 MB
37	  - 线性外推 (留 2GB safety margin, 可用 ~22.5GB):
38	    bs=64  → ~3000 + 865×4 = ~6460 MiB  ✓ 安全
39	    bs=128 → ~3000 + 865×8 = ~9920 MiB  ✓ 安全
40	    bs=256 → ~3000 + 865×16 = ~16840 MiB ✓ 安全但偏紧
41	
42	  ★ 推荐: batch_size=64 (保守) 或 batch_size=128 (激进)
43	  - bs=64:  79 batches/depth, 预计 GPU utilization 70-80%
44	  - bs=128: 40 batches/depth, 预计 GPU utilization 80-90%
45	
46	### Step 4: 特征提取 (forward pass + logits)
47	
48	特征提取的瓶颈是 logits 张量:
49	  - logits: bs × 512 × 151936 (vocab) × 2B (fp16)
50	  - bs=8:  ~1.2 GB logits
51	  - bs=16: ~2.4 GB logits
52	  - bs=32: ~4.7 GB logits
53	
54	  ★ 推荐: feat_batch_size=24 (保守) 或 feat_batch_size=32 (激进)
55	  - bs=24: ~3.6 GB logits + 3GB model = ~8-9 GB, 安全
56	  - bs=32: ~4.7 GB logits + 3GB model = ~10-11 GB, 安全
57	
58	4. 其他优化建议
59	--------------
60	
61	(a) ⚠️ padding_side='left' — 关键修复
62	    当前 log 每个 batch 都报 right-padding 警告。
63	    decoder-only 模型应使用 left padding 做 batched generation。
64	    right padding 会导致:
65	    - 生成质量下降 (attention mask 处理不一致)
66	    - 可能浪费算力在 padding tokens 的生成上
67	    修复: tokenizer.padding_side = "left" (在 run_pipeline.py 加载 tokenizer 后)
68	
69	(b) Flash Attention 2
70	    未检测到 flash-attn 是否安装。如果未装:
71	    pip install flash-attn --no-build-isolation
72	    加载模型时加 attn_implementation="flash_attention_2"
73	    预计节省 10-20% 生成时间 + 显著减少显存占用
74	
75	(c) torch.compile (PyTorch 2.x)
76	    model = torch.compile(model, mode="reduce-overhead")
77	    对 autoregressive generation 效果有限，但 forward pass (Step 4) 可加速 10-15%
78	
79	(d) torch.cuda.empty_cache() 开销
80	    当前每个 batch 后都调用 empty_cache()，在显存充裕时这是不必要的开销。
81	    可以移除或改为每 N 个 batch 调用一次。
82	
83	5. 预估优化后运行时间节省
84	-------------------------
85	
86	假设采用: bs=64, feat_bs=24, left padding, 保留 flash-attn 待查
87	
88	                       当前         优化后        节省
89	Step 3 (生成):        ~162 min     ~105 min     ~57 min (35%)
90	  - 5 depths × 313 batches × 6.2s → 5 × 79 batches × ~16s
91	  - bs 增大 4x, 吞吐预计提升 ~55% (非线性, generation 是 memory-bandwidth bound)
92	
93	Step 4 (特征提取):    ~31 min      ~14 min      ~17 min (55%)
94	  - 6 depths × 625 batches × 0.5s → 6 × 209 batches × ~0.7s
95	  - forward pass 对 batch size 扩展更线性
96	
97	总 pipeline 预计节省: ~74 min (约 38%)
98	
99	如加上 flash-attn + padding_side 修复，可能再多节省 10-15%。
100	
101	6. Full Study 建议参数
102	----------------------
103	
104	python scripts/run_pipeline.py \
105	  --model_path ... \
106	  --batch_size 64 \
107	  --feat_batch_size 24
108	
109	同时在代码中修复:
110	  tokenizer.padding_side = "left"
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "4d571686-cec4-4f9a-b302-d164062f09d3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/gpu_optimization_report.txt",
      "content": "GPU Utilization & Batch Size Optimization Report\n=================================================\nDate: 2026-05-12\nTarget: mvp_pilot_sat_v1 on autodl-4090d (RTX 4090D, 24GB)\nModel: Qwen2.5-1.5B-Instruct (fp16, ~3GB static weight)\n\n1. 当前 GPU 利用率和显存占用\n--------------------------\n- GPU Compute Utilization: 45%\n- VRAM Used: 3865 MiB / 24564 MiB (15.7%)\n- Power: 156W / 425W (37%)\n- Temperature: 49°C\n- 进程 PID: 5933 (python), 占用 3856 MiB\n\n结论：GPU 严重 underutilized，显存空闲 ~20GB，算力利用不到一半。\n\n2. 当前 Batch Size 配置\n-----------------------\n- Step 3 (生成): --batch_size=16 (默认值，未覆盖)\n- Step 4 (特征提取): --feat_batch_size=8 (默认值)\n- 每 depth 313 batches (5000/16), ~6.2s/batch, ~32min/depth\n- 共 5 个 depth → Step 3 总计 ~162 min\n\n3. 显存估算与推荐 Batch Size\n-----------------------------\n\n### Step 3: 生成阶段 (model.generate)\n\n当前显存分解:\n  - 模型权重 (fp16): ~3000 MiB\n  - KV cache + 激活 (bs=16): ~865 MiB\n  - 合计: ~3865 MiB\n\nQwen2.5-1.5B GQA (num_kv_heads=2, head_dim=128, 28 layers):\n  - KV cache/token/layer: 2×2×128×2B = 1KB\n  - Per sequence (768 tokens max): 768×28KB ≈ 21.5 MB\n  - 线性外推 (留 2GB safety margin, 可用 ~22.5GB):\n    bs=64  → ~3000 + 865×4 = ~6460 MiB  ✓ 安全\n    bs=128 → ~3000 + 865×8 = ~9920 MiB  ✓ 安全\n    bs=256 → ~3000 + 865×16 = ~16840 MiB ✓ 安全但偏紧\n\n  ★ 推荐: batch_size=64 (保守) 或 batch_size=128 (激进)\n  - bs=64:  79 batches/depth, 预计 GPU utilization 70-80%\n  - bs=128: 40 batches/depth, 预计 GPU utilization 80-90%\n\n### Step 4: 特征提取 (forward pass + logits)\n\n特征提取的瓶颈是 logits 张量:\n  - logits: bs × 512 × 151936 (vocab) × 2B (fp16)\n  - bs=8:  ~1.2 GB logits\n  - bs=16: ~2.4 GB logits\n  - bs=32: ~4.7 GB logits\n\n  ★ 推荐: feat_batch_size=24 (保守) 或 feat_batch_size=32 (激进)\n  - bs=24: ~3.6 GB logits + 3GB model = ~8-9 GB, 安全\n  - bs=32: ~4.7 GB logits + 3GB model = ~10-11 GB, 安全\n\n4. 其他优化建议\n--------------\n\n(a) ⚠️ padding_side='left' — 关键修复\n    当前 log 每个 batch 都报 right-padding 警告。\n    decoder-only 模型应使用 left padding 做 batched generation。\n    right padding 会导致:\n    - 生成质量下降 (attention mask 处理不一致)\n    - 可能浪费算力在 padding tokens 的生成上\n    修复: tokenizer.padding_side = \"left\" (在 run_pipeline.py 加载 tokenizer 后)\n\n(b) Flash Attention 2\n    未检测到 flash-attn 是否安装。如果未装:\n    pip install flash-attn --no-build-isolation\n    加载模型时加 attn_implementation=\"flash_attention_2\"\n    预计节省 10-20% 生成时间 + 显著减少显存占用\n\n(c) torch.compile (PyTorch 2.x)\n    model = torch.compile(model, mode=\"reduce-overhead\")\n    对 autoregressive generation 效果有限，但 forward pass (Step 4) 可加速 10-15%\n\n(d) torch.cuda.empty_cache() 开销\n    当前每个 batch 后都调用 empty_cache()，在显存充裕时这是不必要的开销。\n    可以移除或改为每 N 个 batch 调用一次。\n\n5. 预估优化后运行时间节省\n-------------------------\n\n假设采用: bs=64, feat_bs=24, left padding, 保留 flash-attn 待查\n\n                       当前         优化后        节省\nStep 3 (生成):        ~162 min     ~105 min     ~57 min (35%)\n  - 5 depths × 313 batches × 6.2s → 5 × 79 batches × ~16s\n  - bs 增大 4x, 吞吐预计提升 ~55% (非线性, generation 是 memory-bandwidth bound)\n\nStep 4 (特征提取):    ~31 min      ~14 min      ~17 min (55%)\n  - 6 depths × 625 batches × 0.5s → 6 × 209 batches × ~0.7s\n  - forward pass 对 batch size 扩展更线性\n\n总 pipeline 预计节省: ~74 min (约 38%)\n\n如加上 flash-attn + padding_side 修复，可能再多节省 10-15%。\n\n6. Full Study 建议参数\n----------------------\n\npython scripts/run_pipeline.py \\\n  --model_path ... \\\n  --batch_size 64 \\\n  --feat_batch_size 24\n\n同时在代码中修复:\n  tokenizer.padding_side = \"left\"\n",
      "numLines": 111,
      "startLine": 1,
      "totalLines": 111
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01Aw7dn5djhnoHYe787y8ePQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "b998d7ab-e332-4fc2-a09b-528f6b1d3cb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFhM6NxjThSNdEd1bZBRCS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5264,
      "cache_read_input_tokens": 37624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5264
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-12T12:50:21.068Z_

<details><summary>↩ Tool result · `toolu_01Aw7dn5djhnoHYe787y8ePQ`</summary>

```text
1	"""
2	MVP Pilot Saturation Study — Complete Pipeline (Steps 2-5)
3	
4	Generates recursive depth chains from C4 seed data using Qwen2.5-1.5B,
5	extracts statistical features, and runs distinguishability analysis.
6	
7	Input:  C4 validation split (streamed from HuggingFace)
8	Output: data/depth_{0..K}.jsonl, data/features.csv, results/*.json + summary.txt
9	
10	Key deps: torch, transformers, datasets, scipy, lightgbm, sklearn, tqdm
11	"""
12	
13	import argparse
14	import json
15	import logging
16	import math
17	import os
18	import sys
19	from collections import Counter
20	from pathlib import Path
21	
22	import numpy as np
23	import torch
24	from scipy import stats
25	from tqdm import tqdm
26	
27	logging.basicConfig(
28	    level=logging.INFO,
29	    format="%(asctime)s [%(levelname)s] %(message)s",
30	    datefmt="%H:%M:%S",
31	)
32	log = logging.getLogger(__name__)
33	
34	
35	# ---------------------------------------------------------------------------
36	# Utility: simple 4-gram BLEU (no nltk dependency)
37	# ---------------------------------------------------------------------------
38	
39	def ngrams(tokens, n):
40	    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]
41	
42	
43	def simple_bleu(candidate_tokens, reference_tokens, max_n=4):
44	    """Compute sentence-level BLEU up to max_n grams with brevity penalty."""
45	    if len(candidate_tokens) == 0:
46	        return 0.0
47	    precisions = []
48	    for n in range(1, max_n + 1):
49	        cand_ngrams = ngrams(candidate_tokens, n)
50	        ref_ngrams = ngrams(reference_tokens, n)
51	        if not cand_ngrams:
52	            precisions.append(0.0)
53	            continue
54	        ref_counts = Counter(ref_ngrams)
55	        clipped = 0
56	        cand_counts = Counter(cand_ngrams)
57	        for ng, cnt in cand_counts.items():
58	            clipped += min(cnt, ref_counts.get(ng, 0))
59	        precisions.append(clipped / len(cand_ngrams))
60	    if any(p == 0 for p in precisions):
61	        return 0.0
62	    log_avg = sum(math.log(p) for p in precisions) / max_n
63	    bp = min(1.0, math.exp(1 - len(reference_tokens) / max(len(candidate_tokens), 1)))
64	    return bp * math.exp(log_avg)
65	
66	
67	# ===================================================================
68	# Step 2: Seed data preparation
69	# ===================================================================
70	
71	def prepare_seed_data(tokenizer, data_dir: Path, num_samples: int, max_tokens: int = 256):
72	    """Download C4 validation, truncate to max_tokens, save as depth_0.jsonl."""
73	    out_path = data_dir / "depth_0.jsonl"
74	    if out_path.exists() and sum(1 for _ in open(out_path)) >= num_samples:
75	        log.info("depth_0.jsonl already exists with enough samples — skipping")
76	        return
77	
78	    from datasets import load_dataset
79	
80	    # Use a single validation shard to avoid slow full-tree listing on proxied networks
81	    hf_endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
82	    C4_SHARD_URL = f"{hf_endpoint}/datasets/allenai/c4/resolve/main/en/c4-validation.00000-of-00008.json.gz"
83	    log.info("Loading C4 validation shard (streaming) ...")
84	    try:
85	        ds = load_dataset("json", data_files=C4_SHARD_URL, split="train", streaming=True)
86	    except Exception as e:
87	        log.warning(f"Direct shard download failed ({e}), falling back to full dataset listing")
88	        ds = load_dataset("allenai/c4", "en", split="validation", streaming=True)
89	
90	    records = []
91	    for i, example in enumerate(tqdm(ds, total=num_samples, desc="Sampling C4")):
92	        if i >= num_samples:
93	            break
94	        text = example["text"].strip()
95	        if not text:
96	            continue
97	        ids = tokenizer.encode(text, add_special_tokens=False)[:max_tokens]
98	        truncated = tokenizer.decode(ids, skip_special_tokens=True)
99	        records.append({"text": truncated, "doc_id": len(records)})
100	        if len(records) >= num_samples:
101	            break
102	
103	    data_dir.mkdir(parents=True, exist_ok=True)
104	    with open(out_path, "w") as f:
105	        for r in records:
106	            f.write(json.dumps(r, ensure_ascii=False) + "\n")
107	    log.info(f"Saved {len(records)} seed documents to {out_path}")
108	
109	
110	# ===================================================================
111	# Step 3: Recursive depth chain generation
112	# ===================================================================
113	
114	REWRITE_PROMPT = (
115	    "Below is a passage. Write a new passage of similar length on the same "
116	    "topic and in the same style.\n\n"
117	    "Original passage:\n{prev_text}\n\nNew passage:\n"
118	)
119	
120	
121	def load_jsonl(path: Path):
122	    with open(path) as f:
123	        return [json.loads(line) for line in f]
124	
125	
126	def generate_depth_chain(
127	    model,
128	    tokenizer,
129	    data_dir: Path,
130	    max_depth: int,
131	    batch_size: int,
132	    max_new_tokens: int = 256,
133	):
134	    """Generate depths 1..max_depth via prompt-chain rewriting."""
135	    for depth in range(1, max_depth + 1):
136	        out_path = data_dir / f"depth_{depth}.jsonl"
137	        prev_path = data_dir / f"depth_{depth - 1}.jsonl"
138	
139	        if out_path.exists() and sum(1 for _ in open(out_path)) >= sum(1 for _ in open(prev_path)):
140	            log.info(f"depth_{depth}.jsonl already complete — skipping")
141	            continue
142	
143	        prev_records = load_jsonl(prev_path)
144	        log.info(f"Generating depth {depth} ({len(prev_records)} docs, batch_size={batch_size}) ...")
145	
146	        results = []
147	        for start in tqdm(range(0, len(prev_records), batch_size), desc=f"depth {depth}"):
148	            batch = prev_records[start : start + batch_size]
149	            prompts = [REWRITE_PROMPT.format(prev_text=r["text"]) for r in batch]
150	
151	            inputs = tokenizer(
152	                prompts,
153	                return_tensors="pt",
154	                padding=True,
155	                truncation=True,
156	                max_length=512,
157	            ).to(model.device)
158	
159	            with torch.no_grad():
160	                outputs = model.generate(
161	                    **inputs,
162	                    max_new_tokens=max_new_tokens,
163	                    do_sample=True,
164	                    top_p=0.95,
165	                    temperature=1.0,
166	                    pad_token_id=tokenizer.pad_token_id,
167	                )
168	
169	            for j, out_ids in enumerate(outputs):
170	                prompt_len = inputs["input_ids"].shape[1]
171	                generated_ids = out_ids[prompt_len:]
172	                text = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
173	                results.append({"text": text, "doc_id": batch[j]["doc_id"]})
174	
175	            torch.cuda.empty_cache()
176	
177	        with open(out_path, "w") as f:
178	            for r in results:
179	                f.write(json.dumps(r, ensure_ascii=False) + "\n")
180	        log.info(f"Saved {len(results)} docs to {out_path}")
181	
182	
183	# ===================================================================
184	# Step 4: Feature extraction
185	# ===================================================================
186	
187	def compute_surprisal_features(model, tokenizer, texts, batch_size=8):
188	    """Compute 9-dim surprisal statistics per text using batched inference."""
189	    all_features = []
190	    for start in tqdm(range(0, len(texts), batch_size), desc="Surprisal"):
191	        batch_texts = texts[start : start + batch_size]
192	        inputs = tokenizer(
193	            batch_texts,
194	            return_tensors="pt",
195	            padding=True,
196	            truncation=True,
197	            max_length=512,
198	        ).to(model.device)
199	
200	        with torch.no_grad():
201	            logits = model(**inputs).logits  # (B, T, V)
202	
203	        log_probs = torch.log_softmax(logits, dim=-1)  # (B, T, V)
204	        input_ids = inputs["input_ids"]  # (B, T)
205	
206	        for i in range(len(batch_texts)):
207	            mask = inputs["attention_mask"][i].bool()
208	            seq_len = mask.sum().item()
209	            if seq_len < 3:
210	                all_features.append([0.0] * 9)
211	                continue
212	
213	            token_ids = input_ids[i, :seq_len]
214	            # surprisal of each token given prefix: -log p(x_t | x_{&lt;t})
215	            # shift: logits[t] predicts token[t+1]
216	            token_log_probs = []
217	            for t in range(1, seq_len):
218	                lp = log_probs[i, t - 1, token_ids[t]].item()
219	                token_log_probs.append(-lp)  # surprisal = -log_prob
220	
221	            arr = np.array(token_log_probs)
222	            if len(arr) < 3:
223	                all_features.append([0.0] * 9)
224	                continue
225	
226	            d1 = np.diff(arr)
227	            d2 = np.diff(d1) if len(d1) > 1 else np.array([0.0])
228	
229	            feats = [
230	                float(np.mean(arr)),
231	                float(np.std(arr)),
232	                float(stats.skew(arr)),
233	                float(stats.kurtosis(arr)),
234	                float(np.mean(d1)),
235	                float(np.std(d1)),
236	                float(stats.skew(d1)) if len(d1) >= 3 else 0.0,
237	                float(np.mean(d2)),
238	                float(np.std(d2)),
239	            ]
240	            all_features.append(feats)
241	
242	        torch.cuda.empty_cache()
243	
244	    return all_features
245	
246	
247	def compute_vocab_diversity(texts, tokenizer, depth_texts_map, depth, sample_bleu=200, bleu_refs=100):
248	    """Compute 3-dim vocabulary diversity features: TTR, hapax ratio, self-BLEU."""
249	    features = []
250	    # tokenize all texts at word level (split on whitespace for simplicity)
251	    tokenized = [t.split() for t in texts]
252	
253	    # pre-select indices for self-BLEU (sample up to sample_bleu texts)
254	    bleu_indices = list(range(len(texts)))
255	    if len(bleu_indices) > sample_bleu:
256	        rng = np.random.RandomState(42 + depth)
257	        bleu_indices = rng.choice(bleu_indices, sample_bleu, replace=False).tolist()
258	    bleu_set = set(bleu_indices)
259	
260	    # pre-tokenize for BLEU refs
261	    same_depth_tokens = tokenized  # all texts from this depth
262	
263	    for idx, tokens in enumerate(tqdm(tokenized, desc=f"VocabDiv d={depth}", leave=False)):
264	        total = len(tokens)
265	        if total == 0:
266	            features.append([0.0, 0.0, 0.0])
267	            continue
268	
269	        unique = set(tokens)
270	        ttr = len(unique) / total
271	
272	        freq = Counter(tokens)
273	        hapax = sum(1 for v in freq.values() if v == 1)
274	        hapax_ratio = hapax / max(len(unique), 1)
275	
276	        # self-BLEU: only compute for sampled indices
277	        if idx in bleu_set:
278	            rng_local = np.random.RandomState(idx)
279	            ref_pool = [j for j in range(len(same_depth_tokens)) if j != idx]
280	            if len(ref_pool) > bleu_refs:
281	                ref_pool = rng_local.choice(ref_pool, bleu_refs, replace=False).tolist()
282	            bleu_scores = [
283	                simple_bleu(tokens, same_depth_tokens[j]) for j in ref_pool
284	            ]
285	            self_bleu = float(np.mean(bleu_scores)) if bleu_scores else 0.0
286	        else:
287	            self_bleu = float("nan")
288	
289	        features.append([ttr, hapax_ratio, self_bleu])
290	
291	    return features
292	
293	
294	def compute_tail_features(texts):
295	    """Compute 3-dim tail-thinning features: freq kurtosis, freq entropy, low-freq ratio."""
296	    features = []
297	    for text in texts:
298	        tokens = text.split()
299	        if len(tokens) < 2:
300	            features.append([0.0, 0.0, 0.0])
301	            continue
302	        freq = Counter(tokens)
303	        counts = np.array(list(freq.values()), dtype=float)
304	
305	        kurt = float(stats.kurtosis(counts)) if len(counts) >= 4 else 0.0
306	
307	        total = counts.sum()
308	        probs = counts / total
309	        entropy = float(-np.sum(probs * np.log2(probs + 1e-12)))
310	
311	        low_freq_ratio = float(np.sum(counts == 1)) / max(len(counts), 1)
312	
313	        features.append([kurt, entropy, low_freq_ratio])
314	
315	    return features
316	
317	
318	SURPRISAL_COLS = [
319	    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
320	    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
321	    "surp_d2_mean", "surp_d2_std",
322	]
323	VOCAB_COLS = ["ttr", "hapax_ratio", "self_bleu"]
324	TAIL_COLS = ["freq_kurtosis", "freq_entropy", "low_freq_ratio"]
325	ALL_FEAT_COLS = SURPRISAL_COLS + VOCAB_COLS + TAIL_COLS
326	
327	
328	def extract_all_features(model, tokenizer, data_dir: Path, max_depth: int, batch_size: int):
329	    """Extract features for all depths and save to features.csv."""
330	    import csv
331	
332	    out_path = data_dir / "features.csv"
333	    expected_total = 0
334	    for d in range(max_depth + 1):
335	        p = data_dir / f"depth_{d}.jsonl"
336	        if p.exists():
337	            expected_total += sum(1 for _ in open(p))
338	
339	    if out_path.exists() and sum(1 for _ in open(out_path)) - 1 >= expected_total:
340	        log.info("features.csv already complete — skipping")
341	        return
342	
343	    log.info("Extracting features for all depths ...")
344	
345	    # group texts by depth for self-BLEU
346	    depth_texts = {}
347	    for d in range(max_depth + 1):
348	        records = load_jsonl(data_dir / f"depth_{d}.jsonl")
349	        depth_texts[d] = records
350	
351	    rows = []
352	    for d in range(max_depth + 1):
353	        records = depth_texts[d]
354	        texts = [r["text"] for r in records]
355	        doc_ids = [r["doc_id"] for r in records]
356	        log.info(f"  depth {d}: {len(texts)} texts")
357	
358	        surp = compute_surprisal_features(model, tokenizer, texts, batch_size=batch_size)
359	        vocab = compute_vocab_diversity(
360	            texts, tokenizer, depth_texts, d
361	        )
362	        tail = compute_tail_features(texts)
363	
364	        for i in range(len(texts)):
365	            row = {"doc_id": doc_ids[i], "depth": d}
366	            for j, col in enumerate(SURPRISAL_COLS):
367	                row[col] = surp[i][j]
368	            for j, col in enumerate(VOCAB_COLS):
369	                row[col] = vocab[i][j]
370	            for j, col in enumerate(TAIL_COLS):
371	                row[col] = tail[i][j]
372	            rows.append(row)
373	
374	    with open(out_path, "w", newline="") as f:
375	        writer = csv.DictWriter(f, fieldnames=["doc_id", "depth"] + ALL_FEAT_COLS)
376	        writer.writeheader()
377	        writer.writerows(rows)
378	    log.info(f"Saved {len(rows)} feature rows to {out_path}")
379	
380	
381	# ===================================================================
382	# Step 5: Distinguishability analysis
383	# ===================================================================
384	
385	def run_analysis(data_dir: Path, results_dir: Path, max_depth: int):
386	    """Pairwise AUC, JSD, K*, ordinal classification, feature importance."""
387	    import csv
388	
389	    import lightgbm as lgb
390	    from sklearn.model_selection import StratifiedKFold
391	    from sklearn.metrics import roc_auc_score, mean_absolute_error, accuracy_score
392	
393	    results_dir.mkdir(parents=True, exist_ok=True)
394	
395	    # load features
396	    feat_path = data_dir / "features.csv"
397	    log.info(f"Loading features from {feat_path} ...")
398	    with open(feat_path) as f:
399	        reader = csv.DictReader(f)
400	        rows = list(reader)
401	
402	    # build arrays
403	    depths = np.array([int(r["depth"]) for r in rows])
404	    feat_matrix = np.array(
405	        [[float(r[c]) if r[c] != "" and r[c] != "nan" else np.nan for c in ALL_FEAT_COLS] for r in rows]
406	    )
407	    # fill NaN with column mean for classification
408	    col_means = np.nanmean(feat_matrix, axis=0)
409	    for j in range(feat_matrix.shape[1]):
410	        mask = np.isnan(feat_matrix[:, j])
411	        feat_matrix[mask, j] = col_means[j]
412	
413	    # --- Pairwise AUC ---
414	    log.info("Computing pairwise AUC ...")
415	    pairwise_auc = {}
416	    for k in range(1, max_depth + 1):
417	        mask = (depths == k - 1) | (depths == k)
418	        X = feat_matrix[mask]
419	        y = (depths[mask] == k).astype(int)
420	        if len(np.unique(y)) < 2:
421	            pairwise_auc[f"{k-1}v{k}"] = float("nan")
422	            continue
423	
424	        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
425	        fold_aucs = []
426	        for train_idx, test_idx in skf.split(X, y):
427	            clf = lgb.LGBMClassifier(
428	                n_estimators=200, max_depth=6, learning_rate=0.05,
429	                num_leaves=31, verbose=-1, n_jobs=-1,
430	            )
431	            clf.fit(X[train_idx], y[train_idx])
432	            proba = clf.predict_proba(X[test_idx])[:, 1]
433	            fold_aucs.append(roc_auc_score(y[test_idx], proba))
434	        auc_mean = float(np.mean(fold_aucs))
435	        pairwise_auc[f"{k-1}v{k}"] = round(auc_mean, 4)
436	        log.info(f"  AUC({k-1} vs {k}) = {auc_mean:.4f}")
437	
438	    with open(results_dir / "pairwise_auc.json", "w") as f:
439	        json.dump(pairwise_auc, f, indent=2)
440	
441	    # --- JSD ---
442	    log.info("Computing pairwise JSD ...")
443	    pairwise_jsd = {}
444	    for k in range(1, max_depth + 1):
445	        mask_prev = depths == k - 1
446	        mask_curr = depths == k
447	        feat_prev = feat_matrix[mask_prev]
448	        feat_curr = feat_matrix[mask_curr]
449	
450	        jsds_per_feat = []
451	        for j in range(feat_matrix.shape[1]):
452	            a = feat_prev[:, j]
453	            b = feat_curr[:, j]
454	            # histogram-based JSD
455	            lo = min(a.min(), b.min())
456	            hi = max(a.max(), b.max())
457	            if hi - lo < 1e-12:
458	                jsds_per_feat.append(0.0)
459	                continue
460	            bins = np.linspace(lo, hi, 51)
461	            p_hist = np.histogram(a, bins=bins, density=True)[0] + 1e-12
462	            q_hist = np.histogram(b, bins=bins, density=True)[0] + 1e-12
463	            p_hist /= p_hist.sum()
464	            q_hist /= q_hist.sum()
465	            m = 0.5 * (p_hist + q_hist)
466	            jsd = 0.5 * np.sum(p_hist * np.log2(p_hist / m)) + 0.5 * np.sum(q_hist * np.log2(q_hist / m))
467	            jsds_per_feat.append(float(jsd))
468	
469	        jsd_mean = float(np.mean(jsds_per_feat))
470	        pairwise_jsd[f"{k-1}v{k}"] = round(jsd_mean, 6)
471	        log.info(f"  JSD({k-1} vs {k}) = {jsd_mean:.6f}")
472	
473	    with open(results_dir / "jsd.json", "w") as f:
474	        json.dump(pairwise_jsd, f, indent=2)
475	
476	    # --- K* ---
477	    k_star = 0
478	    for k in range(1, max_depth + 1):
479	        key = f"{k-1}v{k}"
480	        if pairwise_auc.get(key, 0) > 0.60:
481	            k_star = k
482	
483	    # --- Ordinal classification ---
484	    log.info("Running ordinal LightGBM classification ...")
485	    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
486	    all_preds = np.zeros_like(depths, dtype=float)
487	    all_true = depths.copy()
488	
489	    importances = np.zeros(len(ALL_FEAT_COLS))
490	    for train_idx, test_idx in skf.split(feat_matrix, depths):
491	        clf = lgb.LGBMClassifier(
492	            n_estimators=300, max_depth=8, learning_rate=0.05,
493	            num_leaves=63, verbose=-1, n_jobs=-1,
494	            num_class=max_depth + 1,
495	            objective="multiclass",
496	        )
497	        clf.fit(feat_matrix[train_idx], depths[train_idx])
498	        preds = clf.predict(feat_matrix[test_idx])
499	        all_preds[test_idx] = preds
500	        importances += clf.feature_importances_
501	
502	    importances /= 5.0
503	    mae = float(mean_absolute_error(all_true, all_preds))
504	    accuracy = float(accuracy_score(all_true, all_preds.astype(int)))
505	    log.info(f"  Ordinal MAE = {mae:.4f}, Accuracy = {accuracy:.4f}, K* = {k_star}")
506	
507	    ordinal_results = {"mae": round(mae, 4), "accuracy": round(accuracy, 4), "k_star": k_star}
508	    with open(results_dir / "ordinal_results.json", "w") as f:
509	        json.dump(ordinal_results, f, indent=2)
510	
511	    # --- Feature importance ---
512	    feat_imp = sorted(
513	        [{"feature": ALL_FEAT_COLS[i], "importance": float(importances[i])} for i in range(len(ALL_FEAT_COLS))],
514	        key=lambda x: x["importance"],
515	        reverse=True,
516	    )[:10]
517	    with open(results_dir / "feature_importance.json", "w") as f:
518	        json.dump(feat_imp, f, indent=2)
519	
520	    # --- Summary ---
521	    summary_lines = [
522	        "=" * 60,
523	        "MVP Pilot Saturation Study — Results Summary",
524	        "=" * 60,
525	        "",
526	        "Pairwise AUC (adjacent depths):",
527	    ]
528	    for k in range(1, max_depth + 1):
529	        key = f"{k-1}v{k}"
530	        summary_lines.append(f"  depth {k-1} vs {k}: AUC = {pairwise_auc.get(key, 'N/A')}")
531	    summary_lines += [
532	        "",
533	        "Pairwise JSD (adjacent depths):",
534	    ]
535	    for k in range(1, max_depth + 1):
536	        key = f"{k-1}v{k}"
537	        summary_lines.append(f"  depth {k-1} vs {k}: JSD = {pairwise_jsd.get(key, 'N/A')}")
538	    summary_lines += [
539	        "",
540	        f"K* (max depth with AUC > 0.60): {k_star}",
541	        "",
542	        f"Ordinal Classification (6-class, 5-fold CV):",
543	        f"  MAE = {mae:.4f}",
544	        f"  Accuracy = {accuracy:.4f}",
545	        "",
546	        "Top-10 Feature Importance:",
547	    ]
548	    for fi in feat_imp:
549	        summary_lines.append(f"  {fi['feature']:20s} {fi['importance']:.1f}")
550	    summary_lines.append("")
551	    summary_lines.append("=" * 60)
552	
553	    summary_text = "\n".join(summary_lines)
554	    with open(results_dir / "summary.txt", "w") as f:
555	        f.write(summary_text)
556	    log.info(f"\n{summary_text}")
557	
558	
559	# ===================================================================
560	# Main
561	# ===================================================================
562	
563	def main():
564	    parser = argparse.ArgumentParser(description="MVP Pilot Saturation Study Pipeline")
565	    parser.add_argument("--model_path", type=str,
566	                        default="/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct")
567	    parser.add_argument("--data_dir", type=str,
568	                        default="/root/autodl-tmp/gen-depth-contamination/data")
569	    parser.add_argument("--results_dir", type=str,
570	                        default="/root/autodl-tmp/gen-depth-contamination/results")
571	    parser.add_argument("--num_samples", type=int, default=5000)
572	    parser.add_argument("--max_depth", type=int, default=5)
573	    parser.add_argument("--batch_size", type=int, default=16)
574	    parser.add_argument("--feat_batch_size", type=int, default=8,
575	                        help="Batch size for surprisal feature extraction (uses more VRAM)")
576	    args = parser.parse_args()
577	
578	    data_dir = Path(args.data_dir)
579	    results_dir = Path(args.results_dir)
580	    data_dir.mkdir(parents=True, exist_ok=True)
581	    results_dir.mkdir(parents=True, exist_ok=True)
582	
583	    log.info(f"Model: {args.model_path}")
584	    log.info(f"Data dir: {data_dir}")
585	    log.info(f"Samples: {args.num_samples}, Max depth: {args.max_depth}")
586	
587	    # Load model + tokenizer
588	    from transformers import AutoModelForCausalLM, AutoTokenizer
589	
590	    log.info("Loading tokenizer ...")
591	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
592	    if tokenizer.pad_token is None:
593	        tokenizer.pad_token = tokenizer.eos_token
594	        tokenizer.pad_token_id = tokenizer.eos_token_id
595	
596	    log.info("Loading model ...")
597	    model = AutoModelForCausalLM.from_pretrained(
598	        args.model_path,
599	        torch_dtype=torch.float16,
600	        device_map="auto",
601	        trust_remote_code=True,
602	    )
603	    model.eval()
604	    log.info(f"Model loaded on {model.device}")
605	
606	    # Step 2
607	    log.info("=" * 40 + " Step 2: Seed Data " + "=" * 40)
608	    prepare_seed_data(tokenizer, data_dir, args.num_samples)
609	
610	    # Step 3
611	    log.info("=" * 40 + " Step 3: Depth Chain " + "=" * 40)
612	    generate_depth_chain(model, tokenizer, data_dir, args.max_depth, args.batch_size)
613	
614	    # Step 4
615	    log.info("=" * 40 + " Step 4: Feature Extraction " + "=" * 40)
616	    extract_all_features(model, tokenizer, data_dir, args.max_depth, args.feat_batch_size)
617	
618	    # Step 5
619	    log.info("=" * 40 + " Step 5: Analysis " + "=" * 40)
620	    run_analysis(data_dir, results_dir, args.max_depth)
621	
622	    log.info("Pipeline complete.")
623	
624	
625	if __name__ == "__main__":
626	    main()
627	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "5cf6729e-b63a-4502-a1d3-ec07ce1fce8b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_pipeline.py",
      "content": "\"\"\"\nMVP Pilot Saturation Study — Complete Pipeline (Steps 2-5)\n\nGenerates recursive depth chains from C4 seed data using Qwen2.5-1.5B,\nextracts statistical features, and runs distinguishability analysis.\n\nInput:  C4 validation split (streamed from HuggingFace)\nOutput: data/depth_{0..K}.jsonl, data/features.csv, results/*.json + summary.txt\n\nKey deps: torch, transformers, datasets, scipy, lightgbm, sklearn, tqdm\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport math\nimport os\nimport sys\nfrom collections import Counter\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nfrom scipy import stats\nfrom tqdm import tqdm\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Utility: simple 4-gram BLEU (no nltk dependency)\n# ---------------------------------------------------------------------------\n\ndef ngrams(tokens, n):\n    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]\n\n\ndef simple_bleu(candidate_tokens, reference_tokens, max_n=4):\n    \"\"\"Compute sentence-level BLEU up to max_n grams with brevity penalty.\"\"\"\n    if len(candidate_tokens) == 0:\n        return 0.0\n    precisions = []\n    for n in range(1, max_n + 1):\n        cand_ngrams = ngrams(candidate_tokens, n)\n        ref_ngrams = ngrams(reference_tokens, n)\n        if not cand_ngrams:\n            precisions.append(0.0)\n            continue\n        ref_counts = Counter(ref_ngrams)\n        clipped = 0\n        cand_counts = Counter(cand_ngrams)\n        for ng, cnt in cand_counts.items():\n            clipped += min(cnt, ref_counts.get(ng, 0))\n        precisions.append(clipped / len(cand_ngrams))\n    if any(p == 0 for p in precisions):\n        return 0.0\n    log_avg = sum(math.log(p) for p in precisions) / max_n\n    bp = min(1.0, math.exp(1 - len(reference_tokens) / max(len(candidate_tokens), 1)))\n    return bp * math.exp(log_avg)\n\n\n# ===================================================================\n# Step 2: Seed data preparation\n# ===================================================================\n\ndef prepare_seed_data(tokenizer, data_dir: Path, num_samples: int, max_tokens: int = 256):\n    \"\"\"Download C4 validation, truncate to max_tokens, save as depth_0.jsonl.\"\"\"\n    out_path = data_dir / \"depth_0.jsonl\"\n    if out_path.exists() and sum(1 for _ in open(out_path)) >= num_samples:\n        log.info(\"depth_0.jsonl already exists with enough samples — skipping\")\n        return\n\n    from datasets import load_dataset\n\n    # Use a single validation shard to avoid slow full-tree listing on proxied networks\n    hf_endpoint = os.environ.get(\"HF_ENDPOINT\", \"https://huggingface.co\")\n    C4_SHARD_URL = f\"{hf_endpoint}/datasets/allenai/c4/resolve/main/en/c4-validation.00000-of-00008.json.gz\"\n    log.info(\"Loading C4 validation shard (streaming) ...\")\n    try:\n        ds = load_dataset(\"json\", data_files=C4_SHARD_URL, split=\"train\", streaming=True)\n    except Exception as e:\n        log.warning(f\"Direct shard download failed ({e}), falling back to full dataset listing\")\n        ds = load_dataset(\"allenai/c4\", \"en\", split=\"validation\", streaming=True)\n\n    records = []\n    for i, example in enumerate(tqdm(ds, total=num_samples, desc=\"Sampling C4\")):\n        if i >= num_samples:\n            break\n        text = example[\"text\"].strip()\n        if not text:\n            continue\n        ids = tokenizer.encode(text, add_special_tokens=False)[:max_tokens]\n        truncated = tokenizer.decode(ids, skip_special_tokens=True)\n        records.append({\"text\": truncated, \"doc_id\": len(records)})\n        if len(records) >= num_samples:\n            break\n\n    data_dir.mkdir(parents=True, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        for r in records:\n            f.write(json.dumps(r, ensure_ascii=False) + \"\\n\")\n    log.info(f\"Saved {len(records)} seed documents to {out_path}\")\n\n\n# ===================================================================\n# Step 3: Recursive depth chain generation\n# ===================================================================\n\nREWRITE_PROMPT = (\n    \"Below is a passage. Write a new passage of similar length on the same \"\n    \"topic and in the same style.\\n\\n\"\n    \"Original passage:\\n{prev_text}\\n\\nNew passage:\\n\"\n)\n\n\ndef load_jsonl(path: Path):\n    with open(path) as f:\n        return [json.loads(line) for line in f]\n\n\ndef generate_depth_chain(\n    model,\n    tokenizer,\n    data_dir: Path,\n    max_depth: int,\n    batch_size: int,\n    max_new_tokens: int = 256,\n):\n    \"\"\"Generate depths 1..max_depth via prompt-chain rewriting.\"\"\"\n    for depth in range(1, max_depth + 1):\n        out_path = data_dir / f\"depth_{depth}.jsonl\"\n        prev_path = data_dir / f\"depth_{depth - 1}.jsonl\"\n\n        if out_path.exists() and sum(1 for _ in open(out_path)) >= sum(1 for _ in open(prev_path)):\n            log.info(f\"depth_{depth}.jsonl already complete — skipping\")\n            continue\n\n        prev_records = load_jsonl(prev_path)\n        log.info(f\"Generating depth {depth} ({len(prev_records)} docs, batch_size={batch_size}) ...\")\n\n        results = []\n        for start in tqdm(range(0, len(prev_records), batch_size), desc=f\"depth {depth}\"):\n            batch = prev_records[start : start + batch_size]\n            prompts = [REWRITE_PROMPT.format(prev_text=r[\"text\"]) for r in batch]\n\n            inputs = tokenizer(\n                prompts,\n                return_tensors=\"pt\",\n                padding=True,\n                truncation=True,\n                max_length=512,\n            ).to(model.device)\n\n            with torch.no_grad():\n                outputs = model.generate(\n                    **inputs,\n                    max_new_tokens=max_new_tokens,\n                    do_sample=True,\n                    top_p=0.95,\n                    temperature=1.0,\n                    pad_token_id=tokenizer.pad_token_id,\n                )\n\n            for j, out_ids in enumerate(outputs):\n                prompt_len = inputs[\"input_ids\"].shape[1]\n                generated_ids = out_ids[prompt_len:]\n                text = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()\n                results.append({\"text\": text, \"doc_id\": batch[j][\"doc_id\"]})\n\n            torch.cuda.empty_cache()\n\n        with open(out_path, \"w\") as f:\n            for r in results:\n                f.write(json.dumps(r, ensure_ascii=False) + \"\\n\")\n        log.info(f\"Saved {len(results)} docs to {out_path}\")\n\n\n# ===================================================================\n# Step 4: Feature extraction\n# ===================================================================\n\ndef compute_surprisal_features(model, tokenizer, texts, batch_size=8):\n    \"\"\"Compute 9-dim surprisal statistics per text using batched inference.\"\"\"\n    all_features = []\n    for start in tqdm(range(0, len(texts), batch_size), desc=\"Surprisal\"):\n        batch_texts = texts[start : start + batch_size]\n        inputs = tokenizer(\n            batch_texts,\n            return_tensors=\"pt\",\n            padding=True,\n            truncation=True,\n            max_length=512,\n        ).to(model.device)\n\n        with torch.no_grad():\n            logits = model(**inputs).logits  # (B, T, V)\n\n        log_probs = torch.log_softmax(logits, dim=-1)  # (B, T, V)\n        input_ids = inputs[\"input_ids\"]  # (B, T)\n\n        for i in range(len(batch_texts)):\n            mask = inputs[\"attention_mask\"][i].bool()\n            seq_len = mask.sum().item()\n            if seq_len < 3:\n                all_features.append([0.0] * 9)\n                continue\n\n            token_ids = input_ids[i, :seq_len]\n            # surprisal of each token given prefix: -log p(x_t | x_{&lt;t})\n            # shift: logits[t] predicts token[t+1]\n            token_log_probs = []\n            for t in range(1, seq_len):\n                lp = log_probs[i, t - 1, token_ids[t]].item()\n                token_log_probs.append(-lp)  # surprisal = -log_prob\n\n            arr = np.array(token_log_probs)\n            if len(arr) < 3:\n                all_features.append([0.0] * 9)\n                continue\n\n            d1 = np.diff(arr)\n            d2 = np.diff(d1) if len(d1) > 1 else np.array([0.0])\n\n            feats = [\n                float(np.mean(arr)),\n                float(np.std(arr)),\n                float(stats.skew(arr)),\n                float(stats.kurtosis(arr)),\n                float(np.mean(d1)),\n                float(np.std(d1)),\n                float(stats.skew(d1)) if len(d1) >= 3 else 0.0,\n                float(np.mean(d2)),\n                float(np.std(d2)),\n            ]\n            all_features.append(feats)\n\n        torch.cuda.empty_cache()\n\n    return all_features\n\n\ndef compute_vocab_diversity(texts, tokenizer, depth_texts_map, depth, sample_bleu=200, bleu_refs=100):\n    \"\"\"Compute 3-dim vocabulary diversity features: TTR, hapax ratio, self-BLEU.\"\"\"\n    features = []\n    # tokenize all texts at word level (split on whitespace for simplicity)\n    tokenized = [t.split() for t in texts]\n\n    # pre-select indices for self-BLEU (sample up to sample_bleu texts)\n    bleu_indices = list(range(len(texts)))\n    if len(bleu_indices) > sample_bleu:\n        rng = np.random.RandomState(42 + depth)\n        bleu_indices = rng.choice(bleu_indices, sample_bleu, replace=False).tolist()\n    bleu_set = set(bleu_indices)\n\n    # pre-tokenize for BLEU refs\n    same_depth_tokens = tokenized  # all texts from this depth\n\n    for idx, tokens in enumerate(tqdm(tokenized, desc=f\"VocabDiv d={depth}\", leave=False)):\n        total = len(tokens)\n        if total == 0:\n            features.append([0.0, 0.0, 0.0])\n            continue\n\n        unique = set(tokens)\n        ttr = len(unique) / total\n\n        freq = Counter(tokens)\n        hapax = sum(1 for v in freq.values() if v == 1)\n        hapax_ratio = hapax / max(len(unique), 1)\n\n        # self-BLEU: only compute for sampled indices\n        if idx in bleu_set:\n            rng_local = np.random.RandomState(idx)\n            ref_pool = [j for j in range(len(same_depth_tokens)) if j != idx]\n            if len(ref_pool) > bleu_refs:\n                ref_pool = rng_local.choice(ref_pool, bleu_refs, replace=False).tolist()\n            bleu_scores = [\n                simple_bleu(tokens, same_depth_tokens[j]) for j in ref_pool\n            ]\n            self_bleu = float(np.mean(bleu_scores)) if bleu_scores else 0.0\n        else:\n            self_bleu = float(\"nan\")\n\n        features.append([ttr, hapax_ratio, self_bleu])\n\n    return features\n\n\ndef compute_tail_features(texts):\n    \"\"\"Compute 3-dim tail-thinning features: freq kurtosis, freq entropy, low-freq ratio.\"\"\"\n    features = []\n    for text in texts:\n        tokens = text.split()\n        if len(tokens) < 2:\n            features.append([0.0, 0.0, 0.0])\n            continue\n        freq = Counter(tokens)\n        counts = np.array(list(freq.values()), dtype=float)\n\n        kurt = float(stats.kurtosis(counts)) if len(counts) >= 4 else 0.0\n\n        total = counts.sum()\n        probs = counts / total\n        entropy = float(-np.sum(probs * np.log2(probs + 1e-12)))\n\n        low_freq_ratio = float(np.sum(counts == 1)) / max(len(counts), 1)\n\n        features.append([kurt, entropy, low_freq_ratio])\n\n    return features\n\n\nSURPRISAL_COLS = [\n    \"surp_mean\", \"surp_std\", \"surp_skew\", \"surp_kurt\",\n    \"surp_d1_mean\", \"surp_d1_std\", \"surp_d1_skew\",\n    \"surp_d2_mean\", \"surp_d2_std\",\n]\nVOCAB_COLS = [\"ttr\", \"hapax_ratio\", \"self_bleu\"]\nTAIL_COLS = [\"freq_kurtosis\", \"freq_entropy\", \"low_freq_ratio\"]\nALL_FEAT_COLS = SURPRISAL_COLS + VOCAB_COLS + TAIL_COLS\n\n\ndef extract_all_features(model, tokenizer, data_dir: Path, max_depth: int, batch_size: int):\n    \"\"\"Extract features for all depths and save to features.csv.\"\"\"\n    import csv\n\n    out_path = data_dir / \"features.csv\"\n    expected_total = 0\n    for d in range(max_depth + 1):\n        p = data_dir / f\"depth_{d}.jsonl\"\n        if p.exists():\n            expected_total += sum(1 for _ in open(p))\n\n    if out_path.exists() and sum(1 for _ in open(out_path)) - 1 >= expected_total:\n        log.info(\"features.csv already complete — skipping\")\n        return\n\n    log.info(\"Extracting features for all depths ...\")\n\n    # group texts by depth for self-BLEU\n    depth_texts = {}\n    for d in range(max_depth + 1):\n        records = load_jsonl(data_dir / f\"depth_{d}.jsonl\")\n        depth_texts[d] = records\n\n    rows = []\n    for d in range(max_depth + 1):\n        records = depth_texts[d]\n        texts = [r[\"text\"] for r in records]\n        doc_ids = [r[\"doc_id\"] for r in records]\n        log.info(f\"  depth {d}: {len(texts)} texts\")\n\n        surp = compute_surprisal_features(model, tokenizer, texts, batch_size=batch_size)\n        vocab = compute_vocab_diversity(\n            texts, tokenizer, depth_texts, d\n        )\n        tail = compute_tail_features(texts)\n\n        for i in range(len(texts)):\n            row = {\"doc_id\": doc_ids[i], \"depth\": d}\n            for j, col in enumerate(SURPRISAL_COLS):\n                row[col] = surp[i][j]\n            for j, col in enumerate(VOCAB_COLS):\n                row[col] = vocab[i][j]\n            for j, col in enumerate(TAIL_COLS):\n                row[col] = tail[i][j]\n            rows.append(row)\n\n    with open(out_path, \"w\", newline=\"\") as f:\n        writer = csv.DictWriter(f, fieldnames=[\"doc_id\", \"depth\"] + ALL_FEAT_COLS)\n        writer.writeheader()\n        writer.writerows(rows)\n    log.info(f\"Saved {len(rows)} feature rows to {out_path}\")\n\n\n# ===================================================================\n# Step 5: Distinguishability analysis\n# ===================================================================\n\ndef run_analysis(data_dir: Path, results_dir: Path, max_depth: int):\n    \"\"\"Pairwise AUC, JSD, K*, ordinal classification, feature importance.\"\"\"\n    import csv\n\n    import lightgbm as lgb\n    from sklearn.model_selection import StratifiedKFold\n    from sklearn.metrics import roc_auc_score, mean_absolute_error, accuracy_score\n\n    results_dir.mkdir(parents=True, exist_ok=True)\n\n    # load features\n    feat_path = data_dir / \"features.csv\"\n    log.info(f\"Loading features from {feat_path} ...\")\n    with open(feat_path) as f:\n        reader = csv.DictReader(f)\n        rows = list(reader)\n\n    # build arrays\n    depths = np.array([int(r[\"depth\"]) for r in rows])\n    feat_matrix = np.array(\n        [[float(r[c]) if r[c] != \"\" and r[c] != \"nan\" else np.nan for c in ALL_FEAT_COLS] for r in rows]\n    )\n    # fill NaN with column mean for classification\n    col_means = np.nanmean(feat_matrix, axis=0)\n    for j in range(feat_matrix.shape[1]):\n        mask = np.isnan(feat_matrix[:, j])\n        feat_matrix[mask, j] = col_means[j]\n\n    # --- Pairwise AUC ---\n    log.info(\"Computing pairwise AUC ...\")\n    pairwise_auc = {}\n    for k in range(1, max_depth + 1):\n        mask = (depths == k - 1) | (depths == k)\n        X = feat_matrix[mask]\n        y = (depths[mask] == k).astype(int)\n        if len(np.unique(y)) < 2:\n            pairwise_auc[f\"{k-1}v{k}\"] = float(\"nan\")\n            continue\n\n        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)\n        fold_aucs = []\n        for train_idx, test_idx in skf.split(X, y):\n            clf = lgb.LGBMClassifier(\n                n_estimators=200, max_depth=6, learning_rate=0.05,\n                num_leaves=31, verbose=-1, n_jobs=-1,\n            )\n            clf.fit(X[train_idx], y[train_idx])\n            proba = clf.predict_proba(X[test_idx])[:, 1]\n            fold_aucs.append(roc_auc_score(y[test_idx], proba))\n        auc_mean = float(np.mean(fold_aucs))\n        pairwise_auc[f\"{k-1}v{k}\"] = round(auc_mean, 4)\n        log.info(f\"  AUC({k-1} vs {k}) = {auc_mean:.4f}\")\n\n    with open(results_dir / \"pairwise_auc.json\", \"w\") as f:\n        json.dump(pairwise_auc, f, indent=2)\n\n    # --- JSD ---\n    log.info(\"Computing pairwise JSD ...\")\n    pairwise_jsd = {}\n    for k in range(1, max_depth + 1):\n        mask_prev = depths == k - 1\n        mask_curr = depths == k\n        feat_prev = feat_matrix[mask_prev]\n        feat_curr = feat_matrix[mask_curr]\n\n        jsds_per_feat = []\n        for j in range(feat_matrix.shape[1]):\n            a = feat_prev[:, j]\n            b = feat_curr[:, j]\n            # histogram-based JSD\n            lo = min(a.min(), b.min())\n            hi = max(a.max(), b.max())\n            if hi - lo < 1e-12:\n                jsds_per_feat.append(0.0)\n                continue\n            bins = np.linspace(lo, hi, 51)\n            p_hist = np.histogram(a, bins=bins, density=True)[0] + 1e-12\n            q_hist = np.histogram(b, bins=bins, density=True)[0] + 1e-12\n            p_hist /= p_hist.sum()\n            q_hist /= q_hist.sum()\n            m = 0.5 * (p_hist + q_hist)\n            jsd = 0.5 * np.sum(p_hist * np.log2(p_hist / m)) + 0.5 * np.sum(q_hist * np.log2(q_hist / m))\n            jsds_per_feat.append(float(jsd))\n\n        jsd_mean = float(np.mean(jsds_per_feat))\n        pairwise_jsd[f\"{k-1}v{k}\"] = round(jsd_mean, 6)\n        log.info(f\"  JSD({k-1} vs {k}) = {jsd_mean:.6f}\")\n\n    with open(results_dir / \"jsd.json\", \"w\") as f:\n        json.dump(pairwise_jsd, f, indent=2)\n\n    # --- K* ---\n    k_star = 0\n    for k in range(1, max_depth + 1):\n        key = f\"{k-1}v{k}\"\n        if pairwise_auc.get(key, 0) > 0.60:\n            k_star = k\n\n    # --- Ordinal classification ---\n    log.info(\"Running ordinal LightGBM classification ...\")\n    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)\n    all_preds = np.zeros_like(depths, dtype=float)\n    all_true = depths.copy()\n\n    importances = np.zeros(len(ALL_FEAT_COLS))\n    for train_idx, test_idx in skf.split(feat_matrix, depths):\n        clf = lgb.LGBMClassifier(\n            n_estimators=300, max_depth=8, learning_rate=0.05,\n            num_leaves=63, verbose=-1, n_jobs=-1,\n            num_class=max_depth + 1,\n            objective=\"multiclass\",\n        )\n        clf.fit(feat_matrix[train_idx], depths[train_idx])\n        preds = clf.predict(feat_matrix[test_idx])\n        all_preds[test_idx] = preds\n        importances += clf.feature_importances_\n\n    importances /= 5.0\n    mae = float(mean_absolute_error(all_true, all_preds))\n    accuracy = float(accuracy_score(all_true, all_preds.astype(int)))\n    log.info(f\"  Ordinal MAE = {mae:.4f}, Accuracy = {accuracy:.4f}, K* = {k_star}\")\n\n    ordinal_results = {\"mae\": round(mae, 4), \"accuracy\": round(accuracy, 4), \"k_star\": k_star}\n    with open(results_dir / \"ordinal_results.json\", \"w\") as f:\n        json.dump(ordinal_results, f, indent=2)\n\n    # --- Feature importance ---\n    feat_imp = sorted(\n        [{\"feature\": ALL_FEAT_COLS[i], \"importance\": float(importances[i])} for i in range(len(ALL_FEAT_COLS))],\n        key=lambda x: x[\"importance\"],\n        reverse=True,\n    )[:10]\n    with open(results_dir / \"feature_importance.json\", \"w\") as f:\n        json.dump(feat_imp, f, indent=2)\n\n    # --- Summary ---\n    summary_lines = [\n        \"=\" * 60,\n        \"MVP Pilot Saturation Study — Results Summary\",\n        \"=\" * 60,\n        \"\",\n        \"Pairwise AUC (adjacent depths):\",\n    ]\n    for k in range(1, max_depth + 1):\n        key = f\"{k-1}v{k}\"\n        summary_lines.append(f\"  depth {k-1} vs {k}: AUC = {pairwise_auc.get(key, 'N/A')}\")\n    summary_lines += [\n        \"\",\n        \"Pairwise JSD (adjacent depths):\",\n    ]\n    for k in range(1, max_depth + 1):\n        key = f\"{k-1}v{k}\"\n        summary_lines.append(f\"  depth {k-1} vs {k}: JSD = {pairwise_jsd.get(key, 'N/A')}\")\n    summary_lines += [\n        \"\",\n        f\"K* (max depth with AUC > 0.60): {k_star}\",\n        \"\",\n        f\"Ordinal Classification (6-class, 5-fold CV):\",\n        f\"  MAE = {mae:.4f}\",\n        f\"  Accuracy = {accuracy:.4f}\",\n        \"\",\n        \"Top-10 Feature Importance:\",\n    ]\n    for fi in feat_imp:\n        summary_lines.append(f\"  {fi['feature']:20s} {fi['importance']:.1f}\")\n    summary_lines.append(\"\")\n    summary_lines.append(\"=\" * 60)\n\n    summary_text = \"\\n\".join(summary_lines)\n    with open(results_dir / \"summary.txt\", \"w\") as f:\n        f.write(summary_text)\n    log.info(f\"\\n{summary_text}\")\n\n\n# ===================================================================\n# Main\n# ===================================================================\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"MVP Pilot Saturation Study Pipeline\")\n    parser.add_argument(\"--model_path\", type=str,\n                        default=\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct\")\n    parser.add_argument(\"--data_dir\", type=str,\n                        default=\"/root/autodl-tmp/gen-depth-contamination/data\")\n    parser.add_argument(\"--results_dir\", type=str,\n                        default=\"/root/autodl-tmp/gen-depth-contamination/results\")\n    parser.add_argument(\"--num_samples\", type=int, default=5000)\n    parser.add_argument(\"--max_depth\", type=int, default=5)\n    parser.add_argument(\"--batch_size\", type=int, default=16)\n    parser.add_argument(\"--feat_batch_size\", type=int, default=8,\n                        help=\"Batch size for surprisal feature extraction (uses more VRAM)\")\n    args = parser.parse_args()\n\n    data_dir = Path(args.data_dir)\n    results_dir = Path(args.results_dir)\n    data_dir.mkdir(parents=True, exist_ok=True)\n    results_dir.mkdir(parents=True, exist_ok=True)\n\n    log.info(f\"Model: {args.model_path}\")\n    log.info(f\"Data dir: {data_dir}\")\n    log.info(f\"Samples: {args.num_samples}, Max depth: {args.max_depth}\")\n\n    # Load model + tokenizer\n    from transformers import AutoModelForCausalLM, AutoTokenizer\n\n    log.info(\"Loading tokenizer ...\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n\n    log.info(\"Loading model ...\")\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch.float16,\n        device_map=\"auto\",\n        trust_remote_code=True,\n    )\n    model.eval()\n    log.info(f\"Model loaded on {model.device}\")\n\n    # Step 2\n    log.info(\"=\" * 40 + \" Step 2: Seed Data \" + \"=\" * 40)\n    prepare_seed_data(tokenizer, data_dir, args.num_samples)\n\n    # Step 3\n    log.info(\"=\" * 40 + \" Step 3: Depth Chain \" + \"=\" * 40)\n    generate_depth_chain(model, tokenizer, data_dir, args.max_depth, args.batch_size)\n\n    # Step 4\n    log.info(\"=\" * 40 + \" Step 4: Feature Extraction \" + \"=\" * 40)\n    extract_all_features(model, tokenizer, data_dir, args.max_depth, args.feat_batch_size)\n\n    # Step 5\n    log.info(\"=\" * 40 + \" Step 5: Analysis \" + \"=\" * 40)\n    run_analysis(data_dir, results_dir, args.max_depth)\n\n    log.info(\"Pipeline complete.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 627,
      "startLine": 1,
      "totalLines": 627
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed. Let me synthesize and write the full study plan. Key observations:

From the MVP pipeline code:
- Current batch_size=16, can be optimized to 64-128
- GPU optimization report shows ~38% time savings possible
- Right-padding issue confirmed
- Generation uses prompt-chain with rewrite prompt
- 15 features: 9 surprisal + 3 vocab diversity + 3 tail-thinning
- Pipeline does: seed prep → depth chain → feature extraction → analysis
- Model: Qwen2.5-1.5B-Instruct, fp16, ~3GB VRAM


- Generation at batch size 16 takes about 6.2 seconds per batch, scaling to roughly 32 minutes per depth level and 162 minutes total across 5 depths, but with batch size optimization to 64 this drops to around 105 minutes for generation plus 14 minutes for feature extraction, giving approximately 2 hours per configuration for the 1.5B model.

The MVP estimate was 8-12 GPU hours unoptimized, but with the batch size 64 optimization I'm looking at roughly 2 hours total per 1.5B config when accounting for generation, feature extraction, and analysis. For the other smaller models like Pythia-1.4B and OLMo-1B, I'd expect similar or slightly faster times around 1.5-2 hours, but the 7B model is a different story—it's roughly 4-5 times larger which means I'd need to drop the batch size back to 16, pushing the estimate up to 8-10 hours per config due to the increased memory requirements and slower inference.

Now I'm working through the memory constraints for the 7B model more carefully—with batch size 16, the model weights plus KV cache and activations should fit within 24GB, but the generation phase alone would take around 8.75 hours since the forward pass is significantly slower with more parameters and layers.

The real bottleneck here is memory bandwidth rather than raw compute—the 4090D can sustain roughly 500 GB/s, so reading the 14GB model weights takes about 28ms per forward pass compared to 6ms for the 1.5B model, making the 7B roughly 4.7x slower overall. For the full generation task of 5K documents at 5 depths each, I'm estimating the 7B would need around 490 minutes total.

But batch size matters significantly—the 1.5B can handle bs=64 while the 7B is limited to bs=8 due to VRAM constraints, which affects throughput differently. Accounting for these practical limitations and the overhead of feature extraction and analysis, I'm settling on rough estimates: the 1.5B models take about 2-2.5 hours per configuration, while the 7B would need roughly 10-12 hours.

Now I'm mapping out the P0 experiments across different sampling strategies and model sizes, starting with the 1.5B baseline configurations at various temperature and nucleus probability settings, plus a greedy variant and the Pythia-1.4B model.

Adding OLMo-1B and scaling up to Qwen2.5-7B brings the total generation time to around 27 hours, then feature extraction, classifier training, and downstream evaluation add another 36 hours for a P0 total of 63 hours.

For P1, I'm considering retraining chains with LoRA at different depths and exploring additional model and strategy combinations, though the contamination analysis is still pending.

Looking at the full timeline, I have about 250 realistic hours available across 13 days, which comfortably covers the 133-hour total across all priority levels, but the real bottleneck is the sequential dependencies—each depth chain must complete before feature extraction, which must finish before the classifier trains, which must finish before downstream evaluation.

The schedule maps out to roughly 2 days for MVP and P0 generation, another day for the 7B model, then feature extraction and classification in parallel, followed by downstream eval taking about 1.25 days, P1 experiments around 2 days, and P2 wrapping up in the final day, with writing happening throughout. This is tight but workable if nothing breaks.

Now I'm moving into the actual writeup and need to nail down the downstream evaluation specifics. I'll compare four filtering approaches—no filtering, binary DivEye filtering, depth-aware weighted filtering, and surplexity-based filtering—by creating contaminated training sets that mix human and synthetic text at various depths and proportions, then continuing pretraining on Pythia-1.4B with 5K human docs plus varying synthetic amounts, and evaluating the results on MMLU and HellaSwag using lm-eval-harness. The continued pretraining should take around 2-3 hours per configuration.

Looking at the computational requirements, I'm calculating 12 total configurations across 4 strategies and 3 contamination levels (10%, 30%, 50% synthetic), which comes to roughly 30 hours of pretraining plus another 12 hours for evaluation—so about 42 hours total for the downstream work. That's more than my initial estimate, so I need to reconsider the MVP scope to keep this feasible.

For a phased approach, I could start with just the 30% contamination level across all 4 strategies—that's 4 runs taking about 12 hours of pretraining plus 4 hours of evaluation, totaling around 16 hours. Then I can expand to the other contamination levels as a second phase if needed.

I'm also questioning whether continued pretraining is the right methodology here, since with only 5K documents, a few epochs might not produce meaningful differences. An alternative would be to use the depth classifier to filter a larger existing corpus and show that the filtered version produces better downstream performance. But that requires having access to a sufficiently large corpus to begin with.

Let me go back and check what the IDEA_BRIEF actually specifies about the evaluation approach—it mentions comparing filtering strategies on downstream NLP benchmarks like MMLU subsets.

So the actual pipeline is: start with a human corpus, inject synthetic text at various contamination levels, apply the filtering strategies, continue pretraining on the filtered data, then evaluate on downstream tasks. The reviewer feedback also calls for testing multiple contamination severity levels at 10%, 30%, and 50%.

For the pretraining itself, I'm looking at Pythia-1.4B on a 4090D with about 5K documents over 2-3 epochs. Using LoRA would be much faster—around 30 minutes per run—versus 2-3 hours for full fine-tuning. Since I'm mainly measuring the relative effect of data quality, LoRA should be sufficient and would let me run all 12 configurations in about 6 hours total.

Now I'm finalizing the approach and writing it up. I'll prioritize MMLU and HellaSwag as the main evaluation metrics given the compute constraints, with XSum summarization as a secondary evaluation. For the LoRA configuration, I'm settling on rank 16 with alpha 32, targeting the query-key-value modules that Pythia uses, training for 3 epochs at a learning rate of 2e-4 with batch size 8.

The timeline looks much more feasible than initially thought—each depth takes roughly 1-1.5 hours when accounting for both retraining and generation, bringing the full 5-depth chain to around 5-7.5 hours total. LoRA's lightweight nature makes this practical. I'm also confirming the model specs: Qwen2.5-1.5B-Instruct fits comfortably on a 4090D at around 3GB in fp16, allowing for reasonable batch sizes. Compiling the model specifications...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "bbc7a776-f6b2-4b62-ac86-02817fb501eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7tcMaW6YQWRxwjae8LRz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11210,
      "cache_read_input_tokens": 42888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11210
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 25_

I have all the information. Now I'll write the full study plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "ad26090b-d6f5-46d4-9100-a73ec0f22eb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7tcMaW6YQWRxwjae8LRz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11210,
      "cache_read_input_tokens": 42888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11210
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Write · `toolu_01ANDKDv5WNgaTvKZS2PMVYo`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md",
  "content": "# Full Study 实验矩阵预案\n\n> 基于 MVP (Qwen2.5-1.5B-Instruct, C4 5K, depth 0→5, nucleus p=0.95 T=1.0) 的经验推算\n> 目标: EMNLP ARR 2026-05-25 提交（剩余 13 天）\n> 硬件: 1×RTX 4090D 24GB @ autodl-4090d\n\n---\n\n## 1. 实验矩阵\n\n### 维度 1：模型族\n\n| 模型 | 参数量 | 类型 | HuggingFace 路径 | ModelScope 路径 | VRAM (bf16) | 4090D 可行性 | 推荐 batch_size | 目的 |\n|------|--------|------|-------------------|-----------------|-------------|-------------|----------------|------|\n| Qwen2.5-1.5B-Instruct | 1.5B | Instruct | `Qwen/Qwen2.5-1.5B-Instruct` | `Qwen/Qwen2.5-1.5B-Instruct` | ~3GB | ✅ 余量 21GB | gen=64, feat=24 | MVP baseline，Instruct 代表真实污染源 |\n| Pythia-1.4B | 1.4B | Base | `EleutherAI/pythia-1.4b` | N/A（用 HF_ENDPOINT mirror） | ~2.8GB | ✅ 余量 21GB | gen=64, feat=24 | Base vs Instruct 对比；Drayson et al. 用同系列 |\n| OLMo-1B | 1B | Base | `allenai/OLMo-1B-0724-hf` | N/A（用 HF_ENDPOINT mirror） | ~2GB | ✅ 余量 22GB | gen=64, feat=32 | 不同训练方法/数据的 base model family |\n| Qwen2.5-7B-Instruct | 7B | Instruct | `Qwen/Qwen2.5-7B-Instruct` | `Qwen/Qwen2.5-7B-Instruct` | ~14GB | ✅ 余量 10GB | gen=8, feat=4 | Cross-scale: K* 是否随模型规模变化 |\n\n**注**: Pythia/OLMo 在 ModelScope 无官方仓库，AutoDL 下载需设 `HF_ENDPOINT=https://hf-mirror.com`。Qwen 系列优先走 ModelScope CDN。\n\n### 维度 2：解码策略消融\n\n| ID | 策略 | 参数 | 目的 | 与 MVP 关系 |\n|----|------|------|------|-------------|\n| D-greedy | Greedy | T→0 (do_sample=False) | 确定性下界：最大 mode collapse，预测 K* 最小 | 新增 |\n| D-p90 | Nucleus p=0.9 | top_p=0.9, T=1.0 | p 值敏感性 | 新增 |\n| D-p95 | Nucleus p=0.95 | top_p=0.95, T=1.0 | MVP 默认 | 已有 |\n| D-lowT | Low temperature | top_p=0.95, T=0.7 | 温度降低 → 多样性下降速度加快? | 新增 |\n| D-highT | High temperature | top_p=0.95, T=1.2 | 温度升高 → 延缓饱和? 支撑 MI 衰减假设检验 | 新增 |\n\n**核心假设检验**: greedy → 近指数 MI 衰减（快速饱和），high-T → 较慢多项式衰减（随机性延缓同质化）。用 AIC/BIC 对比拟合优度。\n\n### 维度 3：生成方式\n\n| 方式 | 配置 | 预估耗时 | 目的 |\n|------|------|----------|------|\n| Prompt-chain | 直接喂上一代输出给 LLM，用 rewrite prompt | ~2-2.5h/config (1.5B) | Upper bound，MVP 已验证 |\n| Retrain-chain | 在上一代输出上 LoRA 微调后再生成 | ~6-8h/config (1.4B) | Ecological validity：模拟真实递归训练污染路径 |\n\n### 维度 4：下游评估\n\n| 评估任务 | 工具 | 说明 | 优先级 |\n|----------|------|------|--------|\n| MMLU (5-shot) | lm-eval-harness | 知识密集型，对数据质量敏感 (FineWeb-Edu 验证) | P0 |\n| HellaSwag (10-shot) | lm-eval-harness | 常识推理，DataComp-LM 标准 benchmark | P0 |\n| XSum 摘要 | ROUGE-L | 生成质量评估 | P1 |\n\n**评估方法**: 构造不同深度污染比例的训练集 → LoRA continued pretraining Pythia-1.4B → lm-eval-harness 评估\n\n**过滤策略对比**:\n| 策略 | 说明 |\n|------|------|\n| No filter | 全部混入（baseline） |\n| Binary filter | DivEye 特征二分类移除所有检测为合成的文本 |\n| Depth-graduated | weight = quality(k)/quality(0)，按深度衰减曲线经验推导权重 |\n| Surplexity filter | 按 surprisal 高低过滤 |\n\n**污染比例**: 10% / 30% / 50% 合成文本注入\n\n---\n\n## 2. 实验优先级排序\n\n### P0：核心论文支撑（必须完成）\n\n| # | 实验 | 配置 | 预估 GPU 时间 | 依赖 | 论文贡献 |\n|---|------|------|-------------|------|----------|\n| P0-1 | MVP depth chain | Qwen2.5-1.5B, D-p95, 5K docs, depth 0-5 | ~2.5h | 无 | Pilot K* 判定 (已运行中) |\n| P0-2 | 跨模型 depth chain: Pythia | Pythia-1.4B, D-p95, 5K docs, depth 0-5 | ~2.5h | 无 | Cross-model generalization |\n| P0-3 | 跨模型 depth chain: OLMo | OLMo-1B, D-p95, 5K docs, depth 0-5 | ~2h | 无 | Cross-model generalization |\n| P0-4 | 解码消融: Greedy | Qwen2.5-1.5B, D-greedy, 5K docs, depth 0-5 | ~1.5h | 无 | MI 衰减假设检验 (lower bound) |\n| P0-5 | 解码消融: p=0.9 | Qwen2.5-1.5B, D-p90, 5K docs, depth 0-5 | ~2.5h | 无 | p 值敏感性 |\n| P0-6 | 解码消融: Low T | Qwen2.5-1.5B, D-lowT, 5K docs, depth 0-5 | ~2.5h | 无 | 温度敏感性 |\n| P0-7 | 解码消融: High T | Qwen2.5-1.5B, D-highT, 5K docs, depth 0-5 | ~2.5h | 无 | MI 衰减假设检验 (upper bound) |\n| P0-8 | Cross-scale probe | Qwen2.5-7B, D-p95, 5K docs, depth 0-5 | ~10h | 无 | Scale transfer: 1B → 7B |\n| P0-9 | 全配置特征提取 | P0-1~8 的所有 depth 数据 | ~3h | P0-1~8 | 特征矩阵构建 |\n| P0-10 | Ordinal classifier | CORAL + LightGBM + MLP + baselines | ~3h | P0-9 | C1: depth estimation |\n| P0-11 | K* + 饱和边界分析 | per-feature saturation curves, cross-model comparison | ~2h | P0-9 | C2: saturation boundary K* |\n| P0-12 | 下游过滤评估 (30%) | 4 策略 × 30% 污染, Pythia-1.4B LoRA, MMLU+HellaSwag | ~16h | P0-10 | C3: graduated filtering > binary |\n\n**P0 总计: ~50h GPU**\n\n### P1：重要消融（强烈期望完成）\n\n| # | 实验 | 配置 | 预估 GPU 时间 | 依赖 | 论文贡献 |\n|---|------|------|-------------|------|----------|\n| P1-1 | Retrain-chain | Pythia-1.4B, D-p95, LoRA × 5 depths | ~8h | 无 | Ecological validity |\n| P1-2 | 下游过滤评估 (10%+50%) | 4 策略 × 2 污染比例, MMLU+HellaSwag | ~24h | P0-10 | 污染剂量效应 |\n| P1-3 | Ordinal vs Multinomial vs Regression | 3 种分类范式对比 | ~2h | P0-9 | Ordinal structure 必要性证明 |\n| P1-4 | LLM zero/few-shot depth estimation | Qwen2.5-7B 直接判断 depth | ~4h | P0-8 | \"为什么不直接用 LLM\" baseline |\n| P1-5 | Binary detector confidence as depth proxy | DetectGPT/Binoculars score vs true depth | ~3h | P0-9 | \"为什么不用 detection confidence\" baseline |\n| P1-6 | Prompt-chain vs Retrain-chain 特征对比 | 对比两种方式的特征分布差异 + cross-setting transfer | ~2h | P1-1 | Feature 鲁棒性 |\n| P1-7 | XSum 下游评估 | 4 策略 × 30%, ROUGE-L | ~8h | P0-10 | 生成质量评估 |\n\n**P1 总计: ~51h GPU**\n\n### P2：锦上添花（有时间就做，否则进 appendix/future work）\n\n| # | 实验 | 配置 | 预估 GPU 时间 | 论文贡献 |\n|---|------|------|-------------|----------|\n| P2-1 | Pythia × 其他 decoding 策略 | Pythia-1.4B × D-greedy/D-highT | ~4h | 跨模型 × 跨策略交叉 |\n| P2-2 | OLMo × 其他 decoding 策略 | OLMo-1B × D-greedy/D-highT | ~3.5h | 同上 |\n| P2-3 | Common Crawl 自然验证 | CC 样本 depth prediction + AlignScore proxy | ~5h | Naturalistic validation |\n| P2-4 | Learned representation baseline | Frozen LM embeddings + MLP vs handcrafted | ~3h | Baseline completeness |\n| P2-5 | Heterogeneous model chain | 交替 Pythia→Qwen→OLMo 生成 | ~4h | 鲁棒性 (appendix) |\n| P2-6 | Human editing robustness | Simulated span replacement/paraphrasing | ~3h | 鲁棒性 (appendix) |\n\n**P2 总计: ~22.5h GPU**\n\n---\n\n## 3. 资源规划\n\n### GPU 时间汇总\n\n| 优先级 | GPU 时间 | 累计 |\n|--------|---------|------|\n| P0 | ~50h | 50h |\n| P1 | ~51h | 101h |\n| P2 | ~22.5h | 123.5h |\n| Buffer (调试/重跑 20%) | ~25h | 148.5h |\n\n### 可用资源\n\n- 1×RTX 4090D, 13 天 = **312h 理论上限**\n- 实际可用（考虑文件传输、调试、服务器维护）: **~260h**\n- **P0+P1 可完成，P2 部分可完成**\n\n### 1×4090D 是否够用？\n\n**结论: 勉强够，但没有余量应对意外。**\n\n| 情况 | 能否完成 |\n|------|---------|\n| 只做 P0 | ✅ 充裕（50h / 260h = 19%） |\n| P0 + P1 | ✅ 可行（101h / 260h = 39%） |\n| P0 + P1 + P2 全部 | ✅ 可行（123.5h / 260h = 48%） |\n| P0 + P1 + P2 + buffer | ⚠️ 紧张但可行（148.5h / 260h = 57%） |\n\n**瓶颈不是 GPU 总时间，而是 wall-clock 串行依赖：**\n\n### 关键路径分析\n\n```\nDay 1-2:  MVP 完成 (P0-1, 已运行中)\nDay 2-3:  P0-2,3 (Pythia + OLMo chains, 各~2.5h, 串行 = 5h)\nDay 3-4:  P0-4,5,6,7 (Qwen 1.5B × 4 decoding strategies, 串行 = 9h)\nDay 4-5:  P0-8 (7B chain, ~10h)\nDay 5-6:  P0-9,10,11 (特征提取 + 分类器 + K* 分析, ~8h)\nDay 6-8:  P0-12 (下游过滤评估, ~16h)\n--- P0 完成线: Day 8 ---\nDay 8-9:  P1-1 (retrain-chain, ~8h)\nDay 9-11: P1-2 (更多下游评估, ~24h)\nDay 11-12: P1-3,4,5,6 (各种 baselines, ~11h)\nDay 12-13: P1-7 或 P2 精选\n--- Deadline: Day 13 (May 25) ---\n```\n\n**写作并行**: 全程同步进行，不占 GPU。Day 1-3 写 Intro+Related Work，Day 4-6 写 Method，Day 7-10 写 Results，Day 11-13 整合。\n\n### 如果需要加速\n\n| 方案 | 效果 | 建议 |\n|------|------|------|\n| +1×4090D | P0 和 P1 可完全并行，总 wall-clock 减半 | 强烈建议：可同时跑 7B + 1.5B 实验 |\n| +1×A100 40GB | 7B 实验更快(bs 更大)，且可并行 | 最优方案 |\n| 减少 P1 scope | 砍 P1-2 (只做 30%不做 10%/50%) + 砍 P1-7 | 节省 ~32h，但论文说服力降 |\n\n**建议向 Director 申请**: 1 块额外 4090D（或同级 GPU），专门跑 P0-8 (7B chain, 10h) 和 P1-2 (下游评估, 24h)，主卡跑其余实验。两卡并行可在 Day 9 完成所有 P0+P1。\n\n### 并行策略（单卡）\n\n所有 depth chain 内部必须串行（depth k 依赖 depth k-1），但不同 config 之间完全独立，可按任意顺序串行执行。建议按优先级排队：\n\n```\nQueue: P0-1 → P0-2 → P0-3 → P0-4 → P0-5 → P0-6 → P0-7 → P0-8 → P0-9 → P0-10 → ...\n```\n\n如果有 2 卡：\n```\nGPU-0: P0-1 → P0-2 → P0-3 → P0-4~7 → P0-9 → P0-10 → P0-12\nGPU-1: P0-8 (7B) → P1-1 (retrain) → P1-2 (下游评估)\n```\n\n---\n\n## 4. Retrain-chain 配置细节\n\n### 目标\n模拟真实递归训练污染：不是用 prompt 让模型改写，而是在每一代输出上微调模型后再生成下一代。\n\n### LoRA 配置\n\n| 参数 | 值 | 说明 |\n|------|-----|------|\n| 模型 | Pythia-1.4B | 选 base model 更合理（retrain 场景通常是 base model） |\n| LoRA rank | 16 | 1.4B 模型不需要高 rank |\n| LoRA alpha | 32 | 2× rank，标准实践 |\n| Target modules | `query_key_value` | Pythia 用 fused QKV；如用 Qwen 则为 `q_proj, k_proj, v_proj, o_proj` |\n| Dropout | 0.05 | 防过拟合（小数据集） |\n| 训练数据 | 上一代 depth 输出 (5K docs) | depth 0 = C4 human seed |\n| Max seq length | 512 | 与 prompt-chain 一致 |\n| Epochs | 3 | 5K docs × 3 epochs，不至于过拟合 |\n| Learning rate | 2e-4 | LoRA 标准 lr |\n| LR scheduler | cosine | 标准 |\n| Batch size | 8 | gradient accumulation = 4 → effective batch = 32 |\n| Optimizer | AdamW (8-bit) | 用 bitsandbytes 8-bit Adam 省显存 |\n| bf16 | True | 4090D 支持 |\n\n### 每轮流程\n\n```\ndepth k-1 output (5K docs)\n    ↓\nLoRA fine-tune Pythia-1.4B on depth k-1 output (3 epochs)\n    ↓\nMerge LoRA weights → new model checkpoint\n    ↓\nGenerate depth k output from depth k-1 prompts using new model\n    ↓\n重复直到 depth 5\n```\n\n### 时间估算\n\n| 步骤 | 每轮耗时 | 说明 |\n|------|---------|------|\n| LoRA fine-tune | ~40 min | 5K docs × 3 epochs × 512 tokens, bs=8, 4090D |\n| LoRA merge | ~2 min | 合并权重到 base model |\n| Generation (5K docs, 5 depths worth) | ~25 min | bs=64, 256 new tokens |\n| 小计 | ~67 min/轮 | |\n\n| 项目 | 时间 |\n|------|------|\n| 5 轮 retrain-chain | ~5.6h |\n| 特征提取 (6 depths) | ~0.5h |\n| 分析 | ~0.5h |\n| **总计** | **~6.5h** |\n\n### 与 Prompt-chain 对比分析\n- 比较两种方式下的 15 维特征分布差异 (MMD distance)\n- 用 prompt-chain 训练的 classifier 在 retrain-chain 数据上的 transfer accuracy\n- 报告 K* 是否一致\n\n---\n\n## 5. 已知约束和注意事项\n\n### 必须修复项\n\n| 问题 | 影响 | 修复方案 | 何时修复 |\n|------|------|----------|----------|\n| **right-padding** | batch generation 质量受影响，padding tokens 干扰 attention | `tokenizer.padding_side = \"left\"` | Full study 第一行代码 |\n| **batch_size 未优化** | GPU 利用率仅 45%，VRAM 空闲 20GB | gen: bs=64, feat: bs=24（1.5B 模型）| Full study pipeline |\n| **empty_cache 开销** | 每 batch 调用不必要 | 移除或改为每 N batch 调用 | Full study pipeline |\n\n### AutoDL 环境约束\n\n| 约束 | 应对方案 |\n|------|----------|\n| C4 加载触发全量 shard 解析 → ProxyError | 用单 shard URL + `HF_ENDPOINT=https://hf-mirror.com` (MVP 已验证) |\n| 环境变量不跨 session 生效 | 所有 env vars 写入 `run_*.sh` 启动脚本 |\n| `source /etc/network_turbo` | 每个脚本开头都加 |\n| SSL 证书问题 | 设置 `REQUESTS_CA_BUNDLE` 和 `SSL_CERT_FILE` |\n| HF 大模型下载极慢 | Qwen 走 ModelScope；Pythia/OLMo 走 `HF_ENDPOINT` mirror |\n| 根分区 30GB 限制 | 所有模型/数据/cache → `/root/autodl-tmp/` |\n| `HF_HUB_DISABLE_XET=1` | xet_get 在 AutoDL 返回 401 |\n| SSH 端口重启后可能变 | 连接失败时提醒检查端口 |\n\n### MVP 经验迁移\n\n| 经验 | Full Study 应用 |\n|------|----------------|\n| 5K docs 的 pipeline 约 5-7h (未优化) | 优化后 ~2.5h/config，可靠基准 |\n| 15 维特征已实现且 pipeline 可跑 | 直接复用 `run_pipeline.py` 的特征提取代码 |\n| LightGBM 5-fold CV 分析框架可用 | 复用，新增 CORAL/CORN ordinal regression |\n| Rewrite prompt 格式已验证 | Full study 沿用，retrain-chain 不需要 prompt |\n\n### 代码改造清单（MVP → Full Study）\n\n| 改造项 | 工作量 | 优先级 |\n|--------|--------|--------|\n| 参数化 model_path / decoding 策略 | 小 (argparse 已有框架) | P0 |\n| left-padding 修复 | 1 行 | P0 |\n| batch_size 默认值调大 | 1 行 | P0 |\n| 支持 greedy decoding (do_sample=False) | 5 行 | P0 |\n| 支持 temperature/top_p 参数化 | 5 行 | P0 |\n| 新增 CORAL/CORN ordinal regression | ~100 行新代码 | P0 |\n| 新增 retrain-chain (LoRA pipeline) | ~200 行新代码 | P1 |\n| 新增下游 continued pretraining + eval | ~150 行新代码 | P0 |\n| 新增 flash-attn 支持 | 3 行 | P0 |\n| 结果自动汇总 + 可视化 | ~100 行 | P0 |\n\n### 风险预案\n\n| 风险 | 概率 | 影响 | 预案 |\n|------|------|------|------|\n| K* ≤ 2 (大多数配置) | 中 | 论文 depth estimation 价值降低 | 转 saturation characterization 路线: 哪些特征先饱和、不同模型/策略的 K* 差异本身是贡献 |\n| 7B 模型 OOM | 低 | 失去 cross-scale 数据 | 降 bs=4 或用 4-bit 量化 (bitsandbytes) |\n| Retrain-chain 与 prompt-chain 特征差异过大 | 中 | Cross-setting transfer 不 work | 论文明确定位 prompt-chain 为 upper bound，retrain-chain 作为 ecological validity probe |\n| 下游过滤效果不显著 | 中 | C3 (graduated > binary) 难以成立 | (1) 增大污染比例到 50%; (2) 用更敏感的 metric (held-out PPL); (3) 退路：depth signal 仍可作为数据审计工具 |\n| 13 天跑不完 P0+P1 | 低 | 论文实验不够充分 | 砍 P1-2 (只保留 30% 污染) + 砍 P1-7 (XSum)，节省 ~32h |\n\n---\n\n## 附录：完整实验矩阵（供参考）\n\nFull matrix = 4 models × 5 decoding × 2 generation methods = 40 种 corpus 配置。加上下游评估和 baselines，总实验数 > 60。\n\n**实际执行的子集（P0+P1）：** 8 corpus configs + 1 retrain-chain + 12 downstream runs + 5 classifier variants = 26 个实验，约 101 GPU 小时。\n\n| Config ID | 模型 | 解码策略 | 生成方式 | 优先级 | GPU 时间 |\n|-----------|------|----------|----------|--------|---------|\n| C01 | Qwen2.5-1.5B-Instruct | D-p95 | Prompt | P0 | 2.5h (MVP) |\n| C02 | Pythia-1.4B | D-p95 | Prompt | P0 | 2.5h |\n| C03 | OLMo-1B | D-p95 | Prompt | P0 | 2h |\n| C04 | Qwen2.5-1.5B-Instruct | D-greedy | Prompt | P0 | 1.5h |\n| C05 | Qwen2.5-1.5B-Instruct | D-p90 | Prompt | P0 | 2.5h |\n| C06 | Qwen2.5-1.5B-Instruct | D-lowT | Prompt | P0 | 2.5h |\n| C07 | Qwen2.5-1.5B-Instruct | D-highT | Prompt | P0 | 2.5h |\n| C08 | Qwen2.5-7B-Instruct | D-p95 | Prompt | P0 | 10h |\n| C09 | Pythia-1.4B | D-p95 | Retrain | P1 | 6.5h |\n| C10 | Pythia-1.4B | D-greedy | Prompt | P2 | 2h |\n| C11 | Pythia-1.4B | D-highT | Prompt | P2 | 2.5h |\n| C12 | OLMo-1B | D-greedy | Prompt | P2 | 1.5h |\n| C13 | OLMo-1B | D-highT | Prompt | P2 | 2h |\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "718cb8f7-2de1-4741-ad28-9c99c1310adf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7tcMaW6YQWRxwjae8LRz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11210,
      "cache_read_input_tokens": 42888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11210
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T12:54:02.238Z_

<details><summary>↩ Tool result · `toolu_01ANDKDv5WNgaTvKZS2PMVYo`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "d006f616-aa02-4dec-9fb1-37809e9c6e9a",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md",
    "content": "# Full Study 实验矩阵预案\n\n> 基于 MVP (Qwen2.5-1.5B-Instruct, C4 5K, depth 0→5, nucleus p=0.95 T=1.0) 的经验推算\n> 目标: EMNLP ARR 2026-05-25 提交（剩余 13 天）\n> 硬件: 1×RTX 4090D 24GB @ autodl-4090d\n\n---\n\n## 1. 实验矩阵\n\n### 维度 1：模型族\n\n| 模型 | 参数量 | 类型 | HuggingFace 路径 | ModelScope 路径 | VRAM (bf16) | 4090D 可行性 | 推荐 batch_size | 目的 |\n|------|--------|------|-------------------|-----------------|-------------|-------------|----------------|------|\n| Qwen2.5-1.5B-Instruct | 1.5B | Instruct | `Qwen/Qwen2.5-1.5B-Instruct` | `Qwen/Qwen2.5-1.5B-Instruct` | ~3GB | ✅ 余量 21GB | gen=64, feat=24 | MVP baseline，Instruct 代表真实污染源 |\n| Pythia-1.4B | 1.4B | Base | `EleutherAI/pythia-1.4b` | N/A（用 HF_ENDPOINT mirror） | ~2.8GB | ✅ 余量 21GB | gen=64, feat=24 | Base vs Instruct 对比；Drayson et al. 用同系列 |\n| OLMo-1B | 1B | Base | `allenai/OLMo-1B-0724-hf` | N/A（用 HF_ENDPOINT mirror） | ~2GB | ✅ 余量 22GB | gen=64, feat=32 | 不同训练方法/数据的 base model family |\n| Qwen2.5-7B-Instruct | 7B | Instruct | `Qwen/Qwen2.5-7B-Instruct` | `Qwen/Qwen2.5-7B-Instruct` | ~14GB | ✅ 余量 10GB | gen=8, feat=4 | Cross-scale: K* 是否随模型规模变化 |\n\n**注**: Pythia/OLMo 在 ModelScope 无官方仓库，AutoDL 下载需设 `HF_ENDPOINT=https://hf-mirror.com`。Qwen 系列优先走 ModelScope CDN。\n\n### 维度 2：解码策略消融\n\n| ID | 策略 | 参数 | 目的 | 与 MVP 关系 |\n|----|------|------|------|-------------|\n| D-greedy | Greedy | T→0 (do_sample=False) | 确定性下界：最大 mode collapse，预测 K* 最小 | 新增 |\n| D-p90 | Nucleus p=0.9 | top_p=0.9, T=1.0 | p 值敏感性 | 新增 |\n| D-p95 | Nucleus p=0.95 | top_p=0.95, T=1.0 | MVP 默认 | 已有 |\n| D-lowT | Low temperature | top_p=0.95, T=0.7 | 温度降低 → 多样性下降速度加快? | 新增 |\n| D-highT | High temperature | top_p=0.95, T=1.2 | 温度升高 → 延缓饱和? 支撑 MI 衰减假设检验 | 新增 |\n\n**核心假设检验**: greedy → 近指数 MI 衰减（快速饱和），high-T → 较慢多项式衰减（随机性延缓同质化）。用 AIC/BIC 对比拟合优度。\n\n### 维度 3：生成方式\n\n| 方式 | 配置 | 预估耗时 | 目的 |\n|------|------|----------|------|\n| Prompt-chain | 直接喂上一代输出给 LLM，用 rewrite prompt | ~2-2.5h/config (1.5B) | Upper bound，MVP 已验证 |\n| Retrain-chain | 在上一代输出上 LoRA 微调后再生成 | ~6-8h/config (1.4B) | Ecological validity：模拟真实递归训练污染路径 |\n\n### 维度 4：下游评估\n\n| 评估任务 | 工具 | 说明 | 优先级 |\n|----------|------|------|--------|\n| MMLU (5-shot) | lm-eval-harness | 知识密集型，对数据质量敏感 (FineWeb-Edu 验证) | P0 |\n| HellaSwag (10-shot) | lm-eval-harness | 常识推理，DataComp-LM 标准 benchmark | P0 |\n| XSum 摘要 | ROUGE-L | 生成质量评估 | P1 |\n\n**评估方法**: 构造不同深度污染比例的训练集 → LoRA continued pretraining Pythia-1.4B → lm-eval-harness 评估\n\n**过滤策略对比**:\n| 策略 | 说明 |\n|------|------|\n| No filter | 全部混入（baseline） |\n| Binary filter | DivEye 特征二分类移除所有检测为合成的文本 |\n| Depth-graduated | weight = quality(k)/quality(0)，按深度衰减曲线经验推导权重 |\n| Surplexity filter | 按 surprisal 高低过滤 |\n\n**污染比例**: 10% / 30% / 50% 合成文本注入\n\n---\n\n## 2. 实验优先级排序\n\n### P0：核心论文支撑（必须完成）\n\n| # | 实验 | 配置 | 预估 GPU 时间 | 依赖 | 论文贡献 |\n|---|------|------|-------------|------|----------|\n| P0-1 | MVP depth chain | Qwen2.5-1.5B, D-p95, 5K docs, depth 0-5 | ~2.5h | 无 | Pilot K* 判定 (已运行中) |\n| P0-2 | 跨模型 depth chain: Pythia | Pythia-1.4B, D-p95, 5K docs, depth 0-5 | ~2.5h | 无 | Cross-model generalization |\n| P0-3 | 跨模型 depth chain: OLMo | OLMo-1B, D-p95, 5K docs, depth 0-5 | ~2h | 无 | Cross-model generalization |\n| P0-4 | 解码消融: Greedy | Qwen2.5-1.5B, D-greedy, 5K docs, depth 0-5 | ~1.5h | 无 | MI 衰减假设检验 (lower bound) |\n| P0-5 | 解码消融: p=0.9 | Qwen2.5-1.5B, D-p90, 5K docs, depth 0-5 | ~2.5h | 无 | p 值敏感性 |\n| P0-6 | 解码消融: Low T | Qwen2.5-1.5B, D-lowT, 5K docs, depth 0-5 | ~2.5h | 无 | 温度敏感性 |\n| P0-7 | 解码消融: High T | Qwen2.5-1.5B, D-highT, 5K docs, depth 0-5 | ~2.5h | 无 | MI 衰减假设检验 (upper bound) |\n| P0-8 | Cross-scale probe | Qwen2.5-7B, D-p95, 5K docs, depth 0-5 | ~10h | 无 | Scale transfer: 1B → 7B |\n| P0-9 | 全配置特征提取 | P0-1~8 的所有 depth 数据 | ~3h | P0-1~8 | 特征矩阵构建 |\n| P0-10 | Ordinal classifier | CORAL + LightGBM + MLP + baselines | ~3h | P0-9 | C1: depth estimation |\n| P0-11 | K* + 饱和边界分析 | per-feature saturation curves, cross-model comparison | ~2h | P0-9 | C2: saturation boundary K* |\n| P0-12 | 下游过滤评估 (30%) | 4 策略 × 30% 污染, Pythia-1.4B LoRA, MMLU+HellaSwag | ~16h | P0-10 | C3: graduated filtering > binary |\n\n**P0 总计: ~50h GPU**\n\n### P1：重要消融（强烈期望完成）\n\n| # | 实验 | 配置 | 预估 GPU 时间 | 依赖 | 论文贡献 |\n|---|------|------|-------------|------|----------|\n| P1-1 | Retrain-chain | Pythia-1.4B, D-p95, LoRA × 5 depths | ~8h | 无 | Ecological validity |\n| P1-2 | 下游过滤评估 (10%+50%) | 4 策略 × 2 污染比例, MMLU+HellaSwag | ~24h | P0-10 | 污染剂量效应 |\n| P1-3 | Ordinal vs Multinomial vs Regression | 3 种分类范式对比 | ~2h | P0-9 | Ordinal structure 必要性证明 |\n| P1-4 | LLM zero/few-shot depth estimation | Qwen2.5-7B 直接判断 depth | ~4h | P0-8 | \"为什么不直接用 LLM\" baseline |\n| P1-5 | Binary detector confidence as depth proxy | DetectGPT/Binoculars score vs true depth | ~3h | P0-9 | \"为什么不用 detection confidence\" baseline |\n| P1-6 | Prompt-chain vs Retrain-chain 特征对比 | 对比两种方式的特征分布差异 + cross-setting transfer | ~2h | P1-1 | Feature 鲁棒性 |\n| P1-7 | XSum 下游评估 | 4 策略 × 30%, ROUGE-L | ~8h | P0-10 | 生成质量评估 |\n\n**P1 总计: ~51h GPU**\n\n### P2：锦上添花（有时间就做，否则进 appendix/future work）\n\n| # | 实验 | 配置 | 预估 GPU 时间 | 论文贡献 |\n|---|------|------|-------------|----------|\n| P2-1 | Pythia × 其他 decoding 策略 | Pythia-1.4B × D-greedy/D-highT | ~4h | 跨模型 × 跨策略交叉 |\n| P2-2 | OLMo × 其他 decoding 策略 | OLMo-1B × D-greedy/D-highT | ~3.5h | 同上 |\n| P2-3 | Common Crawl 自然验证 | CC 样本 depth prediction + AlignScore proxy | ~5h | Naturalistic validation |\n| P2-4 | Learned representation baseline | Frozen LM embeddings + MLP vs handcrafted | ~3h | Baseline completeness |\n| P2-5 | Heterogeneous model chain | 交替 Pythia→Qwen→OLMo 生成 | ~4h | 鲁棒性 (appendix) |\n| P2-6 | Human editing robustness | Simulated span replacement/paraphrasing | ~3h | 鲁棒性 (appendix) |\n\n**P2 总计: ~22.5h GPU**\n\n---\n\n## 3. 资源规划\n\n### GPU 时间汇总\n\n| 优先级 | GPU 时间 | 累计 |\n|--------|---------|------|\n| P0 | ~50h | 50h |\n| P1 | ~51h | 101h |\n| P2 | ~22.5h | 123.5h |\n| Buffer (调试/重跑 20%) | ~25h | 148.5h |\n\n### 可用资源\n\n- 1×RTX 4090D, 13 天 = **312h 理论上限**\n- 实际可用（考虑文件传输、调试、服务器维护）: **~260h**\n- **P0+P1 可完成，P2 部分可完成**\n\n### 1×4090D 是否够用？\n\n**结论: 勉强够，但没有余量应对意外。**\n\n| 情况 | 能否完成 |\n|------|---------|\n| 只做 P0 | ✅ 充裕（50h / 260h = 19%） |\n| P0 + P1 | ✅ 可行（101h / 260h = 39%） |\n| P0 + P1 + P2 全部 | ✅ 可行（123.5h / 260h = 48%） |\n| P0 + P1 + P2 + buffer | ⚠️ 紧张但可行（148.5h / 260h = 57%） |\n\n**瓶颈不是 GPU 总时间，而是 wall-clock 串行依赖：**\n\n### 关键路径分析\n\n```\nDay 1-2:  MVP 完成 (P0-1, 已运行中)\nDay 2-3:  P0-2,3 (Pythia + OLMo chains, 各~2.5h, 串行 = 5h)\nDay 3-4:  P0-4,5,6,7 (Qwen 1.5B × 4 decoding strategies, 串行 = 9h)\nDay 4-5:  P0-8 (7B chain, ~10h)\nDay 5-6:  P0-9,10,11 (特征提取 + 分类器 + K* 分析, ~8h)\nDay 6-8:  P0-12 (下游过滤评估, ~16h)\n--- P0 完成线: Day 8 ---\nDay 8-9:  P1-1 (retrain-chain, ~8h)\nDay 9-11: P1-2 (更多下游评估, ~24h)\nDay 11-12: P1-3,4,5,6 (各种 baselines, ~11h)\nDay 12-13: P1-7 或 P2 精选\n--- Deadline: Day 13 (May 25) ---\n```\n\n**写作并行**: 全程同步进行，不占 GPU。Day 1-3 写 Intro+Related Work，Day 4-6 写 Method，Day 7-10 写 Results，Day 11-13 整合。\n\n### 如果需要加速\n\n| 方案 | 效果 | 建议 |\n|------|------|------|\n| +1×4090D | P0 和 P1 可完全并行，总 wall-clock 减半 | 强烈建议：可同时跑 7B + 1.5B 实验 |\n| +1×A100 40GB | 7B 实验更快(bs 更大)，且可并行 | 最优方案 |\n| 减少 P1 scope | 砍 P1-2 (只做 30%不做 10%/50%) + 砍 P1-7 | 节省 ~32h，但论文说服力降 |\n\n**建议向 Director 申请**: 1 块额外 4090D（或同级 GPU），专门跑 P0-8 (7B chain, 10h) 和 P1-2 (下游评估, 24h)，主卡跑其余实验。两卡并行可在 Day 9 完成所有 P0+P1。\n\n### 并行策略（单卡）\n\n所有 depth chain 内部必须串行（depth k 依赖 depth k-1），但不同 config 之间完全独立，可按任意顺序串行执行。建议按优先级排队：\n\n```\nQueue: P0-1 → P0-2 → P0-3 → P0-4 → P0-5 → P0-6 → P0-7 → P0-8 → P0-9 → P0-10 → ...\n```\n\n如果有 2 卡：\n```\nGPU-0: P0-1 → P0-2 → P0-3 → P0-4~7 → P0-9 → P0-10 → P0-12\nGPU-1: P0-8 (7B) → P1-1 (retrain) → P1-2 (下游评估)\n```\n\n---\n\n## 4. Retrain-chain 配置细节\n\n### 目标\n模拟真实递归训练污染：不是用 prompt 让模型改写，而是在每一代输出上微调模型后再生成下一代。\n\n### LoRA 配置\n\n| 参数 | 值 | 说明 |\n|------|-----|------|\n| 模型 | Pythia-1.4B | 选 base model 更合理（retrain 场景通常是 base model） |\n| LoRA rank | 16 | 1.4B 模型不需要高 rank |\n| LoRA alpha | 32 | 2× rank，标准实践 |\n| Target modules | `query_key_value` | Pythia 用 fused QKV；如用 Qwen 则为 `q_proj, k_proj, v_proj, o_proj` |\n| Dropout | 0.05 | 防过拟合（小数据集） |\n| 训练数据 | 上一代 depth 输出 (5K docs) | depth 0 = C4 human seed |\n| Max seq length | 512 | 与 prompt-chain 一致 |\n| Epochs | 3 | 5K docs × 3 epochs，不至于过拟合 |\n| Learning rate | 2e-4 | LoRA 标准 lr |\n| LR scheduler | cosine | 标准 |\n| Batch size | 8 | gradient accumulation = 4 → effective batch = 32 |\n| Optimizer | AdamW (8-bit) | 用 bitsandbytes 8-bit Adam 省显存 |\n| bf16 | True | 4090D 支持 |\n\n### 每轮流程\n\n```\ndepth k-1 output (5K docs)\n    ↓\nLoRA fine-tune Pythia-1.4B on depth k-1 output (3 epochs)\n    ↓\nMerge LoRA weights → new model checkpoint\n    ↓\nGenerate depth k output from depth k-1 prompts using new model\n    ↓\n重复直到 depth 5\n```\n\n### 时间估算\n\n| 步骤 | 每轮耗时 | 说明 |\n|------|---------|------|\n| LoRA fine-tune | ~40 min | 5K docs × 3 epochs × 512 tokens, bs=8, 4090D |\n| LoRA merge | ~2 min | 合并权重到 base model |\n| Generation (5K docs, 5 depths worth) | ~25 min | bs=64, 256 new tokens |\n| 小计 | ~67 min/轮 | |\n\n| 项目 | 时间 |\n|------|------|\n| 5 轮 retrain-chain | ~5.6h |\n| 特征提取 (6 depths) | ~0.5h |\n| 分析 | ~0.5h |\n| **总计** | **~6.5h** |\n\n### 与 Prompt-chain 对比分析\n- 比较两种方式下的 15 维特征分布差异 (MMD distance)\n- 用 prompt-chain 训练的 classifier 在 retrain-chain 数据上的 transfer accuracy\n- 报告 K* 是否一致\n\n---\n\n## 5. 已知约束和注意事项\n\n### 必须修复项\n\n| 问题 | 影响 | 修复方案 | 何时修复 |\n|------|------|----------|----------|\n| **right-padding** | batch generation 质量受影响，padding tokens 干扰 attention | `tokenizer.padding_side = \"left\"` | Full study 第一行代码 |\n| **batch_size 未优化** | GPU 利用率仅 45%，VRAM 空闲 20GB | gen: bs=64, feat: bs=24（1.5B 模型）| Full study pipeline |\n| **empty_cache 开销** | 每 batch 调用不必要 | 移除或改为每 N batch 调用 | Full study pipeline |\n\n### AutoDL 环境约束\n\n| 约束 | 应对方案 |\n|------|----------|\n| C4 加载触发全量 shard 解析 → ProxyError | 用单 shard URL + `HF_ENDPOINT=https://hf-mirror.com` (MVP 已验证) |\n| 环境变量不跨 session 生效 | 所有 env vars 写入 `run_*.sh` 启动脚本 |\n| `source /etc/network_turbo` | 每个脚本开头都加 |\n| SSL 证书问题 | 设置 `REQUESTS_CA_BUNDLE` 和 `SSL_CERT_FILE` |\n| HF 大模型下载极慢 | Qwen 走 ModelScope；Pythia/OLMo 走 `HF_ENDPOINT` mirror |\n| 根分区 30GB 限制 | 所有模型/数据/cache → `/root/autodl-tmp/` |\n| `HF_HUB_DISABLE_XET=1` | xet_get 在 AutoDL 返回 401 |\n| SSH 端口重启后可能变 | 连接失败时提醒检查端口 |\n\n### MVP 经验迁移\n\n| 经验 | Full Study 应用 |\n|------|----------------|\n| 5K docs 的 pipeline 约 5-7h (未优化) | 优化后 ~2.5h/config，可靠基准 |\n| 15 维特征已实现且 pipeline 可跑 | 直接复用 `run_pipeline.py` 的特征提取代码 |\n| LightGBM 5-fold CV 分析框架可用 | 复用，新增 CORAL/CORN ordinal regression |\n| Rewrite prompt 格式已验证 | Full study 沿用，retrain-chain 不需要 prompt |\n\n### 代码改造清单（MVP → Full Study）\n\n| 改造项 | 工作量 | 优先级 |\n|--------|--------|--------|\n| 参数化 model_path / decoding 策略 | 小 (argparse 已有框架) | P0 |\n| left-padding 修复 | 1 行 | P0 |\n| batch_size 默认值调大 | 1 行 | P0 |\n| 支持 greedy decoding (do_sample=False) | 5 行 | P0 |\n| 支持 temperature/top_p 参数化 | 5 行 | P0 |\n| 新增 CORAL/CORN ordinal regression | ~100 行新代码 | P0 |\n| 新增 retrain-chain (LoRA pipeline) | ~200 行新代码 | P1 |\n| 新增下游 continued pretraining + eval | ~150 行新代码 | P0 |\n| 新增 flash-attn 支持 | 3 行 | P0 |\n| 结果自动汇总 + 可视化 | ~100 行 | P0 |\n\n### 风险预案\n\n| 风险 | 概率 | 影响 | 预案 |\n|------|------|------|------|\n| K* ≤ 2 (大多数配置) | 中 | 论文 depth estimation 价值降低 | 转 saturation characterization 路线: 哪些特征先饱和、不同模型/策略的 K* 差异本身是贡献 |\n| 7B 模型 OOM | 低 | 失去 cross-scale 数据 | 降 bs=4 或用 4-bit 量化 (bitsandbytes) |\n| Retrain-chain 与 prompt-chain 特征差异过大 | 中 | Cross-setting transfer 不 work | 论文明确定位 prompt-chain 为 upper bound，retrain-chain 作为 ecological validity probe |\n| 下游过滤效果不显著 | 中 | C3 (graduated > binary) 难以成立 | (1) 增大污染比例到 50%; (2) 用更敏感的 metric (held-out PPL); (3) 退路：depth signal 仍可作为数据审计工具 |\n| 13 天跑不完 P0+P1 | 低 | 论文实验不够充分 | 砍 P1-2 (只保留 30% 污染) + 砍 P1-7 (XSum)，节省 ~32h |\n\n---\n\n## 附录：完整实验矩阵（供参考）\n\nFull matrix = 4 models × 5 decoding × 2 generation methods = 40 种 corpus 配置。加上下游评估和 baselines，总实验数 > 60。\n\n**实际执行的子集（P0+P1）：** 8 corpus configs + 1 retrain-chain + 12 downstream runs + 5 classifier variants = 26 个实验，约 101 GPU 小时。\n\n| Config ID | 模型 | 解码策略 | 生成方式 | 优先级 | GPU 时间 |\n|-----------|------|----------|----------|--------|---------|\n| C01 | Qwen2.5-1.5B-Instruct | D-p95 | Prompt | P0 | 2.5h (MVP) |\n| C02 | Pythia-1.4B | D-p95 | Prompt | P0 | 2.5h |\n| C03 | OLMo-1B | D-p95 | Prompt | P0 | 2h |\n| C04 | Qwen2.5-1.5B-Instruct | D-greedy | Prompt | P0 | 1.5h |\n| C05 | Qwen2.5-1.5B-Instruct | D-p90 | Prompt | P0 | 2.5h |\n| C06 | Qwen2.5-1.5B-Instruct | D-lowT | Prompt | P0 | 2.5h |\n| C07 | Qwen2.5-1.5B-Instruct | D-highT | Prompt | P0 | 2.5h |\n| C08 | Qwen2.5-7B-Instruct | D-p95 | Prompt | P0 | 10h |\n| C09 | Pythia-1.4B | D-p95 | Retrain | P1 | 6.5h |\n| C10 | Pythia-1.4B | D-greedy | Prompt | P2 | 2h |\n| C11 | Pythia-1.4B | D-highT | Prompt | P2 | 2.5h |\n| C12 | OLMo-1B | D-greedy | Prompt | P2 | 1.5h |\n| C13 | OLMo-1B | D-highT | Prompt | P2 | 2h |\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 28_

Now let me register this artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "d806a6f1-aea4-4645-b422-a8e6372e6b32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tFRwoiD4h8KMZt8QDL7B7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11438,
      "cache_read_input_tokens": 54098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11438
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QeEvGFeQUfFUVLwJK24UVy`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "bc186717-8fc6-43ff-ad95-1e5e30e0c924",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tFRwoiD4h8KMZt8QDL7B7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11438,
      "cache_read_input_tokens": 54098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11438
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-12T12:54:06.901Z_

<details><summary>↩ Tool result · `toolu_01QeEvGFeQUfFUVLwJK24UVy`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "5db6600f-738d-41d3-a290-220d16a86594",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
The `save_project_file` tool only allows writing to memory.md, writing_plan.yaml, and paper_framing.md. It can't write to docs/full_study_plan.md. But I already wrote the file directly using the Write tool, so it's already saved. Let me check if there's a register_artifact tool I should use.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "84984341-e319-4f1d-bfc7-d2bb4d263aeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9MdMesijyRLRVEFevKTWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 65536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 371
      },
      "output_tokens": 32,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01D4Zd1akGD8yKE6kAsy3LWS`</summary>

```json
{
  "query": "register artifact",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "cfca783f-cd17-4c87-a7ac-9a2eaa6f2e24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9MdMesijyRLRVEFevKTWv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 371,
      "cache_read_input_tokens": 65536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 371
      },
      "output_tokens": 32,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-12T12:54:11.344Z_

<details><summary>↩ Tool result · `toolu_01D4Zd1akGD8yKE6kAsy3LWS`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "b78ef657-a33b-4675-b1ed-1f10b9815afa",
  "tool_use_result": {
    "matches": [],
    "query": "register artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
No register_artifact tool available. The file is already written. Let me verify the file was written correctly by reading a portion of it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "9dafc9c7-1200-4a4f-a41d-37f4eb3009fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LE4sfeDSTntHWT9NFaBwQa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 187,
      "cache_read_input_tokens": 65907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 187
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 35_

文件已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md`。

**核心结论**:

- **P0 (核心论文支撑)**: ~50h GPU — 8 个 corpus 配置 + 分类器 + K* 分析 + 下游过滤评估
- **P0+P1**: ~101h GPU — 加 retrain-chain、更多下游评估、额外 baselines
- **P0+P1+P2+buffer**: ~148.5h GPU — 1×4090D 13 天 (260h 可用) 完全可以覆盖
- **瓶颈是 wall-clock 串行依赖**，不是 GPU 总量：depth chain 内部必须串行，关键路径 P0 在 Day 8 完成，P0+P1 在 Day 12 完成
- **建议申请 1 块额外 4090D**：主卡跑 1B 级实验，副卡跑 7B chain (10h) + 下游评估 (24h)，两卡并行可 Day 9 完成全部 P0+P1
- **Retrain-chain** 用 Pythia-1.4B LoRA (rank=16, alpha=32, 3 epochs)，每轮 ~67 min，5 轮总计 ~6.5h
- **必须先修复**: left-padding、batch_size 调大、flash-attn

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "uuid": "20b66645-ef97-49ec-9e3b-a0f4337a99db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LE4sfeDSTntHWT9NFaBwQa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 187,
      "cache_read_input_tokens": 65907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 187
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 36_

文件已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md`。

**核心结论**:

- **P0 (核心论文支撑)**: ~50h GPU — 8 个 corpus 配置 + 分类器 + K* 分析 + 下游过滤评估
- **P0+P1**: ~101h GPU — 加 retrain-chain、更多下游评估、额外 baselines
- **P0+P1+P2+buffer**: ~148.5h GPU — 1×4090D 13 天 (260h 可用) 完全可以覆盖
- **瓶颈是 wall-clock 串行依赖**，不是 GPU 总量：depth chain 内部必须串行，关键路径 P0 在 Day 8 完成，P0+P1 在 Day 12 完成
- **建议申请 1 块额外 4090D**：主卡跑 1B 级实验，副卡跑 7B chain (10h) + 下游评估 (24h)，两卡并行可 Day 9 完成全部 P0+P1
- **Retrain-chain** 用 Pythia-1.4B LoRA (rank=16, alpha=32, 3 epochs)，每轮 ~67 min，5 轮总计 ~6.5h
- **必须先修复**: left-padding、batch_size 调大、flash-attn

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 362023,
  "duration_api_ms": 363911,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "6c6414a0-0ffb-433a-846c-54541b5181c0",
  "total_cost_usd": 0.95113775,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 54253,
    "cache_read_input_tokens": 326273,
    "output_tokens": 17871,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 54253,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 466,
        "cache_read_input_tokens": 65907,
        "cache_creation_input_tokens": 187,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 187
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1995,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00208,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 17871,
      "cacheReadInputTokens": 326273,
      "cacheCreationInputTokens": 54253,
      "webSearchRequests": 0,
      "costUSD": 0.9490577499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a8c05f7e-d9f8-4196-956d-8cc5e7499caf"
}
```

</details>

---
