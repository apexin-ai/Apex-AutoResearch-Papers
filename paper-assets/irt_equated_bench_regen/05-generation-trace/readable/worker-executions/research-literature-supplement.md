# research literature supplement

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/workers/worker_research_literature_supplement_20260520T234638.log`
- **Structured JSON:** [`b261c56c5b0d2f492eaa.json`](../../sessions/b2/b261c56c5b0d2f492eaa.json)

## Before a recorded user message

53 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "a385b8f6-6844-4e4e-9c68-e633d97f20f0",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/memory/"
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
    "resetsAt": 1779333600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6a4a169e-c8c2-46dd-a0ff-26658eea1b06",
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f"
}
```

---

### Assistant

_source line 4_

Let me start by reading the existing file and searching for the papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "0079667f-0421-4742-9e3c-d4d0f7ad1eaf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASwFiRD9LMGLaBEYEKN2PR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11498,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11498
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01BU1DP6LsAPbBbVsA7G1TR6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_survey_d011.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "da804d09-1202-43f4-a600-5ffe36e74f39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASwFiRD9LMGLaBEYEKN2PR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11498,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11498
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T23:46:50.355Z_

<details><summary>↩ Tool result · `toolu_01BU1DP6LsAPbBbVsA7G1TR6`</summary>

```text
1	# Literature Survey for Related Work (D011)
2	
3	## 1. Impact-vs-DIF Classics
4	
5	### Shealy & Stout (1993)
6	- **Title**: A Model-Based Standardization Approach that Separates True Bias/DIF from Group Ability Differences and Detects Test Bias/DTF as Well as Item Bias/DIF
7	- **Year**: 1993
8	- **Venue**: Psychometrika, 58(2), 159–194
9	- **Key method/finding**: Developed the SIBTEST procedure — a nonparametric, IRT model-based method that detects and estimates DIF without requiring item response function (IRF) estimation. Uses a multidimensional IRT model to explain how individual items combine to produce differential test functioning (DTF) at the test level. Employs a regression correction technique to control inflated Type I error while separating true bias from group ability differences.
10	- **Relevance to our paper**: SIBTEST is the foundational statistical test for detecting item-level bias across groups. Our DIF-based contamination detection adapts this logic: instead of demographic groups, we compare "pre-contamination" vs. "post-contamination" model cohorts. The multidimensional DIF framework directly informs our approach to separating genuine ability differences from item-specific anomalies.
11	
12	### Clauser & Mazor (1998)
13	- **Title**: Using Statistical Procedures to Identify Differentially Functioning Test Items
14	- **Year**: 1998
15	- **Venue**: Educational Measurement: Issues and Practice, 17(1), 31–44
16	- **Key method/finding**: Comprehensive review of DIF detection methods including Mantel-Haenszel, logistic regression, and SIBTEST. Documents the landscape of statistical techniques for detecting items that function differently across groups while controlling for overall ability.
17	- **Relevance to our paper**: Provides the methodological taxonomy we draw from when selecting DIF detection procedures for the LLM benchmark setting. Establishes that multiple complementary DIF methods exist with different sensitivity profiles — motivating our multi-method approach.
18	
19	### Zumbo (1999)
20	- **Title**: A Handbook on the Theory and Methods of Differential Item Functioning (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type (Ordinal) Item Scores
21	- **Year**: 1999
22	- **Venue**: Technical report, Directorate of Human Resources Research and Evaluation, Department of National Defense, Ottawa, Canada
23	- **Key method/finding**: Presents logistic regression as a unifying framework for DIF analysis applicable to both binary and ordinal item scores. Provides theoretical grounding for understanding DIF as a violation of measurement invariance.
24	- **Relevance to our paper**: Our logistic-regression-based DIF detection for binary (correct/incorrect) LLM responses directly follows this framework. Zumbo's formalization of uniform vs. non-uniform DIF maps onto our distinction between items that are uniformly easier for contaminated models vs. items showing interaction effects with model ability.
25	
26	### Holland & Wainer (1993)
27	- **Title**: Differential Item Functioning (edited volume)
28	- **Year**: 1993
29	- **Venue**: Lawrence Erlbaum Associates, Hillsdale, NJ
30	- **Key method/finding**: Definitive reference volume on DIF. Covers methods for detecting test items that function differently across examinee groups, including Mantel-Haenszel, IRT-based methods, and standardization approaches. Establishes the conceptual distinction between item impact (legitimate group differences) and item bias (construct-irrelevant difficulty).
31	- **Relevance to our paper**: The impact-vs-bias distinction is the conceptual backbone of our work. We argue that contamination-inflated performance is analogous to construct-irrelevant easiness — a form of DIF where the "group" variable is exposure to benchmark data rather than demographics.
32	
33	---
34	
35	## 2. IRT in NLP/LLM Evaluation
36	
37	### Lalor, Wu & Yu (2016)
38	- **Title**: Building an Evaluation Scale using Item Response Theory
39	- **Year**: 2016
40	- **Venue**: EMNLP 2016, pp. 648–657
41	- **Key method/finding**: First to propose IRT as an alternative means for gold-standard test-set generation and NLP system evaluation. Demonstrates that IRT can describe characteristics of individual items (difficulty, discriminating power) and account for these in estimating NLP system ability. Applied to Recognizing Textual Entailment.
42	- **Relevance to our paper**: Pioneering work establishing that IRT is applicable to NLP evaluation. Our work extends this foundation from simple item characterization to cross-cohort equating and DIF detection.
43	
44	### Lalor, Wu & Yu (2019)
45	- **Title**: Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds
46	- **Year**: 2019
47	- **Venue**: EMNLP-IJCNLP 2019, Hong Kong
48	- **Key method/finding**: Addresses the bottleneck of needing human response patterns to calibrate IRT models by proposing to learn IRT parameters from "artificial crowds" of DNN models. Finds medium-to-large positive correlations between parameters learned from human vs. machine response patterns for NLI and sentiment analysis.
49	- **Relevance to our paper**: Validates that IRT parameters estimated from machine (model) responses are meaningful and correlate with human-derived parameters. This justifies our use of LLM response matrices for IRT calibration.
50	
51	### Vania et al. (2021)
52	- **Title**: Comparing Test Sets with Item Response Theory
53	- **Year**: 2021
54	- **Venue**: ACL 2021
55	- **Key method/finding**: Evaluated 29 datasets using predictions from 18 pretrained Transformer models via IRT. Found that Quoref, HellaSwag, and MC-TACO best distinguish among SOTA models, while SNLI, MNLI, and CommitmentBank are saturated. Provides a principled way to compare the discriminative quality of benchmark datasets.
56	- **Relevance to our paper**: Demonstrates IRT-based benchmark comparison at the dataset level. Our work extends this to item-level analysis across temporal model cohorts, using DIF to detect which specific items have degraded discriminative quality due to contamination.
57	
58	### Rodriguez et al. (2021)
59	- **Title**: Evaluation Examples Are Not Equally Informative: How Should That Change NLP Leaderboards?
60	- **Year**: 2021
61	- **Venue**: ACL-IJCNLP 2021
62	- **Key method/finding**: Creates a Bayesian IRT leaderboard model where latent subject skill and latent item difficulty predict correct responses. Demonstrates that IRT can guide annotation priorities, identify annotation errors, detect overfitting, and identify the most informative evaluation examples. Released open-source IRT leaderboard code.
63	- **Relevance to our paper**: Directly relevant methodological predecessor. Their Bayesian IRT approach to leaderboards establishes that item-level modeling reveals evaluation quality issues invisible to aggregate scores. We build on this by using IRT-derived item parameters to detect contamination-induced parameter drift.
64	
65	### Polo et al. (2024)
66	- **Title**: tinyBenchmarks: Evaluating LLMs with Fewer Examples
67	- **Year**: 2024
68	- **Venue**: ICML 2024
69	- **Key method/finding**: Shows that evaluating on ~100 curated IRT-selected items per benchmark is sufficient to accurately reproduce full-benchmark performance. Released IRT-based evaluation tools and tiny versions of Open LLM Leaderboard, MMLU, HELM, and AlpacaEval 2.0. Uses clustering-based item selection to ensure coverage of the difficulty/discrimination space.
70	- **Relevance to our paper**: tinyBenchmarks demonstrates the practical value of IRT for efficient evaluation. Their item selection methodology (clustering IRT representations) is adopted by Growing Pains for anchor selection. Our DIF analysis provides a complementary diagnostic: not just which items are informative, but which items have become unreliable due to contamination.
71	
72	---
73	
74	## 3. Contamination Detection
75	
76	### Shi et al. (2024)
77	- **Title**: Detecting Pretraining Data from Large Language Models
78	- **Year**: 2024
79	- **Venue**: ICLR 2024
80	- **Key method/finding**: Proposes MIN-K% PROB — a membership inference method that identifies pretraining data by checking whether the k% of tokens with minimum probability under the LLM are unlikely enough. Introduces the WIKIMIA benchmark for evaluation. Achieves 7.4% improvement over prior methods. Applied to copyrighted book detection, contaminated example detection, and privacy auditing.
81	- **Relevance to our paper**: Min-K% operates at the instance level (is this text in the training data?) while our DIF approach operates at the item level across model populations (does this item behave differently for likely-contaminated models?). The approaches are complementary: Min-K% requires model access per instance; DIF requires only response matrices.
82	
83	### Zhang et al. (2024) — Min-K%++
84	- **Title**: Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models
85	- **Year**: 2024
86	- **Venue**: ICLR 2025
87	- **Key method/finding**: Extends Min-K% by measuring how sharply peaked the likelihood is around the input (analogous to curvature), using second-order statistics motivated by the connection between maximum likelihood training and the Hessian trace via score matching. More robust than zeroth-order signals.
88	- **Relevance to our paper**: Further develops the instance-level contamination detection paradigm. Our work offers an orthogonal, population-level signal that does not require per-instance likelihood computation.
89	
90	### Balloccu et al. (2024)
91	- **Title**: Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs
92	- **Year**: 2024
93	- **Venue**: EACL 2024
94	- **Key method/finding**: Systematic review of 255 papers using ChatGPT/GPT-4, documenting that over 4.7M samples from 263 datasets were exposed through the web interface. Catalogs evaluation malpractices including unfair baselines, reproducibility issues, and lack of contamination awareness.
95	- **Relevance to our paper**: Establishes the scale and severity of the contamination problem. Their documentation of widespread data leakage motivates our work: if contamination is pervasive and hard to prevent, we need methods to detect and account for it post-hoc — exactly what DIF provides.
96	
97	### Golchin & Surdeanu (2024)
98	- **Title**: Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models
99	- **Year**: 2024
100	- **Venue**: TACL 2024
101	- **Key method/finding**: Frames contamination detection as a multiple-choice quiz: given an original instance and three word-level perturbations, a contaminated model should identify the original. Achieves 92–100% accuracy across seven datasets. Detects specific contamination in AG News, WNLI, and XSum for GPT-4.
102	- **Relevance to our paper**: DCQ is a clever per-model, per-instance detection method but requires generating perturbations and querying the model. Our DIF approach is purely observational — it works from existing response matrices without additional model queries or perturbation generation.
103	
104	### Oren et al. (2024)
105	- **Title**: Proving Test Set Contamination in Black Box Language Models
106	- **Year**: 2024
107	- **Venue**: ICLR 2024
108	- **Key method/finding**: Statistical test comparing likelihood of a benchmark's canonical ordering vs. shuffled versions. Contaminated models find canonical orderings more likely due to memorized example order. Provides exact false positive guarantees without requiring access to pretraining data or model weights. Effective on models as small as 1.4B parameters with only 1000 examples.
109	- **Relevance to our paper**: Elegant black-box method with formal statistical guarantees. However, it detects dataset-level contamination (is the whole benchmark memorized?) rather than item-level contamination effects (which specific items are affected?). Our DIF approach provides item-level granularity.
110	
111	### Deng et al. (2024)
112	- **Title**: Investigating Data Contamination in Modern Benchmarks for Large Language Models
113	- **Year**: 2024
114	- **Venue**: NAACL 2024, pp. 8706–8719
115	- **Key method/finding**: Proposes two methods: a retrieval-based system to find overlaps between benchmarks and pretraining corpora (for open-source LLMs), and Testset Slot Guessing (TS-Guessing) for proprietary LLMs. Finds ChatGPT and GPT-4 achieve 52% and 57% exact match rates in guessing missing MMLU options.
116	- **Relevance to our paper**: Demonstrates contamination in the exact benchmark (MMLU) we analyze. Their TS-Guessing evidence of MMLU contamination in GPT-4 provides ground-truth validation context for our DIF-based detection.
117	
118	---
119	
120	## 4. Dynamic/Adaptive Benchmarks
121	
122	### Zhu et al. (2024a) — DyVal
123	- **Title**: DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks
124	- **Year**: 2024
125	- **Venue**: ICLR 2024
126	- **Key method/finding**: Generates evaluation tasks at test time using graph-based complexity control to mitigate memorization. Applies graph complexity metrics to parameterize reasoning problem difficulty. Dynamically constructs evaluation instances rather than relying on static test sets.
127	- **Relevance to our paper**: Represents the "regenerate the benchmark" approach to contamination. Our work takes the complementary "detect and account for contamination in existing benchmarks" approach, which preserves historical comparability.
128	
129	### Zhu et al. (2024b) — DyVal 2
130	- **Title**: Dynamic Evaluation of Large Language Models by Meta Probing Agents
131	- **Year**: 2024
132	- **Venue**: arXiv:2402.14865
133	- **Key method/finding**: Extends DyVal with Meta Probing Agents (MPA) inspired by psychometrics. Agents automatically transform original evaluation problems targeting three cognitive abilities: language understanding, problem solving, and domain knowledge. More generalizable than task-specific dynamic generation.
134	- **Relevance to our paper**: MPA's psychometric inspiration is conceptually aligned with our IRT-based approach, but they use psychometrics to generate new items while we use it to analyze existing items for contamination signals.
135	
136	### White et al. (2024) — LiveBench
137	- **Title**: LiveBench: A Challenging, Contamination-Free LLM Benchmark
138	- **Year**: 2024
139	- **Venue**: arXiv:2406.19314
140	- **Key method/finding**: Releases new questions monthly based on recent datasets, arXiv papers, news, and IMDb synopses. All questions have verifiable, objective ground-truth answers enabling automatic scoring without LLM judges. Spans 18 tasks across 6 categories (Math, Reasoning, Data Analysis, Language, Coding, Instruction Following).
141	- **Relevance to our paper**: LiveBench's monthly refresh strategy prevents contamination prospectively. Our DIF method detects contamination retrospectively in static benchmarks. The approaches address different temporal windows: LiveBench prevents future contamination; we diagnose past contamination in widely-used benchmarks whose historical results we want to preserve.
142	
143	### Wang et al. (2024) — MMLU-Pro
144	- **Title**: MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark
145	- **Year**: 2024
146	- **Venue**: NeurIPS 2024
147	- **Key method/finding**: Enhances MMLU with harder, reasoning-focused questions and increases answer choices from 4 to 10, reducing random guessing success. Over 12K questions across 14 domains. GPT-4o achieves only 72.6%, and the gap between GPT-4o and GPT-4-Turbo widens from 1% (MMLU) to 9% (MMLU-Pro), showing better discriminative power.
148	- **Relevance to our paper**: MMLU-Pro addresses contamination by making a harder benchmark, but doesn't diagnose which original MMLU items are compromised. Our DIF analysis can quantify exactly which MMLU items have degraded, providing evidence for why harder replacements are needed and which content areas are most affected.
149	
150	### Gema et al. (2024) — MMLU-Redux
151	- **Title**: Are We Done with MMLU?
152	- **Year**: 2024
153	- **Venue**: arXiv:2406.04127
154	- **Key method/finding**: Manual re-annotation of 5,700 MMLU questions reveals a 6.5% error rate. Error types include parsing mistakes, multiple correct answers, and missing context. Virology subset has 57% errors. Re-evaluation with corrected labels shows significant metric discrepancies and ranking shifts.
155	- **Relevance to our paper**: MMLU-Redux addresses data quality while our work addresses contamination — both are sources of measurement error. Items flagged by DIF analysis that are not contaminated may instead have quality issues, making these analyses complementary.
156	
157	---
158	
159	## 5. Key Technical Comparisons
160	
161	### Habba, Itzhak, Yehudai, Perlitz, Bandel, Shmueli-Scheuer, Choshen & Stanovsky (2026) — Growing Pains
162	- **Title**: Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration
163	- **Year**: 2026 (April)
164	- **Venue**: arXiv:2604.12843
165	- **Authors**: Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, Gabriel Stanovsky
166	
167	#### Method Details
168	- **IRT Model**: Multidimensional 2PL IRT (MIRT-2PL). Each item has a discrimination vector **a_i** and intercept **d_i**.
169	- **Calibration**: Fixed Parameter Calibration (FPC) — previously calibrated item parameters are held fixed; only new item parameters are estimated when new benchmarks are added.
170	- **Anchor Selection**: Clustering-based method (following Polo et al.) that distributes anchors across the difficulty/discrimination space. Uses 100 anchor items per dataset. Outperforms top-K discrimination selection.
171	- **Scale**: 400+ models, evaluated on Open LLM Leaderboard (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, WinoGrande) and MMLU's 57 subjects.
172	- **Performance**: Predicts full-evaluation performance within 2–3 percentage points; Spearman ρ ≥ 0.9 for ranking preservation.
173	
174	#### Technical Comparison with Our Approach
175	
176	| Dimension | Growing Pains | Our DIF Approach |
177	|-----------|---------------|------------------|
178	| **Goal** | Efficient, extensible benchmarking via FPC | Detect contamination-induced measurement distortion |
179	| **IRT model** | MIRT-2PL | 2PL (with DIF extensions) |
180	| **Core technique** | Fixed parameter calibration with anchor items | DIF analysis across temporal model cohorts |
181	| **Contamination** | Acknowledged as limitation ("anchors may become contaminated or saturated over time, requiring recalibration") but **not addressed** | Central focus — DIF detects which items are affected |
182	| **Item drift** | Not detected; assumes item parameters are stable | Explicitly models item parameter drift as DIF signal |
183	| **DIF analysis** | Not mentioned | Core methodology |
184	| **Granularity** | Dataset/benchmark level efficiency | Item-level contamination diagnostics |
185	| **Binary response** | Yes (limitation acknowledged) | Yes |
186	
187	#### Complementarity
188	Growing Pains and our work are highly complementary:
189	1. **They assume stable item parameters; we test that assumption.** Their FPC framework relies on anchor item parameters not drifting. Our DIF analysis can identify when this assumption breaks down due to contamination.
190	2. **They optimize evaluation efficiency; we diagnose evaluation validity.** Growing Pains reduces the number of items needed; we identify which items should be trusted.
191	3. **Their acknowledged limitation is our research question.** They note "anchors may become contaminated or saturated over time, requiring recalibration" but do not address it. We provide the diagnostic tool for exactly this problem.
192	4. **Integration pathway**: DIF-flagged items could be excluded from Growing Pains' anchor sets, making their FPC calibration more robust to contamination.
193	
194	### Kipnis et al. (2025) — METABENCH
195	- **Title**: MetaBench: A Sparse Benchmark for LLM Evaluation
196	- **Year**: 2025
197	- **Venue**: ICLR 2025
198	- **Key method/finding**: Distills six Open LLM Leaderboard benchmarks (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, WinoGrande) into <3% of their combined size using data from 5000+ LLMs. Uses Generalized Additive Models (GAM) to model subset-to-full-set relationships. Reconstructs benchmark scores with <0.9% MAE and leaderboard scores with <0.5% MAE. Provides two disjoint versions for repeated evaluation. Integrated into EleutherAI's lm-evaluation-harness.
199	- **Relevance to our paper**: METABENCH is our primary data source — we use their 5000+ model response matrices for IRT calibration and DIF analysis. Their item selection optimizes for predictive accuracy of aggregate scores; our DIF analysis adds a validity dimension by identifying which items remain measurement-invariant across model cohorts. Items selected by MetaBench that we flag as contaminated would suggest the sparse benchmark itself may be vulnerable to contamination effects.
200	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "63f895af-a0c7-4ffa-9c0b-250f04fe8187",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_survey_d011.md",
      "content": "# Literature Survey for Related Work (D011)\n\n## 1. Impact-vs-DIF Classics\n\n### Shealy & Stout (1993)\n- **Title**: A Model-Based Standardization Approach that Separates True Bias/DIF from Group Ability Differences and Detects Test Bias/DTF as Well as Item Bias/DIF\n- **Year**: 1993\n- **Venue**: Psychometrika, 58(2), 159–194\n- **Key method/finding**: Developed the SIBTEST procedure — a nonparametric, IRT model-based method that detects and estimates DIF without requiring item response function (IRF) estimation. Uses a multidimensional IRT model to explain how individual items combine to produce differential test functioning (DTF) at the test level. Employs a regression correction technique to control inflated Type I error while separating true bias from group ability differences.\n- **Relevance to our paper**: SIBTEST is the foundational statistical test for detecting item-level bias across groups. Our DIF-based contamination detection adapts this logic: instead of demographic groups, we compare \"pre-contamination\" vs. \"post-contamination\" model cohorts. The multidimensional DIF framework directly informs our approach to separating genuine ability differences from item-specific anomalies.\n\n### Clauser & Mazor (1998)\n- **Title**: Using Statistical Procedures to Identify Differentially Functioning Test Items\n- **Year**: 1998\n- **Venue**: Educational Measurement: Issues and Practice, 17(1), 31–44\n- **Key method/finding**: Comprehensive review of DIF detection methods including Mantel-Haenszel, logistic regression, and SIBTEST. Documents the landscape of statistical techniques for detecting items that function differently across groups while controlling for overall ability.\n- **Relevance to our paper**: Provides the methodological taxonomy we draw from when selecting DIF detection procedures for the LLM benchmark setting. Establishes that multiple complementary DIF methods exist with different sensitivity profiles — motivating our multi-method approach.\n\n### Zumbo (1999)\n- **Title**: A Handbook on the Theory and Methods of Differential Item Functioning (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type (Ordinal) Item Scores\n- **Year**: 1999\n- **Venue**: Technical report, Directorate of Human Resources Research and Evaluation, Department of National Defense, Ottawa, Canada\n- **Key method/finding**: Presents logistic regression as a unifying framework for DIF analysis applicable to both binary and ordinal item scores. Provides theoretical grounding for understanding DIF as a violation of measurement invariance.\n- **Relevance to our paper**: Our logistic-regression-based DIF detection for binary (correct/incorrect) LLM responses directly follows this framework. Zumbo's formalization of uniform vs. non-uniform DIF maps onto our distinction between items that are uniformly easier for contaminated models vs. items showing interaction effects with model ability.\n\n### Holland & Wainer (1993)\n- **Title**: Differential Item Functioning (edited volume)\n- **Year**: 1993\n- **Venue**: Lawrence Erlbaum Associates, Hillsdale, NJ\n- **Key method/finding**: Definitive reference volume on DIF. Covers methods for detecting test items that function differently across examinee groups, including Mantel-Haenszel, IRT-based methods, and standardization approaches. Establishes the conceptual distinction between item impact (legitimate group differences) and item bias (construct-irrelevant difficulty).\n- **Relevance to our paper**: The impact-vs-bias distinction is the conceptual backbone of our work. We argue that contamination-inflated performance is analogous to construct-irrelevant easiness — a form of DIF where the \"group\" variable is exposure to benchmark data rather than demographics.\n\n---\n\n## 2. IRT in NLP/LLM Evaluation\n\n### Lalor, Wu & Yu (2016)\n- **Title**: Building an Evaluation Scale using Item Response Theory\n- **Year**: 2016\n- **Venue**: EMNLP 2016, pp. 648–657\n- **Key method/finding**: First to propose IRT as an alternative means for gold-standard test-set generation and NLP system evaluation. Demonstrates that IRT can describe characteristics of individual items (difficulty, discriminating power) and account for these in estimating NLP system ability. Applied to Recognizing Textual Entailment.\n- **Relevance to our paper**: Pioneering work establishing that IRT is applicable to NLP evaluation. Our work extends this foundation from simple item characterization to cross-cohort equating and DIF detection.\n\n### Lalor, Wu & Yu (2019)\n- **Title**: Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds\n- **Year**: 2019\n- **Venue**: EMNLP-IJCNLP 2019, Hong Kong\n- **Key method/finding**: Addresses the bottleneck of needing human response patterns to calibrate IRT models by proposing to learn IRT parameters from \"artificial crowds\" of DNN models. Finds medium-to-large positive correlations between parameters learned from human vs. machine response patterns for NLI and sentiment analysis.\n- **Relevance to our paper**: Validates that IRT parameters estimated from machine (model) responses are meaningful and correlate with human-derived parameters. This justifies our use of LLM response matrices for IRT calibration.\n\n### Vania et al. (2021)\n- **Title**: Comparing Test Sets with Item Response Theory\n- **Year**: 2021\n- **Venue**: ACL 2021\n- **Key method/finding**: Evaluated 29 datasets using predictions from 18 pretrained Transformer models via IRT. Found that Quoref, HellaSwag, and MC-TACO best distinguish among SOTA models, while SNLI, MNLI, and CommitmentBank are saturated. Provides a principled way to compare the discriminative quality of benchmark datasets.\n- **Relevance to our paper**: Demonstrates IRT-based benchmark comparison at the dataset level. Our work extends this to item-level analysis across temporal model cohorts, using DIF to detect which specific items have degraded discriminative quality due to contamination.\n\n### Rodriguez et al. (2021)\n- **Title**: Evaluation Examples Are Not Equally Informative: How Should That Change NLP Leaderboards?\n- **Year**: 2021\n- **Venue**: ACL-IJCNLP 2021\n- **Key method/finding**: Creates a Bayesian IRT leaderboard model where latent subject skill and latent item difficulty predict correct responses. Demonstrates that IRT can guide annotation priorities, identify annotation errors, detect overfitting, and identify the most informative evaluation examples. Released open-source IRT leaderboard code.\n- **Relevance to our paper**: Directly relevant methodological predecessor. Their Bayesian IRT approach to leaderboards establishes that item-level modeling reveals evaluation quality issues invisible to aggregate scores. We build on this by using IRT-derived item parameters to detect contamination-induced parameter drift.\n\n### Polo et al. (2024)\n- **Title**: tinyBenchmarks: Evaluating LLMs with Fewer Examples\n- **Year**: 2024\n- **Venue**: ICML 2024\n- **Key method/finding**: Shows that evaluating on ~100 curated IRT-selected items per benchmark is sufficient to accurately reproduce full-benchmark performance. Released IRT-based evaluation tools and tiny versions of Open LLM Leaderboard, MMLU, HELM, and AlpacaEval 2.0. Uses clustering-based item selection to ensure coverage of the difficulty/discrimination space.\n- **Relevance to our paper**: tinyBenchmarks demonstrates the practical value of IRT for efficient evaluation. Their item selection methodology (clustering IRT representations) is adopted by Growing Pains for anchor selection. Our DIF analysis provides a complementary diagnostic: not just which items are informative, but which items have become unreliable due to contamination.\n\n---\n\n## 3. Contamination Detection\n\n### Shi et al. (2024)\n- **Title**: Detecting Pretraining Data from Large Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Proposes MIN-K% PROB — a membership inference method that identifies pretraining data by checking whether the k% of tokens with minimum probability under the LLM are unlikely enough. Introduces the WIKIMIA benchmark for evaluation. Achieves 7.4% improvement over prior methods. Applied to copyrighted book detection, contaminated example detection, and privacy auditing.\n- **Relevance to our paper**: Min-K% operates at the instance level (is this text in the training data?) while our DIF approach operates at the item level across model populations (does this item behave differently for likely-contaminated models?). The approaches are complementary: Min-K% requires model access per instance; DIF requires only response matrices.\n\n### Zhang et al. (2024) — Min-K%++\n- **Title**: Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2025\n- **Key method/finding**: Extends Min-K% by measuring how sharply peaked the likelihood is around the input (analogous to curvature), using second-order statistics motivated by the connection between maximum likelihood training and the Hessian trace via score matching. More robust than zeroth-order signals.\n- **Relevance to our paper**: Further develops the instance-level contamination detection paradigm. Our work offers an orthogonal, population-level signal that does not require per-instance likelihood computation.\n\n### Balloccu et al. (2024)\n- **Title**: Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs\n- **Year**: 2024\n- **Venue**: EACL 2024\n- **Key method/finding**: Systematic review of 255 papers using ChatGPT/GPT-4, documenting that over 4.7M samples from 263 datasets were exposed through the web interface. Catalogs evaluation malpractices including unfair baselines, reproducibility issues, and lack of contamination awareness.\n- **Relevance to our paper**: Establishes the scale and severity of the contamination problem. Their documentation of widespread data leakage motivates our work: if contamination is pervasive and hard to prevent, we need methods to detect and account for it post-hoc — exactly what DIF provides.\n\n### Golchin & Surdeanu (2024)\n- **Title**: Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models\n- **Year**: 2024\n- **Venue**: TACL 2024\n- **Key method/finding**: Frames contamination detection as a multiple-choice quiz: given an original instance and three word-level perturbations, a contaminated model should identify the original. Achieves 92–100% accuracy across seven datasets. Detects specific contamination in AG News, WNLI, and XSum for GPT-4.\n- **Relevance to our paper**: DCQ is a clever per-model, per-instance detection method but requires generating perturbations and querying the model. Our DIF approach is purely observational — it works from existing response matrices without additional model queries or perturbation generation.\n\n### Oren et al. (2024)\n- **Title**: Proving Test Set Contamination in Black Box Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Statistical test comparing likelihood of a benchmark's canonical ordering vs. shuffled versions. Contaminated models find canonical orderings more likely due to memorized example order. Provides exact false positive guarantees without requiring access to pretraining data or model weights. Effective on models as small as 1.4B parameters with only 1000 examples.\n- **Relevance to our paper**: Elegant black-box method with formal statistical guarantees. However, it detects dataset-level contamination (is the whole benchmark memorized?) rather than item-level contamination effects (which specific items are affected?). Our DIF approach provides item-level granularity.\n\n### Deng et al. (2024)\n- **Title**: Investigating Data Contamination in Modern Benchmarks for Large Language Models\n- **Year**: 2024\n- **Venue**: NAACL 2024, pp. 8706–8719\n- **Key method/finding**: Proposes two methods: a retrieval-based system to find overlaps between benchmarks and pretraining corpora (for open-source LLMs), and Testset Slot Guessing (TS-Guessing) for proprietary LLMs. Finds ChatGPT and GPT-4 achieve 52% and 57% exact match rates in guessing missing MMLU options.\n- **Relevance to our paper**: Demonstrates contamination in the exact benchmark (MMLU) we analyze. Their TS-Guessing evidence of MMLU contamination in GPT-4 provides ground-truth validation context for our DIF-based detection.\n\n---\n\n## 4. Dynamic/Adaptive Benchmarks\n\n### Zhu et al. (2024a) — DyVal\n- **Title**: DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Generates evaluation tasks at test time using graph-based complexity control to mitigate memorization. Applies graph complexity metrics to parameterize reasoning problem difficulty. Dynamically constructs evaluation instances rather than relying on static test sets.\n- **Relevance to our paper**: Represents the \"regenerate the benchmark\" approach to contamination. Our work takes the complementary \"detect and account for contamination in existing benchmarks\" approach, which preserves historical comparability.\n\n### Zhu et al. (2024b) — DyVal 2\n- **Title**: Dynamic Evaluation of Large Language Models by Meta Probing Agents\n- **Year**: 2024\n- **Venue**: arXiv:2402.14865\n- **Key method/finding**: Extends DyVal with Meta Probing Agents (MPA) inspired by psychometrics. Agents automatically transform original evaluation problems targeting three cognitive abilities: language understanding, problem solving, and domain knowledge. More generalizable than task-specific dynamic generation.\n- **Relevance to our paper**: MPA's psychometric inspiration is conceptually aligned with our IRT-based approach, but they use psychometrics to generate new items while we use it to analyze existing items for contamination signals.\n\n### White et al. (2024) — LiveBench\n- **Title**: LiveBench: A Challenging, Contamination-Free LLM Benchmark\n- **Year**: 2024\n- **Venue**: arXiv:2406.19314\n- **Key method/finding**: Releases new questions monthly based on recent datasets, arXiv papers, news, and IMDb synopses. All questions have verifiable, objective ground-truth answers enabling automatic scoring without LLM judges. Spans 18 tasks across 6 categories (Math, Reasoning, Data Analysis, Language, Coding, Instruction Following).\n- **Relevance to our paper**: LiveBench's monthly refresh strategy prevents contamination prospectively. Our DIF method detects contamination retrospectively in static benchmarks. The approaches address different temporal windows: LiveBench prevents future contamination; we diagnose past contamination in widely-used benchmarks whose historical results we want to preserve.\n\n### Wang et al. (2024) — MMLU-Pro\n- **Title**: MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark\n- **Year**: 2024\n- **Venue**: NeurIPS 2024\n- **Key method/finding**: Enhances MMLU with harder, reasoning-focused questions and increases answer choices from 4 to 10, reducing random guessing success. Over 12K questions across 14 domains. GPT-4o achieves only 72.6%, and the gap between GPT-4o and GPT-4-Turbo widens from 1% (MMLU) to 9% (MMLU-Pro), showing better discriminative power.\n- **Relevance to our paper**: MMLU-Pro addresses contamination by making a harder benchmark, but doesn't diagnose which original MMLU items are compromised. Our DIF analysis can quantify exactly which MMLU items have degraded, providing evidence for why harder replacements are needed and which content areas are most affected.\n\n### Gema et al. (2024) — MMLU-Redux\n- **Title**: Are We Done with MMLU?\n- **Year**: 2024\n- **Venue**: arXiv:2406.04127\n- **Key method/finding**: Manual re-annotation of 5,700 MMLU questions reveals a 6.5% error rate. Error types include parsing mistakes, multiple correct answers, and missing context. Virology subset has 57% errors. Re-evaluation with corrected labels shows significant metric discrepancies and ranking shifts.\n- **Relevance to our paper**: MMLU-Redux addresses data quality while our work addresses contamination — both are sources of measurement error. Items flagged by DIF analysis that are not contaminated may instead have quality issues, making these analyses complementary.\n\n---\n\n## 5. Key Technical Comparisons\n\n### Habba, Itzhak, Yehudai, Perlitz, Bandel, Shmueli-Scheuer, Choshen & Stanovsky (2026) — Growing Pains\n- **Title**: Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\n- **Year**: 2026 (April)\n- **Venue**: arXiv:2604.12843\n- **Authors**: Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, Gabriel Stanovsky\n\n#### Method Details\n- **IRT Model**: Multidimensional 2PL IRT (MIRT-2PL). Each item has a discrimination vector **a_i** and intercept **d_i**.\n- **Calibration**: Fixed Parameter Calibration (FPC) — previously calibrated item parameters are held fixed; only new item parameters are estimated when new benchmarks are added.\n- **Anchor Selection**: Clustering-based method (following Polo et al.) that distributes anchors across the difficulty/discrimination space. Uses 100 anchor items per dataset. Outperforms top-K discrimination selection.\n- **Scale**: 400+ models, evaluated on Open LLM Leaderboard (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, WinoGrande) and MMLU's 57 subjects.\n- **Performance**: Predicts full-evaluation performance within 2–3 percentage points; Spearman ρ ≥ 0.9 for ranking preservation.\n\n#### Technical Comparison with Our Approach\n\n| Dimension | Growing Pains | Our DIF Approach |\n|-----------|---------------|------------------|\n| **Goal** | Efficient, extensible benchmarking via FPC | Detect contamination-induced measurement distortion |\n| **IRT model** | MIRT-2PL | 2PL (with DIF extensions) |\n| **Core technique** | Fixed parameter calibration with anchor items | DIF analysis across temporal model cohorts |\n| **Contamination** | Acknowledged as limitation (\"anchors may become contaminated or saturated over time, requiring recalibration\") but **not addressed** | Central focus — DIF detects which items are affected |\n| **Item drift** | Not detected; assumes item parameters are stable | Explicitly models item parameter drift as DIF signal |\n| **DIF analysis** | Not mentioned | Core methodology |\n| **Granularity** | Dataset/benchmark level efficiency | Item-level contamination diagnostics |\n| **Binary response** | Yes (limitation acknowledged) | Yes |\n\n#### Complementarity\nGrowing Pains and our work are highly complementary:\n1. **They assume stable item parameters; we test that assumption.** Their FPC framework relies on anchor item parameters not drifting. Our DIF analysis can identify when this assumption breaks down due to contamination.\n2. **They optimize evaluation efficiency; we diagnose evaluation validity.** Growing Pains reduces the number of items needed; we identify which items should be trusted.\n3. **Their acknowledged limitation is our research question.** They note \"anchors may become contaminated or saturated over time, requiring recalibration\" but do not address it. We provide the diagnostic tool for exactly this problem.\n4. **Integration pathway**: DIF-flagged items could be excluded from Growing Pains' anchor sets, making their FPC calibration more robust to contamination.\n\n### Kipnis et al. (2025) — METABENCH\n- **Title**: MetaBench: A Sparse Benchmark for LLM Evaluation\n- **Year**: 2025\n- **Venue**: ICLR 2025\n- **Key method/finding**: Distills six Open LLM Leaderboard benchmarks (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, WinoGrande) into <3% of their combined size using data from 5000+ LLMs. Uses Generalized Additive Models (GAM) to model subset-to-full-set relationships. Reconstructs benchmark scores with <0.9% MAE and leaderboard scores with <0.5% MAE. Provides two disjoint versions for repeated evaluation. Integrated into EleutherAI's lm-evaluation-harness.\n- **Relevance to our paper**: METABENCH is our primary data source — we use their 5000+ model response matrices for IRT calibration and DIF analysis. Their item selection optimizes for predictive accuracy of aggregate scores; our DIF analysis adds a validity dimension by identifying which items remain measurement-invariant across model cohorts. Items selected by MetaBench that we flag as contaminated would suggest the sparse benchmark itself may be vulnerable to contamination effects.\n",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 200
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CU6tZbG1vzXvtVWyvY5snF`</summary>

