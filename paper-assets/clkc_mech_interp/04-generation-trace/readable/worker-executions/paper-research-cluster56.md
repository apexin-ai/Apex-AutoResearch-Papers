# paper research cluster56

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/workers/worker_paper_research_cluster56_20260522T140502.log`
- **Structured JSON:** [`790340def8945a18c786.json`](../../sessions/79/790340def8945a18c786.json)

## Before a recorded user message

59 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
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
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_figures_and_layout",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "c059bc03-cab5-4a63-98d3-6b40b72f9787",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod42-projects-clkc-mech-interp/memory/"
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
    "resetsAt": 1779475200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "1031b43e-e6ad-4272-afdd-317fa6bcc212",
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1"
}
```

---

### Assistant

_source line 4_

I'll search for the missing papers across both clusters in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "38a6d7a4-8d1e-48b0-a960-e95bd6f14ba4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvBDyMmbaqn7e99GSgUgTB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12939,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12939
      },
      "output_tokens": 4,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Es53DXxhkpHgsDBVcATx8Q`</summary>

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
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "a0b6c912-1ead-4401-a469-3cf6476fa6cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BvBDyMmbaqn7e99GSgUgTB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12939,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12939
      },
      "output_tokens": 4,
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

_source line 6 · 2026-05-22T14:05:15.040Z_

<details><summary>↩ Tool result · `toolu_01Es53DXxhkpHgsDBVcATx8Q`</summary>

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
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "def3e250-b1d9-4b95-857b-0219f295f19d",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 51
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me start by searching for all the must-cite papers in parallel, plus reading the current literature_map.yaml.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "727286bd-f3b7-4fc1-9677-4fb317572af7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZ4zncjGF6wjByBG5S36hU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 24780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 617
      },
      "output_tokens": 24,
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

_source line 8_

Let me search for all the required papers and read the current literature map in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "5693f0cc-871d-4e32-9a68-4077c341d99e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZ4zncjGF6wjByBG5S36hU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 24780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 617
      },
      "output_tokens": 24,
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

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0183HxPS9WRfRrC184eNYcM8`</summary>

```json
{
  "query": "Li et al 2024 \"Inference-Time Intervention\" truthful LLM activation addition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "e427b05c-2346-440b-b85a-c6c973a42cde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZ4zncjGF6wjByBG5S36hU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 24780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 617
      },
      "output_tokens": 24,
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

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vx3HvbBK35TxGejvyhTVWC`</summary>

```json
{
  "query": "Zou et al 2023 \"Representation Engineering: A Top-Down Approach to AI Transparency\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "40236609-eaee-4396-aa21-163d9d4b95eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZ4zncjGF6wjByBG5S36hU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 24780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 617
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ryitoxd62cs2mqsp3V4ZNw`</summary>

```json
{
  "query": "XNLI cross-lingual natural language inference Conneau et al 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "80f653a9-0bd3-4231-88bc-eaa8b5bc6306",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZ4zncjGF6wjByBG5S36hU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 24780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 617
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GAh2iJ1izoHTpsKSqVrfXK`</summary>

```json
{
  "query": "COMET translation evaluation metric Rei et al 2020 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "26812349-e121-4938-b091-f68ea8369c5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZ4zncjGF6wjByBG5S36hU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 24780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 617
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_016QoVmroRRwQjmzBpQ2BXVq`</summary>

```json
{
  "query": "Llama 3.1 technical report Meta 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "c4896af1-5e47-43bf-b690-296861a32de0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZ4zncjGF6wjByBG5S36hU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 24780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 617
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — Read · `toolu_01LaMhrWWYMjS1QanbBefD6i`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "45691015-6fce-4764-acb5-90858c41ec58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UZ4zncjGF6wjByBG5S36hU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 24780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 617
      },
      "output_tokens": 24,
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

_source line 15 · 2026-05-22T14:05:21.007Z_

<details><summary>↩ Tool result · `toolu_01LaMhrWWYMjS1QanbBefD6i`</summary>

```text
1	categories: []
2	meta:
3	  last_updated: '2026-05-22T14:30:00Z'
4	  total_papers: 22
5	papers:
6	  basu2026interpretability:
7	    abstract: ''
8	    added_at: '2026-05-21T12:04:50.273Z'
9	    added_by: director-bootstrap
10	    authors:
11	    - Basu, S.
12	    - et al.
13	    bibtex_key: basu2026interpretability
14	    category: sae-steering
15	    doi: ''
16	    relevance: 'SAE steering failure in clinical triage despite 98.2% AUROC probes.
17	      Critical negative result: defines boundary conditions for when SAE steering
18	      works. Our Track 3 design addresses their methodological gaps.'
19	    role: direct-competitor
20	    semantic_scholar_id: ''
21	    title: 'Interpretability without actionability: mechanistic methods cannot correct
22	      language model errors despite near-perfect internal representations'
23	    url: https://arxiv.org/abs/2603.18353
24	    venue: arXiv
25	    verified: true
26	    year: 2026
27	  boer2026probing:
28	    abstract: ''
29	    added_at: '2026-05-21T12:04:50.273Z'
30	    added_by: director-bootstrap
31	    authors:
32	    - Boer, A.
33	    - Brink, I.
34	    - Ulmer, D.
35	    bibtex_key: boer2026probing
36	    category: probing
37	    doi: ''
38	    relevance: 0.96 Macro-F1 parametric-vs-contextual attribution probe on Llama/Mistral/Qwen.
39	      Monolingual performance ceiling for our Track 1. Cross-domain transfer 0.94-0.99
40	      F1.
41	    role: direct-competitor
42	    semantic_scholar_id: ''
43	    title: Probing for Knowledge Attribution in Large Language Models
44	    url: https://arxiv.org/abs/2602.22787
45	    venue: arXiv
46	    verified: true
47	    year: 2026
48	  ifergan2024beneath:
49	    added_at: '2026-05-22T14:00:00Z'
50	    added_by: paper-agent-lit-search
51	    authors:
52	    - Ifergan, M.
53	    - Choshen, L.
54	    - Aharoni, R.
55	    - Szpektor, I.
56	    - Abend, O.
57	    bibtex_key: ifergan2024beneath
58	    category: cross-lingual-conflict
59	    doi: ''
60	    relevance: Shows cross-lingual answer consistency does not imply shared representation;
61	      script similarity dominates sharing. Directly motivates our probing approach
62	      to test whether conflict signals share representations across languages.
63	    role: foundation
64	    title: 'Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge
65	      Representation Sharing in LLMs'
66	    url: https://arxiv.org/abs/2408.10646
67	    venue: Findings of NAACL 2025
68	    verified: true
69	    year: 2024
70	  kialy2026universal:
71	    abstract: ''
72	    added_at: '2026-05-21T12:04:50.273Z'
73	    added_by: director-bootstrap
74	    authors:
75	    - Kialy, U.Z.
76	    - Shtarkberg, A.
77	    - Klein, A.
78	    bibtex_key: kialy2026universal
79	    category: cross-lingual-sae
80	    doi: ''
81	    relevance: First cross-lingual SAE feature discovery. Shows cross-linguistic core
82	      for register features + zero-shot steering transfer. We test whether this extends
83	      to knowledge conflict features.
84	    role: direct-competitor
85	    semantic_scholar_id: ''
86	    title: A Universal Vibe? Finding and Controlling Language-Agnostic Informal Register
87	      with SAEs
88	    url: https://arxiv.org/abs/2603.26236
89	    venue: arXiv
90	    verified: true
91	    year: 2026
92	  li2025taming:
93	    added_at: '2026-05-22T14:00:00Z'
94	    added_by: paper-agent-lit-search
95	    authors:
96	    - Li, G.
97	    - Chen, Y.
98	    - Tong, H.
99	    bibtex_key: li2025taming
100	    category: knowledge-conflict
101	    doi: ''
102	    relevance: Proposes conflict resolution framework for LLMs. Provides resolution
103	      baselines our mechanistic approach complements.
104	    role: direct-competitor
105	    title: Taming Knowledge Conflicts in Language Models
106	    url: https://arxiv.org/abs/2503.10996
107	    venue: ICML 2025 (Spotlight)
108	    verified: true
109	    year: 2025
110	  pham2026where:
111	    abstract: ''
112	    added_at: '2026-05-21T12:04:50.273Z'
113	    added_by: director-bootstrap
114	    authors:
115	    - Pham, M.V.
116	    - Borkakoty, H.
117	    - Hou, Y.
118	    bibtex_key: pham2026where
119	    category: conflict-mechanism
120	    doi: ''
121	    relevance: Activation patching + CMAP for intra-memory conflicts. Attention layers
122	      21-47 dominate conflict resolution in Qwen3-4B. Closest methodological parallel
123	      for within-parametric conflicts.
124	    role: direct-competitor
125	    semantic_scholar_id: ''
126	    title: 'Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge
127	      Conflict in Language Models'
128	    url: https://arxiv.org/abs/2601.09445
129	    venue: arXiv
130	    verified: true
131	    year: 2026
132	  team2026qwen:
133	    abstract: ''
134	    added_at: '2026-05-21T12:04:50.273Z'
135	    added_by: director-bootstrap
136	    authors:
137	    - Qwen Team
138	    bibtex_key: team2026qwen
139	    category: sae-tools
140	    doi: ''
141	    relevance: Pretrained SAEs for Qwen3 family. Our Track 2 uses Qwen-Scope SAEs
142	      on Qwen3-8B-Base. Documents cross-lingual transfer for toxicity features (Section
143	      5.2).
144	    role: foundation
145	    semantic_scholar_id: ''
146	    title: 'Qwen-Scope: Turning Sparse Features into Development Tools for Large Language
147	      Models'
148	    url: https://arxiv.org/abs/2605.11887
149	    venue: arXiv
150	    verified: true
151	    year: 2026
152	  wang2025lost:
153	    abstract: ''
154	    added_at: '2026-05-21T12:04:50.273Z'
155	    added_by: director-bootstrap
156	    authors:
157	    - Wang, M.
158	    - Adel, H.
159	    - Lange, L.
160	    - et al.
161	    bibtex_key: wang2025lost
162	    category: cross-lingual-mechanism
163	    doi: ''
164	    relevance: Language-independent concept space through most layers, language-specific
165	      only in final layers. Key mechanistic finding our H1/H2 hypotheses build on.
166	    role: foundation
167	    semantic_scholar_id: ''
168	    title: 'Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency
169	      in Transformer Language Models'
170	    url: https://arxiv.org/abs/2504.04264
171	    venue: ACL 2025 (SAC Highlights)
172	    verified: true
173	    year: 2025
174	  wong2026langfir:
175	    abstract: ''
176	    added_at: '2026-05-21T12:04:50.273Z'
177	    added_by: director-bootstrap
178	    authors:
179	    - Wong, S.H.
180	    - Siddique, A.B.
181	    - Sajjad, H.
182	    bibtex_key: wong2026langfir
183	    category: cross-lingual-sae
184	    doi: ''
185	    relevance: Random-token filtering isolates <5 language-specific SAE features/language.
186	      Our Track 2 uses this as control to disentangle language-identity from conflict
187	      features.
188	    role: direct-competitor
189	    semantic_scholar_id: ''
190	    title: 'LangFIR: Discovering Sparse Language-Specific Features from Monolingual
191	      Data for Language Steering'
192	    url: https://arxiv.org/abs/2604.03532
193	    venue: arXiv
194	    verified: true
195	    year: 2026
196	  xie2024adaptive:
197	    added_at: '2026-05-22T14:00:00Z'
198	    added_by: paper-agent-lit-search
199	    authors:
200	    - Xie, J.
201	    - Zhang, K.
202	    - Chen, J.
203	    - Lou, R.
204	    - Su, Y.
205	    bibtex_key: xie2024adaptive
206	    category: knowledge-conflict
207	    doi: ''
208	    relevance: Introduces ConflictQA benchmark (PopQA + StrategyQA based) for studying
209	      LLM behavior under context-parametric knowledge conflicts. Our primary evaluation
210	      dataset.
211	    role: foundation
212	    title: 'Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large
213	      Language Models in Knowledge Conflicts'
214	    url: https://arxiv.org/abs/2305.13300
215	    venue: ICLR 2024
216	    verified: true
217	    year: 2024
218	  xing2024evaluating:
219	    added_at: '2026-05-22T14:00:00Z'
220	    added_by: paper-agent-lit-search
221	    authors:
222	    - Xing, X.
223	    - He, Z.
224	    - Xu, H.
225	    - Wang, X.
226	    - Wang, R.
227	    - Hong, Y.
228	    bibtex_key: xing2024evaluating
229	    category: cross-lingual-conflict
230	    doi: ''
231	    relevance: Proposes cross-lingual semantic/accuracy/timeliness consistency metrics
232	      (xSC, xAC, xTC) for evaluating multilingual LLM inconsistency. Provides evaluation
233	      methodology relevant to our cross-lingual conflict measurement.
234	    role: peripheral
235	    title: Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language
236	      Models
237	    url: https://arxiv.org/abs/2407.01358
238	    venue: arXiv
239	    verified: true
240	    year: 2024
241	  xu2024knowledge:
242	    added_at: '2026-05-22T14:00:00Z'
243	    added_by: paper-agent-lit-search
244	    authors:
245	    - Xu, R.
246	    - Qi, Z.
247	    - Guo, Z.
248	    - Wang, C.
249	    - Wang, H.
250	    - Zhang, Y.
251	    - Xu, W.
252	    bibtex_key: xu2024knowledge
253	    category: knowledge-conflict
254	    doi: ''
255	    relevance: Comprehensive survey of context-memory, inter-context, and intra-memory
256	      knowledge conflicts in LLMs. Defines the taxonomy our work builds on.
257	    role: foundation
258	    title: 'Knowledge Conflicts for LLMs: A Survey'
259	    url: https://arxiv.org/abs/2403.08319
260	    venue: EMNLP 2024
261	    verified: true
262	    year: 2024
263	  zhao2024analysing:
264	    abstract: ''
265	    added_at: '2026-05-21T12:04:50.273Z'
266	    added_by: director-bootstrap
267	    authors:
268	    - Zhao, Y.
269	    - Du, X.
270	    - Hong, G.
271	    - et al.
272	    bibtex_key: zhao2024analysing
273	    category: probing
274	    doi: ''
275	    relevance: 'Original conflict probing work: ~90% accuracy detecting conflicts
276	      in residual stream. Foundation for our Track 1 cross-lingual extension.'
277	    role: foundation
278	    semantic_scholar_id: ''
279	    title: Analysing the Residual Stream of Language Models Under Knowledge Conflicts
280	    url: https://arxiv.org/abs/2410.16090
281	    venue: NeurIPS 2024 FMI Workshop
282	    verified: true
283	    year: 2024
284	  zhao2025steering:
285	    abstract: ''
286	    added_at: '2026-05-21T12:04:50.273Z'
287	    added_by: director-bootstrap
288	    authors:
289	    - Zhao, Y.
290	    - Devoto, A.
291	    - Hong, G.
292	    - et al.
293	    bibtex_key: zhao2025steering
294	    category: sae-steering
295	    doi: ''
296	    relevance: 'SpARE: SAE-based conflict feature selection + steering. Core methodology
297	      we extend to cross-lingual setting. MI-based feature selection, constraint-aware
298	      activation editing.'
299	    role: direct-competitor
300	    semantic_scholar_id: ''
301	    title: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation
302	      Engineering
303	    url: https://arxiv.org/abs/2410.15999
304	    venue: NAACL 2025 Oral
305	    verified: true
306	    year: 2025
307	  zhao2026when:
308	    abstract: ''
309	    added_at: '2026-05-21T12:04:50.273Z'
310	    added_by: director-bootstrap
311	    authors:
312	    - Zhao, J.
313	    - et al.
314	    bibtex_key: zhao2026when
315	    category: cross-lingual-conflict
316	    doi: ''
317	    relevance: 'CLEAR benchmark: 10-language cross-lingual conflict evaluation. Behavioral
318	      finding that linguistic similarity governs entity-centric conflict resolution.
319	      Our work provides mechanistic explanation.'
320	    role: direct-competitor
321	    semantic_scholar_id: ''
322	    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'
323	    url: https://arxiv.org/abs/2601.07041
324	    venue: arXiv
325	    verified: true
326	    year: 2026
327	  wu2020emerging:
328	    added_at: '2026-05-22T14:30:00Z'
329	    added_by: paper-agent-lit-search
330	    authors:
331	    - Wu, S.
332	    - Conneau, A.
333	    - Li, H.
334	    - Zettlemoyer, L.
335	    - Stoyanov, V.
336	    bibtex_key: wu2020emerging
337	    category: cross-lingual-repr
338	    doi: 10.18653/v1/2020.acl-main.536
339	    relevance: Shows mid-layer cross-lingual alignment emerges from shared parameters
340	      alone; monolingual representations can be aligned post-hoc. Foundation for understanding
341	      language-agnostic concept space our probing hypotheses build on. MUST CITE.
342	    role: foundation
343	    title: Emerging Cross-lingual Structure in Pretrained Language Models
344	    url: https://aclanthology.org/2020.acl-main.536/
345	    venue: ACL 2020
346	    verified: true
347	    year: 2020
348	  wendler2024llamas:
349	    added_at: '2026-05-22T14:30:00Z'
350	    added_by: paper-agent-lit-search
351	    authors:
352	    - Wendler, C.
353	    - Veselovsky, V.
354	    - Monea, G.
355	    - West, R.
356	    bibtex_key: wendler2024llamas
357	    category: cross-lingual-repr
358	    doi: ''
359	    relevance: Demonstrates English-centric LLMs implicitly pivot through English representations
360	      in middle layers. Three-phase pattern (input language -> English pivot -> output
361	      language) supports hypothesis that conflict signals may route through English-aligned
362	      subspace.
363	    role: foundation
364	    title: 'Do Llamas Work in English? On the Latent Language of Multilingual Transformers'
365	    url: https://arxiv.org/abs/2402.10588
366	    venue: ACL 2024
367	    verified: true
368	    year: 2024
369	  muller2021first:
370	    added_at: '2026-05-22T14:30:00Z'
371	    added_by: paper-agent-lit-search
372	    authors:
373	    - Muller, B.
374	    - Elazar, Y.
375	    - Sagot, B.
376	    - Seddah, D.
377	    bibtex_key: muller2021first
378	    category: cross-lingual-repr
379	    doi: ''
380	    relevance: CKA-based layer-wise analysis showing mBERT decomposes into multilingual
381	      encoder + language-agnostic predictor. Representations first converge to language
382	      neutrality then recover language specificity. Methodological precedent for our
383	      layer-wise analysis.
384	    role: methodology
385	    title: 'First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual
386	      BERT'
387	    url: https://aclanthology.org/2021.eacl-main.189/
388	    venue: EACL 2021
389	    verified: true
390	    year: 2021
391	  kargaran2024mexa:
392	    added_at: '2026-05-22T14:30:00Z'
393	    added_by: paper-agent-lit-search
394	    authors:
395	    - Kargaran, A.H.
396	    - Modarressi, A.
397	    - Nikeghbal, N.
398	    - Diesner, J.
399	    - Yvon, F.
400	    - "Sch\xFCtze, H."
401	    bibtex_key: kargaran2024mexa
402	    category: cross-lingual-repr
403	    doi: ''
404	    relevance: Cross-lingual alignment metric leveraging English pivot hypothesis, 0.90
405	      Pearson correlation with downstream tasks. Provides evaluation methodology for
406	      measuring English-centric alignment relevant to our cross-lingual transfer analysis.
407	    role: methodology
408	    title: 'MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual
409	      Alignment'
410	    url: https://arxiv.org/abs/2410.05873
411	    venue: Findings of ACL 2025
412	    verified: true
413	    year: 2024
414	  belinkov2022probing:
415	    added_at: '2026-05-22T14:30:00Z'
416	    added_by: paper-agent-lit-search
417	    authors:
418	    - Belinkov, Y.
419	    bibtex_key: belinkov2022probing
420	    category: probing-methodology
421	    doi: ''
422	    relevance: Comprehensive survey of probing classifier promises, shortcomings, and
423	      advances. Defines the methodological framework our linear probes follow. MUST
424	      CITE for probing methodology justification.
425	    role: foundation
426	    title: 'Probing Classifiers: Promises, Shortcomings, and Advances'
427	    url: https://arxiv.org/abs/2102.12452
428	    venue: Computational Linguistics 48(1)
429	    verified: true
430	    year: 2022
431	  hewitt2019designing:
432	    added_at: '2026-05-22T14:30:00Z'
433	    added_by: paper-agent-lit-search
434	    authors:
435	    - Hewitt, J.
436	    - Liang, P.
437	    bibtex_key: hewitt2019designing
438	    category: probing-methodology
439	    doi: ''
440	    relevance: Introduces selectivity metric (linguistic accuracy - control accuracy)
441	      to distinguish genuine representation encoding from probe memorization. Our probing
442	      design uses control tasks following this framework. EMNLP 2019 Best Paper Runner
443	      Up.
444	    role: methodology
445	    title: Designing and Interpreting Probes with Control Tasks
446	    url: https://aclanthology.org/D19-1275/
447	    venue: EMNLP 2019
448	    verified: true
449	    year: 2019
450	  ulmer2022deep:
451	    added_at: '2026-05-22T14:30:00Z'
452	    added_by: paper-agent-lit-search
453	    authors:
454	    - Ulmer, D.
455	    - Hardmeier, C.
456	    - Frellsen, J.
457	    bibtex_key: ulmer2022deep
458	    category: probing-methodology
459	    doi: ''
460	    relevance: Bootstrap-based statistical testing framework for neural network comparisons,
461	      including Almost Stochastic Order (ASO). Provides the bootstrap CI methodology
462	      we use for probing accuracy significance testing.
463	    role: methodology
464	    title: 'deep-significance: Easy and Meaningful Statistical Significance Testing
465	      in the Age of Neural Networks'
466	    url: https://arxiv.org/abs/2204.06815
467	    venue: arXiv
468	    verified: true
469	    year: 2022
470	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "cd493d3e-b30c-45e4-8b3d-5ee9d2fb5299",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
      "content": "categories: []\nmeta:\n  last_updated: '2026-05-22T14:30:00Z'\n  total_papers: 22\npapers:\n  basu2026interpretability:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Basu, S.\n    - et al.\n    bibtex_key: basu2026interpretability\n    category: sae-steering\n    doi: ''\n    relevance: 'SAE steering failure in clinical triage despite 98.2% AUROC probes.\n      Critical negative result: defines boundary conditions for when SAE steering\n      works. Our Track 3 design addresses their methodological gaps.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Interpretability without actionability: mechanistic methods cannot correct\n      language model errors despite near-perfect internal representations'\n    url: https://arxiv.org/abs/2603.18353\n    venue: arXiv\n    verified: true\n    year: 2026\n  boer2026probing:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Boer, A.\n    - Brink, I.\n    - Ulmer, D.\n    bibtex_key: boer2026probing\n    category: probing\n    doi: ''\n    relevance: 0.96 Macro-F1 parametric-vs-contextual attribution probe on Llama/Mistral/Qwen.\n      Monolingual performance ceiling for our Track 1. Cross-domain transfer 0.94-0.99\n      F1.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: Probing for Knowledge Attribution in Large Language Models\n    url: https://arxiv.org/abs/2602.22787\n    venue: arXiv\n    verified: true\n    year: 2026\n  ifergan2024beneath:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Ifergan, M.\n    - Choshen, L.\n    - Aharoni, R.\n    - Szpektor, I.\n    - Abend, O.\n    bibtex_key: ifergan2024beneath\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: Shows cross-lingual answer consistency does not imply shared representation;\n      script similarity dominates sharing. Directly motivates our probing approach\n      to test whether conflict signals share representations across languages.\n    role: foundation\n    title: 'Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge\n      Representation Sharing in LLMs'\n    url: https://arxiv.org/abs/2408.10646\n    venue: Findings of NAACL 2025\n    verified: true\n    year: 2024\n  kialy2026universal:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Kialy, U.Z.\n    - Shtarkberg, A.\n    - Klein, A.\n    bibtex_key: kialy2026universal\n    category: cross-lingual-sae\n    doi: ''\n    relevance: First cross-lingual SAE feature discovery. Shows cross-linguistic core\n      for register features + zero-shot steering transfer. We test whether this extends\n      to knowledge conflict features.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: A Universal Vibe? Finding and Controlling Language-Agnostic Informal Register\n      with SAEs\n    url: https://arxiv.org/abs/2603.26236\n    venue: arXiv\n    verified: true\n    year: 2026\n  li2025taming:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Li, G.\n    - Chen, Y.\n    - Tong, H.\n    bibtex_key: li2025taming\n    category: knowledge-conflict\n    doi: ''\n    relevance: Proposes conflict resolution framework for LLMs. Provides resolution\n      baselines our mechanistic approach complements.\n    role: direct-competitor\n    title: Taming Knowledge Conflicts in Language Models\n    url: https://arxiv.org/abs/2503.10996\n    venue: ICML 2025 (Spotlight)\n    verified: true\n    year: 2025\n  pham2026where:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Pham, M.V.\n    - Borkakoty, H.\n    - Hou, Y.\n    bibtex_key: pham2026where\n    category: conflict-mechanism\n    doi: ''\n    relevance: Activation patching + CMAP for intra-memory conflicts. Attention layers\n      21-47 dominate conflict resolution in Qwen3-4B. Closest methodological parallel\n      for within-parametric conflicts.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge\n      Conflict in Language Models'\n    url: https://arxiv.org/abs/2601.09445\n    venue: arXiv\n    verified: true\n    year: 2026\n  team2026qwen:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Qwen Team\n    bibtex_key: team2026qwen\n    category: sae-tools\n    doi: ''\n    relevance: Pretrained SAEs for Qwen3 family. Our Track 2 uses Qwen-Scope SAEs\n      on Qwen3-8B-Base. Documents cross-lingual transfer for toxicity features (Section\n      5.2).\n    role: foundation\n    semantic_scholar_id: ''\n    title: 'Qwen-Scope: Turning Sparse Features into Development Tools for Large Language\n      Models'\n    url: https://arxiv.org/abs/2605.11887\n    venue: arXiv\n    verified: true\n    year: 2026\n  wang2025lost:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Wang, M.\n    - Adel, H.\n    - Lange, L.\n    - et al.\n    bibtex_key: wang2025lost\n    category: cross-lingual-mechanism\n    doi: ''\n    relevance: Language-independent concept space through most layers, language-specific\n      only in final layers. Key mechanistic finding our H1/H2 hypotheses build on.\n    role: foundation\n    semantic_scholar_id: ''\n    title: 'Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency\n      in Transformer Language Models'\n    url: https://arxiv.org/abs/2504.04264\n    venue: ACL 2025 (SAC Highlights)\n    verified: true\n    year: 2025\n  wong2026langfir:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Wong, S.H.\n    - Siddique, A.B.\n    - Sajjad, H.\n    bibtex_key: wong2026langfir\n    category: cross-lingual-sae\n    doi: ''\n    relevance: Random-token filtering isolates <5 language-specific SAE features/language.\n      Our Track 2 uses this as control to disentangle language-identity from conflict\n      features.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'LangFIR: Discovering Sparse Language-Specific Features from Monolingual\n      Data for Language Steering'\n    url: https://arxiv.org/abs/2604.03532\n    venue: arXiv\n    verified: true\n    year: 2026\n  xie2024adaptive:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xie, J.\n    - Zhang, K.\n    - Chen, J.\n    - Lou, R.\n    - Su, Y.\n    bibtex_key: xie2024adaptive\n    category: knowledge-conflict\n    doi: ''\n    relevance: Introduces ConflictQA benchmark (PopQA + StrategyQA based) for studying\n      LLM behavior under context-parametric knowledge conflicts. Our primary evaluation\n      dataset.\n    role: foundation\n    title: 'Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large\n      Language Models in Knowledge Conflicts'\n    url: https://arxiv.org/abs/2305.13300\n    venue: ICLR 2024\n    verified: true\n    year: 2024\n  xing2024evaluating:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xing, X.\n    - He, Z.\n    - Xu, H.\n    - Wang, X.\n    - Wang, R.\n    - Hong, Y.\n    bibtex_key: xing2024evaluating\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: Proposes cross-lingual semantic/accuracy/timeliness consistency metrics\n      (xSC, xAC, xTC) for evaluating multilingual LLM inconsistency. Provides evaluation\n      methodology relevant to our cross-lingual conflict measurement.\n    role: peripheral\n    title: Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language\n      Models\n    url: https://arxiv.org/abs/2407.01358\n    venue: arXiv\n    verified: true\n    year: 2024\n  xu2024knowledge:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xu, R.\n    - Qi, Z.\n    - Guo, Z.\n    - Wang, C.\n    - Wang, H.\n    - Zhang, Y.\n    - Xu, W.\n    bibtex_key: xu2024knowledge\n    category: knowledge-conflict\n    doi: ''\n    relevance: Comprehensive survey of context-memory, inter-context, and intra-memory\n      knowledge conflicts in LLMs. Defines the taxonomy our work builds on.\n    role: foundation\n    title: 'Knowledge Conflicts for LLMs: A Survey'\n    url: https://arxiv.org/abs/2403.08319\n    venue: EMNLP 2024\n    verified: true\n    year: 2024\n  zhao2024analysing:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, Y.\n    - Du, X.\n    - Hong, G.\n    - et al.\n    bibtex_key: zhao2024analysing\n    category: probing\n    doi: ''\n    relevance: 'Original conflict probing work: ~90% accuracy detecting conflicts\n      in residual stream. Foundation for our Track 1 cross-lingual extension.'\n    role: foundation\n    semantic_scholar_id: ''\n    title: Analysing the Residual Stream of Language Models Under Knowledge Conflicts\n    url: https://arxiv.org/abs/2410.16090\n    venue: NeurIPS 2024 FMI Workshop\n    verified: true\n    year: 2024\n  zhao2025steering:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, Y.\n    - Devoto, A.\n    - Hong, G.\n    - et al.\n    bibtex_key: zhao2025steering\n    category: sae-steering\n    doi: ''\n    relevance: 'SpARE: SAE-based conflict feature selection + steering. Core methodology\n      we extend to cross-lingual setting. MI-based feature selection, constraint-aware\n      activation editing.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation\n      Engineering\n    url: https://arxiv.org/abs/2410.15999\n    venue: NAACL 2025 Oral\n    verified: true\n    year: 2025\n  zhao2026when:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, J.\n    - et al.\n    bibtex_key: zhao2026when\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: 'CLEAR benchmark: 10-language cross-lingual conflict evaluation. Behavioral\n      finding that linguistic similarity governs entity-centric conflict resolution.\n      Our work provides mechanistic explanation.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026\n  wu2020emerging:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wu, S.\n    - Conneau, A.\n    - Li, H.\n    - Zettlemoyer, L.\n    - Stoyanov, V.\n    bibtex_key: wu2020emerging\n    category: cross-lingual-repr\n    doi: 10.18653/v1/2020.acl-main.536\n    relevance: Shows mid-layer cross-lingual alignment emerges from shared parameters\n      alone; monolingual representations can be aligned post-hoc. Foundation for understanding\n      language-agnostic concept space our probing hypotheses build on. MUST CITE.\n    role: foundation\n    title: Emerging Cross-lingual Structure in Pretrained Language Models\n    url: https://aclanthology.org/2020.acl-main.536/\n    venue: ACL 2020\n    verified: true\n    year: 2020\n  wendler2024llamas:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wendler, C.\n    - Veselovsky, V.\n    - Monea, G.\n    - West, R.\n    bibtex_key: wendler2024llamas\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Demonstrates English-centric LLMs implicitly pivot through English representations\n      in middle layers. Three-phase pattern (input language -> English pivot -> output\n      language) supports hypothesis that conflict signals may route through English-aligned\n      subspace.\n    role: foundation\n    title: 'Do Llamas Work in English? On the Latent Language of Multilingual Transformers'\n    url: https://arxiv.org/abs/2402.10588\n    venue: ACL 2024\n    verified: true\n    year: 2024\n  muller2021first:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Muller, B.\n    - Elazar, Y.\n    - Sagot, B.\n    - Seddah, D.\n    bibtex_key: muller2021first\n    category: cross-lingual-repr\n    doi: ''\n    relevance: CKA-based layer-wise analysis showing mBERT decomposes into multilingual\n      encoder + language-agnostic predictor. Representations first converge to language\n      neutrality then recover language specificity. Methodological precedent for our\n      layer-wise analysis.\n    role: methodology\n    title: 'First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual\n      BERT'\n    url: https://aclanthology.org/2021.eacl-main.189/\n    venue: EACL 2021\n    verified: true\n    year: 2021\n  kargaran2024mexa:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Kargaran, A.H.\n    - Modarressi, A.\n    - Nikeghbal, N.\n    - Diesner, J.\n    - Yvon, F.\n    - \"Sch\\xFCtze, H.\"\n    bibtex_key: kargaran2024mexa\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Cross-lingual alignment metric leveraging English pivot hypothesis, 0.90\n      Pearson correlation with downstream tasks. Provides evaluation methodology for\n      measuring English-centric alignment relevant to our cross-lingual transfer analysis.\n    role: methodology\n    title: 'MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual\n      Alignment'\n    url: https://arxiv.org/abs/2410.05873\n    venue: Findings of ACL 2025\n    verified: true\n    year: 2024\n  belinkov2022probing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Belinkov, Y.\n    bibtex_key: belinkov2022probing\n    category: probing-methodology\n    doi: ''\n    relevance: Comprehensive survey of probing classifier promises, shortcomings, and\n      advances. Defines the methodological framework our linear probes follow. MUST\n      CITE for probing methodology justification.\n    role: foundation\n    title: 'Probing Classifiers: Promises, Shortcomings, and Advances'\n    url: https://arxiv.org/abs/2102.12452\n    venue: Computational Linguistics 48(1)\n    verified: true\n    year: 2022\n  hewitt2019designing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Hewitt, J.\n    - Liang, P.\n    bibtex_key: hewitt2019designing\n    category: probing-methodology\n    doi: ''\n    relevance: Introduces selectivity metric (linguistic accuracy - control accuracy)\n      to distinguish genuine representation encoding from probe memorization. Our probing\n      design uses control tasks following this framework. EMNLP 2019 Best Paper Runner\n      Up.\n    role: methodology\n    title: Designing and Interpreting Probes with Control Tasks\n    url: https://aclanthology.org/D19-1275/\n    venue: EMNLP 2019\n    verified: true\n    year: 2019\n  ulmer2022deep:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Ulmer, D.\n    - Hardmeier, C.\n    - Frellsen, J.\n    bibtex_key: ulmer2022deep\n    category: probing-methodology\n    doi: ''\n    relevance: Bootstrap-based statistical testing framework for neural network comparisons,\n      including Almost Stochastic Order (ASO). Provides the bootstrap CI methodology\n      we use for probing accuracy significance testing.\n    role: methodology\n    title: 'deep-significance: Easy and Meaningful Statistical Significance Testing\n      in the Age of Neural Networks'\n    url: https://arxiv.org/abs/2204.06815\n    venue: arXiv\n    verified: true\n    year: 2022\n",
      "numLines": 470,
      "startLine": 1,
      "totalLines": 470
    }
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T14:05:25.989Z_

