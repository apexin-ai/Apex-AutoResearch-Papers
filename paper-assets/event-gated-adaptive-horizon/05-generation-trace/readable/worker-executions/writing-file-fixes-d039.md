# writing file fixes d039

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_writing_file-fixes-d039_20260515T062243.log`
- **Structured JSON:** [`9ad45d4abd752300676f.json`](../../sessions/9a/9ad45d4abd752300676f.json)

## Before a recorded user message

29 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
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
  "uuid": "32047d6d-d8f1-4f0a-89cb-4bf174722608",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1778842200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "649051f7-6987-4d2a-bcbb-d36f64d26b9b",
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me find and fix both files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "7bd74a98-345f-447e-ba8d-2a93539a322b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199PmKFxfUFBrpnBhqsUwEK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11211,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11211
      },
      "output_tokens": 30,
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

_source line 5_

查找并读取需要修改的文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "9fc1ec90-f012-4308-b188-dff449d0a603",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199PmKFxfUFBrpnBhqsUwEK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11211,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11211
      },
      "output_tokens": 30,
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

_source line 6_

<details open><summary>🔧 Tool call — Bash · `toolu_01VTF4ZavBKJaNSyjAh6v7DA`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon -name \"*related*\" -type f 2>/dev/null",
  "description": "Find related_work files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "ce3a9439-55b2-4eae-bde7-0847e8087d07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199PmKFxfUFBrpnBhqsUwEK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11211,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11211
      },
      "output_tokens": 30,
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

_source line 7 · 2026-05-15T06:22:56.499Z_

<details><summary>↩ Tool result · `toolu_01VTF4ZavBKJaNSyjAh6v7DA`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related_work_section_20260513T175837_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_research_verify-related-work_20260513T111219.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related-work-revision_20260515T044848_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related_work_section_20260513T175837.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related_work_revision_20260513T180340.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_write_related-work_20260513T085926_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_research_verify-related-work_20260513T111219_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_audit_related-work-reference-check_20260515T042836.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related-work-draft_20260515T042021_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related_work_revision_20260513T180340_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_write_related-work_20260513T085926.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_research_verify_related_work_20260513T164334_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related-work-draft_20260515T042021.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_audit_related-work-reference-check_20260515T042836_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_write_fix-related-work_20260513T090438.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related-work-revision_20260515T044848.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_research_verify_related_work_20260513T164334.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_write_fix-related-work_20260513T090438_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_research_verify_related_work_20260513T164334.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_audit_related-work-reference-check_20260515T042836.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_research_verify_related_work_20260513T164334.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_audit_related-work-reference-check_20260515T042836.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_section_6c6fde.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_draft_0456d1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_section.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "bb1de297-f648-4df1-84e4-e553d99a8f78",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related_work_section_20260513T175837_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_research_verify-related-work_20260513T111219.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related-work-revision_20260515T044848_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related_work_section_20260513T175837.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related_work_revision_20260513T180340.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_write_related-work_20260513T085926_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_research_verify-related-work_20260513T111219_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_audit_related-work-reference-check_20260515T042836.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related-work-draft_20260515T042021_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related_work_revision_20260513T180340_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_write_related-work_20260513T085926.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_research_verify_related_work_20260513T164334_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related-work-draft_20260515T042021.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_audit_related-work-reference-check_20260515T042836_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_write_fix-related-work_20260513T090438.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_related-work-revision_20260515T044848.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_research_verify_related_work_20260513T164334.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_write_fix-related-work_20260513T090438_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_research_verify_related_work_20260513T164334.jsonl\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_audit_related-work-reference-check_20260515T042836.jsonl\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_research_verify_related_work_20260513T164334.lock\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_audit_related-work-reference-check_20260515T042836.lock\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_section_6c6fde.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_draft_0456d1.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_section.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/paper_drafts/related_work_draft.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01UKGswaFi4SJriv6HsF8BEg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "f4d4bda9-cbc3-4e88-846a-6034a9812f48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0199PmKFxfUFBrpnBhqsUwEK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11211,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11211
      },
      "output_tokens": 30,
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

_source line 9 · 2026-05-15T06:22:56.901Z_

<details><summary>↩ Tool result · `toolu_01UKGswaFi4SJriv6HsF8BEg`</summary>

```text
1	# Literature Map — event-gated-adaptive-horizon
2	# Last updated: 2026-05-15
3	# Total: 76 papers (72 existing + 4 incremental scan 2026-05-15)
4	
5	# ============================================================
6	# EXISTING CITATIONS (already in paper.tex)
7	# ============================================================
8	
9	- paper_id: sutton1999options
10	  title: "Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning"
11	  authors: [Sutton R.S., Precup D., Singh S.]
12	  year: 1999
13	  venue: "Artificial Intelligence 112(1-2):181-211"
14	  category: background
15	  role: "Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL"
16	  relevance_score: 5
17	
18	- paper_id: hafner2020dreamerv1
19	  title: "Dream to Control: Learning Behaviors by Latent Imagination"
20	  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]
21	  year: 2020
22	  venue: ICLR
23	  category: background
24	  role: "DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm"
25	  relevance_score: 5
26	
27	- paper_id: hafner2023dreamerv3
28	  title: "Mastering Diverse Domains through World Models"
29	  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]
30	  year: 2023
31	  venue: "arXiv:2301.04104 (Nature 2025)"
32	  category: background
33	  role: "DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here"
34	  relevance_score: 5
35	
36	- paper_id: sharma2017figar
37	  title: "Fine Grained Action Repetition for Deep Reinforcement Learning"
38	  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]
39	  year: 2017
40	  venue: "ICLR Workshop"
41	  category: method-component
42	  role: "FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL"
43	  relevance_score: 4
44	
45	- paper_id: janner2019mbpo
46	  title: "When to Trust Your Model: Model-Based Policy Optimization"
47	  authors: [Janner M., Fu J., Zhang M., Levine S.]
48	  year: 2019
49	  venue: NeurIPS
50	  category: background
51	  role: "MBPO — formalizes model exploitation in MBRL; our conditioning-induced value overestimation (CIVO) is a specific instance of model exploitation tied to temporal embedding"
52	  relevance_score: 5
53	
54	# ============================================================
55	# NEW: Multi-step prediction error compounding
56	# ============================================================
57	
58	- paper_id: ke2019learning
59	  title: "Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future"
60	  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]
61	  year: 2019
62	  venue: ICLR
63	  category: background
64	  role: "Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1"
65	  relevance_score: 4
66	
67	- paper_id: asadi2019combating
68	  title: "Combating the Compounding-Error Problem with a Multi-step Model"
69	  authors: [Asadi K., Misra D., Kim S., Littman M.L.]
70	  year: 2019
71	  venue: "arXiv:1905.13320"
72	  category: background
73	  role: "Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error"
74	  relevance_score: 4
75	
76	- paper_id: venkatraman2015improving
77	  title: "Improving Multi-Step Prediction of Learned Time Series Models"
78	  authors: [Venkatraman A., Hebert M., Bagnell J.A.]
79	  year: 2015
80	  venue: AAAI
81	  category: background
82	  role: "Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error"
83	  relevance_score: 3
84	
85	- paper_id: lambert2022investigating
86	  title: "Investigating Compounding Prediction Errors in Learned Dynamics Models"
87	  authors: [Lambert N., Pister K.S.J., Calandra R.]
88	  year: 2022
89	  venue: "arXiv:2203.09637"
90	  category: background
91	  role: "Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead"
92	  relevance_score: 3
93	
94	# ============================================================
95	# NEW: Model-predictive control with learned dynamics
96	# ============================================================
97	
98	- paper_id: chua2018pets
99	  title: "Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models"
100	  authors: [Chua K., Calandra R., McAllister R., Levine S.]
101	  year: 2018
102	  venue: NeurIPS
103	  category: background
104	  role: "PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach"
105	  relevance_score: 3
106	
107	- paper_id: nagabandi2018neural
108	  title: "Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning"
109	  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]
110	  year: 2018
111	  venue: ICRA
112	  category: background
113	  role: "Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures"
114	  relevance_score: 3
115	
116	- paper_id: hansen2024tdmpc2
117	  title: "TD-MPC2: Scalable, Robust World Models for Continuous Control"
118	  authors: [Hansen N., Su H., Wang X.]
119	  year: 2024
120	  venue: "ICLR (arXiv:2310.16828)"
121	  category: background
122	  role: "TD-MPC2 — SOTA MPC planning route (online planning + learned dynamics); DMC benchmark leader but orthogonal to imagination-based training — reviewer defense: TD-MPC2 does online MPC rollouts at test time, we study actor-critic training via imagined rollouts (DreamerV3 paradigm), not a same-level comparison"
123	  relevance_score: 4
124	
125	# ============================================================
126	# NEW: Pessimistic MBRL / model exploitation mitigation
127	# ============================================================
128	
129	- paper_id: yu2020mopo
130	  title: "MOPO: Model-based Offline Policy Optimization"
131	  authors: [Yu T., Thomas G., Yu L., Ermon S., Zou J., Levine S., Finn C., Ma T.]
132	  year: 2020
133	  venue: "NeurIPS (arXiv:2005.13239)"
134	  category: background
135	  role: "MOPO — pessimistic MBRL via uncertainty-penalized reward (reward -= λ * model_uncertainty); generic model exploitation mitigation — reviewer defense: MOPO addresses distribution shift in offline MBRL, our dt=1 imagination restriction targets dt_embedding-induced CIVO (temporal conditioning corruption), two complementary mechanisms"
136	  relevance_score: 4
137	
138	# ============================================================
139	# NEW: Value overestimation mitigation
140	# ============================================================
141	
142	- paper_id: thrun1993issues
143	  title: "Issues in Using Function Approximation for Reinforcement Learning"
144	  authors: [Thrun S., Schwartz A.]
145	  year: 1993
146	  venue: "Connectionist Models Summer School"
147	  category: background
148	  role: "First identification of systematic value overestimation from function approximation; our CIVO extends this to model-based imagination with temporal conditioning"
149	  relevance_score: 4
150	
151	- paper_id: vanhasselt2016double
152	  title: "Deep Reinforcement Learning with Double Q-Learning"
153	  authors: [van Hasselt H., Guez A., Silver D.]
154	  year: 2016
155	  venue: AAAI
156	  category: background
157	  role: "Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL"
158	  relevance_score: 4
159	
160	- paper_id: fujimoto2018td3
161	  title: "Addressing Function Approximation Error in Actor-Critic Methods"
162	  authors: [Fujimoto S., van Hoof H., Meger D.]
163	  year: 2018
164	  venue: ICML
165	  category: method-component
166	  role: "TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify"
167	  relevance_score: 4
168	
169	- paper_id: haarnoja2018sac
170	  title: "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor"
171	  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]
172	  year: 2018
173	  venue: ICML
174	  category: method-component
175	  role: "SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values"
176	  relevance_score: 3
177	
178	- paper_id: lee2021sunrise
179	  title: "SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning"
180	  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]
181	  year: 2021
182	  venue: ICML
183	  category: method-component
184	  role: "Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified CIVO mechanism"
185	  relevance_score: 3
186	
187	# ============================================================
188	# NEW: Delusional bias
189	# ============================================================
190	
191	- paper_id: lu2018nondelusional
192	  title: "Non-delusional Q-learning and Value-Iteration"
193	  authors: [Lu T., Schuurmans D., Boutilier C.]
194	  year: 2018
195	  venue: NeurIPS
196	  category: background
197	  role: "Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision"
198	  relevance_score: 5
199	
200	# ============================================================
201	# NEW: Hierarchical RL with learned models
202	# ============================================================
203	
204	- paper_id: hafner2022director
205	  title: "Deep Hierarchical Planning from Pixels"
206	  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]
207	  year: 2022
208	  venue: NeurIPS
209	  category: direct-competitor
210	  role: "Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt"
211	  relevance_score: 4
212	
213	- paper_id: nachum2018hiro
214	  title: "Data-Efficient Hierarchical Reinforcement Learning"
215	  authors: [Nachum O., Gu S., Lee H., Levine S.]
216	  year: 2018
217	  venue: NeurIPS
218	  category: background
219	  role: "HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed"
220	  relevance_score: 3
221	
222	# ============================================================
223	# NEW: Action repeat / frame skip
224	# ============================================================
225	
226	- paper_id: braylan2015frame
227	  title: "Frame Skip Is a Powerful Parameter for Learning to Play Atari"
228	  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]
229	  year: 2015
230	  venue: "AAAI Workshop on Learning for General Competency in Video Games"
231	  category: background
232	  role: "Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice"
233	  relevance_score: 3
234	
235	- paper_id: lakshminarayanan2017dynamic
236	  title: "Dynamic Action Repetition for Deep Reinforcement Learning"
237	  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]
238	  year: 2017
239	  venue: AAAI
240	  category: method-component
241	  role: "Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach"
242	  relevance_score: 4
243	
244	- paper_id: biedenkapp2021temporl
245	  title: "TempoRL: Learning When to Act"
246	  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]
247	  year: 2021
248	  venue: ICML
249	  category: method-component
250	  role: "Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify"
251	  relevance_score: 4
252	
253	# ============================================================
254	# NEW: DreamerV2
255	# ============================================================
256	
257	- paper_id: hafner2021dreamerv2
258	  title: "Mastering Atari with Discrete World Models"
259	  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]
260	  year: 2021
261	  venue: ICLR
262	  category: background
263	  role: "DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system"
264	  relevance_score: 5
265	
266	# ============================================================
267	# NEW: Alternative world model architectures
268	# ============================================================
269	
270	- paper_id: micheli2023iris
271	  title: "Transformers are Sample-Efficient World Models"
272	  authors: [Micheli V., Alonso E., Fleuret F.]
273	  year: 2023
274	  venue: ICLR
275	  category: background
276	  role: "IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction"
277	  relevance_score: 3
278	
279	- paper_id: robine2023twm
280	  title: "Transformer-based World Models Are Happy With 100k Interactions"
281	  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]
282	  year: 2023
283	  venue: ICLR
284	  category: background
285	  role: "TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap"
286	  relevance_score: 3
287	
288	- paper_id: chen2022transdreamer
289	  title: "TransDreamer: Reinforcement Learning with Transformer World Models"
290	  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]
291	  year: 2022
292	  venue: "arXiv:2202.09481"
293	  category: background
294	  role: "Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures"
295	  relevance_score: 3
296	
297	# ============================================================
298	# NEW: 2024-2026 concurrent work on temporal abstraction in world models
299	# ============================================================
300	
301	- paper_id: gumbsch2024thick
302	  title: "Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics"
303	  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]
304	  year: 2024
305	  venue: ICLR
306	  category: direct-competitor
307	  role: "THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination"
308	  relevance_score: 5
309	
310	- paper_id: mattes2024hieros
311	  title: "Hieros: Hierarchical Imagination on Structured State Space Sequence World Models"
312	  authors: [Mattes P., Schlosser R., Herbrich R.]
313	  year: 2024
314	  venue: ICML
315	  category: direct-competitor
316	  role: "Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify"
317	  relevance_score: 5
318	
319	# ============================================================
320	# NEW: Seed-dependent instability & value overestimation in MBRL
321	# ============================================================
322	
323	- paper_id: henderson2018deep
324	  title: "Deep Reinforcement Learning that Matters"
325	  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]
326	  year: 2018
327	  venue: AAAI
328	  category: background
329	  role: "Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config"
330	  relevance_score: 4
331	
332	- paper_id: nikishin2022primacy
333	  title: "The Primacy Bias in Deep Reinforcement Learning"
334	  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]
335	  year: 2022
336	  venue: ICML
337	  category: background
338	  role: "Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent"
339	  relevance_score: 4
340	
341	- paper_id: qiao2023mind
342	  title: "Mind the Model, Not the Agent: The Primacy Bias in Model-based RL"
343	  authors: [Qiao Z., Lyu J., Li X.]
344	  year: 2023
345	  venue: "arXiv:2310.15017 (ECAI 2024)"
346	  category: evaluation
347	  role: "Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't"
348	  relevance_score: 5
349	
350	- paper_id: hussing2024dissecting
351	  title: "Dissecting Deep RL with High Update Ratios: Combatting Value Divergence"
352	  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]
353	  year: 2024
354	  venue: "Reinforcement Learning Journal (RLC 2024)"
355	  category: evaluation
356	  role: "Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our CIVO where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization"
357	  relevance_score: 4
358	
359	- paper_id: barkley2024stealing
360	  title: "Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning"
361	  authors: [Barkley B., Fridovich-Keil D.]
362	  year: 2024
363	  venue: "arXiv:2412.14312 (ICML 2025)"
364	  category: evaluation
365	  role: "Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix"
366	  relevance_score: 3
367	
368	- paper_id: bjorck2022variance
369	  title: "Is High Variance Unavoidable in RL? A Case Study in Continuous Control"
370	  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]
371	  year: 2022
372	  venue: ICLR
373	  category: background
374	  role: "Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability"
375	  relevance_score: 3
376	
377	# ============================================================
378	# NEW: Reward prediction quality → MBRL performance
379	# ============================================================
380	# Our key finding: removing dt_embedding causes reward_MAE to spike 75x
381	# (0.01 → 0.747), making performance seed-dependent. These papers
382	# establish that reward prediction quality is a known MBRL bottleneck.
383	
384	- paper_id: lee2024dreamsmooth
385	  title: "DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing"
386	  authors: [Lee V., Abbeel P., Lee Y.]
387	  year: 2024
388	  venue: ICLR
389	  category: background
390	  role: "Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x"
391	  relevance_score: 5
392	
393	- paper_id: ma2024harmonydream
394	  title: "HarmonyDream: Task Harmonization Inside World Models"
395	  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]
396	  year: 2024
397	  venue: ICML
398	  category: background
399	  role: "Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion"
400	  relevance_score: 5
401	
402	- paper_id: lambert2020objective
403	  title: "Objective Mismatch in Model-based Reinforcement Learning"
404	  authors: [Lambert N., Amos B., Yadan O., Calandra R.]
405	  year: 2020
406	  venue: "L4DC (Proceedings of Machine Learning Research, vol. 120)"
407	  category: background
408	  role: "Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch"
409	  relevance_score: 4
410	
411	# ============================================================
412	# NEW: Auxiliary tasks & representation coupling in world models
413	# ============================================================
414	# Our finding: reward prediction quality is tightly coupled to temporal
415	# conditioning (dt_embedding). Removing the embedding degrades the
416	# reward head while dynamics remain intact — suggesting the reward head
417	# acts as more than a passive predictor; it conditions the shared
418	# representation. Literature gap: no prior work studies this coupling
419	# specifically in Dreamer-family world models.
420	
421	- paper_id: jaderberg2017unreal
422	  title: "Reinforcement Learning with Unsupervised Auxiliary Tasks"
423	  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]
424	  year: 2017
425	  venue: ICLR
426	  category: background
427	  role: "UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction"
428	  relevance_score: 4
429	
430	- paper_id: lyle2021auxiliary
431	  title: "On The Effect of Auxiliary Tasks on Representation Dynamics"
432	  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]
433	  year: 2021
434	  venue: AISTATS
435	  category: background
436	  role: "Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space"
437	  relevance_score: 4
438	
439	# ============================================================
440	# NEW: DreamerV3 architecture improvements (2025-2026)
441	# ============================================================
442	
443	- paper_id: bredis2026nedreamer
444	  title: "Next Embedding Prediction Makes World Models Stronger"
445	  authors: [Bredis G., Balagansky N., Gavrilov D., Rakhimov R.]
446	  year: 2026
447	  venue: "arXiv:2603.02765"
448	  category: background
449	  role: "NE-Dreamer — decoder-free MBRL replacing pixel reconstruction with next-embedding prediction via temporal transformer + Barlow Twins; improves RSSM prediction quality on DMC and DMLab but does not address temporal abstraction or CIVO — orthogonal to our dt-embedding diagnosis"
450	  relevance_score: 3
451	
452	- paper_id: zhang2025dymodreamer
453	  title: "DyMoDreamer: World Modeling with Dynamic Modulation"
454	  authors: [Zhang B., Wang R., Xiao W., Zhang W., Sun J., Huang G., Chen J., Wang G.]
455	  year: 2025
456	  venue: NeurIPS
457	  category: background
458	  role: "Modulates RSSM via inter-frame differencing mask and stochastic categorical dynamic modulation; SOTA on Atari 100k (156.6% HNS) and DMC (832) — improves dynamics extraction but does not address variable-rate imagination or dt_embedding-induced value overestimation"
459	  relevance_score: 3
460	
461	# ============================================================
462	# NEW: Temporal abstraction methods
463	# ============================================================
464	
465	- paper_id: liu2025vanta
466	  title: "Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning"
467	  authors: [Liu T.-S., Liu X.-H., Chen R., Jin L., Wang P., Zhang Z., Yu Y.]
468	  year: 2025
469	  venue: ICLR
470	  category: method-component
471	  role: "VanTA — VLM-guided trajectory decomposition into semantically meaningful skills via vector quantization + relabeling; operates at high-level skill abstraction (Franka Kitchen, Crafter) — contrasts with our low-level dt-based temporal abstraction within world-model imagination steps"
472	  relevance_score: 3
473	
474	# ============================================================
475	# NEW: Evaluation methodology
476	# ============================================================
477	
478	- paper_id: agarwal2021precipice
479	  title: "Deep Reinforcement Learning at the Edge of the Statistical Precipice"
480	  authors: [Agarwal R., Schwarzer M., Castro P.S., Courville A.C., Bellemare M.]
481	  year: 2021
482	  venue: NeurIPS
483	  category: evaluation
484	  role: "Proposes rliable — interval estimates, performance profiles, IQM for robust multi-seed RL evaluation (NeurIPS Outstanding Paper); our multi-seed experiment design follows this methodology to ensure statistical validity of collapse detection across seeds"
485	  relevance_score: 4
486	
487	# ============================================================
488	# NEW (2026-05-14 gap analysis): Time discretization theory
489	# ============================================================
490	# Gap: variable timestep / time discretization invariance — foundational
491	# theory for why dt matters and how to handle it.
492	
493	- paper_id: tallec2019making
494	  title: "Making Deep Q-learning methods Robust to Time Discretization"
495	  authors: [Tallec C., Blier L., Ollivier Y.]
496	  year: 2019
497	  venue: "ICML (arXiv:1901.09732)"
498	  category: background
499	  role: "Shows Q-learning performance is highly sensitive to time discretization δ; proposes architectural + exploration modifications for δ-invariance. Theoretical foundation for why our variable-dt imagination introduces a fundamental difficulty: RSSM trained at δ=1 cannot produce δ-invariant predictions at dt>1"
500	  relevance_score: 4
501	
502	- paper_id: park2021sar
503	  title: "Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods"
504	  authors: [Park S., Kim J., Kim G.]
505	  year: 2021
506	  venue: "NeurIPS (arXiv:2111.03941)"
507	  category: method-component
508	  role: "SAR — δ-invariant action repetition for policy gradients; achieves time-discretization robustness in model-free RL via adaptive reaction to state changes during repetition. Contrasts with our finding that world-model RL lacks this robustness when imagination uses dt>1"
509	  relevance_score: 4
510	
511	- paper_id: wang2024seac
512	  title: "Reinforcement Learning with Elastic Time Steps"
513	  authors: [Wang D., Beltrame G.]
514	  year: 2024
515	  venue: "arXiv:2402.14961"
516	  category: method-component
517	  role: "SEAC/MOSEAC — variable-duration time steps where agent selects both action and duration; model-free approach that explicitly treats action duration as part of the action space. Our work reveals why this strategy is problematic in world-model RL: the critic cannot reliably evaluate variable-duration imagined trajectories"
518	  relevance_score: 3
519	
520	# ============================================================
521	# NEW (2026-05-14 gap analysis): Delusional bias mitigation
522	# ============================================================
523	
524	- paper_id: su2020conqur
525	  title: "ConQUR: Mitigating Delusional Bias in Deep Q-learning"
526	  authors: [Su D., Ooi J., Lu T., Schuurmans D., Boutilier C.]
527	  year: 2020
528	  venue: "ICML (arXiv:2002.12399)"
529	  category: background
530	  role: "Follow-up to Lu et al. 2018; mitigates delusional bias via consistency-penalized Q-labels. Addresses delusional bias from policy-class constraints in Q-learning; our CIVO is an analogous phenomenon in MBRL where temporal conditioning (dt_embedding) creates inconsistent value targets across imagination steps"
531	  relevance_score: 4
532	
533	# ============================================================
534	# NEW (2026-05-14 gap analysis): Diagnostic methodology in RL
535	# ============================================================
536	# Gap: our paper is a diagnostic analysis — need methodological
537	# precedents for "what matters" / "implementation matters" style papers.
538	
539	- paper_id: engstrom2020implementation
540	  title: "Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO"
541	  authors: [Engstrom L., Ilyas A., Santurkar S., Tsipras D., Janoos F., Rudolph L., Madry A.]
542	  year: 2020
543	  venue: "ICLR (arXiv:2005.12729)"
544	  category: evaluation
545	  role: "Demonstrates that code-level implementation details (not algorithmic innovations) drive most of PPO's gains over TRPO; methodological precedent for our diagnostic approach — we similarly show that a specific implementation choice (trained vs. untrained dt_embedding) is the primary factor determining collapse vs. stability"
546	  relevance_score: 4
547	
548	- paper_id: andrychowicz2021whatmatters
549	  title: "What Matters for On-Policy Deep Actor-Critic Methods? A Large-Scale Study"
550	  authors: [Andrychowicz M., Raichuk A., Stańczyk P., Orsini M., Girgin S., Marinier R., Hussenot L., Geist M., Pietquin O., Michalski M., Gelly S., Bachem O.]
551	  year: 2021
552	  venue: "ICLR (arXiv:2006.05990)"
553	  category: evaluation
554	  role: "Large-scale factorial study of 50+ design choices in on-policy RL (250K+ agents); methodological template for our factorial experiment design isolating dt_embedding × subsample × horizon effects. Demonstrates that systematic ablation reveals non-obvious interactions — parallel to our finding that dt_embedding training status interacts with subsample and horizon"
555	  relevance_score: 4
556	
557	# ============================================================
558	# NEW (2026-05-14 gap analysis): MBRL rollout quality & value overestimation
559	# ============================================================
560	# Gap: recent ICLR 2025 papers directly studying imagination rollout
561	# quality and value overestimation in model-based settings.
562	
563	- paper_id: frauenknecht2025rollouts
564	  title: "On Rollouts in Model-Based Reinforcement Learning"
565	  authors: [Frauenknecht B., Subhasish D., Solowjow F., Trimpe S.]
566	  year: 2025
567	  venue: "ICLR (arXiv:2501.16918)"
568	  category: evaluation
569	  role: "Shows trajectory-sampling rollouts diverge from ground truth after few steps and can harm policy learning; proposes Infoprop separating aleatoric/epistemic uncertainty with rollout termination criteria. Directly supports our finding that dt>1 imagination produces corrupted data — our work identifies a specific mechanism (dt_embedding-induced value exploitation) beyond general compounding error"
570	  relevance_score: 5
571	
572	- paper_id: voelcker2025madtd
573	  title: "MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL"
574	  authors: [Voelcker C., Hussing M., Eaton E., Farahmand A.-M., Gilitschenski I.]
575	  year: 2025
576	  venue: "ICLR (arXiv:2410.08896)"
577	  category: evaluation
578	  role: "Shows value function misgeneralization to on-policy actions causes instability at high UTD ratios; uses model-generated data to improve value accuracy. Complementary to our finding: MAD-TD addresses value misgeneralization from replay distribution mismatch, we address value overestimation from temporal conditioning corruption in imagination"
579	  relevance_score: 4
580	
581	# ============================================================
582	# NEW (2026-05-14 gap analysis): Latest action repeat methods
583	# ============================================================
584	
585	- paper_id: nie2025sdar
586	  title: "Select before Act: Spatially Decoupled Action Repetition for Continuous Control"
587	  authors: [Nie B., et al.]
588	  year: 2025
589	  venue: "ICLR (arXiv:2502.06919)"
590	  category: method-component
591	  role: "SDAR — per-dimension action repetition decisions for flexible temporal persistence in model-free RL; SOTA on DMC continuous control. Advances action repeat in model-free setting; our work shows the fundamental obstacle to analogous variable-rate approaches in model-based RL (CIVO from dt_embedding)"
592	  relevance_score: 3
593	
594	# ============================================================
595	# NEW (2026-05-14 gap analysis): DreamerV4 / latest Dreamer evolution
596	# ============================================================
597	
598	- paper_id: hafner2025dreamerv4
599	  title: "Training Agents Inside of Scalable World Models"
600	  authors: [Hafner D., Yan W., Lillicrap T.]
601	  year: 2025
602	  venue: "arXiv:2509.24527"
603	  category: background
604	  role: "DreamerV4 — replaces RSSM with efficient transformer world model + shortcut forcing; scales to video pretraining (Minecraft diamonds from video). Architectural successor to DreamerV3; our dt_embedding diagnosis is specific to RSSM but the broader lesson (temporal conditioning must match model fidelity) applies to transformer world models"
605	  relevance_score: 4
606	
607	# ============================================================
608	# NEW (2026-05-14): Training instability dynamics
609	# ============================================================
610	
611	- paper_id: zhang2026instability
612	  title: "Training instability in deep learning follows low-dimensional dynamical principles"
613	  authors: [Zhang L., et al.]
614	  year: 2026
615	  venue: "ICLR 2026 (arXiv:2601.13160)"
616	  category: background
617	  role: "Training instability follows low-dimensional dynamical principles; provides theoretical framework for why seed-dependent collapse vs self-correction occurs in our experiments (008d seed 1 collapses, 009b seed 2 self-corrects under identical config)"
618	  relevance_score: 5
619	
620	# ============================================================
621	# NEW (2026-05-14): Seed-Dependent Stochastic Outcomes in MBRL
622	# ============================================================
623	# Dedicated literature survey for the stochastic collapse phenomenon:
624	# same config (trained dt_embedding + subsample + H=8) produces
625	# collapse in seed 0 (008d) but self-correction in seed 2 (009b).
626	# nve>1.5x is a 100% reliable marker of trained dt_embedding,
627	# but collapse itself is stochastic (1/2 seeds).
628	
629	- paper_id: sokar2023dormant
630	  title: "The Dormant Neuron Phenomenon in Deep Reinforcement Learning"
631	  authors: [Sokar G., Agarwal R., Castro P.S., Evci U.]
632	  year: 2023
633	  venue: "ICML 2023"
634	  category: background
635	  role: "Identifies dormant neurons — inactive units accumulating during RL training that reduce network expressivity. Seed-dependent because different random initializations produce different early dormancy patterns; directly explains why some seeds lose the representational capacity needed to self-correct value overestimation (our seed 0 collapses) while others retain enough active neurons to recover (our seed 2 self-corrects)"
636	  relevance_score: 4
637	  survey_tag: seed-dependent-stochastic-outcomes
638	
639	- paper_id: lyle2022capacity
640	  title: "Understanding and Preventing Capacity Loss in Reinforcement Learning"
641	  authors: [Lyle C., Rowland M., Dabney W.]
642	  year: 2022
643	  venue: "ICLR 2023 (arXiv:2204.09560)"
644	  category: background
645	  role: "Shows feature rank collapse from non-stationary TD targets is a necessary condition for learning failure but not sufficient — sparse rewards and other factors must co-occur. Directly parallels our finding: nve>1.5x (value overestimation from trained dt_embedding) is a necessary precondition for collapse but not a sufficient one; additional stochastic factors (initialization, early replay composition) determine whether collapse actually occurs"
646	  relevance_score: 5
647	  survey_tag: seed-dependent-stochastic-outcomes
648	
649	- paper_id: kumar2022dr3
650	  title: "DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization"
651	  authors: [Kumar A., Agarwal R., Ma T., Courville A., Tucker G., Levine S.]
652	  year: 2022
653	  venue: "ICLR 2022"
654	  category: background
655	  role: "Shows implicit regularization from TD learning favors degenerate feature aliasing (states on both sides of Bellman backup become indistinguishable), creating the substrate for value overestimation. In our setting, trained dt_embedding amplifies this aliasing across different temporal horizons — the critic cannot distinguish between dt=1 and dt>1 value targets, enabling exploitation. Feature aliasing is seed-dependent because it depends on initialization geometry"
656	  relevance_score: 4
657	  survey_tag: seed-dependent-stochastic-outcomes
658	
659	- paper_id: colas2018seeds
660	  title: "How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments"
661	  authors: [Colas C., Sigaud O., Oudeyer P.-Y.]
662	  year: 2018
663	  venue: "arXiv:1806.08295"
664	  category: evaluation
665	  role: "Provides statistical framework for determining seed count needed for significant algorithm comparison; our 2-seed observation (1/2 collapse) has limited statistical power by their analysis — but the qualitative difference (nve 4.12x vs 0.38x) is large enough that even 2 seeds establish the stochastic nature of the phenomenon. Methodological basis for future multi-seed validation"
666	  relevance_score: 3
667	  survey_tag: seed-dependent-stochastic-outcomes
668	
669	- paper_id: nikishin2023plasticity
670	  title: "Deep Reinforcement Learning with Plasticity Injection"
671	  authors: [Nikishin E., Oh J., Ostrovski G., Lyle C., Pascanu R., Dabney W., Barreto A.]
672	  year: 2023
673	  venue: "NeurIPS 2023"
674	  category: method-component
675	  role: "Plasticity injection augments network plasticity without changing parameter count; serves as a diagnostic tool — if injection improves performance, plasticity loss was the bottleneck. Directly applicable to diagnosing whether our seed-dependent collapse is plasticity-mediated: if plasticity injection prevents collapse in seed 0 but has no effect on seed 2 (which already self-corrects), it confirms plasticity loss as the bifurcation mechanism"
676	  relevance_score: 4
677	  survey_tag: seed-dependent-stochastic-outcomes
678	
679	- paper_id: schwarzer2023bbf
680	  title: "Bigger, Better, Faster: Human-level Atari with Human-level Efficiency"
681	  authors: [Schwarzer M., Obando-Ceron J.S., Courville A., Bellemare M., Agarwal R., Castro P.S.]
682	  year: 2023
683	  venue: "ICML 2023"
684	  category: method-component
685	  role: "BBF achieves SOTA sample efficiency via periodic network resets + scaling + weight decay; periodic resets prevent primacy bias accumulation across seeds. Suggests our CIVO collapse might be preventable with periodic critic resets — the reset would break the positive feedback loop between overestimated values and actor exploitation before it becomes irreversible"
686	  relevance_score: 3
687	  survey_tag: seed-dependent-stochastic-outcomes
688	
689	- paper_id: farebrother2024stopregressing
690	  title: "Stop Regressing: Training Value Functions via Classification for Scalable Deep RL"
691	  authors: [Farebrother J., Orbay J., Vuong Q., Taiga A.A., Chebotar Y., Xiao T., Irpan A., Levine S., Castro P.S., Faust A., Kumar A., Agarwal R.]
692	  year: 2024
693	  venue: "ICML 2024"
694	  category: method-component
695	  role: "Shows categorical cross-entropy for value training provides implicit regularization against overestimation vs MSE regression. DreamerV3 already uses categorical value prediction (twohot + symlog) — yet our trained dt_embedding still induces collapse in some seeds, demonstrating that categorical value training is insufficient to prevent dt_embedding-induced value exploitation"
696	  relevance_score: 3
697	  survey_tag: seed-dependent-stochastic-outcomes
698	
699	- paper_id: lyle2024normalization
700	  title: "Normalization and Effective Learning Rates in Reinforcement Learning"
701	  authors: [Lyle C., Zheng Z., Giunchiglia E., Sherstan C., Hashemizadeh M., Schuurmans D., Dabney W.]
702	  year: 2024
703	  venue: "NeurIPS 2024"
704	  category: background
705	  role: "Shows normalization layers combat overestimation but cause effective learning rate decay via parameter norm growth. Provides a potential mechanism for seed 2's self-correction: if parameter norms grow faster in certain initializations, effective LR decays faster, naturally damping value overestimation before it cascades into collapse. Seed 0's slower norm growth → sustained high effective LR → overestimation compounds → collapse"
706	  relevance_score: 4
707	  survey_tag: seed-dependent-stochastic-outcomes
708	
709	# --- Survey synthesis: Seed-Dependent Stochastic Outcomes ---
710	# Summary (2026-05-14):
711	#
712	# 1. STOCHASTIC COLLAPSE HAS PRECEDENT:
713	#    Plasticity loss (Lyle 2022, Sokar 2023, Nikishin 2023) is inherently
714	#    seed-dependent because it depends on initialization → early gradient
715	#    dynamics → neuron activity patterns. Different seeds hit different
716	#    plasticity trajectories under identical configs.
717	#
718	# 2. nve>1.5x AS DIAGNOSTIC MARKER (necessary but not sufficient):
719	#    Lyle 2022 shows feature rank collapse is necessary but not sufficient
720	#    for learning failure. Kumar 2022 shows feature aliasing from TD
721	#    learning creates the overestimation substrate. Our nve>1.5x is
722	#    analogous: it indicates the dt_embedding has enabled value exploitation
723	#    (100% reliable marker), but collapse requires additional conditions
724	#    (plasticity loss, insufficient effective LR decay) that are stochastic.
725	#
726	# 3. SELF-CORRECTION MECHANISM:
727	#    Lyle 2024 provides a candidate mechanism: normalization-induced
728	#    effective LR decay can naturally damp overestimation in some seeds.
729	#    Farebrother 2024 shows categorical value training provides partial
730	#    implicit regularization. Together these explain why seed 2 self-corrects:
731	#    the combination of DreamerV3's categorical critic + normalization +
732	#    favorable initialization produces enough implicit regularization to
733	#    overcome the dt_embedding-induced overestimation.
734	#
735	# 4. THEORETICAL GROUNDING:
736	#    Zhang 2026 (already in map) provides the dynamical systems framework.
737	#    Bjorck 2022 (already in map) shows early outlier events dominate
738	#    variance. Together with the new papers, the framing is:
739	#    "trained dt_embedding creates a necessary condition (nve>1.5x) for
740	#    CIVO collapse, but collapse is a stochastic bifurcation
741	#    whose outcome depends on seed-dependent plasticity dynamics."
742	
743	# ============================================================
744	# INCREMENTAL SCAN (2026-05-14): Δt conditioning & adaptive horizon
745	# ============================================================
746	# 8 new papers from targeted search on:
747	#   - Δt/timestep conditioning in world models
748	#   - Variable-rate imagination / adaptive horizon
749	#   - Hierarchical planning with latent world models (2025-2026)
750	#
751	# KEY FINDING: TAWM (Nhu et al. ICML 2025) explicitly conditions
752	# world model on Δt — closest methodological overlap. But TAWM
753	# uses TD-MPC2 (online MPC) not imagination-based actor-critic,
754	# and treats Δt conditioning as beneficial. Our work diagnoses
755	# Δt conditioning as pathological in imagination-based training
756	# (CIVO). Complementary, not duplicative.
757	
758	- paper_id: nhu2025tawm
759	  title: "Time-Aware World Model for Adaptive Prediction and Control"
760	  authors: [Nhu A.N., Son S., Lin M.C.]
761	  year: 2025
762	  venue: "ICML 2025 (arXiv:2506.08441)"
763	  category: direct-competitor
764	  role: "TAWM — explicitly conditions world model on time-step size Δt and trains over diverse Δt values for multi-rate dynamics learning. Built on TD-MPC2 (online MPC). KEY DISTINCTION from our work: (1) TAWM treats Δt conditioning as beneficial for performance/data-efficiency; we diagnose it as pathological in imagination-based actor-critic training (CIVO). (2) TAWM uses MPC (no imagination rollouts for policy training); our failure mode is specific to imagination-based training where the critic exploits dt-conditioned value estimates. (3) TAWM focuses on observation-rate robustness; we focus on value overestimation from temporal conditioning corruption. TAWM actually strengthens our contribution: it shows Δt conditioning works in MPC settings, making our finding that it fails in imagination-based settings a surprising and important diagnostic."
765	  relevance_score: 5
766	  novelty_threat: "MEDIUM — methodological overlap (Δt conditioning) but fundamentally different paradigm (MPC vs imagination) and opposite conclusion (beneficial vs pathological). Must cite and differentiate in paper."
767	
768	- paper_id: li2025lsimagine
769	  title: "Open-World Reinforcement Learning over Long Short-Term Imagination"
770	  authors: [Li J., Wang Q., Wang Y., Jin X., Li Y., Zeng W., Yang X.]
771	  year: 2025
772	  venue: "ICLR 2025 Oral (arXiv:2410.03618)"
773	  category: direct-competitor
774	  role: "LS-Imagine — extends imagination horizon in Dreamer via goal-conditioned jumpy state transitions and affordance maps. Addresses the 'short-sightedness' of standard Dreamer imagination. KEY DISTINCTION: LS-Imagine adds jumpy transitions to reach long-horizon targets (open-world Minecraft), while our work shows that variable-dt imagination itself introduces CIVO. LS-Imagine's jumpy transitions use goal conditioning (not dt-embedding), potentially avoiding the value overestimation we identify."
775	  relevance_score: 4
776	  novelty_threat: "LOW — different mechanism (goal-conditioned jumps vs dt-embedding) and different focus (long-horizon exploration vs diagnostic of failure modes). Should cite as concurrent approach to extending imagination horizon."
777	
778	- paper_id: zhang2026hwm
779	  title: "Hierarchical Planning with Latent World Models"
780	  authors: [Zhang W., Terver B., Zholus A., Chitnis S., Sutaria H., Assran M., Balestriero R., Bar A., Bardes A., LeCun Y., Ballas N.]
781	  year: 2026
782	  venue: "arXiv:2604.03208"
783	  category: direct-competitor
784	  role: "HWM — learns multi-scale latent world models for hierarchical MPC planning; high-level planner optimizes macro-actions, low-level planner handles primitives. 70% success on real-world non-greedy robotic tasks vs 0% for single-level. Addresses temporal abstraction via hierarchical planning (MPC), not imagination-based actor-critic. Further evidence that temporal abstraction in world models requires hierarchy rather than single-scale variable-dt approaches."
785	  relevance_score: 4
786	  novelty_threat: "LOW — MPC-based hierarchical planning, not imagination-based training. Supports our thesis that flat dt-embedding approaches are inferior to hierarchical alternatives."
787	
788	- paper_id: kobayashi2025metacontroller
789	  title: "Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning"
790	  authors: [Kobayashi S., et al.]
791	  year: 2025
792	  venue: "arXiv:2512.20605"
793	  category: method-component
794	  role: "MetaController — discovers temporal abstractions via higher-order non-causal sequence model controlling base autoregressive model's residual stream. Each controller executes behaviorally meaningful action sequences with learned termination conditions. Operates in fundamentally different paradigm (LLM-style autoregressive models, not world-model imagination), but demonstrates that temporal abstraction benefits from hierarchical structure rather than flat dt-conditioning."
795	  relevance_score: 3
796	
797	- paper_id: shaj2023mts3
798	  title: "Multi Time Scale World Models"
799	  authors: [Shaj V., Gholam Zadeh S., Demir O., Douat L.R., Neumann G.]
800	  year: 2023
801	  venue: "NeurIPS 2023 (arXiv:2310.18534)"
802	  category: method-component
803	  role: "MTS3 — probabilistic multi-time-scale state space model with fast and slow latent dynamics for variable-rate prediction. Provides efficient inference across temporal scales. Foundational multi-rate dynamics architecture; our work shows that even with proper multi-rate modeling, the downstream actor-critic training in imagination can exploit temporal conditioning for value overestimation — a failure mode MTS3 does not address (it focuses on prediction quality, not policy training)."
804	  relevance_score: 4
805	
806	- paper_id: splates2025
807	  title: "Stable Planning with Temporally Extended Skills"
808	  authors: [SPlaTES authors]
809	  year: 2025
810	  venue: "Reinforcement Learning Journal (RLC 2025)"
811	  category: method-component
812	  role: "SPlaTES — hierarchical MPC with temporally extended skills + abstract skill world model. Skill learning via mutual-information objective yields diverse, predictable, task-related behavior. Demonstrates that stable long-horizon planning requires modeling skill outcomes (temporal abstraction via hierarchy), not primitive-action outcomes at variable time steps — consistent with our finding that flat dt-embedding fails."
813	  relevance_score: 3
814	
815	- paper_id: beckerehmck2023multitimestep
816	  title: "Multi-timestep models for Model-based Reinforcement Learning"
817	  authors: [Becker-Ehmck P., Peters J., van der Smagt P.]
818	  year: 2023
819	  venue: "arXiv:2310.05672"
820	  category: background
821	  role: "Proposes multi-timestep training objective (weighted sum of losses at various future horizons) for one-step dynamics models to improve long-horizon R² score. Addresses compounding error at the model training level; our work shows that even with perfect multi-step prediction, the imagination-based actor-critic can still fail due to value overestimation from dt-conditioning — a downstream failure mode distinct from prediction accuracy."
822	  relevance_score: 3
823	
824	- paper_id: liu2022dmve
825	  title: "Dynamic-Horizon Model-Based Value Estimation With Latent Imagination"
826	  authors: [Liu Y., et al.]
827	  year: 2022
828	  venue: "IEEE TNNLS (arXiv:2009.09593)"
829	  category: background
830	  role: "DMVE — adaptive rollout horizon selection via horizon reliability detection (comparing value expansion errors between raw and reconstructed observations). Addresses the horizon selection problem in imagination-based value estimation. Complementary to our work: DMVE selects among fixed-dt horizons; we show that even optimal horizon selection cannot fix the CIVO when dt-embedding is trained (the overestimation is in the value function, not the horizon length)."
831	  relevance_score: 3
832	
833	# --- Incremental scan synthesis (2026-05-14) ---
834	#
835	# NOVELTY ASSESSMENT:
836	# No paper found that diagnoses dt_embedding → CIVO
837	# (value overestimation) → stochastic collapse in imagination-based
838	# MBRL. Our core contribution remains novel.
839	#
840	# TAWM (ICML 2025) is the closest methodological overlap but
841	# operates in MPC paradigm and reaches opposite conclusion
842	# (Δt conditioning is beneficial). This actually STRENGTHENS
843	# our novelty: "Δt conditioning helps in MPC but hurts in
844	# imagination-based training" is a more nuanced and surprising finding.
845	#
846	# LANDSCAPE TREND:
847	# The field is converging on HIERARCHY (THICK, Hieros, Director,
848	# HWM, SPlaTES, MetaController) as the solution to temporal
849	# abstraction in world models, avoiding flat variable-dt approaches.
850	# Our diagnostic paper explains WHY flat dt approaches fail,
851	# providing theoretical grounding for this empirical trend.
852	#
853	# ACTION ITEMS FOR PAPER:
854	# 1. MUST CITE: nhu2025tawm — differentiate MPC vs imagination paradigm
855	# 2. SHOULD CITE: li2025lsimagine — concurrent Dreamer horizon extension
856	# 3. SHOULD CITE: shaj2023mts3 — multi-rate dynamics foundation
857	# 4. CONSIDER: zhang2026hwm — latest hierarchical WM planning
858	
859	# ============================================================
860	# INCREMENTAL SCAN (2026-05-15): Value expansion horizon & overestimation
861	# ============================================================
862	# 4 new papers from targeted search on:
863	#   - "temporal abstraction" + "world model" + RL (2024-2026)
864	#   - "CIVO" / "value overestimation" + MBRL
865	#   - "imagination horizon" + world model
866	#   - "value function collapse" / "value divergence" + MBRL
867	#   - variable timestep imagination + actor-critic failure
868	#
869	# KEY FINDING: Still NO paper diagnosing dt_embedding → CIVO
870	# → stochastic collapse in imagination-based MBRL.
871	# Core contribution remains novel. Palenicek 2025 is the most
872	# relevant new addition — shows even oracle dynamics don't help
873	# with longer rollout horizons, supporting our thesis that the
874	# bottleneck is NOT model accuracy but value estimation corruption.
875	
876	- paper_id: palenicek2025diminishing
877	  title: "Diminishing Return of Value Expansion Methods"
878	  authors: [Palenicek D., Lutter M., Carvalho J., Dennert D., Ahmad F., Peters J.]
879	  year: 2025
880	  venue: "Reinforcement Learning Journal (RLC 2025, arXiv:2412.20537)"
881	  category: evaluation
882	  role: "Shows longer model-based rollout horizons have diminishing returns in sample efficiency — even with oracle dynamics models, each additional expansion step yields progressively smaller gains. The bottleneck is NOT model accuracy. Directly supports our finding: extending imagination horizon via dt>1 does not improve performance because the problem lies in value estimation (CIVO from dt_embedding), not dynamics quality. Strengthens our argument that dt=1 imagination is sufficient."
883	  relevance_score: 5
884	
885	- paper_id: kim2025deas
886	  title: "DEAS: DEtached value learning with Action Sequence for Scalable Offline RL"
887	  authors: [Kim C., Seo Y., et al.]
888	  year: 2025
889	  venue: "arXiv:2510.07730"
890	  category: method-component
891	  role: "Shows action sequences (temporal extension via options/semi-MDP) cause excessive value overestimation in actor-critic algorithms; proposes detached value learning where critic trains separately from policy. Parallel to our finding: temporal extension (whether via action sequences or dt-embedding) creates value overestimation in actor-critic; DEAS's detached learning is analogous to our dt=1 imagination fix (decoupling temporal abstraction from value estimation)."
892	  relevance_score: 4
893	
894	- paper_id: luo2025vpl
895	  title: "A Case for Validation Buffer in Pessimistic Actor-Critic"
896	  authors: [Luo F., et al.]
897	  year: 2025
898	  venue: "IJCAI 2025 (arXiv:2403.01014)"
899	  category: method-component
900	  role: "Validation Pessimism Learning (VPL) — uses validation buffer to adaptively adjust pessimism levels throughout training; shows pessimism is beneficial only during overestimation, detrimental during underestimation. Relevant to our setting: our trained dt_embedding creates persistent overestimation (nve>1.5x), suggesting adaptive pessimism could be a complementary mitigation to our dt=1 imagination restriction."
901	  relevance_score: 3
902	
903	- paper_id: lenz2025macura
904	  title: "Trust the Model Where It Trusts Itself -- Model-Based Actor-Critic with Uncertainty-Aware Rollout Adaption"
905	  authors: [Lenz S., et al.]
906	  year: 2025
907	  venue: "arXiv:2405.19014"
908	  category: method-component
909	  role: "MACURA — uses model uncertainty to adaptively determine local rollout length in model-based actor-critic; avoids uniform rollout horizon. Addresses rollout quality from the uncertainty perspective; our work identifies a different mechanism: even if the model is confident, dt-embedding-conditioned imagination can produce overestimated value estimates (CIVO). MACURA's uncertainty-based termination would not catch our failure mode because the model predictions may be accurate while value estimates are corrupted."
910	  relevance_score: 3
911	
912	# --- Incremental scan synthesis (2026-05-15) ---
913	#
914	# NOVELTY ASSESSMENT (confirmed):
915	# No paper found that diagnoses dt_embedding → CIVO
916	# (value overestimation) → stochastic collapse in imagination-based
917	# MBRL. Core contribution remains novel after 2nd scan.
918	#
919	# KEY NEW INSIGHT from Palenicek 2025:
920	# Even oracle dynamics models show diminishing returns with longer
921	# rollouts. This means the value estimation bottleneck (not model
922	# accuracy) is increasingly recognized as the fundamental limit
923	# of imagination-based MBRL — our paper explains a specific
924	# mechanism (dt_embedding-induced CIVO) by which
925	# this bottleneck manifests.
926	#
927	# DEAS (Kim 2025) provides independent evidence from offline RL
928	# that temporal extension (action sequences) → value overestimation
929	# in actor-critic. Different setting (offline vs online, action
930	# sequences vs dt-embedding) but same causal pattern.
931	#
932	# NO DIRECT COMPETITORS FOUND at CoRL 2025/2026.
933	#
934	# UPDATED ACTION ITEMS FOR PAPER:
935	# 1. MUST CITE: palenicek2025diminishing — rollout horizon diminishing
936	#    returns support our "dt=1 is sufficient" conclusion
937	# 2. SHOULD CITE: kim2025deas — independent evidence of temporal
938	#    extension → value overestimation in actor-critic
939	# 3. CONSIDER: luo2025vpl — adaptive pessimism as potential mitigation
940	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "5179e666-a679-4cc9-8a39-98660cc3e999",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
      "content": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-15\n# Total: 76 papers (72 existing + 4 incremental scan 2026-05-15)\n\n# ============================================================\n# EXISTING CITATIONS (already in paper.tex)\n# ============================================================\n\n- paper_id: sutton1999options\n  title: \"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\"\n  authors: [Sutton R.S., Precup D., Singh S.]\n  year: 1999\n  venue: \"Artificial Intelligence 112(1-2):181-211\"\n  category: background\n  role: \"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\"\n  relevance_score: 5\n\n- paper_id: hafner2020dreamerv1\n  title: \"Dream to Control: Learning Behaviors by Latent Imagination\"\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\n  year: 2020\n  venue: ICLR\n  category: background\n  role: \"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\"\n  relevance_score: 5\n\n- paper_id: hafner2023dreamerv3\n  title: \"Mastering Diverse Domains through World Models\"\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\n  year: 2023\n  venue: \"arXiv:2301.04104 (Nature 2025)\"\n  category: background\n  role: \"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\"\n  relevance_score: 5\n\n- paper_id: sharma2017figar\n  title: \"Fine Grained Action Repetition for Deep Reinforcement Learning\"\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\n  year: 2017\n  venue: \"ICLR Workshop\"\n  category: method-component\n  role: \"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\"\n  relevance_score: 4\n\n- paper_id: janner2019mbpo\n  title: \"When to Trust Your Model: Model-Based Policy Optimization\"\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\n  year: 2019\n  venue: NeurIPS\n  category: background\n  role: \"MBPO — formalizes model exploitation in MBRL; our conditioning-induced value overestimation (CIVO) is a specific instance of model exploitation tied to temporal embedding\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Multi-step prediction error compounding\n# ============================================================\n\n- paper_id: ke2019learning\n  title: \"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\"\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\n  year: 2019\n  venue: ICLR\n  category: background\n  role: \"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\"\n  relevance_score: 4\n\n- paper_id: asadi2019combating\n  title: \"Combating the Compounding-Error Problem with a Multi-step Model\"\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\n  year: 2019\n  venue: \"arXiv:1905.13320\"\n  category: background\n  role: \"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\"\n  relevance_score: 4\n\n- paper_id: venkatraman2015improving\n  title: \"Improving Multi-Step Prediction of Learned Time Series Models\"\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\n  year: 2015\n  venue: AAAI\n  category: background\n  role: \"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\"\n  relevance_score: 3\n\n- paper_id: lambert2022investigating\n  title: \"Investigating Compounding Prediction Errors in Learned Dynamics Models\"\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\n  year: 2022\n  venue: \"arXiv:2203.09637\"\n  category: background\n  role: \"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Model-predictive control with learned dynamics\n# ============================================================\n\n- paper_id: chua2018pets\n  title: \"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\"\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\"\n  relevance_score: 3\n\n- paper_id: nagabandi2018neural\n  title: \"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\"\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\n  year: 2018\n  venue: ICRA\n  category: background\n  role: \"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\"\n  relevance_score: 3\n\n- paper_id: hansen2024tdmpc2\n  title: \"TD-MPC2: Scalable, Robust World Models for Continuous Control\"\n  authors: [Hansen N., Su H., Wang X.]\n  year: 2024\n  venue: \"ICLR (arXiv:2310.16828)\"\n  category: background\n  role: \"TD-MPC2 — SOTA MPC planning route (online planning + learned dynamics); DMC benchmark leader but orthogonal to imagination-based training — reviewer defense: TD-MPC2 does online MPC rollouts at test time, we study actor-critic training via imagined rollouts (DreamerV3 paradigm), not a same-level comparison\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: Pessimistic MBRL / model exploitation mitigation\n# ============================================================\n\n- paper_id: yu2020mopo\n  title: \"MOPO: Model-based Offline Policy Optimization\"\n  authors: [Yu T., Thomas G., Yu L., Ermon S., Zou J., Levine S., Finn C., Ma T.]\n  year: 2020\n  venue: \"NeurIPS (arXiv:2005.13239)\"\n  category: background\n  role: \"MOPO — pessimistic MBRL via uncertainty-penalized reward (reward -= λ * model_uncertainty); generic model exploitation mitigation — reviewer defense: MOPO addresses distribution shift in offline MBRL, our dt=1 imagination restriction targets dt_embedding-induced CIVO (temporal conditioning corruption), two complementary mechanisms\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: Value overestimation mitigation\n# ============================================================\n\n- paper_id: thrun1993issues\n  title: \"Issues in Using Function Approximation for Reinforcement Learning\"\n  authors: [Thrun S., Schwartz A.]\n  year: 1993\n  venue: \"Connectionist Models Summer School\"\n  category: background\n  role: \"First identification of systematic value overestimation from function approximation; our CIVO extends this to model-based imagination with temporal conditioning\"\n  relevance_score: 4\n\n- paper_id: vanhasselt2016double\n  title: \"Deep Reinforcement Learning with Double Q-Learning\"\n  authors: [van Hasselt H., Guez A., Silver D.]\n  year: 2016\n  venue: AAAI\n  category: background\n  role: \"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\"\n  relevance_score: 4\n\n- paper_id: fujimoto2018td3\n  title: \"Addressing Function Approximation Error in Actor-Critic Methods\"\n  authors: [Fujimoto S., van Hoof H., Meger D.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\"\n  relevance_score: 4\n\n- paper_id: haarnoja2018sac\n  title: \"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\"\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\"\n  relevance_score: 3\n\n- paper_id: lee2021sunrise\n  title: \"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\"\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified CIVO mechanism\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Delusional bias\n# ============================================================\n\n- paper_id: lu2018nondelusional\n  title: \"Non-delusional Q-learning and Value-Iteration\"\n  authors: [Lu T., Schuurmans D., Boutilier C.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Hierarchical RL with learned models\n# ============================================================\n\n- paper_id: hafner2022director\n  title: \"Deep Hierarchical Planning from Pixels\"\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\n  year: 2022\n  venue: NeurIPS\n  category: direct-competitor\n  role: \"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\"\n  relevance_score: 4\n\n- paper_id: nachum2018hiro\n  title: \"Data-Efficient Hierarchical Reinforcement Learning\"\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Action repeat / frame skip\n# ============================================================\n\n- paper_id: braylan2015frame\n  title: \"Frame Skip Is a Powerful Parameter for Learning to Play Atari\"\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\n  year: 2015\n  venue: \"AAAI Workshop on Learning for General Competency in Video Games\"\n  category: background\n  role: \"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\"\n  relevance_score: 3\n\n- paper_id: lakshminarayanan2017dynamic\n  title: \"Dynamic Action Repetition for Deep Reinforcement Learning\"\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\n  year: 2017\n  venue: AAAI\n  category: method-component\n  role: \"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\"\n  relevance_score: 4\n\n- paper_id: biedenkapp2021temporl\n  title: \"TempoRL: Learning When to Act\"\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: DreamerV2\n# ============================================================\n\n- paper_id: hafner2021dreamerv2\n  title: \"Mastering Atari with Discrete World Models\"\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\n  year: 2021\n  venue: ICLR\n  category: background\n  role: \"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Alternative world model architectures\n# ============================================================\n\n- paper_id: micheli2023iris\n  title: \"Transformers are Sample-Efficient World Models\"\n  authors: [Micheli V., Alonso E., Fleuret F.]\n  year: 2023\n  venue: ICLR\n  category: background\n  role: \"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\"\n  relevance_score: 3\n\n- paper_id: robine2023twm\n  title: \"Transformer-based World Models Are Happy With 100k Interactions\"\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\n  year: 2023\n  venue: ICLR\n  category: background\n  role: \"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\"\n  relevance_score: 3\n\n- paper_id: chen2022transdreamer\n  title: \"TransDreamer: Reinforcement Learning with Transformer World Models\"\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\n  year: 2022\n  venue: \"arXiv:2202.09481\"\n  category: background\n  role: \"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\n# ============================================================\n\n- paper_id: gumbsch2024thick\n  title: \"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\"\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\n  year: 2024\n  venue: ICLR\n  category: direct-competitor\n  role: \"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\"\n  relevance_score: 5\n\n- paper_id: mattes2024hieros\n  title: \"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\"\n  authors: [Mattes P., Schlosser R., Herbrich R.]\n  year: 2024\n  venue: ICML\n  category: direct-competitor\n  role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Seed-dependent instability & value overestimation in MBRL\n# ============================================================\n\n- paper_id: henderson2018deep\n  title: \"Deep Reinforcement Learning that Matters\"\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\n  year: 2018\n  venue: AAAI\n  category: background\n  role: \"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\"\n  relevance_score: 4\n\n- paper_id: nikishin2022primacy\n  title: \"The Primacy Bias in Deep Reinforcement Learning\"\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\n  year: 2022\n  venue: ICML\n  category: background\n  role: \"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\"\n  relevance_score: 4\n\n- paper_id: qiao2023mind\n  title: \"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\"\n  authors: [Qiao Z., Lyu J., Li X.]\n  year: 2023\n  venue: \"arXiv:2310.15017 (ECAI 2024)\"\n  category: evaluation\n  role: \"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\"\n  relevance_score: 5\n\n- paper_id: hussing2024dissecting\n  title: \"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\"\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\n  year: 2024\n  venue: \"Reinforcement Learning Journal (RLC 2024)\"\n  category: evaluation\n  role: \"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our CIVO where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\"\n  relevance_score: 4\n\n- paper_id: barkley2024stealing\n  title: \"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\"\n  authors: [Barkley B., Fridovich-Keil D.]\n  year: 2024\n  venue: \"arXiv:2412.14312 (ICML 2025)\"\n  category: evaluation\n  role: \"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\"\n  relevance_score: 3\n\n- paper_id: bjorck2022variance\n  title: \"Is High Variance Unavoidable in RL? A Case Study in Continuous Control\"\n  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]\n  year: 2022\n  venue: ICLR\n  category: background\n  role: \"Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Reward prediction quality → MBRL performance\n# ============================================================\n# Our key finding: removing dt_embedding causes reward_MAE to spike 75x\n# (0.01 → 0.747), making performance seed-dependent. These papers\n# establish that reward prediction quality is a known MBRL bottleneck.\n\n- paper_id: lee2024dreamsmooth\n  title: \"DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing\"\n  authors: [Lee V., Abbeel P., Lee Y.]\n  year: 2024\n  venue: ICLR\n  category: background\n  role: \"Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x\"\n  relevance_score: 5\n\n- paper_id: ma2024harmonydream\n  title: \"HarmonyDream: Task Harmonization Inside World Models\"\n  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]\n  year: 2024\n  venue: ICML\n  category: background\n  role: \"Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion\"\n  relevance_score: 5\n\n- paper_id: lambert2020objective\n  title: \"Objective Mismatch in Model-based Reinforcement Learning\"\n  authors: [Lambert N., Amos B., Yadan O., Calandra R.]\n  year: 2020\n  venue: \"L4DC (Proceedings of Machine Learning Research, vol. 120)\"\n  category: background\n  role: \"Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: Auxiliary tasks & representation coupling in world models\n# ============================================================\n# Our finding: reward prediction quality is tightly coupled to temporal\n# conditioning (dt_embedding). Removing the embedding degrades the\n# reward head while dynamics remain intact — suggesting the reward head\n# acts as more than a passive predictor; it conditions the shared\n# representation. Literature gap: no prior work studies this coupling\n# specifically in Dreamer-family world models.\n\n- paper_id: jaderberg2017unreal\n  title: \"Reinforcement Learning with Unsupervised Auxiliary Tasks\"\n  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]\n  year: 2017\n  venue: ICLR\n  category: background\n  role: \"UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction\"\n  relevance_score: 4\n\n- paper_id: lyle2021auxiliary\n  title: \"On The Effect of Auxiliary Tasks on Representation Dynamics\"\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\n  year: 2021\n  venue: AISTATS\n  category: background\n  role: \"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: DreamerV3 architecture improvements (2025-2026)\n# ============================================================\n\n- paper_id: bredis2026nedreamer\n  title: \"Next Embedding Prediction Makes World Models Stronger\"\n  authors: [Bredis G., Balagansky N., Gavrilov D., Rakhimov R.]\n  year: 2026\n  venue: \"arXiv:2603.02765\"\n  category: background\n  role: \"NE-Dreamer — decoder-free MBRL replacing pixel reconstruction with next-embedding prediction via temporal transformer + Barlow Twins; improves RSSM prediction quality on DMC and DMLab but does not address temporal abstraction or CIVO — orthogonal to our dt-embedding diagnosis\"\n  relevance_score: 3\n\n- paper_id: zhang2025dymodreamer\n  title: \"DyMoDreamer: World Modeling with Dynamic Modulation\"\n  authors: [Zhang B., Wang R., Xiao W., Zhang W., Sun J., Huang G., Chen J., Wang G.]\n  year: 2025\n  venue: NeurIPS\n  category: background\n  role: \"Modulates RSSM via inter-frame differencing mask and stochastic categorical dynamic modulation; SOTA on Atari 100k (156.6% HNS) and DMC (832) — improves dynamics extraction but does not address variable-rate imagination or dt_embedding-induced value overestimation\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Temporal abstraction methods\n# ============================================================\n\n- paper_id: liu2025vanta\n  title: \"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning\"\n  authors: [Liu T.-S., Liu X.-H., Chen R., Jin L., Wang P., Zhang Z., Yu Y.]\n  year: 2025\n  venue: ICLR\n  category: method-component\n  role: \"VanTA — VLM-guided trajectory decomposition into semantically meaningful skills via vector quantization + relabeling; operates at high-level skill abstraction (Franka Kitchen, Crafter) — contrasts with our low-level dt-based temporal abstraction within world-model imagination steps\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Evaluation methodology\n# ============================================================\n\n- paper_id: agarwal2021precipice\n  title: \"Deep Reinforcement Learning at the Edge of the Statistical Precipice\"\n  authors: [Agarwal R., Schwarzer M., Castro P.S., Courville A.C., Bellemare M.]\n  year: 2021\n  venue: NeurIPS\n  category: evaluation\n  role: \"Proposes rliable — interval estimates, performance profiles, IQM for robust multi-seed RL evaluation (NeurIPS Outstanding Paper); our multi-seed experiment design follows this methodology to ensure statistical validity of collapse detection across seeds\"\n  relevance_score: 4\n\n# ============================================================\n# NEW (2026-05-14 gap analysis): Time discretization theory\n# ============================================================\n# Gap: variable timestep / time discretization invariance — foundational\n# theory for why dt matters and how to handle it.\n\n- paper_id: tallec2019making\n  title: \"Making Deep Q-learning methods Robust to Time Discretization\"\n  authors: [Tallec C., Blier L., Ollivier Y.]\n  year: 2019\n  venue: \"ICML (arXiv:1901.09732)\"\n  category: background\n  role: \"Shows Q-learning performance is highly sensitive to time discretization δ; proposes architectural + exploration modifications for δ-invariance. Theoretical foundation for why our variable-dt imagination introduces a fundamental difficulty: RSSM trained at δ=1 cannot produce δ-invariant predictions at dt>1\"\n  relevance_score: 4\n\n- paper_id: park2021sar\n  title: \"Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods\"\n  authors: [Park S., Kim J., Kim G.]\n  year: 2021\n  venue: \"NeurIPS (arXiv:2111.03941)\"\n  category: method-component\n  role: \"SAR — δ-invariant action repetition for policy gradients; achieves time-discretization robustness in model-free RL via adaptive reaction to state changes during repetition. Contrasts with our finding that world-model RL lacks this robustness when imagination uses dt>1\"\n  relevance_score: 4\n\n- paper_id: wang2024seac\n  title: \"Reinforcement Learning with Elastic Time Steps\"\n  authors: [Wang D., Beltrame G.]\n  year: 2024\n  venue: \"arXiv:2402.14961\"\n  category: method-component\n  role: \"SEAC/MOSEAC — variable-duration time steps where agent selects both action and duration; model-free approach that explicitly treats action duration as part of the action space. Our work reveals why this strategy is problematic in world-model RL: the critic cannot reliably evaluate variable-duration imagined trajectories\"\n  relevance_score: 3\n\n# ============================================================\n# NEW (2026-05-14 gap analysis): Delusional bias mitigation\n# ============================================================\n\n- paper_id: su2020conqur\n  title: \"ConQUR: Mitigating Delusional Bias in Deep Q-learning\"\n  authors: [Su D., Ooi J., Lu T., Schuurmans D., Boutilier C.]\n  year: 2020\n  venue: \"ICML (arXiv:2002.12399)\"\n  category: background\n  role: \"Follow-up to Lu et al. 2018; mitigates delusional bias via consistency-penalized Q-labels. Addresses delusional bias from policy-class constraints in Q-learning; our CIVO is an analogous phenomenon in MBRL where temporal conditioning (dt_embedding) creates inconsistent value targets across imagination steps\"\n  relevance_score: 4\n\n# ============================================================\n# NEW (2026-05-14 gap analysis): Diagnostic methodology in RL\n# ============================================================\n# Gap: our paper is a diagnostic analysis — need methodological\n# precedents for \"what matters\" / \"implementation matters\" style papers.\n\n- paper_id: engstrom2020implementation\n  title: \"Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO\"\n  authors: [Engstrom L., Ilyas A., Santurkar S., Tsipras D., Janoos F., Rudolph L., Madry A.]\n  year: 2020\n  venue: \"ICLR (arXiv:2005.12729)\"\n  category: evaluation\n  role: \"Demonstrates that code-level implementation details (not algorithmic innovations) drive most of PPO's gains over TRPO; methodological precedent for our diagnostic approach — we similarly show that a specific implementation choice (trained vs. untrained dt_embedding) is the primary factor determining collapse vs. stability\"\n  relevance_score: 4\n\n- paper_id: andrychowicz2021whatmatters\n  title: \"What Matters for On-Policy Deep Actor-Critic Methods? A Large-Scale Study\"\n  authors: [Andrychowicz M., Raichuk A., Stańczyk P., Orsini M., Girgin S., Marinier R., Hussenot L., Geist M., Pietquin O., Michalski M., Gelly S., Bachem O.]\n  year: 2021\n  venue: \"ICLR (arXiv:2006.05990)\"\n  category: evaluation\n  role: \"Large-scale factorial study of 50+ design choices in on-policy RL (250K+ agents); methodological template for our factorial experiment design isolating dt_embedding × subsample × horizon effects. Demonstrates that systematic ablation reveals non-obvious interactions — parallel to our finding that dt_embedding training status interacts with subsample and horizon\"\n  relevance_score: 4\n\n# ============================================================\n# NEW (2026-05-14 gap analysis): MBRL rollout quality & value overestimation\n# ============================================================\n# Gap: recent ICLR 2025 papers directly studying imagination rollout\n# quality and value overestimation in model-based settings.\n\n- paper_id: frauenknecht2025rollouts\n  title: \"On Rollouts in Model-Based Reinforcement Learning\"\n  authors: [Frauenknecht B., Subhasish D., Solowjow F., Trimpe S.]\n  year: 2025\n  venue: \"ICLR (arXiv:2501.16918)\"\n  category: evaluation\n  role: \"Shows trajectory-sampling rollouts diverge from ground truth after few steps and can harm policy learning; proposes Infoprop separating aleatoric/epistemic uncertainty with rollout termination criteria. Directly supports our finding that dt>1 imagination produces corrupted data — our work identifies a specific mechanism (dt_embedding-induced value exploitation) beyond general compounding error\"\n  relevance_score: 5\n\n- paper_id: voelcker2025madtd\n  title: \"MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL\"\n  authors: [Voelcker C., Hussing M., Eaton E., Farahmand A.-M., Gilitschenski I.]\n  year: 2025\n  venue: \"ICLR (arXiv:2410.08896)\"\n  category: evaluation\n  role: \"Shows value function misgeneralization to on-policy actions causes instability at high UTD ratios; uses model-generated data to improve value accuracy. Complementary to our finding: MAD-TD addresses value misgeneralization from replay distribution mismatch, we address value overestimation from temporal conditioning corruption in imagination\"\n  relevance_score: 4\n\n# ============================================================\n# NEW (2026-05-14 gap analysis): Latest action repeat methods\n# ============================================================\n\n- paper_id: nie2025sdar\n  title: \"Select before Act: Spatially Decoupled Action Repetition for Continuous Control\"\n  authors: [Nie B., et al.]\n  year: 2025\n  venue: \"ICLR (arXiv:2502.06919)\"\n  category: method-component\n  role: \"SDAR — per-dimension action repetition decisions for flexible temporal persistence in model-free RL; SOTA on DMC continuous control. Advances action repeat in model-free setting; our work shows the fundamental obstacle to analogous variable-rate approaches in model-based RL (CIVO from dt_embedding)\"\n  relevance_score: 3\n\n# ============================================================\n# NEW (2026-05-14 gap analysis): DreamerV4 / latest Dreamer evolution\n# ============================================================\n\n- paper_id: hafner2025dreamerv4\n  title: \"Training Agents Inside of Scalable World Models\"\n  authors: [Hafner D., Yan W., Lillicrap T.]\n  year: 2025\n  venue: \"arXiv:2509.24527\"\n  category: background\n  role: \"DreamerV4 — replaces RSSM with efficient transformer world model + shortcut forcing; scales to video pretraining (Minecraft diamonds from video). Architectural successor to DreamerV3; our dt_embedding diagnosis is specific to RSSM but the broader lesson (temporal conditioning must match model fidelity) applies to transformer world models\"\n  relevance_score: 4\n\n# ============================================================\n# NEW (2026-05-14): Training instability dynamics\n# ============================================================\n\n- paper_id: zhang2026instability\n  title: \"Training instability in deep learning follows low-dimensional dynamical principles\"\n  authors: [Zhang L., et al.]\n  year: 2026\n  venue: \"ICLR 2026 (arXiv:2601.13160)\"\n  category: background\n  role: \"Training instability follows low-dimensional dynamical principles; provides theoretical framework for why seed-dependent collapse vs self-correction occurs in our experiments (008d seed 1 collapses, 009b seed 2 self-corrects under identical config)\"\n  relevance_score: 5\n\n# ============================================================\n# NEW (2026-05-14): Seed-Dependent Stochastic Outcomes in MBRL\n# ============================================================\n# Dedicated literature survey for the stochastic collapse phenomenon:\n# same config (trained dt_embedding + subsample + H=8) produces\n# collapse in seed 0 (008d) but self-correction in seed 2 (009b).\n# nve>1.5x is a 100% reliable marker of trained dt_embedding,\n# but collapse itself is stochastic (1/2 seeds).\n\n- paper_id: sokar2023dormant\n  title: \"The Dormant Neuron Phenomenon in Deep Reinforcement Learning\"\n  authors: [Sokar G., Agarwal R., Castro P.S., Evci U.]\n  year: 2023\n  venue: \"ICML 2023\"\n  category: background\n  role: \"Identifies dormant neurons — inactive units accumulating during RL training that reduce network expressivity. Seed-dependent because different random initializations produce different early dormancy patterns; directly explains why some seeds lose the representational capacity needed to self-correct value overestimation (our seed 0 collapses) while others retain enough active neurons to recover (our seed 2 self-corrects)\"\n  relevance_score: 4\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: lyle2022capacity\n  title: \"Understanding and Preventing Capacity Loss in Reinforcement Learning\"\n  authors: [Lyle C., Rowland M., Dabney W.]\n  year: 2022\n  venue: \"ICLR 2023 (arXiv:2204.09560)\"\n  category: background\n  role: \"Shows feature rank collapse from non-stationary TD targets is a necessary condition for learning failure but not sufficient — sparse rewards and other factors must co-occur. Directly parallels our finding: nve>1.5x (value overestimation from trained dt_embedding) is a necessary precondition for collapse but not a sufficient one; additional stochastic factors (initialization, early replay composition) determine whether collapse actually occurs\"\n  relevance_score: 5\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: kumar2022dr3\n  title: \"DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization\"\n  authors: [Kumar A., Agarwal R., Ma T., Courville A., Tucker G., Levine S.]\n  year: 2022\n  venue: \"ICLR 2022\"\n  category: background\n  role: \"Shows implicit regularization from TD learning favors degenerate feature aliasing (states on both sides of Bellman backup become indistinguishable), creating the substrate for value overestimation. In our setting, trained dt_embedding amplifies this aliasing across different temporal horizons — the critic cannot distinguish between dt=1 and dt>1 value targets, enabling exploitation. Feature aliasing is seed-dependent because it depends on initialization geometry\"\n  relevance_score: 4\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: colas2018seeds\n  title: \"How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments\"\n  authors: [Colas C., Sigaud O., Oudeyer P.-Y.]\n  year: 2018\n  venue: \"arXiv:1806.08295\"\n  category: evaluation\n  role: \"Provides statistical framework for determining seed count needed for significant algorithm comparison; our 2-seed observation (1/2 collapse) has limited statistical power by their analysis — but the qualitative difference (nve 4.12x vs 0.38x) is large enough that even 2 seeds establish the stochastic nature of the phenomenon. Methodological basis for future multi-seed validation\"\n  relevance_score: 3\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: nikishin2023plasticity\n  title: \"Deep Reinforcement Learning with Plasticity Injection\"\n  authors: [Nikishin E., Oh J., Ostrovski G., Lyle C., Pascanu R., Dabney W., Barreto A.]\n  year: 2023\n  venue: \"NeurIPS 2023\"\n  category: method-component\n  role: \"Plasticity injection augments network plasticity without changing parameter count; serves as a diagnostic tool — if injection improves performance, plasticity loss was the bottleneck. Directly applicable to diagnosing whether our seed-dependent collapse is plasticity-mediated: if plasticity injection prevents collapse in seed 0 but has no effect on seed 2 (which already self-corrects), it confirms plasticity loss as the bifurcation mechanism\"\n  relevance_score: 4\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: schwarzer2023bbf\n  title: \"Bigger, Better, Faster: Human-level Atari with Human-level Efficiency\"\n  authors: [Schwarzer M., Obando-Ceron J.S., Courville A., Bellemare M., Agarwal R., Castro P.S.]\n  year: 2023\n  venue: \"ICML 2023\"\n  category: method-component\n  role: \"BBF achieves SOTA sample efficiency via periodic network resets + scaling + weight decay; periodic resets prevent primacy bias accumulation across seeds. Suggests our CIVO collapse might be preventable with periodic critic resets — the reset would break the positive feedback loop between overestimated values and actor exploitation before it becomes irreversible\"\n  relevance_score: 3\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: farebrother2024stopregressing\n  title: \"Stop Regressing: Training Value Functions via Classification for Scalable Deep RL\"\n  authors: [Farebrother J., Orbay J., Vuong Q., Taiga A.A., Chebotar Y., Xiao T., Irpan A., Levine S., Castro P.S., Faust A., Kumar A., Agarwal R.]\n  year: 2024\n  venue: \"ICML 2024\"\n  category: method-component\n  role: \"Shows categorical cross-entropy for value training provides implicit regularization against overestimation vs MSE regression. DreamerV3 already uses categorical value prediction (twohot + symlog) — yet our trained dt_embedding still induces collapse in some seeds, demonstrating that categorical value training is insufficient to prevent dt_embedding-induced value exploitation\"\n  relevance_score: 3\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: lyle2024normalization\n  title: \"Normalization and Effective Learning Rates in Reinforcement Learning\"\n  authors: [Lyle C., Zheng Z., Giunchiglia E., Sherstan C., Hashemizadeh M., Schuurmans D., Dabney W.]\n  year: 2024\n  venue: \"NeurIPS 2024\"\n  category: background\n  role: \"Shows normalization layers combat overestimation but cause effective learning rate decay via parameter norm growth. Provides a potential mechanism for seed 2's self-correction: if parameter norms grow faster in certain initializations, effective LR decays faster, naturally damping value overestimation before it cascades into collapse. Seed 0's slower norm growth → sustained high effective LR → overestimation compounds → collapse\"\n  relevance_score: 4\n  survey_tag: seed-dependent-stochastic-outcomes\n\n# --- Survey synthesis: Seed-Dependent Stochastic Outcomes ---\n# Summary (2026-05-14):\n#\n# 1. STOCHASTIC COLLAPSE HAS PRECEDENT:\n#    Plasticity loss (Lyle 2022, Sokar 2023, Nikishin 2023) is inherently\n#    seed-dependent because it depends on initialization → early gradient\n#    dynamics → neuron activity patterns. Different seeds hit different\n#    plasticity trajectories under identical configs.\n#\n# 2. nve>1.5x AS DIAGNOSTIC MARKER (necessary but not sufficient):\n#    Lyle 2022 shows feature rank collapse is necessary but not sufficient\n#    for learning failure. Kumar 2022 shows feature aliasing from TD\n#    learning creates the overestimation substrate. Our nve>1.5x is\n#    analogous: it indicates the dt_embedding has enabled value exploitation\n#    (100% reliable marker), but collapse requires additional conditions\n#    (plasticity loss, insufficient effective LR decay) that are stochastic.\n#\n# 3. SELF-CORRECTION MECHANISM:\n#    Lyle 2024 provides a candidate mechanism: normalization-induced\n#    effective LR decay can naturally damp overestimation in some seeds.\n#    Farebrother 2024 shows categorical value training provides partial\n#    implicit regularization. Together these explain why seed 2 self-corrects:\n#    the combination of DreamerV3's categorical critic + normalization +\n#    favorable initialization produces enough implicit regularization to\n#    overcome the dt_embedding-induced overestimation.\n#\n# 4. THEORETICAL GROUNDING:\n#    Zhang 2026 (already in map) provides the dynamical systems framework.\n#    Bjorck 2022 (already in map) shows early outlier events dominate\n#    variance. Together with the new papers, the framing is:\n#    \"trained dt_embedding creates a necessary condition (nve>1.5x) for\n#    CIVO collapse, but collapse is a stochastic bifurcation\n#    whose outcome depends on seed-dependent plasticity dynamics.\"\n\n# ============================================================\n# INCREMENTAL SCAN (2026-05-14): Δt conditioning & adaptive horizon\n# ============================================================\n# 8 new papers from targeted search on:\n#   - Δt/timestep conditioning in world models\n#   - Variable-rate imagination / adaptive horizon\n#   - Hierarchical planning with latent world models (2025-2026)\n#\n# KEY FINDING: TAWM (Nhu et al. ICML 2025) explicitly conditions\n# world model on Δt — closest methodological overlap. But TAWM\n# uses TD-MPC2 (online MPC) not imagination-based actor-critic,\n# and treats Δt conditioning as beneficial. Our work diagnoses\n# Δt conditioning as pathological in imagination-based training\n# (CIVO). Complementary, not duplicative.\n\n- paper_id: nhu2025tawm\n  title: \"Time-Aware World Model for Adaptive Prediction and Control\"\n  authors: [Nhu A.N., Son S., Lin M.C.]\n  year: 2025\n  venue: \"ICML 2025 (arXiv:2506.08441)\"\n  category: direct-competitor\n  role: \"TAWM — explicitly conditions world model on time-step size Δt and trains over diverse Δt values for multi-rate dynamics learning. Built on TD-MPC2 (online MPC). KEY DISTINCTION from our work: (1) TAWM treats Δt conditioning as beneficial for performance/data-efficiency; we diagnose it as pathological in imagination-based actor-critic training (CIVO). (2) TAWM uses MPC (no imagination rollouts for policy training); our failure mode is specific to imagination-based training where the critic exploits dt-conditioned value estimates. (3) TAWM focuses on observation-rate robustness; we focus on value overestimation from temporal conditioning corruption. TAWM actually strengthens our contribution: it shows Δt conditioning works in MPC settings, making our finding that it fails in imagination-based settings a surprising and important diagnostic.\"\n  relevance_score: 5\n  novelty_threat: \"MEDIUM — methodological overlap (Δt conditioning) but fundamentally different paradigm (MPC vs imagination) and opposite conclusion (beneficial vs pathological). Must cite and differentiate in paper.\"\n\n- paper_id: li2025lsimagine\n  title: \"Open-World Reinforcement Learning over Long Short-Term Imagination\"\n  authors: [Li J., Wang Q., Wang Y., Jin X., Li Y., Zeng W., Yang X.]\n  year: 2025\n  venue: \"ICLR 2025 Oral (arXiv:2410.03618)\"\n  category: direct-competitor\n  role: \"LS-Imagine — extends imagination horizon in Dreamer via goal-conditioned jumpy state transitions and affordance maps. Addresses the 'short-sightedness' of standard Dreamer imagination. KEY DISTINCTION: LS-Imagine adds jumpy transitions to reach long-horizon targets (open-world Minecraft), while our work shows that variable-dt imagination itself introduces CIVO. LS-Imagine's jumpy transitions use goal conditioning (not dt-embedding), potentially avoiding the value overestimation we identify.\"\n  relevance_score: 4\n  novelty_threat: \"LOW — different mechanism (goal-conditioned jumps vs dt-embedding) and different focus (long-horizon exploration vs diagnostic of failure modes). Should cite as concurrent approach to extending imagination horizon.\"\n\n- paper_id: zhang2026hwm\n  title: \"Hierarchical Planning with Latent World Models\"\n  authors: [Zhang W., Terver B., Zholus A., Chitnis S., Sutaria H., Assran M., Balestriero R., Bar A., Bardes A., LeCun Y., Ballas N.]\n  year: 2026\n  venue: \"arXiv:2604.03208\"\n  category: direct-competitor\n  role: \"HWM — learns multi-scale latent world models for hierarchical MPC planning; high-level planner optimizes macro-actions, low-level planner handles primitives. 70% success on real-world non-greedy robotic tasks vs 0% for single-level. Addresses temporal abstraction via hierarchical planning (MPC), not imagination-based actor-critic. Further evidence that temporal abstraction in world models requires hierarchy rather than single-scale variable-dt approaches.\"\n  relevance_score: 4\n  novelty_threat: \"LOW — MPC-based hierarchical planning, not imagination-based training. Supports our thesis that flat dt-embedding approaches are inferior to hierarchical alternatives.\"\n\n- paper_id: kobayashi2025metacontroller\n  title: \"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning\"\n  authors: [Kobayashi S., et al.]\n  year: 2025\n  venue: \"arXiv:2512.20605\"\n  category: method-component\n  role: \"MetaController — discovers temporal abstractions via higher-order non-causal sequence model controlling base autoregressive model's residual stream. Each controller executes behaviorally meaningful action sequences with learned termination conditions. Operates in fundamentally different paradigm (LLM-style autoregressive models, not world-model imagination), but demonstrates that temporal abstraction benefits from hierarchical structure rather than flat dt-conditioning.\"\n  relevance_score: 3\n\n- paper_id: shaj2023mts3\n  title: \"Multi Time Scale World Models\"\n  authors: [Shaj V., Gholam Zadeh S., Demir O., Douat L.R., Neumann G.]\n  year: 2023\n  venue: \"NeurIPS 2023 (arXiv:2310.18534)\"\n  category: method-component\n  role: \"MTS3 — probabilistic multi-time-scale state space model with fast and slow latent dynamics for variable-rate prediction. Provides efficient inference across temporal scales. Foundational multi-rate dynamics architecture; our work shows that even with proper multi-rate modeling, the downstream actor-critic training in imagination can exploit temporal conditioning for value overestimation — a failure mode MTS3 does not address (it focuses on prediction quality, not policy training).\"\n  relevance_score: 4\n\n- paper_id: splates2025\n  title: \"Stable Planning with Temporally Extended Skills\"\n  authors: [SPlaTES authors]\n  year: 2025\n  venue: \"Reinforcement Learning Journal (RLC 2025)\"\n  category: method-component\n  role: \"SPlaTES — hierarchical MPC with temporally extended skills + abstract skill world model. Skill learning via mutual-information objective yields diverse, predictable, task-related behavior. Demonstrates that stable long-horizon planning requires modeling skill outcomes (temporal abstraction via hierarchy), not primitive-action outcomes at variable time steps — consistent with our finding that flat dt-embedding fails.\"\n  relevance_score: 3\n\n- paper_id: beckerehmck2023multitimestep\n  title: \"Multi-timestep models for Model-based Reinforcement Learning\"\n  authors: [Becker-Ehmck P., Peters J., van der Smagt P.]\n  year: 2023\n  venue: \"arXiv:2310.05672\"\n  category: background\n  role: \"Proposes multi-timestep training objective (weighted sum of losses at various future horizons) for one-step dynamics models to improve long-horizon R² score. Addresses compounding error at the model training level; our work shows that even with perfect multi-step prediction, the imagination-based actor-critic can still fail due to value overestimation from dt-conditioning — a downstream failure mode distinct from prediction accuracy.\"\n  relevance_score: 3\n\n- paper_id: liu2022dmve\n  title: \"Dynamic-Horizon Model-Based Value Estimation With Latent Imagination\"\n  authors: [Liu Y., et al.]\n  year: 2022\n  venue: \"IEEE TNNLS (arXiv:2009.09593)\"\n  category: background\n  role: \"DMVE — adaptive rollout horizon selection via horizon reliability detection (comparing value expansion errors between raw and reconstructed observations). Addresses the horizon selection problem in imagination-based value estimation. Complementary to our work: DMVE selects among fixed-dt horizons; we show that even optimal horizon selection cannot fix the CIVO when dt-embedding is trained (the overestimation is in the value function, not the horizon length).\"\n  relevance_score: 3\n\n# --- Incremental scan synthesis (2026-05-14) ---\n#\n# NOVELTY ASSESSMENT:\n# No paper found that diagnoses dt_embedding → CIVO\n# (value overestimation) → stochastic collapse in imagination-based\n# MBRL. Our core contribution remains novel.\n#\n# TAWM (ICML 2025) is the closest methodological overlap but\n# operates in MPC paradigm and reaches opposite conclusion\n# (Δt conditioning is beneficial). This actually STRENGTHENS\n# our novelty: \"Δt conditioning helps in MPC but hurts in\n# imagination-based training\" is a more nuanced and surprising finding.\n#\n# LANDSCAPE TREND:\n# The field is converging on HIERARCHY (THICK, Hieros, Director,\n# HWM, SPlaTES, MetaController) as the solution to temporal\n# abstraction in world models, avoiding flat variable-dt approaches.\n# Our diagnostic paper explains WHY flat dt approaches fail,\n# providing theoretical grounding for this empirical trend.\n#\n# ACTION ITEMS FOR PAPER:\n# 1. MUST CITE: nhu2025tawm — differentiate MPC vs imagination paradigm\n# 2. SHOULD CITE: li2025lsimagine — concurrent Dreamer horizon extension\n# 3. SHOULD CITE: shaj2023mts3 — multi-rate dynamics foundation\n# 4. CONSIDER: zhang2026hwm — latest hierarchical WM planning\n\n# ============================================================\n# INCREMENTAL SCAN (2026-05-15): Value expansion horizon & overestimation\n# ============================================================\n# 4 new papers from targeted search on:\n#   - \"temporal abstraction\" + \"world model\" + RL (2024-2026)\n#   - \"CIVO\" / \"value overestimation\" + MBRL\n#   - \"imagination horizon\" + world model\n#   - \"value function collapse\" / \"value divergence\" + MBRL\n#   - variable timestep imagination + actor-critic failure\n#\n# KEY FINDING: Still NO paper diagnosing dt_embedding → CIVO\n# → stochastic collapse in imagination-based MBRL.\n# Core contribution remains novel. Palenicek 2025 is the most\n# relevant new addition — shows even oracle dynamics don't help\n# with longer rollout horizons, supporting our thesis that the\n# bottleneck is NOT model accuracy but value estimation corruption.\n\n- paper_id: palenicek2025diminishing\n  title: \"Diminishing Return of Value Expansion Methods\"\n  authors: [Palenicek D., Lutter M., Carvalho J., Dennert D., Ahmad F., Peters J.]\n  year: 2025\n  venue: \"Reinforcement Learning Journal (RLC 2025, arXiv:2412.20537)\"\n  category: evaluation\n  role: \"Shows longer model-based rollout horizons have diminishing returns in sample efficiency — even with oracle dynamics models, each additional expansion step yields progressively smaller gains. The bottleneck is NOT model accuracy. Directly supports our finding: extending imagination horizon via dt>1 does not improve performance because the problem lies in value estimation (CIVO from dt_embedding), not dynamics quality. Strengthens our argument that dt=1 imagination is sufficient.\"\n  relevance_score: 5\n\n- paper_id: kim2025deas\n  title: \"DEAS: DEtached value learning with Action Sequence for Scalable Offline RL\"\n  authors: [Kim C., Seo Y., et al.]\n  year: 2025\n  venue: \"arXiv:2510.07730\"\n  category: method-component\n  role: \"Shows action sequences (temporal extension via options/semi-MDP) cause excessive value overestimation in actor-critic algorithms; proposes detached value learning where critic trains separately from policy. Parallel to our finding: temporal extension (whether via action sequences or dt-embedding) creates value overestimation in actor-critic; DEAS's detached learning is analogous to our dt=1 imagination fix (decoupling temporal abstraction from value estimation).\"\n  relevance_score: 4\n\n- paper_id: luo2025vpl\n  title: \"A Case for Validation Buffer in Pessimistic Actor-Critic\"\n  authors: [Luo F., et al.]\n  year: 2025\n  venue: \"IJCAI 2025 (arXiv:2403.01014)\"\n  category: method-component\n  role: \"Validation Pessimism Learning (VPL) — uses validation buffer to adaptively adjust pessimism levels throughout training; shows pessimism is beneficial only during overestimation, detrimental during underestimation. Relevant to our setting: our trained dt_embedding creates persistent overestimation (nve>1.5x), suggesting adaptive pessimism could be a complementary mitigation to our dt=1 imagination restriction.\"\n  relevance_score: 3\n\n- paper_id: lenz2025macura\n  title: \"Trust the Model Where It Trusts Itself -- Model-Based Actor-Critic with Uncertainty-Aware Rollout Adaption\"\n  authors: [Lenz S., et al.]\n  year: 2025\n  venue: \"arXiv:2405.19014\"\n  category: method-component\n  role: \"MACURA — uses model uncertainty to adaptively determine local rollout length in model-based actor-critic; avoids uniform rollout horizon. Addresses rollout quality from the uncertainty perspective; our work identifies a different mechanism: even if the model is confident, dt-embedding-conditioned imagination can produce overestimated value estimates (CIVO). MACURA's uncertainty-based termination would not catch our failure mode because the model predictions may be accurate while value estimates are corrupted.\"\n  relevance_score: 3\n\n# --- Incremental scan synthesis (2026-05-15) ---\n#\n# NOVELTY ASSESSMENT (confirmed):\n# No paper found that diagnoses dt_embedding → CIVO\n# (value overestimation) → stochastic collapse in imagination-based\n# MBRL. Core contribution remains novel after 2nd scan.\n#\n# KEY NEW INSIGHT from Palenicek 2025:\n# Even oracle dynamics models show diminishing returns with longer\n# rollouts. This means the value estimation bottleneck (not model\n# accuracy) is increasingly recognized as the fundamental limit\n# of imagination-based MBRL — our paper explains a specific\n# mechanism (dt_embedding-induced CIVO) by which\n# this bottleneck manifests.\n#\n# DEAS (Kim 2025) provides independent evidence from offline RL\n# that temporal extension (action sequences) → value overestimation\n# in actor-critic. Different setting (offline vs online, action\n# sequences vs dt-embedding) but same causal pattern.\n#\n# NO DIRECT COMPETITORS FOUND at CoRL 2025/2026.\n#\n# UPDATED ACTION ITEMS FOR PAPER:\n# 1. MUST CITE: palenicek2025diminishing — rollout horizon diminishing\n#    returns support our \"dt=1 is sufficient\" conclusion\n# 2. SHOULD CITE: kim2025deas — independent evidence of temporal\n#    extension → value overestimation in actor-critic\n# 3. CONSIDER: luo2025vpl — adaptive pessimism as potential mitigation\n",
      "numLines": 940,
      "startLine": 1,
      "totalLines": 940
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