```json
{
  "query": "select:WebSearch",
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
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "2af7224f-222b-40d7-ba3b-b700ad94ca4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASwFiRD9LMGLaBEYEKN2PR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11498,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11498
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T23:46:50.817Z_

<details><summary>↩ Tool result · `toolu_01CU6tZbG1vzXvtVWyvY5snF`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
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
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "758bdecc-3cc6-4f25-8ad8-1798e0845a77",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have the file content and the WebSearch tool. Let me search for all the papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "e64102d8-575a-450e-a202-21e1dd6aeb28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1Kp31LjugxkGjecKAVpb9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6474,
      "cache_read_input_tokens": 23339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6474
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 10_

Now let me search for all the papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "3ef1e084-e54b-49d2-a363-1d38be203822",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1Kp31LjugxkGjecKAVpb9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6474,
      "cache_read_input_tokens": 23339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6474
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SjYEcqPR2uWv7Jbk6ycBeJ`</summary>

```json
{
  "query": "Li contamination detector EMNLP 2024 web-overlap annotation MMLU benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "ad6e373c-ae9a-4633-8bc5-325e23a020b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1Kp31LjugxkGjecKAVpb9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6474,
      "cache_read_input_tokens": 23339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6474
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LGbpFZhTLHxFPAuNo334CH`</summary>

```json
{
  "query": "ConStat contamination detection LLM benchmark statistical test"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "ce58fb2f-765a-41ec-a36e-719868fd8d3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1Kp31LjugxkGjecKAVpb9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6474,
      "cache_read_input_tokens": 23339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6474
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R3pSFvVpTRyDBbRGvYKTqs`</summary>

```json
{
  "query": "GSM1K Scale AI contamination math benchmark accuracy drop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "a8ab123a-be77-4e9f-9e41-8bfcc4e02bfb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1Kp31LjugxkGjecKAVpb9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6474,
      "cache_read_input_tokens": 23339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6474
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ccqx7DB5xgVwX3S5gMaMSj`</summary>

```json
{
  "query": "Growing Pains LLM benchmark arXiv 2604.12843"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "6239c3fb-c263-4777-8559-e5dcc9b5b4a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1Kp31LjugxkGjecKAVpb9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6474,
      "cache_read_input_tokens": 23339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6474
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LCbrAAmEtW1WgFccFRgVPX`</summary>

```json
{
  "query": "Wang ICLR 2026 reinforcement learning hidden contamination signal benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "a5947fab-4f66-4cae-8905-a8540c955083",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A1Kp31LjugxkGjecKAVpb9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6474,
      "cache_read_input_tokens": 23339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6474
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T23:47:02.174Z_

<details><summary>↩ Tool result · `toolu_01SjYEcqPR2uWv7Jbk6ycBeJ`</summary>

```text
Web search results for query: "Li contamination detector EMNLP 2024 web-overlap annotation MMLU benchmark"