<details><summary>↩ Tool result · `toolu_01Vx3HvbBK35TxGejvyhTVWC`</summary>

```text
Web search results for query: "Zou et al 2023 "Representation Engineering: A Top-Down Approach to AI Transparency""

Links: [{"title":"[PDF] Representation Engineering: A Top-Down Approach to AI Transparency | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Representation-Engineering:-A-Top-Down-Approach-to-Zou-Phan/58fdf550600fc3873729d466601c5d08a51ba8a0"},{"title":"[2310.01405v2] Representation Engineering: A Top-Down Approach to AI Transparency","url":"https://arxiv.org/abs/2310.01405v2"},{"title":"[2310.01405v3] Representation Engineering: A Top-Down Approach to AI Transparency","url":"http://arxiv.org/abs/2310.01405v3"},{"title":"[2310.01405] Representation Engineering: A Top-Down Approach to AI Transparency","url":"https://arxiv.org/abs/2310.01405"},{"title":"GitHub - andyzoujm/representation-engineering: Representation Engineering: A Top-Down Approach to AI Transparency · GitHub","url":"https://github.com/andyzoujm/representation-engineering"},{"title":"Representation Engineering: A Top-Down Approach to AI Transparency","url":"https://arxiv.org/pdf/2310.01405"},{"title":"dblp: Representation Engineering: A Top-Down Approach to AI Transparency.","url":"https://dblp.org/rec/journals/corr/abs-2310-01405.html"},{"title":"Representation Engineering: A Top-Down Approach to AI Transparency","url":"https://arxiv.org/html/2310.01405v4"}]

I found the paper you're looking for. Here's what I found:

"Representation Engineering: A Top-Down Approach to AI Transparency" by Zou et al. (2023) identifies and characterizes representation engineering (RepE), an approach to enhancing the transparency of AI systems that draws on insights from cognitive neuroscience. RepE places population-level representations, rather than neurons or circuits, at the center of analysis, equipping us with novel methods for monitoring and manipulating high-level cognitive phenomena in deep neural networks (DNNs).

The methods can provide traction on a wide range of safety-relevant problems, including honesty, harmlessness, power-seeking, and more.

The paper was submitted on October 2, 2023 and has multiple versions available on arXiv (latest version March 3, 2025) (arXiv:2310.01405). The official repository is available on GitHub, and the paper includes applications to honesty and hallucination, utility, power-aversion, probability and risk, emotion, harmlessness, fairness and bias, knowledge editing, and memorization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "097dd1b9-4066-47e8-a63a-9ca5571bcc81",
  "tool_use_result": {
    "query": "Zou et al 2023 \"Representation Engineering: A Top-Down Approach to AI Transparency\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Vzz9HByTTFJkCViMtz3ixR",
        "content": [
          {
            "title": "[PDF] Representation Engineering: A Top-Down Approach to AI Transparency | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Representation-Engineering:-A-Top-Down-Approach-to-Zou-Phan/58fdf550600fc3873729d466601c5d08a51ba8a0"
          },
          {
            "title": "[2310.01405v2] Representation Engineering: A Top-Down Approach to AI Transparency",
            "url": "https://arxiv.org/abs/2310.01405v2"
          },
          {
            "title": "[2310.01405v3] Representation Engineering: A Top-Down Approach to AI Transparency",
            "url": "http://arxiv.org/abs/2310.01405v3"
          },
          {
            "title": "[2310.01405] Representation Engineering: A Top-Down Approach to AI Transparency",
            "url": "https://arxiv.org/abs/2310.01405"
          },
          {
            "title": "GitHub - andyzoujm/representation-engineering: Representation Engineering: A Top-Down Approach to AI Transparency · GitHub",
            "url": "https://github.com/andyzoujm/representation-engineering"
          },
          {
            "title": "Representation Engineering: A Top-Down Approach to AI Transparency",
            "url": "https://arxiv.org/pdf/2310.01405"
          },
          {
            "title": "dblp: Representation Engineering: A Top-Down Approach to AI Transparency.",
            "url": "https://dblp.org/rec/journals/corr/abs-2310-01405.html"
          },
          {
            "title": "Representation Engineering: A Top-Down Approach to AI Transparency",
            "url": "https://arxiv.org/html/2310.01405v4"
          }
        ]
      },
      "I found the paper you're looking for. Here's what I found:\n\n\"Representation Engineering: A Top-Down Approach to AI Transparency\" by Zou et al. (2023) identifies and characterizes representation engineering (RepE), an approach to enhancing the transparency of AI systems that draws on insights from cognitive neuroscience. RepE places population-level representations, rather than neurons or circuits, at the center of analysis, equipping us with novel methods for monitoring and manipulating high-level cognitive phenomena in deep neural networks (DNNs).\n\nThe methods can provide traction on a wide range of safety-relevant problems, including honesty, harmlessness, power-seeking, and more.\n\nThe paper was submitted on October 2, 2023 and has multiple versions available on arXiv (latest version March 3, 2025) (arXiv:2310.01405). The official repository is available on GitHub, and the paper includes applications to honesty and hallucination, utility, power-aversion, probability and risk, emotion, harmlessness, fairness and bias, knowledge editing, and memorization."
    ],
    "durationSeconds": 6.255237625999999
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-22T14:05:26.225Z_

<details><summary>↩ Tool result · `toolu_0183HxPS9WRfRrC184eNYcM8`</summary>

```text
Web search results for query: "Li et al 2024 "Inference-Time Intervention" truthful LLM activation addition"

