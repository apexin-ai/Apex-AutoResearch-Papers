# Research conversation: Read every YAML file in /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/ an

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af2fbae3ae7b535a3.jsonl`
- **Structured JSON:** [`f3f3557dce474c829ae1.json`](../../sessions/f3/f3f3557dce474c829ae1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

57 recorded events

### User

_source line 1 · 2026-05-22T13:24:13.108Z_

Read every YAML file in /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/ and return their FULL contents verbatim. There are 25 files. Read each one completely — do not summarize or truncate. List them one by one with the filename as header.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "780f9fb7-816a-4375-97e1-701df4ed3f23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T13:24:15.199Z_

I'll read all YAML files in that directory. Let me first identify them.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "780f9fb7-816a-4375-97e1-701df4ed3f23",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSECnTyAcMXV2yBr6G",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "60cba6bf-3154-4a5c-8688-c419eb3e707d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CB1mZPRqjysM4sV5KHbqz1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15488,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15488,
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

_source line 3 · 2026-05-22T13:24:15.332Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01Qcz16nvzW9ratZgh21eFKZ`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60cba6bf-3154-4a5c-8688-c419eb3e707d",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSECnTyAcMXV2yBr6G",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1f8ef714-3b35-455a-93c4-1c61c0d91f91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CB1mZPRqjysM4sV5KHbqz1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15488,
      "cache_read_input_tokens": 0,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15488
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15488,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15488,
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

_source line 4 · 2026-05-22T13:24:15.354Z_

<details><summary>↩ Tool result · `toolu_01Qcz16nvzW9ratZgh21eFKZ`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/guo2024linguistic.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/chen2025scales.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/gambetta2024surplexity.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/sigma2026spectral.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/shumailov2024curse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/li2016diversity.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/noci2024mind.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/jing2022understanding.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/dey2024breaking.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/fu2025selfconsuming.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/feng2025escaping.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/barzilai2025consistency.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/gu2025datamixing.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/briesch2024selfconsuming.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/ba2024fill.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/alemohammad2024mad.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/kazdan2025collapse.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/he2025closer.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/dohmatob2024tale.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/dohmatob2025strong.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/dces2026counter.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/truong2025entropy.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/wang2026contaminated.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/du2026geometric.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/gauthier2026alignment.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f8ef714-3b35-455a-93c4-1c61c0d91f91",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "f4fbf0a9-df8d-4bb8-a950-9f19c12e1b1e",
  "sourceToolAssistantUUID": "1f8ef714-3b35-455a-93c4-1c61c0d91f91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-22T13:24:16.951Z_

Now I'll read all 25 YAML files. Since these are independent reads, I'll make multiple parallel calls:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f4fbf0a9-df8d-4bb8-a950-9f19c12e1b1e",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSNoTdJXciQtBVxPRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "50136f50-e32c-4fd2-be59-779cdc0d0f29",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV3WD4dqiHw6RuuQayGwYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2042,
      "cache_read_input_tokens": 15488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2042,
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

### Tool call

_source line 6 · 2026-05-22T13:24:17.197Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Y2B7GYhZJLAMotDRFDdjq4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/guo2024linguistic.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50136f50-e32c-4fd2-be59-779cdc0d0f29",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSNoTdJXciQtBVxPRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b6a3101c-b510-41a0-a704-d26e91bd6124",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV3WD4dqiHw6RuuQayGwYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2042,
      "cache_read_input_tokens": 15488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2042,
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

### Tool result

_source line 7 · 2026-05-22T13:24:17.230Z_

<details><summary>↩ Tool result · `toolu_01Y2B7GYhZJLAMotDRFDdjq4`</summary>

```text
1	paper_key: "guo2024linguistic"
2	title: "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text"
3	venue: "NAACL 2024 Findings"
4	full_text_available: true
5	
6	research:
7	  baselines: []  # intrinsic study - each iteration compared to human data (Gen 0)
8	  metrics:
9	    - {name: "Type-Token Ratio (TTR)", direction: "higher_better"}
10	    - {name: "Distinct-n (n=2,3)", direction: "higher_better"}
11	    - {name: "1-Self-BLEU", direction: "higher_better"}
12	    - {name: "Semantic diversity (cosine distance)", direction: "higher_better"}
13	    - {name: "Syntactic diversity (WL kernel distance)", direction: "higher_better"}
14	    - {name: "Perplexity", direction: "lower_better"}
15	  datasets:
16	    - {name: "XL-SUM", size: "306K", task: "news summarization"}
17	    - {name: "ACL Anthology", size: "40.5K", task: "scientific abstract generation"}
18	    - {name: "WritingPrompts", size: "272.6K", task: "story generation"}
19	  ablation_dimensions:
20	    - task_entropy_level (low/medium/high creativity)
21	    - mitigation_strategy (filtering vs mixing human data)
22	    - diversity_dimension (lexical vs semantic vs syntactic)
23	    - iteration_number (1-6)
24	  training_recipe:
25	    optimizer: "AdamW"
26	    epochs_per_iteration: 5
27	    hardware: "2x NVIDIA RTX A6000"
28	    base_model: "OPT-350M"
29	    iterations: 6
30	  method_family: "recursive_finetuning_analysis"
31	
32	positioning:
33	  core_claim: "Syntactic diversity suffers most severely under recursive synthetic training, more than lexical or semantic diversity — first work to measure and demonstrate this with novel WL-kernel syntactic diversity metrics."
34	  key_results: "Story gen TTR: 0.84%→0.61% (↓73% from human 2.23%); Syntactic diversity: 4.23→1.96 (↓60%); Semantic diversity most stable; Quality filtering amplifies diversity loss"
35	  limitations:
36	    - "English-only; metrics may not generalize to other languages"
37	    - "Only OPT-350M tested; larger scales not explored (700 GPU-hrs for story gen alone)"
38	    - "Cannot simulate realistic web-scale contamination setting"
39	  relation_to_us: "foundation"
40	
41	narrative:
42	  story_type: "突破局限型"
43	  hook: "Data scarcity crisis — world's entire high-quality text is ~17T tokens, major models already consuming 2T. Practitioners turning to synthetic data."
44	  tension: "Prior work showed model collapse (tail vanishing), but nobody measured HOW diversity declines across linguistic dimensions."
45	  key_insight: "Section 4 — syntactic diversity declines far more severely than lexical or semantic. Form degrades faster than content. Revealed via novel WL-kernel metric on dependency trees."
46	  argument_chain: "data scarcity → synthetic training necessity → recursive training simulation → comprehensive diversity metrics (lexical/semantic/syntactic) → syntactic decline most severe → mitigation strategies fail"
47	  contribution_framing: "3 contributions: (1) first comprehensive metrics across 3 diversity dimensions, (2) empirical evaluation across 3 NLG tasks with varying creativity, (3) mitigation analysis"
48	  intro_structure: "4 paragraphs: P1=data scarcity motivation, P2=prior work on model collapse, P3=research questions, P4=contributions"
49	  notable_technique: "Stratifying tasks by 'creativity demand' (low/medium/high entropy) creates natural gradient showing diversity loss scales with task freedom"
50	
51	figures:
52	  figure_count: 5
53	  figure1:
54	    type: "method_overview"
55	    description: "Recursive training cycle diagram: Data(0)→Model(1)→Data(1)→Model(2)→..."
56	    narrative_role: "Establishes the iterative contamination process being studied"
57	    design_elements: ["cycle arrows", "numbered iterations", "data/model alternation"]
58	    visual_style: "Simple flowchart with numbered nodes"
59	  result_figures:
60	    - figure_id: "Figure 2"
61	      viz_type: "line_plot"
62	      what_compared: "Distinct-3 and syntactic diversity across iterations under mitigation strategies"
63	      how_gain_highlighted: "Shows mitigation strategies barely move curves vs no-intervention baseline"
64	      design_note: "Dual y-axis for different metrics; mitigation failure is visually obvious"
65	    - figure_id: "Figure 3"
66	      viz_type: "bar_chart"
67	      what_compared: "Word frequency histograms across iterations"
68	      how_gain_highlighted: "Low-frequency word bins shrink visibly across iterations"
69	      design_note: "Histogram overlay makes tail disappearance concrete and intuitive"
70	  ablation_figures:
71	    - figure_id: "Figure 4"
72	      viz_type: "scatter"
73	      dimensions_varied: ["iteration number"]
74	      design_note: "t-SNE of syntactic embeddings showing spatial compaction — visually compelling proof of diversity collapse"
75	    - figure_id: "Figure 5"
76	      viz_type: "scatter"
77	      dimensions_varied: ["iteration number"]
78	      design_note: "t-SNE of semantic embeddings — less compaction, supporting claim that semantic diversity is more robust"
79	  figure_narrative_role: "Fig1(process setup) → Fig3(word-level evidence) → Fig4(syntactic collapse visualization) → Fig5(semantic stability contrast) → Fig2(mitigation failure)"
80	
81	tables:
82	  table_count: 2
83	  main_result_table:
84	    table_id: "Table 2"
85	    row_axis: "iterations (0-6)"
86	    col_axis: "metrics grouped by diversity dimension"
87	    row_organization: "by_iteration"
88	    col_organization: "grouped_by_metric_type"
89	    highlight_strategy: "arrows showing direction of change from human baseline"
90	    statistical_reporting: "single run values"
91	    num_baselines: 0  # intrinsic comparison to human data
92	    design_note: "Rows are iterations not methods; columns grouped by lexical/semantic/syntactic — readers see degradation trajectory per dimension"
93	  ablation_tables: []
94	  supplementary_tables:
95	    in_appendix: false
96	    content: "Table 1 shows example model outputs across iterations"
97	    reason: "Qualitative examples in main text to make abstract metrics concrete"
98	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6a3101c-b510-41a0-a704-d26e91bd6124",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "138a59ca-acb5-4703-a381-3ea85ce3983b",
  "sourceToolAssistantUUID": "b6a3101c-b510-41a0-a704-d26e91bd6124",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T13:24:17.593Z_

<details open><summary>🔧 Tool call — Read · `toolu_018YDS5kzzu3VQdasTuEJx2h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/chen2025scales.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "138a59ca-acb5-4703-a381-3ea85ce3983b",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSNoTdJXciQtBVxPRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "89e75bce-f7cc-4814-80e9-e284c03e3ddd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV3WD4dqiHw6RuuQayGwYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2042,
      "cache_read_input_tokens": 15488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2042,
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

### Tool result

_source line 9 · 2026-05-22T13:24:17.602Z_

<details><summary>↩ Tool result · `toolu_018YDS5kzzu3VQdasTuEJx2h`</summary>

```text
1	paper_key: "chen2025scales"
2	title: "Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios"
3	venue: "arXiv 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["Pythia-410M", "Pythia-1B", "Pythia-2.8B", "Pythia-6.9B", "Pythia-12B", "STaR", "Self-Instruct"]
8	  metrics:
9	    - {name: "accuracy", direction: "higher_better"}
10	    - {name: "calibration", direction: "lower_better"}
11	  datasets:
12	    - {name: "five diverse tasks (unspecified)", size: "N/A"}
13	  ablation_dimensions:
14	    - model_scale (410M-12B)
15	    - synthetic_ratio (0-50%)
16	    - iteration_count (1-3)
17	    - task_type (reasoning vs retrieval)
18	  training_recipe: {model_family: "Pythia", scale_range: "410M-12B"}
19	  method_family: "empirical_scaling_analysis"
20	
21	positioning:
22	  core_claim: "Models maintain stable performance up to 20% synthetic data; degradation accelerates beyond 30%; calibration degrades before accuracy (early warning); larger models more robust."
23	  key_results: "20% synthetic safe threshold; calibration as early warning; reasoning tasks degrade faster than retrieval"
24	  limitations: ["abstract-only extraction"]
25	  relation_to_us: "complementary"
26	
27	narrative: "N/A"
28	figures: "N/A"
29	tables: "N/A"
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89e75bce-f7cc-4814-80e9-e284c03e3ddd",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "9cedc624-8b74-4bd4-a6a8-5fe15d9a540b",
  "sourceToolAssistantUUID": "89e75bce-f7cc-4814-80e9-e284c03e3ddd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T13:24:18.036Z_

<details open><summary>🔧 Tool call — Read · `toolu_0192x7oRRuxvcGtnaQ1oK2gH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/gambetta2024surplexity.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9cedc624-8b74-4bd4-a6a8-5fe15d9a540b",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSNoTdJXciQtBVxPRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6ed60e84-eb96-43f6-90dc-8196e82fe50f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV3WD4dqiHw6RuuQayGwYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2042,
      "cache_read_input_tokens": 15488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2042,
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

### Tool result

_source line 11 · 2026-05-22T13:24:18.043Z_

<details><summary>↩ Tool result · `toolu_0192x7oRRuxvcGtnaQ1oK2gH`</summary>

```text
1	paper_key: "gambetta2024surplexity"
2	title: "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI"
3	venue: "arXiv 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["human-data filtering"]
8	  metrics:
9	    - {name: "next-token probability distribution", direction: "N/A"}
10	    - {name: "distributional skewedness", direction: "lower_better"}
11	  datasets: []
12	  ablation_dimensions:
13	    - surplexity_threshold
14	    - data_filtering_strategy
15	  training_recipe: {}
16	  method_family: "data_filtering_for_collapse_mitigation"
17	
18	positioning:
19	  core_claim: "Surprise-based data filtering (surplexity) preserves performance and diversity without needing to distinguish human vs AI data."
20	  key_results: "N/A"
21	  limitations: ["abstract-only extraction"]
22	  relation_to_us: "complementary"
23	
24	narrative: "N/A"
25	figures: "N/A"
26	tables: "N/A"
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ed60e84-eb96-43f6-90dc-8196e82fe50f",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "e277e757-c35c-4dbf-b7ce-dd968daf90d1",
  "sourceToolAssistantUUID": "6ed60e84-eb96-43f6-90dc-8196e82fe50f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T13:24:18.362Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L7XaThgsAgkBWDpYsHX55o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/sigma2026spectral.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e277e757-c35c-4dbf-b7ce-dd968daf90d1",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSNoTdJXciQtBVxPRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "da5672ee-698e-477a-974c-7579d4c4c676",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV3WD4dqiHw6RuuQayGwYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2042,
      "cache_read_input_tokens": 15488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2042,
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

### Tool result

_source line 13 · 2026-05-22T13:24:18.368Z_

<details><summary>↩ Tool result · `toolu_01L7XaThgsAgkBWDpYsHX55o`</summary>

```text
1	paper_key: "sigma2026spectral"
2	title: "SIGMA: Scalable Spectral Insights for LLM Model Collapse"
3	venue: "arXiv 2026"
4	full_text_available: false
5	
6	research:
7	  baselines: []
8	  metrics:
9	    - {name: "spectral bounds on embedding Gram matrices", direction: "N/A"}
10	    - {name: "representation space contraction", direction: "lower_better"}
11	  datasets: []
12	  ablation_dimensions:
13	    - model_scale
14	    - iteration_count
15	  training_recipe: {}
16	  method_family: "spectral_analysis_detection"
17	
18	positioning:
19	  core_claim: "Spectral analysis of embedding Gram matrices can quantify and predict model collapse onset with deterministic and stochastic bounds."
20	  key_results: "Scalable collapse detection via spectral bounds"
21	  limitations: ["abstract-only extraction"]
22	  relation_to_us: "complementary"
23	
24	narrative: "N/A"
25	figures: "N/A"
26	tables: "N/A"
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da5672ee-698e-477a-974c-7579d4c4c676",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "2a7c8abc-6ba5-4360-9801-5b1f6f688620",
  "sourceToolAssistantUUID": "da5672ee-698e-477a-974c-7579d4c4c676",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T13:24:18.644Z_

<details open><summary>🔧 Tool call — Read · `toolu_013UAgdUAMghAhgxVKWDdhVE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/shumailov2024curse.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a7c8abc-6ba5-4360-9801-5b1f6f688620",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSNoTdJXciQtBVxPRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9e47d561-a3c1-4847-b0f7-7f6b8b0f1f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV3WD4dqiHw6RuuQayGwYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2042,
      "cache_read_input_tokens": 15488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2042,
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

### Tool result

_source line 15 · 2026-05-22T13:24:18.650Z_

<details><summary>↩ Tool result · `toolu_013UAgdUAMghAhgxVKWDdhVE`</summary>

```text
1	paper_key: "shumailov2024curse"
2	title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
3	venue: "Nature 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["VAE", "Gaussian Mixture Models", "LLMs"]
8	  metrics:
9	    - {name: "distribution tail preservation", direction: "higher_better"}
10	    - {name: "model degradation", direction: "lower_better"}
11	  datasets: []
12	  ablation_dimensions:
13	    - model_type (VAE, GMM, LLM)
14	    - iteration_count
15	  training_recipe: {}
16	  method_family: "model_collapse_theory"
17	
18	positioning:
19	  core_claim: "Training on model-generated data causes irreversible defects where tails of original distribution disappear — coined 'Model Collapse'."
20	  key_results: "Model collapse demonstrated across VAEs, GMMs, and LLMs"
21	  limitations: ["abstract-only extraction"]
22	  relation_to_us: "foundation"
23	
24	narrative: "N/A"
25	figures: "N/A"
26	tables: "N/A"
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e47d561-a3c1-4847-b0f7-7f6b8b0f1f66",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "ab859d34-1db6-4655-a11e-3231b96ede6e",
  "sourceToolAssistantUUID": "9e47d561-a3c1-4847-b0f7-7f6b8b0f1f66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T13:24:18.854Z_

<details open><summary>🔧 Tool call — Read · `toolu_018wkQER1FDoiAjXeixM9Doc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/li2016diversity.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab859d34-1db6-4655-a11e-3231b96ede6e",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSNoTdJXciQtBVxPRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "39e57ad1-af43-4595-81f4-03d6f3d7e5d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV3WD4dqiHw6RuuQayGwYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2042,
      "cache_read_input_tokens": 15488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2042,
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

### Tool result

_source line 17 · 2026-05-22T13:24:18.861Z_

<details><summary>↩ Tool result · `toolu_018wkQER1FDoiAjXeixM9Doc`</summary>

```text
1	paper_key: "li2016diversity"
2	title: "A Diversity-Promoting Objective Function for Neural Conversation Models"
3	venue: "NAACL 2016"
4	full_text_available: false
5	
6	research:
7	  baselines: ["seq2seq with MLE"]
8	  metrics:
9	    - {name: "BLEU", direction: "higher_better"}
10	    - {name: "human evaluation", direction: "higher_better"}
11	  datasets:
12	    - {name: "two conversational datasets", size: "N/A"}
13	  ablation_dimensions:
14	    - objective_function (MLE vs MMI)
15	  training_recipe: {}
16	  method_family: "diversity_promoting_objective"
17	
18	positioning:
19	  core_claim: "Maximum Mutual Information (MMI) objective produces more diverse and appropriate responses than standard MLE in dialogue."
20	  key_results: "MMI outperforms MLE on diversity and appropriateness"
21	  limitations: ["abstract-only extraction"]
22	  relation_to_us: "foundation"
23	
24	narrative: "N/A"
25	figures: "N/A"
26	tables: "N/A"
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39e57ad1-af43-4595-81f4-03d6f3d7e5d7",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "83d234e6-2c75-4fc4-984f-a5fefa19b9cd",
  "sourceToolAssistantUUID": "39e57ad1-af43-4595-81f4-03d6f3d7e5d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T13:24:19.283Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Rdwb1YsqPmS13j32DFYX9x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/noci2024mind.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83d234e6-2c75-4fc4-984f-a5fefa19b9cd",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSNoTdJXciQtBVxPRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dae3f722-9f4e-4e24-b88a-6ae4cd548eee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV3WD4dqiHw6RuuQayGwYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2042,
      "cache_read_input_tokens": 15488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2042,
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

### Tool result

_source line 19 · 2026-05-22T13:24:19.288Z_

<details><summary>↩ Tool result · `toolu_01Rdwb1YsqPmS13j32DFYX9x`</summary>