````text
Found multiple related_work_draft.md files. Let me search for the TAWM text in the most likely candidates and also check the luo2025vpl entry in literature_map.yaml.

From the literature_map.yaml, I can see the luo2025vpl entry at lines 894-901:
```yaml
- paper_id: luo2025vpl
  title: "A Case for Validation Buffer in Pessimistic Actor-Critic"
  authors: [Luo F., et al.]
  year: 2025
  venue: "IJCAI 2025 (arXiv:2403.01014)"
```

Wait, the authors are listed as `[Luo F., et al.]` but they should actually be `[Nauman, Ostaszewski, Cygan]`. I need to correct that. Now let me search through the related_work files to find where "TAWM is built on TD-MPC2" appears.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "4e4a2bfd-c6b4-4b8f-8175-3369dcd99e94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194dMuLptV6v4q2wJvsdd3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19102,
      "cache_read_input_tokens": 23052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19102
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

_source line 11_

Found the literature_map.yaml — `luo2025vpl` authors are `[Luo F., et al.]`, needs correction. Now searching for the TAWM text in related_work files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "915b4c5a-d908-4c80-8c26-c6630e387a94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194dMuLptV6v4q2wJvsdd3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19102,
      "cache_read_input_tokens": 23052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19102
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

_source line 12_