Links: [{"title":"[2306.03341] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/abs/2306.03341"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language   Model","url":"https://arxiv.org/pdf/2306.03341"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/html/2306.03341"},{"title":"[PDF] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Inference-Time-Intervention:-Eliciting-Truthful-a-Li-Patel/405f8f5f1c6df1b3343c812832479aad5180b65f"},{"title":"Inference-Time Intervention (ITI)","url":"https://www.emergentmind.com/topics/inference-time-intervention-iti"},{"title":"(PDF) Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://www.researchgate.net/publication/371347185_Inference-Time_Intervention_Eliciting_Truthful_Answers_from_a_Language_Model"}]

Based on the search results, here's information about the Li et al. Inference-Time Intervention paper:

## Overview

Inference-Time Intervention (ITI) is a technique designed to enhance the "truthfulness" of large language models by shifting model activations during inference, following a set of directions across a limited number of attention heads.

## Key Results

On an instruction-finetuned LLaMA called Alpaca, ITI improves its truthfulness from 32.5% to 65.1%. The intervention significantly improves the performance of LLaMA models on the TruthfulQA benchmark.

## Technical Approach

The technique operates by shifting model activations during inference, following directions across a limited number of attention heads. ITI is minimally invasive and computationally inexpensive, and the technique is data efficient: while approaches like RLHF require extensive annotations, ITI locates truthful directions using only a few hundred examples.

## Key Insight

The findings suggest that LLMs may have an internal representation of the likelihood of something being true, even as they produce falsehoods on the surface.

**Note:** The paper was originally published in June 2023, not 2024. The authors are Kenneth Li, Oam Patel, Fernanda Viégas, Hanspeter Pfister, and Martin Wattenberg from Harvard University.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "7b7f61fb-d9c9-4695-aedf-7a0fc2f3f3f1",
  "tool_use_result": {
    "query": "Li et al 2024 \"Inference-Time Intervention\" truthful LLM activation addition",
    "results": [
      {
        "tool_use_id": "srvtoolu_011r2nFJtppEvRa9HeCfRoJV",
        "content": [
          {
            "title": "[2306.03341] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model",
            "url": "https://arxiv.org/abs/2306.03341"
          },
          {
            "title": "Inference-Time Intervention: Eliciting Truthful Answers from a Language   Model",
            "url": "https://arxiv.org/pdf/2306.03341"
          },
          {
            "title": "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model",
            "url": "https://arxiv.org/html/2306.03341"
          },
          {
            "title": "[PDF] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Inference-Time-Intervention:-Eliciting-Truthful-a-Li-Patel/405f8f5f1c6df1b3343c812832479aad5180b65f"
          },
          {
            "title": "Inference-Time Intervention (ITI)",
            "url": "https://www.emergentmind.com/topics/inference-time-intervention-iti"
          },
          {
            "title": "(PDF) Inference-Time Intervention: Eliciting Truthful Answers from a Language Model",
            "url": "https://www.researchgate.net/publication/371347185_Inference-Time_Intervention_Eliciting_Truthful_Answers_from_a_Language_Model"
          }
        ]
      },
      "Based on the search results, here's information about the Li et al. Inference-Time Intervention paper:\n\n## Overview\n\nInference-Time Intervention (ITI) is a technique designed to enhance the \"truthfulness\" of large language models by shifting model activations during inference, following a set of directions across a limited number of attention heads.\n\n## Key Results\n\nOn an instruction-finetuned LLaMA called Alpaca, ITI improves its truthfulness from 32.5% to 65.1%. The intervention significantly improves the performance of LLaMA models on the TruthfulQA benchmark.\n\n## Technical Approach\n\nThe technique operates by shifting model activations during inference, following directions across a limited number of attention heads. ITI is minimally invasive and computationally inexpensive, and the technique is data efficient: while approaches like RLHF require extensive annotations, ITI locates truthful directions using only a few hundred examples.\n\n## Key Insight\n\nThe findings suggest that LLMs may have an internal representation of the likelihood of something being true, even as they produce falsehoods on the surface.\n\n**Note:** The paper was originally published in June 2023, not 2024. The authors are Kenneth Li, Oam Patel, Fernanda Viégas, Hanspeter Pfister, and Martin Wattenberg from Harvard University."
    ],
    "durationSeconds": 6.941662988999998
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T14:05:27.983Z_

<details><summary>↩ Tool result · `toolu_01Ryitoxd62cs2mqsp3V4ZNw`</summary>

```text
Web search results for query: "XNLI cross-lingual natural language inference Conneau et al 2018"

Links: [{"title":"XNLI","url":"https://cims.nyu.edu/~sbowman/xnli/"},{"title":"XNLI: Evaluating Cross-lingual Sentence Representations | Request PDF","url":"https://www.researchgate.net/publication/334118044_XNLI_Evaluating_Cross-lingual_Sentence_Representations"},{"title":"Cross-Lingual NLI: Benchmarks & Methods","url":"https://www.emergentmind.com/topics/cross-lingual-natural-language-inference-xnli"},{"title":"GitHub - facebookresearch/XNLI: Evaluating Cross-lingual Sentence Representations · GitHub","url":"https://github.com/facebookresearch/XNLI"},{"title":"XNLI: Evaluating Cross-lingual Sentence Representations - ACL Anthology","url":"https://aclanthology.org/D18-1269/"},{"title":"Table 1 from XNLI: Evaluating Cross-lingual Sentence Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XNLI:-Evaluating-Cross-lingual-Sentence-Conneau-Lample/1c3112ef8a346b9817382ed34a8c146c53d5bcf5/figure/0"},{"title":"XNLI: Evaluating Cross-lingual Sentence Representations","url":"https://aclanthology.org/D18-1269.pdf"},{"title":"[PDF] XNLI: Evaluating Cross-lingual Sentence Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XNLI:-Evaluating-Cross-lingual-Sentence-Conneau-Lample/1c3112ef8a346b9817382ed34a8c146c53d5bcf5"},{"title":"[1809.05053] XNLI: Evaluating Cross-lingual Sentence Representations","url":"https://arxiv.org/abs/1809.05053"},{"title":"Myanmar XNLI: building a dataset and exploring low-resource approaches to natural language inference with Myanmar | Language Resources and Evaluation | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10579-025-09844-1"}]

Based on the search results, here's information about the XNLI dataset from Conneau et al. 2018:

## Overview

The Cross-lingual Natural Language Inference (XNLI) corpus is a crowd-sourced collection of 5,000 test and 2,500 dev pairs for the MultiNLI corpus. The dataset extends the development and test sets of the Multi-Genre Natural Language Inference Corpus (MultiNLI) to 14 languages, including low-resource languages such as Swahili and Urdu.

## Languages and Scale

The pairs are annotated with textual entailment and translated into 14 languages: French, Spanish, German, Greek, Bulgarian, Russian, Turkish, Arabic, Vietnamese, Thai, Chinese, Hindi, Swahili and Urdu. This results in 112.5k annotated pairs, with each premise associable with the corresponding hypothesis in the 15 languages, summing up to more than 1.5M combinations.

## Purpose

The corpus is made to evaluate how to perform inference in any language (including low-resources ones like Swahili or Urdu) when only English NLI data is available at training time, with cross-lingual sentence encoding as one solution.

## Baselines

The authors provide several baselines for multilingual sentence understanding, including two based on machine translation systems and two that use parallel data to train aligned multilingual bag-of-words and LSTM encoders, finding that directly translating the test data yields the best performance among available baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "02da3292-d68c-4770-9356-46e708025114",
  "tool_use_result": {
    "query": "XNLI cross-lingual natural language inference Conneau et al 2018",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EHEGyWHDJEae8JSs19CQxh",
        "content": [
          {
            "title": "XNLI",
            "url": "https://cims.nyu.edu/~sbowman/xnli/"
          },
          {
            "title": "XNLI: Evaluating Cross-lingual Sentence Representations | Request PDF",
            "url": "https://www.researchgate.net/publication/334118044_XNLI_Evaluating_Cross-lingual_Sentence_Representations"
          },
          {
            "title": "Cross-Lingual NLI: Benchmarks & Methods",
            "url": "https://www.emergentmind.com/topics/cross-lingual-natural-language-inference-xnli"
          },
          {
            "title": "GitHub - facebookresearch/XNLI: Evaluating Cross-lingual Sentence Representations · GitHub",
            "url": "https://github.com/facebookresearch/XNLI"
          },
          {
            "title": "XNLI: Evaluating Cross-lingual Sentence Representations - ACL Anthology",
            "url": "https://aclanthology.org/D18-1269/"
          },
          {
            "title": "Table 1 from XNLI: Evaluating Cross-lingual Sentence Representations | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/XNLI:-Evaluating-Cross-lingual-Sentence-Conneau-Lample/1c3112ef8a346b9817382ed34a8c146c53d5bcf5/figure/0"
          },
          {
            "title": "XNLI: Evaluating Cross-lingual Sentence Representations",
            "url": "https://aclanthology.org/D18-1269.pdf"
          },
          {
            "title": "[PDF] XNLI: Evaluating Cross-lingual Sentence Representations | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/XNLI:-Evaluating-Cross-lingual-Sentence-Conneau-Lample/1c3112ef8a346b9817382ed34a8c146c53d5bcf5"
          },
          {
            "title": "[1809.05053] XNLI: Evaluating Cross-lingual Sentence Representations",
            "url": "https://arxiv.org/abs/1809.05053"
          },
          {
            "title": "Myanmar XNLI: building a dataset and exploring low-resource approaches to natural language inference with Myanmar | Language Resources and Evaluation | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10579-025-09844-1"
          }
        ]
      },
      "Based on the search results, here's information about the XNLI dataset from Conneau et al. 2018:\n\n## Overview\n\nThe Cross-lingual Natural Language Inference (XNLI) corpus is a crowd-sourced collection of 5,000 test and 2,500 dev pairs for the MultiNLI corpus. The dataset extends the development and test sets of the Multi-Genre Natural Language Inference Corpus (MultiNLI) to 14 languages, including low-resource languages such as Swahili and Urdu.\n\n## Languages and Scale\n\nThe pairs are annotated with textual entailment and translated into 14 languages: French, Spanish, German, Greek, Bulgarian, Russian, Turkish, Arabic, Vietnamese, Thai, Chinese, Hindi, Swahili and Urdu. This results in 112.5k annotated pairs, with each premise associable with the corresponding hypothesis in the 15 languages, summing up to more than 1.5M combinations.\n\n## Purpose\n\nThe corpus is made to evaluate how to perform inference in any language (including low-resources ones like Swahili or Urdu) when only English NLI data is available at training time, with cross-lingual sentence encoding as one solution.\n\n## Baselines\n\nThe authors provide several baselines for multilingual sentence understanding, including two based on machine translation systems and two that use parallel data to train aligned multilingual bag-of-words and LSTM encoders, finding that directly translating the test data yields the best performance among available baselines."
    ],
    "durationSeconds": 8.212437891
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T14:05:27.989Z_

<details><summary>↩ Tool result · `toolu_016QoVmroRRwQjmzBpQ2BXVq`</summary>

```text
Web search results for query: "Llama 3.1 technical report Meta 2024"

Links: [{"title":"Meta Llama 3 - An Overview","url":"https://debuggercafe.com/meta-llama-3-an-overview/"},{"title":"Breaking Down Meta's Llama 3 Herd of Models - Arize AI","url":"https://arize.com/blog/breaking-down-meta-llama-3/"},{"title":"Meta Llama 3.1 405B Review — The First Open-Weight Frontier Model — ChatForest","url":"https://chatforest.com/reviews/meta-llama-3-1-405b-frontier-open-weight-llm-review/"},{"title":"Introducing Llama 3.1: Our most capable models to date","url":"https://ai.meta.com/blog/meta-llama-3-1/"},{"title":"The future of AI: Built with Llama - Meta AI","url":"https://ai.meta.com/blog/future-of-ai-built-with-llama/"},{"title":"Meta’s New Llama 3.1 AI Model: Use Cases & Benchmarks","url":"https://gaper.io/metas-new-llama-3-1/"},{"title":"The Llama 3 Herd of Models | Research - AI at Meta","url":"https://ai.meta.com/research/publications/the-llama-3-herd-of-models/"},{"title":"meta-llama/Meta-Llama-3-8B · Hugging Face","url":"https://huggingface.co/meta-llama/Meta-Llama-3-8B"}]

Based on the search results, here's what I found about the Llama 3.1 technical report from Meta in 2024:

## Overview

The Llama 3 technical report was published on July 23, 2024, and presents a new set of foundation models called Llama 3—a herd of language models that natively support multilinguality, coding, reasoning, and tool usage, with the largest model being a dense Transformer with 405B parameters and a context window of up to 128K tokens.

## Key Features

The release included upgraded versions of the 8B and 70B models that are multilingual and have a significantly longer context length of 128K, state-of-the-art tool use, and overall stronger reasoning capabilities.

## Model Capabilities

Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks. More specifically, the 405B model achieved MMLU 88.6%, GPQA 51.1%, HumanEval 89.0%, and MATH 73.8%.

## Release

Meta publicly released Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and Llama Guard 3 model for input and output safety.

The full technical report is available on Meta's official research publications page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "307497c8-4ee0-4aba-868d-ce1bdaa0dea8",
  "tool_use_result": {
    "query": "Llama 3.1 technical report Meta 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_012te35MfcGxWePYuM6AoWDr",
        "content": [
          {
            "title": "Meta Llama 3 - An Overview",
            "url": "https://debuggercafe.com/meta-llama-3-an-overview/"
          },
          {
            "title": "Breaking Down Meta's Llama 3 Herd of Models - Arize AI",
            "url": "https://arize.com/blog/breaking-down-meta-llama-3/"
          },
          {
            "title": "Meta Llama 3.1 405B Review — The First Open-Weight Frontier Model — ChatForest",
            "url": "https://chatforest.com/reviews/meta-llama-3-1-405b-frontier-open-weight-llm-review/"
          },
          {
            "title": "Introducing Llama 3.1: Our most capable models to date",
            "url": "https://ai.meta.com/blog/meta-llama-3-1/"
          },
          {
            "title": "The future of AI: Built with Llama - Meta AI",
            "url": "https://ai.meta.com/blog/future-of-ai-built-with-llama/"
          },
          {
            "title": "Meta’s New Llama 3.1 AI Model: Use Cases & Benchmarks",
            "url": "https://gaper.io/metas-new-llama-3-1/"
          },
          {
            "title": "The Llama 3 Herd of Models | Research - AI at Meta",
            "url": "https://ai.meta.com/research/publications/the-llama-3-herd-of-models/"
          },
          {
            "title": "meta-llama/Meta-Llama-3-8B · Hugging Face",
            "url": "https://huggingface.co/meta-llama/Meta-Llama-3-8B"
          }
        ]
      },
      "Based on the search results, here's what I found about the Llama 3.1 technical report from Meta in 2024:\n\n## Overview\n\nThe Llama 3 technical report was published on July 23, 2024, and presents a new set of foundation models called Llama 3—a herd of language models that natively support multilinguality, coding, reasoning, and tool usage, with the largest model being a dense Transformer with 405B parameters and a context window of up to 128K tokens.\n\n## Key Features\n\nThe release included upgraded versions of the 8B and 70B models that are multilingual and have a significantly longer context length of 128K, state-of-the-art tool use, and overall stronger reasoning capabilities.\n\n## Model Capabilities\n\nLlama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks. More specifically, the 405B model achieved MMLU 88.6%, GPQA 51.1%, HumanEval 89.0%, and MATH 73.8%.\n\n## Release\n\nMeta publicly released Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and Llama Guard 3 model for input and output safety.\n\nThe full technical report is available on Meta's official research publications page."
    ],
    "durationSeconds": 7.252237248000001
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T14:05:30.247Z_

<details><summary>↩ Tool result · `toolu_01GAh2iJ1izoHTpsKSqVrfXK`</summary>

```text
Web search results for query: "COMET translation evaluation metric Rei et al 2020 2022"

Links: [{"title":"COMET: Crosslingual Translation Evaluation","url":"https://www.emergentmind.com/topics/crosslingual-optimized-metric-for-evaluation-of-translation-comet"},{"title":"(PDF) COMET: A Neural Framework for MT Evaluation","url":"https://www.researchgate.net/publication/347234911_COMET_A_Neural_Framework_for_MT_Evaluation"},{"title":"xcomet: Transparent Machine Translation Evaluation through Fine-grained Error Detection | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00683/124263/xcomet-Transparent-Machine-Translation-Evaluation"},{"title":"Pitfalls and Outlooks in Using COMET","url":"https://arxiv.org/html/2408.15366v3"},{"title":"COMET: A Neural Framework for MT Evaluation - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.213/"},{"title":"Long-context Reference-based MT Quality Estimation","url":"https://arxiv.org/html/2509.13980v1"},{"title":"Pitfalls and Outlooks in Using COMET","url":"https://www2.statmt.org/wmt24/pdf/2024.wmt-1.121.pdf"}]

Based on the search results, here's what I found about COMET:

## Overview

COMET is a neural framework for training multilingual machine translation evaluation models that obtains state-of-the-art correlation with human judgements by leveraging cross-lingual pretrained language modeling to exploit information from both source input and target-language reference translation.

## Original 2020 Paper

The original COMET framework was published by Ricardo Rei, Craig Stewart, Ana C Farinha, and Alon Lavie in 2020. The original COMET framework utilizes a pretrained cross-lingual Transformer encoder, such as XLM-RoBERTa.

## Performance and Evolution

COMET represents a shift from string matching metrics to trained neural metrics in machine translation evaluation, and has been shown to correlate much better with human judgement, making it more reliable in estimating translation quality and ranking translation systems.

## 2022 Extensions

Rei et al. published extensions to COMET, including CometKiwi, in 2020 and 2022, which incorporate source language input. Fine-tuned versions of COMET from 2020 and 2022 are learnable models that directly optimize underlying embedding models to maximize correlation with human judgments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "263bd120-4608-447b-8075-c4670623d235",
  "tool_use_result": {
    "query": "COMET translation evaluation metric Rei et al 2020 2022",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HKmYWvwSV7ASsEyRfkvgZS",
        "content": [
          {
            "title": "COMET: Crosslingual Translation Evaluation",
            "url": "https://www.emergentmind.com/topics/crosslingual-optimized-metric-for-evaluation-of-translation-comet"
          },
          {
            "title": "(PDF) COMET: A Neural Framework for MT Evaluation",
            "url": "https://www.researchgate.net/publication/347234911_COMET_A_Neural_Framework_for_MT_Evaluation"
          },
          {
            "title": "xcomet: Transparent Machine Translation Evaluation through Fine-grained Error Detection | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00683/124263/xcomet-Transparent-Machine-Translation-Evaluation"
          },
          {
            "title": "Pitfalls and Outlooks in Using COMET",
            "url": "https://arxiv.org/html/2408.15366v3"
          },
          {
            "title": "COMET: A Neural Framework for MT Evaluation - ACL Anthology",
            "url": "https://aclanthology.org/2020.emnlp-main.213/"
          },
          {
            "title": "Long-context Reference-based MT Quality Estimation",
            "url": "https://arxiv.org/html/2509.13980v1"
          },
          {
            "title": "Pitfalls and Outlooks in Using COMET",
            "url": "https://www2.statmt.org/wmt24/pdf/2024.wmt-1.121.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about COMET:\n\n## Overview\n\nCOMET is a neural framework for training multilingual machine translation evaluation models that obtains state-of-the-art correlation with human judgements by leveraging cross-lingual pretrained language modeling to exploit information from both source input and target-language reference translation.\n\n## Original 2020 Paper\n\nThe original COMET framework was published by Ricardo Rei, Craig Stewart, Ana C Farinha, and Alon Lavie in 2020. The original COMET framework utilizes a pretrained cross-lingual Transformer encoder, such as XLM-RoBERTa.\n\n## Performance and Evolution\n\nCOMET represents a shift from string matching metrics to trained neural metrics in machine translation evaluation, and has been shown to correlate much better with human judgement, making it more reliable in estimating translation quality and ranking translation systems.\n\n## 2022 Extensions\n\nRei et al. published extensions to COMET, including CometKiwi, in 2020 and 2022, which incorporate source language input. Fine-tuned versions of COMET from 2020 and 2022 are learnable models that directly optimize underlying embedding models to maximize correlation with human judgments."
    ],
    "durationSeconds": 9.993707751999999
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the search results and the current literature map. Let me now search for additional papers for both clusters.

For Cluster 5, I still need:
1. Li et al. 2023 (not 2024) - ITI - confirmed: Kenneth Li, Oam Patel, et al., NeurIPS 2023. Let me verify the venue.
2. Zou et al. 2023 - Representation Engineering - confirmed: arXiv 2310.01405
3. Any 2024-2026 work using probe weights for steering


4. For Cluster 6, I need to confirm XNLI (Conneau et al. 2018, EMNLP), COMET (Rei et al. 2020, EMNLP), and locate the Llama 3.1 and Qwen 2.5 technical reports. Let me search for more details on these remaining papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "09f85b10-2268-492e-9d8d-477d0c8c5e23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5dep2DZfbHhv6vxzNuKQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6935,
      "cache_creation_input_tokens": 3553,
      "cache_read_input_tokens": 25397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3553
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

Now let me search for additional papers and verify venues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "85dd8691-ed6f-416a-908f-ce76f6863cd4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5dep2DZfbHhv6vxzNuKQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6935,
      "cache_creation_input_tokens": 3553,
      "cache_read_input_tokens": 25397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3553
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qwzf4ntDx88MxLndyZoTRm`</summary>

```json
{
  "query": "Kenneth Li \"Inference-Time Intervention\" NeurIPS 2024 venue publication"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "1bda0581-f5bd-4748-9741-2db2d43a4418",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5dep2DZfbHhv6vxzNuKQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6935,
      "cache_creation_input_tokens": 3553,
      "cache_read_input_tokens": 25397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3553
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JmuUDAbDhBBdmiYMUhFz3h`</summary>

```json
{
  "query": "Qwen 2.5 technical report 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "3b6de59d-e623-4701-8d44-03c699aee1f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5dep2DZfbHhv6vxzNuKQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6935,
      "cache_creation_input_tokens": 3553,
      "cache_read_input_tokens": 25397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3553
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pj64N6Qb9kZaFtvtSxgpKZ`</summary>

```json
{
  "query": "\"representation steering\" \"knowledge conflict\" LLM activation editing 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "3eb1d4e1-0dcc-4828-b86c-0ce5526ec277",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5dep2DZfbHhv6vxzNuKQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6935,
      "cache_creation_input_tokens": 3553,
      "cache_read_input_tokens": 25397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3553
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y6GVEBNKF3YLMf4Am7yC3k`</summary>

```json
{
  "query": "arxiv 2407.21783 \"The Llama 3 Herd of Models\" Meta"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "00144293-fa78-4d08-82e6-a48198bbbd5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T5dep2DZfbHhv6vxzNuKQw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6935,
      "cache_creation_input_tokens": 3553,
      "cache_read_input_tokens": 25397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3553
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

_source line 27 · 2026-05-22T14:05:45.234Z_

<details><summary>↩ Tool result · `toolu_01Qwzf4ntDx88MxLndyZoTRm`</summary>

```text
Web search results for query: "Kenneth Li "Inference-Time Intervention" NeurIPS 2024 venue publication"

Links: [{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/81b8390039b7302c909cb769f8b6cd93-Abstract-Conference.html"},{"title":"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/pdf/2306.03341"},{"title":"[2306.03341v6] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/abs/2306.03341v6"},{"title":"[2306.03341] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://arxiv.org/abs/2306.03341"},{"title":"GitHub - likenneth/honest_llama: Inference-Time Intervention: Eliciting Truthful Answers from a Language Model · GitHub","url":"https://github.com/likenneth/honest_llama"},{"title":"【DL輪読会】Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | ドクセル","url":"https://www.docswell.com/s/DeepLearning2023/Z38P8D-2024-06-20-131813"},{"title":"Inference-time intervention | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3667919"},{"title":"NeurIPS Poster Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://neurips.cc/virtual/2023/poster/71200"},{"title":"NeurIPS Poster Inference-Time Intervention: Eliciting Truthful Answers from a Language Model","url":"https://nips.cc/virtual/2023/poster/71200"}]

Based on the search results, Kenneth Li's "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model" was published at Advances in Neural Information Processing Systems 36 (NeurIPS 2023), not NeurIPS 2024.

The paper was authored by Kenneth Li, Oam Patel, Fernanda Viégas, Hanspeter Pfister, and Martin Wattenberg, and appeared in the Main Conference Track.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "33a81d9a-0d11-4bb4-bd10-c23f0c82939b",
  "tool_use_result": {
    "query": "Kenneth Li \"Inference-Time Intervention\" NeurIPS 2024 venue publication",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UcDgKVn3xEoj1ooco5azKh",
        "content": [
          {
            "title": "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/hash/81b8390039b7302c909cb769f8b6cd93-Abstract-Conference.html"
          },
          {
            "title": "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model",
            "url": "https://arxiv.org/pdf/2306.03341"
          },
          {
            "title": "[2306.03341v6] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model",
            "url": "https://arxiv.org/abs/2306.03341v6"
          },
          {
            "title": "[2306.03341] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model",
            "url": "https://arxiv.org/abs/2306.03341"
          },
          {
            "title": "GitHub - likenneth/honest_llama: Inference-Time Intervention: Eliciting Truthful Answers from a Language Model · GitHub",
            "url": "https://github.com/likenneth/honest_llama"
          },
          {
            "title": "【DL輪読会】Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | ドクセル",
            "url": "https://www.docswell.com/s/DeepLearning2023/Z38P8D-2024-06-20-131813"
          },
          {
            "title": "Inference-time intervention | Proceedings of the 37th International Conference on Neural Information Processing Systems",
            "url": "https://dl.acm.org/doi/10.5555/3666122.3667919"
          },
          {
            "title": "NeurIPS Poster Inference-Time Intervention: Eliciting Truthful Answers from a Language Model",
            "url": "https://neurips.cc/virtual/2023/poster/71200"
          },
          {
            "title": "NeurIPS Poster Inference-Time Intervention: Eliciting Truthful Answers from a Language Model",
            "url": "https://nips.cc/virtual/2023/poster/71200"
          }
        ]
      },
      "Based on the search results, Kenneth Li's \"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model\" was published at Advances in Neural Information Processing Systems 36 (NeurIPS 2023), not NeurIPS 2024.\n\nThe paper was authored by Kenneth Li, Oam Patel, Fernanda Viégas, Hanspeter Pfister, and Martin Wattenberg, and appeared in the Main Conference Track."
    ],
    "durationSeconds": 4.554533430000003
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T14:05:48.289Z_

<details><summary>↩ Tool result · `toolu_01JmuUDAbDhBBdmiYMUhFz3h`</summary>

```text
Web search results for query: "Qwen 2.5 technical report 2024 arxiv"

Links: [{"title":"[PDF] Qwen2.5 Technical Report | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Qwen2.5-Technical-Report-Yang-Yang/88aa6b1f37d1fd8e0a40499ce9bb87873f03aaa8"},{"title":"[2409.12186] Qwen2.5-Coder Technical Report","url":"https://arxiv.org/abs/2409.12186"},{"title":"[2412.15115] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115"},{"title":"2024-12-20 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115v1"},{"title":"(PDF) Qwen2.5-Omni Technical Report","url":"https://www.researchgate.net/publication/390213734_Qwen25-Omni_Technical_Report"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v3"},{"title":"[2409.12122] Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement","url":"https://arxiv.org/abs/2409.12122"}]

I found the Qwen 2.5 Technical Report on arXiv. Here are the key details:

**Main Paper:** The Qwen2.5 Technical Report was published on arXiv (paper 2412.15115) on December 19, 2024, with the latest version submitted on January 3, 2025.

**Key Highlights:**

- The report introduces Qwen2.5, a comprehensive series of large language models designed to meet diverse needs.

- Qwen 2.5 leverages 18 trillion tokens for pre-training and has demonstrated the most advanced capabilities within the Qwen series, especially in terms of domain expertise.

- The open-weight flagship Qwen2.5-72B-Instruct outperforms a number of open and proprietary models and demonstrates competitive performance to the state-of-the-art open-weight model, Llama-3-405B-Instruct, which is around 5 times larger.

The paper is available on arXiv at: **https://arxiv.org/abs/2412.15115**


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "57215ee4-3354-4897-a45e-8840e620b42d",
  "tool_use_result": {
    "query": "Qwen 2.5 technical report 2024 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EBPxaiQo7HxJA878rJ6cjt",
        "content": [
          {
            "title": "[PDF] Qwen2.5 Technical Report | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Qwen2.5-Technical-Report-Yang-Yang/88aa6b1f37d1fd8e0a40499ce9bb87873f03aaa8"
          },
          {
            "title": "[2409.12186] Qwen2.5-Coder Technical Report",
            "url": "https://arxiv.org/abs/2409.12186"
          },
          {
            "title": "[2412.15115] Qwen2.5 Technical Report",
            "url": "https://arxiv.org/abs/2412.15115"
          },
          {
            "title": "2024-12-20 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen",
            "url": "https://arxiv.org/pdf/2412.15115v1"
          },
          {
            "title": "(PDF) Qwen2.5-Omni Technical Report",
            "url": "https://www.researchgate.net/publication/390213734_Qwen25-Omni_Technical_Report"
          },
          {
            "title": "2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen",
            "url": "https://arxiv.org/pdf/2412.15115"
          },
          {
            "title": "Qwen2.5-Coder Technical Report",
            "url": "https://arxiv.org/html/2409.12186v3"
          },
          {
            "title": "[2409.12122] Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement",
            "url": "https://arxiv.org/abs/2409.12122"
          }
        ]
      },
      "I found the Qwen 2.5 Technical Report on arXiv. Here are the key details:\n\n**Main Paper:** The Qwen2.5 Technical Report was published on arXiv (paper 2412.15115) on December 19, 2024, with the latest version submitted on January 3, 2025.\n\n**Key Highlights:**\n\n- The report introduces Qwen2.5, a comprehensive series of large language models designed to meet diverse needs.\n\n- Qwen 2.5 leverages 18 trillion tokens for pre-training and has demonstrated the most advanced capabilities within the Qwen series, especially in terms of domain expertise.\n\n- The open-weight flagship Qwen2.5-72B-Instruct outperforms a number of open and proprietary models and demonstrates competitive performance to the state-of-the-art open-weight model, Llama-3-405B-Instruct, which is around 5 times larger.\n\nThe paper is available on arXiv at: **https://arxiv.org/abs/2412.15115**"
    ],
    "durationSeconds": 7.606025476000003
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-22T14:05:49.172Z_

<details><summary>↩ Tool result · `toolu_01Pj64N6Qb9kZaFtvtSxgpKZ`</summary>

```text
Web search results for query: ""representation steering" "knowledge conflict" LLM activation editing 2024 2025"

Links: [{"title":"Steering Knowledge Selection Behaviours in LLMs","url":"https://arxiv.org/pdf/2410.15999"},{"title":"[Quick Review] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering","url":"https://liner.com/review/steering-knowledge-selection-behaviours-in-llms-via-saebased-representation-engineering"},{"title":"arXiv:2502.19649v3 [cs.LG] 12 Mar 2025 - Jan Wehner","url":"https://janwehner.com/files/representation_engineering.pdf"},{"title":"Steering MoE LLMs via Expert (De)Activation","url":"https://arxiv.org/html/2509.09660v1"},{"title":"Representation Engineering for Large-Language Models: Survey and Research Challenges","url":"https://arxiv.org/html/2502.17601v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf"},{"title":"psa: differentially private steering for large language model ...","url":"https://arxiv.org/pdf/2501.18532"},{"title":"Representation Bending for Large Language Model Safety","url":"https://aclanthology.org/2025.acl-long.1173.pdf"}]

I found several highly relevant research papers on this topic. Here's a summary of the search results:

## Key Findings on Representation Steering and Knowledge Conflicts

**SPARE (SAE-Based Representation Engineering):**
A NAACL 2024 paper presents SPARE, a training-free method using Sparse Auto-Encoders to steer LLM knowledge selection. Large language models store significant factual knowledge, but this parametric knowledge can conflict with contextual information, leading to undesirable outputs. The method edits LLM internal activations at inference time by removing features that steer undesired behaviors and adding features that promote desired ones, using orthogonal SAE activations.

**Broader Representation Engineering Landscape:**
Activation steering can simultaneously enforce multiple instruction constraints by applying composite activation vectors during inference. Recent work extends representation engineering by using sparse auto-encoders to resolve context–memory conflicts.

**Foundational Concepts:**
Features and concepts are represented as linear directions in the activation space of LLMs. Steering vectors are computed based on paired input demonstrations that differ by a specific feature and are then used to steer the LLM towards a desired behavior.

The search results include papers from 2024-2025, with comprehensive surveys and specific applications focusing on knowledge conflicts and activation editing techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "6cbf38ba-19e1-49fd-9770-c1c130a3dde4",
  "tool_use_result": {
    "query": "\"representation steering\" \"knowledge conflict\" LLM activation editing 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JQZhapLv9R5QZL3ViVpyGz",
        "content": [
          {
            "title": "Steering Knowledge Selection Behaviours in LLMs",
            "url": "https://arxiv.org/pdf/2410.15999"
          },
          {
            "title": "[Quick Review] Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation Engineering",
            "url": "https://liner.com/review/steering-knowledge-selection-behaviours-in-llms-via-saebased-representation-engineering"
          },
          {
            "title": "arXiv:2502.19649v3 [cs.LG] 12 Mar 2025 - Jan Wehner",
            "url": "https://janwehner.com/files/representation_engineering.pdf"
          },
          {
            "title": "Steering MoE LLMs via Expert (De)Activation",
            "url": "https://arxiv.org/html/2509.09660v1"
          },
          {
            "title": "Representation Engineering for Large-Language Models: Survey and Research Challenges",
            "url": "https://arxiv.org/html/2502.17601v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/c4d26a95fd83f8e590f81c54ae670b5d-Paper-Conference.pdf"
          },
          {
            "title": "psa: differentially private steering for large language model ...",
            "url": "https://arxiv.org/pdf/2501.18532"
          },
          {
            "title": "Representation Bending for Large Language Model Safety",
            "url": "https://aclanthology.org/2025.acl-long.1173.pdf"
          }
        ]
      },
      "I found several highly relevant research papers on this topic. Here's a summary of the search results:\n\n## Key Findings on Representation Steering and Knowledge Conflicts\n\n**SPARE (SAE-Based Representation Engineering):**\nA NAACL 2024 paper presents SPARE, a training-free method using Sparse Auto-Encoders to steer LLM knowledge selection. Large language models store significant factual knowledge, but this parametric knowledge can conflict with contextual information, leading to undesirable outputs. The method edits LLM internal activations at inference time by removing features that steer undesired behaviors and adding features that promote desired ones, using orthogonal SAE activations.\n\n**Broader Representation Engineering Landscape:**\nActivation steering can simultaneously enforce multiple instruction constraints by applying composite activation vectors during inference. Recent work extends representation engineering by using sparse auto-encoders to resolve context–memory conflicts.\n\n**Foundational Concepts:**\nFeatures and concepts are represented as linear directions in the activation space of LLMs. Steering vectors are computed based on paired input demonstrations that differ by a specific feature and are then used to steer the LLM towards a desired behavior.\n\nThe search results include papers from 2024-2025, with comprehensive surveys and specific applications focusing on knowledge conflicts and activation editing techniques."
    ],
    "durationSeconds": 8.188362296
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T14:05:49.617Z_

<details><summary>↩ Tool result · `toolu_01Y6GVEBNKF3YLMf4Am7yC3k`</summary>

```text
Web search results for query: "arxiv 2407.21783 "The Llama 3 Herd of Models" Meta"

Links: [{"title":"The Llama 3 Herd of Models. Paper Review | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/the-llama-3-herd-of-models-2f62252ce1c8"},{"title":"(PDF) The Llama 3 Herd of Models","url":"https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"},{"title":"The Llama 3 Herd of Models Llama Team, AI @ Meta1","url":"https://arxiv.org/pdf/2407.21783"},{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"[2407.21783v1] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v1"},{"title":"[2407.21783v2] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v2"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"The Llama 3 herd of models - Archive ouverte HAL","url":"https://hal.science/hal-05414211"}]

I found the paper! Here are the key details about arxiv 2407.21783:

**Title:** The Llama 3 Herd of Models

**Content Overview:**
This paper presents a new set of foundation models, called Llama 3. It is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage.

**Key Technical Details:**
- The largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens.
- Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks.

**Release:**
Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and Llama Guard 3 model for input and output safety, is publicly released.

**Additional Capabilities:**
The paper also presents the results of experiments in which image, video, and speech capabilities are integrated into Llama 3 via a compositional approach.

The paper was submitted on July 31, 2024, with the latest version (v3) dated November 23, 2024. You can access it directly at https://arxiv.org/abs/2407.21783.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "f097bc6a-6f51-4f3d-a72e-257b2d04eec9",
  "tool_use_result": {
    "query": "arxiv 2407.21783 \"The Llama 3 Herd of Models\" Meta",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Lhchos5Zg3Yzp9J3TEGkGT",
        "content": [
          {
            "title": "The Llama 3 Herd of Models. Paper Review | by Eleventh Hour Enthusiast | Medium",
            "url": "https://medium.com/@EleventhHourEnthusiast/the-llama-3-herd-of-models-2f62252ce1c8"
          },
          {
            "title": "(PDF) The Llama 3 Herd of Models",
            "url": "https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"
          },
          {
            "title": "The Llama 3 Herd of Models Llama Team, AI @ Meta1",
            "url": "https://arxiv.org/pdf/2407.21783"
          },
          {
            "title": "[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv",
            "url": "https://ar5iv.labs.arxiv.org/html/2407.21783"
          },
          {
            "title": "[2407.21783] The Llama 3 Herd of Models",
            "url": "https://arxiv.org/abs/2407.21783"
          },
          {
            "title": "[2407.21783v1] The Llama 3 Herd of Models",
            "url": "https://arxiv.org/abs/2407.21783v1"
          },
          {
            "title": "[2407.21783v2] The Llama 3 Herd of Models",
            "url": "https://arxiv.org/abs/2407.21783v2"
          },
          {
            "title": "The Llama 3 Herd of Models - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"
          },
          {
            "title": "The Llama 3 herd of models - Archive ouverte HAL",
            "url": "https://hal.science/hal-05414211"
          }
        ]
      },
      "I found the paper! Here are the key details about arxiv 2407.21783:\n\n**Title:** The Llama 3 Herd of Models\n\n**Content Overview:**\nThis paper presents a new set of foundation models, called Llama 3. It is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage.\n\n**Key Technical Details:**\n- The largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens.\n- Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks.\n\n**Release:**\nLlama 3, including pre-trained and post-trained versions of the 405B parameter language model and Llama Guard 3 model for input and output safety, is publicly released.\n\n**Additional Capabilities:**\nThe paper also presents the results of experiments in which image, video, and speech capabilities are integrated into Llama 3 via a compositional approach.\n\nThe paper was submitted on July 31, 2024, with the latest version (v3) dated November 23, 2024. You can access it directly at https://arxiv.org/abs/2407.21783."
    ],
    "durationSeconds": 7.507509793999998
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me search for a few more papers to fill out the clusters:

1. For Cluster 5, I need to find more recent steering papers. Let me search for the Wehner et al. 2025 "Representation Engineering" survey that appeared in the search results, and any other recent work.

2. For Cluster 6, I have XNLI, COMET, Llama 3, and Qwen 2.5. Let me also search for COMET-22 specifically.

Let me also verify the COMET paper venue more precisely.

Let me now search for:


- The exact authors and venue for the Rei et al. COMET paper from EMNLP 2020
- The COMET-22 update
- Any additional steering papers that use probe directions
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "28da2f6c-aa07-4f70-a415-15c2c4d07031",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHApVkVuAAfkNgKTXrRRGZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10517,
      "cache_read_input_tokens": 28950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10517
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

Now let me search for a few more specific papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "f2761693-6500-4906-bbf3-c85525c48f89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHApVkVuAAfkNgKTXrRRGZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10517,
      "cache_read_input_tokens": 28950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10517
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WyXpazJrZptqoiefrwMm87`</summary>

```json
{
  "query": "Rei Stewart Farinha Lavie \"COMET: A Neural Framework for MT Evaluation\" EMNLP 2020 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "09e4a48e-2965-4ee1-97fa-35c3d05bad14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHApVkVuAAfkNgKTXrRRGZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10517,
      "cache_read_input_tokens": 28950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10517
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DkwNZGq8F9chj9xb3Bzr1r`</summary>

```json
{
  "query": "\"activation steering\" \"probe direction\" \"residual stream\" LLM 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "89e0c512-5a96-45d6-bf68-7e8602a00110",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHApVkVuAAfkNgKTXrRRGZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10517,
      "cache_read_input_tokens": 28950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10517
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

_source line 35_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FzskF97nbH33LFfnERx9pg`</summary>

```json
{
  "query": "Conneau et al 2018 XNLI authors full list EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "b24702e8-c5be-451b-9990-c7250719c46d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LHApVkVuAAfkNgKTXrRRGZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10517,
      "cache_read_input_tokens": 28950,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10517
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

_source line 36 · 2026-05-22T14:06:01.506Z_

<details><summary>↩ Tool result · `toolu_01WyXpazJrZptqoiefrwMm87`</summary>

```text
Web search results for query: "Rei Stewart Farinha Lavie "COMET: A Neural Framework for MT Evaluation" EMNLP 2020 authors"

Links: [{"title":"EMNLP2020: COMET: A Neural Framework for MT Evaluation","url":"https://virtual.2020.emnlp.org/paper_main.835.html"},{"title":"COMET: A Neural Framework for MT Evaluation - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.213/"},{"title":"[Quick Review] COMET: A Neural Framework for MT Evaluation","url":"https://liner.com/review/comet-neural-framework-for-mt-evaluation"},{"title":"[PDF] COMET: A Neural Framework for MT Evaluation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/COMET:-A-Neural-Framework-for-MT-Evaluation-Rei-Stewart/9e67b9758520e49016ab66bafb974d2e1ed762d1"},{"title":"Aclanthology","url":"https://aclanthology.org/2020.emnlp-main.213.bib"},{"title":"dblp: COMET: A Neural Framework for MT Evaluation.","url":"https://dblp.org/rec/conf/emnlp/ReiSFL20.html"},{"title":"COMET: A Neural Framework for MT Evaluation","url":"https://arxiv.org/pdf/2009.09025"},{"title":"(PDF) COMET: A Neural Framework for MT Evaluation","url":"https://www.researchgate.net/publication/347234911_COMET_A_Neural_Framework_for_MT_Evaluation"},{"title":"6.53 MATEO: MACHINE TRANSLATION EVALUATION ONLINE Bram Vanroy","url":"https://www.clarin.eu/sites/default/files/CLARIN2023_P2.3.1_Vanroy.pdf"},{"title":"Pitfalls and Outlooks in Using COMET","url":"https://www2.statmt.org/wmt24/pdf/2024.wmt-1.121.pdf"}]

Based on the search results, the authors of "COMET: A Neural Framework for MT Evaluation" (EMNLP 2020) are Ricardo Rei, Craig Stewart, Ana C Farinha, and Alon Lavie.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "28800d82-52a0-483b-a90c-6ab2bc83f980",
  "tool_use_result": {
    "query": "Rei Stewart Farinha Lavie \"COMET: A Neural Framework for MT Evaluation\" EMNLP 2020 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UqZKsnrDTCMYatbPm9aBQU",
        "content": [
          {
            "title": "EMNLP2020: COMET: A Neural Framework for MT Evaluation",
            "url": "https://virtual.2020.emnlp.org/paper_main.835.html"
          },
          {
            "title": "COMET: A Neural Framework for MT Evaluation - ACL Anthology",
            "url": "https://aclanthology.org/2020.emnlp-main.213/"
          },
          {
            "title": "[Quick Review] COMET: A Neural Framework for MT Evaluation",
            "url": "https://liner.com/review/comet-neural-framework-for-mt-evaluation"
          },
          {
            "title": "[PDF] COMET: A Neural Framework for MT Evaluation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/COMET:-A-Neural-Framework-for-MT-Evaluation-Rei-Stewart/9e67b9758520e49016ab66bafb974d2e1ed762d1"
          },
          {
            "title": "Aclanthology",
            "url": "https://aclanthology.org/2020.emnlp-main.213.bib"
          },
          {
            "title": "dblp: COMET: A Neural Framework for MT Evaluation.",
            "url": "https://dblp.org/rec/conf/emnlp/ReiSFL20.html"
          },
          {
            "title": "COMET: A Neural Framework for MT Evaluation",
            "url": "https://arxiv.org/pdf/2009.09025"
          },
          {
            "title": "(PDF) COMET: A Neural Framework for MT Evaluation",
            "url": "https://www.researchgate.net/publication/347234911_COMET_A_Neural_Framework_for_MT_Evaluation"
          },
          {
            "title": "6.53 MATEO: MACHINE TRANSLATION EVALUATION ONLINE Bram Vanroy",
            "url": "https://www.clarin.eu/sites/default/files/CLARIN2023_P2.3.1_Vanroy.pdf"
          },
          {
            "title": "Pitfalls and Outlooks in Using COMET",
            "url": "https://www2.statmt.org/wmt24/pdf/2024.wmt-1.121.pdf"
          }
        ]
      },
      "Based on the search results, the authors of \"COMET: A Neural Framework for MT Evaluation\" (EMNLP 2020) are Ricardo Rei, Craig Stewart, Ana C Farinha, and Alon Lavie."
    ],
    "durationSeconds": 3.764933935000001
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-22T14:06:03.465Z_

<details><summary>↩ Tool result · `toolu_01FzskF97nbH33LFfnERx9pg`</summary>

```text
Web search results for query: "Conneau et al 2018 XNLI authors full list EMNLP"

Links: [{"title":"XNLI: Evaluating Cross-lingual Sentence Representations - ACL Anthology","url":"https://aclanthology.org/D18-1269/"},{"title":"dblp: XNLI: Evaluating Cross-lingual Sentence Representations.","url":"https://dblp.org/rec/conf/emnlp/ConneauRLWBSS18.html"},{"title":"(PDF) XNLI: Evaluating Cross-lingual Sentence Representations","url":"https://www.academia.edu/74401248/XNLI_Evaluating_Cross_lingual_Sentence_Representations?uc-g-sw=56434755"},{"title":"XNLI: Evaluating Cross-lingual Sentence Representations","url":"https://arxiv.org/pdf/1809.05053"},{"title":"XNLI","url":"https://cims.nyu.edu/~sbowman/xnli/"},{"title":"[1809.05053] XNLI: Evaluating Cross-lingual Sentence Representations","url":"https://arxiv.org/abs/1809.05053"},{"title":"[PDF] XNLI: Evaluating Cross-lingual Sentence Representations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XNLI:-Evaluating-Cross-lingual-Sentence-Conneau-Lample/1c3112ef8a346b9817382ed34a8c146c53d5bcf5"},{"title":"XNLI: Evaluating Cross-lingual Sentence Representations | Request PDF","url":"https://www.researchgate.net/publication/334118044_XNLI_Evaluating_Cross-lingual_Sentence_Representations"},{"title":"GitHub - facebookresearch/XNLI: Evaluating Cross-lingual Sentence Representations · GitHub","url":"https://github.com/facebookresearch/XNLI"}]

The full list of authors for the Conneau et al. 2018 XNLI paper published at EMNLP is: Alexis Conneau, Ruty Rinott, Guillaume Lample, Adina Williams, Samuel Bowman, Holger Schwenk, and Veselin Stoyanov.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "9f668184-5188-41f3-b96a-32ff3df08488",
  "tool_use_result": {
    "query": "Conneau et al 2018 XNLI authors full list EMNLP",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F8867BgGm4EQqw7SmifLBn",
        "content": [
          {
            "title": "XNLI: Evaluating Cross-lingual Sentence Representations - ACL Anthology",
            "url": "https://aclanthology.org/D18-1269/"
          },
          {
            "title": "dblp: XNLI: Evaluating Cross-lingual Sentence Representations.",
            "url": "https://dblp.org/rec/conf/emnlp/ConneauRLWBSS18.html"
          },
          {
            "title": "(PDF) XNLI: Evaluating Cross-lingual Sentence Representations",
            "url": "https://www.academia.edu/74401248/XNLI_Evaluating_Cross_lingual_Sentence_Representations?uc-g-sw=56434755"
          },
          {
            "title": "XNLI: Evaluating Cross-lingual Sentence Representations",
            "url": "https://arxiv.org/pdf/1809.05053"
          },
          {
            "title": "XNLI",
            "url": "https://cims.nyu.edu/~sbowman/xnli/"
          },
          {
            "title": "[1809.05053] XNLI: Evaluating Cross-lingual Sentence Representations",
            "url": "https://arxiv.org/abs/1809.05053"
          },
          {
            "title": "[PDF] XNLI: Evaluating Cross-lingual Sentence Representations | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/XNLI:-Evaluating-Cross-lingual-Sentence-Conneau-Lample/1c3112ef8a346b9817382ed34a8c146c53d5bcf5"
          },
          {
            "title": "XNLI: Evaluating Cross-lingual Sentence Representations | Request PDF",
            "url": "https://www.researchgate.net/publication/334118044_XNLI_Evaluating_Cross-lingual_Sentence_Representations"
          },
          {
            "title": "GitHub - facebookresearch/XNLI: Evaluating Cross-lingual Sentence Representations · GitHub",
            "url": "https://github.com/facebookresearch/XNLI"
          }
        ]
      },
      "The full list of authors for the Conneau et al. 2018 XNLI paper published at EMNLP is: Alexis Conneau, Ruty Rinott, Guillaume Lample, Adina Williams, Samuel Bowman, Holger Schwenk, and Veselin Stoyanov."
    ],
    "durationSeconds": 4.138995301999996
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T14:06:07.106Z_

<details><summary>↩ Tool result · `toolu_01DkwNZGq8F9chj9xb3Bzr1r`</summary>

```text
Web search results for query: ""activation steering" "probe direction" "residual stream" LLM 2024 2025 2026"

Links: [{"title":"Activation Steering in LLMs","url":"https://www.emergentmind.com/topics/activation-steering-method"},{"title":"Steered LLM Activations are Non-Surjective","url":"https://arxiv.org/html/2604.09839v1"},{"title":"Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection","url":"https://arxiv.org/html/2604.28129v1"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"Published as a conference paper at ICLR 2026 FINE-GRAINED ACTIVATION STEERING:","url":"https://openreview.net/pdf?id=guSVafqhrB"},{"title":"Steering Awareness: Models Can Be Trained to Detect Activation Steering","url":"https://arxiv.org/html/2511.21399v2"},{"title":"Activation Steering for Masked Diffusion Language Models","url":"https://arxiv.org/pdf/2512.24143"},{"title":"Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/pdf/2602.04428"},{"title":"Steer Like the LLM: Activation Steering that Mimics Prompting","url":"https://arxiv.org/html/2605.03907v1"}]

I've completed the web search for your query. Here are the key findings about activation steering, probe directions, and residual streams in LLMs from 2024-2026:

## Recent Developments in Activation Steering

**Core Concepts:**
Activation steering can reliably modify model behavior by adding directions to internal representations, most commonly the residual stream, enabling interventions that induce or suppress refusal and even override alignment behaviors.

**Technical Advances:**

Feature-Space Steering uses sparse autoencoders to disentangle and precisely target interpretable features in SAE latent space (Feature Guided Activation Additions—FGAA).

In music generation, regression-trained linear probes on the residual stream yield robust direction vectors for style, timbre, and genre transfer, outperforming classification-trained probes.

**Recent Methods (2025-2026):**

Conceptor-based steering replaces additive vectors with soft projection matrices derived from conceptor theory, with Boolean operations over conceptors allowing compositional multi-goal steering.

Adaptive/PID steering frames the problem as a control system with proportional, integral, and derivative terms managing injection strength dynamically, handling the strength degradation over long generation problem.

**Steering Awareness:**
A model is steering-aware if, given a prompt and a residual-stream intervention that adds a vector at a fixed layer and token position, it can report whether an injection occurred and identify the injected concept.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "1e996d56-d16d-49d9-9760-19a71a22563f",
  "tool_use_result": {
    "query": "\"activation steering\" \"probe direction\" \"residual stream\" LLM 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012QUmCMCJ3fMCMxjkMZDP2d",
        "content": [
          {
            "title": "Activation Steering in LLMs",
            "url": "https://www.emergentmind.com/topics/activation-steering-method"
          },
          {
            "title": "Steered LLM Activations are Non-Surjective",
            "url": "https://arxiv.org/html/2604.09839v1"
          },
          {
            "title": "Latent Adversarial Detection: Adaptive Probing of LLM Activations for Multi-Turn Attack Detection",
            "url": "https://arxiv.org/html/2604.28129v1"
          },
          {
            "title": "Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 FINE-GRAINED ACTIVATION STEERING:",
            "url": "https://openreview.net/pdf?id=guSVafqhrB"
          },
          {
            "title": "Steering Awareness: Models Can Be Trained to Detect Activation Steering",
            "url": "https://arxiv.org/html/2511.21399v2"
          },
          {
            "title": "Activation Steering for Masked Diffusion Language Models",
            "url": "https://arxiv.org/pdf/2512.24143"
          },
          {
            "title": "Fine-Grained Activation Steering: Steering Less, Achieving More",
            "url": "https://arxiv.org/pdf/2602.04428"
          },
          {
            "title": "Steer Like the LLM: Activation Steering that Mimics Prompting",
            "url": "https://arxiv.org/html/2605.03907v1"
          }
        ]
      },
      "I've completed the web search for your query. Here are the key findings about activation steering, probe directions, and residual streams in LLMs from 2024-2026:\n\n## Recent Developments in Activation Steering\n\n**Core Concepts:**\nActivation steering can reliably modify model behavior by adding directions to internal representations, most commonly the residual stream, enabling interventions that induce or suppress refusal and even override alignment behaviors.\n\n**Technical Advances:**\n\nFeature-Space Steering uses sparse autoencoders to disentangle and precisely target interpretable features in SAE latent space (Feature Guided Activation Additions—FGAA).\n\nIn music generation, regression-trained linear probes on the residual stream yield robust direction vectors for style, timbre, and genre transfer, outperforming classification-trained probes.\n\n**Recent Methods (2025-2026):**\n\nConceptor-based steering replaces additive vectors with soft projection matrices derived from conceptor theory, with Boolean operations over conceptors allowing compositional multi-goal steering.\n\nAdaptive/PID steering frames the problem as a control system with proportional, integral, and derivative terms managing injection strength dynamically, handling the strength degradation over long generation problem.\n\n**Steering Awareness:**\nA model is steering-aware if, given a prompt and a residual-stream intervention that adds a vector at a fixed layer and token position, it can report whether an injection occurred and identify the injected concept."
    ],
    "durationSeconds": 8.422310293999995
  }
}
```

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the "Fine-Grained Activation Steering" ICLR 2026 paper since it's very recent and relevant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "86bf5189-fa31-4592-8b6a-bfb91f170bd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PtPtdPsJe6fDk79rSnM2f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 644,
      "cache_creation_input_tokens": 1838,
      "cache_read_input_tokens": 39467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1838
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

_source line 40_

Let me search for the Fine-Grained Activation Steering paper at ICLR 2026 which looks very relevant.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "07c2eaf6-ae59-4985-b144-531be7250d6a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PtPtdPsJe6fDk79rSnM2f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 644,
      "cache_creation_input_tokens": 1838,
      "cache_read_input_tokens": 39467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1838
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

_source line 41_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P6ZaxhaqwKy2JCKxRTKBGE`</summary>