```text
1	paper_key: "noci2024mind"
2	title: "Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers"
3	venue: "NeurIPS 2024"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Standard softmax attention (with spectral gap)"
9	    - "Identity attention matrix"
10	    - "Orthogonal value matrices"
11	  metrics:
12	    - {name: "Stable rank sr(M)", direction: "higher_better"}
13	    - {name: "Gradient norm", direction: "context_dependent"}
14	  datasets:
15	    - {name: "Synthetic Heaviside function", size: "synthetic"}
16	  ablation_dimensions:
17	    - depth (L=1,2,4,8)
18	    - width/context_length (T=10-1000)
19	    - initialization_scheme (default, Xavier, He)
20	    - architecture_variant (single-layer, +LayerNorm, +skip connections)
21	    - spectral_gap_removal (with/without)
22	  training_recipe:
23	    architecture: "single-head attention-only transformers"
24	    initialization: "N(0,1) for value matrices"
25	    task: "Heaviside function learning"
26	    hardware: "N/A (theoretical focus)"
27	  method_family: "spectral_analysis_signal_propagation"
28	
29	positioning:
30	  core_claim: "Softmax attention creates a spectral gap (eigenvalue 1 vs O(T^{-1/2}) bulk) causing a NEW form of rank collapse in width (sequence length), distinct from known depth collapse. Removing this gap via A⊥ = A - T^{-1}·1 prevents width collapse."
31	  key_results: "Width collapse rate |sr-1|=O(T^{1-4L}); proposed fix makes rank scale linearly with T; gradient explosion bounded by T^{L-1}"
32	  limitations:
33	    - "Analysis primarily for single-layer; multi-layer key-query attention has unknown spectral properties"
34	    - "Multiple outlier eigenvalues emerge beyond first layer, reducing fix effectiveness"
35	    - "Dynamical isometry provably unachievable (Prop 7-8)"
36	    - "Training experiments inconclusive; no large-scale validation"
37	  relation_to_us: "foundation"
38	
39	narrative:
40	  story_type: "突破局限型"
41	  hook: "Transformers excel but face training instability — what goes wrong at initialization in softmax attention?"
42	  tension: "Prior work identified rank collapse in depth, but missed a fundamental width-dependent collapse caused by attention's spectral structure."
43	  key_insight: "Section 2, Theorem 2 — the spectral gap between eigenvalue 1 and the O(T^{-1/2}) bulk is the root cause. Removing it (A⊥) resolves width collapse and controls gradients."
44	  argument_chain: "training instability → spectral analysis of attention at init → identify spectral gap → prove width collapse + gradient explosion → propose A⊥ fix → theoretical guarantees → experiments verify (partially)"
45	  contribution_framing: "4 contributions: diagnose width collapse, identify spectral gap cause, propose fix with proofs, analyze modified model's kernel/Jacobian spectra"
46	  intro_structure: "3 sections: S1.1=background on signal propagation, S1.2=contributions, S1.3=organization"
47	  notable_technique: "Using free probability theory (free multiplicative convolution) to derive exact spectral distributions — mathematically rigorous yet yields clean design insight (subtract the rank-1 component)"
48	
49	figures:
50	  figure_count: 8
51	  figure1:
52	    type: "problem_illustration"
53	    description: "Eigenvalue distribution of Random Markov matrix: circular bulk at O(T^{-1/2}) radius with isolated eigenvalue at 1"
54	    narrative_role: "Visually establishes the spectral gap — the core phenomenon the paper addresses"
55	    design_elements: ["eigenvalue scatter plot", "bulk vs outlier annotation", "scaling annotation"]
56	    visual_style: "Complex plane scatter with circle overlay showing bulk distribution"
57	  result_figures:
58	    - figure_id: "Figure 2"
59	      viz_type: "line_plot"
60	      what_compared: "Stable rank vs context length (width collapse) and vs depth, with/without spectral gap removal"
61	      how_gain_highlighted: "Proposed fix maintains linear rank growth vs flat collapse"
62	      design_note: "Dual-panel (width vs depth); theoretical predictions overlaid on empirical curves"
63	    - figure_id: "Figure 4"
64	      viz_type: "line_plot"
65	      what_compared: "Gradient norm scaling with width at layer 1"
66	      how_gain_highlighted: "Linear trend confirmed across architectures"
67	      design_note: "Log-log scale reveals power-law relationships clearly"
68	    - figure_id: "Figure 5"
69	      viz_type: "line_plot"
70	      what_compared: "Gradient norm vs depth for Random Markov vs key-query attention"
71	      how_gain_highlighted: "Fix controls gradients for Random Markov but not fully for key-query"
72	      design_note: "Honest about limitations — key-query case shows fix is partial"
73	  ablation_figures:
74	    - figure_id: "Figure 3"
75	      viz_type: "line_plot"
76	      dimensions_varied: ["architecture variant (base, +LN, +skip)"]
77	      design_note: "Shows width collapse is universal across architectures — not an artifact of simplified setup"
78	    - figure_id: "Figure 8"
79	      viz_type: "line_plot"
80	      dimensions_varied: ["initialization scheme (Xavier, He, upscaled skip)"]
81	      design_note: "Reveals degenerate behavior under standard initialization choices — motivates rethinking defaults"
82	  figure_narrative_role: "Fig1(spectral gap visualization) → Fig2(collapse proof) → Fig3(universality across architectures) → Fig4-5(gradient analysis) → Fig6-7(training + eigenvalue evolution) → Fig8(initialization pitfalls)"
83	
84	tables:
85	  table_count: 0
86	  main_result_table: "N/A — purely theoretical paper, all results presented as propositions + figures"
87	  ablation_tables: []
88	  supplementary_tables:
89	    in_appendix: true
90	    content: "Proof details and additional experimental configurations"
91	    reason: "Theoretical paper — proofs in appendix, key results as numbered propositions in main text"
92	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dae3f722-9f4e-4e24-b88a-6ae4cd548eee",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "417719f9-ff67-47ef-951a-16bf1173ed81",
  "sourceToolAssistantUUID": "dae3f722-9f4e-4e24-b88a-6ae4cd548eee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-22T13:24:19.732Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Xy17BSVcREeR7m74LwjDiE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/jing2022understanding.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "417719f9-ff67-47ef-951a-16bf1173ed81",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSNoTdJXciQtBVxPRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ce4fb794-322a-4fc8-9697-31a220dbb49a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV3WD4dqiHw6RuuQayGwYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2042,
      "cache_read_input_tokens": 15488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2042,
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

### Tool result

_source line 21 · 2026-05-22T13:24:19.741Z_

<details><summary>↩ Tool result · `toolu_01Xy17BSVcREeR7m74LwjDiE`</summary>

```text
1	paper_key: "jing2022understanding"
2	title: "Understanding Dimensional Collapse in Contrastive Self-supervised Learning"
3	venue: "ICLR 2022"
4	full_text_available: false
5	
6	research:
7	  baselines: ["SimCLR (linear projector)"]
8	  metrics:
9	    - {name: "ImageNet classification accuracy", direction: "higher_better"}
10	  datasets:
11	    - {name: "ImageNet", size: "1.28M images"}
12	  ablation_dimensions:
13	    - projector_type
14	    - representation_dimensionality
15	  training_recipe: {}
16	  method_family: "dimensional_collapse_analysis"
17	
18	positioning:
19	  core_claim: "Contrastive learning embeddings suffer dimensional collapse (spanning lower-dimensional subspace); DirectCLR directly optimizes representation space without trainable projector."
20	  key_results: "DirectCLR outperforms SimCLR with linear projector on ImageNet"
21	  limitations: ["abstract-only extraction"]
22	  relation_to_us: "orthogonal"
23	
24	narrative: "N/A"
25	figures: "N/A"
26	tables: "N/A"
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ce4fb794-322a-4fc8-9697-31a220dbb49a",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "4d6691ff-89d3-4dd4-81a4-ef27625d2c2c",
  "sourceToolAssistantUUID": "ce4fb794-322a-4fc8-9697-31a220dbb49a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T13:24:19.929Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EW99Hxsv2hY2EwYDhQvGGv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/dey2024breaking.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d6691ff-89d3-4dd4-81a4-ef27625d2c2c",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSNoTdJXciQtBVxPRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "50b3cd68-77a9-4b23-85bc-8047a6381107",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV3WD4dqiHw6RuuQayGwYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2042,
      "cache_read_input_tokens": 15488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2042,
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

### Tool result

_source line 23 · 2026-05-22T13:24:19.945Z_

<details><summary>↩ Tool result · `toolu_01EW99Hxsv2hY2EwYDhQvGGv`</summary>

```text
1	paper_key: "dey2024breaking"
2	title: "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"
3	venue: "ICML 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["data replacement loop", "data accumulation loop"]
8	  metrics:
9	    - {name: "cross-entropy validation loss", direction: "lower_better"}
10	    - {name: "test loss/MSE", direction: "lower_better"}
11	  datasets:
12	    - {name: "TinyStories", size: "470M tokens"}
13	    - {name: "GEOM-Drugs", size: "40k molecular conformations"}
14	    - {name: "CelebA", size: "200k face images"}
15	  ablation_dimensions:
16	    - data_regime (replacement vs accumulation)
17	    - model_family (GPT-2, Llama2, GeoDiff, VAE)
18	    - model_scale (12M/42M/125M)
19	  training_recipe: {models: "GPT-2, Llama2 (12M/42M/125M), GeoDiff, VAE"}
20	  method_family: "data_accumulation_for_collapse_prevention"
21	
22	positioning:
23	  core_claim: "Model collapse is NOT inevitable — accumulating synthetic data alongside real data (instead of replacing) avoids collapse. Proven theoretically for linear models and empirically across LMs, diffusion models, and VAEs."
24	  key_results: "Accumulation regime: bounded test error; Replacement regime: collapse"
25	  limitations: ["abstract-only extraction"]
26	  relation_to_us: "competitor"
27	
28	narrative: "N/A"
29	figures: "N/A"
30	tables: "N/A"
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50b3cd68-77a9-4b23-85bc-8047a6381107",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "47ac1e54-0a1f-429c-950c-89ee5d35b0bb",
  "sourceToolAssistantUUID": "50b3cd68-77a9-4b23-85bc-8047a6381107",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-22T13:24:20.569Z_

<details open><summary>🔧 Tool call — Read · `toolu_01V5NyjidR3TUQ4vDzwSuvRk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/fu2025selfconsuming.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47ac1e54-0a1f-429c-950c-89ee5d35b0bb",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSNoTdJXciQtBVxPRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a6874293-1dc6-4b24-96ca-dc867ec5a182",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV3WD4dqiHw6RuuQayGwYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2042,
      "cache_read_input_tokens": 15488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2042,
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

### Tool call

_source line 25 · 2026-05-22T13:24:20.576Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FcAuvcLFVZUB1Tg5Udt4hu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/feng2025escaping.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6874293-1dc6-4b24-96ca-dc867ec5a182",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSNoTdJXciQtBVxPRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4db32bc1-8fb0-4c9e-b51f-d94abc44bb60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV3WD4dqiHw6RuuQayGwYx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2042,
      "cache_read_input_tokens": 15488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2042,
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

### Tool result

_source line 26 · 2026-05-22T13:24:20.582Z_

<details><summary>↩ Tool result · `toolu_01V5NyjidR3TUQ4vDzwSuvRk`</summary>

```text
1	paper_key: "fu2025selfconsuming"
2	title: "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops"
3	venue: "ICLR 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["Self-consuming Training Loop (STL)"]
8	  metrics:
9	    - {name: "Total Variation distance", direction: "lower_better"}
10	    - {name: "KL divergence", direction: "lower_better"}
11	    - {name: "population/empirical risk", direction: "lower_better"}
12	  datasets: []
13	  ablation_dimensions:
14	    - real_synthetic_ratio
15	    - model_architecture
16	    - synthetic_data_sizing
17	  training_recipe: {focus: "theoretical, transformer ICL analysis"}
18	  method_family: "recursive_stability_theory"
19	
20	positioning:
21	  core_claim: "Introduces 'recursive stability' concept; shows both model architecture and real/synthetic data proportion influence STL success. Even constant-sized real data proportion ensures transformer ICL convergence."
22	  key_results: "Convergence bound O(n^{-1}log^2(n) + n^{-1/2}log(n) + n^{-1/4}) for transformer ICL"
23	  limitations: ["abstract-only extraction"]
24	  relation_to_us: "foundation"
25	
26	narrative: "N/A"
27	figures: "N/A"
28	tables: "N/A"
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6874293-1dc6-4b24-96ca-dc867ec5a182",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "eecbdd12-2a67-4eea-88f1-742590301e50",
  "sourceToolAssistantUUID": "a6874293-1dc6-4b24-96ca-dc867ec5a182",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-22T13:24:20.591Z_

<details><summary>↩ Tool result · `toolu_01FcAuvcLFVZUB1Tg5Udt4hu`</summary>

```text
1	paper_key: "feng2025escaping"
2	title: "Escaping Model Collapse via Synthetic Data Verification"
3	venue: "NeurIPS 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["unguided self-consuming loop"]
8	  metrics:
9	    - {name: "model collapse rate", direction: "lower_better"}
10	    - {name: "improvement/convergence bounds", direction: "N/A"}
11	  datasets:
12	    - {name: "MNIST", size: "60K", task: "VAE experiments"}
13	    - {name: "XSUM", size: "N/A", task: "LM fine-tuning"}
14	  ablation_dimensions:
15	    - verifier_reliability
16	    - training_iteration
17	  training_recipe: {models: "linear regression (theory), VAE, SmolLM2-135M"}
18	  method_family: "verifier_guided_retraining"
19	
20	positioning:
21	  core_claim: "External verification (human/superior model) prevents collapse short-term, but unless verifier is perfectly reliable, gains plateau and converge toward verifier's 'knowledge center'."
22	  key_results: "Near-term improvement with verifier; long-term convergence to verifier limit"
23	  limitations: ["abstract-only extraction"]
24	  relation_to_us: "complementary"
25	
26	narrative: "N/A"
27	figures: "N/A"
28	tables: "N/A"
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4db32bc1-8fb0-4c9e-b51f-d94abc44bb60",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "db82b6d4-f9a8-4b84-8905-0931b7c48d2c",
  "sourceToolAssistantUUID": "4db32bc1-8fb0-4c9e-b51f-d94abc44bb60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-22T13:24:20.886Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DKp4ZiHuQ7dry5F7ej7V6A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/barzilai2025consistency.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db82b6d4-f9a8-4b84-8905-0931b7c48d2c",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSNoTdJXciQtBVxPRz",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2ac1bc4f-4073-4ab1-b6a0-c744c6b7dd9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VV3WD4dqiHw6RuuQayGwYx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2042,
      "cache_read_input_tokens": 15488,
      "output_tokens": 974,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2042
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 974,
          "cache_read_input_tokens": 15488,
          "cache_creation_input_tokens": 2042,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2042,
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

_source line 29 · 2026-05-22T13:24:20.893Z_

<details><summary>↩ Tool result · `toolu_01DKp4ZiHuQ7dry5F7ej7V6A`</summary>

```text
1	paper_key: "barzilai2025consistency"
2	title: "When Models Don't Collapse: On the Consistency of Iterative MLE"
3	venue: "ICML 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["iterative MLE with data accumulation"]
8	  metrics:
9	    - {name: "non-asymptotic error bounds", direction: "lower_better"}
10	    - {name: "collapse rate", direction: "lower_better"}
11	  datasets: []
12	  ablation_dimensions:
13	    - real_data_fraction_decay_rate
14	    - statistical_regularity_conditions
15	  training_recipe: {focus: "theoretical, MLE consistency analysis"}
16	  method_family: "iterative_MLE_theory"
17	
18	positioning:
19	  core_claim: "Under standard MLE consistency assumptions, collapse can be avoided even as real data fraction vanishes. But without these assumptions, collapse can occur arbitrarily quickly even with real data present."
20	  key_results: "Non-asymptotic bounds on iterative MLE; first rigorous collapse-with-accumulation counterexamples"
21	  limitations: ["abstract-only extraction"]
22	  relation_to_us: "foundation"
23	
24	narrative: "N/A"
25	figures: "N/A"
26	tables: "N/A"
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ac1bc4f-4073-4ab1-b6a0-c744c6b7dd9e",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "60607174-2468-4041-b4ad-efcac6f309f4",
  "sourceToolAssistantUUID": "2ac1bc4f-4073-4ab1-b6a0-c744c6b7dd9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-22T13:24:22.500Z_

Now reading the remaining 13 files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60607174-2468-4041-b4ad-efcac6f309f4",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1574f7b2-3ca0-4aca-8183-da643f408324",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
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

### Tool call

_source line 31 · 2026-05-22T13:24:23.591Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QdricNtPRbfco2qTwxbkBV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/gu2025datamixing.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1574f7b2-3ca0-4aca-8183-da643f408324",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c468354-b12f-465d-a5d7-881fba09f841",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
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

### Tool result

_source line 32 · 2026-05-22T13:24:23.611Z_

<details><summary>↩ Tool result · `toolu_01QdricNtPRbfco2qTwxbkBV`</summary>

```text
1	paper_key: "gu2025datamixing"
2	title: "Data Mixing Can Induce Phase Transitions in Knowledge Acquisition"
3	venue: "ICLR 2025 Spotlight"
4	full_text_available: false
5	
6	research:
7	  baselines: ["smooth scaling law assumption"]
8	  metrics:
9	    - {name: "biography memorization rate", direction: "higher_better"}
10	    - {name: "critical mixing ratio threshold", direction: "N/A"}
11	  datasets:
12	    - {name: "synthetic biography dataset", size: "N/A"}
13	    - {name: "web-scraped data", size: "N/A"}
14	  ablation_dimensions:
15	    - mixing_ratio
16	    - model_size
17	    - training_duration
18	  training_recipe: {focus: "controlled experiments on data mixing"}
19	  method_family: "phase_transition_analysis"
20	
21	positioning:
22	  core_claim: "Knowledge acquisition from mixed data exhibits phase transitions (not smooth scaling) w.r.t. mixing ratio and model size. Modeled as knapsack capacity allocation with power-law phase transition."
23	  key_results: "Critical threshold in mixing ratio and model size for knowledge memorization; power-law relationship"
24	  limitations: ["abstract-only extraction"]
25	  relation_to_us: "complementary"
26	
27	narrative: "N/A"
28	figures: "N/A"
29	tables: "N/A"
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c468354-b12f-465d-a5d7-881fba09f841",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "c374e96b-e0bd-4107-b476-82555dd19045",
  "sourceToolAssistantUUID": "4c468354-b12f-465d-a5d7-881fba09f841",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T13:24:24.001Z_

<details open><summary>🔧 Tool call — Read · `toolu_011LRJAL5kF8orePwhKVrcue`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/briesch2024selfconsuming.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c374e96b-e0bd-4107-b476-82555dd19045",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4f0930b7-8f80-4750-9151-e3ad3a475f25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
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

### Tool result

_source line 34 · 2026-05-22T13:24:24.007Z_

<details><summary>↩ Tool result · `toolu_011LRJAL5kF8orePwhKVrcue`</summary>

```text
1	paper_key: "briesch2024selfconsuming"
2	title: "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop"
3	venue: "arXiv 2024"
4	full_text_available: false
5	
6	research:
7	  baselines: ["Full Synthetic cycle", "Balanced cycle", "Incremental cycle", "Expanding cycle"]
8	  metrics:
9	    - {name: "syntactic correctness", direction: "higher_better"}
10	    - {name: "semantic correctness", direction: "higher_better"}
11	    - {name: "Levenshtein diversity", direction: "higher_better"}
12	    - {name: "unique expression count", direction: "higher_better"}
13	  datasets:
14	    - {name: "Logic expression dataset", size: "10K unique Boolean expressions"}
15	  ablation_dimensions:
16	    - data_cycle_regime (full_synthetic, balanced, incremental, expanding)
17	    - synthetic_data_proportion
18	    - generation_count
19	  training_recipe: {model: "GPT-style transformer (6L, 6H, 384d, ~10.6M params)", training: "from scratch"}
20	  method_family: "self_consuming_loop_analysis"
21	
22	positioning:
23	  core_claim: "LLM diversity collapse confirmed: correctness may improve initially but diversity declines depending on synthetic data proportion. Full synthetic loop collapses within <10 generations."
24	  key_results: "Full synthetic: collapse <10 gens; fresh human data slows but cannot halt decline"
25	  limitations: ["abstract-only extraction"]
26	  relation_to_us: "foundation"
27	
28	narrative: "N/A"
29	figures: "N/A"
30	tables: "N/A"
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f0930b7-8f80-4750-9151-e3ad3a475f25",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "3366db3b-0c09-4f57-8bfc-2e4f31ceb6ff",
  "sourceToolAssistantUUID": "4f0930b7-8f80-4750-9151-e3ad3a475f25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T13:24:24.190Z_

<details open><summary>🔧 Tool call — Read · `toolu_0192ekagfA6Gvfsdwyo1Ghz6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/ba2024fill.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3366db3b-0c09-4f57-8bfc-2e4f31ceb6ff",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e19ad8b9-d74a-46dc-9731-edc2a148bf4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
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

