# research related work audit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/workers/worker_research_related-work-audit_20260518T135805.log`
- **Structured JSON:** [`b698dc9db65f888a6600.json`](../../sessions/b6/b698dc9db65f888a6600.json)

## Before a recorded user message

70 recorded events

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
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
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
  "uuid": "28b239d2-78d1-4f71-8aec-8520ed6675a7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779123600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b10bb47d-4e53-494c-865e-4a907a293fab",
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current related work and bib files, then conduct web searches for recent papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "88ecc88f-c59b-47e9-b8ce-63e653f2990c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsbjRbAumw4GN3qKJxZ8Zk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13366,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13366
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

先读取当前 related work 和 bib 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "d3e24bab-c8a8-4a2b-904e-e13fbf72bcdf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsbjRbAumw4GN3qKJxZ8Zk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13366,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13366
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

<details open><summary>🔧 Tool call — Read · `toolu_01XjCKCYbgqwtw2oUdX3dxqQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "cea7677a-a0b8-43eb-b60d-1ccef2ae8b42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsbjRbAumw4GN3qKJxZ8Zk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13366,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13366
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

_source line 7 · 2026-05-18T13:58:20.555Z_

<details><summary>↩ Tool result · `toolu_01XjCKCYbgqwtw2oUdX3dxqQ`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Temporal Abstraction.}
5	The options framework \citep{sutton1999options} and model-free action-repetition methods \citep{sharma2017figar, biedenkapp2021temporl, lakshminarayanan2017dynamic} achieve temporal abstraction by training values on real transitions, insulating them from model-induced bias. In world-model RL, the Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} and transformer-based variants \citep{micheli2023iris, robine2023twm, hafner2025dreamerv4} train policies in imagination at fixed $\dt{=}1$. Several works introduce temporal abstraction via hierarchical representations \citep{gumbsch2024thick, mattes2024hieros}, goal-conditioned jumps \citep{li2025lsimagine}, or multi-scale state-space models \citep{shaj2023mts3}, but none conditions a flat dynamics model on $\dt$ for imagination-based policy training.
6	
7	\paragraph{TAWM and the MPC--Imagination Contrast.}
8	TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2} and achieves consistent gains. The critical distinction is architectural: TAWM re-plans from real states at every step, so model errors do not accumulate into the critic. We show that identical $\dt$-conditioning fails in DreamerV3's imagination loop, where errors compound through bootstrapping and transform manageable imprecision into pathological value overestimation.
9	
10	\paragraph{Value Overestimation.}
11	\citet{thrun1993issues} first identified maximization bias in Q-learning with function approximation. Double Q-learning \citep{vanhasselt2016double} decouples action selection from evaluation; TD3 \citep{fujimoto2018td3} extends this to actor-critic methods via clipped double-Q critics; SAC \citep{haarnoja2018sac} uses entropy regularization to implicitly reduce overestimation; REDQ \citep{chen2021redq} further mitigates overestimation through randomized Q-function ensembles. These model-free solutions target the max operator as the amplifier. In model-based settings, MBPO \citep{janner2019mbpo} bounds model use via short rollouts and MOPO \citep{yu2020mopo} penalizes rewards by model uncertainty. \citet{lu2018nondelusional} identify delusional bias from policy-class constraints. Our CIVO is mechanistically distinct: the amplifier is the world model's co-adaptation with a learned temporal embedding. This produces systematic reward-prediction bias at $\dt > 1$ that is model-induced rather than policy-class-induced (\S\ref{sec:civo_mechanism}). \citet{tallec2019making} provide theoretical grounding via Q-function degradation under temporal resolution mismatches. All of the above aim to \emph{prevent} overestimation architecturally or algorithmically. By contrast, our online detector monitors for signs of pathological value divergence \emph{during training} and complements prevention with early diagnosis. To our knowledge, no prior work proposes a runtime diagnostic that specifically targets value overestimation acceleration onset in world-model RL.
12	
13	\paragraph{Model Fidelity and Compounding Error.}
14	\citet{lambert2020objective} formalize objective mismatch (observation loss $\neq$ reward accuracy); \citet{asadi2019combating} and \citet{lambert2022investigating} characterize compounding error in multi-step rollouts. \citet{ma2024harmonydream} address this in DreamerV3 by harmonizing loss weights. Our gradient decomposition (\S\ref{sec:gradient_decomposition}) shows that the observation decoder channel, despite providing the smallest gradient share (16--22\%), carries the $\dt$-specific spatial information that drives the fidelity gap. This confirms objective mismatch as the driver. \citet{palenicek2025diminishing} and \citet{frauenknecht2025rollouts} demonstrate rollout-length diminishing returns and quality-dominance in MBRL; we identify the specific $\dt$-embedding mechanism by which rollout divergence corrupts values.
15	
16	\paragraph{Network Capacity and Diagnostic Methodology.}
17	The primacy bias \citep{nikishin2022primacy} and progressive capacity loss \citep{lyle2022capacity, nikishin2023plasticity} provide our framework for seed-dependent CIVO outcomes (\S\ref{sec:seed_divergence}). Our factorial diagnostic approach follows \citet{henderson2018deep}, \citet{engstrom2020implementation}, and \citet{andrychowicz2021whatmatters} in systematically isolating design-choice effects, extending this tradition to model-based temporal conditioning.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "37409de0-a268-41b6-846c-ef4f0cb1fbde",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Temporal Abstraction.}\nThe options framework \\citep{sutton1999options} and model-free action-repetition methods \\citep{sharma2017figar, biedenkapp2021temporl, lakshminarayanan2017dynamic} achieve temporal abstraction by training values on real transitions, insulating them from model-induced bias. In world-model RL, the Dreamer family \\citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} and transformer-based variants \\citep{micheli2023iris, robine2023twm, hafner2025dreamerv4} train policies in imagination at fixed $\\dt{=}1$. Several works introduce temporal abstraction via hierarchical representations \\citep{gumbsch2024thick, mattes2024hieros}, goal-conditioned jumps \\citep{li2025lsimagine}, or multi-scale state-space models \\citep{shaj2023mts3}, but none conditions a flat dynamics model on $\\dt$ for imagination-based policy training.\n\n\\paragraph{TAWM and the MPC--Imagination Contrast.}\nTAWM \\citep{nhu2025tawm} conditions a world model on $\\dt$ within TD-MPC2 \\citep{hansen2024tdmpc2} and achieves consistent gains. The critical distinction is architectural: TAWM re-plans from real states at every step, so model errors do not accumulate into the critic. We show that identical $\\dt$-conditioning fails in DreamerV3's imagination loop, where errors compound through bootstrapping and transform manageable imprecision into pathological value overestimation.\n\n\\paragraph{Value Overestimation.}\n\\citet{thrun1993issues} first identified maximization bias in Q-learning with function approximation. Double Q-learning \\citep{vanhasselt2016double} decouples action selection from evaluation; TD3 \\citep{fujimoto2018td3} extends this to actor-critic methods via clipped double-Q critics; SAC \\citep{haarnoja2018sac} uses entropy regularization to implicitly reduce overestimation; REDQ \\citep{chen2021redq} further mitigates overestimation through randomized Q-function ensembles. These model-free solutions target the max operator as the amplifier. In model-based settings, MBPO \\citep{janner2019mbpo} bounds model use via short rollouts and MOPO \\citep{yu2020mopo} penalizes rewards by model uncertainty. \\citet{lu2018nondelusional} identify delusional bias from policy-class constraints. Our CIVO is mechanistically distinct: the amplifier is the world model's co-adaptation with a learned temporal embedding. This produces systematic reward-prediction bias at $\\dt > 1$ that is model-induced rather than policy-class-induced (\\S\\ref{sec:civo_mechanism}). \\citet{tallec2019making} provide theoretical grounding via Q-function degradation under temporal resolution mismatches. All of the above aim to \\emph{prevent} overestimation architecturally or algorithmically. By contrast, our online detector monitors for signs of pathological value divergence \\emph{during training} and complements prevention with early diagnosis. To our knowledge, no prior work proposes a runtime diagnostic that specifically targets value overestimation acceleration onset in world-model RL.\n\n\\paragraph{Model Fidelity and Compounding Error.}\n\\citet{lambert2020objective} formalize objective mismatch (observation loss $\\neq$ reward accuracy); \\citet{asadi2019combating} and \\citet{lambert2022investigating} characterize compounding error in multi-step rollouts. \\citet{ma2024harmonydream} address this in DreamerV3 by harmonizing loss weights. Our gradient decomposition (\\S\\ref{sec:gradient_decomposition}) shows that the observation decoder channel, despite providing the smallest gradient share (16--22\\%), carries the $\\dt$-specific spatial information that drives the fidelity gap. This confirms objective mismatch as the driver. \\citet{palenicek2025diminishing} and \\citet{frauenknecht2025rollouts} demonstrate rollout-length diminishing returns and quality-dominance in MBRL; we identify the specific $\\dt$-embedding mechanism by which rollout divergence corrupts values.\n\n\\paragraph{Network Capacity and Diagnostic Methodology.}\nThe primacy bias \\citep{nikishin2022primacy} and progressive capacity loss \\citep{lyle2022capacity, nikishin2023plasticity} provide our framework for seed-dependent CIVO outcomes (\\S\\ref{sec:seed_divergence}). Our factorial diagnostic approach follows \\citet{henderson2018deep}, \\citet{engstrom2020implementation}, and \\citet{andrychowicz2021whatmatters} in systematically isolating design-choice effects, extending this tradition to model-based temporal conditioning.\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_012A1vTGSkcwVSWaLkyBuTSN`</summary>