```json
{
  "query": "\"Fine-Grained Activation Steering\" ICLR 2026 authors arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "a38ba015-455a-4242-94e3-e9f3df93287d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PtPtdPsJe6fDk79rSnM2f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 644,
      "cache_creation_input_tokens": 1838,
      "cache_read_input_tokens": 39467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1838
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

_source line 42_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014r6AYUeATAN5FimUj9B9mj`</summary>

```json
{
  "query": "Qwen2.5 technical report authors \"Yang\" arxiv 2412.15115"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "329ea064-d65f-46ac-9534-06d6e3d3d15a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016PtPtdPsJe6fDk79rSnM2f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 644,
      "cache_creation_input_tokens": 1838,
      "cache_read_input_tokens": 39467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1838
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

_source line 43 · 2026-05-22T14:06:18.046Z_

<details><summary>↩ Tool result · `toolu_01P6ZaxhaqwKy2JCKxRTKBGE`</summary>

```text
Web search results for query: ""Fine-Grained Activation Steering" ICLR 2026 authors arxiv"

Links: [{"title":"Published as a conference paper at ICLR 2026 FINE-GRAINED ACTIVATION STEERING:","url":"https://openreview.net/pdf?id=guSVafqhrB"},{"title":"FINE-GRAINED ACTIVATION STEERING","url":"https://openreview.net/pdf/a9cada056ebe41df04f02a22bc25b2fe3d125857.pdf"},{"title":"Activation Steering with a Feedback Controller","url":"https://arxiv.org/pdf/2510.04309"},{"title":"Activation Steering for Masked Diffusion Language Models","url":"https://arxiv.org/pdf/2512.24143"},{"title":"[2602.04428] Fine-Grained Activation Steering: Steering Less, Achieving More","url":"https://arxiv.org/abs/2602.04428"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2603.06745"},{"title":"Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra","url":"https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"},{"title":"[2505.12189] Mitigating Content Effects on Reasoning in Language Models through Fine-Grained Activation Steering","url":"https://arxiv.org/abs/2505.12189"}]

Based on the search results, I found the paper "Fine-Grained Activation Steering: Steering Less, Achieving More" that was published at ICLR 2026.

The authors are: Zijian Feng, Tianjiao Li, Zixiao Zhu, Hanzhang Zhou, Junlang Qian, Li Zhang, Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng, and Kezhi Mao.

The paper decomposes block activations into fine-grained atomic unit (AU)-level activations, where each AU-level activation corresponds to a single dimension of the block activation. The research reveals that block-level activations are inherently heterogeneous, entangling beneficial, irrelevant, and harmful features, thereby rendering block-level steering coarse, inefficient, and intrusive.

The arXiv preprint is available at arXiv:2602.04428, submitted on February 4, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "010bbdde-305c-49e1-8be9-3d5a789dd4c0",
  "tool_use_result": {
    "query": "\"Fine-Grained Activation Steering\" ICLR 2026 authors arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VfRcVuo8frtbLZcy7BU55s",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 FINE-GRAINED ACTIVATION STEERING:",
            "url": "https://openreview.net/pdf?id=guSVafqhrB"
          },
          {
            "title": "FINE-GRAINED ACTIVATION STEERING",
            "url": "https://openreview.net/pdf/a9cada056ebe41df04f02a22bc25b2fe3d125857.pdf"
          },
          {
            "title": "Activation Steering with a Feedback Controller",
            "url": "https://arxiv.org/pdf/2510.04309"
          },
          {
            "title": "Activation Steering for Masked Diffusion Language Models",
            "url": "https://arxiv.org/pdf/2512.24143"
          },
          {
            "title": "[2602.04428] Fine-Grained Activation Steering: Steering Less, Achieving More",
            "url": "https://arxiv.org/abs/2602.04428"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2603.06745"
          },
          {
            "title": "Activation Steering in 2026: A Practitioner's Field Guide | Subhadip Mitra",
            "url": "https://subhadipmitra.com/blog/2026/activation-steering-field-guide/"
          },
          {
            "title": "[2505.12189] Mitigating Content Effects on Reasoning in Language Models through Fine-Grained Activation Steering",
            "url": "https://arxiv.org/abs/2505.12189"
          }
        ]
      },
      "Based on the search results, I found the paper \"Fine-Grained Activation Steering: Steering Less, Achieving More\" that was published at ICLR 2026.\n\nThe authors are: Zijian Feng, Tianjiao Li, Zixiao Zhu, Hanzhang Zhou, Junlang Qian, Li Zhang, Jia Jim Deryl Chua, Lee Onn Mak, Gee Wah Ng, and Kezhi Mao.\n\nThe paper decomposes block activations into fine-grained atomic unit (AU)-level activations, where each AU-level activation corresponds to a single dimension of the block activation. The research reveals that block-level activations are inherently heterogeneous, entangling beneficial, irrelevant, and harmful features, thereby rendering block-level steering coarse, inefficient, and intrusive.\n\nThe arXiv preprint is available at arXiv:2602.04428, submitted on February 4, 2026."
    ],
    "durationSeconds": 6.387459386000002
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-22T14:06:19.333Z_