### Tool result

_source line 36 · 2026-05-22T13:24:24.197Z_

<details><summary>↩ Tool result · `toolu_0192ekagfA6Gvfsdwyo1Ghz6`</summary>

```text
1	paper_key: "ba2024fill"
2	title: "Fill In The Gaps: Model Calibration and Generalization with Synthetic Data"
3	venue: "EMNLP 2024"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "BERTbase (standard)"
9	    - "Isotonic Regression"
10	    - "Platt Scaling"
11	    - "Monte Carlo Dropout"
12	    - "Temperature Scaling"
13	  metrics:
14	    - {name: "Accuracy (ACC)", direction: "higher_better"}
15	    - {name: "Expected Calibration Error (ECE)", direction: "lower_better"}
16	  datasets:
17	    - {name: "TC (Complaints)", size: "3449", task: "text classification"}
18	    - {name: "SUBJ (Subjectivity)", size: "10K", task: "text classification"}
19	    - {name: "B77 (Banking77)", size: "257", task: "text classification"}
20	    - {name: "SE (SentEval)", size: "3762", task: "text classification"}
21	    - {name: "Arxiv-10", size: "6K", task: "text classification (OOD)"}
22	    - {name: "Medical", size: "3722", task: "text classification (OOD)"}
23	  ablation_dimensions:
24	    - num_bins (10, 15, 20)
25	    - synthetic_strategy (Synthesis vs Synthesis+)
26	    - LLM_accuracy_vs_calibration_correlation
27	  training_recipe:
28	    optimizer: "Adam"
29	    lr: "1e-6"
30	    epochs: 5
31	    batch_size: 32
32	    dropout: 0.5
33	    hardware: "NVIDIA P100 GPUs"
34	    base_model: "BERTbase"
35	    synthetic_generator: "Llama-2-7b-chat-hf (T=0.1)"
36	  method_family: "synthetic_data_for_calibration"
37	
38	positioning:
39	  core_claim: "LLM-generated synthetic data targeted at poorly-calibrated reliability diagram bins can simultaneously improve accuracy (up to 34%) and reduce ECE (up to 33%), with PAC-learning theoretical backing."
40	  key_results: "Avg up to 34% ACC increase, 33% ECE decrease; Synthesis+ (add synthetic) generally outperforms Synthesis (replace); LLM prediction accuracy matters more than LLM calibration for downstream improvement"
41	  limitations:
42	    - "Excessive synthetic data can cause overfitting"
43	    - "Only binary text classification tested"
44	    - "Single LLM (Llama-2-7b) used; no LLM comparison"
45	  relation_to_us: "orthogonal"
46	
47	narrative:
48	  story_type: "化繁为简型"
49	  hook: "Model calibration is critical for trustworthy AI, but existing calibration methods hurt accuracy."
50	  tension: "Post-hoc calibration (Platt, isotonic, temperature scaling) adjusts probabilities but can degrade accuracy. No method addresses both simultaneously."
51	  key_insight: "Section 3.1 — PAC framework proves ECE bound can be reduced by adding synthetic data that fills gaps in reliability diagram. The insight is geometric: target specific miscalibrated confidence bins."
52	  argument_chain: "calibration-accuracy tradeoff → PAC-derived ECE bound → LLM-generated synthetic data fills reliability gaps → simultaneous improvement → validated on 6 NLP datasets"
53	  contribution_framing: "3 contributions: (1) ECE bound derivation via PAC, (2) gap-filling calibration strategy, (3) empirical validation of LLM synthetic data for calibration"
54	  intro_structure: "5 paragraphs: P1=NLP model success, P2=beyond accuracy (calibration importance), P3=modern NNs are miscalibrated, P4=synthetic data motivation, P5=approach + contributions"
55	  notable_technique: "Using reliability diagram 'gaps' as a visual + mathematical target for synthetic data generation — makes abstract calibration theory actionable"
56	
57	figures:
58	  figure_count: 3
59	  figure1:
60	    type: "method_overview"
61	    description: "Framework: train model → identify miscalibrated bins in reliability diagram → generate synthetic data via LLM with target probabilities → retrain"
62	    narrative_role: "End-to-end pipeline visualization that makes the method immediately comprehensible"
63	    design_elements: ["pipeline flow", "reliability diagram inset", "LLM generation step"]
64	    visual_style: "Left-to-right flow with color-coded steps"
65	  result_figures:
66	    - figure_id: "Figure 2"
67	      viz_type: "bar_chart"
68	      what_compared: "Reliability diagram before/after showing target bin identification and synthetic data placement"
69	      how_gain_highlighted: "Gap between confidence and accuracy visually shrinks"
70	      design_note: "Two-panel before/after comparison of reliability diagram — intuitive"
71	  ablation_figures:
72	    - figure_id: "Figure 3"
73	      viz_type: "line_plot"
74	      dimensions_varied: ["iteration of calibration process on toy 1D example"]
75	      design_note: "Toy example makes abstract PAC theory concrete — shows logistic curve convergence"
76	  figure_narrative_role: "Fig1(method overview) → Fig2(bin targeting concept) → Fig3(toy validation)"
77	
78	tables:
79	  table_count: 5
80	  main_result_table:
81	    table_id: "Table 4"
82	    row_axis: "methods"
83	    col_axis: "datasets × (ACC, ECE)"
84	    row_organization: "by_category"
85	    col_organization: "grouped_by_dataset"
86	    highlight_strategy: "highlighted values considering both ACC and ECE, weighing more on ECE"
87	    statistical_reporting: "mean (std) across runs"
88	    num_baselines: 5
89	    design_note: "Dual-metric per dataset; explicit note about weighting ECE more in highlighting — transparent evaluation criteria"
90	  ablation_tables:
91	    - table_id: "Table 5"
92	      what_varied: ["LLM_ACC vs LLM_ECE correlation with downstream improvement"]
93	      variation_style: "full_numbers"
94	      design_note: "Pearson correlation matrix reveals LLM accuracy matters more than LLM calibration — counter-intuitive finding"
95	  supplementary_tables:
96	    in_appendix: true
97	    content: "Table 6 (model params), Table 7 (system prompts for generation), Table 8 (generation examples)"
98	    reason: "Reproducibility details (prompts, hyperparams) in appendix; main text focuses on results"
99	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e19ad8b9-d74a-46dc-9731-edc2a148bf4e",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "416b7e51-d304-451b-a25c-8e720e66a05a",
  "sourceToolAssistantUUID": "e19ad8b9-d74a-46dc-9731-edc2a148bf4e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T13:24:24.639Z_

<details open><summary>🔧 Tool call — Read · `toolu_017kCTBrC2yQPNvGanTixaaE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/alemohammad2024mad.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "416b7e51-d304-451b-a25c-8e720e66a05a",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "78554d93-4969-45e9-a3a6-6be2e978cffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
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

### Tool result

_source line 38 · 2026-05-22T13:24:24.648Z_

<details><summary>↩ Tool result · `toolu_017kCTBrC2yQPNvGanTixaaE`</summary>

```text
1	paper_key: "alemohammad2024mad"
2	title: "Self-Consuming Generative Models Go MAD"
3	venue: "ICLR 2024"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "DDPM (conditional, T=500)"
9	    - "StyleGAN-2 (unconditional)"
10	    - "WGAN-GP"
11	    - "Normalizing Flows (GLOW)"
12	    - "Gaussian/GMM (analytical)"
13	  metrics:
14	    - {name: "FID (Fréchet Inception Distance)", direction: "lower_better"}
15	    - {name: "Precision (k=5 NN)", direction: "higher_better"}
16	    - {name: "Recall (k=5 NN)", direction: "higher_better"}
17	    - {name: "Wasserstein distance", direction: "lower_better"}
18	    - {name: "Effective sample size (n_e)", direction: "higher_better"}
19	  datasets:
20	    - {name: "MNIST", size: "60K"}
21	    - {name: "FFHQ", size: "70K (downsampled to 128x128)"}
22	    - {name: "2D Rosenbrock distribution", size: "10K synthetic"}
23	    - {name: "25-mode 2D GMM", size: "synthetic"}
24	  ablation_dimensions:
25	    - loop_type (fully_synthetic, augmentation, fresh_data)
26	    - sampling_bias_lambda (0-1)
27	    - generation_count
28	    - model_architecture (DDPM, StyleGAN2, WGAN, NF, Gaussian)
29	    - fresh_data_amount (n_r)
30	  training_recipe:
31	    DDPM: "conditional, T=500 diffusion steps, 10% conditioning dropout for CFG"
32	    StyleGAN2: "unconditional, FFHQ 128x128"
33	    NF_GLOW: "8 coupling layers, hidden_dim=64, 20 epochs, batch=256"
34	    data_sizes: "DDPM: 60K/iter; StyleGAN: 70K/iter"
35	  method_family: "autophagous_loop_analysis"
36	
37	positioning:
38	  core_claim: "Without enough fresh real data in each generation, self-consuming generative models inevitably suffer Model Autophagy Disorder (MAD) — either quality (precision) or diversity (recall) progressively decreases. Sampling bias trades quality for diversity loss."
39	  key_results: "Fully synthetic: both precision & recall → 0; With bias (λ<1): precision maintained but recall drops faster; Augmentation with fixed real data only delays MAD; Fresh data prevents MAD if sufficient"
40	  limitations:
41	    - "Primarily image domain (MNIST, FFHQ)"
42	    - "Hardware not specified"
43	    - "No text/LLM experiments"
44	  relation_to_us: "foundation"
45	
46	narrative:
47	  story_type: "突破局限型"
48	  hook: "Biological analogy — mad cow disease from feeding cattle with cattle remains. What happens when AI models consume their own outputs?"
49	  tension: "Synthetic data is proliferating (LAION-5B already contains synthetic images). The temptation to use it is strong (cheaper, privacy-preserving), but consequences are unknown."
50	  key_insight: "Section 3 — Gaussian theory shows covariance is a supermartingale (Σ_t → 0 a.s.), mean is a martingale (random walk). This dual failure mode (diversity collapse + quality drift) holds across all tested architectures."
51	  argument_chain: "synthetic data proliferation → autophagous loop formalization → 3 loop variants → Gaussian theory (martingale/supermartingale) → empirical validation (DDPM, StyleGAN, WGAN, NF) → sampling bias tradeoff → fresh data as remedy → phase transition in fresh data regime"
52	  contribution_framing: "3 contributions: (1) realistic autophagous loop models, (2) sampling bias role, (3) generality across architectures"
53	  intro_structure: "2 subsections: S1.1=context (synthetic data explosion), S1.2=contributions with detailed loop descriptions"
54	  notable_technique: "The 'MAD cow disease' biological analogy is memorable and widely cited. The precision-recall decomposition of FID makes the quality-diversity tradeoff concrete and measurable."
55	
56	figures:
57	  figure_count: 31
58	  figure1:
59	    type: "teaser_result"
60	    description: "StyleGAN-2 generated faces across generations showing progressive cross-hatching artifact amplification"
61	    narrative_role: "Visceral proof of model collapse — faces become visibly degraded"
62	    design_elements: ["grid of generated faces", "generation labels", "artifact progression visible"]
63	    visual_style: "Grid layout, faces across generations, degradation visually striking"
64	  result_figures:
65	    - figure_id: "Figure 4"
66	      viz_type: "line_plot"
67	      what_compared: "FID, precision, recall across generations for fully synthetic loop (FFHQ + MNIST)"
68	      how_gain_highlighted: "All three metrics monotonically degrade"
69	      design_note: "Triple-panel (FID/precision/recall) shows both quality and diversity decline simultaneously"
70	    - figure_id: "Figure 6"
71	      viz_type: "line_plot"
72	      what_compared: "Same metrics with sampling bias — precision maintained, recall drops faster"
73	      how_gain_highlighted: "Explicit quality-diversity tradeoff visualization"
74	      design_note: "Solid vs dashed lines for different models; direct comparison to unbiased case"
75	    - figure_id: "Figure 10"
76	      viz_type: "line_plot"
77	      what_compared: "Fresh data loop — WD/FID converges to steady state independent of initial data size"
78	      how_gain_highlighted: "Plateau behavior = no collapse"
79	      design_note: "Shows asymptotic independence from n_ini — a key theoretical prediction confirmed empirically"
80	  ablation_figures:
81	    - figure_id: "Figure 5"
82	      viz_type: "scatter"
83	      dimensions_varied: ["generation number"]
84	      design_note: "t-SNE of MNIST digits across generations — modes merge/drift, visually compelling"
85	    - figure_id: "Figure 9"
86	      viz_type: "line_plot"
87	      dimensions_varied: ["sampling bias λ values"]
88	      design_note: "Multiple λ curves on same plot; λ=0.8 shown as best compromise"
89	    - figure_id: "Figure 11"
90	      viz_type: "heatmap"
91	      dimensions_varied: ["n_r (real samples)", "n_s (synthetic samples)"]
92	      design_note: "Phase transition boundary (admissible vs inadmissible) — blue shaded region shows where synthetic data helps"
93	  figure_narrative_role: "Fig1(visceral teaser) → Fig3(loop taxonomy) → Fig4-5(fully synthetic collapse) → Fig6-7(bias tradeoff) → Fig8-9(augmentation delays) → Fig10-12(fresh data remedy + phase transition)"
94	
95	tables:
96	  table_count: 0
97	  main_result_table: "N/A — all results presented as figures (line plots, t-SNE, heatmaps)"
98	  ablation_tables: []
99	  supplementary_tables:
100	    in_appendix: true
101	    content: "Additional model samples (Figs 18-29), extended metric plots, WGAN/NF/GMM results"
102	    reason: "Visual-heavy paper; all quantitative comparisons via plots; appendix contains exhaustive sample galleries"
103	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78554d93-4969-45e9-a3a6-6be2e978cffc",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "1dde06c0-bc58-49ef-b5ec-9248aea39ecd",
  "sourceToolAssistantUUID": "78554d93-4969-45e9-a3a6-6be2e978cffc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T13:24:24.878Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RSbw5uTrKTabU3UgYYPW4m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/kazdan2025collapse.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dde06c0-bc58-49ef-b5ec-9248aea39ecd",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c1500e0-9091-49c1-adc4-e22107e041ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
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

### Tool result

_source line 40 · 2026-05-22T13:24:24.887Z_

<details><summary>↩ Tool result · `toolu_01RSbw5uTrKTabU3UgYYPW4m`</summary>

```text
1	paper_key: "kazdan2025collapse"
2	title: "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"
3	venue: "ICML 2025"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Replace scenario (delete + retrain)"
9	    - "Accumulate scenario (keep all data)"
10	    - "Accumulate-Subsample (fixed compute budget)"
11	  metrics:
12	    - {name: "Test loss (NLL on real data)", direction: "lower_better"}
13	    - {name: "Covariance/mean drift (Gaussian)", direction: "lower_better"}
14	    - {name: "R² (cardinality vs proportion)", direction: "higher_better"}
15	  datasets:
16	    - {name: "HelpSteer2 (Nvidia)", size: "~12.5K", task: "LM SFT"}
17	    - {name: "TinyStories", size: "N/A", task: "LM pretraining"}
18	    - {name: "sklearn synthetic (Blobs, Circles, Moons, Swiss Roll)", size: "N/A", task: "KDE"}
19	  ablation_dimensions:
20	    - data_scenario (replace, accumulate, accumulate-subsample)
21	    - model_type (Gaussian, KDE, LM-SFT, LM-pretrain, linear regression)
22	    - real_data_cardinality_vs_proportion
23	    - synthetic_data_amount
24	  training_recipe:
25	    LM_SFT: "Gemma2 2B, greedy decoding, ~55K completions (<512 tokens)"
26	    LM_pretrain: "small GPT/Llama variants on TinyStories"
27	    Gaussian: "n=316 samples per iteration"
28	    KDE: "Gaussian kernel"
29	  method_family: "data_accumulation_collapse_analysis"
30	
31	positioning:
32	  core_claim: "Replace-scenario collapses across all settings; accumulate-scenario avoids collapse; new accumulate-subsample (fixed compute) shows loss plateaus rather than diverges. Cardinality of real data matters more than proportion (R²=0.59 vs 0.34). Synthetic data helps only when real data is scarce."
33	  key_results: "R²=0.59 (cardinality) vs 0.34 (proportion); With ≤1024 real samples, optimal nonzero synthetic amount exists; With abundant real data, any synthetic data hurts"
34	  limitations:
35	    - "No data quality filtering applied"
36	    - "Limited to relatively small models/datasets"
37	    - "Need to understand conditions where synthetic data improves"
38	  relation_to_us: "competitor"
39	
40	narrative:
41	  story_type: "统一框架型"
42	  hook: "The internet contains increasingly more AI-generated content. What happens to future models pretrained on this polluted data?"
43	  tension: "Model collapse literature reaches contradictory conclusions — some say collapse is inevitable, others say it's avoidable. Different papers, different setups, different conclusions."
44	  key_insight: "Section 3-5 — The contradiction resolves by distinguishing replace vs accumulate scenarios. Both claims are correct in their respective regimes. New finding: even with compute budget constraints, accumulation plateaus rather than diverges."
45	  argument_chain: "contradictory claims in literature → unify by testing replace vs accumulate across 5 model types → confirm contrast holds universally → introduce fixed-compute middle ground → investigate real/synthetic data interaction → discover regime-dependent value of synthetic data"
46	  contribution_framing: "3 threads: (1) replace vs accumulate across 3 new settings, (2) fixed-compute middle ground, (3) cardinality vs proportion investigation"
47	  intro_structure: "Long intro with progressive claim refinement, citing specific prior work at each step"
48	  notable_technique: "The 'middle ground' scenario (accumulate-subsample) addresses the most realistic practical constraint (fixed compute budget) that prior work ignored. The R² comparison (cardinality vs proportion) is a clean, memorable quantitative insight."
49	
50	figures:
51	  figure_count: 5
52	  figure1:
53	    type: "teaser_result"
54	    description: "Multivariate Gaussian: replace collapses (covariance→0, mean drifts), accumulate stabilizes"
55	    narrative_role: "Immediate visual proof of the core replace-vs-accumulate contrast"
56	    design_elements: ["side-by-side comparison", "distribution evolution across iterations"]
57	    visual_style: "Dual-panel with iteration progression"
58	  result_figures:
59	    - figure_id: "Figure 2"
60	      viz_type: "line_plot"
61	      what_compared: "KDE NLL across iterations: replace (diverges) vs accumulate (stable) on 4 sklearn datasets"
62	      how_gain_highlighted: "Replace curves shoot up; accumulate curves flat"
63	      design_note: "4 datasets × 2 scenarios in compact multi-panel layout"
64	    - figure_id: "Figure 3"
65	      viz_type: "line_plot"
66	      what_compared: "LM SFT loss: replace vs accumulate on Gemma2/HelpSteer2"
67	      how_gain_highlighted: "Same pattern as Gaussian and KDE"
68	      design_note: "Consistency across model types reinforces the universal claim"
69	    - figure_id: "Figure 4"
70	      viz_type: "line_plot"
71	      what_compared: "Replace vs accumulate vs accumulate-subsample across 5 settings"
72	      how_gain_highlighted: "Accumulate-subsample plateaus between replace (diverges) and accumulate (stable)"
73	      design_note: "Three-curve comparison is the paper's signature visualization"
74	    - figure_id: "Figure 5"
75	      viz_type: "scatter"
76	      what_compared: "Test loss vs real/synthetic data amounts in LM SFT"
77	      how_gain_highlighted: "Shows regime where synthetic helps (scarce real) vs hurts (abundant real)"
78	      design_note: "2D scatter reveals the non-trivial interaction — not a simple monotonic relationship"
79	  ablation_figures: []
80	  figure_narrative_role: "Fig1(Gaussian proof of concept) → Fig2(KDE confirmation) → Fig3(LM confirmation) → Fig4(fixed-compute middle ground) → Fig5(data interaction)"
81	
82	tables:
83	  table_count: 0
84	  main_result_table: "N/A — all results via figures and R² statistics in text"
85	  ablation_tables: []
86	  supplementary_tables:
87	    in_appendix: true
88	    content: "Proofs (Theorem 1), additional model settings, extended results"
89	    reason: "Figure-driven paper; theoretical details in appendix"
90	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c1500e0-9091-49c1-adc4-e22107e041ba",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "44b434e5-3f4c-467f-8579-57fc7751ca26",
  "sourceToolAssistantUUID": "4c1500e0-9091-49c1-adc4-e22107e041ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T13:24:25.090Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KAwmJpWe7SppWQXbQoawXc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/he2025closer.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "44b434e5-3f4c-467f-8579-57fc7751ca26",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c4f4b897-ca3d-4530-b145-ba5e145f5bc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
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