<details open><summary>🔧 Tool call — Grep · `toolu_01XvuxFgTPfitU7tMGQHTc2E`</summary>

```json
{
  "pattern": "TAWM is built on TD-MPC2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "64dbe6c7-d12a-4f4c-b8d0-0d4af4c689e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0194dMuLptV6v4q2wJvsdd3F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19102,
      "cache_read_input_tokens": 23052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19102
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

_source line 13 · 2026-05-15T06:23:06.798Z_

<details><summary>↩ Tool result · `toolu_01XvuxFgTPfitU7tMGQHTc2E`</summary>

```text
Found 19 files
logs/workers/worker_writing_file-fixes-d039_20260515T062243.log
logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb.jsonl
logs/chats/feishu_group_oc_5e879064da2e47dad864c1f891eb37a8_director.jsonl
logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_reviewer.jsonl
logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_paper_agent.jsonl
logs/workers/worker_writing_related-work-revision_20260515T044848.log
logs/chats/worker_audit_related-work-reference-check_20260515T042836.jsonl
logs/workers/worker_audit_related-work-reference-check_20260515T042836.log
artifacts/_project/paper/reference_audit_report.md
logs/workers/worker_writing_related-work-draft_20260515T042021.log
logs/chats/archive/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_reviewer_20260513T213655_142982.jsonl
logs/workers/worker_writing_related_work_revision_20260513T180340.log
logs/workers/worker_writing_related_work_section_20260513T175837.log
logs/chats/worker_research_verify_related_work_20260513T164334.jsonl
logs/workers/worker_research_verify_related_work_20260513T164334.log
logs/workers/worker_research_verify-related-work_20260513T111219.log
artifacts/related_work_draft.md
logs/workers/worker_write_fix-related-work_20260513T090438.log
logs/workers/worker_write_related-work_20260513T085926.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "a7cf9a6c-e5f2-4814-8fcb-2a2c288543ca",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "logs/workers/worker_writing_file-fixes-d039_20260515T062243.log",
      "logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb.jsonl",
      "logs/chats/feishu_group_oc_5e879064da2e47dad864c1f891eb37a8_director.jsonl",
      "logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_reviewer.jsonl",
      "logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_paper_agent.jsonl",
      "logs/workers/worker_writing_related-work-revision_20260515T044848.log",
      "logs/chats/worker_audit_related-work-reference-check_20260515T042836.jsonl",
      "logs/workers/worker_audit_related-work-reference-check_20260515T042836.log",
      "artifacts/_project/paper/reference_audit_report.md",
      "logs/workers/worker_writing_related-work-draft_20260515T042021.log",
      "logs/chats/archive/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_reviewer_20260513T213655_142982.jsonl",
      "logs/workers/worker_writing_related_work_revision_20260513T180340.log",
      "logs/workers/worker_writing_related_work_section_20260513T175837.log",
      "logs/chats/worker_research_verify_related_work_20260513T164334.jsonl",
      "logs/workers/worker_research_verify_related_work_20260513T164334.log",
      "logs/workers/worker_research_verify-related-work_20260513T111219.log",
      "artifacts/related_work_draft.md",
      "logs/workers/worker_write_fix-related-work_20260513T090438.log",
      "logs/workers/worker_write_related-work_20260513T085926.log"
    ],
    "numFiles": 19
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Grep · `toolu_01HjpVtk3S6SK4QGbcHPQcqk`</summary>