```json
{
  "pattern": "docs/paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "4e792edf-41c7-4bb7-929d-017c89045803",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsbjRbAumw4GN3qKJxZ8Zk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13366,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13366
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

_source line 9 · 2026-05-18T13:58:20.604Z_

<details><summary>↩ Tool result · `toolu_012A1vTGSkcwVSWaLkyBuTSN`</summary>

```text
docs/paper/_corl_template/corl_2026_template_submission/example.bib
docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.bib
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "aba9d021-52e9-4915-af01-d2ea7c1a21f8",
  "tool_use_result": {
    "filenames": [
      "docs/paper/_corl_template/corl_2026_template_submission/example.bib",
      "docs/paper/_corl_template/__MACOSX/corl_2026_template_submission/._example.bib",
      "docs/paper/references.bib"
    ],
    "durationMs": 16,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01WfQmJfokDEMJhyYdPYxQLM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "8eb26165-d4db-429c-b3e1-e30b28a2d953",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FNUp6tTBcHv8UyZQ7VU56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1601,
      "cache_read_input_tokens": 24813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1601
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

_source line 11 · 2026-05-18T13:58:23.267Z_

<details><summary>↩ Tool result · `toolu_01WfQmJfokDEMJhyYdPYxQLM`</summary>

```text
1	% Auto-generated from literature_map.yaml
2	% 76 entries
3	
4	@article{sutton1999options,
5	  title = {Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning},
6	  author = {Sutton, R.S and Precup, D and Singh, S},
7	  year = {1999},
8	  journal = {Artificial Intelligence 112},
9	}
10	
11	@inproceedings{hafner2020dreamerv1,
12	  title = {Dream to Control: Learning Behaviors by Latent Imagination},
13	  author = {Hafner, D and Lillicrap, T and Ba, J and Norouzi, M},
14	  year = {2020},
15	  booktitle = {International Conference on Learning Representations},
16	}
17	
18	@article{hafner2023dreamerv3,
19	  title = {Mastering Diverse Domains through World Models},
20	  author = {Hafner, Danijar and Pasukonis, Jurgis and Ba, Jimmy and Lillicrap, Timothy},
21	  year = {2025},
22	  journal = {Nature},
23	  eprint = {2301.04104},
24	  archivePrefix = {arXiv},
25	}
26	
27	@inproceedings{sharma2017figar,
28	  title = {Fine Grained Action Repetition for Deep Reinforcement Learning},
29	  author = {Sharma, S and Lakshminarayanan, A.S and Ravindran, B},
30	  year = {2017},
31	  booktitle = {International Conference on Learning Representations},
32	}
33	
34	@inproceedings{janner2019mbpo,
35	  title = {When to Trust Your Model: Model-Based Policy Optimization},
36	  author = {Janner, M and Fu, J and Zhang, M and Levine, S},
37	  year = {2019},
38	  booktitle = {Advances in Neural Information Processing Systems},
39	}
40	
41	@inproceedings{ke2019learning,
42	  title = {Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future},
43	  author = {Ke, N.R and Singh, A and Touati, A and Goyal, A and Bengio, Y and Parikh, D and Batra, D},
44	  year = {2019},
45	  booktitle = {International Conference on Learning Representations},
46	}
47	
48	@article{asadi2019combating,
49	  title = {Combating the Compounding-Error Problem with a Multi-step Model},
50	  author = {Asadi, K and Misra, D and Kim, S and Littman, M.L},
51	  year = {2019},
52	  journal = {arXiv preprint arXiv:1905.13320},
53	  eprint = {1905.13320},
54	  archivePrefix = {arXiv},
55	}
56	
57	@inproceedings{venkatraman2015improving,
58	  title = {Improving Multi-Step Prediction of Learned Time Series Models},
59	  author = {Venkatraman, A and Hebert, M and Bagnell, J.A},
60	  year = {2015},
61	  booktitle = {AAAI Conference on Artificial Intelligence},
62	}
63	
64	@article{lambert2022investigating,
65	  title = {Investigating Compounding Prediction Errors in Learned Dynamics Models},
66	  author = {Lambert, N and Pister, K.S.J and Calandra, R},
67	  year = {2022},
68	  journal = {arXiv preprint arXiv:2203.09637},
69	  eprint = {2203.09637},
70	  archivePrefix = {arXiv},
71	}
72	
73	@inproceedings{chua2018pets,
74	  title = {Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models},
75	  author = {Chua, K and Calandra, R and McAllister, R and Levine, S},
76	  year = {2018},
77	  booktitle = {Advances in Neural Information Processing Systems},
78	}
79	
80	@inproceedings{nagabandi2018neural,
81	  title = {Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning},
82	  author = {Nagabandi, A and Kahn, G and Fearing, R.S and Levine, S},
83	  year = {2018},
84	  booktitle = {IEEE International Conference on Robotics and Automation},
85	}
86	
87	@inproceedings{hansen2024tdmpc2,
88	  title = {TD-MPC2: Scalable, Robust World Models for Continuous Control},
89	  author = {Hansen, N and Su, H and Wang, X},
90	  year = {2024},
91	  booktitle = {International Conference on Learning Representations},
92	  eprint = {2310.16828},
93	  archivePrefix = {arXiv},
94	}
95	
96	@inproceedings{yu2020mopo,
97	  title = {MOPO: Model-based Offline Policy Optimization},
98	  author = {Yu, T and Thomas, G and Yu, L and Ermon, S and Zou, J and Levine, S and Finn, C and Ma, T},
99	  year = {2020},
100	  booktitle = {Advances in Neural Information Processing Systems},
101	  eprint = {2005.13239},
102	  archivePrefix = {arXiv},
103	}
104	
105	@inproceedings{thrun1993issues,
106	  title = {Issues in Using Function Approximation for Reinforcement Learning},
107	  author = {Thrun, S and Schwartz, A},
108	  year = {1993},
109	  booktitle = {Connectionist Models Summer School},
110	}
111	
112	@inproceedings{vanhasselt2016double,
113	  title = {Deep Reinforcement Learning with Double Q-Learning},
114	  author = {van Hasselt, Hado and Guez, Arthur and Silver, David},
115	  year = {2016},
116	  booktitle = {AAAI Conference on Artificial Intelligence},
117	}
118	
119	@inproceedings{fujimoto2018td3,
120	  title = {Addressing Function Approximation Error in Actor-Critic Methods},
121	  author = {Fujimoto, Scott and {van Hoof}, Herke and Meger, David},
122	  year = {2018},
123	  booktitle = {International Conference on Machine Learning},
124	}
125	
126	@inproceedings{haarnoja2018sac,
127	  title = {Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor},
128	  author = {Haarnoja, T and Zhou, A and Abbeel, P and Levine, S},
129	  year = {2018},
130	  booktitle = {International Conference on Machine Learning},
131	}
132	
133	@inproceedings{lee2021sunrise,
134	  title = {SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning},
135	  author = {Lee, K and Laskin, M and Srinivas, A and Abbeel, P},
136	  year = {2021},
137	  booktitle = {International Conference on Machine Learning},
138	}
139	
140	@inproceedings{lu2018nondelusional,
141	  title = {Non-delusional Q-learning and Value-Iteration},
142	  author = {Lu, T and Schuurmans, D and Boutilier, C},
143	  year = {2018},
144	  booktitle = {Advances in Neural Information Processing Systems},
145	}
146	
147	@inproceedings{hafner2022director,
148	  title = {Deep Hierarchical Planning from Pixels},
149	  author = {Hafner, D and Lee, K.-H and Fischer, I and Abbeel, P},
150	  year = {2022},
151	  booktitle = {Advances in Neural Information Processing Systems},
152	}
153	
154	@inproceedings{nachum2018hiro,
155	  title = {Data-Efficient Hierarchical Reinforcement Learning},
156	  author = {Nachum, O and Gu, S and Lee, H and Levine, S},
157	  year = {2018},
158	  booktitle = {Advances in Neural Information Processing Systems},
159	}
160	
161	@inproceedings{braylan2015frame,
162	  title = {Frame Skip Is a Powerful Parameter for Learning to Play Atari},
163	  author = {Braylan, A and Hollenbeck, M and Meyerson, E and Miikkulainen, R},
164	  year = {2015},
165	  booktitle = {AAAI Conference on Artificial Intelligence},
166	}
167	
168	@inproceedings{lakshminarayanan2017dynamic,
169	  title = {Dynamic Action Repetition for Deep Reinforcement Learning},
170	  author = {Lakshminarayanan, A.S and Sharma, S and Ravindran, B},
171	  year = {2017},
172	  booktitle = {AAAI Conference on Artificial Intelligence},
173	}
174	
175	@inproceedings{biedenkapp2021temporl,
176	  title = {TempoRL: Learning When to Act},
177	  author = {Biedenkapp, A and Rajan, R and Hutter, F and Lindauer, M},
178	  year = {2021},
179	  booktitle = {International Conference on Machine Learning},
180	}
181	
182	@inproceedings{hafner2021dreamerv2,
183	  title = {Mastering Atari with Discrete World Models},
184	  author = {Hafner, D and Lillicrap, T and Norouzi, M and Ba, J},
185	  year = {2021},
186	  booktitle = {International Conference on Learning Representations},
187	}
188	
189	@inproceedings{micheli2023iris,
190	  title = {Transformers are Sample-Efficient World Models},
191	  author = {Micheli, V and Alonso, E and Fleuret, F},
192	  year = {2023},
193	  booktitle = {International Conference on Learning Representations},
194	}
195	
196	@inproceedings{robine2023twm,
197	  title = {Transformer-based World Models Are Happy With 100k Interactions},
198	  author = {Robine, J and Hoeftmann, M and Uelwer, T and Harmeling, S},
199	  year = {2023},
200	  booktitle = {International Conference on Learning Representations},
201	}
202	
203	@article{chen2022transdreamer,
204	  title = {TransDreamer: Reinforcement Learning with Transformer World Models},
205	  author = {Chen, C and Wu, Y.-F and Yoon, J and Ahn, S},
206	  year = {2022},
207	  journal = {arXiv preprint arXiv:2202.09481},
208	  eprint = {2202.09481},
209	  archivePrefix = {arXiv},
210	}
211	
212	@inproceedings{gumbsch2024thick,
213	  title = {Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics},
214	  author = {Gumbsch, C and Sajid, N and Martius, G and Butz, M.V},
215	  year = {2024},
216	  booktitle = {International Conference on Learning Representations},
217	}
218	
219	@inproceedings{mattes2024hieros,
220	  title = {Hieros: Hierarchical Imagination on Structured State Space Sequence World Models},
221	  author = {Mattes, P and Schlosser, R and Herbrich, R},
222	  year = {2024},
223	  booktitle = {International Conference on Machine Learning},
224	}
225	
226	@inproceedings{henderson2018deep,
227	  title = {Deep Reinforcement Learning that Matters},
228	  author = {Henderson, P and Islam, R and Bachman, P and Pineau, J and Precup, D and Meger, D},
229	  year = {2018},
230	  booktitle = {AAAI Conference on Artificial Intelligence},
231	}
232	
233	@inproceedings{nikishin2022primacy,
234	  title = {The Primacy Bias in Deep Reinforcement Learning},
235	  author = {Nikishin, E and Schwarzer, M and D'Oro, P and Bacon, P.-L and Courville, A},
236	  year = {2022},
237	  booktitle = {International Conference on Machine Learning},
238	}
239	
240	@article{qiao2023mind,
241	  title = {Mind the Model, Not the Agent: The Primacy Bias in Model-based RL},
242	  author = {Qiao, Z and Lyu, J and Li, X},
243	  year = {2023},
244	  journal = {arXiv preprint arXiv:2310.15017},
245	  eprint = {2310.15017},
246	  archivePrefix = {arXiv},
247	}
248	
249	@article{hussing2024dissecting,
250	  title = {Dissecting Deep RL with High Update Ratios: Combatting Value Divergence},
251	  author = {Hussing, M and Voelcker, C.A and Gilitschenski, I and Farahmand, A.-M and Eaton, E},
252	  year = {2024},
253	  journal = {Reinforcement Learning Journal},
254	}
255	
256	@article{barkley2024stealing,
257	  title = {Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning},
258	  author = {Barkley, B and Fridovich-Keil, D},
259	  year = {2024},
260	  journal = {arXiv preprint arXiv:2412.14312},
261	  eprint = {2412.14312},
262	  archivePrefix = {arXiv},
263	}
264	
265	@inproceedings{bjorck2022variance,
266	  title = {Is High Variance Unavoidable in RL? A Case Study in Continuous Control},
267	  author = {Bjorck, J and Gomes, C.P and Weinberger, K.Q},
268	  year = {2022},
269	  booktitle = {International Conference on Learning Representations},
270	}
271	
272	@inproceedings{lee2024dreamsmooth,
273	  title = {DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing},
274	  author = {Lee, V and Abbeel, P and Lee, Y},
275	  year = {2024},
276	  booktitle = {International Conference on Learning Representations},
277	}
278	
279	@inproceedings{ma2024harmonydream,
280	  title = {HarmonyDream: Task Harmonization Inside World Models},
281	  author = {Ma, H and Wu, J and Feng, N and Xiao, C and Li, D and Hao, J and Wang, J and Long, M},
282	  year = {2024},
283	  booktitle = {International Conference on Machine Learning},
284	}
285	
286	@inproceedings{lambert2020objective,
287	  title = {Objective Mismatch in Model-based Reinforcement Learning},
288	  author = {Lambert, N and Amos, B and Yadan, O and Calandra, R},
289	  year = {2020},
290	  booktitle = {L4DC},
291	}
292	
293	@inproceedings{jaderberg2017unreal,
294	  title = {Reinforcement Learning with Unsupervised Auxiliary Tasks},
295	  author = {Jaderberg, M and Mnih, V and Czarnecki, W.M and Schaul, T and Leibo, J.Z and Silver, D and Kavukcuoglu, K},
296	  year = {2017},
297	  booktitle = {International Conference on Learning Representations},
298	}
299	
300	@inproceedings{lyle2021auxiliary,
301	  title = {On The Effect of Auxiliary Tasks on Representation Dynamics},
302	  author = {Lyle, C and Rowland, M and Ostrovski, G and Dabney, W},
303	  year = {2021},
304	  booktitle = {International Conference on Artificial Intelligence and Statistics},
305	}
306	
307	@article{bredis2026nedreamer,
308	  title = {Next Embedding Prediction Makes World Models Stronger},
309	  author = {Bredis, G and Balagansky, N and Gavrilov, D and Rakhimov, R},
310	  year = {2026},
311	  journal = {arXiv preprint arXiv:2603.02765},
312	  eprint = {2603.02765},
313	  archivePrefix = {arXiv},
314	}
315	
316	@inproceedings{zhang2025dymodreamer,
317	  title = {DyMoDreamer: World Modeling with Dynamic Modulation},
318	  author = {Zhang, B and Wang, R and Xiao, W and Zhang, W and Sun, J and Huang, G and Chen, J and Wang, G},
319	  year = {2025},
320	  booktitle = {Advances in Neural Information Processing Systems},
321	}
322	
323	@inproceedings{liu2025vanta,
324	  title = {Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning},
325	  author = {Liu, T.-S and Liu, X.-H and Chen, R and Jin, L and Wang, P and Zhang, Z and Yu, Y},
326	  year = {2025},
327	  booktitle = {International Conference on Learning Representations},
328	}
329	
330	@inproceedings{agarwal2021precipice,
331	  title = {Deep Reinforcement Learning at the Edge of the Statistical Precipice},
332	  author = {Agarwal, R and Schwarzer, M and Castro, P.S and Courville, A.C and Bellemare, M},
333	  year = {2021},
334	  booktitle = {Advances in Neural Information Processing Systems},
335	}
336	
337	@article{tassa2018dmcontrol,
338	  title = {DeepMind Control Suite},
339	  author = {Tassa, Yuval and Doron, Yotam and Muldal, Alistair and Erez, Tom and Li, Yazhe and de Las Casas, Diego and Budden, David and Abdolmaleki, Abbas and Merel, Josh and Lefrancq, Andrew and Lillicrap, Timothy and Riedmiller, Martin},
340	  year = {2018},
341	  journal = {arXiv preprint arXiv:1801.00690},
342	  eprint = {1801.00690},
343	  archivePrefix = {arXiv},
344	}
345	
346	@inproceedings{tallec2019making,
347	  title = {Making Deep Q-learning methods Robust to Time Discretization},
348	  author = {Tallec, C and Blier, L and Ollivier, Y},
349	  year = {2019},
350	  booktitle = {International Conference on Machine Learning},
351	  eprint = {1901.09732},
352	  archivePrefix = {arXiv},
353	}
354	
355	@inproceedings{park2021sar,
356	  title = {Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods},
357	  author = {Park, S and Kim, J and Kim, G},
358	  year = {2021},
359	  booktitle = {Advances in Neural Information Processing Systems},
360	  eprint = {2111.03941},
361	  archivePrefix = {arXiv},
362	}
363	
364	@article{wang2024seac,
365	  title = {Reinforcement Learning with Elastic Time Steps},
366	  author = {Wang, D and Beltrame, G},
367	  year = {2024},
368	  journal = {arXiv preprint arXiv:2402.14961},
369	  eprint = {2402.14961},
370	  archivePrefix = {arXiv},
371	}
372	
373	@inproceedings{su2020conqur,
374	  title = {ConQUR: Mitigating Delusional Bias in Deep Q-learning},
375	  author = {Su, D and Ooi, J and Lu, T and Schuurmans, D and Boutilier, C},
376	  year = {2020},
377	  booktitle = {International Conference on Machine Learning},
378	  eprint = {2002.12399},
379	  archivePrefix = {arXiv},
380	}
381	
382	@inproceedings{engstrom2020implementation,
383	  title = {Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO},
384	  author = {Engstrom, L and Ilyas, A and Santurkar, S and Tsipras, D and Janoos, F and Rudolph, L and Madry, A},
385	  year = {2020},
386	  booktitle = {International Conference on Learning Representations},
387	  eprint = {2005.12729},
388	  archivePrefix = {arXiv},
389	}
390	
391	@inproceedings{andrychowicz2021whatmatters,
392	  title = {What Matters for On-Policy Deep Actor-Critic Methods? A Large-Scale Study},
393	  author = {Andrychowicz, M and Raichuk, A and Stańczyk, P and Orsini, M and Girgin, S and Marinier, R and Hussenot, L and Geist, M and Pietquin, O and Michalski, M and Gelly, S and Bachem, O},
394	  year = {2021},
395	  booktitle = {International Conference on Learning Representations},
396	  eprint = {2006.05990},
397	  archivePrefix = {arXiv},
398	}
399	
400	@inproceedings{frauenknecht2025rollouts,
401	  title = {On Rollouts in Model-Based Reinforcement Learning},
402	  author = {Frauenknecht, B and Subhasish, D and Solowjow, F and Trimpe, S},
403	  year = {2025},
404	  booktitle = {International Conference on Learning Representations},
405	  eprint = {2501.16918},
406	  archivePrefix = {arXiv},
407	}
408	
409	@inproceedings{voelcker2025madtd,
410	  title = {MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL},
411	  author = {Voelcker, C and Hussing, M and Eaton, E and Farahmand, A.-M and Gilitschenski, I},
412	  year = {2025},
413	  booktitle = {International Conference on Learning Representations},
414	  eprint = {2410.08896},
415	  archivePrefix = {arXiv},
416	}
417	
418	@inproceedings{nie2025sdar,
419	  title = {Select before Act: Spatially Decoupled Action Repetition for Continuous Control},
420	  author = {Nie, B and et, al},
421	  year = {2025},
422	  booktitle = {International Conference on Learning Representations},
423	  eprint = {2502.06919},
424	  archivePrefix = {arXiv},
425	}
426	
427	@article{hafner2025dreamerv4,
428	  title = {Training Agents Inside of Scalable World Models},
429	  author = {Hafner, D and Yan, W and Lillicrap, T},
430	  year = {2025},
431	  journal = {arXiv preprint arXiv:2509.24527},
432	  eprint = {2509.24527},
433	  archivePrefix = {arXiv},
434	}
435	
436	@inproceedings{zhang2026instability,
437	  title = {Training instability in deep learning follows low-dimensional dynamical principles},
438	  author = {Zhang, L and et, al},
439	  year = {2026},
440	  booktitle = {International Conference on Learning Representations},
441	  eprint = {2601.13160},
442	  archivePrefix = {arXiv},
443	}
444	
445	@inproceedings{sokar2023dormant,
446	  title = {The Dormant Neuron Phenomenon in Deep Reinforcement Learning},
447	  author = {Sokar, G and Agarwal, R and Castro, P.S and Evci, U},
448	  year = {2023},
449	  booktitle = {International Conference on Machine Learning},
450	}
451	
452	@inproceedings{lyle2022capacity,
453	  title = {Understanding and Preventing Capacity Loss in Reinforcement Learning},
454	  author = {Lyle, C and Rowland, M and Dabney, W},
455	  year = {2022},
456	  booktitle = {International Conference on Learning Representations},
457	  eprint = {2204.09560},
458	  archivePrefix = {arXiv},
459	}
460	
461	@inproceedings{kumar2022dr3,
462	  title = {DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization},
463	  author = {Kumar, A and Agarwal, R and Ma, T and Courville, A and Tucker, G and Levine, S},
464	  year = {2022},
465	  booktitle = {International Conference on Learning Representations},
466	}
467	
468	@article{colas2018seeds,
469	  title = {How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments},
470	  author = {Colas, C and Sigaud, O and Oudeyer, P.-Y},
471	  year = {2018},
472	  journal = {arXiv preprint arXiv:1806.08295},
473	  eprint = {1806.08295},
474	  archivePrefix = {arXiv},
475	}
476	
477	@inproceedings{nikishin2023plasticity,
478	  title = {Deep Reinforcement Learning with Plasticity Injection},
479	  author = {Nikishin, E and Oh, J and Ostrovski, G and Lyle, C and Pascanu, R and Dabney, W and Barreto, A},
480	  year = {2023},
481	  booktitle = {Advances in Neural Information Processing Systems},
482	}
483	
484	@inproceedings{schwarzer2023bbf,
485	  title = {Bigger, Better, Faster: Human-level Atari with Human-level Efficiency},
486	  author = {Schwarzer, M and Obando-Ceron, J.S and Courville, A and Bellemare, M and Agarwal, R and Castro, P.S},
487	  year = {2023},
488	  booktitle = {International Conference on Machine Learning},
489	}
490	
491	@inproceedings{farebrother2024stopregressing,
492	  title = {Stop Regressing: Training Value Functions via Classification for Scalable Deep RL},
493	  author = {Farebrother, J and Orbay, J and Vuong, Q and Taiga, A.A and Chebotar, Y and Xiao, T and Irpan, A and Levine, S and Castro, P.S and Faust, A and Kumar, A and Agarwal, R},
494	  year = {2024},
495	  booktitle = {International Conference on Machine Learning},
496	}
497	
498	@inproceedings{lyle2024normalization,
499	  title = {Normalization and Effective Learning Rates in Reinforcement Learning},
500	  author = {Lyle, C and Zheng, Z and Giunchiglia, E and Sherstan, C and Hashemizadeh, M and Schuurmans, D and Dabney, W},
501	  year = {2024},
502	  booktitle = {Advances in Neural Information Processing Systems},
503	}
504	
505	@inproceedings{nhu2025tawm,
506	  title = {Time-Aware World Model for Adaptive Prediction and Control},
507	  author = {Nhu, A.N and Son, S and Lin, M.C},
508	  year = {2025},
509	  booktitle = {International Conference on Machine Learning},
510	  eprint = {2506.08441},
511	  archivePrefix = {arXiv},
512	}
513	
514	@inproceedings{li2025lsimagine,
515	  title = {Open-World Reinforcement Learning over Long Short-Term Imagination},
516	  author = {Li, J and Wang, Q and Wang, Y and Jin, X and Li, Y and Zeng, W and Yang, X},
517	  year = {2025},
518	  booktitle = {International Conference on Learning Representations},
519	  eprint = {2410.03618},
520	  archivePrefix = {arXiv},
521	}
522	
523	@article{zhang2026hwm,
524	  title = {Hierarchical Planning with Latent World Models},
525	  author = {Zhang, W and Terver, B and Zholus, A and Chitnis, S and Sutaria, H and Assran, M and Balestriero, R and Bar, A and Bardes, A and LeCun, Y and Ballas, N},
526	  year = {2026},
527	  journal = {arXiv preprint arXiv:2604.03208},
528	  eprint = {2604.03208},
529	  archivePrefix = {arXiv},
530	}
531	
532	@article{kobayashi2025metacontroller,
533	  title = {Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning},
534	  author = {Kobayashi, S and et, al},
535	  year = {2025},
536	  journal = {arXiv preprint arXiv:2512.20605},
537	  eprint = {2512.20605},
538	  archivePrefix = {arXiv},
539	}
540	
541	@inproceedings{shaj2023mts3,
542	  title = {Multi Time Scale World Models},
543	  author = {Shaj, V and Gholam, Zadeh S and Demir, O and Douat, L.R and Neumann, G},
544	  year = {2023},
545	  booktitle = {Advances in Neural Information Processing Systems},
546	  eprint = {2310.18534},
547	  archivePrefix = {arXiv},
548	}
549	
550	@article{splates2025,
551	  title = {Stable Planning with Temporally Extended Skills},
552	  author = {SPlaTES, authors},
553	  year = {2025},
554	  journal = {Reinforcement Learning Journal},
555	}
556	
557	@article{beckerehmck2023multitimestep,
558	  title = {Multi-timestep models for Model-based Reinforcement Learning},
559	  author = {Becker-Ehmck, Philip and Peters, Jan and {van der Smagt}, Patrick},
560	  year = {2023},
561	  journal = {arXiv preprint arXiv:2310.05672},
562	  eprint = {2310.05672},
563	  archivePrefix = {arXiv},
564	}
565	
566	@article{liu2022dmve,
567	  title = {Dynamic-Horizon Model-Based Value Estimation With Latent Imagination},
568	  author = {Liu, Y and et, al},
569	  year = {2022},
570	  journal = {IEEE TNNLS},
571	  eprint = {2009.09593},
572	  archivePrefix = {arXiv},
573	}
574	
575	@article{palenicek2025diminishing,
576	  title = {Diminishing Return of Value Expansion Methods},
577	  author = {Palenicek, D and Lutter, M and Carvalho, J and Dennert, D and Ahmad, F and Peters, J},
578	  year = {2025},
579	  journal = {Reinforcement Learning Journal},
580	  eprint = {2412.20537},
581	  archivePrefix = {arXiv},
582	}
583	
584	@article{kim2025deas,
585	  title = {DEAS: DEtached value learning with Action Sequence for Scalable Offline RL},
586	  author = {Kim, C and Seo, Y and et, al},
587	  year = {2025},
588	  journal = {arXiv preprint arXiv:2510.07730},
589	  eprint = {2510.07730},
590	  archivePrefix = {arXiv},
591	}
592	
593	@inproceedings{luo2025vpl,
594	  title = {A Case for Validation Buffer in Pessimistic Actor-Critic},
595	  author = {Nauman, M and Ostaszewski, M and Cygan, M},
596	  year = {2025},
597	  booktitle = {IJCAI 2025},
598	  eprint = {2403.01014},
599	  archivePrefix = {arXiv},
600	}
601	
602	@inproceedings{chen2021redq,
603	  title = {Randomized Ensembled Double Q-Learning: Learning Fast Without a Model},
604	  author = {Chen, Xinyue and Wang, Che and Zhou, Zijian and Ross, Keith},
605	  year = {2021},
606	  booktitle = {International Conference on Learning Representations},
607	  eprint = {2101.05982},
608	  archivePrefix = {arXiv},
609	}
610	
611	@article{lenz2025macura,
612	  title = {Trust the Model Where It Trusts Itself -- Model-Based Actor-Critic with Uncertainty-Aware Rollout Adaption},
613	  author = {Lenz, S and et, al},
614	  year = {2025},
615	  journal = {arXiv preprint arXiv:2405.19014},
616	  eprint = {2405.19014},
617	  archivePrefix = {arXiv},
618	}
619	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "3b376fbc-a503-4f0b-b1c7-aca826839239",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml\n% 76 entries\n\n@article{sutton1999options,\n  title = {Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning},\n  author = {Sutton, R.S and Precup, D and Singh, S},\n  year = {1999},\n  journal = {Artificial Intelligence 112},\n}\n\n@inproceedings{hafner2020dreamerv1,\n  title = {Dream to Control: Learning Behaviors by Latent Imagination},\n  author = {Hafner, D and Lillicrap, T and Ba, J and Norouzi, M},\n  year = {2020},\n  booktitle = {International Conference on Learning Representations},\n}\n\n@article{hafner2023dreamerv3,\n  title = {Mastering Diverse Domains through World Models},\n  author = {Hafner, Danijar and Pasukonis, Jurgis and Ba, Jimmy and Lillicrap, Timothy},\n  year = {2025},\n  journal = {Nature},\n  eprint = {2301.04104},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{sharma2017figar,\n  title = {Fine Grained Action Repetition for Deep Reinforcement Learning},\n  author = {Sharma, S and Lakshminarayanan, A.S and Ravindran, B},\n  year = {2017},\n  booktitle = {International Conference on Learning Representations},\n}\n\n@inproceedings{janner2019mbpo,\n  title = {When to Trust Your Model: Model-Based Policy Optimization},\n  author = {Janner, M and Fu, J and Zhang, M and Levine, S},\n  year = {2019},\n  booktitle = {Advances in Neural Information Processing Systems},\n}\n\n@inproceedings{ke2019learning,\n  title = {Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future},\n  author = {Ke, N.R and Singh, A and Touati, A and Goyal, A and Bengio, Y and Parikh, D and Batra, D},\n  year = {2019},\n  booktitle = {International Conference on Learning Representations},\n}\n\n@article{asadi2019combating,\n  title = {Combating the Compounding-Error Problem with a Multi-step Model},\n  author = {Asadi, K and Misra, D and Kim, S and Littman, M.L},\n  year = {2019},\n  journal = {arXiv preprint arXiv:1905.13320},\n  eprint = {1905.13320},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{venkatraman2015improving,\n  title = {Improving Multi-Step Prediction of Learned Time Series Models},\n  author = {Venkatraman, A and Hebert, M and Bagnell, J.A},\n  year = {2015},\n  booktitle = {AAAI Conference on Artificial Intelligence},\n}\n\n@article{lambert2022investigating,\n  title = {Investigating Compounding Prediction Errors in Learned Dynamics Models},\n  author = {Lambert, N and Pister, K.S.J and Calandra, R},\n  year = {2022},\n  journal = {arXiv preprint arXiv:2203.09637},\n  eprint = {2203.09637},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{chua2018pets,\n  title = {Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models},\n  author = {Chua, K and Calandra, R and McAllister, R and Levine, S},\n  year = {2018},\n  booktitle = {Advances in Neural Information Processing Systems},\n}\n\n@inproceedings{nagabandi2018neural,\n  title = {Neural Network Dynamics for Model-Based Deep Reinforcement Learning with Model-Free Fine-Tuning},\n  author = {Nagabandi, A and Kahn, G and Fearing, R.S and Levine, S},\n  year = {2018},\n  booktitle = {IEEE International Conference on Robotics and Automation},\n}\n\n@inproceedings{hansen2024tdmpc2,\n  title = {TD-MPC2: Scalable, Robust World Models for Continuous Control},\n  author = {Hansen, N and Su, H and Wang, X},\n  year = {2024},\n  booktitle = {International Conference on Learning Representations},\n  eprint = {2310.16828},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{yu2020mopo,\n  title = {MOPO: Model-based Offline Policy Optimization},\n  author = {Yu, T and Thomas, G and Yu, L and Ermon, S and Zou, J and Levine, S and Finn, C and Ma, T},\n  year = {2020},\n  booktitle = {Advances in Neural Information Processing Systems},\n  eprint = {2005.13239},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{thrun1993issues,\n  title = {Issues in Using Function Approximation for Reinforcement Learning},\n  author = {Thrun, S and Schwartz, A},\n  year = {1993},\n  booktitle = {Connectionist Models Summer School},\n}\n\n@inproceedings{vanhasselt2016double,\n  title = {Deep Reinforcement Learning with Double Q-Learning},\n  author = {van Hasselt, Hado and Guez, Arthur and Silver, David},\n  year = {2016},\n  booktitle = {AAAI Conference on Artificial Intelligence},\n}\n\n@inproceedings{fujimoto2018td3,\n  title = {Addressing Function Approximation Error in Actor-Critic Methods},\n  author = {Fujimoto, Scott and {van Hoof}, Herke and Meger, David},\n  year = {2018},\n  booktitle = {International Conference on Machine Learning},\n}\n\n@inproceedings{haarnoja2018sac,\n  title = {Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor},\n  author = {Haarnoja, T and Zhou, A and Abbeel, P and Levine, S},\n  year = {2018},\n  booktitle = {International Conference on Machine Learning},\n}\n\n@inproceedings{lee2021sunrise,\n  title = {SUNRISE: A Simple Unified Framework for Ensemble Learning in Deep Reinforcement Learning},\n  author = {Lee, K and Laskin, M and Srinivas, A and Abbeel, P},\n  year = {2021},\n  booktitle = {International Conference on Machine Learning},\n}\n\n@inproceedings{lu2018nondelusional,\n  title = {Non-delusional Q-learning and Value-Iteration},\n  author = {Lu, T and Schuurmans, D and Boutilier, C},\n  year = {2018},\n  booktitle = {Advances in Neural Information Processing Systems},\n}\n\n@inproceedings{hafner2022director,\n  title = {Deep Hierarchical Planning from Pixels},\n  author = {Hafner, D and Lee, K.-H and Fischer, I and Abbeel, P},\n  year = {2022},\n  booktitle = {Advances in Neural Information Processing Systems},\n}\n\n@inproceedings{nachum2018hiro,\n  title = {Data-Efficient Hierarchical Reinforcement Learning},\n  author = {Nachum, O and Gu, S and Lee, H and Levine, S},\n  year = {2018},\n  booktitle = {Advances in Neural Information Processing Systems},\n}\n\n@inproceedings{braylan2015frame,\n  title = {Frame Skip Is a Powerful Parameter for Learning to Play Atari},\n  author = {Braylan, A and Hollenbeck, M and Meyerson, E and Miikkulainen, R},\n  year = {2015},\n  booktitle = {AAAI Conference on Artificial Intelligence},\n}\n\n@inproceedings{lakshminarayanan2017dynamic,\n  title = {Dynamic Action Repetition for Deep Reinforcement Learning},\n  author = {Lakshminarayanan, A.S and Sharma, S and Ravindran, B},\n  year = {2017},\n  booktitle = {AAAI Conference on Artificial Intelligence},\n}\n\n@inproceedings{biedenkapp2021temporl,\n  title = {TempoRL: Learning When to Act},\n  author = {Biedenkapp, A and Rajan, R and Hutter, F and Lindauer, M},\n  year = {2021},\n  booktitle = {International Conference on Machine Learning},\n}\n\n@inproceedings{hafner2021dreamerv2,\n  title = {Mastering Atari with Discrete World Models},\n  author = {Hafner, D and Lillicrap, T and Norouzi, M and Ba, J},\n  year = {2021},\n  booktitle = {International Conference on Learning Representations},\n}\n\n@inproceedings{micheli2023iris,\n  title = {Transformers are Sample-Efficient World Models},\n  author = {Micheli, V and Alonso, E and Fleuret, F},\n  year = {2023},\n  booktitle = {International Conference on Learning Representations},\n}\n\n@inproceedings{robine2023twm,\n  title = {Transformer-based World Models Are Happy With 100k Interactions},\n  author = {Robine, J and Hoeftmann, M and Uelwer, T and Harmeling, S},\n  year = {2023},\n  booktitle = {International Conference on Learning Representations},\n}\n\n@article{chen2022transdreamer,\n  title = {TransDreamer: Reinforcement Learning with Transformer World Models},\n  author = {Chen, C and Wu, Y.-F and Yoon, J and Ahn, S},\n  year = {2022},\n  journal = {arXiv preprint arXiv:2202.09481},\n  eprint = {2202.09481},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{gumbsch2024thick,\n  title = {Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics},\n  author = {Gumbsch, C and Sajid, N and Martius, G and Butz, M.V},\n  year = {2024},\n  booktitle = {International Conference on Learning Representations},\n}\n\n@inproceedings{mattes2024hieros,\n  title = {Hieros: Hierarchical Imagination on Structured State Space Sequence World Models},\n  author = {Mattes, P and Schlosser, R and Herbrich, R},\n  year = {2024},\n  booktitle = {International Conference on Machine Learning},\n}\n\n@inproceedings{henderson2018deep,\n  title = {Deep Reinforcement Learning that Matters},\n  author = {Henderson, P and Islam, R and Bachman, P and Pineau, J and Precup, D and Meger, D},\n  year = {2018},\n  booktitle = {AAAI Conference on Artificial Intelligence},\n}\n\n@inproceedings{nikishin2022primacy,\n  title = {The Primacy Bias in Deep Reinforcement Learning},\n  author = {Nikishin, E and Schwarzer, M and D'Oro, P and Bacon, P.-L and Courville, A},\n  year = {2022},\n  booktitle = {International Conference on Machine Learning},\n}\n\n@article{qiao2023mind,\n  title = {Mind the Model, Not the Agent: The Primacy Bias in Model-based RL},\n  author = {Qiao, Z and Lyu, J and Li, X},\n  year = {2023},\n  journal = {arXiv preprint arXiv:2310.15017},\n  eprint = {2310.15017},\n  archivePrefix = {arXiv},\n}\n\n@article{hussing2024dissecting,\n  title = {Dissecting Deep RL with High Update Ratios: Combatting Value Divergence},\n  author = {Hussing, M and Voelcker, C.A and Gilitschenski, I and Farahmand, A.-M and Eaton, E},\n  year = {2024},\n  journal = {Reinforcement Learning Journal},\n}\n\n@article{barkley2024stealing,\n  title = {Stealing That Free Lunch: Exposing the Limits of Dyna-Style Reinforcement Learning},\n  author = {Barkley, B and Fridovich-Keil, D},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2412.14312},\n  eprint = {2412.14312},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{bjorck2022variance,\n  title = {Is High Variance Unavoidable in RL? A Case Study in Continuous Control},\n  author = {Bjorck, J and Gomes, C.P and Weinberger, K.Q},\n  year = {2022},\n  booktitle = {International Conference on Learning Representations},\n}\n\n@inproceedings{lee2024dreamsmooth,\n  title = {DreamSmooth: Improving Model-based Reinforcement Learning via Reward Smoothing},\n  author = {Lee, V and Abbeel, P and Lee, Y},\n  year = {2024},\n  booktitle = {International Conference on Learning Representations},\n}\n\n@inproceedings{ma2024harmonydream,\n  title = {HarmonyDream: Task Harmonization Inside World Models},\n  author = {Ma, H and Wu, J and Feng, N and Xiao, C and Li, D and Hao, J and Wang, J and Long, M},\n  year = {2024},\n  booktitle = {International Conference on Machine Learning},\n}\n\n@inproceedings{lambert2020objective,\n  title = {Objective Mismatch in Model-based Reinforcement Learning},\n  author = {Lambert, N and Amos, B and Yadan, O and Calandra, R},\n  year = {2020},\n  booktitle = {L4DC},\n}\n\n@inproceedings{jaderberg2017unreal,\n  title = {Reinforcement Learning with Unsupervised Auxiliary Tasks},\n  author = {Jaderberg, M and Mnih, V and Czarnecki, W.M and Schaul, T and Leibo, J.Z and Silver, D and Kavukcuoglu, K},\n  year = {2017},\n  booktitle = {International Conference on Learning Representations},\n}\n\n@inproceedings{lyle2021auxiliary,\n  title = {On The Effect of Auxiliary Tasks on Representation Dynamics},\n  author = {Lyle, C and Rowland, M and Ostrovski, G and Dabney, W},\n  year = {2021},\n  booktitle = {International Conference on Artificial Intelligence and Statistics},\n}\n\n@article{bredis2026nedreamer,\n  title = {Next Embedding Prediction Makes World Models Stronger},\n  author = {Bredis, G and Balagansky, N and Gavrilov, D and Rakhimov, R},\n  year = {2026},\n  journal = {arXiv preprint arXiv:2603.02765},\n  eprint = {2603.02765},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{zhang2025dymodreamer,\n  title = {DyMoDreamer: World Modeling with Dynamic Modulation},\n  author = {Zhang, B and Wang, R and Xiao, W and Zhang, W and Sun, J and Huang, G and Chen, J and Wang, G},\n  year = {2025},\n  booktitle = {Advances in Neural Information Processing Systems},\n}\n\n@inproceedings{liu2025vanta,\n  title = {Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning},\n  author = {Liu, T.-S and Liu, X.-H and Chen, R and Jin, L and Wang, P and Zhang, Z and Yu, Y},\n  year = {2025},\n  booktitle = {International Conference on Learning Representations},\n}\n\n@inproceedings{agarwal2021precipice,\n  title = {Deep Reinforcement Learning at the Edge of the Statistical Precipice},\n  author = {Agarwal, R and Schwarzer, M and Castro, P.S and Courville, A.C and Bellemare, M},\n  year = {2021},\n  booktitle = {Advances in Neural Information Processing Systems},\n}\n\n@article{tassa2018dmcontrol,\n  title = {DeepMind Control Suite},\n  author = {Tassa, Yuval and Doron, Yotam and Muldal, Alistair and Erez, Tom and Li, Yazhe and de Las Casas, Diego and Budden, David and Abdolmaleki, Abbas and Merel, Josh and Lefrancq, Andrew and Lillicrap, Timothy and Riedmiller, Martin},\n  year = {2018},\n  journal = {arXiv preprint arXiv:1801.00690},\n  eprint = {1801.00690},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{tallec2019making,\n  title = {Making Deep Q-learning methods Robust to Time Discretization},\n  author = {Tallec, C and Blier, L and Ollivier, Y},\n  year = {2019},\n  booktitle = {International Conference on Machine Learning},\n  eprint = {1901.09732},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{park2021sar,\n  title = {Time Discretization-Invariant Safe Action Repetition for Policy Gradient Methods},\n  author = {Park, S and Kim, J and Kim, G},\n  year = {2021},\n  booktitle = {Advances in Neural Information Processing Systems},\n  eprint = {2111.03941},\n  archivePrefix = {arXiv},\n}\n\n@article{wang2024seac,\n  title = {Reinforcement Learning with Elastic Time Steps},\n  author = {Wang, D and Beltrame, G},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2402.14961},\n  eprint = {2402.14961},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{su2020conqur,\n  title = {ConQUR: Mitigating Delusional Bias in Deep Q-learning},\n  author = {Su, D and Ooi, J and Lu, T and Schuurmans, D and Boutilier, C},\n  year = {2020},\n  booktitle = {International Conference on Machine Learning},\n  eprint = {2002.12399},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{engstrom2020implementation,\n  title = {Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO},\n  author = {Engstrom, L and Ilyas, A and Santurkar, S and Tsipras, D and Janoos, F and Rudolph, L and Madry, A},\n  year = {2020},\n  booktitle = {International Conference on Learning Representations},\n  eprint = {2005.12729},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{andrychowicz2021whatmatters,\n  title = {What Matters for On-Policy Deep Actor-Critic Methods? A Large-Scale Study},\n  author = {Andrychowicz, M and Raichuk, A and Stańczyk, P and Orsini, M and Girgin, S and Marinier, R and Hussenot, L and Geist, M and Pietquin, O and Michalski, M and Gelly, S and Bachem, O},\n  year = {2021},\n  booktitle = {International Conference on Learning Representations},\n  eprint = {2006.05990},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{frauenknecht2025rollouts,\n  title = {On Rollouts in Model-Based Reinforcement Learning},\n  author = {Frauenknecht, B and Subhasish, D and Solowjow, F and Trimpe, S},\n  year = {2025},\n  booktitle = {International Conference on Learning Representations},\n  eprint = {2501.16918},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{voelcker2025madtd,\n  title = {MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL},\n  author = {Voelcker, C and Hussing, M and Eaton, E and Farahmand, A.-M and Gilitschenski, I},\n  year = {2025},\n  booktitle = {International Conference on Learning Representations},\n  eprint = {2410.08896},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{nie2025sdar,\n  title = {Select before Act: Spatially Decoupled Action Repetition for Continuous Control},\n  author = {Nie, B and et, al},\n  year = {2025},\n  booktitle = {International Conference on Learning Representations},\n  eprint = {2502.06919},\n  archivePrefix = {arXiv},\n}\n\n@article{hafner2025dreamerv4,\n  title = {Training Agents Inside of Scalable World Models},\n  author = {Hafner, D and Yan, W and Lillicrap, T},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2509.24527},\n  eprint = {2509.24527},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{zhang2026instability,\n  title = {Training instability in deep learning follows low-dimensional dynamical principles},\n  author = {Zhang, L and et, al},\n  year = {2026},\n  booktitle = {International Conference on Learning Representations},\n  eprint = {2601.13160},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{sokar2023dormant,\n  title = {The Dormant Neuron Phenomenon in Deep Reinforcement Learning},\n  author = {Sokar, G and Agarwal, R and Castro, P.S and Evci, U},\n  year = {2023},\n  booktitle = {International Conference on Machine Learning},\n}\n\n@inproceedings{lyle2022capacity,\n  title = {Understanding and Preventing Capacity Loss in Reinforcement Learning},\n  author = {Lyle, C and Rowland, M and Dabney, W},\n  year = {2022},\n  booktitle = {International Conference on Learning Representations},\n  eprint = {2204.09560},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{kumar2022dr3,\n  title = {DR3: Value-Based Deep Reinforcement Learning Requires Explicit Regularization},\n  author = {Kumar, A and Agarwal, R and Ma, T and Courville, A and Tucker, G and Levine, S},\n  year = {2022},\n  booktitle = {International Conference on Learning Representations},\n}\n\n@article{colas2018seeds,\n  title = {How Many Random Seeds? Statistical Power Analysis in Deep Reinforcement Learning Experiments},\n  author = {Colas, C and Sigaud, O and Oudeyer, P.-Y},\n  year = {2018},\n  journal = {arXiv preprint arXiv:1806.08295},\n  eprint = {1806.08295},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{nikishin2023plasticity,\n  title = {Deep Reinforcement Learning with Plasticity Injection},\n  author = {Nikishin, E and Oh, J and Ostrovski, G and Lyle, C and Pascanu, R and Dabney, W and Barreto, A},\n  year = {2023},\n  booktitle = {Advances in Neural Information Processing Systems},\n}\n\n@inproceedings{schwarzer2023bbf,\n  title = {Bigger, Better, Faster: Human-level Atari with Human-level Efficiency},\n  author = {Schwarzer, M and Obando-Ceron, J.S and Courville, A and Bellemare, M and Agarwal, R and Castro, P.S},\n  year = {2023},\n  booktitle = {International Conference on Machine Learning},\n}\n\n@inproceedings{farebrother2024stopregressing,\n  title = {Stop Regressing: Training Value Functions via Classification for Scalable Deep RL},\n  author = {Farebrother, J and Orbay, J and Vuong, Q and Taiga, A.A and Chebotar, Y and Xiao, T and Irpan, A and Levine, S and Castro, P.S and Faust, A and Kumar, A and Agarwal, R},\n  year = {2024},\n  booktitle = {International Conference on Machine Learning},\n}\n\n@inproceedings{lyle2024normalization,\n  title = {Normalization and Effective Learning Rates in Reinforcement Learning},\n  author = {Lyle, C and Zheng, Z and Giunchiglia, E and Sherstan, C and Hashemizadeh, M and Schuurmans, D and Dabney, W},\n  year = {2024},\n  booktitle = {Advances in Neural Information Processing Systems},\n}\n\n@inproceedings{nhu2025tawm,\n  title = {Time-Aware World Model for Adaptive Prediction and Control},\n  author = {Nhu, A.N and Son, S and Lin, M.C},\n  year = {2025},\n  booktitle = {International Conference on Machine Learning},\n  eprint = {2506.08441},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{li2025lsimagine,\n  title = {Open-World Reinforcement Learning over Long Short-Term Imagination},\n  author = {Li, J and Wang, Q and Wang, Y and Jin, X and Li, Y and Zeng, W and Yang, X},\n  year = {2025},\n  booktitle = {International Conference on Learning Representations},\n  eprint = {2410.03618},\n  archivePrefix = {arXiv},\n}\n\n@article{zhang2026hwm,\n  title = {Hierarchical Planning with Latent World Models},\n  author = {Zhang, W and Terver, B and Zholus, A and Chitnis, S and Sutaria, H and Assran, M and Balestriero, R and Bar, A and Bardes, A and LeCun, Y and Ballas, N},\n  year = {2026},\n  journal = {arXiv preprint arXiv:2604.03208},\n  eprint = {2604.03208},\n  archivePrefix = {arXiv},\n}\n\n@article{kobayashi2025metacontroller,\n  title = {Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning},\n  author = {Kobayashi, S and et, al},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2512.20605},\n  eprint = {2512.20605},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{shaj2023mts3,\n  title = {Multi Time Scale World Models},\n  author = {Shaj, V and Gholam, Zadeh S and Demir, O and Douat, L.R and Neumann, G},\n  year = {2023},\n  booktitle = {Advances in Neural Information Processing Systems},\n  eprint = {2310.18534},\n  archivePrefix = {arXiv},\n}\n\n@article{splates2025,\n  title = {Stable Planning with Temporally Extended Skills},\n  author = {SPlaTES, authors},\n  year = {2025},\n  journal = {Reinforcement Learning Journal},\n}\n\n@article{beckerehmck2023multitimestep,\n  title = {Multi-timestep models for Model-based Reinforcement Learning},\n  author = {Becker-Ehmck, Philip and Peters, Jan and {van der Smagt}, Patrick},\n  year = {2023},\n  journal = {arXiv preprint arXiv:2310.05672},\n  eprint = {2310.05672},\n  archivePrefix = {arXiv},\n}\n\n@article{liu2022dmve,\n  title = {Dynamic-Horizon Model-Based Value Estimation With Latent Imagination},\n  author = {Liu, Y and et, al},\n  year = {2022},\n  journal = {IEEE TNNLS},\n  eprint = {2009.09593},\n  archivePrefix = {arXiv},\n}\n\n@article{palenicek2025diminishing,\n  title = {Diminishing Return of Value Expansion Methods},\n  author = {Palenicek, D and Lutter, M and Carvalho, J and Dennert, D and Ahmad, F and Peters, J},\n  year = {2025},\n  journal = {Reinforcement Learning Journal},\n  eprint = {2412.20537},\n  archivePrefix = {arXiv},\n}\n\n@article{kim2025deas,\n  title = {DEAS: DEtached value learning with Action Sequence for Scalable Offline RL},\n  author = {Kim, C and Seo, Y and et, al},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2510.07730},\n  eprint = {2510.07730},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{luo2025vpl,\n  title = {A Case for Validation Buffer in Pessimistic Actor-Critic},\n  author = {Nauman, M and Ostaszewski, M and Cygan, M},\n  year = {2025},\n  booktitle = {IJCAI 2025},\n  eprint = {2403.01014},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{chen2021redq,\n  title = {Randomized Ensembled Double Q-Learning: Learning Fast Without a Model},\n  author = {Chen, Xinyue and Wang, Che and Zhou, Zijian and Ross, Keith},\n  year = {2021},\n  booktitle = {International Conference on Learning Representations},\n  eprint = {2101.05982},\n  archivePrefix = {arXiv},\n}\n\n@article{lenz2025macura,\n  title = {Trust the Model Where It Trusts Itself -- Model-Based Actor-Critic with Uncertainty-Aware Rollout Adaption},\n  author = {Lenz, S and et, al},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2405.19014},\n  eprint = {2405.19014},\n  archivePrefix = {arXiv},\n}\n",
      "numLines": 619,
      "startLine": 1,
      "totalLines": 619
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full related work and bib file. Let me catalog the cited papers, then run web searches for each direction. Let me launch multiple search agents in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "bffb44e3-faaa-4d82-8c59-3f800e68cdfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013u4uF88DJoLUHyebeVX381",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9401,
      "cache_read_input_tokens": 26414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9401
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

_source line 13_

已读取所有文件。现在并行搜索三个方向的近期论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "67d45f2b-773e-417f-b243-4ef6cb0449d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013u4uF88DJoLUHyebeVX381",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9401,
      "cache_read_input_tokens": 26414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9401
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

_source line 14_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012EFqgLmXArma4ujY8CA2Ut`</summary>

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
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "1054dd0e-902e-4475-93c1-862ca6d0f093",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013u4uF88DJoLUHyebeVX381",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9401,
      "cache_read_input_tokens": 26414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9401
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

_source line 15 · 2026-05-18T13:58:28.599Z_

<details><summary>↩ Tool result · `toolu_012EFqgLmXArma4ujY8CA2Ut`</summary>

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
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "78a5ac39-65ea-4d89-b027-dcf58109fd2c",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now let me run multiple web searches in parallel for the three directions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "e49412a2-648a-478b-a723-9b34a1617815",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoHYn9sdbAbjgDPTaJ1SnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 35815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 679
      },
      "output_tokens": 33,
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