### Tool result

_source line 42 · 2026-05-22T13:24:25.097Z_

<details><summary>↩ Tool result · `toolu_01KAwmJpWe7SppWQXbQoawXc`</summary>

```text
1	paper_key: "he2025closer"
2	title: "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"
3	venue: "NeurIPS 2025 Spotlight"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Vanilla DDPM (no selection)"
9	    - "CFG (classifier-free guidance)"
10	  metrics:
11	    - {name: "Generalization Score (GS)", direction: "higher_better"}
12	    - {name: "Entropy (KL estimator)", direction: "higher_better"}
13	    - {name: "FID", direction: "lower_better"}
14	  datasets:
15	    - {name: "CIFAR-10", size: "32768 images (32x32)"}
16	    - {name: "FFHQ", size: "8192 images (32x32)"}
17	    - {name: "MNIST", size: "12000 images"}
18	  ablation_dimensions:
19	    - dataset_size (1024-32768)
20	    - selection_method (greedy vs threshold_decay vs vanilla)
21	    - filter_ratio (0.2-1.0)
22	    - paradigm (replace vs accumulate-subsample)
23	    - CFG_scale
24	  training_recipe:
25	    optimizer: "Adam"
26	    lr: "1e-4"
27	    weight_decay: "1e-6"
28	    batch_size: 128
29	    precision: "FP16 mixed"
30	    denoising_steps: 1000
31	    epochs_per_iter: "500 (CIFAR-10), 1000 (FFHQ)"
32	    hardware: "single NVIDIA A100"
33	    model: "UNet-based DDPM (16M/19M params)"
34	  method_family: "entropy_based_data_selection"
35	
36	positioning:
37	  core_claim: "Model collapse in diffusion models manifests as a generalization-to-memorization transition driven by declining training data entropy (Pearson r=0.91). Entropy-based data selection (greedy/threshold decay) effectively mitigates this transition."
38	  key_results: "Accumulate-subsample iter8: vanilla FID 75.7 → greedy FID 44.7; entropy-GS correlation r=0.91; selection naturally favors real images (65% real vs 12.5% random chance at iter8)"
39	  limitations:
40	    - "No rigorous theory for WHY entropy collapses"
41	    - "Greedy selection is computationally expensive"
42	    - "Only image domain tested; no language/discrete diffusion"
43	  relation_to_us: "competitor"
44	
45	narrative:
46	  story_type: "突破局限型"
47	  hook: "AI-generated data flooding the internet creates self-consuming loops, but prior characterizations (variance shrinkage, distribution shift) miss practical manifestations."
48	  tension: "Variance collapse happens over 'extremely large' iterations — rarely a practical concern. Population risk is too holistic to characterize specific failure modes. What actually goes wrong in practice?"
49	  key_insight: "Section 3 — the model transitions from generating novel content to memorizing training data. This transition is driven by entropy collapse (not variance), with r=0.91 correlation. Entropy is both the diagnostic and the remedy (entropy-based selection)."
50	  argument_chain: "prior characterizations inadequate → identify gen-to-mem transition → find entropy as driver (r=0.91) → propose entropy-based selection → validate across datasets and paradigms"
51	  contribution_framing: "3 contributions: (1) identify gen-to-mem transition, (2) establish entropy-generalization correlation, (3) propose entropy-based selection methods"
52	  intro_structure: "3 paragraphs: P1=context (synthetic data proliferation + self-consuming loop), P2=prior work limitations (variance too slow, population risk too holistic), P3=our findings + contributions"
53	  notable_technique: "Using DINOv2 feature space for generalization score creates a perceptually meaningful metric. The 'entropy is both diagnostic and therapy' framing is elegant and actionable."
54	
55	figures:
56	  figure_count: 17
57	  figure1:
58	    type: "method_overview"
59	    description: "Self-consuming pipeline: replace paradigm (top), mitigated iteration with selection (middle), evolution of generated images (bottom right)"
60	    narrative_role: "Establishes the problem setup and previews the solution in one figure"
61	    design_elements: ["pipeline flow", "iteration progression", "image evolution samples"]
62	    visual_style: "Three-tier layout with arrows showing iterative process"
63	  result_figures:
64	    - figure_id: "Figure 2"
65	      viz_type: "qualitative_comparison"
66	      what_compared: "Generated images vs nearest training neighbors across iterations + quantitative GS curves"
67	      how_gain_highlighted: "Visual transition from novel→memorized is immediately apparent; GS drops near-exponentially"
68	      design_note: "Left panel (qualitative) + right panel (quantitative) creates powerful dual evidence"
69	    - figure_id: "Figure 4"
70	      viz_type: "scatter"
71	      what_compared: "Entropy vs GS (r=0.91) and trace-of-covariance vs GS"
72	      how_gain_highlighted: "Strong linear correlation for entropy vs weak for variance — directly challenges prior characterization"
73	      design_note: "Side-by-side scatter plots with r values make the comparison unarguable"
74	    - figure_id: "Figure 5"
75	      viz_type: "line_plot"
76	      what_compared: "GS across iterations with/without selection methods"
77	      how_gain_highlighted: "Selection methods maintain higher GS across all datasets"
78	      design_note: "Multi-panel (dataset per panel) shows generality"
79	    - figure_id: "Figure 6"
80	      viz_type: "line_plot"
81	      what_compared: "FID across iterations with/without selection"
82	      how_gain_highlighted: "Lower FID with selection"
83	      design_note: "Mirrors Figure 5 structure for consistency"
84	  ablation_figures:
85	    - figure_id: "Figure 8"
86	      viz_type: "bar_chart"
87	      dimensions_varied: ["proportion of real vs synthetic in selected subset"]
88	      design_note: "Shows selection naturally favors real images — emergent behavior, not engineered"
89	    - figure_id: "Figure 10-11"
90	      viz_type: "line_plot"
91	      dimensions_varied: ["filter_ratio", "decay_rate"]
92	      design_note: "Standard ablation over hyperparameters"
93	  figure_narrative_role: "Fig1(setup+preview) → Fig2(identify transition) → Fig3(entropy collapse) → Fig4(entropy vs variance) → Fig5-7(selection results) → Fig8(real data emergence) → Fig9(CFG) → Fig10-11(ablation)"
94	
95	tables:
96	  table_count: 0
97	  main_result_table: "N/A — all results via figures; key numbers (FID, GS, correlation) stated in text"
98	  ablation_tables:
99	    - table_id: "Inline table in Section 5"
100	      what_varied: ["filter_ratio (0.2-1.0)"]
101	      variation_style: "full_numbers"
102	      design_note: "Compact inline table for ablation, not a separate numbered table"
103	  supplementary_tables:
104	    in_appendix: true
105	    content: "Network structure, implementation details, additional generated images"
106	    reason: "Figure-driven paper; appendix for reproducibility and visual evidence"
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4f4b897-ca3d-4530-b145-ba5e145f5bc4",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "88fbc9ed-ee1d-45dc-b33f-037f31b71457",
  "sourceToolAssistantUUID": "c4f4b897-ca3d-4530-b145-ba5e145f5bc4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T13:24:25.537Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JCLNX7T7jMaKatn5mmSGoJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/dohmatob2024tale.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88fbc9ed-ee1d-45dc-b33f-037f31b71457",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b6fa341a-36b9-49f1-a73f-22b4e0b9615c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
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

### Tool result

_source line 44 · 2026-05-22T13:24:25.542Z_

<details><summary>↩ Tool result · `toolu_01JCLNX7T7jMaKatn5mmSGoJ`</summary>

```text
1	paper_key: "dohmatob2024tale"
2	title: "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
3	venue: "ICML 2024"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Hutter LLM (infinite memory)"
9	    - "Hutter++ (bigram extension)"
10	    - "Autoregressive bigram model"
11	    - "4-layer transformer (GCD task)"
12	    - "Llama2-7B (LoRA finetuned)"
13	  metrics:
14	    - {name: "Test error (TV distance)", direction: "lower_better"}
15	    - {name: "Test perplexity", direction: "lower_better"}
16	    - {name: "Number of correctly predicted GCDs", direction: "higher_better"}
17	    - {name: "Cross-entropy loss", direction: "lower_better"}
18	  datasets:
19	    - {name: "Synthetic Zipf distributions", size: "variable", task: "theory validation"}
20	    - {name: "GCD pairs (random integers)", size: "300M-1B samples", task: "arithmetic"}
21	    - {name: "Wikitext-103", size: "~2.2M chunks of 128 tokens", task: "LM finetuning"}
22	  ablation_dimensions:
23	    - zipf_exponent_beta (3/2, 7/5, 2)
24	    - tail_cutoff_k
25	    - generation_count (1-9)
26	    - mixing_ratio_pi (clean data fraction)
27	    - model_capacity_d (embedding dimension)
28	    - top_p_and_temperature
29	    - GCD_base (10, 420, 1000, 2017, 2023, 4913)
30	  training_recipe:
31	    Llama2: "LoRA, Adam, lr=5e-5, dropout=0.1, 0.062% trainable params"
32	    GCD_transformer: "4L, 512d, 8 heads, 17.2M params (encoder-only)"
33	    generation: "top_p=0.9, temperature=0.9"
34	    hardware: "NYU IT HPC"
35	  method_family: "scaling_law_theory_of_collapse"
36	
37	positioning:
38	  core_claim: "Model collapse is fundamentally a change of scaling laws caused by tail truncation/narrowing of data distributions. Establishes double scaling law E_test ≍ T^{-c} + k^{-c'}, where k captures tail degradation. Mixing even 2% real data induces grokking (delayed recovery)."
39	  key_results: "Double scaling law validated on Llama2-7B and GCD transformer; multi-generation collapse: E_test^(n) ≍ n·T^{-c}; grokking with 2% real data on Llama2; GCD models plateau on AI data while clean data models keep learning new skills"
40	  limitations:
41	    - "LLM experiments are finetuning only (compute constraints: 'weeks to run')"
42	    - "Grokking exact only in deterministic settings; probabilistic shows smoothed S-shape"
43	    - "Theory for simplified (Hutter/bigram) models; actual LLMs more complex"
44	  relation_to_us: "foundation"
45	
46	narrative:
47	  story_type: "统一框架型"
48	  hook: "The 'synthetic data age' — ChatGPT contributes 0.1% of daily global word production. How will scaling laws change when synthetic data inevitably contaminates training corpora?"
49	  tension: "Neural scaling laws underpin the 'scaling is all you need' paradigm. But these laws assume heavy-tailed (Zipf) data. AI generation truncates/narrows tails — what happens to scaling?"
50	  key_insight: "Section 2, Theorem 2.1 — AI-generated data cuts/narrows distribution tails (Figure 2 empirically, via top-p and temperature). This yields a double scaling law with an irreducible plateau. The framework unifies loss of scaling, skill loss, multi-generation collapse, and grokking under one mathematical umbrella."
51	  argument_chain: "scaling laws need heavy tails → AI generation truncates tails (top-p, temperature, finite sampling) → double scaling law (theory) → loss of skills → multi-generation amplification → mixing produces grokking → validated on Llama2 + GCD transformer"
52	  contribution_framing: "4 contributions: (1) double scaling law, (2) triplet scaling law (capacity-limited), (3) multi-generation universality, (4) mitigation via mixing + grokking"
53	  intro_structure: "Long intro with progressive research question development, citing Zipf's law, scaling laws, contamination evidence (LAION-5B), then contributions"
54	  notable_technique: "Connecting model collapse to scaling laws is the key conceptual innovation — makes the problem relevant to the broader ML community beyond just the synthetic data niche. The GCD 'skill emergence' experiment (Figure 4 right) is a brilliant visual: groups of new GCDs appear as 'bursts' that stop appearing with AI data."
55	
56	figures:
57	  figure_count: 35
58	  figure1:
59	    type: "motivation"
60	    description: "Three mechanisms of tail degradation (top-p, temperature, finite sample) → two consequences (loss of scaling law, loss of skills/GCDs)"
61	    narrative_role: "Conceptual framing figure linking cause (tail damage) to effect (scaling breakdown + skill loss)"
62	    design_elements: ["distribution tail diagrams", "scaling law curves", "GCD skill illustration"]
63	    visual_style: "Split layout: left=mechanisms, top-right=scaling, bottom-right=skill loss"
64	  result_figures:
65	    - figure_id: "Figure 3"
66	      viz_type: "line_plot"
67	      what_compared: "Three theoretical predictions: double scaling law, multi-generation collapse, grokking"
68	      how_gain_highlighted: "Theory curves (broken lines) match empirical points perfectly"
69	      design_note: "Three-panel 'signature figure' that previews all main results; theory-experiment overlay"
70	    - figure_id: "Figure 4"
71	      viz_type: "line_plot"
72	      what_compared: "Llama2 scaling across generations (left), GCD transformer scaling (middle), skill emergence (right)"
73	      how_gain_highlighted: "Clean data curves keep descending; AI data curves plateau; skills stop emerging"
74	      design_note: "Three diverse experiments in one figure — universality across model types and tasks"
75	    - figure_id: "Figure 7"
76	      viz_type: "line_plot"
77	      what_compared: "Llama2 mixing 98% AI + 2% real → grokking curve"
78	      how_gain_highlighted: "Grokking prediction from theory perfectly matches LLM experiment"
79	      design_note: "Theory-to-practice validation on real LLM — strongest evidence in the paper"
80	  ablation_figures:
81	    - figure_id: "Figure 2"
82	      viz_type: "bar_chart"
83	      dimensions_varied: ["top-p setting", "temperature", "generation type"]
84	      design_note: "Empirical measurement of tail degradation on Llama2 and GCD — grounds the theoretical assumptions"
85	    - figure_id: "Figure 6"
86	      viz_type: "line_plot"
87	      dimensions_varied: ["generation count", "top-p value"]
88	      design_note: "Multi-generation Hutter++ with top-p showing how inference settings compound collapse"
89	  figure_narrative_role: "Fig1(mechanism cartoon) → Fig2(empirical tails) → Fig3(theory preview) → Fig4(main experiments) → Fig5-6(extended theory) → Fig7(grokking validation) → appendix(extensive confirmations)"
90	
91	tables:
92	  table_count: 4
93	  main_result_table:
94	    table_id: "Table 1"
95	    row_axis: "GCD bases"
96	    col_axis: "accuracy, number of correct GCDs"
97	    row_organization: "by_dataset"
98	    col_organization: "flat"
99	    highlight_strategy: "no highlighting — descriptive"
100	    statistical_reporting: "single model values"
101	    num_baselines: 0
102	    design_note: "Simple descriptive table showing initial model capabilities; sets up the 'skills to lose' baseline"
103	  ablation_tables:
104	    - table_id: "Table 2"
105	      what_varied: ["training samples (30M/60M/90M)", "clean vs AI data"]
106	      variation_style: "full_numbers"
107	      design_note: "Shows AI data matches clean at early stages but diverges later — timing of collapse"
108	    - table_id: "Table 3"
109	      what_varied: ["300M vs 1B samples", "clean vs AI"]
110	      variation_style: "full_numbers"
111	      design_note: "Scaling comparison: 1B clean data learns new GCDs, 1B AI data doesn't"
112	    - table_id: "Table 4"
113	      what_varied: ["mixture ratio of AI data", "GCD base"]
114	      variation_style: "full_numbers"
115	      design_note: "Grokking delay increases monotonically with AI fraction"
116	  supplementary_tables:
117	    in_appendix: true
118	    content: "Extended results across all experimental settings"
119	    reason: "35 figures + 4 tables in main = very dense paper; appendix has extensive confirmations"
120	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6fa341a-36b9-49f1-a73f-22b4e0b9615c",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "01eb8d11-b42f-489d-a1f7-730ff99c17d1",
  "sourceToolAssistantUUID": "b6fa341a-36b9-49f1-a73f-22b4e0b9615c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-22T13:24:25.746Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q2NrA1TA33ES7sMHJoSS43`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/dohmatob2025strong.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01eb8d11-b42f-489d-a1f7-730ff99c17d1",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f90ed50d-0583-4ee9-9cab-40f6146715ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
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

### Tool result

_source line 46 · 2026-05-22T13:24:25.751Z_

<details><summary>↩ Tool result · `toolu_01Q2NrA1TA33ES7sMHJoSS43`</summary>

