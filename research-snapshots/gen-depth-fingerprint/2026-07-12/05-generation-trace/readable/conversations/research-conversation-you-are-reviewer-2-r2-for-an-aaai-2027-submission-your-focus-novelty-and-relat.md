# Research conversation: You are Reviewer 2 (R2) for an AAAI 2027 submission. Your focus: **Novelty and Related Work**. ## Venue Context - AAAI a

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 2
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aae1c9af8c0574a94.jsonl`
- **Structured JSON:** [`f5b241eb3e4cd8f6301a.json`](../../sessions/f5/f5b241eb3e4cd8f6301a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

5 recorded events

### User

_source line 1 · 2026-05-14T18:51:22.323Z_

You are Reviewer 2 (R2) for an AAAI 2027 submission. Your focus: **Novelty and Related Work**.

## Venue Context
- AAAI acceptance rate: ~17.6% (very competitive)
- Standard 1-10 scale: 10=top 5% seminal, 8=top 50% accept, 7=accept, 6=marginally above threshold, 5=marginally below, 4=not good enough, 3=clear reject
- Evaluation dimensions: technical soundness, significance, novelty, clarity, reproducibility

## Paper to Review
Read the PDF at: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/review_input_e90a5c14.pdf`

## Experiment Design Reference
Read the full imagined experiment list at: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/review_context.yaml`
This YAML contains the complete set of experiments the paper should ideally cover. Use it to assess whether the paper's novelty claims are adequately supported.

## Your Review Focus (R2: Novelty + Related Work)
Evaluate:
1. **Problem novelty**: Is "generation depth estimation" genuinely new? Has it been studied before under a different name? Is the problem well-motivated?
2. **Methodological novelty**: Are the features (entropy stats, hapax ratio, TTR) novel or simply standard NLP features applied to a new task? Is there algorithmic innovation?
3. **Related work coverage**: Are key related works cited? Missing references? Is the positioning against prior art accurate and fair?
   - Model collapse literature (Shumailov et al., Briesch et al.)
   - Synthetic text detection (DetectGPT, FastDetectGPT, watermarking, LD-Score)
   - Data provenance and curation
   - Any missing lines of work (e.g., membership inference, dataset contamination detection, LLM fingerprinting)
4. **Significance of contributions**: Are the three claimed contributions actually significant for AAAI? Would the community care?
5. **H1/H2 hypothesis framing**: Is this truly novel theoretical contribution or obvious observation dressed up in formal language?
6. **Incremental vs. substantial**: Is this a solid full paper or more of a workshop paper?

## Output Format
Provide your review in this exact structure:

### Summary
(2-3 sentences summarizing the paper)

### Strengths
(Bulleted list, each with [S1], [S2], etc. labels)

### Weaknesses
(Bulleted list, each with [W1], [W2], etc. labels — be specific and actionable)

### Questions for Authors
(Numbered list)

### Related Work Gap Analysis
(Specific missing references or lines of work, with explanation of why they matter)

### Novelty Assessment
(Detailed analysis: what's truly new vs. incremental vs. straightforward application of existing tools)

### Minor Issues
(Bulleted list of presentation, typos, etc.)

### Preliminary Rating
- Overall: X/10 (with justification referencing AAAI threshold)
- Novelty: X/5
- Significance: X/5
- Confidence: X/5

Do NOT read the paper superficially. Read every table, every claim, every section carefully. Be rigorous but fair.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4853647d-0304-42ff-bb28-2931a50b53eb",
  "agentId": "aae1c9af8c0574a94",
  "type": "user",
  "uuid": "a7c6a37b-8e23-4973-9ebc-2ffc148a640a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T18:51:22.324Z_

```json
{
  "parentUuid": "a7c6a37b-8e23-4973-9ebc-2ffc148a640a",
  "isSidechain": true,
  "agentId": "aae1c9af8c0574a94",
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
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
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
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "4bb3a6cf-be34-4ea9-b8d2-e2f3f6e07686",
  "timestamp": "2026-05-14T18:51:22.324Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T18:51:24.962Z_



I'll start by reading the paper PDF and the experiment context YAML.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bb3a6cf-be34-4ea9-b8d2-e2f3f6e07686",
  "isSidechain": true,
  "agentId": "aae1c9af8c0574a94",
  "requestId": "req_011Cb2xuqVsnWwNiqdrPTNcL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f0589a22-dc66-4982-b050-8f2c19808547",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Puju4bmTsGvFf4Fn5GpvvH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6668,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6668,
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

_source line 4 · 2026-05-14T18:51:25.921Z_

<details open><summary>🔧 Tool call — Read · `toolu_017mxugSbHZCkZp6WWKPd4DB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/review_input_e90a5c14.pdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0589a22-dc66-4982-b050-8f2c19808547",
  "isSidechain": true,
  "agentId": "aae1c9af8c0574a94",
  "requestId": "req_011Cb2xuqVsnWwNiqdrPTNcL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "59991be7-d743-43f0-8df8-26afa954fbc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Puju4bmTsGvFf4Fn5GpvvH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6668,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6668,
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

_source line 5 · 2026-05-14T18:51:25.944Z_

<details><summary>↩ Tool result · `toolu_017mxugSbHZCkZp6WWKPd4DB`</summary>

```text
PDF file read: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/review_input_e90a5c14.pdf (150KB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59991be7-d743-43f0-8df8-26afa954fbc3",
  "isSidechain": true,
  "promptId": "4853647d-0304-42ff-bb28-2931a50b53eb",
  "agentId": "aae1c9af8c0574a94",
  "type": "user",
  "uuid": "57bb6c20-15a7-4d15-9649-75dcaffcd15d",
  "sourceToolAssistantUUID": "59991be7-d743-43f0-8df8-26afa954fbc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

10 recorded events

### User

_source line 6 · 2026-05-14T18:51:25.943Z_

```json
{
  "type": "document",
  "source": {
    "type": "base64",
    "media_type": "application/pdf",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57bb6c20-15a7-4d15-9649-75dcaffcd15d",
  "isSidechain": true,
  "promptId": "4853647d-0304-42ff-bb28-2931a50b53eb",
  "agentId": "aae1c9af8c0574a94",
  "type": "user",
  "isMeta": true,
  "uuid": "a136e156-5fe0-4a90-89c4-cdc9c08c2a2d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T18:51:26.162Z_

<details open><summary>🔧 Tool call — Read · `toolu_01N87knH15XS1w36YdYChqBB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a136e156-5fe0-4a90-89c4-cdc9c08c2a2d",
  "isSidechain": true,
  "agentId": "aae1c9af8c0574a94",
  "requestId": "req_011Cb2xuqVsnWwNiqdrPTNcL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1643f296-adba-43d2-90c8-a089148637a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Puju4bmTsGvFf4Fn5GpvvH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6668,
      "cache_read_input_tokens": 8250,
      "output_tokens": 213,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6668
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 213,
          "cache_read_input_tokens": 8250,
          "cache_creation_input_tokens": 6668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6668,
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

_source line 8 · 2026-05-14T18:51:26.439Z_

<details><summary>↩ Tool result · `toolu_01N87knH15XS1w36YdYChqBB`</summary>

```text
1	narrative_guidance: 'Reframe Claim 2 from "independent signal" to "complementary multi-view
2	  signal." Reference features and surface features capture different facets of distributional
3	  drift — vocabulary depletion (hapax, TTR) vs probability-mass redistribution (entropy
4	  stats, tail decay). Neither dominates; both are needed. Cross-generator generalization
5	  degrades ~12 F1 points from MVP, with honest per-generator variance reporting showing
6	  Qwen/OLMo holdouts hardest. Shift gen-1/gen-2+ story toward binary depth-aware stratification
7	  (gen-0 vs gen-1+) as primary discriminative boundary; ordinal depth as secondary
8	  finding with diminishing marginal signal. Downstream utility is suggestive (ρ≈0.45)
9	  but the filtering advantage over binary baselines is modest (~1.8%). Add failure-mode
10	  analysis showing reference features rescue specific generators/domains where surface
11	  shortcuts break down. Still submittable to AAAI with adjusted claim strength and
12	  "complementary multi-view" framing.
13	
14	  '
15	imagined_experiments:
16	- name: feature_ablation_and_trend
17	  plan_id: plan_001
18	  description: 'Three-part analysis on MVP data. (A) Feature ablation: ref-only vs
19	    surface-only vs full, XGBoost 5-fold CV. (B) H1/H2 trend: per-feature mean±std
20	    across depth 0-4, linear regression slope + R². (C) Perplexity pre-validation:
21	    Pythia-410M PPL on depth-stratified subsets.
22	
23	    '
24	  expected_results:
25	    ref_only_macro_f1: 0.71
26	    ref_only_gen0_f1: 0.82
27	    ref_only_gen1_f1: 0.63
28	    ref_only_gen2plus_f1: 0.68
29	    surface_only_macro_f1: 0.72
30	    surface_only_gen0_f1: 0.85
31	    surface_only_gen1_f1: 0.62
32	    surface_only_gen2plus_f1: 0.69
33	    full_macro_f1: 0.83
34	    full_gen0_f1: 0.94
35	    full_gen1_f1: 0.75
36	    full_gen2plus_f1: 0.8
37	    ref_minus_surface_delta: -0.01
38	    full_minus_best_single_delta: 0.11
39	    mcnemar_full_vs_surface_p: 0.0003
40	    mcnemar_full_vs_ref_p: 0.0005
41	    mcnemar_ref_vs_surface_p: 0.42
42	    entropy_mean_slope: 0.12
43	    entropy_mean_r2: 0.89
44	    entropy_std_slope: 0.08
45	    entropy_std_r2: 0.72
46	    tail_decay_slope: -0.09
47	    tail_decay_r2: 0.78
48	    hapax_ratio_slope: -0.08
49	    hapax_ratio_r2: 0.91
50	    ttr_slope: -0.06
51	    ttr_r2: 0.83
52	    ppl_gen0: 18.5
53	    ppl_gen1: 22.3
54	    ppl_gen2: 25.1
55	    ppl_gen3: 26.8
56	    ppl_gen4: 27.4
57	    ppl_kruskal_wallis_p: 1.0e-05
58	  result_rationale: 'hapax_ratio 是 MVP 中的主导特征（feature importance ~0.35），surface-only
59	    天然继承了这一优势， 所以 surface-only（0.72）和 ref-only（0.71）打平——不是因为 reference 特征弱，而是因为 hapax_ratio
60	    太强。但两组特征捕捉的是 distributional drift 的不同侧面：surface 特征测量词汇 贫化（type 减少），reference 特征测量概率质量重分布（entropy
61	    升高、tail 变陡）。这两个视角 在大部分样本上一致（都能检测 gen-0），但在边界案例上互补——surface 特征在词汇本身丰富的 generator（如
62	    Qwen）上失灵，reference 特征在输出分布接近参考模型的情况下失灵。Full model 的 +11 F1 跳跃（0.83 vs 0.72）来自这些互补的边界案例的正确分类，McNemar
63	    检验显著确认 组合增益不是噪声。H1/H2 trend 支持 H2（divergence）——所有特征在 depth 0-2 区间单调 变化，但 slope
64	    在 depth 3-4 变缓，说明 drift 速率递减而非匀速累积。Perplexity 预验证 显示 gen-0→gen-1 跳跃（+3.8 PPL）远大于
65	    gen-3→gen-4（+0.6 PPL），预示 Claim 3 的 downstream utility signal 存在但集中在低深度区间。
66	
67	    '
68	  tables:
69	  - name: 'Table 1: Feature Ablation (3-class, 5-fold CV)'
70	    columns:
71	    - feature_set
72	    - macro_f1
73	    - gen0_f1
74	    - gen1_f1
75	    - gen2plus_f1
76	    - n_features
77	    rows:
78	    - - ref-only
79	      - 0.71
80	      - 0.82
81	      - 0.63
82	      - 0.68
83	      - 5
84	    - - surface-only
85	      - 0.72
86	      - 0.85
87	      - 0.62
88	      - 0.69
89	      - 2
90	    - - full
91	      - 0.83
92	      - 0.94
93	      - 0.75
94	      - 0.8
95	      - 7
96	  - name: 'Table 2: H1/H2 Trend — Linear Regression per Feature'
97	    columns:
98	    - feature
99	    - slope_per_depth
100	    - r_squared
101	    - direction
102	    - monotonic
103	    rows:
104	    - - entropy_mean
105	      - 0.12
106	      - 0.89
107	      - increasing
108	      - 'yes'
109	    - - entropy_std
110	      - 0.08
111	      - 0.72
112	      - increasing
113	      - 'yes'
114	    - - entropy_min
115	      - 0.05
116	      - 0.61
117	      - increasing
118	      - 'yes'
119	    - - entropy_max
120	      - 0.03
121	      - 0.45
122	      - increasing
123	      - weak
124	    - - tail_decay
125	      - -0.09
126	      - 0.78
127	      - decreasing
128	      - 'yes'
129	    - - TTR
130	      - -0.06
131	      - 0.83
132	      - decreasing
133	      - 'yes'
134	    - - hapax_ratio
135	      - -0.08
136	      - 0.91
137	      - decreasing
138	      - 'yes'
139	  - name: 'Table 3: Perplexity by Depth (Pythia-410M, no fine-tuning)'
140	    columns:
141	    - depth
142	    - mean_ppl
143	    - std_ppl
144	    - n_samples
145	    rows:
146	    - - gen-0
147	      - 18.5
148	      - 4.2
149	      - 995
150	    - - gen-1
151	      - 22.3
152	      - 5.1
153	      - 982
154	    - - gen-2
155	      - 25.1
156	      - 5.8
157	      - 968
158	    - - gen-3
159	      - 26.8
160	      - 6.3
161	      - 955
162	    - - gen-4
163	      - 27.4
164	      - 6.7
165	      - 942
166	  figures_description:
167	  - 'Fig 1a: Box plots of each feature (7 panels) across depth 0-4. Shows monotonic
168	    shift for entropy_mean and hapax_ratio; weaker for entropy_max. Supports H2 with
169	    diminishing marginal drift.'
170	  - 'Fig 1b: Scatter plot of ref-only vs surface-only error overlap — Venn-style analysis
171	    showing ~30% of errors are shared, ~35% unique to each. Justifies ''complementary''
172	    framing.'
173	  - 'Fig 1c: Perplexity vs depth curve with 95% CI bands. Clear gen-0→gen-1 jump,
174	    plateau at gen-3+.'
175	  analysis: 'Claim 2 需要从 "independent signal" 重新表述为 "complementary multi-view signal"。
176	    两组特征单独使用性能相当（McNemar p=0.42 不显著），但 full model 显著优于任何一方 （p<0.001）。关键证据是错误分析：ref-only
177	    和 surface-only 的错误集合重叠只有 ~30%， 说明它们确实捕捉了不同的 failure mode。这足以回应 RC1——"不仅仅是词汇贫化"的证据
178	    不在于 ref-only > surface-only，而在于 combining 它们产生的 synergy。H1/H2 分析 支持 H2 但需加 caveat：drift
179	    速率递减意味着深度估计在 gen-3+ 区间的分辨率有限。 Perplexity 预验证为 plan_004 亮绿灯。
180	
181	    '
182	- name: cross_generator_evaluation
183	  plan_id: plan_002
184	  description: '5 generators (Pythia-2.8B, OLMo-2-1B, Qwen3.5-2B, Qwen3.5-0.8B, Pythia-1B),
185	    leave-one-generator-out CV. 1000 seeds × 5 generators × 5 depths = 25K chains.
186	
187	    '
188	  expected_results:
189	    cross_gen_leave_one_out_macro_f1: 0.68
190	    cross_gen_leave_one_out_std: 0.04
191	    cross_gen_gen0_f1: 0.83
192	    cross_gen_gen1_f1: 0.62
193	    cross_gen_gen2plus_f1: 0.64
194	    holdout_pythia_2_8b_macro_f1: 0.65
195	    holdout_pythia_1b_macro_f1: 0.73
196	    holdout_olmo_2_1b_macro_f1: 0.67
197	    holdout_qwen3_5_2b_macro_f1: 0.64
198	    holdout_qwen3_5_0_8b_macro_f1: 0.71
199	    holdout_pythia_family_macro_f1: 0.62
200	    holdout_qwen_family_macro_f1: 0.65
201	    holdout_olmo_family_macro_f1: 0.67
202	    binary_gen0_vs_gen1plus_macro_f1: 0.79
203	    pooled_5fold_cv_macro_f1: 0.81
204	  result_rationale: 'Cross-generator 泛化损失 ~12 F1 点（0.81→0.68），符合 median 预期。损失主要集中在
205	    gen-1 分类（0.62）——gen-1 文本最接近人类写作，各 generator 的 gen-1 分布差异最大。 gen-0 仍高（0.83），因为真实文本的分布特征与所有
206	    generator 都不同。Per-generator holdout 方差来自两个因素：(1) 模型族内泄露——hold out Pythia-2.8B
207	    时 Pythia-1B 仍 在训练集，部分学到 Pythia-specific patterns，使 Pythia-1B holdout（0.73）偏高；
208	    (2) 模型能力差异——Qwen3.5-2B 是最强 generator，输出最接近人类分布，holdout 最难 （0.64）。leave-one-family-out
209	    更保守，Pythia family holdout 降至 0.62，说明 generator-family-specific patterns 确实有贡献但不占主导。Binary
210	    分类（gen-0 vs gen-1+） 达到 0.79，比 3-class 高 11 点，支持"gen-0 vs gen-1+ 是主要 discriminative
211	    boundary" 的叙事重构。
212	
213	    '
214	  tables:
215	  - name: 'Table 4: Leave-One-Generator-Out (3-class)'
216	    columns:
217	    - held_out_generator
218	    - macro_f1
219	    - gen0_f1
220	    - gen1_f1
221	    - gen2plus_f1
222	    rows:
223	    - - Pythia-2.8B
224	      - 0.65
225	      - 0.8
226	      - 0.56
227	      - 0.59
228	    - - Pythia-1B
229	      - 0.73
230	      - 0.87
231	      - 0.66
232	      - 0.66
233	    - - OLMo-2-1B
234	      - 0.67
235	      - 0.82
236	      - 0.6
237	      - 0.59
238	    - - Qwen3.5-2B
239	      - 0.64
240	      - 0.79
241	      - 0.55
242	      - 0.58
243	    - - Qwen3.5-0.8B
244	      - 0.71
245	      - 0.86
246	      - 0.64
247	      - 0.63
248	    - - '**Mean ± std**'
249	      - '**0.68±0.04**'
250	      - '**0.83±0.03**'
251	      - '**0.60±0.05**'
252	      - '**0.61±0.04**'
253	  - name: 'Table 5: Leave-One-Family-Out (3-class)'
254	    columns:
255	    - held_out_family
256	    - n_generators
257	    - macro_f1
258	    rows:
259	    - - Pythia (2.8B+1B)
260	      - 2
261	      - 0.62
262	    - - Qwen (2B+0.8B)
263	      - 2
264	      - 0.65
265	    - - OLMo (1B)
266	      - 1
267	      - 0.67
268	  - name: 'Table 6: 3-class vs Binary (gen-0 vs gen-1+)'
269	    columns:
270	    - task
271	    - leave_one_out_macro_f1
272	    - pooled_cv_macro_f1
273	    rows:
274	    - - 3-class (gen-0/gen-1/gen-2+)
275	      - 0.68
276	      - 0.81
277	    - - binary (gen-0 vs gen-1+)
278	      - 0.79
279	      - 0.89
280	  figures_description:
281	  - 'Fig 2a: Bar chart of leave-one-generator-out macro-F1 with error bars. Clear
282	    ordering: Pythia-1B easiest, Qwen3.5-2B hardest. Annotate family-holdout values.'
283	  - 'Fig 2b: Confusion matrix heatmap (averaged across holdouts). gen-1↔gen-2+ confusion
284	    dominates off-diagonal.'
285	  - 'Fig 2c: Per-generator feature importance comparison — shows hapax_ratio dominance
286	    is consistent but entropy_mean importance varies by generator.'
287	  analysis: 'Cross-generator 泛化是 median 叙事的关键张力：信号存在但有限。需要诚实报告 per-generator variance（std=0.04），并分析最差
288	    holdout（Qwen3.5-2B, 0.64）为什么难——Qwen 的 tokenizer 和训练数据与 Pythia reference model
289	    差异最大，导致 entropy 特征噪声增加。 family-holdout 结果（0.62-0.67）说明跨架构泛化的真实水平。Binary task 的强表现
290	    （0.79）支持叙事转向："即便 ordinal depth 分辨率有限，至少 gen-0 vs gen-1+ 的 binary screening 在跨
291	    generator 设置下可靠工作"。Paper 中应以 binary 结果为主打， ordinal 为 secondary finding。
292	
293	    '
294	- name: cross_family_reference_model
295	  plan_id: plan_003
296	  description: 'Non-Pythia reference models (OLMo-2-1B, Qwen3.5-0.8B) for feature
297	    extraction. Addresses RC2: is the signal architecture-specific?
298	
299	    '
300	  expected_results:
301	    pythia_410m_ref_macro_f1: 0.68
302	    olmo_2_1b_ref_macro_f1: 0.66
303	    qwen3_5_0_8b_ref_macro_f1: 0.62
304	    cross_family_ref_mean_macro_f1: 0.65
305	    best_ref_ensemble_macro_f1: 0.72
306	    ref_model_agreement_kappa: 0.58
307	  result_rationale: 'Pythia-410M 仍是最佳 reference model（0.68），因为 5 个 generator 中 2 个是
308	    Pythia 族， 且 Pythia 的训练数据（The Pile）与 seed 文本（Wikipedia）有大量重叠，使 reference 分布 更稳定。OLMo-2-1B（0.66）接近——OLMo
309	    也在高质量英文数据上训练，但其 tokenizer 粒度不同 导致 entropy 特征略有偏移。Qwen3.5-0.8B 最差（0.62），因为 Qwen
310	    的中英双语 tokenizer 在纯英文文本上效率较低，token-level entropy 统计包含更多 tokenization artifact 而非
311	    depth signal。关键发现：信号不完全是 architecture-specific（所有 reference model 都 显著高于 chance），但
312	    reference model 选择确实影响性能（6 F1 点差距）。三模型 ensemble （0.72）高于任何单模型，说明不同 reference model
313	    捕获了不同视角的 drift——这进一步 支持 "multi-view" 叙事。
314	
315	    '
316	  tables:
317	  - name: 'Table 7: Reference Model Comparison (leave-one-generator-out)'
318	    columns:
319	    - reference_model
320	    - params
321	    - macro_f1
322	    - gen0_f1
323	    - gen1_f1
324	    - gen2plus_f1
325	    rows:
326	    - - Pythia-410M
327	      - 410M
328	      - 0.68
329	      - 0.83
330	      - 0.62
331	      - 0.64
332	    - - OLMo-2-1B
333	      - 1B
334	      - 0.66
335	      - 0.81
336	      - 0.59
337	      - 0.62
338	    - - Qwen3.5-0.8B
339	      - 0.8B
340	      - 0.62
341	      - 0.77
342	      - 0.55
343	      - 0.58
344	    - - Ensemble (3 refs)
345	      - —
346	      - 0.72
347	      - 0.86
348	      - 0.65
349	      - 0.68
350	  figures_description:
351	  - 'Fig 3: Grouped bar chart comparing 3 reference models across generators. Shows
352	    Pythia-410M advantage is largest when evaluating Pythia generators, smallest for
353	    Qwen generators — architecture match matters but doesn''t dominate.'
354	  analysis: 'RC2 的回应：depth signal 不是 Pythia-specific artifact——OLMo 和 Qwen 作为 reference
355	    也能 检测，只是性能稍低。但需要 acknowledge reference model 选择对性能有实质影响（最多 6 F1 点）， 并建议 practitioner
356	    选择与目标文本同分布的 reference model。Ensemble 结果（+4 over best single）是 paper 的 bonus finding：如果计算预算允许，multi-reference
357	    方案进一步提升鲁棒性。
358	
359	    '
360	- name: downstream_utility
361	  plan_id: plan_004
362	  description: 'Fine-tune Pythia-410M on depth-stratified subsets. Measure PPL degradation
363	    vs depth. Compare depth-aware filtering vs binary baselines (FastDetectGPT, LD-Score
364	    threshold).
365	
366	    '
367	  expected_results:
368	    depth_quality_spearman_rho: 0.45
369	    depth_quality_spearman_p: 0.008
370	    finetune_ppl_gen0_only: 14.2
371	    finetune_ppl_gen0_plus_gen1: 15.1
372	    finetune_ppl_gen0_through_gen2: 16.8
373	    finetune_ppl_all_depths: 18.3
374	    finetune_ppl_gen2plus_only: 22.7
375	    ppl_no_filter: 18.3
376	    ppl_binary_fastdetectgpt_filter: 15.8
377	    ppl_binary_ldscore_filter: 16.1
378	    ppl_depth_aware_filter_keep_gen0_gen1: 15.1
379	    depth_filter_vs_fastdetectgpt_gap_pct: 1.8
380	    depth_filter_vs_ldscore_gap_pct: 2.4
381	    retention_binary_fastdetectgpt: 0.42
382	    retention_binary_ldscore: 0.45
383	    retention_depth_aware: 0.58
384	  result_rationale: 'Spearman ρ=0.45 说明 depth 与 fine-tuning quality 中等相关——不是完美的因果关系，因为
385	    部分 gen-1 文本质量不低于 gen-0（尤其是当 generator 能力强且 seed 本身质量一般时）。 PPL 随 depth 单调上升但边际递减（gen-0→gen-1:
386	    +0.9, gen-1→gen-2: +1.7, gen-2→all: +1.5）， 与 plan_001 的 perplexity pre-validation
387	    一致。Depth-aware filtering 的 PPL 优势 （1.8% over FastDetectGPT）来自更高的数据保留率（0.58 vs
388	    0.42）——binary detector 把 所有 synthetic 都扔掉（包括有用的 gen-1），而 depth-aware filter 选择性保留
389	    gen-1， 在更大训练集上获得更好的泛化。但 1.8% 的 gap 只是 suggestive——单次 fine-tuning run 的方差可能吃掉这个差距。需要多次
390	    seed 运行和 bootstrap CI 来评估显著性，预期 p≈0.06, 不一定达到 0.05 门槛。
391	
392	    '
393	  tables:
394	  - name: 'Table 8: Fine-tuning PPL by Training Data Depth Composition'
395	    columns:
396	    - training_data
397	    - depth_range
398	    - n_samples
399	    - held_out_ppl
400	    rows:
401	    - - gen-0 only
402	      - 0
403	      - 5000
404	      - 14.2
405	    - - gen-0 + gen-1
406	      - 0-1
407	      - 10000
408	      - 15.1
409	    - - gen-0 through gen-2
410	      - 0-2
411	      - 15000
412	      - 16.8
413	    - - all depths
414	      - 0-4
415	      - 25000
416	      - 18.3
417	    - - gen-2+ only
418	      - 2-4
419	      - 15000
420	      - 22.7
421	  - name: 'Table 9: Filtering Strategy Comparison'
422	    columns:
423	    - strategy
424	    - held_out_ppl
425	    - data_retention
426	    - ppl_improvement_vs_no_filter_pct
427	    rows:
428	    - - No filter
429	      - 18.3
430	      - 1.0
431	      - —
432	    - - FastDetectGPT (binary)
433	      - 15.8
434	      - 0.42
435	      - 13.7
436	    - - LD-Score threshold (binary)
437	      - 16.1
438	      - 0.45
439	      - 12.0
440	    - - Depth-aware (keep gen-0+gen-1)
441	      - 15.1
442	      - 0.58
443	      - 17.5
444	  figures_description:
445	  - 'Fig 4a: Line plot of held-out PPL vs training data max-depth (0 through 4). Monotonically
446	    increasing with diminishing slope. Error bars from 3 random seeds.'
447	  - 'Fig 4b: Pareto frontier plot — data retention (x-axis) vs held-out PPL (y-axis).
448	    Depth-aware filter sits on Pareto front; binary filters dominated.'
449	  analysis: 'Claim 3 在 median tier 下定位为 "suggestive correlation" 而非强因果主张。ρ=0.45 说明
450	    depth 是 data quality 的有用但不完美的 proxy（其他因素如 domain、generator 能力也重要）。 Filtering 实验的关键
451	    insight 不是绝对 PPL 差异（1.8% 可能不显著），而是 Pareto efficiency——depth-aware filter 在保留更多数据的同时达到更低
452	    PPL。Paper 应该展示 Pareto frontier 图而非单点比较，让读者自行判断 trade-off 是否值得。
453	
454	    '
455	- name: prompt_type_comparison
456	  plan_id: plan_005
457	  description: 'Compare continuation vs elaboration vs inspired_rewriting chains.
458	    Same 1000 seeds, Pythia-2.8B, Pythia-410M reference. 3 prompt types × 5 depths.
459	
460	    '
461	  expected_results:
462	    continuation_macro_f1: 0.82
463	    elaboration_macro_f1: 0.77
464	    inspired_rewriting_macro_f1: 0.73
465	    continuation_hapax_importance: 0.35
466	    elaboration_hapax_importance: 0.28
467	    rewriting_hapax_importance: 0.21
468	    continuation_entropy_mean_importance: 0.18
469	    elaboration_entropy_mean_importance: 0.25
470	    rewriting_entropy_mean_importance: 0.3
471	    combined_3types_macro_f1: 0.75
472	  result_rationale: 'Continuation 最容易分类（0.82，接近 MVP），因为 continuation 的语义约束最弱——generator
473	    在开放式 continuation 中自由选择主题和词汇，vocabulary impoverishment 累积最规律。 Elaboration（0.77）介于中间——generator
474	    被要求围绕 seed 主题展开，语义锚定减少了词汇 drift 的幅度但不消除它。Inspired rewriting（0.73）最难——generator
475	    被允许自由改写， output 的词汇分布更接近 generator 的 prior 而非 seed 的 drift，使 depth signal 更弱。
476	    Feature importance 的变化揭示机制：continuation 中 hapax_ratio 主导（词汇贫化是主信号）， 但 inspired
477	    rewriting 中 entropy_mean 变得更重要（词汇贫化信号弱了，但概率质量重分布 仍可检测）。这进一步支持 "complementary features"
478	    叙事——不同 prompt type 下， 不同特征子集承担主要 discriminative 角色。
479	
480	    '
481	  tables:
482	  - name: 'Table 10: Prompt Type Comparison (single-generator, 5-fold CV)'
483	    columns:
484	    - prompt_type
485	    - macro_f1
486	    - gen0_f1
487	    - gen1_f1
488	    - gen2plus_f1
489	    - top_feature
490	    rows:
491	    - - continuation
492	      - 0.82
493	      - 0.93
494	      - 0.74
495	      - 0.79
496	      - hapax_ratio
497	    - - elaboration
498	      - 0.77
499	      - 0.9
500	      - 0.68
501	      - 0.73
502	      - hapax_ratio
503	    - - inspired_rewriting
504	      - 0.73
505	      - 0.87
506	      - 0.63
507	      - 0.69
508	      - entropy_mean
509	    - - combined (3 types)
510	      - 0.75
511	      - 0.89
512	      - 0.66
513	      - 0.7
514	      - hapax_ratio
515	  figures_description:
516	  - 'Fig 5a: Feature importance stacked bars for 3 prompt types. Shows hapax_ratio
517	    shrinks and entropy_mean grows from continuation → rewriting.'
518	  - 'Fig 5b: Per-depth feature distribution violin plots, faceted by prompt type.
519	    Continuation shows tight monotonic shift; rewriting shows wider variance per depth.'
520	  analysis: 'Prompt type 实验回应 RC6（ecological validity）。三种 prompt type 覆盖了从保守（continuation）
521	    到激进（inspired rewriting）的语义自由度谱。结论：depth signal 在所有 prompt type 下存在， 但强度随语义自由度增加而下降。Combined
522	    training（混合三种类型）是更 realistic 的评估设置， F1=0.75 是合理的 "real-world-ish" 期望值。
523	
524	    '
525	- name: paraphrastic_comparison
526	  plan_id: plan_006
527	  description: 'Parallel paraphrasing chains vs continuation chains. Tests attractor
528	    convergence theory. Same seeds, Pythia-2.8B, 5 depths.
529	
530	    '
531	  expected_results:
532	    paraphrase_chain_macro_f1: 0.67
533	    continuation_chain_macro_f1: 0.82
534	    paraphrase_depth2_vs_depth4_f1: 0.53
535	    continuation_depth2_vs_depth4_f1: 0.64
536	    paraphrase_entropy_mean_plateau_depth: 2
537	    continuation_entropy_mean_plateau_depth: null
538	    paraphrase_feature_drift_rate_depth3_4: 0.02
539	    continuation_feature_drift_rate_depth3_4: 0.06
540	  result_rationale: 'Paraphrasing chains 在 depth 2-3 后特征值趋于稳定（plateau），与 attractor
541	    cycle theory 一致——语义保持约束迫使输出分布收敛到 2-period cycle 附近，depth 信号 ceiling 在 ~3 class。
542	    Continuation chains 的特征值持续 drift（虽然速率递减但不 plateau），在 depth 4 仍有 可测量的增量变化。这是论文的核心
543	    theoretical contribution 之一：non-paraphrastic chains 的无界语义空间使 distributional drift
544	    能持续累积，打破 attractor cycle 的 ceiling。 但 continuation 的 depth-2 vs depth-4 分辨率仍然有限（F1=0.64），说明虽然信号不消失
545	    但变得越来越弱——实际应用中 3-class 可能仍是最优粒度。
546	
547	    '
548	  tables:
549	  - name: 'Table 11: Paraphrasing vs Continuation Chains'
550	    columns:
551	    - chain_type
552	    - macro_f1_3class
553	    - depth2_vs_depth4_f1
554	    - feature_drift_rate_d3_d4
555	    rows:
556	    - - paraphrasing
557	      - 0.67
558	      - 0.53
559	      - 0.02
560	    - - continuation
561	      - 0.82
562	      - 0.64
563	      - 0.06
564	  - name: 'Table 12: Feature Plateau Analysis'
565	    columns:
566	    - feature
567	    - paraphrase_plateau_depth
568	    - continuation_plateau_depth
569	    rows:
570	    - - entropy_mean
571	      - 2
572	      - '>4'
573	    - - hapax_ratio
574	      - 2
575	      - '>4'
576	    - - tail_decay
577	      - 3
578	      - '>4'
579	    - - TTR
580	      - 2
581	      - '>4'
582	  figures_description:
583	  - 'Fig 6: Dual-panel line plot — feature values (y) vs depth (x) for paraphrasing
584	    (left) and continuation (right). Paraphrasing shows clear plateau at depth 2-3;
585	    continuation shows diminishing but non-zero slope through depth 4.'
586	  analysis: '这是论文 story 中 "H1 vs H2" framing 的直接实验证据。Paraphrasing → H1 (convergence),
587	    continuation → H2 (divergence, at least through depth 4)。但需要 caveat：continuation
588	    的 drift rate 在递减，不排除更深的 depth（>10）最终也会 plateau——只是在可测量范围内 divergence 持续。Paper
589	    中应表述为 "within the depth range tested (0-4), non-paraphrastic chains show sustained
590	    drift while paraphrastic chains converge"。
591	
592	    '
593	- name: cross_model_chains
594	  plan_id: plan_007
595	  description: 'Different generator per depth step (cross-model chains) vs single-model
596	    chains. More realistic web contamination scenario.
597	
598	    '
599	  expected_results:
600	    cross_model_chain_macro_f1: 0.63
601	    single_model_chain_macro_f1: 0.68
602	    cross_model_degradation: 0.05
603	    cross_model_gen0_f1: 0.81
604	    cross_model_gen1_f1: 0.54
605	    cross_model_gen2plus_f1: 0.56
606	    cross_model_binary_gen0_vs_gen1plus_f1: 0.74
607	  result_rationale: 'Cross-model chains 比 single-model chains 降 5 F1 点（0.63 vs 0.68）。原因：single-model
608	    chain 的 drift 是同一 generator 偏差的累积放大——pattern 规律且可预测。Cross-model chain 的 drift
609	    是多个 generator 偏差的叠加——每步引入不同的 distributional shift 方向，使深度 信号变成异质 mixture 而非 monotonic
610	    progression。gen-1 受影响最大（0.54），因为 gen-1 的 distributional 特征同时受 seed text 和 generator
611	    偏差的双重影响——cross-model 设置下 这两个影响更难分离。gen-0 仍然相对稳健（0.81），因为真实文本与任何 generator 输出的区别
612	    不依赖于 generator-specific patterns。Binary task 仍可用（0.74），进一步支持 "gen-0 vs gen-1+
613	    是实际应用的推荐粒度" 的结论。
614	
615	    '
616	  tables:
617	  - name: 'Table 13: Single-Model vs Cross-Model Chains'
618	    columns:
619	    - chain_type
620	    - macro_f1
621	    - gen0_f1
622	    - gen1_f1
623	    - gen2plus_f1
624	    - binary_f1
625	    rows:
626	    - - single-model
627	      - 0.68
628	      - 0.83
629	      - 0.62
630	      - 0.64
631	      - 0.79
632	    - - cross-model
633	      - 0.63
634	      - 0.81
635	      - 0.54
636	      - 0.56
637	      - 0.74
638	    - - delta
639	      - -0.05
640	      - -0.02
641	      - -0.08
642	      - -0.08
643	      - -0.05
644	  figures_description:
645	  - 'Fig 7: Paired comparison bar chart. Annotate per-class delta. Show that degradation
646	    concentrates on gen-1 and gen-2+ while gen-0 is stable.'
647	  analysis: 'Cross-model 结果回应 RC4（realistic chains）。5 F1 点损失是 moderate——信号存在但需要 更多训练
648	    diversity。Paper 中建议将 cross-model 设置作为 primary evaluation（更保守 但更诚实），single-model
649	    作为 upper bound。
650	
651	    '
652	- name: multi_domain_seeds
653	  plan_id: plan_008
654	  description: '4 domains: Wikipedia, news (CNN/DailyMail), scientific (S2ORC), creative
655	    (WritingPrompts). 500 seeds × 4 domains × 5 depths. Tests domain sensitivity.
656	
657	    '
658	  expected_results:
659	    wikipedia_macro_f1: 0.7
660	    news_macro_f1: 0.68
661	    scientific_macro_f1: 0.64
662	    creative_macro_f1: 0.61
663	    cross_domain_mean_macro_f1: 0.66
664	    cross_domain_std: 0.04
665	    worst_domain_best_domain_gap: 0.09
666	    domain_feature_interaction_anova_p: 0.003
667	  result_rationale: 'Domain 差异主要通过 baseline vocabulary diversity 影响 surface 特征。Scientific
668	    text 天然有低 TTR（术语重复）和低 hapax ratio（固定专业词汇），压缩了 depth 相关的词汇贫化 信号空间——gen-0 scientific
669	    text 的 hapax_ratio 已经接近其他 domain 的 gen-2，使 depth discrimination 更难。Creative writing
670	    的方差最高——不同 seed 的创意风格差异大， noise 淹没了部分 depth signal。Wikipedia 和 news 表现最好，因为 seed
671	    text 分布 相对均匀，depth drift 的 signal-to-noise ratio 最高。ANOVA 交互效应显著（p=0.003） 说明 domain
672	    确实调节 depth signal 的强度，不能忽略。但即便最差 domain（creative, 0.61） 仍远高于 chance（0.33），说明 depth
673	    signal 跨 domain 鲁棒存在。
674	
675	    '
676	  tables:
677	  - name: 'Table 14: Per-Domain Performance (leave-one-generator-out)'
678	    columns:
679	    - domain
680	    - n_seeds
681	    - macro_f1
682	    - gen0_f1
683	    - gen1_f1
684	    - gen2plus_f1
685	    rows:
686	    - - Wikipedia
687	      - 500
688	      - 0.7
689	      - 0.85
690	      - 0.63
691	      - 0.62
692	    - - News
693	      - 500
694	      - 0.68
695	      - 0.83
696	      - 0.61
697	      - 0.6
698	    - - Scientific
699	      - 500
700	      - 0.64
701	      - 0.8
702	      - 0.56
703	      - 0.56
704	    - - Creative
705	      - 500
706	      - 0.61
707	      - 0.77
708	      - 0.52
709	      - 0.54
710	  figures_description:
711	  - 'Fig 8: Heatmap with domain (rows) × depth (columns), cell color = mean hapax_ratio.
712	    Shows scientific text has compressed hapax_ratio range across depths, explaining
713	    lower classification performance.'
714	  analysis: 'Domain 实验回应 RC6。Paper 应报告 per-domain 结果而非仅 aggregate，并讨论 domain 作为 confound
715	    的影响。Practical recommendation：在 domain-specific data curation 中， depth threshold
716	    应该 calibrate per domain（scientific 需要更宽松的 threshold）。
717	
718	    '
719	- name: finer_grained_ordinal
720	  plan_id: plan_009
721	  description: '5-class ordinal classification (gen-0 through gen-4). Tests if depth
722	    resolution extends beyond 3-class.
723	
724	    '
725	  expected_results:
726	    ordinal_5class_macro_f1: 0.51
727	    ordinal_3class_macro_f1: 0.68
728	    ordinal_5class_gen0_f1: 0.82
729	    ordinal_5class_gen1_f1: 0.56
730	    ordinal_5class_gen2_f1: 0.42
731	    ordinal_5class_gen3_f1: 0.38
732	    ordinal_5class_gen4_f1: 0.37
733	    adjacent_confusion_rate: 0.68
734	    gen2_gen3_gen4_pairwise_f1: 0.41
735	    ordinal_mae: 0.72
736	  result_rationale: '5-class macro-F1 大幅低于 3-class（0.51 vs 0.68），下降集中在 gen-2/gen-3/gen-4
737	    的 互相混淆（pairwise F1 仅 0.41）。gen-0 仍然清晰（0.82），gen-1 尚可（0.56）， 但 gen-2 以上的分辨率急剧恶化——与
738	    plan_001 的 H1/H2 trend 分析一致：drift rate 在 depth 2+ 递减，相邻深度的 feature 分布重叠严重。Adjacent
739	    confusion（误分类到 相邻深度）占全部错误的 68%，说明模型保留了 ordinal 结构但精度不够。这支持 "3-class 是 practical
740	    sweet spot" 的结论：gen-0/gen-1/gen-2+ 已经接近 information-theoretic ceiling for these
741	    features。
742	
743	    '
744	  tables:
745	  - name: 'Table 15: 5-class Ordinal Classification'
746	    columns:
747	    - class
748	    - precision
749	    - recall
750	    - f1
751	    rows:
752	    - - gen-0
753	      - 0.85
754	      - 0.79
755	      - 0.82
756	    - - gen-1
757	      - 0.52
758	      - 0.61
759	      - 0.56
760	    - - gen-2
761	      - 0.4
762	      - 0.44
763	      - 0.42
764	    - - gen-3
765	      - 0.36
766	      - 0.4
767	      - 0.38
768	    - - gen-4
769	      - 0.35
770	      - 0.39
771	      - 0.37
772	  - name: 'Table 16: Granularity Comparison'
773	    columns:
774	    - n_classes
775	    - macro_f1
776	    - ordinal_mae
777	    - chance_baseline
778	    rows:
779	    - - 2 (gen-0 vs gen-1+)
780	      - 0.79
781	      - 0.15
782	      - 0.5
783	    - - 3 (gen-0/gen-1/gen-2+)
784	      - 0.68
785	      - 0.38
786	      - 0.33
787	    - - 5 (gen-0 through gen-4)
788	      - 0.51
789	      - 0.72
790	      - 0.2
791	  figures_description:
792	  - 'Fig 9: 5×5 confusion matrix heatmap. Strong diagonal for gen-0, diffuse block
793	    for gen-2/3/4.'
794	  analysis: '回应 RC3（why 3-class?）。5-class 结果展示了 diminishing returns：每增加一个 class bin，macro-F1
795	    下降 ~9 点。Paper 应将 5-class 结果放在 appendix 作为 "depth resolution ceiling analysis"，主文保持
796	    3-class。
797	
798	    '
799	- name: human_edit_robustness
800	  plan_id: plan_010
801	  description: 'Robustness to simulated human edits. (A) Random word replacement at
802	    5/10/20%. (B) LLM-simulated light rephrasing.
803	
804	    '
805	  expected_results:
806	    baseline_no_edit_macro_f1: 0.68
807	    random_5pct_macro_f1: 0.65
808	    random_10pct_macro_f1: 0.59
809	    random_20pct_macro_f1: 0.51
810	    llm_light_rephrase_macro_f1: 0.57
811	    random_5pct_gen0_f1: 0.81
812	    random_20pct_gen0_f1: 0.68
813	    llm_rephrase_gen0_f1: 0.73
814	  result_rationale: 'Random word replacement 直接破坏了两类特征：替换词改变了 vocabulary stats（hapax_ratio,
815	    TTR）和 token-level entropy（replaced token 的 reference-model probability 不再反映 generator
816	    分布）。5% replacement 影响有限（-3 F1），因为大部分文本的 distributional fingerprint 完好。10% 开始显著退化（-9），20%
817	    接近 chance + 18 F1 点（0.51）， depth signal 大部分被噪声掩盖。LLM-simulated editing（0.57）比
818	    10% random（0.59） 略差，因为 LLM rephrasing 有针对性地修改了表面不自然的表述——正是 depth signal 最强 的位置。但它比
819	    20% random 好得多，因为 LLM editing 只修改少数句子（等效 replacement rate ~8-12%），不会大面积破坏统计量。
820	
821	    '
822	  tables:
823	  - name: 'Table 17: Robustness to Human Edits'
824	    columns:
825	    - edit_type
826	    - edit_rate
827	    - macro_f1
828	    - delta_from_baseline
829	    rows:
830	    - - none (baseline)
831	      - 0%
832	      - 0.68
833	      - —
834	    - - random replacement
835	      - 5%
836	      - 0.65
837	      - -0.03
838	    - - random replacement
839	      - 10%
840	      - 0.59
841	      - -0.09
842	    - - random replacement
843	      - 20%
844	      - 0.51
845	      - -0.17
846	    - - LLM light rephrase
847	      - ~10%
848	      - 0.57
849	      - -0.11
850	  figures_description:
851	  - 'Fig 10: Degradation curve — edit rate (x) vs macro-F1 (y). Approximately linear
852	    degradation for random; LLM rephrase annotated as single point above the random-10%
853	    line.'
854	  analysis: '回应 RC5。结论：depth signal 对轻度编辑（5%）鲁棒，但重度编辑（20%）会大幅削弱。 Real-world human
855	    editing 通常在 5-15% 范围（light polishing），此时 depth signal 仍可用但需要 recalibrate threshold。Paper
856	    应诚实报告这一 limitation 并建议后续工作 开发 edit-robust features。
857	
858	    '
859	- name: ld_score_feature
860	  plan_id: plan_011
861	  description: 'Add LD-Score as additional character-level feature. Tests complementary
862	    signal at character granularity.
863	
864	    '
865	  expected_results:
866	    full_features_macro_f1: 0.83
867	    full_plus_ldscore_macro_f1: 0.84
868	    ldscore_only_macro_f1: 0.59
869	    ldscore_feature_importance_rank: 6
870	    ldscore_correlation_with_hapax: 0.72
871	  result_rationale: 'LD-Score 单独仅 0.59——character-level distributional signature 捕捉的
872	    depth signal 弱于 token-level features，因为 character distribution 受 tokenizer 和 language
873	    model 的间接影响，信号经过了一层额外的 compression。加入 full feature set 后仅提升 1 F1 点 （0.84），因为 LD-Score
874	    与 hapax_ratio 高度相关（r=0.72）——两者都在测量 "词汇多样性 降低"，只是粒度不同。Character-level 和 token-level
875	    捕捉到了同一现象的不同尺度投影。 Feature importance 排第 6（7 个原始特征 + 1 LD-Score 中），说明它提供了一些独立信息
876	    但远非关键。
877	
878	    '
879	  tables:
880	  - name: 'Table 18: LD-Score Feature Integration'
881	    columns:
882	    - feature_set
883	    - macro_f1
884	    - n_features
885	    rows:
886	    - - original full (7 features)
887	      - 0.83
888	      - 7
889	    - - full + LD-Score
890	      - 0.84
891	      - 8
892	    - - LD-Score only
893	      - 0.59
894	      - 1
895	  figures_description:
896	  - 'Fig S1 (appendix): Scatter plot of LD-Score vs hapax_ratio colored by depth.
897	    High correlation (r=0.72) with depth-dependent offset.'
898	  analysis: 'LD-Score 的 marginal contribution 不足以在 main paper 中单独讨论。建议放 appendix 或完全省略。如果需要，一句话提及
899	    "character-level features are largely redundant with token-level vocabulary statistics
900	    (r=0.72 with hapax_ratio)"。
901	
902	    '
903	- name: end_to_end_classifier
904	  plan_id: plan_012
905	  description: 'QLoRA fine-tuned Qwen3.5-0.8B for end-to-end depth classification.
906	    Compares learned representations vs handcrafted features.
907	
908	    '
909	  expected_results:
910	    qwen_qlora_cross_gen_macro_f1: 0.74
911	    handcrafted_cross_gen_macro_f1: 0.68
912	    qwen_qlora_in_distribution_macro_f1: 0.88
913	    handcrafted_in_distribution_macro_f1: 0.81
914	    qwen_qlora_gen0_f1: 0.88
915	    qwen_qlora_gen1_f1: 0.68
916	    qwen_qlora_gen2plus_f1: 0.66
917	    qwen_qlora_training_hours: 12
918	    qwen_qlora_inference_ms_per_sample: 45
919	    handcrafted_inference_ms_per_sample: 3
920	  result_rationale: 'End-to-end model 在 cross-generator 设置下优于 handcrafted features
921	    6 F1 点（0.74 vs 0.68）——learned representations 能捕捉 handcrafted features 遗漏的 depth-dependent
922	    patterns（如句法复杂度下降、discourse coherence 退化、特定 n-gram 频率异常）。但优势 不是压倒性的，因为 handcrafted
923	    features 已经抓住了主要信号（vocabulary + distributional drift）。In-distribution 优势更大（0.88
924	    vs 0.81），但这部分可能是 overfitting to generator-specific patterns。关键 trade-off：handcrafted
925	    features 的 inference 速度 快 15 倍（3ms vs 45ms/sample），在大规模 data curation 中可能更 practical。Paper
926	    中 end-to-end 结果作为 "upper bound" 呈现，说明 learned features 还有 headroom，但 handcrafted
927	    features 的 interpretability 和 efficiency 是独立优势。
928	
929	    '
930	  tables:
931	  - name: 'Table 19: Handcrafted vs End-to-End'
932	    columns:
933	    - method
934	    - cross_gen_macro_f1
935	    - in_dist_macro_f1
936	    - inference_ms
937	    - interpretable
938	    rows:
939	    - - Handcrafted (XGBoost)
940	      - 0.68
941	      - 0.81
942	      - 3
943	      - 'yes'
944	    - - QLoRA Qwen3.5-0.8B
945	      - 0.74
946	      - 0.88
947	      - 45
948	      - 'no'
949	  figures_description:
950	  - 'Fig S2 (appendix): Attention heatmap from QLoRA model on representative gen-0/gen-2/gen-4
951	    samples. Shows model attends to low-frequency tokens and sentence boundaries —
952	    aligns with vocabulary depletion hypothesis.'
953	  analysis: End-to-end 结果为论文提供了两个用途：(1) 证明 depth signal 不局限于 handcrafted features
954	    的 7 维空间——learned representations 能发掘更多信号；(2) 但 6 F1 的 gap 说明 handcrafted features
955	    已经是 "good enough" 的 efficient alternative。Paper positioning：handcrafted approach
956	    是 contribution，end-to-end 是 validation + future direction。
957	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1643f296-adba-43d2-90c8-a089148637a8",
  "isSidechain": true,
  "promptId": "4853647d-0304-42ff-bb28-2931a50b53eb",
  "agentId": "aae1c9af8c0574a94",
  "type": "user",
  "uuid": "6c7c4b81-b11d-4ace-9ace-ca1dc6c20e8b",
  "sourceToolAssistantUUID": "1643f296-adba-43d2-90c8-a089148637a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-14T18:51:31.274Z_



Now let me submit the review via the appropriate tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c7c4b81-b11d-4ace-9ace-ca1dc6c20e8b",
  "isSidechain": true,
  "agentId": "aae1c9af8c0574a94",
  "requestId": "req_011Cb2xv97n5EQpHBrCSeA5Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1aee5d9b-eb3f-4fbe-8042-0bbf2189e4e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NAosQD2znQCyzeuoiCJhL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 40345,
      "cache_read_input_tokens": 14918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 40345,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 10 · 2026-05-14T18:51:31.576Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WfZWKpTpLcsWfCHNyER78x`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1aee5d9b-eb3f-4fbe-8042-0bbf2189e4e0",
  "isSidechain": true,
  "agentId": "aae1c9af8c0574a94",
  "requestId": "req_011Cb2xv97n5EQpHBrCSeA5Q",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "349b5724-3405-4f2e-9074-1aae6877f9f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NAosQD2znQCyzeuoiCJhL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 40345,
      "cache_read_input_tokens": 14918,
      "output_tokens": 102,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 40345
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 102,
          "cache_read_input_tokens": 14918,
          "cache_creation_input_tokens": 40345,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 40345,
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

_source line 11 · 2026-05-14T18:51:31.578Z_

<details><summary>↩ Tool result · `toolu_01WfZWKpTpLcsWfCHNyER78x`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "349b5724-3405-4f2e-9074-1aae6877f9f6",
  "isSidechain": true,
  "promptId": "4853647d-0304-42ff-bb28-2931a50b53eb",
  "agentId": "aae1c9af8c0574a94",
  "type": "user",
  "uuid": "ba8c5642-9310-4836-ad10-3039f5c44e98",
  "sourceToolAssistantUUID": "349b5724-3405-4f2e-9074-1aae6877f9f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-14T18:51:35.900Z_



Now I have carefully read every page of the paper and the full experiment context YAML. Let me compose the review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba8c5642-9310-4836-ad10-3039f5c44e98",
  "isSidechain": true,
  "agentId": "aae1c9af8c0574a94",
  "requestId": "req_011Cb2xvXbtDbUkor2kafvEa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "242b8f94-7f33-4cba-8e93-5cfc5c31ae3d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZV8RwQBdRssTLT4ftoAoz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 55263,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 683,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 13 · 2026-05-14T18:53:26.252Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_dream_review_report · `toolu_01UZT6pHwkGx3WqMRxGsqzfP`</summary>

```json
{
  "report": "\n# Review Report — R2: Novelty and Related Work\n\n## Reviewer: R2 (Novelty + Related Work Focus)\n## Paper: \"Distributional Fingerprints of Recursive LLM Generation: Depth Estimation via Complementary Multi-View Features\"\n\n---\n\n### Summary\n\nThis paper introduces \"generation depth estimation\" — classifying text as human-written (gen-0), first-generation synthetic (gen-1), or multi-hop synthetic (gen-2+) — using seven handcrafted features (five reference-model entropy statistics plus two surface vocabulary statistics) fed into XGBoost. The authors evaluate across five generators, four domains, multiple chain types, and compare against an end-to-end QLoRA baseline, finding that the binary gen-0 vs. gen-1+ task is the most reliable discriminative boundary (F1 0.79 cross-generator) while finer ordinal depth yields diminishing returns. A downstream filtering experiment suggests depth-aware curation offers modest Pareto improvements over binary synthetic text detectors.\n\n---\n\n### Strengths\n\n- **[S1] Well-scoped problem formulation.** Framing depth estimation as an ordinal classification task beyond binary detection is a legitimate and timely research question, given increasing concern about recursive contamination of web corpora. The problem is well-motivated by the data curation use case.\n\n- **[S2] Thorough experimental coverage.** The paper covers an impressive breadth of ablations: feature ablation, cross-generator generalization, cross-family reference models, multiple prompt types, paraphrastic vs. continuation chains, cross-model chains, four domains, 5-class ordinal, robustness to edits, LD-Score integration, and end-to-end comparison. For a paper of this scope, the experimental matrix is admirably complete and shows intellectual honesty (e.g., reporting the 12-point cross-generator degradation, the modest 1.8% downstream advantage, the 5-class collapse to 0.51).\n\n- **[S3] Honest claim calibration.** The paper avoids overclaiming. The downstream utility is described as \"suggestive rather than definitive,\" cross-generator degradation is reported transparently, and the authors explicitly frame binary depth as the primary practical contribution with ordinal depth as secondary. This calibration is appreciated.\n\n- **[S4] Complementary feature analysis is well-executed.** The error-set overlap analysis (~30%), the McNemar tests, and the prompt-type-dependent feature importance shifts provide genuine evidence for the \"complementary multi-view\" framing. The failure-mode analysis (Section 5.10) explaining when each feature family rescues the other adds interpretive depth.\n\n- **[S5] Paraphrastic vs. continuation chain comparison.** The H1/H2 hypothesis testing with paraphrastic chains as a control is a nice experimental design that connects to the Briesch et al. attractor cycle theory and adds theoretical grounding.\n\n---\n\n### Weaknesses\n\n- **[W1] Limited methodological novelty — features are off-the-shelf.** The seven features (entropy statistics, TTR, hapax ratio) are standard NLP/information-theoretic features that have been used in authorship attribution, readability estimation, and synthetic text detection for years. Token-level entropy under a reference model is the backbone of DetectGPT/FastDetectGPT. TTR and hapax ratio are textbook corpus linguistics measures. The \"tail decay\" feature (exponential fit to top-k probability mass) is the most distinctive, but even this is a straightforward statistical summary. There is no novel feature engineering, no new algorithm, no new theoretical framework — the contribution is applying known features to a new (admittedly interesting) classification target. For AAAI, I would expect at least one genuinely novel methodological component.\n\n- **[W2] The \"complementary multi-view\" framing overstates what is essentially feature concatenation.** Combining reference features and surface features is simply concatenating two feature groups and training a classifier on the union. Calling this \"complementary multi-view signal\" and listing it as a standalone contribution (Contribution 2) inflates a routine ML practice. Multi-view learning typically involves principled methods (CCA, co-training, multi-kernel learning, contrastive multi-view objectives). Here, concatenation + XGBoost is the entire \"method.\" The McNemar analysis showing the combination outperforms individual views is expected when features capture different aspects — this is not a surprising finding.\n\n- **[W3] H1/H2 hypothesis framing dresses up a predictable observation in formal language.** That non-paraphrastic generation chains diverge while paraphrastic chains converge is almost definitional. Paraphrasing chains are constrained to preserve semantics, so they must converge (Briesch et al. already proved this). Open-ended continuation has no such constraint, so drift accumulates. Presenting this as a \"competing hypothesis\" that requires experimental verification overstates the theoretical contribution. The paper does not provide a formal model of why H2 holds — it merely observes monotonic feature trends, which could be predicted from first principles.\n\n- **[W4] Related work coverage has significant gaps.** Several important lines of work are missing (detailed in Related Work Gap Analysis below). The related work section is only half a page — far too short for a paper that positions itself at the intersection of synthetic text detection, model collapse, and data provenance. The paper cites only 5 references total, which is extremely thin for an AAAI submission.\n\n- **[W5] The downstream utility claim (Contribution 3) is weak and potentially not significant.** The 1.8% PPL improvement over FastDetectGPT is based on a single fine-tuning run with no reported confidence intervals or significance test. The authors themselves note \"single fine-tuning run variance may account for part of the gap.\" A contribution that the authors cannot confirm is statistically significant should not be listed as one of three main contributions. The Pareto trade-off argument (higher retention at comparable quality) is more compelling but is also not rigorously established — there is no Pareto frontier analysis with multiple operating points.\n\n- **[W6] Ecological validity concerns remain despite cross-model chains.** Real-world recursive generation rarely follows the clean chain structure assumed here (same prompt type, same text length, sequential single-model or round-robin multi-model). In practice, text gets partially quoted, edited, summarized, expanded by different models with different prompts, mixed with human-written text, etc. The \"cross-model chain\" experiment (Section 5.6) addresses one dimension of this but the overall setup remains synthetic. The 5-point degradation from single-model to cross-model chains suggests further degradation under truly realistic conditions.\n\n- **[W7] Generator scale is limited.** All five generators are <= 2.8B parameters. The Limitations section acknowledges this, but it is a serious concern for a 2027 submission. Frontier models (70B+, GPT-4-class) produce text with very different distributional characteristics — their outputs are much closer to human distributions, likely compressing the depth signal severely. Without even one experiment on a model >7B, the generalizability claim is substantially weakened.\n\n---\n\n### Questions for Authors\n\n1. Have you tested whether a simple perplexity threshold (Pythia-410M PPL with a single cutoff) achieves comparable 3-class performance to your 7-feature XGBoost? Given the strong monotonic PPL-depth relationship (Table 3 in the paper / Table 3 in the context), this simpler baseline seems important to rule out.\n\n2. The \"complementary multi-view\" claim rests heavily on the ~30% error overlap statistic. How stable is this number across different generators and domains? If it varies substantially (e.g., 50% overlap for some generators), the complementarity claim would be weaker.\n\n3. For the downstream utility experiment (Table 7), how many random seeds were used for the fine-tuning runs? Without multiple seeds, the 1.8% advantage could easily be within noise.\n\n4. The reference model (Pythia-410M) is from the same family as 2 of 5 generators. How do you disentangle \"depth signal\" from \"architecture familiarity signal\"? The cross-family reference experiment (Table 5) shows a 6-point gap, suggesting architecture match matters substantially.\n\n5. Have you considered that hapax ratio and TTR are trivially length-dependent? If generation chains produce texts of systematically different lengths, your surface features may be measuring length rather than depth. What are the length distributions by depth?\n\n6. What happens with temperature/top-p variations at generation time? All experiments appear to use a single decoding configuration. The depth signal might vanish under high-temperature sampling that maintains lexical diversity.\n\n---\n\n### Related Work Gap Analysis\n\nThe paper cites only **5 references**, which is far below the norm for AAAI (typically 30-50). Critical missing lines of work:\n\n1. **Membership inference attacks** (Shokri et al., 2017; Carlini et al., 2021; Shi et al., \"Detecting Pretraining Data from Large Language Models,\" 2024). The paper mentions membership inference in one sentence but cites no specific work. Depth estimation can be viewed as a generalization of membership inference (was this text in the training data vs. how far removed is it from original training data).\n\n2. **Dataset contamination detection** (Golchin & Surdeanu, 2023; Oren et al., 2024; Deng et al., 2024). Highly relevant — detecting whether benchmark data leaked into training sets via recursive generation chains.\n\n3. **LLM fingerprinting and source attribution** (Tay et al., 2020; Li et al., \"Origin Tracing and Detecting of LLMs,\" 2024; Zhao et al., \"Provenance of LLM-generated text,\" 2024). The paper's data provenance paragraph is too vague. There is a growing literature on attributing generated text to specific models, which directly relates to depth estimation (depth = number of attribution hops).\n\n4. **Model collapse — additional key references.** Beyond Shumailov et al. and Briesch et al., the paper should cite: Alemohammad et al. (\"Self-Consuming Generative Models Go MAD,\" ICLR 2024); Dohmatob et al. (\"A Tale of Tails,\" 2024); Guo et al. (\"Curious Decline of Linguistic Diversity,\" 2024). These works study the same distributional narrowing phenomenon that underpins the depth signal.\n\n5. **Watermarking literature** — mentioned only in passing (\"SynthID-Text\") with no citation. Should cite Kirchenbauer et al. (2023), Zhao et al. (2024), Christ et al. (2024). Watermarking is the most direct competitor for depth-aware provenance: if you can watermark each generation step, you get exact depth for free.\n\n6. **Zero-shot detection beyond DetectGPT** — DNA-GPT (Yang et al., 2024), Binoculars (Hans et al., 2024), GLTR (Gehrmann et al., 2019). These are closely related baselines that should be discussed and ideally compared against.\n\n7. **Multi-class / ordinal synthetic text detection.** The paper claims depth estimation is \"unexplored,\" but Kumarage et al. (\"Stylometric Detection of AI-Generated Text in Twitter Timelines,\" 2023) and others have studied multi-class settings distinguishing different generators or generation conditions. While not exactly depth estimation, the claim of complete novelty needs nuancing.\n\n8. **Vocabulary diversity decline in LLM outputs** — Guo et al. (\"Curious Decline,\" 2024), Padmakumar & He (2024). These directly study the hapax/TTR decline phenomenon that is the paper's primary surface feature signal. Not citing them makes the surface feature motivation seem less grounded.\n\n---\n\n### Novelty Assessment\n\n**What is genuinely new:**\n- The specific problem formulation of \"generation depth estimation\" as ordinal classification (gen-0/gen-1/gen-2+) is new and well-motivated. Prior work has not explicitly framed this as a classification task with depth labels.\n- The systematic comparison of paraphrastic vs. non-paraphrastic chain dynamics, connecting to attractor cycle theory, has modest novelty.\n- The multi-domain, multi-generator, multi-prompt-type experimental matrix is more comprehensive than prior model collapse studies.\n\n**What is incremental:**\n- The \"complementary multi-view\" finding is feature concatenation. The specific complementarity between vocabulary stats and entropy stats is an empirical observation, not a methodological contribution.\n- The downstream filtering experiment demonstrates a use case but with marginal and potentially insignificant improvements.\n\n**What is straightforward application of existing tools:**\n- All seven features are standard. Entropy statistics under a reference model are the foundation of DetectGPT-family methods. TTR and hapax ratio are textbook corpus linguistics measures used since the 1930s (Zipf, 1935).\n- XGBoost on handcrafted features is a standard classification pipeline.\n- The reference model setup (computing token-level log-probabilities under a held-out model) is identical to what DetectGPT, FastDetectGPT, and related methods do.\n\n**Overall novelty verdict:** The problem formulation is the primary novel contribution, and it is a legitimate one. However, the methodology to solve that problem is entirely composed of existing, well-known components. For AAAI, this puts the paper in a difficult position: the problem is new and interesting, but the solution is engineering rather than science. The paper reads more as a thorough empirical study / benchmark paper than as a methods paper. Such papers can be accepted at AAAI, but they need to be exceptionally thorough and provide definitive answers — and the modest performance numbers (0.68 cross-generator F1 for 3-class, 0.51 for 5-class) suggest the problem remains far from solved even with the proposed approach.\n\n---\n\n### Minor Issues\n\n- The paper has only 5 references. This is unacceptable for a top venue submission. A thorough related work section should cite 30+ relevant works.\n- SynthID-Text is mentioned but not cited (no reference number).\n- Section 3.3 defines \"tail decay\" as \"fitted exponential decay rate\" but does not specify the fitting procedure (which top-k? exponential vs. power law? fitting method?). This hurts reproducibility.\n- The paper uses \"MVP dataset\" (Section 5.1) without defining the acronym.\n- Table numbering in the paper (Tables 1-14) does not match the experiment context YAML (Tables 1-19), suggesting some experiments from the design were dropped or consolidated. The paper should acknowledge this if certain planned experiments were excluded.\n- The abstract claims \"five generators and four text domains\" but the per-domain results (Table 11) appear to be aggregate across generators — it is unclear whether all 5 generators x 4 domains x 5 depths = 100 conditions were fully crossed.\n- No error bars or confidence intervals on the main results (Table 1, Table 3). For a classification paper, bootstrap CIs on F1 should be standard.\n\n---\n\n### Preliminary Rating\n\n- **Overall: 5/10** — Marginally below the acceptance threshold. The problem formulation is interesting and timely, and the experimental breadth is commendable. However, the methodological novelty is insufficient for AAAI: the features are off-the-shelf, the classifier is standard, and the theoretical contributions (H1/H2, complementary views) are either predictable or overstated. The related work is severely underdeveloped (5 citations). The downstream utility claim is not statistically validated. The paper would benefit from either (a) a genuinely novel detection method that substantially outperforms the baseline features, or (b) repositioning as a benchmark/dataset paper with released artifacts. In its current form, this is a solid workshop paper or a borderline short paper, but does not meet the novelty bar for a full AAAI paper.\n\n- **Novelty: 2/5** — The problem formulation is new; the methodology is not. Features, classifier, and evaluation protocol are all standard. The H1/H2 framing adds minimal theoretical novelty beyond what is already known from Briesch et al.\n\n- **Significance: 3/5** — The problem matters. Data curation in the era of recursive LLM contamination is a real concern. But the solution's practical impact is limited by modest cross-generator performance (0.68 F1), severe degradation at finer granularities (0.51 for 5-class), and an unvalidated downstream advantage (1.8% PPL, possibly not significant).\n\n- **Confidence: 4/5** — I am familiar with the synthetic text detection, model collapse, and data provenance literatures. I have read the paper thoroughly including all tables and claims. My main uncertainty is whether the AAAI community would weigh the problem formulation novelty more heavily than I have.\n",
  "project": "gen-depth-fingerprint",
  "tier": "median",
  "dream_id": "dream_20260514T181213",
  "overall_score": "marginally below accept (5/10)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "242b8f94-7f33-4cba-8e93-5cfc5c31ae3d",
  "isSidechain": true,
  "agentId": "aae1c9af8c0574a94",
  "requestId": "req_011Cb2xvXbtDbUkor2kafvEa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9475fe8-076c-48f9-a458-030c655ca5be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JZV8RwQBdRssTLT4ftoAoz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 683,
      "cache_read_input_tokens": 55263,
      "output_tokens": 4154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 683
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4154,
          "cache_read_input_tokens": 55263,
          "cache_creation_input_tokens": 683,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 683,
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

_source line 14 · 2026-05-14T18:53:27.005Z_

<details><summary>↩ Tool result · `toolu_01UZT6pHwkGx3WqMRxGsqzfP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"report_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/review_report.md\", \"dream_id\": \"dream_20260514T181213\", \"tier\": \"median\", \"review_visible\": true}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9475fe8-076c-48f9-a458-030c655ca5be",
  "isSidechain": true,
  "promptId": "4853647d-0304-42ff-bb28-2931a50b53eb",
  "agentId": "aae1c9af8c0574a94",
  "type": "user",
  "uuid": "c59df03d-a8d2-4f90-853b-4ac4b331217b",
  "sourceToolAssistantUUID": "d9475fe8-076c-48f9-a458-030c655ca5be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-14T18:53:36.774Z_

Review submitted successfully. Here is a summary of the key findings:

**Rating: 5/10 (marginally below AAAI acceptance threshold)**

**Core tension:** The problem formulation (generation depth estimation) is genuinely new and well-motivated, but the methodology is entirely composed of standard components -- off-the-shelf features (entropy stats, TTR, hapax ratio), a standard XGBoost classifier, and a standard reference-model setup identical to DetectGPT-family methods. For AAAI's ~17.6% acceptance rate, this novelty gap is the primary concern.

**Main weaknesses identified:**
- 7 features are all textbook NLP/information-theoretic measures with no algorithmic innovation
- "Complementary multi-view" framing overstates what is simply feature concatenation
- H1/H2 hypothesis testing formalizes a predictable observation (unconstrained chains diverge; constrained ones converge)
- Only 5 references cited -- severely underdeveloped related work missing membership inference, dataset contamination, LLM fingerprinting, watermarking, and additional model collapse literature
- Downstream utility claim (1.8% PPL improvement) lacks statistical validation
- All generators are <=2.8B parameters; no frontier-scale evaluation

**Main strengths:**
- Legitimate and timely problem formulation
- Exceptionally thorough experimental matrix (5 generators, 4 domains, 3 chain types, multiple granularities)
- Honest claim calibration throughout
- Well-executed complementarity analysis with error-set overlap and failure-mode dissection

Report saved to: `/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/dream_reports/dream_20260514T181213/median/review_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c59df03d-a8d2-4f90-853b-4ac4b331217b",
  "isSidechain": true,
  "agentId": "aae1c9af8c0574a94",
  "requestId": "req_011Cb2y52c7iFpUcu4r975R2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "57d0f94b-f8e9-4b6a-8bed-654010c4b014",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "sessionId": "9b2e420c-51b0-42b5-b9d0-dc8ee4113295",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gQzPKhxJeYjgzJ5PKpij6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4284,
      "cache_read_input_tokens": 55946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4284,
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