```json
{
  "pattern": "TAWM is built on TD-MPC2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_draft.md",
  "output_mode": "content",
  "-n": true,
  "-C": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "9d5774e5-30eb-4854-bc5a-efae7649ec22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8cYK5jwF8jbgF8QFdzZDC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 42154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 937
      },
      "output_tokens": 66,
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

_source line 15 · 2026-05-15T06:23:10.442Z_

<details><summary>↩ Tool result · `toolu_01HjpVtk3S6SK4QGbcHPQcqk`</summary>

```text
18-
19:[Omitted long matching line]
20-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "09db1fe2-dd5a-40a7-af5a-e8a1f96c4eac",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "18-\n19:[Omitted long matching line]\n20-",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Grep · `toolu_01XN7yhTSKrorU4wNovHJRUK`</summary>

```json
{
  "pattern": "TAWM is built on TD-MPC2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_draft.md",
  "output_mode": "content",
  "-n": true,
  "-C": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "84e7f80d-d1fd-4309-9378-e19890c81ec2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8cYK5jwF8jbgF8QFdzZDC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 937,
      "cache_read_input_tokens": 42154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 937
      },
      "output_tokens": 66,
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

_source line 17 · 2026-05-15T06:23:11.701Z_

<details><summary>↩ Tool result · `toolu_01XN7yhTSKrorU4wNovHJRUK`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "cd9d7435-ef64-4569-8189-937d311ed5e8",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01TCxZaiYXvSDWFjRCTx6Tkg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_draft.md",
  "offset": 17,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "d3eba3b0-677d-4cf6-9875-d68fbd790266",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3AqCQtMqtNcXAbSk74ept",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 414,
      "cache_read_input_tokens": 43091,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 414
      },
      "output_tokens": 69,
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

_source line 19 · 2026-05-15T06:23:14.339Z_

<details><summary>↩ Tool result · `toolu_01TCxZaiYXvSDWFjRCTx6Tkg`</summary>

```text
17	Several works introduce temporal flexibility into world model dynamics, either through externally specified time gaps or learned hierarchical abstractions.
18	
19	TAWM \citep{freed2024tawm} introduces time-aware world models that condition latent dynamics on a temporal gap $\Delta t$ via RK4/Euler integration, enabling the model to predict across variable time scales. However, $\Delta t$ must be externally specified rather than learned, and TAWM is built on TD-MPC2's short-horizon MPC framework ($H{=}3$--$5$ with MPPI planning), where temporal skipping during planning is counterproductive. Our method adapts the variable-$\Delta t$ conditioning principle to DreamerV3's RSSM but makes $\Delta t$ \emph{state-dependent} via a learned event gate. THICK \citep{romac2024thick} learns a two-level temporal hierarchy via discrete latent dynamics, where the lower level forms invariant contexts and the upper level predicts context changes. While this achieves temporal abstraction, the fixed two-level structure cannot express continuous degrees of event significance or variable skip lengths within a single hierarchy level. HWM \citep{zhang2026hwm} extends this line by learning multi-scale latent world models for hierarchical planning with a learned action encoder for temporal compression, but similarly relies on a fixed two-level planner architecture. ASI \citep{neitz2018adaptive} learns to skip timesteps in recurrent dynamics models by min-pooling over reconstruction losses, selecting intervals that are easiest to predict. It operates on raw observation prediction without integration into a model-based RL loop and optimizes for prediction ease rather than dynamical significance.
20	
21	Our approach avoids the multi-model exploitation problem identified by \citet{schiewer2024hierarchical} in hierarchical world models by operating within a single RSSM, while offering finer temporal adaptation than two-level hierarchies through a continuous per-step stride selection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "05eda193-711f-482e-9188-c6b889ad4bbe",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_draft.md",
      "content": "Several works introduce temporal flexibility into world model dynamics, either through externally specified time gaps or learned hierarchical abstractions.\n\nTAWM \\citep{freed2024tawm} introduces time-aware world models that condition latent dynamics on a temporal gap $\\Delta t$ via RK4/Euler integration, enabling the model to predict across variable time scales. However, $\\Delta t$ must be externally specified rather than learned, and TAWM is built on TD-MPC2's short-horizon MPC framework ($H{=}3$--$5$ with MPPI planning), where temporal skipping during planning is counterproductive. Our method adapts the variable-$\\Delta t$ conditioning principle to DreamerV3's RSSM but makes $\\Delta t$ \\emph{state-dependent} via a learned event gate. THICK \\citep{romac2024thick} learns a two-level temporal hierarchy via discrete latent dynamics, where the lower level forms invariant contexts and the upper level predicts context changes. While this achieves temporal abstraction, the fixed two-level structure cannot express continuous degrees of event significance or variable skip lengths within a single hierarchy level. HWM \\citep{zhang2026hwm} extends this line by learning multi-scale latent world models for hierarchical planning with a learned action encoder for temporal compression, but similarly relies on a fixed two-level planner architecture. ASI \\citep{neitz2018adaptive} learns to skip timesteps in recurrent dynamics models by min-pooling over reconstruction losses, selecting intervals that are easiest to predict. It operates on raw observation prediction without integration into a model-based RL loop and optimizes for prediction ease rather than dynamical significance.\n\nOur approach avoids the multi-model exploitation problem identified by \\citet{schiewer2024hierarchical} in hierarchical world models by operating within a single RSSM, while offering finer temporal adaptation than two-level hierarchies through a continuous per-step stride selection.",
      "numLines": 5,
      "startLine": 17,
      "totalLines": 42
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