_source line 17_

开始并行搜索三个方向的近期论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "e2e3fa52-3caa-4374-9602-8c9ff230f219",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoHYn9sdbAbjgDPTaJ1SnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 35815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 679
      },
      "output_tokens": 33,
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

_source line 18_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WEfiWJC7fgtAsHi7eQV6Jk`</summary>

```json
{
  "query": "world model reinforcement learning temporal abstraction 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "315f294a-d951-463a-a922-81cf55459752",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoHYn9sdbAbjgDPTaJ1SnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 35815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 679
      },
      "output_tokens": 33,
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

_source line 19_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S6Kys6RHQ9Gf4MudX1zu1F`</summary>

```json
{
  "query": "DreamerV3 temporal abstraction variable time step options framework"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "e0d99398-a3d1-4700-9d69-fb4c3ffdc3bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoHYn9sdbAbjgDPTaJ1SnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 35815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 679
      },
      "output_tokens": 33,
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

_source line 20_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X8Zr4t3ujbBC6mPxBDKXBG`</summary>

```json
{
  "query": "value overestimation model-based reinforcement learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "da62b94b-967d-4c3c-8158-210e580b1782",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoHYn9sdbAbjgDPTaJ1SnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 35815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 679
      },
      "output_tokens": 33,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ME9QDbtLS16dhp2eokxWwW`</summary>

```json
{
  "query": "critic overestimation world model imagination rollout bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "b674f00d-77ee-42ca-8350-38ad86de4610",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoHYn9sdbAbjgDPTaJ1SnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 35815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 679
      },
      "output_tokens": 33,
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

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0123ZDNNSJmwZ2iioRQ2hxbM`</summary>

```json
{
  "query": "TAWM temporal abstraction world model Nhu 2025 ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "d8659b4d-466f-4e7c-bd57-04683b498483",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoHYn9sdbAbjgDPTaJ1SnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 35815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 679
      },
      "output_tokens": 33,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NkN8CFfNcihCpB9Dq6GXg3`</summary>

```json
{
  "query": "DreamerV3 variant improvement modification 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "0de08147-11d2-47b5-93bb-5c5e20561273",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoHYn9sdbAbjgDPTaJ1SnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 35815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 679
      },
      "output_tokens": 33,
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

_source line 24 · 2026-05-18T13:58:39.832Z_

<details><summary>↩ Tool result · `toolu_01S6Kys6RHQ9Gf4MudX1zu1F`</summary>

```text
Web search results for query: "DreamerV3 temporal abstraction variable time step options framework"

Links: [{"title":"TransDreamerV3: Implanting Transformer In DreamerV3","url":"https://arxiv.org/html/2506.17103v1"},{"title":"Learning Temporal Abstractions via Variational Homomorphisms in Option-Induced Abstract MDPs","url":"https://arxiv.org/html/2507.16473"},{"title":"DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12510832/"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"Mastering Diverse Control Tasks through World Models","url":"https://danijar.com/project/dreamerv3/"},{"title":"GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub","url":"https://github.com/danijar/dreamerv3"},{"title":"Next Embedding Prediction Makes World Models Stronger","url":"https://arxiv.org/html/2603.02765v1"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"DreamerV3: Mastering Diverse Domains through World Models","url":"https://vitalab.github.io/article/2023/01/19/DreamerV3.html"},{"title":"Temporal Abstraction and the Options Framework How Agents Learn to Think in Subgoals - Engineering Notes","url":"https://notes.muthu.co/2026/02/temporal-abstraction-and-the-options-framework-how-agents-learn-to-think-in-subgoals/"}]

Based on the search results, I found information relevant to your query. Here's what I discovered:

## DreamerV3 Framework

DreamerV3 is a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration. Dreamer learns a model of the environment and improves its behaviour by imagining future scenarios, with robustness techniques based on normalization, balancing and transformations enabling stable learning across domains.

## World Model Architecture

The world model, dubbed the "Recurrent State-Space Model (RSSM)" can be described by several networks including an encoder and dynamics predictor. DreamerV3 learns a world model from experiences and uses it to train an actor critic policy from imagined trajectories. The world model encodes sensory inputs into categorical representations and predicts future representations and rewards given actions.

## Temporal Abstraction and Options Framework

The search results include information about temporal abstraction in the options framework more generally. In this framework, options act as temporally abstracted actions executed over variable time steps, controlled by a master policy that decides when each option should execute and terminate. Temporal abstraction means thinking in terms of extended behaviors that span many low-level steps rather than selecting each action independently.

However, the search results do not contain specific information about DreamerV3 implementing temporal abstraction through variable time step options directly. The results primarily focus on DreamerV3's core architecture and general temporal abstraction concepts in hierarchical reinforcement learning frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "1cdab860-6331-4fcb-95fd-55b1005a0b22",
  "tool_use_result": {
    "query": "DreamerV3 temporal abstraction variable time step options framework",
    "results": [
      {
        "tool_use_id": "srvtoolu_014TyffjJ7kgWXqo3uUK8H2V",
        "content": [
          {
            "title": "TransDreamerV3: Implanting Transformer In DreamerV3",
            "url": "https://arxiv.org/html/2506.17103v1"
          },
          {
            "title": "Learning Temporal Abstractions via Variational Homomorphisms in Option-Induced Abstract MDPs",
            "url": "https://arxiv.org/html/2507.16473"
          },
          {
            "title": "DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12510832/"
          },
          {
            "title": "Mastering diverse control tasks through world models | Nature",
            "url": "https://www.nature.com/articles/s41586-025-08744-2"
          },
          {
            "title": "Mastering Diverse Control Tasks through World Models",
            "url": "https://danijar.com/project/dreamerv3/"
          },
          {
            "title": "GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub",
            "url": "https://github.com/danijar/dreamerv3"
          },
          {
            "title": "Next Embedding Prediction Makes World Models Stronger",
            "url": "https://arxiv.org/html/2603.02765v1"
          },
          {
            "title": "Mastering diverse control tasks through world models - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"
          },
          {
            "title": "DreamerV3: Mastering Diverse Domains through World Models",
            "url": "https://vitalab.github.io/article/2023/01/19/DreamerV3.html"
          },
          {
            "title": "Temporal Abstraction and the Options Framework How Agents Learn to Think in Subgoals - Engineering Notes",
            "url": "https://notes.muthu.co/2026/02/temporal-abstraction-and-the-options-framework-how-agents-learn-to-think-in-subgoals/"
          }
        ]
      },
      "Based on the search results, I found information relevant to your query. Here's what I discovered:\n\n## DreamerV3 Framework\n\nDreamerV3 is a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration. Dreamer learns a model of the environment and improves its behaviour by imagining future scenarios, with robustness techniques based on normalization, balancing and transformations enabling stable learning across domains.\n\n## World Model Architecture\n\nThe world model, dubbed the \"Recurrent State-Space Model (RSSM)\" can be described by several networks including an encoder and dynamics predictor. DreamerV3 learns a world model from experiences and uses it to train an actor critic policy from imagined trajectories. The world model encodes sensory inputs into categorical representations and predicts future representations and rewards given actions.\n\n## Temporal Abstraction and Options Framework\n\nThe search results include information about temporal abstraction in the options framework more generally. In this framework, options act as temporally abstracted actions executed over variable time steps, controlled by a master policy that decides when each option should execute and terminate. Temporal abstraction means thinking in terms of extended behaviors that span many low-level steps rather than selecting each action independently.\n\nHowever, the search results do not contain specific information about DreamerV3 implementing temporal abstraction through variable time step options directly. The results primarily focus on DreamerV3's core architecture and general temporal abstraction concepts in hierarchical reinforcement learning frameworks."
    ],
    "durationSeconds": 7.078369429999999
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-18T13:58:40.383Z_

<details><summary>↩ Tool result · `toolu_01X8Zr4t3ujbBC6mPxBDKXBG`</summary>

```text
Web search results for query: "value overestimation model-based reinforcement learning 2024 2025"

Links: [{"title":"A value-based deep reinforcement learning model with human expertise in optimal treatment of sepsis | npj Digital Medicine","url":"https://www.nature.com/articles/s41746-023-00755-5"},{"title":"MAD-TD: MODEL-AUGMENTED DATA STABILIZES HIGH ...","url":"https://www.seas.upenn.edu/~eeaton/papers/Voelcker2025MADTD.pdf"},{"title":"model-based offline reinforcement learning","url":"https://arxiv.org/pdf/2407.00699"},{"title":"mad-td: model-augmented data stabilizes high update ratio rl","url":"https://arxiv.org/pdf/2410.08896"},{"title":"The State of Reinforcement Learning in 2025 - DataRoot Labs","url":"https://datarootlabs.com/blog/state-of-reinforcement-learning-2025"},{"title":"“Deep Reinforcement Learning for Autonomous Navigation ...","url":"https://jisem-journal.com/index.php/journal/article/download/3620/1566/5930"},{"title":"[2506.14245] Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs","url":"https://arxiv.org/abs/2506.14245"},{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"GitHub - yingchengyang/Reinforcement-Learning-Papers: Related papers for reinforcement learning, including classic papers and latest papers in top conferences · GitHub","url":"https://github.com/yingchengyang/Reinforcement-Learning-Papers"},{"title":"[1803.00101] Model-Based Value Estimation for Efficient Model-Free Reinforcement Learning","url":"https://arxiv.org/abs/1803.00101"}]

Here are the search results for "value overestimation model-based reinforcement learning 2024 2025":

## Key Findings

**Value Overestimation in Reinforcement Learning:**

One of the major challenges in offline reinforcement learning (RL) is the overestimation of values for out-of-distribution actions due to the lack of environment interactions. Model-based offline RL addresses this issue by generating additional (imaginary) training data using a learned model, thereby augmenting the given offline data with synthetic experiences that cover out-of-distribution states and actions.

**Recent Approaches (2024-2025):**

Prior work has stabilized the learning by using double Q minimization to reduce overestimation, training ensemble methods to improve value estimation, introducing architectural regularization, or resetting networks periodically throughout the learning process. However, these interventions can mitigate catastrophic overestimation and divergence, but do not guarantee proper generalization, and pessimistic underestimation and architectural regularization are insufficient by themselves to combat the problem.

**Model-Augmented Approaches:**

A 2025 paper on MAD-TD (Model-Augmented Data) proposes stabilizing high update-ratio RL through model-augmented data approaches, though model-based offline RL struggles with noisy model predictions and value estimates, particularly in long-horizon tasks.

The search results indicate that value overestimation remains an active research problem in model-based reinforcement learning, with ongoing efforts to develop more robust approaches to manage this fundamental challenge.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "55ef75ce-39de-4987-97d2-401e3fba4048",
  "tool_use_result": {
    "query": "value overestimation model-based reinforcement learning 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0195QsG9ejXEuzynSBzYr3CM",
        "content": [
          {
            "title": "A value-based deep reinforcement learning model with human expertise in optimal treatment of sepsis | npj Digital Medicine",
            "url": "https://www.nature.com/articles/s41746-023-00755-5"
          },
          {
            "title": "MAD-TD: MODEL-AUGMENTED DATA STABILIZES HIGH ...",
            "url": "https://www.seas.upenn.edu/~eeaton/papers/Voelcker2025MADTD.pdf"
          },
          {
            "title": "model-based offline reinforcement learning",
            "url": "https://arxiv.org/pdf/2407.00699"
          },
          {
            "title": "mad-td: model-augmented data stabilizes high update ratio rl",
            "url": "https://arxiv.org/pdf/2410.08896"
          },
          {
            "title": "The State of Reinforcement Learning in 2025 - DataRoot Labs",
            "url": "https://datarootlabs.com/blog/state-of-reinforcement-learning-2025"
          },
          {
            "title": "“Deep Reinforcement Learning for Autonomous Navigation ...",
            "url": "https://jisem-journal.com/index.php/journal/article/download/3620/1566/5930"
          },
          {
            "title": "[2506.14245] Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs",
            "url": "https://arxiv.org/abs/2506.14245"
          },
          {
            "title": "GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub",
            "url": "https://github.com/opendilab/awesome-RLVR"
          },
          {
            "title": "GitHub - yingchengyang/Reinforcement-Learning-Papers: Related papers for reinforcement learning, including classic papers and latest papers in top conferences · GitHub",
            "url": "https://github.com/yingchengyang/Reinforcement-Learning-Papers"
          },
          {
            "title": "[1803.00101] Model-Based Value Estimation for Efficient Model-Free Reinforcement Learning",
            "url": "https://arxiv.org/abs/1803.00101"
          }
        ]
      },
      "Here are the search results for \"value overestimation model-based reinforcement learning 2024 2025\":\n\n## Key Findings\n\n**Value Overestimation in Reinforcement Learning:**\n\nOne of the major challenges in offline reinforcement learning (RL) is the overestimation of values for out-of-distribution actions due to the lack of environment interactions. Model-based offline RL addresses this issue by generating additional (imaginary) training data using a learned model, thereby augmenting the given offline data with synthetic experiences that cover out-of-distribution states and actions.\n\n**Recent Approaches (2024-2025):**\n\nPrior work has stabilized the learning by using double Q minimization to reduce overestimation, training ensemble methods to improve value estimation, introducing architectural regularization, or resetting networks periodically throughout the learning process. However, these interventions can mitigate catastrophic overestimation and divergence, but do not guarantee proper generalization, and pessimistic underestimation and architectural regularization are insufficient by themselves to combat the problem.\n\n**Model-Augmented Approaches:**\n\nA 2025 paper on MAD-TD (Model-Augmented Data) proposes stabilizing high update-ratio RL through model-augmented data approaches, though model-based offline RL struggles with noisy model predictions and value estimates, particularly in long-horizon tasks.\n\nThe search results indicate that value overestimation remains an active research problem in model-based reinforcement learning, with ongoing efforts to develop more robust approaches to manage this fundamental challenge."
    ],
    "durationSeconds": 7.089693293
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T13:58:40.961Z_

<details><summary>↩ Tool result · `toolu_01ME9QDbtLS16dhp2eokxWwW`</summary>

```text
Web search results for query: "critic overestimation world model imagination rollout bias"

Links: [{"title":"Dreamer: Learning Long-Horizon Behaviors through Latent Imagination | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/dreamer-learning-long-horizon-behaviors-through-latent-imagination-fa60327c2843"},{"title":"Critiques of World Models","url":"https://arxiv.org/pdf/2507.05169"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"Realistic Actor-Critic: A framework for balance between value overestimation and underestimation - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9868235/"},{"title":"World Models with Hints of Large Language ...","url":"https://aclanthology.org/2025.naacl-long.3.pdf"},{"title":"Interpretable World Model Imaginations as Deep Reinforcement Learning Explanation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-08327-2_7"},{"title":"arXiv:2507.05169v1 [cs.LG] 7 Jul 2025 Critiques of World Models","url":"https://arxiv.org/pdf/2507.05169v1"},{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Critique of World Models As A Path to Human Level Intelligence: A Comprehensive Outline with References | by Jacob Grow | Medium","url":"https://medium.com/@Gbgrow/critique-of-world-models-as-a-path-to-human-level-intelligence-a-comprehensive-outline-with-1a50e459b050"},{"title":"Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss","url":"https://arxiv.org/html/2504.09929v1"}]

Here are the search results for your query about critic overestimation, world models, imagination rollout bias:

## Key Findings

### Critic Overestimation in World Models

Undesirable overestimation bias and accumulation of function approximation errors in temporal difference methods may lead to sub-optimal policy updates and divergent behaviors.

### World Models and Imagination Rollouts

Dreamer uses imagined latent trajectories to train an actor and a critic, with these components optimized via multi-step returns derived from rollouts inside the learned dynamics. To improve value prediction in environments where rewards are challenging to predict, the critic loss is applied both to imagined trajectories and to trajectories sampled from the replay buffer, with the critic replay loss using imagination returns as on-policy value annotations.

### Overestimation Issues in World Model Learning

World models, especially in Dreamer, tend to overestimate aleatoric uncertainty, and therefore world models likely cannot be used to reliably predict the future.

### Addressing Overestimation Bias

Most model-free off-policy RL methods learn approximate lower confidence bound of Q-function to avoid overestimation by introducing underestimation bias. Overestimation bias can be mitigated by defining the target as the minimum value of two approximated Q-functions, referred to as the min-Q target.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "02b445ff-b7ed-4511-8881-404a8512e24d",
  "tool_use_result": {
    "query": "critic overestimation world model imagination rollout bias",
    "results": [
      {
        "tool_use_id": "srvtoolu_011LDNF2nKHBNx7G8ydpxT44",
        "content": [
          {
            "title": "Dreamer: Learning Long-Horizon Behaviors through Latent Imagination | by Dong-Keon Kim | Medium",
            "url": "https://medium.com/@kdk199604/dreamer-learning-long-horizon-behaviors-through-latent-imagination-fa60327c2843"
          },
          {
            "title": "Critiques of World Models",
            "url": "https://arxiv.org/pdf/2507.05169"
          },
          {
            "title": "Mastering diverse control tasks through world models - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"
          },
          {
            "title": "Realistic Actor-Critic: A framework for balance between value overestimation and underestimation - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9868235/"
          },
          {
            "title": "World Models with Hints of Large Language ...",
            "url": "https://aclanthology.org/2025.naacl-long.3.pdf"
          },
          {
            "title": "Interpretable World Model Imaginations as Deep Reinforcement Learning Explanation | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-08327-2_7"
          },
          {
            "title": "arXiv:2507.05169v1 [cs.LG] 7 Jul 2025 Critiques of World Models",
            "url": "https://arxiv.org/pdf/2507.05169v1"
          },
          {
            "title": "Reinforcement Learning Journal 2025 Cover Page",
            "url": "https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"
          },
          {
            "title": "Critique of World Models As A Path to Human Level Intelligence: A Comprehensive Outline with References | by Jacob Grow | Medium",
            "url": "https://medium.com/@Gbgrow/critique-of-world-models-as-a-path-to-human-level-intelligence-a-comprehensive-outline-with-1a50e459b050"
          },
          {
            "title": "Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss",
            "url": "https://arxiv.org/html/2504.09929v1"
          }
        ]
      },
      "Here are the search results for your query about critic overestimation, world models, imagination rollout bias:\n\n## Key Findings\n\n### Critic Overestimation in World Models\n\nUndesirable overestimation bias and accumulation of function approximation errors in temporal difference methods may lead to sub-optimal policy updates and divergent behaviors.\n\n### World Models and Imagination Rollouts\n\nDreamer uses imagined latent trajectories to train an actor and a critic, with these components optimized via multi-step returns derived from rollouts inside the learned dynamics. To improve value prediction in environments where rewards are challenging to predict, the critic loss is applied both to imagined trajectories and to trajectories sampled from the replay buffer, with the critic replay loss using imagination returns as on-policy value annotations.\n\n### Overestimation Issues in World Model Learning\n\nWorld models, especially in Dreamer, tend to overestimate aleatoric uncertainty, and therefore world models likely cannot be used to reliably predict the future.\n\n### Addressing Overestimation Bias\n\nMost model-free off-policy RL methods learn approximate lower confidence bound of Q-function to avoid overestimation by introducing underestimation bias. Overestimation bias can be mitigated by defining the target as the minimum value of two approximated Q-functions, referred to as the min-Q target."
    ],
    "durationSeconds": 6.635991837999998
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T13:58:41.157Z_

<details><summary>↩ Tool result · `toolu_01WEfiWJC7fgtAsHi7eQV6Jk`</summary>

```text
Web search results for query: "world model reinforcement learning temporal abstraction 2024 2025"