```text
1	paper_key: "dohmatob2025strong"
2	title: "Strong Model Collapse"
3	venue: "ICLR 2025 Spotlight"
4	full_text_available: true
5	
6	research:
7	  baselines:
8	    - "Training on real data only (p2=0)"
9	    - "Weighted single-step mixing (Jain et al. 2024)"
10	    - "Iterative/dynamic mixing (Ferbach et al. 2024)"
11	  metrics:
12	    - {name: "Test error (MSE)", direction: "lower_better"}
13	    - {name: "Test loss (cross-entropy)", direction: "lower_better"}
14	    - {name: "Scaling law exponents (implicit)", direction: "higher_better"}
15	  datasets:
16	    - {name: "Gaussian synthetic data", size: "n=500, d=600"}
17	    - {name: "MNIST", size: "10K-50K", task: "regression"}
18	    - {name: "BabiStories", size: "2.2M train + 22K val", task: "LM pretraining"}
19	    - {name: "TinyStories test set", size: "N/A", task: "evaluation"}
20	  ablation_dimensions:
21	    - synthetic_proportion_p2 (0-1, 11 values)
22	    - model_size_hidden_dim (100-10000)
23	    - model_depth_layers (12, 18, 24)
24	    - data_quality_c2 (0, 0.1, 0.5, 1.0)
25	    - mixing_strategy (single-step vs iterative)
26	    - mixing_weight_alpha
27	  training_recipe:
28	    MNIST: "SGD, lr=0.1, batch=128, 400 epochs"
29	    GPT2: "d=768, 12/18/24 layers, 12 heads, context=512, lr=5e-3, dropout=0.05, weight_decay=0.1, warmup=2000"
30	    synthetic_gen: "GPT-2-small, temperature=1, top-p=1"
31	    hardware: "not specified"
32	  method_family: "strong_collapse_theory"
33	
34	positioning:
35	  core_claim: "Even 1% synthetic data causes irreversible model collapse (test error plateaus above baseline) — 'strong model collapse'. Larger models amplify collapse in underparameterized regime but can mitigate it past interpolation threshold (double descent in collapse)."
36	  key_results: "Etest ≃ B+V+ζ where ζ=p2²c² is irreducible collapse term; 1% synthetic data causes visible scaling law degradation in GPT-2; optimal mixing weight α*→0 as n→∞; iterative mixing underperforms real-only training"
37	  limitations:
38	    - "Theory assumes Gaussian features, linear labels, ridge regression"
39	    - "Random projections as neural network proxy"
40	    - "No practical mitigation beyond discarding synthetic data"
41	  relation_to_us: "foundation"
42	
43	narrative:
44	  story_type: "突破局限型"
45	  hook: "Within the scaling laws paradigm that underpins ChatGPT and Llama training — can even small amounts of synthetic data cause collapse?"
46	  tension: "Prior work showed collapse with fully synthetic data. The natural hope is that mixing real + synthetic data can fix it. This paper kills that hope."
47	  key_insight: "Section 3, Theorem 1 — bias-variance decomposition Etest ≃ B+V+ζ reveals an extra term ζ=p2²c² from synthetic data that does NOT vanish as n→∞. Even p2=0.01 means ζ≈0.0001·c², creating an irreducible floor. This is 'strong' model collapse."
48	  argument_chain: "scaling laws paradigm → mix real+synthetic data → new bias-variance decomposition with extra ζ term → ζ doesn't vanish (strong collapse) → model size effect (double descent) → existing mixing strategies fail → validated on MNIST + GPT-2/BabiStories"
49	  contribution_framing: "2 results framed as research questions: Q1 (is collapse inevitable with mixing?) → yes (strong collapse), Q2 (do larger models help?) → double descent"
50	  intro_structure: "2 paragraphs: P1=model collapse context (with extensive citations), P2=scaling concerns for ChatGPT/Llama; then S1.1=contributions"
51	  notable_technique: "The Pareto diagram (Figure 1) is a novel visualization: real-only error on x-axis, mixed-data error on y-axis, model size as color. Points above diagonal = collapse. Creates immediate intuition about when and how much collapse occurs."
52	
53	figures:
54	  figure_count: 10
55	  figure1:
56	    type: "teaser_result"
57	    description: "Pareto diagram comparing test error with real-only vs mixed data, with model size encoded as color, across synthetic data quality levels"
58	    narrative_role: "Immediate visual proof that mixed data always hurts (points above diagonal), with model size interaction"
59	    design_elements: ["scatter plot", "diagonal reference line", "colorbar for model size", "quality level panels"]
60	    visual_style: "3-panel scatter with color gradient, Pareto frontiers annotated"
61	  result_figures:
62	    - figure_id: "Figure 2"
63	      viz_type: "line_plot"
64	      what_compared: "Bias B, Variance V, Extra term ζ, and total Etest as function of model width"
65	      how_gain_highlighted: "ζ term clearly shows as irreducible floor above clean-data curve; double descent visible"
66	      design_note: "4-panel decomposition makes the mechanism transparent — readers can see exactly which component causes collapse"
67	    - figure_id: "Figure 3"
68	      viz_type: "line_plot"
69	      what_compared: "Scaling laws under different synthetic proportions p2 (theory vs experiment)"
70	      how_gain_highlighted: "Theory curves (broken) perfectly overlay experiment (solid); increasing p2 bends scaling curve"
71	      design_note: "Theory-experiment agreement is pixel-perfect — strongest validation"
72	    - figure_id: "Figure 8"
73	      viz_type: "line_plot"
74	      what_compared: "GPT-2 test loss vs tokens under varying p2 (left) and model size with p2=1 (right)"
75	      how_gain_highlighted: "Even p2=0.001 visibly bends the scaling curve; larger models cross over at ~10^10 tokens"
76	      design_note: "The GPT-2 experiment is the clincher — theory predictions hold for real LLMs"
77	  ablation_figures:
78	    - figure_id: "Figure 4"
79	      viz_type: "line_plot"
80	      dimensions_varied: ["model width m", "data quality c²", "synthetic proportion p2"]
81	      design_note: "4 panels × multiple p2 curves — exhaustive exploration of the parameter space"
82	    - figure_id: "Figure 6"
83	      viz_type: "line_plot"
84	      dimensions_varied: ["model hidden dim (100-10000)", "sample count"]
85	      design_note: "MNIST fully-trained network confirms theory predictions from random projections proxy"
86	    - figure_id: "Figure 7"
87	      viz_type: "line_plot"
88	      dimensions_varied: ["synthetic proportion p2 (0-0.9)", "sample count"]
89	      design_note: "Random feature model (left) vs fully-trained (right) — both show same pattern"
90	  figure_narrative_role: "Fig1(Pareto overview) → Fig2(B-V-ζ decomposition) → Fig3-5(theory validation on toy) → Fig6-7(MNIST) → Fig8(GPT-2) → Fig9-10(mixing strategy failure)"
91	
92	tables:
93	  table_count: 0
94	  main_result_table: "N/A — all results via figures; scaling law exponents and Pareto frontiers visualized"
95	  ablation_tables: []
96	  supplementary_tables:
97	    in_appendix: true
98	    content: "Proofs, additional experiments, training details"
99	    reason: "Theory-heavy paper; all visual evidence in main text, proofs in appendix"
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f90ed50d-0583-4ee9-9cab-40f6146715ce",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "213a8632-3035-4dc8-9c10-752744d96ad5",
  "sourceToolAssistantUUID": "f90ed50d-0583-4ee9-9cab-40f6146715ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-22T13:24:26.168Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Eg5VLGg7WgmspnweuTURP2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/dces2026counter.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "213a8632-3035-4dc8-9c10-752744d96ad5",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "58dc78e4-9d28-4fbd-ab05-a71883149bc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
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

### Tool result

_source line 48 · 2026-05-22T13:24:26.179Z_

<details><summary>↩ Tool result · `toolu_01Eg5VLGg7WgmspnweuTURP2`</summary>

```text
1	paper_key: "dces2026counter"
2	title: "Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling"
3	venue: "MDPI Electronics 2026"
4	full_text_available: false
5	
6	research:
7	  baselines: ["naive random sampling", "PPL filtering", "SemDeDup"]
8	  metrics:
9	    - {name: "Perplexity (PPL)", direction: "lower_better"}
10	    - {name: "training loss", direction: "lower_better"}
11	    - {name: "entropy", direction: "higher_better"}
12	  datasets:
13	    - {name: "WikiText-2", size: "N/A", task: "OOD evaluation"}
14	    - {name: "Alpaca", size: "N/A", task: "in-distribution"}
15	  ablation_dimensions:
16	    - sampling_strategy (random, PPL_filter, SemDeDup, DCES)
17	    - model_scale (GPT-2, OPT-125M, Qwen, OPT-6.7B)
18	    - iteration_count (10 rounds)
19	  training_recipe: {models: "GPT-2, OPT-125M, Qwen, OPT-6.7B"}
20	  method_family: "dynamic_data_selection_for_collapse"
21	
22	positioning:
23	  core_claim: "DCES (Dynamic Center-Edge Sampling) constructs automated bias-correction via dynamic inter/intra-cluster sampling, reducing PPL degradation from 33.14→29.70 (vs naive) on OPT-125M after 10 self-training rounds."
24	  key_results: "OPT-125M WikiText-2 PPL: naive 23.56→33.14; DCES →29.70; SemDeDup →30.50"
25	  limitations: ["abstract-only extraction"]
26	  relation_to_us: "complementary"
27	
28	narrative: "N/A"
29	figures: "N/A"
30	tables: "N/A"
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "58dc78e4-9d28-4fbd-ab05-a71883149bc2",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "70ebf23f-e5fd-4005-ae51-9aca06790e20",
  "sourceToolAssistantUUID": "58dc78e4-9d28-4fbd-ab05-a71883149bc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-22T13:24:26.594Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RWPuYKiLdnrzxphpjot7jf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/truong2025entropy.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70ebf23f-e5fd-4005-ae51-9aca06790e20",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "054cb595-a725-4670-adbc-53efab92cb26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
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

### Tool result

_source line 50 · 2026-05-22T13:24:26.610Z_

<details><summary>↩ Tool result · `toolu_01RWPuYKiLdnrzxphpjot7jf`</summary>

```text
1	paper_key: "truong2025entropy"
2	title: "Entropy Collapse: A Universal Failure Mode of Intelligent Systems"
3	venue: "arXiv 2025"
4	full_text_available: false
5	
6	research:
7	  baselines: ["second-order transition assumption (null hypothesis)"]
8	  metrics:
9	    - {name: "entropy order parameter m", direction: "context_dependent"}
10	    - {name: "hysteresis ΔH_hyst (nats)", direction: "lower_better"}
11	    - {name: "relaxation exponent ν", direction: "context_dependent"}
12	  datasets:
13	    - {name: "SmallGPT (2-layer autoregressive transformer)", size: "N=50 vocabulary, 92 conditions, 8 seeds"}
14	  ablation_dimensions:
15	    - feedback_amplification_alpha
16	    - novelty_regeneration_beta
17	    - feedback_curvature_class (Class1 convex vs Class2 linear)
18	  training_recipe: {model: "SmallGPT, 2-layer autoregressive, N=50 vocab"}
19	  method_family: "entropy_collapse_phase_transition_theory"
20	
21	positioning:
22	  core_claim: "Entropy collapse is a first-order (discontinuous) phase transition at α_c=1/(1-β), with hysteresis and no early warning signals. Unifies AI model collapse, economic sclerosis, and evolutionary bottlenecks."
23	  key_results: "ΔH_hyst=2.92 nats (neural) > 2.73 (theory); ν=1.14±0.13; two universality classes"
24	  limitations: ["abstract-only extraction"]
25	  relation_to_us: "foundation"
26	
27	narrative: "N/A"
28	figures: "N/A"
29	tables: "N/A"
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "054cb595-a725-4670-adbc-53efab92cb26",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "3c278d0f-51a7-41b4-8c50-2446f3c185ea",
  "sourceToolAssistantUUID": "054cb595-a725-4670-adbc-53efab92cb26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T13:24:26.827Z_

<details open><summary>🔧 Tool call — Read · `toolu_014RsFWSxWhHPvk5G3xMmmw3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/wang2026contaminated.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c278d0f-51a7-41b4-8c50-2446f3c185ea",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "12d80f85-87d8-4ee6-8852-32f5af1ebb4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
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

### Tool result

_source line 52 · 2026-05-22T13:24:26.836Z_

<details><summary>↩ Tool result · `toolu_014RsFWSxWhHPvk5G3xMmmw3`</summary>

```text
1	paper_key: "wang2026contaminated"
2	title: "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training"
3	venue: "arXiv 2026"
4	full_text_available: false
5	
6	research:
7	  baselines: ["prior Gaussian/discrete model assumptions"]
8	  metrics:
9	    - {name: "convergence rate", direction: "higher_better"}
10	  datasets: []
11	  ablation_dimensions:
12	    - real_data_fraction
13	    - sampling_bias
14	    - generative_model_type (universal approximator)
15	  training_recipe: {focus: "theoretical, general framework with minimal assumptions"}
16	  method_family: "contaminated_recursive_training_theory"
17	
18	positioning:
19	  core_claim: "First positive theoretical result on recursive training without distributional assumptions: convergence rate equals min(baseline model rate, real data fraction). Extends to sampling bias settings."
20	  key_results: "Convergence rate = min(baseline rate, real data fraction per iteration)"
21	  limitations: ["abstract-only extraction"]
22	  relation_to_us: "foundation"
23	
24	narrative: "N/A"
25	figures: "N/A"
26	tables: "N/A"
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12d80f85-87d8-4ee6-8852-32f5af1ebb4c",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "845b19c7-074d-4400-82c4-d5eec967bb7a",
  "sourceToolAssistantUUID": "12d80f85-87d8-4ee6-8852-32f5af1ebb4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-22T13:24:27.037Z_

<details open><summary>🔧 Tool call — Read · `toolu_017qBi3JdUiRpkBcKnPk4pd8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/du2026geometric.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "845b19c7-074d-4400-82c4-d5eec967bb7a",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7fd1fec5-64d9-409e-b7c8-0ce9c1887683",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
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

### Tool result

_source line 54 · 2026-05-22T13:24:27.045Z_

<details><summary>↩ Tool result · `toolu_017qBi3JdUiRpkBcKnPk4pd8`</summary>

```text
1	paper_key: "du2026geometric"
2	title: "Escaping Mode Collapse in LLM Generation via Geometric Regulation"
3	venue: "arXiv 2026 (ICML 2026 accepted)"
4	full_text_available: false
5	
6	research:
7	  baselines: ["standard decoding (no intervention)"]
8	  metrics:
9	    - {name: "entropy rate (nats/step)", direction: "context_dependent"}
10	    - {name: "mode collapse frequency", direction: "lower_better"}
11	    - {name: "generation quality", direction: "higher_better"}
12	  datasets: []
13	  ablation_dimensions:
14	    - intervention_method (RMR vs standard)
15	    - entropy_rate_threshold
16	  training_recipe: {method: "RMR (low-rank damping of value cache)"}
17	  method_family: "geometric_regulation_for_mode_collapse"
18	
19	positioning:
20	  core_claim: "Mode collapse is geometric collapse (internal trajectory confined to low-dimensional subspace). RMR (Reinforced Mode Regulation) damps self-reinforcing directions in transformer value cache, enabling stable generation at 0.8 nats/step (vs 2.0 nats/step collapse threshold for standard)."
21	  key_results: "Stable generation at 0.8 nats/step; standard decoding collapses near 2.0 nats/step"
22	  limitations: ["abstract-only extraction"]
23	  relation_to_us: "complementary"
24	
25	narrative: "N/A"
26	figures: "N/A"
27	tables: "N/A"
28	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7fd1fec5-64d9-409e-b7c8-0ce9c1887683",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "54f31e15-e73f-40c5-87e9-5c2c4b76a2dd",
  "sourceToolAssistantUUID": "7fd1fec5-64d9-409e-b7c8-0ce9c1887683",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-22T13:24:27.408Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KpVAU9rhuzJeqKH6DfuXVA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/distill_tmp/gauthier2026alignment.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54f31e15-e73f-40c5-87e9-5c2c4b76a2dd",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgSnUzn549AwWDcL72i",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "206f8c3c-63ac-4248-8415-cf6811e93de1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Spim9wB85AfoQe7JkSNtmF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 14981,
      "output_tokens": 1038,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11135
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1038,
          "cache_read_input_tokens": 14981,
          "cache_creation_input_tokens": 11135,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11135,
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

_source line 56 · 2026-05-22T13:24:27.413Z_

<details><summary>↩ Tool result · `toolu_01KpVAU9rhuzJeqKH6DfuXVA`</summary>

```text
1	paper_key: "gauthier2026alignment"
2	title: "Explaining and Preventing Alignment Collapse in Iterative RLHF"
3	venue: "arXiv 2026"
4	full_text_available: false
5	
6	research:
7	  baselines: ["standard iterative RLHF (PPO-style)"]
8	  metrics:
9	    - {name: "alignment quality", direction: "higher_better"}
10	    - {name: "reward hacking frequency", direction: "lower_better"}
11	  datasets:
12	    - {name: "controlled environments", size: "N/A"}
13	    - {name: "LLM alignment pipeline", size: "N/A", model: "Llama-3.2-1B"}
14	  ablation_dimensions:
15	    - optimization_method (standard RLHF vs FPO)
16	    - steering_term (included vs dropped)
17	  training_recipe: {models: "Llama-3.2-1B", method: "FPO (foresighted policy optimization)"}
18	  method_family: "alignment_collapse_prevention"
19	
20	positioning:
21	  core_claim: "Standard iterative RLHF drops a 'parameter-steering term' from the Stackelberg game gradient, causing alignment collapse (policy exploits RM blind spots). FPO restores this term via regularization."
22	  key_results: "FPO prevents alignment collapse on Llama-3.2-1B"
23	  limitations: ["abstract-only extraction"]
24	  relation_to_us: "complementary"
25	
26	narrative: "N/A"
27	figures: "N/A"
28	tables: "N/A"
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "206f8c3c-63ac-4248-8415-cf6811e93de1",
  "isSidechain": true,
  "promptId": "41d7afba-8adb-4b45-9898-64fabd6a8b92",
  "agentId": "af2fbae3ae7b535a3",
  "type": "user",
  "uuid": "f44e2ded-940c-4df1-b3ce-032b922c6c4b",
  "sourceToolAssistantUUID": "206f8c3c-63ac-4248-8415-cf6811e93de1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-22T13:27:40.576Z_

Perfect! I have now read all 25 YAML files. Here they are in full, listed one by one:

---

## guo2024linguistic.yaml

```yaml
paper_key: "guo2024linguistic"
title: "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text"
venue: "NAACL 2024 Findings"
full_text_available: true

research:
  baselines: []  # intrinsic study - each iteration compared to human data (Gen 0)
  metrics:
    - {name: "Type-Token Ratio (TTR)", direction: "higher_better"}
    - {name: "Distinct-n (n=2,3)", direction: "higher_better"}
    - {name: "1-Self-BLEU", direction: "higher_better"}
    - {name: "Semantic diversity (cosine distance)", direction: "higher_better"}
    - {name: "Syntactic diversity (WL kernel distance)", direction: "higher_better"}
    - {name: "Perplexity", direction: "lower_better"}
  datasets:
    - {name: "XL-SUM", size: "306K", task: "news summarization"}
    - {name: "ACL Anthology", size: "40.5K", task: "scientific abstract generation"}
    - {name: "WritingPrompts", size: "272.6K", task: "story generation"}
  ablation_dimensions:
    - task_entropy_level (low/medium/high creativity)
    - mitigation_strategy (filtering vs mixing human data)
    - diversity_dimension (lexical vs semantic vs syntactic)
    - iteration_number (1-6)
  training_recipe:
    optimizer: "AdamW"
    epochs_per_iteration: 5
    hardware: "2x NVIDIA RTX A6000"
    base_model: "OPT-350M"
    iterations: 6
  method_family: "recursive_finetuning_analysis"

positioning:
  core_claim: "Syntactic diversity suffers most severely under recursive synthetic training, more than lexical or semantic diversity — first work to measure and demonstrate this with novel WL-kernel syntactic diversity metrics."
  key_results: "Story gen TTR: 0.84%→0.61% (↓73% from human 2.23%); Syntactic diversity: 4.23→1.96 (↓60%); Semantic diversity most stable; Quality filtering amplifies diversity loss"
  limitations:
    - "English-only; metrics may not generalize to other languages"
    - "Only OPT-350M tested; larger scales not explored (700 GPU-hrs for story gen alone)"
    - "Cannot simulate realistic web-scale contamination setting"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Data scarcity crisis — world's entire high-quality text is ~17T tokens, major models already consuming 2T. Practitioners turning to synthetic data."
  tension: "Prior work showed model collapse (tail vanishing), but nobody measured HOW diversity declines across linguistic dimensions."
  key_insight: "Section 4 — syntactic diversity declines far more severely than lexical or semantic. Form degrades faster than content. Revealed via novel WL-kernel metric on dependency trees."
  argument_chain: "data scarcity → synthetic training necessity → recursive training simulation → comprehensive diversity metrics (lexical/semantic/syntactic) → syntactic decline most severe → mitigation strategies fail"
  contribution_framing: "3 contributions: (1) first comprehensive metrics across 3 diversity dimensions, (2) empirical evaluation across 3 NLG tasks with varying creativity, (3) mitigation analysis"
  intro_structure: "4 paragraphs: P1=data scarcity motivation, P2=prior work on model collapse, P3=research questions, P4=contributions"
  notable_technique: "Stratifying tasks by 'creativity demand' (low/medium/high entropy) creates natural gradient showing diversity loss scales with task freedom"

figures:
  figure_count: 5
  figure1:
    type: "method_overview"
    description: "Recursive training cycle diagram: Data(0)→Model(1)→Data(1)→Model(2)→..."
    narrative_role: "Establishes the iterative contamination process being studied"
    design_elements: ["cycle arrows", "numbered iterations", "data/model alternation"]
    visual_style: "Simple flowchart with numbered nodes"
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "line_plot"
      what_compared: "Distinct-3 and syntactic diversity across iterations under mitigation strategies"
      how_gain_highlighted: "Shows mitigation strategies barely move curves vs no-intervention baseline"
      design_note: "Dual y-axis for different metrics; mitigation failure is visually obvious"
    - figure_id: "Figure 3"
      viz_type: "bar_chart"
      what_compared: "Word frequency histograms across iterations"
      how_gain_highlighted: "Low-frequency word bins shrink visibly across iterations"
      design_note: "Histogram overlay makes tail disappearance concrete and intuitive"
  ablation_figures:
    - figure_id: "Figure 4"
      viz_type: "scatter"
      dimensions_varied: ["iteration number"]
      design_note: "t-SNE of syntactic embeddings showing spatial compaction — visually compelling proof of diversity collapse"
    - figure_id: "Figure 5"
      viz_type: "scatter"
      dimensions_varied: ["iteration number"]
      design_note: "t-SNE of semantic embeddings — less compaction, supporting claim that semantic diversity is more robust"
  figure_narrative_role: "Fig1(process setup) → Fig3(word-level evidence) → Fig4(syntactic collapse visualization) → Fig5(semantic stability contrast) → Fig2(mitigation failure)"

tables:
  table_count: 2
  main_result_table:
    table_id: "Table 2"
    row_axis: "iterations (0-6)"
    col_axis: "metrics grouped by diversity dimension"
    row_organization: "by_iteration"
    col_organization: "grouped_by_metric_type"
    highlight_strategy: "arrows showing direction of change from human baseline"
    statistical_reporting: "single run values"
    num_baselines: 0  # intrinsic comparison to human data
    design_note: "Rows are iterations not methods; columns grouped by lexical/semantic/syntactic — readers see degradation trajectory per dimension"
  ablation_tables: []
  supplementary_tables:
    in_appendix: false
    content: "Table 1 shows example model outputs across iterations"
    reason: "Qualitative examples in main text to make abstract metrics concrete"
```