<details><summary>↩ Tool result · `toolu_014r6AYUeATAN5FimUj9B9mj`</summary>

```text
Web search results for query: "Qwen2.5 technical report authors "Yang" arxiv 2412.15115"

Links: [{"title":"[2412.15115] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115"},{"title":"[2412.15115v1] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115v1"},{"title":"[2412.15115v2] Qwen2.5 Technical Report","url":"https://arxiv.org/abs/2412.15115v2"},{"title":"[PDF] Qwen2.5 Technical Report | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Qwen2.5-Technical-Report-Yang-Yang/88aa6b1f37d1fd8e0a40499ce9bb87873f03aaa8"},{"title":"Qwen2.5 Technical Report","url":"https://bibbase.org/network/publication/qwen-yang-yang-zhang-hui-zheng-yu-li-etal-qwen25technicalreport-2025"},{"title":"Paper page - Qwen2.5 Technical Report","url":"https://huggingface.co/papers/2412.15115"},{"title":"dblp: Qwen2.5 Technical Report.","url":"https://dblp.org/rec/journals/corr/abs-2412-15115.html"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"}]

Based on the search results, I found the authors of the Qwen2.5 Technical Report (arXiv:2412.15115). The authors include An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tianyi Tang, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu, with additional authors not shown in the abstract.

Several authors with the surname "Yang" are listed among the co-authors: An Yang, Baosong Yang, Jian Yang, Jianxin Yang, Jiaxi Yang, Kexin Yang, Yang Fan, and Yang Su.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "e8612431-2b3b-4e08-8026-6b1298fd66b7",
  "tool_use_result": {
    "query": "Qwen2.5 technical report authors \"Yang\" arxiv 2412.15115",
    "results": [
      {
        "tool_use_id": "srvtoolu_012cvL2gS7etU7LoHVMbz7UR",
        "content": [
          {
            "title": "[2412.15115] Qwen2.5 Technical Report",
            "url": "https://arxiv.org/abs/2412.15115"
          },
          {
            "title": "[2412.15115v1] Qwen2.5 Technical Report",
            "url": "https://arxiv.org/abs/2412.15115v1"
          },
          {
            "title": "[2412.15115v2] Qwen2.5 Technical Report",
            "url": "https://arxiv.org/abs/2412.15115v2"
          },
          {
            "title": "[PDF] Qwen2.5 Technical Report | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Qwen2.5-Technical-Report-Yang-Yang/88aa6b1f37d1fd8e0a40499ce9bb87873f03aaa8"
          },
          {
            "title": "Qwen2.5 Technical Report",
            "url": "https://bibbase.org/network/publication/qwen-yang-yang-zhang-hui-zheng-yu-li-etal-qwen25technicalreport-2025"
          },
          {
            "title": "Paper page - Qwen2.5 Technical Report",
            "url": "https://huggingface.co/papers/2412.15115"
          },
          {
            "title": "dblp: Qwen2.5 Technical Report.",
            "url": "https://dblp.org/rec/journals/corr/abs-2412-15115.html"
          },
          {
            "title": "2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen",
            "url": "https://arxiv.org/pdf/2412.15115"
          }
        ]
      },
      "Based on the search results, I found the authors of the Qwen2.5 Technical Report (arXiv:2412.15115). The authors include An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tianyi Tang, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu, with additional authors not shown in the abstract.\n\nSeveral authors with the surname \"Yang\" are listed among the co-authors: An Yang, Baosong Yang, Jian Yang, Jianxin Yang, Jiaxi Yang, Kexin Yang, Yang Fan, and Yang Su."
    ],
    "durationSeconds": 7.0348793540000045
  }
}
```