Links: [{"title":"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | OpenReview","url":"https://openreview.net/forum?id=TjCDNssXKU"},{"title":"Exploring the limits of hierarchical world models in reinforcement learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-76719-w"},{"title":"[2512.20605] Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://arxiv.org/abs/2512.20605"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"Hierarchical Planning with Latent World Models","url":"https://arxiv.org/html/2604.03208v1"},{"title":"ICLR Poster Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics","url":"https://iclr.cc/virtual/2024/poster/18558"},{"title":"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://arxiv.org/html/2512.20605v1"},{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"},{"title":"[Quick Review] Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://liner.com/review/emergent-temporal-abstractions-in-autoregressive-models-enable-hierarchical-reinforcement-learning"},{"title":"Humans rationally balance detailed and temporally abstract world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11700031/"}]

I found several highly relevant research papers on world models, reinforcement learning, and temporal abstraction from 2024-2025. Here's a summary of the key findings:

## Recent Advances in Hierarchical World Models with Temporal Abstraction

**THICK (Temporal Hierarchies from Invariant Context Kernels)**

Hierarchical world models can significantly improve model-based reinforcement learning (MBRL) and planning by enabling reasoning across multiple time scales. THICK is an algorithm that learns a world model hierarchy via discrete latent dynamics. THICK adaptively discovers higher-level time scales by guiding the lower-level world model to update parts of its latent state only sparsely in time, and the high-level model is then trained to predict scenarios involving changes in these low-level latent states.

**Emergent Temporal Abstractions in Autoregressive Models (2025)**

A recent paper from December 2025 presents a novel approach: acting and exploring within the internal representations of an autoregressive model is possible by introducing a higher-order, non-causal sequence model whose outputs control the residual stream activations of a base autoregressive model to discover temporally-abstract actions. Internal RL significantly outperforms standard RL finetuning and other baselines in sparse-reward hierarchical tasks, achieving high initial success rates and efficient credit assignment.

**Hierarchical Planning with Latent World Models (2026)**

Learned world models continue to struggle with long-horizon control due to two fundamental challenges: (i) prediction errors compound over time, leading to increasingly inaccurate rollouts, and (ii) even under a perfect model, planning becomes computationally expensive as the search space grows exponentially with horizon.

**Dreamer V3 (2025)**

Dreamer is a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration. Dreamer learns a model of the environment and improves its behaviour by imagining future scenarios.

These works represent significant progress in addressing the challenge of enabling agents to reason and plan effectively across multiple temporal scales using learned world models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "90d3d6de-765d-44f8-afee-81b345c34e29",
  "tool_use_result": {
    "query": "world model reinforcement learning temporal abstraction 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0159PAQsBBLu71yhHVUsov5N",
        "content": [
          {
            "title": "Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | OpenReview",
            "url": "https://openreview.net/forum?id=TjCDNssXKU"
          },
          {
            "title": "Exploring the limits of hierarchical world models in reinforcement learning | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-024-76719-w"
          },
          {
            "title": "[2512.20605] Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning",
            "url": "https://arxiv.org/abs/2512.20605"
          },
          {
            "title": "Mastering diverse control tasks through world models | Nature",
            "url": "https://www.nature.com/articles/s41586-025-08744-2"
          },
          {
            "title": "Hierarchical Planning with Latent World Models",
            "url": "https://arxiv.org/html/2604.03208v1"
          },
          {
            "title": "ICLR Poster Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics",
            "url": "https://iclr.cc/virtual/2024/poster/18558"
          },
          {
            "title": "Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning",
            "url": "https://arxiv.org/html/2512.20605v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"
          },
          {
            "title": "[Quick Review] Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning",
            "url": "https://liner.com/review/emergent-temporal-abstractions-in-autoregressive-models-enable-hierarchical-reinforcement-learning"
          },
          {
            "title": "Humans rationally balance detailed and temporally abstract world models - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11700031/"
          }
        ]
      },
      "I found several highly relevant research papers on world models, reinforcement learning, and temporal abstraction from 2024-2025. Here's a summary of the key findings:\n\n## Recent Advances in Hierarchical World Models with Temporal Abstraction\n\n**THICK (Temporal Hierarchies from Invariant Context Kernels)**\n\nHierarchical world models can significantly improve model-based reinforcement learning (MBRL) and planning by enabling reasoning across multiple time scales. THICK is an algorithm that learns a world model hierarchy via discrete latent dynamics. THICK adaptively discovers higher-level time scales by guiding the lower-level world model to update parts of its latent state only sparsely in time, and the high-level model is then trained to predict scenarios involving changes in these low-level latent states.\n\n**Emergent Temporal Abstractions in Autoregressive Models (2025)**\n\nA recent paper from December 2025 presents a novel approach: acting and exploring within the internal representations of an autoregressive model is possible by introducing a higher-order, non-causal sequence model whose outputs control the residual stream activations of a base autoregressive model to discover temporally-abstract actions. Internal RL significantly outperforms standard RL finetuning and other baselines in sparse-reward hierarchical tasks, achieving high initial success rates and efficient credit assignment.\n\n**Hierarchical Planning with Latent World Models (2026)**\n\nLearned world models continue to struggle with long-horizon control due to two fundamental challenges: (i) prediction errors compound over time, leading to increasingly inaccurate rollouts, and (ii) even under a perfect model, planning becomes computationally expensive as the search space grows exponentially with horizon.\n\n**Dreamer V3 (2025)**\n\nDreamer is a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration. Dreamer learns a model of the environment and improves its behaviour by imagining future scenarios.\n\nThese works represent significant progress in addressing the challenge of enabling agents to reason and plan effectively across multiple temporal scales using learned world models."
    ],
    "durationSeconds": 8.859862068999998
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T13:58:42.152Z_

<details><summary>↩ Tool result · `toolu_0123ZDNNSJmwZ2iioRQ2hxbM`</summary>

```text
Web search results for query: "TAWM temporal abstraction world model Nhu 2025 ICML"

Links: [{"title":"GitHub - anh-nn01/Time-Aware-World-Model: Official Code for Time-Aware World Model (TAWM) with TD-MPC2 as the baseline architecture in the experiments.","url":"https://github.com/anh-nn01/Time-Aware-World-Model"},{"title":"Time-Aware World Model for Adaptive Prediction and Control","url":"https://arxiv.org/html/2506.08441v1"},{"title":"[2506.08441] Time-Aware World Model for Adaptive Prediction and Control","url":"https://arxiv.org/abs/2506.08441"},{"title":"Time-Aware World Model for Adaptive Prediction and Control | OpenReview","url":"https://openreview.net/forum?id=gZ5N3TLjwv"},{"title":"ICML 2025 Schedule","url":"https://icml.cc/virtual/2025/calendar"},{"title":"World Models - ICLR 2025 Workshop","url":"https://sites.google.com/view/worldmodel-iclr2025/"},{"title":"[2404.16078] Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective","url":"https://arxiv.org/abs/2404.16078"},{"title":"Feature 14 IEEE CIRCUITS AND SYSTEMS MAGAZINE FOURTH QUARTER 2025","url":"https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_Embodied%20AI%20from%20LLMs%20to%20World%20Models.pdf"},{"title":"Assessing World Models: Methods and Metrics for Evaluating Understanding","url":"https://icml.cc/virtual/2025/workshop/39967"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"}]

Based on the search results, here's information about TAWM (Time-Aware World Model) by Nhu et al. at ICML 2025:

## Overview

Time-Aware World Model (TAWM) is a model-agnostic and more efficient training method for world models, presented by Anh N. Nhu, Sanghyun Son, and Ming C. Lin from the University of Maryland at the International Conference on Machine Learning (ICML) 2025.

## Core Approach

TAWM is a model-based approach that explicitly incorporates temporal dynamics by conditioning on the time-step size (Δt) and training over a diverse range of Δt values, rather than sampling at a fixed time-step, which allows it to learn both high- and low-frequency task dynamics across diverse control problems.

## Key Innovation

Grounded in the information-theoretic insight that the optimal sampling rate depends on a system's underlying dynamics, this time-aware formulation improves both performance and data efficiency.

## Results

Empirical evaluations show that TAWM consistently outperforms conventional models across varying observation rates in a variety of control tasks, using the same number of training samples and iterations.

## Implementation

TAWM is built on top of TD-MPC2 world model architecture as the basis of the experiments, though TAWM's core contribution is the time-aware training method, which is architecture-agnostic and can be incorporated into any world model training pipeline.

The code can be found online at github.com/anh-nn01/Time-Aware-World-Model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "c9a18a15-8c37-4456-8d28-7615fea473e8",
  "tool_use_result": {
    "query": "TAWM temporal abstraction world model Nhu 2025 ICML",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CmSRdEsgZYZnmfRyB4smDt",
        "content": [
          {
            "title": "GitHub - anh-nn01/Time-Aware-World-Model: Official Code for Time-Aware World Model (TAWM) with TD-MPC2 as the baseline architecture in the experiments.",
            "url": "https://github.com/anh-nn01/Time-Aware-World-Model"
          },
          {
            "title": "Time-Aware World Model for Adaptive Prediction and Control",
            "url": "https://arxiv.org/html/2506.08441v1"
          },
          {
            "title": "[2506.08441] Time-Aware World Model for Adaptive Prediction and Control",
            "url": "https://arxiv.org/abs/2506.08441"
          },
          {
            "title": "Time-Aware World Model for Adaptive Prediction and Control | OpenReview",
            "url": "https://openreview.net/forum?id=gZ5N3TLjwv"
          },
          {
            "title": "ICML 2025 Schedule",
            "url": "https://icml.cc/virtual/2025/calendar"
          },
          {
            "title": "World Models - ICLR 2025 Workshop",
            "url": "https://sites.google.com/view/worldmodel-iclr2025/"
          },
          {
            "title": "[2404.16078] Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective",
            "url": "https://arxiv.org/abs/2404.16078"
          },
          {
            "title": "Feature 14 IEEE CIRCUITS AND SYSTEMS MAGAZINE FOURTH QUARTER 2025",
            "url": "https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_Embodied%20AI%20from%20LLMs%20to%20World%20Models.pdf"
          },
          {
            "title": "Assessing World Models: Methods and Metrics for Evaluating Understanding",
            "url": "https://icml.cc/virtual/2025/workshop/39967"
          },
          {
            "title": "ICML 2025 Papers",
            "url": "https://icml.cc/virtual/2025/papers.html"
          }
        ]
      },
      "Based on the search results, here's information about TAWM (Time-Aware World Model) by Nhu et al. at ICML 2025:\n\n## Overview\n\nTime-Aware World Model (TAWM) is a model-agnostic and more efficient training method for world models, presented by Anh N. Nhu, Sanghyun Son, and Ming C. Lin from the University of Maryland at the International Conference on Machine Learning (ICML) 2025.\n\n## Core Approach\n\nTAWM is a model-based approach that explicitly incorporates temporal dynamics by conditioning on the time-step size (Δt) and training over a diverse range of Δt values, rather than sampling at a fixed time-step, which allows it to learn both high- and low-frequency task dynamics across diverse control problems.\n\n## Key Innovation\n\nGrounded in the information-theoretic insight that the optimal sampling rate depends on a system's underlying dynamics, this time-aware formulation improves both performance and data efficiency.\n\n## Results\n\nEmpirical evaluations show that TAWM consistently outperforms conventional models across varying observation rates in a variety of control tasks, using the same number of training samples and iterations.\n\n## Implementation\n\nTAWM is built on top of TD-MPC2 world model architecture as the basis of the experiments, though TAWM's core contribution is the time-aware training method, which is architecture-agnostic and can be incorporated into any world model training pipeline.\n\nThe code can be found online at github.com/anh-nn01/Time-Aware-World-Model."
    ],
    "durationSeconds": 7.322112251999999
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T13:58:44.128Z_

<details><summary>↩ Tool result · `toolu_01NkN8CFfNcihCpB9Dq6GXg3`</summary>

```text
Web search results for query: "DreamerV3 variant improvement modification 2024 2025"

Links: [{"title":"GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub","url":"https://github.com/danijar/dreamerv3"},{"title":"Mastering Diverse Control Tasks through World Models","url":"https://danijar.com/project/dreamerv3/"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"DreamerV3: Robust Latent Model-Based RL","url":"https://www.emergentmind.com/topics/dreamerv3"},{"title":"Extended Abstract - CS 224R Deep Reinforcement Learning","url":"https://cs224r.stanford.edu/projects/pdfs/Set_Dreamer_CS224R_Final_Project.pdf"},{"title":"RLJ | RLC 2024 Dreaming of Many Worlds: Learning Contextual","url":"https://rlj.cs.umass.edu/2024/papers/RLJ_RLC_2024_167.pdf"},{"title":"DreamerV3-style MBRL Agent","url":"https://www.emergentmind.com/topics/dreamerv3-style-mbrl-agent"},{"title":"DreamerV3-XP: Optimizing exploration through uncertainty estimation","url":"https://arxiv.org/html/2510.21418v1"},{"title":"HarmonyDream: Task Harmonization Inside World Models","url":"https://ise.thss.tsinghua.edu.cn/~mlong/doc/HarmonyDream-icml24.pdf"},{"title":"Mastering Diverse Domains through World Models","url":"https://arxiv.org/pdf/2301.04104"}]

Based on the search results, here are the key DreamerV3 variants and improvements from 2024-2025:

## Core DreamerV3 Improvements

DreamerV3 introduced several key improvements including robustness techniques (observation symlog, KL balance with free bits, 1% unimix for categoricals, percentile return normalization, symexp two-hot loss), network architecture changes (block GRU, RMSNorm normalization, SiLU activation), optimizer improvements (adaptive gradient clipping, LaProp), and replay buffer enhancements (larger capacity, online queue, storing and updating latent states).

## Notable Variants and Extensions (2024-2025)

**Exploration Enhancements:**
DreamerV3-XP injects prioritized trajectory replay and ensemble-based intrinsic reward for exploration, reducing model losses and accelerating learning in sparse-reward settings.

**Contrastive Learning:**
Curled-Dreamer appends a CURL-inspired InfoNCE contrastive loss to the representation, producing more robust vision encodings and increasing median DMC suite performance relative to standard DreamerV3.

**Reconstruction-Free Variants:**
MuDreamer removes pixel reconstruction loss, enforcing predictive learning on values and actions, yielding robustness against visual distractions.

**Context-Aware Learning:**
Researchers proposed an improved Dreamer variant that integrates context more intelligently and demonstrates improved generalization abilities, including a novel approach for conditioning the Dreamer architecture on context that improves zero-shot generalization ability.

**Task Harmonization:**
HarmonyDream either matches or surpasses DreamerV3 in 23 of 26 tested environments and achieves 136.5% of mean human performance on Atari 100K benchmark, setting new state-of-the-art results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "18ad99b3-e333-41a5-8935-41598bfc7c27",
  "tool_use_result": {
    "query": "DreamerV3 variant improvement modification 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YV74EW9D23vWXNtR7mD3uz",
        "content": [
          {
            "title": "GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub",
            "url": "https://github.com/danijar/dreamerv3"
          },
          {
            "title": "Mastering Diverse Control Tasks through World Models",
            "url": "https://danijar.com/project/dreamerv3/"
          },
          {
            "title": "Mastering diverse control tasks through world models - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"
          },
          {
            "title": "DreamerV3: Robust Latent Model-Based RL",
            "url": "https://www.emergentmind.com/topics/dreamerv3"
          },
          {
            "title": "Extended Abstract - CS 224R Deep Reinforcement Learning",
            "url": "https://cs224r.stanford.edu/projects/pdfs/Set_Dreamer_CS224R_Final_Project.pdf"
          },
          {
            "title": "RLJ | RLC 2024 Dreaming of Many Worlds: Learning Contextual",
            "url": "https://rlj.cs.umass.edu/2024/papers/RLJ_RLC_2024_167.pdf"
          },
          {
            "title": "DreamerV3-style MBRL Agent",
            "url": "https://www.emergentmind.com/topics/dreamerv3-style-mbrl-agent"
          },
          {
            "title": "DreamerV3-XP: Optimizing exploration through uncertainty estimation",
            "url": "https://arxiv.org/html/2510.21418v1"
          },
          {
            "title": "HarmonyDream: Task Harmonization Inside World Models",
            "url": "https://ise.thss.tsinghua.edu.cn/~mlong/doc/HarmonyDream-icml24.pdf"
          },
          {
            "title": "Mastering Diverse Domains through World Models",
            "url": "https://arxiv.org/pdf/2301.04104"
          }
        ]
      },
      "Based on the search results, here are the key DreamerV3 variants and improvements from 2024-2025:\n\n## Core DreamerV3 Improvements\n\nDreamerV3 introduced several key improvements including robustness techniques (observation symlog, KL balance with free bits, 1% unimix for categoricals, percentile return normalization, symexp two-hot loss), network architecture changes (block GRU, RMSNorm normalization, SiLU activation), optimizer improvements (adaptive gradient clipping, LaProp), and replay buffer enhancements (larger capacity, online queue, storing and updating latent states).\n\n## Notable Variants and Extensions (2024-2025)\n\n**Exploration Enhancements:**\nDreamerV3-XP injects prioritized trajectory replay and ensemble-based intrinsic reward for exploration, reducing model losses and accelerating learning in sparse-reward settings.\n\n**Contrastive Learning:**\nCurled-Dreamer appends a CURL-inspired InfoNCE contrastive loss to the representation, producing more robust vision encodings and increasing median DMC suite performance relative to standard DreamerV3.\n\n**Reconstruction-Free Variants:**\nMuDreamer removes pixel reconstruction loss, enforcing predictive learning on values and actions, yielding robustness against visual distractions.\n\n**Context-Aware Learning:**\nResearchers proposed an improved Dreamer variant that integrates context more intelligently and demonstrates improved generalization abilities, including a novel approach for conditioning the Dreamer architecture on context that improves zero-shot generalization ability.\n\n**Task Harmonization:**\nHarmonyDream either matches or surpasses DreamerV3 in 23 of 26 tested environments and achieves 136.5% of mean human performance on Atari 100K benchmark, setting new state-of-the-art results."
    ],
    "durationSeconds": 9.090990170999998
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Let me continue with more targeted searches for the remaining directions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "f908332a-5b46-4d47-a782-0cf8b3abaf28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoEhN9UHWgxiZcmc2suyyz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5963,
      "cache_read_input_tokens": 36494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5963
      },
      "output_tokens": 11,
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

_source line 31_

继续搜索更多方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "c970791b-e77f-4c5f-9f67-a47bdac44d83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoEhN9UHWgxiZcmc2suyyz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5963,
      "cache_read_input_tokens": 36494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5963
      },
      "output_tokens": 11,
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

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MwhBDvUTtj36TCJk2RBeVq`</summary>

```json
{
  "query": "delusional bias model-based reinforcement learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "7e3525d0-0b50-4f9d-be7c-c043e9c4bbc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoEhN9UHWgxiZcmc2suyyz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5963,
      "cache_read_input_tokens": 36494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5963
      },
      "output_tokens": 11,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0141izThgjgcdzbtMEXA5zSC`</summary>

```json
{
  "query": "TD-MPC2 temporal abstraction action repetition 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "b3a38454-5f60-4734-bd15-98fd24b902f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoEhN9UHWgxiZcmc2suyyz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5963,
      "cache_read_input_tokens": 36494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5963
      },
      "output_tokens": 11,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FBz4k51QRZZrhi6sjtb4Sw`</summary>

```json
{
  "query": "options framework world model reinforcement learning 2024 2025 ICLR NeurIPS ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "5463bd17-92f5-45d4-91ce-6de98e4e48a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoEhN9UHWgxiZcmc2suyyz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5963,
      "cache_read_input_tokens": 36494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5963
      },
      "output_tokens": 11,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CnzreY4B7ntKpuS7gD3Cso`</summary>

```json
{
  "query": "\"compounding error\" \"world model\" reinforcement learning 2024 2025 rollout"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "c85355dc-3ded-442b-a620-d7ca3b4a8e39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoEhN9UHWgxiZcmc2suyyz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5963,
      "cache_read_input_tokens": 36494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5963
      },
      "output_tokens": 11,
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

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01US1NyKD5Yu66zT6GnU8sej`</summary>

```json
{
  "query": "DreamerV3-XP exploration uncertainty estimation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "754d0ae0-1eb6-4176-a430-94f256f78ae4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoEhN9UHWgxiZcmc2suyyz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5963,
      "cache_read_input_tokens": 36494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5963
      },
      "output_tokens": 11,
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

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GYcctUmFWNFxUApGJ5dT2q`</summary>

```json
{
  "query": "MuDreamer reconstruction-free world model 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "69c36c17-1aec-4f1e-b422-b5ef7d7614c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GoEhN9UHWgxiZcmc2suyyz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5963,
      "cache_read_input_tokens": 36494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5963
      },
      "output_tokens": 11,
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

_source line 38 · 2026-05-18T13:58:55.341Z_

<details><summary>↩ Tool result · `toolu_01MwhBDvUTtj36TCJk2RBeVq`</summary>

```text
Web search results for query: "delusional bias model-based reinforcement learning 2024 2025"

Links: [{"title":"Simulating AI Psychosis, Delusion Reinforcement and ...","url":"https://arxiv.org/pdf/2509.10970"},{"title":"AI 101: The State of Reinforcement Learning in 2025","url":"https://www.turingpost.com/p/stateofrl2025"},{"title":"The State of Reinforcement Learning in 2025 - DataRoot Labs","url":"https://datarootlabs.com/blog/state-of-reinforcement-learning-2025"},{"title":"GitHub - opendilab/awesome-model-based-RL: A curated list of awesome model based RL resources (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-model-based-RL"},{"title":"Reinforcement Learning in 2024: Transforming the Landscape of Generative AI and Large Language Models | by Debu Sinha | Medium","url":"https://medium.com/@debusinha2009/reinforcement-learning-in-2024-transforming-the-landscape-of-generative-ai-and-large-language-fee8b65b1a42"},{"title":"Experimental data-efficient reinforcement learning with an ensemble of surrogate models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0893608025007506"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Handling New Class in Online Label Shift - Peng Zhao","url":"https://www.pengzhao-ml.com/publication/TKDE'25_NOLS.pdf"},{"title":"Latest AI Research (Dec 2025): GPT-5, Agents & Trends | IntuitionLabs","url":"https://intuitionlabs.ai/articles/latest-ai-research-trends-2025"},{"title":"Reinforcement Learning Conference 2024","url":"https://rl-conference.cc/2024/papers.html"}]

Based on the web search results, here's what I found regarding delusional bias in model-based reinforcement learning for 2024-2025:

## Model-Based Reinforcement Learning (2024-2025)

Model-based RL incorporates an internal model of the environment, enabling agents to plan and simulate outcomes before acting. Recent research in 2024-2025 has focused on addressing modeling errors and biases in these systems.

### Model Bias and Error Issues

A significant concern in model-based RL is model error. Modeling errors can undermine training, leading to failures when applied to the actual environment, especially due to discrepancies in the learned dynamics.

One recent approach to address this problem involves proposing a new ensemble of double surrogate models created using symbolic regression to uncover the fundamental physical principles governing system behavior, with the structure of the double surrogate models mitigating model bias, preventing agents from exploiting inaccuracies in the environment that could lead to poor performance.

### Recent Research Activity

Major conferences including NeurIPS 2025, ICML 2025, ICLR 2025, and NeurIPS 2024 have updated their paper lists with model-based RL research.

However, my search results did not specifically identify a research area called "delusional bias" in the context of model-based reinforcement learning. If you're looking for more specific information about this concept, you may want to search for particular papers or authors working on this topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "8bd51b62-31f0-4c2e-87bc-d150c18f7d6a",
  "tool_use_result": {
    "query": "delusional bias model-based reinforcement learning 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_011XttHf6S6eDm53NjgAJ8pT",
        "content": [
          {
            "title": "Simulating AI Psychosis, Delusion Reinforcement and ...",
            "url": "https://arxiv.org/pdf/2509.10970"
          },
          {
            "title": "AI 101: The State of Reinforcement Learning in 2025",
            "url": "https://www.turingpost.com/p/stateofrl2025"
          },
          {
            "title": "The State of Reinforcement Learning in 2025 - DataRoot Labs",
            "url": "https://datarootlabs.com/blog/state-of-reinforcement-learning-2025"
          },
          {
            "title": "GitHub - opendilab/awesome-model-based-RL: A curated list of awesome model based RL resources (continually updated) · GitHub",
            "url": "https://github.com/opendilab/awesome-model-based-RL"
          },
          {
            "title": "Reinforcement Learning in 2024: Transforming the Landscape of Generative AI and Large Language Models | by Debu Sinha | Medium",
            "url": "https://medium.com/@debusinha2009/reinforcement-learning-in-2024-transforming-the-landscape-of-generative-ai-and-large-language-fee8b65b1a42"
          },
          {
            "title": "Experimental data-efficient reinforcement learning with an ensemble of surrogate models - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0893608025007506"
          },
          {
            "title": "ICLR 2025 Papers",
            "url": "https://iclr.cc/virtual/2025/papers.html"
          },
          {
            "title": "Handling New Class in Online Label Shift - Peng Zhao",
            "url": "https://www.pengzhao-ml.com/publication/TKDE'25_NOLS.pdf"
          },
          {
            "title": "Latest AI Research (Dec 2025): GPT-5, Agents & Trends | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/latest-ai-research-trends-2025"
          },
          {
            "title": "Reinforcement Learning Conference 2024",
            "url": "https://rl-conference.cc/2024/papers.html"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding delusional bias in model-based reinforcement learning for 2024-2025:\n\n## Model-Based Reinforcement Learning (2024-2025)\n\nModel-based RL incorporates an internal model of the environment, enabling agents to plan and simulate outcomes before acting. Recent research in 2024-2025 has focused on addressing modeling errors and biases in these systems.\n\n### Model Bias and Error Issues\n\nA significant concern in model-based RL is model error. Modeling errors can undermine training, leading to failures when applied to the actual environment, especially due to discrepancies in the learned dynamics.\n\nOne recent approach to address this problem involves proposing a new ensemble of double surrogate models created using symbolic regression to uncover the fundamental physical principles governing system behavior, with the structure of the double surrogate models mitigating model bias, preventing agents from exploiting inaccuracies in the environment that could lead to poor performance.\n\n### Recent Research Activity\n\nMajor conferences including NeurIPS 2025, ICML 2025, ICLR 2025, and NeurIPS 2024 have updated their paper lists with model-based RL research.\n\nHowever, my search results did not specifically identify a research area called \"delusional bias\" in the context of model-based reinforcement learning. If you're looking for more specific information about this concept, you may want to search for particular papers or authors working on this topic."
    ],
    "durationSeconds": 6.507165846999997
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-18T13:58:56.411Z_

<details><summary>↩ Tool result · `toolu_0141izThgjgcdzbtMEXA5zSC`</summary>

```text
Web search results for query: "TD-MPC2 temporal abstraction action repetition 2024 2025"

