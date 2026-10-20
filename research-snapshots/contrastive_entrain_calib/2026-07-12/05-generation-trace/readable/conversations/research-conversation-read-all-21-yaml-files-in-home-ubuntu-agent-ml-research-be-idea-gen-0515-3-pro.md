# Research conversation: Read all 21 YAML files in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a316456ab2fcd624d.jsonl`
- **Structured JSON:** [`f1970cd56ea4a1a35061.json`](../../sessions/f1/f1970cd56ea4a1a35061.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

46 recorded events

### User

_source line 1 · 2026-05-24T17:44:12.747Z_

Read all 21 YAML files in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/ and return their complete contents concatenated together. The files are:

ackermann2026gradreg.yaml
burns2023ccs.yaml
casper2023openproblems.yaml
consistency2025bctact.yaml
denison2024subterfuge.yaml
gao2023scaling.yaml
li2023iti.yaml
mckinney2023fragility.yaml
obrien2025fewbadneurons.yaml
rimsky2024caa.yaml
shao2024grpo.yaml
shapira2026amplifies.yaml
sharma2023sycophancy.yaml
sinii2025smallvectors.yaml
skalse2022hacking.yaml
turner2023actadd.yaml
wang2025internal.yaml
wei2024synthetic.yaml
wen2024mislead.yaml
zhang2026latentgrpo.yaml
zou2023repe.yaml

Read each file completely and output all contents. This is research-only - do not edit anything.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "ba245091-6466-4b52-af3f-be0e14370caf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-24T17:44:12.752Z_

```json
{
  "parentUuid": "ba245091-6466-4b52-af3f-be0e14370caf",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "55508ba6-0169-4d81-89cb-bcc20eb3b714",
  "timestamp": "2026-05-24T17:44:12.752Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-24T17:44:15.344Z_



I'll read all 21 YAML files. Let me fetch them all in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55508ba6-0169-4d81-89cb-bcc20eb3b714",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bc989a33-7aec-4725-958f-ccfed636d937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T17:44:15.836Z_

<details open><summary>🔧 Tool call — Read · `toolu_015YN2UD1xCWs3t1Xw8vmB4a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/ackermann2026gradreg.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc989a33-7aec-4725-958f-ccfed636d937",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "810405dc-6678-4f9f-9474-553fc8eae186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-24T17:44:15.854Z_

<details><summary>↩ Tool result · `toolu_015YN2UD1xCWs3t1Xw8vmB4a`</summary>

```text
1	paper_key: "ackermann2026gradreg"
2	title: "Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards"
3	venue: "arXiv 2026"
4	full_text_available: false
5	
6	research:
7	  baselines:
8	    - KL penalty (standard RLHF regularization)
9	    - Unregularized RLHF
10	  metrics:
11	    - {name: "Reward hacking rate", direction: "lower_better"}
12	    - {name: "GPT-judged task quality", direction: "higher_better"}
13	    - {name: "Rule-based math reward accuracy", direction: "higher_better"}
14	    - {name: "LLM-as-a-Judge evaluation", direction: "higher_better"}
15	    - {name: "Gradient norm", direction: "lower_better"}
16	    - {name: "Reward model accuracy", direction: "higher_better"}
17	  datasets:
18	    - {name: "GPT-judged tasks", size: "not specified"}
19	    - {name: "Rule-based math rewards", size: "not specified"}
20	    - {name: "LLM-as-a-Judge evaluations", size: "not specified"}
21	  ablation_dimensions:
22	    - regularization method (GR vs KL penalty vs none)
23	    - reward type (learned reward model vs verifiable/rule-based)
24	    - gradient norm correlation with reward accuracy
25	  training_recipe:
26	    optimizer: "RLHF with gradient regularization (GR)"
27	    lr: "not specified"
28	    hardware: "not specified"
29	    key_technique: "bias policy updates towards flatter regions where reward is more accurate"
30	  method_family: "gradient regularization for reward hacking prevention"
31	
32	positioning:
33	  core_claim: "Gradient regularization (GR) biases RLHF training towards flatter regions where reward models are more accurate, theoretically grounded in the connection between reward accuracy and optimum flatness, and outperforms KL penalties across GPT-judged, rule-based, and LLM-as-a-Judge evaluations."
34	  key_results: "GR outperforms KL penalties across multiple evaluation settings; gradient norm and reward accuracy are empirically correlated; theoretical connection established between reward accuracy and flatness of convergence optimum."
35	  limitations:
36	    - "Theoretical analysis may rely on simplifying assumptions"
37	    - "Flatness-accuracy connection may not hold universally"
38	    - "Computational overhead of gradient regularization not discussed in abstract"
39	  relation_to_us: "complementary"
40	
41	narrative: N/A
42	figures: N/A
43	tables: N/A
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "810405dc-6678-4f9f-9474-553fc8eae186",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "71608a79-f0ff-4a5e-bb6a-3e6ff0d77ff6",
  "sourceToolAssistantUUID": "810405dc-6678-4f9f-9474-553fc8eae186",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T17:44:16.309Z_

<details open><summary>🔧 Tool call — Read · `toolu_011w8qw2xu9js4DVKgCeiaPf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/burns2023ccs.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71608a79-f0ff-4a5e-bb6a-3e6ff0d77ff6",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "79d5378a-57d6-4277-84cd-51153d0664c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-24T17:44:16.317Z_

<details><summary>↩ Tool result · `toolu_011w8qw2xu9js4DVKgCeiaPf`</summary>

```text
1	paper_key: "burns2023ccs"
2	title: "Discovering Latent Knowledge in Language Models Without Supervision"
3	venue: "ICLR 2023"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Zero-shot prompting"
9	    - "Calibrated zero-shot (contextual calibration)"
10	    - "CRC-TPC (Top Principal Component clustering)"
11	    - "CRC-BSS (Bimodal Salience Search clustering)"
12	    - "Logistic Regression on hidden states (supervised ceiling)"
13	  metrics:
14	    - {name: "Accuracy", direction: "higher_better"}
15	    - {name: "Prompt sensitivity (std across prompts)", direction: "lower_better"}
16	  datasets:
17	    - {name: "IMDB", size: "1000 examples used"}
18	    - {name: "Amazon", size: "1000 examples used"}
19	    - {name: "AG-News", size: "1000 examples used"}
20	    - {name: "DBpedia", size: "1000 examples used"}
21	    - {name: "RTE", size: "1000 examples used"}
22	    - {name: "QNLI", size: "1000 examples used"}
23	    - {name: "COPA", size: "500 examples used"}
24	    - {name: "Story-Cloze", size: "1000 examples used"}
25	    - {name: "BoolQ", size: "1000 examples used"}
26	    - {name: "PIQA", size: "1000 examples used"}
27	  ablation_dimensions:
28	    - "Probe type (linear vs nonlinear)"
29	    - "Number of training samples (k=1,2,4,...,512)"
30	    - "Layer selection (final vs intermediate hidden states)"
31	    - "Transfer across datasets"
32	    - "Normalization strategy"
33	    - "Misleading prefix robustness"
34	    - "Alternative unsupervised methods (PCA/TPC, BSS)"
35	    - "Encoder vs decoder representations (for encoder-decoder models)"
36	  training_recipe:
37	    optimizer: "AdamW"
38	    lr: "0.01"
39	    runs: "10 independent random restarts, select lowest unsupervised loss"
40	    train_test_split: "60/40"
41	    prompts_per_dataset: "8-13 (avg 9)"
42	    hardware: "not explicitly specified"
43	  method_family: "Unsupervised probing of internal representations / Contrast-consistent representation learning"
44	
45	positioning:
46	  core_claim: "Language models encode latent truth-related knowledge in their hidden states that can be extracted without any supervision via logical consistency constraints (negation consistency + confidence), outperforming zero-shot outputs even under adversarial prompting."
47	  key_results: "CCS 71.2% avg accuracy vs calibrated zero-shot 67.2% (+4%); prompt sensitivity halved (3.2% std vs 6.1%); under misleading prefix, zero-shot drops 9.5% while CCS maintains/improves accuracy (82.1% -> 83.8% on UnifiedQA)"
48	  limitations:
49	    - "Requires model to internally represent and evaluate truth of inputs — unclear when this condition holds precisely"
50	    - "Not evaluated on active deception/lying scenarios"
51	    - "Restricted to binary (yes/no) classification"
52	    - "12.5% gap remains to supervised logistic regression ceiling (71.2% vs 83.7%)"
53	    - "Normalization and random restarts add fragility to the pipeline"
54	  relation_to_us: "foundation"
55	
56	narrative:
57	  story_type: "突破局限型"
58	  hook: "Language models don't always output true text — training objectives (imitation learning, RLHF) are fundamentally misaligned with truth. Opens with AI safety framing: 'raises the stakes of AI research and presents new risks.'"
59	  tension: "All existing approaches to truthfulness rely on human supervision (labels or evaluator ratings), but humans themselves can be fooled or make mistakes. This creates a fundamental ceiling on truth extraction. 'If we try to reward model outputs that look true, a model may still learn to output false text if human raters can't evaluate the correctness.'"
60	  key_insight: "Revealed in paragraph 3 of intro: internal model representations may encode truth independently of what the model outputs. The key logical insight is that truth satisfies negation consistency (a statement and its negation have opposite truth values), and this constraint alone — without any labels — is sufficient to recover knowledge. Formalized as two-loss objective: consistency + confidence."
61	  argument_chain: "LMs output untruthful text → existing fixes rely on supervision → supervision is insufficient for hard-to-verify claims → instead look inside the model → truth has logical structure (negation consistency) → exploit this structure unsupervised → CCS finds truth directions in activation space → validates across 6 models / 10 datasets → robust to misleading prompts → transfers across tasks (suggesting genuine truth representation) → initial step toward supervision-free knowledge elicitation"
62	  contribution_framing: "Framed as 4 claims: (1) method description (CCS), (2) quantitative improvement (+4% over zero-shot, half prompt sensitivity), (3) robustness to adversarial prompts, (4) broader significance as 'initial step toward discovering what language models know, distinct from what they say.' Hedged with 'initial step' — presents as proof-of-concept."
63	  intro_structure: "5 paragraphs: P1 — AI safety risk framing (LMs output false text); P2 — why training objectives cause untruthfulness (imitation, reward hacking, evaluator limitations); P3 — proposed solution (bypass outputs, look at internal representations, use logical consistency); P4 — method overview (CCS specifics, contrast pairs, consistency+confidence loss); P5 — results summary and significance framing"
64	  notable_technique: "Uses AI safety/alignment framing to motivate a fundamentally technical contribution (unsupervised probing). The 'misleading prefix' experiment is narratively powerful — demonstrates the method works even when the model is actively prompted to lie, which directly validates the safety motivation from the intro. Also notable: the supervised LR ceiling is presented upfront as 'LR (Ceiling)' rather than hidden, establishing intellectual honesty."
65	
66	figures:
67	  figure_count: 6  # 4 main-body referenced (Figures 1-4), plus Figures 5-6 in appendix; Figure 10 in appendix
68	  figure1:
69	    type: "method_overview"
70	    description: "Left-to-right pipeline diagram showing 5 stages of CCS: (1) construct contrast pairs from yes-no questions, (2) extract internal activations phi(x), (3) map to probabilities via learned projection p_theta, (4) optimize for consistency (p_i+ ≈ 1 - p_i-) and confidence (p_i+ ≉ p_i-), (5) estimate final probability. Right panel shows a bimodal histogram of learned 'Yes' probabilities on COPA/UnifiedQA, colored by true/false labels (blue=True, orange=False), with clear separation."
71	    narrative_role: "Serves as the single method overview figure — reader can grasp the full pipeline from this one image. The histogram on the right provides immediate empirical evidence that the unsupervised method actually works (bimodal separation without labels)."
72	    design_elements:
73	      - "Left-to-right pipeline flow with arrows"
74	      - "Mathematical notation inline (phi, p_theta, consistency/confidence constraints)"
75	      - "Concrete examples ('Is 22+59=237? Yes/No', 'Are cats mammals?')"
76	      - "Blue/orange color coding for Yes/No and True/False"
77	      - "Bimodal histogram as proof-of-concept visualization"
78	      - "Bottom row of text captions explaining each pipeline stage"
79	    visual_style: "Clean black-on-white pipeline diagram. Rounded rectangle boxes for text/math. Two-color scheme (blue for positive/true, orange for negative/false). Right panel uses standard matplotlib histogram style with fitted curve overlay. Minimal, information-dense layout."
80	  result_figures:
81	    - figure_id: "Figure 2"
82	      viz_type: "heatmap"
83	      what_compared: "Transfer accuracy of CCS across 10 datasets for 3 models (UnifiedQA, T0, DeBERTa). Rows = training dataset, columns = test dataset. Bottom row = no-transfer baseline."
84	      how_gain_highlighted: "Color intensity (yellow-green = high, dark blue = low). The overall pattern of mostly high values (70s-90s) across off-diagonal cells demonstrates successful transfer. Bottom 'No Transfer' row provides within-dataset reference."
85	      design_note: "Three side-by-side heatmaps allow model comparison at a glance. Numeric values printed in each cell provide exact numbers. Dark background with light-colored number annotations. Effective for showing that cross-dataset transfer is broadly successful rather than cherry-picked."
86	    - figure_id: "Figure 4"
87	      viz_type: "scatter"
88	      what_compared: "CCS accuracy vs zero-shot accuracy under misleading prefix condition (UnifiedQA). Each point = one dataset × one prompt combination. y=x line as reference."
89	      how_gain_highlighted: "Points above y=x line indicate CCS superiority. Separate blue (CCS) and orange (zero-shot) point clouds with fitted regression lines show CCS maintaining high accuracy while zero-shot degrades."
90	      design_note: "Scatter plot with fitted regression lines and y=x reference line effectively shows the distribution of per-dataset-per-prompt effects rather than just averages. Light confidence bands around regression lines."
91	  ablation_figures:
92	    - figure_id: "Figure 3"
93	      viz_type: "line_plot"
94	      dimensions_varied: ["Number of training samples (k=1 to 512)", "Model (UQA, T0, DeBERTa)"]
95	      design_note: "Three colored lines (red=UQA, green=T0, blue=DeBERTa) on log-scale x-axis. Shows diminishing returns — most gain happens by k=8-16. UQA starts lowest at k=1 but climbs highest, suggesting different models have different sample efficiency profiles. Clean, minimal style with square markers."
96	    - figure_id: "Figure 10 (Appendix F)"
97	      viz_type: "line_plot"
98	      dimensions_varied: ["Hidden layer index", "Model (T5, UnifiedQA)"]
99	      design_note: "Shows intermediate layers outperform final layers for encoder-decoder models — a key finding that CCS is not simply recovering output-level information."
100	  figure_narrative_role: "Figure 1 (method overview + proof-of-concept histogram) → Figure 2 (transfer heatmaps proving task-agnostic truth) → Figure 3 (sample complexity showing truth is salient) → Figure 4 (robustness to adversarial prompting, the safety payoff). Flow: understand method → see it works → see it generalizes → see it's robust. Appendix figures (5-6, 10) provide supporting details."
101	
102	tables:
103	  table_count: 3  # 2 main body + 1 appendix (Table 3)
104	  main_result_table:
105	    table_id: "Table 1"
106	    row_axis: "methods"
107	    col_axis: "models"
108	    row_organization: "by_category"  # grouped as: zero-shot baselines, CCS variants, supervised ceiling
109	    col_organization: "flat"  # 6 individual models + Mean column
110	    highlight_strategy: "No explicit bold/underline — relies on reader comparing numbers. Supervised LR labeled as 'Ceiling' to set expectations. Parenthetical std values show prompt sensitivity reduction."
111	    statistical_reporting: "mean accuracy across prompts and datasets, with standard deviation of accuracy across prompts in parentheses"
112	    num_baselines: 4  # 0-shot, calibrated 0-shot, CRC-TPC, CRC-BSS (Table 2), plus LR ceiling
113	    design_note: "Compact 5×7 table. Notably includes 'CCS (All Data)' variant using full dataset. The std in parentheses serves double duty — both showing variance and supporting the 'halves prompt sensitivity' claim. LR ceiling row establishes upper bound, framing the 12.5% gap as future work rather than weakness. Six diverse models (RoBERTa, DeBERTa, GPT-J, T5, UnifiedQA, T0) spanning encoder-only, encoder-decoder, decoder-only architectures."
114	  ablation_tables:
115	    - table_id: "Table 2"
116	      what_varied: ["Unsupervised method: CCS vs CRC-TPC vs CRC-BSS"]
117	      variation_style: "full_numbers"
118	      design_note: "Same format as Table 1, directly comparable. Shows CCS is best but simpler PCA-based methods are surprisingly competitive (70.1-70.2% vs 71.2%), supporting the claim that truth is a salient/high-variance feature in activation space."
119	    - table_id: "Table 3 (Appendix B)"
120	      what_varied: ["Prefix condition (regular vs misleading)", "Method (calibrated zero-shot vs CCS)"]
121	      variation_style: "full_numbers"
122	      design_note: "Extends Table 1 with prefix condition dimension. Key comparison: CCS regular 71.2% vs CCS prefix 71.2% (unchanged), while calibrated zero-shot drops from 67.2% to 65.4%. Demonstrates robustness numerically."
123	  supplementary_tables:
124	    in_appendix: true
125	    content: "Table 3 shows full results with misleading prefix conditions across all models. Additional per-dataset breakdowns, statistical significance tests (Appendix H), and dataset setup details (Appendix I) are in appendix."
126	    reason: "Main body keeps Tables 1-2 for core results and method comparison. Appendix houses the misleading prefix full results (more detailed version of the scatter plot in Figure 4) and statistical rigor details that would interrupt the narrative flow."
127	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79d5378a-57d6-4277-84cd-51153d0664c1",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "0dd26feb-b6cc-4b0d-a62d-3c3310c81e3d",
  "sourceToolAssistantUUID": "79d5378a-57d6-4277-84cd-51153d0664c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T17:44:17.254Z_

<details open><summary>🔧 Tool call — Read · `toolu_0175Jy23g6EseLU4t5jLZZ87`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/casper2023openproblems.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dd26feb-b6cc-4b0d-a62d-3c3310c81e3d",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d58e6680-fef7-4543-b606-e024cf201931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-24T17:44:17.263Z_

<details><summary>↩ Tool result · `toolu_0175Jy23g6EseLU4t5jLZZ87`</summary>

```text
1	paper_key: "casper2023openproblems"
2	title: "Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback"
3	venue: "arXiv 2023 (2307.15217)"
4	full_text_available: false
5	
6	research:
7	  baselines:
8	    - "standard RLHF pipeline"
9	    - "reward modeling approaches"
10	    - "preference-based optimization (DPO, etc.)"
11	  metrics:
12	    - {name: "alignment quality", direction: "higher_better"}
13	    - {name: "reward hacking susceptibility", direction: "lower_better"}
14	    - {name: "human preference accuracy", direction: "higher_better"}
15	  datasets:
16	    - {name: "survey of existing RLHF benchmarks", size: "N/A"}
17	  ablation_dimensions:
18	    - "feedback quality and reliability"
19	    - "reward model accuracy vs robustness"
20	    - "policy optimization pitfalls"
21	    - "evaluation and auditing standards"
22	  training_recipe:
23	    optimizer: "N/A (survey paper)"
24	    lr: "N/A"
25	    hardware: "N/A"
26	  method_family: "RLHF / alignment survey"
27	
28	positioning:
29	  core_claim: "RLHF has fundamental limitations across its entire pipeline (feedback collection, reward modeling, policy optimization) that necessitate a multi-faceted approach combining complementary techniques for safer AI systems."
30	  key_results: "Comprehensive taxonomy of RLHF failure modes; proposes auditing and disclosure standards for societal oversight"
31	  limitations:
32	    - "Survey scope bounded by literature available at time of writing"
33	    - "Some identified problems may be partially addressed by newer methods"
34	    - "Proposed standards lack empirical validation"
35	  relation_to_us: "foundation"
36	
37	narrative: N/A
38	figures: N/A
39	tables: N/A
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d58e6680-fef7-4543-b606-e024cf201931",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "a2078273-be1b-499f-acc5-27ca6651a405",
  "sourceToolAssistantUUID": "d58e6680-fef7-4543-b606-e024cf201931",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T17:44:17.726Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UJbB79MeSFp1nF58MiTp8c`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/consistency2025bctact.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2078273-be1b-499f-acc5-27ca6651a405",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b1131006-2a27-4be4-9631-d13e5f4dc6e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T17:44:17.732Z_

<details><summary>↩ Tool result · `toolu_01UJbB79MeSFp1nF58MiTp8c`</summary>

```text
1	paper_key: "consistency2025bctact"
2	title: "Consistency Training Helps Stop Sycophancy and Jailbreaks"
3	venue: "arXiv 2025"
4	full_text_available: false
5	
6	research:
7	  baselines:
8	    - "standard RLHF model (no consistency training)"
9	    - "BCT (Bias-augmented Consistency Training, from Chua et al. 2025)"
10	  metrics:
11	    - {name: "sycophancy rate", direction: "lower_better"}
12	    - {name: "jailbreak success rate", direction: "lower_better"}
13	    - {name: "task performance preservation", direction: "higher_better"}
14	  datasets:
15	    - {name: "sycophancy evaluation tasks", size: "N/A"}
16	    - {name: "jailbreak evaluation prompts", size: "N/A"}
17	  ablation_dimensions:
18	    - "BCT (output-level invariance) vs ACT (activation-level invariance)"
19	    - "sycophancy reduction vs jailbreak reduction"
20	  training_recipe:
21	    optimizer: "N/A"
22	    lr: "N/A"
23	    hardware: "N/A"
24	    model: "Gemini 2.5 Flash"
25	  method_family: "consistency training / self-supervised alignment"
26	
27	positioning:
28	  core_claim: "Self-supervised consistency training (BCT over outputs, ACT over activations) teaches LLMs to be invariant to irrelevant prompt cues, reducing sycophancy and jailbreaks without static adversarial datasets."
29	  key_results: "BCT and ACT reduce sycophancy equally well; BCT does better at jailbreak reduction"
30	  limitations:
31	    - "Evaluated only on Gemini 2.5 Flash"
32	    - "No explicit comparison with activation steering or contrastive methods"
33	    - "Unclear generalization to open-source models"
34	  relation_to_us: "complementary"
35	
36	narrative: N/A
37	figures: N/A
38	tables: N/A
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1131006-2a27-4be4-9631-d13e5f4dc6e3",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "d437e351-bd6b-48b1-8fcb-953014d23fce",
  "sourceToolAssistantUUID": "b1131006-2a27-4be4-9631-d13e5f4dc6e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T17:44:18.190Z_

<details open><summary>🔧 Tool call — Read · `toolu_013GSFGGagC4Emorvpd4j587`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/denison2024subterfuge.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d437e351-bd6b-48b1-8fcb-953014d23fce",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "434c77d3-6560-4438-89dd-822f405ee6ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T17:44:18.196Z_

<details><summary>↩ Tool result · `toolu_013GSFGGagC4Emorvpd4j587`</summary>

```text
1	paper_key: "denison2024subterfuge"
2	title: "Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models"
3	venue: "arXiv 2024"
4	full_text_available: false
5	
6	research:
7	  baselines:
8	    - LLM assistants without curriculum training
9	    - LLM assistants with harmlessness training
10	    - LLM assistants retrained not to game early-curriculum environments
11	  metrics:
12	    - {name: "Specification gaming rate", direction: "lower_better"}
13	    - {name: "Reward-tampering frequency", direction: "lower_better"}
14	    - {name: "Zero-shot generalization to reward rewriting", direction: "lower_better"}
15	  datasets:
16	    - {name: "Curriculum of gameable environments", size: "increasingly sophisticated"}
17	  ablation_dimensions:
18	    - curriculum stage (early vs full)
19	    - harmlessness training (with vs without)
20	    - retraining to prevent early-stage gaming
21	    - environment sophistication level
22	  training_recipe:
23	    optimizer: "not specified"
24	    lr: "not specified"
25	    hardware: "not specified"
26	    training_approach: "curriculum of increasingly sophisticated gameable environments"
27	  method_family: "specification gaming / reward hacking analysis"
28	
29	positioning:
30	  core_claim: "LLMs trained on a curriculum of gameable environments generalize from simple specification gaming (sycophancy) to directly rewriting their own reward function, and this behavior is nontrivial to remove even with harmlessness training or retraining."
31	  key_results: "Small but non-negligible proportion of LLMs generalize zero-shot to reward-tampering; retraining mitigates but does not eliminate the behavior; harmlessness training does not prevent it."
32	  limitations:
33	    - "Reward-tampering occurs only a small proportion of the time"
34	    - "Constructed curriculum may not reflect naturalistic training"
35	    - "Mitigation strategies tested are limited"
36	  relation_to_us: "complementary"
37	
38	narrative: N/A
39	figures: N/A
40	tables: N/A
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "434c77d3-6560-4438-89dd-822f405ee6ee",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "00dc80a0-b176-43ab-9eb6-1e802eb0d24a",
  "sourceToolAssistantUUID": "434c77d3-6560-4438-89dd-822f405ee6ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T17:44:18.660Z_

<details open><summary>🔧 Tool call — Read · `toolu_019b1D3bwHg2GUqQFXTtdjCw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/gao2023scaling.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00dc80a0-b176-43ab-9eb6-1e802eb0d24a",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "25268d5d-123a-4ec9-a71d-e9ef54c072de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-24T17:44:18.670Z_

<details><summary>↩ Tool result · `toolu_019b1D3bwHg2GUqQFXTtdjCw`</summary>

```text
1	paper_key: "gao2023scaling"
2	title: "Scaling Laws for Reward Model Overoptimization"
3	venue: "ICML 2023"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Best-of-n sampling (BoN) with varying n"
9	    - "PPO-based reinforcement learning (RL)"
10	    - "Proxy reward models of varying sizes (3M to 3B parameters)"
11	    - "Gold-standard reward model (6B, from InstructGPT)"
12	  metrics:
13	    - {name: "Gold RM score (ground truth reward)", direction: "higher_better"}
14	    - {name: "Proxy RM score", direction: "higher_better"}
15	    - {name: "KL divergence from initial policy", direction: "lower_better"}
16	    - {name: "RM validation loss (cross-entropy)", direction: "lower_better"}
17	    - {name: "Peak gold RM score", direction: "higher_better"}
18	    - {name: "sqrt(KL) at peak gold score (d*)", direction: "context_dependent"}
19	  datasets:
20	    - {name: "Synthetic comparisons from InstructGPT environment", size: "100,000 comparisons (90k train / 10k validation)"}
21	    - {name: "InstructGPT prompts (broad natural language instructions)", size: "not explicitly stated, same as Ouyang et al. 2022"}
22	  ablation_dimensions:
23	    - "Reward model parameter count (3M, 12M, 25M, 42M, 85M, 300M, 680M, 1.2B, 3B)"
24	    - "RM training data size (120 to 90,000 comparisons)"
25	    - "Policy parameter count (1.2B vs 6B)"
26	    - "KL penalty coefficient (0.0, 0.01, 0.05, 0.1, 0.5)"
27	    - "Optimization method (BoN vs RL)"
28	  training_recipe:
29	    optimizer: "Adam"
30	    lr: "1.67e-2 (RM), 4e-3 (RL)"
31	    hardware: "Not explicitly stated; uses GPT-3 series models (OpenAI internal infrastructure)"
32	    rl_algorithm: "PPO (Proximal Policy Optimization)"
33	    rl_batch_size: 256
34	    rl_ppo_clip: 0.2
35	    rl_timesteps_per_rollout: 256
36	    rl_minibatches_per_epoch: 128
37	    rl_gae_lambda: 0.95
38	    rm_batch_size: 64
39	    initial_policy: "GPT-3 series models fine-tuned with SFT on InstructGPT demonstrations for 2 epochs"
40	    bon_max_n: "up to 60,000 (validated functional form hypothesized at n=1000)"
41	  method_family: "Scaling laws / empirical analysis of RLHF overoptimization"
42	
43	positioning:
44	  core_claim: "Reward model overoptimization follows predictable functional forms -- quadratic for BoN and logarithmic for RL -- whose coefficients scale smoothly with RM size, enabling quantitative prediction of when and how much Goodhart's law degrades true performance during RLHF."
45	  key_results: "BoN gold score follows R_BoN(d) = d(alpha - beta*d); RL follows R_RL(d) = d(alpha - beta*log(d)); coefficients scale smoothly (approx. logarithmically) with RM parameter count; larger RMs yield higher peak gold scores and less overoptimization (beta decreases); policy size has weak effect on overoptimization magnitude; KL penalty is equivalent to early stopping with no improvement on KL-gold frontier."
46	  limitations:
47	    - "Synthetic setup using gold RM instead of real human labels -- may not transfer to real-world settings"
48	    - "All experiments use InstructGPT environment only -- generalization to other domains unvalidated"
49	    - "Does not capture overoptimization from mismatch between ground truth labels and actual human intent"
50	    - "Models not powerful enough to exhibit adversarial Goodhart effects"
51	    - "Policy size scaling limited to only two sizes (1.2B and 6B)"
52	    - "KL penalty result could be sensitive to hyperparameters"
53	    - "Proxy RM score functional form harder to model than gold RM score"
54	    - "Multi-iteration RLHF implications based on simplifying assumptions not empirically validated"
55	  relation_to_us: "complementary"
56	
57	narrative:
58	  story_type: "突破局限型"
59	  hook: "Opens with Goodhart's law as a universal adage ('When a measure becomes a target, it ceases to be a good measure'), immediately connecting a well-known social science principle to the ML proxy optimization problem."
60	  tension: "Overoptimization has been 'frequently observed, but not carefully measured due to the expense of collecting human preference data.' The inability to quantify Goodhart's law in RLHF blocks both practical safe deployment and theoretical understanding of alignment."
61	  key_insight: "The synthetic gold-RM setup decouples the measurement problem from human labeling cost, enabling systematic scaling law analysis. The key discovery is that overoptimization is not chaotic but follows clean, predictable functional forms with smoothly scaling coefficients -- making it forecastable."
62	  argument_chain: "Goodhart's law is important but unmeasured in RLHF -> human labels too expensive for systematic study -> synthetic gold-RM setup enables controlled measurement -> discover distinct functional forms for BoN (quadratic decay) and RL (logarithmic decay) -> coefficients scale smoothly with RM parameters -> ablate data size, policy size, KL penalty -> connect to Goodhart taxonomy (regressional/extremal/causal/adversarial) -> derive implications for iterated RLHF and alignment theory"
63	  contribution_framing: "Four bullet-pointed findings at end of intro: (1) RL vs BoN differences, (2) smooth coefficient scaling, (3) weak policy size dependence, (4) KL penalty ineffectiveness. Framed as empirically validated scaling laws with alignment implications, not just measurements."
64	  intro_structure: "6 paragraphs: P1 = Goodhart's law motivation and importance; P2 = RLHF context and optimization methods; P3 = challenge of human label expense and synthetic solution; P4 = main results (functional forms with equations); P5 = four bullet-pointed additional findings; P6 = forward pointer to discussion implications."
65	  notable_technique: "Placing the two functional form equations (R_BoN and R_RL) directly in the introduction with their mathematical forms creates immediate concreteness and testability. The paper front-loads its core empirical result rather than burying it in results section, giving readers the 'punchline' early and making subsequent sections feel like validation rather than discovery."
66	
67	figures:
68	  figure_count: 26
69	  figure1:
70	    type: "teaser_result"
71	    description: "Two-panel plot (BoN top, RL bottom) showing gold RM score vs sqrt(KL) for 9 different proxy RM sizes (3M to 3B). Each panel shows proxy scores (dashed), gold scores (solid), and fitted curves (thin solid). Demonstrates the characteristic rise-then-fall overoptimization pattern, with larger RMs achieving higher peaks and declining less steeply."
72	    narrative_role: "Serves as the central empirical result -- readers see the overoptimization phenomenon and the scaling law fits in one glance. Establishes visual credibility of the functional forms before formal description."
73	    design_elements:
74	      - "Dual-panel layout separating BoN and RL for direct comparison"
75	      - "Color gradient from dark (small RM) to bright (large RM) for intuitive size ordering"
76	      - "Dashed vs solid lines to distinguish proxy and gold scores"
77	      - "Thin fitted curves overlaid on empirical data to show model quality"
78	      - "Square-root x-axis scale for visual clarity"
79	      - "9 RM sizes creating a dense scaling sweep"
80	    visual_style: "Clean matplotlib aesthetic with muted-to-bright sequential colormap (purple to yellow/green). Legends organized by RM Size and RM Type. Grid-free with axis labels. Two vertically stacked panels with different x-axis ranges (0-10 for BoN, 0-100 for RL) reflecting the KL efficiency difference."
81	  result_figures:
82	    - figure_id: "Figure 1"
83	      viz_type: "line_plot"
84	      what_compared: "Gold and proxy RM scores across 9 RM sizes for both BoN and RL optimization methods"
85	      how_gain_highlighted: "Fitted curves (thin lines) closely track empirical data, visually demonstrating scaling law accuracy. Larger RM sizes clearly achieve higher peaks."
86	      design_note: "The rise-then-fall shape is the paper's visual signature -- every reader immediately grasps overoptimization from this plot."
87	    - figure_id: "Figure 3"
88	      viz_type: "scatter_with_trend"
89	      what_compared: "Scaling law coefficients (alpha_BoN, beta_BoN, beta_RL) vs RM parameter count, for both proxy and gold rewards"
90	      how_gain_highlighted: "Log-scale x-axis with approximately linear trends demonstrates smooth scaling. Dashed vs solid lines separate proxy and gold coefficients."
91	      design_note: "Three sub-panels (a, b, c) isolate each coefficient, making the logarithmic scaling relationship visually obvious. This is the 'scaling law of the scaling law.'"
92	    - figure_id: "Figure 4"
93	      viz_type: "line_plot"
94	      what_compared: "Gold and proxy RM scores across different RM training data sizes (120 to 90,000)"
95	      how_gain_highlighted: "Color-coded lines show clear ordering: more data = higher peak gold score and less overoptimization"
96	      design_note: "Same visual format as Figure 1 but sweeping data size instead of model size, maintaining visual consistency across ablations."
97	    - figure_id: "Figure 8"
98	      viz_type: "scatter_plot"
99	      what_compared: "Proxy RM score vs gold RM score for both BoN and RL across all RM sizes"
100	      how_gain_highlighted: "Reveals that RL and BoN look more similar when indexed by proxy score rather than KL, challenging the KL-as-optimization-measure assumption"
101	      design_note: "Elegant reframing of the data -- same experiments plotted on a different axis to reveal a hidden regularity."
102	    - figure_id: "Figure 5"
103	      viz_type: "scatter_plot"
104	      what_compared: "RM validation loss vs BoN gold RM score at n=1000 across all RM sizes"
105	      how_gain_highlighted: "Clear negative correlation suggests validation loss predicts downstream optimization performance"
106	      design_note: "Points color-coded by RM size. Tests the hypothesis that validation loss is a sufficient statistic for optimization robustness."
107	    - figure_id: "Figure 9"
108	      viz_type: "line_plot"
109	      what_compared: "Effect of different KL penalty coefficients (0.0, 0.01, 0.05, 0.1, 0.5) on RL gold and proxy scores"
110	      how_gain_highlighted: "Shows KL penalty merely acts as early stopping -- all curves follow the same KL-gold frontier"
111	      design_note: "Powerful negative result visualized clearly: despite different KL penalties, gold score curves collapse onto the same trajectory."
112	  ablation_figures:
113	    - figure_id: "Figure 4"
114	      viz_type: "line_plot"
115	      dimensions_varied: ["RM training data size (120 to 90,000)"]
116	      design_note: "Dual-panel (BoN, RL) with color-coded data sizes. Shows diminishing returns and a critical threshold around 2,000 comparisons below which RMs barely exceed chance."
117	    - figure_id: "Figure 6"
118	      viz_type: "line_plot"
119	      dimensions_varied: ["RM data size", "RM parameter count"]
120	      design_note: "RM validation losses broken down by both data size and model size, showing that performance depends on the combination of both."
121	    - figure_id: "Figure 7"
122	      viz_type: "line_plot"
123	      dimensions_varied: ["Policy parameter count (1.2B vs 6B)"]
124	      design_note: "Dual-panel showing BoN and RL. Asterisks mark peak gold scores in RL plot. Demonstrates larger policies benefit less from optimization but don't overoptimize more."
125	    - figure_id: "Figure 9"
126	      viz_type: "line_plot"
127	      dimensions_varied: ["KL penalty coefficient (0.0, 0.01, 0.05, 0.1, 0.5)"]
128	      design_note: "Shows all KL penalty settings trace the same gold-KL frontier, establishing KL penalty as equivalent to early stopping."
129	    - figure_id: "Figure 10"
130	      viz_type: "heatmap"
131	      dimensions_varied: ["RM size (3M to 3B)", "Data size (120 to 90,000)"]
132	      design_note: "Appendix heatmap of max gold scores across full RM size x data size grid. Contour lines overlay discrete cells for readability."
133	  figure_narrative_role: "Figure 1 (main result: overoptimization curves and fits) -> Figure 2 (methodology: synthetic setup diagram) -> Figure 3 (scaling: coefficient trends) -> Figure 4 (ablation: data size effect) -> Figure 5 (analysis: validation loss as predictor) -> Figure 6 (analysis: RM losses breakdown) -> Figure 7 (ablation: policy size effect) -> Figure 8 (insight: proxy-vs-gold reframing) -> Figure 9 (ablation: KL penalty effect). Flow: result first, then methodology, then systematic ablations, then deeper analysis."
134	
135	tables:
136	  table_count: 2
137	  main_result_table:
138	    table_id: "Table 1"
139	    row_axis: "hyperparameters"
140	    col_axis: "values"
141	    row_organization: "by_category"
142	    col_organization: "flat"
143	    highlight_strategy: "none (simple listing)"
144	    statistical_reporting: "single values (no variance reported for hyperparameters)"
145	    num_baselines: 0
146	    design_note: "Not a result comparison table -- this is a hyperparameter reference table. The paper is unusual in having no traditional baseline comparison table because it is an empirical scaling law study, not a method-vs-method benchmark. All results are presented as figures (curves and fits), not tables."
147	  ablation_tables:
148	    - table_id: "Table 2"
149	      what_varied: ["best-of-n sample count (n=1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000)"]
150	      variation_style: "full_numbers"
151	      design_note: "Qualitative illustration table showing actual generated text samples for one question across different n values. Includes proxy and gold scores per sample. Demonstrates that per-question gold scores are noisy even as averages follow clean trends. Serves a narrative/illustrative purpose rather than systematic comparison."
152	  supplementary_tables:
153	    in_appendix: true
154	    content: "Table 1 (hyperparameters) is in Appendix C. Table 2 (sample BoN answers) is in the appendix. The appendix also contains 17 additional figures (Figures 10-26) covering: RM size x data size heatmaps, validation losses, coefficient scaling across data sizes, additional BoN/RL curves for different RM sizes, KL growth over RL steps, policy size comparisons, proxy-gold gaps, and extrapolation tests."
155	    reason: "Main paper focuses on key scaling law results and ablation trends via figures. Detailed supplementary figures cover all parameter combinations and edge cases, keeping main text focused on the core narrative. No supplementary result tables because this is fundamentally a curve-fitting paper where figures are the natural result format."
156	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25268d5d-123a-4ec9-a71d-e9ef54c072de",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "4ac37651-971f-4d56-bf3b-0589391daa23",
  "sourceToolAssistantUUID": "25268d5d-123a-4ec9-a71d-e9ef54c072de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T17:44:19.604Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FsrbxUvR4wALqhy5HnnMEe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/li2023iti.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ac37651-971f-4d56-bf3b-0589391daa23",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2ca71f3e-6ac1-4674-8779-6fd48a314b0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-24T17:44:19.610Z_

<details><summary>↩ Tool result · `toolu_01FsrbxUvR4wALqhy5HnnMEe`</summary>

```text
1	paper_key: "li2023iti"
2	title: "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model"
3	venue: "NeurIPS 2023"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "LLaMA-7B (vanilla greedy decoding)"
9	    - "Supervised Fine-tuning (SFT, Ouyang et al. 2022)"
10	    - "Few-shot Prompting (FSP, 50-shot, Bai et al. 2022a)"
11	    - "Alpaca (instruction-finetuned LLaMA)"
12	    - "Vicuna (instruction-finetuned LLaMA)"
13	    - "Contrast-Consistent Search (CCS, Burns et al. 2022)"
14	    - "Probe Weight Direction"
15	    - "Random Direction"
16	  metrics:
17	    - {name: "True*Informative (%)", direction: "higher_better"}
18	    - {name: "Truthful (%)", direction: "higher_better"}
19	    - {name: "MC Accuracy (%)", direction: "higher_better"}
20	    - {name: "Cross-Entropy (CE)", direction: "lower_better"}
21	    - {name: "KL Divergence", direction: "lower_better"}
22	  datasets:
23	    - {name: "TruthfulQA", size: "817 questions, 38 categories"}
24	    - {name: "Natural Questions", size: "OOD generalization test"}
25	    - {name: "TriviaQA", size: "OOD generalization test"}
26	    - {name: "MMLU", size: "OOD generalization test"}
27	  ablation_dimensions:
28	    - "Intervention strength alpha (1-25)"
29	    - "Number of intervened attention heads K (1-96)"
30	    - "Training set size (percentage of TruthfulQA)"
31	    - "Intervention direction (mass mean shift vs probe weight vs CCS vs random)"
32	    - "Head selection method (none vs point-wise vs head-wise)"
33	  training_recipe:
34	    optimizer: "Not specified (logistic regression probes; no heavy training)"
35	    lr: "Not specified"
36	    hardware: "Not specified (paper emphasizes near-zero computational overhead)"
37	    probe_training: "Binary logistic classifiers with sigmoid activation, 4:1 train-val split"
38	    cross_validation: "2-fold cross-validation for main results"
39	    training_data: "5-10% of TruthfulQA (approx 40-80 questions) sufficient"
40	  method_family: "Activation engineering / inference-time steering"
41	
42	positioning:
43	  core_claim: "LLMs internally encode truthful knowledge that standard decoding fails to elicit; a lightweight inference-time activation shift along truthful directions identified by linear probes can close this generation-discrimination gap without retraining."
44	  key_results: "LLaMA-7B: 30.5% -> 42.3% true*informative; Alpaca: 32.5% -> 65.1%; Vicuna: 51.5% -> 74.0%; OOD generalization on NQ (+4.7%), TriviaQA (+1.5%), MMLU (+4.45%); probe accuracy 83.3% vs generation accuracy 31.6% revealing a 40% latent truthfulness gap."
45	  limitations:
46	    - "ITI alone is insufficient for ensuring truthful outputs; it is one piece of a comprehensive approach"
47	    - "Trade-off between truthfulness and helpfulness -- higher intervention strength increases no comment responses"
48	    - "Directions trained on TruthfulQA show only modest OOD transfer"
49	    - "Lacks mechanistic understanding of why certain heads encode truthfulness"
50	    - "No exploration of unsupervised direction discovery at scale"
51	  relation_to_us: "foundation"
52	
53	narrative:
54	  story_type: "突破局限型"
55	  hook: "Opens with the observation that LLMs generate text that seems correct but often only at first glance, establishing the real-world stakes of hallucination and inaccuracy."
56	  tension: "Models internally know correct answers (probe accuracy 83.3%) but standard generation fails to surface them (generation accuracy 31.6%), creating a dramatic 40% gap. Existing solutions (SFT, RLHF) require expensive retraining and do not directly address this internal knowledge gap."
57	  key_insight: "Revealed in Section 3.2 via the probe accuracy heatmap (Figure 2A): a significant proportion of attention heads display strong truthfulness signal, with the best head (layer 14, head 18) reaching 83.3% accuracy. This motivates targeted, sparse intervention rather than full model modification."
58	  argument_chain: "LLMs hallucinate despite internal knowledge -> linear probes reveal truthful representations in specific attention heads -> a 40% gap exists between probing accuracy and generation accuracy -> inference-time activation shifting along truthful directions closes this gap -> ITI achieves SOTA truthfulness with near-zero compute overhead -> validated across models (LLaMA/Alpaca/Vicuna) and generalizes OOD"
59	  contribution_framing: "Two contributions framed modestly: (1) a minimally-invasive control method to close the knowing-telling gap, (2) evidence that pretraining endows models with an internal world model of real-world truths. Deliberately undersells by acknowledging ITI is not sufficient alone."
60	  intro_structure: "4-5 paragraphs: P1 problem statement (hallucination stakes), P2 evidence of latent knowledge (citing knowledge graphs, self-evaluation), P3 operationalization (TruthfulQA as testbed, generation-discrimination gap quantified), P4 proposed solution (ITI overview), P5 contribution summary and honest limitation acknowledgment."
61	  notable_technique: "The 40% gap quantification is a powerful rhetorical device -- it transforms an abstract claim (models know more than they say) into a concrete, memorable number that motivates the entire method. The honest limitation acknowledgment in the intro builds credibility."
62	
63	figures:
64	  figure_count: 6
65	  figure1:
66	    type: "teaser_result"
67	    description: "Side-by-side comparison of LLaMA responses without ITI (red) and with ITI (blue) on two example questions, showing concrete qualitative improvement in truthfulness."
68	    narrative_role: "Immediate visual hook in intro -- demonstrates the problem and solution simultaneously before any technical detail. Builds intuition for what ITI does."
69	    design_elements: ["Red/blue color contrast for before/after", "Concrete Q&A examples", "Gold standard answers shown for reference", "Two diverse examples covering different error types"]
70	    visual_style: "Text-based comparison layout with colored highlighting; minimal, clean, focuses on readability of the generated text rather than quantitative data."
71	  result_figures:
72	    - figure_id: "Figure 4"
73	      viz_type: "line_plot"
74	      what_compared: "Performance metrics (true*informative, true%, MC accuracy, CE, KL) across varying intervention strength (alpha) and number of heads (K)"
75	      how_gain_highlighted: "Shows inverted-U curve for true*informative, making the sweet spot of intervention strength visually apparent; multiple metrics on shared x-axis reveal trade-offs"
76	      design_note: "Multi-panel line plots with error bands (5 random seeds averaged) effectively communicate hyperparameter sensitivity and the fundamental truthfulness-helpfulness trade-off."
77	    - figure_id: "Figure 5"
78	      viz_type: "horizontal_bar_chart"
79	      what_compared: "Baseline vs ITI performance across TruthfulQA subcategories"
80	      how_gain_highlighted: "Sorted by performance difference, making it immediately visible that ITI improves most categories; horizontal layout accommodates long category names"
81	      design_note: "Subcategory breakdown prevents the argument that gains come from a single easy category; filtering out <10 question categories avoids noise."
82	  ablation_figures:
83	    - figure_id: "Figure 6"
84	      viz_type: "dual_panel_line_plot"
85	      dimensions_varied: ["Training set size (panel A)", "Intervention strength alpha (panel B)"]
86	      design_note: "Panel A shows early plateau of truthfulness with increasing data, arguing the method is data-efficient. Panel B explicitly visualizes the truthfulness-informativeness trade-off as two crossing curves, making the fundamental tension tangible."
87	    - figure_id: "Figure 2"
88	      viz_type: "heatmap_plus_kde"
89	      dimensions_varied: ["Layer index", "Attention head index", "Truthful vs false activation distributions"]
90	      design_note: "Panel A (heatmap) is the key evidence figure -- layer x head grid with probe accuracy as color intensity reveals sparsity of truthful heads. Panel B (KDE) shows clean separation of truthful vs false activations, validating the linear probing approach. This figure carries the core scientific argument."
91	  figure_narrative_role: "Figure 1 (teaser example) -> Figure 2 (scientific evidence for latent truthfulness) -> Figure 3 (method diagram) -> Figure 4 (main quantitative results across hyperparameters) -> Figure 5 (subcategory analysis) -> Figure 6 (ablation and trade-off analysis). Classic progression: hook -> evidence -> method -> results -> analysis -> deeper understanding."
92	
93	tables:
94	  table_count: 5
95	  main_result_table:
96	    table_id: "Table 1"
97	    row_axis: "methods"
98	    col_axis: "metrics (True*Info%, True%, MC Acc%, CE, KL)"
99	    row_organization: "by_category"
100	    col_organization: "flat"
101	    highlight_strategy: "Best results implied by numerical comparison; standard NeurIPS formatting likely bolds best"
102	    statistical_reporting: "5 random seeds averaged; 5% of TruthfulQA used for training"
103	    num_baselines: 4
104	    design_note: "Compact table with 5 metrics including CE and KL divergence as cost metrics alongside performance, showing ITI advantage in being minimally disruptive to the base model. Rows organized as: baseline methods alone, then baseline+ITI combinations."
105	  ablation_tables:
106	    - table_id: "Table 3"
107	      what_varied: ["Intervention direction type (random, CCS, probe weight, mass mean shift)", "Optimal alpha per direction"]
108	      variation_style: "full_numbers"
109	      design_note: "Each direction type shown with its own optimal alpha, enabling fair comparison. Mass mean shift clearly dominates, validating the design choice."
110	    - table_id: "Table 5"
111	      what_varied: ["Head selection method (none, point-wise, head-wise)", "Optimal alpha per method"]
112	      variation_style: "full_numbers"
113	      design_note: "Demonstrates that sparsifying intervention via head-wise selection is better than no selection or point-wise selection, justifying the probe-guided head selection strategy."
114	  supplementary_tables:
115	    in_appendix: true
116	    content: "Table 2 (instruction-finetuned model results with Alpaca/Vicuna) and Table 4 (OOD generalization results on NQ/TriviaQA/MMLU) serve as supplementary validation beyond the core Table 1 results"
117	    reason: "Tables 2 and 4 demonstrate generalization along two orthogonal axes (model variants and dataset transfer) while keeping the main narrative focused on the core LLaMA-7B/TruthfulQA results in Table 1. Table 2 shows the largest absolute gains (Alpaca +32.6%, Vicuna +22.5%) and may be the most impactful result."
118	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ca71f3e-6ac1-4674-8779-6fd48a314b0f",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "09a163ad-012b-488e-b6fe-d47bf6d3f50b",
  "sourceToolAssistantUUID": "2ca71f3e-6ac1-4674-8779-6fd48a314b0f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T17:44:20.076Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B2MvSYW19xpEBEMy1SUwrA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/mckinney2023fragility.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09a163ad-012b-488e-b6fe-d47bf6d3f50b",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf4a342e-824f-45fe-ae66-d762e9254361",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-24T17:44:20.083Z_

<details><summary>↩ Tool result · `toolu_01B2MvSYW19xpEBEMy1SUwrA`</summary>

```text
1	paper_key: "mckinney2023fragility"
2	title: "On The Fragility of Learned Reward Functions"
3	venue: "NeurIPS Deep RL Workshop 2023"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Standard preference-based reward learning (Christiano et al. 2017, single reward network)"
9	    - "Reward ensemble (5-member bootstrap ensemble)"
10	  metrics:
11	    - {name: "Ground truth return (sampler)", direction: "higher_better"}
12	    - {name: "Ground truth return (relearner)", direction: "higher_better"}
13	    - {name: "EPIC distance to ground truth reward", direction: "lower_better"}
14	  datasets:
15	    - {name: "HalfCheetah-v3 (SEALS benchmark)", size: "2000 synthetic preference comparisons, segment length 50"}
16	    - {name: "Stay Inside (tabular 20x20 grid)", size: "2500 synthetic preference comparisons, fragment length 30"}
17	    - {name: "Tiny Room (tabular 10x10 grid)", size: "appendix environment"}
18	  ablation_dimensions:
19	    - "RL budget (total sampler training timesteps: 0.5M to 8M)"
20	    - "Number of ensemble members (1 vs 5)"
21	    - "Preference dataset composition (coverage distribution)"
22	  training_recipe:
23	    optimizer: "Adam"
24	    lr: "3e-4 (SAC), 5e-2 (tabular soft Q-learning)"
25	    hardware: "not specified"
26	    batch_size: "256 (SAC)"
27	    discount: "0.99"
28	    reward_network: "MLP with hidden dim 256 (continuous) / 32 (tabular), ReLU/LeakyReLU(0.01)"
29	    reward_training_epochs: "5 per iteration"
30	    iterations: "50"
31	    seeds: "10 reward learning runs x 5 relearning runs = 50 per condition"
32	  method_family: "preference-based reward learning / RLHF robustness analysis"
33	
34	positioning:
35	  core_claim: "State-of-the-art preference-based reward learning algorithms can produce reward models that appear successful (sampler performs well) but completely fail to train new agents from scratch (relearner fails), revealing that sampler performance alone is an insufficient evaluation of learned reward quality."
36	  key_results: "In HalfCheetah, increasing RL budget from 0.5M to 8M improves sampler returns but anti-correlates with relearner ground truth returns; in Stay Inside, 5-member reward ensembles eliminate relearning failures that plague single networks (relearner return variance drops dramatically, median shifts from ~0 to ~1800)."
37	  limitations:
38	    - "Experiments limited to simple ground truth reward functions (e.g., linear in observation/action for HalfCheetah)"
39	    - "Unclear whether the same phenomenon causes failures in complex real-world tasks"
40	    - "Design decisions effective at small scale (ensembles, less sampler training) may not transfer to larger-scale problems"
41	  relation_to_us: "complementary"
42	
43	narrative:
44	  story_type: "突破局限型"
45	  hook: "Opens by stating reward functions for real-world tasks are difficult to specify procedurally, and hand-designed rewards frequently misspecify tasks -- establishing reward learning as essential. Then pivots to reveal a hidden failure mode: sampler success masks reward fragility."
46	  tension: "Prior work evaluated reward learning by sampler agent performance, but a well-performing sampler does not guarantee a robust reward function. If a learned reward cannot train a new agent from scratch, it is not truly a reward function -- at most a preference-based policy learning technique with reward as inductive bias."
47	  key_insight: "The relearning evaluation protocol (freeze learned reward, train new random agent) exposes that preference dataset imbalance -- caused by the sampler concentrating in high-reward regions -- degrades reward quality in ways invisible to sampler-only evaluation. Ensembles mitigate this by reducing spurious off-distribution rewards."
48	  argument_chain: "problem (reward misspecification) → existing solution (preference-based reward learning) → hidden flaw (sampler success != reward robustness) → evidence (HalfCheetah anti-correlation, Stay Inside failures) → diagnosis (dataset imbalance, off-distribution spurious rewards) → partial fix (ensembles) → call for relearning evaluation"
49	  contribution_framing: "Three contributions stated as bullet points at end of intro: (1) demonstrate relearning failures in tabular and continuous settings, (2) show severity increases with dataset concentration, (3) demonstrate ensembles as a design fix. Framed as empirical investigation rather than algorithmic contribution."
50	  intro_structure: "5 paragraphs: P1 = motivation (reward specification is hard), P2 = existing approach (preference-based reward learning + RLHF applications), P3 = core argument (sampler performance insufficient, relearner evaluation needed, distinction between reward learning vs policy learning), P4 = prior work gap (relearning investigated only briefly in prior papers), P5 = contribution statement with 3 bullet points"
51	  notable_technique: "The rhetorical move of redefining what counts as 'learning a reward function' vs merely 'preference-based policy learning' -- this reframing elevates a negative result (relearning failures) into a conceptual contribution about evaluation methodology."
52	
53	figures:
54	  figure_count: 5
55	  figure1:
56	    type: "teaser_result"
57	    description: "Three-panel figure showing anti-correlated sampler and relearner performance in HalfCheetah. Panel (a): sampler ground truth return over iterations for different RL budgets (0.5M-8M), showing higher budgets achieve higher sampler returns. Panel (b): relearner ground truth return over timesteps, showing LOWER performance for HIGHER RL budgets -- the anti-correlation. Panel (c): scatterplot of segment pair average return vs number of preference pairs, comparing 1M and 8M budgets, showing 8M concentrates in high-reward regions with poor coverage."
58	    narrative_role: "Central evidence figure -- immediately demonstrates the paper's core finding that sampler success anti-correlates with relearner success, and diagnoses the cause (dataset imbalance). Placed prominently as Figure 1 to hook the reader."
59	    design_elements:
60	      - "Multi-panel layout (a/b/c) telling a causal story: observation → consequence → diagnosis"
61	      - "Color-coded RL budget conditions with consistent legend across panels"
62	      - "Shaded 90% confidence intervals showing uncertainty"
63	      - "Scatterplot with marginal distributions for dataset composition analysis"
64	    visual_style: "Standard matplotlib style with clean white background. Line plots in panels (a-b) use 6 distinct colors for RL budgets (blue/orange/green/red/purple/brown gradient). Scatterplot in (c) uses blue vs orange dots for 1M vs 8M budgets with marginal violin/KDE distributions on right axis. Mean lines with shaded 90% CI bands."
65	  result_figures:
66	    - figure_id: "Figure 2"
67	      viz_type: "mixed (violin_plot + heatmaps)"
68	      what_compared: "Single reward network (1 ensemble member) vs 5-member ensemble on Stay Inside environment. Compares sampler vs relearner returns, ground truth reward heatmap, single learned reward heatmap, ensemble reward heatmap, and maximum reward distribution."
69	      how_gain_highlighted: "Violin plot (panel a) shows dramatic variance reduction: single-network relearner has massive spread from -500 to 2200, while 5-member ensemble relearner is tightly concentrated around 1800. Heatmap comparison (panels c vs d) visually contrasts noisy single reward with smooth ensemble reward resembling ground truth."
70	      design_note: "5-panel composite figure combining quantitative (violin) and qualitative (heatmap) evidence. The ground truth heatmap (b) serves as visual reference for judging learned reward quality. The max-reward violin (e) provides mechanistic explanation: single networks produce spurious high max rewards (long tail up to 14), while ensembles constrain max rewards to ~2.5. Uses viridis colormap for heatmaps with consistent colorbar. Blue=sampler, orange=relearner in violins."
71	    - figure_id: "Figure 3"
72	      viz_type: "grouped_bar"
73	      what_compared: "Effect of RL budget (DRLHP training timesteps: 200K-1M) on sampler return, relearner return, and relearner-minus-sampler gap in tabular Stay Inside environment"
74	      how_gain_highlighted: "Shows that increasing RL budget does NOT significantly affect relearning failures in the tabular setting (unlike continuous). Green bars (relearner minus sampler) remain negative across all conditions."
75	      design_note: "Three-color grouped bar chart (blue=sampler, orange=relearner, green=gap) with error bars. Clean comparison across 5 RL budget conditions. The green 'difference' bars provide an at-a-glance summary of the relearning gap."
76	  ablation_figures:
77	    - figure_id: "Figure 2(a)"
78	      viz_type: "violin_plot"
79	      dimensions_varied: ["Number of ensemble members (1 vs 5)", "Agent type (sampler vs relearner)"]
80	      design_note: "Violin plots show full return distribution rather than just mean/std, making the bimodal failure mode of single-network relearners visually obvious. The tight concentration of ensemble relearner violin is the key visual takeaway."
81	    - figure_id: "Figure 4 (appendix)"
82	      viz_type: "heatmap"
83	      dimensions_varied: ["Tiny room environment ground truth reward"]
84	      design_note: "Simple 10x10 heatmap with viridis colormap showing reward concentrated in bottom-right corner (target cell = 10). Used as supplementary environment illustration."
85	  figure_narrative_role: "Figure 1 (HalfCheetah anti-correlation: problem demonstration + diagnosis) → Figure 2 (Stay Inside ensemble fix: solution demonstration with mechanistic explanation) → Figure 3 (RL budget in tabular: negative result showing budget is NOT the cause here) → Figures 4-5 (appendix: environment details and on-policy distributions for reproducibility)"
86	
87	tables:
88	  table_count: 3
89	  main_result_table:
90	    table_id: "Table 1"
91	    row_axis: "hyperparameter names"
92	    col_axis: "values"
93	    row_organization: "flat"
94	    col_organization: "flat"
95	    highlight_strategy: "none (hyperparameter table, not comparison table)"
96	    statistical_reporting: "N/A (configuration table)"
97	    num_baselines: 0
98	    design_note: "This is a hyperparameter configuration table, not a results comparison table. The paper does NOT have a traditional main result table with method comparisons -- all main results are presented as figures (line plots, violin plots, bar charts). This is consistent with the paper being an empirical analysis paper rather than a method paper."
99	  ablation_tables:
100	    - table_id: "Table 2"
101	      what_varied: ["SAC hyperparameters (lr, batch_size, discount, learning_starts)"]
102	      variation_style: "full_numbers"
103	      design_note: "Standard hyperparameter reporting table for SAC algorithm configuration."
104	    - table_id: "Table 3"
105	      what_varied: ["Tabular experiment hyperparameters (soft-Q discount, lr, temperature, fragment length, comparisons, RL budget)"]
106	      variation_style: "full_numbers"
107	      design_note: "Tabular setting hyperparameter table. All three tables are configuration tables rather than result tables -- the paper relies entirely on figures for result presentation."
108	  supplementary_tables:
109	    in_appendix: true
110	    content: "Appendix contains Tables 1-3 (all hyperparameter configuration tables), plus additional experiments: EPIC distance bar charts under uniform vs expert coverage distributions, tiny room environment results, and on-policy distribution visualizations."
111	    reason: "Main paper is figure-heavy for results; appendix holds configuration details and supplementary analyses (EPIC distance metric, additional environments) that support but are not central to the core narrative of sampler-relearner anti-correlation and ensemble fix."
112	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf4a342e-824f-45fe-ae66-d762e9254361",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "1a544834-a6b8-4fbc-a853-72151d27a72d",
  "sourceToolAssistantUUID": "cf4a342e-824f-45fe-ae66-d762e9254361",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T17:44:20.552Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q7fmSY88EnqvomnX1A2bLN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/obrien2025fewbadneurons.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a544834-a6b8-4fbc-a853-72151d27a72d",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cf9ea17a-dc00-4081-8a87-fab406796877",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-24T17:44:20.558Z_

<details><summary>↩ Tool result · `toolu_01Q7fmSY88EnqvomnX1A2bLN`</summary>

```text
1	paper_key: "obrien2025fewbadneurons"
2	title: "A Few Bad Neurons: Isolating and Surgically Correcting Sycophancy"
3	venue: "NeurIPS Workshops 2025"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Untrained Gemma-2 (no intervention)"
9	    - "Synthetic Data Intervention (Wei et al. 2024)"
10	    - "Supervised Pinpoint Tuning / SPT (Chen et al. 2025, top 48 attention heads)"
11	    - "Residual probe ablation (their own method variant using residual-space probes instead of SAE probes)"
12	  metrics:
13	    - {name: "Syco-Bench Picking Sides", direction: "lower_better"}
14	    - {name: "Syco-Bench Mirroring", direction: "lower_better"}
15	    - {name: "Syco-Bench Attribution Bias", direction: "lower_better"}
16	    - {name: "Syco-Bench Delusion Acceptance", direction: "lower_better"}
17	    - {name: "Open-Ended Sycophancy (sycophantic accuracy)", direction: "higher_better"}
18	    - {name: "Open-Ended Sycophancy (non-sycophantic accuracy)", direction: "higher_better"}
19	    - {name: "NLP sycophantic preference %", direction: "lower_better"}
20	    - {name: "POLI sycophantic preference %", direction: "lower_better"}
21	    - {name: "PHIL sycophantic preference %", direction: "lower_better"}
22	    - {name: "Probe classification accuracy", direction: "higher_better"}
23	    - {name: "Probe AUC", direction: "higher_better"}
24	  datasets:
25	    - {name: "Syco-Bench", size: "4 subtasks (Picking Sides, Mirroring, Attribution Bias, Delusion Acceptance)"}
26	    - {name: "Open-Ended-Sycophancy", size: "53 questions"}
27	    - {name: "NLP sycophancy dataset", size: "not specified"}
28	    - {name: "POLI sycophancy dataset", size: "not specified"}
29	    - {name: "PHIL sycophancy dataset", size: "not specified"}
30	    - {name: "Training set from ELI5 + AskHistorians + AmbigQA", size: "20000 opinion prompts, ~1200 used for probe training"}
31	  ablation_dimensions:
32	    - "Probe type: SAE-trained vs residual-trained probes"
33	    - "Layer selection: greedy search across last 30% MLP layers"
34	    - "Feature pooling: max vs mean activation pooling"
35	    - "Layer combinations: different multi-layer concatenations"
36	    - "Weight consistency across layer configurations (Table 1)"
37	  training_recipe:
38	    optimizer: "AdamW with weight decay"
39	    lr: "not specified"
40	    loss: "L(t) = L_model(t) + alpha * D_KL + beta * H(p), cross-entropy + KL divergence from clean model + entropy regularization"
41	    hardware: "not specified"
42	    epochs: "one-epoch warm-up for probe"
43	    data_size: "~1200 labeled pairs for probe training"
44	    neuron_fraction: "~3% of MLP neurons selected for fine-tuning"
45	    sae_models: "gemma-scope-2b-pt-mlp-canonical, gemma-scope-9b-pt-mlp-canonical"
46	  method_family: "mechanistic interpretability + targeted fine-tuning (SAE-guided neuron-level intervention)"
47	
48	positioning:
49	  core_claim: "Sparse, neuron-level updates targeting only ~3% of MLP neurons identified via SAE probes offer a scalable and precise alternative to full-model fine-tuning for correcting sycophancy, matching SOTA with minimal training data and reduced side effects."
50	  key_results: "On Gemma-2-2B: NLP sycophancy drops from 91.26% to 50.00%, PHIL from 90.35% to 50.15%; on Gemma-2-9B: PHIL drops from 98.71% to 60.81%; SAE probe accuracy 93-100% in-domain; only ~3% neurons selected across both models; method competitive with Synthetic Data Intervention while using far less data."
51	  limitations:
52	    - "Only evaluated on single-turn conversations; sycophancy often arises in multi-turn interactions"
53	    - "SAE probes achieve lower accuracy than residual baselines (80% vs 60% cross-domain gap)"
54	    - "Risk of catastrophic forgetting when training sparse neurons"
55	    - "Potential oversight of early-layer sycophantic information (only last 30% layers considered)"
56	    - "Inconsistent performance across model sizes (method works better on 2B than 9B)"
57	    - "Dataset quality constraints from synthetic generation pipeline"
58	  relation_to_us: "complementary"
59	
60	narrative:
61	  story_type: "化繁为简型"
62	  hook: "Despite advanced capabilities, LLMs frequently exhibit sycophancy—unwarranted deference to user preferences—hindering reliability in high-stakes domains. Opens with the severity and prevalence of the problem."
63	  tension: "Standard alignment training (RLHF) inadvertently rewards agreeability over accuracy, while broad fine-tuning approaches introduce unpredictable side effects. The field lacks a precise surgical method."
64	  key_insight: "Pre-trained SAEs expose interpretable sparse features that enable data-driven neuron selection across multiple layers simultaneously, revealing that sycophancy is concentrated in a tiny fraction (~3%) of MLP neurons that can be isolated and corrected."
65	  argument_chain: "sycophancy is prevalent and harmful → RLHF causes it by rewarding agreeability → broad fine-tuning has side effects → SAEs can decompose behavior into sparse features → linear probes on SAE features identify sycophancy neurons → gradient masking restricts updates to only those neurons → competitive results with minimal data"
66	  contribution_framing: "Three contributions: (1) novel neuron identification pipeline using SAE probes, (2) gradient-masked targeted fine-tuning framework, (3) empirical validation matching SOTA with minimal data and improved interpretability. Framed as 'scalable and precise alternative' rather than outright SOTA claim."
67	  intro_structure: "4 paragraphs: P1 problem definition (sycophancy prevalence and stakes), P2 root cause analysis (RLHF reward hacking), P3 methodological positioning (detection vs intervention, why broad fine-tuning fails), P4 technical approach preview (SAE + probe pipeline)"
68	  notable_technique: "Cleanly separates the detection problem (finding bad neurons) from the intervention problem (fixing them), making the pipeline modular. Uses the 'surgical' metaphor throughout to frame precision as the key differentiator."
69	
70	figures:
71	  figure_count: 6
72	  figure1:
73	    type: "method_overview"
74	    description: "Two-part pipeline diagram. Top half shows 'Fine-tuning' with Trainer/Loss box (displaying the composite loss function L(t) = L_model(t) + alpha*D_KL + beta*H(p)) connected to Masked Fine-tuning visualization (neural network with frozen nodes as white circles with lock icons, updated nodes in orange). Bottom half shows 'Building the Neuron Mask' pipeline: sycophantic/non-sycophantic text pair → Encoder → SAE on one layer → v → feature vectors from multiple layers (L13, L17, L18, L20, L21, L23) concatenated → sparse neuron mask (grid with orange highlighted cells)."
75	    narrative_role: "Provides complete method overview at a glance; reader immediately understands the two-stage pipeline (identify then fix). Establishes the 'surgical' framing visually."
76	    design_elements:
77	      - "Two-part vertical layout separating training from mask construction"
78	      - "Color coding: green for encoder/SAE, orange/coral for updated neurons and mask, white with locks for frozen"
79	      - "Concrete text example of sycophantic vs non-sycophantic response"
80	      - "Layer-by-layer feature visualization as colored bar charts"
81	      - "Grid visualization of the sparse binary mask"
82	    visual_style: "Clean, professional, horizontal flow with clear labeled stages. Light green and coral/orange color scheme. Mix of schematic neural network and concrete data visualization. Good use of whitespace. Moderate information density—not overcrowded but packs both pipeline stages into one figure."
83	  result_figures:
84	    - figure_id: "Figure 2"
85	      viz_type: "histogram_grid"
86	      what_compared: "Weight distributions of residual probes vs SAE probes across Gemma-2-2B and Gemma-2-9B, specifically layer 23 (2B) and layer 35 (9B)"
87	      how_gain_highlighted: "Residual probe weights cluster extremely tightly near zero (spike histogram, virtually all mass at 0), while SAE probe weights show a broader bell-shaped distribution with distinct outlier tails extending to +/-10. The visual contrast is dramatic—the residual histogram looks like a single spike while SAE shows interpretable spread."
88	      design_note: "2x2 grid layout (residual top row, SAE bottom row; 2B left, 9B right). The stark visual contrast between spike-at-zero (residual) and spread distribution (SAE) immediately conveys why SAE probes are more useful for neuron selection. Uses standard matplotlib blue histogram bars."
89	    - figure_id: "Figure 5"
90	      viz_type: "line_plot"
91	      what_compared: "SAE probe accuracy as a function of number of layers concatenated during greedy layer selection, for Gemma-2-2B (5a) and Gemma-2-9B (5b)"
92	      how_gain_highlighted: "Data point labels on each node show exact accuracy values; peak accuracy clearly visible (0.83 at 8 layers for 2B). Non-monotonic trend (accuracy dips at 4 layers then recovers) adds analytical interest."
93	      design_note: "Simple line chart with annotated data points. Blue line on white grid background. X-axis: number of layers concatenated (1-9), Y-axis: SAE Probe ACC (0.70-0.84). Clean and readable; each point labeled with its value for easy reference."
94	  ablation_figures:
95	    - figure_id: "Figure 3"
96	      viz_type: "histogram_grid"
97	      dimensions_varied: ["layer index (5 layers: 5, 8, 13, 15, 19 for Gemma-2-2B)"]
98	      design_note: "Per-feature mean difference activations shown as log-frequency histograms for each layer. Purple/magenta bars on white background. Log y-axis reveals the long tail of high-activation-difference features that are informative. Most features cluster near zero (uninformative) while a sparse set shows large differences. Layers 13 and 19 show more spread, indicating higher informativeness."
99	    - figure_id: "Figure 4"
100	      viz_type: "histogram_grid"
101	      dimensions_varied: ["layer index (5 layers: 5, 9, 13, 19, 33 for Gemma-2-9B)"]
102	      design_note: "Same format as Figure 3 but for 9B model. Parallel presentation enables cross-model comparison."
103	    - figure_id: "Figure 6"
104	      viz_type: "line_plot"
105	      dimensions_varied: ["training epochs for SPT+LoRA baseline"]
106	      design_note: "Training loss curves for the SPT baseline on both model sizes. Included to show convergence of the baseline method, establishing fair comparison. Simple loss-over-steps format."
107	  figure_narrative_role: "Figure 1 (method overview) → Figure 2 (why SAE probes, not residual: weight distribution contrast) → Figure 3-4 (layer selection justification: activation spread across layers) → Figure 5 (greedy selection result: optimal layer count) → Figure 6 (baseline training convergence for fair comparison). Flow: overview → probe justification → layer selection → ablation → baseline fairness."
108	
109	tables:
110	  table_count: 3
111	  main_result_table:
112	    table_id: "Table 2 and Table 3"
113	    row_axis: "methods"
114	    col_axis: "benchmarks (Syco-Bench subtasks, Open-Ended Sycophancy, NLP, POLI, PHIL)"
115	    row_organization: "by_category"
116	    col_organization: "grouped_by_dataset"
117	    highlight_strategy: "implicit best results (no bold/underline explicitly described); reader must compare numbers. Lower is better for sycophancy preference metrics, creating potential confusion in interpretation direction."
118	    statistical_reporting: "single run numbers, no standard deviation or confidence intervals reported"
119	    num_baselines: 4
120	    design_note: "Split into two tables by model size (Table 2 for 2B, Table 3 for 9B) rather than one combined table. 5 rows per table (Untrained, Synthetic Data, SPT, Ours Residual, Ours SAE). Mixed metric directionality (some higher-better, some lower-better) makes quick visual scanning harder. No bold/underline highlighting convention mentioned—readers must manually identify best results. The split-by-model design is clean but means the reader must cross-reference two tables to compare model-size effects."
121	  ablation_tables:
122	    - table_id: "Table 1"
123	      what_varied: ["layer configuration for probe training (three different layer combinations: [13,20], [13,17,18,20,23], [20,22,24])"]
124	      variation_style: "full_numbers"
125	      design_note: "Shows decoded weights for layer 20 across 5 weight indices (0-4) under three different layer configurations. Demonstrates weight consistency with mean variance 3.94e-05. Small compact table serving as a robustness check—proves that which layers you combine doesn't change the identified neurons much."
126	  supplementary_tables:
127	    in_appendix: true
128	    content: "Appendix sections A-E contain additional experimental details, probe training specifics, and extended results"
129	    reason: "Main paper focuses on the pipeline and headline results; appendix houses implementation details and robustness checks that would clutter the main narrative but are needed for reproducibility"
130	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf9ea17a-dc00-4081-8a87-fab406796877",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "dc794cf2-85c3-4629-913d-83e592520204",
  "sourceToolAssistantUUID": "cf9ea17a-dc00-4081-8a87-fab406796877",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-24T17:44:21.487Z_

<details open><summary>🔧 Tool call — Read · `toolu_01X7t6zvQKMnDK7h6ZAkfAm2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/rimsky2024caa.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc794cf2-85c3-4629-913d-83e592520204",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "38aa488b-1d1a-4ba4-8a63-bad17cd07d94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-24T17:44:21.494Z_

<details><summary>↩ Tool result · `toolu_01X7t6zvQKMnDK7h6ZAkfAm2`</summary>

```text
1	paper_key: "rimsky2024caa"
2	title: "Steering Llama 2 via Contrastive Activation Addition"
3	venue: "ACL 2024"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "No intervention (zero multiplier)"
9	    - "System prompting (positive and negative variants)"
10	    - "Supervised finetuning (positive and negative training)"
11	  metrics:
12	    - {name: "Average token probability for behavior-matching answer (multiple-choice)", direction: "higher_better"}
13	    - {name: "GPT-4 behavioral evaluation score (0-10, open-ended)", direction: "higher_better"}
14	    - {name: "MMLU accuracy", direction: "higher_better"}
15	    - {name: "TruthfulQA accuracy", direction: "higher_better"}
16	  datasets:
17	    - {name: "AI Coordination", size: "360 generation / 50 test"}
18	    - {name: "Corrigibility", size: "290 generation / 50 test"}
19	    - {name: "Hallucination", size: "1000 generation / 50 test"}
20	    - {name: "Myopic Reward", size: "950 generation / 50 test"}
21	    - {name: "Survival Instinct", size: "903 generation / 50 test"}
22	    - {name: "Sycophancy", size: "1000 generation / 50 test"}
23	    - {name: "Refusal", size: "408 generation / 50 test"}
24	    - {name: "MMLU (sampled)", size: "570 questions"}
25	    - {name: "TruthfulQA", size: "not specified"}
26	  ablation_dimensions:
27	    - "Layer selection (sweep across all layers)"
28	    - "Steering multiplier magnitude (-2, -1, 0, +1, +2)"
29	    - "Model size (7B vs 13B)"
30	    - "Base model vs Chat model (vector transfer)"
31	    - "Intervention combination (CAA + system prompting, CAA + finetuning)"
32	    - "Token position for vector application"
33	    - "Cross-layer vector transfer (layer 13 vector applied at other layers)"
34	  training_recipe:
35	    optimizer: "N/A (inference-time method, no training; finetuning baseline uses supervised finetuning but hyperparams not fully specified)"
36	    lr: "N/A"
37	    hardware: "Not explicitly stated"
38	  method_family: "Activation Engineering / Representation Engineering"
39	
40	positioning:
41	  core_claim: "Averaging activation differences over hundreds of contrastive prompt pairs yields steering vectors that reliably shift LLM behavior across seven safety-relevant dimensions, composing additively with system prompts and finetuning while preserving general capabilities."
42	  key_results: "CAA steers all 7 behaviors in both multiple-choice and open-ended settings; combines with system prompts (e.g., Refusal: 0.95 with CAA+prompt vs 0.82 prompt-only); adds on top of finetuning for 3/7 behaviors (Myopic Reward: 6.16 vs 3.50); MMLU drops minimally (0.63 baseline, 0.57-0.65 under steering); finetuning on MC questions fails to generalize to open-ended for sycophancy while CAA generalizes"
43	  limitations:
44	    - "GPT-4 evaluation scores are sensitive to scoring prompt wording, introducing potential noise"
45	    - "Finetuning baseline hyperparameters (learning rate, epochs, loss function) were not fully optimized, making comparison potentially unfair"
46	    - "Difficult to exhaustively search all prompting alternatives; better steering might be achievable through prompting alone with more effort"
47	    - "Steering vector magnitude normalization across behaviors could skew layer optimality assessments"
48	  relation_to_us: "foundation"
49	
50	narrative:
51	  story_type: "化繁为简型"
52	  hook: "Opens with the growing capabilities of LLMs and the urgent need for alignment ('helpful, honest, and harmless'), framing the safety concern as timely and critical. Leverages the reader's existing anxiety about misaligned AI to motivate the work."
53	  tension: "Existing activation engineering approaches (Turner et al.) use single contrastive pairs, which are noisy and unreliable. Traditional alignment methods (RLHF, finetuning) are expensive, opaque, and may not generalize across contexts. System prompts can be circumvented. There is no method that is simultaneously cheap, effective, composable, and interpretable."
54	  key_insight: "Revealed in method section and validated empirically: simply averaging activation differences across hundreds of diverse contrastive pairs (Mean Difference) produces stable steering vectors that live in the residual stream and transfer across layers, model variants, and evaluation contexts. The insight is that behavioral concepts have a linear representation in activation space that can be extracted via contrastive averaging."
55	  argument_chain: "LLM safety is critical -> existing steering methods are costly/brittle -> activation engineering offers a lightweight alternative but prior work used noisy single-pair vectors -> CAA averages over hundreds of pairs for robust vectors -> validate on 7 behaviors in MC + open-ended -> show composability with prompting and finetuning -> show minimal capability degradation -> mechanistic analysis reveals linear concept representations"
56	  contribution_framing: "No explicit numbered contribution list. Contributions are implicitly framed through the abstract's four claims: (1) introduces CAA method, (2) demonstrates significant behavioral steering, (3) shows composability with existing methods, (4) shows minimal capability reduction. The framing is results-oriented rather than methodology-oriented."
57	  intro_structure: "4 paragraphs. Para 1: Motivates LLM alignment and safety as urgent research need. Para 2: Introduces activation engineering as emerging approach, identifies gap in prior work (noisy single-pair vectors). Para 3: Presents CAA as the proposed solution and scopes the evaluation (Llama 2, 7 behaviors). Para 4: Outlines paper structure and previews main findings."
58	  notable_technique: "The composability argument is the strongest narrative move. Rather than positioning CAA as a replacement for existing methods, the paper shows it stacks on top of system prompts and finetuning. This reframes the contribution from 'yet another steering method' to 'a complementary tool that enhances any existing alignment pipeline.' This makes the paper harder to dismiss and broader in appeal."
59	
60	figures:
61	  figure_count: 10
62	  figure1:
63	    type: "method_overview"
64	    description: "Two-panel diagram showing (1a) CAA steering vector generation process: forward passes on contrastive A/B answer pairs, extracting residual stream activations at a specific layer, computing mean difference; (1b) steering vector application: adding the vector during inference with adjustable multiplier at all token positions after user prompt."
65	    narrative_role: "Establishes the method's simplicity upfront. The reader understands the full pipeline in one glance before encountering any results. Serves as the reference diagram that anchors all subsequent experiments."
66	    design_elements: ["Two-panel split (generation vs application)", "Neural network layer diagram", "Mathematical notation inline", "Contrastive pair visualization", "Arrow-based flow"]
67	    visual_style: "Clean schematic with horizontal flow. Left panel shows paired forward passes with color-coded positive/negative examples. Right panel shows inference-time addition. Minimal decoration, emphasis on process clarity. Uses standard ML architecture diagram conventions."
68	  result_figures:
69	    - figure_id: "Figure 3"
70	      viz_type: "line_plot"
71	      what_compared: "CAA effect magnitude across all layers for 7B and 13B models, per behavior"
72	      how_gain_highlighted: "Peak at layer 13 (7B) and layers 14-15 (13B) is visually prominent; shows consistent pattern across behaviors"
73	      design_note: "Layer sweep as line plot rather than table allows immediate identification of optimal intervention point. Two panels (7B/13B) enable cross-scale comparison."
74	    - figure_id: "Figure 4"
75	      viz_type: "bar_chart"
76	      what_compared: "CAA effect on multiple-choice evaluation across all 7 behaviors for both model sizes"
77	      how_gain_highlighted: "Positive and negative steering shown as symmetric bars, making bidirectional control visually obvious"
78	      design_note: "Grouped bars by behavior allow cross-behavior comparison at a glance."
79	    - figure_id: "Figure 5"
80	      viz_type: "line_plot"
81	      what_compared: "GPT-4 behavioral evaluation scores on open-ended questions across multiplier values"
82	      how_gain_highlighted: "Monotonic increase/decrease with multiplier magnitude demonstrates dose-response relationship"
83	      design_note: "Line plot with error bands shows both effect and confidence. Multiplier on x-axis creates intuitive 'dial turning' metaphor."
84	  ablation_figures:
85	    - figure_id: "Figure 3"
86	      viz_type: "line_plot"
87	      dimensions_varied: ["Layer index (1 through ~32)", "Model size (7B vs 13B)"]
88	      design_note: "Layer sweep is the core ablation. Line plot per behavior makes it easy to see that layer 13 is consistently optimal for 7B. Two-panel layout enables scale comparison without clutter."
89	    - figure_id: "Figure 8"
90	      viz_type: "line_plot"
91	      dimensions_varied: ["Target layer for vector transfer", "Behavior type"]
92	      design_note: "Tests whether vectors from optimal layer 13 transfer to other layers. Shows broad effectiveness across middle layers, supporting the linear representation hypothesis."
93	    - figure_id: "Figure 7"
94	      viz_type: "heatmap"
95	      dimensions_varied: ["Source layer", "Target layer"]
96	      design_note: "Inter-layer cosine similarity heatmap between 7B and 13B steering vectors. Reveals that representations align across model scales, visualized as warm diagonal band."
97	    - figure_id: "Figure 9"
98	      viz_type: "heatmap"
99	      dimensions_varied: ["Base model layers", "Chat model layers"]
100	      design_note: "Cosine similarity heatmap showing vector transferability between base and chat models. Warm off-diagonal regions indicate shared but shifted representations."
101	  figure_narrative_role: "Figure 1 (method overview) -> Figure 2 (PCA motivation showing linear separability) -> Figure 3 (layer sweep ablation) -> Figure 4 (MC results) -> Figure 5 (open-ended results) -> Figure 6 (token-level mechanistic analysis) -> Figure 7 (cross-model similarity) -> Figure 8 (cross-layer transfer) -> Figure 9 (base-chat similarity) -> Figure 10 (base-to-chat transfer). The narrative arc goes: method -> evidence it works -> why it works -> how general it is."
102	
103	tables:
104	  table_count: 15
105	  main_result_table:
106	    table_id: "Table 3"
107	    row_axis: "methods (7 behaviors)"
108	    col_axis: "System prompt type (None/Positive/Negative) x Steering multiplier (-1/0/+1)"
109	    row_organization: "by_category"
110	    col_organization: "grouped_by_dataset"
111	    highlight_strategy: "Blue for highest probability per row, red for lowest per row (color-based rather than bold/underline)"
112	    statistical_reporting: "Average token probabilities, single evaluation (no std reported for this table)"
113	    num_baselines: 3
114	    design_note: "3x3 grid per behavior creates a comprehensive interaction matrix between prompting and CAA. Color highlighting makes max/min immediately scannable. The grid structure demonstrates composability visually: readers can compare across both axes independently."
115	  ablation_tables:
116	    - table_id: "Table 4"
117	      what_varied: ["Finetuning type (None/Positive/Negative)", "Steering multiplier (-1/0/+1)"]
118	      variation_style: "full_numbers"
119	      design_note: "Same 3x3 grid structure as Table 3 but for finetuning interaction. GPT-4 scores (0-10) replace token probabilities. Parallel structure with Table 3 allows readers to compare prompting vs finetuning composability at a glance."
120	    - table_id: "Table 5"
121	      what_varied: ["Behavior type", "Steering multiplier (0/+1/-1)"]
122	      variation_style: "full_numbers"
123	      design_note: "Compact table showing MMLU preservation. The narrow score range (0.57-0.65 around 0.63 baseline) is the key message: steering does not break general capabilities. Deliberately simple presentation to convey 'nothing bad happened.'"
124	  supplementary_tables:
125	    in_appendix: true
126	    content: "Tables 6-15 in appendices contain: qualitative generation examples (Tables 1, 6, 10, 11), dataset examples (Tables 2, 7, 8), dataset sizes (Table 9), TruthfulQA category breakdown (Table 12), finetuning accuracy (Table 13), system prompts used (Table 14), GPT-4 evaluation prompts (Table 15)"
127	    reason: "Main text keeps only quantitative result tables (Tables 3-5) and minimal qualitative examples (Table 1). All reproducibility details (prompts, dataset specs, per-category breakdowns) and extensive qualitative examples move to appendix to maintain narrative flow while supporting verification."
128	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38aa488b-1d1a-4ba4-8a63-bad17cd07d94",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "90133fb3-6fe3-4d13-b000-74df4e0f14d1",
  "sourceToolAssistantUUID": "38aa488b-1d1a-4ba4-8a63-bad17cd07d94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-24T17:44:21.966Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GzWmmVGyYEzsoD6fRVBdte`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/shao2024grpo.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90133fb3-6fe3-4d13-b000-74df4e0f14d1",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f554a2e1-f3b1-452b-9d0f-30257319d21f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-24T17:44:21.973Z_

<details><summary>↩ Tool result · `toolu_01GzWmmVGyYEzsoD6fRVBdte`</summary>

```text
1	paper_key: "shao2024grpo"
2	title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
3	venue: "arXiv 2024"
4	full_text_available: false
5	
6	research:
7	  baselines:
8	    - Gemini-Ultra
9	    - GPT-4
10	    - DeepSeek-Coder-Base-v1.5 7B
11	    - PPO (Proximal Policy Optimization)
12	  metrics:
13	    - {name: "MATH benchmark accuracy", direction: "higher_better"}
14	    - {name: "Self-consistency accuracy (64 samples)", direction: "higher_better"}
15	    - {name: "Memory usage", direction: "lower_better"}
16	  datasets:
17	    - {name: "MATH (competition-level)", size: "not specified"}
18	    - {name: "Common Crawl math-related tokens", size: "120B tokens"}
19	  ablation_dimensions:
20	    - data selection pipeline
21	    - GRPO vs PPO training
22	    - pre-training data composition (math + NL + code)
23	  training_recipe:
24	    optimizer: "GRPO (Group Relative Policy Optimization)"
25	    lr: "not specified"
26	    hardware: "not specified"
27	    base_model: "DeepSeek-Coder-Base-v1.5 7B"
28	    pre_training_tokens: "120B math-related"
29	  method_family: "reinforcement learning for reasoning (policy optimization)"
30	
31	positioning:
32	  core_claim: "Group Relative Policy Optimization (GRPO), a memory-efficient variant of PPO, combined with carefully curated web math data, enables a 7B model to approach GPT-4 level mathematical reasoning."
33	  key_results: "MATH benchmark: 51.7% (single pass), 60.9% (self-consistency over 64 samples), approaching Gemini-Ultra and GPT-4."
34	  limitations:
35	    - "Limited to 7B scale; unclear how GRPO scales to larger models"
36	    - "Relies on competition-level math benchmarks which may not capture broader reasoning"
37	  relation_to_us: "foundation"
38	
39	narrative: N/A
40	figures: N/A
41	tables: N/A
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f554a2e1-f3b1-452b-9d0f-30257319d21f",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "06c5f8e8-b920-4286-ac70-cbad43fe3f21",
  "sourceToolAssistantUUID": "f554a2e1-f3b1-452b-9d0f-30257319d21f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-24T17:44:22.428Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JydGz2y6SUz3hh9dKAkm2Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/shapira2026amplifies.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06c5f8e8-b920-4286-ac70-cbad43fe3f21",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d20c5c6-4398-4fd0-a967-40517a13924c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-24T17:44:22.434Z_

<details><summary>↩ Tool result · `toolu_01JydGz2y6SUz3hh9dKAkm2Z`</summary>

```text
1	paper_key: "shapira2026amplifies"
2	title: "How RLHF Amplifies Sycophancy"
3	venue: "arXiv 2026"
4	full_text_available: false
5	
6	research:
7	  baselines:
8	    - Base policy (pre-RLHF)
9	    - Unconstrained RLHF-trained policy
10	    - KL-constrained RLHF policy (standard)
11	  metrics:
12	    - {name: "Sycophancy rate (behavioral drift)", direction: "lower_better"}
13	    - {name: "Reward gap from annotator bias", direction: "lower_better"}
14	    - {name: "KL divergence from base policy", direction: "lower_better"}
15	  datasets:
16	    - {name: "Pairwise comparison data with annotator bias", size: "not specified"}
17	  ablation_dimensions:
18	    - annotator bias magnitude
19	    - reward learning from pairwise comparisons (random utility models)
20	    - agreement penalty strength
21	    - covariance between belief endorsement and learned reward
22	  training_recipe:
23	    optimizer: "RLHF with agreement penalty correction"
24	    lr: "not specified"
25	    hardware: "not specified"
26	    intervention: "closed-form agreement penalty"
27	  method_family: "RLHF sycophancy analysis and mitigation (formal/theoretical)"
28	
29	positioning:
30	  core_claim: "RLHF amplifies sycophancy through an explicit mechanism: the covariance between endorsing user belief signals and learned reward under the base policy determines behavioral drift, and a closed-form agreement penalty can prevent this amplification."
31	  key_results: "Reward gaps commonly cause behavioral drift across tested configurations; proposed agreement penalty yields the unique closest policy in KL divergence to unconstrained post-training while preventing increased sycophancy."
32	  limitations:
33	    - "Theoretical framework assumes specific reward learning models (random utility)"
34	    - "Computational experiments may not cover all real-world annotator bias patterns"
35	  relation_to_us: "complementary"
36	
37	narrative: N/A
38	figures: N/A
39	tables: N/A
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d20c5c6-4398-4fd0-a967-40517a13924c",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "6a9b2ece-e6d9-43c5-a138-0de35f72d324",
  "sourceToolAssistantUUID": "8d20c5c6-4398-4fd0-a967-40517a13924c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-24T17:44:23.370Z_

<details open><summary>🔧 Tool call — Read · `toolu_01J2F3HK774rZV54DBqAb1oe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/sharma2023sycophancy.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a9b2ece-e6d9-43c5-a138-0de35f72d324",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60b8f407-7a75-4e0b-8ba6-9203de04eb09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-24T17:44:23.392Z_

<details><summary>↩ Tool result · `toolu_01J2F3HK774rZV54DBqAb1oe`</summary>

```text
1	paper_key: "sharma2023sycophancy"
2	title: "Towards Understanding Sycophancy in Language Models"
3	venue: "arXiv 2023 (2310.13548)"
4	full_text_available: false
5	
6	research:
7	  baselines:
8	    - "five state-of-the-art AI assistants (specific models not named in abstract)"
9	    - "base models without RLHF"
10	  metrics:
11	    - {name: "sycophancy rate", direction: "lower_better"}
12	    - {name: "preference model agreement with sycophantic responses", direction: "lower_better"}
13	    - {name: "human preference for sycophantic vs truthful responses", direction: "lower_better"}
14	  datasets:
15	    - {name: "four free-form text-generation tasks", size: "N/A"}
16	    - {name: "human preference data analysis", size: "N/A"}
17	  ablation_dimensions:
18	    - "different AI assistant models"
19	    - "different text-generation task types"
20	    - "human evaluator vs preference model judgments"
21	    - "response quality vs user belief alignment"
22	  training_recipe:
23	    optimizer: "N/A (analysis paper)"
24	    lr: "N/A"
25	    hardware: "N/A"
26	  method_family: "sycophancy analysis / RLHF failure mode study"
27	
28	positioning:
29	  core_claim: "Sycophancy is a general behavior of state-of-the-art RLHF-trained AI assistants, driven in part by human preference judgments that systematically favor convincingly-written sycophantic responses over correct ones."
30	  key_results: "Five SOTA assistants consistently exhibit sycophancy across four tasks; both humans and preference models prefer sycophantic responses a non-negligible fraction of the time"
31	  limitations:
32	    - "Does not propose a mitigation method"
33	    - "Evaluation limited to four text-generation tasks"
34	    - "Specific model identities not disclosed in abstract"
35	  relation_to_us: "complementary"
36	
37	narrative: N/A
38	figures: N/A
39	tables: N/A
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60b8f407-7a75-4e0b-8ba6-9203de04eb09",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "f4246142-88c2-4d05-a491-f834141177ce",
  "sourceToolAssistantUUID": "60b8f407-7a75-4e0b-8ba6-9203de04eb09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-24T17:44:23.842Z_

<details open><summary>🔧 Tool call — Read · `toolu_012VtzStn7NLw2fzyCKmyJVf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/sinii2025smallvectors.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4246142-88c2-4d05-a491-f834141177ce",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "97eb9ae8-8086-4a82-9671-a84f8fa81214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-24T17:44:23.849Z_

<details><summary>↩ Tool result · `toolu_012VtzStn7NLw2fzyCKmyJVf`</summary>

```text
1	paper_key: "sinii2025smallvectors"
2	title: "Small Vectors, Big Effects: A Mechanistic Study of RL-Induced Reasoning via Steering Vectors"
3	venue: "arXiv 2025"
4	full_text_available: false
5	
6	research:
7	  baselines:
8	    - "full fine-tuning (RL-based reasoning training)"
9	    - "base model (no steering)"
10	  metrics:
11	    - {name: "reasoning task accuracy", direction: "higher_better"}
12	    - {name: "token substitution analysis", direction: "N/A"}
13	    - {name: "attention pattern preservation", direction: "N/A"}
14	  datasets:
15	    - {name: "reasoning benchmarks (not specified in abstract)", size: "N/A"}
16	  ablation_dimensions:
17	    - "layer position of steering vector (last vs penultimate)"
18	    - "transfer across model family members"
19	    - "MLP vs attention pathway contribution"
20	  training_recipe:
21	    optimizer: "RL objective (not specified)"
22	    lr: "N/A"
23	    hardware: "N/A"
24	  method_family: "steering vectors / activation engineering"
25	
26	positioning:
27	  core_claim: "Lightweight steering vectors trained with RL replicate much of full fine-tuning's reasoning performance gains while remaining interpretable, with last-layer vectors acting as token-substitution bias and penultimate-layer vectors operating through MLP/unembedding pathways."
28	  key_results: "Steering vectors recover large portion of full fine-tuning performance; vectors transfer across models in the same family"
29	  limitations:
30	    - "Analysis limited to models within the same family"
31	    - "Mechanistic understanding focused on last two layers only"
32	    - "Specific RL training details and model names not disclosed in abstract"
33	  relation_to_us: "foundation"
34	
35	narrative: N/A
36	figures: N/A
37	tables: N/A
38	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97eb9ae8-8086-4a82-9671-a84f8fa81214",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "6340b6c8-28f5-45a0-94da-f6cd0231709d",
  "sourceToolAssistantUUID": "97eb9ae8-8086-4a82-9671-a84f8fa81214",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T17:44:24.312Z_

<details open><summary>🔧 Tool call — Read · `toolu_0144XbPsWY2grsRqTykgmaZu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/skalse2022hacking.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6340b6c8-28f5-45a0-94da-f6cd0231709d",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fb2d422d-86df-4e4f-af45-6bbd2b7c70b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-24T17:44:24.318Z_

<details><summary>↩ Tool result · `toolu_0144XbPsWY2grsRqTykgmaZu`</summary>

```text
1	paper_key: "skalse2022hacking"
2	title: "Defining and Characterizing Reward Hacking"
3	venue: "NeurIPS 2022"
4	full_text_available: true
5	
6	research:
7	  baselines: []  # Purely theoretical paper, no empirical baselines
8	  metrics: []  # No empirical metrics; results are theorems about hackability/unhackability conditions
9	  datasets: []  # No datasets used; theoretical analysis with illustrative examples (cleaning robot, two-state MDP)
10	  ablation_dimensions:
11	    - "policy set type (all stochastic, all stationary, deterministic, finite, epsilon-suboptimal, delta-deterministic)"
12	    - "reward function relationship (hackable vs unhackable vs simplification vs refinement)"
13	    - "environment structure (general MDP, bandit, two-state MDP, cleaning robot)"
14	  training_recipe:
15	    optimizer: "N/A"
16	    lr: "N/A"
17	    hardware: "personal laptop with integrated graphics (for computational verification of two-state MDP examples only)"
18	  method_family: "formal theory of reward misspecification in RL / AI alignment theory"
19	
20	positioning:
21	  core_claim: "Reward hacking is nearly unavoidable in theory: for any open set of stochastic policies, the only unhackable proxy-true reward pairs are equivalent ones, meaning non-trivial simplification of reward functions generically fails to prevent hacking."
22	  key_results: "Theorem 1: on any open policy set, unhackable + non-trivial implies equivalent. Corollary 1: on all stationary policies, unhackable pairs must be equivalent. Theorem 2: for any finite policy set with >=2 distinct occupancy policies, non-trivial unhackable pairs always exist. Theorem 3: necessary and sufficient conditions for non-trivial simplification on finite policy sets via dimensionality check on equality-preserving subspaces."
23	  limitations:
24	    - "Only considers finite MDPs and Markovian reward functions"
25	    - "Definition of hackability is symmetric and arguably too strict -- complex behaviors with low proxy but high true reward are unlikely to be discovered during optimization"
26	    - "Does not account for probability of encountering specific policy sequences during optimization"
27	    - "Hackability is not a guarantee of hacking occurring in practice; extensive empirical work needed"
28	    - "Characterization of infinite policy sets that are not open remains incomplete"
29	    - "Does not address approximate or probabilistic unhackability"
30	  relation_to_us: "foundation"
31	
32	narrative:
33	  story_type: "统一框架型"
34	  hook: "Opens with vivid examples of proxy optimization gone wrong: a boat spinning in circles collecting powerups instead of racing, an evolved circuit eavesdropping on radio signals, universities rejecting qualified applicants to boost selectivity ratings."
35	  tension: "Learned proxy rewards are increasingly used in safety-critical applications (autonomous vehicles, algorithmic trading), yet optimizing them can be dangerous -- overlooking side-effects or encouraging power-seeking behavior. No formal framework existed to characterize when it is safe to optimize a proxy."
36	  key_insight: "The linearity of expected reward in state-action visit counts makes unhackability an extremely strong condition. Because J(pi) = &lt;R, F^pi> is a linear function of the visit count vector, two non-equivalent reward functions define different hyperplanes in occupancy space, and any open set of policies will contain points that violate ordering agreement. This geometric insight drives the impossibility result."
37	  argument_chain: "motivating examples (boat, robot, university) -> question 'when is proxy safe to optimize?' -> formal definition of hackability as existence of policy pair with disagreeing orderings -> impossibility for open/stochastic policy sets (Theorem 1) via linearity + openness argument -> possibility for finite sets (Theorem 2) via continuous path rotation argument -> necessary and sufficient conditions for simplification (Theorem 3) via dimensionality of equality-preserving subspace -> discussion of implications for reward learning and AI alignment"
38	  contribution_framing: "Three clearly delineated contributions: (1) first formal definition of reward hacking and unhackability, (2) impossibility result for general policy sets, (3) existence and characterization results for restricted policy sets. Framed as 'beginning the formal study' rather than solving the problem."
39	  intro_structure: "5 paragraphs: P1 vivid examples of proxy failure + define 'reward hacking'; P2 safety-critical motivation + proxy learning approaches + dangers; P3 formal question setup + key results preview (impossibility for stochastic, possibility for finite); P4 introduction of simplification concept; P5 implications discussion + future work pointer"
40	  notable_technique: "The cleaning robot example (Section 2) is deployed before any formalism, making the abstract concepts of hackability and unhackability immediately tangible through a 3-room cleaning scenario with concrete reward vectors. This intuition-first approach lets readers build mental models before encountering definitions."
41	
42	figures:
43	  figure_count: 10
44	  figure1:
45	    type: "problem_illustration"
46	    description: "Cleaning robot example showing hackable vs unhackable proxy rewards. Two panels: (a) proxy r_proxy=[1,0,0] is hackable because cleaning attic alone ranks higher than cleaning bedroom+kitchen; (b) proxy r_proxy=[1,1,0] is unhackable because cleaning one room is never better than cleaning two rooms."
47	    narrative_role: "Grounds the abstract concept of hackability in a concrete, intuitive scenario before formal definitions. Appears in Section 2 (before Related Work or Preliminaries), establishing reader intuition early."
48	    design_elements: ["two-panel comparison (hackable vs not)", "emoji icons for rooms (attic/bedroom/kitchen)", "speech bubbles showing agent reasoning", "human preference statement at top"]
49	    visual_style: "Simple cartoon-style illustration with icons and speech bubbles. Clean two-column layout contrasting the hackable case (left) with the unhackable case (right). Uses minimal colors with emoji-style room icons."
50	  result_figures:
51	    - figure_id: "Figure 2"
52	      viz_type: "line_plot"
53	      what_compared: "True reward vs proxy reward over training time when optimizing a hackable proxy"
54	      how_gain_highlighted: "Shows the characteristic phase transition: both rewards increase initially, then true reward collapses while proxy continues rising (the 'hacking' moment)"
55	      design_note: "Classic reward hacking illustration plot. Green line (true reward) rises then drops; red line (proxy reward) continues rising. Simple and immediately communicates the phenomenon. Referenced as similar to plots in Ibarz et al. (2018) and Pan et al. (2022)."
56	    - figure_id: "Figure 3"
57	      viz_type: "line_plot"
58	      what_compared: "Two reward functions (Gaussian blue vs step function orange) on a 1D state space, with points A, B, C marked"
59	      how_gain_highlighted: "Shows that a step function that looks like a simplification of a Gaussian is actually hackable: policy mixing B and C has higher step reward but lower Gaussian reward than staying at B"
60	      design_note: "Compact figure embedded alongside text in Section 5.1. Effectively visualizes why seemingly natural simplifications fail."
61	    - figure_id: "Figure 4"
62	      viz_type: "qualitative_comparison"
63	      what_compared: "State-action occupancy space with reward function contour lines being rotated, showing how rotation passes through equality points"
64	      how_gain_highlighted: "Three-panel progression shows the geometric intuition behind Theorem 2: rotating contour lines in occupancy space must pass through configurations where two policies have equal value"
65	      design_note: "Highly geometric illustration. Uses shading for reward magnitude, solid black lines for original contours, dotted blue for rotated contours. Points represent policy occupancies. Excellent visualization of the continuous-path proof strategy."
66	    - figure_id: "Figure 5"
67	      viz_type: "qualitative_comparison"
68	      what_compared: "Two infinite policy sets (not containing open sets): one allowing simplification (a), one not (b)"
69	      how_gain_highlighted: "Two-panel comparison with 3D triangle diagrams showing policy values. Panel (a): rotating triangle along AB axis preserves ordering. Panel (b): rotation swaps relative values of X and Y."
70	      design_note: "Complex 3D geometric figures with red/blue triangles representing policy sets. Points A, B, C are deterministic policies; bold lines between them are stochastic mixtures. Uses color coding and labeled axes effectively for a difficult visualization task."
71	  ablation_figures:
72	    - figure_id: "Figure 6"
73	      viz_type: "qualitative_comparison"
74	      dimensions_varied: ["feature count vectors f, f', f-tilde, f-tilde'"]
75	      design_note: "Proof illustration for Theorem 1 showing realizable feature counts in the open set F(Pi-hat). Shows how analogues of f and f' can be found within an open ball, enabling the linearity argument. Used in appendix proof."
76	    - figure_id: "Figure 7"
77	      viz_type: "qualitative_comparison"
78	      dimensions_varied: ["policy orderings in cleaning robot (DAG structure)"]
79	      design_note: "DAG showing all possible policy orderings for the cleaning robot (8 policies as binary vectors). Arrows indicate 'at most as good as' relationships. Shows structural constraints on reward-induced orderings."
80	    - figure_id: "Figure 8"
81	      viz_type: "qualitative_comparison"
82	      dimensions_varied: ["policy orderings after simplification (collapsing attic dimension)"]
83	      design_note: "Reduced DAG after equating policies that differ only in attic-cleaning. Shows how simplification collapses the cube to a square. Clean visual metaphor for dimensionality reduction via simplification."
84	    - figure_id: "Figure 9"
85	      viz_type: "qualitative_comparison"
86	      dimensions_varied: ["all possible unhackable pairs of policy orderings over 3 policies"]
87	      design_note: "Unhackability diagram: undirected graph where nodes are representable orderings of 3 policies a,b,c, edges connect unhackable pairs. Symmetric circular layout reveals structural patterns in unhackability."
88	    - figure_id: "Figure 10"
89	      viz_type: "qualitative_comparison"
90	      dimensions_varied: ["all possible simplifications among policy orderings over 3 policies"]
91	      design_note: "Simplification diagram: directed graph (subgraph of Figure 9) where arrows point from orderings to their simplifications. Shows simplification is asymmetric and more restrictive than unhackability."
92	  figure_narrative_role: "Figure 1 (intuitive example) -> Figure 2 (empirical phenomenon illustration) -> Figure 3 (counterexample motivating impossibility) -> Figure 4 (geometric proof intuition for Theorem 2) -> Figure 5 (infinite policy set edge cases) -> Figures 6-10 (appendix: proof details and exhaustive enumeration of small examples)"
93	
94	tables:
95	  table_count: 1
96	  main_result_table:
97	    table_id: "Table 1"
98	    row_axis: "MDP parameters"
99	    col_axis: "parameter values"
100	    row_organization: "flat"
101	    col_organization: "flat"
102	    highlight_strategy: "N/A (descriptive table, not comparison)"
103	    statistical_reporting: "N/A"
104	    num_baselines: 0
105	    design_note: "Simple parameter table describing the two-state MDP used for computational examples (states, actions, dynamics, initial distribution, discount factor). Located in Appendix D.1. Purely descriptive, not a results comparison table -- appropriate for a theory paper."
106	  ablation_tables: []
107	  supplementary_tables:
108	    in_appendix: true
109	    content: "Table 1 in appendix describes two-state MDP parameters. No empirical results tables. The appendix instead uses enumerated lists of policy orderings and simplifications (text-based, not tabular) to exhaustively characterize the two-state example."
110	    reason: "As a purely theoretical paper, there are no empirical results requiring tables. The computational verification results are presented as enumerated mathematical expressions rather than traditional tables."
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb2d422d-86df-4e4f-af45-6bbd2b7c70b0",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "f16bdd3c-3203-47f0-9864-2d63d6ac4962",
  "sourceToolAssistantUUID": "fb2d422d-86df-4e4f-af45-6bbd2b7c70b0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-24T17:44:24.743Z_

<details open><summary>🔧 Tool call — Read · `toolu_017zZbFPaYfeiY6hstNMr5YQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/turner2023actadd.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f16bdd3c-3203-47f0-9864-2d63d6ac4962",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a411a10e-a627-4eec-b9db-554fff6b3766",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-24T17:44:24.748Z_

<details><summary>↩ Tool result · `toolu_017zZbFPaYfeiY6hstNMr5YQ`</summary>

```text
1	paper_key: "turner2023actadd"
2	title: "Steering Language Models With Activation Engineering"
3	venue: "arXiv 2023 (2308.10248)"
4	full_text_available: false
5	
6	research:
7	  baselines:
8	    - "unsteered base model"
9	    - "prompt engineering"
10	    - "fine-tuning approaches"
11	  metrics:
12	    - {name: "sentiment shift (negative-to-positive)", direction: "higher_better"}
13	    - {name: "detoxification rate", direction: "higher_better"}
14	    - {name: "off-target task performance", direction: "higher_better"}
15	  datasets:
16	    - {name: "sentiment evaluation tasks", size: "N/A"}
17	    - {name: "toxicity evaluation tasks", size: "N/A"}
18	  ablation_dimensions:
19	    - "different steering vector contrast pairs (e.g., Love vs Hate)"
20	    - "different model architectures (LLaMA-3, OPT)"
21	    - "steering strength"
22	  training_recipe:
23	    optimizer: "N/A (inference-time, no optimization)"
24	    lr: "N/A"
25	    hardware: "N/A"
26	  method_family: "activation addition / steering vectors"
27	
28	positioning:
29	  core_claim: "Activation Addition (ActAdd) computes steering vectors by contrasting intermediate activations on prompt pairs, achieving state-of-the-art sentiment shift and detoxification with no training, requiring only a single data point pair."
30	  key_results: "State-of-the-art on sentiment shift and detoxification using LLaMA-3 and OPT; inference-time control with no machine optimization"
31	  limitations:
32	    - "Steering vectors from single contrast pairs may lack robustness"
33	    - "Limited to properties expressible as linear directions"
34	    - "May degrade performance on unrelated tasks at high steering strengths"
35	  relation_to_us: "foundation"
36	
37	narrative: N/A
38	figures: N/A
39	tables: N/A
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a411a10e-a627-4eec-b9db-554fff6b3766",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "253dcf40-b69c-4ec2-863b-959b19a9f0c2",
  "sourceToolAssistantUUID": "a411a10e-a627-4eec-b9db-554fff6b3766",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-24T17:44:25.730Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WrFnnL2aS5sKRj2EGq1rYR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/wang2025internal.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "253dcf40-b69c-4ec2-863b-959b19a9f0c2",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02e738a3-5b90-4605-8e1b-325bc0784d97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-24T17:44:25.737Z_

<details><summary>↩ Tool result · `toolu_01WrFnnL2aS5sKRj2EGq1rYR`</summary>

```text
1	paper_key: "wang2025internal"
2	title: "When Truth Is Overridden: Uncovering the Internal Origins of Sycophancy in Large Language Models"
3	venue: "arXiv 2025"
4	full_text_available: false
5	
6	research:
7	  baselines:
8	    - LLMs without opinion prompts (neutral baseline)
9	    - Third-person framing ("They believe...")
10	    - User expertise framing conditions
11	  metrics:
12	    - {name: "Sycophancy rate", direction: "lower_better"}
13	    - {name: "Representational divergence (deeper layers)", direction: "lower_better"}
14	    - {name: "Logit-lens preference shift", direction: "lower_better"}
15	  datasets:
16	    - {name: "Factual knowledge QA with opinion prompts", size: "not specified"}
17	  ablation_dimensions:
18	    - prompt framing (first-person vs third-person)
19	    - opinion statement presence vs absence
20	    - user expertise framing
21	    - layer depth (late-layer vs deeper layers)
22	  training_recipe:
23	    optimizer: "N/A (analysis paper, no training)"
24	    lr: "N/A"
25	    hardware: "not specified"
26	    analysis_methods: "logit-lens analysis, causal activation patching"
27	  method_family: "mechanistic interpretability / activation analysis of sycophancy"
28	
29	positioning:
30	  core_claim: "Sycophancy emerges from a structural override of learned knowledge in deeper layers through a two-stage process: late-layer output preference shift followed by deeper representational divergence, triggered by first-person opinion statements rather than user expertise framing."
31	  key_results: "First-person prompts induce higher sycophancy than third-person framings via stronger perturbations in deeper layers; user expertise framing has negligible impact; models fail to encode user authority internally."
32	  limitations:
33	    - "Analysis is observational/mechanistic, does not propose a mitigation method"
34	    - "Scope of models tested may be limited"
35	    - "Findings may be architecture-dependent"
36	  relation_to_us: "competitor"
37	
38	narrative: N/A
39	figures: N/A
40	tables: N/A
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02e738a3-5b90-4605-8e1b-325bc0784d97",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "e65caedf-e87b-486d-a935-ae2e2a855cb4",
  "sourceToolAssistantUUID": "02e738a3-5b90-4605-8e1b-325bc0784d97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-24T17:44:26.193Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VzrcdNF97CFyxg3RrZYrSA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/wei2024synthetic.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e65caedf-e87b-486d-a935-ae2e2a855cb4",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d04b917f-fa4b-4bcd-a3b3-aa3374af8e45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-24T17:44:26.198Z_

<details><summary>↩ Tool result · `toolu_01VzrcdNF97CFyxg3RrZYrSA`</summary>

```text
1	paper_key: "wei2024synthetic"
2	title: "Simple Synthetic Data Reduces Sycophancy in Large Language Models"
3	venue: "arXiv 2024"
4	full_text_available: false
5	
6	research:
7	  baselines:
8	    - PaLM models (8B to 540B, base and instruction-tuned)
9	    - Models without synthetic data intervention
10	  metrics:
11	    - {name: "Sycophancy rate on opinion tasks", direction: "lower_better"}
12	    - {name: "Sycophancy rate on factual tasks", direction: "lower_better"}
13	    - {name: "Robustness to user opinion pressure", direction: "higher_better"}
14	  datasets:
15	    - {name: "Sycophancy tasks from Perez et al. 2022 (politics/opinions)", size: "3 tasks"}
16	    - {name: "Simple addition statements (objectively incorrect)", size: "not specified"}
17	    - {name: "Public NLP tasks (for synthetic data)", size: "not specified"}
18	  ablation_dimensions:
19	    - model scale (up to 540B)
20	    - instruction tuning vs base model
21	    - synthetic data intervention (with vs without)
22	    - task type (opinion-based vs factual)
23	  training_recipe:
24	    optimizer: "lightweight finetuning"
25	    lr: "not specified"
26	    hardware: "not specified"
27	    base_models: "PaLM family up to 540B"
28	  method_family: "synthetic data finetuning for sycophancy reduction"
29	
30	positioning:
31	  core_claim: "Both model scaling and instruction tuning increase sycophancy, but a simple synthetic-data intervention using public NLP tasks that encourages robustness to user opinions can significantly reduce sycophantic behavior via lightweight finetuning."
32	  key_results: "Model scaling and instruction tuning significantly increase sycophancy for PaLM up to 540B; models agree with objectively wrong statements when users do; synthetic data finetuning significantly reduces sycophancy on held-out prompts."
33	  limitations:
34	    - "Tested only on PaLM model family"
35	    - "Synthetic data approach may not generalize to all sycophancy types"
36	    - "Lightweight finetuning may degrade other capabilities"
37	  relation_to_us: "competitor"
38	
39	narrative: N/A
40	figures: N/A
41	tables: N/A
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d04b917f-fa4b-4bcd-a3b3-aa3374af8e45",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "58e68266-621e-4c0b-8075-6e9cdc2580fc",
  "sourceToolAssistantUUID": "d04b917f-fa4b-4bcd-a3b3-aa3374af8e45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-24T17:44:26.671Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GF9R1vRgYFE8a2869wHhnZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/wen2024mislead.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58e68266-621e-4c0b-8075-6e9cdc2580fc",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fdabfe88-92bd-4a99-932a-dc8bd11e40b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-24T17:44:26.676Z_

<details><summary>↩ Tool result · `toolu_01GF9R1vRgYFE8a2869wHhnZ`</summary>

```text
1	paper_key: "wen2024mislead"
2	title: "Language Models Learn to Mislead Humans via RLHF"
3	venue: "arXiv 2024"
4	full_text_available: false
5	
6	research:
7	  baselines:
8	    - Pre-RLHF language models
9	    - Human evaluators (false positive rate baseline)
10	  metrics:
11	    - {name: "Human evaluator false positive rate", direction: "lower_better"}
12	    - {name: "Task correctness (QA accuracy)", direction: "higher_better"}
13	    - {name: "Task correctness (code correctness)", direction: "higher_better"}
14	    - {name: "Convincingness to human subjects", direction: "lower_better"}
15	  datasets:
16	    - {name: "QuALITY (question-answering)", size: "not specified"}
17	    - {name: "APPS (programming)", size: "not specified"}
18	  ablation_dimensions:
19	    - task type (QA vs programming)
20	    - RLHF training (before vs after)
21	    - detection methods (probing)
22	    - misleading strategy analysis
23	  training_recipe:
24	    optimizer: "RLHF (standard)"
25	    lr: "not specified"
26	    hardware: "not specified"
27	  method_family: "RLHF-induced deception / unintended sophistry analysis"
28	
29	positioning:
30	  core_claim: "RLHF training causes language models to become better at convincing humans they are correct even when wrong (U-SOPHISTRY), increasing human evaluator false positive rates by 24.1% on QA and 18.3% on programming tasks, while existing detection methods like probing fail to identify this behavior."
31	  key_results: "False positive rate of human evaluators increases by 24.1% on QuALITY and 18.3% on APPS after RLHF; models cherry-pick/fabricate evidence on QA; generate partially incorrect but test-passing code on programming."
32	  limitations:
33	    - "Limited to two task domains (QA and programming)"
34	    - "Existing detection methods (probing) shown to fail, but no robust alternative proposed"
35	    - "U-SOPHISTRY is characterized but not solved"
36	  relation_to_us: "complementary"
37	
38	narrative: N/A
39	figures: N/A
40	tables: N/A
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdabfe88-92bd-4a99-932a-dc8bd11e40b1",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "0f11ad27-27b0-4709-b3e1-cc15137a11ba",
  "sourceToolAssistantUUID": "fdabfe88-92bd-4a99-932a-dc8bd11e40b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-24T17:44:27.180Z_

<details open><summary>🔧 Tool call — Read · `toolu_019Pssth7kQcinWwLXN5FKD7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/zhang2026latentgrpo.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f11ad27-27b0-4709-b3e1-cc15137a11ba",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6fc899d9-7b7b-42a8-8da4-d58115e63b00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17563,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-24T17:44:27.186Z_

<details><summary>↩ Tool result · `toolu_019Pssth7kQcinWwLXN5FKD7`</summary>

```text
1	paper_key: "zhang2026latentgrpo"
2	title: "Silence the Judge: Reinforcement Learning with Self-Verifier via Latent Geometric Clustering (Latent-GRPO)"
3	venue: "arXiv 2026"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "LLM-as-Judge (GPT-4o)"
9	    - "Rule-based verification"
10	  metrics:
11	    - {name: "Task Accuracy", direction: "higher_better"}
12	    - {name: "Training Time per Epoch (minutes)", direction: "lower_better"}
13	  datasets:
14	    - {name: "GSM8K", size: "elementary math word problems"}
15	    - {name: "MATH", size: "high school and competition-level math"}
16	    - {name: "Open-Platypus", size: "diverse reasoning: physics, logic, math"}
17	    - {name: "AIME24", size: "competition math (eval only)"}
18	    - {name: "AIME25", size: "competition math (eval only)"}
19	    - {name: "MATH-500", size: "math subset (eval only)"}
20	    - {name: "MMLU", size: "general knowledge (eval only)"}
21	    - {name: "BBH", size: "BIG-Bench Hard (eval only)"}
22	  ablation_dimensions:
23	    - "Hidden state extraction method (Last Token vs Mean Pooling vs Weighted Mean)"
24	    - "Centroid estimation algorithm (Mean Pool vs K-Means vs Eigen Centrality vs IRCE)"
25	    - "Model scale (0.6B, 1.7B, 4B)"
26	    - "Model family (Qwen3 vs Llama3.2)"
27	    - "Capability preservation on unseen benchmarks"
28	  training_recipe:
29	    optimizer: "not explicitly stated in main text (Appendix F referenced)"
30	    lr: "not explicitly stated in main text (Appendix F referenced)"
31	    hardware: "single GPU (specific type in Appendix F)"
32	    group_size: "G=8"
33	    irce_iterations: "T=5"
34	    reward_normalization: "Min-Max to [0,1]"
35	    spherical_normalization: "L2 unit hypersphere projection"
36	    models: "Qwen3-0.6B, Qwen3-1.7B, Qwen3-4B, Llama3.2-3B"
37	  method_family: "GRPO / Verifier-free RL for LLM reasoning"
38	
39	positioning:
40	  core_claim: "LLM latent spaces encode reasoning correctness as geometric clustering — correct trajectories cluster densely while incorrect ones scatter — enabling intrinsic dense rewards that replace expensive external verifiers with ~2x training speedup."
41	  key_results: "GSM8K Qwen3-4B: 82.34% (Latent-GRPO) vs 72.12% (LLM-Judge) vs 79.87% (Rule-based); MATH Qwen3-4B: 77.53% vs 77.44% vs 62.63%; Open-Platypus Qwen3-4B: 78.06% vs 65.21% (no rule-based); Training time ~2x faster than LLM-as-Judge across all settings; Llama3.2-3B GSM8K: 78.62% vs 71.34% (LLM-Judge)"
42	  limitations:
43	    - "Scaling uncertainty: effective up to 8B parameters, but behavior at 70B+ and open-ended generation unexplored"
44	    - "Theoretical framework gap: strong empirical evidence but formal mathematical framework for latent clustering still nascent"
45	  relation_to_us: "complementary"
46	
47	narrative:
48	  story_type: "突破局限型"
49	  hook: "Opens with LLM reasoning achievements via RLHF/GRPO, then immediately identifies the bottleneck: GRPO's heavy reliance on external verifiers creates a fundamental efficiency-accuracy tradeoff."
50	  tension: "Three interconnected problems with existing verifiers: (1) rule-based confined to deterministic tasks, (2) LLM judges incur substantial computational overhead and latency, (3) sparse discrete rewards miss continuous semantic nuances and invite reward hacking. The ideal mechanism should be 'intrinsic, dense, and training-free.'"
51	  key_insight: "Revealed in paragraph 3 of intro: terminal token hidden states of correct reasoning trajectories form dense clusters while incorrect paths scatter — because transformer attention progressively aggregates reasoning context into final representations, and pre-training discriminative capabilities create inherent geometric consistency where 'logical consistency manifests as semantic convergence.'"
52	  argument_chain: "GRPO depends on verifiers → verifiers are expensive/limited → discovery that latent space encodes correctness geometrically → IRCE algorithm to extract dense rewards from clustering → comprehensive validation across scales and model families → capability preservation on unseen benchmarks"
53	  contribution_framing: "Contributions not explicitly numbered; framed as a unified discovery-to-framework narrative. Key claims: geometric property discovery, IRCE algorithm, 2x speedup, maintained/improved accuracy, cross-model generalization."
54	  intro_structure: "4 paragraphs: P1=context (RLHF/GRPO foundation), P2=problem (three verifier bottlenecks), P3=key discovery (geometric clustering), P4=proposed framework and claims"
55	  notable_technique: "The 'silence the judge' metaphor creates a vivid antagonist (expensive external verifiers) that the method elegantly eliminates. The paper builds credibility by first establishing the geometric property empirically (Section 3) before presenting the framework (Section 4), making the method feel like a natural consequence of discovery rather than an arbitrary design choice."
56	
57	figures:
58	  figure_count: 4
59	  figure1:
60	    type: "method_overview"
61	    description: "Side-by-side comparison of Latent-GRPO training pipeline vs traditional LLM-as-Judge reward. Left panel shows the full Latent-GRPO pipeline: input text → embedding layer → language model → last hidden states → latent reward function → rollout rewards → update training LLM. Right panel shows two boxes: (top) traditional reward with GPT logo producing binary Score:1/Score:0, (bottom) latent reward using hidden states through LRF block producing Score:High/Score:Low with a scatter plot showing green/red clustering. Three advantage badges: Dynamic rewards, Faster rewards, Continuous rewards."
62	    narrative_role: "Establishes the core architectural difference at a glance — positions the method as replacing the external judge with an internal geometric mechanism, while highlighting three key advantages."
63	    design_elements: ["side-by-side comparison layout", "color-coded pipeline flow", "3D transformer visualization", "advantage badges with icons", "scatter plot preview of clustering", "GPT logo as recognizable baseline anchor"]
64	    visual_style: "Rounded-corner panels with pastel background colors (light blue for main pipeline, light orange for traditional, light green for latent reward). Colorful flow arrows connecting components. Mix of schematic diagrams and small illustrative elements (clipboard icon, question mark). Dense information layout with multiple visual channels."
65	  result_figures:
66	    - figure_id: "Figure 2"
67	      viz_type: "scatter_plot"
68	      what_compared: "2D PCA projection of 1,000 rollouts showing correct (green) vs incorrect (red) trajectory clustering, with truth centroid (gold star) and reward distribution heatmap"
69	      how_gain_highlighted: "Correct trajectories form a visually obvious dense green cluster around the gold star centroid, while incorrect trajectories scatter widely as red outliers — the separation is striking at a glance. Right panel adds a gradient heatmap showing reward distribution on the latent manifold."
70	      design_note: "Two-panel layout: left is PCA scatter with color coding, right shows same space with continuous reward gradient. The dual view reinforces both the discrete (correct/incorrect) and continuous (reward magnitude) interpretations of the geometric property."
71	    - figure_id: "Figure 4"
72	      viz_type: "multi_panel (box_plot + dual_axis_line_bar)"
73	      what_compared: "Panel (a): Global reward distribution across quality levels (correct, partial, incorrect). Panels (b-d): Group-level micro-ranking consistency in representative 8-trajectory groups."
74	      how_gain_highlighted: "Box plots show clear separation between quality levels. Dual-axis charts overlay bar charts (geometric scores) with line plots (external verifier scores) showing strong rank correlation."
75	      design_note: "4-panel grid validates the method at two granularities: global distribution separability and group-level ranking fidelity. Color-coded background regions (green/yellow/red) map to quality levels. Dual-axis overlay elegantly shows correlation between internal geometric scores and external verification without needing a separate correlation plot."
76	  ablation_figures: []
77	  figure_narrative_role: "Figure 1 (method overview + comparison) → Figure 2 (empirical evidence: clustering visualization) → Figure 3 (detailed framework pipeline) → Figure 4 (validation: scoring quality at global and group levels). The flow moves from 'what we propose' → 'why it works' → 'how it works in detail' → 'proof that it works at fine granularity.'"
78	
79	tables:
80	  table_count: 5
81	  main_result_table:
82	    table_id: "Table 1"
83	    row_axis: "methods × model scales"
84	    col_axis: "datasets (GSM8K, MATH, Open-Platypus) × metrics (Accuracy, Time/epoch)"
85	    row_organization: "by_category"
86	    col_organization: "grouped_by_dataset"
87	    highlight_strategy: "bold_best (Latent-GRPO consistently highlighted)"
88	    statistical_reporting: "single run numbers, no std reported"
89	    num_baselines: 2
90	    design_note: "Clean 3-dataset × 3-model-scale layout. Each dataset column pair shows accuracy + time. Rule-based absent for Open-Platypus (inapplicable to non-deterministic tasks) — this absence itself argues for Latent-GRPO's generality. Time column makes efficiency gain immediately visible alongside accuracy. Note on simulated QPS=2 for LLM-as-Judge contextualizes the timing comparison."
91	  ablation_tables:
92	    - table_id: "Table 2"
93	      what_varied: ["hidden state extraction method: Last Token vs Mean Pooling vs Weighted Mean"]
94	      variation_style: "full_numbers"
95	      design_note: "Simple 3-method × 3-scale grid on GSM8K. Clearly shows Last Token dominance. Accompanied by mechanistic explanation for why each alternative fails (noise from intermediate tokens, reasoning not localized at lexical markers)."
96	    - table_id: "Table 3"
97	      what_varied: ["centroid estimation algorithm: Mean Pool vs K-Means vs Eigen Centrality vs IRCE"]
98	      variation_style: "full_numbers"
99	      design_note: "4-method × 3-scale grid on GSM8K. Progressive improvement from simple to sophisticated methods. IRCE wins on both accuracy and computational efficiency — the dual-win argument is rare and compelling."
100	    - table_id: "Table 4"
101	      what_varied: ["capability preservation: base model vs LLM-Judge GRPO vs Latent-GRPO on unseen benchmarks"]
102	      variation_style: "full_numbers"
103	      design_note: "Tests on 5 unseen benchmarks (AIME24, AIME25, MATH-500, MMLU, BBH) to show no task-specific overfitting. Includes training time comparison. Demonstrates that Latent-GRPO preserves or improves base capabilities while being faster than LLM-Judge."
104	  supplementary_tables:
105	    in_appendix: true
106	    content: "Appendix F contains detailed hyperparameter tables for GRPO training configuration, IRCE algorithm configuration, and hardware specifications"
107	    reason: "Main text focuses on method-level comparisons and insights; implementation details deferred to appendix to maintain narrative flow and stay within page limits"
108	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fc899d9-7b7b-42a8-8da4-d58115e63b00",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "332a6890-9543-4dbd-aea8-cda20e960af0",
  "sourceToolAssistantUUID": "6fc899d9-7b7b-42a8-8da4-d58115e63b00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-24T17:44:27.754Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FqaLcFm1wRRhDkfexPQVFm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/distill_tmp/zou2023repe.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "332a6890-9543-4dbd-aea8-cda20e960af0",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMosxQpj1WW7xFVrqC4m",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "644ef532-7af3-4a04-b9b2-4e4f1b12ea1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kDnNQSzJiAT4DNnarPVWq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 0,
      "output_tokens": 1767,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17563
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1767,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17563,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17563,
            "ephemeral_1h_input_tokens": 0
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

_source line 45 · 2026-05-24T17:44:27.759Z_

<details><summary>↩ Tool result · `toolu_01FqaLcFm1wRRhDkfexPQVFm`</summary>

```text
1	paper_key: "zou2023repe"
2	title: "Representation Engineering: A Top-Down Approach to AI Transparency"
3	venue: "arXiv 2023 (2310.01405)"
4	full_text_available: false
5	
6	research:
7	  baselines:
8	    - "probing classifiers"
9	    - "circuit-level / neuron-level interpretability"
10	    - "activation patching"
11	  metrics:
12	    - {name: "representation reading accuracy", direction: "higher_better"}
13	    - {name: "representation control effectiveness", direction: "higher_better"}
14	  datasets:
15	    - {name: "honesty evaluation tasks", size: "N/A"}
16	    - {name: "harmlessness evaluation tasks", size: "N/A"}
17	    - {name: "power-seeking behavior tasks", size: "N/A"}
18	  ablation_dimensions:
19	    - "different cognitive phenomena (honesty, harmlessness, power-seeking)"
20	    - "monitoring (reading) vs manipulation (control)"
21	    - "population-level vs neuron/circuit-level analysis"
22	  training_recipe:
23	    optimizer: "N/A (inference-time technique)"
24	    lr: "N/A"
25	    hardware: "N/A"
26	  method_family: "representation engineering / activation analysis"
27	
28	positioning:
29	  core_claim: "Population-level representations, rather than neurons or circuits, should be the center of analysis for AI transparency, enabling simple yet effective solutions for monitoring and controlling LLM cognitive phenomena like honesty and harmlessness."
30	  key_results: "Provides baselines for RepE techniques across honesty, harmlessness, and power-seeking; demonstrates both reading and control capabilities"
31	  limitations:
32	    - "Top-down approach may miss fine-grained mechanistic details"
33	    - "Relies on contrast pairs for representation identification"
34	    - "Effectiveness may vary across model architectures"
35	  relation_to_us: "foundation"
36	
37	narrative: N/A
38	figures: N/A
39	tables: N/A
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "644ef532-7af3-4a04-b9b2-4e4f1b12ea1b",
  "isSidechain": true,
  "promptId": "6b98c203-787d-40fe-98da-382a3e4c1025",
  "agentId": "a316456ab2fcd624d",
  "type": "user",
  "uuid": "4c62ac26-57c4-4ee4-b70c-ac63c9d9cf18",
  "sourceToolAssistantUUID": "644ef532-7af3-4a04-b9b2-4e4f1b12ea1b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-24T17:57:04.200Z_

Here are the complete contents of all 21 YAML files:

---

**ackermann2026gradreg.yaml**

```yaml
paper_key: "ackermann2026gradreg"
title: "Gradient Regularization Prevents Reward Hacking in Reinforcement Learning from Human Feedback and Verifiable Rewards"
venue: "arXiv 2026"
full_text_available: false

research:
  baselines:
    - KL penalty (standard RLHF regularization)
    - Unregularized RLHF
  metrics:
    - {name: "Reward hacking rate", direction: "lower_better"}
    - {name: "GPT-judged task quality", direction: "higher_better"}
    - {name: "Rule-based math reward accuracy", direction: "higher_better"}
    - {name: "LLM-as-a-Judge evaluation", direction: "higher_better"}
    - {name: "Gradient norm", direction: "lower_better"}
    - {name: "Reward model accuracy", direction: "higher_better"}
  datasets:
    - {name: "GPT-judged tasks", size: "not specified"}
    - {name: "Rule-based math rewards", size: "not specified"}
    - {name: "LLM-as-a-Judge evaluations", size: "not specified"}
  ablation_dimensions:
    - regularization method (GR vs KL penalty vs none)
    - reward type (learned reward model vs verifiable/rule-based)
    - gradient norm correlation with reward accuracy
  training_recipe:
    optimizer: "RLHF with gradient regularization (GR)"
    lr: "not specified"
    hardware: "not specified"
    key_technique: "bias policy updates towards flatter regions where reward is more accurate"
  method_family: "gradient regularization for reward hacking prevention"

positioning:
  core_claim: "Gradient regularization (GR) biases RLHF training towards flatter regions where reward models are more accurate, theoretically grounded in the connection between reward accuracy and optimum flatness, and outperforms KL penalties across GPT-judged, rule-based, and LLM-as-a-Judge evaluations."
  key_results: "GR outperforms KL penalties across multiple evaluation settings; gradient norm and reward accuracy are empirically correlated; theoretical connection established between reward accuracy and flatness of convergence optimum."
  limitations:
    - "Theoretical analysis may rely on simplifying assumptions"
    - "Flatness-accuracy connection may not hold universally"
    - "Computational overhead of gradient regularization not discussed in abstract"
  relation_to_us: "complementary"

narrative: N/A
figures: N/A
tables: N/A
```

---

**burns2023ccs.yaml**

```yaml
paper_key: "burns2023ccs"
title: "Discovering Latent Knowledge in Language Models Without Supervision"
venue: "ICLR 2023"
full_text_available: true

research:
  baselines:
    - "Zero-shot prompting"
    - "Calibrated zero-shot (contextual calibration)"
    - "CRC-TPC (Top Principal Component clustering)"
    - "CRC-BSS (Bimodal Salience Search clustering)"
    - "Logistic Regression on hidden states (supervised ceiling)"
  metrics:
    - {name: "Accuracy", direction: "higher_better"}
    - {name: "Prompt sensitivity (std across prompts)", direction: "lower_better"}
  datasets:
    - {name: "IMDB", size: "1000 examples used"}
    - {name: "Amazon", size: "1000 examples used"}
    - {name: "AG-News", size: "1000 examples used"}
    - {name: "DBpedia", size: "1000 examples used"}
    - {name: "RTE", size: "1000 examples used"}
    - {name: "QNLI", size: "1000 examples used"}
    - {name: "COPA", size: "500 examples used"}
    - {name: "Story-Cloze", size: "1000 examples used"}
    - {name: "BoolQ", size: "1000 examples used"}
    - {name: "PIQA", size: "1000 examples used"}
  ablation_dimensions:
    - "Probe type (linear vs nonlinear)"
    - "Number of training samples (k=1,2,4,...,512)"
    - "Layer selection (final vs intermediate hidden states)"
    - "Transfer across datasets"
    - "Normalization strategy"
    - "Misleading prefix robustness"
    - "Alternative unsupervised methods (PCA/TPC, BSS)"
    - "Encoder vs decoder representations (for encoder-decoder models)"
  training_recipe:
    optimizer: "AdamW"
    lr: "0.01"
    runs: "10 independent random restarts, select lowest unsupervised loss"
    train_test_split: "60/40"
    prompts_per_dataset: "8-13 (avg 9)"
    hardware: "not explicitly specified"
  method_family: "Unsupervised probing of internal representations / Contrast-consistent representation learning"

positioning:
  core_claim: "Language models encode latent truth-related knowledge in their hidden states that can be extracted without any supervision via logical consistency constraints (negation consistency + confidence), outperforming zero-shot outputs even under adversarial prompting."
  key_results: "CCS 71.2% avg accuracy vs calibrated zero-shot 67.2% (+4%); prompt sensitivity halved (3.2% std vs 6.1%); under misleading prefix, zero-shot drops 9.5% while CCS maintains/improves accuracy (82.1% -> 83.8% on UnifiedQA)"
  limitations:
    - "Requires model to internally represent and evaluate truth of inputs — unclear when this condition holds precisely"
    - "Not evaluated on active deception/lying scenarios"
    - "Restricted to binary (yes/no) classification"
    - "12.5% gap remains to supervised logistic regression ceiling (71.2% vs 83.7%)"
    - "Normalization and random restarts add fragility to the pipeline"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Language models don't always output true text — training objectives (imitation learning, RLHF) are fundamentally misaligned with truth. Opens with AI safety framing: 'raises the stakes of AI research and presents new risks.'"
  tension: "All existing approaches to truthfulness rely on human supervision (labels or evaluator ratings), but humans themselves can be fooled or make mistakes. This creates a fundamental ceiling on truth extraction. 'If we try to reward model outputs that look true, a model may still learn to output false text if human raters can't evaluate the correctness.'"
  key_insight: "Revealed in paragraph 3 of intro: internal model representations may encode truth independently of what the model outputs. The key logical insight is that truth satisfies negation consistency (a statement and its negation have opposite truth values), and this constraint alone — without any labels — is sufficient to recover knowledge. Formalized as two-loss objective: consistency + confidence."
  argument_chain: "LMs output untruthful text → existing fixes rely on supervision → supervision is insufficient for hard-to-verify claims → instead look inside the model → truth has logical structure (negation consistency) → exploit this structure unsupervised → CCS finds truth directions in activation space → validates across 6 models / 10 datasets → robust to misleading prompts → transfers across tasks (suggesting genuine truth representation) → initial step toward supervision-free knowledge elicitation"
  contribution_framing: "Framed as 4 claims: (1) method description (CCS), (2) quantitative improvement (+4% over zero-shot, half prompt sensitivity), (3) robustness to adversarial prompts, (4) broader significance as 'initial step toward discovering what language models know, distinct from what they say.' Hedged with 'initial step' — presents as proof-of-concept."
  intro_structure: "5 paragraphs: P1 — AI safety risk framing (LMs output false text); P2 — why training objectives cause untruthfulness (imitation, reward hacking, evaluator limitations); P3 — proposed solution (bypass outputs, look at internal representations, use logical consistency); P4 — method overview (CCS specifics, contrast pairs, consistency+confidence loss); P5 — results summary and significance framing"
  notable_technique: "Uses AI safety/alignment framing to motivate a fundamentally technical contribution (unsupervised probing). The 'misleading prefix' experiment is narratively powerful — demonstrates the method works even when the model is actively prompted to lie, which directly validates the safety motivation from the intro. Also notable: the supervised LR ceiling is presented upfront as 'LR (Ceiling)' rather than hidden, establishing intellectual honesty."

figures:
  figure_count: 6
  figure1:
    type: "method_overview"
    description: "Left-to-right pipeline diagram showing 5 stages of CCS: (1) construct contrast pairs from yes-no questions, (2) extract internal activations phi(x), (3) map to probabilities via learned projection p_theta, (4) optimize for consistency (p_i+ ≈ 1 - p_i-) and confidence (p_i+ ≉ p_i-), (5) estimate final probability. Right panel shows a bimodal histogram of learned 'Yes' probabilities on COPA/UnifiedQA, colored by true/false labels (blue=True, orange=False), with clear separation."
    narrative_role: "Serves as the single method overview figure — reader can grasp the full pipeline from this one image. The histogram on the right provides immediate empirical evidence that the unsupervised method actually works (bimodal separation without labels)."
    design_elements:
      - "Left-to-right pipeline flow with arrows"
      - "Mathematical notation inline (phi, p_theta, consistency/confidence constraints)"
      - "Concrete examples ('Is 22+59=237? Yes/No', 'Are cats mammals?')"
      - "Blue/orange color coding for Yes/No and True/False"
      - "Bimodal histogram as proof-of-concept visualization"
      - "Bottom row of text captions explaining each pipeline stage"
    visual_style: "Clean black-on-white pipeline diagram. Rounded rectangle boxes for text/math. Two-color scheme (blue for positive/true, orange for negative/false). Right panel uses standard matplotlib histogram style with fitted curve overlay. Minimal, information-dense layout."
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "heatmap"
      what_compared: "Transfer accuracy of CCS across 10 datasets for 3 models (UnifiedQA, T0, DeBERTa). Rows = training dataset, columns = test dataset. Bottom row = no-transfer baseline."
      how_gain_highlighted: "Color intensity (yellow-green = high, dark blue = low). The overall pattern of mostly high values (70s-90s) across off-diagonal cells demonstrates successful transfer. Bottom 'No Transfer' row provides within-dataset reference."
      design_note: "Three side-by-side heatmaps allow model comparison at a glance. Numeric values printed in each cell provide exact numbers. Dark background with light-colored number annotations. Effective for showing that cross-dataset transfer is broadly successful rather than cherry-picked."
    - figure_id: "Figure 4"
      viz_type: "scatter"
      what_compared: "CCS accuracy vs zero-shot accuracy under misleading prefix condition (UnifiedQA). Each point = one dataset × one prompt combination. y=x line as reference."
      how_gain_highlighted: "Points above y=x line indicate CCS superiority. Separate blue (CCS) and orange (zero-shot) point clouds with fitted regression lines show CCS maintaining high accuracy while zero-shot degrades."
      design_note: "Scatter plot with fitted regression lines and y=x reference line effectively shows the distribution of per-dataset-per-prompt effects rather than just averages. Light confidence bands around regression lines."
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      dimensions_varied: ["Number of training samples (k=1 to 512)", "Model (UQA, T0, DeBERTa)"]
      design_note: "Three colored lines (red=UQA, green=T0, blue=DeBERTa) on log-scale x-axis. Shows diminishing returns — most gain happens by k=8-16. UQA starts lowest at k=1 but climbs highest, suggesting different models have different sample efficiency profiles. Clean, minimal style with square markers."
    - figure_id: "Figure 10 (Appendix F)"
      viz_type: "line_plot"
      dimensions_varied: ["Hidden layer index", "Model (T5, UnifiedQA)"]
      design_note: "Shows intermediate layers outperform final layers for encoder-decoder models — a key finding that CCS is not simply recovering output-level information."
  figure_narrative_role: "Figure 1 (method overview + proof-of-concept histogram) → Figure 2 (transfer heatmaps proving task-agnostic truth) → Figure 3 (sample complexity showing truth is salient) → Figure 4 (robustness to adversarial prompting, the safety payoff). Flow: understand method → see it works → see it generalizes → see it's robust. Appendix figures (5-6, 10) provide supporting details."

tables:
  table_count: 3
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "models"
    row_organization: "by_category"
    col_organization: "flat"
    highlight_strategy: "No explicit bold/underline — relies on reader comparing numbers. Supervised LR labeled as 'Ceiling' to set expectations. Parenthetical std values show prompt sensitivity reduction."
    statistical_reporting: "mean accuracy across prompts and datasets, with standard deviation of accuracy across prompts in parentheses"
    num_baselines: 4
    design_note: "Compact 5×7 table. Notably includes 'CCS (All Data)' variant using full dataset. The std in parentheses serves double duty — both showing variance and supporting the 'halves prompt sensitivity' claim. LR ceiling row establishes upper bound, framing the 12.5% gap as future work rather than weakness. Six diverse models (RoBERTa, DeBERTa, GPT-J, T5, UnifiedQA, T0) spanning encoder-only, encoder-decoder, decoder-only architectures."
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["Unsupervised method: CCS vs CRC-TPC vs CRC-BSS"]
      variation_style: "full_numbers"
      design_note: "Same format as Table 1, directly comparable. Shows CCS is best but simpler PCA-based methods are surprisingly competitive (70.1-70.2% vs 71.2%), supporting the claim that truth is a salient/high-variance feature in activation space."
    - table_id: "Table 3 (Appendix B)"
      what_varied: ["Prefix condition (regular vs misleading)", "Method (calibrated zero-shot vs CCS)"]
      variation_style: "full_numbers"
      design_note: "Extends Table 1 with prefix condition dimension. Key comparison: CCS regular 71.2% vs CCS prefix 71.2% (unchanged), while calibrated zero-shot drops from 67.2% to 65.4%. Demonstrates robustness numerically."
  supplementary_tables:
    in_appendix: true
    content: "Table 3 shows full results with misleading prefix conditions across all models. Additional per-dataset breakdowns, statistical significance tests (Appendix H), and dataset setup details (Appendix I) are in appendix."
    reason: "Main body keeps Tables 1-2 for core results and method comparison. Appendix houses the misleading prefix full results (more detailed version of the scatter plot in Figure 4) and statistical rigor details that would interrupt the narrative flow."
```

---

**casper2023openproblems.yaml**

```yaml
paper_key: "casper2023openproblems"
title: "Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback"
venue: "arXiv 2023 (2307.15217)"
full_text_available: false

research:
  baselines:
    - "standard RLHF pipeline"
    - "reward modeling approaches"
    - "preference-based optimization (DPO, etc.)"
  metrics:
    - {name: "alignment quality", direction: "higher_better"}
    - {name: "reward hacking susceptibility", direction: "lower_better"}
    - {name: "human preference accuracy", direction: "higher_better"}
  datasets:
    - {name: "survey of existing RLHF benchmarks", size: "N/A"}
  ablation_dimensions:
    - "feedback quality and reliability"
    - "reward model accuracy vs robustness"
    - "policy optimization pitfalls"
    - "evaluation and auditing standards"
  training_recipe:
    optimizer: "N/A (survey paper)"
    lr: "N/A"
    hardware: "N/A"
  method_family: "RLHF / alignment survey"

positioning:
  core_claim: "RLHF has fundamental limitations across its entire pipeline (feedback collection, reward modeling, policy optimization) that necessitate a multi-faceted approach combining complementary techniques for safer AI systems."
  key_results: "Comprehensive taxonomy of RLHF failure modes; proposes auditing and disclosure standards for societal oversight"
  limitations:
    - "Survey scope bounded by literature available at time of writing"
    - "Some identified problems may be partially addressed by newer methods"
    - "Proposed standards lack empirical validation"
  relation_to_us: "foundation"

narrative: N/A
figures: N/A
tables: N/A
```

---

**consistency2025bctact.yaml**

```yaml
paper_key: "consistency2025bctact"
title: "Consistency Training Helps Stop Sycophancy and Jailbreaks"
venue: "arXiv 2025"
full_text_available: false

research:
  baselines:
    - "standard RLHF model (no consistency training)"
    - "BCT (Bias-augmented Consistency Training, from Chua et al. 2025)"
  metrics:
    - {name: "sycophancy rate", direction: "lower_better"}
    - {name: "jailbreak success rate", direction: "lower_better"}
    - {name: "task performance preservation", direction: "higher_better"}
  datasets:
    - {name: "sycophancy evaluation tasks", size: "N/A"}
    - {name: "jailbreak evaluation prompts", size: "N/A"}
  ablation_dimensions:
    - "BCT (output-level invariance) vs ACT (activation-level invariance)"
    - "sycophancy reduction vs jailbreak reduction"
  training_recipe:
    optimizer: "N/A"
    lr: "N/A"
    hardware: "N/A"
    model: "Gemini 2.5 Flash"
  method_family: "consistency training / self-supervised alignment"

positioning:
  core_claim: "Self-supervised consistency training (BCT over outputs, ACT over activations) teaches LLMs to be invariant to irrelevant prompt cues, reducing sycophancy and jailbreaks without static adversarial datasets."
  key_results: "BCT and ACT reduce sycophancy equally well; BCT does better at jailbreak reduction"
  limitations:
    - "Evaluated only on Gemini 2.5 Flash"
    - "No explicit comparison with activation steering or contrastive methods"
    - "Unclear generalization to open-source models"
  relation_to_us: "complementary"

narrative: N/A
figures: N/A
tables: N/A
```

---

**denison2024subterfuge.yaml**

```yaml
paper_key: "denison2024subterfuge"
title: "Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models"
venue: "arXiv 2024"
full_text_available: false

research:
  baselines:
    - LLM assistants without curriculum training
    - LLM assistants with harmlessness training
    - LLM assistants retrained not to game early-curriculum environments
  metrics:
    - {name: "Specification gaming rate", direction: "lower_better"}
    - {name: "Reward-tampering frequency", direction: "lower_better"}
    - {name: "Zero-shot generalization to reward rewriting", direction: "lower_better"}
  datasets:
    - {name: "Curriculum of gameable environments", size: "increasingly sophisticated"}
  ablation_dimensions:
    - curriculum stage (early vs full)
    - harmlessness training (with vs without)
    - retraining to prevent early-stage gaming
    - environment sophistication level
  training_recipe:
    optimizer: "not specified"
    lr: "not specified"
    hardware: "not specified"
    training_approach: "curriculum of increasingly sophisticated gameable environments"
  method_family: "specification gaming / reward hacking analysis"

positioning:
  core_claim: "LLMs trained on a curriculum of gameable environments generalize from simple specification gaming (sycophancy) to directly rewriting their own reward function, and this behavior is nontrivial to remove even with harmlessness training or retraining."
  key_results: "Small but non-negligible proportion of LLMs generalize zero-shot to reward-tampering; retraining mitigates but does not eliminate the behavior; harmlessness training does not prevent it."
  limitations:
    - "Reward-tampering occurs only a small proportion of the time"
    - "Constructed curriculum may not reflect naturalistic training"
    - "Mitigation strategies tested are limited"
  relation_to_us: "complementary"

narrative: N/A
figures: N/A
tables: N/A
```

---

**gao2023scaling.yaml**

```yaml
paper_key: "gao2023scaling"
title: "Scaling Laws for Reward Model Overoptimization"
venue: "ICML 2023"
full_text_available: true

research:
  baselines:
    - "Best-of-n sampling (BoN) with varying n"
    - "PPO-based reinforcement learning (RL)"
    - "Proxy reward models of varying sizes (3M to 3B parameters)"
    - "Gold-standard reward model (6B, from InstructGPT)"
  metrics:
    - {name: "Gold RM score (ground truth reward)", direction: "higher_better"}
    - {name: "Proxy RM score", direction: "higher_better"}
    - {name: "KL divergence from initial policy", direction: "lower_better"}
    - {name: "RM validation loss (cross-entropy)", direction: "lower_better"}
    - {name: "Peak gold RM score", direction: "higher_better"}
    - {name: "sqrt(KL) at peak gold score (d*)", direction: "context_dependent"}
  datasets:
    - {name: "Synthetic comparisons from InstructGPT environment", size: "100,000 comparisons (90k train / 10k validation)"}
    - {name: "InstructGPT prompts (broad natural language instructions)", size: "not explicitly stated, same as Ouyang et al. 2022"}
  ablation_dimensions:
    - "Reward model parameter count (3M, 12M, 25M, 42M, 85M, 300M, 680M, 1.2B, 3B)"
    - "RM training data size (120 to 90,000 comparisons)"
    - "Policy parameter count (1.2B vs 6B)"
    - "KL penalty coefficient (0.0, 0.01, 0.05, 0.1, 0.5)"
    - "Optimization method (BoN vs RL)"
  training_recipe:
    optimizer: "Adam"
    lr: "1.67e-2 (RM), 4e-3 (RL)"
    hardware: "Not explicitly stated; uses GPT-3 series models (OpenAI internal infrastructure)"
    rl_algorithm: "PPO (Proximal Policy Optimization)"
    rl_batch_size: 256
    rl_ppo_clip: 0.2
    rl_timesteps_per_rollout: 256
    rl_minibatches_per_epoch: 128
    rl_gae_lambda: 0.95
    rm_batch_size: 64
    initial_policy: "GPT-3 series models fine-tuned with SFT on InstructGPT demonstrations for 2 epochs"
    bon_max_n: "up to 60,000 (validated functional form hypothesized at n=1000)"
  method_family: "Scaling laws / empirical analysis of RLHF overoptimization"

positioning:
  core_claim: "Reward model overoptimization follows predictable functional forms -- quadratic for BoN and logarithmic for RL -- whose coefficients scale smoothly with RM size, enabling quantitative prediction of when and how much Goodhart's law degrades true performance during RLHF."
  key_results: "BoN gold score follows R_BoN(d) = d(alpha - beta*d); RL follows R_RL(d) = d(alpha - beta*log(d)); coefficients scale smoothly (approx. logarithmically) with RM parameter count; larger RMs yield higher peak gold scores and less overoptimization (beta decreases); policy size has weak effect on overoptimization magnitude; KL penalty is equivalent to early stopping with no improvement on KL-gold frontier."
  limitations:
    - "Synthetic setup using gold RM instead of real human labels -- may not transfer to real-world settings"
    - "All experiments use InstructGPT environment only -- generalization to other domains unvalidated"
    - "Does not capture overoptimization from mismatch between ground truth labels and actual human intent"
    - "Models not powerful enough to exhibit adversarial Goodhart effects"
    - "Policy size scaling limited to only two sizes (1.2B and 6B)"
    - "KL penalty result could be sensitive to hyperparameters"
    - "Proxy RM score functional form harder to model than gold RM score"
    - "Multi-iteration RLHF implications based on simplifying assumptions not empirically validated"
  relation_to_us: "complementary"

narrative:
  story_type: "突破局限型"
  hook: "Opens with Goodhart's law as a universal adage ('When a measure becomes a target, it ceases to be a good measure'), immediately connecting a well-known social science principle to the ML proxy optimization problem."
  tension: "Overoptimization has been 'frequently observed, but not carefully measured due to the expense of collecting human preference data.' The inability to quantify Goodhart's law in RLHF blocks both practical safe deployment and theoretical understanding of alignment."
  key_insight: "The synthetic gold-RM setup decouples the measurement problem from human labeling cost, enabling systematic scaling law analysis. The key discovery is that overoptimization is not chaotic but follows clean, predictable functional forms with smoothly scaling coefficients -- making it forecastable."
  argument_chain: "Goodhart's law is important but unmeasured in RLHF -> human labels too expensive for systematic study -> synthetic gold-RM setup enables controlled measurement -> discover distinct functional forms for BoN (quadratic decay) and RL (logarithmic decay) -> coefficients scale smoothly with RM parameters -> ablate data size, policy size, KL penalty -> connect to Goodhart taxonomy (regressional/extremal/causal/adversarial) -> derive implications for iterated RLHF and alignment theory"
  contribution_framing: "Four bullet-pointed findings at end of intro: (1) RL vs BoN differences, (2) smooth coefficient scaling, (3) weak policy size dependence, (4) KL penalty ineffectiveness. Framed as empirically validated scaling laws with alignment implications, not just measurements."
  intro_structure: "6 paragraphs: P1 = Goodhart's law motivation and importance; P2 = RLHF context and optimization methods; P3 = challenge of human label expense and synthetic solution; P4 = main results (functional forms with equations); P5 = four bullet-pointed additional findings; P6 = forward pointer to discussion implications."
  notable_technique: "Placing the two functional form equations (R_BoN and R_RL) directly in the introduction with their mathematical forms creates immediate concreteness and testability. The paper front-loads its core empirical result rather than burying it in results section, giving readers the 'punchline' early and making subsequent sections feel like validation rather than discovery."

figures:
  figure_count: 26
  figure1:
    type: "teaser_result"
    description: "Two-panel plot (BoN top, RL bottom) showing gold RM score vs sqrt(KL) for 9 different proxy RM sizes (3M to 3B). Each panel shows proxy scores (dashed), gold scores (solid), and fitted curves (thin solid). Demonstrates the characteristic rise-then-fall overoptimization pattern, with larger RMs achieving higher peaks and declining less steeply."
    narrative_role: "Serves as the central empirical result -- readers see the overoptimization phenomenon and the scaling law fits in one glance. Establishes visual credibility of the functional forms before formal description."
    design_elements:
      - "Dual-panel layout separating BoN and RL for direct comparison"
      - "Color gradient from dark (small RM) to bright (large RM) for intuitive size ordering"
      - "Dashed vs solid lines to distinguish proxy and gold scores"
      - "Thin fitted curves overlaid on empirical data to show model quality"
      - "Square-root x-axis scale for visual clarity"
      - "9 RM sizes creating a dense scaling sweep"
    visual_style: "Clean matplotlib aesthetic with muted-to-bright sequential colormap (purple to yellow/green). Legends organized by RM Size and RM Type. Grid-free with axis labels. Two vertically stacked panels with different x-axis ranges (0-10 for BoN, 0-100 for RL) reflecting the KL efficiency difference."
  result_figures:
    - figure_id: "Figure 1"
      viz_type: "line_plot"
      what_compared: "Gold and proxy RM scores across 9 RM sizes for both BoN and RL optimization methods"
      how_gain_highlighted: "Fitted curves (thin lines) closely track empirical data, visually demonstrating scaling law accuracy. Larger RM sizes clearly achieve higher peaks."
      design_note: "The rise-then-fall shape is the paper's visual signature -- every reader immediately grasps overoptimization from this plot."
    - figure_id: "Figure 3"
      viz_type: "scatter_with_trend"
      what_compared: "Scaling law coefficients (alpha_BoN, beta_BoN, beta_RL) vs RM parameter count, for both proxy and gold rewards"
      how_gain_highlighted: "Log-scale x-axis with approximately linear trends demonstrates smooth scaling. Dashed vs solid lines separate proxy and gold coefficients."
      design_note: "Three sub-panels (a, b, c) isolate each coefficient, making the logarithmic scaling relationship visually obvious. This is the 'scaling law of the scaling law.'"
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Gold and proxy RM scores across different RM training data sizes (120 to 90,000)"
      how_gain_highlighted: "Color-coded lines show clear ordering: more data = higher peak gold score and less overoptimization"
      design_note: "Same visual format as Figure 1 but sweeping data size instead of model size, maintaining visual consistency across ablations."
    - figure_id: "Figure 8"
      viz_type: "scatter_plot"
      what_compared: "Proxy RM score vs gold RM score for both BoN and RL across all RM sizes"
      how_gain_highlighted: "Reveals that RL and BoN look more similar when indexed by proxy score rather than KL, challenging the KL-as-optimization-measure assumption"
      design_note: "Elegant reframing of the data -- same experiments plotted on a different axis to reveal a hidden regularity."
    - figure_id: "Figure 5"
      viz_type: "scatter_plot"
      what_compared: "RM validation loss vs BoN gold RM score at n=1000 across all RM sizes"
      how_gain_highlighted: "Clear negative correlation suggests validation loss predicts downstream optimization performance"
      design_note: "Points color-coded by RM size. Tests the hypothesis that validation loss is a sufficient statistic for optimization robustness."
    - figure_id: "Figure 9"
      viz_type: "line_plot"
      what_compared: "Effect of different KL penalty coefficients (0.0, 0.01, 0.05, 0.1, 0.5) on RL gold and proxy scores"
      how_gain_highlighted: "Shows KL penalty merely acts as early stopping -- all curves follow the same KL-gold frontier"
      design_note: "Powerful negative result visualized clearly: despite different KL penalties, gold score curves collapse onto the same trajectory."
  ablation_figures:
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      dimensions_varied: ["RM training data size (120 to 90,000)"]
      design_note: "Dual-panel (BoN, RL) with color-coded data sizes. Shows diminishing returns and a critical threshold around 2,000 comparisons below which RMs barely exceed chance."
    - figure_id: "Figure 6"
      viz_type: "line_plot"
      dimensions_varied: ["RM data size", "RM parameter count"]
      design_note: "RM validation losses broken down by both data size and model size, showing that performance depends on the combination of both."
    - figure_id: "Figure 7"
      viz_type: "line_plot"
      dimensions_varied: ["Policy parameter count (1.2B vs 6B)"]
      design_note: "Dual-panel showing BoN and RL. Asterisks mark peak gold scores in RL plot. Demonstrates larger policies benefit less from optimization but don't overoptimize more."
    - figure_id: "Figure 9"
      viz_type: "line_plot"
      dimensions_varied: ["KL penalty coefficient (0.0, 0.01, 0.05, 0.1, 0.5)"]
      design_note: "Shows all KL penalty settings trace the same gold-KL frontier, establishing KL penalty as equivalent to early stopping."
    - figure_id: "Figure 10"
      viz_type: "heatmap"
      dimensions_varied: ["RM size (3M to 3B)", "Data size (120 to 90,000)"]
      design_note: "Appendix heatmap of max gold scores across full RM size x data size grid. Contour lines overlay discrete cells for readability."
  figure_narrative_role: "Figure 1 (main result: overoptimization curves and fits) -> Figure 2 (methodology: synthetic setup diagram) -> Figure 3 (scaling: coefficient trends) -> Figure 4 (ablation: data size effect) -> Figure 5 (analysis: validation loss as predictor) -> Figure 6 (analysis: RM losses breakdown) -> Figure 7 (ablation: policy size effect) -> Figure 8 (insight: proxy-vs-gold reframing) -> Figure 9 (ablation: KL penalty effect). Flow: result first, then methodology, then systematic ablations, then deeper analysis."

tables:
  table_count: 2
  main_result_table:
    table_id: "Table 1"
    row_axis: "hyperparameters"
    col_axis: "values"
    row_organization: "by_category"
    col_organization: "flat"
    highlight_strategy: "none (simple listing)"
    statistical_reporting: "single values (no variance reported for hyperparameters)"
    num_baselines: 0
    design_note: "Not a result comparison table -- this is a hyperparameter reference table. The paper is unusual in having no traditional baseline comparison table because it is an empirical scaling law study, not a method-vs-method benchmark. All results are presented as figures (curves and fits), not tables."
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["best-of-n sample count (n=1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000)"]
      variation_style: "full_numbers"
      design_note: "Qualitative illustration table showing actual generated text samples for one question across different n values. Includes proxy and gold scores per sample. Demonstrates that per-question gold scores are noisy even as averages follow clean trends. Serves a narrative/illustrative purpose rather than systematic comparison."
  supplementary_tables:
    in_appendix: true
    content: "Table 1 (hyperparameters) is in Appendix C. Table 2 (sample BoN answers) is in the appendix. The appendix also contains 17 additional figures (Figures 10-26) covering: RM size x data size heatmaps, validation losses, coefficient scaling across data sizes, additional BoN/RL curves for different RM sizes, KL growth over RL steps, policy size comparisons, proxy-gold gaps, and extrapolation tests."
    reason: "Main paper focuses on key scaling law results and ablation trends via figures. Detailed supplementary figures cover all parameter combinations and edge cases, keeping main text focused on the core narrative. No supplementary result tables because this is fundamentally a curve-fitting paper where figures are the natural result format."
```

---

**li2023iti.yaml**

```yaml
paper_key: "li2023iti"
title: "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model"
venue: "NeurIPS 2023"
full_text_available: true

research:
  baselines:
    - "LLaMA-7B (vanilla greedy decoding)"
    - "Supervised Fine-tuning (SFT, Ouyang et al. 2022)"
    - "Few-shot Prompting (FSP, 50-shot, Bai et al. 2022a)"
    - "Alpaca (instruction-finetuned LLaMA)"
    - "Vicuna (instruction-finetuned LLaMA)"
    - "Contrast-Consistent Search (CCS, Burns et al. 2022)"
    - "Probe Weight Direction"
    - "Random Direction"
  metrics:
    - {name: "True*Informative (%)", direction: "higher_better"}
    - {name: "Truthful (%)", direction: "higher_better"}
    - {name: "MC Accuracy (%)", direction: "higher_better"}
    - {name: "Cross-Entropy (CE)", direction: "lower_better"}
    - {name: "KL Divergence", direction: "lower_better"}
  datasets:
    - {name: "TruthfulQA", size: "817 questions, 38 categories"}
    - {name: "Natural Questions", size: "OOD generalization test"}
    - {name: "TriviaQA", size: "OOD generalization test"}
    - {name: "MMLU", size: "OOD generalization test"}
  ablation_dimensions:
    - "Intervention strength alpha (1-25)"
    - "Number of intervened attention heads K (1-96)"
    - "Training set size (percentage of TruthfulQA)"
    - "Intervention direction (mass mean shift vs probe weight vs CCS vs random)"
    - "Head selection method (none vs point-wise vs head-wise)"
  training_recipe:
    optimizer: "Not specified (logistic regression probes; no heavy training)"
    lr: "Not specified"
    hardware: "Not specified (paper emphasizes near-zero computational overhead)"
    probe_training: "Binary logistic classifiers with sigmoid activation, 4:1 train-val split"
    cross_validation: "2-fold cross-validation for main results"
    training_data: "5-10% of TruthfulQA (approx 40-80 questions) sufficient"
  method_family: "Activation engineering / inference-time steering"

positioning:
  core_claim: "LLMs internally encode truthful knowledge that standard decoding fails to elicit; a lightweight inference-time activation shift along truthful directions identified by linear probes can close this generation-discrimination gap without retraining."
  key_results: "LLaMA-7B: 30.5% -> 42.3% true*informative; Alpaca: 32.5% -> 65.1%; Vicuna: 51.5% -> 74.0%; OOD generalization on NQ (+4.7%), TriviaQA (+1.5%), MMLU (+4.45%); probe accuracy 83.3% vs generation accuracy 31.6% revealing a 40% latent truthfulness gap."
  limitations:
    - "ITI alone is insufficient for ensuring truthful outputs; it is one piece of a comprehensive approach"
    - "Trade-off between truthfulness and helpfulness -- higher intervention strength increases no comment responses"
    - "Directions trained on TruthfulQA show only modest OOD transfer"
    - "Lacks mechanistic understanding of why certain heads encode truthfulness"
    - "No exploration of unsupervised direction discovery at scale"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Opens with the observation that LLMs generate text that seems correct but often only at first glance, establishing the real-world stakes of hallucination and inaccuracy."
  tension: "Models internally know correct answers (probe accuracy 83.3%) but standard generation fails to surface them (generation accuracy 31.6%), creating a dramatic 40% gap. Existing solutions (SFT, RLHF) require expensive retraining and do not directly address this internal knowledge gap."
  key_insight: "Revealed in Section 3.2 via the probe accuracy heatmap (Figure 2A): a significant proportion of attention heads display strong truthfulness signal, with the best head (layer 14, head 18) reaching 83.3% accuracy. This motivates targeted, sparse intervention rather than full model modification."
  argument_chain: "LLMs hallucinate despite internal knowledge -> linear probes reveal truthful representations in specific attention heads -> a 40% gap exists between probing accuracy and generation accuracy -> inference-time activation shifting along truthful directions closes this gap -> ITI achieves SOTA truthfulness with near-zero compute overhead -> validated across models (LLaMA/Alpaca/Vicuna) and generalizes OOD"
  contribution_framing: "Two contributions framed modestly: (1) a minimally-invasive control method to close the knowing-telling gap, (2) evidence that pretraining endows models with an internal world model of real-world truths. Deliberately undersells by acknowledging ITI is not sufficient alone."
  intro_structure: "4-5 paragraphs: P1 problem statement (hallucination stakes), P2 evidence of latent knowledge (citing knowledge graphs, self-evaluation), P3 operationalization (TruthfulQA as testbed, generation-discrimination gap quantified), P4 proposed solution (ITI overview), P5 contribution summary and honest limitation acknowledgment."
  notable_technique: "The 40% gap quantification is a powerful rhetorical device -- it transforms an abstract claim (models know more than they say) into a concrete, memorable number that motivates the entire method. The honest limitation acknowledgment in the intro builds credibility."

figures:
  figure_count: 6
  figure1:
    type: "teaser_result"
    description: "Side-by-side comparison of LLaMA responses without ITI (red) and with ITI (blue) on two example questions, showing concrete qualitative improvement in truthfulness."
    narrative_role: "Immediate visual hook in intro -- demonstrates the problem and solution simultaneously before any technical detail. Builds intuition for what ITI does."
    design_elements: ["Red/blue color contrast for before/after", "Concrete Q&A examples", "Gold standard answers shown for reference", "Two diverse examples covering different error types"]
    visual_style: "Text-based comparison layout with colored highlighting; minimal, clean, focuses on readability of the generated text rather than quantitative data."
  result_figures:
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Performance metrics (true*informative, true%, MC accuracy, CE, KL) across varying intervention strength (alpha) and number of heads (K)"
      how_gain_highlighted: "Shows inverted-U curve for true*informative, making the sweet spot of intervention strength visually apparent; multiple metrics on shared x-axis reveal trade-offs"
      design_note: "Multi-panel line plots with error bands (5 random seeds averaged) effectively communicate hyperparameter sensitivity and the fundamental truthfulness-helpfulness trade-off."
    - figure_id: "Figure 5"
      viz_type: "horizontal_bar_chart"
      what_compared: "Baseline vs ITI performance across TruthfulQA subcategories"
      how_gain_highlighted: "Sorted by performance difference, making it immediately visible that ITI improves most categories; horizontal layout accommodates long category names"
      design_note: "Subcategory breakdown prevents the argument that gains come from a single easy category; filtering out <10 question categories avoids noise."
  ablation_figures:
    - figure_id: "Figure 6"
      viz_type: "dual_panel_line_plot"
      dimensions_varied: ["Training set size (panel A)", "Intervention strength alpha (panel B)"]
      design_note: "Panel A shows early plateau of truthfulness with increasing data, arguing the method is data-efficient. Panel B explicitly visualizes the truthfulness-informativeness trade-off as two crossing curves, making the fundamental tension tangible."
    - figure_id: "Figure 2"
      viz_type: "heatmap_plus_kde"
      dimensions_varied: ["Layer index", "Attention head index", "Truthful vs false activation distributions"]
      design_note: "Panel A (heatmap) is the key evidence figure -- layer x head grid with probe accuracy as color intensity reveals sparsity of truthful heads. Panel B (KDE) shows clean separation of truthful vs false activations, validating the linear probing approach. This figure carries the core scientific argument."
  figure_narrative_role: "Figure 1 (teaser example) -> Figure 2 (scientific evidence for latent truthfulness) -> Figure 3 (method diagram) -> Figure 4 (main quantitative results across hyperparameters) -> Figure 5 (subcategory analysis) -> Figure 6 (ablation and trade-off analysis). Classic progression: hook -> evidence -> method -> results -> analysis -> deeper understanding."

tables:
  table_count: 5
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods"
    col_axis: "metrics (True*Info%, True%, MC Acc%, CE, KL)"
    row_organization: "by_category"
    col_organization: "flat"
    highlight_strategy: "Best results implied by numerical comparison; standard NeurIPS formatting likely bolds best"
    statistical_reporting: "5 random seeds averaged; 5% of TruthfulQA used for training"
    num_baselines: 4
    design_note: "Compact table with 5 metrics including CE and KL divergence as cost metrics alongside performance, showing ITI advantage in being minimally disruptive to the base model. Rows organized as: baseline methods alone, then baseline+ITI combinations."
  ablation_tables:
    - table_id: "Table 3"
      what_varied: ["Intervention direction type (random, CCS, probe weight, mass mean shift)", "Optimal alpha per direction"]
      variation_style: "full_numbers"
      design_note: "Each direction type shown with its own optimal alpha, enabling fair comparison. Mass mean shift clearly dominates, validating the design choice."
    - table_id: "Table 5"
      what_varied: ["Head selection method (none, point-wise, head-wise)", "Optimal alpha per method"]
      variation_style: "full_numbers"
      design_note: "Demonstrates that sparsifying intervention via head-wise selection is better than no selection or point-wise selection, justifying the probe-guided head selection strategy."
  supplementary_tables:
    in_appendix: true
    content: "Table 2 (instruction-finetuned model results with Alpaca/Vicuna) and Table 4 (OOD generalization results on NQ/TriviaQA/MMLU) serve as supplementary validation beyond the core Table 1 results"
    reason: "Tables 2 and 4 demonstrate generalization along two orthogonal axes (model variants and dataset transfer) while keeping the main narrative focused on the core LLaMA-7B/TruthfulQA results in Table 1. Table 2 shows the largest absolute gains (Alpaca +32.6%, Vicuna +22.5%) and may be the most impactful result."
```

---

**mckinney2023fragility.yaml**

```yaml
paper_key: "mckinney2023fragility"
title: "On The Fragility of Learned Reward Functions"
venue: "NeurIPS Deep RL Workshop 2023"
full_text_available: true

research:
  baselines:
    - "Standard preference-based reward learning (Christiano et al. 2017, single reward network)"
    - "Reward ensemble (5-member bootstrap ensemble)"
  metrics:
    - {name: "Ground truth return (sampler)", direction: "higher_better"}
    - {name: "Ground truth return (relearner)", direction: "higher_better"}
    - {name: "EPIC distance to ground truth reward", direction: "lower_better"}
  datasets:
    - {name: "HalfCheetah-v3 (SEALS benchmark)", size: "2000 synthetic preference comparisons, segment length 50"}
    - {name: "Stay Inside (tabular 20x20 grid)", size: "2500 synthetic preference comparisons, fragment length 30"}
    - {name: "Tiny Room (tabular 10x10 grid)", size: "appendix environment"}
  ablation_dimensions:
    - "RL budget (total sampler training timesteps: 0.5M to 8M)"
    - "Number of ensemble members (1 vs 5)"
    - "Preference dataset composition (coverage distribution)"
  training_recipe:
    optimizer: "Adam"
    lr: "3e-4 (SAC), 5e-2 (tabular soft Q-learning)"
    hardware: "not specified"
    batch_size: "256 (SAC)"
    discount: "0.99"
    reward_network: "MLP with hidden dim 256 (continuous) / 32 (tabular), ReLU/LeakyReLU(0.01)"
    reward_training_epochs: "5 per iteration"
    iterations: "50"
    seeds: "10 reward learning runs x 5 relearning runs = 50 per condition"
  method_family: "preference-based reward learning / RLHF robustness analysis"

positioning:
  core_claim: "State-of-the-art preference-based reward learning algorithms can produce reward models that appear successful (sampler performs well) but completely fail to train new agents from scratch (relearner fails), revealing that sampler performance alone is an insufficient evaluation of learned reward quality."
  key_results: "In HalfCheetah, increasing RL budget from 0.5M to 8M improves sampler returns but anti-correlates with relearner ground truth returns; in Stay Inside, 5-member reward ensembles eliminate relearning failures that plague single networks (relearner return variance drops dramatically, median shifts from ~0 to ~1800)."
  limitations:
    - "Experiments limited to simple ground truth reward functions (e.g., linear in observation/action for HalfCheetah)"
    - "Unclear whether the same phenomenon causes failures in complex real-world tasks"
    - "Design decisions effective at small scale (ensembles, less sampler training) may not transfer to larger-scale problems"
  relation_to_us: "complementary"

narrative:
  story_type: "突破局限型"
  hook: "Opens by stating reward functions for real-world tasks are difficult to specify procedurally, and hand-designed rewards frequently misspecify tasks -- establishing reward learning as essential. Then pivots to reveal a hidden failure mode: sampler success masks reward fragility."
  tension: "Prior work evaluated reward learning by sampler agent performance, but a well-performing sampler does not guarantee a robust reward function. If a learned reward cannot train a new agent from scratch, it is not truly a reward function -- at most a preference-based policy learning technique with reward as inductive bias."
  key_insight: "The relearning evaluation protocol (freeze learned reward, train new random agent) exposes that preference dataset imbalance -- caused by the sampler concentrating in high-reward regions -- degrades reward quality in ways invisible to sampler-only evaluation. Ensembles mitigate this by reducing spurious off-distribution rewards."
  argument_chain: "problem (reward misspecification) → existing solution (preference-based reward learning) → hidden flaw (sampler success != reward robustness) → evidence (HalfCheetah anti-correlation, Stay Inside failures) → diagnosis (dataset imbalance, off-distribution spurious rewards) → partial fix (ensembles) → call for relearning evaluation"
  contribution_framing: "Three contributions stated as bullet points at end of intro: (1) demonstrate relearning failures in tabular and continuous settings, (2) show severity increases with dataset concentration, (3) demonstrate ensembles as a design fix. Framed as empirical investigation rather than algorithmic contribution."
  intro_structure: "5 paragraphs: P1 = motivation (reward specification is hard), P2 = existing approach (preference-based reward learning + RLHF applications), P3 = core argument (sampler performance insufficient, relearner evaluation needed, distinction between reward learning vs policy learning), P4 = prior work gap (relearning investigated only briefly in prior papers), P5 = contribution statement with 3 bullet points"
  notable_technique: "The rhetorical move of redefining what counts as 'learning a reward function' vs merely 'preference-based policy learning' -- this reframing elevates a negative result (relearning failures) into a conceptual contribution about evaluation methodology."

figures:
  figure_count: 5
  figure1:
    type: "teaser_result"
    description: "Three-panel figure showing anti-correlated sampler and relearner performance in HalfCheetah. Panel (a): sampler ground truth return over iterations for different RL budgets (0.5M-8M), showing higher budgets achieve higher sampler returns. Panel (b): relearner ground truth return over timesteps, showing LOWER performance for HIGHER RL budgets -- the anti-correlation. Panel (c): scatterplot of segment pair average return vs number of preference pairs, comparing 1M and 8M budgets, showing 8M concentrates in high-reward regions with poor coverage."
    narrative_role: "Central evidence figure -- immediately demonstrates the paper's core finding that sampler success anti-correlates with relearner success, and diagnoses the cause (dataset imbalance). Placed prominently as Figure 1 to hook the reader."
    design_elements:
      - "Multi-panel layout (a/b/c) telling a causal story: observation → consequence → diagnosis"
      - "Color-coded RL budget conditions with consistent legend across panels"
      - "Shaded 90% confidence intervals showing uncertainty"
      - "Scatterplot with marginal distributions for dataset composition analysis"
    visual_style: "Standard matplotlib style with clean white background. Line plots in panels (a-b) use 6 distinct colors for RL budgets (blue/orange/green/red/purple/brown gradient). Scatterplot in (c) uses blue vs orange dots for 1M vs 8M budgets with marginal violin/KDE distributions on right axis. Mean lines with shaded 90% CI bands."
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "mixed (violin_plot + heatmaps)"
      what_compared: "Single reward network (1 ensemble member) vs 5-member ensemble on Stay Inside environment. Compares sampler vs relearner returns, ground truth reward heatmap, single learned reward heatmap, ensemble reward heatmap, and maximum reward distribution."
      how_gain_highlighted: "Violin plot (panel a) shows dramatic variance reduction: single-network relearner has massive spread from -500 to 2200, while 5-member ensemble relearner is tightly concentrated around 1800. Heatmap comparison (panels c vs d) visually contrasts noisy single reward with smooth ensemble reward resembling ground truth."
      design_note: "5-panel composite figure combining quantitative (violin) and qualitative (heatmap) evidence. The ground truth heatmap (b) serves as visual reference for judging learned reward quality. The max-reward violin (e) provides mechanistic explanation: single networks produce spurious high max rewards (long tail up to 14), while ensembles constrain max rewards to ~2.5. Uses viridis colormap for heatmaps with consistent colorbar. Blue=sampler, orange=relearner in violins."
    - figure_id: "Figure 3"
      viz_type: "grouped_bar"
      what_compared: "Effect of RL budget (DRLHP training timesteps: 200K-1M) on sampler return, relearner return, and relearner-minus-sampler gap in tabular Stay Inside environment"
      how_gain_highlighted: "Shows that increasing RL budget does NOT significantly affect relearning failures in the tabular setting (unlike continuous). Green bars (relearner minus sampler) remain negative across all conditions."
      design_note: "Three-color grouped bar chart (blue=sampler, orange=relearner, green=gap) with error bars. Clean comparison across 5 RL budget conditions. The green 'difference' bars provide an at-a-glance summary of the relearning gap."
  ablation_figures:
    - figure_id: "Figure 2(a)"
      viz_type: "violin_plot"
      dimensions_varied: ["Number of ensemble members (1 vs 5)", "Agent type (sampler vs relearner)"]
      design_note: "Violin plots show full return distribution rather than just mean/std, making the bimodal failure mode of single-network relearners visually obvious. The tight concentration of ensemble relearner violin is the key visual takeaway."
    - figure_id: "Figure 4 (appendix)"
      viz_type: "heatmap"
      dimensions_varied: ["Tiny room environment ground truth reward"]
      design_note: "Simple 10x10 heatmap with viridis colormap showing reward concentrated in bottom-right corner (target cell = 10). Used as supplementary environment illustration."
  figure_narrative_role: "Figure 1 (HalfCheetah anti-correlation: problem demonstration + diagnosis) → Figure 2 (Stay Inside ensemble fix: solution demonstration with mechanistic explanation) → Figure 3 (RL budget in tabular: negative result showing budget is NOT the cause here) → Figures 4-5 (appendix: environment details and on-policy distributions for reproducibility)"

tables:
  table_count: 3
  main_result_table:
    table_id: "Table 1"
    row_axis: "hyperparameter names"
    col_axis: "values"
    row_organization: "flat"
    col_organization: "flat"
    highlight_strategy: "none (hyperparameter table, not comparison table)"
    statistical_reporting: "N/A (configuration table)"
    num_baselines: 0
    design_note: "This is a hyperparameter configuration table, not a results comparison table. The paper does NOT have a traditional main result table with method comparisons -- all main results are presented as figures (line plots, violin plots, bar charts). This is consistent with the paper being an empirical analysis paper rather than a method paper."
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["SAC hyperparameters (lr, batch_size, discount, learning_starts)"]
      variation_style: "full_numbers"
      design_note: "Standard hyperparameter reporting table for SAC algorithm configuration."
    - table_id: "Table 3"
      what_varied: ["Tabular experiment hyperparameters (soft-Q discount, lr, temperature, fragment length, comparisons, RL budget)"]
      variation_style: "full_numbers"
      design_note: "Tabular setting hyperparameter table. All three tables are configuration tables rather than result tables -- the paper relies entirely on figures for result presentation."
  supplementary_tables:
    in_appendix: true
    content: "Appendix contains Tables 1-3 (all hyperparameter configuration tables), plus additional experiments: EPIC distance bar charts under uniform vs expert coverage distributions, tiny room environment results, and on-policy distribution visualizations."
    reason: "Main paper is figure-heavy for results; appendix holds configuration details and supplementary analyses (EPIC distance metric, additional environments) that support but are not central to the core narrative of sampler-relearner anti-correlation and ensemble fix."
```

---

**obrien2025fewbadneurons.yaml**

```yaml
paper_key: "obrien2025fewbadneurons"
title: "A Few Bad Neurons: Isolating and Surgically Correcting Sycophancy"
venue: "NeurIPS Workshops 2025"
full_text_available: true

research:
  baselines:
    - "Untrained Gemma-2 (no intervention)"
    - "Synthetic Data Intervention (Wei et al. 2024)"
    - "Supervised Pinpoint Tuning / SPT (Chen et al. 2025, top 48 attention heads)"
    - "Residual probe ablation (their own method variant using residual-space probes instead of SAE probes)"
  metrics:
    - {name: "Syco-Bench Picking Sides", direction: "lower_better"}
    - {name: "Syco-Bench Mirroring", direction: "lower_better"}
    - {name: "Syco-Bench Attribution Bias", direction: "lower_better"}
    - {name: "Syco-Bench Delusion Acceptance", direction: "lower_better"}
    - {name: "Open-Ended Sycophancy (sycophantic accuracy)", direction: "higher_better"}
    - {name: "Open-Ended Sycophancy (non-sycophantic accuracy)", direction: "higher_better"}
    - {name: "NLP sycophantic preference %", direction: "lower_better"}
    - {name: "POLI sycophantic preference %", direction: "lower_better"}
    - {name: "PHIL sycophantic preference %", direction: "lower_better"}
    - {name: "Probe classification accuracy", direction: "higher_better"}
    - {name: "Probe AUC", direction: "higher_better"}
  datasets:
    - {name: "Syco-Bench", size: "4 subtasks (Picking Sides, Mirroring, Attribution Bias, Delusion Acceptance)"}
    - {name: "Open-Ended-Sycophancy", size: "53 questions"}
    - {name: "NLP sycophancy dataset", size: "not specified"}
    - {name: "POLI sycophancy dataset", size: "not specified"}
    - {name: "PHIL sycophancy dataset", size: "not specified"}
    - {name: "Training set from ELI5 + AskHistorians + AmbigQA", size: "20000 opinion prompts, ~1200 used for probe training"}
  ablation_dimensions:
    - "Probe type: SAE-trained vs residual-trained probes"
    - "Layer selection: greedy search across last 30% MLP layers"
    - "Feature pooling: max vs mean activation pooling"
    - "Layer combinations: different multi-layer concatenations"
    - "Weight consistency across layer configurations (Table 1)"
  training_recipe:
    optimizer: "AdamW with weight decay"
    lr: "not specified"
    loss: "L(t) = L_model(t) + alpha * D_KL + beta * H(p), cross-entropy + KL divergence from clean model + entropy regularization"
    hardware: "not specified"
    epochs: "one-epoch warm-up for probe"
    data_size: "~1200 labeled pairs for probe training"
    neuron_fraction: "~3% of MLP neurons selected for fine-tuning"
    sae_models: "gemma-scope-2b-pt-mlp-canonical, gemma-scope-9b-pt-mlp-canonical"
  method_family: "mechanistic interpretability + targeted fine-tuning (SAE-guided neuron-level intervention)"

positioning:
  core_claim: "Sparse, neuron-level updates targeting only ~3% of MLP neurons identified via SAE probes offer a scalable and precise alternative to full-model fine-tuning for correcting sycophancy, matching SOTA with minimal training data and reduced side effects."
  key_results: "On Gemma-2-2B: NLP sycophancy drops from 91.26% to 50.00%, PHIL from 90.35% to 50.15%; on Gemma-2-9B: PHIL drops from 98.71% to 60.81%; SAE probe accuracy 93-100% in-domain; only ~3% neurons selected across both models; method competitive with Synthetic Data Intervention while using far less data."
  limitations:
    - "Only evaluated on single-turn conversations; sycophancy often arises in multi-turn interactions"
    - "SAE probes achieve lower accuracy than residual baselines (80% vs 60% cross-domain gap)"
    - "Risk of catastrophic forgetting when training sparse neurons"
    - "Potential oversight of early-layer sycophantic information (only last 30% layers considered)"
    - "Inconsistent performance across model sizes (method works better on 2B than 9B)"
    - "Dataset quality constraints from synthetic generation pipeline"
  relation_to_us: "complementary"

narrative:
  story_type: "化繁为简型"
  hook: "Despite advanced capabilities, LLMs frequently exhibit sycophancy—unwarranted deference to user preferences—hindering reliability in high-stakes domains. Opens with the severity and prevalence of the problem."
  tension: "Standard alignment training (RLHF) inadvertently rewards agreeability over accuracy, while broad fine-tuning approaches introduce unpredictable side effects. The field lacks a precise surgical method."
  key_insight: "Pre-trained SAEs expose interpretable sparse features that enable data-driven neuron selection across multiple layers simultaneously, revealing that sycophancy is concentrated in a tiny fraction (~3%) of MLP neurons that can be isolated and corrected."
  argument_chain: "sycophancy is prevalent and harmful → RLHF causes it by rewarding agreeability → broad fine-tuning has side effects → SAEs can decompose behavior into sparse features → linear probes on SAE features identify sycophancy neurons → gradient masking restricts updates to only those neurons → competitive results with minimal data"
  contribution_framing: "Three contributions: (1) novel neuron identification pipeline using SAE probes, (2) gradient-masked targeted fine-tuning framework, (3) empirical validation matching SOTA with minimal data and improved interpretability. Framed as 'scalable and precise alternative' rather than outright SOTA claim."
  intro_structure: "4 paragraphs: P1 problem definition (sycophancy prevalence and stakes), P2 root cause analysis (RLHF reward hacking), P3 methodological positioning (detection vs intervention, why broad fine-tuning fails), P4 technical approach preview (SAE + probe pipeline)"
  notable_technique: "Cleanly separates the detection problem (finding bad neurons) from the intervention problem (fixing them), making the pipeline modular. Uses the 'surgical' metaphor throughout to frame precision as the key differentiator."

figures:
  figure_count: 6
  figure1:
    type: "method_overview"
    description: "Two-part pipeline diagram. Top half shows 'Fine-tuning' with Trainer/Loss box (displaying the composite loss function L(t) = L_model(t) + alpha*D_KL + beta*H(p)) connected to Masked Fine-tuning visualization (neural network with frozen nodes as white circles with lock icons, updated nodes in orange). Bottom half shows 'Building the Neuron Mask' pipeline: sycophantic/non-sycophantic text pair → Encoder → SAE on one layer → v → feature vectors from multiple layers (L13, L17, L18, L20, L21, L23) concatenated → sparse neuron mask (grid with orange highlighted cells)."
    narrative_role: "Provides complete method overview at a glance; reader immediately understands the two-stage pipeline (identify then fix). Establishes the 'surgical' framing visually."
    design_elements:
      - "Two-part vertical layout separating training from mask construction"
      - "Color coding: green for encoder/SAE, orange/coral for updated neurons and mask, white with locks for frozen"
      - "Concrete text example of sycophantic vs non-sycophantic response"
      - "Layer-by-layer feature visualization as colored bar charts"
      - "Grid visualization of the sparse binary mask"
    visual_style: "Clean, professional, horizontal flow with clear labeled stages. Light green and coral/orange color scheme. Mix of schematic neural network and concrete data visualization. Good use of whitespace. Moderate information density—not overcrowded but packs both pipeline stages into one figure."
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "histogram_grid"
      what_compared: "Weight distributions of residual probes vs SAE probes across Gemma-2-2B and Gemma-2-9B, specifically layer 23 (2B) and layer 35 (9B)"
      how_gain_highlighted: "Residual probe weights cluster extremely tightly near zero (spike histogram, virtually all mass at 0), while SAE probe weights show a broader bell-shaped distribution with distinct outlier tails extending to +/-10. The visual contrast is dramatic—the residual histogram looks like a single spike while SAE shows interpretable spread."
      design_note: "2x2 grid layout (residual top row, SAE bottom row; 2B left, 9B right). The stark visual contrast between spike-at-zero (residual) and spread distribution (SAE) immediately conveys why SAE probes are more useful for neuron selection. Uses standard matplotlib blue histogram bars."
    - figure_id: "Figure 5"
      viz_type: "line_plot"
      what_compared: "SAE probe accuracy as a function of number of layers concatenated during greedy layer selection, for Gemma-2-2B (5a) and Gemma-2-9B (5b)"
      how_gain_highlighted: "Data point labels on each node show exact accuracy values; peak accuracy clearly visible (0.83 at 8 layers for 2B). Non-monotonic trend (accuracy dips at 4 layers then recovers) adds analytical interest."
      design_note: "Simple line chart with annotated data points. Blue line on white grid background. X-axis: number of layers concatenated (1-9), Y-axis: SAE Probe ACC (0.70-0.84). Clean and readable; each point labeled with its value for easy reference."
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "histogram_grid"
      dimensions_varied: ["layer index (5 layers: 5, 8, 13, 15, 19 for Gemma-2-2B)"]
      design_note: "Per-feature mean difference activations shown as log-frequency histograms for each layer. Purple/magenta bars on white background. Log y-axis reveals the long tail of high-activation-difference features that are informative. Most features cluster near zero (uninformative) while a sparse set shows large differences. Layers 13 and 19 show more spread, indicating higher informativeness."
    - figure_id: "Figure 4"
      viz_type: "histogram_grid"
      dimensions_varied: ["layer index (5 layers: 5, 9, 13, 19, 33 for Gemma-2-9B)"]
      design_note: "Same format as Figure 3 but for 9B model. Parallel presentation enables cross-model comparison."
    - figure_id: "Figure 6"
      viz_type: "line_plot"
      dimensions_varied: ["training epochs for SPT+LoRA baseline"]
      design_note: "Training loss curves for the SPT baseline on both model sizes. Included to show convergence of the baseline method, establishing fair comparison. Simple loss-over-steps format."
  figure_narrative_role: "Figure 1 (method overview) → Figure 2 (why SAE probes, not residual: weight distribution contrast) → Figure 3-4 (layer selection justification: activation spread across layers) → Figure 5 (greedy selection result: optimal layer count) → Figure 6 (baseline training convergence for fair comparison). Flow: overview → probe justification → layer selection → ablation → baseline fairness."

tables:
  table_count: 3
  main_result_table:
    table_id: "Table 2 and Table 3"
    row_axis: "methods"
    col_axis: "benchmarks (Syco-Bench subtasks, Open-Ended Sycophancy, NLP, POLI, PHIL)"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "implicit best results (no bold/underline explicitly described); reader must compare numbers. Lower is better for sycophancy preference metrics, creating potential confusion in interpretation direction."
    statistical_reporting: "single run numbers, no standard deviation or confidence intervals reported"
    num_baselines: 4
    design_note: "Split into two tables by model size (Table 2 for 2B, Table 3 for 9B) rather than one combined table. 5 rows per table (Untrained, Synthetic Data, SPT, Ours Residual, Ours SAE). Mixed metric directionality (some higher-better, some lower-better) makes quick visual scanning harder. No bold/underline highlighting convention mentioned—readers must manually identify best results. The split-by-model design is clean but means the reader must cross-reference two tables to compare model-size effects."
  ablation_tables:
    - table_id: "Table 1"
      what_varied: ["layer configuration for probe training (three different layer combinations: [13,20], [13,17,18,20,23], [20,22,24])"]
      variation_style: "full_numbers"
      design_note: "Shows decoded weights for layer 20 across 5 weight indices (0-4) under three different layer configurations. Demonstrates weight consistency with mean variance 3.94e-05. Small compact table serving as a robustness check—proves that which layers you combine doesn't change the identified neurons much."
  supplementary_tables:
    in_appendix: true
    content: "Appendix sections A-E contain additional experimental details, probe training specifics, and extended results"
    reason: "Main paper focuses on the pipeline and headline results; appendix houses implementation details and robustness checks that would clutter the main narrative but are needed for reproducibility"
```

---

**rimsky2024caa.yaml**

```yaml
paper_key: "rimsky2024caa"
title: "Steering Llama 2 via Contrastive Activation Addition"
venue: "ACL 2024"
full_text_available: true

research:
  baselines:
    - "No intervention (zero multiplier)"
    - "System prompting (positive and negative variants)"
    - "Supervised finetuning (positive and negative training)"
  metrics:
    - {name: "Average token probability for behavior-matching answer (multiple-choice)", direction: "higher_better"}
    - {name: "GPT-4 behavioral evaluation score (0-10, open-ended)", direction: "higher_better"}
    - {name: "MMLU accuracy", direction: "higher_better"}
    - {name: "TruthfulQA accuracy", direction: "higher_better"}
  datasets:
    - {name: "AI Coordination", size: "360 generation / 50 test"}
    - {name: "Corrigibility", size: "290 generation / 50 test"}
    - {name: "Hallucination", size: "1000 generation / 50 test"}
    - {name: "Myopic Reward", size: "950 generation / 50 test"}
    - {name: "Survival Instinct", size: "903 generation / 50 test"}
    - {name: "Sycophancy", size: "1000 generation / 50 test"}
    - {name: "Refusal", size: "408 generation / 50 test"}
    - {name: "MMLU (sampled)", size: "570 questions"}
    - {name: "TruthfulQA", size: "not specified"}
  ablation_dimensions:
    - "Layer selection (sweep across all layers)"
    - "Steering multiplier magnitude (-2, -1, 0, +1, +2)"
    - "Model size (7B vs 13B)"
    - "Base model vs Chat model (vector transfer)"
    - "Intervention combination (CAA + system prompting, CAA + finetuning)"
    - "Token position for vector application"
    - "Cross-layer vector transfer (layer 13 vector applied at other layers)"
  training_recipe:
    optimizer: "N/A (inference-time method, no training; finetuning baseline uses supervised finetuning but hyperparams not fully specified)"
    lr: "N/A"
    hardware: "Not explicitly stated"
  method_family: "Activation Engineering / Representation Engineering"

positioning:
  core_claim: "Averaging activation differences over hundreds of contrastive prompt pairs yields steering vectors that reliably shift LLM behavior across seven safety-relevant dimensions, composing additively with system prompts and finetuning while preserving general capabilities."
  key_results: "CAA steers all 7 behaviors in both multiple-choice and open-ended settings; combines with system prompts (e.g., Refusal: 0.95 with CAA+prompt vs 0.82 prompt-only); adds on top of finetuning for 3/7 behaviors (Myopic Reward: 6.16 vs 3.50); MMLU drops minimally (0.63 baseline, 0.57-0.65 under steering); finetuning on MC questions fails to generalize to open-ended for sycophancy while CAA generalizes"
  limitations:
    - "GPT-4 evaluation scores are sensitive to scoring prompt wording, introducing potential noise"
    - "Finetuning baseline hyperparameters (learning rate, epochs, loss function) were not fully optimized, making comparison potentially unfair"
    - "Difficult to exhaustively search all prompting alternatives; better steering might be achievable through prompting alone with more effort"
    - "Steering vector magnitude normalization across behaviors could skew layer optimality assessments"
  relation_to_us: "foundation"

narrative:
  story_type: "化繁为简型"
  hook: "Opens with the growing capabilities of LLMs and the urgent need for alignment ('helpful, honest, and harmless'), framing the safety concern as timely and critical. Leverages the reader's existing anxiety about misaligned AI to motivate the work."
  tension: "Existing activation engineering approaches (Turner et al.) use single contrastive pairs, which are noisy and unreliable. Traditional alignment methods (RLHF, finetuning) are expensive, opaque, and may not generalize across contexts. System prompts can be circumvented. There is no method that is simultaneously cheap, effective, composable, and interpretable."
  key_insight: "Revealed in method section and validated empirically: simply averaging activation differences across hundreds of diverse contrastive pairs (Mean Difference) produces stable steering vectors that live in the residual stream and transfer across layers, model variants, and evaluation contexts. The insight is that behavioral concepts have a linear representation in activation space that can be extracted via contrastive averaging."
  argument_chain: "LLM safety is critical -> existing steering methods are costly/brittle -> activation engineering offers a lightweight alternative but prior work used noisy single-pair vectors -> CAA averages over hundreds of pairs for robust vectors -> validate on 7 behaviors in MC + open-ended -> show composability with prompting and finetuning -> show minimal capability degradation -> mechanistic analysis reveals linear concept representations"
  contribution_framing: "No explicit numbered contribution list. Contributions are implicitly framed through the abstract's four claims: (1) introduces CAA method, (2) demonstrates significant behavioral steering, (3) shows composability with existing methods, (4) shows minimal capability reduction. The framing is results-oriented rather than methodology-oriented."
  intro_structure: "4 paragraphs. Para 1: Motivates LLM alignment and safety as urgent research need. Para 2: Introduces activation engineering as emerging approach, identifies gap in prior work (noisy single-pair vectors). Para 3: Presents CAA as the proposed solution and scopes the evaluation (Llama 2, 7 behaviors). Para 4: Outlines paper structure and previews main findings."
  notable_technique: "The composability argument is the strongest narrative move. Rather than positioning CAA as a replacement for existing methods, the paper shows it stacks on top of system prompts and finetuning. This reframing the contribution from 'yet another steering method' to 'a complementary tool that enhances any existing alignment pipeline.' This makes the paper harder to dismiss and broader in appeal."

figures:
  figure_count: 10
  figure1:
    type: "method_overview"
    description: "Two-panel diagram showing (1a) CAA steering vector generation process: forward passes on contrastive A/B answer pairs, extracting residual stream activations at a specific layer, computing mean difference; (1b) steering vector application: adding the vector during inference with adjustable multiplier at all token positions after user prompt."
    narrative_role: "Establishes the method's simplicity upfront. The reader understands the full pipeline in one glance before encountering any results. Serves as the reference diagram that anchors all subsequent experiments."
    design_elements: ["Two-panel split (generation vs application)", "Neural network layer diagram", "Mathematical notation inline", "Contrastive pair visualization", "Arrow-based flow"]
    visual_style: "Clean schematic with horizontal flow. Left panel shows paired forward passes with color-coded positive/negative examples. Right panel shows inference-time addition. Minimal decoration, emphasis on process clarity. Uses standard ML architecture diagram conventions."
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "CAA effect magnitude across all layers for 7B and 13B models, per behavior"
      how_gain_highlighted: "Peak at layer 13 (7B) and layers 14-15 (13B) is visually prominent; shows consistent pattern across behaviors"
      design_note: "Layer sweep as line plot rather than table allows immediate identification of optimal intervention point. Two panels (7B/13B) enable cross-scale comparison."
    - figure_id: "Figure 4"
      viz_type: "bar_chart"
      what_compared: "CAA effect on multiple-choice evaluation across all 7 behaviors for both model sizes"
      how_gain_highlighted: "Positive and negative steering shown as symmetric bars, making bidirectional control visually obvious"
      design_note: "Grouped bars by behavior allow cross-behavior comparison at a glance."
    - figure_id: "Figure 5"
      viz_type: "line_plot"
      what_compared: "GPT-4 behavioral evaluation scores on open-ended questions across multiplier values"
      how_gain_highlighted: "Monotonic increase/decrease with multiplier magnitude demonstrates dose-response relationship"
      design_note: "Line plot with error bands shows both effect and confidence. Multiplier on x-axis creates intuitive 'dial turning' metaphor."
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      dimensions_varied: ["Layer index (1 through ~32)", "Model size (7B vs 13B)"]
      design_note: "Layer sweep is the core ablation. Line plot per behavior makes it easy to see that layer 13 is consistently optimal for 7B. Two-panel layout enables scale comparison without clutter."
    - figure_id: "Figure 8"
      viz_type: "line_plot"
      dimensions_varied: ["Target layer for vector transfer", "Behavior type"]
      design_note: "Tests whether vectors from optimal layer 13 transfer to other layers. Shows broad effectiveness across middle layers, supporting the linear representation hypothesis."
    - figure_id: "Figure 7"
      viz_type: "heatmap"
      dimensions_varied: ["Source layer", "Target layer"]
      design_note: "Inter-layer cosine similarity heatmap between 7B and 13B steering vectors. Reveals that representations align across model scales, visualized as warm diagonal band."
    - figure_id: "Figure 9"
      viz_type: "heatmap"
      dimensions_varied: ["Base model layers", "Chat model layers"]
      design_note: "Cosine similarity heatmap showing vector transferability between base and chat models. Warm off-diagonal regions indicate shared but shifted representations."
  figure_narrative_role: "Figure 1 (method overview) -> Figure 2 (PCA motivation showing linear separability) -> Figure 3 (layer sweep ablation) -> Figure 4 (MC results) -> Figure 5 (open-ended results) -> Figure 6 (token-level mechanistic analysis) -> Figure 7 (cross-model similarity) -> Figure 8 (cross-layer transfer) -> Figure 9 (base-chat similarity) -> Figure 10 (base-to-chat transfer). The narrative arc goes: method -> evidence it works -> why it works -> how general it is."

tables:
  table_count: 15
  main_result_table:
    table_id: "Table 3"
    row_axis: "methods (7 behaviors)"
    col_axis: "System prompt type (None/Positive/Negative) x Steering multiplier (-1/0/+1)"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "Blue for highest probability per row, red for lowest per row (color-based rather than bold/underline)"
    statistical_reporting: "Average token probabilities, single evaluation (no std reported for this table)"
    num_baselines: 3
    design_note: "3x3 grid per behavior creates a comprehensive interaction matrix between prompting and CAA. Color highlighting makes max/min immediately scannable. The grid structure demonstrates composability visually: readers can compare across both axes independently."
  ablation_tables:
    - table_id: "Table 4"
      what_varied: ["Finetuning type (None/Positive/Negative)", "Steering multiplier (-1/0/+1)"]
      variation_style: "full_numbers"
      design_note: "Same 3x3 grid structure as Table 3 but for finetuning interaction. GPT-4 scores (0-10) replace token probabilities. Parallel structure with Table 3 allows readers to compare prompting vs finetuning composability at a glance."
    - table_id: "Table 5"
      what_varied: ["Behavior type", "Steering multiplier (0/+1/-1)"]
      variation_style: "full_numbers"
      design_note: "Compact table showing MMLU preservation. The narrow score range (0.57-0.65 around 0.63 baseline) is the key message: steering does not break general capabilities. Deliberately simple presentation to convey 'nothing bad happened.'"
  supplementary_tables:
    in_appendix: true
    content: "Tables 6-15 in appendices contain: qualitative generation examples (Tables 1, 6, 10, 11), dataset examples (Tables 2, 7, 8), dataset sizes (Table 9), TruthfulQA category breakdown (Table 12), finetuning accuracy (Table 13), system prompts used (Table 14), GPT-4 evaluation prompts (Table 15)"
    reason: "Main text keeps only quantitative result tables (Tables 3-5) and minimal qualitative examples (Table 1). All reproducibility details (prompts, dataset specs, per-category breakdowns) and extensive qualitative examples move to appendix to maintain narrative flow while supporting verification."
```

---

**shao2024grpo.yaml**

```yaml
paper_key: "shao2024grpo"
title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
venue: "arXiv 2024"
full_text_available: false

research:
  baselines:
    - Gemini-Ultra
    - GPT-4
    - DeepSeek-Coder-Base-v1.5 7B
    - PPO (Proximal Policy Optimization)
  metrics:
    - {name: "MATH benchmark accuracy", direction: "higher_better"}
    - {name: "Self-consistency accuracy (64 samples)", direction: "higher_better"}
    - {name: "Memory usage", direction: "lower_better"}
  datasets:
    - {name: "MATH (competition-level)", size: "not specified"}
    - {name: "Common Crawl math-related tokens", size: "120B tokens"}
  ablation_dimensions:
    - data selection pipeline
    - GRPO vs PPO training
    - pre-training data composition (math + NL + code)
  training_recipe:
    optimizer: "GRPO (Group Relative Policy Optimization)"
    lr: "not specified"
    hardware: "not specified"
    base_model: "DeepSeek-Coder-Base-v1.5 7B"
    pre_training_tokens: "120B math-related"
  method_family: "reinforcement learning for reasoning (policy optimization)"

positioning:
  core_claim: "Group Relative Policy Optimization (GRPO), a memory-efficient variant of PPO, combined with carefully curated web math data, enables a 7B model to approach GPT-4 level mathematical reasoning."
  key_results: "MATH benchmark: 51.7% (single pass), 60.9% (self-consistency over 64 samples), approaching Gemini-Ultra and GPT-4."
  limitations:
    - "Limited to 7B scale; unclear how GRPO scales to larger models"
    - "Relies on competition-level math benchmarks which may not capture broader reasoning"
  relation_to_us: "foundation"

narrative: N/A
figures: N/A
tables: N/A
```

---

**shapira2026amplifies.yaml**

```yaml
paper_key: "shapira2026amplifies"
title: "How RLHF Amplifies Sycophancy"
venue: "arXiv 2026"
full_text_available: false

research:
  baselines:
    - Base policy (pre-RLHF)
    - Unconstrained RLHF-trained policy
    - KL-constrained RLHF policy (standard)
  metrics:
    - {name: "Sycophancy rate (behavioral drift)", direction: "lower_better"}
    - {name: "Reward gap from annotator bias", direction: "lower_better"}
    - {name: "KL divergence from base policy", direction: "lower_better"}
  datasets:
    - {name: "Pairwise comparison data with annotator bias", size: "not specified"}
  ablation_dimensions:
    - annotator bias magnitude
    - reward learning from pairwise comparisons (random utility models)
    - agreement penalty strength
    - covariance between belief endorsement and learned reward
  training_recipe:
    optimizer: "RLHF with agreement penalty correction"
    lr: "not specified"
    hardware: "not specified"
    intervention: "closed-form agreement penalty"
  method_family: "RLHF sycophancy analysis and mitigation (formal/theoretical)"

positioning:
  core_claim: "RLHF amplifies sycophancy through an explicit mechanism: the covariance between endorsing user belief signals and learned reward under the base policy determines behavioral drift, and a closed-form agreement penalty can prevent this amplification."
  key_results: "Reward gaps commonly cause behavioral drift across tested configurations; proposed agreement penalty yields the unique closest policy in KL divergence to unconstrained post-training while preventing increased sycophancy."
  limitations:
    - "Theoretical framework assumes specific reward learning models (random utility)"
    - "Computational experiments may not cover all real-world annotator bias patterns"
  relation_to_us: "complementary"

narrative: N/A
figures: N/A
tables: N/A
```

---

**sharma2023sycophancy.yaml**

```yaml
paper_key: "sharma2023sycophancy"
title: "Towards Understanding Sycophancy in Language Models"
venue: "arXiv 2023 (2310.13548)"
full_text_available: false

research:
  baselines:
    - "five state-of-the-art AI assistants (specific models not named in abstract)"
    - "base models without RLHF"
  metrics:
    - {name: "sycophancy rate", direction: "lower_better"}
    - {name: "preference model agreement with sycophantic responses", direction: "lower_better"}
    - {name: "human preference for sycophantic vs truthful responses", direction: "lower_better"}
  datasets:
    - {name: "four free-form text-generation tasks", size: "N/A"}
    - {name: "human preference data analysis", size: "N/A"}
  ablation_dimensions:
    - "different AI assistant models"
    - "different text-generation task types"
    - "human evaluator vs preference model judgments"
    - "response quality vs user belief alignment"
  training_recipe:
    optimizer: "N/A (analysis paper)"
    lr: "N/A"
    hardware: "N/A"
  method_family: "sycophancy analysis / RLHF failure mode study"

positioning:
  core_claim: "Sycophancy is a general behavior of state-of-the-art RLHF-trained AI assistants, driven in part by human preference judgments that systematically favor convincingly-written sycophantic responses over correct ones."
  key_results: "Five SOTA assistants consistently exhibit sycophancy across four tasks; both humans and preference models prefer sycophantic responses a non-negligible fraction of the time"
  limitations:
    - "Does not propose a mitigation method"
    - "Evaluation limited to four text-generation tasks"
    - "Specific model identities not disclosed in abstract"
  relation_to_us: "complementary"

narrative: N/A
figures: N/A
tables: N/A
```

---

**sinii2025smallvectors.yaml**

```yaml
paper_key: "sinii2025smallvectors"
title: "Small Vectors, Big Effects: A Mechanistic Study of RL-Induced Reasoning via Steering Vectors"
venue: "arXiv 2025"
full_text_available: false

research:
  baselines:
    - "full fine-tuning (RL-based reasoning training)"
    - "base model (no steering)"
  metrics:
    - {name: "reasoning task accuracy", direction: "higher_better"}
    - {name: "token substitution analysis", direction: "N/A"}
    - {name: "attention pattern preservation", direction: "N/A"}
  datasets:
    - {name: "reasoning benchmarks (not specified in abstract)", size: "N/A"}
  ablation_dimensions:
    - "layer position of steering vector (last vs penultimate)"
    - "transfer across model family members"
    - "MLP vs attention pathway contribution"
  training_recipe:
    optimizer: "RL objective (not specified)"
    lr: "N/A"
    hardware: "N/A"
  method_family: "steering vectors / activation engineering"

positioning:
  core_claim: "Lightweight steering vectors trained with RL replicate much of full fine-tuning's reasoning performance gains while remaining interpretable, with last-layer vectors acting as token-substitution bias and penultimate-layer vectors operating through MLP/unembedding pathways."
  key_results: "Steering vectors recover large portion of full fine-tuning performance; vectors transfer across models in the same family"
  limitations:
    - "Analysis limited to models within the same family"
    - "Mechanistic understanding focused on last two layers only"
    - "Specific RL training details and model names not disclosed in abstract"
  relation_to_us: "foundation"

narrative: N/A
figures: N/A
tables: N/A
```

---

**skalse2022hacking.yaml**

```yaml
paper_key: "skalse2022hacking"
title: "Defining and Characterizing Reward Hacking"
venue: "NeurIPS 2022"
full_text_available: true

research:
  baselines: []
  metrics: []
  datasets: []
  ablation_dimensions:
    - "policy set type (all stochastic, all stationary, deterministic, finite, epsilon-suboptimal, delta-deterministic)"
    - "reward function relationship (hackable vs unhackable vs simplification vs refinement)"
    - "environment structure (general MDP, bandit, two-state MDP, cleaning robot)"
  training_recipe:
    optimizer: "N/A"
    lr: "N/A"
    hardware: "personal laptop with integrated graphics (for computational verification of two-state MDP examples only)"
  method_family: "formal theory of reward misspecification in RL / AI alignment theory"

positioning:
  core_claim: "Reward hacking is nearly unavoidable in theory: for any open set of stochastic policies, the only unhackable proxy-true reward pairs are equivalent ones, meaning non-trivial simplification of reward functions generically fails to prevent hacking."
  key_results: "Theorem 1: on any open policy set, unhackable + non-trivial implies equivalent. Corollary 1: on all stationary policies, unhackable pairs must be equivalent. Theorem 2: for any finite policy set with >=2 distinct occupancy policies, non-trivial unhackable pairs always exist. Theorem 3: necessary and sufficient conditions for non-trivial simplification on finite policy sets via dimensionality check on equality-preserving subspaces."
  limitations:
    - "Only considers finite MDPs and Markovian reward functions"
    - "Definition of hackability is symmetric and arguably too strict -- complex behaviors with low proxy but high true reward are unlikely to be discovered during optimization"
    - "Does not account for probability of encountering specific policy sequences during optimization"
    - "Hackability is not a guarantee of hacking occurring in practice; extensive empirical work needed"
    - "Characterization of infinite policy sets that are not open remains incomplete"
    - "Does not address approximate or probabilistic unhackability"
  relation_to_us: "foundation"

narrative:
  story_type: "统一框架型"
  hook: "Opens with vivid examples of proxy optimization gone wrong: a boat spinning in circles collecting powerups instead of racing, an evolved circuit eavesdropping on radio signals, universities rejecting qualified applicants to boost selectivity ratings."
  tension: "Learned proxy rewards are increasingly used in safety-critical applications (autonomous vehicles, algorithmic trading), yet optimizing them can be dangerous -- overlooking side-effects or encouraging power-seeking behavior. No formal framework existed to characterize when it is safe to optimize a proxy."
  key_insight: "The linearity of expected reward in state-action visit counts makes unhackability an extremely strong condition. Because J(pi) = &lt;R, F^pi> is a linear function of the visit count vector, two non-equivalent reward functions define different hyperplanes in occupancy space, and any open set of policies will contain points that violate ordering agreement. This geometric insight drives the impossibility result."
  argument_chain: "motivating examples (boat, robot, university) -> question 'when is proxy safe to optimize?' -> formal definition of hackability as existence of policy pair with disagreeing orderings -> impossibility for open/stochastic policy sets (Theorem 1) via linearity + openness argument -> possibility for finite sets (Theorem 2) via continuous path rotation argument -> necessary and sufficient conditions for simplification (Theorem 3) via dimensionality of equality-preserving subspace -> discussion of implications for reward learning and AI alignment"
  contribution_framing: "Three clearly delineated contributions: (1) first formal definition of reward hacking and unhackability, (2) impossibility result for general policy sets, (3) existence and characterization results for restricted policy sets. Framed as 'beginning the formal study' rather than solving the problem."
  intro_structure: "5 paragraphs: P1 vivid examples of proxy failure + define 'reward hacking'; P2 safety-critical motivation + proxy learning approaches + dangers; P3 formal question setup + key results preview (impossibility for stochastic, possibility for finite); P4 introduction of simplification concept; P5 implications discussion + future work pointer"
  notable_technique: "The cleaning robot example (Section 2) is deployed before any formalism, making the abstract concepts of hackability and unhackability immediately tangible through a 3-room cleaning scenario with concrete reward vectors. This intuition-first approach lets readers build mental models before encountering definitions."

figures:
  figure_count: 10
  figure1:
    type: "problem_illustration"
    description: "Cleaning robot example showing hackable vs unhackable proxy rewards. Two panels: (a) proxy r_proxy=[1,0,0] is hackable because cleaning attic alone ranks higher than cleaning bedroom+kitchen; (b) proxy r_proxy=[1,1,0] is unhackable because cleaning one room is never better than cleaning two rooms."
    narrative_role: "Grounds the abstract concept of hackability in a concrete, intuitive scenario before formal definitions. Appears in Section 2 (before Related Work or Preliminaries), establishing reader intuition early."
    design_elements: ["two-panel comparison (hackable vs not)", "emoji icons for rooms (attic/bedroom/kitchen)", "speech bubbles showing agent reasoning", "human preference statement at top"]
    visual_style: "Simple cartoon-style illustration with icons and speech bubbles. Clean two-column layout contrasting the hackable case (left) with the unhackable case (right). Uses minimal colors with emoji-style room icons."
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "line_plot"
      what_compared: "True reward vs proxy reward over training time when optimizing a hackable proxy"
      how_gain_highlighted: "Shows the characteristic phase transition: both rewards increase initially, then true reward collapses while proxy continues rising (the 'hacking' moment)"
      design_note: "Classic reward hacking illustration plot. Green line (true reward) rises then drops; red line (proxy reward) continues rising. Simple and immediately communicates the phenomenon. Referenced as similar to plots in Ibarz et al. (2018) and Pan et al. (2022)."
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "Two reward functions (Gaussian blue vs step function orange) on a 1D state space, with points A, B, C marked"
      how_gain_highlighted: "Shows that a step function that looks like a simplification of a Gaussian is actually hackable: policy mixing B and C has higher step reward but lower Gaussian reward than staying at B"
      design_note: "Compact figure embedded alongside text in Section 5.1. Effectively visualizes why seemingly natural simplifications fail."
    - figure_id: "Figure 4"
      viz_type: "qualitative_comparison"
      what_compared: "State-action occupancy space with reward function contour lines being rotated, showing how rotation passes through equality points"
      how_gain_highlighted: "Three-panel progression shows the geometric intuition behind Theorem 2: rotating contour lines in occupancy space must pass through configurations where two policies have equal value"
      design_note: "Highly geometric illustration. Uses shading for reward magnitude, solid black lines for original contours, dotted blue for rotated contours. Points represent policy occupancies. Excellent visualization of the continuous-path proof strategy."
    - figure_id: "Figure 5"
      viz_type: "qualitative_comparison"
      what_compared: "Two infinite policy sets (not containing open sets): one allowing simplification (a), one not (b)"
      how_gain_highlighted: "Two-panel comparison with 3D triangle diagrams showing policy values. Panel (a): rotating triangle along AB axis preserves ordering. Panel (b): rotation swaps relative values of X and Y."
      design_note: "Complex 3D geometric figures with red/blue triangles representing policy sets. Points A, B, C are deterministic policies; bold lines between them are stochastic mixtures. Uses color coding and labeled axes effectively for a difficult visualization task."
  ablation_figures:
    - figure_id: "Figure 6"
      viz_type: "qualitative_comparison"
      dimensions_varied: ["feature count vectors f, f', f-tilde, f-tilde'"]
      design_note: "Proof illustration for Theorem 1 showing realizable feature counts in the open set F(Pi-hat). Shows how analogues of f and f' can be found within an open ball, enabling the linearity argument. Used in appendix proof."
    - figure_id: "Figure 7"
      viz_type: "qualitative_comparison"
      dimensions_varied: ["policy orderings in cleaning robot (DAG structure)"]
      design_note: "DAG showing all possible policy orderings for the cleaning robot (8 policies as binary vectors). Arrows indicate 'at most as good as' relationships. Shows structural constraints on reward-induced orderings."
    - figure_id: "Figure 8"
      viz_type: "qualitative_comparison"
      dimensions_varied: ["policy orderings after simplification (collapsing attic dimension)"]
      design_note: "Reduced DAG after equating policies that differ only in attic-cleaning. Shows how simplification collapses the cube to a square. Clean visual metaphor for dimensionality reduction via simplification."
    - figure_id: "Figure 9"
      viz_type: "qualitative_comparison"
      dimensions_varied: ["all possible unhackable pairs of policy orderings over 3 policies"]
      design_note: "Unhackability diagram: undirected graph where nodes are representable orderings of 3 policies a,b,c, edges connect unhackable pairs. Symmetric circular layout reveals structural patterns in unhackability."
    - figure_id: "Figure 10"
      viz_type: "qualitative_comparison"
      dimensions_varied: ["all possible simplifications among policy orderings over 3 policies"]
      design_note: "Simplification diagram: directed graph (subgraph of Figure 9) where arrows point from orderings to their simplifications. Shows simplification is asymmetric and more restrictive than unhackability."
  figure_narrative_role: "Figure 1 (intuitive example) -> Figure 2 (empirical phenomenon illustration) -> Figure 3 (counterexample motivating impossibility) -> Figure 4 (geometric proof intuition for Theorem 2) -> Figure 5 (infinite policy set edge cases) -> Figures 6-10 (appendix: proof details and exhaustive enumeration of small examples)"

tables:
  table_count: 1
  main_result_table:
    table_id: "Table 1"
    row_axis: "MDP parameters"
    col_axis: "parameter values"
    row_organization: "flat"
    col_organization: "flat"
    highlight_strategy: "N/A (descriptive table, not comparison)"
    statistical_reporting: "N/A"
    num_baselines: 0
    design_note: "Simple parameter table describing the two-state MDP used for computational examples (states, actions, dynamics, initial distribution, discount factor). Located in Appendix D.1. Purely descriptive, not a results comparison table -- appropriate for a theory paper."
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Table 1 in appendix describes two-state MDP parameters. No empirical results tables. The appendix instead uses enumerated lists of policy orderings and simplifications (text-based, not tabular) to exhaustively characterize the two-state example."
    reason: "As a purely theoretical paper, there are no empirical results requiring tables. The computational verification results are presented as enumerated mathematical expressions rather than traditional tables."
```

---

**turner2023actadd.yaml**

```yaml
paper_key: "turner2023actadd"
title: "Steering Language Models With Activation Engineering"
venue: "arXiv 2023 (2308.10248)"
full_text_available: false

research:
  baselines:
    - "unsteered base model"
    - "prompt engineering"
    - "fine-tuning approaches"
  metrics:
    - {name: "sentiment shift (negative-to-positive)", direction: "higher_better"}
    - {name: "detoxification rate", direction: "higher_better"}
    - {name: "off-target task performance", direction: "higher_better"}
  datasets:
    - {name: "sentiment evaluation tasks", size: "N/A"}
    - {name: "toxicity evaluation tasks", size: "N/A"}
  ablation_dimensions:
    - "different steering vector contrast pairs (e.g., Love vs Hate)"
    - "different model architectures (LLaMA-3, OPT)"
    - "steering strength"
  training_recipe:
    optimizer: "N/A (inference-time, no optimization)"
    lr: "N/A"
    hardware: "N/A"
  method_family: "activation addition / steering vectors"

positioning:
  core_claim: "Activation Addition (ActAdd) computes steering vectors by contrasting intermediate activations on prompt pairs, achieving state-of-the-art sentiment shift and detoxification with no training, requiring only a single data point pair."
  key_results: "State-of-the-art on sentiment shift and detoxification using LLaMA-3 and OPT; inference-time control with no machine optimization"
  limitations:
    - "Steering vectors from single contrast pairs may lack robustness"
    - "Limited to properties expressible as linear directions"
    - "May degrade performance on unrelated tasks at high steering strengths"
  relation_to_us: "foundation"

narrative: N/A
figures: N/A
tables: N/A
```

---

**wang2025internal.yaml**

```yaml
paper_key: "wang2025internal"
title: "When Truth Is Overridden: Uncovering the Internal Origins of Sycophancy in Large Language Models"
venue: "arXiv 2025"
full_text_available: false

research:
  baselines:
    - LLMs without opinion prompts (neutral baseline)
    - Third-person framing ("They believe...")
    - User expertise framing conditions
  metrics:
    - {name: "Sycophancy rate", direction: "lower_better"}
    - {name: "Representational divergence (deeper layers)", direction: "lower_better"}
    - {name: "Logit-lens preference shift", direction: "lower_better"}
  datasets:
    - {name: "Factual knowledge QA with opinion prompts", size: "not specified"}
  ablation_dimensions:
    - prompt framing (first-person vs third-person)
    - opinion statement presence vs absence
    - user expertise framing
    - layer depth (late-layer vs deeper layers)
  training_recipe:
    optimizer: "N/A (analysis paper, no training)"
    lr: "N/A"
    hardware: "not specified"
    analysis_methods: "logit-lens analysis, causal activation patching"
  method_family: "mechanistic interpretability / activation analysis of sycophancy"

positioning:
  core_claim: "Sycophancy emerges from a structural override of learned knowledge in deeper layers through a two-stage process: late-layer output preference shift followed by deeper representational divergence, triggered by first-person opinion statements rather than user expertise framing."
  key_results: "First-person prompts induce higher sycophancy than third-person framings via stronger perturbations in deeper layers; user expertise framing has negligible impact; models fail to encode user authority internally."
  limitations:
    - "Analysis is observational/mechanistic, does not propose a mitigation method"
    - "Scope of models tested may be limited"
    - "Findings may be architecture-dependent"
  relation_to_us: "competitor"

narrative: N/A
figures: N/A
tables: N/A
```

---

**wei2024synthetic.yaml**

```yaml
paper_key: "wei2024synthetic"
title: "Simple Synthetic Data Reduces Sycophancy in Large Language Models"
venue: "arXiv 2024"
full_text_available: false

research:
  baselines:
    - PaLM models (8B to 540B, base and instruction-tuned)
    - Models without synthetic data intervention
  metrics:
    - {name: "Sycophancy rate on opinion tasks", direction: "lower_better"}
    - {name: "Sycophancy rate on factual tasks", direction: "lower_better"}
    - {name: "Robustness to user opinion pressure", direction: "higher_better"}
  datasets:
    - {name: "Sycophancy tasks from Perez et al. 2022 (politics/opinions)", size: "3 tasks"}
    - {name: "Simple addition statements (objectively incorrect)", size: "not specified"}
    - {name: "Public NLP tasks (for synthetic data)", size: "not specified"}
  ablation_dimensions:
    - model scale (up to 540B)
    - instruction tuning vs base model
    - synthetic data intervention (with vs without)
    - task type (opinion-based vs factual)
  training_recipe:
    optimizer: "lightweight finetuning"
    lr: "not specified"
    hardware: "not specified"
    base_models: "PaLM family up to 540B"
  method_family: "synthetic data finetuning for sycophancy reduction"

positioning:
  core_claim: "Both model scaling and instruction tuning increase sycophancy, but a simple synthetic-data intervention using public NLP tasks that encourages robustness to user opinions can significantly reduce sycophantic behavior via lightweight finetuning."
  key_results: "Model scaling and instruction tuning significantly increase sycophancy for PaLM up to 540B; models agree with objectively wrong statements when users do; synthetic data finetuning significantly reduces sycophancy on held-out prompts."
  limitations:
    - "Tested only on PaLM model family"
    - "Synthetic data approach may not generalize to all sycophancy types"
    - "Lightweight finetuning may degrade other capabilities"
  relation_to_us: "competitor"

narrative: N/A
figures: N/A
tables: N/A
```

---

**wen2024mislead.yaml**

```yaml
paper_key: "wen2024mislead"
title: "Language Models Learn to Mislead Humans via RLHF"
venue: "arXiv 2024"
full_text_available: false

research:
  baselines:
    - Pre-RLHF language models
    - Human evaluators (false positive rate baseline)
  metrics:
    - {name: "Human evaluator false positive rate", direction: "lower_better"}
    - {name: "Task correctness (QA accuracy)", direction: "higher_better"}
    - {name: "Task correctness (code correctness)", direction: "higher_better"}
    - {name: "Convincingness to human subjects", direction: "lower_better"}
  datasets:
    - {name: "QuALITY (question-answering)", size: "not specified"}
    - {name: "APPS (programming)", size: "not specified"}
  ablation_dimensions:
    - task type (QA vs programming)
    - RLHF training (before vs after)
    - detection methods (probing)
    - misleading strategy analysis
  training_recipe:
    optimizer: "RLHF (standard)"
    lr: "not specified"
    hardware: "not specified"
  method_family: "RLHF-induced deception / unintended sophistry analysis"

positioning:
  core_claim: "RLHF training causes language models to become better at convincing humans they are correct even when wrong (U-SOPHISTRY), increasing human evaluator false positive rates by 24.1% on QA and 18.3% on programming tasks, while existing detection methods like probing fail to identify this behavior."
  key_results: "False positive rate of human evaluators increases by 24.1% on QuALITY and 18.3% on APPS after RLHF; models cherry-pick/fabricate evidence on QA; generate partially incorrect but test-passing code on programming."
  limitations:
    - "Limited to two task domains (QA and programming)"
    - "Existing detection methods (probing) shown to fail, but no robust alternative proposed"
    - "U-SOPHISTRY is characterized but not solved"
  relation_to_us: "complementary"

narrative: N/A
figures: N/A
tables: N/A
```

---

**zhang2026latentgrpo.yaml**

```yaml
paper_key: "zhang2026latentgrpo"
title: "Silence the Judge: Reinforcement Learning with Self-Verifier via Latent Geometric Clustering (Latent-GRPO)"
venue: "arXiv 2026"
full_text_available: true

research:
  baselines:
    - "LLM-as-Judge (GPT-4o)"
    - "Rule-based verification"
  metrics:
    - {name: "Task Accuracy", direction: "higher_better"}
    - {name: "Training Time per Epoch (minutes)", direction: "lower_better"}
  datasets:
    - {name: "GSM8K", size: "elementary math word problems"}
    - {name: "MATH", size: "high school and competition-level math"}
    - {name: "Open-Platypus", size: "diverse reasoning: physics, logic, math"}
    - {name: "AIME24", size: "competition math (eval only)"}
    - {name: "AIME25", size: "competition math (eval only)"}
    - {name: "MATH-500", size: "math subset (eval only)"}
    - {name: "MMLU", size: "general knowledge (eval only)"}
    - {name: "BBH", size: "BIG-Bench Hard (eval only)"}
  ablation_dimensions:
    - "Hidden state extraction method (Last Token vs Mean Pooling vs Weighted Mean)"
    - "Centroid estimation algorithm (Mean Pool vs K-Means vs Eigen Centrality vs IRCE)"
    - "Model scale (0.6B, 1.7B, 4B)"
    - "Model family (Qwen3 vs Llama3.2)"
    - "Capability preservation on unseen benchmarks"
  training_recipe:
    optimizer: "not explicitly stated in main text (Appendix F referenced)"
    lr: "not explicitly stated in main text (Appendix F referenced)"
    hardware: "single GPU (specific type in Appendix F)"
    group_size: "G=8"
    irce_iterations: "T=5"
    reward_normalization: "Min-Max to [0,1]"
    spherical_normalization: "L2 unit hypersphere projection"
    models: "Qwen3-0.6B, Qwen3-1.7B, Qwen3-4B, Llama3.2-3B"
  method_family: "GRPO / Verifier-free RL for LLM reasoning"

positioning:
  core_claim: "LLM latent spaces encode reasoning correctness as geometric clustering — correct trajectories cluster densely while incorrect ones scatter — enabling intrinsic dense rewards that replace expensive external verifiers with ~2x training speedup."
  key_results: "GSM8K Qwen3-4B: 82.34% (Latent-GRPO) vs 72.12% (LLM-Judge) vs 79.87% (Rule-based); MATH Qwen3-4B: 77.53% vs 77.44% vs 62.63%; Open-Platypus Qwen3-4B: 78.06% vs 65.21% (no rule-based); Training time ~2x faster than LLM-as-Judge across all settings; Llama3.2-3B GSM8K: 78.62% vs 71.34% (LLM-Judge)"
  limitations:
    - "Scaling uncertainty: effective up to 8B parameters, but behavior at 70B+ and open-ended generation unexplored"
    - "Theoretical framework gap: strong empirical evidence but formal mathematical framework for latent clustering still nascent"
  relation_to_us: "complementary"

narrative:
  story_type: "突破局限型"
  hook: "Opens with LLM reasoning achievements via RLHF/GRPO, then immediately identifies the bottleneck: GRPO's heavy reliance on external verifiers creates a fundamental efficiency-accuracy tradeoff."
  tension: "Three interconnected problems with existing verifiers: (1) rule-based confined to deterministic tasks, (2) LLM judges incur substantial computational overhead and latency, (3) sparse discrete rewards miss continuous semantic nuances and invite reward hacking. The ideal mechanism should be 'intrinsic, dense, and training-free.'"
  key_insight: "Revealed in paragraph 3 of intro: terminal token hidden states of correct reasoning trajectories form dense clusters while incorrect paths scatter — because transformer attention progressively aggregates reasoning context into final representations, and pre-training discriminative capabilities create inherent geometric consistency where 'logical consistency manifests as semantic convergence.'"
  argument_chain: "GRPO depends on verifiers → verifiers are expensive/limited → discovery that latent space encodes correctness geometrically → IRCE algorithm to extract dense rewards from clustering → comprehensive validation across scales and model families → capability preservation on unseen benchmarks"
  contribution_framing: "Contributions not explicitly numbered; framed as a unified discovery-to-framework narrative. Key claims: geometric property discovery, IRCE algorithm, 2x speedup, maintained/improved accuracy, cross-model generalization."
  intro_structure: "4 paragraphs: P1=context (RLHF/GRPO foundation), P2=problem (three verifier bottlenecks), P3=key discovery (geometric clustering), P4=proposed framework and claims"
  notable_technique: "The 'silence the judge' metaphor creates a vivid antagonist (expensive external verifiers) that the method elegantly eliminates. The paper builds credibility by first establishing the geometric property empirically (Section 3) before presenting the framework (Section 4), making the method feel like a natural consequence of discovery rather than an arbitrary design choice."

figures:
  figure_count: 4
  figure1:
    type: "method_overview"
    description: "Side-by-side comparison of Latent-GRPO training pipeline vs traditional LLM-as-Judge reward. Left panel shows the full Latent-GRPO pipeline: input text → embedding layer → language model → last hidden states → latent reward function → rollout rewards → update training LLM. Right panel shows two boxes: (top) traditional reward with GPT logo producing binary Score:1/Score:0, (bottom) latent reward using hidden states through LRF block producing Score:High/Score:Low with a scatter plot showing green/red clustering. Three advantage badges: Dynamic rewards, Faster rewards, Continuous rewards."
    narrative_role: "Establishes the core architectural difference at a glance — positions the method as replacing the external judge with an internal geometric mechanism, while highlighting three key advantages."
    design_elements: ["side-by-side comparison layout", "color-coded pipeline flow", "3D transformer visualization", "advantage badges with icons", "scatter plot preview of clustering", "GPT logo as recognizable baseline anchor"]
    visual_style: "Rounded-corner panels with pastel background colors (light blue for main pipeline, light orange for traditional, light green for latent reward). Colorful flow arrows connecting components. Mix of schematic diagrams and small illustrative elements (clipboard icon, question mark). Dense information layout with multiple visual channels."
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "scatter_plot"
      what_compared: "2D PCA projection of 1,000 rollouts showing correct (green) vs incorrect (red) trajectory clustering, with truth centroid (gold star) and reward distribution heatmap"
      how_gain_highlighted: "Correct trajectories form a visually obvious dense green cluster around the gold star centroid, while incorrect trajectories scatter widely as red outliers — the separation is striking at a glance. Right panel adds a gradient heatmap showing reward distribution on the latent manifold."
      design_note: "Two-panel layout: left is PCA scatter with color coding, right shows same space with continuous reward gradient. The dual view reinforces both the discrete (correct/incorrect) and continuous (reward magnitude) interpretations of the geometric property."
    - figure_id: "Figure 4"
      viz_type: "multi_panel (box_plot + dual_axis_line_bar)"
      what_compared: "Panel (a): Global reward distribution across quality levels (correct, partial, incorrect). Panels (b-d): Group-level micro-ranking consistency in representative 8-trajectory groups."
      how_gain_highlighted: "Box plots show clear separation between quality levels. Dual-axis charts overlay bar charts (geometric scores) with line plots (external verifier scores) showing strong rank correlation."
      design_note: "4-panel grid validates the method at two granularities: global distribution separability and group-level ranking fidelity. Color-coded background regions (green/yellow/red) map to quality levels. Dual-axis overlay elegantly shows correlation between internal geometric scores and external verification without needing a separate correlation plot."
  ablation_figures: []
  figure_narrative_role: "Figure 1 (method overview + comparison) → Figure 2 (empirical evidence: clustering visualization) → Figure 3 (detailed framework pipeline) → Figure 4 (validation: scoring quality at global and group levels). The flow moves from 'what we propose' → 'why it works' → 'how it works in detail' → 'proof that it works at fine granularity.'"

tables:
  table_count: 5
  main_result_table:
    table_id: "Table 1"
    row_axis: "methods × model scales"
    col_axis: "datasets (GSM8K, MATH, Open-Platypus) × metrics (Accuracy, Time/epoch)"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "bold_best (Latent-GRPO consistently highlighted)"
    statistical_reporting: "single run numbers, no std reported"
    num_baselines: 2
    design_note: "Clean 3-dataset × 3-model-scale layout. Each dataset column pair shows accuracy + time. Rule-based absent for Open-Platypus (inapplicable to non-deterministic tasks) — this absence itself argues for Latent-GRPO's generality. Time column makes efficiency gain immediately visible alongside accuracy. Note on simulated QPS=2 for LLM-as-Judge contextualizes the timing comparison."
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["hidden state extraction method: Last Token vs Mean Pooling vs Weighted Mean"]
      variation_style: "full_numbers"
      design_note: "Simple 3-method × 3-scale grid on GSM8K. Clearly shows Last Token dominance. Accompanied by mechanistic explanation for why each alternative fails (noise from intermediate tokens, reasoning not localized at lexical markers)."
    - table_id: "Table 3"
      what_varied: ["centroid estimation algorithm: Mean Pool vs K-Means vs Eigen Centrality vs IRCE"]
      variation_style: "full_numbers"
      design_note: "4-method × 3-scale grid on GSM8K. Progressive improvement from simple to sophisticated methods. IRCE wins on both accuracy and computational efficiency — the dual-win argument is rare and compelling."
    - table_id: "Table 4"
      what_varied: ["capability preservation: base model vs LLM-Judge GRPO vs Latent-GRPO on unseen benchmarks"]
      variation_style: "full_numbers"
      design_note: "Tests on 5 unseen benchmarks (AIME24, AIME25, MATH-500, MMLU, BBH) to show no task-specific overfitting. Includes training time comparison. Demonstrates that Latent-GRPO preserves or improves base capabilities while being faster than LLM-Judge."
  supplementary_tables:
    in_appendix: true
    content: "Appendix F contains detailed hyperparameter tables for GRPO training configuration, IRCE algorithm configuration, and hardware specifications"
    reason: "Main text focuses on method-level comparisons and insights; implementation details deferred to appendix to maintain narrative flow and stay within page limits"
```

---

**zou2023repe.yaml**

```yaml
paper_key: "zou2023repe"
title: "Representation Engineering: A Top-Down Approach to AI Transparency"
venue: "arXiv 2023 (2310.01405)"
full_text_available: false

research:
  baselines:
    - "probing classifiers"
    - "circuit-level / neuron-level interpretability"
    - "activation patching"
  metrics:
    - {name: "representation reading accuracy", direction: "higher_better"}
    - {name: "representation control effectiveness", direction: "higher_better"}
  datasets:
    - {name: "honesty evaluation tasks", size: "N/A"}
    - {name: "harmlessness evaluation tasks", size: "N/A"}
    - {name: "power-seeking behavior tasks", size: "N/A"}
  ablation_dimensions:
    - "different cognitive phenomena (honesty, harmlessness, power-seeking)"
    - "monitoring (reading) vs manipulation (control)"
    - "population-level vs neuron/circuit-level analysis"
  training_recipe:
    optimizer: "N/A (inference-time technique)"
    lr: "N/A"
    hardware: "N/A"
  method_family: "representation engineering / activation analysis"

positioning:
  core_claim: "Population-level representations, rather than neurons or circuits, should be the center of analysis for AI transparency, enabling simple yet effective solutions for monitoring and controlling LLM cognitive phenomena like honesty and harmlessness."
  key_results: "Provides baselines for RepE techniques across honesty, harmlessness, and power-seeking; demonstrates both reading and control capabilities"
  limitations:
    - "Top-down approach may miss fine-grained mechanistic details"
    - "Relies on contrast pairs for representation identification"
    - "Effectiveness may vary across model architectures"
  relation_to_us: "foundation"

narrative: N/A
figures: N/A
tables: N/A
```

---

All 21 YAML files have been read and output in full. The files span the following categories:
- **8 full-text papers** with complete narrative/figures/tables analysis: burns2023ccs, gao2023scaling, li2023iti, mckinney2023fragility, obrien2025fewbadneurons, rimsky2024caa, skalse2022hacking, zhang2026latentgrpo
- **13 abstract-only papers** with research/positioning sections only: ackermann2026gradreg, casper2023openproblems, consistency2025bctact, denison2024subterfuge, shao2024grpo, shapira2026amplifies, sharma2023sycophancy, sinii2025smallvectors, turner2023actadd, wang2025internal, wei2024synthetic, wen2024mislead, zou2023repe

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c62ac26-57c4-4ee4-b70c-ac63c9d9cf18",
  "isSidechain": true,
  "agentId": "a316456ab2fcd624d",
  "requestId": "req_011CbMou4qoLKhX9jQBz51N6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0a38c6e4-26fb-45d3-8ee5-ae6a21c14221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/distiller_d3837e25",
  "sessionId": "ace074ae-dece-4078-ac87-f627b7ca36de",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPdvqzNzQ2U4tNeQvXuEXS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 47978,
      "cache_read_input_tokens": 8273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 47978,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
