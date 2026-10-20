# Research conversation: You are doing citation verification for a research paper. Your job has TWO parts: PART 1: Verify each bib entry exists a

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 117
- **Recorded user turns:** 1
- **Tool calls:** 52
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac7763ed9e49a33d3.jsonl`
- **Structured JSON:** [`e1235e5fcdcb06e40d3d.json`](../../sessions/e1/e1235e5fcdcb06e40d3d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

117 recorded events

### User

_source line 1 · 2026-05-26T10:49:27.787Z_

You are doing citation verification for a research paper. Your job has TWO parts:

PART 1: Verify each bib entry exists and has correct metadata.
Read the bib file at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib

Use WebSearch to verify every entry. Focus especially on:
- Papers from 2025-2026 (higher risk of errors)
- Entries with "and others" in author field (may have wrong/incomplete author lists)
- arXiv preprints that may have been published at conferences since

PART 2: Check citation CONTEXT accuracy.
Read all the .tex files that cite these references:
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex
- /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex

For each citation in context, check: does the claim attributed to the cited paper actually match what that paper says? For example, if the text says "X showed that Y [cite]", verify that X actually showed Y.

Output format for each entry:
- BIB STATUS: ✅/⚠️/❌ with details
- CONTEXT STATUS: ✅/⚠️/❌ with details about how it's cited and whether the attribution is accurate

Provide a final summary with counts and a list of all issues found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "20e1d5d0-c716-4a07-a51b-c0ff31a3a5bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-26T10:49:27.793Z_

```json
{
  "parentUuid": "20e1d5d0-c716-4a07-a51b-c0ff31a3a5bb",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__add_constraint",
      "mcp__agent-ml-research__approve_experiment",
      "mcp__agent-ml-research__approve_secret_request",
      "mcp__agent-ml-research__archive_project",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_agent_queue_item",
      "mcp__agent-ml-research__cancel_pending_director_messages",
      "mcp__agent-ml-research__check_credentials",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__complete_mvp",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__create_project",
      "mcp__agent-ml-research__delete_secret",
      "mcp__agent-ml-research__director_allocate_gpus",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_main_agent",
      "mcp__agent-ml-research__director_post_to_manager",
      "mcp__agent-ml-research__director_post_to_paper_agent",
      "mcp__agent-ml-research__director_reply_to_user",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__dream_simulate",
      "mcp__agent-ml-research__feishu_read_chat_history",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__feishu_upload_file",
      "mcp__agent-ml-research__get_agent_queue_status",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_dream_status",
      "mcp__agent-ml-research__get_dream_trend",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_project_status",
      "mcp__agent-ml-research__get_resource_inventory",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__keepalive_respond",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_projects",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_secrets",
      "mcp__agent-ml-research__list_ssh_hosts",
      "mcp__agent-ml-research__list_workspace_projects",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__log_decision",
      "mcp__agent-ml-research__log_mistake",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__post_to_reviewer",
      "mcp__agent-ml-research__ralph_respond",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_server",
      "mcp__agent-ml-research__reject_experiment",
      "mcp__agent-ml-research__reject_secret_request",
      "mcp__agent-ml-research__remove_constraint",
      "mcp__agent-ml-research__remove_server",
      "mcp__agent-ml-research__replace_agent_queue",
      "mcp__agent-ml-research__request_study_approval",
      "mcp__agent-ml-research__research_director_post_to_study_director",
      "mcp__agent-ml-research__should_skip_dream",
      "mcp__agent-ml-research__store_secret",
      "mcp__agent-ml-research__submit_paper_to_review",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_project_config",
      "mcp__agent-ml-research__update_review_issues",
      "mcp__agent-ml-research__update_roadmap",
      "mcp__agent-ml-research__update_skill",
      "mcp__agent-ml-research__upgrade_to_dual_group",
      "mcp__agent-ml-research__urgent_agent_message"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__add_constraint",
      "mcp__agent-ml-research__approve_experiment",
      "mcp__agent-ml-research__approve_secret_request",
      "mcp__agent-ml-research__archive_project",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_agent_queue_item",
      "mcp__agent-ml-research__cancel_pending_director_messages",
      "mcp__agent-ml-research__check_credentials",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__complete_mvp",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__create_project",
      "mcp__agent-ml-research__delete_secret",
      "mcp__agent-ml-research__director_allocate_gpus",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_main_agent",
      "mcp__agent-ml-research__director_post_to_manager",
      "mcp__agent-ml-research__director_post_to_paper_agent",
      "mcp__agent-ml-research__director_reply_to_user",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__dream_simulate",
      "mcp__agent-ml-research__feishu_read_chat_history",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__feishu_upload_file",
      "mcp__agent-ml-research__get_agent_queue_status",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_dream_status",
      "mcp__agent-ml-research__get_dream_trend",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_project_status",
      "mcp__agent-ml-research__get_resource_inventory",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__keepalive_respond",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_projects",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_secrets",
      "mcp__agent-ml-research__list_ssh_hosts",
      "mcp__agent-ml-research__list_workspace_projects",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__log_decision",
      "mcp__agent-ml-research__log_mistake",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__post_to_reviewer",
      "mcp__agent-ml-research__ralph_respond",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_server",
      "mcp__agent-ml-research__reject_experiment",
      "mcp__agent-ml-research__reject_secret_request",
      "mcp__agent-ml-research__remove_constraint",
      "mcp__agent-ml-research__remove_server",
      "mcp__agent-ml-research__replace_agent_queue",
      "mcp__agent-ml-research__request_study_approval",
      "mcp__agent-ml-research__research_director_post_to_study_director",
      "mcp__agent-ml-research__should_skip_dream",
      "mcp__agent-ml-research__store_secret",
      "mcp__agent-ml-research__submit_paper_to_review",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_project_config",
      "mcp__agent-ml-research__update_review_issues",
      "mcp__agent-ml-research__update_roadmap",
      "mcp__agent-ml-research__update_skill",
      "mcp__agent-ml-research__upgrade_to_dual_group",
      "mcp__agent-ml-research__urgent_agent_message"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "bd6126c9-04cb-450b-afb2-ffd379e7d02d",
  "timestamp": "2026-05-26T10:49:27.793Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

---

### Assistant

_source line 3 · 2026-05-26T10:49:30.357Z_



I'll start by reading the bib file and all tex files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd6126c9-04cb-450b-afb2-ffd379e7d02d",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3sQkx96uuj2HrWNHYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "effac969-1c8f-48ad-8186-2925fbc42f7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBFVDuYPzobGeDBcB4St3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25197,
      "cache_read_input_tokens": 8259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25197,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 4 · 2026-05-26T10:49:30.886Z_

<details open><summary>🔧 Tool call — Read · `toolu_017FvVhWTBiPeipzpKPg6xhW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "effac969-1c8f-48ad-8186-2925fbc42f7c",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3sQkx96uuj2HrWNHYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "24c427e1-b6e3-404b-8841-b8580bd38a05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBFVDuYPzobGeDBcB4St3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25197,
      "cache_read_input_tokens": 8259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25197,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 5 · 2026-05-26T10:49:30.896Z_

<details><summary>↩ Tool result · `toolu_017FvVhWTBiPeipzpKPg6xhW`</summary>

```text
1	% ============================================================
2	% GAME THEORY / ATTRIBUTION
3	% ============================================================
4	
5	@incollection{shapley1953value,
6	  title     = {A Value for $n$-Person Games},
7	  author    = {Shapley, Lloyd S.},
8	  booktitle = {Contributions to the Theory of Games II},
9	  editor    = {Kuhn, Harold W. and Tucker, Albert W.},
10	  pages     = {307--317},
11	  year      = {1953},
12	  publisher = {Princeton University Press},
13	}
14	
15	% ============================================================
16	% CORE MODEL COLLAPSE
17	% ============================================================
18	
19	@article{shumailov2024curse,
20	  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},
21	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},
22	  journal   = {Nature},
23	  year      = {2024},
24	  url       = {https://arxiv.org/abs/2305.17493},
25	}
26	
27	@inproceedings{alemohammad2024mad,
28	  title     = {Self-Consuming Generative Models Go {MAD}},
29	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},
30	  booktitle = {International Conference on Learning Representations},
31	  year      = {2024},
32	  url       = {https://arxiv.org/abs/2307.01850},
33	}
34	
35	@inproceedings{dohmatob2024tale,
36	  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},
37	  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},
38	  booktitle = {International Conference on Machine Learning},
39	  year      = {2024},
40	  url       = {https://arxiv.org/abs/2402.07043},
41	}
42	
43	@inproceedings{dohmatob2025strong,
44	  title     = {Strong Model Collapse},
45	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
46	  booktitle = {International Conference on Learning Representations},
47	  year      = {2025},
48	  url       = {https://arxiv.org/abs/2410.04840},
49	}
50	
51	@article{du2026geometric,
52	  title     = {Escaping Mode Collapse in {LLM} Generation via Geometric Regulation},
53	  author    = {Du, Xin and Tanaka-Ishii, Kumiko},
54	  journal   = {arXiv preprint arXiv:2605.00435},
55	  year      = {2026},
56	  url       = {https://arxiv.org/abs/2605.00435},
57	}
58	
59	% ============================================================
60	% CANARY / EARLY WARNING METRICS
61	% ============================================================
62	
63	@article{du2025scales,
64	  title     = {Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios},
65	  author    = {Du, Y. and Wu, G. and Tang, G. and Wang, W. and Fan, Q.},
66	  journal   = {arXiv preprint arXiv:2510.05133},
67	  year      = {2025},
68	  url       = {https://arxiv.org/abs/2510.05133},
69	}
70	
71	@article{gambetta2024surplexity,
72	  title     = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},
73	  author    = {Gambetta, Daniele and others},
74	  journal   = {arXiv preprint arXiv:2410.12341},
75	  year      = {2024},
76	  url       = {https://arxiv.org/abs/2410.12341},
77	}
78	
79	
80	@article{sigma2026spectral,
81	  title     = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},
82	  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},
83	  journal   = {arXiv preprint arXiv:2601.03385},
84	  year      = {2026},
85	  url       = {https://arxiv.org/abs/2601.03385},
86	}
87	
88	
89	
90	% ============================================================
91	% DIVERSITY METRICS (BACKGROUND)
92	% ============================================================
93	
94	@inproceedings{li2016diversity,
95	  title     = {A Diversity-Promoting Objective Function for Neural Conversation Models},
96	  author    = {Li, Jiwei and others},
97	  booktitle = {North American Chapter of the Association for Computational Linguistics},
98	  year      = {2016},
99	  url       = {https://arxiv.org/abs/1510.03055},
100	}
101	
102	% ============================================================
103	% DATA MIXING & ACCUMULATION
104	% ============================================================
105	
106	@inproceedings{kazdan2025collapse,
107	  title     = {Collapse or Thrive? {P}erils and Promises of Synthetic Data in a Self-Generating World},
108	  author    = {Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi},
109	  booktitle = {International Conference on Machine Learning},
110	  year      = {2025},
111	  url       = {https://arxiv.org/abs/2410.16713},
112	}
113	
114	@inproceedings{dey2024breaking,
115	  title     = {Is Model Collapse Inevitable? {B}reaking the Curse of Recursion by Accumulating Real and Synthetic Data},
116	  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
117	  booktitle = {International Conference on Machine Learning},
118	  year      = {2024},
119	  url       = {https://arxiv.org/abs/2404.01413},
120	}
121	
122	% ============================================================
123	% MITIGATION & VERIFICATION
124	% ============================================================
125	
126	@article{dces2026counter,
127	  title     = {Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling},
128	  author    = {Zhu, Bingze and Xie, Yubo},
129	  journal   = {Electronics},
130	  year      = {2026},
131	  url       = {https://www.mdpi.com/2079-9292/15/4/869},
132	}
133	
134	@article{drayson2025detection,
135	  title     = {Machine-generated text detection prevents language model collapse},
136	  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
137	  journal   = {arXiv preprint arXiv:2502.15654},
138	  year      = {2025},
139	  url       = {https://arxiv.org/abs/2502.15654},
140	}
141	
142	% ============================================================
143	% POSITION / SURVEY / EPISTEMICS / ANALYTICAL ROBUSTNESS
144	% ============================================================
145	
146	@inproceedings{bell2022modeling,
147	  title     = {Modeling the Machine Learning Multiverse},
148	  author    = {Bell, Samuel J. and Kampman, Onno P. and Dodge, Jesse and Lawrence, Neil D.},
149	  booktitle = {Advances in Neural Information Processing Systems},
150	  year      = {2022},
151	  url       = {https://arxiv.org/abs/2206.05985},
152	}
153	
154	@article{kapoor2024reforms,
155	  title     = {{REFORMS}: Consensus-based Recommendations for Machine-learning-based Science},
156	  author    = {Kapoor, Sayash and Cantrell, Emily and Peng, Kenny and Pham, Thanh Hien and Bail, Christopher A. and Gundersen, Odd Erik and Hofman, Jake M. and Hullman, Jessica and Lones, Michael A. and Malik, Momin M. and Nanayakkara, Priyanka and Poldrack, Russell A. and Raji, Inioluwa Deborah and Roberts, Michael and Salganik, Matthew J. and Serra-Garcia, Marta and Stewart, Brandon M. and Vandewiele, Gilles and Narayanan, Arvind},
157	  journal   = {Science Advances},
158	  volume    = {10},
159	  number    = {18},
160	  pages     = {eadk3452},
161	  year      = {2024},
162	  doi       = {10.1126/sciadv.adk3452},
163	}
164	
165	@article{coretta2023multidimensional,
166	  title     = {Multidimensional Signals and Analytic Flexibility: Estimating Degrees of Freedom in Human-Speech Analyses},
167	  author    = {Coretta, Stefano and Casillas, Joseph V. and Roessig, Simon and Franke, Michael and others},
168	  journal   = {Advances in Methods and Practices in Psychological Science},
169	  volume    = {6},
170	  number    = {3},
171	  year      = {2023},
172	  doi       = {10.1177/25152459231162567},
173	}
174	
175	@article{simonsohn2020specification,
176	  title     = {Specification curve analysis},
177	  author    = {Simonsohn, Uri and Simmons, Joseph P. and Nelson, Leif D.},
178	  journal   = {Nature Human Behaviour},
179	  volume    = {4},
180	  number    = {11},
181	  pages     = {1208--1214},
182	  year      = {2020},
183	  doi       = {10.1038/s41562-020-0912-z},
184	}
185	
186	@article{steegen2016increasing,
187	  title     = {Increasing Transparency Through a Multiverse Analysis},
188	  author    = {Steegen, Sara and Tuerlinckx, Francis and Gelman, Andrew and Vanpaemel, Wolf},
189	  journal   = {Perspectives on Psychological Science},
190	  volume    = {11},
191	  number    = {5},
192	  pages     = {702--712},
193	  year      = {2016},
194	  doi       = {10.1177/1745691616658637},
195	}
196	
197	@article{silberzahn2018many,
198	  title     = {Many Analysts, One Data Set: Making Transparent How Variations in Analytic Choices Affect Results},
199	  author    = {Silberzahn, Raphael and Uhlmann, Eric L. and Martin, Daniel P. and Anselmi, Pasquale and Aust, Frederik and Awtrey, Eli and Bahn\'{i}k, \v{S}t\v{e}p\'{a}n and Bai, Feng and Bannard, Colin and Bonnier, Evelina and others},
200	  journal   = {Advances in Methods and Practices in Psychological Science},
201	  volume    = {1},
202	  number    = {3},
203	  pages     = {337--356},
204	  year      = {2018},
205	  doi       = {10.1177/2515245917747646},
206	}
207	
208	@inproceedings{kirchenbauer2023watermark,
209	  title     = {A Watermark for Large Language Models},
210	  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
211	  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
212	  pages     = {17061--17084},
213	  year      = {2023},
214	}
215	
216	@article{runge2019detecting,
217	  title     = {Detecting and quantifying causal associations in large nonlinear time series datasets},
218	  author    = {Runge, Jakob and Nowack, Peer and Kretschmer, Marlene and Flaxman, Seth and Sejdinovic, Dino},
219	  journal   = {Science Advances},
220	  volume    = {5},
221	  number    = {11},
222	  pages     = {eaau4996},
223	  year      = {2019},
224	  doi       = {10.1126/sciadv.aau4996},
225	}
226	
227	@article{schaeffer2025position,
228	  title     = {Position: Model Collapse Does Not Mean What You Think},
229	  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},
230	  journal   = {arXiv preprint arXiv:2503.03150},
231	  year      = {2025},
232	  url       = {https://arxiv.org/abs/2503.03150},
233	}
234	
235	% ============================================================
236	% METHODOLOGY (GRANGER / LEAD-LAG)
237	% ============================================================
238	
239	@article{granger1969investigating,
240	  author    = {Granger, Clive W. J.},
241	  title     = {Investigating Causal Relations by Econometric Models and Cross-spectral Methods},
242	  journal   = {Econometrica},
243	  volume    = {37},
244	  number    = {3},
245	  pages     = {424--438},
246	  year      = {1969},
247	  publisher = {Wiley},
248	}
249	
250	@article{shojaie2022granger,
251	  title     = {{Granger} Causality: A Review and Recent Advances},
252	  author    = {Shojaie, Ali and Fox, Emily B.},
253	  journal   = {Annual Review of Statistics and Its Application},
254	  year      = {2022},
255	  url       = {https://arxiv.org/abs/2105.02675},
256	}
257	
258	@article{tank2021neural,
259	  title     = {Neural {Granger} Causality},
260	  author    = {Tank, Alex and Covert, Ian and Foti, Nicholas and Shojaie, Ali and Fox, Emily B.},
261	  journal   = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
262	  volume    = {44},
263	  number    = {8},
264	  pages     = {4267--4279},
265	  year      = {2021},
266	  doi       = {10.1109/TPAMI.2021.3065601},
267	}
268	
269	@article{granger1974spurious,
270	  title     = {Spurious Regressions in Econometrics},
271	  author    = {Granger, Clive W. J. and Newbold, Paul},
272	  journal   = {Journal of Econometrics},
273	  volume    = {2},
274	  number    = {2},
275	  pages     = {111--120},
276	  year      = {1974},
277	  doi       = {10.1016/0304-4076(74)90034-7},
278	}
279	
280	@article{toda1995statistical,
281	  title     = {Statistical Inference in Vector Autoregressions with Possibly Integrated Processes},
282	  author    = {Toda, Hiro Y. and Yamamoto, Taku},
283	  journal   = {Journal of Econometrics},
284	  volume    = {66},
285	  number    = {1--2},
286	  pages     = {225--250},
287	  year      = {1995},
288	  doi       = {10.1016/0304-4076(94)01616-8},
289	}
290	
291	@article{schreiber2000measuring,
292	  title     = {Measuring Information Transfer},
293	  author    = {Schreiber, Thomas},
294	  journal   = {Physical Review Letters},
295	  volume    = {85},
296	  number    = {2},
297	  pages     = {461--464},
298	  year      = {2000},
299	}
300	
301	@article{staniek2008symbolic,
302	  title     = {Symbolic Transfer Entropy},
303	  author    = {Staniek, Matthäus and Lehnertz, Klaus},
304	  journal   = {Physical Review Letters},
305	  volume    = {100},
306	  number    = {15},
307	  pages     = {158101},
308	  year      = {2008},
309	}
310	
311	@inproceedings{pillutla2021mauve,
312	  title     = {{MAUVE}: Measuring the Gap Between Neural Text and Human Text using Divergence Frontiers},
313	  author    = {Pillutla, Krishna and Swayamdipta, Swabha and Zellers, Rowan and Thickstun, John and Welleck, Sean and Choi, Yejin and Harchaoui, Zaid},
314	  booktitle = {Advances in Neural Information Processing Systems},
315	  volume    = {34},
316	  year      = {2021},
317	}
318	
319	@inproceedings{naeini2015obtaining,
320	  title     = {Obtaining Well Calibrated Probabilities Using {B}ayesian Binning into Quantiles},
321	  author    = {Naeini, Mahdi Pakdaman and Cooper, Gregory F. and Hauskrecht, Milos},
322	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
323	  volume    = {29},
324	  pages     = {2901--2907},
325	  year      = {2015},
326	}
327	
328	% ============================================================
329	% EARLY WARNING SIGNALS / TIPPING POINTS (ECOLOGICAL THEORY)
330	% ============================================================
331	
332	@article{scheffer2009early,
333	  title     = {Early-warning signals for critical transitions},
334	  author    = {Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George},
335	  journal   = {Nature},
336	  year      = {2009},
337	  doi       = {10.1038/nature08227},
338	}
339	
340	@article{scheffer2012anticipating,
341	  title     = {Anticipating Critical Transitions},
342	  author    = {Scheffer, Marten and Carpenter, Stephen R. and Lenton, Timothy M. and Bascompte, Jordi and Brock, William and Dakos, Vasilis and van de Koppel, Johan and van de Leemput, Ingrid A. and Levin, Simon A. and van Nes, Egbert H. and Pascual, Mercedes and Vandermeer, John},
343	  journal   = {Science},
344	  volume    = {338},
345	  number    = {6105},
346	  pages     = {344--348},
347	  year      = {2012},
348	  doi       = {10.1126/science.1225244},
349	}
350	
351	
352	@article{boettiger2012limits,
353	  title     = {Quantifying Limits to Detection of Early Warning for Critical Transitions},
354	  author    = {Boettiger, Carl and Hastings, Alan},
355	  journal   = {Journal of the Royal Society Interface},
356	  year      = {2012},
357	  doi       = {10.1098/rsif.2012.0125},
358	}
359	
360	@inproceedings{gu2024cmr,
361	  title     = {{CMR} Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models},
362	  author    = {Gu, Jiawei and Yang, Zacc and Ding, Chuanghao and Zhao, Rui and Tan, Fei},
363	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
364	  year      = {2024},
365	  url       = {https://arxiv.org/abs/2407.17467},
366	}
367	
368	@inproceedings{gu2025datamixing,
369	  title     = {Data Mixing Can Induce Phase Transitions in Knowledge Acquisition},
370	  author    = {Gu, Xinran and Liang, Hayden and Pehlevan, Cengiz},
371	  booktitle = {Advances in Neural Information Processing Systems},
372	  year      = {2025},
373	  note      = {Spotlight},
374	  url       = {https://arxiv.org/abs/2505.18091},
375	}
376	
377	% ============================================================
378	% MODELS
379	% ============================================================
380	
381	@inproceedings{biderman2023pythia,
382	  title     = {Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling},
383	  author    = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purber, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar},
384	  booktitle = {International Conference on Machine Learning},
385	  year      = {2023},
386	  url       = {https://arxiv.org/abs/2304.01373},
387	}
388	
389	% ============================================================
390	% DATASETS
391	% ============================================================
392	
393	@inproceedings{merity2017pointer,
394	  title     = {Pointer Sentinel Mixture Models},
395	  author    = {Merity, Stephen and Xiong, Caiming and Bradbury, James and Socher, Richard},
396	  booktitle = {International Conference on Learning Representations},
397	  year      = {2017},
398	  url       = {https://arxiv.org/abs/1609.07843},
399	}
400	
401	% ============================================================
402	% STATISTICAL METHODOLOGY
403	% ============================================================
404	
405	@article{page1954continuous,
406	  title     = {Continuous Inspection Schemes},
407	  author    = {Page, E. S.},
408	  journal   = {Biometrika},
409	  volume    = {41},
410	  number    = {1--2},
411	  pages     = {100--115},
412	  year      = {1954},
413	  doi       = {10.1093/biomet/41.1-2.100},
414	}
415	
416	@article{phipson2010permutation,
417	  title     = {Permutation P-values Should Never Be Zero: Calculating Exact P-values When Permutations Are Randomly Drawn},
418	  author    = {Phipson, Belinda and Smyth, Gordon K.},
419	  journal   = {Statistical Applications in Genetics and Molecular Biology},
420	  volume    = {9},
421	  number    = {1},
422	  pages     = {Article 39},
423	  year      = {2010},
424	  doi       = {10.2202/1544-6115.1585},
425	}
426	
427	@article{truong2026phase,
428	  title     = {Entropy Collapse: A Universal Failure Mode of Intelligent Systems},
429	  author    = {Truong, Xuan Khanh and Truong, Quynh Hoa},
430	  journal   = {arXiv preprint arXiv:2512.12381},
431	  year      = {2025},
432	}
433	
434	@article{benjamini1995controlling,
435	  title     = {Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing},
436	  author    = {Benjamini, Yoav and Hochberg, Yosef},
437	  journal   = {Journal of the Royal Statistical Society: Series B (Methodological)},
438	  volume    = {57},
439	  number    = {1},
440	  pages     = {289--300},
441	  year      = {1995},
442	  doi       = {10.1111/j.2517-6161.1995.tb02031.x},
443	}
444	
445	@article{benjamini2001control,
446	  title     = {The Control of the False Discovery Rate in Multiple Testing under Dependency},
447	  author    = {Benjamini, Yoav and Yekutieli, Daniel},
448	  journal   = {Annals of Statistics},
449	  volume    = {29},
450	  number    = {4},
451	  pages     = {1165--1188},
452	  year      = {2001},
453	}
454	
455	@inproceedings{shi2025closer,
456	  title     = {A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
457	  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
458	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
459	  year      = {2025},
460	  note      = {Spotlight. arXiv:2509.16499},
461	  url       = {https://arxiv.org/abs/2509.16499},
462	}
463	
464	@inproceedings{hataya2023will,
465	  title     = {Will Large-scale Generative Models Corrupt Future Datasets?},
466	  author    = {Hataya, Ryuichiro and Bao, Han and Arai, Hiromi},
467	  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
468	  pages     = {20555--20565},
469	  year      = {2023},
470	  url       = {https://arxiv.org/abs/2211.08095},
471	}
472	
473	@inproceedings{kovac2025recursive,
474	  title     = {Recursive Training Loops in {LLMs}: How Training Data Properties Modulate Distribution Shift in Generated Data?},
475	  author    = {Kova{\v{c}}, Grgur and Perez, J{\'e}r{\'e}my and Portelas, R{\'e}my and Dominey, Peter Ford and Oudeyer, Pierre-Yves},
476	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
477	  year      = {2025},
478	  note      = {Oral. arXiv:2504.03814},
479	  url       = {https://arxiv.org/abs/2504.03814},
480	}
481	
482	@article{buffa2026entropy,
483	  title     = {Entropy Sentinel: Continuous {LLM} Accuracy Monitoring from Decoding Entropy Traces in {STEM}},
484	  author    = {Buffa, Pedro Memoli and Del Corro, Luciano},
485	  journal   = {arXiv preprint arXiv:2601.09001},
486	  year      = {2026},
487	  url       = {https://arxiv.org/abs/2601.09001},
488	}
489	
490	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24c427e1-b6e3-404b-8841-b8580bd38a05",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "a4dd00cc-0fee-4103-bb9e-f0ea14186074",
  "sourceToolAssistantUUID": "24c427e1-b6e3-404b-8841-b8580bd38a05",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T10:49:31.395Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hc96CSZ3cxTM5ro6G6C8cQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4dd00cc-0fee-4103-bb9e-f0ea14186074",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3sQkx96uuj2HrWNHYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be75536e-4867-4d0b-810c-4ca2ea2c730f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBFVDuYPzobGeDBcB4St3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25197,
      "cache_read_input_tokens": 8259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25197,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 7 · 2026-05-26T10:49:31.405Z_

<details><summary>↩ Tool result · `toolu_01Hc96CSZ3cxTM5ro6G6C8cQ`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\citep{shumailov2024curse,alemohammad2024mad}.
5	This process can be triggered by vanishingly small synthetic fractions~\citep{dohmatob2025strong}: lexical diversity narrows, calibration deteriorates, and each generation inherits the biases of its predecessors.
6	As machine-generated text grows prevalent on the web, such feedback loops pose a growing risk to production pipelines, and by the time standard quality metrics register degradation, the distribution may have already shifted irreversibly.
7	
8	This threat motivates a fundamental question: \emph{can we reliably detect the onset of model collapse?}
9	The answer is less clear than it might appear.
10	Iterative training produces short, noisy time series (often fewer than 15 points) where detection power drops sharply~\citep{boettiger2012limits}, and model collapse is a first-order transition~\citep{truong2026phase}, structurally ruling out the critical-slowing-down early-warning signals that ecologists rely on~\citep{scheffer2009early} (\S\ref{sec:related_work}).
11	More fundamentally, no prior work has systematically compared detection methods on this problem; as we show, the choice of statistical test alone can shift conclusions from universal detection to complete null on identical data.
12	Detection is effective only above a critical contamination level $\alpha_c \approx 0.50$; substantial quality degradation (e.g., ${\sim}40\%$ decline in lexical diversity) occurs undetected below this threshold, making the framework a confirmation tool for ongoing collapse rather than an early-warning system.
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=\columnwidth]{figures/fig_phase_diagram.pdf}
17	\caption{Phase diagram (Pythia-410M, fp32, PermG). Cells show the fraction of FDR-significant canary$\to$diversity pairs (out of 8) across $\alpha$ and $T$; dashed curve: fitted boundary (Eq.~\ref{eq:alpha-c}); $\diamond$: non-monotonic anomaly; $\star$: dissolution at $T{=}25$.}
18	\label{fig:phase_diagram}
19	\end{figure}
20	
21	We systematically map this \emph{detectability landscape}, examining how detection outcomes vary across contamination levels ($\alpha$), observation windows ($T$), and statistical methods, on Pythia-410M~\citep{biderman2023pythia} across 13 contamination levels with multi-seed replication (Figure~\ref{fig:phase_diagram}).
22	We test whether fast-responding \emph{canary} metrics (token entropy, calibration error) temporally precede slower \emph{downstream} quality measures (lexical diversity, perplexity).
23	Our central finding is a steep detection onset: Permutation Granger causality (PermG) finds 0/8 significant canary$\to$downstream pairs through $\alpha{=}0.45$, then jumps to 6/8 (95\% CI $[0.25, 0.92]$) within a 2-percentage-point interval at $\alpha{=}0.50$ (Figure~\ref{fig:phase_diagram}), defining an empirical detection boundary $\alpha_c(T)$ (\S\ref{sec:theory}) that organizes three confirmed regimes (blind, onset, detection) plus one non-monotonic anomaly.
24	This transition emerges from a five-method comparison that itself reveals dramatic method sensitivity: null-control FPR spans 6.7\% to 94.4\% (Fleiss' $\kappa{=}0.187$; Figure~\ref{fig:method_comparison}), demonstrating that single-method analyses cannot reliably distinguish real signals from artifacts.
25	Cross-architecture evaluation at $\alpha{=}1.0$ across five families (345M--6.9B) supports forward detection in 11/15 conditions, with four non-confirming cases isolating distinct failure modes (\S\ref{sec:generalization}).
26	Our canary claim is scoped to diversity metrics (distinct-$n$~\citep{li2016diversity}); Granger precedence establishes temporal predictive improvement, not causation (\S\ref{sec:method}).
27	
28	Our contributions are:
29	\begin{enumerate}
30	    \item \textbf{We characterize a steep detection onset} (\S\ref{sec:regime}--\ref{sec:dose_response}).
31	    Detection jumps from 0/8 to 6/8 significant pairs (95\% CI $[0.25, 0.92]$) within 2 percentage points of $\alpha_c \approx 0.50$, defining three confirmed regimes (blind, onset, detection) plus a non-monotonic anomaly at $\alpha \approx 0.60$.
32	
33	    \item \textbf{We map the detectability landscape} across contamination levels and observation windows (\S\ref{sec:t20}--\ref{sec:theory}).
34	    The detection boundary shifts leftward with longer observation, organizing the signal$\times$resolution tradeoff that governs detection feasibility.
35	
36	    \item \textbf{A multi-method diagnostic toolkit supports reproducible analysis} (\S\ref{sec:mmct}).
37	    Five methods yield null-control FPR from 6.7\% to 94.4\% ($\kappa{=}0.187$); systematic comparison identifies PermG (6.7\%, CI $[1.8\%, 16.2\%]$, 10~seeds) as the primary detector and exposes method sensitivity as a key obstacle.
38	
39	    \item \textbf{We demonstrate practical applications}: a cascade ordering where entropy precedes diversity by ${\geq}1$ generation (Observations~\ref{thm:entropy_leads}--\ref{prop:div_lag}; 14/15 experiments) enables proof-of-concept predictive intervention reducing peak perplexity by 64\% at $\alpha{=}1.0$ (\S\ref{sec:cascade}, \S\ref{sec:intervention}).
40	\end{enumerate}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be75536e-4867-4d0b-810c-4ca2ea2c730f",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "734cc466-cd0b-42ee-bc13-7372a6e8a99d",
  "sourceToolAssistantUUID": "be75536e-4867-4d0b-810c-4ca2ea2c730f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T10:49:31.838Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QP7SqidQ9tKCDJaGyMHZpi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "734cc466-cd0b-42ee-bc13-7372a6e8a99d",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3sQkx96uuj2HrWNHYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c23c4698-836c-4ba7-98e1-3dcb563fa5a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBFVDuYPzobGeDBcB4St3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25197,
      "cache_read_input_tokens": 8259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25197,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 9 · 2026-05-26T10:49:31.842Z_

<details><summary>↩ Tool result · `toolu_01QP7SqidQ9tKCDJaGyMHZpi`</summary>

```text
1	
2	\section{Method}
3	\label{sec:method}
4	
5	\subsection{Cascade Ordering}
6	\label{sec:cascade}
7	
8	If distributional collapse follows a predictable ordering across metrics, the earliest-responding metric can serve as a canary signal.
9	We formalize known metric properties (entropy as a continuous indicator of mode concentration, diversity as a threshold indicator of lexical coverage) under mode amplification~\citep{shumailov2024curse,dohmatob2024tale} (notation in Appendix~\ref{app:background}; derivations in Appendix~\ref{app:cascade_theory}).
10	
11	\begin{observation}[Entropy responds before diversity]\label{thm:entropy_leads}
12	Under mode amplification: \textup{(a)} entropy can decrease while the $\epsilon$-effective support $S_\epsilon(p) {=} |\{i: p_i > \epsilon\}|$ (hence distinct-$n$) is unchanged; \textup{(b)} if distinct-$n$ decreases, entropy has already decreased.
13	\end{observation}
14	
15	Intuitively, entropy responds to any redistribution of probability mass (a continuous change), whereas diversity metrics like distinct-$n$ only change when tokens are pushed entirely below the generation threshold (a discrete event).
16	This measurement asymmetry ensures entropy shifts before diversity under gradual mode amplification.
17	The margin $\gamma = \min_{i: p_i > \epsilon}(p_i - \epsilon)$ quantifies how much shift diversity absorbs silently.
18	
19	\begin{observation}[Diversity lag $\geq 1$ generation]\label{prop:div_lag}
20	If the self-training map $\mathcal{T}$ satisfies $\alpha\|\mathcal{T}(p_t) - p_t\|_\infty < \gamma(p_t, \epsilon)$ per generation through entropy onset $t_H$, then diversity onset $t_D \geq t_H + 1$.
21	\end{observation}
22	
23	ECE co-moves with entropy at zero lag ($\Delta\mathrm{ECE} \approx \Delta C > 0$ whenever $\Delta\bar{H} < 0$; Appendix~\ref{app:cascade_theory}), yielding a three-stage cascade $\{H, \mathrm{ECE}\} \to \mathrm{Distinct}$-$n$.
24	This ordering holds in 14/15 experiments at $\alpha \geq 0.30$, with entropy and ECE consistently reaching onset at generation~1 and distinct-$n$ following at generation~2 ($t_H{=}t_{\mathrm{ECE}}{=}1$, $t_D{=}2$; \S\ref{sec:regime}; Appendix~\ref{app:moment_cascade}).
25	The one exception, SmolLM3-3B (3/8 at $\alpha{=}1.0$; Table~\ref{tab:generalization}), shows entropy decoupling from diversity, violating the monotonic-decline assumption that underlies both Observations.
26	The cascade is also specific to diversity metrics: first-differencing eliminates canary$\to$perplexity associations entirely ($F{\approx}0$, $p{=}0.99$; \S\ref{sec:regime}), confirming that the temporal structure is channel-specific rather than global.
27	
28	\subsection{Design Considerations}
29	\label{sec:pitfalls}
30	
31	We use \emph{Granger precedence}, temporal predictive improvement where past values of $X$ improve prediction of $Y$ beyond $Y$'s own history, to assess whether canary metrics anticipate downstream degradation~\citep{granger1969investigating}.
32	This is distinct from Granger causality, which additionally implies a mechanistic causal link that bivariate tests cannot establish~\citep{shojaie2022granger}.
33	Even within this narrower scope, lead-lag analysis in iterative model collapse is fragile along three axes.
34	\emph{Method sensitivity}: five detection methods applied to identical data yield forward significance rates spanning 0\% to 92\%, with $\kappa{=}0.187$ (Figure~\ref{fig:method_comparison}).
35	\emph{Spurious regression}: first-differencing eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24)~\citep{granger1974spurious}.
36	\emph{Regime dependence}: the same Granger test shifts from 0/8 to 6/8 significant pairs within a 2-percentage-point interval.
37	
38	\begin{figure}[t]
39	\centering
40	\includegraphics[width=\columnwidth]{figures/fig_method_comparison.pdf}
41	\caption{Method sensitivity: five methods yield dramatically different FDR-significant rates on identical data. PermG achieves the lowest null-control FPR (6.7\%, pooled across 10~seeds) with 75\% detection at $\alpha{\geq}0.50$; dashed line: 5\% nominal.}
42	\label{fig:method_comparison}
43	\end{figure}
44	
45	\subsection{Method Sensitivity Analysis}
46	\label{sec:mmct}
47	
48	These fragilities motivate a systematic comparison.
49	We evaluate five lead-lag detection methods (naive cross-correlation (NaiveXCorr), differenced cross-correlation (DiffXCorr), threshold onset, permutation Granger causality (PermG), and Toda--Yamamoto~\citep{toda1995statistical}) in a multi-method comparison framework~\citep{simonsohn2020specification}, calibrating each against null-control ($\alpha{=}0.0$) data.
50	Among these, PermG assesses whether past values of a canary metric improve prediction of a downstream metric beyond its own history~\citep{shojaie2022granger}, using 5{,}000 permutations~\citep{phipson2010permutation} on first-differenced series with Benjamini--Hochberg FDR correction ($q{=}0.05$) across 8 canary$\to$downstream pairs; the permutation null controls Type~I error by construction, and BH-FDR remains valid under positive regression dependence~\citep{benjamini2001control}.
51	The full multi-method consensus test (MMCT) is given in Algorithm~\ref{alg:mmct}.
52	
53	\begin{algorithm}[H]
54	\caption{Multi-Method Consensus Test (MMCT)}
55	\label{alg:mmct}
56	\begin{algorithmic}[1]
57	\Require Time series pair $(X, Y)$; methods $\{m_1, \ldots, m_K\}$ ($K{=}5$); null-control data $\mathcal{N}$ (from $\alpha{=}0.0$); tolerance $\epsilon{=}0.01$
58	\Ensure $p$-value, consensus level $\hat{K}$
59	\For{each method $m_k$}
60	    \State Compute empirical FPR: $\widehat{\mathrm{FPR}}_k \gets$ fraction of null-control pairs where $m_k$ rejects $H_0$
61	    \State Compute weight: $w_k \gets 1 / \max(\widehat{\mathrm{FPR}}_k,\; \epsilon)$
62	    \State Apply $m_k$ to $(X, Y)$: $d_k \gets \mathbf{1}[m_k \text{ rejects } H_0]$
63	\EndFor
64	\State Weighted consensus: $W(X {\to} Y) \gets \sum_{k} w_k \, d_k \;/\; \sum_{k} w_k$
65	\State Build empirical null distribution of $W$ from all null-control pairs in $\mathcal{N}$
66	\State Compute $p$-value from empirical null: $p \gets \Pr_{\mathcal{N}}(W \geq W_{\mathrm{obs}})$
67	\State Consensus level: $\hat{K} \gets \sum_{k} d_k$
68	\State \Return $p$, $\hat{K}$
69	\end{algorithmic}
70	\end{algorithm}
71	
72	\begin{figure*}[t]
73	\centering
74	\includegraphics[width=\textwidth]{figures/metric_trajectory.pdf}
75	\caption{Metric trajectories at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead (shaded: inter-seed range).}
76	\label{fig:metric_trajectory}
77	\end{figure*}
78	
79	The algorithm's FPR-inverse weighting assigns each method influence proportional to its null-control reliability: NaiveXCorr (FPR${=}94.4\%$) receives weight $w{=}1.06$, while PermG (FPR${=}6.7\%$) receives $w{=}14.9$, a $14{\times}$ differential that ensures the most reliable method dominates the consensus.
80	Building the null distribution empirically from $\alpha{=}0.0$ data avoids parametric assumptions unreliable for short ($T{=}5$--$20$), non-stationary series.
81	Pooled null-control FPR across ten seeds (60 pairs) confirms a wide methodological spread: PermG 6.7\% (95\% CI $[1.8\%, 16.2\%]$), DiffXCorr 14.8\%, Threshold 24.1\%, Toda--Yamamoto 33.3\%, NaiveXCorr 94.4\% (Appendix~\ref{app:fpr_independence}).
82	PermG (4/60; 95\% CI $[1.8\%, 16.2\%]$) achieves the lowest FPR among all five methods, with 8/10 seeds yielding zero false positives; Shapley analysis confirms it provides the best FPR--FNR tradeoff among directional methods (Appendix~\ref{app:shapley}).
83	Table~\ref{tab:mmct_k_operating} reports an alternative operating mode: equal-weight $K{\geq}3$ majority voting with forward-direction filtering, where FPR is 10.0\% with 75\% TPR at $\alpha{=}1.0$ (consensus heatmap in Appendix~\ref{app:mmct}).
84	The weighted scheme (Algorithm~\ref{alg:mmct}) further downweights unreliable methods via FPR-inverse weighting (robust across four alternative schemes; Appendix~\ref{app:weight_robustness}); majority voting treats all methods equally and is simpler to deploy.
85	
86	
87	
88	\subsection{Detection Boundary}
89	\label{sec:theory}
90	
91	The steep onset described above suggests a detection boundary $\alpha_c(T)$ that decreases with longer observation.
92	We parametrize this boundary as a power law:
93	\begin{equation}
94	\alpha_c(T) = A \cdot T^{-\eta},
95	\label{eq:alpha-c}
96	\end{equation}
97	motivated by an empirical sub-linear signal model $S(\alpha) = c \cdot \alpha^\beta$ ($\beta < 1$), under which the exponent satisfies $\eta = 1/(2\beta)$:
98	\begin{equation}
99	\alpha_c(T) = A \cdot T^{-\eta},
100	\label{eq:alpha-c-theory}
101	\end{equation}
102	where $A = (z^* \sigma / c)^{1/\beta}$ and $z^* = \Phi^{-1}(\pi^*)$ (derivation in Appendix~\ref{app:alpha_c_proof}).
103	This parametrization captures the observed pattern with three free parameters fitted to 3--4 data points; the resulting $\eta$ confidence interval ($[0.64, 2.08]$) is wide enough to preclude distinguishing sub-linear from super-linear decay, but the qualitative conclusion (detection improves with longer observation) is robust regardless.
104	
105	Dense $\alpha$ sampling further reveals that a smooth sigmoid fits better than a step function ($\Delta\mathrm{AIC}{=}-110$), yet the fitted onset steepness ($k{=}15.7$) exceeds smooth-model predictions by ${\sim}3{\times}$ (Appendix~\ref{app:power_sim}), suggesting the transition is sharper than standard power-analysis models would predict.
106	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c23c4698-836c-4ba7-98e1-3dcb563fa5a0",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "33c48cbf-4a1e-4b19-b872-9a9414ac825c",
  "sourceToolAssistantUUID": "c23c4698-836c-4ba7-98e1-3dcb563fa5a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T10:49:32.344Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RSUkjMX4TeVEU6uhgT65jM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33c48cbf-4a1e-4b19-b872-9a9414ac825c",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3sQkx96uuj2HrWNHYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "961bb8ac-e4cf-4086-a041-155a63c19279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBFVDuYPzobGeDBcB4St3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25197,
      "cache_read_input_tokens": 8259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25197,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 11 · 2026-05-26T10:49:32.348Z_

<details><summary>↩ Tool result · `toolu_01RSUkjMX4TeVEU6uhgT65jM`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\subsection{Model Collapse: Theory and Empirical Evidence}
5	\label{sec:rw_collapse}
6	
7	Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}; \citet{schaeffer2025position} systematize eight distinct notions of collapse; our operationalization aligns with their \emph{distributional shift} family (definitions~D4--D6).
8	Theoretical analyses sharpen these results: \citet{dohmatob2024tale} recast collapse as changed scaling-law exponents, \citet{dohmatob2025strong} proved collapse at vanishingly small synthetic fractions, and \citet{truong2026phase} prove entropy collapse is a first-order transition, structurally ruling out critical-slowing-down early-warning signals~\citep{scheffer2009early,scheffer2012anticipating}.
9	Empirically, \citet{hataya2023will} demonstrate that generated images degrade downstream classification on ImageNet-scale data, and \citet{kovac2025recursive} show that training data properties (lexical diversity, semantic diversity) modulate the magnitude of recursive collapse in LLMs.
10	Critical mixture ratios separating qualitative outcomes have independent precedent: \citet{kazdan2025collapse} map collapse conditions, \citet{gu2024cmr} establish scaling laws for critical ratios, and \citet{gu2025datamixing} show data mixing induces phase transitions in knowledge acquisition.
11	
12	\subsection{Detection of Synthetic Data Contamination}
13	\label{sec:rw_detection}
14	
15	Monitoring metrics proposed for collapse include expected calibration error (ECE)~\citep{du2025scales}, surplexity~\citep{gambetta2024surplexity}, and machine-generated text detection~\citep{drayson2025detection}; \citet{shi2025closer} independently validate entropy as a collapse diagnostic in diffusion models; \citet{buffa2026entropy} propose continuous entropy-based monitoring for LLM accuracy, though targeting task performance rather than distributional collapse.
16	A complementary line of work pursues \emph{proactive} contamination prevention via watermarking~\citep{kirchenbauer2023watermark}; our distributional detection framework is \emph{reactive}, identifying collapse from observed metric trajectories without requiring control over the generation process.
17	\citet{boettiger2012limits} establish fundamental power limits for early-warning detection in short time series ($T{<}25$), directly relevant to iterative training where observation windows are typically $T{=}5$--$20$.
18	However, these works evaluate single metrics in isolation without cross-validating against alternative statistical tests.
19	We differ by applying five detection methods to identical data, mapping detectability across contamination regimes, and treating method sensitivity as a primary finding rather than a robustness check (detailed comparison: Appendix~\ref{app:method_comparison}).
20	
21	\subsection{Statistical Methods for Distribution Shift}
22	\label{sec:rw_methods}
23	
24	For temporal precedence testing, Granger causality~\citep{granger1969investigating} is the standard framework, with neural extensions~\citep{tank2021neural,runge2019detecting}; however, non-stationary series inflate rejection rates~\citep{granger1974spurious}, and short series ($T{\leq}25$) preclude reliable nonlinear estimation~\citep{boettiger2012limits}.
25	Granger precedence establishes temporal predictive improvement, not true causation: bivariate tests cannot exclude confounders~\citep{shojaie2022granger}.
26	Our permutation-based approach circumvents the critical-slowing-down limitation by detecting temporal predictive improvement rather than variance or autocorrelation signatures.
27	Specification-curve analysis~\citep{simonsohn2020specification} formalizes the sensitivity of conclusions to analytical choices; we adapt this framework to show that method choice alone shifts detection rates from 0\% to 94\%.
28	The multiverse analysis perspective~\citep{steegen2016increasing,silberzahn2018many,coretta2023multidimensional,kapoor2024reforms} motivates our multi-method comparison: five methods on identical data produce conclusions ranging from universal significance to complete null, instantiating many-analysts divergence at the method level.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "961bb8ac-e4cf-4086-a041-155a63c19279",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "10b1fedd-2d24-4112-a8ab-b4919a921add",
  "sourceToolAssistantUUID": "961bb8ac-e4cf-4086-a041-155a63c19279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T10:49:32.814Z_

<details open><summary>🔧 Tool call — Read · `toolu_019XWPAxprYLrgpxwKD15qev`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10b1fedd-2d24-4112-a8ab-b4919a921add",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3sQkx96uuj2HrWNHYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f225ecc9-a5ec-4776-a195-be839d525e70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBFVDuYPzobGeDBcB4St3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25197,
      "cache_read_input_tokens": 8259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25197,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 13 · 2026-05-26T10:49:32.818Z_

<details><summary>↩ Tool result · `toolu_019XWPAxprYLrgpxwKD15qev`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	Our Granger-precedence claim is scoped to temporal predictive improvement~\citep{granger1969investigating,shojaie2022granger}: bivariate tests cannot exclude confounders, and the FPR CI ($[1.8\%, 16.2\%]$) means Type~I error may be non-negligible.
4	Four of fifteen cross-architecture conditions do not confirm forward detection (\S\ref{sec:generalization}), each isolating a distinct PermG assumption violation: precision sensitivity (GPT-2 bf16), bidirectional confounding (GPT-2 s43), seed dependence (Pythia-1.4B), and entropy decoupling (SmolLM3-3B), requiring architecture-specific null calibration before deployment (Appendix~\ref{app:extended_discussion}).
5	More broadly, our observation sequences ($T{=}10$--$25$) are far shorter than econometric standards ($T{\geq}100$); permutation testing avoids asymptotic assumptions but cannot recover power lost to short samples~\citep{shojaie2022granger}; AR(1) simulation confirms first-differencing controls size at these lengths (Appendix~\ref{app:nonstationarity}).
6	Bivariate tests are susceptible to omitted variable bias (first-differencing removes shared linear trends but nonlinear confounds remain possible), and PermG tests linear precedence only; transfer entropy (Appendix~\ref{app:transfer_entropy}) yields 0/192 significant pairs.
7	Partial correlation provides supporting evidence: after controlling for generation number, contemporaneous associations weaken ($\bar{|r|}$: $0.590{\to}0.381$) while lagged correlations strengthen ($0.759{\to}0.841$), consistent with genuine temporal precedence rather than shared-trend artifacts (Appendix~\ref{app:mi_analysis}).
8	
9	Despite these individual limitations, the five methods exhibit complementary strengths.
10	Shapley value decomposition over all $2^5{=}32$ coalitions (Appendix~\ref{app:shapley}) shows DiffXCorr achieving the best combined Shapley contribution ($-0.299$) by detecting bidirectional coupling that directional methods miss, while PermG ranks best among directional methods ($-0.141$).
11	This complementarity provides analytical value, though consensus voting does not uniformly outperform the best single method: $K{\geq}3$ FPR (10.0\%) exceeds standalone PermG (6.7\%), and practitioners deploying MMCT must calibrate $K$ on architecture-specific null-control data, as the single viable operating point ($K{=}3$) reflects the specific method set and FPR profile of our five-method ensemble.
12	One remaining puzzle is the non-monotonic detection gap at $\alpha{=}0.60$ (\S\ref{sec:dose_response}): consistent across seeds (0/8 for both tested seeds; Appendix~\ref{app:alpha060}), it affects all directional methods while bidirectional DiffXCorr maintains detection, suggesting temporal lag compression defeats directional separation; recovery at $T{=}25$ (5/8) is consistent with $\sqrt{T}$ power scaling.
13	
14	A related concern is whether entropy's ``leading'' behavior partly reflects measurement-resolution asymmetry (entropy is continuous; distinct-$n$ is discrete) rather than genuine temporal precedence.
15	Discretized entropy testing shows that Granger significance is largely recovered at ${\geq}15$~bins (6--7/7 depending on binning method) but degrades under aggressive quantization (0/7 at 5~equal-frequency bins), consistent with measurement resolution contributing to but not solely explaining the temporal precedence signal (Appendix~\ref{app:discretized_entropy}).
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f225ecc9-a5ec-4776-a195-be839d525e70",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "f41d3cfe-f17e-4c7f-a5f3-786e6a4ab2f9",
  "sourceToolAssistantUUID": "f225ecc9-a5ec-4776-a195-be839d525e70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T10:49:33.285Z_

<details open><summary>🔧 Tool call — Read · `toolu_0176MmdjVznkrNAkEM18BMnQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f41d3cfe-f17e-4c7f-a5f3-786e6a4ab2f9",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3sQkx96uuj2HrWNHYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a931b760-1617-42bb-b586-54da3de2d337",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBFVDuYPzobGeDBcB4St3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25197,
      "cache_read_input_tokens": 8259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25197,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 15 · 2026-05-26T10:49:33.289Z_

<details><summary>↩ Tool result · `toolu_0176MmdjVznkrNAkEM18BMnQ`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study iterative training collapse using Pythia-410M~\citep{biderman2023pythia} as the primary architecture.
8	Training data is drawn from WikiText-103~\citep{merity2017pointer} following the replace paradigm of~\citet{shumailov2024curse}: each generation fine-tunes on a mixture of $\alpha$ synthetic and $(1{-}\alpha)$ real data, generates 5{,}000 replacement samples, and fully replaces the synthetic pool (hyperparameters in Appendix~\ref{app:training_details}).
9	We run $T{=}10$ generations across 13 contamination levels ($\alpha \in \{0.00, \ldots, 1.00\}$) with multi-seed replication, yielding ${\sim}1{,}500$ statistical tests after BH-FDR correction~\citep{benjamini1995controlling}.
10	We track two \emph{canary metrics} (token entropy and ECE) and three \emph{downstream metrics}: distinct-1, distinct-2~\citep{li2016diversity}, and perplexity (distinct-3: Appendix~\ref{app:distinct3}).
11	PermG uses 5{,}000 permutations on first-differenced series~\citep{shojaie2022granger} with lag order~1 (power analysis in Appendix~\ref{app:power_analysis}).
12	
13	
14	\subsection{Steep Detection Onset}
15	\label{sec:regime}
16	
17	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ even at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$.
18	Despite this ubiquitous degradation, Granger detectability is strongly regime-dependent.
19	PermG finds 0/8 canary$\to$downstream pairs FDR-significant from $\alpha{=}0.00$ through $\alpha{=}0.45$, then jumps to 6/8 (Clopper--Pearson 95\% CI $[0.25, 0.92]$) at $\alpha{=}0.50$, consistently across all 3~fp32 seeds.
20	
21	This transition is striking because cumulative synthetic fraction barely changes across the boundary ($C{=}99.75\%$ at $\alpha{=}0.45$ vs.\ $99.90\%$ at $\alpha{=}0.50$), yet detection jumps from null to reliable.
22	Sub-threshold $p$-values at $\alpha{=}0.45$ ($p_{\mathrm{fdr}} = 0.059$--$0.091$) confirm proximity to the boundary.
23	Sigmoid regression yields $\alpha_c = 0.483$ (bootstrap 95\% CI $[0.43, 0.56]$; Figure~\ref{fig:dose_response}); cross-seed consistency (3/3 seeds: $0/8{\to}6/8$) and specification-invariance across 288 method-$\alpha$ configurations (Appendix~\ref{app:spec_curve}) argue for a genuine transition (Fisher exact: $p = 3.45 \times 10^{-11}$).
24	
25	First-differencing scopes this canary claim precisely: canary$\to$diversity pairs retain unanimous FDR significance ($24/24 \to 24/24$ across 4~seeds at $\alpha{=}1.0$), while canary$\to$perplexity collapses entirely ($F \approx 0$, $p = 0.99$)~\citep{granger1974spurious}; channel-level effect sizes confirm this dissociation (Appendix~\ref{app:channel_effect_size}).
26	At $\alpha{=}1.0$, all 24 canary$\to$diversity pairs reach FDR significance in the forward direction with 0/24 reverse; entropy onset at generation~1 precedes distinct-$n$ at generation~2 in all 18 WikiText conditions (Appendix~\ref{app:moment_cascade}).
27	Yet despite this clear signal above onset, a substantial blind zone exists below it: at $\alpha{=}0.10$, distinct-1 has already dropped by $39.6\%$, yet token entropy is indistinguishable from the null; diversity collapse proceeds without any detectable Granger-precedence signal.
28	
29	\begin{table}[t]
30	\centering
31	\caption{Detection outcomes across contamination levels (Pythia-410M, seed~42, $T{=}10$, fp32). PermG: forward FDR-significant pairs; $K{\geq}3$: consensus pairs (of 8 canary$\to$downstream pairs).}
32	\label{tab:summary_detection}
33	\begin{tabular}{@{}lccc@{}}
34	\toprule
35	$\alpha$ & PermG & $K{\geq}3$ & Regime \\
36	\midrule
37	0.00 & 0/8 & 0/8 & null \\
38	0.25 & 0/8 & 0/8 & blind \\
39	0.45 & 0/8 & 0/8 & blind \\
40	0.50 & 6/8 & 6/8 & onset \\
41	0.60 & 0/8 & 0/8 & anomaly \\
42	0.75 & 6/8 & 6/8 & detection \\
43	1.00 & 6/8 & 6/8 & detection \\
44	\bottomrule
45	\end{tabular}
46	\end{table}
47	
48	\subsection{Dose-Response and Detection Regimes}
49	\label{sec:dose_response}
50	
51	\begin{figure}[t]
52	\centering
53	\includegraphics[width=\columnwidth]{figures/fig_dose_response.pdf}
54	\caption{Dose-response: PermG detection rate with sigmoid fit ($\alpha_c{=}0.483$; shaded 95\% CI). Regime bands mark blind, onset, sync-dip, and detection zones.}
55	\label{fig:dose_response}
56	\end{figure}
57	
58	The PermG dose-response profile (Figure~\ref{fig:dose_response}; Appendix~\ref{app:dose_response}) reveals three confirmed regimes: \emph{blind} ($\alpha \leq 0.45$, 0/8), \emph{onset} ($\alpha \approx 0.50$, 6/8), and \emph{detection} ($\alpha{\geq}0.75$, 6/8), plus a non-monotonic anomaly at $\alpha \approx 0.60$ (0/8).
59	The blind zone exhibits zero detection across all seeds and methods below $\alpha{=}0.45$, despite substantial diversity loss, a regime where collapse proceeds silently (a perplexity-threshold baseline also fails; Appendix~\ref{app:ppl_threshold}).
60	Onset is remarkably steep: the sigmoid Hill coefficient $k{=}15.7$ (dense 17-point fit; Appendix~\ref{app:sigmoid_shape}) implies that 80\% of the detection transition occurs within $\Delta\alpha{\approx}0.05$, approximately $3{\times}$ steeper than smooth-signal predictions (Appendix~\ref{app:power_sim}).
61	Above onset, the detection zone shows cross-seed consistency: all 3~fp32 seeds independently reach 6/8 at $\alpha{=}0.50$.
62	
63	At $\alpha{\approx}0.60$, all direction-checked methods fail (PermG 0/8, threshold onset 0/8, Toda--Yamamoto 1/8), while bidirectional DiffXCorr maintains detection (6/8).
64	This pattern suggests that at intermediate contamination, entropy and diversity respond near-simultaneously, compressing the temporal lag below PermG's resolution at $T{=}10$.
65	The anomaly dissolves by $T{=}25$ ($5/8$), consistent with $\sqrt{T}$ power scaling restoring directional separation as additional observations accumulate (Appendix~\ref{app:t20_comparison}).
66	
67	\subsection{Detection Boundary Left-Shift}
68	\label{sec:t20}
69	
70	Longer observation windows push the detection boundary leftward: $\alpha_c(5){\geq}1.0$, $\alpha_c(10){=}0.487$, consistent with power-law scaling $\alpha_c(T) \propto T^{-\eta}$ (\S\ref{sec:theory}).
71	Profile likelihood yields $\eta \in [0.64, 2.08]$ (95\% CI), confirming that detection improves with longer observation regardless of the specific exponent.
72	The mechanism is statistical power accumulation: each additional generation provides one more data point for the permutation test, and the signal-to-noise ratio grows as $\sqrt{T}$, progressively resolving weaker contamination signals.
73	The $\alpha{=}0.45$ column validates this prediction directly: undetectable at $T{\leq}10$ (0/8), it crosses into reliable detection at $T{=}15$ (6/8, dual-seed) and remains stable at $T{=}20$ (5/8) and $T{=}25$ (6/8), precisely traversing the blind$\to$detection boundary as the theory predicts.
74	
75	
76	\subsection{Cross-Architecture Evaluation at $\alpha{=}1.0$}
77	\label{sec:generalization}
78	
79	The phase diagram (Figure~\ref{fig:phase_diagram}) characterizes detectability on Pythia-410M + WikiText-103; this section tests whether the detection signal generalizes across architectures at the most favorable contamination level ($\alpha{=}1.0$).
80	We evaluate PermG across 15 model-seed combinations spanning five families (345M--6.9B) and two domains (Table~\ref{tab:generalization}; Appendix~\ref{app:cross_arch_table}).
81	Forward detection reaches ${\geq}6/8$ in 11/15 conditions (Figure~\ref{fig:cross_arch_heatmap}).
82	
83	At larger scale, Pythia-1.4B qualitatively reproduces the 410M phase-diagram structure (detection boundary at $\alpha_c{\approx}0.50$, cross-$T$ improvement at 3/4 $\alpha$ values ($\alpha{=}0.45$: $0/6{\to}5/6$ from $T{=}10$ to $T{=}15$)), though the 410M sync-dip at $\alpha{=}0.60$ does not appear (4/6 at $T{=}10$), suggesting the anomaly is architecture-specific.
84	The four non-confirming conditions each isolate a distinct PermG assumption violation.
85	\emph{Precision sensitivity}: GPT-2 bf16 yields 0/8 vs.\ fp32 6/8, traced to bf16 quantization noise masking the entropy signal.
86	\emph{Bidirectional confounding}: GPT-2 s43 detects 6/8 in both forward and reverse directions, preventing directional assignment.
87	\emph{Seed dependence}: Pythia-1.4B shows s42 2/8 vs.\ s43 6/8; seed-specific bidirectional confounding also appears at 1.4B (s43 reverse detection 6/8 at $\alpha{=}0.60$), analogous to the GPT-2 case, preventing directional assignment for that seed.
88	\emph{Entropy decoupling}: SmolLM3-3B reaches only 3/8, with ECE-only detection (entropy 0/4), violating the entropy-leads assumption of Observation~\ref{thm:entropy_leads}.
89	Standalone PermG claims therefore require architecture-specific null calibration; GPT-2 null FPR reaches 50\% (Appendix~\ref{app:fpr_independence}; per-architecture breakdown in Appendix~\ref{app:cross_arch_fpr}), driven by ${\sim}4{\times}$ stronger null drift than Pythia.
90	
91	\begin{figure}[t]
92	\centering
93	\includegraphics[width=\columnwidth]{figures/fig_cross_arch_heatmap.pdf}
94	\caption{Cross-architecture validation ($\alpha{=}1.0$): PermG forward detection (${\geq}6/8$) in 11/15 model-seed conditions spanning five families (345M--6.9B); faded bars: non-confirming conditions.}
95	\label{fig:cross_arch_heatmap}
96	\end{figure}
97	
98	
99	\subsection{Canary-Based Intervention (Proof of Concept)}
100	\label{sec:intervention}
101	
102	As a proof-of-concept under favorable conditions ($\alpha{=}1.0$), we implement predictive cessation: training switches to pure real data when token entropy drops beyond a 15\% threshold from generation~0 (robust band $[10\%, 22\%]$; Appendix~\ref{app:intervention_sensitivity}; CUSUM alternative in Appendix~\ref{app:csmp}).
103	The predictive trigger fires at generation~1, one full generation before a reactive baseline that monitors distinct-1 directly (which manifests only at generation~2 due to the cascade lag).
104	Predictive cessation caps peak perplexity at $56.99$ vs.\ $157.09$ reactive, a 64\% reduction (Figure~\ref{fig:intervention}); the result replicates on Pythia-1.4B with comparable effect size (Appendix~\ref{app:extended_discussion}).
105	
106	\begin{table}[t]
107	\centering
108	\caption{Consensus threshold operating characteristics ($K \in \{2,3,4,5\}$). FPR: null-control rate (10~seeds, 60~pairs; $K{\geq}2$ uses 9-seed estimate). TPR: detection rate at selected $\alpha$ levels (Pythia-410M, $T{=}10$, fp32). $K{=}3$ balances FPR control against detection power (75\% at $\alpha{=}1.0$); $K{=}4$ eliminates false positives but reduces TPR to ${\leq}25\%$.}
109	\label{tab:mmct_k_operating}
110	\begin{tabular}{@{}lcccc@{}}
111	\toprule
112	& $K{\geq}2$ & $K{\geq}3$ & $K{\geq}4$ & $K{=}5$ \\
113	\midrule
114	FPR ($\alpha{=}0.0$) & 38.9\% & 10.0\% & 0\% & 0\% \\
115	TPR ($\alpha{=}0.50$) & 85.4\% & 66.7\% & 25.0\% & 4.2\% \\
116	TPR ($\alpha{=}0.75$) & 72.9\% & 37.5\% & 0\% & 0\% \\
117	TPR ($\alpha{=}1.0$) & 75.0\% & 75.0\% & 25.0\% & 0\% \\
118	\bottomrule
119	\end{tabular}
120	\end{table}
121	
122	\begin{figure*}[t]
123	\centering
124	\includegraphics[width=\textwidth]{figures/fig_intervention.pdf}
125	\caption{Canary-triggered intervention (Pythia-410M, $\alpha{=}1.0$). Predictive cessation on entropy (generation~1) reduces peak perplexity by 64\% versus reactive triggering on distinct-1 (generation~2).}
126	\label{fig:intervention}
127	\end{figure*}
128	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a931b760-1617-42bb-b586-54da3de2d337",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "42b1d5d4-1ee8-41c0-9938-7bed9a10c016",
  "sourceToolAssistantUUID": "a931b760-1617-42bb-b586-54da3de2d337",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T10:49:33.740Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DkQEpjaug2b5eXVrTYcSoa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42b1d5d4-1ee8-41c0-9938-7bed9a10c016",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3sQkx96uuj2HrWNHYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8c9460ad-2b1d-4b36-a9f8-cf428f35e70e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBFVDuYPzobGeDBcB4St3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25197,
      "cache_read_input_tokens": 8259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25197,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 9,
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

_source line 17 · 2026-05-26T10:49:33.744Z_

<details><summary>↩ Tool result · `toolu_01DkQEpjaug2b5eXVrTYcSoa`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Iterative training collapse exhibits a steep detection onset: PermG detection jumps from 0/8 to 6/8 significant pairs (95\% CI $[0.25, 0.92]$) within 2~percentage points of $\alpha_c \approx 0.50$, organizing three regimes (blind, onset, detection) that characterize when statistical monitoring can and cannot succeed.
5	The detection boundary shifts leftward with longer observation ($\alpha_c(T) \propto T^{-\eta}$), and systematic method comparison reveals that single-method analyses are unreliable: null-control FPR spans 6.7\% (PermG; 95\% CI $[1.8\%, 16.2\%]$, 10~seeds) to 94.4\%.
6	Token entropy exhibits robust one-generation-ahead precedence over diversity collapse (24/24 forward, 0/24 reverse at $\alpha{=}1.0$; ${\geq}6/8$ in 11/15 cross-architecture conditions at $\alpha{=}1.0$).
7	The blind zone below $\alpha_c$ constrains practical deployment to settings with sufficient contamination; evaluation at ${>}$7B parameters remains open.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c9460ad-2b1d-4b36-a9f8-cf428f35e70e",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "8714e60c-5527-493d-a168-66bdbf090066",
  "sourceToolAssistantUUID": "8c9460ad-2b1d-4b36-a9f8-cf428f35e70e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T10:49:34.935Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Acbc6zCgyUhuknyZcAHTJm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8714e60c-5527-493d-a168-66bdbf090066",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3sQkx96uuj2HrWNHYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c4c96325-4dc8-48f8-b433-ff33ee148970",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBFVDuYPzobGeDBcB4St3t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25197,
      "cache_read_input_tokens": 8259,
      "output_tokens": 687,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25197
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 687,
          "cache_read_input_tokens": 8259,
          "cache_creation_input_tokens": 25197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25197,
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

_source line 19 · 2026-05-26T10:49:34.945Z_

<details><summary>↩ Tool result · `toolu_01Acbc6zCgyUhuknyZcAHTJm`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Scope.}
5	The phase diagram is built on Pythia-410M with full-replacement contamination and a single decoding strategy; frontier-scale models (${>}$7B) and partial-replacement regimes remain untested.
6	
7	\paragraph{Statistical power.}
8	Per-condition detection rates rest on 8 seeds, yielding wide binomial CIs (e.g., $[0.25, 0.92]$ for 6/8); the 3-seed phase diagram provides a coarse topology rather than precise probability estimates.
9	
10	\paragraph{Causal interpretation.}
11	Permutation Granger testing establishes temporal precedence, not causation, and our short-sequence regime ($T{\leq}25$) limits statistical power relative to econometric standards ($T{\geq}100$).
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4c96325-4dc8-48f8-b433-ff33ee148970",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "a5a03da8-eef9-4f7a-b525-008a7fd0d4a0",
  "sourceToolAssistantUUID": "c4c96325-4dc8-48f8-b433-ff33ee148970",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T10:49:34.946Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AmQtjvGGeixYQQLbzXoRaf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5a03da8-eef9-4f7a-b525-008a7fd0d4a0",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3sQkx96uuj2HrWNHYL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d1b6ec24-8ae5-451d-b22b-e7f8e2ae46a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UBFVDuYPzobGeDBcB4St3t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25197,
      "cache_read_input_tokens": 8259,
      "output_tokens": 687,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25197
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 687,
          "cache_read_input_tokens": 8259,
          "cache_creation_input_tokens": 25197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25197,
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

_source line 21 · 2026-05-26T10:49:35.329Z_

<details><summary>↩ Tool result · reported error · `toolu_01AmQtjvGGeixYQQLbzXoRaf`</summary>

```text
File content (45115 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1b6ec24-8ae5-451d-b22b-e7f8e2ae46a5",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "1f4a8cab-bb67-4956-a39b-63bb9bc421cc",
  "toolUseResult": "Error: File content (45115 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "d1b6ec24-8ae5-451d-b22b-e7f8e2ae46a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-26T10:49:38.351Z_

Let me read the appendix in parts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f4a8cab-bb67-4956-a39b-63bb9bc421cc",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3sxzSNUMGtW7qDQ2SQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45011f6f-decf-4d93-b235-53ef0b454008",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013g8gaDZfrLgn4gRq3GoFkY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21221,
      "cache_read_input_tokens": 33456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21221,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 23 · 2026-05-26T10:49:39.920Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NG9XEa4vPyDkD9uCLaycZh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45011f6f-decf-4d93-b235-53ef0b454008",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3sxzSNUMGtW7qDQ2SQ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "305065be-d74e-4b0e-b827-c47cd3bca46f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013g8gaDZfrLgn4gRq3GoFkY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21221,
      "cache_read_input_tokens": 33456,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21221
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 117,
          "cache_read_input_tokens": 33456,
          "cache_creation_input_tokens": 21221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21221,
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

_source line 24 · 2026-05-26T10:49:40.242Z_

<details><summary>↩ Tool result · `toolu_01NG9XEa4vPyDkD9uCLaycZh`</summary>

```text
1	\appendix
2	
3	\section{Training Details and Metric Drift}
4	\label{app:training_details}
5	\label{app:drift}
6	
7	\paragraph{Hyperparameters.}
8	Each generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).
9	Generation uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.
10	Canary metrics: token entropy $H(p_\theta | \text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.
11	Additional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.
12	
13	\paragraph{Architecture-specific training.}
14	Table~\ref{tab:arch_hyperparams} reports training hyperparameters for each architecture in the cross-architecture evaluation (\S\ref{sec:generalization}).
15	All models use the same generation parameters (temperature~$1.0$, top-$k{=}50$, max length 512) to control for decoding-strategy confounds.
16	Batch sizes are adjusted for GPU memory constraints; learning rates follow the respective model families' recommended fine-tuning ranges.
17	
18	\begin{table}[H]
19	\centering
20	\small
21	\caption{Per-architecture training hyperparameters.}
22	\label{tab:arch_hyperparams}
23	\begin{tabular}{lcccl}
24	\toprule
25	Model & Batch & LR & Steps & Precision \\
26	\midrule
27	Pythia-410M & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
28	Pythia-1.4B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
29	Pythia-6.9B & 2 & $2{\times}10^{-5}$ & 5{,}000 & bf16 \\
30	GPT-2-medium & 32 & $5{\times}10^{-5}$ & 5{,}000 & fp32/bf16 \\
31	OPT-1.3B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
32	Qwen3.5-0.8B & 4 & $5{\times}10^{-5}$ & 5{,}000 & fp32 \\
33	SmolLM3-3B & 4 & $2{\times}10^{-5}$ & 5{,}000 & fp32 \\
34	\bottomrule
35	\end{tabular}
36	\end{table}
37	
38	\paragraph{Metric computation details.}
39	Token entropy is computed as $H(p_\theta | x) = -\sum_{v} p_\theta(v|x) \log_2 p_\theta(v|x)$, averaged over 1{,}000 held-out WikiText-103 samples using greedy teacher-forcing (no sampling stochasticity).
40	ECE uses 15 equal-width bins on the confidence axis $c(x) = \max_v p_\theta(v|x)$, following the standard definition~\citep{naeini2015obtaining}:
41	$\mathrm{ECE} = \sum_{b=1}^{B} \frac{|b|}{N} |\mathrm{acc}(b) - \mathrm{conf}(b)|$.
42	Distinct-$n$ ($n \in \{1, 2, 3\}$) is the ratio of unique $n$-grams to total $n$-grams across all 5{,}000 generated samples per generation, following~\citet{li2016diversity}.
43	Perplexity is computed on a fixed 1{,}000-sample held-out split (disjoint from training and generation prompts).
44	
45	\paragraph{Seed and replication structure.}
46	The primary experiments use seeds 42, 43, 44 (3-seed cohort) for the phase diagram ($T{=}10$, 13 $\alpha$ levels).
47	Seed 45 is added for $\alpha{=}1.0$ experiments (4-seed).
48	Extended FPR analysis uses seeds 45--51 (6-pair basis, excluding MAUVE) for a total of 10 distinct seeds.
49	Cross-$T$ extensions ($T{=}15$, $20$, $25$) use the same seed set as the corresponding $\alpha$ condition.
50	
51	\paragraph{Metric drift.}
52	Table~\ref{tab:drift_summary} reports the relative change in each metric from generation~0 to generation~10 across six contamination levels.
53	Two patterns emerge: (1)~entropy and calibration (ECE) degrade monotonically with $\alpha$, while (2)~diversity metrics exhibit a non-monotonic relationship where the largest relative decline occurs at moderate contamination ($\alpha{=}0.25$) rather than full replacement ($\alpha{=}1.0$).
54	Figure~\ref{fig:metric_trajectory} (main text) visualizes representative per-generation trajectories, showing the distinct temporal profiles that underlie the Granger-precedence analysis in \S\ref{sec:method}.
55	
56	\begin{table}[H]
57	\centering
58	\small
59	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
60	\label{tab:drift_summary}
61	\resizebox{\columnwidth}{!}{%
62	\begin{tabular}{lccccc}
63	\toprule
64	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
65	\midrule
66	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
67	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
68	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
69	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
70	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
71	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
72	\bottomrule
73	\end{tabular}}
74	\end{table}
75	
76	\paragraph{Data pipeline.}
77	Each generation follows a fixed protocol: (1)~sample 5{,}000 prompts from WikiText-103 (first 32 tokens of random paragraphs); (2)~generate 512-token continuations using the current model $M_t$ with temperature~$1.0$, top-$k{=}50$; (3)~mix $\alpha$ fraction of generated text with $(1{-}\alpha)$ fraction of fresh WikiText-103 samples; (4)~fine-tune from the \emph{previous generation's} checkpoint (not from pretrained $M_0$).
78	Step~(4) produces iterative collapse by accumulating distributional biases across generations, distinct from single-generation fine-tuning drift.
79	The ``replace'' paradigm (step~3) means each generation trains on a completely fresh synthetic pool---there is no accumulation of earlier-generation synthetic data within the training set.
80	
81	\paragraph{Null-condition drift interpretation.}
82	At $\alpha{=}0.0$ (Table~\ref{tab:drift_summary}), all metrics exhibit non-trivial drift despite zero synthetic contamination: distinct-1 drops $14.1\%$, entropy drops $4.6\%$, and perplexity \emph{improves} by $20.6\%$.
83	This null drift reflects iterated fine-tuning on a fixed corpus: the model progressively memorizes WikiText-103, narrowing its effective vocabulary (lower distinct-$n$, lower entropy) while fitting the held-out distribution better (lower PPL).
84	The distinction between null drift and contamination-induced collapse is critical: our detection framework specifically tests whether canary metrics \emph{temporally precede} downstream metrics, not whether drift exists.
85	Null drift produces shared downward trends but without the temporal structure (lag) that Granger testing requires.
86	
87	\paragraph{Non-monotonic diversity-contamination relationship.}
88	A counterintuitive finding in Table~\ref{tab:drift_summary}: diversity loss is \emph{largest} at $\alpha{=}0.25$ (distinct-1: $-40.3\%$) and \emph{smallest} at $\alpha{=}1.0$ ($-27.8\%$).
89	This non-monotonicity arises because at high $\alpha$, the model collapses rapidly into a few dominant modes (by gen~3--4), after which diversity stabilizes near a floor.
90	The gen-0$\to$10 relative decline is smaller because the trajectory is concave (fast initial drop, then plateau).
91	At $\alpha{=}0.25$, the real-data fraction prevents catastrophic collapse but allows a steady, monotonic diversity decline across all 10 generations, producing a larger cumulative loss.
92	
93	
94	\section{Distinct-3 Results}
95	\label{app:distinct3}
96	
97	Table~\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.
98	Distinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\pm}0.9\%$ at $\alpha{=}0.25$) but attenuates at higher levels ($-30.5\%$ at $\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \S\ref{sec:discussion}.
99	
100	\begin{table}[H]
101	\centering
102	\small
103	\caption{Distinct-3 drift (\%, generation~0$\to$10) across contamination levels. $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.75$: 3-seed mean${\pm}$std; $\alpha{=}1.0$: 4-seed mean${\pm}$std; $\alpha{=}0.50$: single seed.}
104	\label{tab:distinct3_drift}
105	\begin{tabular}{lc}
106	\toprule
107	$\alpha$ & Distinct-3 drift (\%) \\
108	\midrule
109	0.00 & $-4.4{\pm}0.5$ \\
110	0.25 & $-58.9{\pm}0.9$ \\
111	0.50 & $-52.4$ \\
112	0.75 & $-38.6{\pm}1.3$ \\
113	1.00 & $-30.5{\pm}4.0$ \\
114	\bottomrule
115	\end{tabular}
116	\end{table}
117	
118	Distinct-3 exhibits higher lag instability than distinct-1/2 (bimodal lag distribution, std${>}1.5$ vs.\ ${<}0.5$ generations), reflecting its lower signal-to-noise ratio at 512-token generation length.
119	
120	\paragraph{Non-monotonic attenuation.}
121	The inverted-U shape of diversity loss (peaking at $\alpha{=}0.25$--$0.50$, attenuating at $\alpha{=}1.0$) is consistent across all three distinct-$n$ metrics.
122	At low contamination, diversity loss reflects fine-tuning drift amplified by weak synthetic contamination, which narrows the vocabulary without triggering the catastrophic mode collapse that dominates at high $\alpha$.
123	At $\alpha{=}1.0$, the model collapses into a small set of high-frequency modes quickly (by gen~3--4), after which diversity stabilizes at a low floor; the relative decline from gen-0 is therefore smaller because the trajectory is concave rather than linear.
124	
125	\paragraph{Granger detectability of distinct-3.}
126	Despite its large magnitude, distinct-3 drift is less Granger-detectable than distinct-1/2 because of its higher temporal noise.
127	PermG detection rates at $\alpha{=}1.0$: entropy$\to$distinct-1 achieves 6/8 across all seeds; entropy$\to$distinct-3 achieves only 4/8, with 2 seeds failing due to lag instability (bimodal lag distribution shifting the peak between lag~$-1$ and lag~$-2$ across seeds).
128	This motivates our focus on distinct-1 and distinct-2 as the primary downstream metrics in the main text.
129	
130	
131	\section{Observation Window Sensitivity}
132	\label{app:window_sensitivity}
133	
134	Consensus classification stabilizes at $T_{\min}{\geq}5$ (Table~\ref{tab:window_sensitivity}): all six effect-size reference pairs reach $K{\geq}4/5$ agreement at every window from $T_{\min}{=}5$ through $T_{\min}{=}10$.
135	
136	\paragraph{Per-method stability.}
137	At $\alpha{=}1.0$ (Pythia-410M, 4~seeds), we evaluate detection stability as $T_{\min}$ varies from 5 to 10 (i.e., using only generations $T_{\min}$ through $T{=}10$).
138	NaiveXCorr, DiffXCorr, ThresholdOnset, and PermG all maintain 6/6 validated pairs at every window length, confirming complete invariance to the observation start point.
139	Toda--Yamamoto shows the most variability: 3/6 at $T_{\min}{=}5$, rising to 6/6 at $T_{\min}{=}7$, then fluctuating between 3/6 and 6/6 at $T_{\min}{=}8$--$10$.
140	This instability reflects TY's higher sensitivity to degrees of freedom in short series (each 1-generation reduction removes ${\sim}10\%$ of available data at $T{=}10$).
141	
142	\paragraph{Implications for deployment.}
143	The stability result has a practical implication: a monitoring system need not wait for a full $T{=}10$ observation window before running detection.
144	As few as 6 data points ($T_{\min}{=}5$) suffice for reliable consensus-based detection at high contamination ($\alpha{=}1.0$), though the detection boundary $\alpha_c$ at shorter windows remains above $\alpha{=}0.50$ (insufficient power at $T{=}5$ for onset-level contamination).
145	The minimum requirement for Granger-type tests is $T_{\min}{\geq}5$ (below which degrees of freedom are insufficient for lag-1 regression with 2~parameters).
146	
147	\begin{figure}[H]
148	\centering
149	\includegraphics[width=\columnwidth]{figures/fig_window_sensitivity.pdf}
150	\caption{Detection stability as a function of minimum observation window $T_{\min}$ (Pythia-410M, $\alpha{=}1.0$, 4~seeds). PermG forward detection (6/8) and consensus classification ($K{\geq}4$) both stabilize at $T_{\min}{\geq}5$, with no significance flips for $T_{\min} \in [5, 10]$. This robustness confirms that the choice of $T_{\min}{=}5$ in the main analysis does not drive results.}
151	\label{fig:window_sensitivity}
152	\end{figure}
153	
154	\begin{table}[H]
155	\centering
156	\small
157	\caption{Observation window sensitivity for Tier~3 consensus ($K{\geq}4/5$) at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\to$downstream pairs (out of 8 validated) reaching $K{\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \S\ref{sec:method}). Consensus stabilizes at $T_{\min}{\geq}5$; TY stabilizes at $T_{\min}{\geq}6$.}
158	\label{tab:window_sensitivity}
159	\resizebox{\columnwidth}{!}{%
160	\begin{tabular}{lccccccccc}
161	\toprule
162	& \multicolumn{8}{c}{Minimum observation window $T_{\min}$} \\
163	\cmidrule(lr){2-9}
164	& 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
165	\midrule
166	Tier~3 pairs (/8)    & $\dagger$ & $\dagger$ & 6 & 6 & 6 & 6 & 6 & 6 \\
167	TY pairs$^\S$ (/6)   & $\dagger$ & $\dagger$ & 3--6 & 3--6 & 3--6 & 3--6 & 3--6 & 6 \\
168	Stable               & ---       & ---       & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
169	\bottomrule
170	\multicolumn{9}{l}{\footnotesize $\dagger$~Insufficient degrees of freedom for Granger-type tests ($<6$ data points).} \\
171	\multicolumn{9}{l}{\footnotesize $^\S$~TY directional assignment under verification.}
172	\end{tabular}}
173	\end{table}
174	
175	
176	\section{Robustness Analysis}
177	\label{app:robustness}
178	\label{app:spec_curve}
179	
180	\paragraph{Permutation count and FDR sensitivity.}
181	PermG $p$-values are stable between 5{,}000 and 10{,}000 permutations (max $|\Delta p|{=}0.010$, 0/24 significance flips at $\alpha{=}0.75$).
182	Treatment/null separation is robust to FDR threshold choice: at $q{=}0.05$, 4/36 null pairs vs.\ 19/24 treatment pairs reach significance; at $q{=}0.10$, null rejections rise to 8/36.
183	At the onset boundary ($\alpha{=}0.45$), minimum FDR-corrected $p$-values ($0.059$--$0.091$) are consistent with a continuous power transition rather than binary absence of signal.
184	
185	\paragraph{Specification curve.}
186	We construct 288 method-$\alpha$ configurations from 16 contamination levels and 18 method-direction specifications (5~methods $\times$ forward/reverse $\times$ FDR-correction variants; BH FDR $q{=}0.05$).
187	
188	\begin{table}[H]
189	\centering
190	\small
191	\caption{Specification curve summary (288 method-$\alpha$ configurations). The blind$\to$onset jump is robust across specifications: 0\% PermG significance rate through $\alpha{=}0.45$, rising to 75\% at $\alpha{=}0.50$.}
192	\label{tab:spec_curve}
193	\begin{tabular}{lc}
194	\toprule
195	Metric & Value \\
196	\midrule
197	Total configurations & 288 \\
198	Significant (${\geq}3/8$ pairs, FDR $q{<}0.05$) & 131 (45.5\%) \\
199	\midrule
200	\emph{By regime} & \\
201	\quad Blind ($\alpha \leq 0.45$) & 0\% \\
202	\quad Onset ($\alpha{=}0.50$) & 75\% \\
203	\quad Detection ($\alpha \geq 0.75$) & 62--75\% \\
204	\bottomrule
205	\end{tabular}
206	\end{table}
207	
208	The blind$\to$onset jump holds across the vast majority of specifications (Figure~\ref{fig:spec_curve}).
209	
210	\begin{figure}[H]
211	\centering
212	\includegraphics[width=\columnwidth]{figures/fig_spec_curve.pdf}
213	\caption{Specification curve (288 configurations). The blind$\to$onset jump at $\alpha_c{\approx}0.50$ is robust across methods, pairs, and seeds.}
214	\label{fig:spec_curve}
215	\end{figure}
216	
217	\paragraph{Specification decomposition.}
218	Within the 131 significant configurations (45.5\% of 288), the detection rate varies by canary$\to$downstream pair:
219	entropy$\to$distinct-1 and entropy$\to$distinct-2 are the most consistently detectable (significant in 75\% of above-onset specifications), while ECE$\to$perplexity is never significant (0\%, consistent with the first-differencing result in \S\ref{sec:regime}).
220	MAUVE-paired specifications show intermediate rates (50\% at $\alpha{=}1.0$, 0\% at $\alpha{=}0.50$), reflecting MAUVE's floor saturation at 1.4B scale.
221	
222	\paragraph{Cross-seed invariance.}
223	The specification curve's most notable feature is the \emph{absence} of seed-dependent specifications: no specification is significant at one seed but non-significant at another within the same $(\alpha, \text{pair})$ cell for $\alpha \in \{0.50, 0.75, 1.0\}$.
224	This uniformity (Fisher exact: $p = 3.45 \times 10^{-11}$ for the 0/8$\to$6/8 transition) provides the strongest evidence that the detection onset is a property of the data-generating process rather than a particular random initialization.
225	
226	\paragraph{Alternative FDR thresholds.}
227	Repeating the specification curve at $q{=}0.10$ increases significant specifications from 46.2\% to 53.8\%, with the additional detections concentrated at $\alpha{=}0.45$ (4 specifications cross from non-significant to significant) and $\alpha{=}0.60$ (2 specifications).
228	At $q{=}0.01$, the rate drops to 38.4\%, losing detections at $\alpha{=}0.50$ (onset boundary becomes less reliable).
229	The blind$\to$onset jump persists at all three thresholds, confirming structural robustness.
230	
231	\section{Transfer Entropy and Change-Point Analysis}
232	\label{app:transfer_entropy}
233	\phantomsection\label{app:te_mi}
234	
235	Transfer entropy (TE; \citealp{schreiber2000measuring}; 3-bin discretization, $n{=}5{,}000$ permutations) yields 0/192 BH-corrected significant pairs across all conditions, confirming that nonparametric information-theoretic methods lack power at $T{=}11$.
236	A KNN-based TE estimator ($k{=}5$) shows forward-dominant TE fraction increasing monotonically with $\alpha$ (4/8 at $\alpha{=}0.25$ to 8/8 at $\alpha{=}1.0$), but this does not reach statistical significance after FDR correction.
237	
238	\paragraph{Symbolic transfer entropy.}
239	Symbolic TE~\citep{staniek2008symbolic} using Bandt--Pompe ordinal patterns ($m{=}2$, lag${=}1$, 500 circular-shift surrogates, $p{<}0.05$) provides a complementary view.
240	At the $\alpha{=}0.60$ sync-dip where PermG detects 0/8, symbolic TE detects forward causation in 4/6 pairs ($p{<}0.001$): MAUVE-channel TE${=}0.539$ at $T{=}10$ and $0.496$ at $T{=}15$; distinct-1-channel TE${=}0.122$ at $T{=}20$.
241	Positive controls where PermG succeeds (6/8) yield 0/6 significant symbolic TE pairs (TE values 0.000--0.379, all $p{>}0.14$), and baseline conditions ($T{=}5$, $\alpha{=}0.50$) yield 0/2 significant (TE${=}0.000$--$0.189$, $p{=}1.000$).
242	This pattern---symbolic TE detecting signal precisely where PermG fails---suggests the sync-dip reflects compressed temporal lag rather than absent coupling: ordinal-pattern methods capture contemporaneous co-movement that Granger's lag-based framework misses.
243	
244	\paragraph{Conditional Granger analysis.}
245	To test whether ECE confounds the entropy$\to$diversity relationship, we run conditional Granger tests controlling for ECE when testing entropy$\to$diversity and vice versa.
246	Conditioning on ECE does not eliminate entropy's predictive contribution, consistent with the ECE co-movement argument (Appendix~\ref{app:cascade_theory}): both metrics respond to the same underlying mode amplification, but entropy provides the earliest signal.
247	
248	\phantomsection\label{app:change_point}
249	\paragraph{Change-point detection.}
250	Max-split change-point tests ($n{=}5{,}000$ bootstrap) yield 66.7\% FPR under null control (12/18, $\alpha{=}0.00$), precluding use as a standalone detector.
251	However, the temporal ordering of change-points reverses between null and treatment: under null, downstream metrics break first (gen~2) before canary (gen~4--8); under treatment ($\alpha{\geq}0.75$), canary breaks first (gen~1) before downstream (gen~2--4).
252	This ordering reversal shifts monotonically with $\alpha$, consistent with the Granger-precedence analysis.
253	
254	
255	\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}
256	\label{app:csmp}
257	
258	CUSUM sequential testing~\citep{page1954continuous} calibrated against $\alpha{=}0.0$ null control (FAR${=}$0\%) produces identical alarm times as a simple $2\sigma$ threshold at all tested operating points: both trigger at generation~1 for $\alpha{\geq}0.50$.
259	The equivalence arises because the generation-0$\to$1 entropy drop ($|\Delta x|{>}0.7$) greatly exceeds null variability ($\sigma_0{\approx}0.03$); CUSUM's cumulative memory provides no advantage when the initial shift dominates.
260	
261	\paragraph{Operating characteristics.}
262	We evaluate both methods across the full contamination range:
263	\begin{itemize}
264	\item $\alpha{=}0.00$--$0.45$: neither method triggers within $T{=}10$ generations (entropy drift ${\leq}5.3\%$, within null variability band).
265	\item $\alpha{=}0.50$: both trigger at generation~1 (entropy drop $18.0{\pm}0.5\%$, exceeding $2\sigma$ and CUSUM threshold simultaneously).
266	\item $\alpha{=}0.75$--$1.0$: both trigger at generation~1 (entropy drop $27.6$--$60.8\%$).
267	\end{itemize}
268	The regime structure of CUSUM/threshold monitoring thus recapitulates the PermG blind zone: no detection below $\alpha{=}0.50$ at $T{=}10$, immediate detection above.
269	The critical difference is that these methods detect \emph{deviation from baseline}, not \emph{temporal precedence}---they cannot distinguish whether entropy leads or lags diversity without additional directional analysis.
270	
271	\paragraph{Practical implications.}
272	For production monitoring where establishing Granger precedence is unnecessary, a calibrated entropy threshold ($[10\%, 22\%]$; Appendix~\ref{app:intervention_sensitivity}) provides a simple, zero-cost alarm.
273	CUSUM adds value only when the signal emerges gradually across multiple generations (e.g., at contamination levels near $\alpha_c$ where the generation-0$\to$1 drop is small); in our setting, the large initial entropy shift renders CUSUM's cumulative advantage moot.
274	
275	\paragraph{Detection timing comparison.}
276	Table~\ref{tab:sequential_timing} compares alarm generation for CUSUM and calibrated threshold across the full contamination range.
277	
278	\begin{table}[H]
279	\centering
280	\small
281	\caption{Sequential monitoring alarm timing (Pythia-410M, seed~42, fp32). ``---'' = no alarm within $T{=}10$. Both methods produce identical alarm patterns: no detection below $\alpha{=}0.50$, immediate (gen-1) detection above.}
282	\label{tab:sequential_timing}
283	\begin{tabular}{@{}lccc@{}}
284	\toprule
285	$\alpha$ & CUSUM & Threshold & $\Delta H$ (\%) \\
286	\midrule
287	0.00 & --- & --- & $-4.6$ \\
288	0.10 & --- & --- & $-5.3$ \\
289	0.25 & --- & --- & $-4.7$ \\
290	0.45 & --- & --- & $-5.1$ \\
291	0.50 & gen-1 & gen-1 & $-18.0$ \\
292	0.60 & gen-1 & gen-1 & $-28.5$ \\
293	0.75 & gen-1 & gen-1 & $-27.6$ \\
294	1.00 & gen-1 & gen-1 & $-60.8$ \\
295	\bottomrule
296	\end{tabular}
297	\end{table}
298	
299	The binary alarm pattern (no alarm below $\alpha{=}0.50$, immediate alarm above) mirrors PermG's regime structure, confirming that the blind zone is a property of the data-generating process rather than the detection method.
300	However, sequential monitoring methods cannot distinguish between causal temporal precedence and synchronous co-movement---a system relying solely on CUSUM would flag $\alpha{=}0.50$ contamination but could not determine whether entropy decline \emph{causes} or merely \emph{accompanies} diversity loss.
301	
302	\paragraph{False alarm rate calibration.}
303	Under null control ($\alpha{=}0.0$), neither method triggers false alarms at any threshold within the safe operating band $[10\%, 22\%]$, yielding FAR${=}0\%$ across all 3 null-condition seeds.
304	At thresholds below 7.5\%, both methods produce false alarms at gen-3 ($\alpha{=}0.0$ entropy drift: $-4.6\%$ approaches the threshold), giving FAR${=}100\%$.
305	This calibration sensitivity motivates a two-threshold deployment strategy: use the lenient bound ($10\%$) for early warning and the strict bound ($22\%$) for confirmed alarm, with the gap serving as a monitoring zone requiring additional diagnostic tests (e.g., Granger analysis) before triggering intervention.
306	
307	\section{Background and Notation}
308	\label{app:background}
309	\label{sec:background}
310	
311	This section establishes the formal setup and notation used throughout the paper.
312	
313	\paragraph{Iterative training loop.}
314	Let $M_0$ denote a pretrained language model and $\mathcal{D}_\text{real}$ a fixed corpus of human-written text.
315	At each generation $t \geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\mathcal{D}_\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data:
316	\begin{equation}
317	    \mathcal{D}_\text{train}^{(t)} = \alpha \cdot \mathcal{D}_\text{synth}^{(t-1)} \;+\; (1{-}\alpha) \cdot \mathcal{D}_\text{real}, \quad \alpha \in [0, 1].
318	    \label{eq:mixing}
319	\end{equation}
320	At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}.
321	
322	\paragraph{Metric families.}
323	\emph{Canary metrics}: token entropy ($H(p_\theta | \text{context})$ on held-out samples) and expected calibration error (ECE).
324	\emph{Downstream metrics}: distinct-$n$ ($n \in \{1, 2, 3\}$)~\citep{li2016diversity} and perplexity.
325	Each metric produces a time series of $T{+}1$ observations.
326	
327	\paragraph{Lead-lag testing.}
328	Given canary series $X$ and downstream series $Y$, the central question is whether changes in $X$ temporally precede changes in $Y$, requiring directionality and confounder control beyond simple correlation.
329	We employ five methods spanning permissive to conservative: naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality~\citep{shojaie2022granger}, and Toda--Yamamoto Granger causality~\citep{toda1995statistical}.
330	
331	\paragraph{Method details.}
332	\emph{Naive cross-correlation (NaiveXCorr)} computes Pearson $r$ between $X_{t}$ and $Y_{t+\ell}$ at lag $\ell \in [-5, 5]$; significance at any lag below uncorrected $p{<}0.05$ counts as detection.
333	This method is permissive because it ignores shared trends and applies no multiplicity correction.
334	\emph{Differenced cross-correlation (DiffXCorr)} applies the same procedure to first-differenced series $\Delta X_t = X_t - X_{t-1}$, controlling for common trends but remaining bidirectional (cannot distinguish $X \to Y$ from $Y \to X$).
335	\emph{Threshold onset detection} identifies the first generation where each metric crosses a $3\sigma$ threshold below its generation-0 value (where $\sigma$ is the null-control standard deviation); detection is declared if canary onset strictly precedes downstream onset.
336	\emph{Permutation Granger causality (PermG)} tests whether lagged $X$ values improve prediction of $Y$ beyond $Y$'s own history, using 5{,}000 temporal permutations to construct a nonparametric null distribution, followed by BH-FDR correction at $q{=}0.05$ across 8 metric pairs.
337	\emph{Toda--Yamamoto (TY)} augments a VAR model with $d_{\max}$ extra lags to handle potential non-stationarity, then tests the original lag coefficients via Wald test.
338	
339	\paragraph{PermG implementation details.}
340	The permutation Granger procedure operates as follows:
341	(1)~First-difference both series: $\Delta X_t = X_t - X_{t-1}$, $\Delta Y_t = Y_t - Y_{t-1}$.
342	(2)~Fit unrestricted model: $\Delta Y_t = a_0 + \sum_{j=1}^{L} a_j \Delta Y_{t-j} + \sum_{j=1}^{L} b_j \Delta X_{t-j} + \epsilon_t$ (lag $L{=}1$).
343	(3)~Fit restricted model: $\Delta Y_t = a_0 + \sum_{j=1}^{L} a_j \Delta Y_{t-j} + \epsilon_t$.
344	(4)~Compute observed $F$-statistic from the residual sum of squares reduction.
345	(5)~Generate 5{,}000 null realizations by randomly permuting the temporal order of $\Delta X$, re-fitting unrestricted model each time.
346	(6)~$p$-value $= (\text{count}(F_{\text{perm}} \geq F_{\text{obs}}) + 1) / (n_{\text{perm}} + 1)$ following~\citet{phipson2010permutation}.
347	The permutation scheme destroys temporal structure in $X$ while preserving its marginal distribution, providing an exact null for the hypothesis ``past $X$ does not improve prediction of $Y$.''
348	We use fixed $L{=}1$ given the short series length ($T{-}2L \geq 3$ degrees of freedom at $T{=}11$); the Toda--Yamamoto procedure uses AIC-based lag selection separately.
349	
350	\paragraph{Direction checking.}
351	For each significant pair, we additionally test the reverse direction ($Y \to X$).
352	A pair is classified as ``forward-only'' if $X \to Y$ is significant and $Y \to X$ is not; ``bidirectional'' if both are significant; and ``reverse-only'' if only $Y \to X$ is significant.
353	Forward-only pairs provide the strongest evidence for temporal precedence.
354	In the main analysis, we report forward detection counts; bidirectional pairs are flagged in the failure mode taxonomy (\S\ref{sec:generalization}).
355	
356	\paragraph{Multiple testing structure.}
357	At each contamination level and seed, we test 8 canary$\to$downstream pairs (2 canary $\times$ 4 downstream metrics; MAUVE is a 9th pair included in some analyses).
358	BH-FDR correction at $q{=}0.05$ is applied within each $(\alpha, \text{seed}, \text{method})$ family of 8 tests, yielding corrected $p$-values $p_{\mathrm{fdr}}$.
359	We do not correct across $\alpha$ levels or seeds, as these represent genuinely different conditions rather than multiple looks at the same hypothesis.
360	The 8-pair correction is conservative relative to per-family error rate control: BH-FDR at $q{=}0.05$ guarantees that at most 5\% of rejected hypotheses are false discoveries, averaging across the 8 tests within each family.
361	
362	\section{MMCT Algorithm}
363	\label{app:mmct}
364	
365	\noindent\emph{See Algorithm~\ref{alg:mmct} in the main text (\S\ref{sec:mmct}) for the full MMCT pseudocode and design rationale.}
366	
367	\begin{figure}[H]
368	\centering
369	\includegraphics[width=\columnwidth]{figures/consensus_heatmap.pdf}
370	\caption{$K{\geq}3$ consensus heatmap across the $\alpha \times T$ grid (Pythia-410M, fp32). Each cell shows the number of canary$\to$diversity pairs reaching majority agreement (${\geq}3/5$ methods). Consensus detection aligns with PermG's onset at $\alpha{=}0.50$ but eliminates the non-monotonic anomaly at $\alpha{=}0.60$ (consensus detects 8/8 where PermG detects 0/8), indicating the anomaly is PermG-specific.}
371	\label{fig:consensus_heatmap}
372	\end{figure}
373	
374	\paragraph{MMCT design rationale.}
375	The MMCT consensus approach is motivated by the observation that no single method achieves both low FPR and high detection rate across all contamination levels.
376	PermG has the lowest FPR (6.7\%) but misses the $\alpha{=}0.60$ regime; DiffXCorr detects everywhere but cannot establish directionality; NaiveXCorr's 94.4\% FPR makes it unsuitable as a standalone detector.
377	By requiring $K{\geq}3$ methods to agree, MMCT effectively requires that at least one conservative method (PermG or DiffXCorr) participates in the consensus, filtering out detections driven solely by permissive methods.
378	
379	\paragraph{FPR-inverse weighting design.}
380	The weight $w_k = 1/\max(\widehat{\mathrm{FPR}}_k, \epsilon)$ ensures that methods with lower empirical FPR have proportionally higher influence on the consensus score.
381	The floor $\epsilon{=}0.01$ prevents division by zero for methods with 0\% FPR (none in our case).
382	Under this scheme, PermG's weight ($w{=}14.9$) dominates NaiveXCorr's ($w{=}1.06$) by $14{\times}$: a detection requires PermG agreement unless ${\geq}4$ other methods agree without it.
383	The empirical null distribution (step~7 of Algorithm~\ref{alg:mmct}) avoids parametric assumptions that would be unreliable for our short ($T{=}5$--$25$), non-stationary series.
384	
385	\paragraph{Sensitivity to $K$.}
386	Table~\ref{tab:mmct_k_operating} (main text) reports operating characteristics for $K \in \{2, 3, 4, 5\}$.
387	The $K{=}3$ threshold represents a Pareto-optimal operating point: decreasing to $K{=}2$ raises FPR from 10.0\% to 38.9\% with modest TPR gain ($66.7\% \to 85.4\%$ at $\alpha{=}0.50$); increasing to $K{=}4$ eliminates false positives ($0\%$) but drops TPR to ${\leq}25\%$ across all conditions.
388	At $K{=}5$ (unanimity), the expected detection rate is below 5\% everywhere---only achievable when all five methods, including the 94\%-FPR NaiveXCorr, agree.
389	
390	\begin{figure}[H]
391	\centering
392	\includegraphics[width=\columnwidth]{figures/fig_mmct_k_operating.pdf}
393	\caption{MMCT operating characteristics as a function of consensus threshold $K$. Left axis: FPR (null-control false positives); right axis: FNR (missed detections at $\alpha{\geq}0.50$). $K{=}3$ balances FPR and sensitivity; $K{=}4$ reduces FPR further but increases FNR, particularly at boundary conditions. $K{=}2$ is dominated by high-FPR methods (NaiveXCorr, TY) and provides no useful filtering.}
394	\label{fig:mmct_k_operating}
395	\end{figure}
396	
397	\section{Methodological Comparison Table}
398	\label{app:method_comparison}
399	
400	Table~\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \S\ref{sec:method}.
401	No prior work combines all six dimensions.
402	
403	\begin{table}[H]
404	\centering
405	\small
406	\caption{Methodological comparison of canary and monitoring analyses. \checkmark\ = present, $\times$ = absent, $\circ$ = partial (${\leq}2$ levels or limited replication). Diff.\ = differencing/stationarity controls. Multi-M.\ = ${\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\alpha$. Seeds = ${\geq}3$ independent seeds. Arch.\ = ${\geq}2$ architecturally distinct model families.}
407	\label{tab:method-comparison}
408	\resizebox{\columnwidth}{!}{%
409	\begin{tabular}{lccccccl}
410	\toprule
411	Work & Diff. & Multi-M. & MTC & Regime & Seeds & Arch. & Metrics \\
412	\midrule
413	\citet{shumailov2024curse}     & $\times$   & $\times$   & $\times$   & $\circ$    & \checkmark & \checkmark & PPL \\
414	\citet{du2025scales}           & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & $\times$   & ECE, Acc, Dist-$n$ \\
415	\citet{gambetta2024surplexity} & $\times$   & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & Surplexity, Ent \\
416	SIGMA~\citep{sigma2026spectral} & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & Spectral \\
417	DCES~\citep{dces2026counter}    & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & \checkmark & ECE, Ent, PPL \\
418	\midrule
419	\textbf{Ours}                  & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & Ent, ECE, PPL, Dist-$n$ \\
420	\bottomrule
421	\end{tabular}%
422	}
423	\end{table}
424	
425	\paragraph{Dimension justification.}
426	The six diagnostic dimensions in Table~\ref{tab:method-comparison} are motivated by known failure modes in time-series causal inference:
427	\emph{Differencing} controls spurious regression when both series share a deterministic trend~\citep{granger1974spurious}---without it, any two monotonically declining series will appear correlated.
428	\emph{Multi-method comparison} addresses the method sensitivity documented in \S\ref{sec:mmct}: a single method's conclusion may reflect its assumptions rather than the data.
429	\emph{Multiple testing correction} is necessary because each contamination level generates 8 metric pairs; uncorrected testing at $p{<}0.05$ expects ${\sim}0.4$ false positives per condition.
430	\emph{Regime variation} is required to map the detection landscape rather than reporting a single operating point.
431	\emph{Seed replication} distinguishes signal from initialization artifacts.
432	\emph{Cross-architecture evaluation} tests whether findings are specific to one model family or reflect general properties of iterative collapse.
433	Among existing works, \citet{du2025scales} comes closest (4/6 dimensions) but omits differencing and multi-method analysis, both of which our results show are critical.
434	
435	\section{Extended Discussion}
436	\label{app:extended_discussion}
437	
438	\paragraph{Calibration scope.}
439	All calibration results are specific to our setup (Pythia-410M, WikiText-103, $T{=}10$).
440	On C4 at $\alpha{=}0.50$, PermG reverse reaches 7/8 (seed-dependent: s43 1/8), indicating directional asymmetry should be verified per domain.
441	Token entropy ($H(p_\theta|\text{context})$ on held-out data) and perplexity ($\exp(H_\text{cross})$ on generated text) co-move synchronously, explaining why first-differencing eliminates canary$\to$perplexity but preserves canary$\to$diversity.
442	
443	\paragraph{Alternative explanations for the blind zone.}
444	Three mechanisms could explain why detection fails below $\alpha_c$:
445	\emph{(1)~Signal absence}: at low $\alpha$, the real-data fraction dominates, and the model's distributional shift is too small to generate temporal structure detectable by any linear method.
446	\emph{(2)~Power limitation}: the signal exists but falls below PermG's detection threshold at $T{=}10$ (supported by the $T{=}20$ result showing 5/8 at $\alpha{=}0.45$).
447	\emph{(3)~Contemporaneous coupling}: at low $\alpha$, entropy and diversity respond simultaneously rather than sequentially, eliminating the lag that Granger tests require.
448	The MI analysis (Appendix~\ref{app:mi_analysis}) favors explanation~(2): coupling between entropy and diversity exists throughout the blind zone ($\hat{I}_G > 0$ at all $\alpha$), and the cross-$T$ results confirm that longer observation resolves detection at $\alpha{=}0.45$.
449	However, explanation~(3) may contribute at very low $\alpha$ (${\leq}0.10$), where the contamination signal is minimal and both metrics drift primarily due to fine-tuning.
450	
451	\paragraph{Entropy as a measurement artifact.}
452	A potential concern is that entropy's ``leading'' behavior reflects measurement sensitivity rather than a genuine temporal cascade: entropy is a continuous quantity computed from the full probability distribution, while distinct-$n$ is a discrete count computed from a finite sample.
453	Entropy can therefore respond to arbitrarily small distributional shifts that leave the token-level generation unchanged.
454	We note three counterarguments:
455	(1)~The ECE co-movement result confirms that calibration---a separate measurement---also shifts at gen-1, suggesting the signal is real.
456	(2)~First-differencing preserves the canary$\to$diversity relationship while eliminating canary$\to$perplexity, which would not occur if the signal were purely a measurement artifact.
457	(3)~The intervention experiment demonstrates that acting on the entropy signal at gen-1 produces a measurably different outcome (64\% lower peak perplexity), confirming functional relevance.
458	Nonetheless, the possibility that entropy's sensitivity partly reflects measurement properties rather than causal priority cannot be fully excluded without mechanistic analysis.
459	
460	\paragraph{Cross-architecture failure mode analysis.}
461	The four non-confirming conditions in the cross-architecture evaluation each isolate a distinct assumption violation:
462	
463	\begin{table}[H]
464	\centering
465	\small
466	\caption{Failure mode taxonomy for non-confirming cross-architecture conditions ($\alpha{=}1.0$).}
467	\label{tab:failure_modes}
468	\resizebox{\columnwidth}{!}{%
469	\begin{tabular}{llll}
470	\toprule
471	Condition & PermG & Failure mode & Root cause \\
472	\midrule
473	GPT-2 bf16 & 0/8 & Precision & bf16 noise masks signal \\
474	GPT-2 s43 & 6/8 both & Bidirectional & No directional separation \\
475	Pythia-1.4B s42 & 2/8 & Seed & Initialization-dependent \\
476	SmolLM3-3B & 3/8 & Decoupling & Entropy non-monotonic \\
477	\bottomrule
478	\end{tabular}}
479	\end{table}
480	
481	The precision failure (GPT-2 bf16) is actionable: switching to fp32 resolves detection (0/8$\to$6/8) with no change to the underlying collapse dynamics.
482	The bidirectional failure (GPT-2 s43) is more fundamental: it indicates that for some model-seed combinations, the entropy-diversity temporal structure is symmetric, preventing directional assignment.
483	The seed dependence (Pythia-1.4B s42 vs.\ s43: 2/8 vs.\ 6/8) highlights the fragility of directional testing in short series.
484	The entropy decoupling (SmolLM3-3B: entropy 0/4, ECE 3/4) directly violates the cascade ordering assumption, suggesting that SmolLM3's architecture produces a qualitatively different collapse trajectory.
485	
486	\paragraph{Scale verification (Pythia-1.4B).}
487	\label{app:scale_14b}
488	
489	\begin{table}[H]
490	\centering
491	\small
492	\caption{Pythia-1.4B phase diagram replication: PermG forward/reverse detection and $K{\geq}3$ consensus across contamination levels and observation windows (fp32). $\dagger$: bidirectional confounding (reverse${}>0$). Denominator is 8 unless marked $^{*}$ (6-pair basis, MAUVE unavailable).}
493	\label{tab:14b_phase}
494	\begin{tabular}{@{}llcccc@{}}
495	\toprule
496	$T$ & $\alpha$ & Seed & Fwd & Rev & $K{\geq}3$ \\
497	\midrule
498	10 & 0.45 & 42 & 0/8 & 0/8 & 0/8 \\
499	   &      & 43 & 1/8 & 0/8 & 2/8 \\
500	   &      & 44 & 0/6$^{*}$ & 0/6$^{*}$ & 0/6$^{*}$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "305065be-d74e-4b0e-b827-c47cd3bca46f",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "2c6489dc-3fda-4d12-a9fd-e53de614d60c",
  "sourceToolAssistantUUID": "305065be-d74e-4b0e-b827-c47cd3bca46f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T10:49:44.431Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UhqxBVpxEjPNLMzgVJ3DVT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c6489dc-3fda-4d12-a9fd-e53de614d60c",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3tKyVm3e9CNbeWriWh",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5b3f9203-5be9-4e5e-bc98-08dd7781d578",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFRJpfti2JiiSDyEYdjgdC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14585,
      "cache_read_input_tokens": 54677,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14585
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 54677,
          "cache_creation_input_tokens": 14585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14585,
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

_source line 26 · 2026-05-26T10:49:44.715Z_

<details><summary>↩ Tool result · `toolu_01UhqxBVpxEjPNLMzgVJ3DVT`</summary>

```text
500	   &      & 44 & 0/6$^{*}$ & 0/6$^{*}$ & 0/6$^{*}$ \\
501	\cmidrule(l){2-6}
502	   & 0.50 & 42 & 4/8 & 2/8$^{\dagger}$ & 3/8 \\
503	   &      & 43 & 6/6$^{*}$ & 0/6$^{*}$ & 1/6$^{*}$ \\
504	   &      & 44 & 6/6$^{*}$ & 0/6$^{*}$ & 0/6$^{*}$ \\
505	\cmidrule(l){2-6}
506	   & 0.60 & 42 & 4/8 & 0/8 & 3/8 \\
507	   &      & 43 & 4/8 & 6/8$^{\dagger}$ & 3/8 \\
508	   &      & 44 & 6/6$^{*}$ & 0/6$^{*}$ & 5/6$^{*}$ \\
509	\cmidrule(l){2-6}
510	   & 0.75 & 42 & 5/8 & 0/8 & 5/8 \\
511	   &      & 43 & 6/8 & 5/8$^{\dagger}$ & 5/8 \\
512	   &      & 44 & 6/6$^{*}$ & 0/6$^{*}$ & 6/6$^{*}$ \\
513	\midrule
514	15 & 0.45 & 42 & 3/8 & 0/8 & 4/8 \\
515	   &      & 43 & 5/6$^{*}$ & 3/6$^{*\dagger}$ & 3/6$^{*}$ \\
516	\cmidrule(l){2-6}
517	   & 0.50 & 42 & 3/8 & 0/8 & 2/8 \\
518	   &      & 43 & 3/6$^{*}$ & 0/6$^{*}$ & 3/6$^{*}$ \\
519	\cmidrule(l){2-6}
520	   & 0.60 & 42 & 6/8 & 0/8 & 6/8 \\
521	   &      & 43 & 6/6$^{*}$ & 3/6$^{*\dagger}$ & 6/6$^{*}$ \\
522	\cmidrule(l){2-6}
523	   & 0.75 & 42 & 6/8 & 0/8 & 6/8 \\
524	   &      & 43 & 6/6$^{*}$ & 0/6$^{*}$ & 6/6$^{*}$ \\
525	\bottomrule
526	\end{tabular}
527	\end{table}
528	
529	Phase-diagram structure is qualitatively preserved at 1.4B (Table~\ref{tab:14b_phase}; Figure~\ref{fig:14b_phase}): detection boundary at $\alpha_c{\approx}0.50$, cross-$T$ improvement at 3/4 $\alpha$ values ($\alpha{=}0.45$: $0/6{\to}5/6$).
530	The 410M sync-dip does not reproduce at 1.4B (4/6 at $\alpha{=}0.60$, $T{=}10$).
531	Bidirectional confounding is seed-specific: s43 shows reverse significance at $\alpha{=}0.60$ (6/8) and $\alpha{=}0.75$ (5/8) for $T{=}10$, while s42 maintains 0 reverse across all conditions.
532	
533	\begin{figure}[H]
534	\centering
535	\includegraphics[width=\columnwidth]{figures/fig_14b_phase.pdf}
536	\caption{Pythia-1.4B phase diagram (PermG forward, 6-pair basis). Detection boundary ($\alpha_c \approx 0.50$) is consistent with 410M.}
537	\label{fig:14b_phase}
538	\end{figure}
539	
540	\paragraph{Scale effects on detection topology.}
541	Three scale-dependent effects emerge from comparing 410M and 1.4B:
542	\begin{enumerate}
543	\item \emph{Sync-dip suppression}: The $\alpha{=}0.60$ non-monotonic anomaly is absent at 1.4B (4/6--6/6 vs.\ 0/8 at 410M), suggesting that larger models maintain wider entropy-diversity temporal separation, preventing the lag compression that produces the dip.
544	\item \emph{Seed variability amplification}: Cross-seed detection variance is higher at 1.4B (s42: 2/8 vs.\ s43: 6/8 at $\alpha{=}1.0$) than at 410M (6/8 across all seeds), possibly reflecting the larger model's richer attractor landscape.
545	\item \emph{Domain transfer}: Pythia-1.4B on C4 yields 8/8 PermG forward detection ($K{\geq}3{=}8/8$) compared to 2--6/8 on WikiText, indicating that domain characteristics (vocabulary coverage, topic diversity) interact with scale to affect detection sensitivity.
546	\end{enumerate}
547	
548	\paragraph{Intervention at 1.4B.}
549	Predictive cessation replicates at 1.4B: entropy drops $51.9\%$ ($2.946 \to 1.418$) at gen-1, triggering intervention.
550	Peak PPL rises from $19.68$ to $65.37$ (a $232\%$ increase, vs.\ $112\%$ at 410M), but recovery is faster (gen-2 PPL${=}17.44$, below the gen-0 baseline).
551	The larger entropy drop at 1.4B ($51.9\%$ vs.\ $40.7\%$) reflects stronger mode amplification at scale, consistent with the theoretical prediction that higher-capacity models amplify dominant modes more aggressively~\citep{shumailov2024curse}.
552	
553	
554	
555	\section{Per-Method Dose-Response Profiles}
556	\label{app:dose_response}
557	
558	Table~\ref{tab:dose_response_full} reports FDR significance counts (/8 validated pairs) for all five detection methods across 12 contamination levels (seed~42, Pythia-410M, WikiText, fp32).
559	PermG exhibits a steep 0$\to$6 jump at $\alpha{=}0.50$ with a return to 0 at $\alpha{=}0.55$--$0.60$ (non-monotonic dip), while other methods show diffuse profiles: naive cross-correlation saturates at 7--8/8 across all levels including the null, and Toda--Yamamoto fluctuates without a clear onset.
560	
561	\begin{table}[H]
562	\centering
563	\small
564	\caption{Per-method FDR significance (/8 pairs) across contamination levels (Pythia-410M, seed~42, WikiText, fp32). PermG and Diff.\ XCorr use BH-corrected FDR ($q{=}0.05$); Naive XCorr, Threshold, and TY use uncorrected $p{<}0.05$ (no FDR field in pipeline). $\alpha{=}1.0$ from Pythia-410M cross-architecture condition (same seed/domain/precision).}
565	\label{tab:dose_response_full}
566	\resizebox{\columnwidth}{!}{%
567	\begin{tabular}{lccccc}
568	\toprule
569	$\alpha$ & Naive & Diff.\ XCorr & Threshold & PermG & TY$^\S$ \\
570	\midrule
571	0.00 & 8 & 4 & 3 & \textbf{0} & 1 \\
572	0.10 & 7 & 6 & 0 & \textbf{0} & 0 \\
573	0.25 & 8 & 3 & 0 & \textbf{0} & 2 \\
574	0.30 & 8 & 4 & 0 & \textbf{0} & 3 \\
575	0.35 & 8 & 4 & 0 & \textbf{0} & 1 \\
576	0.40 & 8 & 3 & 0 & \textbf{0} & 4 \\
577	0.45 & 8 & 6 & 0 & \textbf{0} & 1 \\
578	0.50 & 8 & 7 & 4 & \textbf{6} & 3 \\
579	0.55 & 8 & 8 & 0 & \textbf{0} & 1 \\
580	0.60 & 8 & 6 & 0 & \textbf{0} & 0 \\
581	0.75 & 7 & 6 & 0 & \textbf{6} & 3 \\
582	1.00 & 8 & 6 & 2 & \textbf{6} & 1 \\
583	\bottomrule
584	\multicolumn{6}{l}{\footnotesize $^\S$TY directional assignment under verification; column retained for completeness.} \\
585	\end{tabular}}
586	\end{table}
587	
588	PermG's dose-response profile most cleanly separates detection regimes: 0/8 at null, steep 0$\to$6 onset at $\alpha{=}0.50$, non-monotonic dip at $\alpha{=}0.55$--$0.60$.
589	Naive monitoring baselines (PPL-slope, variance-threshold) fire at $\alpha{=}0.0$ (FPR 67--100\%) because fine-tuning drift is indistinguishable from contamination without directional testing.
590	
591	\paragraph{Method-specific observations.}
592	\emph{NaiveXCorr} saturates at 7--8/8 at every $\alpha$ including null, making it useless for regime discrimination---its FPR (94.4\%) means it would declare detection in 19 out of 20 null-control runs.
593	\emph{DiffXCorr} shows the highest detection rate at $\alpha{\geq}0.50$ (6--8/8) but maintains 4/8 at null, yielding FPR${=}37.5\%$.
594	Its bidirectional nature (significant in both forward and reverse) prevents causal attribution but confirms the presence of coupling.
595	\emph{Threshold onset} is highly specific (3/8 at null) but insensitive (0/8 at $\alpha{=}0.10$--$0.45$ and $\alpha{=}0.55$--$0.75$), detecting only when the generation-1 entropy drop is unambiguously large.
596	\emph{Toda--Yamamoto} fluctuates between 0/8 and 4/8 across all $\alpha$ levels with no clear dose-response structure, reflecting its poor finite-sample properties at $T{=}10$.
597	
598	\paragraph{Inter-method agreement.}
599	Cohen's $\kappa$ between all method pairs ranges from $-0.04$ (NaiveXCorr vs.\ Threshold, near-random disagreement) to $0.42$ (PermG vs.\ DiffXCorr, moderate agreement above onset).
600	The low overall $\kappa{=}0.187$ across all five methods reflects the fundamental tension: permissive methods detect everywhere (including null), conservative methods detect rarely, and moderate methods disagree about boundary cases.
601	This motivates the MMCT consensus approach (\S\ref{sec:mmct}), which aggregates information from all methods while weighting by empirical reliability.
602	
603	\begin{figure}[H]
604	\centering
605	\includegraphics[width=\columnwidth]{figures/fig_per_method_phase_top.pdf}
606	\caption{Per-method FDR-significant pair counts (/8) across contamination levels (Pythia-410M, seed~42, $T{=}10$, fp32). PermG~(d) exhibits the cleanest regime separation---zero detections through $\alpha{=}0.45$, then a steep 0$\to$6 jump at $\alpha{=}0.50$; NaiveXCorr~(a) saturates at 7--8/8 across all levels including null; DiffXCorr~(b) detects signal but cannot separate forward from reverse. The visual contrast across panels illustrates why method choice is itself a primary source of variability ($\kappa{=}0.187$).}
607	\label{fig:per_method_phase}
608	\end{figure}
609	
610	\begin{figure}[H]\ContinuedFloat
611	\centering
612	\includegraphics[width=\columnwidth]{figures/fig_per_method_phase_bottom.pdf}
613	\caption[]{(\textit{continued})}
614	\end{figure}
615	
616	\section{Cross-Seed Consistency at $\alpha{=}0.60$}
617	\label{app:alpha060}
618	
619	The non-monotonic detection gap at $\alpha{=}0.60$ (\S\ref{sec:dose_response}) is consistent across seeds: PermG yields 0/8 FDR-significant forward pairs for both seed~42 (v4 recompilation) and seed~43.
620	An earlier pipeline version (v3, seed~42) reported 3/8; the discrepancy is resolved by the current pipeline version, which corrected FPR calibration.
621	
622	\paragraph{Detailed metrics at $\alpha{=}0.60$.}
623	Despite PermG non-detection, metric drift at $\alpha{=}0.60$ is substantial: token entropy $-28.5\%$ (gen-0: $3.234$, gen-10: $2.311$), ECE $+1561\%$ ($0.0108 \to 0.179$), perplexity $+92.3\%$ ($26.95 \to 51.83$).
624	Raw (pre-FDR) $p$-values are marginal: ECE$\to$distinct-1 $p{=}0.034$, ECE$\to$distinct-2 $p{=}0.047$---both would pass at uncorrected $\alpha{=}0.05$ but fail BH-FDR correction ($q{=}0.05$, 8 simultaneous tests).
625	This indicates that the signal exists but falls below the corrected significance threshold, consistent with the temporal-compression interpretation.
626	
627	\paragraph{Cross-$T$ behavior.}
628	The sync-dip at $\alpha{=}0.60$ persists across observation windows: $T{=}5$: 0/8; $T{=}10$: 0/8 (both s42, s43); $T{=}15$: 0/8 (s42); $T{=}20$: 0/8 (s42), 3/8 (s43, partial dissolution).
629	Full dissolution occurs only at $T{=}25$: PermG 5/8 (s42), $K{\geq}3$ consensus 6/8.
630	The pattern---persistent non-detection for $T{\leq}20$, resolution at $T{=}25$---is consistent with $\sqrt{T}$ power accumulation eventually resolving a compressed (but non-zero) temporal lag.
631	
632	\paragraph{Scale dependence.}
633	Pythia-1.4B does \emph{not} exhibit the sync-dip at $\alpha{=}0.60$: PermG detects 4/8 (s42) and 4/6 (s43) at $T{=}10$, rising to 6/8 and 6/6 at $T{=}15$.
634	This scale-dependence suggests the phenomenon is architecture-specific: at larger scale, the entropy-diversity lag may be structurally wider (more capacity $\to$ slower mode collapse propagation), preventing the temporal compression that produces the dip at 410M.
635	
636	\paragraph{Sigmoid fit impact.}
637	The sigmoid fit excluding $\alpha{=}0.60$ yields $k{=}5.66$, $\alpha_c{=}0.765$, $R^2{=}0.286$; including it degrades $R^2$ to 0.205 and shifts $\alpha_c$ rightward by 0.058, confirming the point is a genuine outlier rather than noise.
638	Predicted detection probability at $\alpha{=}0.60$ under the sigmoid model is $P(\mathrm{det}){=}0.282$, far below the observed 0/8 (0.00), indicating the anomaly cannot be explained by smooth dose-response variation.
639	
640	
641	\section{PPL Threshold Baseline}
642	\label{app:ppl_threshold}
643	
644	A reviewer asked whether a naive perplexity threshold could match entropy's detection timing.
645	We evaluate thresholds at $+10\%$, $+25\%$, $+50\%$, $+100\%$, $+150\%$, and $+200\%$ above the generation-0 baseline PPL (26.95).
646	
647	\paragraph{Threshold-by-threshold results.}
648	The PPL trajectory at $\alpha{=}1.0$ (Pythia-410M, s42) evolves rapidly: gen-0${=}26.95$, gen-1${=}57.42$ ($+113.1\%$), gen-2${=}162.15$ ($+501.9\%$), gen-3${=}279.17$, gen-5${=}508.85$, gen-10${=}1017.81$.
649	All thresholds from $+10\%$ through $+100\%$ trigger at generation~1, because the gen-0$\to$gen-1 jump ($+113.1\%$) exceeds them all.
650	Thresholds at $+150\%$ and $+200\%$ delay triggering to generation~2 (PPL${=}162.15$ exceeds both).
651	
652	\paragraph{Comparison with entropy.}
653	Entropy's advantage over PPL monitoring is operational rather than temporal at $\alpha{=}1.0$:
654	\begin{enumerate}
655	\item \emph{Zero cost}: entropy is computed from the model's output distribution during generation---no held-out evaluation set or separate forward pass required.
656	\item \emph{Direct signal}: entropy detects distributional narrowing (mode collapse) directly; PPL detects its downstream consequence (degraded generalization).
657	\item \emph{Regime sensitivity}: at lower contamination ($\alpha{=}0.50$), entropy drops $18.0\%$ at gen-1 while PPL rises only $21.0\%$ over 10~generations---a PPL threshold calibrated for $\alpha{=}1.0$ would miss $\alpha{=}0.50$ entirely.
658	\end{enumerate}
659	
660	\paragraph{When PPL monitoring suffices.}
661	For production systems where $\alpha$ is expected to be high (e.g., known synthetic data pipelines), a PPL threshold at $+50\%$ provides equivalent detection timing to entropy with the added benefit of measuring a directly user-relevant quantity (generation quality).
662	The operational cost difference becomes relevant only for online monitoring at scale, where computing held-out PPL on every generation adds latency and requires maintaining a clean reference set.
663	
664	
665	\section{PermG Power Analysis}
666	\label{app:power_analysis}
667	
668	We simulate PermG power under a bivariate DGP with linear coupling $\beta$ ($T \in \{6,\ldots,20\}$, 100 replications, 5{,}000 permutations, BH FDR $q{=}0.05$).
669	At $T{=}10$, $\beta_{50}{=}2.0$ (50\% power requires strong coupling); at $T{=}20$, $\beta_{50}$ drops to 0.9 (Table~\ref{tab:beta50}).
670	Power grows faster than $\sqrt{T}$, so the $\sqrt{T}$ formula in \S\ref{sec:theory} is a conservative lower bound.
671	FPR under FDR correction remains ${\leq}2\%$ across all $T$.
672	
673	\paragraph{Detailed power values.}
674	Selected FDR-corrected power levels illustrate the gain from longer observation: at $\beta{=}1.0$, power rises from 0.17 ($T{=}10$) to 0.30 ($T{=}15$) to 0.66 ($T{=}20$); at $\beta{=}2.0$, from 0.51 ($T{=}10$) to 0.92 ($T{=}15$) to 0.98 ($T{=}20$).
675	Raw FPR (before FDR correction) is higher but still controlled: $T{=}6$: 1\%, $T{=}8$: 6\%, $T{=}10$: 9\%, $T{=}15$: 6\%, $T{=}20$: 5\%.
676	The non-monotonic raw FPR peak at $T{=}10$ reflects the discrete-sample properties of permutation tests at small $T$; FDR correction absorbs this variation.
677	
678	\paragraph{$\sqrt{T}$ scaling product.}
679	If power scaled exactly as $\sqrt{T}$, the product $\beta_{50} \cdot \sqrt{T}$ would be constant.
680	Observed values: $T{=}8$: 5.09; $T{=}10$: 6.32; $T{=}15$: 4.65; $T{=}20$: 4.02.
681	The downward trend indicates that power grows faster than $\sqrt{T}$---each additional generation contributes more information than a simple $\sqrt{T}$ model predicts, likely because the cumulative signal (not just instantaneous SNR) drives detection in Granger-type tests.
682	
683	\paragraph{Toda--Yamamoto bootstrap comparison.}
684	TY bootstrap power simulations (200 reps, same DGP) yield substantially lower power at comparable $T$: $T{=}10$ power${=}0.205$ (vs.\ PermG 0.51 at $\beta{=}2.0$), $T{=}20$ power${=}0.409$, with Type~I error rate 8.1\% (above nominal).
685	TY's $d$-augmented lag structure wastes degrees of freedom in short series, explaining its inferior power-FPR tradeoff relative to PermG.
686	
687	\begin{table}[H]
688	\centering
689	\small
690	\caption{PermG power analysis: $\beta_{50}$ (coupling for 50\% power) under BH-FDR correction ($q{=}0.05$, 8 pairs). Dashes: $<$50\% power not reached within $\beta \leq 2.0$.}
691	\label{tab:beta50}
692	\begin{tabular}{lcccc}
693	\toprule
694	$T$ & $\beta_{50}$ & $\beta_{50} \cdot \sqrt{T}$ & FPR (raw) & FPR (FDR) \\
695	\midrule
696	6  & ---  & ---  & 1\% & 0\% \\
697	8  & ---  & ---  & 6\% & 2\% \\
698	10 & 2.0  & 6.32 & 9\% & 2\% \\
699	15 & 1.2  & 4.65 & 6\% & 2\% \\
700	20 & 0.9  & 4.02 & 5\% & 1\% \\
701	\bottomrule
702	\end{tabular}
703	\end{table}
704	
705	
706	\section{Non-Stationarity Robustness Analysis}
707	\label{app:nonstationarity}
708	
709	\begin{figure}[H]
710	\centering
711	\includegraphics[width=\columnwidth]{figures/fig_ar1_diagnostic.pdf}
712	\caption{AR(1) coefficient estimates across five contamination levels (Pythia-410M, seed~42). (a)~Token entropy: raw $\varphi$ transitions from negative ($-0.51$ at $\alpha{=}0.00$) to near-unit-root ($1.00$ at $\alpha{=}1.00$), but first-differencing keeps all values below 0.98. (b)~Distinct-1: raw $\varphi$ is uniformly high ($0.75$--$0.95$) even at null, driven by deterministic trend; first-differencing reduces all to ${\leq}0.24$. Dashed red line: $\varphi{=}0.95$ danger zone.}
713	\label{fig:ar1_diagnostic}
714	\end{figure}
715	
716	Monte Carlo simulation (AR(1) DGP, $T{=}11$, 1{,}000 reps) shows PermG FPR inflates to ${\sim}10\%$ under strong non-stationarity ($\varphi{\geq}0.95$), while first-differencing maintains proper size ($4.2$--$6.6\%$) at the cost of reduced power (Table~\ref{tab:nonstationarity_sim}).
717	Our pipeline applies first-differencing before permutation testing, combining both advantages.
718	Under null conditions ($\alpha{=}0.0$), token entropy exhibits $\varphi{=}-0.51$ (far from the danger zone); first-differencing reduces distinct-1's high raw $\varphi$ ($0.81$--$0.97$, reflecting deterministic trend) to $-0.14$--$0.44$.
719	Our empirical FPR of 4/60 (6.7\%) confirms adequate size control.
720	
721	\begin{table}[H]
722	\centering
723	\small
724	\caption{Size and power under AR(1) DGP ($T{=}11$, 1{,}000 reps). First-differencing maintains nominal size; PermG FPR inflates at $\varphi{\geq}0.95$.}
725	\label{tab:nonstationarity_sim}
726	\resizebox{\columnwidth}{!}{%
727	\begin{tabular}{lcccccc}
728	\toprule
729	& \multicolumn{3}{c}{Size (\%, $\beta{=}0$)} & \multicolumn{3}{c}{Power (\%, $\beta{=}0.6$)} \\
730	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
731	$\varphi$ & Raw GC & First-Diff & PermG & Raw GC & First-Diff & PermG \\
732	\midrule
733	0.50 & 6.4 & 6.6 & 6.8 & 37.7 & 17.7 & 36.8 \\
734	0.95 & 10.0 & 5.9 & 9.5 & 44.3 & 28.7 & 41.5 \\
735	0.99 & 11.2 & 4.2 & 10.7 & 46.4 & 24.6 & 41.7 \\
736	\bottomrule
737	\end{tabular}}
738	\end{table}
739	
740	\paragraph{Empirical AR(1) coefficients.}
741	Table~\ref{tab:empirical_ar1} reports estimated AR(1) coefficients for all metric series under null ($\alpha{=}0.0$) and treatment ($\alpha{=}1.0$) conditions.
742	Under the null, all metrics exhibit $|\varphi| < 0.60$ in raw levels and $|\varphi| < 0.30$ after first-differencing, well within the safe zone.
743	Under treatment, raw distinct-$n$ series reach $\varphi{=}0.81$--$0.97$ (near unit root), but first-differencing reduces these to $\varphi{=}-0.14$--$0.44$---confirming that the deterministic trend, not stochastic persistence, drives the high raw autocorrelation.
744	
745	\begin{table}[H]
746	\centering
747	\small
748	\caption{Empirical AR(1) coefficients (Pythia-410M, 4~seeds). ``Raw'' = levels; ``Diff'' = first-differenced.}
749	\label{tab:empirical_ar1}
750	\resizebox{\columnwidth}{!}{%
751	\begin{tabular}{lcccc}
752	\toprule
753	& \multicolumn{2}{c}{$\alpha{=}0.0$} & \multicolumn{2}{c}{$\alpha{=}1.0$} \\
754	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
755	Metric & Raw $\varphi$ & Diff $\varphi$ & Raw $\varphi$ & Diff $\varphi$ \\
756	\midrule
757	Token entropy & $-0.51$ & $-0.28$ & $0.72$ & $0.15$ \\
758	ECE & $0.31$ & $-0.15$ & $0.95$ & $0.38$ \\
759	Distinct-1 & $0.55$ & $0.12$ & $0.97$ & $0.44$ \\
760	Distinct-2 & $0.48$ & $0.08$ & $0.95$ & $0.31$ \\
761	Perplexity & $0.42$ & $-0.22$ & $0.93$ & $-0.14$ \\
762	\bottomrule
763	\end{tabular}}
764	\end{table}
765	
766	\paragraph{ADF test results.}
767	Augmented Dickey--Fuller tests on first-differenced series reject the unit root hypothesis at $p{<}0.05$ in all 40 series (5~metrics $\times$ 4~seeds $\times$ 2~conditions), confirming that first-order differencing ($d{=}1$) is sufficient and higher-order differencing ($d{\geq}2$) would unnecessarily reduce power (Figure~\ref{fig:differencing_dmax}).
768	
769	\paragraph{Why not KPSS?}
770	We use ADF (null: unit root) rather than KPSS (null: stationarity) because ADF is more conservative for our purpose: rejecting the unit-root null provides positive evidence of stationarity, while KPSS's failure to reject would only indicate insufficient evidence against stationarity.
771	In the short-series regime ($T{\leq}25$), KPSS has limited power; ADF's rejection at $p{<}0.05$ across all differenced series provides stronger evidence.
772	
773	\paragraph{Power cost of first-differencing.}
774	First-differencing eliminates spurious regression but reduces effective power by discarding level information (Table~\ref{tab:diff_power_cost}).
775	Under the AR(1) DGP ($\varphi{=}0.50$, $\beta{=}0.6$), first-differenced PermG achieves 17.7\% power versus 36.8\% for raw PermG---a 52\% relative power reduction.
776	At $\varphi{=}0.95$ the cost narrows (28.7\% vs.\ 41.5\%, 31\% reduction) because the stronger persistence makes the raw test less reliable (inflated FPR).
777	Our pipeline accepts this power cost as a necessary tradeoff: at the empirical autocorrelation levels observed in treatment series ($\varphi{=}0.72$--$0.97$ in raw levels), raw Granger testing would produce ${\sim}10\%$ FPR, invalidating the detection framework.
778	
779	\begin{table}[H]
780	\centering
781	\small
782	\caption{Power cost of first-differencing under simulated AR(1) DGP ($T{=}11$, $\beta{=}0.6$, 1{,}000 reps). The power reduction is the price paid for valid size control.}
783	\label{tab:diff_power_cost}
784	\begin{tabular}{lcccc}
785	\toprule
786	$\varphi$ & Raw power & Diff power & Reduction & Raw FPR \\
787	\midrule
788	0.50 & 36.8\% & 17.7\% & 52\% & 6.8\% \\
789	0.95 & 41.5\% & 28.7\% & 31\% & 9.5\% \\
790	0.99 & 41.7\% & 24.6\% & 41\% & 10.7\% \\
791	\bottomrule
792	\end{tabular}
793	\end{table}
794	
795	The practical consequence: at $T{=}10$, the differencing-induced power loss is the primary bottleneck for detecting weak contamination ($\alpha < 0.50$).
796	Extending observation to $T{=}20$ more than compensates: differenced power at $T{=}20$ exceeds raw power at $T{=}10$ for $\varphi \leq 0.95$, providing both valid size control and superior detection sensitivity.
797	This explains the large detection gains observed in the $T{=}20$ extension (\S\ref{app:t20_comparison}).
798	
799	
800	\section{Shapley Value Analysis}
801	\label{app:shapley}
802	
803	\begin{figure}[H]
804	\centering
805	\includegraphics[width=\columnwidth]{figures/fig_shapley_contribution_top.pdf}
806	\caption{Shapley value decomposition by method. FPR contribution (positive = worse) and FNR contribution (negative = better) are shown for each of the five detection methods. DiffXCorr achieves the best combined Shapley ($-0.299$) but lacks directional separation; among directional methods, PermG ranks best ($-0.141$). NaiveXCorr contributes the most FPR ($+0.609$) due to its inability to distinguish signal from null drift.}
807	\label{fig:shapley_contribution_app}
808	\end{figure}
809	
810	\begin{figure}[H]\ContinuedFloat
811	\centering
812	\includegraphics[width=\columnwidth]{figures/fig_shapley_contribution_bottom.pdf}
813	\caption[]{(\textit{continued})}
814	\end{figure}
815	
816	Shapley values~\citep{shapley1953value} computed over all $2^5{=}32$ coalitions quantify each method's marginal contribution to FPR and FNR (Table~\ref{tab:shapley_6pair}).
817	DiffXCorr achieves the best combined Shapley ($-0.299$) but cannot separate forward from reverse; among directional methods, PermG ranks best ($-0.141$).
818	The 8-pair variant (including MAUVE) yields identical rankings.
819	
820	\begin{table}[H]
821	\centering
822	\small
823	\caption{Shapley value decomposition (6-pair, MAUVE excluded). Combined = FPR + FNR (more negative = better).}
824	\label{tab:shapley_6pair}
825	\begin{tabular}{lccc}
826	\toprule
827	Method & $\phi^{\text{FPR}}$ & $\phi^{\text{FNR}}$ & $\phi^{\text{comb}}$ \\
828	\midrule
829	Naive XCorr          & $+0.609$ & $-0.419$ & $+0.190$ \\
830	\textbf{Diff.\ XCorr}& $\mathbf{+0.007}$ & $\mathbf{-0.306}$ & $\mathbf{-0.299}$ \\
831	Threshold ($3\sigma$) & $+0.111$ & $-0.027$ & $+0.084$ \\
832	Perm.\ Granger       & $+0.039$ & $-0.180$ & $-0.141$ \\
833	Toda--Yamamoto       & $+0.150$ & $-0.069$ & $+0.082$ \\
834	\bottomrule
835	\end{tabular}
836	\end{table}
837	
838	\section{MMCT Weight Robustness Ablation}
839	\label{app:weight_robustness}
840	
841	PermG ranks first among directional methods under all four weighting schemes tested (equal, cap-5, cap-10, FPR-inverse cap-100), confirming the ranking is not an artifact of the weighting scheme.
842	Cap-10 and cap-100 yield identical values (consensus threshold saturates), and equal weighting still gives PermG the best combined Shapley ($-0.152$) among directional methods.
843	
844	\begin{table}[H]
845	\centering
846	\small
847	\caption{PermG combined Shapley ($\phi^{\text{comb}}$) under four weighting schemes. Rankings are invariant to weight choice.}
848	\label{tab:weight_robustness}
849	\begin{tabular}{lcccc}
850	\toprule
851	Method & Equal & Cap-5 & Cap-10 & FPR-inv \\
852	\midrule
853	PermG & $-0.152$ & $-0.148$ & $-0.141$ & $-0.141$ \\
854	DiffXCorr & $-0.285$ & $-0.291$ & $-0.299$ & $-0.299$ \\
855	Threshold & $+0.078$ & $+0.081$ & $+0.084$ & $+0.084$ \\
856	TY & $+0.088$ & $+0.084$ & $+0.082$ & $+0.082$ \\
857	NaiveXCorr & $+0.195$ & $+0.192$ & $+0.190$ & $+0.190$ \\
858	\bottomrule
859	\end{tabular}
860	\end{table}
861	
862	\paragraph{Interpretation.}
863	The FPR-inverse weighting scheme (\S\ref{sec:mmct}) penalizes high-FPR methods by assigning weight $w_k = 1/\max(\widehat{\mathrm{FPR}}_k, \epsilon)$.
864	Under this scheme, NaiveXCorr (FPR${=}94.4\%$) receives weight $w{=}1.06$, while PermG (FPR${=}6.7\%$) receives $w{=}14.9$---a $14{\times}$ differential.
865	Equal weighting gives all methods identical influence, which reduces PermG's advantage but does not change its ranking among directional methods.
866	The invariance across weighting schemes (Table~\ref{tab:weight_robustness}) confirms that PermG's superiority reflects genuine detection properties rather than favorable weighting.
867	
868	\paragraph{Per-pair contribution variability.}
869	Marginal contributions vary substantially across canary$\to$downstream pairs (Table~\ref{tab:shapley_per_pair}).
870	Token entropy$\to$distinct-1 produces the most consistent positive contribution across coalitions (std${=}0.021$), while ECE$\to$perplexity shows the highest variance (std${=}0.089$), reflecting the contemporaneous coupling issue (\S\ref{app:channel_effect_size}).
871	
872	\begin{table}[H]
873	\centering
874	\small
875	\caption{Shapley contribution by canary$\to$downstream pair (PermG, 6-pair basis). $\phi^{\text{FNR}}$ = FNR reduction (more negative = better). Std = standard deviation across all $2^4$ coalitions that include this pair.}
876	\label{tab:shapley_per_pair}
877	\begin{tabular}{lcc}
878	\toprule
879	Pair & Mean $\phi^{\text{FNR}}$ & Std \\
880	\midrule
881	Entropy$\to$Distinct-1 & $-0.042$ & 0.021 \\
882	Entropy$\to$Distinct-2 & $-0.038$ & 0.024 \\
883	ECE$\to$Distinct-1 & $-0.035$ & 0.031 \\
884	ECE$\to$Distinct-2 & $-0.031$ & 0.028 \\
885	Entropy$\to$PPL & $-0.002$ & 0.067 \\
886	ECE$\to$PPL & $-0.001$ & 0.089 \\
887	\bottomrule
888	\end{tabular}
889	\end{table}
890	
891	The four diversity-channel pairs collectively account for 96.2\% of PermG's total FNR reduction, while the two perplexity-channel pairs contribute only 3.8\%---consistent with the channel effect size analysis (\S\ref{app:channel_effect_size}) showing that perplexity channels lack the temporal lead structure required for Granger detection.
892	This concentration motivates a practical simplification: for deployment scenarios where computational cost matters, testing only the four diversity-channel pairs sacrifices less than 4\% of detection sensitivity while halving the multiple testing burden (4~tests instead of 8, reducing the FDR correction penalty).
893	
894	\paragraph{Coalition stability.}
895	PermG's marginal contribution is stable across coalition sizes: when added to a 1-method coalition, its average combined Shapley is $-0.138$ (SE${=}0.015$); when added to a 4-method coalition, $-0.144$ (SE${=}0.008$).
896	The near-zero variation ($\Delta{=}0.006$) confirms that PermG's value is complementary rather than redundant---it provides directional information that no other single method duplicates.
897	DiffXCorr shows the opposite pattern: its marginal contribution \emph{decreases} from $-0.312$ (1-method coalition) to $-0.281$ (4-method coalition) as it becomes partially redundant with NaiveXCorr (both test correlation, differing only in preprocessing).
898	
899	
900	\section{PermG FPR Independence Analysis}
901	\label{app:fpr_independence}
902	
903	\begin{figure}[H]
904	\centering
905	\includegraphics[width=\columnwidth]{figures/fig_fpr_sensitivity.pdf}
906	\caption{Per-seed FPR distribution across detection methods (Pythia-410M, $\alpha{=}0.0$, 10~seeds). Each dot represents one seed's FPR; boxplots show inter-seed variability. PermG FPR concentrates near 0\% (8/10 seeds yield 0 false positives) with two outlier seeds (s45, s50) driving the aggregate 6.7\%. NaiveXCorr exhibits uniformly high FPR (${\geq}83\%$) across all seeds.}
907	\label{fig:fpr_sensitivity}
908	\end{figure}
909	
910	Table~\ref{tab:null_fpr_methods} reports null-control FPR across nine seeds (54 pairs, 6-pair basis); a tenth seed (s51) yields 0~PermG FP, giving pooled 4/60${=}$6.7\% (CI $[1.8\%, 16.2\%]$).
911	All four FP occur in te$\to$distinct pairs in seeds~45/50 (8/10 seeds yield 0~FP).
912	$K{\geq}3$ consensus produces 6/60 FP (10.0\%), of which PermG contributes to only 2.
913	At $T{=}15$, PermG FPR drops to 0/12 (0\%).
914	
915	\begin{figure}[H]
916	\centering
917	\includegraphics[width=\columnwidth]{figures/fig_null_fpr_diagnostic.pdf}
918	\caption{Null-control diagnostic: PermG $p$-value distributions under null ($\alpha{=}0.0$) across 10~seeds. Most seeds show $p$-values uniformly distributed above 0.05 (expected under the null); seeds~45 and 50 exhibit a cluster of low $p$-values in token-entropy$\to$distinct pairs, suggesting occasional null-condition coupling that does not generalize across seeds.}
919	\label{fig:null_fpr_diagnostic}
920	\end{figure}
921	
922	\begin{table}[H]
923	\centering
924	\small
925	\caption{Null-control FPR by method ($\alpha{=}0.0$, BH-FDR $q{=}0.05$). $^\ddagger$PermG: 10~seeds, 60~pairs; other methods: 9~seeds, 54~pairs (s51 6-pair breakdown pending).}
926	\label{tab:null_fpr_methods}
927	\resizebox{\columnwidth}{!}{%
928	\begin{tabular}{llrr}
929	\toprule
930	Method & Criterion & Rejections & FPR (\%) \\
931	\midrule
932	\textbf{Perm.\ Granger}$^\ddagger$ & \textbf{BH-FDR} & \textbf{4/60} & \textbf{6.7} \\
933	Diff.\ XCorr$^\dagger$ & BH-FDR & 8/54 & 14.8 \\
934	Threshold & $3\sigma$ (det.) & 13/54 & 24.1 \\
935	Toda--Yamamoto & BH-FDR & 18/54 & 33.3 \\
936	Naive XCorr & uncorr. & 51/54 & 94.4 \\
937	\bottomrule
938	\multicolumn{4}{l}{\footnotesize $^\dagger$Bidirectional; cannot separate forward from reverse.} \\
939	\end{tabular}}
940	\end{table}
941	
942	\subsection{Per-Seed FPR Breakdown}
943	\label{app:per_seed_fpr}
944	
945	Table~\ref{tab:per_seed_fpr_8pair} reports FPR on a per-seed, per-method basis for the original 3-seed cohort (s42, s43, s44; 8-pair basis including MAUVE), while Table~\ref{tab:per_seed_fpr_6pair} extends to the 6-seed expansion (s45--s51; 6-pair basis excluding MAUVE).
946	
947	\begin{figure}[H]
948	\centering
949	\includegraphics[width=\columnwidth]{figures/fig_bootstrap_fpr.pdf}
950	\caption{Bootstrap confidence intervals for FPR estimates (10{,}000 resamples, 10~seeds). PermG's 95\% CI ($[1.8\%, 16.2\%]$) is the tightest among directional methods; the upper bound remains below Threshold's point estimate (27.8\%). The bootstrap distribution for NaiveXCorr is sharply peaked near 90\%, confirming that its high FPR is systematic rather than driven by individual seed outliers.}
951	\label{fig:bootstrap_fpr}
952	\end{figure}
953	
954	\begin{table}[H]
955	\centering
956	\small
957	\caption{Per-seed FPR (8-pair basis, $\alpha{=}0.0$, Pythia-410M, seeds 42--44). PermG achieves 0/8 on all three seeds; NaiveXCorr ${\geq}7/8$ on all.}
958	\label{tab:per_seed_fpr_8pair}
959	\resizebox{\columnwidth}{!}{%
960	\begin{tabular}{lccccc}
961	\toprule
962	Seed & PermG & DiffXCorr & Threshold & TY & NaiveXCorr \\
963	\midrule
964	42 & 0/8 & 4/8 & 3/8 & 2/8 & 8/8 \\
965	43 & 0/8 & 2/8 & 1/8 & 2/8 & 7/8 \\
966	44 & 0/8 & 3/8 & 2/8 & 0/8 & 7/8 \\
967	\midrule
968	Pooled & 0.0\% & 37.5\% & 25.0\% & 16.7\% & 91.7\% \\
969	\bottomrule
970	\end{tabular}}
971	\end{table}
972	
973	\begin{table}[H]
974	\centering
975	\small
976	\caption{Per-seed PermG FPR (6-pair basis, $\alpha{=}0.0$, seeds 45--51). Two seeds (s45, s50) contribute all 4 false positives; remaining seeds yield 0/6.}
977	\label{tab:per_seed_fpr_6pair}
978	\begin{tabular}{lccl}
979	\toprule
980	Seed & PermG fwd & $K{\geq}3$ & Affected pairs \\
981	\midrule
982	45 & 2/6 & 0/6 & te$\to$d1, te$\to$d2 \\
983	46 & 0/6 & 1/6 & --- \\
984	47 & 0/6 & 0/6 & --- \\
985	48 & 0/6 & 0/6 & --- \\
986	49 & 0/6 & 0/6 & --- \\
987	50 & 2/6 & 2/6 & te$\to$d1, te$\to$d2 \\
988	51 & 0/6 & 0/6 & --- \\
989	\bottomrule
990	\end{tabular}
991	\end{table}
992	
993	The concentration of false positives in token-entropy$\to$distinct pairs at seeds~45 and 50 suggests stochastic null-condition coupling in these specific initializations rather than a systematic calibration failure.
994	$K{\geq}3$ consensus FPR on the 6-pair basis is 6/36${=}$16.7\%; of these 6 false positives, only 2 include PermG (both at s50)---the remaining 4 are driven by high-FPR methods (NaiveXCorr $+$ Threshold $+$ TY) reaching consensus without PermG participation.
995	This decomposition clarifies why $K{\geq}3$ FPR exceeds standalone PermG FPR: the consensus mechanism aggregates false positives from multiple methods rather than filtering them.
996	
997	
998	\section{Sigmoid Transition Shape}
999	\label{app:sigmoid_shape}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b3f9203-5be9-4e5e-bc98-08dd7781d578",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "a44c8f80-e480-4090-b292-00ca2582089a",
  "sourceToolAssistantUUID": "5b3f9203-5be9-4e5e-bc98-08dd7781d578",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T10:49:50.207Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WrbL7hTbsBU7Xhq5fxGWCx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 999,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a44c8f80-e480-4090-b292-00ca2582089a",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3tf6SmGk9YZBJRW2jF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2d773bff-1efe-432c-9ff8-c558340804ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSpDPJ8PWmEvnc5ynTWjpy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13785,
      "cache_read_input_tokens": 69262,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13785
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 124,
          "cache_read_input_tokens": 69262,
          "cache_creation_input_tokens": 13785,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13785,
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

_source line 28 · 2026-05-26T10:49:50.562Z_

<details><summary>↩ Tool result · `toolu_01WrbL7hTbsBU7Xhq5fxGWCx`</summary>

```text
999	\label{app:sigmoid_shape}
1000	
1001	Sigmoid regression on the original 13-point $T{=}10$ grid yields $\alpha_c = 0.483$ (bootstrap 95\% CI $[0.43, 0.56]$) but $k = 478 \pm 475$ ($\mathrm{SE}(k) \approx k$), indicating that the coarse grid constrains the midpoint but not the transition shape.
1002	Dense $\alpha$ sampling (17~values at $T{=}10$) resolves this ambiguity: formal likelihood-ratio testing strongly favors a smooth sigmoid over a literal step function ($\Delta\mathrm{AIC}{=}-110$), with fitted steepness $k{=}15.7$ (95\% CI $[9.4, 28.2]$).
1003	The transition is steep but finite-width, not a literal discontinuity.
1004	This observed steepness exceeds what smooth signal models predict: VAR(1) simulations under H0 (linear, $k{=}6.1$) and H0$'$ (concave, $k{=}4.9$) produce onset sigmoids with $k{=}4.9$--$6.1$ (\S\ref{app:power_sim}), yielding steepness ratios $k_{\mathrm{obs}} / k_{\mathrm{H0}} \approx 2.6$--$3.2$ (CI lower bound ratio ${\approx}2$).
1005	
1006	\paragraph{Combined $T{=}10 + T{=}20$ fit.}
1007	Fitting a single sigmoid to both $T$ values yields $k{=}279.3$ (SE${=}527.6$), $\alpha_c{=}0.451$, $y_{\max}{=}0.75$, AIC${=}79.86$.
1008	The 90\% transition width narrows from $[0.478, 0.487]$ (width$=0.0092$) at $T{=}10$ alone to $[0.443, 0.459]$ (width$=0.0158$) in the combined fit---a leftward shift of $\alpha_c$ by $0.031$ reflecting the $T{=}20$ data's detection at $\alpha{=}0.45$.
1009	The combined $k$ drops by 41.6\% relative to $T{=}10$-only, confirming that the transition appears broader when viewed across observation lengths (different $T$ values yield different effective detection thresholds).
1010	We ultimately do not report the combined sigmoid in the main text because $\alpha{=}0.45$ yields contradictory counts (0/8 at $T{=}10$ vs.\ 5/8 at $T{=}20$), reflecting genuine power dependence rather than a single dose-response curve.
1011	
1012	\paragraph{Alternative functional forms.}
1013	Probit and sigmoid fits produce identical AIC (32.99 at $T{=}10$, 79.86 combined), as expected given that both are sigmoidal CDFs differing only in tail behavior.
1014	A generalized logistic ($+1$ parameter for asymmetry $\nu$) adds $+2$ AIC penalty without improving fit, confirming that a symmetric sigmoid is sufficient.
1015	
1016	\paragraph{Transition width characterization.}
1017	The 90\% transition width---the $\alpha$ range over which detection probability rises from 5\% to 95\%---quantifies the sharpness of the regime boundary (Table~\ref{tab:transition_width}).
1018	
1019	\begin{table}[H]
1020	\centering
1021	\small
1022	\caption{Sigmoid transition width (90\% range) by observation length and signal model. Narrower width indicates sharper regime onset.}
1023	\label{tab:transition_width}
1024	\begin{tabular}{lccc}
1025	\toprule
1026	Setting & Width ($\Delta\alpha$) & $\alpha_c$ & $k$ \\
1027	\midrule
1028	$T{=}10$ observed (13-pt) & 0.009 & 0.483 & 478 \\
1029	$T{=}10$ dense (17-pt) & 0.028 & 0.481 & 15.7 \\
1030	$T{=}10{+}20$ combined & 0.016 & 0.451 & 279 \\
1031	H0 linear simulation & 0.072 & 0.507 & 6.1 \\
1032	H0$'$ concave simulation & 0.090 & 0.521 & 4.9 \\
1033	\bottomrule
1034	\end{tabular}
1035	\end{table}
1036	
1037	\begin{figure}[H]
1038	\centering
1039	\includegraphics[width=\columnwidth]{figures/differencing_dmax.pdf}
1040	\caption{First-differencing order selection diagnostic. The optimal differencing order $d_{\max}$ is evaluated via ADF test statistics across all canary$\to$downstream series at $\alpha{=}1.0$. First-order differencing ($d{=}1$) achieves stationarity in all series (ADF $p{<}0.05$), confirming that higher-order differencing is unnecessary and would incur additional power loss.}
1041	\label{fig:differencing_dmax}
1042	\end{figure}
1043	
1044	The dense-sampling transition width ($\Delta\alpha{=}0.028$, corresponding to $\alpha \in [0.467, 0.495]$) is ${\sim}3{\times}$ narrower than smooth-model predictions (0.072--0.090), confirming the anomalous sharpness.
1045	In practical terms, a difference of $\Delta\alpha{=}0.03$ in contamination fraction determines whether detection is impossible (0\%) or reliable (75\%)---this represents approximately 150 additional synthetic samples out of 5{,}000.
1046	The narrow transition has implications for monitoring systems: slight increases in synthetic data fraction near the boundary produce large changes in detectability, creating a ``cliff effect'' where monitoring transitions from false security to reliable alarm with minimal change in the underlying contamination level.
1047	A system operating at $\alpha{=}0.47$ (undetectable) and drifting to $\alpha{=}0.50$ (detectable) would experience an abrupt shift from zero alarm rate to 75\% alarm rate---a three percentage-point contamination increase produces a qualitative change in monitoring behavior.
1048	
1049	\section{Intervention Threshold Sensitivity}
1050	\label{app:intervention_sensitivity}
1051	
1052	At $\alpha{=}1.0$, all five tested thresholds (5\%--25\%) trigger at generation~1 (entropy drop 40.7\%$\gg$threshold), producing identical outcomes (peak PPL 57.0, final PPL 21.3).
1053	The safe operating band is $[10\%, 22\%]$: below 7.5\% triggers false alarms on $\alpha{=}0.0$ drift; above 22.4\% misses $\alpha{=}0.50$.
1054	
1055	\paragraph{Cross-seed and cross-scale replication.}
1056	The predictive cessation result replicates on seed~43 (bf16 precision): trigger at gen-1 with a milder entropy drop ($-22.5\%$ vs.\ $-40.7\%$ in fp32), peak PPL${=}24.65$ (lower due to bf16 dampening).
1057	On Pythia-1.4B (s42, fp32): trigger at gen-1, entropy drop $-51.9\%$ ($2.946 \to 1.418$), peak PPL spike from $19.68$ to $65.37$, recovery by gen-2 (PPL${=}17.44$), final PPL at gen-10${=}17.6$.
1058	ECE follows the same pattern: $0.007 \to 0.281$ at the spike, recovering to $0.017$ post-intervention.
1059	
1060	\paragraph{Alpha=0.75 predictive intervention.}
1061	At $\alpha{=}0.75$ (fp32, v4 pipeline), predictive cessation also triggers at gen-1, with recovery by gen-2.
1062	Post-intervention PermG detection reaches 6/8 forward, $K{\geq}4{=}6/8$, confirming that the intervention preserves the statistical detection signal while preventing perplexity degradation.
1063	Entropy drift post-intervention is only $-5.7\%$ over 10~generations (vs.\ $-27.6\%$ without intervention), consistent with the generation-1 trigger halting the collapse cascade before downstream metrics respond.
1064	
1065	\paragraph{No-intervention baseline comparison.}
1066	Without intervention at $\alpha{=}1.0$: gen-10 PPL${=}1003.73$, distinct-1${=}0.0704$.
1067	With predictive cessation: gen-10 PPL${=}21.29$, distinct-1${=}0.0844$ ($+19.9\%$ higher diversity).
1068	The intervention reduces peak perplexity by 64\% ($56.99$ vs.\ $157.09$ reactive) and preserves substantially more lexical diversity, though neither intervention strategy fully prevents the initial diversity loss at gen-1.
1069	
1070	\begin{figure}[H]
1071	\centering
1072	\includegraphics[width=\columnwidth]{figures/fig_cusum_monitoring.pdf}
1073	\caption{CUSUM sequential monitoring versus calibrated threshold (Pythia-410M, $\alpha{=}1.0$). Both methods trigger at generation~1 because the entropy drop ($|\Delta x|{>}0.7$) greatly exceeds null variability ($\sigma_0{\approx}0.03$). CUSUM's cumulative memory provides no advantage when the initial signal dominates. The shaded region marks the safe operating band $[10\%, 22\%]$ for threshold-based detection.}
1074	\label{fig:cusum_monitoring}
1075	\end{figure}
1076	
1077	
1078	\section{Channel Effect Size Analysis}
1079	\label{app:channel_effect_size}
1080	
1081	First-differencing retains comparable $|r|$ for both diversity (0.952) and perplexity (1.00) channels, ruling out selective power loss.
1082	The Granger $F$-statistic asymmetry ($20$--$28{\times}$ higher for diversity) reflects temporal structure: diversity channels peak at canary-leading lags (81\% at lag${<}0$, median $-1$), while perplexity peaks at lag${=}0$ (contemporaneous co-movement).
1083	Granger tests correctly assign low $F$ to contemporaneous relationships.
1084	
1085	\paragraph{Lag structure decomposition.}
1086	Table~\ref{tab:lag_structure} reports the cross-correlation peak lag for each canary$\to$downstream channel, illustrating the structural difference that drives Granger detectability.
1087	
1088	\begin{table}[H]
1089	\centering
1090	\small
1091	\caption{Cross-correlation peak lag by channel (Pythia-410M, $\alpha{=}1.0$, 4~seeds). Negative lag = canary leads. Diversity channels show consistent canary-leading structure; perplexity channels peak at lag~0.}
1092	\label{tab:lag_structure}
1093	\begin{tabular}{lccl}
1094	\toprule
1095	Channel & Peak lag & $|r|$ at peak & Structure \\
1096	\midrule
1097	Entropy$\to$Dist-1 & $-1$ & 0.96 & canary leads \\
1098	Entropy$\to$Dist-2 & $-1$ & 0.95 & canary leads \\
1099	ECE$\to$Dist-1 & $-1$ & 0.94 & canary leads \\
1100	ECE$\to$Dist-2 & $-1$ & 0.93 & canary leads \\
1101	Entropy$\to$PPL & $0$ & 0.99 & contemporaneous \\
1102	ECE$\to$PPL & $0$ & 0.98 & contemporaneous \\
1103	\bottomrule
1104	\end{tabular}
1105	\end{table}
1106	
1107	The contemporaneous co-movement of canary$\to$perplexity explains why Granger tests fail ($F{\approx}0$, $p{=}0.99$ after differencing): perplexity and entropy respond to the same underlying distributional shift at the same time step, so neither provides predictive improvement over the other's own history.
1108	This is not a limitation of the test but a correct inference---perplexity is not ``downstream'' of entropy in the temporal sense.
1109	
1110	\paragraph{Fisher Z-transform comparison.}
1111	To formally test whether diversity and perplexity channels differ in lagged correlation magnitude, we apply the Fisher Z-transform to peak cross-correlation coefficients (Table~\ref{tab:fisher_z}).
1112	
1113	\begin{table}[H]
1114	\centering
1115	\small
1116	\caption{Fisher Z-transform comparison of channel correlations (Pythia-410M, $\alpha{=}1.0$, 4~seeds). $Z_{\text{diff}}$ tests whether lagged ($\ell{=}{-}1$) correlation differs between diversity and perplexity channels.}
1117	\label{tab:fisher_z}
1118	\begin{tabular}{lcccc}
1119	\toprule
1120	Comparison & $r_{\text{div}}$ & $r_{\text{ppl}}$ & $Z_{\text{diff}}$ & $p$ \\
1121	\midrule
1122	\emph{Lag${=}0$ (contemp.)} \\
1123	\quad Entropy$\to$ & 0.955 & 0.990 & $-2.13$ & 0.033 \\
1124	\quad ECE$\to$ & 0.935 & 0.980 & $-2.41$ & 0.016 \\
1125	\midrule
1126	\emph{Lag${=}{-}1$ (canary leads)} \\
1127	\quad Entropy$\to$ & 0.952 & 0.812 & $+3.67$ & ${<}0.001$ \\
1128	\quad ECE$\to$ & 0.941 & 0.795 & $+3.89$ & ${<}0.001$ \\
1129	\bottomrule
1130	\end{tabular}
1131	\end{table}
1132	
1133	At lag${=}0$ (contemporaneous), perplexity channels show \emph{higher} correlation than diversity channels ($r{=}0.990$ vs.\ $0.955$, $Z{=}-2.13$, $p{=}0.033$), reflecting the synchronous entropy-perplexity coupling.
1134	At lag${=}-1$ (canary leading by one generation), the pattern reverses decisively: diversity channels achieve $r{=}0.952$ vs.\ perplexity's $r{=}0.812$ ($Z{=}3.67$, $p{<}0.001$).
1135	This reversal explains the Granger $F$-statistic asymmetry: perplexity channels do not have weaker coupling overall, but their coupling is \emph{contemporaneous rather than lagged}.
1136	A Granger test measures whether \emph{past} values of $X$ predict \emph{current} $Y$ beyond $Y$'s own history; contemporaneous coupling produces zero improvement, hence $F \approx 0$.
1137	The Fisher Z analysis confirms that the canary$\to$perplexity non-detection is a correct statistical inference about temporal structure rather than a power limitation.
1138	
1139	\begin{figure}[H]
1140	\centering
1141	\includegraphics[width=\columnwidth]{figures/fig_channel_effect.pdf}
1142	\caption{Channel effect size comparison: Granger $F$-statistic for canary$\to$diversity versus canary$\to$perplexity channels (Pythia-410M, $\alpha{=}1.0$, 4~seeds). Diversity channels produce $20$--$28{\times}$ higher $F$-statistics than perplexity channels, reflecting the temporal structure difference: diversity correlations peak at canary-leading lags (81\% at lag${<}0$), while perplexity correlations are contemporaneous (50\% at lag${=}0$).}
1143	\label{fig:channel_effect}
1144	\end{figure}
1145	
1146	
1147	\section{Mutual Information and Partial Correlation}
1148	\label{app:mi_analysis}
1149	
1150	Gaussian MI lower bound ($\hat{I}_G = -\frac{1}{2}\log_2(1{-}r^2)$) between token entropy and distinct-$n$ remains positive throughout the blind zone (0.010--0.141~bits), confirming coupling exists below PermG's detection threshold.
1151	No discontinuity at $\alpha_c$: detection onset reflects power accumulation, not an information transition.
1152	
1153	\paragraph{MI across the blind zone.}
1154	Table~\ref{tab:mi_blind} reports Gaussian MI between token entropy and distinct-1 at each contamination level below $\alpha_c$.
1155	MI increases monotonically with $\alpha$, confirming that the entropy--diversity coupling strengthens continuously across the blind$\to$detection boundary.
1156	The detection onset at $\alpha_c$ therefore reflects a power threshold (sufficient signal-to-noise for PermG to detect the coupling) rather than a qualitative change in the underlying statistical relationship.
1157	
1158	\begin{table}[H]
1159	\centering
1160	\small
1161	\caption{Gaussian MI lower bound between token entropy and distinct-1 across the blind zone (Pythia-410M, $T{=}10$, seed~42).}
1162	\label{tab:mi_blind}
1163	\begin{tabular}{lcc}
1164	\toprule
1165	$\alpha$ & $\hat{I}_G$ (bits) & PermG \\
1166	\midrule
1167	0.00 & 0.010 & 0/8 \\
1168	0.10 & 0.025 & 0/8 \\
1169	0.25 & 0.048 & 0/8 \\
1170	0.45 & 0.141 & 0/8 \\
1171	0.50 & 0.312 & 6/8 \\
1172	\bottomrule
1173	\end{tabular}
1174	\end{table}
1175	
1176	\subsection{Partial Correlation Analysis}
1177	\label{app:partial_corr}
1178	
1179	\begin{table}[H]
1180	\centering
1181	\small
1182	\caption{Partial correlation controlling for generation. Lagged partial $|r|$ increases after trend removal, confirming genuine temporal precedence.}
1183	\label{tab:partial_corr}
1184	\resizebox{\columnwidth}{!}{%
1185	\begin{tabular}{@{}l cc cc cc cc@{}}
1186	\toprule
1187	& \multicolumn{4}{c}{Contemporaneous} & \multicolumn{4}{c}{Lagged (canary$_{t-1}$)} \\
1188	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
1189	& \multicolumn{2}{c}{Zero-order} & \multicolumn{2}{c}{Partial} & \multicolumn{2}{c}{Zero-order} & \multicolumn{2}{c}{Partial} \\
1190	\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7} \cmidrule(lr){8-9}
1191	$\alpha$ & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. & $\bar{|r|}$ & Sig. \\
1192	\midrule
1193	0.00 & 0.414 & 3/18 & 0.323 & 0/18 & 0.563 & 8/18 & 0.524 & 9/18 \\
1194	0.50 & 0.590 & 9/18 & 0.381 & 2/18 & 0.759 & 12/18 & 0.841 & 17/18 \\
1195	0.75 & 0.636 & 9/18 & 0.521 & 3/18 & 0.831 & 17/18 & 0.913 & 18/18 \\
1196	\bottomrule
1197	\end{tabular}}
1198	\end{table}
1199	
1200	Partial correlations controlling for generation number (Table~\ref{tab:partial_corr}) show that contemporaneous associations drop after trend removal ($\bar{|r|}$: $0.590{\to}0.381$ at $\alpha{=}0.50$), while lagged correlations \emph{strengthen} ($0.759{\to}0.841$), with 35/36 detection-condition pairs retaining significance.
1201	
1202	\begin{figure}[H]
1203	\centering
1204	\includegraphics[width=\columnwidth]{figures/fig_partial_correlation.pdf}
1205	\caption{Partial correlation scatter plots for canary$\to$diversity pairs at $\alpha{=}0.75$ (Pythia-410M). Left: contemporaneous partial correlations drop after controlling for generation trend. Right: lagged partial correlations \emph{strengthen} after trend removal ($\bar{|r|}$: $0.831{\to}0.913$), confirming that the temporal precedence signal is not a shared-trend artifact.}
1206	\label{fig:partial_corr}
1207	\end{figure}
1208	
1209	\paragraph{Interpretation.}
1210	The partial correlation analysis serves two purposes:
1211	(1)~It confirms that the canary$\to$diversity temporal precedence is not driven by a shared trend (generation number): removing the linear trend \emph{strengthens} rather than eliminates the lagged association.
1212	(2)~It shows that the temporal signal grows with contamination level: at $\alpha{=}0.00$, lagged partial $|r|{=}0.524$ (marginal significance); at $\alpha{=}0.75$, lagged partial $|r|{=}0.913$ (universal significance, 18/18).
1213	This monotonic growth parallels the MI analysis and confirms that the blind-zone boundary reflects statistical power rather than a qualitative transition in the coupling structure.
1214	
1215	\begin{figure}[H]
1216	\centering
1217	\includegraphics[width=\columnwidth]{figures/fig_partial_correlation_agg.pdf}
1218	\caption{Aggregated partial correlation analysis across contamination levels. Lagged canary$\to$diversity correlations increase monotonically with $\alpha$ (from $0.524$ at null to $0.913$ at $\alpha{=}0.75$), while contemporaneous correlations plateau. The growing gap between lagged and contemporaneous partial $|r|$ with increasing contamination indicates that the temporal lead signal strengthens with signal-to-noise ratio.}
1219	\label{fig:partial_corr_agg}
1220	\end{figure}
1221	
1222	\paragraph{Null behavior.}
1223	At $\alpha{=}0.00$, 9/18 lagged pairs reach significance despite no synthetic contamination, reflecting fine-tuning drift coupling: both entropy and diversity decline during pure fine-tuning (Table~\ref{tab:drift_summary}), creating a weak temporal association.
1224	These null-condition correlations are substantially weaker than treatment-condition correlations ($0.524$ vs.\ $0.913$), and the 9/18 significance rate is consistent with the expected false positive rate under weak coupling (mid-range $p$-values cluster near the significance boundary).
1225	
1226	
1227	\section{Moment Cascade Analysis}
1228	\label{app:moment_cascade}
1229	
1230	Onset (5\% threshold) occurs at generation~1 for entropy in all 6 conditions and at generation~2 for distinct-$n$ in all 18 pairwise comparisons (Table~\ref{tab:moment_cascade}; Figure~\ref{fig:cascade_onset}).
1231	
1232	\begin{table}[H]
1233	\centering
1234	\small
1235	\caption{Degradation onset generation (5\% threshold) by metric and condition (Pythia-410M, WikiText, fp32). Token entropy reaches onset at generation~1 in all non-null conditions; distinct-$n$ metrics follow at generation~2.}
1236	\label{tab:moment_cascade}
1237	\resizebox{\columnwidth}{!}{%
1238	\begin{tabular}{llcccccc}
1239	\toprule
1240	Seed & $\alpha$ & Entropy & Dist-1 & Dist-2 & Dist-3 & ECE & PPL \\
1241	\midrule
1242	42 & 0.10 & 1 & 2 & 2 & 2 & 2 & --- \\
1243	42 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\
1244	42 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\
1245	43 & 0.25 & 1 & 2 & 2 & 2 & 4 & --- \\
1246	43 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\
1247	43 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\
1248	\bottomrule
1249	\multicolumn{8}{l}{\footnotesize ---: onset not reached within $T{=}10$ generations.} \\
1250	\end{tabular}}
1251	\end{table}
1252	
1253	\begin{figure}[H]
1254	\centering
1255	\includegraphics[width=\columnwidth]{figures/fig_cascade_onset.pdf}
1256	\caption{Cascade onset timeline (Pythia-410M, WikiText, fp32). Entropy and ECE reach onset at generation~1; distinct-$n$ follows at generation~2. The ordering $t_H \leq t_D$ holds across all conditions.}
1257	\label{fig:cascade_onset}
1258	\end{figure}
1259	
1260	ECE shows onset at generation~1 at $\alpha{\geq}0.50$; perplexity never reaches 5\% onset at low contamination ($\alpha{\leq}0.25$).
1261	
1262	\paragraph{Onset threshold sensitivity.}
1263	Table~\ref{tab:onset_threshold_sensitivity} examines how the cascade ordering result depends on the choice of onset threshold (5\%, 10\%, 15\%, 20\%).
1264	
1265	\begin{table}[H]
1266	\centering
1267	\small
1268	\caption{Cascade ordering $t_H \leq t_D$ validity as a function of onset threshold (Pythia-410M, 6 conditions, $\alpha{\geq}0.10$).}
1269	\label{tab:onset_threshold_sensitivity}
1270	\begin{tabular}{lccc}
1271	\toprule
1272	Threshold & $t_H \leq t_D$ & $t_H = t_D$ & $t_H > t_D$ \\
1273	\midrule
1274	5\% & 6/6 & 0/6 & 0/6 \\
1275	10\% & 6/6 & 0/6 & 0/6 \\
1276	15\% & 5/6 & 1/6 & 0/6 \\
1277	20\% & 4/6 & 2/6 & 0/6 \\
1278	\bottomrule
1279	\end{tabular}
1280	\end{table}
1281	
1282	At all thresholds, the ordering $t_H \leq t_D$ is never violated ($t_H > t_D$ in 0/24 cells).
1283	At the strictest threshold (5\%), entropy precedes diversity by exactly one generation in all 6 conditions.
1284	At relaxed thresholds (${\geq}15\%$), some conditions show simultaneous onset ($t_H = t_D$), because the larger threshold absorbs the diversity lag---consistent with the margin condition in Observation~\ref{prop:div_lag}.
1285	
1286	\paragraph{MAUVE cascade position.}
1287	MAUVE~\citep{pillutla2021mauve} onset occurs at generation~2--3, consistently after distinct-$n$ onset (gen-2), establishing a three-phase cascade: $\{H, \mathrm{ECE}\} \to \mathrm{Dist}\text{-}n \to \mathrm{MAUVE}$.
1288	MAUVE's later onset reflects its distributional-comparison nature: it measures the divergence between generated and reference text distributions, which requires substantial lexical collapse before the divergence exceeds the detection threshold.
1289	At $\alpha{=}1.0$, MAUVE floor saturation (${\sim}0.033$) occurs by gen-3--4, after which it becomes uninformative (constant series).
1290	
1291	\paragraph{Perplexity irregularity.}
1292	Perplexity onset is condition-dependent rather than cascade-ordered: at $\alpha{=}0.50$ (s42), PPL onset occurs at gen-4 (delayed relative to entropy gen-1 and diversity gen-2); at $\alpha{=}0.75$, PPL onset is gen-1 (contemporaneous with entropy).
1293	This irregularity is consistent with the first-differencing result: PPL is not temporally downstream of entropy in the Granger sense.
1294	Instead, PPL responds to a different aspect of collapse (cross-entropy on held-out data) that can accelerate or decelerate independently of the entropy-diversity cascade.
1295	
1296	
1297	\subsection{Discretized Entropy Robustness Test}
1298	\label{app:discretized_entropy}
1299	
1300	A potential concern is that PermG may exploit the continuous resolution of token entropy relative to the discrete-valued distinct-$n$ metrics, producing spurious Granger precedence.
1301	We test this by binning continuous entropy into discrete levels and re-running the permutation Granger test.
1302	
1303	For each of 7~experiments at $\alpha{=}1.0$ (spanning Pythia-410M, GPT-2-medium, OPT-1.3B, and Pythia-1.4B), we discretize the entropy time series using equal-width and equal-frequency binning at 5, 10, 15, and 20~bins, then apply the same PermG test (5{,}000 permutations, first-differenced, max lag~1) on binned entropy$\to$distinct-1.
1304	
1305	\begin{table}[H]
1306	\centering
1307	\small
1308	\caption{Discretized entropy Granger test: number of experiments (out of 7) with FDR-significant entropy$\to$distinct-1 at each binning resolution and method. Continuous baseline: 7/7.}
1309	\label{tab:discretized_entropy}
1310	\begin{tabular}{@{}lcc@{}}
1311	\toprule
1312	Bins & Equal-width & Equal-freq \\
1313	\midrule
1314	20 & 7/7 & 7/7 \\
1315	15 & 6/7 & 7/7 \\
1316	10 & 5/7 & 1/7 \\
1317	5  & 3/7 & 0/7 \\
1318	\bottomrule
1319	\end{tabular}
1320	\end{table}
1321	
1322	At ${\geq}15$~bins, Granger precedence is largely preserved (6--7/7) regardless of binning method (Table~\ref{tab:discretized_entropy}).
1323	Signal degradation occurs only at extreme coarsening (${\leq}10$~bins), where equal-frequency binning is particularly destructive because entropy trajectories are right-skewed (sharp generation~0--2 drop followed by a plateau); equal-frequency bins compress the informative early decline into a single bin.
1324	The Pythia-410M reference case retains significance down to 5~equal-width bins ($p{=}0.035$) but loses it under 5~equal-frequency bins ($p{=}0.700$).
1325	
1326	These results confirm that the temporal precedence finding is not solely attributable to continuous measurement resolution: even moderate discretization (${\geq}15$~levels, well below the effective resolution of distinct-$n$) preserves the signal across all tested architectures, though extreme quantization (${\leq}5$~bins) can eliminate it.
1327	
1328	
1329	
1330	\section{Cascade Ordering Theory: Derivations}
1331	\label{app:cascade_theory}
1332	
1333	This section provides the full derivations for Observation~\ref{thm:entropy_leads} and Observation~\ref{prop:div_lag} from \S\ref{sec:cascade}, plus supporting results.
1334	
1335	\begin{assumption}[Mode Amplification]\label{ass:mode_amp}
1336	The training map $\mathcal{T}$ redistributes probability mass from low-probability to high-probability tokens: there exists a threshold $\bar{p}$ such that $\mathcal{T}(p)_i > p_i \Rightarrow p_i \geq \bar{p}$ and $\mathcal{T}(p)_j < p_j \Rightarrow p_j \leq \bar{p}$.
1337	\end{assumption}
1338	
1339	This captures the standard finite-capacity approximation effect: MLE on finite samples from a peaked distribution amplifies modes and suppresses the tail~\citep{shumailov2024curse,dohmatob2024tale}.
1340	
1341	\begin{proposition}[Entropy is a first-order indicator]\label{prop:entropy_first}
1342	Let $p \in \Delta^{V-1}$ and $\delta = \alpha(\mathcal{T}(p) - p)$ be a mode-amplifying perturbation with $\sum_i \delta_i = 0$. Then $\Delta H = H(p+\delta) - H(p) = -\sum_i \delta_i \log p_i + O(\|\delta\|^2) < 0$.
1343	\end{proposition}
1344	
1345	\begin{proof}
1346	Taylor-expanding $H$ around $p$:
1347	$H(p+\delta) = H(p) - \sum_i \delta_i \log p_i - \sum_i \delta_i - \frac{1}{2}\sum_i \delta_i^2/p_i + O(\|\delta\|^3)$.
1348	Since $\sum_i \delta_i = 0$: $\Delta H = -\sum_i \delta_i \log p_i - \frac{1}{2}\sum_i \delta_i^2/p_i + O(\|\delta\|^3)$.
1349	Under mode amplification, tokens gaining mass ($\delta_i > 0$) have $p_i \geq \bar{p}$ (hence $\log p_i \geq \log \bar{p}$) and tokens losing mass ($\delta_j < 0$) have $p_j \leq \bar{p}$ (hence $\log p_j \leq \log \bar{p}$).
1350	Writing $m = \sum_{i:\delta_i > 0} \delta_i$: $-\sum_i \delta_i \log p_i = -m[\overline{\log p}^{+} - \overline{\log p}^{-}] < 0$, where $\overline{\log p}^{\pm}$ are the $|\delta|$-weighted means over gaining/losing tokens.
1351	The second-order Fisher information term $-\frac{1}{2}\sum_i \delta_i^2/p_i$ is always negative, reinforcing the decrease.
1352	\end{proof}
1353	
1354	\begin{proposition}[Diversity is a threshold indicator]\label{prop:div_threshold}
1355	Define the $\epsilon$-effective support $S_\epsilon(p) = |\{i \in [V]: p_i > \epsilon\}|$, where $\epsilon \approx c/N$ is the generation threshold for sample size $N$.
1356	Under the same perturbation $\delta$: $\Delta S_\epsilon = -|\{i: p_i > \epsilon \text{ and } p_i + \delta_i \leq \epsilon\}|$.
1357	This equals zero whenever $\|\delta\|_\infty < \gamma(p,\epsilon) := \min_{i: p_i > \epsilon}(p_i - \epsilon)$.
1358	\end{proposition}
1359	
1360	\begin{proof}
1361	Token $i$ exits the effective support iff $p_i > \epsilon$ and $p_i + \delta_i \leq \epsilon$, requiring $|\delta_i| \geq p_i - \epsilon$.
1362	If $\|\delta\|_\infty < \gamma$, no token satisfies this condition.
1363	\end{proof}
1364	
1365	\medskip
1366	\noindent\textbf{Derivations from the propositions above.}
1367	
1368	\paragraph{Derivation of Observation~\ref{thm:entropy_leads}.}
1369	\emph{Part (a):} Take any mode-amplifying $\delta$ with $\|\delta\|_\infty < \gamma(p,\epsilon)$.
1370	By Proposition~\ref{prop:div_threshold}, $\Delta S_\epsilon = 0$.
1371	By Proposition~\ref{prop:entropy_first}, $\Delta H < 0$.
1372	Such $\delta$ exists for all $\alpha < \gamma / \max_i |\mathcal{T}(p)_i - p_i|$.
1373	\emph{Part (b):} If $\Delta S_\epsilon < 0$, some token $k$ has $p_k > \epsilon$ but $p_k + \delta_k \leq \epsilon$, so $\delta_k < 0$.
1374	Under mode amplification, this implies $p_k \leq \bar{p}$; the total mass transferred to high-probability tokens ensures $\overline{\log p}^+ > \overline{\log p}^-$.
1375	By Proposition~\ref{prop:entropy_first}, $\Delta H < 0$. $\square$
1376	
1377	\paragraph{Derivation of Observation~\ref{prop:div_lag}.}
1378	By the margin condition, at every generation $s \leq t_H$ the perturbation norm $\alpha\|\mathcal{T}(p_s) - p_s\|_\infty$ is less than $\gamma(p_s, \epsilon)$.
1379	By Proposition~\ref{prop:div_threshold}, no token exits the effective support at any $s \leq t_H$, so $\Delta S_\epsilon = 0$ for all $s \leq t_H$.
1380	Since time is discrete, $t_D \geq t_H + 1$. $\square$
1381	
1382	\medskip
1383	\noindent\textbf{ECE co-movement and empirical validation.}
1384	
1385	\paragraph{ECE co-movement (qualitative argument).}
1386	Under conditional mode amplification (peakier $q_\theta(\cdot|x)$ at each generation), per-token conditional entropy $h(x) = H(q_\theta(\cdot|x))$ decreases while confidence $c(x) = \max_y q_\theta(y|x) \geq \exp(-h(x))$ increases.
1387	Averaging: $\bar{H}_t$ decreases, $C_t$ increases.
1388	With accuracy approximately stationary in early collapse ($A_t \approx A_0$), $\Delta\mathrm{ECE} \approx \Delta C_t > 0$ whenever $\Delta\bar{H}_t < 0$.
1389	This argument establishes the direction of co-movement; the quantitative relationship depends on distribution geometry.
1390	$\bar{H}_t$ denotes mean conditional entropy $\mathbb{E}_{x \sim p_{\text{eval}}}[h(x)]$, which differs from the marginal entropy $H_t = -\sum_i p_t(i)\log p_t(i)$ used in Observation~\ref{thm:entropy_leads}; under mode amplification, both decrease monotonically, so the cascade ordering is consistent across both formulations.
1391	
1392	\paragraph{Empirical ECE drift across contamination levels.}
1393	ECE co-movement with entropy is monotonic across all tested $\alpha$ values (Table~\ref{tab:ece_drift}).
1394	At $\alpha{=}0.25$, ECE increases by $+79.2\%$ while entropy decreases by $-4.7\%$---the asymmetry in magnitude reflects ECE's nonlinear dependence on confidence via the $\max$ operator.
1395	At $\alpha{=}1.0$, ECE drift reaches $+3762$--$3821\%$ ($0.0108 \to 0.417$--$0.424$ across seeds), the largest proportional change among all tracked metrics.
1396	
1397	\begin{table}[H]
1398	\centering
1399	\small
1400	\caption{ECE drift across contamination levels (Pythia-410M, WikiText, fp32). ECE increases monotonically with $\alpha$, co-moving with entropy decrease.}
1401	\label{tab:ece_drift}
1402	\begin{tabular}{lccc}
1403	\toprule
1404	$\alpha$ & ECE gen-0 & ECE gen-10 & Drift (\%) \\
1405	\midrule
1406	0.00 & 0.0108 & $0.015{\pm}0.002$ & $+37.6{\pm}14$ \\
1407	0.25 & 0.0108 & $0.019{\pm}0.002$ & $+79.2{\pm}15.9$ \\
1408	0.50 & 0.0108 & $0.087{\pm}0.002$ & $+703{\pm}18$ \\
1409	0.60 & 0.0108 & 0.179 & $+1561$ \\
1410	0.75 & 0.0108 & $0.215{\pm}0.002$ & $+1885{\pm}18$ \\
1411	1.00 & 0.0108 & $0.421{\pm}0.004$ & $+3792{\pm}30$ \\
1412	\bottomrule
1413	\end{tabular}
1414	\end{table}
1415	
1416	ECE onset timing (5\% threshold) at $\alpha{\geq}0.50$ is generation~1, coinciding with entropy onset---consistent with the qualitative argument above that $\Delta\mathrm{ECE} > 0$ whenever $\Delta\bar{H} < 0$.
1417	At $\alpha{=}0.25$, ECE onset delays to generation~4 (seed~43), reflecting the weaker mode amplification signal at low contamination.
1418	At 1.4B scale, ECE follows the same pattern: gen-0 values are lower ($0.007$--$0.008$) but gen-10 values track collapse severity monotonically ($0.145$ at $\alpha{=}0.45$ to $0.268$ at $\alpha{=}0.75$).
1419	
1420	\paragraph{Empirical support for cascade ordering.}
1421	Cascade ordering $t_H \leq t_D$ holds in 14/15 experiments at $\alpha \geq 0.30$ (GPT-2-medium s43: bidirectional).
1422	Table~\ref{tab:cascade_onset} reports onset generations for representative conditions.
1423	
1424	\begin{table}[H]
1425	\centering
1426	\small
1427	\caption{Cascade onset generations (5\% threshold) for representative experiments (Pythia-410M, WikiText, fp32). Phase~1: entropy and ECE ($t_H$, $t_{\mathrm{ECE}}$); Phase~2: diversity ($t_D$, min over distinct-$n$); Phase~3: MAUVE ($t_M$). All conditions confirm the predicted ordering $t_H = t_{\mathrm{ECE}} \leq t_D \leq t_M$.}
1428	\label{tab:cascade_onset}
1429	\begin{tabular}{llcccc}
1430	\toprule
1431	Seed & $\alpha$ & $t_H$ & $t_{\mathrm{ECE}}$ & $t_D$ & $t_M$ \\
1432	\midrule
1433	42 & 0.50 & 1 & 1 & 2 & 3 \\
1434	43 & 0.50 & 1 & 1 & 2 & 2 \\
1435	42 & 0.75 & 1 & 1 & 2 & 3 \\
1436	43 & 0.75 & 1 & 1 & 2 & 2 \\
1437	\bottomrule
1438	\end{tabular}
1439	\end{table}
1440	
1441	
1442	\begin{figure}[H]
1443	\centering
1444	\includegraphics[width=\columnwidth]{figures/fig_detection_surface.pdf}
1445	\caption{Detection rate surface over $\alpha \times T$ (PermG forward, 3~seeds). Dashed curve: fitted boundary $\alpha_c(T)$. The blind zone ($\alpha \leq 0.45$) shrinks as $T$ increases.}
1446	\label{fig:detection_surface}
1447	\end{figure}
1448	
1449	\phantomsection\label{app:alpha_c_proof}
1450	\paragraph{Justification of the empirical boundary model.}
1451	At the detection threshold, $\mathrm{Power}(\alpha_c, T) = \pi^*$.
1452	Since $\alpha_c$ lies below the non-monotonic dip region ($\alpha_c < 0.55$), the signal model applies directly.
1453	From the power function $\mathrm{Power} = \Phi(S(\alpha) \cdot \sqrt{T} / \sigma)$, setting $S(\alpha_c) \cdot \sqrt{T} / \sigma = z^*$ and substituting the signal model $S(\alpha) = c\,\alpha^\beta$ yields $c\,\alpha_c^\beta = z^* \sigma / \sqrt{T}$.
1454	Solving: $\alpha_c(T) = (z^* \sigma / c)^{1/\beta} \cdot T^{-1/(2\beta)}$, giving the stated form with exponent $\eta = 1/(2\beta)$.
1455	
1456	\paragraph{Calibration and consistency.}
1457	Fitting $P(\mathrm{det}|\alpha,T) = \Phi(A \cdot \alpha^\beta \cdot \sqrt{T} - z_0)$ to $T \in \{10, 20\}$ yields $\beta{=}0.24$, $\alpha_\infty{=}0$.
1458	Held-out test ($T \in \{5, 15\}$): MAE${=}0.106$, 95\% CI coverage 6/6.
1459	Leave-one-$T$-out CV (15 cells, sync-dip excluded): MAE${=}0.037$, coverage 15/15.
1460	Profile likelihood yields $\hat{\beta}{=}0.66$ (CI $[0.24, 0.78]$); the wide interval reflects a flat surface.
1461	
1462	\paragraph{Worked example.}
1463	At $\alpha{=}0.50$, $T{=}10$ (seed~42): entropy drops from $3.234$ to $2.649$ at gen-1 ($-18.1\%$), while distinct-1 remains at $0.0968$ (unchanged from gen-0).
1464	At gen-2, distinct-1 drops to $0.0812$ ($-16.1\%$).
1465	The mode amplification perturbation $\delta = 0.50 \cdot (\mathcal{T}(p_0) - p_0)$ satisfies $\|\delta\|_\infty < \gamma(p_0, \epsilon)$ at gen-0 (entropy responds, diversity does not), but at gen-1 the accumulated shift $p_1 = p_0 + \delta$ produces $\|\delta_1\|_\infty > \gamma(p_1, \epsilon)$, causing tokens to exit the effective support and triggering distinct-1 decline.
1466	The one-generation lag is thus explained by the margin condition in Observation~\ref{prop:div_lag}: the margin $\gamma$ is consumed by the gen-0$\to$1 perturbation, and the gen-1$\to$2 perturbation pushes tokens below the generation threshold $\epsilon$.
1467	
1468	\paragraph{Boundary model limitations.}
1469	The empirical boundary $\alpha_c(T) = A \cdot T^{-\eta}$ is fitted to 3--4 data points ($T \in \{5, 10, 15, 20\}$) with 3 free parameters ($A$, $\eta$, and the sub-linear signal exponent $\beta$).
1470	This parametric flexibility means the model can accommodate a wide range of decay shapes, and the $\eta$ CI ($[0.64, 2.08]$) cannot distinguish sub-linear from super-linear decay.
1471	The boundary should therefore be interpreted as a descriptive summary of the observed pattern rather than a predictive model.
1472	Extrapolation beyond $T{=}25$ or below $\alpha{=}0.25$ is not supported by the data.
1473	The qualitative conclusion---detection improves with longer observation---is robust and does not depend on the specific $\eta$ value.
1474	
1475	\paragraph{Sensitivity to the generation threshold $\epsilon$.}
1476	Observation~\ref{thm:entropy_leads} depends on the margin $\gamma(p, \epsilon)$, which in turn depends on the generation threshold $\epsilon \approx c/N$.
1477	Increasing the generation sample size $N$ (from 5{,}000 to 10{,}000) reduces $\epsilon$ by half, widening the margin and extending the entropy-only phase.
1478	In our experiments ($N{=}5{,}000$, effective $\epsilon \approx 2 \times 10^{-4}$), the margin is consumed after one generation at $\alpha{\geq}0.50$, producing the observed $t_D - t_H = 1$ lag.
1479	At lower contamination ($\alpha{=}0.25$), the smaller perturbation preserves the margin longer: the cumulative perturbation does not exceed $\gamma$ until gen-2--3 (Table~\ref{tab:margin_consumption}), explaining the wider entropy-diversity lag at low $\alpha$.
1480	
1481	\begin{table}[H]
1482	\centering
1483	\small
1484	\caption{Margin consumption across contamination levels (Pythia-410M, seed~42). ``Margin gen'' = first generation where cumulative $\|\delta\|_\infty > \gamma$. The diversity lag $t_D - t_H{=}1$ is invariant despite variable margin consumption timing.}
1485	\label{tab:margin_consumption}
1486	\begin{tabular}{lccc}
1487	\toprule
1488	$\alpha$ & $\gamma(p_0, \epsilon)$ & Margin gen & $t_D - t_H$ \\
1489	\midrule
1490	0.10 & $2.3 \times 10^{-3}$ & 3 & 1 \\
1491	0.25 & $2.3 \times 10^{-3}$ & 2 & 1 \\
1492	0.50 & $2.3 \times 10^{-3}$ & 1 & 1 \\
1493	0.75 & $2.3 \times 10^{-3}$ & 1 & 1 \\
1494	1.00 & $2.3 \times 10^{-3}$ & 1 & 1 \\
1495	\bottomrule
1496	\end{tabular}
1497	\end{table}
1498	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d773bff-1efe-432c-9ff8-c558340804ef",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "7a52f4b2-14cb-4556-ab00-797d1f8f48dd",
  "sourceToolAssistantUUID": "2d773bff-1efe-432c-9ff8-c558340804ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-26T10:49:54.404Z_

Now let me read the remaining portions and also look at the experiments_reframe.tex and intro_reframe.tex to check for additional citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a52f4b2-14cb-4556-ab00-797d1f8f48dd",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3u68LdDQivEvQfBSgv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "04412752-2eca-4e5c-80ef-9aa7b50ed02f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BX67b1caWji6tr5Wv2Xpni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14269,
      "cache_read_input_tokens": 83047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14269,
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

_source line 30 · 2026-05-26T10:49:56.648Z_

<details open><summary>🔧 Tool call — Read · `toolu_017BGJgxo6kjgZD9zKzp8uSA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 1498,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04412752-2eca-4e5c-80ef-9aa7b50ed02f",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3u68LdDQivEvQfBSgv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e3c677e-b303-44e1-95d8-1fd746b3574c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BX67b1caWji6tr5Wv2Xpni",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14269,
      "cache_read_input_tokens": 83047,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14269,
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

_source line 31 · 2026-05-26T10:49:56.662Z_

<details><summary>↩ Tool result · `toolu_017BGJgxo6kjgZD9zKzp8uSA`</summary>

```text
1498	
1499	The invariant $t_D - t_H = 1$ across all $\alpha$ levels (despite variable margin consumption timing) reflects the discrete-time nature of the experiment: even when the margin is consumed within a single generation, the diversity response cannot manifest until the next generation's samples are drawn.
1500	This suggests that continuous-time monitoring (within-generation token-level tracking) could reveal a finer-grained cascade with $\Delta t < 1$ generation, but our current experimental design cannot resolve sub-generation dynamics.
1501	
1502	\section{Power Simulation: Shape Comparison}
1503	\label{app:power_sim}
1504	
1505	Simulated PermG detection under linear (H0), concave (H0$'$), and step (H1) signal models (1{,}000 reps, $n_\text{perm}{=}1{,}000$, BH-FDR $q{=}0.05$).
1506	Smooth models produce onset steepness $k{=}4.9$--$6.1$; the observed $k{=}15.7$ is ${\approx}3{\times}$ higher.
1507	The scaling exponent alone cannot distinguish smooth from step boundaries (H0$'$ $\eta{=}1.87$ vs.\ observed $\eta{=}2.08$).
1508	The 6/8 detection ceiling reflects MAUVE floor saturation, not signal limitations.
1509	
1510	\paragraph{Signal model specifications.}
1511	\emph{H0 (linear)}: $S(\alpha) = c \cdot \alpha$, where $c$ is calibrated to produce 50\% detection at $\alpha{=}0.50$, $T{=}10$.
1512	\emph{H0$'$ (concave)}: $S(\alpha) = c \cdot \alpha^{0.5}$, capturing sub-linear signal growth as mode amplification saturates.
1513	\emph{H1 (step)}: $S(\alpha) = 0$ for $\alpha < \alpha_c$, $S(\alpha) = c$ for $\alpha \geq \alpha_c$, representing a genuine phase transition.
1514	The simulated DGP generates bivariate time series $(X_t, Y_t)$ with $Y_t = \beta X_{t-1} + \epsilon_t$ (lag-1 coupling); $\beta$ is set to produce the target $S(\alpha)$ at each contamination level.
1515	
1516	\paragraph{Onset steepness comparison.}
1517	Table~\ref{tab:steepness_comparison} reports fitted sigmoid steepness $k$ for each signal model.
1518	The observed $k{=}15.7$ (CI $[9.4, 28.2]$) exceeds all smooth-model predictions, with the lower CI bound ($k{=}9.4$) still ${\sim}2{\times}$ higher than the smoothest model (H0$'$: $k{=}4.9$).
1519	This excess steepness is consistent with---but does not prove---a genuine discontinuity in the signal structure at $\alpha_c$.
1520	
1521	\begin{table}[H]
1522	\centering
1523	\small
1524	\caption{Onset steepness $k$ under different signal models (1{,}000 reps, PermG, BH-FDR $q{=}0.05$).}
1525	\label{tab:steepness_comparison}
1526	\begin{tabular}{lccc}
1527	\toprule
1528	Model & $k$ & $\eta$ & $k_{\mathrm{obs}}/k$ \\
1529	\midrule
1530	H0 (linear) & 6.1 & 2.08 & 2.6 \\
1531	H0$'$ (concave) & 4.9 & 1.87 & 3.2 \\
1532	H1 (step) & $\infty$ & --- & --- \\
1533	Observed & 15.7 & 2.08 & 1.0 \\
1534	\bottomrule
1535	\end{tabular}
1536	\end{table}
1537	
1538	\begin{figure}[H]
1539	\centering
1540	\includegraphics[width=\columnwidth]{figures/permg_power_curve.pdf}
1541	\caption{PermG power curves as a function of coupling strength $\beta$ for $T \in \{6, 8, 10, 15, 20\}$ (100 replications, 5{,}000 permutations, BH-FDR $q{=}0.05$). Power increases faster than $\sqrt{T}$, confirming that the theoretical $\sqrt{T}$ formula is a conservative lower bound. At $T{=}10$, 50\% power requires $\beta{\geq}2.0$; at $T{=}20$, this drops to $\beta{\approx}0.9$.}
1542	\label{fig:permg_power_curve}
1543	\end{figure}
1544	
1545	\section{T=20 Extension Results}
1546	\label{app:t20_comparison}
1547	
1548	At $\alpha{\geq}0.50$, PermG counts are consistent across $T{=}10$ and $T{=}20$ (6/8 at both), confirming signal-structure determination.
1549	At $\alpha{=}0.45$, the shift from 0/8 ($T{=}10$) to 5/8 ($T{=}20$) supports power-limited (Model~B) over structurally-undetectable (Model~A), lowering $\alpha_c$ below 0.45.
1550	The $\alpha{=}0.60$ dip persists at $T{=}20$ but dissolves at $T{=}25$ (5/8), confirming $\sqrt{T}$ power scaling eventually overcomes it.
1551	Directional selectivity is consistent: forward 6/8, reverse 0/8 at $\alpha \in \{0.50, 0.75, 1.0\}$ across all tested $T$.
1552	
1553	\paragraph{Full $T{=}25$ results.}
1554	Table~\ref{tab:t25_full} reports PermG forward detection counts at $T{=}25$ across contamination levels.
1555	Two key transitions emerge: (1)~$\alpha{=}0.45$ reaches 6/8 (dual-seed: s42 and s43 both 6/8), confirming that the blind-zone boundary has shifted below $\alpha{=}0.45$ at this observation length; (2)~the $\alpha{=}0.60$ sync-dip dissolves (5/8 at $T{=}25$ vs.\ 0/8 at $T{\leq}20$), with $K{\geq}3$ consensus reaching 6/8.
1556	The 6/8 detection ceiling at $\alpha{=}0.45$, $0.50$, $0.75$ matches the ceiling at shorter $T$, suggesting that 2/8 pairs are structurally non-detectable (likely MAUVE-related; MAUVE floor saturation at ${\sim}0.033$ produces near-constant series).
1557	
1558	\begin{table}[H]
1559	\centering
1560	\small
1561	\caption{PermG forward detection at $T{=}25$ (Pythia-410M, fp32). The $\alpha{=}0.45$ blind zone resolves and the $\alpha{=}0.60$ anomaly dissolves.}
1562	\label{tab:t25_full}
1563	\begin{tabular}{lccc}
1564	\toprule
1565	$\alpha$ & PermG fwd & $K{\geq}3$ & Note \\
1566	\midrule
1567	0.45 (s42) & 6/8 & 6/8 & blind$\to$detection \\
1568	0.45 (s43) & 6/8 & 6/8 & cross-seed confirmed \\
1569	0.50 (s42) & 6/8 & 6/8 & stable (matches $T{=}10$) \\
1570	0.60 (s42) & 5/8 & 6/8 & dip dissolves \\
1571	0.75 (s42) & 6/8 & 6/8 & stable \\
1572	0.75 (s43) & 6/8 & 6/8 & cross-seed confirmed \\
1573	\bottomrule
1574	\end{tabular}
1575	\end{table}
1576	
1577	\paragraph{$\alpha{=}0.25$ at extended $T$.}
1578	An unexpected result at $T{=}20$: PermG detects 3/8 at $\alpha{=}0.25$, where $T{=}10$ yields 0/8.
1579	This partial detection at very low contamination suggests that the blind zone is not absolute but power-limited: with sufficient observation length, even weak contamination signals may become detectable.
1580	However, 3/8 falls below the 6/8 reliability threshold we use for confirmed detection, and the result awaits multi-seed replication.
1581	
1582	\begin{figure}[H]
1583	\centering
1584	\includegraphics[width=\columnwidth]{figures/regime_map.pdf}
1585	\caption{Extended regime map including $T \in \{5, 10, 15, 20, 25\}$. The detection boundary shifts leftward with increasing $T$: $\alpha{=}0.45$ transitions from undetectable (0/8 at $T{\leq}10$) to reliable detection (6/8 at $T{=}15$). The $\alpha{=}0.60$ non-monotonic anomaly persists through $T{=}20$ but dissolves at $T{=}25$ (5/8).}
1586	\label{fig:regime_map_extended}
1587	\end{figure}
1588	
1589	\phantomsection\label{app:task_degradation}
1590	\paragraph{Task degradation.}
1591	End-of-training perplexity (gen~10, Pythia-410M, s42) improves at $\alpha{=}0.05$ (20.8 vs.\ 26.6 baseline, mild augmentation effect) but degrades sharply between $\alpha{=}0.50$ (31.3) and $0.52$ (41.1), aligning with PermG detection onset.
1592	
1593	\paragraph{Comprehensive cross-$T$ comparison.}
1594	Table~\ref{tab:cross_t_full} consolidates PermG forward detection across all tested observation windows, providing a complete view of the detection landscape evolution.
1595	
1596	\begin{table}[H]
1597	\centering
1598	\small
1599	\caption{PermG forward detection (/8 pairs) across $T$ and $\alpha$ (Pythia-410M, seed~42, fp32). Detection improves with $T$ at all contamination levels; the blind zone narrows monotonically.}
1600	\label{tab:cross_t_full}
1601	\begin{tabular}{lccccc}
1602	\toprule
1603	$\alpha$ & $T{=}5$ & $T{=}10$ & $T{=}15$ & $T{=}20$ & $T{=}25$ \\
1604	\midrule
1605	0.25 & 0/8 & 0/8 & --- & 3/8 & --- \\
1606	0.45 & 0/8 & 0/8 & 6/8 & 5/8 & 6/8 \\
1607	0.50 & 0/8 & 6/8 & 6/8 & 6/8 & 6/8 \\
1608	0.60 & 0/8 & 0/8 & 0/8 & 0/8 & 5/8 \\
1609	0.75 & 0/8 & 6/8 & 6/8 & 6/8 & 6/8 \\
1610	1.00 & 0/8 & 6/8 & 6/8 & 6/8 & 6/8 \\
1611	\bottomrule
1612	\multicolumn{6}{l}{\footnotesize ---: not tested at this combination.}
1613	\end{tabular}
1614	\end{table}
1615	
1616	Key observations from Table~\ref{tab:cross_t_full}:
1617	\begin{enumerate}
1618	\item $T{=}5$ yields 0/8 across all $\alpha$ levels---insufficient degrees of freedom for PermG detection.
1619	\item The 6/8 ceiling at $\alpha \in \{0.50, 0.75, 1.0\}$ is invariant across $T{=}10$--$25$, confirming signal-structure determination.
1620	\item $\alpha{=}0.45$ traverses the full blind$\to$detection boundary: 0/8 at $T{\leq}10$, 6/8 at $T{=}15$, stable thereafter.
1621	\item $\alpha{=}0.60$ is the only condition requiring $T{=}25$ for detection, with all shorter windows yielding 0/8.
1622	\item $\alpha{=}0.25$ at $T{=}20$ (3/8) is the only sub-threshold result, suggesting that very low contamination may eventually become detectable with sufficiently long observation.
1623	\end{enumerate}
1624	
1625	\paragraph{Directional consistency.}
1626	Across all conditions with ${\geq}6/8$ forward detection, reverse detection remains at 0/8 (with the exception of Pythia-1.4B s43 at $\alpha{\geq}0.60$; \S\ref{app:scale_14b}).
1627	This directional selectivity confirms that the forward-only constraint is not an artifact of a single $T$ value but reflects the genuine temporal asymmetry of the entropy-diversity cascade.
1628	
1629	\paragraph{Detection efficiency metrics.}
1630	Table~\ref{tab:detection_efficiency} reports detection efficiency---defined as the fraction of FDR-significant pairs out of 8---across observation windows, providing a normalized summary of the detection landscape.
1631	
1632	\begin{table}[H]
1633	\centering
1634	\small
1635	\caption{Detection efficiency (fraction of pairs reaching FDR significance) across the $\alpha \times T$ grid (Pythia-410M, seed~42, fp32). Efficiency plateaus at 0.75 for above-onset conditions, indicating a structural detection ceiling at 6/8 pairs.}
1636	\label{tab:detection_efficiency}
1637	\begin{tabular}{lcccc}
1638	\toprule
1639	$\alpha$ & $T{=}10$ & $T{=}15$ & $T{=}20$ & $T{=}25$ \\
1640	\midrule
1641	0.25 & 0.00 & --- & 0.375 & --- \\
1642	0.45 & 0.00 & 0.75 & 0.625 & 0.75 \\
1643	0.50 & 0.75 & 0.75 & 0.75 & 0.75 \\
1644	0.60 & 0.00 & 0.00 & 0.00 & 0.625 \\
1645	0.75 & 0.75 & 0.75 & 0.75 & 0.75 \\
1646	1.00 & 0.75 & 0.75 & 0.75 & 0.75 \\
1647	\bottomrule
1648	\multicolumn{5}{l}{\footnotesize ---: not tested at this combination.}
1649	\end{tabular}
1650	\end{table}
1651	
1652	The 0.75 plateau (6/8 pairs) is remarkably consistent across all conditions above the detection boundary, regardless of $T$ or $\alpha$.
1653	The 2/8 pairs that never reach significance involve MAUVE (floor saturation at ${\sim}0.033$ producing near-constant series) and perplexity (contemporaneous coupling; \S\ref{app:channel_effect_size}).
1654	This structural ceiling has practical implications: extending observation beyond $T{=}10$ at high contamination ($\alpha{\geq}0.50$) provides no additional detection power---the benefit of longer observation is concentrated in the boundary region ($\alpha \in [0.45, 0.60]$).
1655	
1656	\paragraph{Information gain per additional generation.}
1657	The marginal value of each additional generation varies by region.
1658	At $\alpha{=}0.45$, extending from $T{=}10$ to $T{=}15$ produces $+6$ newly significant pairs (information gain rate: $1.2$ pairs/gen); from $T{=}15$ to $T{=}20$, the rate drops to $-0.2$ pairs/gen (slight regression, likely noise).
1659	At $\alpha{=}0.60$ (sync-dip), the marginal value is zero through $T{=}20$ (0 new pairs across 10 additional generations) before producing $+5$ pairs in the $T{=}20{\to}25$ window (rate: $1.0$ pairs/gen).
1660	This non-uniform marginal return implies that a fixed-$T$ deployment strategy is suboptimal: adaptive monitoring that continues observation only when marginal information gain exceeds a threshold would reduce computational cost by 40--60\% without sacrificing detection reliability at high-$\alpha$ operating points.
1661	
1662	\subsection{Cross-Architecture Detection Table}
1663	\label{app:cross_arch_table}
1664	
1665	\begin{table}[H]
1666	\centering
1667	\small
1668	\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$, 15 model-seed combinations across five families---Pythia, GPT-2, OPT, Qwen, SmolLM3---and two domains; Padding-410M is a Pythia variant). PermG fwd $=$ count of FDR-significant forward pairs out of 8.}
1669	\label{tab:generalization}
1670	\resizebox{\columnwidth}{!}{%
1671	\begin{tabular}{lrcl}
1672	\toprule
1673	Model & Params & Domain & PermG fwd \\
1674	\midrule
1675	Pythia-410M    & 410M & Wiki & \textbf{6/8} \\
1676	Pythia-1.4B    & 1.4B & Wiki & 2--6/8$^\dagger$ \\
1677	Pythia-6.9B    & 6.9B & Wiki & \textbf{7/8}$^*$ \\
1678	\addlinespace
1679	GPT-2-medium   & 345M & Wiki & \textbf{6/8}$^\S$ \\
1680	\addlinespace
1681	OPT-1.3B       & 1.3B & Wiki & \textbf{6/8} \\
1682	\addlinespace
1683	Qwen3.5-0.8B   & 0.8B & Wiki & \textbf{8/8} \\
1684	SmolLM3-3B     & 3.0B & Wiki & 3/8$^\ddagger$ \\
1685	Padding-410M   & 410M & Wiki & \textbf{6/8} \\
1686	\addlinespace
1687	Pythia-1B      & 1.0B & C4   & \textbf{8/8} \\
1688	Pythia-1.4B    & 1.4B & C4   & \textbf{8/8} \\
1689	\bottomrule
1690	\multicolumn{4}{l}{\footnotesize $^\dagger$Seed-dep.\ (s42: 2/8, s43: 6/8); 8-pair incl.\ MAUVE} \\
1691	\multicolumn{4}{l}{\footnotesize \phantom{$^\dagger$}(floor ${\sim}0.033$ at 1.4B; 6-pair in Table~\ref{tab:14b_phase}). $^*$bf16. $^\ddagger$ECE-only (ent.\ 0/4).} \\
1692	\multicolumn{4}{l}{\footnotesize $^\S$s42 fp32: 6/8 fwd, 0 rev; s43: 6/8 both; bf16: 0/8.} \\
1693	\multicolumn{4}{l}{\footnotesize 2 seeds each for Pythia-410M/1.4B, GPT-2, OPT, Pythia-1B C4.} \\
1694	\end{tabular}%
1695	}
1696	\end{table}
1697	
1698	\subsection{Cross-Architecture FPR Sensitivity}
1699	\label{app:cross_arch_fpr}
1700	
1701	GPT-2-medium null-condition PermG FPR is 50\% (6/12 pooled, 2~seeds), dramatically higher than Pythia-410M (6.7\%), driven by ${\sim}4{\times}$ stronger null drift (entropy $-20.5\%$ vs.\ $-4.9\%$; distinct-3 $-35.8\%$ vs.\ $-4.9\%$).
1702	$K{\geq}3$ consensus maintains 0\% FPR (0/12) on GPT-2-medium, providing some protection, but standalone PermG requires architecture-specific null calibration.
1703	
1704	The cross-architecture detection heatmap is shown in Figure~\ref{fig:cross_arch_heatmap} (main text).
1705	
1706	\paragraph{GPT-2-medium: precision sensitivity.}
1707	GPT-2-medium at fp32 (seed~42) achieves 6/8 forward detection with 0/8 reverse, matching the Pythia-410M profile.
1708	Switching to bf16 drops detection to 0/8 without changing the underlying collapse dynamics (distinct-1 drift: $-28.4\%$ in both precisions).
1709	The mechanism is quantization noise masking the entropy signal: bf16 entropy time series exhibit ${\sim}2{\times}$ higher inter-generation variance than fp32, pushing PermG $p$-values from $p{<}0.01$ (fp32) to $p{>}0.20$ (bf16).
1710	This failure mode is fully resolved by using fp32 precision; architectures with native bf16 training (e.g., SmolLM3) require separate investigation.
1711	
1712	\paragraph{GPT-2-medium: seed-specific bidirectionality.}
1713	At seed~43, GPT-2-medium detects 6/8 in \emph{both} forward and reverse directions, preventing directional assignment.
1714	This bidirectionality is absent at seed~42 (6/8 forward, 0/8 reverse) and does not appear for any Pythia seed, suggesting it reflects GPT-2's specific learned dynamics rather than a general property of iterative collapse.
1715	Possible explanations include: (1)~GPT-2's attention patterns create feedback loops where diversity changes instantaneously feed back into entropy through the generation process; (2)~seed~43 produces a collapse trajectory where the entropy-diversity lag is below PermG's temporal resolution.
1716	
1717	\paragraph{SmolLM3-3B: entropy decoupling.}
1718	SmolLM3-3B achieves only 3/8 detection, with all significant pairs involving ECE rather than entropy (entropy: 0/4; ECE: 3/4).
1719	This violates the cascade ordering assumption (Observation~\ref{thm:entropy_leads}): in 3/8 conditions, entropy does not monotonically decrease across generations, exhibiting a recovery pattern between gen-3 and gen-5 before resuming decline.
1720	The non-monotonic entropy trajectory breaks the mode amplification assumption underlying the cascade ordering, suggesting that SmolLM3's architecture (likely due to its different attention mechanism or training objective) produces qualitatively different collapse dynamics.
1721	
1722	\paragraph{Domain effects: WikiText vs.\ C4.}
1723	C4-domain experiments (Pythia-1B and Pythia-1.4B) achieve uniformly higher detection rates (8/8) than their WikiText counterparts (6/8 and 2--6/8 respectively).
1724	This domain advantage may reflect C4's greater vocabulary diversity (broader token distribution $\to$ larger effective support $S_\epsilon$), which increases the margin $\gamma$ and produces a cleaner cascade ordering.
1725	Alternatively, WikiText's specialized vocabulary (encyclopedia-style text) may create mode amplification patterns that compress the entropy-diversity lag.
1726	
1727	\paragraph{Deployment recommendations.}
1728	Based on the cross-architecture results, we recommend:
1729	\begin{enumerate}
1730	\item Run null-control calibration on each target architecture before deployment (GPT-2 FPR: 50\% without calibration).
1731	\item Use fp32 precision for the detection pipeline even if training uses mixed precision.
1732	\item Apply $K{\geq}3$ consensus to reduce architecture-specific FPR inflation (0/12 on GPT-2 vs.\ 50\% standalone PermG).
1733	\item Verify monotonic entropy decline on the target architecture; non-monotonic cases (SmolLM3-3B) require ECE-based detection.
1734	\end{enumerate}
1735	
1736	
1737	\section*{Reproducibility Details}
1738	\label{app:reproducibility}
1739	
1740	\paragraph{Compute requirements.}
1741	Each Pythia-410M experiment (10 generations $\times$ 5{,}000 training steps $+$ 5{,}000 generation samples) requires approximately 4 GPU-hours on a single NVIDIA A100 (40GB).
1742	The full experimental matrix (13 $\alpha$ levels $\times$ 4~seeds $\times$ 5 observation windows $+$ cross-architecture) required approximately 800 GPU-hours total.
1743	Statistical analysis (permutation testing, Shapley computation, specification curves) runs on CPU in under 2 hours for the complete dataset.
1744	
1745	\paragraph{Software versions.}
1746	PyTorch 2.1.0, Transformers 4.36.0, Python 3.10.
1747	All experiments use deterministic mode (\texttt{torch.use\_deterministic\_algorithms(True)}) except generation (stochastic sampling), ensuring that training trajectories are reproducible given the same seed.
1748	
1749	\paragraph{Key implementation choices.}
1750	Several implementation decisions affect reproducibility:
1751	\begin{itemize}
1752	\item \emph{Checkpoint strategy}: each generation fine-tunes from the previous generation's checkpoint (not from pretrained $M_0$), implementing true iterative collapse rather than independent fine-tuning.
1753	\item \emph{Generation prompts}: the same 5{,}000 prompt set (sampled once per experiment) is used across all generations within a run, controlling for prompt-selection variance.
1754	\item \emph{Metric computation}: all metrics are computed on the same held-out set across generations; distinct-$n$ uses the full 5{,}000 generated samples (not a subsample).
1755	\item \emph{Pipeline versioning}: results in this paper use the current pipeline version, which corrected FPR calibration errors present in earlier iterations. The corrected pipeline changed PermG detection at $\alpha{=}0.60$ from 3/8 to 0/8 (reported).
1756	\end{itemize}
1757	
1758	\paragraph{Data availability.}
1759	WikiText-103~\citep{merity2017pointer} is publicly available.
1760	Synthetic data generated during experiments is not released (too large), but the generation scripts are included in the code release.
1761	All statistical analysis code, including the five detection methods, MMCT consensus, and specification curve construction, will be released upon acceptance.
1762	
1763	\section*{Use of AI Assistance}
1764	
1765	We used Claude for coding, code drafting, debugging, and language polishing.
1766	
1767	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e3c677e-b303-44e1-95d8-1fd746b3574c",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "77425039-74c1-4fd5-9d3e-1208fc11fc88",
  "sourceToolAssistantUUID": "6e3c677e-b303-44e1-95d8-1fd746b3574c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-26T10:49:56.928Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GpqoZrGDPdAF6xykdgwwuf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77425039-74c1-4fd5-9d3e-1208fc11fc88",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3u68LdDQivEvQfBSgv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c5cb0fbf-9636-479c-9712-900f959fcba3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BX67b1caWji6tr5Wv2Xpni",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14269,
      "cache_read_input_tokens": 83047,
      "output_tokens": 229,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14269
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 229,
          "cache_read_input_tokens": 83047,
          "cache_creation_input_tokens": 14269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14269,
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

_source line 33 · 2026-05-26T10:49:56.932Z_

<details><summary>↩ Tool result · `toolu_01GpqoZrGDPdAF6xykdgwwuf`</summary>

```text
1	\section*{Ethical Considerations}
2	
3	This work uses only publicly available datasets (WikiText-103) and open-weight models (Pythia, GPT-2, OPT, Qwen2.5, SmolLM3); no private data, human subjects, or crowd-sourced annotations are involved.
4	We do not release models trained on synthetic data, as they exhibit reduced diversity and calibration.
5	Our finding of a blind zone below $\alpha_c \approx 0.50$, where substantial quality degradation proceeds undetected, highlights a practical risk: practitioners relying solely on canary-based monitoring may receive false assurance that their training pipelines are uncontaminated.
6	We encourage pairing statistical detection with complementary safeguards such as data provenance tracking and periodic human evaluation.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5cb0fbf-9636-479c-9712-900f959fcba3",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "8661dcbc-ef76-41a5-8f94-c781c9cee628",
  "sourceToolAssistantUUID": "c5cb0fbf-9636-479c-9712-900f959fcba3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-26T10:50:00.992Z_

Now I have all the content. Let me search for the bib entries using WebSearch to verify each one. I'll start with the higher-risk entries (2025-2026 papers, "and others" entries).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8661dcbc-ef76-41a5-8f94-c781c9cee628",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3uZeYfx7vrFw1ioQ7K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "43570840-46b1-4078-b02e-d7b92d5798a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfQkpov3miKKJSsfHKxmGw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7985,
      "cache_read_input_tokens": 97316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7985,
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

_source line 35 · 2026-05-26T10:50:01.242Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Fu6QnkGHssorhsztHHyHWH`</summary>

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
  "parentUuid": "43570840-46b1-4078-b02e-d7b92d5798a0",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3uZeYfx7vrFw1ioQ7K",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3f76b967-aa18-428b-8553-4da54e7a8383",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfQkpov3miKKJSsfHKxmGw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7985,
      "cache_read_input_tokens": 97316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7985,
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

_source line 36 · 2026-05-26T10:50:01.244Z_

<details><summary>↩ Tool result · `toolu_01Fu6QnkGHssorhsztHHyHWH`</summary>

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
  "parentUuid": "3f76b967-aa18-428b-8553-4da54e7a8383",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "7b7b5c54-ac5c-4105-9dca-0411f82d7fe8",
  "sourceToolAssistantUUID": "3f76b967-aa18-428b-8553-4da54e7a8383",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-26T10:50:04.716Z_



Now let me verify the bib entries systematically. I'll start with the highest-risk ones (2025-2026 papers, incomplete authors, arXiv preprints).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b7b5c54-ac5c-4105-9dca-0411f82d7fe8",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3utZ6g1BD28k6fdiva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "55e1a759-668c-4d2e-a7f8-2681dd826bde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV5eQ5hnac89uPxypoe8SS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 105301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 650,
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

_source line 38 · 2026-05-26T10:50:05.672Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jf35TKiMsftuin591f9978`</summary>

```json
{
  "query": "arXiv 2605.00435 \"Escaping Mode Collapse\" Du Tanaka-Ishii 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55e1a759-668c-4d2e-a7f8-2681dd826bde",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3utZ6g1BD28k6fdiva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dee6c4dd-2b3d-430d-974e-9d325114aea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV5eQ5hnac89uPxypoe8SS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 105301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 650,
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

_source line 39 · 2026-05-26T10:50:06.606Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NdDjQj3JYRQWp2U3m6KyuD`</summary>

```json
{
  "query": "arXiv 2510.05133 \"Characterizing Model Behavior Under Synthetic Data Training\" 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dee6c4dd-2b3d-430d-974e-9d325114aea2",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3utZ6g1BD28k6fdiva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ddd3fcac-d3fa-409e-8e0d-5613686a8ed9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV5eQ5hnac89uPxypoe8SS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 105301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 650,
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

_source line 40 · 2026-05-26T10:50:07.611Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ELom5ePSh7m22qmoE5k3gf`</summary>

```json
{
  "query": "arXiv 2410.12341 \"Learning by Surprise Surplexity\" Gambetta 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddd3fcac-d3fa-409e-8e0d-5613686a8ed9",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3utZ6g1BD28k6fdiva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "80a33839-832f-472d-b492-fb7aab20b682",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV5eQ5hnac89uPxypoe8SS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 105301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 650,
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

_source line 41 · 2026-05-26T10:50:08.612Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H3s83KoDs8JadkDnHfNbk4`</summary>

```json
{
  "query": "arXiv 2601.03385 SIGMA \"Scalable Spectral Insights LLM Model Collapse\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80a33839-832f-472d-b492-fb7aab20b682",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3utZ6g1BD28k6fdiva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60f1cfaf-9d83-4cf1-aeb4-284615141013",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV5eQ5hnac89uPxypoe8SS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 105301,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 650,
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

_source line 42 · 2026-05-26T10:50:09.088Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GYZKcTfBQB3vdqKDdrTcGB`</summary>

```json
{
  "query": "arXiv 2512.12381 \"Entropy Collapse Universal Failure Mode\" Truong 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60f1cfaf-9d83-4cf1-aeb4-284615141013",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3utZ6g1BD28k6fdiva",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "846e170a-581d-44d8-af32-10ae443e3c88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HV5eQ5hnac89uPxypoe8SS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 650,
      "cache_read_input_tokens": 105301,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 650
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 367,
          "cache_read_input_tokens": 105301,
          "cache_creation_input_tokens": 650,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 650,
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

_source line 43 · 2026-05-26T10:50:14.826Z_

<details><summary>↩ Tool result · `toolu_01Jf35TKiMsftuin591f9978`</summary>

```text
Web search results for query: "arXiv 2605.00435 "Escaping Mode Collapse" Du Tanaka-Ishii 2026"

Links: [{"title":"[2605.00435] Escaping Mode Collapse in LLM Generation via Geometric Regulation","url":"https://arxiv.org/abs/2605.00435"},{"title":"Escaping Mode Collapse in LLM Generation via Geometric Regulation","url":"https://arxiv.org/html/2605.00435"},{"title":"Kumiko Tanaka-Ishii's research works | Waseda University and other places","url":"https://www.researchgate.net/scientific-contributions/Kumiko-Tanaka-Ishii-8156212"},{"title":"[2510.16657] Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence","url":"https://arxiv.org/abs/2510.16657"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"[1707.04848] Do Neural Nets Learn Statistical Laws behind Natural Language?","url":"https://arxiv.org/abs/1707.04848"},{"title":"[2605.08127] Ion-Optical Tuning of the Large Acceptance Spectrometer for Improved Angular Resolution and Acceptance","url":"https://arxiv.org/abs/2605.08127"},{"title":"[2605.19331] Locality in effective field theory for inflationary soft modes","url":"https://arxiv.org/abs/2605.19331"}]

Perfect! I found the paper. Here's what the search revealed:

The paper "Escaping Mode Collapse in LLM Generation via Geometric Regulation" by Xin Du and Kumiko Tanaka-Ishii (arXiv:2605.00435) was submitted on May 1, 2026.

**Key findings from the abstract:**

Mode collapse is a persistent challenge in generative modeling and appears in autoregressive text generation as behaviors ranging from explicit looping to gradual loss of diversity and premature trajectory convergence.

The authors take a dynamical-systems view and reinterpret mode collapse as reduced state-space accessibility caused by geometric collapse—during generation, the model's internal trajectory becomes confined to a low-dimensional region of its representation space. They argue that mode collapse is not purely a token-level phenomenon and cannot be reliably solved by symbolic constraints or probability-only decoding heuristics.

The authors propose Reinforced Mode Regulation (RMR), a lightweight, online state-space intervention that regulates dominant self-reinforcing directions in the Transformer value cache (implemented as low-rank damping).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dee6c4dd-2b3d-430d-974e-9d325114aea2",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "9513c519-3deb-499e-95f3-2294503b4b41",
  "sourceToolAssistantUUID": "dee6c4dd-2b3d-430d-974e-9d325114aea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-26T10:50:17.492Z_

<details><summary>↩ Tool result · `toolu_01NdDjQj3JYRQWp2U3m6KyuD`</summary>

```text
Web search results for query: "arXiv 2510.05133 "Characterizing Model Behavior Under Synthetic Data Training" 2025"

Links: [{"title":"Characterizing Model Behavior Under Synthetic Data Training:","url":"https://www.arxiv.org/pdf/2510.05133"},{"title":"[2510.05133] Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios","url":"https://arxiv.org/abs/2510.05133"},{"title":"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios","url":"https://arxiv.org/html/2510.05133"},{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls","url":"https://arxiv.org/html/2510.01631v1"},{"title":"Demystifying Synthetic Data in LLM Pre-training:","url":"https://arxiv.org/pdf/2510.01631"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/html/2404.05090v1"},{"title":"1 INTRODUCTION","url":"https://arxiv.org/html/2510.08095v2"},{"title":"High-dimensional Analysis of Synthetic Data Selection","url":"https://arxiv.org/html/2510.08123v1"}]

I found the paper you're looking for! Here are the key details about arXiv 2510.05133:

## Paper Overview

"Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios" presents a controlled empirical study examining model performance, calibration, and output characteristics when trained on varying synthetic-to-external data ratios.

## Methodology

The study uses the Pythia model suite (410M-12B parameters) across five diverse tasks, evaluating models after one to three training iterations with synthetic data proportions ranging from 0-50%.

## Key Findings

The key findings include: models maintain stable performance with up to 20% synthetic data, but degradation accelerates beyond 30%; larger models (6.9B-12B) show greater robustness to synthetic data than smaller models (410M-1.4B); calibration degradation precedes accuracy loss, providing an early warning signal; and task characteristics matter, with reasoning tasks degrading faster than retrieval tasks.

## Research Questions

The paper investigates four concrete questions: how model performance varies with synthetic data proportion (0-50%), whether larger models respond differently to synthetic data, whether different task types show different sensitivity to synthetic data training, and whether metrics that degrade before task performance drops can enable proactive monitoring.

The paper was published on October 1, 2025, and is available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ddd3fcac-d3fa-409e-8e0d-5613686a8ed9",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "c12aa87a-8027-4e67-b1a3-4ea0a88bda10",
  "sourceToolAssistantUUID": "ddd3fcac-d3fa-409e-8e0d-5613686a8ed9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-26T10:50:17.515Z_

<details><summary>↩ Tool result · `toolu_01ELom5ePSh7m22qmoE5k3gf`</summary>

```text
Web search results for query: "arXiv 2410.12341 "Learning by Surprise Surplexity" Gambetta 2024"

Links: [{"title":"[2410.12341] Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/abs/2410.12341"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/html/2410.12341"},{"title":"Computer Science Oct 2024","url":"https://arxiv.org/list/cs/2024-10?skip=6075&show=2000"},{"title":"[2410.12341v1] A linguistic analysis of undesirable outcomes in the era of generative AI","url":"https://www.arxiv.org/abs/2410.12341v1"},{"title":"Artificial Intelligence Mar 2024","url":"https://web3.arxiv.org/list/cs.AI/2024-03?skip=2400&show=25"},{"title":"arXiv:2410.12509v1 [cs.AI] 16 Oct 2024","url":"https://arxiv.org/pdf/2410.12509"},{"title":"arXiv:2410.20922v1 [cs.AI] 28 Oct 2024","url":"https://arxiv.org/pdf/2410.20922"}]

I found the paper! Here are the results for arXiv 2410.12341:

**Title:** Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI

**Authors:** Daniele Gambetta, Gizem Gezici, Fosca Giannotti, Dino Pedreschi, Alistair Knott, Luca Pappalardo

**Subject Areas:** Computation and Language (cs.CL) and Artificial Intelligence (cs.AI)

**Overview:** The paper addresses "autophagy"—when generative AI models are retrained on their own outputs—which leads to model collapse, a progressive loss of performance and diversity across generations.

**Key Contribution:** The paper introduces new measures that characterise collapse directly from a model's next-token probability distributions, rather than from properties of AI-generated text.

**Proposed Solution:** The paper proposes filtering training items by high surplexity, maximising the surprise of the model. A key advantage of this approach is that it does not require verifying whether a document is human-authored.

**Submission Status:** The paper was submitted on October 16, 2024, with the latest revision on September 2, 2025 (version 3).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80a33839-832f-472d-b492-fb7aab20b682",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "5aa110b8-ddda-475a-bb22-1a3c1275f95b",
  "sourceToolAssistantUUID": "80a33839-832f-472d-b492-fb7aab20b682",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-26T10:50:18.281Z_

<details><summary>↩ Tool result · `toolu_01H3s83KoDs8JadkDnHfNbk4`</summary>

```text
Web search results for query: "arXiv 2601.03385 SIGMA "Scalable Spectral Insights LLM Model Collapse" 2026"

Links: [{"title":"[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/abs/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/html/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Collapse","url":"https://arxiv.org/html/2601.03385v1"},{"title":"SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://www.arxiv.org/pdf/2601.03385"},{"title":"Rohan Paul on X: \"The authors measure LLM health by sampling embeddings and checking whether the meaning space keeps shrinking over training cycles. SIGMA spots LLM collapse early by measuring how much their sentence embedding space shrinks during self training. Recursive training on model https://t.co/ixJmA3N4y7\" / X","url":"https://x.com/rohanpaul_ai/status/2011373977176846463/photo/1"},{"title":"[2601.11042v1] Spectral Characterization and Mitigation of Sequential Knowledge Editing Collapse","url":"https://arxiv.org/abs/2601.11042v1"},{"title":"[2601.02080] The Homogeneity Trap: Spectral Collapse in Doubly-Stochastic Deep Networks","url":"https://arxiv.org/abs/2601.02080"},{"title":"[2601.08393] Controlled LLM Training on Spectral Sphere","url":"https://arxiv.org/abs/2601.08393"},{"title":"On the Fundamental Limits of LLMs at Scale","url":"https://arxiv.org/html/2511.12869v2"}]

I found the paper! Here's what I found about arXiv 2601.03385:

## SIGMA: Scalable Spectral Insights for LLM Model Collapse

SIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix.

**The Problem It Addresses:**
The rapid adoption of synthetic data for training Large Language Models (LLMs) has introduced the technical challenge of "model collapse"—a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality.

**Key Technical Approach:**
By deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the contraction of the representation space. The stochastic formulation enables scalable estimation of these bounds, making the framework applicable to large-scale foundation models.

**Authors and Submission:**
The paper was submitted on January 6, 2026 with the latest version (v3) revised on March 23, 2026. The authors include Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, and Alexander Aue.

The paper provides both theoretical analysis and practical methods for detecting and monitoring LLM model collapse through spectral analysis of embedding spaces.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60f1cfaf-9d83-4cf1-aeb4-284615141013",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "1aaf311b-5416-4951-bd39-cfe379708272",
  "sourceToolAssistantUUID": "60f1cfaf-9d83-4cf1-aeb4-284615141013",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T10:50:20.129Z_

<details><summary>↩ Tool result · `toolu_01GYZKcTfBQB3vdqKDdrTcGB`</summary>

```text
Web search results for query: "arXiv 2512.12381 "Entropy Collapse Universal Failure Mode" Truong 2025"

Links: [{"title":"[2512.12381] Entropy Collapse: A Universal Failure Mode of Intelligent Systems","url":"https://arxiv.org/abs/2512.12381"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems","url":"https://arxiv.org/pdf/2512.12381"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems Exact Phase Transition Analysis, First-Order Discontinuity, and Two Universality Classes","url":"https://arxiv.org/html/2512.12381"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems","url":"https://www.researchgate.net/publication/398720042_Entropy_Collapse_A_Universal_Failure_Mode_of_Intelligent_Systems"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.12381v1"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems by Truong Xuan Khanh, Truong Quynh Hoa :: SSRN","url":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6084126"},{"title":"(PDF) Entropy Collapse: A Universal Failure Mode of Intelligent Systems","url":"https://www.researchgate.net/publication/398655931_Entropy_Collapse_A_Universal_Failure_Mode_of_Intelligent_Systems"},{"title":"(PDF) Entropy Game Theory: Entropy-Conditioned Incentives, Threshold Collapse, and the Governance of Strategic Diversity","url":"https://www.researchgate.net/publication/398929807_Entropy_Game_Theory_Entropy-Conditioned_Incentives_Threshold_Collapse_and_the_Governance_of_Strategic_Diversity"},{"title":"Clip-Low Increases Entropy and Clip-High Decreases Entropy in Reinforcement Learning of Large Language Models | OpenReview","url":"https://openreview.net/forum?id=2ZflH67Uof"},{"title":"why model randomness (entropy) collapses during ...","url":"https://www.facebook.com/0xSojalSec/posts/why-model-randomness-entropy-collapses-during-reinforcement-learning-for-reasoni/1375333587454374/"}]

Based on the search results, here's what I found about arXiv paper 2512.12381:

## Paper Overview

The paper is titled "Entropy Collapse: A Universal Failure Mode of Intelligent Systems" by Truong Xuan Khanh and one co-author (Truong Quynh Hoa).

## Main Findings

The paper proves that entropy collapse - the irreversible contraction of effective state space when feedback amplification alpha exceeds novelty regeneration beta - is a first-order (discontinuous) phase transition.

The authors show this fails for feedback-amplified adaptive systems - specifically, their work contradicts the foundational assumption that critical transitions in complex systems are second-order phenomena preceded by early warning signals.

## Key Results

The paper provides four exact results, including:

- A threshold of alpha_c(beta) = 1/(1-beta), derived from the Jacobian spectrum of the Multiplicative-Weights operator
- A discontinuity where the entropy order parameter jumps Delta m_0 = 0.698 at the critical point, with hysteresis of approximately 2.73 nats (up to 3.9 nats in simulations) and no pre-transition warning

## Broader Context

The paper identifies entropy collapse as a universal dynamical mechanism through which intelligent systems transition from high-entropy adaptive regimes to low-entropy rigid regimes as feedback amplification overwhelms the system's bounded capacity to regenerate novelty.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "846e170a-581d-44d8-af32-10ae443e3c88",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "e42312e5-6976-407c-b06a-7c4ee79abe33",
  "sourceToolAssistantUUID": "846e170a-581d-44d8-af32-10ae443e3c88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-26T10:50:23.828Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WcYCRc3JrPHvSykZTpcCB7`</summary>

```json
{
  "query": "arXiv 2410.04840 \"Strong Model Collapse\" Dohmatob Feng Subramonian Kempe ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e42312e5-6976-407c-b06a-7c4ee79abe33",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3wGYhfwvAimgUDVkQa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "11921edd-f89e-4ce5-b9e1-cdb60de5bc8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXFXrdH5wrcYwoeTPxdkYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4465,
      "cache_read_input_tokens": 105951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4465,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 49 · 2026-05-26T10:50:24.763Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ST3V8nHLk9Y6xfzMxCP9z7`</summary>

```json
{
  "query": "arXiv 2503.03150 \"Position Model Collapse Does Not Mean What You Think\" Schaeffer Kazdan 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11921edd-f89e-4ce5-b9e1-cdb60de5bc8a",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3wGYhfwvAimgUDVkQa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a54ec626-262d-4e7d-8382-14457347d91f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXFXrdH5wrcYwoeTPxdkYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4465,
      "cache_read_input_tokens": 105951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4465,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 50 · 2026-05-26T10:50:26.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R6aN2nPT9zc6JUJpSLDzd2`</summary>

```json
{
  "query": "arXiv 2502.15654 \"Machine-generated text detection prevents language model collapse\" Drayson 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a54ec626-262d-4e7d-8382-14457347d91f",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3wGYhfwvAimgUDVkQa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "214f306e-a23e-4e3d-9857-ab4485cd3826",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXFXrdH5wrcYwoeTPxdkYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4465,
      "cache_read_input_tokens": 105951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4465,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 51 · 2026-05-26T10:50:27.152Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017L7quwRC7cHmJGSjbB5PF7`</summary>

```json
{
  "query": "arXiv 2601.09001 \"Entropy Sentinel\" Buffa Del Corro 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "214f306e-a23e-4e3d-9857-ab4485cd3826",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3wGYhfwvAimgUDVkQa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "681fcb6a-b550-4e3f-a257-5a6636a8456e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXFXrdH5wrcYwoeTPxdkYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4465,
      "cache_read_input_tokens": 105951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4465,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 42,
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

_source line 52 · 2026-05-26T10:50:27.710Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BZcknWK7SnoBw7aKP7uYQk`</summary>

```json
{
  "query": "\"Dynamic Center-Edge Sampling\" \"Countering Model Collapse\" Zhu Xie Electronics 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "681fcb6a-b550-4e3f-a257-5a6636a8456e",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3wGYhfwvAimgUDVkQa",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f979ed8-7b3b-4e25-bbbe-c1ad8d84ff46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VXFXrdH5wrcYwoeTPxdkYt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4465,
      "cache_read_input_tokens": 105951,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4465
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 336,
          "cache_read_input_tokens": 105951,
          "cache_creation_input_tokens": 4465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4465,
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

_source line 53 · 2026-05-26T10:50:31.528Z_

<details><summary>↩ Tool result · `toolu_01WcYCRc3JrPHvSykZTpcCB7`</summary>

```text
Web search results for query: "arXiv 2410.04840 "Strong Model Collapse" Dohmatob Feng Subramonian Kempe ICLR 2025"

Links: [{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"Strong Model Collapse","url":"https://arxiv.org/html/2410.04840.pdf"},{"title":"Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗","url":"https://arxiv.org/pdf/2410.04840"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Strong Model Collapse","url":"https://www.emergentmind.com/papers/2410.04840"},{"title":"Strong Model Collapse | Request PDF","url":"https://www.researchgate.net/publication/384700001_Strong_Model_Collapse"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v2"},{"title":"ICLR Poster Strong Model Collapse","url":"https://iclr.cc/virtual/2025/poster/32070"}]

I found the paper! Here's what I can tell you about it:

## "Strong Model Collapse" - arXiv 2410.04840

The paper is authored by Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, and Julia Kempe. The paper was submitted on October 7, 2024, and has been published as a conference paper at ICLR 2025.

### Main Contribution

Within the scaling laws paradigm, which underpins the training of large neural networks like ChatGPT and Llama, the paper considers a supervised regression setting and establishes a strong form of the model collapse phenomenon, a critical performance degradation due to synthetic data in the training corpus.

### Key Findings

The results show that even the smallest fraction of synthetic data (e.g., as little as 1 per 1000) can still lead to model collapse: larger and larger training sets do not enhance performance. 

The paper further investigates whether increasing model size, an approach aligned with current trends in training large language models, exacerbates or mitigates model collapse.

The paper is available at https://arxiv.org/abs/2410.04840 and has been officially published in the ICLR 2025 proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11921edd-f89e-4ce5-b9e1-cdb60de5bc8a",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "18af6bf1-d680-4dde-9cdd-ee38eebe78bb",
  "sourceToolAssistantUUID": "11921edd-f89e-4ce5-b9e1-cdb60de5bc8a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-26T10:50:35.160Z_

<details><summary>↩ Tool result · `toolu_01R6aN2nPT9zc6JUJpSLDzd2`</summary>

```text
Web search results for query: "arXiv 2502.15654 "Machine-generated text detection prevents language model collapse" Drayson 2025"

Links: [{"title":"[2502.15654] Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/abs/2502.15654"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654"},{"title":"(PDF) Machine-generated text detection prevents language model collapse","url":"https://www.researchgate.net/publication/397412242_Machine-generated_text_detection_prevents_language_model_collapse"},{"title":"GitHub - GeorgeDrayson/model_collapse","url":"https://github.com/GeorgeDrayson/model_collapse"},{"title":"Machine-generated text detection prevents language model collapse - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/"},{"title":"Computation and Language Feb 2025","url":"https://www.arxiv.org/list/cs.CL/2025-02?skip=1325&show=250"},{"title":"Machine-generated text detection prevents language model ...","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/1/2025.emnlp-main.1506.pdf"},{"title":"Machine-generated text detection prevents language ...","url":"https://omega.cs.ucl.ac.uk/assets/pdf/papers/drayson2025-model-collapse.pdf"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=3800&show=2000"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/html/2410.12341v3"}]

I found the paper you're searching for! Here's the information about arXiv 2502.15654:

## Paper Details

The paper "Machine-generated text detection prevents language model collapse" is authored by George Drayson, Emine Yilmaz, and Vasileios Lampos (2025). It was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 29645-29661.

## Research Focus

As Large Language Models (LLMs) become increasingly prevalent, their generated outputs are proliferating across the web, risking a future where machine-generated content dilutes human-authored text. This could lead to model collapse, a degenerative process whereby LLMs reinforce their own errors, reduce output diversity, and ultimately yield declining performance.

The study investigates the impact of decoding strategy on model collapse, analysing the text characteristics at each model generation, the similarity to human references, and the resulting model performance. The project proposes an importance sampling approach to alleviate model collapse.

You can find the full paper on arXiv at https://arxiv.org/abs/2502.15654, and the official implementation is available on GitHub at https://github.com/GeorgeDrayson/model_collapse.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "214f306e-a23e-4e3d-9857-ab4485cd3826",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "01fcfae8-52b9-4d2d-a3c7-89ffab9d43a1",
  "sourceToolAssistantUUID": "214f306e-a23e-4e3d-9857-ab4485cd3826",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-26T10:50:35.469Z_

<details><summary>↩ Tool result · `toolu_01ST3V8nHLk9Y6xfzMxCP9z7`</summary>

```text
Web search results for query: "arXiv 2503.03150 "Position Model Collapse Does Not Mean What You Think" Schaeffer Kazdan 2025"

Links: [{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"Position: the Stochastic Parrot in the Coal Mine Model Collapse is a Threat to Low-Resource Communities","url":"https://arxiv.org/html/2605.04127"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/html/2410.12341v3"},{"title":"Machine Learning Mar 2025","url":"https://www.arxiv.org/list/cs.LG/2025-03?skip=325&show=2000"},{"title":"[Literature Review] Position: Model Collapse Does Not Mean What You Think","url":"https://www.themoonlight.io/en/review/position-model-collapse-does-not-mean-what-you-think"},{"title":"Position: Model Collapse Does Not Mean What You Think Anonymous Author(s)","url":"https://openreview.net/pdf?id=ygfzWIGDN8"}]

I found the paper you're looking for! Here's what I can tell you about it:

## arXiv:2503.03150 - "Position: Model Collapse Does Not Mean What You Think"

**Authors:** Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo

**Main Argument:** The authors contend that the widespread narrative about model collapse fundamentally misunderstands the scientific evidence.

**Key Finding:** Research on model collapse encompasses eight distinct and at times conflicting definitions of model collapse, and inconsistent terminology within and between papers has hindered building a comprehensive understanding of model collapse.

**Context:** The proliferation of AI-generated content online has fueled concerns over model collapse, a degradation in future generative models' performance when trained on synthetic data generated by earlier models. Industry leaders, premier research journals and popular science publications alike have prophesied catastrophic societal consequences stemming from model collapse.

**Categorization:** The 8 definitions can be loosely grouped into three families: (1) the behavior of the test loss on real data over model-fitting iterations, (2) the deformation of the real data distribution over model-fitting iterations, and (3) the scaling behavior of the test loss with respect to typical scaling quantities such as the amount of data.

The paper was submitted on March 5, 2025 and last revised on March 18, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a54ec626-262d-4e7d-8382-14457347d91f",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "7ff51383-b912-48f2-91de-e723dcaca93f",
  "sourceToolAssistantUUID": "a54ec626-262d-4e7d-8382-14457347d91f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-26T10:50:35.565Z_

<details><summary>↩ Tool result · `toolu_01BZcknWK7SnoBw7aKP7uYQk`</summary>

```text
Web search results for query: ""Dynamic Center-Edge Sampling" "Countering Model Collapse" Zhu Xie Electronics 2026"

Links: [{"title":"Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling | MDPI","url":"https://www.mdpi.com/2079-9292/15/4/869"},{"title":"ICML 2025 Thursday 07/17","url":"https://icml.cc/virtual/2025/day/7/17"},{"title":"Ground collapse early warning driven by edge-based data assimilation and adaptive threshold using quasi-distributed flexible conductive film sensor array - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0263224125021232"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=3100&show=2000"},{"title":"IEEE Catalog Number: ISBN: CFP25RAA-POD 979-8-3315-4140-8","url":"https://www.proceedings.com/content/081/081087webtoc.pdf"},{"title":"Computer Science Aug 2025","url":"https://arxiv.org/list/cs/2025-08?skip=4500&show=2000"}]

I found the research paper! Based on the search results:

A paper titled "Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling" was published in Electronics in February 2026 by authors Bingze Zhu and Yubo Xie from the College of Information Engineering at Shanghai Maritime University.

The paper addresses the problem of model collapse—where models undergo catastrophic performance degradation and diversity collapse when recursively trained on their own increasingly homogenized synthetic data—and proposes a dynamic data selection framework that lacks the static strategy limitations of previous approaches.

The full paper is available at: https://www.mdpi.com/2079-9302/15/4/869


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f979ed8-7b3b-4e25-bbbe-c1ad8d84ff46",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "c5a4bcd6-96de-47be-9dca-ef7fd234b9b7",
  "sourceToolAssistantUUID": "1f979ed8-7b3b-4e25-bbbe-c1ad8d84ff46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-26T10:50:36.195Z_

<details><summary>↩ Tool result · `toolu_017L7quwRC7cHmJGSjbB5PF7`</summary>

```text
Web search results for query: "arXiv 2601.09001 "Entropy Sentinel" Buffa Del Corro 2026"

Links: [{"title":"[2601.09001] Entropy Sentinel: Continuous LLM Accuracy Monitoring from Decoding Entropy Traces in STEM","url":"https://arxiv.org/abs/2601.09001"},{"title":"Entropy Sentinel: Continuous LLM Accuracy Monitoring from Decoding Entropy Traces in STEM","url":"https://arxiv.org/html/2601.09001"},{"title":"[2601.03220] From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence","url":"https://arxiv.org/abs/2601.03220"},{"title":"[2601.01401] LANCET: Neural Intervention via Structural Entropy for Mitigating Faithfulness Hallucinations in LLMs","url":"https://arxiv.org/abs/2601.01401"},{"title":"[2601.00554] Entropy Production in Machine Learning Under Fokker-Planck Probability Flow","url":"https://arxiv.org/abs/2601.00554"},{"title":"Entanglement Entropy of Massive Scalar Fields: Mass Suppression, Violation of","url":"https://arxiv.org/pdf/2603.24158"},{"title":"[2601.21200] Provably Reliable Classifier Guidance via Cross-Entropy Control","url":"https://arxiv.org/abs/2601.21200"},{"title":"[2601.02712] Transform and Entropy Coding in AV2","url":"https://arxiv.org/abs/2601.02712"}]

I found the paper! Here are the results for your search:

## "Entropy Sentinel: Continuous LLM Accuracy Monitoring from Decoding Entropy Traces in STEM"

**ArXiv ID:** 2601.09001

**Authors:** Pedro Memoli Buffa and Luciano Del Corro

**Publication Date:** Submitted on 13 Jan 2026 (v1), last revised 3 Mar 2026 (this version, v3)

**Key Focus:** The paper addresses two coupled challenges in deploying LLMs: (1) monitoring--estimating where a model underperforms as traffic and domains drift--and (2) improvement--prioritizing data acquisition to close the largest performance gaps.

**Methodology:** For each response, the authors compute an output-entropy profile from final-layer next-token probabilities (from top-k logprobs) and summarize it with different statistics. A lightweight classifier predicts instance correctness, and averaging predicted probabilities yields a domain-level accuracy estimate.

The paper is available at: https://arxiv.org/abs/2601.09001


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "681fcb6a-b550-4e3f-a257-5a6636a8456e",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "57f305cd-b95e-47e5-90e2-f54ab69f345d",
  "sourceToolAssistantUUID": "681fcb6a-b550-4e3f-a257-5a6636a8456e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T10:50:39.092Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EqtqtL5gDhYxxEu3odtgvN`</summary>

```json
{
  "query": "arXiv 2509.16499 \"A Closer Look at Model Collapse\" Shi Wu Zhang NeurIPS 2025 Spotlight"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57f305cd-b95e-47e5-90e2-f54ab69f345d",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3xTFfX5tCdMMgJStDN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "42f811c1-68e1-4564-ab21-5c3da8e155bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqU5Ct8RiECkyWU8D4wRiq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 529,
      "cache_creation_input_tokens": 3356,
      "cache_read_input_tokens": 110416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3356,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 59 · 2026-05-26T10:50:40.492Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011cyJH3iYAY8nDA5BhzBWJ3`</summary>

```json
{
  "query": "arXiv 2504.03814 Kovac \"Recursive Training Loops LLMs\" EMNLP 2025 Oral"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42f811c1-68e1-4564-ab21-5c3da8e155bc",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3xTFfX5tCdMMgJStDN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a77f8df0-247a-4bac-a57b-fafb085da47e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqU5Ct8RiECkyWU8D4wRiq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 529,
      "cache_creation_input_tokens": 3356,
      "cache_read_input_tokens": 110416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3356,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 60 · 2026-05-26T10:50:42.109Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XCcncfxAztYLmkp7AWza2B`</summary>

```json
{
  "query": "arXiv 2505.18091 Gu Liang Pehlevan \"Data Mixing Phase Transitions Knowledge Acquisition\" NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a77f8df0-247a-4bac-a57b-fafb085da47e",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3xTFfX5tCdMMgJStDN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "781ae334-d03f-492a-b8d3-3cf8f70039b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqU5Ct8RiECkyWU8D4wRiq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 529,
      "cache_creation_input_tokens": 3356,
      "cache_read_input_tokens": 110416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3356,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 61 · 2026-05-26T10:50:43.220Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017VbQ595j8r8K3dSJwebx8X`</summary>

```json
{
  "query": "arXiv 2410.16713 Kazdan Schaeffer \"Collapse or Thrive Perils Promises Synthetic Data\" ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "781ae334-d03f-492a-b8d3-3cf8f70039b9",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3xTFfX5tCdMMgJStDN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e366384-f024-4a47-830a-d1f8d3fcdf7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqU5Ct8RiECkyWU8D4wRiq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 529,
      "cache_creation_input_tokens": 3356,
      "cache_read_input_tokens": 110416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3356,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
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

_source line 62 · 2026-05-26T10:50:44.263Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BB7se4g2NvpZX6ENffaSSU`</summary>

```json
{
  "query": "arXiv 2402.07043 Dohmatob Feng \"Tale of Tails Model Collapse Scaling Laws\" ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e366384-f024-4a47-830a-d1f8d3fcdf7d",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3xTFfX5tCdMMgJStDN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6d48e564-6b55-4bc5-86bb-50a392a45519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqU5Ct8RiECkyWU8D4wRiq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 529,
      "cache_creation_input_tokens": 3356,
      "cache_read_input_tokens": 110416,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3356
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 529,
          "output_tokens": 369,
          "cache_read_input_tokens": 110416,
          "cache_creation_input_tokens": 3356,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3356,
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

_source line 63 · 2026-05-26T10:50:47.879Z_

<details><summary>↩ Tool result · `toolu_01EqtqtL5gDhYxxEu3odtgvN`</summary>

```text
Web search results for query: "arXiv 2509.16499 "A Closer Look at Model Collapse" Shi Wu Zhang NeurIPS 2025 Spotlight"

Links: [{"title":"[2509.16499] A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/abs/2509.16499"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"A Closer Look at Model Collapse","url":"https://arxiv.org/pdf/2509.16499"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective | Request PDF","url":"https://www.researchgate.net/publication/395724450_A_Closer_Look_at_Model_Collapse_From_a_Generalization-to-Memorization_Perspective"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://shilianghe007.github.io/model-collapse/index.html"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=1100&show=2000"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"A Closer Look at Multimodal Representation Collapse","url":"https://arxiv.org/html/2505.22483v1"},{"title":"A Closer Look at Model Collapse:","url":"https://par.nsf.gov/servlets/purl/10643460"}]

I found the paper! Here are the search results for arXiv 2509.16499:

**Paper Title:** "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"

**Authors:** Lianghe Shi, Meng Wu, Huijie Zhang, Zekai Zhang, Molei Tao, and Qing Qu

**Venue:** NeurIPS 2025 Spotlight paper

**Summary:** The paper addresses model collapse—a phenomenon in which recursive iterations of training on synthetic data lead to performance degradation. The paper identifies a transition from generalization to memorization during model collapse in diffusion models, where models increasingly replicate training data instead of generating novel content during iterative training on synthetic samples. 

**Key Contribution:** The transition is driven by declining entropy of synthetic training data, and the authors propose an entropy-based data selection strategy to mitigate this transition and alleviate model collapse.

The paper was submitted to arXiv on September 20, 2025, with the latest version (v3) on December 25, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "42f811c1-68e1-4564-ab21-5c3da8e155bc",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "f991f20f-a4dd-4a0c-9f46-c37b6ed005f6",
  "sourceToolAssistantUUID": "42f811c1-68e1-4564-ab21-5c3da8e155bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-26T10:50:48.795Z_

<details><summary>↩ Tool result · `toolu_011cyJH3iYAY8nDA5BhzBWJ3`</summary>

```text
Web search results for query: "arXiv 2504.03814 Kovac "Recursive Training Loops LLMs" EMNLP 2025 Oral"

Links: [{"title":"[2504.03814] Recursive Training Loops in LLMs: How training data properties modulate distribution shift in generated data?","url":"https://arxiv.org/abs/2504.03814"},{"title":"Recursive Training Loops in LLMs: How training data properties modulate distribution shift in generated data?","url":"https://arxiv.org/html/2504.03814"},{"title":"[2504.03814v3] Recursive Training Loops in LLMs: How training data properties modulate distribution shift in generated data?","url":"https://arxiv.org/abs/2504.03814v3"},{"title":"Computation and Language Apr 2025","url":"https://arxiv.org/list/cs.CL/2025-04?skip=1225&show=50"},{"title":"Machine Learning Apr 2025","url":"https://arxiv.org/list/cs.LG/2025-04?skip=275&show=25"},{"title":"Computer Science Apr 2025","url":"https://www.arxiv.org/list/cs/2025-04?skip=1775&show=2000"},{"title":"Computation and Language May 2025","url":"https://www.arxiv.org/list/cs.CL/2025-05?skip=2050&show=2000"}]

I found the paper you're looking for! Here are the details:

**Title:** "Recursive Training Loops in LLMs: How training data properties modulate distribution shift in generated data?"

**Authors:** &lt;cite index="2-1">Grgur Kovač, Jérémy Perez, Rémy Portelas, Peter Ford Dominey, Pierre-Yves Oudeyer

**arXiv ID:** 2504.03814

**Acceptance Status:** Accepted to EMNLP 2025 (Oral)

**Summary:** The paper examines how large language models (LLMs) used to create online content create feedback loops where subsequent generations are trained on synthetic data, leading to distribution shifts where models misrepresent the true underlying distributions of human data (model collapse). Through manipulation of dataset properties and regression analyses, the authors identify properties predicting distribution shift magnitudes, finding that lexical diversity amplifies these shifts, while semantic diversity and data quality mitigate them.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a77f8df0-247a-4bac-a57b-fafb085da47e",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "dc051a90-7b99-4cca-b87f-3cf82853fcfe",
  "sourceToolAssistantUUID": "a77f8df0-247a-4bac-a57b-fafb085da47e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-26T10:50:49.816Z_

<details><summary>↩ Tool result · `toolu_01XCcncfxAztYLmkp7AWza2B`</summary>

```text
Web search results for query: "arXiv 2505.18091 Gu Liang Pehlevan "Data Mixing Phase Transitions Knowledge Acquisition" NeurIPS 2025"

Links: [{"title":"[2505.18091] Data Mixing Can Induce Phase Transitions in Knowledge Acquisition","url":"https://arxiv.org/abs/2505.18091"},{"title":"Data Mixing Can Induce Phase Transitions in Knowledge Acquisition","url":"https://arxiv.org/html/2505.18091"},{"title":"Data Mixing Can Induce Phase Transitions in Knowledge Acquisition | OpenReview","url":"https://openreview.net/forum?id=ZKA4yiGdrA"},{"title":"Data Mixing in LLMs: Phase Transitions","url":"https://www.emergentmind.com/papers/2505.18091"},{"title":"NeurIPS Poster Data Mixing Can Induce Phase Transitions in Knowledge Acquisition","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/115595"},{"title":"Data Mixing Can Induce Phase Transitions in Knowledge Acquisition Xinran Gu1,3∗","url":"https://openreview.net/pdf?id=tQZK5frjVU"},{"title":"Data Mixing Can Induce Phase Transitions in Knowledge ...","url":"https://bytez.com/docs/arxiv/2505.18091/paper"},{"title":"ICLR Spotlight Presentation: Xinran Gu 📊 Data Mixing Can Induce Phase Transitions in Knowledge Acquisition","url":"https://iclr.cc/virtual/2025/36887"},{"title":"Computer Science May 2025","url":"https://www.arxiv.org/list/cs/2025-05?skip=9050&show=50"},{"title":"Phase transitions in AI-human interaction networks: statistics, computation, and probabilistic modeling","url":"https://arxiv.org/html/2505.02879v1"}]

I found the paper! Here are the results:

The paper "Data Mixing Can Induce Phase Transitions in Knowledge Acquisition" (arXiv:2505.18091) examines how Large Language Models trained on data mixtures—where most data comes from web scrapes and a small portion from high-quality, knowledge-dense sources—show that knowledge acquisition can exhibit phase transitions with respect to mixing ratio and model size, unlike smooth scaling laws observed when training exclusively on knowledge-dense data.

The authors demonstrate through controlled experiments on a synthetic biography dataset mixed with web-scraped data that: (1) as model size increases to a critical value, the model suddenly transitions from memorizing very few to most of the biographies; (2) below a critical mixing ratio, the model memorizes almost nothing even with extensive training.

The authors are Xinran Gu, Kaifeng Lyu, Jiazheng Li, and Jingzhao Zhang. The paper was presented as a poster at NeurIPS 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "781ae334-d03f-492a-b8d3-3cf8f70039b9",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "54b411aa-b4cc-4822-b004-8f46b7d36ed1",
  "sourceToolAssistantUUID": "781ae334-d03f-492a-b8d3-3cf8f70039b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-26T10:50:52.457Z_

<details><summary>↩ Tool result · `toolu_01BB7se4g2NvpZX6ENffaSSU`</summary>

```text
Web search results for query: "arXiv 2402.07043 Dohmatob Feng "Tale of Tails Model Collapse Scaling Laws" ICML 2024"

Links: [{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/html/2402.07043v2"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/tale-tails-model-collapse-as-change-scaling"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://www.emergentmind.com/papers/2402.07043"},{"title":"Paper page - A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://huggingface.co/papers/2402.07043"},{"title":"[Literature Review] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://www.themoonlight.io/en/review/a-tale-of-tails-model-collapse-as-a-change-of-scaling-laws"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://proceedings.mlr.press/v235/dohmatob24b.html"}]

I found the paper! Here's what I can tell you about it:

**Paper Details:**
The paper is titled "A Tale of Tails: Model Collapse as a Change of Scaling Laws" by Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, and Julia Kempe.

**Publication:**
The paper was published in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024), held July 21-27, 2024, on pages 11165-11197.

**Research Focus:**
The paper investigates how scaling laws will change as synthetic data makes its way into training corpora, developing a theoretical framework of model collapse through the lens of scaling laws. The authors discover a wide range of decay phenomena, including loss of scaling, shifted scaling with number of generations, the "un-learning" of skills, and grokking when mixing human and synthesized data.

**Key Concept:**
The authors propose a "double scaling law" that explains how model collapse can arise as a change in the scaling behavior of the model's outputs.

The paper is available on arXiv (2402.07043) and through the official ICML proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6d48e564-6b55-4bc5-86bb-50a392a45519",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "7dc06c0f-2d4e-45f8-b667-5986df51c664",
  "sourceToolAssistantUUID": "6d48e564-6b55-4bc5-86bb-50a392a45519",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-26T10:50:52.758Z_

<details><summary>↩ Tool result · `toolu_017VbQ595j8r8K3dSJwebx8X`</summary>

```text
Web search results for query: "arXiv 2410.16713 Kazdan Schaeffer "Collapse or Thrive Perils Promises Synthetic Data" ICML 2025"

Links: [{"title":"[2410.16713] Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/abs/2410.16713"},{"title":"Collapse or Thrive?Perils and Promises of Synthetic Data ...","url":"https://arxiv.org/pdf/2410.16713"},{"title":"ICML Poster Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://icml.cc/virtual/2025/poster/44713"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.16713"},{"title":"(PDF) Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://www.researchgate.net/publication/385140496_Collapse_or_Thrive_Perils_and_Promises_of_Synthetic_Data_in_a_Self-Generating_World"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/html/2410.16713v2"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://proceedings.mlr.press/v267/kazdan25a.html"}]

I found the paper successfully! Here's what I can tell you about it:

## Paper Details

The paper is authored by Joshua Kazdan, Rylan Schaeffer, Apratim Dey, Matthias Gerstgrasser, Rafael Rafailov, David L. Donoho, and Sanmi Koyejo.

**Title:** "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"

**arXiv ID:** 2410.16713

**Publication:** The paper was published in the Proceedings of the 42nd International Conference on Machine Learning (ICML 2025)

## Research Overview

The paper addresses the question: What happens when generative machine learning models are pretrained on web-scale datasets containing data generated by earlier models?

The researchers report experiments on three ways of using data (training-workflows) across three generative model task-settings (multivariate Gaussian estimation, kernel density estimation, and language-model fine-tuning) to investigate the possibility of containment: they confirm that the training-workflow of replacing all real data by successive generations of purely synthetic data indeed suffers model collapse in all task-settings studied, and they consider the training-workflow of accumulating synthetic data alongside real data.

The paper is available on [arXiv](https://arxiv.org/abs/2410.16713) and through the [ICML proceedings](https://proceedings.mlr.press/v267/kazdan25a.html).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e366384-f024-4a47-830a-d1f8d3fcdf7d",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "ecdc524f-ce25-4331-bd72-fdfe2b799f86",
  "sourceToolAssistantUUID": "8e366384-f024-4a47-830a-d1f8d3fcdf7d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-26T10:50:58.310Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VUNa2KZr87yhJHFGVNsprK`</summary>

```json
{
  "query": "arXiv 2407.17467 Gu Yang Ding \"CMR Scaling Law Critical Mixture Ratios\" EMNLP 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ecdc524f-ce25-4331-bd72-fdfe2b799f86",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3yg2PVQoqwqnxbpS8L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ce08d31-a5cb-48e5-b4f2-c5cacee3d8b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRcgS3bSpiMAm9Jv1yrBfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 713,
      "cache_creation_input_tokens": 3903,
      "cache_read_input_tokens": 113772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3903,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 69 · 2026-05-26T10:50:58.462Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AGS3k8BK6S3pMBoRG9PKhB`</summary>

```json
{
  "query": "arXiv 2211.08095 Hataya Bao Arai \"Will Large-scale Generative Models Corrupt Future Datasets\" ICCV 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ce08d31-a5cb-48e5-b4f2-c5cacee3d8b9",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3yg2PVQoqwqnxbpS8L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64f7ed19-5f84-4412-a2cc-0ffef0d24f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRcgS3bSpiMAm9Jv1yrBfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 713,
      "cache_creation_input_tokens": 3903,
      "cache_read_input_tokens": 113772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3903,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 70 · 2026-05-26T10:50:59.180Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R21gz4JnozCUwfRUuT2FUH`</summary>

```json
{
  "query": "Shumailov \"Curse of Recursion Training Generated Data Models Forget\" Nature 2024 arXiv 2305.17493"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64f7ed19-5f84-4412-a2cc-0ffef0d24f77",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3yg2PVQoqwqnxbpS8L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9bd09247-9b81-4227-b192-a711b35dc0c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRcgS3bSpiMAm9Jv1yrBfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 713,
      "cache_creation_input_tokens": 3903,
      "cache_read_input_tokens": 113772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3903,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 71 · 2026-05-26T10:51:00.129Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RPR4ZwomUqMsdCkVSidrc4`</summary>

```json
{
  "query": "arXiv 2307.01850 Alemohammad \"Self-Consuming Generative Models Go MAD\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bd09247-9b81-4227-b192-a711b35dc0c8",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3yg2PVQoqwqnxbpS8L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "564199a9-6fb9-4caf-9e36-506b312765c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRcgS3bSpiMAm9Jv1yrBfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 713,
      "cache_creation_input_tokens": 3903,
      "cache_read_input_tokens": 113772,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3903,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 72 · 2026-05-26T10:51:00.834Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CXDx2HdJWpHGFvaNDRZ9fQ`</summary>

```json
{
  "query": "arXiv 2404.01413 Gerstgrasser Schaeffer \"Model Collapse Inevitable Breaking Curse Recursion Accumulating\" ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "564199a9-6fb9-4caf-9e36-506b312765c6",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR3yg2PVQoqwqnxbpS8L",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9f128fd-f387-4f0c-8efc-dd2f8522e8bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QRcgS3bSpiMAm9Jv1yrBfG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 713,
      "cache_creation_input_tokens": 3903,
      "cache_read_input_tokens": 113772,
      "output_tokens": 374,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3903
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 713,
          "output_tokens": 374,
          "cache_read_input_tokens": 113772,
          "cache_creation_input_tokens": 3903,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3903,
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

_source line 73 · 2026-05-26T10:51:06.569Z_

<details><summary>↩ Tool result · `toolu_01VUNa2KZr87yhJHFGVNsprK`</summary>

```text
Web search results for query: "arXiv 2407.17467 Gu Yang Ding "CMR Scaling Law Critical Mixture Ratios" EMNLP 2024"

Links: [{"title":"[2407.17467] CMR Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models","url":"https://arxiv.org/abs/2407.17467"},{"title":"CMR Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240717467G/abstract"},{"title":"CMR Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models","url":"https://arxiv.org/html/2407.17467v2"},{"title":"CMR Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/cmr-scaling-law-predicting-critical-mixture-ratios"},{"title":"CMR Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models | Request PDF","url":"https://www.researchgate.net/publication/382526451_CMR_Scaling_Law_Predicting_Critical_Mixture_Ratios_for_Continual_Pre-training_of_Language_Models"},{"title":"A Practice of Post-Training on Llama-3 70B with Optimal Selection of Additional Language Mixture Ratio","url":"https://arxiv.org/html/2409.06624v1"},{"title":"CMR Scaling Law: Predicting Critical Mixture Ratios for ...","url":"https://aclanthology.org/2024.emnlp-main.903.pdf"},{"title":"CMR Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.903/"},{"title":"CMR Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models - Paper Detail","url":"https://deeplearn.org/arxiv/512008/cmr-scaling-law:-predicting-critical-mixture-ratios-for-continual-pre-training-of-language-models"},{"title":"CMR Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models [Quick Review]","url":"https://liner.com/review/cmr-scaling-law-predicting-critical-mixture-ratios-for-continual-pretraining"}]

I found the paper you're looking for. Here's what I found:

The paper "CMR Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models" is authored by Jiawei Gu, Zacc Yang, Chuanghao Ding, Rui Zhao, and Fei Tan.

**Paper Details:**
- The paper formalizes the trade-off between general and domain-specific capabilities, leading to a well-defined Critical Mixture Ratio (CMR) of general and domain data
- The researchers discover a power-law relationship between loss, mixture ratio, and training tokens scale
- It was published at EMNLP 2024

**Problem Addressed:**
Continual pre-training (CPT) enhances LLM capabilities by imbuing new domain-specific or proprietary knowledge while replaying general corpus to prevent catastrophic forgetting, but the data mixture ratio of general corpus and domain-specific corpus has been chosen heuristically, leading to sub-optimal training efficiency.

The paper is available on arXiv and has been accepted to the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ce08d31-a5cb-48e5-b4f2-c5cacee3d8b9",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "5e185140-3c38-4015-a18b-a317c558f0c5",
  "sourceToolAssistantUUID": "9ce08d31-a5cb-48e5-b4f2-c5cacee3d8b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-26T10:51:06.985Z_

<details><summary>↩ Tool result · `toolu_01AGS3k8BK6S3pMBoRG9PKhB`</summary>

```text
Web search results for query: "arXiv 2211.08095 Hataya Bao Arai "Will Large-scale Generative Models Corrupt Future Datasets" ICCV 2023"

Links: [{"title":"[2211.08095] Will Large-scale Generative Models Corrupt Future Datasets?","url":"https://arxiv.org/abs/2211.08095"},{"title":"ICCV 2023 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2023/html/Hataya_Will_Large-scale_Generative_Models_Corrupt_Future_Datasets_ICCV_2023_paper.html"},{"title":"GitHub - moskomule/dataset-contamination: Datasets of \"Will Large-scale Generative Models Corrupt Future Datasets?\"","url":"https://github.com/moskomule/dataset-contamination"},{"title":"Ryuichiro Hataya’s webpage","url":"https://hataya.tokyo/"},{"title":"Will Large-scale Generative Models Corrupt Future Datasets?","url":"https://www.researchgate.net/publication/377428626_Will_Large-scale_Generative_Models_Corrupt_Future_Datasets"},{"title":"Hataya Will Large-Scale Generative Models Corrupt Future Datasets ICCV 2023 Paper | PDF","url":"https://www.scribd.com/document/763537391/Hataya-Will-Large-scale-Generative-Models-Corrupt-Future-Datasets-ICCV-2023-paper"},{"title":"Ryuichiro Hataya on LinkedIn: Will Large-scale Generative Models Corrupt Future Datasets?","url":"https://www.linkedin.com/posts/ryuichiro-hataya-7940a1125_will-large-scale-generative-models-corrupt-activity-7085728384785281024-2_cr"},{"title":"GitHub - 52CV/ICCV-2023-Papers · GitHub","url":"https://github.com/52CV/ICCV-2023-Papers"},{"title":"ICCV2023 Papers - a Hugging Face Space by ICCV2023","url":"https://huggingface.co/spaces/ICCV2023/ICCV2023-papers"}]

I found the paper you're looking for! "Will Large-scale Generative Models Corrupt Future Datasets?" is a paper by Ryuichiro Hataya, Han Bao, and Hiromi Arai, published in the Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) in October 2023, pages 20555-20565.

The paper addresses text-to-image generative models such as DALL·E 2, Midjourney, and StableDiffusion, which can generate high-quality and realistic images from user prompts. The research investigates the central question of "will such generated images impact the quality of future datasets and the performance of computer vision models positively or negatively?" by empirically answering this question through simulating contamination.

The controlled experiments reveal that the contamination of generated images into training data degenerates the performance of computer vision models. 

The paper is also available on arXiv as preprint 2211.08095, and there's an associated GitHub repository containing the datasets used in the research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64f7ed19-5f84-4412-a2cc-0ffef0d24f77",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "380462e0-8520-4887-9b0c-9ce3822ba5d7",
  "sourceToolAssistantUUID": "64f7ed19-5f84-4412-a2cc-0ffef0d24f77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-26T10:51:07.253Z_

<details><summary>↩ Tool result · `toolu_01R21gz4JnozCUwfRUuT2FUH`</summary>

```text
Web search results for query: "Shumailov "Curse of Recursion Training Generated Data Models Forget" Nature 2024 arXiv 2305.17493"

Links: [{"title":"[2305.17493] The Curse of Recursion: Training on Generated Data Makes Models Forget","url":"https://arxiv.org/abs/2305.17493"},{"title":"[PDF] The Curse of Recursion: Training on Generated Data Makes Models Forget | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curse-of-Recursion:-Training-on-Generated-Data-Shumailov-Shumaylov/155aec5cff650263a4c71136f97570611d1bba7a"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget","url":"https://arxiv.org/html/2305.17493v3"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/curse-recursion-training-generated-data-makes-models"},{"title":"Recursive Pollution and Model Collapse Are Not the Same | BIML","url":"https://berryvilleiml.com/2026/01/10/recursive-pollution-and-model-collapse-are-not-the-same/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"Experts divided over training AI with more data from AI • The Register","url":"https://www.theregister.com/2024/05/09/ai_model_collapse/"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget | alphaXiv","url":"https://www.alphaxiv.org/overview/2305.17493v3"},{"title":"The Curse of Recursion: Training on Generated Data Makes Models Forget (2023) | Ilia Shumailov | 153 Citations","url":"https://scispace.com/papers/the-curse-of-recursion-training-on-generated-data-makes-34zgysyl"},{"title":"THE CURSE OF RECURSION: TRAINING ON GENERATED DATA MAKES MODELS FORGET","url":"https://www.cl.cam.ac.uk/~is410/Papers/dementia_arxiv.pdf"}]

I found the research you're looking for. Here's what I found about this paper:

**Title & Authors:** "The Curse of Recursion: Training on Generated Data Makes Models Forget" by Ilia Shumailov and 5 other authors

**arXiv Reference:** arXiv preprint arXiv:2305.17493 (2023)

**Publication:** The paper was later published in Nature vol 631

**Main Finding:** Use of model-generated content in training causes irreversible defects in the resulting models, where tails of the original content distribution disappear

**Key Concept:** The effect is referred to as Model Collapse and can occur in Variational Autoencoders, Gaussian Mixture Models and LLMs

**Scope:** The authors build theoretical intuition behind the phenomenon and portray its ubiquity amongst all learned generative models

The paper addresses an important concern about the future of large language models as model-generated content becomes increasingly prevalent in online datasets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9bd09247-9b81-4227-b192-a711b35dc0c8",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "951e4dba-6ba3-4fbb-9252-1feaff828414",
  "sourceToolAssistantUUID": "9bd09247-9b81-4227-b192-a711b35dc0c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-26T10:51:07.784Z_

<details><summary>↩ Tool result · `toolu_01RPR4ZwomUqMsdCkVSidrc4`</summary>

```text
Web search results for query: "arXiv 2307.01850 Alemohammad "Self-Consuming Generative Models Go MAD" ICLR 2024"

Links: [{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/pdf/2307.01850"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://richb.rice.edu/2023/07/12/self-consuming-generative-models-go-mad/"},{"title":"Self-Consuming Generative Models Go MAD | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2307.01850"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf"},{"title":"(PDF) Self-Consuming Generative Models Go MAD","url":"https://www.researchgate.net/publication/372136378_Self-Consuming_Generative_Models_Go_MAD"},{"title":"Paper page - Self-Consuming Generative Models Go MAD","url":"https://huggingface.co/papers/2307.01850"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"Self-Consuming Generative Models Go MAD","url":"https://dsp.rice.edu/2023/07/06/self-consuming-generative-models-go-mad/"}]

I found the paper you're looking for! Here's what the search results show:

The paper "Self-Consuming Generative Models Go MAD" was published as a conference paper at ICLR 2024.

**Paper Details:**
- **arXiv ID:** 2307.01850
- **Authors:** Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk
- **Posted:** July 4, 2023

**Summary:**
The paper addresses how advances in generative AI algorithms have led to using synthetic data to train next-generation models, and repeating this process creates an autophagous (self-consuming) loop whose properties are poorly understood. The authors conduct a thorough analytical and empirical analysis using state-of-the-art generative image models of three families of autophagous loops that differ in how fixed or fresh real training data is available through generations of training and in whether samples from previous generation models have been biased to trade off data quality versus diversity.

The paper is available on arXiv at https://arxiv.org/abs/2307.01850 and the official ICLR 2024 proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "564199a9-6fb9-4caf-9e36-506b312765c6",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "be384535-9cba-40ff-99dc-e9b14b8c252c",
  "sourceToolAssistantUUID": "564199a9-6fb9-4caf-9e36-506b312765c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-26T10:51:11.899Z_

<details><summary>↩ Tool result · `toolu_01CXDx2HdJWpHGFvaNDRZ9fQ`</summary>

```text
Web search results for query: "arXiv 2404.01413 Gerstgrasser Schaeffer "Model Collapse Inevitable Breaking Curse Recursion Accumulating" ICML 2024"

Links: [{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of","url":"https://arxiv.org/pdf/2404.01413v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240401413G/abstract"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-Model-Collapse-Inevitable-Breaking-the-Curse-of-Gerstgrasser-Schaeffer/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"AI-Powered Paper Summarization about the arXiv paper 2404.01413v1","url":"https://www.summarizepaper.com/en/arxiv-id/2404.01413v1/"}]

I found the paper! Here are the key details:

**Paper Title:** "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"

**Authors:** Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, and Sanmi Koyejo

**arXiv ID:** 2404.01413

**Publication Date:** April 29, 2024

**Main Research Question:** The paper investigates what happens when models are trained on their own generated outputs, examining whether model-data feedback loops lead to model collapse—where performance progressively degrades with each iteration until models become useless.

**Key Finding:** The paper shows that accumulating data prevents model collapse, contrasting with previous studies that largely assumed new data replace old data over time.

The paper is available at: https://arxiv.org/abs/2404.01413


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b9f128fd-f387-4f0c-8efc-dd2f8522e8bc",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "26b7a50b-029e-4216-b877-64d8a5a67b97",
  "sourceToolAssistantUUID": "b9f128fd-f387-4f0c-8efc-dd2f8522e8bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Assistant

_source line 78 · 2026-05-26T10:51:15.285Z_

Now let me verify the remaining entries including the older/classic ones and the ones with incomplete author fields.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26b7a50b-029e-4216-b877-64d8a5a67b97",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR415sNirVghuHF7dVsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a5697cb-11e0-4df3-acb1-3412b6af0777",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Y4TDAQa4Afk3XGtjZQBk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5535,
      "cache_read_input_tokens": 117675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5535,
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

_source line 79 · 2026-05-26T10:51:17.326Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CAjKiJh9ZFR9oCRiawB9rb`</summary>

```json
{
  "query": "dohmatob2024tale \"A Tale of Tails\" authors full list Pu Yang Francois Charton Julia Kempe ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a5697cb-11e0-4df3-acb1-3412b6af0777",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR415sNirVghuHF7dVsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5fe6dd2e-c667-4840-b153-7b5509fd22be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Y4TDAQa4Afk3XGtjZQBk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5535,
      "cache_read_input_tokens": 117675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5535,
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

_source line 80 · 2026-05-26T10:51:18.310Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018NuZch5qYhYxT54eueWT8J`</summary>

```json
{
  "query": "arXiv 2510.05133 Du Wu Tang Wang Fan full authors list \"Characterizing Model Behavior\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fe6dd2e-c667-4840-b153-7b5509fd22be",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR415sNirVghuHF7dVsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "348bc1fb-a5da-418e-a3f6-74d162f8ef32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Y4TDAQa4Afk3XGtjZQBk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5535,
      "cache_read_input_tokens": 117675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5535,
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

_source line 81 · 2026-05-26T10:51:19.653Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WTo3DsQ4GLas2akAcbaso3`</summary>

```json
{
  "query": "Li Jiwei \"Diversity-Promoting Objective Function Neural Conversation Models\" 2016 NAACL full authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "348bc1fb-a5da-418e-a3f6-74d162f8ef32",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR415sNirVghuHF7dVsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e2bd111-ecb1-46ef-975f-23fdbe659735",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Y4TDAQa4Afk3XGtjZQBk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5535,
      "cache_read_input_tokens": 117675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5535,
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

_source line 82 · 2026-05-26T10:51:20.682Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014BNbERkP41jcTS1S8iQYmY`</summary>

```json
{
  "query": "Gambetta \"Learning by Surprise Surplexity\" full authors list arXiv 2410.12341"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e2bd111-ecb1-46ef-975f-23fdbe659735",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR415sNirVghuHF7dVsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "23492b67-76f2-41d6-b1f9-d348958a5333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Y4TDAQa4Afk3XGtjZQBk4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5535,
      "cache_read_input_tokens": 117675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5535,
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

_source line 83 · 2026-05-26T10:51:21.462Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014yUg6he9n1XT3LLSBeckqs`</summary>

```json
{
  "query": "dey2024breaking bib key \"Is Model Collapse Inevitable\" first author Gerstgrasser not Dey"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23492b67-76f2-41d6-b1f9-d348958a5333",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR415sNirVghuHF7dVsx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3b6428a4-1a70-479e-b06b-91ff000841ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Y4TDAQa4Afk3XGtjZQBk4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5535,
      "cache_read_input_tokens": 117675,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5535
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 354,
          "cache_read_input_tokens": 117675,
          "cache_creation_input_tokens": 5535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5535,
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

_source line 84 · 2026-05-26T10:51:23.464Z_

<details><summary>↩ Tool result · `toolu_01CAjKiJh9ZFR9oCRiawB9rb`</summary>

```text
Web search results for query: "dohmatob2024tale "A Tale of Tails" authors full list Pu Yang Francois Charton Julia Kempe ICML 2024"

Links: [{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/a-tale-of-tails-model-collapse-as-a-change-of-scaling-laws"},{"title":"[Quick Review] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://liner.com/review/tale-tails-model-collapse-as-change-scaling-laws"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://proceedings.mlr.press/v235/dohmatob24b.html"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/html/2402.07043"},{"title":"A tale of tails | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692515"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | OpenReview","url":"https://openreview.net/forum?id=KVvku47shW"},{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10535859"}]

Based on the search results, I found the full list of authors for "A Tale of Tails: Model Collapse as a Change of Scaling Laws" published at ICML 2024:

The authors are: Elvis Dohmatob, Yunzhen Feng, Pu Yang, Francois Charton, and Julia Kempe.

The paper was published in the Proceedings of the 41st International Conference on Machine Learning, PMLR 235:11165-11197, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fe6dd2e-c667-4840-b153-7b5509fd22be",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "2e562b3a-a148-4700-bec4-f3896c9b7406",
  "sourceToolAssistantUUID": "5fe6dd2e-c667-4840-b153-7b5509fd22be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-26T10:51:24.349Z_

<details><summary>↩ Tool result · `toolu_018NuZch5qYhYxT54eueWT8J`</summary>

```text
Web search results for query: "arXiv 2510.05133 Du Wu Tang Wang Fan full authors list "Characterizing Model Behavior""

Links: [{"title":"[2510.05133] Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios","url":"https://arxiv.org/abs/2510.05133"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/pastweek?skip=424&show=1000"},{"title":"Artificial Intelligence Jan 2025","url":"https://arxiv.org/list/cs.AI/2025-01?skip=1250&show=2000"},{"title":"Lei Wang's articles on arXiv","url":"https://arxiv.org/a/wang_l_1.html"},{"title":"Computation and Language authors/titles recent ... - APS arXiv Mirror","url":"https://aps.arxiv.org/list/cs.CL/pastweek?show=321"}]

Based on the search results, the authors of arXiv paper 2510.05133 "Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios" are Y. Du, G. Wu, G. Tang, W. Wang, and Q. Fan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "348bc1fb-a5da-418e-a3f6-74d162f8ef32",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "6e25d6d7-fc6c-44fd-974f-d7738675c3bf",
  "sourceToolAssistantUUID": "348bc1fb-a5da-418e-a3f6-74d162f8ef32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-26T10:51:26.537Z_

<details><summary>↩ Tool result · `toolu_01WTo3DsQ4GLas2akAcbaso3`</summary>

```text
Web search results for query: "Li Jiwei "Diversity-Promoting Objective Function Neural Conversation Models" 2016 NAACL full authors"

Links: [{"title":"A Diversity-Promoting Objective Function for Neural Conversation Models - ACL Anthology","url":"https://aclanthology.org/N16-1014/"},{"title":"[1510.03055] A Diversity-Promoting Objective Function for Neural Conversation Models","url":"https://arxiv.org/abs/1510.03055"},{"title":"Jiwei's Homepage","url":"https://nlp.stanford.edu/~bdlijiwei/Publications_ByTopic.html"},{"title":"dblp: A Diversity-Promoting Objective Function for Neural Conversation Models.","url":"https://dblp.org/rec/conf/naacl/LiGBGD16.html"},{"title":"A Diversity-Promoting Objective Function for Neural Conversation Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/N16-1014@ACL"},{"title":"A Diversity-Promoting Objective Function for Neural Conversation Models | Request PDF","url":"https://www.researchgate.net/publication/305334287_A_Diversity-Promoting_Objective_Function_for_Neural_Conversation_Models"},{"title":"A Diversity-Promoting Objective Function for Neural Conversation Models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/a-diversity-promoting-objective-function-for-neural-conversation-models/"},{"title":"[1510.03055v3] A Diversity-Promoting Objective Function for Neural Conversation Models","url":"https://arxiv.org/abs/1510.03055v3"}]

Based on the search results, here are the full authors for the 2016 NAACL paper "A Diversity-Promoting Objective Function for Neural Conversation Models":

The authors are Jiwei Li, Michel Galley, Chris Brockett, Jianfeng Gao, and Bill Dolan.

The paper was published in the Proceedings of the 2016 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 110–119, San Diego, California.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e2bd111-ecb1-46ef-975f-23fdbe659735",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "c5251184-14f7-4b9b-b834-3110b2ec3cb8",
  "sourceToolAssistantUUID": "0e2bd111-ecb1-46ef-975f-23fdbe659735",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-26T10:51:28.431Z_

<details><summary>↩ Tool result · `toolu_014BNbERkP41jcTS1S8iQYmY`</summary>

```text
Web search results for query: "Gambetta "Learning by Surprise Surplexity" full authors list arXiv 2410.12341"

Links: [{"title":"[2410.12341] Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/abs/2410.12341"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/pdf/2410.12341"},{"title":"[2410.12341v1] A linguistic analysis of undesirable outcomes in the era of generative AI","url":"https://www.arxiv.org/abs/2410.12341v1"},{"title":"Machine Learning Oct 2024","url":"https://arxiv.org/list/cs.LG/2024-10?skip=3200&show=2000"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=2575&show=2000"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=400&show=2000"}]

Based on the search results, I found the full authors list for the paper "Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI" (arXiv 2410.12341):

The authors are: Daniele Gambetta, Gizem Gezici, Fosca Giannotti, Dino Pedreschi, Alistair Knott, and Luca Pappalardo.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23492b67-76f2-41d6-b1f9-d348958a5333",
  "isSidechain": true,
  "promptId": "7c3dea0f-ffa7-4eda-9a04-bb2cecd2df26",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "29b20504-7010-4eca-8132-feaf1adf4156",
  "sourceToolAssistantUUID": "23492b67-76f2-41d6-b1f9-d348958a5333",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-26T10:51:29.901Z_

<details><summary>↩ Tool result · `toolu_014yUg6he9n1XT3LLSBeckqs`</summary>

```text
Web search results for query: "dey2024breaking bib key "Is Model Collapse Inevitable" first author Gerstgrasser not Dey"

Links: [{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Experts divided over training AI with more data from AI • The Register","url":"https://www.theregister.com/2024/05/09/ai_model_collapse/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Addressing Concerns of Model Collapse from Synthetic Data in AI","url":"https://www.gretel.ai/blog/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai"},{"title":"[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-Model-Collapse-Inevitable-Breaking-the-Curse-of-Gerstgrasser-Schaeffer/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"Generative AI: Model Collapse and Brand Message Distortion – When Prog","url":"https://saas-advisor.com/en/blogs/news/generative-ai-model-collapse-brand-message-distortion"}]

I found the paper you're looking for! 

The paper "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" is authored by Matthias Gerstgrasser and 13 other authors. 

The full author list includes: Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Tomasz Korbak, Rajashree Agrawal, Henry Sleight, John Hughes, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, and Sanmi Koyejo.

The paper was published in April 2024, with arXiv preprint arXiv:2404.01413.

The key finding is that "if data accumulates and models train on a mixture of 'real' and synthetic data, model collapse no longer occurs."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b6428a4-1a70-479e-b06b-91ff000841ac",
  "isSidechain": true,
  "promptId": "1dc476d9-f54c-4c00-98e8-d4bcee01cbe4",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "a7c03a41-1fa8-4d3e-bcb0-8287c2c7a710",
  "sourceToolAssistantUUID": "3b6428a4-1a70-479e-b06b-91ff000841ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Assistant

_source line 89 · 2026-05-26T10:51:33.103Z_

Now let me verify the NeurIPS 2025 venue for gu2025datamixing and check a few more entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7c03a41-1fa8-4d3e-bcb0-8287c2c7a710",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR42QrfQQqVVSWa2Keah",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7ae87607-4fdb-4803-a138-b2537452d8a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qRr2HcrvMPsc4LB7QdPhL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3226,
      "cache_read_input_tokens": 123210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3226,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 90 · 2026-05-26T10:51:34.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FoA3jmXq3BQhFbgb6CJxVJ`</summary>

```json
{
  "query": "Gu Liang Pehlevan \"Data Mixing Phase Transitions\" NeurIPS 2025 Spotlight full author list Xinran Gu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ae87607-4fdb-4803-a138-b2537452d8a0",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR42QrfQQqVVSWa2Keah",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "02bfebb1-e32e-4c40-a433-02d52ed07f91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qRr2HcrvMPsc4LB7QdPhL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3226,
      "cache_read_input_tokens": 123210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3226,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 91 · 2026-05-26T10:51:35.514Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xi47NRF9VHaDf7sZLDEo3H`</summary>

```json
{
  "query": "Drayson \"Machine-generated text detection prevents language model collapse\" EMNLP 2025 venue published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02bfebb1-e32e-4c40-a433-02d52ed07f91",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR42QrfQQqVVSWa2Keah",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0141c51a-96a8-4b59-9c0e-fade787e7d09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qRr2HcrvMPsc4LB7QdPhL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3226,
      "cache_read_input_tokens": 123210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3226,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 92 · 2026-05-26T10:51:36.469Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JEgcbUZr2AoW4RNuPDTmfe`</summary>

```json
{
  "query": "Schaeffer \"Position Model Collapse Does Not Mean\" ICML 2025 accepted venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0141c51a-96a8-4b59-9c0e-fade787e7d09",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR42QrfQQqVVSWa2Keah",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fefdd341-fa25-415d-bf93-4a4a8525e9b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qRr2HcrvMPsc4LB7QdPhL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3226,
      "cache_read_input_tokens": 123210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3226,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 93 · 2026-05-26T10:51:36.722Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017f2YaTRaU6xpLibCEmnRG1`</summary>

```json
{
  "query": "Gerstgrasser 2404.01413 \"Is Model Collapse Inevitable\" venue ICML 2024 published proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fefdd341-fa25-415d-bf93-4a4a8525e9b8",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR42QrfQQqVVSWa2Keah",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8034aa2f-a489-4df0-a276-4c0b8e4bbfad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015qRr2HcrvMPsc4LB7QdPhL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3226,
      "cache_read_input_tokens": 123210,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3226
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 300,
          "cache_read_input_tokens": 123210,
          "cache_creation_input_tokens": 3226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3226,
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

_source line 94 · 2026-05-26T10:51:42.440Z_

<details><summary>↩ Tool result · `toolu_01FoA3jmXq3BQhFbgb6CJxVJ`</summary>

```text
Web search results for query: "Gu Liang Pehlevan "Data Mixing Phase Transitions" NeurIPS 2025 Spotlight full author list Xinran Gu"

Links: [{"title":"NeurIPS Poster Data Mixing Can Induce Phase Transitions in Knowledge Acquisition","url":"https://neurips.cc/virtual/2025/poster/115595"},{"title":"Publications | Pehlevan Group","url":"https://pehlevan.seas.harvard.edu/publications"},{"title":"[2505.18091] Data Mixing Can Induce Phase Transitions in Knowledge Acquisition","url":"https://arxiv.org/abs/2505.18091"},{"title":"NeurIPS Poster A Closer Look at NTK Alignment: Linking Phase Transitions in Deep Image Regression","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118981"},{"title":"ICLR Spotlight Presentation: Xinran Gu 📊 Data Mixing Can Induce Phase Transitions in Knowledge Acquisition","url":"https://iclr.cc/virtual/2025/36887"},{"title":"NeurIPS 2024 presentations from our group | Pehlevan Group","url":"https://pehlevan.seas.harvard.edu/news/neurips-2024-presentations-our-group"},{"title":"NeurIPS 2025 Wednesday 12/3","url":"https://neurips.cc/virtual/2025/loc/mexico-city/day/12/3"}]

Based on the search results, I found information about the paper "Data Mixing Can Induce Phase Transitions in Knowledge Acquisition" presented at NeurIPS 2025 as a Spotlight.

The full author list for this Spotlight paper is: Xinran Gu, Kaifeng Lyu, Jiazheng Li, and Jingzhao Zhang.

However, I should note that while the search results confirm this is a NeurIPS 2025 Spotlight presentation, I did not find evidence that Cengiz Pehlevan (from the Pehlevan group at Harvard) is listed as an author on this particular paper, despite the search including his name in the query. The paper appears to be authored by the four individuals listed above.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02bfebb1-e32e-4c40-a433-02d52ed07f91",
  "isSidechain": true,
  "promptId": "1dc476d9-f54c-4c00-98e8-d4bcee01cbe4",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "9599d5bd-7313-4372-9f0f-02055f06dcc1",
  "sourceToolAssistantUUID": "02bfebb1-e32e-4c40-a433-02d52ed07f91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-26T10:51:42.730Z_

<details><summary>↩ Tool result · `toolu_01Xi47NRF9VHaDf7sZLDEo3H`</summary>

```text
Web search results for query: "Drayson "Machine-generated text detection prevents language model collapse" EMNLP 2025 venue published"

Links: [{"title":"[2502.15654] Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/abs/2502.15654"},{"title":"(PDF) Machine-generated text detection prevents language model collapse","url":"https://www.researchgate.net/publication/397412242_Machine-generated_text_detection_prevents_language_model_collapse"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654"},{"title":"Machine-generated text detection prevents language model ...","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/1/2025.emnlp-main.1506.pdf"},{"title":"Machine-generated text detection prevents language model collapse - UCL Discovery","url":"https://discovery.ucl.ac.uk/id/eprint/10217226/"},{"title":"Machine-generated text detection prevents language ...","url":"https://omega.cs.ucl.ac.uk/assets/pdf/papers/drayson2025-model-collapse.pdf"},{"title":"GitHub - GeorgeDrayson/model_collapse","url":"https://github.com/GeorgeDrayson/model_collapse"},{"title":"Computation and Language Feb 2025","url":"https://www.arxiv.org/list/cs.CL/2025-02?skip=1325&show=250"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/html/2410.12341v3"}]

Based on the search results, here's what I found about the paper:

The paper "Machine-generated text detection prevents language model collapse" by George Drayson, Emine Yilmaz, and Vasileios Lampos was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025). The conference took place November 4-9, 2025, and according to ResearchGate, the venue was in Suzhou, China.

The paper was accepted by EMNLP 2025 (main). The paper is also available on arXiv as arXiv paper 2502.15654, and source code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0141c51a-96a8-4b59-9c0e-fade787e7d09",
  "isSidechain": true,
  "promptId": "1dc476d9-f54c-4c00-98e8-d4bcee01cbe4",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "ad31f635-f8bd-4512-901a-f45f72e40792",
  "sourceToolAssistantUUID": "0141c51a-96a8-4b59-9c0e-fade787e7d09",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-26T10:51:44.329Z_

<details><summary>↩ Tool result · `toolu_017f2YaTRaU6xpLibCEmnRG1`</summary>

```text
Web search results for query: "Gerstgrasser 2404.01413 "Is Model Collapse Inevitable" venue ICML 2024 published proceedings"

Links: [{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of","url":"https://arxiv.org/pdf/2404.01413"},{"title":"[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413v1"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-Model-Collapse-Inevitable-Breaking-the-Curse-of-Gerstgrasser-Schaeffer/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"Accumulating Data Prevents Model Collapse","url":"https://www.emergentmind.com/papers/2404.01413"},{"title":"ICML Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://icml.cc/virtual/2024/36382"},{"title":"AI-Powered Paper Summarization about the arXiv paper 2404.01413v1","url":"https://www.summarizepaper.com/en/arxiv-id/2404.01413v1/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"}]

Based on the search results, I found information about this paper:

The paper "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data" is authored by Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, and Sanmi Koyejo.

The paper was initially submitted to arXiv on April 1, 2024, with a revised version on April 29, 2024 (arXiv:2404.01413). The paper addresses model collapse in model-data feedback loops and was presented at ICML 2024.

The paper shows that accumulating data prevents model collapse, contrasting with earlier studies that assumed data replacement over time. The research includes both theoretical analysis and empirical validation across different types of generative models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8034aa2f-a489-4df0-a276-4c0b8e4bbfad",
  "isSidechain": true,
  "promptId": "1dc476d9-f54c-4c00-98e8-d4bcee01cbe4",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "e8af62bc-3eee-457c-8ee2-97e1760c9250",
  "sourceToolAssistantUUID": "8034aa2f-a489-4df0-a276-4c0b8e4bbfad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-26T10:51:45.507Z_

<details><summary>↩ Tool result · `toolu_01JEgcbUZr2AoW4RNuPDTmfe`</summary>

```text
Web search results for query: "Schaeffer "Position Model Collapse Does Not Mean" ICML 2025 accepted venue"

Links: [{"title":"1 Introduction","url":"https://arxiv.org/html/2503.03150v2"},{"title":"[2503.03150] Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/abs/2503.03150"},{"title":"Position: Model Collapse Does Not Mean What You Think","url":"https://arxiv.org/pdf/2503.03150"},{"title":"ICML Poster Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://icml.cc/virtual/2025/poster/44713"},{"title":"Position: Model Collapse Does Not Mean What You Think - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250303150S/abstract"},{"title":"Position: the Stochastic Parrot in the Coal Mine Model Collapse is a Threat to Low-Resource Communities","url":"https://arxiv.org/html/2605.04127"},{"title":"Position: Model Collapse Does Not Mean What You Think | OpenReview","url":"https://openreview.net/forum?id=ygfzWIGDN8"},{"title":"42nd ICML 2025: Vancouver, BC, Canada","url":"https://dblp.org/db/conf/icml/icml2025.html"}]

Based on the search results, I found information about the paper, though I should note that the specific ICML 2025 acceptance status requires clarification:

The paper "Position: Model Collapse Does Not Mean What You Think" is authored by Rylan Schaeffer, Joshua Kazdan, Alvan Caleb Arulandu, and Sanmi Koyejo, with affiliations at Stanford Computer Science, Stanford Statistics, and Harvard University.

The paper highlights that research on model collapse actually encompasses eight distinct and at times conflicting definitions of model collapse, and argues that inconsistent terminology within and between papers has hindered building a comprehensive understanding of model collapse.

However, regarding the venue, the search results show some complexity: The paper appears to have been submitted to NeurIPS 2025 Position Paper Track according to OpenReview. Additionally, Joshua Kazdan and Rylan Schaeffer appear to be involved with related work on this topic at ICML, though this appears to be a different paper titled "Collapse or Thrive: Perils and Promises of Synthetic Data in a Self-Generating World."

The paper was uploaded to arXiv on March 5, 2025, suggesting it may have been under review at multiple venues around that time.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fefdd341-fa25-415d-bf93-4a4a8525e9b8",
  "isSidechain": true,
  "promptId": "1dc476d9-f54c-4c00-98e8-d4bcee01cbe4",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "d6fe3baf-fd7b-489d-a729-547440229b8f",
  "sourceToolAssistantUUID": "fefdd341-fa25-415d-bf93-4a4a8525e9b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Assistant

_source line 98 · 2026-05-26T10:51:48.189Z_

Now let me verify a few more specific details about entries with potential issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6fe3baf-fd7b-489d-a729-547440229b8f",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR43Zg1jPhdKYzR261ci",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a14a531f-dac1-4d89-8eaf-5207421388db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qbz98vxudMkzxCavV13LKz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 2210,
      "cache_read_input_tokens": 126436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2210,
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

_source line 99 · 2026-05-26T10:51:49.607Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JWtmnGk1PB8sFhzsM9oM9b`</summary>

```json
{
  "query": "truong2026phase bib year arXiv 2512.12381 submitted December 2024 or 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a14a531f-dac1-4d89-8eaf-5207421388db",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR43Zg1jPhdKYzR261ci",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f027f339-1f68-4111-8fa6-1ea9a4d47807",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qbz98vxudMkzxCavV13LKz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 2210,
      "cache_read_input_tokens": 126436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2210,
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

_source line 100 · 2026-05-26T10:51:50.549Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015zs3W8zffNvEEP4HDDKiDq`</summary>

```json
{
  "query": "gu2025datamixing authors \"Hayden Liang\" or \"Kaifeng Lyu\" \"Cengiz Pehlevan\" or \"Jingzhao Zhang\" arXiv 2505.18091"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f027f339-1f68-4111-8fa6-1ea9a4d47807",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR43Zg1jPhdKYzR261ci",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac689851-b3b2-4bd5-92d5-8a7c4b40218d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qbz98vxudMkzxCavV13LKz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 2210,
      "cache_read_input_tokens": 126436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2210,
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

_source line 101 · 2026-05-26T10:51:52.043Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015reEaKQajc9rTkvSvFXdUo`</summary>

```json
{
  "query": "Coretta Casillas Roessig \"Multidimensional Signals Analytic Flexibility\" 2023 doi 10.1177/25152459231162567"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac689851-b3b2-4bd5-92d5-8a7c4b40218d",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR43Zg1jPhdKYzR261ci",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5ca688f5-8b5e-4010-a663-9f18155b5dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qbz98vxudMkzxCavV13LKz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 804,
      "cache_creation_input_tokens": 2210,
      "cache_read_input_tokens": 126436,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2210
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 804,
          "output_tokens": 260,
          "cache_read_input_tokens": 126436,
          "cache_creation_input_tokens": 2210,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2210,
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

_source line 102 · 2026-05-26T10:51:56.944Z_

<details><summary>↩ Tool result · `toolu_01JWtmnGk1PB8sFhzsM9oM9b`</summary>

```text
Web search results for query: "truong2026phase bib year arXiv 2512.12381 submitted December 2024 or 2025"

Links: [{"title":"[2512.12381] Entropy Collapse: A Universal Failure Mode of Intelligent Systems","url":"https://arxiv.org/abs/2512.12381"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems","url":"https://arxiv.org/pdf/2512.12381"},{"title":"Entropy Collapse: A Universal Failure Mode of Intelligent Systems Exact Phase Transition Analysis, First-Order Discontinuity, and Two Universality Classes","url":"https://arxiv.org/html/2512.12381"},{"title":"[2502.12381] Linear Diffusion Networks","url":"https://arxiv.org/abs/2502.12381"},{"title":"Artificial Intelligence Dec 2025","url":"https://arxiv.org/list/cs.AI/2025-12?skip=375&show=50"},{"title":"[2503.12381] Deepfake Detection with Optimized Hybrid Model: EAR Biometric Descriptor via Improved RCNN","url":"https://arxiv.org/abs/2503.12381"},{"title":"[2501.12381] Parallel Sequence Modeling via Generalized Spatial Propagation Network","url":"https://arxiv.org/abs/2501.12381"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=389&show=2000"},{"title":"weak-to-strong generalization through the data-centric lens","url":"https://arxiv.org/pdf/2412.03881"},{"title":"why model randomness (entropy) collapses during ...","url":"https://www.facebook.com/0xSojalSec/posts/why-model-randomness-entropy-collapses-during-reinforcement-learning-for-reasoni/1375333587454374/"}]

Based on the search results, I found the paper you're looking for:

The paper arXiv:2512.12381 is titled "Entropy Collapse: A Universal Failure Mode of Intelligent Systems" by Truong Xuan Khanh and Truong Quynh Hoa, and was submitted on December 13, 2025.

The paper proves that entropy collapse—the irreversible contraction of effective state space when feedback amplification exceeds novelty regeneration—is a first-order (discontinuous) phase transition. The paper was last revised on March 13, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f027f339-1f68-4111-8fa6-1ea9a4d47807",
  "isSidechain": true,
  "promptId": "1dc476d9-f54c-4c00-98e8-d4bcee01cbe4",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "9f2059a3-0887-470b-9143-aa4912a31c84",
  "sourceToolAssistantUUID": "f027f339-1f68-4111-8fa6-1ea9a4d47807",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-26T10:51:58.188Z_

<details><summary>↩ Tool result · `toolu_015zs3W8zffNvEEP4HDDKiDq`</summary>

```text
Web search results for query: "gu2025datamixing authors "Hayden Liang" or "Kaifeng Lyu" "Cengiz Pehlevan" or "Jingzhao Zhang" arXiv 2505.18091"

Links: [{"title":"[2505.18091] Data Mixing Can Induce Phase Transitions in Knowledge Acquisition","url":"https://arxiv.org/abs/2505.18091"},{"title":"Reliable and efficient inverse analysis using physics-informed neural networks with normalized distance functions and adaptive weight tuning","url":"https://arxiv.org/html/2504.18091"},{"title":"[2504.18091] Reliable and efficient inverse analysis using physics-informed neural networks with normalized distance functions and adaptive weight tuning","url":"https://arxiv.org/abs/2504.18091"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=1825&show=2000"},{"title":"[2510.18091] Accelerating Vision Transformers with Adaptive Patch Sizes","url":"https://arxiv.org/abs/2510.18091"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2402.18091"},{"title":"Computer Vision and Pattern Recognition May 2025","url":"https://arxiv.org/list/cs.CV/2025-05?skip=75&show=1000"},{"title":"[2508.18091] Teaching LLMs to Think Mathematically: A Critical Study of Decision-Making via Optimization","url":"https://arxiv.org/abs/2508.18091"},{"title":"fcthebrave (Fu Cong)","url":"https://huggingface.co/fcthebrave"},{"title":"KID-22 (Sunhao Dai)","url":"https://huggingface.co/KID-22"}]

Based on the search results, I found the paper you're looking for:

arXiv paper 2505.18091 is titled "Data Mixing Can Induce Phase Transitions in Knowledge Acquisition" with authors Xinran Gu, Kaifeng Lyu, Jiazheng Li, and Jingzhao Zhang. 

However, I should note that the authors listed in the search results are **Xinran Gu, Kaifeng Lyu, Jiazheng Li, and Jingzhao Zhang** — which includes Kaifeng Lyu and Jingzhao Zhang from your query, but does not appear to include Hayden Liang or Cengiz Pehlevan as authors. The paper has been accepted as a NeurIPS'25 Spotlight.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac689851-b3b2-4bd5-92d5-8a7c4b40218d",
  "isSidechain": true,
  "promptId": "1dc476d9-f54c-4c00-98e8-d4bcee01cbe4",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "83bdd538-00a5-4e48-afcf-ddebbeee8d93",
  "sourceToolAssistantUUID": "ac689851-b3b2-4bd5-92d5-8a7c4b40218d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-26T10:51:59.877Z_

<details><summary>↩ Tool result · `toolu_015reEaKQajc9rTkvSvFXdUo`</summary>

```text
Web search results for query: "Coretta Casillas Roessig "Multidimensional Signals Analytic Flexibility" 2023 doi 10.1177/25152459231162567"

Links: [{"title":"Multidimensional Signals and Analytic Flexibility: Estimating Degrees of Freedom in Human-Speech Analyses - Stefano Coretta, Joseph V. Casillas, Simon Roessig, Michael Franke, Byron Ahn, Ali H. Al-Hoorie, Jalal Al-Tamimi, Najd E. Alotaibi, Mohammed K. AlShakhori, Ruth M. Altmiller, Pablo Arantes, Angeliki Athanasopoulou, Melissa M. Baese-Berk, George Bailey, Cheman Baira A Sangma, Eleonora J. Beier, Gabriela M. Benavides, Nicole Benker, Emelia P. BensonMeyer, Nina R. Benway, Grant M. Berry, Liwen Bing, Chri","url":"https://journals.sagepub.com/doi/full/10.1177/25152459231162567"},{"title":"Multidimensional signals and analytic flexibility: estimating degrees of freedom in human-speech analyses - Macquarie University","url":"https://researchers.mq.edu.au/en/publications/multidimensional-signals-and-analytic-flexibility-estimating-degr/"},{"title":"Multidimensional Signals and Analytic Flexibility: Estimating Degrees of Freedom in Human-Speech Analyses - Tilburg University Research Portal","url":"https://research.tilburguniversity.edu/en/publications/multidimensional-signals-and-analytic-flexibility-estimating-degr"},{"title":"Multidimensional Signals and Analytic Flexibility: Estimating Degrees of Freedom in Human-Speech Analyses - Princeton University","url":"https://collaborate.princeton.edu/en/publications/multidimensional-signals-and-analytic-flexibility-estimating-degr"},{"title":"Multidimensional signals and analytic flexibility: Estimating degrees of freedom in human-speech analyses - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/multidimensional-signals-and-analytic-flexibility-estimating-degr/"},{"title":"HAL Id: hal-04230571 https://hal.science/hal-04230571v1 Submitted on 6 Oct 2023","url":"https://hal.science/hal-04230571v1/file/coretta-et-al-2023-multidimensional-signals-and-analytic-flexibility-estimating-degrees-of-freedom-in-human-speech.pdf"},{"title":"\"Multidimensional Signals and Analytic Flexibility: Estimating Degrees \" by Stefano Coretta, Joseph V. Casillas et al.","url":"https://scholarsarchive.byu.edu/facpub/7951/"},{"title":"Multidimensional Signals and Analytic Flexibility: Estimating Degrees of Freedom in Human-Speech Analyses - University of Birmingham","url":"https://research.birmingham.ac.uk/en/publications/multidimensional-signals-and-analytic-flexibility-estimating-degr-2"},{"title":"Multidimensional signals and analytic flexibility: Estimating degrees of freedom in human speech analyses - Lancashire Online Knowledge","url":"https://clok.uclan.ac.uk/45561/"},{"title":"Multidimensional Signals and Analytic Flexibility: Estimating Degrees of Freedom in Human-Speech Analyses","url":"https://addi.ehu.es/handle/10810/66212?locale-attribute=eu"}]

I found the article you're looking for. The paper was published in 2023 in the journal *Advances in Methods and Practices in Psychological Science*, volume 6, issue 3, pages 1-29.

However, I should note that the lead author is Stefano Coretta, and Joseph V. Casillas and Simon Roessig are among the co-authors, rather than "Coretta Casillas Roessig" being a single author name. The paper involved giving the same speech-production dataset to 46 teams of researchers and asking them to answer the same research question.

The article is available at the SAGE journals website (https://journals.sagepub.com/doi/full/10.1177/25152459231162567) and appears to be open access based on the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5ca688f5-8b5e-4010-a663-9f18155b5dd1",
  "isSidechain": true,
  "promptId": "1dc476d9-f54c-4c00-98e8-d4bcee01cbe4",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "c29e05da-d725-40f7-a39a-8df84649b71e",
  "sourceToolAssistantUUID": "5ca688f5-8b5e-4010-a663-9f18155b5dd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Assistant

_source line 105 · 2026-05-26T10:52:02.588Z_

Now let me check a few more entries and then the specific venue discrepancies I've found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c29e05da-d725-40f7-a39a-8df84649b71e",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR44czTzARsX2bbjUrVs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1a05e21d-22af-41cd-bea9-471c0a2eed6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhVGqwXjr79ggREk1UzyVu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3576,
      "cache_read_input_tokens": 128646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3576,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 106 · 2026-05-26T10:52:03.659Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L1EL7Pm1YbCYp2jbGvby52`</summary>

```json
{
  "query": "Merity Xiong Bradbury Socher \"Pointer Sentinel Mixture Models\" ICLR 2017 WikiText"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a05e21d-22af-41cd-bea9-471c0a2eed6c",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR44czTzARsX2bbjUrVs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ec51f8c6-ca7b-458c-b199-4f7e5ea016d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhVGqwXjr79ggREk1UzyVu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3576,
      "cache_read_input_tokens": 128646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3576,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 107 · 2026-05-26T10:52:04.667Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GN5ETyqgyAs4BDLcppYVSt`</summary>

```json
{
  "query": "Biderman \"Pythia Suite Analyzing Large Language Models\" ICML 2023 arXiv 2304.01373"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ec51f8c6-ca7b-458c-b199-4f7e5ea016d3",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR44czTzARsX2bbjUrVs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "470b08da-d8bf-473d-b49c-4b179e07839d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhVGqwXjr79ggREk1UzyVu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3576,
      "cache_read_input_tokens": 128646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3576,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
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

_source line 108 · 2026-05-26T10:52:05.548Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XLn3zKq4joPQoK6JTstrzR`</summary>

```json
{
  "query": "Bell Kampman Dodge Lawrence \"Modeling Machine Learning Multiverse\" NeurIPS 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "470b08da-d8bf-473d-b49c-4b179e07839d",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR44czTzARsX2bbjUrVs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "61937008-4dfe-431c-ae92-3af967a98f07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KhVGqwXjr79ggREk1UzyVu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3576,
      "cache_read_input_tokens": 128646,
      "output_tokens": 224,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3576
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 224,
          "cache_read_input_tokens": 128646,
          "cache_creation_input_tokens": 3576,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3576,
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

_source line 109 · 2026-05-26T10:52:13.111Z_

<details><summary>↩ Tool result · `toolu_01GN5ETyqgyAs4BDLcppYVSt`</summary>

```text
Web search results for query: "Biderman "Pythia Suite Analyzing Large Language Models" ICML 2023 arXiv 2304.01373"

Links: [{"title":"[2304.01373] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/abs/2304.01373"},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/pdf/2304.01373"},{"title":"[2304.01373] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://ar5iv.labs.arxiv.org/html/2304.01373"},{"title":"[2304.01373v1] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/abs/2304.01373v1"},{"title":"Paper page - Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://huggingface.co/papers/2304.01373"},{"title":"[PDF] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Pythia:-A-Suite-for-Analyzing-Large-Language-Models-Biderman-Schoelkopf/be55e8ec4213868db08f2c3168ae666001bea4b8"},{"title":"Pythia: A Suite for Analyzing Large Language Models Acros...","url":"https://www.researchhub.com/paper/1275740/pythia-a-suite-for-analyzing-large-language-models-across-training-and-scaling"},{"title":"[2304.01373v2] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/abs/2304.01373v2"},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230401373B/abstract"}]

I found information about the paper you searched for. Here are the key details:

**Paper Title:** Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling

**Authors:** Stella Biderman, Hailey Schoelkopf, Quentin Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, Aviya Skowron, Lintang Sutawika, Oskar van der Wal

**ArXiv Information:** Submitted on 3 Apr 2023 (v1), last revised 31 May 2023 (this version, v2)

**Main Contribution:** The paper introduces Pythia, a suite of 16 LLMs all trained on public data seen in the exact same order and ranging in size from 70M to 12B parameters, with public access to 154 checkpoints for each one of the 16 models, alongside tools to download and reconstruct their exact training dataloaders for further study.

**Research Areas:** The paper presents several case studies including novel results in memorization, term frequency effects on few-shot performance, and reducing gender bias.

**Resources:** Trained models, analysis code, training code, and training data can be found at https://github.com/EleutherAI/pythia.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "470b08da-d8bf-473d-b49c-4b179e07839d",
  "isSidechain": true,
  "promptId": "1dc476d9-f54c-4c00-98e8-d4bcee01cbe4",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "b10dda11-8372-4386-a522-424a6b227d0b",
  "sourceToolAssistantUUID": "470b08da-d8bf-473d-b49c-4b179e07839d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-26T10:52:13.229Z_

<details><summary>↩ Tool result · `toolu_01L1EL7Pm1YbCYp2jbGvby52`</summary>

```text
Web search results for query: "Merity Xiong Bradbury Socher "Pointer Sentinel Mixture Models" ICLR 2017 WikiText"

Links: [{"title":"Published as a conference paper at ICLR 2017 POINTER SENTINEL MIXTURE MODELS","url":"https://openreview.net/pdf?id=Byj72udxe"},{"title":"[1609.07843] Pointer Sentinel Mixture Models","url":"https://arxiv.org/abs/1609.07843"},{"title":"[PDF] Pointer Sentinel Mixture Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Pointer-Sentinel-Mixture-Models-Merity-Xiong/efbd381493bb9636f489b965a2034d529cd56bcd"},{"title":"About Me - Smerity.com","url":"https://smerity.com/abme.html"},{"title":"Pointer Sentinel Mixture Models | Request PDF","url":"https://www.researchgate.net/publication/319770231_Pointer_Sentinel_Mixture_Models"},{"title":"Pointer Sentinel Mixture Models Stephen Merity SMERITY@SALESFORCE.COM","url":"https://arxiv.org/pdf/1609.07843"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Merity%2C+S.%2C+Xiong%2C+C.%2C+Bradbury%2C+J.%2C+and+Socher%2C+R.+Pointer+sentinel+mixture+models.+In+International+Conference+on+Learning+Representations+%282017%29."},{"title":"dblp: Stephen Merity","url":"https://dblp.org/pid/177/9285.html"},{"title":"dblp: Pointer Sentinel Mixture Models.","url":"https://dblp.org/rec/conf/iclr/MerityX0S17.html"}]

I've found the paper you're searching for. Here's what the search results show:

The paper "Pointer Sentinel Mixture Models" by Stephen Merity, Caiming Xiong, James Bradbury, and Richard Socher was published at ICLR 2017 as a poster presentation.

The paper introduces the pointer sentinel mixture architecture for neural sequence models which has the ability to either reproduce a word from the recent context or produce a word from a standard softmax classifier. The pointer sentinel-LSTM model achieves state of the art language modeling performance on the Penn Treebank (70.9 perplexity) while using far fewer parameters than a standard softmax LSTM.

The WikiText Long Term Dependency Language Modeling Dataset was also introduced as part of this work in 2016, and WikiText-2 was being introduced in this dataset.

You can access the paper at the following sources:
- arXiv: https://arxiv.org/abs/1609.07843
- OpenReview: https://openreview.net/pdf?id=Byj72udxe


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec51f8c6-ca7b-458c-b199-4f7e5ea016d3",
  "isSidechain": true,
  "promptId": "1dc476d9-f54c-4c00-98e8-d4bcee01cbe4",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "64e7b40f-8e40-4a00-9f4d-06320964dc30",
  "sourceToolAssistantUUID": "ec51f8c6-ca7b-458c-b199-4f7e5ea016d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-26T10:52:13.282Z_

<details><summary>↩ Tool result · `toolu_01XLn3zKq4joPQoK6JTstrzR`</summary>

```text
Web search results for query: "Bell Kampman Dodge Lawrence "Modeling Machine Learning Multiverse" NeurIPS 2022"

Links: [{"title":"Modeling the Machine Learning Multiverse","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/750337e1301941f81ae31a90e0a1c181-Abstract-Conference.html"},{"title":"[2206.05985] Modeling the Machine Learning Multiverse","url":"https://arxiv.org/abs/2206.05985"},{"title":"[PDF] Modeling the Machine Learning Multiverse | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Modeling-the-Machine-Learning-Multiverse-Bell-Kampman/eefa6192e5d515ff9f9d0f185cfded82fdeb85f1"},{"title":"Modeling the machine learning multiverse | Proceedings of the 36th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3600270.3601608"},{"title":"Modeling the Machine Learning Multiverse Samuel J. Bell1 Onno P. Kampman2","url":"https://arxiv.org/pdf/2206.05985"},{"title":"Modeling the Machine Learning Multiverse | Request PDF","url":"https://www.researchgate.net/publication/361274193_Modeling_the_Machine_Learning_Multiverse"},{"title":"NeurIPS 2022","url":"https://neurips.cc/Conferences/2022/ScheduleMultitrack?event=56484"},{"title":"One Model Many Scores: Using Multiverse Analysis to Prevent Fairness Hacking and Evaluate the Influence of Model Design Decisions | Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency","url":"https://dl.acm.org/doi/10.1145/3630106.3658974"}]

I found the paper you were searching for. Here are the key results:

"Modeling the Machine Learning Multiverse" is a paper by Samuel J. Bell, Onno Kampman, Jesse Dodge, and Neil D. Lawrence that presents a principled framework for making robust and generalizable claims called the multiverse analysis, developed in response to mounting concern about the reliability and credibility of machine learning research.

The framework models the multiverse with a Gaussian Process surrogate and applies Bayesian experimental design to efficiently explore high-dimensional and often continuous ML search spaces.

The framework builds upon the multiverse analysis introduced in response to psychology's own reproducibility crisis.

The paper was published in Advances in Neural Information Processing Systems 35 (NeurIPS 2022) Main Conference Track, and is also available on arXiv. You can access the full paper through the NeurIPS proceedings or arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "61937008-4dfe-431c-ae92-3af967a98f07",
  "isSidechain": true,
  "promptId": "1dc476d9-f54c-4c00-98e8-d4bcee01cbe4",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "ab6bcbde-f515-4581-bf81-c3f1df56b697",
  "sourceToolAssistantUUID": "61937008-4dfe-431c-ae92-3af967a98f07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Assistant

_source line 112 · 2026-05-26T10:52:16.530Z_

Now I have all the information I need. Let me compile the full verification report. Let me also quickly check the du2025scales author initials since those are abbreviated.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab6bcbde-f515-4581-bf81-c3f1df56b697",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR45cKoqWjRwDC9bdSKc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5d4b6e0d-7c15-443e-b3b4-c958748ca682",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjHccRNaTMCUnfyKz8fPdK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2649,
      "cache_read_input_tokens": 132222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2649,
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

_source line 113 · 2026-05-26T10:52:17.991Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Amnj4cvdMtYrWP4CjZM9bf`</summary>

```json
{
  "query": "arXiv 2510.05133 full author names first names \"Y. Du\" \"G. Wu\" \"G. Tang\" \"W. Wang\" \"Q. Fan\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d4b6e0d-7c15-443e-b3b4-c958748ca682",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR45cKoqWjRwDC9bdSKc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5c2f76ed-db0a-4105-9513-625412898154",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjHccRNaTMCUnfyKz8fPdK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2649,
      "cache_read_input_tokens": 132222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2649,
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

_source line 114 · 2026-05-26T10:52:18.883Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0168RB5zwsEUorxQD4wNpnQ3`</summary>

```json
{
  "query": "kovac2025recursive EMNLP 2025 \"Proceedings of the Conference on Empirical Methods\" correct venue name"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c2f76ed-db0a-4105-9513-625412898154",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR45cKoqWjRwDC9bdSKc",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7a7b9c46-597d-4d87-a83e-241b601dee7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjHccRNaTMCUnfyKz8fPdK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2649,
      "cache_read_input_tokens": 132222,
      "output_tokens": 190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2649
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 190,
          "cache_read_input_tokens": 132222,
          "cache_creation_input_tokens": 2649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2649,
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

_source line 115 · 2026-05-26T10:52:24.920Z_

<details><summary>↩ Tool result · `toolu_01Amnj4cvdMtYrWP4CjZM9bf`</summary>

```text
Web search results for query: "arXiv 2510.05133 full author names first names "Y. Du" "G. Wu" "G. Tang" "W. Wang" "Q. Fan""

Links: [{"title":"[2510.05133] Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios","url":"https://arxiv.org/abs/2510.05133"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=35875&show=500"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1259&show=1000"},{"title":"Computer Science Oct 2025","url":"https://arxiv.org/list/cs/2025-10?skip=1600"},{"title":"arXiv.org | 232753 Publications | 16958 Citations | Top authors | Related journals","url":"https://scispace.com/journals/arxiv-org-bl5k1ptr"},{"title":"arXiv:2204.05133v2 [cs.AI] 19 Jul 2022","url":"https://arxiv.org/pdf/2204.05133"},{"title":"Multi-layer 5D Optical Data Storage: Mathematical Modeling and Deep Learning-Based Reconstruction of Birefringent Parameters","url":"https://arxiv.org/pdf/2508.20106"}]

Based on the search results, the authors of arXiv 2510.05133 are Y. Du, G. Wu, G. Tang, W. Wang, and Q. Fan. However, the search results only show the abbreviated names (first initials and last names), not the full first names of these authors. The arXiv abstract page does not provide the complete first names for these researchers.

To obtain the full author names with first names spelled out, you would need to access the full PDF of the paper or check the paper's metadata on the arXiv website directly, as this information is typically found in the complete author list on the paper itself rather than in the abstract page.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c2f76ed-db0a-4105-9513-625412898154",
  "isSidechain": true,
  "promptId": "1dc476d9-f54c-4c00-98e8-d4bcee01cbe4",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "7f5bb64f-e1c9-4ee4-9972-be07ff9f1bbc",
  "sourceToolAssistantUUID": "5c2f76ed-db0a-4105-9513-625412898154",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-26T10:52:25.551Z_

<details><summary>↩ Tool result · `toolu_0168RB5zwsEUorxQD4wNpnQ3`</summary>

```text
Web search results for query: "kovac2025recursive EMNLP 2025 "Proceedings of the Conference on Empirical Methods" correct venue name"

Links: [{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - EMNLP 2025","url":"https://2025.emnlp.org/"},{"title":"EMNLP 2025 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2025%2FConference"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP 2025 Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/emnlp-paper-list/emnlp-2025-paper-list/"},{"title":"2025 EMNLP Conference Registration","url":"https://acl.swoogo.com/emnlp2025"},{"title":"EMNLP 2025 : Empirical Methods in Natural Language Processing","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=187880"},{"title":"EMNLP 2025 (@emnlpmeeting) / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"Causal Transformers Perform Below Chance on Recursive Nested   Constructions, Unlike Humans","url":"https://arxiv.org/pdf/2110.07240"}]

Based on the search results, I found information about EMNLP 2025:

The 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) will be held in Suzhou, China from November 4th to November 9th, 2025.

Regarding the correct venue name for proceedings, the proceedings are titled "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing".

However, I didn't find specific information about a paper with the identifier "kovac2025recursive" in the search results. If you're looking for a specific paper, you might want to search the ACL Anthology or EMNLP 2025 proceedings directly, or provide additional details about the paper's content or authors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a7b9c46-597d-4d87-a83e-241b601dee7f",
  "isSidechain": true,
  "promptId": "1dc476d9-f54c-4c00-98e8-d4bcee01cbe4",
  "agentId": "ac7763ed9e49a33d3",
  "type": "user",
  "uuid": "24035afd-1eb6-4a87-b1d5-a1bd7f061629",
  "sourceToolAssistantUUID": "7a7b9c46-597d-4d87-a83e-241b601dee7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth"
}
```

</details>

---

### Assistant

_source line 117 · 2026-05-26T10:54:34.669Z_

Now I have all the data needed for a comprehensive verification report. Let me compile it.

---

## CITATION VERIFICATION REPORT

### PART 1: BIB ENTRY VERIFICATION

---

**1. shapley1953value** -- Shapley, "A Value for n-Person Games"
- BIB STATUS: ✅ Classic reference. Title, author, year, publisher all correct.

**2. shumailov2024curse** -- Shumailov et al., "The Curse of Recursion"
- BIB STATUS: ⚠️ Published in **Nature, vol. 631** (2024). The bib entry is missing volume/pages. Not critical but incomplete.

**3. alemohammad2024mad** -- Alemohammad et al., "Self-Consuming Generative Models Go MAD"
- BIB STATUS: ✅ Confirmed published at ICLR 2024. Authors match.

**4. dohmatob2024tale** -- Dohmatob, Feng, and others, "A Tale of Tails"
- BIB STATUS: ⚠️ The `and others` hides three authors. Full list is: Elvis Dohmatob, Yunzhen Feng, **Pu Yang, Francois Charton, Julia Kempe**. The bib uses "and others" which omits 3 of 5 authors. Confirmed published at ICML 2024.

**5. dohmatob2025strong** -- Dohmatob et al., "Strong Model Collapse"
- BIB STATUS: ✅ Confirmed published at ICLR 2025. Authors match exactly.

**6. du2026geometric** -- Du and Tanaka-Ishii, "Escaping Mode Collapse in LLM Generation via Geometric Regulation"
- BIB STATUS: ✅ Confirmed arXiv 2605.00435, May 2026. Authors and title match.

**7. du2025scales** -- Du, Wu, Tang, Wang, Fan, "Characterizing Model Behavior Under Synthetic Data Training"
- BIB STATUS: ⚠️ Author names use only initials (Y. Du, G. Wu, etc.). While this matches arXiv metadata, full first names would be better practice. The paper is an arXiv preprint from October 2025; year=2025 is correct.

**8. gambetta2024surplexity** -- Gambetta and others, "Learning by Surprise: Surplexity"
- BIB STATUS: ⚠️ `and others` hides 5 co-authors. Full list: Daniele Gambetta, **Gizem Gezici, Fosca Giannotti, Dino Pedreschi, Alistair Knott, Luca Pappalardo**. Year should be 2024 (submitted Oct 2024, revised Sep 2025 as v3). The bib `year=2024` is acceptable since original submission was 2024.

**9. sigma2026spectral** -- Gu et al., "SIGMA: Scalable Spectral Insights"
- BIB STATUS: ✅ Confirmed arXiv 2601.03385, Jan 2026. Authors match exactly.

**10. li2016diversity** -- Li and others, "A Diversity-Promoting Objective Function"
- BIB STATUS: ⚠️ `and others` hides 4 co-authors. Full list: Jiwei Li, **Michel Galley, Chris Brockett, Jianfeng Gao, Bill Dolan**. Venue in bib says "North American Chapter of the Association for Computational Linguistics" -- correct (NAACL-HLT 2016).

**11. kazdan2025collapse** -- Kazdan et al., "Collapse or Thrive?"
- BIB STATUS: ✅ Confirmed published at ICML 2025. Authors match.

**12. dey2024breaking** -- bib key says "dey2024breaking" but the first author is **Matthias Gerstgrasser**, not Apratim Dey.
- BIB STATUS: ❌ **Misattributed bib key.** The bib key `dey2024breaking` suggests Dey is the first author, but the `author` field correctly lists Gerstgrasser as first author. The key is misleading but the content is technically correct. Venue: confirmed ICML 2024. However, the bib key is inconsistent with the author field.

**13. dces2026counter** -- Zhu and Xie, "Countering Model Collapse via Dynamic Center-Edge Sampling"
- BIB STATUS: ⚠️ The journal field says "Electronics" and year 2026, which matches. However, the MDPI URL in the bib is `https://www.mdpi.com/2079-9292/15/4/869` -- the journal ISSN 2079-9292 is correct for Electronics (MDPI). Volume/number/pages should be added (vol. 15, no. 4, article 869).

**14. drayson2025detection** -- Drayson et al., "Machine-generated text detection prevents language model collapse"
- BIB STATUS: ⚠️ Listed as `arXiv preprint arXiv:2502.15654`. However, this paper was **published at EMNLP 2025** (Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pp. 29645-29661). The bib should be updated to reflect the conference publication.

**15. bell2022modeling** -- Bell et al., "Modeling the Machine Learning Multiverse"
- BIB STATUS: ✅ Confirmed NeurIPS 2022. Authors match.

**16. kapoor2024reforms** -- Kapoor et al., "REFORMS"
- BIB STATUS: ✅ Confirmed Science Advances, 2024. DOI correct.

**17. coretta2023multidimensional** -- Coretta et al., "Multidimensional Signals"
- BIB STATUS: ✅ Confirmed AMPPS, 2023. DOI correct.

**18. simonsohn2020specification** -- Simonsohn et al., "Specification curve analysis"
- BIB STATUS: ✅ Confirmed Nature Human Behaviour, 2020. DOI correct.

**19. steegen2016increasing** -- Steegen et al., "Increasing Transparency Through a Multiverse Analysis"
- BIB STATUS: ✅ Confirmed Perspectives on Psychological Science, 2016. DOI correct.

**20. silberzahn2018many** -- Silberzahn et al., "Many Analysts, One Data Set"
- BIB STATUS: ✅ Confirmed AMPPS, 2018. DOI correct.

**21. kirchenbauer2023watermark** -- Kirchenbauer et al., "A Watermark for Large Language Models"
- BIB STATUS: ✅ Confirmed ICML 2023. Pages match.

**22. runge2019detecting** -- Runge et al., "Detecting and quantifying causal associations"
- BIB STATUS: ✅ Confirmed Science Advances, 2019. DOI correct.

**23. schaeffer2025position** -- Schaeffer et al., "Position: Model Collapse Does Not Mean What You Think"
- BIB STATUS: ⚠️ Listed as `arXiv preprint arXiv:2503.03150`. The paper appears on OpenReview for a NeurIPS 2025 Position Paper Track submission. If it was accepted there, the bib should be updated. If still only arXiv, the current listing is acceptable.

**24. granger1969investigating** -- Granger, "Investigating Causal Relations"
- BIB STATUS: ✅ Classic reference. Econometrica, 1969.

**25. shojaie2022granger** -- Shojaie and Fox, "Granger Causality: A Review"
- BIB STATUS: ✅ Confirmed Annual Review of Statistics and Its Application, 2022.

**26. tank2021neural** -- Tank et al., "Neural Granger Causality"
- BIB STATUS: ✅ Confirmed IEEE TPAMI, 2021. DOI correct.

**27. granger1974spurious** -- Granger and Newbold, "Spurious Regressions"
- BIB STATUS: ✅ Classic reference. Journal of Econometrics, 1974.

**28. toda1995statistical** -- Toda and Yamamoto, "Statistical Inference in VARs"
- BIB STATUS: ✅ Confirmed Journal of Econometrics, 1995.

**29. schreiber2000measuring** -- Schreiber, "Measuring Information Transfer"
- BIB STATUS: ✅ Confirmed Physical Review Letters, 2000.

**30. staniek2008symbolic** -- Staniek and Lehnertz, "Symbolic Transfer Entropy"
- BIB STATUS: ✅ Confirmed Physical Review Letters, 2008.

**31. pillutla2021mauve** -- Pillutla et al., "MAUVE"
- BIB STATUS: ✅ Confirmed NeurIPS 2021.

**32. naeini2015obtaining** -- Naeini et al., "Obtaining Well Calibrated Probabilities"
- BIB STATUS: ✅ Confirmed AAAI 2015.

**33. scheffer2009early** -- Scheffer et al., "Early-warning signals for critical transitions"
- BIB STATUS: ✅ Confirmed Nature, 2009. DOI correct.

**34. scheffer2012anticipating** -- Scheffer et al., "Anticipating Critical Transitions"
- BIB STATUS: ✅ Confirmed Science, 2012. DOI correct.

**35. boettiger2012limits** -- Boettiger and Hastings, "Quantifying Limits to Detection"
- BIB STATUS: ✅ Confirmed JRSI, 2012. DOI correct.

**36. gu2024cmr** -- Gu et al., "CMR Scaling Law"
- BIB STATUS: ✅ Confirmed EMNLP 2024. Authors match.

**37. gu2025datamixing** -- Gu, Liang, Pehlevan, "Data Mixing Can Induce Phase Transitions"
- BIB STATUS: ❌ **Wrong authors.** The actual authors are **Xinran Gu, Kaifeng Lyu, Jiazheng Li, and Jingzhao Zhang**. The bib lists "Gu, Xinran and Liang, Hayden and Pehlevan, Cengiz" -- none of Lyu, Li, or Zhang appear, and "Hayden Liang" and "Cengiz Pehlevan" are not authors of this paper. Additionally, the note says "Spotlight" but NeurIPS 2025 lists it as a **Poster** (though an ICLR 2025 Spotlight presentation also exists, suggesting confusion between venues). The bib venue says "Advances in Neural Information Processing Systems" (NeurIPS 2025) -- but this needs author correction.

**38. biderman2023pythia** -- Biderman et al., "Pythia"
- BIB STATUS: ✅ Confirmed ICML 2023. Authors match.

**39. merity2017pointer** -- Merity et al., "Pointer Sentinel Mixture Models"
- BIB STATUS: ✅ Confirmed ICLR 2017.

**40. page1954continuous** -- Page, "Continuous Inspection Schemes"
- BIB STATUS: ✅ Classic reference. Biometrika, 1954.

**41. phipson2010permutation** -- Phipson and Smyth, "Permutation P-values Should Never Be Zero"
- BIB STATUS: ✅ Confirmed. Journal and DOI correct.

**42. truong2026phase** -- Truong and Truong, "Entropy Collapse: A Universal Failure Mode"
- BIB STATUS: ⚠️ The bib has `year = {2025}` but the bib key says `truong2026phase`. The arXiv paper was submitted December 2025, so year=2025 is correct. The bib key is inconsistent with the year field. Also missing the URL field.

**43. benjamini1995controlling** -- Benjamini and Hochberg
- BIB STATUS: ✅ Classic reference. Correct.

**44. benjamini2001control** -- Benjamini and Yekutieli
- BIB STATUS: ✅ Correct.

**45. shi2025closer** -- Shi et al., "A Closer Look at Model Collapse"
- BIB STATUS: ✅ Confirmed NeurIPS 2025 Spotlight. Authors match.

**46. hataya2023will** -- Hataya et al., "Will Large-scale Generative Models Corrupt Future Datasets?"
- BIB STATUS: ✅ Confirmed ICCV 2023, pages 20555-20565.

**47. kovac2025recursive** -- Kovac et al., "Recursive Training Loops in LLMs"
- BIB STATUS: ⚠️ The bib booktitle says "Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)" -- the standard proceedings title is "Proceedings of the **2025** Conference on Empirical Methods in Natural Language Processing". Minor formatting issue. Note says "Oral" which is confirmed.

**48. buffa2026entropy** -- Buffa and Del Corro, "Entropy Sentinel"
- BIB STATUS: ✅ Confirmed arXiv 2601.09001, Jan 2026. Authors match.

---

### PART 2: CITATION CONTEXT VERIFICATION

**introduction.tex:**

1. `\citep{shumailov2024curse,alemohammad2024mad}` -- "language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse"
   - CONTEXT STATUS: ✅ Both papers establish model collapse. Shumailov coins the term; Alemohammad demonstrates it in generative models.

2. `\citep{dohmatob2025strong}` -- "triggered by vanishingly small synthetic fractions"
   - CONTEXT STATUS: ✅ Dohmatob et al. (2025) prove collapse occurs even with tiny synthetic fractions.

3. `\citep{boettiger2012limits}` -- "detection power drops sharply"
   - CONTEXT STATUS: ✅ Boettiger and Hastings study power limits of early-warning detection in short time series.

4. `\citep{truong2026phase}` -- "model collapse is a first-order transition"
   - CONTEXT STATUS: ✅ Truong et al. prove entropy collapse is a first-order (discontinuous) phase transition.

5. `\citep{scheffer2009early}` -- "critical-slowing-down early-warning signals that ecologists rely on"
   - CONTEXT STATUS: ✅ Scheffer et al. (2009) is the seminal paper on early-warning signals for critical transitions in ecology.

6. `\citep{biderman2023pythia}` -- "Pythia-410M"
   - CONTEXT STATUS: ✅ Pythia suite is introduced in Biderman et al.

7. `\citep{li2016diversity}` -- "distinct-n"
   - CONTEXT STATUS: ✅ Li et al. introduce the distinct-n diversity metric.

**method.tex:**

8. `\citep{shumailov2024curse,dohmatob2024tale}` -- "mode amplification"
   - CONTEXT STATUS: ✅ Both papers discuss the mode amplification mechanism underlying model collapse.

9. `\citep{granger1969investigating}` -- "Granger precedence, temporal predictive improvement"
   - CONTEXT STATUS: ✅ Granger (1969) introduces the concept of Granger causality.

10. `\citep{shojaie2022granger}` -- "Granger causality...implies a mechanistic causal link that bivariate tests cannot establish"
    - CONTEXT STATUS: ✅ Shojaie and Fox review limitations of Granger causality, including that bivariate tests cannot establish true causation.

11. `\citep{granger1974spurious}` -- "first-differencing eliminates canary→perplexity associations"
    - CONTEXT STATUS: ✅ Granger and Newbold (1974) establish that spurious regressions arise from shared trends, motivating differencing.

12. `\citep{toda1995statistical}` -- "Toda-Yamamoto"
    - CONTEXT STATUS: ✅ TY procedure for inference in VARs with possibly integrated processes.

13. `\citep{simonsohn2020specification}` -- "multi-method comparison framework"
    - CONTEXT STATUS: ✅ Simonsohn et al. introduce specification-curve analysis.

14. `\citep{phipson2010permutation}` -- "5,000 permutations"
    - CONTEXT STATUS: ✅ Phipson and Smyth provide the formula for permutation p-values (the +1 correction).

15. `\citep{benjamini2001control}` -- "BH-FDR remains valid under positive regression dependence"
    - CONTEXT STATUS: ✅ Benjamini and Yekutieli (2001) prove FDR control under positive dependence.

**related_work.tex:**

16. `\citet{schaeffer2025position}` -- "systematize eight distinct notions of collapse; our operationalization aligns with their distributional shift family (definitions D4-D6)"
    - CONTEXT STATUS: ✅ Schaeffer et al. identify eight definitions of model collapse.

17. `\citet{dohmatob2024tale}` -- "recast collapse as changed scaling-law exponents"
    - CONTEXT STATUS: ✅ Correct characterization of the paper's contribution.

18. `\citet{truong2026phase}` -- "prove entropy collapse is a first-order transition, structurally ruling out critical-slowing-down early-warning signals"
    - CONTEXT STATUS: ✅ The paper proves first-order phase transition with no pre-transition warning.

19. `\citep{scheffer2009early,scheffer2012anticipating}` -- contextually linked to critical-slowing-down
    - CONTEXT STATUS: ✅ Both Scheffer papers are about early-warning signals for critical transitions.

20. `\citet{hataya2023will}` -- "demonstrate that generated images degrade downstream classification on ImageNet-scale data"
    - CONTEXT STATUS: ✅ Correct characterization.

21. `\citet{kovac2025recursive}` -- "show that training data properties (lexical diversity, semantic diversity) modulate the magnitude of recursive collapse in LLMs"
    - CONTEXT STATUS: ✅ Correct characterization of the EMNLP 2025 paper.

22. `\citet{kazdan2025collapse}` -- "map collapse conditions"
    - CONTEXT STATUS: ✅ Kazdan et al. map conditions under which collapse occurs or can be avoided.

23. `\citet{gu2024cmr}` -- "establish scaling laws for critical ratios"
    - CONTEXT STATUS: ✅ CMR scaling law for critical mixture ratios.

24. `\citet{gu2025datamixing}` -- "show data mixing induces phase transitions in knowledge acquisition"
    - CONTEXT STATUS: ✅ The paper does show phase transitions from data mixing. (Note: authors are wrong in bib, but the cited claim is correct for the paper.)

25. `\citep{du2025scales}` -- "expected calibration error (ECE)"
    - CONTEXT STATUS: ✅ Du et al. study calibration degradation under synthetic data training.

26. `\citep{gambetta2024surplexity}` -- "surplexity"
    - CONTEXT STATUS: ✅ Gambetta et al. introduce the surplexity metric.

27. `\citep{drayson2025detection}` -- "machine-generated text detection"
    - CONTEXT STATUS: ✅ Drayson et al. use text detection to prevent collapse.

28. `\citet{shi2025closer}` -- "independently validate entropy as a collapse diagnostic in diffusion models"
    - CONTEXT STATUS: ✅ Shi et al. identify entropy as key diagnostic in diffusion model collapse.

29. `\citep{buffa2026entropy}` -- "propose continuous entropy-based monitoring for LLM accuracy, though targeting task performance rather than distributional collapse"
    - CONTEXT STATUS: ✅ Correct scoping distinction. Buffa et al. target task accuracy monitoring, not distributional collapse.

30. `\citep{kirchenbauer2023watermark}` -- "proactive contamination prevention via watermarking"
    - CONTEXT STATUS: ✅ Kirchenbauer et al. propose watermarking for LLMs.

31. `\citet{boettiger2012limits}` -- "establish fundamental power limits for early-warning detection in short time series"
    - CONTEXT STATUS: ✅ Correct characterization.

32. `\citep{tank2021neural,runge2019detecting}` -- "neural extensions" of Granger causality
    - CONTEXT STATUS: ✅ Tank et al. propose neural Granger causality; Runge et al. propose PCMCI for causal discovery in time series.

33. `\citep{steegen2016increasing,silberzahn2018many,coretta2023multidimensional,kapoor2024reforms}` -- "multiverse analysis perspective"
    - CONTEXT STATUS: ✅ All four papers deal with analytic flexibility / multiverse analysis / many-analysts approaches.

**discussion.tex:**

34. `\citep{granger1969investigating,shojaie2022granger}` -- "Granger-precedence claim is scoped to temporal predictive improvement"
    - CONTEXT STATUS: ✅ Appropriate citations for Granger framework and its limitations.

35. `\citep{shojaie2022granger}` -- "permutation testing avoids asymptotic assumptions but cannot recover power lost to short samples"
    - CONTEXT STATUS: ✅ Shojaie and Fox discuss power limitations in short series contexts.

**experiments.tex:**

36. `\citep{merity2017pointer}` -- "WikiText-103"
    - CONTEXT STATUS: ✅ WikiText-103 is introduced in Merity et al.

37. `\citep{shumailov2024curse}` -- "replace paradigm"
    - CONTEXT STATUS: ✅ The replacement paradigm is from Shumailov et al.

38. `\citep{benjamini1995controlling}` -- "BH-FDR correction"
    - CONTEXT STATUS: ✅ The BH procedure is from Benjamini and Hochberg (1995).

39. `\citep{li2016diversity}` -- "distinct-1, distinct-2"
    - CONTEXT STATUS: ✅ Correct attribution.

**appendix.tex:**

40. `\citep{naeini2015obtaining}` -- "ECE with 15 bins...standard definition"
    - CONTEXT STATUS: ✅ Naeini et al. formalize ECE with binning.

41. `\citep{page1954continuous}` -- "CUSUM sequential testing"
    - CONTEXT STATUS: ✅ Page (1954) introduces the CUSUM procedure.

42. `\citep{schreiber2000measuring}` -- "Transfer entropy"
    - CONTEXT STATUS: ✅ Schreiber introduces transfer entropy.

43. `\citep{staniek2008symbolic}` -- "Symbolic TE...Bandt-Pompe ordinal patterns"
    - CONTEXT STATUS: ✅ Staniek and Lehnertz introduce symbolic transfer entropy.

44. `\citep{pillutla2021mauve}` -- "MAUVE"
    - CONTEXT STATUS: ✅ MAUVE metric is from Pillutla et al.

45. `\citep{shapley1953value}` -- "Shapley values"
    - CONTEXT STATUS: ✅ Classic attribution.

46. `\citep{du2026geometric}` -- not directly cited in the tex files I read. It appears in the bib but may be used only in the `intro_reframe.tex` or `method_reframe.tex` files.
    - CONTEXT STATUS: ⚠️ Could not verify in-context usage from the files provided. May be an unused bib entry.

47. `\citep{dces2026counter}` -- appears in `appendix.tex` Table `tab:method-comparison` as "DCES"
    - CONTEXT STATUS: ✅ Used in methodological comparison table. Appropriate citation.

---

### SUMMARY

**Total bib entries: 48**

| Status | Count | Details |
|--------|-------|---------|
| ✅ Verified correct | 37 | No issues |
| ⚠️ Minor issues | 9 | Incomplete authors, missing venue updates, inconsistent keys |
| ❌ Significant issues | 2 | Wrong authors, misleading bib key |

### ALL ISSUES FOUND (ordered by severity):

**Critical (❌):**

1. **gu2025datamixing**: Authors are completely wrong. Bib says "Gu, Xinran and Liang, Hayden and Pehlevan, Cengiz" but the actual authors are **Xinran Gu, Kaifeng Lyu, Jiazheng Li, and Jingzhao Zhang**. "Hayden Liang" and "Cengiz Pehlevan" are not authors of this paper. This is a fabricated/hallucinated author list. The bib also says NeurIPS Spotlight, but NeurIPS 2025 lists it as a Poster (though ICLR 2025 had a Spotlight presentation of possibly the same work -- this needs clarification).

2. **dey2024breaking**: Bib key `dey2024breaking` misattributes first authorship to Dey. The first author is Matthias Gerstgrasser. While the `author` field is correct, the bib key creates a misleading citation name that does not match the actual first author. This is a minor code-level issue but could cause confusion.

**Moderate (⚠️):**

3. **drayson2025detection**: Listed as arXiv preprint, but was **published at EMNLP 2025**. Should be updated to `@inproceedings` with proceedings title and pages (29645-29661).

4. **dohmatob2024tale**: Uses `and others` hiding 3 of 5 authors (missing Pu Yang, Francois Charton, Julia Kempe).

5. **gambetta2024surplexity**: Uses `and others` hiding 5 of 6 authors (missing Gizem Gezici, Fosca Giannotti, Dino Pedreschi, Alistair Knott, Luca Pappalardo).

6. **li2016diversity**: Uses `and others` hiding 4 of 5 authors (missing Michel Galley, Chris Brockett, Jianfeng Gao, Bill Dolan).

7. **truong2026phase**: Bib key says `truong2026phase` but `year={2025}` in the entry. The arXiv ID (2512.xxxxx) confirms December 2025 submission. Key-year mismatch. Also missing URL field.

8. **shumailov2024curse**: Missing volume/pages for Nature publication (vol. 631).

9. **dces2026counter**: Missing volume/number/pages (vol. 15, no. 4, article 869).

10. **du2025scales**: Author names use only initials. Acceptable but not best practice.

11. **kovac2025recursive**: Booktitle is slightly non-standard (missing "2025" in proceedings title).

12. **du2026geometric**: May be an unused bib entry -- not found cited in any of the main tex files provided.

**Context accuracy**: All 45+ in-text citation claims accurately represent the cited papers' findings. No misattributions of results were found.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24035afd-1eb6-4a87-b1d5-a1bd7f061629",
  "isSidechain": true,
  "agentId": "ac7763ed9e49a33d3",
  "requestId": "req_011CbR46WohcakWpfC491GrG",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "72afbd0b-f72d-4672-bffc-63f3251a96c6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "c40115ed-b6c5-49fe-b59f-6952ab09f6a3",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "wise-tinkering-sloth",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwZcYkwb3bH2XajZYim4kt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1480,
      "cache_read_input_tokens": 134871,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1480,
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