</details>

---

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the papers to add:

### Cluster 5: Steering & Causal Intervention

1. **li2023iti** - Li et al. 2023, "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model", NeurIPS 2023
   - Authors: Kenneth Li, Oam Patel, Fernanda Viégas, Hanspeter Pfister, Martin Wattenberg
   - URL: https://arxiv.org/abs/2306.03341
   - Category: steering
   - Role: foundation

2. **zou2023representation** - Zou et al. 2023, "Representation Engineering: A Top-Down Approach to AI Transparency", arXiv
   - Authors: Andy Zou, Long Phan, et al.
   - URL: https://arxiv.org/abs/2310.01405
   - Category: steering
   - Role: foundation

3. **feng2026finegrained** - Feng et al. 2026, "Fine-Grained Activation Steering: Steering Less, Achieving More", ICLR 2026
   - Authors: Zijian Feng, Tianjiao Li, Zixiao Zhu, et al.
   - URL: https://arxiv.org/abs/2602.04428
   - Category: steering
   - Role: methodology

Now moving into datasets and evaluation tools, starting with cross-lingual evaluation frameworks and neural machine translation metrics.

Continuing with major language model releases—the Llama 3 family and Qwen 2.5 technical reports that serve as foundational references for understanding current model capabilities.

Now I'm verifying the existing collection of 22 papers to make sure there are no duplicates before finalizing the bibliography.

I need to add at least 6 more papers to reach 28 total. I'm planning to include papers from different clusters: three from Cluster 5 focusing on representation learning and interpretability, and four from Cluster 6 covering cross-lingual evaluation and quality metrics. This would bring the total to 29 papers. Let me double-check the author information for the Zou et al. 2023 paper to ensure accuracy.

Now I'm looking at the full author list for that paper and need to finalize the YAML entries. For the Llama 3 paper, I should verify the proper citation format—the paper lists "Llama Team, AI @ Meta" as the author, though Semantic Scholar attributes it to Aaron Grattafiori and others. I'll settle on a reasonable citation convention for consistency.

Looking at how the existing file handles team-authored papers like `team2026qwen`, I should apply the same pattern here. For the Qwen2.5 technical report, I need to distinguish it from the Qwen-Scope SAE paper that's already in the file, so I'll use `yang2024qwen25` instead. I also need to verify the publication details for the Zou et al. paper, which appeared on arXiv in 2023.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "ae3a1cc1-d218-44ed-b133-b35ad59741d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmLzN9UBZygaAqKvReKRqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2332,
      "cache_read_input_tokens": 41305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2332
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

_source line 46_

I have all the information needed. Now I'll add the 7 new papers to the literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "4780dc44-82b1-47f5-a6cf-8bc49a64dea9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmLzN9UBZygaAqKvReKRqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2332,
      "cache_read_input_tokens": 41305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2332
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

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01Ct9LoWQZu7GjS1qJfezQJN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
  "offset": 465,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "8eebfb44-0ba1-40aa-93cb-bb1546a1aa09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmLzN9UBZygaAqKvReKRqd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2332,
      "cache_read_input_tokens": 41305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2332
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

_source line 48 · 2026-05-22T14:06:55.121Z_

<details><summary>↩ Tool result · `toolu_01Ct9LoWQZu7GjS1qJfezQJN`</summary>

```text
465	      in the Age of Neural Networks'
466	    url: https://arxiv.org/abs/2204.06815
467	    venue: arXiv
468	    verified: true
469	    year: 2022
470	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "113ce3cb-ac53-4a8e-9079-abf3713f4287",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
      "content": "      in the Age of Neural Networks'\n    url: https://arxiv.org/abs/2204.06815\n    venue: arXiv\n    verified: true\n    year: 2022\n",
      "numLines": 6,
      "startLine": 465,
      "totalLines": 470
    }
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Edit · `toolu_01GuMTCcsuae7VCN8zXZFrJr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
  "old_string": "    year: 2022\n",
  "new_string": "    year: 2022\n  li2023iti:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Li, K.\n    - Patel, O.\n    - \"Vi\\xE9gas, F.\"\n    - Pfister, H.\n    - Wattenberg, M.\n    bibtex_key: li2023iti\n    category: steering\n    doi: ''\n    relevance: Inference-Time Intervention shifts activations along truthful directions\n      in attention heads to improve truthfulness. Foundational activation steering method\n      our causal intervention approach builds on.\n    role: foundation\n    title: 'Inference-Time Intervention: Eliciting Truthful Answers from a Language\n      Model'\n    url: https://arxiv.org/abs/2306.03341\n    venue: NeurIPS 2023\n    verified: true\n    year: 2023\n  zou2023representation:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Zou, A.\n    - Phan, L.\n    - Chen, S.\n    - Campbell, J.\n    - Guo, P.\n    - Ren, R.\n    - Pan, A.\n    - et al.\n    bibtex_key: zou2023representation\n    category: steering\n    doi: ''\n    relevance: Introduces Representation Engineering (RepE) framework using population-level\n      representations for monitoring and manipulating high-level cognitive phenomena.\n      Foundational paradigm for our steering methodology.\n    role: foundation\n    title: 'Representation Engineering: A Top-Down Approach to AI Transparency'\n    url: https://arxiv.org/abs/2310.01405\n    venue: arXiv\n    verified: true\n    year: 2023\n  feng2026finegrained:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Feng, Z.\n    - Li, T.\n    - Zhu, Z.\n    - Zhou, H.\n    - Qian, J.\n    - Zhang, L.\n    - Mao, K.\n    bibtex_key: feng2026finegrained\n    category: steering\n    doi: ''\n    relevance: Decomposes block activations into atomic-unit-level activations for\n      fine-grained steering. Shows block-level steering entangles beneficial and harmful\n      features. Methodological advance relevant to our per-feature steering design.\n    role: methodology\n    title: 'Fine-Grained Activation Steering: Steering Less, Achieving More'\n    url: https://arxiv.org/abs/2602.04428\n    venue: ICLR 2026\n    verified: true\n    year: 2026\n  conneau2018xnli:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Conneau, A.\n    - Rinott, R.\n    - Lample, G.\n    - Williams, A.\n    - Bowman, S.\n    - Schwenk, H.\n    - Stoyanov, V.\n    bibtex_key: conneau2018xnli\n    category: dataset-tool\n    doi: ''\n    relevance: Cross-lingual NLI benchmark spanning 15 languages. Used for evaluating\n      cross-lingual transfer and multilingual understanding in our experiments.\n    role: foundation\n    title: 'XNLI: Evaluating Cross-lingual Sentence Representations'\n    url: https://aclanthology.org/D18-1269/\n    venue: EMNLP 2018\n    verified: true\n    year: 2018\n  rei2020comet:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Rei, R.\n    - Stewart, C.\n    - Farinha, A.C.\n    - Lavie, A.\n    bibtex_key: rei2020comet\n    category: dataset-tool\n    doi: ''\n    relevance: Neural MT evaluation metric using cross-lingual pretrained encoders.\n      Provides translation quality evaluation for our cross-lingual dataset construction\n      pipeline.\n    role: methodology\n    title: 'COMET: A Neural Framework for MT Evaluation'\n    url: https://aclanthology.org/2020.emnlp-main.213/\n    venue: EMNLP 2020\n    verified: true\n    year: 2020\n  grattafiori2024llama:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Grattafiori, A.\n    - et al. (Llama Team, AI @ Meta)\n    bibtex_key: grattafiori2024llama\n    category: dataset-tool\n    doi: ''\n    relevance: Technical report for Llama 3.1 models (8B/70B/405B). One of our primary\n      experimental models. Documents multilingual capabilities and 128K context window.\n    role: foundation\n    title: The Llama 3 Herd of Models\n    url: https://arxiv.org/abs/2407.21783\n    venue: arXiv\n    verified: true\n    year: 2024\n  yang2024qwen25:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Yang, A.\n    - Yang, B.\n    - et al. (Qwen Team)\n    bibtex_key: yang2024qwen25\n    category: dataset-tool\n    doi: ''\n    relevance: Technical report for Qwen2.5 model series. One of our primary experimental\n      models. Documents multilingual pretraining on 18T tokens.\n    role: foundation\n    title: Qwen2.5 Technical Report\n    url: https://arxiv.org/abs/2412.15115\n    venue: arXiv\n    verified: true\n    year: 2024\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "ca899e51-43d2-421a-ac7b-7484b9996d22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FZhrSLMdUp9FLiS5vCGfVk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1894,
      "cache_read_input_tokens": 43637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1894
      },
      "output_tokens": 67,
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

_source line 50 · 2026-05-22T14:07:17.437Z_

<details><summary>↩ Tool result · reported error · `toolu_01GuMTCcsuae7VCN8zXZFrJr`</summary>

```text
&lt;tool_use_error>Found 2 matches of the string to replace, but replace_all is false. To replace all occurrences, set replace_all to true. To replace only one occurrence, please provide more context to uniquely identify the instance.
String:     year: 2022
&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "33bc27f1-3c45-46fa-a179-8ba57889f14f",
  "tool_use_result": "Error: Found 2 matches of the string to replace, but replace_all is false. To replace all occurrences, set replace_all to true. To replace only one occurrence, please provide more context to uniquely identify the instance.\nString:     year: 2022\n"
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Edit · `toolu_017itKs6HBwjV25gUKBVk3vj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
  "old_string": "    url: https://arxiv.org/abs/2204.06815\n    venue: arXiv\n    verified: true\n    year: 2022",
  "new_string": "    url: https://arxiv.org/abs/2204.06815\n    venue: arXiv\n    verified: true\n    year: 2022\n  li2023iti:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Li, K.\n    - Patel, O.\n    - \"Vi\\xE9gas, F.\"\n    - Pfister, H.\n    - Wattenberg, M.\n    bibtex_key: li2023iti\n    category: steering\n    doi: ''\n    relevance: Inference-Time Intervention shifts activations along truthful directions\n      in attention heads to improve truthfulness. Foundational activation steering method\n      our causal intervention approach builds on.\n    role: foundation\n    title: 'Inference-Time Intervention: Eliciting Truthful Answers from a Language\n      Model'\n    url: https://arxiv.org/abs/2306.03341\n    venue: NeurIPS 2023\n    verified: true\n    year: 2023\n  zou2023representation:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Zou, A.\n    - Phan, L.\n    - Chen, S.\n    - Campbell, J.\n    - Guo, P.\n    - Ren, R.\n    - Pan, A.\n    - et al.\n    bibtex_key: zou2023representation\n    category: steering\n    doi: ''\n    relevance: Introduces Representation Engineering (RepE) framework using population-level\n      representations for monitoring and manipulating high-level cognitive phenomena.\n      Foundational paradigm for our steering methodology.\n    role: foundation\n    title: 'Representation Engineering: A Top-Down Approach to AI Transparency'\n    url: https://arxiv.org/abs/2310.01405\n    venue: arXiv\n    verified: true\n    year: 2023\n  feng2026finegrained:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Feng, Z.\n    - Li, T.\n    - Zhu, Z.\n    - Zhou, H.\n    - Qian, J.\n    - Zhang, L.\n    - Mao, K.\n    bibtex_key: feng2026finegrained\n    category: steering\n    doi: ''\n    relevance: Decomposes block activations into atomic-unit-level activations for\n      fine-grained steering. Shows block-level steering entangles beneficial and harmful\n      features. Methodological advance relevant to our per-feature steering design.\n    role: methodology\n    title: 'Fine-Grained Activation Steering: Steering Less, Achieving More'\n    url: https://arxiv.org/abs/2602.04428\n    venue: ICLR 2026\n    verified: true\n    year: 2026\n  conneau2018xnli:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Conneau, A.\n    - Rinott, R.\n    - Lample, G.\n    - Williams, A.\n    - Bowman, S.\n    - Schwenk, H.\n    - Stoyanov, V.\n    bibtex_key: conneau2018xnli\n    category: dataset-tool\n    doi: ''\n    relevance: Cross-lingual NLI benchmark spanning 15 languages. Used for evaluating\n      cross-lingual transfer and multilingual understanding in our experiments.\n    role: foundation\n    title: 'XNLI: Evaluating Cross-lingual Sentence Representations'\n    url: https://aclanthology.org/D18-1269/\n    venue: EMNLP 2018\n    verified: true\n    year: 2018\n  rei2020comet:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Rei, R.\n    - Stewart, C.\n    - Farinha, A.C.\n    - Lavie, A.\n    bibtex_key: rei2020comet\n    category: dataset-tool\n    doi: ''\n    relevance: Neural MT evaluation metric using cross-lingual pretrained encoders.\n      Provides translation quality evaluation for our cross-lingual dataset construction\n      pipeline.\n    role: methodology\n    title: 'COMET: A Neural Framework for MT Evaluation'\n    url: https://aclanthology.org/2020.emnlp-main.213/\n    venue: EMNLP 2020\n    verified: true\n    year: 2020\n  grattafiori2024llama:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Grattafiori, A.\n    - et al. (Llama Team, AI @ Meta)\n    bibtex_key: grattafiori2024llama\n    category: dataset-tool\n    doi: ''\n    relevance: Technical report for Llama 3.1 models (8B/70B/405B). One of our primary\n      experimental models. Documents multilingual capabilities and 128K context window.\n    role: foundation\n    title: The Llama 3 Herd of Models\n    url: https://arxiv.org/abs/2407.21783\n    venue: arXiv\n    verified: true\n    year: 2024\n  yang2024qwen25:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Yang, A.\n    - Yang, B.\n    - et al. (Qwen Team)\n    bibtex_key: yang2024qwen25\n    category: dataset-tool\n    doi: ''\n    relevance: Technical report for Qwen2.5 model series. One of our primary experimental\n      models. Documents multilingual pretraining on 18T tokens.\n    role: foundation\n    title: Qwen2.5 Technical Report\n    url: https://arxiv.org/abs/2412.15115\n    venue: arXiv\n    verified: true\n    year: 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "08354d81-a5a2-48a8-9449-ad9e26af9de4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0157TrfBEd3iZDeTmCGrZhC8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1942,
      "cache_read_input_tokens": 45531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1942
      },
      "output_tokens": 67,
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

_source line 52 · 2026-05-22T14:07:41.703Z_