---

## chen2025scales.yaml

```yaml
paper_key: "chen2025scales"
title: "Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios"
venue: "arXiv 2025"
full_text_available: false

research:
  baselines: ["Pythia-410M", "Pythia-1B", "Pythia-2.8B", "Pythia-6.9B", "Pythia-12B", "STaR", "Self-Instruct"]
  metrics:
    - {name: "accuracy", direction: "higher_better"}
    - {name: "calibration", direction: "lower_better"}
  datasets:
    - {name: "five diverse tasks (unspecified)", size: "N/A"}
  ablation_dimensions:
    - model_scale (410M-12B)
    - synthetic_ratio (0-50%)
    - iteration_count (1-3)
    - task_type (reasoning vs retrieval)
  training_recipe: {model_family: "Pythia", scale_range: "410M-12B"}
  method_family: "empirical_scaling_analysis"

positioning:
  core_claim: "Models maintain stable performance up to 20% synthetic data; degradation accelerates beyond 30%; calibration degrades before accuracy (early warning); larger models more robust."
  key_results: "20% synthetic safe threshold; calibration as early warning; reasoning tasks degrade faster than retrieval"
  limitations: ["abstract-only extraction"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## gambetta2024surplexity.yaml

```yaml
paper_key: "gambetta2024surplexity"
title: "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI"
venue: "arXiv 2024"
full_text_available: false

research:
  baselines: ["human-data filtering"]
  metrics:
    - {name: "next-token probability distribution", direction: "N/A"}
    - {name: "distributional skewedness", direction: "lower_better"}
  datasets: []
  ablation_dimensions:
    - surplexity_threshold
    - data_filtering_strategy
  training_recipe: {}
  method_family: "data_filtering_for_collapse_mitigation"