Links: [{"title":"An Open-Source Data Contamination Report for Large ...","url":"https://aclanthology.org/2024.findings-emnlp.30.pdf"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/html/2502.14425v2"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation","url":"https://arxiv.org/html/2406.13990v1"},{"title":"An Open-Source Data Contamination Report for Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.30/"},{"title":"MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark","url":"https://arxiv.org/pdf/2412.15194"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.532/"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"Rethinking Benchmark and Contamination for Language Models with","url":"https://arxiv.org/pdf/2311.04850"},{"title":"Detecting Benchmark Contamination Through Watermarking","url":"https://arxiv.org/pdf/2502.17259"}]

Based on the search results, I found relevant information about a contamination detection work presented at EMNLP 2024:

Yucheng Li, Yunhao Guo, Frank Guerin, and Chenghua Lin published "An Open-Source Data Contamination Report for Large Language Models" in Findings of the Association for Computational Linguistics: EMNLP 2024, pages 528–541.

This paper presents an extensive data contamination report for over 15 popular large language models across six popular multiple-choice QA benchmarks and introduces an open-source pipeline that enables the community to perform contamination analysis on customised data and models.

The experiments reveal varying contamination levels ranging from 1% to 45% across benchmarks, with the contamination degree increasing rapidly over time, and data contamination does not necessarily lead to increased model metrics—while significant accuracy boosts of up to 14% and 7% are observed on contaminated C-Eval and Hellaswag benchmarks, only a minimal increase is noted on contaminated MMLU.

The work addresses data contamination detection across multiple benchmarks including MMLU and provides tools for the research community to analyze contamination in their own datasets and models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "dfd707ee-cbde-4b6b-a3cc-843cd0c2fdb4",
  "tool_use_result": {
    "query": "Li contamination detector EMNLP 2024 web-overlap annotation MMLU benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_015nEbHAwTg7rNzehbvXhJP4",
        "content": [
          {
            "title": "An Open-Source Data Contamination Report for Large ...",
            "url": "https://aclanthology.org/2024.findings-emnlp.30.pdf"
          },
          {
            "title": "A Survey on Data Contamination for Large Language Models",
            "url": "https://arxiv.org/html/2502.14425v2"
          },
          {
            "title": "Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation",
            "url": "https://arxiv.org/html/2406.13990v1"
          },
          {
            "title": "An Open-Source Data Contamination Report for Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.findings-emnlp.30/"
          },
          {
            "title": "MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark",
            "url": "https://arxiv.org/pdf/2412.15194"
          },
          {
            "title": "Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation - ACL Anthology",
            "url": "https://aclanthology.org/2024.findings-emnlp.532/"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          },
          {
            "title": "Rethinking Benchmark and Contamination for Language Models with",
            "url": "https://arxiv.org/pdf/2311.04850"
          },
          {
            "title": "Detecting Benchmark Contamination Through Watermarking",
            "url": "https://arxiv.org/pdf/2502.17259"
          }
        ]
      },
      "Based on the search results, I found relevant information about a contamination detection work presented at EMNLP 2024:\n\nYucheng Li, Yunhao Guo, Frank Guerin, and Chenghua Lin published \"An Open-Source Data Contamination Report for Large Language Models\" in Findings of the Association for Computational Linguistics: EMNLP 2024, pages 528–541.\n\nThis paper presents an extensive data contamination report for over 15 popular large language models across six popular multiple-choice QA benchmarks and introduces an open-source pipeline that enables the community to perform contamination analysis on customised data and models.\n\nThe experiments reveal varying contamination levels ranging from 1% to 45% across benchmarks, with the contamination degree increasing rapidly over time, and data contamination does not necessarily lead to increased model metrics—while significant accuracy boosts of up to 14% and 7% are observed on contaminated C-Eval and Hellaswag benchmarks, only a minimal increase is noted on contaminated MMLU.\n\nThe work addresses data contamination detection across multiple benchmarks including MMLU and provides tools for the research community to analyze contamination in their own datasets and models."
    ],
    "durationSeconds": 6.637745009999999
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T23:47:03.486Z_

<details><summary>↩ Tool result · `toolu_01R3pSFvVpTRyDBbRGvYKTqs`</summary>

```text
Web search results for query: "GSM1K Scale AI contamination math benchmark accuracy drop"

Links: [{"title":"A Careful Examination of Large Language Model Performance on Grade School Arithmetic | PromptLayer","url":"https://www.promptlayer.com/research-papers/a-careful-examination-of-large-language-model-performance-on-grade-school-arithmetic"},{"title":"A Careful Examination of Large Language Model Performance on Grade School Arithmetic","url":"https://arxiv.org/html/2405.00332v1"},{"title":"A Careful Examination of Large Language Model","url":"https://arxiv.org/pdf/2405.00332"},{"title":"Is AI Cheating on the Test: Data Contamination, Gaming, and the Benchmark Crisis | by Jarosław Wasowski | Mar, 2026 | Medium","url":"https://medium.com/@wasowski.jarek/mmlu-85-simpleqa-3-how-to-actually-evaluate-ai-models-in-2026-9dff2fba494f"},{"title":"AI benchmark numbers are meaningless — here’s what to look for instead","url":"https://www.makeuseof.com/ai-benchmark-numbers-are-meaningless-heres-what-to-look-for-instead/"},{"title":"Scale Labs Leaderboard: Math Evaluation","url":"https://labs.scale.com/leaderboard/math"},{"title":"GSM8K Benchmark: Evaluating Math Reasoning","url":"https://www.emergentmind.com/topics/gsm8k-benchmark"},{"title":"Identifying Data Contamination in LLMs for Mathematical Benchmarks DIPLOMARBEIT","url":"https://repositum.tuwien.at/bitstream/20.500.12708/216244/1/Mathis%20Tobias%20Gallus%20-%202025%20-%20Identifying%20Data%20Contamination%20in%20LLMs%20for...pdf"},{"title":"LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT","url":"https://www.lxt.ai/blog/llm-benchmarks/"}]

Based on the search results, here's what the research found:

## Key Findings

Scale AI created GSM1k, a novel dataset designed to measure LLM overfitting on GSM8k. The benchmark was designed to be similar to the existing GSM8k grade-school math test but with entirely new problems.

## Accuracy Drops

When benchmarking leading open- and closed-source models, researchers found substantial evidence that many models have been contaminated by benchmark data, with models showing performance drops of up to 13% accuracy. The Phi and Mistral model families showed accuracy drops of up to 13% on the new questions.

## Evidence of Data Contamination

Models may have memorized answers from GSM8k or similar datasets rather than truly understanding the underlying math concepts. A positive relationship (Spearman's r² = 0.36) was found between a model's probability of generating examples from GSM8k and its performance gap between GSM8k and GSM1k, strongly suggesting that models have partially memorized examples from GSM8k.

## Model-Specific Results

Frontier models such as GPT-4 and Claude display minimal signs of memorization and generalize well, while the Mistral and Phi families show consistent overfitting across almost all model sizes and versions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "1227bcb6-44d7-47ee-915c-d832fba40fbf",
  "tool_use_result": {
    "query": "GSM1K Scale AI contamination math benchmark accuracy drop",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LHHUytxGinXjBWtjZUCp4w",
        "content": [
          {
            "title": "A Careful Examination of Large Language Model Performance on Grade School Arithmetic | PromptLayer",
            "url": "https://www.promptlayer.com/research-papers/a-careful-examination-of-large-language-model-performance-on-grade-school-arithmetic"
          },
          {
            "title": "A Careful Examination of Large Language Model Performance on Grade School Arithmetic",
            "url": "https://arxiv.org/html/2405.00332v1"
          },
          {
            "title": "A Careful Examination of Large Language Model",
            "url": "https://arxiv.org/pdf/2405.00332"
          },
          {
            "title": "Is AI Cheating on the Test: Data Contamination, Gaming, and the Benchmark Crisis | by Jarosław Wasowski | Mar, 2026 | Medium",
            "url": "https://medium.com/@wasowski.jarek/mmlu-85-simpleqa-3-how-to-actually-evaluate-ai-models-in-2026-9dff2fba494f"
          },
          {
            "title": "AI benchmark numbers are meaningless — here’s what to look for instead",
            "url": "https://www.makeuseof.com/ai-benchmark-numbers-are-meaningless-heres-what-to-look-for-instead/"
          },
          {
            "title": "Scale Labs Leaderboard: Math Evaluation",
            "url": "https://labs.scale.com/leaderboard/math"
          },
          {
            "title": "GSM8K Benchmark: Evaluating Math Reasoning",
            "url": "https://www.emergentmind.com/topics/gsm8k-benchmark"
          },
          {
            "title": "Identifying Data Contamination in LLMs for Mathematical Benchmarks DIPLOMARBEIT",
            "url": "https://repositum.tuwien.at/bitstream/20.500.12708/216244/1/Mathis%20Tobias%20Gallus%20-%202025%20-%20Identifying%20Data%20Contamination%20in%20LLMs%20for...pdf"
          },
          {
            "title": "LLM benchmarks in 2026: What they prove and what your business actually needs | High-Quality AI Data to Power Innovation | LXT",
            "url": "https://www.lxt.ai/blog/llm-benchmarks/"
          }
        ]
      },
      "Based on the search results, here's what the research found:\n\n## Key Findings\n\nScale AI created GSM1k, a novel dataset designed to measure LLM overfitting on GSM8k. The benchmark was designed to be similar to the existing GSM8k grade-school math test but with entirely new problems.\n\n## Accuracy Drops\n\nWhen benchmarking leading open- and closed-source models, researchers found substantial evidence that many models have been contaminated by benchmark data, with models showing performance drops of up to 13% accuracy. The Phi and Mistral model families showed accuracy drops of up to 13% on the new questions.\n\n## Evidence of Data Contamination\n\nModels may have memorized answers from GSM8k or similar datasets rather than truly understanding the underlying math concepts. A positive relationship (Spearman's r² = 0.36) was found between a model's probability of generating examples from GSM8k and its performance gap between GSM8k and GSM1k, strongly suggesting that models have partially memorized examples from GSM8k.\n\n## Model-Specific Results\n\nFrontier models such as GPT-4 and Claude display minimal signs of memorization and generalize well, while the Mistral and Phi families show consistent overfitting across almost all model sizes and versions."
    ],
    "durationSeconds": 6.667049678
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T23:47:04.182Z_

<details><summary>↩ Tool result · `toolu_01Ccqx7DB5xgVwX3S5gMaMSj`</summary>

```text
Web search results for query: "Growing Pains LLM benchmark arXiv 2604.12843"

Links: [{"title":"[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/abs/2604.12843"},{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics","url":"https://arxiv.org/pdf/2602.24173"},{"title":"Line Goes Up? Inherent Limitations of Benchmarks for Evaluating Large   Language Models","url":"https://arxiv.org/pdf/2502.14318"},{"title":"Are Large-Language Models Graph Algorithmic Reasoners?","url":"https://arxiv.org/pdf/2410.22597"},{"title":"Benchmarking Large Language Models for Bio-Image Analysis Code Generation","url":"https://www.biorxiv.org/content/10.1101/2024.04.19.590278.full.pdf"}]

Based on the search results, I found information about the paper you're looking for:

"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration" is a recent paper (submitted April 14, 2026, with version 2 on April 15, 2026).

The paper addresses a practical problem in LLM evaluation: the rapid release of both language models and benchmarks makes it increasingly costly to evaluate every model on every dataset, and in practice, models are often evaluated on different samples, making scores difficult to compare across studies.

The proposed solution is a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed. The approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.

The research is authored by Eliya Habba, Itay Itzhak, Asaf Yehudai, and others from institutions including The Hebrew University of Jerusalem, IBM Research, MIT, Technion, and the Allen Institute for AI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "98478a8e-3ccb-48f2-9c1b-3f4b81bc5b2c",
  "tool_use_result": {
    "query": "Growing Pains LLM benchmark arXiv 2604.12843",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XsXQvxiA6pSxsrXWPK1pU7",
        "content": [
          {
            "title": "[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration",
            "url": "https://arxiv.org/abs/2604.12843"
          },
          {
            "title": "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration",
            "url": "https://arxiv.org/html/2604.12843"
          },
          {
            "title": "LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics",
            "url": "https://arxiv.org/pdf/2602.24173"
          },
          {
            "title": "Line Goes Up? Inherent Limitations of Benchmarks for Evaluating Large   Language Models",
            "url": "https://arxiv.org/pdf/2502.14318"
          },
          {
            "title": "Are Large-Language Models Graph Algorithmic Reasoners?",
            "url": "https://arxiv.org/pdf/2410.22597"
          },
          {
            "title": "Benchmarking Large Language Models for Bio-Image Analysis Code Generation",
            "url": "https://www.biorxiv.org/content/10.1101/2024.04.19.590278.full.pdf"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\n\"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\" is a recent paper (submitted April 14, 2026, with version 2 on April 15, 2026).\n\nThe paper addresses a practical problem in LLM evaluation: the rapid release of both language models and benchmarks makes it increasingly costly to evaluate every model on every dataset, and in practice, models are often evaluated on different samples, making scores difficult to compare across studies.\n\nThe proposed solution is a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed. The approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.\n\nThe research is authored by Eliya Habba, Itay Itzhak, Asaf Yehudai, and others from institutions including The Hebrew University of Jerusalem, IBM Research, MIT, Technion, and the Allen Institute for AI."
    ],
    "durationSeconds": 6.338396552
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T23:47:04.336Z_

<details><summary>↩ Tool result · `toolu_01LCbrAAmEtW1WgFccFRgVPX`</summary>

```text
Web search results for query: "Wang ICLR 2026 reinforcement learning hidden contamination signal benchmark"

Links: [{"title":"Vector researchers advance representation learning and deep learning research at ICLR 2026 - Vector Institute for Artificial Intelligence","url":"https://vectorinstitute.ai/vector-researchers-advance-representation-learning-and-deep-learning-research-at-iclr-2026/"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=W8VCH9x1HZ"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/pdf/2510.09259"},{"title":"Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination","url":"https://arxiv.org/pdf/2507.10532"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"ICLR 2026 - Microsoft Research","url":"https://www.microsoft.com/en-us/research/event/iclr-2026/sessions/"},{"title":"[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/abs/2510.09259"}]

I found several relevant papers related to reinforcement learning, data contamination detection, and benchmarks presented at ICLR 2026. Here are the key findings:

## Detecting Data Contamination from RL Post-training

Data contamination poses a significant threat to reliable LLM evaluation, occurring when benchmark samples appear in training sets and compromising reported performance, with detection methods existing for pre-training and SFT but a critical research gap in RL post-training. 

A systematic study proposes "Self-Critique," a method motivated by the observation that after RL phases, output entropy distribution of LLMs tends to collapse into highly specific and sparse modes.

## Related Work on Data Contamination in RL

The issue of data contamination in LLMs arises when benchmark samples inadvertently appear in training sets, compromising validity, with existing detection methods focused on pre-training and SFT stages while leaving a gap for RL post-training.

Studies report that even random or partially incorrect rewards can improve some models, with one hypothesis being that if evaluation benchmarks leaked into pre-training corpora, spurious rewards could cue models to retrieve memorized answers rather than acquire new reasoning skills.

The search results show active research in this area, though I couldn't locate a specific paper with all those exact terms in the title from the ICLR 2026 proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "a60f510a-b9b5-43bb-88ac-ece510413945",
  "tool_use_result": {
    "query": "Wang ICLR 2026 reinforcement learning hidden contamination signal benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DwXCqVyvwtxHaT9ER9F8fu",
        "content": [
          {
            "title": "Vector researchers advance representation learning and deep learning research at ICLR 2026 - Vector Institute for Artificial Intelligence",
            "url": "https://vectorinstitute.ai/vector-researchers-advance-representation-learning-and-deep-learning-research-at-iclr-2026/"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf?id=W8VCH9x1HZ"
          },
          {
            "title": "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/pdf/2510.09259"
          },
          {
            "title": "Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination",
            "url": "https://arxiv.org/pdf/2507.10532"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/pdf/2510.02386"
          },
          {
            "title": "ICLR 2026 - Microsoft Research",
            "url": "https://www.microsoft.com/en-us/research/event/iclr-2026/sessions/"
          },
          {
            "title": "[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/abs/2510.09259"
          }
        ]
      },
      "I found several relevant papers related to reinforcement learning, data contamination detection, and benchmarks presented at ICLR 2026. Here are the key findings:\n\n## Detecting Data Contamination from RL Post-training\n\nData contamination poses a significant threat to reliable LLM evaluation, occurring when benchmark samples appear in training sets and compromising reported performance, with detection methods existing for pre-training and SFT but a critical research gap in RL post-training. \n\nA systematic study proposes \"Self-Critique,\" a method motivated by the observation that after RL phases, output entropy distribution of LLMs tends to collapse into highly specific and sparse modes.\n\n## Related Work on Data Contamination in RL\n\nThe issue of data contamination in LLMs arises when benchmark samples inadvertently appear in training sets, compromising validity, with existing detection methods focused on pre-training and SFT stages while leaving a gap for RL post-training.\n\nStudies report that even random or partially incorrect rewards can improve some models, with one hypothesis being that if evaluation benchmarks leaked into pre-training corpora, spurious rewards could cue models to retrieve memorized answers rather than acquire new reasoning skills.\n\nThe search results show active research in this area, though I couldn't locate a specific paper with all those exact terms in the title from the ICLR 2026 proceedings."
    ],
    "durationSeconds": 6.093318831
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T23:47:07.145Z_

<details><summary>↩ Tool result · `toolu_01LGbpFZhTLHxFPAuNo334CH`</summary>

```text
Web search results for query: "ConStat contamination detection LLM benchmark statistical test"

Links: [{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://constat.ai/"},{"title":"[Quick Review] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://liner.com/review/constat-performancebased-contamination-detection-in-large-language-models"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://files.sri.inf.ethz.ch/website/papers/dekoninck2024constat.pdf"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/html/2405.16281v1"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language   Models","url":"https://arxiv.org/pdf/2405.16281"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models | SRI Lab","url":"https://www.sri.inf.ethz.ch/publications/dekoninck2024constat"},{"title":"GitHub - eth-sri/ConStat: A statistical test for contamination detection in language models. · GitHub","url":"https://github.com/eth-sri/ConStat"}]

Based on the search results, here's what ConStat is:

## Overview

ConStat is a statistical method that tests for performance-based contamination in LLMs. It was presented as a NeurIPS 2024 paper.

## How It Works

Given a reference benchmark and reference models, it computes the likelihood of the observed performance of the model under the null hypothesis that the model is not contaminated. ConStat detects performance-based contamination by comparing a model's performance on a benchmark to its performance on a reference benchmark, identifying contamination if the model performs much better on the benchmark.

## Types of Contamination Detected

Different reference benchmarks test different types of contamination: rephrased samples test syntax-specific contamination, samples from the same distribution test sample-specific contamination, and different benchmarks for the same task test benchmark-specific contamination.

## Key Findings

ConStat was applied to diverse model architectures and contamination scenarios, finding high levels of contamination in multiple popular models including Mistral, Llama, Yi, and the top-3 Open LLM Leaderboard models. ConStat's performance remains strong even in challenging scenarios, such as when models are trained on rephrased data, which are designed to evade syntax-specific detection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "c94c0c08-cda5-4e8a-84d3-a9c2061cd5ea",
  "tool_use_result": {
    "query": "ConStat contamination detection LLM benchmark statistical test",
    "results": [
      {
        "tool_use_id": "srvtoolu_015Sh4HTGWeLWq82XAs7Nu7K",
        "content": [
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://constat.ai/"
          },
          {
            "title": "[Quick Review] ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://liner.com/review/constat-performancebased-contamination-detection-in-large-language-models"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://files.sri.inf.ethz.ch/website/papers/dekoninck2024constat.pdf"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://arxiv.org/html/2405.16281v1"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language   Models",
            "url": "https://arxiv.org/pdf/2405.16281"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models | SRI Lab",
            "url": "https://www.sri.inf.ethz.ch/publications/dekoninck2024constat"
          },
          {
            "title": "GitHub - eth-sri/ConStat: A statistical test for contamination detection in language models. · GitHub",
            "url": "https://github.com/eth-sri/ConStat"
          }
        ]
      },
      "Based on the search results, here's what ConStat is:\n\n## Overview\n\nConStat is a statistical method that tests for performance-based contamination in LLMs. It was presented as a NeurIPS 2024 paper.\n\n## How It Works\n\nGiven a reference benchmark and reference models, it computes the likelihood of the observed performance of the model under the null hypothesis that the model is not contaminated. ConStat detects performance-based contamination by comparing a model's performance on a benchmark to its performance on a reference benchmark, identifying contamination if the model performs much better on the benchmark.\n\n## Types of Contamination Detected\n\nDifferent reference benchmarks test different types of contamination: rephrased samples test syntax-specific contamination, samples from the same distribution test sample-specific contamination, and different benchmarks for the same task test benchmark-specific contamination.\n\n## Key Findings\n\nConStat was applied to diverse model architectures and contamination scenarios, finding high levels of contamination in multiple popular models including Mistral, Llama, Yi, and the top-3 Open LLM Leaderboard models. ConStat's performance remains strong even in challenging scenarios, such as when models are trained on rephrased data, which are designed to evade syntax-specific detection."
    ],
    "durationSeconds": 10.653869455999999
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Let me gather more details on some of these papers. I need:

1. **Li et al. (EMNLP 2024)**: The search found "An Open-Source Data Contamination Report for Large Language Models" by Yucheng Li et al. at EMNLP 2024 Findings. But the user specifically mentioned "9,229 item-level web-overlap annotations for MMLU" and "Contamination Detector". Let me search more specifically for this.

2. **ConStat**: Got good info. Authors: de Koninck et al. NeurIPS 2024. arXiv:2405.16281.


3. **GSM1K**: Found the Scale AI paper on grade school arithmetic performance. arXiv:2405.00332.
4. **Growing Pains**: Confirmed the arXiv ID as 2604.12843.
5. **Wang et al. (ICLR 2026)**: Located a paper on detecting data contamination from reinforcement learning post-training. arXiv:2510.09259. Need to verify this matches what the user is looking for.

Let me run a few more targeted searches to pin down the exact papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "fb02acc9-4d33-4fd9-8246-33108e654d49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TkS2B9GfU3YkNE38dcKnvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2185,
      "cache_creation_input_tokens": 1717,
      "cache_read_input_tokens": 29813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1717
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 22_

Let me search for more details on the Li et al. paper and the Wang et al. ICLR 2026 paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "eab2b3de-2e2b-4caf-8e00-9ea376214609",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TkS2B9GfU3YkNE38dcKnvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2185,
      "cache_creation_input_tokens": 1717,
      "cache_read_input_tokens": 29813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1717
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019GUbef1shXJvwLrMXrC8Gg`</summary>

```json
{
  "query": "\"Yucheng Li\" \"9229\" MMLU contamination web overlap annotation benchmark items"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "49e866d7-8a6a-4284-9746-08d756d095e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TkS2B9GfU3YkNE38dcKnvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2185,
      "cache_creation_input_tokens": 1717,
      "cache_read_input_tokens": 29813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1717
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012vpAvokLw1pquY2WD5Y44n`</summary>

```json
{
  "query": "arXiv 2510.09259 \"Detecting Data Contamination\" reinforcement learning post-training ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "0dfdd6fd-d6cb-4285-91bb-1f7fac161bd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TkS2B9GfU3YkNE38dcKnvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2185,
      "cache_creation_input_tokens": 1717,
      "cache_read_input_tokens": 29813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1717
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LbLWvc1EuXjVTbAWdGn4gT`</summary>

```json
{
  "query": "ConStat dekoninck NeurIPS 2024 performance-based contamination authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "ee45bcc8-e418-4b0e-970d-9b68447c7e5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TkS2B9GfU3YkNE38dcKnvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2185,
      "cache_creation_input_tokens": 1717,
      "cache_read_input_tokens": 29813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1717
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K1JY7A9x82e1fMswmMvQi4`</summary>

```json
{
  "query": "GSM1K \"A Careful Examination\" Scale AI authors Zhang 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "180430e9-e7db-4e04-b93f-3e23f598813b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TkS2B9GfU3YkNE38dcKnvT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2185,
      "cache_creation_input_tokens": 1717,
      "cache_read_input_tokens": 29813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1717
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T23:47:27.459Z_

<details><summary>↩ Tool result · `toolu_019GUbef1shXJvwLrMXrC8Gg`</summary>

```text
Web search results for query: ""Yucheng Li" "9229" MMLU contamination web overlap annotation benchmark items"

Links: [{"title":"GitHub - liyucheng09/Contamination_Detector: Lightweight tool to identify Data Contamination in LLMs evaluation","url":"https://github.com/liyucheng09/Contamination_Detector"},{"title":"MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark | Request PDF","url":"https://www.researchgate.net/publication/394299063_MMLU-CF_A_Contamination-free_Multi-task_Language_Understanding_Benchmark"},{"title":"An Open-Source Data Contamination Report for Large ...","url":"https://aclanthology.org/2024.findings-emnlp.30.pdf"},{"title":"MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark","url":"https://arxiv.org/html/2412.15194v1"},{"title":"Rethinking Benchmark and Contamination for Language Models with","url":"https://arxiv.org/pdf/2311.04850"},{"title":"MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark","url":"https://arxiv.org/pdf/2412.15194"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"Data Contamination Assessment — OpenCompass 0.5.2 documentation","url":"https://opencompass.readthedocs.io/en/latest/advanced_guides/contamination_eval.html"}]

Based on the search results, I found information about Yucheng Li's work on data contamination in the MMLU benchmark. Here's what I discovered:

Yucheng Li published "An Open Source Data Contamination Report for Large Language Models" in 2023 on ArXiv. The work includes contamination examples and annotations for MMLU.

The search results reference a contamination detection methodology that identifies data contamination in two steps, first using the Bing Search API to check if test items appear online. The research examines model accuracy on clean sets versus input-only contaminated and input-and-label contaminated sets.

There's also a contamination annotation framework that generates models' performance on clean, input-only contaminated, and input-and-label contaminated subsets, which appears to be part of the Contamination_Detector tool available on GitHub.

However, I should note that the specific details about "9229" items and the exact annotation benchmark metrics you mentioned weren't found in these search results. If you need more specific information about those particular numbers or aspects of the annotation methodology, you may want to consult the full research paper directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "8362b552-1c71-4603-8037-6a117d270c53",
  "tool_use_result": {
    "query": "\"Yucheng Li\" \"9229\" MMLU contamination web overlap annotation benchmark items",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GnhpkFWEDWB2fXdtrjuPSi",
        "content": [
          {
            "title": "GitHub - liyucheng09/Contamination_Detector: Lightweight tool to identify Data Contamination in LLMs evaluation",
            "url": "https://github.com/liyucheng09/Contamination_Detector"
          },
          {
            "title": "MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark | Request PDF",
            "url": "https://www.researchgate.net/publication/394299063_MMLU-CF_A_Contamination-free_Multi-task_Language_Understanding_Benchmark"
          },
          {
            "title": "An Open-Source Data Contamination Report for Large ...",
            "url": "https://aclanthology.org/2024.findings-emnlp.30.pdf"
          },
          {
            "title": "MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark",
            "url": "https://arxiv.org/html/2412.15194v1"
          },
          {
            "title": "Rethinking Benchmark and Contamination for Language Models with",
            "url": "https://arxiv.org/pdf/2311.04850"
          },
          {
            "title": "MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark",
            "url": "https://arxiv.org/pdf/2412.15194"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          },
          {
            "title": "Data Contamination Assessment — OpenCompass 0.5.2 documentation",
            "url": "https://opencompass.readthedocs.io/en/latest/advanced_guides/contamination_eval.html"
          }
        ]
      },
      "Based on the search results, I found information about Yucheng Li's work on data contamination in the MMLU benchmark. Here's what I discovered:\n\nYucheng Li published \"An Open Source Data Contamination Report for Large Language Models\" in 2023 on ArXiv. The work includes contamination examples and annotations for MMLU.\n\nThe search results reference a contamination detection methodology that identifies data contamination in two steps, first using the Bing Search API to check if test items appear online. The research examines model accuracy on clean sets versus input-only contaminated and input-and-label contaminated sets.\n\nThere's also a contamination annotation framework that generates models' performance on clean, input-only contaminated, and input-and-label contaminated subsets, which appears to be part of the Contamination_Detector tool available on GitHub.\n\nHowever, I should note that the specific details about \"9229\" items and the exact annotation benchmark metrics you mentioned weren't found in these search results. If you need more specific information about those particular numbers or aspects of the annotation methodology, you may want to consult the full research paper directly."
    ],
    "durationSeconds": 5.628931933
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T23:47:28.204Z_

<details><summary>↩ Tool result · `toolu_01LbLWvc1EuXjVTbAWdGn4gT`</summary>

```text
Web search results for query: "ConStat dekoninck NeurIPS 2024 performance-based contamination authors"

Links: [{"title":"ConStat: Performance-Based Contamination Detection in LLMs - YouTube","url":"https://www.youtube.com/watch?v=dgvU0jDFa0c"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://constat.ai/"},{"title":"NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://neurips.cc/virtual/2024/poster/96266"},{"title":"ConStat: Performance-Based Contamination Detection in ...","url":"https://github.com/eth-sri/ConStat"},{"title":"[Quick Review] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://liner.com/review/constat-performancebased-contamination-detection-in-large-language-models"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://files.sri.inf.ethz.ch/website/papers/dekoninck2024constat.pdf"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/a7f89793b9e6f8c6568dbbb6ff727b9b-Paper-Conference.pdf"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"[2405.16281] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/abs/2405.16281"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language   Models","url":"https://arxiv.org/pdf/2405.16281"}]

Based on the search results, here's what I found about the ConStat paper from NeurIPS 2024:

## Authors

The ConStat paper was authored by Jasper Dekoninck, Mark Niklas Müller, and Martin Vechev.

## Paper Information

Jasper Deckoninck is a researcher at ETH Zurich and presented this paper at NeurIPS 2024.

## Performance-Based Contamination Approach

The paper proposes a new performance-based definition of contamination, which defines contamination based on its outcome rather than its cause. More specifically, they propose a novel definition of contamination as artificially inflated and non-generalizing benchmark performance instead of the inclusion of benchmark samples in the training data, enabling detection of any model with inflated performance that does not generalize to rephrased samples, synthetic samples from the same distribution, or different benchmarks for the same task.

## Key Results

The method excels at quantifying contamination, showing excellent predictiveness with a coefficient of determination (r^2) of 0.94 when comparing its estimated sample-specific contamination effect to ground truth measurements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "855a7b89-a982-4592-919c-da468c895cbb",
  "tool_use_result": {
    "query": "ConStat dekoninck NeurIPS 2024 performance-based contamination authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_012DjivJefp1KpyXdGLP6GaY",
        "content": [
          {
            "title": "ConStat: Performance-Based Contamination Detection in LLMs - YouTube",
            "url": "https://www.youtube.com/watch?v=dgvU0jDFa0c"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://constat.ai/"
          },
          {
            "title": "NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://neurips.cc/virtual/2024/poster/96266"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in ...",
            "url": "https://github.com/eth-sri/ConStat"
          },
          {
            "title": "[Quick Review] ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://liner.com/review/constat-performancebased-contamination-detection-in-large-language-models"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://files.sri.inf.ethz.ch/website/papers/dekoninck2024constat.pdf"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/a7f89793b9e6f8c6568dbbb6ff727b9b-Paper-Conference.pdf"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          },
          {
            "title": "[2405.16281] ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://arxiv.org/abs/2405.16281"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language   Models",
            "url": "https://arxiv.org/pdf/2405.16281"
          }
        ]
      },
      "Based on the search results, here's what I found about the ConStat paper from NeurIPS 2024:\n\n## Authors\n\nThe ConStat paper was authored by Jasper Dekoninck, Mark Niklas Müller, and Martin Vechev.\n\n## Paper Information\n\nJasper Deckoninck is a researcher at ETH Zurich and presented this paper at NeurIPS 2024.\n\n## Performance-Based Contamination Approach\n\nThe paper proposes a new performance-based definition of contamination, which defines contamination based on its outcome rather than its cause. More specifically, they propose a novel definition of contamination as artificially inflated and non-generalizing benchmark performance instead of the inclusion of benchmark samples in the training data, enabling detection of any model with inflated performance that does not generalize to rephrased samples, synthetic samples from the same distribution, or different benchmarks for the same task.\n\n## Key Results\n\nThe method excels at quantifying contamination, showing excellent predictiveness with a coefficient of determination (r^2) of 0.94 when comparing its estimated sample-specific contamination effect to ground truth measurements."
    ],
    "durationSeconds": 5.1151011220000004
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T23:47:29.039Z_

<details><summary>↩ Tool result · `toolu_012vpAvokLw1pquY2WD5Y44n`</summary>

```text
Web search results for query: "arXiv 2510.09259 "Detecting Data Contamination" reinforcement learning post-training ICLR 2026"

Links: [{"title":"detecting data contamination from reinforcement learning ...","url":"https://arxiv.org/pdf/2510.09259"},{"title":"[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/abs/2510.09259"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=3650&show=2000"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/html/2510.09259"},{"title":"Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination","url":"https://arxiv.org/pdf/2507.10532"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/pdf/2510.27055"}]

Based on the search results, here's what I found about arXiv paper 2510.09259:

The paper addresses data contamination, which poses a significant threat to the reliable evaluation of Large Language Models (LLMs). This issue arises when benchmark samples may inadvertently appear in training sets, compromising the validity of reported performance.

While detection methods have been developed for the pre-training and Supervised Fine-Tuning stages, a critical research gap exists for the increasingly significant phase of Reinforcement Learning (RL) post-training. The paper conducts the first systematic study of data detection within RL post-training scenario and proposes Self-Critique.

The method is motivated by a key observation: after RL phase, the output entropy distribution of LLMs tends to collapse into highly specific and sparse modes. The Self-Critique method is designed to detect data contamination in the Reinforcement Learning (RL) post-training phase, aiming to prevent misleading performance claims and promote transparent research practices.

The method is applied to public, non-sensitive benchmarks (AIME, K&K, SAT, GSM8K) that contain no personal data. The paper was submitted on October 10, 2025, with the most recent version dated March 18, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "5e00a2ef-2f94-4c36-8064-8715bb388780",
  "tool_use_result": {
    "query": "arXiv 2510.09259 \"Detecting Data Contamination\" reinforcement learning post-training ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015i6RNt2ApHndzLP1DoSvCC",
        "content": [
          {
            "title": "detecting data contamination from reinforcement learning ...",
            "url": "https://arxiv.org/pdf/2510.09259"
          },
          {
            "title": "[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/abs/2510.09259"
          },
          {
            "title": "Machine Learning Oct 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-10?skip=3650&show=2000"
          },
          {
            "title": "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/html/2510.09259"
          },
          {
            "title": "Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination",
            "url": "https://arxiv.org/pdf/2507.10532"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/pdf/2510.27055"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2510.09259:\n\nThe paper addresses data contamination, which poses a significant threat to the reliable evaluation of Large Language Models (LLMs). This issue arises when benchmark samples may inadvertently appear in training sets, compromising the validity of reported performance.\n\nWhile detection methods have been developed for the pre-training and Supervised Fine-Tuning stages, a critical research gap exists for the increasingly significant phase of Reinforcement Learning (RL) post-training. The paper conducts the first systematic study of data detection within RL post-training scenario and proposes Self-Critique.\n\nThe method is motivated by a key observation: after RL phase, the output entropy distribution of LLMs tends to collapse into highly specific and sparse modes. The Self-Critique method is designed to detect data contamination in the Reinforcement Learning (RL) post-training phase, aiming to prevent misleading performance claims and promote transparent research practices.\n\nThe method is applied to public, non-sensitive benchmarks (AIME, K&K, SAT, GSM8K) that contain no personal data. The paper was submitted on October 10, 2025, with the most recent version dated March 18, 2026."
    ],
    "durationSeconds": 6.597610071000003
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T23:47:29.123Z_

<details><summary>↩ Tool result · `toolu_01K1JY7A9x82e1fMswmMvQi4`</summary>

```text
Web search results for query: "GSM1K "A Careful Examination" Scale AI authors Zhang 2024"

Links: [{"title":"A Careful Examination of Large Language Model Performance on Grade School Arithmetic","url":"https://vladbogo.substack.com/p/a-careful-examination-of-large-language"},{"title":"[2405.00332v3] A Careful Examination of Large Language Model Performance on Grade School Arithmetic","url":"https://arxiv.org/abs/2405.00332v3"},{"title":"[2405.00332v1] A Careful Examination of Large Language Model Performance on Grade School Arithmetic","url":"https://arxiv.org/abs/2405.00332v1"},{"title":"[PDF] A Careful Examination of Large Language Model Performance on Grade School Arithmetic | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Careful-Examination-of-Large-Language-Model-on-Zhang-Da/ef62f95c16f668f031d649799cbd79081c6d2b0f"},{"title":"A Careful Examination of Large Language Model Performance on Grade School Arithmetic - Scale Labs | Scale Labs","url":"https://labs.scale.com/papers/llm-performance-grade-school-arithmetic"},{"title":"[2405.00332] A Careful Examination of Large Language Model Performance on Grade School Arithmetic","url":"https://arxiv.org/abs/2405.00332"},{"title":"A Careful Examination of Large Language Model ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/53384f2090c6a5cac952c598fd67992f-Paper-Datasets_and_Benchmarks_Track.pdf"},{"title":"A Careful Examination of Large Language Model Performance on Grade School Arithmetic | PromptLayer","url":"https://www.promptlayer.com/research-papers/a-careful-examination-of-large-language-model-performance-on-grade-school-arithmetic"}]

Based on the search results, I found comprehensive information about this paper:

## Paper Overview

"A Careful Examination of Large Language Model Performance on Grade School Arithmetic" introduces Grade School Math 1000 (GSM1k), designed to mirror the style and complexity of the established GSM8k benchmark, the gold standard for measuring elementary mathematical reasoning.

## Authors

The paper's authors are Hugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Dylan Slack, Qin Lyu, Sean Hendryx, Russell Kaplan, Michele Lunati, and Summer Yue.

## Research Focus

The study addresses growing concern that some of LLM performance actually reflects dataset contamination, where data closely resembling benchmark questions leaks into the training data, instead of true reasoning ability.

## Key Findings

When evaluating leading open- and closed-source LLMs on GSM1k, the researchers observed accuracy drops of up to 13%, with several families of models (e.g., Phi and Mistral) showing evidence of systematic overfitting across almost all model sizes.

## Publication Details

The paper was published as an arXiv preprint (arXiv:2405.00332) in 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "cf9590d0-e192-4bc6-bfc4-43c5ff73fae2",
  "tool_use_result": {
    "query": "GSM1K \"A Careful Examination\" Scale AI authors Zhang 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M1zjCn6QnSqENmD3PjmkRi",
        "content": [
          {
            "title": "A Careful Examination of Large Language Model Performance on Grade School Arithmetic",
            "url": "https://vladbogo.substack.com/p/a-careful-examination-of-large-language"
          },
          {
            "title": "[2405.00332v3] A Careful Examination of Large Language Model Performance on Grade School Arithmetic",
            "url": "https://arxiv.org/abs/2405.00332v3"
          },
          {
            "title": "[2405.00332v1] A Careful Examination of Large Language Model Performance on Grade School Arithmetic",
            "url": "https://arxiv.org/abs/2405.00332v1"
          },
          {
            "title": "[PDF] A Careful Examination of Large Language Model Performance on Grade School Arithmetic | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/A-Careful-Examination-of-Large-Language-Model-on-Zhang-Da/ef62f95c16f668f031d649799cbd79081c6d2b0f"
          },
          {
            "title": "A Careful Examination of Large Language Model Performance on Grade School Arithmetic - Scale Labs | Scale Labs",
            "url": "https://labs.scale.com/papers/llm-performance-grade-school-arithmetic"
          },
          {
            "title": "[2405.00332] A Careful Examination of Large Language Model Performance on Grade School Arithmetic",
            "url": "https://arxiv.org/abs/2405.00332"
          },
          {
            "title": "A Careful Examination of Large Language Model ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/53384f2090c6a5cac952c598fd67992f-Paper-Datasets_and_Benchmarks_Track.pdf"
          },
          {
            "title": "A Careful Examination of Large Language Model Performance on Grade School Arithmetic | PromptLayer",
            "url": "https://www.promptlayer.com/research-papers/a-careful-examination-of-large-language-model-performance-on-grade-school-arithmetic"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about this paper:\n\n## Paper Overview\n\n\"A Careful Examination of Large Language Model Performance on Grade School Arithmetic\" introduces Grade School Math 1000 (GSM1k), designed to mirror the style and complexity of the established GSM8k benchmark, the gold standard for measuring elementary mathematical reasoning.\n\n## Authors\n\nThe paper's authors are Hugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Dylan Slack, Qin Lyu, Sean Hendryx, Russell Kaplan, Michele Lunati, and Summer Yue.\n\n## Research Focus\n\nThe study addresses growing concern that some of LLM performance actually reflects dataset contamination, where data closely resembling benchmark questions leaks into the training data, instead of true reasoning ability.\n\n## Key Findings\n\nWhen evaluating leading open- and closed-source LLMs on GSM1k, the researchers observed accuracy drops of up to 13%, with several families of models (e.g., Phi and Mistral) showing evidence of systematic overfitting across almost all model sizes.\n\n## Publication Details\n\nThe paper was published as an arXiv preprint (arXiv:2405.00332) in 2024."
    ],
    "durationSeconds": 5.709724427000001
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Let me get more specific details. I need:

1. For Li et al., I found "An Open-Source Data Contamination Report for Large Language Models" by Yucheng Li et al. at EMNLP 2024 Findings. The GitHub mentions Contamination_Detector. But the user mentioned 9,229 item-level annotations. Let me check the paper directly or search more specifically.

2. For Wang et al. ICLR 2026 - the arXiv:2510.09259 paper. Need to find the authors. Let me check.

3. Growing Pains arXiv ID 2604.12843 is confirmed.


I'm searching for the remaining author details and verifying the specific annotation counts mentioned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "51f2ebca-925e-4c0b-ae38-6f5baa0551e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zcM6mYtunDiWrsrL6FAAq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5828,
      "cache_read_input_tokens": 31530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5828
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 32_

Let me get the remaining details I need.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "bc9027e6-6563-4c16-a276-53a53b6fe553",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zcM6mYtunDiWrsrL6FAAq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5828,
      "cache_read_input_tokens": 31530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5828
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BgjXjpd1iZgoTgMczyiyQh`</summary>

```json
{
  "query": "arXiv 2510.09259 \"Detecting Data Contamination\" reinforcement learning authors Wang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "f80c68f8-7713-4300-bae9-c0088fa74e43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zcM6mYtunDiWrsrL6FAAq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5828,
      "cache_read_input_tokens": 31530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5828
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019CvhqBe7P8t8RLi7QcZA3e`</summary>

```json
{
  "query": "\"Yucheng Li\" \"Contamination Detector\" EMNLP 2024 \"web overlap\" 9229 MMLU items annotations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "b5392f4a-f66c-4028-97e4-41103c4ee778",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zcM6mYtunDiWrsrL6FAAq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5828,
      "cache_read_input_tokens": 31530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5828
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T23:48:00.062Z_

<details><summary>↩ Tool result · `toolu_019CvhqBe7P8t8RLi7QcZA3e`</summary>

```text
Web search results for query: ""Yucheng Li" "Contamination Detector" EMNLP 2024 "web overlap" 9229 MMLU items annotations"

Links: [{"title":"An Open-Source Data Contamination Report for Large ...","url":"https://aclanthology.org/2024.findings-emnlp.30.pdf"},{"title":"Reusing Leaked Benchmarks for Large Language Model ...","url":"https://aclanthology.org/2024.findings-emnlp.532.pdf"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/html/2502.14425v2"},{"title":"GitHub - liyucheng09/Contamination_Detector: Lightweight tool to identify Data Contamination in LLMs evaluation","url":"https://github.com/liyucheng09/Contamination_Detector"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"An Open-Source Data Contamination Report for Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.30/"},{"title":"dblp: EMNLP (Findings) 2024","url":"https://dblp.org/db/conf/emnlp/emnlp2024f.html"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://openreview.net/pdf?id=O3rnGt7DK7"}]

I found relevant results for your search. Based on the search results, here's what I found:

Yucheng Li, Yunhao Guo, Frank Guerin, and Chenghua Lin published "An Open-Source Data Contamination Report for Large Language Models" in the Findings of the Association for Computational Linguistics: EMNLP 2024.

The research identifies data contamination in two steps, first using the Bing Search API to check if test items appear online, which relates to detecting web overlap mentioned in your query.

The experiments reveal varying contamination levels ranging from 1% to 45% across benchmarks, with the contamination degree increasing rapidly over time. Regarding MMLU specifically, data contamination does not necessarily lead to increased model metrics, with only a minimal increase noted on contaminated MMLU.

The work has an associated GitHub repository (Contamination_Detector) with the citation: "An Open Source Data Contamination Report for Large Language Models".

While the search confirmed the paper exists and discusses data contamination detection with web overlap methodology applied to MMLU and other benchmarks, I wasn't able to locate the specific details about "9229 MMLU items annotations" in the search results. You may find more specific details about the annotation count in the full paper itself, which is available at the ACL Anthology link.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "6926d64d-7785-4f0e-a7ba-2b5715bca828",
  "tool_use_result": {
    "query": "\"Yucheng Li\" \"Contamination Detector\" EMNLP 2024 \"web overlap\" 9229 MMLU items annotations",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UP38SaH5bxVgo5hAwk8Jrm",
        "content": [
          {
            "title": "An Open-Source Data Contamination Report for Large ...",
            "url": "https://aclanthology.org/2024.findings-emnlp.30.pdf"
          },
          {
            "title": "Reusing Leaked Benchmarks for Large Language Model ...",
            "url": "https://aclanthology.org/2024.findings-emnlp.532.pdf"
          },
          {
            "title": "A Survey on Data Contamination for Large Language Models",
            "url": "https://arxiv.org/html/2502.14425v2"
          },
          {
            "title": "GitHub - liyucheng09/Contamination_Detector: Lightweight tool to identify Data Contamination in LLMs evaluation",
            "url": "https://github.com/liyucheng09/Contamination_Detector"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          },
          {
            "title": "An Open-Source Data Contamination Report for Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.findings-emnlp.30/"
          },
          {
            "title": "dblp: EMNLP (Findings) 2024",
            "url": "https://dblp.org/db/conf/emnlp/emnlp2024f.html"
          },
          {
            "title": "A Survey on Data Contamination for Large Language Models",
            "url": "https://openreview.net/pdf?id=O3rnGt7DK7"
          }
        ]
      },
      "I found relevant results for your search. Based on the search results, here's what I found:\n\nYucheng Li, Yunhao Guo, Frank Guerin, and Chenghua Lin published \"An Open-Source Data Contamination Report for Large Language Models\" in the Findings of the Association for Computational Linguistics: EMNLP 2024.\n\nThe research identifies data contamination in two steps, first using the Bing Search API to check if test items appear online, which relates to detecting web overlap mentioned in your query.\n\nThe experiments reveal varying contamination levels ranging from 1% to 45% across benchmarks, with the contamination degree increasing rapidly over time. Regarding MMLU specifically, data contamination does not necessarily lead to increased model metrics, with only a minimal increase noted on contaminated MMLU.\n\nThe work has an associated GitHub repository (Contamination_Detector) with the citation: \"An Open Source Data Contamination Report for Large Language Models\".\n\nWhile the search confirmed the paper exists and discusses data contamination detection with web overlap methodology applied to MMLU and other benchmarks, I wasn't able to locate the specific details about \"9229 MMLU items annotations\" in the search results. You may find more specific details about the annotation count in the full paper itself, which is available at the ACL Anthology link."
    ],
    "durationSeconds": 7.6969777079999915
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T23:48:01.460Z_

<details><summary>↩ Tool result · `toolu_01BgjXjpd1iZgoTgMczyiyQh`</summary>

```text
Web search results for query: "arXiv 2510.09259 "Detecting Data Contamination" reinforcement learning authors Wang"

Links: [{"title":"[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/abs/2510.09259"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/396459308_Detecting_Data_Contamination_from_Reinforcement_Learning_Post-training_for_Large_Language_Models"},{"title":"Paper page - Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://huggingface.co/papers/2510.09259"},{"title":"detecting data contamination from reinforcement learning ...","url":"https://arxiv.org/pdf/2510.09259"},{"title":"Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models","url":"https://arxiv.org/html/2510.09259v1"}]

I found the paper! Here's the information about arXiv 2510.09259:

**Title:** Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models

**Authors:** Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, and Ge Li

**Key Contribution:** The paper conducts the first systematic study of data detection within the RL post-training scenario and proposes Self-Critique.

**Problem Addressed:** While detection methods have been developed for the pre-training and Supervised Fine-Tuning stages, a critical research gap exists for the increasingly significant phase of Reinforcement Learning (RL) post-training.

**Method:** The method is motivated by a key observation: after the RL phase, the output entropy distribution of LLMs tends to collapse into highly specific and sparse modes. Self-Critique addresses data contamination in the RL post-training phase of LLMs by detecting policy collapse, outperforming existing methods with significant improvements in AUC.

The paper was submitted on October 10, 2025, and last revised on March 18, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "05b31905-93a4-47c7-b599-01ae6a21ef42",
  "tool_use_result": {
    "query": "arXiv 2510.09259 \"Detecting Data Contamination\" reinforcement learning authors Wang",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AaGHgMd2uNjYN4SyX3yYGG",
        "content": [
          {
            "title": "[2510.09259] Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/abs/2510.09259"
          },
          {
            "title": "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/396459308_Detecting_Data_Contamination_from_Reinforcement_Learning_Post-training_for_Large_Language_Models"
          },
          {
            "title": "Paper page - Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://huggingface.co/papers/2510.09259"
          },
          {
            "title": "detecting data contamination from reinforcement learning ...",
            "url": "https://arxiv.org/pdf/2510.09259"
          },
          {
            "title": "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
            "url": "https://arxiv.org/html/2510.09259v1"
          }
        ]
      },
      "I found the paper! Here's the information about arXiv 2510.09259:\n\n**Title:** Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models\n\n**Authors:** Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, and Ge Li\n\n**Key Contribution:** The paper conducts the first systematic study of data detection within the RL post-training scenario and proposes Self-Critique.\n\n**Problem Addressed:** While detection methods have been developed for the pre-training and Supervised Fine-Tuning stages, a critical research gap exists for the increasingly significant phase of Reinforcement Learning (RL) post-training.\n\n**Method:** The method is motivated by a key observation: after the RL phase, the output entropy distribution of LLMs tends to collapse into highly specific and sparse modes. Self-Critique addresses data contamination in the RL post-training phase of LLMs by detecting policy collapse, outperforming existing methods with significant improvements in AUC.\n\nThe paper was submitted on October 10, 2025, and last revised on March 18, 2026."
    ],
    "durationSeconds": 9.104659751
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to make all the edits. Let me also check the Wang et al. ICLR 2026 paper more carefully - the authors listed are "Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, and Ge Li" - so it's "Tao, Wang et al." or the user referred to it as "Wang et al." Let me check if this was accepted at ICLR 2026.

Let me also verify the venue for the GSM1K paper - it seems to be NeurIPS 2024 Datasets and Benchmarks track based on the proceedings link.


Now I'm pulling together the Li et al. paper details: it's from Findings of EMNLP 2024, and their contamination detection approach uses Bing Search to identify web overlap with test items, then classifies contamination types as either input-only or input-and-label contamination. They found varying contamination levels across benchmarks ranging from 1-45%, with minimal accuracy impact specifically on MMLU.

For the ConStat paper from NeurIPS 2024, the key distinction is that they define contamination by performance outcomes rather than by source, using statistical tests to compare benchmark performance against a reference benchmark—they achieved an r² of 0.94 when comparing estimated versus ground truth contamination levels.

I also need to note the GSM1K paper by Zhang, Da, and Lee examining large language model performance on grade school arithmetic problems.

For the Growing Pains paper, I've confirmed the arXiv ID is 2604.12843.

There's also a Wang et al. paper coming to ICLR 2026 on detecting data contamination specifically from reinforcement learning post-training in large language models.

I need to verify whether that Wang et al. paper was actually accepted at ICLR 2026 or if it's still just an arXiv preprint—the search results showed it was submitted in October 2025 and revised in March 2026, but I'm not certain about acceptance status, so I should list it conservatively as an arXiv preprint unless I can confirm the venue.

Now I'm planning where to integrate these papers into the document: Li et al. and ConStat both belong in the Contamination Detection section, and I need to figure out whether GSM1K fits there or elsewhere.

GSM1K is more about empirical evidence of contamination, so Section 3 is the right place for it. I also need to adjust how Oren et al. is presented in that section and add the Wang et al. entry as a minor reference. Let me start making these insertions systematically into Section 3.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "3186af7a-5a5a-4777-80c2-63f5c6f1a153",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DgjJnKp4FgzkjeeDy5eSj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 761,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 37358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 929
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 38_

Now I have all the information needed. Let me also load the tools I'll need for registration.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "af77e2b4-38e7-4f41-a8d3-799db9c7f5c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DgjJnKp4FgzkjeeDy5eSj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 761,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 37358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 929
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BAEzeR5wvz66qZm3BNTqM3`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
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
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "04a39c72-d714-45e3-aeb4-b76b372df711",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019DgjJnKp4FgzkjeeDy5eSj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 761,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 37358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 929
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T23:48:30.247Z_

<details><summary>↩ Tool result · `toolu_01BAEzeR5wvz66qZm3BNTqM3`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "3ad96930-1fb3-4441-9ec4-95f781b6d9ba",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 41_

Now making all the edits. Starting with the three new papers, the Oren et al. modification, and the Wang et al. addition.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "6d19e2b8-d952-40ce-a567-124728a50c91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhaeuTqzkWMX7dsy1qM4Er",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2615,
      "cache_read_input_tokens": 38287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2615
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_012Pboo4CKx7Bnm9u61ocz4Z`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_survey_d011.md",
  "old_string": "### Oren et al. (2024)\n- **Title**: Proving Test Set Contamination in Black Box Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Statistical test comparing likelihood of a benchmark's canonical ordering vs. shuffled versions. Contaminated models find canonical orderings more likely due to memorized example order. Provides exact false positive guarantees without requiring access to pretraining data or model weights. Effective on models as small as 1.4B parameters with only 1000 examples.\n- **Relevance to our paper**: Elegant black-box method with formal statistical guarantees. However, it detects dataset-level contamination (is the whole benchmark memorized?) rather than item-level contamination effects (which specific items are affected?). Our DIF approach provides item-level granularity.",
  "new_string": "### Oren et al. (2024)\n- **Title**: Proving Test Set Contamination in Black Box Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Statistical test comparing likelihood of a benchmark's canonical ordering vs. shuffled versions. Contaminated models find canonical orderings more likely due to memorized example order. Provides exact false positive guarantees without requiring access to pretraining data or model weights. Effective on models as small as 1.4B parameters with only 1000 examples.\n- **Relevance to our paper**: Elegant black-box method with formal statistical guarantees. However, it detects dataset-level contamination (is the whole benchmark memorized?) rather than item-level contamination effects (which specific items are affected?). Our DIF approach provides item-level granularity. Notably, canonical ordering 检验是 population-level 方法，与 DIF 更近（都是统计检验方法检测污染），区别在于 Oren 检测记忆顺序而 DIF 检测 differential performance。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "e3dbcbf6-f1ea-407d-b6ff-7ad0342ea15e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhaeuTqzkWMX7dsy1qM4Er",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2615,
      "cache_read_input_tokens": 38287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2615
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T23:48:45.636Z_

<details><summary>↩ Tool result · `toolu_012Pboo4CKx7Bnm9u61ocz4Z`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_survey_d011.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "01025069-f406-447f-a5df-34550c674129",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_survey_d011.md",
    "oldString": "### Oren et al. (2024)\n- **Title**: Proving Test Set Contamination in Black Box Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Statistical test comparing likelihood of a benchmark's canonical ordering vs. shuffled versions. Contaminated models find canonical orderings more likely due to memorized example order. Provides exact false positive guarantees without requiring access to pretraining data or model weights. Effective on models as small as 1.4B parameters with only 1000 examples.\n- **Relevance to our paper**: Elegant black-box method with formal statistical guarantees. However, it detects dataset-level contamination (is the whole benchmark memorized?) rather than item-level contamination effects (which specific items are affected?). Our DIF approach provides item-level granularity.",
    "newString": "### Oren et al. (2024)\n- **Title**: Proving Test Set Contamination in Black Box Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Statistical test comparing likelihood of a benchmark's canonical ordering vs. shuffled versions. Contaminated models find canonical orderings more likely due to memorized example order. Provides exact false positive guarantees without requiring access to pretraining data or model weights. Effective on models as small as 1.4B parameters with only 1000 examples.\n- **Relevance to our paper**: Elegant black-box method with formal statistical guarantees. However, it detects dataset-level contamination (is the whole benchmark memorized?) rather than item-level contamination effects (which specific items are affected?). Our DIF approach provides item-level granularity. Notably, canonical ordering 检验是 population-level 方法，与 DIF 更近（都是统计检验方法检测污染），区别在于 Oren 检测记忆顺序而 DIF 检测 differential performance。",
    "originalFile": "# Literature Survey for Related Work (D011)\n\n## 1. Impact-vs-DIF Classics\n\n### Shealy & Stout (1993)\n- **Title**: A Model-Based Standardization Approach that Separates True Bias/DIF from Group Ability Differences and Detects Test Bias/DTF as Well as Item Bias/DIF\n- **Year**: 1993\n- **Venue**: Psychometrika, 58(2), 159–194\n- **Key method/finding**: Developed the SIBTEST procedure — a nonparametric, IRT model-based method that detects and estimates DIF without requiring item response function (IRF) estimation. Uses a multidimensional IRT model to explain how individual items combine to produce differential test functioning (DTF) at the test level. Employs a regression correction technique to control inflated Type I error while separating true bias from group ability differences.\n- **Relevance to our paper**: SIBTEST is the foundational statistical test for detecting item-level bias across groups. Our DIF-based contamination detection adapts this logic: instead of demographic groups, we compare \"pre-contamination\" vs. \"post-contamination\" model cohorts. The multidimensional DIF framework directly informs our approach to separating genuine ability differences from item-specific anomalies.\n\n### Clauser & Mazor (1998)\n- **Title**: Using Statistical Procedures to Identify Differentially Functioning Test Items\n- **Year**: 1998\n- **Venue**: Educational Measurement: Issues and Practice, 17(1), 31–44\n- **Key method/finding**: Comprehensive review of DIF detection methods including Mantel-Haenszel, logistic regression, and SIBTEST. Documents the landscape of statistical techniques for detecting items that function differently across groups while controlling for overall ability.\n- **Relevance to our paper**: Provides the methodological taxonomy we draw from when selecting DIF detection procedures for the LLM benchmark setting. Establishes that multiple complementary DIF methods exist with different sensitivity profiles — motivating our multi-method approach.\n\n### Zumbo (1999)\n- **Title**: A Handbook on the Theory and Methods of Differential Item Functioning (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type (Ordinal) Item Scores\n- **Year**: 1999\n- **Venue**: Technical report, Directorate of Human Resources Research and Evaluation, Department of National Defense, Ottawa, Canada\n- **Key method/finding**: Presents logistic regression as a unifying framework for DIF analysis applicable to both binary and ordinal item scores. Provides theoretical grounding for understanding DIF as a violation of measurement invariance.\n- **Relevance to our paper**: Our logistic-regression-based DIF detection for binary (correct/incorrect) LLM responses directly follows this framework. Zumbo's formalization of uniform vs. non-uniform DIF maps onto our distinction between items that are uniformly easier for contaminated models vs. items showing interaction effects with model ability.\n\n### Holland & Wainer (1993)\n- **Title**: Differential Item Functioning (edited volume)\n- **Year**: 1993\n- **Venue**: Lawrence Erlbaum Associates, Hillsdale, NJ\n- **Key method/finding**: Definitive reference volume on DIF. Covers methods for detecting test items that function differently across examinee groups, including Mantel-Haenszel, IRT-based methods, and standardization approaches. Establishes the conceptual distinction between item impact (legitimate group differences) and item bias (construct-irrelevant difficulty).\n- **Relevance to our paper**: The impact-vs-bias distinction is the conceptual backbone of our work. We argue that contamination-inflated performance is analogous to construct-irrelevant easiness — a form of DIF where the \"group\" variable is exposure to benchmark data rather than demographics.\n\n---\n\n## 2. IRT in NLP/LLM Evaluation\n\n### Lalor, Wu & Yu (2016)\n- **Title**: Building an Evaluation Scale using Item Response Theory\n- **Year**: 2016\n- **Venue**: EMNLP 2016, pp. 648–657\n- **Key method/finding**: First to propose IRT as an alternative means for gold-standard test-set generation and NLP system evaluation. Demonstrates that IRT can describe characteristics of individual items (difficulty, discriminating power) and account for these in estimating NLP system ability. Applied to Recognizing Textual Entailment.\n- **Relevance to our paper**: Pioneering work establishing that IRT is applicable to NLP evaluation. Our work extends this foundation from simple item characterization to cross-cohort equating and DIF detection.\n\n### Lalor, Wu & Yu (2019)\n- **Title**: Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds\n- **Year**: 2019\n- **Venue**: EMNLP-IJCNLP 2019, Hong Kong\n- **Key method/finding**: Addresses the bottleneck of needing human response patterns to calibrate IRT models by proposing to learn IRT parameters from \"artificial crowds\" of DNN models. Finds medium-to-large positive correlations between parameters learned from human vs. machine response patterns for NLI and sentiment analysis.\n- **Relevance to our paper**: Validates that IRT parameters estimated from machine (model) responses are meaningful and correlate with human-derived parameters. This justifies our use of LLM response matrices for IRT calibration.\n\n### Vania et al. (2021)\n- **Title**: Comparing Test Sets with Item Response Theory\n- **Year**: 2021\n- **Venue**: ACL 2021\n- **Key method/finding**: Evaluated 29 datasets using predictions from 18 pretrained Transformer models via IRT. Found that Quoref, HellaSwag, and MC-TACO best distinguish among SOTA models, while SNLI, MNLI, and CommitmentBank are saturated. Provides a principled way to compare the discriminative quality of benchmark datasets.\n- **Relevance to our paper**: Demonstrates IRT-based benchmark comparison at the dataset level. Our work extends this to item-level analysis across temporal model cohorts, using DIF to detect which specific items have degraded discriminative quality due to contamination.\n\n### Rodriguez et al. (2021)\n- **Title**: Evaluation Examples Are Not Equally Informative: How Should That Change NLP Leaderboards?\n- **Year**: 2021\n- **Venue**: ACL-IJCNLP 2021\n- **Key method/finding**: Creates a Bayesian IRT leaderboard model where latent subject skill and latent item difficulty predict correct responses. Demonstrates that IRT can guide annotation priorities, identify annotation errors, detect overfitting, and identify the most informative evaluation examples. Released open-source IRT leaderboard code.\n- **Relevance to our paper**: Directly relevant methodological predecessor. Their Bayesian IRT approach to leaderboards establishes that item-level modeling reveals evaluation quality issues invisible to aggregate scores. We build on this by using IRT-derived item parameters to detect contamination-induced parameter drift.\n\n### Polo et al. (2024)\n- **Title**: tinyBenchmarks: Evaluating LLMs with Fewer Examples\n- **Year**: 2024\n- **Venue**: ICML 2024\n- **Key method/finding**: Shows that evaluating on ~100 curated IRT-selected items per benchmark is sufficient to accurately reproduce full-benchmark performance. Released IRT-based evaluation tools and tiny versions of Open LLM Leaderboard, MMLU, HELM, and AlpacaEval 2.0. Uses clustering-based item selection to ensure coverage of the difficulty/discrimination space.\n- **Relevance to our paper**: tinyBenchmarks demonstrates the practical value of IRT for efficient evaluation. Their item selection methodology (clustering IRT representations) is adopted by Growing Pains for anchor selection. Our DIF analysis provides a complementary diagnostic: not just which items are informative, but which items have become unreliable due to contamination.\n\n---\n\n## 3. Contamination Detection\n\n### Shi et al. (2024)\n- **Title**: Detecting Pretraining Data from Large Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Proposes MIN-K% PROB — a membership inference method that identifies pretraining data by checking whether the k% of tokens with minimum probability under the LLM are unlikely enough. Introduces the WIKIMIA benchmark for evaluation. Achieves 7.4% improvement over prior methods. Applied to copyrighted book detection, contaminated example detection, and privacy auditing.\n- **Relevance to our paper**: Min-K% operates at the instance level (is this text in the training data?) while our DIF approach operates at the item level across model populations (does this item behave differently for likely-contaminated models?). The approaches are complementary: Min-K% requires model access per instance; DIF requires only response matrices.\n\n### Zhang et al. (2024) — Min-K%++\n- **Title**: Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2025\n- **Key method/finding**: Extends Min-K% by measuring how sharply peaked the likelihood is around the input (analogous to curvature), using second-order statistics motivated by the connection between maximum likelihood training and the Hessian trace via score matching. More robust than zeroth-order signals.\n- **Relevance to our paper**: Further develops the instance-level contamination detection paradigm. Our work offers an orthogonal, population-level signal that does not require per-instance likelihood computation.\n\n### Balloccu et al. (2024)\n- **Title**: Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs\n- **Year**: 2024\n- **Venue**: EACL 2024\n- **Key method/finding**: Systematic review of 255 papers using ChatGPT/GPT-4, documenting that over 4.7M samples from 263 datasets were exposed through the web interface. Catalogs evaluation malpractices including unfair baselines, reproducibility issues, and lack of contamination awareness.\n- **Relevance to our paper**: Establishes the scale and severity of the contamination problem. Their documentation of widespread data leakage motivates our work: if contamination is pervasive and hard to prevent, we need methods to detect and account for it post-hoc — exactly what DIF provides.\n\n### Golchin & Surdeanu (2024)\n- **Title**: Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models\n- **Year**: 2024\n- **Venue**: TACL 2024\n- **Key method/finding**: Frames contamination detection as a multiple-choice quiz: given an original instance and three word-level perturbations, a contaminated model should identify the original. Achieves 92–100% accuracy across seven datasets. Detects specific contamination in AG News, WNLI, and XSum for GPT-4.\n- **Relevance to our paper**: DCQ is a clever per-model, per-instance detection method but requires generating perturbations and querying the model. Our DIF approach is purely observational — it works from existing response matrices without additional model queries or perturbation generation.\n\n### Oren et al. (2024)\n- **Title**: Proving Test Set Contamination in Black Box Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Statistical test comparing likelihood of a benchmark's canonical ordering vs. shuffled versions. Contaminated models find canonical orderings more likely due to memorized example order. Provides exact false positive guarantees without requiring access to pretraining data or model weights. Effective on models as small as 1.4B parameters with only 1000 examples.\n- **Relevance to our paper**: Elegant black-box method with formal statistical guarantees. However, it detects dataset-level contamination (is the whole benchmark memorized?) rather than item-level contamination effects (which specific items are affected?). Our DIF approach provides item-level granularity.\n\n### Deng et al. (2024)\n- **Title**: Investigating Data Contamination in Modern Benchmarks for Large Language Models\n- **Year**: 2024\n- **Venue**: NAACL 2024, pp. 8706–8719\n- **Key method/finding**: Proposes two methods: a retrieval-based system to find overlaps between benchmarks and pretraining corpora (for open-source LLMs), and Testset Slot Guessing (TS-Guessing) for proprietary LLMs. Finds ChatGPT and GPT-4 achieve 52% and 57% exact match rates in guessing missing MMLU options.\n- **Relevance to our paper**: Demonstrates contamination in the exact benchmark (MMLU) we analyze. Their TS-Guessing evidence of MMLU contamination in GPT-4 provides ground-truth validation context for our DIF-based detection.\n\n---\n\n## 4. Dynamic/Adaptive Benchmarks\n\n### Zhu et al. (2024a) — DyVal\n- **Title**: DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Generates evaluation tasks at test time using graph-based complexity control to mitigate memorization. Applies graph complexity metrics to parameterize reasoning problem difficulty. Dynamically constructs evaluation instances rather than relying on static test sets.\n- **Relevance to our paper**: Represents the \"regenerate the benchmark\" approach to contamination. Our work takes the complementary \"detect and account for contamination in existing benchmarks\" approach, which preserves historical comparability.\n\n### Zhu et al. (2024b) — DyVal 2\n- **Title**: Dynamic Evaluation of Large Language Models by Meta Probing Agents\n- **Year**: 2024\n- **Venue**: arXiv:2402.14865\n- **Key method/finding**: Extends DyVal with Meta Probing Agents (MPA) inspired by psychometrics. Agents automatically transform original evaluation problems targeting three cognitive abilities: language understanding, problem solving, and domain knowledge. More generalizable than task-specific dynamic generation.\n- **Relevance to our paper**: MPA's psychometric inspiration is conceptually aligned with our IRT-based approach, but they use psychometrics to generate new items while we use it to analyze existing items for contamination signals.\n\n### White et al. (2024) — LiveBench\n- **Title**: LiveBench: A Challenging, Contamination-Free LLM Benchmark\n- **Year**: 2024\n- **Venue**: arXiv:2406.19314\n- **Key method/finding**: Releases new questions monthly based on recent datasets, arXiv papers, news, and IMDb synopses. All questions have verifiable, objective ground-truth answers enabling automatic scoring without LLM judges. Spans 18 tasks across 6 categories (Math, Reasoning, Data Analysis, Language, Coding, Instruction Following).\n- **Relevance to our paper**: LiveBench's monthly refresh strategy prevents contamination prospectively. Our DIF method detects contamination retrospectively in static benchmarks. The approaches address different temporal windows: LiveBench prevents future contamination; we diagnose past contamination in widely-used benchmarks whose historical results we want to preserve.\n\n### Wang et al. (2024) — MMLU-Pro\n- **Title**: MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark\n- **Year**: 2024\n- **Venue**: NeurIPS 2024\n- **Key method/finding**: Enhances MMLU with harder, reasoning-focused questions and increases answer choices from 4 to 10, reducing random guessing success. Over 12K questions across 14 domains. GPT-4o achieves only 72.6%, and the gap between GPT-4o and GPT-4-Turbo widens from 1% (MMLU) to 9% (MMLU-Pro), showing better discriminative power.\n- **Relevance to our paper**: MMLU-Pro addresses contamination by making a harder benchmark, but doesn't diagnose which original MMLU items are compromised. Our DIF analysis can quantify exactly which MMLU items have degraded, providing evidence for why harder replacements are needed and which content areas are most affected.\n\n### Gema et al. (2024) — MMLU-Redux\n- **Title**: Are We Done with MMLU?\n- **Year**: 2024\n- **Venue**: arXiv:2406.04127\n- **Key method/finding**: Manual re-annotation of 5,700 MMLU questions reveals a 6.5% error rate. Error types include parsing mistakes, multiple correct answers, and missing context. Virology subset has 57% errors. Re-evaluation with corrected labels shows significant metric discrepancies and ranking shifts.\n- **Relevance to our paper**: MMLU-Redux addresses data quality while our work addresses contamination — both are sources of measurement error. Items flagged by DIF analysis that are not contaminated may instead have quality issues, making these analyses complementary.\n\n---\n\n## 5. Key Technical Comparisons\n\n### Habba, Itzhak, Yehudai, Perlitz, Bandel, Shmueli-Scheuer, Choshen & Stanovsky (2026) — Growing Pains\n- **Title**: Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\n- **Year**: 2026 (April)\n- **Venue**: arXiv:2604.12843\n- **Authors**: Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, Gabriel Stanovsky\n\n#### Method Details\n- **IRT Model**: Multidimensional 2PL IRT (MIRT-2PL). Each item has a discrimination vector **a_i** and intercept **d_i**.\n- **Calibration**: Fixed Parameter Calibration (FPC) — previously calibrated item parameters are held fixed; only new item parameters are estimated when new benchmarks are added.\n- **Anchor Selection**: Clustering-based method (following Polo et al.) that distributes anchors across the difficulty/discrimination space. Uses 100 anchor items per dataset. Outperforms top-K discrimination selection.\n- **Scale**: 400+ models, evaluated on Open LLM Leaderboard (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, WinoGrande) and MMLU's 57 subjects.\n- **Performance**: Predicts full-evaluation performance within 2–3 percentage points; Spearman ρ ≥ 0.9 for ranking preservation.\n\n#### Technical Comparison with Our Approach\n\n| Dimension | Growing Pains | Our DIF Approach |\n|-----------|---------------|------------------|\n| **Goal** | Efficient, extensible benchmarking via FPC | Detect contamination-induced measurement distortion |\n| **IRT model** | MIRT-2PL | 2PL (with DIF extensions) |\n| **Core technique** | Fixed parameter calibration with anchor items | DIF analysis across temporal model cohorts |\n| **Contamination** | Acknowledged as limitation (\"anchors may become contaminated or saturated over time, requiring recalibration\") but **not addressed** | Central focus — DIF detects which items are affected |\n| **Item drift** | Not detected; assumes item parameters are stable | Explicitly models item parameter drift as DIF signal |\n| **DIF analysis** | Not mentioned | Core methodology |\n| **Granularity** | Dataset/benchmark level efficiency | Item-level contamination diagnostics |\n| **Binary response** | Yes (limitation acknowledged) | Yes |\n\n#### Complementarity\nGrowing Pains and our work are highly complementary:\n1. **They assume stable item parameters; we test that assumption.** Their FPC framework relies on anchor item parameters not drifting. Our DIF analysis can identify when this assumption breaks down due to contamination.\n2. **They optimize evaluation efficiency; we diagnose evaluation validity.** Growing Pains reduces the number of items needed; we identify which items should be trusted.\n3. **Their acknowledged limitation is our research question.** They note \"anchors may become contaminated or saturated over time, requiring recalibration\" but do not address it. We provide the diagnostic tool for exactly this problem.\n4. **Integration pathway**: DIF-flagged items could be excluded from Growing Pains' anchor sets, making their FPC calibration more robust to contamination.\n\n### Kipnis et al. (2025) — METABENCH\n- **Title**: MetaBench: A Sparse Benchmark for LLM Evaluation\n- **Year**: 2025\n- **Venue**: ICLR 2025\n- **Key method/finding**: Distills six Open LLM Leaderboard benchmarks (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, WinoGrande) into <3% of their combined size using data from 5000+ LLMs. Uses Generalized Additive Models (GAM) to model subset-to-full-set relationships. Reconstructs benchmark scores with <0.9% MAE and leaderboard scores with <0.5% MAE. Provides two disjoint versions for repeated evaluation. Integrated into EleutherAI's lm-evaluation-harness.\n- **Relevance to our paper**: METABENCH is our primary data source — we use their 5000+ model response matrices for IRT calibration and DIF analysis. Their item selection optimizes for predictive accuracy of aggregate scores; our DIF analysis adds a validity dimension by identifying which items remain measurement-invariant across model cohorts. Items selected by MetaBench that we flag as contaminated would suggest the sparse benchmark itself may be vulnerable to contamination effects.\n",
    "structuredPatch": [
      {
        "oldStart": 106,
        "oldLines": 7,
        "newStart": 106,
        "newLines": 7,
        "lines": [
          " - **Year**: 2024",
          " - **Venue**: ICLR 2024",
          " - **Key method/finding**: Statistical test comparing likelihood of a benchmark's canonical ordering vs. shuffled versions. Contaminated models find canonical orderings more likely due to memorized example order. Provides exact false positive guarantees without requiring access to pretraining data or model weights. Effective on models as small as 1.4B parameters with only 1000 examples.",
          "-- **Relevance to our paper**: Elegant black-box method with formal statistical guarantees. However, it detects dataset-level contamination (is the whole benchmark memorized?) rather than item-level contamination effects (which specific items are affected?). Our DIF approach provides item-level granularity.",
          "+- **Relevance to our paper**: Elegant black-box method with formal statistical guarantees. However, it detects dataset-level contamination (is the whole benchmark memorized?) rather than item-level contamination effects (which specific items are affected?). Our DIF approach provides item-level granularity. Notably, canonical ordering 检验是 population-level 方法，与 DIF 更近（都是统计检验方法检测污染），区别在于 Oren 检测记忆顺序而 DIF 检测 differential performance。",
          " ",
          " ### Deng et al. (2024)",
          " - **Title**: Investigating Data Contamination in Modern Benchmarks for Large Language Models"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_01CcuipjwAbVzjvq8QhxcYj1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_survey_d011.md",
  "old_string": "### Deng et al. (2024)\n- **Title**: Investigating Data Contamination in Modern Benchmarks for Large Language Models",
  "new_string": "### Li et al. (2024) — Contamination Detector\n- **Title**: An Open-Source Data Contamination Report for Large Language Models\n- **Year**: 2024\n- **Venue**: Findings of EMNLP 2024, pp. 528–541\n- **Authors**: Yucheng Li, Yunhao Guo, Frank Guerin, Chenghua Lin\n- **Key method/finding**: Two-step contamination detection pipeline: (1) Bing Search API checks whether test items appear verbatim on the web (web-overlap detection), (2) human annotation classifies items as clean, input-only contaminated, or input-and-label contaminated. Provides 9,229 item-level web-overlap annotations for MMLU. Finds contamination levels ranging from 1% to 45% across six benchmarks, with contamination degree increasing rapidly over time. On MMLU, contamination causes only minimal accuracy increase despite substantial overlap.\n- **Relevance to our paper**: **Primary ground truth source.** Their 9,229 item-level MMLU annotations provide the ground truth labels we use to validate DIF enrichment. Critical finding: enrichment ≈ 1.0 because their annotations capture *global* contamination (items available in Common Crawl accessible to all models), whereas DIF detects *differential* contamination (items that differentially advantage specific model cohorts). This global-vs-differential distinction is a key conceptual contribution of our work.\n\n### Dekoninck et al. (2024) — ConStat\n- **Title**: ConStat: Performance-Based Contamination Detection in Large Language Models\n- **Year**: 2024\n- **Venue**: NeurIPS 2024\n- **Authors**: Jasper Dekoninck, Mark Niklas Müller, Martin Vechev\n- **arXiv**: 2405.16281\n- **Key method/finding**: Proposes a performance-based definition of contamination — defines contamination by its outcome (artificially inflated, non-generalizing benchmark performance) rather than its cause (training data overlap). Statistical test compares a model's performance on the target benchmark against reference benchmarks (rephrased samples, same-distribution samples, or different benchmarks for the same task). Achieves r² = 0.94 between estimated and ground-truth contamination effects. Finds high contamination levels in Mistral, Llama, Yi, and top Open LLM Leaderboard models.\n- **Relevance to our paper**: ConStat and DIF are complementary population-level statistical approaches. ConStat detects whether a model's benchmark performance generalizes (performance anomaly); DIF detects whether specific items function differently across model cohorts (item-level anomaly). ConStat requires a reference benchmark for comparison; DIF requires only the original response matrix with temporal cohort labels. Together they cover both the model-level and item-level perspectives on contamination.\n\n### Zhang et al. (2024) — GSM1K\n- **Title**: A Careful Examination of Large Language Model Performance on Grade School Arithmetic\n- **Year**: 2024\n- **Venue**: NeurIPS 2024 (Datasets and Benchmarks Track)\n- **Authors**: Hugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Dylan Slack, Qin Lyu, Sean Hendryx, Russell Kaplan, Michele Lunati, Summer Yue\n- **arXiv**: 2405.00332\n- **Key method/finding**: Creates GSM1K — 1,000 new grade-school math problems designed to mirror GSM8K's style and difficulty. Landmark empirical evidence of benchmark contamination: models show accuracy drops of up to 13 percentage points on fresh problems vs. GSM8K. Phi and Mistral families show systematic overfitting across almost all model sizes. Positive correlation (Spearman r² = 0.36) between a model's probability of generating GSM8K examples and its GSM8K-vs-GSM1K performance gap. Frontier models (GPT-4, Claude) show minimal memorization.\n- **Relevance to our paper**: **Motivating example** for benchmark contamination as a real, quantifiable problem. The 10–13pp accuracy drops demonstrate that contamination materially distorts evaluation. Our DIF approach provides a complementary diagnostic: instead of creating a parallel benchmark (costly), DIF identifies which items in the *existing* benchmark are compromised, enabling in-situ contamination assessment.\n\n### Deng et al. (2024)\n- **Title**: Investigating Data Contamination in Modern Benchmarks for Large Language Models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "31d37672-4bac-4a8f-b02b-6c97f5d693bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014qvWrsXy3iofcSNB2aoAD5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 40902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 706
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T23:49:20.390Z_

<details><summary>↩ Tool result · `toolu_01CcuipjwAbVzjvq8QhxcYj1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_survey_d011.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "5e7179a3-ebac-4ec7-aa54-8bc567133228",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_survey_d011.md",
    "oldString": "### Deng et al. (2024)\n- **Title**: Investigating Data Contamination in Modern Benchmarks for Large Language Models",
    "newString": "### Li et al. (2024) — Contamination Detector\n- **Title**: An Open-Source Data Contamination Report for Large Language Models\n- **Year**: 2024\n- **Venue**: Findings of EMNLP 2024, pp. 528–541\n- **Authors**: Yucheng Li, Yunhao Guo, Frank Guerin, Chenghua Lin\n- **Key method/finding**: Two-step contamination detection pipeline: (1) Bing Search API checks whether test items appear verbatim on the web (web-overlap detection), (2) human annotation classifies items as clean, input-only contaminated, or input-and-label contaminated. Provides 9,229 item-level web-overlap annotations for MMLU. Finds contamination levels ranging from 1% to 45% across six benchmarks, with contamination degree increasing rapidly over time. On MMLU, contamination causes only minimal accuracy increase despite substantial overlap.\n- **Relevance to our paper**: **Primary ground truth source.** Their 9,229 item-level MMLU annotations provide the ground truth labels we use to validate DIF enrichment. Critical finding: enrichment ≈ 1.0 because their annotations capture *global* contamination (items available in Common Crawl accessible to all models), whereas DIF detects *differential* contamination (items that differentially advantage specific model cohorts). This global-vs-differential distinction is a key conceptual contribution of our work.\n\n### Dekoninck et al. (2024) — ConStat\n- **Title**: ConStat: Performance-Based Contamination Detection in Large Language Models\n- **Year**: 2024\n- **Venue**: NeurIPS 2024\n- **Authors**: Jasper Dekoninck, Mark Niklas Müller, Martin Vechev\n- **arXiv**: 2405.16281\n- **Key method/finding**: Proposes a performance-based definition of contamination — defines contamination by its outcome (artificially inflated, non-generalizing benchmark performance) rather than its cause (training data overlap). Statistical test compares a model's performance on the target benchmark against reference benchmarks (rephrased samples, same-distribution samples, or different benchmarks for the same task). Achieves r² = 0.94 between estimated and ground-truth contamination effects. Finds high contamination levels in Mistral, Llama, Yi, and top Open LLM Leaderboard models.\n- **Relevance to our paper**: ConStat and DIF are complementary population-level statistical approaches. ConStat detects whether a model's benchmark performance generalizes (performance anomaly); DIF detects whether specific items function differently across model cohorts (item-level anomaly). ConStat requires a reference benchmark for comparison; DIF requires only the original response matrix with temporal cohort labels. Together they cover both the model-level and item-level perspectives on contamination.\n\n### Zhang et al. (2024) — GSM1K\n- **Title**: A Careful Examination of Large Language Model Performance on Grade School Arithmetic\n- **Year**: 2024\n- **Venue**: NeurIPS 2024 (Datasets and Benchmarks Track)\n- **Authors**: Hugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Dylan Slack, Qin Lyu, Sean Hendryx, Russell Kaplan, Michele Lunati, Summer Yue\n- **arXiv**: 2405.00332\n- **Key method/finding**: Creates GSM1K — 1,000 new grade-school math problems designed to mirror GSM8K's style and difficulty. Landmark empirical evidence of benchmark contamination: models show accuracy drops of up to 13 percentage points on fresh problems vs. GSM8K. Phi and Mistral families show systematic overfitting across almost all model sizes. Positive correlation (Spearman r² = 0.36) between a model's probability of generating GSM8K examples and its GSM8K-vs-GSM1K performance gap. Frontier models (GPT-4, Claude) show minimal memorization.\n- **Relevance to our paper**: **Motivating example** for benchmark contamination as a real, quantifiable problem. The 10–13pp accuracy drops demonstrate that contamination materially distorts evaluation. Our DIF approach provides a complementary diagnostic: instead of creating a parallel benchmark (costly), DIF identifies which items in the *existing* benchmark are compromised, enabling in-situ contamination assessment.\n\n### Deng et al. (2024)\n- **Title**: Investigating Data Contamination in Modern Benchmarks for Large Language Models",
    "originalFile": "# Literature Survey for Related Work (D011)\n\n## 1. Impact-vs-DIF Classics\n\n### Shealy & Stout (1993)\n- **Title**: A Model-Based Standardization Approach that Separates True Bias/DIF from Group Ability Differences and Detects Test Bias/DTF as Well as Item Bias/DIF\n- **Year**: 1993\n- **Venue**: Psychometrika, 58(2), 159–194\n- **Key method/finding**: Developed the SIBTEST procedure — a nonparametric, IRT model-based method that detects and estimates DIF without requiring item response function (IRF) estimation. Uses a multidimensional IRT model to explain how individual items combine to produce differential test functioning (DTF) at the test level. Employs a regression correction technique to control inflated Type I error while separating true bias from group ability differences.\n- **Relevance to our paper**: SIBTEST is the foundational statistical test for detecting item-level bias across groups. Our DIF-based contamination detection adapts this logic: instead of demographic groups, we compare \"pre-contamination\" vs. \"post-contamination\" model cohorts. The multidimensional DIF framework directly informs our approach to separating genuine ability differences from item-specific anomalies.\n\n### Clauser & Mazor (1998)\n- **Title**: Using Statistical Procedures to Identify Differentially Functioning Test Items\n- **Year**: 1998\n- **Venue**: Educational Measurement: Issues and Practice, 17(1), 31–44\n- **Key method/finding**: Comprehensive review of DIF detection methods including Mantel-Haenszel, logistic regression, and SIBTEST. Documents the landscape of statistical techniques for detecting items that function differently across groups while controlling for overall ability.\n- **Relevance to our paper**: Provides the methodological taxonomy we draw from when selecting DIF detection procedures for the LLM benchmark setting. Establishes that multiple complementary DIF methods exist with different sensitivity profiles — motivating our multi-method approach.\n\n### Zumbo (1999)\n- **Title**: A Handbook on the Theory and Methods of Differential Item Functioning (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type (Ordinal) Item Scores\n- **Year**: 1999\n- **Venue**: Technical report, Directorate of Human Resources Research and Evaluation, Department of National Defense, Ottawa, Canada\n- **Key method/finding**: Presents logistic regression as a unifying framework for DIF analysis applicable to both binary and ordinal item scores. Provides theoretical grounding for understanding DIF as a violation of measurement invariance.\n- **Relevance to our paper**: Our logistic-regression-based DIF detection for binary (correct/incorrect) LLM responses directly follows this framework. Zumbo's formalization of uniform vs. non-uniform DIF maps onto our distinction between items that are uniformly easier for contaminated models vs. items showing interaction effects with model ability.\n\n### Holland & Wainer (1993)\n- **Title**: Differential Item Functioning (edited volume)\n- **Year**: 1993\n- **Venue**: Lawrence Erlbaum Associates, Hillsdale, NJ\n- **Key method/finding**: Definitive reference volume on DIF. Covers methods for detecting test items that function differently across examinee groups, including Mantel-Haenszel, IRT-based methods, and standardization approaches. Establishes the conceptual distinction between item impact (legitimate group differences) and item bias (construct-irrelevant difficulty).\n- **Relevance to our paper**: The impact-vs-bias distinction is the conceptual backbone of our work. We argue that contamination-inflated performance is analogous to construct-irrelevant easiness — a form of DIF where the \"group\" variable is exposure to benchmark data rather than demographics.\n\n---\n\n## 2. IRT in NLP/LLM Evaluation\n\n### Lalor, Wu & Yu (2016)\n- **Title**: Building an Evaluation Scale using Item Response Theory\n- **Year**: 2016\n- **Venue**: EMNLP 2016, pp. 648–657\n- **Key method/finding**: First to propose IRT as an alternative means for gold-standard test-set generation and NLP system evaluation. Demonstrates that IRT can describe characteristics of individual items (difficulty, discriminating power) and account for these in estimating NLP system ability. Applied to Recognizing Textual Entailment.\n- **Relevance to our paper**: Pioneering work establishing that IRT is applicable to NLP evaluation. Our work extends this foundation from simple item characterization to cross-cohort equating and DIF detection.\n\n### Lalor, Wu & Yu (2019)\n- **Title**: Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds\n- **Year**: 2019\n- **Venue**: EMNLP-IJCNLP 2019, Hong Kong\n- **Key method/finding**: Addresses the bottleneck of needing human response patterns to calibrate IRT models by proposing to learn IRT parameters from \"artificial crowds\" of DNN models. Finds medium-to-large positive correlations between parameters learned from human vs. machine response patterns for NLI and sentiment analysis.\n- **Relevance to our paper**: Validates that IRT parameters estimated from machine (model) responses are meaningful and correlate with human-derived parameters. This justifies our use of LLM response matrices for IRT calibration.\n\n### Vania et al. (2021)\n- **Title**: Comparing Test Sets with Item Response Theory\n- **Year**: 2021\n- **Venue**: ACL 2021\n- **Key method/finding**: Evaluated 29 datasets using predictions from 18 pretrained Transformer models via IRT. Found that Quoref, HellaSwag, and MC-TACO best distinguish among SOTA models, while SNLI, MNLI, and CommitmentBank are saturated. Provides a principled way to compare the discriminative quality of benchmark datasets.\n- **Relevance to our paper**: Demonstrates IRT-based benchmark comparison at the dataset level. Our work extends this to item-level analysis across temporal model cohorts, using DIF to detect which specific items have degraded discriminative quality due to contamination.\n\n### Rodriguez et al. (2021)\n- **Title**: Evaluation Examples Are Not Equally Informative: How Should That Change NLP Leaderboards?\n- **Year**: 2021\n- **Venue**: ACL-IJCNLP 2021\n- **Key method/finding**: Creates a Bayesian IRT leaderboard model where latent subject skill and latent item difficulty predict correct responses. Demonstrates that IRT can guide annotation priorities, identify annotation errors, detect overfitting, and identify the most informative evaluation examples. Released open-source IRT leaderboard code.\n- **Relevance to our paper**: Directly relevant methodological predecessor. Their Bayesian IRT approach to leaderboards establishes that item-level modeling reveals evaluation quality issues invisible to aggregate scores. We build on this by using IRT-derived item parameters to detect contamination-induced parameter drift.\n\n### Polo et al. (2024)\n- **Title**: tinyBenchmarks: Evaluating LLMs with Fewer Examples\n- **Year**: 2024\n- **Venue**: ICML 2024\n- **Key method/finding**: Shows that evaluating on ~100 curated IRT-selected items per benchmark is sufficient to accurately reproduce full-benchmark performance. Released IRT-based evaluation tools and tiny versions of Open LLM Leaderboard, MMLU, HELM, and AlpacaEval 2.0. Uses clustering-based item selection to ensure coverage of the difficulty/discrimination space.\n- **Relevance to our paper**: tinyBenchmarks demonstrates the practical value of IRT for efficient evaluation. Their item selection methodology (clustering IRT representations) is adopted by Growing Pains for anchor selection. Our DIF analysis provides a complementary diagnostic: not just which items are informative, but which items have become unreliable due to contamination.\n\n---\n\n## 3. Contamination Detection\n\n### Shi et al. (2024)\n- **Title**: Detecting Pretraining Data from Large Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Proposes MIN-K% PROB — a membership inference method that identifies pretraining data by checking whether the k% of tokens with minimum probability under the LLM are unlikely enough. Introduces the WIKIMIA benchmark for evaluation. Achieves 7.4% improvement over prior methods. Applied to copyrighted book detection, contaminated example detection, and privacy auditing.\n- **Relevance to our paper**: Min-K% operates at the instance level (is this text in the training data?) while our DIF approach operates at the item level across model populations (does this item behave differently for likely-contaminated models?). The approaches are complementary: Min-K% requires model access per instance; DIF requires only response matrices.\n\n### Zhang et al. (2024) — Min-K%++\n- **Title**: Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2025\n- **Key method/finding**: Extends Min-K% by measuring how sharply peaked the likelihood is around the input (analogous to curvature), using second-order statistics motivated by the connection between maximum likelihood training and the Hessian trace via score matching. More robust than zeroth-order signals.\n- **Relevance to our paper**: Further develops the instance-level contamination detection paradigm. Our work offers an orthogonal, population-level signal that does not require per-instance likelihood computation.\n\n### Balloccu et al. (2024)\n- **Title**: Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs\n- **Year**: 2024\n- **Venue**: EACL 2024\n- **Key method/finding**: Systematic review of 255 papers using ChatGPT/GPT-4, documenting that over 4.7M samples from 263 datasets were exposed through the web interface. Catalogs evaluation malpractices including unfair baselines, reproducibility issues, and lack of contamination awareness.\n- **Relevance to our paper**: Establishes the scale and severity of the contamination problem. Their documentation of widespread data leakage motivates our work: if contamination is pervasive and hard to prevent, we need methods to detect and account for it post-hoc — exactly what DIF provides.\n\n### Golchin & Surdeanu (2024)\n- **Title**: Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models\n- **Year**: 2024\n- **Venue**: TACL 2024\n- **Key method/finding**: Frames contamination detection as a multiple-choice quiz: given an original instance and three word-level perturbations, a contaminated model should identify the original. Achieves 92–100% accuracy across seven datasets. Detects specific contamination in AG News, WNLI, and XSum for GPT-4.\n- **Relevance to our paper**: DCQ is a clever per-model, per-instance detection method but requires generating perturbations and querying the model. Our DIF approach is purely observational — it works from existing response matrices without additional model queries or perturbation generation.\n\n### Oren et al. (2024)\n- **Title**: Proving Test Set Contamination in Black Box Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Statistical test comparing likelihood of a benchmark's canonical ordering vs. shuffled versions. Contaminated models find canonical orderings more likely due to memorized example order. Provides exact false positive guarantees without requiring access to pretraining data or model weights. Effective on models as small as 1.4B parameters with only 1000 examples.\n- **Relevance to our paper**: Elegant black-box method with formal statistical guarantees. However, it detects dataset-level contamination (is the whole benchmark memorized?) rather than item-level contamination effects (which specific items are affected?). Our DIF approach provides item-level granularity. Notably, canonical ordering 检验是 population-level 方法，与 DIF 更近（都是统计检验方法检测污染），区别在于 Oren 检测记忆顺序而 DIF 检测 differential performance。\n\n### Deng et al. (2024)\n- **Title**: Investigating Data Contamination in Modern Benchmarks for Large Language Models\n- **Year**: 2024\n- **Venue**: NAACL 2024, pp. 8706–8719\n- **Key method/finding**: Proposes two methods: a retrieval-based system to find overlaps between benchmarks and pretraining corpora (for open-source LLMs), and Testset Slot Guessing (TS-Guessing) for proprietary LLMs. Finds ChatGPT and GPT-4 achieve 52% and 57% exact match rates in guessing missing MMLU options.\n- **Relevance to our paper**: Demonstrates contamination in the exact benchmark (MMLU) we analyze. Their TS-Guessing evidence of MMLU contamination in GPT-4 provides ground-truth validation context for our DIF-based detection.\n\n---\n\n## 4. Dynamic/Adaptive Benchmarks\n\n### Zhu et al. (2024a) — DyVal\n- **Title**: DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Generates evaluation tasks at test time using graph-based complexity control to mitigate memorization. Applies graph complexity metrics to parameterize reasoning problem difficulty. Dynamically constructs evaluation instances rather than relying on static test sets.\n- **Relevance to our paper**: Represents the \"regenerate the benchmark\" approach to contamination. Our work takes the complementary \"detect and account for contamination in existing benchmarks\" approach, which preserves historical comparability.\n\n### Zhu et al. (2024b) — DyVal 2\n- **Title**: Dynamic Evaluation of Large Language Models by Meta Probing Agents\n- **Year**: 2024\n- **Venue**: arXiv:2402.14865\n- **Key method/finding**: Extends DyVal with Meta Probing Agents (MPA) inspired by psychometrics. Agents automatically transform original evaluation problems targeting three cognitive abilities: language understanding, problem solving, and domain knowledge. More generalizable than task-specific dynamic generation.\n- **Relevance to our paper**: MPA's psychometric inspiration is conceptually aligned with our IRT-based approach, but they use psychometrics to generate new items while we use it to analyze existing items for contamination signals.\n\n### White et al. (2024) — LiveBench\n- **Title**: LiveBench: A Challenging, Contamination-Free LLM Benchmark\n- **Year**: 2024\n- **Venue**: arXiv:2406.19314\n- **Key method/finding**: Releases new questions monthly based on recent datasets, arXiv papers, news, and IMDb synopses. All questions have verifiable, objective ground-truth answers enabling automatic scoring without LLM judges. Spans 18 tasks across 6 categories (Math, Reasoning, Data Analysis, Language, Coding, Instruction Following).\n- **Relevance to our paper**: LiveBench's monthly refresh strategy prevents contamination prospectively. Our DIF method detects contamination retrospectively in static benchmarks. The approaches address different temporal windows: LiveBench prevents future contamination; we diagnose past contamination in widely-used benchmarks whose historical results we want to preserve.\n\n### Wang et al. (2024) — MMLU-Pro\n- **Title**: MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark\n- **Year**: 2024\n- **Venue**: NeurIPS 2024\n- **Key method/finding**: Enhances MMLU with harder, reasoning-focused questions and increases answer choices from 4 to 10, reducing random guessing success. Over 12K questions across 14 domains. GPT-4o achieves only 72.6%, and the gap between GPT-4o and GPT-4-Turbo widens from 1% (MMLU) to 9% (MMLU-Pro), showing better discriminative power.\n- **Relevance to our paper**: MMLU-Pro addresses contamination by making a harder benchmark, but doesn't diagnose which original MMLU items are compromised. Our DIF analysis can quantify exactly which MMLU items have degraded, providing evidence for why harder replacements are needed and which content areas are most affected.\n\n### Gema et al. (2024) — MMLU-Redux\n- **Title**: Are We Done with MMLU?\n- **Year**: 2024\n- **Venue**: arXiv:2406.04127\n- **Key method/finding**: Manual re-annotation of 5,700 MMLU questions reveals a 6.5% error rate. Error types include parsing mistakes, multiple correct answers, and missing context. Virology subset has 57% errors. Re-evaluation with corrected labels shows significant metric discrepancies and ranking shifts.\n- **Relevance to our paper**: MMLU-Redux addresses data quality while our work addresses contamination — both are sources of measurement error. Items flagged by DIF analysis that are not contaminated may instead have quality issues, making these analyses complementary.\n\n---\n\n## 5. Key Technical Comparisons\n\n### Habba, Itzhak, Yehudai, Perlitz, Bandel, Shmueli-Scheuer, Choshen & Stanovsky (2026) — Growing Pains\n- **Title**: Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\n- **Year**: 2026 (April)\n- **Venue**: arXiv:2604.12843\n- **Authors**: Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, Gabriel Stanovsky\n\n#### Method Details\n- **IRT Model**: Multidimensional 2PL IRT (MIRT-2PL). Each item has a discrimination vector **a_i** and intercept **d_i**.\n- **Calibration**: Fixed Parameter Calibration (FPC) — previously calibrated item parameters are held fixed; only new item parameters are estimated when new benchmarks are added.\n- **Anchor Selection**: Clustering-based method (following Polo et al.) that distributes anchors across the difficulty/discrimination space. Uses 100 anchor items per dataset. Outperforms top-K discrimination selection.\n- **Scale**: 400+ models, evaluated on Open LLM Leaderboard (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, WinoGrande) and MMLU's 57 subjects.\n- **Performance**: Predicts full-evaluation performance within 2–3 percentage points; Spearman ρ ≥ 0.9 for ranking preservation.\n\n#### Technical Comparison with Our Approach\n\n| Dimension | Growing Pains | Our DIF Approach |\n|-----------|---------------|------------------|\n| **Goal** | Efficient, extensible benchmarking via FPC | Detect contamination-induced measurement distortion |\n| **IRT model** | MIRT-2PL | 2PL (with DIF extensions) |\n| **Core technique** | Fixed parameter calibration with anchor items | DIF analysis across temporal model cohorts |\n| **Contamination** | Acknowledged as limitation (\"anchors may become contaminated or saturated over time, requiring recalibration\") but **not addressed** | Central focus — DIF detects which items are affected |\n| **Item drift** | Not detected; assumes item parameters are stable | Explicitly models item parameter drift as DIF signal |\n| **DIF analysis** | Not mentioned | Core methodology |\n| **Granularity** | Dataset/benchmark level efficiency | Item-level contamination diagnostics |\n| **Binary response** | Yes (limitation acknowledged) | Yes |\n\n#### Complementarity\nGrowing Pains and our work are highly complementary:\n1. **They assume stable item parameters; we test that assumption.** Their FPC framework relies on anchor item parameters not drifting. Our DIF analysis can identify when this assumption breaks down due to contamination.\n2. **They optimize evaluation efficiency; we diagnose evaluation validity.** Growing Pains reduces the number of items needed; we identify which items should be trusted.\n3. **Their acknowledged limitation is our research question.** They note \"anchors may become contaminated or saturated over time, requiring recalibration\" but do not address it. We provide the diagnostic tool for exactly this problem.\n4. **Integration pathway**: DIF-flagged items could be excluded from Growing Pains' anchor sets, making their FPC calibration more robust to contamination.\n\n### Kipnis et al. (2025) — METABENCH\n- **Title**: MetaBench: A Sparse Benchmark for LLM Evaluation\n- **Year**: 2025\n- **Venue**: ICLR 2025\n- **Key method/finding**: Distills six Open LLM Leaderboard benchmarks (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, WinoGrande) into <3% of their combined size using data from 5000+ LLMs. Uses Generalized Additive Models (GAM) to model subset-to-full-set relationships. Reconstructs benchmark scores with <0.9% MAE and leaderboard scores with <0.5% MAE. Provides two disjoint versions for repeated evaluation. Integrated into EleutherAI's lm-evaluation-harness.\n- **Relevance to our paper**: METABENCH is our primary data source — we use their 5000+ model response matrices for IRT calibration and DIF analysis. Their item selection optimizes for predictive accuracy of aggregate scores; our DIF analysis adds a validity dimension by identifying which items remain measurement-invariant across model cohorts. Items selected by MetaBench that we flag as contaminated would suggest the sparse benchmark itself may be vulnerable to contamination effects.\n",
    "structuredPatch": [
      {
        "oldStart": 108,
        "oldLines": 6,
        "newStart": 108,
        "newLines": 32,
        "lines": [
          " - **Key method/finding**: Statistical test comparing likelihood of a benchmark's canonical ordering vs. shuffled versions. Contaminated models find canonical orderings more likely due to memorized example order. Provides exact false positive guarantees without requiring access to pretraining data or model weights. Effective on models as small as 1.4B parameters with only 1000 examples.",
          " - **Relevance to our paper**: Elegant black-box method with formal statistical guarantees. However, it detects dataset-level contamination (is the whole benchmark memorized?) rather than item-level contamination effects (which specific items are affected?). Our DIF approach provides item-level granularity. Notably, canonical ordering 检验是 population-level 方法，与 DIF 更近（都是统计检验方法检测污染），区别在于 Oren 检测记忆顺序而 DIF 检测 differential performance。",
          " ",
          "+### Li et al. (2024) — Contamination Detector",
          "+- **Title**: An Open-Source Data Contamination Report for Large Language Models",
          "+- **Year**: 2024",
          "+- **Venue**: Findings of EMNLP 2024, pp. 528–541",
          "+- **Authors**: Yucheng Li, Yunhao Guo, Frank Guerin, Chenghua Lin",
          "+- **Key method/finding**: Two-step contamination detection pipeline: (1) Bing Search API checks whether test items appear verbatim on the web (web-overlap detection), (2) human annotation classifies items as clean, input-only contaminated, or input-and-label contaminated. Provides 9,229 item-level web-overlap annotations for MMLU. Finds contamination levels ranging from 1% to 45% across six benchmarks, with contamination degree increasing rapidly over time. On MMLU, contamination causes only minimal accuracy increase despite substantial overlap.",
          "+- **Relevance to our paper**: **Primary ground truth source.** Their 9,229 item-level MMLU annotations provide the ground truth labels we use to validate DIF enrichment. Critical finding: enrichment ≈ 1.0 because their annotations capture *global* contamination (items available in Common Crawl accessible to all models), whereas DIF detects *differential* contamination (items that differentially advantage specific model cohorts). This global-vs-differential distinction is a key conceptual contribution of our work.",
          "+",
          "+### Dekoninck et al. (2024) — ConStat",
          "+- **Title**: ConStat: Performance-Based Contamination Detection in Large Language Models",
          "+- **Year**: 2024",
          "+- **Venue**: NeurIPS 2024",
          "+- **Authors**: Jasper Dekoninck, Mark Niklas Müller, Martin Vechev",
          "+- **arXiv**: 2405.16281",
          "+- **Key method/finding**: Proposes a performance-based definition of contamination — defines contamination by its outcome (artificially inflated, non-generalizing benchmark performance) rather than its cause (training data overlap). Statistical test compares a model's performance on the target benchmark against reference benchmarks (rephrased samples, same-distribution samples, or different benchmarks for the same task). Achieves r² = 0.94 between estimated and ground-truth contamination effects. Finds high contamination levels in Mistral, Llama, Yi, and top Open LLM Leaderboard models.",
          "+- **Relevance to our paper**: ConStat and DIF are complementary population-level statistical approaches. ConStat detects whether a model's benchmark performance generalizes (performance anomaly); DIF detects whether specific items function differently across model cohorts (item-level anomaly). ConStat requires a reference benchmark for comparison; DIF requires only the original response matrix with temporal cohort labels. Together they cover both the model-level and item-level perspectives on contamination.",
          "+",
          "+### Zhang et al. (2024) — GSM1K",
          "+- **Title**: A Careful Examination of Large Language Model Performance on Grade School Arithmetic",
          "+- **Year**: 2024",
          "+- **Venue**: NeurIPS 2024 (Datasets and Benchmarks Track)",
          "+- **Authors**: Hugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Dylan Slack, Qin Lyu, Sean Hendryx, Russell Kaplan, Michele Lunati, Summer Yue",
          "+- **arXiv**: 2405.00332",
          "+- **Key method/finding**: Creates GSM1K — 1,000 new grade-school math problems designed to mirror GSM8K's style and difficulty. Landmark empirical evidence of benchmark contamination: models show accuracy drops of up to 13 percentage points on fresh problems vs. GSM8K. Phi and Mistral families show systematic overfitting across almost all model sizes. Positive correlation (Spearman r² = 0.36) between a model's probability of generating GSM8K examples and its GSM8K-vs-GSM1K performance gap. Frontier models (GPT-4, Claude) show minimal memorization.",
          "+- **Relevance to our paper**: **Motivating example** for benchmark contamination as a real, quantifiable problem. The 10–13pp accuracy drops demonstrate that contamination materially distorts evaluation. Our DIF approach provides a complementary diagnostic: instead of creating a parallel benchmark (costly), DIF identifies which items in the *existing* benchmark are compromised, enabling in-situ contamination assessment.",
          "+",
          " ### Deng et al. (2024)",
          " - **Title**: Investigating Data Contamination in Modern Benchmarks for Large Language Models",
          " - **Year**: 2024"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 46_

Now add the Wang et al. (Tao et al.) RL contamination paper at the end of Section 3, before the Section 4 divider.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "070ce8d3-92a3-4578-80ad-5c80411f23ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpL4eZpdn8n1Y8WWFhMg8F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 41608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1335
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Edit · `toolu_01H3mj4EFD6gDiYHcoKhnM6P`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_survey_d011.md",
  "old_string": "---\n\n## 4. Dynamic/Adaptive Benchmarks",
  "new_string": "### Tao, Wang et al. (2025) — Self-Critique\n- **Title**: Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models\n- **Year**: 2025\n- **Venue**: arXiv:2510.09259 (submitted Oct 2025, revised Mar 2026)\n- **Authors**: Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, Ge Li\n- **Key method/finding**: First systematic study of contamination detection in the RL post-training phase. Proposes Self-Critique, motivated by the observation that RL training causes output entropy distribution to collapse into highly specific, sparse modes. Outperforms existing detection methods on AIME, K&K, SAT, GSM8K benchmarks.\n- **Relevance to our paper**: RL post-training can hide contamination signals that pre-training-stage detectors (Min-K%, canonical ordering) would otherwise catch, because RL reshapes output distributions. This is a secondary concern for DIF: if RL masks item-level performance inflation, DIF sensitivity may also be reduced. Worth noting as a limitation context, not a primary comparison target.\n\n---\n\n## 4. Dynamic/Adaptive Benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "9ea60d9a-c6aa-44a7-b02a-85b6b6398762",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpL4eZpdn8n1Y8WWFhMg8F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1335,
      "cache_read_input_tokens": 41608,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1335
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T23:49:33.436Z_

<details><summary>↩ Tool result · `toolu_01H3mj4EFD6gDiYHcoKhnM6P`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_survey_d011.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "8c90f5a7-0d13-418f-8465-4173a1dc4e10",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_survey_d011.md",
    "oldString": "---\n\n## 4. Dynamic/Adaptive Benchmarks",
    "newString": "### Tao, Wang et al. (2025) — Self-Critique\n- **Title**: Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models\n- **Year**: 2025\n- **Venue**: arXiv:2510.09259 (submitted Oct 2025, revised Mar 2026)\n- **Authors**: Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, Ge Li\n- **Key method/finding**: First systematic study of contamination detection in the RL post-training phase. Proposes Self-Critique, motivated by the observation that RL training causes output entropy distribution to collapse into highly specific, sparse modes. Outperforms existing detection methods on AIME, K&K, SAT, GSM8K benchmarks.\n- **Relevance to our paper**: RL post-training can hide contamination signals that pre-training-stage detectors (Min-K%, canonical ordering) would otherwise catch, because RL reshapes output distributions. This is a secondary concern for DIF: if RL masks item-level performance inflation, DIF sensitivity may also be reduced. Worth noting as a limitation context, not a primary comparison target.\n\n---\n\n## 4. Dynamic/Adaptive Benchmarks",
    "originalFile": "# Literature Survey for Related Work (D011)\n\n## 1. Impact-vs-DIF Classics\n\n### Shealy & Stout (1993)\n- **Title**: A Model-Based Standardization Approach that Separates True Bias/DIF from Group Ability Differences and Detects Test Bias/DTF as Well as Item Bias/DIF\n- **Year**: 1993\n- **Venue**: Psychometrika, 58(2), 159–194\n- **Key method/finding**: Developed the SIBTEST procedure — a nonparametric, IRT model-based method that detects and estimates DIF without requiring item response function (IRF) estimation. Uses a multidimensional IRT model to explain how individual items combine to produce differential test functioning (DTF) at the test level. Employs a regression correction technique to control inflated Type I error while separating true bias from group ability differences.\n- **Relevance to our paper**: SIBTEST is the foundational statistical test for detecting item-level bias across groups. Our DIF-based contamination detection adapts this logic: instead of demographic groups, we compare \"pre-contamination\" vs. \"post-contamination\" model cohorts. The multidimensional DIF framework directly informs our approach to separating genuine ability differences from item-specific anomalies.\n\n### Clauser & Mazor (1998)\n- **Title**: Using Statistical Procedures to Identify Differentially Functioning Test Items\n- **Year**: 1998\n- **Venue**: Educational Measurement: Issues and Practice, 17(1), 31–44\n- **Key method/finding**: Comprehensive review of DIF detection methods including Mantel-Haenszel, logistic regression, and SIBTEST. Documents the landscape of statistical techniques for detecting items that function differently across groups while controlling for overall ability.\n- **Relevance to our paper**: Provides the methodological taxonomy we draw from when selecting DIF detection procedures for the LLM benchmark setting. Establishes that multiple complementary DIF methods exist with different sensitivity profiles — motivating our multi-method approach.\n\n### Zumbo (1999)\n- **Title**: A Handbook on the Theory and Methods of Differential Item Functioning (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type (Ordinal) Item Scores\n- **Year**: 1999\n- **Venue**: Technical report, Directorate of Human Resources Research and Evaluation, Department of National Defense, Ottawa, Canada\n- **Key method/finding**: Presents logistic regression as a unifying framework for DIF analysis applicable to both binary and ordinal item scores. Provides theoretical grounding for understanding DIF as a violation of measurement invariance.\n- **Relevance to our paper**: Our logistic-regression-based DIF detection for binary (correct/incorrect) LLM responses directly follows this framework. Zumbo's formalization of uniform vs. non-uniform DIF maps onto our distinction between items that are uniformly easier for contaminated models vs. items showing interaction effects with model ability.\n\n### Holland & Wainer (1993)\n- **Title**: Differential Item Functioning (edited volume)\n- **Year**: 1993\n- **Venue**: Lawrence Erlbaum Associates, Hillsdale, NJ\n- **Key method/finding**: Definitive reference volume on DIF. Covers methods for detecting test items that function differently across examinee groups, including Mantel-Haenszel, IRT-based methods, and standardization approaches. Establishes the conceptual distinction between item impact (legitimate group differences) and item bias (construct-irrelevant difficulty).\n- **Relevance to our paper**: The impact-vs-bias distinction is the conceptual backbone of our work. We argue that contamination-inflated performance is analogous to construct-irrelevant easiness — a form of DIF where the \"group\" variable is exposure to benchmark data rather than demographics.\n\n---\n\n## 2. IRT in NLP/LLM Evaluation\n\n### Lalor, Wu & Yu (2016)\n- **Title**: Building an Evaluation Scale using Item Response Theory\n- **Year**: 2016\n- **Venue**: EMNLP 2016, pp. 648–657\n- **Key method/finding**: First to propose IRT as an alternative means for gold-standard test-set generation and NLP system evaluation. Demonstrates that IRT can describe characteristics of individual items (difficulty, discriminating power) and account for these in estimating NLP system ability. Applied to Recognizing Textual Entailment.\n- **Relevance to our paper**: Pioneering work establishing that IRT is applicable to NLP evaluation. Our work extends this foundation from simple item characterization to cross-cohort equating and DIF detection.\n\n### Lalor, Wu & Yu (2019)\n- **Title**: Learning Latent Parameters without Human Response Patterns: Item Response Theory with Artificial Crowds\n- **Year**: 2019\n- **Venue**: EMNLP-IJCNLP 2019, Hong Kong\n- **Key method/finding**: Addresses the bottleneck of needing human response patterns to calibrate IRT models by proposing to learn IRT parameters from \"artificial crowds\" of DNN models. Finds medium-to-large positive correlations between parameters learned from human vs. machine response patterns for NLI and sentiment analysis.\n- **Relevance to our paper**: Validates that IRT parameters estimated from machine (model) responses are meaningful and correlate with human-derived parameters. This justifies our use of LLM response matrices for IRT calibration.\n\n### Vania et al. (2021)\n- **Title**: Comparing Test Sets with Item Response Theory\n- **Year**: 2021\n- **Venue**: ACL 2021\n- **Key method/finding**: Evaluated 29 datasets using predictions from 18 pretrained Transformer models via IRT. Found that Quoref, HellaSwag, and MC-TACO best distinguish among SOTA models, while SNLI, MNLI, and CommitmentBank are saturated. Provides a principled way to compare the discriminative quality of benchmark datasets.\n- **Relevance to our paper**: Demonstrates IRT-based benchmark comparison at the dataset level. Our work extends this to item-level analysis across temporal model cohorts, using DIF to detect which specific items have degraded discriminative quality due to contamination.\n\n### Rodriguez et al. (2021)\n- **Title**: Evaluation Examples Are Not Equally Informative: How Should That Change NLP Leaderboards?\n- **Year**: 2021\n- **Venue**: ACL-IJCNLP 2021\n- **Key method/finding**: Creates a Bayesian IRT leaderboard model where latent subject skill and latent item difficulty predict correct responses. Demonstrates that IRT can guide annotation priorities, identify annotation errors, detect overfitting, and identify the most informative evaluation examples. Released open-source IRT leaderboard code.\n- **Relevance to our paper**: Directly relevant methodological predecessor. Their Bayesian IRT approach to leaderboards establishes that item-level modeling reveals evaluation quality issues invisible to aggregate scores. We build on this by using IRT-derived item parameters to detect contamination-induced parameter drift.\n\n### Polo et al. (2024)\n- **Title**: tinyBenchmarks: Evaluating LLMs with Fewer Examples\n- **Year**: 2024\n- **Venue**: ICML 2024\n- **Key method/finding**: Shows that evaluating on ~100 curated IRT-selected items per benchmark is sufficient to accurately reproduce full-benchmark performance. Released IRT-based evaluation tools and tiny versions of Open LLM Leaderboard, MMLU, HELM, and AlpacaEval 2.0. Uses clustering-based item selection to ensure coverage of the difficulty/discrimination space.\n- **Relevance to our paper**: tinyBenchmarks demonstrates the practical value of IRT for efficient evaluation. Their item selection methodology (clustering IRT representations) is adopted by Growing Pains for anchor selection. Our DIF analysis provides a complementary diagnostic: not just which items are informative, but which items have become unreliable due to contamination.\n\n---\n\n## 3. Contamination Detection\n\n### Shi et al. (2024)\n- **Title**: Detecting Pretraining Data from Large Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Proposes MIN-K% PROB — a membership inference method that identifies pretraining data by checking whether the k% of tokens with minimum probability under the LLM are unlikely enough. Introduces the WIKIMIA benchmark for evaluation. Achieves 7.4% improvement over prior methods. Applied to copyrighted book detection, contaminated example detection, and privacy auditing.\n- **Relevance to our paper**: Min-K% operates at the instance level (is this text in the training data?) while our DIF approach operates at the item level across model populations (does this item behave differently for likely-contaminated models?). The approaches are complementary: Min-K% requires model access per instance; DIF requires only response matrices.\n\n### Zhang et al. (2024) — Min-K%++\n- **Title**: Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2025\n- **Key method/finding**: Extends Min-K% by measuring how sharply peaked the likelihood is around the input (analogous to curvature), using second-order statistics motivated by the connection between maximum likelihood training and the Hessian trace via score matching. More robust than zeroth-order signals.\n- **Relevance to our paper**: Further develops the instance-level contamination detection paradigm. Our work offers an orthogonal, population-level signal that does not require per-instance likelihood computation.\n\n### Balloccu et al. (2024)\n- **Title**: Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs\n- **Year**: 2024\n- **Venue**: EACL 2024\n- **Key method/finding**: Systematic review of 255 papers using ChatGPT/GPT-4, documenting that over 4.7M samples from 263 datasets were exposed through the web interface. Catalogs evaluation malpractices including unfair baselines, reproducibility issues, and lack of contamination awareness.\n- **Relevance to our paper**: Establishes the scale and severity of the contamination problem. Their documentation of widespread data leakage motivates our work: if contamination is pervasive and hard to prevent, we need methods to detect and account for it post-hoc — exactly what DIF provides.\n\n### Golchin & Surdeanu (2024)\n- **Title**: Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models\n- **Year**: 2024\n- **Venue**: TACL 2024\n- **Key method/finding**: Frames contamination detection as a multiple-choice quiz: given an original instance and three word-level perturbations, a contaminated model should identify the original. Achieves 92–100% accuracy across seven datasets. Detects specific contamination in AG News, WNLI, and XSum for GPT-4.\n- **Relevance to our paper**: DCQ is a clever per-model, per-instance detection method but requires generating perturbations and querying the model. Our DIF approach is purely observational — it works from existing response matrices without additional model queries or perturbation generation.\n\n### Oren et al. (2024)\n- **Title**: Proving Test Set Contamination in Black Box Language Models\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Statistical test comparing likelihood of a benchmark's canonical ordering vs. shuffled versions. Contaminated models find canonical orderings more likely due to memorized example order. Provides exact false positive guarantees without requiring access to pretraining data or model weights. Effective on models as small as 1.4B parameters with only 1000 examples.\n- **Relevance to our paper**: Elegant black-box method with formal statistical guarantees. However, it detects dataset-level contamination (is the whole benchmark memorized?) rather than item-level contamination effects (which specific items are affected?). Our DIF approach provides item-level granularity. Notably, canonical ordering 检验是 population-level 方法，与 DIF 更近（都是统计检验方法检测污染），区别在于 Oren 检测记忆顺序而 DIF 检测 differential performance。\n\n### Li et al. (2024) — Contamination Detector\n- **Title**: An Open-Source Data Contamination Report for Large Language Models\n- **Year**: 2024\n- **Venue**: Findings of EMNLP 2024, pp. 528–541\n- **Authors**: Yucheng Li, Yunhao Guo, Frank Guerin, Chenghua Lin\n- **Key method/finding**: Two-step contamination detection pipeline: (1) Bing Search API checks whether test items appear verbatim on the web (web-overlap detection), (2) human annotation classifies items as clean, input-only contaminated, or input-and-label contaminated. Provides 9,229 item-level web-overlap annotations for MMLU. Finds contamination levels ranging from 1% to 45% across six benchmarks, with contamination degree increasing rapidly over time. On MMLU, contamination causes only minimal accuracy increase despite substantial overlap.\n- **Relevance to our paper**: **Primary ground truth source.** Their 9,229 item-level MMLU annotations provide the ground truth labels we use to validate DIF enrichment. Critical finding: enrichment ≈ 1.0 because their annotations capture *global* contamination (items available in Common Crawl accessible to all models), whereas DIF detects *differential* contamination (items that differentially advantage specific model cohorts). This global-vs-differential distinction is a key conceptual contribution of our work.\n\n### Dekoninck et al. (2024) — ConStat\n- **Title**: ConStat: Performance-Based Contamination Detection in Large Language Models\n- **Year**: 2024\n- **Venue**: NeurIPS 2024\n- **Authors**: Jasper Dekoninck, Mark Niklas Müller, Martin Vechev\n- **arXiv**: 2405.16281\n- **Key method/finding**: Proposes a performance-based definition of contamination — defines contamination by its outcome (artificially inflated, non-generalizing benchmark performance) rather than its cause (training data overlap). Statistical test compares a model's performance on the target benchmark against reference benchmarks (rephrased samples, same-distribution samples, or different benchmarks for the same task). Achieves r² = 0.94 between estimated and ground-truth contamination effects. Finds high contamination levels in Mistral, Llama, Yi, and top Open LLM Leaderboard models.\n- **Relevance to our paper**: ConStat and DIF are complementary population-level statistical approaches. ConStat detects whether a model's benchmark performance generalizes (performance anomaly); DIF detects whether specific items function differently across model cohorts (item-level anomaly). ConStat requires a reference benchmark for comparison; DIF requires only the original response matrix with temporal cohort labels. Together they cover both the model-level and item-level perspectives on contamination.\n\n### Zhang et al. (2024) — GSM1K\n- **Title**: A Careful Examination of Large Language Model Performance on Grade School Arithmetic\n- **Year**: 2024\n- **Venue**: NeurIPS 2024 (Datasets and Benchmarks Track)\n- **Authors**: Hugh Zhang, Jeff Da, Dean Lee, Vaughn Robinson, Catherine Wu, Will Song, Tiffany Zhao, Pranav Raja, Dylan Slack, Qin Lyu, Sean Hendryx, Russell Kaplan, Michele Lunati, Summer Yue\n- **arXiv**: 2405.00332\n- **Key method/finding**: Creates GSM1K — 1,000 new grade-school math problems designed to mirror GSM8K's style and difficulty. Landmark empirical evidence of benchmark contamination: models show accuracy drops of up to 13 percentage points on fresh problems vs. GSM8K. Phi and Mistral families show systematic overfitting across almost all model sizes. Positive correlation (Spearman r² = 0.36) between a model's probability of generating GSM8K examples and its GSM8K-vs-GSM1K performance gap. Frontier models (GPT-4, Claude) show minimal memorization.\n- **Relevance to our paper**: **Motivating example** for benchmark contamination as a real, quantifiable problem. The 10–13pp accuracy drops demonstrate that contamination materially distorts evaluation. Our DIF approach provides a complementary diagnostic: instead of creating a parallel benchmark (costly), DIF identifies which items in the *existing* benchmark are compromised, enabling in-situ contamination assessment.\n\n### Deng et al. (2024)\n- **Title**: Investigating Data Contamination in Modern Benchmarks for Large Language Models\n- **Year**: 2024\n- **Venue**: NAACL 2024, pp. 8706–8719\n- **Key method/finding**: Proposes two methods: a retrieval-based system to find overlaps between benchmarks and pretraining corpora (for open-source LLMs), and Testset Slot Guessing (TS-Guessing) for proprietary LLMs. Finds ChatGPT and GPT-4 achieve 52% and 57% exact match rates in guessing missing MMLU options.\n- **Relevance to our paper**: Demonstrates contamination in the exact benchmark (MMLU) we analyze. Their TS-Guessing evidence of MMLU contamination in GPT-4 provides ground-truth validation context for our DIF-based detection.\n\n---\n\n## 4. Dynamic/Adaptive Benchmarks\n\n### Zhu et al. (2024a) — DyVal\n- **Title**: DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks\n- **Year**: 2024\n- **Venue**: ICLR 2024\n- **Key method/finding**: Generates evaluation tasks at test time using graph-based complexity control to mitigate memorization. Applies graph complexity metrics to parameterize reasoning problem difficulty. Dynamically constructs evaluation instances rather than relying on static test sets.\n- **Relevance to our paper**: Represents the \"regenerate the benchmark\" approach to contamination. Our work takes the complementary \"detect and account for contamination in existing benchmarks\" approach, which preserves historical comparability.\n\n### Zhu et al. (2024b) — DyVal 2\n- **Title**: Dynamic Evaluation of Large Language Models by Meta Probing Agents\n- **Year**: 2024\n- **Venue**: arXiv:2402.14865\n- **Key method/finding**: Extends DyVal with Meta Probing Agents (MPA) inspired by psychometrics. Agents automatically transform original evaluation problems targeting three cognitive abilities: language understanding, problem solving, and domain knowledge. More generalizable than task-specific dynamic generation.\n- **Relevance to our paper**: MPA's psychometric inspiration is conceptually aligned with our IRT-based approach, but they use psychometrics to generate new items while we use it to analyze existing items for contamination signals.\n\n### White et al. (2024) — LiveBench\n- **Title**: LiveBench: A Challenging, Contamination-Free LLM Benchmark\n- **Year**: 2024\n- **Venue**: arXiv:2406.19314\n- **Key method/finding**: Releases new questions monthly based on recent datasets, arXiv papers, news, and IMDb synopses. All questions have verifiable, objective ground-truth answers enabling automatic scoring without LLM judges. Spans 18 tasks across 6 categories (Math, Reasoning, Data Analysis, Language, Coding, Instruction Following).\n- **Relevance to our paper**: LiveBench's monthly refresh strategy prevents contamination prospectively. Our DIF method detects contamination retrospectively in static benchmarks. The approaches address different temporal windows: LiveBench prevents future contamination; we diagnose past contamination in widely-used benchmarks whose historical results we want to preserve.\n\n### Wang et al. (2024) — MMLU-Pro\n- **Title**: MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark\n- **Year**: 2024\n- **Venue**: NeurIPS 2024\n- **Key method/finding**: Enhances MMLU with harder, reasoning-focused questions and increases answer choices from 4 to 10, reducing random guessing success. Over 12K questions across 14 domains. GPT-4o achieves only 72.6%, and the gap between GPT-4o and GPT-4-Turbo widens from 1% (MMLU) to 9% (MMLU-Pro), showing better discriminative power.\n- **Relevance to our paper**: MMLU-Pro addresses contamination by making a harder benchmark, but doesn't diagnose which original MMLU items are compromised. Our DIF analysis can quantify exactly which MMLU items have degraded, providing evidence for why harder replacements are needed and which content areas are most affected.\n\n### Gema et al. (2024) — MMLU-Redux\n- **Title**: Are We Done with MMLU?\n- **Year**: 2024\n- **Venue**: arXiv:2406.04127\n- **Key method/finding**: Manual re-annotation of 5,700 MMLU questions reveals a 6.5% error rate. Error types include parsing mistakes, multiple correct answers, and missing context. Virology subset has 57% errors. Re-evaluation with corrected labels shows significant metric discrepancies and ranking shifts.\n- **Relevance to our paper**: MMLU-Redux addresses data quality while our work addresses contamination — both are sources of measurement error. Items flagged by DIF analysis that are not contaminated may instead have quality issues, making these analyses complementary.\n\n---\n\n## 5. Key Technical Comparisons\n\n### Habba, Itzhak, Yehudai, Perlitz, Bandel, Shmueli-Scheuer, Choshen & Stanovsky (2026) — Growing Pains\n- **Title**: Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\n- **Year**: 2026 (April)\n- **Venue**: arXiv:2604.12843\n- **Authors**: Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, Gabriel Stanovsky\n\n#### Method Details\n- **IRT Model**: Multidimensional 2PL IRT (MIRT-2PL). Each item has a discrimination vector **a_i** and intercept **d_i**.\n- **Calibration**: Fixed Parameter Calibration (FPC) — previously calibrated item parameters are held fixed; only new item parameters are estimated when new benchmarks are added.\n- **Anchor Selection**: Clustering-based method (following Polo et al.) that distributes anchors across the difficulty/discrimination space. Uses 100 anchor items per dataset. Outperforms top-K discrimination selection.\n- **Scale**: 400+ models, evaluated on Open LLM Leaderboard (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, WinoGrande) and MMLU's 57 subjects.\n- **Performance**: Predicts full-evaluation performance within 2–3 percentage points; Spearman ρ ≥ 0.9 for ranking preservation.\n\n#### Technical Comparison with Our Approach\n\n| Dimension | Growing Pains | Our DIF Approach |\n|-----------|---------------|------------------|\n| **Goal** | Efficient, extensible benchmarking via FPC | Detect contamination-induced measurement distortion |\n| **IRT model** | MIRT-2PL | 2PL (with DIF extensions) |\n| **Core technique** | Fixed parameter calibration with anchor items | DIF analysis across temporal model cohorts |\n| **Contamination** | Acknowledged as limitation (\"anchors may become contaminated or saturated over time, requiring recalibration\") but **not addressed** | Central focus — DIF detects which items are affected |\n| **Item drift** | Not detected; assumes item parameters are stable | Explicitly models item parameter drift as DIF signal |\n| **DIF analysis** | Not mentioned | Core methodology |\n| **Granularity** | Dataset/benchmark level efficiency | Item-level contamination diagnostics |\n| **Binary response** | Yes (limitation acknowledged) | Yes |\n\n#### Complementarity\nGrowing Pains and our work are highly complementary:\n1. **They assume stable item parameters; we test that assumption.** Their FPC framework relies on anchor item parameters not drifting. Our DIF analysis can identify when this assumption breaks down due to contamination.\n2. **They optimize evaluation efficiency; we diagnose evaluation validity.** Growing Pains reduces the number of items needed; we identify which items should be trusted.\n3. **Their acknowledged limitation is our research question.** They note \"anchors may become contaminated or saturated over time, requiring recalibration\" but do not address it. We provide the diagnostic tool for exactly this problem.\n4. **Integration pathway**: DIF-flagged items could be excluded from Growing Pains' anchor sets, making their FPC calibration more robust to contamination.\n\n### Kipnis et al. (2025) — METABENCH\n- **Title**: MetaBench: A Sparse Benchmark for LLM Evaluation\n- **Year**: 2025\n- **Venue**: ICLR 2025\n- **Key method/finding**: Distills six Open LLM Leaderboard benchmarks (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, WinoGrande) into <3% of their combined size using data from 5000+ LLMs. Uses Generalized Additive Models (GAM) to model subset-to-full-set relationships. Reconstructs benchmark scores with <0.9% MAE and leaderboard scores with <0.5% MAE. Provides two disjoint versions for repeated evaluation. Integrated into EleutherAI's lm-evaluation-harness.\n- **Relevance to our paper**: METABENCH is our primary data source — we use their 5000+ model response matrices for IRT calibration and DIF analysis. Their item selection optimizes for predictive accuracy of aggregate scores; our DIF analysis adds a validity dimension by identifying which items remain measurement-invariant across model cohorts. Items selected by MetaBench that we flag as contaminated would suggest the sparse benchmark itself may be vulnerable to contamination effects.\n",
    "structuredPatch": [
      {
        "oldStart": 141,
        "oldLines": 6,
        "newStart": 141,
        "newLines": 14,
        "lines": [
          " - **Key method/finding**: Proposes two methods: a retrieval-based system to find overlaps between benchmarks and pretraining corpora (for open-source LLMs), and Testset Slot Guessing (TS-Guessing) for proprietary LLMs. Finds ChatGPT and GPT-4 achieve 52% and 57% exact match rates in guessing missing MMLU options.",
          " - **Relevance to our paper**: Demonstrates contamination in the exact benchmark (MMLU) we analyze. Their TS-Guessing evidence of MMLU contamination in GPT-4 provides ground-truth validation context for our DIF-based detection.",
          " ",
          "+### Tao, Wang et al. (2025) — Self-Critique",
          "+- **Title**: Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
          "+- **Year**: 2025",
          "+- **Venue**: arXiv:2510.09259 (submitted Oct 2025, revised Mar 2026)",
          "+- **Authors**: Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, Ge Li",
          "+- **Key method/finding**: First systematic study of contamination detection in the RL post-training phase. Proposes Self-Critique, motivated by the observation that RL training causes output entropy distribution to collapse into highly specific, sparse modes. Outperforms existing detection methods on AIME, K&K, SAT, GSM8K benchmarks.",
          "+- **Relevance to our paper**: RL post-training can hide contamination signals that pre-training-stage detectors (Min-K%, canonical ordering) would otherwise catch, because RL reshapes output distributions. This is a secondary concern for DIF: if RL masks item-level performance inflation, DIF sensitivity may also be reduced. Worth noting as a limitation context, not a primary comparison target.",
          "+",
          " ---",
          " ",
          " ## 4. Dynamic/Adaptive Benchmarks"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 49_

Growing Pains arXiv ID already confirmed as 2604.12843 — no change needed. Now register the updated artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "4ce4e0f3-f32f-4afa-9b23-930a9a354c46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176cpP43GGuzUYF5bRMf7XJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 42943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 670
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_016jwnZQjAmjknb7UmVkR9iq`</summary>

```json
{
  "name": "literature_survey_d011",
  "type": "report",
  "description": "Literature survey for Related Work (D011) — updated with Li et al. (Contamination Detector), ConStat, GSM1K, Tao/Wang et al. (Self-Critique), and Oren et al. relevance修正",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_survey_d011.md",
  "tags": [
    "literature",
    "related-work",
    "contamination",
    "DIF",
    "IRT"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "411b761d-a4b6-4bd6-aa60-f339976b9ae1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176cpP43GGuzUYF5bRMf7XJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 670,
      "cache_read_input_tokens": 42943,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 670
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-20T23:49:41.115Z_

<details><summary>↩ Tool result · `toolu_016jwnZQjAmjknb7UmVkR9iq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_167b57\", \"name\": \"literature_survey_d011\", \"type\": \"report\", \"description\": \"Literature survey for Related Work (D011) — updated with Li et al. (Contamination Detector), ConStat, GSM1K, Tao/Wang et al. (Self-Critique), and Oren et al. relevance修正\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/report/literature_survey_d011_167b57.md\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T23:49:40.539027+00:00\", \"tags\": [\"literature\", \"related-work\", \"contamination\", \"DIF\", \"IRT\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "e6b87b54-2e38-4ff9-8e26-395ebcb11fa2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260520_167b57\\\", \\\"name\\\": \\\"literature_survey_d011\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"Literature survey for Related Work (D011) — updated with Li et al. (Contamination Detector), ConStat, GSM1K, Tao/Wang et al. (Self-Critique), and Oren et al. relevance修正\\\", \\\"path\\\": \\\"projects/irt_equated_bench_regen/artifacts/_project/report/literature_survey_d011_167b57.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"irt_equated_bench_regen\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-20T23:49:40.539027+00:00\\\", \\\"tags\\\": [\\\"literature\\\", \\\"related-work\\\", \\\"contamination\\\", \\\"DIF\\\", \\\"IRT\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_167b57\", \"name\": \"literature_survey_d011\", \"type\": \"report\", \"description\": \"Literature survey for Related Work (D011) — updated with Li et al. (Contamination Detector), ConStat, GSM1K, Tao/Wang et al. (Self-Critique), and Oren et al. relevance修正\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/report/literature_survey_d011_167b57.md\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T23:49:40.539027+00:00\", \"tags\": [\"literature\", \"related-work\", \"contamination\", \"DIF\", \"IRT\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 52_

完成。文件已更新并注册。变更摘要：

**新增 3 篇文献（Section 3）：**
- **Li et al. (EMNLP 2024)** — Contamination Detector，9,229 条 MMLU item-level web-overlap 标注。定位为 primary ground truth source，解释了 enrichment≈1.0 的原因（global vs differential contamination 区分）。
- **Dekoninck et al. (NeurIPS 2024)** — ConStat，performance-based 污染检测。与 DIF 互补：ConStat 检测 model-level performance anomaly，DIF 检测 item-level differential functioning。
- **Zhang et al. (NeurIPS 2024)** — GSM1K，10–13pp accuracy drop 的里程碑实证。定位为 motivating example。

**次要修正：**
- **Oren et al.** — 补充了 canonical ordering 与 DIF 的方法论近似性和区别（都是统计检验，但检测目标不同）。
- **Growing Pains arXiv ID** — 确认 2604.12843 无误，无需修改。
- **Tao, Wang et al. (arXiv 2510.09259)** — 新增 Self-Critique 条目，RL post-training 隐藏污染信号，作为次要条目列入 Section 3 末尾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "uuid": "aed98570-19c9-4973-8997-965eee2a8256",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrvgQLvJZdByAMYWxHdLDx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 635,
      "cache_read_input_tokens": 43613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 635
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 53_

完成。文件已更新并注册。变更摘要：

**新增 3 篇文献（Section 3）：**
- **Li et al. (EMNLP 2024)** — Contamination Detector，9,229 条 MMLU item-level web-overlap 标注。定位为 primary ground truth source，解释了 enrichment≈1.0 的原因（global vs differential contamination 区分）。
- **Dekoninck et al. (NeurIPS 2024)** — ConStat，performance-based 污染检测。与 DIF 互补：ConStat 检测 model-level performance anomaly，DIF 检测 item-level differential functioning。
- **Zhang et al. (NeurIPS 2024)** — GSM1K，10–13pp accuracy drop 的里程碑实证。定位为 motivating example。

**次要修正：**
- **Oren et al.** — 补充了 canonical ordering 与 DIF 的方法论近似性和区别（都是统计检验，但检测目标不同）。
- **Growing Pains arXiv ID** — 确认 2604.12843 无误，无需修改。
- **Tao, Wang et al. (arXiv 2510.09259)** — 新增 Self-Critique 条目，RL post-training 隐藏污染信号，作为次要条目列入 Section 3 末尾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 185553,
  "duration_api_ms": 238600,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "3d41ade3-5397-4be5-ac06-f5d9ef05d71f",
  "total_cost_usd": 0.7826207500000002,
  "usage": {
    "input_tokens": 2960,
    "cache_creation_input_tokens": 32407,
    "cache_read_input_tokens": 341234,
    "output_tokens": 5746,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32407,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 391,
        "cache_read_input_tokens": 43613,
        "cache_creation_input_tokens": 635,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 635
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 117210,
      "outputTokens": 4760,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 11,
      "costUSD": 0.25100999999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 2960,
      "outputTokens": 5746,
      "cacheReadInputTokens": 341234,
      "cacheCreationInputTokens": 32407,
      "webSearchRequests": 0,
      "costUSD": 0.53161075,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b8c5021e-9033-4e42-901b-c48a2e676d9c"
}
```

</details>

---