<details><summary>↩ Tool result · `toolu_017itKs6HBwjV25gUKBVk3vj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "962578df-769d-461b-9947-2f71b5bc3989",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
    "oldString": "    url: https://arxiv.org/abs/2204.06815\n    venue: arXiv\n    verified: true\n    year: 2022",
    "newString": "    url: https://arxiv.org/abs/2204.06815\n    venue: arXiv\n    verified: true\n    year: 2022\n  li2023iti:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Li, K.\n    - Patel, O.\n    - \"Vi\\xE9gas, F.\"\n    - Pfister, H.\n    - Wattenberg, M.\n    bibtex_key: li2023iti\n    category: steering\n    doi: ''\n    relevance: Inference-Time Intervention shifts activations along truthful directions\n      in attention heads to improve truthfulness. Foundational activation steering method\n      our causal intervention approach builds on.\n    role: foundation\n    title: 'Inference-Time Intervention: Eliciting Truthful Answers from a Language\n      Model'\n    url: https://arxiv.org/abs/2306.03341\n    venue: NeurIPS 2023\n    verified: true\n    year: 2023\n  zou2023representation:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Zou, A.\n    - Phan, L.\n    - Chen, S.\n    - Campbell, J.\n    - Guo, P.\n    - Ren, R.\n    - Pan, A.\n    - et al.\n    bibtex_key: zou2023representation\n    category: steering\n    doi: ''\n    relevance: Introduces Representation Engineering (RepE) framework using population-level\n      representations for monitoring and manipulating high-level cognitive phenomena.\n      Foundational paradigm for our steering methodology.\n    role: foundation\n    title: 'Representation Engineering: A Top-Down Approach to AI Transparency'\n    url: https://arxiv.org/abs/2310.01405\n    venue: arXiv\n    verified: true\n    year: 2023\n  feng2026finegrained:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Feng, Z.\n    - Li, T.\n    - Zhu, Z.\n    - Zhou, H.\n    - Qian, J.\n    - Zhang, L.\n    - Mao, K.\n    bibtex_key: feng2026finegrained\n    category: steering\n    doi: ''\n    relevance: Decomposes block activations into atomic-unit-level activations for\n      fine-grained steering. Shows block-level steering entangles beneficial and harmful\n      features. Methodological advance relevant to our per-feature steering design.\n    role: methodology\n    title: 'Fine-Grained Activation Steering: Steering Less, Achieving More'\n    url: https://arxiv.org/abs/2602.04428\n    venue: ICLR 2026\n    verified: true\n    year: 2026\n  conneau2018xnli:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Conneau, A.\n    - Rinott, R.\n    - Lample, G.\n    - Williams, A.\n    - Bowman, S.\n    - Schwenk, H.\n    - Stoyanov, V.\n    bibtex_key: conneau2018xnli\n    category: dataset-tool\n    doi: ''\n    relevance: Cross-lingual NLI benchmark spanning 15 languages. Used for evaluating\n      cross-lingual transfer and multilingual understanding in our experiments.\n    role: foundation\n    title: 'XNLI: Evaluating Cross-lingual Sentence Representations'\n    url: https://aclanthology.org/D18-1269/\n    venue: EMNLP 2018\n    verified: true\n    year: 2018\n  rei2020comet:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Rei, R.\n    - Stewart, C.\n    - Farinha, A.C.\n    - Lavie, A.\n    bibtex_key: rei2020comet\n    category: dataset-tool\n    doi: ''\n    relevance: Neural MT evaluation metric using cross-lingual pretrained encoders.\n      Provides translation quality evaluation for our cross-lingual dataset construction\n      pipeline.\n    role: methodology\n    title: 'COMET: A Neural Framework for MT Evaluation'\n    url: https://aclanthology.org/2020.emnlp-main.213/\n    venue: EMNLP 2020\n    verified: true\n    year: 2020\n  grattafiori2024llama:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Grattafiori, A.\n    - et al. (Llama Team, AI @ Meta)\n    bibtex_key: grattafiori2024llama\n    category: dataset-tool\n    doi: ''\n    relevance: Technical report for Llama 3.1 models (8B/70B/405B). One of our primary\n      experimental models. Documents multilingual capabilities and 128K context window.\n    role: foundation\n    title: The Llama 3 Herd of Models\n    url: https://arxiv.org/abs/2407.21783\n    venue: arXiv\n    verified: true\n    year: 2024\n  yang2024qwen25:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Yang, A.\n    - Yang, B.\n    - et al. (Qwen Team)\n    bibtex_key: yang2024qwen25\n    category: dataset-tool\n    doi: ''\n    relevance: Technical report for Qwen2.5 model series. One of our primary experimental\n      models. Documents multilingual pretraining on 18T tokens.\n    role: foundation\n    title: Qwen2.5 Technical Report\n    url: https://arxiv.org/abs/2412.15115\n    venue: arXiv\n    verified: true\n    year: 2024",
    "originalFile": "categories: []\nmeta:\n  last_updated: '2026-05-22T14:30:00Z'\n  total_papers: 22\npapers:\n  basu2026interpretability:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Basu, S.\n    - et al.\n    bibtex_key: basu2026interpretability\n    category: sae-steering\n    doi: ''\n    relevance: 'SAE steering failure in clinical triage despite 98.2% AUROC probes.\n      Critical negative result: defines boundary conditions for when SAE steering\n      works. Our Track 3 design addresses their methodological gaps.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Interpretability without actionability: mechanistic methods cannot correct\n      language model errors despite near-perfect internal representations'\n    url: https://arxiv.org/abs/2603.18353\n    venue: arXiv\n    verified: true\n    year: 2026\n  boer2026probing:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Boer, A.\n    - Brink, I.\n    - Ulmer, D.\n    bibtex_key: boer2026probing\n    category: probing\n    doi: ''\n    relevance: 0.96 Macro-F1 parametric-vs-contextual attribution probe on Llama/Mistral/Qwen.\n      Monolingual performance ceiling for our Track 1. Cross-domain transfer 0.94-0.99\n      F1.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: Probing for Knowledge Attribution in Large Language Models\n    url: https://arxiv.org/abs/2602.22787\n    venue: arXiv\n    verified: true\n    year: 2026\n  ifergan2024beneath:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Ifergan, M.\n    - Choshen, L.\n    - Aharoni, R.\n    - Szpektor, I.\n    - Abend, O.\n    bibtex_key: ifergan2024beneath\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: Shows cross-lingual answer consistency does not imply shared representation;\n      script similarity dominates sharing. Directly motivates our probing approach\n      to test whether conflict signals share representations across languages.\n    role: foundation\n    title: 'Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge\n      Representation Sharing in LLMs'\n    url: https://arxiv.org/abs/2408.10646\n    venue: Findings of NAACL 2025\n    verified: true\n    year: 2024\n  kialy2026universal:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Kialy, U.Z.\n    - Shtarkberg, A.\n    - Klein, A.\n    bibtex_key: kialy2026universal\n    category: cross-lingual-sae\n    doi: ''\n    relevance: First cross-lingual SAE feature discovery. Shows cross-linguistic core\n      for register features + zero-shot steering transfer. We test whether this extends\n      to knowledge conflict features.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: A Universal Vibe? Finding and Controlling Language-Agnostic Informal Register\n      with SAEs\n    url: https://arxiv.org/abs/2603.26236\n    venue: arXiv\n    verified: true\n    year: 2026\n  li2025taming:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Li, G.\n    - Chen, Y.\n    - Tong, H.\n    bibtex_key: li2025taming\n    category: knowledge-conflict\n    doi: ''\n    relevance: Proposes conflict resolution framework for LLMs. Provides resolution\n      baselines our mechanistic approach complements.\n    role: direct-competitor\n    title: Taming Knowledge Conflicts in Language Models\n    url: https://arxiv.org/abs/2503.10996\n    venue: ICML 2025 (Spotlight)\n    verified: true\n    year: 2025\n  pham2026where:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Pham, M.V.\n    - Borkakoty, H.\n    - Hou, Y.\n    bibtex_key: pham2026where\n    category: conflict-mechanism\n    doi: ''\n    relevance: Activation patching + CMAP for intra-memory conflicts. Attention layers\n      21-47 dominate conflict resolution in Qwen3-4B. Closest methodological parallel\n      for within-parametric conflicts.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge\n      Conflict in Language Models'\n    url: https://arxiv.org/abs/2601.09445\n    venue: arXiv\n    verified: true\n    year: 2026\n  team2026qwen:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Qwen Team\n    bibtex_key: team2026qwen\n    category: sae-tools\n    doi: ''\n    relevance: Pretrained SAEs for Qwen3 family. Our Track 2 uses Qwen-Scope SAEs\n      on Qwen3-8B-Base. Documents cross-lingual transfer for toxicity features (Section\n      5.2).\n    role: foundation\n    semantic_scholar_id: ''\n    title: 'Qwen-Scope: Turning Sparse Features into Development Tools for Large Language\n      Models'\n    url: https://arxiv.org/abs/2605.11887\n    venue: arXiv\n    verified: true\n    year: 2026\n  wang2025lost:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Wang, M.\n    - Adel, H.\n    - Lange, L.\n    - et al.\n    bibtex_key: wang2025lost\n    category: cross-lingual-mechanism\n    doi: ''\n    relevance: Language-independent concept space through most layers, language-specific\n      only in final layers. Key mechanistic finding our H1/H2 hypotheses build on.\n    role: foundation\n    semantic_scholar_id: ''\n    title: 'Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency\n      in Transformer Language Models'\n    url: https://arxiv.org/abs/2504.04264\n    venue: ACL 2025 (SAC Highlights)\n    verified: true\n    year: 2025\n  wong2026langfir:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Wong, S.H.\n    - Siddique, A.B.\n    - Sajjad, H.\n    bibtex_key: wong2026langfir\n    category: cross-lingual-sae\n    doi: ''\n    relevance: Random-token filtering isolates <5 language-specific SAE features/language.\n      Our Track 2 uses this as control to disentangle language-identity from conflict\n      features.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'LangFIR: Discovering Sparse Language-Specific Features from Monolingual\n      Data for Language Steering'\n    url: https://arxiv.org/abs/2604.03532\n    venue: arXiv\n    verified: true\n    year: 2026\n  xie2024adaptive:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xie, J.\n    - Zhang, K.\n    - Chen, J.\n    - Lou, R.\n    - Su, Y.\n    bibtex_key: xie2024adaptive\n    category: knowledge-conflict\n    doi: ''\n    relevance: Introduces ConflictQA benchmark (PopQA + StrategyQA based) for studying\n      LLM behavior under context-parametric knowledge conflicts. Our primary evaluation\n      dataset.\n    role: foundation\n    title: 'Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large\n      Language Models in Knowledge Conflicts'\n    url: https://arxiv.org/abs/2305.13300\n    venue: ICLR 2024\n    verified: true\n    year: 2024\n  xing2024evaluating:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xing, X.\n    - He, Z.\n    - Xu, H.\n    - Wang, X.\n    - Wang, R.\n    - Hong, Y.\n    bibtex_key: xing2024evaluating\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: Proposes cross-lingual semantic/accuracy/timeliness consistency metrics\n      (xSC, xAC, xTC) for evaluating multilingual LLM inconsistency. Provides evaluation\n      methodology relevant to our cross-lingual conflict measurement.\n    role: peripheral\n    title: Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language\n      Models\n    url: https://arxiv.org/abs/2407.01358\n    venue: arXiv\n    verified: true\n    year: 2024\n  xu2024knowledge:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xu, R.\n    - Qi, Z.\n    - Guo, Z.\n    - Wang, C.\n    - Wang, H.\n    - Zhang, Y.\n    - Xu, W.\n    bibtex_key: xu2024knowledge\n    category: knowledge-conflict\n    doi: ''\n    relevance: Comprehensive survey of context-memory, inter-context, and intra-memory\n      knowledge conflicts in LLMs. Defines the taxonomy our work builds on.\n    role: foundation\n    title: 'Knowledge Conflicts for LLMs: A Survey'\n    url: https://arxiv.org/abs/2403.08319\n    venue: EMNLP 2024\n    verified: true\n    year: 2024\n  zhao2024analysing:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, Y.\n    - Du, X.\n    - Hong, G.\n    - et al.\n    bibtex_key: zhao2024analysing\n    category: probing\n    doi: ''\n    relevance: 'Original conflict probing work: ~90% accuracy detecting conflicts\n      in residual stream. Foundation for our Track 1 cross-lingual extension.'\n    role: foundation\n    semantic_scholar_id: ''\n    title: Analysing the Residual Stream of Language Models Under Knowledge Conflicts\n    url: https://arxiv.org/abs/2410.16090\n    venue: NeurIPS 2024 FMI Workshop\n    verified: true\n    year: 2024\n  zhao2025steering:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, Y.\n    - Devoto, A.\n    - Hong, G.\n    - et al.\n    bibtex_key: zhao2025steering\n    category: sae-steering\n    doi: ''\n    relevance: 'SpARE: SAE-based conflict feature selection + steering. Core methodology\n      we extend to cross-lingual setting. MI-based feature selection, constraint-aware\n      activation editing.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation\n      Engineering\n    url: https://arxiv.org/abs/2410.15999\n    venue: NAACL 2025 Oral\n    verified: true\n    year: 2025\n  zhao2026when:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, J.\n    - et al.\n    bibtex_key: zhao2026when\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: 'CLEAR benchmark: 10-language cross-lingual conflict evaluation. Behavioral\n      finding that linguistic similarity governs entity-centric conflict resolution.\n      Our work provides mechanistic explanation.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026\n  wu2020emerging:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wu, S.\n    - Conneau, A.\n    - Li, H.\n    - Zettlemoyer, L.\n    - Stoyanov, V.\n    bibtex_key: wu2020emerging\n    category: cross-lingual-repr\n    doi: 10.18653/v1/2020.acl-main.536\n    relevance: Shows mid-layer cross-lingual alignment emerges from shared parameters\n      alone; monolingual representations can be aligned post-hoc. Foundation for understanding\n      language-agnostic concept space our probing hypotheses build on. MUST CITE.\n    role: foundation\n    title: Emerging Cross-lingual Structure in Pretrained Language Models\n    url: https://aclanthology.org/2020.acl-main.536/\n    venue: ACL 2020\n    verified: true\n    year: 2020\n  wendler2024llamas:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wendler, C.\n    - Veselovsky, V.\n    - Monea, G.\n    - West, R.\n    bibtex_key: wendler2024llamas\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Demonstrates English-centric LLMs implicitly pivot through English representations\n      in middle layers. Three-phase pattern (input language -> English pivot -> output\n      language) supports hypothesis that conflict signals may route through English-aligned\n      subspace.\n    role: foundation\n    title: 'Do Llamas Work in English? On the Latent Language of Multilingual Transformers'\n    url: https://arxiv.org/abs/2402.10588\n    venue: ACL 2024\n    verified: true\n    year: 2024\n  muller2021first:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Muller, B.\n    - Elazar, Y.\n    - Sagot, B.\n    - Seddah, D.\n    bibtex_key: muller2021first\n    category: cross-lingual-repr\n    doi: ''\n    relevance: CKA-based layer-wise analysis showing mBERT decomposes into multilingual\n      encoder + language-agnostic predictor. Representations first converge to language\n      neutrality then recover language specificity. Methodological precedent for our\n      layer-wise analysis.\n    role: methodology\n    title: 'First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual\n      BERT'\n    url: https://aclanthology.org/2021.eacl-main.189/\n    venue: EACL 2021\n    verified: true\n    year: 2021\n  kargaran2024mexa:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Kargaran, A.H.\n    - Modarressi, A.\n    - Nikeghbal, N.\n    - Diesner, J.\n    - Yvon, F.\n    - \"Sch\\xFCtze, H.\"\n    bibtex_key: kargaran2024mexa\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Cross-lingual alignment metric leveraging English pivot hypothesis, 0.90\n      Pearson correlation with downstream tasks. Provides evaluation methodology for\n      measuring English-centric alignment relevant to our cross-lingual transfer analysis.\n    role: methodology\n    title: 'MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual\n      Alignment'\n    url: https://arxiv.org/abs/2410.05873\n    venue: Findings of ACL 2025\n    verified: true\n    year: 2024\n  belinkov2022probing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Belinkov, Y.\n    bibtex_key: belinkov2022probing\n    category: probing-methodology\n    doi: ''\n    relevance: Comprehensive survey of probing classifier promises, shortcomings, and\n      advances. Defines the methodological framework our linear probes follow. MUST\n      CITE for probing methodology justification.\n    role: foundation\n    title: 'Probing Classifiers: Promises, Shortcomings, and Advances'\n    url: https://arxiv.org/abs/2102.12452\n    venue: Computational Linguistics 48(1)\n    verified: true\n    year: 2022\n  hewitt2019designing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Hewitt, J.\n    - Liang, P.\n    bibtex_key: hewitt2019designing\n    category: probing-methodology\n    doi: ''\n    relevance: Introduces selectivity metric (linguistic accuracy - control accuracy)\n      to distinguish genuine representation encoding from probe memorization. Our probing\n      design uses control tasks following this framework. EMNLP 2019 Best Paper Runner\n      Up.\n    role: methodology\n    title: Designing and Interpreting Probes with Control Tasks\n    url: https://aclanthology.org/D19-1275/\n    venue: EMNLP 2019\n    verified: true\n    year: 2019\n  ulmer2022deep:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Ulmer, D.\n    - Hardmeier, C.\n    - Frellsen, J.\n    bibtex_key: ulmer2022deep\n    category: probing-methodology\n    doi: ''\n    relevance: Bootstrap-based statistical testing framework for neural network comparisons,\n      including Almost Stochastic Order (ASO). Provides the bootstrap CI methodology\n      we use for probing accuracy significance testing.\n    role: methodology\n    title: 'deep-significance: Easy and Meaningful Statistical Significance Testing\n      in the Age of Neural Networks'\n    url: https://arxiv.org/abs/2204.06815\n    venue: arXiv\n    verified: true\n    year: 2022\n",
    "structuredPatch": [
      {
        "oldStart": 467,
        "oldLines": 3,
        "newStart": 467,
        "newLines": 149,
        "lines": [
          "     venue: arXiv",
          "     verified: true",
          "     year: 2022",
          "+  li2023iti:",
          "+    added_at: '2026-05-22T16:00:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Li, K.",
          "+    - Patel, O.",
          "+    - \"Vi\\xE9gas, F.\"",
          "+    - Pfister, H.",
          "+    - Wattenberg, M.",
          "+    bibtex_key: li2023iti",
          "+    category: steering",
          "+    doi: ''",
          "+    relevance: Inference-Time Intervention shifts activations along truthful directions",
          "+      in attention heads to improve truthfulness. Foundational activation steering method",
          "+      our causal intervention approach builds on.",
          "+    role: foundation",
          "+    title: 'Inference-Time Intervention: Eliciting Truthful Answers from a Language",
          "+      Model'",
          "+    url: https://arxiv.org/abs/2306.03341",
          "+    venue: NeurIPS 2023",
          "+    verified: true",
          "+    year: 2023",
          "+  zou2023representation:",
          "+    added_at: '2026-05-22T16:00:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Zou, A.",
          "+    - Phan, L.",
          "+    - Chen, S.",
          "+    - Campbell, J.",
          "+    - Guo, P.",
          "+    - Ren, R.",
          "+    - Pan, A.",
          "+    - et al.",
          "+    bibtex_key: zou2023representation",
          "+    category: steering",
          "+    doi: ''",
          "+    relevance: Introduces Representation Engineering (RepE) framework using population-level",
          "+      representations for monitoring and manipulating high-level cognitive phenomena.",
          "+      Foundational paradigm for our steering methodology.",
          "+    role: foundation",
          "+    title: 'Representation Engineering: A Top-Down Approach to AI Transparency'",
          "+    url: https://arxiv.org/abs/2310.01405",
          "+    venue: arXiv",
          "+    verified: true",
          "+    year: 2023",
          "+  feng2026finegrained:",
          "+    added_at: '2026-05-22T16:00:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Feng, Z.",
          "+    - Li, T.",
          "+    - Zhu, Z.",
          "+    - Zhou, H.",
          "+    - Qian, J.",
          "+    - Zhang, L.",
          "+    - Mao, K.",
          "+    bibtex_key: feng2026finegrained",
          "+    category: steering",
          "+    doi: ''",
          "+    relevance: Decomposes block activations into atomic-unit-level activations for",
          "+      fine-grained steering. Shows block-level steering entangles beneficial and harmful",
          "+      features. Methodological advance relevant to our per-feature steering design.",
          "+    role: methodology",
          "+    title: 'Fine-Grained Activation Steering: Steering Less, Achieving More'",
          "+    url: https://arxiv.org/abs/2602.04428",
          "+    venue: ICLR 2026",
          "+    verified: true",
          "+    year: 2026",
          "+  conneau2018xnli:",
          "+    added_at: '2026-05-22T16:00:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Conneau, A.",
          "+    - Rinott, R.",
          "+    - Lample, G.",
          "+    - Williams, A.",
          "+    - Bowman, S.",
          "+    - Schwenk, H.",
          "+    - Stoyanov, V.",
          "+    bibtex_key: conneau2018xnli",
          "+    category: dataset-tool",
          "+    doi: ''",
          "+    relevance: Cross-lingual NLI benchmark spanning 15 languages. Used for evaluating",
          "+      cross-lingual transfer and multilingual understanding in our experiments.",
          "+    role: foundation",
          "+    title: 'XNLI: Evaluating Cross-lingual Sentence Representations'",
          "+    url: https://aclanthology.org/D18-1269/",
          "+    venue: EMNLP 2018",
          "+    verified: true",
          "+    year: 2018",
          "+  rei2020comet:",
          "+    added_at: '2026-05-22T16:00:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Rei, R.",
          "+    - Stewart, C.",
          "+    - Farinha, A.C.",
          "+    - Lavie, A.",
          "+    bibtex_key: rei2020comet",
          "+    category: dataset-tool",
          "+    doi: ''",
          "+    relevance: Neural MT evaluation metric using cross-lingual pretrained encoders.",
          "+      Provides translation quality evaluation for our cross-lingual dataset construction",
          "+      pipeline.",
          "+    role: methodology",
          "+    title: 'COMET: A Neural Framework for MT Evaluation'",
          "+    url: https://aclanthology.org/2020.emnlp-main.213/",
          "+    venue: EMNLP 2020",
          "+    verified: true",
          "+    year: 2020",
          "+  grattafiori2024llama:",
          "+    added_at: '2026-05-22T16:00:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Grattafiori, A.",
          "+    - et al. (Llama Team, AI @ Meta)",
          "+    bibtex_key: grattafiori2024llama",
          "+    category: dataset-tool",
          "+    doi: ''",
          "+    relevance: Technical report for Llama 3.1 models (8B/70B/405B). One of our primary",
          "+      experimental models. Documents multilingual capabilities and 128K context window.",
          "+    role: foundation",
          "+    title: The Llama 3 Herd of Models",
          "+    url: https://arxiv.org/abs/2407.21783",
          "+    venue: arXiv",
          "+    verified: true",
          "+    year: 2024",
          "+  yang2024qwen25:",
          "+    added_at: '2026-05-22T16:00:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Yang, A.",
          "+    - Yang, B.",
          "+    - et al. (Qwen Team)",
          "+    bibtex_key: yang2024qwen25",
          "+    category: dataset-tool",
          "+    doi: ''",
          "+    relevance: Technical report for Qwen2.5 model series. One of our primary experimental",
          "+      models. Documents multilingual pretraining on 18T tokens.",
          "+    role: foundation",
          "+    title: Qwen2.5 Technical Report",
          "+    url: https://arxiv.org/abs/2412.15115",
          "+    venue: arXiv",
          "+    verified: true",
          "+    year: 2024"
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

_source line 53_

Now update the `total_papers` count and verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "7fc3cb08-445e-4a22-ae2e-e5ca504577f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011QtUQzTF68cBZao9nPBEf5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1854,
      "cache_read_input_tokens": 47473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1854
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

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_01EfzwyamRnRnYXoSzhzzAxm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
  "old_string": "  total_papers: 22",
  "new_string": "  total_papers: 29"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "a47e3777-7388-4f3d-bc72-4d51c578f915",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011QtUQzTF68cBZao9nPBEf5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1854,
      "cache_read_input_tokens": 47473,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1854
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

_source line 55 · 2026-05-22T14:07:45.169Z_

<details><summary>↩ Tool result · `toolu_01EfzwyamRnRnYXoSzhzzAxm`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "40343401-7ef5-44c7-a520-e49683b1f48f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
    "oldString": "  total_papers: 22",
    "newString": "  total_papers: 29",
    "originalFile": "categories: []\nmeta:\n  last_updated: '2026-05-22T14:30:00Z'\n  total_papers: 22\npapers:\n  basu2026interpretability:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Basu, S.\n    - et al.\n    bibtex_key: basu2026interpretability\n    category: sae-steering\n    doi: ''\n    relevance: 'SAE steering failure in clinical triage despite 98.2% AUROC probes.\n      Critical negative result: defines boundary conditions for when SAE steering\n      works. Our Track 3 design addresses their methodological gaps.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Interpretability without actionability: mechanistic methods cannot correct\n      language model errors despite near-perfect internal representations'\n    url: https://arxiv.org/abs/2603.18353\n    venue: arXiv\n    verified: true\n    year: 2026\n  boer2026probing:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Boer, A.\n    - Brink, I.\n    - Ulmer, D.\n    bibtex_key: boer2026probing\n    category: probing\n    doi: ''\n    relevance: 0.96 Macro-F1 parametric-vs-contextual attribution probe on Llama/Mistral/Qwen.\n      Monolingual performance ceiling for our Track 1. Cross-domain transfer 0.94-0.99\n      F1.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: Probing for Knowledge Attribution in Large Language Models\n    url: https://arxiv.org/abs/2602.22787\n    venue: arXiv\n    verified: true\n    year: 2026\n  ifergan2024beneath:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Ifergan, M.\n    - Choshen, L.\n    - Aharoni, R.\n    - Szpektor, I.\n    - Abend, O.\n    bibtex_key: ifergan2024beneath\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: Shows cross-lingual answer consistency does not imply shared representation;\n      script similarity dominates sharing. Directly motivates our probing approach\n      to test whether conflict signals share representations across languages.\n    role: foundation\n    title: 'Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge\n      Representation Sharing in LLMs'\n    url: https://arxiv.org/abs/2408.10646\n    venue: Findings of NAACL 2025\n    verified: true\n    year: 2024\n  kialy2026universal:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Kialy, U.Z.\n    - Shtarkberg, A.\n    - Klein, A.\n    bibtex_key: kialy2026universal\n    category: cross-lingual-sae\n    doi: ''\n    relevance: First cross-lingual SAE feature discovery. Shows cross-linguistic core\n      for register features + zero-shot steering transfer. We test whether this extends\n      to knowledge conflict features.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: A Universal Vibe? Finding and Controlling Language-Agnostic Informal Register\n      with SAEs\n    url: https://arxiv.org/abs/2603.26236\n    venue: arXiv\n    verified: true\n    year: 2026\n  li2025taming:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Li, G.\n    - Chen, Y.\n    - Tong, H.\n    bibtex_key: li2025taming\n    category: knowledge-conflict\n    doi: ''\n    relevance: Proposes conflict resolution framework for LLMs. Provides resolution\n      baselines our mechanistic approach complements.\n    role: direct-competitor\n    title: Taming Knowledge Conflicts in Language Models\n    url: https://arxiv.org/abs/2503.10996\n    venue: ICML 2025 (Spotlight)\n    verified: true\n    year: 2025\n  pham2026where:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Pham, M.V.\n    - Borkakoty, H.\n    - Hou, Y.\n    bibtex_key: pham2026where\n    category: conflict-mechanism\n    doi: ''\n    relevance: Activation patching + CMAP for intra-memory conflicts. Attention layers\n      21-47 dominate conflict resolution in Qwen3-4B. Closest methodological parallel\n      for within-parametric conflicts.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge\n      Conflict in Language Models'\n    url: https://arxiv.org/abs/2601.09445\n    venue: arXiv\n    verified: true\n    year: 2026\n  team2026qwen:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Qwen Team\n    bibtex_key: team2026qwen\n    category: sae-tools\n    doi: ''\n    relevance: Pretrained SAEs for Qwen3 family. Our Track 2 uses Qwen-Scope SAEs\n      on Qwen3-8B-Base. Documents cross-lingual transfer for toxicity features (Section\n      5.2).\n    role: foundation\n    semantic_scholar_id: ''\n    title: 'Qwen-Scope: Turning Sparse Features into Development Tools for Large Language\n      Models'\n    url: https://arxiv.org/abs/2605.11887\n    venue: arXiv\n    verified: true\n    year: 2026\n  wang2025lost:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Wang, M.\n    - Adel, H.\n    - Lange, L.\n    - et al.\n    bibtex_key: wang2025lost\n    category: cross-lingual-mechanism\n    doi: ''\n    relevance: Language-independent concept space through most layers, language-specific\n      only in final layers. Key mechanistic finding our H1/H2 hypotheses build on.\n    role: foundation\n    semantic_scholar_id: ''\n    title: 'Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency\n      in Transformer Language Models'\n    url: https://arxiv.org/abs/2504.04264\n    venue: ACL 2025 (SAC Highlights)\n    verified: true\n    year: 2025\n  wong2026langfir:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Wong, S.H.\n    - Siddique, A.B.\n    - Sajjad, H.\n    bibtex_key: wong2026langfir\n    category: cross-lingual-sae\n    doi: ''\n    relevance: Random-token filtering isolates <5 language-specific SAE features/language.\n      Our Track 2 uses this as control to disentangle language-identity from conflict\n      features.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'LangFIR: Discovering Sparse Language-Specific Features from Monolingual\n      Data for Language Steering'\n    url: https://arxiv.org/abs/2604.03532\n    venue: arXiv\n    verified: true\n    year: 2026\n  xie2024adaptive:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xie, J.\n    - Zhang, K.\n    - Chen, J.\n    - Lou, R.\n    - Su, Y.\n    bibtex_key: xie2024adaptive\n    category: knowledge-conflict\n    doi: ''\n    relevance: Introduces ConflictQA benchmark (PopQA + StrategyQA based) for studying\n      LLM behavior under context-parametric knowledge conflicts. Our primary evaluation\n      dataset.\n    role: foundation\n    title: 'Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large\n      Language Models in Knowledge Conflicts'\n    url: https://arxiv.org/abs/2305.13300\n    venue: ICLR 2024\n    verified: true\n    year: 2024\n  xing2024evaluating:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xing, X.\n    - He, Z.\n    - Xu, H.\n    - Wang, X.\n    - Wang, R.\n    - Hong, Y.\n    bibtex_key: xing2024evaluating\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: Proposes cross-lingual semantic/accuracy/timeliness consistency metrics\n      (xSC, xAC, xTC) for evaluating multilingual LLM inconsistency. Provides evaluation\n      methodology relevant to our cross-lingual conflict measurement.\n    role: peripheral\n    title: Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language\n      Models\n    url: https://arxiv.org/abs/2407.01358\n    venue: arXiv\n    verified: true\n    year: 2024\n  xu2024knowledge:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xu, R.\n    - Qi, Z.\n    - Guo, Z.\n    - Wang, C.\n    - Wang, H.\n    - Zhang, Y.\n    - Xu, W.\n    bibtex_key: xu2024knowledge\n    category: knowledge-conflict\n    doi: ''\n    relevance: Comprehensive survey of context-memory, inter-context, and intra-memory\n      knowledge conflicts in LLMs. Defines the taxonomy our work builds on.\n    role: foundation\n    title: 'Knowledge Conflicts for LLMs: A Survey'\n    url: https://arxiv.org/abs/2403.08319\n    venue: EMNLP 2024\n    verified: true\n    year: 2024\n  zhao2024analysing:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, Y.\n    - Du, X.\n    - Hong, G.\n    - et al.\n    bibtex_key: zhao2024analysing\n    category: probing\n    doi: ''\n    relevance: 'Original conflict probing work: ~90% accuracy detecting conflicts\n      in residual stream. Foundation for our Track 1 cross-lingual extension.'\n    role: foundation\n    semantic_scholar_id: ''\n    title: Analysing the Residual Stream of Language Models Under Knowledge Conflicts\n    url: https://arxiv.org/abs/2410.16090\n    venue: NeurIPS 2024 FMI Workshop\n    verified: true\n    year: 2024\n  zhao2025steering:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, Y.\n    - Devoto, A.\n    - Hong, G.\n    - et al.\n    bibtex_key: zhao2025steering\n    category: sae-steering\n    doi: ''\n    relevance: 'SpARE: SAE-based conflict feature selection + steering. Core methodology\n      we extend to cross-lingual setting. MI-based feature selection, constraint-aware\n      activation editing.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation\n      Engineering\n    url: https://arxiv.org/abs/2410.15999\n    venue: NAACL 2025 Oral\n    verified: true\n    year: 2025\n  zhao2026when:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, J.\n    - et al.\n    bibtex_key: zhao2026when\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: 'CLEAR benchmark: 10-language cross-lingual conflict evaluation. Behavioral\n      finding that linguistic similarity governs entity-centric conflict resolution.\n      Our work provides mechanistic explanation.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026\n  wu2020emerging:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wu, S.\n    - Conneau, A.\n    - Li, H.\n    - Zettlemoyer, L.\n    - Stoyanov, V.\n    bibtex_key: wu2020emerging\n    category: cross-lingual-repr\n    doi: 10.18653/v1/2020.acl-main.536\n    relevance: Shows mid-layer cross-lingual alignment emerges from shared parameters\n      alone; monolingual representations can be aligned post-hoc. Foundation for understanding\n      language-agnostic concept space our probing hypotheses build on. MUST CITE.\n    role: foundation\n    title: Emerging Cross-lingual Structure in Pretrained Language Models\n    url: https://aclanthology.org/2020.acl-main.536/\n    venue: ACL 2020\n    verified: true\n    year: 2020\n  wendler2024llamas:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wendler, C.\n    - Veselovsky, V.\n    - Monea, G.\n    - West, R.\n    bibtex_key: wendler2024llamas\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Demonstrates English-centric LLMs implicitly pivot through English representations\n      in middle layers. Three-phase pattern (input language -> English pivot -> output\n      language) supports hypothesis that conflict signals may route through English-aligned\n      subspace.\n    role: foundation\n    title: 'Do Llamas Work in English? On the Latent Language of Multilingual Transformers'\n    url: https://arxiv.org/abs/2402.10588\n    venue: ACL 2024\n    verified: true\n    year: 2024\n  muller2021first:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Muller, B.\n    - Elazar, Y.\n    - Sagot, B.\n    - Seddah, D.\n    bibtex_key: muller2021first\n    category: cross-lingual-repr\n    doi: ''\n    relevance: CKA-based layer-wise analysis showing mBERT decomposes into multilingual\n      encoder + language-agnostic predictor. Representations first converge to language\n      neutrality then recover language specificity. Methodological precedent for our\n      layer-wise analysis.\n    role: methodology\n    title: 'First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual\n      BERT'\n    url: https://aclanthology.org/2021.eacl-main.189/\n    venue: EACL 2021\n    verified: true\n    year: 2021\n  kargaran2024mexa:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Kargaran, A.H.\n    - Modarressi, A.\n    - Nikeghbal, N.\n    - Diesner, J.\n    - Yvon, F.\n    - \"Sch\\xFCtze, H.\"\n    bibtex_key: kargaran2024mexa\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Cross-lingual alignment metric leveraging English pivot hypothesis, 0.90\n      Pearson correlation with downstream tasks. Provides evaluation methodology for\n      measuring English-centric alignment relevant to our cross-lingual transfer analysis.\n    role: methodology\n    title: 'MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual\n      Alignment'\n    url: https://arxiv.org/abs/2410.05873\n    venue: Findings of ACL 2025\n    verified: true\n    year: 2024\n  belinkov2022probing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Belinkov, Y.\n    bibtex_key: belinkov2022probing\n    category: probing-methodology\n    doi: ''\n    relevance: Comprehensive survey of probing classifier promises, shortcomings, and\n      advances. Defines the methodological framework our linear probes follow. MUST\n      CITE for probing methodology justification.\n    role: foundation\n    title: 'Probing Classifiers: Promises, Shortcomings, and Advances'\n    url: https://arxiv.org/abs/2102.12452\n    venue: Computational Linguistics 48(1)\n    verified: true\n    year: 2022\n  hewitt2019designing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Hewitt, J.\n    - Liang, P.\n    bibtex_key: hewitt2019designing\n    category: probing-methodology\n    doi: ''\n    relevance: Introduces selectivity metric (linguistic accuracy - control accuracy)\n      to distinguish genuine representation encoding from probe memorization. Our probing\n      design uses control tasks following this framework. EMNLP 2019 Best Paper Runner\n      Up.\n    role: methodology\n    title: Designing and Interpreting Probes with Control Tasks\n    url: https://aclanthology.org/D19-1275/\n    venue: EMNLP 2019\n    verified: true\n    year: 2019\n  ulmer2022deep:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Ulmer, D.\n    - Hardmeier, C.\n    - Frellsen, J.\n    bibtex_key: ulmer2022deep\n    category: probing-methodology\n    doi: ''\n    relevance: Bootstrap-based statistical testing framework for neural network comparisons,\n      including Almost Stochastic Order (ASO). Provides the bootstrap CI methodology\n      we use for probing accuracy significance testing.\n    role: methodology\n    title: 'deep-significance: Easy and Meaningful Statistical Significance Testing\n      in the Age of Neural Networks'\n    url: https://arxiv.org/abs/2204.06815\n    venue: arXiv\n    verified: true\n    year: 2022\n  li2023iti:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Li, K.\n    - Patel, O.\n    - \"Vi\\xE9gas, F.\"\n    - Pfister, H.\n    - Wattenberg, M.\n    bibtex_key: li2023iti\n    category: steering\n    doi: ''\n    relevance: Inference-Time Intervention shifts activations along truthful directions\n      in attention heads to improve truthfulness. Foundational activation steering method\n      our causal intervention approach builds on.\n    role: foundation\n    title: 'Inference-Time Intervention: Eliciting Truthful Answers from a Language\n      Model'\n    url: https://arxiv.org/abs/2306.03341\n    venue: NeurIPS 2023\n    verified: true\n    year: 2023\n  zou2023representation:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Zou, A.\n    - Phan, L.\n    - Chen, S.\n    - Campbell, J.\n    - Guo, P.\n    - Ren, R.\n    - Pan, A.\n    - et al.\n    bibtex_key: zou2023representation\n    category: steering\n    doi: ''\n    relevance: Introduces Representation Engineering (RepE) framework using population-level\n      representations for monitoring and manipulating high-level cognitive phenomena.\n      Foundational paradigm for our steering methodology.\n    role: foundation\n    title: 'Representation Engineering: A Top-Down Approach to AI Transparency'\n    url: https://arxiv.org/abs/2310.01405\n    venue: arXiv\n    verified: true\n    year: 2023\n  feng2026finegrained:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Feng, Z.\n    - Li, T.\n    - Zhu, Z.\n    - Zhou, H.\n    - Qian, J.\n    - Zhang, L.\n    - Mao, K.\n    bibtex_key: feng2026finegrained\n    category: steering\n    doi: ''\n    relevance: Decomposes block activations into atomic-unit-level activations for\n      fine-grained steering. Shows block-level steering entangles beneficial and harmful\n      features. Methodological advance relevant to our per-feature steering design.\n    role: methodology\n    title: 'Fine-Grained Activation Steering: Steering Less, Achieving More'\n    url: https://arxiv.org/abs/2602.04428\n    venue: ICLR 2026\n    verified: true\n    year: 2026\n  conneau2018xnli:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Conneau, A.\n    - Rinott, R.\n    - Lample, G.\n    - Williams, A.\n    - Bowman, S.\n    - Schwenk, H.\n    - Stoyanov, V.\n    bibtex_key: conneau2018xnli\n    category: dataset-tool\n    doi: ''\n    relevance: Cross-lingual NLI benchmark spanning 15 languages. Used for evaluating\n      cross-lingual transfer and multilingual understanding in our experiments.\n    role: foundation\n    title: 'XNLI: Evaluating Cross-lingual Sentence Representations'\n    url: https://aclanthology.org/D18-1269/\n    venue: EMNLP 2018\n    verified: true\n    year: 2018\n  rei2020comet:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Rei, R.\n    - Stewart, C.\n    - Farinha, A.C.\n    - Lavie, A.\n    bibtex_key: rei2020comet\n    category: dataset-tool\n    doi: ''\n    relevance: Neural MT evaluation metric using cross-lingual pretrained encoders.\n      Provides translation quality evaluation for our cross-lingual dataset construction\n      pipeline.\n    role: methodology\n    title: 'COMET: A Neural Framework for MT Evaluation'\n    url: https://aclanthology.org/2020.emnlp-main.213/\n    venue: EMNLP 2020\n    verified: true\n    year: 2020\n  grattafiori2024llama:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Grattafiori, A.\n    - et al. (Llama Team, AI @ Meta)\n    bibtex_key: grattafiori2024llama\n    category: dataset-tool\n    doi: ''\n    relevance: Technical report for Llama 3.1 models (8B/70B/405B). One of our primary\n      experimental models. Documents multilingual capabilities and 128K context window.\n    role: foundation\n    title: The Llama 3 Herd of Models\n    url: https://arxiv.org/abs/2407.21783\n    venue: arXiv\n    verified: true\n    year: 2024\n  yang2024qwen25:\n    added_at: '2026-05-22T16:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Yang, A.\n    - Yang, B.\n    - et al. (Qwen Team)\n    bibtex_key: yang2024qwen25\n    category: dataset-tool\n    doi: ''\n    relevance: Technical report for Qwen2.5 model series. One of our primary experimental\n      models. Documents multilingual pretraining on 18T tokens.\n    role: foundation\n    title: Qwen2.5 Technical Report\n    url: https://arxiv.org/abs/2412.15115\n    venue: arXiv\n    verified: true\n    year: 2024\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " categories: []",
          " meta:",
          "   last_updated: '2026-05-22T14:30:00Z'",
          "-  total_papers: 22",
          "+  total_papers: 29",
          " papers:",
          "   basu2026interpretability:",
          "     abstract: ''"
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

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_01UkEU2HYDp7xBvBXks1riYn`</summary>