positioning:
  core_claim: "Surprise-based data filtering (surplexity) preserves performance and diversity without needing to distinguish human vs AI data."
  key_results: "N/A"
  limitations: ["abstract-only extraction"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## sigma2026spectral.yaml

```yaml
paper_key: "sigma2026spectral"
title: "SIGMA: Scalable Spectral Insights for LLM Model Collapse"
venue: "arXiv 2026"
full_text_available: false

research:
  baselines: []
  metrics:
    - {name: "spectral bounds on embedding Gram matrices", direction: "N/A"}
    - {name: "representation space contraction", direction: "lower_better"}
  datasets: []
  ablation_dimensions:
    - model_scale
    - iteration_count
  training_recipe: {}
  method_family: "spectral_analysis_detection"

positioning:
  core_claim: "Spectral analysis of embedding Gram matrices can quantify and predict model collapse onset with deterministic and stochastic bounds."
  key_results: "Scalable collapse detection via spectral bounds"
  limitations: ["abstract-only extraction"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## shumailov2024curse.yaml

```yaml
paper_key: "shumailov2024curse"
title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
venue: "Nature 2024"
full_text_available: false

research:
  baselines: ["VAE", "Gaussian Mixture Models", "LLMs"]
  metrics:
    - {name: "distribution tail preservation", direction: "higher_better"}
    - {name: "model degradation", direction: "lower_better"}
  datasets: []
  ablation_dimensions:
    - model_type (VAE, GMM, LLM)
    - iteration_count
  training_recipe: {}
  method_family: "model_collapse_theory"

positioning:
  core_claim: "Training on model-generated data causes irreversible defects where tails of original distribution disappear — coined 'Model Collapse'."
  key_results: "Model collapse demonstrated across VAEs, GMMs, and LLMs"
  limitations: ["abstract-only extraction"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## li2016diversity.yaml

```yaml
paper_key: "li2016diversity"
title: "A Diversity-Promoting Objective Function for Neural Conversation Models"
venue: "NAACL 2016"
full_text_available: false

research:
  baselines: ["seq2seq with MLE"]
  metrics:
    - {name: "BLEU", direction: "higher_better"}
    - {name: "human evaluation", direction: "higher_better"}
  datasets:
    - {name: "two conversational datasets", size: "N/A"}
  ablation_dimensions:
    - objective_function (MLE vs MMI)
  training_recipe: {}
  method_family: "diversity_promoting_objective"

positioning:
  core_claim: "Maximum Mutual Information (MMI) objective produces more diverse and appropriate responses than standard MLE in dialogue."
  key_results: "MMI outperforms MLE on diversity and appropriateness"
  limitations: ["abstract-only extraction"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## noci2024mind.yaml

```yaml
paper_key: "noci2024mind"
title: "Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Transformers"
venue: "NeurIPS 2024"
full_text_available: true

research:
  baselines:
    - "Standard softmax attention (with spectral gap)"
    - "Identity attention matrix"
    - "Orthogonal value matrices"
  metrics:
    - {name: "Stable rank sr(M)", direction: "higher_better"}
    - {name: "Gradient norm", direction: "context_dependent"}
  datasets:
    - {name: "Synthetic Heaviside function", size: "synthetic"}
  ablation_dimensions:
    - depth (L=1,2,4,8)
    - width/context_length (T=10-1000)
    - initialization_scheme (default, Xavier, He)
    - architecture_variant (single-layer, +LayerNorm, +skip connections)
    - spectral_gap_removal (with/without)
  training_recipe:
    architecture: "single-head attention-only transformers"
    initialization: "N(0,1) for value matrices"
    task: "Heaviside function learning"
    hardware: "N/A (theoretical focus)"
  method_family: "spectral_analysis_signal_propagation"

positioning:
  core_claim: "Softmax attention creates a spectral gap (eigenvalue 1 vs O(T^{-1/2}) bulk) causing a NEW form of rank collapse in width (sequence length), distinct from known depth collapse. Removing this gap via A⊥ = A - T^{-1}·1 prevents width collapse."
  key_results: "Width collapse rate |sr-1|=O(T^{1-4L}); proposed fix makes rank scale linearly with T; gradient explosion bounded by T^{L-1}"
  limitations:
    - "Analysis primarily for single-layer; multi-layer key-query attention has unknown spectral properties"
    - "Multiple outlier eigenvalues emerge beyond first layer, reducing fix effectiveness"
    - "Dynamical isometry provably unachievable (Prop 7-8)"
    - "Training experiments inconclusive; no large-scale validation"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Transformers excel but face training instability — what goes wrong at initialization in softmax attention?"
  tension: "Prior work identified rank collapse in depth, but missed a fundamental width-dependent collapse caused by attention's spectral structure."
  key_insight: "Section 2, Theorem 2 — the spectral gap between eigenvalue 1 and the O(T^{-1/2}) bulk is the root cause. Removing it (A⊥) resolves width collapse and controls gradients."
  argument_chain: "training instability → spectral analysis of attention at init → identify spectral gap → prove width collapse + gradient explosion → propose A⊥ fix → theoretical guarantees → experiments verify (partially)"
  contribution_framing: "4 contributions: diagnose width collapse, identify spectral gap cause, propose fix with proofs, analyze modified model's kernel/Jacobian spectra"
  intro_structure: "3 sections: S1.1=background on signal propagation, S1.2=contributions, S1.3=organization"
  notable_technique: "Using free probability theory (free multiplicative convolution) to derive exact spectral distributions — mathematically rigorous yet yields clean design insight (subtract the rank-1 component)"

figures:
  figure_count: 8
  figure1:
    type: "problem_illustration"
    description: "Eigenvalue distribution of Random Markov matrix: circular bulk at O(T^{-1/2}) radius with isolated eigenvalue at 1"
    narrative_role: "Visually establishes the spectral gap — the core phenomenon the paper addresses"
    design_elements: ["eigenvalue scatter plot", "bulk vs outlier annotation", "scaling annotation"]
    visual_style: "Complex plane scatter with circle overlay showing bulk distribution"
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "line_plot"
      what_compared: "Stable rank vs context length (width collapse) and vs depth, with/without spectral gap removal"
      how_gain_highlighted: "Proposed fix maintains linear rank growth vs flat collapse"
      design_note: "Dual-panel (width vs depth); theoretical predictions overlaid on empirical curves"
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Gradient norm scaling with width at layer 1"
      how_gain_highlighted: "Linear trend confirmed across architectures"
      design_note: "Log-log scale reveals power-law relationships clearly"
    - figure_id: "Figure 5"
      viz_type: "line_plot"
      what_compared: "Gradient norm vs depth for Random Markov vs key-query attention"
      how_gain_highlighted: "Fix controls gradients for Random Markov but not fully for key-query"
      design_note: "Honest about limitations — key-query case shows fix is partial"
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      dimensions_varied: ["architecture variant (base, +LN, +skip)"]
      design_note: "Shows width collapse is universal across architectures — not an artifact of simplified setup"
    - figure_id: "Figure 8"
      viz_type: "line_plot"
      dimensions_varied: ["initialization scheme (Xavier, He, upscaled skip)"]
      design_note: "Reveals degenerate behavior under standard initialization choices — motivates rethinking defaults"
  figure_narrative_role: "Fig1(spectral gap visualization) → Fig2(collapse proof) → Fig3(universality across architectures) → Fig4-5(gradient analysis) → Fig6-7(training + eigenvalue evolution) → Fig8(initialization pitfalls)"

tables:
  table_count: 0
  main_result_table: "N/A — purely theoretical paper, all results presented as propositions + figures"
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Proof details and additional experimental configurations"
    reason: "Theoretical paper — proofs in appendix, key results as numbered propositions in main text"
```

---

## jing2022understanding.yaml

```yaml
paper_key: "jing2022understanding"
title: "Understanding Dimensional Collapse in Contrastive Self-supervised Learning"
venue: "ICLR 2022"
full_text_available: false

research:
  baselines: ["SimCLR (linear projector)"]
  metrics:
    - {name: "ImageNet classification accuracy", direction: "higher_better"}
  datasets:
    - {name: "ImageNet", size: "1.28M images"}
  ablation_dimensions:
    - projector_type
    - representation_dimensionality
  training_recipe: {}
  method_family: "dimensional_collapse_analysis"

positioning:
  core_claim: "Contrastive learning embeddings suffer dimensional collapse (spanning lower-dimensional subspace); DirectCLR directly optimizes representation space without trainable projector."
  key_results: "DirectCLR outperforms SimCLR with linear projector on ImageNet"
  limitations: ["abstract-only extraction"]
  relation_to_us: "orthogonal"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## dey2024breaking.yaml

```yaml
paper_key: "dey2024breaking"
title: "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"
venue: "ICML 2024"
full_text_available: false

research:
  baselines: ["data replacement loop", "data accumulation loop"]
  metrics:
    - {name: "cross-entropy validation loss", direction: "lower_better"}
    - {name: "test loss/MSE", direction: "lower_better"}
  datasets:
    - {name: "TinyStories", size: "470M tokens"}
    - {name: "GEOM-Drugs", size: "40k molecular conformations"}
    - {name: "CelebA", size: "200k face images"}
  ablation_dimensions:
    - data_regime (replacement vs accumulation)
    - model_family (GPT-2, Llama2, GeoDiff, VAE)
    - model_scale (12M/42M/125M)
  training_recipe: {models: "GPT-2, Llama2 (12M/42M/125M), GeoDiff, VAE"}
  method_family: "data_accumulation_for_collapse_prevention"

positioning:
  core_claim: "Model collapse is NOT inevitable — accumulating synthetic data alongside real data (instead of replacing) avoids collapse. Proven theoretically for linear models and empirically across LMs, diffusion models, and VAEs."
  key_results: "Accumulation regime: bounded test error; Replacement regime: collapse"
  limitations: ["abstract-only extraction"]
  relation_to_us: "competitor"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## fu2025selfconsuming.yaml

```yaml
paper_key: "fu2025selfconsuming"
title: "A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops"
venue: "ICLR 2025"
full_text_available: false

research:
  baselines: ["Self-consuming Training Loop (STL)"]
  metrics:
    - {name: "Total Variation distance", direction: "lower_better"}
    - {name: "KL divergence", direction: "lower_better"}
    - {name: "population/empirical risk", direction: "lower_better"}
  datasets: []
  ablation_dimensions:
    - real_synthetic_ratio
    - model_architecture
    - synthetic_data_sizing
  training_recipe: {focus: "theoretical, transformer ICL analysis"}
  method_family: "recursive_stability_theory"

positioning:
  core_claim: "Introduces 'recursive stability' concept; shows both model architecture and real/synthetic data proportion influence STL success. Even constant-sized real data proportion ensures transformer ICL convergence."
  key_results: "Convergence bound O(n^{-1}log^2(n) + n^{-1/2}log(n) + n^{-1/4}) for transformer ICL"
  limitations: ["abstract-only extraction"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## feng2025escaping.yaml

```yaml
paper_key: "feng2025escaping"
title: "Escaping Model Collapse via Synthetic Data Verification"
venue: "NeurIPS 2025"
full_text_available: false

research:
  baselines: ["unguided self-consuming loop"]
  metrics:
    - {name: "model collapse rate", direction: "lower_better"}
    - {name: "improvement/convergence bounds", direction: "N/A"}
  datasets:
    - {name: "MNIST", size: "60K", task: "VAE experiments"}
    - {name: "XSUM", size: "N/A", task: "LM fine-tuning"}
  ablation_dimensions:
    - verifier_reliability
    - training_iteration
  training_recipe: {models: "linear regression (theory), VAE, SmolLM2-135M"}
  method_family: "verifier_guided_retraining"

positioning:
  core_claim: "External verification (human/superior model) prevents collapse short-term, but unless verifier is perfectly reliable, gains plateau and converge toward verifier's 'knowledge center'."
  key_results: "Near-term improvement with verifier; long-term convergence to verifier limit"
  limitations: ["abstract-only extraction"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## barzilai2025consistency.yaml

```yaml
paper_key: "barzilai2025consistency"
title: "When Models Don't Collapse: On the Consistency of Iterative MLE"
venue: "ICML 2025"
full_text_available: false

research:
  baselines: ["iterative MLE with data accumulation"]
  metrics:
    - {name: "non-asymptotic error bounds", direction: "lower_better"}
    - {name: "collapse rate", direction: "lower_better"}
  datasets: []
  ablation_dimensions:
    - real_data_fraction_decay_rate
    - statistical_regularity_conditions
  training_recipe: {focus: "theoretical, MLE consistency analysis"}
  method_family: "iterative_MLE_theory"

positioning:
  core_claim: "Under standard MLE consistency assumptions, collapse can be avoided even as real data fraction vanishes. But without these assumptions, collapse can occur arbitrarily quickly even with real data present."
  key_results: "Non-asymptotic bounds on iterative MLE; first rigorous collapse-with-accumulation counterexamples"
  limitations: ["abstract-only extraction"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## gu2025datamixing.yaml

```yaml
paper_key: "gu2025datamixing"
title: "Data Mixing Can Induce Phase Transitions in Knowledge Acquisition"
venue: "ICLR 2025 Spotlight"
full_text_available: false

research:
  baselines: ["smooth scaling law assumption"]
  metrics:
    - {name: "biography memorization rate", direction: "higher_better"}
    - {name: "critical mixing ratio threshold", direction: "N/A"}
  datasets:
    - {name: "synthetic biography dataset", size: "N/A"}
    - {name: "web-scraped data", size: "N/A"}
  ablation_dimensions:
    - mixing_ratio
    - model_size
    - training_duration
  training_recipe: {focus: "controlled experiments on data mixing"}
  method_family: "phase_transition_analysis"

positioning:
  core_claim: "Knowledge acquisition from mixed data exhibits phase transitions (not smooth scaling) w.r.t. mixing ratio and model size. Modeled as knapsack capacity allocation with power-law phase transition."
  key_results: "Critical threshold in mixing ratio and model size for knowledge memorization; power-law relationship"
  limitations: ["abstract-only extraction"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## briesch2024selfconsuming.yaml

```yaml
paper_key: "briesch2024selfconsuming"
title: "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop"
venue: "arXiv 2024"
full_text_available: false

research:
  baselines: ["Full Synthetic cycle", "Balanced cycle", "Incremental cycle", "Expanding cycle"]
  metrics:
    - {name: "syntactic correctness", direction: "higher_better"}
    - {name: "semantic correctness", direction: "higher_better"}
    - {name: "Levenshtein diversity", direction: "higher_better"}
    - {name: "unique expression count", direction: "higher_better"}
  datasets:
    - {name: "Logic expression dataset", size: "10K unique Boolean expressions"}
  ablation_dimensions:
    - data_cycle_regime (full_synthetic, balanced, incremental, expanding)
    - synthetic_data_proportion
    - generation_count
  training_recipe: {model: "GPT-style transformer (6L, 6H, 384d, ~10.6M params)", training: "from scratch"}
  method_family: "self_consuming_loop_analysis"

positioning:
  core_claim: "LLM diversity collapse confirmed: correctness may improve initially but diversity declines depending on synthetic data proportion. Full synthetic loop collapses within <10 generations."
  key_results: "Full synthetic: collapse <10 gens; fresh human data slows but cannot halt decline"
  limitations: ["abstract-only extraction"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## ba2024fill.yaml

```yaml
paper_key: "ba2024fill"
title: "Fill In The Gaps: Model Calibration and Generalization with Synthetic Data"
venue: "EMNLP 2024"
full_text_available: true

research:
  baselines:
    - "BERTbase (standard)"
    - "Isotonic Regression"
    - "Platt Scaling"
    - "Monte Carlo Dropout"
    - "Temperature Scaling"
  metrics:
    - {name: "Accuracy (ACC)", direction: "higher_better"}
    - {name: "Expected Calibration Error (ECE)", direction: "lower_better"}
  datasets:
    - {name: "TC (Complaints)", size: "3449", task: "text classification"}
    - {name: "SUBJ (Subjectivity)", size: "10K", task: "text classification"}
    - {name: "B77 (Banking77)", size: "257", task: "text classification"}
    - {name: "SE (SentEval)", size: "3762", task: "text classification"}
    - {name: "Arxiv-10", size: "6K", task: "text classification (OOD)"}
    - {name: "Medical", size: "3722", task: "text classification (OOD)"}
  ablation_dimensions:
    - num_bins (10, 15, 20)
    - synthetic_strategy (Synthesis vs Synthesis+)
    - LLM_accuracy_vs_calibration_correlation
  training_recipe:
    optimizer: "Adam"
    lr: "1e-6"
    epochs: 5
    batch_size: 32
    dropout: 0.5
    hardware: "NVIDIA P100 GPUs"
    base_model: "BERTbase"
    synthetic_generator: "Llama-2-7b-chat-hf (T=0.1)"
  method_family: "synthetic_data_for_calibration"

positioning:
  core_claim: "LLM-generated synthetic data targeted at poorly-calibrated reliability diagram bins can simultaneously improve accuracy (up to 34%) and reduce ECE (up to 33%), with PAC-learning theoretical backing."
  key_results: "Avg up to 34% ACC increase, 33% ECE decrease; Synthesis+ (add synthetic) generally outperforms Synthesis (replace); LLM prediction accuracy matters more than LLM calibration for downstream improvement"
  limitations:
    - "Excessive synthetic data can cause overfitting"
    - "Only binary text classification tested"
    - "Single LLM (Llama-2-7b) used; no LLM comparison"
  relation_to_us: "orthogonal"

narrative:
  story_type: "化繁为简型"
  hook: "Model calibration is critical for trustworthy AI, but existing calibration methods hurt accuracy."
  tension: "Post-hoc calibration (Platt, isotonic, temperature scaling) adjusts probabilities but can degrade accuracy. No method addresses both simultaneously."
  key_insight: "Section 3.1 — PAC framework proves ECE bound can be reduced by adding synthetic data that fills gaps in reliability diagram. The insight is geometric: target specific miscalibrated confidence bins."
  argument_chain: "calibration-accuracy tradeoff → PAC-derived ECE bound → LLM-generated synthetic data fills reliability gaps → simultaneous improvement → validated on 6 NLP datasets"
  contribution_framing: "3 contributions: (1) ECE bound derivation via PAC, (2) gap-filling calibration strategy, (3) empirical validation of LLM synthetic data for calibration"
  intro_structure: "5 paragraphs: P1=NLP model success, P2=beyond accuracy (calibration importance), P3=modern NNs are miscalibrated, P4=synthetic data motivation, P5=approach + contributions"
  notable_technique: "Using reliability diagram 'gaps' as a visual + mathematical target for synthetic data generation — makes abstract calibration theory actionable"

figures:
  figure_count: 3
  figure1:
    type: "method_overview"
    description: "Framework: train model → identify miscalibrated bins in reliability diagram → generate synthetic data via LLM with target probabilities → retrain"
    narrative_role: "End-to-end pipeline visualization that makes the method immediately comprehensible"
    design_elements: ["pipeline flow", "reliability diagram inset", "LLM generation step"]
    visual_style: "Left-to-right flow with color-coded steps"
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "bar_chart"
      what_compared: "Reliability diagram before/after showing target bin identification and synthetic data placement"
      how_gain_highlighted: "Gap between confidence and accuracy visually shrinks"
      design_note: "Two-panel before/after comparison of reliability diagram — intuitive"
  ablation_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      dimensions_varied: ["iteration of calibration process on toy 1D example"]
      design_note: "Toy example makes abstract PAC theory concrete — shows logistic curve convergence"
  figure_narrative_role: "Fig1(method overview) → Fig2(bin targeting concept) → Fig3(toy validation)"

tables:
  table_count: 5
  main_result_table:
    table_id: "Table 4"
    row_axis: "methods"
    col_axis: "datasets × (ACC, ECE)"
    row_organization: "by_category"
    col_organization: "grouped_by_dataset"
    highlight_strategy: "highlighted values considering both ACC and ECE, weighing more on ECE"
    statistical_reporting: "mean (std) across runs"
    num_baselines: 5
    design_note: "Dual-metric per dataset; explicit note about weighting ECE more in highlighting — transparent evaluation criteria"
  ablation_tables:
    - table_id: "Table 5"
      what_varied: ["LLM_ACC vs LLM_ECE correlation with downstream improvement"]
      variation_style: "full_numbers"
      design_note: "Pearson correlation matrix reveals LLM accuracy matters more than LLM calibration — counter-intuitive finding"
  supplementary_tables:
    in_appendix: true
    content: "Table 6 (model params), Table 7 (system prompts for generation), Table 8 (generation examples)"
    reason: "Reproducibility details (prompts, hyperparams) in appendix; main text focuses on results"
```

---

## alemohammad2024mad.yaml

```yaml
paper_key: "alemohammad2024mad"
title: "Self-Consuming Generative Models Go MAD"
venue: "ICLR 2024"
full_text_available: true

research:
  baselines:
    - "DDPM (conditional, T=500)"
    - "StyleGAN-2 (unconditional)"
    - "WGAN-GP"
    - "Normalizing Flows (GLOW)"
    - "Gaussian/GMM (analytical)"
  metrics:
    - {name: "FID (Fréchet Inception Distance)", direction: "lower_better"}
    - {name: "Precision (k=5 NN)", direction: "higher_better"}
    - {name: "Recall (k=5 NN)", direction: "higher_better"}
    - {name: "Wasserstein distance", direction: "lower_better"}
    - {name: "Effective sample size (n_e)", direction: "higher_better"}
  datasets:
    - {name: "MNIST", size: "60K"}
    - {name: "FFHQ", size: "70K (downsampled to 128x128)"}
    - {name: "2D Rosenbrock distribution", size: "10K synthetic"}
    - {name: "25-mode 2D GMM", size: "synthetic"}
  ablation_dimensions:
    - loop_type (fully_synthetic, augmentation, fresh_data)
    - sampling_bias_lambda (0-1)
    - generation_count
    - model_architecture (DDPM, StyleGAN2, WGAN, NF, Gaussian)
    - fresh_data_amount (n_r)
  training_recipe:
    DDPM: "conditional, T=500 diffusion steps, 10% conditioning dropout for CFG"
    StyleGAN2: "unconditional, FFHQ 128x128"
    NF_GLOW: "8 coupling layers, hidden_dim=64, 20 epochs, batch=256"
    data_sizes: "DDPM: 60K/iter; StyleGAN: 70K/iter"
  method_family: "autophagous_loop_analysis"

positioning:
  core_claim: "Without enough fresh real data in each generation, self-consuming generative models inevitably suffer Model Autophagy Disorder (MAD) — either quality (precision) or diversity (recall) progressively decreases. Sampling bias trades quality for diversity loss."
  key_results: "Fully synthetic: both precision & recall → 0; With bias (λ<1): precision maintained but recall drops faster; Augmentation with fixed real data only delays MAD; Fresh data prevents MAD if sufficient"
  limitations:
    - "Primarily image domain (MNIST, FFHQ)"
    - "Hardware not specified"
    - "No text/LLM experiments"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Biological analogy — mad cow disease from feeding cattle with cattle remains. What happens when AI models consume their own outputs?"
  tension: "Synthetic data is proliferating (LAION-5B already contains synthetic images). The temptation to use it is strong (cheaper, privacy-preserving), but consequences are unknown."
  key_insight: "Section 3 — Gaussian theory shows covariance is a supermartingale (Σ_t → 0 a.s.), mean is a martingale (random walk). This dual failure mode (diversity collapse + quality drift) holds across all tested architectures."
  argument_chain: "synthetic data proliferation → autophagous loop formalization → 3 loop variants → Gaussian theory (martingale/supermartingale) → empirical validation (DDPM, StyleGAN, WGAN, NF) → sampling bias tradeoff → fresh data as remedy → phase transition in fresh data regime"
  contribution_framing: "3 contributions: (1) realistic autophagous loop models, (2) sampling bias role, (3) generality across architectures"
  intro_structure: "2 subsections: S1.1=context (synthetic data explosion), S1.2=contributions with detailed loop descriptions"
  notable_technique: "The 'MAD cow disease' biological analogy is memorable and widely cited. The precision-recall decomposition of FID makes the quality-diversity tradeoff concrete and measurable."

figures:
  figure_count: 31
  figure1:
    type: "teaser_result"
    description: "StyleGAN-2 generated faces across generations showing progressive cross-hatching artifact amplification"
    narrative_role: "Visceral proof of model collapse — faces become visibly degraded"
    design_elements: ["grid of generated faces", "generation labels", "artifact progression visible"]
    visual_style: "Grid layout, faces across generations, degradation visually striking"
  result_figures:
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "FID, precision, recall across generations for fully synthetic loop (FFHQ + MNIST)"
      how_gain_highlighted: "All three metrics monotonically degrade"
      design_note: "Triple-panel (FID/precision/recall) shows both quality and diversity decline simultaneously"
    - figure_id: "Figure 6"
      viz_type: "line_plot"
      what_compared: "Same metrics with sampling bias — precision maintained, recall drops faster"
      how_gain_highlighted: "Explicit quality-diversity tradeoff visualization"
      design_note: "Solid vs dashed lines for different models; direct comparison to unbiased case"
    - figure_id: "Figure 10"
      viz_type: "line_plot"
      what_compared: "Fresh data loop — WD/FID converges to steady state independent of initial data size"
      how_gain_highlighted: "Plateau behavior = no collapse"
      design_note: "Shows asymptotic independence from n_ini — a key theoretical prediction confirmed empirically"
  ablation_figures:
    - figure_id: "Figure 5"
      viz_type: "scatter"
      dimensions_varied: ["generation number"]
      design_note: "t-SNE of MNIST digits across generations — modes merge/drift, visually compelling"
    - figure_id: "Figure 9"
      viz_type: "line_plot"
      dimensions_varied: ["sampling bias λ values"]
      design_note: "Multiple λ curves on same plot; λ=0.8 shown as best compromise"
    - figure_id: "Figure 11"
      viz_type: "heatmap"
      dimensions_varied: ["n_r (real samples)", "n_s (synthetic samples)"]
      design_note: "Phase transition boundary (admissible vs inadmissible) — blue shaded region shows where synthetic data helps"
  figure_narrative_role: "Fig1(visceral teaser) → Fig3(loop taxonomy) → Fig4-5(fully synthetic collapse) → Fig6-7(bias tradeoff) → Fig8-9(augmentation delays) → Fig10-12(fresh data remedy + phase transition)"

tables:
  table_count: 0
  main_result_table: "N/A — all results presented as figures (line plots, t-SNE, heatmaps)"
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Additional model samples (Figs 18-29), extended metric plots, WGAN/NF/GMM results"
    reason: "Visual-heavy paper; all quantitative comparisons via plots; appendix contains exhaustive sample galleries"
```

---

## kazdan2025collapse.yaml

```yaml
paper_key: "kazdan2025collapse"
title: "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"
venue: "ICML 2025"
full_text_available: true

research:
  baselines:
    - "Replace scenario (delete + retrain)"
    - "Accumulate scenario (keep all data)"
    - "Accumulate-Subsample (fixed compute budget)"
  metrics:
    - {name: "Test loss (NLL on real data)", direction: "lower_better"}
    - {name: "Covariance/mean drift (Gaussian)", direction: "lower_better"}
    - {name: "R² (cardinality vs proportion)", direction: "higher_better"}
  datasets:
    - {name: "HelpSteer2 (Nvidia)", size: "~12.5K", task: "LM SFT"}
    - {name: "TinyStories", size: "N/A", task: "LM pretraining"}
    - {name: "sklearn synthetic (Blobs, Circles, Moons, Swiss Roll)", size: "N/A", task: "KDE"}
  ablation_dimensions:
    - data_scenario (replace, accumulate, accumulate-subsample)
    - model_type (Gaussian, KDE, LM-SFT, LM-pretrain, linear regression)
    - real_data_cardinality_vs_proportion
    - synthetic_data_amount
  training_recipe:
    LM_SFT: "Gemma2 2B, greedy decoding, ~55K completions (<512 tokens)"
    LM_pretrain: "small GPT/Llama variants on TinyStories"
    Gaussian: "n=316 samples per iteration"
    KDE: "Gaussian kernel"
  method_family: "data_accumulation_collapse_analysis"

positioning:
  core_claim: "Replace-scenario collapses across all settings; accumulate-scenario avoids collapse; new accumulate-subsample (fixed compute) shows loss plateaus rather than diverges. Cardinality of real data matters more than proportion (R²=0.59 vs 0.34). Synthetic data helps only when real data is scarce."
  key_results: "R²=0.59 (cardinality) vs 0.34 (proportion); With ≤1024 real samples, optimal nonzero synthetic amount exists; With abundant real data, any synthetic data hurts"
  limitations:
    - "No data quality filtering applied"
    - "Limited to relatively small models/datasets"
    - "Need to understand conditions where synthetic data improves"
  relation_to_us: "competitor"

narrative:
  story_type: "统一框架型"
  hook: "The internet contains increasingly more AI-generated content. What happens to future models pretrained on this polluted data?"
  tension: "Model collapse literature reaches contradictory conclusions — some say collapse is inevitable, others say it's avoidable. Different papers, different setups, different conclusions."
  key_insight: "Section 3-5 — The contradiction resolves by distinguishing replace vs accumulate scenarios. Both claims are correct in their respective regimes. New finding: even with compute budget constraints, accumulation plateaus rather than diverges."
  argument_chain: "contradictory claims in literature → unify by testing replace vs accumulate across 5 model types → confirm contrast holds universally → introduce fixed-compute middle ground → investigate real/synthetic data interaction → discover regime-dependent value of synthetic data"
  contribution_framing: "3 threads: (1) replace vs accumulate across 3 new settings, (2) fixed-compute middle ground, (3) cardinality vs proportion investigation"
  intro_structure: "Long intro with progressive claim refinement, citing specific prior work at each step"
  notable_technique: "The 'middle ground' scenario (accumulate-subsample) addresses the most realistic practical constraint (fixed compute budget) that prior work ignored. The R² comparison (cardinality vs proportion) is a clean, memorable quantitative insight."

figures:
  figure_count: 5
  figure1:
    type: "teaser_result"
    description: "Multivariate Gaussian: replace collapses (covariance→0, mean drifts), accumulate stabilizes"
    narrative_role: "Immediate visual proof of the core replace-vs-accumulate contrast"
    design_elements: ["side-by-side comparison", "distribution evolution across iterations"]
    visual_style: "Dual-panel with iteration progression"
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "line_plot"
      what_compared: "KDE NLL across iterations: replace (diverges) vs accumulate (stable) on 4 sklearn datasets"
      how_gain_highlighted: "Replace curves shoot up; accumulate curves flat"
      design_note: "4 datasets × 2 scenarios in compact multi-panel layout"
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "LM SFT loss: replace vs accumulate on Gemma2/HelpSteer2"
      how_gain_highlighted: "Same pattern as Gaussian and KDE"
      design_note: "Consistency across model types reinforces the universal claim"
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Replace vs accumulate vs accumulate-subsample across 5 settings"
      how_gain_highlighted: "Accumulate-subsample plateaus between replace (diverges) and accumulate (stable)"
      design_note: "Three-curve comparison is the paper's signature visualization"
    - figure_id: "Figure 5"
      viz_type: "scatter"
      what_compared: "Test loss vs real/synthetic data amounts in LM SFT"
      how_gain_highlighted: "Shows regime where synthetic helps (scarce real) vs hurts (abundant real)"
      design_note: "2D scatter reveals the non-trivial interaction — not a simple monotonic relationship"
  ablation_figures: []
  figure_narrative_role: "Fig1(Gaussian proof of concept) → Fig2(KDE confirmation) → Fig3(LM confirmation) → Fig4(fixed-compute middle ground) → Fig5(data interaction)"

tables:
  table_count: 0
  main_result_table: "N/A — all results via figures and R² statistics in text"
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Proofs (Theorem 1), additional model settings, extended results"
    reason: "Figure-driven paper; theoretical details in appendix"
```

---

## he2025closer.yaml

```yaml
paper_key: "he2025closer"
title: "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"
venue: "NeurIPS 2025 Spotlight"
full_text_available: true

research:
  baselines:
    - "Vanilla DDPM (no selection)"
    - "CFG (classifier-free guidance)"
  metrics:
    - {name: "Generalization Score (GS)", direction: "higher_better"}
    - {name: "Entropy (KL estimator)", direction: "higher_better"}
    - {name: "FID", direction: "lower_better"}
  datasets:
    - {name: "CIFAR-10", size: "32768 images (32x32)"}
    - {name: "FFHQ", size: "8192 images (32x32)"}
    - {name: "MNIST", size: "12000 images"}
  ablation_dimensions:
    - dataset_size (1024-32768)
    - selection_method (greedy vs threshold_decay vs vanilla)
    - filter_ratio (0.2-1.0)
    - paradigm (replace vs accumulate-subsample)
    - CFG_scale
  training_recipe:
    optimizer: "Adam"
    lr: "1e-4"
    weight_decay: "1e-6"
    batch_size: 128
    precision: "FP16 mixed"
    denoising_steps: 1000
    epochs_per_iter: "500 (CIFAR-10), 1000 (FFHQ)"
    hardware: "single NVIDIA A100"
    model: "UNet-based DDPM (16M/19M params)"
  method_family: "entropy_based_data_selection"

positioning:
  core_claim: "Model collapse in diffusion models manifests as a generalization-to-memorization transition driven by declining training data entropy (Pearson r=0.91). Entropy-based data selection (greedy/threshold decay) effectively mitigates this transition."
  key_results: "Accumulate-subsample iter8: vanilla FID 75.7 → greedy FID 44.7; entropy-GS correlation r=0.91; selection naturally favors real images (65% real vs 12.5% random chance at iter8)"
  limitations:
    - "No rigorous theory for WHY entropy collapses"
    - "Greedy selection is computationally expensive"
    - "Only image domain tested; no language/discrete diffusion"
  relation_to_us: "competitor"

narrative:
  story_type: "突破局限型"
  hook: "AI-generated data flooding the internet creates self-consuming loops, but prior characterizations (variance shrinkage, distribution shift) miss practical manifestations."
  tension: "Variance collapse happens over 'extremely large' iterations — rarely a practical concern. Population risk is too holistic to characterize specific failure modes. What actually goes wrong in practice?"
  key_insight: "Section 3 — the model transitions from generating novel content to memorizing training data. This transition is driven by entropy collapse (not variance), with r=0.91 correlation. Entropy is both the diagnostic and the remedy (entropy-based selection)."
  argument_chain: "prior characterizations inadequate → identify gen-to-mem transition → find entropy as driver (r=0.91) → propose entropy-based selection → validate across datasets and paradigms"
  contribution_framing: "3 contributions: (1) identify gen-to-mem transition, (2) establish entropy-generalization correlation, (3) propose entropy-based selection methods"
  intro_structure: "3 paragraphs: P1=context (synthetic data proliferation + self-consuming loop), P2=prior work limitations (variance too slow, population risk too holistic), P3=our findings + contributions"
  notable_technique: "Using DINOv2 feature space for generalization score creates a perceptually meaningful metric. The 'entropy is both diagnostic and therapy' framing is elegant and actionable."

figures:
  figure_count: 17
  figure1:
    type: "method_overview"
    description: "Self-consuming pipeline: replace paradigm (top), mitigated iteration with selection (middle), evolution of generated images (bottom right)"
    narrative_role: "Establishes the problem setup and previews the solution in one figure"
    design_elements: ["pipeline flow", "iteration progression", "image evolution samples"]
    visual_style: "Three-tier layout with arrows showing iterative process"
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "qualitative_comparison"
      what_compared: "Generated images vs nearest training neighbors across iterations + quantitative GS curves"
      how_gain_highlighted: "Visual transition from novel→memorized is immediately apparent; GS drops near-exponentially"
      design_note: "Left panel (qualitative) + right panel (quantitative) creates powerful dual evidence"
    - figure_id: "Figure 4"
      viz_type: "scatter"
      what_compared: "Entropy vs GS (r=0.91) and trace-of-covariance vs GS"
      how_gain_highlighted: "Strong linear correlation for entropy vs weak for variance — directly challenges prior characterization"
      design_note: "Side-by-side scatter plots with r values make the comparison unarguable"
    - figure_id: "Figure 5"
      viz_type: "line_plot"
      what_compared: "GS across iterations with/without selection methods"
      how_gain_highlighted: "Selection methods maintain higher GS across all datasets"
      design_note: "Multi-panel (dataset per panel) shows generality"
    - figure_id: "Figure 6"
      viz_type: "line_plot"
      what_compared: "FID across iterations with/without selection"
      how_gain_highlighted: "Lower FID with selection"
      design_note: "Mirrors Figure 5 structure for consistency"
  ablation_figures:
    - figure_id: "Figure 8"
      viz_type: "bar_chart"
      dimensions_varied: ["proportion of real vs synthetic in selected subset"]
      design_note: "Shows selection naturally favors real images — emergent behavior, not engineered"
    - figure_id: "Figure 10-11"
      viz_type: "line_plot"
      dimensions_varied: ["filter_ratio", "decay_rate"]
      design_note: "Standard ablation over hyperparameters"
  figure_narrative_role: "Fig1(setup+preview) → Fig2(identify transition) → Fig3(entropy collapse) → Fig4(entropy vs variance) → Fig5-7(selection results) → Fig8(real data emergence) → Fig9(CFG) → Fig10-11(ablation)"

tables:
  table_count: 0
  main_result_table: "N/A — all results via figures; key numbers (FID, GS, correlation) stated in text"
  ablation_tables:
    - table_id: "Inline table in Section 5"
      what_varied: ["filter_ratio (0.2-1.0)"]
      variation_style: "full_numbers"
      design_note: "Compact inline table for ablation, not a separate numbered table"
  supplementary_tables:
    in_appendix: true
    content: "Network structure, implementation details, additional generated images"
    reason: "Figure-driven paper; appendix for reproducibility and visual evidence"
```

---

## dohmatob2024tale.yaml

```yaml
paper_key: "dohmatob2024tale"
title: "A Tale of Tails: Model Collapse as a Change of Scaling Laws"
venue: "ICML 2024"
full_text_available: true

research:
  baselines:
    - "Hutter LLM (infinite memory)"
    - "Hutter++ (bigram extension)"
    - "Autoregressive bigram model"
    - "4-layer transformer (GCD task)"
    - "Llama2-7B (LoRA finetuned)"
  metrics:
    - {name: "Test error (TV distance)", direction: "lower_better"}
    - {name: "Test perplexity", direction: "lower_better"}
    - {name: "Number of correctly predicted GCDs", direction: "higher_better"}
    - {name: "Cross-entropy loss", direction: "lower_better"}
  datasets:
    - {name: "Synthetic Zipf distributions", size: "variable", task: "theory validation"}
    - {name: "GCD pairs (random integers)", size: "300M-1B samples", task: "arithmetic"}
    - {name: "Wikitext-103", size: "~2.2M chunks of 128 tokens", task: "LM finetuning"}
  ablation_dimensions:
    - zipf_exponent_beta (3/2, 7/5, 2)
    - tail_cutoff_k
    - generation_count (1-9)
    - mixing_ratio_pi (clean data fraction)
    - model_capacity_d (embedding dimension)
    - top_p_and_temperature
    - GCD_base (10, 420, 1000, 2017, 2023, 4913)
  training_recipe:
    Llama2: "LoRA, Adam, lr=5e-5, dropout=0.1, 0.062% trainable params"
    GCD_transformer: "4L, 512d, 8 heads, 17.2M params (encoder-only)"
    generation: "top_p=0.9, temperature=0.9"
    hardware: "NYU IT HPC"
  method_family: "scaling_law_theory_of_collapse"

positioning:
  core_claim: "Model collapse is fundamentally a change of scaling laws caused by tail truncation/narrowing of data distributions. Establishes double scaling law E_test ≍ T^{-c} + k^{-c'}, where k captures tail degradation. Mixing even 2% real data induces grokking (delayed recovery)."
  key_results: "Double scaling law validated on Llama2-7B and GCD transformer; multi-generation collapse: E_test^(n) ≍ n·T^{-c}; grokking with 2% real data on Llama2; GCD models plateau on AI data while clean data models keep learning new skills"
  limitations:
    - "LLM experiments are finetuning only (compute constraints: 'weeks to run')"
    - "Grokking exact only in deterministic settings; probabilistic shows smoothed S-shape"
    - "Theory for simplified (Hutter/bigram) models; actual LLMs more complex"
  relation_to_us: "foundation"

narrative:
  story_type: "统一框架型"
  hook: "The 'synthetic data age' — ChatGPT contributes 0.1% of daily global word production. How will scaling laws change when synthetic data inevitably contaminates training corpora?"
  tension: "Neural scaling laws underpin the 'scaling is all you need' paradigm. But these laws assume heavy-tailed (Zipf) data. AI generation truncates/narrows tails — what happens to scaling?"
  key_insight: "Section 2, Theorem 2.1 — AI-generated data cuts/narrows distribution tails (Figure 2 empirically, via top-p and temperature). This yields a double scaling law with an irreducible plateau. The framework unifies loss of scaling, skill loss, multi-generation collapse, and grokking under one mathematical umbrella."
  argument_chain: "scaling laws need heavy tails → AI generation truncates tails (top-p, temperature, finite sampling) → double scaling law (theory) → loss of skills → multi-generation amplification → mixing produces grokking → validated on Llama2 + GCD transformer"
  contribution_framing: "4 contributions: (1) double scaling law, (2) triplet scaling law (capacity-limited), (3) multi-generation universality, (4) mitigation via mixing + grokking"
  intro_structure: "Long intro with progressive research question development, citing Zipf's law, scaling laws, contamination evidence (LAION-5B), then contributions"
  notable_technique: "Connecting model collapse to scaling laws is the key conceptual innovation — makes the problem relevant to the broader ML community beyond just the synthetic data niche. The GCD 'skill emergence' experiment (Figure 4 right) is a brilliant visual: groups of new GCDs appear as 'bursts' that stop appearing with AI data."

figures:
  figure_count: 35
  figure1:
    type: "motivation"
    description: "Three mechanisms of tail degradation (top-p, temperature, finite sample) → two consequences (loss of scaling law, loss of skills/GCDs)"
    narrative_role: "Conceptual framing figure linking cause (tail damage) to effect (scaling breakdown + skill loss)"
    design_elements: ["distribution tail diagrams", "scaling law curves", "GCD skill illustration"]
    visual_style: "Split layout: left=mechanisms, top-right=scaling, bottom-right=skill loss"
  result_figures:
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "Three theoretical predictions: double scaling law, multi-generation collapse, grokking"
      how_gain_highlighted: "Theory curves (broken lines) match empirical points perfectly"
      design_note: "Three-panel 'signature figure' that previews all main results; theory-experiment overlay"
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      what_compared: "Llama2 scaling across generations (left), GCD transformer scaling (middle), skill emergence (right)"
      how_gain_highlighted: "Clean data curves keep descending; AI data curves plateau; skills stop emerging"
      design_note: "Three diverse experiments in one figure — universality across model types and tasks"
    - figure_id: "Figure 7"
      viz_type: "line_plot"
      what_compared: "Llama2 mixing 98% AI + 2% real → grokking curve"
      how_gain_highlighted: "Grokking prediction from theory perfectly matches LLM experiment"
      design_note: "Theory-to-practice validation on real LLM — strongest evidence in the paper"
  ablation_figures:
    - figure_id: "Figure 2"
      viz_type: "bar_chart"
      dimensions_varied: ["top-p setting", "temperature", "generation type"]
      design_note: "Empirical measurement of tail degradation on Llama2 and GCD — grounds the theoretical assumptions"
    - figure_id: "Figure 6"
      viz_type: "line_plot"
      dimensions_varied: ["generation count", "top-p value"]
      design_note: "Multi-generation Hutter++ with top-p showing how inference settings compound collapse"
  figure_narrative_role: "Fig1(mechanism cartoon) → Fig2(empirical tails) → Fig3(theory preview) → Fig4(main experiments) → Fig5-6(extended theory) → Fig7(grokking validation) → appendix(extensive confirmations)"

tables:
  table_count: 4
  main_result_table:
    table_id: "Table 1"
    row_axis: "GCD bases"
    col_axis: "accuracy, number of correct GCDs"
    row_organization: "by_dataset"
    col_organization: "flat"
    highlight_strategy: "no highlighting — descriptive"
    statistical_reporting: "single model values"
    num_baselines: 0
    design_note: "Simple descriptive table showing initial model capabilities; sets up the 'skills to lose' baseline"
  ablation_tables:
    - table_id: "Table 2"
      what_varied: ["training samples (30M/60M/90M)", "clean vs AI data"]
      variation_style: "full_numbers"
      design_note: "Shows AI data matches clean at early stages but diverges later — timing of collapse"
    - table_id: "Table 3"
      what_varied: ["300M vs 1B samples", "clean vs AI"]
      variation_style: "full_numbers"
      design_note: "Scaling comparison: 1B clean data learns new GCDs, 1B AI data doesn't"
    - table_id: "Table 4"
      what_varied: ["mixture ratio of AI data", "GCD base"]
      variation_style: "full_numbers"
      design_note: "Grokking delay increases monotonically with AI fraction"
  supplementary_tables:
    in_appendix: true
    content: "Extended results across all experimental settings"
    reason: "35 figures + 4 tables in main = very dense paper; appendix has extensive confirmations"
```

---

## dohmatob2025strong.yaml

```yaml
paper_key: "dohmatob2025strong"
title: "Strong Model Collapse"
venue: "ICLR 2025 Spotlight"
full_text_available: true

research:
  baselines:
    - "Training on real data only (p2=0)"
    - "Weighted single-step mixing (Jain et al. 2024)"
    - "Iterative/dynamic mixing (Ferbach et al. 2024)"
  metrics:
    - {name: "Test error (MSE)", direction: "lower_better"}
    - {name: "Test loss (cross-entropy)", direction: "lower_better"}
    - {name: "Scaling law exponents (implicit)", direction: "higher_better"}
  datasets:
    - {name: "Gaussian synthetic data", size: "n=500, d=600"}
    - {name: "MNIST", size: "10K-50K", task: "regression"}
    - {name: "BabiStories", size: "2.2M train + 22K val", task: "LM pretraining"}
    - {name: "TinyStories test set", size: "N/A", task: "evaluation"}
  ablation_dimensions:
    - synthetic_proportion_p2 (0-1, 11 values)
    - model_size_hidden_dim (100-10000)
    - model_depth_layers (12, 18, 24)
    - data_quality_c2 (0, 0.1, 0.5, 1.0)
    - mixing_strategy (single-step vs iterative)
    - mixing_weight_alpha
  training_recipe:
    MNIST: "SGD, lr=0.1, batch=128, 400 epochs"
    GPT2: "d=768, 12/18/24 layers, 12 heads, context=512, lr=5e-3, dropout=0.05, weight_decay=0.1, warmup=2000"
    synthetic_gen: "GPT-2-small, temperature=1, top-p=1"
    hardware: "not specified"
  method_family: "strong_collapse_theory"

positioning:
  core_claim: "Even 1% synthetic data causes irreversible model collapse (test error plateaus above baseline) — 'strong model collapse'. Larger models amplify collapse in underparameterized regime but can mitigate it past interpolation threshold (double descent in collapse)."
  key_results: "Etest ≃ B+V+ζ where ζ=p2²c² is irreducible collapse term; 1% synthetic data causes visible scaling law degradation in GPT-2; optimal mixing weight α*→0 as n→∞; iterative mixing underperforms real-only training"
  limitations:
    - "Theory assumes Gaussian features, linear labels, ridge regression"
    - "Random projections as neural network proxy"
    - "No practical mitigation beyond discarding synthetic data"
  relation_to_us: "foundation"

narrative:
  story_type: "突破局限型"
  hook: "Within the scaling laws paradigm that underpins ChatGPT and Llama training — can even small amounts of synthetic data cause collapse?"
  tension: "Prior work showed collapse with fully synthetic data. The natural hope is that mixing real + synthetic data can fix it. This paper kills that hope."
  key_insight: "Section 3, Theorem 1 — bias-variance decomposition Etest ≃ B+V+ζ reveals an extra term ζ=p2²c² from synthetic data that does NOT vanish as n→∞. Even p2=0.01 means ζ≈0.0001·c², creating an irreducible floor. This is 'strong' model collapse."
  argument_chain: "scaling laws paradigm → mix real+synthetic data → new bias-variance decomposition with extra ζ term → ζ doesn't vanish (strong collapse) → model size effect (double descent) → existing mixing strategies fail → validated on MNIST + GPT-2/BabiStories"
  contribution_framing: "2 results framed as research questions: Q1 (is collapse inevitable with mixing?) → yes (strong collapse), Q2 (do larger models help?) → double descent"
  intro_structure: "2 paragraphs: P1=model collapse context (with extensive citations), P2=scaling concerns for ChatGPT/Llama; then S1.1=contributions"
  notable_technique: "The Pareto diagram (Figure 1) is a novel visualization: real-only error on x-axis, mixed-data error on y-axis, model size as color. Points above diagonal = collapse. Creates immediate intuition about when and how much collapse occurs."

figures:
  figure_count: 10
  figure1:
    type: "teaser_result"
    description: "Pareto diagram comparing test error with real-only vs mixed data, with model size encoded as color, across synthetic data quality levels"
    narrative_role: "Immediate visual proof that mixed data always hurts (points above diagonal), with model size interaction"
    design_elements: ["scatter plot", "diagonal reference line", "colorbar for model size", "quality level panels"]
    visual_style: "3-panel scatter with color gradient, Pareto frontiers annotated"
  result_figures:
    - figure_id: "Figure 2"
      viz_type: "line_plot"
      what_compared: "Bias B, Variance V, Extra term ζ, and total Etest as function of model width"
      how_gain_highlighted: "ζ term clearly shows as irreducible floor above clean-data curve; double descent visible"
      design_note: "4-panel decomposition makes the mechanism transparent — readers can see exactly which component causes collapse"
    - figure_id: "Figure 3"
      viz_type: "line_plot"
      what_compared: "Scaling laws under different synthetic proportions p2 (theory vs experiment)"
      how_gain_highlighted: "Theory curves (broken) perfectly overlay experiment (solid); increasing p2 bends scaling curve"
      design_note: "Theory-experiment agreement is pixel-perfect — strongest validation"
    - figure_id: "Figure 8"
      viz_type: "line_plot"
      what_compared: "GPT-2 test loss vs tokens under varying p2 (left) and model size with p2=1 (right)"
      how_gain_highlighted: "Even p2=0.001 visibly bends the scaling curve; larger models cross over at ~10^10 tokens"
      design_note: "The GPT-2 experiment is the clincher — theory predictions hold for real LLMs"
  ablation_figures:
    - figure_id: "Figure 4"
      viz_type: "line_plot"
      dimensions_varied: ["model width m", "data quality c²", "synthetic proportion p2"]
      design_note: "4 panels × multiple p2 curves — exhaustive exploration of the parameter space"
    - figure_id: "Figure 6"
      viz_type: "line_plot"
      dimensions_varied: ["model hidden dim (100-10000)", "sample count"]
      design_note: "MNIST fully-trained network confirms theory predictions from random projections proxy"
    - figure_id: "Figure 7"
      viz_type: "line_plot"
      dimensions_varied: ["synthetic proportion p2 (0-0.9)", "sample count"]
      design_note: "Random feature model (left) vs fully-trained (right) — both show same pattern"
  figure_narrative_role: "Fig1(Pareto overview) → Fig2(B-V-ζ decomposition) → Fig3-5(theory validation on toy) → Fig6-7(MNIST) → Fig8(GPT-2) → Fig9-10(mixing strategy failure)"

tables:
  table_count: 0
  main_result_table: "N/A — all results via figures; scaling law exponents and Pareto frontiers visualized"
  ablation_tables: []
  supplementary_tables:
    in_appendix: true
    content: "Proofs, additional experiments, training details"
    reason: "Theory-heavy paper; all visual evidence in main text, proofs in appendix"
```

---

## dces2026counter.yaml

```yaml
paper_key: "dces2026counter"
title: "Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling"
venue: "MDPI Electronics 2026"
full_text_available: false

research:
  baselines: ["naive random sampling", "PPL filtering", "SemDeDup"]
  metrics:
    - {name: "Perplexity (PPL)", direction: "lower_better"}
    - {name: "training loss", direction: "lower_better"}
    - {name: "entropy", direction: "higher_better"}
  datasets:
    - {name: "WikiText-2", size: "N/A", task: "OOD evaluation"}
    - {name: "Alpaca", size: "N/A", task: "in-distribution"}
  ablation_dimensions:
    - sampling_strategy (random, PPL_filter, SemDeDup, DCES)
    - model_scale (GPT-2, OPT-125M, Qwen, OPT-6.7B)
    - iteration_count (10 rounds)
  training_recipe: {models: "GPT-2, OPT-125M, Qwen, OPT-6.7B"}
  method_family: "dynamic_data_selection_for_collapse"

positioning:
  core_claim: "DCES (Dynamic Center-Edge Sampling) constructs automated bias-correction via dynamic inter/intra-cluster sampling, reducing PPL degradation from 33.14→29.70 (vs naive) on OPT-125M after 10 self-training rounds."
  key_results: "OPT-125M WikiText-2 PPL: naive 23.56→33.14; DCES →29.70; SemDeDup →30.50"
  limitations: ["abstract-only extraction"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## truong2025entropy.yaml

```yaml
paper_key: "truong2025entropy"
title: "Entropy Collapse: A Universal Failure Mode of Intelligent Systems"
venue: "arXiv 2025"
full_text_available: false

research:
  baselines: ["second-order transition assumption (null hypothesis)"]
  metrics:
    - {name: "entropy order parameter m", direction: "context_dependent"}
    - {name: "hysteresis ΔH_hyst (nats)", direction: "lower_better"}
    - {name: "relaxation exponent ν", direction: "context_dependent"}
  datasets:
    - {name: "SmallGPT (2-layer autoregressive transformer)", size: "N=50 vocabulary, 92 conditions, 8 seeds"}
  ablation_dimensions:
    - feedback_amplification_alpha
    - novelty_regeneration_beta
    - feedback_curvature_class (Class1 convex vs Class2 linear)
  training_recipe: {model: "SmallGPT, 2-layer autoregressive, N=50 vocab"}
  method_family: "entropy_collapse_phase_transition_theory"

positioning:
  core_claim: "Entropy collapse is a first-order (discontinuous) phase transition at α_c=1/(1-β), with hysteresis and no early warning signals. Unifies AI model collapse, economic sclerosis, and evolutionary bottlenecks."
  key_results: "ΔH_hyst=2.92 nats (neural) > 2.73 (theory); ν=1.14±0.13; two universality classes"
  limitations: ["abstract-only extraction"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## wang2026contaminated.yaml

```yaml
paper_key: "wang2026contaminated"
title: "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training"
venue: "arXiv 2026"
full_text_available: false

research:
  baselines: ["prior Gaussian/discrete model assumptions"]
  metrics:
    - {name: "convergence rate", direction: "higher_better"}
  datasets: []
  ablation_dimensions:
    - real_data_fraction
    - sampling_bias
    - generative_model_type (universal approximator)
  training_recipe: {focus: "theoretical, general framework with minimal assumptions"}
  method_family: "contaminated_recursive_training_theory"

positioning:
  core_claim: "First positive theoretical result on recursive training without distributional assumptions: convergence rate equals min(baseline model rate, real data fraction). Extends to sampling bias settings."
  key_results: "Convergence rate = min(baseline rate, real data fraction per iteration)"
  limitations: ["abstract-only extraction"]
  relation_to_us: "foundation"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## du2026geometric.yaml

```yaml
paper_key: "du2026geometric"
title: "Escaping Mode Collapse in LLM Generation via Geometric Regulation"
venue: "arXiv 2026 (ICML 2026 accepted)"
full_text_available: false

research:
  baselines: ["standard decoding (no intervention)"]
  metrics:
    - {name: "entropy rate (nats/step)", direction: "context_dependent"}
    - {name: "mode collapse frequency", direction: "lower_better"}
    - {name: "generation quality", direction: "higher_better"}
  datasets: []
  ablation_dimensions:
    - intervention_method (RMR vs standard)
    - entropy_rate_threshold
  training_recipe: {method: "RMR (low-rank damping of value cache)"}
  method_family: "geometric_regulation_for_mode_collapse"

positioning:
  core_claim: "Mode collapse is geometric collapse (internal trajectory confined to low-dimensional subspace). RMR (Reinforced Mode Regulation) damps self-reinforcing directions in transformer value cache, enabling stable generation at 0.8 nats/step (vs 2.0 nats/step collapse threshold for standard)."
  key_results: "Stable generation at 0.8 nats/step; standard decoding collapses near 2.0 nats/step"
  limitations: ["abstract-only extraction"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

---

## gauthier2026alignment.yaml

```yaml
paper_key: "gauthier2026alignment"
title: "Explaining and Preventing Alignment Collapse in Iterative RLHF"
venue: "arXiv 2026"
full_text_available: false

research:
  baselines: ["standard iterative RLHF (PPO-style)"]
  metrics:
    - {name: "alignment quality", direction: "higher_better"}
    - {name: "reward hacking frequency", direction: "lower_better"}
  datasets:
    - {name: "controlled environments", size: "N/A"}
    - {name: "LLM alignment pipeline", size: "N/A", model: "Llama-3.2-1B"}
  ablation_dimensions:
    - optimization_method (standard RLHF vs FPO)
    - steering_term (included vs dropped)
  training_recipe: {models: "Llama-3.2-1B", method: "FPO (foresighted policy optimization)"}
  method_family: "alignment_collapse_prevention"

positioning:
  core_claim: "Standard iterative RLHF drops a 'parameter-steering term' from the Stackelberg game gradient, causing alignment collapse (policy exploits RM blind spots). FPO restores this term via regularization."
  key_results: "FPO prevents alignment collapse on Llama-3.2-1B"
  limitations: ["abstract-only extraction"]
  relation_to_us: "complementary"

narrative: "N/A"
figures: "N/A"
tables: "N/A"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f44e2ded-940c-4df1-b3ce-032b922c6c4b",
  "isSidechain": true,
  "agentId": "af2fbae3ae7b535a3",
  "requestId": "req_011CbHgTGN3JnPnbZX3pdehJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "46a5b45d-c8c1-4a76-ba46-064dce3056db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/distiller_3275b75a",
  "sessionId": "90945114-fddb-4708-8635-e1e588525e36",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HaaSS2oZgsUoHGTUDVnMKq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 28110,
      "cache_read_input_tokens": 14981,
      "output_tokens": 20712,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28110
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 20712,
          "cache_read_input_tokens": 14981,
          "cache_creation_input_tokens": 28110,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28110,
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