Links: [{"title":"TD-MPC2","url":"https://www.tdmpc2.com/"},{"title":"GitHub - nicklashansen/tdmpc2: Code for \"TD-MPC2: Scalable, Robust World Models for Continuous Control\" · GitHub","url":"https://github.com/nicklashansen/tdmpc2"},{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Temporal Difference MPC","url":"https://www.emergentmind.com/topics/temporal-difference-model-predictive-control-td-mpc"},{"title":"[2310.16828] TD-MPC2: Scalable, Robust World Models for Continuous Control","url":"https://arxiv.org/abs/2310.16828"},{"title":"Improving Temporal Difference MPC Through Policy Constraint","url":"https://darthutopian.github.io/tdmpc_square/"},{"title":"[2502.03550] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint","url":"https://arxiv.org/abs/2502.03550"},{"title":"TD-MPC: Temporal Difference for Control","url":"https://www.emergentmind.com/topics/temporal-difference-learning-for-model-predictive-control-td-mpc"},{"title":"TD-MPC2: Scalable, Robust World Models for Continuous Control TD-MPC2","url":"https://iclr.cc/media/iclr-2024/Slides/18722.pdf"},{"title":"TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint","url":"https://darthutopian.github.io/tdmpc_square/static/pdfs/paper.pdf"}]

I found several relevant results about TD-MPC2 and related temporal abstraction and action repetition concepts. Here's what the search revealed:

## TD-MPC2 Overview

TD-MPC is a model-based reinforcement learning (MBRL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoder-free) world model, with TD-MPC2 presenting a series of improvements upon the TD-MPC algorithm. TD-MPC2 compares favorably to existing model-free and model-based methods across 104 continuous control tasks spanning multiple domains, with a single set of hyperparameters.

## Recent Developments (2024-2025)

TD-MPC2 was published at the International Conference on Learning Representations (ICLR) in 2024.

### Temporal Abstraction with Skills

Recent work in 2025 has explored temporal abstraction concepts related to TD-MPC2. Research has modified TD-MPC2 to keep track of skill-related variables when rolling out its model. Work has proposed learning temporally extended skills alongside an abstract world model that predicts skill outcomes.

### Policy Improvements (2025)

Recent work titled "TD-M(PC)²: Improving Temporal Difference MPC Through Policy Constraint" (2025) addresses value overestimation through policy regularization. This approach improves performance over TD-MPC2 baselines by large margins, particularly in 61-DoF humanoid tasks.

The search results show active research on TD-MPC2 with focus on hierarchical abstractions, skill learning, and policy constraints during 2024-2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "dcc4b87d-557f-4102-b0c5-52b00450ade1",
  "tool_use_result": {
    "query": "TD-MPC2 temporal abstraction action repetition 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fr3X9SwCtpz8989RADMcKp",
        "content": [
          {
            "title": "TD-MPC2",
            "url": "https://www.tdmpc2.com/"
          },
          {
            "title": "GitHub - nicklashansen/tdmpc2: Code for \"TD-MPC2: Scalable, Robust World Models for Continuous Control\" · GitHub",
            "url": "https://github.com/nicklashansen/tdmpc2"
          },
          {
            "title": "Reinforcement Learning Journal 2025 Cover Page",
            "url": "https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"
          },
          {
            "title": "Temporal Difference MPC",
            "url": "https://www.emergentmind.com/topics/temporal-difference-model-predictive-control-td-mpc"
          },
          {
            "title": "[2310.16828] TD-MPC2: Scalable, Robust World Models for Continuous Control",
            "url": "https://arxiv.org/abs/2310.16828"
          },
          {
            "title": "Improving Temporal Difference MPC Through Policy Constraint",
            "url": "https://darthutopian.github.io/tdmpc_square/"
          },
          {
            "title": "[2502.03550] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint",
            "url": "https://arxiv.org/abs/2502.03550"
          },
          {
            "title": "TD-MPC: Temporal Difference for Control",
            "url": "https://www.emergentmind.com/topics/temporal-difference-learning-for-model-predictive-control-td-mpc"
          },
          {
            "title": "TD-MPC2: Scalable, Robust World Models for Continuous Control TD-MPC2",
            "url": "https://iclr.cc/media/iclr-2024/Slides/18722.pdf"
          },
          {
            "title": "TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint",
            "url": "https://darthutopian.github.io/tdmpc_square/static/pdfs/paper.pdf"
          }
        ]
      },
      "I found several relevant results about TD-MPC2 and related temporal abstraction and action repetition concepts. Here's what the search revealed:\n\n## TD-MPC2 Overview\n\nTD-MPC is a model-based reinforcement learning (MBRL) algorithm that performs local trajectory optimization in the latent space of a learned implicit (decoder-free) world model, with TD-MPC2 presenting a series of improvements upon the TD-MPC algorithm. TD-MPC2 compares favorably to existing model-free and model-based methods across 104 continuous control tasks spanning multiple domains, with a single set of hyperparameters.\n\n## Recent Developments (2024-2025)\n\nTD-MPC2 was published at the International Conference on Learning Representations (ICLR) in 2024.\n\n### Temporal Abstraction with Skills\n\nRecent work in 2025 has explored temporal abstraction concepts related to TD-MPC2. Research has modified TD-MPC2 to keep track of skill-related variables when rolling out its model. Work has proposed learning temporally extended skills alongside an abstract world model that predicts skill outcomes.\n\n### Policy Improvements (2025)\n\nRecent work titled \"TD-M(PC)²: Improving Temporal Difference MPC Through Policy Constraint\" (2025) addresses value overestimation through policy regularization. This approach improves performance over TD-MPC2 baselines by large margins, particularly in 61-DoF humanoid tasks.\n\nThe search results show active research on TD-MPC2 with focus on hierarchical abstractions, skill learning, and policy constraints during 2024-2025."
    ],
    "durationSeconds": 7.262576136999996
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T13:58:57.413Z_

<details><summary>↩ Tool result · `toolu_01US1NyKD5Yu66zT6GnU8sej`</summary>

```text
Web search results for query: "DreamerV3-XP exploration uncertainty estimation 2025"

Links: [{"title":"[2510.21418] DreamerV3-XP: Optimizing exploration through uncertainty estimation","url":"https://arxiv.org/abs/2510.21418"},{"title":"DreamerV3-XP: Optimizing exploration through uncertainty estimation","url":"https://arxiv.org/html/2510.21418v1"},{"title":"DreamerV3-XP: Optimizing exploration through uncertainty estimation | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2510.21418"},{"title":"(PDF) DreamerV3-XP: Optimizing exploration through uncertainty estimation","url":"https://www.researchgate.net/publication/396924103_DreamerV3-XP_Optimizing_exploration_through_uncertainty_estimation"},{"title":"DreamerV3: Robust Latent Model-Based RL","url":"https://www.emergentmind.com/topics/dreamerv3"},{"title":"(PDF) Exploiting Model Errors for Exploration in Model-Based Reinforcement Learning","url":"https://www.researchgate.net/publication/395384561_Exploiting_Model_Errors_for_Exploration_in_Model-Based_Reinforcement_Learning"},{"title":"Mueed Mohammed's Post","url":"https://www.linkedin.com/posts/mueed-mohammed_ai-machinelearning-dreamerv3-activity-7264338975278997504-6hPa"},{"title":"GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub","url":"https://github.com/LMD0311/Awesome-World-Model"},{"title":"DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12510832/"},{"title":"GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub","url":"https://github.com/danijar/dreamerv3"}]

Based on the search results, here's what I found about DreamerV3-XP:

## Overview

DreamerV3-XP is an extension of DreamerV3 that improves exploration and learning efficiency. It optimizes exploration through uncertainty estimation.

## Key Components

DreamerV3-XP includes (i) a prioritized replay buffer, scoring trajectories by return, reconstruction loss, and value error and (ii) an intrinsic reward based on disagreement over predicted environment rewards from an ensemble of world models.

More specifically, it introduces an intrinsic reward obtained using the variance among reward predictions from an ensemble of world models as a proxy for uncertainty.

## Performance Results

DreamerV3-XP was evaluated on a subset of Atari100k and DeepMind Control Visual Benchmark tasks, confirming the original DreamerV3 results and showing that the extensions lead to faster learning and lower dynamics model loss, particularly in sparse-reward settings.

Prioritized replay consistently reduced dynamics loss, confirming the hypothesis that prioritizing trajectories based on reconstruction error, value error, and return improves model learning by helping the agent focus on parts of the experience buffer that are both informative and underexplored.

The paper was published on arXiv on October 24, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "93a2b78f-c4c5-40ed-ad51-45fc02780c18",
  "tool_use_result": {
    "query": "DreamerV3-XP exploration uncertainty estimation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WmnYTkQrFeVeeaLZN1sHgB",
        "content": [
          {
            "title": "[2510.21418] DreamerV3-XP: Optimizing exploration through uncertainty estimation",
            "url": "https://arxiv.org/abs/2510.21418"
          },
          {
            "title": "DreamerV3-XP: Optimizing exploration through uncertainty estimation",
            "url": "https://arxiv.org/html/2510.21418v1"
          },
          {
            "title": "DreamerV3-XP: Optimizing exploration through uncertainty estimation | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2510.21418"
          },
          {
            "title": "(PDF) DreamerV3-XP: Optimizing exploration through uncertainty estimation",
            "url": "https://www.researchgate.net/publication/396924103_DreamerV3-XP_Optimizing_exploration_through_uncertainty_estimation"
          },
          {
            "title": "DreamerV3: Robust Latent Model-Based RL",
            "url": "https://www.emergentmind.com/topics/dreamerv3"
          },
          {
            "title": "(PDF) Exploiting Model Errors for Exploration in Model-Based Reinforcement Learning",
            "url": "https://www.researchgate.net/publication/395384561_Exploiting_Model_Errors_for_Exploration_in_Model-Based_Reinforcement_Learning"
          },
          {
            "title": "Mueed Mohammed's Post",
            "url": "https://www.linkedin.com/posts/mueed-mohammed_ai-machinelearning-dreamerv3-activity-7264338975278997504-6hPa"
          },
          {
            "title": "GitHub - LMD0311/Awesome-World-Model: Collect some World Models for Autonomous Driving (and Robotic, etc.) papers. · GitHub",
            "url": "https://github.com/LMD0311/Awesome-World-Model"
          },
          {
            "title": "DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12510832/"
          },
          {
            "title": "GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub",
            "url": "https://github.com/danijar/dreamerv3"
          }
        ]
      },
      "Based on the search results, here's what I found about DreamerV3-XP:\n\n## Overview\n\nDreamerV3-XP is an extension of DreamerV3 that improves exploration and learning efficiency. It optimizes exploration through uncertainty estimation.\n\n## Key Components\n\nDreamerV3-XP includes (i) a prioritized replay buffer, scoring trajectories by return, reconstruction loss, and value error and (ii) an intrinsic reward based on disagreement over predicted environment rewards from an ensemble of world models.\n\nMore specifically, it introduces an intrinsic reward obtained using the variance among reward predictions from an ensemble of world models as a proxy for uncertainty.\n\n## Performance Results\n\nDreamerV3-XP was evaluated on a subset of Atari100k and DeepMind Control Visual Benchmark tasks, confirming the original DreamerV3 results and showing that the extensions lead to faster learning and lower dynamics model loss, particularly in sparse-reward settings.\n\nPrioritized replay consistently reduced dynamics loss, confirming the hypothesis that prioritizing trajectories based on reconstruction error, value error, and return improves model learning by helping the agent focus on parts of the experience buffer that are both informative and underexplored.\n\nThe paper was published on arXiv on October 24, 2025."
    ],
    "durationSeconds": 6.2701336920000035
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-18T13:58:57.996Z_

<details><summary>↩ Tool result · `toolu_01FBz4k51QRZZrhi6sjtb4Sw`</summary>

```text
Web search results for query: "options framework world model reinforcement learning 2024 2025 ICLR NeurIPS ICML"

Links: [{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"GitHub - DmitryRyumin/ICML-2025-Papers: ICML 2025 Papers: Dive into cutting-edge research from the premier machine learning conference. Stay current with breakthroughs in deep learning, generative AI, optimization, reinforcement learning, and beyond. Code implementations included. ⭐ support the future of machine learning research!","url":"https://github.com/DmitryRyumin/ICML-2025-Papers"},{"title":"GitHub - opendilab/awesome-model-based-RL: A curated list of awesome model based RL resources (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-model-based-RL"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5fc1e662bd63c4a70b95088ba5d08cb8-Paper-Conference.pdf"},{"title":"ICML 2024 Papers","url":"https://icml.cc/virtual/2024/papers.html"},{"title":"ICML 2025 Schedule","url":"https://icml.cc/virtual/2025/calendar"},{"title":"AAAI-26 New Faculty Highlights Program - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/new-faculty-highlights-program/"},{"title":"ICML 2025 Papers","url":"https://icml.cc/virtual/2025/papers.html"},{"title":"ICML Poster Knowledge Retention in Continual Model-Based Reinforcement Learning","url":"https://icml.cc/virtual/2025/poster/45991"},{"title":"Apple Machine Learning Research at ICLR 2025 - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/iclr-2025"}]

I've completed the web search for your query on options framework, world models, and reinforcement learning research at major 2024-2025 conferences. Here are the key findings:

## Search Results Summary

The search returned information about recent reinforcement learning research at ICLR 2025, NeurIPS 2025, and ICML 2025, though the specific "options framework" topic wasn't prominently featured in these initial results.

### Relevant Resources Found:

1. **Model-Based RL Repository**: An "Awesome Model-Based Reinforcement Learning" resource organizes papers by conferences including NeurIPS 2025, ICML 2025, ICLR 2025, and previous years.

2. **World Models Research at ICML 2025**: DRAGO is a novel approach for continual model-based reinforcement learning that improves the incremental development of world models across tasks, comprising Synthetic Experience Rehearsal and Regaining Memories Through Exploration components.

3. **ICML 2025 Schedule**: ICML 2025 includes papers on world models and reinforcement learning topics such as "Time-Aware World Model for Adaptive Prediction and Control" and "Temporal Distance-aware Transition Augmentation for Offline Model-based Reinforcement Learning".

4. **ICLR 2025 Research**: At ICLR 2025, researchers are presenting work exploring the capabilities of LLMs for RL across interactive domains, showing that LLMs' general knowledge can be leveraged for policy learning.

The search results show active research in world models and model-based RL at these top venues in 2024-2025, though you may want to access the conference paper listings directly for more specific papers on the options framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "75c8174e-064b-419a-89bc-0530e60d04bb",
  "tool_use_result": {
    "query": "options framework world model reinforcement learning 2024 2025 ICLR NeurIPS ICML",
    "results": [
      {
        "tool_use_id": "srvtoolu_011PyWnDFbYNDCf1akZ4TEjE",
        "content": [
          {
            "title": "ICLR 2025 Papers",
            "url": "https://iclr.cc/virtual/2025/papers.html"
          },
          {
            "title": "GitHub - DmitryRyumin/ICML-2025-Papers: ICML 2025 Papers: Dive into cutting-edge research from the premier machine learning conference. Stay current with breakthroughs in deep learning, generative AI, optimization, reinforcement learning, and beyond. Code implementations included. ⭐ support the future of machine learning research!",
            "url": "https://github.com/DmitryRyumin/ICML-2025-Papers"
          },
          {
            "title": "GitHub - opendilab/awesome-model-based-RL: A curated list of awesome model based RL resources (continually updated) · GitHub",
            "url": "https://github.com/opendilab/awesome-model-based-RL"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/5fc1e662bd63c4a70b95088ba5d08cb8-Paper-Conference.pdf"
          },
          {
            "title": "ICML 2024 Papers",
            "url": "https://icml.cc/virtual/2024/papers.html"
          },
          {
            "title": "ICML 2025 Schedule",
            "url": "https://icml.cc/virtual/2025/calendar"
          },
          {
            "title": "AAAI-26 New Faculty Highlights Program - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/new-faculty-highlights-program/"
          },
          {
            "title": "ICML 2025 Papers",
            "url": "https://icml.cc/virtual/2025/papers.html"
          },
          {
            "title": "ICML Poster Knowledge Retention in Continual Model-Based Reinforcement Learning",
            "url": "https://icml.cc/virtual/2025/poster/45991"
          },
          {
            "title": "Apple Machine Learning Research at ICLR 2025 - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/research/iclr-2025"
          }
        ]
      },
      "I've completed the web search for your query on options framework, world models, and reinforcement learning research at major 2024-2025 conferences. Here are the key findings:\n\n## Search Results Summary\n\nThe search returned information about recent reinforcement learning research at ICLR 2025, NeurIPS 2025, and ICML 2025, though the specific \"options framework\" topic wasn't prominently featured in these initial results.\n\n### Relevant Resources Found:\n\n1. **Model-Based RL Repository**: An \"Awesome Model-Based Reinforcement Learning\" resource organizes papers by conferences including NeurIPS 2025, ICML 2025, ICLR 2025, and previous years.\n\n2. **World Models Research at ICML 2025**: DRAGO is a novel approach for continual model-based reinforcement learning that improves the incremental development of world models across tasks, comprising Synthetic Experience Rehearsal and Regaining Memories Through Exploration components.\n\n3. **ICML 2025 Schedule**: ICML 2025 includes papers on world models and reinforcement learning topics such as \"Time-Aware World Model for Adaptive Prediction and Control\" and \"Temporal Distance-aware Transition Augmentation for Offline Model-based Reinforcement Learning\".\n\n4. **ICLR 2025 Research**: At ICLR 2025, researchers are presenting work exploring the capabilities of LLMs for RL across interactive domains, showing that LLMs' general knowledge can be leveraged for policy learning.\n\nThe search results show active research in world models and model-based RL at these top venues in 2024-2025, though you may want to access the conference paper listings directly for more specific papers on the options framework."
    ],
    "durationSeconds": 7.853258626999995
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T13:58:58.533Z_

<details><summary>↩ Tool result · `toolu_01GYcctUmFWNFxUApGJ5dT2q`</summary>

```text
Web search results for query: "MuDreamer reconstruction-free world model 2024"

Links: [{"title":"MuDreamer: Learning Predictive World Models without Reconstruction | OpenReview","url":"https://openreview.net/forum?id=9pe38WpsbX"},{"title":"[2405.15083] MuDreamer: Learning Predictive World Models without Reconstruction","url":"https://arxiv.org/abs/2405.15083"},{"title":"(PDF) MuDreamer: Learning Predictive World Models without Reconstruction","url":"https://www.researchgate.net/publication/380894388_MuDreamer_Learning_Predictive_World_Models_without_Reconstruction"},{"title":"MuDreamer: Learning Predictive World Models without Reconstruction","url":"https://arxiv.org/html/2405.15083v1"},{"title":"MUDREAMER: LEARNING PREDICTIVE WORLD ...","url":"https://openreview.net/pdf/8801375407fde3d9751dbb78c2f906238f519a12.pdf"},{"title":"[Literature Review] MuDreamer: Learning Predictive World Models without Reconstruction","url":"https://www.themoonlight.io/en/review/mudreamer-learning-predictive-world-models-without-reconstruction"},{"title":"MuDreamer: Learning Predictive World Mod...","url":"https://axi.lims.ac.uk/paper/2405.15083"},{"title":"DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning","url":"https://proceedings.mlr.press/v162/deng22a/deng22a.pdf"},{"title":"Learning Predictive World Models without Reconstruction","url":"https://www.semanticscholar.org/paper/MuDreamer:-Learning-Predictive-World-Models-without-Burchi-Timofte/c1657ff831dccf187a109ebee73c45a915080156"},{"title":"Learning Predictive World Models without Reconstruction","url":"https://www.connectedpapers.com/main/c1657ff831dccf187a109ebee73c45a915080156/MuDreamer:-Learning-Predictive-World-Models-without-Reconstruction/graph"}]

Based on the search results, here's what I found about MuDreamer:

## Overview

MuDreamer is a robust reinforcement learning agent that builds upon the DreamerV3 algorithm by learning a predictive world model without the need for reconstructing input signals, instead learning hidden representations by predicting the environment value function and previously selected actions.

## Key Motivation

The DreamerV3 agent demonstrated state-of-the-art performance across diverse domains using a pixel reconstruction loss, however while the reconstruction loss is essential for Dreamer's performance, it also necessitates modeling unnecessary information. Dreamer sometimes fails to perceive crucial elements which are necessary for task-solving when visual distractions are present in the observation.

## Technical Approach

MuDreamer learns a world model in latent space by predicting not only rewards and continuation flags but also the environment value function and previously selected actions. The use of batch normalization is crucial to prevent learning collapse.

## Performance Results

MuDreamer demonstrates stronger robustness to visual distractions compared to DreamerV3 and other reconstruction-free approaches, replacing the environment background with task-irrelevant real-world videos. The method achieves comparable performance on the Atari100k benchmark while benefiting from faster training.

The paper was authored by Maxime Burchi and Radu Timofte and became available on arXiv on May 23, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "0420c7b3-b48c-456a-bd15-164acb6e8a19",
  "tool_use_result": {
    "query": "MuDreamer reconstruction-free world model 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RTdsATnBKtGKwPi6XrPZsG",
        "content": [
          {
            "title": "MuDreamer: Learning Predictive World Models without Reconstruction | OpenReview",
            "url": "https://openreview.net/forum?id=9pe38WpsbX"
          },
          {
            "title": "[2405.15083] MuDreamer: Learning Predictive World Models without Reconstruction",
            "url": "https://arxiv.org/abs/2405.15083"
          },
          {
            "title": "(PDF) MuDreamer: Learning Predictive World Models without Reconstruction",
            "url": "https://www.researchgate.net/publication/380894388_MuDreamer_Learning_Predictive_World_Models_without_Reconstruction"
          },
          {
            "title": "MuDreamer: Learning Predictive World Models without Reconstruction",
            "url": "https://arxiv.org/html/2405.15083v1"
          },
          {
            "title": "MUDREAMER: LEARNING PREDICTIVE WORLD ...",
            "url": "https://openreview.net/pdf/8801375407fde3d9751dbb78c2f906238f519a12.pdf"
          },
          {
            "title": "[Literature Review] MuDreamer: Learning Predictive World Models without Reconstruction",
            "url": "https://www.themoonlight.io/en/review/mudreamer-learning-predictive-world-models-without-reconstruction"
          },
          {
            "title": "MuDreamer: Learning Predictive World Mod...",
            "url": "https://axi.lims.ac.uk/paper/2405.15083"
          },
          {
            "title": "DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning",
            "url": "https://proceedings.mlr.press/v162/deng22a/deng22a.pdf"
          },
          {
            "title": "Learning Predictive World Models without Reconstruction",
            "url": "https://www.semanticscholar.org/paper/MuDreamer:-Learning-Predictive-World-Models-without-Burchi-Timofte/c1657ff831dccf187a109ebee73c45a915080156"
          },
          {
            "title": "Learning Predictive World Models without Reconstruction",
            "url": "https://www.connectedpapers.com/main/c1657ff831dccf187a109ebee73c45a915080156/MuDreamer:-Learning-Predictive-World-Models-without-Reconstruction/graph"
          }
        ]
      },
      "Based on the search results, here's what I found about MuDreamer:\n\n## Overview\n\nMuDreamer is a robust reinforcement learning agent that builds upon the DreamerV3 algorithm by learning a predictive world model without the need for reconstructing input signals, instead learning hidden representations by predicting the environment value function and previously selected actions.\n\n## Key Motivation\n\nThe DreamerV3 agent demonstrated state-of-the-art performance across diverse domains using a pixel reconstruction loss, however while the reconstruction loss is essential for Dreamer's performance, it also necessitates modeling unnecessary information. Dreamer sometimes fails to perceive crucial elements which are necessary for task-solving when visual distractions are present in the observation.\n\n## Technical Approach\n\nMuDreamer learns a world model in latent space by predicting not only rewards and continuation flags but also the environment value function and previously selected actions. The use of batch normalization is crucial to prevent learning collapse.\n\n## Performance Results\n\nMuDreamer demonstrates stronger robustness to visual distractions compared to DreamerV3 and other reconstruction-free approaches, replacing the environment background with task-irrelevant real-world videos. The method achieves comparable performance on the Atari100k benchmark while benefiting from faster training.\n\nThe paper was authored by Maxime Burchi and Radu Timofte and became available on arXiv on May 23, 2024."
    ],
    "durationSeconds": 6.9741963390000015
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-18T13:59:01.149Z_

<details><summary>↩ Tool result · `toolu_01CnzreY4B7ntKpuS7gD3Cso`</summary>

```text
Web search results for query: ""compounding error" "world model" reinforcement learning 2024 2025 rollout"

Links: [{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Robotic World Model","url":"https://sites.google.com/view/roboticworldmodel"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://ntumars.github.io/wm-robot-survey/"},{"title":"[Literature Review] Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning","url":"https://www.themoonlight.io/en/review/diffusion-world-model-future-modeling-beyond-step-by-step-rollout-for-offline-reinforcement-learning"},{"title":"Model-Based Reinforcement Learning","url":"https://www.emergentmind.com/topics/model-based-reinforcement-learning"},{"title":"A unified objective for dynamics model and policy learning ...","url":"https://www.eurekalert.org/news-releases/1056672"},{"title":"The World Model Inflection: 2025 Made It Real | by Graison Thomas | Dec, 2025 | Medium","url":"https://medium.com/@graison/the-world-model-inflection-2025-made-it-real-f5a9c31475d4"},{"title":"World Model for Robot Learning: A Comprehensive Survey","url":"https://arxiv.org/html/2605.00080v1"},{"title":"Learning to Combat Compounding-Error in Model-Based Reinforcement Learning","url":"https://webdocs.cs.ualberta.ca/~chenjun/files/drlw_adambrl_full.pdf"},{"title":"Learning to Combat Compounding-Error in Model-Based Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=S1g_S0VYvr"}]

I've found several relevant research results on compounding error in world models for reinforcement learning rollouts. Here's what the search reveals:

## The Compounding Error Problem

Due to compounding model errors, world model-based methods are generally limited to rolling out the model for a small number of time steps, which severely reduces their ability to solve complex tasks that require longer rollout horizons to discover good solutions. Compounding error is the defining failure mode of predictive simulation—a world model can look perfect for 20 frames and still collapse when you try to plan 2,000 steps ahead.

## Recent Approaches (2024-2025)

Several recent methods are addressing this challenge:

1. **Skill-Based Planning**: By modeling the outcome of temporally extended skills instead of the effect of primitive actions, a mutual-information-based skill learning objective ensures predictable, diverse, and task-related behavior, with the resulting skills compensating for perturbations and drifts to enable stable long-horizon planning.

2. **Robotic World Models**: Dual autoregression and multi-step self-supervised training explicitly reduce compounding errors even beyond the training forecast horizon, allowing imagined trajectories to remain robust under noise and support reliable long-horizon policy learning and transfer.

3. **Diffusion-Based Models**: Diffusion World Models use a conditional diffusion model to predict multiple future states and rewards concurrently, with this single-forward-pass prediction aiming to alleviate the compounding errors inherent in recursive, step-by-step predictions.

4. **Unified Objectives**: A novel model-based learning approach unifies the objectives of model learning and policy learning by directly maximizing the policy's performance in the real world through the Model Gradient algorithm, achieving both higher sample efficiency and better performance compared with existing model-based methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "3780dd8c-3fdd-4df8-9d2e-31184f5f8887",
  "tool_use_result": {
    "query": "\"compounding error\" \"world model\" reinforcement learning 2024 2025 rollout",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TGn81WR9eZytuqmB12GCaf",
        "content": [
          {
            "title": "Reinforcement Learning Journal 2025 Cover Page",
            "url": "https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"
          },
          {
            "title": "Robotic World Model",
            "url": "https://sites.google.com/view/roboticworldmodel"
          },
          {
            "title": "World Model for Robot Learning: A Comprehensive Survey",
            "url": "https://ntumars.github.io/wm-robot-survey/"
          },
          {
            "title": "[Literature Review] Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning",
            "url": "https://www.themoonlight.io/en/review/diffusion-world-model-future-modeling-beyond-step-by-step-rollout-for-offline-reinforcement-learning"
          },
          {
            "title": "Model-Based Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/model-based-reinforcement-learning"
          },
          {
            "title": "A unified objective for dynamics model and policy learning ...",
            "url": "https://www.eurekalert.org/news-releases/1056672"
          },
          {
            "title": "The World Model Inflection: 2025 Made It Real | by Graison Thomas | Dec, 2025 | Medium",
            "url": "https://medium.com/@graison/the-world-model-inflection-2025-made-it-real-f5a9c31475d4"
          },
          {
            "title": "World Model for Robot Learning: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2605.00080v1"
          },
          {
            "title": "Learning to Combat Compounding-Error in Model-Based Reinforcement Learning",
            "url": "https://webdocs.cs.ualberta.ca/~chenjun/files/drlw_adambrl_full.pdf"
          },
          {
            "title": "Learning to Combat Compounding-Error in Model-Based Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=S1g_S0VYvr"
          }
        ]
      },
      "I've found several relevant research results on compounding error in world models for reinforcement learning rollouts. Here's what the search reveals:\n\n## The Compounding Error Problem\n\nDue to compounding model errors, world model-based methods are generally limited to rolling out the model for a small number of time steps, which severely reduces their ability to solve complex tasks that require longer rollout horizons to discover good solutions. Compounding error is the defining failure mode of predictive simulation—a world model can look perfect for 20 frames and still collapse when you try to plan 2,000 steps ahead.\n\n## Recent Approaches (2024-2025)\n\nSeveral recent methods are addressing this challenge:\n\n1. **Skill-Based Planning**: By modeling the outcome of temporally extended skills instead of the effect of primitive actions, a mutual-information-based skill learning objective ensures predictable, diverse, and task-related behavior, with the resulting skills compensating for perturbations and drifts to enable stable long-horizon planning.\n\n2. **Robotic World Models**: Dual autoregression and multi-step self-supervised training explicitly reduce compounding errors even beyond the training forecast horizon, allowing imagined trajectories to remain robust under noise and support reliable long-horizon policy learning and transfer.\n\n3. **Diffusion-Based Models**: Diffusion World Models use a conditional diffusion model to predict multiple future states and rewards concurrently, with this single-forward-pass prediction aiming to alleviate the compounding errors inherent in recursive, step-by-step predictions.\n\n4. **Unified Objectives**: A novel model-based learning approach unifies the objectives of model learning and policy learning by directly maximizing the policy's performance in the real world through the Model Gradient algorithm, achieving both higher sample efficiency and better performance compared with existing model-based methods."
    ],
    "durationSeconds": 10.539117762000002
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Let me continue with a few more targeted searches to cover important recent works.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "e8d85fb7-efe5-4e9b-9ff8-0e8351dfee21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dwW9soPsH9oEmtNbhmWxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1803,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 42457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 45_

继续搜索更多针对性方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "38a909a3-f603-4000-9530-64e80323d8dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dwW9soPsH9oEmtNbhmWxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1803,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 42457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 46_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EZAXcSfwKBuFPwnYX8qEYA`</summary>

```json
{
  "query": "\"TD-M(PC)2\" \"policy constraint\" temporal difference MPC value overestimation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "79fa32e9-5829-4241-98ef-84287dabb792",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dwW9soPsH9oEmtNbhmWxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1803,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 42457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AYQRLKVDhKe3DBhg4vbPEB`</summary>

```json
{
  "query": "Moderate Actor-Critic expectile loss overestimation bias 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "a2a6ea29-72f5-4a21-adcb-71be71d64cc0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dwW9soPsH9oEmtNbhmWxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1803,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 42457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PfgPQFym9d1pMVZUesChPS`</summary>

```json
{
  "query": "\"Critiques of World Models\" 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "2600b583-fbc1-4369-bc41-4b88933178f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dwW9soPsH9oEmtNbhmWxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1803,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 42457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 49_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S7PAjMDWmKaQrGSUf52vSX`</summary>

```json
{
  "query": "plasticity loss deep reinforcement learning 2024 2025 capacity network resets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "013c051e-9dc5-4de3-a0f0-281e5fa4aaaa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dwW9soPsH9oEmtNbhmWxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1803,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 42457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 50_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P4igAWaGCE3e2RyZJ3QJWR`</summary>

```json
{
  "query": "VANTA semantic temporal abstraction vision language model ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "38d784f8-fe83-47c4-a7dc-ebaf8018be19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dwW9soPsH9oEmtNbhmWxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1803,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 42457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 51_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wj8W686ozYYPSiaYNvNoj9`</summary>

```json
{
  "query": "\"adaptive rollout length\" model-based reinforcement learning uncertainty 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "538a3df1-8464-4625-a9d8-fca7d664d813",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dwW9soPsH9oEmtNbhmWxD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1803,
      "cache_creation_input_tokens": 4096,
      "cache_read_input_tokens": 42457,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4096
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

_source line 52 · 2026-05-18T13:59:13.013Z_

<details><summary>↩ Tool result · `toolu_01EZAXcSfwKBuFPwnYX8qEYA`</summary>

```text
Web search results for query: ""TD-M(PC)2" "policy constraint" temporal difference MPC value overestimation 2025"

Links: [{"title":"[2502.03550] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint","url":"https://arxiv.org/abs/2502.03550"},{"title":"TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint","url":"https://arxiv.org/html/2502.03550v1"},{"title":"Improving Temporal Difference MPC Through Policy Constraint","url":"https://darthutopian.github.io/tdmpc_square/"},{"title":"TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint | OpenReview","url":"https://openreview.net/forum?id=ph7BXPU08c"},{"title":"TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint","url":"https://darthutopian.github.io/tdmpc_square/static/pdfs/paper.pdf"},{"title":"[2502.03550v1] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint","url":"http://arxiv.org/abs/2502.03550v1"},{"title":"Guanya Shi ✈️ NeurIPS'25 on X: \"TD-M(PC)^2 (Temporal Difference MPC with Policy Constraints) is a new planner-based MBRL algorithm that achieves SOTA 🚀performance in various benchmarks. We observed and proved the persistent value overestimation problem in planner-based MBRL with learned value/policy priors: https://t.co/qib8xVz6Dk\" / X","url":"https://x.com/GuanyaShi/status/1889143771432112406"},{"title":"[Literature Review] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint","url":"https://www.themoonlight.io/en/review/td-mpc2-improving-temporal-difference-mpc-through-policy-constraint"},{"title":"GitHub - DarthUtopian/tdmpc_square_public: Official repo for paper \"TD-M(PC)^2: Improving Temporal Difference MPC Through Policy Constraint\" · GitHub","url":"https://github.com/DarthUtopian/tdmpc_square_public"},{"title":"Temporal Difference MPC","url":"https://www.emergentmind.com/topics/temporal-difference-model-predictive-control-td-mpc"}]

I found comprehensive information about TD-M(PC)² and the research you're searching for. Here's a summary of the key findings:

## Overview

TD-M(PC)² is a paper titled "Improving Temporal Difference MPC Through Policy Constraint", published in February 2025.

## The Problem: Value Overestimation

Existing methods that rely on standard SAC-style policy iteration for value learning often result in persistent value overestimation, rooted in structural policy mismatch between the data generation policy bootstrapped by the planner and the learned policy prior.

## The Solution

The proposed approach uses a policy regularization term reducing out-of-distribution (OOD) queries to improve value learning. The method involves minimum changes on top of existing frameworks and requires no additional computation.

## Performance Results

The approach improves performance over baselines such as TD-MPC2 by large margins, particularly in 61-DoF humanoid tasks.

## Technical Implementation

The algorithm modifies the policy improvement step to include a distribution constraint (via KL-divergence) that limits the policy updates to actions similar to those observed in the behavior policy.

The paper and official GitHub repository (https://github.com/DarthUtopian/tdmpc_square_public) contain the full implementation details and experimental results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "193262d6-7d34-4e9a-8f78-f4f720cf3053",
  "tool_use_result": {
    "query": "\"TD-M(PC)2\" \"policy constraint\" temporal difference MPC value overestimation 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01K1YASAu8fqGs7RNWo1fJUs",
        "content": [
          {
            "title": "[2502.03550] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint",
            "url": "https://arxiv.org/abs/2502.03550"
          },
          {
            "title": "TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint",
            "url": "https://arxiv.org/html/2502.03550v1"
          },
          {
            "title": "Improving Temporal Difference MPC Through Policy Constraint",
            "url": "https://darthutopian.github.io/tdmpc_square/"
          },
          {
            "title": "TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint | OpenReview",
            "url": "https://openreview.net/forum?id=ph7BXPU08c"
          },
          {
            "title": "TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint",
            "url": "https://darthutopian.github.io/tdmpc_square/static/pdfs/paper.pdf"
          },
          {
            "title": "[2502.03550v1] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint",
            "url": "http://arxiv.org/abs/2502.03550v1"
          },
          {
            "title": "Guanya Shi ✈️ NeurIPS'25 on X: \"TD-M(PC)^2 (Temporal Difference MPC with Policy Constraints) is a new planner-based MBRL algorithm that achieves SOTA 🚀performance in various benchmarks. We observed and proved the persistent value overestimation problem in planner-based MBRL with learned value/policy priors: https://t.co/qib8xVz6Dk\" / X",
            "url": "https://x.com/GuanyaShi/status/1889143771432112406"
          },
          {
            "title": "[Literature Review] TD-M(PC)$^2$: Improving Temporal Difference MPC Through Policy Constraint",
            "url": "https://www.themoonlight.io/en/review/td-mpc2-improving-temporal-difference-mpc-through-policy-constraint"
          },
          {
            "title": "GitHub - DarthUtopian/tdmpc_square_public: Official repo for paper \"TD-M(PC)^2: Improving Temporal Difference MPC Through Policy Constraint\" · GitHub",
            "url": "https://github.com/DarthUtopian/tdmpc_square_public"
          },
          {
            "title": "Temporal Difference MPC",
            "url": "https://www.emergentmind.com/topics/temporal-difference-model-predictive-control-td-mpc"
          }
        ]
      },
      "I found comprehensive information about TD-M(PC)² and the research you're searching for. Here's a summary of the key findings:\n\n## Overview\n\nTD-M(PC)² is a paper titled \"Improving Temporal Difference MPC Through Policy Constraint\", published in February 2025.\n\n## The Problem: Value Overestimation\n\nExisting methods that rely on standard SAC-style policy iteration for value learning often result in persistent value overestimation, rooted in structural policy mismatch between the data generation policy bootstrapped by the planner and the learned policy prior.\n\n## The Solution\n\nThe proposed approach uses a policy regularization term reducing out-of-distribution (OOD) queries to improve value learning. The method involves minimum changes on top of existing frameworks and requires no additional computation.\n\n## Performance Results\n\nThe approach improves performance over baselines such as TD-MPC2 by large margins, particularly in 61-DoF humanoid tasks.\n\n## Technical Implementation\n\nThe algorithm modifies the policy improvement step to include a distribution constraint (via KL-divergence) that limits the policy updates to actions similar to those observed in the behavior policy.\n\nThe paper and official GitHub repository (https://github.com/DarthUtopian/tdmpc_square_public) contain the full implementation details and experimental results."
    ],
    "durationSeconds": 6.47300303
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-18T13:59:13.351Z_

<details><summary>↩ Tool result · `toolu_01PfgPQFym9d1pMVZUesChPS`</summary>

```text
Web search results for query: ""Critiques of World Models" 2025 arxiv"

Links: [{"title":"[2507.05169] Critiques of World Models","url":"https://arxiv.org/abs/2507.05169"},{"title":"Critiques of World Models","url":"https://arxiv.org/pdf/2507.05169"},{"title":"arXiv:2507.05169v1 [cs.LG] 7 Jul 2025 Critiques of World Models","url":"https://arxiv.org/pdf/2507.05169v1"},{"title":"Critiques of World Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250705169X/abstract"},{"title":"Critiques of World Models - ArXivIQ","url":"https://arxiviq.substack.com/p/critiques-of-world-models"},{"title":"Internalizing World Models via Self-Play Finetuning for Agentic RL","url":"https://arxiv.org/html/2510.15047v1"},{"title":"Critiques of World Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/critiques-world-models"},{"title":"(PDF) Critiques of World Models","url":"https://www.researchgate.net/publication/393478311_Critiques_of_World_Models"},{"title":"Robotics Jul 2025","url":"https://www.arxiv.org/list/cs.RO/2025-07?skip=625&show=50"},{"title":"Paper page - Critiques of World Models","url":"https://huggingface.co/papers/2507.05169"}]

I found the paper "Critiques of World Models" from 2025 on arXiv. Here's what I found:

## Paper Overview

The paper addresses world models as algorithmic surrogates of real-world environments that agents experience and act upon, which has become an emerging topic due to rising needs to develop artificial (general) intelligence agents.

## Main Contributions

The authors offer critiques of several schools of thought on world modeling and argue the primary goal of a world model is to simulate all actionable possibilities of the real world for purposeful reasoning and acting.

Building on these critiques, the authors propose a new architecture for a general-purpose world model based on hierarchical, multi-level, and mixed continuous/discrete representations, and a generative and self-supervision learning framework, with an outlook of a Physical, Agentic, and Nested (PAN) AGI system.

## Key Critiques

The paper presents a comprehensive critique of prevailing approaches to building World Models, arguing that the field has become overly focused on high-fidelity video generation. The authors argue that this focus is a distraction from the true purpose of a world model: to serve as a sandbox for purposeful reasoning and acting.

**Paper Details:**
- **arXiv ID:** 2507.05169
- **Submitted:** July 7, 2025 (revised July 27, 2025)
- **Authors:** Eric Xing, Mingkai Deng, Jinyu Hou, Zhiting Hu


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "8fcb4f94-f13d-44bc-95a3-8a61cf660346",
  "tool_use_result": {
    "query": "\"Critiques of World Models\" 2025 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XMbSDrszQGwL9cKFKmyjHX",
        "content": [
          {
            "title": "[2507.05169] Critiques of World Models",
            "url": "https://arxiv.org/abs/2507.05169"
          },
          {
            "title": "Critiques of World Models",
            "url": "https://arxiv.org/pdf/2507.05169"
          },
          {
            "title": "arXiv:2507.05169v1 [cs.LG] 7 Jul 2025 Critiques of World Models",
            "url": "https://arxiv.org/pdf/2507.05169v1"
          },
          {
            "title": "Critiques of World Models - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250705169X/abstract"
          },
          {
            "title": "Critiques of World Models - ArXivIQ",
            "url": "https://arxiviq.substack.com/p/critiques-of-world-models"
          },
          {
            "title": "Internalizing World Models via Self-Play Finetuning for Agentic RL",
            "url": "https://arxiv.org/html/2510.15047v1"
          },
          {
            "title": "Critiques of World Models | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/critiques-world-models"
          },
          {
            "title": "(PDF) Critiques of World Models",
            "url": "https://www.researchgate.net/publication/393478311_Critiques_of_World_Models"
          },
          {
            "title": "Robotics Jul 2025",
            "url": "https://www.arxiv.org/list/cs.RO/2025-07?skip=625&show=50"
          },
          {
            "title": "Paper page - Critiques of World Models",
            "url": "https://huggingface.co/papers/2507.05169"
          }
        ]
      },
      "I found the paper \"Critiques of World Models\" from 2025 on arXiv. Here's what I found:\n\n## Paper Overview\n\nThe paper addresses world models as algorithmic surrogates of real-world environments that agents experience and act upon, which has become an emerging topic due to rising needs to develop artificial (general) intelligence agents.\n\n## Main Contributions\n\nThe authors offer critiques of several schools of thought on world modeling and argue the primary goal of a world model is to simulate all actionable possibilities of the real world for purposeful reasoning and acting.\n\nBuilding on these critiques, the authors propose a new architecture for a general-purpose world model based on hierarchical, multi-level, and mixed continuous/discrete representations, and a generative and self-supervision learning framework, with an outlook of a Physical, Agentic, and Nested (PAN) AGI system.\n\n## Key Critiques\n\nThe paper presents a comprehensive critique of prevailing approaches to building World Models, arguing that the field has become overly focused on high-fidelity video generation. The authors argue that this focus is a distraction from the true purpose of a world model: to serve as a sandbox for purposeful reasoning and acting.\n\n**Paper Details:**\n- **arXiv ID:** 2507.05169\n- **Submitted:** July 7, 2025 (revised July 27, 2025)\n- **Authors:** Eric Xing, Mingkai Deng, Jinyu Hou, Zhiting Hu"
    ],
    "durationSeconds": 5.536150432000002
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-18T13:59:14.519Z_

<details><summary>↩ Tool result · `toolu_01AYQRLKVDhKe3DBhg4vbPEB`</summary>

```text
Web search results for query: "Moderate Actor-Critic expectile loss overestimation bias 2025"

Links: [{"title":"[2504.09929] Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss","url":"https://arxiv.org/abs/2504.09929"},{"title":"Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss","url":"https://arxiv.org/html/2504.09929v1"},{"title":"[Literature Review] Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss","url":"https://www.themoonlight.io/en/review/moderate-actor-critic-methods-controlling-overestimation-bias-via-expectile-loss"},{"title":"Machine Learning Apr 2025","url":"https://www.arxiv.org/list/cs.LG/2025-04?skip=725&show=50"},{"title":"Computer Science Apr 2025","url":"https://www.arxiv.org/list/cs/2025-04?skip=4400&show=2000"},{"title":"Value Improved Actor Critic Algorithms Yaniv Oren","url":"https://arxiv.org/pdf/2406.01423"},{"title":"Value Improved Actor Critic Algorithms","url":"https://arxiv.org/html/2406.1423"},{"title":"A Case for Validation Buffer in Pessimistic Actor-Critic","url":"https://www.ijcai.org/proceedings/2025/0665.pdf"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/html/2403.00514v1"},{"title":"Addressing Function Approximation Error in Actor-Critic Methods","url":"https://proceedings.mlr.press/v80/fujimoto18a/fujimoto18a.pdf"}]

Based on the search results, I found relevant information about "Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss."

## Key Findings

Overestimation is a fundamental characteristic of model-free reinforcement learning (MF-RL), arising from the principles of temporal difference learning and the approximation of the Q-function.

### The Proposed Solution

The paper proposes a novel moderate target in the Q-function update, formulated as a convex optimization of an overestimated Q-function and its lower bound, with the lower bound efficiently estimated through the lower expectile of the Q-value distribution conditioned on a state.

### Key Innovation

Expectile loss (Bellini & Di Bernardino, 2017) is used as a generalization of the classical mean-squared-error (MSE) loss.

### Algorithm Integration and Results

The moderate target integrates seamlessly into state-of-the-art (SOTA) MF-RL algorithms, including Deep Deterministic Policy Gradient (DDPG) and Soft Actor Critic (SAC), with experimental results validating the effectiveness of the moderate target in mitigating overestimation bias in DDPG, SAC, and distributional RL algorithms.

### Implementation

The proposed moderate target is incorporated into Deep Deterministic Policy Gradient (DDPG), Twin-Delayed DDPG (TD3), Soft Actor Critic (SAC), and Truncated Quantile Critics (TQC), establishing Moderate Policy Gradient (MPG) and Moderate Actor Gradient (MAC), and when applied to distributional RL (TQC), resulting in Moderate Quantile Critics (MQC).

The paper was submitted to arXiv on April 14, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "1fb3a27a-3c13-4aeb-96d4-42efa9c0e42e",
  "tool_use_result": {
    "query": "Moderate Actor-Critic expectile loss overestimation bias 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_019nGKx4MLn5DmxruqA7TrrZ",
        "content": [
          {
            "title": "[2504.09929] Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss",
            "url": "https://arxiv.org/abs/2504.09929"
          },
          {
            "title": "Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss",
            "url": "https://arxiv.org/html/2504.09929v1"
          },
          {
            "title": "[Literature Review] Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss",
            "url": "https://www.themoonlight.io/en/review/moderate-actor-critic-methods-controlling-overestimation-bias-via-expectile-loss"
          },
          {
            "title": "Machine Learning Apr 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-04?skip=725&show=50"
          },
          {
            "title": "Computer Science Apr 2025",
            "url": "https://www.arxiv.org/list/cs/2025-04?skip=4400&show=2000"
          },
          {
            "title": "Value Improved Actor Critic Algorithms Yaniv Oren",
            "url": "https://arxiv.org/pdf/2406.01423"
          },
          {
            "title": "Value Improved Actor Critic Algorithms",
            "url": "https://arxiv.org/html/2406.1423"
          },
          {
            "title": "A Case for Validation Buffer in Pessimistic Actor-Critic",
            "url": "https://www.ijcai.org/proceedings/2025/0665.pdf"
          },
          {
            "title": "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning",
            "url": "https://arxiv.org/html/2403.00514v1"
          },
          {
            "title": "Addressing Function Approximation Error in Actor-Critic Methods",
            "url": "https://proceedings.mlr.press/v80/fujimoto18a/fujimoto18a.pdf"
          }
        ]
      },
      "Based on the search results, I found relevant information about \"Moderate Actor-Critic Methods: Controlling Overestimation Bias via Expectile Loss.\"\n\n## Key Findings\n\nOverestimation is a fundamental characteristic of model-free reinforcement learning (MF-RL), arising from the principles of temporal difference learning and the approximation of the Q-function.\n\n### The Proposed Solution\n\nThe paper proposes a novel moderate target in the Q-function update, formulated as a convex optimization of an overestimated Q-function and its lower bound, with the lower bound efficiently estimated through the lower expectile of the Q-value distribution conditioned on a state.\n\n### Key Innovation\n\nExpectile loss (Bellini & Di Bernardino, 2017) is used as a generalization of the classical mean-squared-error (MSE) loss.\n\n### Algorithm Integration and Results\n\nThe moderate target integrates seamlessly into state-of-the-art (SOTA) MF-RL algorithms, including Deep Deterministic Policy Gradient (DDPG) and Soft Actor Critic (SAC), with experimental results validating the effectiveness of the moderate target in mitigating overestimation bias in DDPG, SAC, and distributional RL algorithms.\n\n### Implementation\n\nThe proposed moderate target is incorporated into Deep Deterministic Policy Gradient (DDPG), Twin-Delayed DDPG (TD3), Soft Actor Critic (SAC), and Truncated Quantile Critics (TQC), establishing Moderate Policy Gradient (MPG) and Moderate Actor Gradient (MAC), and when applied to distributional RL (TQC), resulting in Moderate Quantile Critics (MQC).\n\nThe paper was submitted to arXiv on April 14, 2025."
    ],
    "durationSeconds": 7.646470136000003
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-18T13:59:16.527Z_

<details><summary>↩ Tool result · `toolu_01P4igAWaGCE3e2RyZJ3QJWR`</summary>

```text
Web search results for query: "VANTA semantic temporal abstraction vision language model ICLR 2025"

Links: [{"title":"SEMANTIC TEMPORAL ABSTRACTION VIA VISION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7c8c0db90a14c7a2db9475e52dc343a9-Paper-Conference.pdf"},{"title":"ICLR Poster Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning","url":"https://iclr.cc/virtual/2025/poster/27665"},{"title":"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/7c8c0db90a14c7a2db9475e52dc343a9-Abstract-Conference.html"},{"title":"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=zY37C8d6bS"},{"title":"Semantic Temporal Abstraction via Vision-Language ...","url":"https://iclr.cc/media/iclr-2025/Slides/27665_0737VV2.pdf"},{"title":"dblp: Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning.","url":"https://dblp.dagstuhl.de/rec/conf/iclr/LiuL0JWZ025.html"},{"title":"Planning with Reasoning using Vision Language World Model","url":"https://arxiv.org/html/2509.02722v1"},{"title":"Published as a conference paper at ICLR 2025 VLAS: VISION-LANGUAGE-ACTION MODEL","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf"},{"title":"[2510.09586] Vision Language Models: A Survey of 26K Papers","url":"https://arxiv.org/abs/2510.09586"},{"title":"Towards Comprehensive Reasoning in Vision-Language Models | ICCV 2025","url":"https://wangywust.github.io/iccv-tutorial-reasoning-vlm/"}]

I found relevant information about VANTA (Vision-language model guided Temporal Abstraction) from ICLR 2025. Here's what the search revealed:

## Overview

VanTA (Vision-language model guided Temporal Abstraction) facilitates the discovery of more interpretable and task-relevant temporal segmentations from offline data without the need for extensive manual intervention or heuristics.

## Problem It Addresses

Extracting temporally extended skills can significantly improve the efficiency of reinforcement learning (RL) by breaking down complex decision-making problems with sparse rewards into simpler subtasks, however existing abstraction methods either discover skills in an unsupervised manner which often lacks semantic information and leads to scattered skill extraction results, or require substantial human intervention.

## Key Approach

The method leverages the extensive knowledge in pretrained Vision-Language Models (VLMs) to progressively guide the latent space after vector quantization to be more semantically meaningful through relabeling each skill.

## Experimental Validation

The effectiveness of the approach is validated through extensive experiments on diverse environments including Franka Kitchen, Minigrid, and Crafter, with results showing that the method surpasses existing approaches in long-horizon offline reinforcement learning scenarios with both proprioceptive and visual observations.

The paper was authored by Tian-Shuo Liu, Xu-Hui Liu, Ruifeng Chen, Lixuan Jin, Pengyuan Wang, Zhilong Zhang, and Yang Yu.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "9905ab33-635a-46a4-bc37-d61a9fe8e779",
  "tool_use_result": {
    "query": "VANTA semantic temporal abstraction vision language model ICLR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CvoDzXkQFwHJfVx1hMnAQG",
        "content": [
          {
            "title": "SEMANTIC TEMPORAL ABSTRACTION VIA VISION",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/7c8c0db90a14c7a2db9475e52dc343a9-Paper-Conference.pdf"
          },
          {
            "title": "ICLR Poster Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning",
            "url": "https://iclr.cc/virtual/2025/poster/27665"
          },
          {
            "title": "Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/7c8c0db90a14c7a2db9475e52dc343a9-Abstract-Conference.html"
          },
          {
            "title": "Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=zY37C8d6bS"
          },
          {
            "title": "Semantic Temporal Abstraction via Vision-Language ...",
            "url": "https://iclr.cc/media/iclr-2025/Slides/27665_0737VV2.pdf"
          },
          {
            "title": "dblp: Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning.",
            "url": "https://dblp.dagstuhl.de/rec/conf/iclr/LiuL0JWZ025.html"
          },
          {
            "title": "Planning with Reasoning using Vision Language World Model",
            "url": "https://arxiv.org/html/2509.02722v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 VLAS: VISION-LANGUAGE-ACTION MODEL",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf"
          },
          {
            "title": "[2510.09586] Vision Language Models: A Survey of 26K Papers",
            "url": "https://arxiv.org/abs/2510.09586"
          },
          {
            "title": "Towards Comprehensive Reasoning in Vision-Language Models | ICCV 2025",
            "url": "https://wangywust.github.io/iccv-tutorial-reasoning-vlm/"
          }
        ]
      },
      "I found relevant information about VANTA (Vision-language model guided Temporal Abstraction) from ICLR 2025. Here's what the search revealed:\n\n## Overview\n\nVanTA (Vision-language model guided Temporal Abstraction) facilitates the discovery of more interpretable and task-relevant temporal segmentations from offline data without the need for extensive manual intervention or heuristics.\n\n## Problem It Addresses\n\nExtracting temporally extended skills can significantly improve the efficiency of reinforcement learning (RL) by breaking down complex decision-making problems with sparse rewards into simpler subtasks, however existing abstraction methods either discover skills in an unsupervised manner which often lacks semantic information and leads to scattered skill extraction results, or require substantial human intervention.\n\n## Key Approach\n\nThe method leverages the extensive knowledge in pretrained Vision-Language Models (VLMs) to progressively guide the latent space after vector quantization to be more semantically meaningful through relabeling each skill.\n\n## Experimental Validation\n\nThe effectiveness of the approach is validated through extensive experiments on diverse environments including Franka Kitchen, Minigrid, and Crafter, with results showing that the method surpasses existing approaches in long-horizon offline reinforcement learning scenarios with both proprioceptive and visual observations.\n\nThe paper was authored by Tian-Shuo Liu, Xu-Hui Liu, Ruifeng Chen, Lixuan Jin, Pengyuan Wang, Zhilong Zhang, and Yang Yu."
    ],
    "durationSeconds": 7.24357979299999
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-18T13:59:17.556Z_

<details><summary>↩ Tool result · `toolu_01S7PAjMDWmKaQrGSUf52vSX`</summary>

```text
Web search results for query: "plasticity loss deep reinforcement learning 2024 2025 capacity network resets"

Links: [{"title":"Attribution-Based Neuron Utility for Plasticity Restoration in Deep Networks","url":"https://arxiv.org/html/2605.06834"},{"title":"[2411.04832] Plasticity Loss in Deep Reinforcement Learning: A Survey","url":"https://arxiv.org/abs/2411.04832"},{"title":"Loss of plasticity in deep continual learning | Nature","url":"https://www.nature.com/articles/s41586-024-07711-7"},{"title":"Self-Normalized Resets for Plasticity in Continual Learning | OpenReview","url":"https://openreview.net/forum?id=G82uQztzxl"},{"title":"Paper Notes: Loss of Plasticity in Deep Continual Learning – Shawn’s Blog","url":"https://pengxiang-wang.com/posts/paper-notes-loss-of-plasticity-in-deep-continual-learning"},{"title":"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/ce7984e36d58659211a8dc7d5457cd6f-Paper-Conference.pdf"},{"title":"ICML Poster Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn","url":"https://icml.cc/virtual/2025/poster/45929"},{"title":"Loss of plasticity in deep continual learning","url":"https://pubmed.ncbi.nlm.nih.gov/39169245/"},{"title":"[2303.07507] Loss of Plasticity in Continual Deep Reinforcement Learning","url":"https://ar5iv.labs.arxiv.org/html/2303.07507"},{"title":"Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn","url":"https://arxiv.org/html/2506.00592v1"}]

I've completed a web search on plasticity loss in deep reinforcement learning with recent developments from 2024-2025. Here are the key findings:

## Key Concepts and Recent Work

Plasticity refers to a network's ability to adapt to changing data distributions, which is crucial for deep reinforcement learning. Loss of plasticity causes performance plateaus and contributes to scaling failures, overestimation bias, and insufficient exploration.

Standard deep-learning methods gradually lose plasticity in continual-learning settings until they learn no better than a shallow network, as demonstrated using classic datasets like ImageNet and reinforcement-learning problems across various network and learning algorithm variations.

## Network Reset Strategies

Several reset-based interventions have been proposed to address plasticity loss:

Reset-based methods periodically reinitialize parts of the network judged to have low utility, injecting fresh capacity while attempting to preserve the current function.

The continual backpropagation algorithm is exactly like classical backpropagation except that a tiny proportion of less-used units are reinitialized on each step much as they were all initialized at the start of training.

Self-Normalized Resets (SNR) mitigates plasticity loss by resetting a neuron's weights when evidence suggests its firing rate has effectively dropped to zero.

## Recent Mechanistic Understanding (2024-2025)

Prior work has linked plasticity degradation to dormant or saturated units, pre-activation and target-distribution shift, parameter norm growth and reduced effective rank, and loss of useful curvature directions.

Recent research studies plasticity loss through the lens of churn (network output variability induced by training data), demonstrating that plasticity loss is accompanied by exacerbation of churn due to gradual rank decrease of the Neural Tangent Kernel (NTK) matrix.

Methods which best resolve plasticity loss are those which act as continual regularizers, with a soft variant of shrink+perturb combined with LayerNorm performing best across evaluated settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "6246cdd7-2993-493f-816b-411a839e5972",
  "tool_use_result": {
    "query": "plasticity loss deep reinforcement learning 2024 2025 capacity network resets",
    "results": [
      {
        "tool_use_id": "srvtoolu_014weRAoZHBfiBAoT1A5vTyS",
        "content": [
          {
            "title": "Attribution-Based Neuron Utility for Plasticity Restoration in Deep Networks",
            "url": "https://arxiv.org/html/2605.06834"
          },
          {
            "title": "[2411.04832] Plasticity Loss in Deep Reinforcement Learning: A Survey",
            "url": "https://arxiv.org/abs/2411.04832"
          },
          {
            "title": "Loss of plasticity in deep continual learning | Nature",
            "url": "https://www.nature.com/articles/s41586-024-07711-7"
          },
          {
            "title": "Self-Normalized Resets for Plasticity in Continual Learning | OpenReview",
            "url": "https://openreview.net/forum?id=G82uQztzxl"
          },
          {
            "title": "Paper Notes: Loss of Plasticity in Deep Continual Learning – Shawn’s Blog",
            "url": "https://pengxiang-wang.com/posts/paper-notes-loss-of-plasticity-in-deep-continual-learning"
          },
          {
            "title": "A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/ce7984e36d58659211a8dc7d5457cd6f-Paper-Conference.pdf"
          },
          {
            "title": "ICML Poster Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn",
            "url": "https://icml.cc/virtual/2025/poster/45929"
          },
          {
            "title": "Loss of plasticity in deep continual learning",
            "url": "https://pubmed.ncbi.nlm.nih.gov/39169245/"
          },
          {
            "title": "[2303.07507] Loss of Plasticity in Continual Deep Reinforcement Learning",
            "url": "https://ar5iv.labs.arxiv.org/html/2303.07507"
          },
          {
            "title": "Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn",
            "url": "https://arxiv.org/html/2506.00592v1"
          }
        ]
      },
      "I've completed a web search on plasticity loss in deep reinforcement learning with recent developments from 2024-2025. Here are the key findings:\n\n## Key Concepts and Recent Work\n\nPlasticity refers to a network's ability to adapt to changing data distributions, which is crucial for deep reinforcement learning. Loss of plasticity causes performance plateaus and contributes to scaling failures, overestimation bias, and insufficient exploration.\n\nStandard deep-learning methods gradually lose plasticity in continual-learning settings until they learn no better than a shallow network, as demonstrated using classic datasets like ImageNet and reinforcement-learning problems across various network and learning algorithm variations.\n\n## Network Reset Strategies\n\nSeveral reset-based interventions have been proposed to address plasticity loss:\n\nReset-based methods periodically reinitialize parts of the network judged to have low utility, injecting fresh capacity while attempting to preserve the current function.\n\nThe continual backpropagation algorithm is exactly like classical backpropagation except that a tiny proportion of less-used units are reinitialized on each step much as they were all initialized at the start of training.\n\nSelf-Normalized Resets (SNR) mitigates plasticity loss by resetting a neuron's weights when evidence suggests its firing rate has effectively dropped to zero.\n\n## Recent Mechanistic Understanding (2024-2025)\n\nPrior work has linked plasticity degradation to dormant or saturated units, pre-activation and target-distribution shift, parameter norm growth and reduced effective rank, and loss of useful curvature directions.\n\nRecent research studies plasticity loss through the lens of churn (network output variability induced by training data), demonstrating that plasticity loss is accompanied by exacerbation of churn due to gradual rank decrease of the Neural Tangent Kernel (NTK) matrix.\n\nMethods which best resolve plasticity loss are those which act as continual regularizers, with a soft variant of shrink+perturb combined with LayerNorm performing best across evaluated settings."
    ],
    "durationSeconds": 9.268859065000004
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-18T13:59:18.083Z_

<details><summary>↩ Tool result · `toolu_01Wj8W686ozYYPSiaYNvNoj9`</summary>

```text
Web search results for query: ""adaptive rollout length" model-based reinforcement learning uncertainty 2024 2025"

Links: [{"title":"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning","url":"https://arxiv.org/html/2605.02178v1"},{"title":"ON ROLLOUTS IN MODEL-BASED REINFORCEMENT ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/be7a642a92de108a57e4d50866144d73-Paper-Conference.pdf"},{"title":"On Rollouts in Model-Based Reinforcement Learning","url":"https://arxiv.org/html/2501.16918v1"},{"title":"[PDF] Improving model-based RL with Adaptive Rollout using Uncertainty Estimation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Improving-model-based-RL-with-Adaptive-Rollout-Nguyen/cf40c34c1020819ffd7c4696904233a379f57b73"},{"title":"ZERO-SHOT MODEL-BASED REINFORCEMENT LEARN","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5fc1e662bd63c4a70b95088ba5d08cb8-Paper-Conference.pdf"},{"title":"[2501.16918] On Rollouts in Model-Based Reinforcement Learning","url":"https://arxiv.org/abs/2501.16918"},{"title":"Controllable Flow Matching for Online Reinforcement Learning","url":"https://arxiv.org/html/2511.06816v1"},{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Scalable and reliable multi-agent reinforcement learning for traffic assignment - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2772424725000654"},{"title":"Efficient Reinforcement Learning for LLM Reasoning via ...","url":"https://www.arxiv.org/pdf/2506.02177"}]

The search has returned several highly relevant results on adaptive rollout length in model-based reinforcement learning with uncertainty. Here are the key findings:

## Key Papers and Findings

### Infoprop: On Rollouts in Model-Based Reinforcement Learning

Infoprop is a model-based rollout mechanism that separates aleatoric from epistemic model uncertainty and reduces the influence of the latter on the data distribution, while also keeping track of accumulated model errors along a model rollout and providing termination criteria to limit data corruption. The improved predictive distribution and capability to estimate accumulated error of Infoprop allows for substantially longer rollouts up to 100 steps, and the Infoprop termination criteria reliably stop distorted rollouts, resulting in consistent rollouts over long horizons. This work was published in early 2025 and addresses the key challenge of how to adaptively determine rollout length based on model uncertainty.

### Uncertainty-Guided Exploration Control (T2PO)

At the token level, T2PO monitors uncertainty dynamics and triggers a thinking intervention once the marginal uncertainty change falls below a threshold, while at the turn level, T2PO identifies interactions with negligible exploration progress and dynamically resamples such turns to avoid wasted rollouts.

### Related Work: MACURA

Bernd Frauenknecht et al. (2024) published "Trust the model where it trusts itself – model-based actor-critic with uncertainty-aware rollout adaption," which appears to be a foundational work on using model uncertainty for adaptive rollout determination. MACURA uses inherent model uncertainty to consider local accuracy to make rollouts.

These recent works from 2024-2025 demonstrate significant progress in using uncertainty estimates to adaptively control rollout lengths and improve model-based reinforcement learning performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "726b55d2-fd1a-4d1e-88f4-4c6b2334ecbb",
  "tool_use_result": {
    "query": "\"adaptive rollout length\" model-based reinforcement learning uncertainty 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Sx33vxB2AtQ2P652JkWTLL",
        "content": [
          {
            "title": "T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.02178v1"
          },
          {
            "title": "ON ROLLOUTS IN MODEL-BASED REINFORCEMENT ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/be7a642a92de108a57e4d50866144d73-Paper-Conference.pdf"
          },
          {
            "title": "On Rollouts in Model-Based Reinforcement Learning",
            "url": "https://arxiv.org/html/2501.16918v1"
          },
          {
            "title": "[PDF] Improving model-based RL with Adaptive Rollout using Uncertainty Estimation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Improving-model-based-RL-with-Adaptive-Rollout-Nguyen/cf40c34c1020819ffd7c4696904233a379f57b73"
          },
          {
            "title": "ZERO-SHOT MODEL-BASED REINFORCEMENT LEARN",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/5fc1e662bd63c4a70b95088ba5d08cb8-Paper-Conference.pdf"
          },
          {
            "title": "[2501.16918] On Rollouts in Model-Based Reinforcement Learning",
            "url": "https://arxiv.org/abs/2501.16918"
          },
          {
            "title": "Controllable Flow Matching for Online Reinforcement Learning",
            "url": "https://arxiv.org/html/2511.06816v1"
          },
          {
            "title": "Reinforcement Learning Journal 2025 Cover Page",
            "url": "https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"
          },
          {
            "title": "Scalable and reliable multi-agent reinforcement learning for traffic assignment - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S2772424725000654"
          },
          {
            "title": "Efficient Reinforcement Learning for LLM Reasoning via ...",
            "url": "https://www.arxiv.org/pdf/2506.02177"
          }
        ]
      },
      "The search has returned several highly relevant results on adaptive rollout length in model-based reinforcement learning with uncertainty. Here are the key findings:\n\n## Key Papers and Findings\n\n### Infoprop: On Rollouts in Model-Based Reinforcement Learning\n\nInfoprop is a model-based rollout mechanism that separates aleatoric from epistemic model uncertainty and reduces the influence of the latter on the data distribution, while also keeping track of accumulated model errors along a model rollout and providing termination criteria to limit data corruption. The improved predictive distribution and capability to estimate accumulated error of Infoprop allows for substantially longer rollouts up to 100 steps, and the Infoprop termination criteria reliably stop distorted rollouts, resulting in consistent rollouts over long horizons. This work was published in early 2025 and addresses the key challenge of how to adaptively determine rollout length based on model uncertainty.\n\n### Uncertainty-Guided Exploration Control (T2PO)\n\nAt the token level, T2PO monitors uncertainty dynamics and triggers a thinking intervention once the marginal uncertainty change falls below a threshold, while at the turn level, T2PO identifies interactions with negligible exploration progress and dynamically resamples such turns to avoid wasted rollouts.\n\n### Related Work: MACURA\n\nBernd Frauenknecht et al. (2024) published \"Trust the model where it trusts itself – model-based actor-critic with uncertainty-aware rollout adaption,\" which appears to be a foundational work on using model uncertainty for adaptive rollout determination. MACURA uses inherent model uncertainty to consider local accuracy to make rollouts.\n\nThese recent works from 2024-2025 demonstrate significant progress in using uncertainty estimates to adaptively control rollout lengths and improve model-based reinforcement learning performance."
    ],
    "durationSeconds": 8.357002366000009
  }
}
```

</details>

---

### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Let me do a few more targeted searches to ensure completeness, particularly for some important papers I noticed in the search results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "7055dd8b-f863-4c78-adf4-2cd9de45afeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwdrE4yk15V7tdVtQmQk7s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7964,
      "cache_read_input_tokens": 46553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7964
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

_source line 59_

再搜索几个重要方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "b9a3a4a8-53f5-4e57-b059-bbe34e642357",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwdrE4yk15V7tdVtQmQk7s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7964,
      "cache_read_input_tokens": 46553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7964
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

_source line 60_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LpPa8pZ5iLHQWX2uYckhY4`</summary>

```json
{
  "query": "\"overestimation overfitting plasticity actor-critic bitter lesson\" reinforcement learning 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "802a1c6b-f6e5-4718-b82f-e653e0dc50f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwdrE4yk15V7tdVtQmQk7s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7964,
      "cache_read_input_tokens": 46553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7964
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

_source line 61_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011wsRic4hLoUz4DkpVuPBdg`</summary>

```json
{
  "query": "\"Diffusion World Model\" offline reinforcement learning step-by-step rollout 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "84aa6cd1-1f37-413d-9d50-ccee478b9b82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwdrE4yk15V7tdVtQmQk7s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7964,
      "cache_read_input_tokens": 46553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7964
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

_source line 62_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N17Mn2hp43xuG2wmXWDJwn`</summary>

```json
{
  "query": "\"SPlaTES\" stable planning temporally extended skills reinforcement learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "31ec576e-72f2-4343-86bc-e2f4b22620b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwdrE4yk15V7tdVtQmQk7s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7964,
      "cache_read_input_tokens": 46553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7964
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

_source line 63_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KeG791zuuXQQctQ64SxpPa`</summary>

```json
{
  "query": "\"learning world models hierarchical temporal abstractions probabilistic\" 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "000f425f-d2fa-4c69-8376-1fd4005b088e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WwdrE4yk15V7tdVtQmQk7s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7964,
      "cache_read_input_tokens": 46553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7964
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

_source line 64 · 2026-05-18T13:59:30.203Z_

<details><summary>↩ Tool result · `toolu_01LpPa8pZ5iLHQWX2uYckhY4`</summary>

```text
Web search results for query: ""overestimation overfitting plasticity actor-critic bitter lesson" reinforcement learning 2024"

Links: [{"title":"[2403.00514] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/abs/2403.00514"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://proceedings.mlr.press/v235/nauman24a.html"},{"title":"[PDF] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Overestimation,-Overfitting,-and-Plasticity-in-the-Nauman-Bortkiewicz/dcf39ce4ea7c1d073dcd0dbb131a0b90a4bd2977"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=5vZzmCeTYu"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/html/2403.00514v2"},{"title":"[2403.00514v2] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/abs/2403.00514v2"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/overestimation-overfitting-plasticity-actor-critic-bitter-lesson"},{"title":"Overestimation, overfitting, and plasticity in actor-critic | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3693586"},{"title":"ICML Poster Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://icml.cc/virtual/2024/poster/34956"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/zh/overview/2403.00514v2"}]

I found a highly relevant 2024 research paper matching your search query. Here's a summary of the findings:

## "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning"

Recent advancements in off-policy Reinforcement Learning (RL) have significantly improved sample efficiency, primarily due to the incorporation of various forms of regularization that enable more gradient update steps than traditional agents. To address limitations in understanding these mechanisms, researchers implemented over 60 different off-policy agents, each integrating established regularization techniques from recent state-of-the-art algorithms.

### Key Findings

The study tested these agents across 14 diverse tasks from 2 simulation benchmarks, measuring training metrics related to overestimation, overfitting, and plasticity loss. While the effectiveness of a specific regularization setup varies with the task, certain combinations consistently demonstrate robust and superior performance.

Notably, a simple Soft Actor-Critic agent, appropriately regularized, reliably finds a better-performing policy within the training regime, which previously was achieved mainly through model-based approaches.

### The "Bitter Lesson" Insight

The authors discuss the "bitter lesson" that RL researchers have learned - that focusing on fundamental principles and scalable solutions is often more important than trying to engineer complex, specialized algorithms. By understanding and addressing these core challenges, the field of RL can make more meaningful progress towards more robust and capable agents.

The paper was published in the 2024 Proceedings of the 41st International Conference on Machine Learning (ICML) and is available on arXiv and multiple academic platforms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "bcca9c0e-d068-4ae2-86b0-85c2a439adb0",
  "tool_use_result": {
    "query": "\"overestimation overfitting plasticity actor-critic bitter lesson\" reinforcement learning 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ld7t53MsWoLLsEkAUYNvE6",
        "content": [
          {
            "title": "[2403.00514] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning",
            "url": "https://arxiv.org/abs/2403.00514"
          },
          {
            "title": "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning",
            "url": "https://proceedings.mlr.press/v235/nauman24a.html"
          },
          {
            "title": "[PDF] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Overestimation,-Overfitting,-and-Plasticity-in-the-Nauman-Bortkiewicz/dcf39ce4ea7c1d073dcd0dbb131a0b90a4bd2977"
          },
          {
            "title": "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=5vZzmCeTYu"
          },
          {
            "title": "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning",
            "url": "https://arxiv.org/html/2403.00514v2"
          },
          {
            "title": "[2403.00514v2] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning",
            "url": "https://arxiv.org/abs/2403.00514v2"
          },
          {
            "title": "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/overestimation-overfitting-plasticity-actor-critic-bitter-lesson"
          },
          {
            "title": "Overestimation, overfitting, and plasticity in actor-critic | Proceedings of the 41st International Conference on Machine Learning",
            "url": "https://dl.acm.org/doi/10.5555/3692070.3693586"
          },
          {
            "title": "ICML Poster Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning",
            "url": "https://icml.cc/virtual/2024/poster/34956"
          },
          {
            "title": "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | alphaXiv",
            "url": "https://www.alphaxiv.org/zh/overview/2403.00514v2"
          }
        ]
      },
      "I found a highly relevant 2024 research paper matching your search query. Here's a summary of the findings:\n\n## \"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning\"\n\nRecent advancements in off-policy Reinforcement Learning (RL) have significantly improved sample efficiency, primarily due to the incorporation of various forms of regularization that enable more gradient update steps than traditional agents. To address limitations in understanding these mechanisms, researchers implemented over 60 different off-policy agents, each integrating established regularization techniques from recent state-of-the-art algorithms.\n\n### Key Findings\n\nThe study tested these agents across 14 diverse tasks from 2 simulation benchmarks, measuring training metrics related to overestimation, overfitting, and plasticity loss. While the effectiveness of a specific regularization setup varies with the task, certain combinations consistently demonstrate robust and superior performance.\n\nNotably, a simple Soft Actor-Critic agent, appropriately regularized, reliably finds a better-performing policy within the training regime, which previously was achieved mainly through model-based approaches.\n\n### The \"Bitter Lesson\" Insight\n\nThe authors discuss the \"bitter lesson\" that RL researchers have learned - that focusing on fundamental principles and scalable solutions is often more important than trying to engineer complex, specialized algorithms. By understanding and addressing these core challenges, the field of RL can make more meaningful progress towards more robust and capable agents.\n\nThe paper was published in the 2024 Proceedings of the 41st International Conference on Machine Learning (ICML) and is available on arXiv and multiple academic platforms."
    ],
    "durationSeconds": 6.122776146999997
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-18T13:59:31.776Z_

<details><summary>↩ Tool result · `toolu_01N17Mn2hp43xuG2wmXWDJwn`</summary>

```text
Web search results for query: ""SPlaTES" stable planning temporally extended skills reinforcement learning 2025"

Links: [{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Learning Temporally Extended Skills in Continuous Domains as Symbolic Actions for Planning | seads","url":"https://seads.is.tue.mpg.de/"},{"title":"[2207.05018] Learning Temporally Extended Skills in Continuous Domains as Symbolic Actions for Planning","url":"https://arxiv.org/abs/2207.05018"},{"title":"Learning Temporally Extended Skills in Continuous Domains as Symbolic Actions for Planning | OpenReview","url":"https://openreview.net/forum?id=t-IO7wCaNgH"},{"title":"Temporally extended successor feature neural episodic control | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-65687-w"},{"title":"LLMs augmented hierarchical reinforcement learning with action primitives for long-horizon manipulation tasks | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-20653-y"},{"title":"Multi-Turn Reinforcement Learning","url":"https://www.emergentmind.com/topics/multi-turn-reinforcement-learning-mt-rl"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/7c8c0db90a14c7a2db9475e52dc343a9-Paper-Conference.pdf"},{"title":"Learning Temporally Extended Skills in Continuous Domains ...","url":"https://proceedings.mlr.press/v205/achterhold23a/achterhold23a.pdf"},{"title":"Learning Temporally Extended Skills in Continuous Domains as Symbolic Actions for Planning | Request PDF","url":"https://www.researchgate.net/publication/361923815_Learning_Temporally_Extended_Skills_in_Continuous_Domains_as_Symbolic_Actions_for_Planning?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbH19"}]

I found information about SPlaTES! Based on the search results, here's what I found:

## SPlaTES Overview

SPlaTES (Stable Planning with Temporally Extended Skills) is a method that consists of learning temporally extended skills in tandem with an abstract world model, while using them for model predictive control (MPC).

## Key Components and Features

The method learns temporally extended skills on the lower level and an abstract world model over skill outcomes on the higher level, with both levels being model-based and performing MPC on different timescales.

The skill learning objective yields diverse, predictable, task-related, and error-correcting behavior.

## Performance

Planning over entire episodes enables SPlaTES to outperform competitive model-based and skill-based methods on a range of challenging long-horizon continuous control tasks.

## Advantages

The computational cost of MPC is reduced by a factor of K² compared to planning over the same effective horizon with a low-level model, and the skills are trained to efficiently move through the abstract state space which encodes everything that is crucial for the task.

The paper appears to be from the Reinforcement Learning Journal 2025, presenting this as a method for handling long-horizon continuous control problems through hierarchical skill learning combined with abstract world models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "b32d4a2e-9db7-4e6b-81c1-10a47b65fb15",
  "tool_use_result": {
    "query": "\"SPlaTES\" stable planning temporally extended skills reinforcement learning 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Se6uMDZNwaA5CPi8o7rYqE",
        "content": [
          {
            "title": "Reinforcement Learning Journal 2025 Cover Page",
            "url": "https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"
          },
          {
            "title": "Learning Temporally Extended Skills in Continuous Domains as Symbolic Actions for Planning | seads",
            "url": "https://seads.is.tue.mpg.de/"
          },
          {
            "title": "[2207.05018] Learning Temporally Extended Skills in Continuous Domains as Symbolic Actions for Planning",
            "url": "https://arxiv.org/abs/2207.05018"
          },
          {
            "title": "Learning Temporally Extended Skills in Continuous Domains as Symbolic Actions for Planning | OpenReview",
            "url": "https://openreview.net/forum?id=t-IO7wCaNgH"
          },
          {
            "title": "Temporally extended successor feature neural episodic control | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-024-65687-w"
          },
          {
            "title": "LLMs augmented hierarchical reinforcement learning with action primitives for long-horizon manipulation tasks | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-20653-y"
          },
          {
            "title": "Multi-Turn Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/multi-turn-reinforcement-learning-mt-rl"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/7c8c0db90a14c7a2db9475e52dc343a9-Paper-Conference.pdf"
          },
          {
            "title": "Learning Temporally Extended Skills in Continuous Domains ...",
            "url": "https://proceedings.mlr.press/v205/achterhold23a/achterhold23a.pdf"
          },
          {
            "title": "Learning Temporally Extended Skills in Continuous Domains as Symbolic Actions for Planning | Request PDF",
            "url": "https://www.researchgate.net/publication/361923815_Learning_Temporally_Extended_Skills_in_Continuous_Domains_as_Symbolic_Actions_for_Planning?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbH19"
          }
        ]
      },
      "I found information about SPlaTES! Based on the search results, here's what I found:\n\n## SPlaTES Overview\n\nSPlaTES (Stable Planning with Temporally Extended Skills) is a method that consists of learning temporally extended skills in tandem with an abstract world model, while using them for model predictive control (MPC).\n\n## Key Components and Features\n\nThe method learns temporally extended skills on the lower level and an abstract world model over skill outcomes on the higher level, with both levels being model-based and performing MPC on different timescales.\n\nThe skill learning objective yields diverse, predictable, task-related, and error-correcting behavior.\n\n## Performance\n\nPlanning over entire episodes enables SPlaTES to outperform competitive model-based and skill-based methods on a range of challenging long-horizon continuous control tasks.\n\n## Advantages\n\nThe computational cost of MPC is reduced by a factor of K² compared to planning over the same effective horizon with a low-level model, and the skills are trained to efficiently move through the abstract state space which encodes everything that is crucial for the task.\n\nThe paper appears to be from the Reinforcement Learning Journal 2025, presenting this as a method for handling long-horizon continuous control problems through hierarchical skill learning combined with abstract world models."
    ],
    "durationSeconds": 6.297406854000001
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-18T13:59:32.323Z_

<details><summary>↩ Tool result · `toolu_011wsRic4hLoUz4DkpVuPBdg`</summary>

```text
Web search results for query: ""Diffusion World Model" offline reinforcement learning step-by-step rollout 2024"

Links: [{"title":"[2402.03570] Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning","url":"https://arxiv.org/abs/2402.03570"},{"title":"Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240203570D/abstract"},{"title":"Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning - DEV Community","url":"https://dev.to/aimodels-fyi/diffusion-world-model-future-modeling-beyond-step-by-step-rollout-for-offline-reinforcement-learning-o66"},{"title":"Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning","url":"https://arxiv.org/html/2402.03570v3"},{"title":"Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2402.03570v4"},{"title":"World model-driven process industry operations: An offline reinforcement learning solution based on conditional diffusion - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0166361526000096"},{"title":"Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/diffusion-world-model-future-modeling-beyond-step"},{"title":"[Literature Review] Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning","url":"https://www.themoonlight.io/en/review/diffusion-world-model-future-modeling-beyond-step-by-step-rollout-for-offline-reinforcement-learning"},{"title":"RLJ | RLC 2024 Policy-Guided Diffusion Matthew T. Jackson∗ Michael T. Matthews","url":"https://rlj.cs.umass.edu/2024/papers/RLJ_RLC_2024_233.pdf"},{"title":"Diffusion World Models | OpenReview","url":"https://openreview.net/forum?id=bAXmvOLtjA"}]

Based on the search results, I found comprehensive information about the Diffusion World Model research. Here's what the search revealed:

## Key Research Paper

The Diffusion World Model (DWM) is a conditional diffusion model capable of predicting multistep future states and rewards concurrently. As opposed to traditional one-step dynamics models, DWM offers long-horizon predictions in a single forward pass, eliminating the need for recursive queries.

## Core Problem It Addresses

Traditional model-based reinforcement learning (MBRL) approaches suffer from a fundamental limitation known as the "compounding error problem." When using one-step dynamics models to predict future states and rewards, errors accumulate rapidly during recursive rollouts, causing performance to degrade severely as the simulation horizon increases.

## How It Works

DWM uses a conditional diffusion model to predict multiple future states and rewards concurrently. This single-forward-pass prediction aims to alleviate the compounding errors inherent in recursive, step-by-step predictions.

## Performance Results

In terms of absolute performance, DWM significantly surpasses one-step dynamics models with a 44% performance gain, and is comparable to or slightly surpassing their model-free counterparts. Experiments on the D4RL dataset confirm the robustness of DWM to long-horizon simulation.

## Application in Offline RL

DWM is integrated into model-based value estimation, where the short-term return is simulated by future trajectories sampled from DWM. In the context of offline reinforcement learning, DWM can be viewed as a conservative value regularization through generative modeling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "3c633f40-afab-459c-b151-7bd677aa34ad",
  "tool_use_result": {
    "query": "\"Diffusion World Model\" offline reinforcement learning step-by-step rollout 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FZV7MzekSnWyQsA81zW6vR",
        "content": [
          {
            "title": "[2402.03570] Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning",
            "url": "https://arxiv.org/abs/2402.03570"
          },
          {
            "title": "Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240203570D/abstract"
          },
          {
            "title": "Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning - DEV Community",
            "url": "https://dev.to/aimodels-fyi/diffusion-world-model-future-modeling-beyond-step-by-step-rollout-for-offline-reinforcement-learning-o66"
          },
          {
            "title": "Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning",
            "url": "https://arxiv.org/html/2402.03570v3"
          },
          {
            "title": "Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2402.03570v4"
          },
          {
            "title": "World model-driven process industry operations: An offline reinforcement learning solution based on conditional diffusion - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0166361526000096"
          },
          {
            "title": "Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/diffusion-world-model-future-modeling-beyond-step"
          },
          {
            "title": "[Literature Review] Diffusion World Model: Future Modeling Beyond Step-by-Step Rollout for Offline Reinforcement Learning",
            "url": "https://www.themoonlight.io/en/review/diffusion-world-model-future-modeling-beyond-step-by-step-rollout-for-offline-reinforcement-learning"
          },
          {
            "title": "RLJ | RLC 2024 Policy-Guided Diffusion Matthew T. Jackson∗ Michael T. Matthews",
            "url": "https://rlj.cs.umass.edu/2024/papers/RLJ_RLC_2024_233.pdf"
          },
          {
            "title": "Diffusion World Models | OpenReview",
            "url": "https://openreview.net/forum?id=bAXmvOLtjA"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the Diffusion World Model research. Here's what the search revealed:\n\n## Key Research Paper\n\nThe Diffusion World Model (DWM) is a conditional diffusion model capable of predicting multistep future states and rewards concurrently. As opposed to traditional one-step dynamics models, DWM offers long-horizon predictions in a single forward pass, eliminating the need for recursive queries.\n\n## Core Problem It Addresses\n\nTraditional model-based reinforcement learning (MBRL) approaches suffer from a fundamental limitation known as the \"compounding error problem.\" When using one-step dynamics models to predict future states and rewards, errors accumulate rapidly during recursive rollouts, causing performance to degrade severely as the simulation horizon increases.\n\n## How It Works\n\nDWM uses a conditional diffusion model to predict multiple future states and rewards concurrently. This single-forward-pass prediction aims to alleviate the compounding errors inherent in recursive, step-by-step predictions.\n\n## Performance Results\n\nIn terms of absolute performance, DWM significantly surpasses one-step dynamics models with a 44% performance gain, and is comparable to or slightly surpassing their model-free counterparts. Experiments on the D4RL dataset confirm the robustness of DWM to long-horizon simulation.\n\n## Application in Offline RL\n\nDWM is integrated into model-based value estimation, where the short-term return is simulated by future trajectories sampled from DWM. In the context of offline reinforcement learning, DWM can be viewed as a conservative value regularization through generative modeling."
    ],
    "durationSeconds": 7.324233517000001
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-18T13:59:36.220Z_

<details><summary>↩ Tool result · `toolu_01KeG791zuuXQQctQ64SxpPa`</summary>

```text
Web search results for query: ""learning world models hierarchical temporal abstractions probabilistic" 2024"

Links: [{"title":"[2404.16078] Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective","url":"https://arxiv.org/abs/2404.16078"},{"title":"ICLR Poster Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics","url":"https://iclr.cc/virtual/2024/poster/18558"},{"title":"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | OpenReview","url":"https://openreview.net/forum?id=TjCDNssXKU"},{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"},{"title":"Exploring the limits of hierarchical world models in reinforcement learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-76719-w"},{"title":"GitHub - CognitiveModeling/THICK · GitHub","url":"https://github.com/CognitiveModeling/THICK"},{"title":"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | Autonomous Learning – MPI-IS","url":"https://is.mpg.de/al/publications/gumbsch2024-thickworldmodels"},{"title":"Hierarchical Model-Based Reinforcement Learning with Temporal Abstractions | Open Research Commons","url":"https://bcommons.berkeley.edu/hierarchical-model-based-reinforcement-learning-temporal-abstractions"},{"title":"Exploring the limits of hierarchical world models in reinforcement learning - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11538428/"},{"title":"GitHub - GuochenZhou/World-Model: A paper list of world model","url":"https://github.com/GuochenZhou/World-Model"}]

I found several relevant results for your search on learning world models with hierarchical temporal abstractions and probabilistic approaches in 2024. Here are the key findings:

## Main 2024 Research

Hierarchical world models can significantly improve model-based reinforcement learning (MBRL) and planning by enabling reasoning across multiple time scales, with the THICK algorithm learning a world model hierarchy via discrete latent dynamics.

The THICK architecture adaptively discovers higher-level time scales by guiding the lower-level world model to update parts of its latent state only sparsely in time, with the high-level model then trained to predict scenarios involving changes in these low-level latent states.

## Probabilistic Formalism Work

Research titled "Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective" addresses the challenge of devising formalisms to develop internal world models that accurately reflect causal hierarchies in real-world dynamics, proposing Hidden-Parameter SSMs and Multi-Time Scale SSMs to address limitations with state space models.

## Hierarchical MBRL Framework

Another 2024 approach presents an HMBRL framework consisting of a hierarchical world model with a hierarchy of agents trained using simulated data, constructing hierarchical world models that simulate the environment at various levels of temporal abstraction, with models used to train agents that communicate top-down by proposing goals.

These papers represent significant advances in combining hierarchical structures with temporal abstractions for more efficient and scalable world models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "bac31ad9-26c7-4835-a1c8-aa1054364942",
  "tool_use_result": {
    "query": "\"learning world models hierarchical temporal abstractions probabilistic\" 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JdbtzsNaU8mjAbf8cLBTEb",
        "content": [
          {
            "title": "[2404.16078] Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective",
            "url": "https://arxiv.org/abs/2404.16078"
          },
          {
            "title": "ICLR Poster Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics",
            "url": "https://iclr.cc/virtual/2024/poster/18558"
          },
          {
            "title": "Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | OpenReview",
            "url": "https://openreview.net/forum?id=TjCDNssXKU"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"
          },
          {
            "title": "Exploring the limits of hierarchical world models in reinforcement learning | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-024-76719-w"
          },
          {
            "title": "GitHub - CognitiveModeling/THICK · GitHub",
            "url": "https://github.com/CognitiveModeling/THICK"
          },
          {
            "title": "Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | Autonomous Learning – MPI-IS",
            "url": "https://is.mpg.de/al/publications/gumbsch2024-thickworldmodels"
          },
          {
            "title": "Hierarchical Model-Based Reinforcement Learning with Temporal Abstractions | Open Research Commons",
            "url": "https://bcommons.berkeley.edu/hierarchical-model-based-reinforcement-learning-temporal-abstractions"
          },
          {
            "title": "Exploring the limits of hierarchical world models in reinforcement learning - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11538428/"
          },
          {
            "title": "GitHub - GuochenZhou/World-Model: A paper list of world model",
            "url": "https://github.com/GuochenZhou/World-Model"
          }
        ]
      },
      "I found several relevant results for your search on learning world models with hierarchical temporal abstractions and probabilistic approaches in 2024. Here are the key findings:\n\n## Main 2024 Research\n\nHierarchical world models can significantly improve model-based reinforcement learning (MBRL) and planning by enabling reasoning across multiple time scales, with the THICK algorithm learning a world model hierarchy via discrete latent dynamics.\n\nThe THICK architecture adaptively discovers higher-level time scales by guiding the lower-level world model to update parts of its latent state only sparsely in time, with the high-level model then trained to predict scenarios involving changes in these low-level latent states.\n\n## Probabilistic Formalism Work\n\nResearch titled \"Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective\" addresses the challenge of devising formalisms to develop internal world models that accurately reflect causal hierarchies in real-world dynamics, proposing Hidden-Parameter SSMs and Multi-Time Scale SSMs to address limitations with state space models.\n\n## Hierarchical MBRL Framework\n\nAnother 2024 approach presents an HMBRL framework consisting of a hierarchical world model with a hierarchy of agents trained using simulated data, constructing hierarchical world models that simulate the environment at various levels of temporal abstraction, with models used to train agents that communicate top-down by proposing goals.\n\nThese papers represent significant advances in combining hierarchical structures with temporal abstractions for more efficient and scalable world models."
    ],
    "durationSeconds": 7.526969637999995
  }
}
```

</details>

---

### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture. Let me compile the analysis report. Let me first catalog all the papers currently cited in the related work, then identify which important recent papers are missing.

Currently cited papers in related_work.tex:
1. sutton1999options - Options framework
2. sharma2017figar - FiGAR
3. biedenkapp2021temporl - TempoRL
4. lakshminarayanan2017dynamic - Dynamic action repetition
5. hafner2020dreamerv1 - DreamerV1


6. hafner2021dreamerv2 - DreamerV2
7. hafner2023dreamerv3 - DreamerV3
8. micheli2023iris - IRIS
9. robine2023twm - TWM
10. hafner2025dreamerv4 - DreamerV4 (Training Agents Inside of Scalable World Models)
11. gumbsch2024thick - THICK
12. mattes2024hieros - Hieros
13. li2025lsimagine - LS-Imagine
14. shaj2023mts3 - MTS3

Now I'm continuing through the list of papers to get a complete picture of what's already included. Continuing through the bibliography, I'm adding more recent papers on model-based RL challenges like diminishing returns from value expansion, the importance of rollouts, and various forms of neural network degradation like plasticity loss and primacy bias. I'm also including foundational papers on implementation details and what actually matters in deep RL. Then I'm noting which papers are in the bibliography but haven't been cited in the related work section yet, though they may appear elsewhere in the document. I'm adding a few more recent papers to the bibliography and then cross-checking which important 2024-2025 papers on world models and temporal abstraction are still missing from the file. I'm finding a few more critical papers I need to add—particularly one from ICML 2024 that directly connects overestimation with plasticity issues in actor-critic methods, and another recent work on value overestimation in TD-MPC. I'm also tracking down the complete list of DreamerV3 variants to make sure I haven't missed any key citations. Checking the TAWM citation now—the bibliography entry matches what I found: Anh N. Nhu, Sanghyun Son, and Ming C. Lin published at ICML 2025, with the arXiv preprint 2506.08441. Now I need to look at the SPlaTES entry, which has a suspicious placeholder-style author field that needs fixing.

Let me identify the most critical papers to add to the document. The Nauman et al. paper from ICML 2024 on overestimation, overfitting, and plasticity in actor-critic methods is directly relevant—it connects to both the value overestimation discussion and the network capacity section, and their findings about regularization align with CIVO's approach.

TD-M(PC)² is important because TAWM builds on TD-MPC2, and this paper demonstrates that overestimation occurs in TD-MPC2 as well, just manifesting differently due to replanning from real states. The plasticity loss papers are worth including too—the NeurIPS 2024 study extends plasticity understanding to on-policy methods, and the recent ICML 2025 paper on mitigating plasticity loss through churn reduction is timely, though the survey might be less critical than the empirical studies.

MuDreamer and DWM are more tangential—MuDreamer's removal of reconstruction loss relates to the gradient decomposition discussion, while DWM addresses compounding error through diffusion-based prediction. I think I have enough to compile the report now, so let me organize these by how directly they support the paper's core arguments. I'm checking whether lenz2025macura is already in the bibliography but missing from the related work section—it is, though that's separate from the main task of identifying gaps. The real question is what 2024-2025 papers should be cited in related work given the paper's focus on temporal abstraction, value overestimation, and compounding error. The most notable missing piece is Nauman et al.'s ICML 2024 work on overestimation and plasticity in actor-critic methods. I'm wrapping up the analysis and ready to compile the final report with these key missing citations identified.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "c6e76881-9fb4-468d-8669-7f9257d043db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rztpo9sSqrG8cLKLioZc3s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4298,
      "cache_read_input_tokens": 54517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4298
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

_source line 69_

搜索完成。现在编译分析报告。

---

## 已引用论文清单

**Temporal Abstraction 段落 (14篇):**
- Sutton et al. 1999 (Options framework)
- Sharma et al. 2017 (FiGAR)
- Biedenkapp et al. 2021 (TempoRL)
- Lakshminarayanan et al. 2017 (Dynamic action repetition)
- Hafner et al. 2020/2021/2023/2025 (DreamerV1/V2/V3/V4)
- Micheli et al. 2023 (IRIS)
- Robine et al. 2023 (TWM)
- Gumbsch et al. 2024 (THICK)
- Mattes et al. 2024 (Hieros)
- Li et al. 2025 (LS-Imagine)
- Shaj et al. 2023 (MTS3)

**TAWM 段落 (2篇):**
- Nhu et al. 2025 (TAWM)
- Hansen et al. 2024 (TD-MPC2)

**Value Overestimation 段落 (10篇):**
- Thrun & Schwartz 1993, van Hasselt et al. 2016 (Double Q), Fujimoto et al. 2018 (TD3), Haarnoja et al. 2018 (SAC), Chen et al. 2021 (REDQ)
- Janner et al. 2019 (MBPO), Yu et al. 2020 (MOPO), Lu et al. 2018 (Non-delusional)
- Tallec et al. 2019 (Time discretization)

**Model Fidelity 段落 (5篇):**
- Lambert et al. 2020 (Objective mismatch), Asadi et al. 2019, Lambert et al. 2022 (Compounding error)
- Ma et al. 2024 (HarmonyDream)
- Palenicek et al. 2025, Frauenknecht et al. 2025 (Rollout diminishing returns)

**Network Capacity 段落 (5篇):**
- Nikishin et al. 2022 (Primacy bias), Lyle et al. 2022 (Capacity loss), Nikishin et al. 2023 (Plasticity injection)
- Henderson et al. 2018, Engstrom et al. 2020, Andrychowicz et al. 2021

---

## 搜索发现的相关但未引用论文

### 直接相关（建议添加）

**1. Nauman et al., "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning" (ICML 2024)**
- 相关性: **直接相关**
- 与本文关系: 系统性研究 overestimation、overfitting、plasticity loss 三者的耦合关系。对 60+ off-policy agent 进行消融实验，发现适当 regularization 同时缓解三个问题。这与本文将 CIVO（value overestimation）和 seed-dependent divergence（plasticity/capacity）联系起来的分析高度吻合。审稿人极有可能要求引用此文。
- 建议添加位置: **Value Overestimation 段落**末尾或 **Network Capacity 段落**，作为连接 overestimation 与 plasticity 的桥梁文献。

**2. TD-M(PC)² (2025, arXiv 2502.03550)**
- 相关性: **直接相关**
- 与本文关系: 发现并证明 TD-MPC2 中 planner 和 learned policy prior 之间的 structural policy mismatch 导致持续性 value overestimation。由于 TAWM 基于 TD-MPC2，而本文的核心对比就是 TAWM（MPC re-planning）vs DreamerV3（imagination loop）在 overestimation 上的差异，该工作提供了 TD-MPC2 一侧 overestimation 机制的详细分析，有力支撑本文的 "MPC re-plans from real states so errors don't compound into critic" 的论点。
- 建议添加位置: **TAWM 段落**，在讨论 TAWM 与 DreamerV3 架构差异时引用。

**3. "A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning" (NeurIPS 2024)**
- 相关性: **直接相关**
- 与本文关系: 已引用 Nikishin 2022/2023 和 Lyle 2022，但缺少 2024 NeurIPS 上的最新 plasticity 研究。该文将 plasticity loss 研究从 off-policy 扩展到 on-policy 场景，提供更全面的理论视角。
- 建议添加位置: **Network Capacity 段落**，与 Nikishin 2022/2023 并列。

**4. "Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn" (ICML 2025)**
- 相关性: **直接相关**
- 与本文关系: 通过 Neural Tangent Kernel (NTK) 矩阵的 rank 下降解释 plasticity loss 的机制，提出 churn 作为 plasticity loss 的直接度量。为本文的 seed-dependent CIVO 现象提供了更精细的机制解释。
- 建议添加位置: **Network Capacity 段落**。

### 间接相关（可考虑添加）

**5. MuDreamer (Burchi & Timofte, arXiv 2024)**
- 相关性: 间接相关
- 与本文关系: 移除 DreamerV3 的 pixel reconstruction loss，改用 value function + action prediction。与本文 gradient decomposition 中 observation decoder channel 只占 16-22% 但承载关键 Δt spatial information 的发现形成有趣对照：如果去掉 reconstruction，Δt conditioning 的信息传播路径会完全不同。
- 建议添加位置: **Temporal Abstraction 段落**，作为 DreamerV3 变体之一提及。

**6. "Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective" (arXiv 2404.16078)**
- 相关性: 间接相关
- 与本文关系: 从概率角度形式化分层时间抽象 world model，提出 Hidden-Parameter SSMs 和 Multi-Time Scale SSMs。已引用 THICK 和 MTS3，此文是同方向的理论补充。
- 建议添加位置: **Temporal Abstraction 段落**，与 THICK 和 MTS3 并列。

**7. Diffusion World Model (DWM, arXiv 2024)**
- 相关性: 间接相关
- 与本文关系: 用 diffusion model 一次性预测多步未来状态，回避 step-by-step rollout 的 compounding error。与本文 compounding error 段落讨论的问题直接相关，但方法路线完全不同（offline RL）。
- 建议添加位置: **Model Fidelity 段落**，可一句话提及作为非自回归方案对比。

**8. MACURA / Lenz et al. 2025 "Trust the Model Where It Trusts Itself"**
- 相关性: 间接相关
- 与本文关系: 基于模型不确定性自适应调整 rollout 长度。已在 bib 中（lenz2025macura），但未在 related work 引用。与 Frauenknecht et al. 2025 主题接近。
- 建议添加位置: **Model Fidelity 段落**，与 Frauenknecht et al. 并列。

---

## TAWM 引用验证

当前 bib 条目：
```bibtex
@inproceedings{nhu2025tawm,
  title = {Time-Aware World Model for Adaptive Prediction and Control},
  author = {Nhu, A.N and Son, S and Lin, M.C},
  year = {2025},
  booktitle = {International Conference on Machine Learning},
  eprint = {2506.08441},
  archivePrefix = {arXiv},
}
```

验证结果：
- **Title**: 正确 ✓
- **Authors**: Anh N. Nhu, Sanghyun Son, Ming C. Lin (University of Maryland) ✓
- **Venue**: ICML 2025 ✓ (已通过 OpenReview 和 ICML 2025 schedule 确认)
- **arXiv ID**: 2506.08441 ✓
- **Year**: 2025 ✓

TAWM 引用信息全部准确，无需修改。

---

## 总结建议

**必须添加（2篇）：**
1. **Nauman et al. (ICML 2024)** — 审稿人最可能指出的遗漏。该文是 2024 年 overestimation + plasticity 交叉研究的标杆，与本文横跨 Value Overestimation 和 Network Capacity 两个段落的主题高度重合。
2. **TD-M(PC)² (2025)** — 本文花了整段讨论 TAWM/TD-MPC2 vs DreamerV3 的架构对比，引用在 TD-MPC2 上发现 overestimation 问题的最新工作能强化论证。

**强烈建议添加（2篇）：**
3. **NeurIPS 2024 plasticity study** — 补全 plasticity 文献的时效性
4. **ICML 2025 churn-based plasticity** — 最新 plasticity 机制研究

**可选添加（4篇）：**
5-8. MuDreamer、Probabilistic hierarchical WM、DWM、MACURA — 根据页数空间决定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "uuid": "46539639-6930-4239-bff7-c8859d24a8c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rztpo9sSqrG8cLKLioZc3s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4298,
      "cache_read_input_tokens": 54517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4298
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

### Task result

_source line 70_

搜索完成。现在编译分析报告。

---

## 已引用论文清单

**Temporal Abstraction 段落 (14篇):**
- Sutton et al. 1999 (Options framework)
- Sharma et al. 2017 (FiGAR)
- Biedenkapp et al. 2021 (TempoRL)
- Lakshminarayanan et al. 2017 (Dynamic action repetition)
- Hafner et al. 2020/2021/2023/2025 (DreamerV1/V2/V3/V4)
- Micheli et al. 2023 (IRIS)
- Robine et al. 2023 (TWM)
- Gumbsch et al. 2024 (THICK)
- Mattes et al. 2024 (Hieros)
- Li et al. 2025 (LS-Imagine)
- Shaj et al. 2023 (MTS3)

**TAWM 段落 (2篇):**
- Nhu et al. 2025 (TAWM)
- Hansen et al. 2024 (TD-MPC2)

**Value Overestimation 段落 (10篇):**
- Thrun & Schwartz 1993, van Hasselt et al. 2016 (Double Q), Fujimoto et al. 2018 (TD3), Haarnoja et al. 2018 (SAC), Chen et al. 2021 (REDQ)
- Janner et al. 2019 (MBPO), Yu et al. 2020 (MOPO), Lu et al. 2018 (Non-delusional)
- Tallec et al. 2019 (Time discretization)

**Model Fidelity 段落 (5篇):**
- Lambert et al. 2020 (Objective mismatch), Asadi et al. 2019, Lambert et al. 2022 (Compounding error)
- Ma et al. 2024 (HarmonyDream)
- Palenicek et al. 2025, Frauenknecht et al. 2025 (Rollout diminishing returns)

**Network Capacity 段落 (5篇):**
- Nikishin et al. 2022 (Primacy bias), Lyle et al. 2022 (Capacity loss), Nikishin et al. 2023 (Plasticity injection)
- Henderson et al. 2018, Engstrom et al. 2020, Andrychowicz et al. 2021

---

## 搜索发现的相关但未引用论文

### 直接相关（建议添加）

**1. Nauman et al., "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning" (ICML 2024)**
- 相关性: **直接相关**
- 与本文关系: 系统性研究 overestimation、overfitting、plasticity loss 三者的耦合关系。对 60+ off-policy agent 进行消融实验，发现适当 regularization 同时缓解三个问题。这与本文将 CIVO（value overestimation）和 seed-dependent divergence（plasticity/capacity）联系起来的分析高度吻合。审稿人极有可能要求引用此文。
- 建议添加位置: **Value Overestimation 段落**末尾或 **Network Capacity 段落**，作为连接 overestimation 与 plasticity 的桥梁文献。

**2. TD-M(PC)² (2025, arXiv 2502.03550)**
- 相关性: **直接相关**
- 与本文关系: 发现并证明 TD-MPC2 中 planner 和 learned policy prior 之间的 structural policy mismatch 导致持续性 value overestimation。由于 TAWM 基于 TD-MPC2，而本文的核心对比就是 TAWM（MPC re-planning）vs DreamerV3（imagination loop）在 overestimation 上的差异，该工作提供了 TD-MPC2 一侧 overestimation 机制的详细分析，有力支撑本文的 "MPC re-plans from real states so errors don't compound into critic" 的论点。
- 建议添加位置: **TAWM 段落**，在讨论 TAWM 与 DreamerV3 架构差异时引用。

**3. "A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning" (NeurIPS 2024)**
- 相关性: **直接相关**
- 与本文关系: 已引用 Nikishin 2022/2023 和 Lyle 2022，但缺少 2024 NeurIPS 上的最新 plasticity 研究。该文将 plasticity loss 研究从 off-policy 扩展到 on-policy 场景，提供更全面的理论视角。
- 建议添加位置: **Network Capacity 段落**，与 Nikishin 2022/2023 并列。

**4. "Mitigating Plasticity Loss in Continual Reinforcement Learning by Reducing Churn" (ICML 2025)**
- 相关性: **直接相关**
- 与本文关系: 通过 Neural Tangent Kernel (NTK) 矩阵的 rank 下降解释 plasticity loss 的机制，提出 churn 作为 plasticity loss 的直接度量。为本文的 seed-dependent CIVO 现象提供了更精细的机制解释。
- 建议添加位置: **Network Capacity 段落**。

### 间接相关（可考虑添加）

**5. MuDreamer (Burchi & Timofte, arXiv 2024)**
- 相关性: 间接相关
- 与本文关系: 移除 DreamerV3 的 pixel reconstruction loss，改用 value function + action prediction。与本文 gradient decomposition 中 observation decoder channel 只占 16-22% 但承载关键 Δt spatial information 的发现形成有趣对照：如果去掉 reconstruction，Δt conditioning 的信息传播路径会完全不同。
- 建议添加位置: **Temporal Abstraction 段落**，作为 DreamerV3 变体之一提及。

**6. "Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective" (arXiv 2404.16078)**
- 相关性: 间接相关
- 与本文关系: 从概率角度形式化分层时间抽象 world model，提出 Hidden-Parameter SSMs 和 Multi-Time Scale SSMs。已引用 THICK 和 MTS3，此文是同方向的理论补充。
- 建议添加位置: **Temporal Abstraction 段落**，与 THICK 和 MTS3 并列。

**7. Diffusion World Model (DWM, arXiv 2024)**
- 相关性: 间接相关
- 与本文关系: 用 diffusion model 一次性预测多步未来状态，回避 step-by-step rollout 的 compounding error。与本文 compounding error 段落讨论的问题直接相关，但方法路线完全不同（offline RL）。
- 建议添加位置: **Model Fidelity 段落**，可一句话提及作为非自回归方案对比。

**8. MACURA / Lenz et al. 2025 "Trust the Model Where It Trusts Itself"**
- 相关性: 间接相关
- 与本文关系: 基于模型不确定性自适应调整 rollout 长度。已在 bib 中（lenz2025macura），但未在 related work 引用。与 Frauenknecht et al. 2025 主题接近。
- 建议添加位置: **Model Fidelity 段落**，与 Frauenknecht et al. 并列。

---

## TAWM 引用验证

当前 bib 条目：
```bibtex
@inproceedings{nhu2025tawm,
  title = {Time-Aware World Model for Adaptive Prediction and Control},
  author = {Nhu, A.N and Son, S and Lin, M.C},
  year = {2025},
  booktitle = {International Conference on Machine Learning},
  eprint = {2506.08441},
  archivePrefix = {arXiv},
}
```

验证结果：
- **Title**: 正确 ✓
- **Authors**: Anh N. Nhu, Sanghyun Son, Ming C. Lin (University of Maryland) ✓
- **Venue**: ICML 2025 ✓ (已通过 OpenReview 和 ICML 2025 schedule 确认)
- **arXiv ID**: 2506.08441 ✓
- **Year**: 2025 ✓

TAWM 引用信息全部准确，无需修改。

---

## 总结建议

**必须添加（2篇）：**
1. **Nauman et al. (ICML 2024)** — 审稿人最可能指出的遗漏。该文是 2024 年 overestimation + plasticity 交叉研究的标杆，与本文横跨 Value Overestimation 和 Network Capacity 两个段落的主题高度重合。
2. **TD-M(PC)² (2025)** — 本文花了整段讨论 TAWM/TD-MPC2 vs DreamerV3 的架构对比，引用在 TD-MPC2 上发现 overestimation 问题的最新工作能强化论证。

**强烈建议添加（2篇）：**
3. **NeurIPS 2024 plasticity study** — 补全 plasticity 文献的时效性
4. **ICML 2025 churn-based plasticity** — 最新 plasticity 机制研究

**可选添加（4篇）：**
5-8. MuDreamer、Probabilistic hierarchical WM、DWM、MACURA — 根据页数空间决定

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 194621,
  "duration_api_ms": 324505,
  "num_turns": 27,
  "stop_reason": "end_turn",
  "session_id": "deaea69b-fade-4d43-8dcc-a54c104b8c62",
  "total_cost_usd": 1.2868659999999998,
  "usage": {
    "input_tokens": 1814,
    "cache_creation_input_tokens": 47368,
    "cache_read_input_tokens": 278510,
    "output_tokens": 7919,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 47368,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 6058,
        "cache_read_input_tokens": 54517,
        "cache_creation_input_tokens": 4298,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4298
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 368136,
      "outputTokens": 11276,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 22,
      "costUSD": 0.6445159999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1814,
      "outputTokens": 7919,
      "cacheReadInputTokens": 278510,
      "cacheCreationInputTokens": 47368,
      "webSearchRequests": 0,
      "costUSD": 0.64235,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8afc1465-995f-4c61-9138-31fdefff6f05"
}
```

</details>

---