```json
{
  "command": "grep -c 'bibtex_key:' /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
  "description": "Count total papers in literature map"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "65aa27d9-8c96-4e9f-a80b-bc8c19b81734",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ArrykmMGtKhPQvnSuC5tmx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 214,
      "cache_read_input_tokens": 49327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 214
      },
      "output_tokens": 51,
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

_source line 57 · 2026-05-22T14:07:48.623Z_

<details><summary>↩ Tool result · `toolu_01UkEU2HYDp7xBvBXks1riYn`</summary>

```text
29
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "e38ce029-e698-4e03-8f96-6cb051e9e521",
  "tool_use_result": {
    "stdout": "29",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 58_

29 篇，符合 ≥28 要求。

## 新增汇报

### Cluster 5: Steering & Causal Intervention（+3 篇，现有 7 篇）

| key | title | venue |
|-----|-------|-------|
| `li2023iti` | Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | NeurIPS 2023 |
| `zou2023representation` | Representation Engineering: A Top-Down Approach to AI Transparency | arXiv 2023 |
| `feng2026finegrained` | Fine-Grained Activation Steering: Steering Less, Achieving More | ICLR 2026 |

### Cluster 6: Datasets & Evaluation Tools（+4 篇，现有 5 篇）

| key | title | venue |
|-----|-------|-------|
| `conneau2018xnli` | XNLI: Evaluating Cross-lingual Sentence Representations | EMNLP 2018 |
| `rei2020comet` | COMET: A Neural Framework for MT Evaluation | EMNLP 2020 |
| `grattafiori2024llama` | The Llama 3 Herd of Models | arXiv 2024 |
| `yang2024qwen25` | Qwen2.5 Technical Report | arXiv 2024 |

所有 must_cite 论文均已找到并验证 URL。注意 ITI 论文实际发表于 2023 年（NeurIPS 2023），不是 2024。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "uuid": "1e1abee7-3525-4c9e-9c4f-34b98df44252",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0186NPD95PvbT5vAse6Livyf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 129,
      "cache_read_input_tokens": 49541,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 129
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

_source line 59_

29 篇，符合 ≥28 要求。

## 新增汇报

### Cluster 5: Steering & Causal Intervention（+3 篇，现有 7 篇）

| key | title | venue |
|-----|-------|-------|
| `li2023iti` | Inference-Time Intervention: Eliciting Truthful Answers from a Language Model | NeurIPS 2023 |
| `zou2023representation` | Representation Engineering: A Top-Down Approach to AI Transparency | arXiv 2023 |
| `feng2026finegrained` | Fine-Grained Activation Steering: Steering Less, Achieving More | ICLR 2026 |

### Cluster 6: Datasets & Evaluation Tools（+4 篇，现有 5 篇）

| key | title | venue |
|-----|-------|-------|
| `conneau2018xnli` | XNLI: Evaluating Cross-lingual Sentence Representations | EMNLP 2018 |
| `rei2020comet` | COMET: A Neural Framework for MT Evaluation | EMNLP 2020 |
| `grattafiori2024llama` | The Llama 3 Herd of Models | arXiv 2024 |
| `yang2024qwen25` | Qwen2.5 Technical Report | arXiv 2024 |

所有 must_cite 论文均已找到并验证 URL。注意 ITI 论文实际发表于 2023 年（NeurIPS 2023），不是 2024。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 164473,
  "duration_api_ms": 230582,
  "num_turns": 22,
  "stop_reason": "end_turn",
  "session_id": "66968723-15fa-41d5-9793-62bb752e9bd1",
  "total_cost_usd": 0.99498775,
  "usage": {
    "input_tokens": 7591,
    "cache_creation_input_tokens": 37829,
    "cache_read_input_tokens": 407249,
    "output_tokens": 7694,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37829,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 415,
        "cache_read_input_tokens": 49541,
        "cache_creation_input_tokens": 129,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 129
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 158532,
      "outputTokens": 5219,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 14,
      "costUSD": 0.324627,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7591,
      "outputTokens": 7694,
      "cacheReadInputTokens": 407249,
      "cacheCreationInputTokens": 37829,
      "webSearchRequests": 0,
      "costUSD": 0.67036075,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b2d5c420-6b7c-4ccc-893d-c3ca801d4a19"
}
```

</details>

---