Found the text at line 19. Now applying both fixes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "88aaf608-902d-4086-8269-4b76cbce7a9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qpmQwoaaHFUbk1pJypVFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 591,
      "cache_read_input_tokens": 43505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 591
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01VmMTqPs1StJNwJZsvTR9nz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_draft.md",
  "old_string": "TAWM is built on TD-MPC2",
  "new_string": "TAWM is evaluated on TD-MPC2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "94c8da2a-4421-4f06-be59-c04b5946b444",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qpmQwoaaHFUbk1pJypVFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 591,
      "cache_read_input_tokens": 43505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 591
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

_source line 22 · 2026-05-15T06:23:18.263Z_

<details><summary>↩ Tool result · `toolu_01VmMTqPs1StJNwJZsvTR9nz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "73305711-284c-4af3-86e2-f5bbc7654f41",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_draft.md",
    "oldString": "TAWM is built on TD-MPC2",
    "newString": "TAWM is evaluated on TD-MPC2",
    "originalFile": "# 2. Related Work\n\nWe situate our approach within five related lines of research: fixed-rate model-based RL, variable-rate and temporal abstraction, learned skipping for planning, imagination quality improvement, and event-aware world models.\n\n## 2.1 Model-Based RL with Fixed-Rate Imagination\n\nModern model-based RL agents learn latent world models and optimize policies through imagined rollouts at a fixed temporal resolution.\n\nDreamerV3 \\citep{hafner2023dreamerv3} learns a Recurrent State-Space Model (RSSM) that maintains deterministic and stochastic latent states, training an actor-critic purely through $H$-step imagined trajectories. It achieves strong performance across diverse domains but operates at a fixed one-environment-step-per-latent-step resolution, limiting the effective planning horizon to $H$ environment steps regardless of episode length. NE-Dreamer \\citep{nedreamer2026} replaces pixel-level reconstruction with next-embedding prediction, yielding a decoder-free latent world model that improves sample efficiency while retaining the fixed-rate imagination structure. R2-Dreamer \\citep{r2dreamer2026} similarly eliminates the observation decoder by training with redundancy-reduced latent targets, accelerating training and improving robustness.\n\nThese methods share a fundamental limitation: each imagination step covers exactly one environment timestep, so for long-horizon tasks (e.g., 250-step manipulation episodes), a rollout of $H{=}15$ steps covers only 6\\% of the episode, creating a credit assignment bottleneck. Our method addresses this by learning to skip uneventful timesteps, extending the effective horizon to $\\sum \\Delta t_i$ environment steps (up to $H \\times K$) without additional latent computation.\n\n## 2.2 Variable-Rate and Temporal Abstraction\n\nTemporal abstraction has deep roots in RL: the options framework \\citep{sutton1999options} formalizes temporally extended actions with initiation sets and termination conditions; FiGAR \\citep{sharma2017figar} augments the policy with a learned action-repetition head; TempoRL \\citep{biedenkapp2021temporl} learns skip lengths via a dedicated skip network. These approaches operate at the level of \\emph{environment interaction}---choosing how long to commit to an action---whereas our stride selection operates in \\emph{imagination space} and does not alter the agent's environment interaction frequency.\n\nSeveral works introduce temporal flexibility into world model dynamics, either through externally specified time gaps or learned hierarchical abstractions.\n\nTAWM \\citep{freed2024tawm} introduces time-aware world models that condition latent dynamics on a temporal gap $\\Delta t$ via RK4/Euler integration, enabling the model to predict across variable time scales. However, $\\Delta t$ must be externally specified rather than learned, and TAWM is built on TD-MPC2's short-horizon MPC framework ($H{=}3$--$5$ with MPPI planning), where temporal skipping during planning is counterproductive. Our method adapts the variable-$\\Delta t$ conditioning principle to DreamerV3's RSSM but makes $\\Delta t$ \\emph{state-dependent} via a learned event gate. THICK \\citep{romac2024thick} learns a two-level temporal hierarchy via discrete latent dynamics, where the lower level forms invariant contexts and the upper level predicts context changes. While this achieves temporal abstraction, the fixed two-level structure cannot express continuous degrees of event significance or variable skip lengths within a single hierarchy level. HWM \\citep{zhang2026hwm} extends this line by learning multi-scale latent world models for hierarchical planning with a learned action encoder for temporal compression, but similarly relies on a fixed two-level planner architecture. ASI \\citep{neitz2018adaptive} learns to skip timesteps in recurrent dynamics models by min-pooling over reconstruction losses, selecting intervals that are easiest to predict. It operates on raw observation prediction without integration into a model-based RL loop and optimizes for prediction ease rather than dynamical significance.\n\nOur approach avoids the multi-model exploitation problem identified by \\citet{schiewer2024hierarchical} in hierarchical world models by operating within a single RSSM, while offering finer temporal adaptation than two-level hierarchies through a continuous per-step stride selection.\n\n## 2.3 Learned Skipping for Planning\n\nA separate line of work learns explicit skip or jump decisions to extend planning horizons.\n\nLS-Imagine \\citep{li2025lsimagine} learns jumping flags based on affordance-map kurtosis for open-world exploration in MineDojo, enabling the agent to skip over low-information states during imagination via goal-conditioned jumpy state transitions. Our gate differs in two key ways: it operates within the actor-critic MBRL imagination loop with policy-dependent variable-rate stepping rather than goal-conditioned exploration jumps, and it selects strides based on latent-state dynamics rather than observation-space affordance maps. I-TAP \\citep{itap2026} learns temporal abstractions via discrete residual tokens with an RQ-VAE, performing MCTS planning in token space for offline RL. It operates in a fundamentally different paradigm---offline and autoregressive---from our online RSSM-based approach.\n\nWhile both LS-Imagine and I-TAP demonstrate the value of temporal flexibility in planning, neither addresses the specific setting of online actor-critic training with variable-rate latent imagination. Our event gate fills this gap by integrating state-dependent stride selection directly into DreamerV3's imagination pipeline.\n\n## 2.4 Imagination Quality Improvement\n\nRather than changing temporal resolution, several recent works improve the quality of fixed-rate imagination rollouts.\n\nDMWM \\citep{wang2025dmwm} introduces a dual-mind architecture combining an RSSM-based System~1 for intuitive transitions with a logic-informed neural network (LINN) System~2 that provides logical reasoning feedback, improving long-horizon imagination coherence through logical constraints. It shares our motivation of extending effective RSSM imagination but addresses error accumulation at fixed temporal resolution rather than extending the temporal horizon. DyMoDreamer \\citep{dymodreamer2025} extracts motion cues via inter-frame differencing masks at the observation level and integrates stochastic categorical dynamic modulation into the RSSM latent space, focusing on motion-relevant features and achieving strong results on visual benchmarks (Atari 100k, DMC). Whereas DyMoDreamer improves per-step representation quality by bridging observation-level motion cues with latent-space dynamics modeling, our method changes the \\emph{temporal resolution} of imagination---the two approaches target complementary axes of improvement and could in principle be combined. ELVIS \\citep{du2026elvis} introduces ensemble-calibrated uncertainty-aware $\\lambda$-return gating for long-horizon RSSM-based MPC, adaptively weighting bootstrapping versus continued rollout based on epistemic uncertainty. While ELVIS adapts \\emph{how much} to trust each imagination step, it does not change \\emph{how many} environment steps each imagination step covers---our gate modifies the temporal resolution itself.\n\n## 2.5 Event-Aware World Models\n\nEvent-driven representations have recently been applied to world models, though primarily at the observation level.\n\nEA-WM \\citep{eawm2026} introduces event-aware fusion via frame-difference supervision for video world models at the pixel level, using event signals to improve generation quality of dynamic regions. While both EA-WM and our method leverage event-like signals (frame differences vs. latent-state deltas), EA-WM applies them to improve pixel-level video prediction quality, whereas we use latent-state change magnitude to drive \\emph{temporal stride selection} in the imagination loop for policy optimization. Our event gate operates entirely in the learned latent space, using state-delta magnitude as a proxy for dynamical significance to determine when fine-grained versus coarse-grained imagination is warranted.\n",
    "structuredPatch": [
      {
        "oldStart": 16,
        "oldLines": 7,
        "newStart": 16,
        "newLines": 7,
        "lines": [
          " ",
          " Several works introduce temporal flexibility into world model dynamics, either through externally specified time gaps or learned hierarchical abstractions.",
          " ",
          "-TAWM \\citep{freed2024tawm} introduces time-aware world models that condition latent dynamics on a temporal gap $\\Delta t$ via RK4/Euler integration, enabling the model to predict across variable time scales. However, $\\Delta t$ must be externally specified rather than learned, and TAWM is built on TD-MPC2's short-horizon MPC framework ($H{=}3$--$5$ with MPPI planning), where temporal skipping during planning is counterproductive. Our method adapts the variable-$\\Delta t$ conditioning principle to DreamerV3's RSSM but makes $\\Delta t$ \\emph{state-dependent} via a learned event gate. THICK \\citep{romac2024thick} learns a two-level temporal hierarchy via discrete latent dynamics, where the lower level forms invariant contexts and the upper level predicts context changes. While this achieves temporal abstraction, the fixed two-level structure cannot express continuous degrees of event significance or variable skip lengths within a single hierarchy level. HWM \\citep{zhang2026hwm} extends this line by learning multi-scale latent world models for hierarchical planning with a learned action encoder for temporal compression, but similarly relies on a fixed two-level planner architecture. ASI \\citep{neitz2018adaptive} learns to skip timesteps in recurrent dynamics models by min-pooling over reconstruction losses, selecting intervals that are easiest to predict. It operates on raw observation prediction without integration into a model-based RL loop and optimizes for prediction ease rather than dynamical significance.",
          "+TAWM \\citep{freed2024tawm} introduces time-aware world models that condition latent dynamics on a temporal gap $\\Delta t$ via RK4/Euler integration, enabling the model to predict across variable time scales. However, $\\Delta t$ must be externally specified rather than learned, and TAWM is evaluated on TD-MPC2's short-horizon MPC framework ($H{=}3$--$5$ with MPPI planning), where temporal skipping during planning is counterproductive. Our method adapts the variable-$\\Delta t$ conditioning principle to DreamerV3's RSSM but makes $\\Delta t$ \\emph{state-dependent} via a learned event gate. THICK \\citep{romac2024thick} learns a two-level temporal hierarchy via discrete latent dynamics, where the lower level forms invariant contexts and the upper level predicts context changes. While this achieves temporal abstraction, the fixed two-level structure cannot express continuous degrees of event significance or variable skip lengths within a single hierarchy level. HWM \\citep{zhang2026hwm} extends this line by learning multi-scale latent world models for hierarchical planning with a learned action encoder for temporal compression, but similarly relies on a fixed two-level planner architecture. ASI \\citep{neitz2018adaptive} learns to skip timesteps in recurrent dynamics models by min-pooling over reconstruction losses, selecting intervals that are easiest to predict. It operates on raw observation prediction without integration into a model-based RL loop and optimizes for prediction ease rather than dynamical significance.",
          " ",
          " Our approach avoids the multi-model exploitation problem identified by \\citet{schiewer2024hierarchical} in hierarchical world models by operating within a single RSSM, while offering finer temporal adaptation than two-level hierarchies through a continuous per-step stride selection.",
          " "
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

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01DtCuQ8cWnpAk9w7WMCQxDq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
  "old_string": "  authors: [Luo F., et al.]\n  year: 2025\n  venue: \"IJCAI 2025 (arXiv:2403.01014)\"",
  "new_string": "  authors: [Nauman M., Ostaszewski M., Cygan M.]\n  year: 2025\n  venue: \"IJCAI 2025 (arXiv:2403.01014)\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "642d641a-5fc3-441e-a4bc-83d25ddab03b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qpmQwoaaHFUbk1pJypVFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 591,
      "cache_read_input_tokens": 43505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 591
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

_source line 24 · 2026-05-15T06:23:19.459Z_

<details><summary>↩ Tool result · `toolu_01DtCuQ8cWnpAk9w7WMCQxDq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "19ddc559-a898-4ced-afb9-90659a61fcec",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/literature_map.yaml",
    "oldString": "  authors: [Luo F., et al.]\n  year: 2025\n  venue: \"IJCAI 2025 (arXiv:2403.01014)\"",
    "newString": "  authors: [Nauman M., Ostaszewski M., Cygan M.]\n  year: 2025\n  venue: \"IJCAI 2025 (arXiv:2403.01014)\"",
    "originalFile": "# Literature Map — event-gated-adaptive-horizon\n# Last updated: 2026-05-15\n# Total: 76 papers (72 existing + 4 incremental scan 2026-05-15)\n\n# ============================================================\n# EXISTING CITATIONS (already in paper.tex)\n# ============================================================\n\n- paper_id: sutton1999options\n  title: \"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\"\n  authors: [Sutton R.S., Precup D., Singh S.]\n  year: 1999\n  venue: \"Artificial Intelligence 112(1-2):181-211\"\n  category: background\n  role: \"Foundational options framework for temporal abstraction in RL; our work investigates why temporal abstraction fails in world-model RL\"\n  relevance_score: 5\n\n- paper_id: hafner2020dreamerv1\n  title: \"Dream to Control: Learning Behaviors by Latent Imagination\"\n  authors: [Hafner D., Lillicrap T., Ba J., Norouzi M.]\n  year: 2020\n  venue: ICLR\n  category: background\n  role: \"DreamerV1 — base architecture family; our experiments build on the RSSM and imagination-based training paradigm\"\n  relevance_score: 5\n\n- paper_id: hafner2023dreamerv3\n  title: \"Mastering Diverse Domains through World Models\"\n  authors: [Hafner D., Pasukonis J., Ba J., Lillicrap T.]\n  year: 2023\n  venue: \"arXiv:2301.04104 (Nature 2025)\"\n  category: background\n  role: \"DreamerV3 — the specific base system we modify; symlog transforms, discrete latents, all default hyperparameters come from here\"\n  relevance_score: 5\n\n- paper_id: sharma2017figar\n  title: \"Fine Grained Action Repetition for Deep Reinforcement Learning\"\n  authors: [Sharma S., Lakshminarayanan A.S., Ravindran B.]\n  year: 2017\n  venue: \"ICLR Workshop\"\n  category: method-component\n  role: \"FiGAR — learns action-repeat durations in model-free RL; we extend the idea to imagination step size in world-model RL\"\n  relevance_score: 4\n\n- paper_id: janner2019mbpo\n  title: \"When to Trust Your Model: Model-Based Policy Optimization\"\n  authors: [Janner M., Fu J., Zhang M., Levine S.]\n  year: 2019\n  venue: NeurIPS\n  category: background\n  role: \"MBPO — formalizes model exploitation in MBRL; our conditioning-induced value overestimation (CIVO) is a specific instance of model exploitation tied to temporal embedding\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Multi-step prediction error compounding\n# ============================================================\n\n- paper_id: ke2019learning\n  title: \"Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future\"\n  authors: [Ke N.R., Singh A., Touati A., Goyal A., Bengio Y., Parikh D., Batra D.]\n  year: 2019\n  venue: ICLR\n  category: background\n  role: \"Addresses long-term dynamics prediction via latent-variable autoregressive model; directly relevant to our finding that multi-step RSSM predictions degrade with dt>1\"\n  relevance_score: 4\n\n- paper_id: asadi2019combating\n  title: \"Combating the Compounding-Error Problem with a Multi-step Model\"\n  authors: [Asadi K., Misra D., Kim S., Littman M.L.]\n  year: 2019\n  venue: \"arXiv:1905.13320\"\n  category: background\n  role: \"Proposes multi-step models to bypass compounding error; our work shows that even with multi-step imagination, the dt-embedding creates a different failure mode (value overestimation) distinct from compounding error\"\n  relevance_score: 4\n\n- paper_id: venkatraman2015improving\n  title: \"Improving Multi-Step Prediction of Learned Time Series Models\"\n  authors: [Venkatraman A., Hebert M., Bagnell J.A.]\n  year: 2015\n  venue: AAAI\n  category: background\n  role: \"Data-as-Demonstrator (DaD) for robust multi-step prediction; establishes theoretical guarantee relating training error to multi-step prediction error\"\n  relevance_score: 3\n\n- paper_id: lambert2022investigating\n  title: \"Investigating Compounding Prediction Errors in Learned Dynamics Models\"\n  authors: [Lambert N., Pister K.S.J., Calandra R.]\n  year: 2022\n  venue: \"arXiv:2203.09637\"\n  category: background\n  role: \"Empirical study of compounding error properties; we rule out compounding error as the primary failure mechanism (008c vs 008a comparison) and identify value overestimation instead\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Model-predictive control with learned dynamics\n# ============================================================\n\n- paper_id: chua2018pets\n  title: \"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\"\n  authors: [Chua K., Calandra R., McAllister R., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"PETS — ensemble-based uncertainty-aware MPC; uses explicit uncertainty quantification to avoid model exploitation, contrasting with DreamerV3's implicit approach\"\n  relevance_score: 3\n\n- paper_id: nagabandi2018neural\n  title: \"Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning\"\n  authors: [Nagabandi A., Kahn G., Fearing R.S., Levine S.]\n  year: 2018\n  venue: ICRA\n  category: background\n  role: \"Demonstrates NN dynamics + MPC for locomotion; model errors accumulate over prediction horizon, motivating our investigation of horizon-dependent failures\"\n  relevance_score: 3\n\n- paper_id: hansen2024tdmpc2\n  title: \"TD-MPC2: Scalable, Robust World Models for Continuous Control\"\n  authors: [Hansen N., Su H., Wang X.]\n  year: 2024\n  venue: \"ICLR (arXiv:2310.16828)\"\n  category: background\n  role: \"TD-MPC2 — SOTA MPC planning route (online planning + learned dynamics); DMC benchmark leader but orthogonal to imagination-based training — reviewer defense: TD-MPC2 does online MPC rollouts at test time, we study actor-critic training via imagined rollouts (DreamerV3 paradigm), not a same-level comparison\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: Pessimistic MBRL / model exploitation mitigation\n# ============================================================\n\n- paper_id: yu2020mopo\n  title: \"MOPO: Model-based Offline Policy Optimization\"\n  authors: [Yu T., Thomas G., Yu L., Ermon S., Zou J., Levine S., Finn C., Ma T.]\n  year: 2020\n  venue: \"NeurIPS (arXiv:2005.13239)\"\n  category: background\n  role: \"MOPO — pessimistic MBRL via uncertainty-penalized reward (reward -= λ * model_uncertainty); generic model exploitation mitigation — reviewer defense: MOPO addresses distribution shift in offline MBRL, our dt=1 imagination restriction targets dt_embedding-induced CIVO (temporal conditioning corruption), two complementary mechanisms\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: Value overestimation mitigation\n# ============================================================\n\n- paper_id: thrun1993issues\n  title: \"Issues in Using Function Approximation for Reinforcement Learning\"\n  authors: [Thrun S., Schwartz A.]\n  year: 1993\n  venue: \"Connectionist Models Summer School\"\n  category: background\n  role: \"First identification of systematic value overestimation from function approximation; our CIVO extends this to model-based imagination with temporal conditioning\"\n  relevance_score: 4\n\n- paper_id: vanhasselt2016double\n  title: \"Deep Reinforcement Learning with Double Q-Learning\"\n  authors: [van Hasselt H., Guez A., Silver D.]\n  year: 2016\n  venue: AAAI\n  category: background\n  role: \"Double DQN — mitigates overestimation via double estimator; our finding that trained dt-embedding enables value exploitation is a complementary overestimation mechanism in MBRL\"\n  relevance_score: 4\n\n- paper_id: fujimoto2018td3\n  title: \"Addressing Function Approximation Error in Actor-Critic Methods\"\n  authors: [Fujimoto S., van Hoof H., Meger D.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"TD3 — clipped double-Q to limit overestimation in actor-critic; DreamerV3 uses a single critic, making it more vulnerable to the overestimation we identify\"\n  relevance_score: 4\n\n- paper_id: haarnoja2018sac\n  title: \"Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor\"\n  authors: [Haarnoja T., Zhou A., Abbeel P., Levine S.]\n  year: 2018\n  venue: ICML\n  category: method-component\n  role: \"SAC — entropy regularization implicitly mitigates overestimation; relevant contrast to DreamerV3's actor which can greedily exploit overestimated values\"\n  relevance_score: 3\n\n- paper_id: lee2021sunrise\n  title: \"SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning\"\n  authors: [Lee K., Laskin M., Srinivas A., Abbeel P.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Ensemble-based uncertainty weighting for value estimation; potential mitigation for our identified CIVO mechanism\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Delusional bias\n# ============================================================\n\n- paper_id: lu2018nondelusional\n  title: \"Non-delusional Q-learning and Value-Iteration\"\n  authors: [Lu T., Schuurmans D., Boutilier C.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"Formalizes delusional bias from policy-class constraints in Q-learning; we identify an analogous phenomenon where temporal conditioning enables the critic to exploit model imprecision\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Hierarchical RL with learned models\n# ============================================================\n\n- paper_id: hafner2022director\n  title: \"Deep Hierarchical Planning from Pixels\"\n  authors: [Hafner D., Lee K.-H., Fischer I., Abbeel P.]\n  year: 2022\n  venue: NeurIPS\n  category: direct-competitor\n  role: \"Director — hierarchical planning in Dreamer latent space via subgoals; addresses temporal abstraction through goal hierarchy rather than variable dt\"\n  relevance_score: 4\n\n- paper_id: nachum2018hiro\n  title: \"Data-Efficient Hierarchical Reinforcement Learning\"\n  authors: [Nachum O., Gu S., Lee H., Levine S.]\n  year: 2018\n  venue: NeurIPS\n  category: background\n  role: \"HIRO — off-policy HRL with learned subgoals; demonstrates that hierarchical temporal abstraction can improve sample efficiency when properly designed\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Action repeat / frame skip\n# ============================================================\n\n- paper_id: braylan2015frame\n  title: \"Frame Skip Is a Powerful Parameter for Learning to Play Atari\"\n  authors: [Braylan A., Hollenbeck M., Meyerson E., Miikkulainen R.]\n  year: 2015\n  venue: \"AAAI Workshop on Learning for General Competency in Video Games\"\n  category: background\n  role: \"Empirical study showing frame skip strongly affects Atari performance; motivates investigation of temporal granularity as a critical design choice\"\n  relevance_score: 3\n\n- paper_id: lakshminarayanan2017dynamic\n  title: \"Dynamic Action Repetition for Deep Reinforcement Learning\"\n  authors: [Lakshminarayanan A.S., Sharma S., Ravindran B.]\n  year: 2017\n  venue: AAAI\n  category: method-component\n  role: \"Learns per-step action repetition duration; model-free analog of our variable-dt imagination approach\"\n  relevance_score: 4\n\n- paper_id: biedenkapp2021temporl\n  title: \"TempoRL: Learning When to Act\"\n  authors: [Biedenkapp A., Rajan R., Hutter F., Lindauer M.]\n  year: 2021\n  venue: ICML\n  category: method-component\n  role: \"Learns action persistence via skip-policy; demonstrates up to 10x speedup — but in model-free setting without the model exploitation risk we identify\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: DreamerV2\n# ============================================================\n\n- paper_id: hafner2021dreamerv2\n  title: \"Mastering Atari with Discrete World Models\"\n  authors: [Hafner D., Lillicrap T., Norouzi M., Ba J.]\n  year: 2021\n  venue: ICLR\n  category: background\n  role: \"DreamerV2 — introduces discrete latent representations used in DreamerV3; key architectural predecessor to our base system\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Alternative world model architectures\n# ============================================================\n\n- paper_id: micheli2023iris\n  title: \"Transformers are Sample-Efficient World Models\"\n  authors: [Micheli V., Alonso E., Fleuret F.]\n  year: 2023\n  venue: ICLR\n  category: background\n  role: \"IRIS — autoregressive transformer world model; alternative to RSSM that may exhibit different compounding error characteristics under temporal abstraction\"\n  relevance_score: 3\n\n- paper_id: robine2023twm\n  title: \"Transformer-based World Models Are Happy With 100k Interactions\"\n  authors: [Robine J., Hoeftmann M., Uelwer T., Harmeling S.]\n  year: 2023\n  venue: ICLR\n  category: background\n  role: \"TWM — Transformer-XL world model with direct state access; circumvents RSSM's recurrent compression that exacerbates our identified prediction gap\"\n  relevance_score: 3\n\n- paper_id: chen2022transdreamer\n  title: \"TransDreamer: Reinforcement Learning with Transformer World Models\"\n  authors: [Chen C., Wu Y.-F., Yoon J., Ahn S.]\n  year: 2022\n  venue: \"arXiv:2202.09481\"\n  category: background\n  role: \"Replaces RSSM with Transformer State-Space Model; directly tests whether RSSM-specific architecture contributes to temporal abstraction failures\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: 2024-2026 concurrent work on temporal abstraction in world models\n# ============================================================\n\n- paper_id: gumbsch2024thick\n  title: \"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\"\n  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]\n  year: 2024\n  venue: ICLR\n  category: direct-competitor\n  role: \"THICK — learns adaptive temporal abstractions via context-change detection; closest concurrent work — addresses temporal abstraction in Dreamer but via hierarchy rather than variable-dt imagination\"\n  relevance_score: 5\n\n- paper_id: mattes2024hieros\n  title: \"Hieros: Hierarchical Imagination on Structured State Space Sequence World Models\"\n  authors: [Mattes P., Schlosser R., Herbrich R.]\n  year: 2024\n  venue: ICML\n  category: direct-competitor\n  role: \"Multi-scale hierarchical imagination with S5 world model; demonstrates temporal abstraction via hierarchy avoids the single-scale dt-embedding failure we identify\"\n  relevance_score: 5\n\n# ============================================================\n# NEW: Seed-dependent instability & value overestimation in MBRL\n# ============================================================\n\n- paper_id: henderson2018deep\n  title: \"Deep Reinforcement Learning that Matters\"\n  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]\n  year: 2018\n  venue: AAAI\n  category: background\n  role: \"Foundational study on seed variance in deep RL — shows statistically different performance distributions arise from random seeds alone with identical hyperparameters; directly supports our observation that seed 0 vs seed 2 produce qualitatively different value dynamics under the same dt_embed_dim=0 config\"\n  relevance_score: 4\n\n- paper_id: nikishin2022primacy\n  title: \"The Primacy Bias in Deep Reinforcement Learning\"\n  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]\n  year: 2022\n  venue: ICML\n  category: background\n  role: \"Identifies primacy bias — agents overfit early data and lose ability to learn from new transitions, leading to delayed performance collapse; parallels our finding where value overestimation initially appears benign but becomes pathological later, and the collapse timing is seed-dependent\"\n  relevance_score: 4\n\n- paper_id: qiao2023mind\n  title: \"Mind the Model, Not the Agent: The Primacy Bias in Model-based RL\"\n  authors: [Qiao Z., Lyu J., Li X.]\n  year: 2023\n  venue: \"arXiv:2310.15017 (ECAI 2024)\"\n  category: evaluation\n  role: \"Extends primacy bias to MBRL, testing on DreamerV2 — shows world model primacy bias dominates over agent primacy bias; directly relevant to Dreamer-family training instability and explains why some seeds recover (model escapes early overfitting) while others don't\"\n  relevance_score: 5\n\n- paper_id: hussing2024dissecting\n  title: \"Dissecting Deep RL with High Update Ratios: Combatting Value Divergence\"\n  authors: [Hussing M., Voelcker C.A., Gilitschenski I., Farahmand A.-M., Eaton E.]\n  year: 2024\n  venue: \"Reinforcement Learning Journal (RLC 2024)\"\n  category: evaluation\n  role: \"Shows value overestimation and Q-divergence under high update-to-data ratios, driven by optimizer momentum — overestimation occurs on both in-distribution and OOD data; mechanism maps to our CIVO where imagination-trained critic inflates values progressively, with divergence onset sensitive to initialization\"\n  relevance_score: 4\n\n- paper_id: barkley2024stealing\n  title: \"Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning\"\n  authors: [Barkley B., Fridovich-Keil D.]\n  year: 2024\n  venue: \"arXiv:2412.14312 (ICML 2025)\"\n  category: evaluation\n  role: \"Demonstrates that synthetic rollouts (imagination) can degrade performance inconsistently across environments, with overestimation bias as a contributing factor; supports our finding that imagination-based training creates environment- and seed-dependent failure modes that existing mitigation techniques do not reliably fix\"\n  relevance_score: 3\n\n- paper_id: bjorck2022variance\n  title: \"Is High Variance Unavoidable in RL? A Case Study in Continuous Control\"\n  authors: [Bjorck J., Gomes C.P., Weinberger K.Q.]\n  year: 2022\n  venue: ICLR\n  category: background\n  role: \"Shows RL variance mostly arises early in training from poor 'outlier' runs caused by numerical instability; parallels our observation that seed 2 diverges early while seed 0 recovers — the reward prediction degradation from removing dt_embedding may create exactly this early-training instability\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Reward prediction quality → MBRL performance\n# ============================================================\n# Our key finding: removing dt_embedding causes reward_MAE to spike 75x\n# (0.01 → 0.747), making performance seed-dependent. These papers\n# establish that reward prediction quality is a known MBRL bottleneck.\n\n- paper_id: lee2024dreamsmooth\n  title: \"DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing\"\n  authors: [Lee V., Abbeel P., Lee Y.]\n  year: 2024\n  venue: ICLR\n  category: background\n  role: \"Directly demonstrates reward prediction is a bottleneck in MBRL — sparse/ambiguous rewards cause the reward model to predict zeros, creating gradient-free landscapes during imagination; our dt_embed_dim=0 ablation creates an analogous bottleneck where the reward head loses temporal conditioning and MAE spikes 75x\"\n  relevance_score: 5\n\n- paper_id: ma2024harmonydream\n  title: \"HarmonyDream: Task Harmonization Inside World Models\"\n  authors: [Ma H., Wu J., Feng N., Xiao C., Li D., Hao J., Wang J., Long M.]\n  year: 2024\n  venue: ICML\n  category: background\n  role: \"Shows observation prediction dominates reward prediction in world model training, degrading reward model quality; proposes dynamic loss balancing for 10-69% gains — directly relevant to our finding that dt_embedding removal disrupts the observation-reward prediction balance and causes reward MAE explosion\"\n  relevance_score: 5\n\n- paper_id: lambert2020objective\n  title: \"Objective Mismatch in Model-based Reinforcement Learning\"\n  authors: [Lambert N., Amos B., Yadan O., Calandra R.]\n  year: 2020\n  venue: \"L4DC (Proceedings of Machine Learning Research, vol. 120)\"\n  category: background\n  role: \"Formalizes that one-step prediction likelihood does not correlate with control performance — the 'objective mismatch' problem; our work reveals a specific instance: the reward head's prediction accuracy (measured by MAE) directly gates whether the critic can learn stable value estimates, creating a reward-specific objective mismatch\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: Auxiliary tasks & representation coupling in world models\n# ============================================================\n# Our finding: reward prediction quality is tightly coupled to temporal\n# conditioning (dt_embedding). Removing the embedding degrades the\n# reward head while dynamics remain intact — suggesting the reward head\n# acts as more than a passive predictor; it conditions the shared\n# representation. Literature gap: no prior work studies this coupling\n# specifically in Dreamer-family world models.\n\n- paper_id: jaderberg2017unreal\n  title: \"Reinforcement Learning with Unsupervised Auxiliary Tasks\"\n  authors: [Jaderberg M., Mnih V., Czarnecki W.M., Schaul T., Leibo J.Z., Silver D., Kavukcuoglu K.]\n  year: 2017\n  venue: ICLR\n  category: background\n  role: \"UNREAL — introduces reward prediction as an auxiliary task that shapes shared representations; foundational evidence that reward prediction is not just a passive output but actively conditions what features the network learns — our finding that removing dt_embedding selectively degrades reward prediction (but not dynamics) suggests the temporal conditioning specifically enables reward-relevant feature extraction\"\n  relevance_score: 4\n\n- paper_id: lyle2021auxiliary\n  title: \"On The Effect of Auxiliary Tasks on Representation Dynamics\"\n  authors: [Lyle C., Rowland M., Ostrovski G., Dabney W.]\n  year: 2021\n  venue: AISTATS\n  category: background\n  role: \"Theoretical analysis showing auxiliary tasks shape representations toward top eigenvectors of the transition operator; provides formal grounding for why removing temporal conditioning from the reward head could alter the entire representation — the reward head's gradients contribute to spectral structure of the shared latent space\"\n  relevance_score: 4\n\n# ============================================================\n# NEW: DreamerV3 architecture improvements (2025-2026)\n# ============================================================\n\n- paper_id: bredis2026nedreamer\n  title: \"Next Embedding Prediction Makes World Models Stronger\"\n  authors: [Bredis G., Balagansky N., Gavrilov D., Rakhimov R.]\n  year: 2026\n  venue: \"arXiv:2603.02765\"\n  category: background\n  role: \"NE-Dreamer — decoder-free MBRL replacing pixel reconstruction with next-embedding prediction via temporal transformer + Barlow Twins; improves RSSM prediction quality on DMC and DMLab but does not address temporal abstraction or CIVO — orthogonal to our dt-embedding diagnosis\"\n  relevance_score: 3\n\n- paper_id: zhang2025dymodreamer\n  title: \"DyMoDreamer: World Modeling with Dynamic Modulation\"\n  authors: [Zhang B., Wang R., Xiao W., Zhang W., Sun J., Huang G., Chen J., Wang G.]\n  year: 2025\n  venue: NeurIPS\n  category: background\n  role: \"Modulates RSSM via inter-frame differencing mask and stochastic categorical dynamic modulation; SOTA on Atari 100k (156.6% HNS) and DMC (832) — improves dynamics extraction but does not address variable-rate imagination or dt_embedding-induced value overestimation\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Temporal abstraction methods\n# ============================================================\n\n- paper_id: liu2025vanta\n  title: \"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning\"\n  authors: [Liu T.-S., Liu X.-H., Chen R., Jin L., Wang P., Zhang Z., Yu Y.]\n  year: 2025\n  venue: ICLR\n  category: method-component\n  role: \"VanTA — VLM-guided trajectory decomposition into semantically meaningful skills via vector quantization + relabeling; operates at high-level skill abstraction (Franka Kitchen, Crafter) — contrasts with our low-level dt-based temporal abstraction within world-model imagination steps\"\n  relevance_score: 3\n\n# ============================================================\n# NEW: Evaluation methodology\n# ============================================================\n\n- paper_id: agarwal2021precipice\n  title: \"Deep Reinforcement Learning at the Edge of the Statistical Precipice\"\n  authors: [Agarwal R., Schwarzer M., Castro P.S., Courville A.C., Bellemare M.]\n  year: 2021\n  venue: NeurIPS\n  category: evaluation\n  role: \"Proposes rliable — interval estimates, performance profiles, IQM for robust multi-seed RL evaluation (NeurIPS Outstanding Paper); our multi-seed experiment design follows this methodology to ensure statistical validity of collapse detection across seeds\"\n  relevance_score: 4\n\n# ============================================================\n# NEW (2026-05-14 gap analysis): Time discretization theory\n# ============================================================\n# Gap: variable timestep / time discretization invariance — foundational\n# theory for why dt matters and how to handle it.\n\n- paper_id: tallec2019making\n  title: \"Making Deep Q-learning methods Robust to Time Discretization\"\n  authors: [Tallec C., Blier L., Ollivier Y.]\n  year: 2019\n  venue: \"ICML (arXiv:1901.09732)\"\n  category: background\n  role: \"Shows Q-learning performance is highly sensitive to time discretization δ; proposes architectural + exploration modifications for δ-invariance. Theoretical foundation for why our variable-dt imagination introduces a fundamental difficulty: RSSM trained at δ=1 cannot produce δ-invariant predictions at dt>1\"\n  relevance_score: 4\n\n- paper_id: park2021sar\n  title: \"Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods\"\n  authors: [Park S., Kim J., Kim G.]\n  year: 2021\n  venue: \"NeurIPS (arXiv:2111.03941)\"\n  category: method-component\n  role: \"SAR — δ-invariant action repetition for policy gradients; achieves time-discretization robustness in model-free RL via adaptive reaction to state changes during repetition. Contrasts with our finding that world-model RL lacks this robustness when imagination uses dt>1\"\n  relevance_score: 4\n\n- paper_id: wang2024seac\n  title: \"Reinforcement Learning with Elastic Time Steps\"\n  authors: [Wang D., Beltrame G.]\n  year: 2024\n  venue: \"arXiv:2402.14961\"\n  category: method-component\n  role: \"SEAC/MOSEAC — variable-duration time steps where agent selects both action and duration; model-free approach that explicitly treats action duration as part of the action space. Our work reveals why this strategy is problematic in world-model RL: the critic cannot reliably evaluate variable-duration imagined trajectories\"\n  relevance_score: 3\n\n# ============================================================\n# NEW (2026-05-14 gap analysis): Delusional bias mitigation\n# ============================================================\n\n- paper_id: su2020conqur\n  title: \"ConQUR: Mitigating Delusional Bias in Deep Q-learning\"\n  authors: [Su D., Ooi J., Lu T., Schuurmans D., Boutilier C.]\n  year: 2020\n  venue: \"ICML (arXiv:2002.12399)\"\n  category: background\n  role: \"Follow-up to Lu et al. 2018; mitigates delusional bias via consistency-penalized Q-labels. Addresses delusional bias from policy-class constraints in Q-learning; our CIVO is an analogous phenomenon in MBRL where temporal conditioning (dt_embedding) creates inconsistent value targets across imagination steps\"\n  relevance_score: 4\n\n# ============================================================\n# NEW (2026-05-14 gap analysis): Diagnostic methodology in RL\n# ============================================================\n# Gap: our paper is a diagnostic analysis — need methodological\n# precedents for \"what matters\" / \"implementation matters\" style papers.\n\n- paper_id: engstrom2020implementation\n  title: \"Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO\"\n  authors: [Engstrom L., Ilyas A., Santurkar S., Tsipras D., Janoos F., Rudolph L., Madry A.]\n  year: 2020\n  venue: \"ICLR (arXiv:2005.12729)\"\n  category: evaluation\n  role: \"Demonstrates that code-level implementation details (not algorithmic innovations) drive most of PPO's gains over TRPO; methodological precedent for our diagnostic approach — we similarly show that a specific implementation choice (trained vs. untrained dt_embedding) is the primary factor determining collapse vs. stability\"\n  relevance_score: 4\n\n- paper_id: andrychowicz2021whatmatters\n  title: \"What Matters for On-Policy Deep Actor-Critic Methods? A Large-Scale Study\"\n  authors: [Andrychowicz M., Raichuk A., Stańczyk P., Orsini M., Girgin S., Marinier R., Hussenot L., Geist M., Pietquin O., Michalski M., Gelly S., Bachem O.]\n  year: 2021\n  venue: \"ICLR (arXiv:2006.05990)\"\n  category: evaluation\n  role: \"Large-scale factorial study of 50+ design choices in on-policy RL (250K+ agents); methodological template for our factorial experiment design isolating dt_embedding × subsample × horizon effects. Demonstrates that systematic ablation reveals non-obvious interactions — parallel to our finding that dt_embedding training status interacts with subsample and horizon\"\n  relevance_score: 4\n\n# ============================================================\n# NEW (2026-05-14 gap analysis): MBRL rollout quality & value overestimation\n# ============================================================\n# Gap: recent ICLR 2025 papers directly studying imagination rollout\n# quality and value overestimation in model-based settings.\n\n- paper_id: frauenknecht2025rollouts\n  title: \"On Rollouts in Model-Based Reinforcement Learning\"\n  authors: [Frauenknecht B., Subhasish D., Solowjow F., Trimpe S.]\n  year: 2025\n  venue: \"ICLR (arXiv:2501.16918)\"\n  category: evaluation\n  role: \"Shows trajectory-sampling rollouts diverge from ground truth after few steps and can harm policy learning; proposes Infoprop separating aleatoric/epistemic uncertainty with rollout termination criteria. Directly supports our finding that dt>1 imagination produces corrupted data — our work identifies a specific mechanism (dt_embedding-induced value exploitation) beyond general compounding error\"\n  relevance_score: 5\n\n- paper_id: voelcker2025madtd\n  title: \"MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL\"\n  authors: [Voelcker C., Hussing M., Eaton E., Farahmand A.-M., Gilitschenski I.]\n  year: 2025\n  venue: \"ICLR (arXiv:2410.08896)\"\n  category: evaluation\n  role: \"Shows value function misgeneralization to on-policy actions causes instability at high UTD ratios; uses model-generated data to improve value accuracy. Complementary to our finding: MAD-TD addresses value misgeneralization from replay distribution mismatch, we address value overestimation from temporal conditioning corruption in imagination\"\n  relevance_score: 4\n\n# ============================================================\n# NEW (2026-05-14 gap analysis): Latest action repeat methods\n# ============================================================\n\n- paper_id: nie2025sdar\n  title: \"Select before Act: Spatially Decoupled Action Repetition for Continuous Control\"\n  authors: [Nie B., et al.]\n  year: 2025\n  venue: \"ICLR (arXiv:2502.06919)\"\n  category: method-component\n  role: \"SDAR — per-dimension action repetition decisions for flexible temporal persistence in model-free RL; SOTA on DMC continuous control. Advances action repeat in model-free setting; our work shows the fundamental obstacle to analogous variable-rate approaches in model-based RL (CIVO from dt_embedding)\"\n  relevance_score: 3\n\n# ============================================================\n# NEW (2026-05-14 gap analysis): DreamerV4 / latest Dreamer evolution\n# ============================================================\n\n- paper_id: hafner2025dreamerv4\n  title: \"Training Agents Inside of Scalable World Models\"\n  authors: [Hafner D., Yan W., Lillicrap T.]\n  year: 2025\n  venue: \"arXiv:2509.24527\"\n  category: background\n  role: \"DreamerV4 — replaces RSSM with efficient transformer world model + shortcut forcing; scales to video pretraining (Minecraft diamonds from video). Architectural successor to DreamerV3; our dt_embedding diagnosis is specific to RSSM but the broader lesson (temporal conditioning must match model fidelity) applies to transformer world models\"\n  relevance_score: 4\n\n# ============================================================\n# NEW (2026-05-14): Training instability dynamics\n# ============================================================\n\n- paper_id: zhang2026instability\n  title: \"Training instability in deep learning follows low-dimensional dynamical principles\"\n  authors: [Zhang L., et al.]\n  year: 2026\n  venue: \"ICLR 2026 (arXiv:2601.13160)\"\n  category: background\n  role: \"Training instability follows low-dimensional dynamical principles; provides theoretical framework for why seed-dependent collapse vs self-correction occurs in our experiments (008d seed 1 collapses, 009b seed 2 self-corrects under identical config)\"\n  relevance_score: 5\n\n# ============================================================\n# NEW (2026-05-14): Seed-Dependent Stochastic Outcomes in MBRL\n# ============================================================\n# Dedicated literature survey for the stochastic collapse phenomenon:\n# same config (trained dt_embedding + subsample + H=8) produces\n# collapse in seed 0 (008d) but self-correction in seed 2 (009b).\n# nve>1.5x is a 100% reliable marker of trained dt_embedding,\n# but collapse itself is stochastic (1/2 seeds).\n\n- paper_id: sokar2023dormant\n  title: \"The Dormant Neuron Phenomenon in Deep Reinforcement Learning\"\n  authors: [Sokar G., Agarwal R., Castro P.S., Evci U.]\n  year: 2023\n  venue: \"ICML 2023\"\n  category: background\n  role: \"Identifies dormant neurons — inactive units accumulating during RL training that reduce network expressivity. Seed-dependent because different random initializations produce different early dormancy patterns; directly explains why some seeds lose the representational capacity needed to self-correct value overestimation (our seed 0 collapses) while others retain enough active neurons to recover (our seed 2 self-corrects)\"\n  relevance_score: 4\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: lyle2022capacity\n  title: \"Understanding and Preventing Capacity Loss in Reinforcement Learning\"\n  authors: [Lyle C., Rowland M., Dabney W.]\n  year: 2022\n  venue: \"ICLR 2023 (arXiv:2204.09560)\"\n  category: background\n  role: \"Shows feature rank collapse from non-stationary TD targets is a necessary condition for learning failure but not sufficient — sparse rewards and other factors must co-occur. Directly parallels our finding: nve>1.5x (value overestimation from trained dt_embedding) is a necessary precondition for collapse but not a sufficient one; additional stochastic factors (initialization, early replay composition) determine whether collapse actually occurs\"\n  relevance_score: 5\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: kumar2022dr3\n  title: \"DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization\"\n  authors: [Kumar A., Agarwal R., Ma T., Courville A., Tucker G., Levine S.]\n  year: 2022\n  venue: \"ICLR 2022\"\n  category: background\n  role: \"Shows implicit regularization from TD learning favors degenerate feature aliasing (states on both sides of Bellman backup become indistinguishable), creating the substrate for value overestimation. In our setting, trained dt_embedding amplifies this aliasing across different temporal horizons — the critic cannot distinguish between dt=1 and dt>1 value targets, enabling exploitation. Feature aliasing is seed-dependent because it depends on initialization geometry\"\n  relevance_score: 4\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: colas2018seeds\n  title: \"How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments\"\n  authors: [Colas C., Sigaud O., Oudeyer P.-Y.]\n  year: 2018\n  venue: \"arXiv:1806.08295\"\n  category: evaluation\n  role: \"Provides statistical framework for determining seed count needed for significant algorithm comparison; our 2-seed observation (1/2 collapse) has limited statistical power by their analysis — but the qualitative difference (nve 4.12x vs 0.38x) is large enough that even 2 seeds establish the stochastic nature of the phenomenon. Methodological basis for future multi-seed validation\"\n  relevance_score: 3\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: nikishin2023plasticity\n  title: \"Deep Reinforcement Learning with Plasticity Injection\"\n  authors: [Nikishin E., Oh J., Ostrovski G., Lyle C., Pascanu R., Dabney W., Barreto A.]\n  year: 2023\n  venue: \"NeurIPS 2023\"\n  category: method-component\n  role: \"Plasticity injection augments network plasticity without changing parameter count; serves as a diagnostic tool — if injection improves performance, plasticity loss was the bottleneck. Directly applicable to diagnosing whether our seed-dependent collapse is plasticity-mediated: if plasticity injection prevents collapse in seed 0 but has no effect on seed 2 (which already self-corrects), it confirms plasticity loss as the bifurcation mechanism\"\n  relevance_score: 4\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: schwarzer2023bbf\n  title: \"Bigger, Better, Faster: Human-level Atari with Human-level Efficiency\"\n  authors: [Schwarzer M., Obando-Ceron J.S., Courville A., Bellemare M., Agarwal R., Castro P.S.]\n  year: 2023\n  venue: \"ICML 2023\"\n  category: method-component\n  role: \"BBF achieves SOTA sample efficiency via periodic network resets + scaling + weight decay; periodic resets prevent primacy bias accumulation across seeds. Suggests our CIVO collapse might be preventable with periodic critic resets — the reset would break the positive feedback loop between overestimated values and actor exploitation before it becomes irreversible\"\n  relevance_score: 3\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: farebrother2024stopregressing\n  title: \"Stop Regressing: Training Value Functions via Classification for Scalable Deep RL\"\n  authors: [Farebrother J., Orbay J., Vuong Q., Taiga A.A., Chebotar Y., Xiao T., Irpan A., Levine S., Castro P.S., Faust A., Kumar A., Agarwal R.]\n  year: 2024\n  venue: \"ICML 2024\"\n  category: method-component\n  role: \"Shows categorical cross-entropy for value training provides implicit regularization against overestimation vs MSE regression. DreamerV3 already uses categorical value prediction (twohot + symlog) — yet our trained dt_embedding still induces collapse in some seeds, demonstrating that categorical value training is insufficient to prevent dt_embedding-induced value exploitation\"\n  relevance_score: 3\n  survey_tag: seed-dependent-stochastic-outcomes\n\n- paper_id: lyle2024normalization\n  title: \"Normalization and Effective Learning Rates in Reinforcement Learning\"\n  authors: [Lyle C., Zheng Z., Giunchiglia E., Sherstan C., Hashemizadeh M., Schuurmans D., Dabney W.]\n  year: 2024\n  venue: \"NeurIPS 2024\"\n  category: background\n  role: \"Shows normalization layers combat overestimation but cause effective learning rate decay via parameter norm growth. Provides a potential mechanism for seed 2's self-correction: if parameter norms grow faster in certain initializations, effective LR decays faster, naturally damping value overestimation before it cascades into collapse. Seed 0's slower norm growth → sustained high effective LR → overestimation compounds → collapse\"\n  relevance_score: 4\n  survey_tag: seed-dependent-stochastic-outcomes\n\n# --- Survey synthesis: Seed-Dependent Stochastic Outcomes ---\n# Summary (2026-05-14):\n#\n# 1. STOCHASTIC COLLAPSE HAS PRECEDENT:\n#    Plasticity loss (Lyle 2022, Sokar 2023, Nikishin 2023) is inherently\n#    seed-dependent because it depends on initialization → early gradient\n#    dynamics → neuron activity patterns. Different seeds hit different\n#    plasticity trajectories under identical configs.\n#\n# 2. nve>1.5x AS DIAGNOSTIC MARKER (necessary but not sufficient):\n#    Lyle 2022 shows feature rank collapse is necessary but not sufficient\n#    for learning failure. Kumar 2022 shows feature aliasing from TD\n#    learning creates the overestimation substrate. Our nve>1.5x is\n#    analogous: it indicates the dt_embedding has enabled value exploitation\n#    (100% reliable marker), but collapse requires additional conditions\n#    (plasticity loss, insufficient effective LR decay) that are stochastic.\n#\n# 3. SELF-CORRECTION MECHANISM:\n#    Lyle 2024 provides a candidate mechanism: normalization-induced\n#    effective LR decay can naturally damp overestimation in some seeds.\n#    Farebrother 2024 shows categorical value training provides partial\n#    implicit regularization. Together these explain why seed 2 self-corrects:\n#    the combination of DreamerV3's categorical critic + normalization +\n#    favorable initialization produces enough implicit regularization to\n#    overcome the dt_embedding-induced overestimation.\n#\n# 4. THEORETICAL GROUNDING:\n#    Zhang 2026 (already in map) provides the dynamical systems framework.\n#    Bjorck 2022 (already in map) shows early outlier events dominate\n#    variance. Together with the new papers, the framing is:\n#    \"trained dt_embedding creates a necessary condition (nve>1.5x) for\n#    CIVO collapse, but collapse is a stochastic bifurcation\n#    whose outcome depends on seed-dependent plasticity dynamics.\"\n\n# ============================================================\n# INCREMENTAL SCAN (2026-05-14): Δt conditioning & adaptive horizon\n# ============================================================\n# 8 new papers from targeted search on:\n#   - Δt/timestep conditioning in world models\n#   - Variable-rate imagination / adaptive horizon\n#   - Hierarchical planning with latent world models (2025-2026)\n#\n# KEY FINDING: TAWM (Nhu et al. ICML 2025) explicitly conditions\n# world model on Δt — closest methodological overlap. But TAWM\n# uses TD-MPC2 (online MPC) not imagination-based actor-critic,\n# and treats Δt conditioning as beneficial. Our work diagnoses\n# Δt conditioning as pathological in imagination-based training\n# (CIVO). Complementary, not duplicative.\n\n- paper_id: nhu2025tawm\n  title: \"Time-Aware World Model for Adaptive Prediction and Control\"\n  authors: [Nhu A.N., Son S., Lin M.C.]\n  year: 2025\n  venue: \"ICML 2025 (arXiv:2506.08441)\"\n  category: direct-competitor\n  role: \"TAWM — explicitly conditions world model on time-step size Δt and trains over diverse Δt values for multi-rate dynamics learning. Built on TD-MPC2 (online MPC). KEY DISTINCTION from our work: (1) TAWM treats Δt conditioning as beneficial for performance/data-efficiency; we diagnose it as pathological in imagination-based actor-critic training (CIVO). (2) TAWM uses MPC (no imagination rollouts for policy training); our failure mode is specific to imagination-based training where the critic exploits dt-conditioned value estimates. (3) TAWM focuses on observation-rate robustness; we focus on value overestimation from temporal conditioning corruption. TAWM actually strengthens our contribution: it shows Δt conditioning works in MPC settings, making our finding that it fails in imagination-based settings a surprising and important diagnostic.\"\n  relevance_score: 5\n  novelty_threat: \"MEDIUM — methodological overlap (Δt conditioning) but fundamentally different paradigm (MPC vs imagination) and opposite conclusion (beneficial vs pathological). Must cite and differentiate in paper.\"\n\n- paper_id: li2025lsimagine\n  title: \"Open-World Reinforcement Learning over Long Short-Term Imagination\"\n  authors: [Li J., Wang Q., Wang Y., Jin X., Li Y., Zeng W., Yang X.]\n  year: 2025\n  venue: \"ICLR 2025 Oral (arXiv:2410.03618)\"\n  category: direct-competitor\n  role: \"LS-Imagine — extends imagination horizon in Dreamer via goal-conditioned jumpy state transitions and affordance maps. Addresses the 'short-sightedness' of standard Dreamer imagination. KEY DISTINCTION: LS-Imagine adds jumpy transitions to reach long-horizon targets (open-world Minecraft), while our work shows that variable-dt imagination itself introduces CIVO. LS-Imagine's jumpy transitions use goal conditioning (not dt-embedding), potentially avoiding the value overestimation we identify.\"\n  relevance_score: 4\n  novelty_threat: \"LOW — different mechanism (goal-conditioned jumps vs dt-embedding) and different focus (long-horizon exploration vs diagnostic of failure modes). Should cite as concurrent approach to extending imagination horizon.\"\n\n- paper_id: zhang2026hwm\n  title: \"Hierarchical Planning with Latent World Models\"\n  authors: [Zhang W., Terver B., Zholus A., Chitnis S., Sutaria H., Assran M., Balestriero R., Bar A., Bardes A., LeCun Y., Ballas N.]\n  year: 2026\n  venue: \"arXiv:2604.03208\"\n  category: direct-competitor\n  role: \"HWM — learns multi-scale latent world models for hierarchical MPC planning; high-level planner optimizes macro-actions, low-level planner handles primitives. 70% success on real-world non-greedy robotic tasks vs 0% for single-level. Addresses temporal abstraction via hierarchical planning (MPC), not imagination-based actor-critic. Further evidence that temporal abstraction in world models requires hierarchy rather than single-scale variable-dt approaches.\"\n  relevance_score: 4\n  novelty_threat: \"LOW — MPC-based hierarchical planning, not imagination-based training. Supports our thesis that flat dt-embedding approaches are inferior to hierarchical alternatives.\"\n\n- paper_id: kobayashi2025metacontroller\n  title: \"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning\"\n  authors: [Kobayashi S., et al.]\n  year: 2025\n  venue: \"arXiv:2512.20605\"\n  category: method-component\n  role: \"MetaController — discovers temporal abstractions via higher-order non-causal sequence model controlling base autoregressive model's residual stream. Each controller executes behaviorally meaningful action sequences with learned termination conditions. Operates in fundamentally different paradigm (LLM-style autoregressive models, not world-model imagination), but demonstrates that temporal abstraction benefits from hierarchical structure rather than flat dt-conditioning.\"\n  relevance_score: 3\n\n- paper_id: shaj2023mts3\n  title: \"Multi Time Scale World Models\"\n  authors: [Shaj V., Gholam Zadeh S., Demir O., Douat L.R., Neumann G.]\n  year: 2023\n  venue: \"NeurIPS 2023 (arXiv:2310.18534)\"\n  category: method-component\n  role: \"MTS3 — probabilistic multi-time-scale state space model with fast and slow latent dynamics for variable-rate prediction. Provides efficient inference across temporal scales. Foundational multi-rate dynamics architecture; our work shows that even with proper multi-rate modeling, the downstream actor-critic training in imagination can exploit temporal conditioning for value overestimation — a failure mode MTS3 does not address (it focuses on prediction quality, not policy training).\"\n  relevance_score: 4\n\n- paper_id: splates2025\n  title: \"Stable Planning with Temporally Extended Skills\"\n  authors: [SPlaTES authors]\n  year: 2025\n  venue: \"Reinforcement Learning Journal (RLC 2025)\"\n  category: method-component\n  role: \"SPlaTES — hierarchical MPC with temporally extended skills + abstract skill world model. Skill learning via mutual-information objective yields diverse, predictable, task-related behavior. Demonstrates that stable long-horizon planning requires modeling skill outcomes (temporal abstraction via hierarchy), not primitive-action outcomes at variable time steps — consistent with our finding that flat dt-embedding fails.\"\n  relevance_score: 3\n\n- paper_id: beckerehmck2023multitimestep\n  title: \"Multi-timestep models for Model-based Reinforcement Learning\"\n  authors: [Becker-Ehmck P., Peters J., van der Smagt P.]\n  year: 2023\n  venue: \"arXiv:2310.05672\"\n  category: background\n  role: \"Proposes multi-timestep training objective (weighted sum of losses at various future horizons) for one-step dynamics models to improve long-horizon R² score. Addresses compounding error at the model training level; our work shows that even with perfect multi-step prediction, the imagination-based actor-critic can still fail due to value overestimation from dt-conditioning — a downstream failure mode distinct from prediction accuracy.\"\n  relevance_score: 3\n\n- paper_id: liu2022dmve\n  title: \"Dynamic-Horizon Model-Based Value Estimation With Latent Imagination\"\n  authors: [Liu Y., et al.]\n  year: 2022\n  venue: \"IEEE TNNLS (arXiv:2009.09593)\"\n  category: background\n  role: \"DMVE — adaptive rollout horizon selection via horizon reliability detection (comparing value expansion errors between raw and reconstructed observations). Addresses the horizon selection problem in imagination-based value estimation. Complementary to our work: DMVE selects among fixed-dt horizons; we show that even optimal horizon selection cannot fix the CIVO when dt-embedding is trained (the overestimation is in the value function, not the horizon length).\"\n  relevance_score: 3\n\n# --- Incremental scan synthesis (2026-05-14) ---\n#\n# NOVELTY ASSESSMENT:\n# No paper found that diagnoses dt_embedding → CIVO\n# (value overestimation) → stochastic collapse in imagination-based\n# MBRL. Our core contribution remains novel.\n#\n# TAWM (ICML 2025) is the closest methodological overlap but\n# operates in MPC paradigm and reaches opposite conclusion\n# (Δt conditioning is beneficial). This actually STRENGTHENS\n# our novelty: \"Δt conditioning helps in MPC but hurts in\n# imagination-based training\" is a more nuanced and surprising finding.\n#\n# LANDSCAPE TREND:\n# The field is converging on HIERARCHY (THICK, Hieros, Director,\n# HWM, SPlaTES, MetaController) as the solution to temporal\n# abstraction in world models, avoiding flat variable-dt approaches.\n# Our diagnostic paper explains WHY flat dt approaches fail,\n# providing theoretical grounding for this empirical trend.\n#\n# ACTION ITEMS FOR PAPER:\n# 1. MUST CITE: nhu2025tawm — differentiate MPC vs imagination paradigm\n# 2. SHOULD CITE: li2025lsimagine — concurrent Dreamer horizon extension\n# 3. SHOULD CITE: shaj2023mts3 — multi-rate dynamics foundation\n# 4. CONSIDER: zhang2026hwm — latest hierarchical WM planning\n\n# ============================================================\n# INCREMENTAL SCAN (2026-05-15): Value expansion horizon & overestimation\n# ============================================================\n# 4 new papers from targeted search on:\n#   - \"temporal abstraction\" + \"world model\" + RL (2024-2026)\n#   - \"CIVO\" / \"value overestimation\" + MBRL\n#   - \"imagination horizon\" + world model\n#   - \"value function collapse\" / \"value divergence\" + MBRL\n#   - variable timestep imagination + actor-critic failure\n#\n# KEY FINDING: Still NO paper diagnosing dt_embedding → CIVO\n# → stochastic collapse in imagination-based MBRL.\n# Core contribution remains novel. Palenicek 2025 is the most\n# relevant new addition — shows even oracle dynamics don't help\n# with longer rollout horizons, supporting our thesis that the\n# bottleneck is NOT model accuracy but value estimation corruption.\n\n- paper_id: palenicek2025diminishing\n  title: \"Diminishing Return of Value Expansion Methods\"\n  authors: [Palenicek D., Lutter M., Carvalho J., Dennert D., Ahmad F., Peters J.]\n  year: 2025\n  venue: \"Reinforcement Learning Journal (RLC 2025, arXiv:2412.20537)\"\n  category: evaluation\n  role: \"Shows longer model-based rollout horizons have diminishing returns in sample efficiency — even with oracle dynamics models, each additional expansion step yields progressively smaller gains. The bottleneck is NOT model accuracy. Directly supports our finding: extending imagination horizon via dt>1 does not improve performance because the problem lies in value estimation (CIVO from dt_embedding), not dynamics quality. Strengthens our argument that dt=1 imagination is sufficient.\"\n  relevance_score: 5\n\n- paper_id: kim2025deas\n  title: \"DEAS: DEtached value learning with Action Sequence for Scalable Offline RL\"\n  authors: [Kim C., Seo Y., et al.]\n  year: 2025\n  venue: \"arXiv:2510.07730\"\n  category: method-component\n  role: \"Shows action sequences (temporal extension via options/semi-MDP) cause excessive value overestimation in actor-critic algorithms; proposes detached value learning where critic trains separately from policy. Parallel to our finding: temporal extension (whether via action sequences or dt-embedding) creates value overestimation in actor-critic; DEAS's detached learning is analogous to our dt=1 imagination fix (decoupling temporal abstraction from value estimation).\"\n  relevance_score: 4\n\n- paper_id: luo2025vpl\n  title: \"A Case for Validation Buffer in Pessimistic Actor-Critic\"\n  authors: [Luo F., et al.]\n  year: 2025\n  venue: \"IJCAI 2025 (arXiv:2403.01014)\"\n  category: method-component\n  role: \"Validation Pessimism Learning (VPL) — uses validation buffer to adaptively adjust pessimism levels throughout training; shows pessimism is beneficial only during overestimation, detrimental during underestimation. Relevant to our setting: our trained dt_embedding creates persistent overestimation (nve>1.5x), suggesting adaptive pessimism could be a complementary mitigation to our dt=1 imagination restriction.\"\n  relevance_score: 3\n\n- paper_id: lenz2025macura\n  title: \"Trust the Model Where It Trusts Itself -- Model-Based Actor-Critic with Uncertainty-Aware Rollout Adaption\"\n  authors: [Lenz S., et al.]\n  year: 2025\n  venue: \"arXiv:2405.19014\"\n  category: method-component\n  role: \"MACURA — uses model uncertainty to adaptively determine local rollout length in model-based actor-critic; avoids uniform rollout horizon. Addresses rollout quality from the uncertainty perspective; our work identifies a different mechanism: even if the model is confident, dt-embedding-conditioned imagination can produce overestimated value estimates (CIVO). MACURA's uncertainty-based termination would not catch our failure mode because the model predictions may be accurate while value estimates are corrupted.\"\n  relevance_score: 3\n\n# --- Incremental scan synthesis (2026-05-15) ---\n#\n# NOVELTY ASSESSMENT (confirmed):\n# No paper found that diagnoses dt_embedding → CIVO\n# (value overestimation) → stochastic collapse in imagination-based\n# MBRL. Core contribution remains novel after 2nd scan.\n#\n# KEY NEW INSIGHT from Palenicek 2025:\n# Even oracle dynamics models show diminishing returns with longer\n# rollouts. This means the value estimation bottleneck (not model\n# accuracy) is increasingly recognized as the fundamental limit\n# of imagination-based MBRL — our paper explains a specific\n# mechanism (dt_embedding-induced CIVO) by which\n# this bottleneck manifests.\n#\n# DEAS (Kim 2025) provides independent evidence from offline RL\n# that temporal extension (action sequences) → value overestimation\n# in actor-critic. Different setting (offline vs online, action\n# sequences vs dt-embedding) but same causal pattern.\n#\n# NO DIRECT COMPETITORS FOUND at CoRL 2025/2026.\n#\n# UPDATED ACTION ITEMS FOR PAPER:\n# 1. MUST CITE: palenicek2025diminishing — rollout horizon diminishing\n#    returns support our \"dt=1 is sufficient\" conclusion\n# 2. SHOULD CITE: kim2025deas — independent evidence of temporal\n#    extension → value overestimation in actor-critic\n# 3. CONSIDER: luo2025vpl — adaptive pessimism as potential mitigation\n",
    "structuredPatch": [
      {
        "oldStart": 893,
        "oldLines": 7,
        "newStart": 893,
        "newLines": 7,
        "lines": [
          " ",
          " - paper_id: luo2025vpl",
          "   title: \"A Case for Validation Buffer in Pessimistic Actor-Critic\"",
          "-  authors: [Luo F., et al.]",
          "+  authors: [Nauman M., Ostaszewski M., Cygan M.]",
          "   year: 2025",
          "   venue: \"IJCAI 2025 (arXiv:2403.01014)\"",
          "   category: method-component"
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

_source line 25_

Now let me check if the `_project/paper/related_work_draft.md` copy also needs the same fix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "452f9ad6-a52d-410c-9c58-78b7cac289e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9xzoSKaq6qLzqKmsCEC66",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 44096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 656
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

_source line 26_

<details open><summary>🔧 Tool call — Grep · `toolu_01BHr3G4x27ECuGRka4wS4Kt`</summary>

```json
{
  "pattern": "TAWM is built on TD-MPC2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "6a8f5f90-5aea-4963-84e6-77912c1717f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9xzoSKaq6qLzqKmsCEC66",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 656,
      "cache_read_input_tokens": 44096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 656
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

_source line 27 · 2026-05-15T06:23:23.424Z_

<details><summary>↩ Tool result · `toolu_01BHr3G4x27ECuGRka4wS4Kt`</summary>

```text
Found 1 file
artifacts/_project/paper/reference_audit_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "83624b29-de3d-4070-81c3-4a8216095c27",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/_project/paper/reference_audit_report.md"
    ],
    "numFiles": 1
  }
}
```

</details>

---

### Assistant

_source line 28_

`_project/paper/related_work_draft.md` 不含该文本，无需改动。`reference_audit_report.md` 只是审计日志，不修改。

两处修正完成：

**Fix 1: `artifacts/related_work_draft.md` 第19行**
- 修改前: `TAWM is built on TD-MPC2's short-horizon MPC framework`
- 修改后: `TAWM is evaluated on TD-MPC2's short-horizon MPC framework`

**Fix 2: `literature_map.yaml` luo2025vpl 条目**
- 修改前: `authors: [Luo F., et al.]`
- 修改后: `authors: [Nauman M., Ostaszewski M., Cygan M.]`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "uuid": "2c001923-f6fc-4d0b-afb6-070efa5566a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T9KWAJAW4UUp7vCBhWt93X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 197,
      "cache_read_input_tokens": 44752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 197
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

_source line 29_

`_project/paper/related_work_draft.md` 不含该文本，无需改动。`reference_audit_report.md` 只是审计日志，不修改。

两处修正完成：

**Fix 1: `artifacts/related_work_draft.md` 第19行**
- 修改前: `TAWM is built on TD-MPC2's short-horizon MPC framework`
- 修改后: `TAWM is evaluated on TD-MPC2's short-horizon MPC framework`

**Fix 2: `literature_map.yaml` luo2025vpl 条目**
- 修改前: `authors: [Luo F., et al.]`
- 修改后: `authors: [Nauman M., Ostaszewski M., Cygan M.]`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 37703,
  "duration_api_ms": 38179,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "01bfe605-792e-4241-9918-d9ddaebbe7ad",
  "total_cost_usd": 0.38051650000000004,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 33108,
    "cache_read_input_tokens": 252491,
    "output_tokens": 1846,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 33108,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 207,
        "cache_read_input_tokens": 44752,
        "cache_creation_input_tokens": 197,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 197
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1066,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0011510000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 1846,
      "cacheReadInputTokens": 252491,
      "cacheCreationInputTokens": 33108,
      "webSearchRequests": 0,
      "costUSD": 0.3793655,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "91081387-0336-4af9-8a65-f89fa7398e93"
}
```

</details>

---
